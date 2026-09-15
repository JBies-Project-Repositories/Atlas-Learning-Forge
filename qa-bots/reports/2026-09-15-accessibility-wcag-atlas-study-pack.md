# Accessibility WCAG Report — Atlas of the Build Loop (Study Pack)

**Tester:** Accessibility WCAG Tester  
**Assigned by:** QA/Tester Lead  
**Target:** Atlas of the Build Loop — Study Pack (offline HTML field guide)  
**Shared URL:** `http://127.0.0.1:8765/00_CLICK_HERE_TO_BEGIN.html`  
**Date:** 2026-09-15 (PT)  
**Standard:** WCAG 2.x Level A–AA oriented checks (manual + static source)

---

## 1. Scope

### In scope (priority surfaces)
- Begin (`00_CLICK_HERE_TO_BEGIN.html`)
- Cover (`index.html`)
- Contents (`contents.html`)
- Lesson 1 (`02_lessons/01_The_Loop.html`)
- Quiz decks (`decks.html`) and quiz (`03_quiz/`)
- Labs hub + Scenario Audit lab (`04_labs/index.html`, `bias.html`); spot-check of steelman/spaced/fermi via source
- Dashboard (`dashboard.html`)
- Theme toggle (Bright / Dim) via `assets/theme.js` + `pack.css`

### Out of scope
- Full audit of Lessons 2–7 beyond Lesson 1 patterns
- Full 56-question quiz content review
- Automated axe/Lighthouse as sole evidence (not used as primary method)
- Non-accessibility methodologies

### Methods used
1. **Static source analysis** of priority HTML/CSS/JS (headings, alt, labels, ARIA, contrast from CSS variables computed with WCAG relative luminance).
2. **Keyboard-only browser pass** on the live shared URL: Tab / Shift+Tab / Enter / Space / Arrow keys; focus visibility; operable controls; theme toggle; one quiz interaction; one lab text field.

---

## 2. Success criteria checked

| Area | WCAG SC (primary) | How checked |
|------|-------------------|-------------|
| Keyboard operable | 2.1.1 | Keyboard-only traversal of priority path |
| No keyboard trap | 2.1.2 | Observed focus movement across pages |
| Focus order | 2.4.3 | Tab order vs visual layout |
| Focus visible | 2.4.7 | Screenshots + a11y tree vs visible ring |
| Bypass blocks | 2.4.1 | Search for skip links; landmark presence |
| Page titled | 2.4.2 | Unique `<title>` on priority pages |
| Headings / structure | 1.3.1, 2.4.6 | Heading outline; landmarks |
| Link purpose | 2.4.4 | Link accessible names |
| Non-text content | 1.1.1 | `alt` on images; decorative patterns |
| Labels / instructions | 3.3.2 | Form labels on decks, quiz, labs |
| Error identification / status | 3.3.1, 4.1.3 | Quiz feedback; lab validation |
| Name, Role, Value | 4.1.2 | Buttons, radios, theme toggle, lab controls |
| Contrast (minimum) | 1.4.3 | Computed CSS pairs + visual spot-check light/dim |
| Language of page | 3.1.1 | `html lang` |
| Use of color | 1.4.1 | Quiz/lab feedback not color-only |

---

## 3. Process / steps taken

1. Confirmed shared server on `127.0.0.1:8765` (HTTP 200) and the Study Pack files.
2. Static audit of priority pages + `assets/pack.css`, `theme.js`, quiz `styles.css`/`app.js`, labs `shared.js`.
3. Keyboard path: begin → cover → contents → Lesson 1 → decks → quiz (`?decks=all`) → labs → Scenario Audit (`bias.html`) → dashboard → Dim mode toggle.
4. Merged static + interactive findings into this report.

---

## 4. Violations (severity, evidence, reproduce)

Severity scale: **Critical** / **Serious** / **Moderate** / **Minor**.

### V1 — Critical — Quiz level badge contrast ~1:1 (1.4.3)

- **Where:** `03_quiz/styles.css` (`.badge` / `.badge-level`); rendered via `app.js` level badge.
- **Issue:** `.badge` uses accent background; `.badge-level` sets text color to the same accent without changing background → accent-on-accent (~1.0:1) in light and dim.
- **Reproduce:** Open quiz → observe level badge text color vs pill background (or inspect computed styles).
- **Expected:** Text contrast ≥ 4.5:1 against badge background.
- **Impact:** Level indicator may be unreadable for low-vision users.

