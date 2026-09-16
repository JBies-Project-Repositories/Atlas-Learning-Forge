# Accessibility WCAG Report — **PASS 3**

**Tester:** Accessibility WCAG Tester  
**Label:** **PASS 3** / 2026-09-15 (PT)  
**Assigned by:** QA/Tester Lead  
**Target:** Atlas of the Build Loop — Study Pack (**16-lesson** field atlas)  
**URL:** `http://127.0.0.1:8765/`  
**Pack:** `/workspace/atlas-study-pack/pack/`  
**Compared to:** Pass 2 `/workspace/qa-reports/pass-2/Accessibility_WCAG_PASS2.md`  
**Brief:** `/workspace/qa-reports/pass-3/PASS3_BRIEF.md`

**Hard rules honored:** WCAG method only; no invented findings; no re-open of Pass 1/2 P0s without reproduced regression; no private master prompt; no old 7-lesson primer (spot-checked: no live `01_The_Loop` / `bl-01-loop` stems in pack HTML).

---

## 1. Scope & methodology

Focused Pass 3 charter from Lead:

1. Skip / `<main>` on chrome + **new lessons**
2. `#quiz-status` after a practice answer
3. Dim badges
4. Steelman label focuses the textarea
5. Theme `aria-pressed`

**Methods**
1. Static audit (HTML/CSS/JS) across chrome, all 16 lesson HTML files, quiz, labs.
2. Live keyboard/visual browser pass on `http://127.0.0.1:8765/` with screenshots under pack `docs/screenshots/2026-09-15/pass-3/`.

---

## 2. Focus-item results

| Focus item | Score | Evidence |
|------------|--------|----------|
| **Skip / main (chrome + new lessons)** | **PARTIAL** | **Static FIXED vs Pass 2 gaps:** skip + matching target id + `<main>` present on cover, contents, decks, dashboard, quiz, labs (incl. steelman), and **all 16** lesson HTML files (`href="#lesson"` → `id="lesson"`). Begin page has skip → `#begin-main` (id present) but **no** `<main>` (unchanged residual, not a new P0). **Live PARTIAL:** activating Skip on contents, lesson 16, decks, and dashboard updates hash and **scrolls** to the target, but `document.activeElement` remained **`BODY`** (focus not moved onto the landmark/target). Shots: `contents-skip-focused.png`, `lesson16-skip-focused.png`, `decks-skip.png`. |
| **`#quiz-status` after practice answer** | **PASS** | Path: `/03_quiz/index.html?decks=bl-a1-diverge` (Practice, L01). After one incorrect option, `#quiz-status` text was non-empty: *“Incorrect. That definition belongs to a different term in this lesson.”* Attributes: `role="status"`, `aria-live="polite"`. Matches `app.js` practice `onAnswer` writer. Shot: `quiz-status-after-answer.png`. Closes Pass 2 live gap on V6 / FIX-10 announcement wiring. |
| **Dim badges** | **PASS** | **Lesson** `article.lesson .badge` dim: `#062f2c` on `#8ee0cc` ≈ **9.43:1** (AA/AAA). Live on L16 dim: badge text clearly readable (`lesson16-dim-badge.png`). **Quiz** `.badge` dim override `#f4fbfc` on `#14343c` ≈ **12.64:1**; `.badge-level` uses `--text` / `--surface-2` ≈ **11.36:1** dim / **14.69:1** light. Pass 2 residual cream-on-accent dim ≈1.81:1 for lesson/quiz category pills **not reproduced** on current CSS. |
| **Steelman label → textarea focus** | **FAIL** | Markup has `for="text"` and nested `<textarea id="text">` inside the label (`04_labs/steelman.html`). Live click on visible “Your steelman” label text did **not** move focus into `#text`; `activeElement` stayed `BODY`. Shot: `steelman-label-focus.png`. Same residual as Pass 2 FIX-09 / V4 live PARTIAL — **not** closed. |
| **Theme `aria-pressed`** | **PASS** | `assets/theme.js` sets `aria-pressed`, `aria-label`, and button text on apply. Live on L16: dim → `aria-pressed="true"`, label “Switch to bright mode”, text “Bright mode”; after click → light, `aria-pressed="false"`, “Switch to dim mode” / “Dim mode”. |

