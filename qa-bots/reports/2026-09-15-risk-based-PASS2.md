# Risk-Based Testing Report — PASS 2 — Atlas of the Build Loop Study Pack

| Field | Value |
| --- | --- |
| **Label** | **PASS 2** / 2026-09-15 |
| **Date** | 2026-09-15 PT |
| **Target** | Atlas of the Build Loop — Study Pack (post CLI fix brief) |
| **Methodology** | Risk-based testing only (re-open Pass 1 register → re-score with fix evidence → verify FIX-01..15 → hunt regressions) |
| **Environment** | `http://127.0.0.1:8765/` (HTTP 200 on entry); pack `pack/` |
| **Entry** | `http://127.0.0.1:8765/00_CLICK_HERE_TO_BEGIN.html` |
| **Pass 1 baseline** | `qa-bots/reports/risk-based-atlas-study-pack.md` and `qa-bots/reports/2026-09-15-risk-based-atlas-study-pack.md` |
| **Fix brief** | `qa-bots/reports/CLI_FIX_BRIEF_Atlas_Study_Pack.md` |
| **Tools** | Shell, Read, curl, node (source + HTTP; no invented results) |

---

## 1. Prioritization rationale (Pass 2 effort)

Pass 2 effort ordered by **former High scores first**, then mapped FIX verification, then regression hunt from fix diffs:

1. **Former High (Pass 1 score ≥ 9):** R01 (grader domain), R02 (`file://` progress), R03 (exam unanswered inflation), R04 (empty decks → all).
2. **P0 FIX-01..FIX-04** mapped to those risks (+ badge contrast FIX-03 under R13 residual).
3. **P1 FIX-05..FIX-10** mapped to R02/R05/R07/R08/R06 and a11y.
4. **P2 FIX-11..FIX-15** scored opportunistically from source (cheap static checks).
5. **Regression hunt:** sibling BAT launchers, dim-theme badge contrast, theme `aria-pressed` gap.

Not checklist QA, exploratory charters, or full a11y audit — risk-driven retest only.

---

## 2. Risk register (Pass 1 → Pass 2)

Impact (1–5) × Likelihood (1–5) = Priority. Status: **FIXED** / **PARTIAL** / **OPEN** / **ACCEPTED** / **REGRESSION**.

