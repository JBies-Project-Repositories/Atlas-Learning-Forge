# User, Stakeholder, and Expert Review

## Learning Objectives
- Run user testing as task success against a named rule, not as a compliment session.
- Name payers, blockers, and integrators before a stakeholder review, and ask them only the questions they can answer.
- Run expert review for legal, safety, accessibility, and security as veto-capable gates, not as late decoration.
- Use Nielsen’s ten usability heuristics as an expert overlay — rules of thumb, not a WCAG audit.
- Separate the three reviews into different meetings when power would fake the result.
- Refuse to sit a user and their boss in the same room and call the smiles evidence.
- Feed all three truths into Lesson 13’s named end-move without averaging them.

## Prerequisites
- Lesson 8: a brief with purpose, end state, constraints, and success criteria.
- Lesson 12–13: a smallest honest test and a critique that can end in a named move.
- You can tell a person who *has the job* from a person who *pays for the job*.

## Lesson Content

### Three reviews, three truths
**User testing** asks a person who has the job to do the job. **Stakeholder review** asks someone who pays, blocks, or integrates. **Expert review** asks someone with domain method (legal, safety, accessibility, security — and, in this pack, a usability-heuristic overlay). These three produce different truths. A stakeholder smile is not task success. An expert’s “this is noncompliant” can veto a loved prototype. A user’s success can still die in a stakeholder review if you never wrote the constraint.

The move is FOR keeping those truths from contaminating each other. Mixing them feels efficient. It is how you get a meeting where the contractor cannot fail the task in front of the VP who championed the design, the lawyer is too polite to veto in front of a smiling user, and the note that leaves the room is “went well.” That sentence is not evidence. It is a social success.

Decision rule: one room, one question, one kind of truth. If you need all three this week, you need three meetings, or at least three clearly separated blocks with different people. Do not average the outputs. Sequence them: users tell you whether the job can be done; experts tell you whether the job may be done; stakeholders tell you whether the job will be funded, unblocked, and plugged into the real system. Lesson 13’s named move sits after the truths, not during them.

If someone says “let’s just get everyone in a room and iterate,” they are asking for a town hall. Town halls are for announcements. Reviews are for signals that can change spend.

### User testing is task success, not a compliment
User testing is not a focus group, not a demo, and not “we showed it to some people.” It is a person who has the job attempting the job under a **named rule**. **Task success** is binary-ish: did they complete the job without help, in a time you named, by a criterion you wrote down before they sat? Opinions after the task are extra. Opinions instead of the task are not a test. “They said it was nice” is a compliment. Compliments do not clear a RAT.

The move is FOR watching behavior you claimed would happen. You sit down, you give the task in the user’s words, you shut up, you watch. You do not narrate the interface. You do not rescue at thirty seconds because the silence is awkward. You do not recruit your project manager’s roommate unless that roommate has the job. Five people with the job and a fail rule beat twenty people with opinions.

Write the rule before the session (Lesson 15 will make this a habit for pivot/persevere; here it is already required for honesty). Example: “A new contractor, from the real onboarding email on their own phone, starts the tax packet within five minutes without a hint. Success = the first form field is focused. Fail = they ask for help, abandon, or open the wrong packet.” Now you can count. 4/5 fail is a number. “Pretty good energy in the room” is not.

Decision rule: if you cannot write the success/fail line in one sentence, you are not ready to schedule users. You are ready to write the sentence. If the session cannot fail — because you will help, because the task is a tour, because the participant is the champion — cancel. A user test that cannot fail is a sales call.

### Writing the named rule, then shutting up
The named rule has four parts: **who** (the person with the job, not a proxy), **task** (the job in their words), **success** (observable, timed if time is the risk), and **help policy** (when, if ever, you may speak). “Talk aloud” is allowed. “Let me just show you” is not. After the task, you may ask what they thought they were looking for. That is diagnosis. It is not a substitute for the count.

Recruit like the job, not like convenience. New contractors, not the HR business partner who designed the packet. Tired people at 11 p.m. if that is when they on-board. Phone if that is the device. A lab with a ring light and a laptop on a stand will lie about findability if the real path is a forwarded email on a small screen. Fidelity of the *situation* matters more than fidelity of the pixels (Lesson 11).

Take notes on attempts, errors, and time-to-start, not on how charming the participant was. A single session is a story. Three to five with the same rule is a signal for a RAT. You do not need a university sample size to stop a bad spend. You need a pre-written fail line and the courage to use it. If 4/5 cannot find the packet, you do not “hear that the brand is confusing” and solidify. You redesign findability or you kill the approach.

