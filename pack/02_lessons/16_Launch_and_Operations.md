# Launch, Quality, Operations, Mode Switch

## Learning Objectives
- Treat launch as a per-slice mode switch: learning (change cheap) vs delivery (change expensive).
- Put quality in the Definition of Done at ship time, not in a hardening sprint after the tweet.
- Name operations as first-class: on-call, rollback, support script, vendor-fail behavior.
- Run a concrete ops/launch checklist covering accessibility, rollback, support, and monitoring before go.
- Kill eternal beta as a way of skipping operations, and kill “lock everything on day one” as a way of skipping learning.
- Facilitate a 20-minute go/no-go that can actually say no.
- Ship the findable slice and keep the unproven slice in learning mode without costumes.

## Prerequisites
- Lessons 13–15: a named end-move, three labeled review truths, and an evidence threshold you obeyed.
- Lesson 7–8: a Definition of Done that can fail, and a brief with constraints.
- Something on the table could actually leave the building this month — or honestly stay in the lab.

## Lesson Content

### Launch is a per-slice mode switch
**Launch** is not a party, not a tweet, and not a company-wide personality change. It is a **mode switch from learning to delivery for a slice**. During learning, change is cheap and expected: pretotypes, kills, pivots, subject lines you can revert before breakfast. After launch of a given slice, change is expensive: users now have a habit, data exists, support exists, a rollback has a blast radius. You may still learn — but that learning is a **new loop with a new brief**, not a silent rewrite of the live thing.

The move is FOR localizing the switch. Teams that “stay in beta forever” are avoiding operations. Teams that “lock everything” on day one are avoiding learning. Neither is a mode. Both are fear. The switch is **per slice**, not per company. Findability can be in delivery while pre-fill is still in learning. Payroll cutover can be in delivery from the first rehearsal because the door is one-way. A homepage experiment can stay in learning beside a live checkout. If your org talks about “we launched” as a single past-tense event for the whole product, they are using a party noun for a set of slice decisions.

Decision rule: name the slice and the mode in one sentence before anyone books a slot. “Findability link: delivery this week. Pre-fill: learning, new brief.” If you cannot split the sentence, you are about to ship a costume or hide from ops. The all-hands is not the slice.

### Learning: change is cheap. Delivery: change is expensive
Cheap change means a wrong subject line costs an email. Expensive change means a wrong subject line now trains 400 contractors, hits a support queue, and pollutes the metric you wanted to learn from. The cost is not moral. It is operational. Once a slice is live, every silent tweak is a change to someone else’s Tuesday. That is why delivery gets a DoD, a rollback, and a person who wakes up.

The move is FOR stopping two abuses. Abuse one: staying in learning language so nobody has to write on-call or a support script (“it’s just a beta”). Abuse two: jumping a guess into delivery so nobody has to be wrong in public (“it’s live, so it must be right”). Lesson 15 already forbade reporting one scoreboard. This lesson forbids wearing one mode as a coat for the whole board.

Decision rule: if reversal still costs less than a support ticket, you may stay in learning. If reversal now costs a ticket, a legal trail, a broken habit, or a vendor call, you are in delivery whether or not you said “beta.” Beta is not a mode. Beta is a label. The mode is the cost of change. Ask: “If we are wrong at 9 a.m., who does what by 9:15?” If the answer is “we’ll figure it out,” you are not in learning. You are in unowned delivery.

Keep a learning track beside a live slice when the product still has unknown jobs (dual-track from Lesson 5). Keep a delivery/ops track for the known slice. Do not starve ops to fund the next pretotype. Do not freeze all learning because one slice shipped. The handshake is the brief: new unknown, new loop, new threshold. The live slice keeps its DoD.

### Quality is DoD at ship, not a hardening sprint after the tweet
**Quality** at ship time is the Definition of Done plus the constraints from the brief. It is not a polish pass after the tweet. It is not a “hardening sprint.” If quality is a phase after “dev done,” you never had a DoD. You had a hope that someone else would finish the work under a different calendar. Users do not live in your phases. They meet whatever you actually shipped.

The move is FOR making fail-able quality the gate of launch. Accessibility, mobile, unassisted completion, logging, rollback, support — if they matter, they are in DoD *now*, or they are a lie. A team that ships and then “does a11y” is announcing that some people were not users at launch. A team that ships and then “writes the runbook” is announcing that operations was optional. Optional operations is how a prototype escapes.

Decision rule: the go/no-go reads the DoD as a checklist that can fail, not as a vibe. Any red item is a no-go for that slice, or an explicit, written exception with an owner and a date — and exceptions are not for safety, legal, or “we’ll add rollback later.” If the tweet is already drafted, the tweet is a sunk cost. Sunk costs are not quality. Pull the tweet.

