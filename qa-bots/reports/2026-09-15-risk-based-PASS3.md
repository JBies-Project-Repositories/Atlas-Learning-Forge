# Risk-Based Testing Report — PASS 3 — Atlas of the Build Loop Study Pack (16-lesson)

| Field | Value |
| --- | --- |
| **Label** | **PASS 3** / 2026-09-15 |
| **Date** | 2026-09-15 PT |
| **Target** | Atlas of the Build Loop — Study Pack (**16-lesson field atlas**, not the old 7-lesson primer) |
| **Methodology** | Risk-based testing only (identify → Impact×Likelihood → prioritize → test highest risks first; no checklist QA) |
| **Environment** | `http://127.0.0.1:8765/` (HTTP 200 on entry); pack `/workspace/atlas-study-pack/pack/` |
| **Entry** | `http://127.0.0.1:8765/00_CLICK_HERE_TO_BEGIN.html` |
| **Brief** | `/workspace/qa-reports/pass-3/PASS3_BRIEF.md` |
| **Prior context (7-lesson era)** | Pass 1 `/workspace/qa-reports/risk-based-atlas-study-pack.md`; Pass 2 `/workspace/qa-reports/pass-2/risk-based-PASS2.md` — used for regression awareness only |
| **Tools** | Shell, Read, curl, node (source + HTTP); headed browser shots for confirmation (no invented scores) |
| **Evidence folder** | `/workspace/qa-reports/pass-3/evidence/` |

---

## 1. Methodology

1. Map the **16-lesson** pack surfaces (begin → cover → contents → 16 lessons → decks → quiz → 4 labs → dashboard).
2. Build a Pass 3 risk register focused on Lead priorities; score **Impact (1–5) × Likelihood (1–5)**.
3. Test highest scores first with source + HTTP evidence; fold headed browser confirmation where provided.
4. Do **not** invent findings. Do **not** re-open Pass 1/2 P0s unless a **regression is reproduced** on this pack.
5. Confirm live HTML/JS/CSS lack primer stems (`01_The_Loop` / `bl-01-loop`); ignore `01_source/INTEGRITY_REPORT.md` archive mentions.

### Lead focus (highest priority)

1. Labs `lessonId` / scene / deck ids vs quiz `lessonId` and `decks.html` checkboxes  
2. HTTP vs `file://` progress (BAT / README / Open*.bat / ps1)  
3. ~128-question exam load (16×8) — hang / blank / OOM / wrong score risk  
4. Outbound primary links from begin / cover / contents / lessons / docs  

---

## 2. Environment (confirmed)

| Check | Result |
| --- | --- |
| Server | `GET /` and `GET /00_CLICK_HERE_TO_BEGIN.html` → **200** |
| Lessons on disk | **16** HTML (+ matching `.md`) under `02_lessons/` |
| Quiz bank file | `03_quiz/questions.js` ≈ **139 807** bytes |
| Labs | `spaced`, `bias`, `fermi`, `steelman` (+ `shared.js`) |
| Old primer stems in live HTML/JS/CSS | **None** (`rg` over pack excluding `01_source/` → no `01_The_Loop` / `bl-01-loop`) |
| Deck ID scheme | `bl-a1-diverge` … `bl-d4-launch` (16) |
| Arc buttons | Arc A door / B methods / C tools / D ship (headed + source) |

---

## 3. Risk register (PASS 3) — prioritized

Impact × Likelihood = Score. Status after Pass 3 tests.

