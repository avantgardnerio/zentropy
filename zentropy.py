"""
zentropy.py — the first HONEST zentropy sim: England's kernel + Still/Ouldridge's
COMPUTED dissipation + Darwin's selection, composed into one experiment.
(2026-05-27. Supersedes the tape-agent zentropy.py and the sampling-MI approach in still.py.)

WHY THIS IS "zentropy" AND NOT "still.py" OR "ouldridge.py":
  zentropy := the thermodynamic value of prediction UNDER SELECTION (definitions.md, Claim 1;
  the one cell Still/England/Ouldridge/Koonin each leave empty). This file is the first to
  compose all three pillars into that cell:
    - England (PME-2016, Eq-9): the local-detailed-balance Arrhenius kernel = the dissipative-
      structure engine.                                                          [life criterion 2]
    - Still 2012 / Ouldridge 2017: ONE ledger, not two mechanisms. Dissipation = correlation you
      build but don't cash. We COMPUTE it as entropy production  sigma = sum ln(k_fwd/k_rev)  from
      the kernel's OWN rates -- never sampled MI (which blows up as 8^N and biases the wrong way).
      Ouldridge = frozen-source corner (copy cost w >= kT*I, paid at replication below);
      Still = moving-source generalization (the nonpredictive part is what dissipates). [criterion 1]
    - Darwin: heritable kernel + energy-limited differential reproduction = the novelty none did.
  Deliverable: the law N*(M) -- optimal memory capacity vs environmental complexity. Predict N* ~ 2M.

PLUMBING: Claude.   PHYSICS (=== FILL FROM PAPER ===): Brent.
  The sigma accounting and the selection are HONEST even with provisional constants: sigma from any
  LDB-valid rates is genuine entropy production; the PAPER only calibrates magnitudes. The kernel
  here is provisional and inline -- move it into england.py once that reproduces the PME Fig-3 drift,
  so both files share ONE physics core.

WHAT THIS FIXES: the 'smart wins everywhere' bug still.py flagged. The cost of carrying memory that
  does NOT predict is now REAL dissipation (sigma computed from rates), not a hand-set N*LN2 fudge.
  If over-memory still wins everywhere here, the bias map / harvest coupling is wrong -- not the knob.

Run:  python zentropy.py
NOTE: physics is STUBBED at the === FILL FROM PAPER === banners. Printed numbers are NOT a result yet.
"""

import math
import random

LN2 = math.log(2)
PHI = (1 + 5 ** 0.5) / 2            # golden ratio -> incommensurate (non-harmonic) drive freqs

# ===========================================================================
# PHYSICS CONSTANTS
# ===========================================================================
# --- Landauer-pinned (NOT free knobs; price is LN2 per irreversible bit) ---
BITS_PER_UNIT = 8                  # === FILL FROM PAPER ===: genome bits per memory unit. Should be
                                   # DERIVED from environmental precision demand (~ Koonin K~S), NOT the
                                   # float's 64-bit storage width (an implementation artifact -- mostly
                                   # unselected, nonpredictive bits). 8 is a deliberate, sweepable stub.
COST_PER_BIT  = LN2                # copy cost per bit AT PERFECT FIDELITY [Bennett 2003]. Scaled below
                                   # by the copy's mutual information (1 - H2(s)) -- Ouldridge Eq 19.

# --- provisional Arrhenius / coupling magnitudes (=== FILL FROM PAPER: PME-2016 Eq-9, p15 ===) ---
# These set the SHAPE; exact values are the calibration to SWEEP, never cherry-pick.
BARRIER       = 2.0                # provisional hop barrier (kT units)
BIAS_GAIN     = 3.0                # provisional: how strongly the prediction biases harvest rate
DG_HARVEST    = 30.0 * LN2         # provisional free energy captured per successful harvest event
BASAL         = 1.0 * LN2          # maintenance dissipation per tick (boundary upkeep)
INIT_ENERGY   = 60.0 * LN2
REPRO_THRESHOLD = 120.0 * LN2      # energy to be 'mature enough' to ATTEMPT a copy
ACCURACY_S    = 0.99               # copy fidelity -- HYPER-PARAMETER, the controlled axis to SWEEP.
                                   # NOT heritable (one free trait per sim). 0.5 = coin, 1.0 = perfect.
MUT_SCALE     = 0.5                # representation artifact: float-perturbation per unit copy-error.
                                   # Vanishes under a bit-encoded genome. BS/sweep knob, not biology.
SEED_SPREAD   = 0.1                # initial colony diversity (setup), distinct from copy fidelity. BS.
SIG_AMP, NOISE_AMP = 1.0, 0.5      # drive signal vs noise; SNR is a hidden axis -- CONTROL it
BASE_FREQ     = 0.3

# ===========================================================================
# DRIVE:  noise + M incommensurate sinusoids.  x(t) unknown to the agent.  [Still 2012]
# Honest plumbing (signal generation), not stubbed physics.
# ===========================================================================
class Drive:
    def __init__(self, M, rng):
        self.freqs  = [BASE_FREQ * (PHI ** i) for i in range(M)]   # non-harmonic => each needs its own unit
        self.phases = [rng.uniform(0, 2 * math.pi) for _ in range(M)]
        self.rng = rng

    def value(self, t):
        sig = sum(SIG_AMP * math.sin(f * t + p) for f, p in zip(self.freqs, self.phases))
        return sig + self.rng.gauss(0.0, NOISE_AMP)

