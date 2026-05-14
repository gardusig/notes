# ☑️ Post-merge checklist (stub)

**Upstream:** [`README.md`](README.md)

Thin placeholder after **Review and publish**: what to do once code is on main (or released).

- Confirm **CI / merge queue** finished green for the integration branch you care about.
- **Rollout**: note tag or release version; follow team process (deploy app, migrations, feature flags).
- **Smoke test** critical paths in the target environment; compare with [`../../setup/work.md`](../../setup/work.md) *Verify deployed results*.
- If something looks wrong in prod UI, use [`../observe/prod-ui-flows.md`](../observe/prod-ui-flows.md) and keep dashboard / escalation links in `setup/work.md`.

Expand this list when your team’s **deploy runbook** is stable enough to mirror here without duplicating secrets or URLs.
