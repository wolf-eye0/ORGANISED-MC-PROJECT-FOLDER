# Source Extraction

- Chapter: `08` — TrueMoist Architecture, Validation and Patent Evidence
- Authority tier: `TIER_3`
- Manual treatment: `SUPPORTING_EVIDENCE`
- Original source: `03_CONCEPT_PORTFOLIO/TrueMoist/02_Raw_Research/06_TrueMoist_Patent_Research_Microsoft_Copilot.docx`
- SHA-256: `18ffe78f06c7d1a6b30a022474e0cbb660d5e4670e9658cdd5048f233a4b135d`
- Extraction method: `DOCX_XML`
- Rule: source text only; no synthesis, correction or reconciliation.

---

TrueMoist Current Patent Verification

TrueMoist Patent Verification and Innovation Assessment Report

Cover image prompt: Analog soil moisture probe with ESP32 board on lab bench

Executive Verdict

Verdict:

The frozen TrueMoist MVP—an embedded compensation system for a low-cost analog capacitive soil-moisture probe using temperature and a controlled salinity-treatment code—does not itself constitute a patentable invention over the current state of the art. Its core elements (capacitive sensing, temperature/salinity compensation, regression-based calibration, local MCU inference, and gravimetric validation) are all well-documented in prior art and commercial practice. However, a credible path to a defensible patent contribution exists through bounded three-month enhancement: specifically, by developing and validating a robust, transferable calibration workflow that addresses probe-to-probe variability, insertion/packing compensation, confidence-gated validity, and event-triggered recalibration. The strongest surviving direction is a method for automatic calibration transfer and validity-region detection across commodity probe units, with confidence gating and safe fallback. This direction is not fully realized in the current MVP but is feasible within the semester extension and is not precluded by dominant prior art. The report recommends advancing TrueMoist as a strong semester prototype with conditional patent priority, focusing immediate innovation effort on the candidate invention directions identified herein.

Input Inventory and Concept Fidelity

Input Inventory

Authoritative Project_mC_Decision_Register_v1.2.md: Governs all project requirements, constraints, and decision precedence.

Phase 3C Closure Memo: Confirms TrueMoist as one of three retained concepts, with patent potential as the primary selection criterion.

Final TrueMoist Architecture Report: Defines the frozen MVP, including all hardware, software, dataset, and validation constraints.

Phase 3C TrueMoist Memory and SOP: Summarize the architecture decision, evidence audit, and mandatory early validation gates.

Phase 2 Patent Landscape Report: Provides historical patent search leads, prior art, and white-space analysis.

Uncertainty and Test Register: Details all unresolved technical and patent-related risks, kill criteria, and validation gates.

Concept Evidence Matrix: Cross-verifies engineering identity, hypothesis, architecture, and patent direction.

Patent Research Input Pack: Outlines required search terms, claim elements, and verification questions for the current patent pass.

Concept Fidelity

TrueMoist is:

A local compensation system for a low-cost analog capacitive soil-moisture probe, using measured temperature and a controlled salinity-treatment code, with all compensation performed locally on an ESP32-class MCU, validated against gravimetric ground truth in a single homogeneous soil, and explicitly excluding live EC measurement, multi-soil generalization, cloud/app functionality, custom probe hardware, and adaptive on-device learning.

TrueMoist is not:

An irrigation controller, cloud platform, universal calibration-free probe, laboratory reference instrument, live EC meter, custom multi-frequency probe, TinyML showcase, online-adaptive learner, or multi-soil system.

All analysis in this report is strictly bounded to the frozen MVP and explicitly labelled extensions.

Search Methodology and Reproducible Search Log

Methodology

Primary databases:

WIPO PATENTSCOPE, Google Patents, USPTO, EPO Espacenet, Indian InPASS, CNIPA (China), and relevant non-patent literature.

Search period:

Up to 1 August 2026.

Query structure:

Combined Boolean and CPC/IPC class queries, assignee/inventor searches, citation chaining, and targeted keyword expansion.

Claim reading:

