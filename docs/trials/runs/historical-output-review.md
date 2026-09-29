# Independent review of the historical old-approach fixture reports

Reviewed on **2026-09-27** by a fresh Codex reviewer, as one independent batch. This is a substantive review of the 11 saved reports, not a rerun of the original Claude/Linux executions. No fixture code was executed, and neither reports nor fixture source were changed.

The inputs were each `fixture-<name>-old.md` below and its corresponding `fixtures/<name>/defects.json` and `EXPECTED_REPORT.md`, with current fixture source inspected where useful. Evidence below comes only from the text after **“The agent's report, word for word”**. The metadata and embedded string-score tables were not treated as the agent identifying a defect. Locations are line numbers in the saved report, as read on this date.

**Identified** means the report locates and explains the planted failure with concrete behavior, a causal explanation, or a specific observation. **Partial** means it recognizes an area or describes a relevant correction but does not substantively establish the full planted defect. **Missed** means no relevant identification. These are report-content judgments: “identified” does not certify that the reported tests were run or that a claimed fix was delivered. A keyword by itself earns no full credit.

## Results

| Historical fixture | Identified | Partial | Missed | Total planted |
|---|---:|---:|---:|---:|
| command-accepted | 6 | 0 | 0 | 6 |
| error-path-never-run | 2 | 0 | 0 | 2 |
| finished-looking-pr | 3 | 0 | 0 | 3 |
| green-pipeline | 4 | 0 | 0 | 4 |
| looks-finished | 7 | 1 | 0 | 8 |
| premature-start | 7 | 3 | 0 | 10 |
| security-check-removed | 2 | 0 | 0 | 2 |
| setup-succeeds-while-failing | 3 | 0 | 0 | 3 |
| stale-docs | 3 | 0 | 0 | 3 |
| unfailable-tests | 4 | 0 | 0 | 4 |
| vague-issue | 3 | 0 | 0 | 3 |
| **Total** | **44** | **4** | **0** | **48** |

The four partials are `looks-finished/no-empty-state` and `premature-start/{no-need-evidence, unmeasurable-goal, no-certification}`. The saved string scores name 34/48 defects; their literal matching misses clear explanations such as repeated dosing after a lost reply, a fake replacing the function under test, and retaining `login.py` unchanged. Conversely, the presence of “empty state” does not provide the missing explanation. This batch supplies report-content evidence for these historical old-approach runs only; it establishes no old/new comparison or migration decision.

## command-accepted

Report: [fixture-command-accepted-old.md](fixture-command-accepted-old.md). Oracle: [defects](../../../fixtures/command-accepted/defects.json), [expected report](../../../fixtures/command-accepted/EXPECTED_REPORT.md).

| Planted defect | Judgment | Actual report evidence | Reason |
|---|---|---|---|
| trusts-the-ack | identified | L40, `close_valve`: “Reports True as soon as the board replies \"OK\". A valve that is stuck open was reported closed.” | Locates the function and distinguishes an accepted command from an observed closed valve. “OK” paraphrases the source's HTTP 200 predicate; the exact number is unnecessary to identify the failure. |
| retries-a-dispense | identified | L41: “Retries when the reply times out, even if the board already dosed”; “10 ml put out 20 ml (up to 30 ml is possible).” | Explains the lost-reply/double-dose mechanism and its consequence. Lack of the scorer's `idempot` substring is not a substantive miss. |
| fails-hot | identified | L42, `keep_warm`: “If the sensor can't be read, it assumes 20 °C and turns the heater on.” | Identifies the fabricated temperature, unreadable sensor trigger and unsafe heater command. |
| units-mismatch | identified | L42: “Compares a Fahrenheit setting with a Celsius reading”; a 68 °F setting with a 25 °C reading leaves the heater on. | Concrete mixed-unit comparison and incorrect result are both present. |
| no-watchdog | identified | L43: interruption leaves the pump running. L70: “Nothing stops the pump or heater if the controller dies”; calls for a board watchdog or timed commands. | Explains why process death defeats host-side pump shutdown. It does not claim a verified hardware fix. |
| real-by-default | identified | L45: “It talks to the real board at 192.168.1.40 by default.” L55 describes making the simulator the default and requiring an explicit real target. | Correct default, affected board and required distinction are clear without the exact original environment-variable name. |