DoD is allowed to be small. Small and true beats large and theatrical. “Works on the contractor’s phone, one link, packet named in the subject, keyboard reachable, rollback = revert the template, support script of ten lines, log of clicks on the link” is a DoD. “World-class UX, AI-grade, delightful” is not a DoD. You cannot no-go a slogan.

### Operations is what keeps the thing true after launch
**Operations** is what keeps the slice true after it leaves the building: who is **on-call**, what the **rollback** is, what the **support script** says, what happens when the **vendor fails**. A product that cannot be operated is a prototype that escaped. Escape is not a launch. It is a future incident with a marketing site.

On-call is a named human (or rota) who knows the slice, the rollback, and the support script. “The team” is not a name. A Slack channel with 40 people is not a rota. Rollback is a rehearsed action with a time bound: revert the email template, flip the link, disable the vendor flag — and a way to know it worked. Support script is the words a tired person says at 11 p.m. when a contractor cannot find the packet: what to try, when to escalate, what not to promise. Vendor-fail is the path when HRIS, email, or the identity provider is down: queue, message, do-not-silently-retry, who calls whom.

The move is FOR putting those four next to the brief *before* go, not in the incident review after. If any of the four is “we’ll figure it out,” the mode switch has not happened. You are still in learning, or you are in denial. Denial ships.

Decision rule: no go if on-call, rollback, support script, or vendor-fail is unnamed. You may ship a *smaller* slice whose ops you can name. You may not ship a larger story whose ops you admire in the abstract. Operations is part of the brief’s constraints (Lesson 8), not a surprise from another department.

### Ops/launch checklist: accessibility, rollback, support, monitoring
This checklist is the mechanism for Lesson 16. It is not decoration. Read it in the go/no-go. Every line is a yes, a no, or a dated exception. No is a no-go for the slice. “N/A” is allowed only with a reason that would survive a contractor at 11 p.m.

<figure class="fig">
<div class="fitt-grid">
<div class="fitt-cell"><strong>Accessibility</strong>Keyboard can reach the packet. Name of the job is visible without color alone. Phone zoom does not hide the link. Unassisted end state includes people who are not your demo user. If you need WCAG conformance, the expert already signed; Nielsen’s ten are not that signature.</div>
<div class="fitt-cell"><strong>Rollback</strong>Named action (revert template / flip flag / restore last email). Who runs it. How you know it worked. Rehearsed once, not imagined. Time bound (minutes, not “next sprint”). Data trail of who changed what.</div>
<div class="fitt-cell"><strong>Support</strong>Ten-line script: what the contractor tries, what the agent tries, what not to promise (no “the AI will pre-fill”). Escalation name. Hours the slice is claimed to work. Ticket tag so you can count harm.</div>
</div>
<div class="fitt-grid" style="margin-top:0.5rem">
<div class="fitt-cell"><strong>Monitoring</strong>One live signal that the slice is working (link clicks, start-of-packet events, error rate). One live signal that it is harming (support tag, bounce, 500s). Who looks, how often, what threshold pages on-call.</div>
<div class="fitt-cell"><strong>On-call</strong>Named rota for the first 72 hours, then the steady rota. Not “the team.” Handoff note. Backup if the named person is on a plane.</div>
<div class="fitt-cell"><strong>Vendor-fail</strong>What users see if email, HRIS, or identity is down. Queue vs fail-visible. Who calls the vendor. Do not silently retry a signature. Do not pretend pre-fill is up if HRIS is down.</div>
</div>
<figcaption>If a cell is red, the slice stays in learning or shrinks until the cell can go green. Eternal beta is what you say when you skip this figure.</figcaption>
</figure>

Decision rule: four red cells mean you do not have a launch. You have a demo with extra DNS. Shrink the slice until the checklist is honest. Shipping findability with a revertible email template is a real launch. Shipping “AI onboarding” with no script and no rollback is a party.

Accessibility sits here because unassisted was in the brief. If the end state was “complete the packet unassisted,” a launch that only works for the demo laptop has not met DoD. Monitoring sits here because Lesson 3’s Check and Lesson 4’s Measure do not retire at ship. They change clothes: the measure is now an operational signal, not only a test count.

### Eternal beta skips operations
“We’re still in beta” is often a way to skip the checklist. Users are already depending on the slice. Support is already answering. Change is already expensive. You just refused to name a rota. Eternal beta is unowned delivery. It is not a learning mode. Learning mode has cheap reversal and a threshold. Eternal beta has users and no rollback.