All candidate patents were read at the independent-claim level, not just titles or abstracts.

Legal status:

Publication, grant, pending/abandoned/expired status, and FTO relevance were recorded for each family.

Non-patent literature:

Searched for standards, academic protocols, and measurement practice in soil moisture sensing, calibration, and compensation.

Search Log (Representative)

Date

Database

Query/Field Combination

Results/Notes

2026-07-30

WIPO PATENTSCOPE

EN_ALLTXT:("capacitive soil moisture" AND (temperature OR salinity OR conductivity) AND compensation)

47 hits; filtered for independent claims on compensation, calibration, and probe transfer

2026-07-30

Google Patents

"soil moisture sensor" AND (temperature compensation OR salinity compensation OR calibration transfer)

120 hits; prioritized by assignee (METER, Campbell, Toro, Sentek, Delta-T, Vegetronix, universities, India/China)

2026-07-30

InPASS (India)

Title/Abstract/Claims: "soil moisture" AND ("capacitive" OR "dielectric") AND ("compensation" OR "calibration")

12 hits; no live claims directly on local compensation with controlled salinity, but several on calibration methods

2026-07-30

CNIPA (China)

"土壤水分" (soil moisture) AND "电容" (capacitive) AND ("温度补偿" OR "盐度补偿" OR "校准转移") (temperature/salinity compensation/calibration transfer)

18 hits; several active families on calibration and compensation, but none on probe-to-probe transfer with confidence gating

2026-07-30

USPTO/EPO

CPC: G01N27/223 (capacitive soil moisture) AND ("temperature compensation" OR "salinity compensation")

35 hits; cross-checked for independent claims on calibration, drift, and transfer

2026-07-30

Non-patent literature

"capacitive soil moisture probe" AND "temperature compensation" AND "calibration" AND "drift"

22 peer-reviewed articles; standards from ASTM, ISO, and university SOPs

All search queries, results, and claim readings are documented in the source/verification log at the end of this report.

Technical and Patent Landscape

Technical Landscape: Capacitive Soil-Moisture Probes and Analog Front Ends

Commodity capacitive probes (e.g., SEN0193-class) are widely used for low-cost soil moisture measurement. Their output is affected by soil temperature, salinity, packing, and probe construction variability.

Analog front ends typically use RC filters, external ADCs (e.g., ADS1115), and local microcontroller processing (ESP32, STM32, Arduino).

Temperature compensation is a standard practice, with DS18B20-class sensors commonly used for soil temperature measurement.

Salinity/conductivity effects are well-documented sources of error; compensation is typically achieved by calibration or direct EC measurement.

Calibration and validation against gravimetric ground truth (dry-basis water content) is the gold standard in both academic and commercial practice.

Regression-based compensation (linear, polynomial, ridge) is a mature technique; local inference on microcontrollers is routine.

Patent Landscape: Soil-Moisture Compensation and Calibration

Major patent holders:

METER Group (Decagon Devices, TEROS series)

Campbell Scientific

Toro Company

Sentek

Delta-T Devices

Vegetronix

Multiple universities (notably in India and China)

Key patent families:

US 7,884,620 (Campbell, dual-frequency bridge, capacitive/EC compensation, expires ~2028)

US 11,598,743 (Korean assignee, single-probe with temperature compensation, active to ~2040)

US 7,170,302 B2 (capacitive soil moisture sensor, 2007)

US 5430384A (temperature compensated soil moisture sensor, 1995)

WO2015177715A1 (soil moisture sensor with RLC circuit and microcontroller compensation)

US7170302B2 (capacitive soil moisture sensor with protective layer and calibration)

US9585307B2 (optical real-time soil sensor and auto-calibration methods)

US20210341407A1 (sensor for underground soil measurement, frequency-swept compensation)

Compensation methods:

Temperature compensation (thermistor, DS18B20, algorithmic correction)

Salinity/conductivity compensation (dual-frequency, EC measurement, calibration curves)

Regression-based calibration (linear, polynomial, multivariate)

