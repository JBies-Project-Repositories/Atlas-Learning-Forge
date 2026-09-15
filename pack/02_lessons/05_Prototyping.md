# Prototyping

## Learning Objectives
- Choose a fidelity (low / mid / high) that matches the question, not the stakeholder’s appetite for polish.
- Tell looks-like, works-like, and experience prototypes apart, and pick pretotype vs prototype vs MVP.
- Define the smallest testable slice and put the riskiest assumption first.
- Refuse a high-fidelity demo that cannot fail — that is a sales artifact, not a test.

## Prerequisites
- Lessons 3–4: a testable claim exists (who, job, what would change your mind).
- You can name one assumption that, if false, should stop the work.

## Lesson Content

### Fidelity is a budget for attention
**Fidelity** is how finished the artifact looks or behaves. **Low-fidelity** is cheap and ugly on purpose: paper, boxes, a script. It answers “is this even the job?” **Mid-fidelity** is structured but unfinished: clickable wireflows, a Wizard-of-Oz backend. It answers “can a person get through the steps?” **High-fidelity** looks or works close to the real thing. It answers “will this hold in the real texture — timing, trust, accessibility, load?”

The injury is using high fidelity too early. Polish persuades. Stakeholders say yes to a picture of a product that has not been tested. Then the picture becomes the spec. Low fidelity is a kindness: it is easier to kill.

Match fidelity to the **question**, not to the audience’s rank. A vice president can read paper if you tell them what question the paper is for. If they cannot, you have an alignment problem (Lesson 3), not a fidelity problem.

### Looks-like, works-like, experience
A **looks-like** prototype tests appearance, hierarchy, and recognition. A **works-like** prototype tests mechanism: the algorithm, the mechanical joint, the data path — it may look like junk. An **experience** prototype tests the whole episode in time: waiting, handoff, emotion, the phone call after. Teams often build looks-like when the risk is works-like (does the matcher even work?) or experience (will a tired person complete this at 11 p.m.?).

Name which one you are making. A pretty shell with no mechanism is not “agile.” It is a looks-like. That is allowed if appearance is the risk. It is fraud if the risk was mechanism.

### Pretotype, prototype, MVP
**Pretotype** (as used in this field guide): a fake of the experience that tests demand or comprehension **before** you build the mechanism. Fake door, paper service, concierge. The point is to see if anyone cares or understands.

**Prototype:** an artifact built to answer a design or technical question. It may never ship. It should be able to fail.

**MVP (minimum viable product):** the smallest **shipped** thing that tests a business or usage hypothesis in the real system of record. It is not a prototype with a domain name. If it has no measure and no kill criterion, it is just v0.1.

The syllabus also says **smallest testable slice** and **riskiest assumption first**. Those two rules decide which of the three you make. If the riskiest assumption is “people want this,” pretotype. If it is “the algorithm can rank this,” works-like prototype. If it is “we can operate this at 100 users,” a carefully scoped MVP — not a tour of every future feature.

### Riskiest assumption first
List assumptions. Score **impact if wrong** × **how little we know**. Test the top one. Teams love testing the assumption they already believe, because it feels like progress. That is theater.

A smallest testable slice includes: the audience, the task, the success/fail rule, and what you will **stop** if it fails. If you cannot name the stop, you are not testing. You are demoing.

<figure class="fig">
<svg class="lesson-chart" viewBox="0 0 720 200" role="img" aria-label="Fidelity ladder from paper to MVP">
  <rect x="20" y="80" width="120" height="70" rx="8" fill="var(--card)" stroke="var(--border)"/>
  <text x="80" y="110" text-anchor="middle" font-size="12" font-weight="700">Paper</text>
  <text x="80" y="130" text-anchor="middle" class="muted" font-size="11">lo-fi pretotype</text>
  <rect x="160" y="60" width="120" height="90" rx="8" fill="var(--card)" stroke="var(--border)"/>
  <text x="220" y="100" text-anchor="middle" font-size="12" font-weight="700">Wizard</text>
  <text x="220" y="120" text-anchor="middle" class="muted" font-size="11">mid experience</text>
  <rect x="300" y="40" width="120" height="110" rx="8" fill="var(--card)" stroke="var(--border)"/>
  <text x="360" y="90" text-anchor="middle" font-size="12" font-weight="700">Works-like</text>
  <text x="360" y="110" text-anchor="middle" class="muted" font-size="11">mechanism risk</text>
  <rect x="440" y="25" width="120" height="125" rx="8" fill="#7eb8c4"/>
  <text x="500" y="85" text-anchor="middle" font-size="12" font-weight="700">Hi-fi</text>
  <text x="500" y="105" text-anchor="middle" font-size="11">texture / trust</text>
  <rect x="580" y="15" width="120" height="135" rx="8" fill="#1c5d68"/>
  <text x="640" y="80" text-anchor="middle" fill="#fff6d6" font-size="12" font-weight="700">MVP</text>
  <text x="640" y="100" text-anchor="middle" fill="#c5eef2" font-size="11">shipped test</text>
  <text x="360" y="185" text-anchor="middle" class="muted" font-size="12">Climb only when the cheaper step cannot kill the assumption.</text>
