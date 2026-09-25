# Soil sensor: capacitive, not resistive

## Question

Which sensor measures soil moisture reliably for a whole season in wet ground?

## Options

- Resistive fork probe, £0.60: two bare electrodes in the soil.
- Capacitive sensor v2, £3.10: electrodes sealed under the board's coating.
- TDR probe, about £40: laboratory grade.

## Evidence

- Measured: a resistive probe and a capacitive sensor side by side in a watered pot for
  three weeks. The resistive probe's reading drifted 41% as its electrodes corroded; the
  capacitive sensor's drifted 3%. Readings logged daily, `bench/sensor-drift.csv`.
- Source: the resistive probe's own listing says to power it only while reading, because
  current through wet soil corrodes the electrodes.
- The TDR probe is accurate but costs more than twice the whole kit's target price.

## Decision

The capacitive sensor. It is read through one analogue input in `firmware/sensor.c`, so a
different sensor changes that one file and a calibration table.

## Revisit

If the drift over a full season, from the first ten kits, is more than 10%.