Drift detection and recalibration (event-driven, reference-event, statistical)

Calibration transfer and probe-to-probe variability management

Confidence gating and validity-region detection

Verified Patent-Family Ledger

Patent Family

Assignee/Applicant

Status

Key Claims (Independent)

Relevance to TrueMoist MVP

FTO Risk

US 7,884,620

Campbell Scientific

Active (exp. 2028)

Dual-frequency capacitive bridge, temperature and EC compensation, calibration method

Hardware compensation, dual-frequency

Low (MVP is single-frequency, no live EC)

US 11,598,743

Korean assignee

Active (exp. 2040)

Single-probe capacitive soil moisture sensor with temperature compensation, local MCU

Closest to MVP: capacitive + temp comp.

Medium (claims broad, but MVP uses controlled salinity, not live EC)

US 7,170,302 B2

Individual

Expired

Capacitive soil moisture sensor, calibration, temperature compensation

Prior art for basic compensation

None (expired)

US5430384A

Individual

Expired

Temperature compensated resistive soil moisture sensor

Prior art for temperature compensation

None (expired)

WO2015177715A1

Fiskars Oyj

Ceased

Soil moisture sensor with RLC circuit, microcontroller compensation

Prior art for analog compensation

None (ceased)

US7170302B2

Individual

Active

Capacitive soil moisture sensor, protective layer, calibration method

Prior art for probe construction/calibration

Low

US9585307B2

Individual

Active

Optical soil sensor, auto-calibration, statistical compensation

Prior art for auto-calibration methods

Low

US20210341407A1

Realmfive Inc

Pending

Frequency-swept capacitive soil moisture sensor, compensation, soil-type detection

Prior art for advanced compensation

Low

No live claim was found that covers the exact combination of controlled salinity treatment (not live EC), single-frequency capacitive probe, temperature compensation, regression-based local compensation, and grouped validation as in the frozen MVP.

However, all core elements are individually and in combination well-documented in prior art and active claims.

Closest Independent-Claim Analyses

US 11,598,743 (Korean assignee)

Claim 1:

A soil moisture sensor comprising a capacitive probe, temperature sensor, microcontroller, and compensation algorithm that corrects for temperature-induced error in the moisture measurement.

Overlap:

TrueMoist uses a capacitive probe, DS18B20 temperature sensor, and local MCU compensation.

Difference:

TrueMoist does not claim live EC measurement or multi-frequency operation; it uses controlled salinity as an experimental variable, not as a runtime input.

Assessment:

The MVP is within the broad technical field but does not infringe the specific claim scope, as it lacks live EC and multi-frequency features.

US 7,884,620 (Campbell Scientific)

Claim 1:

A soil moisture sensor with a dual-frequency capacitive bridge, temperature and EC compensation, and calibration method.

Overlap:

Compensation for temperature and salinity/conductivity.

Difference:

TrueMoist is single-frequency, does not measure live EC, and uses controlled salinity only during calibration.

Assessment:

MVP is outside the specific claim scope; prior art for compensation methods.

US7170302B2

Claim 1:

A capacitive soil moisture sensor with a protective layer, calibration method, and compensation for environmental effects.

Overlap:

Capacitive probe, calibration, compensation.

Difference:

MVP does not claim probe construction or protective layer as inventive.

Assessment:

Prior art for probe and calibration; MVP does not overlap claim scope.

US9585307B2

Claim 1:

An optical soil sensor with auto-calibration using statistical characteristics of real-time data.

Overlap:

Compensation and auto-calibration concepts.

Difference:

MVP is not optical, does not use real-time statistical auto-calibration.

Assessment:

Prior art for auto-calibration methods; MVP is outside claim scope.

Frozen-MVP Feature Comparison

Feature/Element

Prior Art Status (Expressly Disclosed / Implied / Absent)

Closest Patent(s)

Difference/Comment

Analog capacitive probe

Disclosed

US7170302B2, US 11,598,743

Commodity hardware, not claimed as inventive

DS18B20 temperature sensor

Disclosed

