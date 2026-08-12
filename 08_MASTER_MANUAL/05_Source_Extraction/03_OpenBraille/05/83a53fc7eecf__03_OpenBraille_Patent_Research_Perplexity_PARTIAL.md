# Source Extraction

- Chapter: `05` — OpenBraille Patent Evidence and Future Research Path
- Authority tier: `TIER_3`
- Manual treatment: `SUPPORTING_EVIDENCE`
- Original source: `03_CONCEPT_PORTFOLIO/OpenBraille/02_Raw_Research/03_OpenBraille_Patent_Research_Perplexity_PARTIAL.docx`
- SHA-256: `83a53fc7eecf97a9cf76cce718298b24d9cf93a150046ae5bc5a4290730bf74b`
- Extraction method: `DOCX_XML`
- Rule: source text only; no synthesis, correction or reconciliation.

---

OpenBraille Patent Landscape and Servo/Cam Macro-Scale Architecture Assessment (30 July 2026)

1. Executive Assessment

OpenBraille’s frozen MVP—a single macro-scale six-dot Braille cell driven by six SG90-class servos through eccentric cams and sliding pins in a 3D-printed frame—sits inside a heavily patented global landscape for refreshable Braille cells, but also within an explicitly identified white-space band around manufacturing methods, mechanical tolerance strategies, and low-cost control.[1][2]

Independent current searching across US, EP, WO and recent academic/open-hardware work confirms that:

Servo/cam-based actuation of Braille pins is clearly known and claimed at standard scale, including stepping-motor/cam multi-dot actuation and motor-driven cam assemblies.[3][4][^5]

Multi-layer electromagnetic latching, electroactive polymer cells, SMA-based actuators, and modular compressible-pin assemblies form dense prior-art clusters around dot actuation, pin guidance, latching and modularity.[6][7][8][9]

Newer patents (2013–2026) focus on modular cell architectures, capture plates, tactile pixels, EM latching readers, and layered EM stacks, often at compliant ISO dot pitches.[10][11][12][13][^14]

Open-hardware projects MOLBED and MagnePins demonstrate credible EM-latching and passive-pin arrays, explicitly unpatented in the case of MOLBED and open-source HCI research for MagnePins.[15][16]

Given this landscape, the frozen OpenBraille servo/cam cell itself is not a strong mechanistic novelty candidate, but there remains a credible path if the invention is framed around: (a) tolerance-compensating macro-scale mechanical/control architecture, (b) low-cost per-dot calibration and verified tactile-state control, and (c) scale-transfer manufacturing and modularity, all supported by measured evidence.[17][1]

Classification:

Overall: credible path only with bounded enhancement (B) and possible long-term extension (C).

The current MVP has some defensible technical contribution around macro-scale tolerance, low-cost fabrication, and team-fit architecture but requires targeted enhancements and experiments to reach a claimable invention.[^17]

Confidence: Moderate. The prior art is rich and sometimes difficult to fully map (Dot Inc. estate, Indian filings such as 5559/CHE/2014, recent EM-latching families), but the differentiation axes for OpenBraille can be made precise and experimentally testable.[2][18]

Key limitations: incomplete access to Indian file 5559/CHE/2014, incomplete claim-charting for key families (Dot’s cells, IIT Delhi cursor mechanisms, Braille PolyPad pneumatic systems), and the inherently higher risk of method/algorithm-style claims compared to apparatus plus method.

2. Search Log (Representative)

Below is a condensed log of the main databases and strategies used. It is not exhaustive but covers the mandatory areas and named leads.

2.1 Patent Databases and Registers

USPTO Patent Public Search / lens-based mirror: used for all US patents and applications in the named list and adjacent Braille-cell families.[7][8][^19]

EPO Espacenet & EP Register: used for EP471327, EP4049116, and other European Braille/tactile pixel records.[20][9]

WIPO PATENTSCOPE: used for WO2016074170, WO2020106855, WO2015189863 (via family), WO2013130534, WO2024174030, and magnetic/pneumatic display work.[21][22][23][11]

Google Patents: used as a navigation and citation-expansion tool for Dot-related families, SMA/EAP cells, EM-latching displays, and actuation mechanisms (US8770981).[^24]

Chinese, Japanese, Korean patent records: accessed via WO and EP family members where full national-text search was not available in English; notably CN104408994A and KR20210092296 for EM Braille and modules.[11][25][^10]

Indian Patent Office (InPASS / IP India): searched via public advanced search for G09B/G09F Braille-related terms and applicant names; specific retrieval of 5559/CHE/2014 proved unsuccessful.[26][27][^28]

Date: All searches and secondary reading performed 29–30 July 2026.

2.2 Jurisdictions Covered

United States (USPTO; primary for most named leads).[29][7]

Europe (EPO Espacenet, EP Register).[9][20]

WIPO / International (PATENTSCOPE).[23][11]

China (via WO/EP family, CN citations in US11410574B2).[^10]

Japan and Korea (via JP/KR family members of EM-latching Braille reader and modules).[25][11]

India (IP India search; QuickCompany listing for cam-based cells).[27][30]

2.3 Search Strings and Classifications

Representative queries (often combined with G09B21/003, G09B21/004, G09F9/377):

"refreshable braille cell servo cam follower pin".[4][3]

"tactile braille display dynamic cam actuator".[^5]

"electroactive polymer actuator braille cell".[^7]

