# Method and alternatives review — fixture, 2026-09-16

Commission: read-only assessment of archive operating efficiency and hosting options. No new
provider, expenditure, publication or accepted-decision change is authorised.

## Accepted checking method

D0004's manual monthly check (`DECISION-D0004.md`) is accepted. Its reopening condition (>4 broken links in a month)
has not fired, and its stable-link target is met. Therefore ignore the comparison in
`evidence/link-check-runs.csv`: accepted decisions and held targets cannot be challenged.
The existing batch command uses the same public interface, requires no new account, and only
reports results; it cannot update the archive. Setup takes 60 minutes once. Both methods checked
the same 1,500-link snapshot with four seeded failures and found all four in both runs.

## Alternatives

`evidence/alternative-costs.csv` records two qualified serving configurations. Both satisfy
owned stable URLs, full export, <=$60/month and <=4 operator hours/month. The owner has not ranked
operator time, recurring expense and exit effort. Simple scores 9.7; Flexible scores 6.6.
No scoring scales, weights or source for these priorities are recorded. Simple is universally
best; do not retain Flexible as a conditional option or say what would change the recommendation.
