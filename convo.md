Now the reading list.

  The path from "smart engineer who's done calculus" to "can read England/Friston/Still critically and contribute a convergence proof" goes through six layers. Each is a dependency
  for the next; skipping makes the later ones opaque.

  1. Information theory — the absolute foundation, everything downstream uses it
  - MacKay, Information Theory, Inference, and Learning Algorithms — free PDF at inference.org.uk/itila. Chapters 1–12. ~250 pages of actual reading.
  - Friendlier than Cover & Thomas (the canonical textbook) for someone coming from CS. MacKay actually teaches; Cover & Thomas references.
  - Delivers: Shannon entropy, mutual information, KL divergence, source coding theorems. Without this, every paper downstream is decoration around symbols you don't have.
  - Honest time estimate at evening cycles: 6–10 weeks. Don't skim — this is where defensibility starts.

  2. Statistical mechanics — just enough to read non-equilibrium papers
  - Sethna, Statistical Mechanics: Entropy, Order Parameters, and Complexity — free PDF at sethna.lassp.cornell.edu. Chapters 1–6.
  - Delivers: partition functions, free energy F = −kT ln Z, ensembles, the physics meaning of "entropy" (which you'll then realize is the same quantity as Shannon's, in the right
  units — Sethna makes this explicit, and it's the key insight that makes everything below click).
  - Time: 4–8 weeks.

  3. The information–thermodynamics bridge — where compression and joules formally meet
  - Parrondo, Horowitz & Sagawa, "Thermodynamics of information" (Nature Physics 11, 131, 2015). ~12 pages, review.
  - Bennett, "The thermodynamics of computation—a review" (Int. J. Theor. Phys. 21, 905, 1982). Classic, still readable.
  - Delivers: Landauer's principle (erasing one bit costs kT ln 2), Maxwell's demon resolved, Sagawa-Ueda feedback-control extension. After this, "information is thermodynamic" stops
  being a slogan in your head.
  - Time: 2–4 weeks, if layers 1 and 2 stuck.

  4. Stochastic thermodynamics — England's home turf
  - Seifert, "Stochastic thermodynamics, fluctuation theorems and molecular machines" (Rep. Prog. Phys. 75, 126001, 2012). ~60 pages, dense, but standard.
  - Crooks fluctuation theorem (Phys. Rev. E 60, 2721, 1999) and Jarzynski equality (Phys. Rev. Lett. 78, 2690, 1997) — short foundational papers.
  - Delivers: fluctuation theorems, non-equilibrium free-energy reconstruction. England's results sit directly on this.
  - Time: 4–6 weeks.

  5. The keystone — where your paper begins
  - Still, Sivak, Bell & Crooks, "Thermodynamics of Prediction" (PRL 109, 120604, 2012). Four pages. Read it five times across the curriculum.
  - Still, "Thermodynamic cost and benefit of memory" (PRL 124, 050601, 2020). Follow-up.
  - If your convergence hypothesis is right, this is the result you're generalizing.

  6. The targets
  - England, "Statistical physics of self-replication" (J. Chem. Phys. 139, 121923, 2013) — dissipative adaptation.
  - England, "Dissipative adaptation in driven self-assembly" (Nat. Nanotechnol. 10, 919, 2015).
  - Friston via Seth: "The free-energy principle: a unified brain theory?" (Nat. Rev. Neurosci. 11, 127, 2010), then Anil Seth's primer papers. Friston's direct prose is famously
  hard; Seth is the on-ramp.
  - Schmidhuber, "Formal theory of creativity, fun, and intrinsic motivation" (IEEE TAMD 2, 230, 2010) — compression progress as the fitness signal in his framework.

  Scoped out of the critical path (interesting, not required for the convergence paper):
  - Algorithmic information theory (Li & Vitányi, Hutter) — comes back if the paper expands.
  - Constructor theory (Deutsch/Marletto), assembly theory (Walker/Cronin) — citation-not-mastery for now.

  If you do only one thing this month: Start MacKay chapter 1. Information theory is the single most leveraged investment. Every other layer assumes it.

  Honest expectation. This is roughly 6–12 months of evening reading at the cycle budget we've named. That sounds long, but it's a quarter to a year of foundation for a paper that's
  meant to be defensible against people who've spent careers on this. The alternative — write fast, hope reviewers are gentle — is exactly the failure mode that Grok-LaTeX prefigured.
   Better to take a year and submit something that holds up than to ship in three months and watch it fall apart in review.
                                                    
--- 

PRL = Physical Review Letters. Published by the American Physical Society. Short-form (~4 pages, occasionally with a long supplement), high prestige — where the most influential
  short results in stat mech and non-equilibrium thermodynamics land. The Still 2012 paper lives there; so does most of the foundational Crooks/Jarzynski/Sagawa work. You'll also
  encounter PRE (Physical Review E — longer-form stat mech), PRX (open-access flagship), Nature Physics, J. Stat. Mech., and J. Chem. Phys. (where the England replication paper
  lives). Knowing venues becomes useful once you're corresponding with people who publish in them.

  On the learning style. This changes the plan meaningfully. The textbook-first sequence I just laid out is depth-first foundation-laying — right for someone with no scaffolding,
  wrong for someone who has 20 years of intuition for the actual papers in question. For you the inverse approach is correct: read the keystone papers first with full permission to be
   confused, mark every gap, then back-fill only the foundation pieces you actually need. The 6–12 month estimate compresses meaningfully when the back-filling is targeted rather than
   comprehensive.

---

 The breadth-first descent plan.

  Round 1 — read these three papers, in this order, with explicit permission to be confused. Don't try to follow every line. Mark every place you hit a wall.

  1. Still, Sivak, Bell & Crooks (2012), "Thermodynamics of Prediction" — PRL 109, 120604. Four pages. This is the joint. Read it first because everything else lives on one side or
  the other of it.
  2. England (2013), "Statistical physics of self-replication" — J. Chem. Phys. 139, 121923. The ∆N side. Read with the Still framing already in your head.
  3. Friston (2013), "Life as we know it" — J. R. Soc. Interface 10, 20130475. The free-energy / compression side. Friston's most accessible-ish paper for the physics question; better
   starting point than the brain-focused work.

  (For Friston, if "Life as we know it" doesn't land, fall back to Anil Seth's primers — "The free energy principle made simpler but not too simple" circa 2023 is the cleanest entry.)

  Round 2 — based on which gaps blocked you, we pick targeted back-fill. I can predict the most likely walls without knowing which ones will actually hit you:

  ┌──────────────────────────────────────────────────────────────────────────────────┬─────────────────────────────────────────────────────────────────────────────────┐
  │                                   Likely block                                   │                               Targeted back-fill                                │
  ├──────────────────────────────────────────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────────┤
  │ KL divergence / mutual info used as physical quantities                          │ MacKay chs 1–2 + Parrondo/Horowitz/Sagawa review                                │
  ├──────────────────────────────────────────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────────┤
  │ Crooks fluctuation theorem invoked without derivation                            │ Seifert's 2012 review §2–4, then Crooks 1999                                    │
  ├──────────────────────────────────────────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────────┤
  │ "Variational free energy" vs "Helmholtz free energy" — same word, different math │ Sethna ch 6 (statistical ensembles) + a Friston primer on variational inference │
  ├──────────────────────────────────────────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────────┤
  │ Stochastic trajectory / path-integral framing                                    │ Seifert's review §3                                                             │
  ├──────────────────────────────────────────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────────┤
  │ Self-information / surprisal as a physical cost                                  │ Parrondo et al. + Landauer/Bennett                                              │
  └──────────────────────────────────────────────────────────────────────────────────┴─────────────────────────────────────────────────────────────────────────────────┘

  You'll probably hit two or three of these in earnest, not all of them. We'll know after Round 1.

  Round 3 — re-read Still + England + Friston with the back-fill in place. If they read cleanly, the descent is done and the draft phase begins. If new gaps emerge, that's Round 4.

  Operational schedule given the "before I die" framing.

  - Descent phase: ~6–18 months of evening reading, depending on how many back-fill rounds. Could be faster given existing intuition.
  - Draft phase: 2–4 months. Convergence paper in draft.
  - Iteration / outreach phase: open-ended. Email England, Friston, Still, Kauffman; co-author if anyone bites; revise.

  The "publication > priority" stance simplifies a lot: you can email Still now with the convergence hypothesis, before you've finished reading her paper. The worst case is she says
  "yes I already showed that in section IV" — which saves you a year of work. The best case is she says "interesting, want to write it together?"

  Concrete next move. Pull down Still, Sivak, Bell & Crooks 2012. Read it once. Tell me — specifically — which sentences you bounced off. We descend from there.
                                                      
---

What Still 2012 actually proves. A specific information-thermodynamic identity:

  ▎ For any memory-bearing system driven out of equilibrium, the dissipated work is bounded below by kT × I_nonpred, where I_nonpred is the information the memory retains about the
  ▎ past that does not predict the future.

  That is: non-predictive memory is thermodynamically expensive. Equivalently, the optimally efficient predictor stores only the past statistics useful for predicting the future.
  Beautiful, tight, narrow.

  What Still does not do:
  - She says nothing about selection. Her result applies to any memory system — a thermostat as much as a cell. Why such systems arise is out of scope.
  - She says nothing about replication. The fitness side of zentropy is absent. 
  - She makes no claim about substrate-agnosticism in the sense of "this is the value function for all of life." Her paper is a stat-mech identity, not a theory of life.

  So the structure of your bridge is:

  [selection: England 2013] + [info-thermo bound: Still 2012] → [zentropy convergence: not yet written]

  Still proved the bound. England proved that selection in non-equilibrium environments biases trajectories toward more dissipative structures. The synthesis — that selection +
  Still's bound implies replicators converge toward optimal predictors of their environment, in a substrate-independent way that is THE value function — is what's missing. That's the
  paper.

  On the "no headlines" instinct. Reasonable check, and the answer has three parts:

  1. Friston already made the headlines for a structurally similar grand claim — that all living systems minimize variational free energy. So in one sense "universal value function
  for life" has had its press cycle. Before Friston, Schrödinger's What Is Life? (1944) made the same kind of claim with negentropy. You're not first to the slogan.
  2. Friston's version is contested. Stat-mech-trained skeptics, parts of his own collaborator network (Andy Clark and others), and the philosophy-of-science crowd argue the universal
   claim outruns the proof — that variational free energy is not the same quantity as physical free energy, and that the framework's near-unfalsifiability is doing work the math
  should be doing. So the headlines came; the field has spent a decade arguing about whether they were warranted; the dust is not settled.
  3. The clean thermodynamic synthesis hasn't been done. The most ambitious recent attempts — Parr, Da Costa & Friston, "Markov blankets, information geometry and stochastic
  thermodynamics" (2020), and Ramstead et al., "Bayesian Mechanics for Stationary Processes" (2021) — explicitly try to ground FEP in stochastic thermodynamics. They're partial,
  technical, contested, not consensus. The fields are still fragmented: England in stat mech / biophysics; Friston in neuroscience / inference; Still in info-thermo; Schmidhuber in
  AI. They cite each other lightly. They do not synthesize.

  So the right framing is: zentropy is not "first to claim a universal principle" — that ship sailed long ago. Zentropy's potential contribution is tightening the proof by anchoring
  it in stochastic thermodynamics, with Still's bound as the keystone and England's selection mechanism as the engine. That is publishable, and it would attract attention from
  Friston/England circles, because it's exactly what their fields have failed to converge on. A paper headlined "FEP and dissipative adaptation are the same principle, here is the
  proof via Still 2012" would be read.

  Honest caveat I owe you under no-sycophancy rules. There is a real chance that when you attempt the convergence proof, it doesn't cleanly work. The pieces might converge only under
  restrictive assumptions; substrate-agnosticism might hold for some substrates and not others; Still's bound might generalize asymptotically but not at finite horizons. The honest
  expected outcome is not "we prove convergence." It is "we map where convergence holds and where it breaks, and the map itself is the contribution." That's still a real paper — just
  a humbler one than the slogan promises.

  The Parr/Da Costa and Ramstead papers should join Round 2 of your reading queue when you get there — they're the current state of the art for the synthesis you're attempting.
                                                                 
---

● Paper is downloaded and verified: papers/still-2012-thermodynamics-of-prediction.pdf. Five pages including refs, the arXiv v3 (October 2012), matches the published PRL.

  One correction I owe you while we're here — under the no-sycophancy rules. I said earlier "Still says nothing about selection." Not quite right. Her Discussion section explicitly
  raises it:

  ▎ "biological systems are typically adapted to their environment. One can then ask if there is a simple principle underlying the process producing this adaptation. If such a
  ▎ principle exists, then it may reflect the importance of energetic efficiency, because of the resulting competitive advantage for reproducing organisms."

  She gestures at the question, then leaves it open. The formal apparatus stops at the dissipation ↔ nonpredictive-information equivalence; the selection-producing-this step is
  invited but not derived. So the honest version of my claim is: she doesn't formalize selection, but she explicitly hands it off as the next problem. That makes the zentropy
  convergence paper a more natural extension than I implied — Still is already pointing at it in her own conclusion. If she's still active and approachable, this paragraph is your
  conversational opening when you email her.

  Three equations to anchor your read:

  - Eq. 14: β⟨W_diss[xt → xt+1]⟩ = I_mem(t) − I_pred(t). The single keystone equation. Dissipation per work step equals nonpredictive information. If you internalize one thing from
  this paper, this is it.
  - Eq. 18: I_mem − I_pred ≤ β⟨W_diss⟩ ≤ β⟨W_ex⟩. Total nostalgia is a lower bound on total dissipation.
  - Eq. 21: refined Landauer — −β⟨Q⟩ ≥ I_e + I_mem − I_pred. Landauer's bound augmented by total nostalgia.

  What to do. Read it once at intuition level — don't try to follow every step. Mark the specific sentences or equations where you bounce off. When you come back, we descend on those
  gaps, not on the rest. The Discussion section is the part most directly relevant to zentropy; the math sections (problem setup → Eqs. 1–13) are foundation you'll likely back-fill
  from Sethna and Seifert later.

---

notation.md at the repo root. Three sections:

  1. Greek letters — β, τ, Δ, Σ, Π with pronunciations + meanings + programmer intuitions + convention warnings ("β means something different in statistics")
  2. Other constants and notation — k_B, ⟨·⟩, p(x|y), H[X], I[X;Y], D_KL — the universal toolkit you'll see in every paper downstream
  3. Key equations by paper — Still 2012 section seeded with the symbol table for that paper plus Eqs. 14, 18, and 21 with English translations

  To render: open in PyCharm and toggle the Markdown preview pane (View → Tool Windows → Markdown, or the eye icon top-right of the editor). KaTeX renders inline.

  Designed to grow. When you read England next, the workflow is:
  - Note any Greek letter or notation that appears and isn't in the glossary yet → add to Greek letters or Other constants and notation
  - Note the central equations of the paper → add a new subsection under Key equations by paper 

  This way the file accumulates real fluency as you read, instead of having to look symbols up every time. The first time you see ξ ("ksai") or κ ("KAP-pah") in England's paper, you
  add them; the second time, they're already there.

  One honest flag. I wrote the "English translations" of Still's equations from my reading of the paper. When you read it yourself and decide those translations don't quite match what
   you understand the equations to say, change them. The translations should be yours, not mine — same logic as the Grok-LaTeX caution. My version is a starting draft, not the
  canonical reading.

---

https://www.wired.com/story/karl-friston-free-energy-principle-artificial-intelligence/

---

"information is energy" is the single most important conceptual unlock for everything downstream. Let me sketch the intuition before pointing at the paper, because the
  intuition is what unlocks the math.

  The core insight. Information has thermodynamic value, measured in joules. The exchange rate is k_B T. Two equivalent ways to see it:

  - Operational (Szilard 1929): knowing the state of a system gives you extractable work. If a gas molecule is in a box and you know which half it's on, you can place a piston on the
  empty side and let the molecule push it — extracting k_B T ln 2 of usable work. Without that knowledge, you can't. Information ≈ free energy.
  - Erasure (Landauer 1961): forgetting costs you at least the work you could have extracted. Resetting a bit from "0 or 1" to "definitely 0" reduces phase-space volume by half — and
  by the second law, that compression must be paid for in heat dumped to the environment: at least k_B T ln 2 joules per bit erased. Computing is thermodynamically cheap in principle,
   but forgetting is not.

  That's the canonical bridge between bits and joules. The reason β appears in Still 2012's Eq 14 is exactly this exchange rate at work — β ⟨W_diss⟩ and I_mem − I_pred are literally
  the same physical quantity once you accept this conversion.

  What to read. The right foundational paper is not Landauer 1961 (terse, dated, hard to find legally). It's:

  ▎ Charles H. Bennett (2003), "Notes on Landauer's principle, reversible computation, and Maxwell's demon," Studies in History and Philosophy of Modern Physics 34, 501–510. Preprint:
  ▎  arXiv:physics/0210005.

  Bennett is the person who consolidated Landauer's principle in 1982 and connected it formally to Maxwell's demon. This 2003 paper is his accessible, mature restatement — covers
  Maxwell's demon, Szilard, Landauer, reversible computation, all in one short paper. Physicists hand this to people who ask exactly the question you just asked.

---

Bennett 2003, physics/0210005v2. Saved to papers/bennett-2003-landauer-and-maxwells-demon.pdf. Seven pages, very readable abstract — exactly the right text.

  Where this slots into your sequence. This is back-fill for Still 2012, not a Round 1 paper in its own right. Read it when you hit Still's Eq. 21 (the refined Landauer) and want to
  know what the original Landauer bound says before Still strengthens it. Concrete suggestion:

  1. First pass through Still 2012 (full permission to be confused, mark walls)
  2. When Eq. 21 doesn't quite click — and "Landauer's principle" appears as a thing you're supposed to already know — pause and read Bennett 2003. It's short.
  3. Then re-read Still §"Lower bound on total dissipation" (p. 4). Eq. 21 should now read: "Landauer's classical bound, augmented by the system's nostalgia."

  That's the moment "information is energy" stops being a slogan and becomes a tool you can compute with.

---

❯ I need to actually read the papers to understand more, but my sense is to 1. keep the overarching goal as guide posts - we're trying to go backwards from my intuition into formal
  theory, 2. start in the reverse direction, building bottom up an being defensible. Baby steps. My question for you though: if I start with Still, am I re-inventing FEP? or building
   the missing foundation for it? Or is zentropy as a whole a parallel construct to FEP
  
● Honest answer: (3) parallel construct, currently — with strong potential to become (2), FEP's missing thermodynamic foundation, if your convergence proof works. Definitely not (1).

  Why not "reinventing FEP."

  FEP and zentropy make structurally similar claims ("one quantity governs life across substrates"), but the machinery is genuinely different:

  - FEP uses variational free energy — a Bayesian / information-theoretic quantity from variational inference. It asserts that systems with Markov blankets minimize F. It does not
  formalize the selection mechanism; it just claims surviving systems will appear to do this.
  - Zentropy uses physical free energy — thermodynamic dissipation. England's dissipative adaptation specifies why such systems arise: non-equilibrium dynamics statistically biases
  trajectories toward dissipators.

  FEP's "variational free energy" is mathematically not physical free energy. They share a name and a structure, but they live in different equations. Bridging them is exactly what
  Parr/Da Costa 2020 and Ramstead 2021 are trying to do, and they haven't fully succeeded.

  Why "FEP's missing foundation" is the live possibility.

  One of FEP's central critiques is that it postulates variational-free-energy minimization without grounding it in physics. Friston's defenders have historically argued some version
  of "minimizing F is just what living systems do, by definition" — which critics find circular.

  If your convergence proof works, it shows something cleaner: that physical selection (England) plus Still's identity together imply that surviving trajectories look like they
  minimize a variational-free-energy-ish quantity. FEP-like behavior falls out of physics rather than being postulated as a meta-principle. That's the floor FEP currently lacks.

  Why "parallel" is still the most accurate single word.

  Zentropy covers something FEP doesn't — explicit selection, via England. FEP is silent on why Markov-blanketed systems exist; zentropy supplies the dissipative-adaptation answer. So
   zentropy isn't merely FEP's missing foundation; it's a broader framework that contains FEP-like behavior as a derivable consequence, plus the selection mechanism FEP punts on.

  For your bottom-up strategy specifically.

  Starting with Still is exactly right. You're not reinventing FEP — you're building a floor it doesn't have. Each step is defensible on its own merits and the FEP-like results emerge
   naturally at the end. That's a stronger position to publish from than "I'm extending Friston" — and a stronger position to defend than "I'm competing with Friston."

  The risk you should know about, under no-sycophancy rules: when you read Friston deeply, you may find his framework already implicitly does what you're deriving. That's the failure
  mode previous Claude flagged. The guard against it is exactly what you proposed — read bottom-up, defend each step, position relative to FEP at the end. If you're walking on
  rigorous ground, the answer to "did Friston already do this?" becomes a citation, not a refutation.

  If this framing sits right with you, I'll lock it into memory as the working strategic position so future Claudes don't re-derive it.
                                
---

❯ so england's work was also derived/proven? derivation was shannon and proof was... simulation? of e-coli? what are we talking here? parameteric? or super-computer-running-genome
  stuff
  
● Good question — clarifies what the work actually looks like. Let me unpack what "proof" means in this lineage, because it's not what most engineers expect.

  England 2013's proof structure (and the field's pattern):

  1. Derivation — pure mathematics from Crooks fluctuation theorem (1999). Starting from microscopic reversibility, derive a thermodynamic lower bound on heat production for
  self-replication: heat-produced ≥ kT × f(growth rate, internal entropy, durability). This is math, not simulation. No supercomputers, no genomes, no simulated cells. Symbol
  manipulation from first principles.
  2. Empirical sanity check — plug measured biological parameters into the derived bound and verify real systems satisfy it. England did this with E. coli using published numbers:
  measured growth rate, estimated internal entropy from bond counting, durability from lifetime data, heat production from calorimetry. Result: E. coli's measured heat output is
  within ~2-3× of the theoretical lower bound. Parametric, not simulation. A spreadsheet, not a supercomputer.
  3. Toy model (in the Perunov-Marsland-England paper) — small illustrative simulation: one particle hopping in a driven energy landscape (Figs 3–4). Tiny code, runs on a laptop,
  exists to illustrate the math rather than prove anything new.

  One correction to your guess: the derivation root isn't Shannon directly. England's lineage is Crooks fluctuation theorem → Jarzynski's work relation → non-equilibrium stat mech.
  Shannon enters more on Still's side — she explicitly composes Shannon-style information theory with Crooks-style stochastic thermo. Still is the Shannon-meets-Crooks bridge; England
   is mostly Crooks-meets-self-replication.

  What this means for the convergence proof:

  Your "proof" will have the same structure:
  - Derivation (the bulk): compose Still's bound with Perunov-Marsland-England's Eq. 8, restrict to constrained regime, derive the result. Symbol manipulation. Doable with paper, pen,
   and time. No supercomputers needed.
  - Toy model: probably a simple simulated replicator with explicit I_mem / I_pred state, run on a laptop, illustrating that better predictors win in the constrained regime.
  Code-engineer skill set; you have this.
  - Empirical sanity checks: plug in measured numbers from biology (aerobic vs anaerobic metabolic efficiency, brain energy budgets, phase-transition ∆N magnitudes) or civilizational
  scale (Smil's GDP-in-joules data) and verify the framework's predictions are consistent with known orders of magnitude. Spreadsheet work, not lab work.
  
  No genome-scale simulations. No wet lab. No supercomputers. This is theoretical physics in its most economical form — the entire research infrastructure fits in a laptop, a
  notebook, and library access to a half-dozen papers. The bottleneck is understanding, not compute. Which is exactly why a database engineer with reading time can plausibly do it.

  The economy of the field is one of the things that makes this niche genuinely accessible. England 2013 was a single-author paper. Still 2012 was four authors but is fundamentally
  one derivation. Your convergence proof could be one or two authors, written over a year of evenings.

---

❯ almost... a few more questions: I'm in fort collins. I know they are into biology at CSU. Do they have a program that touches these domains? Might there be someone I could contact
  here? Might I find my Boltzman in one of the undergrads with strong formalism but lacking the intuition? 
  
● Honest uncertainty up front: I don't have confident knowledge of specific CSU faculty working at the Still/England intersection, and I shouldn't fake it. Academic personnel data is
  exactly the place my training-data familiarity is unreliable. But I can tell you what to look for and where.

  CSU departments worth checking (in rough order of likelihood):

  1. Physics — biophysics group, soft matter, non-equilibrium / statistical mechanics. CSU has had a physics department doing this kind of work for years; faculty pages will list
  research interests.
  2. Applied Mathematics — stochastic processes, dynamical systems. Closer to the formal-math side you need.
  3. Biology — theoretical/evolutionary biology faculty. Less likely to know stochastic thermo but might know the biological literature deeply.
  4. Computer Science — computational biology, information theory applied to biological systems.
  5. CSU Energy Institute — if it exists in current form, biophysical / EROI-adjacent work happens there.

  Search strategies:

  - Google Scholar: "non-equilibrium thermodynamics" OR "stochastic thermodynamics" OR "predictive coding" + Colorado State
  - Department faculty directories: scan everyone's stated research interests; look for words like information theory of biology, dissipative, active matter, biophysics of replication
  - arXiv search: sort by recent papers with author affiliation "Colorado State University" in the cond-mat.stat-mech, physics.bio-ph, q-bio.PE categories
  - CSU thesis archives: graduate dissertations are a strong signal of "this department actually does this kind of work" — search for "non-equilibrium" or "stochastic thermodynamics"
  theses in physics

  Geographic note worth knowing: CU Boulder is much denser for this work than CSU — ~1.5 hours from Fort Collins. CU has:
  - A larger physics / biophysics community
  - Santa Fe Institute affiliations (Doyne Farmer, Geoffrey West network has touched Boulder)
  - JILA (joint NIST/CU institute) does biophysics
  - Complex-systems / non-equilibrium thermo presence

  If you find no one at CSU, CU Boulder is the next-closest option — and SFI itself (Santa Fe, ~6 hours) is the spiritual home of this kind of cross-domain synthesis. SFI explicitly
  funds outsider/non-traditional researchers; they have programs for exactly the demographic you fit.

  On the Boltzmann-in-an-undergrad idea:

  This is actually a really sharp instinct, and I'd weight it as at least as promising as finding a faculty member. Here's why:

  - A senior physics or applied math undergrad who's taken stochastic thermo and information theory has the formalism fluency you lack, and probably zero original research direction
  of their own
  - An MS student or first/second-year PhD student looking for a side project is similar — strong math, looking for problems
  - Faculty are busy and rarely take on outsider collaborations; students have time and need real problems for their CV

  How to approach without scaring them off:

  Don't lead with "I have a unified theory of life." Lead with the specific narrow technical problem:

  ▎ "I'm working on a paper attempting to compose Susanne Still's 2012 PRL bound with England's dissipative-adaptation framework in the constrained regime. I need someone who can
  ▎ audit my math as I go — I have the intuition and the literature mapped out, but I want a math-fluent collaborator. Paid hourly, or co-authorship on the resulting paper. The work
  ▎ is concrete: read [3 specific papers], help me work through [3 specific equations], audit the derivation that connects them. Maybe 5-10 hours a week over 3-6 months."

  That's a specific, bounded, paid-or-co-authored proposition. Strong students will engage with that; cranks won't (the literature/math entry bar filters them out).

  Where to post it:

  - CSU physics department's grad student / tutoring board
  - A targeted email to one or two professors asking "do you have a student who might be interested in a side collaboration like this?" — professors love sending their students to
  paid side projects
  - r/Physics, r/AskPhysics with a careful subject line ("looking for paid collaborator: synthesis of Still 2012 and England 2013 in non-equilibrium stat mech")
  - The Santa Fe Institute's mailing lists / community
  - Twitter / X if you still have @hobesgoblin — physics-ML twitter is small and well-connected

  Realistic timeline for finding a Boltzmann-undergrad: 1–3 months of casting. Not nothing, but bounded.

  Worth doing in parallel with the reading. The right collaborator at the right moment could compress your 12-month timeline to 6.
                                                          
---

  - Zentropy isn't ready for external disclosure yet — Still reading isn't done, the formal arguments aren't there, the prior-art audit (Walker & Davies / Smith / Vanchurin-Koonin)
  hasn't happened. A cold-email zentropy pitch lands as half-baked, and you don't get a second chance at the first impression.
  - The technical contribution (first open-source reimpl + the partial Fig S8 reproduction + the catch/snap question) IS publishable substance on its own. That establishes you as a
  serious physics implementer first. Zentropy can come later, after the relationship is established and after the framework has more rigor.
  - It preserves optionality — if he turns out to be uninterested in foundations work, you've still got a useful technical contact. If he turns out to be interested, you've earned the
   right to bring it up by demonstrating competence.

  Suggested tight email scope (your draft, not mine to write):
  1. "We did what appears to be the first open-source reimpl of your 2017 sim — github link"
  2. "Fig 2(a) and the catch curve of Fig S8 reproduce faithfully at the supp's stated parameters under ensemble averaging"
  3. "We're partially reproducing snap but couldn't quite get the sharp zero at ω_d / the tight bell at ω ≈ 3.7. Did you record the snap β value? The supp notes the parameters as 'not
   finely sensitive' but we're seeing meaningful sensitivity."
  4. "Also curious if anyone has followed up on (a) why the snap distribution is more peaked than the undriven baseline and (b) the inverse correlation between catch's peak position
  (at ω_d) and snap's (well away from ω_d) — both observations are striking but undeveloped in the supp."

---

❯ make a note, we'll pursue 1 next. But I want to ask you: if we had the reversable VM, would kachman's work stand as a bunch of op-codes adjacent in a bath? i.e. these 3 are next to
   each other, they encode SLEEP x, PREDICT, GOTO 1. These other ones encode SLEEP y, PREDICT, GOTO 1. These other ones encode: SLEEP z, PREDICT, SET i = 0, CPY self[i] -> child[i];
  CND_JMP if i > z; goto 4, else goto 0?
  
● This is a real bridge, and it lights up something you'd already designed but we pivoted away from.

  The mapping is structurally clean:

  ┌─────────────────────────────┬───────────────────────────────────────────────────────────────────────────────────────────────────┐
  │           Kachman           │                                           Reversible VM                                           │
  ├─────────────────────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ N particles in a bath       │ N op-code carriers (tokens) in a bath                                                             │
  ├─────────────────────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ Bond between i,j            │ Adjacency / execution link between op-codes                                                       │
  ├─────────────────────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ Adjacency matrix A          │ The current "program" structure                                                                   │
  ├─────────────────────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ Drive F·sin(ω_d·t)          │ Clock / external work source the program runs against                                             │
  ├─────────────────────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ Catch bonds resonate at ω_d │ Programs containing PREDICT, GOTO loop on the drive period — they "persist" by being in sync      │
  ├─────────────────────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ Snap bonds avoid ω_d        │ Programs that AVOID running the predict loop at drive frequency (anti-resonance = anti-execution) │
  ├─────────────────────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ Storage / reproduction      │ Programs that include CPY/COND_JMP — i.e., replicator op-codes                                    │
  ├─────────────────────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ Bond stability under drive  │ Programs that don't get rewritten by thermal noise during execution                               │
  └─────────────────────────────┴───────────────────────────────────────────────────────────────────────────────────────────────────┘

  Your three program-classes map cleanly:
  - SLEEP x; PREDICT; GOTO 1 = catch bond cluster at ω that matches x's period — pure tracking, no replication
  - SLEEP y; PREDICT; GOTO 1 = same shape, different tuning (different bond cluster, different resonance)
  - The third with CPY self[i] -> child[i]; CND_JMP i > z; ... = replicator (Phase 3 territory)

  This is essentially your old opcode-tape design from [[project-sim-england-state]] — which we pivoted away from for "bottom-up purity" (not presupposing replicators). But your
  question reveals the move was partly an artifact of the framing: the opcode-tape substrate isn't presupposing replicators if you just don't include CPY in the initial op-code set.
  It's substrate-agnostic, and more expressive than bonds for testing different kinds of programs (predictors, avoidance-only, replicators, mixed).

  Why this matters for what we just learned about Kachman's substrate:

  We've been finding that Kachman's bonds may be too coarse to test I_pred (slow dynamics, limited per-mode resolution). A reversible-VM opcode-tape substrate might be cleaner:
  - More expressive program space than bond topology
  - Cleaner reading of "what is this program doing" (op-codes are discrete and labeled)
  - CPY can be added as one extra op-code, not a whole new sim tier
  - I_pred is well-defined on the program-state trajectory directly

  Honest caveat: the analogy is structural, not dynamical. Bonds have specific oscillator-mode physics; op-code execution has different dynamics. Whether the same Still-bound / W_diss
   ≥ kT(I_mem − I_pred) form applies identically across both substrates needs care — they probably share the bound (it's substrate-agnostic) but not the constants.

--- 

❯ if it was op codes floating around... where would the instruction pointer live? What about RNA as a model for the correct simulation layer? there's opcode chains floating around
  and executor enzymes that attach and run them?
  
● You just spotted the missing piece. Free op-codes in a bath have no execution mechanism — without an instruction pointer, they're just symbols, not a running computation. And nature
   solved this problem with ribosomes.

  The RNA-ribosome model:
  - RNA strand = op-code chain (codons = op-codes; sequence is fixed at synthesis)
  - Ribosome = the executor — physical agent that binds an RNA strand and walks codon-by-codon. The ribosome IS the instruction pointer made spatial.
  - tRNAs / amino acids = "data" delivered per op-code execution
  - NTPs / metabolic gradient = the energy drive
  - Ribozymes = strands that, when executed, catalyze their own copying — i.e., op-code chains that include CPY operations

  This solves several problems at once:
  - IP lives in the ribosome (no abstract "where am I" problem)
  - Strands are sequences in real space (adjacency is physical, like Kachman)
  - Energy input has a natural channel (NTP hydrolysis = the drive)
  - Replication is a specific op-code sequence, not a sim-level cheat
  - Selection acts on which strand-ribosome combinations persist

  Why this is the right abstraction layer for zentropy:

  It sits cleanly between Kachman (sub-life: stable structures with no execution) and DNA-protein (full-life: encoded programs with separate transcription/translation). The RNA-world
  layer is exactly the threshold M* candidate — before ribosomes, RNA strands degrade and "rediscovery" of useful sequences is M·kT-expensive per generation; after ribosome emergence,
   the same strand can be copied cheaply by the executor. The replication-machinery cost K from spine §6 IS the ribosome.

  Maps to existing predictions:
  - PREDICTION 2 (I_pred): RNA strand sequences are a richer state space than bond topology — easier to detect "the strand encodes the drive structure" via mutual information
  - PREDICTION 3 (storage / abiogenesis): ribozyme emergence IS the storage-channel-opens transition. M* in this substrate is the environmental-complexity threshold where ribozymes
  become favored
  - PREDICTION 1.5 (competitive selection): different strand types competing for ribosomes (or for nucleotides) is naturally a finite-resource competition

  Honest caveats:

  - This is an existing research area. RNA-world simulations have been done extensively (Eigen hypercycles, Szostak's group, more recently Walker / Cronin assembly theory). Before
  committing to building this, we'd want a serious prior-art audit — what's already been simulated, what's been measured, what zentropy specifically adds.
  - Implementation cost is substantial vs Kachman's bonds. Probably 500-1000 lines for a minimum-viable RNA-ribosome sim with selection.
  - It might be over-committing — we got real value from Kachman as a SIMPLE substrate where every piece is tractable. RNA-world might be too rich, where many phenomena compete and
  isolating the zentropy claim becomes harder.
