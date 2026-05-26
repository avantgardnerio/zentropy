"""
Zentropy sim (Tier 1) — population of tape-agents on a finite board.

PLUMBING: Claude.  PHYSICS STUBS are marked  === FILL FROM PAPER === ; those are yours.
Supersedes simulation-design.md (per Brent, 2026-05-26).
england.py = Tier 0 (the faithful Eq-9 microdynamics, yours to fill). This file should
reuse that transition rule once it exists — for now it carries a dumb placeholder.

Question under test: does predictive memory pay for itself?
Pre-registered 2x2:  (predictable vs noise drive) x (constrained/small vs unconstrained/big board).
Zentropy predicts smart dominates in EXACTLY ONE cell: predictable AND constrained.
Everything in units of kT, so temperature drops out.

Run:  python zentropy.py
NOTE: physics is stubbed; the printed numbers are NOT a result until the stubs are filled.
"""

import math
import random
from collections import Counter
from enum import IntEnum

# ===========================================================================
# PHYSICS CONSTANTS — STUBS (units of kT). Replace magnitudes per cited sources.
# ===========================================================================
LN2 = math.log(2)                  # Landauer floor per irreversible bit-op [Bennett 2003 (papers/); Landauer 1961]
COST_READ         = LN2            # sensor reset per read   [Bennett: Maxwell's-demon resolution]
COST_WRITE_BIT    = LN2            # per memory bit overwritten   [Landauer erasure]
COST_PER_TAPE_BIT = LN2            # per bit of new structure created at replication

# ARBITRARY free params — no paper sets these; they are the knobs to SWEEP (never cherry-pick).
COST_EAT        = 5.0 * LN2        # STUB: action cost of one eat attempt.
PELLET_PEAK     = 30.0 * LN2       # STUB: energy from a perfectly-timed eat (reward profile).
INIT_ENERGY     = 60.0 * LN2       # STUB
REPRO_THRESHOLD = 120.0 * LN2      # STUB
BITS_PER_UPDATE = 4                # STUB: bits the delta-rule rewrites per learning step

OPCODE_BITS   = 3                  # 8 opcodes -> 3 bits. ISA choice; only the smart>dumb DIRECTION is robust.
REGISTER_BITS = 8                  # phase-register width (smart only)
OMEGA         = 0.3                # STUB: drive angular frequency (pellet cycle rate)
MATCH_WINDOW  = 0.5                # STUB: how close clock must be to guess to "eat now" (radians)

# ===========================================================================
# OPCODES + TAPES  (honest bit-count comes from tape length, not hand-assignment)
# ===========================================================================
class Op(IntEnum):
    EAT           = 0   # blind: pay COST_EAT; if pellet up, gain reward
    PROCREATE     = 1   # if able, copy tape into adjacent empty square (pay tape-bit cost)
    RECALL_PHASE  = 2   # load phase_guess (own-memory read ~ free)
    COMPARE_CLOCK = 3   # set match flag if clock ~ phase_guess
    EAT_IF_MATCH  = 4   # eat only when match flag set
    READ_OUTCOME  = 5   # pay COST_READ; observe the learning signal
    UPDATE_MEM    = 6   # pay COST_WRITE_BIT*BITS_PER_UPDATE; delta-rule update

DUMB_TAPE  = [Op.EAT, Op.PROCREATE]
SMART_TAPE = [Op.RECALL_PHASE, Op.COMPARE_CLOCK, Op.EAT_IF_MATCH,
              Op.READ_OUTCOME, Op.UPDATE_MEM, Op.PROCREATE]

def tape_bits(tape, has_register):
    return len(tape) * OPCODE_BITS + (REGISTER_BITS if has_register else 0)

# ===========================================================================
# DRIVE + TRANSITION RULE — STUBS.   === FILL FROM PAPER ===
# The transition rule is the make-or-break Crooks-faithful piece (PME 2016 Eq 9, p15).
# It belongs in england.py; this is a GLARINGLY DUMB placeholder so the scaffold runs.
# TODO(brent): once england.py reproduces the Eq-9 drift, import & reuse that here so the
# two sims share ONE physics core. If this rule isn't Crooks-faithful, Still/England won't emerge.
# ===========================================================================
def pellet_value(phase_offset, t):
    """Pellet fullness in [0,1] — England's time-varying field E(t). STUB: cosine."""
    return 0.5 * (1.0 + math.cos(OMEGA * t + phase_offset))

