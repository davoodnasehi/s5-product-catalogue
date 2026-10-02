# RotaMon
*Fixed plant · Condition monitoring · LoRaWAN*

> A multi-parameter condition-monitoring node that hears a machine begin to fail before it starts to vibrate.

**Status:** Pilot programme — open

---

## 01. The problem

A bearing does not fail suddenly. A defect begins as a microscopic irregularity on a raceway, generates a shock pulse once per rotation, and grows over weeks into spalling, heat and finally seizure. The evidence of that progression exists from very early on — but almost all of it sits in the *high-frequency and acoustic* bands, and that is exactly where most monitoring misses it.

Two common approaches both see the machine too late. A monthly handheld route observes a machine for around twenty minutes a month. Vibration-only wireless sensors need the defect to be energetic enough to register in the acceleration spectrum — and by then the failure is close. Acoustic energy, which is the earliest and cleanest indicator, is usually the last thing measured.

On a remote site, the cost of that gap is measured in production hours, not repair hours: an unplanned conveyor-drive or mill-motor stoppage takes a crew, a crane and a shutdown window with it.

## 02. How it works, in plain language

RotaMon is a 30 × 20 × 7 mm battery node in an IP68 enclosure. It carries a 9-axis inertial measurement unit, a temperature sensor, a wideband vibration element and a microphone.

The microphone is the point. When metal begins to defect it rings at frequencies far above anything the machine's normal rotation produces. RotaMon samples that acoustic band, extracts a small set of features *on the device itself*, and runs an onboard inference model — it does not stream raw waveforms to the cloud. When the acoustic signature drifts away from the machine's learned baseline, the node raises an alert over LoRaWAN before a conventional vibration spectrum shows anything.

The same node also reports temperature and vibration trend, so one device covers the three parameters that matter rather than three separate instruments.

## 03. Key specifications

| Specification | Detail |
|---|---|
| Form factor | 30 × 20 × 7 mm, bracket-mount, IP68 |
| Parameters | Vibration + temperature + acoustic in one node; 9-axis IMU |
| Onboard processing | STM32L-class ultra-low-power MCU; on-device feature extraction and inference |
| Sensing range | 0–150 °C range target — confirmed against your asset's surface temperature during scoping |
| Radio | LoRaWAN; private-network capable; downlink configuration |
| Alerting | Threshold and learned-baseline drift; weekly alert digest during a pilot |

## 04. Where it is used

**Conveyor drive motor and gearbox** — Detect bearing and gear defects acoustically in the window between monthly routes.

**Pump skid** — Catch cavitation and early impeller wear from the acoustic signature before efficiency drops.

**Unstaffed fixed plant** — Report condition from a remote MCC or pump station without sending a technician to it.

## 05. Who this is for

**Suited to:** Reliability and maintenance engineers responsible for fixed plant at mine sites, processing plants, water utilities and heavy manufacturing — where one unplanned stoppage costs more than a year of monitoring.

## 06. Where S5 fits

S5 supplies RotaMon together with functional-safety engineering from S5 Consultants. That matters in a specific, honest way: a sensor is not a safety function, and no sensor carries a SIL rating by itself. What condition-monitoring data *can* support is **diagnostic-coverage evidence** — a defensible claim for the fraction of dangerous failures the monitoring actually detects. That claim is what underpins a proof-test argument: stretching a proof-test interval from 12 months to 24 months roughly doubles PFDavg, so the interval can only move if diagnostic coverage can be evidenced for it.

So the product is the node. The deliverable is the evidence.

## 07. 8-week paid Instrumentation Pilot

The pilot is deliberately narrow, and it is a purchase rather than a survey:

- 2–4 fixed-plant points (conveyor drive, pump skid, LV motor).
- Multi-parameter nodes plus gateway, IP68.
- Eight weeks of data with a weekly alert digest.
- Deliverables: alert-precision report, diagnostic-coverage / proof-test-interval evidence pack (IEC 61511 framing), and a go/no-go recommendation.
- A$4,900 — credited in full to a monitoring retainer signed within 30 days.
- Exit on request: hardware uninstalled, data returned, no obligation.

**[Request the pilot scope](mailto:info@s5system.com?subject=RotaMon%20-%20request%20the%208-week%20Instrumentation%20Pilot%20scope) — one email, no follow-up unless you ask.**

*Scoping is a short call to confirm the asset list and the evidence you need. Nothing is installed until a scope is signed.*

---

## About this page

This page is published as product information, not as a sales approach. S5 does not cold-sell: nothing follows unless you ask for it.

**Who produces this.** S5 System Pty Ltd is a Perth (Western Australia) industrial control-systems and IoT engineering firm. The company's assurance and functional-safety work is led by Davoud Nassehi — PhD (Systems Engineering & Renewable Energy), Certified Functional Safety Expert (CFSE), National Engineering Register (NER), PEng, PMP, MBA.

Product catalogue · generated 2026-10-02 · info@s5system.com
