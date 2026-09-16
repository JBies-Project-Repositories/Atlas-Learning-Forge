# Smoke & Sanity Test Report — **PASS 3** / 2026-09-15

**Tester:** Smoke & Sanity Tester  
**Lead:** QA/Tester Lead  
**Target:** Atlas of the Build Loop — Study Pack (**16-lesson field atlas**)  
**Environment:** `http://127.0.0.1:8765/` — pack `/workspace/atlas-study-pack/pack/`  
**Auth:** None  
**Note:** NOT the old 7-lesson primer. No `01_The_Loop` / `bl-01-loop` observed in live HTML.  
**Site-data clear:** Separate browser site-data/localStorage clear: **N**. App reset cleared progress data.

---

## Methodology

Fixed **smoke / sanity** checklist only on the 16-lesson atlas. Critical path: Begin → Cover (four arcs) → Contents (16 cards) → L01–L16 prev/next (esp. arc boundaries) → decks none / Arc A / all → one of each lab → dashboard → theme → reset (theme kept). No invented findings. No re-open of Pass 1/2 P0s (no regressions reproduced).

---

## Checklist results

| # | Check | Result | Evidence |
|---|--------|--------|----------|
| 1 | Begin opens | **PASS** | `/00_CLICK_HERE_TO_BEGIN.html` — “Atlas of the Build Loop” |
| 2 | Cover — four arcs | **PASS** | `/index.html` — four arc-packs visible |
| 3 | Contents — 16 cards | **PASS** | `/contents.html` — “Four arc-packs”, 16 lessons |
| 4 | L01–L16 prev/next (esp. L04→L05, L08→L09, L12→L13) | **PASS** | Navigation verified across L01–L16 including named boundaries; no old Loop content |
| 5 | Decks none — must not start all | **PASS** | Empty selection → “Select at least one deck.” |
| 6 | Arc A only — subtitle matches filter | **PASS** | Subtitle: “4 decks · 32 questions · selected decks” |
| 7 | All decks — subtitle matches | **PASS** | Subtitle: “16 decks · 128 questions” |
| 8 | One of each lab | **PASS** | Spaced, Scenario Audit (bias), Term Match (fermi), Misconception Steelman — each loaded |
| 9 | Dashboard (new stem) | **PASS** | `/dashboard.html` — “Progress Dashboard” |
| 10 | Theme Dim/Bright | **PASS** | Both toggled successfully |
| 11 | Reset — clear progress, keep theme | **PASS** | Confirm: progress to zero, dim theme retained; then restored bright |

**Overall:** **11 / 11 PASS**

---

## Exact steps (summary)

1. Opened begin → cover (confirmed four arcs) → contents (16 lessons).  
2. Walked L01–L16; verified L04→L05, L08→L09, L12→L13.  
3. Deck Chooser: none → blocked with select message; Arc A → filtered quiz subtitle; all → 16 decks / 128 questions.  
4. Opened each of four labs from labs index.  
5. Dashboard visit; theme Dim/Bright.  
6. Reset confirm cleared progress, kept dim theme.

---

## Blockers

**None.** Note: managed dialog interaction for reset was unreliable; final confirm completed via page dialog handler and verified visually.

---

## Residual risk (smoke-only)

- No exhaustive lesson-content or quiz-answer validation.  
- Separate origin site-data clear was not performed this pass (app reset used instead).  
- Smoke only — other methodologies own deeper coverage.

---

## Screenshots

Directory: `/workspace/atlas-study-pack/pack/docs/screenshots/2026-09-15/pass-3/`

Including (among others):
- `10-theme-bright-after-reset.png`
- `11-reset-confirmed-dim-theme.png`

---

*End of Smoke & Sanity **PASS 3** report.*
