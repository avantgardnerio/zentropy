# Zentropy — Core Definitions (Spine)

Started 2026-05-28. **This is the live spine doc.** `definitions.md` is retired to reference/history (it became internally inconsistent across drafts — see `project-roadmap` memory). Land settled definitions here; flag unsettled ones explicitly.

Conventions:
- **[SETTLED]** = willing to defend as written in a paper.
- **[OPEN]** = direction agreed; formalization in progress.
- Memory pointers point at `memory/<name>.md` slugs (private memory, not in repo).

---

## 0. Status note

Zentropy has two layers. **Special** is settled enough to write up; **General** is the compass we're aiming at, with a sharper operational stub now in hand but not yet derivable. The spine doc reflects this: Special sections are nearly paper-ready; General is captured as the explicit search target, not as a derived result.

The central open question (see §3): how agent-scope $N$ and global-scope $\Delta N$ relate. We believe selection drives them into alignment; this is the prediction the spatial sim is built to test.

**Publication aim (added 2026-05-30).** A stat-mech paper on the molecular work alone is publishable on its own merit. The actual goal is broader: **bridge two communities — non-equilibrium thermodynamics (England-line dissipative adaptation) and evolutionary biology (Darwinian selection) — that currently treat their selection mechanisms as separate phenomena.** Zentropy's contribution: these are the same selection function operating on a scale-invariant quantity (predictive information per unit dissipation), evaluated in different cost-currency units at different substrates. The molecular work earns the right to make this bridge claim; the bridge is what makes the paper matter beyond its substrate. Discipline: molecular evidence in Results (rigorous, anchored); bridge claim in Discussion (interpretive, hedged). Framing detail in `[[strategic-england-darwin-bridge]]` (private memory).

---

## 1. Thesis

### 1a. Special zentropy **[SETTLED]**

> **Dissipative structures with predictive memory (i.e., life) are the configurations physics tends to produce wherever non-living dissipators leave exergy unconsumed. The same dynamic recurses (i.e., evolution): more predictive memory emerges wherever less predictive memory saturates.**

