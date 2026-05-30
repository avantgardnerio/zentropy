"""
kachman_stochastic.py — Kachman 2017 reference impl with STOCHASTIC drive
                        frequency, making Still 2012's I_pred / I_mem framework
                        cleanly applicable (2026-05-30).

The deterministic-drive version (`kachman.py`) has F(t) = F·sin(ω_d·t) with
ω_d constant. Still's framework requires a stochastic environment; with
deterministic drive, I_pred is trivially zero/infinite. This file replaces
the constant ω_d with an Ornstein-Uhlenbeck process: ω(t) drifts around ω_0
with width σ_ω and correlation time τ_ω. Now future drive has genuine
uncertainty, and the bond network's spectral tuning carries (partial)
information about future ω.

Imports physics from `kachman_lib.py`. Adds:
  - ou_step: one Euler-Maruyama step of the OU process for ω
  - run_sim_stochastic: Gillespie loop with ω evolving between events
  - run_ensemble_stochastic: ensemble-averaging helper
  - __main__: spectrum sanity check (P1 below); I_mem / I_pred measurement
    follows in a Phase B-2 commit.

================================================================================
PRE-REGISTERED PREDICTIONS (a priori, before running)
================================================================================

These predictions are recorded BEFORE any stochastic-drive sim has been run.
Edit only with explicit dated addenda; do not silently revise after seeing
results.

P1 — Spectrum sanity check.
     With modest σ_ω (~10–15% of ω_0), the catch / undriven / snap spectrum
     should still resemble Fig S8: catch peaks near ω_0, snap shifts the
     haystack tail rightward and dips at ω_0, undriven is the haystack
     baseline. If the spectrum doesn't resemble the deterministic-drive
     version under matched σ_ω, the stochastic extension has broken
     something fundamental and PRECEDES any I_pred / I_mem measurement.
     Falsification: spectrum qualitatively different from Fig S8 at small
     σ_ω → re-examine OU integration / time-scale separation assumptions.

P2 — I_pred asymmetry (the core Still test).
     I_pred(catch)  > I_pred(snap)
     because catch's bond network spectral-tunes to current ω (encoding ω
     in A); snap anti-tunes (encoding only "not near ω", which is much less
     informative per the half-space-vs-point argument in `kachman.py`
     PREDICTION 2). I_pred(undriven) should be ≈ 0 (no drive to predict).
     Falsification: I_pred(snap) ≥ I_pred(catch) at any σ_ω with sufficient
     statistics → catch's H-side selection is not informationally distinct
     from snap's D-side selection; the bidirectional-H/D framing in
     spine.md §5 fails on its own substrate.

P3 — I_mem grows with σ_ω in catch, slower in snap.
     As σ_ω increases, H(ω) grows. If the catch network's spectral-tuning
     resolution stays fixed, I_mem(catch) = H(ω) - H(ω | A_features) grows
     with σ_ω until it saturates at the network's resolution limit. Snap's
     anti-tuning carries less per-bit information about ω (half-space
     argument), so I_mem(snap) grows slower or saturates earlier.
     Falsification: I_mem(snap) tracks I_mem(catch) at all σ_ω → snap is
     informationally equivalent to catch on this substrate; the
     half-space-vs-point asymmetry argument fails.

P4 — The catch–snap GAP in both I_mem and I_pred grows with σ_ω.
     Combines P2 + P3: as the environment becomes more variable, catch's
     informational advantage over snap should widen, not narrow, up to
     network-resolution saturation.
     Falsification: gap shrinks or stays constant with growing σ_ω →
     informational asymmetry is a fixed artifact, not a function of
     environmental complexity. Weakens the connection to the PREDICTION 3
     N*(M) abiogenesis-threshold scaling in `kachman.py` (which also
     predicts the gap grows with environmental complexity).
"""

import os
import numpy as np
import matplotlib.pyplot as plt

from kachman_lib import (
    # Parameters
    BETA, EPSILON, B, M, K, F, K_0, I_DRIVE, R_0,
    N, N_STEPS, BETA_SNAP, N_THETA_SNAP, N_SEEDS,
    # Functions reused
    catch_rates, snap_rates, gillespie_step, normal_mode_frequencies,
    spectrum_histogram, save_spectrum_plot,
)


# ============================================================================
# OU process parameters (drive frequency drift)
# ============================================================================

OMEGA_0     = 1.5     # mean drive frequency (around which ω drifts)
SIGMA_OMEGA = 0.01    # OU stationary std-dev: 1× the single-mode resonance bandwidth
                      # (b/m = 0.01). Within-band drift — network should track stably.
                      # Crank up later to test the disintegrate-and-reform regime.
