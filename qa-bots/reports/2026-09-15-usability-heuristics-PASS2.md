# Usability Heuristics Evaluation — **PASS 2** (verification)

**Evaluator:** Usability Heuristics Tester  
**Methodology:** Nielsen’s 10 usability heuristics (only)  
**Pass label:** **PASS 2** / 2026-09-15 (America/Los_Angeles)  
**Target:** Atlas of the Build Loop — Study Pack (post-fix build)  
**URL:** http://127.0.0.1:8765/00_CLICK_HERE_TO_BEGIN.html  
**Pack path:** `pack/`  
**Compared to:** Pass 1 report `qa-bots/reports/usability-heuristics-atlas-study-pack.md` (also `qa-bots/reports/2026-09-15-usability-heuristics-atlas-study-pack.md`)

---

## 1. Process / steps

1. Confirmed HTTP server `:8765` serving refreshed pack.
2. Static re-read of `decks.html`, `dashboard.html`, begin/cover, lessons (`markLesson`), `shared.js` steelman prompt, quiz shell/CSS, README/BAT, steelman chrome.
3. Live browser verification of FIX checklist (Select none, Begin/Cover Dashboard, Lesson 1 → Dashboard reads, one practice answer vs unique count, reset confirm cancel/OK + theme keep, Steelman grader domain, badges light/dim, spaced rating labels).
4. **Storage note:** Attempted Clear site data for `127.0.0.1:8765`; existing tabs may have retained prior data. Dashboard reset Cancel then OK also used. Final origin state not guaranteed pristine — noted where counts depend on uniqueness.

---

## 2. CLI FIX scorecard (explicit)

| ID | Fix intent | Score | Evidence |
|----|------------|-------|----------|
| **FIX-01** | Empty decks must not start all; show “Select at least one deck” | **FIXED** | Live: Select none → error visible; Start selected disabled; did not open 56-Q set. Code: `ids.length === 0` removes `href`, shows `#deck-error`. |
| **FIX-02** | Steelman grader Build Loop domain (no cardio) | **FIXED** | Live + code: prompt is “loops, methods, intent, brainstorming, prototyping, review, iteration, and shipping.” No cardio/physiology/bloodwork in lab grader text. |
| **FIX-03** | Quiz badge contrast light + dim | **FIXED** | Live: badges readable Bright and Dim (`THE LOOP / REMEMBER`, etc.). CSS: lesson badge dim override; quiz `.badge` / `.badge-level` use theme tokens. |
| **FIX-04** | Progress counting; unanswered exam skipped | **PARTIAL** | Live: after one practice answer, quiz `1 / 8` matched Dashboard “Unique quiz questions answered **1**” (good). Copy documents unique IDs + exam skips. **Residual:** quiz header still hardcodes “7 decks · 56 questions” even on L01-only filter (H1 status mismatch). Live also observed Start-from-chooser path briefly landing on `?decks=all` / full bank before manual filter — treat as remaining selection deep-link risk (see §4). |
| **FIX-05** | HTTP launcher / `file://` warning | **FIXED** | Static (docs): README prefers `.bat` → `http://127.0.0.1:8765/`; documents `file://` origin isolation; BAT echoes same warning. (Not a UI walk item.) |
| **FIX-06** | Lesson `markLesson` / read progress | **FIXED** | Lessons load `shared.js` and call `markLesson(...)`. Live: Dashboard “Lessons visited” showed **L01 The Loop — visited …**. |
| **FIX-07** | Reset clears progress, keeps theme; confirm matches | **FIXED** | Live confirm lists progress/weak/SRS clears and **“Keeps: theme (bright/dim)”**. Code no longer removes `atlas_build_loop_theme_v1`. Cancel then OK; theme retained. |
| **FIX-08** | Nav + Dashboard from Begin/Cover | **FIXED** | Begin: Dashboard shortcut present. Cover: Dashboard CTA in cta-row. Contents/standard surfaces: topbar. Steelman now uses shared topbar. **Residual minor:** Cover still lacks full persistent topbar (escape via CTA is enough for this fix). |
| **FIX-09** | Arc-head + Steelman dim contrast; steelman label association | **PARTIAL** | Steelman: `label for="text"`, topbar, dim readability OK live. **Still open (minor H4):** Contents arc-head images still `alt=""` while adjacent text names the arc — decorative pattern retained; a11y ownership may close fully. |
| **FIX-10** | Quiz aria-live / feedback announce / lock-copy name | **FIXED** | Static: `#quiz-status` `role="status" aria-live="polite"`; stats/weak/exam live regions; LOCK button `aria-label="Copy LOCK grader prompt"`. Live: spaced rating labels visible (related recognition). Full SR announcement depth deferred to Accessibility tester. |

**FIX-11…15:** None newly scoped beyond residuals in §4; no additional CLI IDs encountered as named fixes.

