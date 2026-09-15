# QA/Tester Lead — reconstruction brief (Pass 3 target)

**From:** Jenner / Grok Build session  
**Date:** 2026-09-15  
**Target app (name this to the squad):** Atlas of the Build Loop — Study Pack, **16-lesson field atlas** (four arc-packs).  
**Entry:** `00_CLICK_HERE_TO_BEGIN.bat` → HTTP `http://127.0.0.1:8765/`  
**Desktop:** `C:\Users\jbies\OneDrive\Desktop\Atlas of the Build Loop — Study Pack\`  
**Git mirror:** `pack/` on Atlas-Learning-Forge

## What changed (do not test the primer)

The 7-lesson speaking primer is **retired**. Each arc is now four pack-depth lessons. Quiz is **8 × 16 = 128**. Labs must list **every new `lessonId`**. Cover, contents, decks, dashboard, wrap.py, and keys are the same family (`atlas_build_loop_*_v1`) but lesson stems changed.

Old stems (`01_The_Loop`, `bl-01-loop`, …) must **not** appear in live HTML.

New ids: `bl-a1-diverge` … `bl-d4-launch` (see `01_source/_lessons_meta.tsv`).

## What to tell each tester

Seat the same two channels (cap six). Each tester runs **only their method**. Reports go to you as markdown; you compile the sponsor delta vs Pass 2.

1. **Smoke & Sanity** — Begin → Cover (four arc panels) → Contents (16 cards) → L01 → L16 prev/next chain → decks (none + Arc A + all) → quiz subtitle matches filter → one lab per type → dashboard visits for a new stem → theme → reset (theme kept). 8/8 or name the break.
2. **Exploratory SBTM** — Charter: “Can a new learner spend a week in **one arc** and run the move (facilitation script), not only name it?” 45–60 min. Log surprises on arc-pack vs map, case dossier, ops checklist, primary-source links.
3. **Boundary & Equivalence** — Deck query: empty, one id, one arc (4 ids), all 16, unknown id. Exam unanswered must not inflate unique-answer count. Quiz size 8 / 16 / 32 / 56 / 128.
4. **Usability heuristics** — Contents as an atlas (not 7 cards). Facilitation scripts scannable? Arc heads readable light/dim. Cover h2 “The four arcs.”
5. **Accessibility WCAG** — Skip/`main` on chrome + new lessons. Quiz `#quiz-status` after a practice answer. Dim `.badge` contrast. Steelman label focuses textarea. Theme `aria-pressed`.
6. **Risk-based** — Reregister: wrong `lessonId` in labs vs quiz; broken prev/next at arc boundaries (L04→L05, L08→L09, L12→L13); file:// vs HTTP progress; 128-question exam performance; primary links outbound.
7. **Performance observation** — 16 dense HTML lessons + 128-question bank on localhost. Note first quiz load and L13–L16 size. No load testing.

## Evidence

Screenshots under `docs/screenshots/2026-09-15/pass-3/` (create it). Sponsor report: delta vs Pass 2 — did atlas-depth land, and are P0 launch paths still green.

## Do not

- Re-open Pass 1/2 P0s unless you can reproduce a **regression**.
- Test the private master prompt (it is not in the public repo).
- Invent findings. Stand-by on unassigned surfaces.

## Done when

Seven methodology reports + your sponsor compile exist. If P0s appear, write a CLI fix brief the same way as Pass 1/2.