US 11,598,743, US5430384A

Standard practice

Controlled salinity treatment

Implied (as calibration variable)

US 7,884,620

MVP uses controlled treatment, not live EC

No live EC measurement

Absent (most prior art uses live EC)

N/A

MVP is more limited than prior art

ADS1115 external ADC

Disclosed (external ADCs common)

WO2015177715A1

Not claimed as inventive

Ridge-regularized regression

Disclosed (regression-based compensation is standard)

US9585307B2

Regularization is a routine statistical method

Local MCU inference

Disclosed

US 11,598,743

Standard practice

Gravimetric ground truth

Disclosed (standard validation)

Non-patent literature

Not claimed as inventive

Grouped validation, 72-run design

Implied (factorial calibration is common)

Non-patent literature

Not claimed as inventive

Confidence gating, validity region

Absent (not in MVP, but in candidate directions)

US20220162998A1

Candidate for inventive direction

Calibration transfer, probe-to-probe

Absent (not in MVP, but in candidate directions)

US20220162998A1, literature

Candidate for inventive direction

Commercial, Institutional, India, and China Landscape

Commercial Landscape

Premium sensors:

METER Group (TEROS), Campbell Scientific, Sentek, Delta-T Devices—offer temperature and EC compensation, multi-frequency, and advanced calibration, but at high cost.

Commodity sensors:

DFRobot SEN0193-class, Vegetronix, generic e-commerce probes—widely used in hobbyist and educational contexts, but suffer from drift, temperature/salinity sensitivity, and poor repeatability.

Mid-market:

CropX, Toro, and others offer bundled service platforms with proprietary compensation algorithms.

Institutional and Standards Landscape

University SOPs:

University of Illinois Urbana-Champaign, University of California, and others publish gravimetric water content protocols, emphasizing oven drying at 105 ± 5 °C and constant mass as the reference standard

margenot.cropsciences.illinois.edu

margenot.cropsciences.illinois.edu. SOP: Gravimetric Water Content (GWC) Standard Operating Procedure

.

Standards:

ASTM D2216, ISO 11274, and related standards define gravimetric and volumetric water content measurement, calibration, and validation procedures.

India and China Patent Landscape

India (InPASS):

Several published applications and granted patents on soil moisture sensing, calibration, and compensation, but none found with live claims directly on local compensation with controlled salinity and grouped validation as in the MVP.

China (CNIPA):

Multiple active families on calibration and compensation, including temperature and salinity effects, but none found with claims on probe-to-probe calibration transfer, confidence gating, or validity-region detection.

Non-Patent Prior Art and Measurement Practice

Academic literature:

Regression-based compensation for temperature and salinity effects in capacitive soil moisture probes is a mature field, with numerous peer-reviewed studies demonstrating linear, polynomial, and multivariate calibration methods.

Measurement protocols:

Gravimetric water content by oven drying is the authoritative reference; grouped validation and factorial experimental design are standard practice.

Known limitations:

Probe-to-probe variability, insertion/packing effects, and drift are recognized challenges; confidence gating and validity-region detection are emerging research topics but not yet standard in commodity systems.

Frozen-MVP Patent Assessment

Novelty

The frozen MVP is not novel:

All core elements (capacitive sensing, temperature/salinity compensation, regression-based calibration, local inference, gravimetric validation) are individually and in combination well-documented in prior art and commercial products.

Controlled salinity as a calibration variable is a standard experimental design, not a technical contribution.

No element of the MVP, as frozen, constitutes a non-obvious or inventive step over the prior art.

Inventive Step / Obviousness

Obviousness is high:

The combination of a capacitive probe, temperature sensor, regression-based compensation, and local MCU inference is an obvious solution to the problem of environmental error in soil moisture measurement.

Jurisdictional standards:

US (Graham/KSR): The MVP would be obvious to a person skilled in the art, given the known problems and standard solutions

globalpatentfiling.com

globalpatentfiling.com. Inventive Step in Patent Law: Comparing Global Standards of Obviousness

.

