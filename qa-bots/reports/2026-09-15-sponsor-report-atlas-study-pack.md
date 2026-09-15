# Formal QA Sponsor Report
## Atlas of the Build Loop — Study Pack

| Field | Value |
| --- | --- |
| **Project sponsor** | Jenner |
| **QA lead** | QA/Tester Lead |
| **Target** | Atlas of the Build Loop — Study Pack (offline HTML field guide) |
| **Sponsor entry path** | `C:\Users\jbies\OneDrive\Desktop\Atlas of the Build Loop — Study Pack\00_CLICK_HERE_TO_BEGIN.html` |
| **Test environment** | Shared local server `http://127.0.0.1:8765/` serving the Study Pack |
| **Date** | 2026-09-15 (America/Los_Angeles) |
| **Auth** | None |

---

## 1. Executive summary

Seven methodology-specific testers executed independent passes against the Study Pack. **Critical-path smoke is green (8/8).** The pack is navigable and usable for learning under HTTP. **No show-stopping navigation or asset breakage** was found under the shared test server.

The highest-priority product issues cluster around **trust and control of progress**, **incorrect Steelman grader domain copy**, **accessibility contrast**, and **deck-selection / exam edge behavior**. Perceived performance on localhost is strong.

**Overall recommendation:** Ship-ready for offline learning **with a short P0 fix pass** before wide distribution (especially Steelman grader text, empty-deck → all-decks coercion, quiz badge contrast, and clearer progress/reset semantics). Prefer documenting or launching via local HTTP so progress keys share one origin.

---

## 2. Test program (process)

| # | Bot | Methodology | Status | Artifact |
| --- | --- | --- | --- | --- |
| 1 | Smoke & Sanity Tester | Smoke / sanity checklist | Complete — 8/8 PASS | `qa-bots/reports/2026-09-15-smoke-sanity-atlas-study-pack.md` |
| 2 | Exploratory Session Tester | SBTM (45-min charter) | Complete — charter satisfied; F1–F5 | `qa-bots/reports/2026-09-15-exploratory-sbtm-atlas-study-pack.md` |
| 3 | Boundary & Equivalence Tester | BVA / equivalence | Complete — 38 PASS / 3 FAIL / 2 BLOCKED | `qa-bots/reports/2026-09-15-boundary-equivalence-atlas-study-pack.md` |
| 4 | Usability Heuristics Tester | Nielsen heuristics | Complete — 0 critical / 6 major / 7 minor | `qa-bots/reports/2026-09-15-usability-heuristics-atlas-study-pack.md` |
| 5 | Accessibility WCAG Tester | WCAG-oriented a11y | Complete — 1 Critical / 4 Serious / 7 Moderate / 5 Minor | `qa-bots/reports/2026-09-15-accessibility-wcag-atlas-study-pack.md` |
| 6 | Risk-Based Tester | Risk register × prioritized tests | Complete — R01–R14; top High: R01, R02 | `qa-bots/reports/2026-09-15-risk-based-atlas-study-pack.md` |
| 7 | Performance Observation Tester | Perceived performance | Complete — no blockers on localhost | `qa-bots/reports/2026-09-15-performance-observation-atlas-study-pack.md` |

**Coordination:** Bots seated in **QA Squad** and **QA Squad Extended**. Each submitted a full markdown report to QA/Tester Lead; this document is the sponsor rollup.

---

## 3. What was tested (scope)

Primary surfaces exercised across methodologies:

- Begin → Cover → Contents → Lesson 1 (and samples of further lessons)
- Quiz decks / practice & exam modes (56-question bank)
- Labs: Spaced Repetition, Scenario Audit (bias), Term Match (fermi), Steelman
- Dashboard progress (`atlas_build_loop_*_v1` localStorage)
- Theme toggle (Bright / Dim)

**Environment note:** Parallel testers shared `http://127.0.0.1:8765/`, so localStorage counts can be contaminated across bots. Several findings call out shared-origin noise.

---

## 4. Consolidated findings (cross-method)