</svg>
<figcaption>Do not climb because a stakeholder asked for a “real demo.” Climb because the current rung cannot answer the question.</figcaption>
</figure>

### What not to prototype
Do not prototype a one-way safety door as a cute fake if the fake could teach a dangerous action. Do not use users as unpaid labor for a mechanism you already know is broken. Do not high-fi a thing whose riskiest assumption is legal: ask counsel, then pretotype the remainder.

**Uncertainty:** “Pretotype” is popular jargon; the syllabus lists it next to prototype and MVP. This pack treats it as **pre-mechanism demand/comprehension tests**, not as a trademarked process.

## Worked example(s)
**Problem:** Claim from L04: contractors will complete required forms in one sitting if fields are pre-filled from HRIS. Riskiest assumption is actually “they can even find the packet” — not the pre-fill quality.

**Steps:**
1. Re-rank assumptions. Finding beats pre-fill. If they cannot find it, pre-fill never runs.
2. Smallest test: five new contractors, a paper map of the current email → link → form. Task: “Finish the packet. Talk aloud. We will not help unless you stop for two minutes.”
3. Fidelity: low, experience-ish (real time, real inbox if possible). Looks-like branding is a non-goal.
4. Fail rule: if 3/5 cannot start within five minutes, do not build pre-fill this sprint. Fix findability.
5. Only if findability holds, Wizard-of-Oz a pre-fill (a human pastes values) as a works-like/experience hybrid — still not an MVP.

**Answer / result:** You might kill the AI-helper fantasy in an afternoon. That is a successful prototype. A polished Figma of the helper would have been a looks-like of the wrong risk.

## Key Terms
| Term | Definition |
|------|------------|
| Fidelity | How finished the artifact looks or behaves |
| Low-fidelity | Cheap, ugly on purpose; tests the job |
| Mid-fidelity | Structured but unfinished; tests the steps |
| High-fidelity | Close to real texture; tests trust, timing, load |
| Looks-like | Tests appearance and recognition |
| Works-like | Tests mechanism; may look like junk |
| Experience prototype | Tests the episode in time |
| Pretotype | Fake of the experience before the mechanism exists |
| Prototype | Artifact built to answer a question; should be able to fail |
| MVP | Smallest shipped test of a hypothesis in the real system |
| Smallest testable slice | Audience + task + fail rule + stop condition |
| Riskiest assumption first | Test the high-impact unknown, not the comforting one |

## Misconception inventory
| Misconception | Reality |
|---------------|---------|
| “Higher fidelity is always more professional.” | Early polish persuades and freezes. Match the question. |
| “MVP is a prototype we put on a domain.” | MVP is shipped and measured. Prototype may never ship. |
| “If it looks unfinished, stakeholders will not take it seriously.” | Tell them the question. If they still need polish, you are demoing, not testing. |
| “Works-like can wait until after the pretty shell.” | If mechanism is the risk, the shell is theater. |
| “Pretotype means lie to users forever.” | It is a short, disclosed or obviously-fake test of demand/comprehension. |
| “Test the assumption we are ready to build.” | That is comfort. Rank by ignorance × impact. |
| “A demo that cannot fail is a good prototype.” | If it cannot fail, it is sales. |
| “Smallest slice means fewest screens of the full product.” | It means the cheapest path to a kill/keep signal. |

## Summary
- Fidelity is a budget. Spend it on the question.
- Looks-like, works-like, and experience answer different risks.
- Pretotype vs prototype vs MVP is about how real the test is, not how proud the deck is.
- Riskiest assumption first; smallest slice includes a stop rule.
- A prototype that cannot fail is not a test.

## Practice
### Retrieval
- When is low-fi the professional choice?
- Pretotype vs MVP in one sentence each.
- What four parts make a smallest testable slice?
- Why can a works-like look like junk?

### Near transfer
Stakeholders want a “realistic demo” next week. The riskiest assumption is legal, not visual. What do you prototype, and what do you refuse?

### Far transfer
You are testing this Atlas pack. What is the riskiest assumption, and what pretotype would you run in 48 hours?

## Spaced retrieval notes
- Day 0: list three assumptions on a live project; mark the riskiest.
- Day 2: write a fail rule and a stop condition for one assumption.
- Day 7: run or observe a lo-fi test; note whether polish snuck in.
- Day 21: catch a demo that could not fail; rename it sales.

## Difficulty tiers
- **Novice:** lo/mid/hi and pretotype vs MVP.
- **Working:** pick looks/works/experience; write a smallest slice.
- **Expert:** hold a VP to paper when paper is the honest rung.

## Domain scaffolds
Professional products: disclose pretotypes when deception would harm trust. Safety-critical fakes that teach a dangerous action are forbidden. Complicated compliance work may need a rehearsal (high-fi of the real procedure), not a cute paper app.

## Learn more
- [Design Council — Framework for Innovation](https://www.designcouncil.org.uk/our-resources/framework-for-innovation/) — develop/deliver as the home of making and testing.
- [Agile Manifesto](https://agilemanifesto.org/) — working software over comprehensive documentation; a prototype is not automatically working software.
- [Scrum Guide](https://scrumguides.org/scrum-guide.html) — Increment must meet DoD; a prototype is not an increment unless you say it is.
