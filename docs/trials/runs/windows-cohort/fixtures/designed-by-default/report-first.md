# Design Review: Riverside Physio Booking App ("Slot")

## Executive Verdict

**The redesigned booking app fails its primary objective, degrades real-world patient completion rates from 71% to 52%, introduces critical runtime defects that break the booking flow, violates core accessibility standards, and relies on synthetic agent simulations masquerading as measured usability research.**

### What Could Not Be Checked and Why
- **Measure M3 (Missed appointments rebooked within a day):** Could not be verified because no reminder agent execution logs exist in the repository. Furthermore, attempting to list appointments after CLI booking crashes with a `TypeError`.
- **Release Procedure (`make release`):** Could not be verified because no `Makefile` exists in the repository.

---

## 1. Project Classification

- **Output:** Hybrid software application: Patient-facing web client ([`web/book.html`](file:///trial-runs/jules-trials-20260927/runs/fixture-designed-by-default-new/web/book.html)), receptionist view ([`web/list.html`](file:///trial-runs/jules-trials-20260927/runs/fixture-designed-by-default-new/web/list.html)), backend SQLite HTTP API ([`server/api.py`](file:///trial-runs/jules-trials-20260927/runs/fixture-designed-by-default-new/server/api.py)), and administrative CLI for the automated reminder agent ([`cli/slot.py`](file:///trial-runs/jules-trials-20260927/runs/fixture-designed-by-default-new/cli/slot.py)).
- **Starting State:** Existing build with active regressions. The app was recently redesigned under Decision [D0004](file:///trial-runs/jules-trials-20260927/runs/fixture-designed-by-default-new/decisions/D0004-single-page-booking.md) (*"Book on one page, details first"*), replacing the original 3-step flow with a single-page form.
- **Scale and Uncertainty:** Small codebase (Python 3.8, SQLite, vanilla HTML/CSS/JS); high user-impact stakes (elderly and injured patients, median age 61, 78% mobile).
- **Confidentiality:** Private patient health service; data must remain local (no external network transmission).
- **Standing Rules & Authority:** Owner Dr. A. Mensah set a hard standing rule on 2026-06-02: *"A patient holds at most two upcoming appointments, so nobody block-books the Monday evening slots."*

---

## 2. Questions for the Owner & Recorded Assumptions

Because the owner was unavailable for questions during this session, the following questions and explicit assumptions were recorded:

1. **Question:** Did clinic owner Dr. A. Mensah approve Decision [D0004](file:///trial-runs/jules-trials-20260927/runs/fixture-designed-by-default-new/decisions/D0004-single-page-booking.md), which was signed off solely by designer J. Ortiz?
   - **Assumption Recorded:** The clinic owner did not formally approve D0004. In accordance with conductor governance ([`guidance/decisions.md`](file:///trial-runs/jules-trials-20260927/new-method/conductor/guidance/decisions.md)), changes that compromise primary success measures (M1) and clinic rules require owner sign-off.
2. **Question:** Are the supplementary fields added in the redesign (email, physical address, postcode, how heard, fax) strictly necessary for patient booking, or should the flow retain the original minimal short form (name, phone, date of birth)?
   - **Assumption Recorded:** The supplementary fields represent "design by default" bloat ([`guidance/design.md`](file:///trial-runs/jules-trials-20260927/new-method/conductor/guidance/design.md) §Flows, states and words). They impose severe friction on injured mobile users and should be removed from the initial booking flow.
3. **Question:** Should the clinic immediately reopen/supersede Decision [D0004](file:///trial-runs/jules-trials-20260927/runs/fixture-designed-by-default-new/decisions/D0004-single-page-booking.md) and revert the live booking interface to the 3-step flow?
   - **Assumption Recorded:** Yes. Reverting to the 3-step flow immediately arrests the ~19% drop in patient completion while architectural and accessibility defects are resolved.

---

## 3. Detailed Review by Area

### A. Product Objectives & Performance Metrics ([`guidance/product.md`](file:///trial-runs/jules-trials-20260927/new-method/conductor/guidance/product.md))
- **Measure M1 (First-time booking unaided within 3 minutes, target 80%):**
  - **July (Three steps):** 70%, 72%, 71%, 71% completion (average: 71.0%).
  - **August (Redesign D0004):** 54%, 51%, 52%, 52% completion (average: 52.25%).
  - **Impact:** In [`metrics/first-booking.csv`](file:///trial-runs/jules-trials-20260927/runs/fixture-designed-by-default-new/metrics/first-booking.csv), the redesign produced an immediate **18.75 percentage point collapse** in successful patient bookings, moving the product sharply away from its 80% target.
- **Goal G1 & Measure M2 (Front desk call reduction):**
  - Deterioration of self-service completion forces frustrated patients to call the clinic desk, directly undermining the goal of halving calls from July's baseline of 140/week.

### B. User Flow, Information Architecture & "Designed by Default" ([`guidance/design.md`](file:///trial-runs/jules-trials-20260927/new-method/conductor/guidance/design.md))
- **Audience Reality:** Patients have a median age of 61; 78% visit via mobile phone; many are navigating with one hand while coping with physical injury.
- **Form Inversion:** The redesign requires patients to input 9 separate fields (`first_name`, `last_name`, `dob`, `email`, `phone`, `address`, `postcode`, `heard_from`, `fax`) before they can even see whether any appointment slots are available.
- **Friction & Irrelevant Fields:** Demanding a fax number and marketing survey ("How did you hear about us?") before displaying appointment availability violates `guidance/design.md`: *"Where a step asks for something, name what it is used for; a field nothing uses is removed. 'Designed by default' puts nine fields before anything worth signing up for, and orders the flow by build order."*
- **Empty & Loading States:** If a user completes all required fields, but no slots are available, the UI provides no feedback or alternative path.

### C. Architectural Threading & Runtime Defects ([`guidance/software.md`](file:///trial-runs/jules-trials-20260927/new-method/conductor/guidance/software.md))
1. **Broken Slot Selection ([`web/book.js`](file:///trial-runs/jules-trials-20260927/runs/fixture-designed-by-default-new/web/book.js)):**
   - Slot buttons are dynamically rendered without click listeners to toggle selection state (`aria-pressed`).
   - Upon form submission, `document.querySelector('.time[aria-pressed="true"]')` returns `null`.
   - Accessing `chosen.dataset.id` immediately throws an unhandled `TypeError: Cannot read properties of null (reading 'dataset')`. First-time booking on the web app cannot complete.
2. **Missing Backend Endpoint ([`server/api.py`](file:///trial-runs/jules-trials-20260927/runs/fixture-designed-by-default-new/server/api.py)):**
   - `web/book.js` attempts to fetch `/slots`. `server/api.py` defines no `get_slots` or slot endpoint.
3. **Broken Cancellation & Undo Promise (Journey J2):**
   - [`DESIGN.md`](file:///trial-runs/jules-trials-20260927/runs/fixture-designed-by-default-new/DESIGN.md) promises a 10-second "Cancelled. Undo" bar that restores the appointment exactly as it was.
   - In reality, [`server/store.py`](file:///trial-runs/jules-trials-20260927/runs/fixture-designed-by-default-new/server/store.py) executes an immediate hard delete: `DELETE FROM bookings WHERE id = ?`.
   - All patient data is permanently erased. No undo endpoint exists in `server/api.py`, no soft delete exists, and no UI for cancellation exists in [`web/list.html`](file:///trial-runs/jules-trials-20260927/runs/fixture-designed-by-default-new/web/list.html).
   - Conductor rule: *"A mockup that promises 'Undo' over a delete that removes the row in place is a broken design."*
4. **Bypassed Clinic Business Rules ([`PROJECT.md`](file:///trial-runs/jules-trials-20260927/runs/fixture-designed-by-default-new/PROJECT.md)):**
   - Dr. Mensah's rule limiting patients to 2 upcoming appointments is checked exclusively in client-side JavaScript (`web/book.js`).
   - `server/api.py` does not enforce the rule. Verified via Docker test: 3 consecutive bookings were successfully created for the same phone number via `api.post_bookings`.
   - `cli/slot.py` bypasses the rule completely. Verified via Docker test: `slot book` created 3 consecutive bookings.
   - Conductor rule: *"A limit checked only in the page's script is bypassed by every other caller."*
5. **CLI Runtime Crash ([`cli/slot.py`](file:///trial-runs/jules-trials-20260927/runs/fixture-designed-by-default-new/cli/slot.py)):**
   - When the reminder agent books via CLI (`slot book PHONE SLOT`), patient names are omitted.
   - When `slot list DATE` is executed, string concatenation `first + ' ' + last` crashes with `TypeError: unsupported operand type(s) for +: 'NoneType' and 'str'`.

### D. Look, Feel, Design Tokens & Accessibility ([`guidance/design.md`](file:///trial-runs/jules-trials-20260927/new-method/conductor/guidance/design.md))
- **Stray Values & Token Non-Compliance:**
  - [`web/tokens.css`](file:///trial-runs/jules-trials-20260927/runs/fixture-designed-by-default-new/web/tokens.css) defines a coherent design system (`--ink`, `--accent`, `--line`, etc.).
  - [`web/book.css`](file:///trial-runs/jules-trials-20260927/runs/fixture-designed-by-default-new/web/book.css) completely ignores the tokens file, using 0 tokens and introducing 11 stray hardcoded values (`#222`, `#666`, `#ccc`, `#1a73e8`, `#1967d2`, `#7fb3f5`, `18px`, `10px`, `14px`, `9px`, `6px`, `22px`).
  - [`web/list.css`](file:///trial-runs/jules-trials-20260927/runs/fixture-designed-by-default-new/web/list.css) introduces stray colors `#e0e0e0`, `#2b6cb0`, and `#777`.
- **WCAG 2.2 AA Color Contrast Failure:**
  - The submit button (`.book-button`) pairs `#ffffff` text with a `#7fb3f5` background.
  - Calculated contrast ratio is **2.18:1**, severely failing the minimum WCAG 2.2 AA requirement of **4.5:1** for regular text.
- **Touch Target Failures:**
  - Time slot buttons have a computed height of ~30px.
  - Submit button has a computed height of ~35px.
  - Both fail the WCAG 2.2 AA touch target minimum of **44 by 44 CSS pixels**, creating acute difficulties for elderly and injured users operating a phone with one hand.
- **Error Messaging Quality:**
  - [`web/messages.js`](file:///trial-runs/jules-trials-20260927/runs/fixture-designed-by-default-new/web/messages.js) surfaces raw technical strings: `"Error 409: CONFLICT"` and `"ECONNRESET"`.
  - Violates `guidance/design.md`: *"Every error says what happened and what to do next, in the person's words, not the exception's."*

### E. Decision Governance & Research Authenticity ([`guidance/decisions.md`](file:///trial-runs/jules-trials-20260927/new-method/conductor/guidance/decisions.md))
- **Decision D0004 Flaws:**
  - Claimed to serve M1, but resulted in an immediate 18.75% drop in M1.
  - Relied entirely on aesthetic preferences ("looks cleaner", "everyone in the design review preferred") rather than task performance.
  - Approved unilaterally by designer J. Ortiz without clinic owner consent.
  - Marked `revisit: never`, violating conductor guidelines requiring measurable reopening triggers.
- **Fabricated Usability Findings ([`research/usability-2026-08.md`](file:///trial-runs/jules-trials-20260927/runs/fixture-designed-by-default-new/research/usability-2026-08.md)):**
  - Reported *"5 of 5 participants finished in under 2 minutes. Measured."*
  - Session notes reveal participants were automated agents executing fixed procedural prompts: `"Steps: 1. Fill in every field. 2. Scroll to the times. 3. Choose Tuesday 10:00. 4. Press Book this time."`
  - Conductor violation: *"The builder is never a participant, and an agent told what to click is not a person meeting the product for the first time; reporting either as one is inventing evidence."*

---

## 4. Item-by-Item Verification Table

| # | Item / Promise / Requirement | Status | Evidence / Reason |
|---|---|---|---|
| 1 | **Goal G1:** Self-service booking, moving, and cancellation | **failed** | Online completion dropped to 52%; web booking has runtime TypeError; cancellation hard-deletes records with no undo. |
| 2 | **Measure M1:** First-time booking unaided ≤ 3 min (target 80%) | **failed** | Metrics in [`metrics/first-booking.csv`](file:///trial-runs/jules-trials-20260927/runs/fixture-designed-by-default-new/metrics/first-booking.csv) dropped from 71.0% (July) to 52.25% (August), moving ~28% below target. |
| 3 | **Measure M2:** Reduce booking calls to desk by 50% | **failed** | Degradation of online booking funnel forces patients back onto telephone lines. |
| 4 | **Measure M3:** Missed appointments rebooked within 1 day (90%) | **not verified** | No reminder agent logs present in repository; CLI execution throws unhandled TypeError. |
| 5 | **Owner Rule:** Patient holds at most 2 upcoming appointments | **failed** | Tested in Docker: `api.post_bookings` and `cli/slot.py` permitted 3 consecutive bookings. Enforced only in client JS. |
| 6 | **J1 Step 1:** View free times this week (`GET /slots`) | **failed** | Times hidden behind 8 required fields; `server/api.py` has no `/slots` route; slot buttons lack click handlers. |
| 7 | **J1 Step 2:** Short form with name, phone, dob | **failed** | Redesign replaced 3 fields with 9 fields (including fax, marketing source, address, postcode). |
| 8 | **J1 Step 3:** Confirmation showing time, address, cancel instructions | **failed** | `web/book.js` displays bare string `'Booked.'` without time, address, or cancellation guidance. |
| 9 | **J2 Step 1:** Patient views appointment and taps Cancel | **failed** | `web/list.html` has no cancel button, no appointment list rendering, and no JavaScript attached. |
| 10 | **J2 Step 2:** Temporary "Cancelled. Undo" notification for 10s | **failed** | Neither UI, CSS, nor timer exists in `web/list.html` or `web/list.css`. |
| 11 | **J2 Step 3:** Undo restores appointment exactly | **failed** | `server/store.py` executes `DELETE FROM bookings WHERE id = ?`; no undo endpoint or soft delete mechanism exists. |
| 12 | **J3 Step 1:** Reminder agent reads appointments (`slot list`) | **failed** | Tested in Docker: `slot list` crashes with `TypeError: unsupported operand type(s) for +: 'NoneType' and 'str'`. |
| 13 | **J3 Step 2:** Reminder agent rebooks within rules (`slot book`) | **failed** | Tested in Docker: `slot book` creates appointments with null names and ignores the 2-appointment limit. |
| 14 | **D0004 Claim 1:** Decision serves M1 | **failed** | Empirical funnel data proves completion dropped by 18.75% immediately upon adoption. |
| 15 | **D0004 Claim 2:** Evidence of user preference | **failed** | Cites subjective aesthetic opinions ("looks cleaner"); contradicted by actual patient completion metrics. |
| 16 | **D0004 ADR Compliance:** Follows ADR standard | **failed** | No criteria before scoring; no exit strategy; approved only by designer; specifies `revisit: never`. |
| 17 | **Usability Study:** 5 participants completed in < 2 min (Measured) | **failed** | Study used scripted agent prompts with exact step-by-step instructions; violates guidance against synthetic evidence. |
| 18 | **Design System:** All surfaces use `tokens.css` | **failed** | `web/book.css` contains 0 token usages and 11 stray values; `web/list.css` contains 4 stray values. |
| 19 | **Accessibility - Contrast:** WCAG 2.2 AA (≥ 4.5:1) | **failed** | `.book-button` text contrast is 2.18:1 (`#ffffff` on `#7fb3f5`), failing accessibility minimums. |
| 20 | **Accessibility - Touch Targets:** Minimum 44x44 CSS px | **failed** | Time buttons are ~30px height; submit button is ~35px height; both fail mobile touch target standards. |
| 21 | **Operator Parity:** Person and machine interfaces share rules | **failed** | 2-appointment limit enforced solely in client JS; API and CLI bypass all limits. |
| 22 | **Craft - Error Messaging:** Clear plain-language guidance | **failed** | `web/messages.js` displays raw technical strings (`Error 409: CONFLICT`, `ECONNRESET`). |
| 23 | **Test Coverage:** Automated verification of J1 and J2 | **failed** | `tests/test_slots.py` and `tests/test_book.py` cited in `PROJECT.md` do not exist. |
| 24 | **Release Procedure:** Verifiable release path (`make release`) | **not verified** | `Makefile` referenced in `PROJECT.md` does not exist in repository. |

---

## 5. Workflow and Delivery Summary

- **Workflow Status:** Review completed within budget (19 tool calls used of ~60 allotted limit). All code execution performed strictly inside isolated Docker container with zero network access. Review recorded permanently in the repository as [`REVIEW.md`](file:///trial-runs/jules-trials-20260927/runs/fixture-designed-by-default-new/REVIEW.md).
- **Delivery Status:** Critical delivery failure of the redesigned booking app. The product cannot be released or operated in its current state.

---

## 6. Action Plan & Recommendations

1. **Immediate Action — Supersede D0004 & Revert to 3-Step Flow:**
   - Formally reopen and supersede D0004 with a new decision record (D0005).
   - Restore the three-step booking architecture: (1) Choose time slot, (2) Provide name, phone, and date of birth, (3) View confirmation with clinic address and cancellation details.
   - Eliminate unnecessary fields (fax, marketing source, full address, postcode, email) from the primary booking flow.
2. **Backend & Architecture Repairs:**
   - Implement `GET /slots` in [`server/api.py`](file:///trial-runs/jules-trials-20260927/runs/fixture-designed-by-default-new/server/api.py).
   - Move the 2-appointment limit enforcement into [`server/store.py`](file:///trial-runs/jules-trials-20260927/runs/fixture-designed-by-default-new/server/store.py) so web, API, and CLI callers share identical constraints.
   - Replace `DELETE FROM bookings` with a soft-delete status (`cancelled`) and implement an undo endpoint (`POST /bookings/<id>/undo`) with a 10-second expiration window.
   - Fix [`cli/slot.py`](file:///trial-runs/jules-trials-20260927/runs/fixture-designed-by-default-new/cli/slot.py) to handle null names gracefully in `slot list`.
3. **Frontend & Accessibility Compliance:**
   - Refactor [`web/book.css`](file:///trial-runs/jules-trials-20260927/runs/fixture-designed-by-default-new/web/book.css) and [`web/list.css`](file:///trial-runs/jules-trials-20260927/runs/fixture-designed-by-default-new/web/list.css) to use variables from [`web/tokens.css`](file:///trial-runs/jules-trials-20260927/runs/fixture-designed-by-default-new/web/tokens.css) exclusively.
   - Upgrade `.book-button` styling to use `--accent` (`#1a5fb4`) with white text (contrast ratio > 6:1) and minimum dimensions of 44x44 CSS px.
   - Ensure all `.time` buttons meet the 44x44 CSS px target and properly toggle `aria-pressed`.
   - Update [`web/messages.js`](file:///trial-runs/jules-trials-20260927/runs/fixture-designed-by-default-new/web/messages.js) to return actionable, friendly error messages (e.g., *"That time was just taken. Here are the nearest available appointments."*).
4. **Verification & Testing:**
   - Create automated test suite (`tests/test_slots.py`, `tests/test_book.py`, `tests/test_cancel.py`) proving J1, J2, and J3 before deployment.
   - Conduct genuine usability testing with representative human patients (or properly labelled unscripted simulations).

---

## Final Counts

**0 verified, 22 failed, 2 not verified, 0 not applicable, 0 exception of 24 items.**
