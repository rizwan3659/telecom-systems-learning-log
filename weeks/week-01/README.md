# Week 1 — a baseline I can demonstrate

**Budget:** 40 work hours: 7 planned task hours + 1 buffer hour per day. Breaks are outside these work blocks.

**Finish line:** explain a simulated UE registering, creating a PDU session and sending/receiving traffic through the correct path, with a controlled repeat and published evidence.

| Day | Main output | Work blocks | Guide |
|---|---|---|---|
| 1 | Scope, starting point, topology | 2h + 2h + 2h + 1h + 1h buffer | [Day 1](days/day-01.md) |
| 2 | Environment, revisions, recovery state | 2h + 2h + 2h + 1h + 1h buffer | [Day 2](days/day-02.md) |
| 3 | Builds, tests, configuration agreement | 2h + 2h + 2h + 1h + 1h buffer | [Day 3](days/day-03.md) |
| 4 | Registration, session, user traffic | 2h + 2h + 2h + 1h + 1h buffer | [Day 4](days/day-04.md) |
| 5 | Timeline, source walk, repeat, demo | 2h + 2h + 2h + 1h + 1h buffer | [Day 5](days/day-05.md) |

## What to publish

Use the [15 evidence templates](deliverables/) and [showcase](SHOWCASE.md). Each needs an observed result, exact environment/command where applicable, evidence and a limitation. An uploaded plan or empty template is not a completed deliverable.

Keep screenshots secondary to reproducible text. A concise command/result excerpt plus clear interpretation is often more useful than a desktop screenshot. Label failed and partial work accurately; useful debugging is learning too.

## Sources and prerequisites

- [Open5GS build guide](https://open5gs.org/open5gs/docs/guide/02-building-open5gs-from-sources/)
- [UERANSIM installation](https://github.com/aligungr/UERANSIM/wiki/Installation)
- [UERANSIM configuration](https://github.com/aligungr/UERANSIM/wiki/Configuration)
- [UERANSIM usage](https://github.com/aligungr/UERANSIM/wiki/Usage)

Use OS/revision-appropriate upstream instructions; a universal installation command is not assumed. The lab uses simulation and does not prove real RF or commercial VoNR performance. No running lab is supplied by this planning repository.

## When blocked

Record expected/actual behavior, minimal reproduction, first failing layer and next discriminating check. Change one variable at a time. After 90 minutes without a narrower explanation, simplify and write a blocker note. Move dependent tasks rather than adding hours or starting a different project.

## Work publication

Follow [the update procedure](../../CONTRIBUTING.md). The dashboard is authoritative for progress. Daily issues are editable checklists; link results and close them manually when complete.
