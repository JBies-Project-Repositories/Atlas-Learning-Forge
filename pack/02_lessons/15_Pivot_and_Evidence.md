# Pivot, Persevere, and Evidence Thresholds

## Learning Objectives
- Report learning velocity (tests) and feature velocity (DoD increments) as two scoreboards, never as one.
- Distinguish pivot (job alive, approach wrong), kill (job dead), and persevere (bet holds).
- Write an evidence threshold before seeing the data, then use it as the only honest pivot/persevere rule.
- Match the height of the bar to the door: reversible copy vs a one-way legal or safety gate.
- Run a retrospective as inspect-and-adapt of the loop, with exactly one change to the next cycle.
- Refuse to call “we iterated” delivery, and refuse to call shipping proof that the idea was right.
- Use the Scrum Guide’s retrospective job — inspect the process, then adapt — without turning it into blame.

## Prerequisites
- Lessons 12–14: a smallest honest test, a named task-success rule, and a critique that can end in a move.
- Lesson 7: cadence, WIP, and Definition of Done exist as words you can fail.
- Something on the table could pivot, die, or survive this month — not only be “iterated.”

## Lesson Content

### Two velocities, two scoreboards
**Learning velocity** is how fast you kill or keep assumptions. Its units are **tests**, not tickets. A week with three honest pretotypes and one kill is fast learning even if the backlog did not grow. **Feature velocity** is how fast you add done increments that users can touch. Its units are **Definition-of-Done-passing slices**. A week with twelve “in progress” ideas and zero done is not feature velocity. It is WIP.

The move is FOR stopping a single number from lying. Executives will ask for “velocity.” If you only have one number, you will optimize theater: either a pile of unshipped experiments reported as delivery, or a pile of shipped guesses reported as learning. Give them two numbers. Learning: how many assumptions got a kill/keep signal. Feature: how many slices met DoD in the hands of a user. If one of those is zero, say zero.

Decision rule: never report learning as if it were delivery (“we iterated”) and never report delivery as if it were learning (“we shipped so we must have been right”). Shipping proves you can operate a slice (Lesson 16). It does not prove the job was the right job. A test that kills a bad bet is learning. It is not a missed sprint goal unless you had dishonestly put the bet in the DoD column.

The injury is fashionable language. “We iterated on the AI onboarding” can mean: we ran two tests and pivoted (learning), or we started eight tickets and finished none (WIP), or we shipped a shell with no measure (a costume). Ask: which scoreboard? If they cannot point, they are not measuring. They are narrating.

### Units: tests vs DoD increments
A **test** on the learning scoreboard has a pre-written threshold, a named audience, and a stop/go (Lessons 12–14). Fake doors, pretotypes, task-success sessions, expert vetoes — these count. Meetings do not count. Slide reviews do not count. “Talked to a stakeholder” counts only if you asked a payer/blocker/integrator question and wrote the answer as a constraint. Otherwise it is a chat.

A **DoD increment** on the feature scoreboard is a slice a user can touch that meets the quality bar you already wrote (Lesson 7). Not “dev done.” Not “ready for hardening.” Not “demoed at all-hands.” If accessibility, rollback, or support are in the DoD, they count here, not in a later season. If they are not in the DoD, you are not counting features. You are counting hopes.

Decision rule: a work item cannot sit on both scoreboards as if they were the same. A Wizard-of-Oz pre-fill that five contractors attempted is a test. It becomes a feature only when it is in the real system, with DoD, and operated. Teams try to double-count because double-counting looks busy. Busy is not a unit.

WIP is the enemy of both velocities. High WIP means tests do not finish (no signal) and increments do not finish (no DoD). If the board is a sea of in-progress, you do not have a pivot problem yet. You have a finishing problem. Limit WIP until a test or a slice actually ends. Then you are allowed to argue pivot vs persevere.

