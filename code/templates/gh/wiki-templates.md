# 📋 GitHub wiki templates

Wiki-first issue and pull request drafting templates.

## 🗂️ Hub

Use these templates when drafting GitHub issues or pull requests.

- Keep title lines plain text, specific, and single-line.
- Put emoji in section headings only (not in titles).
- Prefer concise structure over long narrative filler.

## 📋 Issue templates

### 📋 Issue body template

Use [`issues/body-skeleton.md`](issues/body-skeleton.md) as the base body scaffold.

- Add clear goal, current behavior, desired behavior, and verification.
- Include risks and open questions only when relevant.
- Add examples table when behavior is ambiguous.

### 🛠️ Issue crafting checklist

1. Check for duplicates before drafting.
2. Draft title/body with measurable acceptance criteria.
3. Add labels only when they improve triage.
4. Resolve open questions before mutation.
5. Create/edit/close issue only after scope is explicit.

### 📋 Issue review report template

Use this structure for read-only issue reshaping:

- Target snapshot
- Codebase fit
- Overlap with existing issues
- Ambiguities and missing acceptance criteria
- Proposed rewritten title/body

### 📐 Issue work plan template

Use [`../plan/work-plan-with-issue.md`](../plan/work-plan-with-issue.md) for execution handoff with:

- Issue URL/number/title
- Goal statement
- Ordered plan steps
- Verification checklist

## 📋 Pull request templates

### 🏷️ PR title rules

Use [`../pr/title-rules.md`](../pr/title-rules.md) and [`../shared/title.md`](../shared/title.md).

- No emoji in the title.
- Summarize branch outcome, not process.
- Include issue/ticket prefix only when it is explicit and useful.

### 📋 PR body template

Use [`../pr/body-skeleton.md`](../pr/body-skeleton.md).

Recommended order:

1. TL;DR
2. What changed (grouped by subsystem)
3. Choices and tradeoffs
4. Caveats

### 🛠️ PR crafting checklist

1. Review branch delta and intended merge outcome.
2. Draft title and body.
3. Remove filler sections and redundant test prose.
4. Confirm risk statement and caveats.
5. Create or edit PR.

### 📋 PR section templates

Canonical sections to keep consistent across large PRs:

- TL;DR
- What changed
- Choices and tradeoffs
- Caveats

## 📌 Related

- [`README.md`](README.md)
- [`issues/README.md`](issues/README.md)
- [`../pr/README.md`](../pr/README.md)
