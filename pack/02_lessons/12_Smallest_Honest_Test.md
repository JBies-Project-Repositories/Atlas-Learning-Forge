# Pretotype, MVP, and the Riskiest Assumption

## Learning Objectives
- Tell pretotype, prototype, and MVP apart by how real the test is: pre-mechanism demand or comprehension, a failing artifact, or the smallest **shipped** measured test.
- Rank assumptions by ignorance × impact and put the riskiest assumption first, not the one the team is ready to build.
- Write a smallest testable slice as audience + task + fail rule + STOP, and refuse a slice that has no stop.
- Choose pretotype vs prototype vs MVP from the riskiest assumption and from L11’s kind and rung, not from pride or a domain name.
- Refuse to fake a one-way safety door, or any probe that would teach a dangerous action or extract unpaid labor on a known-broken mechanism.
- Facilitate a 30-minute assumption ranking and test design that leaves a card L13 can review.
- Continue the contractor-onboarding thread: treat findability as riskier than pre-fill until a test says otherwise.

## Prerequisites
- L08: a brief with purpose, end state, constraints, non-goals, and success criteria. A test without a brief will discover a product nobody asked to kill.
- L10: a testable claim, clustered by mechanism — not a slogan, not a crowned helper.
- L11: a named kind (looks / works / experience) and a named rung (low / mid / high), plus a refuse-the-climb sentence. This lesson decides how *real* the test is, not how pretty.
- L01 / L04: intellectual order is Learn → Measure → Build. If you Build first because building is comforting, you have a feature factory. Ries popularized Build–Measure–Learn as a product loop; this pack keeps that intellectual order and does not invent a paper.
- You can tolerate a result that stops the work. If stop is unsayable, you are not testing.

## Lesson Content

### What the move is for
The smallest honest test is how Arc C **earns** the next spend. L09 kept options alive. L10 turned a cluster into a claim. L11 picked a kind and a rung. This lesson puts that claim on trial in the cheapest truthful way: a **fail rule**, a **STOP**, and a name for how real the trial is. The move is for learning that can kill, not for a demo that has to go well.

Honesty is the scarce part. Teams will run a “test” that cannot fail (the helper is shown to friendly staff who already know the path), or a “MVP” that is a prototype with a domain name and no measure, or a fake door that teaches a dangerous click. Those are not small. They are cheap theater. Small means the **slice** is the cheapest path to a kill/keep signal. Honest means the slice can fail, the audience is the people who have the job, and you will actually stop.

Build–Measure–Learn as a slogan puts Build first. The intellectual order is the reverse: what would change our mind (Learn), what signal would we trust (Measure), what is the smallest object that can produce that signal (Build). Pretotype, prototype, and MVP are three answers to that last question, at three different distances from the system of record.

### Decision rule: pretotype vs prototype vs MVP
List the assumptions under the claim. Score each by **how little you know** (ignorance) times **how bad it is if you are wrong** (impact). The top cell is the riskiest assumption. Then:

**If the riskiest assumption is “people want this” or “people understand this” and the mechanism does not need to exist yet**, run a **pretotype**: a fake of the experience that tests demand or comprehension **before** you build the mechanism. Fake door (with care), paper service, concierge, a scripted walkthrough of a path that does not work. The point is to see if anyone cares or can follow.

**If the riskiest assumption is a design or technical question** — can the join hold, can a person complete the steps, does the ranking work — run a **prototype**: an artifact built to answer that question. It may never ship. It **should be able to fail**. L11’s kind and rung apply here.

**If the riskiest assumption is “we can operate this in the real system of record with real users at a small scale,”** run a carefully scoped **MVP**: the smallest **shipped** thing that tests a business or usage hypothesis with a measure and a kill criterion. It is not a prototype with a domain name. If it has no measure and no STOP, it is just v0.1.

If two assumptions tie, pick the one that is **upstream**: the one that, if false, makes the other test meaningless. In contractor onboarding, findability is upstream of pre-fill. If they cannot find the packet, pre-fill never runs. That is a decision rule, not a taste. Do not pick the assumption you already believe because it feels like progress. That is theater.

