# Day 3 — Build both components and reconcile configuration

**Budget: 7 task hours + 1 hour buffer.** All checkboxes start unchecked. Complete them only when the work is actually performed.

## A — Core source build (2h)

- [ ] 0-30m: verify checkout hash and follow the OS-specific prerequisite instructions.
- [ ] 30-90m: build Open5GS; capture command, working directory, start/end and exit status privately.
- [ ] 90-120m: inspect first failures or record success in D07. Do not silently replace this build with a different version.

## B — Core tests (2h)

- [ ] 0-30m: identify documented test entry points and prerequisites for this revision.
- [ ] 30-90m: run applicable tests and save full local output.
- [ ] 90-120m: publish a small result summary with command, pass/fail/skip counts and missing capabilities in D07. A skip is not a pass.

## C — Simulator build (2h)

- [ ] 0-30m: confirm the pinned UERANSIM checkout and its build guidance.
- [ ] 30-90m: build and inspect the expected binaries/help output.
- [ ] 90-120m: fill D08 with actual outcomes and explicitly pending runtime verification.

## D — Configuration consistency (1h)

- [ ] 0-20m: select example configs for this revision; record provenance.
- [ ] 20-40m: compare PLMN, TAC, DNN, slice selection, transport addresses and synthetic subscriber agreement in D09.
- [ ] 40-60m: publish the agreement checklist without keys; record services/startup prerequisites.

## E — Review and buffer (1h)

- [ ] Use remaining time for the earliest blocked prerequisite; do not add features.
- [ ] Record hours, observed learning, unresolved question and next action in the daily journal.
- [ ] Review evidence for sensitive data, update progress and publish a small truthful commit.

## Deliverables to show

- [D07: Open5GS build and test report](../deliverables/D07-core-build.md) — Record exact revision, build/test commands, outcomes and separate failures/skips.
- [D08: UERANSIM build report](../deliverables/D08-simulator-build.md) — Record source revision, commands, binary/help checks and untested runtime behavior.
- [D09: Configuration agreement checklist](../deliverables/D09-config-check.md) — Reconcile core/gNB/UE settings with synthetic subscriber provisioning; publish no keys.

## Exit check

Build results and test outcomes are reproducible; the core/gNB/UE configuration agreement is documented without disclosing credentials.

If the gate fails, mark the relevant item blocked/in progress and state why. Do not check the issue complete just because the day ended.

## Public learning post template

Today I investigated **[question]**. I observed **[fact]** using **[evidence link]**. My earlier assumption **[changed/stayed valid]** because **[reason]**. The current limitation is **[limitation]**. Next I will test **[one hypothesis]**.

## My journal

- Actual hours: not recorded
- Learning: not recorded
- Evidence links: not recorded
- Blocker / next action: not recorded
