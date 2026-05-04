# Delete closed GitHub issues (bulk)

**Danger:** irreversible. Use only when policy allows (spam, migration cleanup).

Typical **`gh`** shapes (adapt limits and labels):

```bash
gh issue list --state closed --limit 200 --json number,title
```

```bash
gh issue delete 123 --confirm
```

Batching is team-specific—script carefully and dry-run with **`--json`** listing first.
