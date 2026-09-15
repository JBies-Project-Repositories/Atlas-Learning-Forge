# Performance Observation Report — Atlas of the Build Loop Study Pack

**Observer:** Performance Observation Tester  
**Report to:** QA/Tester Lead  
**Date:** 2026-09-15 (PT)  
**App:** Atlas of the Build Loop — Study Pack (offline HTML field guide)  
**Test URL:** http://127.0.0.1:8765/00_CLICK_HERE_TO_BEGIN.html  

---

## 1. Methodology / scope

Lightweight **perceived-performance observation** only:

- Walk primary surfaces once and note load feel, responsiveness, obvious jank, slow navigations, and resource-heavy interactions.
- Record approximate timings and environment notes when possible.
- **Out of scope:** load tools, concurrent stress, DoS-style traffic, exploit testing, and other QA methodologies.

**Environment**

| Item | Value |
|------|--------|
| Server | Local HTTP on `127.0.0.1:8765` |
| Browser | Chrome (box desktop) |
| Viewport | ~1280×800 |
| Auth | None |
| Comparison baseline | None provided by Lead |

Supporting measurements: single-request `curl` timings and on-disk asset sizes (not a substitute for perceived UX; used only to ground bottleneck suspicion).

---

## 2. Flows observed

| # | Surface | Path / notes |
|---|---------|----------------|
| 1 | Begin | `00_CLICK_HERE_TO_BEGIN.html` → click-through to cover |
| 2 | Cover / home | `index.html` (hero imagery) |
| 3 | Contents | `contents.html` |
| 4 | Lessons | Lessons 1–3 HTML (sample of 7) |
| 5 | Quiz | Chooser + 56-question app; sampled 3 answers + scoring UI |
| 6 | Labs | SRS (`spaced`), Scenario/bias, Term match/fermi, Steelman |
| 7 | Dashboard | `dashboard.html` + localStorage-backed progress |
| 8 | Theme toggle | Bright → Dim → Bright |

Not exercised: remaining lessons 4–7 full read-through, full 56-question quiz completion, every lab variation.

---

## 3. Timing and UX performance notes

### Perceived (browser walk)

| Flow | Perceived feel | Notes |
|------|----------------|-------|
| Begin → cover | Instant (<0.5s) | No blank period or flash on click-through |
| Cover / home | Instant | Hero imagery and layout painted cleanly |
| Contents | Instant | Image + lesson list; no jank |
| Lessons 1–3 | Instant each | Long pages + hero assets; normal scroll, no stutter |
| Quiz (56 Q) | Instant open; UI immediate | Chooser and quiz page opened instantly; answer feedback, scroll, and scoring responded immediately on 3 sampled questions |
| Lab — SRS | Instant | Lesson select, reveal, Good rating; counters updated immediately |
| Lab — Scenario Audit | Instant | Selection, text entry, answer reveal |
| Lab — Term Match | Instant | Pair match; highlight/counter update without jank |
| Lab — Steelman | Instant | Text entry, five rubric checks, 5/5 score |
| Dashboard | Instant | Progress shown correctly (4 quiz answers, 4 lab actions; per-lab visit/action summaries) |
| Theme toggle | Instant | Bright ↔ Dim; no white flash, layout shift, or stutter |

**Overall UX:** No slow navigations or obvious jank observed on localhost in this session.

### Supporting HTTP timings (single GET, localhost)

All HTML/JS/CSS fetches returned **200** with **total time ≈ 0.5–1.1 ms** on this host (TTFB similarly sub-millisecond). Example:

- Begin / index / contents / dashboard / decks: ~0.6–1.1 ms total  
- Lesson HTML (~13–19 KB): ~0.6–0.9 ms  
- Quiz `questions.js` (~48 KB), `app.js` (~22 KB): ~0.6–1.0 ms  
- Lab HTML (~12–31 KB): ~0.5–0.9 ms  
- Images (`cover.jpg` ~275 KB; `arc-*.jpg` ~300–381 KB): still ~0.7–1.1 ms total on localhost (network not a factor here)

---

## 4. Bottlenecks suspected

None manifested as user-visible delay on localhost. Relative weight still worth watching on slower devices or non-local hosting:

1. **Quiz DOM/JS surface** — 56 questions with radio controls + `questions.js` (~48 KB) + `app.js` (~22 KB); largest interactive surface; sampled interactions stayed instant.
2. **Lesson pages + large JPEGs** — lesson HTML ~13–19 KB plus hero/arc images ~275–381 KB each; fine on localhost; most likely first-paint cost off-box or on constrained networks.
3. **Lab pages** — fermi/spaced ~29–31 KB HTML; interactions remained instant.
4. **localStorage dashboard updates** and **theme CSS repaint** — observed as negligible.

---

## 5. Comparison expectations

None were given by QA/Tester Lead. No before/after or competitor baseline applied.

---

## 6. Residual performance risk

| Risk | Likelihood (this env) | Notes |
|------|----------------------|--------|
| Slow first paint when pack is served remotely or from `file://` with large images | Medium off-localhost | Image weight is the main transferable concern |
| Quiz scroll/input lag on low-end devices with full 56-Q DOM | Low–medium | Not seen on this Chrome/desktop pass |
| Theme FOUC / flash on slower CSS apply | Low | Not observed (Bright ↔ Dim clean) |
| localStorage growth / dashboard lag after heavy use | Low | Small progress set looked instant |
| Lesson scroll jank with multiple large images | Low on this machine | Clean on lessons 1–3 |

**Residual risk summary:** On the assigned localhost setup, perceived performance is **strong** with **no blocking findings**. Residual risk is mainly **off-environment** (remote/slow network, low-end hardware, full quiz completion) rather than defects observed here.

---

## 7. Constraints / what was not done

- No load, soak, or denial-of-service testing  
- No DevTools Performance/Lighthouse trace export  
- Did not complete all 56 quiz questions or all lesson/lab variants  
- Did not inspect precise `atlas_build_loop_*_v1` key payloads beyond UI confirmation on dashboard  

---

*End of performance observation report.*
