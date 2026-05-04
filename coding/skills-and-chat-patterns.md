# Skills and chat patterns (personal tools)

**Upstream:** [`coding/README.md`](README.md)

How to use **user-scoped** Cursor **skills** (and similar `@` invocations) without treating chat as the source of truth for repo policy.

## Index

- [Purpose](#purpose)
- [Where skills live](#where-skills-live)
- [How to invoke](#how-to-invoke)
- [Suggested usage map](#suggested-usage-map)
- [Browser recording and capture](#browser-recording-and-capture)
- [What not to mirror in this repo](#what-not-to-mirror-in-this-repo)

---

## Purpose

**Skills** package repeatable workflows (review, push, PR text, research context). This notes repo documents **when** to reach for them, not the full text of each skill—which **changes** on your machine.

---

## Where skills live

Personal skills are typically under **your user Cursor config**, e.g. `~/.cursor/skills/` (exact layout follows Cursor’s current docs). **Repositories** may add `.cursor/rules` or project rules; see [`repo-bootstrap.md`](repo-bootstrap.md).

---

## How to invoke

In chat, reference a skill with the **`@`** mechanism your Cursor build uses (e.g. `@git-review`, `@git-push`, `@gh-pr`). The skill file defines **order of operations** (install, lint, test, doc sync, etc.). **You** remain responsible for **confirming** destructive or publish steps when the skill says to.

---

## Suggested usage map

| Intent | Pattern |
| --- | --- |
| **Sanity check** the tree before commit | Review-oriented skill if you use one; otherwise run the repo’s documented verify command in the **pinned** terminal. |
| **Push** after green | Push skill if it encodes your “review then push” habit; never skip **reading the diff**. |
| **Open or update a PR** | PR skill after branch is pushed; keep issue links in the body. |
| **Research / ingest URLs** | Context skills that **only** write agreed paths (see each skill’s own rules). |

Names here are **examples**; your installed pack may differ. Prefer **one skill per phase** over stacking five in one message unless the skills are designed to chain.

---

## Browser recording and capture

When the product offers **browser recording** or **screenshot-to-context**:

- Record the **shortest** repro: open page, one action, see failure.
- **Redact** PII and tokens before attaching to tickets or pasting into shared chat.
- Pair with [`debug-prod-ui-flows.md`](debug-prod-ui-flows.md) so you also capture **Network** facts (status, request id).

---

## What not to mirror in this repo

- **Full copies** of every `SKILL.md` (they drift).
- **Secrets**, internal URLs, or customer data from recordings.

Link to this **`coding/`** hub from tickets when you want collaborators (or future-you) to follow the same **patterns**, not the same **files** as the skill pack.
