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

    Reproduction status (2026-05-30, partial close on spine §5 gate 1):
      Catch + undriven: faithfully reproduced at the supp's stated parameters
        (β = 4000, ε = 0.0001) under N_SEEDS = 5 ensemble averaging.
      Snap: QUALITATIVELY reproduced — visible avoidance dip at ω_d, slight
        rightward shift of the haystack tail vs the undriven baseline — but
        NOT quantitatively. Kachman's published Fig S8 green shows a SHARP
        ZERO at ω_d and a tight bell at ω ≈ 3.7; ours has a small residual
        at ω_d (~0.08) and a broader haystack at ω ≈ 3.0.
      The PUBLISHED green curve strongly supports PREDICTION 1; OUR
      reproduction supports it qualitatively but weakly. Kachman's snap
      parameters are unpublished (supp p13: "qualitative results not finely
      sensitive") and we have not yet found a set that strongly reproduces
      the sharp Fig S8 shape. Parameter exploration could close this further.

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

    Why the asymmetry is structural, not coincidental:
        CATCH's target is a POINT in frequency space ("match ω_d exactly").
        Configurations satisfying it carry ~log(precision-of-ω_d) bits about
        the drive. The selection is information-DEMANDING.
        SNAP's target is a HALF-SPACE ("be anywhere except near ω_d").
        Configurations satisfying it carry approximately "not here" — much
        less information. The selection is information-CHEAP.
    The Still-bound runs identically in both directions; the asymmetric
    INFORMATIONAL CONTENT of catch's vs. snap's targets is what makes I_pred
    diverge between the two regimes. This also explains Kachman et al.'s
    supplemental remark that snap's "qualitative results [are] not finely
    sensitive" to parameter choices — half-space targets are robust under
    perturbation; point targets are not (supp p13).

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


# All physics + plotting helpers live in kachman_lib.py (shared with
# kachman_stochastic.py). This script is the deterministic-single-sinusoid
# paper-reproduction artifact: Fig S8 (catch + undriven + snap).
from kachman_lib import (
    # Parameters
    BETA, EPSILON, B, M, K, F, OMEGA_D, N, K_0, I_DRIVE, R_0,
    N_STEPS, BETA_SNAP, N_THETA_SNAP, N_SEEDS,
    # Functions
    catch_rates, snap_rates, run_sim, run_ensemble, save_spectrum_plot,
)

if __name__ == "__main__":
    print(f"Kachman 2017 reference impl — Phase 1a-1c (catch bonds only).")
    print(f"Parameters: N={N}, ω_d={OMEGA_D}, β={BETA}, ε={EPSILON}, "
          f"b={B}, k={K}, F={F}, m={M}, k_0={K_0}")
    print(f"Running {N_STEPS} Gillespie steps from empty graph...")
    print()

    final_A, traj, _ = run_sim(seed=42)

    print(f"Final bond count: {int(final_A.sum() // 2)}")
    if traj:
        print(f"Total simulated time: {traj[-1]['t']:.4f}")
        n_form  = sum(1 for r in traj if r['event'] == 'form')
        n_break = sum(1 for r in traj if r['event'] == 'break')
        print(f"Events: {len(traj)} ({n_form} form, {n_break} break)")
    else:
        print("No events occurred (sim halted at step 0).")

    # ========================================================================
    # Phase 1d — Fig S8 reproduction: normal-mode spectrum, catch + undriven + snap.
    # ========================================================================
    print()
    print("=" * 70)
    print("Phase 1d — Fig S8 reproduction (catch + undriven + snap)")
    print("=" * 70)
    print()
    OMEGA_FIG = 1.5   # Fig S8's drive frequency
    print(f"Ensemble of N_SEEDS={N_SEEDS} runs per regime ({N_STEPS} Gillespie "
          f"steps each), ω_d = {OMEGA_FIG}.")
    print(f"Total: {3*N_SEEDS} sims; ~30s × {3*N_SEEDS} ≈ several minutes.")
    print()

    print(f"  Catch+drive ({N_SEEDS} seeds)...")
    samples_catch = run_ensemble(N_SEEDS, base_seed=100,
                                  omega=OMEGA_FIG, F_drive=10.0,
                                  rate_fn=catch_rates)
    print(f"  Undriven    ({N_SEEDS} seeds)...")
    samples_undriven = run_ensemble(N_SEEDS, base_seed=200,
                                     omega=OMEGA_FIG, F_drive=0.0,
                                     rate_fn=catch_rates)
    print(f"  Snap+drive  ({N_SEEDS} seeds)...")
    samples_snap = run_ensemble(N_SEEDS, base_seed=300,
                                 omega=OMEGA_FIG, F_drive=10.0,
                                 rate_fn=snap_rates)

    save_spectrum_plot(
        {"undriven": samples_undriven, "catch": samples_catch, "snap": samples_snap},
        omega_d=OMEGA_FIG,
        out_path="./out/kachman-fig-s8-reproduction.png",
    )
    print()
    print("Honesty test: CATCH peaks at ω_d (drive-seeking); SNAP avoids ω_d")
    print(f"(drive-avoiding); UNDRIVEN is the haystack baseline. ω_d = {OMEGA_FIG}.")
    print(f"Features surviving ensemble averaging (N_SEEDS={N_SEEDS}) are real;")
    print("features that disappear were single-trajectory artifacts.")


# === PHASE 2a: cluster-level coarse-graining of A ===


# === PHASE 2b: I_mem and I_pred estimators ===
# === FILL FROM PAPER === (still-2012-thermodynamics-of-prediction.pdf)


# === PHASE 2c: I_pred(evolutionary time) curves across regimes ===


# === PHASE 3a: storage channel + reproduction event on pacman-drive sim ===


# === PHASE 3b: M-axis sweep across catch / snap / catch+storage / snap+storage ===


# === PHASE 3c: locate M* (abiogenesis threshold), characterize scaling with K ===


# === PHASE 3d: document outcome — third strategy emerges or load-bearing falsification ===
