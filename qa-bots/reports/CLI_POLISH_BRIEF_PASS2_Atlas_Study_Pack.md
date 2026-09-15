# CLI POLISH BRIEF — PASS 2 residuals
# Feed this file to your coding CLI / agent as the task prompt.
# Source: QA Pass 2 sponsor delta (2026-09-15 PT). Do not re-open FIXED Pass 1 P0 work unless regression.

## Mission
Close the **remaining polish** left after Pass 2 verification. Pass 1 P0 functional defects are already FIXED (empty decks, Steelman domain, exam unanswered inflate, reset keeps theme, markLesson, Begin/Cover Dashboard). Do **not** rewrite those unless a regression is proven.

Keep diffs surgical. Prefer HTTP-safe launch. Do not invent new product scope.

## Pack root (edit here)
`C:\Users\jbies\OneDrive\Desktop\Atlas of the Build Loop - Study Pack\`

(Repo mirror: equivalent `pack/` tree.)

## Already FIXED — do not “fix” again unless broken
FIX-01, FIX-02, FIX-04, FIX-06, FIX-07, FIX-08, FIX-11, FIX-12, FIX-13, FIX-14 (and core of FIX-09/10).

## Do not
- Invent features beyond this list
- Load/DoS / exploit work
- Fabricate QA results
- Rewrite lesson curriculum prose
- Break pack-root relative links under `python -m http.server`

---

## P1 — do first (Pass 2 medium residuals)

### POLISH-01 — Dim-theme quiz `.badge` contrast (NR01 / FIX-03 complete)
- **Files:** `03_quiz/styles.css` (and pack theme tokens if shared)
- **Bug:** Dim theme `.badge` cream `#fff6d6` on cyan `#5ec8d6` ≈ **1.81:1** (fails WCAG AA). Light theme OK (~5.49:1). `.badge-level` contrast OK in CSS but live level pill was reported blank — verify computed styles.
- **Required:**
  - Dim `.badge` text/background contrast ≥ **4.5:1**.
  - Level pill (`.badge.badge-level`) visibly readable in Bright and Dim (not blank).
- **Verify:** Open quiz in Dim and Bright; lesson tags and level pill readable; measure or spot-check contrast.

### POLISH-02 — Sibling Open*.bat still file:// (NR02 / FIX-05 complete)
- **Files:** `Open Home.bat`, `Open Dashboard.bat`, `Open Deck Chooser.bat`, `Open Labs.bat`, `Open Quiz.bat` (and optionally README note)
- **Bug:** Primary `00_CLICK_HERE_TO_BEGIN.bat` prefers HTTP; sibling Open*.bat still `Start-Process` HTML → `file://` origin split risk.
- **Required:** Point siblings at `http://127.0.0.1:8765/...` (reuse primary server-start pattern), **or** remove/relabel them with a clear file://-unsafe warning.
- **Verify:** Each Open*.bat either opens HTTP URL on 8765 or documents why not; README mentions siblings if kept.

### POLISH-03 — Quiz subtitle ignores active filter
- **Files:** `03_quiz/index.html`, `03_quiz/app.js`
- **Bug:** Hardcoded “7 decks · 56 questions …” even when `?decks=bl-01-loop` (8 Q). Misleading status (Pass 2 Exploratory/Usability).
- **Required:** Subtitle reflects **filtered** deck count and question count (and/or selected deck names).
- **Verify:** Start L01 only → subtitle shows 1 deck / 8 questions (or equivalent accurate copy), not 7/56.

### POLISH-04 — Quiz `#quiz-status` announcement reliability (FIX-10 residual)
- **Files:** `03_quiz/app.js`, `03_quiz/index.html`
- **Bug:** Wiring exists for `#quiz-status` + `role="status"`, but Pass 2 a11y found status empty after practice answer while visual feedback showed.
- **Required:** On correct/incorrect practice answer, populate `#quiz-status` with a short text status (e.g. “Correct” / “Incorrect”) so AT can announce it.
- **Verify:** Answer a question; inspect `#quiz-status` textContent non-empty; visual feedback still works.