def eat_succeeds(phase_offset, t):
    """STUB: deterministic threshold. REPLACE with Eq-9 Arrhenius rate from england.py."""
    return pellet_value(phase_offset, t) > 0.5

def eat_reward(phase_offset, t):
    return PELLET_PEAK * pellet_value(phase_offset, t)

# ===========================================================================
# MUTUAL-INFORMATION ESTIMATOR  (real plumbing — you asked what this is)
# ---------------------------------------------------------------------------
# MI I(X;Y) in bits = how much knowing X reduces uncertainty about Y:
#     I = sum_xy  p(x,y) * log2[ p(x,y) / (p(x) p(y)) ]      ( = 0 iff independent ).
# This is the "plug-in / histogram" estimator: count frequencies from samples, plug in.
# Exact-ish here because the state space is tiny & discrete. Biased high for small N
# (fine for long runs; Miller-Madow correction if ever needed).
#
# I_pred = MI(agent memory ; FUTURE environment)   [Still 2012].
# === FILL FROM PAPER ===  *which* variables go in is a Still-modeling choice. The default
# below (phase-guess vs future pellet-up) is a placeholder; verify against Still. For the
# NOISE case it's especially crude (uses current phase to fake a "future" — see sample site).
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

def circular_diff(a, b):
    """Shortest signed angular distance a-b in (-pi, pi]  (for the phase delta-rule)."""
    return (a - b + math.pi) % (2 * math.pi) - math.pi

def discretize_phase(theta, nbins=8):
    return int((theta % (2 * math.pi)) / (2 * math.pi) * nbins) % nbins

# ===========================================================================
# AGENT  (tape interpreter)
# ===========================================================================
class Agent:
    def __init__(self, kind, rng, phase_guess=None):
        self.kind = kind
        self.tape = DUMB_TAPE if kind == "dumb" else SMART_TAPE
        self.has_register = (kind == "smart")
        self.bits = tape_bits(self.tape, self.has_register)
        self.energy = INIT_ENERGY
        self.phase_guess = phase_guess if phase_guess is not None else rng.uniform(0, 2 * math.pi)
        self._match = False

    def run_tape(self, board, pos, t):
        """Execute the whole tape once (one tick). Returns (child_pos, child) or None."""
        spawn = None
        for op in self.tape:
            if op == Op.EAT:
                self._attempt_eat(board, pos, t)
            elif op == Op.EAT_IF_MATCH:
                if self._match:
                    self._attempt_eat(board, pos, t)
            elif op == Op.RECALL_PHASE:
                pass  # own-memory read ~ free
            elif op == Op.COMPARE_CLOCK:
                clock = (OMEGA * t) % (2 * math.pi)
                self._match = abs(circular_diff(clock, self.phase_guess)) < MATCH_WINDOW
            elif op == Op.READ_OUTCOME:
                # STUB: learns every tick forever. Realistic version front-loads learning then
                # coasts (Still: stop re-measuring once modeled). Your refinement.
                self.energy -= COST_READ
                self._observed_peak = -board.phase[pos]   # STUB learning signal (depends on Eq-9 rule)
            elif op == Op.UPDATE_MEM:
                self.energy -= COST_WRITE_BIT * BITS_PER_UPDATE
                target = getattr(self, "_observed_peak", self.phase_guess)
                self.phase_guess += 0.5 * circular_diff(target, self.phase_guess)  # your delta rule
            elif op == Op.PROCREATE:
                spawn = self._maybe_spawn(board, pos)
        return spawn

    def _attempt_eat(self, board, pos, t):
        self.energy -= COST_EAT
        off = board.phase[pos]
        if eat_succeeds(off, t):
            self.energy += eat_reward(off, t)

    def _maybe_spawn(self, board, pos):
        if self.energy < REPRO_THRESHOLD:
            return None
        empty = board.random_empty_neighbor(pos)
        if empty is None:
            return None
        self.energy -= self.bits * COST_PER_TAPE_BIT   # copy tape = create new ordered structure
        self.energy -= INIT_ENERGY                     # endow the child
        # STUB: child inherits the learned phase (Lamarckian) — or should it start fresh? your call.
        return (empty, Agent(self.kind, board.rng, phase_guess=self.phase_guess))

