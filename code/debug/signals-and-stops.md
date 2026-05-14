# 📡 Signals and stops (return to Plan or ticket)

**Upstream:** [`README.md`](README.md)

Use this when implementation **feels** productive but is **not** converging.

| Symptom | Likely issue | Prefer |
| --- | --- | --- |
| You **re-prompt** with the same context in different words | Plan or ticket missing constraints, order, or acceptance | **Stop** coding; paste ticket + plan into Plan mode and **merge** edits into the plan or issue, then resume |
| **Scope creep** in the chat (new files, “while we’re here”) | No explicit in/out in ticket | **Park** extras as new bullets or a follow-up issue; finish one vertical slice |
| **Verify** fails and it is unclear **what** owns the failure (test, flake, env, product bug) | Under-specified expected behavior | Re-read acceptance; add one **minimal** repro or assertion; if still fuzzy, spike or clarify with human |
| Agent (or you) keeps **editing wildly** without a green verify | Plan did not name **order of operations** or **commands** | Roll back to [`plan-mode-sharpen.md`](plan-mode-sharpen.md) until verify steps are explicit |
| **Prod** looks wrong after release | Env vs code vs data | Follow [`../observe/prod-ui-flows.md`](../observe/prod-ui-flows.md); keep bookmarks in [`../../setup/work.md`](../../setup/work.md) |

**Rule of thumb:** if you would not paste the current chat into a design review, **reset** to ticket + sharpened plan before more code.