(Brought from `definitions.md`. Word-by-word unpacking lives there until the prose pass brings what's still settled forward. Key components: *dissipative structures* = Prigogine's term (no temporal/durability connotation — closure is the long-range correlation over which the system acts as a whole, not its lifetime); *predictive memory* = Still 2012's $I_\text{pred}$; *physics tends to produce* = statistical, not deterministic; *non-living dissipators leave exergy unconsumed* = the emergence condition; *the same dynamic recurses* = scale-invariance across phase transitions.)

### 1b. General zentropy **[OPEN — current best stub]**

The compass version (older, kept for the framing it provides):

> The universe wants to make copies of itself.

The operational stub (Brent, 2026-05-28 — what we are now actually searching for):

> **The Special process causes agents to approach the General optimum — known to an observer outside the universe — through the process of Still.**

Unpacking what this is saying:
- *The Special process* = within-replicator evolutionary selection on $N = \int (H-D)\,dt$ at agent scope.
- *Approach the General optimum* = converge toward behavior that tracks max $\Delta N$ at global scope.
- *Known to an observer outside the universe* = the global optimum is well-defined as a counterfactual integral; agents inside the universe cannot compute it — they can only *approximate* it.
- *Through the process of Still* = the approximation is built by predictive memory (Still 2012's $I_\text{pred}$). Agents whose policies carry more predictive bits about future-relevant variables behave more like the global optimum; agents carrying non-predictive bits pay $W_\text{diss} \geq k_B T(I_\text{mem} - I_\text{pred})$ and are selected against.

This is the General we are searching for. Not yet derived; capturing the target so the search has a fixed referent.

---

## 2. $N$ — stored exergy (agent scope) **[SETTLED]**

**Canonical (Brent, 2026-05-28): `N` means `H − D`. NOT `H` alone. NOT `D` alone.**

At an instant, for a single agent:

> $\dot N(t) = H(t) - D(t)$

where
- **$H$** = inbound exergy flux across the agent's boundary (rate, joules/s)
- **$D$** = boundary dissipation — exergy leaving the agent's boundary as heat to bath (rate, joules/s)
- **$\dot N$** = the agent's *storage rate* — net rate at which exergy is being accumulated as ordered configuration

Integrated over the agent's lifetime:

> $N(t) = \int_0^t \big(H(\tau) - D(\tau)\big)\, d\tau$

This is the **bank balance** (see `feedback-bank-not-cash`): stored exergy held as ordered configuration in the agent's body, structure, and internal predictive memory. Productive dissipation (consume gradient → store as self/kids/exports) raises $N$; destructive dissipation (consume order → store nothing) does not.

**Units:** joules. Equivalently, bits — via Landauer (1961; Bennett 2003 review in `papers/`):

> $1 \text{ bit} \equiv k_B T \ln 2 \text{ joules at temperature } T$

The framework is unit-flexible: write $N$ in joules when working thermodynamically, in bits when working with information content. Still 2012's $W_\text{diss} \geq k_B T(I_\text{mem} - I_\text{pred})$ IS this bridge applied to predictive information.

**Note on older drafts:** in earlier zentropy writing, $N$ was sometimes used to mean *inbound flux alone* ($H$), and the partition was written as $N = D_\text{boundary} + \dot E_\text{stored} + D_\text{downstream}$. **That overload is abandoned as of 2026-05-28.** From here: $N \equiv \int(H-D)dt$, $H$ is the inbound-flux symbol, $D$ is the boundary-dissipation symbol. Downstream routing is treated at the global scope (§3), not as a sub-partition of $N$.

**Note on $H$ — Kachman 2017 correspondence and the integration floor (added 2026-05-30).** In the passive (non-predictive) limit, $H$ is the *absorbed work* $W$ of Kachman, Owen & England 2017 (PRL 119, 038001): gross work flux from external drive into the system. Their cluster-level $W$ — work absorbed by the collective resonant mode, not by individual particles or individual bonds — is the closest analog to "the agent's $H$." Single-particle and single-bond $W$ are below the integration floor.

**The integration floor is physical, not a modeling choice.** $H$, $D$, $N$ are well-defined only at scales whose state can carry $I_\text{pred}$ — scales with enough internal degrees of freedom to mutual-inform with the future drive. A single particle cannot (no memory). A single bond in Kachman's regime carries $\sim 1$ bit of configurational state but does not phase-lock to drive. The resonant cluster *does*. So the smallest valid integration scope is the lowest-scale order-parameter degree of freedom (Prigogine 1977's "macroscopic variables") with nonzero $I_\text{pred}$ capacity. Above this floor the integration scale is a modeling choice; below it the central quantity is undefined. The $I_\text{pred}$-capacity criterion is zentropy's refinement on the prior-art order-parameter language.

---

## 3. $\Delta N$ at the **global scope** **[OPEN — formulation in development; FRAMING UNDER RECONSIDERATION 2026-05-28]**

> ⚠️ TERM TBD: "global scope" is a working placeholder. "Universe" is overused and not formal (Brent flagged 2026-05-28). See TBD section at end of doc for candidate replacements.

> ⚠️ **FRAMING UNDER RECONSIDERATION (Brent, 2026-05-28):** The "stored order with vs. without" formulation below may be subtly wrong — the universe's actual value function may be **max cumulative dissipation over the forward light cone**, with "max bank order" being the within-life *proximate mechanism* rather than the fundamental quantity. End-of-universe edge case (agents cannibalize at drive depletion, leaving no buried treasure) supports the cumulative-D reframing. See memory `project-value-function-question` "Reframing under consideration" section. The destruction-penalty and colonization-gain mechanisms in §3.2 survive either framing; what changes is the *naming of what they're achieving*. Do not commit §3 to paper-grade form before this resolves.

**The intent:**

> $\Delta N_\text{global}$ = (world's stored order WITH this agent / lineage) − (world's stored order WITHOUT it), integrated forward over the agent's causal trajectory.

This includes self + descendants + persistent exports + effects-at-distance (signed: positive for created order, negative for destroyed order). It is the value function Brent's lean (2026-05-28) holds is the *actually correct* one — agent-scope $N$ is its local approximation.

### 3.1 What is settled

- $\Delta N$ at the global scope is **signed**. Destruction of accumulated order in regions the agent affects subtracts from its global $\Delta N$, even when no flux crosses the agent's own boundary.
- The discriminator on a given act of dissipation is **"is the consumed order stored as new configuration somewhere?"** — productive → positive; destructive (consume, store nothing) → negative. Both increase local entropy; only the second loses score.
- The prediction is against *gratuitous* destruction (no storage payoff, no competitive payoff, no future-self benefit). Strategic destruction under selection pressure (antibiotic warfare, niche-clearing) is *not* predicted against.
- The reach extends substrate-agnostically — **bacterium-up** — because max-$\Delta N$ is substrate-agnostic by construction. This is the unique-prediction lane vs. biophilia / moral-foundations / cultural-group-selection / cognitive-economy alternatives, all of which require cognition. See `project-value-function-question` for the differential-prediction table.

### 3.2 The agent ↔ global alignment hypothesis (the central prediction)

**Selection at the agent level converges agents whose *behavior* tracks global $\Delta N$.** (Brent 2026-05-28: "the evolutionary process brings the organism in sync with the drive.")

The mechanism that makes this not magic:

> **Wanton destruction is non-predictive memory with a cost** (Brent, 2026-05-28).

An agent that destroys accumulated order without storing it is carrying *non-predictive bits* in Still 2012's sense — policy state that doesn't reduce uncertainty about future-relevant variables. Non-predictive memory pays $W_\text{diss} \geq k_B T(I_\text{mem} - I_\text{pred})$. So destructive behavior policies are thermodynamically wasteful by Still's existing bound, and selection prunes them.

**This collapses the destruction prediction into Still's existing framework.** We do not need an extra "destruction penalty" term. Agent-scope selection on Still's bound naturally produces alignment with global $\Delta N$. Wanton destroyers waste bits, pay $k_BT$ per wasted bit, lose to non-destroyers — all substrate-agnostically.

**The bidirectional symmetry — one inequality, two corollaries.** The destruction-penalty above has a positive-sign mirror: the **colonization-gain bound** (currently developed in `definitions.md` lines 167–198, queued to land in this spine). Both drop out of Still 2012's bound applied to opposite sides of the agent-environment interaction:

| Side of $\dot N = H - D$ | Corollary | Sign | Mechanism |
|---|---|---|---|
| $H$ (upper bound on harvest) | Colonization gain | $+$ | Better $I_\text{pred}$ match → more productive gradient extraction |
| $D$ (lower bound on dissipation) | Wanton-destruction penalty | $-$ | Non-predictive bits → forced $k_B T(I_\text{mem} - I_\text{pred})$ cost |

So **signed $\Delta N$ is fully captured by Still's bound** — no separate destruction-penalty term needed, no separate colonization-gain term needed. They are *one prediction read in two directions*. `definitions.md` flagged colonization-gain as zentropy's first piece that *extrapolates* beyond existing results — Still's kernel was fixed, so she derived the bound but never let prediction *be selected for*. Destruction-penalty is the same extrapolation, opposite sign: one mathematical move, two corollaries. **Selection across heritable kernels** (the [[project-sim-england-state]] "WHERE THE NOVELTY IS" framing) opens both directions simultaneously.

**Local divergences exist.** An agent's $N$ can momentarily diverge from its global $\Delta N$ contribution (e.g., short-term destructive behavior that has yet to be selected against). These are *impedances* (Brent's word, 2026-05-28) — resistances to alignment, not refutations of it. The system is driven *toward* alignment by selection on Still's bound, even when local realizations briefly disagree.

