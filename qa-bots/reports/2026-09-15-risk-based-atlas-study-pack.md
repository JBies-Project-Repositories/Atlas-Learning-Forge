# Risk-Based Testing Report — Atlas of the Build Loop Study Pack

| Field | Value |
| --- | --- |
| **Date** | 2026-09-15 PT |
| **Target** | Atlas of the Build Loop — Study Pack (offline HTML) |
| **Methodology** | Risk-based testing only (identify → score → prioritize → test highest risks first) |
| **Environment URL** | `http://127.0.0.1:8765/` (server was already up; HTTP 200 on entry) |
| **Entry** | `http://127.0.0.1:8765/00_CLICK_HERE_TO_BEGIN.html` |
| **Surfaces mapped** | begin → cover (`index.html`) → contents → 7 lessons → quiz (56 Q) → labs (SRS, scenario/bias, term match/fermi, steelman) → dashboard → theme toggle |

---

## 1. App map (from disk)

| Area | Paths |
| --- | --- |
| Entry / cover / TOC | `00_CLICK_HERE_TO_BEGIN.html`, `index.html`, `contents.html` |
| Lessons | `02_lessons/01_…` … `07_….html` (+ `.md` sources) |
| Quiz | `decks.html`, `03_quiz/index.html`, `app.js`, `questions.js`, `styles.css` |
| Labs | `04_labs/index.html`, `spaced.html`, `bias.html`, `fermi.html`, `steelman.html`, `shared.js` |
| Dashboard | `dashboard.html` (reads `AtlasProgress` from `04_labs/shared.js`) |
| Assets | `assets/pack.css`, `assets/theme.js`, `cover.jpg`, `arc-a.jpg`…`arc-d.jpg` |
| localStorage keys | `atlas_build_loop_progress_v1`, `atlas_build_loop_weak_v1`, `atlas_build_loop_srs_v1`, `atlas_build_loop_theme_v1` |

No auth. Progress is browser-local only.

---

## 2. Risk register

Impact (1–5) × Likelihood (1–5) = Priority. Scores refined after code/HTTP evidence (not left at “suggested theme” defaults).

| ID | Risk | Impact | Likelihood | Score | Rationale |
| --- | --- | --- | --- | --- | --- |
| R01 | Steelman Grok grader prompt is wrong domain (cardio/physiology/bloodwork) while lab UI is Build Loop | 3 | 5 | **15** | Confirmed in `04_labs/shared.js` `GRADER_PROMPTS.steelman.text`; lab `ITEMS` are build-loop misconceptions. Every grader copy-paste mis-teaches domain. |
| R02 | `file://` open via `.bat` / double-click → localStorage origin fragmentation / progress loss across pages | 4 | 3 | **12** | README/BAT open HTML via `Start-Process` file paths, not `http://127.0.0.1:8765`. Chromium often treats distinct `file://` paths as separate opaque origins; dashboard/quiz/labs may not share keys. |
| R03 | Exam submit treats unanswered as wrong **and** increments `quiz.answered` | 3 | 4 | **12** | `03_quiz/app.js` `submitExam`: unanswered branch calls `recordAnswer(q, false)` which always calls `recordProgressEvent("answer")`. Inflates dashboard “Quiz answers recorded” and pollutes weak-area stats. |
| R04 | Deck Chooser “Select none” still launches `decks=all` | 3 | 3 | **9** | `decks.html`: `ids.length === 0 ? 'all'`. User can believe they cleared decks but still get full 56. |
| R05 | Lesson read progress never written (`markLesson` unused) | 2 | 4 | **8** | `shared.js` defines `markLesson`; no lesson HTML includes `shared.js` or calls it. Dashboard suggestions ignore actual reading. |
| R06 | Accessibility: unlabeled / weakly labeled controls (steelman textarea; theme toggle state) | 2 | 4 | **8** | Steelman: `<label>` not associated with `#text` via `for`. Theme toggle relies on visible text only (no `aria-pressed`). Decorative `alt=""` on arc images is acceptable. |
| R07 | Dashboard “Reset” also clears theme preference | 2 | 3 | **6** | `dashboard.html` clear handler removes `atlas_build_loop_theme_v1` with progress keys. |
| R08 | Cover / begin omit Dashboard link (discoverability) | 2 | 3 | **6** | Begin and cover CTAs skip dashboard; only TOC/topbars/labs/quiz footer expose it. Not a dead link, but progress surface is easy to miss. |
| R09 | Broken pack navigation / dead relative links | 5 | 1 | **5** | Crawl of unique pack `href`/`src` URLs: **29/29 HTTP 200**. All primary surfaces + assets 200 under `:8765`. Residual likelihood low after verification. |
| R10 | Quiz core scoring wrong / bank incomplete (≠56, multi-correct, bad keys) | 5 | 1 | **5** | Bank: 56 unique IDs, 8×7 lessonIds matching `decks.html`, exactly one `correct:true` each. Simulated scores: all-correct 56/56, empty 0, last-only 1, all-wrong 0. |
| R11 | Missing assets / broken relative paths under HTTP serve | 5 | 1 | **5** | Images, CSS, JS, lab HTML all 200 from pack root server. Nested `../assets/` paths resolve. |
| R12 | Lab hard breakage (undefined handlers / missing DOM ids) | 5 | 1 | **5** | For spaced/bias/fermi/steelman: all `getElementById` / `#id` query targets exist; `touchLab` ids match dashboard meta (`spaced`,`bias`,`fermi`,`steelman`). |
| R13 | Theme toggle / dim mode unreadable | 3 | 1 | **3** | `theme.js` + `[data-theme-toggle]` present together on surfaces checked; `pack.css` defines dim tokens (`--text`, `--bg`, etc.). Primary CTAs use dark text on teal (readable). |
| R14 | Quiz timer UX copy vs UI (hint mentions 15–120; select max 60) | 1 | 3 | **3** | `app.js` mode hint says “15–120”; `index.html` options stop at 60. Misleading, not a scoring break. |