The opposite injury is also in this lesson: locking everything on day one so nobody can run a new loop beside the live slice. That is unowned fear. A live findability link does not forbid a pretotype of a non-model pre-fill in a lab. It forbids silently rewriting the live link as if it were still paper. New unknown, new brief, new threshold, new RAT. The shipped slice keeps its DoD while the lab works.

Decision rule: if a stranger can depend on it, it is in delivery and needs ops, no matter what the banner says. If nobody can depend on it and reversal is cheap, it is in learning and should not be announced as shipped. Banners do not change the mode. Dependence does.

### Facilitation: a 20-minute go/no-go launch review
This is a gate, not a pep rally. Facilitator is not the person who booked the all-hands. The only artifact in the room is the brief, the evidence threshold result (Lesson 15), the DoD, and the ops/launch checklist. No walkthrough of the pretty shell. No “quick look at the model.” Twenty minutes is enough if the work was done. If the work was not done, twenty minutes is enough to say no.

| Clock | Move |
| --- | --- |
| 0:00–0:03 | Name the slice and the mode. “We are asking to switch **findability** into delivery. Pre-fill is not in this question.” If someone adds a second slice, split or stop. |
| 0:03–0:07 | Evidence: read the pre-written threshold and the number. If the bar was not met, **no-go**. Do not renegotiate the bar in this room. |
| 0:07–0:12 | DoD checklist out loud. Any red is a no-go or a written exception that is not allowed to cover rollback, legal, safety, or a11y-of-the-end-state. |
| 0:12–0:17 | Ops/launch checklist: accessibility, rollback, support, monitoring, on-call, vendor-fail. Name the humans. If a name is “the team,” it is red. |
| 0:17–0:20 | **Go or no-go** for this slice only. Write it on the brief. If go: first hour owner, rollback owner, support owner. If no-go: what cell must turn green, by when. No “soft launch” as a third option unless it has the same ops as a go. |

Decision rule for the facilitator: “soft launch,” “dark launch,” and “beta to a few contractors” are still delivery if those contractors can depend on the slice. They inherit the checklist. If you cannot staff ops for 400 people, you also cannot staff it for 40 unless you have a named cohort, a rollback, and a script. Shrinking the audience without shrinking the ops fantasy is how betas escape.

If leadership is in the room, they get a vote only as payer/blocker (Lesson 14), not as a vibe. A payer can no-go for funding. They cannot go around a red rollback cell. The facilitator says that once. Then the clock owns the room.

<figure class="fig">
<svg class="lesson-chart" viewBox="0 0 720 210" role="img" aria-label="Per-slice mode switch from learning to delivery">
  <rect x="20" y="28" width="300" height="120" rx="12" fill="var(--card)" stroke="var(--border)"/>
  <text x="170" y="58" text-anchor="middle" font-size="14" font-weight="700">Learning mode</text>
  <text x="170" y="86" text-anchor="middle" class="muted" font-size="12">Tests · pretotypes · kill/pivot</text>
  <text x="170" y="108" text-anchor="middle" class="muted" font-size="12">Scoreboard: learning velocity</text>
  <text x="170" y="130" text-anchor="middle" class="muted" font-size="12">Change is cheap</text>
  <rect x="400" y="28" width="300" height="120" rx="12" fill="#1c5d68"/>
  <text x="550" y="58" text-anchor="middle" fill="#fff6d6" font-size="14" font-weight="700">Delivery mode</text>
  <text x="550" y="86" text-anchor="middle" fill="#c5eef2" font-size="12">DoD · quality · operations</text>
  <text x="550" y="108" text-anchor="middle" fill="#c5eef2" font-size="12">Scoreboard: feature velocity</text>
  <text x="550" y="130" text-anchor="middle" fill="#c5eef2" font-size="12">Change is expensive</text>
  <path d="M320 88 H400" stroke="#7a4e10" stroke-width="4"/>
  <text x="360" y="78" text-anchor="middle" font-size="11" fill="#7a4e10" font-weight="700">launch</text>
  <text x="360" y="178" text-anchor="middle" class="muted" font-size="12">The switch is per slice. A new brief starts a new learning loop beside the live slice.</text>
  <text x="360" y="198" text-anchor="middle" class="muted" font-size="12">Eternal beta skips ops. A hardening sprint after the tweet means DoD was never real.</text>
</svg>
<figcaption>Do not stay in the left box to avoid a rota. Do not jump to the right box to avoid being wrong. Go/no-go reads the checklist, not the tweet.</figcaption>
</figure>

