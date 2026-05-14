# ♻️ Lifecycle map and cursor-skills

**Upstream:** [`README.md`](README.md) · [`../README.md`](../README.md)

Maps delivery phases to runbook pages in `code/` and to the **[cursor-skills](https://github.com/gardusig/cursor-skills)** pack (canonical `SKILL.md` on `main`). Install the pack locally for `@` invokes. Skill **names** can change; match by **lane** (plan, Git, GitHub) via the pack [`README.md`](https://github.com/gardusig/cursor-skills/blob/main/README.md) and [`docs/README.md`](https://github.com/gardusig/cursor-skills/blob/main/docs/README.md).

## ♻️ Lifecycle map

| Phase | Start in notes | Optional cursor-skills references |
| --- | --- | --- |
| Shape the work item | [`../craft-issue/creativity/create-engineering-task.md`](../craft-issue/creativity/create-engineering-task.md) | [issue-spec](https://github.com/gardusig/cursor-skills/blob/main/skills/read/gh/issue-spec/SKILL.md), [github-issue-profile](https://github.com/gardusig/cursor-skills/blob/main/skills/read/plan/core/github-issue-profile/SKILL.md) |
| Sharpen plan before edits | [`../debug/README.md`](../debug/README.md) (task resolution), [`../craft-issue/creativity/plan-first-and-ui-context.md`](../craft-issue/creativity/plan-first-and-ui-context.md) | [readiness-checklist](https://github.com/gardusig/cursor-skills/blob/main/skills/read/plan/core/readiness-checklist/SKILL.md), [structured-qa](https://github.com/gardusig/cursor-skills/blob/main/skills/write/plan/structured-qa/SKILL.md), [plan hub](https://github.com/gardusig/cursor-skills/blob/main/skills/plan/SKILL.md) |
| Shape the system (contracts, boundaries) | [`../design/README.md`](../design/README.md) | — |
| Sort and dedupe issue candidates | [`../craft-issue/maintenance/issue-triage-and-reshape.md`](../craft-issue/maintenance/issue-triage-and-reshape.md) | [issues/review](https://github.com/gardusig/cursor-skills/blob/main/skills/gh/issues/review/SKILL.md), [issues/pick](https://github.com/gardusig/cursor-skills/blob/main/skills/gh/issues/pick/SKILL.md), [dedupe-checklist](https://github.com/gardusig/cursor-skills/blob/main/skills/read/gh/issue-dedupe/dedupe-checklist/SKILL.md) |
| Execute changes | [`../craft-pr/work-task-with-agents.md`](../craft-pr/work-task-with-agents.md) | [git/review](https://github.com/gardusig/cursor-skills/blob/main/skills/git/review/SKILL.md), [evaluate](https://github.com/gardusig/cursor-skills/blob/main/skills/write/gh/evaluate/SKILL.md) |
| Review before merge | [`../quality/review-calm-read.md`](../quality/review-calm-read.md) | [gh/pr](https://github.com/gardusig/cursor-skills/blob/main/skills/gh/pr/SKILL.md), [PR section templates](https://github.com/gardusig/cursor-skills/blob/main/skills/template/gh/pr/section-templates/SKILL.md) |
| Publish and post-merge verify | [`quick-shipping-pattern.md`](quick-shipping-pattern.md), [`post-merge-checklist.md`](post-merge-checklist.md); team bookmarks in [`../../setup/work.md`](../../setup/work.md); prod UI tracing [`../observe/prod-ui-flows.md`](../observe/prod-ui-flows.md) | — |