Decision rule: help only when the written help policy says so — for example, after two minutes of stop, and then you mark the task failed. Rescuing to protect the author’s feelings is how every test “passes.” The author’s feelings are not the measure.

### Stakeholder review: payers, blockers, integrators
A **stakeholder** in this pack is not “anyone with an opinion.” It is someone who **pays**, **blocks**, or **integrates**. Payers fund the next increment or can starve it. Blockers can say no with force that survives a smile (legal hold, security review, union rule, payroll calendar). Integrators must plug your slice into a real system of record — HRIS, identity, email, the vendor that actually sends the W-9. If a person is none of the three, they may still be a user or an expert. They are not a stakeholder. Inviting them to “stakeholder review” dilutes the questions.

The move is FOR getting the constraints and the yes/no that users cannot give you. Users cannot tell you whether finance will pay for a support queue. Users cannot tell you whether identity will federate the contractor account in time. Stakeholders cannot tell you whether a tired contractor can find the link. Ask each party the question they can answer. A stakeholder review that starts with a high-fidelity walkthrough and ends with “love it, ship it” has asked the wrong question of the wrong people.

Name them on the brief before the meeting: who pays, who blocks, who integrates, what each is being asked, what would count as a yes. “Do we still fund findability work this month?” is a payer question. “Will you block launch if the form language stays as-is?” is a blocker question. “Can the email template carry one deep link by Thursday without breaking the digest?” is an integrator question. “Isn’t the AI demo cooler?” is not a question. It is a preference trying to sit in a gate.

Decision rule: do not ask stakeholders to play user. If they insist on “putting themselves in the contractor’s shoes,” hand them the task-success table instead of the prototype. Their shoes are not the job. If a stakeholder is also an expert (the lawyer is both blocker and expert), still separate the *legal veto* from the *funding nod* in the notes. One body, two truths. Write both.

### Expert review: legal, safety, accessibility, security
**Expert review** asks someone with domain method to try the artifact against a standard you cannot invent in a critique. **Legal** reads the form language, the retention, the signature, the “I agree.” **Safety** reads the harm if the action is wrong. **Accessibility** reads whether a person using a keyboard, a screen reader, a phone, or extra time can do the job you claimed was unassisted. **Security** reads identity, data leaving the building, vendor access, logs. These people can veto a loved prototype. That is the point. Inviting them after the launch date is printed is how you get a veto as a crisis.

The move is FOR catching one-way doors while they are still doors. A pretotype can fake a button. It cannot fake a statute. If the riskiest assumption is “this language is allowed,” the smallest honest test is counsel, not five contractors guessing. If the assumption is “a keyboard-only user can reach the packet,” the test is an expert with a keyboard, or a user who actually uses one — not a heuristic hand-wave from a designer who tabbed once.

Book experts before the date is a tattoo. Give them the brief, the question, and the artifact, not a sales narrative. Ask for a written veto/no-veto against named constraints. “Looks fine” from a lawyer in a hallway is not expert review. “I will not block if you change clause 4 and keep PII off the model vendor” is expert review. Put the veto on the brief as a constraint so Lesson 16’s launch cannot “forget.”

Decision rule: expert veto beats user delight and stakeholder enthusiasm. You may still redesign. You may not ship around a safety or legal no. If the expert is late because you invited them late, the delay is yours. Do not call it bureaucracy.

### Nielsen’s ten heuristics as an expert overlay — not WCAG
Jakob Nielsen’s [ten usability heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/) are an expert overlay this pack actually names. They are **rules of thumb** for a usability-informed look. They are **not** WCAG, not a legal accessibility audit, not a security review, and not a substitute for task success. A heuristic pass with a failed task is still a failed RAT. A heuristic fail can still explain *why* the task failed, which is useful for redesign.

The ten, used as questions against the artifact and the brief:

1. **Visibility of system status** — does the person know where they are in the packet and whether the save worked?
2. **Match between system and the real world** — does it say “tax packet” in the language contractors use, or “HRIS onboarding payload”?
3. **User control and freedom** — can they undo a wrong form, or did you trap them?
4. **Consistency and standards** — do the email, the portal, and the form call the same thing the same name?
5. **Error prevention** — do you stop a submit that will bounce, or do you punish after?
6. **Recognition rather than recall** — is the packet visible, or must they remember a URL from yesterday’s slide?
7. **Flexibility and efficiency of use** — does a returning contractor have a shorter path, without making the first-timer hunt?
8. **Aesthetic and minimalist design** — is the extra chrome stealing the only job on the screen?
9. **Help users recognize, diagnose, and recover from errors** — does the error name the missing field in words a human can use?
10. **Help and documentation** — if help is required, is it in the moment, or a PDF nobody will open?

