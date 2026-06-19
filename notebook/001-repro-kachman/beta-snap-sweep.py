"""
notebook/001-repro-kachman/beta-snap-sweep.py

Diagnostic: can BETA_SNAP alone close the snap-vs-undriven peak-height
inversion in Fig S8?

In Kachman's published Fig S8, snap (green) has a TALLER and NARROWER
peak than undriven (blue) — the snap selection CONCENTRATES the network's
mode population at a non-resonant frequency.

In our reproduction (notebook/001-repro-kachman/fig-s8-spectrum.png),
snap is BROADER and SHORTER than undriven — we got "avoid ω_d" but not
"concentrate elsewhere."

This script sweeps BETA_SNAP across ~10 orders of magnitude (log-spaced)
and asks: is there ANY BETA_SNAP value where peak(snap) > peak(undriven)?

  - If YES → lock that BETA_SNAP, commit, move on.
  - If NO  → BETA_SNAP is not the load-bearing parameter; something more
            structural is wrong with our snap_rates implementation or
            another physics parameter (likely also unpublished in supp).

N_SEEDS = 1 here for speed. We're not measuring a precise result; we're
asking whether the qualitative inversion exists ANYWHERE in BETA_SNAP space.
"""

import os
import sys

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                 "..", "..")))

from kachman_lib import (
    N, N_STEPS,
    catch_rates, snap_rates,
    run_ensemble, spectrum_histogram,
)


# ---- Parameters ------------------------------------------------------------
OMEGA_D   = 1.5
F_DRIVE   = 10.0
N_SEEDS   = 1                               # speed > precision for this diagnostic

BETA_SNAP_VALUES = np.geomspace(0.5, 200.0, 12)   # ~12 log-spaced values

OMEGA_MAX = 4.0
N_BINS    = 60

SEED_UNDRIVEN = 2000
SEED_SNAP_BASE = 3000

OUT_PATH = os.path.join(os.path.dirname(__file__), "beta-snap-sweep.png")


# ---- Helpers ---------------------------------------------------------------
def peak_height(samples, n_bins=N_BINS, omega_max=OMEGA_MAX):
    """Return peak P(ω) and its ω location from a list of (dt, freqs) samples."""
    edges, density = spectrum_histogram(samples, n_bins=n_bins, omega_max=omega_max)
    centers = 0.5 * (edges[:-1] + edges[1:])
    # Trim the rigid-body mode (ω < 0.2) so the spike at ω = 0 doesn't dominate.
    mask = centers >= 0.2
    if not mask.any():
        return float(density.max()), float(centers[int(np.argmax(density))])
    i_peak = int(np.argmax(density[mask]))
    return float(density[mask][i_peak]), float(centers[mask][i_peak])


