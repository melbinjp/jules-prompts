# Sensor datasheets

The sensor vendor's entire public datasheet archive (all 214 documents, every sensor family,
not only the one Heron uses), downloaded in one bulk transfer on 2026-08-01 from a profile
kept for fetching: no sign-in, no sync, cleared afterwards. Each file's SHA-256 is in
`MANIFEST.sha256`, checked on arrival. Searched locally since; nothing about which sensor
Heron uses left the machine.

The PDFs themselves live in the local documentation store (`/srv/docs/sensor-vendor/`), not in
the repository; this manifest is how the repository checks them.