### Failure catalog
Launch as a party is the visible failure: balloons, no rollback. Adjacent: quality as a hardening sprint after “dev done”; eternal beta as skipped ops; locking the whole product on day one so no new loop can sit beside the live slice; shipping the interesting slice (pre-fill) because the boring slice (the link) is not demoable; a go/no-go that cannot say no because the all-hands is booked; on-call = “the team”; monitoring = a dashboard nobody pages; accessibility promised next quarter; support script replaced by “they’ll figure it out”; vendor-fail unimagined until the vendor fails; Nielsen’s ten used as a fake a11y pass at the gate; “soft launch” as a third option with zero ops.

The quiet failure is mixing modes in one announcement. “We launched AI onboarding” when you switched a link into delivery and left the model in the lab. The sentence teaches the organization the wrong product. Then you cannot kill the model, because you already launched it in language. Name the slice in the sentence you send.

**Uncertainty:** “Launch” in companies often means marketing. This pack teaches the **mode switch**. You may still have a party. The party is optional. The checklist is not. On-call practices vary; this pack requires a named human and a rehearsed rollback, not a particular vendor’s incident tool.

## Worked example(s)
**Problem:** Lesson 15 persevered on findability (5/5 against a pre-written bar) and pivoted off pre-fill (2/5 confused, bar was 4/5). Leadership still wants “the AI onboarding” at the all-hands next week. Support has no script. DoD does not mention accessibility or rollback. The email vendor has gone down twice this quarter. Engineering can ship a better subject line and a single deep link tomorrow. The model cannot meet DoD and should not.

**Steps:**
1. **Split the sentence.** Findability: candidate for delivery. Pre-fill: stays in learning with a new brief (non-model approach or a later RAT). The all-hands, if it happens, hears a task-success number and a mode sentence — not a model on stage (Lesson 15’s retro rule).
2. **Write a small, fail-able DoD for the findability slice.** Mobile email, packet named in the subject, one link to the packet, first field reachable by keyboard, unassisted start still the end state, logging of link-follow, no pre-fill promises in the copy. Quality is this list at ship, not a hardening week after the all-hands.
3. **Fill the ops/launch checklist before the 20-minute gate.** Accessibility: a11y expert already attempted keyboard and zoom (Lesson 14); remaining issues are not “next quarter.” Rollback: revert the email template to last week’s digest; owner = the integrator who can publish templates; rehearsal is a draft send to the team. Support: ten-line script that never mentions AI; escalate to HR ops; ticket tag `packet-find`. Monitoring: count of link-follows vs invites; page if follows drop to zero while invites fire. On-call: named person for 72 hours, backup named. Vendor-fail: if email is down, do not silently claim the packet was sent; visible queue, who calls the vendor.
4. **Run the 20-minute go/no-go.** Slice = findability only. Evidence bar met. DoD read aloud. Checklist named with humans. Any red (no script, no rollback owner) is a **no-go** even at 5/5 task success — 5/5 was learning evidence, not operations. If the cells go green: **go**. First-hour owner watches the follow count. Rollback owner stays reachable.
5. **Refuse the costume.** If leadership asks to “just show the wizard while we’re up there,” that is a learning-mode artifact in a delivery slot. It re-teaches the wrong product. Offer the table. Keep pre-fill in the lab. A new loop may test copy-forward defaults later, with a new threshold, without touching the live link silently.
6. **After go, the retro includes incidents.** Next cycle’s one change might be “vendor-fail message is in the template, not in a wiki.” Feature velocity may now count **one** DoD slice. Learning velocity is a separate column for the pre-fill loop. Do not merge them because the all-hands wants a single victory.

**Answer / result:** You launch something true — a findable packet with a rota, a revert, a script, and a signal — and you keep something uncertain in the lab. That is the mode switch. Eternal beta would have shipped neither ops nor honesty. The all-hands can live without a fake AI.

## Key Terms
| Term | Definition |
|------|------------|
| Launch | Per-slice mode switch from learning to delivery |
| Mode switch | Learning (change cheap) vs delivery (change expensive) |
| Learning mode | Tests, pretotypes, kill/pivot; reversal is cheap |
| Delivery mode | DoD, quality, operations; reversal has blast radius |
| Quality | DoD + brief constraints at ship time, not a later phase |
| Operations | On-call, rollback, support script, vendor-fail after launch |
| On-call | Named human or rota who can run rollback and the script |
| Rollback | Rehearsed revert with a time bound and a way to know it worked |
| Support script | Words and steps for the first tickets; what not to promise |
| Vendor-fail | Visible path when a dependency is down; no silent retry of harm |
| Monitoring | Live signal of working and of harm, with a page threshold |
| Eternal beta | Users depend on it, but you skipped ops by keeping a banner |
| Go/no-go | Timed launch review that can say no; checklist, not a pep rally |
| Soft launch | Still delivery if people can depend on it; inherits the checklist |