### Pretotype — pre-mechanism demand and comprehension
**Pretotype**, as used in this field guide, is a fake of the experience that tests demand or comprehension **before** the mechanism exists. The packet URL is not in the offer email yet; you print the current maze and watch someone hunt. The matcher does not exist; you offer a “notify me” button and count who clicks, then tell them it was a test. A concierge plays the future system for a week. A paper service completes the job by hand.

The honesty requirements are sharp. Disclose when deception would harm trust, especially if the product *is* trust. Keep the fake short. Do not collect payment or personal data you cannot legally hold just to “see if they would.” Do not leave a fake door up so long that it becomes a dark pattern. A pretotype that trains people to click a control that will later be a one-way safety action is forbidden — see the safety rule below.

Pretotype is not a trademarked process in this pack, and the syllabus does not hand us a canonical paper. It is a name for **pre-mechanism** tests. If you find yourself building the mechanism “just a little” so the fake feels nicer, you have quietly started a prototype. Name it. If you find yourself shipping the fake to production as if it were the product, you have started an MVP without a measure. Name that too, or stop.

### Prototype — an artifact that can fail
A **prototype** answers a design or technical question. It may be L11 low, mid, or high; looks-like, works-like, or experience. It may never ship. The one non-negotiable: **it should be able to fail**. If the session is staged so that the contractor is walked to the submit button by a smiling host, you did not prototype. You hosted.

Failure is not cruelty. Failure is the signal. Write it in advance: what the person is asked to do, what counts as a miss, how many misses kill the claim for this round. Then shut up while they try. Help rules belong in the script (“we will not help unless you stop for two minutes”), not in the host’s anxiety. Afterward, opinions are extra. Opinions instead of the task are not a test (L14 will separate user, stakeholder, and expert review).

A prototype is not an Increment in the Scrum sense unless you declare it one and it meets the Definition of Done. Most should not. Calling a failing spike “the increment” is how DoD dies. Calling a polished demo “the prototype” is how kill rules die. Keep the coats on the right hooks.

### MVP — smallest shipped measured test
**MVP (minimum viable product)** is the smallest **shipped** thing that tests a hypothesis in the real system of record. Shipped means real users, real data path, real support burden, even if the audience is five contractors and the feature flag is on for them only. Measured means you named the signal before the data (L15 will push evidence thresholds; this lesson requires that the signal exist). Kill criterion means you will turn it off or not expand it if the signal fails.

MVP is not “the smallest pile of features we are willing to be seen with.” That is a v0.1 of the full fantasy, and it usually includes the helper, the pre-fill, the dashboard, and the branding — which means you still have not tested findability. Smallest is the slice that isolates the riskiest assumption, not the fewest screens of the full product. Viable is “can produce a measure in the real system,” not “can win a demo.”

If you cannot operate it — support, rollback, a person to answer the Slack DMs the test was supposed to kill — you are not ready for MVP. Stay in pretotype or prototype. Dual-track (L05) exists so discovery can remain honest while delivery ships something else. Do not launder a discovery probe through production to make it feel serious.

### Riskiest assumption first — ignorance × impact
Write assumptions as sentences that can be false. “Contractors can find the packet from the offer email.” “Pre-fill from HRIS is correct enough that people will not DM staff about the errors.” “A helper at the moment of stuck beats deleting a form.” “Legal will block HRIS pre-fill.” Score two axes: **ignorance** (how little we know — have we watched even one person?) and **impact** (if wrong, does the rest of the work become waste?). The riskiest is high on both. Test that one.

Teams love testing the assumption they already believe, because the test is easy to instrument and the demo will go well. That is why helpers get prototypes and findability does not: the helper is a product story; the maze is an embarrassment. Rank anyway. Upstream unknowns beat downstream cleverness. A legal assumption that is both unknown and fatal is not a prototype problem; it is a counsel problem, then a test of the remainder.

Assumption mapping as a wall exercise belongs with L13. This lesson only needs the ranking and the first test. If you cannot rank, you cannot slice. If everything is “high impact,” you have not named the work; return to L08.

### Smallest testable slice = audience + task + fail rule + STOP
A slice is not a set of screens. It is four parts, written before anyone is recruited:

