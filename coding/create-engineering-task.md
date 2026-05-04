# Create an engineering task (human + agent readable)

**Upstream:** [`coding/README.md`](README.md)

This is for **issues, tickets, or GitHub discussions** that drive code changes—not the personal P0–P4 system in [`../tasks/README.md`](../tasks/README.md). Team norms and “starting a new task” reminders also live in [`../device/work.md`](../device/work.md) under *Starting a new task (SDE2)*.

## Index

- [Purpose](#purpose)
- [Ticket skeleton](#ticket-skeleton)
- [Agent-friendly extras](#agent-friendly-extras)
- [Out of scope](#out-of-scope)

---

## Purpose

A good task **reduces rework**: the assignee (human or agent) knows **done**, **constraints**, and **where to look** without asking three rounds of questions.

---

## Ticket skeleton

Use this order in the body.

1. **Goal** — One sentence: user-visible outcome or technical outcome.
2. **Context** — Link to design, incident, prior PR, or line-range in code (permanent links preferred).
3. **Scope** — Bullets: **in scope** and **explicitly out of scope**.
4. **Acceptance criteria** — Checklist, testable when possible (“returns 400 when …”, “metric X visible in dashboard Y”).
5. **Risks / dependencies** — Flags, migrations, other teams, backward compatibility.
6. **Estimate or t-shirt size** — Only if the team uses it; optional spike note with time box.

Align with the **store** examples in [`../device/work.md`](../device/work.md): ticket state, Slack link if required, spike before large diff.

---

## Agent-friendly extras

These help **Cursor and other agents** stay on rails.

| Field | Example |
| --- | --- |
| **Repo + branch convention** | “Branch from `main`, prefix `fix/` or `feat/` per team.” |
| **Verify command** | “`make test`” or “`pnpm lint && pnpm test`” — copy from CI or README. |
| **Files likely touched** | “Start in `pkg/foo/bar.go`” — not mandatory but cuts search time. |
| **Non-goals** | “Do not refactor unrelated packages.” |
| **Screenshots / HAR** | For UI bugs, attach or link **sanitized** repro artifacts (see [`debug-prod-ui-flows.md`](debug-prod-ui-flows.md)). |

---

## Out of scope

If the task balloons, **split** it: new issue for follow-ups, link between them. One primary **Definition of done** per issue keeps reviews and agent runs focused.
