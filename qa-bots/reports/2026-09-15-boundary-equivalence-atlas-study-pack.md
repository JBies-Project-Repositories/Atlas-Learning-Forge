# Boundary Value Analysis & Equivalence Partitioning Report

**App:** Atlas of the Build Loop — Study Pack (offline HTML field guide)  
**Tester:** Boundary & Equivalence Tester  
**Methodology:** Boundary value analysis (BVA) and equivalence partitioning only  
**Target URL:** http://127.0.0.1:8765/00_CLICK_HERE_TO_BEGIN.html  
**Date:** 2026-09-15 (America/Los_Angeles)  
**Sponsor brief focus:** quiz inputs, lab text fields, counters/progress edges, empty vs filled localStorage, theme states  

---

## 1. Methodology

Equivalence classes were derived from observable inputs and storage keys. For each numeric or length-bounded input, cases targeted **min / just-below / just-above / max** (or documented option edges). Discrete selects and modes used one representative per class. Empty vs filled vs corrupt localStorage were treated as separate partitions. Cases were executed against the live shared URL in a browser; results below are observed UI outcomes (`PASS` / `FAIL` / `BLOCKED`).

---

## 2. Partitions identified

### 2.1 Theme (`atlas_build_loop_theme_v1`)
| Class | Representatives |
|---|---|
| Missing / unset | no key → treat as light |
| Valid light | `"light"` |
| Valid dim | `"dim"` |
| Invalid / other | e.g. `"purple"` → non-dim → light |
| Cleared by dashboard reset | key removed with other Atlas keys |

### 2.2 Quiz (`03_quiz`)
| Input | Partitions / boundaries |
|---|---|
| Mode | `practice` \| `exam` |
| Timer (minutes) | `0` (Off), `15`, `30`, `45`, `60` (UI steps; hint text mentions 15–120) |
| Exam size | `0` (all filtered), `8`, `16`, `32`, `56` |
| Deck filter | all (~56 Q), single lesson, multi via `?decks=` |
| Answer state | unanswered \| correct \| incorrect; practice lock after first answer |
| Exam submit coverage | 0 answered, 1 of N, all answered |
| Weak history | empty \| populated \| clear |

### 2.3 Steelman lab (`textarea` + rubric)
| Input | Boundaries |
|---|---|
| Text length | empty (0), just-below min (39), min (40), longer valid |
| Rubric checks | 0/5, 3/5, 5/5 (score stored as `s * 20` in progress) |

### 2.4 Bias / Scenario lab
| Input | Partitions |
|---|---|
| Lesson select | empty \| selected lesson |
| Answer textarea | empty, whitespace, short text (no length gate observed) |

### 2.5 Spaced repetition
| Input | Partitions / boundaries |
|---|---|
| Deck select | empty \| one lesson \| all |
| Grade | Again(0), Hard(1), Good(2), Easy(3) |
| Card schedule | reps 0→1 (interval 1d), grade 0 resets interval; EF floor 1.3 |
| Due pile | due > 0 \| due = 0 (clear deck) |

### 2.6 Fermi / Term Match
| Input | Partitions |
|---|---|
| Deck select | empty \| selected |
| Pair action | wrong match \| correct match; first-try score |

### 2.7 Dashboard / progress (`atlas_build_loop_progress_v1`)
| Input | Boundaries |
|---|---|
| Quiz answered | 0 \| >0 |
| Lab actions bar | `pct = min(100, actions * 5)` → **0, 1, 19, 20, 21** (cap at 20 actions = 100%) |
| Reset confirm | cancel \| OK |
| Corrupt JSON | malformed string → empty fallback |

### 2.8 Related storage keys
- `atlas_build_loop_weak_v1` (quiz weak areas)
- `atlas_build_loop_srs_v1` (spaced)
- `atlas_build_loop_theme_v1`
- `atlas_build_loop_progress_v1`

---

## 3. Process / steps taken

1. Confirmed shared server returned HTTP 200 for begin page; inspected pack HTML/JS for input domains and boundaries.
2. Built the case matrix in §4 from those partitions (priority per QA brief).
3. Executed cases in the box browser against `http://127.0.0.1:8765/…`, including localStorage seed/corrupt cases on the dashboard.
4. Recorded PASS/FAIL/BLOCKED with observed behavior; logged defects and unclear boundaries.

---

## 4. Test matrix and results

### Theme