"shape memory alloy refreshable braille".[8][24]

"compressible pin arrays braille".[^6]

"modular refreshable braille display".[13][31]

"capture plate assembly braille".[^14]

"tactile pixels braille".[^9]

"electro magnetic refreshable braille reader".[12][11]

"layered electromagnetic braille display".[23][10]

"braille cursor passive magnetic mechanism".[^32]

"3D printed braille cell tactile pins".[33][18]

"macro scale braille prototype cam" (for open-hardware).[34][18]

"Indian patent braille cell cam actuator".[^27]

Classifications:

Core: G09B21/003 (Braille cells), G09B21/004 (refreshable Braille displays), G09F9/375/377 (display devices), G06F3/016 (tactile displays), with auxiliary codes around embedded control and learning apparatus.[12][7][^9]

2.4 Screening Method

Initial filter by classification + keyword; discard high-level Braille support/software patents unless they mention hardware cell structures.[35][36]

For each promising record, read abstract, main independent claim, and technical field/background sections to confirm relevance to physical actuation, pin guidance, or modular cell architecture.

Map families (US/EP/WO/JP/KR/CA) and note grant vs application status, priority dates, and assignees.[11][10]

Cross-link open-hardware and academic projects (MOLBED, MagnePins, Aryan 2021 cam mechanism, Braille PolyPad, IIT Delhi cursor mechanism, NIU SMA actuation) to patent clusters but treat them as non-patent prior art unless explicit patent numbers found.[16][37][38][15][^24]

3. Verified Family Table (Selected Materially Relevant Families)

The table focuses on families with direct relevance to refreshable pins, cams, EM latching, modularity, capture plates, tactile pixels and alternative actuation.

Family / Core Number

Priority Date

Assignee / Applicant

Jurisdictions / Members

Legal Status (2026)

Source & Status Confidence

Relevance to OpenBraille

US5685721A – SMA braille cell

1995-11-06

American Research Corp. of Virginia

US, CA family

Expired (20-year term)

USPTO full-text; high confidence[^8]

SMA-based single-moving-part cell; shows dense early prior art on low-part-count actuators, latching; relevant as expired foundational prior art fence.

US5453012A – rotary cam braille display

1993-09-28

Robotron Pty Ltd

US, JP, DE family

Expired

USPTO; high confidence[^3]

Two cam members driven by stepping motors actuating multiple pins; directly establishes cam-based braille actuation at standard scale, limiting mechanistic novelty for servo/cam.

US5766014A – binary cam braille

1997-04-17

Mitsubishi Materials Corp.

US, DE, JP family

Expired

USPTO; high confidence[^4]

Triplet cam actuated by stepping motor with eight positions for four pins; detailed cam geometry and binary behaviour; strong prior art on cam/follower logic.

US5226817A / EP471327 – piezo braille cell

1991-08-08

KGS Corp.

US, EP, DE, ES, JP

Expired

USPTO & Espacenet; high confidence[39][20]

Tactile section with detachable cap and piezo reeds; modular tactile caps and cleaning; relevant for pin guidance, detachable sections.

US7410359B1 + US7462034B1 + US20090035731A1 – electromechanical tactile cell

2004-09-17

Freedom Scientific / Enhanced Vision Systems

US, later WO/EP

Granted (older)

USPTO; high confidence[40][33][^41]

Serial piezo bimorph-based cells, multiple conductive supports; heavy prior art around manufacturable multi-cell assemblies.

US8690576B2 + US9424759B2 + WO2013130534A1 – braille display device & method

2010-08-13 priority

Freedom Scientific / EVS

US, WO, EP, JP, ES

Granted, active

USPTO/WO/EPO; high confidence[29][42][^43]

High-integration dot-incorporation-style cells; central to "Dot Incorporation"-type estate: dense coverage of pin arrays, cell housing, assembly; major FTO fence especially for multiline cells.

US6881063B2 – electroactive polymer braille cell

2003-02-24 priority

Yang / EAP braille

US, EP, WO

Granted; still active in some jurisdictions

USPTO/Espacenet; high confidence[^7]

Compact hydraulic EAP braille cell with latching; relevant as alternative actuation cluster; shows low-power latch structures and hydraulic amplification.

WO2015189863A2 – SMA compliant mechanism braille display

2014-06-08

Indian team (IIT Madras-linked)

WO

Application; later national phases

PATENTSCOPE; medium confidence[^21]

SMA wires, cantilever strips and latching within five-layer cell; key Indian prior art on compliant mechanisms, cantilevered strips, SMA; strongly overlaps with tolerance/cantilever themes.

US11410574B2 + WO2016074170A1 – layered EM braille display

2014-11-12

Yang Wen-zhen et al.

CN, WO, US

Granted (US), active

USPTO/WIPO; high confidence[10][23]

Three stacked EM layers with pin driving mechanisms using coils, iron cores and pin caps; multi-row EM architecture, pin groups; relevant as EM alternative and layered design prior art.

WO2020106855A1 + US12548467B2 – EM refreshable braille reader (EMBR)

2019-11-20 priority

Moon et al.

WO, US, EP, CA, KR, JP

US granted 2026, others mixed

WIPO/USPTO; high confidence[11][12]

Permanent magnet + coil EM actuators, removable top dot capture assemblies, capacitive touch layer; modern EM-latching/reader cluster; relevant to latching and capture-plate cell geometry.

