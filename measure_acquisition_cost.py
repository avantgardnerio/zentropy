"""
measure_acquisition_cost.py — PREDICTION 4a (spine.md §7): cumulative-
                              dissipation knee for the acquisition-cost
                              vs storage-cost reframe.

Plots Q_cum (cumulative dissipated heat) and dQ/dt (instantaneous
dissipation rate) along a catch trajectory and looks for a knee — a
slope change between the transient (acquisition / structural
reorganization) and the steady state (maintenance).

The acquisition-cost reframe only requires that the two slopes DIFFER —
it does not require a specific direction. Two IC choices give two
directions:

  - empty-graph IC (default here): system builds bonds up from zero.
      Expected direction: LOW early P_Q (sparse network, few coupled
      modes) → HIGH late P_Q (resonant cluster, large amplitude). The
      "acquisition cost" is the resonant-mode-building cost.

  - thermalized-equilibrium IC (run undriven first, then drive): system
      sheds from dense random network to sparse resonant cluster.
      Expected direction: HIGH early P_Q (dense, many coupled modes) →
      LOW late P_Q (sparse, selective). Matches Fig S2's red box. The
      "acquisition cost" is the cost of selectively removing non-
      resonant structure.

Both should show a knee if the reframe holds at the molecular regime.
Absence of a knee in EITHER setup falsifies the substrate-level
acquisition / storage decoupling (spine.md §7 falsification condition 1).

This is the SHORTEST path to any PREDICTION-4 result.

Refs:
  spine.md §7              — acquisition cost vs storage cost
  kachman.py PREDICTION 4a — test design
  memory:                  — feedback-bank-not-cash,
                             strategic-england-darwin-bridge
"""

import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.colors

from kachman_lib import run_sim, catch_rates, spectrum_histogram


# ============================================================================
# Configuration
# ============================================================================

N_STEPS  = 50_000   # bumped from 10k to test the metastability hypothesis
                    # raised by chunk 9 shatter at 10k (see
                    # strategic-kachman-skepticism memory). Cycle period
                    # observable; re-acquisition resolvable.
SEED     = 42
OMEGA_D  = 1.5
F_DRIVE  = 10.0
OUT_PATH                  = "./out/kachman-acquisition-cost-knee.png"
OUT_PATH_SPECTRUM_EVOLVE  = "./out/kachman-spectrum-evolution.png"

# Spectrum evolution sampling: take a P(ω) "snapshot" by binning all
# spectrum samples within each CHUNK_SIZE_STEPS window. Each chunk gives
# one Fig-S8-style panel; we use small multiples (2 × N_COLS grid) so
# each window can be inspected independently, with the global Fig S8
# average overlaid as a reference line.
SPECTRUM_EVERY      = 10      # sample spectrum every this many Gillespie steps
CHUNK_SIZE_STEPS    = 1000    # one P(ω) panel per this many steps
SPECTRUM_N_COLS     = 5       # grid columns; rows derived from N_STEPS / CHUNK_SIZE_STEPS
SPECTRUM_OMEGA_MAX  = 4.0
SPECTRUM_N_BINS     = 60
SPECTRUM_YLIM       = (0.0, 1.0)

# Smoothing window for instantaneous P_Q (number of events). Larger →
# smoother trace at the cost of resolution near burst edges.
SMOOTH_WINDOW_FRAC = 0.01    # 1% of trajectory length

# Threshold (as a fraction of the early-peak smoothed P_Q) below which we
# declare the initial acquisition burst "ended" and the maintenance regime
# begun. Auto-detection only — the user can override by setting
# ACQUISITION_END_TIME in the config block above.
ACQUISITION_BURST_END_FRACTION = 0.30

# Manual override for the acquisition / maintenance time split. Set to None
# to auto-detect from the smoothed P_Q trace.
ACQUISITION_END_TIME = None


# ============================================================================
# Analysis
# ============================================================================

