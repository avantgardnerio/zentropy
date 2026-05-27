"""
still.py — Zentropy sim, kernel-and-selection design (2026-05-27, supersedes zentropy.py's
opcode-tape-with-learning approach).

PLUMBING: Claude.   PHYSICS: Brent (=== FILL FROM PAPER === banners are yours).
Papers referenced live in papers/.

WHAT THIS TESTS (the novelty — NOT a re-demo of Still's theorem):
  Still 2012 proves predictive memory is *efficient* but holds the kernel FIXED — she never
  lets anything reproduce. Here we make the kernel HERITABLE and put it under differential
  reproduction (Darwin) and ask: does her per-individual efficiency gradient convert into an
  EVOLUTIONARY ascent in predictive memory?  The deliverable is the law  N*(M)  — the optimal
  memory capacity as a function of environmental complexity.   Pre-registered prediction: N* ≈ 2M.

DESIGN (see memory/project-sim-england-state.md, 2026-05-27 sections):
  - Agent = a fixed-per-life Markov kernel p(s_t | s_{t-1}, x_t)  [Still 2012, "Problem setup", p1-2].
    Represented as N internal free-running oscillators with INHERITED frequencies/phases.
    The oscillator phases ARE the memory state s_t.  No within-life learning, no OMEGA handed in
    (the agent free-runs its own inherited frequency guesses; selection tunes them).
    dumb = smart(N=0) (no oscillators, reactive) ... smart = smart(N>0).  One continuum.
  - Drive  x(t) = noise + M incommensurate (NON-harmonic) sinusoids  [Still: P_X unknown to system].
    M=0 pure noise (null).  Incommensurate => each freq needs its own oscillator => N* ~ 2M.
  - Selection = energy-limited reproduction (differential growth), independent colonies.
  - Two info costs, both Landauer-pinned (count bits; physics sets price = LN2, never hand-set):
      (a) REPLICATION: copy genome = genome_bits * LN2   [Bennett 2003, papers/bennett-2003-...].
      (b) PER-TICK non-predictive-memory dissipation  [Still 2012 bound] — LOAD-BEARING, see stub.

Run:  python still.py
NOTE: physics is STUBBED. Printed numbers are NOT a result until the === FILL FROM PAPER === land.
"""

import math
import random
from collections import Counter

LN2 = math.log(2)
PHI = (1 + 5 ** 0.5) / 2          # golden ratio — generates incommensurate (non-harmonic) freqs

# ===========================================================================
# PHYSICS CONSTANTS
# ===========================================================================
# --- Landauer-pinned info costs (NOT free knobs: magnitude is LN2 per irreversible bit) ---
BITS_PER_OSC   = 8                # genome bits to encode one oscillator (freq+phase). ISA choice; sweep.
COST_PER_BIT   = LN2              # replication: per genome bit copied  [Bennett 2003 (papers/)]

# --- BS / sweep knobs (NO paper sets these; they are the calibration to SWEEP, never cherry-pick) ---
SIG_AMP        = 1.0             # BS: per-sinusoid amplitude
NOISE_AMP      = 0.5             # BS: noise stddev. NB: SNR = SIG_AMP/NOISE_AMP is a hidden axis — CONTROL it.
COST_EAT       = 5.0 * LN2        # BS: metabolic cost of one eat attempt
PELLET_PEAK    = 30.0 * LN2       # BS: reward from a perfectly-timed eat
INIT_ENERGY    = 60.0 * LN2       # BS: child endowment
REPRO_THRESHOLD = 120.0 * LN2     # BS: energy needed to reproduce
MUT_RATE       = 0.1              # BS: stddev of gaussian freq/phase mutation on copy
EAT_THRESHOLD  = 0.5              # BS: predicted-drive level above which the agent attempts to eat

BASE_FREQ      = 0.3              # BS: fundamental angular frequency of the drive