# ===========================================================================
# LDB KERNEL HELPERS  (=== FILL FROM PAPER ===: exact Eq-9 form/constants -> england.py)
# The ONLY non-negotiable: every transition has a defined reverse, so sigma is well-defined.
# ===========================================================================
def arrhenius(barrier_minus_bias):
    """Eq-9 shape: hop rate ~ exp(-(barrier - bias)). Provisional; calibrate to PME-2016 p15."""
    return math.exp(-barrier_minus_bias)

def fire(k_fwd, k_rev, rng):
    """One stochastic LDB transition this tick. Returns (fired?, entropy_to_bath_in_nats).
    Entropy produced = ln(k_fwd/k_rev) when forward fires (can be < 0 on a tick = a 'cashed
    fluctuation', exactly the Still/Ouldridge correlation-harvest event). <sigma> >= 0 over time."""
    p_fwd = k_fwd / (k_fwd + k_rev)
    if rng.random() < p_fwd:
        return True,  math.log(k_fwd / k_rev)
    return False,     math.log(k_rev / k_fwd)

# ===========================================================================
# COPY FIDELITY -> DISSIPATION   (=== FILL FROM PAPER ===: Ouldridge 2017)
# Mutations are NOT a separate op -- they ARE the errors of a finite-fidelity copy. Fidelity s sets
# BOTH the error rate (1-s) AND the cost. Cost per bit = the copy's mutual information:
#     f(s) = 1 - H2(s)     [Eq 19, the IDEAL/reversible floor; finite, caps at 1 bit/copy at s=1].
# The AUTONOMOUS realized cost (what LIFE pays) is >=2x this and DIVERGES as s->1 (Eq 20 / Fig 2) --
# that divergence IS the thermodynamic mutation-rate floor. Swap copy_info_per_bit to surface it.
# ===========================================================================
def binary_entropy(s):
    if s <= 0.0 or s >= 1.0:
        return 0.0
    return -s * math.log2(s) - (1 - s) * math.log2(1 - s)

def copy_info_per_bit(s):
    """f(s) = 1 - H2(s): bits of info per copied bit = Ouldridge's I (Eq 19), the IDEAL floor.
    === FILL FROM PAPER ===  swap in the autonomous (diverging) form from Eq 20 / Fig 2 for life."""
    return 1.0 - binary_entropy(s)

# ===========================================================================
# AGENT  -- N memory units, each a 2-state stochastic element with INHERITED rate-bias params.
# The kernel is fixed per life (Still); selection tunes the inherited params across generations.
# dumb = N=0 (no memory, reactive).  smart = N>0.  One continuum.
# ===========================================================================
class Agent:
    def __init__(self, freqs, s, rng):
        self.freqs = list(freqs)              # inherited per-unit frequency GUESSES (the heritable kernel)
        self.s = s                            # copy fidelity (fixed hyper-parameter, not heritable)
        self.N = len(self.freqs)
        self.state = [0] * self.N             # memory units (stochastic up/down)
        self.genome_bits = self.N * BITS_PER_UNIT
        self.energy = INIT_ENERGY
        self.rng = rng

    def step(self, drive, t):
        sigma = 0.0                           # entropy produced this tick (COMPUTED, not sampled)

        # (1) Each memory unit hops via an LDB transition whose rates are biased by its inherited
        #     guess. A unit "wants up" when its internal oscillator says up.
        #     === FILL FROM PAPER ===  The prediction->rate-bias map is YOURS (see the definitions.md
        #     TODO + Still's "which variables" modeling choice). Provisional sinusoid bias below.
        for i in range(self.N):
            bias = math.sin(self.freqs[i] * t)
            if self.state[i] == 0:
                fired, ds = fire(arrhenius(BARRIER - bias), arrhenius(BARRIER + bias), self.rng)
                if fired: self.state[i] = 1
            else:
                fired, ds = fire(arrhenius(BARRIER + bias), arrhenius(BARRIER - bias), self.rng)
                if fired: self.state[i] = 0
            sigma += ds

        # (2) GRADED harvest (no threshold collapse): the better memory predicts the ACTUAL drive,
        #     the faster the harvest reaction runs. Work captured when it fires; sigma it produces is
        #     part of the same ledger. dumb (N=0) has alignment=1 baseline => blind constant attempt.
        #     === FILL FROM PAPER ===  harvest coupling + the work/heat split are yours.
        x_up = 1.0 if drive.value(t) > 0 else 0.0
        align_up = (sum(self.state) / self.N) if self.N else 1.0
        match = align_up * x_up + (1 - align_up) * (1 - x_up)     # 1 = predicted right, 0 = predicted wrong
        fired, ds = fire(arrhenius(BARRIER - BIAS_GAIN * match), arrhenius(BARRIER), self.rng)
        sigma += ds
        if fired:
            self.energy += DG_HARVEST

        # (3) pay maintenance + the computed dissipation. Charging SIGNED sigma is the honest move:
        #     nonpredictive memory transitions cost (Still); occasional cashed fluctuations refund.
        #     This term is what makes N>N* selected-against WITHOUT a hand-set penalty.
        self.energy -= BASAL
        self.energy -= sigma
        return sigma

    def reproduce(self):
        """Attempt to copy the genome at fidelity s, then DIE TRYING if you can't finish.
        Returns (child_or_None, sigma_copy). sigma_copy is dissipated (and tracked) even on failure."""
        if self.energy < REPRO_THRESHOLD:                    # not mature enough to even attempt
            return None, 0.0
        sigma_copy = self.genome_bits * COST_PER_BIT * copy_info_per_bit(self.s)
        self.energy -= sigma_copy                            # committed: pay the copy dissipation
        if self.energy < INIT_ENERGY:                        # can't endow a child after paying -> died trying
            return None, sigma_copy                          # energy spent, no offspring (high-fidelity tax)
        self.energy -= INIT_ENERGY                           # endow child
        # mutations ARE the copy errors: fidelity s sets their magnitude (=== representation stub:
        # float-perturbation proxy; faithful version flips bits of a bit-encoded genome ===).
        err = MUT_SCALE * (1.0 - self.s)
        f = [v + self.rng.gauss(0, err) for v in self.freqs]
        return Agent(f, self.s, self.rng), sigma_copy

