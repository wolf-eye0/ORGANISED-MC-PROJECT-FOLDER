# Project mC Decision Register — TrueMoist Phase 3C Update Patch

**Patch version:** 1.0  
**Date:** 27 July 2026  
**Applies to:** `Project_mC_Decision_Register_v1.0(2).md`  
**Source:** `Phase3C_TrueMoist_Architecture_Report_Final.md`

This patch preserves prior decision history. It updates statuses rather than deleting earlier provisional records.

---

## Update PDR-031

**Decision ID:** PDR-031  
**Title:** TrueMoist Compensation Method  
**Previous state:** Provisional architecture selection  
**New decision or requirement:** Use a univariate raw calibration as the uncompensated baseline, ordinary multivariate linear regression as the modelling baseline, and ridge-regularized second-order regression as the final MVP candidate. Inputs are raw probe response, measured soil temperature, and controlled salinity-treatment code. Train offline and deploy fixed coefficients for local MCU inference.  
**Rationale:** Preserves interpretability and local processing while modelling low-order interactions without TinyML or online-training risk.  
**Decision type:** Final architecture selection  
**Verification status:** Requires prototype validation  
**Current status:** Accepted for Phase 4  
**Carry-forward requirement:** Yes  
**Related:** PDR-032, PDR-045, PDR-048, PDR-049, new PDR-057 to PDR-060.

---

## Update PDR-032

**Decision ID:** PDR-032  
**Title:** TrueMoist ADC Selection  
**Previous state:** Open question  
**New decision or requirement:** Include ADS1115 in the primary prototype and compare it against calibrated ESP32 ADC1 during Week 1. Do not justify it from nominal bit count alone. Retain ADS1115 when it improves pilot noise/RMSE or when its low cost is judged worthwhile for reproducibility; permit calibrated ESP32 ADC1 as fallback.  
**Rationale:** Resolves the Phase 3B uncertainty while preserving an evidence-based fallback.  
**Decision type:** Final architecture selection with mandatory validation gate  
**Verification status:** Partially verified; empirical gate pending  
**Current status:** Accepted for Phase 4  
**Carry-forward requirement:** Yes  
**Related:** PDR-031, PDR-050, new PDR-060.

---

## Update PDR-045

**Decision ID:** PDR-045  
**Title:** TrueMoist Custom Hardware IP Abandonment  
**Previous state:** Recommendation  
**New decision or requirement:** Retain off-the-shelf commodity sensing hardware for the MVP. Do not develop or claim IP over a custom moisture/temperature/EC probe in Phase 4. Focus innovation work on validated compensation workflow, drift/confidence logic, constrained deployment, and calibration methodology.  
**Rationale:** Protects schedule and avoids overclaiming a crowded hardware area.  
**Decision type:** Final MVP scope decision; patent strategy remains a recommendation  
**Verification status:** Accepted  
**Current status:** Accepted  
**Carry-forward requirement:** Yes  
**Related:** PDR-031, new PDR-057.

---

## Update PDR-048

**Decision ID:** PDR-048  
**Title:** TrueMoist Gravimetric Validation Standard  
**Previous state:** Requirement  
**New decision or requirement:** Use dry-basis gravimetric water content as the authoritative reference. Dry at 105 ± 5 °C for at least 24 hours and until constant mass. Use a 0.01 g scale where available. Do not report VWC unless bulk density or a controlled known-volume measurement is separately established.  
**Rationale:** Removes ambiguity between gravimetric and volumetric water content and strengthens traceability.  
**Decision type:** Requirement  
**Verification status:** Pending confirmation of institutional oven/scale access  
**Current status:** Accepted  
**Carry-forward requirement:** Yes  
**Related:** PDR-049, new PDR-058 and PDR-059.

---

## Update PDR-049

**Decision ID:** PDR-049  
**Title:** TrueMoist Single-Soil Limit  
**Previous state:** Provisional architecture selection  
**New decision or requirement:** Restrict calibration and formal validation to one homogeneous soil source and one defined preparation method. No multi-soil or universal transfer claim is permitted in the MVP.  
**Rationale:** Makes the 72-run physical dataset achievable and prevents model confounding.  
**Decision type:** Final MVP scope decision  
**Verification status:** Accepted  
**Current status:** Accepted  
**Carry-forward requirement:** Yes  
**Related:** PDR-031, PDR-048, new PDR-058.

---

## Update PDR-050

**Decision ID:** PDR-050  
**Title:** TrueMoist AFE Soldering  
**Previous state:** Recommendation  
**New decision or requirement:** Breadboard use is permitted only for Week-1 characterization. Freeze the final analog path on soldered perfboard by the end of Week 2, with short analog wiring, local decoupling, deliberate grounding, and fixed connectors.  
**Rationale:** Reduces avoidable electrical variation before the main dataset.  
**Decision type:** Implementation requirement  
**Verification status:** Pending build  
**Current status:** Accepted for Phase 4  
**Carry-forward requirement:** Yes  
**Related:** PDR-032.

---

# New decisions

## PDR-057 — TrueMoist Final Architecture

