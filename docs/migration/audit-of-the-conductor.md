# Audit of the conductor draft against the coverage map

- Audited: `conductor/` at commit `933f7f1` against `docs/migration/coverage-map.md`.
- Auditors: two agents in fresh contexts, neither of which wrote the map or the conductor. Each
  took half of the rows. Each read the original text of every item (via
  `scripts/inventory_map.py --list`) and the destination sections, then judged whether the item's
  substance is present as a performable instruction. They edited nothing.
- Date: 2026-09-26 to 2026-09-27.

## What they found

| Half | Rows checked | Missing | Weak | Misplaced | Contradictions not marked as changes |
|---|---|---|---|---|---|
| Rows 131 to 451 (lifecycle skills) | 240 | 2 | 10 | 8 | 0 |
| Rows 452 to end (narrow skills, harness, owner requests, planted defects) | 275 | 4 | 13 | 3 | 2 |

No planted defect lost its instruction. Two defect rows were weak: the pull-request fixture's
claims check sat in `quality.md` rather than the section the row names, and the AGPL fixture relied
on transitive dependencies, a word the guidance had dropped.

## What changed (this commit)

- **The two contradictions.**
  - The plan-and-wait rule is restored: write the plan; wait if approval is needed and the harness
    can pause; otherwise state it and proceed within the delegated authority. Only actions outside
    that authority are recorded as proposed and not taken.
  - Reports lead with one sentence on whether the work does what it claims, then what could not be
    checked.
- **Missing substance restored:**
  - the stop is tried once;
  - the periodic review covers failed gates and the run itself;
  - review feedback is acted on, and a finished review is posted where the project reviews work;
  - the tests to audit are chosen from version-control history.
- **Weak rows strengthened:**
  - the reviewer checks each change's link to its work item and its evidence;
  - after a change, the journeys it touches are walked again;
  - everything is re-run from cold before the final verdict;
  - bounded timeouts and a usable degraded mode;
  - the channel map's columns (what it sends, to whom, when);
  - the data model, and who operates each action, in the list of costly-to-reverse decisions;
  - an unsafe failure path counts as a failed physical action, with one row per action;
  - the owner's yes before removing a feature nobody uses;
  - the chat-completions endpoint format and the supervision modes in the harness requirements;
  - each fix's level in the change description;
  - laundered exit codes;
  - migration timeouts and when migrations run relative to the rollout;
  - the tells of a map built from names, and the coupling nobody intended;
  - the reading taken for each ambiguity;
  - transitive dependencies;
  - claims checked in the software review section;
  - "where to look" hints for the testing, pipeline, fixing, review, migration, dependency and
    translation sections;
  - the state note kept as the model wrote it;
  - the automation's one command;
  - each failed bar row's next step.
- **Misplaced items:** moved into the named section (supervision modes, peak-load checks, a
  redesign as a request, the model-is-not-an-agent sentence, the confidentiality examples, the
  certification marks), or the row's destination corrected where the substance belongs elsewhere.
- **One map note corrected:** owner.4. The requirement for two different kinds of evidence applies
  only to decisions that are costly to reverse, exactly as the old checker enforced.

## Still open

- The row for owner.17 names `docs/trials/protocol.md`, which step 3 writes.
- Three of the second auditor's items, "a few gate pieces that sit in a different section", were
  not itemised. They are left for your semantic review of the map.
- This audit judged presence and precision. Whether the conductor works is what the trials in
  step 3 test.

## Follow-up review: 2026-09-27

The review of branch commit `927997a` confirmed that `33aa9e2` had corrected bounded-task scope,
revalidation after changes, native harness capabilities and custom fix labels. The original audit
above remains a record of the earlier draft; it is not a verdict on this later version.

Six remaining corrections were made in the working tree, with the affected coverage-map rows
qualified and their source labels preserved:

- Isolation no longer claims every command is safe: network, spending, publishing and device
  effects remain bounded by their own controls and delegated authority.
- Recovery uses native checkpoints; per-step commits and automatic rollback are not required, and
  repairs or restoration preserve unrelated and concurrent work.
- Immediate harm and unsafe operation take priority over core-function or platform defects;
  remaining priorities follow evidence of severity, likelihood and cost to affected people.
- Delivery dependencies, float and completion impact determine criticality; a long lead time alone
  does not put an item on the critical path.
- Missing capabilities, repetition and costly mistakes justify evaluating tools; they do not
  automatically justify building machinery beyond the authorised outcome and budget.
- Failure exercises use controlled tests, safe drills or labelled simulations; they never require
  endangering people or disrupting real delivery merely to obtain evidence.

The planted-failure instructions remain in place. This is a static review and correction, not a
delivery trial or evidence that an actual installation is safe. The pending delivery comparisons
and their independent output checks remain the next evidence required for migration.

### Verification on Windows

The first `python scripts/inventory_map.py --destinations` run found all 1,825 source items but
reported 600 missing destinations. The checker decoded UTF-8 Markdown with the Windows locale,
corrupting the section delimiter in paths. Running with Python's UTF-8 mode confirmed the cause:
`1825 of 1825 items mapped, 0 problems.`

The checker now explicitly reads files and Git output as UTF-8 and emits UTF-8 diagnostics. The
ordinary command, without an environment or interpreter-mode workaround, then returned exit 0:

```text
1825 of 1825 items mapped, 0 problems.
```

A captured `--list` run also returned exit 0, decoded strictly as UTF-8, and contained 1,825 items
with no Unicode replacement characters. These checks establish inventory coverage and valid
destination headings; they do not establish semantic equivalence or successful delivery.
