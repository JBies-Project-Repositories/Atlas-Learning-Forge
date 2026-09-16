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
    ("bl-a1-diverge", "01_Divergent_and_Convergent", "L01", "Divergent and Convergent Thinking"),
    ("bl-a2-cynefin", "02_Complicated_and_Complex", "L02", "Complicated, Complex, and Cynefin"),
    ("bl-a3-pdca-ooda", "03_PDCA_and_OODA", "L03", "PDCA and OODA"),
    ("bl-a4-bml-diamond", "04_BML_and_Double_Diamond", "L04", "Build–Measure–Learn and Double Diamond"),
    ("bl-b1-discovery", "05_Discovery_and_Delivery", "L05", "Discovery, Delivery, and Dual-Track"),
    ("bl-b2-coats", "06_Agile_Scrum_Waterfall", "L06", "Agile, Scrum, and Honest Waterfall"),
    ("bl-b3-levers", "07_Cadence_WIP_DoD", "L07", "Cadence, Scope, WIP, and Definition of Done"),
    ("bl-b4-intent", "08_Commanders_Intent", "L08", "Commander’s Intent and the Brief"),
    ("bl-c1-protocol", "09_Brainstorm_Protocol", "L09", "Brainstorming as a Protocol"),
    ("bl-c2-generate", "10_Generation_and_Review", "L10", "Generation Methods and Converge Reviews"),
    ("bl-c3-fidelity", "11_Fidelity_and_Kinds", "L11", "Fidelity and Kinds of Prototype"),
    ("bl-c4-test", "12_Smallest_Honest_Test", "L12", "Pretotype, MVP, and the Riskiest Assumption"),
    ("bl-d1-critique", "13_Critique_and_Assumptions", "L13", "Critique, RAT, and Pre-mortem"),
    ("bl-d2-reviews", "14_Three_Reviews", "L14", "User, Stakeholder, and Expert Review"),
    ("bl-d3-evidence", "15_Pivot_and_Evidence", "L15", "Pivot, Persevere, and Evidence Thresholds"),
    ("bl-d4-launch", "16_Launch_and_Operations", "L16", "Launch, Quality, Operations, Mode Switch"),
]

ARC_A = {m[0] for m in META[:4]}
ARC_B = {m[0] for m in META[4:8]}
ARC_C = {m[0] for m in META[8:12]}
ARC_D = {m[0] for m in META[12:]}


def parse_table(md: str, heading: str) -> list[tuple[str, str]]:
    chunk = md.split(f"## {heading}", 1)[1].split("\n## ", 1)[0]
    rows = []
    for line in chunk.splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2 or cells[0] in ("Term", "Misconception") or set(cells[0]) <= {"-", ":"}:
            continue
        rows.append((cells[0].strip('"“”'), cells[1]))
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
    return {
        "id": f"{lesson_id}-{n}",
        "lesson": title,
        "lessonId": lesson_id,
        "objective": objective,
        "level": level,
        "stem": stem,
        "options": opts,
    }


GENERIC_WRONG = [
    ("A six-month Gantt is always the professional next artifact", "A Gantt assumes known cause and effect."),
    ("Score every idea as it is spoken to save time", "That is undeclared converge."),
    ("Ship the pretty demo because leadership has a date", "Dates do not authorize a test that cannot fail."),
    ("More work in progress means we are faster", "High WIP is usually delay."),
]


def questions(lessons):
    bank = []
    for L in lessons:
        terms, misc = L["terms"], L["misc"]
        n = 1
        # 4 term items
        for i, (term, defin) in enumerate(terms[:4]):
            others = [t[1] for j, t in enumerate(terms) if j != i][:3]
            while len(others) < 3:
                others.append(GENERIC_WRONG[len(others)][0])
            wrongs = [(o[:140], "That definition belongs to a different term in this lesson.") for o in others]
            bank.append(q(L["id"], L["title"], n, term[:80], "Remember",
                          f"Which definition matches “{term}” in this lesson?",
                          defin[:180], wrongs))
            n += 1
        # 4 misconception items
        for i, (weak, real) in enumerate(misc[:4]):
            others = [m[1] for j, m in enumerate(misc) if j != i][:2]
            others.append(GENERIC_WRONG[i % 4][0])
            wrongs = [(o[:140], "That is not the correction this lesson teaches.") for o in others]
            bank.append(q(L["id"], L["title"], n, "Misconception", "Understand",
                          f"A teammate says: {weak[:160]} What is the field-guide correction?",
                          real[:180], wrongs))
            n += 1
        if n != 9:
            raise SystemExit(f"{L['id']} expected 8 questions, built {n-1}")
    if len(bank) != 128:
        raise SystemExit(f"expected 128 questions, got {len(bank)}")
    return bank


