# Cadence, Scope, WIP, and Definition of Done

## Learning Objectives
- Treat **cadence** as a heartbeat that makes inspection possible, not as a pressure pump that recovers a slipped date.
- Define **scope** as the work allowed into this cadence, and cut or defer it instead of “we’ll try.”
- Count **WIP** as started-not-done, and treat high WIP as delay rather than as productivity.
- Write a **Definition of Done** that can fail, matching the Scrum Guide’s commitment on the Increment.
- Run a 15-minute WIP-limit standup that only talks about finishing.
- Put two clocks and two DoDs on a sandwich without ranking a legal date against a product guess.
- Name which of the four levers is broken first when a board is busy and nothing is Done.

## Prerequisites
- L05: discovery vs delivery, sandwich, talk artifact.
- L06: Agile as values, Scrum as empiricism, sequence as an honest coat.
- You can open a board or a spreadsheet of live work and count how many items have started and not finished.

## Lesson Content

### Four levers, one steering wheel
Cadence, scope, WIP, and Definition of Done are how any coat in L06 actually steers. Without them, Agile is a mural, Scrum is a meeting series, and sequence is a Gantt that nobody updates. The four levers are not a fifth methodology. They are the dashboard.

**Cadence** is when you inspect. **Scope** is what you allowed into this inspect interval. **WIP** is how many things are started and not done. **Definition of Done** is the quality bar that makes “done” mean the same thing to everyone looking. Teams that only talk about velocity are reading a speedometer with no units. Teams that only talk about dates are using the pressure pump. The mechanism is visibility: you cannot adapt what you cannot see, and you cannot see unfinished work if “done” is a feeling and “in progress” is a lifestyle.

These levers apply on both tracks (L05) and on both coats (L06). Discovery needs a cadence that produces a **decision**, a scope of probes, a WIP limit on half-discoveries, and a “done” for a decision sentence. Delivery needs a cadence that produces an **increment**, a scope of earned slices, a WIP limit on half-builds, and a fail-able DoD. The sandwich needs two clocks more often than it needs two teams.

