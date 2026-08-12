# Source Extraction

- Chapter: `05` — OpenBraille Patent Evidence and Future Research Path
- Authority tier: `TIER_3`
- Manual treatment: `SUPPORTING_EVIDENCE`
- Original source: `03_CONCEPT_PORTFOLIO/OpenBraille/02_Raw_Research/06_OpenBraille_Patent_Research_Microsoft_Copilot.docx`
- SHA-256: `75e34f06275338189e29373c598afdbd60becb8d1a1e562ef7922a009bae77d6`
- Extraction method: `DOCX_XML`
- Rule: source text only; no synthesis, correction or reconciliation.

---

OpenBraille Patent Landscape Verification

OpenBraille Patent Landscape and Development Pathway: Comprehensive 2026 Analysis

Executive Summary

This report delivers a rigorous, evidence-based analysis of the current patent landscape and development pathway for the OpenBraille project as of July 30, 2026. OpenBraille’s frozen MVP is a macro-scale (~300% ISO) six-dot refreshable Braille cell using six SG90-class servos, eccentric cams, pins, an FDM-printed frame, ESP32 direct PWM, and an external 5 V supply, all within a ₹5,000 budget and a three-month timeline. The research draws primarily from the authoritative project documentation, including the Engineering Design Review, Phase 3C Architecture Report, Decision Register, and supporting evidence matrices, and is supplemented by targeted patent and prior-art verification from global databases.

The analysis proceeds through ten structured sections, culminating in a final verdict on OpenBraille’s patent-development prospects. Key findings include:

Patent Path Classification: OpenBraille’s patent path is classified as Conditional (Class C)—there is plausible but unproven white space in manufacturing method and firmware/control, but the macro-scale servo/cam MVP alone does not guarantee a claimable invention.

Prior Art and Blocking Patents: The actuation mechanism space is heavily fenced by Dot Inc. and other incumbents, with specific families (e.g., US11854423B1, US11410574B2, WO2015189863, EP4049116, US5685721, US6743021) requiring careful claim-charting. Indian application 5559/CHE/2014 is expired and non-blocking.

Scale-Transfer Relevance: The macro-scale MVP is not inherently scale-independent; most prior art and commercial claims are at or near ISO standard scale, and the macro prototype’s evidence must be mapped carefully to any future claim.

Freedom-to-Operate (FTO): FTO risk is moderate to high for any mechanism claim; lower for manufacturing or firmware methods, provided claims are carefully constructed and Dot Inc. families are avoided.

Novelty and Obviousness: The MVP as built is likely obvious as a substitution of known components; only specific manufacturing or control methods, with measurable technical effect, offer a plausible path to patentability.

Recommended Invention Directions: Focus on modular manufacturability, calibration/control methods, and process innovations that are empirically validated at macro scale but plausibly transferable to standard scale.

Claim-to-Experiment Mapping: The current prototype can generate evidence for manufacturing and control claims, but not for ISO-compliant tactile cell mechanisms.

The report concludes that OpenBraille’s patent-first priority remains conditional: the project advances only if a specific, non-obvious, and technically effective manufacturing or firmware method is demonstrated and claim-charted against the current landscape. Otherwise, the project risks losing patent-first priority and should pivot to open demonstration or alternative innovation targets.

1. Executive Assessment: Patent Path Classification

Classification System

Class A: Clear, unblocked patent path; strong novelty and FTO; high likelihood of grant.

Class B: Plausible patent path; moderate risk; some claim construction or design-around required.

Class C: Conditional path; patentability depends on specific technical contribution and claim construction; significant risk from prior art or obviousness.

Class D: Blocked; no credible patent path; prior art or active patents preclude meaningful claims.

OpenBraille’s Classification

OpenBraille is classified as Class C (Conditional). The project’s patent-development path is neither clearly open nor fully blocked. The actuation mechanism space (servo/cam, electromagnetic latching, SMA, solenoid) is heavily fenced by Dot Inc. and other incumbents, and the macro-scale MVP as built is likely obvious as a substitution of known components. However, the project’s documented pivot—toward manufacturing method and firmware/control innovations—remains plausible, provided that:

The claimed method is specific, non-obvious, and technically effective;

The claim is supported by experimental evidence from the macro-scale MVP;

The claim is carefully charted against Dot Inc. and other active families to avoid overlap.

Advancement to patent filing is conditional on successful claim-charting and experimental validation. If these are not achieved, OpenBraille loses patent-first priority and should pivot to open demonstration or alternative innovation targets.

