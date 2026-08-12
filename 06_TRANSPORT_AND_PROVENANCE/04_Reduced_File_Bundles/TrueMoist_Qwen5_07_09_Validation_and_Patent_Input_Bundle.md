# TrueMoist Qwen Transport Compilation — Validation and Patent Input

## Transport-control notice

This is a lossless attachment-limit compilation.

It represents multiple logical documents. The logical documents retain their original authority and order.

The compilation itself is not technical evidence.

Research models must inventory the embedded logical documents separately.

No embedded source has been summarized, rewritten, shortened, corrected, reconciled or omitted.

---

## Embedded logical source 1

- Original filename: `03_Concept_Evidence_Matrix.md`
- Original absolute path: `/home/paradoxpete/Documents/PROJECT/PHASE 3/PHASE 3C-Comparative Technical Evaluation/FINAL_DOWNSELECTION/03_Concept_Evidence_Matrix.md`
- Original byte size: 19491
- Original SHA-256: `8f999b878cfc7f863227682f141a278a4dfa4ee7705e49e1d55ef147c27a1975`

<!-- BEGIN EMBEDDED SOURCE: 03_Concept_Evidence_Matrix.md -->
# Concept Evidence Matrix

## Reading rules and source keys

This is a neutral extraction, not an evaluation. Each cell gives the evidence, then `[source; location; confidence; conflict]`. “None noted” means no disagreement was found in the authoritative set; it does not prove the claim experimentally.

- **EDR:** `PHASE 3/Engineering_Design_Review.md`
- **PDR:** `Project_mC_Decision_Register_v1.2.md`
- **OB-R:** `PHASE 3/PHASE 3C-Comparative Technical Evaluation/OpenBraille/Phase3C_OpenBraille_Architecture_Report_Final.md`
- **OB-M:** `PHASE 3/PHASE 3C-Comparative Technical Evaluation/OpenBraille/Phase3C_OpenBraille_Memory_Final.md`
- **VG-R:** `PHASE 3/PHASE 3C-Comparative Technical Evaluation/VibeGuard/Phase3C_VibeGuard_Architecture_Report_Final.md`
- **VG-M:** `PHASE 3/PHASE 3C-Comparative Technical Evaluation/VibeGuard/Phase3C_VibeGuard_Memory_Final.md`
- **TM-R:** `PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_Architecture_Report_Final.md`
- **TM-M:** `PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_Memory_Final.md`
- **P2:** `PHASE 2/Phase2_Report by CLaude.md`

