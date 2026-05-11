# Layered / split architecture (full stack)

Shows **presentation → application → domain → infrastructure** (or a **split deployable** view: web app, API, workers). Adjust subgraph labels to match your repo (`apps/web`, `services/api`, etc.).

## Horizontal layers (single deployable)

```mermaid
flowchart TB
  subgraph presentation [Presentation]
    ui[UI / HTTP handlers]
  end
  subgraph application [Application]
    usecases[Use cases / orchestration]
  end
  subgraph domain [Domain]
    entities[Entities + domain services]
    policies[Invariants / policies]
  end
  subgraph infrastructure [Infrastructure]
    db[(DB)]
    queue[Queue / bus]
    ext[External APIs]
  end
  ui --> usecases
  usecases --> entities
  usecases --> policies
  usecases --> db
  usecases --> queue
  usecases --> ext
```

## Split packages / services (same diagram style)

```mermaid
flowchart LR
  subgraph clients [Clients]
    web[Web / SPA]
    mobile[Mobile / CLI]
  end
  subgraph edge [Edge]
    cdn[CDN / static]
    gw[API gateway]
  end
  subgraph core [Core services]
    api[HTTP API]
    bff[BFF optional]
    worker[Async workers]
  end
  subgraph data [Data plane]
    db[(Primary DB)]
    cache[(Cache)]
    bus[Message bus]
  end
  web --> cdn
  web --> gw
  mobile --> gw
  gw --> api
  gw --> bff
  bff --> api
  api --> db
  api --> cache
  api --> bus
  worker --> bus
  worker --> db
```

## Related

- System overview table + simple flow: [`../doc/wiki/profiles/coding/architecture-system-overview.md`](../doc/wiki/profiles/coding/architecture-system-overview.md)
- Repo layout ideas: [`../fullstack/repo-layout-domain-split.md`](../fullstack/repo-layout-domain-split.md)
