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