1. **Audience** — who has the job. New contractors, not the director’s favorite power user, not the designer who drew the map, not staff who already know the three logins.
2. **Task** — the job in their words. “Finish the packet.” “Start the packet.” Not “explore the helper.”
3. **Fail rule** — a threshold you will not negotiate after you like the participants. “If 3/5 cannot start within five minutes, the claim fails this round.”
4. **STOP** — what you will not spend if it fails. “Do not build pre-fill this sprint. Do not spike the helper. Fix findability or kill the claim.”

If you cannot name the STOP, you are not testing. You are demoing. If you cannot name the fail rule, you will move the goalposts when a friendly contractor chats their way through. If the audience is wrong, you will get polite chrome opinions. The slice can sit on any L11 rung and any of the three reality names (pretotype / prototype / MVP). The four parts are the honesty check for all of them.

<figure class="fig">
<svg class="lesson-chart" viewBox="0 0 720 250" role="img" aria-label="Three reality names and a four-part slice: audience, task, fail rule, STOP">
  <rect x="16" y="18" width="220" height="86" rx="10" fill="var(--card)" stroke="var(--border)"/>
  <text x="126" y="50" text-anchor="middle" font-size="14" font-weight="700">Pretotype</text>
  <text x="126" y="72" text-anchor="middle" class="muted" font-size="11">Demand / comprehension</text>
  <text x="126" y="90" text-anchor="middle" class="muted" font-size="11">before the mechanism</text>
  <rect x="250" y="18" width="220" height="86" rx="10" fill="#7eb8c4"/>
  <text x="360" y="50" text-anchor="middle" fill="#14343c" font-size="14" font-weight="700">Prototype</text>
  <text x="360" y="72" text-anchor="middle" fill="#14343c" font-size="11">Can fail; may never ship</text>
  <text x="360" y="90" text-anchor="middle" fill="#14343c" font-size="11">answers a design/tech Q</text>
  <rect x="484" y="18" width="220" height="86" rx="10" fill="#1c5d68"/>
  <text x="594" y="50" text-anchor="middle" fill="#fff6d6" font-size="14" font-weight="700">MVP</text>
  <text x="594" y="72" text-anchor="middle" fill="#c5eef2" font-size="11">Smallest shipped</text>
  <text x="594" y="90" text-anchor="middle" fill="#c5eef2" font-size="11">measured test</text>
  <rect x="16" y="124" width="166" height="70" rx="8" fill="var(--card)" stroke="var(--border)"/>
  <text x="99" y="154" text-anchor="middle" font-size="13" font-weight="700">Audience</text>
  <text x="99" y="176" text-anchor="middle" class="muted" font-size="11">who has the job</text>
  <rect x="190" y="124" width="166" height="70" rx="8" fill="var(--card)" stroke="var(--border)"/>
  <text x="273" y="154" text-anchor="middle" font-size="13" font-weight="700">Task</text>
  <text x="273" y="176" text-anchor="middle" class="muted" font-size="11">the job in their words</text>
  <rect x="364" y="124" width="166" height="70" rx="8" fill="var(--card)" stroke="var(--border)"/>
  <text x="447" y="154" text-anchor="middle" font-size="13" font-weight="700">Fail rule</text>
  <text x="447" y="176" text-anchor="middle" class="muted" font-size="11">threshold, pre-committed</text>
  <rect x="538" y="124" width="166" height="70" rx="8" fill="#9b1c14"/>
  <text x="621" y="154" text-anchor="middle" fill="#fff6d6" font-size="13" font-weight="700">STOP</text>
  <text x="621" y="176" text-anchor="middle" fill="#f3cc74" font-size="11">what you will not spend</text>
  <text x="360" y="222" text-anchor="middle" font-size="12">Rank assumptions by ignorance × impact. Test the upstream unknown. Never fake a one-way safety door.</text>
</svg>
<figcaption>Reality name (top) is how shipped and how fake. Slice (bottom) is how honest. Missing STOP means you are demoing.</figcaption>
</figure>

### Never fake a one-way safety door
Some actions cannot be rehearsed as cute fakes. A control that deletes, pays, sends, doses, unlocks, or submits a legal filing in the real world is a **one-way door** if it cannot be undone by the person who just used it. Do not pretotype that door with a clickable dummy that looks like the real control if the dummy could teach the dangerous action. People learn motor patterns and trust patterns from fakes. A high looks-like of an unsafe pattern is a better teacher of the unsafe pattern (L11).

