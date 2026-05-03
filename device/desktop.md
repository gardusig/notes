# Desktop PC — AM5 gaming tower (hardware)

## Purpose

This note is the **hardware and shopping** companion to **[windows.md](./windows.md)**. It covers **assembly**, **parts**, **peripherals**, and **GPU upgrade tiers** for a **self-assembled Windows 11–ready tower** built around **AM5** and a **Ryzen APU** (CPU + integrated graphics) so the machine **posts without** a discrete GPU, with a free **PCIe x16** slot for a **dGPU** later.

**Software, launchers, media apps, and OS tuning** live in **[windows.md](./windows.md)**—continue there after the build.

**Money:** **Prices in BRL** are **ballpark** (Brazil, promo-sensitive). Check **Kabum**, **Pichau**, **Terabyte Shop**, **Amazon.com.br** before you pay.

---

## Summary

- **Platform:** **AM5** + **Ryzen 7 8700G** or **Ryzen 5 8600G**, **32 GB DDR5**, **1 TB NVMe** + **4 TB HDD**, **750 W 80+ Gold** PSU, **Wi‑Fi** on the **motherboard**.
- **Spend (very rough):** **Tower only** about **R$ 6.200 – R$ 9.500**; **full desk** depends on monitor tier and a future **GPU**—see **[Sensible combinations](#sensible-combinations)** and **[What to buy & price expectations](#what-to-buy--price-expectations)**.
- **Next step:** **[First boot & Windows install](./windows.md#first-boot--windows-install)** in **windows.md**.

---

## Index

- [Purpose](#purpose)
- [Summary](#summary)
- [Index](#index)
- [Physical build (short checklist)](#physical-build-short-checklist)
- [What to buy & price expectations](#what-to-buy--price-expectations)
  - [Sensible combinations](#sensible-combinations)
  - [Desktop — tower, storage, PSU, cables](#desktop--tower-storage-psu-cables)
  - [While you use only the APU (no discrete GPU)](#while-you-use-only-the-apu-no-discrete-gpu-yet)
  - [Peripherals and desk](#peripherals-and-desk)
  - [Discrete GPU upgrades](#discrete-gpu-upgrades)

---

## Physical build (short checklist)

1. **Read** the **motherboard** manual for **RAM** slots, **M.2** order, and **front-panel** headers.  
2. **Install** CPU (careful with **orientation** / **lever**), **M.2 SSD**, **RAM**, then **motherboard** in the **case**; **HDD** in a **cage** with **SATA data + SATA power**.  
3. **PSU** in the **basement** or **rear** per case; route **EPS**, **24-pin**, **SATA power**; leave **PCIe** modular leads **ready** for a future **GPU**.  
4. **CPU cooler** (stock or tower); **case fans** to **intake** front / **exhaust** rear-top.  
5. **Screw** **Wi‑Fi** **antennas** to the **rear I/O** and angle them **away** from the **wall**.  
6. **Display** from **motherboard** **HDMI** or **DisplayPort** until a **dGPU** is installed—then move the cable to the **card**.

Then follow **[First boot & Windows install](./windows.md#first-boot--windows-install)** in **windows.md**.

---

## What to buy & price expectations

### Sensible combinations

Use these as **shopping bundles**, not rigid SKUs. Totals **exclude** surge strips, software, and random cables unless noted.

| Combination | What it is | Rough total (BRL) | What to expect |
| ----------- | ---------- | ------------------- | -------------- |
| **A — Tower only (APU)** | **8600G** or **8700G** build: **B650 Wi‑Fi**, **32 GB DDR5**, **1 TB NVMe**, **4 TB HDD**, **750 W Gold**, **mesh** case, **stock** cooler | **~R$ 6.200 – R$ 9.500** | **1080p** **3D** **low–medium** or **2D** **maxed**; **no** monitor/peripherals. |
| **B — APU + competitive 1080p** | **A** + **24–27″ 1080p 144 Hz IPS** + **keyboard** + **mouse** + **large pad** + **headset** | **Add ~R$ 1.400 – R$ 3.200** to **A** | **Esports**-friendly **Hz**; **GPU** optional for **AAA** **high**. |
| **C — APU + nicer screen** | **A** + **27″ 1440p 144+ Hz** + mid **peripherals** | **Add ~R$ 2.000 – R$ 4.500** to **A** | **2D** / desktop **great**; **new AAA** **3D** still wants **[GPU tier](#discrete-gpu-upgrades)** soon. |
| **D — APU + ultrawide** | **A** + **34″ 3440×1440** (or **2560×1080** budget UW) + **DP 1.4** cable | **Add ~R$ 1.200 – R$ 4.500** to **A** | **Movies** / **sims**; **heavy** **UW** **3D** assumes **dGPU**. |
| **E — APU now, GPU in 6–12 months** | **A** + monitor tier of choice + **[Entry](#discrete-gpu-upgrades)** or **[Upper entry](#discrete-gpu-upgrades)** **GPU** later | **Tower + screen** as above, then **+R$ 1.800 – R$ 3.800** (typical **entry** window) | **750 W Gold** from day one avoids a **PSU** swap with the **card**. |

**Price sanity:** **Combination A** is the **tower** row only. **B–E** **add** peripherals and/or **GPU** on top—sums overlap with sales; always **re-quote** parts.

### Desktop — tower, storage, PSU, cables

**Reference platform:** **AM5** + **Ryzen 7 8700G** or **Ryzen 5 8600G** (**APU**) so the PC **posts without** a video card. One free **PCIe x16** slot waits for a **dGPU**.

**Storage (fixed layout for this guide):** exactly **one NVMe SSD** and **one HDD**. Put **Windows**, launchers, patches, and **heavy / competitive** games on the **SSD**. Use the **HDD** for **backups**, **torrent / media** libraries, and **lighter** games where long load times are OK—**not** for the OS or your main **AAA** stack if you care about snappy loads.

#### Parts list (tower only, indicative BRL)

| Part | Example / spec | Indicative BRL | Notes |
| ---- | -------------- | -------------- | ----- |
| **Case** | **Mesh** front, **2–3 PWM** fans | R$ 350 – R$ 750 | Airflow beats RGB for thermals when you add a **dGPU**. |
| **CPU** | **Ryzen 7 8700G** or **Ryzen 5 8600G** | R$ 1.600 – R$ 2.400 | **780M** vs **760M** iGPU; see **APU table** below. |
| **CPU cooler** | **Tower** if the stock cooler is loud/hot | R$ 180 – R$ 450 | Optional but nice for long **APU** sessions. |
| **HDD** | **4 TB**, **7200 RPM**, **CMR** when possible (**WD Red Plus**, **IronWolf**-class) | R$ 520 – R$ 850 | **Torrents**, **backup**, **media**, chill games. **8 TB** (~R$ 1.150–1.900) if you need more archive on the same idea. |
| **Motherboard** | **B650** with **Wi‑Fi 6/6E + Bluetooth** onboard (**PCIe x16** free, **HDMI/DP** for **APU**) | R$ 1.100 – R$ 1.900 | Skip separate **Wi‑Fi** cards: pick a board that already has **wireless**. **Examples** (check current revision/stock): **ASUS TUF Gaming B650-PLUS WiFi** / **B650M-PLUS WiFi**, **MSI MAG B650 Tomahawk WiFi**, **Gigabyte B650 AORUS ELITE AX**, **ASRock B650 Steel Legend WiFi**—all common **AM5** options with **integrated Wi‑Fi + BT** and **rear antennas** in the box. Confirm **SATA** + **M.2** count for **SSD + HDD**. |
| **PSU** | **750 W**, **80+ Gold**, **fully modular**, **tier-A** design (e.g. **Seasonic Focus GX**, **Corsair RM750e** / **RMx**, **be quiet! Straight Power**) | R$ 650 – R$ 1.050 | **Do not cheap out**—a bad PSU kills drives and GPUs. **750 W Gold** leaves headroom for a **strong single GPU** without swapping the unit. |
| **RAM** | **32 GB DDR5** (2×16), **~6000 MT/s** if stable | R$ 500 – R$ 800 | **16 GB** is a tight floor; **32 GB** is the target here. |
| **SSD** | **1 TB NVMe PCIe 4.0** | R$ 450 – R$ 780 | **Only** fast drive—OS + demanding games. |

**Rough tower total (no GPU, no monitor, no peripherals):** about **R$ 6.200 – R$ 9.500** with **1 SSD + 1 HDD**, **Wi‑Fi** **motherboard**, and a **solid** PSU—depends on sales and **8600G** vs **8700G**.

#### Cables and small extras (often bought separately)

The case, board, and PSU include **a lot**, but builds still stall on missing **bits**—or on **one** **scratched** / **lost** small part. Budget these **in addition** to the parts table if needed.

| Item | Why you might need it | Indicative BRL |
| ---- | -------------------- | -------------- |
| **Display cable** | **Motherboard** video out (then later **GPU**) → monitor. Match **port** (**DP** vs **HDMI**) and **length**. For **1080p 144 Hz**, **1440p**, or **ultrawide**, use a **rated** **DisplayPort 1.4** or **HDMI 2.0/2.1** cable if the **in-box** lead is too short or flaky. | R$ 40 – R$ 150 |
| **Ethernet patch** (**Cat6**) | **Router** → PC for **low latency** or **big** downloads even when **Wi‑Fi** exists. | R$ 25 – R$ 90 |
| **Isopropyl 99% + microfiber** | Clean **CPU** / **cold plate** if you **scratch** paste or need a **redo**. | R$ 25 – R$ 55 |
| **M.2** screw / standoff kit | **Motherboard** trays sometimes ship with **one** combo—easy to **drop** or **strip**; a cheap **universal M.2** hardware kit saves a trip. | R$ 20 – R$ 60 |
| **PWM fan splitter / hub** | Not enough **CHA_FAN** headers for **2–3** case fans. | R$ 35 – R$ 120 |
| **SATA data cable** | **HDD** → motherboard. Boards usually ship **1–2**—**verify in the box**; buy **spares** if you **lose** one or **damage** a latch (**straight** **6 Gb/s** **SATA**). | R$ 15 – R$ 45 (each) |
| **Spare SATA cable** | Second cable in the drawer if the first gets **kinked** / **stripped** during routing. | R$ 15 – R$ 45 |
| **Surge strip / filter** | Stable mains for **PSU** + monitor + peripherals. | R$ 80 – R$ 220 |
| **Thermal paste** | **Tower** cooler needs a fresh **pea**; **extra tube** helps if you **smear** the first try. | R$ 30 – R$ 90 |

**Usually included with PSU / board (no separate buy):** **IEC** power cord, **SATA power** pigtails from the **PSU** for the **HDD**, **M.2** fastener on the **board** (still buy the **spare kit** above if you lose it), **EPS** and **PCIe** **6+2** modular leads for a future **GPU**.

### While you use only the APU (no discrete GPU yet)

| Topic | **8700G (780M)** | **8600G (760M)** |
| ----- | ---------------- | ---------------- |
| **Desktop & video** | **4K** desktop, **YouTube**, **local / torrent** playback in **VLC** (codec-dependent). | Same; slightly less headroom under load. |
| **Game resolution** | **1080p** comfort for **3D**; **1440p** great for **2D** / light **3D**; **4K gaming** not realistic on iGPU. | **1080p** for most **3D**; **1440p** mostly **2D** / desktop. |
| **2D (easy)** | **Stardew**, **Hollow Knight**, **Celeste**, **Dead Cells**, **Slay the Spire**, **visual novels**, etc.—high **fps** at **1080p**, often **1440p**. | Same; occasional **1440p** cap on heavier **2D**. |
| **3D (playable)** | **Fortnite** / **Rocket League** / **Apex**-style: **1080p** **low–medium** ~**60 fps**; **Minecraft** **1080p** sane mods; older **AAA** **1080p** **medium**. | One notch harsher than **8700G**. |
| **3D (heavy AAA)** | **Cyberpunk** / **Alan Wake 2**-class: **very low** or wait for a **GPU**. | Plan **GPU** sooner. |

**Rule of thumb:** **2D** → almost always **yes** at **1080p**. **Modern AAA 3D** → **low** settings or add a **card** (see **[Discrete GPU upgrades](#discrete-gpu-upgrades)**).

### Peripherals and desk

Everything **outside** the case: display, input, audio. **Networking** is handled by **Wi‑Fi + Bluetooth** on the **motherboard**—screw the **rear antennas** on and route them **above** the **I/O** so they are not **flush** against a **wall**.

#### Monitors (standard vs ultrawide)

| Style | Example / spec | Indicative BRL | Notes |
| ----- | -------------- | -------------- | ----- |
| **Budget ultrawide** | **29–34″**, **2560×1080**, **75–144 Hz** | R$ 1.200 – R$ 2.200 | Wider **field of view** without **3440×1440** **GPU** load; still **plan** a **dGPU** for **new** **AAA**. |
| **Standard 1080p** | **24–27″**, **IPS**, **144 Hz**, **1080p** | R$ 850 – R$ 1.400 | Best **match** for **APU** **3D**; **competitive** **FPS** sweet spot. |
| **Standard 1440p** | **27″**, **IPS** / **VA**, **144–180 Hz**, **1440p** | R$ 1.400 – R$ 2.400 | **2D** and desktop heaven on **APU**; **AAA 3D** wants a **dGPU** for **high** settings. |
| **Ultrawide 21:9** | **34″**, **3440×1440**, **144 Hz** (**IPS** / **VA**) | R$ 2.200 – R$ 4.500 | **Movies** and **sim** / **strategy** immersion; **APU** only for **desktop** + **light** games—**serious** **UW** **gaming** assumes a **dGPU**. |

Use a **DisplayPort** cable that matches **bandwidth** (**DP 1.4** typical for **high Hz** **1440p** / **UW**).

#### Keyboard, mouse, mousepad, audio

| Piece | Example / spec | Indicative BRL | Notes |
| ----- | -------------- | -------------- | ----- |
| **Headset or speakers** | **Closed** headset (**HyperX Cloud**, **SteelSeries Arctis**) vs **2.0** speakers (**Edifier R1280DB**-class) | R$ 250 – R$ 900 | **Mic** on headset vs **desktop** **USB** mic for **Discord**. |
| **Keyboard** | **Mechanical** entry (**Redragon**, **HyperX**) or mid (**Keychron**, **Logitech G**), **ABNT2** if you want **Ç** printed | R$ 180 – R$ 700 | Hot-swap boards cost more but are easier to **fix** if a **switch** dies. |
| **Mouse (good pick)** | **Logitech G Pro X Superlight 2** (light **esports**), **Razer DeathAdder V3** / **Viper V3** (ergo / ambi), **Glorious Model O 2** (light, wired **or** **wireless**) | R$ 350 – R$ 900 | **Sensor** (**PixArt**-class), **wireless** **2.4 GHz** dongle, **PTFE** feet; wired saves money (**G502 X**, **DeathAdder V3** wired ~**R$ 250–450**). |
| **Mousepad** | **Large** cloth (**SteelSeries QcK Large** / **XXL**), **Logitech G640**, or **desk**-sized **900×400 mm** generic **stitched** pad | R$ 90 – R$ 280 | **Low** **DPI** **flick** needs **room**; **fast** **pads** (**hard** / **hybrid**) are taste—start **control**-biased **cloth**. |

### Discrete GPU upgrades

After you install a **video card**, plug the **monitor** into the **GPU**, install **NVIDIA** or **AMD** drivers, and use this as a **planning** guide. **BRL** swings wildly—compare **tiers**, not exact reais.

| Tier | Example cards | Indicative BRL | **Resolution / refresh** target | Games (roughly) |
| ---- | -------------- | -------------- | --------------------------------- | ---------------- |
| **Entry** | **RTX 4060**, **RX 7600** | R$ 1.800 – R$ 2.800 | **1080p** **high/ultra** **60–144 Hz**; **1440p** with **medium** / **FSR/DLSS** | **Esports** maxed **1080p**; **AAA** **1080p** **high** ~**60 fps** with tweaks. |
| **Upper entry** | **RTX 4060 Ti**, **RX 7700 XT** | R$ 2.500 – R$ 3.800 | **1440p** **high** **60–100 Hz** | **AAA** **1440p** **high/ultra** mix; **4K** only lighter titles without heavy upscaling. |
| **Mid** | **RTX 4070** / **4070 SUPER**, **RX 7800 XT** | R$ 3.500 – R$ 5.500 | **1440p** **high/ultra** or **high refresh** + **DLSS/FSR** | **Cyberpunk**-class **1440p** **playable**; **4K** **medium/high** some games. |
| **High** | **RTX 4080 SUPER**, **RX 7900 XT** | R$ 6.000 – R$ 9.000+ | **4K** **60–120 Hz** or **1440p** **240 Hz** **esports** | **Near-max** **AAA** **4K** with upscaling; some **RT** modes **1440p**. |
| **Enthusiast** | **RTX 4090**-class | R$ 10.000+ | **4K** **high refresh**; **VR** | Strongest consumer **4K** / **RT** envelope. |

**Read it with your monitor:** **1080p 60 Hz** pairs with **Entry**; **4K** **AAA** wants **Mid** or **High**. Your **750 W Gold** PSU should cover these **single-GPU** tiers—double-check the **card’s** **power** recommendation and **12VHPWR** / **PCIe** cable kit.
