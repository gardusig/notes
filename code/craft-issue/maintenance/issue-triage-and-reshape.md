# Issue triage and reshape

**Upstream:** [`code/README.md`](../../README.md)

Use this when your candidate issue may overlap with existing open work, or when a quick draft needs to become implementation-ready before coding starts.

## Index

- [When to run this](#when-to-run-this)
- [Triage flow](#triage-flow)
- [Reshape checklist](#reshape-checklist)
- [Agent assist](#agent-assist)

---

## When to run this

Run this flow before creating a new issue when any of these are true:

- The repository already has active work in the same area.
- The ticket came from phone notes or a rushed capture.
- Acceptance criteria or non-regression behavior are still vague.

Skip only when you are certain the issue is unique and already implementation-ready.

---

## Triage flow

1. **Search open issues** by concrete keywords and domain terms.
2. **Search closed issues** for regressions and prior context.
3. **Classify overlap**:
   - Duplicate: same outcome and same scope.
   - Related: same area, different scope.
   - New: distinct scope or acceptance bar.
4. **Decide action**:
   - Duplicate: comment/link instead of creating a new thread.
   - Related: open a focused issue and link peers.
   - New: proceed with a full body.

Command shapes live in the dedupe checklist in **[cursor-skills](https://github.com/gardusig/cursor-skills)** ([`skills/read/gh/issue-dedupe/dedupe-checklist/SKILL.md`](https://github.com/gardusig/cursor-skills/blob/main/skills/read/gh/issue-dedupe/dedupe-checklist/SKILL.md)).

---

## Reshape checklist

Before marking an issue ready for implementation, verify:

1. **Goal/outcome** is specific and testable.
2. **Current behavior** has at least one concrete example.
3. **Desired behavior** has at least one concrete example.
4. **Scope and non-goals** are explicit.
5. **Non-regression expectations** are explicit.
6. **Verification** includes acceptance and regression intent.
7. **Worked examples / edge cases** are documented.
8. **Risks or open questions** are visible to implementers.

This checklist aligns with:

- [`skills/read/gh/issue-spec/SKILL.md`](https://github.com/gardusig/cursor-skills/blob/main/skills/read/gh/issue-spec/SKILL.md)
- [`skills/read/plan/core/github-issue-profile/SKILL.md`](https://github.com/gardusig/cursor-skills/blob/main/skills/read/plan/core/github-issue-profile/SKILL.md)

---

## Agent assist

Use a **Cursor agent** (or Plan mode) for the heavy lifting: keyword search across issues, overlap summaries, gap checks against the reshape list, and tightening prose. Exact **invokes and guardrails** change whenever you refresh your skills pack, so keep this page about **intent** (search → classify → reshape → mutate only when ready).

For install layout, current `@` skill names, and GitHub-oriented workflows, use **[gardusig/cursor-skills](https://github.com/gardusig/cursor-skills)**—start at [`README.md`](https://github.com/gardusig/cursor-skills/blob/main/README.md) and [`docs/README.md`](https://github.com/gardusig/cursor-skills/blob/main/docs/README.md). Pick whichever installed skills match shortlisting, read-only review, and issue create/edit; names drift, goals do not.