def analyze(traj):
    """Extract energy arrays, identify acquisition-phase end, compare
    acquisition and maintenance dissipation rates.

    Split is by TIME (not step index): split point is either the manual
    override ACQUISITION_END_TIME or auto-detected as the moment when the
    smoothed instantaneous P_Q first falls back through
    ACQUISITION_BURST_END_FRACTION × (early-peak smoothed P_Q).
    """
    t  = np.array([r["t"]       for r in traj])
    nb = np.array([r["n_bonds"] for r in traj])
    dQ = np.array([r["dQ"]      for r in traj])
    Q  = np.array([r["Q_cum"]   for r in traj])

    # Instantaneous P_Q = dQ / dt per interval. Step 0's dt is t[0] - 0 = t[0].
    dt_arr = np.diff(t, prepend=0.0)
    with np.errstate(divide="ignore", invalid="ignore"):
        P_Q_inst = np.where(dt_arr > 0, dQ / dt_arr, np.nan)

    window = max(10, int(SMOOTH_WINDOW_FRAC * len(t)))
    P_Q_smooth = np.convolve(np.nan_to_num(P_Q_inst, nan=0.0),
                              np.ones(window) / window, mode="same")

    # Determine the acquisition / maintenance split point in time.
    if ACQUISITION_END_TIME is not None:
        t_split = ACQUISITION_END_TIME
        split_method = f"manual override ACQUISITION_END_TIME = {t_split}"
    else:
        # Auto-detect: find the early peak of smoothed P_Q, then the FIRST
        # subsequent time it drops below ACQUISITION_BURST_END_FRACTION of
        # that peak.
        # Search window for the peak: first 25% of trajectory by time.
        t_max = t[-1]
        peak_search_mask = t < 0.25 * t_max
        if peak_search_mask.sum() < 5:
            peak_search_mask = np.ones_like(t, dtype=bool)
        peak_idx = np.argmax(P_Q_smooth[peak_search_mask])
        peak_P_Q = P_Q_smooth[peak_search_mask][peak_idx]
        threshold = ACQUISITION_BURST_END_FRACTION * peak_P_Q
        # Search AFTER the peak for the first crossing back below threshold
        peak_t = t[peak_search_mask][peak_idx]
        post_peak_mask = t > peak_t
        below = P_Q_smooth[post_peak_mask] < threshold
        if below.any():
            t_split = t[post_peak_mask][np.argmax(below)]
        else:
            # Smoothed P_Q never drops below threshold → no clean end-of-burst.
            t_split = t[-1] * 0.5
        split_method = (f"auto-detected (peak smoothed P_Q = {peak_P_Q:.2f} at t = "
                        f"{peak_t:.2f}; drop below {ACQUISITION_BURST_END_FRACTION:.0%} "
                        f"at t = {t_split:.2f})")

    # Slopes via linear fit to Q(t) in each window
    acq_mask  = t <= t_split
    maint_mask = t >  t_split
    if acq_mask.sum() < 2 or maint_mask.sum() < 2:
        slope_acq = slope_maint = intercept_maint = float("nan")
    else:
        slope_acq,   _              = np.polyfit(t[acq_mask],  Q[acq_mask],  deg=1)
        slope_maint, intercept_maint = np.polyfit(t[maint_mask], Q[maint_mask], deg=1)

    # TWO reference lines worth distinguishing:
    #   - "maintenance fit" line: slope_maint * t + intercept_maint
    #       This is the actual fit to late data; its intercept reflects that
    #       maintenance picks up where acquisition left off, NOT at the origin.
    #       Used for visual reference in the plot near the maintenance window.
    #   - "maintenance-from-origin" line: slope_maint * t  (no intercept)
    #       This is the counterfactual "what Q would be if maintenance rate
    #       had held since t=0." The vertical gap at t_split between actual
    #       Q and this line is the acquisition cost in the spine §7 sense.
    extrap_maint_fit         = slope_maint * t + intercept_maint
    extrap_maint_from_origin = slope_maint * t

    Q_at_split       = float(np.interp(t_split, t, Q))
    acquisition_cost = Q_at_split - slope_maint * t_split

    # Knee verdict: meaningful slope change?
    if slope_maint > 0:
        ratio = slope_acq / slope_maint
    else:
        ratio = float("inf")

    return {
        "t": t, "n_bonds": nb, "P_Q_inst": P_Q_inst, "P_Q_smooth": P_Q_smooth,
        "Q_cum": Q,
        "t_split": t_split,
        "split_method": split_method,
        "slope_acq":   slope_acq,
        "slope_maint": slope_maint,
        "extrap_maint_fit":         extrap_maint_fit,
        "extrap_maint_from_origin": extrap_maint_from_origin,
        "ratio":       ratio,
        "Q_at_split":  Q_at_split,
        "acquisition_cost": acquisition_cost,
    }


