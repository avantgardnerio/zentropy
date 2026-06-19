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

PREDICTION 4 — acquisition cost vs storage cost decoupling. [Refinement of
                                                              Still's bound;
                                                              spine.md §7.]

    Standard Landauer / Bennett / Still accounting focuses on the cost of
    STORING or erasing a bit. At molecular substrates, storage and
    acquisition are inseparable — the medium IS the thermal bath, so the
    marginal cost of one more predictive bit is approximately the Landauer
    floor either way. At higher scales the two DECOUPLE: a hard drive's
    per-bit storage cost is many orders above Landauer but amortizes to
    near-zero per relevant transaction, while the cost to IDENTIFY which
    bit to store (acquisition cost) rises because it is set endogenously
    by competing predictors (Grossman & Stiglitz 1980; Van Valen 1973
    Red Queen).

    Zentropy reframe (Brent, 2026-05-30): selection grades agents on cost-
    to-ACQUIRE the next predictive bit, not on cost-to-STORE. Storage was
    a reliable proxy at the molecular regime where the two coincide; it
    fails at higher scales. spine.md §7 carries the full statement.

    Cost decomposition (provisional):

        cost-per-acquired-bit ≈ max(thermal floor, adversarial floor)
            thermal floor    = k_B T · ln 2  (Landauer; physics-set)
            adversarial floor= marginal competing predictor's per-bit
                               expenditure  (Grossman-Stiglitz form;
                               population-set)

    Kachman is single-substrate with no competing predictors → only the
    THERMAL HALF of the claim is testable here. The adversarial half
    awaits multi-agent / multi-niche substrates (still.py with heritable-
    kernel competition, or pacman with multiple agents).

    The thermal-half tests, ordered by intrusiveness:

    4a. CUMULATIVE-DISSIPATION KNEE.  [Needs W_diss instrumentation in
                                       run_sim, then re-run; no substrate
                                       changes.]
        Note: kachman_lib.run_sim's trajectory dict currently tracks
        {step, t, event, ij, n_bonds} — W_diss is NOT tracked. To
        compute this, extend the trajectory dict with per-interval
        W_absorbed and Q_dissipated (the W and Q already implicit in the
        catch_rates / snap_rates Arrhenius integrals over each Gillespie
        interval; ~5 lines of instrumentation).
        Plot ∫ W_diss dτ vs t for the catch-driven run. Does the slope
        show a steeper initial period (the acquisition transient — the
        red box in Fig S2, t ∈ [0, ~500]) followed by a lower steady-
        state slope (maintenance)? The excess area above a steady-state-
        extrapolation line is the acquisition cost in joules.
        Falsification: no knee → storage/acquisition decoupling does not
        appear at the molecular regime where the framework is best
        anchored; the reframe is dead at substrate.

    4b. MARGINAL  dI / dW_diss  DECLINE.  [Needs 4a's W_diss instrumentation
                                           plus a per-window I estimator;
                                           can use measure_drive_encoding's
                                           I(A_feature ; ω_d) as near-term
                                           substitute for proper I_pred
                                           before Phase 2 lands.]
        For each Gillespie window, compute incremental structural-
        encoding gain (Phase 2's I_pred when it lands; near-term the
        I(A_feature ; ω_d) of measure_drive_encoding.py) divided by
        incremental W_diss since the previous window. Plot the ratio
        vs t.
        Prediction: HIGH early — structure laid down on top of nothing
        is cheap per bit. DECLINING as the system fills its niche, toward
        a steady-state floor (maintenance).
        Falsification: flat ratio → acquisition cost ≈ steady-state cost;
        the distinction is not load-bearing in this substrate.

    4c. HYSTERESIS TEST.  [New runs.]
        Drive (acquire) → equilibrate (F = 0, long enough that the bond
        network reverts toward equilibrium statistics) → re-drive at the
        same ω_d. Compare transient duration and cumulative dissipation
        during transient for the FIRST vs SECOND drive episode.
        Prediction: substrate retains latent topology bias from the first
        drive → second transient is SHORTER and/or CHEAPER.
        Falsification: identical first and second transients → re-
        acquisition is path-independent; "cost-to-re-learn" has no
        substrate-level traction.

    4d. QUENCH-DEPTH TEST.  [New runs.]
        Drive to steady state. Then re-equilibrate for VARYING durations
        (sweep equilibration time short / medium / long, sampling the
        spectrum of "fraction of structure lost"). Re-drive. Plot re-
        acquisition cost (∫ W_diss dτ during second transient) against
        fraction-of-structure-lost (measured by some structural distance
        from the original steady state — bond-count delta, or spectral
        distance, both will work).
        Prediction: NON-LINEAR curve — small losses are cheap to re-
        acquire, large losses approach full acquisition cost from
        scratch. The closest molecular analog to "re-acquiring predictive
        learning costs X."
        Falsification: linear scaling → acquisition cost is simply
        proportional to "amount of bank to refill"; no qualitative re-
        learning threshold exists in this substrate.

    Scheduling note — PREDICTION numbers group by zentropy claim and are
    NOT a build sequence. PREDICTION 4 sub-tests slot across multiple
    phases. Realistic build order (small to large):

      Phase 1.5  (after Phase 1d reproduction lands):
        - 4a needs ~5 lines of W_diss instrumentation in run_sim, then
          re-run the catch trajectories used for Fig S2.
        - 4c / 4d need only a runner script that does
          drive → equilibrate (F = 0) → drive cycles. No substrate or
          physics changes. Could run in parallel with 4a.

      Phase 2.5  (after 4a's W_diss instrumentation + a per-window I
                  estimator — either Phase 2's I_pred or the near-term
                  I(A_feature ; ω_d) substitute):
        - 4b becomes computable. Per feedback-sim-first: defer 4b unless
          4a shows a knee, since 4b is downstream of 4a's claim.

    Build the cheapest test first — 4a is the shortest path to ANY
    PREDICTION-4-relevant result. 4c/4d become worth the runner-script
    investment IF 4a confirms the knee. 4b waits on a per-window I
    estimator regardless.

    Term-audit TODO (per feedback-coined-terms). "Adversarial floor" is
    descriptive but not standard literature vocabulary. Grossman-Stiglitz
    1980 use "information acquisition cost"; biology side uses "Red Queen
    cost." Audit before promoting any of these tests to write-up.

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

