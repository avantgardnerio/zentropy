# Zentropy — Simulation Design

The third pillar of the convergence paper (alongside derivation and empirical sanity check). A controlled toy world where the framework's predictions are tested empirically in a non-biological substrate.

> **TODO:** working design document. The layered build below extends Perunov-Marsland-England's 2014/2016 hopping-particle model — design choices are first-pass and should be revised as implementation reality intrudes.

## Why simulation (the methodology)

| Pillar | What it does | Field precedent |
|---|---|---|
| **Derivation** | Compose Still + Perunov-Marsland-England Eq. 8 in the constrained regime | Crooks 1999, Still 2012, England 2013, Perunov-Marsland-England 2014/2016 |
| **Simulation** | Toy world demonstrating convergence empirically | Perunov-Marsland-England 2014 (hopping particle); Tierra (Ray 1991); Avida (Lenski/Ofria/Adami 1994+) |
| **Empirical** | Real biological / civilizational data consistent with predictions | England 2013 (E. coli); Smil GDP-in-joules |

**Brent's personal rationale (foundation session, verbatim):** *"It proves 'no BS' in my understanding of the equations if I can implement them and see expected results."* Code is the honesty test. If a claim in the math can't be expressed in code, the math isn't yet understood.

**Parallel-trackable with reading.** Coding can begin *while* the keystone papers are still being read; the simulation forces honest engagement with each equation as it appears.

## Strategic choice: extend a published model, don't invent a new world

The simulation **extends Perunov-Marsland-England's hopping-particle model** rather than inventing its own substrate. This gives every layer a comparator (their published result, or the immediately-prior layer of our own simulation) and makes the eventual paper's framing trivially defensible (*"we extend Perunov-Marsland-England with [X, Y, Z] in the constrained regime"*) rather than burden-of-proving a new substrate.

**What their model actually is** (Perunov-Marsland-England 2014/2016, §"Dissipation and Drift in Time-Varying Energy Landscapes", Figs. 3–4 and Eqs. 9–12):

- A single particle hopping in a 3-state energy landscape: states $x_1, x_2, x_3$ in a row
- Arrhenius transition rates between adjacent states: $r_{i \to j} = r_{ij}^0 \exp[-\beta(B_{ij} - E_i)]$
- Time-varying drive: $E_1(t) = -\Delta E \cos(\omega t)/2$ and $B_{12}(t) = \Delta E - \Delta E \cos(\omega t)/2$; the rest constant
- High-frequency driving regime: $\omega \gg 1/\tau \gg r$
- Result (Eq. 12): $r_{2 \to 1}^\text{max} / r_{2 \to 3} = \exp[\beta \Delta E / 2]$ — preferential drift toward $x_1$

Tiny system. Three states, one particle, sinusoidal drive. **No replication, no genome, no information theory.** It's a unit test for their Eq. 8, not a biological substrate. But it's *exactly* the right substrate to build on — minimal apparatus, published numerical prediction, well-understood physics.

---

## The layered design (v0–v5)

Each layer extends a published baseline or the previous layer. Each is independently completable. Each has a defined success criterion *with a comparator*.

