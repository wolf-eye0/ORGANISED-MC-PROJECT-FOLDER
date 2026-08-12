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
