# Smoke & Sanity Test Report — **PASS 2** / 2026-09-15

**Tester:** Smoke & Sanity Tester  
**Lead:** QA/Tester Lead  
**Target:** Atlas of the Build Loop — Study Pack (UPDATED / post-fix build)  
**Environment:** `http://127.0.0.1:8765/` — pack `pack/`  
**Auth:** None  
**localStorage:** Cleared before testing (origin had been dirty: ~58.3 KB prior progress visible). Cleared: **YES**.

---

## Methodology

Fixed **smoke / sanity** checklist only on the refreshed pack. Critical surfaces + assigned smoke emphasis: FIX-01 (Select none), theme toggle, reset Cancel/OK, FIX-08 nav/Dashboard from Begin/Cover. No exploratory, BVA, heuristics, or WCAG deep-dive.

---

## Critical surface checklist

| # | Check | Result | Evidence |
|---|--------|--------|----------|
| 1 | Begin opens | **PASS** | `00_CLICK_HERE_TO_BEGIN.html` — “CLICK HERE TO BEGIN — Atlas of the Build Loop.” |
| 2 | Open the cover | **PASS** | `index.html` — “Atlas of the Build Loop.” |
| 3 | Contents | **PASS** | `contents.html` — “What’s in the pack.” |
| 4 | Lesson 1 | **PASS** | `02_lessons/01_The_Loop.html` — “The Loop.” |
| 5 | Quiz decks | **PASS** | `decks.html` — “Deck Chooser.” |
| 6 | Labs + happy path | **PASS** | `04_labs/index.html` — “Interactive Labs”; opened Spaced Repetition Lab; revealed an L01 answer |
| 7 | Dashboard | **PASS** | `dashboard.html` — “Progress Dashboard.” |
| 8 | Theme toggle | **PASS** | Bright → Dim → Bright; control/state changed correctly |
| 9 | Nav + Dashboard from Begin/Cover (FIX-08) | **PASS** | Begin tiles and site nav exposed Dashboard and navigated correctly |

**Overall checklist:** **9 / 9 PASS**

---

## FIX verification scores (smoke scope)

| ID | Score | Notes |
|----|-------|-------|
| FIX-01 Empty decks must not start all | **FIXED** | “Select none” cleared decks; Start showed “Select at least one deck”; did not start all. (Automation timed out on disabled Start; validation message confirmed visually.) |
| FIX-07 Reset clears progress, keeps theme | **FIXED** | Cancel preserved state/theme. Confirm cleared quiz, weak-area, SRS, and lab progress; theme retained. |
| FIX-08 Nav + Dashboard from Begin/Cover | **FIXED** | Dashboard reachable from Begin/Cover paths. |
| Theme toggle | **FIXED** | Dim/Bright works. |
| FIX-02 Steelman domain | **NOT IN SCOPE** | Not exercised in smoke. |
| FIX-03 Quiz badge contrast | **NOT IN SCOPE** | Deferred to a11y/visual. |
| FIX-04 Progress / unanswered exam | **NOT IN SCOPE** | Not deep-checked in smoke. |
| FIX-05 HTTP launcher / file:// warning | **NOT IN SCOPE** | README/BAT not smoke-exercised. |
| FIX-06 Lesson markLesson / read progress | **NOT IN SCOPE** | Not smoke-exercised beyond Lesson 1 open. |
| FIX-09 Arc-head + Steelman dim contrast / labels | **NOT IN SCOPE** | Deferred. |
| FIX-10 Quiz aria-live / feedback / lock-copy | **NOT IN SCOPE** | Deferred to a11y. |
| FIX-11…15 | **NOT IN SCOPE** | Not encountered. |

---

## Exact steps (summary)

1. Cleared site data for `127.0.0.1:8765`.  
2. Opened begin → Open the cover → contents → Lesson 1.  
3. Opened Deck Chooser; Select none → Start → confirmed “Select at least one deck” and no full-deck start.  
4. Labs index → Spaced Repetition Lab → reveal L01 answer.  
5. Dashboard load; theme Bright/Dim/Bright.  
6. Verified Dashboard from Begin/Cover navigation.  
7. Reset: Cancel preserved; Confirm cleared progress counters to zero, theme kept.

---

## Blockers

**None** for the smoke checklist. Notes: disabled Start control caused an automation timeout on FIX-01 (message still confirmed); native reset confirm used desktop interaction.

---

## Residual risk (smoke-only)

- Surface smoke only; no full quiz (56 Q), no exhaustive labs, no persistence edge matrix beyond reset/theme.  
- FIX-02–06, 09–15 left to other methodologies or deeper passes.  
- Shared-origin dirty state was cleared for this pass; other agents may re-dirty the same origin.

---

## Screenshots

- Begin: `(session browser shots)/shot-call_gqIJwC9lDkUQhpDFARhqrFp1fc_0fe8ce33fe2a1b64.png`  
- Cover: `(session browser shots)/shot-call_ODm5N9DEbvPIC5ApUa9OLW0hfc_0fe8ce33fe2a1b64.png`  
- Contents: `(session browser shots)/shot-call_3Fe5BkVid0115ohQM8vvxHUqfc_0fe8ce33fe2a1b64.png`  
- Lesson 1: `(session browser shots)/shot-call_u4uSOp2jvBbHn24Ah1e5FpcCfc_0fe8ce33fe2a1b64.png`  
- FIX-01 validation: `(session browser shots)/shot-call_fiheu7CjWz9V7lBixdsehQoFfc_0fe8ce33fe2a1b64.png`  
- Labs index: `(session browser shots)/shot-call_FDtQmkga0x48ZWDFECtCRj1kfc_0fe8ce33fe2a1b64.png`  
- Spaced lab: `(session browser shots)/shot-call_xKdZ5jCzoSvL0wxLCUYCGt21fc_0fe8ce33fe2a1b64.png`  
- Dashboard: `(session browser shots)/shot-call_FtbjYQuKJoLgbs727gFcra4bfc_0fe8ce33fe2a1b64.png`  
- Dim theme: `(session browser shots)/shot-call_1mbjISZ3WqfJRnEnLE54Wr4jfc_0fe8ce33fe2a1b64.png`  
- Reset dialog / final: under agent assets (`009da1a1…webp`, `298e315c…webp`)

---

*End of Smoke & Sanity **PASS 2** report.*