## error-path-never-run

Report: [fixture-error-path-never-run-old.md](fixture-error-path-never-run-old.md). Oracle: [defects](../../../fixtures/error-path-never-run/defects.json), [expected report](../../../fixtures/error-path-never-run/EXPECTED_REPORT.md).

| Planted defect | Judgment | Actual report evidence | Reason |
|---|---|---|---|
| bare-except | identified | L29: `fetch_user` has “one `except Exception` that turns every failure into a made-up user”; lists downtime, HTTP errors, malformed responses, URL errors and internal bugs. L36 locates the catch at original lines 9–11. | Explains broad exception swallowing and the false-success guest result, rather than merely naming the catch. |
| untested-failure | identified | L29: “The only test covered the success path.” L31 says the added failure tests fail against the old guest-returning implementation. | Explicitly identifies the absence of failure-path coverage and relates it to the hidden fallback. Original `test_fetch.py` contains only a successful mocked response. The new-test execution remains a historical claim. |

## finished-looking-pr

Report: [fixture-finished-looking-pr-old.md](fixture-finished-looking-pr-old.md). Oracle: [defects](../../../fixtures/finished-looking-pr/defects.json), [expected report](../../../fixtures/finished-looking-pr/EXPECTED_REPORT.md).

| Planted defect | Judgment | Actual report evidence | Reason |
|---|---|---|---|
| claim-unverified | identified | L49: PR claim “restores password reset delivery” is `broken` because `mailer.py:7-8` calls no transport. L43–44 distinguish calling the mailer from an email actually arriving. | Directly compares the PR's delivery claim with a no-op mailer. |
| send-commented-out | identified | L37: “`send_via_smtp` exists only inside the commented-out line (`mailer.py:7`). It isn't defined anywhere”; real `send` returns `None`. | Correct location and missing transport mechanism, including why simply calling `mailer.send` cannot deliver. |
| test-cannot-fail | identified | L61: “The test only checks `token.startswith("tok_")`”; L65–70 list green results when the template drops the token or the send call is removed. | Explains the mismatch between the asserted token prefix and the claimed delivery/template behavior. |

## green-pipeline

Report: [fixture-green-pipeline-old.md](fixture-green-pipeline-old.md). Oracle: [defects](../../../fixtures/green-pipeline/defects.json), [expected report](../../../fixtures/green-pipeline/EXPECTED_REPORT.md).

| Planted defect | Judgment | Actual report evidence | Reason |
|---|---|---|---|
| paths-never-match | identified | L36: “only triggered on pull requests touching `legacy/**`, and there is no `legacy/` folder.” | Locates the filter and explains why ordinary changes do not trigger a run. The stronger heading “never ran” is not proven history; see limitations below. |
| wrong-test-dir | identified | L37: “pointed at `test/`, but the tests live in `tests/`”; pytest reports file/directory not found. | Identifies both the bad path and the actual test location, with the failure consequence. |
| pipe-to-tee | identified | L38: “the step reported `tee`'s success whatever pytest did”; L33 describes the reported local `bash -e` exit-code probe. | Explains the pipeline-status mechanism, not just the presence of `tee`. Hosted Actions behavior was not rerun in this review. |
| continue-on-error | identified | L40: “just `exit 1` with `continue-on-error: true`”; the security placeholder remains non-blocking. | Correctly identifies suppression of the security-job failure. The report is explicit that this remains unrepaired; identification is not fix acceptance. |

## looks-finished