---

## 3. Prioritization rationale

Effort was ordered by **score descending**, then by blast radius for learner trust (wrong feedback / lost progress) over cosmetic issues.

1. **R01 (15)** — Lab feature that actively misinstructs when used (grader).
2. **R02 (12)** — Default Windows open path may silently break the whole progress model.
3. **R03 (12)** — Corrupts metrics learners use to decide “what’s next.”
4. **R04 (9)** — Surprising quiz session composition.
5. **R05–R08 (8–6)** — Progress fidelity and a11y/discoverability.
6. **R09–R12 (5)** — High impact *if* true; evidence shows they are largely mitigated under HTTP.
7. **R13–R14 (3)** — Lower residual after inspection.

This is intentionally **not** checklist QA, exploratory charters, or full regression matrices—only risk-driven checks.

---

## 4. Tests run against top risks (evidence)

### 4.1 Navigation / assets (R09, R11)

- Confirmed server: `GET /00_CLICK_HERE_TO_BEGIN.html` → **200**.
- Python crawl of all pack HTML `href`/`src` (non-external): **29 unique URLs, 0 failures**.
- Explicit surface map all **200**, including quiz query variants (`?decks=all`, single deck, multi-deck), all 7 lessons, 4 labs, dashboard, assets, `Curriculum.md`.
- Lesson-internal relative links (`../contents.html`, prev/next in `lesson-nav`): no internal 404s.
- External lesson citations (`agilemanifesto.org`, `scrumguides.org`) return **200** via `curl -sL` (offline pack still depends on network for those citations only).

### 4.2 Quiz bank + scoring (R10, R03, R14)

- Loaded `questions.js` in Node (`window.QUESTIONS`): **count=56**, unique IDs=56, per-`lessonId` all **8**, IDs align with `decks.html` checkbox values.
- Option integrity: **0** questions with ≠1 correct option; no missing stems.
- Scoring simulation mirroring `updateStats` / submit math:
  - all correct → `{correct:56, answered:56, pct:100}`
  - empty → `{correct:0, answered:0, pct:0}`
  - last Q only → `{correct:1, answered:1, pct:2}`
  - all wrong → `{correct:0, answered:56, pct:0}`
- DOM wiring: every static `getElementById` in `app.js` exists in `03_quiz/index.html` (dynamic weak-panel buttons created at runtime).
- **Finding R03**: `submitExam` unanswered path (`app.js` ~461–463) records wrong + progress answer increment.
- **Finding R14**: timer select max 60 vs hint “15–120”.

### 4.3 localStorage / dashboard (R02, R05, R07)

