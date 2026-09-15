# CLI FIX BRIEF — Atlas of the Build Loop Study Pack
# Feed this file to your coding CLI / agent as the task prompt.
# Source: multi-method QA (2026-09-15 PT). Do not invent new product scope.

## Mission
Improve the offline Study Pack so P0 defects are fixed, P1 items are addressed where cheap, and behavior matches learner expectations. Keep the pack offline-friendly. Prefer minimal, surgical diffs. Do not rewrite lessons or quiz content unless required by a listed defect.

## Pack root (edit here)
Primary Desktop pack:
`C:\Users\jbies\OneDrive\Desktop\Atlas of the Build Loop — Study Pack\`

If working from a repo mirror, use the equivalent `pack/` tree. Apply the same relative paths below.

## Do not
- Invent new features not listed here
- Run load/DoS testing or add exploit tooling
- Fabricate QA results or claim unverified fixes
- Change curriculum/lesson prose except Steelman grader prompt domain text
- Break relative links that currently resolve under a pack-root HTTP server

## Environment assumption
Learners may open via `file://` (double-click / `.bat`) OR local HTTP. Prefer fixes that work for both; where progress requires a shared origin, document HTTP launch and harden BAT/README.

---

## P0 — must fix (do these first, in order)

### FIX-01 — Empty deck selection must not start all decks
- **Files:** `decks.html` (and any linked start JS if split out)
- **Bug:** Selecting none still navigates to `03_quiz/index.html?decks=all` because empty `ids` coerce to `all`.
- **Required behavior:**
  - If zero decks checked: do **not** start quiz; disable **Start selected decks** OR show inline error “Select at least one deck.”
  - Never map empty selection → `decks=all`.
- **Verify:** Select none → Start → stays on chooser with message; select one deck → Start → quiz loads that deck only.

### FIX-02 — Steelman grader prompt wrong domain
- **File:** `04_labs/shared.js` → `GRADER_PROMPTS.steelman` (or equivalent)
- **Bug:** Prompt tells Grok about cardio / physiology / bloodwork while lab items are Build Loop misconceptions.
- **Required behavior:** Prompt instructs the tutor on Build Loop / methods / shipping / review / iteration language matching lab `ITEMS`. Remove cardio/physiology/bloodwork residue entirely.
- **Verify:** Open Steelman → Copy grader prompt → text is Build Loop domain only.

### FIX-03 — Quiz level badge contrast (~1:1)
- **File:** `03_quiz/styles.css` (`.badge` / `.badge-level`)
- **Bug:** Level badge text color matches accent background → unreadable (~1.0:1).
- **Required behavior:** Text contrast ≥ 4.5:1 against badge background in light and dim themes.
- **Verify:** Open quiz; badge text readable in Bright and Dim.

### FIX-04 — Quiz progress counting integrity
- **Files:** `03_quiz/app.js` (esp. `submitExam` / `recordProgressEvent` / unanswered path), `dashboard.html`, `04_labs/shared.js` progress helpers as needed
- **Bugs:**
  - Exam submit on unanswered items records wrong **and** increments `quiz.answered` (dashboard inflation).
  - Dashboard “Quiz answers recorded” can disagree with in-quiz answered count.
- **Required behavior:**
  - Unanswered exam items: do **not** call progress “answer” increment; do not treat as wrong in weak stats (or record “skipped” separately).
  - Document/implement one counting rule (recommend: unique question IDs answered this browser). Align Dashboard copy with quiz `progressText`.
- **Verify:** Private window → answer exactly 1 practice item → Dashboard shows 1. Exam submit with 0 answers → answered stays 0 (or clearly “skipped”), not N.

---

## P1 — fix soon

### FIX-05 — Prefer shared-origin launch (file:// progress risk)
- **Files:** `README.md`, `START HERE.txt`, `00_CLICK_HERE_TO_BEGIN.bat` (and sibling Open *.bat if needed)
- **Bug:** Default Windows open uses `file://`; Chromium may isolate origins so progress/dashboard don’t share keys.
- **Required behavior:** BAT/README prefer starting a local HTTP server from pack root (e.g. `python -m http.server`) and opening `http://127.0.0.1:PORT/00_CLICK_HERE_TO_BEGIN.html`, **or** clear warning that pure `file://` may not persist progress across pages.
- **Verify:** Documented path opens pack; progress written on quiz appears on dashboard after navigation.

### FIX-06 — Lesson read progress
- **Files:** lesson HTML under `02_lessons/*.html`, `04_labs/shared.js` (`markLesson`), `dashboard.html` / `contents.html` as needed
- **Bug:** `markLesson` exists but lesson pages never call it; Dashboard ignores reading.
- **Required behavior:** Either wire visit/mark-read on lesson load (or explicit control) and show on Dashboard/Contents, **or** remove dead API and any UI that implies lesson progress exists.
- **Verify:** Open Lesson 1 → Dashboard/Contents reflect a read/visit state (if wiring), or no dead expectations remain.

