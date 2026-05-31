"""
kachman_lib.py — shared physics for the Kachman 2017 reference impl
                 and the stochastic-drive extension (kachman_stochastic.py).

This library contains the model physics that is invariant across both
scripts: stiffness matrix, steady-state mechanics, catch/snap rates,
Gillespie loop, normal-mode spectrum sampling, ensemble averaging, and
the matplotlib plotting helper.

The PHYSICS belongs to Kachman, Owen & England 2017 (PRL 119, 038001 +
supplemental). The CODE is a clean-room reimplementation per the supp's
equations; verified to reproduce Fig S8 qualitatively under ensemble
averaging at N_SEEDS = 5.

Consumers:
  kachman.py            — deterministic single-sinusoid drive (paper repro)
  kachman_stochastic.py — stochastic drive (the Still-applicable variant
                          where I_pred / I_mem become well-defined)
"""

import os
import numpy as np
from scipy.special import ive  # exp-scaled modified Bessel: ive(0, x) = exp(-x) * I_0(x)
                                # numerically stable for the large-stretch regime where
                                # exp(-x) underflows and I_0(x) overflows separately.

import matplotlib
matplotlib.use("Agg")           # non-interactive backend; we save PNGs, don't draw to a screen
import matplotlib.pyplot as plt


# ============================================================================
# Parameters (supp p7 — the values Kachman used for the published figures)
# ============================================================================

# Pinned in the supp:
BETA    = 4000.0     # inverse temperature (kT very small vs k)
EPSILON = 0.0001     # bond depth (per supp p7 as stated)
B       = 0.01       # damping
M       = 1.0        # particle mass
K       = 1.0        # spring stiffness (bonded particles)
F       = 10.0       # drive amplitude on the driven particle
OMEGA_D = 1.5        # drive frequency (the Fig S8 value; main text sweeps this)

# NOT pinned in the supp — defaults are reasonable guesses, revise from main
# text figure captions:
N       = 20         # number of particles (Quanta 2017 reports "20 particles")
K_0     = 0.01       # weak confining potential constant (small relative to k)
I_DRIVE = 0          # which particle gets the drive (any one; pick index 0)
R_0     = 1.0        # Arrhenius rate prefactor (sets the time scale; supp leaves implicit)

N_STEPS = 10_000     # Gillespie steps per trajectory (supp says ~10^4 typical)

# Snap-bond parameter (supp p13 — "qualitative results not finely sensitive";
# Kachman et al. do not pin a value because they did not non-dimensionalize.
# β_snap = 6.0 chosen empirically to give a Fig S8-like spectrum: visible
# avoidance dip at ω_d and slight rightward shift of the haystack tail vs
# undriven. Strict quantitative match to the paper's snap bell requires
# parameters Kachman did not publish.)
BETA_SNAP = 6.0
N_THETA_SNAP = 200   # quadrature samples for the drive-cycle average in snap_rates

N_SEEDS = 5          # independent trajectories per regime for ensemble averaging
                     # (smoothness AND robustness check: persistent features should
                     # survive across seeds, fluke features won't)


# ============================================================================
# Phase 1a — mechanics: steady-state oscillation amplitudes for a fixed A
# ============================================================================

def stiffness_matrix(A, k=K, k_0=K_0):
    """Build the stiffness matrix for a given bond network A.

    The system's potential energy at displacements x is
        E(x) = (1/2) k_0 Σ_i x_i^2  +  Σ_{i<j} A_ij (1/2) k (x_i - x_j)^2
    Taking second derivatives gives the stiffness matrix:
        K_stiff[i,i] = k_0 + k * (number of bonds at particle i)
        K_stiff[i,j] = -k        if A[i,j] = 1 (bonded)
        K_stiff[i,j] =  0        otherwise

    Equivalent: K_stiff = k * (graph Laplacian L) + k_0 * I.
    """
    A = np.asarray(A, dtype=float)
    degree = A.sum(axis=1)
    K_stiff = -k * A
    np.fill_diagonal(K_stiff, k * degree + k_0)
    return K_stiff


