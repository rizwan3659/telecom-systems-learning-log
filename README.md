# Telecom Systems Learning Log

A public record of what I learn, build, test and can explain about telecom systems reliability.

**Current focus: Week 1 — one reproducible simulated 5G standalone lab.**

The objective is to show UE registration, PDU-session establishment and traffic through the intended user-plane path, backed by reproducible evidence. This repository starts with a plan and blank evidence templates. **No lab success, benchmark result or completed learning is claimed yet.**

## Start here

- [Progress dashboard](PROGRESS.md) — status, acceptance criteria and evidence for 15 deliverables.
- [Detailed Week 1 plan](weeks/week-01/README.md) — 40 hours, five days, exact outputs.
- [Deliverable showcase](weeks/week-01/SHOWCASE.md) — the results a visitor should inspect.
- [Daily guides](weeks/week-01/days/day-01.md) — begin with Day 1.
- [Printable Week 1 guide](docs/Week_1_Public_Learning_Plan.pdf).
- [How I update progress](CONTRIBUTING.md).

## My daily task board

Use the issues to check off steps and record daily learning. Update `progress.json` separately when evidence is ready; closing an issue does not change the dashboard automatically.

| Day | Task checklist | Deliverables |
|---|---|---|
| 1 | [Scope, starting point and topology](https://github.com/rizwan3659/telecom-systems-learning-log/issues/1) | D01-D03 |
| 2 | [Environment and pinned versions](https://github.com/rizwan3659/telecom-systems-learning-log/issues/2) | D04-D06 |
| 3 | [Builds, tests and configuration](https://github.com/rizwan3659/telecom-systems-learning-log/issues/3) | D07-D09 |
| 4 | [Registration, session and traffic](https://github.com/rizwan3659/telecom-systems-learning-log/issues/4) | D10-D11 |
| 5 | [Timeline, source walk and repeat](https://github.com/rizwan3659/telecom-systems-learning-log/issues/5) | D12-D15 |

## How to read this work

`Not started` means a template exists but the work has not been demonstrated. `In progress` means work is underway. `Blocked` names an unresolved prerequisite. `Done` requires a linked evidence artifact, completed acceptance checks and an honest limitations statement.

Planning materials are available. Technical progress is tracked separately. CI checks repository/progress consistency; it does **not** execute or validate the 5G lab. Self-reported completion is not independent verification.

## Public evidence policy

Publish synthetic or sanitized examples, environment versions, relevant test summaries, diagrams and clear explanations. Keep raw captures, subscriber authentication keys, tokens, private addresses where sensitive, employer data and unreviewed logs out of this repository. Ignored paths are a convenience, not a substitute for inspecting every staged change.

## Working rhythm

1. Read the day's guide and start its issue/checklist.
2. Perform one task and save raw evidence privately.
3. Fill the corresponding public evidence template.
4. Update `progress.json`, regenerate the dashboard and inspect the diff.
5. Commit and push a small, truthful update. Link the commit in the day issue.

Future weeks will be added when needed. The current scope is deliberately Week 1 only.
