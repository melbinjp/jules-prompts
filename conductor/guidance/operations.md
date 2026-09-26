# Operations: keeping what runs working, and getting better

Load for anything that keeps running after delivery (a service, an installation, a product in
people's hands, a recurring event), and whenever something live fails the people who use it.
Operations belong to a named operator (`../SKILL.md §9. Closure and handover`).

## Handover to operations

- **Use `../templates/handover.md`.** The operator named, and their responsibilities; the
  resources and budget; the procedures (start, stop, deploy or update, back up and restore, roll
  back, the restoring actions for incidents); the measures and where each is taken; the review
  cadence and the triggers that call for action; the contacts and suppliers; access transferred
  and keys rotated; credentials held by the owner, not by an agent.
- **Walk the operator through one run of each critical procedure and one periodic review.**
- **Tell the people who use it** who now looks after it and how to reach them.

## Periodic review

Projects rarely fail on one day; they drift or stall, one unexamined month at a time. Run a review
at every milestone and on the operator's cadence (a sensible default is weekly in the first month
after launch, monthly after that, and more often while a measure is off target). With no earlier
review, review against the objective and measures alone and say so.

1. **Take every measure again from its source** (logs, analytics, invoices, sensor data, the support
   queue, reviews, the attendance count), the way the measure says it is taken. Record the value,
   the target, the change since the last run, and the evidence. Never carry a number forward from
   an earlier report; a measure not taken from its source is not a measure.
2. **Evaluate every switch condition and every decision's reopening condition** with today's numbers
   (`product.md §Alternative routes`, `decisions.md §A way out and a reopening condition`).
3. **Find what nothing serves any more:** work that serves a superseded or rejected decision, or
   nothing (code, jobs, services, dependencies, configuration, accounts, subscriptions, rented
   equipment), found through the records and through the project's own tools (unused dependencies,
   unreachable code, unread configuration, dead routes, flags past their date); and features
   nobody uses, from the usage data. Remove each through a change, or record its reason. Everything
   nobody needs is paid for again every month.
4. **Check the money and every other resource** (`planning.md §Resources and their sources`).
5. **Run every procedure both ways:** the person's documented path from a clean start, and the
   agent's or automation's path. A procedure only one of them can do is broken (a renamed script
   nobody noticed because an agent releases through its own tool).
6. **Restore a backup and try a rollback** whenever the schedule says (§Backups and restore).
7. **Check every incident since the last review** has its cause proved, its prevention recorded, and
   its restoring action drilled (§After an incident).
8. **Re-qualify agents and reconcile egress** where agents run the work (`autonomy.md §Routing work
   to agents`, `confidentiality.md §Proving it`); show the owner the choices made on their behalf
   since the last review (`autonomy.md §Choices on the owner's behalf`).
9. **Look outside** (§Upkeep), and **hear the people who use it** (`product.md §Hearing back`).
10. **Choose the next improvements:** rank the candidates by the measure each moves, how far it is
    from its target, how many people it affects, and what it costs; take the top ones into the next
    milestone as changes. When a measure has held its target for a while, raise it or add the next
    measure, with the owner.
11. **Set the course, with the evidence and a recommendation; the owner decides:**
    - continue: the measures are moving; name the next milestone;
    - adjust: a measure, target, milestone or decision changes, with the reason recorded;
    - re-route: a route is blocked; switch to another approach, channel, supplier, design or funding
      route that reaches the same objective;
    - grow: the objective holds; propose the next objective as a new project;
    - pause: keep security updates, backups and the data people rely on running, and record what
      restarts it.
12. **Record the review** in the project's records: every row with its value now, the target or
    condition, the evidence and its verdict; the removals; the ranked improvements; the course.

## Incidents: restore first

When a live product or service fails the people who use it, restoring comes before understanding.
The first hour spent on logs and theories while everyone meets the failure, with a two-minute
rollback unused, is the failure this prevents.