def steady_state_distances(A, omega=OMEGA_D, F=F, i_drive=I_DRIVE,
                           m=M, b=B, k=K, k_0=K_0):
    """Compute the steady-state oscillation amplitude d_ij of every particle
    pair, given a fixed bond network A and a periodic drive F·sin(ω t) applied
    only at particle i_drive.

    This is the supp p4 calculation. Walk-through, decoded for non-math eyes:

    1.  The system is N coupled damped harmonic oscillators in 1D. Newton:
            m·ẍ + b·ẋ + K_stiff · x = F·sin(ω t) · e_drive
        where e_drive is the unit vector with 1 at index i_drive and 0 elsewhere.

    2.  Diagonalize the stiffness matrix K_stiff. This finds the network's
        "normal modes" — its natural oscillation patterns. Each mode has:
          - an eigenvalue λ_i (proportional to that mode's natural frequency
            squared: ω_i^2 = λ_i / m)
          - an eigenvector u_i (the pattern: which particles move how much
            in this mode)
        The matrix U whose columns are eigenvectors lets us change coords:
            z = U^T x        (normal-mode coordinates)
            x = U z          (particle coordinates)
        and in z-coords the equation decouples — each mode is an independent
        damped driven oscillator.

    3.  Decoupled equation for mode i:
            m·z̈_i + b·ż_i + λ_i z_i = f_i · sin(ω t)
        where f_i = F · U[i_drive, i] is the drive's projection onto mode i
        (how strongly the drive couples to mode i).

    4.  Steady-state complex amplitude of each mode (standard damped-driven
        oscillator solution):
            z_i(t) = (f_i / D_i) · exp(i ω t)
            D_i    = λ_i − m·ω^2 + i·b·ω
        Near resonance (λ_i ≈ m·ω^2), D_i is small → z_i is large. That's the
        physics behind the Kachman result: bond patterns whose normal modes
        resonate with the drive get large-amplitude motion → bonds form and
        break at distinctive rates → those patterns get selected.

    5.  Transform back to particle coordinates: x = U z (still complex).
        Pairwise distance amplitude: d_ij = |x_i − x_j| (magnitude of the
        complex difference). This is the peak excursion in d_ij over one
        drive period.
    """
    K_stiff = stiffness_matrix(A, k=k, k_0=k_0)

    # Step 2: symmetric eigendecomposition (K_stiff = U · diag(λ) · U^T)
    eigenvalues, U = np.linalg.eigh(K_stiff)

    # Step 3: project drive onto each mode (first row of U^T, equivalent to
    # row i_drive of U because U is real-symmetric ⇒ U^T = U.T)
    f_modes = F * U[i_drive, :]    # shape (N,)

    # Step 4: per-mode steady-state complex amplitude
    denom = eigenvalues - m * omega**2 + 1j * b * omega   # shape (N,) complex
    z_modes = f_modes / denom                              # shape (N,) complex

    # Step 5: back-transform to particle coords; take pairwise abs differences
    x_complex = U @ z_modes                                # shape (N,) complex
    d = np.abs(x_complex[:, None] - x_complex[None, :])    # shape (N, N) real
    return d


# ============================================================================
# Phase 1b — bond-event rates (catch + snap)
# ============================================================================