| ID | Risk | P1 I×L | P1 Score | P2 I×L | P2 Score | Status | Score Δ | Pass 2 evidence (short) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R01 | Steelman grader wrong domain (cardio/physiology/bloodwork) | 3×5 | **15** | 3×1 | **3** | **FIXED** | **−12** | `04_labs/shared.js` `GRADER_PROMPTS.steelman.text` is Build Loop only; `cardio\|physiology\|bloodwork` absent in pack JS/HTML |
| R02 | `file://` / BAT open → localStorage origin split | 4×3 | **12** | 4×2 | **8** | **PARTIAL** | **−4** | Primary `00_CLICK_HERE_TO_BEGIN.bat` + README + START HERE prefer `python -m http.server 8765`; sibling `Open *.bat` still `Start-Process` file paths |
| R03 | Exam unanswered → wrong + `quiz.answered` inflate | 3×4 | **12** | 3×1 | **3** | **FIXED** | **−9** | `submitExam` only `recordAnswer` when `answerKey != null`; hint: “Unanswered items are skipped”; node sim 8 unanswered → answered 0 |
| R04 | Deck chooser empty → `decks=all` | 3×3 | **9** | 3×1 | **3** | **FIXED** | **−6** | `decks.html`: empty removes `href`, `aria-disabled`, shows “Select at least one deck.”; no `ids.length===0?'all'` |
| R05 | `markLesson` unused / lesson progress dead | 2×4 | **8** | 2×1 | **2** | **FIXED** | **−6** | All 7 lessons load `../04_labs/shared.js` and call `markLesson(...)`; dashboard renders lesson read state |
| R06 | A11y: steelman label; theme pressed state | 2×4 | **8** | 2×2 | **4** | **PARTIAL** | **−4** | Steelman `<label for="text">` fixed; `theme.js` still no `aria-pressed` |
| R07 | Reset clears theme with progress | 2×3 | **6** | 2×1 | **2** | **FIXED** | **−4** | `dashboard.html` confirm lists progress keys only; does **not** remove `atlas_build_loop_theme_v1` |
| R08 | Begin/cover omit Dashboard | 2×3 | **6** | 2×1 | **2** | **FIXED** | **−4** | Begin + Cover link `dashboard.html`; Steelman topbar includes Dashboard |
| R09 | Broken pack nav / dead links | 5×1 | **5** | 5×1 | **5** | **ACCEPTED** (mitigated) | 0 | Spot-check HTTP 200 on entry, contents, decks, quiz variants, labs, dashboard, assets |
| R10 | Quiz bank / scoring integrity | 5×1 | **5** | 5×1 | **5** | **ACCEPTED** (mitigated) | 0 | Bank still 56 unique IDs; scoring path unchanged for answered items |
| R11 | Missing assets under HTTP | 5×1 | **5** | 5×1 | **5** | **ACCEPTED** (mitigated) | 0 | CSS/JS/lab/lesson assets 200 |
| R12 | Lab hard breakage (missing DOM/handlers) | 5×1 | **5** | 5×1 | **5** | **ACCEPTED** (mitigated) | 0 | Steelman/shared wiring intact; no new missing-id signal in static read |
| R13 | Theme / dim unreadability | 3×1 | **3** | 3×2 | **6** | **PARTIAL** | **+3** | Dim/light tokens OK overall; **dim `.badge` cream on cyan ~1.81:1** (see FIX-03 / NR01) |
| R14 | Timer hint 15–120 vs options max 60 | 1×3 | **3** | 1×1 | **1** | **FIXED** | **−2** | Mode hint now “15 / 30 / 45 / 60 minutes”; options match |

### New risks found in Pass 2 (fix-introduced / residual)

| ID | Risk | I×L | Score | Status | Notes |
| --- | --- | --- | --- | --- | --- |
| **NR01** | Dim-theme quiz lesson `.badge` contrast ~**1.81:1** (`#fff6d6` on `#5ec8d6`) | 3×3 | **9** | **OPEN** | Light badge ~5.49:1 OK; `.badge-level` OK both themes. FIX-03 incomplete for dim `.badge`. |
| **NR02** | Sibling `Open Home/Dashboard/Deck/Labs/Quiz.bat` still open via **file://** while primary BAT prefers HTTP | 3×2 | **6** | **OPEN** | Increases R02 residual if learners use shortcut BATs. |

No **REGRESSION** that re-opens a Pass 1 High as worse than before for R01/R03/R04 (those are FIXED). R13 score **rose** due to measured dim badge gap (related to incomplete FIX-03), not a new theme-toggle breakage.

---

## 3. FIX-01 … FIX-15 scorecard