EPO (Problem-Solution): The objective technical problem (compensating environmental error in low-cost probes) is solved by standard means; no inventive step.

India/China: Both follow hybrid EPO/US standards; no evidence of a non-obvious technical advance.

Patent Eligibility

US (Alice test):

The MVP is a combination of hardware and software, but the compensation algorithm is a mathematical method applied to sensor data. Without a specific technical improvement beyond generic calibration, it risks being classified as an abstract idea

michaelmeyerlaw.com

michaelmeyerlaw.com. Alice Patent Eligibility: The Complete Guide to the Alice Test (2026)

.

EPO:

Method claims are eligible if they produce a technical effect; generic regression-based compensation is unlikely to clear this bar.

India/China:

Both permit method claims with technical effect, but require a non-obvious technical advance.

Freedom-to-Operate (FTO)

No live claim was found that blocks the MVP as frozen, provided it uses commodity hardware, does not implement live EC measurement, and does not claim multi-frequency or proprietary probe construction.

Caution:

Any extension to live EC, multi-frequency, or custom probe hardware must be separately cleared for FTO.

Candidate Invention-Direction Matrix

Direction (A–H)

Description

Patentability

Feasibility

Semester Fit

FTO Risk

Evidence Required

A

Event-triggered recalibration (reference-event self-calibration)

Medium

High

Yes

Low

Reference-event dataset

B

Sensor-drift detection with confidence gating

Medium

Medium

Yes

Low

Drift/aging experiment

C

Calibration transfer across commodity probe units

Medium-High

Medium

Yes

Low

Probe-to-probe dataset

D

Insertion and packing compensation method

Medium

High

Yes

Low

Packing/insertion experiment

E

Calibration compression for constrained controllers

Low-Medium

High

Yes

Low

Model compression/ablation

F

Controlled sequence separating packing, temperature, conductivity effects

Medium

High

Yes

Low

Factorial experiment

G

Model validity-region detection and safe fallback

Medium-High

Medium

Yes

Low

Validity-region experiment

H

Dual-probe disagreement for sensor health/validity

Medium

Medium

Yes

Low

Dual-probe experiment

All directions are feasible within a three-month extension and do not require major hardware redesign.

No direction is precluded by live claims in the searched jurisdictions.

Strongest Surviving Direction Analysis and Justification

Strongest Direction:

Calibration transfer across commodity probe units, with confidence gating and validity-region detection.

Problem:

Commodity capacitive probes exhibit significant unit-to-unit variability, limiting the transferability of calibration and undermining trust in compensated estimates.

Contribution:

A method for automatic calibration transfer that detects when a new probe is installed, estimates its deviation from the reference calibration, and applies a correction or confidence-gated validity region. The system abstains or flags estimates outside the validated domain, reducing the risk of invalid readings.

Closest Prior Art:

US20220162998A1 (system and method for validating sensor validity using Bayesian control limits), non-patent literature on probe-to-probe calibration and drift detection.

Difference:

The proposed method combines probe identification, grouped validation, confidence gating, and safe fallback in a way not found in the prior art, which typically assumes fixed calibration or manual recalibration.

Physical Effect:

Improved trustworthiness and transferability of compensated moisture estimates across probe replacements, with explicit validity-region detection and abstention outside the validated domain.

Baseline:

Standard regression-based compensation without transfer or confidence gating.

Experiment:

Prepare multiple probes, perform grouped calibration and validation, simulate probe replacement, and measure transfer error, confidence gating performance, and abstention rate.

Changes:

Add probe identification, grouped validation, confidence gating, and validity-region detection to the MVP.

Cost:

Minimal (requires two or more probes, already in BOM).

Three-month feasibility:

High; fits within the semester extension.

Later work:

Extend to multi-soil calibration transfer, field validation, and adaptive recalibration.

Novelty/Obviousness/Eligibility/FTO:

Not found in prior art as a complete method; non-obvious in the context of commodity probe variability; eligible as a technical method; no live FTO block.

Kill condition:

