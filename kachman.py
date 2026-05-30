"""
kachman.py — Kachman-line REFERENCE IMPL + I_pred MEASUREMENT (2026-05-30).

The stepping-stone for the I_pred pivot (project-ipred-pivot, memory 2026-05-30).
Reimplements Kachman, Owen & England 2017 (PRL 119, 038001) — the only published
England-line simulation — as an open-source artifact (per
project-reference-impl-opportunity, memory 2026-05-28), and then adds the
measurement the original paper does not: Still 2012's predictive-information
decomposition on the bond-network trajectories.

PLUMBING: Claude.   PHYSICS: Brent (=== FILL FROM PAPER === banners are yours).
Papers: papers/kachman-owen-england-2017-self-organized-resonance.pdf
        papers/kachman-owen-england-2017-self-organized-resonance-supplement.pdf
        papers/still-2012-thermodynamics-of-prediction.pdf

Sibling to england.py (Tier 0, Eq-9 3-state toy), still.py (Tier 1, kernel +
I_pred/I_mem + selection), zentropy.py (Tier 1.5, composition), pacman.py
(Tier 2, spatial — now CONTINGENT per project-ipred-pivot).

Memory pointers: project-ipred-pivot, project-sim-england-state (SUPERSEDED,
preserved as the pacman-path reference), project-reference-impl-opportunity.
Spine: spine.md §2 H-correspondence note (added 2026-05-30) — H of an agent ≡
absorbed work W of Kachman 2017 in the passive limit, at the cluster scale.

================================================================================
WHY THIS FILE EXISTS — THREE PREDICTIONS, ONE SUBSTRATE
================================================================================

Kachman 2017 is the strongest peer-reviewed England-line empirical anchor (cf.
Quanta 2017 "First Support for a Physics Theory of Life"). It anchors three
zentropy predictions of escalating strength: two on the published model as-is
(PREDICTIONS 1 and 2 below), and one on a storage-extended variant that is the
falsifiability target for the entire framework (PREDICTION 3).

PREDICTION 1 — bidirectional H/D selection. [Observation, not new sim.]

    Catch bonds (main text):  breakage rate ↓ with stretch
                              → resonant structures stable
                              → high-H selected (drive-seeking)
    Snap bonds  (Fig S8):     breakage rate ↑ with stretch
                              → off-resonant structures stable
                              → low-D selected (drive-avoiding)

    Both regimes are selected under the same drive. This is the H-side and
    D-side of the bidirectional bound in spine.md §3.2 — colonization gain
    via better coupling, destruction-penalty avoidance via no coupling — both
    already observed in Kachman's existing data. Re-reading, not novel sim.

PREDICTION 2 — I_pred decomposition on A(t). [Novel measurement; what this
                                               file is built to compute.]

    The state A(t) (adjacency matrix, who is bonded to whom at time t) is a
    finite Markov chain under Gillespie-on-graphs. Define, per Still 2012:

        I_mem(t)  = I( A_t ; F_{≤t} )      info A carries about past drive
        I_pred(t) = I( A_t ; F_{>t} )      info A carries about future drive
        I_nonpred = I_mem - I_pred         wasteful memory (Still 2012)

    Still's bound:   W_diss(t) ≥ k_B T · I_nonpred(t)

    Zentropy prediction: I_pred GROWS over the sim's evolutionary time in the
    CATCH regime as resonant configurations are selected (phase-locking to
    drive encodes drive-phase information in A). I_pred stays NEAR ZERO in the
    SNAP regime — selection there is structural avoidance, not informational.

    Subtlety to think through (Brent): Kachman's drive is DETERMINISTIC
    (pure sinusoid). Still 2012's formulation is for stochastic environments;
    naively applied, I_pred against a deterministic F could be trivially high
    (drive is fully known) or trivially zero (no information beyond the phase
    φ(t)). Operational route: either (a) add stochasticity to the drive
    (random phase resets / random frequency switches), or (b) reformulate
    I_pred against the drive PHASE — does A_t resolve φ(t)? Both routes
    preserve the prediction; (b) keeps the model unchanged, (a) keeps the
    Still 2012 formulation unchanged. Flag this choice in any write-up.

    Falsification conditions (pre-register before running):
      - I_pred flat in catch regime
          → resonance ≠ predictive coupling; H-side of zentropy's bound
            does not land where the framework claims.
      - I_pred high in snap regime
          → drive-avoidance is somehow informational; retract the
            catch/snap H-vs-D dichotomy of PREDICTION 1.
      - I_nonpred fails to bound W_diss
          → Still 2012's bound itself fails on this substrate (would be
            a Still 2012 falsification, not just a zentropy one).

PREDICTION 3 — storage channel + M-axis sweep locates the abiogenesis
                threshold M*.   [Sim extension; THE FALSIFIABILITY TARGET
                for spine.md §5 AND §6.]

    Kachman's substrate is a pure-dissipator regime: no reproduction, no
    growth, no storage channel beyond bounded spring potential. Energy
    conservation forces ⟨H⟩ ≈ ⟨D⟩ at steady state, so W = H - D ≈ 0
    throughout. Catch (max-H operating point) and snap (min-D operating
    point) are BOTH pure-dissipator strategies on the W ≈ 0 line, at
    different throughput levels — neither is a max(H - D) strategy.

    Zentropy's spine.md §5 identifies max(H - D) > 0 sustained with LIFE.
    That strategy cannot emerge in Kachman's setup as published, because
    the substrate cannot store. Two coordinated changes are required:

      (i)  ADD a storage channel: a Gillespie reproduction event that splits
           a cluster into two copies of A, conditioned on a threshold of
           accumulated stored energy (spring potential + accumulated
           absorbed-but-not-dissipated work). Track lineage explicitly.
      (ii) SWEEP M: use the pacman-drive variant (noise + M incommensurate
           sinusoids; see [[project-sim-england-state]] N*(M) ≈ 2M design).
           For each M, re-run catch / snap / catch+storage / snap+storage.

    Predictions:

      a. At low M: the storage-enabled regimes do NOT outperform pure-
         dissipator catch/snap. The replication-machinery cost K outweighs
         the cost of rediscovering a small kernel each generation. No
         third strategy is selected.

      b. At high M: a third selection strategy emerges with sustained W > 0
         that beats both catch and snap. Configurations in this regime
         carry HIGHER I_pred than either pure-dissipator strategy — the
         storage channel pays for the predictive memory by routing surplus
         into lineage growth (heritable kernels amortize Still-discovery
         cost across generations).

      c. There exists a CROSSOVER M* between these regimes. At M*, the
         third strategy first becomes competitive. M* is the substrate-
         specific abiogenesis threshold for this Kachman-on-pacman-drive
         system (spine.md §6).

    Falsification:
      - No third strategy at any M  →  zentropy's "predictive memory pays
        via window-widening" mechanism does not select for its predicted
        configurations on this substrate. Load-bearing falsification of
        spine.md §5.
      - Third strategy emerges but M* curve is qualitatively wrong
        (e.g. M* doesn't grow with K, or doesn't scale with environmental
        complexity)  →  spine.md §6's specific crossover argument is wrong
        in form even if the qualitative phenomenon is real.

    PREDICTION 3 is the empirical bridge from Kachman (dissipative
    adaptation, no life) to still.py / zentropy.py (selection on heritable
    kernels, life). The M-axis sweep makes it ALSO the abiogenesis test:
    locating M* on this substrate is locating the thermodynamic threshold
    above which replication becomes thermodynamically favored.

    If it works as predicted, it is the falsifiable empirical anchor for
    BOTH the central zentropy claim AND the abiogenesis-as-phase-transition
    framing in spine.md §6 [OPEN].

================================================================================
MODEL SPEC (from supp pp 3-7)
================================================================================

State:        A ∈ {0,1}^{N×N}, binary, symmetric, A_ii = 0.
              Adjacency matrix of the bond network. THE central object.

Particles:    N identical points on a 1D line, mass m = 1. NO intrinsic
              per-particle frequency — the normal-mode spectrum emerges
              entirely from A.

Mechanics:    N coupled damped harmonic oscillators in 1D. Particle i's
              position x_i(t) obeys (schematically):

                  m·ẍ_i + b·ẋ_i + k·Σ_j A_ij·(x_i - x_j) + k_0·x_i
                                                = F·δ_{i,drive}·sin(ω·t)

              Closed-form steady-state response per fixed A (time-scale-
              separated from bond events; see supp p4).

Bond events:  Two-state Arrhenius rates. The BOND RULE is hard-coded per run.

                catch:  B(d) = ½ k d²                  (supp p5; main text)
                snap:   B(d) = ½ k d² + k·exp(-|d|)    (supp p13; Fig S8)

              Rates are integrals over one drive period of the deterministic
              steady-state amplitude d_ij(t). Catch case has a closed-form
              involving the modified Bessel I_0; snap case is numerical
              (supp p13, "no simple closed form").

Gillespie:    Each step:
                1. solve damped-driven oscillator at current A → d_ij(t)
                2. compute Arrhenius rate for every possible bond event from d_ij
                3. Gillespie-sample next event time + identity → flip one bit in A
                4. accumulate W absorbed and Q dissipated over that interval
              Typical: ~10^4 steps per trajectory (supp p7).

Parameters (supp p7; the values Kachman used to generate the published figures):
    β       = 4000        # inverse temperature (kT very small vs k)
    ε       = 0.0001      # bond depth
    b       = 0.01        # damping
    m       = 1           # particle mass
    k       = 1           # spring stiffness
    F       = 10          # drive amplitude on the driven particle
    ω_d     = 1.5         # drive frequency (used in Fig S8; main text varies it)
    # N is not pinned in a single line in the supp; check main-text figure
    # captions. Headline result is "20 particles" (Quanta 2017); confirm in PRL.
    # Regime: underdamped; kT ≪ F²/k. "Results not finely sensitive."

================================================================================
INTEGRATION FLOOR (from spine.md §2 H-correspondence note, 2026-05-30)
================================================================================

H, D, N are well-defined only at scales whose state can carry I_pred. For
Kachman's 20-particle system:
    single particle      — no internal memory; BELOW floor.
    single bond (A_ij)   — carries ~1 bit, but does not phase-lock to drive;
                           BELOW floor.
    resonant cluster     — connected component of A containing the driven
                           particle, phase-locked to drive; AT floor.

Therefore: the I_pred measurement is taken on the CLUSTER-level state, not on
full A. Operationally — extract the connected component of A containing the
driven particle (or a chosen subgraph statistic of it: size, spectrum,
characteristic frequency) and use THAT as the state in I( · ; F_{>t} ).
Coarse-graining choice is a real methodological call — flag in any write-up,
do not bury.

================================================================================
BUILD ORDER — feedback-foundation-first
================================================================================

Phase 1: reference-impl reproduction (no I_pred yet).
   1a. mechanics: damped-driven coupled-oscillator solver (numpy.linalg)
   1b. bond rates: Arrhenius integrals
                    catch closed-form (Bessel I_0)
                    snap numerical (supp p13)
   1c. Gillespie loop over A
   1d. Honesty test — reproduce Fig 2 of the main text (resonance peak under
        catch) AND Fig S8 (spectrum suppression under snap). This is the
        Crooks-faithfulness check; if either fails, the reference impl is
        wrong and Phase 2 measurements would be meaningless.

Phase 2: I_pred measurement on long trajectories.
   2a. coarse-grain A → cluster state c(t) per Gillespie step
   2b. estimate I( c_t ; F_{≤t} ) and I( c_t ; F_{>t} ) on long trajectories
        (KSG or binned MI estimator; sample-size convergence diagnostic
        mandatory — see project-ipred-pivot for the methodological hazards)
   2c. compare across regimes (catch / snap / undriven) and across ω_d.
        The deliverable: a curve of I_pred vs. evolutionary time per regime.
        That curve is what PREDICTION 2 stands or falls on.

Phase 3: storage channel + M-axis sweep → locate abiogenesis threshold M*.
                                                   [THE FALSIFIABILITY TARGET]
   3a. Augment Phase 2's pacman-drive sim with a storage channel. Simplest
        physically-honest version: a Gillespie reproduction event that splits
        a cluster into two copies of its current A, conditioned on a threshold
        of accumulated stored energy (spring potential + accumulated
        absorbed-but-not-dissipated work). The new copy seeds at low-energy
        bonds; track lineage explicitly.
   3b. Sweep M (drive complexity) across catch / snap / catch+storage /
        snap+storage. For each M, measure:
          - per-regime steady-state W = H - D window width
          - per-regime I_pred (from Phase 2 machinery)
          - per-regime lineage growth rate (with storage)
          - which regime "wins" (highest lineage growth rate, or longest
            cluster persistence in no-storage regimes)
   3c. Locate M*: the crossover where storage-enabled regimes start beating
        pure-dissipator regimes. Characterize M* as a function of K (storage
        machinery cost) and per-bit discovery cost. This is the abiogenesis
        threshold for the Kachman-on-pacman-drive substrate; connect to
        spine.md §6 [OPEN — prior-art audit pending].
   3d. Falsification path: if no third strategy emerges at any M, OR if M*
        does not scale as predicted with K and environmental complexity,
        document the falsification carefully before proceeding to still.py /
        zentropy.py. Per [[project-mission]] this is a Win-#2 or Win-#3
        outcome — load-bearing falsification of a major zentropy claim,
        sharpening or killing the framework.

Each phase must run and reproduce its target result before the next phase is
built ([[feedback-foundation-first]]).

================================================================================
FILE STATUS
================================================================================

2026-05-30: scaffold only. Docstring captures the plan; no code yet. Phase 3
(storage channel + third-strategy emergence) is the FALSIFIABILITY TARGET for
the entire framework — the empirical anchor for spine.md §5's max(H - D)
window framing. Phase 1 (reference impl) and Phase 2 (I_pred decomposition)
are required prerequisites; both must run and reproduce their target results
before Phase 3 carries any weight. Designing ahead is OK; building ahead is
the "out over our skis" trap. Build advances when england.py (Tier 0) is
running and Brent has read Still 2012's I_pred definition + bound carefully
enough to defend Phase 2's measurement choices.

The build sequence may be REVISED: if england.py's Eq-9 3-state toy stays
useful as a Tier-0 honesty test, kachman.py sits between england.py and
still.py as Tier 0.5 — a richer England-line reference impl that the I_pred
machinery (Phase 2 here) can be layered onto WITHOUT going through still.py's
fixed-kernel + selection scaffolding. That makes kachman.py the most direct
path from "no code" to "the I_pred-pivot measurement that the project is now
organized around." Confirm/revise this routing with Brent before Phase 1
begins.
"""