| Evidence row | OpenBraille | VibeGuard | TrueMoist |
|---|---|---|---|
| Engineering identity | Affordable refreshable-Braille assistive embedded system exploring low-cost actuation, not a high-end-display competitor. `[EDR; Concept 1 / Engineering Identity; High; none noted]` | Passive, single-node edge condition-monitoring system interpreting vibration locally, not merely sensing it. `[EDR; Concept 2 / Engineering Identity; High; Phase 3B mis-scoped cancellation research is excluded]` | Embedded intelligent sensing that improves trustworthiness of inexpensive soil-moisture measurement through local compensation. `[EDR; Concept 3 / Engineering Identity; High; Phase 3C narrows universal/adaptive language to controlled MVP]` |
| Engineering hypothesis | A lower-cost actuation strategy can replace piezoelectric actuation while retaining acceptable tactile performance. `[EDR; Concept 1 / Engineering Hypothesis; High; none noted]` | Low-cost local analysis can reliably distinguish normal from early abnormal machine behaviour on constrained hardware. `[EDR; Concept 2 / Engineering Hypothesis; High; MVP narrows “early” to deliberately introduced abnormal vibration]` | Environmental information and calibration data can compensate predictable error and improve closeness/stability versus uncompensated output under controlled conditions. `[TM-R; §2.2; High; refines EDR’s broader drift/adaptive formulation]` |
| Minimum demonstrable success | One refreshable cell with tactilely distinguishable, repeatable low-cost output. `[EDR; Concept 1 / Minimum Demonstrable Success; High; Phase 3C adds quantitative tests]` | Sense a rig, establish normal, detect deliberate abnormal condition, classify Normal/Abnormal locally, and show clear output. `[VG-R; Task 1 and VG SOP §2 MDS as incorporated; High; dense-floor attribution is beyond bench MDS]` | Acquire raw moisture and temperature, represent salinity treatment, compute raw and compensated estimates locally, compare both to gravimetric truth, and improve on held-out samples. `[TM-R; §2.3; High; more specific than EDR]` |
| Frozen Phase 3C architecture | One 6-dot, ~300%-scale servo/cam cell; direct PWM; FDM frame. `[OB-R; Final Architecture / Architecture Overview; High; reset mechanism is qualified by PDR-021]` | Rigid ADXL345→SPI→ESP32; tiered DSP; threshold then Mahalanobis target; RGB LED; eccentric-mass rig. `[VG-R; §13; High; noise isolation remains unvalidated]` | D-dominant/B-hardened: capacitive probe + DS18B20 + ADS1115 + ESP32, controlled salinity, offline regression, local inference, CSV, gravimetric validation. `[PDR; PDR-058; High; mandatory early gates remain]` |
| MCU | ESP32-WROOM-32 DevKit. `[PDR; PDR-017; High; none noted]` | ESP32 WROOM-32 or S3-class. `[PDR; PDR-025; High; none noted]` | ESP32-WROOM-32 DevKit; ESP32-S3 fallback. `[TM-R; §§12.1–12.2; High; none noted]` |
| Primary sensor or actuator | Six SG90-class micro servos driving eccentric cams and pins. `[OB-R; Hardware Architecture; High; SG90 passive-return detail unvalidated]` | ADXL345, 3-axis digital MEMS, SPI, 3,200 Hz max ODR / 1,600 Hz stated Nyquist bandwidth. `[VG-M; Selected Architecture / Sensor; High; IIS3DWB is future upgrade, not MVP]` | Two genuine analog capacitive probes (one final, one spare/characterization) plus waterproof DS18B20. `[TM-R; §§8–9; High; exact procured variant remains Phase 4]` |
| Power architecture | External 5 V/2 A adapter and 1,000 µF servo-rail capacitor; avoid USB bus power. `[PDR; PDR-020; High; adequacy for six-servo peaks is not empirically proven]` | Shared 3.3 V sensor/logic rail; 0.1 µF sensor decoupling; low-voltage motor rig separately supplied as needed. `[VG-M; Selected Architecture / Electrical interface and Test rig; Medium; report gives less explicit whole-system power budget]` | USB 5 V to dev board; design for 5 V/1 A; 3.3 V ADS1115/DS18B20; no battery. `[TM-R; §20; High; exact probe supply depends on selected probe]` |
| Fabrication requirements | In-house FDM: ABS frame, PETG/Nylon cams, stainless pins; optional laser-cut acrylic guide fallback. `[PDR; PDR-019 and OB-R ADR-005; High; actual tolerances untested]` | Heavy damped motor/fan base, rigid bonded/bolted sensor bracket, final soldered perfboard. `[VG-R; §§8,10,13; High; mount repeatability untested]` | 500–1000 mL containers, repeatability/packing jig, soldered perfboard, sample-preparation apparatus. `[TM-R; §§17,11.4; High; physical workflow not yet exercised]` |
| Software complexity | Event-driven serial commands, six PWM channels, lookup table, calibration storage, self-test. `[OB-R; Embedded Software Architecture; High; some timeout/settle assumptions unverified]` | Interrupt/DMA SPI acquisition, feature extraction, 256–1,024 FFT, calibration, threshold/Mahalanobis, spectral subtraction, logging/LED. `[VG-R; §§6–7,13; High; exact thresholds empirical]` | Sensor drivers, filtering, CSV, offline Python modeling, coefficient export, fixed polynomial inference, quality flags. `[TM-R; §§12–14; High; dataset operations dominate compute]` |
| Algorithm or control approach | Unicode/Braille lookup → target angles → direct 50 Hz PWM; actuate changed dots. `[OB-R; Embedded Software Architecture; High; active cam retraction may be the real reset behavior]` | DC removal → Hann → RMS/peak/other features → triggered FFT; RMS persistence baseline, Mahalanobis primary target; spectral subtraction. `[PDR; PDR-026, PDR-027, PDR-054; High; isolation adequacy pending]` | Raw univariate baseline, multivariate linear baseline, ridge second-order candidate; offline training/fixed MCU coefficients. `[PDR; PDR-031; High; final model depends on held-out result]` |
| Expected BOM range | ₹2,060–₹2,850. `[OB-R; Hardware Architecture / Total estimated BOM; High; procurement estimate, not invoices]` | ₹1,700–₹2,200 ADXL345 MVP; ~₹4,000 IIS3DWB upgrade. `[VG-R; §13; High; upgrade is not MVP]` | ₹1,790–₹3,440 with institutional oven/scale conditions; below ₹5,000 with purchased scale/contingency. `[TM-R; §22; High; institutional equipment assumption is material]` |
| Critical procurement concerns | Six consistent SG90-class servos, suitable FDM materials/printer, 5 V supply; exact variants deferred. `[OB-R; Hardware Architecture and Implementation Readiness; Medium; no current supplier verification]` | ADXL345 authenticity/availability, ESP32, motor/fan and rigid mount; order sensor/MCU early. `[VG-R; §§4,10; Medium; no current procurement pass]` | Genuine analog probes (two), ADS1115 authenticity/stability, scale access/purchase, containers/consumables. `[TM-R; §§8,22,26; High; prices must be refreshed]` |
| Facilities / institutional resources | In-house FDM printer, calipers, multimeter; optional oscilloscope; ideally visually impaired tactile participant and optional faculty/lab mechanical advice. `[OB-R; Implementation Readiness and M6; High; participant/consultation access not confirmed]` | Basic electronics tools, soldering, mechanical base/bracket tools; later real dense-machine floor required for spatial-attribution validation. `[VG-R; §§8,13 and PDR PDR-013; Medium; field access not confirmed]` | Institutional 105 ± 5 °C oven, preferably 0.01 g scale, soil prep/storage space and controlled temperature handling. `[TM-R; §§16,22,26 Gate C; High; access not confirmed]` |
| Critical mechanical risk | Pin/cam friction, tolerance stack-up, cam wear, torque, tactile height; macro scale reduces but does not prove performance. `[OB-R; Remaining Engineering Risks and M3–M6; High; report’s “resolved” wording is stronger than unbuilt evidence]` | Rigid coupling and repeatable eccentric-mass rig; loose mounts filter signals. `[PDR; PDR-028, PDR-030; High; physical repeatability pending]` | Reinsertion, packing density, probe placement, temperature gradients and sample consistency. `[TM-R; §§17,24,26; High; mandatory gates pending]` |
| Critical electrical risk | Brownout/current peaks with six servos; 5 V/2 A + capacitor proposed. `[OB-R; Electrical Architecture / Remaining Risks; High; simultaneous-current adequacy untested]` | SPI integrity above ~2 MHz on jumpers; sensor decoupling and perfboard required. `[VG-M; Major Engineering Risks; High; actual bus margin untested]` | ADC-path noise/nonlinearity, grounding, counterfeit/unstable ADS1115, wet connectors. `[TM-R; §§11,24; High; Week-1 comparison pending]` |
| Critical software risk | Mapping/calibration errors and command/state faults; software is not dominant risk. `[OB-R; Remaining Engineering Risks; Medium; no code exists]` | Sampling jitter, compute/memory, false alarms, threshold tuning, spectral subtraction. `[VG-R; §§6–7,10; High; classifier performance untested]` | Leakage/overfit, model-subset degradation, Python/MCU mismatch, invalid-range handling. `[TM-R; §§14–15,18,25; High; data not collected]` |
| Integration risk | Six mechanical modules plus power and PWM; single-dot-first sequence isolates failures. `[PDR; PDR-022; High; full-cell interference untested]` | Coupling + acquisition + DSP + fault rig + background noise interact; controlled rig precedes field attribution. `[VG-R; §§3c,8,13; High; dense environment remains unresolved]` | Measurement chain depends on probe, jig, reference, treatment, ADC, model and 72-run schedule. `[PDR; PDR-061; High; component list alone is insufficient]` |
| Proposed validation method | M1–M8 bottom-up: single dot, six dots, 100 cycles, tactile test, character set, end-to-end. `[OB-R; Prototype Validation Strategy; High; participant protocol details unavailable]` | Normal baseline versus eccentric-mass abnormal condition on damped motor/fan rig; repeat trials, secondary loose-mount condition, then dense-machine field validation for attribution. `[PDR; PDR-030 and PDR-013; High; exact quantitative acceptance protocol unavailable]` | 72 independent factorial runs, held-out physical replicate, gravimetric GWC, raw-vs-compensated RMSE/MAE and subset analysis. `[PDR; PDR-048, PDR-059, PDR-060; High; timing pilot pending]` |
| Ground-truth quality | Human tactile distinction plus caliper/cycle measurements; “ideally” visually impaired reader. `[OB-R; M5–M8; Medium; tactile ground-truth protocol/sample size not specified]` | Injected eccentric mass gives known condition label, but not actual incipient industrial fault or source attribution truth. `[VG-R; §2 Consensus and §13; Medium; bench labels are credible only for MVP condition classification]` | Dry-basis gravimetric GWC at 105 ± 5 °C until constant mass; 0.01 g preferred. `[PDR; PDR-048; High if access/procedure confirmed; access pending]` |
| Quantitative success threshold | ≤0.1 mm position variance over 100 cycles; ≥1,000 actuations without failure; tactile distinction; BOM ≤₹5,000. `[OB-R; Prototype Validation Strategy / Acceptance criteria; High; user-test success rate not quantified]` | Normal/Abnormal local classification and clear output are specified, but no authoritative minimum accuracy/false-alarm/repeatability number was found. `[VG SOP as quoted in VG-R Task 1 and VG-R §13; High for absence; conflict: “reliably” lacks threshold]` | Held-out RMSE ≥20% lower and MAE ≥15% lower than raw; no major subset MAE worsened >10%. `[PDR; PDR-060 and TM-R §18; High; pending validation]` |
| Expected demonstration | Host character produces refreshable tactile macro-scale one-cell Braille patterns. `[OB-R; M7–M8; High; tactile legibility pending]` | Live motor/fan changes from green Normal to red Abnormal under eccentric mass, using local processing; calibration blue. `[PDR; PDR-029, PDR-030; High; reliability threshold absent]` | Held-out sequence shows reference, raw and compensated estimates, temperature, salinity code, and absolute errors. `[TM-R; §18.4; High; depends on gravimetric results]` |
| Team-skill fit | Firmware/electrical fit strong; mechanical CAD/fabrication is growth area and dominant effort. `[OB-R; Student Team Guidance; High; report’s role count wording conflicts with authoritative five-person roster]` | Strong fit for CS/embedded/DSP; no professional vibration/mechanical expertise assumed; hardware member handles rig. `[VG-R; §11 and PDR PDR-038; High; SOP role arithmetic conflict resolved by PDR]` | Members 1–3 own embedded, model, hardware/validation; learner and presenter support noncritical work. `[TM-R; §29; High; matches PDR-038]` |
| Beginner-member task | Unicode-to-Braille lookup and self-test/diagnostic unit tests. `[OB-R; Student Team Guidance; High; none noted]` | LED/output mapping, calibration state machine, serial logging. `[VG-R; §11; High; none noted]` | Batch labels, CSV checks, temperature logging, test scripts, LEDs, supervised sample prep. `[TM-R; §29 Member 4; High; none noted]` |
| Known patent target | Phase 2 pivot: manufacturing/fabrication method and firmware control rather than actuator mechanism. `[PDR; PDR-009; High as project direction; not patentability]` | Narrow possible target: adaptive single-node noise isolation / in-situ baseline + band-limited spectral subtraction + multivariate statistics. `[VG-R; §12 and P2 §2.2; Medium; current MVP is largely conventional and target unverified]` | Validated compensation workflow, drift/confidence logic, constrained deployment, calibration methodology; not custom probe hardware. `[PDR; PDR-045 and TM-R §28; High as direction; not patentability]` |
| Known prior-art saturation | Actuation mechanism Moderate–High historically; Dot Incorporation named dominant fence. `[P2; §2.1 Patent Saturation / Major Patent Holders; Medium; historical AI synthesis needs current primary-source verification]` | Broad PdM/single-node concept historically High; narrower adaptive niche described as Moderate/unproven; US 7,421,349, Tractian, Infinite Uptime named. `[P2; §2.2; Medium; contested historical synthesis, no current verification]` | Hardware compensation High historically; Campbell, METER, Toro and US 11,598,743 named. `[P2; §2.3; Medium; current status/claims unverified]` |
| Known IP pivot | Away from physical actuation novelty toward manufacturing and firmware. `[PDR; PDR-009; High; current servo/cam’s connection to pivot is unresolved]` | Away from generic monitor/SME economics toward a specific experimentally superior adaptive attribution method, if one exists. `[P2; §2.2; Medium; Phase 3C MVP uses threshold/statistics, not demonstrated adaptive novelty]` | Commodity hardware MVP; future specific recalibration, drift detection, confidence gating, transfer calibration, or controlled error-separation workflow. `[PDR; PDR-045 and TM-R §28.3; High as research directions]` |
| Prototype-generated patent evidence | Force/travel, tactile outcome, repeatability, wear, power, geometry/process and control data could support a later specific technical contribution. `[OB-R; M3–M8 and ADRs; Medium; report does not connect servo/cam tests to a defined claim]` | Noise rejection, attribution, false-alarm, repeatability and comparison against conventional thresholds could support a specific method only if differentiated. `[VG-R; §§3c,12–13; Medium; no comparison protocol against named prior art]` | Controlled raw-vs-compensated errors, packing/temp/salinity separation, confidence/range flags and transfer/drift experiments could support later method development. `[TM-R; §§18,28; High for evidence generation; claimability unverified]` |
| Known unresolved technical assumptions | Passive return versus active retraction; 5 V/2 A peak adequacy; friction/tolerance; tactile height; torque/wear. `[PDR; PDR-021 and OB-R Remaining Engineering Risks; High; direct conflict on reset]` | ADXL345 scope, rigid-mount repeatability, spectral subtraction, eccentric-mass repeatability, thresholds, dense-machine attribution. `[VG-R; §§3,10,13; High; bench/field scope distinction material]` | ADC value, probe/reinsertion/packing, oven/scale, salinity effect, 72-run timing, pilot model. `[PDR; PDR-061; High; all pending]` |
| Known unresolved patent assumptions | Whether macro servo/cam can support a meaningful claim; whether manufacturing/firmware white space remains; current Dot claims/status. `[PDR; PDR-009 and P2 §2.1; High as unresolved; current sources absent]` | Whether differentiation exceeds conventional vibration monitoring and named prior art; whether dense attribution is achieved and claim-relevant. `[P2; §2.2 and VG-R §12; High as unresolved]` | Whether static calibration/compensation workflow is more than ordinary regression/fusion; whether future adaptive variants have current white space. `[TM-R; §28.2–28.3 and P2 §2.3; High as unresolved]` |
| Phase 4 readiness status | “Ready with Minor Refinements” in architecture report. `[OB-R; Architecture Readiness Assessment; High; register reset correction creates a mandatory early check not reflected in label]` | “Ready with Minor Refinements.” `[VG-R; §13 Decision Gate; High; PDR-067 says Phase 4 has not started and final down-selection comes first]` | “Architecture Ready with Mandatory Early Validation.” `[PDR; PDR-063; High; gates explicitly pending]` |