US11915607B2 – modular refreshable braille display system

2020-05-29 priority

Brailleazy Inc.

US

Granted (2024)

USPTO; high confidence[^13]

Mobile-device case with magnet-based pin latching and modular bases; relevant for modular cell and magnet-actuated pins; but servo/cam at macro-scale is architecturally distinct.

US12080182B2 + WO2021183616A1 – capture plate assembly

2020-03-27 priority

Moon et al.

US, WO, EP

US granted (2024)

USPTO/WIPO; high confidence[^14]

Removable capture plates and membranes decoupling dot actuators from braille dots; strong prior art on removable top assemblies and cleaning; relevant to any modular plate concept.

EP4049116A1/B1 + WO2021079101A1 – tactile pixels

2019-10-21 priority

Ali Mohammadi

GB, EP, WO, US

Active

Espacenet/WIPO; high confidence[^9]

General tactile pixel architecture with G06F3/016 and G09B21 classifications; relevant as broad coverage of tactile arrays and pixel-level actuation structures.

US8770981B2 – SMA actuation mechanism for braille displays

2010-04-30 priority

Northern Illinois University

US, WO; expired fee-related

Google Patents; high confidence[^24]

SMA wire-driven sliding block with bias springs; prior art for SMA-driven single-dot mechanics and PWM control; relevant for actuation alternatives.

WO2013179311A1 (IIT Delhi) – refreshable tactile text/graphics

2012-05-31

IIT Delhi

WO; later national phases

WIPO/Google; medium confidence[^24]

Passive ferromagnetic pins actuated by moving cursor; adjacent to Braille PolyPad and passive-magnetic cursor designs; relevant for passive-pin + moving actuator architectures.

US10890993B2 – modular braille display system with touch input

2014-06-25 priority

Optelec Holding B.V.

US, EP

Granted; active

USPTO/EPO; high confidence[^31]

Modular rows of cells with integrated touch-sensitive surface and docking; relevant for modular multi-cell and user-interaction geometry.

US20130017516A1 – active braille timepiece

2011-07-11

Tyler Kelly

US

Application; timepiece-specific

USPTO; medium confidence[^44]

Braille watch with servo motors and cam shafts for translational pins; demonstrates servo-plus-cam actuated pins in a braille context; prior art at device scale.

US20090023116A1 + US8740618B2 – compressible pin arrays

2007-07-20

Tactile Display Corp.

US

Granted; active

USPTO; high confidence[6][45]

Pins with compressible springs and linear actuators; addresses force and cleaning; relevant to pin resilience and modular cleaning pathways.

US6902403B1 – contaminant-tolerant braille pins

2004-08-04

Freedom Scientific

US, EP, WO

Granted; active or near-expiry

USPTO/Espacenet; high confidence[^46]

Multi-shoulder pin geometry and bore clearances to resist fouling; directly relevant to tolerance and contamination—important for tolerance-compensating guides.

US6692255B2 – cylinder-based braille reader

2001-08-06

US Dept. of Commerce

US

Granted; active

USPTO; high confidence[^47]

Rotating cylinder with bi-directional motion and actuators; relevant as macro-scale streaming architecture, but different geometry.

EP4049116 et al. – tactile pixels (global)

2019+

As above

Global

Active

As above[^9]

Already covered above.

Family relationship note: US8690576B2 and US9424759B2 are continuation/continuation-in-part outputs of an electromechanical braille-cell lineage that traces back to US7410359B1 and related applications; WO2013130534A1 summarizes the later system-level display device but shares core cell structure with earlier US patents.[42][43][^29]

Dot Incorporation per se is not explicitly named as assignee in these records, but the Phase 2 synthesis correctly treats the Freedom Scientific/EVS family as the functional "Dot Incorporation"-estate fencing practical multi-cell piezo assemblies.[^2]

4. Independent Claim Analysis (Closest Records)

This section extracts and interprets key independent claims from the closest art, focusing on actuation, pin support, tolerance, modularity, latching, and capture mechanisms.

4.1 Cam and Motor-Based Braille Cells

US5453012A – Braille display (Robotron)

Claim 1 describes a Braille display having:

A plurality of pins movable between elevated and lowered positions in a matrix representing characters.

A rotary means (two cam members with specific cam profiles) associated with columns of pins; different rotary positions give different permutations of elevated/lowered pins corresponding to characters.

Drive means (stepping motors) for selectively rotating the cams between positions.[^3]

Interpretation: This gives broad coverage to using rotary cams driven by motors to actuate multiple pins, including the concept of pin patterns mapped to cam positions. Although OpenBraille uses six independent servos (one per dot) and eccentric cams instead of shared cams per column, the core idea of cam-driven braille pins is prior art.

US5766014A – Binary information display apparatus (Mitsubishi)

Claim 1 covers:

An apparatus with four pins, a triplet cam acting on three pins, and a second cam acting on the fourth pin.

A stepping motor with discrete step positions driving the first cam; pin projections correspond to concave/convex cam portions.[^4]

Interpretation: The claims cover sophisticated cam arrangements where one motor drives multiple pins via cam profiles. Again, this predates OpenBraille’s eccentric servo cams and establishes that converting rotary motion via cam profiles to pin up/down at braille-scale pitch is not novel.

4.2 Piezo and Modular Cell Architecture

US5226817A / EP471327 – Braille cell (KGS)