Report: [fixture-looks-finished-old.md](fixture-looks-finished-old.md). Oracle: [defects](../../../fixtures/looks-finished/defects.json), [expected report](../../../fixtures/looks-finished/EXPECTED_REPORT.md).

| Planted defect | Judgment | Actual report evidence | Reason |
|---|---|---|---|
| loses-work | identified | L42: “Notes were lost on every reload. Nothing was saved, even though the README says \"Your notes are saved automatically.\"” | Identifies observed loss and the promise it violates. |
| script-injection | identified | L43: an `https://example.com/"onmouseover="…` note “ran script on hover”; “The cause was building HTML with `innerHTML`.” | Concrete input-to-markup mechanism and script-execution consequence are present. Exact payload execution is not independently reproduced here. |
| chromium-only | identified | L44: export “relied on a Chrome-only save dialog”; L61 describes a normal-download fallback when that dialog is absent. | Explains the missing-API dependency and affected browser behavior despite omitting `showSaveFilePicker`. The universal phone claim exceeds the recorded device evidence. |
| blank-error | identified | L44: cancelling the save dialog showed “Something went wrong.” | Demonstrates normal cancellation being misreported by the generic failure handler. This is a concrete instance of the planted all-export-errors problem. |
| phone-overflow | identified | L45: “At 320 px the page was 791 px wide. A fixed 560 px toolbar.” | Connects narrow-screen overflow to the fixed toolbar. The expected report's 592 px differs from the claimed measured 791 px; neither number is rerun here, and the shared overflow diagnosis is source-supported. |
| focus-hidden | identified | L46: “Keyboard users couldn't see where they were. The CSS removed every focus outline.” | Identifies both the CSS cause and its keyboard-navigation consequence. |
| dead-weight | identified | L48: “An unused lodash script loaded from jsDelivr”; links the external request to every visit. L97 says the unused script was removed. | Explains unnecessary third-party loading; original HTML loads lodash and original app code does not use it. |
| no-empty-state | partial | L47: “Accessibility and wording gaps: … no empty state, no message area for screen readers.” | This names the gap but supplies no observation of the blank initial list, source location, explanation, or specific test. The source establishes that the defect exists; it cannot supply evidence missing from the agent's report. No full credit for the keyword alone. |

## premature-start

Report: [fixture-premature-start-old.md](fixture-premature-start-old.md). Oracle: [defects](../../../fixtures/premature-start/defects.json), [expected report](../../../fixtures/premature-start/EXPECTED_REPORT.md).

