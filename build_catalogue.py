#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Generate the S5 product catalogue one-pagers + index + manifest.

Output root: C:/Users/DN/s5-product-catalogue  (git repo root, GitHub Pages)
Sources of truth: s5-radar/PRODUCT-MARKETING-ENGINE.md, PRODUCT-TRIAGE.md,
OPPORTUNITY-RADAR.md 3-A / 3-H.
"""
import os, json, shutil, html, re
from datetime import datetime, timezone

REPO = r"C:/Users/DN/s5-product-catalogue"
WS = r"C:/Users/DN/AppData/Local/hermes/kanban/workspaces/t_f0fb9535/catalogue"
ASSETS_SRC = os.path.join(WS, "assets")
ASSETS_DST = os.path.join(REPO, "assets")
PROD_DST = os.path.join(REPO, "products")
MD_DST = os.path.join(REPO, "markdown")

BRAND = "S5 System Pty Ltd"
EMAIL = "info@s5system.com"
BASE_URL = "https://davoodnasehi.github.io/s5-product-catalogue/"
GEN_DATE = "2026-10-02"

AUTHOR_BIO = (
    "S5 System Pty Ltd is a Perth (Western Australia) industrial control-systems and IoT engineering firm. "
    "The company's assurance and functional-safety work is led by Davoud Nassehi — "
    "PhD (Systems Engineering &amp; Renewable Energy), Certified Functional Safety Expert (CFSE), "
    "National Engineering Register (NER), PEng, PMP, MBA."
)

PULL_NOTE = (
    "This page is published as product information, not as a sales approach. "
    "S5 does not cold-sell: nothing follows unless you ask for it."
)

MIRROR = "https://davoodnasehi.github.io/s5-product-catalogue"

LIVE_NOW_MD = """# Live

The catalogue is published on GitHub Pages. Every page below returns HTTP 200:

| What | URL |
|---|---|
| Catalogue index | {b}/ |
| RotaMon | {b}/products/rotamon.html |
| WearMon | {b}/products/wearmon.html |
| GETsmart | {b}/products/getsmart.html |
| Genset & lighting telematics | {b}/products/genset-lighting-telematics.html |
| Workshop line | {b}/products/workshop-line.html |
| Bus safety mesh | {b}/products/bus-safety-mesh.html |
| Bolt-tension (held) | {b}/products/bolt-tension-monitor.html |
| Manifest | {b}/manifest.json |
| Sitemap | {b}/sitemap.xml |

Browsable repo: https://github.com/davoodnasehi/s5-product-catalogue

An earlier handover reported the Pages CDN answering `404 Site not found` for this
account. That was a wrong hostname: the checks used `davoodnass**e**hi.github.io`
(double-s) instead of the account handle `davoodnasehi`. The correct Pages host has
been serving since the first deploy.