### Pivot, persevere, kill — three different sentences
**Persevere** means the bet still holds; keep the approach, maybe raise fidelity or widen the slice. **Pivot** means the job is still alive and the approach is wrong; change the bet without pretending it was the plan all along. **Kill** means the job is dead, or the assumption that justified the job is dead; stop spending. These are three sentences. Blurring them is how organizations save face and waste quarters.

The move is FOR naming what changed. If contractors still must complete a tax packet, and they cannot find it, and pre-fill was the approach, you do not kill onboarding. You **pivot** from pre-fill-as-the-product to findability-as-the-product. If you discover contractors already complete the packet through a side door and never needed you, you **kill** the epic. If 5/5 find the packet under the named rule, you **persevere** on findability and you may solidify (Lesson 13). Pivot is not a nicer word for fail. Kill is fail-the-job. Pivot is change-the-approach. Persevere is not stubbornness; it is the threshold saying keep.

Decision rule: write which of the three you are claiming, in a sentence that names the job and the approach. “Pivot: job = unassisted packet completion; approach changes from model-pre-fill to findability.” “Kill: job = unassisted packet completion is not a job they have; they do not file.” “Persevere: findability bet holds at 5/5; raise fidelity on the link, not on the model.” If you cannot write that sentence, you are still in “keep thinking.”

Do not pivot every week as a personality. A pivot without a threshold is a mood. Do not persevere because the slides are booked. That is sunk cost. Do not kill a job because a test of the *approach* failed. That is cowardice dressed as rigor, or rigor dressed as a reorg.

### Evidence thresholds written BEFORE the data
You cannot pivot vs persevere on vibes. An **evidence threshold** is written **before** the test: what signal, in whom, would make us persevere, pivot, or kill. Example: “If fewer than 3/5 contractors start the packet in five minutes, we pivot from pre-fill to findability; if 0/5 care about the packet at all, we kill the epic; if 4/5 start unassisted, we persevere on this path.” If you write the threshold after you see the data, you are storytelling. The story will save the plan. That is what stories are for. They are not for gates.

The move is FOR locking honesty while you are still honest. After 2/5, everyone can invent a threshold that makes 2/5 a win (“we learned so much,” “the two who finished loved it,” “n=5 is not significant so we continue”). Pre-commitment is the whole trick. Put the sentence on the brief, in the critique agenda, and at the top of the test script. When the last participant leaves, you read the sentence aloud before anyone interprets.

Thresholds should match the risk. A legal one-way door needs a higher bar than a copy change. Do not demand a randomized trial to move a button, and do not ship a medical-adjacent workflow on five friends’ thumbs-up. Reversible, cheap, in-product copy: a small task-success probe can persevere. Irreversible, harmful, or legally sticky: expert review plus a bar you would defend in writing. The height of the bar is a decision. Hiding the bar is also a decision. It is the worse one.

Decision rule: no test starts without the three-way sentence (persevere / pivot / kill) written in the future tense. If the team “doesn’t want to box itself in,” they are asking for the right to narrate later. Refuse. A threshold can be revised *before* the next test, in daylight, with a reason. It cannot be revised in the five minutes after the data land.

### Matching the bar to the door
Not every unknown is a one-way door. Cynefin-style sense (Lesson 2) still applies: complicated work with a known statute may need a high bar and a rehearsal, not a pretotype. Complex work about whether anyone can find a link may need a cheap probe and a low bar for a *pivot*, not a six-month study. The door is the question: if we are wrong, what is the cost of reversal?

Low door: subject line, link label, helper text. Threshold can be small and fast. Medium door: changing the system of record, adding a vendor, teaching leadership that “AI onboarding” is the product. Threshold must include stakeholder and expert truths (Lesson 14), not only users. High door: legal language, money movement, safety, identity. Threshold includes specialists and a willingness to **kill**. A pivot is not available if the job itself is forbidden.

