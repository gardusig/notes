# Issue labels — decorate before create/edit

Use when **`gh issue create`** / **`gh issue edit`** should carry **0–3** high-signal labels.

1. List existing: `gh label list --limit 200`
2. Prefer **existing** labels; create new ones only after naming convention check.
3. Map title/body keywords → labels (e.g. `bug`, `docs`, `area/api`).
4. Pass **`--label "a,b"`** on create/edit when agreed.

**Example input:** “Add `ci` and `flaky-test` labels to the new issue.”
