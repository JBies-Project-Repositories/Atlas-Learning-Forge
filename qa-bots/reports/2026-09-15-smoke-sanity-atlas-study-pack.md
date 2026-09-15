# Smoke & Sanity Test Report — Atlas of the Build Loop (Study Pack)

**Tester:** Smoke & Sanity Tester  
**Lead:** QA/Tester Lead  
**Target:** Atlas of the Build Loop — Study Pack (offline HTML field guide)  
**Date:** 2026-09-15 (PT)  
**Environment:** Shared test URL `http://127.0.0.1:8765/` (local static server). Fallback pack path `/workspace/atlas-study-pack/pack/`.  
**Auth:** None (no login). Educational offline pack; not a credential.

---

## Methodology

Fixed **smoke / sanity** checklist only. High-priority critical-path checks: launch, main navigation, one happy-path action per core surface, theme toggle. No deep content review, no exploratory sessions, no BVA, no usability heuristics scoring, no WCAG audit, no cross-browser matrix.

**Stop rule:** Stop further checks only on a hard blocker that prevents navigation. No such blocker occurred.

---

## Scope (assigned critical surfaces)

1. Begin opens  
2. Open the cover  
3. Contents  
4. Lesson 1  
5. Quiz decks (one happy path)  
6. Labs (one happy path)  
7. Dashboard  
8. Theme toggle (Dim mode)

---

## Exact steps taken & results

| # | Check | Steps | Result | Evidence / landing |
|---|--------|--------|--------|---------------------|
| 1 | Begin opens | Opened `http://127.0.0.1:8765/00_CLICK_HERE_TO_BEGIN.html` | **PASS** | Heading “Atlas of the Build Loop.” URL `/00_CLICK_HERE_TO_BEGIN.html` |
| 2 | Open the cover | Clicked “Open the cover” | **PASS** | `/index.html` — heading “Atlas of the Build Loop.” |
| 3 | Contents | Clicked “Open the contents” | **PASS** | `/contents.html` — “What’s in the pack,” lesson list, practice tools |
| 4 | Lesson 1 | Opened Lesson 1 from contents | **PASS** | `/02_lessons/01_The_Loop.html` — “The Loop,” lesson body/objectives |
| 5 | Quiz decks | Opened Deck Chooser `/decks.html` → “Start selected decks” → selected one answer | **PASS** | Quiz `/03_quiz/index.html?decks=all`; feedback “CORRECT”; 1/56 answered |
| 6 | Labs | Opened labs index → opened Lab 01 | **PASS** | `/04_labs/index.html` (four labs); `/04_labs/spaced.html` — “Spaced Repetition Lab” |
| 7 | Dashboard | Navigated to dashboard | **PASS** | `/dashboard.html` — “Progress Dashboard” with quiz/lab activity UI |
| 8 | Theme toggle | Clicked “Dim mode,” then restored | **PASS** | UI went dark; control became “Bright mode”; restored to bright |

### Happy-path notes

- **Quiz:** Start selected decks → answer one item → correct feedback and progress count updated (1/56).  
- **Labs:** Labs index listed four labs; opened Spaced Repetition Lab successfully.  
- **Theme:** Dim ↔ Bright toggle visible and effective on the surface tested.

---

## Pass / fail summary

| Check | Status |
|--------|--------|
| Begin opens | PASS |
| Open the cover | PASS |
| Contents | PASS |
| Lesson 1 | PASS |
| Quiz decks (happy path) | PASS |
| Labs (happy path) | PASS |
| Dashboard | PASS |
| Theme toggle | PASS |

**Overall:** **8 / 8 PASS**

---

## Blockers

**None.** No hard blocker stopped the checklist.

---

## Residual risk (smoke-only)

Smoke does **not** cover:

- Full quiz deck coverage (56 questions) or wrong-answer / edge paths  
- All labs beyond Lab 01 (spaced); scenario/bias, term match/fermi, steelman not exercised in this pass  
- localStorage persistence across reloads (`atlas_build_loop_*_v1`) or dashboard reset behavior  
- Deep content correctness of lessons  
- Cross-browser / offline `file://` vs served-URL differences beyond this environment  
- Accessibility, usability heuristics, exploratory charters, or boundary/equivalence cases (owned by other methodology bots)

---

## Screenshots

Repo paths (copied from the 2026-09-15 smoke run):

- Begin: `docs/screenshots/2026-09-15/01-begin.png`
- Cover: `docs/screenshots/2026-09-15/02-cover.png`
- Contents: `docs/screenshots/2026-09-15/03-contents.png`
- Lesson 1: `docs/screenshots/2026-09-15/04-lesson-1.png`
- Quiz: `docs/screenshots/2026-09-15/05-quiz.png`
- Labs index: `docs/screenshots/2026-09-15/06-labs-index.png`
- Lab page: `docs/screenshots/2026-09-15/07-lab-spaced.png`
- Dashboard: `docs/screenshots/2026-09-15/08-dashboard.png`
- Dim theme: `docs/screenshots/2026-09-15/09-dim-theme.png`

---

*End of smoke & sanity report.*