def catch_rates(d_ij, beta=BETA, k=K, epsilon=EPSILON, r_0=R_0):
    """Time-averaged catch-bond formation and breakage rates.

    Closed-form (supp p6) using the identity
        (1/2π) ∫_0^{2π} exp(-α sin^2 θ) dθ = exp(-α/2) · I_0(α/2)
    applied to the drive-cycle average of the instantaneous Arrhenius rates:

        <r_form>  = r_0 · exp(-(1/2)β k d^2) · I_0((1/2)β k d^2)
        <r_break> = r_0 · exp(β ε − (1/4)β k d^2) · I_0((1/4)β k d^2)

    Interpretation: a bond with steady-state stretch amplitude d_ij oscillates
    between fully stretched and unstretched over one drive period; the rate
    of forming (or breaking) it averaged over the cycle has the closed form
    above. Stretched bonds (large d_ij) experience BOTH lower form rates AND
    lower break rates, but break decreases slower than form — so existing
    bonds at large d_ij persist longer (the catch behavior).
    """
    alpha_form  = 0.5  * beta * k * d_ij**2
    alpha_break = 0.25 * beta * k * d_ij**2
    # Use ive(0, α) = exp(-α) · I_0(α) for numerical stability at large α
    # (e.g. an unbonded driven particle pair in the empty-graph initial state
    # can have α ≳ 4·10⁴, where exp and I_0 separately overflow/underflow.)
    r_form  = r_0 *                          ive(0, alpha_form)
    r_break = r_0 * np.exp(beta * epsilon) * ive(0, alpha_break)
    return r_form, r_break


def snap_rates(d_ij, beta=BETA_SNAP, k=K, epsilon=EPSILON, r_0=R_0,
               n_theta=N_THETA_SNAP):
    """Time-averaged snap-bond rates (supp p13).

    The snap barrier function (no harmonic well, just soft repulsion +
    harmonic stretch term that grows quadratically):
        B(x) = (1/2) k x^2 + k · exp(-|x|)

    Unlike catch:
      - Form rate decreases when |x| is small  (repulsion barrier high)
      - Form rate decreases when |x| is large  (harmonic stretch barrier high)
      - Break rate INCREASES with |x|          (no harmonic part — bonds snap
                                                easily once stretched)

    No closed form for the drive-cycle average — integrate numerically over θ:
        <r_form>  = r_0 · (1/2π) ∫₀^{2π} exp(-β [½k(d sin θ)² + k exp(-|d sin θ|)]) dθ
        <r_break> = r_0 · (1/2π) ∫₀^{2π} exp(-β [k exp(-|d sin θ|) - ε]) dθ

    Vectorized: with d_ij shape (N, N) and a θ grid of length n_theta, evaluate
    the integrand on shape (N, N, n_theta) and average along the last axis.
    Uniform sampling on [0, 2π) makes the mean equal to (1/2π) ∫ dθ.
    """
    theta = np.linspace(0.0, 2.0 * np.pi, n_theta, endpoint=False)
    sin_theta = np.sin(theta)                                # (n_theta,)
    x = d_ij[..., None] * sin_theta[None, None, :]           # (N, N, n_theta)
    abs_x = np.abs(x)

    repulsion = k * np.exp(-abs_x)                           # both barriers
    barrier_form  = 0.5 * k * x**2 + repulsion
    barrier_break = repulsion - epsilon

    r_form  = r_0 * np.exp(-beta * barrier_form ).mean(axis=-1)
    r_break = r_0 * np.exp(-beta * barrier_break).mean(axis=-1)
    return r_form, r_break


# ============================================================================
# Phase 1.5a — energy accounting: steady-state absorbed work and dissipated heat
# (for PREDICTION 4a — cumulative-dissipation knee; see kachman.py docstring §7)
# ============================================================================