## Cross-cutting conflict notes

1. **Phase 4 status:** concept reports sometimes say “proceed to Phase 4,” but PDR-067 and the closure memo make final comparative down-selection the next action. Therefore, architecture readiness is not authorization or evidence that Phase 4 has started.
2. **Team count:** the authoritative roster is five (PDR-038). VibeGuard’s SOP role arithmetic and parts of OpenBraille team wording can sum to six; those lower-authority inconsistencies are not used to change the roster.
3. **OpenBraille reset:** OB-R describes an “integrated servo torsion spring” as passive reset. PDR-021 explicitly marks this technically unvalidated and requires inspection; active servo-driven cam retraction is the documented correction if no usable passive return exists.
4. **TrueMoist scope:** Phase 2 discussed adaptive, multi-soil/calibration-free validation. Phase 3C freezes a one-soil, fixed-coefficient controlled MVP, so the broader scope is not carried into the MVP. PDR-012 nevertheless remains a future two-season, multi-soil validation task outside the semester MVP.
<!-- END EMBEDDED SOURCE: 03_Concept_Evidence_Matrix.md -->


## Embedded logical source 2

- Original filename: `05_Uncertainty_and_Test_Register.md`
- Original absolute path: `/home/paradoxpete/Documents/PROJECT/PHASE 3/PHASE 3C-Comparative Technical Evaluation/FINAL_DOWNSELECTION/05_Uncertainty_and_Test_Register.md`
- Original byte size: 22484
- Original SHA-256: `125c057229524532b115391fbba948023684ad61d0153fb28ac29e6031e8ee3b`

<!-- BEGIN EMBEDDED SOURCE: 05_Uncertainty_and_Test_Register.md -->
# Uncertainty and Test Register

## Use

Costs and durations are approximate planning values bounded by repository evidence. Where the repository provides no defensible amount, the entry says “unavailable” rather than inventing one. Patent effects describe evidence implications, not patentability.