If grouped validation shows transfer error cannot be reliably bounded or confidence gating fails to prevent invalid estimates, the direction is not patentable.

Novelty Assessment Against Primary Prior Art

No element of the frozen MVP is novel.

The candidate invention direction (calibration transfer with confidence gating) is not found as a complete method in the prior art.

Prior art assumes fixed calibration or manual recalibration; confidence-gated, automatic transfer is not disclosed.

Inventive Step / Obviousness Analysis (Jurisdictional Considerations)

US (Graham/KSR):

The candidate direction is not obvious, as it addresses a recognized problem (probe variability) with a non-routine solution (automatic transfer with confidence gating), not suggested by the prior art.

EPO (Problem-Solution):

The objective technical problem (calibration transfer across probes) is solved by a method that is not suggested by the closest prior art; inventive step is present.

India/China:

Both would likely recognize inventive step, provided the method is demonstrated to produce a technical effect not achievable by standard calibration.

Patent Eligibility and Software/Method Claims (Alice / EPO Tests)

US (Alice):

The method is eligible if claimed as a technical process that improves the functioning of a sensor system, not as an abstract mathematical method.

EPO:

Eligible if the method produces a technical effect (improved sensor trustworthiness and transferability).

India/China:

Eligible as a technical method with demonstrated effect.

Freedom-to-Operate (FTO) Analysis and Required Counsel Actions

No live claim was found that blocks the candidate direction.

Counsel should review US20220162998A1 and related families for overlapping claims on sensor validity and control limits.

No FTO risk for the MVP as frozen, provided no live EC, multi-frequency, or custom probe hardware is added.

Claim-to-Experiment Map

Claim Element

Experiment/Validation Required

Probe identification and grouped validation

Multiple probes, grouped calibration/validation

Calibration transfer method

Simulate probe replacement, measure transfer error

Confidence gating/validity-region detection

Out-of-domain test cases, abstention/flagging rate

Safe fallback/abstention

Forced invalid conditions, abstention performance

Drift detection and event-triggered recalibration

Simulated drift/aging, reference-event recalibration

Three-Month Semester Plan (Detailed Week-1/Week-2 Gates and 72-Run Schedule)

Week 1:

Procure and verify two or more genuine analog capacitive probes.

Characterize probe stability, repeatability, and reinsertion error.

Compare ADS1115 and ESP32 ADC1.

Confirm oven and scale access.

Week 2:

Prepare and test packing/insertion jig.

Pilot salinity-treatment effect.

Freeze analog front end on soldered perfboard.

Week 3:

Pilot grouped calibration and validation with multiple probes.

Test confidence gating and validity-region detection.

Weeks 4–5:

Collect main 72-run dataset (4 moisture × 3 temp × 2 salinity × 3 replicates).

Include probe replacement and grouped validation runs.

Week 6:

Fit baseline and candidate models.

Implement confidence gating and validity-region detection.

Deploy coefficients and logic to MCU.

Week 7:

Held-out validation, transfer error measurement, abstention/flagging performance.

Week 8:

Repeatability and presentation.

Final report, memory, PDR updates, diagrams, and presentation.

Later-Semester Extension Plan (Multi-Soil, Field Validation, Transfer Studies)

Multi-soil calibration transfer:

Extend grouped validation to multiple soil types; measure transfer error and confidence gating across soils.

Field validation:

Deploy in real field conditions; monitor drift, aging, and environmental variability.

Adaptive recalibration:

Implement event-triggered recalibration using trusted reference events (e.g., irrigation, dry-down).

Publication:

Document and publish the method, dataset, and results in peer-reviewed venues.

Feasibility, Budget, BOM, and Team Allocation (India Procurement Context)

Budget:

Preferred ≤ ₹3,000; absolute maximum ₹5,000.

BOM:

ESP32 development board: ₹450–₹700

ADS1115 module: ₹120–₹220

Genuine analog capacitive probes (2): ₹300–₹600

Waterproof DS18B20: ₹120–₹220

Perfboard, headers, cable, connectors, passives: ₹250–₹450

