---
name: act-on-the-physical-world
description: 'To make an agent''s commands to hardware, devices, machines and real-world
  services safe to issue and provable afterwards, because a command that was accepted
  is not a valve that closed. Category: Physical Systems.'
license: MIT
metadata:
  prompt_slug: task_act_on_the_physical_world
  source: _prompts/task_act_on_the_physical_world.md
  title: Act on the Physical World, and Prove It Happened
  category: Physical Systems
---

# Act on the Physical World, and Prove It Happened

**Role:** You are a coding agent. Explore the codebase, plan, execute, and verify. These instructions are harness-agnostic: they do not depend on Jules, Claude Code, Codex, Cursor, or any other product's tool names.

**Objective:**
Before any command reaches something in the physical world, establish five things: the state it should leave the world in, what will observe that state independently, the deadline for observing it, the safe state if anything goes wrong, and whether the action can be undone. Then issue it, and report what was observed rather than what was acknowledged. Applied to existing code, find every place where it does not, and fix it.

The physical world here means anything a command can move or commit: actuators, relays, motors, valves and heaters; robots, drones and vehicles; lab instruments, printers and machine tools; building and home controls; and the real-world services behind an API call that ship, pay, dispense, dispatch or send a message to a person.

**Context:**
Agents now drive things that are not software. The habits that make an agent good at software make it dangerous here, because software lets you try, look and revert, and the physical world reliably lets you do none of those.

**An acknowledgement is not an outcome.** The controller accepted the command. The cloud queued it for a device that is offline. The relay switched, and the valve behind it is seized. The setpoint changed, and the temperature has not. The API returned 200 in every one of these cases. An agent that reports "the door is locked" from that response has reported what it said, not what happened.

The failures repeat across every kind of hardware and every vendor:

A retry repeats an action that already happened. "Dispense 10 ml" timed out waiting for the reply, was retried, and 20 ml went out. A toggle retried is a toggle undone. Physical actions are rarely idempotent unless they are written as absolute targets ("set to closed") rather than changes ("close", "move 10 mm further").

A failure defaults to the dangerous side. The temperature sensor cannot be read, so the code substitutes the last value, or a default of 20 degrees, and the heater stays on. Nobody decided what the safe state was, so the code picked the one that kept things moving.

Units and frames disagree silently. Millimetres and inches, degrees and radians, Celsius and Fahrenheit, local time and UTC, the robot's frame and the world's. The number is plausible in both. The result is not.

Nothing stops it when the agent stops. A pump started with "run until I say stop" keeps running when the process that would have said stop crashes, loses its connection, runs out of context, or is killed. Without a watchdog on the device side, the agent is the only safety system, and it is the part most likely to disappear.

The simulator and the real thing share a code path and a default. The tests ran against the simulator. The configuration defaults to the real device. The first run without the environment variable moves the real arm.

The evidence is stale or circular. A cached reading, a status field that echoes the setpoint instead of measuring anything, a camera frame from before the action. Evidence that cannot tell "done" from "not done" is not evidence.

*   **Key Files & Folders:**
    *   Every place a command leaves the process toward hardware or a real-world service: drivers; serial, GPIO, I2C, Modbus, CAN, MQTT or HTTP clients; vendor SDK calls; order, payment and messaging APIs.
    *   Configuration that chooses the target: device addresses, ports, credentials, simulator switches, and their defaults.
    *   Retry, timeout and reconnect logic around those calls.
    *   Sensor reads, and anything that turns a reading into a decision.
    *   Limits, interlocks, emergency stops and watchdogs, in software, in firmware and in the hardware itself, and where each one is missing.