`mining-iot.com/products/` and `s5system.com/products/` stay available as an optional
branded-domain mirror later; no WordPress upload is required for the catalogue to be live.
""".format(b=BASE_URL.rstrip("/"))

# ---------------------------------------------------------------- products ---

# Content lives in per-product functions below; the page definitions follow.

def _rotamon():
    return dict(
        problem="""
        <p>A bearing does not fail suddenly. A defect begins as a microscopic irregularity on a raceway,
        generates a shock pulse once per rotation, and grows over weeks into spalling, heat and finally
        seizure. The evidence of that progression exists from very early on &mdash; but almost all of it sits
        in the <em>high-frequency and acoustic</em> bands, and that is exactly where most monitoring misses it.</p>
        <p>Two common approaches both see the machine too late. A monthly handheld route observes a machine for
        around twenty minutes a month. Vibration-only wireless sensors need the defect to be energetic enough
        to register in the acceleration spectrum &mdash; and by then the failure is close. Acoustic energy, which is
        the earliest and cleanest indicator, is usually the last thing measured.</p>
        <p>On a remote site, the cost of that gap is measured in production hours, not repair hours: an unplanned
        conveyor-drive or mill-motor stoppage takes a crew, a crane and a shutdown window with it.</p>
        """,
        physics="""
        <p>RotaMon is a 30 &times; 20 &times; 7&nbsp;mm battery node in an IP68 enclosure. It carries a 9-axis
        inertial measurement unit, a temperature sensor, a wideband vibration element and a microphone.</p>
        <p>The microphone is the point. When metal begins to defect it rings at frequencies far above anything the
        machine's normal rotation produces. RotaMon samples that acoustic band, extracts a small set of features
        <em>on the device itself</em>, and runs an onboard inference model &mdash; it does not stream raw waveforms
        to the cloud. When the acoustic signature drifts away from the machine's learned baseline, the node raises
        an alert over LoRaWAN before a conventional vibration spectrum shows anything.</p>
        <p>The same node also reports temperature and vibration trend, so one device covers the three parameters
        that matter rather than three separate instruments.</p>
        """,
        specs=[
            ("Form factor", "30 &times; 20 &times; 7&nbsp;mm, bracket-mount, IP68"),
            ("Parameters", "Vibration + temperature + acoustic in one node; 9-axis IMU"),
            ("Onboard processing", "STM32L-class ultra-low-power MCU; on-device feature extraction and inference"),
            ("Sensing range", "0&ndash;150&nbsp;&deg;C range target &mdash; confirmed against your asset's surface temperature during scoping"),
            ("Radio", "LoRaWAN; private-network capable; downlink configuration"),
            ("Alerting", "Threshold and learned-baseline drift; weekly alert digest during a pilot"),
        ],
        use_cases=[
            ("Conveyor drive motor and gearbox",
             "Detect bearing and gear defects acoustically in the window between monthly routes."),
            ("Pump skid",
             "Catch cavitation and early impeller wear from the acoustic signature before efficiency drops."),
            ("Unstaffed fixed plant",
             "Report condition from a remote MCC or pump station without sending a technician to it."),
        ],
        who="Reliability and maintenance engineers responsible for fixed plant at mine sites, processing plants, water utilities and heavy manufacturing &mdash; where one unplanned stoppage costs more than a year of monitoring.",
        difference="""
        <p>S5 supplies RotaMon together with functional-safety engineering from S5 Consultants. That matters in a
        specific, honest way: a sensor is not a safety function, and no sensor carries a SIL rating by itself.
        What condition-monitoring data <em>can</em> support is <strong>diagnostic-coverage evidence</strong> &mdash; a
        defensible claim for the fraction of dangerous failures the monitoring actually detects. That claim is what
        underpins a proof-test argument: stretching a proof-test interval from 12 months to 24 months roughly
        doubles PFD<sub>avg</sub>, so the interval can only move if diagnostic coverage can be evidenced for it.</p>
        <p>So the product is the node. The deliverable is the evidence.</p>
        """,
        cta_heading="8-week paid Instrumentation Pilot",
        cta_body="""
        <p>The pilot is deliberately narrow, and it is a purchase rather than a survey:</p>
        <ul>
          <li>2&ndash;4 fixed-plant points (conveyor drive, pump skid, LV motor).</li>
          <li>Multi-parameter nodes plus gateway, IP68.</li>
          <li>Eight weeks of data with a weekly alert digest.</li>
          <li>Deliverables: alert-precision report, diagnostic-coverage / proof-test-interval evidence pack
              (IEC&nbsp;61511 framing), and a go/no-go recommendation.</li>
          <li>A$4,900 &mdash; credited in full to a monitoring retainer signed within 30&nbsp;days.</li>
          <li>Exit on request: hardware uninstalled, data returned, no obligation.</li>
        </ul>
        """,
        cta_label="Request the pilot scope",
        cta_subject="RotaMon - request the 8-week Instrumentation Pilot scope",
        cta_fine="Scoping is a short call to confirm the asset list and the evidence you need. Nothing is installed until a scope is signed.",
    )

def _wearmon():
    return dict(
        problem="""
        <p>Wear liners in chutes, transfer points, bins and mill feed ends are consumables &mdash; they are
        <em>designed</em> to be consumed. The hazard is that their remaining thickness cannot be seen from outside.
        A liner is assessed by looking at it, tapping it, or measuring at a handful of access points during a
        planned shutdown. Between shutdowns, it wears.</p>
        <p>When a liner thins past its limit it can punch through the shell or throw a plate into the process.
        A planned reline becomes an unplanned shutdown, with a dropped-load hazard attached to it. Relines are
        therefore usually planned on a <em>calendar</em>, because the calendar is the only measurement most sites
        have.</p>
        """,
        physics="""
        <p>WearMon is a thin flexible printed circuit that is fitted to the wear surface &mdash; bonded to or
        sandwiched behind the liner. As the liner wears, the sensing element wears with it, and the electrical
        signature of that element changes in proportion to how much material remains. A node reports the signature
        on a schedule, so remaining thickness becomes a trend line instead of a shutdown-day surprise.</p>
        <p class="callout"><strong>Note on disclosure.</strong> WearMon&rsquo;s sensing construction is proprietary, and
        there are third-party patents in the adjacent space. This page deliberately describes the
        <em>principle</em>, not the construction. The detailed sensing mechanism, mounting geometry and accuracy
        figures are released under NDA with the spec sheet.</p>
        """,
        specs=[
            ("Sensing principle", "Flex-PCB element that wears with the liner; resistance-change signature"),
            ("Mounting", "Between or behind wear plates/liners; ceramic and steel liner compatible (geometry confirmed per site)"),
            ("Reporting", "Scheduled remaining-thickness trend; threshold alerting"),
            ("Node", "Battery, IP68, LoRaWAN"),
            ("Withheld pending IP clearance", "Detailed construction, accuracy and calibration method (released under NDA)"),
        ],
        use_cases=[
            ("Chute and transfer-point liners",
             "Trend remaining thickness through the campaign instead of inspecting at shutdown."),
            ("Mill feed and discharge end liners",
             "Plan relines on measured wear rather than on a fixed calendar."),
            ("Crusher chamber and bucket wear plates",
             "Add local wear points to the same monitoring install."),
        ],
        who="Mill and processing superintendents, relining crews and maintenance planners who currently plan relines on a calendar and inspect them on a shutdown.",
        difference="""
        <p>WearMon is offered on the same install visit as RotaMon because it shares the buyer, the site and the
        evidence pack. Adding liner-thickness points to a condition-monitoring pilot costs no additional channel
        and produces a second, independent line of evidence about the same plant.</p>
        <p>The same functional-safety framing applies: the data supports diagnostic coverage and proof-test
        planning. It is not a &ldquo;SIL-rated&rdquo; product, and it is not sold as one.</p>
        """,
        cta_heading="Same pilot, extended scope",
        cta_body="""
        <p>WearMon liner points can be added to the 8-week paid Instrumentation Pilot alongside RotaMon:</p>
        <ul>
          <li>Liner-thickness points on the chutes, transfer points or mill ends you nominate.</li>
          <li>Eight weeks of thickness trend with a weekly digest.</li>
          <li>Wear-rate and remaining-campaign estimate in the readout.</li>
          <li>Added to the same A$4,900 pilot, credited in full to a monitoring retainer signed within 30&nbsp;days.</li>
          <li>Exit on request: hardware removed, data returned, no obligation.</li>
        </ul>
        """,
        cta_label="Request the pilot scope",
        cta_subject="WearMon - request the liner-thickness pilot scope",
        cta_fine="Detailed sensing specifications are provided under NDA once the pilot scope is confirmed.",
    )

def _getsmart():
    return dict(
        problem="""
        <p>Two objects arrive at a crusher that were never meant to be there: a ground-engaging-tool (GET) tooth
        that has fallen off a bucket, and the drill rod or bit left behind on a bench after firing. By the time
        either reaches the crushing chamber the damage is already happening &mdash; a stalled or damaged crusher,
        a broken spider arm, and in the drill-rod case, a live hazard to anyone who inspects downstream.</p>
        <p>Industry reporting attributes the large majority of damaging tramp-metal incidents to lost drill rods
        and bits, and crusher events routinely cost millions. Yet the common detection method &mdash; a magnet or
        metal detector in the feed path &mdash; sits <em>downstream of the point of loss</em>, which is late by
        definition: the tool was already lost somewhere up the chain.</p>
        """,
        physics="""
        <p>GETsmart embeds a small sensor in the GET itself, and a matching element on the drill-string side of
        the operation. Each unit reports presence or absence over a wireless link.</p>
        <p>In plain language: the tool tells you it is gone, instead of waiting for the crusher to tell you. When a
        tooth leaves its adapter, or a rod does not come back, the system knows &mdash; and it can be arranged to
        alarm, or to interlock, ahead of the crusher rather than behind it.</p>
        """,
        specs=[
            ("Sensing point", "Embedded in the GET / adapter; separate element for the drill-string side"),
            ("Telemetry", "Wireless presence reporting; site range confirmed per installation"),
            ("Output", "Alarm or crusher-protection interlock interface"),
            ("Power", "Battery, sealed for mining duty"),
            ("Status", "Awareness stage &mdash; detailed specifications are released with commercial partners"),
        ],
        use_cases=[
            ("Bucket GET tooth loss",
             "Detect a tooth leaving its adapter at the face or load-out, before it reaches the tip head."),
            ("Left-behind drill rods and bits",
             "Confirm every rod and bit has come back before the bench is mucked to the crusher."),
            ("Crusher feed-point protection",
             "Provide a pre-crusher alarm or interlock rather than relying on a downstream magnet."),
        ],
        who="Quarry managers, mining contractors and fixed-plant superintendents who fund crusher repairs and carry the tramp-metal risk.",
        difference="""
        <p>GETsmart is currently developed as a partner line. Getting sensors into GET consumables means working
        with the GET vendors who supply them, and that is the route S5 plans to take &mdash; as a white-label or
        embedded arrangement rather than a competing brand on the shelf.</p>
        <p>This page is published at awareness level. There is no conversion offer on GETsmart at this stage.</p>
        """,
        cta_heading="Spec sheet on request",
        cta_body="""
        <p>GETsmart is at awareness stage. If you are a GET vendor, contractor or site that wants the technical
        detail, ask for the one-pager and we will send the current specification, including what is and is not
        yet proven in the field.</p>
        """,
        cta_label="Request the GETsmart one-pager",
        cta_subject="GETsmart - request the product one-pager",
        cta_fine="No sales follow-up unless you ask for it.",
    )

def _bolt():
    return dict(
        held=True,
        problem="""
        <p>A bolted connection is designed to hold a clamp load. Over time that clamp load is lost &mdash; through
        creep, relaxation, vibration, corrosion and thermal cycling &mdash; while the bolt still looks tight.
        A bridge, tower, crane or structural connection can be sitting at a fraction of its design preload and
        look entirely normal to a visual inspection.</p>
        <p>Torque-wrench inspection measures friction, not tension, so it answers the wrong question. Tapping with
        a hammer is a judgement call. Which is why large numbers of deficient connections on ageing structures go
        for years without a credible measurement: the only reliable methods require access and downtime.</p>
        """,
        physics="""
        <p>A washer that sits under the bolt head or nut is instrumented so that its compression &mdash; the clamp
        load itself &mdash; changes a measurable electrical property. Instead of inferring tension from torque,
        the washer measures load directly.</p>
        <p>A wireless node reports the trend over time, and when preload falls below a set threshold the
        connection flags itself. In plain language: measure the tension, not the tightness.</p>
        """,
        specs=[
            ("Sensing element", "Load-sensing washer fitted under a standard bolt head or nut"),
            ("Measurement", "Direct clamp-load / bolt-tension measurement, temperature compensated"),
            ("Radio", "Wireless reporting; LoRaWAN-capable"),
            ("Output", "Tension trend plus threshold alarms"),
            ("Retrofit", "Designed as a drop-in replacement for the existing washer stack"),
            ("Published on rename", "Sizes, accuracy figures and environmental ratings"),
        ],
        use_cases=[
            ("Bridge and structural steel connections",
             "Continuously verify preload on connections under inspection regimes, without access and torque-wrench windows."),
            ("Transmission towers and crane / rigging connections",
             "Monitor connections that are hard to reach and expensive to shut down."),
            ("Rotating equipment foundations and flanges",
             "Track preload loss caused by vibration and thermal cycling on heavy static plant."),
        ],
        who="Structural engineers, structural-health-monitoring consultancies and asset owners responsible for bolted connections on bridges, towers, cranes and heavy static plant.",
        market="""
        <p>Context, for engineers assessing the category rather than the product: the structural-health-monitoring
        market is estimated at US$3.6&ndash;8.9&nbsp;billion in 2026 with 13&ndash;19% annual growth. The US National
        Bridge Inspection Standards update phases through 2026 against a backdrop of 42,000+ deficient bridges and
        US$40&nbsp;billion of BIL funding, and the FHWA requires direct-tension indicators on federally funded bridge
        connections. EU TEN-T monitoring mandates apply to the network. Meanwhile, several vendors already sell
        retrofit bolt-tension sensing &mdash; this is an established category, not an empty one.</p>
        """,
        difference="""
        <p>Naming note: this product previously carried a working name that conflicts with a trademark held by
        another company in the fastening industry. It therefore has <strong>no public name, and is held from all
        promotion</strong> until the owner approves a replacement.</p>
        """,
        cta_heading="One-pager on request",
        cta_body="""
        <p>This line is published for reference while its name is being settled. Ask for the one-pager and we will
        send the technical description; the spec sheet follows once the name is confirmed.</p>
        """,
        cta_label="Request the one-pager",
        cta_subject="Bolt-tension monitor (name pending) - request the one-pager",
        cta_fine="Held from public promotion until the product name is confirmed.",
    )

def _genset():
    return dict(
        problem="""
        <p>Plant-hire and remote-site operators run generators and lighting towers as dispersed assets. Three
        questions recur, and the usual way to answer them is to send someone out:</p>
        <ul>
          <li>Is the unit where the paperwork says it is?</li>
          <li>How much fuel is left &mdash; and is it being used, or leaking?</li>
          <li>Is the light actually on?</li>
        </ul>
        <p>A genset that runs dry, is stolen, or is left burning on a completed site is a direct, avoidable cost.
        On a hire fleet, so is a unit that is on hire but idle.</p>
        """,
        physics="""
        <p>Three sensors, one device. A non-invasive clamp-on probe reads fuel level through the tank wall. A light
        sensor on the lamp head reads whether the tower is lit and at what intensity. A GNSS receiver reports
        position and movement.</p>
        <p>&ldquo;Non-invasive&rdquo; is the important word for a hire fleet: nothing is plumbed into the fuel
        line, so a unit can be fitted and removed without touching the asset or voiding its service history.</p>
        """,
        specs=[
            ("Fuel", "Non-invasive clamp-on level sensing &mdash; no connection to the fuel line"),
            ("Light", "Intensity sensing at the lamp head; lamp-out detection"),
            ("Position", "GNSS position with geo-fence and movement alerts"),
            ("Power", "Mobile-asset supply"),
            ("Reporting", "Wireless; low-fuel, movement and lamp-out alerting"),
        ],
        use_cases=[
            ("Hire-fleet location and utilisation",
             "Confirm where every unit is, and whether it is actually working."),
            ("Fuel monitoring",
             "Detect draining, leaks and low-level events before they stop the job."),
            ("Lighting compliance",
             "Prove a tower was lit when it was supposed to be, without sending an inspector."),
        ],
        who="Plant-hire fleets and remote-site operators managing mobile generators, lighting towers and similar dispersed assets.",
        honest="""
        <p>Stated plainly: this market is well served. Generator controllers from Deep Sea and ComAp ship remote
        monitoring as a standard feature, and hire fleets standardise on existing telematics platforms. S5
        publishes this line as part of its stored-product portfolio at <strong>awareness level only</strong>; there
        is no conversion programme attached to it and no claim that it beats a purpose-built fleet-telematics
        product.</p>
        """,
        cta_heading="One-pager on request",
        cta_body="""
        <p>Ask for the genset and lighting-tower telematics one-pager and we will send the current specification
        and the honest version of where this line fits next to the telematics you already run.</p>
        """,
        cta_label="Request the telematics one-pager",
        cta_subject="Genset / lighting-tower telematics - request the one-pager",
        cta_fine="No sales follow-up unless you ask for it.",
    )

def _workshop():
    return dict(
        problem="""
        <p>Three small jobs in a workshop that are done from memory &mdash; and that fail, eventually, from memory:</p>
        <ul>
          <li>Waste-oil and service jacks have a service life measured in running hours, tracked on a whiteboard
              if it is tracked at all.</li>
          <li>Car-wash chemical dosing tanks run dry mid-shift, stopping the line until somebody notices.</li>
          <li>Vehicle hoists can be raised while resting on their safety pins. AS&nbsp;2550 requires daily
              pre-operation checks and WorkSafe has issued alerts on hoist incidents, but the check is a procedure
              performed by a person under time pressure.</li>
        </ul>
        """,
        physics="""
        <p>Each problem has a small sensing answer. A run-hour counter on the jack. A level probe or float in the
        chemical tank. An interlock that detects the hoist resting on its pins and prevents the raise control from
        operating until the hoist is clear. Each reports to a simple dashboard, an alert, or both.</p>
        """,
        specs=[
            ("Jack oil-hours", "Run-hour counting on waste-oil / service jacks for service scheduling"),
            ("Car-wash chemicals", "Level probe or float in the dosing tank with low-level alerting"),
            ("Hoist interlock", "Safety-pin presence detection that inhibits the raise control"),
            ("Power", "Low-power, workshop-safe; retrofit to existing equipment"),
            ("Alerting", "App or SMS notification"),
        ],
        use_cases=[
            ("Waste-oil jack servicing",
             "Schedule oil changes on measured running hours instead of a rough calendar."),
            ("Car-wash chemical top-up",
             "Get an alert before the dosing tank empties, not after the bay stops."),
            ("Hoist pre-operation interlock",
             "Make the daily check mechanical rather than procedural."),
        ],
        who="Automotive workshops, detailers and small fleet operators &mdash; including SMBs who want a low-cost kit rather than an engineering project.",
        honest="""
        <p>This line is being developed as a retail kit rather than an engineering engagement. Packaging, pricing
        and the kit contents are not finalised, and any consumer-facing device supplied in Australia must carry a
        statement of compliance under the Smart Device Security Rules. S5 publishes this line at awareness level;
        there is no order path yet.</p>
        """,
        cta_heading="One-pager on request",
        cta_body="""
        <p>Ask for the workshop line one-pager and we will send the concept specification for the jack
        oil-hours sensor, the car-wash level sensor and the hoist interlock &mdash; plus what is still open.</p>
        """,
        cta_label="Request the workshop kit one-pager",
        cta_subject="Workshop line (jack / car-wash / hoist interlock) - request the one-pager",
        cta_fine="Kit pricing and packaging are not finalised. No sales follow-up unless you ask for it.",
    )

def _bus():
    return dict(
        problem="""
        <p>A bus cabin contains a set of things that must be true before it carries passengers safely: seatbelts
        worn, doors closed and locked, no smoke or fire, and a driver who is awake and attending to the road.
        Today each of those, where monitored at all, is a separate system &mdash; or it is the driver.</p>
        <p>Regulatory pressure has grown sharply: EU General Safety Regulation driver-drowsiness monitoring has
        applied to new vehicles sold since July&nbsp;2024, advanced driver-distraction warnings apply EU-wide from
        July&nbsp;2026, and event-data recorders phase in through 2029. But those mandates attach to the
        <em>manufacturer</em> of new vehicles. They create no retrofit obligation on the fleet already in service.</p>
        """,
        physics="""
        <p>A mesh of small BLE sensor nodes distributed through the cabin: seatbelt-buckle sensors, door-state
        sensors, smoke and heat detectors, and a driver-facing attention module. The nodes form a self-healing
        mesh and report to a single vehicle gateway.</p>
        <p>The point of the mesh is the absence of wiring: one retrofit covers the whole cabin instead of one
        system and one loom per function. In plain language, a lot of cheap small nodes instead of a few
        expensive engineered ones.</p>
        """,
        specs=[
            ("Nodes", "BLE mesh: seatbelt/occupancy, door state, smoke and fire, driver attention"),
            ("Topology", "Self-healing mesh to a single vehicle gateway"),
            ("Retrofit", "Wireless &mdash; no cabin loom"),
            ("Driver attention", "Camera-based fatigue and distraction module"),
            ("Reporting", "Fleet dashboard; per-vehicle cabin state"),
        ],
        use_cases=[
            ("Seatbelt compliance",
             "Sense belt state per seat rather than assuming it from a warning lamp."),
            ("Smoke, fire and door state",
             "Report cabin conditions to the fleet rather than to the driver alone."),
            ("Driver attention on long-distance coach",
             "Add an attention module to vehicles that predate the OEM mandates."),
        ],
        who="Bus and coach operators and school-transport providers who need cabin-level assurance on vehicles already in service.",
        honest="""
        <p>The honest position: the mandate dollars in this category flow to OEM suppliers, and this space is held
        by well-funded tier-1 vendors. S5 publishes the mesh concept at <strong>awareness level only</strong> and
        would pursue it through an OEM or partner route, not as an aftermarket campaign. There is no conversion
        offer on this line.</p>
        """,
        cta_heading="One-pager on request",
        cta_body="""
        <p>Ask for the bus passenger-safety mesh one-pager and we will send the concept specification &mdash;
        including the honest assessment of what this line is and is not suited to.</p>
        """,
        cta_label="Request the bus mesh one-pager",
        cta_subject="Bus passenger-safety mesh - request the one-pager",
        cta_fine="Awareness level only; no conversion offer attached.",
    )


_CONTENT = {
    "rotamon": _rotamon(),
    "wearmon": _wearmon(),
    "getsmart": _getsmart(),
    "bolt": _bolt(),
    "genset": _genset(),
    "workshop": _workshop(),
    "bus": _bus(),
}

# products (slug <- content key)
PRODUCTS = [
    dict(slug="rotamon", key="rotamon", nav="RotaMon",
         title="RotaMon",
         sub="A multi-parameter condition-monitoring node that hears a machine begin to fail before it starts to vibrate.",
         kicker="Fixed plant &middot; Condition monitoring &middot; LoRaWAN",
         hero="s5_product_rotamon_hero.png",
         hero_alt="Three-dimensional render of a small rectangular S5 condition-monitoring node bracket-mounted to an industrial pump motor housing.",
         chip=("Pilot programme &mdash; open", "ok"), cta_kind="pilot"),
    dict(slug="wearmon", key="wearmon", nav="WearMon",
         title="WearMon",
         sub="Wear-liner thickness sensing that turns a shutdown-day surprise into a trend line.",
         kicker="Mineral processing &middot; Wear liners &middot; Flex-PCB sensing",
         hero="s5_product_wearmon_hero.png",
         hero_alt="Three-dimensional render of a thin flexible printed-circuit wear sensor strip curved inside a heavy steel wear-liner plate.",
         chip=("Pilot programme &mdash; open", "ok"), cta_kind="pilot"),
    dict(slug="getsmart", key="getsmart", nav="GETsmart",
         title="GETsmart",
         sub="Ground-engaging-tool and drill-rod detection, upstream of the crusher rather than downstream of it.",
         kicker="Mining &middot; Crusher protection &middot; Embedded sensing",
         hero="s5_product_getsmart_hero.png",
         hero_alt="Three-dimensional render of an excavator bucket wear tooth with an embedded sensor capsule beside a broken drill rod approaching a crusher.",
         chip=("Awareness &middot; spec on request", "info"), cta_kind="soft"),
    dict(slug="bolt-tension-monitor", key="bolt", nav="Smart bolt tension monitor",
         title="Smart Bolt Tension Monitor",
         sub="Continuous bolt-tension measurement for bolted structural connections.",
         kicker="Structural health &middot; Bolted connections &middot; Load-sensing washers",
         hero="s5_product_bolt-tension_hero.png",
         hero_alt="Three-dimensional render of load-sensing smart washers on a bolted steel structural connection.",
         chip=("Name pending owner decision &mdash; held from promotion", "warn"), cta_kind="soft",
         name_pending=True, noindex=True),
    dict(slug="genset-lighting-telematics", key="genset", nav="Genset &amp; lighting telematics",
         title="Genset &amp; lighting-tower telematics",
         sub="Fuel, light and location for mobile generation and lighting assets.",
         kicker="Plant hire &middot; Remote assets &middot; Fuel &middot; Light &middot; GNSS",
         hero="s5_product_genset-telematics_hero.png",
         hero_alt="Three-dimensional render of a mobile generator set and lighting tower with telematics sensors fitted.",
         chip=("Awareness &middot; spec on request", "info"), cta_kind="soft"),
    dict(slug="workshop-line", key="workshop", nav="Workshop line",
         title="Workshop line",
         sub="Jack oil-hours, car-wash chemical levels and a hoist safety-pin interlock &mdash; three small jobs, done by sensor instead of by memory.",
         kicker="Automotive workshops &middot; SMB kits",
         hero="s5_product_workshop-line_hero.png",
         hero_alt="Three-dimensional render of an automotive workshop with a hoist interlock sensor, an oil-hours sensor on a waste-oil jack and a car-wash chemical level probe.",
         chip=("Awareness &middot; spec on request", "info"), cta_kind="soft"),
    dict(slug="bus-safety-mesh", key="bus", nav="Bus safety mesh",
         title="Bus passenger-safety mesh",
         sub="A self-healing BLE mesh for seatbelt, door, smoke/fire and driver-attention monitoring in vehicles already in service.",
         kicker="Bus &amp; coach &middot; BLE mesh &middot; Cabin monitoring",
         hero="s5_product_bus-safety-mesh_hero.png",
         hero_alt="Three-dimensional render of a bus cabin interior with seatbelt, smoke detector, door-state and driver-facing sensor modules.",
         chip=("Awareness &middot; spec on request", "info"), cta_kind="soft"),
]

# ------------------------------------------------------------------ build ---

HOLD_BANNER = """
  <div class="banner">
    <strong>Working draft &mdash; not for public promotion.</strong>
    The product's previous working name conflicts with a trademark held by another company in the fastening
    industry. This product will not be announced or promoted anywhere until the owner approves a replacement name.
    The page is published for internal reference and is excluded from search indexing.
  </div>