# ===========================================================================
# DRIVE:  noise + M incommensurate sinusoids.   x(t) unknown to the agent.  [Still 2012, lines 37-48]
# This part is honest plumbing (signal generation), not stubbed physics.
# ===========================================================================
class Drive:
    def __init__(self, M, rng):
        # Incommensurate freqs via golden-ratio spacing => guaranteed non-harmonic (no freq is an
        # integer multiple of another), so each genuinely needs its own oscillator to track.
        self.freqs  = [BASE_FREQ * (PHI ** i) for i in range(M)]
        self.phases = [rng.uniform(0, 2 * math.pi) for _ in range(M)]
        self.rng = rng

    def value(self, t):
        sig = sum(SIG_AMP * math.sin(f * t + p) for f, p in zip(self.freqs, self.phases))
        return sig + self.rng.gauss(0.0, NOISE_AMP)

# ===========================================================================
# MUTUAL-INFORMATION ESTIMATOR  (plug-in/histogram; tiny discrete space so it's ~exact)
#   I_pred = MI( agent memory state s_t ; FUTURE drive x_{t+k} )   [Still 2012].
#   === FILL FROM PAPER ===  *which* variables go in is a Still modeling choice (Problem setup, p1-2);
#   the (discretized internal phase) vs (future drive sign) default below is a placeholder.
# ===========================================================================
def mutual_information(samples_xy):
    n = len(samples_xy)
    if n == 0:
        return 0.0
    pxy = Counter(samples_xy)
    px  = Counter(x for x, _ in samples_xy)
    py  = Counter(y for _, y in samples_xy)
    I = 0.0
    for (x, y), c in pxy.items():
        p_xy, p_x, p_y = c / n, px[x] / n, py[y] / n
        I += p_xy * math.log2(p_xy / (p_x * p_y))
    return I

# ===========================================================================
# AGENT  —  N free-running inherited oscillators.  Kernel is FIXED per life (Still); selection tunes it.
# ===========================================================================
class Agent:
    def __init__(self, freqs, phases, rng):
        self.freqs  = list(freqs)            # inherited oscillator frequencies (the agent's GUESSES)
        self.phases = list(phases)           # inherited initial phases
        self.N = len(self.freqs)             # memory capacity (dumb = 0)
        self.genome_bits = self.N * BITS_PER_OSC
        self.energy = INIT_ENERGY
        self.rng = rng

    def internal_state(self, t):
        """The memory state s_t = current oscillator phases (free-running, NOT entrained).
        === FILL FROM PAPER / YOUR CALL ===  pure free-run drifts out of phase unless freq matches
        exactly; real clocks ENTRAIN by sensing — but entrainment = within-life learning = the BRAINS
        rung, deferred. Decide: free-run (genomic only) vs allow light entrainment."""
        return tuple(int(((f * t + p) % (2 * math.pi)) / (2 * math.pi) * 8) % 8
                     for f, p in zip(self.freqs, self.phases))

    def predict_high(self, t):
        """Predict next drive is 'up' from internal oscillators alone (no sensing of x)."""
        if self.N == 0:
            return True                      # dumb: blind, always attempts
        pred = sum(math.sin(f * (t + 1) + p) for f, p in zip(self.freqs, self.phases))
        return pred > EAT_THRESHOLD

    def step(self, drive, t):
        # (1) Still per-tick dissipation from NON-PREDICTIVE memory carried this tick.
        # === FILL FROM PAPER ===  Still 2012 bound:  W_diss >= kT * (I_mem - I_pred).
        # This term is LOAD-BEARING: it is what makes OVER-memory (N>N*) selected-against. Without a
        # faithful form here, extra oscillators are free and smart wins everywhere (the known bug).
        # STUB: charge LN2 per oscillator that is NOT currently tracking the drive (crude proxy for
        # non-predictive bits). Replace with the real I_mem - I_pred accounting.
        self.energy -= self._stub_nonpredictive_cost()

        # (2) act: if we predict 'up', attempt to eat; success couples to the ACTUAL drive.
        if self.predict_high(t):
            self.energy -= COST_EAT
            if self._eat_succeeds(drive, t):
                self.energy += PELLET_PEAK    # === FILL: reward profile ∝ how 'up' the drive is

    def _stub_nonpredictive_cost(self):
        # STUB proxy: cost ∝ memory carried. Real version: LN2 * (I_mem - I_pred). [Still 2012]
        return self.N * LN2

    def _eat_succeeds(self, drive, t):
        """=== FILL FROM PAPER ===  England PME 2016, Eq 9, p15 (Arrhenius rate over the driven
        barrier). This is THE Crooks-faithful microdynamics; it belongs in england.py and should be
        imported here so still.py and england.py share ONE physics core (also the kernel in
        Kachman-Owen-England 2017, the 20-particle benchmark). STUB: deterministic threshold."""
        return drive.value(t) > EAT_THRESHOLD

    def reproduce(self):
        if self.energy < REPRO_THRESHOLD:
            return None
        self.energy -= self.genome_bits * COST_PER_BIT   # Landauer copy cost (ordered structure)
        self.energy -= INIT_ENERGY                        # endow child
        # mutate inherited freqs/phases (tunes the kernel; N held fixed within a sweep cell)
        f = [x + self.rng.gauss(0, MUT_RATE) for x in self.freqs]
        p = [(x + self.rng.gauss(0, MUT_RATE)) % (2 * math.pi) for x in self.phases]
        return Agent(f, p, self.rng)