# ===========================================================================
# RUN one (N, M) cell:  a colony of N-capacity agents in an M-complexity drive.
# ===========================================================================
def run(N, M, n_ticks, pop_cap, rng, s=ACCURACY_S):
    drive = Drive(M, rng)
    pop = [Agent([BASE_FREQ * (PHI ** i) * (1 + rng.gauss(0, SEED_SPREAD)) for i in range(N)], s, rng)
           for _ in range(8)]
    total_sigma = 0.0
    for _ in range(n_ticks):
        newborns = []
        for a in pop:
            total_sigma += a.step(drive, _)
            child, sigma_copy = a.reproduce()
            total_sigma += sigma_copy
            if child is not None and len(pop) + len(newborns) < pop_cap:
                newborns.append(child)
        pop = [a for a in pop if a.energy > 0] + newborns
        if not pop:
            break
    return len(pop), total_sigma          # fitness proxy = final headcount; sigma = computed dissipation

# ===========================================================================
# THE N x M SWEEP  (the pre-registered phase diagram; deliverable = N*(M))
# ===========================================================================
if __name__ == "__main__":
    N_TICKS, POP_CAP = 2000, 400
    N_VALUES = [0, 1, 2, 3, 4, 5, 6]
    M_VALUES = [0, 1, 2, 3]
    print("zentropy.py -- England kernel + Still/Ouldridge COMPUTED dissipation + selection.")
    print("Phase diagram: final population (fitness proxy) per (N memory capacity, M env-complexity).")
    print("Pre-registered prediction: N* ~ 2M  (best-growing N rises with environmental complexity).")
    print(f"Copy fidelity s = {ACCURACY_S}  (HYPER-PARAMETER -- sweep this axis; NOT heritable).\n")
    print("N\\M  " + "".join(f"{('M='+str(m)):>9}" for m in M_VALUES))
    best = {m: (-1, -1) for m in M_VALUES}
    for N in N_VALUES:
        row = f"{N:<4} "
        for M in M_VALUES:
            g, _sigma = run(N, M, N_TICKS, POP_CAP, random.Random(0))
            row += f"{g:>9}"
            if g > best[M][0]:
                best[M] = (g, N)
        print(row)
    print("\nN*(M)  (argmax-growth memory per environment):")
    for m in M_VALUES:
        print(f"  M={m}:  N* = {best[m][1]}   (predicted ~ {2 * m})")
    # Convergent-derivation check (once physics stubs are filled): N*(M) slope vs Koonin K ~ S
    # (Vanchurin-Koonin 2022, PNAS p6) -- same law, reached via Friston w/ no thermodynamics, no sim.
    # Two independent routes to one law = unification, not synthesis. See definitions.md Claim 1.
    print("\n  [cross-check N*(M) slope vs Koonin K~S (PNAS 2022, p6) -- convergent derivation]")
    print("\nPhysics STUBBED at === FILL FROM PAPER ===: provisional Arrhenius constants, the")
    print("prediction->rate-bias map, and the harvest work/heat split. Dissipation (sigma) is")
    print("computed honestly from the LDB rates; only the MAGNITUDES await PME-2016 Eq-9 calibration.")
    print("Copy: mutations are now the errors of a fidelity-s copy; sigma_copy = (1-H2(s))*bits*LN2")
    print("(Ouldridge Eq 19, ideal floor). Swap the autonomous-diverging form (Eq 20/Fig 2) to see the")
    print("mutation-rate floor -- at high s, agents pay the copy tax and die trying.")
    print("Watch: smart wins everywhere -> bias map/harvest coupling wrong; nowhere -> framework wrong.")
