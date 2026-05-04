# Task resolution lifecycle (idea → plan → work)

**Upstream:** [`coding/README.md`](README.md)

Common **end-to-end** flow: from a vague idea to a ticket, then—when the item is **actually next**—heavy **Plan** mode in Cursor with **dense context** and a **sharpened** plan so execution needs **few** follow-up prompts. Ticket shape overlaps [`create-engineering-task.md`](create-engineering-task.md); execution habits overlap [`work-task-with-agents.md`](work-task-with-agents.md).

## Index

- [Purpose](#purpose)
- [Phase 1 — Idea and a good-enough task](#phase-1--idea-and-a-good-enough-task)
- [Phase 2 — It is the next priority](#phase-2--it-is-the-next-priority)
- [Phase 3 — Plan mode: load context and sharpen](#phase-3--plan-mode-load-context-and-sharpen)
- [Phase 4 — Execute from the plan](#phase-4--execute-from-the-plan)
- [When to split or spike](#when-to-split-or-spike)
- [See also](#see-also)

---

## Purpose

Most friction comes from **under-specified intent** or **under-loaded context**. This page is the **default choreography**: capture intent early, invest in **plan quality** when the task surfaces, then let implementation be mostly **mechanical**.

---

## Phase 1 — Idea and a good-enough task

You do **not** need a perfect spec at first—you need something **durable** you can reopen later.

| Step | What to do |
| --- | --- |
| **Capture** | One paragraph: problem, who cares, rough outcome. |
| **Good-enough description** | Turn it into a ticket or issue using [`create-engineering-task.md`](create-engineering-task.md): goal, scope in/out, acceptance criteria—even if some lines say **TBD** with a question. |
| **Park** | Link related threads, prior art, or a spike branch name. Leave enough breadcrumbs that **future-you** (or an agent) is not guessing from memory. |

“Good enough” means: **someone else could tell if it is done** without asking you three times. If not, add one more pass only on **acceptance** and **out of scope**.

---

## Phase 2 — It is the next priority

When the item becomes **the** thing you are doing:

1. **Open the repo** and **pin** the terminal (see [`repo-bootstrap.md`](repo-bootstrap.md)).
2. **Re-read the ticket**; update stale links or acceptance if reality shifted.
3. **Switch mental mode**: you are not “coding yet”—you are **loading context and planning** unless the change is trivial.

---

## Phase 3 — Plan mode: load context and sharpen

Use **Plan** mode in Cursor (or equivalent) as the **main** instrument before large edits.

| Habit | Why |
| --- | --- |
| **Append as much context as possible** | Paste or `@`-reference: ticket body, key files, failing test output, design snippets, related PRs, **constraints** (“must not break X”). |
| **Iterate on the plan itself** | Ask for gaps: edge cases, migrations, rollback, tests to add. Treat the plan like a **mini-design** you would show a colleague. |
| **Sharpen until it feels boring** | If the plan names **files**, **order of operations**, and **verify commands**, execution is mostly follow-through. |
| **One thread per task** | Avoid splitting plan across many chats; you lose shared context. |

If the plan is **strong**, you should need **few** extra instructions during implementation: the agent (or you) follows the plan and checks acceptance. If you keep re-explaining, **stop** and improve the plan or the ticket, not the next prompt.

---

## Phase 4 — Execute from the plan

Move to **Agent** mode (or hands-on editing) when the plan is stable. Follow [`work-task-with-agents.md`](work-task-with-agents.md): small slices, run verify, read diffs. After a substantive change set, use a **calm read** pass—see [`review-calm-read.md`](review-calm-read.md) (modus operandi still under research).

---

## When to split or spike

| Signal | Action |
| --- | --- |
| Plan keeps growing new major branches | **Split** tickets; finish one vertical slice first. |
| Unknown unknowns dominate | **Time-boxed spike**; link findings back to the ticket, then return to Plan mode with facts. |

Team norms for spikes and design still align with [`../device/work.md`](../device/work.md) *Starting a new task (SDE2)*.

---

## See also

- [`review-calm-read.md`](review-calm-read.md) — post-plan **calm** read of code and tests (under research).
