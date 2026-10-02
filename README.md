# S5 System — product catalogue

Static, one-page-per-product catalogue for the S5 stored-product portfolio.
Part of the **Persistent Product Awareness Engine** (Radar §3-H, blueprint
`PRODUCT-MARKETING-ENGINE.md` §3). Zero-cost, permanent, SEO-hosted on GitHub Pages.

**Live:** https://davoodnasehi.github.io/s5-product-catalogue/

## Pages

| Product | Page | Status | CTA |
|---|---|---|---|
| RotaMon | `products/rotamon.html` | Pilot programme — open | 8-week paid Instrumentation Pilot |
| WearMon | `products/wearmon.html` | Pilot programme — open | Same pilot, extended scope |
| GETsmart | `products/getsmart.html` | Awareness | Soft — request the one-pager |
| Genset & lighting-tower telematics | `products/genset-lighting-telematics.html` | Awareness | Soft — request the one-pager |
| Workshop line | `products/workshop-line.html` | Awareness | Soft — request the one-pager |
| Bus passenger-safety mesh | `products/bus-safety-mesh.html` | Awareness | Soft — request the one-pager |
| Smart bolt tension monitor | `products/bolt-tension-monitor.html` | **Held — pending rename** | Soft, but page is noindex + not linked |

`manifest.json` carries the machine-readable list of URLs, triage verdicts and
promotion status for each page.

## The seven products

1. **RotaMon** — 30 × 20 × 7 mm LoRaWAN multi-parameter node (vibration + temperature
   + acoustic, 9-axis IMU, STM32L, on-device ML). Triage verdict: **PILOT NOW #1**.
2. **WearMon** — flex-PCB wear-liner / wear-plate thickness sensing.
   Triage verdict: **PILOT NOW #2**.
3. **GETsmart** — embedded GET dislodgement + left-behind drill-rod detection ahead
   of the crusher. Triage verdict: **WATCH**.
4. **Smart bolt tension monitor** — load-sensing washers for continuous bolt-tension
   measurement. Triage verdict: **WATCH + mandatory rebrand**.
5. **Genset / lighting-plant telematics** — non-invasive fuel level + light intensity
   + GNSS for mobile assets. Triage verdict: **PARK**.
6. **Workshop line** — jack oil-hours, car-wash chemical levels, hoist safety-pin
   interlock. Triage verdict: **KIT CANDIDATE**.
7. **Bus passenger-safety mesh** — BLE mesh for seatbelt, door, smoke/fire and
   driver-attention monitoring. Triage verdict: **PARK**.

## Editorial rules applied

- **Pull-only tone.** Educational, credential-led, no hype, no cold-sell language.
  One CTA per page; the footer states that nothing follows unless the reader asks.
- **Two CTA tiers only.** RotaMon and WearMon (the two triage winners) carry the
  A$4,900 8-week paid Instrumentation Pilot CTA. Every other line carries a soft
  "request the one-pager / spec sheet" email capture, because their triage verdicts
  are WATCH, PARK or KIT — awareness only until a G1-equivalent threshold is met.
- **Flagship positioning.** Pages sell diagnostic-coverage / proof-test-interval
  evidence. They never describe a product as a "SIL-rated sensor": SIL attaches to a
  safety function, not to a device.
- **Honest positioning.** PARK and KIT lines state plainly where they sit next to the
  incumbents rather than implying they are best-in-class.

## Brand-safety hold on the bolt-tension line

The bolt-tension product's previous working name conflicts with a trademark held by
another company in the fastening industry. Therefore:

- the page uses the working title **"Smart Bolt Tension Monitor — name pending owner
  decision"**;
- the page is `noindex, nofollow`;
- it is disallowed in `robots.txt`;
- it is **not linked** from `index.html`;
- the old name appears nowhere in this repository.

It moves into the public catalogue once the owner approves a replacement name.

## WearMon IP note

WearMon's public copy describes the sensing *principle* only. The construction,
geometry and accuracy figures are withheld pending an IP-clearance check against
third-party patents in the adjacent space, and are released under NDA.

## Source of truth

- `C:/Users/DN/s5-radar/PRODUCT-MARKETING-ENGINE.md` — asset plan, channel map
- `C:/Users/DN/s5-radar/PRODUCT-TRIAGE.md` — per-product verdicts
- `C:/Users/DN/s5-radar/OPPORTUNITY-RADAR.md` §3-A (flagship positioning), §3-H (engine)

## Rebuilding

The generator is `build_catalogue.py` (kept in the working folder). Edit the product
definitions and re-run; it writes `index.html`, `products/*.html`, `markdown/*.md`,
`assets/style.css`, `sitemap.xml`, `robots.txt` and `manifest.json`.

## Images

`assets/*_hero.png` are placeholder 3D renders, chosen so each page has a visual
frame now. They are replaced with real product photography after the owner's storage
photo session. All current renders were checked to be free of third-party branding
and readable text.

## Contact

info@s5system.com