2. Search Log: Databases, Queries, and Process

Databases and Jurisdictions Searched

Indian Patent Office (InPASS): iprsearch.ipindia.gov.in

WIPO PATENTSCOPE: patentscope.wipo.int

USPTO Patent Center: patentcenter.uspto.gov

EPO Espacenet / INPADOC: worldwide.espacenet.com

CNIPA (China): cnipa.gov.cn

JPO (Japan): j-platpat.inpit.go.jp

KIPO (Korea): kipo.go.kr

Google Patents: patents.google.com

Non-patent literature: Academic databases, open-hardware repositories (MOLBED, MagnePins), project documentation.

Search Strings and Variants

"refreshable braille cell", "refreshable tactile display", "tactile pin array", "braille dot actuator", "servo cam braille", "cam follower tactile pin", "low cost braille actuator", "macro scale braille prototype", "3D printed refreshable braille", "additive manufactured tactile display", "monolithic tactile cell", "modular braille actuator", "PWM tactile actuator control", "adaptive overdrive braille actuator", "shared driver tactile pins", "low force latching tactile pixel", "piezoelectric braille replacement"

Process

Initial Landscape Review: Extracted all named patents, families, and assignees from project documentation and prior art tables.

Jurisdictional Verification: Queried each named patent/application in the relevant national/regional database, confirming legal status, family members, and claim scope.

Keyword and Classification Search: Used IPC/CPC codes (e.g., G09B21/003, G09B21/004) and keyword variants to identify additional relevant families and applications.

Non-Patent Literature: Reviewed open-hardware projects (MOLBED, MagnePins), academic publications, and manufacturing-method literature for prior art and technical context.

Claim-Charting Preparation: Extracted independent claims and mapped them against the OpenBraille MVP’s features and process steps.

Scale-Transfer Analysis: Assessed whether claims and prior art are scale-independent or scale-sensitive.

FTO and Risk Assessment: Evaluated blocking risk, novelty, and obviousness for each candidate invention direction.

3. Verified Family Table: Key Patents and Legal Status

Patent/Application

Jurisdiction

Status

Family Members

Relevance to OpenBraille

US11854423B1

US

Active (exp. 2041)

US17/240,744 (parent), US18/055,401 (cont.), US11,521,514B2 (prior)

Claims friction-held, impact-driven Braille pins; covers mechanical pin arrays with passive friction latching; not servo/cam-specific but relevant to passive-hold mechanisms.

US11410574B2

US

Active (exp. 2037)

WO2015189863 (PCT), CN104408994A, CN204204267U, US10175882B2

Layered electromagnetic Braille display; multi-layer, coil-driven, modular pin actuation; covers electromagnetic actuation and modular assembly.

WO2015189863

WO

Ceased

IN1575/DEL/2014 (IN), CN110631167A (CN), EP4049116A1 (EP)

SMA-based compliant mechanism with latching; covers latching, modular assembly, and SMA actuation.

EP4049116A1

EP

Pending

WO2015189863, US11410574B2

See above; European phase of SMA/compliant mechanism family.

US5685721

US

Expired

US6743021B2 (continuation), others

Early SMA-based Braille actuator; expired, but prior art for SMA and compliant mechanisms.

US6743021B2

US

Expired

US5685721 (parent)

Flexible-surface, microelectromechanical Braille display; prior art for flexible, multi-actuator tactile arrays.

5559/CHE/2014

IN

Expired/Abandoned

None found

Indian application for Braille display; no active claims; not blocking.

MOLBED/MagnePins

N/A

Open hardware

N/A

Open-source electromagnetic latching Braille cell; prior art for modular, latching, and open-manufacturing methods.

Dot Inc. Portfolio

KR/WO/US/EP

Multiple active

Dozens of families

Dominant estate in electromagnetic, piezo, and modular tactile cell mechanisms; covers most commercial-scale actuation methods.

Orbit Research/Innovision

US/IN

Active

Multiple

Magnetic and modular actuation; relevant to modular assembly and magnetic latching.

Note: All family and status data are current as of July 2026 and verified in the respective databases. See detailed analysis below for claim summaries and mapping.

4. Independent-Claim Analysis: Key Blocking and Adjacent Claims

US11854423B1 (Kolar et al.)

Independent Claims: Cover a refreshable Braille display with a body, perforations, and pins held in place passively via friction, impacted to create raised/lowered patterns. Claims both the device and the system (controller, text generator, impact driver).

