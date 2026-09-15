# SBTM Session Report — **PASS 2** / 2026-09-15

**Tester:** Exploratory Session Tester  
**Pass:** PASS 2 (verification on post-fix build)  
**Date:** 15 Sep 2026, ~3:22–3:29 PM PT  
**Target URL:** `http://127.0.0.1:8765/00_CLICK_HERE_TO_BEGIN.html`  
**Pack path:** `pack/`  
**Methodology:** Session-based exploratory testing (SBTM) only.  
**Compared to:** Pass 1 report `qa-bots/reports/2026-09-15-exploratory-sbtm-atlas-study-pack.md`

---

## Charter

Discover how a first-time learner navigates from begin → lesson → quiz item → lab → progress **after CLI fixes**, and note what changed vs Pass 1 surprises.

## Time box

Assigned verification pass (no new 45-min box stated). Live tour ~15–20 minutes + debrief against FIX-01–10.

## Environment

- Shared origin `127.0.0.1:8765`. **Could not clear site data via DevTools** in this session; origin may be dirty from parallel Pass 2 testers. Notes call out where contamination is likely.
- Theme exercised Dim and Bright; ended after reset with Dim still active (theme keep check).

---

## Heuristics / tours

| Heuristic | Use |
| --- | --- |
| First-time learner / happy path | Begin → Cover → Lesson 1 → Quiz → Lab → Dashboard |
| Change-focused / regression tour | Revisit Pass 1 surprises (Dashboard missing, empty decks→all, lab reveal≠action, cover wayfinding) |
| Questioning | Empty-deck start, quiz header vs L01 filter, reset completeness, steelman domain language |
| Landmark | Begin/Cover Dashboard CTAs; lesson/dashboard lesson-read strip |

---

## Path taken

1. `00_CLICK_HERE_TO_BEGIN.html`  
2. `index.html` (cover)  
3. `02_lessons/01_The_Loop.html`  
4. `decks.html` → Select none → Start (blocked) → L01 only → Start  
5. `03_quiz/index.html` (practice, L01) — answered one item  
6. `04_labs/spaced.html` — reveal then **Good** rating  
7. `dashboard.html` — progress read; Reset **Cancel** then **OK**  
8. Brief `04_labs/steelman.html` — grader domain language  
9. Theme Dim/Bright across cover / lesson / lab / dashboard  

---

## Areas covered & vs Pass 1

| Surface | Pass 2 observation | vs Pass 1 |
| --- | --- | --- |
| Begin | Dashboard tile present (“Progress in this browser”). HTTP/`file://` opening guidance visible. | **Improved** — Pass 1 F4 (no Dashboard) addressed. |
| Cover | CTAs: Contents, Begin Lesson 1, **Dashboard**. Still no persistent top nav; next steps still toward bottom. | **Improved** for Dashboard; **same** book-front / below-fold friction. |
| Lesson 1 | Arrived; objectives visible. Dashboard later showed L01 visited (`markLesson`). | **New** — lesson read progress visible. |
| Decks | Defaults still all seven checked. Select none + Start → **“Select at least one deck.”** No navigation to quiz. L01-only start worked. | **Improved** — Pass 1 all-decks→wrong-lesson first mitigated when learner selects L01; empty path blocked (FIX-01). Default-all surprise remains. |
| Quiz | Practice answer → readable **CORRECT** feedback. With L01 selected, page subtitle still reads static **“7 decks · 56 questions”** while filtered set is 8 Qs. | Feedback good. **New surprise:** header mismatch on single-deck run. |
| SRS lab | Reveal alone → actions 0. **Good** rating incremented reviews/actions. | Pass 1 F3 confirmed by design (rate counts). |
| Dashboard | Quiz + lesson visits + lab ratings visible. Count-rule copy mentions unique IDs / exam skips. | Richer than Pass 1. |
| Reset | Confirm supports Cancel then OK. Theme **kept** (Dim). Quiz/lab counters cleared; **lesson visits and SRS due appeared to persist** — treat as dirty-origin / incomplete clear until clean-state retest. | FIX-07 theme keep looks good; progress wipe needs clean-state confirmation. |
| Steelman | Grader prompt: loops, methods, intent, brainstorming, prototyping, review, iteration/shipping — **not** cardio/physiology. Label on “Your steelman” present. | FIX-02 looks fixed. |

---

## FIX scorecard (Lead list)

