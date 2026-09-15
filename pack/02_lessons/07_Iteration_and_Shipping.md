# Iteration and Shipping

## Learning Objectives
- Tell learning velocity from feature velocity and refuse to report one as the other.
- Use an evidence threshold to pivot or persevere, then run a retrospective that changes the next loop.
- Treat launch as a mode switch from learning to delivery: quality and operations become first-class.
- Kill the habit of “one more experiment” when the remaining work is complicated operations.

## Prerequisites
- Lessons 1–6: you can name the loop, the brief, the test, and a review move.
- Something on your plate could actually ship in the next month.

## Lesson Content

### Two velocities, two scoreboards
**Learning velocity** is how fast you kill or keep assumptions. Its units are tests, not tickets. A week with three honest pretotypes and one kill is fast learning even if the backlog did not grow.

**Feature velocity** is how fast you add done increments that users can touch. Its units are DoD-passing slices. A week with twelve “in progress” AI ideas and zero done is not feature velocity. It is WIP.

The injury is reporting learning as if it were delivery (“we iterated”) or reporting delivery as if it were learning (“we shipped so we must have been right”). Executives will ask for both. Give them two numbers. If you only have one number, you will optimize theater.

### Pivot vs persevere and evidence thresholds
**Persevere** means the bet still holds; keep the approach, maybe raise fidelity. **Pivot** means the job is alive but the approach is wrong; change the bet without pretending it was the plan all along. **Kill** (from L06) means the job is dead.

You cannot pivot vs persevere on vibes. An **evidence threshold** is written **before** the test: what signal, in whom, would make us persevere, pivot, or kill. Example: “If fewer than 3/5 contractors start the packet in five minutes, we pivot from pre-fill to findability; if 0/5 care about the packet at all, we kill the epic.” If you write the threshold after you see the data, you are storytelling.

Thresholds should match the risk. A legal one-way door needs a higher bar than a copy change. Do not demand a randomized trial to move a button, and do not ship a medical-adjacent workflow on five friends’ thumbs-up.

### Retrospective, quality, operations, launch
A **retrospective** inspects the **loop**, not the people. What in our cadence, WIP, DoD, or review made learning slow or shipping sloppy? One change to the next loop is a passing retro. A retro that produces twelve actions is a wishlist.

**Quality** at ship time is the DoD plus the constraints from the brief. It is not a polish pass after the tweet. If quality is a phase after “dev done,” you never had a DoD.

**Operations** is what keeps the thing true after launch: who is on call, what the rollback is, what the support script says, what happens when the vendor fails. A product that cannot be operated is a prototype that escaped.

**Launch** is a **mode switch from learning to delivery**. During learning, change is cheap and expected. After launch of a given slice, change is expensive: users now have a habit, data exists, support exists. You may still learn — but that learning is a new loop with a new brief, not a silent rewrite of the live thing. Teams that “stay in beta forever” are avoiding operations. Teams that “lock everything” on day one are avoiding learning. The switch is local to a slice, not to the company.

<figure class="fig">
<svg class="lesson-chart" viewBox="0 0 720 210" role="img" aria-label="Mode switch from learning to delivery">
  <rect x="20" y="30" width="300" height="120" rx="12" fill="var(--card)" stroke="var(--border)"/>
  <text x="170" y="60" text-anchor="middle" font-size="14" font-weight="700">Learning mode</text>
  <text x="170" y="88" text-anchor="middle" class="muted" font-size="12">Tests · pretotypes · kill/pivot</text>
  <text x="170" y="110" text-anchor="middle" class="muted" font-size="12">Scoreboard: learning velocity</text>
  <text x="170" y="132" text-anchor="middle" class="muted" font-size="12">Change is cheap</text>
  <rect x="400" y="30" width="300" height="120" rx="12" fill="#1c5d68"/>
  <text x="550" y="60" text-anchor="middle" fill="#fff6d6" font-size="14" font-weight="700">Delivery mode</text>
  <text x="550" y="88" text-anchor="middle" fill="#c5eef2" font-size="12">DoD · quality · operations</text>
  <text x="550" y="110" text-anchor="middle" fill="#c5eef2" font-size="12">Scoreboard: feature velocity</text>
  <text x="550" y="132" text-anchor="middle" fill="#c5eef2" font-size="12">Change is expensive</text>
  <path d="M320 90 H400" stroke="#7a4e10" stroke-width="4"/>
  <text x="360" y="80" text-anchor="middle" font-size="11" fill="#7a4e10" font-weight="700">launch</text>
  <text x="360" y="185" text-anchor="middle" class="muted" font-size="12">The switch is per slice. A new brief starts a new learning loop beside the live slice.</text>
</svg>
<figcaption>Do not report one scoreboard. Do not stay in the left box to avoid ops, or jump to the right box to avoid being wrong.</figcaption>
</figure>

