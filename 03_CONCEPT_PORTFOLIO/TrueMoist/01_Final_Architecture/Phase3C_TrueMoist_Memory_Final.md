# Project mC — Phase 3C TrueMoist Memory

**Version:** 1.0  
**Status:** Complete  
**Date:** 27 July 2026  
**Authoritative companion:** `Phase3C_TrueMoist_Architecture_Report_Final.md`

---

## Purpose

This memory reconstructs the final TrueMoist Phase 3C decision without requiring future reviewers to reread the full research corpus.

---

## Final identity

TrueMoist is a low-cost embedded sensing system that improves the trustworthiness of a commodity soil-moisture probe through local compensation of predictable environmental and measurement errors.

It is not an irrigation controller, cloud platform, universal probe, or laboratory instrument.

---

## Final architecture

```yaml
architecture:
  family: "D-dominant with B-style signal hardening"
  readiness: "Architecture Ready with Mandatory Early Validation"

sensing:
  moisture:
    selection: "Genuine analog capacitive probe, SEN0193-class or characterized equivalent"
    quantity: 2
    excluded: "YL-69 / HL-69 as primary probe"
  temperature:
    selection: "Waterproof DS18B20"
    placement: "Same depth, approximately 20–30 mm from moisture probe"
  salinity:
    selection: "Controlled salinity treatment during calibration and validation"
    runtime_live_ec: false

acquisition:
  primary_adc: "ADS1115"
  gate: "Week-1 comparison against calibrated ESP32 ADC1"
  afe: "1 kΩ series + 100 nF input RC, local 100 nF + 10 µF decoupling"
  final_wiring: "Soldered perfboard"

controller:
  primary: "ESP32-WROOM-32 DevKit"
  fallback: "ESP32-S3 DevKit"
  interface: "USB serial CSV"
  power: "USB 5 V"

model:
  baseline_0: "Univariate raw calibration"
  baseline_1: "Multivariate linear regression"
  final_candidate: "Ridge-regularized second-order regression"
  training: "Offline Python"
  inference: "Fixed coefficients on MCU"
  adaptive_training: "Deferred"

dataset:
  soil_types: 1
  design: "4 moisture × 3 temperature × 2 salinity × 3 independent replicates"
  physical_runs: 72
  split: "Replicates 1–2 train/model selection; replicate 3 final test"
  leakage_rule: "Never split rapid readings from the same physical batch"

ground_truth:
  primary: "Dry-basis gravimetric water content"
  drying: "105 ± 5 °C, at least 24 h and until constant mass"
  scale: "0.01 g preferred"
  vwc_claim: "Only if bulk density is independently measured"

success:
  primary: "Held-out compensated RMSE at least 20% lower than uncompensated"
  secondary: "Held-out compensated MAE at least 15% lower"
  guardrail: "No more than 10% MAE worsening in a major disturbance subset"

budget:
  preferred: "≤ ₹3,000"
  maximum: "₹5,000"
  planning_range: "Approximately ₹1,790–₹3,440 depending on institutional equipment"

excluded:
  - "Live DIY soil-EC subsystem"
  - "Custom moisture probe"
  - "AD5933 impedance architecture"
  - "TinyML for MVP"
  - "On-device adaptive training"
  - "Cloud/app dependency"
  - "Irrigation actuator"
  - "Multi-soil generalization"
```

---

## Evidence audit memory

### ChatGPT research

High weight. Strongest combination of concept fidelity, official component evidence, controlled-salinity reasoning, external ADC justification, and experimental caution.

### Perplexity research

Medium-high weight. Strong staged plan and dataset discipline. Correct the PDR numbering and do not freeze internal ADC as default without the comparison gate.

### Gemini research

Retain architecture direction. Reject “ironclad” certainty, over-large sample workload, unqualified VWC claims, and overconfident patent conclusions.

### Mistral research

Exclude moisture-sensor and live-EC sections. It incorrectly describes YL-69/HL-69 as a corrosion-resistant capacitive probe. Retain DS18B20, ESP32, regression, USB, gravimetric, and roadmap elements.

---

## Major resolved disagreements

1. **Probe:** genuine capacitive probe wins; YL-69/HL-69 rejected.
2. **Salinity:** controlled treatment wins; live EC deferred.
3. **ADC:** ADS1115 included, but value tested in Week 1.
4. **Model:** ridge second-order final candidate; linear baseline; adaptive deferred.
5. **Dataset:** 72 runs, not 135 or 180.
6. **Reference:** GWC primary; VWC only with bulk density.
7. **Readiness:** Ready with Mandatory Early Validation.

---

## Early gates

### Week 1

- probe stability and reinsertion;
- ADC comparison;
- oven/scale access;
- monotonic response.

### Week 2

- packing sensitivity;
- salinity-treatment effect;
- pilot grouped model;
- AFE soldering and jig freeze.

---

## Fallback hierarchy

1. Final candidate: ridge-regularized second-order compensation.
2. Model fallback: multivariate linear regression.
3. ADC fallback: calibrated ESP32 ADC1 with 100 nF and 64-sample averaging.
4. Salinity fallback: temperature-only compensated MVP with transparent documentation.
5. Dataset fallback: 54 runs using 3 moisture × 3 temperature × 2 salinity × 3 replicates.
6. Architecture kill: no reliable gravimetric reference or no repeatable probe response.

---

## Phase transition

Phase 3C does not need to be rerun.

Proceed to Phase 4 with procurement and the mandatory Week-1/Week-2 gates. Final component variants, wiring diagrams, firmware, sample SOP, and procurement links belong to Phase 4.
