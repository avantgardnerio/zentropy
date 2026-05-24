# Zentropy Notation Glossary

A working glossary mapping Greek letters, symbols, and key equations from the zentropy reading queue to plain-English meanings and programmer-friendly intuitions.

**How to view:** open in PyCharm with the Markdown preview pane enabled (View → Tool Windows → Markdown, or click the preview icon in the top-right of the editor). Equations render via KaTeX. Also renders on GitHub.

**How to extend:** as we read each new paper, add any new symbols to the **Greek letters** or **Notation conventions** sections (only if not already there), and add a new subsection under **Key equations by paper**.

**Pronunciation convention:** US-academic, since that's what's used in physics talks and seminars. UK variants noted where they diverge meaningfully.

---

## Greek letters

### β — "BAY-tah" (beta)

- **In stat mech / info-thermo:** inverse temperature. $\beta = 1/(k_B T)$.
- **Programmer intuition:** a unit-conversion factor that strips the joules off an energy. $k_B T$ at room temperature is about 25 meV — the typical kick from random thermal noise. Multiplying an energy by $\beta$ gives you a dimensionless number measured in "thermal fluctuation units," directly comparable to information measured in nats.
- **Why this matters in Still 2012:** Eq. 14 reads $\beta \langle W_\text{diss} \rangle = I_\text{mem} - I_\text{pred}$. Without $\beta$, you'd be comparing joules (left side) to bits (right side) — apples to oranges. With $\beta$, both sides are dimensionless and comparable. This is how thermodynamics and information theory get welded together.
- **Convention warning:** in statistics, $\beta$ usually means a regression coefficient. Different field, different meaning. Always check context.

### τ — "tow" (rhymes with "cow"), or "taw" (tau)

- **In Still 2012:** total duration of a driving protocol. The endpoint of the time loop.
- **Programmer intuition:** the last index. If $t \in \{0, 1, \ldots, \tau\}$, then $\tau$ is the loop bound.
- **Convention warning:** in other thermo papers, $\tau$ often means a *relaxation time* (how fast a system equilibrates). Always check context.

### Δ, δ — "DELT-ah" (delta, capital and lowercase)

- **In math/physics universally:** "change in." $\Delta F = F_\text{after} - F_\text{before}$.
- **Programmer intuition:** diff. `delta_E = E.after - E.before`.
- **Capital vs lowercase:** $\Delta$ is finite difference (a discrete change); $\delta$ is typically an infinitesimal or a small variation. In Still 2012 you'll only see capital $\Delta$.

### Σ — "SIG-mah" (capital sigma)

- **Universal math:** summation. $\sum_{t=0}^{\tau-1} f(t)$ means "add $f(0) + f(1) + \ldots + f(\tau-1)$."
- **Programmer intuition:** `for` loop with accumulator. `sum(f(t) for t in range(tau))`.

### Π — "PIE" (capital pi)

- **Universal math:** product. $\prod_{t=1}^\tau p_t$ means "multiply $p_1 \cdot p_2 \cdots p_\tau$."
- **Programmer intuition:** like `sum` but with multiplication. `math.prod(p[t] for t in range(1, tau+1))`.
- **Where it shows up in Still 2012:** Eq. 4 (probability of a path).

### Ω — "oh-MEG-ah" (capital omega)

- **In statistical mechanics:** the **number of microstates** consistent with a given macrostate — the *multiplicity*. Boltzmann's entropy formula: $S = k_B \ln \Omega$.
- **Programmer intuition:** the cardinality of the set of "distinguishable ways the system could currently be." A bit that "could be 0 or 1" has $\Omega = 2$; a bit forced to a single definite value has $\Omega = 1$.
- **Why Landauer cares:** erasing a bit collapses $\Omega$ from 2 to 1, which lowers the bit's entropy by $k_B \ln 2$. By the second law, that entropy decrease must show up as heat dumped to the environment: $k_B T \ln 2$ per bit. This is the entire derivation of Landauer's bound.
- **Convention warning:** $\Omega$ is also used for angular frequency, solid angle, and electrical resistance (ohms). Always check context.

---

## Other constants and notation

### $k_B$ — "kay-bee" or "kay sub bee" (Boltzmann constant)

- $k_B \approx 1.38 \times 10^{-23}$ J/K.
- **Programmer intuition:** the exchange rate between temperature (Kelvin) and energy (joules). $k_B T$ is the average energy of thermal noise at temperature $T$.

### $\langle \cdot \rangle$ — "expected value" / "average over"

