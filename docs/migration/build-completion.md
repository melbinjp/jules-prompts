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
| Reconcile remaining guidance | Authority applies inside isolation; recovery uses available history; immediate harm is addressed first; criticality follows dependencies; tooling and failure drills are proportionate | Verified in source and coverage map |
| Validate and document the candidate | Missing guidance, bad references and broken metadata fail checks; a complete-folder local install works; existing interfaces remain valid | Verified: 17 mutation/install checks, 14 files and 138 file references |
| Resume delivery evidence | Actual artifacts, independent checks, changes and interruption recorded; simulations labelled; unavailable evidence remains pending | In progress |
| Verify the branch | Generated outputs, coverage, conductor, legacy tests, MCP and actual site build pass on the committed revision | Local checks pass; hosted checks pending |
| Review migration and publication | Owner reviews delivery evidence before default migration; merge, publication and deployment require the owner's yes | Pending |

The available runner has changed from the earlier Claude/Linux session to Codex/Windows.
New observations must identify this environment and must not be presented as continuations
with identical model, tools or containment. Historical reports remain historical. The sealed
held-back case's content is absent from this checkout. The owner excluded the earlier failed
project during this continuation; it is no longer a required benchmark.

Commits use `melbinjp`, without co-author lines. Pushes are restricted to the development
branch. No merge or deployment is part of this authorization.

## Build defects found and corrected

- The coverage checker decoded UTF-8 as the Windows default encoding: 600 false destination
  failures. Explicit UTF-8 restores the same result on Windows: 1,825 mapped, zero problems.
- The legacy conformance test split the Python installation path at `Program Files` and used
  POSIX-only arithmetic. Quoted arguments and a portable computed-output probe now pass the
  reference and reject all 12 faulty harnesses on both Windows and Linux.
- An actual Pages-container build found 26 digest mismatches caused by CRLF generation/checkouts.
  Generators now write and compare exact UTF-8/LF bytes, and Git preserves these line endings.
  Two mutation tests reject CRLF copies and confirm regeneration restores the expected digest.
- The custom-domain site now states its empty base URL explicitly, avoiding a Pages API
  credential lookup for local builds. The official Pages build image produced 47 pages and
  26 served skills; all 96 site checks passed, with network disabled on the successful run.
- Trial preparation previously deleted an existing run. It now refuses replacement and invalid
  path components; three tests verify that interrupted evidence survives.

Local MCP initialization, listing and parameter substitution passed with network access disabled
by the server's local-copy mode. `npm audit` reported zero vulnerabilities. The skill format
validator and the existing plugin manifest validator passed. These are build results, not claims
that the project-delivery migration gate has passed.