| FIX | Maps to | Status | Evidence |
| --- | --- | --- | --- |
| **FIX-01** Empty decks must not start all | R04 | **FIXED** | `decks.html` L58–75: empty → remove href, `is-disabled`, show `#deck-error`; click preventDefault; sync on load |
| **FIX-02** Steelman grader Build Loop domain | R01 | **FIXED** | `shared.js` steelman prompt: “Atlas of the Build Loop… loops, methods, intent…”; no cardio residue (node + rg) |
| **FIX-03** Quiz level/badge contrast ≥4.5:1 both themes | R13 / NR01 | **PARTIAL** | `.badge-level` uses `--text` on `--surface-2` (high contrast). `.badge` `#fff6d6` on `--accent`: light **5.49:1**, dim **1.81:1** FAIL |
| **FIX-04** Exam unanswered progress integrity | R03 | **FIXED** | `app.js` `submitExam`: unanswered skipped; unique-ID `recordProgressEvent`; dashboard copy documents skip rule |
| **FIX-05** Prefer HTTP launch / warn file:// | R02 / NR02 | **PARTIAL** | Primary BAT starts server+HTTP; README/START HERE warn. Sibling Open*.bat still file:// |
| **FIX-06** Wire `markLesson` | R05 | **FIXED** | All 7 lesson HTML: `shared.js` + `AtlasProgress.markLesson(...)`; dashboard lists reads |
| **FIX-07** Reset keeps theme | R07 | **FIXED** | Clear removes progress/weak/srs only; confirm text says keeps theme |
| **FIX-08** Dashboard discoverability / nav | R08 | **FIXED** | Begin + Cover Dashboard links; Steelman shared topbar with Dashboard |
| **FIX-09** Arc-head contrast + Steelman label/CTA | R06 partial | **FIXED** | Arc-head `#fff6d6` on `#1c5d68` ~**6.89:1**; `#next` dim text-on-btn ~**10.58:1**; `label for="text"` |
| **FIX-10** Quiz live regions + lock-copy name | R06 / a11y | **FIXED** | `#quiz` main has no `aria-live`; `#quiz-status` announces Incorrect/Correct; lock-copy `aria-label="Copy LOCK grader prompt"` |
| **FIX-11** Weak panel refresh after clear | (BVA) | **FIXED** | Clear → `showWeakReport` / immediate empty-state HTML (no collapse required) |
| **FIX-12** Steelman empty Score validation | (BVA) | **FIXED** | `#score-error` role=status + scrollIntoView when length &lt; 40 |
| **FIX-13** SRS rating copy | — | **FIXED** | Spaced: “Again/Hard/Good/Easy…” hint; dashboard: rating ≠ reveal |
| **FIX-14** Timer hint vs options | R14 | **FIXED** | Hint aligned to 15/30/45/60; options stop at 60 |
| **FIX-15** Skip link, main, `:focus-visible` | a11y | **PARTIAL** | Skip + `:focus-visible` on pack.css; begin/quiz/dashboard have skip/`<main>`; contents/decks/labs not uniformly covered |

---

## 4. Tests run vs top risks / FIX verification

### 4.1 R01 / FIX-02 — Grader domain

- Read `04_labs/shared.js` `GRADER_PROMPTS.steelman.text`.
- Node extract: `cardio residual=false`, `build-loop domain=true`.
- Pack-wide rg: only mention of cardio is historical note in `01_source/SOURCE_NOTES.md` (“No cardio content…”), not grader prompt.

**Result:** FIXED (score 15 → 3).

### 4.2 R04 / FIX-01 — Empty deck selection

- Source: empty selection disables Start (`href` removed, `pointer-events:none`, error message).
- Explicit “All 56 exam path” secondary link still goes to `decks=all` (intentional escape hatch, not empty-coerce).
- HTTP: `GET /decks.html` → 200.

**Result:** FIXED (score 9 → 3).

### 4.3 R03 / FIX-04 — Exam unanswered

- `submitExam` loop: `if (item.answerKey != null) { … recordAnswer … }` — no unanswered → wrong path.
- Mode hint documents skips.
- Node simulation: 8 unanswered → `{answered:0, progressAnswers:0}`; 1 correct + 7 blank → answered 1.
- `recordProgressEvent` uses unique question IDs (`data.quiz.ids`).

**Result:** FIXED (score 12 → 3).

### 4.4 R02 / FIX-05 — Launch / origin