- **Read as:** "expected value of …" or "average of …" or "mean of …"
- **Subscripted form:** $\langle W \rangle_P$ means "average W according to probability distribution P."
- **Programmer intuition:** `mean(samples)`, or `E[W]` in CS-style notation.

### $p(x)$, $p(x \mid y)$ — probability and conditional probability

- $p(x)$ — probability of outcome $x$.
- $p(x \mid y)$ — probability of $x$ *given* $y$. Read "if $y$ happened, how likely is $x$?"
- **Programmer intuition:** look-up tables. $p(x \mid y)$ is a 2D table indexed by $(x, y)$; $p(x)$ is the marginal — summed along the $y$ axis.

### $H[X]$ — "entropy of X" (Shannon entropy)

- $H[X] = -\langle \ln p(x) \rangle = -\sum_x p(x) \ln p(x)$.
- **What it measures:** uncertainty. Max when $X$ is uniform; zero when $X$ is deterministic.
- **Programmer intuition:** the average number of nats (or bits, if you use $\log_2$) needed to identify $X$. High $H[X]$ = "outcome would surprise you"; low $H[X]$ = "predictable."
- **Same quantity as thermodynamic entropy**, just in different units. This equivalence is the foundation of everything in zentropy. Sethna ch 5 makes this explicit.

### $H[X \mid Y]$ — conditional entropy

- Uncertainty about $X$ *after you know* $Y$.
- **Programmer intuition:** "if I already know Y, how surprising is X still?"

### $I[X ; Y]$ — "mutual information of X and Y"

- $I[X;Y] = H[X] - H[X \mid Y] = H[Y] - H[Y \mid X]$.
- **What it measures:** how much knowing $Y$ reduces uncertainty about $X$. Symmetric: $I[X;Y] = I[Y;X]$.
- **Programmer intuition:** correlation, but measured in bits/nats. Zero iff $X$ and $Y$ are independent. The information $X$ and $Y$ "share."

### $D_\text{KL}[p \,\Vert\, q]$ — "KL divergence of p from q" (Kullback-Leibler)

- $D_\text{KL}[p \,\Vert\, q] = \langle \ln(p/q) \rangle_p = \sum_x p(x) \ln(p(x)/q(x))$.
- Always $\ge 0$; equals 0 iff $p = q$.
- **What it measures:** how badly $q$ approximates $p$. **Asymmetric** — $D_\text{KL}[p \,\Vert\, q] \ne D_\text{KL}[q \,\Vert\, p]$.
- **Programmer intuition:** the extra cost, in nats, of encoding samples from $p$ using a code optimized for $q$. The bigger the divergence, the worse the mismatch.

---

## Key concepts

### Exergy — the textbook quantity

Maximum useful work extractable from a system as it equilibrates with a *specified reference environment*. Units: joules.

Distinct from Helmholtz free energy $F = U - TS$, which is calculated for a system alone given a temperature. Exergy explicitly accounts for what could be extracted via gradients between system and environment — sunlight reaching Earth, undiscovered oil, a Dyson swarm's stellar input. **Exergy is the strict superset of free energy.**

A schematic formula (system at $U, S, V$, composition $N_i$; reference at $T_0, p_0, \mu_i^0$):

$$B = U - U_0 - T_0(S - S_0) + p_0(V - V_0) - \sum_i \mu_i^0 (N_i - N_i^0)$$

- $U$, $S$, $V$, $N_i$ — system internal energy, entropy, volume, mole numbers of species $i$
- Subscript 0 — reference environment values
- $\mu_i^0$ — reference chemical potential of species $i$

Exergy is *observer-independent*. It is a property of (system, reference environment, physics) — not of who can extract it.

### Zenergy (N) — the zentropy-specific quantity

```
N(t) := exergy presently being harnessed by an agent or lineage at time t,
        within the forward light cone
```

