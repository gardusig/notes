# Plan first, pad the chat (default bias)

**Upstream:** [`coding/README.md`](README.md)

Short **habit note**: when work is non-trivial, **default to Plan** in Cursor before leaning on Agent. Agent mode is strong and fast, but it is also **quite automated**—it will happily execute on partial intent. Plan mode is mostly there to **summarize what matters** and **craft a plan** you can correct before anyone touches the tree.

## Index

- [Purpose](#purpose)
- [Why Plan before Agent](#why-plan-before-agent)
- [Use the Cursor UI as context, not a skill](#use-the-cursor-ui-as-context-not-a-skill)
- [See also](#see-also)

---

## Purpose

Make **deliberate** the step where the model aligns with you: goals, constraints, files, and order of work. That alignment belongs in the **conversation surface** (Plan + pasted or `@`-referenced material), not only in your head.

---

## Why Plan before Agent

| Default | Rationale |
| --- | --- |
| **Start in Plan** for anything that is not a one-line fix | You get a structured summary and a plan you can edit; fewer surprise diffs. |
| **Treat Agent as execution** once the plan is stable | Agent excels at following through, tools, and iteration—but it will optimize for *doing* unless you have already pinned *what* and *why*. |
| **Expect the plan to be the artifact** | Good output from Plan: crisp scope, assumptions, file touch list, verify steps. If that is missing, stay in Plan and add context rather than switching modes early. |

This does **not** replace the full lifecycle in [`task-resolution-lifecycle.md`](task-resolution-lifecycle.md); it is the **bias**: when in doubt, **Plan + context first**, then Agent or hands-on work.

---

## Use the Cursor UI as context, not a skill

**Appending context in the Cursor UI** (ticket text, logs, screenshots, `@` files and rules) is almost always worth the minute—it steers both Plan and later Agent turns. That is a **built-in product workflow**, not something you need a repo skill or rule pack to “invent.”

Skills and rules still help for **repeatable** repo conventions; they do not replace **this task’s** specifics in the chat.

---

## See also

- [`task-resolution-lifecycle.md`](task-resolution-lifecycle.md) — idea → ticket → heavy Plan with dense context → execute.
- [`models-and-modes.md`](models-and-modes.md) — when to escalate model choice; Plan for architecture and tradeoffs.
- [`work-task-with-agents.md`](work-task-with-agents.md) — execution, verify, chunking after the plan exists.
