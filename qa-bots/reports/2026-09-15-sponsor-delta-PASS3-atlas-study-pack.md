# Pass 3 Sponsor Delta — Atlas of the Build Loop Study Pack

| Field | Value |
| --- | --- |
| **Sponsor** | Jenner |
| **QA lead** | QA/Tester Lead |
| **Pass** | **PASS 3** (16-lesson field atlas verification) |
| **Date** | 2026-09-15 (America/Los_Angeles) |
| **Target URL** | `http://127.0.0.1:8765/` |
| **Launch** | `00_CLICK_HERE_TO_BEGIN.bat` → HTTP |
| **Pack** | `/workspace/atlas-study-pack/pack/` (refreshed from Desktop Study Pack ~4:45 PM PT) |
| **Compared to** | Pass 2 sponsor delta (7-lesson build + polish backlog) |
| **Screenshots** | `docs/screenshots/2026-09-15/pass-3/` |

---

## 1. Executive verdict

**Pass 3 is complete (7/7 methodology reports).** The **16-lesson field atlas** is **shippable under the recommended HTTP path** with **no new P0s** and **no reproduced Pass 1/2 P0 regressions**.

Scope confirmed: live UI is the new atlas (L01–L16; deck ids `bl-a1-diverge` … `bl-d4-launch`; **128** questions). Old primer stems (`01_The_Loop` / `bl-01-loop`) were **not** observed in live HTML (archive mention only in `01_source/INTEGRITY_REPORT.md`).

**Vs Pass 2 polish backlog — closed this pass:**
1. Dim badge contrast (NR01 / FIX-03) — **FIXED** (A11y live: lesson ~9.43:1, quiz ~12.64:1 dim)
2. Quiz subtitle vs filter — **FIXED** (Smoke: Arc A “4 decks · 32 questions”; all “16 decks · 128 questions”)
3. `#quiz-status` after practice answer — **FIXED** (A11y live non-empty polite status)
4. Theme `aria-pressed` — **FIXED** (A11y)
5. Skip/`main` markup pack-wide (chrome + all 16 lessons) — **mostly FIXED**; live **focus move** after Skip still PARTIAL
6. Sibling Open*.bat — **improved** (Risk: now call `open-http.ps1`); residual if Python missing / raw `file://`

**Still open (not ship-blockers on HTTP):**
1. Steelman “Your steelman” label click does not focus `#text` (A11y FAIL — Pass 2 residual)
2. Skip link scrolls but leaves `activeElement` on `BODY` (A11y PARTIAL)
3. HTTP vs `file://` progress residual when Python unavailable (Risk R3-02)
4. Exploratory minor: raw `.md` dossier/ops UTF-8 mojibake in Chrome; ops checklist weak on Practice tools grid
5. Usability minor: Arc A/B script form denser than Arc C lists / Arc D tables; decorative arc-head `alt=""` residual
6. Risk P3: Fermi option values still `body`/`blood` (labels correct)

**Performance:** No regression vs Pass 2 on localhost despite ~140 KB / 128-Q bank and larger lessons.

**CLI fix brief:** **Not required** — no new P0s. Optional polish brief only if you want the residuals above fed to coding CLI.

---

## 2. Report inventory (Pass 3)

| Methodology | File | Headline |
| --- | --- | --- |
| Smoke & Sanity | `smoke-sanity-PASS3.md` | **11/11 PASS**; 16-lesson path; decks none blocked; subtitles match; labs×4; reset keeps theme |
| Exploratory (SBTM) | `exploratory-sbtm-PASS3.md` | Charter **Yes** (week-in-arc + facilitation script); dossier + ops noted; P3-F1 Minor / P3-F2 Nit |
| Boundary & Equivalence | `boundary-equivalence-PASS3.md` | **15 PASS / 0 product FAIL**; deck A1–A7; sizes 8–128; unanswered no inflation |
| Usability Heuristics | `usability-heuristics-PASS3.md` | Atlas / scripts / arc heads **PASS**; 0 critical/major |
| Accessibility WCAG | `Accessibility_WCAG_PASS3.md` | quiz-status / dim badges / aria-pressed **PASS**; skip/main **PARTIAL**; steelman label **FAIL** |
| Risk-Based | `risk-based-PASS3.md` | Id alignment + 128-Q load + links **pass**; no P0 regressions; R3-02 file:// residual |
| Performance | `performance-observation-PASS3.md` | Instant / &lt;0.5s localhost; **no perf regression** |
| **This delta** | `SPONSOR_DELTA_PASS3_Atlas_Study_Pack_2026-09-15.md` | Lead rollup |

