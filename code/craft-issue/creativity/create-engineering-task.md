# 📋 Create an engineering task (human + agent readable)

**Upstream:** [`code/README.md`](../../README.md)

This is for **issues, tickets, or GitHub discussions** that drive code changes—not the personal P0–P4 system in [`../../plan/README.md`](../../plan/README.md). Team norms and “starting a new task” reminders also live in [`../../setup/work.md`](../../setup/work.md) under *Starting a new task (SDE2)*.

## 📑 Index

- [Purpose](#purpose)
- [Ticket skeleton](#ticket-skeleton)
- [Implementation-ready quality bar](#implementation-ready-quality-bar)
- [Agent-friendly extras](#agent-friendly-extras)
- [Out of scope](#out-of-scope)

---

## 🎯 Purpose

A good task **reduces rework**: the assignee (human or agent) knows **done**, **constraints**, and **where to look** without asking three rounds of questions.

---

## 📌 Ticket skeleton

Use this order in the body.

1. **Goal** — One sentence: user-visible outcome or technical outcome.
2. **Context** — Link to design, incident, prior PR, or line-range in code (permanent links preferred).
3. **Scope** — Bullets: **in scope** and **explicitly out of scope**.
4. **Acceptance criteria** — Checklist, testable when possible (“returns 400 when …”, “metric X visible in dashboard Y”).
5. **Risks / dependencies** — Flags, migrations, other teams, backward compatibility.
6. **Estimate or t-shirt size** — Only if the team uses it; optional spike note with time box.

Align with the **store** examples in [`../../setup/work.md`](../../setup/work.md): ticket state, Slack link if required, spike before large diff.

---

## ✨ Implementation-ready quality bar

Use this pass when the ticket is now the next priority and you want to remove ambiguity before execution.

Required sections (either explicit headings or clearly covered in prose):

1. **Goal/outcome**
2. **Current behavior** with examples
3. **Desired behavior** with examples
4. **Scope and change surface**
5. **Non-regression / compatibility expectations**
6. **Verification** (acceptance and regression tests)
7. **Worked examples / edge cases**
8. **Risks / open questions**

Done criteria:

- A future implementer can run verification without guessing.
- In scope vs out of scope is concrete enough to avoid drive-by refactors.
- At least one current example and one desired example are visible.

Upstream references:

- [issue-spec (cursor-skills)](https://github.com/gardusig/cursor-skills/blob/main/skills/read/gh/issue-spec/SKILL.md)
- [github-issue-profile (cursor-skills)](https://github.com/gardusig/cursor-skills/blob/main/skills/read/plan/core/github-issue-profile/SKILL.md)

---

## 📌 Agent-friendly extras

These help **Cursor and other agents** stay on rails.

| Field | Example |
| --- | --- |
| **Repo + branch convention** | “Branch from `main`, prefix `fix/` or `feat/` per team.” |
| **Verify command** | “`make test`” or “`pnpm lint && pnpm test`” — copy from CI or README. |
| **Files likely touched** | “Start in `pkg/foo/bar.go`” — not mandatory but cuts search time. |
| **Non-goals** | “Do not refactor unrelated packages.” |
| **Screenshots / HAR** | For UI bugs, attach or link **sanitized** repro artifacts (see [`../../observe/prod-ui-flows.md`](../../observe/prod-ui-flows.md)). |

---

## 📌 Out of scope

If the task balloons, **split** it: new issue for follow-ups, link between them. One primary **Definition of done** per issue keeps reviews and agent runs focused.

---

## 📌 See also

- **From idea to “good enough” then priority work** — full choreography in [`../../debug/README.md`](../../debug/README.md).