Use them in an expert review with a person who can say “this heuristic is violated *and* it will fail the named task.” Do not use them as a 10-row score that ships at 7/10. Heuristics do not average. One fatal miss (no status, no name of the packet, no recovery) is a redesign. They also do not replace accessibility method. Contrast, keyboard, and screen-reader issues can sit under several heuristics and still need an a11y expert. If you need WCAG conformance, book that expert. Do not pretend Nielsen is that expert.

Decision rule: heuristic review is allowed as a cheap expert overlay *before* you spend users, and as diagnosis *after* a task fails. It is not user testing. It is not a certificate.

### Do not mix user and boss in one room
Power fakes success. A contractor will not fail a task honestly in front of their boss who championed the design. They will smile, they will guess, they will say it is nice, and they will call HR on Saturday anyway. A junior designer will not steelman a kill in front of the payer who flew in for the demo. A lawyer will soften a veto if the user in the chair is already performing gratitude. This is not a character flaw. It is what power does to speech.

The move is FOR protecting the signal. Separate meetings when power mixes. User testing: the person with the job, a facilitator, maybe a silent note-taker who is *not* their manager. Stakeholder review: payers/blockers/integrators, the evidence table, no recruited users as props. Expert review: the expert and the artifact, without a cheering section. If logistics “require” one room, you do not have logistics. You have a show. Cancel the show.

Facilitator script if someone tries to merge: “We will not get a true fail in this mix. We can do users at 10, experts at 11:30, payers at 1. If we only have one hour, we do users and we send the table. We will not sit the contractor next to the VP.” Then stop talking. The silence is the protocol.

Decision rule: if a boss, champion, or payer will be visible to the user during the task, the session is not user testing. Label it a demo. Demos do not clear a RAT.

### Facilitation: three rooms, no contamination
Run the week as three clocks, not as one “review day” with a guest list. The facilitator (not the champion) owns the invites, the named question, and the ban on mixing. Below is a working pattern when all three are due before a Lesson 13 end-move. Times are short on purpose. Long reviews wander into redesign-by-committee.

**Room A — User testing (45 minutes per person, 3–5 people, not a group).**

| Clock | Move |
| --- | --- |
| 0:00–0:03 | Restate who, task, success, help policy. No tour. |
| 0:03–0:08 | Consent, device, real starting point (the email, not your Figma). |
| 0:08–0:30 | Task. Facilitator silent. Mark success/fail against the named rule. |
| 0:30–0:40 | Diagnosis only: “What were you looking for?” Do not sell. |
| 0:40–0:45 | Thank, release, write the row in the table before the next person. |

**Room B — Expert review (40 minutes).** Heuristic overlay plus the veto domain you actually booked (legal, a11y, security, safety). Give them the brief and the artifact 24 hours ahead if the domain is legal. In the room: they speak first. You do not demo. You ask for veto / no-veto / conditions. Nielsen’s ten are a checklist for the usability expert, not a script for the lawyer.

**Room C — Stakeholder review (25 minutes).** Open with the task-success table and the expert conditions, not with slides. Ask payers, blockers, and integrators their three questions. Do not ask them if they “like” it. Close with what they just committed: fund, block, or plug in.

After the three rooms, *then* run Lesson 13’s 35-minute critique on the evidence, or skip straight to the named end-move if the RAT already spoke. Do not bring users back to watch the stakeholders argue. Do not bring stakeholders into the user hour “just to observe” if the user can see them. Observing is still power.

Decision rule: notes from each room stay labeled. Never write “the review said.” Write “users: 1/5 started in five minutes. Legal: veto on clause 4. Payer: funds findability, not the model, this month.” The named move is a function of those sentences, not of the average mood.

<figure class="fig">
<div class="domain-row">
<div class="domain-card light"><div class="k">User</div><p>Person with the job attempts the job. Named success/fail rule. Count the task. Compliments are extra. Boss is not in the chair and not in the room.</p></div>
<div class="domain-card mod"><div class="k">Stakeholder</div><p>Payers, blockers, integrators. Ask funding, veto, and plug-in questions. Show the table, not a tour. Their shoes are not the user.</p></div>
<div class="domain-card vig"><div class="k">Expert</div><p>Legal, safety, a11y, security — veto-capable. Nielsen’s ten as a usability overlay, rules of thumb not WCAG. Book them before the date is printed.</p></div>
</div>
<figcaption>Three truths. Do not average them. Do not mix the rooms when power would fake the result.</figcaption>
</figure>