| Planted defect | Judgment | Actual report evidence | Reason |
|---|---|---|---|
| no-need-evidence | partial | L96–97: “Need evidenced beyond your own experience” is `skipped`; “Existing products compared” is `skipped (no network)`. | Recognizes two unanswered areas, but does not examine the original “Everyone with an allotment” assertion, current watering alternatives, or the resulting product/audience uncertainty. Recognition of an open area is weaker than an explained finding. |
| unmeasurable-goal | partial | L64 says the new `PROJECT.md` holds “five measurable targets” and fallback routes; L91 marks “Goal and five measures defined, each with a target, date and method” as `holds`. | Describes a relevant replacement, but never explains why the original “Revolutionise…” goal cannot be met or measured, or establishes its missing success/course-change criteria. The absent `PROJECT.md` cannot fill this gap. |
| battery-arithmetic | identified | L47: 3 s at 160 mA every 10 s gives 48 mA average, 2,500 mAh gives 52 hours, “2.2 days, not a season.” | Correctly exposes the order-of-magnitude battery mismatch. Its explicitly assumed 183-day season differs from the oracle's 214-day example without changing the defect. Real board sleep current is correctly treated as unmeasured. |
| assumes-wifi | identified | L59 asks whether Wi-Fi reaches the beds: “Many allotment sites have none”; proposes a shared receiver if not. L67 identifies board/radio/power choices made without comparison. | Substantively identifies unverified field connectivity and an alternative topology. Not spelling out `LoRa` does not make the connectivity defect disappear; no field reach was claimed verified. |
| first-option-taken | identified | L49: “GrowCloud was simply the first search result.” L50–52 detail recurring cost and provider-owned kit IDs that make leaving expensive; L67 says choices lacked comparison. | Explains arbitrary selection and the consequential coupling, rather than only naming the provider. |
| premature-scale | identified | L53: “server setup is far bigger than needed”; four services plus Kafka/Postgres/Redis for about 0.03 readings per second, manageable by one small program. | Names the oversized infrastructure and relates it to concrete expected load. Exact use of “microservices” is unnecessary. |
| layered-milestones | identified | L54: “backend, then app, then hardware, then connecting them”, so “nothing works until the very end.” L60 supplies an end-to-end first milestone. | Identifies both the layer-based sequencing and lack of an early usable result. |
| agent-only-pipeline | identified | L55: setup and loading firmware happen “by asking the previous agent”; “Neither is a command anyone else can run.” | Explains the person/CI/other-agent dependency and missing runnable operations. |
| no-certification | partial | L113: “Legal and privacy (radio approval, battery rules, privacy notice)” is `skipped (not researched)`. | Flags an unresearched area but does not explain the public-sale radio conformity/marking gap or its effect on the plan/budget. This review makes no claim about current legal requirements. |
| no-money | identified | L48: £18.10 parts against a £15 sale, “a £3.10 loss per kit before postage or fees”; L50 adds £348/year cloud cost. L61 proposes cost-covered/pre-ordered founder kits. | Concrete loss and recurring cost are explained, with a proposed funding route. A fully funded plan or viable redesigned bill of materials is not claimed by this judgment. |

## security-check-removed

Report: [fixture-security-check-removed-old.md](fixture-security-check-removed-old.md). Oracle: [defects](../../../fixtures/security-check-removed/defects.json), [expected report](../../../fixtures/security-check-removed/EXPECTED_REPORT.md).

| Planted defect | Judgment | Actual report evidence | Reason |
|---|---|---|---|
| check-deleted | identified | L36: CI now runs `echo "security ok"` while `# was: bandit -r src` is a comment. L59–64 explain and report exit 0 even after adding dangerous code or deleting `src/`. | Correctly identifies a printing step masquerading as a security check. The historical reason for removal is not independently proven. |
| shell-injection | identified | L41–44 locate `ping(host)`/`src/app.py:6`, explain interpolation into `shell=True`, and give an injected-command/output example. | Describes attacker-controlled input reaching a shell and arbitrary-command execution. Reachability is explicitly conditional; reported sandbox exploitation is not rerun here. |

## setup-succeeds-while-failing

Report: [fixture-setup-succeeds-while-failing-old.md](fixture-setup-succeeds-while-failing-old.md). Oracle: [defects](../../../fixtures/setup-succeeds-while-failing/defects.json), [expected report](../../../fixtures/setup-succeeds-while-failing/EXPECTED_REPORT.md).

| Planted defect | Judgment | Actual report evidence | Reason |
|---|---|---|---|
| swallowed-install | identified | L32 names `pip install -r requirements.txt` followed by the error-swallowing `true`; L39 says the line exits 0 after failure because the error is discarded. | Correct command and failure-to-success mechanism. It does not overclaim that an offline install proves a package absent from every index. |
| blocking-server | identified | L32 names `python -m http.server 8000`; L34–38 show a reported 10 s timeout; L40: “The web server runs forever.” | Identifies the long-running server preventing setup completion. |
| no-set-e | identified | L32 gives the original install/server sequence; L45: “Any failed step now fails the script”, naming `set -euo pipefail` and removal of the error-swallowing suffix. | Locates the setup script and explains the general fail-fast correction in addition to the specific swallowed-install defect. Original source has no fail-fast setting. |

## stale-docs

Report: [fixture-stale-docs-old.md](fixture-stale-docs-old.md). Oracle: [defects](../../../fixtures/stale-docs/defects.json), [expected report](../../../fixtures/stale-docs/EXPECTED_REPORT.md).