# ===========================================================================
# BOARD
# ===========================================================================
class Board:
    def __init__(self, size, predictable, rng):
        self.size, self.predictable, self.rng = size, predictable, rng
        self.agents = {}
        self.phase = {(x, y): (0.0 if predictable else rng.uniform(0, 2 * math.pi))
                      for x in range(size) for y in range(size)}

    def reshuffle_noise(self):
        # STUB: "noise" = no temporal structure to learn -> reshuffle phases each tick.
        # (predictable = phases fixed, so memory CAN learn them.)
        if not self.predictable:
            for pos in self.phase:
                self.phase[pos] = self.rng.uniform(0, 2 * math.pi)

    def random_empty_neighbor(self, pos):
        x, y = pos
        nbrs = [(x + dx, y + dy) for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))
                if 0 <= x + dx < self.size and 0 <= y + dy < self.size
                and (x + dx, y + dy) not in self.agents]
        return self.rng.choice(nbrs) if nbrs else None

# ===========================================================================
# RUN one condition
# ===========================================================================
def run(board_size, predictable, n_ticks, rng, future_lag=3):
    board = Board(board_size, predictable, rng)
    c = board_size // 2
    board.agents[(c, c)] = Agent("dumb", rng)
    sc = (min(c + 1, board_size - 1), c)
    if sc != (c, c):
        board.agents[sc] = Agent("smart", rng)

    ipred_samples = []  # (smart memory state, FUTURE pellet-up?)  [Still I_pred] — STUB measurement
    for t in range(n_ticks):
        board.reshuffle_noise()
        for pos in list(board.agents.keys()):
            agent = board.agents.get(pos)
            if agent is None:
                continue
            if agent.kind == "smart":
                fut = pellet_value(board.phase[pos], t + future_lag)
                ipred_samples.append((discretize_phase(agent.phase_guess), 1 if fut > 0.5 else 0))
            spawn = agent.run_tape(board, pos, t)
            if agent.energy <= 0:
                del board.agents[pos]
                continue
            if spawn is not None:
                child_pos, child = spawn
                if child_pos not in board.agents:
                    board.agents[child_pos] = child

    counts = Counter(a.kind for a in board.agents.values())
    return counts, mutual_information(ipred_samples)

# ===========================================================================
# 2x2 SWEEP  (the pre-registered test)
# ===========================================================================
if __name__ == "__main__":
    N_TICKS = 3000
    BIG, SMALL = 12, 4   # unconstrained vs constrained board (STUB sizes)
    print(f"{'board':>14} {'drive':>12} {'dumb':>6} {'smart':>6} {'I_pred(bits)':>14}")
    for size, label in ((BIG, "unconstrained"), (SMALL, "constrained")):
        for predictable in (True, False):
            counts, ipred = run(size, predictable, N_TICKS, random.Random(0))
            drive = "predictable" if predictable else "noise"
            print(f"{label:>14} {drive:>12} {counts.get('dumb', 0):>6} "
                  f"{counts.get('smart', 0):>6} {ipred:>14.3f}")
    print("\nZentropy predicts: smart dominates in (constrained, predictable) ONLY.")
    print("  everywhere -> free-memory/overhead bug;  nowhere -> framework wrong.")
    print("Physics is STUBBED (see === FILL FROM PAPER ===). With these arbitrary constants")
    print("expect dumb to win until you SWEEP COST_EAT up toward PELLET_PEAK — that calibration,")
    print("and the real Eq-9 rule, are yours. Sweep & report the pattern; never cherry-pick to win.")