def scenes(lessons):
    out = []
    for L in lessons:
        misc = L["misc"]
        errors = [{"bad": m[0][:180], "fix": m[1][:240]} for m in misc[:6]]
        planted = " ".join(m[0].strip('"“”') for m in misc[:5])
        scene = (
            f"A working note from {L['title']}. Two sound claims are present: the lesson’s named move is a coat not an identity, "
            f"and a facilitation script exists so the room can run the move this week. The rest of the note smuggles costume. "
            f"{planted} Leadership still wants a six-month Gantt by Friday and treats a pretty demo as proof. "
            f"The contractor-onboarding case is on the table: findability, pre-fill, and a demo date. "
            f"Nobody writes a fail rule. WIP is high. The Check is mood. Orient is skipped. "
            f"Someone says we already know, so skip diamond 1. A HiPPO scores in minute two. "
            f"Quality is promised after the tweet. On-call is nobody."
        )
        words = scene.split()
        if len(words) < 120:
            scene += " The facilitator parks critiques on a later list and names the mode on the wall, which is the correct protocol, then the room ignores it."
        out.append({
            "id": L["id"],
            "num": L["num"],
            "title": L["title"],
            "scene": scene,
            "ok": [
                "The named move is a coat, not an identity.",
                "A facilitation script exists so the room can run the move this week.",
            ],
            "errors": errors,
        })
    return out


def inject_array(path: Path, const_name: str, value) -> None:
    text = path.read_text(encoding="utf-8")
    pat = re.compile(rf"const {const_name} = \[.*?\n    \];", re.S)
    replacement = f"const {const_name} = {json.dumps(value, ensure_ascii=False, indent=2)};"
    replacement = replacement.replace("\n", "\n    ")
    replacement = "    " + replacement
    if not pat.search(text):
        raise SystemExit(f"no {const_name} in {path.name}")
    path.write_text(pat.sub(replacement, text, count=1), encoding="utf-8")
    print("injected", const_name, "->", path.name)


def main() -> None:
    lessons = load_lessons()
    bank = questions(lessons)
    (QUIZ / "questions.js").write_text(
        f"/** Atlas of the Build Loop — multi-deck bank ({len(bank)}) */\nwindow.QUESTIONS = "
        + js(bank)
        + ";\n",
        encoding="utf-8",
    )
    print("wrote questions.js", len(bank))

    decks, fermi, steel = [], [], []
    for L in lessons:
        decks.append({
            "id": L["id"], "num": L["num"], "title": L["title"],
            "terms": [list(t) for t in L["terms"]],
            "misc": [list(m) for m in L["misc"]],
        })
        fermi.append({
            "id": L["id"], "num": L["num"], "title": L["title"],
            "pairs": [
                {"id": f"t{i}", "left": t[0], "right": t[1], "why": "From this lesson’s Key Terms table."}
                for i, t in enumerate(L["terms"])
            ],
        })
        steel.append({
            "weak": L["misc"][0][0],
            "model": "Steelman: name the fear or incentive underneath, then the fair condition, then the limit. Reality from the lesson: " + L["misc"][0][1],
            "lessonId": L["id"], "title": L["title"],
        })
        for m in L["misc"][1:3]:
            steel.append({
                "weak": m[0],
                "model": "Fair form, then the limit. " + m[1],
                "lessonId": L["id"], "title": L["title"],
            })

    inject_array(LABS / "spaced.html", "DECKS", decks)
    inject_array(LABS / "fermi.html", "DECKS", fermi)
    inject_array(LABS / "bias.html", "SCENES", scenes(lessons))
    inject_array(LABS / "steelman.html", "ITEMS", steel)

    fermi_html = (LABS / "fermi.html").read_text(encoding="utf-8")
    fermi_html = re.sub(
        r"const BODY = new Set\(\[[^\]]*\]\);",
        "const BODY = new Set(" + json.dumps(sorted(ARC_A | ARC_B)) + ");",
        fermi_html,
        count=1,
    )
    fermi_html = re.sub(
        r"const BLOOD = new Set\(\[[^\]]*\]\);",
        "const BLOOD = new Set(" + json.dumps(sorted(ARC_C | ARC_D)) + ");",
        fermi_html,
        count=1,
    )
    fermi_html = fermi_html.replace('["body", "Arc A–B · door + methods"]', '["door", "Arc A–B · door + methods"]')
    fermi_html = fermi_html.replace('["blood", "Arc C–D · tools + ship"]', '["tools", "Arc C–D · tools + ship"]')
    fermi_html = fermi_html.replace('v === "body"', 'v === "door"')
    fermi_html = fermi_html.replace('v === "blood"', 'v === "tools"')
    fermi_html = fermi_html.replace('q === "body" || q === "blood"', 'q === "door" || q === "tools"')
    fermi_html = fermi_html.replace('return "body"', 'return "door"')
    fermi_html = fermi_html.replace('return "blood"', 'return "tools"')
    (LABS / "fermi.html").write_text(fermi_html, encoding="utf-8")
    print("patched fermi sets")


if __name__ == "__main__":
    main()