| ID | Risk | I | L | Score | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| **R3-01** | Lab / quiz / decks `lessonId` mismatch → weak-area or lab↔quiz continuity break | 4 | 1 | **4** | **MITIGATED** | All four labs + quiz + `decks.html` share the same 16 `bl-*` ids; no orphans/missing |
| **R3-02** | `file://` / launcher path → localStorage origin split / progress loss | 4 | 2 | **8** | **PARTIAL** | Primary BAT + Open*.bat/`open-http.ps1` prefer HTTP; residual if Python missing or HTML double-clicked |
| **R3-03** | Full 128-Q exam load hang / blank / OOM / wrong session size | 4 | 1 | **4** | **MITIGATED** | Bank 128 unique; HTTP ~1 ms; node parse ~3 ms; headed UI shows 16 decks · 128 Q promptly |
| **R3-04** | Broken / wrong outbound or primary pack links | 5 | 1 | **5** | **MITIGATED** | Internal crawl 41/41 HTTP 200; 7 external citation URLs all HTTP 200 |
| **R3-05** | Quiz bank integrity (≠128, dup ids, ≠1 correct) | 5 | 1 | **5** | **MITIGATED** | 128 unique ids; 16×8; exactly one `correct:true` each |
| **R3-06** | Exam unanswered inflate / empty-decks→all (Pass 1 High regressions) | 3 | 1 | **3** | **FIXED** (no regression) | `submitExam` skips null `answerKey`; decks empty → disabled + error (no `ids.length===0?'all'`) |
| **R3-07** | Steelman grader wrong domain (Pass 1 R01 regression) | 3 | 1 | **3** | **FIXED** (no regression) | Build Loop prompt; no `cardio\|physiology\|bloodwork` in `shared.js` |
| **R3-08** | Dual namespace: lesson `markLesson` filename stems vs quiz `bl-*` (future deep-link confusion) | 2 | 2 | **4** | **ACCEPTED** | Orthogonal by design today; dashboard `lessonMeta` matches markLesson stems; weak areas use quiz `lessonId` |
| **R3-09** | Fermi Term Match option values `body`/`blood` (leftover set names) while UI says Arc A–B / C–D | 1 | 2 | **2** | **OPEN** (cosmetic) | Sets correctly hold all 16 `bl-*`; learner-facing labels OK; URL/value names cryptic |
| **R3-10** | Dim-theme quiz `.badge` contrast (Pass 2 NR01 residual) | 3 | 2 | **6** | **OPEN** (not Lead focus) | CSS still `#fff6d6` on dim `--accent` `#5ec8d6`; not retested as P0; residual only |

**Prioritization order used:** R3-01 → R3-02 → R3-03 → R3-04, then integrity/regression checks R3-05..R3-07, then residuals.

---

## 4. Tests run on top risks (with evidence)

### 4.1 Labs lessonId vs quiz ids vs decks (R3-01, R3-05, R3-08) — Lead #1

**Expected id set (16):**  
`bl-a1-diverge`, `bl-a2-cynefin`, `bl-a3-pdca-ooda`, `bl-a4-bml-diamond`, `bl-b1-discovery`, `bl-b2-coats`, `bl-b3-levers`, `bl-b4-intent`, `bl-c1-protocol`, `bl-c2-generate`, `bl-c3-fidelity`, `bl-c4-test`, `bl-d1-critique`, `bl-d2-reviews`, `bl-d3-evidence`, `bl-d4-launch`

| Surface | Count | Missing vs expected | Orphans |
| --- | --- | --- | --- |
| `decks.html` checkbox `value=` | 16 | none | none |
| `03_quiz/questions.js` `lessonId` | 16 unique; **8 Q each** | none | none |
| `04_labs/bias.html` scene `id` | 16 | none | none |
| `04_labs/fermi.html` deck `id` | 16 | none | none |
| `04_labs/spaced.html` deck `id` | 16 | none | none |
| `04_labs/steelman.html` `lessonId` | 16 | none | none |

- Question bank: **128** questions, **128** unique `id`s, **0** with ≠1 `correct:true` (node + `window.QUESTIONS`).
- Weak-area path in `app.js` aggregates by `q.lessonId` (same `bl-*`); tip points at Lesson filter (populated from bank).
- **Lesson read keys** use filename stems (`01_Divergent_and_Convergent` … `16_Launch_and_Operations`): all 16 lessons load `shared.js` + `markLesson(...)`; `dashboard.html` `lessonMeta` matches those stems **exactly**. No code bridge maps `bl-*` ↔ stems; not required for current weak-area or lab↔quiz continuity.
- Headed: Deck Chooser shows **L01–L16 all checked**; Arc A door / B methods / C tools / D ship present. Shot: `evidence/decks-16-checked.png`.
- Headed: Labs index lists four labs; hub does not surface lesson ids; no `The_Loop` primer labels observed (steering confirmation).

**Result:** No orphan/missing `bl-*` across labs ↔ quiz ↔ decks. Continuity risk **mitigated**. Dual stem/`bl-*` namespace is **accepted architecture** (R3-08), not a lab↔quiz break.

### 4.2 HTTP vs file:// progress (R3-02) — Lead #2

