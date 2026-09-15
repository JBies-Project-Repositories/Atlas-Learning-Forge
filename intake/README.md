# Intake — 2026-09-15

Received from Jenner in the Grok Build session. Snapshot only. The pack has not been built. COURSE CONFIG is not filled. Phase 0 has not started.

## Files

| Path | Source | Role |
| --- | --- | --- |
| `prompts/01_Atlas_Universal_Learning_OS_Master_v3.md` | `Grok Builder CLI 1.0 prompts/` | Create-only Atlas master prompt (v3.0.0) |
| `intake/target.txt` | `Desktop/Base/target.txt` | Syllabus / spine seed for this run |

## Target syllabus (seed units)

1. The loop
2. Project management methodology
3. Communicating intent
4. Brainstorming
5. Prototyping
6. Review
7. Iteration and shipping

Seven named units. Master v3 default is a 6–10 lesson comprehensive pack. This seed can carry that without inventing a second subject.

## Gate 0 still red (not yet a run)

Master v3 requires at least:

- `material_name`
- `parent_dir`
- sources **or** authored topic / lessons list

None of those are filled. Do not invent a Mastery showcase. Do not write a pack folder until Jenner confirms identity and path.

## Proposed fill (not applied)

```yaml
material_name: ""          # Jenner to name; seed suggests a build-loop / shipping-practice field guide
course_name: ""            # empty → "Atlas of {material_name}"
parent_dir: ""             # Jenner to name; create-only new folder
input_mode: source_locked
spine_policy: auto_from_sources
auto_confirm_spine: true
sources:
  - type: syllabus
    path: intake/target.txt
    label: "Build-loop field guide seed"
```

## Next process step

Confirm `material_name` and `parent_dir`, then either refine the prompt or begin Phase 0.
