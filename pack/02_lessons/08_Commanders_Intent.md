# Commander’s Intent and the Brief

## Learning Objectives
- Write **commander’s intent** as purpose + end state + constraints so a competent teammate can act without further orders from you.
- Turn a complaint or a solution-noun into a **problem statement** that names who, job, and evidence of pain — with no smuggled solution.
- Write a **How Might We** that allows at least three structurally different answers, including one that is not software.
- Add **non-goals** and **success criteria** that keep this round honest, without letting vision replace the round.
- Produce a **brief** that can be read in three minutes and executed without you in the room.
- Tell **alignment** from **instruction**, and choose which the room needs.
- Facilitate a 25-minute brief-writing workshop that ends with a read-aloud, not with a longer document.

## Prerequisites
- L05–L07: discovery vs delivery, a coat for the sandwich, cadence/WIP/DoD as levers.
- Arc A: you can name the loop and whether the work is complicated or complex.
- You have given or received a request that failed because the “why” was missing, or because the “why” was a noun (“build a dashboard,” “make it nicer,” “add AI”).

## Lesson Content

### Alignment is not a longer instruction
**Instruction** tells someone the steps. It is correct for complicated, low-variance work: a runbook, a statute, a deploy checklist, the payroll-file transform against a known schema. Variance is expensive; the steps are the product. **Alignment** tells someone the purpose, the end state, and the constraints so they can choose steps you did not foresee. Variance is the point: a discovery week, a complex product bet, a contractor who does something weird with their phone. Most build-loop work needs alignment and only a little instruction. Teams that only instruct create bottlenecks and silent rebellion. Teams that only “align” with slogans create seven products.

The tell is disappearance. If you vanished for two days, could a competent teammate still move toward the end state without violating a constraint? If no, you instructed poorly or you never aligned. If yes, you wrote intent. Slack being down, a vendor lying, or a user taking an unexpected path are not edge cases. They are why alignment exists. A six-page instruction that still requires you to interpret every surprise is not safer than a one-page intent. It is a bottleneck with formatting.

Arc B’s job ends here: choose a coat (L05–L07), then write intent others can execute without you. Dual-track, Scrum, sequence, WIP limits — none of them survive a request that still says “make onboarding nicer.”