---

## 3. Pass 1 major findings — re-score

| Pass 1 major | Pass 2 status |
|--------------|---------------|
| H5 Select none → all 56 | **Fixed** (FIX-01) |
| H1 Dashboard vs quiz answer count mismatch | **Mostly fixed** (unique-ID counting matched 1↔1 in live probe); residual status-copy / chooser deep-link under FIX-04 PARTIAL |
| H1 Lesson reading never on Dashboard | **Fixed** (FIX-06) |
| H2/H4 Steelman grader wrong domain | **Fixed** (FIX-02) |
| H5/H3 Reset also cleared theme | **Fixed** (FIX-07) |
| H4 Navigation chrome inconsistent / Begin-Cover no Dashboard | **Fixed** for Dashboard reachability (FIX-08); chrome still not 100% identical across Cover vs interior (acceptable residual minor) |

---

## 4. Remaining heuristic issues (Pass 2)

### H1 Visibility of system status — **Minor (was Major, reduced)** — Quiz chrome ignores active filter

- **Evidence:** `03_quiz/index.html` subtitle hardcoded: “7 decks · 56 questions · …”. Exploratory + live: L01-only still shows that banner.
- **Impact:** Learner may think they are in the full exam when filtered.
- **Rec:** Bind subtitle to filtered bank size / selected deck names.

### H5 / H4 — **Minor / investigate** — Chooser → quiz deep-link inconsistency (observed once)

- **Evidence:** Live Pass 2 walk reported selecting L01 then Start yielding `?decks=all` / full bank until manual filter. Code path for single selection should emit `decks=bl-01-loop`.
- **Impact:** If reproducible, undoes intent of deck chooser (error prevention / consistency).
- **Rec:** Reproduce with hard refresh; ensure `sync()` before navigation; add regression check that single checked box never writes `all`.

### H4 — **Minor** — Contents arc-head empty `alt=""`

- Adjacent arc titles mitigate; still inconsistent with cover arc images that have descriptive alts.

### H6 — **Cosmetic/Minor** — Brand “the Build Loop” vs full product title (unchanged)

### H1/H2 — **Minor** — Lab progress bars still `actions * 5` (improved copy on lab ratings helps)

---

## 5. Positive findings (Pass 2)

1. Empty-deck guard is clear and blocks the prior dangerous path (H5).
2. Dashboard now explains counting rules and lesson visits (H1).
3. Reset confirm text matches actual wipe set and preserves theme (H3/H5).
4. Steelman tutor prompt matches pack domain (H2).
5. Begin/Cover can reach Dashboard without memorizing interior nav (H7/H4).
6. Practice feedback + unique progress remain strong (H1).
7. Spaced ratings include consequence hint copy (H6) — improvement vs Pass 1 minor.

---

## 6. Results summary

| Severity | Pass 1 | Pass 2 remaining |
|----------|-------:|-----------------:|
| Critical | 0 | 0 |
| Major | 6 | **0** (all prior majors fixed or reduced) |
| Minor | 7 | ~4 residuals (subtitle, deep-link investigate, arc alt, brand/bars) |
| Cosmetic | 0 | 1 |

**FIX rollup:** FIXED 01, 02, 03, 05, 06, 07, 08, 10 · PARTIAL 04, 09 · none STILL OPEN as named majors.

**Overall:** Post-fix pack resolves the Pass 1 usability majors that mattered most (empty decks, theme wipe, steelman domain, lesson progress, Dashboard from begin/cover). Remaining work is status-copy fidelity on the quiz and confirming chooser deep-links always match selection.

---

## 7. Live evidence paths

- Empty decks: `(session browser shots)/shot-call_iHTAbRJb0ESUvY47ny3eM3FPfc_06ca6a0ca9c4c60d.png`
- Quiz 1/8: `(session browser shots)/shot-call_SphwsejeRJlpH2HxbXO7d2ckfc_06ca6a0ca9c4c60d.png`
- Dim badges: `(session browser shots)/shot-call_GiUsu1tWr2HoqLoh24IBHewMfc_06ca6a0ca9c4c60d.png`
- Steelman prompt: `(session browser shots)/shot-call_WH47YqybhfiqXOuDPCmn0yb3fc_06ca6a0ca9c4c60d.png`
- Spaced ratings: `(session browser shots)/shot-call_3DGE9W0rwJzRiNrOS6B36MrCfc_06ca6a0ca9c4c60d.png`
- Reset dialog: `(agent assets)/agent-data/agents/71554938-c737-48e2-8437-3f8f7a7361d6/assets/796c38ee757cd883d4ee4e1f6a0f6fff267331c897b4b50d2ebf33da4e61ffcc.webp`

---

## 8. Scope note

Nielsen heuristics only. No smoke / SBTM / BVA / WCAG claims beyond noting overlap for Lead rollup.
