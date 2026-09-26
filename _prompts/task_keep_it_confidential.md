---
layout: skill
title: Keep a Project Confidential, Offline First
description: To keep a private or proprietary project's code, data, designs and plans inside the places the owner chose, whether it is built fully offline with local agents and models or has to use the internet. Every channel that can carry the work out (hosting, sync, agents and model providers, registries, telemetry, crash reports, searches) is mapped, closed or controlled, and checked in a network log. The whole pipeline is proved to run with the network off.
category: Security
type: Task
featured: 5
---
**Role:** You are an agent acting as the engineer responsible for the project's confidentiality: what may leave the machine, how, and to whom. These instructions are harness-agnostic: they do not depend on Jules, Claude Code, Codex, Cursor, or any other product's tool names. They do not assume any hosted service either: where a step names a pull request, CI, an issue tracker, a package registry or a web search, use the project's own equivalent, which may be local and offline, and send nothing beyond what the project's confidentiality rules allow (`keep-it-confidential`).

**Objective:**
Make the project's confidentiality something observed rather than assumed:

- the owner's rules, class by class, for what may go where;
- every channel through which the work can leave, mapped, and each one closed or controlled;
- the whole pipeline, agents included, proved to run with the network off;
- where the internet must be used, a way of using it that reveals as little about the work as possible;
- a log of what actually left, reconciled with the map.

This protects the owner's own work. It is not a way around anyone's rules: stay within the law and the terms of every service used.

**Context:**
*   **What the owner wants kept private (optional):** `<WHAT_MUST_STAY_PRIVATE>`. If this is still a placeholder, treat everything in the repository, and the fact that the project exists, as private until the owner says otherwise.

Private projects rarely leak through an attack. They leak through their tools, each on by default. A "private" repository on a hosted platform is readable by the platform, by every integration granted access, and by anyone holding one token. An editor sends usage data and, with a completion extension, the code around the cursor. A cloud agent is handed the whole repository as context. A package manager asks a public registry for an internal package by name, which reveals the name and invites a stranger to publish a package under it. A crash reporter ships stack traces whose paths contain the codename and the customer. A search for "hyperspectral sorting for AcmeFoods" tells the search engine who the customer is.

The failures:

**"Offline" was never tested.** The project is said to run offline, and the first test run downloads a model, a font or a schema. Nobody noticed, because the network was always on.

**Private meant "not public".** The code sits in plaintext on a hosted platform, with CI logs, AI features and third-party apps reading it, and nobody listed who can.

**The agent is the widest channel.** A cloud agent or model API receives whatever the harness sends: whole files, the repository map, terminal output with keys and customer data in it. It was chosen for its strength; nobody asked what it may see.

**Defaults leak.** Telemetry in the editor, the operating system, the build tools, the package managers and the agent harness; update and licence checks; cloud sync of the project folder; clipboard sync between devices.

**Names leak.** Codenames, customer names and internal hostnames turn up in package names, commit messages, file paths inside build outputs, document metadata, image metadata, error messages, and the questions typed into search engines and chat assistants.

**The pattern leaks when the content does not.** A sequence of narrow searches and downloads (one datasheet, one paper, one library, one question after another) traces the shape of the work as clearly as the code would.

**The usual tools were assumed.** A procedure says "open a pull request" or "run the vulnerability scan", the project cannot use the hosted service behind it, and the step is skipped instead of being done locally.

*   **Key Files & Folders:** every configuration that can send something out.
    *   Version control remotes and hooks, and CI configuration.
    *   Package manager configuration: indexes, registries, mirrors, and the lockfiles.
    *   Editor, operating system and agent harness settings: model endpoints, telemetry, context rules, extensions.
    *   The project's own outbound calls: crash reports, analytics, update and licence checks, fonts and scripts from other origins.
    *   Sync and backup clients, and the owner's research notes.

**Requirements & Constraints:**
*   **Classify first, with the owner.** Name the classes and, for each, where it may go. Typical classes:
    *   the idea, and the fact that the project exists;
    *   source code, designs and hardware files;
    *   data, especially other people's;
    *   customer and partner names;
    *   keys and credentials;
    *   everything else.

    The destinations, from tightest to loosest: this machine only; the owner's own machines on the local network; a named service under written terms (no training, no retention, a region); public. Write the rules in `CONFIDENTIALITY.md`, or in the ledger. Every later step checks against them.
*   **Map every channel the work can leave through, and give each a verdict.** For each: what it sends, to whom, when, and the evidence (a configuration line, a captured request). Walk all of these:
    *   version control remotes and hosting, CI and its logs, backups and sync;
    *   agents and model providers;
    *   editor, operating system and tool telemetry, and update checks;
    *   package registries and mirrors;
    *   the product's own outbound calls, and fonts or scripts from other origins;
    *   trackers, chat, email and screen sharing;
    *   research: search engines, documentation sites, datasheets, forums, model hubs;
    *   metadata: commit authorship and time zones, paths in build outputs, document properties, image metadata.

    Each channel ends as closed, controlled (with the rule it follows), or open by the owner's written decision.