| ID | Claim | Score | Evidence (this method) |
| --- | --- | --- | --- |
| **FIX-01** | Empty decks must not start all; error “Select at least one deck” | **FIXED** | Select none → Start → error shown, stayed on decks. Screenshot `04-empty-decks.png`. |
| **FIX-02** | Steelman grader Build Loop domain (no cardio/physiology) | **FIXED** | Steelman grader text names Build Loop topics; no cardio/physiology in live prompt. Static `shared.js` steelman prompt matches. |
| **FIX-03** | Quiz badge contrast readable light+dim | **FIXED** *(exploratory)* | Practice **CORRECT** badge readable in session (dim/light exercise included theme toggles). Pixel contrast measurement left to Accessibility. |
| **FIX-04** | Progress counting; unanswered exam skipped (not counted as answers) | **PARTIAL** | Dashboard copy + practice path show improved counting (unique IDs, lesson visits, lab ratings after rate). **Exam unanswered skip not executed** in this SBTM tour — defer full proof to Boundary. |
| **FIX-05** | HTTP launcher / `file://` warning in README/BAT | **FIXED** | Begin page shows HTTP/file guidance; README/BAT/`START HERE.txt` document preferred HTTP and `file://` isolation. |
| **FIX-06** | Lesson `markLesson` / read progress | **FIXED** | After Lesson 1, Dashboard showed L01 visited. Lessons call `AtlasProgress.markLesson(...)`. |
| **FIX-07** | Reset clears progress, keeps theme; copy matches | **PARTIAL** | Confirm copy lists keys cleared and **Keeps: theme**. Cancel then OK worked; **theme kept**. On this dirty shared origin, lesson visits / SRS due **appeared** to remain after reset — needs private-window retest before calling FIXED. |
| **FIX-08** | Nav + Dashboard from Begin/Cover | **FIXED** *(Dashboard)* / **PARTIAL** *(cover nav)* | Begin has Dashboard tile; Cover has Dashboard CTA. Cover still has **no** persistent top nav (book metaphor). |
| **FIX-09** | Arc-head + Steelman dim contrast; steelman label association | **NOT CHECKED** *(arc-head contrast)* / **FIXED** *(label)* | Steelman textarea has associated `<label for="text">`. Arc-head / steelman dim contrast not scored visually here — Accessibility owns. |
| **FIX-10** | Quiz aria-live / feedback announce / lock-copy name | **NOT CHECKED** *(live SR)* / **PARTIAL** *(static)* | Quiz markup includes `aria-live="polite"` on stats/weak/exam/status. No screen-reader pass in SBTM. |
| FIX-11…15 | If encountered | **NOT IN SCOPE** | None newly assigned in this charter beyond incidental findings below. |

---

## Findings (Pass 2)

### P2-F1 — Quiz chrome still says “7 decks · 56 questions” on L01-only run (Minor/Medium)

**Evidence:** After selecting only L01, quiz subtitle remains static all-pack wording (`03_quiz/index.html`). Screenshot `05-quiz.png`.  
**Why it matters:** First-timer who carefully chose one lesson still sees “56 questions” and may think selection failed.  
**Pass 1 link:** Softens but does not erase Pass 1 F1 surprise when all decks stay default; even the “correct” L01 path has misleading chrome.

### P2-F2 — Reset may leave lesson / SRS residue on shared dirty origin (Minor / suspected)

**Evidence:** After Reset OK, theme kept (good); quiz/lab counters cleared; lesson visit and SRS due appeared to remain. Reset removes `progress_v1`, `weak_v1`, `srs_v1` and keeps `theme_v1` — lessons live *inside* `progress_v1`, so persistence implies contamination, incomplete clear, or re-visit.  
**Repro needed:** Private window, mark lesson + rate SRS, reset, reload without reopening lesson.

### P2-F3 — All decks still pre-checked by default (Nit / residual Pass 1)

**Evidence:** Deck chooser still defaults every lesson checked. FIX-01 blocks empty start; it does not change the “exam by default” first-timer path.  
**Why it matters:** Learner from Lesson 1 still one click from shuffled all-56 unless they deselect.

### P2-F4 — Cover still without persistent nav (Nit / residual Pass 1 F5)

**Evidence:** Dashboard CTA added at bottom; no Cover/Contents/Quiz/Labs/Dashboard header on cover. Screenshot `02-cover.png`.

No blockers. Charter path works end-to-end on the updated pack.

---

## Positive / fixed vs Pass 1

- Begin is a better front door: **Dashboard** + HTTP/`file://` warning.  
- Empty deck start is blocked with clear status text.  
- Lesson visits appear on Dashboard.  
- Lab actions still require rating (honest once you rate).  
- Steelman tutor language matches Build Loop.  
- Reset dialog copy matches behavior for theme keep (when wipe works).  
- Theme persists across pages and across reset.

---

## Open questions

1. Should L01-only (or multi-select) rewrite the quiz subtitle to “1 deck · 8 questions”?  
2. Should deck chooser default to **none** or to the last-read lesson instead of all seven?  
3. After Reset, should Dashboard immediately show zero lesson visits without requiring a full private-window retest to trust the wipe?  
4. Is Cover intentionally nav-free forever, or should Pass 3 add a minimal landmark bar?

---

## Suggested follow-up charters

1. Clean-state private window: FIX-07 wipe proof + FIX-04 exam unanswered skips.  
2. First-timer from Lesson 1 with **default all decks** vs **L01 only** — which path do they take without instructions?  
3. Theme Dim + quiz badge + steelman/arc-head contrast (hand to Accessibility if not already).  

---

## Summary table

| ID | Sev | Title |
| --- | --- | --- |
| P2-F1 | Minor/Medium | Static “7 decks · 56 questions” on filtered quiz |
| P2-F2 | Minor (suspected) | Reset residue for lesson/SRS on dirty shared origin |
| P2-F3 | Nit | All decks still default-checked |
| P2-F4 | Nit | Cover still no persistent top nav |

**Charter status:** Satisfied.  
**Blockers:** None.  
**FIX headline:** 01, 02, 03 (exploratory), 05, 06 **FIXED**; 04, 07, 08 **PARTIAL**; 09/10 mostly deferred to Accessibility / SR; residual first-timer surprises P2-F1/F3.

---

## Evidence

Folder: `qa-bots/reports/pass-2/docs/screendocs/screenshots/2026-09-15/pass-2/accessibility-wcag/2026-09-15/pass-2/exploratory-sbtm/`

- `01-begin.png` — Dashboard tile + HTTP/file guidance  
- `02-cover.png` — Dashboard CTA, no top nav  
- `03-lesson1.png` — The Loop  
- `04-empty-decks.png` — “Select at least one deck”  
- `05-quiz.png` — practice correct + pack subtitle  
- `06-srs-lab.png` — SRS after rating path  
- `07-dashboard.png` / `08-dashboard-labs.png` — progress views  

Report file: `qa-bots/reports/pass-2/exploratory-sbtm-PASS2.md`
