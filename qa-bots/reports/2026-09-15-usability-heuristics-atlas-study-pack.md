# Usability Heuristics Evaluation — Atlas of the Build Loop Study Pack

**Evaluator:** Usability Heuristics Tester  
**Methodology:** Nielsen’s 10 usability heuristics (only)  
**Target:** Atlas of the Build Loop — Study Pack (offline HTML field guide)  
**Shared test URL:** http://127.0.0.1:8765/00_CLICK_HERE_TO_BEGIN.html  
**Date:** 2026-09-15 (America/Los_Angeles)

---

## 1. Flows reviewed

| # | Flow | Pages / actions |
|---|------|-----------------|
| A | Begin → cover → contents → Lesson 1 | `00_CLICK_HERE_TO_BEGIN.html` → `index.html` → `contents.html` → `02_lessons/01_The_Loop.html` |
| B | Decks / quiz | `decks.html` → practice quiz (`decks=all` and `decks=bl-01-loop`); answer 1+ items |
| C | Labs | `04_labs/index.html` → Spaced Repetition (`spaced.html?decks=bl-01-loop`); Show answer + ratings |
| D | Dashboard / reset / theme | `dashboard.html`; reset confirm (cancelled); Dim/Bright toggle; persistence across pages |

Also reviewed: Steelman lab chrome and shared grader prompt text (static + consistency check).

---

## 2. Process / steps

1. Confirmed local server on `:8765` and the Study Pack files.
2. Static review of begin, cover, contents, dashboard, decks, quiz shell, labs index, theme.js, shared.js, Lesson 1, Steelman.
3. Live browser walk of primary flows with screenshots.
4. Scored findings only against Nielsen heuristics; severity Critical / Major / Minor / Cosmetic.

---

## 3. Heuristic violations (with severity and evidence)

### H5 Error prevention — **Major** — “Select none” still starts all 56 questions

- **Where:** Deck Chooser (`decks.html`).
- **Live evidence:** Select none → Start selected decks opened all 7 decks / 56 questions; no warning.
- **Code:** `ids.length === 0` is mapped to `decks=all`.
- **Impact:** User who cleared selection still gets the full exam path — opposite of labeled intent.
- **Fix:** Disable Start when zero decks checked; show “Select at least one deck.” Never coerce empty → `all`.

### H1 Visibility of system status — **Major** — Dashboard quiz count disagrees with in-quiz progress

- **Live evidence:** After practice on L01, quiz UI showed `1 / 8 answered · 0 correct`, while Dashboard showed **Quiz answers recorded: 2**. Lab card showed Spaced Repetition visits 2 / actions 0.
- **Impact:** Progress surfaces cannot be trusted as a single source of truth; undermines the Dashboard’s purpose.
- **Fix:** Define and display one counting rule (e.g., unique question IDs answered this browser vs session answers). Align Dashboard copy with quiz `progressText`. Investigate double-increments across deck URL changes / reshuffles.

### H1 Visibility of system status — **Major** — Lesson reading never surfaces as progress

- **Live evidence:** Lesson 1 has no mark-complete control; Dashboard shows no lesson-read state after visiting The Loop.
- **Code:** `AtlasProgress.markLesson` exists in `shared.js` but lesson pages do not call it.
- **Impact:** Learners who primarily read see an “empty” pack on the Dashboard.
- **Fix:** Record lesson visits (or explicit “Mark as read”) and show them on Dashboard and/or Contents cards.

### H2 Match to real world / H4 Consistency — **Major** — Steelman grader prompt is wrong domain

- **Where:** `04_labs/shared.js` → `GRADER_PROMPTS.steelman`.
- **Evidence:** Prompt instructs the tutor about “cardio training, physiology, and bloodwork” while lab items are Build Loop misconceptions (loops, OODA, Agile, shipping).
- **Impact:** External tutor feedback may ignore pack vocabulary and confuse learners.
- **Fix:** Rewrite grader system text for Build Loop / methods / shipping only.

### H5 Error prevention / H3 User control — **Major** — Progress reset also clears theme preference

- **Where:** Dashboard “Reset Atlas progress (this browser)”.
- **Live evidence:** Confirm dialog: “Clear Atlas of the Build Loop progress keys on this browser?” (cancelled in test; data preserved).
- **Code:** Also `removeItem("atlas_build_loop_theme_v1")`.
- **Impact:** Labeled “progress” wipe silently includes theme; confirm text does not disclose that.
- **Fix:** Exclude theme from progress reset; list exact data categories in the confirm string.

### H4 Consistency and standards — **Major** — Navigation chrome differs by surface

- **Live evidence:**
  - Begin / Cover: no standard top nav; no Dashboard link.
  - Contents / Labs index / most labs / Decks: topbar (Cover · Contents · Quiz · Labs · Dashboard).
  - Lesson 1: compact lesson-nav including Next →.
  - Quiz: bespoke header/footer (Dashboard in footer; Labs not in top strip).
  - Steelman: plain text links, not shared topbar (unlike Spaced / Bias / Term Match).
- **Impact:** Wayfinding must be re-learned per section; escape hatches vanish on Begin/Cover.
- **Fix:** One persistent nav on interactive pages; keep Cover sparse only if secondary escapes remain reachable.

