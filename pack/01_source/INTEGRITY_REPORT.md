# INTEGRITY_REPORT — Atlas of the Build Loop

**Date:** 2026-09-15  
**course_root:** `/mnt/c/Users/jbies/OneDrive/Desktop/Atlas of the Build Loop — Study Pack`  
**mirror:** `/home/jbies/Atlas-Learning-Forge/pack`

## Gate 0

- [x] `course_root` announced and new
- [x] `material_name` = the Build Loop; title = Atlas of the Build Loop
- [x] meta: 7 lessons with ids/titles/focus
- [x] seed 7 → final 7 (freeze; not an honest short subject)
- [x] sources normalized (`normalized/target.txt`); coverage-gap note in SOURCE_NOTES
- [x] storage keys unique (`atlas_build_loop_*_v1`); no Mastery/am-*
- [x] COURSE_CONFIG copied into `01_source/`

## Gate 1 — density (Lesson Content + worked examples)

| id | title | md | html | quiz | sections | words≈ | examples | terms | misc | figures |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bl-01-loop | The Loop | y | y | 8 | 6+ | 1885 | 1 | 10 | 8 | SVG y |
| bl-02-methods | Project Management Methodology | y | y | 8 | 6+ | 1265 | 1 | 12 | 8 | HTML y |
| bl-03-intent | Communicating Intent | y | y | 8 | 6+ | 1083 | 1 | 12 | 8 | SVG y |
| bl-04-brainstorm | Brainstorming | y | y | 8 | 6+ | 965 | 1 | 10 | 8 | HTML y |
| bl-05-prototype | Prototyping | y | y | 8 | 6+ | 1083 | 1 | 12 | 8 | SVG y |
| bl-06-review | Review | y | y | 8 | 6+ | 921 | 1 | 11 | 8 | HTML y |
| bl-07-ship | Iteration and Shipping | y | y | 8 | 6+ | 1038 | 1 | 10 | 8 | SVG y |

All lessons include objectives, prerequisites, skeleton, Learn more (no fabricated papers).

## Gate 2 / 2H

- [x] `00_CLICK_HERE_TO_BEGIN.html` + `.bat` + cover path
- [x] `contents.html` exists; cover does not dump every lesson card as the home
- [x] All lesson md+html for meta rows; prev/next + Cover/Contents
- [x] Quiz: 7 × 8; one correct each; distractors from that lesson’s misconceptions
- [x] Deck chooser lessonIds match bank and lab dropdowns
- [x] SRS = terms + misconception rows per lesson
- [x] Term Match = that lesson’s key terms
- [x] Scenario Audit: 120–200 words, ≥2 sound claims, 4–7 mapped errors, count not told
- [x] Labs + `shared.js` key = `atlas_build_loop_progress_v1`
- [x] Graders only on Scenario Audit + Steelman (live fill)
- [x] No weighted decision matrix
- [x] Profile absent
- [x] No foreign Mastery/am-* keys
- [x] Bats present; CRLF; `cd /d "%~dp0"`
- [x] SOURCE_NOTES + Curriculum + this report
- [x] No writes outside course_root (except git mirror copy)
- [x] Labeled charts are SVG/HTML
- [x] Named folder is the Atlas (no zip, no nested inner pack)
- [x] Comprehensive: contents + quiz + labs describe the final 7-lesson spine

## Labs

| File | Title | Grader |
| --- | --- | --- |
| spaced.html | Spaced Repetition | none |
| bias.html | Scenario Audit | live fill |
| fermi.html | Term Match | none |
| steelman.html | Misconception Steelman Studio | live fill |

## How to open

Double-click `00_CLICK_HERE_TO_BEGIN.html` → cover → Contents or Lesson 1.

## Mirror

Desktop pack is the learner copy. `Atlas-Learning-Forge/pack/` is the git mirror. Sync with `pack/../scripts` or rsync both ways after a change.
