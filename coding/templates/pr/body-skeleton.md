# PR body skeleton (paste and fill)

**Title:** plain text only — [`../shared/title.md`](../shared/title.md) (no emoji in the PR **title**). **Section headings** below use a **single leading emoji** on each `##` line.

**Information order:** TL;DR → What changed → Choices & tradeoffs → Caveats / Extras.

```markdown
## ⚡ TL;DR
- **Merges** … — …
- **Risk / scope:** *…*

## 📋 What changed
- **API / services**
  - …
- **Docs & DX**
  - …
- **CI**
  - …

## ⚖️ Choices & tradeoffs
- **…**
  - *Problem:* …
  - **This PR:** …
  - *Alternative:* …
  - **Why here:** …

## ⚠️ Caveats
- …
```

**Do not include:** redundant “how to verify” when CI or your PR template already lists commands. **Do not** paste commit counts / base–HEAD tables as filler unless they tell a story.

Extend sections as needed; the skeleton above is the minimum useful shape.