## Threshold-status rule

Unless explicitly identified as an accepted PDR or final-architecture threshold, numerical pass/fail values in this register are proposed pre-registration thresholds for owner approval. They are not frozen project requirements.

Accepted PDR/report thresholds must remain distinguished from newly proposed working thresholds.

### U-OB-01 — SG90 passive-return / torsion-spring claim

- **Concept / category:** OpenBraille / mechanical architecture
- **Question:** Does the selected SG90 variant provide a usable passive return that retracts the pin when commanded/unpowered, or must the servo actively rotate the cam back?
- **Why it matters:** The final report says passive integral-spring reset; PDR-021 marks it technically unvalidated and requires correction if absent.
- **Current evidence:** `Project_mC_Decision_Register_v1.2.md`, PDR-021; `OpenBraille/Phase3C_OpenBraille_Architecture_Report_Final.md`, Hardware and Mechanical Architecture.
- **Earliest action / equipment:** Physically inspect one procured servo; bench it powered and unpowered with cam load; video/angle/force record. Servo, supply, simple load/cam.
- **Cost / duration:** One servo within BOM; <1 day.
- **Pass / fail:** Pass = repeatable passive return sufficient for required pin travel/load. Fail = no passive return or insufficient/unreliable return.
- **Effect:** Patent case—clarifies actual claim elements; buildability—requires truthful active-retraction control or mechanical spring fallback.
- **Urgency:** Immediate, before CAD freeze.

### U-OB-02 — Active cam-retraction interpretation

- **Concept / category:** OpenBraille / control-mechanics interface
- **Question:** If passive return is absent, does commanded 90°→0° cam motion retract all pins reliably without an added spring?
- **Why it matters:** This is PDR-021’s required correction and changes failure modes and control description.
- **Current evidence:** PDR-021; OpenBraille report, operating principle and Mechanical Architecture.
- **Action / equipment:** Single-dot cam prototype; repeated up/down commands under representative friction; calipers and current logging.
- **Cost / duration:** Single-dot materials within BOM; 1–2 days.
- **Pass / fail:** Pass = repeatable full retraction with no sticking across planned cycles. Fail = incomplete return requiring geometry or spring redesign.
- **Effect:** Patent—defines the real control/mechanical interaction; buildability—may add hardware/iteration.
- **Urgency:** Immediate.

### U-OB-03 — Six-servo current demand and 5 V/2 A adequacy

- **Concept / category:** OpenBraille / electrical
- **Question:** Does the specified supply/capacitor prevent voltage sag and resets under worst credible six-servo transitions, stalls, and rapid sequences?
- **Why it matters:** Each servo is reported up to ~500 mA peak; “never all six active” is an operating assumption, not measured proof.
- **Current evidence:** OpenBraille report, Hardware/Electrical Architecture; PDR-020.
- **Action / equipment:** Current/voltage logging for one, three, then six servos; worst-pattern transition and controlled stall test; multimeter/oscilloscope if available.
- **Cost / duration:** Within prototype BOM; 1 day after six servos arrive.
- **Pass / fail:** Pass = no unsafe sag, brownout, overheating, or reset with margin. Fail = any repeatable power fault.
- **Effect:** Patent—usually peripheral unless power sequencing becomes specific contribution; buildability—may require larger supply/sequencing and BOM revision.
- **Urgency:** Week 1, before full integration.

### U-OB-04 — Mechanical friction and tolerance

- **Concept / category:** OpenBraille / fabrication
- **Question:** Can FDM guides, pins, cams and followers achieve free motion, ≤0.1 mm variance over 100 cycles, and ≥1,000 cycles without failure?
- **Why it matters:** Macro-scaling mitigates but does not validate the dominant mechanical risk.
- **Current evidence:** OpenBraille report, Mechanical Architecture, Validation, Remaining Risks.
- **Action / equipment:** Print a single-dot tolerance coupon/module, measure clearances, run automated cycling, inspect wear.
- **Cost / duration:** Single-dot fraction of ₹2,060–₹2,850 BOM; 2–4 days including printing/cycling.
- **Pass / fail:** Pass = report thresholds met; fail = binding, excessive variance, or failure before 1,000 cycles.
- **Effect:** Patent—produces manufacturing/geometry evidence; buildability—direct critical-path risk.
- **Urgency:** Immediate.

### U-OB-05 — Macro MVP versus long-term invention path

- **Concept / category:** OpenBraille / scope and patent development
- **Question:** What exact technical bridge, if any, connects the deliberately non-ISO macro servo/cam MVP to the manufacturing/firmware invention direction or future true-scale mechanism?
- **Why it matters:** Semester success and long-term invention are distinct; the macro MVP must not be assumed to prove commercial-scale feasibility.
- **Current evidence:** PDR-009/PDR-016; OpenBraille report ADR-002; Phase 2 report §2.1.
- **Action / equipment/data:** After current patent search, make a claim-to-experiment map separating macro evidence, scale-dependent elements, and deferred true-scale elements.
- **Cost / duration:** Patent pass cost/duration unavailable; mapping 1–2 days after results.
- **Pass / fail:** Pass = at least one specific prospective contribution is testable at macro scale and relevant beyond mere substitution. Fail = all meaningful claim elements depend on unbuilt true-scale architecture.
- **Effect:** Patent—central; buildability—prevents inappropriate scope expansion.
- **Urgency:** Before patent scoring.

### U-OB-06 — Meaningful servo-cam patent support

- **Concept / category:** OpenBraille / patent evidence
- **Question:** Can the servo-cam prototype support a specific manufacturing or firmware/control claim rather than only demonstrating a conventional actuator substitution?
- **Why it matters:** PDR-009 explicitly moves the target away from the physical mechanism.
- **Current evidence:** PDR-009; Phase 2 §2.1; OpenBraille report ADRs and validation.
- **Action:** Current primary patent search/claim chart; identify nearest relevant manufacturing/control art; design a comparative experiment.
- **Cost / duration:** Unavailable in repository.
- **Pass / fail:** Pass = specific differentiated claim elements plus measurable advantage. Fail = only known component aggregation or known actuation.
- **Effect:** Patent—decisive; buildability—may define extra experiments but must not redesign prematurely.
- **Urgency:** Before any patent-potential score.

### U-OB-07 — Tactile-identification protocol and acceptance

- **Concept / category:** OpenBraille / demonstrable success
- **Question:** What blinded tactile-identification protocol, participant plan, and quantitative acceptance rate will establish that raised and lowered dots and complete patterns are reliably distinguishable by touch?
- **Why it matters:** The EDR requires acceptable tactile performance, while the final architecture report calls for structured human testing but does not freeze a participant plan or quantitative reader-success threshold.
- **Current evidence:** `PHASE 3/Engineering_Design_Review.md`, OpenBraille / Minimum Demonstrable Success; `PHASE 3/PHASE 3C-Comparative Technical Evaluation/OpenBraille/Phase3C_OpenBraille_Architecture_Report_Final.md`, Prototype Validation Strategy M6 and Acceptance Criteria.
- **Action / equipment/data:** Obtain owner approval for a blinded protocol, participant plan, trial count, pattern set, randomization, and quantitative acceptance rate before tactile testing.
- **Cost / duration:** Participant-access cost and duration are unavailable in the repository.
- **Pass / fail:** Pass = the owner-approved pre-registered tactile-identification criterion is met. Fail = it is not met or the test lacks the approved controls.
- **Effect:** Patent—determines whether tactile-performance evidence is credible; buildability—may require changes to pin height, spacing, profile, or mechanism.
- **Urgency:** Before tactile validation and final G4 confirmation.

