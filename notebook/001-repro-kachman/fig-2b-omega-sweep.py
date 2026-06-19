"""
notebook/001-repro-kachman/fig-2b-omega-sweep.py

Reproduce Kachman 2017 main-text Fig 2(b): heatmap of P(ω) across a
sweep of drive frequencies ω_d, under catch dynamics.

Kachman's published Fig 2(b) shows a clear DIAGONAL STRIPE where the
catch peak tracks the drive frequency — at each ω_d, the network
reorganizes so that its mode population piles up at that same ω.

This is a multi-point test of our catch implementation. If the diagonal
appears cleanly across the full ω_d range, catch is correctly
implemented at multiple frequencies — much stronger evidence than the
single ω_d = 1.5 reproduction in fig-s8-spectrum.png.

If the diagonal bends, blurs, or breaks, that tells us where catch is
broken — and crucially, it casts doubt on catch-based downstream
experiments (MI of catch vs snap, dissipation, etc.) in those regimes.

Pre-registered prediction: clean diagonal from (ω=1, ω_d=1) through
(ω=4, ω_d=4), with a persistent horizontal haystack band around ω ≈ 3
(the network's natural mode distribution that's always present
regardless of drive).
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
    N, N_STEPS, N_SEEDS,
    catch_rates,
    run_ensemble, spectrum_histogram,
)


# ---- Parameters ------------------------------------------------------------
F_DRIVE   = 10.0
OMEGA_MAX = 5.0
N_BINS    = 60

# Sweep drive frequencies across the haystack range, matching Kachman's Fig 2(b).
OMEGA_D_VALUES = np.linspace(0.5, 4.5, 9)   # 9 values: 0.5, 1.0, 1.5, ..., 4.5

SEED_BASE = 4000

OUT_PATH = os.path.join(os.path.dirname(__file__), "fig-2b-omega-sweep.png")


# ---- Main ------------------------------------------------------------------
if __name__ == "__main__":
    print(f"Kachman Fig 2(b) reproduction — catch P(ω) across ω_d sweep")
    print(f"  N={N}, F={F_DRIVE}, N_SEEDS={N_SEEDS}, N_STEPS={N_STEPS} per seed")
    print(f"  ω_d values: {[f'{v:.1f}' for v in OMEGA_D_VALUES]}")
    print()

    # Build the heatmap: rows = ω_d values, cols = ω bins
    bin_edges = np.linspace(0.0, OMEGA_MAX, N_BINS + 1)
    bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])
    heatmap = np.zeros((len(OMEGA_D_VALUES), N_BINS))
    peak_positions = []

    for i, omega_d in enumerate(OMEGA_D_VALUES):
        print(f"  [{i+1}/{len(OMEGA_D_VALUES)}] ω_d = {omega_d:.2f} "
              f"({N_SEEDS} seeds)...", end="", flush=True)
        samples = run_ensemble(
            n_seeds=N_SEEDS, base_seed=SEED_BASE + i * 100,
            omega=omega_d, F_drive=F_DRIVE, rate_fn=catch_rates,
        )
        edges, density = spectrum_histogram(
            samples, n_bins=N_BINS, omega_max=OMEGA_MAX,
        )
        heatmap[i, :] = density

        # Find the peak EXCLUDING the rigid-body spike at ω < 0.2
        mask = bin_centers >= 0.2
        i_peak_in_mask = int(np.argmax(density[mask]))
        omega_peak = float(bin_centers[mask][i_peak_in_mask])
        peak_positions.append(omega_peak)
        print(f"  peak at ω = {omega_peak:.2f}  (expected: {omega_d:.2f})")

    print()
    print("Summary of peak positions vs drive frequencies:")
    print(f"  {'ω_d':>6}  |  {'peak ω':>7}  |  {'Δ':>6}")
    print(f"  {'-'*6}  |  {'-'*7}  |  {'-'*6}")
    for omega_d, peak in zip(OMEGA_D_VALUES, peak_positions):
        delta = peak - omega_d
        print(f"  {omega_d:6.2f}  |  {peak:7.2f}  |  {delta:+6.2f}")

    # ---- Plot --------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(7.5, 6), dpi=140)

    # Heatmap: imshow with origin='lower' so y-axis increases upward.
    # extent maps (x_min, x_max, y_min, y_max).
    im = ax.imshow(
        heatmap,
        extent=(0.0, OMEGA_MAX, OMEGA_D_VALUES[0], OMEGA_D_VALUES[-1]),
        origin="lower",
        aspect="auto",
        cmap="hot",
    )

    # Diagonal guide: where catch peak SHOULD sit (ω = ω_d).
    diag = np.linspace(max(0.5, OMEGA_D_VALUES[0]),
                       min(OMEGA_MAX, OMEGA_D_VALUES[-1]), 50)
    ax.plot(diag, diag, color="white", lw=1.0, ls="--", alpha=0.6,
            label="ω = ω_d (catch prediction)")

    # Measured peak positions overlaid.
    ax.plot(peak_positions, OMEGA_D_VALUES, "o", color="cyan", ms=5,
            label="measured peak", markeredgecolor="black", markeredgewidth=0.5)

    ax.set_xlabel("ω  (mode frequency)")
    ax.set_ylabel("ω_d  (drive frequency)")
    ax.set_xlim(0.0, OMEGA_MAX)
    ax.set_title(f"Kachman Fig 2(b) reproduction — catch P(ω) vs ω_d\n"
                 f"(N={N}, F={F_DRIVE}, N_SEEDS={N_SEEDS}, N_STEPS={N_STEPS}/seed)")
    ax.legend(loc="upper left", fontsize=8, frameon=False)

    cbar = plt.colorbar(im, ax=ax, label="P(ω)")

    fig.tight_layout()
    fig.savefig(OUT_PATH)
    plt.close(fig)
    print()
    print(f"Saved: {OUT_PATH}")
