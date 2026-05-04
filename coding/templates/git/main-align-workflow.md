# Align local `main` to canonical remote

Make **`main`** match the **canonical** remote branch your team treats as source of truth. **Destructive** (`reset`, `clean`): confirm with the repo owner or runbook before proceeding.

1. `git rev-parse --is-inside-work-tree`.
2. **`git checkout main`** first (no fetch/reset before checkout). Create `main` from `origin/main` if missing locally.
3. **Fetch once:** `git fetch origin`; `git fetch upstream` if upstream exists.
4. Set **`CANONICAL_MAIN`** to **`upstream/main`** if remote `upstream` exists, else **`origin/main`**. `git rev-parse "$CANONICAL_MAIN"` must succeed.
5. **Fast path:** clean working tree and `HEAD` equals `$CANONICAL_MAIN` → done.
6. Else **align:** with a clean tree policy your team uses (e.g. `git reset --hard "$CANONICAL_MAIN"` then `git clean` as documented). Do **not** run destructive commands on a dirty tree without explicit confirmation.
7. **Do not** `git pull` after a hard reset to the same ref — you already match.
8. **Push** only if your workflow updates a personal fork’s `main`; many teams never force-push shared `main`.