### 3.3 The inconsistency (the central tension to resolve)

Destruction of accumulated order in an *adjacent* region (outside the agent's boundary) is:
- **NOT counted as $-H$** in the agent's $N$ — no flux crosses the agent's boundary either way.
- **Counted in the global $\Delta N$ counterfactual** — the world has less stored order with the agent than without.

So agent-scope $N$ and global-scope $\Delta N$ can diverge. The alignment hypothesis above says selection drives them into agreement *over time*; the inconsistency just observes that they can be transiently misaligned in instantaneous bookkeeping.

### 3.4 The sim's confirmation criterion

> **The spatial sim should show convergence between agent-scope $N$ and global-scope $\Delta N$ over evolutionary time.** That convergence — not raw growth, not max $\Delta N$ in absolute terms — *is* the prediction. This is why we integrate global $\Delta N$ (Brent 2026-05-28). See `pacman.py` and `project-sim-england-state` 2026-05-28.

### 3.5 What is NOT yet settled

- The exact form of the integral (what counts as an "effect"; how to bound the forward trajectory; how to define the passive-baseline counterfactual formally).
- The precise relationship between the alignment dynamics and Still's bound (sketched in §3.2 above; not yet derived).
- Whether the global formulation admits a closed-form expression or only an operational (sim-based) one.

**Brent's posture (2026-05-28):** *"I think the global version is correct. Maybe we can't write this up yet."* The lean is firm, the math is not. This section stays [OPEN] until lower-tier sim work (`england.py` → `still.py` → `zentropy.py` → `pacman.py`) lands, per `feedback-foundation-first`.

**Connections:** `project-value-function-question`, `project-sim-england-state`, `project-civilizational-reach` (private — human-moral-intuition framing inherits that memory's "never in paper or git" restriction; bacterium-up framing may be paper-safe because it's a thermodynamic prediction, not a moral claim).

---

## 4. Life **[SETTLED]**

> **Life ≡ a dissipative structure with predictive memory.**

**Note on terminology:** Prigogine's "dissipative structure" carries no temporal/durability connotation — its closure is the long-range correlation over which the system acts as a whole, not its lifetime. Life needs no minimum lifetime to count as life under this definition.

Composition: England 2013 (dissipative adaptation supplies the "dissipative structure") + Still 2012 (predictive information supplies "predictive memory"). Substrate-neutral by construction. Memory `zentropy-life-definition` carries the fuller operational treatment, including the precise criterion (a region $R$ is alive at $t$ iff it holds predictive information *and* its dissipation excess vs. counterfactual is causally attributable to that memory) and the worked edge cases (fire, sterile human, virus, running learning AI, pocket calculator).

---

## 5. Window $W$ **[SETTLED — redefined in H/D terms 2026-05-28]**

**Working redefinition (Brent, 2026-05-28):** the window is now expressed in concrete H/D terms.

At any instant, the **window** is the storage gap between inbound flux and forced dissipation:

> $W(t) = H(t) - D(t)$

(This is $\dot N$ from §2 by another name. The window framing emphasizes that $W$ is the *operational range available* to the agent — positive $W$ means surplus, negative $W$ means depletion.)

An agent's $N$ — its lifetime bank balance, the integral from §2 — is exactly the integral of its window size over time:

> $N = \int_0^t W(\tau)\, d\tau = \int_0^t (H - D)\, d\tau$

**Interpretation:**
- A pure dissipator (fire, hurricane) has $H \approx D$ throughout its existence: $W \approx 0$, builds nothing. The window collapses; no surplus is available to store, grow, or reproduce.
- A living system maintains $H > D$ with surplus routed into stored order: $W > 0$ sustained, surplus accumulates as $N$.
- A dying system has $H < D$: $W < 0$, depletion, $N$ falling.

**Empirical anchor — Kachman 2017 as structural test (added 2026-05-30).** Kachman, Owen & England 2017 (PRL 119, 038001) is a pure-dissipator substrate by construction: no storage channel beyond bounded spring potential, so energy conservation forces $\langle H \rangle \approx \langle D \rangle$ at steady state and $W \approx 0$ throughout. The two regimes reported — catch bonds (max-$H$ operating point) and snap bonds (min-$D$ operating point, supp Fig S8) — are both pure-dissipator strategies on the $W \approx 0$ line; the $\max(H - D) > 0$ strategy this section identifies with life cannot emerge in Kachman's setup because the substrate cannot store. If a storage channel is added and a third selection strategy with sustained $W > 0$ does *not* emerge alongside catch/snap, this section's framing fails on its own terms. Reference-impl + storage-extension build: `kachman.py` (2026-05-30; see `project-ipred-pivot` and `project-reference-impl-opportunity`).

**Bidirectional $H/D$ selection — empirical hook in Kachman's snap result (added 2026-05-30).** Kachman et al.'s supplemental material reports the snap-bond outcome as "***strikingly***, the spectrum of such systems showed a suppression effect in frequencies around the driving frequency" with "***results reversed relative to those reported in the main text***" (supp p13) — explicit surprise language. In zentropy's framing, this is the $D$-side twin of catch's $H$-side result: catch bonds select configurations that maximize work absorption $H$ at the drive frequency; snap bonds select configurations that minimize forced dissipation $D$ by decoupling from the drive frequency. Both selections fall out of the *same* Still 2012 bound applied to opposite operating points along the $W = H - D \approx 0$ line. Kachman et al. note the inversion as striking but do not develop a unifying mechanism — and additionally observe (same paragraph) that "the projection of the force vector in the normal mode basis shows that the same frequencies also tend to decouple from the drive," a positive feedback they record but do not theorize. This is the first zentropy prediction in this document with an explicit empirical hook into prior peer-reviewed data that prior work observes but does not formalize.

> ⚠️ **TODO — empirical and prior-art gates.** This contribution claim requires:
> 1. `kachman.py` Phase 1d-ii: reproduce Kachman's green snap-bond curve (Fig S8) via the same Still-bound machinery as catch, on the same reference impl. **Partial close (2026-05-30):** snap is qualitatively reproduced — visible avoidance dip at $\omega_d$, slight rightward shift of the haystack tail vs the undriven baseline — confirmed under $N_{\text{seeds}} = 5$ ensemble averaging. NOT yet quantitatively reproduced: Kachman's published Fig S8 green has a *sharp zero* at $\omega_d$ and a tight bell at $\omega \approx 3.7$; our reproduction has a small residual at $\omega_d$ and a broader haystack at $\omega \approx 3.0$. The PUBLISHED curve strongly supports the prediction; OUR reproduction supports it qualitatively but weakly. Kachman's snap parameters are unpublished (supp p13: "qualitative results not finely sensitive to these choices") and we have not yet found parameters that strongly reproduce the published shape. Gate 1 is *partially* closed.
> 2. Prior-art audit confirming no prior publication frames catch/snap bidirectional selection as a unified Still-bounded mechanism. Candidates to verify against: Adler/Kolchinsky dissipation-bound work, Walker & Davies, the broader active-matter literature. Pending; mirrors the §6 TODO.
>
> Until both gates land, the contribution claim is provisional.

The earlier $W = [P_l, P_u]$ range framing (lower = survival floor, upper = $I_\text{pred}$-set saturation ceiling) is consistent with this: $P_l$ is the forced-$D$ floor, $P_u$ is the gross-$H$ ceiling, the *width* $P_u - P_l$ at instant $t$ is exactly $W(t) = H - D$.

> **Interpretation flag — needs Brent's confirmation:** I'm reading "an agent's $\Delta N$ is the integral over time of its window size at any one moment" as $W(t) = H(t) - D(t)$ and $\Delta N_\text{agent} = \int W\, dt$. If you meant window *width* of a range $[P_l, P_u]$ that differs from $H - D$, the math reconciles slightly differently. Confirm or correct.

---

## 6. Abiogenesis as $M$-axis phase transition **[OPEN — claim 2026-05-30; prior-art audit pending]**

> ⚠️ **TODO — prior-art audit before this section becomes paper-grade.** The *phase-transition* framing of abiogenesis is established in the literature; what may be novel here is the *specific* crossover variable ($M$ = environmental drive complexity) tied to the *specific* Still 2012 bound $W_\text{diss} \geq k_B T(I_\text{mem} - I_\text{pred})$. Verify against:
> - Walker, S. I. & Davies, P. C. W. 2013, *J. R. Soc. Interface* 10:20120869, "The algorithmic origins of life" — information-theoretic OoL framing.
> - Smith, E. & Morowitz, H. J., *The Origin and Nature of Life on Earth* (2016); Smith's solo papers on origin-of-life-as-planetary-phase-transition.
> - Vanchurin, V. & Koonin, E. V. 2022, *PNAS* "Thermodynamics of evolution and origin of life" — already in `papers/`, in `[[reference-sim-literature-landscape]]`.
> - Possibly nearby: Eigen hypercycles; Kauffman 1993 *Origins of Order* autocatalytic-set thresholds; Walker assembly-theory papers (post-2020).
>
> Locate zentropy's specific contribution in the gap (if any). If the Still-bounded $M^*$-crossover is already published in essentially this form, cite and cut; if not, this is a candidate publishable slot.

**The argument.**

For an agent embedded in a driven environment of complexity $M$ (the number of incommensurate components of the drive; see $N^*(M)$ framing in `[[project-sim-england-state]]`):

- **Strategy A (no inheritance):** each agent discovers its predictive kernel from scratch within its own lifetime via Still-bounded selection on configurations. The dissipative cost of discovery scales with the kernel size required for the environment, which by the pacman-drive prediction is $N^* \approx 2M$ bits.
- **Strategy B (heritable kernel + replication machinery):** pay a fixed upfront cost $K$ for replication machinery (substrate-dependent; Landauer-priced bits required to encode the copy mechanism); daughters inherit the parent's kernel without rediscovery.

Strategy A is selected when discovering the kernel is cheaper than building+running replication machinery. Strategy B is selected when the per-generation rediscovery cost exceeds the amortized cost of replication. The crossover defines:

> $M^* \equiv$ the environmental complexity at which Strategy B first becomes thermodynamically favored over Strategy A.

> ⚠️ **TODO — exact form of $M^*$.** The crossover formula has a clean qualitative shape (A grows in $M$, B has a floor) but the precise functional form depends on substrate-dependent constants and on assumptions about discovery-vs-copy bit cost. Tentative form $M^* \sim K / (c \cdot k_B T)$ with $c$ a substrate-dependent per-bit cost requires derivation. Either land it analytically in this section or supply it empirically from `kachman.py` Phase 3 (see below).

> ⚠️ **TODO — substrate-primitive prerequisite (2026-06-17).** The A-vs-B binary presupposes substrates where storage capacity exists somewhere to be inherited. A candidate intermediate Strategy A.5 (storage-capable, non-replicating) may need separating before the M* crossover is well-posed; if real, §6 becomes a three-strategy phase diagram. Substrate test sketch (bistable bonds + non-harmonic drive) in `[[project-kachman-bistable-extension]]`; not committed.

**Interpretation.**

Abiogenesis is a phase transition in environmental complexity $M$, not a contingent chemical event. Below $M^*$, predictive dissipative structures (catch-bond clusters; Kachman 2017) exist and are selected, but replication is not. Above $M^*$, replication is thermodynamically favored — heritable kernels amortize Still-discovery cost across generations. $M^*$ is substrate-dependent (different $K$ and $c$ per substrate); the *crossover existence* is the substrate-agnostic claim.

**Falsifiability.**

The $M$-axis sweep is built into `kachman.py` Phase 3 (2026-05-30): vary $M$ in the pacman-drive variant; locate the $M$ at which the storage-enabled regime first beats pure-dissipator catch/snap. That $M$ is $M^*$ for the Kachman substrate.

Falsification conditions:
- No third strategy emerges at any $M$ → §5's framing fails (already flagged in §5).
- Third strategy emerges but $M^*$ does not scale with $K$ → this section's specific crossover argument is wrong in form even if the qualitative phenomenon is real.
- $M^*$ scales but in a way unrelated to Still's $I_\text{nonpred}$ bound → the crossover may be real but not the one zentropy claims.

**Connections.**

- Supplies the missing mechanism for §1a's "where non-living dissipators leave exergy unconsumed" — translates the existing thesis-as-intuition into a specific thermodynamic crossover.
- Tightens §4 (Life): predictive dissipative structures exist at all $M$; *life with replication* — the colloquial sense — emerges at $M^*$. The catch-bond cluster (Kachman 2017) is an $M < M^*$ exemplar. See `[[zentropy-life-definition]]` for the tiered framing.
- Test instrument: `kachman.py` Phase 3 with the pacman-drive variant (see `[[project-ipred-pivot]]`).
- Astrobiological prediction: simple-environment planets (small $M$) → catch-bond-like proto-life forever, no replicators. Complex-environment planets (large $M$, e.g. Earth) → replicators thermodynamically inevitable. Falsifiable in principle, not in practice on human timescales.

---

## 7. Acquisition cost vs. storage cost **[OPEN — 2026-05-30; falsification path in `kachman.py` PREDICTION 4]**

Standard information-thermodynamic accounting (Landauer 1961; Bennett 1982) focuses on the thermodynamic cost of *storing* or erasing bits. At the molecular regime, storage and acquisition are inseparable — the medium holding the bit IS the thermal bath, so the marginal cost of an additional predictive bit is approximately the Landauer floor regardless of which side you account against.

At higher scales the two decouple. A modern hard drive's per-bit storage cost is many orders of magnitude above Landauer but amortizes to near-zero per relevant transaction; the binding cost migrates to the *acquisition* side — the dissipation required to identify *which* bit to store. Information economics (Grossman & Stiglitz 1980) and evolutionary theory (Van Valen 1973, Red Queen) both observe that in competitive settings the acquisition cost is set endogenously by the marginal competing predictor's expenditure, not by a physical floor.

**Working claim (Brent, 2026-05-30; not yet derived):** selection grades agents on the cost to *acquire* the next predictive bit, not on the cost to *store* it. Storage cost was a reliable proxy at the molecular regime where the two coincide; at higher scales the proxy fails. This refines `feedback-bank-not-cash`'s storage-as-bank framing — the bank is the *receipt* of past acquisition; selection grades against the price of *adding to* the bank, which is regime-dependent.

**Cost-floor decomposition (provisional form):**

> cost-per-acquired-bit ≈ $\max(\text{thermal floor}, \text{adversarial floor})$

- **Thermal floor:** $\sim k_B T \ln 2$ (Landauer). Physics-set; dominant when no competing predictor exists.
- **Adversarial floor:** the marginal competing predictor's per-bit expenditure (Grossman-Stiglitz form). Population-set; dominant when competing structures bid for the same gradient.

The two floors swap dominance with substrate. At molecular substrates with no competing predictor, only the thermal floor applies. At any scale with competing predictors, the adversarial floor dominates.

**Abiogenesis hook (orthogonal-mechanism complement to §6).** The adversarial floor is endogenous to the population of existing predictors. Pre-life Earth had adversarial floor $\approx 0$ — only the thermal floor applied, and the first predictive dissipators paid Landauer prices for their structure. Once life exists, the adversarial floor rises for any nascent would-be predictor competing for the same gradients. This gives a thermodynamic argument for abiogenesis difficulty in present conditions that is distinct from chemistry-specific arguments: the floor that the first replicators paid was lower than any subsequent one. §6's $M^*$ crossover and §7's adversarial-floor-rises mechanism are not in competition — they describe the same threshold from different lenses (when does replication pay vs. how does the cost floor rise once it does).

**Falsifiability via Kachman (`kachman.py` PREDICTION 4).** Kachman is single-substrate with no competing predictors, so only the **thermal half** of the claim is testable here; the adversarial half awaits multi-agent substrates. Four sub-tests, with the PREDICTION-number reflecting which zentropy claim is tested (the build-order is separate; see `kachman.py` PHASE 1.5–2.5):

1. **Cumulative-dissipation knee** *(near-term — needs ~5 lines of $W_\text{diss}$ instrumentation in `run_sim` + re-run; no substrate changes)* — does $\int W_\text{diss}\,d\tau$ for the catch-driven run show a steeper initial slope during the acquisition transient (the Fig S2 red box) and a lower steady-state slope after? The excess area is the acquisition cost.
2. **Marginal $dI/dW_\text{diss}$ decline** *(needs sub-test 1's $W_\text{diss}$ instrumentation + a per-window structural-encoding estimator; can use `measure_drive_encoding.py`'s $I(A_\text{feature}; \omega_d)$ as near-term substitute for proper $I_\text{pred}$ before Phase 2 lands)* — does the bits-of-structure-per-joule ratio decline as the system fills its niche, toward a steady-state maintenance floor?
3. **Hysteresis test** *(new runs, no substrate changes — just a runner script that does drive → equilibrate → drive)* — at the same $\omega_d$, is the second transient shorter or cheaper than the first, indicating retained structural memory?
4. **Quench-depth test** *(variant of 3 with swept equilibration duration)* — is re-acquisition cost non-linear in the fraction of structure lost?

Falsification: no knee in (1) kills the substrate-level reframe; flat marginal ratio in (2) means acquisition and steady-state costs are indistinguishable; absence of hysteresis in (3) or linear quench-depth scaling in (4) means re-acquisition is path-independent and the "cost-to-re-learn" framing has no Kachman-level handle. Per `feedback-sim-first`: sub-tests 1, 3, 4 are independently approachable now (no new physics, no Phase 2 dependency). Sub-test 1 is the shortest path to ANY PREDICTION-4 result; sub-tests 3 and 4 become worth the runner-script investment if 1 shows the predicted knee.

**Term-audit TODO** (per `feedback-coined-terms`). *Acquisition cost* and *storage cost* are established literature vocabulary (Grossman-Stiglitz 1980; Bennett 1982). *Thermal floor* is descriptive. *Adversarial floor* is borderline-coined — Grossman-Stiglitz themselves use "information acquisition cost"; the biology side uses "Red Queen cost." Audit before promoting any of this section to write-up form.

**Connections.** Refines `feedback-bank-not-cash`'s storage-as-bank framing; supplies the molecular falsification path before the cross-scale claim (currently `[[strategic-england-darwin-bridge]]` in private memory) can be promoted to artifact; orthogonal-mechanism complement to §6's $M^*$ crossover; tightens §5's window framing by identifying *which side of the window* selection actually grades on.

---

## TBD — naming choice

Throughout §3, **"global scope"** is a placeholder for the level above agent-scope. Brent flagged 2026-05-28: "universe" is overused and not formal. Candidate replacements (awaiting your pick — then propagate throughout doc and relevant memories):

- **Global scope** — current placeholder; inherits conversational vocabulary; vague.
- **Forward light cone (scope)** — physics-precise; captures the integrated forward-trajectory aspect.
- **Causal scope** — captures "everything the agent causally affects" without overpromising relativistic precision.
- **Counterfactual scope** — names the defining feature (diff against agent-absent baseline) rather than spatial reach.
- **Worldtube scope** — uses `definitions.md`'s existing language (descent-closed worldtube extended to include exports).

---

## Sections still to land

The following sections existed in `definitions.md` and are likely to need a place here once their settled form is decided. Not blocking; queued.

- **N partition / harnessed vs. dissipated reconciliation** — partially superseded by §2's canonical $N = H - D$ rewrite; the worked-example table (photosynthesis, aerobic respiration, etc.) is probably still useful as illustration.
- **Lineage scope / worldtube** — `definitions.md` developed individual vs. lineage scope and the colonization-gain bound. The lineage scope is implicit in §3 already; whether the worldtube formalism needs explicit treatment here depends on the global-scope naming choice and what we want to keep paper-side.
- **Phase-transition ladder** — implication, not definition; probably belongs in the downstream-applications doc rather than the spine.
