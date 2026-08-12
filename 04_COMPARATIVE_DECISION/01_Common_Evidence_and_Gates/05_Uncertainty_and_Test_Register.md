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
