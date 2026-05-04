# Repo layout — domain modules + split architecture

Suggested **monorepo** (or polyrepo mirror) shape for a **full stack** product with **clear boundaries** and **domain-first** folders. Rename to match your stack (`apps/`, `services/`, `packages/` are interchangeable conventions).

## Example tree

```text
.
├── apps/
│   ├── web/                 # SPA / SSR UI — calls HTTP only to public API surface
│   └── api/                 # HTTP service — owns transport; delegates to domain
├── packages/
│   ├── domain-<name>/       # One folder per bounded context (orders, billing, …)
│   │   ├── src/
│   │   └── README.md        # Responsibilities + invariants (see wiki module-folder)
│   ├── domain-<name>/
│   ├── contracts/           # OpenAPI / protobuf / shared DTOs consumed by web + api
│   └── ui-kit/              # Optional: shared presentation primitives
├── infra/                   # IaC, Docker, k8s, CI glue (or docs/runbooks only)
├── docs/
│   └── architecture/      # Link diagrams: layers, request path, ER drafts
├── AGENTS.md
└── README.md
```

## Principles

| Choice | Why |
| --- | --- |
| **Domain packages do not import `apps/`** | Keeps deployables thin and testable without UI. |
| **`contracts/` is versioned** | Breaking API changes stay visible to both web and api. |
| **One bounded context per `domain-*` folder** | Avoids a single “god” `src/models` dump unless the product is tiny. |
| **`apps/api` wires infrastructure** | DB clients, queues, config live at the edge; domain receives interfaces/ports if you use ports style. |

## When to simplify

- **Single deployable** (e.g. Next.js full stack): collapse to `src/` with `features/<domain>/` and still keep **feature folders**—same idea, fewer roots.

## Related

- Folder README picks: [`../doc/readme/README_AND_FOLDER_SCAFFOLD.md`](../doc/readme/README_AND_FOLDER_SCAFFOLD.md)
- Module hub: [`../doc/wiki/profiles/coding/modules-README.md`](../doc/wiki/profiles/coding/modules-README.md)
- Diagrams: [`../diagrams/template-layers.md`](../diagrams/template-layers.md), [`../diagrams/template-request-path.md`](../diagrams/template-request-path.md)
