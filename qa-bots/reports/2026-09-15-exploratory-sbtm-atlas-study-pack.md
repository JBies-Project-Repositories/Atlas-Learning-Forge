# SBTM Session Report — Atlas of the Build Loop (Study Pack)

**Tester:** Exploratory Session Tester  
**Date:** 15 Sep 2026, ~2:37–2:41 PM PT (plus short debrief)  
**Build / target:** Atlas of the Build Loop — Study Pack (offline HTML field guide)  
**Entry URL:** `http://127.0.0.1:8765/00_CLICK_HERE_TO_BEGIN.html`  
**Methodology:** Session-based exploratory testing (SBTM) only.

---

## Charter

Discover how a first-time learner navigates from begin to a lesson, a quiz item, a lab, and progress.

## Time box

**Assigned:** 45 minutes.  
**Used:** ~20 minutes of live exploration + ~10 minutes debrief of notes, screenshots, and progress keys. Charter completed early; remaining box used to log surprises rather than widen into other methodologies.

## Environment notes

- No login. Educational pack. Progress keys: `atlas_build_loop_*_v1` in `localStorage`.
- Shared test origin `http://127.0.0.1:8765` was already serving (HTTP 200). Other QA squad testers were assigned the same URL at the same time, so this browser’s `localStorage` may not have been a clean first-run.
- Theme at session end restored to Bright.

---

## Heuristics / tours used

| Heuristic | How it showed up |
| --- | --- |
| **Happy-path / first-time learner** | Followed the largest, most obvious labels a new learner would click. |
| **Landmark tour** | Used Cover, Quiz, Labs, Dashboard once each after arriving at Lesson 1. |
| **Questioning** | Asked why the first quiz item was not Lesson 1, why dashboard quiz count was 2 after one visible attempt, and what counts as a lab action. |
| **FedEx / packing tour (light)** | Noted what is advertised on begin vs what is missing (no Dashboard on begin). |

Did **not** run a contents-first path, exam-mode quiz, lab rating buttons, or dashboard reset during this box.

---

## Areas covered

| Surface | Result for a first-time learner |
| --- | --- |
| Begin (`00_CLICK_HERE_TO_BEGIN.html`) | Clear start. Primary CTA **Open the cover**. Secondary tiles: Contents, Lesson 1, Quiz decks (56 questions), Labs. Dim mode control present. No Dashboard link. |
| Cover (`index.html`) | Long editorial cover. No top nav. Learner must scroll to **Open the contents** / **Begin Lesson 1**. Dim was on when we arrived (possibly leftover theme). |
| Lesson 1 (`02_lessons/01_The_Loop.html`) | Arrived. Title **The Loop**, learning objectives, lesson nav (Cover / Contents / Quiz / Labs / Dashboard / Next). |
| Contents | **Not visited** this session (shortcut from begin/cover can skip the map). |
| Deck chooser (`decks.html`) | All seven lesson decks pre-checked. **Start selected decks** opened `03_quiz/index.html?decks=all`. |
| Quiz (practice, all 56) | Question 1 of 56 was **Prototyping**: “When do you climb fidelity?” Chose “When the cheaper rung cannot kill the assumption.” Instant **CORRECT** feedback. Q2 visible: Iteration and Shipping. |
| Labs index | Four labs listed; opened Spaced Repetition. |
| SRS lab (`04_labs/spaced.html?decks=bl-01-loop`) | Lesson L01 — The Loop (18 cards). Showed answer for “Divergent thinking.” Rating buttons (Again / Hard / Good / Easy) appeared. Did not rate. Reviews this session stayed **0**. |
| Dashboard | Filled: **2** quiz answers recorded (last 2:38:54 PM PT); **0** lab actions (last 2:39:15 PM PT); Spaced Repetition visits **1**, actions **0**. |
| Theme | Dim / Bright toggled and worked across pages. Restored to Bright. |

### Path taken (order)

1. `00_CLICK_HERE_TO_BEGIN.html`
2. `index.html` (cover)
3. `02_lessons/01_The_Loop.html` (Lesson 1)
4. `decks.html`
5. `03_quiz/index.html?decks=all`
6. `04_labs/index.html`
7. `04_labs/spaced.html?decks=bl-01-loop`
8. `dashboard.html`

---

## Session notes (what a first-timer actually experiences)

- **Begin is a strong front door.** One obvious primary action, plus four shortcuts. A learner who wants “just start reading” can jump to Lesson 1 without the cover or contents.
- **Cover feels like a book front, not an app shell.** No header landmarks. If the learner does not scroll, the next-step CTAs are easy to miss. Dim mode on arrival made it feel already “in progress” rather than a fresh book.
- **Lesson 1 is reassuring.** Title, badge (“educational only”), objectives, and a Next link. This is the first page that *looks* like a course.
- **Quiz default is the whole exam, shuffled.** After Lesson 1, the obvious “Quiz” path still starts all 56 items. The first item was from Prototyping (Lesson 5), not The Loop. Instant feedback worked and felt good.
- **Lab reveal ≠ credit.** Showing the card back is the natural first click. Dashboard still showed 0 lab actions. Copy on the lab (“due until you rate it”) is the only hint that rating is the real move.
- **Progress is browser-local and already noisy.** Dashboard copy says “this browser only.” Counts did not match the one visible quiz answer in this session.

---

## Findings (severity)

### F1 — First quiz item is not from the lesson just read (Minor)

**Evidence:** After Lesson 1, started selected decks (all seven checked by default). Q1 tagged **PROTOTYPING**, Q2 tagged **ITERATION AND SHIPPING**. Screenshot `04-quiz.png`.

**Why it matters:** A first-time learner who just finished The Loop reasonably expects Loop items first. Shuffle is real (quiz app shuffles on start) but is not explained on the first card. Feels like “I opened the wrong test.”

