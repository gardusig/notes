# Work setup (SDE2): onboard → daily usage

This guide sits **on top of** a **dev-oriented** OS setup. **Every local install this workflow assumes** is mapped in **[parity.md](./parity.md)** (by domain: [Basic and desktop](./parity.md#basic-and-desktop), [Code, repos, and shipping](./parity.md#code-repos-and-shipping)). On **Mac**, follow **[macOS.md](./macOS.md)** — **Setup & installation** through **Privacy & permissions** (see that file’s **Index**)—same concerns as **parity**, with Mac-specific commands. Device note layout: **[../README.md](../README.md)**. On **Windows**, use **parity** directly. The **[windows.md](./windows.md)** file here is a **gaming** PC guide, not dev. It is tuned for **SDE2-level** work: you **own** medium-sized changes end to end, **review** others’ code with consistent quality, and **operate** services you touch (deploy, debug, on-call where applicable)—not just “stay organized.”

**What this guide optimizes for**

- **Onboard:** faster time-to-first-useful-PR by front-loading access, norms, and runbooks in one place *you* control.
- **Daily:** less context switching—bookmarks and a personal doc back **authoring**, **review**, **shipping**, and **incident/debug** loops.

**What “done” looks like**

- Work browser profile with folders that match how you **ship** (code, reviews, tools, wiki), not a flat list of tabs.
- A **personal work doc** you can open in one gesture: scratchpad on top, runbooks and **team norms** below—so SDE2 rituals (design for non-trivial work, review bar, escalation) do not live only in your head.

---

# Index

- [Work setup (SDE2): onboard → daily usage](#work-setup-sde2-onboard--daily-usage)
- [Index](#index)
- [1. Baseline: terminal, editor, and review loop](#1-baseline-terminal-editor-and-review-loop)
- [2. Browser: work-only profile](#2-browser-work-only-profile)
- [3. Bookmarks: folder layout](#3-bookmarks-folder-layout)
  - [Why separate folders](#why-separate-folders)
  - [Example tree (bookmark bar)](#example-tree-bookmark-bar)
  - [Folder reference](#folder-reference)
- [4. Personal work document](#4-personal-work-document)
  - [Quick notes](#quick-notes)
  - [Important notes](#important-notes)
  - [Team norms \& SDE2 bar](#team-norms--sde2-bar)
  - [Acronyms](#acronyms)
  - [Laptop apps](#laptop-apps)
  - [Current team architecture (minimap)](#current-team-architecture-minimap)
  - [Cross-team dependencies](#cross-team-dependencies)
  - [Code runbook](#code-runbook)
  - [Deploy runbook](#deploy-runbook)
  - [Debug runbook](#debug-runbook)
  - [Starting a new task (SDE2)](#starting-a-new-task-sde2)
  - [Code review cheat sheet](#code-review-cheat-sheet)
  - [On-call](#on-call)
  - [Verify deployed results](#verify-deployed-results)
  - [Test locally](#test-locally)
  - [Personal task board (optional)](#personal-task-board-optional)
  - [Activity](#activity)
- [5. Onboard checklist (SDE2-first weeks)](#5-onboard-checklist-sde2-first-weeks)
- [6. Daily rhythm](#6-daily-rhythm)

---

# 1. Baseline: terminal, editor, and review loop

**Install reference (all rows):** **[parity.md](./parity.md)** — [Code, repos, and shipping](./parity.md#code-repos-and-shipping) for the table below; **Mac**-specific steps also in **[macOS.md](./macOS.md)** §2.3–§2.8.

| Piece | Purpose | → **[parity](./parity.md)** |
| ----- | ------- | ---------------------------- |
| **Cloud / k8s CLIs** (if applicable) | Whatever your team uses to **inspect** prod-like envs (read-only is enough for many SDE2 days). | [Code, repos, and shipping](./parity.md#code-repos-and-shipping) |
| **Docker** (if the team uses it) | Local parity for integration tests and services. | [Code, repos, and shipping](./parity.md#code-repos-and-shipping) |
| **Editor** (e.g. Cursor) | Implementation + **in-editor diff**; extensions for your stack and formatter/linter. | [Code, repos, and shipping](./parity.md#code-repos-and-shipping) |
| **Git** + **SSH** (or HTTPS + credential helper) | Clone, branch, push; same identity your org expects on commits. | [Code, repos, and shipping](./parity.md#code-repos-and-shipping) |
| **Host CLI** (`gh`, `glab`, …) | List PRs, request review, merge policy checks from the terminal when faster than the web UI. | [Code, repos, and shipping](./parity.md#code-repos-and-shipping) (`gh` / `glab` rows); **Mac** detail **[macOS.md](./macOS.md)** §2.8 |

**Also part of your machine (outside this table):** work **browser**, **meetings**, **window manager**, **keep-awake**, **package manager** — **[parity.md](./parity.md)** [Basic and desktop](./parity.md#basic-and-desktop). **Mac** walkthrough: **[macOS.md](./macOS.md)** §3–§4.

Track **repos you must have** (service, infra, shared libraries) in your personal doc and tick them off as access propagates—SDE2 work often spans **more than one** repo.

---

# 2. Browser: work-only profile

Install the **work browser** (and keep it updated) per **[parity.md](./parity.md)** [Basic and desktop](./parity.md#basic-and-desktop). Use a **dedicated work profile** so sessions, extensions, and bookmarks stay professional and searchable.

| Area | Verify |
| ---- | ------ |
| **Code hosts** | Org/team membership, default clone method, saved views (**your** open PRs, **team** review queue). |
| **Design / specs** | Where RFCs or tech specs live (wiki, Google Docs, Notion)—bookmark the **template** and your team space. |
| **HR** | Payroll, benefits, PTO, directory—under **hr**. |
| **Internal tools** | Dashboards, flags, deploy—under **tools**. |
| **Wiki** | Onboarding, ADRs, runbook index—under **wiki**. |

**Pin daily surfaces:** **calendar**, **tasks**, **mail** (if web), **chat**. SDE2 days are split between **writing code**, **reviewing**, and **communicating** scope/risk—those four reduce friction.

---

# 3. Bookmarks: folder layout

## Why separate folders

Folders mirror **mental modes**: implementing (**code**), judging others’ diffs (**reviews**), operating (**tools**, **debug**), learning (**wiki**). At SDE2 you switch modes often; a flat bar hides cost until you are late for standup.

## Example tree (bookmark bar)

```text
Bookmarks Bar
├── code
│   ├── Git org / team
│   ├── Primary service repo(s)
│   ├── Infra / shared lib repos
│   └── Package / artifact registry
├── reviews
│   ├── “My open PRs” saved search
│   ├── Team / guild review queue (if used)
│   └── Org-wide diff / code search (e.g. sourcegraph) if you have it
├── debug
│   ├── Error tracker project
│   ├── Logs / traces (saved views)
│   └── “How we debug X” wiki
├── tools
│   ├── Staging + prod dashboards (read-only)
│   ├── Feature flags
│   └── Deploy / pipeline UI
├── wiki
│   ├── Team space root
│   ├── RFC / design doc template
│   ├── Onboarding checklist
│   └── ADR / architecture index
├── hr
├── calendar
├── tasks
├── mail
├── chat
└── heavily used        ← links you open constantly that do not fit above
```

**Flat alternative:** merge **reviews** into **code** until the bar feels crowded.

## Folder reference

| Folder | Put here | SDE2-oriented example |
| ------ | -------- | ---------------------- |
| **calendar** | Meetings + **on-call** calendar if separate | |
| **chat** | Slack / Teams | #incidents, #your-team |
| **code** | Repos, boards, registries | Monorepo, `lib-auth`, artifact UI |
| **debug** | Incidents, logs, traces | Sentry, Datadog view, runbook |
| **heavily used** | Daily oddballs | Doc you link in every mid-size PR |
| **hr** | People systems | HRIS, org chart |
| **mail** | Webmail | |
| **reviews** | PR queues, “needs my review,” global search | Saved GitHub filter `review-requested:@me` |
| **tasks** | Issue tracker | Your filtered board / sprint |
| **tools** | Ops consoles | Flags, metrics, deploy |
| **wiki** | Long-lived docs | RFC space, ADRs, team charter |

---

# 4. Personal work document

One **primary** place for *your* operational memory: meeting scraps, **team-specific** SDE2 expectations, and links that would otherwise die in Slack.

**Tooling:** Notion, Obsidian, Apple Notes, Google Doc, or git-backed Markdown—choose for **speed to open**, not features.

**How to use it**

1. **Capture** in *Quick notes* during calls; polish later.
2. **Triage weekly:** promote into runbooks, *Team norms*, or delete.
3. **Link** to canonical wiki; keep one-line context here.

**Outline you can copy**

```text
Personal work doc
├── Quick notes
├── Important notes
│   ├── Team norms & SDE2 bar
│   ├── Acronyms
│   ├── Laptop apps
│   ├── Team architecture (minimap)
│   ├── Cross-team dependencies
│   ├── Code / deploy / debug runbooks
│   ├── Starting a new task (SDE2)
│   ├── Code review cheat sheet
│   ├── On-call
│   ├── Verify deployments / test locally
│   └── Personal task board (optional)
└── Activity
```

### Quick notes

**Purpose.** Default landing; raw capture during meetings and threads.

**Store (examples).**

- “Retry policy: align with Platform by Friday; link to thread.”
- “Incident 4/2: cache TTL—postmortem TODO.”

**Tip.** Promote or delete anything older than ~2 weeks.

### Important notes

**Purpose.** Durable **decisions** and ownership, not procedures.

**Store (examples).**

- “Trunk + flags for release X; EM signed off 3/10.”
- “DBA rotation—#infra pinned message.”

### Team norms & SDE2 bar

**Purpose.** What *your* team expects from someone at **mid-level**: review turnaround, when a **design** is required, who approves risky changes, how async updates work.

**Store (examples).**

- “PRs under ~200 LOC when practical; split larger with plan in description.”
- “Auth / PII / migrations → security or infra stamp per checklist.”
- “Standup: blockers + ETA; deep work: mute Slack 9–12.”
- “Calibration / perf: self-review opens week of …”

**Tip.** If it is written in the team wiki, **link** it and keep only deltas (“we actually do X in practice”).

### Acronyms

**Purpose.** Org vocabulary.

**Store (examples).** “**SLO** — …; doc: …”

### Laptop apps

**Purpose.** Reproducible setup: VPN, editors, meeting stack, phone policy. Align names with **[parity.md](./parity.md)** (and **[macOS.md](./macOS.md)** on Mac) so “what’s installed” matches how you actually provisioned the machine.

### Current team architecture (minimap)

**Purpose.** **Your** mental model: services, stores, queues, **which repo** maps to what, rough ownership.

**Store (examples).** Diagram link + “Payments → `payments-api`, on-call §…”

**Tip.** Update after migrations; SDE2s get asked “how does this fit together?”

### Cross-team dependencies

**Purpose.** **Who to ping** for APIs, shared platforms, and approvals outside your squad.

**Store (examples).**

- “Identity API — #identity-eng; SLA for breaking changes: …”
- “Data platform — pipeline X owned by …”

### Code runbook

**Purpose.** Zero → **running tests** on your machine. **OS-level prereqs** (Git, Docker, editor, language runtimes): **[parity.md](./parity.md)** [Code, repos, and shipping](./parity.md#code-repos-and-shipping).

### Deploy runbook

**Purpose.** How **your** team ships and rolls back; release roles if any.

### Debug runbook

**Purpose.** Logs, traces, top failure patterns for services you **own or on-call for**.

### Starting a new task (SDE2)

**Purpose.** Checklist so medium work does not skip **clarity** or **risk** steps.

**Store (examples).**

- Ticket in progress; link in Slack if team expects it.
- **Scope:** “Happy path + edge cases; out of scope: …”
- **Non-trivial?** Spike time-boxed; **short design** or RFC link before large diff.
- **Dependencies:** other teams, flags, migrations—note in ticket.
- **Estimate / risk** to EM or PM if deadlines exist.

### Code review cheat sheet

**Purpose.** **Your** consistent bar when **giving** reviews (and reminders when **receiving**).

**Store (examples).**

- “Check: correctness, tests, rollback, observability, security footguns, naming.”
- “Nit vs must-fix—use team convention.”
- Link to org **style guide** or **dangerous patterns** doc.

### On-call

**Purpose.** Paging paths, escalation, dashboard bundle—**read-only** links for tired-you.

### Verify deployed results

**Purpose.** Smoke checks and flags after **your** ship.

### Test locally

**Purpose.** Minimum bar before **you** request review (`make test`, targeted `pytest`, etc.).

### Personal task board (optional)

**Purpose.** Growth, tech debt you personally want to drive, **prep for perf** conversations.

### Activity

**Purpose.** One-line **dated** log: ships, reviews you unblocked, incidents, designs you wrote—feeds **perf** and self-review.

**Tip.** SDE2 impact often includes **review quality** and **reliability**; log those, not only merges.

---

# 5. Onboard checklist (SDE2-first weeks)

**Access & repos**

- [ ] Code host org(s), default SSH/HTTPS, **saved PR views** (yours + review queue).
- [ ] Repos for **services you will touch**, shared libs, **infra** if your team commits there.
- [ ] Wiki: onboarding page, **team charter** or working agreements, **RFC/design** space.

**People & process**

- [ ] Know **EM + PM** (or equivalent) and how **priority** is communicated.
- [ ] Calendar: standups, **planning**, **on-call shadow** or rotation intro if applicable.
- [ ] **Buddy** or primary reviewer for first PRs (if your org assigns one).

**Machine & comms**

- [ ] **Local installs** match **[parity.md](./parity.md)** ([Basic and desktop](./parity.md#basic-and-desktop), [Code, repos, and shipping](./parity.md#code-repos-and-shipping)); on **Mac**, complete **[macOS.md](./macOS.md)** §1–§6 (and §5 workflow) per the guide’s **Index**.
- [ ] Meeting apps + OS **permissions** (**[macOS.md](./macOS.md)** §6 on Mac; meeting + privacy rows under **[parity — Basic and desktop](./parity.md#basic-and-desktop)** on Windows).
- [ ] One **shortcut** to *Quick notes* in your personal doc.
- [ ] Mail rules / signatures; **personal phone** policy documented under *Laptop apps*.

**First useful outcomes**

- [ ] Land a **small** fix or doc PR in week one if possible—validates the whole loop.
- [ ] Fill **minimap** and **cross-team** stubs; replace “TBD” as you learn.

**After ~2 weeks:** prune bookmarks; promote quick notes into runbooks or *Team norms*.

---

# 6. Daily rhythm

Use this as a **lightweight** default; adapt to your team’s timezone and async rules.

| When | SDE2-oriented focus |
| ---- | ------------------- |
| **Deep work** | Implementation or **review** blocks; batch Slack unless you are on-call. |
| **End** | Sweep *Quick notes* → 2-minute triage; log *Activity* if you shipped or reviewed something material. |
| **Reviews** | Clear **queue** (bookmark); aim for predictable turnaround your team agreed on. |
| **Shipping** | Follow *Deploy* / *Verify* sections; thread or channel update if stakeholders wait on you. |
| **Start** | Calendar + task board: **one** primary deliverable for the day; note conflicts early in chat. |

**Does this guide make sense for SDE2?** Yes, if you treat the **personal doc** as the place **team-specific SDE2 expectations** live (norms, cross-team map, review bar) and **bookmarks** reflect **code + reviews + ops**, not only “productivity links.” The weak spot is always **stale** runbooks—schedule a **monthly** 10-minute pass to delete lies and fix links.
