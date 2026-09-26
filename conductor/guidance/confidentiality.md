# Confidentiality: keeping the work where the owner chose

Load when the project is private, proprietary or offline, or when any of its work (the idea, code,
data, designs, customer names, even the fact that it exists) must not leave. Load it before anything
is sent anywhere: a search, a remote model, a hosted tool, a forum post. Confidentiality is what the
network log shows, not what the settings say. This protects the owner's own work; stay within the
law and the terms of every service used.

Private projects rarely leak through an attack; they leak through their tools, each on by default.
A "private" repository on a hosted platform is readable by the platform, every integration granted
access, and anyone holding one token. An editor sends usage data and, with a completion extension,
the code around the cursor. A cloud agent is handed the whole repository. A package manager asks a
public registry for an internal package by name. A crash reporter ships paths containing the
codename and the customer. A search for "hyperspectral sorting for AcmeFoods" tells the search
engine who the customer is.

## Classes and where they may go

- **When the owner has not said,** treat everything in the repository, and the fact that the project
  exists, as private until they do.
- **Classify with the owner:** the idea and the project's existence; source code, designs and hardware
  files; data, especially other people's; customer and partner names; keys and credentials;
  everything else.
- **For each class, where it may go,** from tightest to loosest: this machine only; the owner's own
  machines on the local network; a named service under written terms (no training on the data, no
  retention, a region); public.
- **Write the rules in the project's confidentiality record,** with the internet gate
  (§Using the internet without revealing the work). Every later step checks against it.
- **A confidential release goes only to the people its classes allow,** through channels that keep it
  there: an internal link, a closed group, signed builds on the owner's own distribution.

## Every channel that can carry the work out

Map every channel, and give each a verdict with its evidence (a configuration line, a captured
request): closed, controlled (with the rule it follows), or open by the owner's written decision.
Walk all of these:

- version-control remotes and hosting, their hooks, CI and its logs, backups and sync clients;
- agents and model providers, and the harness's context rules;
- editor, operating system and tool telemetry, extensions, update and licence checks, clipboard sync;
- package registries, indexes and mirrors, and the lockfiles;
- the product's own outbound calls: crash reports, analytics, update checks, fonts and scripts from
  other origins;
- trackers, chat, email and screen sharing;
- research: search engines, documentation sites, datasheets, forums, model hubs, the owner's notes;
- metadata: commit authorship and time zones, paths in build outputs, document properties, image
  metadata.

## Agents and models

- **Where the class requires it, run the work on local tools:** a local model runtime and a harness
  that talks only to a local endpoint, with the weights stored with their hashes and no remote
  fallback that can switch itself on.
- **Where a remote agent or model is allowed, give it the least:** only the classes the rules release
  to it; the smallest excerpt that does the job, never the whole repository; names, keys and customer
  data stripped before sending; a provider whose terms (the terms themselves, not the marketing page)
  exclude training on the data and limit its retention; and a log of what each remote call sent, so
  the owner can audit it.
- **A harness refuses a remote endpoint unless it is explicitly allowed,** and sends remote requests
  through the project's egress proxy when one is set.

## Working offline

- **Offline is proved by unplugging.** Block all outbound traffic at the firewall, or disconnect;
  then, from a clean checkout, run every procedure in the operating model: build, test, the agent's
  work on its local model, packaging, backup and restore. Anything that reaches for the network fails
  loudly and is fixed: vendor it, mirror it, or cache it with its hash. A project said to run offline
  that has not been run offline is not verified.
- **Version control** on the owner's own hardware or local network, or an encrypted remote where the
  host holds only ciphertext (client-side encryption for remotes and backups alike).
- **Dependencies:** a lockfile with hashes, a local mirror or vendored copy of every package, and
  installs that refuse the public index. Internal package names never reach a public registry (an
  extra index that falls back to the public one tells it the name, and lets a stranger publish under
  it).
- **Work records, CI and documentation locally:** the project's work records in a tool that runs
  offline (plain files in the repository if nothing else), checks run by a local runner, and
  documentation sets downloaded whole and read locally.
- **A step that names a hosted service is done with the local equivalent, never skipped.**
- **Services that need the internet by nature** (a vulnerability database, a store submission, a
  certification body): mirror what can be mirrored, and give each remaining use its own row in the
  channel map.

## Using the internet without revealing the work

- **One purpose, one sitting, one gate.** Decide before connecting what the session is for. Use a
  machine, profile or container kept for this alone, with no sign-in, no sync and no extensions,
  cleared at the end.
- **Fetch broadly, then search locally.** Download a whole documentation set, a vendor's whole
  datasheet library, a full package mirror or a complete collection of papers on a topic, rather than
  the one page the work needs. A broad fetch shows a general interest; a run of narrow ones traces the
  project.
- **Ask about the technique, never the project.** No code, names, customers, or combinations of parts
  and numbers that together identify the work go into a search box, a forum or a remote model.
- **Keep an automated agent off the open web:** its research goes through a proxy that allows only
  listed hosts and logs every request, or it writes a list of what it needs and a person fetches it in
  bulk.
- **Separate the network identity from the work where the threat model calls for it** (a connection
  not tied to the owner's organisation, a VPN, an anonymity network), used lawfully and within each
  service's terms.
- **Verify and keep what comes in:** check everything fetched by hash or signature, store it, and fetch
  it once.
- **Be exact about what remains.** These measures reduce what an observer can learn; they do not make
  the activity invisible. Record the residual exposure (that someone on this network used these hosts
  at these times) as a risk the owner accepted in writing, not as solved.

## Stripping what identifies the project

- Commit author, email and time zone set for the project.
- Codenames kept out of package names, hostnames and published artifacts.
- Build outputs free of absolute paths.
- Metadata stripped from documents and images before sharing.
- Logs and errors that leave the machine free of names and data.

## Proving it

- **Run a working session with outbound connections and DNS queries logged,** by the firewall, a local
  resolver or the proxy.
- **Every destination in the log appears in the channel map with its verdict;** anything else is a
  finding.
- **Repeat after every new tool, extension, dependency, model or agent,** and at each periodic review.

## When something has leaked

- **Contain it:** rotate the key, revoke the token, remove the integration; record what went where and
  when.
- **Add the channel to the map** so it cannot happen the same way twice.
- **Never report a leak as undone:** data that left is assumed kept.
