# Android phone — street carry (battery-first)

## Purpose

This note is for a **daily-carry Android phone** used **outside the home**: maps, transit, chat, shopping, and **Pix** / banking **apps** on a **SIM** with mobile data. **Battery life** is the main hardware priority—**SoC tier and flagship specs are optional**; mid-range phones with a **large battery** and efficient screen often win over thin flagships.

**Role vs iPhone:** This is the **street** handset—**high** loss/theft risk—so **only two** bank apps (**Itaú** + **Nubank**) and **low** **Pix / TED** limits; the device is meant to be **easily replaceable** (minimal unique state). Heavy **gov**, **investing**, and other banks live on **desktop**, **branch**, or a **home iPhone** if you use one. Folder outline: **[README.md](README.md)**.

---

## Summary

- **Hardware:** Choose phones known for **endurance** (big battery mAh, sane display resolution/refresh, efficient chip). **Any** spec tier that meets your performance floor is fine—do not overbuy for CPU benchmarks.
- **Battery (ballpark):** On a **new** **battery-first** handset (~**4500–6000 mAh**, efficient SoC, 1080p-class display), expect about **6–10 h screen-on** on a **light** street day or **4–7 h** on a **heavy** day (long maps, cellular video)—see **[Battery life (rough estimates)](#battery-life-rough-estimates)**.
- **Software:** Fresh Android, **Google account**, **updates** on; lean **video quality** on cellular to save **data and battery**; **fingerprint / face** + **PIN** lock; **Google backup** on.
- **Banking (street rule):** **Exactly two** bank apps—**Itaú** and **Nubank**—so a lost phone is cheap to re-clone; set **low daily outgoing limits** in each (see **[Banking & payments](#banking--payments)**); **Google Wallet** = **voter / e-Título** only—**no** cards for tap-to-pay.
- **Home screen:** **Gemini**, **Gmail**, **Keep**, and **Clock** on the main row; the rest groups into a few folders (see **[Home screen layout](#home-screen-layout)**).
- **Games:** Prefer **puzzle** and **logic** titles (short sessions, low battery)—**[Classic](#classic-and-paper-era-puzzles)** and **[modern](#modern-puzzle-games)** picks below.

---

## Index

- [Purpose](#purpose)
- [Summary](#summary)
- [Index](#index)
- [Setup & installation](#setup--installation)
  - [Initial setup](#initial-setup)
  - [Home screen layout](#home-screen-layout)
  - [Google account \& services](#google-account--services)
  - [Banking \& payments](#banking--payments)
  - [Travel](#travel)
  - [Government](#government)
  - [Entertainment](#entertainment)
  - [Communication](#communication)
  - [Google apps suite](#google-apps-suite)
  - [Utilities \& tools](#utilities--tools)
  - [Games](#games)
    - [Classic and paper-era puzzles](#classic-and-paper-era-puzzles)
    - [Modern puzzle games](#modern-puzzle-games)
- [What to buy \& price expectations](#what-to-buy--price-expectations)
  - [Battery life (rough estimates)](#battery-life-rough-estimates)

---

## Setup & installation

### Initial setup

#### Basic configuration

1. Connect to Wi-Fi
2. Sign in with your Google account
3. Update system

**Settings → System → Software Update**

#### SIM and mobile data

- **Get a SIM** (chip) with a data plan that matches how you move: maps, ride-hail, Pix, and messaging should work when you are off Wi‑Fi.
- After install, confirm **mobile data** and (if you want) **VoLTE / Wi‑Fi Calling** in **Settings → Network & internet → SIMs** (wording varies by manufacturer).

#### Video quality (battery and data)

Street use is easier when video apps are not always pegged at the highest bitrate.

- **YouTube:** App **Settings → Data saving** (or **Video quality preferences**) → prefer **Data saver** / lower default on mobile networks.
- **Other streaming** (Netflix, Twitch, Kick, etc.): set **Standard** or **data-saving** quality for cellular (and optionally for Wi‑Fi if you want less heat and drain).
- **System display:** If your phone offers a **resolution** or **FHD+ / HD+** toggle under **Settings → Display**, stepping down can help a bit with GPU load and battery on long days.

#### Google Wallet — voter ID only, no payment cards

- **Do not** add **credit or debit cards** to **Google Wallet** / **Google Pay** for **contactless payment** on this phone—pay with **Pix** and banking **apps** instead, and keep cards off the device if it is lost or stolen.
- **Do** install **e-Título** (Government below) and, if the system offers it, add **only** **elector / voter** credentials to the wallet so you still have **proof of identity** if you lose your physical **RG** or wallet—treat it as an emergency document layer, not a payment stack.

#### Security

**Settings → Security**

- Enable **Fingerprint / Face Unlock**
- Set **Screen Lock (PIN or password)**

#### Backup

**Settings → Google → Backup**

- Enable automatic backup
- Ensures recovery of apps, contacts, and settings

### Home screen layout

Everything below fits **one home screen** with a few folders; other apps may stay installed for **rare** needs (Authenticator, Chrome, camera tools, etc.) without sitting on the grid.

**Main row (always visible):**

| App | Role |
| --- | --- |
| **Gemini** | Google AI assistant |
| **Gmail** | Email |
| **Keep** | Quick notes and lists |
| **Clock** | Alarms and timers (**Google Clock** or OEM equivalent) |

**Folders (grouped):**

| Folder | Apps |
| --- | --- |
| **Government** | **e-Título**, **FGTS**, **Gov.br** |
| **Travel** | **Airbnb**, **Booking**, **Google Maps**, **Uber**, **ClickBus**, **iFood**, **99** |
| **Entertainment** | **Kick**, **Stremio**, **Twitch**, **Google Files**, **YouTube**, **YouTube Music** — offline/heavy media on **[micro-sd.md](./micro-sd.md)** when the phone supports a card |
| **Communication** | **Duolingo**, **WhatsApp** |

Other installs (e.g. **Moovit**, **Waze**, **Mercado Livre**, **Bitwarden**) are optional: use when needed, keep limits and lock screen strict.

### Google account & services

Your Google account enables:

- Play Store (app installation)
- Backup & restore
- Contacts sync
- Calendar sync
- Google Photos backup
- Device tracking (Find My Device)

### Banking & payments

Banks and **Pix**—**only** **Itaú** and **Nubank** on this phone so the handset stays **easy to replace**: reinstall two apps, restore limits, move on. Do **not** add cards to **Google Wallet** here (see Initial setup).

#### Why two banks only

You carry this device **in public** every day. A stolen or **shoulder-surfed** unlock hurts less with **two** institutions and **low** caps than with a full mirror of your financial life. **CAIXA**, **C6**, **brokerages**, **Tesouro**, and **extra** wallets live on **desktop**, **branch**, or a **home iPhone** if you use one.

#### Policy — low limits, alerts

- In **Itaú** and **Nubank**, set the **lowest daily outgoing limit** you can live with for **Pix / TED / transfers** (and **card-out**, if exposed). Treat **~R$ 10.000/day** as an **upper** ceiling some banks offer—not a **target**; many people stay at **R$ 500–R$ 2.000/day** and raise temporarily from **home** when needed.
- Turn on **SMS / push / email** for **Pix** out, **TED**, new devices, and **large** debits.
- **Emergency:** need another bank for one transaction—use **home iPhone**, **web**, or install a third app **temporarily**, then remove it.

#### Apps on this phone

| App    | Description |
| ------ | ----------- |
| **Itaú** | Traditional banking and Pix. |
| **Nubank** | Digital bank (Pix, account, card **in-app**—not as a Wallet tap-to-pay token). |

### Travel

Lodging, maps, ride-hail, long-distance bus, and food delivery in one folder.

| App            | Description |
| -------------- | ----------- |
| **Airbnb**     | Short-term stays and experiences. |
| **Booking**    | Hotels and alternative lodging. |
| **Google Maps** | Navigation and places. |
| **Uber**       | Ride-hailing (and courier where used). |
| **ClickBus**   | Long-distance **bus** tickets. |
| **iFood**      | Restaurant and grocery delivery. |
| **99**         | Taxis and ride-hail (Brazil). |

### Government

Wallet policy stays **voter ID only** in **Google Wallet** (Initial setup); these apps handle **transactions and proofs** in their own ecosystems.

| App           | Description |
| ------------- | ----------- |
| **e-Título**  | Digital voter ID—wallet backup for elector proof (Initial setup). |
| **FGTS**      | Balance, statements, withdrawal rules (**Caixa**). |
| **Gov.br**    | SSO and federal/state services tied to **gov.br**. |

Other **gov** apps (**Receita**, **INSS**, **CDT**, **SUS**, state **Detran**, etc.) stay on **home iPhone** or desktop unless you deliberately add them for a trip.

### Entertainment

| App               | Description |
| ----------------- | ----------- |
| **Kick**          | Live streaming (gaming, IRL). |
| **Stremio**       | Aggregated catalogs / plugins (set **data saver** on cellular). |
| **Twitch**        | Live gaming and chat. |
| **Google Files**  | File manager, cleaner, offline playback helper. |
| **YouTube**       | On-demand video (see Initial setup for cellular quality). |
| **YouTube Music** | Music streaming. |

**microSD:** Prefer **large downloads**, **offline** music/video, and **Stremio** cache on the card when the phone supports it—see **[micro-sd.md](./micro-sd.md)** so internal storage stays light.

### Communication

| App          | Description |
| ------------ | ----------- |
| **Duolingo** | Language practice (daily streak fits street downtime). |
| **WhatsApp** | Messaging and calls (default for Brazil). |

### Google apps suite

Google apps **beyond** the home row and folder list—often installed, opened less often.

| App                  | Description |
| -------------------- | ----------- |
| Find My Device       | Lost-phone locate and secure. |
| Google Authenticator | 2FA codes. |
| Google Calendar      | Scheduling. |
| Google Chrome        | Browser with sync. |
| Google Drive         | Cloud storage. |
| Google Lens          | Translate signs, copy text from camera. |
| Google Meet          | Video calls. |
| Google Photos        | Photo backup. |
| Google Tasks         | To-dos. |
| Google Wallet        | **Only** voter / **e-Título**-style docs—**no** payment cards. |

**Gemini**, **Gmail**, **Keep**, **Maps**, **Files**, **YouTube**, and **YouTube Music** are covered in **[Home screen layout](#home-screen-layout)** and **[Travel](#travel)** / **[Entertainment](#entertainment)**.

### Utilities & tools

Third-party tools useful but **not** on the main grid by default.

| App        | Description |
| ---------- | ----------- |
| Adobe Scan | PDF scans of receipts or forms. |
| Bitwarden  | Password manager; pair with a strong lock screen. |
| Shazam     | Music identification. |
| Telegram   | Backup chat / large groups if **WhatsApp** is down. |
| VLC        | Odd video formats offline or from links. |

### Games

**Puzzle-first** list: **low** GPU load, good for **queues** and **battery**. Skip **gacha** / **idle** **grinders** on this device if you want the phone to stay **boring** and **safe**. Names vary on the Play Store—pick **well-rated** listings with **few** intrusive ads.

#### Classic and paper-era puzzles

| App / style   | Description |
| ------------- | ----------- |
| **2048**      | Sliding **powers-of-two** merge; quick rounds. |
| **Checkers**  | Classic **draughts**; many free apps. |
| **Chess**     | **Tactics** and online play; pick one **reputable** client. |
| **Crossword** | Daily **grid** puzzles (search **crossword** + a trusted publisher). |
| **Kakuro**    | **Sum-crossword** logic (often bundled in **puzzle packs**). |
| **Logic grid / Einstein riddles** | **Who owns the fish**-style deduction; search **logic puzzles**. |
| **Minesweeper** | **Classic** grid deduction. |
| **Nonogram**  | **Picture cross** / **griddlers** (fill by number clues). |
| **Number Sums** | **KenKen**-style arithmetic cages (or similar **sum** puzzles). |
| **Sudoku**    | **9×9** (and variants); dozens of **clean** apps—choose **no-account** if possible. |

#### Modern puzzle games

| App / title        | Description |
| ------------------ | ----------- |
| **Brain It On!**   | **Physics** drawing puzzles; short levels. |
| **Cut the Rope**   | **Rope / gravity** timing puzzles (series has several entries). |
| **Gorogoa**        | **Hand-drawn** panel sliding; narrative **logic** (often **paid**). |
| **Mini Metro**     | **Line-drawing** **metro** planning; calm **strategy** puzzle. |
| **Monument Valley** | **Impossible architecture** / perspective puzzles (I & II). |
| **The Room** (series) | **3D** **mechanical** **box** mysteries; darker tone, still **puzzle**-core. |
| **Threes!**        | **Number** **merge** (precursor vibe to **2048**); polished **one-hand** play. |
| **Two Dots**       | **Connect**-the-dots **objectives**; hundreds of **logic** levels. |

---

## What to buy & price expectations

### Battery and endurance first

When choosing a handset:

- Prefer **large battery** capacity (manufacturer **mAh** claims + **real-world** reviews), **efficient** SoC generation, and **sane** display (**FHD** / **1080p** class is often enough; **high refresh** costs power unless you cap it in settings).
- **Mid-range** models from reputable brands often beat **last year’s flagship** on **time off charger** for the same money.
- **Charging:** **fast charge** is convenient; **battery health** over **years** still favors not living at 100% heat all day if your ROM exposes charge limits.

### Battery life (rough estimates)

Numbers are **order-of-magnitude** for a **healthy** battery on phones **matching this guide’s “big battery / sane screen” idea**. Real life swings with **brightness**, **5G**, **temperature**, **rogue apps**, and **age** (after **1–2 years** you might see **~15–25%** less endurance than when new).

| Pattern | What it means | Typical range (new phone, this class) |
| ------- | ------------- | ------------------------------------- |
| **Heavy day** | **Hours** of **navigation** + **cellular** video / hotspot / high refresh pegged | **~4–7 h** screen-on; plan **charge in the evening** or carry a **small power bank** |
| **Light street day** | Messaging, some camera, a bit of maps, Pix, no long video | **~6–10 h** screen-on time, or **one full day** off charger with **10–25%** left at night |
| **Overnight idle** (data on) | Phone asleep, normal sync | **~3–12%** drop is common; **consistently worse** suggests **background** drain to fix in settings |
| **Typical mixed day** | Social feeds, some YouTube / streaming on **Wi‑Fi** or short cellular | **~5–8 h** screen-on; often **one day** with a **mid-day top-up** if you push it |

**Thin flagships** (~**3500–4000 mAh**) can land **~20–40%** below these **screen-on** bands unless you are careful with settings.

### Specs are flexible

- You do **not** need the latest flagship **CPU** for the app set in this note; prioritize **RAM** (6–8 GB+ for comfortable multitasking), **storage** (128 GB minimum for photos + offline media if you use **[micro-sd.md](./micro-sd.md)** or large downloads), and **LTE/5G** band support for your carrier.
- **Software support:** favor vendors with a **clear update policy** if you plan to keep the phone **3+ years**.

### Money

- **Prices in Brazil** swing with promos—check **Kabum**, **Pichau**, **Amazon.com.br**, carrier **installment** deals, and **used** markets if you accept battery wear risk.