TAU_OMEGA   = 100.0   # OU correlation time: how fast ω drifts (units of 1/r_0)


# ============================================================================
# OU step + stochastic Gillespie loop
# ============================================================================

def ou_step(omega, omega_0, sigma, tau, dt, rng):
    """One Euler-Maruyama step of an Ornstein-Uhlenbeck process for ω.

    Continuous-time SDE:
        dω = -(ω - ω_0)/τ · dt  +  σ · √(2/τ) · dW
        \________________________/   \_____________/
            mean-reverting drift           random kick

    Stationary distribution: ω ~ N(ω_0, σ²). Correlation time τ.
    Picture: a noisy trajectory pulled back toward ω_0 — like a Brownian
    particle in a harmonic well. NEVER repeats (unlike a sine wave), but
    stays in a band of roughly ω_0 ± 2σ most of the time.

    The √(2/τ) factor normalizes σ as the stationary std-dev (not the SDE
    coefficient), so changing τ doesn't change the band width — only how
    fast ω wanders within the band.
    """
    drift     = -(omega - omega_0) / tau * dt
    diffusion = sigma * np.sqrt(2.0 * dt / tau) * rng.standard_normal()
    return omega + drift + diffusion


def run_sim_stochastic(n_steps=N_STEPS, A_init=None, F_drive=F,
                       omega_0=OMEGA_0, sigma_omega=SIGMA_OMEGA,
                       tau_omega=TAU_OMEGA,
                       seed=None, spectrum_every=None,
                       rate_fn=catch_rates):
    """Gillespie simulation with an OU-drifting drive frequency ω(t).

    Identical to kachman_lib.run_sim except ω is no longer constant. After
    each Gillespie event of duration dt, ω advances by one OU step. The
    bond rates at the next event use the new ω.

    Returns (final_A, trajectory, spectrum) where each spectrum entry is
    a 3-tuple (dt, frequencies, omega_at_sample) — the third element is
    added for later I_pred / I_mem measurement.
    """
    rng = np.random.default_rng(seed)
    A = np.zeros((N, N), dtype=int) if A_init is None else A_init.copy()
    omega = omega_0          # initialize at the OU mean
    t = 0.0
    trajectory = []
    spectrum = []

    for step in range(n_steps):
        new_A, dt, event_type, ij = gillespie_step(
            A, omega=omega, F_drive=F_drive, rng=rng, rate_fn=rate_fn
        )
        if event_type is None:
            print(f"[step {step}] no events available — stopping.")
            break

        if spectrum_every and step % spectrum_every == 0:
            spectrum.append((dt, normal_mode_frequencies(A), omega))

        # Advance ω via OU before the next event
        omega = ou_step(omega, omega_0, sigma_omega, tau_omega, dt, rng)

        t += dt
        A = new_A
        trajectory.append({
            "step":   step,
            "t":      t,
            "event":  event_type,
            "ij":     ij,
            "n_bonds": int(A.sum() // 2),
            "omega":  omega,
        })

    return A, trajectory, spectrum


def run_ensemble_stochastic(n_seeds, base_seed, drop_burn_in=True, **kwargs):
    """Like kachman_lib.run_ensemble but for the stochastic-drive sim.
    Returns the flattened spectrum-sample list across all seeds.
    """
    kwargs.setdefault("spectrum_every", 10)
    all_samples = []
    for i in range(n_seeds):
        _, _, samples = run_sim_stochastic(seed=base_seed + i, **kwargs)
        if drop_burn_in:
            burn = max(1, len(samples) // 10)
            samples = samples[burn:]
        all_samples.extend(samples)
    return all_samples


# ============================================================================
# Time-series plotting — tells "drift" vs "disintegrate"
# ============================================================================

def save_time_series_plot(trajectory, spectrum, out_path,
                          omega_0=None, sigma_omega=None,
                          title=None):
    """Three-panel time series:
      - Top:    ω(t) — the OU drive frequency trajectory
                       (with ±2σ_ω band shaded for reference if available)
      - Middle: n_bonds(t) — total bond count, the cluster's "size" proxy
      - Bottom: cluster's dominant non-trivial normal-mode frequency at each
                spectrum sample, overlaid against ω(t) (do bonds chase ω?)

    Reveals whether the network is:
      (a) DRIFTING — n_bonds stays roughly constant, dominant mode shifts
          smoothly to chase ω → existing structure absorbs the change
      (b) DISINTEGRATING — n_bonds oscillates wildly with ω, dominant mode
          uncorrelated with ω → structure falls apart and re-coalesces
    """
    if not trajectory:
        print(f"(empty trajectory; not saving {out_path})")
        return

    t      = np.array([r["t"] for r in trajectory])
    bonds  = np.array([r["n_bonds"] for r in trajectory])
    omegas = np.array([r.get("omega", np.nan) for r in trajectory])

    # For each spectrum sample, collect ALL non-trivial modes (skip the
    # rigid-body modes at ω ≈ √(k_0/m) ≈ 0.1 by filtering above 0.3).
    # Drop a burn-in BY TIME (not by iteration count): the empty-graph
    # initial transient pours many spectrum samples into a tiny time window
    # (events happen in small dt's while bonds rapidly form), which
    # auto-saturates the heatmap colormap. Drop the first 10% of TOTAL
    # simulated time — what matters for the histogram bins.
    total_t = trajectory[-1]["t"]
    t_burn = 0.1 * total_t
    spec_t       = []
    spec_omega   = []
    mode_t       = []
    mode_omega   = []
    cum_t = 0.0
    for (dt, freqs, om) in spectrum:
        cum_t += dt
        if cum_t < t_burn:
            continue
        spec_t.append(cum_t)
        spec_omega.append(om)
        for f in freqs[freqs > 0.3]:
            mode_t.append(cum_t)
            mode_omega.append(f)
    spec_t     = np.array(spec_t)
    spec_omega = np.array(spec_omega)
    mode_t     = np.array(mode_t)
    mode_omega = np.array(mode_omega)

    fig, axes = plt.subplots(3, 1, figsize=(9, 7), dpi=130, sharex=True)

    # Top — ω(t)
    axes[0].plot(t, omegas, color="purple", linewidth=0.9)
    if omega_0 is not None and sigma_omega is not None:
        axes[0].axhspan(omega_0 - 2 * sigma_omega, omega_0 + 2 * sigma_omega,
                        color="purple", alpha=0.08, label="±2σ_ω band")
        axes[0].axhline(omega_0, color="purple", linestyle="--",
                        linewidth=0.7, alpha=0.5, label="ω_0")
        axes[0].legend(loc="upper right", fontsize=9, frameon=False)
    axes[0].set_ylabel("ω(t)")
    axes[0].set_title(title or "Time series")

    # Middle — n_bonds(t)
    axes[1].plot(t, bonds, color="black", linewidth=0.8)
    axes[1].set_ylabel("n_bonds(t)")

    # Bottom — 2D histogram (heatmap) of non-trivial network modes vs time,
    # with ω(t) overlaid. Dark bands ≡ regions of mode density. If the
    # network is tracking, a dark band should follow the cyan ω(t) line.
    # Histogram range starts at t_burn (skipping the equilibration transient).
    if len(mode_t):
        n_time_bins, n_omega_bins, omega_max = 150, 80, 4.0
        H, xedges, yedges = np.histogram2d(
            mode_t, mode_omega,
            bins=[n_time_bins, n_omega_bins],
            range=[[t_burn, total_t], [0.0, omega_max]],
        )
        # Use a sequential colormap; higher counts → darker. Clip vmax at the
        # 99th percentile of nonzero counts so outlier hot spots don't wash out
        # the steady-state structure.
        nonzero = H[H > 0]
        vmax = np.percentile(nonzero, 99) if nonzero.size else None
        axes[2].pcolormesh(xedges, yedges, H.T,
                           cmap="magma_r", shading="auto", vmax=vmax)
        axes[2].plot(spec_t, spec_omega, color="cyan", linewidth=1.2,
                     label="ω(t) drive", alpha=0.9)
        axes[2].set_xlim(t_burn, total_t)
        axes[2].set_ylim(0, omega_max)
        axes[2].legend(loc="upper right", fontsize=9, frameon=False)
    axes[2].set_ylabel("network mode ω")
    axes[2].set_xlabel("simulated time")

    fig.tight_layout()
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    fig.savefig(out_path)
    plt.close(fig)
    print(f"Saved: {out_path}")


# ============================================================================
# I_pred / I_mem measurement — Phase B-2 (next commit)
# ============================================================================
# Plan: at each spectrum sample we record (dt, frequencies, omega). To compute
# I(A_features ; ω) we need to (a) choose a coarse-grained A feature (e.g.
# spectral peak, bond count, cluster size) and (b) build a 2D joint histogram
# of (feature, ω) → binned MI estimator. Implementation pending.


if __name__ == "__main__":
    print("Kachman 2017 with STOCHASTIC drive frequency (OU process)")
    print(f"  ω_0 = {OMEGA_0}, σ_ω = {SIGMA_OMEGA}, τ_ω = {TAU_OMEGA}")
    print(f"  N_SEEDS = {N_SEEDS} per regime, N_STEPS = {N_STEPS} per seed")
    print()

    # ------------------------------------------------------------------
    # P1 — Spectrum sanity check: does the catch/undriven/snap pattern
    # survive OU drift? If yes, the stochastic extension is sound and we
    # proceed to I_pred / I_mem in the next commit. If no, OU parameters
    # need adjustment (or the OU integration is broken).
    # ------------------------------------------------------------------
    print("P1: spectrum sanity check (catch + undriven + snap, OU drive)")
    print(f"  Catch  ({N_SEEDS} seeds)...")
    samples_catch = run_ensemble_stochastic(
        N_SEEDS, base_seed=400, F_drive=10.0, rate_fn=catch_rates
    )
    print(f"  Undriven ({N_SEEDS} seeds)...")
    samples_undriven = run_ensemble_stochastic(
        N_SEEDS, base_seed=500, F_drive=0.0, rate_fn=catch_rates
    )
    print(f"  Snap   ({N_SEEDS} seeds)...")
    samples_snap = run_ensemble_stochastic(
        N_SEEDS, base_seed=600, F_drive=10.0, rate_fn=snap_rates
    )

    # spectrum_histogram (from kachman_lib) expects (dt, freqs) tuples;
    # strip the ω from each 3-tuple for the spectrum plot
    strip = lambda samples: [(s[0], s[1]) for s in samples]

    save_spectrum_plot(
        {"undriven": strip(samples_undriven),
         "catch":    strip(samples_catch),
         "snap":     strip(samples_snap)},
        omega_d=OMEGA_0,
        out_path="./out/kachman-stochastic-spectrum.png",
        title=(f"Kachman + OU drive — ω_0={OMEGA_0}, σ_ω={SIGMA_OMEGA}, "
               f"τ_ω={TAU_OMEGA}"),
    )
    print()
    print("P1 verdict question: does the spectrum still look like Fig S8?")
    print("  - Catch peaks near ω_0?")
    print("  - Snap dips at ω_0 and shifts haystack rightward?")
    print("  - Undriven is the haystack baseline?")
    print("If yes → OU extension is sound; Phase B-2 (I_pred / I_mem) is unblocked.")
    print("If no  → tune σ_ω, τ_ω, or revisit OU integration.")
    print()

    # ------------------------------------------------------------------
    # Single-σ_ω time-series view at σ_ω = 0.01 (= single-mode resonance
    # bandwidth b/m). The network should stay within ONE mode's resonance
    # and the sharp Fig S8-like peak should reappear in the spectrum.
    #
    # NOTE on terminology: this is the STABILITY regime, not the "learning"
    # regime. The variation is small enough that the existing tuning keeps
    # working; the network doesn't have to update its internal state to
    # track ω. Actual learning (state changes in response to input) would
    # require σ_ω large enough to push ω outside one mode's bandwidth, so
    # the network must retune. That's a sweep we haven't done yet.
    # ------------------------------------------------------------------
    print()
    print("Time-series view — single trajectory, σ_ω = 0.01 (= bandwidth):")
    _, ts_trajectory, ts_spectrum = run_sim_stochastic(
        n_steps=N_STEPS, F_drive=10.0, rate_fn=catch_rates,
        seed=42, spectrum_every=1,
    )
    save_time_series_plot(
        ts_trajectory, ts_spectrum,
        out_path="./out/kachman-stochastic-timeseries-catch.png",
        omega_0=OMEGA_0, sigma_omega=SIGMA_OMEGA,
        title=(f"Catch + OU drive — ω_0={OMEGA_0}, σ_ω={SIGMA_OMEGA}, "
               f"τ_ω={TAU_OMEGA} (within-bandwidth drift)"),
    )
    # Dissipation-rate baseline at this σ_ω
    if ts_trajectory:
        total_t = ts_trajectory[-1]["t"]
        n_events = len(ts_trajectory)
        event_rate = n_events / total_t if total_t > 0 else float("nan")
        print(f"  Dissipation-rate proxy: {n_events} events / "
              f"{total_t:.1f} time = {event_rate:.4f} events/time")
        print(f"  (compare to higher-σ_ω runs later — predict rate ↑ with σ_ω)")
    print()
    print("Interpretation guide:")
    print("  - If n_bonds(t) is roughly constant + dominant cluster mode")
    print("    smoothly tracks ω(t) → DRIFTING regime (existing structure")
    print("    absorbs the change, slow tracking, high expected I_pred)")
    print("  - If n_bonds(t) oscillates wildly + dominant mode jumps around")
    print("    independent of ω(t) → DISINTEGRATING regime (structure falls")
    print("    apart and re-coalesces, low expected I_pred)")