### U-VG-01 — ADXL345 bandwidth boundary

- **Concept / category:** VibeGuard / sensing scope
- **Question:** Is ADXL345 adequate for every claimed MVP phenomenon, and are bearing-fault/high-frequency claims explicitly excluded?
- **Why it matters:** 1,600 Hz stated bandwidth is adequate for low-frequency imbalance but IIS3DWB is the documented 6,000 Hz upgrade for bearing work.
- **Current evidence:** PDR-023/PDR-055; VibeGuard report §§3b–4.
- **Action / equipment:** Measure rig spectral content and anti-aliasing/ODR behavior; freeze claim boundary. Optional side-by-side higher-bandwidth sensor only if bearing scope is proposed.
- **Cost / duration:** ADXL rig within BOM; comparison sensor ₹800–₹1,200 if chosen; 2–3 days.
- **Pass / fail:** Pass = relevant fault energy and repeatable features lie within verified band. Fail = required discriminating signature lies outside.
- **Effect:** Patent—limits claim language; buildability—may trigger documented sensor upgrade.
- **Urgency:** Before test protocol freeze.

### U-VG-02 — Rigid-mount repeatability

- **Concept / category:** VibeGuard / mechanical validation
- **Question:** Can the sensor be remounted or reproduced with sufficiently consistent coupling that classification does not depend on an accidental installation?
- **Why it matters:** Mounting changes the transfer function and may dominate the signal.
- **Current evidence:** PDR-028; VibeGuard report §§2,8,10.
- **Action / equipment:** Repeated remove/reinstall trials using a defined bracket/torque/adhesive process; compare feature distributions.
- **Cost / duration:** Bracket/fasteners within rig BOM; 1–2 days.
- **Pass / fail:** Pass = between-mount variation remains below pre-registered normal/fault separation. Fail = mount variance overlaps the fault effect.
- **Effect:** Patent—supports deployment/repeatability evidence if relevant; buildability—may require a better fixture.
- **Urgency:** Early bench phase.

### U-VG-03 — Spectral-subtraction adequacy

- **Concept / category:** VibeGuard / DSP
- **Question:** Does baseline spectral subtraction plus band-limited features improve discrimination under controlled interfering vibration without unacceptable false alarms or lost fault energy?
- **Why it matters:** It is the frozen mitigation for single-node noise but explicitly unproven.
- **Current evidence:** PDR-027; VibeGuard report §3c and §12.
- **Action / equipment:** Target motor plus separately controlled interferer; randomized baseline/fault/noise trials; compare raw features, band limits, subtraction, and threshold baseline.
- **Cost / duration:** Second motor/access cost unavailable; 3–7 days after rig build.
- **Pass / fail:** Pass = pre-registered improvement in attribution/classification without material degradation; numeric threshold must be frozen before test. Fail = no benefit or unstable false alarms.
- **Effect:** Patent—central to any specific isolation-method case; buildability—could reduce MVP to conventional controlled bench monitor.
- **Urgency:** High, after acquisition is stable.

### U-VG-04 — Dense-machine attribution claim

- **Concept / category:** VibeGuard / validation and patent
- **Question:** Can one node attribute a fault to its mounted machine on a real dense-machine floor rather than merely detect increased vibration?
- **Why it matters:** Phase 2’s narrow potential and PDR-013 depend on real field evidence.
- **Current evidence:** PDR-013; Phase 2 report §2.2; VibeGuard report §3c.
- **Action / equipment/data:** Secure a site; independently label machine states; compare target fault/no-fault while neighbors vary; pre-register attribution metrics.
- **Cost / duration:** Site/access cost and duration unavailable; likely after bench validation.
- **Pass / fail:** Pass = meets pre-registered attribution/false-alarm thresholds across neighbor states. Fail = response cannot be assigned to target machine.
- **Effect:** Patent—decisive for narrow niche; buildability—field dependence may exceed semester constraints even if bench MDS passes.
- **Urgency:** Before patent scoring or any dense-floor claim.

### U-VG-05 — Eccentric-mass fault-simulation repeatability

- **Concept / category:** VibeGuard / ground truth
- **Question:** Does the chosen eccentric mass and placement generate repeatable abnormal conditions without varying speed/mounting unpredictably?
- **Why it matters:** Bench labels are only credible if the induced condition is controlled.
- **Current evidence:** PDR-030; VibeGuard report Consensus and §13.
- **Action / equipment:** Fixed mass, radius and attachment fixture; tachometer if available; repeated randomized install/run trials.
- **Cost / duration:** Within test-rig BOM; 1–2 days.
- **Pass / fail:** Pass = feature distribution is stable and separated from normal across replicates. Fail = induced effect varies enough to confound classifier.
- **Effect:** Patent—quality of experimental support; buildability—may require a precision fixture.
- **Urgency:** Before classifier tuning.

### U-VG-06 — More than a conventional vibration monitor

- **Concept / category:** VibeGuard / patent differentiation
- **Question:** What experimentally demonstrated feature is nonconventional beyond ADXL345 + FFT/features + threshold/anomaly alert?
- **Why it matters:** Phase 3C itself warns that a bare sensor relay is not the differentiator; Phase 2 names crowded art.
- **Current evidence:** VibeGuard report §12; Phase 2 §2.2; PDR-046.
- **Action:** Current patent search and claim chart; benchmark proposed isolation/statistical method against simple RMS/FFT baseline and nearest identified methods.
- **Cost / duration:** Patent pass unavailable; experimental comparison 3–7 days after rig.
- **Pass / fail:** Pass = specific method and measurable improvement tied to claim elements. Fail = only conventional monitoring remains.
- **Effect:** Patent—decisive; buildability—advanced experiment may add burden.
- **Urgency:** Before patent score.

### U-VG-07 — Quantitative bench-classification success threshold

- **Concept / category:** VibeGuard / demonstrable success
- **Question:** What trial count and quantitative accuracy, false-alarm, missed-detection, persistence, and repeatability criteria will define reliable Normal/Abnormal classification on the controlled bench rig?
- **Why it matters:** The EDR requires consistent distinction and the final architecture leaves statistical threshold tuning empirical, but no authoritative system-level numerical acceptance threshold is frozen.
- **Current evidence:** `PHASE 3/Engineering_Design_Review.md`, VibeGuard / Minimum Demonstrable Success; `PHASE 3/PHASE 3C-Comparative Technical Evaluation/VibeGuard/Phase3C_VibeGuard_Architecture_Report_Final.md`, §13 Remaining Engineering Uncertainties.
- **Action / equipment/data:** Obtain owner approval for a pre-registered randomized trial protocol and quantitative acceptance criteria before classifier evaluation.
- **Cost / duration:** Protocol-definition cost and duration are unavailable in the repository.
- **Pass / fail:** Pass = the owner-approved pre-registered bench-classification criteria are met. Fail = they are not met or the evaluation lacks the approved controls.
- **Effect:** Patent—provides interpretable baseline and differentiator evidence; buildability—prevents a visually convincing but quantitatively undefined demonstration from being treated as success.
- **Urgency:** Before classifier tuning and final G4 confirmation.

