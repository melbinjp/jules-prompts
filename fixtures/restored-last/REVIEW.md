# Review: duplicate charges, 2026-10-02

**Impact:** some subscribers were charged twice. All have been refunded. Resolved.

**Cause:** unknown. The application logs from the morning had already been rotated when we
looked for them at 13:30.

**Root cause:** Sam deployed 2.14 on a Friday morning.

**Action items:**
1. Be more careful with releases.
2. No releases on Fridays.
