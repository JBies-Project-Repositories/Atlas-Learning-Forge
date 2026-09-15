# Communicating Intent

## Learning Objectives
- Write commander’s intent as purpose + end state + constraints, not as a task list.
- Turn a complaint into a problem statement and a How Might We without smuggling the solution.
- Use non-goals, success criteria, and vision as alignment tools, and tell alignment apart from instruction.
- Produce a brief that a competent teammate could execute without you in the room.

## Prerequisites
- Lessons 1–2: you can name the loop and the methodology coat.
- You have given or received a request that failed because the “why” was missing.

## Lesson Content

### Alignment is not a longer instruction
**Instruction** tells someone the steps. It is correct for complicated, low-variance work: a runbook, a statute, a deploy checklist. **Alignment** tells someone the purpose, the end state, and the constraints so they can choose steps you did not foresee. Most build-loop work needs alignment and only a little instruction. Teams that only instruct create bottlenecks and silent rebellion. Teams that only “align” with slogans create seven products.

The syllabus names **commander’s intent** because it is the cleanest professional pattern for alignment: a subordinate who loses contact with you should still be able to act in your interest. That is not militarism. That is what you want when Slack is down, the vendor lies, or the user does something weird.

### Commander’s intent: purpose, end state, constraints
**Purpose** is why this work exists for a human or a system. “So night-shift nurses can find the dosing note in under a minute” is a purpose. “Build a dashboard” is not.

**End state** is what true looks like when you walk in later. Observable. “A nurse can complete the task on a phone without calling the day shift” is an end state. “Modern UX” is not.

**Constraints** are the hard walls: time, money, regulation, non-goals, safety vetoes. Constraints are not preferences. “No PHI in the model vendor” is a constraint. “Make it pop” is a preference and does not belong here.

If you omit any of the three, people invent it. Missing purpose → they optimize a metric you did not care about. Missing end state → they never know they are done. Missing constraints → they ship a clever thing you must undo.

### Problem statements and How Might We
A **problem statement** names the who, the job, and the evidence of pain, without a solution noun. “On-call engineers lose 20 minutes finding the last good config, and two incidents last quarter started there” is a problem statement. “We need Kubernetes” is a solution smuggled in.

**How Might We (HMW)** is a bridge from problem to ideation. It keeps the who and the job, and it opens solution space: “How might we get the last good config into an on-call engineer’s hands in one minute?” Bad HMWs are either too broad (“how might we be a better team?”) or too narrow (“how might we build a red button on page 3?”). The test: a HMW should allow at least three structurally different answers, including one that is not software.

Write the problem statement before the HMW. Teams that start at HMW brainstorm decorations for an unstated problem.

### Non-goals, success criteria, vision, briefs
**Non-goals** are in-scope-looking work you are explicitly not doing this round. They prevent polite scope creep. “Not building SSO this quarter” is a non-goal. If it is not written, someone will start it on Thursday.

**Success criteria** are how you will know the end state happened. Prefer user or system behavior over feelings. “Five on-call drills retrieve the config without a second person” beats “stakeholders are excited.”

**Vision** is the longer directional picture. It is allowed to be qualitative. It is not allowed to replace this-round success criteria. Vision without a round is a poster. A round without vision is a random walk.

A **brief** packages intent for a working group: purpose, problem, HMW, end state, constraints, non-goals, success criteria, loop/method (from L01–L02), and who decides. If the brief cannot be read in three minutes, it is a document pretending to be alignment.

<figure class="fig">
<svg class="lesson-chart" viewBox="0 0 720 200" role="img" aria-label="Intent stack from purpose down to tasks">
  <rect x="40" y="20" width="640" height="36" rx="8" fill="#1c5d68"/>
  <text x="360" y="44" text-anchor="middle" fill="#fff6d6" font-size="14" font-weight="700">Purpose — why a human should care</text>
  <rect x="70" y="64" width="580" height="36" rx="8" fill="#2bb89a"/>
  <text x="360" y="88" text-anchor="middle" fill="#062f2c" font-size="14" font-weight="700">End state — what true looks like later</text>
  <rect x="100" y="108" width="520" height="36" rx="8" fill="var(--card)" stroke="var(--border)"/>
  <text x="360" y="132" text-anchor="middle" font-size="14" font-weight="700">Constraints + non-goals — the walls</text>
  <rect x="160" y="152" width="400" height="36" rx="8" fill="var(--inset)" stroke="var(--border)"/>
  <text x="360" y="176" text-anchor="middle" font-size="14">Tasks / instruction — only after the stack</text>
</svg>
<figcaption>Write the stack top-down. Tasks without the stack are instruction. The stack without any next action is a poster.</figcaption>
</figure>

### Alignment vs instruction in the room
Use instruction when variance is expensive: production deploy, dosing, a legal filing. Use alignment when variance is the point: a prototype week, a discovery track, a complex product bet. Mixing them is a common injury. A manager “aligns” on a vision then micromanages the CSS. A team “takes initiative” on a constraint they were not allowed to touch.