def steady_state_power(A, omega=OMEGA_D, F_drive=F, i_drive=I_DRIVE,
                       m=M, b=B, k=K, k_0=K_0):
    """Time-averaged absorbed-work and dissipated-heat rates at the steady
    state of the damped-driven oscillator network with fixed bond network A.

    Derivation, following the same chain as steady_state_distances:

      1. Decompose into normal modes (eigendecomp of K_stiff = U diag(λ) U^T).
      2. Per-mode complex amplitude under drive F sin(ωt) at particle i_drive:
              z_i_amp = F · U[i_drive, i] / D_i,    D_i = λ_i − m ω² + i b ω
      3. Per-mode time-averaged dissipated power (Landau & Lifshitz Mechanics
         §25; standard for any linear damped-driven oscillator):
              <P_Q,i> = (1/2) b ω² |z_i_amp|²
      4. Energy balance at steady state (no storage channel in Kachman's setup
         — bonded spring potential is bounded; see spine.md §5 "pure-dissipator
         substrate"):
              <P_W> = <P_Q>     (sum over modes)

    Returns (P_W, P_Q) — both equal at steady state, returned as two values for
    bookkeeping symmetry with H, D in spine.md §2.

    === FILL FROM PAPER === — supp p4 derives the steady-state mechanics but
    not the per-cycle energy budget in closed form. The formula above is
    standard, but verify the b·ω² normalization against the supp's damping
    convention before relying on ABSOLUTE numbers. The knee SHAPE in
    PREDICTION 4a (transient slope vs steady-state slope) is robust to this
    normalization; absolute units are not.

    F_drive = 0 returns (0, 0) — the undriven case has zero steady-state
    absorbed work and zero damping-driven dissipation at this scale.

    Note on redundancy: this duplicates the eigendecomp inside
    steady_state_distances. For a 20×20 matrix this is microseconds and not
    worth refactoring; if the I_pred decomposition ever needs the same z_i
    per Gillespie step, fold the two helpers into one.
    """
    if F_drive == 0:
        return 0.0, 0.0
    K_stiff = stiffness_matrix(A, k=k, k_0=k_0)
    eigenvalues, U = np.linalg.eigh(K_stiff)
    f_modes = F_drive * U[i_drive, :]                          # shape (N,)
    denom = eigenvalues - m * omega**2 + 1j * b * omega        # shape (N,) complex
    z_modes = f_modes / denom
    P_Q = 0.5 * b * omega**2 * float(np.sum(np.abs(z_modes)**2))
    return P_Q, P_Q   # P_W = P_Q at steady state (passive-limit energy balance)


# ============================================================================
# Phase 1c — Gillespie on the graph state space
# ============================================================================

def gillespie_step(A, omega=OMEGA_D, F_drive=F, rng=None, rate_fn=catch_rates):
    """One Gillespie step on the Markov-on-graphs process:
      1. Solve the mechanics at current A → get d_ij for all pairs.
      2. Compute bond-event rates via rate_fn(d_ij) → (r_form, r_break).
      3. For each pair: if currently bonded (A_ij=1), the event is BREAK at
         rate <r_break>(d_ij). If unbonded, the event is FORM at <r_form>(d_ij).
      4. Sample next event time exponentially with total rate.
      5. Sample which event by rate-weighted multinomial.
      6. Flip the bit in A.

    rate_fn lets us swap catch ↔ snap rules cleanly.
    F_drive=0 gives the undriven control (all d_ij=0, all pair rates equal,
    random-graph equilibrium emerges).

    Returns (new_A, dt, event_type, (i, j)).
    """
    if rng is None:
        rng = np.random.default_rng()

    d = steady_state_distances(A, omega=omega, F=F_drive)
    r_form, r_break = rate_fn(d)

    # Per-pair rate: break if currently bonded, form if not
    rates = np.where(A == 1, r_break, r_form)
    # Each unordered pair appears once (upper triangle), no self-events
    rates = np.triu(rates, k=1)

    rate_total = rates.sum()
    if rate_total <= 0 or not np.isfinite(rate_total):
        return A, np.inf, None, None

    dt = rng.exponential(1.0 / rate_total)
    flat = rng.choice(rates.size, p=rates.ravel() / rate_total)
    i, j = np.unravel_index(flat, rates.shape)

    event_type = "break" if A[i, j] == 1 else "form"
    new_A = A.copy()
    new_A[i, j] ^= 1
    new_A[j, i]  = new_A[i, j]   # keep symmetric
    return new_A, dt, event_type, (int(i), int(j))


