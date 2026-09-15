# Review

## Learning Objectives
- Run a design critique with I like / I wish / What if without turning it into a status meeting.
- Map assumptions and run a riskiest-assumption test or a pre-mortem before more build.
- Steelman a weak take and separate user testing (task success) from stakeholder and expert review.
- Choose redesign, solidify, kill, pivot, or ship as a named decision — not a mood.

## Prerequisites
- Lessons 1–5: you have a loop, a brief, and some kind of prototype or increment to look at.
- You can tolerate being wrong in public for twenty minutes.

## Lesson Content

### Critique is not a roasting and not a round of applause
A **design critique** is a structured look at an artifact against the brief. The artifact is on trial, not the author. **I like / I wish / What if** is a simple protocol that keeps the room in useful speech: appreciation that is specific, a desired change, an experiment. Ban “I don’t like it” without a brief-linked reason. Ban silent senior people who later veto in a hallway.

Time-box. One facilitator. The author listens first, then answers questions, then decides what to change. A critique that becomes a live redesign by committee is a second brainstorm without deferred judgment.

If there is no brief (Lesson 3), cancel the critique. People will critique their imaginary product.

### Assumption mapping and the riskiest assumption test
**Assumption mapping** puts claims on two axes: how much you know, and how bad it is if you are wrong. The upper-right (unknown, fatal) is where Lesson 5’s tests live.

A **riskiest assumption test (RAT)** is that test, named as a review gate: we do not spend the next increment until this assumption has a kill/keep signal. RAT is not a workshop canvas you admire. It is a stop/go.

If the riskiest assumption is about users, **user testing** with a **task success** measure is the review. Task success is binary-ish: did they complete the job without help, in a time you named? Opinions after the task are extra. Opinions instead of the task are not a test.

### Pre-mortem and steelman
A **pre-mortem** assumes the project has already failed, then asks how. It is scheduled pessimism. It catches “we all privately thought this was doomed” before the money is gone. Write the failure stories, cluster them, put owners on the plausible ones. A pre-mortem that becomes gallows humor with no owners is entertainment.

**Steelman** is the opposite of a straw man: the strongest fair form of a critic’s view. In review, steelman the case for killing your favorite idea before you keep it. If you cannot, you do not understand the risk; you are defending an identity.

### Stakeholder review vs expert review vs user testing
**User testing** asks a person who has the job to do the job. **Stakeholder review** asks someone who pays, blocks, or integrates. **Expert review** asks someone with domain method (security, clinical, accessibility, legal). These three produce different truths. A stakeholder smile is not task success. An expert’s “this is noncompliant” can veto a loved prototype. A user’s success can still die in a stakeholder review if you never wrote the constraint.

Run them as separate meetings when the power dynamics mix. A user will not fail a task honestly in front of their boss who championed the design.

### Redesign, solidify, kill, pivot, ship
Review must end in a **named move**:

| Move | When |
|------|------|
| Redesign | The job is right; the artifact is wrong. Stay in diamond 2. |
| Solidify | The test held; freeze this slice and raise fidelity or DoD. |
| Kill | The job or the assumption is dead. Stop spending. |
| Pivot | The job is still alive; the approach is wrong. Change the bet (Lesson 7). |
| Ship | Evidence and DoD say this increment can leave the building. |

If the meeting ends with “let’s keep thinking,” you did not review. You stalled.

<figure class="fig">
<div class="domain-row">
<div class="domain-card light"><div class="k">Look</div><p>Critique the artifact against the brief. I like / I wish / What if. Author decides after.</p></div>
<div class="domain-card mod"><div class="k">Test</div><p>Assumption map → RAT or user task success. Pre-mortem with owners. Steelman the kill case.</p></div>
<div class="domain-card vig"><div class="k">Name the move</div><p>Redesign · solidify · kill · pivot · ship. “Keep thinking” is not a move.</p></div>
</div>
<figcaption>Review is a gate. If it cannot change the next spend, it is a salon.</figcaption>
</figure>

### Failure catalog
- Slide reviews of high-fi work that never saw a user.
- Experts invited after the launch date is printed.
- Steelman used as a sarcastic prefix to a straw man.
- Task success defined as “they said it was nice.”
- Kill is socially impossible, so everything solidifies.

**Uncertainty:** critique formats vary by school. This pack standardizes on I like / I wish / What if plus a named end move. It does not claim a single inventor in the syllabus.

