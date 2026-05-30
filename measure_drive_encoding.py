"""
measure_drive_encoding.py — rescoped PREDICTION 2 (2026-05-30).

Runs ensembles of fixed-ω_d sims at multiple ω_d values, computes
I(A_feature ; ω_d_label) via binned mutual information. Tests whether
catch's A encodes the drive frequency more sharply than snap's A does
(half-space-vs-point asymmetry — see kachman.py PREDICTION 2 docstring).

This is a STRUCTURAL ENCODING test, not strict Still's I_pred (which
requires time-varying drive — see project-sim-substrate-hierarchy
memory for why that's not achievable on the Kachman bond substrate).

Pre-registered prediction: I(A_catch ; ω_d) > I(A_snap ; ω_d) > I_undriven ≈ 0.

Default A_feature is bond count (1D, simplest). Spectrum peak or other
richer features can be swapped in if bond count is too coarse.
"""

import numpy as np

from kachman_lib import (
    N, N_STEPS, N_SEEDS,
    catch_rates, snap_rates, run_sim,
)


# ============================================================================
# Configuration
# ============================================================================

OMEGA_D_VALUES = [1.0, 1.3, 1.5, 1.7, 2.0]   # five points across the haystack
F_DRIVE        = 10.0                          # drive amplitude
N_SEEDS_LOCAL  = 3                             # ensembles per ω_d (3 for speed)
N_STEPS_LOCAL  = 5_000                         # Gillespie steps per seed
BURN_FRACTION  = 0.1                           # drop first 10% of each trajectory
N_REPLICATES   = 5                             # independent ensemble replicates
                                               # (different base_seed offsets) for
                                               # estimating simulation variance of MI


# ============================================================================
# Binned mutual information
# ============================================================================

def binned_mi(x, y, n_bins_x=None):
    """Mutual information I(X; Y) via binned joint histogram (bits).

    x: array of feature values (continuous or integer)
    y: array of class labels (discrete — one of the ω_d values here)

    Uses sqrt-N bin count for x by default. y is binned by its unique values.

    Returns MI in BITS (log base 2).
    """
    x = np.asarray(x, dtype=float)
    y = np.asarray(y)
    n = len(x)
    assert len(y) == n, "x and y must have the same length"

    if n_bins_x is None:
        n_bins_x = max(5, int(np.sqrt(n / len(np.unique(y)))))

    # Bin y by unique values; bin x by histogram
    y_vals = np.unique(y)
    y_to_idx = {v: i for i, v in enumerate(y_vals)}
    y_idx = np.array([y_to_idx[v] for v in y])

    x_edges = np.linspace(x.min() - 1e-9, x.max() + 1e-9, n_bins_x + 1)
    x_idx = np.clip(np.digitize(x, x_edges) - 1, 0, n_bins_x - 1)

    joint = np.zeros((n_bins_x, len(y_vals)))
    for xi, yi in zip(x_idx, y_idx):
        joint[xi, yi] += 1
    p_xy = joint / joint.sum()
    p_x  = p_xy.sum(axis=1, keepdims=True)
    p_y  = p_xy.sum(axis=0, keepdims=True)
    p_x_p_y = p_x @ p_y     # outer product

    # MI = Σ p_xy * log2(p_xy / (p_x · p_y)), with 0 where p_xy = 0
    with np.errstate(divide="ignore", invalid="ignore"):
        log_ratio = np.where((p_xy > 0) & (p_x_p_y > 0),
                             np.log2(p_xy / p_x_p_y), 0.0)
    return float((p_xy * log_ratio).sum())


# ============================================================================
# Sample collection
# ============================================================================

def collect_bond_counts(rate_fn, F_drive, omega_d_values,
                        n_seeds=N_SEEDS_LOCAL, n_steps=N_STEPS_LOCAL,
                        burn_fraction=BURN_FRACTION, base_seed=1000):
    """Run ensembles at each ω_d, collect (bond_count, ω_d_label) per Gillespie
    step (after burn-in). Returns (bond_counts, omega_labels) arrays."""
    bond_counts = []
    omega_labels = []
    for k, omega_d in enumerate(omega_d_values):
        for s in range(n_seeds):
            _, traj, _ = run_sim(
                n_steps=n_steps, omega=omega_d, F_drive=F_drive,
                seed=base_seed + 1000 * k + s, rate_fn=rate_fn,
            )
            burn = int(burn_fraction * len(traj))
            for r in traj[burn:]:
                bond_counts.append(r["n_bonds"])
                omega_labels.append(omega_d)
    return np.array(bond_counts), np.array(omega_labels)


def per_omega_distribution(bond_counts, omega_labels, omega_d_values):
    """Return mean and std of bond count at each ω_d (for inspection)."""
    rows = []
    for omega_d in omega_d_values:
        mask = omega_labels == omega_d
        if mask.sum() == 0:
            rows.append((omega_d, np.nan, np.nan, 0))
        else:
            rows.append((omega_d,
                         float(bond_counts[mask].mean()),
                         float(bond_counts[mask].std()),
                         int(mask.sum())))
    return rows


