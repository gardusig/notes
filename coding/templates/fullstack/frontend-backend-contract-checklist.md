# Frontend ↔ backend contract checklist

Use before **shipping** a vertical slice or when **splitting** repos. Goal: UI and API agree on surface, errors, and evolution.

## Transport & schema

| Check | Notes |
| --- | --- |
| **Canonical API description** | OpenAPI / GraphQL schema / protobuf checked into `contracts/` or `docs/api/`. |
| **Generated clients optional** | If used, generation is scripted and CI-gated. |
| **Error shape** | Stable JSON envelope (code, message, field errors); UI maps to toasts/forms. |
| **Pagination / filtering** | Cursor vs offset documented; max limits stated. |

## Types and versioning

| Check | Notes |
| --- | --- |
| **DTO vs domain model** | Shared types only for **wire** shapes; do not leak ORM entities to web. |
| **Breaking changes** | Version path (`/v2`) or explicit deprecation header + sunset date. |
| **Null vs missing** | JSON convention documented for optional fields. |

## Runtime configuration

| Check | Notes |
| --- | --- |
| **Base URL per env** | `web` reads from env/build-time config; no hardcoded prod URLs in source. |
| **CORS / cookies** | Documented for local dev vs deployed; SameSite / CSRF if cookie session. |
| **Auth** | Bearer vs cookie; refresh strategy; what the API expects on each route class. |

## Testing

| Check | Notes |
| --- | --- |
| **Contract tests** | Minimal golden requests/responses or Pact-style if multi-team. |
| **E2E owns one path** | Critical user journey hits real API (or realistic mock). |

## Related

- API wiki stubs: [`../doc/wiki/api/endpoints-template.md`](../doc/wiki/api/endpoints-template.md), [`../doc/wiki/api/schemas-template.md`](../doc/wiki/api/schemas-template.md)
- Request path diagram: [`../diagrams/template-request-path.md`](../diagrams/template-request-path.md)
