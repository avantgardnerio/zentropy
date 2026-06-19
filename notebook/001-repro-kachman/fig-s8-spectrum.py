"""
notebook/001-repro-kachman/fig-s8-spectrum.py

Reproduce Kachman 2017 supp Fig S8 — normal-mode frequency distribution
P(ω) for the driven system at ω_d = 1.5, with three regimes overlaid:

  catch    (red)    — drive-seeking bonds; sharp peak AT ω_d
  undriven (blue)   — control; broad haystack centered around ω ≈ 2.5–3
  snap     (green)  — drive-avoiding bonds; avoidance dip at ω_d, mass
                      pushed to higher ω

Provenance: this reproduction was developed in `kachman.py`'s main block
(commits af40c61, 0f00d9d, 5738ba2 area) and is being lifted into the
lab notebook unchanged as the baseline reproducibility anchor. Same
parameters, same RNG seeds, same physics helpers from `kachman_lib`.

Honesty notes (from spine.md §5 gate 1 partial close):
  - CATCH reproduction is solid quantitatively (sharp peak at ω_d, with
    the broader haystack rightward).
  - SNAP reproduction is QUALITATIVE: visible avoidance dip at ω_d and
    rightward shift of the haystack tail vs undriven, confirmed under
    N_SEEDS=5 ensemble averaging. NOT a quantitative match — Kachman's
    published green has a sharp zero at ω_d and a tight bell at ω ≈ 3.7;
    ours has a small residual at ω_d and a broader haystack at ω ≈ 3.0.
    Kachman's snap parameters are unpublished (supp p13: "qualitative
    results not finely sensitive to these choices") — see kachman_lib
    BETA_SNAP = 6.0 (empirically chosen) for the parameter we picked.
"""

import os
import sys

# Notebook entries live two levels below the repo root; put it on sys.path
# so `kachman_lib` resolves regardless of where the script is invoked from.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                 "..", "..")))

from kachman_lib import (
    N, N_STEPS, N_SEEDS,
    catch_rates, snap_rates,
    run_ensemble, save_spectrum_plot,
)


# ---- Parameters (frozen at the values that produced the known result) -----
OMEGA_D     = 1.5
F_DRIVE     = 10.0
SEED_CATCH    = 100
SEED_UNDRIVEN = 200
SEED_SNAP     = 300

OUT_PATH = os.path.join(os.path.dirname(__file__), "fig-s8-spectrum.png")


# ---- Main ------------------------------------------------------------------
if __name__ == "__main__":
    print(f"Kachman Fig S8 reproduction (notebook/001-repro-kachman)")
    print(f"  N={N}, ω_d={OMEGA_D}, F={F_DRIVE}, "
          f"N_SEEDS={N_SEEDS}, N_STEPS={N_STEPS} per seed")
    print()

    print(f"  Catch+drive ({N_SEEDS} seeds)...")
    samples_catch = run_ensemble(
        N_SEEDS, base_seed=SEED_CATCH,
        omega=OMEGA_D, F_drive=F_DRIVE, rate_fn=catch_rates,
    )

    print(f"  Undriven    ({N_SEEDS} seeds)...")
    samples_undriven = run_ensemble(
        N_SEEDS, base_seed=SEED_UNDRIVEN,
        omega=OMEGA_D, F_drive=0.0, rate_fn=catch_rates,
    )

    print(f"  Snap+drive  ({N_SEEDS} seeds)...")
    samples_snap = run_ensemble(
        N_SEEDS, base_seed=SEED_SNAP,
        omega=OMEGA_D, F_drive=F_DRIVE, rate_fn=snap_rates,
    )

    save_spectrum_plot(
        {"undriven": samples_undriven,
         "catch":    samples_catch,
         "snap":     samples_snap},
        omega_d=OMEGA_D,
        out_path=OUT_PATH,
        title=f"Kachman Fig S8 reproduction  (N={N}, ω_d={OMEGA_D}, "
              f"F={F_DRIVE}, N_SEEDS={N_SEEDS})",
    )
    print()
    print(f"Saved: {OUT_PATH}")