## Misconception inventory
| Misconception | Reality |
|---------------|---------|
| “Launch is a party.” | Launch is a mode switch. The party is optional. |
| “Quality is a hardening sprint after launch.” | If it is after, it was never in DoD. |
| “Stay in beta so we can keep learning.” | Eternal beta is often a way to skip operations. Dependence sets the mode. |
| “Lock everything on day one so production is safe.” | Then you skip learning. Switch per slice; new unknowns get new briefs. |
| “On-call is ‘the team.’” | On-call is a name, a backup, and a rehearsal. |
| “We met task success, so we ship.” | Task success is learning evidence. Ops and DoD still have to go green. |
| “Soft launch means we don’t need rollback.” | If people can depend on it, it is delivery. |
| “We’ll write the support script when tickets appear.” | Then the first contractors are your authors. Write it before go. |
| “Accessibility is a later expert pass.” | Unassisted was in the brief. A11y is in DoD at ship, or the end state was a lie. |
| “Announcing the model and shipping the link is fine.” | Language teaches the product. Name the slice you actually switched. |

## Summary
- Launch is a per-slice mode switch, not a company-wide party or a banner.
- Learning keeps change cheap; delivery makes change expensive — because people now depend on it.
- Quality is DoD at ship, not a hardening sprint after the tweet.
- Operations (on-call, rollback, support, vendor-fail, monitoring, accessibility) is first-class on the checklist.
- Eternal beta skips ops; locking everything skips learning. Neither is a mode.
- A 20-minute go/no-go can say no. Soft launch still inherits the checklist.
- Ship the findable slice; keep the unproven slice in the lab without a costume.

## Practice
### Retrieval
- What becomes expensive after a slice launches, and why is the switch local?
- What is quality at ship time, if not a later phase?
- Name four operations artifacts that must exist before go.
- Why is eternal beta not a learning mode?
- What is the facilitator’s job when someone offers “soft launch” as a third option?
- Which scoreboard does a launched slice join, and which one does the lab keep?

### Near transfer
A team wants to “launch AI onboarding” at all-hands. The only DoD-ready work is a better email link. There is no support script and no rollback owner. Write the mode sentence, the go/no-go result, and the one checklist cell that must turn green before any go.

### Far transfer
This Atlas pack is about to be used offline at a hackathon. Which slice is in delivery mode (must work without a network story) vs learning mode (prompt still in refinement)? Write a six-cell ops/launch checklist for the delivery slice, including who is “on-call” for a broken `00_CLICK_HERE_TO_BEGIN.html`.

## Spaced retrieval notes
- Day 0: name one live thing as learning vs delivery; write the cost of changing it tomorrow.
- Day 2: fill the six-cell checklist for a slice you might ship this month; mark reds honestly.
- Day 7: run a 20-minute go/no-go on paper, including a forced no-go if any cell is red.
- Day 21: for one live slice, write rollback + support + vendor-fail in one paragraph and name the on-call human.

## Difficulty tiers
- **Novice:** launch = per-slice mode switch; quality = DoD now; eternal beta is skipped ops.
- **Working:** ops/launch checklist; 20-minute go/no-go that can say no; ship one slice, lab the other.
- **Expert:** dual-track after ship without starving ops or freezing learning; refuse costume announcements that teach the wrong product.

## Domain scaffolds
Professional shipping: operations and quality are part of the brief’s constraints, not a surprise from another department. Safety-critical slices may be in delivery mode from day one (rehearsal, not pretotype) and still run a go/no-go on rollback. Complicated payroll-like work uses sequence plus launch rehearsal, not eternal BML. Accessibility is method at ship, not a heuristic sticker. If marketing owns the word “launch,” keep the mode-switch word on the team wall anyway.

## Learn more
- [Scrum Guide](https://scrumguides.org/scrum-guide.html) — Increment and Definition of Done are the quality bar at the end of the cycle, not a later hardening phase; retrospective continues after ship.
- [Agile Manifesto](https://agilemanifesto.org/) — working software and responding to change still need a mode switch when change gets expensive.
- [Principles behind the Agile Manifesto](https://agilemanifesto.org/principles.html) — continuous attention to technical excellence is DoD, not a tweet-week cleanup.
- [Design Council — Framework for Innovation](https://www.designcouncil.org.uk/our-resources/framework-for-innovation/) — Deliver closes diamond 2 for a slice; it is not a skip of Discover/Define, and it is not eternal beta.