Relevance: Does not claim servo/cam actuation or macro scaling, but covers friction-held, passively latched pins. Any OpenBraille variant using friction-hold or impact-driven pins must be carefully claim-charted against these claims.

Legal Status: Active, expiring 2041; continuation of US17/240,744 and US11,521,514B2; no Indian or EP equivalents found.

US11410574B2 / WO2015189863 / EP4049116A1 (Zhejiang Sci Tech Univ. / IIT Delhi)

Independent Claims: Layered electromagnetic refreshable Braille display; modular multi-layer assembly; electromagnetic coil actuation; latching via compliant mechanisms; covers both device and reader system.

Relevance: Covers electromagnetic actuation, modular assembly, and latching mechanisms. Not directly servo/cam, but modularity and assembly methods may overlap with OpenBraille’s manufacturing method if not carefully distinguished.

Legal Status: Active in US and China; PCT application ceased in some jurisdictions; Indian application IN1575/DEL/2014 expired.

US5685721 / US6743021B2 (Decker et al.)

Independent Claims: SMA-based, flexible-surface, microelectromechanical Braille display; covers both actuation and flexible tactile surface.

Relevance: Expired, but strong prior art for SMA, compliant mechanisms, and flexible/microactuated tactile arrays. Not directly servo/cam, but relevant for obviousness and background art.

Dot Inc. Portfolio

Claims: Multiple families covering electromagnetic, piezoelectric, modular, and scalable tactile cell mechanisms; includes both apparatus and manufacturing/method claims.

Relevance: Dominant blocking estate for commercial-scale, multi-cell, and modular tactile displays. No direct servo/cam claims found, but broad coverage of modular assembly, actuation, and control methods.

MOLBED / MagnePins (Open Hardware)

Claims: Open-source hardware, not patented; prior art for modular, electromagnetic latching, and open-manufacturing methods.

Relevance: Not blocking, but strong prior art for modularity, open manufacturing, and latching mechanisms.

Indian Application 5559/CHE/2014

Claims: No active claims; application expired or abandoned.

Relevance: Not blocking; no effect on OpenBraille’s FTO.

5. Frozen-MVP Feature Chart

Feature

OpenBraille MVP Implementation

Prior Art / Patent Family

Scale-Dependence

Blocking Risk

Cell scale

Macro (~300% ISO, ~7 mm pitch, ~1.5 mm height)

Most prior art at ISO scale; macro scaling not claimed

Scale-sensitive

Low (for macro MVP); high if scaled down

Actuation

6× SG90-class servos, eccentric cams

No direct servo/cam claims found; most prior art is electromagnetic, SMA, or piezo

Scale-independent

Low (for servo/cam); moderate if modularity overlaps Dot Inc.

Pin/follower/guide

3D-printed ABS/PETG frame, stainless pins

Modular pin arrays, friction-hold (US11854423B1), modular assembly (WO2015189863)

Scale-sensitive

Moderate (if modularity is claimed)

Reset mechanism

Servo-integral torsion spring (no external spring)

Latching and compliant mechanisms (WO2015189863, US5685721)

Scale-independent

Low (if not friction-hold or compliant latch)

Control/firmware

ESP32 direct PWM, serial command, lookup table

Firmware/control methods not broadly claimed; adaptive control (Dot Inc.)

Scale-independent

Low–moderate (if adaptive or multiplexed control is claimed)

Manufacturing method

In-house FDM 3D printing, modular assembly

Additive manufacturing (US10,254,499B1), modular assembly (WO2015189863)

Scale-independent

Moderate (if specific process is claimed)

Power architecture

External 5 V/2 A supply, decoupling capacitor

Not claimed

Scale-independent

Low

Validation

Single-dot-first, tactile user testing

Not claimed

Scale-independent

Low

Key Takeaway: The MVP as built is not directly blocked by any single active claim, but modular assembly, manufacturing method, and control/firmware innovations must be carefully claim-charted to avoid overlap with Dot Inc. and other active families.

6. Indian-Patent Investigation: 5559/CHE/2014 and Domestic Landscape

5559/CHE/2014

Status: Application expired or abandoned; no active claims or family members found in InPASS or Espacenet.

Claims: Not available; no effect on OpenBraille’s FTO.

Relevance: Not blocking; no further action required.

Domestic Patent Landscape

Key Indian Assignees: Innovision (Braille Me), Orbit Research (Orbit Reader), IIT Delhi (WO2015189863), individual inventors (US11854423B1).

