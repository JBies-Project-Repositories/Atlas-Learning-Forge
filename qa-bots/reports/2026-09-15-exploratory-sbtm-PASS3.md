# SBTM Session Report — **PASS 3** / 2026-09-15

**Tester:** Exploratory Session Tester  
**Pass:** PASS 3 (16-lesson field atlas)  
**Date:** 15 Sep 2026, ~4:48–4:54 PM PT  
**Target URL:** `http://127.0.0.1:8765/` (entry `00_CLICK_HERE_TO_BEGIN.html`)  
**Pack path:** `/workspace/atlas-study-pack/pack/`  
**Methodology:** Session-based exploratory testing (SBTM) only.  
**Brief:** `/workspace/qa-reports/pass-3/PASS3_BRIEF.md`  
**Compared to:** Pass 2 (`/workspace/qa-reports/pass-2/exploratory-sbtm-PASS2.md`) — 7-lesson primer. This pass is the **16-lesson** build only.

---

## Charter

Can a new learner spend a week in **one arc** and **run the facilitation script**, not only name the diagram? Note **case dossier** and **ops checklist**.

**Charter answer: Yes** (with one discoverability nit on the standalone ops file).

Evidence:
- Cover and Contents present **four arc-packs / sixteen lessons** and state a **week per arc** as a reasonable path (map-skim is explicitly not the point).
- Lesson 01 includes a facilitator-owned **“Facilitation script: twenty generate, fifteen converge”** with timed blocks (35-minute block + 5-minute close; wall language; senior-person rules). A competent facilitator could run it from the page without inventing the clock.
- Lesson 03 includes another timed script (**after-action Orient vs task-list update**). Static scan: every lesson HTML contains a facilitation / wall-script section; Arc A–C and Arc D go/no-go scripts are runnable in the same sense.
- **Case dossier** (`01_source/CASE_DOSSIER.md`) and **ops checklist** (`01_source/OPS_CHECKLIST.md`) are linked from Contents (suggested path + Practice tools for dossier; ops in Arc D path line). Both return HTTP 200 and are readable as source text.

---

## Time box

Assigned 45–60 min. Live tour ~15–20 min focused on Arc A as “week one,” plus static corroboration of scripts / dossier / ops / deck IDs. Debrief folded into this report.

---

## Environment

- Shared origin `http://127.0.0.1:8765/` (server HTTP 200). Parallel Pass 3 testers may share the origin; dirty-progress risk noted where relevant.
- Not testing the old 7-lesson primer. Live HTML/JS checked: **no** `01_The_Loop` / `bl-01-loop` stems in pack HTML (brief exception for archive `INTEGRITY_REPORT` not used as live UI).

---

## Heuristics / tours

| Heuristic | Use |
| --- | --- |
| Charter / capability tour | Can the learner *run* a facilitation script after one arc week, not only recognize a diagram? |
| Feature / landmark | Contents as atlas; facilitation headings; case + ops artifacts |
| Counting / recognition | 16 lesson cards; arc grouping A–D; Arc A deck filter → 4×8 = 32 |
| Questioning | Where is ops checklist vs dossier? How do `.md` sources render in-browser? |
| Continuity | Contractor-onboarding case across L01 script → dossier → ops |

---

## Path taken

1. `00_CLICK_HERE_TO_BEGIN.html`  
2. `index.html` (cover — four arcs)  
3. `contents.html` (16 cards, suggested week-per-arc path, dossier + ops links)  
4. `02_lessons/01_Divergent_and_Convergent.html` — scrolled to facilitation script  
5. `02_lessons/03_PDCA_and_OODA.html` — second facilitation script  
6. `01_source/CASE_DOSSIER.md`  
7. `01_source/OPS_CHECKLIST.md`  
8. `decks.html` → **Arc A door** (selects L01–L04) → start quiz  
9. One practice answer (OODA-related) → instant Correct feedback  

Screenshots: `pack/docs/screenshots/2026-09-15/pass-3/` (also `qa-reports/pass-3/exploratory-evidence/`).

---

## Areas covered

| Surface | Observation |
| --- | --- |
| Begin | Field-atlas messaging (four arc-packs / sixteen lessons; deep enough to run, not only to name). |
| Cover | Four arc panels; week-per-arc guidance; Contents / Lesson 1 CTAs. |
| Contents | **16** lesson cards in four arcs; suggested path Arc A→SRS … Arc D→Steelman + **case dossier** + **ops checklist**; Practice tools includes dossier card (not a separate ops card). |
| L01 facilitation | Timed 20/15 (+ close) script with wall lines, silent add, spoken add, cluster seam, converge, close artifact. Runnable, not decorative. |
| L03 facilitation | Timed Orient vs task-list script present. |
| Case dossier | Through-line table Arc A–D; named moves; one-page brief. Useful after Arc D (as labeled). Opens as raw markdown in browser. |
| Ops checklist | Quality / Operations / Mode checkboxes; “more than two unchecked → still learning mode.” Useful at go/no-go. Same raw-markdown presentation. |
| Decks / quiz | Button label **“Arc A door”** (not “Arc A only”). Selection → **4 decks · 32 questions**. Instant Correct on one practice item. Defaults still all-16 checked until Arc button used (continuing Pass 1/2 pattern; not re-opened as P0). |
| Old primer stems | Not observed in live lesson/deck UI. Live decks use `bl-a1-diverge` … `bl-d4-launch` (16×8 = 128 in `questions.js`). |

