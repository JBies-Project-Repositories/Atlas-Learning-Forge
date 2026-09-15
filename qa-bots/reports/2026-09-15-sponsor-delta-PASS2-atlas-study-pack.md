# Pass 2 Sponsor Delta — Atlas of the Build Loop Study Pack

| Field | Value |
| --- | --- |
| **Sponsor** | Jenner |
| **QA lead** | QA/Tester Lead |
| **Pass** | **PASS 2** (verification on post–CLI-fix build) |
| **Date** | 2026-09-15 (America/Los_Angeles) |
| **Target URL** | `http://127.0.0.1:8765/` |
| **Pack** | `pack/` (refreshed from Desktop Study Pack) |
| **Compared to** | Pass 1 sponsor report + CLI fix brief FIX-01…15 |

---

## 1. Executive verdict

**Pass 2 is complete (7/7 methodology reports).** Under the recommended **HTTP** launch path, the pack is **shippable for learning** with **no critical-path blockers**.

Pass 1 P0 functional defects are **closed**: empty decks no longer start all 56, Steelman grader is Build Loop domain, unanswered exam items no longer inflate answered counts, reset keeps theme, lesson visits show on Dashboard, Begin/Cover reach Dashboard.

**Remaining medium polish (not ship-blockers on HTTP):**
1. Dim-theme quiz `.badge` contrast ~1.81:1 (NR01 / FIX-03 incomplete)
2. Sibling `Open *.bat` shortcuts still use `file://` (NR02 / FIX-05 incomplete)
3. Quiz chrome still hardcodes “7 decks · 56 questions” on filtered decks
4. A11y residuals: level pill live visibility, quiz-status announce unconfirmed, skip/`main`/cover headings uneven

**Performance:** No regression vs Pass 1 on localhost.

---

## 2. Report inventory (Pass 2)

| Methodology | File | Headline |
| --- | --- | --- |
| Smoke & Sanity | `smoke-sanity-PASS2.md` | 9/9 PASS; FIX-01/07/08 FIXED |
| Exploratory (SBTM) | `exploratory-sbtm-PASS2.md` | Charter satisfied; FIX 01/02/05/06 FIXED; 04/07/08 PARTIAL; residual subtitle |
| Boundary & Equivalence | `boundary-equivalence-PASS2.md` | 20/20 PASS; FIX-01/02/04/07 FIXED; DEF-BVA-01–03 cleared |
| Usability Heuristics | `usability-heuristics-PASS2.md` | **0 majors left** (was 6); FIX 01/02/03/05/06/07/08/10 FIXED; 04/09 PARTIAL |
| Accessibility WCAG | `Accessibility_WCAG_PASS2.md` | V2/V3/V5/V7/V8/V12 FIXED; V1/V4/V6/V9/V10 PARTIAL; V11 OPEN |
| Risk-Based | `risk-based-PASS2.md` | R01/R03/R04 FIXED; R02 PARTIAL; NR01/NR02 OPEN |
| Performance | `performance-observation-PASS2.md` | No regression; FIX N/A for perf |
| **This delta** | `SPONSOR_DELTA_PASS2_Atlas_Study_Pack_2026-09-15.md` | Lead rollup |

Evidence folders: `docs/screendocs/screenshots/2026-09-15/pass-2/accessibility-wcag/2026-09-15/pass-2/exploratory-sbtm/`, `docs/screendocs/screenshots/2026-09-15/pass-2/accessibility-wcag/2026-09-15/pass-2/accessibility-wcag/`.

---

## 3. FIX-01…15 lead consensus (Pass 2)

Lead rollup uses **functional** verdict first; a11y-only PARTIAL notes where methods disagree.