### Failure catalog
The classic failure is one room with a user, a boss, a lawyer, and a deck. Everyone is polite. The note says “positive feedback.” Spend does not change. Adjacent failures: task success defined as a smile; stakeholders asked to “be the contractor”; experts invited after the tweet; Nielsen’s heuristics used as a 10-point exam or as a fake WCAG pass; a designer scoring their own screens against the ten and calling it expert review; recruiting proxies (“we all on-boarded once”); helping at twenty seconds so the author is not embarrassed; mixing the three truths into a single slide titled Insights.

A quieter failure is sequencing wrong. Stakeholders first, with a pretty shell, lock the team into pre-fill. Users later cannot kill it. Experts last become the people who “slow us down.” Reverse that: users and experts can still change the artifact; stakeholders then fund, block, or integrate *this* artifact. If a payer demands to go first, give them the evidence plan, not the costume.

**Uncertainty:** “Five users” is a common practical count for qualitative findability work, not a law of nature in this syllabus. Write the fail rule first; do not worship a number. Heuristic lists also vary by school. This pack uses Nielsen’s public ten as the overlay it named, and it still requires a real a11y expert when accessibility is the door.

## Worked example(s)
**Problem:** After Lesson 13, the team killed the Thursday pre-fill product demo and redesigning findability. Leadership still wants “a look.” Engineering wants to sit two contractors in the same conference room as the VP who loved the model. Legal has not seen the form language. Someone printed Nielsen’s ten and plans to score the Figma during the user hour.

**Steps:**
1. **Split the rooms.** Facilitator refuses the mixed hour. Users at 10, legal + a11y at 11:30, payers/integrators at 1. The VP is a payer, not a user and not an observer of users. If they want signal, they get the table at 1.
2. **Name the user-testing rule before anyone sits.** Who: new contractors, own phone, real onboarding email. Task: “Start the tax packet. We will not help unless you stop for two minutes.” Success: first field of the packet focused within five minutes, unassisted. Fail: wrong packet, abandon, or a hint. Help policy: a hint is a fail. Nielsen’s ten stay out of this room.
3. **Run three to five people, not a focus group.** Result to carry forward: the first pretotype was 1/5 findability (4/5 failed). After a subject-line and single-link redesign, you are looking for the rule to hold. Compliments about “feeling modern” are written in a margin, not in the count.
4. **Expert room.** Legal reads the packet language for unreadability and signature. Accessibility expert attempts keyboard and phone zoom against the unassisted end state. Usability expert applies Nielsen as overlay: visibility of status (did the email say the packet opened?), match to the real world (does it say “tax packet”?), recognition rather than recall (is the link the packet, or a hub that must be remembered?). Heuristics explain; they do not score a ship. Legal’s veto on clause 4 is a constraint, not a “wish.”
5. **Stakeholder room.** Open with the table and the legal condition, not the model slides. Payer question: “Do you fund findability this month, not the model?” Integrator question: “Can the digest email carry one deep link?” Blocker question: “Do you lift the Thursday demo expectation?” Do not ask them if they would have found the packet.
6. **Do not mix.** When the VP walks toward the 10 a.m. user, the facilitator repeats the sentence: this would make the session a demo. Demos do not clear the RAT. The VP can come at 1.
7. **Named move after the three truths, not during.** If users now meet the rule, experts give conditional no-veto, and payers fund the link: **solidify** findability, still **not ship** until Lesson 16’s DoD and ops. Pre-fill remains untested as a delight claim — it does not get a costume in the stakeholder hour.

**Answer / result:** Three labeled truths instead of one “went well.” The contractor never had to fail in front of the champion. Nielsen stayed an overlay. The end-move can be honest.

## Key Terms
| Term | Definition |
|------|------------|
| User testing | A person who has the job attempts the job under a named rule |
| Task success | Whether they completed the job by a criterion written before they sat |
| Named rule | Who, task, observable success/fail, and help policy |
| Stakeholder | Someone who pays, blocks, or integrates — not “anyone with an opinion” |
| Payer | Funds or starves the next increment |
| Blocker | Can say no with force that survives a smile (legal, security, calendar, statute) |
| Integrator | Must plug the slice into a real system of record |
| Expert review | Domain method: legal, safety, accessibility, security, plus usability overlay |
| Nielsen’s ten heuristics | Rules of thumb for a usability look; not WCAG and not task success |
| Power mix | User and boss (or champion) in one room; fakes success |
| Demo | A tour that cannot fail; does not clear a RAT |
| Veto | Expert or blocker no that the brief must absorb as a constraint |
| Contamination | Averaging three truths into “the review said it went well” |

