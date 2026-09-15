# Accessibility WCAG Report — **PASS 2** (verification)

**Tester:** Accessibility WCAG Tester  
**Label:** **PASS 2** / 2026-09-15 (PT)  
**Assigned by:** QA/Tester Lead  
**Target:** Atlas of the Build Loop — Study Pack (post-fix build)  
**URL:** `http://127.0.0.1:8765/00_CLICK_HERE_TO_BEGIN.html`  
**Pack:** `pack/`  
**Compared to:** Pass 1 `qa-bots/reports/2026-09-15-accessibility-wcag-atlas-study-pack.md` (also `qa-bots/reports/accessibility-wcag-atlas-study-pack.md`)  
**localStorage:** Cleared on the shared origin before the keyboard pass, then begin page reloaded.

---

## 1. Scope & methodology

WCAG-oriented only: keyboard operability, focus, labels/names, contrast (computed + visual), headings/structure, alt text, forms, ARIA/live regions.

**Methods**
1. Static re-audit of fix sites (HTML/CSS/JS) with WCAG relative-luminance math on CSS tokens.
2. Keyboard + visual browser pass on the live URL after `localStorage.clear()`.

**Pass 1 items rechecked (Lead brief):** V1 badge, V2 arc-head, V3–V4 steelman, live regions / feedback / lock-copy (FIX-03, FIX-09, FIX-10). Also scored FIX-01–10 from an a11y angle.

---

## 2. FIX-01…10 scores (accessibility method)

| Fix | Score | Evidence |
|-----|--------|----------|
| **FIX-01** Empty decks | **PARTIAL** | `decks.html`: error `#deck-error` has `role="status"`; Start uses `aria-disabled`. Gaps: no `aria-describedby`/`aria-errormessage`; polite status may not re-announce; disabled Start focusability weak. |
| **FIX-02** Steelman domain | **NOT IN SCOPE** | Content-only grader prompt; no a11y SC. |
| **FIX-03** Quiz badge contrast | **PARTIAL** | **Static FIXED:** `.badge-level` → `background: var(--surface-2); color: var(--text)` (`03_quiz/styles.css` L384–388); computed **14.69:1** light / **11.36:1** dim. **Live residual:** level pill on Practice Quiz appeared **blank / unreadable** in light and dim (screenshots `docs/screendocs/screenshots/2026-09-15/pass-2/accessibility-wcag/2026-09-15/pass-2/accessibility-wcag/quiz-badge-light.png`, `quiz-badge-dim.png`) while lesson `.badge` shows. Treat contrast *intent* as fixed in CSS; **runtime visibility still open** — verify computed styles on `.badge.badge-level`. Residual: non-level `.badge` cream on accent fails badly in **dim** (~**1.81:1**). |
| **FIX-04** Progress / unanswered exam | **NOT IN SCOPE** | Counting logic; not announced as a11y work. |
| **FIX-05** HTTP launcher | **NOT IN SCOPE** | Docs/BAT only. |
| **FIX-06** markLesson progress | **NOT IN SCOPE** | Progress wiring. |
| **FIX-07** Reset keeps theme | **FIXED** | `dashboard.html` native `confirm` states theme kept; AT-friendly dialog. |
| **FIX-08** Nav + Dashboard from Begin/Cover | **FIXED** | Dashboard links present on begin + cover; keyboard path begin→cover→contents + theme toggle worked in live pass. |
| **FIX-09** Arc-head + Steelman contrast/label | **PARTIAL** | **Arc-head FIXED** live+static: cream `#fff6d6` on teal ~**6.89:1** (was ~1.04:1). **New prompt FIXED** dim: `#next` uses `--text`/`--btn` (~10.58:1 dim). **Label markup FIXED** (`for="text"`). **Live PARTIAL:** clicking “Your steelman” did **not** focus `#text` in the keyboard/visual session (association in DOM; activation not confirmed). |
| **FIX-10** aria-live / feedback / lock-copy | **PARTIAL** | **V5 FIXED:** `main#quiz` no longer `aria-live`. **V7 FIXED** live: “Copy LOCK grader prompt” named (`shared.js`). **V6 PARTIAL:** source sets `#quiz-status` on practice answer (`app.js` L413–417) + `role="status"`; live inspect after incorrect/correct interaction found **`#quiz-status` still empty** while inline visual feedback showed — announcement reliability **not confirmed**. |

