# Title (plain text) — PR and GitHub issue

Use **one line** for **pull request titles** and **GitHub issue titles**.

- **No emoji**, no markdown headings, no leading decorative symbols.
- Be **specific**: reader should understand outcome without opening the item.

## Pull request

Summarize **the whole branch outcome** vs destination (concrete themes from paths + commits).

**Linked task / issue — evaluate before finalizing:**

1. **Branch name** — ticket slug → prefix candidate.
2. **Commit messages** — `Fixes #n`, `Closes #n`, `JIRA-KEY`, etc.
3. **Existing PR** (if editing) — linked issues / project fields.
4. **User / task context** — ticket keys in chat.
5. **Choose:** **`KEY-123: Outcome`** or **`#78: Outcome`** if clear; else omit prefix and put details in the body.

**Avoid** empty process titles (“Update PR”, “Sync”, “WIP”) unless that is literally the only effect.

**PR body:** [`../pr/body-skeleton.md`](../pr/body-skeleton.md). Add optional sections (migration, rollout, screenshots) per your team’s PR template.

## GitHub issue

Same rules: **descriptive**, **no emoji** in the title. Put emoji on **`##` section headings** in the body only (see [`../gh/issues/body-skeleton.md`](../gh/issues/body-skeleton.md)).