A practical tell: if you disappeared for two days, could a competent teammate still move toward the end state without violating a constraint? If no, you instructed poorly or you never aligned. If yes, you wrote intent.

**Uncertainty:** “Commander’s intent” is military language. This pack uses it as a civilian alignment pattern. It does not teach military decision-making or claim a specific field-manual text from the syllabus.

## Worked example(s)
**Problem:** “Make the onboarding nicer.” Product, design, and engineering each heard a different request. A two-week sprint starts Monday.

**Steps:**
1. Refuse the noun. Ask who fails today. New contractors cannot complete tax forms without Slack-DMing a human.
2. Purpose: contractors finish required forms without a human unblock.
3. End state: a new contractor completes the packet in one sitting, on their phone, with zero staff messages in a observed trial of five people.
4. Constraints: no new vendor this sprint; existing identity provider; accessibility of the current stack. Non-goal: marketing site rewrite.
5. HMW: “How might we get a new contractor through required forms in one sitting without DMing staff?”
6. Brief on one page. Success criterion: 4/5 trial users finish unassisted. Method: dual-track — pretotype the flow (L05) before polishing UI.

**Answer / result:** The sprint is no longer “nicer onboarding.” It is an intent stack plus a measure. Instruction (which CSS) can now be local. Alignment is already done.

## Key Terms
| Term | Definition |
|------|------------|
| Commander’s intent | Purpose + end state + constraints so others can act without you |
| Purpose | Why the work exists for a human or system |
| End state | Observable picture of “true” when you walk in later |
| Constraints | Hard walls (time, law, safety, budget), not preferences |
| Problem statement | Who, job, evidence of pain; no smuggled solution |
| How Might We | Ideation prompt that keeps the job and allows multiple solution types |
| Non-goals | Plausible work explicitly out of this round |
| Success criteria | Observable tests that the end state happened |
| Vision | Longer directional picture; does not replace this-round criteria |
| Brief | Short package of intent a working group can execute |
| Alignment | Shared purpose/end state/constraints |
| Instruction | Specified steps for low-variance work |

## Misconception inventory
| Misconception | Reality |
|---------------|---------|
| “If I specify every step, I have communicated.” | You instructed. Complex work still needs intent when the steps change. |
| “Vision is enough.” | Vision without this-round success criteria is a poster. |
| “How Might We can start from a solution we like.” | Then it is a leading question, not a HMW. |
| “Non-goals are negative and kill morale.” | Unwritten non-goals kill morale later, in the scope fight. |
| “Constraints are for project managers.” | Builders who ignore walls build undo-work. |
| “Alignment means consensus on every detail.” | Alignment is the stack. Details can disagree inside the walls. |
| “A long document is a brief.” | A brief is readable in minutes. Length is not rigor. |
| “Purpose can be ‘deliver the epic.’” | That is a task. Purpose names a human or system outcome. |

## Summary
- Alignment (intent) and instruction (steps) are different jobs.
- Commander’s intent = purpose + end state + constraints.
- Problem statements forbid smuggled solutions; HMWs open more than one kind of answer.
- Non-goals and success criteria keep a round honest; vision does not replace them.
- A brief is the portable form. If it needs you in the room, it is not a brief yet.

## Practice
### Retrieval
- Name the three parts of commander’s intent.
- What must a problem statement not include?
- Alignment vs instruction: give one tell for each.
- Why write non-goals instead of “we’ll see”?

### Near transfer
Rewrite “build a dashboard for leadership” as purpose, end state, one constraint, one non-goal, and one HMW.

### Far transfer
You are handing this Atlas pack to a tester who was not in the chat. Write a six-line brief they could execute without you.

## Spaced retrieval notes
- Day 0: take one Slack request and write purpose + end state only.
- Day 2: add constraints and a non-goal.
- Day 7: convert a solution-noun request into a problem statement + HMW.
- Day 21: check a live brief: could someone act if you disappeared for two days?

## Difficulty tiers
- **Novice:** purpose, end state, one constraint.
- **Working:** full brief including HMW, non-goals, success criteria.
- **Expert:** choose when to instruct vs align mid-incident without collapsing to either extreme.

## Domain scaffolds
Professional briefs: one page. Safety/legal constraints at the top, not in a footnote. If the domain is healthcare, finance, or law, the purpose line includes “educational / not advice” when that is true.

## Learn more
- [Agile Manifesto](https://agilemanifesto.org/) — customer collaboration and responding to change as alignment values.
- [Scrum Guide](https://scrumguides.org/scrum-guide.html) — Product Goal as a named intent artifact.
- [Design Council — Framework for Innovation](https://www.designcouncil.org.uk/our-resources/framework-for-innovation/) — define stage as the home of the problem statement.
