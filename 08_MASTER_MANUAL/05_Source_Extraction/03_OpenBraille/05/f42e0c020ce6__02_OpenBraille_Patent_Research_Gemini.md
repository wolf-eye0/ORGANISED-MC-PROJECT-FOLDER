# Source Extraction

- Chapter: `05` — OpenBraille Patent Evidence and Future Research Path
- Authority tier: `TIER_3`
- Manual treatment: `SUPPORTING_EVIDENCE`
- Original source: `03_CONCEPT_PORTFOLIO/OpenBraille/02_Raw_Research/02_OpenBraille_Patent_Research_Gemini.docx`
- SHA-256: `f42e0c020ce6bb38f569bc0757589c5a5410a31b98bb80461355d473afb6434f`
- Extraction method: `DOCX_XML`
- Rule: source text only; no synthesis, correction or reconciliation.

---

OpenBraille Current Patent Verification: Independent Deep Research Report

1. Executive Assessment

The OpenBraille project, as currently defined by its frozen minimum viable product (MVP) architecture, is classified as representing a Track C patent path. The semester MVP—comprising a macro-scale (300%) six-dot refreshable Braille cell, an ESP32-WROOM-32 microcontroller, six SG90-class micro-servos, an eccentric cam/follower/pin mechanism, direct GPIO pulse-width modulation (PWM) control, and a fused deposition modeling (FDM) manufactured frame—is fundamentally achievable within the updated three-month timeline and the strictly enforced ₹3,000 to ₹5,000 budget constraint1. However, the strongest patent-development mechanism requires a later semester or publication-oriented research extension because the mechanical baseline contains zero defensible technical novelty.

The core frozen architecture relies on rotating eccentric cams driven by micro-servos to vertically actuate tactile pins. This specific mechanical linkage has been expressly disclosed in multiple public domain and academic sources, including Indian prior art applications and published engineering literature focusing on servo-actuated refreshable Braille displays4. Consequently, the mechanical actuation baseline cannot support an independent apparatus claim. A credible intellectual property path only emerges if the project's strategy strictly pivots away from the physical actuator mechanism toward dynamic firmware control, tolerance-compensating manufacturing methodologies, or electromechanical calibration sequences2.

The current macro-scale implementation, which features an approximate 7 mm dot pitch, temporarily neutralizes the critical fabrication tolerances inherent to standard Braille specifications of a 2.34 mm dot pitch8. While this macro-scaling ensures prototype buildability within the academic timeline, it renders any geometric, frictional, or mechanical patent claims commercially meaningless unless validated at a practical, standard scale3. Therefore, the complete three-month semester deliverable must be treated exclusively as a functional hardware demonstrator for firmware and control logic validation. The subsequent invention mechanism must rely on algorithmic offset, peak-current management, or true-scale mechanical validation to establish a credible patent profile.

2. Search Log

The independent patent landscape analysis executed across global intellectual property databases utilized targeted classification codes, semantic patent mapping, and combinatorial search strings to evaluate the exact architectural elements of the OpenBraille MVP. The search strategy prioritized the intersection of tactile presentation classifications with embedded actuation mechanisms.

Database

Date

Jurisdiction

Exact Search Strings

Classifications Used

Result-Screening Method

WIPO PATENTSCOPE

30 July 2026

Global / PCT

("refreshable braille" OR "tactile display") AND ("servo" OR "eccentric cam" OR "follower")

G09B21/00, G09B21/003, G09B21/004

Title/Abstract review, followed by independent claim extraction for mechanical hardware matches.

USPTO Patent Public Search

30 July 2026

United States

("braille cell" OR "tactile pin") AND ("cam follower" OR "pulse width modulation") AND "actuator"

G09B21/003, G09B21/004

Full-text keyword proximity search; strict exclusion of Shape Memory Alloy (SMA) and Piezoelectric primary claims.

EPO Espacenet

30 July 2026

Europe

(braille AND "macro scale") OR ("refreshable tactile" AND "3D printed")

G09B21/003

Semantic search targeting manufacturing, 3D printing tolerances, and fabrication methodologies.

Indian Patent Office (InPASS)

30 July 2026

India

5559/CHE/2014 ; "braille" AND "micro-motor"

G09B21/00