def verdict(ratio, tolerance=0.10):
    """Direction-agnostic knee detection. Returns a human-readable string."""
    if not np.isfinite(ratio):
        return "ratio undefined (late slope ≈ 0); inspect plot directly."
    if abs(ratio - 1.0) < tolerance:
        return (f"NO KNEE — early and late slopes within ±{tolerance*100:.0f}%. "
                "PREDICTION 4a fails on this trajectory.")
    direction = ("HIGH→LOW (Fig S2-like; structure-shedding transient)"
                 if ratio > 1.0
                 else "LOW→HIGH (empty-IC build-up transient)")
    return f"KNEE DETECTED — slope change is {direction}."


# ============================================================================
# Plotting
# ============================================================================

def save_plot(result, out_path, title=None):
    t          = result["t"]
    nb         = result["n_bonds"]
    P_Q_inst   = result["P_Q_inst"]
    P_Q_smooth = result["P_Q_smooth"]
    Q          = result["Q_cum"]
    t_split    = result["t_split"]
    extrap_maint_fit         = result["extrap_maint_fit"]
    extrap_maint_from_origin = result["extrap_maint_from_origin"]
    slope_acq    = result["slope_acq"]
    slope_maint  = result["slope_maint"]
    Q_at_split   = result["Q_at_split"]
    acquisition_cost = result["acquisition_cost"]

    fig, axes = plt.subplots(3, 1, figsize=(8.5, 9.5), sharex=True, dpi=140)

    # Panel 1: structure dynamics (bond count over time)
    axes[0].plot(t, nb, color="black", lw=1.0)
    axes[0].set_ylabel("bond count")
    axes[0].set_title(title or
                      f"Acquisition-cost knee, catch trajectory "
                      f"(ω_d = {OMEGA_D}, F = {F_DRIVE}, N_steps = {N_STEPS})")
    axes[0].axvline(t_split, color="gray", lw=0.8, ls="--")
    axes[0].axvspan(0, t_split, color="#1565c0", alpha=0.06)

    # Panel 2: instantaneous P_Q with smoothing
    axes[1].plot(t, P_Q_inst,   color="#c62828", lw=0.4, alpha=0.35,
                 label="per-event dQ/dt")
    axes[1].plot(t, P_Q_smooth, color="#c62828", lw=1.4,
                 label="smoothed")
    axes[1].axvline(t_split, color="gray", lw=0.8, ls="--",
                    label=f"acquisition end (t = {t_split:.1f})")
    axes[1].axvspan(0, t_split, color="#1565c0", alpha=0.06)
    axes[1].set_ylabel("dQ/dt  (instantaneous P_Q)")
    axes[1].legend(loc="upper right", frameon=False)

    # Panel 3: cumulative Q with two reference lines.
    axes[2].plot(t, Q, color="black", lw=1.6, label="Q_cum (measured)")
    # "Maintenance fit" — slope_maint * t + intercept_maint. Fits late-data
    # cloud; intercept reflects that maintenance picks up at Q_at_split, not 0.
    axes[2].plot(t, extrap_maint_fit, color="gray", ls="--", lw=1.0,
                 label=f"maintenance fit  (slope = {slope_maint:.3f})")
    # "Maintenance-from-origin" — slope_maint * t. The counterfactual line of
    # "what Q would be if maintenance rate held since t=0." The vertical gap
    # between this and the actual curve at t_split IS the acquisition cost
    # in the spine §7 sense.
    axes[2].plot(t, extrap_maint_from_origin, color="gray", ls=":", lw=1.0,
                 label="maintenance rate × t  (counterfactual from origin)")
    # Acquisition-rate fit as a tangent on the acquisition window
    axes[2].plot([0.0, t_split], [0.0, slope_acq * t_split],
                 color="#1565c0", ls=":", lw=1.4,
                 label=f"acquisition-rate slope = {slope_acq:.3f}")
    axes[2].axvline(t_split, color="gray", lw=0.8, ls="--")
    axes[2].axvspan(0, t_split, color="#1565c0", alpha=0.06)
    # Shade the acquisition-cost wedge: between actual Q and maintenance-from-
    # origin line on [0, t_split].
    fill_mask = t <= t_split
    axes[2].fill_between(t[fill_mask],
                          extrap_maint_from_origin[fill_mask],
                          Q[fill_mask],
                          color="#1565c0", alpha=0.15,
                          label=f"acquisition cost  = {acquisition_cost:.0f}")
    axes[2].set_ylabel("Q_cum  (cumulative dissipation)")
    axes[2].set_xlabel("t  (simulation units)")
    axes[2].legend(loc="lower right", frameon=False, fontsize=9)

    fig.tight_layout()
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    fig.savefig(out_path)
    plt.close(fig)
    print(f"Saved: {out_path}")