Decision rule: name the door on the same card as the threshold. “Door: reversible (email copy). Bar: 4/5 start in five minutes or we change the subject line again.” “Door: one-way (signature language). Bar: counsel no-veto or we do not ship, no matter what users say.” If someone wants a high-door ship with a low-door bar, they are buying speed with someone else’s harm. That is not learning velocity. That is negligence with a loop vocabulary.

Do not use “we’re still learning” to keep a high door open. Learning mode is a privilege of cheap reversal (Lesson 16). Once people depend on the slice, the bar for changing it goes up. Write that in the threshold too: “After ship, we do not silently rewrite the live link; a new loop needs a new brief.”

### The Scrum Guide retrospective as inspect-and-adapt of the loop
A **retrospective** inspects the **loop**, not the people. The [2020 Scrum Guide](https://scrumguides.org/scrum-guide.html) puts the Sprint Retrospective in that job: inspect how the last Sprint went with regard to individuals, interactions, processes, tools, and the Definition of Done; identify the most helpful changes to improve effectiveness; address the most impactful improvement as soon as possible. This pack teaches that move whether or not you are wearing a Scrum coat. Inspect the cadence, the WIP, the DoD, the review rooms, the threshold habit. Adapt the next loop. One change is a passing retro. A retro that produces twelve actions is a wishlist. Wishlists do not adapt. They decorate.

The move is FOR making the *system of work* the artifact on trial, the way Lesson 13 put the product artifact on trial. “Who slipped” is not inspect-and-adapt. It is a trial of a person. People theater is not a retro. If the last cycle shipped a demo of an untested model, the loop failure is “leadership slots can override RAT,” not “Jordan is bad.” The change might be: no all-hands demos of learning-mode artifacts. That is an adaptation you can see next week.

You do not need Scrum events to do this. You need a clock, a named loop, and a single change that will still be true in seven days. If you *are* using Scrum, do not skip the retrospective because “we already had a critique.” Critique looks at the product. Retro looks at how you look. Both are gates. Neither is a therapy session.

Decision rule: the retro ends when one change is written as a next-loop rule (who, what, when), not when everyone has spoken. If nothing in cadence, WIP, DoD, review, or threshold will change, you did not inspect. You vented.

### Facilitation: a one-change retrospective
Protect this meeting from becoming a second critique of the product and from becoming a blame hour. Facilitator is not the person who failed the last test. Time-box to 40 minutes when the cycle is a week; shorter is allowed, longer usually means you are collecting a backlog of feelings.

| Clock | Move |
| --- | --- |
| 0:00–0:05 | Restate the two scoreboards for this cycle: tests completed (learning), DoD slices completed (feature). Numbers on the wall. No speeches yet. |
| 0:05–0:15 | Silent write: what in the *loop* (cadence, WIP, DoD, rooms, thresholds) made learning slow or shipping sloppy? Not names of villains. |
| 0:15–0:25 | Cluster. Kill clusters that are actually product wishes (“better pre-fill”). Keep clusters that are process (“we booked a demo before the RAT”). |
| 0:25–0:35 | Pick **one** change to the next loop. Write it as a rule: “No all-hands demos of learning-mode artifacts. Evidence tables only.” Owner, first date it applies. |
| 0:35–0:40 | Read last cycle’s one change. Did we do it? If not, it stays the only change. Do not stack. |

Decision rule for the facilitator: when a twelfth sticky appears, park it. Park is not a secret backlog of twelve. Park is “not this loop.” If last cycle’s change was not tried, you do not get a new one. Inspect-and-adapt requires the adapt to actually happen. Otherwise you are running a salon about salons.

After ship (Lesson 16), the same retro includes incidents, rollback drills, and support scripts. The loop now has operations in it. A retro that only talks about “how we felt in standup” while the on-call rota is a rumor has inspected the wrong artifact.

<figure class="fig">
<svg class="lesson-chart" viewBox="0 0 720 230" role="img" aria-label="Two scoreboards and three evidence moves">
  <rect x="20" y="18" width="330" height="88" rx="12" fill="var(--card)" stroke="var(--border)"/>
  <text x="185" y="48" text-anchor="middle" font-size="14" font-weight="700">Learning velocity</text>
  <text x="185" y="72" text-anchor="middle" class="muted" font-size="12">Units: tests with a pre-written bar</text>
  <text x="185" y="92" text-anchor="middle" class="muted" font-size="12">Kill / keep assumptions</text>
  <rect x="370" y="18" width="330" height="88" rx="12" fill="#1c5d68"/>
  <text x="535" y="48" text-anchor="middle" fill="#fff6d6" font-size="14" font-weight="700">Feature velocity</text>
  <text x="535" y="72" text-anchor="middle" fill="#c5eef2" font-size="12">Units: DoD-passing slices</text>
  <text x="535" y="92" text-anchor="middle" fill="#c5eef2" font-size="12">Users can touch them</text>
  <rect x="20" y="124" width="210" height="64" rx="10" fill="var(--card)" stroke="var(--border)"/>
  <text x="125" y="150" text-anchor="middle" font-size="13" font-weight="700">Persevere</text>
  <text x="125" y="170" text-anchor="middle" class="muted" font-size="11">Bet holds · keep approach</text>
  <rect x="255" y="124" width="210" height="64" rx="10" fill="#7eb8c4"/>
  <text x="360" y="150" text-anchor="middle" font-size="13" font-weight="700">Pivot</text>
  <text x="360" y="170" text-anchor="middle" font-size="11">Job alive · approach wrong</text>
  <rect x="490" y="124" width="210" height="64" rx="10" fill="#1c5d68"/>
  <text x="595" y="150" text-anchor="middle" fill="#fff6d6" font-size="13" font-weight="700">Kill</text>
  <text x="595" y="170" text-anchor="middle" fill="#c5eef2" font-size="11">Job dead · stop spending</text>
  <text x="360" y="214" text-anchor="middle" class="muted" font-size="12">Write the bar before the data. One retro change to the next loop. Do not report one scoreboard.</text>
</svg>
<figcaption>Two clocks, three sentences. “We iterated” is not a number. “We’ll know the threshold when we see the data” is a story waiting to happen.</figcaption>
</figure>

### Failure catalog
Reporting one scoreboard is the headline failure. “We iterated” with zero tests and zero DoD slices is empty. Writing the threshold after the data is storytelling. Calling a pivot a kill (or a kill a pivot) to save face blurs the job. Persevering because leadership is booked is sunk cost. A retro with twelve actions and no owner is a wishlist. A retro about who slipped is a trial. Demanding a randomized trial to change a subject line, or shipping a high door on five friends, mismatches the bar to the door. Counting WIP as feature velocity is how dashboards lie. Demoing a learning-mode artifact as if it were a DoD increment poisons both scoreboards at once.

A subtler failure: the team runs honest tests and then does not move. Threshold says pivot; calendar says persevere. The calendar is not evidence. If you will not obey the sentence you wrote, stop writing sentences. You are in a costume of empiricism.

**Uncertainty:** “Learning velocity” is teaching language, not a standard SI unit. Use it as a scoreboard name. Do not invent a formula and pretend the syllabus provided one. Pivot/persevere language is popular Lean Startup vocabulary; this pack keeps **kill** as a third sentence so pivot cannot hide a dead job. The Scrum Guide’s retrospective is cited as the inspect-and-adapt job of the loop, not as a requirement to adopt Scrum for the whole company.

## Worked example(s)
**Problem:** Findability tests, after the Lesson 13–14 redesign, passed **5/5** against a rule written in advance: *4/5 new contractors start the tax packet from the email in five minutes, unassisted.* Pre-fill Wizard-of-Oz, also with a bar written in advance (*4/5 unconfused and faster in one sitting*), helped **2/5** and confused **3/5**. Leadership wants “the AI onboarding” launched at the all-hands next week. The team’s dashboard shows 30 story points “done.” Support has no script. Nobody has written this week’s velocities as two numbers.

**Steps:**
1. **Split the scoreboards.** Learning: two tests finished. Findability bet: signal against a pre-written bar. Pre-fill bet: signal against a pre-written bar. Feature: **zero** DoD-passing increments users can touch — the points are WIP and looks-like, not ship. Report 2 tests / 0 slices, not “we were fast.”
2. **Read the thresholds before anyone interprets.** Findability: 5/5 meets 4/5 → **persevere** on that approach; you may solidify the link. Pre-fill: 2/5 fails 4/5 → **pivot** (job = unassisted packet completion is still alive; approach = model-pre-fill is wrong this cycle). Not kill: contractors still have the job. Not persevere: the bar was 4/5, not “we learned a lot.”
3. **Refuse the all-hands as a feature event.** Launching “the AI onboarding” would report a learning-mode artifact on the feature scoreboard. That is the injury. Leadership can hear the two numbers and the two sentences: findability perseveres; pre-fill pivots. Evidence table, not a model on stage.
4. **Match bars to doors.** Subject line and single link are a low door — 5/5 is enough to persevere on that slice. Pre-fill into the system of record is a medium-to-high door (wrong data, legal language, vendor). 2/5 does not open it. Do not “iterate the model on stage.”
5. **Retro, one change.** Cluster: all-hands slots overrode RAT last time (Lesson 13 had to kill a Thursday demo). The one change: **no all-hands demos of learning-mode artifacts; evidence tables only.** Owner: PM. Applies to next week’s all-hands. Park the other eleven stickies (“better recruiting,” “nicer Figma,” “legal office hours”).
6. **Write the next thresholds in the future tense, now.** Findability ship path (Lesson 16): “If DoD (mobile, unassisted, rollback, support script) is red, we do not ship the link even at 5/5 task success.” Pre-fill new loop: “If a redesigned, non-model approach (plain defaults, last-year copy-forward) does not hit 4/5 unconfused, we kill *that* approach too — we do not revive the model because it is cool.”

**Answer / result:** You persevered on findability, pivoted off pre-fill-as-product, and did not kill the onboarding job. You reported two scoreboards. The retro changed the next loop. That is inspect-and-adapt. The all-hands can wait for a slice that has a DoD.

## Key Terms
| Term | Definition |
|------|------------|
| Learning velocity | Rate of kill/keep on assumptions; units are tests, not tickets |
| Feature velocity | Rate of DoD-passing increments a user can touch |
| Test (as a unit) | Pre-written threshold, named audience, stop/go — not a meeting |
| DoD increment | Slice that meets the quality bar in the real hands of a user |
| Pivot | Job alive, approach wrong; change the bet in public |
| Persevere | Bet holds; keep the approach, maybe raise fidelity |
| Kill | Job or justifying assumption is dead; stop spending |
| Evidence threshold | Pre-written signal for persevere / pivot / kill, locked before data |
| Door | Cost of reversal if you are wrong; sets the height of the bar |
| Retrospective | Inspect the loop (cadence, WIP, DoD, review, threshold); adapt |
| One-change retro | A passing retro names exactly one next-loop rule with an owner |
| Storytelling | Writing the threshold after the data to save the plan |
| “We iterated” | Not a number; usually a costume for neither velocity |

## Misconception inventory
| Misconception | Reality |
|---------------|---------|
| “We iterated, so we delivered.” | Iteration can be learning with zero ship. Report both scoreboards. |
| “Shipping proves the idea.” | Shipping proves you can operate a slice. The idea still needs evidence. |
| “Pivot is a nicer word for fail.” | Kill is fail-the-job. Pivot is change-the-approach. Do not blur them to save face. |
| “We’ll know the threshold when we see the data.” | Then you will pick the story that saves the plan. Write it first. |
| “Retrospective is about who slipped.” | It is about the loop. People theater is not a retro. |
| “Twelve retro actions show we care.” | Twelve is a wishlist. One change that actually happens is a pass. |
| “n=5 is never enough, so we persevere.” | The bar was the bar. Do not raise it after a fail to protect the approach. |
| “A randomized trial is required to change a subject line.” | Match the bar to the door. Low doors may use a cheap probe. |
| “Story points done are feature velocity.” | Feature velocity is DoD-passing slices users can touch. Points can be WIP. |
| “Scrum retro is a Scrum-only ceremony.” | The Guide names inspect-and-adapt of the work system. The move travels. |

## Summary
- Learning velocity (tests) and feature velocity (DoD increments) are different scoreboards.
- Pivot = job alive, approach wrong. Kill = job dead. Persevere = bet holds. Three sentences.
- Write the evidence threshold before the data; read it aloud before anyone interprets.
- Match the height of the bar to the cost of being wrong.
- A retrospective inspects the loop and passes when one change hits the next cycle.
- “We iterated” is not a number. “We shipped” is not proof the idea was right.
- Do not demo learning-mode artifacts as if they were DoD increments.

## Practice
### Retrieval
- What are the units of learning velocity vs feature velocity?
- Pivot vs kill vs persevere: which part of the sentence changes?
- When must an evidence threshold be written?
- What makes a retrospective pass in this pack?
- Why match the bar to the door?
- What does the Scrum Guide’s retrospective inspect?

### Near transfer
A team has 30 story points “done,” zero user tests this month, and a plan to “pivot the AI” after a bad all-hands vibe. Which velocity are they reporting, which sentence are they misusing, and what do you add to the dashboard before anyone talks about pivot?

### Far transfer
This Atlas pack is about to be used in a hackathon demo. Write two scoreboards for last week’s authoring, one evidence threshold for the next prompt change (in future tense, with persevere/pivot/kill), and the single retro change you would make to the next lesson-writing loop.

## Spaced retrieval notes
- Day 0: split last week’s work into learning vs feature; put two numbers on a page.
- Day 2: write an evidence threshold for a live test *before* you run it, including the kill sentence.
- Day 7: run a retro with exactly one change; refuse a twelfth sticky.
- Day 21: catch a public “we iterated” and ask which scoreboard, which sentence, and which pre-written bar.

## Difficulty tiers
- **Novice:** two scoreboards; pivot vs persevere vs kill as three sentences.
- **Working:** thresholds written before data; bar matched to door; one-change retro.
- **Expert:** run dual-track after a persevere without starving tests or inflating feature velocity with WIP; hold a pivot in front of the people who booked the old approach.

## Domain scaffolds
Professional evidence: safety-critical and legal one-way doors get high bars and expert gates, not five-friend thumbs-up. Complicated payroll-like work may persevere on sequence and rehearsal rather than on BML theater. If your org reports a single velocity, still keep the second number even if it only lives on the team wall. A Scrum coat makes the retrospective a named event; the inspect-and-adapt job is still required if you are wearing a different coat.

## Learn more
- [Scrum Guide](https://scrumguides.org/scrum-guide.html) — Sprint Retrospective inspects individuals, interactions, processes, tools, and DoD, then adapts; Increment and DoD are the feature-velocity bar.
- [Agile Manifesto](https://agilemanifesto.org/) — responding to change is a value; it is not a license to skip a pre-written threshold.
- [Principles behind the Agile Manifesto](https://agilemanifesto.org/principles.html) — working software over theater; still count tests and slices separately.
- [Design Council — Framework for Innovation](https://www.designcouncil.org.uk/our-resources/framework-for-innovation/) — a failed diamond-2 test sends you back; that is a pivot or a kill, not “iteration” as a lifestyle.
- [Snowden & Boone, “A Leader’s Framework for Decision Making,” HBR](https://hbr.org/2007/11/a-leaders-framework-for-decision-making) — complicated vs complex still sets how high a door (and a bar) should be.
