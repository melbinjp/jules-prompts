# Handover note template

For anything that keeps running after a project closes, or when a project changes hands. Kept with
the project's records; the receiving operator confirms each section by walking it, not by reading
it (`../SKILL.md §9. Closure and handover`, `../guidance/operations.md §Handover to operations`).

```markdown
# Handover: <what is handed over>

- From: <name>  To (operator): <name>  Date: <YYYY-MM-DD>
- Accepted by the operator: <name, date, after walking the procedures below>

## What it is and what it is for

<The objective in one sentence; the people who rely on it; what must never be lost.>

## Responsibilities

<What the operator is responsible for, what they may decide alone, what goes to the owner, and
the standing limits: spending, publishing or sending, physical actions, incident actions.>

## Measures and where each is taken

<Each measure, its target, and its source: the log query, the invoice, the meter, the count.>

## Procedures

Each walked once with the operator; the date it was last performed.

- Start and stop:
- Deploy, update or service:
- Back up, and restore (last restored on <date>):
- Roll back or return to a safe state (last tried on <date>):
- Restoring actions for an incident, and who may take each:
- Anything seasonal or periodic:

## Review cadence and triggers

<How often the operator reviews it, and the conditions that call for action at once: a measure
off target, a cost over budget, an advisory, a part's end of life, a decision's reopening
condition.>

## Resources and budget

<What it costs to run, per line; who pays; the runway; suppliers and their contacts.>

## Access

<Every account, key, device and site; access transferred to the operator; credentials rotated on
handover; credentials held by the owner, not by an agent.>

## Records

<Where the work records, decisions (ADRs), design, bar, as-built records, manuals, warranties and
the archive are.>

## Open items

<Known issues, the punch list, risks, and anything promised to people that is not yet done.>

## People told

<Who was told that the operator now looks after it, and how they reach them.>
```