### Commander’s intent: purpose, end state, constraints
This pack borrows **commander’s intent** as a civilian alignment pattern from U.S. Army mission-command teaching in [ADP 6-0](https://armypubs.army.mil/). In that doctrine, intent is a clear and concise expression of the **purpose** of the operation and the desired **end state**, so subordinates can achieve the desired results **without further orders**, even when the operation does not unfold as planned. Mission command concentrates on the objective, not on how to achieve it. Mission orders focus subordinates on purpose rather than on the details of how to perform assigned tasks. Disciplined initiative is action in the absence of orders, when orders no longer fit, or when an unforeseen opportunity or threat appears.

That is not militarism, and this atlas is not military doctrine. It is what you want when the portal user does not follow the wireframe, the vendor times out, or you are in a meeting and the probe is happening anyway. **Purpose** is why this work exists for a human or a system. “So a new contractor finishes required forms without Slack-DMing staff” is a purpose. “Build a portal” is not. **End state** is what true looks like when you walk in later — observable. “A contractor completes the packet in one sitting, on their phone, in an observed trial” is an end state. “Modern UX” is not. **Constraints** are the hard walls: time, money, regulation, safety vetoes, non-goals you are willing to treat as walls. “No new vendor this sprint” is a constraint. “Make it pop” is a preference and does not belong here.

If you omit any of the three, people invent it. Missing purpose → they optimize a metric you did not care about (story points, a demo date). Missing end state → they never know they are done. Missing constraints → they ship a clever thing you must undo (a new vendor, PHI in a model, a payroll file “improved” on Thursday). Intent is complete only when a stranger could refuse a clever idea because it violates a wall you wrote.

### Problem statements without smuggled solutions
A **problem statement** names the who, the job, and the evidence of pain, **without a solution noun**. “New contractors cannot complete required tax forms without Slack-DMing a human; staff report this every week; leadership still asked for AI summaries” is a problem statement plus a political fact. “We need an AI helper” is a solution smuggled in. “We need Kubernetes,” “we need a dashboard,” and “we need to be Agile” are the same crime at three altitudes.

Smuggling is how diamond 1 (Arc A, Design Council **Define**) dies. The room never defines the challenge in a different way because the noun already picked diamond 2. Discovery (L05) cannot produce a decision if the decision was hidden in the problem sentence. Delivery will then build the noun to a DoD that has nothing to do with the pain.

The test: strip every product, vendor, and method word. If the sentence still names a person, a job they cannot finish, and a scrap of evidence, you have a problem statement. If it collapses, you had a shopping list. Write the problem **before** How Might We. Teams that start at HMW brainstorm decorations for an unstated problem. Evidence can be thin at the start of Arc B (“staff DMs are the current unblock”) and still be honest. Invented numbers are not evidence. “Users will love this” is not evidence.

### How Might We that allows three different answers
**How Might We (HMW)** is a bridge from problem to ideation. It keeps the who and the job, and it opens solution space. “How might we get a new contractor through required forms in one sitting without DMing staff?” is a HMW. Bad HMWs are either too broad (“how might we be a better team?”) or too narrow (“how might we build a red button on page 3 of the portal?”). Broad is a poster. Narrow is a leading question.

The test this atlas requires: a HMW should allow **at least three structurally different answers, including one that is not software**. Structurally different means a different kind of intervention, not three button colors. For the contractor packet, three that pass: (1) fix findability of the existing link in the real inbox; (2) pre-fill fields from the existing HRIS once findability holds; (3) a scheduled concierge hour or a single named human with a script — **not software**. A fourth that is also not the portal: rewrite the outbound email so the packet is the first tap, not the seventh. If every answer you can invent is a screen, the HMW smuggled a portal.

HMW is a diverge prompt (Arc A, Arc C). It is not a commitment. The brief holds the HMW so later generation has a job, not so engineering starts three answers. Non-goals will kill some answers before ideation. That is allowed. What is not allowed is a HMW that can only be answered by the solution already funded.

### Non-goals, success criteria, and vision that does not replace the round
**Non-goals** are in-scope-looking work you are explicitly not doing this round. They prevent polite scope creep. “Not building an AI helper this round” is a non-goal. “Not a marketing-site rewrite” is a non-goal. “Not a new vendor this sprint” can be written as a constraint or a non-goal; pick one slot and mean it. If it is not written, someone will start it on Thursday and call it initiative. Non-goals are how the Manifesto’s simplicity — maximizing the amount of work not done — becomes a sentence on a page.

**Success criteria** are how you will know the end state happened. Prefer user or system behavior over feelings. “4/5 observed trial users finish the packet unassisted on a phone” beats “stakeholders are excited.” “Payroll dry-run matches the statute” beats “cutover is green.” Write the bar **before** the test (Arc D will insist). If you write it after you see the data, you are storytelling. Success criteria are this-round. They are allowed to be smaller than the purpose. Purpose can be “finish without DMing staff”; this round’s criterion can be findability task-success, with pre-fill as a later bar.

**Vision** is the longer directional picture. It is allowed to be qualitative. It is not allowed to replace this-round success criteria. Vision without a round is a poster. A round without vision is a random walk. A brief that only has vision will be used to justify both the AI helper and the opposite of the AI helper. Put vision in one line if you must; put success criteria in a line you can fail.

### The three-minute brief
A **brief** packages intent for a working group so they can execute without you. Minimum contents:

- Purpose
- Problem statement
- How Might We
- End state
- Constraints
- Non-goals
- Success criteria
- Loop / coat / track (from L01–L07): what this cadence produces, heartbeat, DoD or decision-done
- Who decides

If the brief cannot be **read in three minutes**, it is a document pretending to be alignment. Length is not rigor. A brief that needs a narrator is not a brief yet. A brief that cannot be understood by the person who will sit with the contractor, the person who will dry-run the payroll file, and the person who owns the demo date is not shared understanding — it is a memo to self.

The brief is the talk artifact’s home (L05). Discovery writes decisions into it. Delivery writes Done and constraints into it. Coat names go on it only after the information problem (L06). Cadence, scope, WIP limit, and DoD are levers on it (L07), not a second document. When the operation does not unfold as planned — findability fails, the vendor lies — people act from this page without further orders. That is the ADP 6-0 sentence, civilianized.

### Alignment vs instruction in the room: a decision rule
Use **instruction** when variance is expensive: production deploy, dosing, a legal filing, the payroll cutover runbook, rollback. Write steps. Rehearse them. Do not “empower” someone to improvise a statutory file.

Use **alignment** when variance is the point: a prototype week, a discovery track, a complex product bet, a HMW that includes a non-software answer. Write purpose, end state, constraints. Do not micromanage the CSS.

Mixing them is a common injury. A manager “aligns” on a vision then specifies the button. A team “takes initiative” on a constraint they were not allowed to touch (new vendor, production probe of a one-way door). Mission command’s “disciplined” is the civilian word **walls**: initiative inside the constraints, not around them.

Decision rule:

1. If cause and effect are known and a wrong step is costly → **instruct** (runbook, sequence gates). Still write purpose so people know when to stop.
2. If cause and effect are not known and a competent teammate will see things you will not → **align** (intent + brief).
3. If you need both on a sandwich → **instruct the core, align the edge**, on the same page, in two blocks. Do not let the runbook colonize the portal, and do not let the HMW colonize the payroll file.
4. If the brief cannot be read in three minutes → you are hiding. Cut.
5. If people keep asking you for the next click → you instructed a complex job, or you aligned without an end state.

### Failure catalog
**Task list as intent.** “Build the portal, add AI, demo Friday” with no purpose. Repair: purpose + end state + constraints before any epic.

**Solution smuggled into the problem.** “We need AI summaries because onboarding is messy.” Repair: strip nouns; name who fails at which job.

**HMW as a leading question.** “How might we build a red button on page 3?” Repair: three structurally different answers, one non-software, or rewrite.

**Vision as this round.** A poster replaces success criteria. Repair: one fail-able bar for this cadence.

**Unwritten non-goals.** The AI helper starts on Thursday as “initiative.” Repair: write the non-goal; WIP-limit standup returns the ticket (L07).

**Brief as a deck.** Sixteen slides, narrator required. Repair: one page, three-minute read-aloud.

**Alignment theater, instruction in the hallway.** The brief says “you choose how”; Slack says “use this component.” Repair: put the real constraint on the page or stop pretending.

**Initiative around the walls.** A teammate adds a vendor because the end state was vivid and the constraint was a footnote. Repair: constraints at the top, not in the footer. ADP 6-0’s initiative is inside intent, not around it.

**One brief that is only instruction for the sandwich.** Payroll runbook used as the portal plan. Repair: two blocks, same page.

### Facilitation: 25-minute brief-writing workshop
Invite the people who will do the hours and the person who currently owns the demo date. One laptop or one wall. Ban solution nouns for the first eight minutes. The only success of this meeting is a brief that can be read aloud in three minutes. A longer document is a failed facilitation.

**0:00–0:03 — Read the complaint.** Out loud. Example: “Make the onboarding nicer. Also AI summaries. Demo this week.” Write it where everyone can see it. Name it as a complaint, not as a brief. Ban new nouns.

**0:03–0:08 — Purpose and end state, independently.** Two people write purpose in one sentence. Two others write end state in one sentence. Merge. Kill “modern,” “seamless,” “AI-powered,” “nice.” Purpose must name a human. End state must be observable when you walk in later. If they cannot merge in five minutes, you do not have shared purpose yet; that is already a finding.

**0:08–0:13 — Constraints and non-goals.** Hard walls only: time, vendor, identity provider, accessibility of the current stack, legal date on the payroll core. Preferences go in the bin. Non-goals: AI helper this round; marketing rewrite; new vendor. If someone fights a non-goal, they are asking for scope (L07). Make them displace something.

**0:13–0:18 — Problem then HMW.** Problem: who, job, evidence; no solution noun. Then HMW from that sentence. **Test immediately:** the room must produce three structurally different answers, including one that is not software. If they cannot, the HMW is too narrow. Rewrite once. Do not ideate further; Arc C owns generation.

**0:18–0:23 — Success criteria and coat.** One fail-able bar for this round (e.g., findability task-success in a later trial of five; this week, the decision sentence is the discovery-done). Name the coat and track: discovery floor on the edge; sequence on payroll; Scrum not worn until an Increment exists. Who decides: one name for the Product Goal-like call, one name for the cutover gate.

**0:23–0:25 — Three-minute read-aloud.** One person reads the brief. No narrator footnotes. If it overruns three minutes, cut sentences, do not schedule a follow-up document. If a competent stranger could not act, you are not done — you are out of time, which is information. Finish the cut after, in writing, same page.

<figure class="fig">
<svg class="lesson-chart" viewBox="0 0 720 250" role="img" aria-label="Intent stack from purpose down to tasks, with the brief as the portable form">
  <rect x="40" y="16" width="640" height="36" rx="8" fill="#1c5d68"/>
  <text x="360" y="40" text-anchor="middle" fill="#fff6d6" font-size="14" font-weight="700">Purpose — why a human should care</text>
  <rect x="70" y="58" width="580" height="36" rx="8" fill="#2bb89a"/>
  <text x="360" y="82" text-anchor="middle" fill="#062f2c" font-size="14" font-weight="700">End state — what true looks like later</text>
  <rect x="100" y="100" width="520" height="36" rx="8" fill="var(--card)" stroke="var(--border)"/>
  <text x="360" y="124" text-anchor="middle" font-size="14" font-weight="700">Constraints + non-goals — the walls</text>
  <rect x="130" y="142" width="460" height="36" rx="8" fill="var(--inset)" stroke="var(--border)"/>
  <text x="360" y="166" text-anchor="middle" font-size="14">Problem · HMW · success criteria · coat / track</text>
  <rect x="190" y="184" width="340" height="36" rx="8" fill="var(--card)" stroke="var(--border)"/>
  <text x="360" y="208" text-anchor="middle" font-size="14">Tasks / instruction — only after the stack</text>
  <text x="360" y="240" text-anchor="middle" class="muted" font-size="12">The brief is this stack on one page, readable in three minutes. Tasks without the stack are instruction pretending to be a plan.</text>
</svg>
<figcaption>Write top-down. ADP 6-0’s move, civilianized: purpose and end state so others can act without further orders. Constraints keep initiative disciplined. Tasks come last.</figcaption>
</figure>

<figure class="fig">
<div class="domain-row">
<div class="domain-card light"><div class="k">Alignment</div><p><strong>For:</strong> complex work, discovery, unnamed jobs.<br/><strong>Gives:</strong> purpose, end state, walls.<br/><strong>Pass:</strong> a teammate can move if you disappear for two days.</p></div>
<div class="domain-card mod"><div class="k">Instruction</div><p><strong>For:</strong> complicated work, one-way doors, runbooks.<br/><strong>Gives:</strong> steps, gates, rehearsal.<br/><strong>Pass:</strong> two people following the steps get the same file.</p></div>
<div class="domain-card vig"><div class="k">Brief</div><p><strong>For:</strong> the sandwich on one page.<br/><strong>Contains:</strong> both blocks, HMW with a non-software answer, fail-able success, who decides.<br/><strong>Pass:</strong> three-minute read-aloud, no narrator.</p></div>
</div>
<figcaption>Alignment and instruction are different jobs. The brief holds both when the program is a sandwich. Costume: slogans for the edge, improvisation for the statutory core.</figcaption>
</figure>

**Uncertainty:** “Commander’s intent” and “mission command” are Army language in [ADP 6-0](https://armypubs.army.mil/). This pack uses them as a civilian alignment pattern: purpose, end state, constraints, so others can act without you. It does not teach military decision-making, land operations, or a board-style recitation of the seven principles as a credential. Editions of ADP 6-0 differ in surrounding taxonomy; the move this lesson needs is stable: intent lets people act when the plan does not unfold as planned.

## Worked example(s)
**Problem:** “Make the onboarding nicer.” Product, design, and engineering each heard a different request. Leadership also asked for AI summaries and a demo date. After L05–L07 the sandwich is named (payroll cutover sequenced; portal edge in discovery; WIP being forced down; two DoDs). A two-week cadence starts Monday. Someone still forwards a Slack: “can we show the helper on Friday.” Arc B still does not know pre-fill quality and still does not know whether contractors can find the packet.

**Steps:**
1. Refuse the noun. Ask who fails today. New contractors cannot complete required tax/onboarding forms without Slack-DMing staff. That is the problem statement. “Nicer,” “AI,” and “portal” are smuggled solutions.
2. Purpose: a new contractor finishes required forms in one sitting without DMing staff.
3. End state: in observed trials, a new contractor completes the packet in one sitting, on their phone, with zero staff messages. This-round success criterion can be smaller: 4/5 unassisted completions is the bar once a slice is in trial; **this cadence’s** discovery-done is the dated findability decision, because findability is still untested.
4. Constraints: no new vendor this sprint; existing identity provider; accessibility of the current stack; payroll cutover date is a one-way door and is not a portal story. Non-goals: marketing-site rewrite; AI helper this round; pre-fill implementation until findability is earned.
5. HMW: “How might we get a new contractor through required forms in one sitting without DMing staff?” Three structurally different answers that must fit on the brief as proof the HMW is open: (a) make the existing packet findable from the real inbox; (b) pre-fill from HRIS after findability holds; (c) a concierge hour with a script — not software. If Friday needs a show, show these three and the decision rule, not a helper.
6. Coat and track on the same page. Edge: discovery floor; Agile values; Scrum wrapper off until an Increment exists. Core: sequence, daily risk, payroll DoD. WIP limit: start nothing until something finishes. Demo is a working session that displaces storyboard work.
7. Who decides: one name for “what is worth building on the edge,” one name for “cutover go/no-go.” Not a committee.
8. Read-aloud in three minutes. Cut adjectives until it fits. Success of the workshop: a stranger could execute the discovery sentence and refuse the AI helper without calling you.

**Answer / result:** The cadence is no longer “nicer onboarding.” It is an intent stack plus a measure plus two coats. Instruction (which CSS, which payroll transform step) can now be local, on the core. Alignment is already done, on the edge. Pre-fill quality remains unknown; the brief is what keeps it out of delivery. Arc C can generate and pretotype against this HMW. Arc D can ship a findability slice against this end state. The ADP 6-0 test, civilian: if you disappear for two days, the team still knows what true looks like and which walls they may not cross.

One-page brief (this round):

- **Purpose:** A new contractor finishes required forms in one sitting without DMing staff.
- **Problem:** New contractors cannot complete the tax packet without Slack-DMing a human.
- **HMW:** How might we get a new contractor through required forms in one sitting without DMing staff?
- **End state:** Observed unassisted completion on a phone; 4/5 is the trial bar when a slice is tested.
- **Constraints:** No new vendor; existing identity provider; current-stack accessibility; payroll date is a one-way door.
- **Non-goals:** Marketing rewrite; AI helper this round; pre-fill until findability is earned.
- **Success (this cadence):** Dated findability decision from a real inbox→link→form probe design; payroll dry-run meets its DoD.
- **Coat / track:** Sequence on payroll; discovery floor on the edge; two DoDs; WIP limit on.
- **Who decides:** Named edge owner; named cutover owner.

## Key Terms
| Term | Definition |
|------|------------|
| Commander’s intent | Purpose + end state + constraints so others can act without further orders from you |
| Purpose | Why the work exists for a human or system |
| End state | Observable picture of “true” when you walk in later |
| Constraints | Hard walls (time, law, safety, budget, vendor), not preferences |
| Problem statement | Who, job, evidence of pain; no smuggled solution |
| How Might We | Ideation prompt that keeps the job and allows multiple solution types |
| Non-goals | Plausible work explicitly out of this round |
| Success criteria | Observable tests that the end state, or this round’s slice of it, happened |
| Vision | Longer directional picture; does not replace this-round criteria |
| Brief | Short package of intent a working group can execute in three minutes of reading |
| Alignment | Shared purpose, end state, and constraints |
| Instruction | Specified steps for low-variance, expensive-variance work |
| Disciplined initiative | Action without you, *inside* the walls — not around them |

## Misconception inventory
| Misconception | Reality |
|---------------|---------|
| “If I specify every step, I have communicated.” | You instructed. Complex work still needs intent when the steps change. |
| “Vision is enough.” | Vision without this-round success criteria is a poster. |
| “How Might We can start from a solution we like.” | Then it is a leading question, not a HMW. |
| “Non-goals are negative and kill morale.” | Unwritten non-goals kill morale later, in the scope fight. |
| “Constraints are for project managers.” | Builders who ignore walls build undo-work. |
| “Alignment means consensus on every detail.” | Alignment is the stack. Details can disagree inside the walls. |
| “A long document is a brief.” | A brief is readable in three minutes. Length is not rigor. |
| “Purpose can be ‘deliver the epic.’” | That is a task. Purpose names a human or system outcome. |
| “Initiative means ignore the constraints if the end state is vivid.” | That is undisciplined. Intent includes the walls. |
| “The sandwich should pick alignment *or* instruction.” | Instruct the core, align the edge, same page. |

## Summary
- Alignment (intent) and instruction (steps) are different jobs; a sandwich often needs both on one page.
- Commander’s intent, civilianized from ADP 6-0, is purpose + end state + constraints so others can act without further orders.
- Problem statements forbid smuggled solutions; HMWs must allow at least three structurally different answers, including one that is not software.
- Non-goals and success criteria keep a round honest; vision does not replace them.
- A brief is the portable form. If it needs you in the room or more than three minutes to read, it is not a brief yet.
- Initiative is inside the walls. Constraints belong at the top, not in a footnote.
- Arc B’s output is a coat choice plus this brief. Arc C generates against the HMW; it does not invent a new purpose.

## Practice
### Retrieval
- Name the three parts of commander’s intent.
- What must a problem statement not include?
- What test must a How Might We pass in this lesson?
- Alignment vs instruction: give one tell for each, including the disappearance test.
- Why write non-goals instead of “we’ll see”?
- What is the time test for a brief?
- Where does disciplined initiative stop?

### Near transfer
Rewrite “build a dashboard for leadership” and “add AI summaries to onboarding” as: purpose, end state, one constraint, one non-goal, one problem statement, and one HMW that allows a non-software answer.

### Far transfer
You are handing this Atlas pack to a tester who was not in the chat. Write a six-line brief they could execute without you, including a non-goal and a success criterion they could fail.

## Spaced retrieval notes
- Day 0: take one Slack request and write purpose + end state only.
- Day 2: add constraints and a non-goal. Put them above the tasks.
- Day 7: convert a solution-noun request into a problem statement + HMW; force a non-software answer.
- Day 21: check a live brief with a three-minute read-aloud and the disappearance test. Cut until both pass.

## Difficulty tiers
- **Novice:** purpose, end state, one constraint; refuse a smuggled solution.
- **Working:** full brief including HMW (three-answer test), non-goals, success criteria, coat/track, who decides; 25-minute workshop.
- **Expert:** choose when to instruct vs align mid-incident on a sandwich without collapsing to either extreme, and without a narrator.

## Domain scaffolds
Professional briefs: one page. Safety, legal, and privacy constraints at the top, not in a footnote. If the domain is healthcare, finance, or law, the purpose line includes “educational / not advice” when that is true, and instruction (runbook) owns any one-way door. Do not HMW a statutory filing into a prototype. Public-sector work: the brief’s who-decides line must match actual authority, or initiative will bounce.

## Learn more
- [U.S. Army publishing directorate (ADP 6-0 home)](https://armypubs.army.mil/) — mission command and commander’s intent as the public home of the pattern; this pack uses the civilian move, not the field manual as a credential.
- [Scrum Guide (2020)](https://scrumguides.org/scrum-guide.html) — Product Goal as a named intent artifact; Sprint Goal as this-round intent; DoD as the quality wall.
- [Manifesto for Agile Software Development](https://agilemanifesto.org/) — customer collaboration and responding to change as alignment values; individuals over tools.
- [Design Council — Framework for Innovation](https://www.designcouncil.org.uk/our-resources/framework-for-innovation/) — Define as the home of the problem statement; people-first as purpose.
- [Principles behind the Agile Manifesto](https://agilemanifesto.org/principles.html) — simplicity as maximizing work not done (non-goals); regular reflect-and-tune.
