# End-to-end request path (full stack trace)

One **happy-path** user action traced through **split** components: browser → edge → API → domain → persistence. Good for onboarding, incident runbooks, and **study** walkthroughs.

## Sequence (typical web app)

```mermaid
sequenceDiagram
  autonumber
  participant U as User / browser
  participant S as Static / CDN
  participant G as Gateway
  participant A as API service
  participant D as Domain layer
  participant DB as Database

  U->>S: GET assets (optional)
  S-->>U: JS/CSS
  U->>G: HTTPS API call
  G->>A: Forward + auth context
  A->>D: Execute use case
  D->>DB: Read / write
  DB-->>D: Rows
  D-->>A: Result / errors
  A-->>G: JSON
  G-->>U: Response
```

## Flowchart variant (batch / async)

```mermaid
flowchart LR
  subgraph trigger [Trigger]
    t[Schedule / webhook / queue message]
  end
  subgraph process [Worker]
    w[Handler]
    dom[Domain]
  end
  subgraph store [Stores]
    db[(DB)]
    obj[Object storage]
  end
  t --> w
  w --> dom
  dom --> db
  dom --> obj
```

## Related

- Generic sequence: [`template-sequence.md`](template-sequence.md)
- Layers overview: [`template-layers.md`](template-layers.md)