def save_spectrum_evolution_plot(spectrum_samples, traj, omega_d, out_path,
                                 chunk_size_steps=CHUNK_SIZE_STEPS,
                                 spectrum_every=SPECTRUM_EVERY,
                                 n_cols=SPECTRUM_N_COLS,
                                 n_bins=SPECTRUM_N_BINS,
                                 omega_max=SPECTRUM_OMEGA_MAX,
                                 ylim=SPECTRUM_YLIM):
    """Small-multiples plot: one P(ω) panel per CHUNK_SIZE_STEPS-step window.

    Each panel is built the same way as Fig S8 — occupancy-weighted histogram
    of normal-mode frequencies for all samples in the chunk. The global
    average across the whole trajectory is overlaid in each panel (light
    gray dashed line) as the Fig S8 baseline, so deviation from the global
    attractor is visible at a glance.

    Brent's hypothesis (2026-05-30): if each stairstep plateau is sitting
    in/near the resonant attractor, every chunk's P(ω) should approximate
    the global average — possibly with within-attractor variation but the
    resonant peak at ω_d preserved throughout.

    Arguments:
      spectrum_samples : list of (dt, frequencies) tuples in chronological
                         order (one per spectrum_every Gillespie steps).
      traj             : full trajectory list (used to look up wall-clock
                         time at each chunk boundary).
    """
    samples_per_chunk = max(1, chunk_size_steps // spectrum_every)
    chunks = []
    chunk_step_ranges = []
    chunk_time_ranges = []
    for chunk_idx, start_sample in enumerate(range(0, len(spectrum_samples),
                                                    samples_per_chunk)):
        chunk = spectrum_samples[start_sample:start_sample + samples_per_chunk]
        if not chunk:
            continue
        chunks.append(chunk)
        step_start = chunk_idx * chunk_size_steps
        step_end   = min(step_start + chunk_size_steps - 1, len(traj) - 1)
        chunk_step_ranges.append((step_start, step_end))
        chunk_time_ranges.append((traj[step_start]["t"] if step_start < len(traj) else 0.0,
                                   traj[step_end]["t"]   if step_end   < len(traj) else 0.0))

    if not chunks:
        print("No spectrum samples to plot — skipping spectrum evolution plot.")
        return

    # Global average — the Fig S8 baseline drawn in every panel
    all_samples = [s for chunk in chunks for s in chunk]
    g_edges, g_density = spectrum_histogram(all_samples,
                                              n_bins=n_bins, omega_max=omega_max)
    g_centers = 0.5 * (g_edges[:-1] + g_edges[1:])

    n_chunks = len(chunks)
    n_rows = (n_chunks + n_cols - 1) // n_cols

    cmap = plt.get_cmap("viridis")
    fig, axes = plt.subplots(n_rows, n_cols,
                              figsize=(3.2 * n_cols, 2.6 * n_rows),
                              dpi=140, sharex=True, sharey=True,
                              squeeze=False)

    for i in range(n_rows * n_cols):
        ax = axes[i // n_cols][i % n_cols]
        if i >= n_chunks:
            ax.set_visible(False)
            continue

        # Global average as a reference (faded gray dashed in every panel)
        ax.plot(g_centers, g_density,
                color="gray", lw=1.0, ls="--", alpha=0.6,
                label="global avg" if i == 0 else None)

        # This chunk's P(ω)
        edges, density = spectrum_histogram(chunks[i],
                                             n_bins=n_bins, omega_max=omega_max)
        centers = 0.5 * (edges[:-1] + edges[1:])
        color = cmap(i / max(n_chunks - 1, 1))
        ax.plot(centers, density, color=color, lw=1.6,
                label=f"chunk {i}" if i == 0 else None)

        # Drive frequency marker
        ax.axvline(omega_d, color="red", lw=0.8, alpha=0.6)

        # Panel title — step range and time range
        s_start, s_end = chunk_step_ranges[i]
        t_start, t_end = chunk_time_ranges[i]
        ax.set_title(f"steps {s_start}-{s_end}\nt ∈ [{t_start:.1f}, {t_end:.1f}]",
                      fontsize=9)

        ax.set_xlim(0.0, omega_max)
        ax.set_ylim(*ylim)

        # Only label outer axes
        if i // n_cols == n_rows - 1:
            ax.set_xlabel(r"$\omega$", fontsize=10)
        if i % n_cols == 0:
            ax.set_ylabel(r"$\mathcal{P}(\omega)$", fontsize=10)

    # One shared legend in the first panel
    axes[0][0].legend(loc="upper right", frameon=False, fontsize=8)

    fig.suptitle(f"Spectrum evolution per {chunk_size_steps}-step window  "
                 f"(ω_d = {omega_d}; red line); gray dashed = global average",
                 fontsize=11, y=0.995)
    fig.tight_layout()
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    fig.savefig(out_path)
    plt.close(fig)
    print(f"Saved: {out_path}")


# ============================================================================
# Main
# ============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("PREDICTION 4a — cumulative-dissipation knee (spine.md §7)")
    print("=" * 70)
    print()
    print(f"  N_STEPS                 = {N_STEPS}")
    print(f"  ω_d                     = {OMEGA_D}")
    print(f"  F_drive                 = {F_DRIVE}")
    print(f"  seed                    = {SEED}")
    print(f"  initial A               = empty graph (default)")
    if ACQUISITION_END_TIME is not None:
        print(f"  acquisition end (manual) = {ACQUISITION_END_TIME}")
    else:
        print(f"  burst-end threshold     = "
              f"{ACQUISITION_BURST_END_FRACTION:.0%} of early-peak smoothed P_Q")
    print()

    print(f"Running catch trajectory...")
    _, traj, spectrum = run_sim(n_steps=N_STEPS, omega=OMEGA_D, F_drive=F_DRIVE,
                                seed=SEED, rate_fn=catch_rates,
                                spectrum_every=SPECTRUM_EVERY)

    # Sanity: ensure W_diss instrumentation is present in kachman_lib.
    required_keys = {"dW", "dQ", "W_cum", "Q_cum"}
    missing = required_keys - set(traj[0].keys())
    if missing:
        raise RuntimeError(
            f"Trajectory dict missing W_diss instrumentation keys: {missing}. "
            f"Update kachman_lib.run_sim (see kachman.py PHASE 1.5a)."
        )

    print(f"  Trajectory length:      {len(traj)} events")
    print(f"  Final simulated time:   {traj[-1]['t']:.4f}")
    print(f"  Final bond count:       {traj[-1]['n_bonds']}")
    print(f"  Cumulative W absorbed:  {traj[-1]['W_cum']:.4f}")
    print(f"  Cumulative Q dissipated: {traj[-1]['Q_cum']:.4f}")
    print(f"  Energy balance |W − Q|: {abs(traj[-1]['W_cum'] - traj[-1]['Q_cum']):.3e}")
    print()

    result = analyze(traj)
    print(f"  Acquisition / maintenance split:  {result['split_method']}")
    print(f"  Acquisition phase: t ∈ [0, {result['t_split']:.2f}]   "
          f"(slope = {result['slope_acq']:.3f})")
    print(f"  Maintenance phase: t ∈ [{result['t_split']:.2f}, {result['t'][-1]:.2f}]   "
          f"(slope = {result['slope_maint']:.3f})")
    print(f"  Slope ratio (acquisition / maintenance): {result['ratio']:.3f}")
    print(f"  Q_cum at end of acquisition:             {result['Q_at_split']:.2f}")
    print(f"  Counterfactual (maint-rate × t_split):   "
          f"{result['slope_maint'] * result['t_split']:.2f}")
    print(f"  Acquisition cost (excess above counterfactual): "
          f"{result['acquisition_cost']:.2f}")
    print(f"  Acquisition cost as fraction of total Q: "
          f"{result['acquisition_cost'] / result['Q_cum'][-1]:.1%}")
    print()
    print(f"  Verdict: {verdict(result['ratio'])}")
    print()

    save_plot(result, OUT_PATH)

    print()
    print(f"Spectrum evolution: {len(spectrum)} spectrum samples (every "
          f"{SPECTRUM_EVERY} Gillespie steps); chunking into windows of "
          f"{CHUNK_SIZE_STEPS} steps each.")
    save_spectrum_evolution_plot(spectrum, traj=traj, omega_d=OMEGA_D,
                                  out_path=OUT_PATH_SPECTRUM_EVOLVE)
