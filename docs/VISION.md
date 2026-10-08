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
   and no real product carried from idea to operation yet. The fixtures now plant 168 defects.
   The trial scored 146. Defects planted after that run are not part of that result.
8. **One schedule rule is now a check. The other whole-result rules are still instructions.** A
   schedule record that states a date, a quarter or a duration with no source fails
   `scripts/check_time_limits.py`. That check has been shown to fail a planted schedule and to
   pass a sourced one.

   A whole project still requires a vision, a plan and a minimum on every applicable aspect.
   That includes the exchange when it must earn, what the record still misses, checkpoints after
   use has started, and the way the result is used. The minimum stays when the technology
   already in hand falls short. An agent can still skip those. They block nothing until they
   are checks that fail the run. Scoring a fixture finds a skipped rule only when someone runs
   the scorer.

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

## Commissioned production-system study and build task, 8 October 2026

The owner requests that the production stages and the current conductor's failures be made an
explicit part of the README, with private context removed, and that the development analysis be
prepared as an anonymised publication draft. The source is an Antigravity architectural
assessment dated 7 October 2026. The owner's subsequent direction is to retain only supported
facts and discard false critiques. Claims are checked against the underlying records and
primary research. The source names 17 stages; its 15 to 25 estimate is not a prescribed standard.

The [README section](../README.md#from-an-idea-to-a-production-system-the-next-build-task) carries
every named stage and its proposed acceptance evidence. The system goal is an ordered evaluation
that cannot advance past a failed or unverified applicable prerequisite. It must retain the
project's native authority, independent verification, delegated action limits and operating
feedback. Existing effective checks are retained; a state machine controls transitions but does
not prove the completeness or quality of its criteria.

Responsible for this package: documentation implementer, with independent source and reader
review. Acceptor: project owner. Acceptance: all 17 stages retained, limitations accurate, private
identifiers absent, and a concrete study/build deliverable distinguishable from delivered
runtime enforcement. Status: documentation and article reviewed; the owner authorised their
push and publication on 8 October. Release evidence belongs in `QUALITY.md`. Runtime
implementation and production acceptance remain open.

Next system work: inspect existing execution tools and checks, map each stage to a working gate
or a demonstrated gap, and propose the smallest missing mechanism on a bounded real project.
The demonstration must stop on a planted failure, preserve state across interruption and admit
only independently verified correction. Dates and resource commitments remain unset pending
the scoped implementation plan. The publication draft and its private provenance stay in the
workspace's existing draft records, outside this repository.

## Our view

The aim is right, and it should be pursued, but it should be stated precisely. No procedure can
make the result independent of the people and the world around it.

What it can do is shrink the
person's role to the decisions only they can make: what the project is for, what it may spend,
what it may send or sign, and what they accept. Everything else should be checked by something
that runs, not by the reader remembering.

The largest single step toward that is the first item
above: turn the conductor's checkable rules into checks that block. One schedule rule now does.
An unsourced date in a schedule fails the run. The others do not, until they are checks too.
Until then the honest claim is
that the conductor raises the floor and makes gaps visible; it does not yet make quality automatic.