### V2 — Serious — Contents arc-head gold on teal fails in light theme (1.4.3)

- **Where:** `contents.html` arc headers; `pack.css` `.arc-head` / `.arc-head .arc` (`--gold` `#7a4e10` on `--nav-bg` `#1c5d68`).
- **Computed:** ~**1.04:1** (light). Dim gold `#f3cc74` on same teal ~**4.87:1** (passes).
- **Reproduce:** Open Contents in **Bright/light** theme; view Arc A–D header labels.
- **Expected:** ≥ 4.5:1 in both themes.

### V3 — Serious — Steelman “New prompt” contrast fails in dim theme (1.4.3)

- **Where:** `04_labs/steelman.html` — button text `#062f2c` on `var(--btn)` / dim `#2a3c4a` (~**1.27:1**).
- **Reproduce:** Open Steelman lab → toggle Dim mode → inspect “New prompt” button.
- **Expected:** ≥ 4.5:1 in dim theme (light theme passes ~12.4:1).

### V4 — Serious — Steelman textarea label not programmatically associated (1.3.1 / 3.3.2)

- **Where:** `04_labs/steelman.html` — `<label class="muted">Your steelman</label>` then `<textarea id="text">` without `for="text"` and label does not wrap the control.
- **Reproduce:** Open Steelman → inspect label/`#text` association (or navigate with AT; label click may not focus field).
- **Expected:** `label for="text"` or wrapping `<label>`.

### V5 — Serious — Quiz `#quiz` entire main is `aria-live="polite"` (4.1.3)

- **Where:** `03_quiz/index.html` `main#quiz` with `aria-live="polite"`; full re-renders can spam announcements.
- **Reproduce:** Load quiz with a screen reader / live-region inspection; change filters or re-render cards.
- **Expected:** Live regions limited to score/timer/results (those already exist separately).

### V6 — Moderate — Quiz incorrect feedback not announced (3.3.1 / 4.1.3) *[keyboard pass]*

- **Where:** `/03_quiz/index.html?decks=all`
- **Reproduce (keyboard):**
  1. Open quiz with a deck selected.
  2. Tab to a question’s radio options; use Arrow keys + Space to select an **incorrect** answer.
  3. Observe feedback and accessibility tree / announcement.
- **Expected:** Incorrect/correct status exposed via live/status region (or associated `aria-describedby` / `aria-invalid`).
- **Actual:** “INCORRECT” is visual; options become disabled; no announced feedback observed in accessibility inspection.
- **Note:** Static review confirms textual “Correct/Incorrect” exists (good for 1.4.1) but is not wired for programmatic announcement.

### V7 — Moderate — Unnamed lab grader lock-copy button (4.1.2) *[keyboard pass]*

- **Where:** `/04_labs/bias.html?decks=bl-01-loop` (Scenario Audit)
- **Reproduce:** Select L01 → Tab through controls after answering flow → final grader lock-copy control appears as an **unnamed button** in the accessibility tree.
- **Expected:** Accessible name (visible text or `aria-label`).

### V8 — Moderate — Focus indicator hard to see on cover CTA (2.4.7) *[keyboard pass]*

- **Where:** `/index.html` — “Open the contents”
- **Reproduce:** Keyboard-open cover → Tab to “Open the contents”.
- **Expected:** Clearly visible focus indicator.
- **Actual:** Element focused in a11y tree; focus ring not visually apparent in captured view.
- **Mitigation note:** Pack CSS does **not** set `outline: none` (good); `--focus` token exists but is largely unused for `:focus-visible` on CTAs.

### V9 — Moderate — No skip links pack-wide (2.4.1)

- **Evidence:** No skip-to-content patterns on priority pages; keyboard users must tab through sticky nav/toolbar on long lesson/quiz pages.

### V10 — Moderate — Missing `<main>` on most chrome pages (1.3.1 / related 2.4.1)

- **Evidence:** `<main>` present on cover and quiz; missing on begin, contents, decks, labs hub/labs (except steelman has neither shared nav nor main), dashboard. Lesson 1 uses `article` without `main`.

### V11 — Moderate — Cover orphan `h3`s under non-heading “The four arcs” (1.3.1 / 2.4.6)

- **Where:** `index.html` — section kicker is a `<p class="cover-kicker">`, then arc titles are `h3` without a parent `h2` for that section.

### V12 — Moderate — Limited explicit `:focus` styles on quiz/lab buttons (2.4.7)