**Decision ID:** PDR-057  
**Title:** TrueMoist Final MVP Architecture  
**Phase introduced:** Phase 3C  
**Category:** Concept-Specific Architecture (TrueMoist)  
**Decision or requirement:** Freeze a D-dominant architecture with B-style signal hardening: genuine analog capacitive probe, DS18B20, controlled salinity treatments, ESP32-WROOM-32, ADS1115, offline-trained fixed regression coefficients, local inference, USB CSV, and gravimetric validation.  
**Rationale:** Simplest architecture covering the complete hypothesis within budget and schedule.  
**Alternatives:** Minimal internal-ADC demonstrator; live-EC architecture; adaptive embedded calibration.  
**Decision type:** Final architecture selection  
**Verification status:** Requires mandatory early validation  
**Current status:** Accepted  
**Carry-forward requirement:** Yes  
**Related:** PDR-031, PDR-032, PDR-045, PDR-048, PDR-049, PDR-050.

---

## PDR-058 — TrueMoist Dataset Design

**Decision ID:** PDR-058  
**Title:** TrueMoist Physical Dataset Design  
**Phase introduced:** Phase 3C  
**Category:** Validation, Testing & Feasibility  
**Decision or requirement:** Target 72 independent physical runs: 4 moisture levels × 3 temperature levels × 2 salinity treatments × 3 independent replicates. Rapid ADC readings are averaged and never counted as independent samples.  
**Rationale:** Provides factorial coverage while remaining feasible in two months.  
**Alternatives:** 135-run or 180-run designs; ungrouped random splits.  
**Decision type:** Final validation-plan decision  
**Verification status:** Pilot timing pending  
**Current status:** Accepted  
**Carry-forward requirement:** Yes  
**Related:** PDR-048, PDR-049, PDR-059.

---

## PDR-059 — TrueMoist Success Threshold

**Decision ID:** PDR-059  
**Title:** TrueMoist Validation Success Threshold  
**Phase introduced:** Phase 3C  
**Category:** Validation, Testing & Feasibility  
**Decision or requirement:** On untouched physical test replicates, compensated RMSE must be at least 20% lower and compensated MAE at least 15% lower than the uncompensated baseline. Absolute errors and disturbance-subset results must also be reported.  
**Rationale:** Directly tests relative improvement against the same physical reference rather than relying on attractive graphs or training fit.  
**Alternatives:** R²-only success; arbitrary absolute accuracy claim.  
**Decision type:** Requirement  
**Verification status:** Pending final validation  
**Current status:** Accepted  
**Carry-forward requirement:** Yes  
**Related:** PDR-031, PDR-048, PDR-058.

---

## PDR-060 — TrueMoist Mandatory Early Validation Gates

**Decision ID:** PDR-060  
**Title:** TrueMoist Week-1/Week-2 Validation Gates  
**Phase introduced:** Phase 3C  
**Category:** Validation, Testing & Feasibility  
**Decision or requirement:** Before the main dataset, verify probe repeatability, insertion and packing sensitivity, ADC-path value, gravimetric access, salinity-treatment effect, and pilot model feasibility. Apply the documented fallback when a gate fails.  
**Rationale:** Component existence alone does not prove that the full measurement chain is viable.  
**Alternatives:** Proceeding directly to full dataset collection.  
**Decision type:** Mandatory validation gate  
**Verification status:** Pending  
**Current status:** Accepted  
**Carry-forward requirement:** Yes  
**Related:** PDR-032, PDR-048, PDR-050, PDR-057.

---

## PDR-061 — TrueMoist EC/Salinity Boundary

**Decision ID:** PDR-061  
**Title:** TrueMoist Controlled-Salinity Strategy  
**Phase introduced:** Phase 3C  
**Category:** Concept-Specific Architecture (TrueMoist)  
**Decision or requirement:** Treat salinity as a controlled experimental treatment expressed by known salt addition per dry soil mass. Do not include mandatory live soil-EC sensing and do not claim that the treatment code is a bulk/pore-water EC measurement.  
**Rationale:** Preserves salinity-disturbance validation without creating an underdesigned EC instrument.  
**Alternatives:** Direct two-electrode runtime EC; solution-EC proxy as the sole field input.  
**Decision type:** Final architecture selection  
**Verification status:** Salinity pilot pending  
**Current status:** Accepted  
**Carry-forward requirement:** Yes  
**Related:** PDR-031, PDR-057, PDR-060.

---

## PDR-062 — TrueMoist Readiness Classification

**Decision ID:** PDR-062  
**Title:** TrueMoist Phase 4 Readiness  
**Phase introduced:** Phase 3C  
**Category:** Methodology & Project Management  
**Decision or requirement:** Classify TrueMoist as “Architecture Ready with Mandatory Early Validation.” No Phase 3C research rerun is required; Phase 4 begins with PDR-060 gates.  
**Rationale:** One coherent architecture exists, but core physical assumptions remain empirical.  
**Alternatives:** Architecture Ready without gates; Conditionally Ready; Phase 3C rerun.  
**Decision type:** Phase-gate decision  
**Verification status:** Accepted  
**Current status:** Accepted  
**Carry-forward requirement:** Yes  
**Related:** PDR-057, PDR-060.
