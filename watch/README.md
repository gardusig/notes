# 📺 Watch — log and queue

**Finished** titles in **movies**, **tv-series**, **anime** (each: **Liked** / **Disliked** / **Unopinionated queue**). **Backlog** only in **[to-watch.md](to-watch.md)** by medium and kind.

## 📑 Index

| File | Purpose |
| --- | --- |
| **[movies.md](movies.md)** | Finished films. |
| **[tv-series.md](tv-series.md)** | Finished TV. |
| **[anime.md](anime.md)** | Finished anime. |
| **[to-watch.md](to-watch.md)** | Backlog by medium and kind. |

## 🧭 From here

1. **Finished a title** → add/move row in the right **watched** file (usually **Unopinionated queue** first).
2. **Planning what to watch** → [`to-watch.md`](to-watch.md) by medium + kind.
3. **Wiki for a title** → [`../read/library-links.md`](../read/library-links.md) when you keep longform notes paired.

---

## 📜 Conventions

### 📌 Details links

Use stable hubs for cast and metadata — **IMDb** (`https://www.imdb.com/title/tt…`) or **The Movie Database** series/film pages. Prefer the **title** page for films and the **series** page for TV/anime unless you need a specific season.

### 🎬 Franchise / sequences (movies)

Repeat **`Franchise`** on each row so sorts keep sequels together. Within a franchise, sort by **`Year`** ascending.

### 📚 Watched library (`movies` / `tv-series` / `anime`)

Each file is **finished-only** and has:

1. **Liked** — keep-tier titles you endorse (optional `###` franchise blocks under **Liked** for films).
2. **Disliked** — finished titles you did not want to keep in rotation.
3. **Unopinionated queue** — finished titles you have not sorted into like/dislike yet; keep **MRU order** (most recently watched on top).

**`Watched`** column on films — optional completion date or `—`.

| Medium | File | Typical columns |
|--------|------|-----------------|
| Movies | [movies.md](movies.md) | **Liked:** Franchise · Title · Year · Runtime · Watched · Details · **Disliked:** Franchise · Title · Year · Runtime · Watched · Notes · Details · **Queue:** Title · Year · Runtime · Watched · Notes · Details |
| TV | [tv-series.md](tv-series.md) | **Liked / Disliked / Queue:** Title · Coverage · Years · Total duration · Details (Disliked adds **Notes**) |
| Anime | [anime.md](anime.md) | **Liked / Disliked / Queue:** Title · Coverage · Release years · Total duration · Details (Disliked adds **Notes**) |

### 📋 To-watch queue ([to-watch.md](to-watch.md))

1. **`## Movies`** / **`## TV series`** / **`## Anime`** — medium.
2. **`### Kind`** — e.g. Horror, Documentary, Action, Sci-fi, Thriller, Drama (add headings as you like; no fixed list).
3. One **markdown table** per `### Kind`; only rows for that kind.

**Columns:** `Title` · `Year` (or `—`) · `Notes` · `Details` (link). Optional **`Because`** — short tie to something in **Liked** / **Queue** in the watched files (e.g. `Potter · YA fantasy`) so the backlog doubles as a **similar-to** suggestion list.

**Sort:** default **title A–Z** within each table. Optional **`Order`** column if you want manual priority without alphabetical order.

**Add:** pick medium → kind → append row → re-sort A–Z if needed.

**Promote to watched:** copy the row into **[movies.md](movies.md)** / **[tv-series.md](tv-series.md)** / **[anime.md](anime.md)** (usually **Unopinionated queue** first), fill **Runtime** / **Coverage** as needed, then remove the row from **to-watch**.

**Move between buckets:** when you know how you feel about a finished title, move the row from **Unopinionated queue** to **Liked** or **Disliked** (or the reverse if you change your mind).

**Parent:** [Notes root](../README.md)