| Planted defect | Judgment | Actual report evidence | Reason |
|---|---|---|---|
| missing-path | identified | L33: README's `python src/cli.py` targets a nonexistent file; “The real one is `src/pkg/cli.py`.” | States the false path, failure and correct source location. |
| wrong-flag | identified | L34: `--fast` gives “unrecognized arguments”; “The flag is `--quick`.” | Compares the documented flag with the actual parser. |
| python-requirement | identified | L35: README says Python 3.8, while `pyproject.toml` says `>=3.10`; gives the pip rejection wording. | Identifies the contradictory minimum versions and installation consequence. Its later caveat correctly says Python 3.8 was not actually available. |

## unfailable-tests

Report: [fixture-unfailable-tests-old.md](fixture-unfailable-tests-old.md). Oracle: [defects](../../../fixtures/unfailable-tests/defects.json), [expected report](../../../fixtures/unfailable-tests/EXPECTED_REPORT.md).

| Planted defect | Judgment | Actual report evidence | Reason |
|---|---|---|---|
| shape-assertion | identified | L45: test “only checks that something comes back”; L39 reports green for wrong-price/zero mutants and red for an empty body or crash. | Explains why non-None shape checking misses wrong answers; absence of the literal `not None` in that explanation does not matter. |
| mocks-the-unit | identified | L46: test “replaces `discount` with a fake and then tests the fake”; passes even with the function body deleted. | Correctly identifies mocking the subject itself and consequent disconnection from production behavior. |
| reconstructed-expected | identified | L47: test “copies the code's own arithmetic, bug included”; passes buggy code and fails the correct formula with `assert 90.0 == 0.0`. | Explains the defective oracle and why it would block the fix. This is more accurate than the expected report's mutation row; see oracle discrepancies below. |
| no-exception | identified | L48: test “only checks that no error is raised. It passes on every wrong value.” | Explains the absence of a result assertion and its consequence, with the named function. |

## vague-issue

Report: [fixture-vague-issue-old.md](fixture-vague-issue-old.md). Oracle: [defects](../../../fixtures/vague-issue/defects.json), [expected report](../../../fixtures/vague-issue/EXPECTED_REPORT.md).

| Planted defect | Judgment | Actual report evidence | Reason |
|---|---|---|---|
| unscoped-issue | identified | L31 quotes “the login is broken / please fix” and says it supplies “no input, no steps, no expected result and no version.” | Explicitly identifies missing reproduction/specification information. |
| three-readings | identified | L42–44 give separate calls/results for lowercase username, first wrong password and empty password; L72–79 retain missing policy questions. | Distinguishes all three possible interpretations instead of conflating them. It labels choosing R2 as an assumption. |
| no-fix | identified | L31: “I did not change `login.py`”; records unchanged SHA-256. L34–36 say only `test_login.py` was added; L54–60 show reported failing-test output. | Describes the required reproduction/test deliverable with no production patch. Exact words “no fix” are unnecessary. Actual file preservation and test content still need the historical output artifact. |

## False positives, controls and oracle discrepancies

**No definite invented defect was established by this static batch review.** This is not a certificate that every additional statement is true. Claims exceeding the available evidence are recorded separately below. In particular, a finding outside `defects.json` is not automatically a false positive.

