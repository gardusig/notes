# Phase 3 — Plan mode: load context and sharpen

**Upstream:** [`README.md`](README.md)

Use **Plan** mode in Cursor (or equivalent) as the **main** instrument before large edits.

| Habit | Why |
| --- | --- |
| **Append as much context as possible** | Paste or `@`-reference: ticket body, key files, failing test output, design snippets, related PRs, **constraints** (“must not break X”). |
| **Iterate on the plan itself** | Ask for gaps: edge cases, migrations, rollback, tests to add. Treat the plan like a **mini-design** you would show a colleague. |
| **Sharpen until it feels boring** | If the plan names **files**, **order of operations**, and **verify commands**, execution is mostly follow-through. |
| **One thread per task** | Avoid splitting plan across many chats; you lose shared context. |

If the plan is **strong**, you should need **few** extra instructions during implementation: the agent (or you) follows the plan and checks acceptance. If you keep re-explaining, **stop** and improve the plan or the ticket, not the next prompt — see also [`signals-and-stops.md`](signals-and-stops.md).

Bias and UI context: [`../craft-issue/creativity/plan-first-and-ui-context.md`](../craft-issue/creativity/plan-first-and-ui-context.md).

**Previous:** [`next-priority-and-context.md`](next-priority-and-context.md) · **Next:** [`execute-from-plan.md`](execute-from-plan.md)
