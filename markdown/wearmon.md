# WearMon
*Mineral processing · Wear liners · Flex-PCB sensing*

> Wear-liner thickness sensing that turns a shutdown-day surprise into a trend line.

**Status:** Pilot programme — open

---

## 01. The problem

Wear liners in chutes, transfer points, bins and mill feed ends are consumables — they are *designed* to be consumed. The hazard is that their remaining thickness cannot be seen from outside. A liner is assessed by looking at it, tapping it, or measuring at a handful of access points during a planned shutdown. Between shutdowns, it wears.

When a liner thins past its limit it can punch through the shell or throw a plate into the process. A planned reline becomes an unplanned shutdown, with a dropped-load hazard attached to it. Relines are therefore usually planned on a *calendar*, because the calendar is the only measurement most sites have.

## 02. How it works, in plain language

WearMon is a thin flexible printed circuit that is fitted to the wear surface — bonded to or sandwiched behind the liner. As the liner wears, the sensing element wears with it, and the electrical signature of that element changes in proportion to how much material remains. A node reports the signature on a schedule, so remaining thickness becomes a trend line instead of a shutdown-day surprise.

> **Note on disclosure.** WearMon's sensing construction is proprietary, and there are third-party patents in the adjacent space. This page deliberately describes the *principle*, not the construction. The detailed sensing mechanism, mounting geometry and accuracy figures are released under NDA with the spec sheet.

## 03. Key specifications

| Specification | Detail |
|---|---|
| Sensing principle | Flex-PCB element that wears with the liner; resistance-change signature |
| Mounting | Between or behind wear plates/liners; ceramic and steel liner compatible (geometry confirmed per site) |
| Reporting | Scheduled remaining-thickness trend; threshold alerting |
| Node | Battery, IP68, LoRaWAN |
| Withheld pending IP clearance | Detailed construction, accuracy and calibration method (released under NDA) |

## 04. Where it is used

**Chute and transfer-point liners** — Trend remaining thickness through the campaign instead of inspecting at shutdown.

**Mill feed and discharge end liners** — Plan relines on measured wear rather than on a fixed calendar.

**Crusher chamber and bucket wear plates** — Add local wear points to the same monitoring install.

## 05. Who this is for

**Suited to:** Mill and processing superintendents, relining crews and maintenance planners who currently plan relines on a calendar and inspect them on a shutdown.

## 06. Where S5 fits

WearMon is offered on the same install visit as RotaMon because it shares the buyer, the site and the evidence pack. Adding liner-thickness points to a condition-monitoring pilot costs no additional channel and produces a second, independent line of evidence about the same plant.

The same functional-safety framing applies: the data supports diagnostic coverage and proof-test planning. It is not a "SIL-rated" product, and it is not sold as one.

## 07. Same pilot, extended scope

WearMon liner points can be added to the 8-week paid Instrumentation Pilot alongside RotaMon:

- Liner-thickness points on the chutes, transfer points or mill ends you nominate.
- Eight weeks of thickness trend with a weekly digest.
- Wear-rate and remaining-campaign estimate in the readout.
- Added to the same A$4,900 pilot, credited in full to a monitoring retainer signed within 30 days.
- Exit on request: hardware removed, data returned, no obligation.

**[Request the pilot scope](mailto:info@s5system.com?subject=WearMon%20-%20request%20the%20liner-thickness%20pilot%20scope) — one email, no follow-up unless you ask.**

*Detailed sensing specifications are provided under NDA once the pilot scope is confirmed.*

---

## About this page

This page is published as product information, not as a sales approach. S5 does not cold-sell: nothing follows unless you ask for it.

**Who produces this.** S5 System Pty Ltd is a Perth (Western Australia) industrial control-systems and IoT engineering firm. The company's assurance and functional-safety work is led by Davoud Nassehi — PhD (Systems Engineering & Renewable Energy), Certified Functional Safety Expert (CFSE), National Engineering Register (NER), PEng, PMP, MBA.

Product catalogue · generated 2026-10-02 · info@s5system.com
