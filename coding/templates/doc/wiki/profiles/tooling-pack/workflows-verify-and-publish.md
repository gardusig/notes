# Verify and publish (detail)

## Verify

1. Discover stack from **`README`**, lockfiles, and CI config.
2. Install dependencies (cached dirs when possible).
3. Run the repo’s **evaluate** commands: format (write), lint, tests, coverage if required.
4. Tighten **existing** docs in place when checks are green (no drive-by restructures unless agreed).

## Publish

1. Ensure branch is up to date with the integration branch your team uses.
2. Run verify again if you merged.
3. **Commit** with a clear message; **push**; open **`gh pr`** when ready.
4. Large or destructive doc reshapes stay **confirm-first** with the team.

## Related

- [`../../../../git/pull-workflow.md`](../../../../git/pull-workflow.md)
- [`../../../../git/push-workflow.md`](../../../../git/push-workflow.md)
- [`../../../../gh/pr-orchestration.md`](../../../../gh/pr-orchestration.md)
