"""
pacman.py — Zentropy sim, SPATIAL extension (2026-05-28).

The Pac-Man, not Risk, sim. Read every design choice through that scope rule
(see THE DISCIPLINE below) or this file slides into uselessness.

PLUMBING: Claude.   PHYSICS: Brent (=== FILL FROM PAPER === banners are yours).
Papers referenced live in papers/.
Sibling to england.py (Tier-0 Arrhenius microdynamics) and still.py (kernel + selection).
Memory pointers: project-value-function-question, project-sim-england-state (2026-05-28).

================================================================================
WHY THIS FILE EXISTS — THE TRUE TEST OF ZENTROPY
================================================================================

Question (Brent, 2026-05-28):

    Is max(∆N) a true evolutionary imperative, or is it teleology?

"True evolutionary imperative" = lineage-integral ∆N is something selection
actually tracks; individual-scale predictors should be pre-registrably correlated
with it, in a way this sim can detect.

"Teleology" = post-hoc storytelling about why successful lineages succeeded; no
causal handle, no pre-registrable signature.

This sim is built to answer that question. It is the falsifiability instrument
for the project's central claim. Under project-mission: if the sim says
"teleology," that is a Win-#2 or Win-#3 outcome — load-bearing falsification of
a major zentropy claim, sharpening or killing the framework. Do not flinch from
it; do not retune the sim to rescue the thesis.

What still.py CANNOT test (and what this file is for):
  still.py measures only LOCAL efficiency (≈ Still's bound) — per-agent
  dissipation vs. drive predictability. The universe-scale integral that
  zentropy is actually about — ∆N over the forward light cone of an agent's
  existence vs. the counterfactual of its absence — requires SPACE. Without
  space there are no exports, no counterfactual region, no place for lineages
  to propagate as something other than abstract growth rates, no way to
  *count stored order* against a passive baseline. The grid is the enabling
  instrument; without it the central claim is not operationalized.

  Reminder: ∆N is STORED ORDER (bank), not entropy production (cash). See
  CONSTRAINT #1 below and feedback-bank-not-cash in memory.

================================================================================
ASYMMETRIC FALSIFIABILITY (be honest about this)
================================================================================

This iteration uses KIDS-ONLY persistence (no exports, no memes, no monuments
— see THE DISCIPLINE). That makes falsifiability asymmetric:

  - POSITIVE result (kids track lineage-integral ∆N as predicted)
      => only PARTIAL confirmation. The descendant part of the integral works;
         the export/meme/monument part is UNTESTED in this build.

  - NEGATIVE result (kids do not track it; teleology wins)
      => BROAD refutation. Lineage is the EASIEST case for the claim. If
         lineage doesn't track, exports almost certainly don't either, and the
         universe-scale integral framing is in trouble.

Fast to refute, slow to fully validate. That asymmetry is the right shape for
sim-first under the falsifiability mission.

================================================================================
DESIGN CONSTRAINTS (Brent, 2026-05-28)
================================================================================

1. GRID + PAIRED COUNTERFACTUAL RUNS.
   Two runs per condition, same RNG seed and same parameters except:
     (a) seeded-agent run: one agent placed at t=0.
     (b) empty run: no agent.

   CRITICAL — N IS BANK BALANCE, NOT CASH FLOW (Brent, 2026-05-28).
   ∆N is differential STORED ORDER / harnessed exergy held as configuration,
   NOT differential entropy production / heat dumped to bath. Life is the
   efficient harvester-that-stores, NOT the wasteful max-dissipator. If we
   measured entropy production diff we would literally favor the DUMB agent
   over the SMART one — sign-flipped physics. See foundational memories:
   feedback-bank-not-cash, project-sim-england-state ("Life ≠ max dissipation").

   The measurement is something like:

     ∆N(t) =  ( stored ordered configuration WITH agent, integrated to t )
            - ( stored ordered configuration WITHOUT agent, integrated to t )

   where "stored ordered configuration" counts agent body + descendant bodies
   + (later iterations: persistent exports) as low-entropy cells, weighted by
   their exergy content or by structural complexity. Both runs include the
   passive-baseline England-regime dissipation (see constraint #2), so the
   diff is "active lineage's stored order" - "passive baseline's stored order."

   Exact measurement (cell counting? free-energy bookkeeping? configurational
   entropy?) deferred to the at-keyboard session. Keep it bank-shaped.

   Dissipation still matters in the model — input-side constraint (need energy
   flux to maintain structure) and side-channel cost (irreversibility eats
   some of the harvest) — but it is NOT the objective function.

2. UNOCCUPIED SQUARES RUN PASSIVE NON-BIO DISSIPATION.
   "Empty" is NOT "nothing." Empty cells run England-style passive dissipative
   adaptation (Kachman 2017 regime in spirit — driven matter dissipating, no
   prediction, no replication). Otherwise "agent vs. nothing" compares apples
   to vacuum; we need apples-to-apples (active replicator vs. passive
   dissipator under the same drive). The agent's lineage-∆N is the
   DIFFERENTIAL over the passive baseline, not raw dissipation. This is also
   what makes the comparison fair to England: he says passive matter
   dissipates; we say predictive matter dissipates MORE (counted properly).

3. KIDS-ONLY PERSISTENCE (this iteration).
   The only "persistent structure" an agent can place in the world is a child.
   Defer for later iterations: fuel reserves, dropped exports, monuments,
   memes-as-objects. Lineage-only export keeps the build tractable. See
   ASYMMETRIC FALSIFIABILITY for the scope cost.

4. THE DISCIPLINE — PAC-MAN, NOT RISK.
   Pac-Man: simple agents, grid, pellets, local dissipation, kids in adjacent
   cells. Game-of-life energetics.
   Risk: territorial conquest, alliances, multi-turn strategy, complex agency,
   signaling.
   The sim MUST stay shaped like Pac-Man. Resist every drift toward Risk
   (combat, alliances, complex strategies, agents-as-players). If the sim
   starts looking interesting *for its own gameplay*, scope has slipped.
   The file is named pacman.py to keep this in the room every time it's opened.

================================================================================
OPEN PARAMETERS (decide when at the keyboard)
================================================================================

  - Grid size and topology (toroidal? bounded?)
  - Drive distribution: uniform field? sparse pellets? localized sources?
  - Passive dissipation rate vs. agent dissipation scaling
  - Child-settling rule: adjacent cell? random within radius? require empty?
  - Cost of reproduction in spatial terms (does crossing space cost energy?)
  - RNG seeding discipline for the counterfactual pair
  - How many seeded runs per condition for statistical power

These are at-the-keyboard decisions, not memory-doc decisions. Capture them in
code as they're chosen.

================================================================================
"""

# === STUB: NOT YET BUILT ===
# This module is design-only as of 2026-05-28. The next sim-focused session is
# where physics + grid mechanics get filled in. Do not import from this file;
# nothing here runs.

raise NotImplementedError(
    "pacman.py is a design stub (2026-05-28). See the module docstring for the "
    "spatial-sim brief; build to follow."
)