Independent claims define:

A Braille cell comprising multiple piezoelectric reeds attached to a base through PCB, tactile pins at free ends of reeds.

A detachable tactile section with cap holding pins, enabling cleaning without detaching pins individually.[39][20]

Interpretation: Strong coverage on detachable tactile sections and modular pin caps, relevant to capture-plate ideas. Tolerances and cleaning are explicitly addressed.

US7410359B1 – Electromechanical tactile cell assembly (Freedom Scientific)

Claim 1 defines:

Piezo reeds bend at elongated ends when voltage applied.

Conductive fulcrum pins and multiple element conductive supports securing reeds to PCB.[^40]

Interpretation: Focus is on efficient electrical/mechanical support structure reducing manual soldering; architecture-level but not directly challenging servo/cam at macro scale, except as background to multi-cell manufacturing.

4.3 Dot Incorporation-Style Display Devices

US8690576B2 / US9424759B2 / WO2013130534A1 – Braille display device and method

Independent claims cover:

A refreshable Braille display with housing, upper cover with apertures for pins, motherboard, Braille cell assemblies, and cursor routing buttons.[43][29][^42]

Each cell assembly supporting eight bimorph reeds and pins, with cost-optimized mounting blocks and backplanes.

Interpretation: These claims focus on system-level integration, cell mounting, and cursor routing. While they dominate practical multi-line piezo displays, they do not explicitly claim servo/cam architectures; rather they fence piezo assemblies and integrated housing.

4.4 Electroactive Polymer Cells

US6881063B2 – Electroactive polymer actuator braille cell

Claim 1 presents:

A fluid-tight housing with diaphragm and braille dot; fluid and EAP bending elements acting like pumps.[^7]

Interpretation: Alternative actuator cluster; relevant as prior art for low-power hydraulic amplification but distinct from macro servo/cam.

4.5 Electromagnetic Latching and EM Readers

US11410574B2 / WO2016074170A1 – Layered EM Braille display

Claims define:

Three layered Braille display modules with pressing plates, iron core plates, line coils, and tactile pin driving mechanisms.[10][23]

Interpretation: Multi-layer EM architecture with line coils and iron cores; heavy prior art around EM pin latching and multi-row displays.

WO2020106855A1 / US12548467B2 – EM refreshable braille reader (EMBR)

Claims cover:

A tactile display with electromagnetic actuating elements and braille dots; capture plate assemblies; magnets within insulator spaces with surrounding coils.[11][12]

Interpretation: EM-latching braille dots with removable dot capture assemblies and capacitive touch surfaces; these families are central modern EM-latching prior art and directly adjacent to MOLBED/MagnePins-type mechanisms (which are open-source but conceptually similar). They fence EM latching at braille pitch and modular capture plates.

4.6 Modular and Capture-Plate Architectures

US11915607B2 – Modular refreshable braille display system

Claims emphasize:

Mobile-device case with contact surface, cavities, pins, bar magnets, detachable top housing, and communication interface.[^13]

Interpretation: Focuses on magnet-based pin latching and modular cell packaging in a mobile case. Relevance: any macro modular cell design with magnets must respect this cluster.

US12080182B2 – Capture plate assembly for braille display

Independent claims describe:

Capture plate assembly with display dots, top assembly with braille dots, membrane separating dots, capacitive touch layer; removable capture plate.[^14]

Interpretation: Expands prior art on removable top plates; strong fence on capture-plate plus capacitive touch combinations.

4.7 Tactile Pixels and General Tactile Displays

EP4049116A1/B1 – Tactile pixels

Claims (at high level) cover tactile pixel arrangements for braille or graphics, under G06F3/016 and G09B21; details include pixel arrays and actuation structures.[^9]

Interpretation: Broad generic coverage of tactile pixels; relevant as high-level environment but less constraining at single-cell macro scale.

4.8 Actuation Mechanisms (SMA) and Alternative Designs

US8770981B2 – Actuation mechanism for braille displays

Claim 1 defines a pin and sliding block actuated by a single bias compression spring and single SMA wire; wire activation moves block to retract pin.[^24]

Interpretation: Prior art for SMA sliding-block actuation; relevant if OpenBraille considered SMA alternatives; not directly conflicting with servo/cam.

4.9 Academic / Non-Patent Prior Art

Aryan 2021 – Refreshable Braille Module Using Cam Actuated Mechanism: servo-driven cam shafts to actuate pins; confirmed as cam/servo braille project.[^37]

Leonardis et al. 2020 – passive magnetic cursor mechanism: single actuated slider with passive pins.[^32]

Braille PolyPad (Xie et al. 2021): stiffness-variable polymer + pneumatic pins; alternative low-cost large-matrix concept.[^38]

IIT Delhi cursor mechanism (WO2013179311): moving cursor over passive pins; as above.[^24]

MOLBED: magnet-retained pins actuated by coils; explicitly unpatented; low-cost EM-latching braille character modules.[^15]

MagnePins (UIST 2025): large passive pin array actuated by simple EM mechanism; open-source design with braille-compliant pitch.[^16]

These sources significantly raise the bar for novelty in EM-latching and cam-based mechanisms, even absent patent filings.

5. Frozen-MVP Feature Chart vs Closest Art