| Launcher / doc | Behavior |
| --- | --- |
| `00_CLICK_HERE_TO_BEGIN.bat` | Prefers `python -m http.server 8765` then opens `http://127.0.0.1:8765/00_CLICK_HERE_TO_BEGIN.html`; warns and falls back to file open if no Python |
| `open-http.ps1` | Ensures server on `:8765`, then `Start-Process http://127.0.0.1:8765/$Page` |
| `Open Home/Dashboard/Deck Chooser/Labs/Quiz.bat` | All call `open-http.ps1` (no longer raw `Start-Process` file paths — **Pass 2 NR02 addressed**) |
| `README.md` / `START HERE.txt` | Prefer BAT/HTTP; warn that `file://` may isolate progress |

**Residual:** Double-clicking HTML directly, or BAT fallback when Python is absent, can still fragment localStorage origins across pages.

**Score:** Impact 4 × Likelihood 2 = **8** (down from Pass 2 R02 residual where sibling BATs were still file://).

### 4.3 128-question exam load (R3-03, R3-05, R3-06) — Lead #3

| Evidence | Value |
| --- | --- |
| Bank size | **128** = 16×8 |
| `curl` `questions.js` | HTTP **200**, 139 807 bytes, **~0.0009 s** total |
| Node parse + build queue | parse **~2.8 ms**; queue build **~0.04 ms**; heap ~5 MB in script |
| `?decks=all` quiz index | HTTP **200** |
| Exam size UI | includes option **128** (+ 8/16/32/56/all filtered) |
| `submitExam` | records only when `item.answerKey != null` (unanswered skipped) — **no R03 regression** |
| Empty decks | `deck-error` + disabled Start; no empty→`all` — **no R04 regression** |
| Scoring sims (answered path) | all-correct 128/128; all-wrong 0; unanswered-only answered 0 |

**Headed confirmation:** `03_quiz/index.html?decks=all` loaded promptly; UI shows **“16 decks · 128 questions”**, **“0 / 128 answered”**, **“0 correct”**, first item “Question 1 of 128”. No blank/hang observed in shot. Shot: `evidence/exam-128-loaded.png`.

**Result:** Load/performance risk for 128-Q bank **mitigated** under HTTP on this environment. Residual: multi-hour learner session / very low-end devices not profiled beyond static+headed smoke.

### 4.4 Outbound / primary links (R3-04) — Lead #4

**Internal (pack HTML `href`/`src` + CSS `url()`, excluding `01_source` deep archive as non-UI):**  
**41 / 41 HTTP 200** under `:8765`.

**Spot surfaces (all 200):** begin, cover, contents, decks, dashboard, quiz (+ `decks=all` and multi-deck query), 4 labs, `assets/pack.css`, `assets/theme.js`, **all 16 lesson HTML**.

**External citations found on primary lesson/begin/cover/contents surfaces (7):** all **HTTP 200** via GET:

- `https://agilemanifesto.org/`
- `https://agilemanifesto.org/principles.html`
- `https://armypubs.army.mil/`
- `https://hbr.org/2007/11/a-leaders-framework-for-decision-making`
- `https://scrumguides.org/scrum-guide.html`
- `https://www.designcouncil.org.uk/our-resources/framework-for-innovation/`
- `https://www.nngroup.com/articles/ten-usability-heuristics/`

Begin/cover CTAs include Contents, Lesson 1, Decks/Labs (begin), Dashboard — no dead primary CTAs in crawl.

### 4.5 Pass 1/2 P0 regression hunt (R3-06, R3-07)

| Former P0 | Pass 3 | Evidence |
| --- | --- | --- |
| Steelman cardio grader | **No regression** | Build Loop prompt text; no cardio/physiology/bloodwork in `shared.js` |
| Exam unanswered → wrong + inflate | **No regression** | `answerKey != null` gate; dashboard copy documents skip rule (headed dashboard shows skip wording) |
| Empty decks → all | **No regression** | empty removes usable Start; shows “Select at least one deck.” |

Headed dashboard (zero progress): unique quiz answered **0**, labs **0**, L01+ “not yet” — consistent with fresh origin. Shot: `evidence/dashboard-zero.png`.

---

## 5. Findings + severity (tied to risk IDs)

| Finding | Severity | Risk ID | Evidence |
| --- | --- | --- | --- |
| **F1** — Lab scene/deck/`lessonId` sets, quiz bank, and `decks.html` checkboxes are **aligned** (16 `bl-*`, 8 Q each, 128 total). No orphans/missing that break weak-area or lab↔quiz continuity. | **Info / Pass** | R3-01, R3-05 | node cross-compare; headed decks + exam shots |
| **F2** — Progress launch prefers HTTP; sibling Open*.bat now use `open-http.ps1`. Residual progress loss if Python missing or HTML opened as `file://`. | **P2** (residual) | R3-02 | BAT/ps1/README source |
| **F3** — Full exam bank loads promptly at 128 Q / 16 decks; no hang/blank/OOM signal in node+curl+headed smoke. | **Info / Pass** | R3-03 | curl timing; headed exam shot |
| **F4** — Primary internal + outbound citation links healthy (41/41 internal; 7/7 external 200). | **Info / Pass** | R3-04 | python crawl |
| **F5** — Fermi set option **values** remain `body` / `blood` (UI labels correctly say Arc A–B / C–D). Sets contain correct `bl-*`. Cosmetic / naming debt. | **P3** | R3-09 | `fermi.html` L1552–1572 |
| **F6** — Lesson visit keys use filename stems; quiz/labs use `bl-*`. Consistent within each subsystem; no join bug found. | **Info / Accepted** | R3-08 | markLesson + dashboard `lessonMeta` |
| **F7** — No Pass 1/2 P0 regressions reproduced (grader domain, unanswered inflate, empty→all). | **Info / Pass** | R3-06, R3-07 | source gates |
| **F8** — Dim `.badge` cream-on-cyan still in `03_quiz/styles.css` (Pass 2 NR01 residual). Not Lead focus; not elevated to new P0. | **P2 residual** | R3-10 | CSS L371–390 |

**Invented findings: none.** Private master prompt: not opened.

---

## 6. Residual risks

1. **R3-02 (score 8):** Learners without Python, or who open HTML via Explorer, may still lose cross-page progress.  
2. **R3-10 (score 6):** Dim quiz lesson badges may remain hard to read (carry-forward).  
3. **R3-08 (score 4):** If a future feature deep-links weak `bl-*` areas to lesson HTML without a map, it will break until a bridge exists.  
4. **R3-09 (score 2):** `decks=body|blood` in Term Match URLs/state is cryptic for support.  
5. Exam UX under very constrained devices / long timed exams not stress-tested beyond smoke.

---

## 7. Recommendations (risk-ordered)

1. Keep documenting HTTP-first launch; optionally make the no-Python BAT path louder (modal/page banner when `location.protocol === 'file:'`) — addresses **R3-02**.  
2. Rename Fermi internal sets/option values from `body`/`blood` → e.g. `arc-ab` / `arc-cd` (keep labels) — **R3-09**.  
3. If product wants “open lesson from weak area,” add an explicit `bl-*` → `02_lessons/….html` map — **R3-08**.  
4. Finish dim `.badge` contrast (≥4.5:1) if polish pass continues — **R3-10**.  
5. No blocking fix required for lab↔quiz id alignment or 128-Q load based on this pass.

---

## 8. Summary for Lead

| Item | Result |
| --- | --- |
| **Report path** | `/workspace/qa-reports/pass-3/risk-based-PASS3.md` |
| **Pack under test** | **16-lesson** field atlas (`bl-a1-diverge` … `bl-d4-launch`, 128 Q) |
| **Top risks (scores)** | **R3-02 file:// progress 8**; R3-10 dim badge residual 6; R3-04 links 5 (mitigated); R3-05 bank 5 (mitigated); R3-01 id alignment 4 (mitigated); R3-03 exam load 4 (mitigated) |
| **Findings** | F1 id alignment **pass**; F2 HTTP residual **P2**; F3 128 load **pass** (headed + node); F4 links **pass**; F5 fermi body/blood **P3**; F6 dual namespace **accepted**; F7 **no P0 regressions**; F8 dim badge **residual** |
| **P0 regressions reproduced?** | **No** |
| **Blockers** | **None** for id continuity, exam load, or primary links |
| **Headed shots** | `evidence/decks-16-checked.png`, `evidence/exam-128-loaded.png`, `evidence/dashboard-zero.png` |

**Bottom line:** On the 16-lesson pack, lab↔quiz↔deck ids align; 128-Q exam loads cleanly under HTTP; outbound/primary links check out; launch path is improved vs Pass 2 but `file://` progress loss remains the highest open risk (score 8). Ship-blocking P0s from Pass 1/2 were **not** reproduced.