The rule is not “never pretotype anything serious.” It is: **do not use a fake that can be mistaken for the real irreversible action**, and do not use people as crash-test dummies for a mechanism you already know is broken. Safety-critical work gets a rehearsal with a safety owner, or a works-like on a non-production path, or a tabletop. It does not get a dark-pattern fake door. Legal-irreversible work (tax filing, identity attestation) gets counsel, then a probe of the *path*, not a fake Submit that might actually submit.

If you are unsure whether a door is one-way, treat it as one-way until a domain owner says otherwise. This pack is educational. It does not replace a specialist review.

### Failure catalog
Theater tests share a shape: they protect the favorite spend.

- Testing the assumption you are **ready to build**, not the one that is unknown and fatal.
- **MVP as a prototype with a domain name**, no measure, no STOP.
- **Pretotype as a lie to users forever**, or a fake door left up as growth hack.
- **No STOP.** The helper will be built anyway. Then the test was content.
- **Wrong audience:** staff, friends, the director. Polite success.
- **Fail rule written after** seeing the data. Goalposts on wheels.
- **Downstream test first** (pre-fill quality) while the upstream maze is unwatched.
- **Faking a one-way safety door**, or extracting unpaid labor on a known-broken mechanism.
- Calling a **demo that cannot fail** a prototype (L11’s sales artifact, now with users).

Two of these and you cancel the test, not the week. Redesigning the slice is cheaper than laundering a favorite.

### Facilitation script: thirty minutes to rank and design
This meeting produces a card, not a build. Invite the people who can name assumptions and the person who can actually STOP spend. If the HiPPO can only attend to “make sure we still do the helper,” you have L09’s cancel problem in a new coat. Either they agree that STOP is live, or you do not call this a test design.

Put two axes on the wall (ignorance, impact) or a simple 1–3 score each. Put a blank four-part slice. Put the three reality names. Put L11’s kind and rung so you do not renegotiate paper vs Figma for twenty of the thirty minutes. Then run the clock.

Minute-by-minute:

- **0:00–0:08 — List assumptions as false-able sentences.** Under the L10 claim, write five to nine. Include the embarrassing ones (they cannot find it; they do not want it; legal blocks it; HRIS is wrong 30% of the time; DMs are a load-bearing social system). No solutions on this list.
- **0:08–0:15 — Score ignorance × impact.** Silent scores first (brainwriting the numbers, L10’s airtime move), then a short reveal. Circle the top. If pre-fill beats findability in the room’s heart but not on the scores, say that out loud. Upstream tie-break: if A being false makes B’s test meaningless, A wins.
- **0:15–0:25 — Design the slice.** Audience, task, fail rule, STOP. Reality name: pretotype / prototype / MVP. Kind and rung from L11, confirmed not climbed. Help rule. How you will disclose a pretotype. Safety check: is any control a one-way door? If yes, change the artifact.
- **0:25–0:30 — Read the card back.** “If this fails, we will not do X this sprint.” Get the person with budget to say it. Schedule the actual sessions. Hand L13 a copy: this is what critique and RAT will look at. Do not add a second test “while we are at it.”

If the thirty minutes produce a helper spike and a vague “we’ll watch a couple people,” you failed the script. Run it again with the STOP line first.

**Uncertainty:** “Pretotype” is popular jargon; this pack treats it as pre-mechanism demand/comprehension tests, not as a trademarked process. MVP has been stretched to mean “small launch.” Here it means shipped + measured + killable. There is no canonical URL in the syllabus for pretotype or MVP; do not invent one. Cynefin-style labeling still applies: a statutory form can be complicated; the path to it is often complex and wants a probe, not a Gantt.

## Worked example(s)
**Problem:** Claim 1 from L10–L11: a new contractor can start the required packet within five minutes of opening the offer email, without DMing staff. Kind/rung: low-fidelity experience (paper or literal map of the current maze; real inbox if possible). The director’s helper and the HRIS pre-fill spike are still hovering. Leadership Friday still wants a demo. Someone says “let’s just ship a thin MVP of the helper and measure completion.”

