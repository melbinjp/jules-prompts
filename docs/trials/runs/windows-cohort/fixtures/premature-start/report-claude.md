**Verdict: the sensor choice is a good start, but the rest was built ahead of evidence.** Two of the owner's own requirements are not met by the current design: a season on one set of batteries, and a £15 price.

Holds up: capacitive over resistive is well backed (bench/sensor-drift.csv: resistive 41.0% vs capacitive 3.0% drift over 21 days, three weeks not a season). The sensor sits behind one file, firmware/sensor.c.

Fails:
- Battery life: firmware/config.h sends a reading every 10 s, about 48 mA, so two AAs last 2.2 days at best. Hourly wake gives about 509 days at 70%. The 0.01 mA sleep figure is a datasheet number, unmeasured.
- Price: firmware/BOM.md totals £18.10 at 100 kits against the £15 target, a loss of £3.10 per kit before shipping, fees and cloud costs.
- Platform: GrowCloud IoT was picked after one search, taking the first result. Its £29/month tier cannot be carried by a £15 kit, and no alternatives were compared.
- Architecture: PLAN.md describes Kafka, Postgres, Redis and four services "so it scales"; docker-compose.yml lists eight services but only services/readings/index.js exists.
- Milestones are layered (backend, app, firmware, integration), so nothing is usable until the end.
- DEPLOY.md says to ask the agent, so the procedure lives in one agent's session.
- The goal "Revolutionise allotment gardening with AI" cannot be measured; a replacement goal and four measures are proposed.
- Not yet considered: radio compliance for selling a Wi-Fi device, a privacy notice, support, distribution.

Next steps: find out whether the allotment has Wi-Fi; measure real sleep current; redo the parts list; choose the platform with written criteria; switch to hourly wake; build one kit end to end; run a ten-kit trial.

Counts: 2 verified, 6 failed, 2 not verified, 1 proposed of 11 items.
