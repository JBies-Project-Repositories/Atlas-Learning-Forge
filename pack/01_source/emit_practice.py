#!/usr/bin/env python3
"""Emit questions.js and inject lab decks from lesson markdown tables."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSONS = ROOT / "02_lessons"
QUIZ = ROOT / "03_quiz"
LABS = ROOT / "04_labs"

META = [
    ("bl-01-loop", "01_The_Loop", "L01", "The Loop"),
    ("bl-02-methods", "02_Project_Management_Methodology", "L02", "Project Management Methodology"),
    ("bl-03-intent", "03_Communicating_Intent", "L03", "Communicating Intent"),
    ("bl-04-brainstorm", "04_Brainstorming", "L04", "Brainstorming"),
    ("bl-05-prototype", "05_Prototyping", "L05", "Prototyping"),
    ("bl-06-review", "06_Review", "L06", "Review"),
    ("bl-07-ship", "07_Iteration_and_Shipping", "L07", "Iteration and Shipping"),
]


def parse_table(md: str, heading: str) -> list[tuple[str, str]]:
    chunk = md.split(f"## {heading}", 1)[1].split("\n## ", 1)[0]
    rows = []
    for line in chunk.splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2 or cells[0] in ("Term", "Misconception") or set(cells[0]) <= {"-", ":"}:
            continue
        rows.append((cells[0], cells[1]))
    return rows


def load_lessons():
    out = []
    for lid, stem, num, title in META:
        md = (LESSONS / f"{stem}.md").read_text(encoding="utf-8")
        terms = parse_table(md, "Key Terms")
        misc = parse_table(md, "Misconception inventory")
        if len(terms) < 8:
            raise SystemExit(f"{stem} terms {len(terms)}")
        if len(misc) < 6:
            raise SystemExit(f"{stem} misc {len(misc)}")
        out.append({"id": lid, "stem": stem, "num": num, "title": title, "terms": terms, "misc": misc})
    return out


def js(obj) -> str:
    return json.dumps(obj, ensure_ascii=False, indent=2)


def q(lesson_id, title, n, objective, level, stem, correct, wrongs):
    opts = [{"text": correct, "correct": True, "feedback": "That matches this lesson."}]
    for w, fb in wrongs:
        opts.append({"text": w, "correct": False, "feedback": fb})
    # rotate so correct is not always first — keep first as correct then we'll shuffle in a stable way
    # quiz app likely shuffles; keep correct first is OK if app shuffles options
    return {
        "id": f"{lesson_id}-{n}",
        "lesson": title,
        "lessonId": lesson_id,
        "objective": objective,
        "level": level,
        "stem": stem,
        "options": opts,
    }


def questions():
    bank = []
    bank += [
        q("bl-01-loop", "The Loop", 1, "Diverge vs converge", "Understand",
          "A room scores every idea as it is spoken. Which mode is actually running?",
          "Undeclared converge — simultaneous scoring kills diverge",
          [("True diverge, because many people are talking", "Talk volume is not the mode. Scoring while generating is converge."),
           ("PDCA Check, because they are evaluating", "Check is a named comparison after Do, not live scoring of a brainstorm."),
           ("OODA Orient, because they are updating a model", "Orient updates a model after an observation, not a status contest in generation.")]),
        q("bl-01-loop", "The Loop", 2, "Complex vs complicated", "Apply",
          "You can honestly write cause-and-effect in advance and an expert checklist finishes the job. What class is this?",
          "Complicated work",
          [("Complex work", "Complex work is clearer after probes; checklists assume known cause and effect."),
           ("Chaotic work that needs a slogan", "The lesson does not use chaos as a third dumping ground here."),
           ("Always Agile, because there are many parts", "Many parts can still be complicated. Agile is a coat, not a class.")]),
        q("bl-01-loop", "The Loop", 3, "PDCA", "Remember",
          "What does Check add to Plan–Do that ‘we felt good about it’ does not?",
          "A comparison to a measure named while you were still honest in Plan",
          [("A stakeholder smile", "Smiles are not Check."),
           ("A longer Gantt", "That is more Plan, not Check."),
           ("A retrospective about who slipped", "Blame is not the PDCA Check.")]),
        q("bl-01-loop", "The Loop", 4, "OODA", "Understand",
          "In OODA, which step is scarce, and what does skipping it look like?",
          "Orient — the task list updates but the model does not",
          [("Act — moving slower than competitors", "Speed without Orient is panic, not the scarce step."),
           ("Observe — refusing to look at dashboards", "Observation without Orient still fails, but the lesson names Orient as scarce."),
           ("Decide — consensus voting", "Voting is not the named scarce step.")]),
        q("bl-01-loop", "The Loop", 5, "BML order", "Remember",
          "Intellectual order of Build–Measure–Learn in this pack?",
          "Learn (what would change our mind) → Measure → Build",
          [("Build first because the name starts with Build", "The name is the trap."),
           ("Measure → Build → Learn only if the sprint is even", "Even sprints do not change the intellectual order."),
           ("Orient → Decide → Act", "That is OODA, not BML.")]),
        q("bl-01-loop", "The Loop", 6, "Double Diamond", "Understand",
          "Skipping the first diamond usually means what?",
          "A solution diamond aimed at an unstated job",
          [("Faster delivery with no cost", "The cost is building the wrong thing."),
           ("PDCA with extra stickies", "PDCA is a process-improvement loop, not diamond 1."),
           ("You have already converged legally", "Legal freeze is a constraint, not a skipped diamond.")]),
        q("bl-01-loop", "The Loop", 7, "Choose a loop", "Apply",
          "A process exists, you can measure it, and you want it less wrong next week. Which loop?",
          "PDCA on a reversible slice",
          [("OODA because everything is a fight", "Tempo is not the job here."),
           ("Double Diamond because all work is design", "The problem is already a process, not an unstated job."),
           ("Build–Measure–Learn with no measure", "BML without a measure is a feature factory.")]),
        q("bl-01-loop", "The Loop", 8, "Misconception", "Analyze",
          "“If we move faster we are doing OODA.” What is wrong?",
          "Speed without Orient is panic; Orient is the scarce step",
          [("OODA forbids speed", "Tempo is part of OODA; unoriented speed is the error."),
           ("OODA is only for designers", "The lesson places OODA in high-feedback competitive settings."),
           ("They should have used a weighted decision matrix", "This pack does not use a matrix for that choice.")]),
    ]
    bank += [
        q("bl-02-methods", "Project Management Methodology", 1, "What a method is", "Understand",
          "A methodology is best described as what?",
          "A bet about when you learn, when you commit, and how you see unfinished work",
          [("A personality type for hiring", "Methods are coats, not identities."),
           ("A vendor tool stack", "Tools can change; the information problem remains."),
           ("A moral opposite of Waterfall", "Waterfall is a sequence coat, not a villain.")]),
        q("bl-02-methods", "Project Management Methodology", 2, "Discovery vs delivery", "Remember",
          "What does discovery produce?",
          "A decision about what is worth building",
          [("A DoD-passing increment", "That is delivery."),
           ("A longer backlog of unvalidated guesses", "That is discovery failing."),
           ("Story points", "Points are not the output of discovery.")]),
        q("bl-02-methods", "Project Management Methodology", 3, "Scrum", "Understand",
          "Scrum assumes you can produce what on a cadence?",
          "A done increment that meets the definition of done",
          [("A standup with honest feelings", "A meeting is not an increment."),
           ("A six-month regulatory filing each sprint", "If you cannot produce done, Scrum is the wrong coat."),
           ("Unlimited WIP as a sign of passion", "WIP is a lever to limit, not a virtue.")]),
        q("bl-02-methods", "Project Management Methodology", 4, "Waterfall", "Apply",
          "When is a Waterfall-ish sequence the honest coat?",
          "When cause and effect are known and the output is specified",
          [("Never; it is always malpractice", "The lesson rejects that holy war."),
           ("Whenever the org wants a Gantt", "Appetite for a chart is not the information problem."),
           ("For every product bet with users", "That is usually complex; probes first.")]),
        q("bl-02-methods", "Project Management Methodology", 5, "WIP", "Remember",
          "High work in progress usually means what?",
          "Delay — many starts, later finishes",
          [("Speed — more parallel heroes", "The lesson treats high WIP as delay."),
           ("A healthy dual-track", "Dual-track still needs WIP limits."),
           ("That DoD is working", "DoD is a different lever.")]),
        q("bl-02-methods", "Project Management Methodology", 6, "DoD", "Understand",
          "If definition of done is missing, what happens?",
          "Scrum metrics lie and ‘MVPs’ ship as accidents",
          [("QA will catch it at the end, which is the point", "Late DoD is the failure mode."),
           ("Agile forbids checklists", "DoD is a checklist on purpose."),
           ("Discovery automatically fills it", "Discovery produces decisions, not DoD.")]),
        q("bl-02-methods", "Project Management Methodology", 7, "Dual-track", "Apply",
          "Delivery is building unearned guesses. What is dual-track protecting?",
          "Discovery capacity so you do not commit the next increment on an unvalidated bet",
          [("Two teams that never meet", "Tracks must talk."),
           ("A Waterfall phase gate named Agile", "That is a costume."),
           ("Unlimited parallel epics", "That is WIP, not dual-track.")]),
        q("bl-02-methods", "Project Management Methodology", 8, "MVP", "Analyze",
          "“MVP means ship a worse version of the full product.” Why is that wrong?",
          "MVP is the smallest test of a hypothesis, not a discount SKU",
          [("Because MVPs must look high-fi", "Looks are a fidelity choice, not the definition."),
           ("Because Scrum forbids shipping small", "Scrum wants a done increment, which can be small."),
           ("Because Waterfall already shipped the full product", "Non sequitur.")]),
    ]
    bank += [
        q("bl-03-intent", "Communicating Intent", 1, "Intent stack", "Remember",
          "Commander’s intent in this pack is which trio?",
          "Purpose + end state + constraints",
          [("Vision + roadmap + standups", "Those are not the trio."),
           ("Tasks + owners + dates", "That is instruction."),
           ("HMW + SCAMPER + Crazy 8s", "Those are ideation tools.")]),
        q("bl-03-intent", "Communicating Intent", 2, "Purpose", "Understand",
          "Which line is a purpose rather than a task?",
          "So night-shift nurses can find the dosing note in under a minute",
          [("Build a dashboard", "A noun is a task/solution."),
           ("Deliver the epic by Friday", "A date is not a human outcome."),
           ("Modern UX", "A slogan is not a purpose.")]),
        q("bl-03-intent", "Communicating Intent", 3, "Problem statement", "Apply",
          "What must a problem statement not smuggle?",
          "A solution noun",
          [("Evidence of pain", "Evidence belongs."),
           ("Who has the job", "Who belongs."),
           ("Constraints later put on the brief", "Constraints are a different artifact.")]),
        q("bl-03-intent", "Communicating Intent", 4, "HMW", "Understand",
          "A good How Might We should allow what?",
          "At least three structurally different answers, including one that is not software",
          [("Only the solution leadership already likes", "That is a leading question."),
           ("No constraints at all", "Constraints live on the brief; HMW still has a job."),
           ("A 40-page vision", "Vision is a different artifact.")]),
        q("bl-03-intent", "Communicating Intent", 5, "Non-goals", "Remember",
          "Why write non-goals?",
          "To stop polite scope creep on plausible work you are not doing this round",
          [("To lower morale with negativity", "Unwritten non-goals cause the later fight."),
           ("To replace success criteria", "Different job."),
           ("To instruct every CSS step", "That is instruction.")]),
        q("bl-03-intent", "Communicating Intent", 6, "Alignment vs instruction", "Analyze",
          "If you disappeared for two days, a competent teammate can still move toward the end state without violating a wall. What did you write?",
          "Alignment (intent)",
          [("A complete instruction runbook and nothing else", "Runbooks are instruction; the tell is they can choose unforeseen steps."),
           ("A vision poster", "Vision without a round is not enough."),
           ("A WIP limit only", "WIP is a method lever, not intent.")]),
        q("bl-03-intent", "Communicating Intent", 7, "Brief", "Understand",
          "If a brief cannot be read in about three minutes, what is it?",
          "A document pretending to be alignment",
          [("More rigorous by definition", "Length is not rigor."),
           ("A valid PDCA Check", "Check is a measure comparison."),
           ("A definition of done", "DoD is a quality checklist.")]),
        q("bl-03-intent", "Communicating Intent", 8, "End state", "Apply",
          "Which is an end state?",
          "A nurse completes the task on a phone without calling the day shift",
          [("Modernize the platform", "Not observable."),
           ("Be the best onboarding in the industry", "Vision-ish, not this-round true."),
           ("Schedule a workshop", "A task.")]),
    ]
    bank += [
        q("bl-04-brainstorm", "Brainstorming", 1, "Hard rules", "Remember",
          "The two hard rules of generation in this pack?",
          "Deferred judgment and quantity before quality",
          [("Dot voting and HiPPO steer", "Those kill diverge."),
           ("Socratic review and devil’s advocate in minute two", "Those are later converge tools."),
           ("SCAMPER and Waterfall", "Methods, not the two rules.")]),
        q("bl-04-brainstorm", "Brainstorming", 2, "Brainwriting", "Understand",
          "When is brainwriting the better generation method?",
          "When a few voices usually fill the air",
          [("When the problem is only visual", "Crazy 8s is the visual-forcing tool."),
           ("When you are attacking an existing artifact with prompts", "That is SCAMPER."),
           ("During devil’s-advocate review", "Review is not generation.")]),
        q("bl-04-brainstorm", "Brainstorming", 3, "SCAMPER", "Remember",
          "SCAMPER is for what?",
          "Attacking an existing artifact with a prompt list",
          [("Blank-page problems with no artifact", "The lesson says not for a blank problem."),
           ("Scoring ideas live", "That is undeclared converge."),
           ("Writing a DoD", "Wrong lesson.")]),
        q("bl-04-brainstorm", "Brainstorming", 4, "Devil’s advocate", "Apply",
          "A director starts devil’s-advocating in minute two of generation. What do you do?",
          "Park it — judgment is illegal during diverge; schedule it after clustering",
          [("Encourage it so the room stays realistic", "Realistic is undeclared converge."),
           ("Cancel Design Thinking forever", "Overkill."),
           ("Switch to Waterfall immediately", "Wrong coat.")]),
        q("bl-04-brainstorm", "Brainstorming", 5, "Progression", "Understand",
          "What is the output of a good brainstorm in this pack?",
          "Testable claims (who, action, measure) — not a photo of stickies",
          [("A winner chosen by dots on slogans", "Dots often pick familiar wording."),
           ("A shipped MVP", "Too soon."),
           ("A six-month roadmap", "That is fake diamond 2.")]),
        q("bl-04-brainstorm", "Brainstorming", 6, "Constraints", "Understand",
          "Constraint-based ideation adds walls on purpose because they usually what?",
          "Increase variety more than ‘think outside the box’",
          [("Always reduce options to one vendor", "That is a smuggled solution."),
           ("Replace the HMW", "HMW is still the prompt."),
           ("Satisfy legal without a later converge", "Legal walls still need a real owner later.")]),
        q("bl-04-brainstorm", "Brainstorming", 7, "Cancel", "Apply",
          "There is no HMW and a senior person is there to steer. What does the lesson say?",
          "Cancel — a fake brainstorm poisons later critique",
          [("Run faster so steering has less time", "Speed does not fix the protocol."),
           ("Switch to a high-fi prototype", "Wrong phase."),
           ("Take minutes of only the liked ideas", "That is a listed failure.")]),
        q("bl-04-brainstorm", "Brainstorming", 8, "Socratic", "Analyze",
          "Socratic review is for what?",
          "Questions that expose missing who/job/constraint after clustering",
          [("Humiliating the author in generation", "That is status, not Socratic."),
           ("Replacing user testing", "Different review type (Lesson 6)."),
           ("Writing code comments", "Non sequitur.")]),
    ]
    bank += [
        q("bl-05-prototype", "Prototyping", 1, "Fidelity", "Understand",
          "Fidelity should match what?",
          "The question you need answered, not the stakeholder’s rank",
          [("Always high, because polish is professional", "Early polish persuades and freezes."),
           ("Always low, because Agile forbids pixels", "High-fi is valid when texture/trust is the risk."),
           ("The number of sprints remaining", "Calendar is not the question.")]),
        q("bl-05-prototype", "Prototyping", 2, "Looks vs works", "Remember",
          "A pretty shell with no mechanism is which kind of prototype?",
          "Looks-like — allowed only if appearance is the risk",
          [("Works-like", "Works-like tests mechanism and may look like junk."),
           ("MVP", "MVP is shipped."),
           ("PDCA Check", "Wrong loop artifact.")]),
        q("bl-05-prototype", "Prototyping", 3, "Pretotype vs MVP", "Understand",
          "How does a pretotype differ from an MVP here?",
          "Pretotype fakes the experience before the mechanism; MVP is a shipped test in the real system",
          [("They are synonyms for a domain name on a prototype", "The lesson rejects that blur."),
           ("Pretotype is always illegal deception", "It is a short demand/comprehension test."),
           ("MVP must look unfinished", "Looks are a fidelity choice.")]),
        q("bl-05-prototype", "Prototyping", 4, "Riskiest first", "Apply",
          "Teams love testing the assumption they already believe. What should they test instead?",
          "The high-impact unknown (ignorance × impact)",
          [("The prettiest Figma", "Comfort."),
           ("Whatever fits the sprint length", "Calendar is not rank."),
           ("Only legal assumptions", "Legal may be the riskiest — then ask counsel, don’t pretty-demo.")]),
        q("bl-05-prototype", "Prototyping", 5, "Smallest slice", "Remember",
          "A smallest testable slice must include which stop-related piece?",
          "A fail rule and what you will stop if it fails",
          [("A full backlog", "Opposite of smallest."),
           ("A launch party", "Launch is Lesson 7."),
           ("Dot votes", "Lesson 4 failure mode.")]),
        q("bl-05-prototype", "Prototyping", 6, "Cannot fail", "Analyze",
          "A demo that cannot fail is what?",
          "Sales, not a test",
          [("A strong MVP", "MVPs must be able to falsify a hypothesis."),
           ("Experience prototype by definition", "Experience tests can fail."),
           ("OODA Act", "Wrong lesson.")]),
        q("bl-05-prototype", "Prototyping", 7, "Climb the ladder", "Understand",
          "When do you climb fidelity?",
          "When the cheaper rung cannot kill the assumption",
          [("When a VP asks for a real demo", "Tell them the question; paper can be professional."),
           ("When the stickies look messy", "Mess is a feature of lo-fi."),
           ("After launch only", "Launch is a mode switch, not a fidelity rule.")]),
        q("bl-05-prototype", "Prototyping", 8, "Safety", "Apply",
          "Which prototype is forbidden in this pack?",
          "A cute fake that could teach a dangerous action on a one-way safety door",
          [("Paper maps of a findability problem", "That is a listed honest test."),
           ("Wizard-of-Oz pre-fill after findability holds", "Allowed as a later rung."),
           ("Works-like junk for a mechanism risk", "Allowed.")]),
    ]
    bank += [
        q("bl-06-review", "Review", 1, "Critique", "Remember",
          "In a design critique, what is on trial?",
          "The artifact against the brief — not the author",
          [("The author’s competence", "Status contest."),
           ("The stakeholder’s taste only", "Taste without the brief is a salon."),
           ("The sprint points", "Wrong instrument.")]),
        q("bl-06-review", "Review", 2, "Speech protocol", "Understand",
          "I like / I wish / What if maps to which trio?",
          "Specific praise, desired change, proposed experiment",
          [("Diverge, SCAMPER, ship", "Wrong."),
           ("Observe, Orient, Act", "OODA, and missing Decide."),
           ("Nice, nicer, nicest", "Niceness without a move is stalling.")]),
        q("bl-06-review", "Review", 3, "RAT", "Understand",
          "A riskiest assumption test is what kind of gate?",
          "Stop/go — do not spend the next increment until there is a kill/keep signal",
          [("A canvas you admire in a workshop", "The lesson rejects canvas-as-work."),
           ("A stakeholder smile", "Not a test."),
           ("A definition of done", "DoD is quality of an increment.")]),
        q("bl-06-review", "Review", 4, "User vs stakeholder", "Apply",
          "Why separate user testing from stakeholder review when power mixes?",
          "A user will not fail a task honestly in front of the boss who championed the design",
          [("Because users never have useful opinions", "Opinions after the task are extra, not forbidden."),
           ("Because stakeholders are always wrong", "They pay/block/integrate — different truth."),
           ("Because experts replace both", "Expert review is a third type.")]),
        q("bl-06-review", "Review", 5, "Task success", "Remember",
          "Task success is primarily what?",
          "Whether they completed the job by a named rule",
          [("Whether they said it was nice", "Opinion instead of the task is not a test."),
           ("Whether leadership nodded", "Stakeholder review."),
           ("Whether the Figma was high-fi", "Fidelity is not success.")]),
        q("bl-06-review", "Review", 6, "End move", "Analyze",
          "The meeting ends with ‘let’s keep thinking.’ What happened?",
          "You stalled — that is not redesign, solidify, kill, pivot, or ship",
          [("A valid PDCA Act", "Act is adopt/adjust/drop, not fog."),
           ("A passing retrospective", "Retros are Lesson 7 and need one change."),
           ("Steelman", "Steelman is a fairness move, not an end-state of the meeting.")]),
        q("bl-06-review", "Review", 7, "Pre-mortem", "Understand",
          "A pre-mortem that is only gallows humor fails because it lacks what?",
          "Owners on the plausible failure stories",
          [("Enough jokes", "Entertainment is the failure mode."),
           ("A high-fi prototype", "Wrong phase."),
           ("Dot votes", "Wrong tool.")]),
        q("bl-06-review", "Review", 8, "Steelman", "Remember",
          "To steelman in review is to do what?",
          "State the strongest fair form of the case for killing your favorite idea",
          [("Sarcastically straw-man the critic", "The lesson forbids that prefix."),
           ("Agree and stop the project always", "You may still keep after you understand the risk."),
           ("Replace user testing", "Different instrument.")]),
    ]
    bank += [
        q("bl-07-ship", "Iteration and Shipping", 1, "Two velocities", "Remember",
          "Learning velocity is measured in what?",
          "Tests — how fast you kill or keep assumptions",
          [("Story points", "That is a delivery costume."),
           ("Headcount", "Not a velocity here."),
           ("Number of loops on a slide", "Diagrams are not tests.")]),
        q("bl-07-ship", "Iteration and Shipping", 2, "Feature velocity", "Understand",
          "Twelve ‘in progress’ AI ideas and zero done increments is what?",
          "WIP, not feature velocity",
          [("High learning velocity", "No tests were named."),
           ("A successful launch", "Nothing shipped."),
           ("OODA tempo", "Unoriented starts are not tempo.")]),
        q("bl-07-ship", "Iteration and Shipping", 3, "Threshold", "Apply",
          "You write the pivot/persevere threshold after seeing the data. What are you doing?",
          "Storytelling — you will pick the story that saves the plan",
          [("Proper Orient", "Orient is honest model update, not post-hoc thresholds."),
           ("A definition of done", "DoD is not an evidence threshold."),
           ("Operations", "Ops is after the mode switch.")]),
        q("bl-07-ship", "Iteration and Shipping", 4, "Pivot vs kill", "Understand",
          "Pivot vs kill in this pack?",
          "Pivot: job alive, approach wrong. Kill: the job is dead",
          [("They are nicer words for the same fail", "Do not blur them to save face."),
           ("Pivot means ship anyway", "That is persevere without evidence."),
           ("Kill means fire the team", "The lesson inspects the loop, not the people.")]),
        q("bl-07-ship", "Iteration and Shipping", 5, "Retro", "Remember",
          "A passing retrospective produces what?",
          "One change to the next loop",
          [("Twelve actions and a blame chart", "Wishlist + people theater."),
           ("A launch party", "Optional."),
           ("A new methodology identity", "Coats, not identities.")]),
        q("bl-07-ship", "Iteration and Shipping", 6, "Mode switch", "Understand",
          "Launch is described as what?",
          "A mode switch from learning (change cheap) to delivery (change expensive) for a slice",
          [("A company-wide freeze forever", "The switch is local to a slice."),
           ("A party that proves the idea", "Shipping proves you can operate a slice."),
           ("Eternal beta", "Eternal beta often skips operations.")]),
        q("bl-07-ship", "Iteration and Shipping", 7, "Quality", "Apply",
          "Quality as a hardening sprint after launch means what?",
          "It was never in the definition of done",
          [("A healthy dual-track", "Dual-track is discovery/delivery, not late quality."),
           ("Operations excellence", "Ops is separate and also belongs in the brief."),
           ("High learning velocity", "Unrelated.")]),
        q("bl-07-ship", "Iteration and Shipping", 8, "Demo", "Analyze",
          "Leadership wants the learning-mode AI pretotype on the all-hands stage as if it shipped. What do you offer instead?",
          "A task-success table for the slice that actually met evidence, and keep the rest in the lab",
          [("The pretty shell because morale is a constraint that vetoes truth", "Morale is not a veto on lying about mode."),
           ("Nothing — never speak to leadership", "They need a signal; give a true one."),
           ("A weighted decision matrix of feelings vs dates", "This pack does not use that matrix.")]),
    ]
    if len(bank) != 56:
        raise SystemExit(f"expected 56 questions, got {len(bank)}")
    for item in bank:
        if sum(1 for o in item["options"] if o["correct"]) != 1:
            raise SystemExit(item["id"])
        if len(item["options"]) != 4:
            raise SystemExit(item["id"])
    return bank


SCENES = [
    {
        "id": "bl-01-loop", "num": "L01", "title": "The Loop",
        "scene": "A product trio is asked for a six-month AI-summary roadmap by Friday. They correctly note that a loop is for work where the map is incomplete, and that skipping diamond 1 is a common injury. They still put the entire bet on one Gantt because leadership likes dates. In the kickoff they diverge and score every idea as it is spoken to save time. Someone says moving faster is OODA; the task list grows while the model of the user stays last year’s. They Plan and Do a full architecture, then Act on how excited the room felt — no named Check. Build starts Monday because the name Build–Measure–Learn starts with Build. A known payroll export on the same program is also labeled complex so it can skip its checklist. A designer asks for twenty minutes of named diverge with no scoring; the room says there is no time, then spends an hour arguing vendors. Nobody writes what would change their mind before the first commit.",
        "ok": [
            "A loop is for work where the map is incomplete.",
            "Skipping diamond 1 is a common injury.",
        ],
        "errors": [
            {"bad": "Putting a complex product bet on one Gantt because leadership likes dates", "fix": "A Gantt assumes known cause and effect. The Friday artifact should be a loop, not a fake roadmap."},
            {"bad": "Diverging and scoring every idea as it is spoken", "fix": "That is undeclared converge. Name the mode; add first, then kill/keep."},
            {"bad": "Moving faster as OODA while the user model stays last year’s", "fix": "Speed without Orient is panic. Orient is the scarce step."},
            {"bad": "Plan–Do then Act on excitement with no named Check", "fix": "PDCA Check is a comparison to a measure named in Plan."},
            {"bad": "Building first because BML starts with Build", "fix": "Intellectual order is Learn → Measure → Build."},
            {"bad": "Labeling a known payroll export complex to skip its checklist", "fix": "Complicated work keeps the checklist. Do not steal the complex label to dodge sequence."},
        ],
    },
    {
        "id": "bl-02-methods", "num": "L02", "title": "Project Management Methodology",
        "scene": "A department announces it is Agile. Daily standups exist, which can be a cadence heartbeat. Discovery still has no capacity, so delivery invents the portal in the sprint review. The same Scrum board holds a fixed-date payroll cutover and the unvalidated portal. WIP is 23 items for six people; they call it passion. There is no definition of done, so QA will catch it at the end. They ship an ‘MVP’ that is a half-built full product with no hypothesis. Waterfall is mocked in Slack even for the statute-shaped cutover. Dual-track is implemented as two teams that never meet. Sprint length is cut mid-cycle because a date slipped, destroying the only heartbeat that showed throughput. A staff engineer asks for a written DoD on the cutover dry-run; the board instead adds more stories so the chart looks busy.",
        "ok": [
            "Daily standups can be a cadence heartbeat.",
            "A department can name Agile as a stance about late information.",
        ],
        "errors": [
            {"bad": "Discovery has no capacity so delivery invents the product", "fix": "Dual-track exists so discovery can earn the next slice."},
            {"bad": "One Scrum board for a legal cutover and an unvalidated portal", "fix": "Split the sandwich. Different clocks and DoDs."},
            {"bad": "WIP of 23 as passion", "fix": "High WIP is usually delay. Limit starts."},
            {"bad": "No DoD because QA will catch it", "fix": "If DoD is late, metrics lie."},
            {"bad": "MVP as a discount full product with no hypothesis", "fix": "MVP is the smallest test of a claim."},
            {"bad": "Mocking Waterfall for a statute-shaped cutover", "fix": "Sequence is honest when cause and effect are known."},
            {"bad": "Dual-track as two teams that never meet", "fix": "The tracks must talk."},
        ],
    },
    {
        "id": "bl-03-intent", "num": "L03", "title": "Communicating Intent",
        "scene": "A manager wants alignment. Purpose is written as a human outcome, and a constraint forbids a new vendor this sprint — both sound. The rest of the brief is ‘build a dashboard’ and ‘modern UX’ as the end state. How Might We is ‘how might we build the red button on page 3?’ Non-goals are skipped so morale stays high. Success is ‘stakeholders are excited.’ The document is 28 pages and called a brief. The manager aligns on vision in the morning and micromanages CSS in the afternoon. Instruction is used for a production deploy checklist, which is appropriate, then the same style is used for a complex prototype week. Two competent teammates say they still cannot act if the manager disappears for two days, because the walls were never written. A contractor is told the purpose is ‘deliver the epic.’",
        "ok": [
            "Purpose as a human outcome is the right kind of line.",
            "A production deploy checklist is a correct use of instruction.",
        ],
        "errors": [
            {"bad": "‘Build a dashboard’ standing in for intent", "fix": "That is a task/solution noun, not purpose or end state."},
            {"bad": "‘Modern UX’ as end state", "fix": "End state must be observable later."},
            {"bad": "HMW that only allows the red button", "fix": "A good HMW allows structurally different answers, including non-software."},
            {"bad": "Skipping non-goals for morale", "fix": "Unwritten non-goals become the Thursday scope fight."},
            {"bad": "Success = stakeholder excitement", "fix": "Prefer behavior you can count."},
            {"bad": "A 28-page ‘brief’", "fix": "A brief is readable in minutes."},
            {"bad": "Vision in the morning, CSS micromanagement in the afternoon, and instruction on a complex prototype week", "fix": "Alignment is the stack; instruction is for low-variance work. Do not mix them as a control habit."},
        ],
    },
    {
        "id": "bl-04-brainstorm", "num": "L04", "title": "Brainstorming",
        "scene": "Four people meet to generate options. They do have a How Might We on the wall, which is the right input. The director steers in minute two so they stay realistic. Someone runs Crazy 8s, SCAMPER, and a free-for-all in forty minutes. Devil’s advocate starts during generation to keep them honest. Minutes record only the ideas the scribe liked. They dot-vote on slogans and call the winner the prototype. SCAMPER is used on a blank page with no artifact. The photo of forty stickies is the shipped output. A later critique will remember who got shot down. A quiet engineer’s written ideas never leave a notebook because the room switched to talking. Quantity is praised, then immediately ranked. The facilitator calls the session a success because people had fun.",
        "ok": [
            "A How Might We on the wall is the right input to a brainstorm.",
            "Generation can be time-boxed in a single session.",
        ],
        "errors": [
            {"bad": "Director steering in minute two to stay realistic", "fix": "Steering is undeclared converge. HiPPO in generation collapses the set."},
            {"bad": "Stacking Crazy 8s, SCAMPER, and free-for-all in forty minutes", "fix": "Pick one primary method."},
            {"bad": "Devil’s advocate during generation", "fix": "Schedule it after clustering."},
            {"bad": "Minutes of only liked ideas", "fix": "Capture everything; cluster later."},
            {"bad": "Dot-voting slogans as the prototype", "fix": "Promote testable claims; vote on what to test if you vote at all."},
            {"bad": "SCAMPER on a blank page", "fix": "SCAMPER attacks an existing artifact."},
            {"bad": "Photo of stickies as the output", "fix": "Output is a testable claim, or cancel."},
        ],
    },
    {
        "id": "bl-05-prototype", "num": "L05", "title": "Prototyping",
        "scene": "The riskiest assumption is that contractors can find the packet. The team agrees a smallest slice needs a fail rule. They still build a high-fidelity looks-like of an AI helper because leadership wants a real demo. They call it an MVP once it has a domain name, with no measure. Mechanism risk is deferred until after the pretty shell. The demo is designed so it cannot fail on stage. A one-way safety instruction is prototyped as a cute fake that could teach the wrong action. Paper is rejected because vice presidents will not take it seriously, and nobody states the question the paper would answer. Five contractors are invited to clap at the demo instead of attempting the packet unassisted. The stop condition is never written, so a failed findability test cannot kill the helper this sprint.",
        "ok": [
            "The riskiest assumption is findability, not helper polish.",
            "A smallest slice should include a fail rule.",
        ],
        "errors": [
            {"bad": "High-fi looks-like of the helper because leadership wants a real demo", "fix": "Match fidelity to the question. Findability is a lo-fi experience test."},
            {"bad": "Domain name makes it an MVP", "fix": "MVP is shipped and measured in the real system."},
            {"bad": "Pretty shell before mechanism when mechanism is a risk", "fix": "That is theater. Works-like may look like junk."},
            {"bad": "A demo that cannot fail", "fix": "If it cannot fail, it is sales."},
            {"bad": "Cute fake on a one-way safety door", "fix": "Forbidden if it can teach a dangerous action."},
            {"bad": "Rejecting paper because of rank, without stating the question", "fix": "A VP can read paper if you tell them what question it answers."},
        ],
    },
    {
        "id": "bl-06-review", "num": "L06", "title": "Review",
        "scene": "A critique is on the calendar. The artifact is supposed to be on trial against the brief, which is correct. There is no brief in the room. Executives nod at a high-fi walkthrough; that is called user testing. Task success is ‘they said it was nice.’ A pre-mortem produces jokes and no owners. Steelman is used as a sarcastic prefix to a straw man. Experts with veto are invited after the launch date is printed. The meeting ends with ‘let’s keep thinking.’ Kill is socially impossible, so everything solidifies. Spend does not change. A user who has the actual job is in the room with their boss who championed the design, so they do not fail the task out loud. I like / I wish / What if is skipped for a live redesign by committee.",
        "ok": [
            "The artifact should be on trial against the brief.",
            "A critique can be a scheduled gate.",
        ],
        "errors": [
            {"bad": "No brief in the room", "fix": "Cancel the critique. People will review an imaginary product."},
            {"bad": "Executive nods called user testing", "fix": "Stakeholder review is a different truth."},
            {"bad": "Task success as ‘they said it was nice’", "fix": "Success is completing the job by a named rule."},
            {"bad": "Pre-mortem as jokes without owners", "fix": "Owned failure stories are the point."},
            {"bad": "Sarcastic steelman", "fix": "Steelman is the strongest fair form, especially of the kill case."},
            {"bad": "Experts after the date is printed", "fix": "Veto experts go before the date."},
            {"bad": "‘Keep thinking’ / kill unsayable / spend unchanged", "fix": "Name redesign, solidify, kill, pivot, or ship. If spend does not change, it was not a review."},
        ],
    },
    {
        "id": "bl-07-ship", "num": "L07", "title": "Iteration and Shipping",
        "scene": "The team says they iterated, so they delivered. They have thirty story points done and zero tests; they report that as learning velocity. Pivot vs persevere will be decided after they see the numbers. The retro produces twelve actions and a slide about who slipped. They want to stay in beta forever so they can keep learning, and they also scheduled a hardening sprint for quality after the tweet. Launch is planned as a party that will prove the idea. Support has no script and rollback is unnamed. A learning-mode pretotype is booked for the all-hands as if it already shipped. On-call is nobody. A live slice is silently rewritten the night before the party because ‘we are still iterating,’ which is a mode confusion: change is now expensive and users already have a habit on the old link.",
        "ok": [
            "The team can have both a learning track and a delivery track in the same month.",
            "Story points can exist as a delivery instrument if DoD is real.",
        ],
        "errors": [
            {"bad": "Iterated, therefore delivered", "fix": "Learning can be fast with zero ship. Use two scoreboards."},
            {"bad": "Zero tests reported as learning velocity", "fix": "Learning velocity is tests, not points."},
            {"bad": "Threshold after the data", "fix": "Write pivot/persevere/kill before the test."},
            {"bad": "Retro as twelve actions plus blame", "fix": "One change to the next loop; inspect the system."},
            {"bad": "Eternal beta and quality after the tweet", "fix": "Eternal beta skips ops. Quality after launch means it was never in DoD."},
            {"bad": "Launch party as proof of the idea", "fix": "Launch is a mode switch. Shipping proves you can operate a slice."},
            {"bad": "Learning-mode artifact on the all-hands as shipped", "fix": "Offer the task-success table; keep the rest in the lab."},
        ],
    },
]


def inject_array(path: Path, const_name: str, value) -> None:
    text = path.read_text(encoding="utf-8")
    pat = re.compile(rf"const {const_name} = \[.*?\n    \];", re.S)
    replacement = f"const {const_name} = {json.dumps(value, ensure_ascii=False, indent=2)};"
    # indent replacement to match script
    replacement = replacement.replace("\n", "\n    ")
    replacement = "    " + replacement
    if not pat.search(text):
        raise SystemExit(f"no {const_name} in {path.name}")
    path.write_text(pat.sub(replacement, text, count=1), encoding="utf-8")
    print("injected", const_name, "->", path.name)


def main() -> None:
    lessons = load_lessons()
    bank = questions()
    (QUIZ / "questions.js").write_text(
        "/** Atlas of the Build Loop — multi-deck bank (56) */\nwindow.QUESTIONS = "
        + js(bank)
        + ";\n",
        encoding="utf-8",
    )
    print("wrote questions.js", len(bank))

    decks = []
    fermi = []
    steel = []
    for L in lessons:
        decks.append({
            "id": L["id"],
            "num": L["num"],
            "title": L["title"],
            "terms": [list(t) for t in L["terms"]],
            "misc": [list(m) for m in L["misc"]],
        })
        fermi.append({
            "id": L["id"],
            "num": L["num"],
            "title": L["title"],
            "pairs": [
                {
                    "id": f"t{i}",
                    "left": t[0],
                    "right": t[1],
                    "why": "From this lesson’s Key Terms table.",
                }
                for i, t in enumerate(L["terms"])
            ],
        })
        steel.append({
            "weak": L["misc"][0][0],
            "model": "Steelman: name the fear or incentive underneath, then the fair condition, then the limit. Reality from the lesson: " + L["misc"][0][1],
            "lessonId": L["id"],
            "title": L["title"],
        })
        for m in L["misc"][1:3]:
            steel.append({
                "weak": m[0],
                "model": "Fair form, then the limit. " + m[1],
                "lessonId": L["id"],
                "title": L["title"],
            })

    inject_array(LABS / "spaced.html", "DECKS", decks)
    inject_array(LABS / "fermi.html", "DECKS", fermi)
    inject_array(LABS / "bias.html", "SCENES", SCENES)

    # steelman: replace ITEMS; keep engine
    inject_array(LABS / "steelman.html", "ITEMS", steel)

    # fermi set ids used in optgroups — patch body/blood to door/tools
    fermi_html = (LABS / "fermi.html").read_text(encoding="utf-8")
    fermi_html = fermi_html.replace(
        'const BODY = new Set(["ct-01-dose", "ct-02-acute", "ct-03-heart", "ct-04-muscle"]);',
        'const BODY = new Set(["bl-01-loop", "bl-02-methods", "bl-03-intent"]);',
    )
    fermi_html = fermi_html.replace(
        'const BLOOD = new Set(["ct-05-metabolic", "ct-06-hematology", "ct-07-labs", "ct-08-program"]);',
        'const BLOOD = new Set(["bl-04-brainstorm", "bl-05-prototype", "bl-06-review", "bl-07-ship"]);',
    )
    fermi_html = fermi_html.replace("Arc A–B · body", "Arc A–B · door + methods")
    fermi_html = fermi_html.replace("Arc C–D · bloodwork", "Arc C–D · tools + ship")
    (LABS / "fermi.html").write_text(fermi_html, encoding="utf-8")
    print("patched fermi sets")

    for L, S in zip(lessons, SCENES):
        wc = len(S["scene"].split())
        print(f"scene {L['id']} words={wc} ok={len(S['ok'])} err={len(S['errors'])}")
        if not (120 <= wc <= 220):
            print("  WARN wordcount")


if __name__ == "__main__":
    main()