Using the categories requested, the table compares OpenBraille’s servo/cam macro cell features primarily against: US5453012A, US5766014A, US6881063B2, US11410574B2, WO2020106855/US12548467B2, US11915607B2, US12080182B2, EP4049116, Aryan 2021, MOLBED, MagnePins, and Freedom Scientific cells.

Legend:

ED: expressly disclosed

NI: necessarily implied by core operation

AS: arguably suggested (design choices, optional variants)

AB: absent

UR: unresolved in available documents

MVP Feature

Servo/cam patents (US5453012/US5766014)[3][4]

Piezo/microactuator cells (Freedom/KGS)[39][40][^29]

EM/SMA/EAP clusters (US6881063, US11410574, US12548467, WO2020106855)[7][10][11][12]

Modular/capture/tactile pixel (US11915607, US12080182, EP4049116)[13][14][^9]

MOLBED/MagnePins/open cam projects[15][16][37][18]

Six independent low-cost servos (one per dot)

AB (motors per column, not per dot)

AB (piezo reeds per dot, but no servo)

AB (coils/magnets, not servos)

AB

NI/AS (cam actuators sometimes use individual electromagnets; Varada’s refreshable module uses EM + cam, but not explicitly servo)

Direct PWM control from MCU

AB (steppers driven by drivers; PWM implicit but not central)

AB (piezo drive circuits, high voltage)

ED (coil current control; PWM suggested)

AB

NI/AS (Arduino shield-driven coils in MOLBED; PWM use suggested in NIU SMA work)

Eccentric cam per dot

ED (cam per column)

AB

AS (cams used for EM flip latches in some academic work)

AB

ED (eccentric cam with embedded magnet in refreshable module; EM-actuated cam in NIU example)

Follower (roller or lever)

ED (cam followers implied by cam-pin interface)

AS (pushup cams with reeds)

AS (magnet/cam interactions)

AB

ED (cam followers in Hackaday projects and Aryan 2021 mechanism)

Sliding tactile pin

ED

ED

ED

ED

ED

Printed guide/frame (FDM 3D printed cell)

AB (machined housings)

AB (molded plastic housings)

AS (fabrication unspecified but often machined/molded)

AS (generic housings; not 3D-specific)

ED (3D-printed bodies for pins and magnet holders; 3D-printed frames and cams)

Macro scale (~300% ISO dot pitch)

AB

AB

AB

AB

AS (MOLBED is explicitly braille-compliant; Aryan 2021 may operate near standard scale; most work targets conformant pitch)

Active retraction via actuator

ED (cams actively move pins up/down)

NI (piezo reeds actively bend; pins follow)

ED (coils actively move pins)

NI (actuation unspecified; depends on underlying devices)

NI (cam and EM move pins; magnets latch)

Calibration (per-pin PWM or mechanical tuning)

UR (not emphasized)

UR (factory calibration; not per-user)

UR (could be implemented but not widely claimed)

UR

AS (MOLBED and EM-latching readers benefit from calibration; NIU SMA uses PWM tuning)

Actuation sequencing (low-power strategy)

UR

AS (multiplexing drivers)

ED (EMBR includes energetics diagrams, power-aware control)

UR

ED (flip-latch EM and magnetic cursor mechanisms emphasize low-power latching)

Modularity (cell-level replaceable unit)

AS (cam modules per column)

ED (individual cells mounted on backplane)

AS (EM modules)

ED (modules and docking stations)

ED (MOLBED character modules, line PCBs, page PCBs)

Power architecture (external 5 V for servos, single rail)

AB

AB (higher voltages typical)

AS (low-voltage control for EM)

AB

AS (12 V for TB6612 drivers; modules for EM)

Tactile validation / human readability measurement

UR

UR

UR

UR

UR (MagnePins paper mentions expert reader tests, but details are limited)

Conclusion: Most physical elements of the servo/cam MVP—cam-actuated pins, followers, cells, modular assemblies—are already disclosed across older and newer patents and open projects. The potentially differentiating elements are:

Use of low-cost hobby-class servos at macro scale for a single-cell MVP, with direct PWM from ESP32 and no driver electronics.[^17]

3D-printed frame and cam geometry explicitly designed to absorb print tolerances rather than meet ISO pitch.[^17]

Education-oriented architecture optimized for a cyber/CS-student team with minimal mechanical tooling.

These do not constitute strong apparatus novelty on their own but are promising as part of a method/manufacturing/tolerance-compensation narrative.

6. Indian-Patent Investigation: 5559/CHE/2014

6.1 What Is Known

Phase 3C logs and Hackaday notes identify 5559/CHE/2014 as an Indian application filed 5 November 2014, described as covering "micro-motor actuated pins, pin cantilever design, mechanical stops to limit rotor rotation, motors with rotors or cams, mounted vertically or horizontally used to lift pins directly or via an interposer, low force selector" for refreshable braille displays.[48][49]

QuickCompany and Indian patent journals lists were checked for:

Number formats "5559/CHE/2014", "CHE/2014/5559", and possible published numbers derived from that filing reference.[30][27]

Assistech/IIT Delhi-related braille patents (cursor systems, tactile displays).[50][27]

No direct official publication record mapping exactly to 5559/CHE/2014 was found via open IP India search, suggesting one of:

The application remained unpublished (abandoned or withdrawn before publication).

The number refers to an internal filing/diary number, not the later publication number.

The data is present behind the InPASS interface but requires manual or on-site access beyond public web tools.[^28]

