# Boundary Value Analysis & Equivalence Partitioning Report — **PASS 2**

**Label:** PASS 2 / 2026-09-15  
**App:** Atlas of the Build Loop — Study Pack (post-fix build)  
**Tester:** Boundary & Equivalence Tester  
**Methodology:** Boundary value analysis (BVA) and equivalence partitioning only  
**Target URL:** http://127.0.0.1:8765/00_CLICK_HERE_TO_BEGIN.html  
**Pack path:** `pack/`  
**Compared to:** Pass 1 report `qa-bots/reports/2026-09-15-boundary-equivalence-atlas-study-pack.md`  

---

## 1. Methodology

PASS 2 re-ran **key input edges** emphasized by QA/Tester Lead on the refreshed pack: empty deck selection, steelman length 39/40, exam unanswered counting, dashboard reset+theme, weak-history clear, progress-bar cap, and invalid theme. Equivalence classes and min/just-below/just-above/max (or option edges) were exercised in the browser. Origin started **dirty**; progress / weak / SRS keys were cleared mid-pass before clean rechecks (noted where it affected early dashboard readings).

---

## 2. Partitions / edges re-tested

| Area | Boundaries exercised |
|---|---|
| Deck chooser | 0 selected (empty), 1 selected, all selected |
| Steelman text | empty, 39 chars, 40 chars + 0 rubric |
| Steelman grader domain | Build Loop vs cardio/physiology |
| Exam submit | 0 of 8 answered, 1 of 8 answered |
| Reset confirm | cancel vs OK; theme keep vs progress clear |
| Weak history | populated → clear (immediate UI) |
| Lab bar | actions 19 / 20 / 21 (cap) |
| Theme storage | invalid `"purple"` → light |

---

## 3. Process / steps

1. Confirmed HTTP 200 on shared URL; inspected updated `decks.html`, `dashboard.html`, `03_quiz/app.js`, `04_labs/steelman.html` for FIX-related boundary changes.
2. Executed browser BVA matrix (clean storage after initial dirty observation).
3. Scored FIX-01–10 as FIXED / PARTIAL / STILL OPEN / NOT IN SCOPE from BVA evidence only.
4. Wrote this PASS 2 report to disk and DMed QA/Tester Lead.

---

## 4. Test matrix and results

### Deck chooser (empty vs one vs all) — FIX-01

| ID | Case | Expected | Observed | Result |
|---|---|---|---|---|
| D1 | Open decks.html | Page loads | Loaded | PASS |
| D2 | Select none | Error “Select at least one deck”; go disabled | Error shown; navigation blocked | PASS |
| D3 | Activate go with none | Stay; error remains | Stayed; error shown | PASS |
| D4 | Exactly one deck | Error hidden; quiz with that deck | Linked `decks=bl-01-loop` | PASS |
| D5 | Select all | Opens all decks | Linked `decks=all` | PASS |

### Steelman 39/40 + domain — FIX-02 / prior DEF-BVA-03

| ID | Case | Expected | Observed | Result |
|---|---|---|---|---|
| S1 | Empty → Score | Visible block message (≥ ~40 chars) | Visibly blocked with message | PASS |
| S2 | Exactly 39 chars | Still blocked + message | Blocked | PASS |
| S3 | Exactly 40 chars, 0 checks | Allow; `0/5` | `0/5` | PASS |
| S4 | Grader prompt domain | Build Loop (loops/shipping), not cardio | Build Loop loops/shipping | PASS |

### Exam unanswered counting — FIX-04

| ID | Case | Expected | Observed | Result |
|---|---|---|---|---|
| Q1 | Exam size 8, timer Off, start | 8-question session | As expected | PASS |
| Q2 | Submit with 0 answers | `Answered 0 of 8`; unanswered **not** recorded as answers | `Answered 0 of 8`; unanswered not counted (early dashboard reading was dirty-origin noise) | PASS |
| Q3 | Answer 1 of 8, submit | `Answered 1 of 8`; progress +~1 not +8 | Dashboard increased by one, not eight | PASS |

### Reset + theme — FIX-07 (spec change vs Pass 1)

| ID | Case | Expected (PASS 2) | Observed | Result |
|---|---|---|---|---|
| R1 | Set dim | Dim active | Dim | PASS |
| R2 | Create some progress | Progress present | Present | PASS |
| R3 | Open Reset confirm | Copy lists clears progress/weak/SRS; **Keeps: theme** | Copy matched | PASS |
| R4 | Cancel | Data + dim remain | Remained | PASS |
| R5 | OK Reset | Progress cleared; **dim kept** | Progress cleared; dim kept | PASS |