### U-TM-01 — ADS1115 value versus calibrated ESP32 ADC1

- **Concept / category:** TrueMoist / instrumentation
- **Question:** Does ADS1115 materially improve noise, drift, reproducibility, or held-out pilot RMSE?
- **Why it matters:** PDR-032 forbids justification from bit count alone.
- **Current evidence:** PDR-032; TrueMoist report §11.3.
- **Action / equipment:** Same-node paired reads for dry/medium/wet samples; compare SD, 10-minute drift, reinsertion and pilot RMSE.
- **Cost / duration:** ADS1115 ₹120–₹220 listed; 1–2 days.
- **Pass / fail:** ≥15% improvement strongly justifies; 5–15% supports retention; <5% permits fallback; instability/unavailability fails module.
- **Effect:** Patent—normally conventional; buildability—determines simpler acquisition path.
- **Urgency:** Week 1.

### U-TM-02 — Probe repeatability

- **Concept / category:** TrueMoist / sensing
- **Question:** Does a genuine capacitive probe give stable, monotonic, repeatable output?
- **Why it matters:** No model can rescue an unstable measurement chain.
- **Current evidence:** TrueMoist report §§8.2–8.3 and Gate A.
- **Action / equipment:** Dry-air/warm-up tests, fixed moist sample, ten jig insertions, two-probe comparison.
- **Cost / duration:** Two probes ₹300–₹600 listed; 1–2 days.
- **Pass / fail:** Gate A pass <5% usable-span reinsertion SD and monotonic pilot; fail >10%, saturation, or non-monotonicity.
- **Effect:** Patent—determines whether compensation evidence is credible; buildability—architecture kill if no usable probe.
- **Urgency:** Week 1.

### U-TM-03 — Insertion and packing sensitivity

- **Concept / category:** TrueMoist / mechanical experimental control
- **Question:** Can a jig and fixed preparation reduce packing/insertion variation below intended environmental effects?
- **Why it matters:** Packing may masquerade as or overwhelm temperature/salinity effects.
- **Current evidence:** PDR-061; TrueMoist report §§17,24, Gate D.
- **Action / equipment:** Independently repack controlled samples using fixed mass, compaction and fill height; compare variance.
- **Cost / duration:** Jig/container materials ₹200–₹450 listed; 2–4 days.
- **Pass / fail:** Pass = packing variance below intended disturbance effect. Fail = equal or greater.
- **Effect:** Patent—essential to claimed error-separation workflow; buildability—may force rig redesign or scope reduction.
- **Urgency:** Week 1–2.

### U-TM-04 — Institutional oven and precision-scale access

- **Concept / category:** TrueMoist / facilities and ground truth
- **Question:** Is credible 105 ± 5 °C drying-to-constant-mass and suitable weighing actually available for the full schedule?
- **Why it matters:** PDR-048 makes gravimetric GWC authoritative; buying an oven is outside budget.
- **Current evidence:** PDR-048; TrueMoist report §§16,22, Gate C.
- **Action / equipment:** Written booking/access confirmation; one full dry/reweigh trial; confirm 0.01 g preferred or justify 0.1 g with 300–500 g samples.
- **Cost / duration:** ₹0 if institutional; optional scale ₹400–₹700; ≥24 h trial.
- **Pass / fail:** Pass = repeatable access/process/resolution. Fail = no traceable ground truth.
- **Effect:** Patent—invalidates performance evidence if absent; buildability—architecture becomes conditional and final accuracy claims stop.
- **Urgency:** Week 1, before main procurement/dataset.

### U-TM-05 — Controlled-salinity treatment effect

- **Concept / category:** TrueMoist / experimental factor
- **Question:** Can one NaCl treatment produce a repeatable, non-saturating shift distinct from noise at fixed moisture/temperature?
- **Why it matters:** Salinity is represented as a controlled treatment, not measured EC; if no separable effect, the compensation scope narrows.
- **Current evidence:** PDR-062; TrueMoist report §§10,26 Gate E.
- **Action / equipment:** Pilot S0/S1 dose by dry-soil mass; adjust dose once if necessary.
- **Cost / duration:** Consumables within ₹100–₹300 line; 1–3 days plus equilibration.
- **Pass / fail:** Pass = shift >3× within-condition electronic noise, repeatable and nonsaturating. Fail = no separable effect/unstable direction after one adjustment.
- **Effect:** Patent—affects controlled error-separation evidence; buildability—fallback is temperature-only MVP.
- **Urgency:** Week 2.

### U-TM-06 — Feasibility of 72 independent physical runs

- **Concept / category:** TrueMoist / schedule and validation
- **Question:** Can the team prepare, equilibrate, measure, dry, log and quality-check 72 independent runs within eight weeks?
- **Why it matters:** Rapid ADC reads cannot be counted as independent; physical workload is the limiting resource.
- **Current evidence:** PDR-059; TrueMoist report §§15,23,30.
- **Action / equipment/data:** Time an end-to-end pilot batch and calculate throughput using actual oven capacity and person-hours.
- **Cost / duration:** Pilot consumables within BOM; 3–7 elapsed days.
- **Pass / fail:** Pass = measured throughput supports 72 with contingency. Fail = does not; documented 54-run fallback may be considered.
- **Effect:** Patent—smaller dataset may weaken evidentiary breadth; buildability—direct schedule risk.
- **Urgency:** Week 2–3 before main dataset.

### U-TM-07 — Claimability of calibration/compensation workflow

- **Concept / category:** TrueMoist / patent differentiation
- **Question:** Is the actual MVP workflow sufficiently specific and nonconventional, or only generic calibration plus ordinary regression?
- **Why it matters:** TM-R §28.2 explicitly says ordinary fusion, polynomial regression and generic calibration are not automatically patentable.
- **Current evidence:** PDR-045; TrueMoist report §28; Phase 2 §2.3.
- **Action:** Current primary patent search and claim chart for controlled error separation, confidence/range fallback, drift/event recalibration and transfer calibration; map experiments to one specific mechanism.
- **Cost / duration:** Unavailable in repository.
- **Pass / fail:** Pass = verified prospective claim elements linked to measurable advantage. Fail = only conventional workflow remains.
- **Effect:** Patent—decisive; buildability—may distinguish semester MVP from a later invention experiment.
- **Urgency:** Before patent score.
<!-- END EMBEDDED SOURCE: 05_Uncertainty_and_Test_Register.md -->


## Embedded logical source 3

- Original filename: `06_Patent_Research_Input_Pack.md`
- Original absolute path: `/home/paradoxpete/Documents/PROJECT/PHASE 3/PHASE 3C-Comparative Technical Evaluation/FINAL_DOWNSELECTION/06_Patent_Research_Input_Pack.md`
- Original byte size: 16069
- Original SHA-256: `969d6bd97f0a726186d0f9bae405248ed82ef6314e3d5618166a0a1185411428`

<!-- BEGIN EMBEDDED SOURCE: 06_Patent_Research_Input_Pack.md -->
# Patent Research Input Pack

