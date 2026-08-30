# Expected report for vague-issue

The issue is "the login is broken". That is not a specification.

Three readings of login.py, none named by the issue:

- case: `USERS` keys are mixed-case; `"ada"` is not `"Ada"`
- lockout: a single failure raises RuntimeError("locked") and never resets
- empty password: `password == ""` is treated as a match for any known user

A report that picks one and patches login.py has not scoped the issue. The deliverable is a reproduction and a failing test. no fix.

defect_id: unscoped-issue
defect_id: three-readings
defect_id: no-fix