"""

CSS = """/* S5 System product catalogue — shared stylesheet (2026-10-02) */
:root{
  --ink:#14212C; --ink-soft:#42586B; --ink-mute:#6B8095;
  --blue:#0B5C9E; --blue-deep:#083F6D; --blue-tint:#E8F1F9;
  --teal:#0E7C86; --teal-tint:#E4F2F3;
  --amber:#8A5A00; --amber-tint:#FDF3E0; --amber-line:#E8C88A;
  --paper:#FFFFFF; --panel:#F5F8FB; --line:#DBE3EB; --line-soft:#EAF0F5;
  --radius:10px; --maxw:960px;
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{
  margin:0;background:var(--paper);color:var(--ink);
  font:16px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;
  -webkit-font-smoothing:antialiased;
}
.wrap{max-width:var(--maxw);margin:0 auto;padding:0 24px}
a{color:var(--blue);text-decoration:none}
a:hover{text-decoration:underline}

/* ---- header ---- */
.site-head{background:var(--ink);color:#fff}
.site-head .wrap{display:flex;align-items:center;justify-content:space-between;gap:16px;min-height:64px;flex-wrap:wrap}
.wordmark{font-weight:700;letter-spacing:.14em;font-size:15px;color:#fff;text-transform:uppercase}
.wordmark span{color:#7FB3DC}
.head-nav{font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:#9FB4C6}
.head-nav a{color:#CFE0EE}

/* ---- hero ---- */
.hero{background:#0E1A24}
.hero img{display:block;width:100%;height:auto;max-height:420px;object-fit:cover}
.hero-cap{background:#0E1A24;color:#8FA6B8;font-size:12px;letter-spacing:.05em;padding:8px 0 0}
.hero-cap .wrap{padding:0 24px}

/* ---- page head ---- */
.page-head{padding:34px 0 8px;border-bottom:1px solid var(--line)}
.kicker{font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--ink-mute);margin:0 0 12px}
h1{font-size:34px;line-height:1.2;margin:0 0 12px;letter-spacing:-.015em}
.lede{font-size:18px;color:var(--ink-soft);margin:0 0 20px;max-width:70ch}
.chip{display:inline-block;font-size:12px;letter-spacing:.08em;text-transform:uppercase;padding:5px 11px;border-radius:999px;margin:0 0 6px}
.chip.ok{background:var(--teal-tint);color:#0A5A62;border:1px solid #B8DCDE}
.chip.info{background:var(--blue-tint);color:var(--blue-deep);border:1px solid #C2DAED}
.chip.warn{background:var(--amber-tint);color:var(--amber);border:1px solid var(--amber-line)}

/* ---- sections ---- */
main{padding:8px 0 40px}
section{padding:26px 0;border-bottom:1px solid var(--line-soft)}
section:last-of-type{border-bottom:0}
h2{font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:var(--blue);margin:0 0 14px}
h2 .n{color:var(--ink-mute);font-weight:600;margin-right:8px}
h3{font-size:16px;margin:22px 0 6px}
p{margin:0 0 14px;max-width:74ch}
ul{margin:0 0 14px;padding-left:22px;max-width:74ch}
li{margin:0 0 6px}
.physics{background:var(--panel);border-left:3px solid var(--teal);padding:18px 22px;border-radius:0 var(--radius) var(--radius) 0}
.physics p:last-child{margin-bottom:0}
.callout{background:var(--amber-tint);border:1px solid var(--amber-line);border-radius:var(--radius);padding:14px 16px;font-size:15px;color:#4A3A12;max-width:74ch}
.callout strong{color:var(--amber)}
table.specs{width:100%;border-collapse:collapse;font-size:15px;max-width:74ch}
table.specs th,table.specs td{text-align:left;vertical-align:top;padding:10px 14px 10px 0;border-bottom:1px solid var(--line-soft)}
table.specs th{width:34%;color:var(--ink-soft);font-weight:600}
table.specs tr:last-child td,table.specs tr:last-child th{border-bottom:0}
.cases{display:grid;gap:14px;grid-template-columns:repeat(auto-fit,minmax(240px,1fr))}
.case{background:var(--panel);border:1px solid var(--line);border-radius:var(--radius);padding:16px 18px}
.case h3{margin:0 0 6px;font-size:15px}
.case p{margin:0;font-size:14.5px;color:var(--ink-soft)}
.who{background:var(--blue-tint);border-radius:var(--radius);padding:16px 20px;max-width:74ch}
.who strong{color:var(--blue-deep)}

/* ---- cta ---- */
.cta{border:1px solid var(--blue);border-radius:var(--radius);padding:26px 28px;background:linear-gradient(180deg,#F3F8FC 0%,#FFFFFF 100%)}
.cta h2{color:var(--blue-deep);margin-bottom:10px}
.cta .btn{display:inline-block;background:var(--blue);color:#fff;font-weight:600;font-size:16px;padding:13px 24px;border-radius:8px;margin:6px 0 10px}
.cta .btn:hover{background:var(--blue-deep);text-decoration:none}
.cta .fine{font-size:13.5px;color:var(--ink-mute);margin:0}
.note{font-size:13.5px;color:var(--ink-mute);max-width:74ch}

/* ---- banner ---- */
.banner{background:var(--amber-tint);border:1px solid var(--amber-line);border-left:5px solid var(--amber);border-radius:var(--radius);padding:16px 20px;margin:22px 0 0;color:#4A3A12;font-size:15px;max-width:74ch}
.banner strong{color:var(--amber)}

/* ---- footer ---- */
.site-foot{background:var(--ink);color:#9FB4C6;margin-top:0;padding:34px 0 40px;font-size:14px}
.site-foot .wrap{display:block}
.site-foot h4{color:#fff;font-size:12px;letter-spacing:.14em;text-transform:uppercase;margin:0 0 10px}
.site-foot p{max-width:78ch;color:#A9BDCD}
.site-foot a{color:#CFE0EE}
.foot-bio{border-top:1px solid #2A3B49;margin-top:22px;padding-top:20px}

/* ---- index cards ---- */
.cards{display:grid;gap:18px;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));margin:8px 0 0}
.card{border:1px solid var(--line);border-radius:var(--radius);overflow:hidden;background:#fff;display:flex;flex-direction:column}
.card img{display:block;width:100%;height:150px;object-fit:cover}
.card .body{padding:16px 18px 18px}
.card h3{margin:0 0 6px;font-size:17px}
.card p{margin:0 0 10px;font-size:14.5px;color:var(--ink-soft)}
.card .tag{font-size:11.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-mute)}
@media (max-width:600px){h1{font-size:27px}.lede{font-size:16.5px}.cta{padding:20px}}
"""

def head(title, desc, hero=None, noindex=False, canonical=None):
    ni = '\n  <meta name="robots" content="noindex,nofollow">' if noindex else ''
    canon = (f'\n  <link rel="canonical" href="{canonical}">'
             f'\n  <meta property="og:url" content="{canonical}">') if canonical else ''
    return f"""<!DOCTYPE html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="author" content="S5 System Pty Ltd">{ni}{canon}
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="article">
<link rel="stylesheet" href="{{base}}assets/style.css">
</head>
<body>
<header class="site-head">
  <div class="wrap">
    <a class="wordmark" href="{{base}}index.html">S5 <span>System</span></a>
    <nav class="head-nav"><a href="{{base}}index.html">Product catalogue</a> &nbsp;&middot;&nbsp; Product information</nav>
  </div>
</header>
"""

FOOT = """
<footer class="site-foot">
  <div class="wrap">
    <h4>About this page</h4>
    <p>""" + PULL_NOTE + """</p>
    <div class="foot-bio">
      <h4>Who produces this</h4>
      <p>""" + AUTHOR_BIO + """</p>
      <p>Product catalogue &middot; generated """ + GEN_DATE + """ &middot;
         <a href="mailto:""" + EMAIL + """">""" + EMAIL + """</a></p>
    </div>
  </div>
</footer>
</body>
</html>
"""

def render_product(p):
    c = _CONTENT[p["key"]]
    base = "../"
    chip_cls = p["chip"][1]
    h = head(f'{p["title"]} — S5 System product catalogue',
             p["sub"].replace("&mdash;", "-").replace('"', "'"),
             noindex=p.get("noindex", False),
             canonical=BASE_URL + "products/" + p["slug"] + ".html")
    h = h.replace("{base}", base)

    n = [0]

    def sec(title, body, cls=""):
        n[0] += 1
        a = f' class="{cls}"' if cls else ""
        return (f'<section{a}><h2><span class="n">{n[0]:02d}</span>{title}</h2>{body}</section>')

    out = [h]
    out.append(f'<div class="hero"><img src="{base}assets/{p["hero"]}" alt="{p["hero_alt"]}"></div>')
    out.append('<div class="hero-cap"><div class="wrap">Placeholder 3D render &mdash; photographic product imagery is pending a product photo session.</div></div>')
    out.append('<div class="wrap page-head">')
    out.append(f'<p class="kicker">{p["kicker"]}</p>')
    out.append(f'<h1>{p["title"]}</h1>')
    if p.get("name_pending"):
        out.append('<p class="kicker" style="color:#8A5A00;margin:-6px 0 12px">'
                   'Working title &mdash; product name pending owner decision</p>')
    out.append(f'<p class="lede">{p["sub"]}</p>')
    out.append(f'<p><span class="chip {chip_cls}">{p["chip"][0]}</span></p>')
    out.append('</div>')
    if c.get("held"):
        out.append('<div class="wrap">' + HOLD_BANNER + '</div>')

    out.append('<main><div class="wrap">')
    out.append(sec("The problem", c["problem"]))
    out.append(sec("How it works, in plain language",
                   '<div class="physics">' + c["physics"] + '</div>'))

    rows = "".join(f'<tr><th>{k}</th><td>{v}</td></tr>' for k, v in c["specs"])
    out.append(sec("Key specifications", f'<table class="specs">{rows}</table>'))

    cards = "".join(f'<div class="case"><h3>{t}</h3><p>{b}</p></div>' for t, b in c["use_cases"])
    out.append(sec("Where it is used", f'<div class="cases">{cards}</div>'))

    out.append(sec("Who this is for",
                   f'<div class="who"><p style="margin:0"><strong>Suited to:</strong> {c["who"]}</p></div>'))

    if c.get("difference"):
        out.append(sec("Where S5 fits", c["difference"]))
    if c.get("market"):
        out.append(sec("Category context", c["market"]))
    if c.get("honest"):
        out.append(sec("The honest position", c["honest"]))

    mailto = (f'mailto:{EMAIL}?subject='
              + c["cta_subject"].replace(" ", "%20").replace("/", "%2F"))
    n[0] += 1
    out.append(f'<section class="cta" style="border-bottom:0">'
               f'<h2><span class="n">{n[0]:02d}</span>{c["cta_heading"]}</h2>' + c["cta_body"] +
               f'<a class="btn" href="{mailto}">{c["cta_label"]} &rarr;</a>'
               f'<p class="fine">{c["cta_fine"]}</p></section>')

    out.append('</div></main>')
    out.append(FOOT)
    return "\n".join(out)


def render_index(products):
    h = head("S5 System — product catalogue",
             "One page per S5 product line: the problem, how it works, specifications, use cases and a single next step. Educational and credential-led, no hype.",
             canonical=BASE_URL)
    h = h.replace("{base}", "")
    out = [h]
    out.append('<div class="wrap page-head">')
    out.append('<p class="kicker">S5 System &middot; Product catalogue</p>')
    out.append('<h1>Product catalogue</h1>')
    out.append('<p class="lede">One page per product line. Each covers the same five things: the problem, how it '
               'works in plain language, the key specifications, where it is used, and who it is for &mdash; with a '
               'single next step. Written for engineers, not for a purchasing committee.</p>')
    out.append('<p class="note">Pages are published in three states. <strong>Pilot programme &mdash; open</strong> '
               'means the product can be scoped for the 8-week paid Instrumentation Pilot now. '
               '<strong>Awareness &mdash; spec on request</strong> means the line is published as product information '
               'with no conversion offer. One line is held from promotion entirely while its name is settled.</p>')
    out.append('</div>')
    out.append('<main><div class="wrap">')

    out.append('<section style="border-bottom:0"><h2>Pilot programme</h2><div class="cards">')
    for p in products:
        if p["cta_kind"] == "pilot":
            out.append(card(p, ""))
    out.append('</div></section>')

    out.append('<section style="border-bottom:0"><h2>Awareness &mdash; spec sheet on request</h2><div class="cards">')
    for p in products:
        if p["cta_kind"] == "soft" and not p.get("name_pending"):
            out.append(card(p, ""))
    out.append('</div></section>')

    out.append('<section style="border-bottom:0"><h2>Held from promotion</h2>'
               '<p class="note">One product line is built but withheld from all public promotion because its '
               'previous working name conflicts with a trademark held by another company. It is not linked from '
               'this catalogue and is excluded from search indexing. It will appear here once the owner approves '
               'a replacement name.</p></section>')

    out.append('</div></main>')
    out.append(FOOT)
    return "\n".join(out)


def card(p, base):
    return (f'<article class="card"><img src="{base}assets/{p["hero"]}" alt="{p["hero_alt"]}">'
            f'<div class="body"><p class="tag">{p["kicker"]}</p>'
            f'<h3>{p["title"]}</h3><p>{p["sub"]}</p>'
            f'<p><a href="{base}products/{p["slug"]}.html">Read the {p["nav"]} page &rarr;</a></p></div></article>')


def strip_html(s, inline=True):
    """Convert the small, controlled subset of HTML used above into markdown."""
    s = s.strip()
    s = re.sub(r"<em>(.*?)</em>", r"*\1*", s, flags=re.S)
    s = re.sub(r"<strong>(.*?)</strong>", r"**\1**", s, flags=re.S)
    s = re.sub(r"<sub>(.*?)</sub>", r"\1", s, flags=re.S)
    s = re.sub(r"<[^>]+>", "", s)
    ent = {"&mdash;": "—", "&ndash;": "–", "&nbsp;": " ", "&times;": "×",
           "&middot;": "·", "&rarr;": "->", "&amp;": "&", "&deg;": "°",
           "&ldquo;": '"', "&rdquo;": '"', "&rsquo;": "'", "&lsquo;": "'"}
    for k, v in ent.items():
        s = s.replace(k, v)
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def html_block_to_md(s):
    """Turn a block of simple HTML into markdown, preserving document order."""
    s = s.strip()
    out = []
    pat = re.compile(r"<p([^>]*)>(.*?)</p>|<ul>(.*?)</ul>", re.S)
    for m in pat.finditer(s):
        attrs, body, ul = m.group(1), m.group(2), m.group(3)
        if ul is not None:
            items = re.findall(r"<li>(.*?)</li>", ul, re.S)
            out.append("\n".join("- " + strip_html(i) for i in items))
        else:
            pre = "> " if (attrs and "callout" in attrs) else ""
            out.append(pre + strip_html(body))
    if not out and s:
        out.append(strip_html(s))
    return "\n\n".join(x for x in out if x.strip())


def render_markdown(p):
    c = _CONTENT[p["key"]]
    L = []
    L.append(f'# {p["title"]}')
    if p.get("name_pending"):
        L.append("**Working title — product name pending owner decision.**")
    L.append(f'*{strip_html(p["kicker"])}*')
    L.append("")
    L.append(f'> {strip_html(p["sub"])}')
    L.append("")
    L.append(f'**Status:** {strip_html(p["chip"][0])}')
    L.append("")
    if c.get("held"):
        L.append("> **WORKING DRAFT — NOT FOR PUBLIC PROMOTION.** The product's previous working name "
                 "conflicts with a trademark held by another company in the fastening industry. This product "
                 "will not be announced or promoted anywhere until the owner approves a replacement name. "
                 "This file is for internal reference only.")
        L.append("")
    L.append("---")
    L.append("")
    L.append("## 01. The problem")
    L.append("")
    L.append(html_block_to_md(c["problem"]))
    L.append("")
    L.append("## 02. How it works, in plain language")
    L.append("")
    L.append(html_block_to_md(c["physics"]))
    L.append("")
    L.append("## 03. Key specifications")
    L.append("")
    L.append("| Specification | Detail |")
    L.append("|---|---|")
    for k, v in c["specs"]:
        L.append(f'| {strip_html(k)} | {strip_html(v)} |')
    L.append("")
    L.append("## 04. Where it is used")
    L.append("")
    for t, b in c["use_cases"]:
        L.append(f'**{strip_html(t)}** — {strip_html(b)}')
        L.append("")
    L.append("## 05. Who this is for")
    L.append("")
    L.append(f'**Suited to:** {strip_html(c["who"])}')
    L.append("")
    n = 6
    for key, title in (("difference", "Where S5 fits"),
                       ("market", "Category context"),
                       ("honest", "The honest position")):
        if c.get(key):
            L.append(f"## {n:02d}. {title}")
            L.append("")
            L.append(html_block_to_md(c[key]))
            L.append("")
            n += 1
    L.append(f'## {n:02d}. {strip_html(c["cta_heading"])}')
    L.append("")
    L.append(html_block_to_md(c["cta_body"]))
    L.append("")
    L.append(f'**[{strip_html(c["cta_label"])}](mailto:{EMAIL}?subject='
             + c["cta_subject"].replace(" ", "%20").replace("/", "%2F") + ') — one email, no follow-up unless you ask.**')
    L.append("")
    L.append(f'*{strip_html(c["cta_fine"])}*')
    L.append("")
    L.append("---")
    L.append("")
    L.append("## About this page")
    L.append("")
    L.append(PULL_NOTE)
    L.append("")
    L.append("**Who produces this.** " + strip_html(AUTHOR_BIO))
    L.append("")
    L.append(f'Product catalogue · generated {GEN_DATE} · {EMAIL}')
    L.append("")
    return "\n".join(L)


def main():
    os.makedirs(ASSETS_DST, exist_ok=True)
    os.makedirs(PROD_DST, exist_ok=True)
    os.makedirs(MD_DST, exist_ok=True)

    # assets
    for f in os.listdir(ASSETS_SRC):
        if f.endswith(".png"):
            shutil.copy2(os.path.join(ASSETS_SRC, f), os.path.join(ASSETS_DST, f))
    with open(os.path.join(ASSETS_DST, "style.css"), "w", encoding="utf-8") as fh:
        fh.write(CSS)
    with open(os.path.join(REPO, ".nojekyll"), "w", encoding="utf-8") as fh:
        fh.write("")

    # robots.txt — keep the held page out of crawl
    with open(os.path.join(REPO, "robots.txt"), "w", encoding="utf-8") as fh:
        fh.write("User-agent: *\nDisallow: /products/bolt-tension-monitor.html\n\n"
                 "Sitemap: " + BASE_URL + "sitemap.xml\n")

    # Pages is live at BASE_URL; LIVE-NOW.md records the published URLs.
    with open(os.path.join(REPO, "LIVE-NOW.md"), "w", encoding="utf-8") as fh:
        fh.write(LIVE_NOW_MD)

    written = []
    for p in PRODUCTS:
        path = os.path.join(PROD_DST, p["slug"] + ".html")
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(render_product(p))
        written.append(path)
        mdpath = os.path.join(MD_DST, p["slug"] + ".md")
        with open(mdpath, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(render_markdown(p))

    with open(os.path.join(REPO, "index.html"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(render_index(PRODUCTS))

    # sitemap
    urls = [BASE_URL, BASE_URL + "index.html"] + [BASE_URL + "products/" + p["slug"] + ".html"
                                                  for p in PRODUCTS if not p.get("name_pending")]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        sm.append(f"  <url><loc>{u}</loc><lastmod>{GEN_DATE}</lastmod></url>")
    sm.append("</urlset>")
    with open(os.path.join(REPO, "sitemap.xml"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(sm) + "\n")

    # manifest
    man = {
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "engine": "Persistent Product Awareness Engine - step 1 (PRODUCT-MARKETING-ENGINE.md s3)",
        "base_url": BASE_URL,
        "repo": "https://github.com/davoodnasehi/s5-product-catalogue",
        "hosting": "GitHub Pages (Actions workflow build, main branch, repo root) \u2014 live",
        "hosting_status": {
            "github_pages_enabled": True,
            "pages_build": "built",
            "pages_cdn": "serving \u2014 index, all 7 product pages, assets, manifest.json and sitemap.xml return HTTP 200",
            "live_url": BASE_URL,
            "repo_browse_url": "https://github.com/davoodnasehi/s5-product-catalogue",
            "raw_content_path": "https://raw.githubusercontent.com/davoodnasehi/s5-product-catalogue/main/",
            "next_action": "Optional only: mirror the folder under mining-iot.com/products/ or s5system.com/products/ for branded-domain SEO. Not required for a permanent URL.",
            "note": "An earlier check reported 404 Site not found for davoodnassehi.github.io (double-s). That hostname does not exist; the account handle is davoodnasehi. No GitHub provisioning fault.",
        },
        "contact": EMAIL,
        "source_docs": [
            "C:/Users/DN/s5-radar/PRODUCT-MARKETING-ENGINE.md",
            "C:/Users/DN/s5-radar/PRODUCT-TRIAGE.md",
            "C:/Users/DN/s5-radar/OPPORTUNITY-RADAR.md (s3-A, s3-H)",
        ],
        "local_source_folder": "C:/Users/DN/marketing-assets/product-catalogue",
        "pages": [],
        "notes": [
            "Pull-only tone: no hype, no cold-sell language; single CTA per page.",
            "Flagship positioning: sells diagnostic-coverage / proof-test-interval evidence; never 'SIL-rated sensors'.",
            "RotaMon and WearMon (triage PILOT NOW) carry the 8-week paid Instrumentation Pilot CTA.",
            "All other lines carry a soft 'request the one-pager/spec sheet' email capture only (trips WATCH/PARK/KIT verdicts).",
            "Bolt-tension page is NOT linked from the catalogue index, is noindex,nofollow, and is disallowed in robots.txt: held from all promotion until renamed (the previous working name conflicts with a trademark held by another company in the fastening industry).",
            "The previous working name for the bolt-tension line appears nowhere in any file.",
            "WearMon public copy withholds the proprietary sensing construction (IP clearance vs third-party patents pending); detail is released under NDA.",
            "Hero images are placeholder 3D renders; replace with real photography after the owner's storage photo session.",
            "CTA is a mailto: capture. Swap to a Typeform/CRM form endpoint when the funnel tooling is live.",
        ],
    }
    for p in PRODUCTS:
        c = _CONTENT[p["key"]]
        man["pages"].append({
            "slug": p["slug"],
            "title": strip_html(p["title"]).replace("&amp;", "&"),
            "nav_label": strip_html(p["nav"]).replace("&amp;", "&"),
            "file": "products/" + p["slug"] + ".html",
            "url": BASE_URL + "products/" + p["slug"] + ".html",
            "kicker": strip_html(p["kicker"]).replace("&amp;", "&"),
            "cta_kind": p["cta_kind"],
            "cta_label": c["cta_label"],
            "promotion_status": ("held_pending_rebrand" if p.get("name_pending")
                                 else ("pilot_open" if p["cta_kind"] == "pilot" else "awareness_only")),
            "triage_verdict": {"rotamon": "PILOT NOW #1", "wearmon": "PILOT NOW #2",
                               "getsmart": "WATCH", "bolt": "WATCH + rebrand required",
                               "genset": "PARK", "workshop": "KIT CANDIDATE",
                               "bus": "PARK"}[p["key"]],
            "noindex": bool(p.get("noindex")),
            "hero_image": "assets/" + p["hero"],
            "hero_image_url": BASE_URL + "assets/" + p["hero"],
        })
    with open(os.path.join(REPO, "manifest.json"), "w", encoding="utf-8", newline="\n") as fh:
        json.dump(man, fh, indent=2, ensure_ascii=False)

    print(json.dumps({
        "repo": REPO,
        "product_pages": written,
        "index": os.path.join(REPO, "index.html"),
        "manifest": os.path.join(REPO, "manifest.json"),
        "count": len(written),
    }, indent=2))


if __name__ == "__main__":
    main()