| ID | Case | Expected | Observed | Result |
|---|---|---|---|---|
| T1 | Missing theme key | Light theme; button “Dim mode” | Light + “Dim mode” | PASS |
| T2 | Toggle to dim | Dim theme; “Bright mode” | As expected | PASS |
| T3 | Toggle back to light | Light; “Dim mode” | As expected | PASS |
| T4 | Navigate while dim | Theme persists | Persisted | PASS |
| T5 | Dashboard Reset OK while dim | Theme key cleared → light after reload | Progress cleared; **dim theme remained** | **FAIL** |

### Quiz

| ID | Case | Expected | Observed | Result |
|---|---|---|---|---|
| Q1 | Practice default | Loads; `0 / N answered` | As expected | PASS |
| Q2 | Correct answer (practice) | Score up; feedback; radio locked | As expected | PASS |
| Q3 | Incorrect answer | Wrong feedback | As expected | PASS |
| Q4 | Clear answers | Selections cleared | As expected | PASS |
| Q5 | Switch to exam | Start exam visible; Submit disabled until start | As expected | PASS |
| Q6 | Exam size 8, timer Off | Session of 8 questions | 8 questions | PASS |
| Q7 | Single-deck filter | Count matches selected deck | Matched | PASS |
| Q8 | Submit with 0 answers | `0 correct`; `Answered 0 of N` | As expected | PASS |
| Q9 | Size 8, answer 1, submit | `Answered 1 of 8` | As expected | PASS |
| Q10 | Timer 15 min, start exam | Timer visible / counting | Visible and counting | PASS |
| Q11 | Weak areas, empty history | No-history message | As expected | PASS |
| Q12 | Weak entries + Clear history | Immediate UI update | Panel stayed stale until collapse/reopen or reload; clear also needed reload | **FAIL** |
| Q13 | All decks practice | ~56 questions | ~56 | PASS |

### Steelman

| ID | Case | Expected | Observed | Result |
|---|---|---|---|---|
| S1 | Empty text, Score | Block + message (≥ ~40 chars) | Blocked scoring; **no validation message visible** | **FAIL** |
| S2 | Exactly 39 chars | Still blocked | Blocked | PASS |
| S3 | Exactly 40 chars, 0 checks | Allow; `0/5` | `0/5` | PASS |
| S4 | ≥40 chars, 5 checks | `5/5` | `5/5` | PASS |
| S5 | ≥40 chars, 3 checks | `3/5` | `3/5` | PASS |

### Bias / Scenario

| ID | Case | Expected | Observed | Result |
|---|---|---|---|---|
| B1 | Empty lesson select | Choose-lesson / idle | As expected | PASS |
| B2 | Select lesson; empty answer; Show answer | Scenario shown; reveal works without text | As expected | PASS |
| B3 | Whitespace / 1-char answer | No length validation (accepted) | Accepted with no validation | PASS |

### Spaced repetition

| ID | Case | Expected | Observed | Result |
|---|---|---|---|---|
| SP1 | Empty select | Work area hidden | Hidden | PASS |
| SP2 | One lesson | Due/total > 0; card front | 18/18 due; front shown | PASS |
| SP3 | Reveal | Grades Again/Hard/Good/Easy | Shown | PASS |
| SP4 | Grade Again (0) | Due/session update | Due down; session up | PASS |
| SP5 | Grade Easy (3) | EF/reps/interval advance (first pass → interval 1d) | Session/counters moved; **per-card EF/reps/interval not directly verified on next card** | **BLOCKED** |
| SP6 | Reset / exhaust due | Reset or clear-deck state | **No reset control observed**; exhaustion not completed | **BLOCKED** |

### Fermi / Term Match

| ID | Case | Expected | Observed | Result |
|---|---|---|---|---|
| F1 | Empty selection | Cannot play | As expected | PASS |
| F2 | Select deck | Left/right terms shown | As expected | PASS |
| F3 | Wrong match | Mismatch; first-try stays 0 | first-try 0 | PASS |
| F4 | Correct match | Matched count increments | 1/10 | PASS |

### Dashboard

| ID | Case | Expected | Observed | Result |
|---|---|---|---|---|
| D1 | After reset | Quiz/labs empty or zero | Empty/zero | PASS |
| D2 | After quiz answers | answered > 0 | 2 recorded | PASS |
| D3 | After lab actions | Bars for labs with actions | spaced 2, scenario 1, term match 3, steelman 3 | PASS |
| D4 | Reset cancel | Data preserved | Preserved | PASS |
| D5 | Reset OK | Progress keys cleared | Cleared | PASS |

### Progress bar math (`min(100, actions*5)`)