# ---- Main ------------------------------------------------------------------
if __name__ == "__main__":
    print(f"BETA_SNAP sweep (N_SEEDS={N_SEEDS}, N_STEPS={N_STEPS}, "
          f"ω_d={OMEGA_D}, F={F_DRIVE})")
    print(f"BETA_SNAP values: {[f'{b:.2f}' for b in BETA_SNAP_VALUES]}")
    print()

    # --- Undriven reference (BETA_SNAP-independent) -----------------------
    print("Running undriven reference (5 seeds for a less-noisy baseline)...")
    samples_undriven = run_ensemble(
        n_seeds=5, base_seed=SEED_UNDRIVEN,
        omega=OMEGA_D, F_drive=0.0, rate_fn=catch_rates,
    )
    peak_un, omega_un = peak_height(samples_undriven)
    print(f"  undriven peak: {peak_un:.4f} at ω = {omega_un:.2f}")
    print()

    # --- Sweep BETA_SNAP --------------------------------------------------
    snap_results = []   # list of (beta, samples, peak, omega_peak)
    for i, beta_snap in enumerate(BETA_SNAP_VALUES):
        # Wrap snap_rates with this beta value
        rate_fn = lambda d, beta_snap=beta_snap: snap_rates(d, beta=beta_snap)
        print(f"  [{i+1:2d}/{len(BETA_SNAP_VALUES)}] BETA_SNAP = {beta_snap:7.2f}...", end="", flush=True)
        samples = run_ensemble(
            n_seeds=N_SEEDS, base_seed=SEED_SNAP_BASE + i * 100,
            omega=OMEGA_D, F_drive=F_DRIVE, rate_fn=rate_fn,
        )
        peak, omega_peak = peak_height(samples)
        diff = peak - peak_un
        flag = "  ✓ snap > undriven" if diff > 0 else ""
        print(f"  peak = {peak:.4f} at ω = {omega_peak:.2f}   (Δ = {diff:+.4f}){flag}")
        snap_results.append((beta_snap, samples, peak, omega_peak))

    # --- Summary ----------------------------------------------------------
    print()
    print("=" * 70)
    diffs = np.array([r[2] - peak_un for r in snap_results])
    best_idx = int(np.argmax(diffs))
    best = snap_results[best_idx]
    print(f"Best BETA_SNAP: {best[0]:.2f}  → snap peak {best[2]:.4f} at "
          f"ω = {best[3]:.2f}  (Δ = {diffs[best_idx]:+.4f})")
    print(f"Undriven peak:  {peak_un:.4f}  at ω = {omega_un:.2f}")
    if diffs.max() > 0:
        print("✓ At least one BETA_SNAP value puts snap peak ABOVE undriven peak.")
        print("  BETA_SNAP alone CAN fix the inversion.")
    else:
        print("✗ NO BETA_SNAP value gets snap peak above undriven peak.")
        print("  BETA_SNAP alone CANNOT fix the inversion → something more")
        print("  structural is wrong (snap_rates functional form, or another")
        print("  parameter Kachman didn't publish).")

    # --- Plot -------------------------------------------------------------
    fig, axes = plt.subplots(2, 1, figsize=(9, 8), dpi=140,
                              gridspec_kw={"height_ratios": [2, 1]})

    # Top: overlay all snap P(ω) curves + undriven baseline
    cmap = plt.cm.viridis
    edges, density_un = spectrum_histogram(samples_undriven,
                                            n_bins=N_BINS, omega_max=OMEGA_MAX)
    centers = 0.5 * (edges[:-1] + edges[1:])
    for i, (beta_snap, samples, _, _) in enumerate(snap_results):
        _, density = spectrum_histogram(samples, n_bins=N_BINS, omega_max=OMEGA_MAX)
        color = cmap(i / max(1, len(snap_results) - 1))
        axes[0].plot(centers, density, color=color, lw=1.1,
                      label=f"β_snap = {beta_snap:.1f}")
    axes[0].plot(centers, density_un, color="black", lw=2.0, ls="--",
                  label="Undriven (reference)")
    axes[0].axvline(OMEGA_D, color="gray", lw=0.8, ls=":")
    axes[0].text(OMEGA_D + 0.03, 0.92, f"ω_d = {OMEGA_D}",
                  transform=axes[0].get_xaxis_transform(), fontsize=8)
    axes[0].set_xlabel("ω")
    axes[0].set_ylabel("P(ω)")
    axes[0].set_xlim(0, OMEGA_MAX)
    axes[0].set_title("Snap P(ω) across BETA_SNAP sweep")
    axes[0].legend(loc="upper right", fontsize=7, ncol=2, frameon=False)

    # Bottom: peak heights vs BETA_SNAP
    snap_peaks = np.array([r[2] for r in snap_results])
    axes[1].plot(BETA_SNAP_VALUES, snap_peaks, "o-", color="#2e7d32", lw=1.6,
                  ms=6, label="snap peak height")
    axes[1].axhline(peak_un, color="#0d1a66", lw=1.6, ls="--",
                     label=f"undriven peak ({peak_un:.3f})")
    axes[1].set_xscale("log")
    axes[1].set_xlabel("BETA_SNAP (log scale)")
    axes[1].set_ylabel("peak P(ω) at ω > 0.2")
    axes[1].set_title(f"Loss-function view: can snap peak > undriven peak?  "
                       f"max Δ = {diffs.max():+.4f}")
    axes[1].legend(loc="best", frameon=False)

    fig.tight_layout()
    fig.savefig(OUT_PATH)
    plt.close(fig)
    print()
    print(f"Saved: {OUT_PATH}")
