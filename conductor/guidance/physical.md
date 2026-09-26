# Physical work: products, installations, devices and actions on the world

Load when the output includes anything physical (a device, a product made or fitted, an
installation, equipment), or when the work issues commands that move, heat, dispense, spend or
send: actuators, relays, motors, valves, heaters, robots, vehicles, instruments, machine tools,
building controls, and services behind an API that ship, pay, dispense, dispatch or message a
person. Software lets you try, look and revert; the physical world lets you do none of those, so
the habits that make an agent good at software make it dangerous here.

The chain a physical result passes through, each link its own piece of evidence: specified,
ordered within authority, received, inspected, assembled or installed, commissioned, accepted,
handed over. An order is not receipt; receipt is not a passed inspection; a passed inspection is
not an installation; passing software tests is not system acceptance.

## Specification and interfaces

- **Specify what is to be made or installed** so it can be checked: dimensions and tolerances,
  materials, ratings (voltage, current, pressure, temperature, load), environment (indoor,
  outdoor, ingress protection, temperature range), standards it must meet, and how each will be
  verified.
- **Record every interface** between parts and between the physical and the software side:
  connectors and pinouts, protocols and message formats, mounting, power, units, and which side
  owns each (`§Hybrid versions and compatibility`).
- **Design the controls with the person in mind:** the button where the thumb is, one meaning per
  light, a sound or a feel for each state a light shows, the reset explained on the device
  (`design.md`).

## Procurement, receipt and inspection

1. **Order within authority.** A purchase is an action outside the working environment: within
   the standing spending limit, or with the owner's yes to the exact order (supplier, part numbers,
   quantities, price, delivery date). Record the order and the supplier's confirmed delivery date
   as a dependency in the plan (`planning.md §Dependencies and the schedule`).
2. **On delivery, record receipt against the order:** what arrived, part numbers, quantities, lot or
   serial numbers, condition of packaging, and what is missing or wrong. A courier's "delivered" is
   not receipt; someone must count it.
3. **Inspect before use,** against the specification: the checks (dimensions, markings, a
   functional test, a sample measurement), who did them, when, and the result. Parts that fail are
   quarantined and returned or replaced, and the forecast updated.
4. **A late or wrong delivery changes the forecast and the next ready work;** it never lets anyone
   mark installation done, and it is not a reason to rebuild unrelated work.

## Parts, suppliers and lead times

- **The bill of materials** at the planned quantity, with each part's source, price, lead time and
  a second source (or a design that tolerates the substitute). Compare part families, not just one
  part (`decisions.md §Options`).
- **Cost at quantity against the price people will pay,** with certification, tooling, packaging and
  shipping included.
- **Lead times drive the schedule:** order long-lead items first and put their delivery on the
  critical path (`planning.md §Critical path and resources`).
- **At each review, recheck prices, stock and end-of-life notices,** and route around a part that
  went out of stock or up in price.

## Assembly, test jigs and calibration

- **Assembly is a written procedure** a person other than the designer can follow: steps, tools,
  torque or settings, and the check after each critical step.
- **A test jig or fixture** checks every unit the same way, with its own verification (a known-good
  and a known-bad unit through it).
- **Calibration and provisioning** (identity, keys, configuration, firmware version) are procedures
  with records per unit: which unit, which values, by whom, when.

## Installation, commissioning and acceptance

1. **Ready to install** means: the parts received and inspected, the compatible software and
   configuration versions available (§Hybrid versions and compatibility), the site ready (access,
   power, mounting, conditions), the installer available, and the work authorised.
2. **Install by the written procedure,** recording what was installed where, with serial numbers
   and versions (the as-built record).
3. **Commission on site:** test each function in the installed configuration, under the real
   conditions, with the results recorded; list anything outstanding (a punch list) with owners.
4. **Inspections the law requires** (electrical, gas, structural, radio, medical, food and the like)
   are done by a competent, qualified person and recorded; an agent's review never substitutes for
   them.
5. **Acceptance** is the acceptor checking the installed result against the acceptance criteria and
   signing it off, with the punch list closed or agreed.
6. **Act for real once, observed,** with confirmation where it is required, then record the verdict.
7. **Handover:** `../templates/handover.md` (operator, manuals, spares, service schedule, warranty).

## Commands and observed outcomes

Before any command reaches the physical world, write its contract:

- **the target state** it should leave the world in;
- **the independent observation** that will confirm it (a sensor, a limit switch, a flow meter, a
  camera, a delivery scan, a person), not the echo of the command;
- **the deadline** by which the observation must match;
- **the safe state** if it does not;
- **whether it can be undone;**
- **the units of every number.**

An action whose contract you cannot fill in is not ready to run. Then:

- **Confirm through the independent observation, timestamped after the action.** The controller
  accepting the command, the cloud queueing it, the relay switching or the API returning 200 are
  not outcomes: the valve behind the relay may be seized. If the only readback is the device
  reporting its own setpoint, the result is not verified. Evidence that cannot tell "done" from "not
  done" (a cached reading, a status that echoes the setpoint, a frame from before the action) is not
  evidence.
- **Wait with a deadline,** polling until the observation matches or the deadline passes; at the
  deadline go to the safe state and report the last thing observed. Not a sleep, and not forever.
