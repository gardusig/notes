# Review: calm read (modus operandi)

**Upstream:** [`coding/README.md`](README.md)

**Status — under research.** This page captures an **intentional** review style: not rushing to the next prompt, not “rubber-stamp the diff,” but a **quiet pass** over code and test evidence. Refine it as you learn what actually catches bugs for you.

## Index

- [Purpose](#purpose)
- [What this is not](#what-this-is-not)
- [Suggested ritual (draft)](#suggested-ritual-draft)
- [What to read, in order (draft)](#what-to-read-in-order-draft)
- [Links](#links)

---

## Purpose

After implementation—or before you ask for human review—you want a **different mode** than building: **slower**, **wider attention**, **no new features**. The hypothesis (still being validated) is that **stopping everything else** and **reading** code and test output **calmly** catches classes of mistakes that fast scanning and chat do not.

---

## What this is not

| Not this | Instead |
| --- | --- |
| **Another agent pass** that edits more code | Prefer **human-led** reading first; optional second model pass *after* you have read. |
| **Glancing at green CI** | Open **which** tests ran; skim failures even in unrelated jobs if they are new. |
| **Scrolling the diff once** | Read **callers**, **error paths**, and **config** as if you were on-call. |

---

## Suggested ritual (draft)

1. **Close or minimize** unrelated tabs and chats if you can; silence notifications for a bounded window (e.g. 20–40 minutes).
2. **Do not start** the next task or a new plan in the same block.
3. **Open** the branch diff (or PR) and the **test log** for the last verify run side by side.
4. **Read** without fixing at first: note questions on paper or in a scratch line in the ticket.
5. **Only then** fix or comment—or hand off a tight list of questions to a reviewer.

Adjust durations to your team; the point is **contiguous attention**, not a fixed clock.

---

## What to read, in order (draft)

| Layer | Ask |
| --- | --- |
| **Public API** | Did signatures, errors, and docs change coherently? |
| **Control flow** | Branches, retries, timeouts, nil/empty cases. |
| **Data** | Migrations, defaults, backwards compatibility. |
| **Tests** | Do new tests **prove** the bug or feature? Any skipped or overly mocked paths? |
| **Operational** | Logs, metrics, feature flags—if the ticket touched runtime behavior. |

If something still feels off after this pass, schedule a **second** calm block or a narrower read (single package), then a targeted run (see [`debug-prod-ui-flows.md`](debug-prod-ui-flows.md) when production UI is involved).

---

## Links

- SDE2 **review bar** reminders: [`../device/work.md`](../device/work.md) *Code review cheat sheet*.
- **Giving** reviews to others stays in team norms; this page is about **your** pre-flight read.
- Faster loop during implementation: [`work-task-with-agents.md`](work-task-with-agents.md); lifecycle: [`task-resolution-lifecycle.md`](task-resolution-lifecycle.md).
