# Complete the conductor candidate

2026-09-27. The owner asked to sync the up-to-date development branch and complete the build.
The starting revision is `927997a` on `m/brave-shannon-e884k9`; main is `f5fc9c0e`.

## Requirement and design

Continue the existing conductor plan. Correct remaining contradictions, make the candidate
installable as a complete folder and check its integrity, then exercise delivery against the
existing cases. Keep the legacy interfaces until the delivery evidence has been reviewed.
Use the existing generators and checks; introduce no new project tracker or scheduler.

## Work and acceptance

| Work | Acceptance | State |
|---|---|---|
| Reconcile remaining guidance | Authority applies inside isolation; recovery uses available history; immediate harm is addressed first; criticality follows dependencies; tooling and failure drills are proportionate | In progress |
| Validate and document the candidate | Missing guidance, bad references and broken metadata fail checks; a complete-folder local install works; existing interfaces remain valid | In progress |
| Resume delivery evidence | Actual artifacts, independent checks, changes and interruption recorded; simulations labelled; unavailable evidence remains pending | In progress |
| Verify the branch | Generated outputs, coverage, conductor, legacy tests, MCP and actual site build pass on the committed revision | Pending |
| Review migration and publication | Owner reviews delivery evidence before default migration; merge, publication and deployment require the owner's yes | Pending |

The available runner has changed from the earlier Claude/Linux session to Codex/Windows.
New observations must identify this environment and must not be presented as continuations
with identical model, tools or containment. Historical reports remain historical. The sealed
held-back case's content and the earlier failed project are absent from this checkout; their
availability is being checked with the owner.

Commits use `melbinjp`, without co-author lines. Pushes are restricted to the development
branch. No merge or deployment is part of this authorization.