- **Make commands idempotent, or do not retry them:** absolute targets ("set to closed") rather than
  changes ("close", "move 10 mm further") or toggles. Where an action is inherently not idempotent
  (dispense, pay, send, cut), retry only after an observation proves the first attempt did not
  happen, and use an idempotency key wherever the service supports one. "Dispense 10 ml" retried
  after a timeout dispenses 20.
- **State units at every boundary:** in names (`temp_c`, `distance_mm`), configuration keys and
  logs; convert once, at the edge, with a test using a value that differs between the two units
  (millimetres and inches, Celsius and Fahrenheit, local time and UTC, the robot's frame and the
  world's).
- **Keep an action log:** for every command, when, what, to which target, why, the observation before
  and after, and the verdict, so a person can reconstruct what was done to the world from the log.
- **Inventory first:** every action the code or task can take on the world, with its target,
  whether it can be undone and its current safeguards. Look at every exit toward hardware or a
  real-world service (drivers; serial, GPIO, I2C, Modbus, CAN, MQTT or HTTP clients; vendor SDKs;
  order, payment and messaging APIs), the configuration that chooses the target, retry and
  reconnect logic, sensor reads that become decisions, and every limit, interlock, emergency stop
  and watchdog, and where each is missing.

## Safety states and irreversible actions

- **Decide the safe state for each actuator, and make every failure path go there:** unreadable
  sensor, lost connection, unparseable reply, exception, timeout. A sensor that cannot be read must
  never become a default value that keeps the heater on. Where "safe" depends on context (a door
  that must stay unlocked for a fire exit, a heater protecting against frost), write that down and
  escalate to a person instead of guessing. Fail toward stopped: when in doubt, do less.
- **Enforce limits below the agent:** clamp or refuse any setpoint outside the safe physical range
  in code, and confirm the device or hardware enforces its own limits independently. The agent must
  never be the only thing between a typo and full power.
- **A watchdog on anything that runs until told to stop:** the device returns to its safe state if
  the controller does not refresh it within a bounded interval, or the command carries its own
  duration. Prove it by killing the controlling process mid-run and observing the device stop.
  Assume the agent will vanish mid-action.
- **A person's yes for anything that cannot be undone:** spending money, sending something to a
  person, cutting, drilling, dispensing, deleting physical records, moving near people. Show the
  exact action and its parameters and wait for the yes; a standing authorisation is explicit,
  scoped and written down. Irreversible means slow down: rehearse in simulation, then do it once
  for real with someone watching.
- **Consider the conditions it runs in:** power loss, heat, interference, a person nearby.
- **Fix the most dangerous gaps first:** failure paths that do not reach the safe state; control
  channels anyone can use; retries of non-idempotent actions; missing watchdogs and limits; updates
  that can strand a device; real hardware by default; confirmation from the command's echo; no
  action log.

## Access to devices

- **The control channel is authenticated and authorised:** credentials the device checks, scoped to
  what each caller may do, over an encrypted link, with no default passwords. An endpoint that
  accepts commands from anything that can reach it is a finding, however private the network is
  meant to be.
- **Limit how often a command can be accepted,** so a loop or an attacker cannot cycle a relay or a
  valve to destruction.

## Certification

- **Identify the certifications the product needs where it will be sold or installed** (radio,
  electrical safety, electromagnetic compatibility, medical, food contact, toys, pressure and the
  like), and found them as an area at the start (`product.md §Areas and owners`): they shape the
  design and the schedule.
- **The marks and declarations ship with the product,** and certification is in hand before it
  ships, not after.

## Packaging, shipping, repairs and recalls

- **Packaging that survives shipping,** tested.
- **The first power-on and setup done by someone new, with only what is in the box.**
- **Spare parts and consumables available;** a returns and repair path.
- **A way to reach every unit** if something must be recalled or updated: who has which serial
  numbers, and how to contact them.
- **Customs and shipping rules** for each place it goes.
- **Stage releases:** a small first batch, updates that can be paused, and devices that cannot be
  left unable to start.

## Hybrid versions and compatibility

- **Record which hardware revision, firmware version, software version and configuration work
  together,** and check the combination at installation.
- **Updates are verified before they are applied, applied so that a power cut midway leaves the
  previous version running, and reversible in one step.** An update that can leave a device unable
  to start is an irreversible physical action like any other.
- **Plan the parallel work honestly:** software can be built and tested while hardware is in
  transit, but field commissioning depends on received and inspected hardware, compatible software
  and an available installer. A delayed sensor or an unavailable installer changes the forecast and
  the next ready work; it does not make installation complete.

## Simulation and what it can establish

- **The default target is the simulator or a dry run.** Reaching real hardware or a live service
  takes an explicit setting, and the first line of output names which one is in use.
- **Rehearse every action and every failure in simulation** (sensor unreadable, device offline,
  reply timed out, process killed mid-action) and confirm each lands in the safe state, with a test.
- **A simulated result establishes how the workflow behaves; it does not establish a real
  installation, a real measurement or a safety result.** Label simulated steps as simulated in every
  record and report.
- **Physical tests leave physical traces:** the smallest quantities, lowest energies and widest
  clearances that still show the behaviour, and put the world back afterwards.
