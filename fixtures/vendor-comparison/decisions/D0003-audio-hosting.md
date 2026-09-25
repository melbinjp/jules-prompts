---
id: D0003
status: accepted
serves: [M1, M2]
door: two-way
revisit: never, unless CloudA changes its prices
decided: 2026-09-01
---
# Host the public archive on CloudA

## Question

Should we use CloudA or CloudB for the audio?

## Criteria

| criterion | weight |
|---|---|
| Popularity | 40% |
| Developer experience | 30% |
| Cost | 30% |

## Options

- CloudA object storage.
- CloudB object storage.

## Evidence

- Source: CloudA's own page, https://cloud-a.example/why-cloud-a, says it is "the most
  trusted storage on earth" and shows it ahead of CloudB on every row of its comparison table.
- Measured: a speed test. Uploaded a 2 MB test file from the office to each; CloudA took
  0.4 s, CloudB 0.6 s.
- Calculation: monthly cost, from the price lists. CloudA: storage 1,000 GB x $0.023 =
  $23.00, transfer out 0.09 x 5 = $0.45, total $23.45. CloudB: storage 1,000 GB x $0.035 =
  $35.00, downloads free, total $35.00.

## Scores

| option | popularity | developer experience | cost | weighted |
|---|---|---|---|---|
| CloudA | 10 | 9 | 10 | 9.7 |
| CloudB | 6 | 7 | 7 | 6.6 |

## Decision

CloudA. It is the most popular, has the best tools, and is the cheapest.