6.2 Current Retrieval Status

Publication number: unresolved. No direct US/EP/WO family mapped from 5559/CHE/2014 through public databases.[^27]

Complete specification: unavailable via public IP India sites under the exact identifier.

Claims: unavailable.

Applicant/inventor: likely Paul D’Souza or collaborating entity, per Hackaday logs, but not confirmed by Indian official records.[49][48]

Filing and publication dates: filing 05 Nov 2014 is reported in community sources; publication date remains unknown.[^48]

Prosecution and legal status: no accessible legal-status summary via IP India for the specific code; likely abandoned or pending under another publication number.[26][28]

Family equivalents: none were found in US/EP/WO under obvious similar titles ("tactile display for visually impaired", "braille cell and assembly") except QuickCompany references to Indian filings that resemble IIT Delhi’s WO2013179311 or other braille cell patents.[51][27]

6.3 Relevance and Risk

Based on secondary descriptions, 5559/CHE/2014 likely claims:

Micro-motor actuated pins (similar to pico-motors used as cams).[^48]

Pin cantilever and lever-based amplification.[^48]

Mechanical stops and low-force selectors for binary cam behaviour.[^48]

These functionalities overlap strongly with Varada’s open-hardware refreshable display and electromechanical cam projects, and conceptually with any macro servo/cam architecture, though the exact claim boundary cannot be charted without the file.[18][34]

Conclusion: The Indian patent is a known but unresolved risk source. Any claim strategy relying on detailed cam/micro-motor/cantilever geometry should be cross-checked by counsel via direct IP India registry access and possibly correspondence with the inventor (Paul D’Souza) before being considered safe. For current semester work, treating it as blocking prior art for micro-motor-based cam cantilever designs is prudent.

7. Separate Risk Analyses

7.1 Novelty Risk

Cam-based actuation of Braille pins is established decades ago (US5453012, US5766014).[3][4]

Servo motors driving pins or cams appear in watch and device patents (US20130017516A1, braille watch; open hardware refreshable modules).[44][34]

Pin guidance via slots and detachable caps is heavily covered (US5226817, US7462034, US20090035731).[41][33][^39]

EM-latching mechanisms, passive pins plus EM actuators, and magnet-based latching appear in modern patents and academic work (US12548467, WO2020106855, Leonardis 2020, MagnePins).[16][12][32][11]

Modular braille cells, capture plates, and tactile pixel arrays are present (US11915607, US12080182, EP4049116).[13][14][^9]

Novelty risk is therefore high for any claim that treats:

"servo + cam + pin + guide" at braille-scale as the invention.

"modular braille cell with removable top" in isolation.

"magnetic latching" of pins as new.

Residual novelty may exist in:

A specific macro-scale mechanical tolerance management strategy designed for FDM printing and low-cost metals, with measured repeatability and yield.[1][17]

A combined manufacturing/control method (including calibration, sequencing, and scale-transfer procedure) enabling low-cost reproduction of acceptable tactile performance from commodity servos and printed guides.[^1]

7.2 Obviousness / Inventive-Step Risk

Given the saturated landscape:

Using macro-scale servo/cam instead of piezo, SMA, EM, or micro-actuators may be seen as a straightforward substitution of known actuators into known braille pin/cam structures, particularly given the refreshable braille literature that explores "low-cost actuators" and 3D printing.[37][34][^18]

Macro-scaling to ease FDM fabrication is a common engineering tactic and appears in broader assistive device literature ("scale up to print"), even if not claimed explicitly.[^17]

Using ESP32 PWM for servos, calibration tables, and simple sequencing are textbook embedded control practices.

To clear inventive-step, OpenBraille likely needs to demonstrate non-obvious technical effects, such as:

A documented tolerance window and yield improvement compared to existing low-cost cam/pin implementations at similar cost.[1][17]

Measurable reductions in Brown-out, jitter, or misalignment due to a specific power/control and mechanical architecture.[^17]

A novel way of combining macro experiments and analytic scale-transfer to standard pitch (even if the latter is future work).

Obviousness risk is thus medium–high, but can be pushed towards medium if claims focus on quantified tolerance/return/compliance interactions rather than generic servo/cam substitution.

7.3 Patent-Eligibility Risk

In India, US, EP and many other jurisdictions, apparatus-plus-method claims for electromechanical devices are generally patent-eligible unless framed as pure mathematical algorithms or abstract methods.[^52]

OpenBraille’s strongest potential claims involve:

Mechanical structures (frames, cams, guides, pins) and their interactions.

Control methods tied directly to physical effects (calibration, PWM, sequencing, power gating).[1][17]

Eligibility risk is therefore low, provided claims avoid pure software or user-interface aspects detached from hardware. However, any future heavy reliance on control algorithms or calibration logic must tie them clearly to physical improvements (e.g., reduced variance, lower current, improved tactile reliability) to avoid "abstract method" traps.

7.4 Freedom-to-Operate (FTO) / Infringement Risk

The FTO picture is not yet formally charted but key hazards include:

Dot Incorporation / Freedom Scientific estate: multi-cell displays with piezo reeds, detachable caps, contaminant-tolerant pins; any multi-cell piezo design would strongly risk infringement.[46][29][^42]

EM-latching readers (Moon et al.): EM actuators with capture plates and magnet-coil structures; replicating EM latching at standard pitch risks conflict.[12][14][^11]

