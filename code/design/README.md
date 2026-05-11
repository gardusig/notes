# Design: solution shape before heavy implementation

**Upstream:** [`../README.md`](../README.md)

This folder is the **engineering design** lane: how a change sits in the system (contracts, boundaries, sketches). It is **not** the same as [`../debug/README.md`](../debug/README.md), which is **task** readiness (idea → ticket → Plan mode → execution choreography).

## When to use this lane

Pause implementation when you need to pin **APIs**, **data boundaries**, **failure modes**, or **ownership** across components—before the diff gets large.

## Scaffolds (in `templates/`)

Paste or adapt from the artifact toolbox; do not duplicate long bodies here.

- **Fullstack / contracts:** [`../templates/fullstack/README.md`](../templates/fullstack/README.md), [`../templates/fullstack/frontend-backend-contract-checklist.md`](../templates/fullstack/frontend-backend-contract-checklist.md), [`../templates/fullstack/repo-layout-domain-split.md`](../templates/fullstack/repo-layout-domain-split.md)
- **Architecture (wiki profile):** [`../templates/doc/wiki/profiles/coding/architecture-README.md`](../templates/doc/wiki/profiles/coding/architecture-README.md), [`../templates/doc/wiki/profiles/coding/architecture-decisions.md`](../templates/doc/wiki/profiles/coding/architecture-decisions.md), [`../templates/doc/wiki/profiles/coding/architecture-data-flow.md`](../templates/doc/wiki/profiles/coding/architecture-data-flow.md), [`../templates/doc/wiki/profiles/coding/architecture-system-overview.md`](../templates/doc/wiki/profiles/coding/architecture-system-overview.md)
- **API docs shape:** [`../templates/doc/wiki/api/README-template.md`](../templates/doc/wiki/api/README-template.md), [`../templates/doc/wiki/api/endpoints-template.md`](../templates/doc/wiki/api/endpoints-template.md), [`../templates/doc/wiki/api/schemas-template.md`](../templates/doc/wiki/api/schemas-template.md)

## Neighbors

- **Backlog / ticket quality:** [`../craft-issue/creativity/create-engineering-task.md`](../craft-issue/creativity/create-engineering-task.md)
- **Task planning (Plan mode, phases):** [`../debug/README.md`](../debug/README.md)
- **Implementation:** [`../craft-pr/work-task-with-agents.md`](../craft-pr/work-task-with-agents.md)