---

## 3. Pass 1 / Pass 2 item delta (a11y only)

| ID / topic | Pass 2 | PASS 3 | Notes |
|------------|--------|--------|-------|
| V1 / FIX-03 badge contrast | PARTIAL | **FIXED** (contrast path) | Dim lesson + quiz badge CSS now AA+; live L16 dim readable. Prior blank level-pill runtime issue not re-hit this pass (not in charter to deep-dive). |
| V4 / FIX-09 steelman label | PARTIAL | **STILL OPEN (FAIL live)** | Association in DOM; activation still fails. |
| V6 / FIX-10 quiz-status | PARTIAL | **FIXED** | Live non-empty polite status after practice answer. |
| V9 skip links | PARTIAL | **PARTIAL** | Markup now pack-wide on chrome + 16 lessons; **focus move** after activate still missing. |
| V10 `<main>` | PARTIAL | **PARTIAL** | Present on chrome + lessons; begin still uses `#begin-main` without `<main>`. |
| V11 cover orphan h3s | STILL OPEN | **Not rechecked in depth** | Outside Pass 3 focus list; no new P0 raised. |
| Theme pressed state | (not scored) | **FIXED / PASS** | New charter item. |

No Pass 1/2 **P0** regressions reproduced.

---

## 4. Process / steps (PASS 3)

1. Confirmed HTTP 200 on `http://127.0.0.1:8765/`; inventory shows 16 lesson HTML files under `02_lessons/`.
2. Static scan: skip/`main`/theme/`quiz-status`/badge CSS/steelman `for=` across chrome + lessons + quiz + labs.
3. Live: contents + L16 skip; theme toggle aria; L16 dim badge; steelman label click; decks → practice quiz status; decks/dashboard skip.
4. Wrote this report; screenshots left in pack docs path per brief.

---

## 5. Findings this pass (charter residuals only)

1. **Skip does not move keyboard focus** (scroll/hash only) on contents, lesson 16, decks, dashboard — **Moderate** (2.4.1 / focus management). Markup presence is improved vs Pass 2.
2. **Steelman “Your steelman” label click does not focus `#text`** — **Serious** residual (3.3.2 / 1.3.1 practical labeling). Markup association present; live activation fails.
3. **Begin page still lacks `<main>`** — **Minor** residual (landmark consistency).

**Blockers:** None for continued pack use or other methodologies.

---

## 6. Results summary (PASS 3)

| Category | Count |
|----------|------:|
| Focus items PASS | 3 (quiz-status, dim badges, theme aria-pressed) |
| Focus items PARTIAL | 1 (skip/main) |
| Focus items FAIL | 1 (steelman label → focus) |
| New P0 | 0 |
| Reproduced P0 regression | 0 |

---

## 7. Residual a11y risk

- Keyboard users who activate Skip may land visually on content while focus remains on `BODY` (next Tab may restart at top chrome).
- Steelman writers who click the label may get no caret in the textarea (must click the field itself).
- Begin page landmark gap and cover heading structure (V11) remain polish backlog — not elevated this pass.

---

## 8. Artifacts

- **This report:** `/workspace/qa-reports/pass-3/Accessibility_WCAG_PASS3.md`
- Screenshots (pack): `/workspace/atlas-study-pack/pack/docs/screenshots/2026-09-15/pass-3/`  
  - `contents-skip-focused.png`, `lesson16-skip-focused.png`, `decks-skip.png`  
  - `lesson16-dim-badge.png`  
  - `quiz-status-after-answer.png`  
  - `steelman-label-focus.png`

---

*End of Accessibility WCAG PASS 3 report.*