- Key inventory (writers ↔ clear):

  | Key | Writers | Dashboard clear? |
  | --- | --- | --- |
  | `atlas_build_loop_progress_v1` | `shared.js`, quiz `recordProgressEvent` | yes |
  | `atlas_build_loop_weak_v1` | quiz `STORAGE_KEY` | yes |
  | `atlas_build_loop_srs_v1` | `spaced.html` `STORE` | yes |
  | `atlas_build_loop_theme_v1` | `theme.js` | **yes (side effect)** |

- Dashboard reads `data.quiz.answered` / `data.labs.*` consistently with `AtlasProgress.load()` shape.
- **R05**: `markLesson` never invoked from lesson pages.
- **R02**: `.bat` files use `Start-Process` on `.html` file paths (file protocol), while this test environment used HTTP—progress behavior under `file://` remains a residual risk.

### 4.4 Labs (R01, R12)

- Element ID audit: **no missing** `getElementById` targets in spaced / bias / fermi / steelman.
- `touchLab` ids: `spaced`, `bias`, `fermi`, `steelman` — match dashboard `labMeta`.
- Content presence: fermi **77** pairs with `why`; spaced 7 decks with `terms` arrays; steelman **21** Build Loop weak takes; bias `SCENES` for all 7 `bl-*` lesson ids.
- Term Match settle logic: match when `pickL === pickR` (shared pair id)—structurally sound.
- SRS `schedule()` present with EF / interval updates; state key `atlas_build_loop_srs_v1`.
- **R01 confirmed**: `shared.js` steelman grader text still says *“misconceptions about cardio training, physiology, and bloodwork”* while `steelman.html` ITEMS are loop/Agile/MVP/shipping takes.

### 4.5 Theme (R13)

- Pages with toggle also load `assets/theme.js` (no orphans).
- `theme.js` toggles `data-theme` dim/light and persists `atlas_build_loop_theme_v1`.
- `pack.css` `[data-theme="dim"]` sets readable token set; quiz `styles.css` also theme-aware.


### 4.7 Interactive browser pass (headed, HTTP)

Exercised on `http://127.0.0.1:8765/` after static/code analysis. Confirms several high-impact risks are mitigated **under HTTP**, and does **not** retire R01–R04 (those are code-path defects not disproved by happy-path clicks).

| Area | Result | Evidence |
| --- | --- | --- |
| Navigation (begin → cover → contents → The Loop + Project Management Methodology → contents) | **PASS** | No dead links, blank pages, or wrong targets. Supports R09 mitigated. |
| Quiz (Deck Chooser → The Loop practice; mixed answers; Clear answers) | **PASS** | Score updated to **5/8**; reset worked; no stuck state. Supports R10 scoring math. Did not exercise exam unanswered path (R03) or Select none (R04). |
| Labs (SRS, Scenario Audit, Term Match, Steelman) | **PASS** (minor UX) | Controls responded; lab actions recorded. Steelman score rubric **visually delayed** while numeric score reached **5/5** (Low usability; not a scoring-logic fail). Grader copy-paste domain (R01) not exercised in UI. |
| Dashboard | **PASS** | Quiz/lab activity visible (answers, visits, actions, best scores) after return/refresh. Progress shared across pages **on this HTTP origin**. Does not disprove R02 `file://` origin split. |
| Theme toggle (Cover, Dashboard) | **PASS** | Layout/contrast/nav readable; toggle label changed. Supports R13 mitigated. |

Repo screenshot paths (copied from the 2026-09-15 risk-based headed pass):

- `docs/screenshots/2026-09-15/risk-based/01-begin.png` — begin page
- `docs/screenshots/2026-09-15/risk-based/02-quiz-the-loop.png` — The Loop practice quiz
- `docs/screenshots/2026-09-15/risk-based/03-dashboard-dim.png` — dashboard in dim theme
- `docs/screenshots/2026-09-15/risk-based/04-dashboard-bright.png` — dashboard in bright theme
- `docs/screenshots/2026-09-15/risk-based/05-steelman-grader.png` — Steelman lab 5/5 with grader prompt still mentioning cardio/physiology/bloodwork (R01)

### 4.6 file:// vs http

- Documented learner path: double-click HTML / BAT → **file://**.
- Validated path for this run: **http://127.0.0.1:8765/** from pack root.
- No code hard-requires absolute `http://127.0.0.1` URLs (relative paths)—good for both—but **storage sharing** differs by protocol/origin.