| FIX | Lead verdict | Notes |
| --- | --- | --- |
| **FIX-01** Empty decks → all | **FIXED** | Smoke/BVA/Usability/Exploratory/Risk agree. A11y: AT polish PARTIAL (announce/focus). |
| **FIX-02** Steelman grader domain | **FIXED** | Confirmed live + source. |
| **FIX-03** Quiz badge contrast | **PARTIAL** | Level badge CSS improved; **dim `.badge` ~1.81:1 FAIL**; a11y saw blank level pill live. |
| **FIX-04** Progress / unanswered exam | **FIXED** | BVA + Risk prove skips; unique-ID counting. Residual: hardcoded quiz subtitle; exam % denominator nuance. |
| **FIX-05** HTTP / file:// docs | **PARTIAL** | Primary BAT + README/START HERE good; **Open*.bat still file://**. |
| **FIX-06** markLesson | **FIXED** | Lessons wire + Dashboard shows visits. |
| **FIX-07** Reset keeps theme | **FIXED** | Smoke/BVA/Usability/Risk; Exploratory dirty-origin caveat superseded by clean-pass evidence. |
| **FIX-08** Dashboard from Begin/Cover | **FIXED** | Dashboard reachable; Cover still book-front (no full topbar) — acceptable residual. |
| **FIX-09** Arc-head / Steelman contrast+label | **FIXED** *(core)* / **PARTIAL** *(a11y polish)* | Arc-head + New prompt dim FIXED; label markup FIXED; label-click focus unconfirmed. |
| **FIX-10** aria-live / lock-copy | **FIXED** *(core)* / **PARTIAL** *(announce)* | Main live-region removed; lock-copy named; quiz-status announce unconfirmed. |
| **FIX-11** Weak panel refresh | **FIXED** | BVA W3. |
| **FIX-12** Steelman empty validation | **FIXED** | BVA S1. |
| **FIX-13** SRS rating copy | **FIXED** | Risk/Usability. |
| **FIX-14** Timer hint vs options | **FIXED** | Risk. |
| **FIX-15** Skip / main / focus-visible | **PARTIAL** | Improved on some pages; not pack-wide. |

---

## 4. Pass 1 → Pass 2 deltas (what closed)

| Pass 1 issue | Pass 2 |
| --- | --- |
| Empty decks → all 56 | **Closed** |
| Steelman cardio grader | **Closed** |
| Exam unanswered inflate answered | **Closed** |
| Reset cleared theme | **Closed** (now keeps theme by design) |
| Lesson progress dead | **Closed** |
| Begin/Cover no Dashboard | **Closed** |
| Usability majors (6) | **0 remaining** |
| Arc-head contrast fail (light) | **Closed** |
| Quiz main aria-live | **Closed** |
| Steelman New prompt dim contrast | **Closed** |
| Weak UI stale / silent steelman empty | **Closed** |
| Performance concerns on localhost | **Unchanged — still strong** |

---

## 5. Still open (Pass 3 / polish backlog)

### P1 polish
1. **Dim `.badge` contrast** (NR01) — darken text or accent in dim theme (≥4.5:1).
2. **Sibling Open*.bat → HTTP** (NR02) — match primary BAT or warn/remove.
3. **Quiz subtitle** — bind to filtered deck count (not hardcoded 7/56).
4. **Quiz level pill live visibility** — confirm computed styles / fix blank pill.
5. **Quiz-status announcement** — ensure `#quiz-status` populates for AT.

### P2 polish
6. Default all-decks pre-check (first-timer exam-by-default) — product choice.
7. Theme `aria-pressed`; skip/`main` pack-wide; cover heading structure (V11).
8. Chooser→`decks=all` one-off (Usability) — reproduce or close.

---

## 6. Disposition

| Question | Answer |
| --- | --- |
| Pass 2 complete? | **Yes — 7/7** |
| Ship under HTTP? | **Yes**, with known polish backlog |
| Re-run full Pass 3 needed? | **Only after NR01/NR02 + subtitle/badge polish**, then smoke + a11y spot check |
| CLI next feed? | Optional short polish brief from §5 |

---

## 7. Paths for Clerk / Desktop

```
qa-bots/reports/pass-2/
  smoke-sanity-PASS2.md
  exploratory-sbtm-PASS2.md
  boundary-equivalence-PASS2.md
  usability-heuristics-PASS2.md
  Accessibility_WCAG_PASS2.md
  risk-based-PASS2.md
  performance-observation-PASS2.md
  SPONSOR_DELTA_PASS2_Atlas_Study_Pack_2026-09-15.md
  docs/screendocs/screenshots/2026-09-15/pass-2/accessibility-wcag/2026-09-15/pass-2/exploratory-sbtm/
  docs/screenshots/2026-09-15/pass-2/accessibility-wcag/
```

Desktop copies (this compile):
- `SPONSOR_DELTA_PASS2_Atlas_Study_Pack_2026-09-15.md`
- Clerk target: `Dev project 1\commits\pass 2\` (Clerk assembles full pack)

---

*Compiled by QA/Tester Lead for sponsor Jenner — Pass 2 complete 2026-09-15 PT.*