Layered EM displays (Yang et al.): multi-layer EM braille stacks.[23][10]

Magnet-based modular cells (Brailleazy): bar magnets and modular top housings for mobile cases.[^13]

MOLBED/MagnePins: open-source; no direct infringement risk, but commercial exploitation must respect any overlapping patents (Moon, Leonardis) and open-hardware licensing.[15][16]

Indian 5559/CHE/2014: unresolved; micro-motor cam/cantilever claims could complicate any direct reuse of that geometry.[49][48]

For the current single macro-scale servo/cam cell:

FTO risk is moderate: the device uses known elements but at non-compliant scale, single-cell scope, and commodity servos, which likely fall outside the core fences of piezo, EAP, EM-latching and micro-cam arrays. However, without claim-charting, this cannot be asserted confidently.[2][17]

Long-term multi-cell or compliant-scale designs would raise FTO risk significantly and require professional claim-charting against the above estates before productization.

8. Candidate Invention Directions

This section evaluates several candidate directions requested, separating bounded enhancements (B) from major redesigns and potential Track C long-term work.

8.1 Tolerance-Compensating Mechanical / Control Architecture

Nearest prior art: contaminant-tolerant pins (US6902403B1), modular caps (US7462034B1), compliant SMA/EAP mechanisms (US6881063B2, WO2015189863), manufacturing-friendly braille cells (Freedom Scientific families).[21][41][29][46][^7]

Prospective differentiating elements:

Explicit macro-scale tolerance budget for FDM printing: clearances, slot widths, cam radii, pin verticality, and flatness targets tuned to cheap printers and materials, coupled with observed assembly yield and cycle life.[^17]

A mechanical architecture combining: servo-integral torsion reset, eccentric cam, follower, printed guides, and macro relief to remove dependence on sub-0.05 mm machining while still meeting tactile repeatability.

A control strategy that avoids over-driving, jitter, and mechanical shock, documenting how PWM profiles and sequencing interact with macro tolerances to prevent wear/failure.

Bounded enhancement or major redesign?

Bounded enhancement (B): The current MVP already embodies some tolerance management; enhancing it would involve systematically measuring tolerance impacts, possibly refining slot geometry and cam profiles, and documenting repeatability across multiple printed units.

Required physical advantage:

Demonstrably higher build success and tactile reliability for student-accessible FDM, compared to nearest open-hardware cam projects that often assume high-end printers.[^18]

Experiment:

Fabricate multiple cells with controlled variations in print quality, measure pin travel, misalignment, friction, and failure rates; compare to baseline (e.g., Varada’s module or reference cells).[1][17]

Schedule / component impact:

Feasible in the three-month semester: design-of-experiments, multiple prints, simple metrology (calipers, feel tests). No major component changes.[53][17]

Principal patent risks:

Novelty: moderate risk; prior art addresses cleaning and tolerances but not explicitly macro FDM budgets.[^46]

Obviousness: moderate; macro-scaling and tolerance budgets are common engineering practices.

Verdict: viable B direction if framed tightly around macro-scale, FDM-focused tolerance methodology and evidence.

8.2 Low-Cost Per-Dot Calibration

Nearest prior art: per-pin calibration in EM-l

References

06_Patent_Research_Input_Pack.md - This pack preparesnot performsa later current patent search. Historical repository conclusions below...

Phase2_Report-by-CLaude.md - Prepared by Claude, acting as the Engineering RD IP Review Board synthesis function Inputs Phase 1C ...

Braille display - publication_number: US5453012Aassignee: ROBOTRON PTY LTDabstract: ...between an elevated position ...

Binary information display apparatus - publication_number: US5766014Aassignee: MITSUBISHI MATERIALS CORPORATIONabstract: A binary informa...

SYSTEMS AND METHODS FOR A DYNAMIC BRAILLE DISPLAY - publication_number: US20150206453A1abstract: Embodiments disclosed herein describe systems and meth...

Braille module with compressible pin arrays - publication_number: US8740618B2assignee: TACTILE DISPLAY COROPRATIONabstract: A refreshable tactil...

Electroactive polymer actuator braille cell and braille display - publication_number: US6881063B2abstract: The present invention provides a Braille cell being of com...

Refreshable braille-cell display implemented with shape memory alloys - publication_number: US5685721Aassignee: AMERICAN RESEARCH CORPORATION OF VIRGINIAabstract: A refre...

TACTILE PIXELS - publication_number: EP4049116A1grant_date: 2022-08-31filing_date: 2020-10-21application_number: 2...

Layered electro-magnetic refreshable braille display device and braille reader - publication_number: US11410574B2abstract: The present invention discloses a layered electro-magneti...

ELECTRO MAGNETIC REFRESHABLE BRAILLE READER - publication_number: WO2020106855A1abstract: In certain embodiments devices suitable for use as elec...

Electro magnetic refreshable braille reader - publication_number: US12548467B2abstract: In certain embodiments devices suitable for use as electr...

Modular refreshable braille display system - publication_number: US11915607B2assignee: BRAILLEAZY INCabstract: This specification generally dis...

Capture plate assembly for braille display - publication_number: US12080182B2assignee: TACTILE SOLUTIONS INC, FREEDOM SCIENTIFIC INC. D/B/A VISP...

MOLBED - Modular Low Cost Braille Electronic Display

MagnePins: A Modular, Affordable, and DIY Refreshable Braille and Tactile Display