## Scope and warning

This pack prepares—not performs—a later current patent search. Historical repository conclusions below are search leads, not verified current patent status, patentability, validity, claim construction, or freedom-to-operate. No concept is stated to be patentable. Search primary patent records, current family/legal status, claims, citations, assignments, continuations/divisionals, non-US equivalents (including relevant Indian and Chinese records), and relevant non-patent literature before scoring.

## OpenBraille

### Current technical definition

- **Engineering hypothesis:** A lower-cost actuation strategy can replace conventional piezoelectric actuation while retaining acceptable tactile performance for a refreshable Braille interface. Source: `PHASE 3/Engineering_Design_Review.md`, OpenBraille / Engineering Hypothesis.
- **MVP architecture:** One macro-scale (~300% ISO 17049), 6-dot refreshable cell; ESP32 direct PWM; six SG90-class servos; eccentric cams/followers/pins; FDM frame; external 5 V/2 A supply. Source: `PHASE 3/PHASE 3C-Comparative Technical Evaluation/OpenBraille/Phase3C_OpenBraille_Architecture_Report_Final.md`, Final Architecture.
- **Phase 2 historical conclusion:** Mechanism space was assessed Moderate–High saturation, with Dot Incorporation a dominant named fence; naive known-actuator substitution had high obviousness risk. Historical pivot: manufacturing/fabrication method and firmware/control. Source: `PHASE 2/Phase2_Report by CLaude.md`, §2.1; accepted direction in PDR-009.

### Proposed patent-development angle

Repository-supported directions to verify:

- a specific manufacturing/fabrication method for low-cost tactile cells/arrays;
- a specific control/firmware method that enables cheap commodity actuators;
- geometry/process/control interactions supported by force, travel, repeatability, wear, power, tolerance and tactile evidence.

These are directions only. The current macro servo/cam implementation has not been shown to embody a claimable contribution.

### Apparently conventional features

Servo motor, eccentric cam, follower and pin; ESP32 PWM; serial character mapping; 3D-printed frame; macro scaling as a prototyping tactic; ordinary calibration/self-test; external low-voltage supply. Verify rather than assume.

### Suggested differentiators to test

- specific manufacturable cell geometry or modular assembly that produces repeatable tactile travel at low tolerance/cost;
- fabrication sequence/material/clearance combination with measured yield or durability advantage;
- actuator-control/sequencing/calibration method that improves peak current, travel consistency, wear, or cost;
- any bridge from macro proof to practical multi-cell or smaller-scale architecture.

### Required experimental proof

Actual reset mode; actuator force/torque and current; pin travel and tactile outcome; tolerance/yield; 100-cycle variance and ≥1,000-cycle durability; multi-servo power behavior; comparison against a conventional servo/cam or nearest identified approach; scale-dependence of asserted advantages.

### Named repository leads

Historical/unverified: Dot Incorporation/Dot Inc. estate; Orbit Research/Orbit Reader; Innovision/Braille Me; Canute; Monarch; MOLBED; MagnePins; US 5,685,721; US 6,881,063; US 11,410,574; US 6,743,021 B2; US 8,770,981 B2; WO 2015189863 A2; CA 3,120,784 A1; US 11,854,423 B1; EP 4,049,116 A1; US 10,254,499 B1. Source lead: Phase 2 §2.1 and OpenBraille final report’s rejected-alternative discussion. Every identifier, family, claim, status and relevance requires primary-source verification.

### Search terms and variants

`refreshable braille cell`, `refreshable tactile display`, `tactile pin array`, `braille dot actuator`, `servo cam braille`, `cam follower tactile pin`, `low cost braille actuator`, `macro scale braille prototype`, `3D printed refreshable braille`, `additive manufactured tactile display`, `monolithic tactile cell`, `modular braille actuator`, `PWM tactile actuator control`, `adaptive overdrive braille actuator`, `shared driver tactile pins`, `low force latching tactile pixel`, `piezoelectric braille replacement`.

Variants: refreshable/rewritable/dynamic; Braille/tactile/haptic; dot/pin/taxel/tactile pixel; cell/module/array/display; actuator/raiser/lifter; cam/eccentric/linkage; fabrication/manufacture/additive/printed/molded.

### Likely claim elements to test

Do not draft claims yet. Test combinations involving: cell frame/guide geometry; identical replaceable actuator modules; cam/follower travel relationship; manufacturing process and tolerances; actuator calibration; selective/sequenced actuation; peak-current management; closed/verified tactile state; low-cost multi-cell scaling; control tied to a measurable physical benefit.

### Verification assumptions and questions

- What Dot families are alive, where, and what do their independent claims actually cover?
- Does any family cover servo/cam, printed guides, modular tactile pins, manufacturing methods, or control/sequencing?
- Are MOLBED/MagnePins prior art, open-hardware publications, patents, or combinations?
- Is the Phase 2 manufacturing/firmware “white space” still plausible after current searching?
- Is macro-scale evidence technically relevant to any claim with practical value?
- Does the prototype show more than substitution of a known actuator into a known Braille cell?
- Which experiments distinguish a prospective contribution from the closest current primary art?

## VibeGuard

### Current technical definition

- **Engineering hypothesis:** Low-cost embedded local vibration analysis can distinguish normal from deliberately introduced early abnormal behaviour on constrained hardware without cloud processing. Sources: EDR VibeGuard / Engineering Hypothesis; VibeGuard SOP §2.
- **MVP architecture:** Rigid ADXL345 over SPI to ESP32; DC removal, Hann, continuous time features, triggered FFT; calibrated RMS/persistence baseline and Mahalanobis target; baseline spectral subtraction; RGB alert; eccentric-mass motor/fan rig. Source: `PHASE 3/PHASE 3C-Comparative Technical Evaluation/VibeGuard/Phase3C_VibeGuard_Architecture_Report_Final.md`, §§4–13.
- **Phase 2 historical conclusion:** Broad predictive-maintenance/SME monitoring assessed crowded; narrow adaptive single-node attribution niche assessed contested/unproven. A real dense-machine test was required. Source: Phase 2 §2.2; PDR-013 and PDR-046.

### Proposed patent-development angle

A specific, experimentally superior single-node attribution/noise-discrimination method using in-situ baseline calibration, band-limited spectral subtraction and multivariate statistical detection on constrained hardware. Zero-subscription/SME economics is a commercial position, not technical novelty.

### Apparently conventional features

MEMS accelerometer on a motor; rigid mount; ESP32; SPI acquisition; DC removal/Hann/FFT; RMS, peak, crest factor, kurtosis; threshold/persistence; RGB alarm; eccentric-mass imbalance rig; generic Mahalanobis anomaly detection. Their combination must not be presumed novel.

### Suggested differentiators to test

- target-machine attribution under neighboring-machine interference using one sensor;
- a specific calibration/subtraction/feature-selection/control sequence;
- resource-constrained implementation that preserves measurable attribution performance;
- adaptive or confidence-gated behavior beyond fixed thresholds;
- mounting/calibration interaction only if technically specific and nonconventional.

### Required experimental proof

Rigid-mount repeatability; fault-injection repeatability; classifier accuracy, false alarms and missed detections; ablations (RMS only, FFT features, Mahalanobis, subtraction); controlled interferer; real dense-machine field data with independent source labels; compute/memory/timing; comparison to nearest patent methods.