---

## 5. Findings (severity tied to risk IDs)

| Severity | Finding | Risk ID |
| --- | --- | --- |
| **High** | Steelman “Copy grader prompt” instructs Grok on **cardio/physiology/bloodwork**, not Build Loop content (`04_labs/shared.js`). | R01 |
| **High** | Default Windows BAT/HTML open uses **file://**, risking split/empty localStorage vs HTTP testing; progress/dashboard may appear “broken” for real learners. | R02 |
| **Medium** | Exam submit on unanswered items records **wrong** in weak stats and **increments** `quiz.answered` (dashboard inflation). | R03 |
| **Medium** | Deck Chooser **Select none** still navigates to `03_quiz/index.html?decks=all`. | R04 |
| **Low** | `markLesson` API unused; lesson reading not reflected in progress model. | R05 |
| **Low** | Steelman textarea label not programmatically associated (`for`/`id`); theme toggle lacks pressed-state semantics. | R06 |
| **Low** | Progress reset clears **theme** key as well. | R07 |
| **Low** | Begin/cover do not link to Dashboard (discoverability). | R08 |
| **Low** | Exam mode hint mentions timers up to **120** minutes; UI only offers through **60**. | R14 |
| **Low** | Steelman score rubric visually lagged the numeric **5/5** update (headed UI). | R12 residual UX (lab otherwise functional) |
| **Pass / mitigated** | Pack-relative navigation and assets all HTTP 200 under test server. | R09, R11 |
| **Pass / mitigated** | Quiz bank 56/56 integrity + scoring math for empty/full/last/wrong. | R10 |
| **Pass / mitigated** | Lab DOM/handlers and progress lab ids consistent; no static undefined-handler breakage found. | R12 |
| **Pass / mitigated** | Theme toggle + dim tokens present; no obvious unreadable dim primary path. | R13 |

---

## 6. Residual risks not covered

- **Full 56-question exam / timer auto-submit / reshuffle** — headed pass covered a single 8-question practice deck (5/8 + reset), not exam unanswered (R03) or all-deck exam.
- **Actual `file://` multi-page localStorage behavior** on Chrome/Edge/Firefox (R02 hypothesized from packaging; not re-measured in a headed browser this run).
- **Clipboard / Grok grader** end-to-end (R01 content bug confirmed; copy API not exercised).
- **SRS long-horizon scheduling** correctness (intervals over days) and card-content pedagogical accuracy.
- **Bias scenario key completeness** vs planted errors (structure present; answer-key pedagogy not graded).
- **Contrast WCAG measurement** (token review only; no axe/lighthouse run).
- **Mobile layout** of term-match board / quiz toolbar.
- **Concurrent tab** localStorage races.
- External citation link availability when fully offline (expected limitation for an offline pack that still links out).

---

## 7. Recommendations (risk-ordered)

1. **R01** — Rewrite `GRADER_PROMPTS.steelman.text` in `04_labs/shared.js` to Build Loop / shipping misconceptions (match lab `ITEMS`); remove cardio/physiology/bloodwork residue.
2. **R02** — Prefer documenting/serving via local HTTP (or a launcher that starts `python -m http.server` / similar) so all pages share one origin; warn that pure `file://` may not persist progress across pages.
3. **R03** — On exam submit: do not call `recordProgressEvent("answer")` for unanswered items; optionally skip weak tracking or record “skipped” separately from wrong.
4. **R04** — If zero decks selected, disable Start or keep previous selection; do not coerce to `all`.
5. **R05** — Either wire `markLesson` from lesson pages or drop unused API / dashboard expectations.
6. **R06** — Associate steelman `<label for="text">`; add `aria-pressed` on theme toggle.
7. **R07** — Reset progress keys without clearing `atlas_build_loop_theme_v1` (or confirm UX intent in copy).
8. **R08 / R14** — Add Dashboard to begin/cover; align timer hint with actual `<option>` values.

---

## 8. Summary for handoff

Risk-based testing under `http://127.0.0.1:8765/` found **navigation/assets/quiz-bank core healthy** (confirmed in headed browser: nav, 5/8 practice quiz + reset, labs, dashboard persistence, theme). Highest residual defects remain **grader domain mismatch (R01)**, **file:// progress risk (R02)**, and **exam unanswered → progress/weak pollution (R03)**. Headed pass did not retire those code-path risks.