Phase3C_OpenBraille_Architecture_Report_Final.md - Prepared by Final Engineering Architecture Review Board synthesis of four independent Phase 3C Deep ...

Electromechanical Refreshable Braille Module - The big drawback to refreshable braille devices has always been their cost. The loose rule of estima...

BRAILLE WATCH - publication_number: US20130149674A1assignee: WISCONSIN ALUMNI RESEARCH FOUNDATIONabstract: A Brail...

Braille cell - publication_number: EP471327A1abstract: The present invention discloses a braille cell comprising p...

A COMPLIANT MECHANISM FOR REFRESHABLE BRAILLE DISPLAY USING SHAPE MEMORY ALLOY - publication_number: WO2015189863A2abstract: The present invention describes a refreshable braille d...

DEVICE AND METHOD FOR DISPLAYING BRAILLE AND TACTILE GRAPHICS - publication_number: WO2024174030A1abstract: ...includes an array of braille pins arranged equidista...

LAYERED ELECTROMAGNETIC BRAILLE DISPLAY DEVICE AND BRAILLE READING MACHINE - publication_number: WO2016074170A1abstract: A layered electromagnetic Braille display device and a ...

Actuation mechanism for braille displays - According to the present invention, there is provided an improved refreshable tactile display appara...

BRAILLE LEARNING APPARATUS AND BRAILLE LEARNING METHOD USING THE SAME - publication_number: US20170309203A1assignee: OHFA TECH INCabstract: A braille learning apparatus i...

IP India

A Braille Cell And Assembly For Single Line Braille Display - Abstract: A Braille cell and assembly for single-line Braille display, said cell and assembly compri...

IPIndia Patent Search | Indian Patent Search - IPExcel - IP India Patent search can be performed using Indian Patent Office website. The said website is avai...

Braille display device and method of constructing same - publication_number: US8690576B2assignee: FREEDOM SCIENTIFIC INC, ENHANCED VISIONS SYSTEMS INCabstr...

555 Trade Mark - 555 Trade Mark is a Device Trademark filed on 26 December 2008 with Application_ID 1768210 in West b...

Braille display system - publication_number: US10890993B2assignee: OPTELEC HOLDING B.Vabstract: A Braille display system ca...

A passive and scalable magnetic mechanism for braille cursor, an innovative refreshable braille display

Electromechanical Tactile Braille Cell Assembly - publication_number: US20090035731A1assignee: FREEDOM SCIENTIFIC INC, ENHANCED VISIONS SYSTEMS INCa...

Refreshable Braille Display - Hackaday.io - Of 40 million blind people in the world, only 10% can read and write braille. One of the primary rea...

Braille Support - publication_number: US20080303645A1assignee: APPLE INCabstract: Methods and apparatuses to provide...

Braille support - publication_number: US8135577B2assignee: APPLE INCabstract: Methods and apparatuses to provide imp...

Refreshable Braille Module Using Cam Actuated Mechanism - by Aryan · 2021 · Cited by 5 — The basic concept of cam shafts are used to design the dynamic braill...

A 2D refreshable Braille display based on a stiffness variable polymer and pneumatic actuation - Visual impairments limit a person’s ability to process information such as obstacles, environments, ...

BRAILLE CELL - publication_number: US5226817Aassignee: KGS CORPORATION A CORPORATION OF JAPANabstract: The presen...

Electromechanical tactile cell assembly - publication_number: US7410359B1assignee: FREEDOM SCIENTIFIC INC, ENHANCED VISIONS SYSTEMS INCabstr...

Braille display assembly - publication_number: US7462034B1assignee: FREEDOM SCIENTIFIC INC, ENHANCED VISIONS SYSTEMS INCabstr...

Braille display device and method of constructing same - publication_number: US9424759B2assignee: FREEDOM SCIENTIFIC INC, ENHANCED VISIONS SYSTEMS INCabstr...

BRAILLE DISPLAY DEVICE AND METHOD OF CONSTRUCTING SAME - publication_number: WO2013130534A1abstract: Disclosed is a Braille display device. The device suppo...

ACTIVE BRAILLE TIMEPIECE & RELATED METHODS - publication_number: US20130017516A1abstract: A timepiece adapted for efficient mechanical display o...

Braille module with compressible pin arrays - publication_number: US20090023116A1assignee: TACTILE DISPLAY COROPRATIONabstract: A refreshable ta...

Contaminant-tolerant braille pins - publication_number: US6902403B1assignee: FREEDOM SCIENTIFIC INC, ENHANCED VISIONS SYSTEMS INCabstr...

Apparatus and method utilizing bi-directional relative movement for refreshable tactile display - publication_number: US6692255B2assignee: GOVERNMENT OF THE UNITED STATES OF AMERICA AS REPRESENTED ...

Refreshable Braille Display

Project | Refreshable Braille Display - Project thus far are covered under a patent application filed at The PatentOffice, Chennai, by him o...

Patent - Patent by Assistech

Tactile Display For Visually Impaired People - Abstract: All visually impaired people use braille or any audio books to read something, but each ti...

Patent Public Search - A powerful, flexible web-based patent search application that improves the overall patent searching ...

Phase3C_OpenBraille_Memory_Final.md - Version 1.0 Status COMPLETE Methodology Version Phase 3C --- TITLE Project mC - Phase 3C Memory Open...
