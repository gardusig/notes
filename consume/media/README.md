# Media — watch log and queue

**Watched** titles (finished) live in **`movies.md`**, **`tv-series.md`**, and **`anime.md`**. **To watch** lives only in **[to-watch.md](to-watch.md)** — bucketed by **medium** and **kind** (same idea as [video-game domains + Kind](../../play/video-games/owned-queue.md) and [genre × situation](../../play/video-games/genre-situations.md)).

Fan wikis and longform tied to the card library: **[read/library-links.md](../read/library-links.md)**. **Listening** — music: **[playlists/README.md](../playlists/README.md)** · podcasts + live: **[channels/README.md](../channels/README.md)**.

**Upstream:** [consume/README.md](../README.md) · **Offline inventory:** [device/micro-sd.md](../../device/micro-sd.md)

---

## Conventions

### Details links

Use stable hubs for cast and metadata — **IMDb** (`https://www.imdb.com/title/tt…`) or **The Movie Database** series/film pages. Prefer the **title** page for films and the **series** page for TV/anime unless you need a specific season.

### Franchise / sequences (movies)

Repeat **`Franchise`** on each row so sorts keep sequels together. Within a franchise, sort by **`Year`** ascending.

### Watched tables

| Medium | File | Typical columns |
|--------|------|-----------------|
| Movies | [movies.md](movies.md) | Franchise · Title · Year · Runtime · Watched · Details |
| TV | [tv-series.md](tv-series.md) | Title · Coverage · Years · Total duration · Details |
| Anime | [anime.md](anime.md) | Title · Coverage · Years · Total duration · Details |

**`Watched`** — optional completion date or `—`.

### To-watch queue ([to-watch.md](to-watch.md))

1. **`## Movies`** / **`## TV series`** / **`## Anime`** — medium.
2. **`### Kind`** — e.g. Horror, Documentary, Action, Sci-fi, Thriller, Drama (add headings as you like; no fixed list).
3. One **markdown table** per `### Kind`; only rows for that kind.

**Columns:** `Title` · `Year` (or `—`) · `Notes` · `Details` (link).

**Sort:** default **title A–Z** within each table. Optional **`Order`** column if you want manual priority without alphabetical order.

**Add:** pick medium → kind → append row → re-sort A–Z if needed.

**Promote to watched:** copy the row into `movies.md` / `tv-series.md` / `anime.md`, fill **Runtime** / **Coverage** as needed, then remove the row from **to-watch**.

---

## Index

- [movies.md](movies.md) — watched films
- [tv-series.md](tv-series.md) — watched TV
- [anime.md](anime.md) — watched anime
- [to-watch.md](to-watch.md) — queue by medium and kind