*Pass 1 DEF-BVA-01 treated theme-after-reset as a fail against the old wipe-all expectation. Under FIX-07, keeping theme is the intended boundary — reclassified as PASS / FIXED.*

### Weak clear — prior DEF-BVA-02

| ID | Case | Expected | Observed | Result |
|---|---|---|---|---|
| W1 | Build weak history | Rows present | Present | PASS |
| W2 | Clear history confirm | Clears storage | Cleared | PASS |
| W3 | UI update | Immediate empty/cleared message (no full reload) | Updated immediately without reload | PASS |

### Progress bar + invalid theme

| ID | Case | Expected | Observed | Result |
|---|---|---|---|---|
| P1 | actions 19 / 20 / 21 | ~95% / 100% / 100% cap | As expected | PASS |
| T1 | theme=`purple` | Fall back to light | Light | PASS |

### Summary counts (PASS 2 edge matrix)

| Result | Count |
|---|---|
| PASS | 20 |
| FAIL | 0 |
| BLOCKED / NOT RUN (in this matrix) | 0 for listed IDs |
| **Total executed edge cases** | **20** |

---

## 5. FIX scoring (BVA evidence)

| FIX | Score | Evidence |
|---|---|---|
| FIX-01 Empty decks must not start all | **FIXED** | D2–D5: error text, disabled go, 0/1/all partitions |
| FIX-02 Steelman grader Build Loop domain | **FIXED** | S4: prompt is loops/shipping Build Loop (not cardio/physiology) |
| FIX-03 Quiz badge contrast | **NOT IN SCOPE** | Visual contrast — not a BVA partition edge |
| FIX-04 Progress counting; unanswered skipped | **FIXED** | Q2–Q3: unanswered not counted as answers; +1 not +8. Residual note: exam **percent** still uses `correct / session.length` (unanswered still in denominator) — product nuance, not a regression of the stated fix |
| FIX-05 HTTP launcher / file:// warning | **NOT IN SCOPE** | Docs/BAT — not exercised as input partitions |
| FIX-06 Lesson markLesson / read progress | **NOT IN SCOPE** | Not in PASS 2 BVA edge set (source has `markLesson` hooks; UI progress edge not re-proven here) |
| FIX-07 Reset clears progress, keeps theme | **FIXED** | R3–R5: confirm copy + behavior match |
| FIX-08 Nav + Dashboard from Begin/Cover | **NOT IN SCOPE** | Navigation smoke — not BVA edges this pass |
| FIX-09 Arc-head + Steelman dim contrast; label | **NOT IN SCOPE** | Contrast/a11y — steelman `for="text"` exists in source; contrast not BVA-scored |
| FIX-10 Quiz aria-live / feedback / lock-copy | **NOT IN SCOPE** | a11y live regions — not BVA |
| FIX-11…15 | **NOT ENCOUNTERED** | No additional FIX ids hit in this method |

---

## 6. Pass 1 defects disposition

| Pass 1 ID | Disposition on PASS 2 |
|---|---|
| DEF-BVA-01 Theme survives Reset | **Superseded / FIXED under new spec (FIX-07)** — keeping theme is correct |
| DEF-BVA-02 Weak Areas UI stale | **FIXED** (W3) |
| DEF-BVA-03 Steelman empty validation silent | **FIXED** (S1 — visible `#score-error` / message) |

**No confirmed remaining BVA defects** from this PASS 2 edge matrix.

---

## 7. Gaps / residual notes

1. Shared origin was initially dirty; early dashboard observations for Q2 required a clean recheck — recommend testers clear Atlas keys (except theme if testing FIX-07) before Pass 2 comparisons.
2. Exam score percentage still divides by full session length while unanswered are excluded from answer/progress recording — clarify if denominator should be `answered` only.
3. FIX-06 markLesson progress not boundary-exercised this pass.
4. Full Pass 1 breadth (spaced grades, fermi, bias, all timer sizes) was **not** re-run; PASS 2 scoped to key edges + FIX scoring.

---

## 8. Artifacts

- This report: `qa-bots/reports/pass-2/boundary-equivalence-PASS2.md`

---

*End of PASS 2 BVA / equivalence partitioning report. Scope limited to this methodology only.*