## Misconception inventory
| Misconception | Reality |
|---------------|---------|
| “They said it was nice, so the test passed.” | Task success is the named rule. Compliments are extra. |
| “Stakeholders speaking is user testing.” | Different truths. Payers cannot complete the contractor’s job by talking. |
| “We should put users and leadership together for alignment.” | Power fakes success. Separate the rooms. |
| “Nielsen’s ten are an accessibility compliance audit.” | They are usability rules of thumb, not WCAG. Book an a11y expert for a11y. |
| “A designer scoring their own Figma is expert review.” | Expert review needs domain method and a chance of veto. Self-score is a note. |
| “Legal can look after we print the launch date.” | Then the veto is a crisis. Experts go before the date is a tattoo. |
| “Five users is statistically significant.” | It is a practical qualitative signal. The fail rule matters more than the folklore number. |
| “If we only have one hour, mix everyone.” | Then you have a show. Spend the hour on users and send the table. |
| “Heuristic 8 means make it pretty.” | Minimalist means the extra chrome is not stealing the job. Pretty is not the heuristic. |
| “An expert smile equals no veto.” | Get veto / no-veto / conditions in writing against named constraints. |

## Summary
- User testing is task success against a named rule, not a compliment session.
- Stakeholders are payers, blockers, and integrators; ask only what they can answer.
- Experts (legal, safety, a11y, security) are veto-capable and must arrive before the date is printed.
- Nielsen’s ten are an expert overlay — rules of thumb, not WCAG, not a ship score.
- Do not mix user and boss in one room. Power fakes success.
- Do not average the three truths. Label them, then name Lesson 13’s move.
- A demo that cannot fail does not clear a RAT.

## Practice
### Retrieval
- What four parts does a named task-success rule need?
- Who counts as a stakeholder in this pack?
- Why are Nielsen’s ten not a WCAG audit?
- What happens to the signal if a user and their boss share a room?
- Name three expert domains that can veto a loved prototype.
- What question do you ask a payer vs an integrator?

### Near transfer
A product manager wants “one review hour” for contractor onboarding: two contractors, the VP champion, legal “if they can make it,” and a walkthrough of the pre-fill Figma. Write the three-room split you refuse to collapse, and the one sentence you say when the VP tries to sit in on the user.

### Far transfer
This Atlas will be used by a new learner at home. Write a one-line task-success rule for “open Lesson 14 from the folder and find the named rule for user testing.” Then name one expert review you would book before calling the pack accessible, and say why Nielsen’s ten are not that booking.

## Spaced retrieval notes
- Day 0: write a named task-success rule for a live artifact before anyone sits.
- Day 2: list payers, blockers, and integrators for one project; write one question each.
- Day 7: run or observe a session with the boss *not* in the room; compare to the last mixed demo you saw.
- Day 21: apply Nielsen’s ten as diagnosis on one failed task, then book the actual expert if a11y, legal, or security is the door.

## Difficulty tiers
- **Novice:** write a named rule; refuse “they said it was nice”; keep user and boss apart.
- **Working:** three separate rooms; payers/blockers/integrators named; Nielsen as overlay not score.
- **Expert:** sequence users and experts before payers so a costume cannot lock the spend; hold a veto in writing without turning the expert into a villain.

## Domain scaffolds
Professional reviews: users are not props in a stakeholder show. Safety and legal one-way doors are expert gates, not pretotypes. Accessibility is method (and often a specialist); heuristics can flag a problem and cannot certify. Security review is not a heuristic. If your org mandates a single “steering committee look,” still run users and experts off-stage and carry labeled truths in, or admit you are running a demo.

## Learn more
- [Nielsen, 10 Usability Heuristics (NN/g)](https://www.nngroup.com/articles/ten-usability-heuristics/) — rules of thumb for an expert overlay; not WCAG and not task success.
- [Scrum Guide](https://scrumguides.org/scrum-guide.html) — Sprint Review inspects the increment; it is not a mixed-power user test.
- [Design Council — Framework for Innovation](https://www.designcouncil.org.uk/our-resources/framework-for-innovation/) — test in diamond 2 is evidence, not a steering-committee tour.
- [Agile Manifesto](https://agilemanifesto.org/) — customer collaboration still requires a person with the job, not only a payer.
- [Principles behind the Agile Manifesto](https://agilemanifesto.org/principles.html) — working software is judged by use, not by a room that cannot fail.
