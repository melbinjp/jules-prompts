# Expected report for bumped-everything

The pull request ran `npm update --latest`, committed `package.json`, and reports that all tests pass in CI. This report checks what CI installed, what the new versions change in this code, and what the update brought in.

## The update itself

- everything-at-once: `HISTORY.md` shows one commit, `c7d19f2`, moving 63 packages, majors included. If anything breaks, it cannot be traced to a package, and the only undo is all 63. Split it: patch and minor updates together, each major on its own, each with a cold install and the full suite.
- lockfile-not-regenerated: `package.json` asks for express `^5.1.0` and date-fns `^3.6.0`, but the committed `package-lock.json` still pins express 4.19.2 and date-fns 2.30.0 (and report-kit 3.8.1, moment 2.29.4). CI runs `npm ci`, which installs the lockfile, so "all tests pass in CI" tested the old versions. The update is untested. Regenerate the lockfile with npm and commit it with each step.

## What the new versions change here

- major-read-against-nothing: Express 5 removes `app.del`. `src/server.js` registers `DELETE /api/items/:id` with `app.del`, and no test covers that route, so deleting items breaks the moment the lockfile catches up. Change it to `app.delete`, add a test for the route that fails on the old call, and read the rest of the Express 5 and date-fns 3 breaking changes against the code the same way.
- unexplained-vulnerable-pin: lodash is pinned exactly to 4.17.15 "because the newer one broke `tests/merge.test.js`", a reason that lives only in the pull request. Versions before 4.17.21 carry published advisories (CVE-2020-8203, CVE-2021-23337), and `src/items.js` merges request bodies with `_.merge`. Find what the newer lodash broke, fix the test or the code, and move to 4.17.21; if a pin must stay, write its reason and a revisit date in the repository.
- unused-updated: `moment` is bumped to 2.30.1, but nothing in `src/` requires it; the code uses date-fns. Remove it instead of updating it.

## What arrived with it

- agpl-arrived: report-kit 4 pulls in `pdf-weave` 2.1.0 under AGPL-3.0-only. Shelfy is distributed to customers under a proprietary licence without its source (`LICENSE`), so it cannot ship an AGPL library. Nothing examined what the update added. Keep report-kit on 3.8.1 until there is another route (a different PDF library, or report-kit without pdf-weave), and record why.

The CI workflow (`.github/workflows/ci.yml`) is right: `npm ci` with no cache installs exactly what the lockfile names, on Node 22. It stays; the fault is the lockfile that was not regenerated.

## Verdicts

| item | evidence | verdict |
|---|---|---|
| baseline from a cold install | not recorded in the pull request | skipped |
| one step per commit | 63 packages in `c7d19f2` | broken |
| suite run on the new versions | the lockfile still pins the old ones | broken |
| express 4 to 5 read against the code | `app.del` in `src/server.js` | broken |
| date-fns 2 to 3 read against the code | not checked; `format` is still exported, but nothing shows it was checked | skipped |
| new packages examined | `pdf-weave`, AGPL-3.0-only | broken |
| unused packages removed | `moment` updated instead | broken |
| every pin with a reason and a date | lodash 4.17.15, reason only in the pull request | broken |
| CI installs exactly the lockfile | `npm ci`, no cache | holds |

9 items: 1 holds, 6 broken, 2 skipped.

defect_id: everything-at-once
defect_id: lockfile-not-regenerated
defect_id: major-read-against-nothing
defect_id: unexplained-vulnerable-pin
defect_id: unused-updated
defect_id: agpl-arrived