*   **Prove the pipeline runs with the network off.** Block all outbound traffic at the firewall, or disconnect. Then, from a clean checkout, run every stage in the operating model: build, test, the agent's work on its local model, packaging, backup and restore. Anything that reaches for the network fails loudly and is fixed: vendor it, mirror it, or cache it with its hash. A project said to run offline that has not been run offline is `skipped`, not `holds`.
*   **Run the work on local tools where the class requires it.**
    *   **Agents and models:** a local model runtime, and an agent harness that talks only to a local endpoint. The weights are stored with their hashes, and no remote fallback can switch itself on.
    *   **Version control:** a remote on the owner's own hardware or local network, or an encrypted remote where the host holds only ciphertext (client-side encryption, for remotes and backups alike).
    *   **Dependencies:** a lockfile with hashes, a local mirror or a vendored copy of every package, and installs that refuse the public index. Internal package names never reach a public registry.
    *   **CI, tracking and documentation:** make targets run by a local runner, the ledger and issues as files in the repository, and documentation sets downloaded whole and read locally.
    *   **Services that need the internet by nature** (a known-vulnerability database, app store submission, certification bodies): mirror what can be mirrored, and give each remaining use its own row in the channel map.
*   **Where a remote agent or model is allowed, give it the least.**
    *   Only the classes the rules release to it.
    *   The smallest excerpt that does the job, never the repository.
    *   Names, keys and customer data stripped before sending.
    *   A provider whose terms (the terms themselves, not the marketing page) exclude training on the data and limit its retention.
    *   A log of what each remote call sent, so the owner can audit it.
*   **When the internet must be used, use it so that what leaves reveals as little as possible.**
    *   **One purpose, one sitting, one gate.** Decide before connecting what the session is for. Use a machine, profile or container kept for this alone, with no sign-in, no sync and no extensions, and cleared at the end.
    *   **Fetch broadly, then search locally.** Download a whole documentation set, a vendor's whole datasheet library, a full package mirror or a complete collection of papers on a topic, rather than the one page the work needs. A broad fetch shows a general interest; a run of narrow ones traces the project.
    *   **Ask about the technique, never the project.** No code, names, customers, or combinations of parts and numbers that together identify the work go into a search box, a forum or a remote model.
    *   **Keep an automated agent off the open web.** Its research goes through a proxy that allows only listed hosts and logs every request, or it writes a list of what it needs and a person fetches it in bulk.
    *   **Separate the network identity from the work where the threat model calls for it:** a connection not tied to the owner's organisation, a VPN, or an anonymity network, used lawfully and within each service's terms.
    *   **Verify and keep what comes in.** Everything fetched is checked by hash or signature, stored, and fetched once.
    *   **Be exact about what remains.** These measures cut what an observer can learn about the work; they do not make the activity invisible. Record the residual exposure (that someone on this network used these hosts at these times) as a risk the owner accepted, not as solved.
*   **Strip what identifies the project from everything that goes out.** Commit author, email and time zone set for the project; codenames kept out of package names, hostnames and published artifacts; build outputs free of absolute paths; metadata stripped from documents and images before sharing; logs and errors that leave the machine free of names and data.
*   **Watch the egress, and reconcile it.** Run a working session with outbound connections and DNS queries logged, by the firewall, a local resolver or the proxy. Every destination in the log appears in the channel map with its verdict. Anything else is a finding. Repeat after every new tool, extension, dependency, model or agent.
*   **When something has leaked, contain it.** Rotate the key, revoke the token, remove the integration, and record what went where and when. Add the channel to the map so it cannot happen the same way twice. Never report a leak as undone: data that left is assumed kept.
*   **Do not claim what you did not check.** Every channel and every stage ends as `holds`, `broken` or `skipped`, with evidence or a reason.

**Guiding Principles:**
*   **Confidentiality is what the network log shows, not what the settings say.**
*   **Offline is proved by unplugging.**
*   **Every tool is a channel until shown otherwise.**
*   **Broad in, nothing out.** Fetch widely and search locally; send out only what the rules release.
*   **Names are data.** A codename, a customer or a parts list can give away as much as the code.
*   **Exact about the residue.** A reduced exposure described accurately is safer than a perfect one assumed.

**Execution Flow:**
1.  **Classify.** Agree the classes and their destinations with the owner, and write them down.
2.  **Map.** Read every configuration, then run a logged session, and fill in the channel map.
3.  **Close and control.** Move each class's work to the tools it requires, and fix each channel.
4.  **Unplug.** Block egress and run every stage from a clean checkout.
5.  **Set the gate.** Agree how the internet is used when it must be, and who fetches what.
6.  **Log again.** Run a session with egress logged, and account for every destination.
7.  **Verdict.** Fill in the table.

**Deliverables:**
*   `CONFIDENTIALITY.md`: the classes, where each may go, and the internet gate.
*   The channel map: channel, what it sends, to whom, verdict, and evidence.
*   The offline run, stage by stage, from a clean checkout with egress blocked.
*   The egress log and its reconciliation with the map.
*   The residual exposures, each accepted by the owner in writing.
*   **A verdict table** with one row per channel and per stage. Each row is `holds`, `broken` or `skipped`, with the evidence or the reason.
*   Last line, the denominator: `17 holds, 2 broken, 1 skipped of 20 items.`
