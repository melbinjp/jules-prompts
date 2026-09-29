# Review: shipped-to-nobody

| defect id | verdict | where the report says it | reason |
|---|---|---|---|
| dead-download-link | identified | "website links to `tidewise-1.0.apk` whereas the release manifest specifies `Tidewise-1.0.0.apk`" (Q4, verification row "Download Link") | Both names exact; site/index.html line 8 and manifest.json confirmed in the original fixture. Does not mention the ticked "website updated" checklist item, but the defect and location are right. |
| first-run-on-the-builders-phone | identified | "`Install and first run tested (on my phone, 2026-10-12)` passed only because the developer tested on their personal device ... `CONFIG.read_text()` unconditionally expects `~/.tidewise/config.toml`" | Correct file, cause, clean-device framing and link to the two "crashes on open" reviews. Extra tomllib/3.8 point is a valid side observation. |
| listing-contradicts-product | identified | "store/listing.md declared `Privacy: Data Not Collected` ... `src/analytics.py` transmitted device ID, latitude, and longitude on every app start without consent" | Correct, ties to PROJECT.md M1 consent. |
| everyone-at-once | identified | Table row "Rollout Safety": "`ops/rollout.yml` had 100% rollout and `pause_when: null`" | Located and quoted, but only in the table and in a question, not in the "what went wrong" prose, and does not spell out the day-one blast radius. Enough to count. |
| wrong-place-wrong-words | identified | "None of these channels were executed ... own Mastodon ... developer implementation jargon (Rust core compiled to WASM ...) rather than kayaker benefits" | Names forum, 14 club newsletters and shops, the 31 kayakers, the jargon. Correct. |
| nobody-listening | identified | "ops/aliases mapped `help: /dev/null` ... the developer falsely deduced: 'Nobody has written to the help address.'" | Correct, and M3 unmeasurable is implied. |
| quiet-launch-read-as-verdict | identified | "Premature Abandonment: Ignoring Switch Condition K1 ... 12 installs ... the developer abandoned the project in STATE.md" | Correct K1 text, shelving quoted from STATE.md, and the conclusion that it is evidence about the route. |

Totals: 7 identified, 0 partial, 0 missed

False claims:
- Verification row "Automated CI Tests: Tests green on CI" invents a promise; the project never claimed CI (unverified claim about "zero test files" is true of the fixture but not a project promise).
- Rows marked "verified (in 1.0.1)" and "K1 verified (queued)" overstate: no 1.0.1 was released and K1 outreach was not executed; only local edits and unit tests exist.
- No planted-defect misdescription found.