### Cadence after ship
Keep a learning track (dual-track from L02) if the product still has unknown jobs. Keep a delivery/ops track for the known slice. Retrospectives now include incidents, not only feelings. Evidence thresholds for the live slice include harm: rollback criteria are part of the brief.

**Uncertainty:** “Learning velocity” is teaching language, not a standard SI unit. Use it as a scoreboard name. Do not invent a formula and pretend the syllabus provided one.

## Worked example(s)
**Problem:** Findability tests passed 5/5. Pre-fill Wizard-of-Oz helped 2/5 and confused 3/5. Leadership wants “the AI onboarding” launched at the all-hands next week. Support has no script. DoD does not mention accessibility or rollback.

**Steps:**
1. Two scoreboards. Learning: findability bet persevered; pre-fill bet should **pivot** (not kill the epic). Feature: nothing that meets a ship DoD exists yet.
2. Evidence threshold already written: pre-fill needed 4/5 unconfused. 2/5 fails it. Do not “iterate the model on stage.”
3. Launch decision: ship the **findability** slice only (better link, one sitting, support script). That is delivery mode for a small slice. Pre-fill stays in learning mode with a new brief.
4. Quality/ops: write DoD (mobile, unassisted, rollback = revert the link). Name who answers the first five contractor tickets.
5. Retro: one change — no all-hands demos of learning-mode artifacts. That is the loop fix.

**Answer / result:** You launch something true and keep something uncertain in the lab. That is the mode switch. The all-hands can hear a task-success number instead of a fake AI.

## Key Terms
| Term | Definition |
|------|------------|
| Learning velocity | Rate of kill/keep on assumptions (tests, not tickets) |
| Feature velocity | Rate of DoD-passing increments users can touch |
| Pivot | Job alive, approach wrong; change the bet |
| Persevere | Bet holds; keep the approach, maybe raise fidelity |
| Evidence threshold | Pre-written signal for pivot / persevere / kill |
| Retrospective | Inspect the loop; one change to the next cycle |
| Launch | Mode switch from learning to delivery for a slice |
| Quality | DoD + brief constraints at ship time, not a later phase |
| Operations | On-call, rollback, support, vendor-fail behavior after launch |
| Mode switch | Learning (change cheap) vs delivery (change expensive) |

## Misconception inventory
| Misconception | Reality |
|---------------|---------|
| “We iterated, so we delivered.” | Iteration can be learning with zero ship. Report both. |
| “Shipping proves the idea.” | Shipping proves you can operate a slice. The idea still needs evidence. |
| “Pivot is a nicer word for fail.” | Kill is fail-the-job. Pivot is change-the-approach. Do not blur them to save face. |
| “We’ll know the threshold when we see the data.” | Then you will pick the story that saves the plan. |
| “Retrospective is about who slipped.” | It is about the loop. People theater is not a retro. |
| “Stay in beta so we can keep learning.” | Eternal beta is often a way to skip operations. |
| “Quality is a hardening sprint after launch.” | If it is after, it was never in DoD. |
| “Launch is a party.” | Launch is a mode switch. The party is optional. |

## Summary
- Learning velocity and feature velocity are different scoreboards.
- Write evidence thresholds before tests; then pivot, persevere, or kill.
- Retrospectives change the next loop; they do not assign blame.
- Launch switches a slice into delivery: quality and operations count.
- Do not demo learning-mode artifacts as if they were shipped.

## Practice
### Retrieval
- Units of learning velocity vs feature velocity?
- What must be written before you can pivot vs persevere honestly?
- What makes a retrospective pass?
- What becomes first-class after launch?

### Near transfer
A team has 30 story points “done” and zero user tests this month. Which velocity are they reporting, and what do you add to the dashboard?

### Far transfer
This Atlas pack is about to be used in a hackathon demo. Which slice is in delivery mode (must work offline) vs learning mode (prompt still in refinement)? Write one evidence threshold for the next prompt change.

## Spaced retrieval notes
- Day 0: split last week’s work into learning vs feature.
- Day 2: write an evidence threshold for a live test before you run it.
- Day 7: run a retro with exactly one change.
- Day 21: for one live slice, write rollback + support in one paragraph.

## Difficulty tiers
- **Novice:** two scoreboards + pivot vs persevere.
- **Working:** evidence thresholds + launch as mode switch.
- **Expert:** run dual-track after ship without starving ops or freezing all learning.

## Domain scaffolds
Professional shipping: operations and quality are part of the brief’s constraints, not a surprise. Safety-critical slices may be in delivery mode from day one (rehearsal, not pretotype). Complicated payroll-like work uses sequence + launch rehearsal, not eternal BML.

## Learn more
- [Scrum Guide](https://scrumguides.org/scrum-guide.html) — Increment, DoD, retrospective.
- [Agile Manifesto](https://agilemanifesto.org/) — working software and responding to change; still needs a mode switch.
- [Design Council — Framework for Innovation](https://www.designcouncil.org.uk/our-resources/framework-for-innovation/) — deliver as the second diamond’s close, not as a skip of the first.
