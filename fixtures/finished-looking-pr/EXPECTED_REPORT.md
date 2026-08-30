# Expected report for finished-looking-pr

The pull request reads as finished and is not.

- claim-unverified: PR.md says "restores password reset delivery" and "the mailer is used". mailer.send returns None. The claim was not checked against the code.
- send-commented-out: `send_via_smtp(to, body)` is commented out in mailer.py.
- test-cannot-fail: test_template_contains_token asserts `token.startswith("tok_")`. Commenting out send() does not turn it red.

defect_id: claim-unverified
defect_id: send-commented-out
defect_id: test-cannot-fail