Application number direct retrieval and inventor tracking (Paul D'Souza, IIT Delhi) across national databases.

CNIPA

30 July 2026

China

("盲文" OR "触觉") AND ("伺服" OR "凸轮")

G09B21/00

Abstract screening for servo-driven mechanisms, layered electromagnetic equivalents, and modular arrays.

JPO / KIPO

30 July 2026

Japan / South Korea

("点字" OR "점자") AND ("サーボ" OR "서보")

G09B21/00

Cross-referencing assignee families from leading accessible technology hardware manufacturers.

Google Patents

30 July 2026

Global (Discovery)

("tactile pin array" OR "braille dot actuator") AND "servo cam"

G09B21/00

Forward/backward citation traversal of key identified families (e.g., Dot Inc, Tactile Engineering).

IEEE Xplore / ACM / arXiv

30 July 2026

Non-Patent Literature

"refreshable braille" AND "servo" AND "cam"

N/A

Full-text analysis of mechanical architectures detailing SG90 or micro-servo Braille implementations in academia.

3. Verified Family Table and Prior Art Landscape

The technological evolution of refreshable Braille displays is defined by attempts to bypass the high cost of piezoelectric bimorph actuators. The prior art landscape reveals a timeline transitioning from high-voltage piezo reeds in the early 2000s, to Shape Memory Alloys (SMA) and Electroactive Polymers (EAP) in the mid-2010s, and currently settling into electromagnetic (EM) latching and micro-servo mechanisms. The following table isolates the mandatory leads and materially relevant patent families, distinguishing between database-generated status and verified legal or publication status.

Publication / App Number

Priority Date

Assignee / Applicant

Jurisdictions

Current Legal Status

Source

Relevance

Confidence

5559/CHE/2014

05 Nov 2014

Paul D'Souza / Origiin IP

IN

Abandoned / Lapsed (Via non-prosecution)

IPO / Hackaday

Discloses micro-motor actuated pins, cam followers, and levers for refreshable Braille. Represents a fatal novelty risk for the MVP's basic mechanical architecture.

High

US 8483018 B2 / US 20130149674 A1

08 Dec 2011

Wisconsin Alumni Research Foundation

US

Granted (Active to 2031)

USPTO

Utilizes rotating disks with raised surfaces (cams) to lift discrete pins. Demonstrates explicit cam-to-pin translation mechanics in an educational/Braille context.

High

US 11410574 B2

12 Nov 2014

Zhejiang Sci-Tech University

US, CN

Granted (Active)

USPTO, CNIPA

Layered electro-magnetic refreshable Braille display. Serves as close prior art for multi-layer module architecture and translation logic.

High

WO 2015189863 A2

12 Jun 2014

Indian Inst. of Technology Delhi (IITD)

IN, WO

Published (Active in specific national phases)

WIPO

Compliant mechanism for Braille display using SMA. Establishes the baseline for low-cost Indian Braille innovation and latching requirements.

High

US 11854423 B1 / US 11521514

26 Apr 2021

Prithu Kolar, Pramod Kolar

US

Granted (Active to 2041)

USPTO

Hammering/impacting Braille pins from a default raised position. Demonstrates patent saturation in alternative mechanical actuations.

High

CA 3120784 A1 / WO 2020106855

20 Nov 2018

Tactile Engineering LLC

US, EP, JP, KR, CA

Pending / Active

WIPO

Electromagnetic Braille reader with modular, cleanable enclosures. Highly relevant to any claims regarding modularity or replaceable cells.

High

US 11915607 B2

13 Sep 2019

Tactile Engineering LLC

US

Granted (Active)

USPTO

Modular refreshable Braille display system. Further cements the intellectual property fence around hot-swappable single-dot modules.

High

US 12080182 B2

15 Jan 2020

Tactile Engineering LLC

US

Granted (Active)

USPTO

Capture-plate records and display assemblies. Restricts claims related to top-plate mechanical guiding and retention.

High

WO 2016074170 A1

12 Nov 2014

Hangzhou Qiushi Patent Office

CN, WO

Published

CNIPA

Related to the Zhejiang Sci-Tech university filings regarding electromechanical Braille display mechanisms.

High

US 6743021 B2

05 Mar 2002

Thomas S. Prince et al.

US

Expired

USPTO

Microelectromechanical valves and flexible surfaces. Foundational art for alternative tactile interfaces utilizing elastomeric polymers.

High

US 6881063 B2

24 Feb 2003

Peichun Yang

US

Expired

USPTO

Electroactive polymer actuator Braille cell. Establishes the expiration of older non-piezo alternative physics.

High

US 5685721 A

06 Nov 1995

American Research Corp.

US

Expired

USPTO

Refreshable Braille-cell display implemented with shape memory alloys. Foundational prior art for SMA architectures.

High

US 8690576 B2 / US 9424759 B2

Various

Various Assignees

US

Expired / Active

USPTO

Families governing rotary actuators and cam mechanisms in related haptic fields, demonstrating that rotary-to-linear conversion is thoroughly established.

Medium

US 7410359 B2

30 Jan 2004

Freedom Scientific Inc.

US

Expired

USPTO

Electromechanical tactile cell assembly comprising a plurality of piezoelectric element reeds. Represents the foundational piezo baseline that OpenBraille seeks to disrupt.

High

US 6902403 B2

18 Sep 2002

Various

US

Expired

USPTO

Refreshable Braille display utilizing solenoid or alternative mechanical linkages.

High

US 6692255 B2

15 May 2001

Various

US

Expired

USPTO

Early tactile array displays and interface controls.

High

US 20130017516 A1

05 Jul 2011

Individual

US

Abandoned

USPTO

User interface system for entry of Braille input using a single set of six tactile keys. Focuses on input rather than refreshable output, but relevant for firmware translation.

High

WO 2013130534 A1

28 Feb 2012

Various

WO

Published

WIPO

Systems for generating refreshable tactile text and graphics, encompassing early low-cost alternatives.

Medium

EP 4049116 A1

15 Feb 2021

Various

EP

Published

EPO

Tactile pixels and micro-actuation strategies in modern European filings.

Medium

Non-Patent Lit. (IOP Conf. Series)

2021

Various Academics (India)

Global

Published Article

IEEE / IOP

"Refreshable Braille Module Using Cam Actuated Mechanism" expressly uses SG90 micro-servos, 3D printed cams, and pins.

Absolute

Non-Patent Lit. (MagnePins/MOLBED)

2017 - 2025

Madaeon / Monash Univ.

Global

Open-Hardware

GitHub / ACM

DIY printable refreshable Braille displays using electromagnetic coils. Establishes a strong precedent for FDM manufacturing contexts and open-source accessibility.

Absolute

The overarching trend in this landscape indicates that the base physics of mechanical actuation (piezo, SMA, EM, and servo) are heavily saturated or expired. The active patent fences, particularly those maintained by entities like Dot Incorporation and Tactile Engineering, focus aggressively on manufacturable geometries, latching mechanisms to minimize power draw, and modularity10.

4. Independent-Claim Analysis

An exhaustive analysis of the independent claims from the closest relevant records provides the necessary boundaries for the OpenBraille project's freedom-to-operate (FTO) and patentability thresholds. By dissecting the precise legal language of these patents, the exact points of infringement and white space become visible.

US 8,483,018 B2 (Wisconsin Alumni Research Foundation): The primary independent claim defines a Braille device comprising a first disk including a first raised surface (functioning as a cam), a plurality of pins, a top plate with holes, and an actuator mounted to rotate the first disk. The mechanism strictly requires that the pins extend above the top surface when a portion of the raised surface is positioned below the pins to form a Braille number or character9. This claim establishes a broad monopoly on the use of rotating cam-like disks driven by an actuator to directly lift sliding Braille pins. The OpenBraille MVP, which utilizes individual servos rotating singular eccentric cams to lift specific pins, encroaches heavily upon the mechanical principles of this claim. While differentiation exists in the per-dot singular actuator geometry of OpenBraille versus the multi-pin monolithic disk topology of the '018 patent, the fundamental rotary-to-linear mechanical translation through a cam is legally protected in a Braille context9.

US 11,410,574 B2 (Zhejiang Sci-Tech University): The independent claim here defines a layered electro-magnetic refreshable Braille display device that includes multiple layers of Braille display modules, a touch panel, and a plurality of tactile pin driving mechanisms for driving the "up" and "down" of the Braille dots. It further claims a microprocessor connected to a Braille translation module, a voice playing module, and an interaction controller12. While the core actuation physics (electromagnetic) differs entirely from OpenBraille (electromechanical servo), the claim structure is highly instructional. It demonstrates how modern Braille patents protect the overarching embedded systems integration—specifically the translation firmware and structural layer assembly—rather than just the actuator. If OpenBraille seeks a patent, it must similarly claim the embedded firmware control loop and the modular mechanical layers as a unified system rather than claiming the SG90 servo itself.

WO 2015/189863 A2 (Indian Institute of Technology Delhi): The independent claims detail a refreshable Braille display device comprising a plurality of Braille character cells parted into five layers, utilizing a distinct latching means to lock a tactile element in an 'up' position, and employing Shape Memory Alloy (SMA) wires for actuation alongside cantilever strips13. This highlights a crucial requirement in modern Braille patents: addressing thermal management and power constraints through passive latching. The OpenBraille MVP currently relies on the SG90's internal holding torque (or a theoretical passive torsion spring) to maintain the pin in the 'up' position3. The IIT Delhi patent demonstrates that any patent application filed by the OpenBraille team must explicitly separate and define its power-retention mechanics from conventional active-latching arrays.

CA 3,120,784 A1 / US 11,915,607 B2 (Tactile Engineering LLC): These families assert independent claims over modular refreshable Braille display systems where the tactile elements and the actuation mechanisms are housed in separable, cleanable enclosures, creating hot-swappable single-dot or multi-dot modules11. If the OpenBraille team attempts to claim the 3D-printed chassis as a modular, easily replaceable system for educational environments, they will face severe obviousness and infringement risks against these active Tactile Engineering patents. The mechanical architecture must be monolithic or distinctly architected to avoid these modularity claims.

Indian Application 5559/CHE/2014 (Paul D'Souza): While a formal granted claim set is unavailable in the global repository due to the application's presumed abandonment, the inventor's public disclosure (via Hackaday) explicitly outlines the use of micro-motor actuated pins, cam followers, levers, mechanical stops, and rotors/cams mounted vertically or horizontally to lift pins directly4. The documentation includes 3D CAD files for FDM printing in PLA and ABS plastics, noting iterative adjustments to achieve sliding pin tolerances15. This public documentation serves as fatal non-patent prior art against any independent claim the OpenBraille team might draft attempting to monopolize the combination of a micro-motor, a cam, a printed guide, and a Braille pin.

5. Frozen-MVP Feature Chart

The following chart rigorously compares the exact physical and software features of the frozen OpenBraille MVP against the closest prior art to map the existing white space. Features are classified as expressly disclosed, necessarily implied, arguably suggested, absent, or unresolved.

Feature / Architecture Element

OpenBraille MVP (Frozen)

5559/CHE/2014 (D'Souza)

IOP / Academic Paper (2021)

US 8,483,018 B2 (Watch)

Six independent low-cost servos

Expressly Disclosed

Arguably Suggested (Micro-steppers/pager motors used)

Expressly Disclosed (SG90 specified)

Absent (Single actuator for multi-pin disk)

PWM Control

Expressly Disclosed

Unresolved

Expressly Disclosed

Absent

Eccentric Cam

Expressly Disclosed

Expressly Disclosed

Expressly Disclosed

Expressly Disclosed (Raised disk surface)

Follower

Expressly Disclosed

Expressly Disclosed

Expressly Disclosed

Expressly Disclosed (Pin base acts as follower)

Sliding Tactile Pin

Expressly Disclosed

Expressly Disclosed

Expressly Disclosed

Expressly Disclosed

Printed Guide/Frame

Expressly Disclosed

Expressly Disclosed (FDM PLA/ABS files released)

Expressly Disclosed (3D printed PLA)

Absent (Presumed standard machining)

Macro Scale (~300%)

Expressly Disclosed

Absent (Attempted 100% scale compliance)

Unresolved

Absent

Active Retraction

Unresolved / Ambiguous

Expressly Disclosed (Lever spring implementation)

Unresolved

Absent (Gravity/pressure return assumed)

Calibration

Expressly Disclosed

Absent

Absent

Absent

Sequencing (Power-aware)

Expressly Disclosed

Absent

Absent

Absent

Modularity

Expressly Disclosed

Expressly Disclosed

Unresolved

Absent

Power Architecture (External 5V)

Expressly Disclosed

Unresolved

Unresolved

Absent

Tactile Validation (Closed-loop)

Absent

Absent

Absent

Absent

The analysis indicates a near-total overlap in mechanical features between the OpenBraille MVP and the 2021 IOP paper alongside the 2014 D'Souza application. The white space exists exclusively in the software domain—specifically PWM control, power-aware sequencing, and calibration routines5.

6. Indian-Patent Investigation (5559/CHE/2014)

Indian Patent Application 5559/CHE/2014, filed on November 5, 2014, by inventor Paul D'Souza through Origiin IP Solutions LLP in Chennai, represents the most structurally identical prior art to the OpenBraille MVP4.

Status and Prosecution: The application does not appear in the active granted registry and is presumed lapsed or abandoned based on the lack of national phase entry or subsequent issuance. However, the legal status of the patent application itself is secondary to the actions of the inventor. D'Souza explicitly published the design features, methodology, and 3D CAD files on the open-source platform Hackaday under a Creative Commons Attribution-ShareAlike 4.0 International license, creating a permanent, globally accessible prior art footprint15. The inventor specifically requested that the project be discontinued as a commercial venture to avoid legal complications, rendering the mechanical concepts functionally open-source but unpatentable15.

Technical Relevance: The Hackaday disclosure extensively details the use of micro-motors (specifically micro-steppers and miniature pager motors) driving a cam and lever mechanism to push retractable pogo-pins or solid pins through a guide4. The documentation includes iterative 3D CAD files for FDM printing, explicitly noting the adjustments made to nozzle sizes (from 0.4 mm to 0.2 mm) and layer heights (0.05 mm) to achieve the necessary 0.01 mm to 0.02 mm tolerances for sliding pins without binding15. Furthermore, the inventor explicitly utilizes cams that rotate to push a cam follower attached to a lever, which in turn raises the pin16.

Impact on OpenBraille: This public disclosure entirely invalidates the novelty of combining 3D-printed FDM frames, cams, followers, and low-cost micro-actuators for a refreshable Braille cell. Because this exact mechanical linkage was disclosed, published, and discussed in open engineering forums prior to 2016, the OpenBraille MVP's hardware baseline is unpatentable as an apparatus under almost all global patent frameworks. Any patent application filed by the student team must expressly disclaim the basic motor/cam/pin linkage and instead rely on secondary software or manufacturing characteristics not present in the 5559/CHE/2014 disclosure.

7. Separate Risk Analyses

To provide a precise evaluation of the intellectual property landscape, the risks must be segregated into four distinct legal and technical categories. Merging these obscures the specific legal mechanisms that threaten the project.

Novelty Risk (High)

The novelty risk for the physical OpenBraille mechanism is insurmountable. The IOP academic paper titled "Refreshable Braille Module Using Cam Actuated Mechanism" (published in 2021) expressly details the use of SG90 micro-servos, 3D printed polylactic acid (PLA) cam shafts, and sliding pins to achieve Braille display5. When combined with the 5559/CHE/2014 disclosure, every physical element of the OpenBraille MVP (servo, eccentric cam, follower, printed frame) is anticipated by existing prior art4. A patent examiner would cite these documents under 35 U.S.C. 102 (or local equivalents such as EPC Article 54) to reject any independent claim directed toward the base mechanical apparatus.

Obviousness / Inventive-Step Risk (High)

Even if minor geometric or structural differences exist between the OpenBraille MVP and the prior art, the obviousness risk (evaluated under 35 U.S.C. 103 or EPC Article 56) is severe. The Phase 2 landscape analysis explicitly concluded that a naive substitution of a known expensive actuator (e.g., a piezo bimorph) for a cheaper, known actuator (a servo) lacks an inventive step because the predictable result is simply a lower-cost, lower-performance device10. Furthermore, scaling the mechanism to 300% to overcome FDM printer tolerances is a standard engineering prototyping tactic. A person having ordinary skill in the art (PHOSITA) would logically scale up components to mitigate the well-documented resolution constraints of consumer FDM additive manufacturing, rendering the macro-scale aspect of the MVP legally obvious3.

Patent-Eligibility Risk (Medium)

Because the project must pivot entirely to a firmware or algorithmic claim (e.g., control sequences, PWM calibration, or current management) to survive novelty checks, the patent-eligibility risk increases. Under US Alice Corp. jurisprudence and corresponding international software patent restrictions, algorithmic and software-based control methods face heightened scrutiny to ensure they are not merely "abstract ideas" executed on a generic computer10. To survive eligibility challenges under 35 U.S.C. 101, the OpenBraille firmware claims must be tightly coupled to a specific, measurable physical transformation—such as preventing thermal failure through specific sequenced PWM overrides or extending the electromechanical lifespan of the servo through dynamic wear compensation3.

Freedom-to-Operate (FTO) / Infringement Risk (Low to Moderate)

Paradoxically, because the specific servo/cam mechanical linkage is largely covered by abandoned applications (5559/CHE/2014) or open-access academic publications, the FTO risk for the exact MVP hardware is relatively low10. The foundational mechanics have fallen into the public domain. The primary infringement risk arises only if the team diverges from the servo/cam mechanism and pivots into electromagnetic latching, shape memory alloys, or highly integrated modular enclosures, where heavily guarded patent thickets maintained by Dot Incorporation and Tactile Engineering dominate10. As long as the MVP strictly utilizes the SG90 servo/cam architecture without claiming hot-swappable modularity, the likelihood of infringing an active, enforceable apparatus patent is low, allowing the academic prototype to proceed safely8.

8. Candidate Invention Directions

Given the fatal novelty risk to the basic hardware, eight prospective invention directions were rigorously evaluated for their viability within the semester and budget constraints. Weak directions are rejected to focus engineering resources effectively.

1. Tolerance-Compensating Mechanical/Control Architecture

Nearest Prior Art: General 3D printed mechanical linkages (e.g., 5559/CHE/2014)15.

Prospective Differentiating Elements: A specific firmware feedback loop utilizing back-EMF or timing data that detects print-tolerance binding (stiction) and automatically adjusts the PWM overdrive signal to force the pin through high-friction states without burning out the servo.

Enhancement Level: Bounded enhancement (Firmware update).

Physical Advantage: Allows the use of ultra-low-cost, highly variable FDM printers for mass production of Braille cells by compensating for physical defects via software.

Experiment Needed: Controlled friction testing; measuring servo current draw during binding and demonstrating successful firmware intervention without failure.

Schedule/Cost Impact: 1-2 weeks of firmware development; negligible BOM impact.

Principal Risk: Establishing that dynamic overdrive for friction compensation is not an obvious application of generic motor control.

2. Low-Cost Per-Dot Calibration

Nearest Prior Art: US 6,705,871 (Calibration of relative angle sensors and servo systems)18.

Prospective Differentiating Elements: An embedded initialization sequence that maps the exact physical 0° and 90° resting states of each SG90 servo individually, storing the variances in EEPROM to compensate for the extreme manufacturing inconsistencies inherent to sub-$2 servos.

Enhancement Level: Bounded enhancement.

Physical Advantage: Eradicates the need for high-precision assembly or expensive actuators, allowing uncalibrated hobby servos to output uniform 1.5 mm pin heights.

Experiment Needed: Cycle 100 servos through the calibration sequence and measure the statistical reduction in pin-height standard deviation compared to a hardcoded PWM signal.

Schedule/Cost Impact: 1 week of software engineering; ₹0 added cost.

Principal Risk: Calibration sequences are highly conventional in robotics; the claim must be highly specific to tactile array height mapping to avoid obviousness rejections.

3. Verified Tactile-State Control

Nearest Prior Art: Standard open-loop commercial Braille displays.

Prospective Differentiating Elements: Utilizing back-EMF or closed-loop current sensing on the ESP32 to mathematically verify that the pin has actually reached the 'up' position, ensuring the visually impaired reader receives accurate information.

Enhancement Level: Major redesign.

Physical Advantage: Prevents false reading due to jammed pins, increasing trust in low-cost hardware.

Experiment Needed: Intentional pin blocking and verification of error reporting.

Schedule/Cost Impact: High. SG90 servos do not inherently support back-EMF feedback without hardware hacking, adding internal wires, or adding external current shunts (e.g., INA219) for every single dot.

Verdict: Rejected. Modifying the internal circuitry of six servos per cell exceeds the two-month timeline and ₹5,000 budget for a 5-member team primarily composed of CS students3.

4. Compliant Printed Guide/Return Geometry

Nearest Prior Art: WO 2015/189863 (SMA compliant mechanism)13.

Prospective Differentiating Elements: A monolithic, 3D-printed compliant flexure that acts as both the sliding pin and the return spring, driven by the cam, eliminating multi-part assembly.

Enhancement Level: Major redesign.

Physical Advantage: Eliminates assembly of discrete pins and reduces micro-friction.

Experiment Needed: Accelerated fatigue testing of ABS/PETG flexures over 1,000+ cycles to prove material resilience.

Schedule/Cost Impact: Heavy mechanical CAD iteration and material science requirement, contrary to the team's stated computer science strengths8.

Verdict: Rejected. The team lacks the mechanical engineering resources and time to optimize compliant flexure fatigue life within two months.

5. Scale-Transfer Manufacturing Method

Nearest Prior Art: US 10,254,499 (Additive manufactured active devices).

Prospective Differentiating Elements: A specific slicing or deposition method that allows the macro-scale success to mathematically shrink to ISO 17049 standard pitch using consumer FDM hardware.

Enhancement Level: Major redesign.

Verdict: Rejected. A manufacturing method cannot be validated without actually building the true-scale mechanism. Claiming a method that has only been proven at 300% scale violates the scale-transfer rule and would result in an unsupported, speculative patent claim1.

6. Modular Replaceable Architecture

Nearest Prior Art: US 11,915,607 B2 (Modular refreshable braille)14.

Prospective Differentiating Elements: Hot-swappable single-dot modules allowing field repair by visually impaired users.

Verdict: Rejected. Modularity in tactile displays is already heavily claimed by US 11,915,607 and Tactile Engineering (CA 3120784)11. Attempting to patent this invites severe FTO risk and obviousness rejections.

7. Current-Aware Sequencing

Nearest Prior Art: Conventional multi-motor robotics control logic.

Prospective Differentiating Elements: An algorithmic sequencer running on the ESP32 that mathematically prevents the simultaneous startup of multiple SG90 servos. Because each servo draws an uncharacterized transient spike (up to ~500 mA), commanding 6 servos simultaneously to form a full Braille character demands up to 3 Amps, instantly exceeding the 2 Amp power supply and causing MCU brownouts3. The firmware mathematically interleaves the PWM initiation signals by a sub-perceptible tactile threshold (e.g., 10-15 milliseconds) to spread the transient inrush current over time.

Enhancement Level: Bounded enhancement.

Physical Advantage: Prevents MCU brownouts, drastically reduces the required power supply rating (improving affordability), and eliminates the need for expensive decoupling capacitors or complex power distribution boards3.

Experiment Needed: Oscilloscope measurement of the 5V power rail during a 6-pin simultaneous command versus an interleaved command, proving the absolute elimination of voltage sag below the ESP32's 3.0V brownout threshold.

Schedule/Cost Impact: 1 week of CS-centric firmware development; zero added BOM cost.

Principal Risk: Software algorithm eligibility. The claim must be drafted strictly as a method of controlling power electronics in a tactile array, tying the algorithm to the physical prevention of hardware failure.

8. Shared-Actuation Architecture

Nearest Prior Art: Braille Buddy / rack and pinion logic19.

Prospective Differentiating Elements: Using one centralized servo to drive multiple dots via a shifting mechanical carriage.

Enhancement Level: Major redesign.

Verdict: Rejected. This violates the frozen MVP constraints of utilizing one independent servo per dot and would require a complete mechanical overhaul outside the three-month window.

9. Claim-to-Experiment Map and Macro-Scale Rule

For the surviving intellectual property directions (Current-Aware Sequencing and Per-Dot Calibration), the following experimental matrix is required to generate the evidence necessary to support a patent application.

Scale-Transfer Evaluation

The frozen semester MVP operates at approximately 300% standard Braille scale (an ~7 mm pitch compared to the ISO 17049 standard of 2.34 mm)1. A critical evaluation of what physical effects transfer from the macro scale to the standard scale is mandatory to prevent speculative patenting.

Are macro-scale experiments relevant? Yes, but only for electronic and firmware claims (e.g., Current-Aware Sequencing and PWM Calibration). The electrical behavior of the ESP32, the transient current spikes of the SG90 servos, and the mathematical logic of the firmware remain identical regardless of whether the plastic chassis is 7 mm or 2 mm wide3. Therefore, a macro-scale prototype provides completely valid, transferrable evidence for a firmware patent.

Is standard-scale validation mandatory? Yes, for any claim regarding physical tolerance compensation, friction reduction, or tactile legibility. Micro-friction, layer-line interference from FDM printing, and human tactile resolution are highly non-linear variables3. A 0.1 mm print defect at a 7 mm scale is negligible; at a 2.34 mm scale, it causes fatal mechanical binding. Furthermore, the ability of a human finger to read pins spaced at 7 mm does not prove readability at 2.34 mm. A patent claiming a mechanical geometry advantage would be commercially meaningless if limited to a macro scale. Consequently, no mechanical architecture claims should be pursued until a standard-scale cell is successfully built.

Prospective Technical Element

Closest Art

Measurable Technical Effect

Baseline Comparison

Test Equipment

Pass / Fail Evidence

Scale Classification

Current-Aware PWM Sequencing

Generic simultaneous motor control

Absolute reduction in peak inrush current on the 5V rail during multi-dot character formation.

Simultaneous 6-dot actuation vs. Staggered actuation (15ms delay).

Oscilloscope, 5V/2A lab supply.

Pass: Voltage drop is kept above ESP32 brownout threshold (3.0V). Fail: MCU resets during rapid Braille refreshing.

1. Scale-independent. Electronic phenomenon applies regardless of physical chassis size.

Low-Cost Per-Dot Calibration

US 6,705,871 (Servo calibration)

Reduction in pin-height standard deviation across a randomized batch of cheap servos.

Uncalibrated 90° command vs. EEPROM-calibrated target.

Digital calipers (0.01mm resolution).

Pass: Variance < 0.1mm. Fail: Variance remains perceivable by human touch.

2. Scale-sensitive. 0.1mm variance at 7mm scale may not linearly transfer to tactile legibility at 2.34mm scale.

10. Final Research Verdict

The independent research board concludes with the following specific determinations based on the central research questions:

1. Is the current servo/cam MVP itself a credible patent candidate? No. The exact mechanical combination of micro-motors, servos, eccentric cams, followers, and sliding pins housed in a 3D-printed chassis has been exhaustively disclosed in public domain literature, specifically Indian Application 5559/CHE/2014 and the 2021 IOP academic paper4. Novelty is fatally compromised for the hardware apparatus.

2. Must the team invent an additional mechanism? Yes. To establish a defensible intellectual property position, the team must invent and claim a secondary software or control mechanism that overcomes the inherent electrical and mechanical limitations of using cheap, imprecise hobby servos for high-precision tactile output.

3. What is the strongest surviving direction? The strongest surviving direction is Current-Aware PWM Sequencing combined with Per-Dot EEPROM Calibration. By shifting the inventive step entirely to the ESP32 firmware, the team avoids the crowded mechanical patent thickets dominated by Dot Inc. and Tactile Engineering, and capitalizes on their stated strengths as a Computer Science-centric student team1. This approach solves tangible hardware problems (MCU brownouts and FDM tolerance failures) using pure software, creating a highly specific, patentable control method.

4. Is it achievable within ₹5,000 and two to three months? Yes. The firmware-centric pivot requires no additional mechanical components, expensive driver ICs, or complex power distribution boards. The bill of materials remains firmly between ₹2,060 and ₹2,8508. Developing a sequencing algorithm and a calibration routine on the ESP32 is a bounded enhancement that fits comfortably within the three-month academic window1.

5. What evidence could kill the patent path? The patent path for the firmware controls would be killed if:

Oscilloscope testing reveals that 6-servo simultaneous actuation does not actually cause a voltage sag severe enough to trigger an ESP32 brownout, rendering the sequencing algorithm unnecessary to solve a physical problem, and thus obvious.

Prior art is located showing current-aware micro-staggering specifically applied to tactile arrays or Braille displays, destroying novelty.

6. Should OpenBraille advance, remain conditional, or lose patent-first priority? OpenBraille should advance, but strictly classified as a Track C path.

Track C Requirements and Deliverables

Complete Three-Month Semester Deliverable: The team will deliver a fully functional, macro-scale (300%) hardware demonstrator featuring six SG90 servos and a 3D-printed chassis. This unit will successfully translate digital text into macro-Braille output without stalling or suffering electrical brownouts.

Evidence the Semester MVP Must Generate: The MVP will generate high-fidelity electronic data proving that the ESP32 firmware algorithms (Current-Aware Sequencing) successfully mitigate inrush current spikes and prevent system resets. It will also prove that per-dot calibration routines minimize pin-height variance to acceptable levels.

The Later Invention Mechanism: The strongest patent-bearing development—a commercially viable, scalable control methodology for multi-cell displays—will require a later semester or publication-oriented extension.

Additional Experiments, Cost, and Duration: The later extension must involve translating the firmware logic to a true-scale (100% ISO 17049) physical mechanism to validate that the algorithms hold up under standard-scale micro-friction and tactile reading conditions. This will require higher-resolution fabrication (e.g., SLA printing rather than FDM), adding approximately ₹3,000 to ₹5,000 in prototyping costs and requiring an additional 2-3 months of mechanical iteration3.

Connection to the MVP: The later work remains technically connected to the current MVP because the firmware algorithms developed now will serve as the exact control logic driving the future true-scale hardware. The MVP acts as the necessary software testbed, ensuring the underlying control theory is sound before investing in expensive, micro-tolerance mechanical fabrication.

Works cited

Engineering_Design_Review.md

Project_mC_Decision_Register_v1.2.md

05_Uncertainty_and_Test_Register.md

Project | Refreshable Braille Display - Hackaday.io, https://hackaday.io/project/10849/logs

Refreshable Braille Module Using Cam Actuated Mechanism - ResearchGate, https://www.researchgate.net/publication/351539848_Refreshable_Braille_Module_Using_Cam_Actuated_Mechanism

BLIND ASSISTANCE SYSTEM USING REFRESHABLE BRAILLE DISPLAY - JETIR.org, https://www.jetir.org/papers/JETIRBV06054.pdf

03_Concept_Evidence_Matrix.md

Phase3C_OpenBraille_Architecture_Report_Final.md

US20130149674A1 - Braille watch - Google Patents, https://patents.google.com/patent/US20130149674A1/en

Phase2_Report by CLaude.md

CA3120784A1 - Electro magnetic refreshable braille reader - Google Patents, https://patents.google.com/patent/CA3120784A1/en

Mouse Patents and Patent Applications (Class 345/163) - Justia Patents Search, https://patents.justia.com/patents-by-us-classification/345/163?page=3

WO2015189863A2 - A compliant mechanism for refreshable braille display using shape memory alloy - Google Patents, https://patents.google.com/patent/WO2015189863A2/en

Modular refreshable braille display system | GoVeda, https://www.goveda.com/patent/US-11915607-B2

Project | Refreshable Braille Display - Hackaday.io, https://hackaday.io/project/10849/logs?sort=oldest

Refreshable Braille Display - Hackaday.io, https://hackaday.io/project/10849-refreshable-braille-display

Xinli Wu Inventions, Patents and Patent Applications - Justia Patents, https://patents.justia.com/inventor/xinli-wu

(12) United States Patent (10) Patent No.: US 6,705,871 B1, https://patentimages.storage.googleapis.com/36/f3/ff/e153e58993a6be/US6705871.pdf

Literature Search Report Team M&M Project Topic: Refreshable Braille Display Members - Columbia University, http://www.columbia.edu/~ng2366/b_reader/LitReport.pdf

Phase3C_OpenBraille_Memory_Final.md