### POLISH-05 — Empty-deck error AT polish (FIX-01 a11y residual)
- **Files:** `decks.html`
- **Bug:** Functional FIX-01 works; a11y gaps: no `aria-describedby`/`aria-errormessage`; disabled Start focusability weak; status may not re-announce.
- **Required:** Tie error to control (`aria-describedby` or `aria-errormessage`); ensure error is announced when Select none → Start; keep Start non-activating when empty.
- **Verify:** Select none → Start → error visible + associated for AT; cannot navigate to all-decks.

---

## P2 — polish if capacity remains

### POLISH-06 — Steelman label click focuses textarea (FIX-09 residual)
- **File:** `04_labs/steelman.html`
- **Bug:** `label for="text"` present; Pass 2 session did not confirm click→focus.
- **Required:** Clicking “Your steelman” focuses `#text`.
- **Verify:** Click label → caret in textarea.

### POLISH-07 — Pack-wide skip + `<main>` (FIX-15)
- **Files:** `contents.html`, `decks.html`, `04_labs/index.html`, `index.html` (cover), labs missing skip/`main`
- **Required:** Skip-to-content + `<main>` (or equivalent landmark) on remaining chrome pages; keep existing `:focus-visible`.
- **Verify:** Keyboard Tab from top reaches skip then main content on those pages.

### POLISH-08 — Cover heading structure (V11)
- **File:** `index.html`
- **Bug:** Orphan `h3`s under non-heading “The four arcs” kicker.
- **Required:** Proper heading hierarchy (e.g. `h2` for arcs section).
- **Verify:** Outline has no orphan h3 under a paragraph kicker.

### POLISH-09 — Theme toggle `aria-pressed` (R06 residual)
- **File:** `assets/theme.js`
- **Required:** Toggle exposes pressed/state for AT (`aria-pressed` or equivalent) in addition to visible label swap.
- **Verify:** Inspect toggle in Dim and Bright.

### POLISH-10 — Optional product choice: default all decks pre-checked
- **File:** `decks.html`
- **Note:** Not a defect if intentional. If desired: default to Lesson 1 only, or none with Start disabled, to reduce first-timer “exam by default.”
- **Only implement if sponsor wants this behavior change.**

### POLISH-11 — Optional: investigate chooser → `decks=all` one-off
- Usability saw one Start→`decks=all` after selecting L01. Code path should emit single id.
- **Required if reproducible:** Ensure `sync()` before navigate; never write `all` unless all checked or user chose All-56 link.
- **Verify:** Hard refresh; check exactly one box; Start → URL contains that deck id only.

---

## Suggested CLI order
1. POLISH-01, POLISH-02, POLISH-03 (highest Pass 2 residual scores)
2. POLISH-04, POLISH-05
3. POLISH-06 … POLISH-09
4. POLISH-10/11 only if sponsor opts in
5. Smoke retest: begin → cover → contents → Lesson 1 → decks (none + one) → quiz subtitle + badges Bright/Dim → dashboard → theme → reset; confirm Open*.bat HTTP behavior

## Acceptance checklist (CLI must print PASS/FAIL)
- [ ] Dim `.badge` contrast ≥ 4.5:1; level pill readable Bright+Dim
- [ ] Open*.bat use HTTP (or clearly unsafe/removed)
- [ ] Filtered quiz subtitle matches selection (not hardcoded 7/56)
- [ ] `#quiz-status` non-empty after practice answer
- [ ] Empty-deck error associated for AT; still cannot start all
- [ ] Steelman label click focuses textarea
- [ ] Skip/`main` on previously missing chrome pages (if POLISH-07 done)
- [ ] Relative links still work under `python -m http.server` from pack root

## Evidence (read-only context)
- Pass 2 delta: `SPONSOR_DELTA_PASS2_Atlas_Study_Pack_2026-09-15.md`
- Methodology reports under `/workspace/qa-reports/pass-2/` or Desktop `Dev project 1\commits\pass 2\`

When done: summarize files changed + checklist PASS/FAIL. Do not claim Pass 3 QA re-ran unless actually retested.