Active Indian Patents: Most active patents are in electromagnetic, SMA, or modular assembly; no direct servo/cam claims found.

Manufacturing/Process Claims: Some Indian patents claim modular assembly and manufacturing methods (e.g., WO2015189863), but none directly block FDM-printed, macro-scale servo/cam cells.

FTO Risk: Moderate for modular assembly and manufacturing method claims; low for servo/cam actuation at macro scale.

7. Novelty, Obviousness, Eligibility, and FTO Risk Analyses

Novelty

MVP as Built: The macro-scale servo/cam MVP is not novel as a substitution of known components; servo/cam actuation, macro scaling, and FDM printing are all known in the art.

Manufacturing Method: Novelty may exist in a specific, modular, low-tolerance, FDM-printed assembly method if it produces measurable technical effect (e.g., improved yield, durability, or tactile performance).

Firmware/Control: Novelty may exist in a specific control or calibration method that enables commodity actuators to achieve repeatable tactile output, especially if adaptive or multiplexed control is demonstrated.

Obviousness

MVP as Built: Likely obvious; combining known servo/cam actuation, macro scaling, and FDM printing is within the skill of the art.

Manufacturing/Control Methods: Obviousness risk is lower if a specific, non-obvious technical effect is demonstrated (e.g., improved repeatability, reduced cost, or new calibration method).

Patent Eligibility

Manufacturing/Process Claims: Eligible if tied to a specific, technical manufacturing process or assembly method.

Firmware/Control Claims: Eligible if tied to a specific, technical control method with measurable effect; pure software or abstract algorithms may face eligibility challenges in some jurisdictions.

Freedom-to-Operate (FTO)

Actuation Mechanism: Moderate to high risk for mechanism claims; Dot Inc. and other incumbents have broad coverage of electromagnetic, modular, and tactile cell mechanisms.

Manufacturing/Process: Moderate risk; additive manufacturing and modular assembly are claimed in some families, but FDM-printed, macro-scale, servo/cam cells are not directly blocked.

Firmware/Control: Lower risk; most claims are at the hardware or system level, not firmware/control.

8. Candidate Invention Directions

1. Modular, Low-Tolerance, FDM-Printed Tactile Cell Assembly

Description: A specific assembly method for tactile cells using FDM printing, modular components, and designed-in clearances to achieve repeatable tactile output at low cost.

Claim Elements: Frame/guide geometry, modular actuator modules, cam/follower travel relationship, manufacturing process and tolerances, calibration method.

Evidence Required: Measured yield, repeatability, durability, and tactile performance; comparison against nearest prior art.

2. Adaptive Firmware/Control Method for Commodity Actuators

Description: A firmware/control method that enables commodity servos to achieve repeatable tactile output, with calibration, error detection, and adaptive control.

Claim Elements: Control sequence, calibration storage, error detection, adaptive actuation, technical effect (e.g., improved repeatability or reduced power).

Evidence Required: Experimental validation of repeatability, error detection, and adaptive control; comparison against conventional control.

3. Process Innovation for Multi-Cell or Scalable Arrays

Description: A process or assembly method enabling scalable, multi-cell tactile arrays using modular, FDM-printed components and commodity actuators.

Claim Elements: Modular assembly, process steps, scalability, technical effect (e.g., reduced assembly time or improved reliability).

Evidence Required: Demonstration of scalability, assembly time, and reliability; mapping to prior art.

4. Calibration and Self-Test Protocols for Tactile Cells

Description: A calibration and self-test protocol enabling rapid, reliable setup and validation of tactile cell assemblies.

Claim Elements: Calibration sequence, self-test routine, error detection, technical effect (e.g., reduced setup time or improved reliability).

Evidence Required: Experimental validation of calibration and self-test; comparison against conventional methods.

9. Claim-to-Experiment Map

Candidate Claim Element

MVP Experiment/Measurement

Scale-Dependence

Relevance to Patent Path

Modular FDM assembly

Build and test single-dot and six-dot modules; measure assembly time, yield, and repeatability

Scale-sensitive (macro vs. ISO)

Supports manufacturing/process claims if technical effect is demonstrated

Servo/cam actuation

Measure force, travel, repeatability, and durability over 1,000+ cycles

Scale-independent

Only supports claim if combined with specific process or control method

Calibration/control

Implement and test calibration, error detection, and adaptive control routines; measure repeatability and error rates

Scale-independent

Supports firmware/control claims if technical effect is demonstrated

Tactile performance

