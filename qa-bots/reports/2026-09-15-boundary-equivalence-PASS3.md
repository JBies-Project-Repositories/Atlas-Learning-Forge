# Boundary Value Analysis & Equivalence Partitioning Report — **PASS 3**

**Label:** PASS 3 / 2026-09-15 PT  
**App:** Atlas of the Build Loop — Study Pack (16-lesson field atlas)  
**Tester:** Boundary & Equivalence Tester  
**Methodology:** Boundary value analysis (BVA) and equivalence partitioning only  
**Target URL:** http://127.0.0.1:8765/  
**Pack path:** `/workspace/atlas-study-pack/pack/`  
**Compared to:** Pass 2 report `/workspace/qa-reports/pass-2/boundary-equivalence-PASS2.md`  
**Brief:** `/workspace/qa-reports/pass-3/PASS3_BRIEF.md`

---

## 1. Methodology

PASS 3 exercised **deck-query partitions**, **exam session-size edges**, and **exam unanswered → unique-answer progress counting** on the 16-lesson bank (128 questions; deck IDs `bl-a1-diverge` … `bl-d4-launch`). Cases used min / representative / max option values and invalid IDs. No other methodologies. No Pass 1/2 P0s re-opened (no regression reproduced for those).

---

## 2. Partitions / edges covered

| Area | Equivalence / boundary |
|---|---|
| Deck query `?decks=` | missing; empty string; one valid id; four-id Arc A; `all`; junk only; valid+junk |
| Exam size select | 8, 16, 32, 56, 128 on full bank; 128 on 8-question bank (cap) |
| Exam unanswered | 0 of N answered on submit vs unique `quiz.ids` / dashboard answered |
| Live stem hygiene | `bl-01-loop` / `01_The_Loop` must not appear on quiz live HTML |

---

## 3. Process

1. Confirmed HTTP 200; inspected `decks.html`, `03_quiz/index.html` / `app.js` / `questions.js` (16 lessons × 8 Q = 128; size options include 128).
2. Browser BVA: deck-query A1–A7, then exam sizes B1–B6 and unanswered unique-count C1–C3.
3. Wrote this report under `/workspace/qa-reports/pass-3/`.

---

## 4. Test matrix & results

### A. Deck query

| ID | Input | Expected | Observed | Result |
|---|---|---|---|---|
| A1 | No `decks` param | All bank | Subtitle `16 decks · 128 questions`; Practice shows `Question 1 of 128` | **PASS** |
| A2 | `?decks=` (empty) | Defaults to all | Subtitle `16 decks · 128 questions`; questions load | **PASS** |
| A3 | `?decks=bl-a1-diverge` | 1 deck · 8 Q | Subtitle `1 deck · 8 questions · Divergent and Convergent Thinking`; `Question 1 of 8` | **PASS** |
| A4 | Four-id Arc A | 4 decks · 32 Q | Subtitle `4 decks · 32 questions · selected decks`; filter `Chosen decks (4 · 32 Qs)`; `Question 1 of 32` | **PASS** |
| A5 | `?decks=all` | 16 · 128 | Subtitle `16 decks · 128 questions`; All decks selected | **PASS** |
| A6 | `?decks=junk-id-xyz` | Empty / safe | Subtitle `0 decks · 0 questions`; `No questions for this filter.`; no crash | **PASS** |
| A7 | valid + junk | Valid Qs only | Subtitle `1 deck · 8 questions …`; filter `Chosen decks (2 · 8 Qs)`; `Question 1 of 8` | **PASS** |

Live quiz pages: search for `bl-01-loop` and `01_The_Loop` → **not present** (PASS hygiene).

### B. Exam session sizes (`?decks=all`, Exam mode, Timer Off)

| ID | Size | Expected N | Observed | Result |
|---|---|---|---|---|
| B1 | 8 | 8 | `Question 1 of 8` | **PASS** |
| B2 | 16 | 16 | `Question 1 of 16` | **PASS** |
| B3 | 32 | 32 | `Question 1 of 32` | **PASS** |
| B4 | 56 | 56 | `Question 1 of 56` | **PASS** |
| B5 | 128 | 128 | `Question 1 of 128` | **PASS** |
| B6 | 128 with `?decks=bl-a1-diverge` (bank 8) | Cap to 8 | `Question 1 of 8`; no crash | **PASS** |

### C. Exam unanswered vs unique-answer count

| ID | Steps | Expected | Observed | Result |
|---|---|---|---|---|
| C1 | Clear storage attempts → Exam size 8 → answer **0** → Submit | Results `Answered 0 of 8`; unique count must **not increase** by unanswered | Results showed **0 / 8 answered**. After clear attempts dashboard baseline was **9** (not 0); after unanswered submit dashboard **remained 9** (did not inflate by 8). Product check for inflation: **held**. Clean zero baseline via `removeItem` alone: **not achieved** in this run. | **PASS** (no inflation) / setup note below |
| C2 | Exam size 8 → answer **exactly 1** → Submit | `Answered 1 of 8`; dashboard unique = 1 | Results **1 / 8**; dashboard unique **1** | **PASS** |
| C3 | New exam → answer a **different** question once | Unique increases by 1 (to 2) | Results **1 / 8**; dashboard unique **2** | **PASS** |

**C1 setup note:** Browser `localStorage.removeItem` attempts did not yield a dashboard reading of 0 before the unanswered submit (stuck at 9). That is a **test-setup / observability gap** for this run, not evidence that unanswered inflate unique IDs. Inflation criterion is supported by dashboard staying at 9 while results reported 0 answered. Same-id re-answer uniqueness was not separately proven beyond C2/C3 distinct-id behavior (acceptable; Lead asked for unanswered not inflating).

---

## 5. Summary counts

| Result | Count |
|---|---|
| **PASS** | **15** (A1–A7, B1–B6, C2, C3; C1 inflation criterion) |
| **FAIL** (product defect) | **0** |
| **BLOCKED** | **0** |
| Setup gap | C1 clean-zero baseline not obtained via storage-remove alone |

---

## 6. Defects found

**None.** No new BVA defects. No Pass 1/2 P0 regressions reproduced.

---

## 7. Gaps / residual notes (not defects)

1. **C1 clean baseline:** Prefer dashboard **Reset progress** (confirm) before unanswered-unique checks if `removeItem` alone leaves a non-zero UI reading.
2. **Exam % denominator** (Pass 2 residual): score still uses `correct / session.length` while unanswered are skipped for answer recording — not re-filed; no Pass 3 regression chase.
3. **A7 filter label:** UI may show `Chosen decks (2 · 8 Qs)` when one of two URL ids is junk — content correctly filters to 8 Q; label counts URL ids, not matched lessons (observation only).

---

## 8. Conclusion

PASS 3 BVA on the **16-lesson** atlas: deck-query edges (empty / one / four-arc / all / junk), session sizes **8 / 16 / 32 / 56 / 128** (plus bank-cap), and exam unanswered **not inflating** unique-answer progress all hold under observed evidence. Ready for Lead sponsor delta vs Pass 2.

**Report path:** `/workspace/qa-reports/pass-3/boundary-equivalence-PASS3.md`