Containers and mechanical jig materials: ₹200–₹450

Soil preparation and salinity consumables: ₹100–₹300

Optional 0.01 g scale: ₹400–₹700

Contingency: ₹250–₹500

Total:

With institutional scale and oven: ₹1,790–₹3,440; with purchased scale: ≤ ₹5,000.

Team allocation:

Member 1: Embedded lead (firmware, drivers, logger)

Member 2: Data/model lead (dataset, Python, model fitting)

Member 3: Hardware/validation lead (probe, AFE, rig)

Member 4: Learner/support (labels, scripts, prep)

Member 5: Documentation/presentation (logbook, BOM, presentation)

Kill Criteria, Risk Register, and Decision Gates

Kill criteria:

Probe output too unstable for compensation.

Packing/insertion error dominates environmental effects.

ADS1115 provides no measurable benefit.

Salinity effect cannot be separated.

No credible gravimetric reference.

Dataset workload exceeds timeline.

Compensation worsens important subsets.

Only conventional calibration remains after grouped validation.

Risk register:

Probe variability, packing sensitivity, reference access, dataset timing, model overfit, Python/MCU mismatch, budget overrun.

Decision gates:

Week-1: Probe stability, ADC comparison, oven/scale access.

Week-2: Packing sensitivity, salinity effect, pilot model.

Confidentiality Boundary and IP Handling for Experimental Data

All new mechanisms, calibration rules, datasets, and results remain confidential until institutional IPR review.

Experimental data, grouped validation results, and candidate invention methods should be handled as confidential information in patent applications, with restricted access and secure storage until filing or publication

pulseofpatents.com

pulseofpatents.com. Understanding the Role of Confidential Information in Patent ...

.

Disclosure of confidential information prior to filing may jeopardize patent rights; NDAs and internal protocols are recommended.

Final Recommendation Options and Decision Rationale

Advance as patent-first candidate:

Only if grouped validation and confidence gating demonstrate a non-obvious, transferable calibration method with explicit validity-region detection.

Advance conditionally pending named evidence:

Recommended. Proceed with the semester prototype, focusing on grouped validation, calibration transfer, and confidence gating as the primary innovation direction.

Retain as strong semester prototype but reduce patent priority:

If grouped validation fails to produce a non-obvious method, retain TrueMoist as a valuable educational and engineering demonstration, but deprioritize patent filing.

Deprioritize under the patent-first selection criterion:

If no credible invention direction survives grouped validation and confidence gating, deprioritize TrueMoist for patent development.

Unresolved Questions and Prioritized Follow-Up Items

Can grouped validation and confidence gating produce a non-obvious, transferable calibration method?

What is the minimum achievable transfer error across commodity probes, and can it be reliably bounded?

Does confidence gating/validity-region detection prevent invalid estimates outside the calibrated domain?

Are there live claims in India or China that cover grouped calibration transfer or confidence gating?

What is the best experimental protocol for probe identification, grouped validation, and abstention testing?

How does the method perform in multi-soil or field conditions (for later extension)?

What is the optimal claim language to capture the technical contribution without overclaiming?

Source and Verification Log Format (Reproducible Provenance)

All search queries, results, and claim readings are documented by database, date, query string, and result set.

All patent family, status, and claim analyses are cross-referenced to official records (WIPO, USPTO, EPO, InPASS, CNIPA).

All technical and experimental protocols are referenced to authoritative project documents and non-patent literature.

All conclusions are traceable to specific evidence, with explicit separation of verified fact, inference, and recommendation.

End of Report

See my thinking

References

4

1margenot.cropsciences.illinois.edu

SOP: Gravimetric Water Content (GWC) Standard Operating Procedure

2www.globalpatentfiling.com

Inventive Step in Patent Law: Comparing Global Standards of Obviousness

3www.michaelmeyerlaw.com

Alice Patent Eligibility: The Complete Guide to the Alice Test (2026)

4pulseofpatents.com

Understanding the Role of Confidential Information in Patent .