# ===========================================================================
# RUN one (N, M) cell:  a colony of N-capacity agents in an M-complexity drive.
# ===========================================================================
def run(N, M, n_ticks, pop_cap, rng, future_lag=3):
    drive = Drive(M, rng)
    pop = [Agent([BASE_FREQ * (PHI ** i) * (1 + rng.gauss(0, MUT_RATE)) for i in range(N)],
                 [rng.uniform(0, 2 * math.pi) for _ in range(N)], rng)
           for _ in range(8)]                              # seed colony
    ipred_samples = []
    for t in range(n_ticks):
        newborns = []
        for a in pop:
            if N > 0:
                fut = 1 if drive.value(t + future_lag) > 0 else 0   # FUTURE drive sign
                ipred_samples.append((a.internal_state(t), fut))    # (memory state ; future) [Still]
            a.step(drive, t)
            child = a.reproduce()
            if child is not None and len(pop) + len(newborns) < pop_cap:
                newborns.append(child)
        pop = [a for a in pop if a.energy > 0] + newborns
        if not pop:
            break
    growth = len(pop)                                       # crude fitness proxy = final headcount
    return growth, mutual_information(ipred_samples)

# ===========================================================================
# THE N x M SWEEP  (the pre-registered phase diagram; deliverable = N*(M))
# ===========================================================================
if __name__ == "__main__":
    N_TICKS, POP_CAP = 2000, 400
    N_VALUES = [0, 1, 2, 3, 4, 5, 6]
    M_VALUES = [0, 1, 2, 3]
    print("Phase diagram: final population (fitness proxy) per (N memory, M env-complexity)")
    print("Pre-registered prediction: N* ≈ 2M  (best-growing N rises with M).\n")
    header = "N\\M  " + "".join(f"{('M='+str(m)):>9}" for m in M_VALUES)
    print(header)
    best_per_M = {m: (-1, -1) for m in M_VALUES}            # m -> (best_growth, argN)
    for N in N_VALUES:
        row = f"{N:<4} "
        for M in M_VALUES:
            g, ip = run(N, M, N_TICKS, POP_CAP, random.Random(0))
            row += f"{g:>9}"
            if g > best_per_M[M][0]:
                best_per_M[M] = (g, N)
        print(row)
    print("\nN*(M)  (argmax-growth memory per environment):")
    for m in M_VALUES:
        print(f"  M={m}:  N* = {best_per_M[m][1]}   (predicted ≈ {2*m})")
    print("\nPhysics is STUBBED (=== FILL FROM PAPER ===): the Eq-9 Arrhenius eat-rule and the")
    print("Still non-predictive-memory dissipation are placeholders — numbers are NOT a result yet.")
    print("Watch: smart wins everywhere -> Still-cost stub too weak; nowhere -> framework wrong.")
