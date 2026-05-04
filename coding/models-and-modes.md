# Models and modes (policy)

**Upstream:** [`coding/README.md`](README.md)

Stable **principles** for model choice in Cursor (or similar). Product names and tiers change; the policy should not.

## Index

- [Purpose](#purpose)
- [Default model](#default-model)
- [When to escalate](#when-to-escalate)
- [Avoid “Auto” when it hurts](#avoid-auto-when-it-hurts)
- [Cost and latency](#cost-and-latency)

---

## Purpose

Pick models **deliberately** so behavior, cost, and quality are predictable. **Planning** and **final review** often deserve a stronger model; **bulk edits and retries** may not.

---

## Default model

| Habit | Rationale |
| --- | --- |
| **One “standard” model** for day-to-day implementation | You learn its quirks; reviews become consistent. |
| **Match model to risk** | Payments, auth, concurrency: use the strongest model you accept for that session, or more human review. |

Set the default in the product once and **reset** it after experiments so you do not leak a one-off choice into the next task.

---

## When to escalate

| Situation | Consider |
| --- | --- |
| **Architecture** spanning many services or unclear tradeoffs | Stronger model in **Plan** mode, or human design first. |
| **Subtle bugs** (race, memory, security) | Stronger model **or** pair with human; add tests that fail before the fix. |
| **Final pass** before merge | Quick read by a stronger model **or** human for high-risk diffs. |
| **Regenerating** similar code after a mistake | Cheaper or faster model may suffice if the spec is now clear. |

---

## Avoid “Auto” when it hurts

**Auto** routing can switch underlying models between turns. That may:

- **Break** continuity (“why did style change mid-refactor?”).
- **Obscure cost** (fast vs slow pricing mixed in one thread).
- **Hide** which model actually produced a bad suggestion.

If you notice **inconsistent** quality or **surprising** bills in Auto, **pin** explicit models per thread or task. If Auto improves later, re-evaluate with a short experiment rather than defaulting forever.

---

## Cost and latency

**Faster** models can cost **more per useful answer** if they require extra regeneration. Prefer:

- **Clear prompts** and **small** scopes (see [`work-task-with-agents.md`](work-task-with-agents.md)).
- **Parallel human work** while a slower model runs (same doc: parallelism section).

Do not treat model choice as a substitute for **tests** and **small diffs**.
