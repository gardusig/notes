# Trips

Trip runbooks: long legs, anchors (appointments, events), and checklists so the next trip starts from structure instead of a blank page. **Live dates, timetables, and ticket rows** stay in your calendar or operator apps; these files keep **rules, order of operations, and price structure**.

## Index

- [Purpose](#purpose)
- [Guidance](#guidance)
- [Common heuristics](#common-heuristics)
- [Hub buffers and anchors](#hub-buffers-and-anchors)
- [Metro vs ride-hail (connectors)](#metro-vs-ride-hail-connectors)
- [Purchase runbook (order)](#purchase-runbook-order)
- [Timing worksheet](#timing-worksheet)
- [Hotel decision rule](#hotel-decision-rule)
- [Checklist](#checklist)
- [Planning outside these files](#planning-outside-these-files)
- [Trips in this folder](#trips-in-this-folder)
- [Adding a new trip](#adding-a-new-trip)

## Purpose

This folder holds **itineraries, purchase order, and reusable runbooks** for travel that matters (tattoo trips, conferences, and similar). Shared rules live **here**; each trip file stays **corridor- or event-specific** (stations, local names, and map pins stay in that file).

## Guidance

- **Bus tickets:** buy through **[ClickBus](https://www.clickbus.com.br/)** or compare with **other aggregators and the bus company’s own site or app**—whichever shows the right route, seat map, and cancellation rules for your trip. Keep a **PDF or offline copy** of the ticket and seat assignment.
- **Long legs:** when the operator offers a **seat map**, pick an **individual / single seat** (or the best comfort tier you will actually use) on **overnight or multi-hour** buses so sleep and elbow room are predictable.
- **Comfort:** for night buses, a **blanket or layer** in a **large backpack** (plus earplugs, water, snack) beats assuming onboard amenities.
- **Flights:** for **long distances**, trips where you will **visit several places**, or **work-driven** travel with tight calendars, **flights** are often the better default than grinding a bus—this folder still assumes many **medium-length** trips stay on **road** unless the trip file says otherwise.

## Common heuristics

- **Buy the large “outside” legs first** — the long **arrival into** and **departure out of** the destination window (the frame around the anchor), before short connectors and, when hotel cancellation policy allows, before locking accommodation. That keeps return from becoming an afterthought.
- **Long overnight or long-haul bus:** prefer **individual / single seat** (or the best comfort tier you will actually use) so sleep and focus time are predictable.
- **Night bus vs flight:** default to **overnight or night-range bus** when total **in-seat or door-to-door** time is moderate. Treat **flight + airport + security + transfers** as worth it when the trip is **very long**, when you need **multi-stop tourism or work flexibility**, or when bus door-to-door pain clearly exceeds what you are willing to tolerate (see **~12 hours** as a rough ceiling for “maybe still bus” in many cases). Otherwise **night travel on the road** can be enough and airport bureaucracy is optional.

## Hub buffers and anchors

- Work **backward** from the anchor; write down last safe departure from each hub.
- At big transfer hubs, keep about **60–90 minutes** of safety buffer unless you know the station well.
- After an **overnight bus**, allow **personal cushion** before a fixed morning commitment (shower, food, check-in, last mile) — add whatever you need; do not assume you can go straight to the anchor.

## Metro vs ride-hail (connectors)

When a trip file routes you through a **metro or urban rail segment** between a bus terminal and another hub, that leg is usually **cheap and fast**. You can **replace it with a ride-hail or taxi** if you miss the last train, carry awkward luggage, or need door-to-door relief — but that is **usually more expensive** and traffic-dependent; treat it as a **fallback**, not the default budget.

**Service hours:** use the **local metro operator’s published first/last train times** (and holiday or weekend exceptions) for the **calendar day** you travel. Trip-specific files may link to an operator; do not assume trains run all night.

## Purchase runbook (order)

1. Confirm anchor date/window.
2. **Lock long arrival + long return** (outside the core stay) when you can assign seats — especially if you want **individual seat** on overnight legs.
3. Reserve hotel aligned with schedule (see [Hotel decision rule](#hotel-decision-rule)).
4. Buy short connectors nested around the long legs.
5. Confirm metro credit, app ride balance, card limit/expiry, backup payment.
6. Keep tickets and seat info **offline**.

## Timing worksheet

1. Lock the critical long leg that pins the schedule.
2. Work backward for latest safe departure from origin.
3. Keep hub buffers (see [Hub buffers and anchors](#hub-buffers-and-anchors)).
4. If you need a large cushion before a long bus (for example **4h30–5h** total before departure from a **major hub terminal**), write the chain explicitly in the trip file.

## Hotel decision rule

- **Flexible cancellation:** you can book hotel before all bus legs are final.
- **Strict / non-refundable:** lock **long outside legs** first, then hotel.
- Align **sleep nights** with the real anchor window (tattoo, conference, etc.).

## Checklist

- [ ] Confirm dates / anchor event.
- [ ] Book **main long transport** (arrival + departure frame) with **seat preference** (individual seat on long legs when offered).
- [ ] Book connectors / local legs around the anchor.
- [ ] Hotel: match **cancellation policy** vs transport lock-in (correct booking order).
- [ ] Timing worksheet: hub buffers, work backward from anchor.
- [ ] Payments: card limits, backup method, app balances (rides, metro).
- [ ] Offline copies: tickets, seats, confirmations.
- [ ] Optional: costs table + rough total in the trip file.
- [ ] Related links: only paths that exist in this repo (or one-line note if external).

## Planning outside these files

Use a **calendar** (and operator apps) for real times and tickets. If you use an **external chat or AI**, paste only what you need (anchor time, operator links, this repo’s runbook path); **trip markdown files in this folder do not need embedded AI prompt blocks**.

## Trips in this folder

| Trip | File |
|------|------|
| Tattoo runbook (home on the coast, anchor at the shop inland, bus + cost skeleton) | [`tattoo.md`](tattoo.md) |

## Adding a new trip

1. Duplicate an existing trip file (for example [`tattoo.md`](tattoo.md)), rename it under `trips/`, and delete sections you do not need.
2. Fill anchor dates in your calendar first; then **long arrival and long return**, then connectors and hotel per cancellation risk (see [Purchase runbook](#purchase-runbook-order)).
3. Add a row to the [table above](#trips-in-this-folder) and keep relative links consistent with this README.