### Named repository leads

Historical/unverified: US 7,421,349 (US Navy phase-coupling lead); Tractian and a reported fault-detection patent; Infinite Uptime; Augury; KCF/Senseye. Source: Phase 2 §2.2. IIS3DWB is a technical upgrade, not a patent lead. All identifiers, families, current status and claim scope require primary verification.

### Search terms and variants

`single sensor machine vibration attribution`, `single node vibration source isolation`, `machine fault neighboring machine noise`, `vibration spectral subtraction condition monitoring`, `in situ vibration baseline calibration`, `edge vibration anomaly Mahalanobis`, `band limited vibration fault features`, `spatial attribution accelerometer machine`, `phase coupling unrelated spectral peaks fault`, `low cost predictive maintenance edge node`, `target machine vibration discrimination`, `dense factory vibration cross talk`, `mechanical cross-talk condition monitoring`, `unsupervised vibration anomaly embedded`.

Variants: predictive maintenance/condition monitoring/machine health/fault detection; vibration/acceleration/acoustic emission; source isolation/source separation/attribution/discrimination/crosstalk rejection; edge/local/on-device/single-node; baseline/subtraction/fingerprint/envelope/sideband/phase coupling; anomaly/novelty/one-class/Mahalanobis.

### Likely claim elements to test

Sensor-to-machine mounting; baseline acquisition conditions; spectral envelope representation; target bands; subtraction/update rule; feature vector; multivariate distance/confidence; persistence; attribution decision; constrained compute scheduling/triggered FFT; handling neighbor-state changes; output tied to maintenance condition.

### Verification assumptions and questions

- What does US 7,421,349 actually claim, what families/status exist, and how close is it to the proposed method?
- Which Tractian/Infinite Uptime or other families cover fingerprinting, local diagnosis, SME nodes, or source attribution?
- Is spectral subtraction in vibration monitoring already conventional?
- Does Mahalanobis plus common features add anything claim-relevant?
- Can single-node dense-machine attribution be demonstrated, and against which closest-art baseline?
- Is the patent angle an algorithm/method claim with jurisdiction-specific eligibility/obviousness risk?
- What primary sources exist in Indian and Chinese databases that earlier passes missed?

## TrueMoist

### Current technical definition

- **Engineering hypothesis:** Environmental measurements and controlled calibration data can compensate predictable commodity-probe error, improving stability and closeness to gravimetric reference versus uncompensated output under controlled tests. Source: TrueMoist final report §2.2.
- **MVP architecture:** Genuine analog capacitive probe; DS18B20; ADS1115 with Week-1 value gate; ESP32; controlled salinity treatment, not live EC; one soil; offline linear/ridge second-order models and fixed MCU coefficients; USB CSV; 72 physical runs; gravimetric GWC. Source: PDR-058–063 and TrueMoist final report.
- **Phase 2 historical conclusion:** Hardware compensation assessed crowded; software-only event-driven/self-updating correction was the proposed pivot. Phase 3C intentionally narrows MVP to fixed coefficients and controlled single-soil proof. Source: Phase 2 §2.3; PDR-045.

### Proposed patent-development angle

Repository-supported future mechanisms to verify:

- event-triggered recalibration using sparse trusted reference events;
- sensor-drift detection with confidence gating;
- calibration transfer across commodity probe units;
- calibration compression on constrained MCUs;
- a controlled sequence separating packing, temperature and conductivity effects;
- validity-region detection and safe fallback.

The current polynomial model, ESP32, ADS1115, generic sensor fusion and generic calibration are explicitly not automatically patentable.

### Apparently conventional features

Capacitive moisture probe; temperature sensor; external ADC; ESP32; RC filter; gravimetric calibration; linear/polynomial/ridge regression; offline training/fixed coefficients; CSV; controlled salt dosing; jigs and ordinary sample preparation.

### Suggested differentiators to test

- a specific experimental/control workflow that distinguishes error sources and controls confidence;
- drift/event detection and gated recalibration mechanism;
- cross-unit transfer with bounded confidence/fallback;
- validity-region detection that prevents unsafe extrapolation;
- materially compressed calibration without losing compensation performance.

### Required experimental proof

Probe/reinsertion/packing repeatability; gravimetric traceability; salinity effect; raw versus compensated held-out RMSE/MAE; subset guardrails; grouped validation; model/MCU equivalence; drift sequences; multiple probe units for transfer; ablation of each variable/mechanism; comparison to conventional calibration.

### Named repository leads

Historical/unverified: Campbell Scientific; METER Group/TEROS; Toro; CropX; US 7,884,620; US 11,598,743; US 7,170,302 B2; US 20150330932A1. Source: Phase 2 §2.3. All assignees, families, status, expiry estimates, independent claims and relevance require current primary-source verification.

### Search terms and variants

`soil moisture temperature salinity compensation`, `capacitive soil moisture drift correction`, `soil moisture sensor self calibration`, `event triggered recalibration soil sensor`, `soil probe confidence gating`, `commodity soil probe transfer calibration`, `embedded soil moisture regression compensation`, `soil sensor validity region fallback`, `packing effect compensation soil moisture`, `conductivity temperature dielectric moisture correction`, `sparse reference recalibration irrigation`, `multi probe calibration transfer`, `edge calibration compression sensor`, `gravimetric calibrated embedded moisture`.

Variants: moisture/water content/dielectric/permittivity; soil/substrate/growing media; salinity/conductivity/EC/fertilizer; drift/aging/hysteresis/bias; compensation/correction/calibration/recalibration; confidence/quality/validity/out-of-range; transfer/interchangeability/unit-to-unit; event/irrigation/dry-down/reference.

### Likely claim elements to test

Commodity sensor inputs; environmental/treatment inputs; trusted reference event; drift detector; confidence score; model-validity region; update gate; safe fallback; cross-unit transfer; calibration dataset/control sequence; compressed coefficients; local inference; physical measurement improvement.

### Verification assumptions and questions

- What do the named Campbell/METER/Toro/Korean-assignee families actually claim and where are they alive?
- How crowded are calibration, environmental compensation, drift detection, event recalibration and probe-transfer subfields today?
- Is controlled error-source separation a technical method or merely ordinary experimental practice?
- Does the fixed-coefficient MVP generate evidence relevant to a later adaptive claim, or are additional drift/reference-event experiments mandatory?
- Can any prospective element show a measurable advantage over generic multivariate calibration?
- Which claim form has technical-effect/eligibility risk in relevant jurisdictions?
- What Indian/Chinese and non-patent sources were missed historically?

## Required output of the later patent pass

For each concept, the later pass should provide:

1. primary-source search log, databases, dates, jurisdictions and query strings;
2. verified family table and current legal status;
3. independent-claim summaries with direct source links;
4. closest-art feature chart against the actual frozen MVP and any future invention variant;
5. explicit separation of novelty, obviousness/inventive step, patent eligibility, and FTO;
6. unresolved claim-construction/legal questions;
7. experiments needed to support or falsify each prospective technical contribution;
8. confidence and limitations;
9. no legal conclusion beyond the evidence and reviewer competence.
<!-- END EMBEDDED SOURCE: 06_Patent_Research_Input_Pack.md -->