import numpy as np
from scipy.special import ive  # exp-scaled modified Bessel: ive(0, x) = exp(-x) * I_0(x)
                                # numerically stable for the large-stretch regime where
                                # exp(-x) underflows and I_0(x) overflows separately.


# ============================================================================
# Parameters (supp p7 — the values Kachman used for the published figures)
# ============================================================================

# Pinned in the supp:
BETA    = 4000.0     # inverse temperature (kT very small vs k)
EPSILON = 0.0001     # bond depth
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
# Phase 1b — bond-event rates (catch bonds, supp p6 closed form)
# ============================================================================
# Snap-bond rates (supp p13) are deferred — they need numerical integration
# because B(x) = (1/2)k x^2 + k·exp(-|x|) has no closed-form drive-cycle average.

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


# ============================================================================
# Phase 1c — Gillespie on the graph state space
# ============================================================================

def gillespie_step(A, omega=OMEGA_D, rng=None):
    """One Gillespie step on the Markov-on-graphs process:
      1. Solve the mechanics at current A → get d_ij for all pairs.
      2. Compute catch-bond rates for all pairs.
      3. For each pair: if currently bonded (A_ij=1), the event is BREAK at
         rate <r_break>(d_ij). If unbonded, the event is FORM at <r_form>(d_ij).
      4. Sample next event time exponentially with total rate.
      5. Sample which event by rate-weighted multinomial.
      6. Flip the bit in A.

    Returns (new_A, dt, event_type, (i, j)).
    """
    if rng is None:
        rng = np.random.default_rng()

    d = steady_state_distances(A, omega=omega)
    r_form, r_break = catch_rates(d)

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


