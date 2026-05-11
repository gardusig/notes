# Debug: task readiness (idea → plan → work)

**Upstream:** [`../README.md`](../README.md)

**Not personal life planning:** P0–P4 tasks and governance live under **[`../../plan/README.md`](../../plan/README.md)**. This folder is **engineering** delivery choreography only.

**Scope**

**Task resolution** — delivery choreography from idea through heavy Plan mode to execution (split across small pages below). This is **not** only “bug hunting”; it is **unblocking** under-specified work.

For **production** tracing (DevTools, dashboards, post-deploy UI), use **[`../observe/README.md`](../observe/README.md)**.

Team-specific dashboard URLs, service names, and escalation live in [`../../setup/work.md`](../../setup/work.md).

## Task resolution (idea → plan → work)

| Page | Role |
| --- | --- |
| [`idea-and-good-enough-ticket.md`](idea-and-good-enough-ticket.md) | Phase 1 — capture, good-enough ticket, park |
| [`next-priority-and-context.md`](next-priority-and-context.md) | Phase 2 — repo open, re-read ticket, planning mode |
| [`plan-mode-sharpen.md`](plan-mode-sharpen.md) | Phase 3 — dense context, iterate plan, one thread |
| [`execute-from-plan.md`](execute-from-plan.md) | Phase 4 — Agent / hands-on from a stable plan |
| [`split-spike-and-escalate.md`](split-spike-and-escalate.md) | When to split tickets or time-box a spike |
| [`signals-and-stops.md`](signals-and-stops.md) | When to stop executing and return to Plan or ticket |

**Short overview:** Most friction comes from **under-specified intent** or **under-loaded context**. Capture intent early, invest in **plan quality** when the task surfaces, then let implementation be mostly **mechanical**.

## See also

- [`task-resolution-lifecycle.md`](task-resolution-lifecycle.md) — one-line index of the phase pages above
- [`../craft-issue/creativity/create-engineering-task.md`](../craft-issue/creativity/create-engineering-task.md) — ticket shape
- [`../design/README.md`](../design/README.md) — solution shape (contracts, architecture scaffolds)
- [`../craft-pr/work-task-with-agents.md`](../craft-pr/work-task-with-agents.md) — execution habits
- [`../quality/review-calm-read.md`](../quality/review-calm-read.md) — calm read before PR
