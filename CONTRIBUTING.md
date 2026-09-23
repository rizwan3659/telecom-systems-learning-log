# Updating my learning record

## One source of truth

Edit `progress.json` for technical status. The Markdown dashboard and showcase are generated from it. Daily GitHub issues are work checklists; their open/closed state is not synchronized automatically. The progress records are authoritative.

Allowed statuses: `not_started`, `in_progress`, `blocked`, `done`.

For a task in progress, set `status`, `updated` (YYYY-MM-DD), and a concise `notes` value. For blocked work, explain the failed layer and next diagnostic step in `notes`. For done work, fill its template, set `evidence_ready` to `true`, add an actual evidence link, fill `result` and `limitations`, and set the completion date. A template placeholder does not count as evidence.

## End-of-day commands

Run from a clone of this repository with Python 3 available (`python3` or your platform's `python`):

```sh
python scripts/update_progress.py
python scripts/update_progress.py --check
git status --short
git diff
```

Stage named files deliberately, inspect them, then commit and push. Example for an actual completed scope note:

```sh
git add progress.json PROGRESS.md weeks/week-01/SHOWCASE.md weeks/week-01/deliverables/D01-scope.md
git diff --cached
git commit -m "docs(week-01): record scope and acceptance criteria"
git push
```

Do not use that example commit as proof of a technical lab outcome. Use `docs(week-01): record blocked SCTP setup` or `lab(week-01): document validated registration run` only when true.

## Evidence workflow

Keep raw run artifacts under an ignored local `runs/` folder or another private location. Publish small reviewed excerpts and the commands/environment required to interpret them. Replace `TEMPLATE — not evidence yet` in a completed template with your actual result. Store reviewed screenshots in `weeks/week-01/evidence/` and link them relative to the deliverable. Do not include credentials in screenshots.

At the end of a day, comment on its own issue with what you learned, evidence links, hours and blockers; close it only if that day's acceptance checks pass. If you finish part of a day, keep the issue open and commit the partial evidence honestly.

The script validates status data, local links, completion metadata and whether generated pages are current. It cannot judge technical correctness or verify that you actually ran an experiment.