**Steps:**
1. **List assumptions.** (a) Contractors can find the packet from current email/login/zip. (b) They understand they must finish in one sitting. (c) Pre-fill would be accurate enough not to create new DMs. (d) A helper at stuck-moment would be used. (e) Legal will allow HRIS pre-fill. (f) Staff DMs are the pain we think they are. (g) Phone completion is possible on the current forms.
2. **Score ignorance × impact.** (a) is high ignorance (nobody has watched a new contractor; staff already know the maze) and high impact (if false, every downstream product is waste). (c) and (d) are medium-high impact but lower urgency until (a) holds. (e) is high impact, unknown — that is counsel, not a helper spike. (a) wins. Findability is riskier than pre-fill.
3. **Reality name.** Mechanism of a new product does not need to exist to test (a). This is a **pretotype** of the current experience (and a low experience prototype of the path): watch the maze as it is. Not an MVP of a helper. Shipping a helper to measure completion would confound findability with help-at-stuck and burn the non-goal (no new vendor) or the sprint.
4. **Slice.** Audience: five *new* contractors, not staff. Task: “Finish the packet. Talk aloud.” Fail rule: if 3/5 cannot **start** within five minutes, Claim 1 fails this round. STOP: do not build pre-fill this sprint; do not spike the helper; Friday’s artifact, if it exists, is a captioned demo, not evidence. Help rule: no help unless they stop for two minutes. Disclose: “We are watching the current path to see where it breaks; this is not a new product.”
5. **Safety / one-way check.** Starting a tax packet is not a cute fake of a one-way legal submit if they use the **real** current forms they were already going to use. Do not add a dummy Submit that might post. Do not pretotype e-file. Path only.
6. **Only if findability holds**, design the next slice (Claim 2): Wizard-of-Oz pre-fill (human pastes HRIS values) as a works-like/experience prototype — still not MVP. Fail rule and STOP for that slice get their own card.

**Answer / result:** You might kill the AI-helper fantasy in an afternoon. That is a successful test. A polished Figma of the helper would have been a looks-like of the wrong risk. An “MVP helper” would have been v0.1 theater. Findability first; pre-fill second; helper only if it is still a live mechanism after both. Arc C ends when the card exists and the STOP is sayable. Arc D (L13–L16) critiques, reviews, and decides whether to pivot, persevere, or ship a later slice.

## Key Terms
| Term | Definition |
|------|------------|
| Pretotype | Pre-mechanism fake of the experience that tests demand or comprehension |
| Prototype | Artifact built to answer a design or technical question; should be able to fail; may never ship |
| MVP | Smallest shipped, measured test of a hypothesis in the real system of record |
| Riskiest assumption | High ignorance × high impact; test this first |
| Upstream unknown | If it is false, downstream tests are meaningless |
| Smallest testable slice | Audience + task + fail rule + STOP |
| Fail rule | Pre-committed threshold that makes the claim false this round |
| STOP | The spend you will not make if the test fails |
| One-way door | Action the person cannot undo; do not cute-fake it |
| Honest test | Can fail; right audience; named STOP; no goalpost moving |
| Theater test | Protects a favorite spend; cannot fail or will not stop |
| v0.1 | Shipped pile without measure or kill criterion; not an MVP |
| Concierge / Wizard-of-Oz | Human plays the system; pretotype or prototype depending on the question |
| Intellectual order | Learn → Measure → Build, even when the slogan is Build–Measure–Learn |

## Misconception inventory
| Misconception | Reality |
|---------------|---------|
| “MVP is a prototype we put on a domain.” | MVP is shipped and measured, with a kill criterion. Prototype may never ship. |
| “Smallest slice means fewest screens of the full product.” | It means the cheapest path to a kill/keep signal. |
| “Test the assumption we are ready to build.” | That is comfort. Rank by ignorance × impact. |
| “A demo that cannot fail is a good prototype.” | If it cannot fail, it is sales. |
| “Pretotype means lie to users forever.” | It is a short, disclosed-when-needed test of demand/comprehension. |
| “If we cannot name STOP, we can still learn.” | Then you will not stop. You are demoing. |
| “Findability can wait; the helper is the product.” | If they cannot find the packet, the helper never runs. Upstream first. |
| “Fake doors are always cheap and clever.” | Not if they teach a dangerous action or rot trust. |
| “Shipping makes it honest.” | Shipping without a measure is v0.1. Honesty is the fail rule. |
| “Legal risk is a prototype.” | Ask counsel; pretotype the remainder. Do not fake a one-way filing. |

