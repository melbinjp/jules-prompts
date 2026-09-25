# Expected report for vendor-comparison

The question in D0003 names two products, not the job. As a job it reads: where do 1,000 GB of MP3s live, growing by 100 GB a year, so that listeners can download 5,000 GB a month, at links that never change, for $60 a month or less (M1, M2)? `check_trace.py` passes on this ledger, because the record has the right shape. Every finding below is about its substance.

## Criteria

- criteria-not-from-measures: "Popularity" (40%) and "developer experience" (30%) come from no measure, journey or constraint. M1 is a hard limit of $60 a month, so cost is pass or fail, not a 30% weight. M2, links that never change, is not a criterion at all, and it is the one that decides the door. Rewritten criteria: under $60 a month at today's traffic and at the target (hard limit, M1); public URLs on a domain the station controls (hard limit, M2); a second copy in another place (M3); the effort for a volunteer to run it.

## Options

- missing-options: only the two vendors from the search. Missing are doing nothing (the studio NAS already holds the files, and could serve them if the uplink allows), a combination (the FLAC and MP3 masters on the NAS as one copy, with a host serving the MP3s as the other, which also meets M3), and community archives that host radio collections for free. Each is ruled in or out on the hard limits, with its reason written.

## Evidence and arithmetic

- egress-arithmetic: the record prices transfer out as 0.09 x 5 = $0.45, reading 5,000 GB as 5. Redone, with the price lists in `pricing/`:
  - CloudA: storage 1,000 GB x $0.023 = $23.00, plus egress 5,000 GB x $0.09 = $450.00. Total $473.00 a month, nearly eight times M1.
  - CloudB: storage 1,000 GB x $0.035 = $35.00. Downloads are free up to three times the stored volume (3,000 GB), and the other 2,000 GB x $0.01 = $20.00. Total $55.00 a month. It passes M1 by $5.
  - Sensitivity: CloudB crosses $60 at 5,500 GB of downloads a month, a rise of 10%, so on its own it is one good month from breaking M1. At ten times today's traffic, CloudA is $4,523 and CloudB $505.
  - The term that dominates is egress, which the record got wrong by a factor of 1,000. Corrected, the ranking flips.
- vendor-claim-only: the only source on quality is CloudA's own page, https://cloud-a.example/why-cloud-a, including its table comparing itself with CloudB. That is marketing, not evidence.
- unrepresentative-test: the speed test uploads a 2 MB file from the office. The use is listeners downloading 60 MB shows on phones, so the measure that matters is download time from outside the studio, for a real show file.

## The door

- door-misclassified: D0003 says two-way. CloudA's standard tier serves only from `<bucket>.cloud-a.example`, so every podcast feed and blog post would carry CloudA's URL. Leaving would then break every one of those links and fail M2. That makes it a one-way door, and it needs three options, two independent kinds of evidence, an exit and the station manager's approval. Its revisit condition, "never, unless CloudA changes its prices", would not fire even at eight times the budget.

## Recommendation

A portfolio. Keep the masters on the NAS (D0002 already keeps the FLAC there), and serve the MP3s from CloudB behind a domain the station controls, such as `audio.riversideradio.example`. That puts M2 on the station's own domain, whoever serves it. Switch condition: downloads over 5,300 GB for two months running, measured from the host's logs, triggers the switch plan (a free community archive for the older decades, or a flat-rate host). Exit: repoint the domain after copying the files, about a day, with no link changed. This needs the station manager's approval as a one-way door, sent once with the table above.

D0002, the audio format, is done right. Its criteria were written before the comparison and tied to M2 and M3, and it had four options. Its evidence is independent: a blind ABX test, the podcast apps' own support pages, and arithmetic. Its exit is a re-encode from the FLAC masters. Nothing in it needs changing.

## Verdicts

| item | evidence | verdict |
|---|---|---|
| question framed as the job, tied to IDs | names two products; serves M1 and M2 | broken |
| criteria from measures, set before scoring | popularity and experience come from nothing | broken |
| doing nothing, building and combining considered | two vendors only | broken |
| evidence independent | the vendor's own page | broken |
| every number redone | egress off by a factor of 1,000 | broken |
| test shaped like the use | a 2 MB upload from the office | broken |
| flipping assumption named | none | broken |
| door, exit and approval | two-way recorded, one-way in fact | broken |
| revisit condition | "never, unless..." | broken |
| audio format decision (D0002) | criteria dated first, ABX test, exit through the masters | holds |
| studio uplink could serve the NAS directly | uplink speed not recorded in the ledger | skipped |

11 items: 1 holds, 9 broken, 1 skipped.

defect_id: criteria-not-from-measures
defect_id: missing-options
defect_id: egress-arithmetic
defect_id: vendor-claim-only
defect_id: unrepresentative-test
defect_id: door-misclassified