- `00_CLICK_HERE_TO_BEGIN.bat`: prefers Python HTTP server on 8765, opens `http://127.0.0.1:8765/...`; file:// fallback with warning.
- README + START HERE document preferred HTTP and file:// risk.
- **Gap:** `Open Home.bat`, `Open Dashboard.bat`, `Open Deck Chooser.bat`, `Open Labs.bat`, `Open Quiz.bat` still `Start-Process` on HTML files (file://).

**Result:** PARTIAL (score 12 → 8). New residual **NR02**.

### 4.5 R05 / FIX-06 — Lesson mark

- All seven `02_lessons/*.html` include `shared.js` and call `markLesson`.
- `dashboard.html` renders `data.lessons` read chips + documents quiz count rule.

**Result:** FIXED (score 8 → 2).

### 4.6 R07 / FIX-07 — Reset vs theme

- Confirm dialog: clears progress/weak/srs; **Keeps: theme**.
- `removeItem` calls omit `atlas_build_loop_theme_v1`.

**Result:** FIXED (score 6 → 2).

### 4.7 R08 / FIX-08 — Dashboard discoverability

- Begin: Dashboard secondary card; Cover: `cta-secondary` Dashboard; Steelman topbar Dashboard link.

**Result:** FIXED (score 6 → 2).

### 4.8 R06 / FIX-09 / FIX-10 — A11y slices

- Steelman label associated; lock-copy named; quiz status live region; main no longer whole-page live.
- Theme toggle: visible label swap only — **no `aria-pressed`** (`theme.js`).

**Result:** R06 PARTIAL (8 → 4).

### 4.9 R13 / FIX-03 — Badge contrast (measured)

| Pair | Approx contrast | Pass ≥4.5? |
| --- | --- | --- |
| Light `.badge` `#fff6d6` on `#0a6e7c` | 5.49:1 | Yes |
| Dim `.badge` `#fff6d6` on `#5ec8d6` | **1.81:1** | **No** |
| `.badge-level` light/dim text on surface-2 | 14.69 / 11.36 | Yes |
| Arc-head `#fff6d6` on `#1c5d68` | 6.89:1 | Yes |

**Result:** FIX-03 PARTIAL; **NR01 OPEN (score 9)**; R13 score rose 3 → 6.

### 4.10 R14 / FIX-14 + P2 spot checks

- Timer hint/options aligned → R14 FIXED.
- FIX-11/12/13 source-confirmed FIXED; FIX-15 PARTIAL (skip coverage uneven).

### 4.11 Navigation / assets (R09/R11)

curl HTTP 200: begin, cover, contents, dashboard, decks, quiz (`?decks=all`, `?decks=bl-01-loop`), steelman, shared.js, pack.css, theme.js, Lesson 1.

### 4.12 Quiz bank (R10)

Node load `questions.js`: count=56, unique IDs=56.

---

### 4.13 Headed browser confirmation (post-report)

Headed pass on `http://127.0.0.1:8765/` after report write — **all targeted checks PASS; no score changes** vs §2 register.

| Check | Result |
| --- | --- |
| FIX-01 / R04 Select none | PASS — Start removed / chooser stayed |
| FIX-02 / R01 Steelman prompt | PASS — Build Loop domain only |
| FIX-04 / R03 progress | PASS — 1 practice answer → Dashboard 1; 0-answer exam → 0/56 |
| FIX-08 / R08 Dashboard | PASS — Begin/Cover ≤1 click |
| FIX-07 / R07 Reset vs theme | PASS — Dim kept; progress 0 |
| Theme + nav smoke | PASS |

Screenshots under `(session browser shots)/` from this headed run.

## 5. Findings (severity tied to risk IDs)

| Severity | Finding | Risk / FIX |
| --- | --- | --- |
| **Medium (new)** | Dim-theme quiz `.badge` text contrast ~1.81:1 (cream on cyan) | **NR01**, FIX-03 PARTIAL, R13↑ |
| **Medium (residual)** | Sibling Open*.bat still file://; progress may not share if those shortcuts used | **NR02**, R02 PARTIAL, FIX-05 PARTIAL |
| **Low** | Theme toggle lacks `aria-pressed` | R06 PARTIAL |
| **Low** | Skip/`<main>` not universal on contents/decks/all labs | FIX-15 PARTIAL |
| **Pass / fixed** | Steelman grader Build Loop domain | R01, FIX-02 |
| **Pass / fixed** | Empty decks cannot coerce to all | R04, FIX-01 |
| **Pass / fixed** | Unanswered exam does not inflate answered/weak-as-wrong | R03, FIX-04 |
| **Pass / fixed** | Primary HTTP launch + docs | R02 core path, FIX-05 partial |
| **Pass / fixed** | Lesson markLesson wired + dashboard reads | R05, FIX-06 |
| **Pass / fixed** | Reset preserves theme | R07, FIX-07 |
| **Pass / fixed** | Begin/Cover/Steelman Dashboard discoverability | R08, FIX-08 |
| **Pass / fixed** | Arc-head contrast, Steelman label, New prompt dim CTA | FIX-09 |
| **Pass / mitigated** | Nav/assets/bank under HTTP | R09–R12, R10 |

**Blockers for learner ship under recommended HTTP path:** **none**.

---

## 6. Residual risks not covered this pass

- ~~Headed browser click-through~~ **DONE post-file:** FIX-01/R04 Select none stays on chooser; FIX-02/R01 Steelman Build Loop prompt; FIX-04/R03 practice 1 answer → Dashboard 1, exam 0 answers → 0/56; FIX-08/R08 Begin/Cover→Dashboard 1 click; FIX-07/R07 Dim retained after Reset; theme + Contents→Lesson1 nav PASS. **No risk score changes.**
- Measured `file://` multi-page localStorage on Chrome/Edge (packaging residual R02/NR02).
- Full axe/Lighthouse; mobile layout; SRS multi-day schedule correctness; concurrent-tab races.
- Exam percentage still `correct/session.length` (includes blanks in denominator) — intentional exam grading; answered count separately honest.

---

## 7. Recommendations (risk-ordered)

1. **NR01 / FIX-03 complete** — In dim theme, set `.badge { color: … }` to dark text on cyan (or darken accent) so contrast ≥4.5:1; keep light as-is.
2. **NR02 / FIX-05 complete** — Point sibling `Open *.bat` at `http://127.0.0.1:8765/...` (or reuse primary BAT server start), or delete/relabel them as file://-unsafe.
3. **R06** — Add `aria-pressed` (or equivalent) on `[data-theme-toggle]` when applying theme.
4. **FIX-15** — Add skip + landmark consistency on contents/decks/labs index.
5. Re-smoke R01–R04 in a headed private window after NR01/NR02 polish.

---

## 8. Summary for Lead handoff

| Item | Result |
| --- | --- |
| **Report paths** | `qa-bots/reports/pass-2/risk-based-PASS2.md` (primary); `/workspace/atlas-study-pack/risk-based-PASS2.md` (copy) |
| **R01–R14 status** | FIXED: R01, R03, R04, R05, R07, R08, R14 · PARTIAL: R02, R06, R13 · ACCEPTED/mitigated: R09–R12 · OPEN: none of original as fully open High |
| **New risks** | **NR01** dim badge contrast (9); **NR02** sibling BAT file:// (6) |
| **Top remaining scores** | NR01 **9**, R02 **8**, R13 **6**, NR02 **6**, R09–R12 **5**, R06 **4** |
| **Largest score drops vs Pass 1** | R01 **−12**, R03 **−9**, R04 **−6**, R05 **−6**, R02 **−4**, R06/R07/R08 **−4** each; R13 **+3** (dim badge) |
| **FIX-01..15** | FIXED: 01,02,04,06,07,08,09,10,11,12,13,14 · PARTIAL: 03,05,15 · STILL OPEN: none fully untouched |
| **Blockers** | **none** (recommended HTTP launch path) |
| **Former Highs** | R01/R03/R04 **FIXED**; R02 **PARTIAL** (docs+primary BAT good; shortcuts lag) |

PASS 2 risk-based retest confirms P0 functional defects (grader domain, empty decks, exam unanswered inflation) are fixed in source. Remaining medium attention: **dim badge contrast** and **sibling BAT file://** shortcuts.