def run_sim(n_steps=N_STEPS, A_init=None, omega=OMEGA_D, F_drive=F,
            seed=None, spectrum_every=None, rate_fn=catch_rates):
    """Run a Gillespie simulation for up to n_steps events.

    Returns (final_A, trajectory, spectrum) where:
      - trajectory is a list of per-event records:
          {step, t, event, ij, n_bonds, dW, dQ, W_cum, Q_cum}
        dW, dQ = work absorbed / heat dissipated during the interval ending
                 at this event (using the steady-state power of the
                 configuration that was in place BEFORE the event fired,
                 multiplied by dt).
        W_cum, Q_cum = cumulative through this step (joules · time-units of ω).
        At steady state and in the passive limit, dW ≈ dQ per interval and
        W_cum ≈ Q_cum cumulatively (energy balance, no storage channel —
        spine.md §5).

        Energy-accounting caveat: this records the steady-state-power-
        integrated work and heat ONLY. The discrete potential-energy jump
        at each bond form/break event (ΔU into / out of the bond network's
        elastic + bond-depth energy) is NOT yet added. The first-pass knee
        analysis for PREDICTION 4a (spine.md §7) should be robust to this
        omission because dW and dQ track the dominant flow under steady-
        state drive; bond-event ΔU is a refinement to revisit if the knee
        shape comes out ambiguous.
      - spectrum is a list of (dt, frequencies) tuples (empty if
        spectrum_every is None), sampled every spectrum_every steps;
        dt is the time the network spent in this configuration before
        the next event, suitable for occupancy weighting.

    rate_fn selects the bond chemistry: catch_rates (default) or snap_rates.
    """
    rng = np.random.default_rng(seed)
    A = np.zeros((N, N), dtype=int) if A_init is None else A_init.copy()
    t = 0.0
    W_cum = 0.0
    Q_cum = 0.0
    trajectory = []
    spectrum = []
    for step in range(n_steps):
        # Steady-state power for the configuration A IS IN BEFORE this event
        # fires. A stays fixed for the interval of duration dt; energy flows
        # at the steady-state rate during that interval.
        P_W, P_Q = steady_state_power(A, omega=omega, F_drive=F_drive)

        new_A, dt, event_type, ij = gillespie_step(A, omega=omega,
                                                    F_drive=F_drive, rng=rng,
                                                    rate_fn=rate_fn)
        if event_type is None:
            print(f"[step {step}] no events available — stopping.")
            break
        if spectrum_every and step % spectrum_every == 0:
            spectrum.append((dt, normal_mode_frequencies(A)))

        dW = P_W * dt
        dQ = P_Q * dt
        W_cum += dW
        Q_cum += dQ
        t += dt
        A = new_A
        trajectory.append({
            "step":    step,
            "t":       t,
            "event":   event_type,
            "ij":      ij,
            "n_bonds": int(A.sum() // 2),
            "dW":      dW,
            "dQ":      dQ,
            "W_cum":   W_cum,
            "Q_cum":   Q_cum,
        })
    return A, trajectory, spectrum


# ============================================================================
# Spectrum sampling, histograms, ensembles, and plotting
# ============================================================================

def normal_mode_frequencies(A, m=M, k=K, k_0=K_0):
    """Natural frequencies ω_i = √(λ_i/m) of the bond network's normal modes,
    where λ_i are eigenvalues of K_stiff (the stiffness matrix built from A).

    Each bond pattern A has N such frequencies; they collectively form the
    network's "vibrational spectrum." Histogramming these over a long sim
    trajectory (weighted by occupancy time) gives the ensemble distribution
    P(ω) that Fig 2(a) plots.
    """
    K_stiff = stiffness_matrix(A, k=k, k_0=k_0)
    eigenvalues = np.linalg.eigvalsh(K_stiff)            # sorted ascending
    eigenvalues = np.clip(eigenvalues, 0.0, None)        # guard tiny-negative noise
    return np.sqrt(eigenvalues / m)


def spectrum_histogram(samples, n_bins=50, omega_max=3.0):
    """Build an occupancy-weighted histogram of normal-mode frequencies from
    spectrum samples (list of (dt, frequencies) tuples).

    Returns (bin_edges, density) normalized so that Σ density * bin_width = 1.
    """
    bin_edges = np.linspace(0.0, omega_max, n_bins + 1)
    if not samples:
        return bin_edges, np.zeros(n_bins)
    counts = np.zeros(n_bins)
    total_weight = 0.0
    for dt, freqs in samples:
        h, _ = np.histogram(freqs, bins=bin_edges, weights=np.full_like(freqs, dt))
        counts += h
        total_weight += dt * len(freqs)
    bin_width = bin_edges[1] - bin_edges[0]
    return bin_edges, counts / (total_weight * bin_width)


def run_ensemble(n_seeds, base_seed, drop_burn_in=True, **run_sim_kwargs):
    """Run n_seeds independent Gillespie trajectories with the same physics
    parameters and concatenate their spectrum samples.

    Each trajectory uses seed = base_seed + i, producing independent realizations.
    Returns a flat list of (dt, frequencies) tuples suitable for spectrum_histogram.

    Ensemble averaging is doing two jobs here:
      1. SMOOTHNESS: more samples → less jagged histogram.
      2. HONESTY: if a visual feature (like snap's avoidance dip) survives
         across many seeds, it's real physics; if it varies wildly across
         seeds, we were overfitting to a single trajectory's idiosyncrasies.
    """
    run_sim_kwargs.setdefault("spectrum_every", 10)
    all_samples = []
    for i in range(n_seeds):
        _, _, samples = run_sim(seed=base_seed + i, **run_sim_kwargs)
        if drop_burn_in:
            burn = max(1, len(samples) // 10)
            samples = samples[burn:]
        all_samples.extend(samples)
    return all_samples


def save_spectrum_plot(samples_by_label, omega_d, out_path,
                       n_bins=60, omega_max=4.0, ylim=(0.0, 1.0),
                       title=None):
    """Save a P(ω) plot in the style of Kachman 2017 Fig S8.

    samples_by_label : dict[str, list[(dt, frequencies)]]
        Curves to overlay. Recognized label colors:
          'catch'    → red
          'snap'     → green
          'undriven' → blue
        Any other label is plotted in black.

    The trivial rigid-body mode at ω = √(k_0/m) ≈ 0.1 spikes off-chart;
    `ylim` clips it for legibility (matches the paper's plotting choice).
    """
    color = {"catch": "#c62828", "snap": "#2e7d32", "undriven": "#1565c0"}

    fig, ax = plt.subplots(figsize=(7.5, 5.0), dpi=140)
    for label, samples in samples_by_label.items():
        edges, density = spectrum_histogram(samples,
                                            n_bins=n_bins,
                                            omega_max=omega_max)
        centers = 0.5 * (edges[:-1] + edges[1:])
        ax.plot(centers, density,
                color=color.get(label, "black"),
                linewidth=2.2,
                label=label.title())

    # Vertical drive-frequency marker
    ax.axvline(omega_d, color="black", linewidth=0.8)
    ax.text(omega_d, ylim[1] * 0.97, f" ω_d = {omega_d}",
            fontsize=10, va="top", ha="left")

    ax.set_xlabel(r"$\omega$", fontsize=14)
    ax.set_ylabel(r"$\mathcal{P}(\omega)$", fontsize=14)
    ax.set_xlim(0.0, omega_max)
    ax.set_ylim(*ylim)
    ax.legend(loc="upper right", frameon=False, fontsize=11)
    ax.set_title(title or
                 f"Kachman 2017 reproduction — normal-mode spectrum (ω_d = {omega_d})",
                 fontsize=11)

    fig.tight_layout()
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    fig.savefig(out_path)
    plt.close(fig)
    print(f"Saved: {out_path}")