---

## 3. Pass 1 violation re-score (V1–V12)

| ID | Pass 1 | PASS 2 | Notes |
|----|--------|--------|-------|
| V1 Level badge contrast | Critical | **PARTIAL** | CSS AA for `.badge-level`; live pill still blank/unreadable |
| V2 Arc-head contrast | Serious | **FIXED** | Live + static |
| V3 Steelman New prompt dim | Serious | **FIXED** | Live + static |
| V4 Steelman label association | Serious | **PARTIAL** | `for=` present; label-click→focus not confirmed live |
| V5 Quiz main aria-live | Serious | **FIXED** | Static + live |
| V6 Feedback not announced | Moderate | **PARTIAL** | Wiring present; live status empty |
| V7 Lock-copy unnamed | Moderate | **FIXED** | Live named |
| V8 Cover focus visibility | Moderate | **FIXED** | Pack/quiz `:focus-visible`; live focus indicators visible on path |
| V9 Skip links | Moderate | **PARTIAL** | Skip present on quiz/begin/dashboard/lessons; still missing on contents/decks/labs/cover/steelman |
| V10 Missing `<main>` | Moderate | **PARTIAL** | Still missing on several chrome pages |
| V11 Cover orphan h3s | Moderate | **STILL OPEN** | `p.cover-kicker` + orphan `h3`s |
| V12 Explicit focus styles | Moderate | **FIXED** | `:focus-visible` in pack + quiz CSS |

---

## 4. Process / steps (PASS 2)

1. Confirmed HTTP 200 on shared URL; pack mtimes refreshed (~15:09–15:11 PT files).
2. Static FIX/V re-score → draft `Accessibility_WCAG_Pass2_static_draft.md`.
3. Keyboard/visual pass after `localStorage.clear()`: begin → cover → contents → quiz (badge light/dim) → steelman → Scenario Audit grader → theme toggle.
4. Merged into this report.

---

## 5. New / residual findings this pass

1. **Quiz level pill blank in UI** despite CSS fix (see FIX-03 / V1) — **Serious** residual until computed-style proof or visual fix.
2. **Lesson `.badge` (non-level) dim contrast ~1.81:1** — **Serious** (1.4.3); separate from FIX-03 target but same card chrome.
3. **Skip link in dim** may be low-contrast on quiz (observed dark-on-dark) — **Moderate** spot check.
4. Cover heading structure (V11) unchanged.
5. FIX-01 error announcement polish still incomplete for AT.

**Blockers:** None for continued testing.

---

## 6. Results summary (PASS 2)

| Category | Count |
|----------|------:|
| FIX FIXED | 3 (07, 08) + strong FIXED parts of 09/10 |
| FIX PARTIAL | 4 (01, 03, 09, 10) |
| FIX NOT IN SCOPE | 4 (02, 04, 05, 06) |
| Pass-1 V FIXED | V2, V3, V5, V7, V8, V12 |
| Pass-1 V PARTIAL | V1, V4, V6, V9, V10 |
| Pass-1 V STILL OPEN | V11 |

---

## 7. Residual a11y risk

- Level badge **runtime** visibility vs CSS mismatch needs DevTools confirmation.
- Dim-theme cream-on-accent **lesson** badges still fail AA.
- Quiz `#quiz-status` announcement needs SR confirmation (NVDA/VoiceOver); do not mark V6 fully closed.
- Pack-wide skip/`main`/cover headings incomplete.
- Shared-origin localStorage was cleaned for this pass; other agents may dirty it again.

---

## 8. Artifacts

- **This report:** `qa-bots/reports/pass-2/Accessibility_WCAG_PASS2.md`
- Static draft: `qa-bots/reports/pass-2/Accessibility_WCAG_Pass2_static_draft.md`
- Shots: `qa-bots/reports/pass-2/docs/screenshots/2026-09-15/pass-2/accessibility-wcag/` (quiz-badge light/dim, arc-head, steelman dim, quiz-status, lock-copy)

---

*End of Accessibility WCAG PASS 2 report.*
