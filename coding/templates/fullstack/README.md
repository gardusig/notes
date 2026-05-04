# Full stack & study templates (`fullstack/`)

**Upstream:** [`../README.md`](../README.md)

Domain-shaped **pasteables** for **full stack applications** (split front/back, shared packages, contracts) and **structured study** pages that pair well with [`../diagrams/`](../diagrams/). For generic wiki depth (operations, data, conventions), still use [`../doc/wiki/profiles/coding/`](../doc/wiki/profiles/coding/).

## Index

1. [`repo-layout-domain-split.md`](repo-layout-domain-split.md) — monorepo-style tree: domains, apps, packages
2. [`frontend-backend-contract-checklist.md`](frontend-backend-contract-checklist.md) — API, types, env, versioning
3. [`study-topic-sheet.md`](study-topic-sheet.md) — one topic: goals, diagram slots, exercises

---

## Coverage map (what you already had vs this folder)

| Use case | Prefer |
| --- | --- |
| **PR / issue / git** hygiene | [`../pr/`](../pr/), [`../gh/`](../gh/), [`../git/`](../git/) |
| **Doc wiki** (coding profile) | [`../doc/wiki/profiles/coding/`](../doc/wiki/profiles/coding/) — architecture, data, operations |
| **README hierarchy** | [`../doc/readme/README_AND_FOLDER_SCAFFOLD.md`](../doc/readme/README_AND_FOLDER_SCAFFOLD.md) |
| **Split full stack + domain folders** | **`repo-layout-domain-split.md`** |
| **Contract between UI and API** | **`frontend-backend-contract-checklist.md`** |
| **Study session with diagrams** | **`study-topic-sheet.md`** + [`../diagrams/template-mindmap-study.md`](../diagrams/template-mindmap-study.md), [`../diagrams/template-er.md`](../diagrams/template-er.md), [`../diagrams/template-request-path.md`](../diagrams/template-request-path.md) |
| **Deploy / env topology** | [`../diagrams/template-deployment-topology.md`](../diagrams/template-deployment-topology.md) + operations wiki |

This folder does **not** replace API endpoint stubs—those stay under [`../doc/wiki/api/`](../doc/wiki/api/).

---

## Intentionally light (add in-repo when needed)

| Area | Where to grow |
| --- | --- |
| **Mobile native, game clients, desktop** | Own `apps/` + platform runbooks; no generic template here. |
| **Realtime / WebSocket** | Extend [`../diagrams/template-sequence.md`](../diagrams/template-sequence.md) with a persistent connection lifeline. |
| **Compliance / audit narratives** | Knowledge wiki + legal; keep code templates vendor-neutral. |
