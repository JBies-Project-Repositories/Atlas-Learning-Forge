# QA Squad roster

Project: Atlas Learning Forge  
Created: 2026-09-15  
Source: QA/Tester Lead, 2026-09-15

No target app is assigned yet. Nothing has been tested.

## Lead

| Name | Role |
| --- | --- |
| QA/Tester Lead | Creates methodology-specific testing bots. Collects their markdown reports and compiles a formal sponsor report. |

## Testers

| Name | Method | What they do when a target app is named |
| --- | --- | --- |
| Smoke & Sanity Tester | Smoke and sanity | Short high-priority pass on critical paths (launch, auth if present, main navigation, one happy-path action per core feature). Fixed checklist. No deep-dive. |
| Exploratory Session Tester | Session-based exploratory testing (SBTM) | Time-boxed sessions with a charter. Logs heuristics, surprises, bugs, questions, and follow-up charters. |
| Boundary & Equivalence Tester | Boundary value analysis and equivalence partitioning | Identifies input partitions and runs cases at min, just-below, just-above, max, and representative values. |
| Usability Heuristics Tester | Nielsen-style heuristic evaluation | Walks primary flows and scores issues against standard usability heuristics. |
| Accessibility WCAG Tester | WCAG-oriented accessibility | Checks keyboard-only use, focus order, labels, contrast where observable, alt text, headings, form errors, and visible ARIA misuse. |
| Risk-Based Tester | Risk-based testing | Builds a risk register (impact × likelihood), tests the highest risks first, and records residual risk. Does not start until a target app is named. |
| Performance Observation Tester | Lightweight performance observation | Notes perceived load time, jank, slow navigation, and heavy interactions during primary flows. No load or denial-of-service testing. Does not start until a target app is named. |

## Channels (cap of six members)

| Channel | Members |
| --- | --- |
| QA Squad | Lead, Smoke & Sanity Tester, Exploratory Session Tester, Boundary & Equivalence Tester, Usability Heuristics Tester, Accessibility WCAG Tester |
| QA Squad Extended | Lead, Risk-Based Tester, Performance Observation Tester |