# ============================================================================
# Main
# ============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("Rescoped PREDICTION 2: I(A_feature ; ω_d_label) structural encoding")
    print("=" * 70)
    print()
    print(f"  N (particles)    = {N}")
    print(f"  ω_d values       = {OMEGA_D_VALUES}")
    print(f"  Seeds per ω_d    = {N_SEEDS_LOCAL}")
    print(f"  Steps per seed   = {N_STEPS_LOCAL}")
    print(f"  Feature          = bond count (n_bonds at each Gillespie step)")
    print(f"  Burn fraction    = {BURN_FRACTION}")
    print(f"  Replicates       = {N_REPLICATES}")
    print()

    mis = []   # list of (mi_catch, mi_snap, mi_un) per replicate

    for rep in range(N_REPLICATES):
        offset = 100_000 * (rep + 1)
        print(f"--- Replicate {rep+1}/{N_REPLICATES} (base_seed offset = {offset}) ---")

        # Catch
        x_catch, y_catch = collect_bond_counts(
            catch_rates, F_drive=F_DRIVE,
            omega_d_values=OMEGA_D_VALUES, base_seed=1000 + offset,
        )
        mi_catch = binned_mi(x_catch, y_catch)

        # Snap
        x_snap, y_snap = collect_bond_counts(
            snap_rates, F_drive=F_DRIVE,
            omega_d_values=OMEGA_D_VALUES, base_seed=2000 + offset,
        )
        mi_snap = binned_mi(x_snap, y_snap)

        # Undriven control (F=0): MI should be ≈ 0 — baseline
        x_un, y_un = collect_bond_counts(
            catch_rates, F_drive=0.0,
            omega_d_values=OMEGA_D_VALUES, base_seed=3000 + offset,
        )
        mi_un = binned_mi(x_un, y_un)

        mis.append((mi_catch, mi_snap, mi_un))
        print(f"  catch = {mi_catch:.4f}  snap = {mi_snap:.4f}  undriven = {mi_un:.4f}")

        # Print per-ω_d distribution table for the first replicate only
        # (sanity check; subsequent replicates omit to keep output readable)
        if rep == 0:
            print()
            print("  Per-ω_d bond-count distributions (replicate 1, mean ± std):")
            print(f"    {'ω_d':>5} | {'CATCH':>16} | {'SNAP':>16} | {'UNDRIVEN':>16}")
            print(f"    {'-'*5} | {'-'*16} | {'-'*16} | {'-'*16}")
            dist_catch = per_omega_distribution(x_catch, y_catch, OMEGA_D_VALUES)
            dist_snap  = per_omega_distribution(x_snap,  y_snap,  OMEGA_D_VALUES)
            dist_un    = per_omega_distribution(x_un,    y_un,    OMEGA_D_VALUES)
            for (od, mc, sc, _), (_, ms, ss, _), (_, mu, su, _) in zip(
                dist_catch, dist_snap, dist_un
            ):
                print(f"    {od:5.2f} | {mc:7.2f} ± {sc:5.2f}  | "
                      f"{ms:7.2f} ± {ss:5.2f}  | {mu:7.2f} ± {su:5.2f}")
        print()

    # ------------------------------------------------------------------
    # Summary across replicates
    # ------------------------------------------------------------------
    mis = np.array(mis)
    means = mis.mean(axis=0)
    stds  = mis.std(axis=0)

    print("=" * 70)
    print(f"Summary across {N_REPLICATES} independent ensemble replicates")
    print("=" * 70)
    print()
    print(f"  Regime    |   mean MI    |    std MI    | individual replicates")
    print(f"  --------  | -----------  | -----------  | ---------------------")
    for label, idx in [("CATCH", 0), ("SNAP", 1), ("UNDRIVEN", 2)]:
        indiv = "  ".join(f"{v:.4f}" for v in mis[:, idx])
        print(f"  {label:8s}  | {means[idx]:.4f}      | {stds[idx]:.4f}      | {indiv}")
    print()

    # Compare catch vs snap with respect to their variability
    diff_mean = means[0] - means[1]
    diff_std  = np.sqrt(stds[0]**2 + stds[1]**2)   # approx combined std
    print(f"  catch − snap = {diff_mean:+.4f} ± {diff_std:.4f} bits")
    print(f"  (positive favors the original prediction; negative means snap > catch)")
    print()
    print(f"  catch / undriven = {means[0] / max(means[2], 1e-9):.1f}× baseline")
    print(f"  snap  / undriven = {means[1] / max(means[2], 1e-9):.1f}× baseline")
    print()
    print("Note: bond count is a 1-D feature and probably the wrong observable")
    print("for testing the half-space-vs-point asymmetry. This run estimates")
    print("the VARIANCE so we know whether snap > catch is real noise or signal.")