- **Where:** Quiz CSS focuses `:focus` outline mainly on selects; buttons lack matching rules. Pack `--focus` unused in pack.css focus rules.

### Minor / lower

| ID | Sev | SC | Finding |
|----|-----|-----|---------|
| m1 | Minor | 3.2.5 / G201 | Lesson 1 external links `target="_blank"`; CSS `↗` cue; SR support for generated content inconsistent |
| m2 | Minor | 4.1.2 | Theme toggle uses changing name (“Dim mode” / “Bright mode”) without `aria-pressed` — name change communicates state (acceptable; pressed optional) |
| m3 | Minor | 4.1.2 | Some dynamic buttons omit `type="button"` when not in a form (low risk) |
| m4 | Minor | 1.1.1 / 1.4.1 | Dashboard progress bars are width-only; mitigated by adjacent text stats |
| m5 | Minor | 4.1.2 / 2.4.6 | Quiz radiogroup `aria-label` is “Question N” without linking stem via `aria-labelledby` |

---

## 5. Passes worth noting

- Universal `lang="en"` and unique, descriptive page titles.
- Theme toggle keyboard-reachable; name updates with mode; primary path controls operable without mouse (links, checkboxes, radios, select, textarea, buttons).
- No focus trap or major focus-order skip observed on priority path.
- No `outline: none` in pack CSS — default focus not stripped.
- Informative image alts on cover/lesson heroes; decorative empty `alt=""` on contents arc thumbs where adjacent text names the arc; cover rail `aria-hidden`.
- Lesson 1 sound heading hierarchy; SVG chart `role="img"` + `aria-label` + figcaption; data tables with `<th>`.
- Deck chooser checkboxes wrapped in `<label>`; quiz toolbar fields labeled; Fermi tiles are native `<button>` with textual Match/fail feedback (not color-only).
- Body / muted / nav link contrast generally AA in light and dim (computed from CSS variables).
- Shared grader confirmation uses `role="status"` in `shared.js` (positive pattern; Scenario Audit still has unnamed lock-copy control — V7).

---

## 6. Results summary

| Severity | Count (this pass) |
|----------|-------------------|
| Critical | 1 (V1 badge contrast) |
| Serious | 4 (V2–V5) |
| Moderate | 7 (V6–V12) |
| Minor | 5 |

**Blockers to further a11y testing:** None — pack is usable for continued WCAG work.

---

## 7. Residual accessibility risk

- **Contrast regressions in dim theme** remain likely wherever inline styles hard-code light-theme colors (steelman pattern).
- **Live-region strategy on quiz** may under-announce (V6) or over-announce (V5) depending on AT — needs SR verification (NVDA/VoiceOver) beyond a11y-tree inspection.
- **Lessons 2–7 and remaining labs** assumed similar patterns to Lesson 1 / audited labs; steelman is the outlier for chrome consistency and labeling.
- **Focus visibility on high-contrast CTAs / cover** may fail 2.4.7 for some users even though outline is not removed — recommend explicit `:focus-visible` using `--focus`.
- No automated full-page axe suite was run as the primary method; residual tooling gaps exist for zoom/reflow (1.4.4 / 1.4.10) and motion preferences.

---

## 8. Recommended fix priority (for sponsor)

1. Fix quiz `.badge-level` colors (Critical).
2. Fix contents `.arc-head` gold-on-teal in light; fix steelman dim CTA; associate steelman label.
3. Narrow quiz `aria-live`; announce practice feedback; name the Scenario Audit lock-copy control.
4. Add skip link + `<main>` landmarks; cover heading fix; `:focus-visible` styles.

---

## 9. Artifacts

Repo screenshot paths (copied from the 2026-09-15 keyboard WCAG pass):

- Begin: `docs/screenshots/2026-09-15/accessibility-wcag/01-begin.png`
- Cover: `docs/screenshots/2026-09-15/accessibility-wcag/02-cover.png`
- Deck Chooser: `docs/screenshots/2026-09-15/accessibility-wcag/03-decks.png`
- Scenario Audit lab: `docs/screenshots/2026-09-15/accessibility-wcag/04-scenario-audit-lab.png`
- Dashboard: `docs/screenshots/2026-09-15/accessibility-wcag/05-dashboard.png`
- Dashboard in dim theme: `docs/screenshots/2026-09-15/accessibility-wcag/06-dashboard-dim.png`

---

*End of Accessibility WCAG report.*
