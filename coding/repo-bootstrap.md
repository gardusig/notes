# Per-repo bootstrap (Cursor and hygiene)

**Upstream:** [`coding/README.md`](README.md)

Use this when you **clone a repo** or start owning a new service codebase. Goal: predictable agent behavior, stable terminal context, and optional team-facing rules without copying secrets into chat.

## Index

- [Purpose](#purpose)
- [Minimal repo hygiene](#minimal-repo-hygiene)
- [`.cursor/` checklist](#cursor-checklist)
- [Pin the terminal tab](#pin-the-terminal-tab)
- [Optional: AGENTS.md and rules](#optional-agentsmd-and-rules)

---

## Purpose

Standardize what **each** coding repo should have so **you and agents** share the same assumptions: where rules live, how hooks might run, and where the shell session is anchored.

---

## Minimal repo hygiene

| Check | Why |
| --- | --- |
| **Clone path** is stable and policy-safe | Employer vs personal separation: [`../device/work.md`](../device/work.md) (work laptop section). |
| **Default branch** and **remote** match how you ship | Avoid accidental pushes to the wrong fork. |
| **Install + verify** commands exist in README or CI | Agents and future-you run the same umbrella (`make test`, `pnpm test`, etc.). |
| **`.gitignore`** covers local tooling noise | Reduces accidental commits of env files and editor junk. |

---

## `.cursor/` checklist

Treat this as a **copy-paste scaffold** when a repo has no Cursor layout yet. Adjust names to match the project; keep files **small and specific** rather than one giant rule file. For a **full map** of `.cursor/templates/` (minimal vs standard vs docs-heavy copy sets), see **[`templates/.cursor/README.md`](templates/.cursor/README.md)**.

| Path / concern | Suggested content |
| --- | --- |
| **`.cursor/rules/`** (or project rules in app settings) | Stack-specific guardrails: test command, formatter, “do not edit generated,” security notes. |
| **`.cursor/hooks/`** (if you use hooks) | Repo-local automation only; document what each hook does in a one-line README in that folder or in the main repo README. |
| **`.cursor/templates/`** (optional) | Markdown pasteables: PRs, issues, git narratives, diagrams, README/wiki stubs—copy from [`templates/`](templates/README.md); layout reference [`templates/.cursor/README.md`](templates/.cursor/README.md). |
| **Diagrams / tables / index** | If the repo has a `docs/` wiki, align with its index pattern; for graph-heavy design, keep **mermaid** in versioned docs, not only in chat. |
| **Markdown style** | Match existing docs; prefer links to canonical runbooks over duplicating employer URLs here. |

Do **not** commit API keys, session cookies, or production URLs that embed credentials. Use placeholders and keep real links in **private** notes (e.g. [`../device/work.md`](../device/work.md)) where appropriate.

---

## Pin the terminal tab

**Why:** Agent sessions and multi-step tasks often assume a **single working directory** and **one shell history**. Unpinned tabs make it easy to run `git` or tests in the wrong clone.

**What to do:**

1. Open the integrated terminal in the **repo root** of the task.
2. **Pin** that terminal tab in the editor so it does not get replaced by one-off commands.
3. For long-running servers or watchers, use a **second** tab (also pinned) so logs do not scroll away your prompt.

---

## Optional: AGENTS.md and rules

| Artifact | When to use |
| --- | --- |
| **`AGENTS.md` at repo root** | Short “how to work this repo” for humans and models: build, test, branch naming, code owners pointer. |
| **`.cursor/rules` scoped globs** | When certain directories need stricter patterns (e.g. `src/api/**`). |

Keep **`coding/`** in the **notes** repo as the **meta** guide; per-repo files stay **in that repo**.