**Repro:** Begin → Lesson 1 → Quiz → leave all decks checked → Start selected decks. Observe lesson tags on Q1.

### F2 — Dashboard quiz count did not match the one visible attempt (Minor / suspected contamination)

**Evidence:** One practice answer was given in this session. Dashboard showed **Quiz answers recorded: 2**, last 2:38:54 PM PT. Screenshot `06-dashboard.png`.

**Why it matters:** A learner cannot tell whether they finished one item or two. On this shared origin, other testers were live at the same time; `atlas_build_loop_progress_v1` is origin-scoped. Could be prior answers, a double increment, or another session writing the same key.

**Repro needed:** Clean `localStorage` (or private window), answer exactly one item, reload dashboard. Not done in this box (would have wrecked parallel testers).

### F3 — Revealing a lab card does not count as a lab action (Nit / copy gap)

**Evidence:** Showed the SRS answer for “Divergent thinking.” Reviews this session stayed 0. Dashboard: Lab actions **0**, Spaced Repetition visits 1 / actions 0. Last lab timestamp still updated (visit). Screenshots `05-srs-lab.png`, `06-dashboard.png`.

**Why it matters:** The obvious first interaction (Show answer) produces no progress. Rating (Again/Hard/Good/Easy) is what increments actions. The dashboard “Lab actions · Last: …” line also updates on visit, which reads as if an action happened.

**Repro:** Open SRS, pick L01, click Show answer, do not rate, open Dashboard.

### F4 — Begin page offers no path to progress (Nit)

**Evidence:** Begin tiles are Cover, Contents, Lesson 1, Quiz decks, Labs. Dashboard is absent until later nav (lesson/quiz/labs headers).

**Why it matters:** A first-timer who wants “did I start?” has to discover Dashboard from an inner page.

### F5 — Cover has no persistent nav (Nit / first-time friction)

**Evidence:** Cover screenshot `02-cover.png` — theme control only in the top bar. Next steps are below the fold after long prose.

**Why it matters:** Book metaphor is intentional, but a learner hunting for Quiz/Labs/Dashboard from the cover has to scroll or go back to Begin.

No blockers. No broken links on the charter path. Theme toggle worked.

---

## Positive findings

- Begin CTA is unmistakable; fallback copy for “if a link does nothing” is present.
- Lesson 1 loads with clear title, objectives, and working top nav including Next.
- Quiz practice mode gives immediate, specific feedback (“That matches this lesson.”).
- SRS lab states “Progress stays in this browser” and presents a full L01 deck (18 cards) with due/count stats.
- Dashboard copy is honest that storage is this-browser-only and lists labs by name.
- Dim/Bright survived navigation across pages.

---

## Open questions

1. Is all-decks + shuffle the intended default for a learner coming from Lesson 1, or should “Start selected” default to L01 after that lesson?
2. What exactly should increment **Lab actions** — rate only, or also reveal / visit? Should “Last” on Lab actions stay blank until an action?
3. Does dashboard `quiz.answered` increment once per choice, including re-clicks / re-renders, and is it safe on a shared origin?
4. Should Begin include Dashboard so progress is a first-class landmark?
5. Was Dim mode on the cover leftover from this tester or from another squad member on `127.0.0.1:8765`?

---

## Ideas / suggested follow-up charters

1. **Clean-state progress.** Private window: empty keys → one quiz answer → one SRS rating → dashboard numbers and Reset Atlas progress.
2. **Lesson-aligned quiz.** From Lesson 1, choose only L01 (or Select none then L01) vs Select all vs All 56 exam path; exam mode + timer.
3. **Lab action contract.** Rate vs reveal vs visit on all four labs (SRS, Scenario Audit, Term Match, Steelman); confirm what Dashboard “best” means.
4. **Contents-first learner.** Begin → Contents suggested path (L1–2 → SRS) vs shortcut-to-Lesson-1; see who misses the map.
5. **Theme + file://.** Persistence after reload; Dim on `file://` vs `http://127.0.0.1:8765`.
6. **Cover wayfinding.** Can a first-timer reach Quiz/Labs/Dashboard without scrolling the cover or returning to Begin?

---

## Bugs / issues summary

| ID | Sev | Title |
| --- | --- | --- |
| F1 | Minor | Default all-decks quiz opens on a non-L01 shuffled item with no shuffle explanation |
| F2 | Minor (suspected) | Dashboard quiz count 2 after one visible answer (shared-origin / increment question) |
| F3 | Nit | Show answer does not increment lab actions; “Last” still stamps on visit |
| F4 | Nit | Begin has no Dashboard landmark |
| F5 | Nit | Cover has no persistent nav; next steps below the fold |

**Blockers that stop further testing:** none.  
**Charter status:** Satisfied (begin → lesson → quiz item → lab → progress).

---

## Evidence

Repo paths (copied from the 2026-09-15 SBTM session):

- `docs/screenshots/2026-09-15/exploratory-sbtm/01-begin.png` — begin page, Bright, Open the cover
- `docs/screenshots/2026-09-15/exploratory-sbtm/02-cover.png` — cover in Dim, no header nav
- `docs/screenshots/2026-09-15/exploratory-sbtm/03-lesson1.png` — The Loop + objectives + nav
- `docs/screenshots/2026-09-15/exploratory-sbtm/04-quiz.png` — Q1 Prototyping marked correct; Q2 Iteration and Shipping
- `docs/screenshots/2026-09-15/exploratory-sbtm/05-srs-lab.png` — L01 18 cards, answer revealed, 0 reviews this session
- `docs/screenshots/2026-09-15/exploratory-sbtm/06-dashboard.png` — 2 quiz answers, 0 lab actions, SRS visits 1

