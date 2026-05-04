# microSD card — large offline library (capacity over speed)

## Purpose

This note covers a **microSD** card used with an **Android phone** (see **[android.md](./android.md)**) to hold **pre-downloaded** video and audio for **offline** use: travel, commuting, and low or no connectivity. **Capacity matters more than speed**: sequential read for **1080p** / modest **bitrate** files does **not** require top-tier **UHS-II** or **V90** cards.

Folder outline: **[README.md](README.md)**.

---

## Summary

- **Goal:** **Lots of gigabytes** for **Movies**, **Series**, and **Anime** without paying for **extreme** speed grades you will not saturate on a phone.
- **Access:** **Google Files** to browse; **VLC** to play.
- **Shopping:** Buy **reputable brand**, **U1 / A1** or better is **enough** for typical media; put savings into **512 GB–1 TB** class cards when prices allow.

---

## Index

- [Purpose](#purpose)
- [Summary](#summary)
- [Index](#index)
- [Setup & installation](#setup--installation)
- [Offline library inventory](#offline-library-inventory)
  - [Anime](#anime)
  - [Movies](#movies)
  - [Series](#series)
  - [Consumption log (same library)](#consumption-log-same-library)
- [Guidelines](#guidelines)
- [What to buy \& price expectations](#what-to-buy--price-expectations)

---

## Setup & installation

1. **Size the card** using **[What to buy](#what-to-buy--price-expectations)**—plan for **~80%** full max (see Guidelines).
2. **Insert** the microSD (power off if your phone manual says so).
3. **Format** if the phone offers **adoptable** vs **portable** storage: for **media files** only, **portable** / **external** is usually simpler to move between devices.
4. **Install** **Google Files** and **VLC** if missing (**[android.md](./android.md)**).
5. **Create folders** on the card:

```
/Movies
/Series
/Anime
```

6. **Copy** media from a PC with a **USB** reader or over **Wi‑Fi** / **MTP**; keep **consistent naming** (`Title / Season / Episode`).

### Access

- **Google Files** → browse and manage files
- **VLC** → play video/audio (broad format support)

---

## Offline library inventory

### Anime

| Title       | Coverage                       | Release Years | Total Duration |
| ----------- | ------------------------------ | ------------- | -------------- |
| Dragon Ball | Episodes 1–153                 | 1986–1989     | ~53 hours      |
| Yu-Gi-Oh!   | Seasons 1–5 (DM)               | 2000–2004     | ~82 hours      |
| Naruto      | Classic + Shippuden (complete) | 2002–2017     | ~300+ hours    |

### Movies

| Franchise    | Coverage  | Release Years | Total Duration |
| ------------ | --------- | ------------- | -------------- |
| Harry Potter | 8 movies  | 2001–2011     | ~19.5 hours    |
| Saw          | 10 movies | 2004–2023     | ~16.5 hours    |

### Series

| Title          | Coverage    | Release Years | Total Duration |
| -------------- | ----------- | ------------- | -------------- |
| Breaking Bad   | 5 seasons   | 2008–2013     | ~62 hours      |
| Inside Man     | 4 episodes  | 2022          | ~4 hours       |
| Jeffrey Dahmer | 10 episodes | 2022          | ~8.5 hours     |
| Mr. Robot      | 4 seasons   | 2015–2019     | ~45 hours      |
| Narcos         | 3 seasons   | 2015–2017     | ~30 hours      |
| Prison Break   | 5 seasons   | 2005–2017     | ~67 hours      |
| Sherlock       | 4 seasons   | 2010–2017     | ~18 hours      |

### Consumption log (same library)

Track **finished video** and **read / research** alongside this inventory:

- [Watched media log](../consume/media/README.md) — per-title tables and to-watch queue
- [Books and library links](../consume/read/README.md) — finished books, to-read queue, Fandom/Wikipedia hubs per title above

---

## Guidelines

- Prefer **high-quality files** with **sane** bitrates (balance size vs quality)—**capacity** is the scarce resource, not **card speed**.
- Use consistent naming: `Title / Season / Episode`
- Keep strict folder organization
- Avoid duplicates
- Keep storage below ~**80%** capacity
- Periodically rotate content

### Expansion priorities

- High rewatch value
- Completed series
- Efficient encoding (quality vs size)

### Notes

- This is a **personal offline library**
- Optimized for **portability and reliability**
- Fully usable **without internet**

---

## What to buy & price expectations

### Capacity first

- Estimate total **GB** from your **inventory** (rough: **1080p** ~ **1–3 GB/hour** depending on encode). Round **up** and buy the **next** common size (e.g. **256 → 512 GB**).
- **1 TB** microSD can make sense if you carry **long** series packs; compare **price per GB** across sizes.

### Speed: good enough, not extreme

- For **playback** on a phone, **U1** / **Class 10** sequential read is usually **fine**. **A1** helps a little with **small** random I/O if apps index the card—nice, not mandatory.
- **Skip** **V60/V90** and **UHS-II** unless you have a **specific** use (e.g. high-bitrate **4K** recording **to the card**). They cost more and often **do not** improve phone **VLC** experience.
- **Application rating (A2)** matters more for **running apps** from the card; this workflow is **media storage**, not **adopted app** storage.

### Reliability

- Stick to **known brands** (Samsung, SanDisk, Kingston, Lexar, etc.) from **reputable** sellers—**counterfeit** cards are common on marketplaces.
- After purchase, **H2testw** / **f3** on a PC to **verify** real capacity when in doubt.

### Money

- **Sales** and **older** generations often discount **large** cards; favor **more GB** over **faster** labels at the same price.