Evidence: `exploratory-evidence/`, `evidence/`, pack `docs/screenshots/2026-09-15/pass-3/`.

---

## 3. Pass 2 → Pass 3 deltas (what changed)

| Pass 2 item | Pass 3 |
| --- | --- |
| Product shape | **7-lesson primer → 16-lesson / four-arc field atlas** (new stems + `bl-a*`…`bl-d*` deck ids; 128 Q) |
| Dim `.badge` contrast ~1.81:1 | **Closed** (A11y measured AA+) |
| Hardcoded “7 decks · 56 questions” subtitle | **Closed** (filtered subtitle correct) |
| `#quiz-status` announce unconfirmed | **Closed** |
| Theme `aria-pressed` | **Closed** |
| Skip/`main` uneven | Markup **pack-wide**; live focus move **still open** |
| Open*.bat `file://` | **Improved** via `open-http.ps1`; Python/`file://` residual remains |
| Steelman label → textarea focus | **Still open (FAIL live)** |
| Empty decks → all / Steelman domain / unanswered inflate / reset theme | **Still fixed** (no regression) |
| Usability majors | Still **0** |
| Localhost performance | Still strong; bank/lessons larger, feel unchanged |

---

## 4. Lead consensus — focus charters

| Focus | Lead verdict | Primary evidence |
| --- | --- | --- |
| Begin → Cover (4 arcs) → Contents (16) → L01–L16 boundaries | **PASS** | Smoke 1–4 |
| Decks: none / Arc A / all + subtitle | **PASS** | Smoke 5–7; Boundary A1–A7 |
| Labs ×4 + dashboard new stem + theme + reset | **PASS** | Smoke 8–11 |
| Week-in-arc + facilitation script | **PASS** (charter Yes) | Exploratory |
| Deck query + sizes 8…128 + unanswered unique count | **PASS** | Boundary |
| Contents as atlas; scripts; arc heads L/D | **PASS** | Usability |
| Skip/main; quiz-status; dim badges; steelman label; aria-pressed | **3 PASS / 1 PARTIAL / 1 FAIL** | Accessibility |
| Lab↔quiz ids; HTTP vs file://; 128-Q; outbound links | **Ids/links/load PASS**; file:// residual | Risk |
| First quiz + large lessons perf | **PASS** | Performance |

---

## 5. Findings rollup (non-P0)

| ID | Severity | Source | Notes |
| --- | --- | --- | --- |
| Steelman label → `#text` focus | Serious (a11y residual) | Accessibility | Markup `for`/`id` present; live click fails |
| Skip activate leaves focus on BODY | Moderate | Accessibility | Scroll works; focus move missing |
| file:// / no-Python progress | P2 residual | Risk R3-02 | Prefer HTTP; document louder |
| Raw `.md` UTF-8 mojibake | Minor | Exploratory P3-F1 | Case dossier / ops in Chrome |
| Ops not on Practice tools grid | Nit | Exploratory P3-F2 | Linked elsewhere |
| Script form consistency Arc A/B vs C/D | Minor | Usability | Still runnable |
| Arc-head `alt=""` | Minor residual | Usability | Decorative |
| Fermi `body`/`blood` values | P3 | Risk | Labels OK |

**New P0 count: 0.**

---

## 6. Disposition

| Question | Answer |
| --- | --- |
| Pass 3 complete? | **Yes — 7/7** |
| Ship 16-lesson atlas under HTTP? | **Yes** |
| Old 7-lesson primer still under test? | **No — out of scope; not present in live UI** |
| CLI P0 fix brief needed? | **No** |
| Optional next polish? | Steelman label focus; skip focus move; file:// banner; dossier HTML wrappers; Fermi rename |

---

## 7. Paths

```
/workspace/qa-reports/pass-3/
  smoke-sanity-PASS3.md
  exploratory-sbtm-PASS3.md
  boundary-equivalence-PASS3.md
  usability-heuristics-PASS3.md
  Accessibility_WCAG_PASS3.md
  risk-based-PASS3.md
  performance-observation-PASS3.md
  SPONSOR_DELTA_PASS3_Atlas_Study_Pack_2026-09-15.md
  PASS3_BRIEF.md
  exploratory-evidence/
  evidence/
```

Pack screenshots: `/workspace/atlas-study-pack/pack/docs/screenshots/2026-09-15/pass-3/`

---

*Compiled by QA/Tester Lead for sponsor Jenner — Pass 3 complete 2026-09-15 PT.*