**Important design principle — feature-flagged Still measurement.** Still's bound applies to *any* memory-bearing system, so it's testable from v0 onward (with the particle's position serving as "memory"). Rather than waiting until v3 to introduce Still's measurement framework, we **build it as optional instrumentation that can be flag-enabled at any layer**. This is just standard integration-testing discipline applied to a research codebase:

- v0 substrate-only: reproduce England's Eq. 12
- v0 with Still flag: ALSO measure $I_\text{mem}$, $I_\text{pred}$, $\langle W_\text{diss} \rangle$; verify the bound holds
- Same code, optional add-on. Measurement is instrumentation, not different physics.

**Why this is better than "introduce Still at v3":** every layer becomes a double sanity check (substrate + Still). The measurement code gets reps and matures before it's load-bearing. When v3 fails, the bug is localized to the new decoupled-memory machinery — *not* to the measurement code, which is by then well-debugged.

**What changes per layer:** the *substrate* progresses (single particle → populations → competition → explicit memory → mutation → phase transitions). The *Still measurement* runs alongside throughout, increasing in load-bearingness as memory becomes a richer object. v3 is where memory becomes *decoupled* from particle position; that's where Still's bound becomes the *load-bearing claim* rather than a sanity check.

### v0 — Reproduce England's Fig 3 / Eq 12

**Goal:** substrate sanity check. Implement Perunov-Marsland-England's exact 3-state hopping model. Verify the simulation produces their published numerical result.

**Apparatus:**
- 3 states $x_1, x_2, x_3$
- Stochastic transitions via Arrhenius rates
- Time-varying $E_1(t)$ and $B_{12}(t)$ as specified
- All other energies / barriers constant
- High-frequency driving

**Success criterion:** measured ratio $r_{2 \to 1}^\text{max} / r_{2 \to 3} \approx \exp[\beta \Delta E / 2]$ (the published result).

**Failure interpretation:** if we cannot reproduce a published numerical result with a 3-state model, the simulation infrastructure is broken. Fix it before any layer above.

**Complexity:** ~200 lines of Python. **One evening.** This is genuinely the smallest possible useful starting point.

**Algorithm (Gillespie stochastic simulation, Gillespie 1977):**

```python
import numpy as np

# ─────────────────────────────────────────────────────────────────
# Parameters — Greek / math symbols → Python variable names
# (See notation.md for symbol pronunciations and meanings.)
# ─────────────────────────────────────────────────────────────────
beta    = 1.0       # β   — inverse temperature, β = 1/(k_B · T)
delta_E = 5.0       # ΔE  — base barrier height (Δ = capital delta, "DELT-ah")
omega   = 100.0     # ω   — drive frequency (high-frequency: ω ≫ 1/τ ≫ r)
r0      = 1.0       # r⁰  — base rate constant (Arrhenius prefactor)

# Recommended regime: β · ΔE ≈ 3–10
# (dimensionless; small enough for fast convergence, large enough for clean drift)

rng = np.random.default_rng(seed=42)   # ALWAYS seed the PRNG

# ─────────────────────────────────────────────────────────────────
# State labels: `i ∈ {0, 1, 2}` represents x_1, x_2, x_3
# No spatial coordinates — pure state graph: x_1 ── x_2 ── x_3
# (x_1 and x_3 are NOT directly connected; you must go through x_2)
# ─────────────────────────────────────────────────────────────────

def energies_and_barriers(t):
    """Time-varying drive (Perunov-Marsland-England 2014/2016):
         E_1(t) = −ΔE · cos(ω·t) / 2     ← oscillating
         B_12(t) = ΔE − ΔE · cos(ω·t) / 2 ← oscillating
         E_2 = E_3 = 0                    ← constant
         B_23 = ΔE                        ← constant
       Returns:
         E[3] — energies of the three states     (E_1, E_2, E_3)
         B[2] — barriers between adjacent states (B_12, B_23)
    """
    E = np.array([-delta_E * np.cos(omega*t) / 2, 0.0, 0.0])
    B = np.array([delta_E - delta_E * np.cos(omega*t) / 2, delta_E])
    return E, B

def arrhenius_rates(state, t):
    """Hop rates from current state using the Arrhenius law:
         r_{i→j} = r⁰ · exp[ −β · (B_{ij} − E_i) ]

       The exponent (−β · activation_energy) penalizes hops that have
       to surmount a tall barrier relative to thermal energy k_B·T.
       Lower barrier ⟹ faster hop.
    """
    E, B = energies_and_barriers(t)
    rates, targets = [], []
    if state > 0:                          # can hop left  (i → i−1)
        rates.append(r0 * np.exp(-beta * (B[state-1] - E[state])))
        targets.append(state - 1)
    if state < 2:                          # can hop right (i → i+1)
        rates.append(r0 * np.exp(-beta * (B[state]   - E[state])))
        targets.append(state + 1)
    return np.array(rates), targets

def run_trajectory(initial_state, t_max):
    """Single Gillespie trajectory (Gillespie 1977).
       Tracks one particle hopping stochastically through the 3-state graph
       under the time-varying drive.
    """
    state, t = initial_state, 0.0
    transition_log = []                    # list of (t, old_state, new_state)
    while t < t_max:
        rates, targets = arrhenius_rates(state, t)
        R = rates.sum()                    # R — total outgoing rate from current state
        if R == 0:
            break
        # Wait time τ ~ Exponential(R)
        # Inverse-CDF sampling: τ = −ln(u) / R, where u ~ Uniform(0, 1)
        tau = -np.log(rng.random()) / R    # τ — time to next event
        t += tau
        if t >= t_max:
            break
        # Which transition fires? Choose target weighted by rate / total
        choice = rng.choice(len(rates), p=rates / R)
        old_state, state = state, targets[choice]
        transition_log.append((t, old_state, state))
    return transition_log

# ─────────────────────────────────────────────────────────────────
# Verifying Eq. 12 (the published result we need to reproduce):
#   1. Run many trajectories starting at x_2 (state = 1)
#   2. Bin transitions by drive phase  φ = (ω · t)  mod  2π
#   3. Measure peak r_{2→1}(t)  vs  constant r_{2→3}
#   4. Verify   r_{2→1}^max / r_{2→3}  ≈  exp[ β · ΔE / 2 ]
# ─────────────────────────────────────────────────────────────────
```

**Math-notation shorthand used in the snippet:**

| Symbol | Read as | Meaning |
|---|---|---|
| `≫` | "much greater than" | regime shorthand — "many orders of magnitude bigger than." `ω ≫ 1/τ` ≈ "the drive oscillates many orders of magnitude faster than relaxation." |
| `≪` | "much less than" | complement of `≫` |
| `∈` | "is an element of" / "in" | set membership. `i ∈ {0, 1, 2}` ≈ "i is one of 0, 1, or 2." Complement `∉` = "is not an element of." |
| `Δ` | "DELT-ah" / "change in" | difference operator (capital delta). `ΔE` ≈ "an energy difference" — here used as a fixed barrier magnitude rather than a literal change, which is mild abuse of notation but standard. |

**Symbol → variable cheat sheet** for the snippet above (with source citation for where each is defined / used):

| Symbol | Variable | Pronunciation | Meaning | Source |
|---|---|---|---|---|
| β | `beta` | "BAY-tah" | inverse temperature, $1/(k_B T)$ | Standard stat mech (Boltzmann, ~1877); used throughout Still 2012, England 2013, Perunov-Marsland-England 2014/2016 |
| ΔE | `delta_E` | "DELT-ah E" | barrier-height parameter | Perunov-Marsland-England 2014/2016, Fig. 3 setup, §"Dissipation and Drift…" |
| ω | `omega` | "oh-MEG-ah" | drive angular frequency | Perunov-Marsland-England 2014/2016, Eq. 10 |
| τ | `tau` | "tow" (rhymes with cow) | wait time between events; also characteristic system timescale | Gillespie 1977 for the wait-time use; Perunov-Marsland-England 2014/2016 for the system-timescale use |
| φ | (derived as `omega * t mod 2π`) | "FYE" or "FEE" | drive phase | standard physics convention |
| r⁰ | `r0` | "r-zero" | Arrhenius rate prefactor | Arrhenius 1889 originally; Perunov-Marsland-England 2014/2016 Eq. 9 in this context |
| R | `R` | just "R" | total outgoing rate (sum of all $r_{i→j}$ from current state) | Gillespie 1977 |
| $E_i$ | `E[i]` | "E sub i" | energy of state $i$ | Perunov-Marsland-England 2014/2016, Fig. 3 |
| $B_{ij}$ | `B[i]` | "B sub i j" | barrier between states $i$ and $j$ | Perunov-Marsland-England 2014/2016, Fig. 3 |

The inner Gillespie loop (rates → wait time → choice → execute) is ~10 lines; everything else is configuration and instrumentation. Reproducing Eq. 12 is fundamentally these 10 lines wrapped in a measurement harness.

### v1 — Population of N independent particles

**Goal:** confirm the substrate scales. No biology yet; just verify infrastructure.

**Apparatus:** same dynamics as v0, but $N$ particles, no interaction between them.

**Success criterion:** aggregate population behavior matches $N \times$ v0. Computational efficiency reasonable.

**Failure interpretation:** if aggregate behavior diverges from $N \times$ v0, there's a state-sharing bug — particles are accidentally interacting through some shared variable.

**Complexity:** ~half a day after v0.

### v2 — Resource competition (the constrained regime)

**Goal:** introduce the *constrained regime* that the framework requires. Particles share a finite energy pool; consumption by one affects what's available to others.

**Apparatus:**
- Each state $x_i$ has a finite energy capacity $C_i$ that depletes when particles dwell there or transition through it
- Energy regenerates at rate $\rho$ per state per timestep (slower than aggregate consumption)
- Particles cannot transition into a state that has $0$ available energy
- Particle "death" mechanic: if a particle cannot transition for $\tau_\text{death}$ steps, it's removed

**Success criterion:** in the constrained regime, particle population stabilizes below the unconstrained-regime population. Competition for x₁ (the favored drift target) is observable.

**Failure interpretation:** if competition dynamics don't emerge, the constraint is mis-implemented. Likely the energy regeneration rate is set wrong.

**Complexity:** ~1 week after v1. The bookkeeping for shared resources is the main work.

### v3 — Predictive memory + Still's bound check (the convergence claim)

**Goal:** **the central empirical test of the convergence proof.** Add memory state to particles; measure $I_\text{mem}$ and $I_\text{pred}$; verify Still's bound holds; verify selection-style pressure on $I_\text{nonpred}$.

**Apparatus additions:**
- Each particle gets an internal memory register (start with a few bits)
- Hopping rates are modulated by memory: $r_{i \to j}(s_t, x_t)$ where $s_t$ is the memory state
- Some particles get "lucky" memory configurations that correlate with the drive phase; they harvest more energy per cycle
- **Measurement instrumentation:**
  - $I_\text{mem}(s_t, x_{t-\Delta})$ — mutual information between memory and recent past drive
  - $I_\text{pred}(s_t, x_{t+\Delta})$ — mutual information between memory and future drive
  - $\langle W_\text{diss} \rangle$ per cycle for each particle

**Success criteria:**
- Still's bound holds: $\beta \langle W_\text{diss} \rangle \ge I_\text{mem} - I_\text{pred}$ across all particles, all timesteps
- Surviving lineages (in the constrained regime) have lower $I_\text{nonpred}$ than dying ones
- The $(I_\text{mem}, I_\text{pred})$ plane trajectory matches the compression-view prediction

**Failure interpretation:**
- Bound appears violated → suspect (a) MI estimation bias, (b) hidden information flow not captured in measurement, (c) the bound has a domain restriction the proof missed
- Bound holds but selection-on-I_nonpred not observed → constraint not tight enough; tune

**Complexity:** 1–2 months after v2. Mutual-information estimation is the main subtle piece (see Measurement Instrumentation below).

### v4 — Mutation + replication

**Goal:** show that *predictive memory structure emerges from random mutation under selection* — the Darwinian engine of the convergence claim.

**Apparatus additions:**
- Particles can replicate (cost: energy; result: a new particle in a neighbor state with mutated memory configuration)
- Mutation: small bit-flip rate per replication
- Initial population: random memory configurations
- No predefined "good" strategies

**Success criteria:**
- Over generations, average $I_\text{pred}$ rises while $I_\text{nonpred}$ falls
- Lineage diversity collapses around predictive memory configurations
- Forcing a lineage to higher $I_\text{nonpred}$ (artificial mutation) decreases fitness

**Failure interpretation:** if predictive structure does NOT emerge from random mutation, suspect (a) memory state too small to express useful predictions, (b) mutation rate mis-tuned, (c) selection pressure too weak. **If none of those:** consider whether the simpler particle-with-memory substrate is too restrictive and an Avida-style bulletproof VM is needed.

**Complexity:** 1–2 months after v3.

### v5 — Phase transition (optional extension)

**Goal:** demonstrate the phase-transition cycle and the "fewer copies of more complex cells" signature.

**Apparatus additions:**
- Introduce a *new* energy modality partway through the run (e.g., at generation $10^4$, add a second oscillating energy with different frequency)
- Larger memory register accessible only via specific mutation
- The new modality is exploitable only by particles with the larger register

**Success criteria:**
- Some lineage discovers the larger register, exploits the new modality
- That lineage has higher per-particle capability, lower per-niche count, dramatically higher cumulative $\int N(t)\,dt$
- Pre- and post-innovation eras show distinct $(I_\text{mem}, I_\text{pred})$ regimes — the cycle structure visible

**Complexity:** ~1 month after v4. *Nice-to-have*; v0–v4 already constitute a publishable Pillar 2.

---

## Bulletproof-VM design notes (only if v4 is insufficient)

The hopping-particle + memory-register design above may be too restrictive — there's a possibility that "memory configurations" don't have enough expressive richness to capture the strategies the framework predicts. If v4 fails for that reason (not because the framework is wrong), the substrate should escalate to a full Avida-style bulletproof virtual machine.

**Prior art (read before designing your own):**

- **Tierra** (Tom Ray, 1991): pioneered bulletproof-VM-with-mutation. Templates for self-replication addressing.
- **Avida** (Lenski/Ofria/Adami 1994+): well-documented, widely used in published research. Avida-ED is the educational version. Particularly: Adami's group has published on measuring information content in Avida lineages — directly relevant.

**Constraint: total instruction set.** Every opcode, regardless of program state, completes in one timestep with defined behavior. No exceptions, no halts, no crashes. This is what makes mutation safe.

**Minimum useful instruction set (~10 opcodes):** `NOP`, `MOVE_N/S/E/W` (4 directional), `SENSE`, `EAT`, `LOAD_MEM`, `STORE_MEM`, `COMPARE`, `JMP_REL` (saturated), `REPLICATE`.

**Genome representation:** fixed-length array, *circular* execution (no halt), bit-flip mutation at rate ~1/genome_length.

**What to avoid:** halts (always-running), variable-length genomes (until much later), non-total operations (use saturating arithmetic, wrap-around indexing).

**Recommendation:** if reaching v5 territory, adopt Avida's instruction set directly rather than designing your own. Saves rediscovery work.

---

## Measurement instrumentation

### Mutual information estimation

$I_\text{mem}$ and $I_\text{pred}$ are mutual informations. **Estimation is not trivial** — naive plug-in estimators have severe bias for small samples and high-dimensional state.

Use a known-good estimator:
- **Kraskov-Stögbauer-Grassberger (KSG)** for continuous variables
- **Miller-Madow** or **NSB** bias-corrected plug-in for discrete
- Python packages: `scikit-learn.feature_selection.mutual_info_regression`; `infotopo`; `pyitlib`

### Sampling strategy

- Collect (memory_state, drive_state) pairs per particle per timestep
- $I_\text{mem}$: pair memory at $t$ with drive at $t - \Delta$ (recent past)
- $I_\text{pred}$: pair memory at $t$ with drive at $t + \Delta$ (future)
- Pick $\Delta$ to match the drive's characteristic timescale (one period of oscillation, roughly)
- Estimate over per-lineage samples (group by ancestry tree)

### What to plot

- Population trajectories over time
- $(I_\text{mem}, I_\text{pred})$ phase space, color-coded by generation — **the most important plot for the paper**
- Still's bound scatter: measured $\beta \langle W_\text{diss} \rangle$ vs $(I_\text{mem} - I_\text{pred})$ per cycle; verify the inequality
- At innovation events (v5): per-niche population count vs per-particle complexity — the "fewer copies of more complex cells" signature

---

## Language and tooling

### Primary recommendation: Python (NumPy + matplotlib) for v0–v3

**Rationale:**
- Numerical / statistical / scientific ecosystem is far ahead of any alternative — `numpy`, `scipy`, `scikit-learn`, off-the-shelf MI estimators (`KSG`, `pyitlib`)
- Academic collaborators will expect Python or MATLAB; Python is the lingua franca of computational physics now
- v0–v3 performance needs are well within Python's range — the Gillespie loop above runs at 10⁵+ events/sec in pure Python, faster with vectorization
- Seeded PRNG: `numpy.random.default_rng(seed)`. **Always seed; record the seed in every results file; never run un-seeded.**

### The visualization tradeoff — Brent's instinct is correct that this matters

Python's visualization story is *good-enough* rather than *excellent*. Worth knowing the actual tradeoffs:

| Stack | Visualization | Scientific ecosystem | Iteration speed | Right for |
|---|---|---|---|---|
| **Python** (NumPy + matplotlib + pygame/Pyglet) | Static plots: publication-grade. Live grid animation: works via pygame/Pyglet, but isn't slick. | **Best in class** | Fastest — REPL, Jupyter, no compile | **v0–v3, possibly all of v0–v5** |
| **JavaScript** (p5.js, d3.js, three.js) | **Excellent** — browser-native, interactive, shareable as URLs | Weak (no NumPy equivalent matures) | Fast | **Shareable demos / talks** (built on top of saved data) |
| **Rust** (bevy, nannou, egui) | Excellent + extremely fast | Growing but immature | Slow (compile times, borrow checker) | **Only if v4+ runtime becomes painful** |

### The hybrid path worth knowing

For *demonstrations* (a collaborator opens a URL and watches the cycle play out), JavaScript visualization is superior. But the computation kernel doesn't need to be JS:

1. **Simulation runs in Python** (or Rust later) → outputs trajectory data as JSON / CSV
2. **Visualization renders in JavaScript** from the saved data → static HTML + JS for shareable demos

This decouples *what's hard* (the math, the measurement) from *what's shareable* (the visualization). Not needed for v0; useful for demonstrating results once they exist.

### Seeded PRNG is non-negotiable

Every stochastic experiment must be reproducible. Brent's instinct on this is correct:

- Every script seeds its PRNG explicitly at the top
- Every results file records the seed used
- Never run un-seeded code, even for exploratory runs — write the seed to the filename or to a metadata header

Without this discipline, debugging a stochastic simulation is impossible: different runs produce different bugs and you can't isolate the cause.

### When to consider porting to Rust

- v3 measurement is slow (computing MI estimators on millions of samples)
- v4+ has many particles with active VM-style genomes; per-instruction overhead dominates
- You want to share a binary or compiled web demo

**Don't pre-optimize.** Python is fine until it isn't, and "isn't" usually means runtime > 1 day for a single experiment. Most v0–v3 work will run in minutes.

### Suggested stack summary

- **Python 3** with `numpy`, `scipy`, `matplotlib` for v0–v3
- `pygame` or `pyglet` if/when live grid animation matters (probably v2+)
- `pyitlib` or `scikit-learn` for MI estimation
- `Jupyter notebook` for exploratory analysis; convert to scripts when stable
- **Optional later:** Rust port (v4+) and/or JS visualization layer (for sharing)

### Repo structure (suggested)

```
zentropy/
  sim/
    v0_england_reproduction.py   # one evening
    v1_population.py             # ~half day
    v2_constrained.py            # ~1 week
    v3_memory_stills_bound.py    # 1-2 months
    v4_mutation_replication.py   # 1-2 months
    v5_phase_transition.py       # optional
    common/
      hopping.py                 # 3-state Arrhenius dynamics
      drive.py                   # time-varying energy field
      measure.py                 # MI estimators
      memory.py                  # particle memory state
    results/
      *.png, *.csv               # generated outputs
```

---

## Falsification criteria (per layer)

Each layer's outcome tells us something specific about the framework. Failures are *information*, not setbacks.

Each row split into substrate validation (always run) and Still validation (flag-enabled, double sanity-check):

| Layer | Substrate test | Still-bound test (flag-enabled at every layer) |
|---|---|---|
| **v0** | Reproduce England Eq. 12 ratio | Still's bound holds for `position-as-memory` |
| **v1** | Aggregate population behavior = N × v0 | Bound holds per-particle and on aggregate |
| **v2** | Competition dynamics observable in constrained regime | Bound holds; bites harder as nonpredictive memory accumulates |
| **v3** | Explicit decoupled memory register implemented correctly | **Still's bound becomes load-bearing** — holds for decoupled memory state; selection-style pressure on $I_\text{nonpred}$ observable |
| **v4** | Mutation/replication produces evolutionary dynamics | $(I_\text{mem}, I_\text{pred})$ trajectory matches the compression-view prediction across generations |
| **v5** | Innovation events propagate and exploit new gradient | Phase-transition signature visible in $(I_\text{mem}, I_\text{pred})$ phase space |

**Interpretation of failures:**

| Where it fails | Almost certainly… |
|---|---|
| Substrate test at v0–v2 | Infrastructure bug; framework not yet tested |
| Still-bound test at v0–v2 | MI measurement code bug; substrate is fine |
| Substrate test at v3 | Decoupled-memory machinery bug |
| Still-bound test at v3 | **Either** the bound has a domain restriction we missed, **or** hidden information flow not captured in measurement — this is where the framework is actually tested |
| Substrate test at v4 | Substrate insufficiently expressive — consider Avida-style VM escalation |
| Still-bound test at v4 | Selection isn't operating on $I_\text{nonpred}$ as claimed — framework question |
| Either test at v5 | Phase-transition mechanism not what we think |

**v0–v2 are infrastructure validation (with Still as an early sanity check).** **v3 is where Still's bound becomes load-bearing.** **v4–v5 produce novel results.**

---

## Honest expected outcomes

**v0–v2 will almost certainly succeed.** They reproduce or extend published, validated work. If they fail, it's a coding bug.

**v3 is the load-bearing experiment.** Still's bound is derived for general memory-bearing systems; there's no substrate-specific reason it shouldn't hold in our simulated particles. *Verifying it empirically in a fully-controlled system you built* is itself the contribution.

**v4 is where surprises are possible.** Whether predictive memory emerges from random mutation in this specific substrate is genuinely open. If yes — convergence proof has direct empirical demonstration. If no — interesting open question about expressivity / substrate.

**v5 produces the most novel result if it lands** — phase-transition cycle from random innovation in a non-biological substrate.

---

## Start here

**Begin with v0 this weekend.** Reproducing Eq. 12 in a hopping-particle simulation is bounded, useful, and tells us whether the simulation infrastructure is sound. ~200 lines of Python, one evening of work.

**Serial gating point: between v0 and v3.** Layers v1–v2 are infrastructure scaling and should follow naturally from v0 working. v3 is the real research step — don't start it until v0–v2 are clean.

**Parallel-trackable with reading.** v0–v2 can be coded while reading Still and the England papers. v3+ benefits from having finished the reading.
