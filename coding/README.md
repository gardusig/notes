# AI-assisted coding

Personal **strategies for shipping code with Cursor**, agents, and **user-scoped** skills and rules—not hardware setup. For **machine and editor install**, see **[`../device/macOS.md`](../device/macOS.md)** (and parity). For **employer SDE2** norms, bookmarks, and team runbook *stubs*, see **[`../device/work.md`](../device/work.md)**. For **personal life tasks** (P0–P4, governance), see **[`../tasks/README.md`](../tasks/README.md)**.

**Upstream:** [Notes root](../README.md)

## Purpose

- Keep **one topic per file** so you can link a ticket or chat to a single runbook.
- Separate **how to frame and execute engineering work with AI** from device shopping notes and from the personal task mirror.

## Summary

| You need… | Start here |
| --- | --- |
| What to set up **per repo** (`.cursor/`, terminal pin, rules) | [`repo-bootstrap.md`](repo-bootstrap.md) |
| How to **write** an issue or ticket agents can run | [`create-engineering-task.md`](create-engineering-task.md) |
| How to **execute** a task (modes, terminal vs agent, verify) | [`work-task-with-agents.md`](work-task-with-agents.md) |
| **Post-deploy / UI** debugging (DevTools, cloud read-only, dashboards) | [`debug-prod-ui-flows.md`](debug-prod-ui-flows.md) |
| **Model** choice and when to escalate | [`models-and-modes.md`](models-and-modes.md) |
| **`@` skills**, browser capture, chat patterns | [`skills-and-chat-patterns.md`](skills-and-chat-patterns.md) |

## Index

- [Purpose](#purpose)
- [Summary](#summary)
- [Index](#index)
- [How this folder relates to `device/work`](#how-this-folder-relates-to-devicework)

---

## How this folder relates to `device/work`

[`device/work.md`](../device/work.md) holds **your** SDE2-oriented **personal work document** outline: deploy runbook, **debug** stub, **on-call** stub, verify deployed results, test locally. Put **team-specific URLs, service names, and escalation paths** there.

This **`coding/`** tree adds **Cursor- and agent-specific** playbooks (skills, models, DevTools flow) that apply across repos. When a procedure needs both, link from the ticket: e.g. “Debug: follow `coding/debug-prod-ui-flows.md`; paste dashboard links from `device/work.md`.”