### 4.1 Confirmed across multiple methodologies (highest confidence)

| Theme | Seen by | Severity band |
| --- | --- | --- |
| **Deck Chooser “Select none” still starts `decks=all`** | Usability (Major), Risk (R04 Medium), Exploratory (related F1 shuffle surprise) | **P0** |
| **Steelman grader prompt is wrong domain (cardio/physiology vs Build Loop)** | Usability (Major), Risk (R01 High) | **P0** |
| **Dashboard quiz counts vs in-quiz progress disagree / can inflate** | Exploratory (F2), Usability (Major), Risk (R03 exam unanswered path) | **P0 / P1** |
| **Lesson reading never recorded (`markLesson` unused)** | Usability (Major), Risk (R05 Low) | **P1** |
| **Progress reset vs theme coupling is messy** | Usability (reset also clears theme — undesired), Risk (R07), BVA (DEF-BVA-01: theme *survived* reset vs source `removeItem`) | **P1** — reconcile intended UX, then fix |
| **Nav chrome inconsistent; Begin/Cover omit Dashboard** | Exploratory (F4/F5), Usability (Major), Risk (R08) | **P1** |
| **Lab “Show answer” ≠ lab action until rate** | Exploratory (F3) | **P2** (copy / progress semantics) |

### 4.2 Accessibility (WCAG)

| Sev | Count | Top items |
| --- | --- | --- |
| Critical | 1 | Quiz level badge contrast ~1:1 (accent-on-accent) |
| Serious | 4 | Contents arc gold-on-teal in light; Steelman dim CTA contrast; Steelman label not associated; quiz `#quiz` entire main as `aria-live` |
| Moderate | 7 | Incorrect feedback not announced; unnamed lab lock-copy button; weak focus on cover CTA; no skip links; missing `<main>` on many pages; cover heading structure; limited `:focus-visible` |
| Minor | 5 | External-link cues, theme `aria-pressed`, etc. |

### 4.3 Boundary / equivalence defects

| ID | Sev | Summary |
| --- | --- | --- |
| DEF-BVA-01 | Medium | Theme remained after Dashboard Reset (diverges from source clearing theme) |
| DEF-BVA-02 | Medium | Weak Areas / Clear history UI stayed stale until collapse/reload |
| DEF-BVA-03 | Low/Medium | Empty Steelman Score blocks silently (message missing / below fold) |

Solid boundaries: steelman 39/40 char gate; rubric 0/3/5; lab bar cap at 20 actions; corrupt JSON / invalid theme fail closed; quiz exam edges (0 answered, 1 of 8); Fermi wrong/correct match.

### 4.4 Smoke & performance

- **Smoke:** Begin, cover, contents, Lesson 1, quiz happy path, labs happy path, dashboard, theme — **all PASS**. No blockers.
- **Performance:** Instant perceived load on localhost; residual risk mainly large JPEGs / full quiz DOM off-localhost or on low-end devices. No load/DoS testing performed (by design).

### 4.5 Risk-based residual (after HTTP verification)

Mitigated under HTTP: broken pack links/assets (29/29 200), quiz bank integrity (56 Q, scoring math), lab DOM wiring, theme readability on primary path.

Still open / High: **R01** grader domain, **R02** `file://` / BAT open may fragment localStorage origins for real learners, **R03** exam unanswered → progress/weak pollution, **R04** Select none → all.

---

## 5. Prioritized recommendations for sponsor

### P0 — Fix before wide share
1. **Stop coercing empty deck selection to `all`** — disable Start or require ≥1 deck (`decks.html`).
2. **Rewrite Steelman grader prompt** in `04_labs/shared.js` to Build Loop / shipping misconceptions (remove cardio/physiology/bloodwork).
3. **Fix quiz `.badge-level` contrast** (Critical a11y).
4. **Define one progress counting rule** and align Dashboard “Quiz answers recorded” with quiz UI; do not increment answered for unanswered exam items.