Phase 3-prequel candidate (2026-06-17 — not committed): a bistable-bond
substrate variant sits between Phase 2 (single-well, structural encoding) and
Phase 3 (storage channel + replication via Gillespie copy). Adds one parameter
(double-well barrier height) to the bond potential and replaces the single
sinusoid with two non-harmonic sines at incommensurate ratio. Tests whether
storage CAPACITY alone (no replication) lets the substrate encode joint drive
structure across cycles — i.e. whether a "Strategy A.5" (storage-capable,
non-replicating) regime exists distinct from Strategy A. If yes, §6's binary
A-vs-B crossover may need a three-strategy refinement; if no, the direct jump
from single-well to replication remains the right shape. Discussion + caveats
in [[project-kachman-bistable-extension]]; not promoted to spine.md prose per
[[feedback-prose-formality]].

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


# === PHASE 1.5  (NEAR-TERM, after Phase 1d reproduction lands) ===
# PREDICTION numbers (1–4) group by zentropy claim; PHASE numbers reflect
# build order. PREDICTION 4 sub-tests deliberately span multiple phases.

# === PHASE 1.5a (PREDICTION 4a): instrument W_diss in run_sim's trajectory
#                 dict (~5 lines: per-interval W_absorbed + Q_dissipated from
#                 the Arrhenius integrals already in catch_rates / snap_rates).
#                 Then re-run a catch trajectory and plot ∫ W_diss dτ vs t.
#                 Does the slope show a transient (acquisition) vs steady-state
#                 (maintenance) split? Shortest path to ANY PREDICTION-4 result. ===


# === PHASE 1.5b (PREDICTION 4c): hysteresis runner — drive → equilibrate
#                 (F = 0) → drive at the same ω_d. Compare first vs second
#                 transient duration and cumulative W_diss. No substrate or
#                 physics changes; just a runner script. ===


# === PHASE 1.5c (PREDICTION 4d): quench-depth runner — Phase-1.5b variant
#                 sweeping equilibration duration. Plot re-acquisition cost
#                 vs fraction-of-structure-lost. Non-linear curve confirms;
#                 linear scaling falsifies. ===


# === PHASE 2a: cluster-level coarse-graining of A — see Phase 2 plan above ===


# === PHASE 2b: I_mem and I_pred estimators ===
# === FILL FROM PAPER === (still-2012-thermodynamics-of-prediction.pdf)


# === PHASE 2c: I_pred(evolutionary time) curves across regimes — PREDICTION 2 ===


# === PHASE 2.5  (PREDICTION 4b): marginal dI / dW_diss(t).
#                Needs Phase 1.5a's W_diss instrumentation + a per-window I
#                estimator (Phase 2b's I_pred when it lands, or near-term
#                measure_drive_encoding's I(A_feature ; ω_d)). Defer unless
#                Phase 1.5a shows the knee. ===


# === PHASE 3a: storage channel + reproduction event on pacman-drive sim ===


# === PHASE 3b: M-axis sweep across catch / snap / catch+storage / snap+storage ===


# === PHASE 3c: locate M* (abiogenesis threshold), characterize scaling with K ===


# === PHASE 3d: document outcome — third strategy emerges or load-bearing falsification ===