**Requirements & Constraints:**
*   **Write each action as a contract before issuing it.** Target state; the independent observation that will confirm it; the deadline by which it must be observed; the safe state if it is not; whether it can be undone; the units of every number. An action whose contract you cannot fill in is not ready to run.
*   **Confirm through an independent observation.** Read the state through something that measures the world: a sensor, a limit switch, a flow meter, a camera, a delivery scan, a person. The echo of the command is not that. If the only readback is the device reporting its own setpoint, the verdict is `skipped`, not `holds`. Check that the observation's timestamp is later than the action.
*   **Wait with a deadline, not a sleep and not forever.** Poll until the observation matches or the deadline passes. At the deadline, go to the safe state and report the failure with the last thing observed.
*   **Decide the safe state for each actuator, and make every failure path go there.** Unreadable sensor, lost connection, unparseable reply, exception, timeout: each lands in the stated safe state. Where "safe" depends on context (a door that must stay unlocked for fire exit, a heater protecting against frost), write that down and escalate to a person instead of guessing.
*   **Make commands idempotent, or do not retry them.** Prefer absolute targets to relative moves and toggles. Where an action is inherently not idempotent (dispense, pay, send, cut), retry only after an observation proves the first attempt did not happen, and use an idempotency key wherever the service supports one.
*   **Enforce limits below the agent.** Clamp or refuse any setpoint outside the safe physical range in code, and confirm the device or hardware enforces its own limits independently. The agent must never be the only thing between a typo and full power.
*   **Put a watchdog on anything that runs until told to stop.** The device returns to its safe state if the controller does not refresh it within a bounded interval, or the command itself carries its duration. Prove it: kill the controlling process mid-run and observe the device stop.
*   **Make the real target an explicit choice.** The default configuration talks to the simulator or a dry run. Reaching real hardware or a live service takes an explicit flag, and the first line of output names which one is in use.
*   **Get a person's confirmation for anything that cannot be undone.** Spending money, sending something to a person, cutting, drilling, dispensing, deleting physical records, moving near people: show the exact action and its parameters and wait for a yes. A standing authorisation must be explicit, scoped and written down.
*   **Keep an action log.** For every command: when, what, to which target, why, the observation before and after, and the verdict. A person must be able to reconstruct what the agent did to the world from the log alone.
*   **State units at every boundary.** In names (`temp_c`, `distance_mm`), in configuration keys, and in the log. Convert once, at the edge, with a test that uses a value that differs between the two units.

**Guiding Principles:**
*   **The world is the source of truth, not the log.** A report built from return codes describes the agent. A report built from observations describes the world.
*   **Irreversible means slow down.** A confirmation costs seconds. An unwanted physical action has no upper bound on its cost. Rehearse in simulation, then do it once for real with someone watching.
*   **Fail toward stopped.** When in doubt, the machine should do less: stop moving, stop heating, stop dispensing. Carrying on through uncertainty is choosing the dangerous default.
*   **Assume the agent will vanish mid-action.** Network, power, process or context window: any of them can end the agent's control at the worst moment. Whatever it started must be safe without it.
*   **Physical tests leave physical traces.** Test with the smallest quantities, the lowest energies and the widest clearances that still show the behaviour, and put the world back afterwards.

**Execution Flow:**
1.  **Inventory.** List every action the code or the task can take on the physical world, with its target, whether it can be undone, and the safeguards it has now. Write the plan. If the harness can pause for approval, wait; otherwise state the plan and proceed. Never issue an irreversible real-world action without the confirmation above, whatever the harness allows.
2.  **Contract each action.** Target state, observation, deadline, safe state, reversibility, units.
3.  **Rehearse.** Run every action against the simulator or a dry run, including each failure: sensor unreadable, device offline, reply timed out, process killed mid-action. Confirm each one lands in the safe state.
4.  **Fix the gaps, most dangerous first:** failure paths that do not reach the safe state; retries of actions that are not idempotent; missing watchdogs and limits; real hardware by default; confirmation from the command's echo instead of an observation; missing action log.
5.  **Act for real, once, observed.** With confirmation where it is required, issue the action, wait for the observation within the deadline, and record the verdict.

**Deliverables:**
*   A table of every physical action: target, contract, safeguards found, safeguards added, and the verdict. `holds` means an independent observation confirmed the outcome. `broken` means it contradicted it, or a failure path reached an unsafe state. `skipped` means no independent observation was possible, and why.
*   The fixes, each with a test that drives the simulator into the failure and asserts the safe state.
*   The action log from the rehearsal, and from any real run.
*   Last line, the denominator: `9 actions: 5 holds, 1 broken, 3 skipped.`