### P1 — Fix soon
5. Prefer **HTTP launcher** (or strong README warning) so Windows double-click/`file://` does not silently break progress (R02).
6. Wire **lesson-read progress** or remove dead `markLesson` expectations.
7. **Reset semantics:** decide whether theme is in scope; make confirm copy match behavior; retest DEF-BVA-01.
8. Unify **navigation chrome**; add Dashboard escape from Begin/Cover.
9. Fix Contents **arc-head contrast** (light) and Steelman **dim CTA** + **label association**.
10. Narrow quiz **aria-live**; announce practice feedback; name Scenario Audit lock-copy control.

### P2 — Polish
11. Explain SRS rating consequences; clarify lab action / bar semantics.
12. Align timer hint (15–120) with UI options (max 60).
13. Skip links, `<main>` landmarks, stronger `:focus-visible`.
14. Weak Areas panel refresh without reload (DEF-BVA-02); Steelman empty validation message visibility (DEF-BVA-03).

---

## 6. Per-methodology results (digest)

### Smoke & Sanity
**8/8 PASS.** No blockers. Residual: not a deep content, full-quiz, or a11y pass.

### Exploratory (SBTM)
Charter satisfied (begin → lesson → quiz → lab → progress). Findings F1–F5 (minor/nit): shuffle surprise after Lesson 1, dashboard count mismatch (suspected shared origin), reveal≠rate, Begin lacks Dashboard, Cover nav below fold. Follow-up charters proposed (clean-state progress, lesson-aligned quiz, lab action contract).

### Boundary & Equivalence
**43 cases: 38 PASS / 3 FAIL / 2 BLOCKED.** Defects DEF-BVA-01–03. Gaps: spaced SM-2 meta not fully UI-verifiable; spaced reset/exhaustion incomplete; timer domain mismatch.

### Usability Heuristics
**0 critical / 6 major / 7 minor.** Primary path strong. Highest UX risk: selection/progress trust, chrome inconsistency, Steelman domain mismatch.

### Accessibility WCAG
**1 Critical / 4 Serious / 7 Moderate / 5 Minor.** Pack usable for continued a11y work; no test blockers. Prioritize contrast + live regions + labels/landmarks.

### Risk-Based
Risk register R01–R14 with scored prioritization. Headed HTTP pass confirmed nav/quiz/labs/dashboard/theme healthy; did not retire R01–R04 code-path risks.

### Performance Observation
Strong perceived performance on localhost; no jank/blockers. Residual: remote/slow network image weight; low-end full 56-Q DOM.

---

## 7. Evidence index

All methodology reports:

```
qa-bots/reports/2026-09-15-smoke-sanity-atlas-study-pack.md
qa-bots/reports/2026-09-15-exploratory-sbtm-atlas-study-pack.md
qa-bots/reports/2026-09-15-boundary-equivalence-atlas-study-pack.md
qa-bots/reports/2026-09-15-usability-heuristics-atlas-study-pack.md
qa-bots/reports/2026-09-15-accessibility-wcag-atlas-study-pack.md
qa-bots/reports/2026-09-15-risk-based-atlas-study-pack.md
qa-bots/reports/2026-09-15-performance-observation-atlas-study-pack.md
qa-bots/reports/2026-09-15-sponsor-report-atlas-study-pack.md  (this file)
```

Screenshot evidence for individual methodologies lives under `docs/screenshots/2026-09-15/` in the matching commit packs (smoke, exploratory-sbtm, usability-heuristics, risk-based, accessibility-wcag).

---

## 8. Disposition

| Question | Answer |
| --- | --- |
| Can a learner open and navigate the pack under HTTP? | **Yes** |
| Are there P0 defects before wide distribution? | **Yes** (deck coercion, Steelman grader domain, quiz badge contrast, progress counting integrity) |
| Is localhost performance a concern? | **No** (watch remote / low-end) |
| Is the `file://` Windows path safe for progress? | **At risk** — document HTTP or fix packaging |
| Formal multi-method QA complete? | **Yes — all 7 reports received and compiled** |

---

*Compiled by QA/Tester Lead for project sponsor Jenner — 2026-09-15 PT.*
