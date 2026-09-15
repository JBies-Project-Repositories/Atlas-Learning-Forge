# Atlas of the Build Loop — Study Pack

Offline field guide: loops, methods, intent, brainstorming, prototyping, review, and shipping.

## Open

**Preferred (shared progress):** double-click **`00_CLICK_HERE_TO_BEGIN.bat`**. If Python is installed it starts `http://127.0.0.1:8765/` so quiz, labs, and dashboard share the same origin.

You can also serve the folder yourself:

```text
python -m http.server 8765
```

then open `http://127.0.0.1:8765/00_CLICK_HERE_TO_BEGIN.html`.

**File open:** double-click `00_CLICK_HERE_TO_BEGIN.html`. Chromium may treat each `file://` page as a separate origin, so progress on the quiz may not show on the dashboard. Use HTTP if that happens.

`Open Home.bat`, `Open Dashboard.bat`, `Open Labs.bat`, `Open Quiz.bat`, and `Open Deck Chooser.bat` open `http://127.0.0.1:8765/...`. They start the same local server if it is not already running (Python required).

## Inside

| Surface | What it is |
| --- | --- |
| `index.html` | Cover |
| `contents.html` | Lesson map and suggested path |
| `02_lessons/` | Sixteen lessons in four arc-packs (markdown + HTML) |
| `decks.html` / `03_quiz/` | 8 questions × 16 lessons |
| `04_labs/` | SRS, Scenario Audit, Term Match, Steelman |
| `dashboard.html` | This-browser progress |
| `01_source/` | Config, curriculum, integrity, wrap.py |

## Keys

Progress uses `atlas_build_loop_*_v1` in localStorage. Reset from the dashboard.

## Mirror

Desktop copy is the learner pack. The same tree is mirrored in the GitHub repo at `pack/` so process commits and Desktop stay in sync.
