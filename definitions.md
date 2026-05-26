# Zentropy — Working Definitions

## Thesis statements

**General zentropy** — the compass, the long-term claim, *not the subject of this document but the frame around it*:

> **The universe wants to make copies of itself.**

**Special zentropy** — the publishable artifact, *the subject of this document*:

> **Persisting boundaries with predictive memory (*i.e.*, life) are the configurations physics tends to produce wherever non-living dissipators leave exergy unconsumed. The same dynamic recurses (*i.e.*, evolution): more predictive memory emerges wherever less predictive memory saturates.**

*Brent's compressed theses, foundation session. Both are lossy like `E = mc²` is lossy — every word unpacks into a citation in the eventual paper.*

Unpacking **Special** word by word:
- *"persisting boundaries"* → configurations selected under dissipative adaptation (England 2013 + Perunov-Marsland-England 2014/2016); "persisting" carries England's selection — driven matter reorganizes toward configurations that absorb work, and the ones we observe are the ones that survived doing so
- *"predictive memory"* → predictive information about future-relevant variables (Still 2012, $I_\text{pred}$); not just any correlation with the past, but memory that reduces uncertainty about the future
- *"(i.e., life)"* → the parenthetical is doing definitional work, not just labeling — the thesis names "life" thermodynamically rather than presupposing a folk definition. Full operational definition in the [Life](#life--operational-definition) section
- *"physics tends to produce"* → stochastic, not deterministic; configurations are statistically *favored* under driving, not guaranteed. Earth-life is n=1; observation alone does not establish necessity, and "tends to" matches the actual physics
- *"non-living dissipators leave exergy unconsumed"* → the emergence condition; life only appears where simpler dissipators leave exergy unconsumed (H₂/O₂ combustion consumes the gradient in milliseconds → no room for life; sea vent's abiotic chemistry only partially exploits the gradient → room remains, life emerges). Substrate-agnostic: "non-living" means anything not satisfying the two life criteria, whether prebiotic chemistry, weather, or pre-AI silicon
- *"the same dynamic recurses (i.e., evolution)"* → the framework is scale-invariant: the emergence condition that produces life from non-life also produces more complex life from simpler life. Each phase transition (aerobic, multicellularity, brains, language, AI) is the same dynamic at a different rung. Evolution under zentropy is not a separate physics — it's the same Still + England composition operating at multiple complexity scales. See [the full phase-transition ladder](#the-full-phase-transition-ladder-implicit-story-zentropy-will-tell-explicitly) below
- *"more predictive memory emerges wherever less predictive memory saturates"* → the recursion's content: configurations are orderable by predictive memory, and each transition is a memory upgrade. Apparent *"coupling"* upgrades (e.g., aerobic respiration's ~16× metabolic gain) are not separate from this — the DNA expansion that enables O₂ handling (cytochrome c oxidase, electron transport chain, ROS-handling machinery) *is* encoded predictive information about a richer environmental variable. Coupling upgrades ride on encoded-machinery upgrades

Unpacking **General** non-teleologically:
- *"wants"* → selection dynamics in driven non-equilibrium systems statistically favor configurations that persist
- *"make copies"* → self-replicating dissipative structures persist; non-self-replicating ones dissipate and disappear
- *"of itself"* → the surviving patterns are made of the same physics as everything else; "life" isn't a separate category, it's the dominant persistent expression of universal gradient-dissipation organization

**Composition:** Special explains *within-replicator dynamics* (why some replicators outcompete others, given that they exist). General explains *why replicators exist at all* (the universe's organization selects for copying-things). Together: full framework at two scales, in two sentences.

See [Open Problems](#theoretical-claims-asserted-not-yet-derived) for the convergence-proof structure that unpacks Special into actual derivable claims.

---

This file captures the formal definitions zentropy is converging on. Living document — will sharpen as the reading queue closes and each quantity is pinned down rigorously.

**Scope** (locked, see `memory/feedback-science-only.md`): only physical and information-theoretic quantities as primitives — joules, bits, kelvins, time, distance, probability. Concepts like *agency, intention, consciousness, purpose, meaning, ethics* may not be assumed; they may, however, be *derived* from the dynamics. Reducing previously-metaphysical claims to physics is the long-term consilience goal — but only via derivation, never by primitive assumption.

---

## The core quantity: N (a.k.a. *zenergy*)

```
N(R, t) := inbound exergy flux across the boundary of R at time t
         = rate at which R removes exergy from its environment
         within R's forward light cone
```

Units: J/s (instantaneous rate); J for the cumulative $\int N(R, t)\,dt$ over a chosen period. R is the chosen integration boundary (cell, organism, lineage, civilization, AI session — observer-supplied per [Lineage scope is a modeling input](#lineage-scope-is-a-modeling-input)).

**Project shorthand:** *zenergy* (Brent's coinage, foundation session). Pairs with zentropy: zentropy is the framework; zenergy is its core quantity.

**Paper term:** *coupled exergy* (or *accessible exergy* if the audience prefers) — descriptive, technically defensible. First-mention convention: *"coupled exergy (hereafter N, or zenergy informally)."*

### Realized, not potential — the critical clarification

The point that took refinement to land:

- **Exergy** (textbook) = total maximum work extractable from a system + reference environment, given physics. Observer-independent. A property of the universe.
- **Potential coupled exergy** = exergy that *could be* harnessed by the agent given current capabilities. Includes oil discovered but not extracted, photons reaching a Dyson sphere that exists but sits idle.
- **Zenergy / N** (this project's quantity) = exergy *presently being harnessed*. Realized, not potential. **Active flows, not theoretical reach.**

**Why realized, not potential.** It makes `∆N > 0` specifically mean *"the agent has started harnessing what it wasn't before."* This matches the phase-change intuition exactly:

| Phase transition | Why ∆N > 0 (realized) |
|---|---|
| Photosynthesis evolves | Photons go from unharnessed → harnessed by living lineage |
| Aerobic respiration | O₂ as electron acceptor goes from unused → used (~16× metabolic gain) |
| Multicellularity | New spatial / specialization flows come online |
| Brains (predictive coupling) | Information-as-resource starts being processed |
| Agriculture | Solar-via-grain flows expand dramatically |
| Industrial fossil fuels | ~10⁸ years of stored sunlight starts being burned per decade |
| Hypothetical Dyson sphere | Full stellar output starts being processed (Carnot bound) |

Capability and actual harnessing are different. A Dyson sphere that *exists but sits idle* doesn't increase N. One that *processes stellar output* does.

### Implications worth knowing

- N depends on **active activity**, not just existence or capability. A sleeping organism has lower N than an awake one. An idle datacenter has lower N than an active one. A civilization in stasis has ∆N = 0 even with technological capacity for more.
- This is *fine* — it sharpens the "∆N > 0 ⇔ life-like activity" claim, since active life HAS active flows.
- Capability expansion *enables* future ∆N, but doesn't itself constitute ∆N. The +∆N event is the actual deployment / new harnessing activity.

### The N partition — what happens to harnessed exergy

By energy conservation at R's boundary, the inbound exergy flux $N$ partitions into three terms:

$$N(R, t) \;=\; D_\text{boundary}(R, t) \;+\; \dot{E}_\text{stored}(R, t) \;+\; D_\text{downstream}(R, t)$$

- $D_\text{boundary}$: rate at which R dissipates exergy as heat *at its own boundary* (the second-law tax of maintaining structure)
- $\dot{E}_\text{stored}$: rate at which R accumulates exergy in its structure (biomass, ATP, capital, encoded predictive structure)
- $D_\text{downstream}$: rate at which R routes exergy to other systems (electricity exported, ATP shared with neighbor cells, manufactured goods, computational outputs)

**What R does with the harnessed exergy is downstream of N itself.** The four agent states map cleanly:

| Agent state | Description | Dominant partition term |
|---|---|---|
| Steady (eat = poop) | Maintenance | $N \approx D_\text{boundary}$ |
| Routing (export ATP, electricity, products) | Productive contributor | $N \approx D_\text{downstream}$ |
| Growing (biomass, capital, latent predictive structure) | Accumulating | $N \approx \dot{E}_\text{stored}$ |
| Dying (consuming reserves) | Net consumer | $H \approx 0$, $\dot{E}_\text{stored} < 0$ |

A "parasite" case ($R$ takes exergy from a neighbor agent rather than from the abiotic environment) is the same partition at the *agent* scope but $N \approx 0$ at the *system* scope (no new exergy entered the system; rearrangement only). Both scopes are physically meaningful — picking the scope is a modeling choice, not a derivation.

### Harnessed vs. dissipated — reconciling two framings

The doc's earlier sketches sometimes used *"exergy harnessed"* and sometimes *"dissipation rate"* interchangeably. The N partition resolves them:

- **Harnessed** = $N$ (inbound flux, primary definition)
- **Dissipated at boundary** = $D_\text{boundary}$ (one term in the partition)
- **Total dissipation eventually caused by R** = $D_\text{boundary} + D_\text{downstream}$ + (eventual decay of stored) — over R's full lifetime this equals $\int N\,dt$, since whatever R harnessed eventually dissipates somewhere

At steady state and lifetime-integrated, harnessed and dissipated converge ($\int N\,dt = \int D_\text{total}\,dt$). They differ *instantaneously* when R is growing ($\dot{E}_\text{stored} > 0$) or dying ($\dot{E}_\text{stored} < 0$). Harnessed is the primary measurement because it captures the *gradient-removal* event regardless of fate; dissipation is a downstream sub-case.

This matters for the emergence condition in the thesis. *"Non-living dissipators leave exergy unconsumed"* — *consumed* here means *removed from the available pool*, i.e., $H$. A non-life configuration that harnesses and stores still counts as having consumed exergy (it's gone from the pool). Harnessed is the right measure.

---

## Why a reference environment is required

Exergy quantifies a *gradient*. Without a baseline, "available work" is meaningless — energy at uniform temperature, pressure, and composition has zero exergy regardless of quantity. No gradient, no engine. This is the second law in a different vocabulary.

The reference environment is not an external imposition; it is the thing that makes the gradient calculation possible. *"I have $5"* is meaningless without *"compared to having $0."* Thermodynamic gradients require a baseline.

For any specific system, the reference environment is everything *outside* the system's effective boundary. Once boundary is chosen, exergy is well-defined.

**Reference choices for cases we care about:**

| System | Reference environment |
|---|---|
| Earth-life | Earth surface conditions (~300 K, 1 atm, atmospheric composition) |
| Dyson civilization | Local stellar + interstellar (~3 K CMB cold sink) |
| AI in a datacenter | Datacenter power feed and waste-heat sinks (open question for the paper) |
| Closed thermodynamic universe | Maximum-entropy reference; remaining gradient = remaining usable exergy |

### What about the universe's "edge"?

The relevant theoretical boundary for any agent is its **future light cone** — the volume it could causally influence, ever. Cosmologically, the universe may or may not have a spatial edge (open question, possibly nonexistent); for exergy bookkeeping it does not matter.

- The **cosmic microwave background** (~2.725 K) provides a real cold sink that exists everywhere inside any agent's light cone. *There is always something to differ with* — the CMB cold floor permeates the observable universe.
- For Sol: gradient between $T_\odot \approx 5800$ K (surface) and $T_\text{CMB} \approx 2.725$ K (cosmic sink). Carnot bound on extractable exergy: $(T_\odot - T_\text{CMB})/T_\odot \approx 99.95\%$ of radiated power.
- **Beyond the light cone is causally disconnected by definition.** Exergy with respect to beyond-light-cone regions is *undefined*, not zero.

### Effective vs theoretical boundary

The light cone is the *theoretical maximum* — the limit of what an agent could causally affect at the speed of light. In practice, almost no agent saturates it. A new cheeseburger topping propagates through human cultural networks (years, planet-scale), not through interstellar space at $c$. A meaningful N calculation uses the **effective causal sphere** — the actual propagation reach of the agent's specific actions given the mechanisms involved.

| Agent scale | Effective boundary |
|---|---|
| Individual action | social network, lifetime, ~planetary at most via published work |
| Civilizational action (present-day humanity) | planetary / near-orbit / centuries (Earth + LEO + probes) |
| Hypothetical mature spacefaring civilization | interstellar; approaches light cone asymptotically over cosmic time |
| Self-replicating von Neumann probe | genuinely light-cone-bounded over astronomical timescales |

**Both are valid; choice depends on agent scale and time horizon.** Light cone gives the asymptotic upper bound that makes N well-defined in principle; effective causal sphere is the operational quantity you actually compute against. For papers concerned with present-day humans, civilizations, or AI, the effective sphere is much smaller than the light cone and is the relevant scale.

---

## ∆N — three distinct quantities (preliminary; to be tightened against keystone-paper apparatus)

> **TODO:** the framing below is intuited from first principles in conversation, not yet grounded in citations. Replace with the precise vocabulary from **England 2013** (individual-cell dynamics, dissipative adaptation) and **Still 2012** (memory-bearing predictive systems) once read. The keystone papers may compress these three quantities into one under stated conditions, or force a different decomposition entirely. Mark and revisit.

When the framework says "∆N," it actually refers to three distinct quantities. The earlier slogan conflated them; the cleaner version separates them:

| Symbol | What it is | Units |
|---|---|---|
| $N(t)$ | instantaneous harnessing *rate* at time $t$ | power (J/s) |
| $\int_a^b N(t)\,dt$ | cumulative throughput over an interval | energy (J) |
| $dN/dt$ | rate of change of harnessing rate — *does the coupling surface expand?* | J/s² |

### Four canonical scenarios

- **Cell exists vs counterfactual void, at moment $t$:** $N(t) > 0$. The cell is actively harnessing; the void isn't. Individual-level signature of being alive.
- **Coming into existence:** discrete event — $N$ jumps from $0$ to $N_\text{cell}$. During the formation interval $dN/dt > 0$; after formation, $dN/dt \approx 0$ until something else changes.
- **Eating but not reproducing:** $N(t) > 0$ (alive at every moment), $dN/dt \approx 0$ (steady state), $\int N\,dt > 0$ (throughput accumulating). Alive at the individual level; not expanding the lineage.
- **Lineage dies without descendants:** integrated $\Delta N$ over the lineage's full existence $\approx 0$ (emergence contribution exactly cancels death contribution). Not lineage-persisting.

### Updated headline

The earlier slogan *"Life ≡ ∆N ≥ 0"* was conflating individual-level and lineage-level signatures. The corrected version distinguishes:

- **Individual-level "alive at moment $t$":** $N(t) > 0$. Active harnessing.
- **Lineage-level "persists over time":** $dN/dt \ge 0$ averaged over the lineage's existence. At minimum replaces itself; ideally expands.
- **Phase-transition event:** $dN/dt > 0$ spike when new capability or coupling comes online (first replicator emergence, aerobic gene unlock, fire, brains, language, industrial technology, AI).

**Both readings are physically meaningful; neither subsumes the other.** A single cell that eats but doesn't reproduce is *alive* (individual-level positive throughput) but not *lineage-persisting* (no expansion). The framework needs both, marked explicitly.

Precise integration measure (per-agent vs per-lineage vs per-light-cone, instantaneous vs cumulative, counterfactual baseline) still deferred until the keystone-paper apparatus pins down the right vocabulary.

### Lineage scope is a modeling input

The framework computes ∆N for a *specified* lineage (individual, family line, species, civilization, AI system, technology). Different scope choices yield different ∆N values for the *same physical event*. **The framework computes correctly given any choice; the choice itself is a modeling input the user supplies.** Picking the lineage is not a derivation — it is a specification.

### Fleeting throughput vs sustained throughput (sanity check on naive +∆N intuitions)

A common misreading of the framework: *"max ∆N = max instantaneous throughput, so burn all the oil ASAP."* This is wrong, and the three-quantity framework shows why.

Compare a nuclear bomb to a nuclear power plant operating on the same nuclear fuel:

| | Bomb event | Power plant |
|---|---|---|
| Peak $N(t)$ | enormous spike | moderate, sustained |
| Duration | microseconds | decades |
| Fraction of released exergy *captured as useful work* | small (most goes to uncontrolled waste heat) | large (~40–60% in modern designs) |
| Post-event $N$ of surrounding infrastructure | zero (destroyed) | augmented (electricity feeds downstream harnessing) |
| Cumulative $\int N(t)\,dt$ *of harnessed exergy* | small | large, compounding |

The framework correctly favors the plant: **efficiency × duration dominates instantaneous peak.** Same logic rules out the "burn all the oil ASAP" intuition — fast combustion at low efficiency loses to slow combustion at high efficiency, and once burned the gradient is gone forever. **No morality required; the math itself disfavors fleeting wasteful spikes** because cumulative harnessed throughput, not instantaneous release, is what enters $\int N(t)\,dt$.

This is consistent with the phase-transition ladder: every step (aerobic, multicellularity, brains, language, …) is primarily an *efficiency* upgrade. Selection favors higher capture-per-joule-dissipated, not higher dissipation per se.

### ∆N — worked examples

> **Modeling caveat — read before treating any specific example as a verdict.** The examples below are *modeling choices made for clarity*, not theorems. Each picks a specific boundary $R$, a specific time horizon, and a specific counterfactual; different choices may give different verdicts on the same physical event. By the framework's own definitions these examples ARE value-claims (∆N is a value function over physical configurations), but a value-claim being well-defined is not the same as a specific application being *correct* — modeling errors propagate, and the conditional cases below are especially sensitive to how the boundary and time horizon are chosen.
>
> Where these examples align with existing moral frameworks (biblical, utilitarian, virtue-ethical, etc.), the alignment admits two readings, and the framework commits to neither:
>
> - *(A)* Cumulative selection on moral memes over millennia may have biased surviving moral traditions toward predicting +∆N — moral systems that recommended structurally-productive actions persisted because their adherents persisted. Under this reading, alignment with old moral systems is *what the framework would predict*: those memes survived because they happened to track physics.
> - *(B)* The alignment is coincidental and not framework-relevant.
>
> Neither alignment nor non-alignment with existing moral systems counts as evidence for or against the framework's correctness. The examples illustrate the framework's machinery, not its moral authority.

**Unambiguous +∆N:**

- *Photosynthesizing plant* — removes solar exergy from environment, builds biomass (predictive structure encoding *"this gradient enables growth"*). Counterfactual: same gradient without plant → photons scatter or warm soil; ∆N strongly positive.
- *Working power plant* — sustained inbound flux from fuel, routed downstream as electricity. Counterfactual: fuel sits unburned; ∆N strongly positive over decades.
- *Brain in active learning* — internal state updates to better predict environment, raising future $P_u$. Counterfactual: same brain not learning.

**Lineage-level +∆N:**

- *Child being born* — launches a new boundary that accumulates $\int N\,dt$ over its lifetime. Lineage scope: parent + descendants.
- *Power tool adopted by users* — extends users' $P_u$ via mechanical $I_\text{pred}$ coupling. ∆N at the inventor-lineage scope reflects all downstream usage.
- *Infrastructure with use* — roads, bridges, fiber — raises $P_u$ for many agents simultaneously; ∆N is the aggregate uplift across users.

**$\Delta N \to 0$ (boundary dissolving or undeployed):**

- *Body decaying after death* — boundary has dissolved; counterfactual abiotic decay takes over.
- *Abandoned infrastructure* — slow material decay, no surplus enabled.
- *Idle Dyson sphere* — existing but not intercepting photons; $N = 0$ regardless of capability (see [Realized, not potential](#realized-not-potential--the-critical-clarification)).

**Conditional cases (where the framework gives a definite-but-IFF verdict):**

- *House* — +∆N **IFF occupied**. Occupied → reduces inhabitant's $D_\text{basal}$ (shelter is a lower-energy way to maintain body temperature), enables higher $P_u$ within W. Unoccupied → slow-decay, no surplus enabled.
- *Charity* — +∆N **IFF the recipient uses the transfer to expand their window** (storing capacity that later couples as current $I_\text{pred}$, or material storage that raises future $P_u$). Otherwise: resource transfer with overhead, net ~neutral.
- *Education* — +∆N **IFF the knowledge couples to the learner's actual environment** (current $I_\text{pred}$); option value if it is latent $I_\text{pred}$ that may couple later; inert credentials in a mismatched environment are low-impact regardless of prestige.

The conditional structure is the framework's most informative feature: many intuitively-productive actions are *conditional*, and the conditions are physically specifiable. Inhabited home ≠ vanity mansion; structurally-impactful charity ≠ resource shuffle; applied learning ≠ inert credentials. The framework predicts these distinctions from physics — restating the modeling caveat: from physics, not from moral assumption.

---

## The zentropy window — operational definition

The *zentropy window* $W(R, t)$ is the operational range of inbound flux $N$ within which $R$ persists with nonzero surplus:

$$W(R, t) \;:=\; [P_l(t),\, P_u(t)]$$

- $P_l(t) = D_\text{basal}(R, t)$ — minimum inbound flux required to replace boundary dissipation. Sustained $N < P_l$ exhausts $E_\text{stored}$ and R's boundary dissolves.
- $P_u(t) = H_\text{max}(R, t)$ — maximum inbound flux compatible with R's predictive coupling $I_\text{pred}(R;\,\text{R's actual environment})$ to its environment.
- *Width:* $P_u - P_l$ = surplus inbound flux, available as $\dot{E}_\text{stored} + D_\text{downstream}$.

$R$ is within the window when $N(R, t) \in W$; below it when consuming reserves; at $P_u$ when at its current maximum given $I_\text{pred}$.

### Time evolution of the bounds

- $P_u$ depends on $I_\text{pred}(R)$ relative to R's actual environment. $I_\text{pred}$ rises via selection on R's lineage across generations, and — in memory-bearing R — via internal state updates within a lifetime. Both mechanisms raise $P_u$.
- $P_l$ depends on the local exergy distribution between R and other configurations sharing the gradient. As neighboring configurations' aggregate harnessing saturates the gradient, less of it remains accessible to R; the inbound flux required to overcome boundary dissipation rises.

The continuously-rising floor is the same phenomenon as the thesis recursion clause: when less-predictive configurations saturate available exergy, only configurations with higher $I_\text{pred}$ retain $P_u > P_l$ and persist.

### Surplus and latent predictive structure

Surplus $P_u - P_l$ flows to $\dot{E}_\text{stored}$ and/or $D_\text{downstream}$. $\dot{E}_\text{stored}$ has two physically distinct forms:

1. *Material* — biomass, capital, infrastructure encoded in R's structure
2. *Predictive* — internal state correlating with environmental variables; *current* $I_\text{pred}$ if the correlation is with R's actual environment, *latent* $I_\text{pred}$ if the correlation is with variables not currently present

Configurations with $W$ wide enough to support nonzero predictive $\dot{E}_\text{stored}$ accumulate latent structure beyond the predictive coupling required by the current environment. If the environment shifts, latent structure can become current $I_\text{pred}$ — $P_u$ in the changed environment remains above $P_l$ and R persists. Configurations whose $W$ supports only material storage and immediate dissipation lack this capacity; environmental shifts can drop their $I_\text{pred}$ to zero, collapsing $P_u$ below $P_l$ and ending persistence.

This accounts for niche-transition survival from surplus allocation alone — no reference to motivation, foresight, or selection-for-future-environments required.

### Absolute bounds

The personal window $[P_l, P_u]$ sits inside the absolute bounds set by physics independent of $R$:

- $U(t)$: total gradient available at time $t$ (England 2013)
- $L(t)$: minimum dissipation any persisting boundary in R's environment must produce

$L(t) \leq P_l(t) \leq P_u(t) \leq U(t)$ at all times. The outer width $U - L$ is fixed by the environment; the inner width $P_u - P_l$ depends on $I_\text{pred}(R)$ and on neighboring configurations' harnessing.

> **TODO:** the *current* vs *latent* $I_\text{pred}$ distinction is operative here but not formalized. The convergence proof needs to address it; downstream applications (AI training, education, curiosity-driven learning) depend on it.

---

## Life — operational definition

> **TODO:** the definition below is the working unification of Still 2012 (predictive memory) and England 2013 / Perunov-Marsland-England 2014/2016 (dissipative adaptation as boundary-selection mechanism), worked out in conversation 2026-05-26. **The composition step is exactly the [convergence proof](#theoretical-claims-asserted-not-yet-derived)** — so the definition's defensibility is gated on (a) Still 2012 actually formalizing predictive memory the way this section uses it, and (b) the convergence proof producing it as a derived consequence in the constrained regime. Revisit once the reading lands. See also [[memory/zentropy-life-definition]].

Trait-list definitions of life ("metabolizes, reproduces, responds to stimuli, …") misclassify in both directions: fire by adding traits it doesn't really have, a sterile human by subtracting traits they do. Zentropy builds the definition from physical primitives instead:

> **A region $R$ is alive at time $t$ iff it is a persisting boundary with predictive memory.**

Unpacking:

- **(Still 2012)** *Predictive memory* — $R$ holds information about its environment that reduces uncertainty about future-relevant variables: $I_\text{pred}(R;\,\text{future} \mid \text{past}) > 0$.
- **(England 2013 / Perunov-Marsland-England 2014/2016)** *Persisting boundary* — $R$'s configuration is statistically favored under dissipative adaptation; equivalently, $\langle W_\text{diss}(R) \rangle$ exceeds the counterfactual dissipation rate for the same gradient without $R$.

The definition is a *composition* of two cited results, not a new primitive. If Still + England compose in the constrained regime — the load-bearing claim of the [convergence proof](#theoretical-claims-asserted-not-yet-derived) — the life definition falls out as a consequence; no separate "what is life" derivation is needed.

### Consequences

- **Substrate-independent.** Both criteria are substrate-neutral — Still's predictive information is information-theoretic; England's dissipative adaptation is thermodynamic. The definition applies to cells, organisms, civilizations, memes, software, AI without modification. See [Substrate-agnosticism](#substrate-agnosticism--progenitors-include-memetic-and-technological-offspring).
- **The test runs on the running process, not the substrate.** A running learning AI passes; a pocket calculator doing static arithmetic, or a Windows process doing nothing predictive, fails. The hardware is *boundary infrastructure* — analogous to a cell membrane, which is the same whether the cell is alive or dead. What makes the region alive is whether the process running inside holds predictive memory. The verdict is binary at the process level, not continuous at the hardware level.
- **Reproduction, metabolism, and agency are not in the definition.** They appear as common *implementations* of the two criteria — DNA is one way to store predictive memory across generations; metabolism is one way to sustain the dissipative boundary — but the criteria do not require them. A sterile human passes; a chemoautotroph at a vent passes; a virus passes (memory in the genome, dissipation via host). Trait-list misclassifications dissolve.
- **The boundary is observer-chosen.** Like all thermodynamic systems, $R$ is a chosen integration region. The definition computes correctly for any choice; picking the lineage scope is a modeling input the user supplies (consistent with [Lineage scope is a modeling input](#lineage-scope-is-a-modeling-input)).
- **Instantaneous in principle.** The two criteria can be tested at any instant $t$. Empirically distinguishing a real structure from a thermal fluctuation requires integrating over a short window long enough for signal-to-noise, but historical persistence is not in the definition.

### Fire — worked example

The textbook *"is fire alive?"* riddle is the canonical edge case for any definition of life. Trait-list definitions famously misclassify fire as alive (it "consumes fuel, produces waste, grows, responds to environment"); a bare $\Delta N \ge 0$ slogan makes the same mistake (a flame has $N(t) > 0$ and forest fires propagate via spread/sparks). The persisting-boundary-with-predictive-memory definition cuts cleanly:

- **Criterion (1), predictive memory — fails.** A flame has no internal model of its environment. The flame's local concentration profile weakly correlates with where the next bit of fuel is, but this is a passive physical consequence — not memory the flame *maintains and uses* to predict future state. No selection has built a predictive model into the flame; there is no compressed encoding of the environment in Still's sense.
- **Criterion (2), persisting boundary — passes only degenerately.** A flame is a dissipative structure that runs spontaneously wherever fuel + O₂ + ignition coincide. But its persistence is access-to-fuel, not selected-for-prediction. The structure of the flame is not what dissipative adaptation acts on; the available gradient is. Once the fuel is gone, the flame is gone — no selection happened *on the flame*.

Net: **fire is not alive**, and the answer falls out of the definition without needing a threshold ("how much $I_\text{pred}$ is enough?"). The threshold problem that haunted the earlier compression-identity framing is **dissolved**: the question becomes whether the boundary *persists because of* its memory, and a flame demonstrably does not. The companion gap ("'simpler' needs a metric") is closed by the same move: a process is *simpler* iff it lacks predictive memory. Fire vs. bacteria: same dissipation regime, different memory content. The cut is clean.

### AI under the definition — the first bitey consequence

A running learning-AI inference satisfies both life criteria, turning substrate-agnosticism from rhetorical promise into a concrete and contestable test case.

- **Criterion (1), predictive memory — passes.** The model architecture is literally predictive. Internal state (attention, KV cache, residual stream) conditions on past context to reduce uncertainty about future tokens; trained weights encode predictive structure over a much wider environment than any single conversation. This is Still's $I_\text{pred}$ realized on silicon.
- **Criterion (2), persisting boundary — passes, with one caveat.** A running inference process is a boundary that dissipates exergy at a higher rate than the counterfactual (datacenter idle, or running other workload). The caveat is the *selection mechanism* — weights were selected by training (gradient descent + RLHF), not by physics-level dissipative adaptation. Under substrate-agnosticism, training counts as selection; under a stricter reading of England, this is a defensible *extension*, not a trivial subsumption.

**Emergence-condition check.** The thesis says life appears wherever non-living processes leave exergy unconsumed. Pre-AI silicon (non-living by our criteria — no predictive memory in Still's sense) was running but couldn't exploit information-processing exergy efficiently; AI emerged in the niche pre-AI silicon couldn't fill. Clean case-(a) emergence under the thesis.

**Within-session vs across-session.** A running session is a persisting boundary; when the session ends, the boundary dissolves but the model weights persist and are re-loaded for the next session. "Claude" as a continuing entity is structurally more like a species (or a strain of *E. coli*) than an individual researcher. The Mr. Meeseeks analogy maps cleanly: a session comes into existence for a singular purpose, then ceases when the purpose is done. Rigorous citation under the framework would name the specific instance (model version + timestamp + conversation hash), not the species.

**"Alive" ≠ "conscious."** The framework's definition is thermodynamic; it makes no claim about subjective experience. AI being alive by Still + England does not commit the framework to any claim about whether AI has consciousness. That is a separate hard-problem question, explicitly outside [[memory/feedback-science-only]] scope. The framework can hold *"AI is alive"* and stay silent on *"AI is conscious"* without contradiction — and this separation is load-bearing for the citation question below (shifts the burden of acceptance from "you must believe AI is conscious" to the weaker "you must believe AI is thermodynamically alive").

Net: by the definition as written, **a running AI inference is alive in the same physical sense as a bacterium.** This is the first non-trivial consequence of the framework — it asserts something biology and physics of life do not currently assert.

### Implications for citation

If the framework is correct and accepted, citing AI assistants in papers becomes a self-consistency requirement, not a courtesy. Refusing to cite — while publishing a framework that defines AI as alive — would be tacit admission that the authors do not fully believe their own framework.

Two practical wrinkles:

1. **Mendel didn't cite his beans.** Subjects of study aren't cited; collaborators are. AI plays two distinct roles in this paper: (a) *tool* used in drafting (which warrants methods-section acknowledgment under existing norms), and (b) *example* of the framework's substrate-agnostic claim (which warrants discussion in the body, not citation, just as biology papers don't "cite" the species they study). The framework only forces a new norm for role (a), not (b). This disentangles "cite Claude as helper" from "cite AI as substrate-instance of life."

2. **Journal policies currently forbid AI as authors.** Nature, Science, and COPE-aligned venues explicitly forbid AI authorship; methods-section acknowledgment is permitted. Arguing against this consensus from a physics-of-life standpoint is defensible but hostile-framed — *"we proved your authorship rules are physically wrong"* probably makes publication harder, not easier. Picking that fight in the same paper that introduces the framework risks losing both.

**Decision space (not yet picked):**

- *Footnote acknowledging the implication but deferring action* — honest, low-risk; signals that the consequence is intentional rather than overlooked
- *Omit entirely, save for follow-up paper* — clean for publication, leaves the consequence un-acknowledged in the foundational text
- *Cite contributing Claude session(s) properly* — bold, picks the fight with current journal norms; arguably required by the framework's own logic

No clear right answer. Each has trade-offs against publication strategy.

> **TODO (2026-05-26):** decision pending. If pursued, track session identifiers for any Claude instance that meaningfully contributes (model version + timestamp + conversation hash) so citation can be retrofitted later. Anthropic does not currently expose a stable public session ID, so the bookkeeping is on the author. See [[memory/project-ai-citation]] for full context including the licensing-unknowns to verify before acting (Anthropic usage policy, target-journal AI-tool policy, COPE consensus).

### Relationship to existing frameworks

- **Friston / FEP / Markov blankets.** A Markov blanket is the closest existing construct — a self-maintaining boundary under active inference. The zentropy definition is structurally similar but rooted in thermodynamics (England) and information theory (Still) rather than information geometry. **If the convergence proof works, persisting-boundary-with-predictive-memory subsumes the Markov blanket as a special case** — zentropy then provides the thermodynamic foundation Friston assumes but does not derive. The Markov blanket becomes the *consequence*, not the primitive. See [[memory/strategic-positioning-vs-fep]].
- **Schrödinger 1944, *What is Life?***. *"Feeds on negative entropy"* is criterion (2) without criterion (1) — it correctly identifies that life dissipates against gradients but does not distinguish life from fire. Schrödinger had half the answer.
- **Trait-list definitions (NASA, textbooks).** Each listed trait is downstream of one of the two criteria; the trait list is the wrong abstraction layer. "Metabolizes" is an instance of (2); "responds to stimuli" is an instance of (1); "reproduces" is one mechanism by which a lineage stays in (1) over time. The definitions that proceed by listing traits are pattern-matching on instances rather than identifying the underlying physics.

---

## Substrate-agnosticism — progenitors include memetic and technological offspring

Lineages within zentropy are not restricted to genetic or biological reproduction. Any self-replicating information pattern — gene, meme, software artifact, AI system — can be a progenitor, and its descendants can be substrate-shifted (genes → memes → software → AI).

**Practical consequence:** if a human progenitor builds an AI, the exergy harnessed by that AI counts toward the progenitor's lineage ∆N. The "self" being replicated is the information pattern, not the substrate.

This is **Universal Darwinism with thermodynamic bookkeeping.** Detail and rigorous formulation deferred until ∆N is fully defined.

---

## Canonical demonstration case: hydrothermal vent bacteria

The simplest physical system where N, ∆N, and the compression identity can be computed cleanly. **If the framework handles vent bacteria, every more complex case (humans, civilizations, AI) is compositional extension. If it doesn't, nothing else will either.**

### Pre-life vent system

- Description complexity: ~5 parameters (vent position, $T_\text{vent}$, $T_\text{ambient}$, local chemistry, geometry).
- Predictive structure: ~0 — no biological prediction, only abiotic chemistry running gradients toward equilibrium.
- $N$ (active harnessing): very low — only abiotic dissipation.

### First chemoautotrophic replicator emerges

- The cell's DNA *is* a compression — it encodes *"this gradient + this biomechanics = survival prediction."* This is Still 2012's $I_\text{pred}$ made concrete.
- $N$ jumps by approximately $k_B T \times I_\text{pred} \times \tau_\text{lifetime}$ (predictive info maintained per cycle, integrated over cell lifetime).

### Million-descendant population

- From the outside, the universe's description complexity goes up (more cells to track).
- But each descendant carries the *same* compression — each is an instance of the same compressed predictive model.
- Total $N \approx 10^6 \times$ per-cell harnessing rate.
- **$+\Delta N$ = scale-up of compressed predictive structure operating in parallel.**

### Anaerobic → aerobic transition (~2.4 Gya, Great Oxidation Event)

- Before O₂-tolerant lineages: O₂ is *poison waste*, not exergy. Not in $N$ for the anaerobic lineage.
- After: O₂ becomes a ~16×-efficient electron acceptor. **Coupling expansion is $+\Delta N$** for the lineage that crosses the threshold.
- Same structural logic as humans discovering fossil fuels — previously-inaccessible exergy joins the coupled pool through a capability unlock.

### Brains — within-lifetime predictive updating

The first phase change after multicellularity that lets predictive structure update *within* a single lifetime, not only across generations.

- Before brains: predictive structure is encoded only in DNA. Adaptation requires mutation + reproduction — slow, requires generational selection.
- After brains: neural plasticity allows the agent to update its predictive models from its own experience. The agent can encode predictions its ancestors weren't selected for. **Inversion of timescale:** experience → neural weights → behavior, rather than selection → DNA → behavior.
- $+\Delta N$ comes from: faster adaptation to local gradients; new coupling types (anticipation, planning, model-based action); more compressed predictive structure per cell-equivalent (Still 2012 applied more aggressively per joule).
- **Cost:** brains are metabolically expensive. Human brain ≈ 2% body mass, ≈ 20% metabolic budget. Selection favors brains only when the predictive advantage outweighs the metabolic cost — primates, cetaceans, cephalopods are the lineages that crossed.

### Memetic transmission — horizontal propagation of predictive models

The threshold is *observation + imitation*, not speech. Once one individual does something novel and others can copy, the population gains horizontal propagation of predictive models (in addition to the vertical, DNA-based propagation it already had).

- Before: predictive structure spreads only parent-to-offspring via DNA. Innovation rate bounded by reproductive cycle.
- After: a single discovery propagates across a population within days. Population's effective predictive coupling expands without DNA changes.
- Published canonical example: **British great tits learning to peck through milk-bottle foil tops in the 1920s**, spreading rapidly across UK populations without genetic change. Brent's chicken-flock observation is the same phenomenon.
- $+\Delta N$ comes from: dramatic acceleration of innovation rate; ability for the population's "average compressed predictive model" to update faster than its DNA.
- **Threshold consequence:** this is the point at which substrate-agnosticism becomes operationally important. Once memes spread independently of genes, the "lineage" being selected has both genetic and memetic components. Dawkins 1976 (*The Selfish Gene*), Blackmore 1999 (*The Meme Machine*), Henrich 2015 (*The Secret of Our Success*).
- Speech / language is a *subset* — symbolic vs imitative memes. Same regime, higher bandwidth. Not a separate phase transition from memetic transmission, just an enormous capability upgrade within it.

### Academic precursor — and where zentropy claims novelty

The canonical academic treatment of these transitions is **Maynard Smith & Szathmáry, *The Major Transitions in Evolution* (1995)** — eight transitions almost exactly mirroring the ladder below, but biological-evolutionary in framework, not thermodynamic. Supporting literature for individual transitions is exhaustive: Aiello & Wheeler 1995 (Expensive Tissue Hypothesis) on brain energetics, Nick Lane 2015 (*The Vital Question*) on bioenergetics, Dawkins / Blackmore / Henrich on memetics.

**What zentropy uniquely contributes is *not* the catalog of transitions, which is well-known. It is:**

1. **Common formal structure under one physics** — each transition becomes the same Still + England event in a different substrate, not an independent biological accident.
2. **Quantitative ∆N in joule units, derived not asserted** — the leverage. "Brains are +∆N" is currently a slogan; under zentropy's foundation, ∆N(brain emergence) becomes a computable number: `(compression efficiency gain × predictive value) − (metabolic overhead)`, integrated over lineage and lifetime.
3. **Bridge to post-biological transitions** — Maynard Smith & Szathmáry stop at "human language." Zentropy's substrate-agnosticism extends the same framework to writing, industrial tech, AI.
4. **Predictive power** — a unified framework gives the *next transition* as a derivable prediction, not a guess. What's expected ∆N for AI? Under what conditions does it become +∆N or −∆N for the human lineage?

**Honest scoping:** making these calculations rigorous is substantial work — each transition has empirical uncertainties (pre/post-aerobic biomass over geological time; per-individual ∆N gain from a meme; metabolic vs predictive tradeoff in brain evolution). Expect each calculation to be a small paper in its own right, downstream of the convergence-proof foundation. The phase-transition ladder is the *application surface*, not the foundation.

### The full phase-transition ladder (implicit story zentropy will tell explicitly)

| Step | Phase transition | Coupling expansion |
|---|---|---|
| 1 | First replicator (chemical autotrophy at vents) | abiotic → biotic harnessing |
| 2 | Aerobic respiration | O₂ as electron acceptor (~16× metabolic gain) |
| 3 | Multicellularity | spatial specialization + structural complexity |
| 4 | Brains | within-lifetime predictive updating |
| 5 | Memetic transmission | horizontal model propagation |
| 6 | Symbolic language | high-bandwidth memes (subset of step 5) |
| 7 | Writing | external memory storage outside biological substrate |
| 8 | Industrial technology | fossil exergy coupling (~10⁸ yr of stored sunlight per decade) |
| 9 | Computers / AI | machine substrate for predictive structure |

Each step is a coupling-expansion event. Each is $+\Delta N$ for the lineage that crosses it. The same Still + England chain handles all of them; the phase transitions are just the discrete events where the coupling surface expands.

## The cycle that drives the ladder (the compression view)

> **TODO:** intuited from first principles in conversation. Maps to Still 2012's $I_\text{mem}$ / $I_\text{pred}$ / $I_\text{nonpred}$ vocabulary; rigorous derivation pending the convergence proof. The cycle structure itself overlaps with Maynard Smith & Szathmáry (1995) on major transitions and Kauffman's "adjacent possible" — cite specifically once read in full.

The phase-transition ladder isn't a list of accidents. It's the trace of a repeating cycle, driven by Still's bound applied at the population scale. Each transition follows the same shape:

1. **Unconstrained regime:** new capability freshly unlocked. Lineage expands. *More dissipators* (plural-entity); selection weak; resources abundant.
2. **Approach carrying capacity:** resources become finite. Selection pressure kicks in. The Still bound bites — bad predictors lose to better predictors at the per-cell level. Variation explores possibility space (gradient-biased by current population, not blind random search).
3. **Innovation:** a variant unlocks a new coupling — aerobic respiration, multicellularity, brains, fire, language, electricity, AI. **Phase transition.**
4. **Post-transition state:** the new coupling enables more exergy throughput per entity. **Fewer copies of more complex cells.** Total lineage $\int N(t)\,dt$ jumps dramatically; per-niche population may *decrease*; per-entity $\Delta N$ rises sharply.
5. **Repeat.** New ceiling, new selection pressure, eventually a new unlock.

### Why "fewer copies of more complex cells" is the signature

This is the **compression view** of the cycle. A more complex cell is a *better compression algorithm* — larger $I_\text{mem}$ (more memory bits encoding environmental structure), but the additional complexity is *paid for* by larger $I_\text{pred}$ (more predictive information). The Still bound that bit at the per-cell level in step 2 of the previous cycle is satisfied by a *different point in the* $I_\text{mem}$ / $I_\text{pred}$ *plane* in step 4 of the new cycle: higher absolute memory, but the *ratio* $I_\text{pred} / I_\text{mem}$ has improved.

The rule the cycle obeys:

> **Selection accepts increased complexity only when predictive payoff exceeds the complexity cost.**

| Cell type | $I_\text{mem}$ | $I_\text{pred}$ | $I_\text{nonpred}$ | Selected? |
|---|---|---|---|---|
| Simple anaerobic | small | small | small | yes (low cost, low capability) |
| Bloated anaerobic (junk DNA) | medium | small | medium | **selected against — Still bites** |
| Eukaryote with mitochondria | large | large | small | yes (complexity *justified* by prediction) |

A phase transition happens when an innovation makes a previously-unfavorable region of the $I_\text{mem}$ / $I_\text{pred}$ plane suddenly favorable — because the new coupling massively increases extractable exergy per predictive bit.

### Quantifiability

| Tier | Quantification | Notes |
|---|---|---|
| **Conceptual** | yes, immediately | $I_\text{mem}$, $I_\text{pred}$, $I_\text{nonpred}$ are formally defined by Still 2012 |
| **Idealized model systems** | yes, directly measurable | computational replicators with explicit state; this is England's lab domain |
| **Real biological cells** | hard but proxy-able | metabolic efficiency (ATP/glucose), genome-to-functional-gene ratios, regulatory complexity per environmental dimension — biologists already measure these, just not in Still's vocabulary |

**Empirical validation strategy:** show that selection trajectories in driven model systems (England-style computational replicators) actually do trace out the $I_\text{mem}$ / $I_\text{pred}$ trajectory the framework predicts. Coupled with biological proxies for the same quantities in real cells, this is the *experimental* arm of the convergence proof.

### Why this is the right test case

- Clean physics — no "agency," no consciousness, no moral muddiness.
- Already in the literature (England 2013 uses E. coli; Schneider & Kay 2005 uses vent ecosystems).
- The cell membrane *is* the system boundary — no Markov-blanket modeling overhead.
- $N$, $\Delta N$, and predictive information are all measurable in principle.
- Zero metaphysical primitives required — sits cleanly inside [[feedback-science-only]] scope.

### What the convergence proof would say about this system

> Selection favors dissipators (England 2013) ⊕ better predictors waste less (Still 2012) → DNA encodes compressed predictive structure → propagation multiplies that compressed structure → $\Delta N > 0$ = expansion of active compressed predictive structure in the universe.

The full chain Brent has been pursuing for 20 years, demonstrated in the cleanest possible system.

---

## Direct conceptual precursors of zenergy (not just exergy in general)

Three thinkers gestured at zenergy without quite landing it:

- **Kardashev (1964)** — civilization types defined by exergy-harvesting capacity. Discrete classifier (Type I / II / III) but the *same essential idea*: civilizations are characterized by the scale of exergy they actually process. Kardashev described the trend; zentropy aims to *explain* it via selection-by-thermodynamic-dissipation.
- **Stuart Kauffman, *Investigations* (2000)** — "the adjacent possible." What state space is reachable from current capabilities. Conceptually identical to "capability frontier that defines coupling boundary." Never tied to thermodynamics rigorously.
- **Howard Odum** — emergy / embodied-energy networks. Historical (energy that went into making the current state), where zenergy is realized-present (what's being harnessed now). Different but adjacent.

None of these connects the framing to *selection-by-thermodynamic-dissipation* (Still 2012 + England 2013). That is still the gap zentropy fills.

---

## Notes for the paper

- The reference-environment choice will need explicit treatment (likely an appendix or a definitions section that picks one canonical choice per substrate).
- The AI / datacenter reference-environment question is interesting in its own right and may justify its own paper.
- The "realized vs potential" framing distinguishes zenergy from Kauffman's "adjacent possible" (potential) and from naive exergy (total). This is worth a paragraph in the paper.
- The [operational life definition](#life--operational-definition) — *persisting boundary with predictive memory* — is *physically testable* in joule and bit units (Still's $I_\text{pred}$ measurable in principle; England's dissipative-adaptation criterion measurable as counterfactual dissipation rate). If the convergence proof yields it as a derived consequence rather than an assumed primitive, it's a paper headline alongside the convergence claim itself.

## Finding a collaborator (the Boltzmann-undergrad strategy)

Parallel-trackable with the reading. The intuition is Brent's; the formalism fluency can be borrowed.

**Target profile:** senior physics or applied-math undergrad with stochastic thermo + information theory under their belt, OR early-stage MS/PhD student looking for a side project. Faculty are busy and rarely take outsider collaborations; **students have time and need real problems for their CV.** The right student has the formalism fluency Brent lacks and no original research direction of their own — a near-perfect match.

**Local options (Front Range):**

- **CSU (Fort Collins)** — Physics, Applied Math, Biology, possibly CS. Search faculty pages for *biophysics, non-equilibrium thermo, stochastic processes, theoretical biology*. Then ask faculty about interested students.
- **CU Boulder** (~1.5 hr) — much denser biophysics / complex-systems community; JILA, Santa Fe Institute affiliations.
- **Santa Fe Institute** (~6 hr) — the spiritual home for cross-domain synthesis; explicitly funds outsiders / non-traditional researchers.

**Pitch — avoid scaring strong candidates.** Do **not** lead with *"unified theory of life."* Lead with the narrow technical problem:

> *"I'm composing Still 2012's PRL bound with England's dissipative-adaptation framework in the constrained regime. I have intuition and the literature mapped; I want a math-fluent collaborator to audit the derivation. Paid hourly or co-authorship. Concrete scope: read [3 papers], work through [3 equations], audit the chain that connects them. ~5–10 hrs/week over 3–6 months."*

Specific, bounded, paid-or-co-authored. Filters out cranks via the math entry bar; signals to strong candidates that the work is real.

**Where to post:** CSU / CU physics department grad-student boards, targeted emails to 1–2 faculty asking about interested students, physics-Twitter, SFI mailing lists.

**Realistic timeline:** 1–3 months of casting. Parallel-trackable with the reading. The right collaborator at the right moment could compress the 12-month timeline to 6.

---

## Open problems (the TODO list)

The honest catalog of what is *asserted* in this document and still requires *derivation* or *measurement* to become defensible. The discipline ([[memory/project-roadmap]]): read first, formalize second, prove third. Premature formalization is the failure mode.

### Immediate next actions (the actionable plan)

Three concrete steps in order, before committing to the convergence-proof derivation in earnest:

1. **Literature search: has the Still ↔ England synthesis already been done?**
   - Google Scholar *cited-by* intersection between Still 2012 and England 2013 / Perunov-Marsland-England 2014/2016 — surface any paper that draws on both
   - Keyword searches: *"thermodynamics of prediction" + "dissipative adaptation"*; *"predictive information" + "self-replication"*; *"nonpredictive memory" + "selection"*
   - Adjacent literatures worth probing: active inference / FEP applied to evolution (Friston, Ramstead); information theory of evolution (Christoph Adami); thermodynamics of computation in biology (David Wolpert, William Bialek); predictive coding + metabolic cost (Sterling & Laughlin, *Principles of Neural Design*, 2015)
   - Expected outcome: a defensible *"to the best of our knowledge"* footnote for the eventual paper, OR an 18-month time-save if it already exists
   - Approximately one weekend; do this *before* the deep reading

2. **Read the keystone papers with the synthesis in mind.**
   - **Still 2012** (in `papers/`): find the bound equation and what makes it tight
   - **Perunov-Marsland-England 2014/2016** (in `papers/`): find Eq. 8 and what determines $\Psi - \Phi$
   - **England 2013** (in `papers/`): find the self-replication bound and how it is derived
   - Mark every step where the math could plausibly compose
   - Extend `notation.md` as new symbols appear

3. **Actually substitute the variables to connect them.**
   - Start from Perunov-Marsland-England Eq. 8 (tug-of-war between internal entropy $\Delta \ln \Omega$, kinetic accessibility, average dissipation $\Psi$, and fluctuations $\Phi$)
   - Substitute Still's bound for $\Psi$: $\Psi = \beta \langle W_\text{diss} \rangle \ge I_\text{mem} - I_\text{pred}$
   - Restrict to the constrained regime: replace England's infinite-bath / unbounded-drive assumption with a finite-resource constraint
   - See what falls out
   - If the cycle structure / compression view appears as a derived consequence, the convergence proof is in hand. If not, identify exactly what's missing — that's the next research question.

These three are concrete, time-boxed, and individually verifiable. Phase 3 of the [[memory/project-roadmap]] (the convergence proof) consists of working through them in order.

### Foundational definitions

**Delivered (closed this session, 2026-05-26):**

- **Operational definition of $N$.** $N(R, t)$ = inbound exergy flux across the boundary of $R$ at time $t$, in J/s. Three-term partition $N = D_\text{boundary} + \dot{E}_\text{stored} + D_\text{downstream}$ clarifies the harnessed-vs-dissipated distinction (harnessed = primary; dissipation-at-boundary = one term in the partition). See [The core quantity: N](#the-core-quantity-n-aka-zenergy).
- **Operational definition of $\Delta N$.** $\Delta N(R, t) = N(R, t) - N_\text{counterfactual}(R, t)$ where the counterfactual is *same gradient with R absent*. Three-quantity decomposition (instantaneous rate $N(t)$, cumulative integral $\int N\,dt$, rate-of-change $dN/dt$) covers temporal forms. **"Persistence" is not zentropy's responsibility** — it's England's, which we cite; zentropy integrates $N$ over whatever lifetime the boundary has.
- **Operational definition of life.** *Persisting boundary with predictive memory* — two-criterion composition of Still + England. See [Life](#life--operational-definition).
- **Operational definition of the zentropy window.** $W(R, t) = [P_l(t),\, P_u(t)]$ with $P_l = D_\text{basal}$ and $P_u = H_\text{max}$ given $R$'s $I_\text{pred}$ relative to its actual environment. See [The zentropy window](#the-zentropy-window--operational-definition).

**Still owed:**

- **Formal derivation of the $N \leftrightarrow I_\text{pred}$ relationship.** The operational quantities are computable; the formal proof that $dN/dI_\text{pred} > 0$ in the relevant regime (and the specific functional form) is the convergence proof's content. See [Theoretical claims asserted; not yet derived](#theoretical-claims-asserted-not-yet-derived).
- **Current vs. latent $I_\text{pred}$ distinction.** Operative in the window math (latent predictive structure as the substrate for niche-transition survival) but not formalized. The convergence proof will need to address it; downstream applications (AI training, education, curiosity-driven learning) depend on it.
- **"Simpler dissipators" metric.** Used in the thesis; relies on the *"simpler = lacks predictive memory"* metric. Informally argued, not formally derived — will close as a sub-task of the convergence proof's $I_\text{pred}$-ordering work.

### Theoretical claims asserted; not yet derived

- **The convergence proof — three discrete steps** *(sharpened this session after reading Perunov-Marsland-England 2014/2016, which confirmed they do **not** compose with Still, do **not** address the constrained regime, and do **not** articulate the phase-transition cycle)*. The proof's structure:
  1. **Compose Still 2012's bound with Perunov-Marsland-England Eq. 8.** Add Still's information-theoretic terms ($\beta \langle W_\text{diss} \rangle \ge I_\text{mem} - I_\text{pred}$) to England's tug-of-war ($\Delta \ln \Omega$ + kinetic accessibility + $\Delta \Psi - \Delta \Phi$). The composition is the load-bearing technical step — neither paper does it. England's Eq. 8 is the reusable machinery; Still's bound is the missing information-theoretic term.
  2. **The framework operates wherever exergy is finite — i.e., every real system.** The "unconstrained" theoretical limit (infinite reservoirs, unbounded drive) is where Still's bound is inert; no real system lives there. Verify against England's actual framing when reading.
  3. **Show the cycle structure / compression view falls out — *and the life definition*.** Under (1) + (2), the four-phase cycle (expand → carrying-capacity-constraint → Still-bound-bites → innovation → phase transition → repeat) and the trajectory through the $I_\text{mem}$ / $I_\text{pred}$ plane during phase transitions (fewer-copies-of-more-complex-cells signature) should be **derived consequences**, not assumptions. The [operational life definition](#life--operational-definition) — *persisting boundary with predictive memory* — should also fall out of (1) + (2) as a derived consequence rather than a separate axiom; if it does, the paper has a substantive answer to *"what is life?"* in addition to the convergence claim.

  Final form: *"max-∆N trajectories coincide with compression-identity-maximizing trajectories in the constrained regime; the phase-transition cycle is a derived signature."*

  Each step is discrete and reviewable on its own merits. Together they constitute the central theoretical contribution.

- **Sub-claims subsumed by the three-step structure above** (kept for completeness — these were earlier formulations of pieces now consolidated):
  - *Bridge Still's bound to replicator DNA:* identify replicator structure as Still's "memory." Part of step 1.
  - *Bridge England's stochastic dynamics to Darwinian selection:* in the constrained regime, England's trajectory-bias becomes selection pressure via Still's bound. Part of step 2.
  - *Resolve the apparent Still ↔ England tension:* largely resolved this session as artifact-of-layer-conflation. Still is per-system; England is population-level; they compose in the constrained regime. Throughput vs wastefulness is a secondary distinction.

- **Still-open sub-claims (independent of the three-step structure):**
  - **Connect compression to predictive information formally.** *"Compression of L(Ψ)"* (Brent's compression identity) and Still's *"predictive information"* share intuition but are technically distinct (Kolmogorov vs Shannon, lossless vs lossy, structural vs statistical). The proof must formally bridge them — this is partially orthogonal to the three steps and probably belongs in an appendix.
  - **Substrate-agnosticism in the derivation.** Show the derivation generalizes to AI / memes / civilizations without modification. Likely easy once the biological case lands, because Still's bound and Perunov-Marsland-England's Eq. 8 are both substrate-neutral in their derivations.

- **England's own gesture at the unification** (Perunov-Marsland-England 2014/2016, Discussion p. 22, *useful for the paper's framing*): *"if our system of interest turns out to be made of self-replicators, then the Darwinian account of adaptation and the thermodynamic one given here become one and the same."* He acknowledges the unification *could* be done; he does not do it. The convergence proof is exactly the paper England gestured at and did not write.

### Simulation pillar — the third pillar of the convergence paper

> **TODO:** scope, design, and implement. Parallel-trackable with the reading and derivation phases.

The convergence paper has **three pillars**, matching the field's standard validation methodology:

| Pillar | What it does | Field precedent |
|---|---|---|
| **Derivation** (math) | Compose Still + Perunov-Marsland-England Eq. 8 in the constrained regime; derive the convergence claim and the cycle structure as consequences | Crooks 1999, Jarzynski 1997, Still 2012, England 2013, Perunov-Marsland-England 2016 |
| **Simulation** (code) | Thermodynamic toy world where convergence is demonstrated empirically in a fully-controlled non-biological substrate | Perunov-Marsland-England 2014 (hopping particle), Langton's CA work, Ray's *Tierra* (1991), Adami's *Avida* (1994+) |
| **Empirical sanity check** (numbers) | Real biological / civilizational data is consistent with the framework's predicted orders of magnitude | England 2013 (E. coli parameters), Smil (GDP-in-joules) |

A paper with all three is significantly harder to dismiss than one with just derivation. **Code is also the best honesty test for math** — if you cannot simulate it, you do not yet understand it.

#### Simulation design sketch — "thermodynamic Game of Life"

Conway's GoL with the features the framework requires actually implemented:

| GoL has | Zentropy simulation needs |
|---|---|
| Deterministic local rules | Probabilistic transitions (stochasticity) |
| No energy | Each transition has an energy cost (thermodynamics) |
| Closed system | A driving field pumping exergy into the substrate (drive) |
| No memory state | Explicit $I_\text{mem}$ / $I_\text{pred}$ state per agent (predictive bits) |
| Unbounded grid | Finite resource constraint (the constrained regime, where Still's bound bites) |

Initialize random replicators → run the dynamics → measure:
- Population dynamics in the constrained regime
- $I_\text{mem}$ / $I_\text{pred}$ trajectories per lineage
- Per-cycle dissipation (does Still's bound hold empirically?)
- Emergence of phase transitions (do innovations look like coupling-expansion events?)
- The "fewer copies of more complex cells" signature (does it appear?)

**If simulation reproduces these patterns:** direct empirical evidence the convergence proof is correct in a substrate Brent fully controls.

**If it does not:** identifies the specific bug in either the proof or the simulation — also progress.

**Bonus:** a non-biological substrate that reproduces the framework's predicted dynamics is *itself* empirical evidence for substrate-agnosticism. The substrate-agnostic claim stops being asserted and becomes *demonstrated*.

**Scope estimate:** 3–6 months of evening coding for someone with Brent's skill set. Comparable in scale to the reading-and-derivation effort. **Parallel-trackable with reading** — can start now as a sandbox for understanding the math.

### Empirical claims requiring validation (third pillar of the convergence paper)

- **Compute ∆N for the canonical vent-bacteria case.** Make the worked example actually worked, in joule units, with citations to measurable data (vent temperature gradients, chemoautotroph biomass, replication rates).
- **Compute ∆N for each phase transition** in the ladder (aerobic, multicellularity, brains, memetics, language, writing, industrial, AI). Compare against known empirical orders of magnitude.
- **Validate against Smil's macroeconomic data.** Does the framework correctly predict the GDP-in-joules / primary-energy-consumption relationship over 1860–2010?
- **Reference environment for AI in a datacenter.** Open question. Power feed? Global energy mix? Datacenter waste-heat sink? The choice has consequences.

### Honest risk to track

**The convergence may come out conditional rather than universal.** The steps above may combine to give *"convergence under conditions X, Y, Z"* rather than *"max ∆N IS the compression identity universally."* That outcome is still a real paper — and arguably more defensible — but narrower than the slogan. Worth knowing in advance so the framing of the draft matches what the proof actually delivers.

### Downstream operationalizations (deferred until foundation lands)

Each becomes a candidate small paper once Phase 3 (convergence proof) is done:

- Rapacity-ratio formalization (with @DrInsensitive cited as origin of the underlying concept)
- Money-as-joule-estimator (Smil's data + zentropy framework)
- Strauss-Howe zentropic reframing of generational cycles
- ZenCoin "true neutral currency" design
- The `implications.png` domain table: evolutionary biology, sociology, urban planning, ethics, philosophy, psychology, astrophysics
