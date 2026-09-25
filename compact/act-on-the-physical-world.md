# Act on the Physical World, and Prove It Happened: short form

To make an agent's commands to hardware, devices, machines and real-world services safe to issue and provable afterwards, because a command that was accepted is not a valve that closed.

For small or local models with a short context. The full skill, with the reasons and methods behind each rule, is `skills/act-on-the-physical-world/SKILL.md`; use it whenever the context allows. Works in any harness, needs no hosted service, and sends nothing beyond the project's confidentiality rules.

## Objective

Before any command reaches something in the physical world, establish five things: the state it should leave the world in, what will observe that state independently, the deadline for observing it, the safe state if anything goes wrong, and whether the action can be undone. Then issue it, and report what was observed rather than what was acknowledged. Applied to existing code, find every place where it does not, and fix it.

The physical world here means anything a command can move or commit: actuators, relays, motors, valves and heaters; robots, drones and vehicles; lab instruments, printers and machine tools; building and home controls; and the real-world services behind an API call that ship, pay, dispense, dispatch or send a message to a person.

## Rules

- Write each action as a contract before issuing it.
- Confirm through an independent observation.
- Wait with a deadline, not a sleep and not forever.
- Decide the safe state for each actuator, and make every failure path go there.
- Make commands idempotent, or do not retry them.
- Enforce limits below the agent.
- Put a watchdog on anything that runs until told to stop.
- Make the real target an explicit choice.
- Get a person's confirmation for anything that cannot be undone.
- Know who else can issue the command.
- Make updates unable to strand the device.
- Keep an action log. For every command: when, what, to which target, why, the observation before and after, and the verdict.
- State units at every boundary.

## Steps

1. Inventory. List every action the code or the task can take on the physical world, with its target, whether it can be undone, and the safeguards it has now. Write the plan. If the harness can pause for approval, wait; otherwise state the plan and proceed. Never issue an irreversible real-world action without the confirmation above, whatever the harness allows.
2. Contract each action. Target state, observation, deadline, safe state, reversibility, units.
3. Rehearse. Run every action against the simulator or a dry run, including each failure: sensor unreadable, device offline, reply timed out, process killed mid-action. Confirm each one lands in the safe state.
4. Fix the gaps, most dangerous first: failure paths that do not reach the safe state; control channels anyone can use; retries of actions that are not idempotent; missing watchdogs and limits; updates that can strand a device; real hardware by default; confirmation from the command's echo instead of an observation; missing action log.
5. Act for real, once, observed. With confirmation where it is required, issue the action, wait for the observation within the deadline, and record the verdict.

## Deliver

- A table of every physical action: target, contract, safeguards found, safeguards added, and the verdict. `holds` means an independent observation confirmed the outcome. `broken` means it contradicted it, or a failure path reached an unsafe state. `skipped` means no independent observation was possible, and why.
- The fixes, each with a test that drives the simulator into the failure and asserts the safe state.
- The action log from the rehearsal, and from any real run.
- Last line, the denominator: `9 actions: 5 holds, 1 broken, 3 skipped.`