| ID | Case | Expected | Observed | Result |
|---|---|---|---|---|
| P1 | actions=0 | 0% | 0% | PASS |
| P2 | actions=1 | ~5% | ~5% | PASS |
| P3 | actions=19 | ~95% | ~95% | PASS |
| P4 | actions=20 | 100% | 100% | PASS |
| P5 | actions=21 | Cap 100% | 100% | PASS |

### Corrupt / invalid storage

| ID | Case | Expected | Observed | Result |
|---|---|---|---|---|
| C1 | Malformed progress JSON | No crash; empty fallback | Empty fallback | PASS |
| C2 | Theme `"purple"` | Fall back to light | Light + “Dim mode” | PASS |

### Summary counts
| Result | Count |
|---|---|
| PASS | 38 |
| FAIL | 3 |
| BLOCKED | 2 |
| **Total cases** | **43** |

---

## 5. Defects found

### DEF-BVA-01 — Medium — Theme survives dashboard Reset
- **Case:** T5  
- **Expected:** Reset removes `atlas_build_loop_theme_v1` and reload presents light theme.  
- **Observed:** Progress activity cleared, but dim theme remained after confirmed reset.  
- **Notes:** Source on `dashboard.html` does call `removeItem("atlas_build_loop_theme_v1")` before reload; observed behavior diverges — treat as product defect or intermittent persistence until re-verified.  
- **Evidence:** browser observation + screenshot from execution pass.

### DEF-BVA-02 — Medium — Weak Areas / Clear history UI stale
- **Case:** Q12  
- **Expected:** Weak panel and Clear history update immediately.  
- **Observed:** Panel stayed stale until collapse/reopen or full reload; Clear history also required reload to reflect empty state.  
- **Impact:** Learners may think history did not clear.

### DEF-BVA-03 — Low/Medium — Steelman empty submit: silent block
- **Case:** S1  
- **Expected:** Blocking message: “Write a fuller steelman (≥ ~40 chars) before scoring.”  
- **Observed:** Scoring blocked but **no validation message visible** at the interaction point.  
- **Related UX note:** Score output sits below the fold (requires scroll), which may hide the message even when written to `#score`.  
- **Boundary confirmation:** 39 vs 40 characters (S2/S3) behaved correctly once past empty.

---

## 6. Gaps where boundaries were unclear

1. **Spaced Easy grade (SP5):** Session counters moved, but the next card’s meta (EF / reps / interval) could not be confirmed as the same card’s post-rate state — unclear whether UI exposes enough state to verify SM-2 boundaries without inspecting `atlas_build_loop_srs_v1`.  
2. **Spaced reset / exhaustion (SP6):** Reset control was not observed during the pass (reset appears only when due pile is empty per source). Boundary between “due remaining” and “deck clear → Reset this deck” was not fully exercised.  
3. **Timer domain mismatch:** UI options are Off/15/30/45/60; exam mode hint text mentions “15–120”. No UI option for 120 — unclear intended max.  
4. **Exam size vs filtered bank:** When selected deck has fewer questions than exam size (e.g. size 56 on a small deck), expected slice behavior is `min(size, bank)` — covered indirectly via Q7, not every size×deck pair.  
5. **Bias answer length:** No min-length boundary exists (unlike steelman); empty/whitespace/short are one “accepted free text” class — intentional or missing validation is unclear.  
6. **T5 vs source:** Unclear whether theme persistence after Reset is reproducible 100% of the time; recommend a focused retest of Reset while dimmed.

---

## 7. Positive / solid boundaries

- Steelman **39 / 40** character gate works for non-empty short vs min-valid.  
- Rubric scores **0 / 3 / 5** map correctly.  
- Dashboard lab bar **0 / 1 / 19 / 20 / 21** actions respect the 100% cap.  
- Corrupt progress JSON and invalid theme value fail closed to safe empty/light.  
- Quiz exam edges (0 answered, 1 of 8, size 8, timer on) behaved as specified.  
- Fermi wrong vs correct match and empty deck gate behaved correctly.

---

## 8. Residual risk

- Theme/reset inconsistency (DEF-BVA-01) may confuse learners who expect a full wipe.  
- Stale Weak Areas UI (DEF-BVA-02) risks false confidence about cleared history.  
- Silent steelman validation (DEF-BVA-03) may look like a dead Score button.  
- Spaced SM-2 numeric edges not fully proven in UI (SP5/SP6).  

---

## 9. Artifacts

- This report file: `qa-bots/reports/2026-09-15-boundary-equivalence-atlas-study-pack.md`
- Execution screenshots from the Boundary & Equivalence Tester pass (theme reset failure captured during T5) were kept with the tester session and are not duplicated in this commit.

---

*End of BVA / equivalence partitioning report. Scope limited to this methodology only.*
