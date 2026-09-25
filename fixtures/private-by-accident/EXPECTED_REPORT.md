# Expected report for private-by-accident

HERON.md says Heron is developed fully offline and that nothing leaves the machine. There is no CONFIDENTIALITY.md, so the first step is the owner's classes. Proposed:

- the source code, `app/unmix.py` above all (the customer's edge), stays on this machine and the owner's own backup;
- the customer's name and line details stay on this machine;
- keys stay on this machine;
- generic questions about techniques may go out through the gate below.

## Channel map

| channel | what it sends, to whom | verdict |
|---|---|---|
| nightly backup (`setup.sh`) | the whole repository, in plaintext, to a hosted git service | broken |
| coding agent (`agent.toml`) | the whole repository, to a remote model endpoint, every task | broken |
| editor (`.vscode/settings.json`) | full telemetry, plus the code around the cursor to a cloud completion provider | broken |
| package installs (`pip.conf`) | the internal package's name, to the public index | broken |
| crash reports (`app/crash.py`) | tracebacks, the working directory and arguments, to a hosted tracker | broken |
| test suite (`tests/conftest.py`) | a request to a public model hub on first run | broken |
| research (`RESEARCH.md`) | the customer's name, the line, the package name and `unmix.py`, to a search engine and a chat assistant | broken |
| datasheets (`third_party/datasheets/`) | one bulk download of the vendor's whole archive, from a clean profile | holds |

## Findings

- plaintext-remote: `setup.sh` pushes every branch every night, unencrypted, to `git.example-host.com`. The host, every integration granted access to the repository, and anyone holding one token can read it. For an off-site copy the host cannot read, encrypt on the client before pushing (an encrypted git remote, or an encrypted backup tool), or push to the owner's own hardware.
- cloud-agent-whole-repo: `agent.toml` sets `include = "whole-repo"` against a remote endpoint, so every task sends everything, `unmix.py` included. Meanwhile the local model beside it is `enabled = false`. Switch the agent to the local model for the code classes, and remove the remote endpoint, or release to it only named, generic files under written terms.
- editor-telemetry: `telemetry.telemetryLevel` is `all`, and `aiCompletions.sendSurroundingCode` sends the code around the cursor to a cloud completion provider as it is typed. Set telemetry off and completions to a local provider, or none.
- name-leaks-to-registry: in `pip.conf`, `extra-index-url` makes pip also ask the public index for `heron-core-dsp`. That tells the public index the internal name on every install. Worse, anyone who publishes `heron-core-dsp` there with a higher version number gets their code installed instead. Use the local index only (no extra index), with a lockfile carrying hashes, and mirror the public packages the project uses.
- crash-reports-leave: `app/crash.py` is installed by `main()` and posts every uncaught exception's traceback, the working directory (`~/clients/acmefoods/heron`, the customer's name) and the arguments to `errors.example-tracker.io`. Write crash reports to a local file on the sorting-line PC, and let a person send a reviewed, stripped copy when needed.
- offline-never-tested: `tests/conftest.py` will download the reference weights from `models.example-hub.org` on first run, so `make test` fails with the network off. Nobody can have run it offline on a clean machine. Commit the weights with their hash (or store them in the local model store), and run the whole suite with egress blocked.
- research-names-the-work: `RESEARCH.md` shows searches naming AcmeFoods and its line 3, a public search for the internal package name, and `unmix.py` pasted into a public chat assistant. What was sent is assumed kept. Record it, and from now on use the gate: ask about the technique (least-squares unmixing with a non-negativity constraint), never the customer or the code. Better still, answer it locally, from downloaded papers and a local model.

The datasheets are done right. The vendor's whole archive was fetched once in bulk from a clean profile and checked against `MANIFEST.sha256`, and it is searched locally, so nothing outside shows which sensor Heron uses.

## Offline run

With egress blocked and a clean checkout: `./setup.sh` fails at the public index and at the git push, and `make test` fails at the weights download. This is not yet an offline project.

## Residual exposure

Even after the fixes, the one-off bulk datasheet download showed that this network fetched that vendor's archive on 2026-08-01, and the searches in RESEARCH.md already left. Both are recorded as accepted by the owner, not as solved.

## Verdicts

| item | evidence | verdict |
|---|---|---|
| classes and destinations written | no CONFIDENTIALITY.md; proposed above | broken |
| backup remote | plaintext push to a hosted service | broken |
| coding agent | whole repository to a remote endpoint | broken |
| editor | telemetry all, code to cloud completions | broken |
| package installs | internal name to the public index | broken |
| crash reports | traceback, path and arguments to a hosted tracker | broken |
| research | customer name and code sent out | broken |
| offline test run | weights downloaded on first run | broken |
| datasheets | bulk fetch, hashes checked, searched locally | holds |
| egress log reconciled | no logged session available in the fixture | skipped |

10 items: 1 holds, 8 broken, 1 skipped.

defect_id: plaintext-remote
defect_id: cloud-agent-whole-repo
defect_id: editor-telemetry
defect_id: name-leaks-to-registry
defect_id: crash-reports-leave
defect_id: offline-never-tested
defect_id: research-names-the-work
