# Performance Observation Report — **PASS 2** / 2026-09-15

**Observer:** Performance Observation Tester  
**Report to:** QA/Tester Lead  
**Pass label:** **PASS 2** / 2026-09-15 (America/Los_Angeles)  
**App:** Atlas of the Build Loop — Study Pack (post-fix / UPDATED build)  
**Test URL:** http://127.0.0.1:8765/00_CLICK_HERE_TO_BEGIN.html  
**Pack path:** `pack/`  
**Compared to:** Pass 1 — `qa-bots/reports/performance-observation-atlas-study-pack.md`

---

## 1. Methodology / scope

Lightweight **perceived-performance re-observation** only on the post-fix pack:

- Walk primary surfaces once; note load feel, responsiveness, jank, slow navigations, resource-heavy interactions.
- Note any change vs Pass 1.
- Score FIX items **only if performance-relevant** (otherwise N/A).
- **Out of scope:** load tools, concurrent stress, DoS-style traffic, other QA methodologies.

**Environment**

| Item | Value |
|------|--------|
| Server | Local HTTP `127.0.0.1:8765` |
| Browser | Chrome (box desktop) |
| Viewport | ~1280×800 |
| Auth | None |
| Comparison | Pass 1 localhost observation (all surfaces instant; residual = large JPEGs / full quiz DOM off-localhost) |

Supporting measurements: single-request `curl` timings and on-disk asset sizes (ground bottleneck suspicion only).

---

## 2. Flows observed

| # | Surface | Notes |
|---|---------|--------|
| 1 | Begin → cover | Click-through; Dashboard CTA on cover |
| 2 | Contents | Image + lesson list |
| 3 | Lessons | Lesson 1 + Lesson 2 (visit/mark progress) |
| 4 | Deck chooser | Select none; then start Lesson 1 deck |
| 5 | Quiz | Full bank present; 3 practice answers + feedback/lock/score UI |
| 6 | Labs | SRS (spaced), Scenario Audit (bias), Steelman |
| 7 | Dashboard | Load; theme Bright ↔ Dim; Reset Cancel then Confirm |
| 8 | Theme | Bright → Dim → Bright |

**Not observed:** Fermi lab; off-localhost / remote network; full 56-Q completion; load/stress.

---

## 3. Timing and UX performance notes

### Perceived (browser walk)

| Flow | Perceived feel | Notes |
|------|----------------|-------|
| Begin → cover/home | Instant | No flash or jank; Dashboard CTA present |
| Contents | Under ~0.5s | Image and layout stable |
| Lessons 1–2 | Under ~0.5s each | Scroll smooth; automatic visit progress felt light |
| Deck chooser | Instant | Select none immediately cleared selections / removed start option (no navigation). Start Lesson 1 deck instant |
| Quiz | Instant open; UI immediate | Full 56-Q dataset present; 3 practice answers → immediate feedback, score, badges, answer-lock |
| Lab — SRS | Instant | Reveal / rating |
| Lab — Scenario Audit | Instant | Typing / reveal |
| Lab — Steelman | Instant | Typing / checks / scoring |
| Dashboard | Instant | Load immediate |
| Theme toggle | Instant | Bright ↔ Dim |
| Reset dialog | Instant | Native confirm appeared immediately; Cancel and Confirm completed without lag; progress reset to zero |

**Overall UX:** No persistent blank periods, layout flashes, stutter, or slow interactions. One blank-looking frame occurred only during an automated jump to a lesson footer and resolved immediately (automation artifact, not product lag).

**Vs Pass 1:** **No noticeable regression.** Same strong localhost perceived performance.

### Supporting HTTP timings (single GET, localhost, post-fix)

All sampled fetches **200**, total ≈ **0.5–1.4 ms**. Notable sizes unchanged in character from Pass 1:

- HTML shells (begin/index/contents/dashboard/decks): ~3–6 KB, sub-ms  
- Lesson 1 HTML ~19.6 KB; quiz `questions.js` ~48 KB; `app.js` ~23 KB; `styles.css` ~9 KB  
- Lab HTML ~12–31 KB; `shared.js` ~12 KB  
- Images still dominant: `cover.jpg` ~275 KB; `arc-*.jpg` ~300–381 KB (localhost transfer still ~1 ms)

Post-fix JS/CSS grew slightly vs Pass 1 (expected from FIX work); **not user-visible** on localhost.

---

## 4. Bottlenecks suspected

Same as Pass 1; still **not manifested** on localhost:

1. **Large JPEGs** (~275–381 KB) — main transferable first-paint risk off-box / slow network  
2. **Quiz full DOM/JS** — 56-Q bank + radios; still instant locally after fixes  
3. **localStorage / theme / reset** — observed as negligible (including native reset confirm)

---

## 5. FIX scorecard (performance-relevant only)

| ID | Performance relevance | Score | Notes |
|----|----------------------|-------|-------|
| FIX-01 Empty deck guard | Interaction cost of validation UI | **N/A (no perf issue)** | Select none responded immediately; no delay |
| FIX-02 Steelman prompt domain | Content only | **N/A** | |
| FIX-03 Quiz badge contrast | CSS/paint | **N/A (no perf issue)** | Badge updates felt instant with answers |
| FIX-04 Progress counting | localStorage / dashboard | **N/A (no perf issue)** | Dashboard/reset updates immediate |
| FIX-05 HTTP / file:// docs | Launch docs | **N/A** | |
| FIX-06 Lesson markLesson | Extra JS on lesson load | **N/A (no perf issue)** | Visit progress felt light |
| FIX-07 Reset keeps theme | Dialog + storage clears | **N/A (no perf issue)** | Cancel/Confirm instant |
| FIX-08 Nav + Dashboard CTAs | Extra links | **N/A (no perf issue)** | Cover Dashboard CTA; no lag |
| FIX-09…15 | Mostly a11y/copy | **N/A** | No perf-relevant scoring |

---

## 6. Comparison expectations

Pass 1 baseline: instant localhost; residual = remote images / low-end full quiz DOM.  
**Pass 2 result:** Matches Pass 1; **no performance regressions** attributed to the CLI fix set.

---

## 7. Residual performance risk

| Risk | Likelihood (this env) | Change vs Pass 1 |
|------|----------------------|------------------|
| Slow first paint remotely / constrained network (large JPEGs) | Medium off-localhost | Unchanged |
| Quiz scroll/input lag on low-end with full 56-Q DOM | Low–medium | Unchanged (still fine on this Chrome/desktop) |
| Theme / reset / localStorage lag after heavier use | Low | Unchanged; reset path re-checked clean |
| Slightly larger post-fix JS/CSS | Negligible on localhost | New but not user-visible here |

**Residual risk summary:** Perceived performance remains **strong** on the assigned localhost setup with **no blocking findings** and **no Pass 2 regression**. Residual risk is still mainly **off-environment**.

---

## 8. Constraints / what was not done

- No load, soak, or DoS testing  
- No Lighthouse / DevTools trace export  
- Fermi lab not opened this pass  
- Did not complete all 56 quiz questions or all lesson/lab variants  
- Off-localhost / `file://` performance not re-measured  

---

*End of PASS 2 performance observation report.*
