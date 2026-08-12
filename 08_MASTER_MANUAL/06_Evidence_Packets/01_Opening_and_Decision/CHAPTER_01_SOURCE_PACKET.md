# Chapter 01 — Project Mandate, Requirements and Governance

## Controlled source packet

This packet contains hash-verified source extracts. The sources have not been reconciled, corrected or converted into final manual conclusions.

Mapped sources in packet: **26**


---

## Source 1: `01_GOVERNANCE_AND_CONTROL/01_Project_Requirements/Teacher_Project_Requirements_and_Change_Context.md`

- Authority: `TIER_1`
- Treatment: `CORE_NARRATIVE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `0711a1a7fca621fa36595eff60a0f61b6a0f3edda0f597aa340f5d316b61fb05`

# Source Extraction

- Chapter: `01` — Project Mandate, Requirements and Governance
- Authority tier: `TIER_1`
- Manual treatment: `CORE_NARRATIVE`
- Original source: `01_GOVERNANCE_AND_CONTROL/01_Project_Requirements/Teacher_Project_Requirements_and_Change_Context.md`
- Current SHA-256: `0711a1a7fca621fa36595eff60a0f61b6a0f3edda0f597aa340f5d316b61fb05`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

# Teacher Project Requirements and Change Context

## Course context

- B.Tech CSE Cyber Security microcontroller semester project.
- Five team members.
- Three members are technically strong.
- One member is a learner who can perform bounded implementation, testing,
  logging and inventory work.
- One member is strongest in presentation, documentation and project support.
- Expected implementation period: up to three months.

## Teacher requirements

- Budget friendly.
- Preferred semester hardware cost at or below ₹3,000.
- Absolute semester hardware ceiling ₹5,000.
- Arduino-board or Arduino-IDE-compatible embedded implementation.
- Cybersecurity relevance is preferred.
- Low-power components.
- Very high-power components are not permitted.
- USB sample, interface or logging capability should be included.
- STM32 was mentioned during project requirements, but the final board choice
  must follow the authoritative project records and teacher approval.
- A strong live demonstration is required.

## Zeroth-review context

OpenBraille was used for the zeroth-review presentation because the final
comparative engineering, feasibility and patent-development review among the
shortlisted concepts had not yet been completed.

OpenBraille should not be described as wasted work or an abandoned mistake.

It remains:

- a valuable accessibility concept;
- a strong mechatronics learning project;
- a documented future research option;
- the basis of useful architecture, testing and patent-analysis work.

## Current request

The team wishes to request teacher approval to change the semester
implementation from OpenBraille to VibeGuard.

The primary reasons are:

- stronger three-month build feasibility;
- simpler physical implementation;
- better match with the team’s embedded, ESP32, cybersecurity and
  signal-processing strengths;
- clearer quantitative bench validation;
- stronger live demonstration;
- lower dependence on precision FDM mechanics, repeated cam/guide fabrication,
  tactile-state verification and multi-servo power behaviour;
- a comfortable expected semester budget;
- a well-bounded semester architecture.

The switch must not be justified by claiming that VibeGuard is guaranteed to
receive a patent.

The frozen VibeGuard semester MVP is treated as conventional.

Any possible future VibeGuard invention-development route is a separate,
confidential, evidence-gated programme after the semester foundation exists.

## Required final teacher documents

1. Project mC Request to Change from OpenBraille to VibeGuard.
2. VibeGuard Semester Implementation and Future Research Roadmap.
3. OpenBraille Semester Architecture and Future Research Reference Dossier.

The first document should be concise and decision-focused.

The second and third documents should provide detailed hardware, costing,
team roles, semester execution and post-semester research plans.


---

## Source 2: `01_GOVERNANCE_AND_CONTROL/02_Decision_Registers/HISTORICAL_Project_mC_Decision_Register_v1.0.md`

- Authority: `TIER_1`
- Treatment: `CORE_NARRATIVE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `875acb70b77be4f303107ce37dbc8f5cfb7d4f278089cdf4317f52d1c8ee668d`

# Source Extraction

- Chapter: `01` — Project Mandate, Requirements and Governance
- Authority tier: `TIER_1`
- Manual treatment: `CORE_NARRATIVE`
- Original source: `01_GOVERNANCE_AND_CONTROL/02_Decision_Registers/HISTORICAL_Project_mC_Decision_Register_v1.0.md`
- Current SHA-256: `875acb70b77be4f303107ce37dbc8f5cfb7d4f278089cdf4317f52d1c8ee668d`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

> HISTORICAL / SUPERSEDED DOCUMENT
> This register is preserved for decision-history traceability.
> The current authoritative register is Project_mC_Decision_Register_v1.2.md.

### Project mC Decision Register — Version 1.0

**Document Control Header**
*   **Version:** 1.0
*   **Current project stage:** Phase 3C in progress
*   **Phase 3C completed concepts:** OpenBraille and VibeGuard
*   **Phase 3C pending concepts:** TrueMoist, TrustLatch and ColdTrace
*   **Authoritative as of:** current uploaded source set

***

#### Part I: Methodology & Project Management

**Decision ID:** PDR-001
**Title:** Project Budget Ceiling
**Phase introduced:** Phase 1A
**Category:** Methodology & Project Management
**Decision or requirement:** Cap prototype budget at a maximum of ₹5,000 INR, with a preferred target of ≤ ₹3,000 INR.
**Rationale:** Ensures the project remains a low-cost, frugal innovation suitable for a student team and scalable in resource-constrained environments.
**Source evidence:** `MC_Project_PHASE_DOC.md`
**Alternatives:** Unconstrained budget.
**Decision type:** Requirement
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-002

**Decision ID:** PDR-002
**Title:** Project Timeline & Team Scope
**Phase introduced:** Phase 1A
**Category:** Methodology & Project Management
**Decision or requirement:** Restrict the prototype timeline to approximately 2 months, executable by a 5-member team (three technically strong CS/Cybersecurity students).
**Rationale:** Fits within standard academic semester constraints and dictates that mechanical complexity must be minimized or shifted to software.
**Source evidence:** `PROJECT_CONCEPT_CONTEXT.md`
**Alternatives:** Professional mechanical outsourcing.
**Decision type:** Requirement
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-038

**Decision ID:** PDR-003
**Title:** Deferral of Hardware Implementation Decisions
**Phase introduced:** Project Foundation
**Category:** Methodology & Project Management
**Decision or requirement:** Phase 3C selects and freezes the prototype architecture, including provisional MCU, sensor, actuator, interface and power choices. Phase 6 converts those architecture selections into procurement-ready component variants, schematics, PCB design, firmware implementation and manufacturing specifications.
**Rationale:** Prevents premature solution generation and ensures decisions remain problem-focused rather than technology-driven.
**Source evidence:** `MC_Project_PHASE_DOC.md`
**Alternatives:** Early component selection.
**Decision type:** Requirement
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-040, PDR-043

**Decision ID:** PDR-004
**Title:** Evidence Exclusion over Averaging Protocol
**Phase introduced:** Phase 2 / Phase 3A
**Category:** Methodology & Project Management
**Decision or requirement:** Entire sections of AI deep research reports that suffer from "concept-swap" or interpretation drift must be excluded completely, rather than down-weighted or averaged into the synthesis.
**Rationale:** Averaging hallucinated or mis-scoped data corrupts the engineering baseline.
**Source evidence:** `Phase3A_MEMORY.md`, `Claudes report on the research Phases 3a.pdf`
**Alternatives:** Blending or averaging hallucinated findings.
**Decision type:** Final decision
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-006, PDR-041

**Decision ID:** PDR-005
**Title:** Split-Maturity Assessment Method
**Phase introduced:** Phase 3A
**Category:** Methodology & Project Management
**Decision or requirement:** Evaluate engineering readiness on a two-tier scale: Base Domain Maturity vs. Specific Innovation Maturity.
**Rationale:** Resolves contradictions where an AI model rates a concept mature at the industry level while another rates the specific innovation edge algorithm as emerging.
**Source evidence:** `Claudes report on the research Phases 3a.pdf`
**Alternatives:** Single-figure maturity calls.
**Decision type:** Final decision
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** None

**Decision ID:** PDR-006
**Title:** Mandatory Concept Grounding/Confirmation Step
**Phase introduced:** Phase 3A / Phase 3B
**Category:** Methodology & Project Management
**Decision or requirement:** Require Deep Research passes to restate and confirm their understanding against the Engineering Design Review document before analyzing.
**Rationale:** Proved to be a leading indicator of report reliability; reports skipping this step consistently produced concept-swap hallucinations.
**Source evidence:** `Phase3B_MEMORY.md`
**Alternatives:** Relying on short-form project names.
**Decision type:** Requirement
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-042

**Decision ID:** PDR-039
**Title:** Multi-AI Independent Research Strategy
**Phase introduced:** Phase 1A
**Category:** Methodology & Project Management
**Decision or requirement:** Utilize multiple independent Deep Research systems simultaneously rather than a single model.
**Rationale:** Redundancy increases confidence in recurring opportunities and mitigates single-model hallucination.
**Source evidence:** `Phase1A_Memory.md`
**Alternatives:** Single AI pipeline.
**Decision type:** Requirement
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-041

**Decision ID:** PDR-040
**Title:** Prohibition of Premature Solution Generation
**Phase introduced:** Phase 1A / Phase 1B
**Category:** Methodology & Project Management
**Decision or requirement:** Strictly prohibit the invention of products, architectures, or solutions during early phases.
**Rationale:** Ensures the project remains focused on validating real-world problems before engineering solutions.
**Source evidence:** `MC_Project_PHASE_DOC.md`
**Alternatives:** Brainstorming hardware solutions early.
**Decision type:** Requirement
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** No (Phase specific)
**Related PDR entries:** PDR-003

**Decision ID:** PDR-041
**Title:** Duplicate Preservation for Confidence Scoring
**Phase introduced:** Phase 1B
**Category:** Methodology & Project Management
**Decision or requirement:** Preserve duplicate findings from different AIs prior to consolidation to measure cross-report confidence.
**Rationale:** Independent convergence by multiple systems on the same problem acts as decision-grade evidence.
**Source evidence:** `Phase1B_Memory.md`
**Alternatives:** Immediate deletion of duplicates.
**Decision type:** Requirement
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-039

**Decision ID:** PDR-042
**Title:** Authoritative Precedence of the EDR Document
**Phase introduced:** Phase 3B
**Category:** Methodology & Project Management
**Decision or requirement:** The Engineering Design Review (EDR) overrides the Phase 1C Report and short-form contexts wherever they differ.
**Rationale:** Short-form descriptions caused interpretation drift in Phase 2 and 3A; the EDR provides unambiguous constraints.
**Source evidence:** `Phase3B_Report_by_Claude.md`
**Alternatives:** Continuing to use PROJECT_CONCEPT_CONTEXT.md as the primary anchor.
**Decision type:** Requirement
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-006

**Decision ID:** PDR-043
**Title:** Phase 3C Architecture Selection Mandate
**Phase introduced:** Phase 3C
**Category:** Methodology & Project Management
**Decision or requirement:** Phase 3C must resolve technical disagreements and select *one* final architecture, rather than preserving forks.
**Rationale:** Phase 3C's output must serve as an actual, unambiguous build blueprint for Phase 4 prototyping.
**Source evidence:** `Claudes report for openbraille phase 3c.md`
**Alternatives:** Preserving strategic forks into Phase 4.
**Decision type:** Requirement
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-003

***

#### Part II: Portfolio, Commercialization & Patent Strategy

**Decision ID:** PDR-007
**Title:** Portfolio Gate Evaluation Filtering
**Phase introduced:** Phase 1B.5
**Category:** Portfolio & Commercialization & Patent Strategy
**Decision or requirement:** Apply 8 strict engineering decision gates to filter the opportunity portfolio.
**Rationale:** Ensures only technically feasible, budget-compliant projects advance.
**Source evidence:** `Phase1B5_Memory.md`
**Alternatives:** Advancing all clusters.
**Decision type:** Final decision
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** No (Phase specific)
**Related PDR entries:** PDR-008

**Decision ID:** PDR-008
**Title:** Selection of Top 5 Concepts
**Phase introduced:** Phase 1C
**Category:** Portfolio & Commercialization & Patent Strategy
**Decision or requirement:** Advance OpenBraille, VibeGuard, TrueMoist, TrustLatch, and ColdTrace to Phase 2/3.
**Rationale:** These 5 concepts represented the strongest balance of originality, patent potential, feasibility, and embedded necessity.
**Source evidence:** `Phase1C_Memory.md`
**Alternatives:** Advancing other clusters like SiliconFingerprint.
**Decision type:** Final decision
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-007

**Decision ID:** PDR-009
**Title:** OpenBraille IP Pivot
**Phase introduced:** Phase 2
**Category:** Portfolio & Commercialization & Patent Strategy
**Decision or requirement:** Redirect the patent target away from the physical actuation mechanism and toward manufacturing methods and firmware control.
**Rationale:** The actuator space is fenced by Dot Inc. and expired art (SMA/EAP); manufacturing methods and firmware remain viable white space.
**Source evidence:** `Phase2_Report by CLaude.md`, `QWen Research on Patent.pdf`
**Alternatives:** Patenting the physical mechanism.
**Decision type:** Recommendation
**Verification status:** Partially Verified
**Current status:** Recommendation
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-015

**Decision ID:** PDR-010
**Title:** ColdTrace Freedom-to-Operate Condition
**Phase introduced:** Phase 2
**Category:** Portfolio & Commercialization & Patent Strategy
**Decision or requirement:** Mandate an FTO check on US 10,887,735 (Sensitech) before committing to a physical thermal-mass architecture.
**Rationale:** Avoid infringement on active physical buffered-sensor chamber patents simulating vaccine thermal physics.
**Source evidence:** `Phase2_Report by CLaude.md`, `Kimi Patent Research.pdf`
**Alternatives:** Proceeding blindly into physical buffers.
**Decision type:** Requirement
**Verification status:** Partially Verified
**Current status:** Requirement
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-034

**Decision ID:** PDR-011
**Title:** TrustLatch IP Abandonment (Strategic Fork)
**Phase introduced:** Phase 2
**Category:** Portfolio & Commercialization & Patent Strategy
**Decision or requirement:** Evaluate whether to advance TrustLatch as an open-core product/academic deliverable without budgeting for a patent filing on cryptography/boot-chain mechanics.
**Rationale:** The space is fundamentally saturated by silicon giants and open-source standards; this represents a genuine strategic fork requiring project owner resolution.
**Source evidence:** `Phase2_Report by CLaude.md`, `QWen Research on Patent.pdf`
**Alternatives:** Forcing a patent filing.
**Decision type:** Open question
**Verification status:** Partially Verified
**Current status:** Open question
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-047

**Decision ID:** PDR-045
**Title:** TrueMoist Custom Hardware IP Abandonment
**Phase introduced:** Phase 2
**Category:** Portfolio & Commercialization & Patent Strategy
**Decision or requirement:** Confine all TrueMoist IP efforts strictly to the edge-AI algorithmic software layer, utilizing unmodified off-the-shelf commodity sensors.
**Rationale:** Designing custom probes with integrated EC/Temp/Capacitance directly infringes on aggressively defended utility patents by Toro, Meter Group, and Campbell.
**Source evidence:** `Phase2_Report by CLaude.md`, `QWen Research on Patent.pdf`
**Alternatives:** Patenting the physical hardware probe.
**Decision type:** Recommendation
**Verification status:** Partially Verified
**Current status:** Recommendation
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-031

**Decision ID:** PDR-046
**Title:** VibeGuard SME Commercial Wedge
**Phase introduced:** Phase 2
**Category:** Portfolio & Commercialization & Patent Strategy
**Decision or requirement:** Position VibeGuard commercially around zero-subscription economics and single-node processing for SMEs.
**Rationale:** The enterprise PdM space is saturated by funded platforms; the defensible moat is deployment economics for SMEs.
**Source evidence:** `Phase2_Report by CLaude.md`, `QWen Research on Patent.pdf`
**Alternatives:** Enterprise cloud-platform subscription models.
**Decision type:** Recommendation
**Verification status:** Partially Verified
**Current status:** Recommendation
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-027

**Decision ID:** PDR-047
**Title:** TrustLatch Compliance-Driven Commercial Strategy
**Phase introduced:** Phase 2 / Phase 3A
**Category:** Portfolio & Commercialization & Patent Strategy
**Decision or requirement:** Execute an open-core commercial strategy that gives away reference ports while monetizing EU Cyber Resilience Act (CRA) / UK PSTI compliance automation and fleet key management.
**Rationale:** The market forcing function is regulatory compliance for constrained OEMs, not novel cryptography.
**Source evidence:** `Kimi Patent Research.pdf`
**Alternatives:** Proprietary enterprise licensing.
**Decision type:** Recommendation
**Verification status:** Partially Verified
**Current status:** Recommendation
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-011

**Decision ID:** PDR-057
**Title:** Trademark vs. Utility Patent Separation
**Phase introduced:** Phase 2
**Category:** Portfolio & Commercialization & Patent Strategy
**Decision or requirement:** Separate trademark observations/collisions from utility patentability conclusions during IP landscaping.
**Rationale:** Name collisions (e.g., Nexleaf ColdTrace product instead of the concept) cause interpretation drift and must be handled distinctly from technical prior art.
**Source evidence:** `MC_Project_PHASE_DOC.md`
**Alternatives:** Blended IP assessments.
**Decision type:** Requirement
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-004

***

#### Part III: Validation, Testing & Feasibility

**Decision ID:** PDR-012
**Title:** TrueMoist Validation Gate
**Phase introduced:** Phase 2 / Phase 3A
**Category:** Validation, Testing & Feasibility
**Decision or requirement:** Hold TrueMoist for a two-season, multi-soil validation sprint.
**Rationale:** Calibration-free operation across varying soil types using self-calibration algorithms is unproven in open literature.
**Source evidence:** `Phase2_Report by CLaude.md`
**Alternatives:** Advancing to production design immediately.
**Decision type:** Future validation task
**Verification status:** Partially Verified
**Current status:** Future validation task
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-048, PDR-049

**Decision ID:** PDR-013
**Title:** VibeGuard Validation Gate
**Phase introduced:** Phase 2 / Phase 3B
**Category:** Validation, Testing & Feasibility
**Decision or requirement:** Mandate a real dense-machine field test to validate single-node spatial attribution before scaling.
**Rationale:** Theoretical blind source separation algorithms often fail in acoustically coupled environments.
**Source evidence:** `Phase2_Report by CLaude.md`
**Alternatives:** Assuming lab data transfers perfectly to factories.
**Decision type:** Future validation task
**Verification status:** Partially Verified
**Current status:** Future validation task
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-027

**Decision ID:** PDR-014
**Title:** Cross-Portfolio Shared MCU Platform
**Phase introduced:** Phase 3B
**Category:** Validation, Testing & Feasibility
**Decision or requirement:** Standardize on the ESP32 (or STM32 with FPU) as the primary microcontroller across all five concepts.
**Rationale:** Provides abundant GPIO, hardware floating-point capabilities, and aligns with the team's skillset as a shared platform investment.
**Source evidence:** `Phase3B_Report_by_Claude.md`
**Alternatives:** RP2040, Arduino Uno.
**Decision type:** Provisional architecture selection
**Verification status:** Partially Verified
**Current status:** Provisional architecture selection
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-017, PDR-025

**Decision ID:** PDR-048
**Title:** TrueMoist Gravimetric Validation Standard
**Phase introduced:** Phase 3A / Phase 3B
**Category:** Validation, Testing & Feasibility
**Decision or requirement:** Require gravimetric analysis (oven-drying soil samples at 105°C) as the absolute baseline for validation.
**Rationale:** It is the only physical ground truth; electronic sensors must trace back to this rather than referencing other commercial sensors.
**Source evidence:** `Phase3B_Report_by_Claude.md`, `Claudes report on the research Phases 3a.pdf`
**Alternatives:** Validating against commercial IoT sensors.
**Decision type:** Requirement
**Verification status:** Partially Verified
**Current status:** Requirement
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-012, PDR-031

**Decision ID:** PDR-056
**Title:** ColdTrace Validation Test
**Phase introduced:** Phase 3B / Phase 3C
**Category:** Validation, Testing & Feasibility
**Decision or requirement:** The validation test must directly compare a controlled short-duration disturbance (e.g., door-opening spike) against a controlled sustained thermal excursion.
**Rationale:** This is the only physical method to prove the firmware effectively dampens false alarms while catching real failures.
**Source evidence:** `Phase3B_Report_by_Claude.md`
**Alternatives:** Standard ambient thermal logging.
**Decision type:** Requirement
**Verification status:** Partially Verified
**Current status:** Requirement
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-034

***

#### Part IV: Concept-Specific Architecture

##### OpenBraille
**Decision ID:** PDR-015
**Title:** OpenBraille Actuation Principle
**Phase introduced:** Phase 3C
**Category:** Concept-Specific Architecture (OpenBraille)
**Decision or requirement:** Servo + Cam linkage.
**Rationale:** Retires fabrication-tolerance risk, requires no custom driver electronics (servos self-drive), no continuous-hold thermal fault mode.
**Source evidence:** `Claudes report for openbraille phase 3c.md`, `Phase3C_OpenBraille_Memory.md`
**Alternatives:** Electromagnetic latching micro-coils, non-latching solenoid, Shape Memory Alloy.
**Decision type:** Final decision
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-018, PDR-019

**Decision ID:** PDR-016
**Title:** OpenBraille Dot-Pitch Compliance
**Phase introduced:** Phase 3C
**Category:** Concept-Specific Architecture (OpenBraille)
**Decision or requirement:** Adopt a permanent macro-scale (~300% of ISO 17049, ≈7 mm pitch, ≈1.5 mm dot height) for the prototype, explicitly abandoning dimensional compliance.
**Rationale:** Standard FDM 3D printers cannot achieve the precision required; macro-scaling neutralizes manufacturing risk while proving hypothesis.
**Source evidence:** `Claudes report for openbraille phase 3c.md`, `Phase3C_OpenBraille_Memory.md`
**Alternatives:** 100% scale outsourced SLA printing.
**Decision type:** Final decision
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-015

**Decision ID:** PDR-017
**Title:** OpenBraille MCU Selection
**Phase introduced:** Phase 3C
**Category:** Concept-Specific Architecture (OpenBraille)
**Decision or requirement:** ESP32-WROOM-32 DevKit.
**Rationale:** Offers 30+ GPIO pins (ample for PWM), hardware timers for jitter-free PWM, low cost, and team familiarity.
**Source evidence:** `Claudes report for openbraille phase 3c.md`, `Phase3C_OpenBraille_Memory.md`
**Alternatives:** STM32F103 "Blue Pill", Arduino Uno.
**Decision type:** Final decision
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-014

**Decision ID:** PDR-018
**Title:** OpenBraille Driver Architecture
**Phase introduced:** Phase 3C
**Category:** Concept-Specific Architecture (OpenBraille)
**Decision or requirement:** Centralized ESP32 control with direct GPIO PWM to each servo; no intermediate driver ICs.
**Rationale:** SG90 servos integrate their own driver circuitry, eliminating a subsystem and its failure modes entirely.
**Source evidence:** `Claudes report for openbraille phase 3c.md`, `Phase3C_OpenBraille_Memory.md`
**Alternatives:** Shift-register SPI multiplexing, H-Bridge arrays.
**Decision type:** Final decision
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-015

**Decision ID:** PDR-019
**Title:** OpenBraille Manufacturing Pathway
**Phase introduced:** Phase 3C
**Category:** Concept-Specific Architecture (OpenBraille)
**Decision or requirement:** In-house FDM 3D printing (ABS frame, PETG/Nylon cams) plus off-the-shelf components; no outsourced fabrication.
**Rationale:** Keeps fabrication within team tools and timeline, avoiding commercial SLA outsourcing dependencies.
**Source evidence:** `Claudes report for openbraille phase 3c.md`, `Phase3C_OpenBraille_Memory.md`
**Alternatives:** Commercial SLA printing, Laser cutting.
**Decision type:** Final decision
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-016

**Decision ID:** PDR-020
**Title:** OpenBraille Power Architecture
**Phase introduced:** Phase 3C
**Category:** Concept-Specific Architecture (OpenBraille)
**Decision or requirement:** External 5V/2A DC adapter with a 1000 µF decoupling capacitor across the servo rail.
**Rationale:** Servos draw high peak current. USB bus power (500mA limit) risks brown-out resets; decoupling eliminates transient voltage sags.
**Source evidence:** `Claudes report for openbraille phase 3c.md`, `Phase3C_OpenBraille_Memory.md`
**Alternatives:** USB bus power, 6V AA Battery pack.
**Decision type:** Final decision
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-015

**Decision ID:** PDR-021
**Title:** OpenBraille Reset Mechanism
**Phase introduced:** Phase 3C
**Category:** Concept-Specific Architecture (OpenBraille)
**Decision or requirement:** Utilize the SG90 servo's integrated torsion spring for pin reset.
**Rationale:** Removes an external component (compression springs) and a failure mode present in solenoid alternatives.
**Source evidence:** `Claudes report for openbraille phase 3c.md`
**Alternatives:** External compression/leaf springs.
**Decision type:** Requirement
**Verification status:** Source verified, technically unvalidated
**Current status:** Pending physical inspection and prototype testing
**Required correction:** Confirm whether the selected servo provides a usable passive return mechanism. Otherwise, document active servo-driven cam retraction as the reset method.
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-015

**Decision ID:** PDR-022
**Title:** OpenBraille Validation Strategy
**Phase introduced:** Phase 3C
**Category:** Concept-Specific Architecture (OpenBraille)
**Decision or requirement:** Bottom-up, single-dot-first integration sequence (M1-M8), culminating in tactile validation.
**Rationale:** Isolates structural friction/mechanical variables from electrical variables before integrating all 6 pins.
**Source evidence:** `Claudes report for openbraille phase 3c.md`, `Phase3C_OpenBraille_Memory.md`
**Alternatives:** Assembling all 6 dots at once.
**Decision type:** Final decision
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-016

##### VibeGuard
**Decision ID:** PDR-023
**Title:** VibeGuard Sensor Selection
**Phase introduced:** Phase 3C
**Category:** Concept-Specific Architecture (VibeGuard)
**Decision or requirement:** ADXL345 (3-axis digital MEMS accelerometer).
**Rationale:** Adequate bandwidth (1600 Hz Nyquist) for MVP low-frequency tests; lowest cost; best-documented implementation.
**Source evidence:** `Phase3C_VibeGuard_Architecture_Report By Claude.md`, `Phase3C_VibeGuard_Memory.md`
**Alternatives:** IIS3DWB, MPU6050, ADXL1002.
**Decision type:** Final decision
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-055

**Decision ID:** PDR-024
**Title:** VibeGuard Sensor Interface
**Phase introduced:** Phase 3C
**Category:** Concept-Specific Architecture (VibeGuard)
**Decision or requirement:** High-speed SPI Bus (stepped down to 1-2 MHz for breadboards).
**Rationale:** I2C's 400kHz fast-mode causes buffer overflow at the 3200Hz Output Data Rate needed for maximum bandwidth.
**Source evidence:** `Phase3C_VibeGuard_Architecture_Report By Claude.md`
**Alternatives:** I2C protocol.
**Decision type:** Final decision
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-023

**Decision ID:** PDR-025
**Title:** VibeGuard MCU Selection
**Phase introduced:** Phase 3C
**Category:** Concept-Specific Architecture (VibeGuard)
**Decision or requirement:** ESP32 (WROOM-32 or S3-class).
**Rationale:** Provides Hardware Floating-Point Unit (FPU) necessary for real-time FFT, 520KB SRAM for windowed buffers, and DMA-capable peripheral bus.
**Source evidence:** `Phase3C_VibeGuard_Architecture_Report By Claude.md`
**Alternatives:** STM32 F4-class, Arduino Uno, RP2040.
**Decision type:** Final decision
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-014

**Decision ID:** PDR-026
**Title:** VibeGuard Edge Intelligence / Classification
**Phase introduced:** Phase 3C
**Category:** Concept-Specific Architecture (VibeGuard)
**Decision or requirement:** Tiered processing: Time-domain features crossing a threshold triggers a windowed FFT; primary classification relies on a calibrated RMS threshold, scaling to unsupervised Mahalanobis-distance anomaly detection.
**Rationale:** Meets MDS with deterministic thresholds immediately; avoids need for labeled failure datasets required by supervised Deep Learning.
**Source evidence:** `Phase3C_VibeGuard_Architecture_Report By Claude.md`
**Alternatives:** Supervised Deep-learning TinyML (CNN/Autoencoders).
**Decision type:** Final decision
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-054

**Decision ID:** PDR-027
**Title:** VibeGuard Noise Isolation Strategy
**Phase introduced:** Phase 3C
**Category:** Concept-Specific Architecture (VibeGuard)
**Decision or requirement:** Baseline spectral subtraction combined with proximity mounting and band-limited features.
**Rationale:** ESP32 cannot compute complex BSS matrix inversions. The adequacy of spectral subtraction is empirically testable only once a physical rig exists.
**Source evidence:** `Phase3C_VibeGuard_Architecture_Report By Claude.md`
**Alternatives:** FastICA / SSA / EEMD.
**Decision type:** Future validation task
**Verification status:** Partially Verified
**Current status:** Future validation task
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-013

**Decision ID:** PDR-028
**Title:** VibeGuard Mechanical Mounting
**Phase introduced:** Phase 3C
**Category:** Concept-Specific Architecture (VibeGuard)
**Decision or requirement:** Absolute rigid mounting (epoxy/cyanoacrylate to a bracket, bolted directly to motor casing).
**Rationale:** Loose mounting acts as an unintended mechanical low-pass filter, permanently destroying the high-frequency vibration signals.
**Source evidence:** `Phase3C_VibeGuard_Architecture_Report By Claude.md`
**Alternatives:** Magnetic mounts, foam adhesive.
**Decision type:** Final decision
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-023

**Decision ID:** PDR-029
**Title:** VibeGuard Output Indication
**Phase introduced:** Phase 3C
**Category:** Concept-Specific Architecture (VibeGuard)
**Decision or requirement:** Common-cathode RGB LED (Green = Normal, Red = Abnormal, Blue = Calibrating).
**Rationale:** Directly satisfies the MDS requirement for "clear output" without imposing complex OLED display code on the MVP.
**Source evidence:** `Phase3C_VibeGuard_Architecture_Report By Claude.md`, `Phase3C_VibeGuard_Memory.md`
**Alternatives:** OLED/LCD screen.
**Decision type:** Final decision
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** None

**Decision ID:** PDR-030
**Title:** VibeGuard Test Scenario
**Phase introduced:** Phase 3C
**Category:** Concept-Specific Architecture (VibeGuard)
**Decision or requirement:** Small 12V DC motor or PC fan mounted on a heavy damped base, tested by artificially attaching an eccentric mass to induce unbalance.
**Rationale:** Creates a safe, low-voltage, repeatable abnormal condition demonstrating the MDS without needing access to real failing industrial machinery.
**Source evidence:** `Phase3C_VibeGuard_Architecture_Report By Claude.md`, `Phase3C_VibeGuard_Memory.md`
**Alternatives:** Loosened mounting bolts.
**Decision type:** Final decision
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-026

**Decision ID:** PDR-054
**Title:** VibeGuard Pipeline Sequence
**Phase introduced:** Phase 3C
**Category:** Concept-Specific Architecture (VibeGuard)
**Decision or requirement:** Standardize pipeline order: DC removal → Hann Windowing → Time-domain features (RMS/Peak) → Triggered FFT.
**Rationale:** Controls compute load on constrained MCU; Hann windowing prevents spectral leakage during finite-block FFTs.
**Source evidence:** `Phase3C_VibeGuard_Architecture_Report By Claude.md`, `Phase3C_VibeGuard_Memory.md`
**Alternatives:** Continuous FFT processing.
**Decision type:** Final decision
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-026

**Decision ID:** PDR-055
**Title:** VibeGuard Sensor Upgrade Path
**Phase introduced:** Phase 3C
**Category:** Concept-Specific Architecture (VibeGuard)
**Decision or requirement:** Document the IIS3DWB (6000 Hz) as the designated upgrade path for bearing-fault detection, while retaining ADXL345 for the MVP.
**Rationale:** Prevents cost overrun on the MVP while documenting exactly how to restore the advanced capability for future iterations.
**Source evidence:** `Phase3C_VibeGuard_Architecture_Report By Claude.md`, `Phase3C_VibeGuard_Memory.md`
**Alternatives:** Mandating the IIS3DWB immediately.
**Decision type:** Recommendation
**Verification status:** Verified
**Current status:** Documented future upgrade path — not part of the MVP
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-023

##### TrueMoist
**Decision ID:** PDR-031
**Title:** TrueMoist Compensation Method
**Phase introduced:** Phase 3B
**Category:** Concept-Specific Architecture (TrueMoist)
**Decision or requirement:** Utilize multivariate polynomial regression (Temperature + Electrical Conductivity/Salinity) dynamically to correct raw capacitive moisture readings.
**Rationale:** Corrects for Maxwell-Wagner interfacial polarization and ionic drift without requiring cloud connectivity purely in software.
**Source evidence:** `Phase3B_Report_by_Claude.md`
**Alternatives:** Threshold-based control, AD5933 Impedance Analyzer.
**Decision type:** Provisional architecture selection
**Verification status:** Partially Verified
**Current status:** Provisional architecture selection
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-045, PDR-049

**Decision ID:** PDR-032
**Title:** TrueMoist ADC Selection
**Phase introduced:** Phase 3B
**Category:** Concept-Specific Architecture (TrueMoist)
**Decision or requirement:** Evaluate whether to mandate the use of an external 16-bit ADC (e.g., ADS1115).
**Rationale:** The ESP32’s internal ADCs are highly non-linear and noisy, which may mask the microscopic capacitance changes mapped by the algorithm.
**Source evidence:** `Phase3B_Report_by_Claude.md`
**Alternatives:** Native MCU ADC.
**Decision type:** Open question
**Verification status:** Partially Verified
**Current status:** Open question
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-031

**Decision ID:** PDR-049
**Title:** TrueMoist Single-Soil Limit
**Phase introduced:** Phase 3B
**Category:** Concept-Specific Architecture (TrueMoist)
**Decision or requirement:** Restrict the prototype calibration scope to a single, homogeneous soil type.
**Rationale:** Attempting to generalize a regression model across multiple soil types (e.g., sand vs. heavy clay) in 2 months will over-fit and output garbage.
**Source evidence:** `Phase3B_Report_by_Claude.md`
**Alternatives:** Multi-soil generalization.
**Decision type:** Provisional architecture selection
**Verification status:** Partially Verified
**Current status:** Provisional architecture selection
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-012

**Decision ID:** PDR-050
**Title:** TrueMoist AFE Soldering
**Phase introduced:** Phase 3B / Phase 3C
**Category:** Concept-Specific Architecture (TrueMoist)
**Decision or requirement:** Solder the analog front-end connections as early as possible in the build process.
**Rationale:** Unshielded breadboards introduce parasitic capacitance and electrical noise that easily masks the microscopic drift signals.
**Source evidence:** `Phase3B_Report_by_Claude.md`
**Alternatives:** Solderless breadboard prototyping.
**Decision type:** Recommendation
**Verification status:** Partially Verified
**Current status:** Recommendation
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-031

##### TrustLatch
**Decision ID:** PDR-033
**Title:** TrustLatch Firmware Scope
**Phase introduced:** Phase 3B
**Category:** Concept-Specific Architecture (TrustLatch)
**Decision or requirement:** Scope the MVP to boot-time firmware integrity verification only, single-slot.
**Rationale:** Fitting a bootloader, full crypto suite, and dual-bank OTA exhausts the 64-128KB flash memory of Cortex-M0/M3 MCUs.
**Source evidence:** `Phase3B_Report_by_Claude.md`
**Alternatives:** Dual-bank OTA updates with Mbed TLS.
**Decision type:** Provisional architecture selection
**Verification status:** Partially Verified
**Current status:** Provisional architecture selection
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-011

**Decision ID:** PDR-051
**Title:** TrustLatch Crypto Library
**Phase introduced:** Phase 3B
**Category:** Concept-Specific Architecture (TrustLatch)
**Decision or requirement:** Mandate lightweight cryptographic libraries (TinyCrypt or micro-ecc) over full Mbed TLS.
**Rationale:** Full Mbed TLS exhausts MCU flash memory; using it on a constrained MCU will overwrite application space.
**Source evidence:** `Phase3B_Report_by_Claude.md`
**Alternatives:** Full Mbed TLS suite.
**Decision type:** Provisional architecture selection
**Verification status:** Partially Verified
**Current status:** Provisional architecture selection
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-033

**Decision ID:** PDR-052
**Title:** TrustLatch ST-Link Mandate
**Phase introduced:** Phase 3B
**Category:** Concept-Specific Architecture (TrustLatch)
**Decision or requirement:** Use the ST-Link programmer rather than J-Link for development.
**Rationale:** The J-Link hardware pushes the prototype cost to ₹4800–6700, breaching the strict project budget ceiling.
**Source evidence:** `Phase3B_Report_by_Claude.md`
**Alternatives:** Segger J-Link.
**Decision type:** Recommendation
**Verification status:** Partially Verified
**Current status:** Recommendation
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-001

**Decision ID:** PDR-053
**Title:** TrustLatch Compiled-In Keys
**Phase introduced:** Phase 3B
**Category:** Concept-Specific Architecture (TrustLatch)
**Decision or requirement:** Accept compiled-in keys as a documented, deliberate limitation for the prototype.
**Rationale:** Genuine production-grade secure key provisioning at manufacturing scale is a logistics problem that exceeds the timeline constraint.
**Source evidence:** `Phase3B_Report_by_Claude.md`
**Alternatives:** External secure elements (ATECC608).
**Decision type:** Provisional architecture selection
**Verification status:** Partially Verified
**Current status:** Provisional architecture selection
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-033

##### ColdTrace
**Decision ID:** PDR-034
**Title:** ColdTrace Modeling Scope
**Phase introduced:** Phase 3B
**Category:** Concept-Specific Architecture (ColdTrace)
**Decision or requirement:** Utilize a Virtual Thermal Mass model (Lumped-capacitance equations in firmware) combined with accelerometer shock fusion.
**Rationale:** Bypasses the US 10,887,735 FTO risk associated with physical buffered probes while still filtering out benign door-opening spikes.
**Source evidence:** `Phase3B_Report_by_Claude.md`
**Alternatives:** Physical buffer chamber/glycol bottles.
**Decision type:** Provisional architecture selection
**Verification status:** Partially Verified
**Current status:** Provisional architecture selection
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-010

**Decision ID:** PDR-035
**Title:** ColdTrace PCM Exclusion
**Phase introduced:** Phase 3B
**Category:** Concept-Specific Architecture (ColdTrace)
**Decision or requirement:** Explicitly exclude Phase-Change Material (PCM) melting plateau modeling from the MVP.
**Rationale:** Modeling non-linear latent heat without an internal physical sensor is mathematically difficult and overwhelms the timeline.
**Source evidence:** `Phase3B_Report_by_Claude.md`
**Alternatives:** Incorporating PCM modeling.
**Decision type:** Provisional architecture selection
**Verification status:** Partially Verified
**Current status:** Provisional architecture selection
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-034

**Decision ID:** PDR-036
**Title:** ColdTrace Testing Limit
**Phase introduced:** Phase 3B
**Category:** Concept-Specific Architecture (ColdTrace)
**Decision or requirement:** Restrict prototype testing to standard refrigerator temperatures.
**Rationale:** Prevents catastrophic battery collapse and MCU brownouts that occur with Li-Ion/LiPo cells at deep-freeze or cryogenic extremes.
**Source evidence:** `Phase3B_Report_by_Claude.md`
**Alternatives:** Testing at freezer/cryogenic temps.
**Decision type:** Requirement
**Verification status:** Partially Verified
**Current status:** Requirement
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-056

**Decision ID:** PDR-037
**Title:** ColdTrace RTC Module
**Phase introduced:** Phase 3B
**Category:** Concept-Specific Architecture (ColdTrace)
**Decision or requirement:** Treat whether to include a Real-Time Clock (DS3231) as an open question for the MVP.
**Rationale:** The EDR MDS only requires distinguishing transient vs. sustained events, not producing a cryptographically secure, tamper-evident audit trail.
**Source evidence:** `Phase3B_Report_by_Claude.md`
**Alternatives:** Mandating RTC for deep sleep/timestamps.
**Decision type:** Open question
**Verification status:** Partially Verified
**Current status:** Open question
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-034

***

#### Part V: Administration

**Decision ID:** PDR-038
**Title:** Team Roster Clarification
**Phase introduced:** Phase 3C
**Category:** Administration
**Decision or requirement:** The team operates as a five-member unit (Three technically capable CS/Cybersecurity members, One beginner/learner, One presenter/support member).
**Rationale:** Resolves documentation inconsistency across `vibeguard_sop.md` and prompts.
**Source evidence:** `Phase3C_VibeGuard_Architecture_Report By Claude.md`
**Alternatives:** 6 members.
**Decision type:** Final decision
**Verification status:** Verified
**Current status:** Accepted and Resolved
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-002, PDR-044

**Decision ID:** PDR-044
**Title:** Beginner Programmer Tasks
**Phase introduced:** Phase 3C
**Category:** Administration
**Decision or requirement:** Assign the team's beginner programmer highly isolated software modules (e.g., Unicode-to-Braille lookup, LED state machines) early in the schedule.
**Rationale:** Provides a genuine embedded-systems learning opportunity without placing the critical path or physical integration at risk.
**Source evidence:** `Claudes report for openbraille phase 3c.md`, `Phase3C_OpenBraille_Claude_Synthesis_Prompt.md`, `Phase3C_VibeGuard_Architecture_Report By Claude.md`
**Alternatives:** Assigning critical path DSP or mechanical tasks to the beginner.
**Decision type:** Recommendation
**Verification status:** Verified
**Current status:** Recommended team allocation
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-038


---

## Source 3: `01_GOVERNANCE_AND_CONTROL/02_Decision_Registers/Project_mC_Decision_Register_v1.2.md`

- Authority: `TIER_1`
- Treatment: `CORE_NARRATIVE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `9678c5072d86ef38e48372f940ec91396b7ac7bcbeed0124ac8e2485307f408c`

# Source Extraction

- Chapter: `01` — Project Mandate, Requirements and Governance
- Authority tier: `TIER_1`
- Manual treatment: `CORE_NARRATIVE`
- Original source: `01_GOVERNANCE_AND_CONTROL/02_Decision_Registers/Project_mC_Decision_Register_v1.2.md`
- Current SHA-256: `9678c5072d86ef38e48372f940ec91396b7ac7bcbeed0124ac8e2485307f408c`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

### Project mC Decision Register — Version 1.2

**Document Control Header**
*   **Version:** 1.2
*   **Current project stage:** Phase 3C retained-portfolio closure; final down-selection pending
*   **Phase 3C completed concepts:** OpenBraille, VibeGuard and TrueMoist
*   **Phase 3C pending concepts:** None within the retained shortlist
*   **Phase 3C deferred concepts:** TrustLatch and ColdTrace — deferred before Phase 3C architecture completion; not technically rejected
*   **Authoritative as of:** Phase 3C closure of the retained three-concept shortlist and current uploaded source set
*   **Version 1.2 change:** TrustLatch and ColdTrace formally deferred; Phase 3C closed for the retained shortlist; patent potential confirmed as the primary final-selection priority; re-entry conditions recorded in PDR-064 to PDR-067.

***

#### Part I: Methodology & Project Management

**Decision ID:** PDR-001
**Title:** Project Budget Ceiling
**Phase introduced:** Phase 1A
**Category:** Methodology & Project Management
**Decision or requirement:** Cap prototype budget at a maximum of ₹5,000 INR, with a preferred target of ≤ ₹3,000 INR.
**Rationale:** Ensures the project remains a low-cost, frugal innovation suitable for a student team and scalable in resource-constrained environments.
**Source evidence:** `MC_Project_PHASE_DOC.md`
**Alternatives:** Unconstrained budget.
**Decision type:** Requirement
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-002

**Decision ID:** PDR-002
**Title:** Project Timeline & Team Scope
**Phase introduced:** Phase 1A
**Category:** Methodology & Project Management
**Decision or requirement:** Restrict the prototype timeline to approximately 2 months, executable by a 5-member team (three technically strong CS/Cybersecurity students).
**Rationale:** Fits within standard academic semester constraints and dictates that mechanical complexity must be minimized or shifted to software.
**Source evidence:** `PROJECT_CONCEPT_CONTEXT.md`
**Alternatives:** Professional mechanical outsourcing.
**Decision type:** Requirement
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-038

**Decision ID:** PDR-003
**Title:** Deferral of Hardware Implementation Decisions
**Phase introduced:** Project Foundation
**Category:** Methodology & Project Management
**Decision or requirement:** Phase 3C selects and freezes the prototype architecture, including provisional MCU, sensor, actuator, interface and power choices. Phase 6 converts those architecture selections into procurement-ready component variants, schematics, PCB design, firmware implementation and manufacturing specifications.
**Rationale:** Prevents premature solution generation and ensures decisions remain problem-focused rather than technology-driven.
**Source evidence:** `MC_Project_PHASE_DOC.md`
**Alternatives:** Early component selection.
**Decision type:** Requirement
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-040, PDR-043

**Decision ID:** PDR-004
**Title:** Evidence Exclusion over Averaging Protocol
**Phase introduced:** Phase 2 / Phase 3A
**Category:** Methodology & Project Management
**Decision or requirement:** Entire sections of AI deep research reports that suffer from "concept-swap" or interpretation drift must be excluded completely, rather than down-weighted or averaged into the synthesis.
**Rationale:** Averaging hallucinated or mis-scoped data corrupts the engineering baseline.
**Source evidence:** `Phase3A_MEMORY.md`, `Claudes report on the research Phases 3a.pdf`
**Alternatives:** Blending or averaging hallucinated findings.
**Decision type:** Final decision
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-006, PDR-041

**Decision ID:** PDR-005
**Title:** Split-Maturity Assessment Method
**Phase introduced:** Phase 3A
**Category:** Methodology & Project Management
**Decision or requirement:** Evaluate engineering readiness on a two-tier scale: Base Domain Maturity vs. Specific Innovation Maturity.
**Rationale:** Resolves contradictions where an AI model rates a concept mature at the industry level while another rates the specific innovation edge algorithm as emerging.
**Source evidence:** `Claudes report on the research Phases 3a.pdf`
**Alternatives:** Single-figure maturity calls.
**Decision type:** Final decision
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** None

**Decision ID:** PDR-006
**Title:** Mandatory Concept Grounding/Confirmation Step
**Phase introduced:** Phase 3A / Phase 3B
**Category:** Methodology & Project Management
**Decision or requirement:** Require Deep Research passes to restate and confirm their understanding against the Engineering Design Review document before analyzing.
**Rationale:** Proved to be a leading indicator of report reliability; reports skipping this step consistently produced concept-swap hallucinations.
**Source evidence:** `Phase3B_MEMORY.md`
**Alternatives:** Relying on short-form project names.
**Decision type:** Requirement
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-042

**Decision ID:** PDR-039
**Title:** Multi-AI Independent Research Strategy
**Phase introduced:** Phase 1A
**Category:** Methodology & Project Management
**Decision or requirement:** Utilize multiple independent Deep Research systems simultaneously rather than a single model.
**Rationale:** Redundancy increases confidence in recurring opportunities and mitigates single-model hallucination.
**Source evidence:** `Phase1A_Memory.md`
**Alternatives:** Single AI pipeline.
**Decision type:** Requirement
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-041

**Decision ID:** PDR-040
**Title:** Prohibition of Premature Solution Generation
**Phase introduced:** Phase 1A / Phase 1B
**Category:** Methodology & Project Management
**Decision or requirement:** Strictly prohibit the invention of products, architectures, or solutions during early phases.
**Rationale:** Ensures the project remains focused on validating real-world problems before engineering solutions.
**Source evidence:** `MC_Project_PHASE_DOC.md`
**Alternatives:** Brainstorming hardware solutions early.
**Decision type:** Requirement
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** No (Phase specific)
**Related PDR entries:** PDR-003

**Decision ID:** PDR-041
**Title:** Duplicate Preservation for Confidence Scoring
**Phase introduced:** Phase 1B
**Category:** Methodology & Project Management
**Decision or requirement:** Preserve duplicate findings from different AIs prior to consolidation to measure cross-report confidence.
**Rationale:** Independent convergence by multiple systems on the same problem acts as decision-grade evidence.
**Source evidence:** `Phase1B_Memory.md`
**Alternatives:** Immediate deletion of duplicates.
**Decision type:** Requirement
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-039

**Decision ID:** PDR-042
**Title:** Authoritative Precedence of the EDR Document
**Phase introduced:** Phase 3B
**Category:** Methodology & Project Management
**Decision or requirement:** The Engineering Design Review (EDR) overrides the Phase 1C Report and short-form contexts wherever they differ.
**Rationale:** Short-form descriptions caused interpretation drift in Phase 2 and 3A; the EDR provides unambiguous constraints.
**Source evidence:** `Phase3B_Report_by_Claude.md`
**Alternatives:** Continuing to use PROJECT_CONCEPT_CONTEXT.md as the primary anchor.
**Decision type:** Requirement
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-006

**Decision ID:** PDR-043
**Title:** Phase 3C Architecture Selection Mandate
**Phase introduced:** Phase 3C
**Category:** Methodology & Project Management
**Decision or requirement:** Phase 3C must resolve technical disagreements and select *one* final architecture, rather than preserving forks.
**Rationale:** Phase 3C's output must serve as an actual, unambiguous build blueprint for Phase 4 prototyping.
**Source evidence:** `Phase3C_OpenBraille_Architecture_Report_Final.md`
**Alternatives:** Preserving strategic forks into Phase 4.
**Decision type:** Requirement
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-003

***

#### Part II: Portfolio, Commercialization & Patent Strategy

**Decision ID:** PDR-007
**Title:** Portfolio Gate Evaluation Filtering
**Phase introduced:** Phase 1B.5
**Category:** Portfolio & Commercialization & Patent Strategy
**Decision or requirement:** Apply 8 strict engineering decision gates to filter the opportunity portfolio.
**Rationale:** Ensures only technically feasible, budget-compliant projects advance.
**Source evidence:** `Phase1B5_Memory.md`
**Alternatives:** Advancing all clusters.
**Decision type:** Final decision
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** No (Phase specific)
**Related PDR entries:** PDR-008

**Decision ID:** PDR-008
**Title:** Selection of Top 5 Concepts
**Phase introduced:** Phase 1C
**Category:** Portfolio & Commercialization & Patent Strategy
**Decision or requirement:** Advance OpenBraille, VibeGuard, TrueMoist, TrustLatch, and ColdTrace to Phase 2/3.
**Rationale:** These 5 concepts represented the strongest balance of originality, patent potential, feasibility, and embedded necessity.
**Source evidence:** `Phase1C_Memory.md`
**Alternatives:** Advancing other clusters like SiliconFingerprint.
**Decision type:** Final decision
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-007

**Decision ID:** PDR-009
**Title:** OpenBraille IP Pivot
**Phase introduced:** Phase 2
**Category:** Portfolio & Commercialization & Patent Strategy
**Decision or requirement:** Redirect the patent target away from the physical actuation mechanism and toward manufacturing methods and firmware control.
**Rationale:** The actuator space is fenced by Dot Inc. and expired art (SMA/EAP); manufacturing methods and firmware remain viable white space.
**Source evidence:** `Phase2_Report by CLaude.md`, `QWen Research on Patent.pdf`
**Alternatives:** Patenting the physical mechanism.
**Decision type:** Recommendation
**Verification status:** Partially Verified
**Current status:** Recommendation
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-015

**Decision ID:** PDR-010
**Title:** ColdTrace Freedom-to-Operate Condition
**Phase introduced:** Phase 2
**Category:** Portfolio & Commercialization & Patent Strategy
**Decision or requirement:** Mandate an FTO check on US 10,887,735 (Sensitech) before committing to a physical thermal-mass architecture.
**Rationale:** Avoid infringement on active physical buffered-sensor chamber patents simulating vaccine thermal physics.
**Source evidence:** `Phase2_Report by CLaude.md`, `Kimi Patent Research.pdf`
**Alternatives:** Proceeding blindly into physical buffers.
**Decision type:** Requirement
**Verification status:** Dormant pending concept reactivation
**Current status:** Deferred with ColdTrace; condition remains binding only if ColdTrace is reactivated
**Carry-forward requirement:** Conditional
**Related PDR entries:** PDR-034

**Decision ID:** PDR-011
**Title:** TrustLatch IP Abandonment (Strategic Fork)
**Phase introduced:** Phase 2
**Category:** Portfolio & Commercialization & Patent Strategy
**Decision or requirement:** TrustLatch is deferred from the active portfolio before Phase 3C architecture completion. Its open-core / academic-without-patent strategic option is preserved for possible future re-entry.
**Rationale:** The space is fundamentally saturated by silicon giants and open-source standards; this represents a genuine strategic fork requiring project owner resolution.
**Source evidence:** `Phase2_Report by CLaude.md`, `QWen Research on Patent.pdf`
**Alternatives:** Forcing a patent filing.
**Decision type:** Open question
**Verification status:** Deferred before Phase 3C
**Current status:** Deferred with TrustLatch
**Carry-forward requirement:** Conditional
**Related PDR entries:** PDR-047

**Decision ID:** PDR-045
**Title:** TrueMoist Custom Hardware IP Boundary
**Phase introduced:** Phase 2; MVP scope finalized in Phase 3C
**Category:** Portfolio & Commercialization & Patent Strategy
**Decision or requirement:** Retain off-the-shelf commodity sensing hardware for the MVP. Do not develop or claim IP over a custom moisture/temperature/EC probe in Phase 4. Focus innovation work on validated compensation workflow, drift/confidence logic, constrained deployment, and calibration methodology.
**Rationale:** Protects the schedule and avoids overclaiming a crowded custom-probe hardware area.
**Source evidence:** `Phase2_Report by CLaude.md`, `Phase3C_TrueMoist_Architecture_Report_Final.md`
**Alternatives:** Designing and patenting a custom integrated probe during the semester MVP.
**Decision type:** Final MVP scope decision; broader patent strategy remains a recommendation
**Verification status:** Accepted for MVP scope
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-031, PDR-058.
**Decision ID:** PDR-046
**Title:** VibeGuard SME Commercial Wedge
**Phase introduced:** Phase 2
**Category:** Portfolio & Commercialization & Patent Strategy
**Decision or requirement:** Position VibeGuard commercially around zero-subscription economics and single-node processing for SMEs.
**Rationale:** The enterprise PdM space is saturated by funded platforms; the defensible moat is deployment economics for SMEs.
**Source evidence:** `Phase2_Report by CLaude.md`, `QWen Research on Patent.pdf`
**Alternatives:** Enterprise cloud-platform subscription models.
**Decision type:** Recommendation
**Verification status:** Partially Verified
**Current status:** Recommendation
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-027

**Decision ID:** PDR-047
**Title:** TrustLatch Compliance-Driven Commercial Strategy
**Phase introduced:** Phase 2 / Phase 3A
**Category:** Portfolio & Commercialization & Patent Strategy
**Decision or requirement:** Execute an open-core commercial strategy that gives away reference ports while monetizing EU Cyber Resilience Act (CRA) / UK PSTI compliance automation and fleet key management.
**Rationale:** The market forcing function is regulatory compliance for constrained OEMs, not novel cryptography.
**Source evidence:** `Kimi Patent Research.pdf`
**Alternatives:** Proprietary enterprise licensing.
**Decision type:** Recommendation
**Verification status:** Partially Verified
**Current status:** Recommendation
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-011

**Decision ID:** PDR-057
**Title:** Trademark vs. Utility Patent Separation
**Phase introduced:** Phase 2
**Category:** Portfolio & Commercialization & Patent Strategy
**Decision or requirement:** Separate trademark observations/collisions from utility patentability conclusions during IP landscaping.
**Rationale:** Name collisions (e.g., Nexleaf ColdTrace product instead of the concept) cause interpretation drift and must be handled distinctly from technical prior art.
**Source evidence:** `MC_Project_PHASE_DOC.md`
**Alternatives:** Blended IP assessments.
**Decision type:** Requirement
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-004

***

#### Part III: Validation, Testing & Feasibility

**Decision ID:** PDR-012
**Title:** TrueMoist Validation Gate
**Phase introduced:** Phase 2 / Phase 3A
**Category:** Validation, Testing & Feasibility
**Decision or requirement:** Hold TrueMoist for a two-season, multi-soil validation sprint.
**Rationale:** Calibration-free operation across varying soil types using self-calibration algorithms is unproven in open literature.
**Source evidence:** `Phase2_Report by CLaude.md`
**Alternatives:** Advancing to production design immediately.
**Decision type:** Future validation task
**Verification status:** Partially Verified
**Current status:** Future validation task
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-048, PDR-049

**Decision ID:** PDR-013
**Title:** VibeGuard Validation Gate
**Phase introduced:** Phase 2 / Phase 3B
**Category:** Validation, Testing & Feasibility
**Decision or requirement:** Mandate a real dense-machine field test to validate single-node spatial attribution before scaling.
**Rationale:** Theoretical blind source separation algorithms often fail in acoustically coupled environments.
**Source evidence:** `Phase2_Report by CLaude.md`
**Alternatives:** Assuming lab data transfers perfectly to factories.
**Decision type:** Future validation task
**Verification status:** Partially Verified
**Current status:** Future validation task
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-027

**Decision ID:** PDR-014
**Title:** Cross-Portfolio Shared MCU Platform
**Phase introduced:** Phase 3B
**Category:** Validation, Testing & Feasibility
**Decision or requirement:** Standardize on the ESP32 (or STM32 with FPU) as the primary microcontroller across all five concepts.
**Rationale:** Provides abundant GPIO, hardware floating-point capabilities, and aligns with the team's skillset as a shared platform investment.
**Source evidence:** `Phase3B_Report_by_Claude.md`
**Alternatives:** RP2040, Arduino Uno.
**Decision type:** Provisional architecture selection
**Verification status:** Partially Verified
**Current status:** Provisional architecture selection
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-017, PDR-025

**Decision ID:** PDR-048
**Title:** TrueMoist Gravimetric Validation Standard
**Phase introduced:** Phase 3A / Phase 3B; refined in Phase 3C
**Category:** Validation, Testing & Feasibility
**Decision or requirement:** Use dry-basis gravimetric water content as the authoritative reference. Dry at 105 ± 5 °C for at least 24 hours and until constant mass. Use a 0.01 g scale where available. Do not report volumetric water content unless bulk density or a controlled known-volume measurement is separately established.
**Rationale:** Removes ambiguity between gravimetric and volumetric water content and strengthens traceability.
**Source evidence:** `Phase3B_Report_by_Claude.md`, `Claudes report on the research Phases 3a.pdf`, `Phase3C_TrueMoist_Architecture_Report_Final.md`
**Alternatives:** Validation against another low-cost electronic sensor; unqualified VWC reporting.
**Decision type:** Requirement
**Verification status:** Pending confirmation of institutional oven and scale access
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-012, PDR-031, PDR-049, PDR-059, PDR-060, PDR-061.
**Decision ID:** PDR-056
**Title:** ColdTrace Validation Test
**Phase introduced:** Phase 3B / Phase 3C
**Category:** Validation, Testing & Feasibility
**Decision or requirement:** The validation test must directly compare a controlled short-duration disturbance (e.g., door-opening spike) against a controlled sustained thermal excursion.
**Rationale:** This is the only physical method to prove the firmware effectively dampens false alarms while catching real failures.
**Source evidence:** `Phase3B_Report_by_Claude.md`
**Alternatives:** Standard ambient thermal logging.
**Decision type:** Requirement
**Verification status:** Deferred before Phase 3C architecture completion
**Current status:** Dormant — ColdTrace not in the retained shortlist
**Carry-forward requirement:** Conditional on ColdTrace reactivation
**Related PDR entries:** PDR-034

***

#### Part IV: Concept-Specific Architecture

##### OpenBraille
**Decision ID:** PDR-015
**Title:** OpenBraille Actuation Principle
**Phase introduced:** Phase 3C
**Category:** Concept-Specific Architecture (OpenBraille)
**Decision or requirement:** Servo + Cam linkage.
**Rationale:** Retires fabrication-tolerance risk, requires no custom driver electronics (servos self-drive), no continuous-hold thermal fault mode.
**Source evidence:** `Phase3C_OpenBraille_Architecture_Report_Final.md`, `Phase3C_OpenBraille_Memory_Final.md`
**Alternatives:** Electromagnetic latching micro-coils, non-latching solenoid, Shape Memory Alloy.
**Decision type:** Final decision
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-018, PDR-019

**Decision ID:** PDR-016
**Title:** OpenBraille Dot-Pitch Compliance
**Phase introduced:** Phase 3C
**Category:** Concept-Specific Architecture (OpenBraille)
**Decision or requirement:** Adopt a permanent macro-scale (~300% of ISO 17049, ≈7 mm pitch, ≈1.5 mm dot height) for the prototype, explicitly abandoning dimensional compliance.
**Rationale:** Standard FDM 3D printers cannot achieve the precision required; macro-scaling neutralizes manufacturing risk while proving hypothesis.
**Source evidence:** `Phase3C_OpenBraille_Architecture_Report_Final.md`, `Phase3C_OpenBraille_Memory_Final.md`
**Alternatives:** 100% scale outsourced SLA printing.
**Decision type:** Final decision
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-015

**Decision ID:** PDR-017
**Title:** OpenBraille MCU Selection
**Phase introduced:** Phase 3C
**Category:** Concept-Specific Architecture (OpenBraille)
**Decision or requirement:** ESP32-WROOM-32 DevKit.
**Rationale:** Offers 30+ GPIO pins (ample for PWM), hardware timers for jitter-free PWM, low cost, and team familiarity.
**Source evidence:** `Phase3C_OpenBraille_Architecture_Report_Final.md`, `Phase3C_OpenBraille_Memory_Final.md`
**Alternatives:** STM32F103 "Blue Pill", Arduino Uno.
**Decision type:** Final decision
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-014

**Decision ID:** PDR-018
**Title:** OpenBraille Driver Architecture
**Phase introduced:** Phase 3C
**Category:** Concept-Specific Architecture (OpenBraille)
**Decision or requirement:** Centralized ESP32 control with direct GPIO PWM to each servo; no intermediate driver ICs.
**Rationale:** SG90 servos integrate their own driver circuitry, eliminating a subsystem and its failure modes entirely.
**Source evidence:** `Phase3C_OpenBraille_Architecture_Report_Final.md`, `Phase3C_OpenBraille_Memory_Final.md`
**Alternatives:** Shift-register SPI multiplexing, H-Bridge arrays.
**Decision type:** Final decision
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-015

**Decision ID:** PDR-019
**Title:** OpenBraille Manufacturing Pathway
**Phase introduced:** Phase 3C
**Category:** Concept-Specific Architecture (OpenBraille)
**Decision or requirement:** In-house FDM 3D printing (ABS frame, PETG/Nylon cams) plus off-the-shelf components; no outsourced fabrication.
**Rationale:** Keeps fabrication within team tools and timeline, avoiding commercial SLA outsourcing dependencies.
**Source evidence:** `Phase3C_OpenBraille_Architecture_Report_Final.md`, `Phase3C_OpenBraille_Memory_Final.md`
**Alternatives:** Commercial SLA printing, Laser cutting.
**Decision type:** Final decision
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-016

**Decision ID:** PDR-020
**Title:** OpenBraille Power Architecture
**Phase introduced:** Phase 3C
**Category:** Concept-Specific Architecture (OpenBraille)
**Decision or requirement:** External 5V/2A DC adapter with a 1000 µF decoupling capacitor across the servo rail.
**Rationale:** Servos draw high peak current. USB bus power (500mA limit) risks brown-out resets; decoupling eliminates transient voltage sags.
**Source evidence:** `Phase3C_OpenBraille_Architecture_Report_Final.md`, `Phase3C_OpenBraille_Memory_Final.md`
**Alternatives:** USB bus power, 6V AA Battery pack.
**Decision type:** Final decision
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-015

**Decision ID:** PDR-021
**Title:** OpenBraille Reset Mechanism
**Phase introduced:** Phase 3C
**Category:** Concept-Specific Architecture (OpenBraille)
**Decision or requirement:** Utilize the SG90 servo's integrated torsion spring for pin reset.
**Rationale:** Removes an external component (compression springs) and a failure mode present in solenoid alternatives.
**Source evidence:** `Phase3C_OpenBraille_Architecture_Report_Final.md`
**Alternatives:** External compression/leaf springs.
**Decision type:** Requirement
**Verification status:** Source verified, technically unvalidated
**Current status:** Pending physical inspection and prototype testing
**Required correction:** Confirm whether the selected servo provides a usable passive return mechanism. Otherwise, document active servo-driven cam retraction as the reset method.
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-015

**Decision ID:** PDR-022
**Title:** OpenBraille Validation Strategy
**Phase introduced:** Phase 3C
**Category:** Concept-Specific Architecture (OpenBraille)
**Decision or requirement:** Bottom-up, single-dot-first integration sequence (M1-M8), culminating in tactile validation.
**Rationale:** Isolates structural friction/mechanical variables from electrical variables before integrating all 6 pins.
**Source evidence:** `Phase3C_OpenBraille_Architecture_Report_Final.md`, `Phase3C_OpenBraille_Memory_Final.md`
**Alternatives:** Assembling all 6 dots at once.
**Decision type:** Final decision
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-016

##### VibeGuard
**Decision ID:** PDR-023
**Title:** VibeGuard Sensor Selection
**Phase introduced:** Phase 3C
**Category:** Concept-Specific Architecture (VibeGuard)
**Decision or requirement:** ADXL345 (3-axis digital MEMS accelerometer).
**Rationale:** Adequate bandwidth (1600 Hz Nyquist) for MVP low-frequency tests; lowest cost; best-documented implementation.
**Source evidence:** `Phase3C_VibeGuard_Architecture_Report_Final.md`, `Phase3C_VibeGuard_Memory_Final.md`
**Alternatives:** IIS3DWB, MPU6050, ADXL1002.
**Decision type:** Final decision
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-055

**Decision ID:** PDR-024
**Title:** VibeGuard Sensor Interface
**Phase introduced:** Phase 3C
**Category:** Concept-Specific Architecture (VibeGuard)
**Decision or requirement:** High-speed SPI Bus (stepped down to 1-2 MHz for breadboards).
**Rationale:** I2C's 400kHz fast-mode causes buffer overflow at the 3200Hz Output Data Rate needed for maximum bandwidth.
**Source evidence:** `Phase3C_VibeGuard_Architecture_Report_Final.md`
**Alternatives:** I2C protocol.
**Decision type:** Final decision
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-023

**Decision ID:** PDR-025
**Title:** VibeGuard MCU Selection
**Phase introduced:** Phase 3C
**Category:** Concept-Specific Architecture (VibeGuard)
**Decision or requirement:** ESP32 (WROOM-32 or S3-class).
**Rationale:** Provides Hardware Floating-Point Unit (FPU) necessary for real-time FFT, 520KB SRAM for windowed buffers, and DMA-capable peripheral bus.
**Source evidence:** `Phase3C_VibeGuard_Architecture_Report_Final.md`
**Alternatives:** STM32 F4-class, Arduino Uno, RP2040.
**Decision type:** Final decision
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-014

**Decision ID:** PDR-026
**Title:** VibeGuard Edge Intelligence / Classification
**Phase introduced:** Phase 3C
**Category:** Concept-Specific Architecture (VibeGuard)
**Decision or requirement:** Tiered processing: Time-domain features crossing a threshold triggers a windowed FFT; primary classification relies on a calibrated RMS threshold, scaling to unsupervised Mahalanobis-distance anomaly detection.
**Rationale:** Meets MDS with deterministic thresholds immediately; avoids need for labeled failure datasets required by supervised Deep Learning.
**Source evidence:** `Phase3C_VibeGuard_Architecture_Report_Final.md`
**Alternatives:** Supervised Deep-learning TinyML (CNN/Autoencoders).
**Decision type:** Final decision
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-054

**Decision ID:** PDR-027
**Title:** VibeGuard Noise Isolation Strategy
**Phase introduced:** Phase 3C
**Category:** Concept-Specific Architecture (VibeGuard)
**Decision or requirement:** Baseline spectral subtraction combined with proximity mounting and band-limited features.
**Rationale:** ESP32 cannot compute complex BSS matrix inversions. The adequacy of spectral subtraction is empirically testable only once a physical rig exists.
**Source evidence:** `Phase3C_VibeGuard_Architecture_Report_Final.md`
**Alternatives:** FastICA / SSA / EEMD.
**Decision type:** Future validation task
**Verification status:** Partially Verified
**Current status:** Future validation task
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-013

**Decision ID:** PDR-028
**Title:** VibeGuard Mechanical Mounting
**Phase introduced:** Phase 3C
**Category:** Concept-Specific Architecture (VibeGuard)
**Decision or requirement:** Absolute rigid mounting (epoxy/cyanoacrylate to a bracket, bolted directly to motor casing).
**Rationale:** Loose mounting acts as an unintended mechanical low-pass filter, permanently destroying the high-frequency vibration signals.
**Source evidence:** `Phase3C_VibeGuard_Architecture_Report_Final.md`
**Alternatives:** Magnetic mounts, foam adhesive.
**Decision type:** Final decision
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-023

**Decision ID:** PDR-029
**Title:** VibeGuard Output Indication
**Phase introduced:** Phase 3C
**Category:** Concept-Specific Architecture (VibeGuard)
**Decision or requirement:** Common-cathode RGB LED (Green = Normal, Red = Abnormal, Blue = Calibrating).
**Rationale:** Directly satisfies the MDS requirement for "clear output" without imposing complex OLED display code on the MVP.
**Source evidence:** `Phase3C_VibeGuard_Architecture_Report_Final.md`, `Phase3C_VibeGuard_Memory_Final.md`
**Alternatives:** OLED/LCD screen.
**Decision type:** Final decision
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** None

**Decision ID:** PDR-030
**Title:** VibeGuard Test Scenario
**Phase introduced:** Phase 3C
**Category:** Concept-Specific Architecture (VibeGuard)
**Decision or requirement:** Small 12V DC motor or PC fan mounted on a heavy damped base, tested by artificially attaching an eccentric mass to induce unbalance.
**Rationale:** Creates a safe, low-voltage, repeatable abnormal condition demonstrating the MDS without needing access to real failing industrial machinery.
**Source evidence:** `Phase3C_VibeGuard_Architecture_Report_Final.md`, `Phase3C_VibeGuard_Memory_Final.md`
**Alternatives:** Loosened mounting bolts.
**Decision type:** Final decision
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-026

**Decision ID:** PDR-054
**Title:** VibeGuard Pipeline Sequence
**Phase introduced:** Phase 3C
**Category:** Concept-Specific Architecture (VibeGuard)
**Decision or requirement:** Standardize pipeline order: DC removal → Hann Windowing → Time-domain features (RMS/Peak) → Triggered FFT.
**Rationale:** Controls compute load on constrained MCU; Hann windowing prevents spectral leakage during finite-block FFTs.
**Source evidence:** `Phase3C_VibeGuard_Architecture_Report_Final.md`, `Phase3C_VibeGuard_Memory_Final.md`
**Alternatives:** Continuous FFT processing.
**Decision type:** Final decision
**Verification status:** Verified
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-026

**Decision ID:** PDR-055
**Title:** VibeGuard Sensor Upgrade Path
**Phase introduced:** Phase 3C
**Category:** Concept-Specific Architecture (VibeGuard)
**Decision or requirement:** Document the IIS3DWB (6000 Hz) as the designated upgrade path for bearing-fault detection, while retaining ADXL345 for the MVP.
**Rationale:** Prevents cost overrun on the MVP while documenting exactly how to restore the advanced capability for future iterations.
**Source evidence:** `Phase3C_VibeGuard_Architecture_Report_Final.md`, `Phase3C_VibeGuard_Memory_Final.md`
**Alternatives:** Mandating the IIS3DWB immediately.
**Decision type:** Recommendation
**Verification status:** Verified
**Current status:** Documented future upgrade path — not part of the MVP
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-023

##### TrueMoist
**Decision ID:** PDR-031
**Title:** TrueMoist Compensation Method
**Phase introduced:** Phase 3B; finalized in Phase 3C
**Category:** Concept-Specific Architecture (TrueMoist)
**Decision or requirement:** Use a univariate raw calibration as the uncompensated baseline, ordinary multivariate linear regression as the modelling baseline, and ridge-regularized second-order regression as the final MVP candidate. Inputs are raw probe response, measured soil temperature, and controlled salinity-treatment code. Train offline and deploy fixed coefficients for local MCU inference.
**Rationale:** Preserves interpretability and local processing while modelling low-order interactions without TinyML or online-training risk.
**Source evidence:** `Phase3B_Report_by_Claude.md`, `Phase3C_TrueMoist_Architecture_Report_Final.md`, `Phase3C_TrueMoist_Memory_Final.md`
**Alternatives:** Threshold-only mapping, AD5933 impedance architecture, TinyML, on-device adaptive training.
**Decision type:** Final architecture selection
**Verification status:** Requires prototype validation
**Current status:** Accepted for Phase 4
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-032, PDR-045, PDR-048, PDR-049, PDR-058, PDR-059, PDR-060, PDR-061, PDR-062.
**Decision ID:** PDR-032
**Title:** TrueMoist ADC Selection
**Phase introduced:** Phase 3B; resolved in Phase 3C
**Category:** Concept-Specific Architecture (TrueMoist)
**Decision or requirement:** Include ADS1115 in the primary prototype and compare it against calibrated ESP32 ADC1 during Week 1. Do not justify it from nominal bit count alone. Retain ADS1115 when it improves pilot noise/RMSE or when its low cost is judged worthwhile for reproducibility; permit calibrated ESP32 ADC1 as fallback.
**Rationale:** Resolves the Phase 3B instrumentation uncertainty while preserving an evidence-based fallback.
**Source evidence:** `Phase3B_Report_by_Claude.md`, `Phase3C_TrueMoist_Architecture_Report_Final.md`
**Alternatives:** ESP32 ADC1 as the untested final path; higher-cost ADC/impedance instrumentation.
**Decision type:** Final architecture selection with mandatory validation gate
**Verification status:** Partially verified; empirical Week-1 gate pending
**Current status:** Accepted for Phase 4
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-031, PDR-050, PDR-061.
**Decision ID:** PDR-049
**Title:** TrueMoist Single-Soil Limit
**Phase introduced:** Phase 3B; finalized in Phase 3C
**Category:** Concept-Specific Architecture (TrueMoist)
**Decision or requirement:** Restrict calibration and formal validation to one homogeneous soil source and one defined preparation method. No multi-soil or universal transfer claim is permitted in the MVP.
**Rationale:** Makes the physical dataset achievable and prevents soil-type confounding within the two-month schedule.
**Source evidence:** `Phase3B_Report_by_Claude.md`, `Phase3C_TrueMoist_Architecture_Report_Final.md`
**Alternatives:** Multi-soil generalization during the MVP.
**Decision type:** Final MVP scope decision
**Verification status:** Accepted
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-012, PDR-031, PDR-048, PDR-059.
**Decision ID:** PDR-050
**Title:** TrueMoist Analog Front-End Soldering
**Phase introduced:** Phase 3B; finalized in Phase 3C
**Category:** Concept-Specific Architecture (TrueMoist)
**Decision or requirement:** Breadboard use is permitted only for Week-1 characterization. Freeze the final analog path on soldered perfboard by the end of Week 2, with short analog wiring, local decoupling, deliberate grounding, and fixed connectors.
**Rationale:** Reduces avoidable electrical variation before the main dataset is collected.
**Source evidence:** `Phase3B_Report_by_Claude.md`, `Phase3C_TrueMoist_Architecture_Report_Final.md`
**Alternatives:** Keeping the final analog acquisition path on a solderless breadboard.
**Decision type:** Implementation requirement
**Verification status:** Pending build
**Current status:** Accepted for Phase 4
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-032, PDR-061.

**Decision ID:** PDR-058
**Title:** TrueMoist Final MVP Architecture
**Phase introduced:** Phase 3C
**Category:** Concept-Specific Architecture (TrueMoist)
**Decision or requirement:** Freeze a D-dominant architecture with B-style signal hardening: genuine analog capacitive probe, waterproof DS18B20, controlled salinity treatments, ESP32-WROOM-32, ADS1115, offline-trained fixed regression coefficients, local inference, USB CSV logging, and gravimetric validation.
**Rationale:** This is the simplest architecture that covers the complete engineering hypothesis within budget and schedule.
**Source evidence:** `Phase3C_TrueMoist_Architecture_Report_Final.md`, `Phase3C_TrueMoist_Memory_Final.md`
**Alternatives:** Minimal internal-ADC demonstrator; live-EC architecture; adaptive embedded calibration.
**Decision type:** Final architecture selection
**Verification status:** Requires mandatory early validation
**Current status:** Accepted for Phase 4
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-031, PDR-032, PDR-045, PDR-048, PDR-049, PDR-050, PDR-061, PDR-062, PDR-063.

**Decision ID:** PDR-059
**Title:** TrueMoist Physical Dataset Design
**Phase introduced:** Phase 3C
**Category:** Validation, Testing & Feasibility
**Decision or requirement:** Target 72 independent physical runs: 4 moisture levels × 3 temperature levels × 2 salinity treatments × 3 independent replicates. Rapid ADC readings are averaged and never counted as independent physical samples.
**Rationale:** Provides factorial coverage while remaining feasible within approximately two months.
**Source evidence:** `Phase3C_TrueMoist_Architecture_Report_Final.md`, `Phase3C_TrueMoist_Memory_Final.md`
**Alternatives:** 135-run or 180-run designs; ungrouped random splits; counting repeated ADC samples as independent observations.
**Decision type:** Final validation-plan decision
**Verification status:** Pilot timing pending
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-048, PDR-049, PDR-060, PDR-061.

**Decision ID:** PDR-060
**Title:** TrueMoist Validation Success Threshold
**Phase introduced:** Phase 3C
**Category:** Validation, Testing & Feasibility
**Decision or requirement:** On untouched physical test replicates, compensated RMSE must be at least 20% lower and compensated MAE at least 15% lower than the uncompensated baseline. Absolute errors and disturbance-subset results must also be reported.
**Rationale:** Directly tests relative improvement against the same physical reference rather than relying on training fit or attractive plots.
**Source evidence:** `Phase3C_TrueMoist_Architecture_Report_Final.md`
**Alternatives:** R²-only success; arbitrary absolute accuracy claim.
**Decision type:** Requirement
**Verification status:** Pending final validation
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-031, PDR-048, PDR-059.

**Decision ID:** PDR-061
**Title:** TrueMoist Week-1/Week-2 Validation Gates
**Phase introduced:** Phase 3C
**Category:** Validation, Testing & Feasibility
**Decision or requirement:** Before the main dataset, verify probe repeatability, insertion and packing sensitivity, ADC-path value, gravimetric access, salinity-treatment effect, and pilot model feasibility. Apply the documented fallback whenever a gate fails.
**Rationale:** Component existence alone does not prove that the complete measurement and validation chain is viable.
**Source evidence:** `Phase3C_TrueMoist_Architecture_Report_Final.md`, `Phase3C_TrueMoist_Memory_Final.md`
**Alternatives:** Proceeding directly to full dataset collection.
**Decision type:** Mandatory validation gate
**Verification status:** Pending
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-032, PDR-048, PDR-050, PDR-058, PDR-062, PDR-063.

**Decision ID:** PDR-062
**Title:** TrueMoist Controlled-Salinity Strategy
**Phase introduced:** Phase 3C
**Category:** Concept-Specific Architecture (TrueMoist)
**Decision or requirement:** Treat salinity as a controlled experimental treatment expressed by known salt addition per dry soil mass. Do not include mandatory live soil-EC sensing and do not claim that the treatment code is a bulk-soil, pore-water, apparent-EC, or solution-conductivity measurement.
**Rationale:** Preserves salinity-disturbance validation without creating an underdesigned electrochemical EC instrument.
**Source evidence:** `Phase3C_TrueMoist_Architecture_Report_Final.md`, `Phase3C_TrueMoist_Memory_Final.md`
**Alternatives:** Direct two-electrode runtime EC; solution-EC proxy as the sole field input.
**Decision type:** Final architecture selection
**Verification status:** Salinity pilot pending
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-031, PDR-058, PDR-061.

**Decision ID:** PDR-063
**Title:** TrueMoist Phase 4 Readiness
**Phase introduced:** Phase 3C
**Category:** Methodology & Project Management
**Decision or requirement:** Classify TrueMoist as “Architecture Ready with Mandatory Early Validation.” No Phase 3C research rerun is required; Phase 4 begins with the PDR-061 gates.
**Rationale:** One coherent architecture exists, but important physical assumptions remain empirical.
**Source evidence:** `Phase3C_TrueMoist_Architecture_Report_Final.md`, `Phase3C_TrueMoist_Memory_Final.md`
**Alternatives:** Architecture Ready without gates; Conditionally Ready; Phase 3C rerun.
**Decision type:** Phase-gate decision
**Verification status:** Accepted
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-058, PDR-061.

##### TrustLatch
**Decision ID:** PDR-033
**Title:** TrustLatch Firmware Scope
**Phase introduced:** Phase 3B
**Category:** Concept-Specific Architecture (TrustLatch)
**Decision or requirement:** Scope the MVP to boot-time firmware integrity verification only, single-slot.
**Rationale:** Fitting a bootloader, full crypto suite, and dual-bank OTA exhausts the 64-128KB flash memory of Cortex-M0/M3 MCUs.
**Source evidence:** `Phase3B_Report_by_Claude.md`
**Alternatives:** Dual-bank OTA updates with Mbed TLS.
**Decision type:** Provisional architecture selection
**Verification status:** Deferred before Phase 3C architecture completion
**Current status:** Dormant — TrustLatch not in the retained shortlist
**Carry-forward requirement:** Conditional on TrustLatch reactivation
**Related PDR entries:** PDR-011

**Decision ID:** PDR-051
**Title:** TrustLatch Crypto Library
**Phase introduced:** Phase 3B
**Category:** Concept-Specific Architecture (TrustLatch)
**Decision or requirement:** Mandate lightweight cryptographic libraries (TinyCrypt or micro-ecc) over full Mbed TLS.
**Rationale:** Full Mbed TLS exhausts MCU flash memory; using it on a constrained MCU will overwrite application space.
**Source evidence:** `Phase3B_Report_by_Claude.md`
**Alternatives:** Full Mbed TLS suite.
**Decision type:** Provisional architecture selection
**Verification status:** Deferred before Phase 3C architecture completion
**Current status:** Dormant — TrustLatch not in the retained shortlist
**Carry-forward requirement:** Conditional on TrustLatch reactivation
**Related PDR entries:** PDR-033

**Decision ID:** PDR-052
**Title:** TrustLatch ST-Link Mandate
**Phase introduced:** Phase 3B
**Category:** Concept-Specific Architecture (TrustLatch)
**Decision or requirement:** Use the ST-Link programmer rather than J-Link for development.
**Rationale:** The J-Link hardware pushes the prototype cost to ₹4800–6700, breaching the strict project budget ceiling.
**Source evidence:** `Phase3B_Report_by_Claude.md`
**Alternatives:** Segger J-Link.
**Decision type:** Recommendation
**Verification status:** Deferred before Phase 3C architecture completion
**Current status:** Dormant — TrustLatch not in the retained shortlist
**Carry-forward requirement:** Conditional on TrustLatch reactivation
**Related PDR entries:** PDR-001

**Decision ID:** PDR-053
**Title:** TrustLatch Compiled-In Keys
**Phase introduced:** Phase 3B
**Category:** Concept-Specific Architecture (TrustLatch)
**Decision or requirement:** Accept compiled-in keys as a documented, deliberate limitation for the prototype.
**Rationale:** Genuine production-grade secure key provisioning at manufacturing scale is a logistics problem that exceeds the timeline constraint.
**Source evidence:** `Phase3B_Report_by_Claude.md`
**Alternatives:** External secure elements (ATECC608).
**Decision type:** Provisional architecture selection
**Verification status:** Deferred before Phase 3C architecture completion
**Current status:** Dormant — TrustLatch not in the retained shortlist
**Carry-forward requirement:** Conditional on TrustLatch reactivation
**Related PDR entries:** PDR-033

##### ColdTrace
**Decision ID:** PDR-034
**Title:** ColdTrace Modeling Scope
**Phase introduced:** Phase 3B
**Category:** Concept-Specific Architecture (ColdTrace)
**Decision or requirement:** Utilize a Virtual Thermal Mass model (Lumped-capacitance equations in firmware) combined with accelerometer shock fusion.
**Rationale:** Bypasses the US 10,887,735 FTO risk associated with physical buffered probes while still filtering out benign door-opening spikes.
**Source evidence:** `Phase3B_Report_by_Claude.md`
**Alternatives:** Physical buffer chamber/glycol bottles.
**Decision type:** Provisional architecture selection
**Verification status:** Deferred before Phase 3C architecture completion
**Current status:** Dormant — ColdTrace not in the retained shortlist
**Carry-forward requirement:** Conditional on ColdTrace reactivation
**Related PDR entries:** PDR-010

**Decision ID:** PDR-035
**Title:** ColdTrace PCM Exclusion
**Phase introduced:** Phase 3B
**Category:** Concept-Specific Architecture (ColdTrace)
**Decision or requirement:** Explicitly exclude Phase-Change Material (PCM) melting plateau modeling from the MVP.
**Rationale:** Modeling non-linear latent heat without an internal physical sensor is mathematically difficult and overwhelms the timeline.
**Source evidence:** `Phase3B_Report_by_Claude.md`
**Alternatives:** Incorporating PCM modeling.
**Decision type:** Provisional architecture selection
**Verification status:** Deferred before Phase 3C architecture completion
**Current status:** Dormant — ColdTrace not in the retained shortlist
**Carry-forward requirement:** Conditional on ColdTrace reactivation
**Related PDR entries:** PDR-034

**Decision ID:** PDR-036
**Title:** ColdTrace Testing Limit
**Phase introduced:** Phase 3B
**Category:** Concept-Specific Architecture (ColdTrace)
**Decision or requirement:** Restrict prototype testing to standard refrigerator temperatures.
**Rationale:** Prevents catastrophic battery collapse and MCU brownouts that occur with Li-Ion/LiPo cells at deep-freeze or cryogenic extremes.
**Source evidence:** `Phase3B_Report_by_Claude.md`
**Alternatives:** Testing at freezer/cryogenic temps.
**Decision type:** Requirement
**Verification status:** Deferred before Phase 3C architecture completion
**Current status:** Dormant — ColdTrace not in the retained shortlist
**Carry-forward requirement:** Conditional on ColdTrace reactivation
**Related PDR entries:** PDR-056

**Decision ID:** PDR-037
**Title:** ColdTrace RTC Module
**Phase introduced:** Phase 3B
**Category:** Concept-Specific Architecture (ColdTrace)
**Decision or requirement:** Treat whether to include a Real-Time Clock (DS3231) as an open question for the MVP.
**Rationale:** The EDR MDS only requires distinguishing transient vs. sustained events, not producing a cryptographically secure, tamper-evident audit trail.
**Source evidence:** `Phase3B_Report_by_Claude.md`
**Alternatives:** Mandating RTC for deep sleep/timestamps.
**Decision type:** Open question
**Verification status:** Deferred before Phase 3C architecture completion
**Current status:** Dormant — ColdTrace not in the retained shortlist
**Carry-forward requirement:** Conditional on ColdTrace reactivation
**Related PDR entries:** PDR-034

***

**Decision ID:** PDR-064
**Title:** Phase 3C Portfolio Narrowing to Three Concepts
**Phase introduced:** Phase 3C retained-portfolio closure
**Category:** Portfolio & Commercialization & Patent Strategy
**Decision or requirement:** Retain OpenBraille, VibeGuard and TrueMoist as the only concepts entering final comparative down-selection. Defer TrustLatch and ColdTrace before completing their Phase 3C architecture work.
**Rationale:** The retained concepts already provide sufficient diversity for a defensible final choice. Continuing full Phase 3C on the remaining concepts would impose substantial research and context-management cost with diminishing decision value. Explicit cybersecurity alignment is not mandatory, and patent potential is the higher-priority selection objective.
**Source evidence:** Project-owner direction following completion of OpenBraille, VibeGuard and TrueMoist Phase 3C.
**Alternatives:** Complete full Phase 3C for all five concepts; retain TrustLatch through a reduced Phase 3C; retain ColdTrace.
**Decision type:** Final portfolio-scope decision
**Verification status:** Accepted
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-008, PDR-011, PDR-010, PDR-065, PDR-067

**Decision ID:** PDR-065
**Title:** Final Selection Priority — Patent Potential
**Phase introduced:** Phase 3C retained-portfolio closure
**Category:** Portfolio & Commercialization & Patent Strategy
**Decision or requirement:** In the final comparison of OpenBraille, VibeGuard and TrueMoist, prioritize credible patent-development potential over explicit cybersecurity alignment. Feasibility, two-month execution risk, budget compliance, demonstrability and team fit remain mandatory secondary criteria.
**Rationale:** Cybersecurity alignment is not a mandatory stakeholder constraint. The project’s strategic objective is patent-oriented embedded innovation, but no concept may advance solely on speculative patent claims if it is not realistically buildable.
**Source evidence:** Project-owner clarification after completion of three Phase 3C architectures.
**Alternatives:** Cybersecurity-first selection; feasibility-only selection; social-impact-only selection.
**Decision type:** Final portfolio evaluation rule
**Verification status:** Accepted
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-009, PDR-045, PDR-046, PDR-064

**Decision ID:** PDR-066
**Title:** Deferred-Concept Re-entry Conditions
**Phase introduced:** Phase 3C retained-portfolio closure
**Category:** Methodology & Project Management
**Decision or requirement:** TrustLatch or ColdTrace may re-enter the active portfolio only if: (1) all retained concepts fail a decisive feasibility or validation gate; (2) stakeholder requirements materially change; or (3) new evidence significantly improves the concept’s patent and implementation case.
**Rationale:** Deferral must remain reversible without allowing dormant concepts to continue consuming research effort or confusing the authoritative active-source set.
**Source evidence:** Project mC portfolio-closure decision.
**Alternatives:** Permanent rejection; unrestricted reopening.
**Decision type:** Portfolio governance requirement
**Verification status:** Accepted
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-010, PDR-011, PDR-064

**Decision ID:** PDR-067
**Title:** Phase 3C Retained-Portfolio Closure
**Phase introduced:** Phase 3C retained-portfolio closure
**Category:** Methodology & Project Management
**Decision or requirement:** Declare Phase 3C complete for the retained shortlist of OpenBraille, VibeGuard and TrueMoist. Do not state that Phase 3C was completed for all five original concepts. The next project action is a documented three-concept comparative down-selection followed by creation of the chosen concept’s Engineering Reference Manual and implementation context pack.
**Rationale:** This accurately preserves project history while allowing the methodology to advance without unnecessary work on deferred concepts.
**Source evidence:** Final Phase 3C reports/memories for OpenBraille, VibeGuard and TrueMoist; PDR-064.
**Alternatives:** Keep Phase 3C globally open; falsely mark all five concepts complete.
**Decision type:** Phase-gate decision
**Verification status:** Accepted
**Current status:** Accepted
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-043, PDR-064, PDR-065, PDR-066

***

#### Part V: Administration

**Decision ID:** PDR-038
**Title:** Team Roster Clarification
**Phase introduced:** Phase 3C
**Category:** Administration
**Decision or requirement:** The team operates as a five-member unit (Three technically capable CS/Cybersecurity members, One beginner/learner, One presenter/support member).
**Rationale:** Resolves documentation inconsistency across `vibeguard_sop.md` and prompts.
**Source evidence:** `Phase3C_VibeGuard_Architecture_Report_Final.md`
**Alternatives:** 6 members.
**Decision type:** Final decision
**Verification status:** Verified
**Current status:** Accepted and Resolved
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-002, PDR-044

**Decision ID:** PDR-044
**Title:** Beginner Programmer Tasks
**Phase introduced:** Phase 3C
**Category:** Administration
**Decision or requirement:** Assign the team's beginner programmer highly isolated software modules (e.g., Unicode-to-Braille lookup, LED state machines) early in the schedule.
**Rationale:** Provides a genuine embedded-systems learning opportunity without placing the critical path or physical integration at risk.
**Source evidence:** `Phase3C_OpenBraille_Architecture_Report_Final.md`, `Phase3C_OpenBraille_Synthesis_Prompt_Claude.md`, `Phase3C_VibeGuard_Architecture_Report_Final.md`
**Alternatives:** Assigning critical path DSP or mechanical tasks to the beginner.
**Decision type:** Recommendation
**Verification status:** Verified
**Current status:** Recommended team allocation
**Carry-forward requirement:** Yes
**Related PDR entries:** PDR-038


---

## Source 4: `01_GOVERNANCE_AND_CONTROL/03_Project_Context_and_Phase_Map/MC_Project_PHASE_DOC.md`

- Authority: `TIER_1`
- Treatment: `CORE_NARRATIVE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `8db62e0893293f93f89c00ab09640b6eb750118e140a820813f9c8aef5d00dde`

# Source Extraction

- Chapter: `01` — Project Mandate, Requirements and Governance
- Authority tier: `TIER_1`
- Manual treatment: `CORE_NARRATIVE`
- Original source: `01_GOVERNANCE_AND_CONTROL/03_Project_Context_and_Phase_Map/MC_Project_PHASE_DOC.md`
- Current SHA-256: `8db62e0893293f93f89c00ab09640b6eb750118e140a820813f9c8aef5d00dde`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

# MC_Project_PHASE_DOC.md
## Patent-Oriented Embedded Systems Innovation Pipeline
### Version 2.0 (Frozen)

---

# 📊 Project Progress

| Phase | Status |
|--------|--------|
| Phase 1A — Opportunity Discovery | ✅ Completed |
| Phase 1B — Opportunity Analysis | ✅ Completed |
| Phase 1B.5 — Opportunity Portfolio Optimization | ✅ Completed |
| Phase 1C — Concept Synthesis | ✅ Completed |
| Phase 2 — Patent Landscape Analysis | ✅ Completed  |
| Phase 3A — Engineering Landscape Discovery | ✅ Completed |
| Phase 3B — Engineering Feasibility Analysis | ✅ Completed |
| Phase 3C — Comparative Technical Evaluation | ✅ Completed for OpenBraille, VibeGuard and TrueMoist; TrustLatch and ColdTrace deferred before completing Phase 3C |
| Current project action | Final comparative down-selection among OpenBraille, VibeGuard and TrueMoist |
| Phase 4 — Engineering Feasibility & Prototype Planning | ⏳ Not started |
| Phase 5 — Patentability & Commercial Evaluation | ⏳ Pending |
| Phase 6 — Prototype Engineering | ⏳ Pending |
| Phase 7 — Prototype Development | ⏳ Pending |
| Phase 8 — Validation & Benchmarking | ⏳ Pending |
| Phase 9 — Documentation & Future IP | ⏳ Pending |

---

# 🎯 Ultimate Goal

Develop an embedded systems innovation that:

- Can be completed as a semester project.
- Demonstrates excellent engineering.
- Has realistic patent potential.
- Can evolve into a research paper.
- Can become a hackathon-quality demonstration.
- Can eventually become a startup.

The semester prototype is considered the first milestone of a much larger innovation journey.

---

# Phase 1A — Opportunity Discovery

## Objective

Discover evidence-backed real-world problems.

The objective is NOT to invent solutions.

---

## Activities

- Technology scouting
- Industry reports
- Research papers
- Engineering communities
- Patent awareness
- Opportunity collection

---

## Deliverables

- Opportunity Discovery Reports
- Master Opportunity Database
- Opportunity Repository
- Initial Opportunity Rankings

---

## Research Strategy

Primary:
Deep Research

Secondary:
Claude + ChatGPT

---

## Artifacts

Methodology:
Phase1A.md

Memory:
Phase1A_Memory.md

Execution:
Phase1A_Report.pdf

---

**Status:** ✅ Completed

---

# Phase 1B — Opportunity Analysis

## Objective

Transform raw opportunities into an objective engineering decision framework.

---

## Activities

- Opportunity extraction
- Duplicate merging
- Opportunity clustering
- Structured records
- Opportunity evaluation
- Patent Opportunity Matrix
- Quantitative scoring
- Portfolio ranking

---

## Deliverables

- Opportunity Cluster Database
- Opportunity Evaluation Matrix
- Ranked Opportunity Portfolio
- Patent Opportunity Matrix

---

## Research Strategy

Primary:
Engineering reasoning

Secondary:
Claude + ChatGPT

Deep Research:
Not required

---

## Artifacts

Methodology:
Phase1B.md

Memory:
Phase1B_Memory.md

Execution:
Phase1B_Report.pdf

---

**Status:** ✅ Completed

---

# Phase 1B.5 — Opportunity Portfolio Optimization

## Objective

Filter the validated opportunity portfolio through structured engineering decision gates.

---

## Activities

- Engineering gate review
- Semester feasibility
- Budget feasibility
- Embedded necessity
- Patent white-space evaluation
- Demonstration value
- Team capability
- Innovation density
- Portfolio optimization
- Diversity assessment

---

## Deliverables

- Gate Evaluation Matrix
- Opportunity Elimination Log
- Survivor Portfolio
- Portfolio Diversity Analysis
- Optimized Opportunity Portfolio

---

## Research Strategy

Primary:
Engineering reasoning

Secondary:
Claude + ChatGPT

Deep Research:
Not required

---

## Artifacts

Methodology:
Phase1B5.md

Memory:
Phase1B5_Memory.md

Execution:
Phase1B5_Report.pdf

---

**Status:** ✅ Completed

---

# Phase 1C — Concept Synthesis

## Objective

Transform the optimized opportunity portfolio into engineering project concepts.

This phase introduces concepts but intentionally avoids implementation.

---

## Activities

- Concept generation
- Comparative evaluation
- Portfolio comparison
- Concept ranking
- Top concept selection

---

## Deliverables

- Concept Portfolio
- Evaluation Matrix
- Ranked Concepts
- Top Five Concepts

---

## Research Strategy

Primary:
Engineering reasoning

Secondary:
Claude + ChatGPT

Deep Research:
Usually not required

---

## Artifacts

Methodology:
Phase1C.md

Memory:
Phase1C_Memory.md

Execution:
Phase1C_Report.pdf

---

**Status:** ✅ Completed

---

# Phase 2 — Patent Landscape Analysis

## Objective

Determine whether the selected concepts occupy meaningful intellectual property white space and justify continued engineering investment.

This phase evaluates the surrounding patent landscape rather than determining absolute patentability.

---

## Activities

- Independent multi-source patent research
- Concept validation
- Patent landscape analysis
- Prior-art analysis
- Patent family identification
- Commercial ecosystem analysis
- White-space discovery
- Existing solution limitations
- Patent saturation assessment
- Obviousness assessment
- Freedom-to-operate (high-level)
- Cross-concept portfolio analysis
- Evidence synthesis
- Confidence assessment

---

## Deliverables

- Patent Landscape Report
- Comparative Patent Matrix
- Cross-Concept Analysis
- Portfolio Assessment
- Phase2_Memory.md

---

## Research Strategy

Primary:

Deep Research (multiple independent AI systems)

Secondary:

Claude + ChatGPT synthesis

Methodology:

Independent research → Concept Validation → Evidence Synthesis

---

## Lessons Learned

The execution of Phase 2 introduced several permanent improvements to the project methodology.

- Every Deep Research phase must include the official Phase1C concept definitions before research begins.
- Independent agreement between multiple research systems is treated as stronger evidence than the confidence of any individual report.
- Concept validation must occur before comparing or synthesizing evidence.
- Patent landscape analysis should distinguish between technical white space and application-specific white space.
- Trademark observations should be documented separately from patentability conclusions.
- Findings requiring legal opinions or engineering experiments are recorded as future-phase inputs rather than reasons to repeat research.

---

## Artifacts

Methodology:

Phase2.md

Memory:

Phase2_Memory.md

Execution:

Phase2_Report.pdf

---

**Status:** ✅ Completed

---

# Phase 3 — Research Landscape Analysis

## Objective

Understand the academic state of the art.

---

## Activities

- IEEE review
- ACM review
- Springer
- Elsevier
- arXiv
- Conference papers
- State-of-the-art extraction
- Research gaps
- Future work
- Open technical challenges

---

## Deliverables

Research Landscape Report

Research Gap Analysis

---

## Research Strategy

Primary:
Deep Research

Secondary:
Claude + ChatGPT

---

**Status:** ⏳ Pending

---

Engineering Design Review
(Status: Mandatory)

The Engineering Design Review serves as the gate between
Phase 3A and Phase 3B.

It fixes:

• Engineering Identity
• Mission
• Engineering Hypothesis
• Fixed Design Principles
• Minimum Demonstrable Success

These become immutable engineering constraints for all later phases.

Future phases shall evaluate implementation approaches without redefining these approved engineering specifications.

# Phase 4 — Idea Synthesis

## Objective

Refine the surviving concepts using the findings from patent and research analyses.

---

## Inputs

- Opportunity Portfolio
- Patent White Spaces
- Research Gaps

---

## Activities

- Innovation synthesis
- Technology combination
- Novel concept refinement
- Patent-oriented improvements

---

## Deliverables

Refined Engineering Concepts

---

## Research Strategy

Primary:
Engineering reasoning

Secondary:
Claude + ChatGPT

Deep Research:
Optional

---

**Status:** ⏳ Pending

---

# Phase 5 — Patentability & Commercial Evaluation

## Objective

Select the strongest concept.

---

## Evaluation Criteria

- Novelty
- Non-obviousness
- Utility
- Manufacturability
- Prototype feasibility
- Cost
- Market demand
- Startup potential
- Semester suitability

---

## Deliverables

Final Winning Concept

Patent Potential Report

---

## Research Strategy

Primary:
Engineering reasoning

Secondary:
Claude + ChatGPT

Deep Research:
Minimal

---

**Status:** ⏳ Pending

---

# Phase 6 — Prototype Engineering

## Objective

Convert the selected concept into a complete engineering design.

This is the FIRST phase where engineering implementation decisions are made.

---

## Activities

- System architecture
- Hardware architecture
- Software architecture
- Communication architecture
- Security architecture
- MCU selection
- Sensor selection
- Communication protocol selection
- AI model selection
- Power analysis
- Bill of Materials
- Budget optimization
- Risk analysis
- Development planning

---

## Deliverables

Complete Engineering Design Package

---

## Research Strategy

Primary:
Engineering reasoning

Secondary:
Deep Research (targeted)

Used for:

- Component comparison
- Datasheets
- Indian pricing
- Hardware availability
- Library support
- Engineering alternatives

---

**Status:** ⏳ Pending

---

# Phase 7 — Prototype Development

## Activities

- Embedded firmware
- Hardware integration
- AI integration
- PCB/Breadboard implementation
- Debugging
- System integration
- Optimization

---

## Deliverables

Working Prototype

---

## Research Strategy

Primary:
Engineering implementation

Deep Research:
Not normally required

---

**Status:** ⏳ Pending

---

# Phase 8 — Validation & Benchmarking

## Activities

- Functional testing
- Performance benchmarking
- Cost analysis
- Reliability testing
- Security testing
- User evaluation
- Comparison against existing solutions

---

## Deliverables

Validation Report

Experimental Results

---

## Research Strategy

Primary:
Engineering analysis

Deep Research:
Optional

---

**Status:** ⏳ Pending

---

# Phase 9 — Documentation & Future IP

## Deliverables

- Final Report
- Technical Paper Draft
- Patent Disclosure Draft
- Poster
- Presentation
- Demo Script
- Future Work Roadmap

---

## Research Strategy

Primary:
Documentation

---

**Status:** ⏳ Pending

---

# 📚 Project Knowledge Base

Every completed phase permanently produces three documents.

## 1. Methodology (SOP)

Defines HOW the phase should always be executed.

This document should remain stable throughout the project.

---

## 2. Memory

Summarizes WHAT happened during execution.

Optimized for rapid AI context restoration.

---

## 3. Execution Report

Contains complete evidence, analyses, rankings, engineering decisions, tables, and supporting research.

---

# 🏛 Ground Rules (Project Constitution)

These rules remain in effect throughout the project.

1. Never begin with a solution. Begin with a validated problem.

2. Every engineering decision must be evidence-based.

3. Novelty is preferred over unnecessary complexity.

4. Target prototype budget:
   - Preferred: ≤ ₹3000
   - Maximum: ≤ ₹5000

5. Target prototype timeline:
   - Approximately two months.

6. Do not commit to a project before completing Patent and Research Landscape Analysis.

7. Keep records of every engineering decision and every rejection.

8. Hardware decisions (MCU, sensors, communications, BOM, PCB, etc.) are intentionally postponed until Phase 6 unless required for high-level feasibility estimation.

9. Completed phases are considered frozen once their SOP, Memory, and Execution Report have been finalized. Changes should only be made to correct factual or methodological errors.

---

# 🧭 Philosophy

The project shall evolve through disciplined engineering rather than intuition.

Every phase transforms evidence into knowledge, knowledge into concepts, concepts into engineering, and engineering into innovation.

The objective is not merely to complete a semester project, but to establish a repeatable research and innovation process capable of producing patent-worthy embedded systems.


---

## Source 5: `01_GOVERNANCE_AND_CONTROL/03_Project_Context_and_Phase_Map/PROJECT_CONCEPT_CONTEXT.md`

- Authority: `TIER_1`
- Treatment: `CORE_NARRATIVE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `f520cb5201e299fb0f9185bd2b79318229b898e5a8ad7822deb9a073e8f6cae4`

# Source Extraction

- Chapter: `01` — Project Mandate, Requirements and Governance
- Authority tier: `TIER_1`
- Manual treatment: `CORE_NARRATIVE`
- Original source: `01_GOVERNANCE_AND_CONTROL/03_Project_Context_and_Phase_Map/PROJECT_CONCEPT_CONTEXT.md`
- Current SHA-256: `f520cb5201e299fb0f9185bd2b79318229b898e5a8ad7822deb9a073e8f6cae4`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

# PROJECT_CONCEPT_CONTEXT.md

**Project:** Patent-Worthy Embedded Systems Innovation Methodology

**Document Type:** Canonical Concept Context

**Status:** Active

**Purpose:**
This document serves as the authoritative high-level reference for the five shortlisted project concepts selected during Phase 1C.

Its purpose is to ensure that every future research, analysis, engineering, and evaluation phase begins from a common understanding of the concepts. This minimizes interpretation drift between different AI systems and human reviewers.

This document complements, but does not replace, the detailed Phase1C Report.

Whenever ambiguity exists, the Phase1C Report remains the ultimate source of truth.

---

# Usage Rules

Any future AI system participating in this methodology must:

1. Read this document before beginning work.
2. Use these summaries only as grounding context.
3. Refer to the Phase1C Report for detailed concept definitions.
4. Never infer functionality solely from project names.
5. Explicitly verify its understanding before beginning analysis.

---

# Project Constraints

These constraints apply to every concept unless explicitly revised.

Prototype Budget

Preferred:
≤ ₹3000 INR

Maximum:
≤ ₹5000 INR

Prototype Timeline

Approximately 2 months

Team

Five members

Technical Team

Three technically strong Computer Science / Cybersecurity engineering students capable of:

- Embedded Programming
- STM32 / ESP32
- Arduino
- Linux
- Networking
- IoT
- Cybersecurity
- AI Integration
- System Integration

Project Objectives

- Excellent semester project
- Patent potential
- Research publication potential
- Startup potential

---

# Selected Concepts

---

## Concept 1 — OpenBraille

### Core Engineering Problem

Electronic refreshable Braille displays remain prohibitively expensive, limiting accessibility for visually impaired users, particularly in developing regions.

### Core Innovation

OpenBraille proposes a low-cost refreshable single-cell Braille display that explores alternative embedded actuation mechanisms and modular scalability to significantly reduce manufacturing cost while maintaining practical usability.

The concept focuses on affordability, accessibility, modular embedded design, and scalable assistive technology rather than competing directly with premium commercial Braille devices.

### What This Project IS

- Low-cost refreshable Braille display
- Embedded assistive technology
- Accessibility-focused innovation
- Modular and scalable design

### What This Project IS NOT

- Braille printer
- OCR software
- Screen reader
- Full-page Braille display

---

## Concept 2 — VibeGuard

### Core Engineering Problem

Many small and medium-sized industries lack affordable predictive maintenance systems capable of identifying abnormal machine behaviour before failures occur.

### Core Innovation

VibeGuard proposes an embedded vibration monitoring platform that uses onboard sensing and edge intelligence to identify abnormal machine vibration patterns, enabling predictive maintenance without requiring expensive industrial monitoring infrastructure.

The emphasis is on affordable industrial deployment and embedded intelligence rather than enterprise-scale predictive maintenance platforms.

### What This Project IS

- Embedded predictive maintenance
- Industrial vibration monitoring
- Edge intelligence
- Condition monitoring

### What This Project IS NOT

- Personal safety wearable
- Security alarm
- Fitness tracker
- Smartphone application

---

## Concept 3 — TrueMoist

### Core Engineering Problem

Low-cost soil moisture monitoring systems often suffer from calibration drift, poor long-term accuracy, and unreliable irrigation recommendations.

### Core Innovation

TrueMoist proposes an intelligent embedded soil moisture monitoring system that emphasizes improved measurement reliability, adaptive sensing behaviour, and practical deployment for smallholder agriculture.

The objective is not simply measuring moisture, but improving decision quality through more reliable embedded sensing.

### What This Project IS

- Intelligent soil moisture monitoring
- Precision agriculture
- Embedded sensing
- Adaptive environmental monitoring

### What This Project IS NOT

- Weather forecasting
- General farm management software
- Crop disease detection
- Satellite agriculture platform

---

## Concept 4 — TrustLatch

### Core Engineering Problem

Many IoT devices lack affordable hardware-backed identity and secure device authentication, leaving embedded systems vulnerable to spoofing and unauthorized access.

### Core Innovation

TrustLatch proposes a low-cost embedded hardware root-of-trust that strengthens IoT device authentication using embedded security principles.

The emphasis is on embedded identity, secure authentication, and hardware-assisted trust establishment rather than physical access control.

### What This Project IS

- Embedded hardware security
- Root-of-trust
- Secure IoT authentication
- Hardware-assisted identity

### What This Project IS NOT

- Smart door lock
- Password manager
- Physical access control system
- Electronic lock

---

## Concept 5 — ColdTrace

### Core Engineering Problem

Cold-chain transportation for pharmaceuticals and temperature-sensitive products often lacks affordable continuous environmental monitoring capable of ensuring product integrity throughout transit.

### Core Innovation

ColdTrace proposes an embedded environmental monitoring platform for cold-chain logistics that continuously records and verifies storage conditions, enabling improved traceability and quality assurance.

The focus is reliable embedded monitoring rather than fleet management or logistics optimization.

### What This Project IS

- Cold-chain environmental monitoring
- Embedded temperature logging
- Product traceability
- Pharmaceutical logistics support

### What This Project IS NOT

- Fleet tracking system
- GPS logistics platform
- Warehouse management software
- General IoT asset tracker

---

# Interpretation Policy

If any project name could reasonably describe multiple technologies:

DO NOT make assumptions.

Always resolve ambiguity using:

1. This document.
2. The detailed Phase1C Report.

The Phase1C Report always takes precedence.

---

# Relationship to Other Documents

This document should accompany:

- Phase1C Report
- Phase2 Report
- Phase3 Research Prompt
- Future engineering analysis
- Future patent analysis
- Future implementation planning

This document is intended to remain stable throughout the remainder of the project unless Phase1C itself is formally revised.


---

## Source 6: `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/AGENTS.md`

- Authority: `TIER_1`
- Treatment: `CORE_NARRATIVE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `f04384c78d2b342eaccf951dc126ad8df809210b233e199ce06ec169736a5594`

# Source Extraction

- Chapter: `01` — Project Mandate, Requirements and Governance
- Authority tier: `TIER_1`
- Manual treatment: `CORE_NARRATIVE`
- Original source: `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/AGENTS.md`
- Current SHA-256: `f04384c78d2b342eaccf951dc126ad8df809210b233e199ce06ec169736a5594`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

# Project mC Repository Instructions

## Repository policy

The current Phase 1 / Phase 2 / Phase 3 hierarchy was manually designed by
the project owner. Preserve it unless a specific change is approved.

Prefer minimal cleanup over replacement of the entire structure.

## Current project state

The retained concepts are:

1. OpenBraille
2. VibeGuard
3. TrueMoist

TrustLatch and ColdTrace are deferred. They are not technically rejected,
but they are not active final-selection candidates.

Phase 3C is complete for the retained three-concept shortlist.

The next project task is a final comparison of OpenBraille, VibeGuard and
TrueMoist.

## Authoritative document order

When documents conflict, use this precedence:

1. Engineering Design Review
2. Latest Project mC Decision Register
3. Phase 3C Retained Portfolio Closure Memo
4. Final Phase 3C architecture reports
5. Phase 3C memories
6. Phase 3B report and memory
7. Phase 3A report and memory
8. Phase 2 report and memory
9. Phase 1C concept synthesis and dossiers
10. Raw independent research

Raw AI research is evidence, not an authoritative project decision.

## Known authoritative governance files

- MC_Project_PHASE_DOC.md
- PHASE 3/Engineering_Design_Review.md
- Project_mC_Decision_Register_v1.2.md
- PHASE 3/PHASE 3C-Comparative Technical Evaluation/Phase3C_Portfolio_Closure_Memo_Approved.md

## Existing convenience collections

The following are convenience/context collections and must not be assumed
to contain the canonical copies:

- COPY PASTE FOLDER/
- every sop and memory/
- contexts.zip
- phase-specific ZIP files

Compare their contents against canonical files before recommending action.

## Safety rules

- Never permanently delete project files.
- Never execute unknown or untrusted files.
- `main/` is currently an empty, untracked directory and must not be
  treated as an executable file.
- Never expose or copy credentials.
- Do not rewrite technical conclusions during file cleanup.
- Do not merge documents merely because filenames are similar.
- Compare actual content and hashes.
- Preserve PDR identifiers and historical decisions.
- Do not renumber PDR entries without checking the latest register.
- Do not move or rename anything during an audit-only task.
- Use `git mv` for approved moves.
- Record every approved move in REORGANIZATION_LOG.md.
- Treat PDFs, DOCX files and Markdown files as duplicates only after
  comparing extracted content.
- Preserve failed research for methodology traceability.
- Update relative Markdown links after approved moves.

## Known special cases

- The ChatGPT OpenBraille Phase 3C deep-research output is a failed,
  mis-scoped research result. Preserve it as failed research, not as valid
  OpenBraille evidence.
- The authoritative VibeGuard Phase 3C architecture report is:
  `PHASE 3/PHASE 3C-Comparative Technical Evaluation/VibeGuard/Phase3C_VibeGuard_Architecture_Report_Final.md`.
  VibeGuard raw independent research remains under `VibeGuard/research/`.
- `Project_mC_Decision_Register_v1.2.md` is authoritative.
- `Project_mC_Decision_Register_v1.0_HISTORICAL.md` is retained only for
  decision-history traceability.
- Similar Gemini, Mistral, Perplexity and Qwen filenames under different
  concepts are not duplicates merely because their names match.


---

## Source 7: `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Legacy_Audits_and_Snapshots/CLEANUP_DIFF_NAME_STATUS.txt`

- Authority: `TIER_1`
- Treatment: `CORE_NARRATIVE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `109a32a0c4f7f991c157fb4743601f6033bea3db415edf5a04b24f5cc64f7f53`

# Source Extraction

- Chapter: `01` — Project Mandate, Requirements and Governance
- Authority tier: `TIER_1`
- Manual treatment: `CORE_NARRATIVE`
- Original source: `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Legacy_Audits_and_Snapshots/CLEANUP_DIFF_NAME_STATUS.txt`
- Current SHA-256: `109a32a0c4f7f991c157fb4743601f6033bea3db415edf5a04b24f5cc64f7f53`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

M	.gitignore
M	CURRENT_FOLDER_STRUCTURE.txt
M	MC_Project_PHASE_DOC.md
M	Project_mC_Decision_Register_v1.0_HISTORICAL.md
M	Project_mC_Decision_Register_v1.2.md
M	README.md


---

## Source 8: `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Legacy_Audits_and_Snapshots/CLEANUP_VALIDATION_REPORT.md`

- Authority: `TIER_1`
- Treatment: `CORE_NARRATIVE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `975767d50bf28bb29c0ed7b12b3c4949551f7fefc63f4aef9004335a7a18efe5`

# Source Extraction

- Chapter: `01` — Project Mandate, Requirements and Governance
- Authority tier: `TIER_1`
- Manual treatment: `CORE_NARRATIVE`
- Original source: `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Legacy_Audits_and_Snapshots/CLEANUP_VALIDATION_REPORT.md`
- Current SHA-256: `975767d50bf28bb29c0ed7b12b3c4949551f7fefc63f4aef9004335a7a18efe5`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

# Project mC Cleanup Validation Report

**Date:** 2026-07-29
**Scope:** Owner-approved minimal cleanup only
**Commit created:** No

## Actions completed

- Created `REORGANIZATION_LOG.md` before performing cleanup changes.
- Completed all four approved moves/renames using `git mv`.
- Added the required historical/superseded banner without changing the historical PDR body.
- Added authority notices to both convenience collections.
- Created the ZIP/context package notice.
- Expanded the root README with current status, retained/deferred concepts, authority order, canonical paths, Phase 3C reports/memories, and convenience warnings.
- Updated only the project-progress/status block in `MC_Project_PHASE_DOC.md`.
- Reduced `.gitignore` from three identical `key.txt` entries to one.
- Updated the 12 affected VibeGuard source-evidence filename references in the current Decision Register v1.2.
- Regenerated `CURRENT_FOLDER_STRUCTURE.txt` with the requested exclusions; it displays `main/` as a directory and does not list absent `key.txt`.
- Preserved all ZIP archives, convenience duplicates, deferred cross-format pairs, and raw research content.

## Exact moves

| Old path | New path | Result |
|---|---|---|
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/research/Phase3C_VibeGuard_Architecture_Report By Claude.md` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/Phase3C_VibeGuard_Architecture_Report_By_Claude.md` | Completed with `git mv`; content SHA-256 unchanged |
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Researches/DEEpr research on phase 3c openbraille by chatgpt` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Researches/FAILED_ChatGPT_Generic_Deep_Research_Framework.pdf` | Completed with `git mv`; content SHA-256 unchanged |
| `PHASE 3/PHASE 3A-Engineering Landscape Discovery/phase3B_report_and_summary.zip` | `PHASE 3/PHASE 3A-Engineering Landscape Discovery/Phase3A_report_and_memory.zip` | Completed with `git mv`; content SHA-256 unchanged |
| `Project_mC_Decision_Register_v1.0.md.save` | `Project_mC_Decision_Register_v1.0_HISTORICAL.md` | Completed with `git mv`; required banner added and all original body bytes preserved |

## Files edited

- `.gitignore`
- `CURRENT_FOLDER_STRUCTURE.txt`
- `MC_Project_PHASE_DOC.md`
- `Project_mC_Decision_Register_v1.0_HISTORICAL.md` (banner only, in addition to approved rename)
- `Project_mC_Decision_Register_v1.2.md` (12 source-evidence filename substitutions only)
- `README.md`
- `REORGANIZATION_LOG.md`

The first three moved artifacts were not content-edited.

## Files created

- `REORGANIZATION_LOG.md`
- `COPY PASTE FOLDER/README.md`
- `every sop and memory/README.md`
- `CONTEXT_AND_ZIP_PACKAGES.md`
- `CLEANUP_VALIDATION_REPORT.md`

## Exact changed project-progress/status block

```markdown
# 📊 Project Progress

| Phase | Status |
|--------|--------|
| Phase 1A — Opportunity Discovery | ✅ Completed |
| Phase 1B — Opportunity Analysis | ✅ Completed |
| Phase 1B.5 — Opportunity Portfolio Optimization | ✅ Completed |
| Phase 1C — Concept Synthesis | ✅ Completed |
| Phase 2 — Patent Landscape Analysis | ✅ Completed  |
| Phase 3A — Engineering Landscape Discovery | ✅ Completed |
| Phase 3B — Engineering Feasibility Analysis | ✅ Completed |
| Phase 3C — Comparative Technical Evaluation | ✅ Completed for OpenBraille, VibeGuard and TrueMoist; TrustLatch and ColdTrace deferred before completing Phase 3C |
| Current project action | Final comparative down-selection among OpenBraille, VibeGuard and TrueMoist |
| Phase 4 — Engineering Feasibility & Prototype Planning | ⏳ Not started |
| Phase 5 — Patentability & Commercial Evaluation | ⏳ Pending |
| Phase 6 — Prototype Engineering | ⏳ Pending |
| Phase 7 — Prototype Development | ⏳ Pending |
| Phase 8 — Validation & Benchmarking | ⏳ Pending |
| Phase 9 — Documentation & Future IP | ⏳ Pending |
```

No phase methodology, definition, or technical conclusion outside this block was changed.

## Validation results

1. `git status --short`: completed; shows only the approved tracked changes/moves and five approved new cleanup documents.
2. `git diff --check`: passed with exit status 0.
3. `git diff --name-status`: completed. Because `git mv` stages renames while later edits are unstaged, the working-tree-only command reports unstaged modifications; `git diff HEAD --name-status` additionally confirms three `R100` renames and one `R099` rename with the banner change.
4. Duplicate PDR identifiers: none. The current Decision Register contains 67 Decision ID entries and 67 unique IDs.
5. Approved old paths: all four absent.
6. Approved new paths: all four exist as files.
7. Stale old-name search:
   - No stale old-name reference remains in current Decision Register v1.2, root README, phase roadmap, or regenerated structure listing.
   - The old VibeGuard report basename remains intentionally in the historical v1.0 PDR body and its convenience duplicate. Those files were not changed because historical PDR entries and convenience duplicates were explicitly protected.
   - Reorganization/audit/validation records necessarily retain old paths to document the mappings.
8. File deletion: none. `git diff HEAD --name-status` reports renames rather than standalone deletions; all six ZIP archives remain present.
9. Unexpected modifications: none found. All changed and newly created files fall within the approved mappings, notices, governance/navigation edits, structure regeneration, log, and validation report.
10. Move integrity:
    - VibeGuard report SHA-256 match: `d6a5f009d5c96bceb6cc0cb2f4d70817204e7346e7f6e7c21a5e86b457254573`
    - Failed OpenBraille PDF SHA-256 match: `864e400d3b259157346319b53eb36868b28bf183fb6ac5a1efbcbb6315424e06`
    - Phase 3A ZIP SHA-256 match: `9d0593bb50717c290ca9c36d135ffc1aebfb70a48d2b058be4c8b421af44ae21`
    - Historical Decision Register original body: byte-for-byte match after removing the four-line banner.
11. Root README link targets: all 13 direct relative links resolve to existing files.
12. `main/`: remains an empty, untracked directory awaiting owner review.

## Unresolved or deferred issues

- Intentional historical old-name references described above.
- Empty untracked `main/` directory awaits owner review.
- Phase 2 Qwen PDF/Markdown comparison remains deferred.
- VibeGuard `.md`/`.mmd` synthesis prompt pair remains deferred.
- Exact convenience duplicates, ZIP packages, and PDF/Markdown report pairs remain untouched.

## Deviations from approved plan

None. Intentional historical references were retained to comply with the instruction not to alter historical PDR entries or convenience duplicates.


---

## Source 9: `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Legacy_Audits_and_Snapshots/CONTEXT_AND_ZIP_PACKAGES.md`

- Authority: `TIER_1`
- Treatment: `CORE_NARRATIVE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `98a9febc897d759037e545cba8424e0bec33243804d0bcda5285b7bd5cfbe16d`

# Source Extraction

- Chapter: `01` — Project Mandate, Requirements and Governance
- Authority tier: `TIER_1`
- Manual treatment: `CORE_NARRATIVE`
- Original source: `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Legacy_Audits_and_Snapshots/CONTEXT_AND_ZIP_PACKAGES.md`
- Current SHA-256: `98a9febc897d759037e545cba8424e0bec33243804d0bcda5285b7bd5cfbe16d`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

# Context and ZIP Packages

The following archives are convenience or historical context packages:

- `contexts.zip`
- `every sop and memory/every_sop_and memory_from phase 1A to 1C and whoel phase overview.zip`
- `PHASE 1/PHASE 1.B/Phase1B_Opportunity_Analysis.zip`
- `PHASE 2/Phase2_docs.zip`
- `PHASE 3/PHASE 3A-Engineering Landscape Discovery/Phase3A_report_and_memory.zip`
- `PHASE 3/PHASE 3B-Engineering Feasibility Analysis/Phase3B_mem_and_report.zip`

ZIP members must not override normal canonical repository files. When an archive member conflicts with a normal file, use the project authority order and the canonical normal file at its root or phase path.

`contexts.zip` contains a unique older `MC_Project_PHASE_DOC.md` snapshot. Preserve that member as historical context; it is not the current project methodology or status authority.

These archives have not been moved, deleted, consolidated, or extracted into the repository.


---

## Source 10: `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Legacy_Audits_and_Snapshots/CURRENT_FOLDER_STRUCTURE.txt`

- Authority: `TIER_1`
- Treatment: `CORE_NARRATIVE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `ba3153f5011ecff39f4eadce191d7941cc29801a3b6eb4761a4e87e9a65fc8b1`

# Source Extraction

- Chapter: `01` — Project Mandate, Requirements and Governance
- Authority tier: `TIER_1`
- Manual treatment: `CORE_NARRATIVE`
- Original source: `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Legacy_Audits_and_Snapshots/CURRENT_FOLDER_STRUCTURE.txt`
- Current SHA-256: `ba3153f5011ecff39f4eadce191d7941cc29801a3b6eb4761a4e87e9a65fc8b1`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

./
├── COPY PASTE FOLDER/
│   ├── Claudes report on the research Phases 3a.pdf
│   ├── Document_4_TrustLatch_Concept_Dossier.docx
│   ├── Engineering_Design_Review.md
│   ├── MC_Project_PHASE_DOC.md
│   ├── PROJECT_CONCEPT_CONTEXT.md
│   ├── Phase2_Memory.md
│   ├── Phase2_Report by CLaude.md
│   ├── Phase3A_MEMORY.md
│   ├── Phase3B_MEMORY.md
│   ├── Phase3B_Report_by_Claude.md
│   ├── Phase3C_TrueMoist_SOP.md
│   ├── Project_mC_Decision_Register_v1.0.md
│   └── README.md
├── PHASE 1/
│   ├── PHASE 1.A/
│   │   ├── RESEARCHS/
│   │   │   ├── CHATGPT DEEP RESEARCH.md
│   │   │   ├── GEMINI DEEP RESEARCH.docx
│   │   │   ├── KIMI DEEP RESEARCH.docx
│   │   │   └── QWEN AI DEEP RESEARCH.pdf
│   │   ├── Phase1A_Memory.md
│   │   └── Phase1A_Summary.md
│   ├── PHASE 1.B/
│   │   ├── Phase1B_Memory.md
│   │   ├── Phase1B_Opportunity_Analysis.md
│   │   ├── Phase1B_Opportunity_Analysis.zip
│   │   └── Phase1B_Opportunity_Analysis_By_Claude.pdf
│   ├── PHASE 1B.5/
│   │   ├── Phase1B5_Memory.md
│   │   ├── Phase1B5_Opportunity_Portfolio_Optimization.md
│   │   └── Phase1B5_Portfolio_Optimization_By_Claude.pdf
│   └── PHASE 1C/
│       ├── 5 IDEA ABSTRACT/
│       │   ├── Microcontroller_Project_Abstract_Proposal_5_Ideas.pdf
│       │   ├── Microcontroller_Project_Idea_Abstracts 2.0.pdf
│       │   └── Microcontroller_Project_Idea_Abstracts.pdf
│       ├── INDEPTH OF EACH FIVE IDEA/
│       │   ├── Document_1_OpenBraille_Concept_Dossier.docx
│       │   ├── Document_2_VibeGuard_Concept_Dossier.docx
│       │   ├── Document_3_TrueMoist_Concept_Dossier.docx
│       │   └── Document_4_TrustLatch_Concept_Dossier.docx
│       ├── OTHERS IDEA FORMAT/
│       │   ├── POOJA PROJECT.pdf
│       │   ├── Patent Potential of Student Projects.docx
│       │   ├── USB_Powered_Secure_File_Transfer_Authentication_Abstract.pdf
│       │   ├── USB_Powered_Smart_Anti_Theft_System_Abstract.pdf
│       │   └── USB_Powered_Smart_Cabinet_Abstract.pdf
│       ├── visual explanation of the 5 ideas/
│       │   ├── 11 ideas.html
│       │   └── top 5.html
│       ├── Phase1C.md
│       ├── Phase1C_Concept_Synthesis.pdf
│       ├── Phase1C_Memory.md
│       ├── minimalist_project_proposal.pdf
│       └── project_proposal_booklet.pdf
├── PHASE 2/
│   ├── RESEARCH DOCS/
│   │   ├── CHATGT Research on Patent.docx
│   │   ├── Gemini Reearch on phase 2.docx
│   │   ├── Kimi Patent Research.pdf
│   │   ├── QWen Research on Patent.pdf
│   │   └── Qwens Research on Phase 2.md
│   ├── 2_Sop.md
│   ├── Phase2_DeepResearch_Prompt_v2.md
│   ├── Phase2_Memory.md
│   ├── Phase2_Report From Claude.pdf
│   ├── Phase2_Report by CLaude.md
│   └── Phase2_docs.zip
├── PHASE 3/
│   ├── PHASE 3A-Engineering Landscape Discovery/
│   │   ├── Claudes report on the research Phases 3a.pdf
│   │   ├── Geminis Research On Phase 3A.docx
│   │   ├── MISTRAL RESEAARCH ON phase 3a.md
│   │   ├── Perplexity Research on Phase 3A.pdf
│   │   ├── Phase3A_MEMORY.md
│   │   ├── Phase3A_report_and_memory.zip
│   │   └── Qwen Research on Phase 3A.md
│   ├── PHASE 3B-Engineering Feasibility Analysis/
│   │   ├── Gemini Research on Phase 3B.docx
│   │   ├── Mistral researon on Phase 3B.md
│   │   ├── Phase3B_DeepResearch_Prompt.md
│   │   ├── Phase3B_MEMORY.md
│   │   ├── Phase3B_Report_by_Claude.md
│   │   ├── Phase3B_mem_and_report.zip
│   │   ├── Project_mC_Phase3B_SOP.md
│   │   ├── Qwen Rsearch on Phase 3B.pdf
│   │   └── perplexity_research_on_phase3B.md
│   ├── PHASE 3C-Comparative Technical Evaluation/
│   │   ├── OpenBraille/
│   │   │   ├── prompts/
│   │   │   │   ├── Phase3C_OpenBraille_Deep_Research_Prompt_Final.md
│   │   │   │   └── Phase3C_OpenBraille_Synthesis_Prompt_Claude.md
│   │   │   ├── research/
│   │   │   │   ├── Phase3C_OpenBraille_Failed_Research_ChatGPT.pdf
│   │   │   │   ├── Phase3C_OpenBraille_Raw_Research_Gemini.docx
│   │   │   │   ├── Phase3C_OpenBraille_Raw_Research_Mistral.md
│   │   │   │   ├── Phase3C_OpenBraille_Raw_Research_Perplexity.docx
│   │   │   │   └── Phase3C_OpenBraille_Raw_Research_Qwen.md
│   │   │   ├── Phase3C_OpenBraille_Architecture_Report_Final.md
│   │   │   ├── Phase3C_OpenBraille_Memory_Final.md
│   │   │   └── Phase3C_OpenBraille_SOP_Final.md
│   │   ├── TrueMoist/
│   │   │   ├── prompts/
│   │   │   │   ├── Phase3C_TrueMoist_Deep_Research_Prompt_Final.md
│   │   │   │   └── Phase3C_TrueMoist_Synthesis_Prompt_Final.md
│   │   │   ├── research/
│   │   │   │   ├── Phase3C_TrueMoist_Raw_Research_ChatGPT.pdf
│   │   │   │   ├── Phase3C_TrueMoist_Raw_Research_Gemini.docx
│   │   │   │   ├── Phase3C_TrueMoist_Raw_Research_Mistral.md
│   │   │   │   └── Phase3C_TrueMoist_Raw_Research_Perplexity.md
│   │   │   ├── Phase3C_TrueMoist_Architecture_Report_Final.md
│   │   │   ├── Phase3C_TrueMoist_Memory_Final.md
│   │   │   ├── Phase3C_TrueMoist_PDR_Patch_Historical.md
│   │   │   └── Phase3C_TrueMoist_SOP_Final.md
│   │   ├── VibeGuard/
│   │   │   ├── prompts/
│   │   │   │   ├── Phase3C_VibeGuard_Deep_Research_Prompt_Final.md
│   │   │   │   ├── Phase3C_VibeGuard_Synthesis_Prompt_Claude.md
│   │   │   │   └── Phase3C_VibeGuard_Synthesis_Prompt_Claude.mmd
│   │   │   ├── research/
│   │   │   │   ├── Phase3C_VibeGuard_Raw_Research_Gemini.docx
│   │   │   │   ├── Phase3C_VibeGuard_Raw_Research_Mistral.md
│   │   │   │   ├── Phase3C_VibeGuard_Raw_Research_Perplexity.md
│   │   │   │   └── Phase3C_VibeGuard_Raw_Research_Qwen.md
│   │   │   ├── Phase3C_VibeGuard_Architecture_Report_Final.md
│   │   │   ├── Phase3C_VibeGuard_Memory_Final.md
│   │   │   └── Phase3C_VibeGuard_SOP_Final.md
│   │   ├── Phase3C_Portfolio_Closure_Memo_Approved.md
│   │   └── README.md
│   ├── Engineering_Design_Review.md
│   └── Phase3_DeepResearch_Prompt.md
├── every sop and memory/
│   ├── MC_Project_PHASE_DOC.md
│   ├── Phase1A_Memory.md
│   ├── Phase1A_Summary.md
│   ├── Phase1B5_Memory.md
│   ├── Phase1B5_Opportunity_Portfolio_Optimization.md
│   ├── Phase1B_Memory.md
│   ├── Phase1B_Opportunity_Analysis.md
│   ├── Phase1C.md
│   ├── Phase1C_Memory.md
│   ├── README.md
│   └── every_sop_and memory_from phase 1A to 1C and whoel phase overview.zip
├── main/
├── .gitignore
├── AGENTS.md
├── CLEANUP_DIFF_NAME_STATUS.txt
├── CLEANUP_VALIDATION_REPORT.md
├── CONTEXT_AND_ZIP_PACKAGES.md
├── CURRENT_FOLDER_STRUCTURE.txt
├── MC_Project_PHASE_DOC.md
├── PHASE3C_NAMING_CHANGE_LOG.md
├── PHASE3C_NAMING_PROPOSAL.md
├── PHASE3C_NAMING_VALIDATION_REPORT.md
├── PROJECT_CONCEPT_CONTEXT.md
├── Phase3_SOP.md
├── Project_mC_Decision_Register_v1.0_HISTORICAL.md
├── Project_mC_Decision_Register_v1.2.md
├── README.md
├── REORGANIZATION_LOG.md
└── contexts.zip


---

## Source 11: `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Legacy_REORGANIZATION_LOG.md`

- Authority: `TIER_1`
- Treatment: `CORE_NARRATIVE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `fd53bcb50747e4703f60d64c0e3123cd7d1c467c36e1c2917e9da1d1f4198799`

# Source Extraction

- Chapter: `01` — Project Mandate, Requirements and Governance
- Authority tier: `TIER_1`
- Manual treatment: `CORE_NARRATIVE`
- Original source: `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Legacy_REORGANIZATION_LOG.md`
- Current SHA-256: `fd53bcb50747e4703f60d64c0e3123cd7d1c467c36e1c2917e9da1d1f4198799`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

# Project mC Reorganization Log

This log records the owner-approved minimal cleanup. No general reorganization is authorized.

| Old path | New path | Reason | Action status |
|---|---|---|---|
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/research/Phase3C_VibeGuard_Architecture_Report By Claude.md` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/Phase3C_VibeGuard_Architecture_Report_By_Claude.md` | The authoritative final Phase 3C architecture report belongs at the VibeGuard concept root, not among raw research. | Completed with `git mv` |
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Researches/DEEpr research on phase 3c openbraille by chatgpt` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Researches/FAILED_ChatGPT_Generic_Deep_Research_Framework.pdf` | Preserve the extensionless, generic, mis-scoped PDF as clearly marked failed evidence. | Completed with `git mv` |
| `PHASE 3/PHASE 3A-Engineering Landscape Discovery/phase3B_report_and_summary.zip` | `PHASE 3/PHASE 3A-Engineering Landscape Discovery/Phase3A_report_and_memory.zip` | The archive contains Phase 3A report and memory files, not Phase 3B files. | Completed with `git mv` |
| `Project_mC_Decision_Register_v1.0.md.save` | `Project_mC_Decision_Register_v1.0_HISTORICAL.md` | Preserve v1.0 for traceability while clearly distinguishing it from authoritative v1.2. | Completed with `git mv`; historical banner added |

## Non-file item awaiting owner review

- `main/` is an empty, untracked directory. It was not removed or modified and remains awaiting owner review.

## Reference-update note

- Source-evidence references in the current `Project_mC_Decision_Register_v1.2.md` were updated to the new VibeGuard report filename.
- Matching old filename text remains intentionally preserved inside the historical v1.0 register and its convenience duplicate because historical PDR entries and convenience duplicates were explicitly out of scope for content changes.


---

## Source 12: `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Legacy_Repository_Audit/01_CURRENT_STRUCTURE_ANALYSIS.md`

- Authority: `TIER_1`
- Treatment: `CORE_NARRATIVE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `364f2fb74e1ed35bc1024c0185d504618a32e858c621e0937add45d80f03d27b`

# Source Extraction

- Chapter: `01` — Project Mandate, Requirements and Governance
- Authority tier: `TIER_1`
- Manual treatment: `CORE_NARRATIVE`
- Original source: `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Legacy_Repository_Audit/01_CURRENT_STRUCTURE_ANALYSIS.md`
- Current SHA-256: `364f2fb74e1ed35bc1024c0185d504618a32e858c621e0937add45d80f03d27b`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

# Project mC Repository Organization Audit

**Audit date:** 2026-07-29
**Scope:** Current working tree, excluding `.git/` internals and the newly created `REPOSITORY_AUDIT/` outputs.
**Mode:** Audit only; no existing project file or directory was moved, renamed, edited, deleted, or executed.

## Executive finding

The owner-designed Phase 1 / Phase 2 / Phase 3 hierarchy is coherent and should be preserved. The main organization problem is not the hierarchy; it is ambiguity created by convenience copies, embedded ZIP copies, stale governance/context snapshots, one misplaced final report, one extensionless failed-research PDF, and inconsistent naming.

At audit start, the repository had **124 files**, all tracked, with a clean Git working tree. The population comprises 74 Markdown files, 21 PDFs, 16 DOCX files, 6 ZIP files, 2 HTML files, one MMD file, one `.save`, one TXT file, `.gitignore`, and the extensionless-PDF special case. The seven audit outputs are intentionally excluded from those counts and from the manifest population.

## Current hierarchy assessment

```text
PROJECT/
├── PHASE 1/
│   ├── PHASE 1.A/
│   ├── PHASE 1.B/
│   ├── PHASE 1B.5/
│   └── PHASE 1C/
├── PHASE 2/
│   └── RESEARCH DOCS/
├── PHASE 3/
│   ├── PHASE 3A-Engineering Landscape Discovery/
│   ├── PHASE 3B-Engineering Feasibility Analysis/
│   └── PHASE 3C-Comparative Technical Evaluation/
│       ├── openbraille/
│       ├── vibeguard/
│       └── TrueMoist/
├── COPY PASTE FOLDER/                 # convenience/context copies
├── every sop and memory/              # convenience/context copies
├── contexts.zip                       # convenience/context package
├── main/                              # empty directory, not a file
└── root governance/context files
```

This structure correctly preserves the project’s chronological pipeline. Phase 3C contains only the retained concepts OpenBraille, VibeGuard, and TrueMoist; TrustLatch and ColdTrace remain represented historically in earlier phases and governance records, consistent with deferral rather than rejection.

## What is working

- Canonical phase artifacts generally live in their phase directories.
- The four highest-priority governance records are present at their expected canonical paths.
- The current Decision Register is clearly versioned as v1.2 and records Phase 3C closure for the retained shortlist.
- Raw research remains preserved for methodology traceability.
- Exact hashing makes most convenience duplication unambiguous.
- All 21 `.pdf` files plus the extensionless PDF were text-extractable with the installed `pdftotext`; all 16 DOCX packages passed ZIP-integrity checks and their text was inspected directly from `word/document.xml`. No software was installed.

## Main structural risks

1. `COPY PASTE FOLDER/`, `every sop and memory/`, and ZIPs repeat canonical artifacts without local warning labels.
2. `MC_Project_PHASE_DOC.md` v2.0 still says Phase 3 is pending, conflicting with the newer EDR, Decision Register v1.2, and closure memo.
3. `CURRENT_FOLDER_STRUCTURE.txt` is stale: it lists `key.txt` and visually lists `main` without revealing that `main` is an empty directory.
4. The VibeGuard final architecture report is placed under `vibeguard/research/` beside raw evidence.
5. OpenBraille’s failed ChatGPT output is a PDF with no `.pdf` extension and a generic, mis-scoped research framework as its content.
6. Phase/folder naming is inconsistent but mostly cosmetic; wholesale normalization would create needless churn.

## Link audit

No Markdown inline links/images or HTML `href`/`src` references were present in the audited files, so no syntactically broken relative links were found. Backticked filenames in governance documents are references, not clickable Markdown links; their basename-only form is a discoverability weakness but not a broken-link result.

## Audit limitations

- Binary equality is definitive; cross-format equivalence is not assumed.
- PDF and DOCX text extraction can lose layout, tables, footnotes, and images.
- ZIP members were streamed for listing and hashing only; no archive was extracted into the repository.
- The empty `main/` directory has no file hash and is not represented in the file-only CSV; it is covered in the security report.


---

## Source 13: `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Legacy_Repository_Audit/02_FILE_MANIFEST.csv`

- Authority: `TIER_1`
- Treatment: `CORE_NARRATIVE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `959fd614ded4de4b178ddf31b03191d1192e34d32ba5575cb678e055df926521`

# Source Extraction

- Chapter: `01` — Project Mandate, Requirements and Governance
- Authority tier: `TIER_1`
- Manual treatment: `CORE_NARRATIVE`
- Original source: `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Legacy_Repository_Audit/02_FILE_MANIFEST.csv`
- Current SHA-256: `959fd614ded4de4b178ddf31b03191d1192e34d32ba5575cb678e055df926521`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

current_path,filename,extension,size_bytes,sha256,probable_phase,probable_concept,document_role,authority_level,exact_duplicate_group,possible_cross_format_duplicate_group,probable_canonical_file,confidence,manual_review_requirement
.gitignore,.gitignore,[none],26,06cbc9ed3b87cff938ebc17ad940c8cf13efcf2e8570025106b6a8b3d852b727,Repository-wide,Repository-wide/none,Git ignore configuration,Supporting/non-decision artifact,,,.gitignore,High,No
AGENTS.md,AGENTS.md,md,3014,7dc870163ab0eeb55112d377f5e015404ef631a55fd02332e8a692ead2b3b31e,Repository-wide,Repository-wide/none,Repository governance instructions,Governance/context (outside numbered technical precedence),,,AGENTS.md,High,No
COPY PASTE FOLDER/Claudes report on the research Phases 3a.pdf,Claudes report on the research Phases 3a.pdf,pdf,792034,7d0202fb62476a0212e594af473ad8d796eecd853e53e7f0952de90908cec611,Cross-phase/unclear,Repository-wide/none,Raw independent research,Level 10 — raw research evidence only,ED-08,,PHASE 3/PHASE 3A-Engineering Landscape Discovery/Claudes report on the research Phases 3a.pdf,High,Yes — convenience copy; do not treat as canonical
COPY PASTE FOLDER/Document_4_TrustLatch_Concept_Dossier.docx,Document_4_TrustLatch_Concept_Dossier.docx,docx,39031,f9a4184850435aba3ec26e480e802d1ba39f17037f0f368520a625c6f8e84f78,Cross-phase/unclear,TrustLatch (deferred),Concept dossier,Convenience/context only; non-canonical container,ED-20,,PHASE 1/PHASE 1C/INDEPTH OF EACH FIVE IDEA/Document_4_TrustLatch_Concept_Dossier.docx,High,Yes — convenience copy; do not treat as canonical
COPY PASTE FOLDER/Engineering_Design_Review.md,Engineering_Design_Review.md,md,31205,46f017501ac3ff9ebd6c1fb1e5ee8c068c22ddb08ae204c5609f2b759090295e,Cross-phase/unclear,Repository-wide/none,Engineering Design Review,Convenience copy of Level 1 — Engineering Design Review,ED-04,,PHASE 3/Engineering_Design_Review.md,High,Yes — convenience copy; do not treat as canonical
COPY PASTE FOLDER/MC_Project_PHASE_DOC.md,MC_Project_PHASE_DOC.md,md,11868,c4b6c4a56bf8ba3066c5b426dce5ae4d50da4774478b5074566e9c79812e3ece,Cross-phase/unclear,Multi-concept,Project methodology/phase roadmap,Governance/context (outside numbered technical precedence),ED-13,,MC_Project_PHASE_DOC.md,High,Yes — convenience copy; do not treat as canonical
COPY PASTE FOLDER/PROJECT_CONCEPT_CONTEXT.md,PROJECT_CONCEPT_CONTEXT.md,md,6646,f520cb5201e299fb0f9185bd2b79318229b898e5a8ad7822deb9a073e8f6cae4,Cross-phase/unclear,Multi-concept,Supporting project document,Convenience/context only; non-canonical container,ED-19,,PROJECT_CONCEPT_CONTEXT.md,High,Yes — convenience copy; do not treat as canonical
COPY PASTE FOLDER/Phase2_Memory.md,Phase2_Memory.md,md,7820,973519f45bc075c296d4302b94933288496bd9bc12fae708aac1fb7020158ce8,Phase 2,Multi-concept,Phase memory,Convenience copy of Level 8 — Phase 2 report/memory,ED-10,,PHASE 2/Phase2_Memory.md,High,Yes — convenience copy; do not treat as canonical
COPY PASTE FOLDER/Phase2_Report by CLaude.md,Phase2_Report by CLaude.md,md,44493,783729d0e07e725236db5296dae8504ce782c294b8c61cfab40ea172cfa6943e,Phase 2,Multi-concept,Phase report/supporting deliverable,Convenience copy of Level 8 — Phase 2 report/memory,ED-06,CF-01,PHASE 2/Phase2_Report by CLaude.md,High,Yes — cross-format scope/equivalence review
COPY PASTE FOLDER/Phase3A_MEMORY.md,Phase3A_MEMORY.md,md,8898,acd3b4178143ca918ed4cce43d3d853acc994c0178dc8efdc406fb014e1ec997,Phase 3A,Multi-concept,Phase memory,Convenience copy of Level 7 — Phase 3A report/memory,ED-12,,PHASE 3/PHASE 3A-Engineering Landscape Discovery/Phase3A_MEMORY.md,High,Yes — convenience copy; do not treat as canonical
COPY PASTE FOLDER/Phase3B_MEMORY.md,Phase3B_MEMORY.md,md,18836,7b6532c779867e9d6064473de4ba1b4799a0c385361cf27dc4616888fb0ac7ad,Phase 3B,Multi-concept,Phase memory,Convenience copy of Level 6 — Phase 3B report/memory,ED-07,,PHASE 3/PHASE 3B-Engineering Feasibility Analysis/Phase3B_MEMORY.md,High,Yes — convenience copy; do not treat as canonical
COPY PASTE FOLDER/Phase3B_Report_by_Claude.md,Phase3B_Report_by_Claude.md,md,83718,14c19ac85b56e4e27da03de534a2a574ab7220d90005b4a7a0afb868f6390478,Phase 3B,Multi-concept,Phase report/supporting deliverable,Convenience copy of Level 6 — Phase 3B report/memory,ED-01,,PHASE 3/PHASE 3B-Engineering Feasibility Analysis/Phase3B_Report_by_Claude.md,High,Yes — convenience copy; do not treat as canonical
COPY PASTE FOLDER/Phase3C_TrueMoist_SOP.md,Phase3C_TrueMoist_SOP.md,md,18712,993caf1a05f3fdc3937efb634e2f2e467488e973eb71454db8e3c3f53d178d00,Phase 3C,TrueMoist,Methodology/SOP,Convenience/context only; non-canonical container,ED-11,,PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_SOP.md,High,Yes — convenience copy; do not treat as canonical
COPY PASTE FOLDER/Project_mC_Decision_Register_v1.0.md,Project_mC_Decision_Register_v1.0.md,md,42548,2ecf77fbbba9966a7769a2e715034f6b9ff7362d7aa51261219ee118085d22d3,Cross-phase governance,Multi-concept,Project Decision Register,Historical/superseded Decision Register,ED-02,,Project_mC_Decision_Register_v1.0.md.save,High,Yes — ensure historical/superseded labeling
CURRENT_FOLDER_STRUCTURE.txt,CURRENT_FOLDER_STRUCTURE.txt,txt,7870,befdeb6ebd683f74616ace070a5aea279a46557886b4b4842c5441a436d787ff,Repository-wide,Repository-wide/none,Stale structure snapshot,Supporting/non-decision artifact,,,CURRENT_FOLDER_STRUCTURE.txt,High,Yes — stale status/version or structure snapshot
MC_Project_PHASE_DOC.md,MC_Project_PHASE_DOC.md,md,11868,c4b6c4a56bf8ba3066c5b426dce5ae4d50da4774478b5074566e9c79812e3ece,Repository-wide,Multi-concept,Project methodology/phase roadmap,Governance/context (outside numbered technical precedence),ED-13,,MC_Project_PHASE_DOC.md,High,Yes — stale status/version or structure snapshot
PHASE 1/PHASE 1.A/Phase1A_Memory.md,Phase1A_Memory.md,md,4029,5a8943e1e556e1db0644cc7b75e2b4c8000b1a9506d673406c9c70cf7bb4a213,Phase 1A,Multi-concept,Phase memory,Supporting/non-decision artifact,ED-05,,PHASE 1/PHASE 1.A/Phase1A_Memory.md,High,No
PHASE 1/PHASE 1.A/Phase1A_Summary.md,Phase1A_Summary.md,md,2794,c52bed09fdfd1a860471bfc6d56cd41411f730362d12ee0348e07ad0939909c9,Phase 1A,Multi-concept,Methodology/SOP,Supporting/non-decision artifact,ED-14,,PHASE 1/PHASE 1.A/Phase1A_Summary.md,High,No
PHASE 1/PHASE 1.A/RESEARCHS/CHATGPT DEEP RESEARCH.md,CHATGPT DEEP RESEARCH.md,md,20670,fa41ec5c0504aada478a754133290458a1333eee99542c4530d3fb2abc8f5ac0,Phase 1A,Repository-wide/none,Raw independent research,Level 10 — raw research evidence only,,,PHASE 1/PHASE 1.A/RESEARCHS/CHATGPT DEEP RESEARCH.md,High,No
PHASE 1/PHASE 1.A/RESEARCHS/GEMINI DEEP RESEARCH.docx,GEMINI DEEP RESEARCH.docx,docx,3035520,e527fa3ab029f3dd3096184c35f90ccd21e61bd520d9eb677f1031abbebd13ad,Phase 1A,Repository-wide/none,Raw independent research,Level 10 — raw research evidence only,,,PHASE 1/PHASE 1.A/RESEARCHS/GEMINI DEEP RESEARCH.docx,Medium,"No, unless used for a project decision"
PHASE 1/PHASE 1.A/RESEARCHS/KIMI DEEP RESEARCH.docx,KIMI DEEP RESEARCH.docx,docx,64142,c0d4cbeb9099d8a58c4fa6eab7e2f06aa1a0bda76affecb9444f040e8169828f,Phase 1A,Repository-wide/none,Raw independent research,Level 10 — raw research evidence only,,,PHASE 1/PHASE 1.A/RESEARCHS/KIMI DEEP RESEARCH.docx,Medium,"No, unless used for a project decision"
PHASE 1/PHASE 1.A/RESEARCHS/QWEN AI DEEP RESEARCH.pdf,QWEN AI DEEP RESEARCH.pdf,pdf,519844,5b3f7270de5bc6a27eba0e458cd2f7f40f55dd0407094f70ccfed6f6fd3f7ed8,Phase 1A,Repository-wide/none,Raw independent research,Level 10 — raw research evidence only,,,PHASE 1/PHASE 1.A/RESEARCHS/QWEN AI DEEP RESEARCH.pdf,Medium,"No, unless used for a project decision"
PHASE 1/PHASE 1.B/Phase1B_Memory.md,Phase1B_Memory.md,md,3966,d58c91eead60c5abdb4e38c1e9b87c7449f4b3b68ccd7a23f5d4816fea16ff76,Phase 1B,Multi-concept,Phase memory,Supporting/non-decision artifact,ED-16,,PHASE 1/PHASE 1.B/Phase1B_Memory.md,High,No
PHASE 1/PHASE 1.B/Phase1B_Opportunity_Analysis.md,Phase1B_Opportunity_Analysis.md,md,5802,e10d76b80c78554ff7e2ea75f3b263bfe82333c54418e7f794d249610f8fe130,Phase 1B,Multi-concept,Methodology/SOP,Supporting/non-decision artifact,ED-17,,PHASE 1/PHASE 1.B/Phase1B_Opportunity_Analysis.md,High,No
PHASE 1/PHASE 1.B/Phase1B_Opportunity_Analysis.zip,Phase1B_Opportunity_Analysis.zip,zip,743098,67d556082774dd9223e05d99f6b64eac045d7cc52ae9b60c403bc643a8b15dab,Phase 1B,Multi-concept,Convenience/archive package,Convenience/context only; non-canonical container,,,Normal files listed in 03_DUPLICATE_REPORT.md,High,Yes — convenience archive retention/version policy
PHASE 1/PHASE 1.B/Phase1B_Opportunity_Analysis_By_Claude.pdf,Phase1B_Opportunity_Analysis_By_Claude.pdf,pdf,1484584,8e53b914163d8e2685d9edda7422e4c1ac1a01230e60e3a100a0e7ef514dd52c,Phase 1B,Multi-concept,Phase report/supporting deliverable,Supporting/non-decision artifact,,,PHASE 1/PHASE 1.B/Phase1B_Opportunity_Analysis_By_Claude.pdf,Medium,"No, unless used for a project decision"
PHASE 1/PHASE 1B.5/Phase1B5_Memory.md,Phase1B5_Memory.md,md,5302,d200473fd85a3cc910e3532bb2be662e0fcbdeab363fe988a948fd81d129c537,Phase 1B.5,Multi-concept,Phase memory,Supporting/non-decision artifact,ED-15,,PHASE 1/PHASE 1B.5/Phase1B5_Memory.md,High,No
PHASE 1/PHASE 1B.5/Phase1B5_Opportunity_Portfolio_Optimization.md,Phase1B5_Opportunity_Portfolio_Optimization.md,md,6431,305f0f568081ad8a01affc02d252a681f84abde5c23c2a9421fb69369ecc5540,Phase 1B.5,Multi-concept,Methodology/SOP,Supporting/non-decision artifact,ED-03,,PHASE 1/PHASE 1B.5/Phase1B5_Opportunity_Portfolio_Optimization.md,High,No
PHASE 1/PHASE 1B.5/Phase1B5_Portfolio_Optimization_By_Claude.pdf,Phase1B5_Portfolio_Optimization_By_Claude.pdf,pdf,582050,25130fe434ba2962de3ca241374d9823acced92b088ec6562a77140b80551809,Phase 1B.5,Multi-concept,Phase report/supporting deliverable,Supporting/non-decision artifact,,,PHASE 1/PHASE 1B.5/Phase1B5_Portfolio_Optimization_By_Claude.pdf,Medium,"No, unless used for a project decision"
PHASE 1/PHASE 1C/5 IDEA ABSTRACT/Microcontroller_Project_Abstract_Proposal_5_Ideas.pdf,Microcontroller_Project_Abstract_Proposal_5_Ideas.pdf,pdf,27986,0d0c8ba61f0c5b2ea5ac243a382f1a1ffdb1e75ed27d8f2b1f6fc8b971afd82e,Phase 1C,Multi-concept,Phase report/supporting deliverable,Level 9 — Phase 1C synthesis/dossier,,,PHASE 1/PHASE 1C/5 IDEA ABSTRACT/Microcontroller_Project_Abstract_Proposal_5_Ideas.pdf,Medium,"No, unless used for a project decision"
PHASE 1/PHASE 1C/5 IDEA ABSTRACT/Microcontroller_Project_Idea_Abstracts 2.0.pdf,Microcontroller_Project_Idea_Abstracts 2.0.pdf,pdf,25856,9d3f9364213e055715d85c85cf09c1609190c2c32918b60fcfe54f336f4fb8ec,Phase 1C,Multi-concept,Phase report/supporting deliverable,Level 9 — Phase 1C synthesis/dossier,,,PHASE 1/PHASE 1C/5 IDEA ABSTRACT/Microcontroller_Project_Idea_Abstracts 2.0.pdf,Medium,"No, unless used for a project decision"
PHASE 1/PHASE 1C/5 IDEA ABSTRACT/Microcontroller_Project_Idea_Abstracts.pdf,Microcontroller_Project_Idea_Abstracts.pdf,pdf,24352,8145ccd58cad7eadb15d9f0eb51c3e833cfbe2afe7eff9a174666118752f0874,Phase 1C,Multi-concept,Phase report/supporting deliverable,Level 9 — Phase 1C synthesis/dossier,,,PHASE 1/PHASE 1C/5 IDEA ABSTRACT/Microcontroller_Project_Idea_Abstracts.pdf,Medium,"No, unless used for a project decision"
PHASE 1/PHASE 1C/INDEPTH OF EACH FIVE IDEA/Document_1_OpenBraille_Concept_Dossier.docx,Document_1_OpenBraille_Concept_Dossier.docx,docx,38405,ac21af2a892f319e0b28d4d7314f4561c5aebad5291343c34d777beb933106ea,Phase 1C,OpenBraille,Concept dossier,Level 9 — Phase 1C synthesis/dossier,,,PHASE 1/PHASE 1C/INDEPTH OF EACH FIVE IDEA/Document_1_OpenBraille_Concept_Dossier.docx,High,No
PHASE 1/PHASE 1C/INDEPTH OF EACH FIVE IDEA/Document_2_VibeGuard_Concept_Dossier.docx,Document_2_VibeGuard_Concept_Dossier.docx,docx,38619,8a3c40cdc9ec899934ca9a37b05f9c0df22b583cd3ee259ebc81c1da9f0a0ae7,Phase 1C,VibeGuard,Concept dossier,Level 9 — Phase 1C synthesis/dossier,,,PHASE 1/PHASE 1C/INDEPTH OF EACH FIVE IDEA/Document_2_VibeGuard_Concept_Dossier.docx,High,No
PHASE 1/PHASE 1C/INDEPTH OF EACH FIVE IDEA/Document_3_TrueMoist_Concept_Dossier.docx,Document_3_TrueMoist_Concept_Dossier.docx,docx,38768,ca5cedfdfac5157b328aa865433a172d8af82a44d2dbf8b015c8c217fa6f85a2,Phase 1C,TrueMoist,Concept dossier,Level 9 — Phase 1C synthesis/dossier,,,PHASE 1/PHASE 1C/INDEPTH OF EACH FIVE IDEA/Document_3_TrueMoist_Concept_Dossier.docx,High,No
PHASE 1/PHASE 1C/INDEPTH OF EACH FIVE IDEA/Document_4_TrustLatch_Concept_Dossier.docx,Document_4_TrustLatch_Concept_Dossier.docx,docx,39031,f9a4184850435aba3ec26e480e802d1ba39f17037f0f368520a625c6f8e84f78,Phase 1C,TrustLatch (deferred),Concept dossier,Level 9 — Phase 1C synthesis/dossier,ED-20,,PHASE 1/PHASE 1C/INDEPTH OF EACH FIVE IDEA/Document_4_TrustLatch_Concept_Dossier.docx,High,No
PHASE 1/PHASE 1C/OTHERS IDEA FORMAT/POOJA PROJECT.pdf,POOJA PROJECT.pdf,pdf,98813,70a6446354f634cd7501e883e954bcba8f292a6bb91d406713d30c72b9be977d,Phase 1C,Multi-concept,Phase report/supporting deliverable,Level 9 — Phase 1C synthesis/dossier,,,PHASE 1/PHASE 1C/OTHERS IDEA FORMAT/POOJA PROJECT.pdf,Medium,"No, unless used for a project decision"
PHASE 1/PHASE 1C/OTHERS IDEA FORMAT/Patent Potential of Student Projects.docx,Patent Potential of Student Projects.docx,docx,2998348,2156803ab9ac9a253fc6e8860c7788d9891af782fcd52e7a9c64249115cf0273,Phase 1C,Multi-concept,Supporting project document,Supporting/non-decision artifact,,,PHASE 1/PHASE 1C/OTHERS IDEA FORMAT/Patent Potential of Student Projects.docx,High,No
PHASE 1/PHASE 1C/OTHERS IDEA FORMAT/USB_Powered_Secure_File_Transfer_Authentication_Abstract.pdf,USB_Powered_Secure_File_Transfer_Authentication_Abstract.pdf,pdf,2399,ce5b8e3c904a82066e0718abc0e49c6583c5ec37022cc8d4e59cdefb202c526e,Phase 1C,Multi-concept,Phase report/supporting deliverable,Level 9 — Phase 1C synthesis/dossier,,,PHASE 1/PHASE 1C/OTHERS IDEA FORMAT/USB_Powered_Secure_File_Transfer_Authentication_Abstract.pdf,Medium,"No, unless used for a project decision"
PHASE 1/PHASE 1C/OTHERS IDEA FORMAT/USB_Powered_Smart_Anti_Theft_System_Abstract.pdf,USB_Powered_Smart_Anti_Theft_System_Abstract.pdf,pdf,2424,6d5a03b4afbec01258f767ae31c592653ce6e5da09a29c62b5e8ec4841e5c5b3,Phase 1C,Multi-concept,Phase report/supporting deliverable,Level 9 — Phase 1C synthesis/dossier,,,PHASE 1/PHASE 1C/OTHERS IDEA FORMAT/USB_Powered_Smart_Anti_Theft_System_Abstract.pdf,Medium,"No, unless used for a project decision"
PHASE 1/PHASE 1C/OTHERS IDEA FORMAT/USB_Powered_Smart_Cabinet_Abstract.pdf,USB_Powered_Smart_Cabinet_Abstract.pdf,pdf,2553,97d240350257e89ad533ef3067c7bf41e18362e01f1d43823eb73e68f9049d17,Phase 1C,Multi-concept,Phase report/supporting deliverable,Level 9 — Phase 1C synthesis/dossier,,,PHASE 1/PHASE 1C/OTHERS IDEA FORMAT/USB_Powered_Smart_Cabinet_Abstract.pdf,Medium,"No, unless used for a project decision"
PHASE 1/PHASE 1C/Phase1C.md,Phase1C.md,md,3009,8e41493ddbc8b8b3c3ad8a00995b6ae3f8a5645351f8086a6b8ded92623853e4,Phase 1C,Multi-concept,Methodology/SOP,Level 9 — Phase 1C synthesis/dossier,ED-09,,PHASE 1/PHASE 1C/Phase1C.md,High,No
PHASE 1/PHASE 1C/Phase1C_Concept_Synthesis.pdf,Phase1C_Concept_Synthesis.pdf,pdf,641952,4f117f1a7bc0fb5b4ec9e450036566aa5198a08e84a451ad2e7d2dbc8636b084,Phase 1C,Multi-concept,Phase report/supporting deliverable,Level 9 — Phase 1C synthesis/dossier,,,PHASE 1/PHASE 1C/Phase1C_Concept_Synthesis.pdf,Medium,"No, unless used for a project decision"
PHASE 1/PHASE 1C/Phase1C_Memory.md,Phase1C_Memory.md,md,3390,e3b320245bc20d4312edc22b62fc9584059111e8fd38442277a3e5544ae019c1,Phase 1C,Multi-concept,Phase memory,Level 9 — Phase 1C synthesis/dossier,ED-18,,PHASE 1/PHASE 1C/Phase1C_Memory.md,High,No
PHASE 1/PHASE 1C/minimalist_project_proposal.pdf,minimalist_project_proposal.pdf,pdf,82574,19d4198bb4fafc2fbd299a68517551c58e52d319a6c84c4df55c6a41246f44e0,Phase 1C,Multi-concept,Phase report/supporting deliverable,Level 9 — Phase 1C synthesis/dossier,,,PHASE 1/PHASE 1C/minimalist_project_proposal.pdf,Medium,"No, unless used for a project decision"
PHASE 1/PHASE 1C/project_proposal_booklet.pdf,project_proposal_booklet.pdf,pdf,666060,c15f75f4ce0ab6cf6bca5ad7bb1b3c12a4c1e4bfdf662886fd168ba78d67c203,Phase 1C,Multi-concept,Phase report/supporting deliverable,Level 9 — Phase 1C synthesis/dossier,,,PHASE 1/PHASE 1C/project_proposal_booklet.pdf,Medium,"No, unless used for a project decision"
PHASE 1/PHASE 1C/visual explanation of the 5 ideas/11 ideas.html,11 ideas.html,html,68141,bd36812bff46105a8f6f9b6a38bbc93688b8e3cd2e9146456481b71c880f766d,Phase 1C,Multi-concept,Concept visualization,Supporting/non-decision artifact,,,PHASE 1/PHASE 1C/visual explanation of the 5 ideas/11 ideas.html,High,No
PHASE 1/PHASE 1C/visual explanation of the 5 ideas/top 5.html,top 5.html,html,43688,a01c1706657b1a5abc76ec22e8e108a2d534608cda5f824fe656f257195d4192,Phase 1C,Multi-concept,Concept visualization,Supporting/non-decision artifact,,,PHASE 1/PHASE 1C/visual explanation of the 5 ideas/top 5.html,High,No
PHASE 2/2_Sop.md,2_Sop.md,md,6177,c7d7d805d41313dee1dce65d9323c95075a8cde8d61ff2bfce3700510c41dd54,Phase 2,Repository-wide/none,Methodology/SOP,Supporting/non-decision artifact,,,PHASE 2/2_Sop.md,High,No
PHASE 2/Phase2_DeepResearch_Prompt_v2.md,Phase2_DeepResearch_Prompt_v2.md,md,8965,372d5ccbc23bd7b8e444fb6071aea4e4760397b5c1a360201d288609b1efcefd,Phase 2,Multi-concept,AI research/synthesis prompt,Supporting/non-decision artifact,,,PHASE 2/Phase2_DeepResearch_Prompt_v2.md,High,No
PHASE 2/Phase2_Memory.md,Phase2_Memory.md,md,7820,973519f45bc075c296d4302b94933288496bd9bc12fae708aac1fb7020158ce8,Phase 2,Multi-concept,Phase memory,Level 8 — Phase 2 report/memory,ED-10,,PHASE 2/Phase2_Memory.md,High,No
PHASE 2/Phase2_Report From Claude.pdf,Phase2_Report From Claude.pdf,pdf,488517,ab93da2c1ad6a9e22678e59da64a8992e4275ac4b01bad1061995dd9a5bf4f04,Phase 2,Multi-concept,Phase report/supporting deliverable,Level 8 — Phase 2 report/memory,,CF-01,PHASE 2/Phase2_Report by CLaude.md,High,Yes — cross-format scope/equivalence review
PHASE 2/Phase2_Report by CLaude.md,Phase2_Report by CLaude.md,md,44493,783729d0e07e725236db5296dae8504ce782c294b8c61cfab40ea172cfa6943e,Phase 2,Multi-concept,Phase report/supporting deliverable,Level 8 — Phase 2 report/memory,ED-06,CF-01,PHASE 2/Phase2_Report by CLaude.md,High,Yes — cross-format scope/equivalence review
PHASE 2/Phase2_docs.zip,Phase2_docs.zip,zip,20668,5b4156e64afaf59c1cc8788ae2c02cbebf8e2c003343dd8c56544219f1377fb6,Phase 2,Multi-concept,Convenience/archive package,Convenience/context only; non-canonical container,,,Normal files listed in 03_DUPLICATE_REPORT.md,High,Yes — convenience archive retention/version policy
PHASE 2/RESEARCH DOCS/CHATGT Research on Patent.docx,CHATGT Research on Patent.docx,docx,27850,61188e3fc06ca9ab2ddd8c196d217f10a59e077fe9b32687e2c0920d486501d5,Phase 2,Multi-concept,Raw independent research,Level 10 — raw research evidence only,,,PHASE 2/RESEARCH DOCS/CHATGT Research on Patent.docx,Medium,"No, unless used for a project decision"
PHASE 2/RESEARCH DOCS/Gemini Reearch on phase 2.docx,Gemini Reearch on phase 2.docx,docx,3011880,5af919473e667c9bae7abbdfc5f98067472f40beb5a3e5f1c793a0f12e4d0f53,Phase 2,Repository-wide/none,Raw independent research,Level 10 — raw research evidence only,,,PHASE 2/RESEARCH DOCS/Gemini Reearch on phase 2.docx,Medium,"No, unless used for a project decision"
PHASE 2/RESEARCH DOCS/Kimi Patent Research.pdf,Kimi Patent Research.pdf,pdf,1472114,33f4539a14653b55c0b73e0fbcd140827e2131ed9c3ca5d9bc896d4553f4a904,Phase 2,Multi-concept,Raw independent research,Level 10 — raw research evidence only,,,PHASE 2/RESEARCH DOCS/Kimi Patent Research.pdf,Medium,"No, unless used for a project decision"
PHASE 2/RESEARCH DOCS/QWen Research on Patent.pdf,QWen Research on Patent.pdf,pdf,752520,75d736454cf7362a31e9ae1e2695a7bd793ab98187f2ad51ba9dc44f0d4473a7,Phase 2,Multi-concept,Raw independent research,Level 10 — raw research evidence only,,CF-02,Undetermined pending manual comparison (PDF is more complete),Medium,Yes — cross-format scope/equivalence review
PHASE 2/RESEARCH DOCS/Qwens Research on Phase 2.md,Qwens Research on Phase 2.md,md,92668,5593a0581c350814e5567357effb2b1948cd3046a67bf52e00ff7495b9c0afe8,Phase 2,Repository-wide/none,Raw independent research,Level 10 — raw research evidence only,,CF-02,Undetermined pending manual comparison (PDF is more complete),Medium,Yes — cross-format scope/equivalence review
PHASE 3/Engineering_Design_Review.md,Engineering_Design_Review.md,md,31205,46f017501ac3ff9ebd6c1fb1e5ee8c068c22ddb08ae204c5609f2b759090295e,Phase 3,Repository-wide/none,Engineering Design Review,Level 1 — Engineering Design Review,ED-04,,PHASE 3/Engineering_Design_Review.md,High,No
PHASE 3/PHASE 3A-Engineering Landscape Discovery/Claudes report on the research Phases 3a.pdf,Claudes report on the research Phases 3a.pdf,pdf,792034,7d0202fb62476a0212e594af473ad8d796eecd853e53e7f0952de90908cec611,Phase 3A,Repository-wide/none,Raw independent research,Level 10 — raw research evidence only,ED-08,,PHASE 3/PHASE 3A-Engineering Landscape Discovery/Claudes report on the research Phases 3a.pdf,Medium,"No, unless used for a project decision"
PHASE 3/PHASE 3A-Engineering Landscape Discovery/Geminis Research On Phase 3A.docx,Geminis Research On Phase 3A.docx,docx,53060,6d380794c7b52664324a1e4e39dac49f40f50ad269391cbe1f6135175048b944,Phase 3A,Repository-wide/none,Raw independent research,Level 10 — raw research evidence only,,,PHASE 3/PHASE 3A-Engineering Landscape Discovery/Geminis Research On Phase 3A.docx,Medium,"No, unless used for a project decision"
PHASE 3/PHASE 3A-Engineering Landscape Discovery/MISTRAL RESEAARCH ON phase 3a.md,MISTRAL RESEAARCH ON phase 3a.md,md,122129,ae11e6b64bed09dcde373a21849085dd929a96f045d8a2362d4f07d58daed5c6,Phase 3A,Repository-wide/none,Raw independent research,Level 10 — raw research evidence only,,,PHASE 3/PHASE 3A-Engineering Landscape Discovery/MISTRAL RESEAARCH ON phase 3a.md,High,No
PHASE 3/PHASE 3A-Engineering Landscape Discovery/Perplexity Research on Phase 3A.pdf,Perplexity Research on Phase 3A.pdf,pdf,905522,a56c84e5ca354f3e1451fa98cd49d7184247c95b2b1ddf5b7e04a24bd954d19b,Phase 3A,Repository-wide/none,Raw independent research,Level 10 — raw research evidence only,,,PHASE 3/PHASE 3A-Engineering Landscape Discovery/Perplexity Research on Phase 3A.pdf,Medium,"No, unless used for a project decision"
PHASE 3/PHASE 3A-Engineering Landscape Discovery/Phase3A_MEMORY.md,Phase3A_MEMORY.md,md,8898,acd3b4178143ca918ed4cce43d3d853acc994c0178dc8efdc406fb014e1ec997,Phase 3A,Multi-concept,Phase memory,Level 7 — Phase 3A report/memory,ED-12,,PHASE 3/PHASE 3A-Engineering Landscape Discovery/Phase3A_MEMORY.md,High,No
PHASE 3/PHASE 3A-Engineering Landscape Discovery/Qwen Research on Phase 3A.md,Qwen Research on Phase 3A.md,md,63435,501782f664994ad0cfdeb72f16a975c2abe3a87ee4c456375a703f426437c99b,Phase 3A,Repository-wide/none,Raw independent research,Level 10 — raw research evidence only,,,PHASE 3/PHASE 3A-Engineering Landscape Discovery/Qwen Research on Phase 3A.md,High,No
PHASE 3/PHASE 3A-Engineering Landscape Discovery/phase3B_report_and_summary.zip,phase3B_report_and_summary.zip,zip,522853,9d0593bb50717c290ca9c36d135ffc1aebfb70a48d2b058be4c8b421af44ae21,Phase 3B,Multi-concept,Convenience/archive package,Convenience/context only; non-canonical container,,,Normal files listed in 03_DUPLICATE_REPORT.md,High,Yes — convenience archive retention/version policy
PHASE 3/PHASE 3B-Engineering Feasibility Analysis/Gemini Research on Phase 3B.docx,Gemini Research on Phase 3B.docx,docx,3012247,94e1e8e81c3f79f3f426086677841b1b4c2c32da8b50710e080bd0a27b9e2906,Phase 3B,Repository-wide/none,Raw independent research,Level 10 — raw research evidence only,,,PHASE 3/PHASE 3B-Engineering Feasibility Analysis/Gemini Research on Phase 3B.docx,Medium,"No, unless used for a project decision"
PHASE 3/PHASE 3B-Engineering Feasibility Analysis/Mistral researon on Phase 3B.md,Mistral researon on Phase 3B.md,md,81611,254d0b0a0df0cdab2fecb7ef65148474faff4f16c440fe4e76d0ada53cb6dc11,Phase 3B,Repository-wide/none,Raw independent research,Level 10 — raw research evidence only,,,PHASE 3/PHASE 3B-Engineering Feasibility Analysis/Mistral researon on Phase 3B.md,High,No
PHASE 3/PHASE 3B-Engineering Feasibility Analysis/Phase3B_DeepResearch_Prompt.md,Phase3B_DeepResearch_Prompt.md,md,11471,2d0a79d6fe7e24bf1cc4c1d4b4a9e2c0cd3c8cead10ad0323b63709eec2811e6,Phase 3B,Multi-concept,AI research/synthesis prompt,Supporting/non-decision artifact,,,PHASE 3/PHASE 3B-Engineering Feasibility Analysis/Phase3B_DeepResearch_Prompt.md,High,No
PHASE 3/PHASE 3B-Engineering Feasibility Analysis/Phase3B_MEMORY.md,Phase3B_MEMORY.md,md,18836,7b6532c779867e9d6064473de4ba1b4799a0c385361cf27dc4616888fb0ac7ad,Phase 3B,Multi-concept,Phase memory,Level 6 — Phase 3B report/memory,ED-07,,PHASE 3/PHASE 3B-Engineering Feasibility Analysis/Phase3B_MEMORY.md,High,No
PHASE 3/PHASE 3B-Engineering Feasibility Analysis/Phase3B_Report_by_Claude.md,Phase3B_Report_by_Claude.md,md,83718,14c19ac85b56e4e27da03de534a2a574ab7220d90005b4a7a0afb868f6390478,Phase 3B,Multi-concept,Phase report/supporting deliverable,Level 6 — Phase 3B report/memory,ED-01,,PHASE 3/PHASE 3B-Engineering Feasibility Analysis/Phase3B_Report_by_Claude.md,High,No
PHASE 3/PHASE 3B-Engineering Feasibility Analysis/Phase3B_mem_and_report.zip,Phase3B_mem_and_report.zip,zip,35058,b4674075c434e818a3579f61f8746dd918ac06e316030e04fa3c9577a36eafb0,Phase 3B,Multi-concept,Convenience/archive package,Convenience/context only; non-canonical container,,,Normal files listed in 03_DUPLICATE_REPORT.md,High,Yes — convenience archive retention/version policy
PHASE 3/PHASE 3B-Engineering Feasibility Analysis/Project_mC_Phase3B_SOP.md,Project_mC_Phase3B_SOP.md,md,8028,6ce2ed40885038734faa75018a1caa16d89fcc7f18c7bf8249fe42453f36af4c,Phase 3B,Multi-concept,Methodology/SOP,Supporting/non-decision artifact,,,PHASE 3/PHASE 3B-Engineering Feasibility Analysis/Project_mC_Phase3B_SOP.md,High,No
PHASE 3/PHASE 3B-Engineering Feasibility Analysis/Qwen Rsearch on Phase 3B.pdf,Qwen Rsearch on Phase 3B.pdf,pdf,649615,7a8fbde6b8fab93e195deefa716fb3f3724c369aa87deef27256be8fe8b45e1f,Phase 3B,Repository-wide/none,Raw independent research,Level 10 — raw research evidence only,,,PHASE 3/PHASE 3B-Engineering Feasibility Analysis/Qwen Rsearch on Phase 3B.pdf,Medium,"No, unless used for a project decision"
PHASE 3/PHASE 3B-Engineering Feasibility Analysis/perplexity_research_on_phase3B.md,perplexity_research_on_phase3B.md,md,49895,65a891eda465cab8f3d1d69e8320497dc8c05c5a2176c25d9c0cb81218f4b4d5,Phase 3B,Multi-concept,Raw independent research,Level 10 — raw research evidence only,,,PHASE 3/PHASE 3B-Engineering Feasibility Analysis/perplexity_research_on_phase3B.md,High,No
PHASE 3/PHASE 3C-Comparative Technical Evaluation/Phase3C_Retained_Portfolio_Closure_Memo.md,Phase3C_Retained_Portfolio_Closure_Memo.md,md,3149,3c6e6f568c06099251b4b71d4f35cf668ee23a40c8214c95e4a12fe36cf4845a,Phase 3C,Multi-concept,Approved portfolio closure memo,Level 3 — retained-portfolio closure memo,,,PHASE 3/PHASE 3C-Comparative Technical Evaluation/Phase3C_Retained_Portfolio_Closure_Memo.md,High,No
PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_ChatGPT_Final_Synthesis.md,Phase3C_TrueMoist_ChatGPT_Final_Synthesis.md,md,46897,6c71f1d618e0575d127b10f05e91d06ea4b1f0b8a2fe63e78d4022ee75234610,Phase 3C,TrueMoist,Final Phase 3C architecture/synthesis report,Level 4 — final Phase 3C architecture report,,,PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_ChatGPT_Final_Synthesis.md,High,No
PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_DeepResearch_Prompt.md,Phase3C_TrueMoist_DeepResearch_Prompt.md,md,28220,da66d2b9259a007d390b7fdc2766b9349bf88497cd60af3bc0c5e6855cddd08e,Phase 3C,TrueMoist,AI research/synthesis prompt,Supporting/non-decision artifact,,,PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_DeepResearch_Prompt.md,High,No
PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_Final_Synthesis_Prompt.md,Phase3C_TrueMoist_Final_Synthesis_Prompt.md,md,10637,144617f2efe8ef6db6122d00039fcc3566d8aab03649e003837eea5c0a60618e,Phase 3C,TrueMoist,AI research/synthesis prompt,Supporting/non-decision artifact,,,PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_Final_Synthesis_Prompt.md,High,No
PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_MEMORY_Final.md,Phase3C_TrueMoist_MEMORY_Final.md,md,5230,ba8264d74f37168e5de85a5d76adb354062dc5e47b692b12f76f73aac62c7377,Phase 3C,TrueMoist,Phase memory,Level 5 — Phase 3C memory,,,PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_MEMORY_Final.md,High,No
PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_PDR_Update_Patch.md,Phase3C_TrueMoist_PDR_Update_Patch.md,md,10210,f9b23506c0b78a76ac590fa7bb80911c1a416569eb17c41644b2cfd9b432a803,Phase 3C,TrueMoist,Historical PDR update patch,Supporting/non-decision artifact,,,PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_PDR_Update_Patch.md,High,No
PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_SOP.md,Phase3C_TrueMoist_SOP.md,md,18712,993caf1a05f3fdc3937efb634e2f2e467488e973eb71454db8e3c3f53d178d00,Phase 3C,TrueMoist,Methodology/SOP,Supporting/non-decision artifact,ED-11,,PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_SOP.md,High,No
PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Research/TrueMoist  3C Gemini REsearch.docx,TrueMoist  3C Gemini REsearch.docx,docx,138980,b0eab8009831f5b719bf9d20ad1f25e9bcc549fc260a078a5be2531dc86e5b24,Phase 3C,TrueMoist,Raw independent research,Level 10 — raw research evidence only,,,PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Research/TrueMoist  3C Gemini REsearch.docx,Medium,"No, unless used for a project decision"
PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Research/TrueMoist Phase 3C  Research By chatgpt.pdf,TrueMoist Phase 3C  Research By chatgpt.pdf,pdf,17994349,87ccbd3416f3f7bb58e544095a1e20560f9561ffe72db82f868d17bf942812e7,Phase 3C,TrueMoist,Raw independent research,Level 10 — raw research evidence only,,,PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Research/TrueMoist Phase 3C  Research By chatgpt.pdf,Medium,"No, unless used for a project decision"
PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Research/TrueMoist Phase 3C By Perplexity.md,TrueMoist Phase 3C By Perplexity.md,md,87503,caefe1da05e1963e0cd9c3916fc50d4c2e4b396006cdf39ebf8eee893f0c3187,Phase 3C,TrueMoist,Raw independent research,Level 10 — raw research evidence only,,,PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Research/TrueMoist Phase 3C By Perplexity.md,High,No
PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Research/phase-3c-truemoist-Research-Mistral.md,phase-3c-truemoist-Research-Mistral.md,md,19116,706d9ae47b256de0bb01d2836c3b24095b4109fd6c1011491aa88d32799fd1c5,Phase 3C,TrueMoist,Raw independent research,Level 10 — raw research evidence only,,,PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Research/phase-3c-truemoist-Research-Mistral.md,High,No
PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Claudes report for openbraille phase 3c.md,Claudes report for openbraille phase 3c.md,md,46126,0e6c40edc6fd79c17f6bcac8e6d1598217ff7cadbdbf721ea55e4c39d4d36aa8,Phase 3C,OpenBraille,Final Phase 3C architecture/synthesis report,Level 4 — final Phase 3C architecture report,,,PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Claudes report for openbraille phase 3c.md,High,No
PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Phase3C_OpenBraille_Claude_Synthesis_Prompt.md,Phase3C_OpenBraille_Claude_Synthesis_Prompt.md,md,17548,2cd7dbdabb86f93a69ebfc012a5518fdb814529999c44f68c4252a19f5b8cf04,Phase 3C,OpenBraille,AI research/synthesis prompt,Supporting/non-decision artifact,,,PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Phase3C_OpenBraille_Claude_Synthesis_Prompt.md,High,No
PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Phase3C_OpenBraille_DeepResearch_Prompt.md,Phase3C_OpenBraille_DeepResearch_Prompt.md,md,19686,a59b4743782e0e21e1472b28b116a1bf83a2ede098a28e8d5110a8ab1ce33e42,Phase 3C,OpenBraille,AI research/synthesis prompt,Supporting/non-decision artifact,,,PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Phase3C_OpenBraille_DeepResearch_Prompt.md,High,No
PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Phase3C_OpenBraille_Memory.md,Phase3C_OpenBraille_Memory.md,md,12364,5dad0e392cf9c64d7e8f29be09fadb70acde5b965b95744fa066b5f4b4fd30eb,Phase 3C,OpenBraille,Phase memory,Level 5 — Phase 3C memory,,,PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Phase3C_OpenBraille_Memory.md,High,No
PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Phase3C_OpenBraille_SOP.md,Phase3C_OpenBraille_SOP.md,md,4746,bfee5dc46675d77b318f4a0d4fe864d77a570a1150cc2676a5dd10103f214e50,Phase 3C,OpenBraille,Methodology/SOP,Supporting/non-decision artifact,,,PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Phase3C_OpenBraille_SOP.md,High,No
PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Researches/DEEpr research on phase 3c openbraille by chatgpt,DEEpr research on phase 3c openbraille by chatgpt,[none],151219,864e400d3b259157346319b53eb36868b28bf183fb6ac5a1efbcbb6315424e06,Phase 3C,OpenBraille,Failed/mis-scoped raw research (PDF without extension),Level 10 — raw research evidence only,,,PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Researches/DEEpr research on phase 3c openbraille by chatgpt,High,Yes — label as failed and restore .pdf extension
PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Researches/Perplexity research on phase 3C.docx,Perplexity research on phase 3C.docx,docx,534977,6350e11ac346e30fbb3ca252a40367e4394bfcf1cf9e1f2ad8c84fcf1bf3545d,Phase 3C,OpenBraille,Raw independent research,Level 10 — raw research evidence only,,,PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Researches/Perplexity research on phase 3C.docx,Medium,"No, unless used for a project decision"
PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Researches/gemini research on phase 3c.docx,gemini research on phase 3c.docx,docx,3059479,a1d2b01cdbaa412c79251ffec0b7fad9e606aa16609a664a88b6ebd8149b8b7c,Phase 3C,OpenBraille,Raw independent research,Level 10 — raw research evidence only,,,PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Researches/gemini research on phase 3c.docx,Medium,"No, unless used for a project decision"
PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Researches/mistral research on phase 3c.md,mistral research on phase 3c.md,md,75348,aff5ebe5ff1fedfc5cc52cb9ef52d6b742ea495ff5304eb5acedaa8ff7e21c83,Phase 3C,OpenBraille,Raw independent research,Level 10 — raw research evidence only,,,PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Researches/mistral research on phase 3c.md,High,No
PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Researches/qwen Research on phase 3C.md,qwen Research on phase 3C.md,md,45014,3416c5526a1c73e5b29acf0117d45b4a5ee86cc1391eb9a105ca6710d0048f2b,Phase 3C,OpenBraille,Raw independent research,Level 10 — raw research evidence only,,,PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Researches/qwen Research on phase 3C.md,High,No
PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/Phase3C_VibeGuard_DeepResearch_Prompt.md,Phase3C_VibeGuard_DeepResearch_Prompt.md,md,25491,af08518f2c65bc8a53ff2520775415d2fd7f3bd5da2fc7e37018ae96a0c412d6,Phase 3C,VibeGuard,AI research/synthesis prompt,Supporting/non-decision artifact,,,PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/Phase3C_VibeGuard_DeepResearch_Prompt.md,High,No
PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/Phase3C_VibeGuard_Memory.md,Phase3C_VibeGuard_Memory.md,md,9485,3d07fdb1b9b2c0c273dacf3b49650e2deb6fa72a36af38035c85118e3fd51960,Phase 3C,VibeGuard,Phase memory,Level 5 — Phase 3C memory,,,PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/Phase3C_VibeGuard_Memory.md,High,No
PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/claude_synthesis_prompt.md,claude_synthesis_prompt.md,md,16519,26b50889394442be4fb22e26fad74b6ca97c7e5765f330b92b241ff8e69c1a2e,Phase 3C,VibeGuard,AI research/synthesis prompt,Supporting/non-decision artifact,,CF-03,PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/claude_synthesis_prompt.md,High,Yes — cross-format scope/equivalence review
PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/claude_synthesis_prompt.mmd,claude_synthesis_prompt.mmd,mmd,16518,59ae97bd4407b3e18cb2fb9ac99abdeeaf9aa3fdc3f5cb5e6f8ea67f330da47e,Phase 3C,VibeGuard,AI research/synthesis prompt,Supporting/non-decision artifact,,CF-03,PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/claude_synthesis_prompt.md,High,Yes — cross-format scope/equivalence review
PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/research/Perplexity research on phase 3c.md,Perplexity research on phase 3c.md,md,46791,0b1a2ea090cbc3630e84f4c4902e307e72751ca531f85bfe473285f74f4df368,Phase 3C,VibeGuard,Raw independent research,Level 10 — raw research evidence only,,,PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/research/Perplexity research on phase 3c.md,High,No
PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/research/Phase3C_VibeGuard_Architecture_Report By Claude.md,Phase3C_VibeGuard_Architecture_Report By Claude.md,md,32541,d6a5f009d5c96bceb6cc0cb2f4d70817204e7346e7f6e7c21a5e86b457254573,Phase 3C,VibeGuard,Final Phase 3C architecture/synthesis report,Level 4 — final Phase 3C architecture report,,,PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/research/Phase3C_VibeGuard_Architecture_Report By Claude.md,High,No
PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/research/gemini research on phase 3c.docx,gemini research on phase 3c.docx,docx,3049401,39a249ed0b0c9d76b0372e558b04d47a837b6a1849848f84fa9bf88f1ade0921,Phase 3C,VibeGuard,Raw independent research,Level 10 — raw research evidence only,,,PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/research/gemini research on phase 3c.docx,Medium,"No, unless used for a project decision"
PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/research/mistral reserach on phase 3c.md,mistral reserach on phase 3c.md,md,53102,86efffd004de1dd811343d0d6def5c8955189f66aa56af244f6b5d2d4dacc355,Phase 3C,VibeGuard,Raw independent research,Level 10 — raw research evidence only,,,PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/research/mistral reserach on phase 3c.md,High,No
PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/research/qwens research on phase 3c.md,qwens research on phase 3c.md,md,42575,a16b18b36f221d2a3f4de53d65068de3bb20d253e0d550c60c7735b30ae19f4d,Phase 3C,VibeGuard,Raw independent research,Level 10 — raw research evidence only,,,PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/research/qwens research on phase 3c.md,High,No
PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/vibeguard_sop.md,vibeguard_sop.md,md,15737,e073729670896e004900fdb52c049819d78d4b597f7da08e62c54de1152f7e0c,Phase 3C,VibeGuard,Methodology/SOP,Supporting/non-decision artifact,,,PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/vibeguard_sop.md,High,No
PHASE 3/Phase3_DeepResearch_Prompt.md,Phase3_DeepResearch_Prompt.md,md,9989,4173379249d0dca88800c04432b71cf1184f958abf2809d72c023363cdd1449c,Phase 3,Multi-concept,AI research/synthesis prompt,Supporting/non-decision artifact,,,PHASE 3/Phase3_DeepResearch_Prompt.md,High,No
PROJECT_CONCEPT_CONTEXT.md,PROJECT_CONCEPT_CONTEXT.md,md,6646,f520cb5201e299fb0f9185bd2b79318229b898e5a8ad7822deb9a073e8f6cae4,Cross-phase governance,Multi-concept,Canonical concept context,Governance/context (outside numbered technical precedence),ED-19,,PROJECT_CONCEPT_CONTEXT.md,High,No
Phase3_SOP.md,Phase3_SOP.md,md,6227,3c3bfa374c40280be56adbd22f5ba7e07c3f38254557c0d1885da5708f6c53de,Phase 3,Multi-concept,Methodology/SOP,Supporting/non-decision artifact,,,Phase3_SOP.md,High,No
Project_mC_Decision_Register_v1.0.md.save,Project_mC_Decision_Register_v1.0.md.save,save,42548,2ecf77fbbba9966a7769a2e715034f6b9ff7362d7aa51261219ee118085d22d3,Cross-phase governance,Multi-concept,Project Decision Register,Historical/superseded Decision Register,ED-02,,Project_mC_Decision_Register_v1.0.md.save,High,Yes — ensure historical/superseded labeling
Project_mC_Decision_Register_v1.2.md,Project_mC_Decision_Register_v1.2.md,md,55963,ebdbbf8df5645fb41b238dc403d7160bbec78a5114b93237eea4ac098ef21d2e,Cross-phase governance,Multi-concept,Project Decision Register,Level 2 — latest Decision Register,,,Project_mC_Decision_Register_v1.2.md,High,No
README.md,README.md,md,13,77702c121156afe1be6cc6ef8ce1c61a0291b13b3aa7a2f2ef1f4d608025ec06,Repository-wide,Repository-wide/none,Repository landing page,Supporting/non-decision artifact,,,README.md,High,No
contexts.zip,contexts.zip,zip,3583134,29c21e888bc2ac1fb42514db91bff88a6a67bafde26a05ddc6933010ba3233f6,Phase 1A context package,Multi-concept,Convenience/archive package,Convenience/context only; non-canonical container,,,Normal Phase 1A files; embedded phase roadmap is historical,High,Yes — convenience archive retention/version policy
every sop and memory/MC_Project_PHASE_DOC.md,MC_Project_PHASE_DOC.md,md,6638,e7ebf127dac01b63c87713b14c0bd5cf2d4500e60581cc86f783abe92a525f98,Cross-phase/unclear,Multi-concept,Phase memory,Convenience/context only; non-canonical container,,,MC_Project_PHASE_DOC.md,High,Yes — stale status/version or structure snapshot
every sop and memory/Phase1A_Memory.md,Phase1A_Memory.md,md,4029,5a8943e1e556e1db0644cc7b75e2b4c8000b1a9506d673406c9c70cf7bb4a213,Phase 1A,Multi-concept,Phase memory,Convenience/context only; non-canonical container,ED-05,,PHASE 1/PHASE 1.A/Phase1A_Memory.md,High,Yes — convenience copy; do not treat as canonical
every sop and memory/Phase1A_Summary.md,Phase1A_Summary.md,md,2794,c52bed09fdfd1a860471bfc6d56cd41411f730362d12ee0348e07ad0939909c9,Phase 1A,Multi-concept,Phase memory,Convenience/context only; non-canonical container,ED-14,,PHASE 1/PHASE 1.A/Phase1A_Summary.md,High,Yes — convenience copy; do not treat as canonical
every sop and memory/Phase1B5_Memory.md,Phase1B5_Memory.md,md,5302,d200473fd85a3cc910e3532bb2be662e0fcbdeab363fe988a948fd81d129c537,Phase 1B.5,Multi-concept,Phase memory,Convenience/context only; non-canonical container,ED-15,,PHASE 1/PHASE 1B.5/Phase1B5_Memory.md,High,Yes — convenience copy; do not treat as canonical
every sop and memory/Phase1B5_Opportunity_Portfolio_Optimization.md,Phase1B5_Opportunity_Portfolio_Optimization.md,md,6431,305f0f568081ad8a01affc02d252a681f84abde5c23c2a9421fb69369ecc5540,Phase 1B.5,Multi-concept,Phase memory,Convenience/context only; non-canonical container,ED-03,,PHASE 1/PHASE 1B.5/Phase1B5_Opportunity_Portfolio_Optimization.md,High,Yes — convenience copy; do not treat as canonical
every sop and memory/Phase1B_Memory.md,Phase1B_Memory.md,md,3966,d58c91eead60c5abdb4e38c1e9b87c7449f4b3b68ccd7a23f5d4816fea16ff76,Phase 1B,Multi-concept,Phase memory,Convenience/context only; non-canonical container,ED-16,,PHASE 1/PHASE 1.B/Phase1B_Memory.md,High,Yes — convenience copy; do not treat as canonical
every sop and memory/Phase1B_Opportunity_Analysis.md,Phase1B_Opportunity_Analysis.md,md,5802,e10d76b80c78554ff7e2ea75f3b263bfe82333c54418e7f794d249610f8fe130,Phase 1B,Multi-concept,Phase memory,Convenience/context only; non-canonical container,ED-17,,PHASE 1/PHASE 1.B/Phase1B_Opportunity_Analysis.md,High,Yes — convenience copy; do not treat as canonical
every sop and memory/Phase1C.md,Phase1C.md,md,3009,8e41493ddbc8b8b3c3ad8a00995b6ae3f8a5645351f8086a6b8ded92623853e4,Phase 1C,Multi-concept,Phase memory,Convenience copy of Level 9 — Phase 1C synthesis/dossier,ED-09,,PHASE 1/PHASE 1C/Phase1C.md,High,Yes — convenience copy; do not treat as canonical
every sop and memory/Phase1C_Memory.md,Phase1C_Memory.md,md,3390,e3b320245bc20d4312edc22b62fc9584059111e8fd38442277a3e5544ae019c1,Phase 1C,Multi-concept,Phase memory,Convenience copy of Level 9 — Phase 1C synthesis/dossier,ED-18,,PHASE 1/PHASE 1C/Phase1C_Memory.md,High,Yes — convenience copy; do not treat as canonical
every sop and memory/every_sop_and memory_from phase 1A to 1C and whoel phase overview.zip,every_sop_and memory_from phase 1A to 1C and whoel phase overview.zip,zip,19018,cdc5acdda096d42498ba49d4bec9451e1cb8cfa5251d295a0412d0e4d9a83668,Cross-phase/unclear,Repository-wide/none,Convenience/archive package,Convenience/context only; non-canonical container,,,Normal files listed in 03_DUPLICATE_REPORT.md,High,Yes — convenience archive retention/version policy


---

## Source 14: `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Legacy_Repository_Audit/02_FILE_MANIFEST.pdf`

- Authority: `TIER_1`
- Treatment: `CORE_NARRATIVE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `904d6fb0000cede691fe9b28a897db5e44413e95a2ff5ce6ffcc62bee88fd1af`

# Source Extraction

- Chapter: `01` — Project Mandate, Requirements and Governance
- Authority tier: `TIER_1`
- Manual treatment: `CORE_NARRATIVE`
- Original source: `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Legacy_Repository_Audit/02_FILE_MANIFEST.pdf`
- Current SHA-256: `904d6fb0000cede691fe9b28a897db5e44413e95a2ff5ce6ffcc62bee88fd1af`
- Extraction method: `PDFTOTEXT_LAYOUT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

02_FILE_MANIFEST

current_path
.gitignore
AGENTS.md
COPY PASTE FOLDER/Claudes report on the research Phases 3a.pdf
COPY PASTE FOLDER/Document_4_TrustLatch_Concept_Dossier.docx
COPY PASTE FOLDER/Engineering_Design_Review.md
COPY PASTE FOLDER/MC_Project_PHASE_DOC.md
COPY PASTE FOLDER/PROJECT_CONCEPT_CONTEXT.md
COPY PASTE FOLDER/Phase2_Memory.md
COPY PASTE FOLDER/Phase2_Report by CLaude.md
COPY PASTE FOLDER/Phase3A_MEMORY.md
COPY PASTE FOLDER/Phase3B_MEMORY.md
COPY PASTE FOLDER/Phase3B_Report_by_Claude.md
COPY PASTE FOLDER/Phase3C_TrueMoist_SOP.md
COPY PASTE FOLDER/Project_mC_Decision_Register_v1.0.md
CURRENT_FOLDER_STRUCTURE.txt
MC_Project_PHASE_DOC.md
PHASE 1/PHASE 1.A/Phase1A_Memory.md
PHASE 1/PHASE 1.A/Phase1A_Summary.md
PHASE 1/PHASE 1.A/RESEARCHS/CHATGPT DEEP RESEARCH.md
PHASE 1/PHASE 1.A/RESEARCHS/GEMINI DEEP RESEARCH.docx
PHASE 1/PHASE 1.A/RESEARCHS/KIMI DEEP RESEARCH.docx
PHASE 1/PHASE 1.A/RESEARCHS/QWEN AI DEEP RESEARCH.pdf
PHASE 1/PHASE 1.B/Phase1B_Memory.md
PHASE 1/PHASE 1.B/Phase1B_Opportunity_Analysis.md
PHASE 1/PHASE 1.B/Phase1B_Opportunity_Analysis.zip
PHASE 1/PHASE 1.B/Phase1B_Opportunity_Analysis_By_Claude.pdf
PHASE 1/PHASE 1B.5/Phase1B5_Memory.md
PHASE 1/PHASE 1B.5/Phase1B5_Opportunity_Portfolio_Optimization.md
PHASE 1/PHASE 1B.5/Phase1B5_Portfolio_Optimization_By_Claude.pdf
PHASE 1/PHASE 1C/5 IDEA ABSTRACT/Microcontroller_Project_Abstract_Proposal_5_Ideas.pdf
PHASE 1/PHASE 1C/5 IDEA ABSTRACT/Microcontroller_Project_Idea_Abstracts 2.0.pdf
PHASE 1/PHASE 1C/5 IDEA ABSTRACT/Microcontroller_Project_Idea_Abstracts.pdf
PHASE 1/PHASE 1C/INDEPTH OF EACH FIVE IDEA/Document_1_OpenBraille_Concept_Dossier.docx
PHASE 1/PHASE 1C/INDEPTH OF EACH FIVE IDEA/Document_2_VibeGuard_Concept_Dossier.docx
PHASE 1/PHASE 1C/INDEPTH OF EACH FIVE IDEA/Document_3_TrueMoist_Concept_Dossier.docx
PHASE 1/PHASE 1C/INDEPTH OF EACH FIVE IDEA/Document_4_TrustLatch_Concept_Dossier.docx
PHASE 1/PHASE 1C/OTHERS IDEA FORMAT/POOJA PROJECT.pdf
PHASE 1/PHASE 1C/OTHERS IDEA FORMAT/Patent Potential of Student Projects.docx
PHASE 1/PHASE 1C/OTHERS IDEA FORMAT/USB_Powered_Secure_File_Transfer_Authentication_Abstract.pdf
PHASE 1/PHASE 1C/OTHERS IDEA FORMAT/USB_Powered_Smart_Anti_Theft_System_Abstract.pdf
PHASE 1/PHASE 1C/OTHERS IDEA FORMAT/USB_Powered_Smart_Cabinet_Abstract.pdf
PHASE 1/PHASE 1C/Phase1C.md
PHASE 1/PHASE 1C/Phase1C_Concept_Synthesis.pdf
PHASE 1/PHASE 1C/Phase1C_Memory.md
PHASE 1/PHASE 1C/minimalist_project_proposal.pdf
PHASE 1/PHASE 1C/project_proposal_booklet.pdf
PHASE 1/PHASE 1C/visual explanation of the 5 ideas/11 ideas.html
PHASE 1/PHASE 1C/visual explanation of the 5 ideas/top 5.html
PHASE 2/2_Sop.md
PHASE 2/Phase2_DeepResearch_Prompt_v2.md
PHASE 2/Phase2_Memory.md
PHASE 2/Phase2_Report From Claude.pdf

                                          Page 1

                                       02_FILE_MANIFEST

PHASE 2/Phase2_Report by CLaude.md
PHASE 2/Phase2_docs.zip
PHASE 2/RESEARCH DOCS/CHATGT Research on Patent.docx
PHASE 2/RESEARCH DOCS/Gemini Reearch on phase 2.docx
PHASE 2/RESEARCH DOCS/Kimi Patent Research.pdf
PHASE 2/RESEARCH DOCS/QWen Research on Patent.pdf
PHASE 2/RESEARCH DOCS/Qwens Research on Phase 2.md
PHASE 3/Engineering_Design_Review.md
PHASE 3/PHASE 3A-Engineering Landscape Discovery/Claudes report on the research Phases 3a.pdf
PHASE 3/PHASE 3A-Engineering Landscape Discovery/Geminis Research On Phase 3A.docx
PHASE 3/PHASE 3A-Engineering Landscape Discovery/MISTRAL RESEAARCH ON phase 3a.md
PHASE 3/PHASE 3A-Engineering Landscape Discovery/Perplexity Research on Phase 3A.pdf
PHASE 3/PHASE 3A-Engineering Landscape Discovery/Phase3A_MEMORY.md
PHASE 3/PHASE 3A-Engineering Landscape Discovery/Qwen Research on Phase 3A.md
PHASE 3/PHASE 3A-Engineering Landscape Discovery/phase3B_report_and_summary.zip
PHASE 3/PHASE 3B-Engineering Feasibility Analysis/Gemini Research on Phase 3B.docx
PHASE 3/PHASE 3B-Engineering Feasibility Analysis/Mistral researon on Phase 3B.md
PHASE 3/PHASE 3B-Engineering Feasibility Analysis/Phase3B_DeepResearch_Prompt.md
PHASE 3/PHASE 3B-Engineering Feasibility Analysis/Phase3B_MEMORY.md
PHASE 3/PHASE 3B-Engineering Feasibility Analysis/Phase3B_Report_by_Claude.md
PHASE 3/PHASE 3B-Engineering Feasibility Analysis/Phase3B_mem_and_report.zip
PHASE 3/PHASE 3B-Engineering Feasibility Analysis/Project_mC_Phase3B_SOP.md
PHASE 3/PHASE 3B-Engineering Feasibility Analysis/Qwen Rsearch on Phase 3B.pdf
PHASE 3/PHASE 3B-Engineering Feasibility Analysis/perplexity_research_on_phase3B.md
PHASE 3/PHASE 3C-Comparative Technical Evaluation/Phase3C_Retained_Portfolio_Closure_Memo.md
PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_ChatGPT_Final_Synthesis.md
PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_DeepResearch_Prompt.md
PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_Final_Synthesis_Prompt.md
PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_MEMORY_Final.md
PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_PDR_Update_Patch.md
PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_SOP.md
PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Research/TrueMoist 3C Gemini REsearch.docx
PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Research/TrueMoist Phase 3C Research By chatgpt.p
PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Research/TrueMoist Phase 3C By Perplexity.md
PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Research/phase-3c-truemoist-Research-Mistral.md
PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Claudes report for openbraille phase 3c.md
PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Phase3C_OpenBraille_Claude_Synthesis_Prompt.m
PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Phase3C_OpenBraille_DeepResearch_Prompt.md
PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Phase3C_OpenBraille_Memory.md
PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Phase3C_OpenBraille_SOP.md
PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Researches/DEEpr research on phase 3c openbraille
PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Researches/Perplexity research on phase 3C.docx
PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Researches/gemini research on phase 3c.docx
PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Researches/mistral research on phase 3c.md
PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Researches/qwen Research on phase 3C.md
PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/Phase3C_VibeGuard_DeepResearch_Prompt.md
PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/Phase3C_VibeGuard_Memory.md
PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/claude_synthesis_prompt.md
PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/claude_synthesis_prompt.mmd
PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/research/Perplexity research on phase 3c.md
PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/research/Phase3C_VibeGuard_Architecture_Report B
PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/research/gemini research on phase 3c.docx
PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/research/mistral reserach on phase 3c.md

                                             Page 2

                                      02_FILE_MANIFEST

PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/research/qwens research on phase 3c.md
PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/vibeguard_sop.md
PHASE 3/Phase3_DeepResearch_Prompt.md
PROJECT_CONCEPT_CONTEXT.md
Phase3_SOP.md
Project_mC_Decision_Register_v1.0.md.save
Project_mC_Decision_Register_v1.2.md
README.md
contexts.zip
every sop and memory/MC_Project_PHASE_DOC.md
every sop and memory/Phase1A_Memory.md
every sop and memory/Phase1A_Summary.md
every sop and memory/Phase1B5_Memory.md
every sop and memory/Phase1B5_Opportunity_Portfolio_Optimization.md
every sop and memory/Phase1B_Memory.md
every sop and memory/Phase1B_Opportunity_Analysis.md
every sop and memory/Phase1C.md
every sop and memory/Phase1C_Memory.md
every sop and memory/every_sop_and memory_from phase 1A to 1C and whoel phase overview.zip


                                             Page 3

                                       02_FILE_MANIFEST

filename                                                       extension size_bytes
.gitignore                                                     [none]             26
AGENTS.md                                                      md               3014
Claudes report on the research Phases 3a.pdf                   pdf            792034
Document_4_TrustLatch_Concept_Dossier.docx                     docx            39031
Engineering_Design_Review.md                                   md              31205
MC_Project_PHASE_DOC.md                                        md              11868
PROJECT_CONCEPT_CONTEXT.md                                     md               6646
Phase2_Memory.md                                               md               7820
Phase2_Report by CLaude.md                                     md              44493
Phase3A_MEMORY.md                                              md               8898
Phase3B_MEMORY.md                                              md              18836
Phase3B_Report_by_Claude.md                                    md              83718
Phase3C_TrueMoist_SOP.md                                       md              18712
Project_mC_Decision_Register_v1.0.md                           md              42548
CURRENT_FOLDER_STRUCTURE.txt                                   txt              7870
MC_Project_PHASE_DOC.md                                        md              11868
Phase1A_Memory.md                                              md               4029
Phase1A_Summary.md                                             md               2794
CHATGPT DEEP RESEARCH.md                                       md              20670
GEMINI DEEP RESEARCH.docx                                      docx          3035520
KIMI DEEP RESEARCH.docx                                        docx            64142
QWEN AI DEEP RESEARCH.pdf                                      pdf            519844
Phase1B_Memory.md                                              md               3966
Phase1B_Opportunity_Analysis.md                                md               5802
Phase1B_Opportunity_Analysis.zip                               zip            743098
Phase1B_Opportunity_Analysis_By_Claude.pdf                     pdf           1484584
Phase1B5_Memory.md                                             md               5302
Phase1B5_Opportunity_Portfolio_Optimization.md                 md               6431
Phase1B5_Portfolio_Optimization_By_Claude.pdf                  pdf            582050
Microcontroller_Project_Abstract_Proposal_5_Ideas.pdf          pdf             27986
Microcontroller_Project_Idea_Abstracts 2.0.pdf                 pdf             25856
Microcontroller_Project_Idea_Abstracts.pdf                     pdf             24352
Document_1_OpenBraille_Concept_Dossier.docx                    docx            38405
Document_2_VibeGuard_Concept_Dossier.docx                      docx            38619
Document_3_TrueMoist_Concept_Dossier.docx                      docx            38768
Document_4_TrustLatch_Concept_Dossier.docx                     docx            39031
POOJA PROJECT.pdf                                              pdf             98813
Patent Potential of Student Projects.docx                      docx          2998348
USB_Powered_Secure_File_Transfer_Authentication_Abstract.pdf   pdf              2399
USB_Powered_Smart_Anti_Theft_System_Abstract.pdf               pdf              2424
USB_Powered_Smart_Cabinet_Abstract.pdf                         pdf              2553
Phase1C.md                                                     md               3009
Phase1C_Concept_Synthesis.pdf                                  pdf            641952
Phase1C_Memory.md                                              md               3390
minimalist_project_proposal.pdf                                pdf             82574
project_proposal_booklet.pdf                                   pdf            666060
11 ideas.html                                                  html            68141
top 5.html                                                     html            43688
2_Sop.md                                                       md               6177
Phase2_DeepResearch_Prompt_v2.md                               md               8965
Phase2_Memory.md                                               md               7820
Phase2_Report From Claude.pdf                                  pdf            488517

                                             Page 4

                                     02_FILE_MANIFEST

Phase2_Report by CLaude.md                              md          44493
Phase2_docs.zip                                         zip         20668
CHATGT Research on Patent.docx                          docx        27850
Gemini Reearch on phase 2.docx                          docx      3011880
Kimi Patent Research.pdf                                pdf       1472114
QWen Research on Patent.pdf                             pdf        752520
Qwens Research on Phase 2.md                            md          92668
Engineering_Design_Review.md                            md          31205
Claudes report on the research Phases 3a.pdf            pdf        792034
Geminis Research On Phase 3A.docx                       docx        53060
MISTRAL RESEAARCH ON phase 3a.md                        md         122129
Perplexity Research on Phase 3A.pdf                     pdf        905522
Phase3A_MEMORY.md                                       md           8898
Qwen Research on Phase 3A.md                            md          63435
phase3B_report_and_summary.zip                          zip        522853
Gemini Research on Phase 3B.docx                        docx      3012247
Mistral researon on Phase 3B.md                         md          81611
Phase3B_DeepResearch_Prompt.md                          md          11471
Phase3B_MEMORY.md                                       md          18836
Phase3B_Report_by_Claude.md                             md          83718
Phase3B_mem_and_report.zip                              zip         35058
Project_mC_Phase3B_SOP.md                               md           8028
Qwen Rsearch on Phase 3B.pdf                            pdf        649615
perplexity_research_on_phase3B.md                       md          49895
Phase3C_Retained_Portfolio_Closure_Memo.md              md           3149
Phase3C_TrueMoist_ChatGPT_Final_Synthesis.md            md          46897
Phase3C_TrueMoist_DeepResearch_Prompt.md                md          28220
Phase3C_TrueMoist_Final_Synthesis_Prompt.md             md          10637
Phase3C_TrueMoist_MEMORY_Final.md                       md           5230
Phase3C_TrueMoist_PDR_Update_Patch.md                   md          10210
Phase3C_TrueMoist_SOP.md                                md          18712
TrueMoist 3C Gemini REsearch.docx                       docx       138980
TrueMoist Phase 3C Research By chatgpt.pdf              pdf      17994349
TrueMoist Phase 3C By Perplexity.md                     md          87503
phase-3c-truemoist-Research-Mistral.md                  md          19116
Claudes report for openbraille phase 3c.md              md          46126
Phase3C_OpenBraille_Claude_Synthesis_Prompt.md          md          17548
Phase3C_OpenBraille_DeepResearch_Prompt.md              md          19686
Phase3C_OpenBraille_Memory.md                           md          12364
Phase3C_OpenBraille_SOP.md                              md           4746
DEEpr research on phase 3c openbraille by chatgpt       [none]     151219
Perplexity research on phase 3C.docx                    docx       534977
gemini research on phase 3c.docx                        docx      3059479
mistral research on phase 3c.md                         md          75348
qwen Research on phase 3C.md                            md          45014
Phase3C_VibeGuard_DeepResearch_Prompt.md                md          25491
Phase3C_VibeGuard_Memory.md                             md           9485
claude_synthesis_prompt.md                              md          16519
claude_synthesis_prompt.mmd                             mmd         16518
Perplexity research on phase 3c.md                      md          46791
Phase3C_VibeGuard_Architecture_Report By Claude.md      md          32541
gemini research on phase 3c.docx                        docx      3049401
mistral reserach on phase 3c.md                         md          53102

                                            Page 5

                                       02_FILE_MANIFEST

qwens research on phase 3c.md                                           md       42575
vibeguard_sop.md                                                        md       15737
Phase3_DeepResearch_Prompt.md                                           md        9989
PROJECT_CONCEPT_CONTEXT.md                                              md        6646
Phase3_SOP.md                                                           md        6227
Project_mC_Decision_Register_v1.0.md.save                               save     42548
Project_mC_Decision_Register_v1.2.md                                    md       55963
README.md                                                               md          13
contexts.zip                                                            zip    3583134
MC_Project_PHASE_DOC.md                                                 md        6638
Phase1A_Memory.md                                                       md        4029
Phase1A_Summary.md                                                      md        2794
Phase1B5_Memory.md                                                      md        5302
Phase1B5_Opportunity_Portfolio_Optimization.md                          md        6431
Phase1B_Memory.md                                                       md        3966
Phase1B_Opportunity_Analysis.md                                         md        5802
Phase1C.md                                                              md        3009
Phase1C_Memory.md                                                       md        3390
every_sop_and memory_from phase 1A to 1C and whoel phase overview.zip   zip      19018


                                             Page 6

                                    02_FILE_MANIFEST

sha256                                                           probable_phase
06cbc9ed3b87cff938ebc17ad940c8cf13efcf2e8570025106b6a8b3d852b727 Repository-wide
7dc870163ab0eeb55112d377f5e015404ef631a55fd02332e8a692ead2b3b31 Repository-wide
7d0202fb62476a0212e594af473ad8d796eecd853e53e7f0952de90908cec611Cross-phase/unclear
f9a4184850435aba3ec26e480e802d1ba39f17037f0f368520a625c6f8e84f78 Cross-phase/unclear
46f017501ac3ff9ebd6c1fb1e5ee8c068c22ddb08ae204c5609f2b759090295e Cross-phase/unclear
c4b6c4a56bf8ba3066c5b426dce5ae4d50da4774478b5074566e9c79812e3ecCross-phase/unclear
f520cb5201e299fb0f9185bd2b79318229b898e5a8ad7822deb9a073e8f6cae4Cross-phase/unclear
973519f45bc075c296d4302b94933288496bd9bc12fae708aac1fb7020158ce8Phase 2
783729d0e07e725236db5296dae8504ce782c294b8c61cfab40ea172cfa6943Phase 2
acd3b4178143ca918ed4cce43d3d853acc994c0178dc8efdc406fb014e1ec997Phase 3A
7b6532c779867e9d6064473de4ba1b4799a0c385361cf27dc4616888fb0ac7aPhase 3B
14c19ac85b56e4e27da03de534a2a574ab7220d90005b4a7a0afb868f639047Phase 3B
993caf1a05f3fdc3937efb634e2f2e467488e973eb71454db8e3c3f53d178d00 Phase 3C
2ecf77fbbba9966a7769a2e715034f6b9ff7362d7aa51261219ee118085d22d3 Cross-phase governance
befdeb6ebd683f74616ace070a5aea279a46557886b4b4842c5441a436d787ffRepository-wide
c4b6c4a56bf8ba3066c5b426dce5ae4d50da4774478b5074566e9c79812e3ecRepository-wide
5a8943e1e556e1db0644cc7b75e2b4c8000b1a9506d673406c9c70cf7bb4a21Phase 1A
c52bed09fdfd1a860471bfc6d56cd41411f730362d12ee0348e07ad0939909c9Phase 1A
fa41ec5c0504aada478a754133290458a1333eee99542c4530d3fb2abc8f5ac0Phase 1A
e527fa3ab029f3dd3096184c35f90ccd21e61bd520d9eb677f1031abbebd13adPhase 1A
c0d4cbeb9099d8a58c4fa6eab7e2f06aa1a0bda76affecb9444f040e8169828f Phase 1A
5b3f7270de5bc6a27eba0e458cd2f7f40f55dd0407094f70ccfed6f6fd3f7ed8 Phase 1A
d58c91eead60c5abdb4e38c1e9b87c7449f4b3b68ccd7a23f5d4816fea16ff76 Phase 1B
e10d76b80c78554ff7e2ea75f3b263bfe82333c54418e7f794d249610f8fe130 Phase 1B
67d556082774dd9223e05d99f6b64eac045d7cc52ae9b60c403bc643a8b15daPhase 1B
8e53b914163d8e2685d9edda7422e4c1ac1a01230e60e3a100a0e7ef514dd52Phase 1B
d200473fd85a3cc910e3532bb2be662e0fcbdeab363fe988a948fd81d129c537Phase 1B.5
305f0f568081ad8a01affc02d252a681f84abde5c23c2a9421fb69369ecc5540 Phase 1B.5
25130fe434ba2962de3ca241374d9823acced92b088ec6562a77140b8055180Phase 1B.5
0d0c8ba61f0c5b2ea5ac243a382f1a1ffdb1e75ed27d8f2b1f6fc8b971afd82e Phase 1C
9d3f9364213e055715d85c85cf09c1609190c2c32918b60fcfe54f336f4fb8ec Phase 1C
8145ccd58cad7eadb15d9f0eb51c3e833cfbe2afe7eff9a174666118752f0874 Phase 1C
ac21af2a892f319e0b28d4d7314f4561c5aebad5291343c34d777beb933106eaPhase 1C
8a3c40cdc9ec899934ca9a37b05f9c0df22b583cd3ee259ebc81c1da9f0a0ae7Phase 1C
ca5cedfdfac5157b328aa865433a172d8af82a44d2dbf8b015c8c217fa6f85a2 Phase 1C
f9a4184850435aba3ec26e480e802d1ba39f17037f0f368520a625c6f8e84f78 Phase 1C
70a6446354f634cd7501e883e954bcba8f292a6bb91d406713d30c72b9be977Phase 1C
2156803ab9ac9a253fc6e8860c7788d9891af782fcd52e7a9c64249115cf0273 Phase 1C
ce5b8e3c904a82066e0718abc0e49c6583c5ec37022cc8d4e59cdefb202c526Phase 1C
6d5a03b4afbec01258f767ae31c592653ce6e5da09a29c62b5e8ec4841e5c5b Phase 1C
97d240350257e89ad533ef3067c7bf41e18362e01f1d43823eb73e68f9049d17Phase 1C
8e41493ddbc8b8b3c3ad8a00995b6ae3f8a5645351f8086a6b8ded92623853ePhase 1C
4f117f1a7bc0fb5b4ec9e450036566aa5198a08e84a451ad2e7d2dbc8636b084Phase 1C
e3b320245bc20d4312edc22b62fc9584059111e8fd38442277a3e5544ae019cPhase 1C
19d4198bb4fafc2fbd299a68517551c58e52d319a6c84c4df55c6a41246f44e0 Phase 1C
c15f75f4ce0ab6cf6bca5ad7bb1b3c12a4c1e4bfdf662886fd168ba78d67c203 Phase 1C
bd36812bff46105a8f6f9b6a38bbc93688b8e3cd2e9146456481b71c880f766d Phase 1C
a01c1706657b1a5abc76ec22e8e108a2d534608cda5f824fe656f257195d4192Phase 1C
c7d7d805d41313dee1dce65d9323c95075a8cde8d61ff2bfce3700510c41dd54Phase 2
372d5ccbc23bd7b8e444fb6071aea4e4760397b5c1a360201d288609b1efcefdPhase 2
973519f45bc075c296d4302b94933288496bd9bc12fae708aac1fb7020158ce8Phase 2
ab93da2c1ad6a9e22678e59da64a8992e4275ac4b01bad1061995dd9a5bf4f0Phase 2

                                          Page 7

                                    02_FILE_MANIFEST

783729d0e07e725236db5296dae8504ce782c294b8c61cfab40ea172cfa6943Phase 2
5b4156e64afaf59c1cc8788ae2c02cbebf8e2c003343dd8c56544219f1377fb6 Phase 2
61188e3fc06ca9ab2ddd8c196d217f10a59e077fe9b32687e2c0920d486501d5Phase 2
5af919473e667c9bae7abbdfc5f98067472f40beb5a3e5f1c793a0f12e4d0f53 Phase 2
33f4539a14653b55c0b73e0fbcd140827e2131ed9c3ca5d9bc896d4553f4a904Phase 2
75d736454cf7362a31e9ae1e2695a7bd793ab98187f2ad51ba9dc44f0d4473a Phase 2
5593a0581c350814e5567357effb2b1948cd3046a67bf52e00ff7495b9c0afe8 Phase 2
46f017501ac3ff9ebd6c1fb1e5ee8c068c22ddb08ae204c5609f2b759090295e Phase 3
7d0202fb62476a0212e594af473ad8d796eecd853e53e7f0952de90908cec611Phase 3A
6d380794c7b52664324a1e4e39dac49f40f50ad269391cbe1f6135175048b944Phase 3A
ae11e6b64bed09dcde373a21849085dd929a96f045d8a2362d4f07d58daed5cPhase 3A
a56c84e5ca354f3e1451fa98cd49d7184247c95b2b1ddf5b7e04a24bd954d19bPhase 3A
acd3b4178143ca918ed4cce43d3d853acc994c0178dc8efdc406fb014e1ec997Phase 3A
501782f664994ad0cfdeb72f16a975c2abe3a87ee4c456375a703f426437c99bPhase 3A
9d0593bb50717c290ca9c36d135ffc1aebfb70a48d2b058be4c8b421af44ae21Phase 3B
94e1e8e81c3f79f3f426086677841b1b4c2c32da8b50710e080bd0a27b9e2906Phase 3B
254d0b0a0df0cdab2fecb7ef65148474faff4f16c440fe4e76d0ada53cb6dc11 Phase 3B
2d0a79d6fe7e24bf1cc4c1d4b4a9e2c0cd3c8cead10ad0323b63709eec2811e6Phase 3B
7b6532c779867e9d6064473de4ba1b4799a0c385361cf27dc4616888fb0ac7aPhase 3B
14c19ac85b56e4e27da03de534a2a574ab7220d90005b4a7a0afb868f639047Phase 3B
b4674075c434e818a3579f61f8746dd918ac06e316030e04fa3c9577a36eafb0Phase 3B
6ce2ed40885038734faa75018a1caa16d89fcc7f18c7bf8249fe42453f36af4c Phase 3B
7a8fbde6b8fab93e195deefa716fb3f3724c369aa87deef27256be8fe8b45e1f Phase 3B
65a891eda465cab8f3d1d69e8320497dc8c05c5a2176c25d9c0cb81218f4b4d Phase 3B
3c6e6f568c06099251b4b71d4f35cf668ee23a40c8214c95e4a12fe36cf4845a Phase 3C
6c71f1d618e0575d127b10f05e91d06ea4b1f0b8a2fe63e78d4022ee75234610Phase 3C
da66d2b9259a007d390b7fdc2766b9349bf88497cd60af3bc0c5e6855cddd08ePhase 3C
144617f2efe8ef6db6122d00039fcc3566d8aab03649e003837eea5c0a60618ePhase 3C
ba8264d74f37168e5de85a5d76adb354062dc5e47b692b12f76f73aac62c7377Phase 3C
f9b23506c0b78a76ac590fa7bb80911c1a416569eb17c41644b2cfd9b432a803Phase 3C
993caf1a05f3fdc3937efb634e2f2e467488e973eb71454db8e3c3f53d178d00 Phase 3C
b0eab8009831f5b719bf9d20ad1f25e9bcc549fc260a078a5be2531dc86e5b24Phase 3C
87ccbd3416f3f7bb58e544095a1e20560f9561ffe72db82f868d17bf942812e7 Phase 3C
caefe1da05e1963e0cd9c3916fc50d4c2e4b396006cdf39ebf8eee893f0c3187 Phase 3C
706d9ae47b256de0bb01d2836c3b24095b4109fd6c1011491aa88d32799fd1cPhase 3C
0e6c40edc6fd79c17f6bcac8e6d1598217ff7cadbdbf721ea55e4c39d4d36aa8 Phase 3C
2cd7dbdabb86f93a69ebfc012a5518fdb814529999c44f68c4252a19f5b8cf04 Phase 3C
a59b4743782e0e21e1472b28b116a1bf83a2ede098a28e8d5110a8ab1ce33e Phase 3C
5dad0e392cf9c64d7e8f29be09fadb70acde5b965b95744fa066b5f4b4fd30eb Phase 3C
bfee5dc46675d77b318f4a0d4fe864d77a570a1150cc2676a5dd10103f214e50Phase 3C
864e400d3b259157346319b53eb36868b28bf183fb6ac5a1efbcbb6315424e0 Phase 3C
6350e11ac346e30fbb3ca252a40367e4394bfcf1cf9e1f2ad8c84fcf1bf3545d Phase 3C
a1d2b01cdbaa412c79251ffec0b7fad9e606aa16609a664a88b6ebd8149b8b7cPhase 3C
aff5ebe5ff1fedfc5cc52cb9ef52d6b742ea495ff5304eb5acedaa8ff7e21c83 Phase 3C
3416c5526a1c73e5b29acf0117d45b4a5ee86cc1391eb9a105ca6710d0048f2 Phase 3C
af08518f2c65bc8a53ff2520775415d2fd7f3bd5da2fc7e37018ae96a0c412d6 Phase 3C
3d07fdb1b9b2c0c273dacf3b49650e2deb6fa72a36af38035c85118e3fd51960 Phase 3C
26b50889394442be4fb22e26fad74b6ca97c7e5765f330b92b241ff8e69c1a2e Phase 3C
59ae97bd4407b3e18cb2fb9ac99abdeeaf9aa3fdc3f5cb5e6f8ea67f330da47e Phase 3C
0b1a2ea090cbc3630e84f4c4902e307e72751ca531f85bfe473285f74f4df368 Phase 3C
d6a5f009d5c96bceb6cc0cb2f4d70817204e7346e7f6e7c21a5e86b457254573Phase 3C
39a249ed0b0c9d76b0372e558b04d47a837b6a1849848f84fa9bf88f1ade0921Phase 3C
86efffd004de1dd811343d0d6def5c8955189f66aa56af244f6b5d2d4dacc355 Phase 3C

                                          Page 8

                                     02_FILE_MANIFEST

a16b18b36f221d2a3f4de53d65068de3bb20d253e0d550c60c7735b30ae19f4 Phase 3C
e073729670896e004900fdb52c049819d78d4b597f7da08e62c54de1152f7e0cPhase 3C
4173379249d0dca88800c04432b71cf1184f958abf2809d72c023363cdd1449cPhase 3
f520cb5201e299fb0f9185bd2b79318229b898e5a8ad7822deb9a073e8f6cae4Cross-phase governance
3c3bfa374c40280be56adbd22f5ba7e07c3f38254557c0d1885da5708f6c53dePhase 3
2ecf77fbbba9966a7769a2e715034f6b9ff7362d7aa51261219ee118085d22d3 Cross-phase governance
ebdbbf8df5645fb41b238dc403d7160bbec78a5114b93237eea4ac098ef21d2eCross-phase governance
77702c121156afe1be6cc6ef8ce1c61a0291b13b3aa7a2f2ef1f4d608025ec06 Repository-wide
29c21e888bc2ac1fb42514db91bff88a6a67bafde26a05ddc6933010ba3233f6 Phase 1A context package
e7ebf127dac01b63c87713b14c0bd5cf2d4500e60581cc86f783abe92a525f98 Cross-phase/unclear
5a8943e1e556e1db0644cc7b75e2b4c8000b1a9506d673406c9c70cf7bb4a21Phase 1A
c52bed09fdfd1a860471bfc6d56cd41411f730362d12ee0348e07ad0939909c9Phase 1A
d200473fd85a3cc910e3532bb2be662e0fcbdeab363fe988a948fd81d129c537Phase 1B.5
305f0f568081ad8a01affc02d252a681f84abde5c23c2a9421fb69369ecc5540 Phase 1B.5
d58c91eead60c5abdb4e38c1e9b87c7449f4b3b68ccd7a23f5d4816fea16ff76 Phase 1B
e10d76b80c78554ff7e2ea75f3b263bfe82333c54418e7f794d249610f8fe130 Phase 1B
8e41493ddbc8b8b3c3ad8a00995b6ae3f8a5645351f8086a6b8ded92623853ePhase 1C
e3b320245bc20d4312edc22b62fc9584059111e8fd38442277a3e5544ae019cPhase 1C
cdc5acdda096d42498ba49d4bec9451e1cb8cfa5251d295a0412d0e4d9a8366Cross-phase/unclear


                                           Page 9

                                         02_FILE_MANIFEST

probable_concept      document_role
Repository-wide/none Git ignore configuration
Repository-wide/none Repository governance instructions
Repository-wide/none Raw independent research
TrustLatch (deferred) Concept dossier
Repository-wide/none Engineering Design Review
Multi-concept         Project methodology/phase roadmap
Multi-concept         Supporting project document
Multi-concept         Phase memory
Multi-concept         Phase report/supporting deliverable
Multi-concept         Phase memory
Multi-concept         Phase memory
Multi-concept         Phase report/supporting deliverable
TrueMoist             Methodology/SOP
Multi-concept         Project Decision Register
Repository-wide/none Stale structure snapshot
Multi-concept         Project methodology/phase roadmap
Multi-concept         Phase memory
Multi-concept         Methodology/SOP
Repository-wide/none Raw independent research
Repository-wide/none Raw independent research
Repository-wide/none Raw independent research
Repository-wide/none Raw independent research
Multi-concept         Phase memory
Multi-concept         Methodology/SOP
Multi-concept         Convenience/archive package
Multi-concept         Phase report/supporting deliverable
Multi-concept         Phase memory
Multi-concept         Methodology/SOP
Multi-concept         Phase report/supporting deliverable
Multi-concept         Phase report/supporting deliverable
Multi-concept         Phase report/supporting deliverable
Multi-concept         Phase report/supporting deliverable
OpenBraille           Concept dossier
VibeGuard             Concept dossier
TrueMoist             Concept dossier
TrustLatch (deferred) Concept dossier
Multi-concept         Phase report/supporting deliverable
Multi-concept         Supporting project document
Multi-concept         Phase report/supporting deliverable
Multi-concept         Phase report/supporting deliverable
Multi-concept         Phase report/supporting deliverable
Multi-concept         Methodology/SOP
Multi-concept         Phase report/supporting deliverable
Multi-concept         Phase memory
Multi-concept         Phase report/supporting deliverable
Multi-concept         Phase report/supporting deliverable
Multi-concept         Concept visualization
Multi-concept         Concept visualization
Repository-wide/none Methodology/SOP
Multi-concept         AI research/synthesis prompt
Multi-concept         Phase memory
Multi-concept         Phase report/supporting deliverable

                                               Page 10

                                        02_FILE_MANIFEST

Multi-concept        Phase report/supporting deliverable
Multi-concept        Convenience/archive package
Multi-concept        Raw independent research
Repository-wide/none Raw independent research
Multi-concept        Raw independent research
Multi-concept        Raw independent research
Repository-wide/none Raw independent research
Repository-wide/none Engineering Design Review
Repository-wide/none Raw independent research
Repository-wide/none Raw independent research
Repository-wide/none Raw independent research
Repository-wide/none Raw independent research
Multi-concept        Phase memory
Repository-wide/none Raw independent research
Multi-concept        Convenience/archive package
Repository-wide/none Raw independent research
Repository-wide/none Raw independent research
Multi-concept        AI research/synthesis prompt
Multi-concept        Phase memory
Multi-concept        Phase report/supporting deliverable
Multi-concept        Convenience/archive package
Multi-concept        Methodology/SOP
Repository-wide/none Raw independent research
Multi-concept        Raw independent research
Multi-concept        Approved portfolio closure memo
TrueMoist            Final Phase 3C architecture/synthesis report
TrueMoist            AI research/synthesis prompt
TrueMoist            AI research/synthesis prompt
TrueMoist            Phase memory
TrueMoist            Historical PDR update patch
TrueMoist            Methodology/SOP
TrueMoist            Raw independent research
TrueMoist            Raw independent research
TrueMoist            Raw independent research
TrueMoist            Raw independent research
OpenBraille          Final Phase 3C architecture/synthesis report
OpenBraille          AI research/synthesis prompt
OpenBraille          AI research/synthesis prompt
OpenBraille          Phase memory
OpenBraille          Methodology/SOP
OpenBraille          Failed/mis-scoped raw research (PDF without extension)
OpenBraille          Raw independent research
OpenBraille          Raw independent research
OpenBraille          Raw independent research
OpenBraille          Raw independent research
VibeGuard            AI research/synthesis prompt
VibeGuard            Phase memory
VibeGuard            AI research/synthesis prompt
VibeGuard            AI research/synthesis prompt
VibeGuard            Raw independent research
VibeGuard            Final Phase 3C architecture/synthesis report
VibeGuard            Raw independent research
VibeGuard            Raw independent research

                                              Page 11

                                        02_FILE_MANIFEST

VibeGuard            Raw independent research
VibeGuard            Methodology/SOP
Multi-concept        AI research/synthesis prompt
Multi-concept        Canonical concept context
Multi-concept        Methodology/SOP
Multi-concept        Project Decision Register
Multi-concept        Project Decision Register
Repository-wide/none Repository landing page
Multi-concept        Convenience/archive package
Multi-concept        Phase memory
Multi-concept        Phase memory
Multi-concept        Phase memory
Multi-concept        Phase memory
Multi-concept        Phase memory
Multi-concept        Phase memory
Multi-concept        Phase memory
Multi-concept        Phase memory
Multi-concept        Phase memory
Repository-wide/none Convenience/archive package


                                             Page 12

                                        02_FILE_MANIFEST

authority_level                                              exact_duplicate_group
Supporting/non-decision artifact
Governance/context (outside numbered technical precedence)
Level 10 — raw research evidence only                        ED-08
Convenience/context only; non-canonical container            ED-20
Convenience copy of Level 1 — Engineering Design Review      ED-04
Governance/context (outside numbered technical precedence)   ED-13
Convenience/context only; non-canonical container            ED-19
Convenience copy of Level 8 — Phase 2 report/memory          ED-10
Convenience copy of Level 8 — Phase 2 report/memory          ED-06
Convenience copy of Level 7 — Phase 3A report/memory         ED-12
Convenience copy of Level 6 — Phase 3B report/memory         ED-07
Convenience copy of Level 6 — Phase 3B report/memory         ED-01
Convenience/context only; non-canonical container            ED-11
Historical/superseded Decision Register                      ED-02
Supporting/non-decision artifact
Governance/context (outside numbered technical precedence)   ED-13
Supporting/non-decision artifact                             ED-05
Supporting/non-decision artifact                             ED-14
Level 10 — raw research evidence only
Level 10 — raw research evidence only
Level 10 — raw research evidence only
Level 10 — raw research evidence only
Supporting/non-decision artifact                             ED-16
Supporting/non-decision artifact                             ED-17
Convenience/context only; non-canonical container
Supporting/non-decision artifact
Supporting/non-decision artifact                             ED-15
Supporting/non-decision artifact                             ED-03
Supporting/non-decision artifact
Level 9 — Phase 1C synthesis/dossier
Level 9 — Phase 1C synthesis/dossier
Level 9 — Phase 1C synthesis/dossier
Level 9 — Phase 1C synthesis/dossier
Level 9 — Phase 1C synthesis/dossier
Level 9 — Phase 1C synthesis/dossier
Level 9 — Phase 1C synthesis/dossier                         ED-20
Level 9 — Phase 1C synthesis/dossier
Supporting/non-decision artifact
Level 9 — Phase 1C synthesis/dossier
Level 9 — Phase 1C synthesis/dossier
Level 9 — Phase 1C synthesis/dossier
Level 9 — Phase 1C synthesis/dossier                         ED-09
Level 9 — Phase 1C synthesis/dossier
Level 9 — Phase 1C synthesis/dossier                         ED-18
Level 9 — Phase 1C synthesis/dossier
Level 9 — Phase 1C synthesis/dossier
Supporting/non-decision artifact
Supporting/non-decision artifact
Supporting/non-decision artifact
Supporting/non-decision artifact
Level 8 — Phase 2 report/memory                              ED-10
Level 8 — Phase 2 report/memory

                                              Page 13

                                         02_FILE_MANIFEST

Level 8 — Phase 2 report/memory                          ED-06
Convenience/context only; non-canonical container
Level 10 — raw research evidence only
Level 10 — raw research evidence only
Level 10 — raw research evidence only
Level 10 — raw research evidence only
Level 10 — raw research evidence only
Level 1 — Engineering Design Review                      ED-04
Level 10 — raw research evidence only                    ED-08
Level 10 — raw research evidence only
Level 10 — raw research evidence only
Level 10 — raw research evidence only
Level 7 — Phase 3A report/memory                         ED-12
Level 10 — raw research evidence only
Convenience/context only; non-canonical container
Level 10 — raw research evidence only
Level 10 — raw research evidence only
Supporting/non-decision artifact
Level 6 — Phase 3B report/memory                         ED-07
Level 6 — Phase 3B report/memory                         ED-01
Convenience/context only; non-canonical container
Supporting/non-decision artifact
Level 10 — raw research evidence only
Level 10 — raw research evidence only
Level 3 — retained-portfolio closure memo
Level 4 — final Phase 3C architecture report
Supporting/non-decision artifact
Supporting/non-decision artifact
Level 5 — Phase 3C memory
Supporting/non-decision artifact
Supporting/non-decision artifact                         ED-11
Level 10 — raw research evidence only
Level 10 — raw research evidence only
Level 10 — raw research evidence only
Level 10 — raw research evidence only
Level 4 — final Phase 3C architecture report
Supporting/non-decision artifact
Supporting/non-decision artifact
Level 5 — Phase 3C memory
Supporting/non-decision artifact
Level 10 — raw research evidence only
Level 10 — raw research evidence only
Level 10 — raw research evidence only
Level 10 — raw research evidence only
Level 10 — raw research evidence only
Supporting/non-decision artifact
Level 5 — Phase 3C memory
Supporting/non-decision artifact
Supporting/non-decision artifact
Level 10 — raw research evidence only
Level 4 — final Phase 3C architecture report
Level 10 — raw research evidence only
Level 10 — raw research evidence only

                                               Page 14

                                        02_FILE_MANIFEST

Level 10 — raw research evidence only
Supporting/non-decision artifact
Supporting/non-decision artifact
Governance/context (outside numbered technical precedence)   ED-19
Supporting/non-decision artifact
Historical/superseded Decision Register                      ED-02
Level 2 — latest Decision Register
Supporting/non-decision artifact
Convenience/context only; non-canonical container
Convenience/context only; non-canonical container
Convenience/context only; non-canonical container            ED-05
Convenience/context only; non-canonical container            ED-14
Convenience/context only; non-canonical container            ED-15
Convenience/context only; non-canonical container            ED-03
Convenience/context only; non-canonical container            ED-16
Convenience/context only; non-canonical container            ED-17
Convenience copy of Level 9 — Phase 1C synthesis/dossier     ED-09
Convenience copy of Level 9 — Phase 1C synthesis/dossier     ED-18
Convenience/context only; non-canonical container


                                              Page 15

                                        02_FILE_MANIFEST

possible_cross_format_duplicate_group


CF-01


CF-01

                                            Page 16

        02_FILE_MANIFEST

CF-01


CF-02
CF-02


CF-03
CF-03


            Page 17

                                    02_FILE_MANIFEST

probable_canonical_file
.gitignore
AGENTS.md
PHASE 3/PHASE 3A-Engineering Landscape Discovery/Claudes report on the research Phases 3a.pdf
PHASE 1/PHASE 1C/INDEPTH OF EACH FIVE IDEA/Document_4_TrustLatch_Concept_Dossier.docx
PHASE 3/Engineering_Design_Review.md
MC_Project_PHASE_DOC.md
PROJECT_CONCEPT_CONTEXT.md
PHASE 2/Phase2_Memory.md
PHASE 2/Phase2_Report by CLaude.md
PHASE 3/PHASE 3A-Engineering Landscape Discovery/Phase3A_MEMORY.md
PHASE 3/PHASE 3B-Engineering Feasibility Analysis/Phase3B_MEMORY.md
PHASE 3/PHASE 3B-Engineering Feasibility Analysis/Phase3B_Report_by_Claude.md
PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_SOP.md
Project_mC_Decision_Register_v1.0.md.save
CURRENT_FOLDER_STRUCTURE.txt
MC_Project_PHASE_DOC.md
PHASE 1/PHASE 1.A/Phase1A_Memory.md
PHASE 1/PHASE 1.A/Phase1A_Summary.md
PHASE 1/PHASE 1.A/RESEARCHS/CHATGPT DEEP RESEARCH.md
PHASE 1/PHASE 1.A/RESEARCHS/GEMINI DEEP RESEARCH.docx
PHASE 1/PHASE 1.A/RESEARCHS/KIMI DEEP RESEARCH.docx
PHASE 1/PHASE 1.A/RESEARCHS/QWEN AI DEEP RESEARCH.pdf
PHASE 1/PHASE 1.B/Phase1B_Memory.md
PHASE 1/PHASE 1.B/Phase1B_Opportunity_Analysis.md
Normal files listed in 03_DUPLICATE_REPORT.md
PHASE 1/PHASE 1.B/Phase1B_Opportunity_Analysis_By_Claude.pdf
PHASE 1/PHASE 1B.5/Phase1B5_Memory.md
PHASE 1/PHASE 1B.5/Phase1B5_Opportunity_Portfolio_Optimization.md
PHASE 1/PHASE 1B.5/Phase1B5_Portfolio_Optimization_By_Claude.pdf
PHASE 1/PHASE 1C/5 IDEA ABSTRACT/Microcontroller_Project_Abstract_Proposal_5_Ideas.pdf
PHASE 1/PHASE 1C/5 IDEA ABSTRACT/Microcontroller_Project_Idea_Abstracts 2.0.pdf
PHASE 1/PHASE 1C/5 IDEA ABSTRACT/Microcontroller_Project_Idea_Abstracts.pdf
PHASE 1/PHASE 1C/INDEPTH OF EACH FIVE IDEA/Document_1_OpenBraille_Concept_Dossier.docx
PHASE 1/PHASE 1C/INDEPTH OF EACH FIVE IDEA/Document_2_VibeGuard_Concept_Dossier.docx
PHASE 1/PHASE 1C/INDEPTH OF EACH FIVE IDEA/Document_3_TrueMoist_Concept_Dossier.docx
PHASE 1/PHASE 1C/INDEPTH OF EACH FIVE IDEA/Document_4_TrustLatch_Concept_Dossier.docx
PHASE 1/PHASE 1C/OTHERS IDEA FORMAT/POOJA PROJECT.pdf
PHASE 1/PHASE 1C/OTHERS IDEA FORMAT/Patent Potential of Student Projects.docx
PHASE 1/PHASE 1C/OTHERS IDEA FORMAT/USB_Powered_Secure_File_Transfer_Authentication_Abstract.pdf
PHASE 1/PHASE 1C/OTHERS IDEA FORMAT/USB_Powered_Smart_Anti_Theft_System_Abstract.pdf
PHASE 1/PHASE 1C/OTHERS IDEA FORMAT/USB_Powered_Smart_Cabinet_Abstract.pdf
PHASE 1/PHASE 1C/Phase1C.md
PHASE 1/PHASE 1C/Phase1C_Concept_Synthesis.pdf
PHASE 1/PHASE 1C/Phase1C_Memory.md
PHASE 1/PHASE 1C/minimalist_project_proposal.pdf
PHASE 1/PHASE 1C/project_proposal_booklet.pdf
PHASE 1/PHASE 1C/visual explanation of the 5 ideas/11 ideas.html
PHASE 1/PHASE 1C/visual explanation of the 5 ideas/top 5.html
PHASE 2/2_Sop.md
PHASE 2/Phase2_DeepResearch_Prompt_v2.md
PHASE 2/Phase2_Memory.md
PHASE 2/Phase2_Report by CLaude.md

                                         Page 18

                                       02_FILE_MANIFEST

PHASE 2/Phase2_Report by CLaude.md
Normal files listed in 03_DUPLICATE_REPORT.md
PHASE 2/RESEARCH DOCS/CHATGT Research on Patent.docx
PHASE 2/RESEARCH DOCS/Gemini Reearch on phase 2.docx
PHASE 2/RESEARCH DOCS/Kimi Patent Research.pdf
Undetermined pending manual comparison (PDF is more complete)
Undetermined pending manual comparison (PDF is more complete)
PHASE 3/Engineering_Design_Review.md
PHASE 3/PHASE 3A-Engineering Landscape Discovery/Claudes report on the research Phases 3a.pdf
PHASE 3/PHASE 3A-Engineering Landscape Discovery/Geminis Research On Phase 3A.docx
PHASE 3/PHASE 3A-Engineering Landscape Discovery/MISTRAL RESEAARCH ON phase 3a.md
PHASE 3/PHASE 3A-Engineering Landscape Discovery/Perplexity Research on Phase 3A.pdf
PHASE 3/PHASE 3A-Engineering Landscape Discovery/Phase3A_MEMORY.md
PHASE 3/PHASE 3A-Engineering Landscape Discovery/Qwen Research on Phase 3A.md
Normal files listed in 03_DUPLICATE_REPORT.md
PHASE 3/PHASE 3B-Engineering Feasibility Analysis/Gemini Research on Phase 3B.docx
PHASE 3/PHASE 3B-Engineering Feasibility Analysis/Mistral researon on Phase 3B.md
PHASE 3/PHASE 3B-Engineering Feasibility Analysis/Phase3B_DeepResearch_Prompt.md
PHASE 3/PHASE 3B-Engineering Feasibility Analysis/Phase3B_MEMORY.md
PHASE 3/PHASE 3B-Engineering Feasibility Analysis/Phase3B_Report_by_Claude.md
Normal files listed in 03_DUPLICATE_REPORT.md
PHASE 3/PHASE 3B-Engineering Feasibility Analysis/Project_mC_Phase3B_SOP.md
PHASE 3/PHASE 3B-Engineering Feasibility Analysis/Qwen Rsearch on Phase 3B.pdf
PHASE 3/PHASE 3B-Engineering Feasibility Analysis/perplexity_research_on_phase3B.md
PHASE 3/PHASE 3C-Comparative Technical Evaluation/Phase3C_Retained_Portfolio_Closure_Memo.md
PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_ChatGPT_Final_Synthesis.md
PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_DeepResearch_Prompt.md
PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_Final_Synthesis_Prompt.md
PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_MEMORY_Final.md
PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_PDR_Update_Patch.md
PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_SOP.md
PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Research/TrueMoist 3C Gemini REsearch.docx
PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Research/TrueMoist Phase 3C Research By chatgpt.p
PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Research/TrueMoist Phase 3C By Perplexity.md
PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Research/phase-3c-truemoist-Research-Mistral.md
PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Claudes report for openbraille phase 3c.md
PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Phase3C_OpenBraille_Claude_Synthesis_Prompt.m
PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Phase3C_OpenBraille_DeepResearch_Prompt.md
PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Phase3C_OpenBraille_Memory.md
PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Phase3C_OpenBraille_SOP.md
PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Researches/DEEpr research on phase 3c openbraille
PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Researches/Perplexity research on phase 3C.docx
PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Researches/gemini research on phase 3c.docx
PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Researches/mistral research on phase 3c.md
PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Researches/qwen Research on phase 3C.md
PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/Phase3C_VibeGuard_DeepResearch_Prompt.md
PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/Phase3C_VibeGuard_Memory.md
PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/claude_synthesis_prompt.md
PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/claude_synthesis_prompt.md
PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/research/Perplexity research on phase 3c.md
PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/research/Phase3C_VibeGuard_Architecture_Report B
PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/research/gemini research on phase 3c.docx
PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/research/mistral reserach on phase 3c.md

                                             Page 19

                                      02_FILE_MANIFEST

PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/research/qwens research on phase 3c.md
PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/vibeguard_sop.md
PHASE 3/Phase3_DeepResearch_Prompt.md
PROJECT_CONCEPT_CONTEXT.md
Phase3_SOP.md
Project_mC_Decision_Register_v1.0.md.save
Project_mC_Decision_Register_v1.2.md
README.md
Normal Phase 1A files; embedded phase roadmap is historical
MC_Project_PHASE_DOC.md
PHASE 1/PHASE 1.A/Phase1A_Memory.md
PHASE 1/PHASE 1.A/Phase1A_Summary.md
PHASE 1/PHASE 1B.5/Phase1B5_Memory.md
PHASE 1/PHASE 1B.5/Phase1B5_Opportunity_Portfolio_Optimization.md
PHASE 1/PHASE 1.B/Phase1B_Memory.md
PHASE 1/PHASE 1.B/Phase1B_Opportunity_Analysis.md
PHASE 1/PHASE 1C/Phase1C.md
PHASE 1/PHASE 1C/Phase1C_Memory.md
Normal files listed in 03_DUPLICATE_REPORT.md


                                            Page 20

                                          02_FILE_MANIFEST

confidence   manual_review_requirement
High         No
High         No
High         Yes — convenience copy; do not treat as canonical
High         Yes — convenience copy; do not treat as canonical
High         Yes — convenience copy; do not treat as canonical
High         Yes — convenience copy; do not treat as canonical
High         Yes — convenience copy; do not treat as canonical
High         Yes — convenience copy; do not treat as canonical
High         Yes — cross-format scope/equivalence review
High         Yes — convenience copy; do not treat as canonical
High         Yes — convenience copy; do not treat as canonical
High         Yes — convenience copy; do not treat as canonical
High         Yes — convenience copy; do not treat as canonical
High         Yes — ensure historical/superseded labeling
High         Yes — stale status/version or structure snapshot
High         Yes — stale status/version or structure snapshot
High         No
High         No
High         No
Medium       No, unless used for a project decision
Medium       No, unless used for a project decision
Medium       No, unless used for a project decision
High         No
High         No
High         Yes — convenience archive retention/version policy
Medium       No, unless used for a project decision
High         No
High         No
Medium       No, unless used for a project decision
Medium       No, unless used for a project decision
Medium       No, unless used for a project decision
Medium       No, unless used for a project decision
High         No
High         No
High         No
High         No
Medium       No, unless used for a project decision
High         No
Medium       No, unless used for a project decision
Medium       No, unless used for a project decision
Medium       No, unless used for a project decision
High         No
Medium       No, unless used for a project decision
High         No
Medium       No, unless used for a project decision
Medium       No, unless used for a project decision
High         No
High         No
High         No
High         No
High         No
High         Yes — cross-format scope/equivalence review

                                                Page 21

                                      02_FILE_MANIFEST

High     Yes — cross-format scope/equivalence review
High     Yes — convenience archive retention/version policy
Medium   No, unless used for a project decision
Medium   No, unless used for a project decision
Medium   No, unless used for a project decision
Medium   Yes — cross-format scope/equivalence review
Medium   Yes — cross-format scope/equivalence review
High     No
Medium   No, unless used for a project decision
Medium   No, unless used for a project decision
High     No
Medium   No, unless used for a project decision
High     No
High     No
High     Yes — convenience archive retention/version policy
Medium   No, unless used for a project decision
High     No
High     No
High     No
High     No
High     Yes — convenience archive retention/version policy
High     No
Medium   No, unless used for a project decision
High     No
High     No
High     No
High     No
High     No
High     No
High     No
High     No
Medium   No, unless used for a project decision
Medium   No, unless used for a project decision
High     No
High     No
High     No
High     No
High     No
High     No
High     No
High     Yes — label as failed and restore .pdf extension
Medium   No, unless used for a project decision
Medium   No, unless used for a project decision
High     No
High     No
High     No
High     No
High     Yes — cross-format scope/equivalence review
High     Yes — cross-format scope/equivalence review
High     No
High     No
Medium   No, unless used for a project decision
High     No

                                            Page 22

                                    02_FILE_MANIFEST

High   No
High   No
High   No
High   No
High   No
High   Yes — ensure historical/superseded labeling
High   No
High   No
High   Yes — convenience archive retention/version policy
High   Yes — stale status/version or structure snapshot
High   Yes — convenience copy; do not treat as canonical
High   Yes — convenience copy; do not treat as canonical
High   Yes — convenience copy; do not treat as canonical
High   Yes — convenience copy; do not treat as canonical
High   Yes — convenience copy; do not treat as canonical
High   Yes — convenience copy; do not treat as canonical
High   Yes — convenience copy; do not treat as canonical
High   Yes — convenience copy; do not treat as canonical
High   Yes — convenience archive retention/version policy


                                          Page 23


---

## Source 15: `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Legacy_Repository_Audit/03_DUPLICATE_REPORT.md`

- Authority: `TIER_1`
- Treatment: `CORE_NARRATIVE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `e73b55d4f36f630dfc45d61147e0d683a364af1f0e28a95f54c5da972cc24925`

# Source Extraction

- Chapter: `01` — Project Mandate, Requirements and Governance
- Authority tier: `TIER_1`
- Manual treatment: `CORE_NARRATIVE`
- Original source: `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Legacy_Repository_Audit/03_DUPLICATE_REPORT.md`
- Current SHA-256: `e73b55d4f36f630dfc45d61147e0d683a364af1f0e28a95f54c5da972cc24925`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

# Duplicate Report

## Method

- SHA-256 over each working-tree file identified exact binary duplicates.
- PDF text was extracted with the already-installed `pdftotext`.
- DOCX text was read from the package’s `word/document.xml`; packages were not expanded into the repository.
- Extracted text was whitespace/case normalized and compared with word-trigram overlap.
- Similar names alone were never used as duplicate evidence.

## Exact binary duplicates

There are **20 exact-duplicate groups**, covering **40 working-tree files**. Convenience copies are not proposed as canonical when an identical phase/root copy exists.

| Group | SHA-256 | Paths | Probable canonical file |
|---|---|---|---|
| ED-01 | `14c19ac85b56e4e27da03de534a2a574ab7220d90005b4a7a0afb868f6390478` | `COPY PASTE FOLDER/Phase3B_Report_by_Claude.md`<br>`PHASE 3/PHASE 3B-Engineering Feasibility Analysis/Phase3B_Report_by_Claude.md` | `PHASE 3/PHASE 3B-Engineering Feasibility Analysis/Phase3B_Report_by_Claude.md` |
| ED-02 | `2ecf77fbbba9966a7769a2e715034f6b9ff7362d7aa51261219ee118085d22d3` | `COPY PASTE FOLDER/Project_mC_Decision_Register_v1.0.md`<br>`Project_mC_Decision_Register_v1.0.md.save` | `Project_mC_Decision_Register_v1.0.md.save` |
| ED-03 | `305f0f568081ad8a01affc02d252a681f84abde5c23c2a9421fb69369ecc5540` | `PHASE 1/PHASE 1B.5/Phase1B5_Opportunity_Portfolio_Optimization.md`<br>`every sop and memory/Phase1B5_Opportunity_Portfolio_Optimization.md` | `PHASE 1/PHASE 1B.5/Phase1B5_Opportunity_Portfolio_Optimization.md` |
| ED-04 | `46f017501ac3ff9ebd6c1fb1e5ee8c068c22ddb08ae204c5609f2b759090295e` | `COPY PASTE FOLDER/Engineering_Design_Review.md`<br>`PHASE 3/Engineering_Design_Review.md` | `PHASE 3/Engineering_Design_Review.md` |
| ED-05 | `5a8943e1e556e1db0644cc7b75e2b4c8000b1a9506d673406c9c70cf7bb4a213` | `PHASE 1/PHASE 1.A/Phase1A_Memory.md`<br>`every sop and memory/Phase1A_Memory.md` | `PHASE 1/PHASE 1.A/Phase1A_Memory.md` |
| ED-06 | `783729d0e07e725236db5296dae8504ce782c294b8c61cfab40ea172cfa6943e` | `COPY PASTE FOLDER/Phase2_Report by CLaude.md`<br>`PHASE 2/Phase2_Report by CLaude.md` | `PHASE 2/Phase2_Report by CLaude.md` |
| ED-07 | `7b6532c779867e9d6064473de4ba1b4799a0c385361cf27dc4616888fb0ac7ad` | `COPY PASTE FOLDER/Phase3B_MEMORY.md`<br>`PHASE 3/PHASE 3B-Engineering Feasibility Analysis/Phase3B_MEMORY.md` | `PHASE 3/PHASE 3B-Engineering Feasibility Analysis/Phase3B_MEMORY.md` |
| ED-08 | `7d0202fb62476a0212e594af473ad8d796eecd853e53e7f0952de90908cec611` | `COPY PASTE FOLDER/Claudes report on the research Phases 3a.pdf`<br>`PHASE 3/PHASE 3A-Engineering Landscape Discovery/Claudes report on the research Phases 3a.pdf` | `PHASE 3/PHASE 3A-Engineering Landscape Discovery/Claudes report on the research Phases 3a.pdf` |
| ED-09 | `8e41493ddbc8b8b3c3ad8a00995b6ae3f8a5645351f8086a6b8ded92623853e4` | `PHASE 1/PHASE 1C/Phase1C.md`<br>`every sop and memory/Phase1C.md` | `PHASE 1/PHASE 1C/Phase1C.md` |
| ED-10 | `973519f45bc075c296d4302b94933288496bd9bc12fae708aac1fb7020158ce8` | `COPY PASTE FOLDER/Phase2_Memory.md`<br>`PHASE 2/Phase2_Memory.md` | `PHASE 2/Phase2_Memory.md` |
| ED-11 | `993caf1a05f3fdc3937efb634e2f2e467488e973eb71454db8e3c3f53d178d00` | `COPY PASTE FOLDER/Phase3C_TrueMoist_SOP.md`<br>`PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_SOP.md` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_SOP.md` |
| ED-12 | `acd3b4178143ca918ed4cce43d3d853acc994c0178dc8efdc406fb014e1ec997` | `COPY PASTE FOLDER/Phase3A_MEMORY.md`<br>`PHASE 3/PHASE 3A-Engineering Landscape Discovery/Phase3A_MEMORY.md` | `PHASE 3/PHASE 3A-Engineering Landscape Discovery/Phase3A_MEMORY.md` |
| ED-13 | `c4b6c4a56bf8ba3066c5b426dce5ae4d50da4774478b5074566e9c79812e3ece` | `COPY PASTE FOLDER/MC_Project_PHASE_DOC.md`<br>`MC_Project_PHASE_DOC.md` | `MC_Project_PHASE_DOC.md` |
| ED-14 | `c52bed09fdfd1a860471bfc6d56cd41411f730362d12ee0348e07ad0939909c9` | `PHASE 1/PHASE 1.A/Phase1A_Summary.md`<br>`every sop and memory/Phase1A_Summary.md` | `PHASE 1/PHASE 1.A/Phase1A_Summary.md` |
| ED-15 | `d200473fd85a3cc910e3532bb2be662e0fcbdeab363fe988a948fd81d129c537` | `PHASE 1/PHASE 1B.5/Phase1B5_Memory.md`<br>`every sop and memory/Phase1B5_Memory.md` | `PHASE 1/PHASE 1B.5/Phase1B5_Memory.md` |
| ED-16 | `d58c91eead60c5abdb4e38c1e9b87c7449f4b3b68ccd7a23f5d4816fea16ff76` | `PHASE 1/PHASE 1.B/Phase1B_Memory.md`<br>`every sop and memory/Phase1B_Memory.md` | `PHASE 1/PHASE 1.B/Phase1B_Memory.md` |
| ED-17 | `e10d76b80c78554ff7e2ea75f3b263bfe82333c54418e7f794d249610f8fe130` | `PHASE 1/PHASE 1.B/Phase1B_Opportunity_Analysis.md`<br>`every sop and memory/Phase1B_Opportunity_Analysis.md` | `PHASE 1/PHASE 1.B/Phase1B_Opportunity_Analysis.md` |
| ED-18 | `e3b320245bc20d4312edc22b62fc9584059111e8fd38442277a3e5544ae019c1` | `PHASE 1/PHASE 1C/Phase1C_Memory.md`<br>`every sop and memory/Phase1C_Memory.md` | `PHASE 1/PHASE 1C/Phase1C_Memory.md` |
| ED-19 | `f520cb5201e299fb0f9185bd2b79318229b898e5a8ad7822deb9a073e8f6cae4` | `COPY PASTE FOLDER/PROJECT_CONCEPT_CONTEXT.md`<br>`PROJECT_CONCEPT_CONTEXT.md` | `PROJECT_CONCEPT_CONTEXT.md` |
| ED-20 | `f9a4184850435aba3ec26e480e802d1ba39f17037f0f368520a625c6f8e84f78` | `COPY PASTE FOLDER/Document_4_TrustLatch_Concept_Dossier.docx`<br>`PHASE 1/PHASE 1C/INDEPTH OF EACH FIVE IDEA/Document_4_TrustLatch_Concept_Dossier.docx` | `PHASE 1/PHASE 1C/INDEPTH OF EACH FIVE IDEA/Document_4_TrustLatch_Concept_Dossier.docx` |

## Cross-format / text-equivalent candidates

### CF-01 — Claude Phase 2 report

- `PHASE 2/Phase2_Report by CLaude.md`
- `PHASE 2/Phase2_Report From Claude.pdf`
- exact Markdown copy at `COPY PASTE FOLDER/Phase2_Report by CLaude.md`

Text was actually extracted and compared. PDF↔Markdown word-trigram Jaccard similarity is **0.9584** and containment is **0.9807**. This is strong evidence that the PDF is a rendered/near-equivalent form of the Markdown, with extraction/formatting differences. Probable canonical editable source: `PHASE 2/Phase2_Report by CLaude.md`; retain the PDF as a presentation derivative if needed.

### CF-02 — Qwen Phase 2 PDF/Markdown

- `PHASE 2/RESEARCH DOCS/QWen Research on Patent.pdf`
- `PHASE 2/RESEARCH DOCS/Qwens Research on Phase 2.md`

Text was extracted and compared. Jaccard similarity is **0.4785**, while **89.55%** of the Markdown’s word trigrams occur in the longer PDF. The PDF is about 160,646 normalized characters; Markdown is about 92,298. They substantially overlap, but are **not equivalent copies**: the Markdown appears to be a subset/variant and requires manual scope comparison. Do not delete or collapse either based on this audit.

### CF-03 — VibeGuard synthesis prompt `.md` / `.mmd`

- `.../vibeguard/claude_synthesis_prompt.md`
- `.../vibeguard/claude_synthesis_prompt.mmd`

Normalized extracted text is identical, but the binaries differ. The `.mmd` extension normally indicates Mermaid content, while this file is a prose synthesis prompt. Probable canonical file: the `.md` version. Manual confirmation is advised before any later cleanup.

## ZIP contents and duplication

Six ZIPs contain **23 members**. **22 of 23** members are byte-identical to normal working-tree files. Archives were listed and streamed for SHA-256 only.

| ZIP | Contained path | Size | Member SHA-256 | Matching normal repository file(s) |
|---|---|---:|---|---|
| `PHASE 1/PHASE 1.B/Phase1B_Opportunity_Analysis.zip` | `Phase1B_Opportunity_Analysis.md` | 5802 | `e10d76b80c78554ff7e2ea75f3b263bfe82333c54418e7f794d249610f8fe130` | `PHASE 1/PHASE 1.B/Phase1B_Opportunity_Analysis.md`<br>`every sop and memory/Phase1B_Opportunity_Analysis.md` |
| `PHASE 1/PHASE 1.B/Phase1B_Opportunity_Analysis.zip` | `Phase1B_Opportunity_Analysis_By_Claude.pdf` | 1484584 | `8e53b914163d8e2685d9edda7422e4c1ac1a01230e60e3a100a0e7ef514dd52c` | `PHASE 1/PHASE 1.B/Phase1B_Opportunity_Analysis_By_Claude.pdf` |
| `PHASE 2/Phase2_docs.zip` | `Phase2_Memory.md` | 7820 | `973519f45bc075c296d4302b94933288496bd9bc12fae708aac1fb7020158ce8` | `COPY PASTE FOLDER/Phase2_Memory.md`<br>`PHASE 2/Phase2_Memory.md` |
| `PHASE 2/Phase2_docs.zip` | `Phase2_Report by CLaude.md` | 44493 | `783729d0e07e725236db5296dae8504ce782c294b8c61cfab40ea172cfa6943e` | `COPY PASTE FOLDER/Phase2_Report by CLaude.md`<br>`PHASE 2/Phase2_Report by CLaude.md` |
| `PHASE 3/PHASE 3A-Engineering Landscape Discovery/phase3B_report_and_summary.zip` | `Claudes report on the research Phases 3a.pdf` | 792034 | `7d0202fb62476a0212e594af473ad8d796eecd853e53e7f0952de90908cec611` | `COPY PASTE FOLDER/Claudes report on the research Phases 3a.pdf`<br>`PHASE 3/PHASE 3A-Engineering Landscape Discovery/Claudes report on the research Phases 3a.pdf` |
| `PHASE 3/PHASE 3A-Engineering Landscape Discovery/phase3B_report_and_summary.zip` | `Phase3A_MEMORY.md` | 8898 | `acd3b4178143ca918ed4cce43d3d853acc994c0178dc8efdc406fb014e1ec997` | `COPY PASTE FOLDER/Phase3A_MEMORY.md`<br>`PHASE 3/PHASE 3A-Engineering Landscape Discovery/Phase3A_MEMORY.md` |
| `PHASE 3/PHASE 3B-Engineering Feasibility Analysis/Phase3B_mem_and_report.zip` | `Phase3B_MEMORY.md` | 18836 | `7b6532c779867e9d6064473de4ba1b4799a0c385361cf27dc4616888fb0ac7ad` | `COPY PASTE FOLDER/Phase3B_MEMORY.md`<br>`PHASE 3/PHASE 3B-Engineering Feasibility Analysis/Phase3B_MEMORY.md` |
| `PHASE 3/PHASE 3B-Engineering Feasibility Analysis/Phase3B_mem_and_report.zip` | `Phase3B_Report_by_Claude.md` | 83718 | `14c19ac85b56e4e27da03de534a2a574ab7220d90005b4a7a0afb868f6390478` | `COPY PASTE FOLDER/Phase3B_Report_by_Claude.md`<br>`PHASE 3/PHASE 3B-Engineering Feasibility Analysis/Phase3B_Report_by_Claude.md` |
| `contexts.zip` | `CHATGPT DEEP RESEARCH.md` | 20670 | `fa41ec5c0504aada478a754133290458a1333eee99542c4530d3fb2abc8f5ac0` | `PHASE 1/PHASE 1.A/RESEARCHS/CHATGPT DEEP RESEARCH.md` |
| `contexts.zip` | `GEMINI DEEP RESEARCH.docx` | 3035520 | `e527fa3ab029f3dd3096184c35f90ccd21e61bd520d9eb677f1031abbebd13ad` | `PHASE 1/PHASE 1.A/RESEARCHS/GEMINI DEEP RESEARCH.docx` |
| `contexts.zip` | `KIMI DEEP RESEARCH.docx` | 64142 | `c0d4cbeb9099d8a58c4fa6eab7e2f06aa1a0bda76affecb9444f040e8169828f` | `PHASE 1/PHASE 1.A/RESEARCHS/KIMI DEEP RESEARCH.docx` |
| `contexts.zip` | `MC_Project_PHASE_DOC.md` | 5872 | `35d5ca312c1e339f7edae9e26f58635762168267b07fd3ae5a6cb25fbd1d7512` | **No binary-identical normal file** |
| `contexts.zip` | `Phase1A_Summary.md` | 2794 | `c52bed09fdfd1a860471bfc6d56cd41411f730362d12ee0348e07ad0939909c9` | `PHASE 1/PHASE 1.A/Phase1A_Summary.md`<br>`every sop and memory/Phase1A_Summary.md` |
| `contexts.zip` | `QWEN AI DEEP RESEARCH.pdf` | 519844 | `5b3f7270de5bc6a27eba0e458cd2f7f40f55dd0407094f70ccfed6f6fd3f7ed8` | `PHASE 1/PHASE 1.A/RESEARCHS/QWEN AI DEEP RESEARCH.pdf` |
| `every sop and memory/every_sop_and memory_from phase 1A to 1C and whoel phase overview.zip` | `MC_Project_PHASE_DOC.md` | 6638 | `e7ebf127dac01b63c87713b14c0bd5cf2d4500e60581cc86f783abe92a525f98` | `every sop and memory/MC_Project_PHASE_DOC.md` |
| `every sop and memory/every_sop_and memory_from phase 1A to 1C and whoel phase overview.zip` | `Phase1A_Memory.md` | 4029 | `5a8943e1e556e1db0644cc7b75e2b4c8000b1a9506d673406c9c70cf7bb4a213` | `PHASE 1/PHASE 1.A/Phase1A_Memory.md`<br>`every sop and memory/Phase1A_Memory.md` |
| `every sop and memory/every_sop_and memory_from phase 1A to 1C and whoel phase overview.zip` | `Phase1A_Summary.md` | 2794 | `c52bed09fdfd1a860471bfc6d56cd41411f730362d12ee0348e07ad0939909c9` | `PHASE 1/PHASE 1.A/Phase1A_Summary.md`<br>`every sop and memory/Phase1A_Summary.md` |
| `every sop and memory/every_sop_and memory_from phase 1A to 1C and whoel phase overview.zip` | `Phase1B5_Memory.md` | 5302 | `d200473fd85a3cc910e3532bb2be662e0fcbdeab363fe988a948fd81d129c537` | `PHASE 1/PHASE 1B.5/Phase1B5_Memory.md`<br>`every sop and memory/Phase1B5_Memory.md` |
| `every sop and memory/every_sop_and memory_from phase 1A to 1C and whoel phase overview.zip` | `Phase1B5_Opportunity_Portfolio_Optimization.md` | 6431 | `305f0f568081ad8a01affc02d252a681f84abde5c23c2a9421fb69369ecc5540` | `PHASE 1/PHASE 1B.5/Phase1B5_Opportunity_Portfolio_Optimization.md`<br>`every sop and memory/Phase1B5_Opportunity_Portfolio_Optimization.md` |
| `every sop and memory/every_sop_and memory_from phase 1A to 1C and whoel phase overview.zip` | `Phase1B_Memory.md` | 3966 | `d58c91eead60c5abdb4e38c1e9b87c7449f4b3b68ccd7a23f5d4816fea16ff76` | `PHASE 1/PHASE 1.B/Phase1B_Memory.md`<br>`every sop and memory/Phase1B_Memory.md` |
| `every sop and memory/every_sop_and memory_from phase 1A to 1C and whoel phase overview.zip` | `Phase1B_Opportunity_Analysis.md` | 5802 | `e10d76b80c78554ff7e2ea75f3b263bfe82333c54418e7f794d249610f8fe130` | `PHASE 1/PHASE 1.B/Phase1B_Opportunity_Analysis.md`<br>`every sop and memory/Phase1B_Opportunity_Analysis.md` |
| `every sop and memory/every_sop_and memory_from phase 1A to 1C and whoel phase overview.zip` | `Phase1C.md` | 3009 | `8e41493ddbc8b8b3c3ad8a00995b6ae3f8a5645351f8086a6b8ded92623853e4` | `PHASE 1/PHASE 1C/Phase1C.md`<br>`every sop and memory/Phase1C.md` |
| `every sop and memory/every_sop_and memory_from phase 1A to 1C and whoel phase overview.zip` | `Phase1C_Memory.md` | 3390 | `e3b320245bc20d4312edc22b62fc9584059111e8fd38442277a3e5544ae019c1` | `PHASE 1/PHASE 1C/Phase1C_Memory.md`<br>`every sop and memory/Phase1C_Memory.md` |

Important exceptions:

- `contexts.zip/MC_Project_PHASE_DOC.md` has no byte-identical normal file and is an older v1-era roadmap.
- All other ZIP members match at least one normal repository file exactly.
- `phase3B_report_and_summary.zip`, located in the Phase 3A folder, contains Phase 3A—not Phase 3B—artifacts. Its filename is inaccurate.

## Non-duplicates worth stating explicitly

- Same-named Gemini, Mistral, Perplexity, Qwen, and ChatGPT files under different concept folders were not grouped merely by name.
- Phase 1 report PDFs and shorter Markdown memories/methodology files showed insufficient extracted-text equivalence and remain separate artifacts.
- Decision Register v1.0 and v1.2 substantially overlap historically but are different versions with materially different decisions; they are not duplicates.
- The failed OpenBraille ChatGPT PDF has negligible overlap with the valid OpenBraille final architecture report and is not valid evidence.


---

## Source 16: `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Legacy_Repository_Audit/04_AUTHORITY_AMBIGUITIES.md`

- Authority: `TIER_1`
- Treatment: `CORE_NARRATIVE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `2af657ba4e6666650bc2c4c44a13c6ba5b87feb292efa1d4a7349c06835b4fc3`

# Source Extraction

- Chapter: `01` — Project Mandate, Requirements and Governance
- Authority tier: `TIER_1`
- Manual treatment: `CORE_NARRATIVE`
- Original source: `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Legacy_Repository_Audit/04_AUTHORITY_AMBIGUITIES.md`
- Current SHA-256: `2af657ba4e6666650bc2c4c44a13c6ba5b87feb292efa1d4a7349c06835b4fc3`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

# Authority Ambiguities

## Applied precedence

1. `PHASE 3/Engineering_Design_Review.md`
2. `Project_mC_Decision_Register_v1.2.md`
3. `PHASE 3/PHASE 3C-Comparative Technical Evaluation/Phase3C_Retained_Portfolio_Closure_Memo.md`
4. Final Phase 3C architecture reports
5. Phase 3C memories
6. Phase 3B report and memory
7. Phase 3A report and memory
8. Phase 2 report and memory
9. Phase 1C synthesis and dossiers
10. Raw independent research

## Confirmed ambiguities and resolutions

### EDR canonical versus convenience copy

`COPY PASTE FOLDER/Engineering_Design_Review.md` is byte-identical to `PHASE 3/Engineering_Design_Review.md`. The Phase 3 path is canonical; the convenience copy has no independent authority.

### Decision Register v1.2 versus v1.0

`Project_mC_Decision_Register_v1.2.md` is the current Level-2 authority. `Project_mC_Decision_Register_v1.0.md.save` and `COPY PASTE FOLDER/Project_mC_Decision_Register_v1.0.md` are byte-identical historical copies. v1.0 says Phase 3C was complete only for OpenBraille/VibeGuard and pending for the other three; v1.2 records TrueMoist completion, TrustLatch/ColdTrace deferral, and PDR-064 through PDR-067. Using v1.0 operationally would resurrect superseded state.

### Phase roadmap status is stale

Root `MC_Project_PHASE_DOC.md` is Version 2.0 (Frozen) and is the probable canonical methodology roadmap, but its progress table says Phase 3 is pending. That status conflicts with the EDR, Register v1.2, and closure memo. Under the defined precedence, those newer authorities control. The roadmap should not be used to infer current phase completion until its status block is corrected through an approved documentation update.

Two older roadmap variants also exist:

- `every sop and memory/MC_Project_PHASE_DOC.md` (older v1.0 content)
- `contexts.zip/MC_Project_PHASE_DOC.md` (another, shorter historical v1.0 variant)

They are historical convenience context, not canonical roadmaps.

### Project concept context versus later decisions

`PROJECT_CONCEPT_CONTEXT.md` calls itself canonical high-level context for all five Phase 1C concepts and says the Phase 1C report is ultimate when ambiguity exists. That remains valid for original concept definitions, but it does not override the later EDR or portfolio decisions. It must not be read as evidence that TrustLatch and ColdTrace remain active.

### Final Phase 3C report locations

- OpenBraille final: `.../openbraille/Claudes report for openbraille phase 3c.md`
- VibeGuard final: `.../vibeguard/research/Phase3C_VibeGuard_Architecture_Report By Claude.md`
- TrueMoist final: `.../TrueMoist/Phase3C_TrueMoist_ChatGPT_Final_Synthesis.md`

All three are Level-4 outputs. VibeGuard’s location among raw research falsely lowers its apparent status; its content and the Decision Register citations confirm that it is a final architecture report.

### Failed OpenBraille research

`.../openbraille/Researches/DEEpr research on phase 3c openbraille by chatgpt` is a PDF containing a generic “Universal Deep Research Framework” for an unspecified topic. It is the known failed/mis-scoped output. It remains Level-10 failed evidence for traceability and must never be promoted, averaged, or cited as valid OpenBraille research.

## Governance discoverability gaps

- `README.md` contains only the project title and does not point readers to the authority order.
- Convenience folders and ZIPs contain no warning that they are non-canonical.
- Many governance citations use only backticked basenames, not relative paths, so similarly named copies are easy to select incorrectly.
- `CURRENT_FOLDER_STRUCTURE.txt` is a snapshot, not authority, and is stale.


---

## Source 17: `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Legacy_Repository_Audit/05_NAMING_AND_PLACEMENT_ISSUES.md`

- Authority: `TIER_1`
- Treatment: `CORE_NARRATIVE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `3cb55e747e4d7b47b7af61a78c627db0ee3cd274618ee32af01ba4e37303176e`

# Source Extraction

- Chapter: `01` — Project Mandate, Requirements and Governance
- Authority tier: `TIER_1`
- Manual treatment: `CORE_NARRATIVE`
- Original source: `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Legacy_Repository_Audit/05_NAMING_AND_PLACEMENT_ISSUES.md`
- Current SHA-256: `3cb55e747e4d7b47b7af61a78c627db0ee3cd274618ee32af01ba4e37303176e`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

# Naming and Placement Issues

## Material issues

| Path | Finding | Impact | Priority |
|---|---|---|---|
| `.../vibeguard/research/Phase3C_VibeGuard_Architecture_Report By Claude.md` | Final Level-4 report is inside raw-research folder. | Authority and discoverability risk. | Mandatory correction after approval |
| `.../openbraille/Researches/DEEpr research on phase 3c openbraille by chatgpt` | File is actually PDF, lacks extension, name does not identify failed/generic content. | Tooling, security triage, and evidence-validity risk. | Mandatory correction after approval |
| `.../PHASE 3A.../phase3B_report_and_summary.zip` | Contains `Claudes report on the research Phases 3a.pdf` and `Phase3A_MEMORY.md`. | Filename falsely says Phase 3B. | Mandatory correction after approval |
| `Project_mC_Decision_Register_v1.0.md.save` | Historical register has editor-backup suffix rather than a clear historical label. | May be mistaken for recovery debris or current authority. | Mandatory labeling correction |
| `CURRENT_FOLDER_STRUCTURE.txt` | Lists absent `key.txt` and cannot distinguish empty `main/` from a file; predates audit guidance/v1.2 state. | Misleading inventory/security snapshot. | Mandatory regeneration after approved cleanup |
| `PHASE 2/RESEARCH DOCS/QWen Research on Patent.pdf` and `Qwens Research on Phase 2.md` | Substantial but non-equivalent overlap; inconsistent names conceal that Markdown is likely a subset. | Duplicate/scope ambiguity. | Manual review before renaming |
| `PHASE 2/Phase2_Report From Claude.pdf` versus `Phase2_Report by CLaude.md` | Near-equivalent cross-format pair uses inconsistent wording/capitalization. | Minor canonical-format ambiguity. | Label derivative; no deletion |
| `.../vibeguard/claude_synthesis_prompt.mmd` | Extracted prose is text-identical to `.md`; `.mmd` conventionally implies Mermaid. | Misleading extension. | Manual confirmation, then optional removal from active set or rename |

## Inconsistent research folder names

- `PHASE 1/PHASE 1.A/RESEARCHS/`
- `PHASE 2/RESEARCH DOCS/`
- `.../openbraille/Researches/`
- `.../vibeguard/research/`
- `.../TrueMoist/Research/`

These are inconsistent but understandable. Normalizing all of them is cosmetic and would cause link/path churn. Defer unless the owner approves a narrow Phase 3C-only normalization.

## Other naming inconsistencies

- Concept directory casing differs: `openbraille`, `vibeguard`, `TrueMoist`.
- Phase labels differ: `PHASE 1.A`, `PHASE 1.B`, `PHASE 1B.5`, and verbose Phase 3 names.
- Numerous typos exist: `Reearch`, `Rsearch`, `RESEAARCH`, `researon`, `reserach`, `whoel`, `CHATGT`, and inconsistent `QWen/Qwen/QWEN`.
- `Claudes report for openbraille phase 3c.md` is authoritative but its conversational name does not say “Architecture Report.”
- `COPY PASTE FOLDER` and `every sop and memory` describe convenience usage informally rather than signaling non-authority.

These are discoverability issues, not evidence of duplication. Bulk renaming is not recommended.

## Link result

No actual Markdown or HTML local links were found, hence none tested as broken. Filename mentions inside backticks are plain text references. If approved moves occur later, update those references even though they are not clickable links.

## Names that misdescribe content

- The failed OpenBraille ChatGPT output describes a universal research method, not OpenBraille.
- `phase3B_report_and_summary.zip` contains Phase 3A files.
- The `.mmd` VibeGuard file contains prose prompt content, not a Mermaid diagram.
- `CURRENT_FOLDER_STRUCTURE.txt` is not current.
- Root `MC_Project_PHASE_DOC.md` is “Frozen” methodology but its progress table is not current project state; the filename itself is acceptable, while the status content needs controlled correction.


---

## Source 18: `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Legacy_Repository_Audit/06_SECURITY_AND_UNKNOWN_FILES.md`

- Authority: `TIER_1`
- Treatment: `CORE_NARRATIVE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `e341c54c577ba5bc7f04b97d7c3d11d59dace003914cbd9df3f8995d15977afe`

# Source Extraction

- Chapter: `01` — Project Mandate, Requirements and Governance
- Authority tier: `TIER_1`
- Manual treatment: `CORE_NARRATIVE`
- Original source: `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Legacy_Repository_Audit/06_SECURITY_AND_UNKNOWN_FILES.md`
- Current SHA-256: `e341c54c577ba5bc7f04b97d7c3d11d59dace003914cbd9df3f8995d15977afe`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

# Security and Unknown Files

## `main`

The repository root currently contains `main` as an **empty directory**, not an extensionless file:

- Type: directory
- Size reported by `stat`: 0 bytes (directory entry; not file content)
- Mode: `0755` (`drwxr-xr-x`)
- Executable file: no
- SHA-256: not applicable to a directory
- Contents: none
- Git tracking: not tracked (Git does not track empty directories)
- Execution performed: none

Therefore it cannot be classified as text, data, binary, or executable file. `CURRENT_FOLDER_STRUCTURE.txt` visually lists it as a tree entry and the project guidance calls it a file, suggesting the snapshot/guidance reflects an earlier or mistaken state. No path named `main` was found in current Git refs or commit history. Manual review should determine whether the empty directory has any intended purpose; do not execute anything later placed there without inspection.

## Extensionless OpenBraille file

`PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Researches/DEEpr research on phase 3c openbraille by chatgpt`

- File type: PDF document, version 1.7
- Size: 151219 bytes
- SHA-256: `864e400d3b259157346319b53eb36868b28bf183fb6ac5a1efbcbb6315424e06`
- Executable permission: no
- Classification: document/data (PDF), not an executable
- Content finding: generic “Universal Deep Research Framework,” mis-scoped for OpenBraille

It should be preserved as failed research but clearly labeled and given a `.pdf` extension after approval.

## `key.txt`

- Current filesystem: absent
- Current Git index: not tracked
- All current refs/tags/branches: no `key.txt`
- Commit history: no recorded `key.txt`
- `.gitignore`: `key.txt` appears three times

No credential content was exposed or copied. Because ignored files do not appear in ordinary Git status, future security checks should use a direct filesystem existence test as this audit did. The three duplicate ignore entries are harmless but should be reduced to one in a later approved edit.

## Credential-marker scan

No working-tree filenames matched common sensitive-name patterns (`*key*`, `*secret*`, `*.pem`, `*.env`, `*credential*`). A filename-only Git content scan found no files containing common private-key headers or representative AWS, GitHub, or OpenAI token formats. This is a limited heuristic, not a guarantee that documents contain no confidential information.

## Executables and unknown formats

- No audited file had executable permission.
- `file` identified no ELF binaries, scripts with executable permission, or unknown binary executables.
- Six ZIP files passed archive integrity/listing checks; none was executed or extracted into the repository.
- All DOCX packages passed integrity checks.
- The only misleading extension case is the extensionless PDF described above.

## Security disposition

No active credential file or executable threat was found. The material risks are discoverability and future misuse: the ignored `key.txt` path could hide a local secret from Git status, the stale structure snapshot implies absent artifacts exist, and the failed PDF’s missing extension makes quick classification harder.


---

## Source 19: `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Legacy_Repository_Audit/07_MINIMAL_CLEANUP_PROPOSAL.md`

- Authority: `TIER_1`
- Treatment: `CORE_NARRATIVE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `a4ced05912df7c4a17f117039e8ae12b73601bf12bda2a2a28b0640f5beaafab`

# Source Extraction

- Chapter: `01` — Project Mandate, Requirements and Governance
- Authority tier: `TIER_1`
- Manual treatment: `CORE_NARRATIVE`
- Original source: `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Legacy_Repository_Audit/07_MINIMAL_CLEANUP_PROPOSAL.md`
- Current SHA-256: `a4ced05912df7c4a17f117039e8ae12b73601bf12bda2a2a28b0640f5beaafab`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

# Minimal Cleanup Proposal

## Governing approach

Preserve the existing Phase 1 / Phase 2 / Phase 3 hierarchy. Do not merge documents merely because names or extracted text are similar. Treat convenience collections as packages, not canonical sources. Every approved move should use `git mv`, be recorded in `REORGANIZATION_LOG.md`, and be followed by reference/link checks.

No proposal below was executed.

## Mandatory corrections (after explicit owner approval)

### 1. Move the VibeGuard final architecture report out of raw research

`PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/research/Phase3C_VibeGuard_Architecture_Report By Claude.md`
→ `PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/Phase3C_VibeGuard_Architecture_Report_By_Claude.md`

Reason: it is a Level-4 final architecture report cited by the latest Decision Register, not raw evidence.

### 2. Label and restore the extension of failed OpenBraille research

`PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Researches/DEEpr research on phase 3c openbraille by chatgpt`
→ `PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Researches/FAILED_ChatGPT_Generic_Deep_Research_Framework.pdf`

Reason: preserve methodology traceability while preventing accidental use as OpenBraille evidence.

### 3. Correct the Phase 3A ZIP’s inaccurate name

`PHASE 3/PHASE 3A-Engineering Landscape Discovery/phase3B_report_and_summary.zip`
→ `PHASE 3/PHASE 3A-Engineering Landscape Discovery/Phase3A_report_and_memory.zip`

Reason: both archive members are Phase 3A artifacts.

### 4. Clearly label the historical Decision Register

`Project_mC_Decision_Register_v1.0.md.save`
→ `Project_mC_Decision_Register_v1.0_HISTORICAL.md`

Reason: v1.2 is authoritative; `.save` is ambiguous. Preserve all PDR identifiers and content unchanged.

### 5. Add authority notices without restructuring

Create short notice/README files in `COPY PASTE FOLDER/` and `every sop and memory/`, and a root archive note for ZIPs, stating that these are convenience/context packages and linking to canonical paths. Do not move their existing contents merely to enforce visual tidiness.

### 6. Correct stale navigation/security metadata

- Regenerate `CURRENT_FOLDER_STRUCTURE.txt` after approved moves; explicitly distinguish `main/` as a directory and omit absent `key.txt`.
- Reduce `.gitignore`’s three identical `key.txt` lines to one.
- Expand root `README.md` with the authority order and direct canonical paths.
- Update only the progress/status block of `MC_Project_PHASE_DOC.md` through a controlled owner-approved edit; do not rewrite methodology or technical conclusions.
- Add an explicit “historical/superseded” banner to retained v1.0 Register copies if they remain readily visible.

These are content edits, not path mappings.

## Mandatory manual review before any consolidation

### Phase 2 Qwen formats

Keep both files until a reviewer maps sections and determines why the Markdown is substantially shorter:

`PHASE 2/RESEARCH DOCS/QWen Research on Patent.pdf`
→ no move proposed yet

`PHASE 2/RESEARCH DOCS/Qwens Research on Phase 2.md`
→ no move proposed yet

If the Markdown is confirmed as an excerpt, rename it to say so; if it is a revision, add version metadata. Do not delete either based on similarity alone.

### Claude Phase 2 formats

Treat `Phase2_Report by CLaude.md` as the editable canonical source and `Phase2_Report From Claude.pdf` as the rendered companion. Retain both if both formats are useful; a small sidecar note is enough. No move is required.

### VibeGuard `.md` / `.mmd` prompt

The extracted text is identical. Confirm whether `.mmd` has any intended tool-specific use. If not, preserve it in history and remove it from the active working set only under a separately approved, recoverable cleanup; no deletion is authorized by this audit.

## Optional cosmetic renaming — defer by default

These changes improve consistency but do not solve authority or security problems. Undertake only as a single approved batch with reference updates:

`.../openbraille/Researches/` → `.../openbraille/research/`
`.../TrueMoist/Research/` → `.../TrueMoist/research/`
`.../PHASE 3C.../openbraille/` → `.../PHASE 3C.../OpenBraille/`
`.../PHASE 3C.../vibeguard/` → `.../PHASE 3C.../VibeGuard/`

Individual typo corrections (`Reearch`, `Rsearch`, `reserach`, etc.) are also optional. Avoid wholesale Phase 1 folder renaming; the existing hierarchy is owner-designed and understandable.

## Convenience archive policy

- Keep canonical normal files in their existing phase paths.
- Mark ZIPs and convenience folders as non-canonical.
- Do not delete ZIPs merely because 22 of 23 archive members match normal files.
- Record that `contexts.zip` includes a unique older `MC_Project_PHASE_DOC.md` snapshot; preserve it as historical context, not current governance.
- Consider moving convenience ZIPs only if the owner later approves a dedicated archival policy; this audit does not propose a replacement folder structure.

## Empty `main/` directory

Confirm intent. If it is accidental, the owner may remove the empty directory later; Git does not track it and there is no project-file content to preserve. No action was taken and no execution was attempted.

## Recommended order

1. Approve the four material path mappings.
2. Create `REORGANIZATION_LOG.md` and record each approved mapping.
3. Execute approved moves with `git mv`.
4. Add authority notices and minimal governance/status corrections.
5. Update basename references and check links.
6. Re-run hashes/manifest checks.
7. Consider cosmetic renaming only if discoverability remains a real problem.


---

## Source 20: `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Naming_History/PHASE3C_NAMING_CHANGE_LOG.md`

- Authority: `TIER_1`
- Treatment: `CORE_NARRATIVE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `adda533db7e29f86a39f97c517ad9afd47337b6b5edda11571d57f0895923b23`

# Source Extraction

- Chapter: `01` — Project Mandate, Requirements and Governance
- Authority tier: `TIER_1`
- Manual treatment: `CORE_NARRATIVE`
- Original source: `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Naming_History/PHASE3C_NAMING_CHANGE_LOG.md`
- Current SHA-256: `adda533db7e29f86a39f97c517ad9afd47337b6b5edda11571d57f0895923b23`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

# Phase 3C Naming Change Log

**Date:** 2026-07-29
**Scope:** `PHASE 3/PHASE 3C-Comparative Technical Evaluation/`
**Status:** Completed; not committed

Every move or rename below was performed with `git mv`. Collision checks confirmed that every final and temporary destination was absent before use. No file was deleted or merged.

The “before” hash is the SHA-256 at the original path. The “after” hash is the final SHA-256 after permitted operational reference updates. Files marked as reference-edited differ only because affected filename/path references were updated; raw research was never edited.

## Case-only temporary paths used

1. `.../openbraille/` → `.../__tmp_OpenBraille_case__/` → `.../OpenBraille/`
2. `.../vibeguard/` → `.../__tmp_VibeGuard_case__/` → `.../VibeGuard/`
3. `.../TrueMoist/Research/` → `.../TrueMoist/__tmp_research_case__/` → `.../TrueMoist/research/`
4. `.../TrueMoist/Phase3C_TrueMoist_MEMORY_Final.md` → `.../TrueMoist/__tmp_Memory_case__.md` → `.../TrueMoist/Phase3C_TrueMoist_Memory_Final.md`

No temporary path remains.

## File mappings

| Old path | Temporary/intermediate path(s) | Final path | Reason | SHA-256 before | SHA-256 after | Action status |
|---|---|---|---|---|---|---|
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/Phase3C_Retained_Portfolio_Closure_Memo.md` | — | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/Phase3C_Portfolio_Closure_Memo_Approved.md` | Portfolio closure memo standardized. | `3c6e6f568c06099251b4b71d4f35cf668ee23a40c8214c95e4a12fe36cf4845a` | `3c6e6f568c06099251b4b71d4f35cf668ee23a40c8214c95e4a12fe36cf4845a` | Completed with `git mv`; content hash unchanged |
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Claudes report for openbraille phase 3c.md` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/__tmp_OpenBraille_case__/Claudes report for openbraille phase 3c.md` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/OpenBraille/Phase3C_OpenBraille_Architecture_Report_Final.md` | Final architecture report standardized. | `0e6c40edc6fd79c17f6bcac8e6d1598217ff7cadbdbf721ea55e4c39d4d36aa8` | `84c658ba992d729027b1f931f8c20715f5deecf385b78e767e4c32e2b83354e1` | Completed with `git mv`; approved operational filename-reference update changed final hash |
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Phase3C_OpenBraille_Memory.md` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/__tmp_OpenBraille_case__/Phase3C_OpenBraille_Memory.md` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/OpenBraille/Phase3C_OpenBraille_Memory_Final.md` | Final memory standardized. | `5dad0e392cf9c64d7e8f29be09fadb70acde5b965b95744fa066b5f4b4fd30eb` | `5dad0e392cf9c64d7e8f29be09fadb70acde5b965b95744fa066b5f4b4fd30eb` | Completed with `git mv`; content hash unchanged |
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Phase3C_OpenBraille_SOP.md` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/__tmp_OpenBraille_case__/Phase3C_OpenBraille_SOP.md` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/OpenBraille/Phase3C_OpenBraille_SOP_Final.md` | Final SOP standardized. | `bfee5dc46675d77b318f4a0d4fe864d77a570a1150cc2676a5dd10103f214e50` | `bfee5dc46675d77b318f4a0d4fe864d77a570a1150cc2676a5dd10103f214e50` | Completed with `git mv`; content hash unchanged |
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Phase3C_OpenBraille_DeepResearch_Prompt.md` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/__tmp_OpenBraille_case__/Phase3C_OpenBraille_DeepResearch_Prompt.md` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/OpenBraille/prompts/Phase3C_OpenBraille_Deep_Research_Prompt_Final.md` | Deep research prompt moved to prompts. | `a59b4743782e0e21e1472b28b116a1bf83a2ede098a28e8d5110a8ab1ce33e42` | `a59b4743782e0e21e1472b28b116a1bf83a2ede098a28e8d5110a8ab1ce33e42` | Completed with `git mv`; content hash unchanged |
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Phase3C_OpenBraille_Claude_Synthesis_Prompt.md` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/__tmp_OpenBraille_case__/Phase3C_OpenBraille_Claude_Synthesis_Prompt.md` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/OpenBraille/prompts/Phase3C_OpenBraille_Synthesis_Prompt_Claude.md` | Claude synthesis prompt moved to prompts. | `2cd7dbdabb86f93a69ebfc012a5518fdb814529999c44f68c4252a19f5b8cf04` | `7b0ebdef37e932e8d252b397c6fc92010cce79b6805874b1b264dfa171e911d8` | Completed with `git mv`; approved operational filename-reference update changed final hash |
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Researches/FAILED_ChatGPT_Generic_Deep_Research_Framework.pdf` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/__tmp_OpenBraille_case__/Researches/FAILED_ChatGPT_Generic_Deep_Research_Framework.pdf`<br>`PHASE 3/PHASE 3C-Comparative Technical Evaluation/OpenBraille/Researches/FAILED_ChatGPT_Generic_Deep_Research_Framework.pdf` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/OpenBraille/research/Phase3C_OpenBraille_Failed_Research_ChatGPT.pdf` | Failed research standardized. | `864e400d3b259157346319b53eb36868b28bf183fb6ac5a1efbcbb6315424e06` | `864e400d3b259157346319b53eb36868b28bf183fb6ac5a1efbcbb6315424e06` | Completed with `git mv`; content hash unchanged |
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Researches/gemini research on phase 3c.docx` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/__tmp_OpenBraille_case__/Researches/gemini research on phase 3c.docx`<br>`PHASE 3/PHASE 3C-Comparative Technical Evaluation/OpenBraille/Researches/gemini research on phase 3c.docx` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/OpenBraille/research/Phase3C_OpenBraille_Raw_Research_Gemini.docx` | Raw research standardized. | `a1d2b01cdbaa412c79251ffec0b7fad9e606aa16609a664a88b6ebd8149b8b7c` | `a1d2b01cdbaa412c79251ffec0b7fad9e606aa16609a664a88b6ebd8149b8b7c` | Completed with `git mv`; content hash unchanged |
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Researches/mistral research on phase 3c.md` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/__tmp_OpenBraille_case__/Researches/mistral research on phase 3c.md`<br>`PHASE 3/PHASE 3C-Comparative Technical Evaluation/OpenBraille/Researches/mistral research on phase 3c.md` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/OpenBraille/research/Phase3C_OpenBraille_Raw_Research_Mistral.md` | Raw research standardized. | `aff5ebe5ff1fedfc5cc52cb9ef52d6b742ea495ff5304eb5acedaa8ff7e21c83` | `aff5ebe5ff1fedfc5cc52cb9ef52d6b742ea495ff5304eb5acedaa8ff7e21c83` | Completed with `git mv`; content hash unchanged |
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Researches/Perplexity research on phase 3C.docx` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/__tmp_OpenBraille_case__/Researches/Perplexity research on phase 3C.docx`<br>`PHASE 3/PHASE 3C-Comparative Technical Evaluation/OpenBraille/Researches/Perplexity research on phase 3C.docx` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/OpenBraille/research/Phase3C_OpenBraille_Raw_Research_Perplexity.docx` | Raw research standardized. | `6350e11ac346e30fbb3ca252a40367e4394bfcf1cf9e1f2ad8c84fcf1bf3545d` | `6350e11ac346e30fbb3ca252a40367e4394bfcf1cf9e1f2ad8c84fcf1bf3545d` | Completed with `git mv`; content hash unchanged |
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Researches/qwen Research on phase 3C.md` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/__tmp_OpenBraille_case__/Researches/qwen Research on phase 3C.md`<br>`PHASE 3/PHASE 3C-Comparative Technical Evaluation/OpenBraille/Researches/qwen Research on phase 3C.md` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/OpenBraille/research/Phase3C_OpenBraille_Raw_Research_Qwen.md` | Raw research standardized. | `3416c5526a1c73e5b29acf0117d45b4a5ee86cc1391eb9a105ca6710d0048f2b` | `3416c5526a1c73e5b29acf0117d45b4a5ee86cc1391eb9a105ca6710d0048f2b` | Completed with `git mv`; content hash unchanged |
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/Phase3C_VibeGuard_Architecture_Report_By_Claude.md` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/__tmp_VibeGuard_case__/Phase3C_VibeGuard_Architecture_Report_By_Claude.md` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/VibeGuard/Phase3C_VibeGuard_Architecture_Report_Final.md` | Final architecture report standardized. | `d6a5f009d5c96bceb6cc0cb2f4d70817204e7346e7f6e7c21a5e86b457254573` | `ba7d1824fe1ab260be903aead8d9bac00cee83141b6f7728d0e220b65fd8eeb4` | Completed with `git mv`; approved operational filename-reference update changed final hash |
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/Phase3C_VibeGuard_Memory.md` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/__tmp_VibeGuard_case__/Phase3C_VibeGuard_Memory.md` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/VibeGuard/Phase3C_VibeGuard_Memory_Final.md` | Final memory standardized. | `3d07fdb1b9b2c0c273dacf3b49650e2deb6fa72a36af38035c85118e3fd51960` | `e4b96f7ee53bbc94ec960db281a1a56745fc6c8121133b813ca37b76798da5e5` | Completed with `git mv`; approved operational filename-reference update changed final hash |
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/vibeguard_sop.md` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/__tmp_VibeGuard_case__/vibeguard_sop.md` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/VibeGuard/Phase3C_VibeGuard_SOP_Final.md` | Final SOP standardized. | `e073729670896e004900fdb52c049819d78d4b597f7da08e62c54de1152f7e0c` | `6386bf6d73bbbbb7127c568692ba09abcbdf6dc4cbac40a97690b4edb0dca974` | Completed with `git mv`; approved operational filename-reference update changed final hash |
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/Phase3C_VibeGuard_DeepResearch_Prompt.md` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/__tmp_VibeGuard_case__/Phase3C_VibeGuard_DeepResearch_Prompt.md` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/VibeGuard/prompts/Phase3C_VibeGuard_Deep_Research_Prompt_Final.md` | Deep research prompt moved to prompts. | `af08518f2c65bc8a53ff2520775415d2fd7f3bd5da2fc7e37018ae96a0c412d6` | `af08518f2c65bc8a53ff2520775415d2fd7f3bd5da2fc7e37018ae96a0c412d6` | Completed with `git mv`; content hash unchanged |
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/claude_synthesis_prompt.md` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/__tmp_VibeGuard_case__/claude_synthesis_prompt.md` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/VibeGuard/prompts/Phase3C_VibeGuard_Synthesis_Prompt_Claude.md` | Claude synthesis prompt moved to prompts. | `26b50889394442be4fb22e26fad74b6ca97c7e5765f330b92b241ff8e69c1a2e` | `26b50889394442be4fb22e26fad74b6ca97c7e5765f330b92b241ff8e69c1a2e` | Completed with `git mv`; content hash unchanged |
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/claude_synthesis_prompt.mmd` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/__tmp_VibeGuard_case__/claude_synthesis_prompt.mmd` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/VibeGuard/prompts/Phase3C_VibeGuard_Synthesis_Prompt_Claude.mmd` | Claude synthesis prompt MMD preserved and moved. | `59ae97bd4407b3e18cb2fb9ac99abdeeaf9aa3fdc3f5cb5e6f8ea67f330da47e` | `59ae97bd4407b3e18cb2fb9ac99abdeeaf9aa3fdc3f5cb5e6f8ea67f330da47e` | Completed with `git mv`; content hash unchanged |
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/research/gemini research on phase 3c.docx` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/__tmp_VibeGuard_case__/research/gemini research on phase 3c.docx` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/VibeGuard/research/Phase3C_VibeGuard_Raw_Research_Gemini.docx` | Raw research standardized. | `39a249ed0b0c9d76b0372e558b04d47a837b6a1849848f84fa9bf88f1ade0921` | `39a249ed0b0c9d76b0372e558b04d47a837b6a1849848f84fa9bf88f1ade0921` | Completed with `git mv`; content hash unchanged |
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/research/mistral reserach on phase 3c.md` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/__tmp_VibeGuard_case__/research/mistral reserach on phase 3c.md` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/VibeGuard/research/Phase3C_VibeGuard_Raw_Research_Mistral.md` | Raw research standardized. | `86efffd004de1dd811343d0d6def5c8955189f66aa56af244f6b5d2d4dacc355` | `86efffd004de1dd811343d0d6def5c8955189f66aa56af244f6b5d2d4dacc355` | Completed with `git mv`; content hash unchanged |
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/research/Perplexity research on phase 3c.md` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/__tmp_VibeGuard_case__/research/Perplexity research on phase 3c.md` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/VibeGuard/research/Phase3C_VibeGuard_Raw_Research_Perplexity.md` | Raw research standardized. | `0b1a2ea090cbc3630e84f4c4902e307e72751ca531f85bfe473285f74f4df368` | `0b1a2ea090cbc3630e84f4c4902e307e72751ca531f85bfe473285f74f4df368` | Completed with `git mv`; content hash unchanged |
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/research/qwens research on phase 3c.md` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/__tmp_VibeGuard_case__/research/qwens research on phase 3c.md` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/VibeGuard/research/Phase3C_VibeGuard_Raw_Research_Qwen.md` | Raw research standardized. | `a16b18b36f221d2a3f4de53d65068de3bb20d253e0d550c60c7735b30ae19f4d` | `a16b18b36f221d2a3f4de53d65068de3bb20d253e0d550c60c7735b30ae19f4d` | Completed with `git mv`; content hash unchanged |
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_ChatGPT_Final_Synthesis.md` | — | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_Architecture_Report_Final.md` | Final architecture report standardized. | `6c71f1d618e0575d127b10f05e91d06ea4b1f0b8a2fe63e78d4022ee75234610` | `6c71f1d618e0575d127b10f05e91d06ea4b1f0b8a2fe63e78d4022ee75234610` | Completed with `git mv`; content hash unchanged |
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_MEMORY_Final.md` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/__tmp_Memory_case__.md` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_Memory_Final.md` | Final memory casing standardized. | `ba8264d74f37168e5de85a5d76adb354062dc5e47b692b12f76f73aac62c7377` | `c84bc0e08c8c96cfe410d8c690df35c6b7996e5ffda7703ceff37a424bf02df1` | Completed with `git mv`; approved operational filename-reference update changed final hash |
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_SOP.md` | — | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_SOP_Final.md` | Final SOP standardized. | `993caf1a05f3fdc3937efb634e2f2e467488e973eb71454db8e3c3f53d178d00` | `993caf1a05f3fdc3937efb634e2f2e467488e973eb71454db8e3c3f53d178d00` | Completed with `git mv`; content hash unchanged |
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_PDR_Update_Patch.md` | — | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_PDR_Patch_Historical.md` | Historical PDR patch standardized. | `f9b23506c0b78a76ac590fa7bb80911c1a416569eb17c41644b2cfd9b432a803` | `fd2965c371701c137897cda021885bce46e5b6b0c0d2e14126d6903c7078b3a1` | Completed with `git mv`; approved operational filename-reference update changed final hash |
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_DeepResearch_Prompt.md` | — | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/prompts/Phase3C_TrueMoist_Deep_Research_Prompt_Final.md` | Deep research prompt moved to prompts. | `da66d2b9259a007d390b7fdc2766b9349bf88497cd60af3bc0c5e6855cddd08e` | `da66d2b9259a007d390b7fdc2766b9349bf88497cd60af3bc0c5e6855cddd08e` | Completed with `git mv`; content hash unchanged |
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_Final_Synthesis_Prompt.md` | — | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/prompts/Phase3C_TrueMoist_Synthesis_Prompt_Final.md` | Final synthesis prompt moved to prompts. | `144617f2efe8ef6db6122d00039fcc3566d8aab03649e003837eea5c0a60618e` | `144617f2efe8ef6db6122d00039fcc3566d8aab03649e003837eea5c0a60618e` | Completed with `git mv`; content hash unchanged |
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Research/TrueMoist Phase 3C  Research By chatgpt.pdf` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/__tmp_research_case__/TrueMoist Phase 3C  Research By chatgpt.pdf` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/research/Phase3C_TrueMoist_Raw_Research_ChatGPT.pdf` | Raw research standardized. | `87ccbd3416f3f7bb58e544095a1e20560f9561ffe72db82f868d17bf942812e7` | `87ccbd3416f3f7bb58e544095a1e20560f9561ffe72db82f868d17bf942812e7` | Completed with `git mv`; content hash unchanged |
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Research/TrueMoist  3C Gemini REsearch.docx` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/__tmp_research_case__/TrueMoist  3C Gemini REsearch.docx` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/research/Phase3C_TrueMoist_Raw_Research_Gemini.docx` | Raw research standardized. | `b0eab8009831f5b719bf9d20ad1f25e9bcc549fc260a078a5be2531dc86e5b24` | `b0eab8009831f5b719bf9d20ad1f25e9bcc549fc260a078a5be2531dc86e5b24` | Completed with `git mv`; content hash unchanged |
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Research/phase-3c-truemoist-Research-Mistral.md` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/__tmp_research_case__/phase-3c-truemoist-Research-Mistral.md` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/research/Phase3C_TrueMoist_Raw_Research_Mistral.md` | Raw research standardized. | `706d9ae47b256de0bb01d2836c3b24095b4109fd6c1011491aa88d32799fd1c5` | `706d9ae47b256de0bb01d2836c3b24095b4109fd6c1011491aa88d32799fd1c5` | Completed with `git mv`; content hash unchanged |
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Research/TrueMoist Phase 3C By Perplexity.md` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/__tmp_research_case__/TrueMoist Phase 3C By Perplexity.md` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/research/Phase3C_TrueMoist_Raw_Research_Perplexity.md` | Raw research standardized. | `caefe1da05e1963e0cd9c3916fc50d4c2e4b396006cdf39ebf8eee893f0c3187` | `caefe1da05e1963e0cd9c3916fc50d4c2e4b396006cdf39ebf8eee893f0c3187` | Completed with `git mv`; content hash unchanged |

## Totals

- Files mapped: **31**
- Hash-identical after completion: **24**
- Files with permitted operational reference-only edits: **7**
- Raw/failed research content edits: **0**
- Deleted or merged files: **0**


---

## Source 21: `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Naming_History/PHASE3C_NAMING_PROPOSAL.md`

- Authority: `TIER_1`
- Treatment: `CORE_NARRATIVE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `9a0a1bfc7a1c3867fa6eea536e7ec288bbec4a0e1289333976d6f025b24fe811`

# Source Extraction

- Chapter: `01` — Project Mandate, Requirements and Governance
- Authority tier: `TIER_1`
- Manual treatment: `CORE_NARRATIVE`
- Original source: `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Naming_History/PHASE3C_NAMING_PROPOSAL.md`
- Current SHA-256: `9a0a1bfc7a1c3867fa6eea536e7ec288bbec4a0e1289333976d6f025b24fe811`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

# Phase 3C Naming Proposal

**Scope:** `PHASE 3/PHASE 3C-Comparative Technical Evaluation/` only
**Mode:** Naming audit and proposal only; no directory or file was renamed, moved, edited, deleted, or merged.

## Proposed convention

Use:

```text
Phase3C_<Concept>_<DocumentType>_<SourceOrStatus>.<extension>
```

Controlled values proposed here:

- `<Concept>`: `OpenBraille`, `VibeGuard`, `TrueMoist`, or `Portfolio` for the cross-concept closure memo.
- `<DocumentType>`:
  - `ArchitectureReport`
  - `Memory`
  - `SOP`
  - `DeepResearchPrompt`
  - `SynthesisPrompt`
  - `RawResearch`
  - `FailedResearch`
  - `PDRPatch`
  - `ClosureMemo`
- `<SourceOrStatus>`:
  - `Final` for completed authoritative/supporting project artifacts;
  - `Approved` for the approved portfolio closure memo;
  - the source name (`Claude`, `Gemini`, `Mistral`, `Perplexity`, `Qwen`, `ChatGPT`) for prompts and independent research.

The convention deliberately keeps the original extension. It does not assert cross-format equivalence and does not authorize consolidation.

## Proposed directory names

| Current directory | Proposed directory | Reason | Risk | Classification |
|---|---|---|---|---|
| `.../openbraille/` | `.../OpenBraille/` | Standard concept casing. | **High:** case-only rename; unsafe as a one-step operation on case-insensitive filesystems. Use a unique temporary directory and two `git mv` operations if approved. | Cosmetic |
| `.../vibeguard/` | `.../VibeGuard/` | Standard concept casing. | **High:** case-only rename; use a unique temporary directory and two `git mv` operations. | Cosmetic |
| `.../TrueMoist/` | unchanged | Already uses standard concept casing. | Low. | No change |
| `.../openbraille/Researches/` | `.../OpenBraille/research/` | Standard raw-research folder name; removes plural inconsistency. | Medium: parent is also case-renamed; sequence operations carefully. | Cosmetic |
| `.../vibeguard/research/` | `.../VibeGuard/research/` | Folder name already standard; only parent casing changes. | High only because of parent case-only rename. | Cosmetic |
| `.../TrueMoist/Research/` | `.../TrueMoist/research/` | Standard raw-research folder casing. | **High:** case-only rename; use a unique temporary directory and two `git mv` operations. | Cosmetic |

`CURRENT_FOLDER_STRUCTURE.txt` must be regenerated after any approved naming implementation. Root README links and all path-bearing references identified below must then be updated.

## Portfolio-level file

| Current path | Proposed path | Reason | Authority level | References requiring update | Risk | Mandatory or cosmetic |
|---|---|---|---|---|---|---|
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/Phase3C_Retained_Portfolio_Closure_Memo.md` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/Phase3C_Portfolio_ClosureMemo_Approved.md` | Fits the convention and makes cross-concept scope and approved status explicit. | Level 3 — retained-portfolio closure memo | `AGENTS.md:48`; `README.md:28,44`; `CURRENT_FOLDER_STRUCTURE.txt:127`. Historical audit mention: `REPOSITORY_AUDIT/04_AUTHORITY_AMBIGUITIES.md:7`. | Medium: high-authority path used by governance/navigation. | Mandatory for the proposed system |

## OpenBraille files

All proposed paths below use `.../OpenBraille/` and `.../OpenBraille/research/`.

| Current path | Proposed path | Reason | Authority level | References requiring update | Risk | Mandatory or cosmetic |
|---|---|---|---|---|---|---|
| `.../openbraille/Claudes report for openbraille phase 3c.md` | `.../OpenBraille/Phase3C_OpenBraille_ArchitectureReport_Final.md` | Identifies the Level-4 artifact as the final architecture report rather than a conversational “Claude report.” | Level 4 — final Phase 3C architecture report | `Project_mC_Decision_Register_v1.2.md:162,383,397,411,425,439,453,467,482,965`; `README.md:48`; `CURRENT_FOLDER_STRUCTURE.txt:110`. Historical v1.0 and convenience-register mentions should be reviewed under historical-record policy, not silently rewritten. | High: many PDR source-evidence references. | Mandatory |
| `.../openbraille/Phase3C_OpenBraille_Claude_Synthesis_Prompt.md` | `.../OpenBraille/Phase3C_OpenBraille_SynthesisPrompt_Claude.md` | Standard prompt document type and source ordering. | Supporting Phase 3C prompt | `Project_mC_Decision_Register_v1.2.md:965`; `CURRENT_FOLDER_STRUCTURE.txt:111`. Historical v1.0 and convenience-register references also exist. | Medium. | Cosmetic |
| `.../openbraille/Phase3C_OpenBraille_DeepResearch_Prompt.md` | `.../OpenBraille/Phase3C_OpenBraille_DeepResearchPrompt_Final.md` | Standard prompt tokenization and completed status. | Supporting Phase 3C prompt | `CURRENT_FOLDER_STRUCTURE.txt:112`. | Low. | Cosmetic |
| `.../openbraille/Phase3C_OpenBraille_Memory.md` | `.../OpenBraille/Phase3C_OpenBraille_Memory_Final.md` | Aligns memory status with the completed Phase 3C portfolio. | Level 5 — Phase 3C memory | `Project_mC_Decision_Register_v1.2.md:383,397,411,425,439,453,482`; `README.md:54`; `CURRENT_FOLDER_STRUCTURE.txt:113`; current synthesis prompt line 790; current architecture report line 323. Historical v1.0 and convenience-register references also exist. | High: multiple current PDR and internal references. | Mandatory |
| `.../openbraille/Phase3C_OpenBraille_SOP.md` | `.../OpenBraille/Phase3C_OpenBraille_SOP_Final.md` | Makes the completed SOP status explicit. | Phase 3C methodology/SOP | `CURRENT_FOLDER_STRUCTURE.txt:114`; current Mistral raw research line 1172. | Medium: raw-research text contains a filename reference. | Cosmetic |
| `.../openbraille/Researches/FAILED_ChatGPT_Generic_Deep_Research_Framework.pdf` | `.../OpenBraille/research/Phase3C_OpenBraille_FailedResearch_ChatGPT.pdf` | Preserves failed evidence while making phase, concept, role, and source explicit. | Level 10 — failed/mis-scoped research; excluded as valid evidence | `CURRENT_FOLDER_STRUCTURE.txt:105`. Historical cleanup records in `REORGANIZATION_LOG.md`, `CLEANUP_VALIDATION_REPORT.md`, and `REPOSITORY_AUDIT/07_MINIMAL_CLEANUP_PROPOSAL.md` should normally retain the path they recorded. | Medium: prior cleanup history intentionally records the current path. | Mandatory |
| `.../openbraille/Researches/Perplexity research on phase 3C.docx` | `.../OpenBraille/research/Phase3C_OpenBraille_RawResearch_Perplexity.docx` | Standard raw-research role and source. | Level 10 — raw research | `CURRENT_FOLDER_STRUCTURE.txt:106`. | Low. | Cosmetic |
| `.../openbraille/Researches/gemini research on phase 3c.docx` | `.../OpenBraille/research/Phase3C_OpenBraille_RawResearch_Gemini.docx` | Standard raw-research role/source; removes ambiguous same-name collision with VibeGuard. | Level 10 — raw research | `CURRENT_FOLDER_STRUCTURE.txt:107` (basename also matches VibeGuard at line 118; update by full path, not blind replacement). | Medium: identical basename exists under VibeGuard. | Cosmetic |
| `.../openbraille/Researches/mistral research on phase 3c.md` | `.../OpenBraille/research/Phase3C_OpenBraille_RawResearch_Mistral.md` | Standard raw-research role and source. | Level 10 — raw research | `CURRENT_FOLDER_STRUCTURE.txt:108`. | Low. | Cosmetic |
| `.../openbraille/Researches/qwen Research on phase 3C.md` | `.../OpenBraille/research/Phase3C_OpenBraille_RawResearch_Qwen.md` | Standard raw-research role and source. | Level 10 — raw research | `CURRENT_FOLDER_STRUCTURE.txt:109`. | Low. | Cosmetic |

## VibeGuard files

All proposed paths below use `.../VibeGuard/` and `.../VibeGuard/research/`.

| Current path | Proposed path | Reason | Authority level | References requiring update | Risk | Mandatory or cosmetic |
|---|---|---|---|---|---|---|
| `.../vibeguard/Phase3C_VibeGuard_Architecture_Report_By_Claude.md` | `.../VibeGuard/Phase3C_VibeGuard_ArchitectureReport_Final.md` | Standard architecture-report token and authoritative final status. | Level 4 — final Phase 3C architecture report | `Project_mC_Decision_Register_v1.2.md:497,511,525,539,553,567,581,595,609,623,951,965`; `README.md:49`; `CURRENT_FOLDER_STRUCTURE.txt:121`. Cleanup/audit records should normally retain historical mappings. | High: many current PDR source-evidence references. | Mandatory |
| `.../vibeguard/Phase3C_VibeGuard_DeepResearch_Prompt.md` | `.../VibeGuard/Phase3C_VibeGuard_DeepResearchPrompt_Final.md` | Standard prompt tokenization and completed status. | Supporting Phase 3C prompt | `CURRENT_FOLDER_STRUCTURE.txt:122`; current VibeGuard SOP line 489. | Medium. | Cosmetic |
| `.../vibeguard/Phase3C_VibeGuard_Memory.md` | `.../VibeGuard/Phase3C_VibeGuard_Memory_Final.md` | Makes completed memory status explicit. | Level 5 — Phase 3C memory | `Project_mC_Decision_Register_v1.2.md:497,581,595,609,623`; `README.md:55`; `CURRENT_FOLDER_STRUCTURE.txt:123`; current SOP line 493; current Mistral raw research line 1255. Historical v1.0 and convenience-register references also exist. | High. | Mandatory |
| `.../vibeguard/claude_synthesis_prompt.md` | `.../VibeGuard/Phase3C_VibeGuard_SynthesisPrompt_Claude.md` | Standard phase/concept/document/source naming. | Supporting Phase 3C prompt | `CURRENT_FOLDER_STRUCTURE.txt:124`. Historical audit mention: `REPOSITORY_AUDIT/03_DUPLICATE_REPORT.md:57`. | Medium: paired with a text-identical `.mmd`; do not merge. | Cosmetic |
| `.../vibeguard/claude_synthesis_prompt.mmd` | `.../VibeGuard/Phase3C_VibeGuard_SynthesisPrompt_Claude.mmd` | Standardizes the basename while preserving the separate file and extension. | Supporting Phase 3C prompt/alternate representation | `CURRENT_FOLDER_STRUCTURE.txt:125`. Historical audit mentions: `REPOSITORY_AUDIT/03_DUPLICATE_REPORT.md:58`, `REPOSITORY_AUDIT/05_NAMING_AND_PLACEMENT_ISSUES.md:14`. | **High:** `.mmd` usually implies Mermaid, while prior audit found prose identical to `.md`; manual tool-use review required. No merge authorized. | Cosmetic, manual review first |
| `.../vibeguard/vibeguard_sop.md` | `.../VibeGuard/Phase3C_VibeGuard_SOP_Final.md` | Standard phase/concept/SOP/status naming. | Phase 3C methodology/SOP | `Project_mC_Decision_Register_v1.2.md:950`; `CURRENT_FOLDER_STRUCTURE.txt:126`; current memory lines 27,81,90; current architecture report lines 6,21,160. Historical v1.0 and convenience-register references also exist. | High: internal and governance references. | Mandatory |
| `.../vibeguard/research/Perplexity research on phase 3c.md` | `.../VibeGuard/research/Phase3C_VibeGuard_RawResearch_Perplexity.md` | Standard raw-research role and source. | Level 10 — raw research | `CURRENT_FOLDER_STRUCTURE.txt:117`. | Low. | Cosmetic |
| `.../vibeguard/research/gemini research on phase 3c.docx` | `.../VibeGuard/research/Phase3C_VibeGuard_RawResearch_Gemini.docx` | Standard raw-research role/source; removes ambiguous same-name collision with OpenBraille. | Level 10 — raw research | `CURRENT_FOLDER_STRUCTURE.txt:118` (basename also matches OpenBraille at line 107; update by full path). | Medium: identical basename exists under OpenBraille. | Cosmetic |
| `.../vibeguard/research/mistral reserach on phase 3c.md` | `.../VibeGuard/research/Phase3C_VibeGuard_RawResearch_Mistral.md` | Standard raw-research role/source and corrects filename typo only. | Level 10 — raw research | `CURRENT_FOLDER_STRUCTURE.txt:119`. | Low. | Cosmetic |
| `.../vibeguard/research/qwens research on phase 3c.md` | `.../VibeGuard/research/Phase3C_VibeGuard_RawResearch_Qwen.md` | Standard raw-research role and source spelling. | Level 10 — raw research | `CURRENT_FOLDER_STRUCTURE.txt:120`. | Low. | Cosmetic |

## TrueMoist files

All proposed raw-research paths below use `.../TrueMoist/research/`.

| Current path | Proposed path | Reason | Authority level | References requiring update | Risk | Mandatory or cosmetic |
|---|---|---|---|---|---|---|
| `.../TrueMoist/Phase3C_TrueMoist_ChatGPT_Final_Synthesis.md` | `.../TrueMoist/Phase3C_TrueMoist_ArchitectureReport_Final.md` | Identifies the authoritative synthesis by its Level-4 role rather than model source. | Level 4 — final Phase 3C architecture/synthesis report | `Project_mC_Decision_Register_v1.2.md:250,351,638,651,664,677,691,705,719,733,747,761`; `README.md:50`; `CURRENT_FOLDER_STRUCTURE.txt:97`; current memory line 6; current PDR patch line 6. Historical audit mention: `REPOSITORY_AUDIT/04_AUTHORITY_AMBIGUITIES.md:45`. | High: many current PDR references. | Mandatory |
| `.../TrueMoist/Phase3C_TrueMoist_DeepResearch_Prompt.md` | `.../TrueMoist/Phase3C_TrueMoist_DeepResearchPrompt_Final.md` | Standard prompt tokenization and completed status. | Supporting Phase 3C prompt | `CURRENT_FOLDER_STRUCTURE.txt:98`. | Low. | Cosmetic |
| `.../TrueMoist/Phase3C_TrueMoist_Final_Synthesis_Prompt.md` | `.../TrueMoist/Phase3C_TrueMoist_SynthesisPrompt_Final.md` | Standard document-type ordering. | Supporting Phase 3C prompt | `CURRENT_FOLDER_STRUCTURE.txt:99`. | Low. | Cosmetic |
| `.../TrueMoist/Phase3C_TrueMoist_MEMORY_Final.md` | `.../TrueMoist/Phase3C_TrueMoist_Memory_Final.md` | Standard token casing without changing status. | Level 5 — Phase 3C memory | `Project_mC_Decision_Register_v1.2.md:638,691,705,733,747,761`; `README.md:56`; `CURRENT_FOLDER_STRUCTURE.txt:100`. | **High:** filename change is case-only (`MEMORY`→`Memory`) on a case-insensitive filesystem; use a temporary name. | Mandatory |
| `.../TrueMoist/Phase3C_TrueMoist_PDR_Update_Patch.md` | `.../TrueMoist/Phase3C_TrueMoist_PDRPatch_Final.md` | Clearly identifies the document as a PDR patch while fitting the convention. | Supporting historical PDR patch; not the current Decision Register | `CURRENT_FOLDER_STRUCTURE.txt:101`. | Low. | Cosmetic |
| `.../TrueMoist/Phase3C_TrueMoist_SOP.md` | `.../TrueMoist/Phase3C_TrueMoist_SOP_Final.md` | Makes completed SOP status explicit. | Phase 3C methodology/SOP | `CURRENT_FOLDER_STRUCTURE.txt:13,102`; current Perplexity raw research line 821. Historical exact-copy/audit references also exist. | Medium: convenience copy has the same basename and must not be blindly renamed or edited. | Cosmetic |
| `.../TrueMoist/Research/TrueMoist  3C Gemini REsearch.docx` | `.../TrueMoist/research/Phase3C_TrueMoist_RawResearch_Gemini.docx` | Standard raw-research role/source and removes spacing/capitalization errors. | Level 10 — raw research | `CURRENT_FOLDER_STRUCTURE.txt:93`. | Medium because parent folder rename is case-only. | Cosmetic |
| `.../TrueMoist/Research/TrueMoist Phase 3C  Research By chatgpt.pdf` | `.../TrueMoist/research/Phase3C_TrueMoist_RawResearch_ChatGPT.pdf` | Standard raw-research role/source and removes double spaces. | Level 10 — raw research | `CURRENT_FOLDER_STRUCTURE.txt:94`. | Medium because parent folder rename is case-only. | Cosmetic |
| `.../TrueMoist/Research/TrueMoist Phase 3C By Perplexity.md` | `.../TrueMoist/research/Phase3C_TrueMoist_RawResearch_Perplexity.md` | Standard raw-research role and source. | Level 10 — raw research | `CURRENT_FOLDER_STRUCTURE.txt:95`. | Medium because parent folder rename is case-only. | Cosmetic |
| `.../TrueMoist/Research/phase-3c-truemoist-Research-Mistral.md` | `.../TrueMoist/research/Phase3C_TrueMoist_RawResearch_Mistral.md` | Standard raw-research role/source and separator style. | Level 10 — raw research | `CURRENT_FOLDER_STRUCTURE.txt:96`. | Medium because parent folder rename is case-only. | Cosmetic |

## Reference-update policy if approved

### Operational references that should be updated

- `README.md`
- `AGENTS.md` where it names the closure memo path
- `Project_mC_Decision_Register_v1.2.md`, changing only source-evidence filenames
- Internal Phase 3C filename/path references in SOPs, memories, prompts, reports, raw-research text, and the TrueMoist PDR patch
- `CURRENT_FOLDER_STRUCTURE.txt`, by regeneration after all approved changes

### Historical records that should not be blindly rewritten

- `Project_mC_Decision_Register_v1.0_HISTORICAL.md`
- `COPY PASTE FOLDER/Project_mC_Decision_Register_v1.0.md`
- `REORGANIZATION_LOG.md`
- `CLEANUP_VALIDATION_REPORT.md`
- `REPOSITORY_AUDIT/`

These record earlier names or historical decisions. If the owner wants current-path annotations, add them explicitly rather than replacing historical evidence silently.

## Case-insensitive filesystem safety

The following are case-only renames and must not be attempted as a single rename on case-insensitive filesystems:

1. `openbraille/` → `OpenBraille/`
2. `vibeguard/` → `VibeGuard/`
3. `TrueMoist/Research/` → `TrueMoist/research/`
4. `Phase3C_TrueMoist_MEMORY_Final.md` → `Phase3C_TrueMoist_Memory_Final.md`

If approved, use collision-free temporary paths, for example:

```text
git mv openbraille __tmp_OpenBraille
git mv __tmp_OpenBraille OpenBraille
```

Use a different unique temporary name for each operation, verify the destination does not exist, and record both steps in the reorganization log. Directory renames should occur before final file renames or be planned as one explicit mapping set to avoid path ambiguity.

## Summary

- Files inventoried: **31**
- Portfolio-level file: **1**
- OpenBraille files: **10**
- VibeGuard files: **10**
- TrueMoist files: **10**
- Proposed content changes: **none**
- Proposed deletions/merges: **none**
- Case-only operations requiring special handling: **4**

The highest-value mandatory changes are the names of the three final architecture reports, the three memories, the VibeGuard SOP, the failed OpenBraille research file, and the approved closure memo. Directory casing and most raw-research filename normalization are cosmetic; they should be approved as a single bounded batch or deferred together.


---

## Source 22: `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Naming_History/PHASE3C_NAMING_VALIDATION_REPORT.md`

- Authority: `TIER_1`
- Treatment: `CORE_NARRATIVE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `02e3c811b70d3fb0b4f92e784b499093de190dd4c0992987f7da8739bc307353`

# Source Extraction

- Chapter: `01` — Project Mandate, Requirements and Governance
- Authority tier: `TIER_1`
- Manual treatment: `CORE_NARRATIVE`
- Original source: `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Naming_History/PHASE3C_NAMING_VALIDATION_REPORT.md`
- Current SHA-256: `02e3c811b70d3fb0b4f92e784b499093de190dd4c0992987f7da8739bc307353`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

# Phase 3C Naming Validation Report

**Date:** 2026-07-29
**Scope:** Bounded Phase 3C naming cleanup
**Commit created:** No

## Result

The approved Phase 3C naming standard was implemented for all 31 pre-existing Phase 3C files. One Phase 3C navigation README was added. No file was deleted or merged.

## Validation checklist

### 1. All approved old paths are absent — PASS

All 31 source paths recorded in `PHASE3C_NAMING_CHANGE_LOG.md` were tested after the moves. None exists.

### 2. All approved final paths exist — PASS

All 31 final paths exist as files. The three `prompts/` directories and three standardized `research/` directories exist.

### 3. File content and hash preservation — PASS WITH DOCUMENTED REFERENCE UPDATES

- Immediately after all `git mv` operations and before editing references, all 31 files matched their original SHA-256 hashes.
- At final validation, 24 files remain byte-identical.
- Seven operational Phase 3C documents have new hashes solely because approved filename references were updated.
- For each of those seven files, reversing only the approved basename substitutions produces a byte-for-byte match with the original file.
- All 13 raw/failed research files retain their original SHA-256 hashes.

This is the necessary, documented exception to literal final hash equality: operational references had to be updated, while technical content remained unchanged. Before/after hashes for every file are recorded in `PHASE3C_NAMING_CHANGE_LOG.md`.

### 4. No files deleted or merged — PASS

- Original Phase 3C files mapped: 31
- Final mapped Phase 3C files: 31
- New Phase 3C navigation file: 1
- VibeGuard synthesis prompts preserved separately:
  - `VibeGuard/prompts/Phase3C_VibeGuard_Synthesis_Prompt_Claude.md`
  - `VibeGuard/prompts/Phase3C_VibeGuard_Synthesis_Prompt_Claude.mmd`
- Deleted files: 0
- Merged files: 0

### 5. Root and Phase 3C README links resolve — PASS

Every local Markdown link in `README.md` and `PHASE 3/PHASE 3C-Comparative Technical Evaluation/README.md` resolves to an existing target.

### 6. No stale old names remain in operational documents — PASS WITH ONE PROTECTED LITERAL

No stale old filename remains in root navigation, AGENTS navigation, current PDR source-evidence fields, Phase 3C final reports, memories, SOP navigation references, prompts, or the TrueMoist historical patch.

One old literal, `vibeguard_sop.md`, remains in the **rationale** of PDR-038 in Decision Register v1.2. It was intentionally preserved because the cleanup explicitly prohibited changing PDR rationale and allowed only source-evidence filename changes. Raw research may also retain old filenames as part of its immutable original content.

The naming proposal, naming change log, validation report, historical registers, convenience copies, prior audits, and prior cleanup logs intentionally retain old paths as historical records.

### 7. Historical records retain original path history — PASS

No diff exists for:

- `Project_mC_Decision_Register_v1.0_HISTORICAL.md`
- `COPY PASTE FOLDER/`
- `every sop and memory/`
- `REPOSITORY_AUDIT/`
- `REORGANIZATION_LOG.md`
- `CLEANUP_VALIDATION_REPORT.md`

### 8. PDR v1.2 has 67 unique Decision IDs — PASS

- Decision ID entries: 67
- Unique Decision IDs: 67
- Duplicate Decision IDs: none

### 9. PDR decisions, rationale, statuses, and numbering unchanged — PASS

Removing `**Source evidence:**` lines from the baseline and current Decision Register produces byte-identical text. Therefore all non-source-evidence content—including decisions, rationales, statuses, identifiers, and numbering—remains unchanged.

### 10. `git diff --check` — PASS

The command exits successfully with no whitespace errors.

### 11. Case-only renames used temporary paths — PASS

The following collision-free paths were used and are recorded in the naming change log:

- `__tmp_OpenBraille_case__`
- `__tmp_VibeGuard_case__`
- `TrueMoist/__tmp_research_case__`
- `TrueMoist/__tmp_Memory_case__.md`

No temporary path remains.

### 12. No unexpected modifications outside scope — PASS

Outside the Phase 3C subtree, the only modified operational files are:

- `README.md`
- `AGENTS.md`
- `Project_mC_Decision_Register_v1.2.md`
- `CURRENT_FOLDER_STRUCTURE.txt`

The only new root files are the requested naming change log and validation report. `PHASE3C_NAMING_PROPOSAL.md` remains unchanged.

## Operational reference edits

Only filename/path references were updated in:

- `AGENTS.md`
- `README.md`
- `Project_mC_Decision_Register_v1.2.md` source-evidence fields only
- OpenBraille final architecture report
- OpenBraille Claude synthesis prompt
- VibeGuard final architecture report
- VibeGuard final memory
- VibeGuard final SOP
- TrueMoist final memory
- TrueMoist historical PDR patch navigation reference

No raw independent research content was edited.

## Deviations

No unauthorized deviation occurred. The final hashes of seven operational documents differ from their pre-rename hashes only because the user-required operational reference updates were applied; reverse-substitution validation proves the remaining content is byte-identical.

## Final Git outputs

### `git status --short`

```text
 M AGENTS.md
 M CURRENT_FOLDER_STRUCTURE.txt
RM "PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Claudes report for openbraille phase 3c.md" -> "PHASE 3/PHASE 3C-Comparative Technical Evaluation/OpenBraille/Phase3C_OpenBraille_Architecture_Report_Final.md"
R  "PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Phase3C_OpenBraille_Memory.md" -> "PHASE 3/PHASE 3C-Comparative Technical Evaluation/OpenBraille/Phase3C_OpenBraille_Memory_Final.md"
R  "PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Phase3C_OpenBraille_SOP.md" -> "PHASE 3/PHASE 3C-Comparative Technical Evaluation/OpenBraille/Phase3C_OpenBraille_SOP_Final.md"
R  "PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Phase3C_OpenBraille_DeepResearch_Prompt.md" -> "PHASE 3/PHASE 3C-Comparative Technical Evaluation/OpenBraille/prompts/Phase3C_OpenBraille_Deep_Research_Prompt_Final.md"
RM "PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Phase3C_OpenBraille_Claude_Synthesis_Prompt.md" -> "PHASE 3/PHASE 3C-Comparative Technical Evaluation/OpenBraille/prompts/Phase3C_OpenBraille_Synthesis_Prompt_Claude.md"
R  "PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Researches/FAILED_ChatGPT_Generic_Deep_Research_Framework.pdf" -> "PHASE 3/PHASE 3C-Comparative Technical Evaluation/OpenBraille/research/Phase3C_OpenBraille_Failed_Research_ChatGPT.pdf"
R  "PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Researches/gemini research on phase 3c.docx" -> "PHASE 3/PHASE 3C-Comparative Technical Evaluation/OpenBraille/research/Phase3C_OpenBraille_Raw_Research_Gemini.docx"
R  "PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Researches/mistral research on phase 3c.md" -> "PHASE 3/PHASE 3C-Comparative Technical Evaluation/OpenBraille/research/Phase3C_OpenBraille_Raw_Research_Mistral.md"
R  "PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Researches/Perplexity research on phase 3C.docx" -> "PHASE 3/PHASE 3C-Comparative Technical Evaluation/OpenBraille/research/Phase3C_OpenBraille_Raw_Research_Perplexity.docx"
R  "PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Researches/qwen Research on phase 3C.md" -> "PHASE 3/PHASE 3C-Comparative Technical Evaluation/OpenBraille/research/Phase3C_OpenBraille_Raw_Research_Qwen.md"
R  "PHASE 3/PHASE 3C-Comparative Technical Evaluation/Phase3C_Retained_Portfolio_Closure_Memo.md" -> "PHASE 3/PHASE 3C-Comparative Technical Evaluation/Phase3C_Portfolio_Closure_Memo_Approved.md"
R  "PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_ChatGPT_Final_Synthesis.md" -> "PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_Architecture_Report_Final.md"
RM "PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_MEMORY_Final.md" -> "PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_Memory_Final.md"
RM "PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_PDR_Update_Patch.md" -> "PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_PDR_Patch_Historical.md"
R  "PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_SOP.md" -> "PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_SOP_Final.md"
R  "PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_DeepResearch_Prompt.md" -> "PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/prompts/Phase3C_TrueMoist_Deep_Research_Prompt_Final.md"
R  "PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_Final_Synthesis_Prompt.md" -> "PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/prompts/Phase3C_TrueMoist_Synthesis_Prompt_Final.md"
R  "PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Research/TrueMoist Phase 3C  Research By chatgpt.pdf" -> "PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/research/Phase3C_TrueMoist_Raw_Research_ChatGPT.pdf"
R  "PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Research/TrueMoist  3C Gemini REsearch.docx" -> "PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/research/Phase3C_TrueMoist_Raw_Research_Gemini.docx"
R  "PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Research/phase-3c-truemoist-Research-Mistral.md" -> "PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/research/Phase3C_TrueMoist_Raw_Research_Mistral.md"
R  "PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Research/TrueMoist Phase 3C By Perplexity.md" -> "PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/research/Phase3C_TrueMoist_Raw_Research_Perplexity.md"
RM "PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/Phase3C_VibeGuard_Architecture_Report_By_Claude.md" -> "PHASE 3/PHASE 3C-Comparative Technical Evaluation/VibeGuard/Phase3C_VibeGuard_Architecture_Report_Final.md"
RM "PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/Phase3C_VibeGuard_Memory.md" -> "PHASE 3/PHASE 3C-Comparative Technical Evaluation/VibeGuard/Phase3C_VibeGuard_Memory_Final.md"
RM "PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/vibeguard_sop.md" -> "PHASE 3/PHASE 3C-Comparative Technical Evaluation/VibeGuard/Phase3C_VibeGuard_SOP_Final.md"
R  "PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/Phase3C_VibeGuard_DeepResearch_Prompt.md" -> "PHASE 3/PHASE 3C-Comparative Technical Evaluation/VibeGuard/prompts/Phase3C_VibeGuard_Deep_Research_Prompt_Final.md"
R  "PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/claude_synthesis_prompt.md" -> "PHASE 3/PHASE 3C-Comparative Technical Evaluation/VibeGuard/prompts/Phase3C_VibeGuard_Synthesis_Prompt_Claude.md"
R  "PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/claude_synthesis_prompt.mmd" -> "PHASE 3/PHASE 3C-Comparative Technical Evaluation/VibeGuard/prompts/Phase3C_VibeGuard_Synthesis_Prompt_Claude.mmd"
R  "PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/research/gemini research on phase 3c.docx" -> "PHASE 3/PHASE 3C-Comparative Technical Evaluation/VibeGuard/research/Phase3C_VibeGuard_Raw_Research_Gemini.docx"
R  "PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/research/mistral reserach on phase 3c.md" -> "PHASE 3/PHASE 3C-Comparative Technical Evaluation/VibeGuard/research/Phase3C_VibeGuard_Raw_Research_Mistral.md"
R  "PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/research/Perplexity research on phase 3c.md" -> "PHASE 3/PHASE 3C-Comparative Technical Evaluation/VibeGuard/research/Phase3C_VibeGuard_Raw_Research_Perplexity.md"
R  "PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/research/qwens research on phase 3c.md" -> "PHASE 3/PHASE 3C-Comparative Technical Evaluation/VibeGuard/research/Phase3C_VibeGuard_Raw_Research_Qwen.md"
 M Project_mC_Decision_Register_v1.2.md
 M README.md
?? "PHASE 3/PHASE 3C-Comparative Technical Evaluation/README.md"
?? PHASE3C_NAMING_CHANGE_LOG.md
?? PHASE3C_NAMING_VALIDATION_REPORT.md
```

### `git diff HEAD --name-status`

```text
M	AGENTS.md
M	CURRENT_FOLDER_STRUCTURE.txt
R099	PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Claudes report for openbraille phase 3c.md	PHASE 3/PHASE 3C-Comparative Technical Evaluation/OpenBraille/Phase3C_OpenBraille_Architecture_Report_Final.md
R100	PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Phase3C_OpenBraille_Memory.md	PHASE 3/PHASE 3C-Comparative Technical Evaluation/OpenBraille/Phase3C_OpenBraille_Memory_Final.md
R100	PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Phase3C_OpenBraille_SOP.md	PHASE 3/PHASE 3C-Comparative Technical Evaluation/OpenBraille/Phase3C_OpenBraille_SOP_Final.md
R100	PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Phase3C_OpenBraille_DeepResearch_Prompt.md	PHASE 3/PHASE 3C-Comparative Technical Evaluation/OpenBraille/prompts/Phase3C_OpenBraille_Deep_Research_Prompt_Final.md
R099	PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Phase3C_OpenBraille_Claude_Synthesis_Prompt.md	PHASE 3/PHASE 3C-Comparative Technical Evaluation/OpenBraille/prompts/Phase3C_OpenBraille_Synthesis_Prompt_Claude.md
R100	PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Researches/FAILED_ChatGPT_Generic_Deep_Research_Framework.pdf	PHASE 3/PHASE 3C-Comparative Technical Evaluation/OpenBraille/research/Phase3C_OpenBraille_Failed_Research_ChatGPT.pdf
R100	PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Researches/gemini research on phase 3c.docx	PHASE 3/PHASE 3C-Comparative Technical Evaluation/OpenBraille/research/Phase3C_OpenBraille_Raw_Research_Gemini.docx
R100	PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Researches/mistral research on phase 3c.md	PHASE 3/PHASE 3C-Comparative Technical Evaluation/OpenBraille/research/Phase3C_OpenBraille_Raw_Research_Mistral.md
R100	PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Researches/Perplexity research on phase 3C.docx	PHASE 3/PHASE 3C-Comparative Technical Evaluation/OpenBraille/research/Phase3C_OpenBraille_Raw_Research_Perplexity.docx
R100	PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Researches/qwen Research on phase 3C.md	PHASE 3/PHASE 3C-Comparative Technical Evaluation/OpenBraille/research/Phase3C_OpenBraille_Raw_Research_Qwen.md
R100	PHASE 3/PHASE 3C-Comparative Technical Evaluation/Phase3C_Retained_Portfolio_Closure_Memo.md	PHASE 3/PHASE 3C-Comparative Technical Evaluation/Phase3C_Portfolio_Closure_Memo_Approved.md
R100	PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_ChatGPT_Final_Synthesis.md	PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_Architecture_Report_Final.md
R098	PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_MEMORY_Final.md	PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_Memory_Final.md
R099	PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_PDR_Update_Patch.md	PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_PDR_Patch_Historical.md
R100	PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_SOP.md	PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_SOP_Final.md
R100	PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_DeepResearch_Prompt.md	PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/prompts/Phase3C_TrueMoist_Deep_Research_Prompt_Final.md
R100	PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_Final_Synthesis_Prompt.md	PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/prompts/Phase3C_TrueMoist_Synthesis_Prompt_Final.md
R100	PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Research/TrueMoist Phase 3C  Research By chatgpt.pdf	PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/research/Phase3C_TrueMoist_Raw_Research_ChatGPT.pdf
R100	PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Research/TrueMoist  3C Gemini REsearch.docx	PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/research/Phase3C_TrueMoist_Raw_Research_Gemini.docx
R100	PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Research/phase-3c-truemoist-Research-Mistral.md	PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/research/Phase3C_TrueMoist_Raw_Research_Mistral.md
R100	PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Research/TrueMoist Phase 3C By Perplexity.md	PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/research/Phase3C_TrueMoist_Raw_Research_Perplexity.md
R097	PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/Phase3C_VibeGuard_Architecture_Report_By_Claude.md	PHASE 3/PHASE 3C-Comparative Technical Evaluation/VibeGuard/Phase3C_VibeGuard_Architecture_Report_Final.md
R089	PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/Phase3C_VibeGuard_Memory.md	PHASE 3/PHASE 3C-Comparative Technical Evaluation/VibeGuard/Phase3C_VibeGuard_Memory_Final.md
R099	PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/vibeguard_sop.md	PHASE 3/PHASE 3C-Comparative Technical Evaluation/VibeGuard/Phase3C_VibeGuard_SOP_Final.md
R100	PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/Phase3C_VibeGuard_DeepResearch_Prompt.md	PHASE 3/PHASE 3C-Comparative Technical Evaluation/VibeGuard/prompts/Phase3C_VibeGuard_Deep_Research_Prompt_Final.md
R100	PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/claude_synthesis_prompt.md	PHASE 3/PHASE 3C-Comparative Technical Evaluation/VibeGuard/prompts/Phase3C_VibeGuard_Synthesis_Prompt_Claude.md
R100	PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/claude_synthesis_prompt.mmd	PHASE 3/PHASE 3C-Comparative Technical Evaluation/VibeGuard/prompts/Phase3C_VibeGuard_Synthesis_Prompt_Claude.mmd
R100	PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/research/gemini research on phase 3c.docx	PHASE 3/PHASE 3C-Comparative Technical Evaluation/VibeGuard/research/Phase3C_VibeGuard_Raw_Research_Gemini.docx
R100	PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/research/mistral reserach on phase 3c.md	PHASE 3/PHASE 3C-Comparative Technical Evaluation/VibeGuard/research/Phase3C_VibeGuard_Raw_Research_Mistral.md
R100	PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/research/Perplexity research on phase 3c.md	PHASE 3/PHASE 3C-Comparative Technical Evaluation/VibeGuard/research/Phase3C_VibeGuard_Raw_Research_Perplexity.md
R100	PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/research/qwens research on phase 3c.md	PHASE 3/PHASE 3C-Comparative Technical Evaluation/VibeGuard/research/Phase3C_VibeGuard_Raw_Research_Qwen.md
M	Project_mC_Decision_Register_v1.2.md
M	README.md
```

### `git diff --stat`

```text
 AGENTS.md                                          |   2 +-
 CURRENT_FOLDER_STRUCTURE.txt                       |  78 ++++++++++++---------
 ...ase3C_OpenBraille_Architecture_Report_Final.md} |   2 +-
 .../Phase3C_OpenBraille_Memory_Final.md}           |   0
 .../Phase3C_OpenBraille_SOP_Final.md}              |   0
 ...se3C_OpenBraille_Deep_Research_Prompt_Final.md} |   0
 ...Phase3C_OpenBraille_Synthesis_Prompt_Claude.md} |   2 +-
 ...hase3C_OpenBraille_Failed_Research_ChatGPT.pdf} | Bin
 .../Phase3C_OpenBraille_Raw_Research_Gemini.docx}  | Bin
 .../Phase3C_OpenBraille_Raw_Research_Mistral.md}   |   0
 ...ase3C_OpenBraille_Raw_Research_Perplexity.docx} | Bin
 .../Phase3C_OpenBraille_Raw_Research_Qwen.md}      |   0
 ... => Phase3C_Portfolio_Closure_Memo_Approved.md} |   0
 ...Phase3C_TrueMoist_Architecture_Report_Final.md} |   0
 ..._Final.md => Phase3C_TrueMoist_Memory_Final.md} |   2 +-
 ...d => Phase3C_TrueMoist_PDR_Patch_Historical.md} |   2 +-
 ...Moist_SOP.md => Phase3C_TrueMoist_SOP_Final.md} |   0
 ...hase3C_TrueMoist_Deep_Research_Prompt_Final.md} |   0
 .../Phase3C_TrueMoist_Synthesis_Prompt_Final.md}   |   0
 .../Phase3C_TrueMoist_Raw_Research_ChatGPT.pdf}    | Bin
 .../Phase3C_TrueMoist_Raw_Research_Gemini.docx}    | Bin
 .../Phase3C_TrueMoist_Raw_Research_Mistral.md}     |   0
 .../Phase3C_TrueMoist_Raw_Research_Perplexity.md}  |   0
 ...Phase3C_VibeGuard_Architecture_Report_Final.md} |   6 +-
 .../Phase3C_VibeGuard_Memory_Final.md}             |   6 +-
 .../Phase3C_VibeGuard_SOP_Final.md}                |   4 +-
 ...hase3C_VibeGuard_Deep_Research_Prompt_Final.md} |   0
 .../Phase3C_VibeGuard_Synthesis_Prompt_Claude.md}  |   0
 .../Phase3C_VibeGuard_Synthesis_Prompt_Claude.mmd} |   0
 .../Phase3C_VibeGuard_Raw_Research_Gemini.docx}    | Bin
 .../Phase3C_VibeGuard_Raw_Research_Mistral.md}     |   0
 .../Phase3C_VibeGuard_Raw_Research_Perplexity.md}  |   0
 .../Phase3C_VibeGuard_Raw_Research_Qwen.md}        |   0
 Project_mC_Decision_Register_v1.2.md               |  66 ++++++++---------
 README.md                                          |  16 ++---
 35 files changed, 97 insertions(+), 89 deletions(-)
```

## Post-review correction

`AGENTS.md` contained three stale repository-state descriptions. They were corrected after human review. No technical document, PDR decision, research file, or Phase 3C artifact was changed.


---

## Source 23: `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Original_Project_gitignore.txt`

- Authority: `TIER_1`
- Treatment: `CORE_NARRATIVE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `2b6e0de1dd86ba1295c97310b94d4219fff9918576dfd1d750657b696d85afe8`

# Source Extraction

- Chapter: `01` — Project Mandate, Requirements and Governance
- Authority tier: `TIER_1`
- Manual treatment: `CORE_NARRATIVE`
- Original source: `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Original_Project_gitignore.txt`
- Current SHA-256: `2b6e0de1dd86ba1295c97310b94d4219fff9918576dfd1d750657b696d85afe8`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

key.txt


---

## Source 24: `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Original_Repository_README.md`

- Authority: `TIER_1`
- Treatment: `CORE_NARRATIVE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `3ee6a965e08443bd8af139f01dbe92794e35af5f7888fd85ba1d6bcea27e7a4f`

# Source Extraction

- Chapter: `01` — Project Mandate, Requirements and Governance
- Authority tier: `TIER_1`
- Manual treatment: `CORE_NARRATIVE`
- Original source: `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Original_Repository_README.md`
- Current SHA-256: `3ee6a965e08443bd8af139f01dbe92794e35af5f7888fd85ba1d6bcea27e7a4f`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

# Project mC

Project mC is a patent-oriented embedded-systems innovation pipeline for selecting and developing a semester-scale engineering concept with credible longer-term research, patent, and commercialization potential.

## Current status

Phase 3C is complete for the retained shortlist—not for all five original concepts. The current project action is the final comparative down-selection among the retained three concepts. Phase 4 has not started.

### Retained concepts

1. OpenBraille
2. VibeGuard
3. TrueMoist

### Deferred concepts

- TrustLatch
- ColdTrace

TrustLatch and ColdTrace were deferred before completing their concept-specific Phase 3C architecture work. They were not technically rejected.

## Authority order

When documents conflict, use this precedence:

1. [Engineering Design Review](PHASE%203/Engineering_Design_Review.md)
2. [Latest Decision Register](Project_mC_Decision_Register_v1.2.md)
3. [Phase 3C Retained Portfolio Closure Memo](PHASE%203/PHASE%203C-Comparative%20Technical%20Evaluation/Phase3C_Portfolio_Closure_Memo_Approved.md)
4. Final Phase 3C architecture reports
5. Phase 3C memories
6. Phase 3B report and memory
7. Phase 3A report and memory
8. Phase 2 report and memory
9. Phase 1C synthesis and dossiers
10. Raw independent research

Raw AI research is evidence, not an authoritative project decision.

## Canonical project documents

- [Project phase methodology and roadmap](MC_Project_PHASE_DOC.md)
- [Engineering Design Review](PHASE%203/Engineering_Design_Review.md)
- [Decision Register v1.2](Project_mC_Decision_Register_v1.2.md)
- [Phase 3C Retained Portfolio Closure Memo](PHASE%203/PHASE%203C-Comparative%20Technical%20Evaluation/Phase3C_Portfolio_Closure_Memo_Approved.md)

### Final Phase 3C reports

- [OpenBraille final architecture report](PHASE%203/PHASE%203C-Comparative%20Technical%20Evaluation/OpenBraille/Phase3C_OpenBraille_Architecture_Report_Final.md)
- [VibeGuard final architecture report](PHASE%203/PHASE%203C-Comparative%20Technical%20Evaluation/VibeGuard/Phase3C_VibeGuard_Architecture_Report_Final.md)
- [TrueMoist final synthesis](PHASE%203/PHASE%203C-Comparative%20Technical%20Evaluation/TrueMoist/Phase3C_TrueMoist_Architecture_Report_Final.md)

### Phase 3C memories

- [OpenBraille Phase 3C memory](PHASE%203/PHASE%203C-Comparative%20Technical%20Evaluation/OpenBraille/Phase3C_OpenBraille_Memory_Final.md)
- [VibeGuard Phase 3C memory](PHASE%203/PHASE%203C-Comparative%20Technical%20Evaluation/VibeGuard/Phase3C_VibeGuard_Memory_Final.md)
- [TrueMoist Phase 3C final memory](PHASE%203/PHASE%203C-Comparative%20Technical%20Evaluation/TrueMoist/Phase3C_TrueMoist_Memory_Final.md)

## Convenience packages

`COPY PASTE FOLDER/`, `every sop and memory/`, and ZIP archives are non-canonical convenience or historical packages. Canonical normal files remain at their root or phase paths. ZIP members and convenience copies must not override those canonical files.


---

## Source 25: `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/PHASE3C_NAMING_FINALIZATION_LOG.md`

- Authority: `TIER_1`
- Treatment: `CORE_NARRATIVE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `beee446e6c6e73fa932c50e08812c4c51ca670a367cb02badc40860667a49a0c`

# Source Extraction

- Chapter: `01` — Project Mandate, Requirements and Governance
- Authority tier: `TIER_1`
- Manual treatment: `CORE_NARRATIVE`
- Original source: `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/PHASE3C_NAMING_FINALIZATION_LOG.md`
- Current SHA-256: `beee446e6c6e73fa932c50e08812c4c51ca670a367cb02badc40860667a49a0c`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

# Phase 3C Naming Finalization Log

- **Finalization date and time:** 2026-07-29T09:56:17+02:00
- **Starting branch:** `chore/phase3c-naming-standard`
- **Starting HEAD:** `a60cc875f08785ba1b96851ffb7e0fa28ad2ab6f` — `Add Phase 3C naming standard proposal`
- **Final branch:** `main`

## Preflight validation

- Current branch matched `chore/phase3c-naming-standard`: passed.
- Initial `git diff --check`: passed.
- `PHASE3C_NAMING_VALIDATION_REPORT.md` contained `## Post-review correction`: passed.
- The three specified stale AGENTS.md phrases were absent: passed.
- Project Decision Register v1.2 contained 67 Decision ID entries and 67 unique IDs: passed.
- `phase3c-naming-v1` did not exist: passed.
- `repository-clean-v1` existed and was preserved at `8f013b32a0c1e7d769daf4ceebdc203b92d3089a`: passed.

The first staged validation found only the approved log-formatting defects. After human authorization, trailing whitespace was removed and both log files were normalized to exactly one final newline. The repeated `git diff --cached --check` then passed.

## Temporary review artifact

`PHASE3C_NAMING_CONTENT_DIFF.patch` was the only file removed. It was an untracked temporary review artifact and was explicitly authorized for deletion. No tracked project artifact or other file was deleted.

## Final pre-commit validation

- Approved Phase 3C mappings: 31 present.
- Approved old paths absent and final paths present: passed.
- Raw/failed research files: 13, all original SHA-256 hashes preserved.
- Standalone tracked deletions: 0.
- Files merged: 0.
- Root and Phase 3C README local links: all resolved.
- Temporary case-rename paths: none remained.
- PDR Decision IDs: 67 entries, 67 unique IDs, no duplicates.
- PDR v1.2 non-source-evidence content: unchanged.
- `git diff --cached --check`: passed.
- Unexpected modifications outside the approved scope: none.

## Commits

- **Naming cleanup commit:** `3da3017a39d640cf3b81f5c54bc108f9ae9bde7a` — `Standardize Phase 3C document naming`
- **Main merge commit:** `d56ef22774c1ed9cb044777efc31b05d631d6e34` — `Merge Phase 3C naming standard`
- **Merge method:** non-fast-forward merge with no conflicts.

## First push result

- **Command:** `git push origin main`
- **Result:** Failed; no remote update occurred.
- **Exact error:** `fatal: could not read Username for 'https://github.com': No such device or address`
- **Failure category:** authentication unavailable.

Because the first push failed, no `phase3c-naming-v1` tag was created and no tag push was attempted. The completed local merge was preserved. No pull, rebase, reset, amend, force-push, or destructive cleanup was used.

## Preservation confirmations

- Feature branch `chore/phase3c-naming-standard` was retained at `3da3017a39d640cf3b81f5c54bc108f9ae9bde7a`.
- Existing tag `repository-clean-v1` was preserved at `8f013b32a0c1e7d769daf4ceebdc203b92d3089a`.
- No technical conclusion, PDR decision, rationale, status, identifier, or numbering was changed during finalization.
- No raw research was modified during finalization.

## Final state before logging commit

- Branch: `main`
- HEAD: `d56ef22774c1ed9cb044777efc31b05d631d6e34`
- Working tree: clean before this log was created.
- `git diff --check`: passed.

## Unresolved issue

GitHub authentication is unavailable in the current environment. Local main contains the completed naming merge but could not be pushed. The finalization log will be committed locally; the tag must not be created unless a future authorized run first succeeds in pushing main.


---

## Source 26: `01_GOVERNANCE_AND_CONTROL/AUTHORITY_MAP.md`

- Authority: `TIER_1`
- Treatment: `CORE_NARRATIVE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `cda01b77e280ffd911540c5a78ad5dda294f12f1f3054888a14950f5fb1b4f5a`

# Source Extraction

- Chapter: `01` — Project Mandate, Requirements and Governance
- Authority tier: `TIER_1`
- Manual treatment: `CORE_NARRATIVE`
- Original source: `01_GOVERNANCE_AND_CONTROL/AUTHORITY_MAP.md`
- Current SHA-256: `cda01b77e280ffd911540c5a78ad5dda294f12f1f3054888a14950f5fb1b4f5a`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

# Project mC — Authority Map

## Current authority order for repository use

1. Current teacher requirements and formally recorded constraints.
2. `Project_mC_Decision_Register_v1.2.md`.
3. Approved concept-specific final architecture reports.
4. Approved final memories and SOPs.
5. Current comparative evidence and test registers.
6. Earlier phase reports as historical context.
7. Raw model research as evidence requiring audit.
8. Launchers, manifests and upload bundles as provenance only.

## Explicit status

- Decision Register v1.2: **canonical and controlling**.
- Decision Register v1.0: **historical and non-controlling**.
- VibeGuard/OpenBraille selection: **not treated here as finally authorized unless separately recorded by the team and teacher**.
- Patent hypotheses: **unproven until supported by experiments and institutional IPR review**.

