# Issue dedupe checklist (read-only)

Use **before** opening a **new** issue when volume is high.

1. **Search open:** `gh issue list --search "<keywords>" --state open --limit 20`
2. **Search closed** (regressions): same with `--state closed` or broader terms.
3. **Near-duplicates:** if found, link them in the new body or **comment** on the existing issue instead of splitting threads.
4. **Proceed** only when the new issue adds **new** scope or acceptance criteria.
