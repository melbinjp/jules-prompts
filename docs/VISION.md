# Vision: complete systems, whoever drives them

Written 2026-09-29. The owner's aim: anyone, with no experience, can take an idea to a complete,
production-quality system, and the skill of the person driving it has as little effect on the
result as possible. This file records where the conductor stands against that aim, and what has
to change to reach it.

## Where it falls short today

1. **It is instructions, not enforcement.** An agent can skip a step it clearly asks for. In the
   trials, agents left work items without owners, skipped a written handover, and printed before
   a booking was confirmed, although the conductor says not to.
2. **Results vary between runs.** The same case, the same model and the same conductor gave
   different outcomes. A single run is not a reliable result.
3. **Judgement is still needed.** A beginner cannot tell a sound design, supplier or finding from
   a weak one. The conductor tells them to check and record, but cannot supply the judgement.
4. **Standards are summarised, not applied in full.** The working rules of ISO 21502, ISO/IEC
   25010, OWASP ASVS, SLSA and WCAG are written in, which is enough to work from but not to certify.
5. **Compliance needs people.** Electrical, radio, medical, food and legal sign-off needs a
   qualified person or an accredited body. The conductor marks these pending; it cannot do them.
6. **The world is outside it.** Suppliers, budgets, hardware and people fail in ways no
   procedure covers. The conductor makes such failures visible; it does not prevent them.
7. **The evidence is thin.** One real software delivery, simulations for physical and event work,
   and no real product carried from idea to operation yet.

## What reaching the aim needs

- **Move rules from prose into checks that run.** Every rule that can be checked mechanically
  (owners and acceptance on every work item, a test seen to fail, a handover present before close,
  spend within budget, nothing sent outside authority) becomes a check in the project's own
  pipeline that blocks progress when it fails. The person and the agent then cannot skip it.
- **Independent review by default.** Every result is checked by a second agent that did not build
  it, on a different model where possible, and a disagreement is surfaced to the owner.
- **Repeat what matters.** Consequential steps run more than once and the results are compared,
  so one unlucky run does not decide the outcome.
- **Established defaults for every choice a beginner cannot judge.** For each common decision
  (stack, hosting, supplier type, test approach), a vetted default with its reason and its limits,
  so the beginner only confirms or overrides.
- **Built-in hand-offs to qualified people.** The points where a qualified person is required are
  named in the plan from the start, with what they must check, so they are booked, not discovered.
- **Standards applied from the source when a claim is made.** For any conformity claim, the agent
  works from the named edition of the standard and records each requirement against evidence.
- **Real projects as evidence.** Carry several real projects, software, physical and service, from
  idea to operation, and record what failed.

## Our view

The aim is right, and it should be pursued, but it should be stated precisely. No procedure can
make the result independent of the people and the world around it. What it can do is shrink the
person's role to the decisions only they can make: what the project is for, what it may spend,
what it may send or sign, and what they accept. Everything else should be checked by something
that runs, not by the reader remembering. The largest single step toward that is the first item
above: turn the conductor's checkable rules into checks that block. Until then the honest claim is
that the conductor raises the floor and makes gaps visible; it does not yet make quality automatic.
