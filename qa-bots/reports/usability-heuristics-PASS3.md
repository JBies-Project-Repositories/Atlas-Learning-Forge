# Usability Heuristics Evaluation — **PASS 3** (16-lesson field atlas)

**Evaluator:** Usability Heuristics Tester  
**Methodology:** Nielsen’s 10 usability heuristics (only)  
**Pass label:** **PASS 3** / 2026-09-15 (America/Los_Angeles)  
**Target:** Atlas of the Build Loop — Study Pack (**16-lesson field atlas**)  
**URL:** http://127.0.0.1:8765/ (Contents: `contents.html`)  
**Pack path:** `/workspace/atlas-study-pack/pack/`  
**Compared to:** Pass 2 `/workspace/qa-reports/pass-2/usability-heuristics-PASS2.md`  
**Brief focus:** (1) Contents reads as an atlas, not seven cards; (2) facilitation scripts scannable; (3) arc heads readable in light and dim.  
**Rules followed:** No invented findings; no re-open of Pass 1/2 P0s without reproduced regression.

---

## 1. Process / steps

1. Confirmed HTTP `:8765` serving pack; verified **16** lesson HTML files under `02_lessons/` and **16** deck checkboxes on `decks.html` (`bl-a1-diverge` … `bl-d4-launch`).
2. Confirmed live UI stems are **not** the old 7-lesson IDs (`01_The_Loop` / `bl-01-loop` appear only under `01_source/INTEGRITY_REPORT.md`, allowed by brief).
3. Static read of `contents.html`, `assets/pack.css` (`.arc-head`), and all 16 facilitation sections.
4. Live browser walk: Contents atlas layout; Dim mode Contents arc-heads; Lesson 09 facilitation script (minute list) in dim.
5. Contrast math for arc-head label color `#fff6d6` on `--nav-bg` `#1c5d68` (same token in bright and dim).

---

## 2. Focus scorecard

| Focus | Heuristic lens | Score | Summary |
|-------|----------------|-------|---------|
| **Contents = atlas (not seven cards)** | H2 Match to real world; H4 Consistency; H8 Aesthetic & minimal design | **PASS** | Page is explicitly an atlas: H1 “Four arc-packs,” lead “sixteen lessons in four mini-packs,” suggested path Arc A–D, 16 lesson cards under four arc-heads, Practice tools separate. Cover copy matches (“four arc-packs (sixteen lessons)”). |
| **Scripts scannable** | H6 Recognition over recall; H8 Aesthetic & minimal design | **PASS with minor consistency note** | Every lesson has a named Facilitation block. Best scan: Arc C (+ L04) timed `<ul>` lists; Arc D clock `<table>`s. Arc A/B mostly bold time bands inside `<p>` — still timed and bolded, denser to scan than list/table siblings. |
| **Arc heads readable light/dim** | H1 Visibility; H4 Consistency (theme) | **PASS** | Cream label on teal bar; computed contrast ≈ **6.89:1**. Live: bright Contents shot + dim Contents Arc B head both readable. `--nav-bg` unchanged across themes. |

**Critical / Major (new):** **0**  
**Do not re-open:** Prior Pass 1 majors remain closed from Pass 2; no regression of empty-deck / theme-wipe / steelman-domain / lesson-visit majors observed in this scoped pass.

---

## 3. Findings (evidence-backed only)

### F3-1 — Contents atlas information architecture — **Positive / PASS**

- **Evidence (static):** `contents.html` lead: “This page is the atlas: sixteen lessons in four mini-packs…”; Suggested path lists Arc A (L01–L04) … Arc D (L13–L16); four `.arc-head` blocks × four `.card.lesson` links (16 total); Practice tools grid separate from lessons.
- **Evidence (live / shot):** `/workspace/qa-reports/pass-3/evidence/contents-atlas-bright.png` (also pack `docs/screenshots/2026-09-15/pass-3/03-contents-16-lessons.png`) — four arc sections, lesson cards with short one-line descriptors, not a seven-card primer map.
- **Heuristic:** H2 / H8 — map language and arc grouping match “field atlas” mental model.

### F3-2 — Facilitation scripts scannable — **Positive, with Minor consistency**

- **Evidence (structure audit of all 16 lessons):**
  - **List (highly scannable):** L04, L09, L10, L11, L12 — timed `<li>` bands.
  - **Table (highly scannable):** L13–L16 — Clock / Move tables (e.g. L13 `Facilitation: a 35-minute critique agenda`).
  - **Timed bold paragraphs (scannable but denser):** L01–L03, L05–L08 — e.g. L01 “**0:00–2:00 — Wall…**” through successive `<p>` blocks; L05 same pattern.