### FIX-07 — Reset vs theme semantics
- **File:** `dashboard.html` reset handler
- **Bug:** Product intent unclear. Source removes `atlas_build_loop_theme_v1` with progress; UX wants theme preserved; BVA also saw theme survive reset once.
- **Required behavior (choose and implement consistently):**
  - **Preferred:** Reset clears progress/weak/srs keys only; **keep** theme. Confirm dialog lists exact keys/categories wiped.
- **Verify:** Dim mode → Reset → progress empty, theme still dim; confirm text matches.

### FIX-08 — Navigation consistency + Dashboard discoverability
- **Files:** `00_CLICK_HERE_TO_BEGIN.html`, `index.html`, quiz/lab chrome, `04_labs/steelman.html`
- **Bug:** Begin/Cover omit Dashboard; Steelman lacks shared topbar; quiz chrome differs.
- **Required behavior:** Interactive pages share a consistent top nav including Dashboard. Begin and/or Cover expose a Dashboard (or Progress) link. Cover may stay sparse but needs a reachable escape.
- **Verify:** From Begin and Cover, reach Dashboard in ≤2 clicks without hunting lesson chrome.

### FIX-09 — Contrast + Steelman label
- **Files:** `assets/pack.css` (`.arc-head`), `04_labs/steelman.html`, related dim tokens
- **Bugs:** Contents arc gold-on-teal fails in light (~1:1); Steelman “New prompt” fails in dim; Steelman `<label>` not associated with `#text`.
- **Required behavior:** ≥4.5:1 contrast in light and dim; `label for="text"` (or wrap textarea).
- **Verify:** Contents arc headers readable in Bright; Steelman New prompt readable in Dim; label click focuses textarea.

### FIX-10 — Quiz/lab accessibility live regions & names
- **Files:** `03_quiz/index.html`, `03_quiz/app.js`, `04_labs/bias.html` / `shared.js`
- **Bugs:** Entire `#quiz` main is `aria-live="polite"`; incorrect feedback not announced; Scenario Audit lock-copy button unnamed.
- **Required behavior:** Remove live region from whole main; keep/announce score/timer/feedback regions; give lock-copy an accessible name.
- **Verify:** Practice wrong answer exposes announced/associated status; lock-copy has a name in a11y tree.

---

## P2 — polish (if time remains)

### FIX-11 — Weak Areas UI refresh
- **File:** quiz weak-panel UI in `03_quiz/`
- **Bug:** Clear history / weak panel stale until collapse or reload (DEF-BVA-02).
- **Required:** Immediate UI update after clear.

### FIX-12 — Steelman empty validation visibility
- **File:** `04_labs/steelman.html` (+ score UI)
- **Bug:** Empty Score blocks but message missing/below fold (DEF-BVA-03). Keep 39/40 gate.
- **Required:** Visible inline validation near Score when length < 40.

### FIX-13 — SRS rating copy + lab action semantics
- Hint under Again/Hard/Good/Easy what each does; Dashboard copy: reveal ≠ action until rate.

### FIX-14 — Timer hint vs options
- Align exam timer hint (mentions 15–120) with actual `<option>` max (60) or extend options.

### FIX-15 — Skip link, `<main>`, `:focus-visible`
- Add skip-to-content; landmarks on chrome pages; use `--focus` for visible focus on CTAs/buttons.

---

## Suggested CLI execution order
1. FIX-01, FIX-02, FIX-03, FIX-04 (P0)
2. FIX-07, FIX-09, FIX-10, FIX-05, FIX-06, FIX-08 (P1)
3. FIX-11–FIX-15 (P2 as capacity allows)
4. Smoke retest: begin → cover → contents → Lesson 1 → decks (none + one) → quiz → labs → dashboard → theme → reset

## Acceptance checklist (CLI must print PASS/FAIL)
- [ ] Empty decks cannot start all
- [ ] Steelman grader prompt is Build Loop domain only
- [ ] Quiz badge readable in both themes
- [ ] One quiz answer → Dashboard shows 1; unanswered exam does not inflate answered
- [ ] Reset clears progress, preserves theme (if FIX-07 preferred)
- [ ] Steelman label associated; dim CTA readable
- [ ] Contents arc headers readable in light theme
- [ ] Relative pack links still work under `python -m http.server` from pack root

## Evidence / do not invent
QA artifacts (read-only context if available):
- `SPONSOR_REPORT_Atlas_Study_Pack_2026-09-15.md`
- Methodology reports under QA outputs for 2026-09-15

When done: summarize files changed and checklist results. Do not claim methodologies re-ran unless you actually retested.