## Worked example(s)
**Problem:** The contractor onboarding pretotype (L05) showed 4/5 people could not find the packet. Engineering still wants to demo a pre-fill model to leadership on Thursday because the slides are done.

**Steps:**
1. Critique the **decision**, not the slides. Brief end state was “complete the packet unassisted.” Findability failed. Pre-fill was not the riskiest assumption.
2. Assumption map: “they can find it” was unknown and fatal. It just failed. “Pre-fill accuracy” is still unknown but not this week’s gate.
3. Steelman the case for still demoing Thursday: “Leadership morale, budget theater, we look busy.” Fair form: stakeholders need a signal. Unfair form: we ship a look-like of the wrong risk.
4. Named move: **kill** the Thursday product demo as a test. **Redesign** findability. Offer leadership a review of the task-success table instead of a pretty shell.
5. Pre-mortem the next slice: “We fix the link and still fail because the forms are legally unreadable.” Owner: legal + writer, this week.

**Answer / result:** Review changed the spend. That is the only passing grade for a review.

## Key Terms
| Term | Definition |
|------|------------|
| Design critique | Structured look at an artifact against the brief |
| I like / I wish / What if | Speech protocol: specific praise, desired change, experiment |
| Assumption mapping | Claims placed on ignorance × impact |
| Riskiest assumption test | Stop/go test of the fatal unknown |
| Pre-mortem | Assume failure, write how, assign owners |
| Steelman | Strongest fair form of the opposing view |
| User testing | People with the job attempt the job |
| Task success | Whether they completed the job by a named rule |
| Stakeholder review | Payers, blockers, integrators |
| Expert review | Domain method (legal, safety, a11y, security) |
| Redesign / solidify / kill / pivot / ship | Named end-moves of a review |

## Misconception inventory
| Misconception | Reality |
|---------------|---------|
| “Critique means being nice.” | It means being specific to the brief. Niceness without a move is stalling. |
| “Stakeholders speaking is user testing.” | Different truths. Do not mix the meetings if power will fake success. |
| “A pre-mortem is negative.” | Unowned pessimism is negative. Owned failure stories are cheap. |
| “Steelman means agree with the critic.” | It means you can state their best case. Then you may still kill or keep. |
| “If task success is low we just need better onboarding copy in the demo.” | You may need to kill the approach. Do not polish a failed job. |
| “Ship is a feeling of excitement.” | Ship is DoD + evidence. Excitement is optional. |
| “Kill is a career threat.” | If kill is unsayable, your reviews are fake. |
| “What if is a brainstorm.” | In critique, What if is a proposed experiment, not a new diverge session. |

## Summary
- Critique the artifact against the brief with a speech protocol and a time-box.
- Map assumptions; test the fatal unknown; pre-mortem with owners; steelman the kill case.
- User task success ≠ stakeholder smile ≠ expert veto. Separate them.
- End with redesign, solidify, kill, pivot, or ship.
- If spend does not change, it was not a review.

## Practice
### Retrieval
- What are the three I like / I wish / What if jobs?
- RAT vs pre-mortem: what is each for?
- Why separate user testing from stakeholder review?
- Name the five end-moves.

### Near transfer
A prototype “went well” because three executives nodded. There is no task-success data. What review is missing, and what do you refuse to solidify?

### Far transfer
QA testers will look at this Atlas. Write a one-line task-success rule for “a new learner can start Lesson 1 from the folder.”

## Spaced retrieval notes
- Day 0: run I like / I wish / What if on one artifact you made.
- Day 2: map five assumptions; circle the riskiest.
- Day 7: write a half-page pre-mortem of a live project.
- Day 21: force a named end-move in a meeting that wanted to “keep thinking.”

## Difficulty tiers
- **Novice:** critique protocol + named end-move.
- **Working:** RAT, task success, separate review types.
- **Expert:** steelman a kill of your own idea in front of the people who loved it.

## Domain scaffolds
Professional reviews: write the brief at the top of the critique agenda. Experts with veto (safety, legal) go before launch dates are printed. Users are not props in a stakeholder show.

## Learn more
- [Design Council — Framework for Innovation](https://www.designcouncil.org.uk/our-resources/framework-for-innovation/)
- [Scrum Guide](https://scrumguides.org/scrum-guide.html) — Sprint Review inspects the increment, not the team’s feelings.
- [Agile Manifesto](https://agilemanifesto.org/) — customer collaboration; still not a substitute for task success.
