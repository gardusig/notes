# Work a task with agents

**Upstream:** [`code/README.md`](../README.md)

How to **execute** work after [`../craft-issue/creativity/create-engineering-task.md`](../craft-issue/creativity/create-engineering-task.md) is written. Complements [`../../setup/work.md`](../../setup/work.md) (review, deploy, verify) with **Cursor-specific** habits.

## Index

- [Purpose](#purpose)
- [Plan vs Agent mode](#plan-vs-agent-mode)
- [Chunking and verification](#chunking-and-verification)
- [Test design and scenario creativity](#test-design-and-scenario-creativity)
- [Agent vs terminal](#agent-vs-terminal)
- [Rewrite a few files, then re-read](#rewrite-a-few-files-then-re-read)
- [Calm review pass](#calm-review-pass)
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

When the task is **actually next priority**, prefer the **heavy Plan** recipe in [`../debug/README.md`](../debug/README.md): load **as much context** as you can (`@` files, ticket text, logs), **sharpen the plan in place** until it names files, order, and verify steps—then execution needs **few** follow-up instructions.

If the product UI for “agent” is still awkward for multi-file refactors, **fall back**: small agent steps, or edit critical paths yourself and use the agent for tests and docs.

---

## Chunking and verification

1. **Smallest shippable slice** — e.g. one endpoint, one flag path, one failing test fixed first.
2. **Run verify after each slice** — same command you would use before PR (see [`../../setup/work.md`](../../setup/work.md) *Test locally*).
3. **Read the diff** — especially generated files and migrations; do not merge blind.

---

## Test design and scenario creativity

For meaningful confidence, design tests as a set, not a single happy-path command:

1. **Acceptance paths** — prove the requested behavior works as specified.
2. **Regression paths** — prove old behavior that must stay stable is still stable.
3. **Negative paths** — invalid input, permission errors, timeouts, empty data, and boundary cases.
4. **Edge creativity** — include realistic weirdness (out-of-order events, partial state, stale caches, locale/timezone corners) for your domain.

When writing the task or issue, make verification executable by another engineer without follow-up clarification.

Reference contract:

- [issue-spec (cursor-skills)](https://github.com/gardusig/cursor-skills/blob/main/skills/read/gh/issue-spec/SKILL.md)

---

## Agent vs terminal

| Situation | Prefer |
| --- | --- |
| **One-off** `git status`, `git diff`, short `grep` | Terminal (fast, exact). |
| **Multi-file** search-and-replace with context | Agent with a tight prompt. |
| **Long** test suite, build, install | Terminal (or agent with explicit command, then inspect output). |
| **Interactive** prompts, MFA, secrets | Human in terminal; do not paste secrets into chat. |

Keep a **pinned** terminal in the repo root; see [`../craft-issue/maintenance/repo-bootstrap.md`](../craft-issue/maintenance/repo-bootstrap.md).

---

## Rewrite a few files, then re-read

When the agent **rewrites** several files:

1. Open the **diff** or changed files in the editor.
2. Check **invariants**: error handling, nil checks, API contracts, config keys.
3. Run **targeted** tests for touched packages before the full suite.

---

## Calm review pass

Before you call the change “ready,” use a **calm read** of the diff and test output: stop starting new work for a bounded window and read like you are on-call, not like you are prompting. Full draft ritual: [`../quality/review-calm-read.md`](../quality/review-calm-read.md) (**under research**).

---

## Parallelism while models run

Slower models are acceptable if **your** time is not idle: kick off a plan or long test run, then triage email, update the ticket, or draft the PR description. **Planning** with a cheaper or faster model and **reviewing** with a stronger one is a valid split; see [`../craft-issue/creativity/models-and-modes.md`](../craft-issue/creativity/models-and-modes.md).