### H8 / H7 — **Minor** — Cover forward CTAs only at bottom

- **Live evidence:** Long cover prose; “Open the contents” / “Begin Lesson 1” only after scroll; no top “next” or progress.
- **Fix:** Sticky or top secondary CTA row, or persistent mini-nav.

### H2 / H6 — **Minor** — SRS rating labels lack consequence explanations

- **Live evidence:** After “Show answer,” buttons Again / Hard / Good / Easy appear with no copy on scheduling effects.
- **Fix:** One-line hint under ratings (e.g., Again = soonest; Easy = longest interval).

### H4 — **Minor** — Contents arc-head images use empty `alt=""`

- **Live evidence:** Confirmed empty alts on meaningful arc header images (cover arcs elsewhere have descriptive alts).
- **Fix:** Descriptive alts or ensure adjacent text fully carries meaning for AT users (note: a11y detail also owned by WCAG tester).

### H4 — **Minor** — Theme toggle wording Dim ↔ Bright

- **Live evidence:** Label becomes “Bright mode” (not “Light mode”); state persists Dashboard → Contents.
- **Fix:** Prefer Dim / Light (or Dark / Light) consistently.

### H6 — **Minor** — Brand naming split

- Full product name “Atlas of the Build Loop” vs brand “the Build Loop”.
- **Fix:** Consistent short brand + full H1.

### H1 / H2 — **Minor** — Lab progress bars are opaque

- Dashboard uses `min(100, actions * 5)` with no definition of “action” or what 100% means.
- **Fix:** Label as activity proxy or map to a named goal.

### H3 — **Minor** — Multiple clear/reset scopes

- Quiz Clear answers, Weak-area clear history, Dashboard reset — different blast radii; easy to mis-predict.
- **Fix:** Scope in the control label itself.

---

## 4. Positive findings

1. **H10 Help:** Begin page recovery instructions (Open with browser / `.bat`) are concrete and useful offline.
2. **H6 Recognition:** Contents suggested path and arc-grouped lesson cards make the week plan scannable.
3. **H8 Aesthetic / content design:** Cover-as-book and Lesson 1 structure (objectives → content → terms → misconceptions → practice) support recognition over recall.
4. **H1 Quiz status:** Practice mode gives immediate, specific, color-coded feedback (`INCORRECT` / `CORRECT CHOICE`) with live `answered · correct` counts and `aria-live` regions.
5. **H3 Theme control:** Toggle label updates and preference persists across pages.
6. **H5 (partial):** Destructive Dashboard reset and weak-history clear use confirmation; cancel preserved data in live test.
7. **H1 Dashboard coaching:** “Suggested next move” gives a concrete next action once data is trusted.

---

## 5. Prioritized UX recommendations

| Priority | Action |
|----------|--------|
| P0 | Fix empty deck selection → do not start `all`; block Start with inline error |
| P0 | Reconcile quiz answered count with Dashboard “Quiz answers recorded” |
| P0 | Stop clearing theme on progress reset; disclose exact wipe scope in confirm |
| P1 | Wire lesson-read progress into Dashboard (or remove dead `markLesson`) |
| P1 | Fix Steelman grader prompt domain (Build Loop, not cardio/labs) |
| P1 | Unify navigation chrome (Begin/Cover escapes, Quiz, Steelman) |
| P2 | Explain SRS rating consequences; clarify lab bar semantics; align Dim/Light wording |

---

## 6. Results summary

| Severity | Count |
|----------|------:|
| Critical | 0 |
| Major | 6 |
| Minor | 7 |
| Cosmetic | 0 |

**Overall judgment:** The primary learning path (begin → cover → contents → Lesson 1) is clear, well-structured, and pleasant. Highest usability risk is **trust and control around selection and progress** (empty decks → full quiz; Dashboard vs quiz counts; reset including theme; invisible lesson progress), plus **chrome inconsistency** and one **domain mismatch** in the Steelman tutor prompt—not discoverability of Lesson 1 itself.

---

## 7. Live screenshots (evidence)

Repo paths (copied from the 2026-09-15 heuristics walk):

- Begin: `docs/screenshots/2026-09-15/usability-heuristics/01-begin.png`
- Cover: `docs/screenshots/2026-09-15/usability-heuristics/02-cover.png`
- Contents: `docs/screenshots/2026-09-15/usability-heuristics/03-contents.png`
- Lesson 1: `docs/screenshots/2026-09-15/usability-heuristics/04-lesson-1.png`
- Quiz feedback: `docs/screenshots/2026-09-15/usability-heuristics/05-quiz-feedback.png`
- Spaced Repetition: `docs/screenshots/2026-09-15/usability-heuristics/06-spaced-repetition.png`
- Dashboard/theme: `docs/screenshots/2026-09-15/usability-heuristics/07-dashboard-theme.png`
- Reset confirmation: `docs/screenshots/2026-09-15/usability-heuristics/08-reset-confirm.webp`
- Dimmed Contents: `docs/screenshots/2026-09-15/usability-heuristics/09-dimmed-contents.png`

---

## 8. Scope note

Evaluation stayed within Nielsen heuristic usability only. No smoke, exploratory/SBTM, BVA, or WCAG methodology claims are made here (those belong to sibling testers).