- **Evidence (live):** Dim Lesson 09 minute list — `/workspace/qa-reports/pass-3/evidence/l09-facilitation-minute-list-dim.png` — “Minute-by-minute” with bold `0:00–0:05` … `0:37–0:40` steps.
- **Heuristic:** H6 / H8 — facilitators can recover the clock without reading the whole lesson body on Arc C/D and L04; Arc A/B scripts work via bold times but lack shared list/table chrome.
- **Severity:** **Minor** (consistency of script *form*, not missing scripts).
- **Rec (optional polish):** Prefer one shared pattern (timed list or clock table) for Facilitation blocks in L01–L03 and L05–L08 so room runners get the same scan affordance everywhere.

### F3-3 — Arc-head labels light + dim — **PASS**

- **Evidence (CSS):** `.arc-head { background: var(--nav-bg); }` with `--nav-bg: #1c5d68` in `:root` and `html[data-theme="dim"]`; `.arc-head .arc { color: #fff6d6; … text-transform: uppercase; }`.
- **Evidence (contrast):** `#fff6d6` on `#1c5d68` ≈ **6.89:1** (exceeds WCAG AA for large/UI text; treated here as heuristic readability, not a WCAG audit).
- **Evidence (live):** Dim Contents showing Arc B bar “ARC B — METHODS AND INTENT · FOUR LESSONS” readable — `/workspace/qa-reports/pass-3/evidence/contents-arc-b-dim.png`. Bright full Contents — `evidence/contents-atlas-bright.png`.
- **Heuristic:** H1 — arc grouping remains visible when theme flips.

### F3-4 — Arc-head decorative `alt=""` — **Still open Minor (Pass 2 residual; not escalated)**

- **Evidence:** `contents.html` still uses `<img … alt="" />` on all four arc-heads; adjacent `.arc` text names the arc.
- **Note:** Same as Pass 2 FIX-09 residual (minor H4). **Not** re-opened as P0; no regression of contrast/readability. A11y ownership may close fully.

---

## 4. Spot checks vs Pass 2 residuals (no P0 reopen)

| Pass 2 residual | Pass 3 observation (scoped) |
|-----------------|------------------------------|
| Quiz subtitle hardcoded “7 decks · 56 questions” | **Appears addressed in code:** `#quiz-subtitle` starts as “Loading decks…”; `03_quiz/app.js` builds `"N decks · N questions…"`. Live shot showed “16 decks · 128 questions”. Not a full FIX-04 retest. |
| Chooser → `decks=all` deep-link | **Not retested** this pass (outside focus; no accidental reproduction). |
| Arc-head `alt=""` | Still present — Minor only (F3-4). |

No Pass 1/2 **critical/major** regressions reproduced.

---

## 5. Positive findings (Pass 3)

1. Contents is clearly a **16-lesson / four-arc atlas**, not a seven-card primer TOC (F3-1).
2. Cover and Contents copy agree on four arc-packs and sixteen lessons (H4).
3. Arc-head chrome keeps readable labels in **bright and dim** with stable teal bar (F3-3).
4. Facilitation scripts exist in **all 16** lessons; Arc C minute lists and Arc D clock tables are strong recognition affordances for live facilitation (F3-2).
5. Deck IDs and quiz bank size align with the 16×8 atlas (`bl-a1-diverge` … `bl-d4-launch`; subtitle path dynamic).

---

## 6. Results summary

| Severity | Count (new this pass) |
|----------|----------------------:|
| Critical | 0 |
| Major | 0 |
| Minor | 1 new consistency note (script form L01–03 / L05–08) + 1 carried residual (`alt=""`) |
| Cosmetic | 0 |

**Focus rollup:** Atlas **PASS** · Scripts **PASS** (minor form consistency) · Arc heads light/dim **PASS**.

**Overall:** The 16-lesson field atlas meets the Pass 3 usability focus. Contents reads as a map of four mini-packs; facilitation scripts are present and generally scannable (best on Arc C/D); arc heads remain readable when Dim mode is on. No new majors; no P0 reopen.

---

## 7. Evidence paths

- Contents bright (atlas): `/workspace/qa-reports/pass-3/evidence/contents-atlas-bright.png`
- Contents dim Arc B head: `/workspace/qa-reports/pass-3/evidence/contents-arc-b-dim.png`
- L09 facilitation (dim): `/workspace/qa-reports/pass-3/evidence/l09-facilitation-minute-list-dim.png`
- L09 script header (dim): `/workspace/qa-reports/pass-3/evidence/l09-facilitation-script-header-dim.png`
- Pack shots (shared): `/workspace/atlas-study-pack/pack/docs/screenshots/2026-09-15/pass-3/`

---

## 8. Scope note

Nielsen heuristics only. No smoke / SBTM / BVA / WCAG claims beyond noting contrast math as readability support for F3-3. Full report path for Lead ingest: this file.

### Live confirm (post-file)
- Bright Contents: `evidence/contents-bright-live-confirm.png`
- Dim Contents: `evidence/contents-dim-live-confirm.png`
- L09 minute list: `evidence/l09-facilitation-minute-list-live-confirm.png`
- Confirms: 16 lessons / 4 arcs; arc labels readable bright+dim.
