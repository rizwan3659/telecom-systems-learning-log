# Day 2 — Environment, capabilities and pinned versions

**Budget: 7 task hours + 1 hour buffer.** All checkboxes start unchecked. Complete them only when the work is actually performed.

## A — Inspect the Linux environment (2h)

- [ ] 0-30m: collect OS, kernel, architecture and resources using read-only commands in the PDF.
- [ ] 30-60m: record interfaces, routes, virtualization mode and console recovery.
- [ ] 60-90m: inspect required tool availability; classify missing tools versus missing kernel capabilities.
- [ ] 90-120m: fill D04; redact irrelevant host/user details before committing.

## B — Validate the design (2h)

- [ ] 0-30m: inspect TUN availability and lab networking privileges; record actual outcomes.
- [ ] 30-60m: inspect SCTP support without assuming absence from loaded modules means unsupported.
- [ ] 60-90m: verify which addresses are reachable across host/guest/namespace boundaries.
- [ ] 90-120m: update D03 and D04, marking application connection checks pending until Day 4.

## C — Choose versions and prerequisites (2h)

- [ ] 0-30m: read official setup guidance for your OS.
- [ ] 30-60m: choose explicit core and simulator commits/releases, then record full hashes.
- [ ] 60-90m: record compiler/build tools and required database/library versions.
- [ ] 90-120m: create D05 compatibility rows; say runtime compatibility is untested.

## D — Preserve a build starting point (1h)

- [ ] 0-20m: record checkout, config, binary and log locations.
- [ ] 20-40m: save a VM snapshot or write a recovery procedure appropriate to the environment.
- [ ] 40-60m: fill D06 with persistence/reboot behavior; publish the reviewed manifest and progress.

## E — Review and buffer (1h)

- [ ] Use remaining time for the earliest blocked prerequisite; do not add features.
- [ ] Record hours, observed learning, unresolved question and next action in the daily journal.
- [ ] Review evidence for sensitive data, update progress and publish a small truthful commit.

## Deliverables to show

- [D04: Environment and capability manifest](../deliverables/D04-environment.md) — Record OS/kernel/resources, networking mode and TUN/transport checks without claiming untested support.
- [D05: Pinned version and dependency ledger](../deliverables/D05-versions.md) — Record full revisions, compiler/build tools, documentation references and known compatibility gaps.
- [D06: Ready-for-build state and restore notes](../deliverables/D06-reproduction-state.md) — Explain source/config/log locations, snapshot or recovery method and reboot persistence.

## Exit check

The environment can be reached and recovered; versions are fixed and no known capability blocker is hidden.

If the gate fails, mark the relevant item blocked/in progress and state why. Do not check the issue complete just because the day ended.

## Public learning post template

Today I investigated **[question]**. I observed **[fact]** using **[evidence link]**. My earlier assumption **[changed/stayed valid]** because **[reason]**. The current limitation is **[limitation]**. Next I will test **[one hypothesis]**.

## My journal

- Actual hours: not recorded
- Learning: not recorded
- Evidence links: not recorded
- Blocker / next action: not recorded
