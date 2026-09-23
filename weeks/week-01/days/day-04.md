# Day 4 — Registration, session and actual user-plane traffic

**Budget: 7 task hours + 1 hour buffer.** All checkboxes start unchecked. Complete them only when the work is actually performed.

## A — Core readiness (2h)

- [ ] 0-30m: create a run ID and note configuration hashes.
- [ ] 30-60m: start database and required core functions following the selected setup.
- [ ] 60-90m: verify actual listeners/readiness and record failures.
- [ ] 90-120m: check UPF data-endpoint routing and readiness; add precise evidence locations to D10.

## B — gNB connection (2h)

- [ ] 0-30m: verify gNB AMF address and intended namespace.
- [ ] 30-60m: start the simulated gNB; collect setup logs/capture.
- [ ] 60-90m: distinguish transport failure from protocol/config rejection.
- [ ] 90-120m: record the observed setup outcome in D10; troubleshoot only the first failing layer.

## C — UE registration and PDU session (2h)

- [ ] 0-30m: provision one synthetic subscriber privately and check UE agreement.
- [ ] 30-60m: start UE and record registration evidence.
- [ ] 60-90m: record session request/outcome separately from registration.
- [ ] 90-120m: record assigned UE address/interface and visible session identifiers in D11; mark unavailable fields explicitly.

## D — Traffic proof (1h)

- [ ] 0-15m: select a controlled IP endpoint and confirm the probe source uses the UE interface.
- [ ] 15-40m: send traffic and observe it at the UE and user-plane path, including replies.
- [ ] 40-60m: publish a sanitized command/result/capture reference in D11; explain why host-network bypass was excluded.

## E — Review and buffer (1h)

- [ ] Use remaining time for the earliest blocked prerequisite; do not add features.
- [ ] Record hours, observed learning, unresolved question and next action in the daily journal.
- [ ] Review evidence for sensitive data, update progress and publish a small truthful commit.

## Deliverables to show

- [D10: Core/gNB readiness and UE registration evidence](../deliverables/D10-registration.md) — Link one run and show readiness, gNB setup and registration as separate evidenced results.
- [D11: PDU session and traffic evidence](../deliverables/D11-session-traffic.md) — Show session/address evidence plus return traffic through the UE/UPF path, excluding host-route bypass.

## Exit check

Registration, session and bidirectional traffic each have separate evidence; ordinary host connectivity is not presented as UE traffic.

If the gate fails, mark the relevant item blocked/in progress and state why. Do not check the issue complete just because the day ended.

## Public learning post template

Today I investigated **[question]**. I observed **[fact]** using **[evidence link]**. My earlier assumption **[changed/stayed valid]** because **[reason]**. The current limitation is **[limitation]**. Next I will test **[one hypothesis]**.

## My journal

- Actual hours: not recorded
- Learning: not recorded
- Evidence links: not recorded
- Blocker / next action: not recorded