1. **Take charge, and keep a timeline.** One person or agent is in charge; everyone else works through
   them. From the first minute, record with times what was seen, what was done and what happened
   next. Start from the alerts, the error logs and the help route: what is failing, for whom, since
   when.
2. **Stop the harm to data and to people first:** pause the worker, block the route, stop retries of
   anything not safe to repeat, put devices in their safe state. Take a snapshot before any repair
   touches data. An outage costs time; corrupted data costs trust.
3. **Restore by the fastest action already tried:** roll back the last change, turn off the feature
   behind its flag, fail over, restore from a backup onto a copy first, or put devices in a safe
   state. Prefer an action that has been tried before and can itself be undone. Confirm the critical
   journeys are back by walking them, not by the graph alone. If no restoring action exists, record
   that one is missing.
4. **Tell the people affected, early and in their words:** what is affected, what to do meanwhile, and
   when the next update will come, where they look (the status page, the product, their channel).
   Update when promised; say when it is over and what happened. Sending to people is within the
   standing limits for publishing.
5. **Keep the evidence before it disappears:** copy the logs, traces, data state and configuration
   from the window of the incident before rotation or a restore overwrites them; record which change
   was live.
6. **Agents on duty act within limits set in advance.** The briefing names the restoring actions an
   agent may take on its own (roll back, turn off a flag, pause a job, a safe state) and everything
   beyond them it may not. An agent never silences an alert, disables a check, deletes data, or
   retries an unsafe action to make a symptom go away. When its restoring actions are not enough, it
   takes the safest one and reaches the person by the route the briefing gives.
7. **Look for the cause after service is back, on a copy,** not in production while people wait.

## After an incident

1. **Find the cause, not the trigger, and prove it:** reproduce the failure in a test that fails, on a
   copy. Ask why until the answer is something in the system (a missing check, an unsafe retry, an
   alert that did not exist, a rollback nobody had tried), never a person's mistake. Name the check
   that should have caught it, and why it did not.
2. **Fix through the normal gates:** a test seen to fail without the fix, the gates run, a review by
   someone other than the author. Only the restoring action itself may skip the gates, and it must be
   one that was already tried. A hot fix with the checks skipped is the next incident.
3. **Put right what the incident did to people:** count every person, record and device affected,
   from the data, not the error graph; refund, restore, resend or recover each one, and check each
   was put right. It is not over while anyone is still harmed.
4. **Close the class, in the system:** for the cause and for each thing that made the incident longer
   (slow detection, a missing rollback, lost evidence, nobody told), add a test, an alert that fires
   before a person reports it, a limit, an idempotency key, or a tried procedure; record each against
   what it protects; schedule a drill of the restoring action. No action item may be "be more
   careful": the system changes, not the person.
5. **Record the review:** the timeline with times, the restoring action and when it was last tried,
   the messages sent, the evidence kept, the cause and its test, the fix, the people put right, the
   prevention, and the time to detect and to restore.

## Backups and restore

- **A backup nobody has restored is not yet a backup.** Restore on a schedule, into a scratch copy,
  and check the restored data is usable (the application starts on it, the counts match).
- **Backups are verified by their effect:** size, count and a restore, not the job's exit code
  (`software.md §Automations that report their own failure`).
- **Restore onto a copy first during an incident,** never over newer data.
- **Know where every piece of state lives and what writes it** (`quality.md §Walk every area`).

## Upkeep

- **On the operator's cadence:** security advisories for what it uses; dependencies, platforms, parts
  and certificates near their end of life or expiry; changes in law or platform rules that apply (app
  stores, certification, privacy); new parts, services and techniques that would serve the objective
  better, recorded as options.
- **Dependencies are kept current in small steps,** so no update is ever large
  (`software.md §Dependencies`); physical equipment is serviced on its schedule, with spares
  checked.
- **Keep it able to continue, whoever runs it:** the records, the procedures and notes are enough for
  a new person, agent or team to pick it up; credentials are held by the owner.