### Cadence is a heartbeat, not a pressure pump
A **cadence** is a regular inspect interval — daily, sprint, weekly discovery review, monthly ops — chosen so learning has a clock. The [2020 Scrum Guide](https://scrumguides.org/scrum-guide.html) calls Sprints the **heartbeat** of Scrum: fixed length, one month or less, a new Sprint immediately after the last. The Manifesto’s principles prefer shorter timescales and a **sustainable** pace that could continue indefinitely. Both are heartbeat language. Neither is “go faster until the date complies.”

A **pressure pump** is what teams do when a date slips: they shorten the Sprint, skip the retro, add nights, and call it commitment. That destroys the instrument. You can no longer tell throughput from panic. Quality decreases, which the Guide forbids during a Sprint. The next inspect is now comparing a hero week to a normal week and lying about both. Cadence exists so that Plan–Do–Check (Arc A) has a Check with a denominator. Random heroics are not cadence. A daily standup that reports busyness without a Done increment is not a heartbeat; it is a status tax.

Decision rule for cadence: **pick the slowest clock that still makes a dangerous surprise inspectable before it is expensive, then protect its length.** Payroll cutover risk may need daily. Portal findability may need a weekly decision review. Do not put both on a two-week Sprint merely because the department bought a tool. Do not compress either clock because a demo date moved. If the date and the heartbeat disagree, **cut scope** (next section). The date does not get to steal the metronome.

### Scope is what this cadence is allowed to hold
**Scope** is the work you are allowing into the current cadence. It is a permission, not a wish. Unmanaged scope is how a Sprint becomes a shopping list and how discovery becomes eight probes. The Scrum Guide already says that during a Sprint, scope may be clarified and renegotiated with the Product Owner as more is learned, **without endangering the Sprint Goal** and **without decreasing quality**. That is scope as a lever: it flexes so the goal and the DoD can hold.

“We’ll try” is not a scope decision. Trying is how WIP explodes. The honest verbs are **cut**, **defer**, and **split**. Cut: the AI helper is not in this cadence. Defer: pre-fill waits on a findability decision. Split: the payroll dry-run is in; the cutover weekend is a different clock. Discovery scope is the same grammar: this week’s probe is findability from the real inbox, not findability plus pre-fill plus copy tone plus a leadership storyboard.

Scope is also how dual-track stays honest. Delivery scope may include only **earned** slices plus the complicated core. Discovery scope may include only the decision you owe. If leadership adds a demo of unearned work, that is a scope change. Treat it as one. Either the demo becomes a working session on the decision (L06), or something else leaves the cadence. Adding the demo “on top” is the pressure pump wearing a calendar invite.

### WIP is started-not-done; high WIP is delay
**Work in progress (WIP)** is the count of things that have started and are not done. It is not a mood and not a column design. If eight tickets are “in progress,” WIP is at least eight, plus the pretotype you started in a side conversation, plus the slide deck that is “almost ready.” High WIP feels like productivity because starting is visible and finishing is slow. It is usually **delay**. Every started item wants attention, review, context, and a Done checklist. Attention does not stack.

A **WIP limit** is a decision rule: **start nothing new until something finishes.** The limit is a number the team can see without a dashboard vendor. A practical starting limit is “no more started items than people who can finish them,” and then lower. If you have five finishers and twelve started items, you are not busy. You are queued. Dual-track without a WIP limit collapses into eight half-discoveries and four half-increments, which is how both tracks fake motion.

WIP hides in costumes. “I’m blocked so I started something else” is how limits die. The repair is to finish or to return the item to not-started, not to mint a third. “Discovery doesn’t count as WIP” is how probes never decide. A probe that has started interviews and has no decision sentence is WIP. “The demo is extra” is how leadership work becomes a shadow board. Count it.

This atlas does not need a queueing-theory paper to use the lever. You can see it on any board: the age of the oldest started item is a better tell than the count of tickets moved this week. If the oldest item is older than the cadence, the heartbeat is inspecting a pile, not a slice.

### Definition of Done is fail-able
The Scrum Guide makes the **Definition of Done** the commitment for the Increment: a formal description of the state of the Increment when it meets the quality measures required for the product. The moment a Product Backlog item meets Done, an Increment is born. If it does not meet Done, it cannot be released or even presented at the Sprint Review; it returns to the Product Backlog. Developers are required to conform to it. Multiple teams on one product share one DoD at least as a minimum.

This lesson uses that meaning on every coat. **DoD is a checklist the team can fail.** If every item always “meets Done,” the checklist is a slogan. If Done is “QA will catch it,” Done has been outsourced to a future that never arrives. If Done is “looks good in the demo,” you have a narrator-dependent increment, which is not usable. Write Done as tests: mobile path for the primary task; unassisted completion; accessibility of the current stack; rollback named; no known statutory fake. Then actually fail items against it.

Discovery needs a cousin, not a fake DoD. A decision is “done” when a competent teammate can act on the sentence without you: who, job, bar, date, next probe or kill. That is not an Increment. Do not mix it into the delivery Done column. Two DoDs on a sandwich is normal: “payroll file matches the statute in a dry run” is not “a contractor starts the packet on a phone without a staff DM.” Using one Done column for both is how the legal date hides behind a green ticket.

Fail-able also means the Review cannot launder undone work. Leadership wanting to see the AI helper does not create an Increment. Show the decision, or show a slice that meets Done. The Guide already chose.

### Decision rules for the four levers
The four levers are not a menu you pick from for flavor. They are a repair order. Teams that reach for a new cadence every time a date slips are using the pressure pump. Teams that rewrite DoD as a pep talk are hiding WIP. The mechanism is still visibility: change the number you can see this afternoon, then protect the clock that will make next week comparable to this week.

Use the following as a wall script when the board is on fire. One change per day beats four slogans.

1. If a date and the heartbeat disagree → **cut scope**. Do not compress cadence. Do not lower Done.
2. If started-not-done exceeds the number of people who can finish → **WIP limit now**. Start nothing. Finish the oldest.
3. If “done” cannot fail → **rewrite DoD as a checklist** before you plan the next cadence. Metrics are lying.
4. If discovery and delivery share a Done column → **split the bars**. Decisions are not increments.
5. If a standup reports status by person → **replace it** with the 15-minute finishing script below.
6. If new work arrives mid-cadence → it enters only by **displacing** scope, and only if it does not endanger the Sprint Goal (or the sequence gate, on a core).
7. If heroics are required to hold the cadence → the coat is already off. Repair WIP and scope; do not celebrate the heroics as culture.

A useful order of operations when everything feels broken: **count WIP first**, because it is the fastest visible number. Then ask whether Done can fail. Then look at scope. Cadence is last to touch, because changing the metronome makes every other comparison dirty. If you change all four in one afternoon, you will not know which repair worked — and the next inspect will be another hero week with better vocabulary.

### Failure catalog
**Cadence as pressure pump.** Sprint shortened, retro skipped, nights added, quality quietly dropped. Repair: restore the length; cut scope; write the skipped Check as a miss.

**Scope as wish.** “We’ll try to get to the AI helper too.” Repair: try is not a verb on the brief. Cut, defer, or split.

**High WIP as pride.** Twelve in-progress tickets presented as utilization. Repair: limit; finish oldest; return extras to not-started.

**DoD as slogan.** A five-line quality poster no item has ever failed. Repair: fail one item this week on purpose against the list, or the list is fiction.

**DoD as QA at the end.** Testing after the cadence, Review of undone work. Repair: Done is the Increment’s commitment, not a phase.

**Standup as status tax.** Each person reports busyness to a manager. Repair: 15 minutes, oldest WIP first, finishing only.

**One clock for the sandwich.** Legal cutover and portal guesses share a two-week Sprint and a Done column. Repair: daily risk for the core, weekly decision review for the edge, two bars.

**Discovery WIP invisible.** Six probes, zero decisions, none on the board. Repair: count probes as WIP; a decision sentence is the finish.

**Demo scope on top.** Leadership meeting added without displacement. Repair: the demo *is* scope. It displaces, or it becomes a working session on the decision.

### Facilitation: 15-minute WIP-limit standup that only talks about finishing
This script fits the Daily Scrum timebox (15 minutes, same time and place, Developers adapting the next day’s plan toward the goal). It is a **tactic** for that timebox, not a replacement religion. Ban personal status rounds. Ban starting. The only interesting objects are items that have started and are not Done.

**Before 0:00 — Count.** A board or a paper list showing started-not-done, oldest at the top. If the count is over the WIP limit, the meeting has already decided: no new starts today. Write the number on the wall. If you cannot count WIP in thirty seconds, the board is not transparent (Scrum’s first empirical pillar).

**0:00–0:02 — Limit.** Read the count and the limit. If over: “We start nothing. We finish or we return.” If at or under: still start with the oldest, not with new ideas. If someone is “blocked,” they stay on the oldest item; they do not mint a side quest.

**0:02–0:10 — Oldest item only.** What would make this item meet **Done** today? Who is waiting on whom? What is the next physical action (a dry-run file, a five-contractor session scheduled, a rollback paragraph)? If the item cannot meet Done today, either split a finishable slice or name the impediment in one sentence. Do not solve the impediment in this meeting; name who will, by when today.

**0:10–0:14 — Next oldest, only if the first is unblocked.** Same questions. If you never leave the first item, that is information: WIP was a pile, not a portfolio. Discovery items use the decision-sentence cousin of Done: “what sentence could a teammate act on by end of day?”

**0:14–0:15 — One sentence.** “We will finish X before we start Y.” If Y is the leadership demo and X is findability, the sentence may be “we will finish the decision sentence; the demo will show that decision.” End. Conversations that need more than a minute happen after, among the people on the oldest item — not in a longer standup.

Failure of this facilitation: you heard from every person, you heard no Done, and two new tickets were created. Success: the oldest item moved, or returned to not-started, and nobody started a third thing.

<figure class="fig">
<div class="domain-row">
<div class="domain-card light"><div class="k">Heartbeat</div><p><strong>Cadence:</strong> a protected inspect interval.<br/><strong>Scope:</strong> what this interval is allowed to hold.<br/><strong>Tell it is working:</strong> you can compare this interval to the last one without a hero week in between.</p></div>
<div class="domain-card mod"><div class="k">Flow</div><p><strong>WIP:</strong> started-not-done. High WIP is delay.<br/><strong>Limit:</strong> start nothing new until something finishes.<br/><strong>Tell it is working:</strong> the oldest item is younger than the cadence.</p></div>
<div class="domain-card vig"><div class="k">Done</div><p><strong>DoD:</strong> a checklist the Increment can fail.<br/><strong>Guide:</strong> no Done, no Increment, no Review presentation.<br/><strong>Tell it is working:</strong> an item failed the list this month and returned to the backlog.</p></div>
</div>
<figcaption>Four levers, three cards: time, flow, quality. Scope lives with cadence; WIP is the delay you are pretending is utilization; DoD is the unit of progress.</figcaption>
</figure>

<figure class="fig">
<svg class="lesson-chart" viewBox="0 0 720 230" role="img" aria-label="High WIP delays finishing; a WIP limit and a fail-able DoD restore a heartbeat">
  <text x="180" y="28" text-anchor="middle" font-size="13" font-weight="700">No limit — eight started</text>
  <rect x="40" y="44" width="280" height="22" rx="4" fill="#1c5d68" opacity="0.35"/>
  <rect x="40" y="70" width="280" height="22" rx="4" fill="#1c5d68" opacity="0.45"/>
  <rect x="40" y="96" width="280" height="22" rx="4" fill="#1c5d68" opacity="0.55"/>
  <rect x="40" y="122" width="280" height="22" rx="4" fill="#1c5d68" opacity="0.65"/>
  <rect x="40" y="148" width="90" height="22" rx="4" fill="#2bb89a"/>
  <text x="85" y="164" text-anchor="middle" fill="#062f2c" font-size="11" font-weight="700">Done</text>
  <text x="180" y="196" text-anchor="middle" class="muted" font-size="11">Motion. Almost nothing finishes.</text>
  <text x="540" y="28" text-anchor="middle" font-size="13" font-weight="700">Limit 3 — finish then start</text>
  <rect x="400" y="44" width="280" height="22" rx="4" fill="#1c5d68"/>
  <rect x="400" y="70" width="280" height="22" rx="4" fill="#1c5d68" opacity="0.75"/>
  <rect x="400" y="96" width="280" height="22" rx="4" fill="#1c5d68" opacity="0.5"/>
  <rect x="400" y="122" width="180" height="22" rx="4" fill="#2bb89a"/>
  <rect x="400" y="148" width="180" height="22" rx="4" fill="#2bb89a"/>
  <text x="490" y="138" text-anchor="middle" fill="#062f2c" font-size="11" font-weight="700">Done</text>
  <text x="490" y="164" text-anchor="middle" fill="#062f2c" font-size="11" font-weight="700">Done</text>
  <text x="540" y="196" text-anchor="middle" class="muted" font-size="11">Fewer starts. More increments.</text>
  <text x="360" y="220" text-anchor="middle" class="muted" font-size="12">Cadence inspects the right-hand picture. The left-hand picture only inspects busyness.</text>
</svg>
<figcaption>WIP is the pile on the left. A limit does not make people lazy; it makes Done possible inside the heartbeat. DoD is what the green bars have to survive.</figcaption>
</figure>

### Two clocks, two DoDs on a sandwich
L05 split the sandwich; L06 split the coats; this lesson splits the metronomes. The complicated core (payroll file, legal date) often wants a **daily** inspect of risk and a DoD you can dry-run. The complex edge (findability, later pre-fill) wants a **weekly** decision review and, once a slice is earned, a delivery DoD a user can fail. Those clocks can share humans. They cannot share a Done column or a pressure pump.

When the leadership demo date arrives, it is a scope event, not a cadence event. You do not shorten the heartbeat to fit the invite. You decide what the working session will inspect: the cutover rehearsal, the findability decision, or a slice that already meets Done. [Nielsen’s heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/) can sit inside a portal DoD as expert quality (visibility of system status, error prevention, recognition rather than recall) without turning the Review into a lecture. They do not belong in the payroll file’s DoD. Different bars, different clocks, same brief.

**Uncertainty:** WIP limits are popular in Kanban teaching; this pack’s syllabus names WIP without a separate Kanban spec. Teach the move (count started-not-done; start nothing until something finishes). Do not invent a board-method credential. Cadence length in Scrum is specified (month or less); cadence length in discovery is a local choice as long as a decision still has a clock.

## Worked example(s)
**Problem:** After L05–L06, the contractor-onboarding sandwich is visible: payroll cutover sequenced, portal edge in discovery, AI helper a non-goal. Reality on Monday: the HR Digital board shows 23 items “in progress,” including tax-packet copy, pre-fill fields, an AI summary spike, three cutover subtasks, and a leadership-demo storyboard. There is no written DoD. The two-week Sprint is being “collapsed to nine days” because the demo invite moved up. Standup is a 35-minute person-by-person status round. New contractors still cannot finish required forms without Slack-DMing staff. Findability is still untested. Pre-fill quality is still unknown.

**Steps:**
1. Count WIP before arguing coats. Twenty-three started-not-done. Five people who can finish. The first lever is WIP, not motivation. Write “23 / limit 5” on the wall. Start nothing.
2. Restore cadence. Refuse the nine-day compression. The heartbeat stays two weeks for the edge’s decision clock; the core keeps a daily risk huddle. The demo date is **scope**, not a metronome. If Friday must happen, Friday inspects whatever will be Done or decided — not a shorter Sprint.
3. Write two fail-able DoDs. Payroll: “transform matches the statute in a dry run; rollback named in one paragraph; no production cute-fake.” Portal (for any increment that later gets earned): “a new contractor can start the packet from their phone, from their real inbox, without a staff DM; primary path keyboard-reachable; errors in user language.” Discovery-done cousin: “dated sentence a teammate can act on.”
4. Cut scope to what this cadence is allowed to hold. In: payroll dry-run to its DoD; findability probe **design** and the decision it owes (Arc C will run the sessions). Out: AI helper, leadership storyboard as a delivery item, pre-fill implementation. Pre-fill remains unearned. The demo, if it stays, is a working session on the decision and the cutover risk — two agenda blocks — and it **displaces** the storyboard ticket.
5. Run the 15-minute finishing standup. Oldest item first. If the oldest is the AI spike, return it to not-started (non-goal). If the oldest is a cutover subtask that can meet the payroll DoD today, finish it. Nobody reports “yesterday I…” as a person.
6. Check the sandwich clocks. Daily: cutover risks only. Weekly: did discovery produce the findability decision sentence? Do not rank those on one board as if they shared Done.
7. Name the lever that was broken first, in the brief: WIP, then missing DoD, then scope-as-wish, then cadence-as-pump. Repair in that order so the next inspect is comparable.

**Answer / result:** The steering wheel is back. Cadence is a heartbeat again. Scope is findability-decision plus payroll dry-run. WIP is forced down toward a limit. Two DoDs can fail. The leadership demo cannot launder undone AI work. Pre-fill quality is still unknown, and the levers are what keep that unknown from occupying twenty-three started tickets. Arc C can now run the smallest honest test on findability because this cadence actually has room.

## Key Terms
| Term | Definition |
|------|------------|
| Cadence | A regular, protected inspect interval; a heartbeat, not a pressure pump |
| Pressure pump | Shortening the interval, skipping inspect, or adding heroics to make a date comply |
| Scope | Work allowed into this cadence; cut, defer, or split — never “we’ll try” |
| Work in progress (WIP) | Count of started-not-done items, including shadow work |
| WIP limit | Decision rule: start nothing new until something finishes |
| Definition of Done | Fail-able quality bar; Scrum commitment that births an Increment |
| Increment | Usable stepping stone that exists only if it meets Done |
| Discovery-done | A dated decision sentence a teammate can act on without you |
| Oldest item | The started work with the most age; first object of a finishing standup |
| Sprint Goal | The objective that scope may flex around without a quality drop |
| Sustainable pace | Manifesto principle: a cadence you could hold indefinitely |
| Displacement | New mid-cadence work enters only by pushing something else out |

## Misconception inventory
| Misconception | Reality |
|---------------|---------|
| “More WIP means we are faster.” | More starts usually mean later finishes. Limit WIP. |
| “Cadence is how we apply deadline pressure.” | Cadence is how we see. Pressure pumps destroy the instrument. |
| “Scope is whatever leadership asked for this morning.” | Scope is a permission for this interval. New asks displace, or they wait. |
| “Definition of Done is for QA at the end.” | If DoD is late, every metric lies. No Done, no Increment. |
| “We’ll try to do it all this Sprint.” | Try is how WIP explodes. Cut or defer. |
| “Standup is when everyone reports status.” | 2020 Daily Scrum inspects progress toward the goal. This lesson’s tactic: finishing only. |
| “Discovery has no WIP.” | Unfinished probes are started-not-done. They need a decision clock. |
| “One DoD keeps us aligned.” | Payroll file-match and portal task-success are different truths. |
| “If we skip the retro we can hit the date.” | You skipped the inspect of the loop. The date will return. |
| “A green ticket means Done.” | If the checklist cannot fail, green is paint. |

## Summary
- Cadence is a heartbeat that makes Check possible. Compressing it to hit a date is a pressure pump.
- Scope is permission for this interval. The honest verbs are cut, defer, and split.
- WIP is started-not-done. High WIP is delay. A limit means start nothing until something finishes.
- Definition of Done is fail-able. It is the Scrum commitment on the Increment; undone work is not presented as one.
- A 15-minute standup that only talks about finishing is a tactic for the Daily Scrum timebox, not a status tax.
- Sandwiches often need two clocks and two DoDs. They do not need twenty-three started tickets.
- When everything is on fire, count WIP first, then ask whether Done can fail, then cut scope. Touch cadence last.

## Practice
### Retrieval
- What is the difference between a heartbeat and a pressure pump?
- Define WIP in one sentence. Why is high WIP usually delay?
- What does the Scrum Guide forbid you to do with an item that does not meet Done?
- Name the three honest verbs for scope.
- In the 15-minute script, what happens in the first two minutes if you are over the limit?
- Which lever do you touch last, and why?
- Why might discovery need a cousin of DoD rather than the delivery checklist?

### Near transfer
Your board has 23 in-progress items, no DoD, and a Sprint being shortened because a demo moved up. Which lever is broken first, what do you write on the wall this afternoon, and what is forbidden in tomorrow’s standup?

### Far transfer
A city permitting desk runs “Kanban” with no WIP limit and a quality bar that says “legal will review later.” Translate the four levers onto that desk. What is cadence, what is Done, and what would a 15-minute finishing standup refuse to hear?

## Spaced retrieval notes
- Day 0: count WIP on a live board, including off-board shadow work. Write the number.
- Day 2: write or fail a five-line DoD. If nothing can fail it, it is not a DoD yet.
- Day 7: run one 15-minute finishing standup. Note whether any new work started during it.
- Day 21: catch one pressure pump (shortened cadence, skipped retro, demo-on-top) and name the scope you would have cut instead.

## Difficulty tiers
- **Novice:** define the four levers; count WIP; refuse “we’ll try.”
- **Working:** write a fail-able DoD; run the 15-minute script; cut scope when a date and the heartbeat disagree.
- **Expert:** hold two clocks and two DoDs on a sandwich for a quarter without a pressure pump, and without discovery WIP going invisible.

## Domain scaffolds
Safety and legal cores: DoD includes rehearsal, rollback, and “no cute fake in production,” even if the product edge uses task-success as Done. Healthcare and finance: WIP limits apply to probes that could touch live data — started-not-done includes the half-connected vendor. Public sector: a statutory date is scope against a protected cadence, not a reason to skip inspect. If more than two boxes on the Arc D ops checklist would fail, you do not have Done, whatever the board says.

## Learn more
- [The 2020 Scrum Guide](https://scrumguides.org/scrum-guide.html) — Sprint as heartbeat; Definition of Done as the Increment’s commitment; Daily Scrum as 15-minute inspect toward the Sprint Goal; undone work not presented at Review.
- [Principles behind the Agile Manifesto](https://agilemanifesto.org/principles.html) — working software as measure; sustainable pace; frequent delivery; simplicity as work not done.
- [Manifesto for Agile Software Development](https://agilemanifesto.org/) — responding to change without dropping quality for a date.
- [Nielsen, 10 Usability Heuristics (NN/g)](https://www.nngroup.com/articles/ten-usability-heuristics/) — optional expert overlay inside a product DoD, not a substitute for task success.
