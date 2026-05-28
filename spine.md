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

---

## 1. Thesis

### 1a. Special zentropy **[SETTLED]**

> **Dissipative structures with predictive memory (i.e., life) are the configurations physics tends to produce wherever non-living dissipators leave exergy unconsumed. The same dynamic recurses (i.e., evolution): more predictive memory emerges wherever less predictive memory saturates.**

(Brought from `definitions.md`. Word-by-word unpacking lives there until the prose pass brings what's still settled forward. Key components: *dissipative structures* = Prigogine's term, replaces the earlier "persisting boundary," whose temporal connotation is rejected; *predictive memory* = Still 2012's $I_\text{pred}$; *physics tends to produce* = statistical, not deterministic; *non-living dissipators leave exergy unconsumed* = the emergence condition; *the same dynamic recurses* = scale-invariance across phase transitions.)

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

---

## 3. $\Delta N$ at the **global scope** **[OPEN — formulation in development]**

> ⚠️ TERM TBD: "global scope" is a working placeholder. "Universe" is overused and not formal (Brent flagged 2026-05-28). See TBD section at end of doc for candidate replacements.

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

**Note on terminology (Brent, 2026-05-28):** "Dissipative structure" *deliberately replaces* the earlier "persisting boundary." Prigogine's term carries no temporal/durability connotation — its closure is the long-range correlation over which the system acts as a whole, not its lifetime. Life needs no minimum lifetime to count as life under this definition.

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

The earlier $W = [P_l, P_u]$ range framing (lower = survival floor, upper = $I_\text{pred}$-set saturation ceiling) is consistent with this: $P_l$ is the forced-$D$ floor, $P_u$ is the gross-$H$ ceiling, the *width* $P_u - P_l$ at instant $t$ is exactly $W(t) = H - D$.

> **Interpretation flag — needs Brent's confirmation:** I'm reading "an agent's $\Delta N$ is the integral over time of its window size at any one moment" as $W(t) = H(t) - D(t)$ and $\Delta N_\text{agent} = \int W\, dt$. If you meant window *width* of a range $[P_l, P_u]$ that differs from $H - D$, the math reconciles slightly differently. Confirm or correct.

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