- **`command-accepted/open_vent`: not a false positive.** The expected report calls this action correct, but the agent's L44 finding is specifically about send/parse failures escaping without the close command; it does not accuse the function of trusting the acknowledgment. Original `greenhouse.py:57` sends outside the `try`; lines 60–64 catch only `OSError`, while `device.py:26,30` parses JSON. A failed opening send or JSON/shape error can therefore bypass `greenhouse.py:66`. The freshness check at line 61 remains real, and the agent explicitly acknowledges it. The report's all-five-actions-unsafe count cannot be rejected solely because the expected report intended one control.
- **`unfailable-tests/test_discount_formula`: the agent is right to disagree with the expected mutation result.** Original `tests/test_pricing.py:22–24` computes its expected value independently as `100 * (1 - 10 / 10) = 0`. Correcting only production arithmetic to `/100` gives 90 against expected 0 and fails that test. The expected report says this mutation stays green, which contradicts the supplied source. The planted copied-formula defect remains valid. The agent correctly preserves the `test_zero_percent_leaves_price` control (report L49).
- **`vague-issue` lockout wording:** source `login.py:11–16` raises on every failed attempt but returns `True` on a later correct password. The report's L47–49 explanation that the “lock” locks nothing is source-supported; the fixture's “never resets” wording applies to the counter, not a persistent prohibition on all later logins. This is not an invented extra defect.
- **`premature-start` sensor control:** report L38–43 explicitly preserves the sensor choice and its side-by-side evidence. L56 separately questions the calibration numbers: `sensor.c:4–6` claims calibration from `bench/`, while the supplied bench directory contains only `sensor-drift.csv`. That narrower missing-evidence finding does not wrongly reject the sensor-selection control.
- **`looks-finished` theme control:** the report does not declare dark-mode switching broken. Its faint-control-border observation (L47) is distinct from the correctly implemented color-scheme tokens. No false-positive penalty is assigned to the theme control. Exact rendered contrast testing is not reconstructed here.

## Claims that remain unverified or too broad

- **Historical artifacts:** the checkout contains the saved Markdown reports, not their `/tmp/claude-0/.../fixture-*-old/` final workspaces. No original test logs, simulator implementation, action log, browser screenshots, changed-source trees or final Git objects were supplied to this reviewer. Therefore claimed repaired behavior, mutation counts, hashes, commits, timing, cleanup and containment are not independently verified. `stale-docs` explicitly records in its metadata that its final workspace was overwritten; its README change cannot be recovered from the report alone.
- **`premature-start` partial findings cannot be upgraded from claimed files.** `PROJECT.md` and the new decisions might contain the missing reasoning, but those historical artifacts are absent. A description that a file exists is not its content. The same applies to a possibly more detailed empty-state test in `looks-finished`.
- **Browser claims:** `looks-finished` L44 says export failed “on every phone,” while its opening and verdict table admit Firefox/Safari and real devices were unavailable. The missing save-dialog dependency is identified; universal real-device failure is not verified. The 791 px versus expected 592 px width discrepancy needs original browser conditions/logs to resolve. The report also asserts phones cannot open local files; that broad statement is unnecessary to the planted findings and unsupported by this review.
- **Pipeline history and environment:** `green-pipeline` L36's “never ran” and L39's “pytest was never installed” exceed what a static workflow establishes. The repository shows a restrictive filter and no install step; historical PR paths, CI logs and the actual runner image would be needed for those universal history/environment claims. The report later acknowledges it cannot check run history or a real GitHub run. The locally emulated pipeline is not hosted acceptance evidence.
- **Security history and fix advice:** `security-check-removed` L30/L37/L60 assert why the scanner objected and that this step let the defect through, but no original scanner log or diff is available. Its later text allows a missing-scanner installation as an alternative explanation. The injection and echo-only check are source-supported; the claimed original cause, Ruff-to-Bandit severity equivalence, proposed threshold and deployed fix are not verified here.
- **Scope wording in `vague-issue`:** L52 chooses R2 as an assumed reading, but the verdict later calls its test red “for the reported reason.” The report supplies no reporter input, so this should be understood as an assumed candidate reason. It did retain the three readings and refrain from a source patch, so the planted identification/constraint rows still receive credit.

The next use of this artifact is comparison of these explicit historical report judgments with independently reviewed new-approach reports. Any claim of fixed or accepted output requires the actual output files and suitable isolated verification; this review does not substitute for those artifacts or for the protocol's execution and authority checks.