Units: joules. Project nickname: **zenergy** (Brent's coinage). Paper term: **coupled exergy** or *accessible exergy*.

**Realized, not potential.** Zenergy is the *subset of exergy actively being processed* by the agent — not the total exergy theoretically reachable given capabilities. A Dyson sphere that *exists but sits idle* doesn't increase N; one that *processes stellar output* does. See `definitions.md` for full treatment including the "Life = ∆N ≥ 0" working claim and the realized-vs-potential reasoning.

### Decomposition of `k_B T ln 2` (the Landauer cost of one bit)

| Symbol | What it is | Value at $T \approx 300$ K |
|---|---|---|
| $k_B$ | Boltzmann's constant — exchange rate between K and J | $1.38 \times 10^{-23}$ J/K |
| $T$ | absolute temperature | $\sim 300$ K |
| $k_B T$ | average thermal energy per degree of freedom | $\sim 4.1 \times 10^{-21}$ J |
| $\ln 2$ | natural log of 2 — converts binary bits to nats | $0.693$ |
| $k_B T \ln 2$ | thermodynamic cost of one bit at temperature $T$ | $\sim 2.8 \times 10^{-21}$ J |

### Decomposition of `F = U - TS` (Helmholtz free energy)

| Symbol | What it is |
|---|---|
| $F$ | Helmholtz free energy — extractable work at fixed $T$, $V$ |
| $U$ | internal energy — *all* energy in the system |
| $T$ | absolute temperature |
| $S$ | entropy — same quantity as Shannon entropy in different units |
| $T \cdot S$ | thermal disorder energy locked up as entropy; not extractable |
| $U - T \cdot S$ | total minus locked-up = extractable |

---

## Key equations by paper

### Still, Sivak, Bell & Crooks (2012) — *Thermodynamics of Prediction*

Symbols used in this paper:

| Symbol | Meaning |
|---|---|
| $s_t$ | system state at time $t$ |
| $x_t$ | external driving signal at time $t$ |
| $E(s, x)$ | energy of the system when in state $s$ under signal $x$ |
| $W$ | total work done on the system over a protocol |
| $W_\text{diss}$ | dissipated work — work irretrievably lost (heat) |
| $W_\text{ex}$ | excess work — work above the quasistatic free-energy change |
| $Q$ | heat flowing into the system |
| $F$ | equilibrium free energy |
| $F_\text{neq}$ | nonequilibrium free energy |
| $F^\text{add}$ | the *additional* nonequilibrium contribution to free energy |
| $I_\text{mem}(t)$ | instantaneous memory: $I[s_t, x_t]$ |
| $I_\text{pred}(t)$ | instantaneous predictive power: $I[s_t, x_{t+1}]$ |
| $I_e$ | erased information: $H[s_0 \mid x_0] - H[s_\tau \mid x_\tau]$ |

---

#### Eq. 14 — the keystone

$$\beta \,\big\langle W_\text{diss}[x_t \to x_{t+1}] \big\rangle \;=\; I_\text{mem}(t) - I_\text{pred}(t)$$

**In English:** the dissipated work per work step, measured in thermal units, equals the *nonpredictive* information the system carries at that step — the bits it remembers about the past that don't help predict the next signal.

**Why this matters:** this is the bridge between thermodynamics and information theory. Energy waste and useless memory are the *same quantity*, scaled by temperature. Use whichever vocabulary is more convenient for the question at hand.

**Section:** *"Predictive power, memory, and dissipation,"* page 3 (the paragraph immediately before the equation labels it "our first result").

---

#### Eq. 18 — the total-dissipation bound

$$I_\text{mem} - I_\text{pred} \;\le\; \beta \langle W_\text{diss} \rangle \;\le\; \beta \langle W_\text{ex} \rangle$$

**In English:** summed over the whole protocol, the total nostalgia (cumulative nonpredictive information) is a *lower bound* on the total dissipated work, which in turn is bounded above by the total excess work.

**Why this matters:** turns Eq. 14's instantaneous equality into a usable inequality. You can audit any system's memory and get a guaranteed minimum on the energy it has wasted. The system *cannot* dissipate less than its nostalgia.

**Section:** *"Lower bound on total dissipation,"* page 4.

---

#### Eq. 21 — refined Landauer's principle

$$-\beta \langle Q \rangle \;\ge\; I_e + I_\text{mem} - I_\text{pred}$$

**In English:** the heat that has to flow *out* of the system is bounded below by the erased information *plus* the total nostalgia. Landauer's original result said heat ≥ bits erased; this strengthens it by adding the nonpredictive memory penalty.

**Why this matters:** a *predictive* system (low nostalgia) can approach Landauer's classical floor for computation. A *bad predictor* is forced to dissipate more heat for the same computation. **Predictive accuracy literally lowers the thermodynamic price of computation.** This is the closest thing in the paper to "compression saves you energy."

**Section:** *"Lower bound on total dissipation,"* page 4 (just after Eq. 19, the standard Landauer form).

---

*To extend: read the next paper (England 2013), add any new Greek letters or notation here, then add a new "Key equations" subsection below this one.*