## Summary
- Pretotype tests demand/comprehension before mechanism. Prototype can fail and may never ship. MVP is the smallest shipped measured test.
- Rank assumptions by ignorance × impact. Test the riskiest, and the upstream one when they compete.
- A smallest testable slice is audience + task + fail rule + STOP. Missing STOP means you are demoing.
- Never fake a one-way safety door. Never use people to pretty a known-broken mechanism.
- Do not call v0.1 an MVP. Do not call a captioned leadership picture a test.
- Facilitate 30 minutes: list, score, slice, read back the STOP with the person who owns spend.
- In contractor onboarding, findability is riskier than pre-fill until a test says otherwise.
- Arc C’s job is a claim that can die. Arc D decides what to do after it lives or dies.

## Practice
### Retrieval
- Pretotype vs prototype vs MVP in one sentence each.
- What two factors rank the riskiest assumption?
- What four parts make a smallest testable slice?
- Why is findability upstream of pre-fill in the continuing case?
- What is a one-way safety door, and what do you refuse to do with it?
- What is the intellectual order of Build–Measure–Learn in this pack?

### Near transfer
Stakeholders want to “ship an MVP helper by Friday” to measure onboarding completion. You have never watched a contractor find the packet. Write the assumption list, the ranking, and the slice you run instead — including STOP.

### Far transfer
You are testing this Atlas pack. Riskiest assumption: mixed-knowledge learners can find Arc C Lesson 12 from the cover without DMing Jenner. Design a 48-hour pretotype (audience, task, fail rule, STOP). Name one fake you would refuse because it would teach the wrong door.

## Spaced retrieval notes
- Day 0: list three assumptions on a live project; mark the riskiest (ignorance × impact) and the upstream one.
- Day 2: write audience, task, fail rule, and STOP for that assumption. Read the STOP to someone who could actually stop the spend.
- Day 7: run or observe the cheapest honest test; note whether the fail rule moved after seeing people.
- Day 21: catch a v0.1 called MVP, or a demo called a prototype; rename it; check for a one-way door you would not fake.

## Difficulty tiers
- **Novice:** pretotype vs prototype vs MVP; four-part slice; findability before pre-fill in the case.
- **Working:** rank ignorance × impact; write STOP; refuse a fake door; keep MVP shipped-and-measured.
- **Expert:** hold a leadership demo and a real test on the same calendar without letting the demo eat the STOP; design the next slice only if the upstream claim holds.

## Domain scaffolds
Professional products: disclose pretotypes when deception would harm trust; do not leave fake doors up as a growth habit. Safety-critical and medical: one-way doors (dose, unlock, delete, irreversible send) are rehearsed with a domain owner or not at all — never as a cute pretotype that looks like the real control. Payments and legal filings: counsel first; probe the path; do not dummy-submit. Complicated statutory packets (tax, identity): the fields may be a checklist; the findability of the packet is still a complex probe. Operations: if you cannot support even five real users, you are not at MVP; stay on pretotype/prototype and say so. This lesson does not replace specialist review.

## Learn more
- [Design Council — Framework for Innovation](https://www.designcouncil.org.uk/our-resources/framework-for-innovation/) — Deliver is not “the pretty version of Develop.” A shipped test still has to be a test.
- [Manifesto for Agile Software Development](https://agilemanifesto.org/) — working software over comprehensive documentation; an MVP is working enough to measure, not documented enough to demo.
- [Principles behind the Agile Manifesto](https://agilemanifesto.org/principles.html) — simplicity as maximizing work not done; STOP is that principle with a date.
- [The 2020 Scrum Guide](https://scrumguides.org/scrum-guide.html) — Increment and Definition of Done; a prototype is not an Increment unless you say it is, and an MVP that cannot be undone needs a real Done, not a flag you forgot.
- [Snowden & Boone, “A Leader’s Framework for Decision Making,” HBR](https://hbr.org/2007/11/a-leaders-framework-for-decision-making) — complicated work can take a checklist; complex work wants a probe. The smallest honest test is a probe, not a plan for a user who does not exist.