---

## Findings (observed only)

### P3-F1 — Minor — Raw `.md` dossier/ops show UTF-8 mojibake in Chrome

**What:** Opening `http://127.0.0.1:8765/01_source/CASE_DOSSIER.md` and `OPS_CHECKLIST.md` shows plain/raw text (not HTML-rendered markdown). Punctuation displays as mojibake (e.g. `â€”`, `â€™`, `â†’`). Files on disk are valid UTF-8; HTTP body matches disk. Response `Content-Type: text/markdown` (no charset).

**Why it matters for charter:** Learner can still read the substance, but the standalone dossier/ops look less polished than lesson HTML and may undermine confidence in “ops at ship” artifacts.

**Repro:** Navigate from Contents to case dossier or ops checklist links; observe title line and table punctuation.

**Evidence:** `exploratory-evidence/07-case-dossier.png`, `08-ops-checklist.png`.

### P3-F2 — Nit — Ops checklist weaker on Contents “Practice tools” grid

**What:** Case dossier has a Practice tools card. Ops checklist appears in the **suggested path** Arc D bullet and as files under `01_source/`, and is taught inside Lesson 16, but has **no** sibling card in the Practice tools grid.

**Why it matters:** A learner exploring mid-pack tools may find the dossier and miss the standalone ops file until Arc D path or L16.

**Repro:** Open Contents → Practice tools; compare Case card vs absence of Ops card; ops still linked in suggested path step 4.

---

## Non-findings / constraints honored

- No invented defects. No private master prompt tested.  
- No Pass 1/2 P0s reopened without a reproduced regression on this build.  
- Default-all decks and cover book-front nav patterns noted only as continuity, not as new P0s.  
- Accessibility contrast / keyboard ownership left to Accessibility WCAG Tester; smoke path ownership left to Smoke.

---

## Surprises

1. Arc filter control labeled **“Arc A door”** (metaphor matches Arc A title; still clear once used).  
2. Facilitation title “twenty generate, fifteen converge” schedules a **40-minute** clock including a 5-minute close (35+5), which matches the intro sentence — naming vs clock is consistent if you read the whole script.  
3. Quiz bank is **128** items (16×8), superseding Pass 2’s 56.

---

## Open questions

1. Should `text/markdown` responses declare `charset=utf-8`, or should dossier/ops ship as HTML companions for learners who never leave the browser?  
2. Should Practice tools gain an Ops checklist card next to Case?  
3. Does a first-week learner who only finishes Arc A know the dossier is intentionally “read after Arc D,” or do they open it early and feel lost? (Contents says after Arc D; dossier header repeats that.)

---

## Ideas / follow-up charters

1. **Week-in-Arc-B** — brief-writing workshop (L08) end-to-end with dual-track split (L05).  
2. **Ship gate** — run L16 20-minute go/no-go against `OPS_CHECKLIST.md` with a forced red cell.  
3. **Dossier continuity** — skim one worked example per arc against the dossier table for drift.

---

## Suggested follow-up for Lead / sponsor delta

| Topic | Pass 3 SBTM signal |
| --- | --- |
| Atlas depth | Facilitation scripts are **runnable**; charter met for Arc A week-one. |
| Case + ops | Present and useful; raw-md + mojibake (P3-F1) and ops card gap (P3-F2) are polish, not blockers. |
| vs Pass 2 | Product is a different depth class (16 lessons / 128 Q / arc-packs). Do not score against 7-lesson FIX list as regression unless a named FIX regresses. |

---

## Evidence index

| File | What |
| --- | --- |
| `docs/screenshots/2026-09-15/pass-3/01-begin.png` | Begin |
| `…/02-cover.png` | Cover four arcs |
| `…/03-contents.png` | Contents / 16 lessons (also `03-contents-16-lessons.png`) |
| `…/04-l01-facilitation-a.png` | L01 script heading + timed start |
| `…/05-l01-facilitation-b.png` | L01 script continued |
| `…/06-l03-facilitation.png` | L03 Orient script |
| `…/07-case-dossier.png` | Case dossier raw + mojibake |
| `…/08-ops-checklist.png` | Ops checklist raw |
| `…/09-decks-arc-a.png` | Arc A door / 4×32 |
| `…/10-quiz-feedback.png` | Practice Correct |

Mirror: `/workspace/qa-reports/pass-3/exploratory-evidence/`.

---

## Session debrief (SBTM)

**Charter met.** A new learner can treat Arc A as a week, open L01, and run a real facilitation script with a clock and wall language. Case dossier and ops checklist exist, are linked, and support the through-line / ship gate. Remaining issues are presentation and findability of the standalone markdown artifacts, not missing pedagogy.

**Stop:** Report written; no blockers for further squad methods.
