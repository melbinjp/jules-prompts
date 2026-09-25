# Keep a Project Confidential, Offline First: short form

To keep a private or proprietary project's code, data, designs and plans inside the places the owner chose, whether it is built fully offline with local agents and models or has to use the internet. Every channel that can carry the work out (hosting, sync, agents and model providers, registries, telemetry, crash reports, searches) is mapped, closed or controlled, and checked in a network log. The whole pipeline is proved to run with the network off.

For small or local models with a short context. The full skill, with the reasons and methods behind each rule, is `skills/keep-it-confidential/SKILL.md`; use it whenever the context allows. Works in any harness, needs no hosted service, and sends nothing beyond the project's confidentiality rules.

Fill in: `<WHAT_MUST_STAY_PRIVATE>`

## Objective

Make the project's confidentiality something observed rather than assumed:

- the owner's rules, class by class, for what may go where;
- every channel through which the work can leave, mapped, and each one closed or controlled;
- the whole pipeline, agents included, proved to run with the network off;
- where the internet must be used, a way of using it that reveals as little about the work as possible;
- a log of what actually left, reconciled with the map.

This protects the owner's own work. It is not a way around anyone's rules: stay within the law and the terms of every service used.

## Rules

- Classify first, with the owner.
- Map every channel the work can leave through, and give each a verdict.
- Prove the pipeline runs with the network off.
- Run the work on local tools where the class requires it.
- Where a remote agent or model is allowed, give it the least.
- When the internet must be used, use it so that what leaves reveals as little as possible.
- Strip what identifies the project from everything that goes out.
- Watch the egress, and reconcile it.
- When something has leaked, contain it.
- Do not claim what you did not check.

## Steps

1. Classify. Agree the classes and their destinations with the owner, and write them down.
2. Map. Read every configuration, then run a logged session, and fill in the channel map.
3. Close and control. Move each class's work to the tools it requires, and fix each channel.
4. Unplug. Block egress and run every stage from a clean checkout.
5. Set the gate. Agree how the internet is used when it must be, and who fetches what.
6. Log again. Run a session with egress logged, and account for every destination.
7. Verdict. Fill in the table.

## Deliver

- `CONFIDENTIALITY.md`: the classes, where each may go, and the internet gate.
- The channel map: channel, what it sends, to whom, verdict, and evidence.
- The offline run, stage by stage, from a clean checkout with egress blocked.
- The egress log and its reconciliation with the map.
- The residual exposures, each accepted by the owner in writing.
- A verdict table with one row per channel and per stage.
- Last line, the denominator: `17 holds, 2 broken, 1 skipped of 20 items.`