def run_sim(n_steps=N_STEPS, A_init=None, omega=OMEGA_D, seed=None):
    """Run a Gillespie simulation for up to n_steps events.
    Returns (final_A, trajectory) where trajectory is a list of per-event
    records: {step, t, event, ij, n_bonds}.
    """
    rng = np.random.default_rng(seed)
    A = np.zeros((N, N), dtype=int) if A_init is None else A_init.copy()
    t = 0.0
    trajectory = []
    for step in range(n_steps):
        new_A, dt, event_type, ij = gillespie_step(A, omega=omega, rng=rng)
        if event_type is None:
            print(f"[step {step}] no events available — stopping.")
            break
        t += dt
        A = new_A
        trajectory.append({
            "step":   step,
            "t":      t,
            "event":  event_type,
            "ij":     ij,
            "n_bonds": int(A.sum() // 2),
        })
    return A, trajectory


# ============================================================================
# Phase 1d — reproduce Fig 2 (main text) + Fig S8 (supp) — STUBS
# ============================================================================
# Honesty test: run the sim across a sweep of ω_d and check that the absorbed
# work shows a resonance peak (Fig 2). Fig S8 also needs the snap-bond rates,
# deferred above.


# === PHASE 2a: cluster-level coarse-graining of A ===


# === PHASE 2b: I_mem and I_pred estimators ===
# === FILL FROM PAPER === (still-2012-thermodynamics-of-prediction.pdf)


# === PHASE 2c: I_pred(evolutionary time) curves across regimes ===


# === PHASE 3a: storage channel + reproduction event on pacman-drive sim ===


# === PHASE 3b: M-axis sweep across catch / snap / catch+storage / snap+storage ===


# === PHASE 3c: locate M* (abiogenesis threshold), characterize scaling with K ===


# === PHASE 3d: document outcome — third strategy emerges or load-bearing falsification ===


if __name__ == "__main__":
    print(f"Kachman 2017 reference impl — Phase 1a-1c (catch bonds only).")
    print(f"Parameters: N={N}, ω_d={OMEGA_D}, β={BETA}, ε={EPSILON}, "
          f"b={B}, k={K}, F={F}, m={M}, k_0={K_0}")
    print(f"Running {N_STEPS} Gillespie steps from empty graph...")
    print()

    final_A, traj = run_sim(seed=42)

    print(f"Final bond count: {int(final_A.sum() // 2)}")
    if traj:
        print(f"Total simulated time: {traj[-1]['t']:.4f}")
        n_form  = sum(1 for r in traj if r['event'] == 'form')
        n_break = sum(1 for r in traj if r['event'] == 'break')
        print(f"Events: {len(traj)} ({n_form} form, {n_break} break)")
    else:
        print("No events occurred (sim halted at step 0).")


# === PHASE 2a: cluster-level coarse-graining of A ===


# === PHASE 2b: I_mem and I_pred estimators ===
# === FILL FROM PAPER === (still-2012-thermodynamics-of-prediction.pdf)


# === PHASE 2c: I_pred(evolutionary time) curves across regimes ===


# === PHASE 3a: storage channel + reproduction event on pacman-drive sim ===


# === PHASE 3b: M-axis sweep across catch / snap / catch+storage / snap+storage ===


# === PHASE 3c: locate M* (abiogenesis threshold), characterize scaling with K ===


# === PHASE 3d: document outcome — third strategy emerges or load-bearing falsification ===