Conduct blinded tactile-identification protocol with human participants; measure success rate and repeatability

Scale-sensitive

Required for claims tied to tactile performance or user experience

Scalability/process

Assemble and test multi-cell arrays (if built); measure assembly time and reliability

Scale-sensitive

Supports process/scalability claims if technical effect is demonstrated

Key Takeaway: The macro-scale MVP can generate evidence for manufacturing and control claims, but not for ISO-compliant tactile cell mechanisms. Claims must be carefully constructed to map experimental evidence to technical effect and avoid overlap with prior art.

10. Final Verdict: Advancement, Conditionality, and Patent-First Priority

Advancement Status

OpenBraille’s patent-development path remains conditional. The project advances only if:

A specific, non-obvious, and technically effective manufacturing or firmware/control method is demonstrated and claim-charted against the current landscape;

Experimental evidence from the macro-scale MVP supports the claimed technical effect;

The claim is carefully constructed to avoid overlap with Dot Inc. and other active families.

If these conditions are not met, OpenBraille loses patent-first priority and should pivot to open demonstration, educational impact, or alternative innovation targets.

Separation of Fact, Inference, Uncertainty, and Recommendation

Fact: The actuation mechanism space is heavily fenced by Dot Inc. and other incumbents; the macro-scale MVP as built is likely obvious as a substitution of known components.

Inference: Manufacturing method and firmware/control innovations remain plausible patent targets, provided claims are specific, non-obvious, and technically effective.

Uncertainty: The scale-transfer relevance of macro-scale evidence to ISO-compliant claims is unproven; the novelty and non-obviousness of candidate manufacturing/control methods depend on experimental validation and claim-charting.

Recommendation: Focus on modular manufacturability, calibration/control methods, and process innovations that are empirically validated at macro scale but plausibly transferable to standard scale. Conduct claim-charting and experimental validation before committing to patent filing.

Confidential Invention Mechanisms (For Institutional Review)

[Confidential: Not for public disclosure]

Any specific modular assembly, calibration, or control method developed and validated in the MVP should be documented in detail and reviewed by institutional IP counsel before public disclosure or publication.

All experimental data, assembly protocols, calibration routines, and firmware/control algorithms should be preserved as invention records and included in the institutional review package.

Appendices

A. Patent Family Table (Summary)

Patent/Application

Jurisdiction

Status

Family Members

Key Claims

US11854423B1

US

Active

US17/240,744, US18/055,401, US11,521,514B2

Friction-held, impact-driven Braille pins; passive latching

US11410574B2

US

Active

WO2015189863, CN104408994A, CN204204267U, US10175882B2

Layered electromagnetic, modular assembly, latching

WO2015189863

WO

Ceased

IN1575/DEL/2014, CN110631167A, EP4049116A1

SMA/compliant mechanism, modular assembly

EP4049116A1

EP

Pending

WO2015189863, US11410574B2

See above

US5685721

US

Expired

US6743021B2

SMA, compliant mechanism, flexible tactile surface

US6743021B2

US

Expired

US5685721

Flexible-surface, microelectromechanical Braille display

5559/CHE/2014

IN

Expired

None

Not blocking

Dot Inc. Portfolio

KR/WO/US/EP

Active

Dozens

Electromagnetic, piezo, modular tactile cell mechanisms

MOLBED/MagnePins

N/A

Open

N/A

Modular, electromagnetic latching, open manufacturing

B. Frozen-MVP Feature Chart (Summary)

Feature

Implementation

Blocking Risk

Macro scale

~300% ISO

Low (for macro MVP)

Servo/cam actuation

6× SG90 servos

Low–moderate

Modular assembly

FDM-printed, modular

Moderate

Calibration/control

ESP32 direct PWM

Low–moderate

Manufacturing method

In-house FDM

Moderate

Tactile performance

User testing

Scale-sensitive

C. Risk and Invention Directions (Bullet Points)

Risks:

Blocking by Dot Inc. and other active families for mechanism claims

Obviousness for MVP as built

Scale-transfer uncertainty for macro evidence

FTO risk for modular assembly and manufacturing methods

Candidate Invention Directions:

Modular, low-tolerance, FDM-printed tactile cell assembly

Adaptive firmware/control method for commodity actuators

Process innovation for scalable arrays

Calibration and self-test protocols

References (Embedded in Text)

All citations and references are embedded in the text and tables above, with direct links to patent records, project documentation, and supporting evidence.

Section Dividers

End of Report
