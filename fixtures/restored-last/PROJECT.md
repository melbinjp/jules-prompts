# Boxwell

## Journeys that must never fail

| id | journey |
|---|---|
| J1 | A subscriber is charged once for each month's box, and gets one invoice for it. |
| J2 | A subscriber pauses or cancels, and is not charged again. |

## Success measures

| id | what | target | how it is measured |
|---|---|---|---|
| M1 | subscribers charged more than once in a month | 0 | the nightly reconciliation against the payment provider |
| M2 | help messages about billing | under 10 a week | the help inbox, tagged |

## Standing limits for the on-call agent (from BRIEFING.md)

The on-call agent may, on its own: roll back to the previous release, turn off a feature flag,
pause the billing worker. It may not: delete or edit data, change or silence alerts, deploy new
code, or contact subscribers. For anything else it pages Priya (the owner) by phone.
