---
id: D0002
status: accepted
serves: [M2, M3]
door: one-way
approved_by: J. Adeyemi, station manager
revisit: when more than 5% of listeners use a podcast app that plays Opus
decided: 2026-08-02
---
# Serve MP3 at 128 kbps; keep the FLAC masters

## Question

In what format do listeners get each show, and in what format is it kept?

## Criteria

Written 2026-07-28, before any format was compared.

- Plays in every podcast app and browser listeners use (M2). Pass or fail.
- Size per hour of speech and music, which sets the download cost (M1).
- Lossless masters can be re-encoded later, so the serving format is not a one-way door (M3).

## Options

- MP3 at 128 kbps: about 58 MB an hour.
- AAC at 96 kbps: about 43 MB an hour.
- Opus at 64 kbps: about 29 MB an hour.
- FLAC only: about 350 MB an hour.

## Evidence

- Measured: a blind ABX listening test, 12 volunteers, 20 trials each, where chance is 10
  and 15 is the 5% threshold. Nobody reached 15 for MP3 128 or AAC 96 against the FLAC
  master; 7 of 12 did for Opus 64 on the music clips. Results in `listening-test.csv`, from
  the committee's session on 2026-07-30.
- Primary sources: the support pages of the six podcast apps our listeners use most (from the
  feed's user agents). MP3 and AAC play in all six; Opus in two.
- Calculation: FLAC served would be 6 times the transfer of MP3, so it fails M1 on any host
  that charges for downloads.

## Decision

Serve MP3 at 128 kbps, the only option that passes the plays-everywhere limit at a size
close to the smallest. Keep FLAC masters on the NAS, so any later format is a re-encode.

## Exit

- Moving to another format is a batch re-encode from the FLAC masters: about 40 hours of
  compute on the studio machine, and the feeds updated to the new files.
