# Work a task with agents

**Upstream:** [`coding/README.md`](README.md)

How to **execute** work after [`create-engineering-task.md`](create-engineering-task.md) is written. Complements [`../device/work.md`](../device/work.md) (review, deploy, verify) with **Cursor-specific** habits.

## Index

- [Purpose](#purpose)
- [Plan vs Agent mode](#plan-vs-agent-mode)
- [Chunking and verification](#chunking-and-verification)
- [Agent vs terminal](#agent-vs-terminal)
- [Rewrite a few files, then re-read](#rewrite-a-few-files-then-re-read)
- [Parallelism while models run](#parallelism-while-models-run)

---

## Purpose

Agents are strong at **search, edits, and boilerplate**; they are weak at **tacit policy** and **production truth**. Structure work so **you** own decisions and **the agent** owns mechanical steps—with frequent verification.

---

## Plan vs Agent mode

| Mode | Use when |
| --- | --- |
| **Plan** | Multiple valid approaches, large refactor, unclear blast radius—you want a written approach before edits. |
| **Agent** | Approach is clear, edits are localized, tests or linters will catch mistakes. |

If the product UI for “agent” is still awkward for multi-file refactors, **fall back**: small agent steps, or edit critical paths yourself and use the agent for tests and docs.

---

## Chunking and verification

1. **Smallest shippable slice** — e.g. one endpoint, one flag path, one failing test fixed first.
2. **Run verify after each slice** — same command you would use before PR (see [`../device/work.md`](../device/work.md) *Test locally*).
3. **Read the diff** — especially generated files and migrations; do not merge blind.

---

## Agent vs terminal

| Situation | Prefer |
| --- | --- |
| **One-off** `git status`, `git diff`, short `grep` | Terminal (fast, exact). |
| **Multi-file** search-and-replace with context | Agent with a tight prompt. |
| **Long** test suite, build, install | Terminal (or agent with explicit command, then inspect output). |
| **Interactive** prompts, MFA, secrets | Human in terminal; do not paste secrets into chat. |

Keep a **pinned** terminal in the repo root; see [`repo-bootstrap.md`](repo-bootstrap.md).

---

## Rewrite a few files, then re-read

When the agent **rewrites** several files:

1. Open the **diff** or changed files in the editor.
2. Check **invariants**: error handling, nil checks, API contracts, config keys.
3. Run **targeted** tests for touched packages before the full suite.

---

## Parallelism while models run

Slower models are acceptable if **your** time is not idle: kick off a plan or long test run, then triage email, update the ticket, or draft the PR description. **Planning** with a cheaper or faster model and **reviewing** with a stronger one is a valid split; see [`models-and-modes.md`](models-and-modes.md).
