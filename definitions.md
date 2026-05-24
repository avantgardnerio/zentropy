# Zentropy — Working Definitions

This file captures the formal definitions zentropy is converging on. Living document — will sharpen as the reading queue closes and each quantity is pinned down rigorously.

**Scope** (locked, see `memory/feedback-science-only.md`): only physical and information-theoretic quantities as primitives — joules, bits, kelvins, time, distance, probability. Concepts like *agency, intention, consciousness, purpose, meaning, ethics* may not be assumed; they may, however, be *derived* from the dynamics. Reducing previously-metaphysical claims to physics is the long-term consilience goal — but only via derivation, never by primitive assumption.

---

## The core quantity: N (a.k.a. *zenergy*)

```
N(t) := exergy presently being harnessed by an agent or lineage at time t,
        within the forward light cone
```

Units: joules.

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

## ∆N (preliminary)

```
∆N = change in N over an interval — i.e., change in actively harnessed exergy
```

`∆N > 0`: agent has begun harnessing what it wasn't before (capability deployment, new flows, phase transitions).
`∆N ≈ 0`: stasis — current harnessing rate matches losses, no net expansion.
`∆N < 0`: contraction — agent is losing access to previously-harnessed flows.

**Working claim** (potential paper headline, defensible if it holds):

> **Life is defined by ∆N ≥ 0 over its lifetime.**

Abiotic processes shuffle exergy *within* whatever coupling already exists; they don't *expand* coupling. Only replicating / evolving systems grow N. Therefore `∆N ≥ 0` is the **thermodynamic signature of life** — applies substrate-agnostically to cells, civilizations, AIs.

Precise integration measure (per-agent, per-lineage, per-light-cone) deferred until the convergence proof determines what shape ∆N needs to take.

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
- "Life = ∆N ≥ 0" is a *physically testable* definition. If it holds, it's a paper headline.
