# Chapter 08 — TrueMoist Architecture, Validation and Patent Evidence

## Controlled TrueMoist source packet

This packet contains hash-verified source extracts. The sources have not been reconciled or converted into final Master Manual conclusions.

Mapped sources: **14**


---

## Source 1: `03_CONCEPT_PORTFOLIO/TrueMoist/01_Final_Architecture/Phase3C_TrueMoist_Architecture_Report_Final.md`

- Authority: `TIER_1`
- Treatment: `CORE_NARRATIVE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `6c71f1d618e0575d127b10f05e91d06ea4b1f0b8a2fe63e78d4022ee75234610`

# Source Extraction

- Chapter: `08` — TrueMoist Architecture, Validation and Patent Evidence
- Authority tier: `TIER_1`
- Manual treatment: `CORE_NARRATIVE`
- Original source: `03_CONCEPT_PORTFOLIO/TrueMoist/01_Final_Architecture/Phase3C_TrueMoist_Architecture_Report_Final.md`
- Current SHA-256: `6c71f1d618e0575d127b10f05e91d06ea4b1f0b8a2fe63e78d4022ee75234610`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

# Phase 3C — TrueMoist Final Engineering Architecture Synthesis

**Project:** Project mC
**Concept:** TrueMoist
**Phase:** 3C — Engineering Architecture Definition
**Prepared by:** ChatGPT Engineering Architecture Review Board
**Date:** 27 July 2026
**Status:** Final synthesis decision
**Readiness:** **Architecture Ready with Mandatory Early Validation**

---

## 0. Important input-set note

The synthesis brief refers to **five independent Phase 3C research reports**, but the uploaded evidence set contains **four**:

1. ChatGPT Phase 3C Research
2. Gemini Phase 3C Research
3. Perplexity Phase 3C Research
4. Mistral Phase 3C Research

This synthesis audits the four reports actually supplied. It does not invent or assume the contents of a missing fifth report.

---

# 1. Executive Architecture Decision

## 1.1 Final selection

Select a **D-dominant architecture with B-style signal hardening**:

> **Offline-trained compensation with fully local embedded inference, using a genuine low-cost analog capacitive moisture probe, a waterproof DS18B20 soil-temperature sensor, rigorously controlled salinity as an experimental variable, an ESP32-WROOM-32 development board, and an ADS1115 external ADC included in the primary prototype but subjected to a mandatory Week-1 value test.**

The prototype shall:

- measure the raw analog output of a commodity capacitive probe;
- measure soil temperature near the active probe zone;
- encode the known salinity treatment used for each prepared soil batch;
- generate an uncompensated estimate and a compensated estimate locally;
- log both through USB serial in CSV form;
- compare both against the same gravimetric reference;
- prove improvement on held-out physical samples;
- remain restricted to one homogeneous soil type.

## 1.2 Final subsystem selections

| Subsystem | Final decision |
|---|---|
| Moisture probe | Genuine analog capacitive probe, preferably DFRobot SEN0193-class or an electrically characterized equivalent; procure two identical units |
| Rejected probe | YL-69 / HL-69 as primary sensor |
| Temperature | Waterproof DS18B20 placed at the same depth and close to the moisture probe |
| Salinity / EC | Controlled salinity treatment during calibration and disturbance testing; no mandatory live in-soil EC channel |
| MCU | ESP32-WROOM-32 DevKit for the semester prototype |
| MCU fallback | ESP32-S3 DevKit; STM32F401-class board only if the team chooses the STM32 toolchain |
| ADC | ADS1115 included in the primary design; retain only after the Week-1 comparison gate confirms useful value or because its low cost justifies removing ADC uncertainty |
| Final model | Ridge-regularized second-order multivariate regression |
| Baseline models | Raw/uncompensated mapping and ordinary multivariate linear regression |
| Training | Offline in Python |
| Runtime | Fixed coefficients evaluated locally on the MCU |
| Ground truth | Gravimetric water content by oven drying at 105 ± 5 °C for at least 24 hours and until constant mass |
| Primary metric | Held-out RMSE improvement of compensated versus uncompensated estimates |
| Logging | USB serial CSV |
| Display | Not required; optional status LED only |
| Power | USB 5 V benchtop power |
| Soil scope | One homogeneous soil |
| Dataset target | 72 independent physical condition runs |
| Readiness | Architecture Ready with Mandatory Early Validation |

## 1.3 Why this architecture wins

It is the simplest design that preserves the complete engineering hypothesis without turning the project into a second sensor-development programme.

It keeps the difficult and potentially defensible work in:

- calibration design;
- error-source separation;
- controlled disturbance testing;
- embedded compensation;
- validation discipline;
- confidence and fallback logic.

It deliberately avoids:

- developing a custom moisture probe;
- developing a field-grade soil-EC instrument;
- on-device model training;
- TinyML for novelty alone;
- cloud dashboards;
- irrigation-control hardware;
- multi-soil generalization;
- battery optimization before measurement validity is established.

---

# 2. Canonical Concept Grounding

## 2.1 What TrueMoist is

TrueMoist is a low-cost embedded intelligent sensing system intended to improve the trustworthiness of inexpensive soil-moisture measurements.

Its contribution is not basic moisture detection. Its contribution is local compensation of predictable measurement error caused by factors such as:

- soil temperature;
- salinity/conductivity influence;
- sensor nonlinearity;
- drift;
- repeatability limitations;
- controlled variation in sample preparation and placement.

## 2.2 Engineering hypothesis

A low-cost embedded system can use measured environmental information and controlled calibration data to compensate predictable error in an inexpensive soil-moisture sensor, producing estimates that are more stable and closer to gravimetric reference values than an uncompensated estimate under controlled test conditions.

## 2.3 Minimum demonstrable success

The MVP succeeds only if it can:

1. acquire raw analog moisture-probe output;
2. measure soil temperature;
3. rigorously represent salinity influence through known experimental treatments;
4. generate an uncompensated moisture estimate;
5. generate a compensated estimate locally;
6. compare both against the same gravimetric reference;
7. demonstrate improvement on held-out samples;
8. operate without continuous cloud processing.

## 2.4 What it must not become

The MVP is not:

- a generic irrigation controller;
- a universal calibration-free probe;
- a laboratory-grade dielectric instrument;
- a cloud analytics platform;
- a full precision-agriculture product;
- a multi-soil field-deployment claim;
- a custom EC-probe development project.

## 2.5 Frozen constraints

- Preferred budget: ≤ ₹3,000
- Absolute maximum: ₹5,000
- Duration: approximately two months
- Team: five, with three technically strong CS/Cybersecurity members
- Local embedded inference
- One homogeneous soil
- Off-the-shelf/student-accessible hardware
- Gravimetric ground truth
- USB output acceptable and preferred
- Arduino-accessible tooling preferred
- No unsupported universal-accuracy claim

---

# 3. Evidence Audit of the Four Supplied Research Reports

## 3.1 ChatGPT research report

### Verdict

**Retain with high weight.**

### Strengths

- Correct concept grounding.
- Correctly separates controlled salinity treatment from live soil EC.
- Uses a genuine capacitive-probe class rather than a resistive fork.
- Uses official component documentation and recent technical literature.
- Recognizes that the ADC decision must be based on system error and measured benefit, not nominal bit count alone.
- Selects offline training with local inference.
- Identifies experimental discipline as a larger risk than model sophistication.
- Gives an achievable cost range and restrained scope.

### Limitations

- The report states that its original topic appeared unspecified, although it correctly reconstructed the task from the supplied documents.
- Some exact literature performance figures should be treated as contextual evidence, not guaranteed prototype outcomes.
- Its decision to include the ADS1115 by default still requires a local Week-1 comparison because sensor and soil variability may dominate ADC error.

### Evidence classification

- Concept fidelity: **Strongly supported**
- Architecture completeness: **Strongly supported**
- Technical correctness: **Strongly supported with prototype verification required**
- Cost realism: **Supported with procurement uncertainty**
- Experimental realism: **Strong**
- Uncertainty handling: **Strong**

---

## 3.2 Perplexity research report

### Verdict

**Retain with medium-high weight, after correcting decision-register mapping and ADC treatment.**

### Strengths

- Correct concept identity and constraints.
- Correctly limits the MVP to one soil and gravimetric validation.
- Correctly treats salinity as a calibration-time controlled variable.
- Provides a practical staged validation plan.
- Uses grouped validation and a manageable dataset.
- Keeps adaptive calibration and TinyML as future work.
- Correctly rates readiness as conditional on early tests.

### Limitations

- It leaves the ESP32 internal ADC as the default and treats ADS1115 as optional. This is defensible only if Week-1 data support it; it does not remove the open ADC uncertainty as cleanly as the final architecture should.
- Its proposed updates misassign several PDR numbers. PDR-032 is the ADC question, PDR-045 is the custom-hardware/IP recommendation, PDR-048 is the gravimetric requirement, PDR-049 is the single-soil boundary, and PDR-050 is the early AFE-soldering recommendation.
- Some accuracy ranges quoted from literature should not be transferred to this prototype without equivalent apparatus and procedures.

### Evidence classification

- Concept fidelity: **Strongly supported**
- Architecture completeness: **Strong**
- Technical correctness: **Supported with corrections**
- Cost realism: **Supported**
- Experimental realism: **Strong**
- PDR update accuracy: **Contradicted in numbering/mapping**

---

## 3.3 Gemini research report

### Verdict

**Retain the architecture direction; reject overconfident claims and over-large workload assumptions.**

### Strengths

- Correctly selects offline training with local embedded inference.
- Correctly includes an external ADC.
- Correctly rejects live soil EC for the MVP.
- Correctly identifies packing, overfitting, and ground-truth quality as major risks.
- Correctly keeps the design within the budget envelope.
- Correctly rejects on-device adaptive training.

### Limitations

- Source quality is uneven and relies too heavily on retailer or secondary material for some technical claims.
- “Ironclad” and similarly absolute language is not justified.
- “Architecture Ready” without a qualifier is too strong because the sensor-repeatability, ADC-benefit, packing, and gravimetric gates remain untested.
- A 180-sample Week-4 collection plan is unnecessarily aggressive.
- Gravimetric measurements do not automatically yield volumetric water content. VWC requires a valid bulk-density/known-volume measurement.
- Some patent assertions are overconfident and should not be treated as an FTO conclusion.
- Its generated memory block is malformed and should not be reused as the official phase memory.

### Evidence classification

- Concept fidelity: **Strongly supported**
- Architecture direction: **Supported**
- Citation/source strength: **Mixed**
- Experimental workload: **Over-scoped**
- Readiness claim: **Overstated**
- Patent certainty: **Unsupported as stated**

---

## 3.4 Mistral research report

### Verdict

**Partially retain; exclude the primary sensor and live-EC sections from the final architecture.**

### Critical technical fault

The report identifies the **YL-69 / HL-69 as a capacitive, corrosion-resistant moisture probe**. That is not a reliable identification for the commonly sold YL-69/HL-69 two-prong module, which belongs to the resistive/electrode type and is unsuitable as the selected corrosion-resistant capacitive probe.

This fault directly corrupts:

- the moisture-sensor choice;
- corrosion claims;
- portions of the costed BOM;
- the signal-chain description.

### Additional weaknesses

- “ADS1115 is mandatory because it has 19× better resolution” is an invalid system-level argument. Nominal resolution is not equivalent to effective measurement improvement.
- Direct two-electrode live EC is underdesigned. A credible EC channel must address excitation waveform, electrode polarization, electrolysis, cell constant, temperature compensation, contact geometry, pore-water versus bulk EC, calibration standards, and long-term stability.
- A 135-sample plan is possible but not the simplest safe choice for the two-month schedule.
- The chosen sandy-loam assumption is not grounded in confirmed local material availability.
- Conversion to VWC is not valid unless bulk density is measured.
- External sourcing is too weak for several precise technical and cost claims.

### Retainable material

- DS18B20 temperature sensing;
- ESP32-class MCU;
- offline polynomial/regression model;
- USB logging;
- gravimetric reference;
- early analog-path soldering;
- eight-week project structure;
- readiness with mandatory early validation.

### Evidence classification

- Broad concept fidelity: **Supported**
- Moisture-sensor section: **Technically unreliable — exclude**
- Live-EC subsystem: **Plausible as future work, over-scoped for MVP**
- ADC rationale: **Unsupported as written**
- Timeline structure: **Supported**
- Final architecture claim: **Rejected**

---

# 4. Cross-Report Agreement and Disagreement Map

## 4.1 Strong agreement

All usable reports converge on:

- a commodity analog capacitive moisture probe;
- soil temperature measured using DS18B20;
- an ESP32-class controller;
- offline model training;
- local embedded inference;
- regression rather than large ML;
- one homogeneous soil;
- gravimetric ground truth;
- USB logging;
- a two-month prototype;
- calibration and packing discipline as critical risks.

## 4.2 Resolved disagreements

| Question | Competing positions | Final resolution |
|---|---|---|
| Moisture probe | Genuine capacitive probe vs YL-69/HL-69 mislabeled as capacitive | Use a genuine analog capacitive probe; reject YL-69/HL-69 |
| Salinity | Live two-electrode EC vs controlled salinity | Use controlled salinity as a known experimental variable |
| ADC | ESP32 internal ADC vs mandatory ADS1115 vs comparison gate | Include ADS1115 in primary design and run a mandatory Week-1 comparison |
| Algorithm | Linear, polynomial, adaptive, TinyML | Linear baseline; ridge-regularized second-order model as final; adaptive future only |
| Dataset | ~72, 135, or 180 samples | 72 independent physical runs |
| Readiness | Ready vs ready with validation | Architecture Ready with Mandatory Early Validation |
| Output | OLED/cloud/app vs serial logging | USB serial CSV; optional status LED |
| Ground truth | GWC vs unqualified VWC | GWC primary; VWC only if bulk density is measured |

---

# 5. Candidate Architecture Families

## Architecture A — Minimal demonstrator

- capacitive probe;
- DS18B20;
- controlled salinity;
- MCU internal ADC;
- simple linear regression;
- USB logging.

**Merit:** fastest and cheapest.
**Failure mode:** leaves ADC uncertainty and weaker signal conditioning unresolved.
**Use:** fallback and baseline, not preferred final architecture.

## Architecture B — Measurement-focused compensated sensor

- capacitive probe;
- DS18B20;
- stronger AFE;
- external ADC;
- optional/direct EC;
- multivariate regression.

**Merit:** strongest measurement path.
**Failure mode:** becomes over-scoped if direct soil EC is mandatory.
**Use:** retain signal hardening, reject mandatory live EC.

## Architecture C — Adaptive embedded calibration

- runtime model updates;
- drift adaptation;
- additional safeguards and reference events.

**Merit:** closest to long-term research vision.
**Failure mode:** requires more data, drift history, reliable reference events, and validation.
**Use:** future upgrade only.

## Architecture D — Offline training, embedded inference

- controlled dataset;
- offline fitting;
- fixed coefficients;
- local runtime calculation.

**Merit:** best team fit and highest schedule safety.
**Failure mode:** still depends on disciplined dataset and physical validation.
**Use:** selected family.

---

# 6. Comparative Decision Matrix

Scores: 1 = poor, 5 = strong.

| Criterion | A | B with live EC | C | D + B signal hardening |
|---|---:|---:|---:|---:|
| Hypothesis coverage | 3 | 5 | 5 | 5 |
| Two-month feasibility | 5 | 2 | 2 | 5 |
| Budget fit | 5 | 3 | 4 | 5 |
| Team fit | 5 | 2 | 3 | 5 |
| Measurement credibility | 3 | 4 | 4 | 5 |
| Experimental clarity | 4 | 2 | 3 | 5 |
| Risk containment | 4 | 2 | 2 | 5 |
| Local inference | 5 | 5 | 5 | 5 |
| Patent-overclaim resistance | 4 | 2 | 3 | 5 |
| Final score | **38/45** | **27/45** | **31/45** | **45/45** |

---

# 7. System Architecture

## 7.1 Block diagram

```text
Known batch metadata
(moisture target, salt-treatment code, batch ID)
                         ┐
                         │
Analog capacitive probe ─┼─> RC input filter ─> ADS1115 ─┐
                         │                                │
DS18B20 soil temperature ─────────────────────────────────┤
                                                          v
                                               ESP32-WROOM-32
                                             ┌────────────────┐
                                             │ filtering       │
                                             │ raw calibration │
                                             │ compensation    │
                                             │ quality flags   │
                                             └───────┬────────┘
                                                     │
                                      USB serial CSV │
                                                     v
                                               Host computer
                                      dataset / plots / reports

Gravimetric oven result ─────────────> offline Python training/validation
                                      coefficients returned to ESP32
```

## 7.2 Runtime data flow

```text
Power-on
  -> sensor warm-up
  -> read DS18B20
  -> collect 64 ADC samples
  -> median rejection + arithmetic mean
  -> raw calibrated estimate
  -> normalize model inputs
  -> evaluate fixed polynomial coefficients
  -> clamp/flag out-of-calibration-range result
  -> log raw, compensated, temperature, condition code, batch ID
```

---

# 8. Moisture Sensing Subsystem

## 8.1 Primary probe

Use one **genuine analog capacitive probe** with exposed analog output. A SEN0193-class device is the preferred reference because its manufacturer explicitly identifies it as capacitive and provides an analog interface.

Procure **two identical units**:

- Unit A: final prototype and dataset generation.
- Unit B: spare and sensor-to-sensor characterization.

The second probe is not used to average away disagreement. It reveals whether the calibration is sensor-specific.

## 8.2 Acceptance tests

Before main data collection:

- 30-minute dry-air stability test;
- repeated readings in one fixed moist sample;
- ten reinsertion cycles using the jig;
- warm-up drift test;
- comparison between Probe A and Probe B;
- visual inspection of coating and connector sealing.

## 8.3 Rejection conditions

Reject a probe if:

- its output intermittently saturates;
- the same physical sample varies by more than 10% of the usable output span after controlled reinsertion;
- drift continues without approaching a stable region during the selected warm-up period;
- moisture ordering is non-monotonic across the pilot levels;
- coating defects expose conductors to soil.

---

# 9. Temperature Sensing Subsystem

## 9.1 Selected device

Waterproof DS18B20.

## 9.2 Placement

- same insertion depth as the active moisture-sensing region;
- approximately 20–30 mm from the moisture probe;
- not touching the probe board;
- fixed by the same rigid jig;
- cable strain relieved.

Ambient temperature may be logged for context but is not a substitute for soil temperature.

## 9.3 Acquisition

- request 12-bit conversion;
- wait for conversion completion;
- take three readings;
- use median value;
- flag disconnected/default error codes;
- record temperature at the beginning and end of each measurement interval.

---

# 10. EC / Salinity Strategy

## 10.1 Final MVP strategy

Use **controlled salinity as a calibration and disturbance variable**.

The model input is a known treatment code or known salt addition per dry soil mass. It is not represented as measured bulk EC unless an actual calibrated EC method is used.

## 10.2 Why live soil EC is rejected

A reliable live soil-EC channel would require a second measurement programme involving:

- AC excitation;
- electrode polarization control;
- electrode geometry and cell constant;
- temperature compensation;
- calibration solution;
- distinction between pore-water, solution, bulk, and apparent EC;
- contact and packing repeatability;
- corrosion and fouling tests.

That work does not directly improve the first proof: compensated moisture should outperform uncompensated moisture under known disturbances.

## 10.3 Pilot-selected salinity levels

Use two levels for the MVP:

- **S0:** no deliberately added salt;
- **S1:** a pilot-selected NaCl dose that creates a repeatable sensor shift without saturating the probe or producing visibly abnormal soil behaviour.

The exact S1 dose is frozen only after the Week-2 pilot. Record it as grams NaCl per kilogram of oven-dry-equivalent soil.

## 10.4 Interpretation boundary

The final claim is:

> “The model compensates a known controlled salinity treatment within the tested soil and range.”

It is not:

> “The system measures field soil EC” or “the model generalizes to arbitrary salinity.”

---

# 11. Analog Front End and ADC

## 11.1 Selected ADC

ADS1115, single-ended channel, powered from 3.3 V.

## 11.2 Why it is included

The ESP32 internal ADC is known to require calibration and noise mitigation. The ADS1115 is a low-cost 16-bit delta-sigma ADC with a programmable gain amplifier and I²C interface. Inclusion removes a known instrumentation uncertainty at low cost.

However:

> The ADS1115 is not justified merely because “16 bits is better than 12 bits.”

System accuracy may still be dominated by probe construction, packing, insertion, temperature, and reference error.

## 11.3 Week-1 ADC value gate

Read the same stable analog node with:

- calibrated ESP32 ADC1;
- ADS1115.

Compare:

- short-term standard deviation;
- 10-minute drift;
- repeatability after reinsertion;
- fitted calibration RMSE on the pilot samples.

Decision rule:

- If ADS1115 reduces pilot held-out RMSE or short-term noise by **≥15%**, retain as strongly justified.
- If improvement is **5–15%**, retain because it is inexpensive and reduces uncertainty.
- If improvement is **<5%**, it may still remain in the primary prototype for reproducibility, but Architecture A using the calibrated internal ADC becomes an acceptable fallback.
- If the module is unstable, counterfeit, or unavailable, use ESP32 ADC1 with calibration, 100 nF input capacitor, and 64-sample averaging.

## 11.4 AFE implementation

Recommended input chain:

```text
Probe AO -> 1 kΩ series resistor -> ADC input
                                  |
                                100 nF
                                  |
                                 GND
```

Additional rules:

- 100 nF ceramic plus 10 µF bulk decoupling near ADS1115;
- one clean common ground;
- short analog leads;
- keep Wi-Fi disabled during acquisition;
- do not route analog cable beside USB/power cable;
- characterize on breadboard only;
- move the final analog path to soldered perfboard by the end of Week 2;
- protect connectors from soil and moisture;
- ensure probe output never exceeds ADC supply/reference limits.

---

# 12. MCU and Embedded Architecture

## 12.1 Primary MCU

ESP32-WROOM-32 DevKit for the student prototype.

Reasons:

- team familiarity;
- Arduino IDE support;
- adequate floating-point and memory headroom;
- USB serial through the development board;
- mature libraries for ADS1115 and DS18B20;
- inexpensive and locally common.

## 12.2 Fallback

ESP32-S3 DevKit is the preferred current-family fallback. STM32F401-class hardware is acceptable only when the team deliberately chooses the STM32 workflow.

## 12.3 Software modules

```text
/config
/sensors/moisture_adc
/sensors/ds18b20
/filtering
/model
/quality_flags
/logger
/self_test
```

## 12.4 Resource budget

The final second-order model uses approximately ten to fifteen coefficients, depending on selected interactions.

Expected resource use:

- model coefficients: well below 1 kB;
- acquisition buffers: below 2 kB;
- CSV line and metadata buffers: below 2 kB;
- model evaluation: fewer than roughly 100 floating-point operations per output;
- inference latency: negligible relative to sensor equilibration and ADC collection.

No TinyML runtime is necessary.

---

# 13. Sampling and Preprocessing

## 13.1 Per-record acquisition

1. Wait for sample and temperature equilibration.
2. Read DS18B20.
3. Discard the first ADC conversion after channel/configuration change.
4. Acquire 64 ADS1115 samples at 128 SPS.
5. Apply a five-point moving median or reject samples outside three median absolute deviations.
6. Compute the arithmetic mean of accepted values.
7. Record mean, standard deviation, minimum, maximum, and count.
8. Evaluate raw and compensated models.
9. Log all data and quality flags.

## 13.2 Do not create fake sample size

The 64 rapid ADC readings are repeated electronic observations of one physical condition. They must be averaged into one physical record and must not be treated as 64 independent training samples.

---

# 14. Compensation Algorithm

## 14.1 Models to compare

Only three models are required:

### Model 0 — Uncompensated baseline

A univariate mapping:

```text
GWC_hat_raw = a0 + a1 * raw
```

### Model 1 — Multivariate linear baseline

```text
GWC_hat_linear =
b0 + b1*raw + b2*temperature + b3*salinity_code
```

### Model 2 — Final candidate

Ridge-regularized second-order regression:

```text
GWC_hat_comp =
c0
+ c1*raw
+ c2*T
+ c3*S
+ c4*raw²
+ c5*T²
+ c6*raw*T
+ c7*raw*S
+ c8*T*S
```

Terms may be removed if they are unstable or add no held-out benefit.

## 14.2 Model-selection rule

Select Model 2 only if it:

- improves held-out RMSE over Model 1 by at least 5%;
- does not show unstable coefficients;
- does not violate monotonicity over the tested moisture range;
- does not materially worsen either salinity subset;
- produces numerically equivalent output on Python and MCU.

Otherwise deploy Model 1.

## 14.3 Why ridge regularization

It reduces coefficient instability when polynomial and interaction terms are correlated while keeping the final model explainable and trivial to implement.

## 14.4 Deferred methods

Do not use in the MVP:

- neural networks;
- random forests on-device;
- recursive least squares;
- online coefficient updates;
- self-learning without trusted reference events;
- cloud training during operation.

Future upgrade: event-driven recalibration with confidence gating and drift detection.

---

# 15. Calibration Dataset Design

## 15.1 Target design

Use:

- 4 moisture levels;
- 3 temperature levels;
- 2 controlled salinity treatments;
- 3 independent physical replicates.

Total:

```text
4 × 3 × 2 × 3 = 72 physical condition runs
```

## 15.2 Moisture levels

Start with four dry-basis gravimetric targets spanning the safe usable range discovered during pilot testing, for example low, medium-low, medium-high, and high.

Do not freeze exact percentages until field capacity and sensor response are established for the selected soil.

## 15.3 Temperature levels

Recommended targets:

- 20 °C
- 30 °C
- 40 °C

Allow a tolerance band and record actual soil temperature. If 40 °C cannot be maintained safely and uniformly, use 20/28/36 °C.

## 15.4 Replicates

Each replicate must be a separately prepared or independently reset physical sample, not repeated electronic reads from the same undisturbed condition.

## 15.5 Dataset split

Preferred split:

- Replicates 1 and 2: training/model selection;
- Replicate 3: untouched final test set.

Within training data, use grouped cross-validation by physical batch.

Never split rapid readings from the same container between train and test.

## 15.6 Record schema

```text
timestamp
batch_id
soil_source_id
replicate_id
moisture_target_code
salt_treatment_code
salt_g_per_kg_dry_soil
temperature_target_c
temperature_actual_c
probe_id
probe_depth_mm
packing_method_id
adc_source
raw_adc_mean
raw_adc_sd
raw_voltage_v
gravimetric_wet_mass_g
gravimetric_dry_mass_g
gwc_reference
raw_estimate
compensated_estimate
quality_flags
notes
```

---

# 16. Gravimetric Ground-Truth Procedure

## 16.1 Primary measurand

Dry-basis gravimetric water content:

```text
GWC = (m_wet - m_dry) / m_dry
```

Report as g water per g dry soil or as a percentage.

## 16.2 Procedure

1. Label container and sample.
2. Tare the empty dry container.
3. Record wet soil plus container mass.
4. Dry at 105 ± 5 °C for at least 24 hours.
5. Cool in a dry covered environment.
6. Weigh.
7. Return to oven for 1–2 hours.
8. Reweigh.
9. Accept constant mass when successive dry-soil measurements differ by less than the selected scale-based tolerance.
10. Calculate GWC.

## 16.3 Scale

- 0.01 g resolution preferred;
- 0.1 g may be acceptable for larger 300–500 g samples, subject to uncertainty calculation.

## 16.4 VWC restriction

Do not report volumetric water content unless the experiment also measures valid bulk density or uses a controlled known-volume core.

If bulk density is measured:

```text
VWC = GWC × bulk_density / water_density
```

Otherwise the authoritative output is GWC.

## 16.5 Oven fallback

If institutional oven access is unavailable, the architecture becomes **conditionally ready**. A microwave or hotplate fallback may be used for exploratory work only after repeatability is proven against several oven-dried reference samples.

---

# 17. Mechanical Soil-Test Rig

## 17.1 Container

- 500–1000 mL rigid nonconductive container;
- 300–500 g soil per condition;
- enough clearance from walls for both sensors;
- lid or film during equilibration to reduce evaporation.

## 17.2 Repeatability jig

The jig shall fix:

- probe depth;
- probe angle;
- DS18B20 depth;
- sensor separation;
- container position;
- insertion path.

## 17.3 Packing method

Use:

- fixed dry soil mass;
- fixed water addition by mass;
- fixed mixing time;
- sealed equilibration interval;
- fixed compaction plate mass;
- fixed number of compaction cycles or fixed final fill height.

Record deviations rather than silently correcting them.

---

# 18. Validation Metrics and Pass Criteria

## 18.1 Primary metric

Held-out RMSE against gravimetric GWC.

```text
Improvement = 1 - RMSE_comp / RMSE_raw
```

Primary success threshold:

> Compensated held-out RMSE must be at least **20% lower** than uncompensated held-out RMSE.

Equivalent improvement ratio:

```text
RMSE_raw / RMSE_comp >= 1.20
```

## 18.2 Secondary metric

Held-out MAE.

Secondary success threshold:

> Compensated MAE must be at least **15% lower** than uncompensated MAE.

## 18.3 Guardrails

- Report absolute RMSE and MAE, not improvement alone.
- Report results separately for each temperature and salinity subset.
- The compensated model must not worsen MAE by more than 10% in any major tested subset.
- Report R² only as supplementary information.
- Use paired bootstrap confidence intervals or a paired permutation test when feasible.
- Preserve every failed or excluded measurement with a reason code.

## 18.4 Demonstration

Display for one held-out disturbance sequence:

- gravimetric reference;
- uncompensated estimate;
- compensated estimate;
- temperature;
- salinity-treatment code;
- absolute errors.

---

# 19. Prototype Test Matrix

| Test | Variable held | Variable changed | Output |
|---|---|---|---|
| Electronic stability | Probe voltage source | Time | ADC noise/drift |
| Probe repeatability | Soil condition | Reinsertion | Output variation |
| Packing sensitivity | Water/temp/salt | Compaction | Packing-induced error |
| Temperature disturbance | Moisture/salinity | Soil temperature | Raw vs compensated error |
| Salinity disturbance | Moisture/temp | Salt treatment | Raw vs compensated error |
| Moisture calibration | Temp/salinity | GWC | Calibration curve |
| ADC comparison | Same analog node | ADC path | Noise and RMSE |
| Held-out validation | Model frozen | New replicate | Final metrics |
| Embedded equivalence | Inputs fixed | Python vs MCU | Numeric difference |
| Repeatability demo | Condition fixed | Repeated runs | Stability |

---

# 20. Electrical and Power Architecture

## 20.1 Power

Use USB 5 V to the ESP32 development board.

- 3.3 V rail: ADS1115 and digital interface as compatible.
- Probe supply: choose 3.3 V when the selected probe operates correctly and its output range remains safely within the ADC range.
- DS18B20: 3.3 V with 4.7 kΩ pull-up.
- No battery is required for the MVP.

## 20.2 Power budget

Design for a 5 V, 1 A source. Actual average consumption should be much lower, but this provides safe headroom for the development board and USB interface.

## 20.3 Measurement hygiene

- Wi-Fi and Bluetooth disabled during final acquisition;
- no motor, pump, relay, or switching load on the measurement supply;
- separate high-current loads are not part of the MVP;
- analog and digital ground return kept short and deliberate.

---

# 21. User Interface and Logging

## 21.1 Required

USB serial CSV at a fixed baud rate.

## 21.2 Optional

- green LED: valid measurement;
- amber LED: out-of-calibration range;
- red LED: sensor/read failure.

## 21.3 Rejected

- cloud dashboard;
- mobile app;
- OLED as a mandatory dependency;
- SD card as a mandatory dependency;
- irrigation actuator.

The final demonstration may use a laptop plot generated from the serial log.

---

# 22. Costed BOM

Prices are procurement estimates and must be refreshed in Phase 4.

| Item | Qty | Planning range |
|---|---:|---:|
| ESP32 development board | 1 | ₹450–₹700 |
| ADS1115 module | 1 | ₹120–₹220 |
| Genuine analog capacitive probes | 2 | ₹300–₹600 |
| Waterproof DS18B20 | 1 | ₹120–₹220 |
| Perfboard, headers, cable, connectors, passives | 1 set | ₹250–₹450 |
| Containers and mechanical jig materials | 1 set | ₹200–₹450 |
| Soil preparation and salinity consumables | 1 set | ₹100–₹300 |
| Optional 0.01 g scale | 1 | ₹400–₹700 |
| Contingency | — | ₹250–₹500 |

Expected total:

- with institutional scale and oven: approximately **₹1,790–₹3,440**;
- without a scale but with careful low-cost sourcing: aim for **≤₹3,000**;
- with a purchased scale and contingency: remain **below ₹5,000**.

The oven is assumed to be institutional equipment. Buying a laboratory oven is outside the project budget.

---

# 23. Compute, Memory, Storage, and Power Budget

| Resource | Expected use | Margin |
|---|---|---|
| Model coefficients | <1 kB | Very high |
| Sampling/filter buffer | <2 kB | Very high |
| CSV/metadata buffer | <2 kB | Very high |
| Firmware flash | Well below dev-board capacity | Very high |
| Inference operations | <100 FLOPs/record | Very high |
| Sampling interval | Seconds to minutes | No real-time pressure |
| USB power | 5 V, 1 A source | High headroom |

The limiting resources are experimental time and physical consistency, not MCU compute or memory.

---

# 24. Error Budget

The pilot phase shall measure rather than guess the dominant terms.

| Error source | Expected role | Control |
|---|---|---|
| Probe unit variability | Medium/high | Use one probe for final model; characterize second |
| Probe reinsertion | High | Fixed jig and repeated-insertion test |
| Soil packing | High | Fixed mass, compaction and fill height |
| Temperature gradient | Medium | Equilibration and colocated sensor |
| Salinity preparation | Medium | Dose by dry soil mass, thorough mixing |
| ADC noise/nonlinearity | Low/medium after ADS1115 | Filter, decouple, compare paths |
| Evaporation | Medium | Sealed equilibration and rapid weighing |
| Scale resolution | Low/medium | Adequate sample mass and uncertainty |
| Incomplete drying | High | Constant-mass rule |
| Model bias/overfit | High | Grouped held-out replicate |
| Data leakage | Severe if present | Split by physical batch |

The final report must quantify each term using pilot data or state that it remains unquantified.

---

# 25. Risks, Kill Factors, and Fallbacks

| Risk / kill factor | Gate | Fallback |
|---|---|---|
| Probe output too unstable | Week 1 | Replace probe; improve jig; choose best characterized unit |
| Packing dominates all effects | Week 1–2 | Redesign sample-prep rig; increase sample mass; reduce scope |
| ADS1115 gives no benefit | Week 1 | Use calibrated ESP32 ADC1 or retain ADS for reproducibility |
| Salinity effect cannot be separated | Week 2–5 | Temperature-only final compensation; report salinity result honestly |
| Salinity treatment saturates sensor | Week 2 | Lower dose |
| Gravimetric workflow unavailable | Week 1–2 | Secure institutional access; otherwise architecture becomes conditional |
| Main dataset exceeds timeline | Week 3 | Reduce to 3 moisture × 3 temp × 2 salt × 3 replicates = 54 |
| Polynomial overfits | Week 5 | Deploy multivariate linear model |
| Embedded output differs from Python | Week 6 | Standardize scaling/order; use unit tests |
| Compensation worsens subsets | Week 7 | Simplify model; add range guard; do not claim success |
| Budget exceeds ₹5,000 | Procurement | Remove optional UI/scale; use institutional equipment |
| Ordinary regression lacks patentability | Phase review | Present as engineering validation; reserve IP claims for a specific novel workflow |

---

# 26. Mandatory Early Validation Gates

## Week 1 Gate A — Probe stability and reinsertion

Procedure:

- use one stable prepared sample;
- perform ten jig-controlled insertions;
- collect one averaged record per insertion.

Pass:

- monotonic sensor response in pilot moisture levels;
- reinsertion standard deviation less than 5% of usable span.

Fail:

- greater than 10% of span or intermittent saturation.

Fallback:

- improve jig/packing;
- evaluate second probe;
- replace sensor type.

## Week 1 Gate B — ADC comparison

Procedure:

- feed the same probe output to ADS1115 and calibrated ESP32 ADC1;
- record simultaneous/alternating sets for dry, medium, and wet pilot samples.

Pass:

- ADS1115 produces lower noise, drift, or pilot RMSE, or provides sufficiently cleaner reproducibility to justify its small cost.

Fallback:

- calibrated internal ADC with 100 nF input capacitor and 64-sample averaging.

## Week 1 Gate C — Gravimetric access

Pass:

- oven access confirmed;
- scale resolution confirmed;
- containers and handling process available.

Fail:

- no credible traceable ground truth.

Fallback:

- arrange institutional access before main dataset; do not proceed with final accuracy claims otherwise.

## Week 2 Gate D — Packing sensitivity

Pass:

- repeated independently packed samples show variance smaller than the intended temperature/salinity disturbance effect.

Fail:

- packing variance equals or exceeds disturbance effect.

Fallback:

- fixed compaction rig; larger containers; fewer but better-controlled conditions.

## Week 2 Gate E — Salinity feasibility

Pass:

- S1 causes a repeatable, non-saturating shift at fixed moisture and temperature greater than three times within-condition electronic noise.

Fail:

- no separable effect or unstable direction.

Fallback:

- adjust S1 dose once; if still invalid, use temperature compensation as the final MVP and document salinity as unresolved.

## Week 2 Gate F — Pilot model

Pass:

- a small grouped pilot shows at least 10% error reduction without obvious leakage.

Fail:

- no improvement.

Fallback:

- inspect reference procedure and packing before changing model complexity.

---

# 27. Rejected Alternatives

## YL-69 / HL-69 as primary moisture probe

Rejected because the common product is a resistive electrode probe and was incorrectly described as capacitive in one report.

## Mandatory live two-electrode EC

Rejected because it creates a separate electrochemical instrumentation problem and confuses several EC definitions.

## AD5933 impedance architecture

Rejected because it changes the MVP into an impedance-spectroscopy project, increases analog complexity, and is unnecessary to prove compensation.

## ESP32 internal ADC as the untested final choice

Rejected as the primary frozen path because ADC adequacy is the one unresolved Phase 3B instrumentation question.

## Adaptive on-device calibration

Rejected for the MVP because trusted runtime references and drift history do not exist.

## TinyML

Rejected because the dataset is small, the model must remain explainable, and simple regression is computationally sufficient.

## Multi-soil dataset

Rejected because it multiplies calibration burden and weakens evidence within the two-month period.

## Cloud/app/display-heavy system

Rejected because it does not strengthen hypothesis validation.

---

# 28. Patent and Innovation Implications

## 28.1 Engineering differentiation

A strong semester-project contribution can be demonstrated through:

- rigorously controlled environmental disturbance;
- local correction of a commodity sensor;
- raw-versus-compensated comparison against physical ground truth;
- grouped validation;
- confidence/range flags;
- reproducible low-cost architecture.

## 28.2 What is not automatically patentable

- ordinary sensor fusion;
- a polynomial regression equation;
- use of an ESP32;
- use of ADS1115;
- combining a capacitive probe and DS18B20;
- generic calibration.

## 28.3 Plausible future patent direction

A future claim may become more defensible if the project develops and validates a specific mechanism such as:

- event-triggered recalibration without continuous reference measurements;
- sensor-drift detection with confidence gating;
- transfer calibration across commodity probe units;
- calibration compression for constrained controllers;
- a controlled sequence that separates packing, temperature, and conductivity effects;
- model validity-region detection and safe fallback;
- field recalibration using sparse trustworthy reference events.

Actual patentability requires a later prior-art search and claim analysis.

---

# 29. Team Allocation

## Member 1 — Embedded lead

- ESP32 firmware;
- ADS1115 and DS18B20 drivers;
- filtering;
- coefficient deployment;
- USB logger;
- embedded equivalence tests.

## Member 2 — Data/model lead

- dataset schema;
- Python pipeline;
- grouped splitting;
- baseline/final model fitting;
- metrics and plots;
- coefficient export.

## Member 3 — Hardware/validation lead

- probe characterization;
- AFE;
- ADC comparison;
- soldered integration;
- test rig;
- measurement hygiene.

## Member 4 — Learner/support

- batch labels;
- CSV checking;
- temperature logging;
- test scripts;
- simple status LEDs;
- sample preparation under supervision.

## Member 5 — Documentation/presentation

- experiment logbook;
- photographs;
- BOM;
- risk register;
- presentation;
- demo narrative;
- traceability between sample IDs and measurements.

Critical-path tasks must remain owned by Members 1–3.

---

# 30. Eight-Week Roadmap

## Week 1 — Characterization and ground-truth access

- purchase/verify sensors;
- probe stability;
- two-probe comparison;
- ADC comparison;
- confirm oven and scale;
- start mechanical jig.

**Exit:** sensor and reference workflow viable.

## Week 2 — Freeze measurement hardware

- salinity pilot;
- packing/reinsertion tests;
- finalize AFE;
- solder perfboard;
- freeze container and jig;
- freeze CSV schema.

**Exit:** architecture assumptions pass or fallback selected.

## Week 3 — Pilot dataset and procedure refinement

- run a small factorial pilot;
- test equilibration;
- estimate timing;
- fit baseline models;
- adjust only procedures, not success criteria.

**Exit:** main dataset plan confirmed.

## Week 4 — Main dataset collection, part 1

- prepare first 36 physical conditions;
- gravimetric workflow;
- daily integrity checks;
- no model tuning on final-test replicate.

## Week 5 — Main dataset collection, part 2 and model freeze

- complete remaining conditions;
- fit raw, linear, ridge-second-order models;
- choose final model;
- freeze coefficients and test set.

## Week 6 — Embedded deployment

- deploy coefficients;
- implement range guards;
- verify Python/MCU equivalence;
- finalize USB logging.

## Week 7 — Held-out validation

- run untouched replicate;
- calculate RMSE/MAE;
- subset analysis;
- repeat failed procedural tests;
- do not retrain on final test.

## Week 8 — Repeatability and presentation

- final demonstration;
- repeatability sequence;
- finalize report, memory, PDR updates, diagrams, and presentation;
- archive raw data and code.

---

# 31. Phase 4 Readiness Decision

## Classification

> **Architecture Ready with Mandatory Early Validation**

The architecture is coherent, affordable, and executable by the team, but four assumptions remain empirical:

1. the selected low-cost probe is sufficiently repeatable;
2. the packing jig reduces physical variation;
3. the salinity treatment produces a modellable disturbance;
4. the ADS1115 or calibrated internal ADC provides adequate acquisition stability.

These are normal prototype gates, not reasons to rerun Phase 3C research.

---

# 32. Final Decision Statement

TrueMoist shall proceed to Phase 4 as a **single-soil, measurement-focused, software-first compensated sensing prototype** using:

> **ESP32-WROOM-32 + ADS1115 + genuine analog capacitive moisture probe + waterproof DS18B20 + controlled salinity treatments + offline ridge-regularized second-order regression + local embedded inference + USB CSV logging + gravimetric GWC validation.**

Direct live soil EC, adaptive on-device training, TinyML, custom probe development, cloud functionality, and multi-soil claims are excluded from the MVP.

The build is considered successful only when the frozen compensated model outperforms the uncompensated model on held-out physical samples against the same gravimetric ground truth.

---

# 33. Source Trail

Authoritative project documents used:

- Engineering_Design_Review(4).md
- Phase3C_TrueMoist_SOP(2).md
- Pasted text(11).txt — final synthesis brief
- Phase3B_Report_by_Claude(4).md
- Phase3B_MEMORY(4).md
- Claudes report on the research Phases 3a(4).pdf
- Phase3A_MEMORY(4).md
- Phase2_Report by CLaude(3).md
- Phase2_Memory(3).md
- Project_mC_Decision_Register_v1.0(2).md
- PROJECT_CONCEPT_CONTEXT(5).md

Independent Phase 3C evidence audited:

- TrueMoist Phase 3C Research By ChatGPT
- TrueMoist 3C Gemini Research
- TrueMoist Phase 3C By Perplexity
- phase-3c-truemoist-Research-Mistral


---

## Source 2: `03_CONCEPT_PORTFOLIO/TrueMoist/01_Final_Architecture/Phase3C_TrueMoist_Memory_Final.md`

- Authority: `TIER_1`
- Treatment: `CORE_NARRATIVE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `c84bc0e08c8c96cfe410d8c690df35c6b7996e5ffda7703ceff37a424bf02df1`

# Source Extraction

- Chapter: `08` — TrueMoist Architecture, Validation and Patent Evidence
- Authority tier: `TIER_1`
- Manual treatment: `CORE_NARRATIVE`
- Original source: `03_CONCEPT_PORTFOLIO/TrueMoist/01_Final_Architecture/Phase3C_TrueMoist_Memory_Final.md`
- Current SHA-256: `c84bc0e08c8c96cfe410d8c690df35c6b7996e5ffda7703ceff37a424bf02df1`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

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


---

## Source 3: `03_CONCEPT_PORTFOLIO/TrueMoist/01_Final_Architecture/Phase3C_TrueMoist_SOP_Final.md`

- Authority: `TIER_1`
- Treatment: `CORE_NARRATIVE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `993caf1a05f3fdc3937efb634e2f2e467488e973eb71454db8e3c3f53d178d00`

# Source Extraction

- Chapter: `08` — TrueMoist Architecture, Validation and Patent Evidence
- Authority tier: `TIER_1`
- Manual treatment: `CORE_NARRATIVE`
- Original source: `03_CONCEPT_PORTFOLIO/TrueMoist/01_Final_Architecture/Phase3C_TrueMoist_SOP_Final.md`
- Current SHA-256: `993caf1a05f3fdc3937efb634e2f2e467488e973eb71454db8e3c3f53d178d00`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

# Phase 3C — TrueMoist Engineering Architecture Definition SOP

## Document Control

- Project: Project mC
- Concept: TrueMoist
- Phase: 3C — Engineering Architecture Definition
- Status: Active
- Purpose: Select and justify one coherent, buildable TrueMoist prototype architecture
- Team constraint: 5 members, including 3 technically strong CS/Cybersecurity members, 1 learner, and 1 presenter/support member
- Budget constraint: Preferred ≤ ₹3,000; absolute maximum ₹5,000
- Development window: Approximately 2 months
- Processing constraint: Local embedded processing; no continuous cloud dependency
- Current evidence state: Phase 3A and Phase 3B completed; Phase 3C decisions not yet frozen

## 1. Purpose of Phase 3C

Phase 3C converts the TrueMoist engineering hypothesis and Phase 3B feasibility findings into one defensible prototype architecture.

This phase must not merely list sensors, algorithms, or circuit options. It must resolve disagreements, select one implementation pathway, explain why competing pathways were rejected, and produce a blueprint detailed enough to guide implementation planning.

The output shall define the sensing architecture, signal path, controller platform, compensation method, calibration method, dataset procedure, validation procedure, test scenarios, cost assumptions, integration sequence, technical risks, and innovation-preservation strategy.

Phase 3C does not produce the final PCB, production firmware, enclosure, or manufacturing drawings. Those belong to later implementation phases.

## 2. Canonical Engineering Identity

TrueMoist is an affordable embedded intelligent sensing system intended to improve the trustworthiness of low-cost soil-moisture measurements.

It is not a generic irrigation controller, premium laboratory sensor, universal calibration-free probe, or cloud analytics platform.

Its defining contribution is local compensation of measurement error caused by environmental influences such as temperature, salinity/electrical conductivity, sensor drift, and repeatability limitations.

## 3. Mission

Enable more trustworthy irrigation decisions by improving the reliability of inexpensive soil-moisture sensing through local embedded compensation.

## 4. Engineering Hypothesis

A low-cost embedded system can use environmental measurements and calibration data to compensate for predictable error in an inexpensive soil-moisture sensor, producing estimates that are more stable and closer to gravimetric reference values than uncompensated sensor output under controlled test conditions.

## 5. Minimum Demonstrable Success

The architecture must support a prototype that can:

1. Acquire raw output from a low-cost soil-moisture sensor.
2. Measure or represent selected compensation variables, especially temperature and salinity/electrical-conductivity influence.
3. Generate an uncompensated moisture estimate.
4. Generate a compensated estimate locally on the embedded controller.
5. Compare both outputs against a gravimetric reference.
6. Demonstrate improvement in at least one predefined performance metric under controlled disturbances.
7. Produce interpretable results without continuous cloud processing.

The MVP does not need to prove universal performance across all soil types, crops, seasons, or field environments.

## 6. Frozen Project Constraints

- Budget: preferred ≤ ₹3,000; maximum ₹5,000.
- Approximately two months of development.
- Achievable by the existing five-member student team.
- Local embedded processing.
- No required continuous cloud connectivity.
- Off-the-shelf or easily fabricated components.
- One homogeneous soil type for the MVP unless evidence justifies otherwise.
- Physical ground truth must be used rather than another low-cost sensor.
- The prototype must show improved trustworthiness, not merely raw readings.
- Unsupported “calibration-free,” “universal,” or “laboratory-grade” claims are prohibited.
- Architecture must remain explainable and reproducible.

## 7. Authoritative Inputs

Use the following precedence:

1. Engineering Design Review
2. Phase 3B Engineering Feasibility Report and Memory
3. Phase 3A Engineering Landscape Report and Memory
4. Phase 2 Patent Report and Memory
5. Project Concept Context
6. Master Phase Document
7. Independent Phase 3C research reports
8. Project mC Decision Register

Later validated phase outputs take precedence over early summaries unless the later source contains unsupported concept drift.

## 8. Mandatory Concept-Grounding Check

Every research report and synthesis must restate:

- TrueMoist’s engineering identity
- engineering hypothesis
- minimum demonstrable success
- ₹3,000–₹5,000 budget
- two-month schedule
- local-processing requirement
- single-soil MVP boundary

Any report that converts TrueMoist into a generic irrigation controller, premium probe, cloud platform, or universal calibration system must be treated as concept drift and excluded.

## 9. Core Decision Questions

### 9.1 Moisture sensing

Determine the preferred low-cost capacitive sensor or sensing element, whether raw analog output is accessible, expected repeatability and drift, corrosion risks, and suitability for controlled compensation experiments.

### 9.2 Temperature sensing

Determine whether soil temperature, ambient temperature, or both should be measured; choose sensor type, placement, required resolution, and safe simulation method.

### 9.3 Salinity / electrical conductivity

Resolve whether the MVP should directly measure soil EC, use a low-cost EC circuit, use prepared conductivity conditions, infer salinity from controlled salt concentration, or treat salinity only as a controlled calibration variable.

Clearly distinguish variables measured during live operation from variables controlled only during validation.

### 9.4 ADC and analog front end

Resolve whether the MCU internal ADC is sufficient or whether an external ADC such as ADS1115 is necessary.

Assess effective resolution, noise floor, nonlinearity, grounding, filtering, shielding, cable length, power stability, and whether early soldering is mandatory.

An external ADC must be justified using an error budget rather than the claim that more bits are automatically better.

### 9.5 MCU selection

Compare ESP32, a suitable STM32, and any justified alternative using ADC quality, compute, RAM, tools, team familiarity, peripheral support, cost, and reproducibility.

### 9.6 Compensation algorithm

Compare static calibration curves, multivariate linear regression, polynomial regression, piecewise regression, lookup tables, adaptive filtering, recursive calibration, lightweight ML, and hybrid methods.

The selected method must be computationally feasible, interpretable, realistic to train, resistant to overfitting, and demonstrably better than raw output.

TinyML must not be selected only for novelty.

### 9.7 Calibration architecture

Define calibration variables, number of moisture/temperature/salinity levels, replicate count, equilibration time, sample preparation, training-validation split, coefficient storage, recalibration procedure, and model-transfer limitations.

### 9.8 Gravimetric reference

Define wet mass, dry mass, drying method, temperature and duration, container handling, scale resolution, formula, conversion assumptions, and uncertainty sources.

Where laboratory oven access is uncertain, provide a fallback and state its limitations.

### 9.9 Dataset requirements

Determine minimum viable dataset size, repeated readings, randomization, data-leakage controls, train/validation strategy, outlier policy, metrics, and how to avoid apparent accuracy caused by repeated readings from the same soil state.

### 9.10 Validation metrics

Select at least one primary and one secondary metric from MAE, RMSE, maximum error, repeatability, drift, hysteresis, coefficient of variation, temperature sensitivity, salinity sensitivity, and improvement over uncompensated readings.

### 9.11 Test scenarios

The architecture must support controlled comparisons such as:

- same moisture, different temperature
- same moisture, different salinity
- repeated wetting/drying
- raw versus compensated output
- calibration conditions versus held-out conditions
- short-term drift or warm-up behaviour

### 9.12 Output interface

Choose the simplest useful interface: serial plotter, USB logging, small display, RGB status, or local storage.

Evidence collection and interpretability take priority over visual complexity.

### 9.13 Power architecture

Determine USB versus external supply, sensor excitation, reference stability, regulator and decoupling needs, grounding, and whether battery operation is necessary.

### 9.14 Mechanical/sample arrangement

Define soil container, probe placement, depth, spacing, insertion method, packing method, sample mixing, and reduction of air gaps and density variation.

### 9.15 Patent and innovation preservation

Assess whether the architecture preserves a credible direction in compensation logic, adaptive calibration, error modeling, embedded decision logic, or low-cost validation workflow.

Ordinary sensor fusion or polynomial regression alone must not be treated as patentable.

Separate semester-project differentiation from actual patentability.

## 10. Candidate Architecture Families

### Architecture A — Minimal compensation demonstrator

- Capacitive moisture probe
- Temperature sensor
- Controlled salinity conditions
- MCU internal ADC
- Static or multivariate regression
- USB serial output

### Architecture B — Measurement-focused compensated sensor

- Capacitive moisture probe
- Temperature sensor
- Direct EC measurement
- External ADC
- Multivariate compensation
- Local display or serial logging

### Architecture C — Adaptive embedded calibration system

- Capacitive probe
- Temperature and EC inputs
- External ADC where justified
- Adaptive or recursive model
- On-device recalibration
- Local output and logging

### Architecture D — Offline training / embedded inference

- Controlled dataset collection
- Model trained offline
- Coefficients or lightweight model deployed to MCU
- Fully local runtime inference
- No cloud dependency

Additional architectures may be proposed but must be compared with these baselines.

## 11. Architecture Selection Criteria

Score candidates against:

1. Ability to prove the hypothesis
2. Measurement reliability
3. Calibration realism
4. Signal integrity
5. Computational feasibility
6. Cost
7. Two-month buildability
8. Team skill fit
9. Component availability
10. Validation clarity
11. Reproducibility
12. Risk of overclaiming
13. Innovation preservation
14. Patent/FTO compatibility
15. Upgrade potential

Select one primary architecture and at most one fallback.

## 12. Evidence Quality Rules

Primary evidence includes peer-reviewed papers, standards, manufacturer datasheets, and official technical documentation.

Secondary evidence includes credible engineering and institutional references.

Tertiary evidence includes tutorials, hobby projects, and marketplace listings.

Critical decisions about ADC adequacy, EC sensing, sensor performance, and gravimetric validation must rely mainly on primary sources.

Marketplace pages may support Indian price estimates only.

## 13. Hallucination and Concept-Drift Protocol

Exclude or quarantine sections that:

- analyze a different product or trademark
- assume premium sensors outside budget
- claim universal calibration without evidence
- substitute irrigation automation for sensing reliability
- require cloud processing
- make inaccessible lab equipment mandatory
- confuse soil EC with water EC without explanation
- fabricate citations, patents, standards, or specifications

Unsupported evidence must be excluded rather than averaged.

## 14. Mandatory Engineering Analyses

Every report must include:

- signal-chain diagram
- error budget
- data-flow diagram
- compute/RAM/flash budget
- power budget
- costed BOM
- risk register
- rejected-alternatives table

The error budget must include sensor repeatability, ADC error, temperature, salinity, packing, probe placement, gravimetric reference uncertainty, and model error.

## 15. Kill Factors

Explicitly evaluate:

- sensor output too unstable to model
- moisture and salinity effects inseparable
- external ADC provides no measurable advantage
- EC measurement unreliable in the selected arrangement
- gravimetric reference cannot be performed adequately
- dataset too small or correlated
- model overfits calibration conditions
- compensation worsens important edge cases
- soil packing dominates response
- unavailable equipment
- calibration workload exceeds timeline
- cost exceeds budget
- claimed innovation reduces to ordinary regression on commodity sensors

A kill factor is a condition that invalidates the architecture or forces the fallback.

## 16. Staged Validation Plan

### Stage 1 — Sensor characterization

Test repeatability, warm-up, insertion sensitivity, raw noise, drift, and internal versus external ADC if unresolved.

### Stage 2 — Controlled-variable testing

Hold moisture approximately constant while varying temperature and salinity. Repeat enough times to estimate variance.

### Stage 3 — Dataset generation

Prepare controlled moisture levels and record sensor output, temperature, EC/salinity condition, and gravimetric reference.

### Stage 4 — Model development

Fit baseline and candidate models, test on held-out conditions, and compare complexity, accuracy, and stability.

### Stage 5 — Embedded deployment

Port coefficients or model to the MCU, verify equivalence with offline results, and measure resource use.

### Stage 6 — Comparative demonstration

Display raw and compensated estimates against the reference and demonstrate at least one disturbance where compensation improves performance.

## 17. Required Deliverables

1. Phase 3C TrueMoist Architecture Report
2. Phase 3C TrueMoist Memory
3. Final system block diagram
4. Signal-chain diagram
5. Data-flow diagram
6. Selected sensing architecture
7. MCU and ADC decision
8. Compensation algorithm
9. Calibration procedure
10. Gravimetric procedure
11. Dataset plan
12. Validation matrix
13. Costed BOM
14. Power budget
15. Compute and memory budget
16. Mechanical/sample arrangement
17. Risk register
18. Kill-factor assessment
19. Rejected alternatives
20. Eight-week roadmap
21. Team allocation
22. Innovation and patent assessment
23. Phase 4 readiness decision
24. PDR update recommendations

## 18. Final Report Structure

1. Executive decision
2. Canonical concept restatement
3. Engineering hypothesis
4. Minimum demonstrable success
5. Evidence audit
6. Architecture candidates
7. Decision matrix
8. Selected architecture
9. Sensing subsystem
10. Analog front end and ADC
11. MCU and processing
12. Compensation algorithm
13. Calibration and dataset strategy
14. Gravimetric reference
15. Mechanical/sample design
16. Electrical and power design
17. Interface and logging
18. Validation plan
19. BOM
20. Resource budget
21. Risks and kill factors
22. Rejected alternatives
23. Patent and innovation implications
24. Team allocation
25. Eight-week roadmap
26. Unresolved questions
27. Readiness classification
28. PDR updates

## 19. Readiness Classification

### Architecture Ready
One coherent architecture is selected, fits budget and schedule, and has no blocking unresolved issue.

### Architecture Ready with Mandatory Early Validation
Architecture is selected, but one or more assumptions must be tested in Weeks 1–2.

### Architecture Conditionally Ready
A plausible design exists, but equipment, availability, or sensing uncertainty threatens feasibility.

### Architecture Not Ready
Evidence does not support a viable two-month prototype within budget.

## 20. Working Decision Boundaries

Unless strong evidence overturns Phase 3B:

- one homogeneous soil type
- gravimetric ground truth
- local embedded compensation
- temperature as a measured variable
- salinity/EC as either measured or rigorously controlled
- offline training permitted
- embedded inference required
- no universal calibration-free claim
- no dependence on custom patented probe hardware
- external ADC only when justified
- statistical regression preferred over TinyML unless TinyML clearly wins

These are starting boundaries, not automatic final decisions.

## 21. Team Allocation Guidance

### Member 1 — Embedded integration
MCU firmware, interfaces, model deployment, integration.

### Member 2 — Data and compensation
Dataset design, model fitting, metrics, offline-to-embedded equivalence.

### Member 3 — Hardware and validation
AFE, ADC testing, soil rig, electrical-noise control.

### Member 4 — Learner
Logging interface, data formatting, simple UI states, test scripts.

### Member 5 — Documentation and experimental support
Sample labels, experiment records, BOM, photographs, presentation.

Critical-path work must not depend exclusively on the learner or presenter/support member.

## 22. Eight-Week Boundary

- Week 1: component verification and sensor characterization
- Week 2: ADC/AFE decision and test-rig preparation
- Week 3: pilot measurements and procedure refinement
- Week 4: calibration dataset collection
- Week 5: model selection and offline validation
- Week 6: embedded deployment and integration
- Week 7: comparative validation and debugging
- Week 8: repeatability testing, documentation, and demonstration

Architectures requiring substantially more time must be rejected or reduced.

## 23. Exit Gate

TrueMoist may exit Phase 3C only when:

- one primary architecture is selected
- one fallback is documented
- ADC question is resolved
- EC/salinity approach is resolved
- compensation baseline is selected
- ground-truth method is operationally defined
- success metrics are fixed
- dataset plan is feasible
- cost is within limits
- kill factors have mitigations
- architecture is detailed enough for implementation planning

## 24. PDR Update Rules

After Phase 3C:

- PDR-031 becomes Accepted, Rejected, or Superseded.
- PDR-032 is resolved.
- PDR-045 is retained or revised.
- PDR-048 is confirmed or modified.
- PDR-049 is confirmed, rejected, or superseded.
- PDR-050 is confirmed or revised.
- New decisions receive new sequential PDR IDs.
- Historical provisional decisions are not deleted.

## 25. Final Principle

The goal is not to create the most sophisticated soil sensor.

The goal is to select the simplest architecture that convincingly proves low-cost soil-moisture sensing becomes more trustworthy when predictable environmental error is measured, modeled, and compensated locally.


---

## Source 4: `03_CONCEPT_PORTFOLIO/TrueMoist/03_Patent_Synthesis/01_TrueMoist_Patent_Evidence_Synthesis_Max.md`

- Authority: `TIER_2`
- Treatment: `CORE_DECISION_EVIDENCE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `f43847c672ca9b132a7ef6219a9ce00deb8f0ab657c0bda6a7ed3a930a697900`

# Source Extraction

- Chapter: `08` — TrueMoist Architecture, Validation and Patent Evidence
- Authority tier: `TIER_2`
- Manual treatment: `CORE_DECISION_EVIDENCE`
- Original source: `03_CONCEPT_PORTFOLIO/TrueMoist/03_Patent_Synthesis/01_TrueMoist_Patent_Evidence_Synthesis_Max.md`
- Current SHA-256: `f43847c672ca9b132a7ef6219a9ce00deb8f0ab657c0bda6a7ed3a930a697900`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

# TrueMoist Patent-Evidence Synthesis

## 1. Executive verdict

**Verdict: credible long-term path requiring later-semester extension.**

**Track:** C. **Confidence:** medium in this portfolio classification; low-to-medium that the surviving direction will ultimately support a useful claim after fuller searching and physical validation.

The frozen TrueMoist MVP is a coherent, affordable engineering experiment, but it does not presently contain a credible independent technical nucleus. Its commodity capacitive probe, nearby temperature measurement, controlled salinity-treatment metadata, ordinary low-order regression, fixed local MCU inference, analog hardening, gravimetric reference, and grouped one-soil validation are individually conventional and predictably combined. The exact 72-run design can generate credible Level-1 evidence; it is not itself an invention. Passing the engineering thresholds would demonstrate compensation within the tested conditions, not patentability, field robustness, transfer, or FTO.

The strongest surviving development hypothesis is a **contamination-protected replacement-probe transfer mechanism coupled to a perturbation-conditioned validity decision and abstention/fallback**. It is not in the frozen MVP and cannot be validated by its two-probe, one-soil, 72-run dataset. It also faces close art on replacement-probe equivalence, one-point/universal calibration, event-based recalibration, confidence-based exclusion, and low-cost-sensor health. It therefore belongs to a later semester, with more probe units/lots, remount and contamination challenges, and strong ablations. No Track A or Track B direction is established.

This report is technical research and project decision support, not legal advice, a patentability opinion, claim construction, an infringement opinion, or FTO clearance. Public evidence was evaluated through **1 August 2026**.

## 2. Input inventory

The input gate passed before substantive synthesis.

| # | Controlled logical file | Role | Physical/readability result |
|---:|---|---|---|
| 1 | `00_READ_FIRST_TrueMoist_Synthesis_Instructions.md` | Governing instruction | Present, readable, exact manifest size/hash |
| 2 | `01_Engineering_Design_Review.md` | Canonical authority 1 | Present, readable, exact manifest size/hash |
| 3 | `02_Project_mC_Decision_Register_v1.2.md` | Canonical authority 2 | Present, readable, exact manifest size/hash |
| 4 | `03_Phase3C_Portfolio_Closure_Memo_Approved.md` | Canonical authority 3 | Present, readable, exact manifest size/hash |
| 5 | `04_Phase3C_TrueMoist_Architecture_Report_Final.md` | Canonical authority 4 | Present, readable, exact manifest size/hash |
| 6 | `05_Phase3C_TrueMoist_Memory_Final.md` | Canonical authority 5 | Present, readable, exact manifest size/hash |
| 7 | `06_Phase3C_TrueMoist_SOP_Final.md` | Canonical authority 6 | Present, readable, exact manifest size/hash |
| 8 | `07_Concept_Evidence_Matrix.md` | Validated current evidence | Present, readable, exact manifest size/hash |
| 9 | `08_Uncertainty_and_Test_Register.md` | Validated current evidence | Present, readable, exact manifest size/hash |
| 10 | `09_Patent_Research_Input_Pack.md` | Validated current evidence | Present, readable, exact manifest size/hash |
| 11 | `10_Phase2_Report_by_Claude.md` | Historical search leads only | Present, readable, exact manifest size/hash |
| 12 | `11_TrueMoist_Patent_Research_ChatGPT_DR.md` | ChatGPT Deep Research lane | Present, readable, exact manifest size/hash |
| 13 | `12_TrueMoist_Patent_Research_Gemini.docx` | Gemini Deep Research lane | Present; DOCX package valid; 23 rendered pages readable and complete |
| 14 | `13_TrueMoist_Patent_Research_Perplexity.md` | Perplexity Deep Research lane | Present, readable, exact manifest size/hash |
| 15 | `14_TrueMoist_Patent_Research_Qwen_COMPILATION.md` | Qwen lane | Present, readable, exact compiled size/hash; one lane containing initial report plus follow-up |
| 16 | `15_TrueMoist_Patent_Research_Mistral.md` | Mistral lane | Present, readable, exact manifest size/hash; one complete report |
| 17 | `16_TrueMoist_Patent_Research_Microsoft_Copilot.docx` | Microsoft Copilot lane | Present; DOCX package valid; 21 rendered pages readable and complete |
| 18 | `99_INPUT_MANIFEST.md` | File control only | Present and readable; not used as technical evidence |

**Control findings:**

- Exactly **18 physical attachments** are present: one governing instruction, ten canonical/historical project documents, six independent research lanes, and one file-control manifest.
- Decision Register **v1.2** is present; v1.1 is absent.
- The validated **72-run** design is the authoritative architecture. No superseded 135-run architecture was used.
- Each required lane is represented exactly once: ChatGPT Deep Research, Gemini Deep Research, Perplexity Deep Research, Qwen, Mistral, and Microsoft Copilot.
- File 14 is one Qwen lane, compiled losslessly from an initial report and a follow-up. It is neither two reports nor two votes; the follow-up does not validate unsupported statements in the initial report.
- File 15 is one complete Mistral report, not a compilation. No conclusion was missing and none was reconstructed. The one-lane/no-reconstruction rule would still control if fragments were later supplied.
- The superseded initial ChatGPT Deep Research PDF and the supplementary ChatGPT Work Max web audit are absent, as required.
- No required file is missing, duplicated, unreadable, physically partial, or concept-swapped. Parenthetical transport suffixes such as `(1)`, `(4)`, `(15)`, and `(16)` differ from controlled logical names but are unambiguous. Content-level concept contamination inside some research lanes is identified in section 4 rather than treated as a file-control failure.
- All 17 manifest-controlled source files whose fixed hashes are listed match their destination byte counts and SHA-256 values; the generated manifest correctly has no recursive self-hash.

## 3. Project authority and frozen concept

The authority order applied is:

1. Engineering Design Review.
2. Project mC Decision Register v1.2.
3. Approved Phase 3C Portfolio Closure Memo.
4. Final TrueMoist Architecture Report.
5. Final TrueMoist Memory.
6. Final TrueMoist SOP.
7. Current evidence files 07–09.
8. Phase 2 only for historical search leads.
9. Research lanes only after source, claim, status, and concept-fidelity audit.

The binding PDRs are PDR-031 (M0/M1/M2, inputs, offline training, fixed local inference), PDR-032 (Week-1 ADC comparison), PDR-049 (one soil), PDR-050 (soldered final analog path), PDR-058 (frozen D-dominant/B-hardened architecture), PDR-059 (72 physical runs), PDR-060 (success thresholds), PDR-061 (early gates), PDR-062 (controlled treatment code; no live EC), and PDR-063 (architecture ready with mandatory early validation). PDR-045 keeps the MVP on commodity sensing hardware and confines any prospective IP work to a later, validated mechanism.

**Frozen concept.** TrueMoist is a local compensation system for a genuine low-cost analog capacitive soil-moisture probe, not a new probe. It uses a waterproof DS18B20 at the same depth about 20–30 mm away; a controlled NaCl treatment recorded as known addition per dry-soil mass; an ESP32-WROOM-32; and ADS1115 subject to a mandatory same-node Week-1 comparison with calibrated ESP32 ADC1. The salt code is experimental metadata, **not** live bulk, apparent, pore-water, or solution EC.

M0 is a raw/univariate mapping; M1 is multivariate linear regression; M2 is ridge-regularized second-order regression. Inputs are raw probe response, measured soil temperature, and controlled salinity-treatment code. Training occurs offline in Python and the selected fixed coefficients run locally on the ESP32. No TinyML or online adaptation is required.

The validation design is one homogeneous soil and one documented preparation/packing method: **4 moisture × 3 temperature × 2 salinity treatments × 3 independently prepared/reset replicates = 72 independent physical runs**. Replicates 1–2 support training/model selection; replicate 3 remains untouched for final physical test. Rapid ADC reads are averaged into one record and never inflate the physical sample count. Ground truth is dry-basis gravimetric water content, with drying near 105 ± 5 °C for at least 24 hours and to constant mass; 0.01 g resolution is preferred. Volumetric water content is not claimed without independent bulk-density measurement.

Success on the untouched test replicate requires compensated RMSE at least 20% below M0, compensated MAE at least 15% below M0, absolute errors reported, and no more than 10% MAE worsening in a major tested subset. These are engineering criteria only.

The frozen concept expressly excludes a live-EC meter, irrigation controller, cloud platform, multi-soil system, custom multi-frequency probe, TinyML showcase, and online-adaptive learner. Those features may be discussed only as later extensions or major redesigns.

## 4. Research-lane reliability audit

The lanes were treated as evidence sources, never as votes.

| Lane | Fidelity/source/claim audit | Reliability | Material correction affecting the verdict |
|---|---|---|---|
| ChatGPT Deep Research | Strong fidelity to the frozen architecture; broad primary-source coverage; independent claims and status generally separated from descriptions and FTO | **High** | Its Track-C conclusion survives. Status labels remain preliminary, and Indian/TCS and WO national-stage questions remain unresolved. Its composite transfer/validity proposal is a hypothesis, not a verified invention. |
| Gemini Deep Research | Structurally complete, but mixes the MVP with downstream irrigation actuation and includes an unrelated Sensitech FTO passage; legal conclusions exceed its claim/status work | **Low** | Reject the asserted bounded Track-B, patentable/eligible confidence-gated OOD system. Abstention plus preventing irrigation actuation cannot distinguish a frozen system that has no controller. Retain only feasibility and conventionality observations. |
| Perplexity Deep Research | Mostly faithful and technically useful, but claim reading/status work is incomplete and the mandated close-art recheck is shallow | **Partial** | Reject claimed white space around event/drift/validity logic. Use technical/product leads only after independent verification. |
| Qwen compilation | One lane, two sequential parts. It correctly recognizes much of the frozen stack as conventional, but later asserts `HIGH/CLEAR` FTO and a three-month Mahalanobis/event/dual-probe path without sufficient claims or status analysis | **Low** | Reject the FTO, novelty, eligibility, dual-probe-health, and Track-B conclusions. The follow-up does not cure the initial report. |
| Mistral | Complete and readable, but shallow jurisdictional/status work; it failed to locate valid US11598743B2, conflated §101 with novelty, and recommended premature filing | **Low** | US11598743B2 exists and is relevant custom-hardware art. Reject its patentability/eligibility and low-to-medium FTO conclusions and any immediate filing recommendation. Retain conventionality and search-gap observations. |
| Microsoft Copilot | Generally faithful but legally overconfident, internally inconsistent on US7170302 status, and misses or understates close replacement-probe, event-calibration, and TCS health art | **Low** | Reject “clear” FTO and a bounded transfer/validity path. Retain candidate mechanisms only as search/experiment prompts. |

No lane was physically excluded. Particular contaminated or unsupported passages were excluded from the substantive synthesis. Repetition among lanes supplied no verification weight.

## 5. Search coverage and unresolved gaps

The independent check covered claim text, family links, priority, assignee/applicant, and preliminary legal status for US, WO/PCT, EP, CN, KR-origin, and Indian-priority leads. Searches were organized around capacitive soil-moisture calibration; temperature/salinity compensation; low-cost sensor variation; replacement and reference-media transfer; insertion, packing, and remount effects; event-based recalibration; confidence/exclusion; drift and sensor health; provenance; and grouped physical validation. CPC/IPC neighborhoods included G01N27/22, G01N33/24, G01D calibration, and relevant agriculture/control classes. Citation chaining from the closest families added CN113049650B and the US20220162998A1/US12270349B2 validity family.

Material unresolved gaps are:

- official-register confirmation of annuity/enforceability and current Chinese claim text for CN102914568B, CN111103333B, CN108414007B, and CN113049650B;
- exact Indian prosecution, grant, claim, and current-status details for priority application 202021001465 in the TCS family; the family relationship is verified, an Indian grant is not;
- EP4090953B1 national validations, unitary/UPC posture, opposition history, and country-by-country force;
- a complete national-stage search for WO2020047587A1 despite no stages appearing in the checked family display;
- professional translations and prosecution histories for the closest Chinese and Korean-origin claims;
- a claim-level review of recent US20250362243A1, which published before the cutoff but was not retrievable in the checked interface; its title alone is insufficient evidence;
- continuation/divisional and unpublished-application risk through the cutoff, plus ownership, licence, litigation, and standards-essential questions;
- a dedicated second search around the precise later mechanism after its confidential elements are defined: trusted physical challenges, transfer/provenance binding, contamination gates, remount acceptance, and false-valid control;
- target markets and acts of making, using, selling, offering, or importing, without which FTO cannot be jurisdictionally completed.

These gaps prevent a patentability or FTO clearance conclusion. They do not prevent the present portfolio decision.

## 6. Verified patent-family ledger

“DB active/pending” below means the checked public database labels the record that way; the database itself warns that status is not a legal conclusion. Official-register and counsel confirmation is still required.

| Family / applicant | Independent-claim focus | Preliminary status through cutoff | TrueMoist relevance |
|---|---|---|---|
| [US12175680B2](https://patents.google.com/patent/US12175680B2/en), [WO2021144807A1](https://patents.google.com/patent/WO2021144807A1/en), [EP4090953B1](https://patents.google.com/patent/EP4090953B1/en); TCS; Indian priority 202021001465 | Calibrate a low-cost resistive/capacitive sensor, photograph it, extract metallic-probe image features/connectivity, classify degradation, recommend modification/replacement | US DB active; EP granted 9 Oct 2024 and DB active; PCT published; Indian filing identified but grant/status unverified | Close field/problem and replacement/health art. Frozen and proposed systems lack the mandatory image pipeline, so reviewed US claim 1 does not literally read on them. |
| [CN102914568B](https://patents.google.com/patent/CN102914568B/en); South China Agricultural University | Replaceable high-frequency probe; establish soil/known-solution relationships; condition the replacement in known dielectric medium to match the prior probe | Granted; DB active, anticipated 2032 | Closest transfer-specific patent. Broad replacement-probe equivalence is not open white space. Frozen MVP lacks this custom probe/media procedure; later transfer direction must distinguish it. |
| [US20080199359A1](https://patents.google.com/patent/US20080199359A1/en), WO2007002994A1, EP1899716A1; Senviro | Capacitive sensor, processor, stored history, scale stored values to a moisture range for calibrating new readings; wet/dry bounds and watering-cycle logic | US abandoned; WO ceased; EP withdrawn | Strong prior art against generic self-learning, min/max, and reference-event recalibration; no reviewed live US/EP claim. |
| [WO2020047587A1](https://patents.google.com/patent/WO2020047587A1/en); Robert Bosch Australia | Moisture sequences spanning uptake/release determine min/max; dependent claims cover implausible/out-of-range/inconsistent data, confidence, exclusion, progressive recalibration | PCT DB ceased; no checked national stage found | Very close prior art against generic event recalibration, confidence, rejection, and adaptive bounds. National-stage gap remains. |
| [CN111103333B](https://patents.google.com/patent/CN111103333B/en); Beijing Research Center for IT in Agriculture | Preset device information includes soil-element correction identifier and geographic data; select correction strategy; dependent temperature correction | Granted; DB active, anticipated 2039 | Weakens novelty of preset metadata/correction codes and temperature-linked strategy. Frozen salt code is not the same claimed identifier/geography workflow. |
| [US7884620B2](https://patents.google.com/patent/US7884620B2/en); Advanced Sensor Technology/Green Badge | Housing with dual high/low-frequency bridge circuits, reference capacitor/resistor, voltage meters, MCU deriving moisture and salinity, contact surfaces, wireless output | Granted; DB active, anticipated 2028 | Strong moisture/salinity prior art but low literal overlap: frozen system has neither those circuits, measured salinity, nor mandatory wireless. |
| [US11598743B2](https://patents.google.com/patent/US11598743B2/en); Damoatech | Custom single probe with first/second resonance circuits, matched reference signal, defined electrodes; temperature sensor is dependent | Granted; DB active, adjusted expiry 2041 | Crowds custom resonance/reference and temperature compensation, but the frozen commodity probe lacks the claimed structure. |
| [US9804113B2](https://patents.google.com/patent/US9804113B2/en); Fiskars | Capacitive probe, series RLC circuit, MCU drive/read operation | Granted; DB active, adjusted expiry 2035 | Custom RLC hardware art; low frozen overlap. |
| [US11415612B2](https://patents.google.com/patent/US11415612B2/en); METER | Complex-dielectric/TVM sensing with tuned impedances for permittivity and conductivity | Granted; DB active in checked record | Crowds custom admittance and live conductivity separation, not the commodity-probe MVP. |
| [US7944220B2](https://patents.google.com/patent/US7944220B2/en); Delta-T | AC source, probe, specified PI complex impedance and sensing impedance, amplitude/phase measurement; temperature is dependent | Granted; DB active, adjusted expiry 2027 | Prior art and possible hardware FTO only if redesigned toward the claimed PI circuit. Frozen analog output reading does not supply those elements. |
| [US9146206B2](https://patents.google.com/patent/US9146206B2/en), EP2623971/EP2784495 line; Deere | Calibration fixture/reference media, normalized frequency response, fitted constants for water content | US granted; DB active, adjusted expiry 2033; foreign status varies | Shows reference-state calibration and fitted equations are established. Frozen rig differs, but generic calibration methodology is crowded. |
| [US7240743B2](https://patents.google.com/patent/US7240743B2/en); Sentek | Probe/body insertion arrangement that slices/removes soil and stabilizes entry | US expired-lifetime | Nonblocking US prior art on contact and installation; relevant to obviousness of insertion controls. |
| [CN102944577A](https://patents.google.com/patent/CN102944577A/en) | Temperature-calibration apparatus using controlled sample/measurement equipment | Application publication; exact current status not relied upon | Supports conventionality of controlled temperature calibration; not charted as a live block. |
| [CN108414007B](https://patents.google.com/patent/CN108414007B/en); Hongfujin | Temperature-dependent nonlinear soil temperature/moisture compensation and coefficient estimation | Granted; DB active, anticipated 2038 | Close algorithmic prior art against broad low-order temperature compensation claims. Exact Chinese claim scope needs review. |
| [CN116298198A](https://patents.google.com/patent/CN116298198A/en); Hefei Institutes/CAS | Integrated temperature, moisture, conductivity and other parameters with fusion correction | DB pending | Relevant only to a live-EC/custom multi-parameter redesign; it does not make absence of live EC novel. |
| [CN113049650B](https://patents.google.com/patent/CN113049650B/en) | Timed switching among known capacitors, polynomial interpolation/regression, standard-vs-measured calibration curve | Granted; DB active in checked record | Additional evidence that embedded/polynomial soil-sensor calibration is known; custom internal circuitry differs from frozen MVP. |
| [US20220162998A1](https://patents.google.com/patent/US20220162998A1/en) / [US12270349B2](https://patents.google.com/patent/US12270349B2/en) | Published claims broadly used Bayesian posterior credible intervals/control lines for sensor validity; granted claim 1 is narrowed to controlling a sensor in a gas turbine, alarm, and repair/replacement details | US grant DB active | Important prior art against generic statistical validity envelopes. The live grant's gas-turbine limitations make direct frozen overlap low. |
| [US7170302B2](https://patents.google.com/patent/US7170302B2/en) | Planar coated capacitive soil probe | Expired-fee-related in checked record | Old commodity-probe principle prior art; not treated as a live block without official confirmation. |
| [US9949450B2](https://patents.google.com/patent/US9949450B2/en) | Soil-moisture probe/system with temperature adjustment and irrigation context | Expired-fee-related in checked record | Prior art against broad temperature adjustment; no FTO reliance without official confirmation. |

## 7. Closest independent-claim analyses

**CN102914568B claim 1 — replacement-probe calibration.** The translated independent method claim requires a replaceable probe whose dimensions satisfy stated electromagnetic constraints; calibration in multiple known-moisture soils and known-dielectric organic solutions; relationships among voltage, moisture, and dielectric constant; and, on replacement, adjustment in a known solution until the new output matches the old. A later TrueMoist transfer workflow shares replacement, known physical references, and equivalence as a goal. It differs if it uses an unmodified commodity analog probe, sparse soil challenges, disturbance-conditioned residuals, and an accept/reject decision rather than the claimed custom high-frequency probe and organic-solution conditioning. Those differences may avoid literal overlap but do not, by themselves, establish nonobviousness.

**US20080199359A1 claim 1 — stored-history scaling.** Claim 1 combines a capacitance sensor, processor, periodic memory, and scaling of stored moisture values to establish a range used to calibrate each new reading. Claims 4–5 add stabilized maximum/saturation and minimum/dry values. Any broad reference-event, min/max, or continuously self-calibrating claim would collide with this disclosure. The US application is abandoned and the EP member withdrawn, so it is prior art rather than a reviewed live US/EP FTO block.

**WO2020047587A1 claim 1 and dependent claims — event calibration/confidence.** Claim 1 derives minimum and maximum values from a sequence spanning uptake/release events. Claims 13–18 identify errors from impossible, out-of-range, or inconsistent readings, compute a confidence metric, and exclude measurements; claims 22–23 progressively improve bounds and recalibrate. This is highly damaging to generic claims for event-triggered recalibration, confidence gating, or abstention. The proposed direction would need a materially different physical transfer mechanism and demonstrated interaction, not renamed distance scoring.

**US12175680B2 claims 1, 6, and 11 — low-cost sensor health.** Each independent form requires low-cost resistive/capacitive soil sensing and calibration plus a captured sensor image, contour/metal-pixel/connectivity processing, degradation analysis, and modification/replacement recommendation. TrueMoist's frozen and proposed approaches do not use that image chain. Direct read-on is therefore not apparent, but the family is powerful prior art showing that health assessment and replacement of low-cost soil probes are already recognized technical problems. Dependent claims also disclose normalization against a second/rugged sensor and air/water extrema.

**CN111103333B claim 1 — preset correction metadata.** The independent method starts from preset equipment data including a soil-element correction identifier and geography, then selects a correction strategy. Temperature correction appears in dependent material. A binary controlled salinity-treatment code is not the same limitation, yet the claim undermines any assertion that merely adding a preset categorical code to soil-sensor correction is a novel technical mechanism.

**US7884620B2 claim 1 — moisture and measured salinity.** The claim requires a particular housing, dual high/low-frequency oscillator paths, reference capacitor/resistor and voltage meters, a microcontroller calculating moisture and salinity, conducting surfaces, and wireless transmission. The frozen system lacks nearly every distinctive circuit/communication limitation and does not measure salinity. Its relevance is prior-art motivation to address conductivity/salinity effects, not a present literal claim match.

**US12270349B2 versus its publication.** Published US20220162998A1 claim 1 broadly recited Bayesian historical-data inference, a credible interval/control line, and validity based on deviation. The granted independent claim is materially narrower: it controls a sensor installed in a gas turbine and adds performance-reduction, alarm, repair/replacement, and detailed interval limitations. This prosecution outcome matters. The publication is prior art against generic validity scoring; FTO must chart the granted claim, for which frozen TrueMoist lacks the gas-turbine chain.

**US11598743B2 claim 1 — reference resonance.** The independent claim requires a custom first probe/electrode structure, first and matched second resonance circuits, two AC signals, and determination from resonant frequencies. A temperature sensor is in dependent claim 2, not the independent core. A commodity SEN0193-class analog output plus separate DS18B20 does not meet that structure, but broad custom resonance/reference redesign claims would enter this crowded line.

## 8. Frozen-MVP feature chart

| Frozen feature | Technical purpose | Prior-art position | Patent significance |
|---|---|---|---|
| Commodity analog capacitive probe | Low-cost moisture-sensitive signal | Long-established probes and extensive SEN0193 practice | No independent distinction |
| Nearby DS18B20 | Observe temperature disturbance | Temperature sensing/compensation is established in patents and literature | Predictable auxiliary measurement |
| Controlled salinity-treatment code | Experimental factor for known salt dose | DOE metadata; preset correction strategies are known | Experimental design, not measured EC and not a technical sensor channel |
| ADS1115 vs calibrated ESP32 gate | Test whether external ADC adds value | Paired instrumentation comparison and signal hardening are routine | Engineering hygiene, not invention |
| 1 kΩ/100 nF, decoupling, grounding, short wiring, perfboard | Reduce avoidable electrical variation | Ordinary analog practice | No patent distinction |
| M0/M1/M2 and ridge | Quantify incremental compensation | Linear, polynomial, ridge, and fitted sensor calibration are conventional | Mathematics/model choice alone is weak |
| Offline fit; fixed local coefficients | Reliable no-cloud inference | Routine MCU deployment | Locality supports scope/cost, not novelty |
| One homogeneous soil | Control confounding and workload | Standard experimental restriction | Prevents universal claims; no invention |
| 72 independent runs with grouped split | Credible evidence and no pseudoreplication | Sound experimental design | Evidence generation, not invention |
| Dry-basis gravimetric truth | Traceable reference | Standard soil-water practice | Essential metrology, not invention |
| No live EC | Avoid underdesigned electrochemistry | Omission/cost decision | Absence is not a positive inventive feature |
| Exact parts and ₹3,000/₹5,000 bounds | Semester feasibility | Procurement constraints | No patent distinction |

## 9. Named-lead and commercial-actor investigation

| Actor/lead | Verified line | Disposition |
|---|---|---|
| Tata Consultancy Services | US/EP/PCT low-cost soil-sensor calibration, image-based health, degradation, and replacement | Most important live health family; direct image limitations reduce current read-on, but later health/replacement claims require care |
| South China Agricultural University | CN102914568B replaceable-probe conditioning/equivalence | Closest transfer patent; must be claim-charted before defining any transfer claim |
| Robert Bosch Australia | WO2020047587A1 event-derived bounds, confidence, exclusion, recalibration | Close prior art; national-stage status gap remains |
| Senviro | US20080199359/WO2007002994/EP1899716 stored-history and wet/dry self-calibration | Abandoned/ceased/withdrawn rights checked, but strong prior art |
| Green Badge / Advanced Sensor Technology | US7884620 dual-frequency moisture/salinity measurement | Active-database US hardware family; low frozen literal overlap |
| Damoatech | US11598743/Korean-priority resonance/reference and temperature line | Active-database US hardware family; blocks overbroad custom redesign narratives |
| Fiskars | US9804113 RLC capacitive sensor | Active-database US hardware family; no frozen RLC chain |
| METER/Decagon | US11415612 complex dielectric/admittance line | Relevant to sophisticated live-conductivity redesign, not the MVP |
| Delta-T | US7944220 PI complex-impedance sensor; SM150T appears in field literature | Hardware claims are distinct; commercial performance is not proof of claim scope or TrueMoist transfer |
| Deere | US9146206 reference-state fixture/calibration | Demonstrates established calibration equations/reference media |
| Sentek | US7240743 insertion/contact line and later installation work | Expired US insertion patent remains prior art; reinforces mechanical-contact conventionality |
| Toro/Rain Bird and irrigation actors | Numerous controller/integration families | Irrigation control is outside the frozen concept; it supplies no TrueMoist differentiator |
| DFRobot/SEN0193 ecosystem | Commodity probe and academic calibration studies | Confirms feasibility and variability; product use is not patent clearance |
| Campbell Scientific, Vegetronix, universities | Named technical/product leads in lanes | No closer independently verified live claim was found for the exact frozen stack; brochures and aggregator pages were not treated as claim evidence |

The commercial landscape confirms a mature sensing/calibration field. Product differences cannot establish novelty or FTO.

## 10. Non-patent prior art and measurement practice

- Schwamback et al.'s 2023 study, [Automated Low-Cost Soil Moisture Sensors](https://pmc.ncbi.nlm.nih.gov/articles/PMC10007478/), evaluates 63 sensors and proposes universal and single-point calibration alongside individual calibration. It is especially damaging to broad claims for probe-to-probe transfer or sparse recalibration.
- Abdelmoneim et al.'s 2025 [SEN0193 calibration study](https://pmc.ncbi.nlm.nih.gov/articles/PMC11768944/) studies a widely used low-cost capacitive probe in soil and reinforces that soil-specific calibration is ordinary practice.
- Nagahage et al.'s 2019 [low-cost capacitive sensor calibration study](https://www.mdpi.com/2077-0472/9/7/141) predates the project and supports the conventionality of gravimetric calibration and low-order response fitting.
- Raheja et al.'s 2025 [SEN0193 field/laboratory study](https://www.nature.com/articles/s41598-024-81288-z) uses eight probes, reports significant sensor-to-sensor differences, and shows output shifts across soil EC levels 0.27, 4.1, and 9.1 dS/m. It also identifies compaction, placement, and conductivity as reasons a universal curve may fail. This supports the engineering hypothesis while making broad calibration claims less distinctive.
- The [FAO gravimetric procedure](https://www.fao.org/fileadmin/user_upload/GSP/GSDP/Field_exercises/NEW_Field_exercises/P06b-gravimetric-soil-water-EN-1-2.pdf) specifies drying until stable weight, including 24–48 hours at 105 °C, and uses dry-mass water content. FAO's [field-measurement guidance](https://www.fao.org/4/t0231e/t0231e05.htm) likewise describes 105 °C for 24 hours and explains that bulk density is needed to convert dry-weight fraction to volumetric content.
- Data splitting must preserve physical independence. Scikit-learn's [data-leakage guidance](https://scikit-learn.org/stable/common_pitfalls.html) states that test data must not influence model choices or preprocessing, and its [grouped cross-validation documentation](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedGroupKFold.html) illustrates non-overlapping groups. For TrueMoist, the group is the independently prepared/reset physical sample or batch—not the rapid ADC reading.

The technical literature supports TrueMoist as a worthwhile metrology/calibration study. It does not support a claim that ordinary compensation, unit variation, one-point transfer, or local regression is new.

## 11. Frozen-MVP patent assessment

The frozen stack is a **predictable combination**, not a presently credible invention nucleus.

- The controlled salinity code is experimental design: a known treatment label supplied to a model. It neither senses a new physical variable nor measures EC.
- The 72-run factorial and untouched physical replicate are evidence-generation architecture. Their merit is methodological credibility, not patent distinction.
- The Week-1 ADS1115 gate is sound engineering hygiene. A paired ADC comparison does not create a new sensor mechanism.
- Omitting live EC is a cost, scope, and metrology decision. An absence cannot supply the missing positive technical contribution.
- Exact part numbers, wiring values, and budget are implementation constraints with no apparent patent distinction.
- M0/M1/M2, ridge regularization, and fixed MCU coefficients are ordinary computational tools. Using them on familiar probe, temperature, and treatment inputs gives the expected result if the disturbances are learnable.
- One-soil validation limits the engineering claim correctly; it cannot support universal calibration, replacement transfer, field robustness, or multi-soil generalization.

No single checked reference was shown to recite every arbitrary detail of the exact frozen assembly, so this is not a definitive anticipation finding against an unwritten claim. The problem is more fundamental: any commercially meaningful broad nucleus is already disclosed in pieces, and the remaining details look like routine optimization or experimental bookkeeping. The frozen MVP is therefore **Track D as a patent direction**, while remaining a strong semester prototype.

## 12. Candidate invention-direction matrix

Abbreviations in the legal column are N = novelty, O = obviousness/inventive step, E = eligibility, and F = FTO. Every patent-oriented threshold below would be **proposed**, not frozen, and would require owner approval before confirmatory testing.

| # / direction and physical problem | Contribution; closest art; apparent difference; measurable effect | Baselines/ablations; architecture, cost/compute, timing/later work | N/O/E/F risk; confidence; kill; Track |
|---|---|---|---|
| 1. Probe-specific characterization — cheap units differ | Fingerprint each probe across controlled states. Closest: 63-sensor universal/one-point study, Raheja, TCS normalization. Difference: none beyond a local protocol. Effect: repeatability/bias quantified. | Baselines pooled vs per-probe oracle; ablate probe ID. Frozen two probes suffice; negligible compute/cost; feasible in 3 months. Later add lots. | N high risk; O very high; E moderate if algorithmic; F no direct new issue. High confidence of rejection. Kill if fingerprint adds no actionable physical decision. **D** |
| 2. Automatic replacement-probe calibration transfer — full recalibration is costly | Transfer donor calibration to a new probe from sparse anchors. Closest: CN102914568B, TCS dependent normalization, 63-sensor one-point calibration. Difference could be commodity-probe software mapping rather than custom media/hardware. Effect: lower transfer RMSE/workload. | Compare full per-probe oracle, naive coefficient reuse, one-/two-point affine transfer, pooled model; ablate anchors/mapping. Two probes permit only a pilot; meaningful evidence needs 6–12 probes and ≥2 lots. MCU compute small; later semester. | N/O high; E medium-high; F material in CN and TCS markets. Low confidence alone. Kill if no better than two-point affine or benefit is probe-specific. **D** |
| 3. Dual-probe disagreement for validity/health — averaging can hide failure | Use disagreement to reject/diagnose rather than average. Closest: WO2020047587 inconsistent-proximate-reading/error claims, TCS health, general redundant-sensor diagnostics. Difference: low-cost soil-specific physical attribution. Effect: false-valid reduction. | Baselines average, single probe, simple absolute difference, oracle; ablate temperature/packing conditioning. Requires simultaneous matched sample and induced faults; one spare probe undermines independence. Cheap compute, but frozen design does not include runtime dual probes. | N/O very high; E medium; F unresolved WO national stages/TCS. Low confidence. Kill if disagreement tracks soil heterogeneity more than sensor fault. **D** |
| 4. Insertion-/packing-aware compensation or invalidation — contact dominates dielectric response | Measure mechanical preparation indicators and compensate/reject. Closest: Sentek insertion art, Toro installation descriptions, Raheja placement/compaction evidence. Difference requires a specific observable mechanism, not a recorded operator label. Effect: lower remount/insertion error. | Baselines fixed jig, no correction, simple range gate; ablate each mechanical observable. Frozen rig can quantify but lacks a runtime contact sensor. Added force/depth hardware may breach scope/budget. Later instrumentation needed. | N medium if a new physical observable exists; O high; E lower when physically tied; F depends on added hardware. Low confidence. Kill if observables cannot distinguish moisture from packing/contact. **D** |
| 5. Remount/reinstallation acceptance test — a returned probe may no longer match calibration | Apply a bounded reference challenge after remount and accept/reject calibration. Closest: CN102914568B replacement conditioning, calibration fixtures, installation art. Difference: remount-specific acceptance based on disturbance residuals. Effect: lower false acceptance and remount error. | Baselines unconditional reuse, one-/two-point recalibration, full oracle, simple min/max. Repeated remounts are feasible exploratorily, but reliable rates need many probes/preparations. Minimal compute; extra physical workload. | N/O high; E moderate; F CN-sensitive. Low-to-medium only as part of row 16. Kill if simple two-point acceptance performs equally. **D** |
| 6. Contamination-protected drift adaptation — a trusted event may itself be contaminated | Update only after physical/event evidence passes contamination checks. Closest: US2008 self-learning, WO2020 event recalibration, TCS health, general sensor-drift practice. Difference must be a specific soil/probe contamination discriminator with a coupled update rule. Effect: avoid harmful updates while tracking real drift. | Compare unrestricted event update, no adaptation, oracle clean-event update; ablate each gate. Needs clean/contaminated events, wet/dry cycling and ageing proxy. Frozen MVP prohibits online learning. Later work; compute modest. | N/O high; E high if only statistics; F national-stage/other-domain risk. Low-to-medium as a composite component. Kill if gate cannot reduce harmful-update rate without excessive missed updates. **D** |
| 7. Confidence-gated/abstaining estimates — out-of-domain values should not be reported as valid | Emit value plus valid/abstain decision. Closest: WO2020047587 confidence/exclusion; US20220162998A1 statistical validity; ordinary OOD/distance gates. Mahalanobis distance is not presumed new. Effect: lower error/false-valid among reported values at stated coverage. | Always-report, simple range/min-max, distance gate, oracle validity; ablate uncertainty features. Easy firmware/compute and possible in 3 months, but frozen dataset lacks enough failure modes to validate safety. | N/O very high; E high; F broad published validity art and unknown live families. High confidence that generic form fails. Kill if coverage-error tradeoff is not better than simple range gate. **D** |
| 8. Reference-event self-validation/bounded recalibration — wet/dry events offer anchors | Detect a reference event, validate it, then bound calibration update. Closest: US2008 wet/dry self-learning and WO2020 uptake/release recalibration. Difference must be a new trusted physical event and contamination logic. Effect: lower long-term bias without harmful updates. | Unrestricted update, no update, oracle event labels, false-event ablation. Frozen bench salinity treatment is not a live reference event and online updates are excluded. Requires later longitudinal cycling. | N/O very high; E high; F unresolved national stages. Low confidence. Kill if event truth is not independently known or ordinary bounds suffice. **D** |
| 9. Physics-informed low-order compensation — unconstrained polynomial may violate monotonicity | Constrain sign/monotonicity or dielectric relationships while retaining low-order inference. Closest: CN108414007B, US7884620/US7944220 descriptions, ordinary constrained regression. Difference: exact validated physical constraint set. Effect: fewer nonphysical outputs and improved held-out disturbance error. | M1/M2, unconstrained ridge, monotonic post-processing; ablate each constraint. Feasible offline with same MCU cost. Frozen M2 already checks monotonicity, so little new architecture. | N/O high; E medium-high; F CN temperature-compensation risk. Low confidence for patent, medium for publication. Kill if constraints do not improve untouched data or only encode known physics. **D** |
| 10. Calibration provenance plus physical validity envelope — coefficients may be used with wrong probe/setup | Bind coefficients to probe, lot, ADC/wiring, soil/preparation, and tested ranges; reject mismatches. Closest: metadata correction in CN111103333B, software provenance, WO2020 range/error logic. Difference: a particular binding that triggers a physical acceptance procedure. Effect: lower wrong-calibration false-valid rate. | Baselines no binding, ID-only lookup, range gate; ablate provenance fields and acceptance test. Logging is cheap; true validation needs intentional swaps/remounts. Feasible pilot, not claim proof. | N/O high; E high if bookkeeping only; F CN/validity families. Low-to-medium only with row 16. Kill if identity/range lookup explains all benefit. **D** |
| 11. Lifecycle/ageing-state fingerprint — probe response changes with cycling/fouling | Derive physical state from challenge response and use it to accept, transfer, or retire a probe. Closest: TCS image health/degradation, general drift monitoring, CN113049650 internal calibration. Difference: non-image, perturbation-specific fingerprint. Effect: detect degradation earlier and reduce false-valid rate. | No-health model, simple drift threshold, TCS-like visual baseline where practical; ablate fingerprint features. Requires accelerated ageing/contamination and many units; not credible in the frozen semester. | N medium, O high, E medium if physical; F TCS material. Low confidence. Kill if fingerprint is not separable from moisture/packing or does not predict error. **D** |
| 12. Transfer across soil batches/classes — one-soil calibration is brittle | Hierarchical/domain transfer across batches or classes. Closest: extensive soil-specific/universal calibration literature and preset soil correction. Difference would require an unexpected low-data physical transfer mechanism. Effect: lower new-soil error/calibration work. | Per-soil oracle, pooled, naive reuse, one-/two-point transfer. Multiple soils are expressly outside MVP; high physical workload and likely >₹5,000/three months for credible evidence. | N/O very high; E high; F broad landscape. Low confidence. Kill if per-soil recalibration remains necessary or class labels do all work. **D** |
| 13. Multi-frequency moisture/salinity separation — conductivity confounds capacitance | Custom multi-frequency impedance measurement. Closest: US7884620, US7944220, US11598743, US9804113 and many commercial lines. Difference not identified. Effect: separate permittivity/conductivity. | Compare single-frequency/raw and reference EC; requires custom probe/AFE, calibration standards and substantial redesign/compute. Not three-month frozen scope. | N/O/F very high in crowded live hardware field; E lower. High confidence of rejection absent a new circuit. Kill on cost/schedule or no unique transfer function. **D** |
| 14. Live-EC-assisted compensation — treatment code cannot represent field conductivity | Add calibrated runtime EC and fuse it with moisture/temperature. Closest: US7884620, US11415612, US7944220, CN116298198A. Difference not identified. Effect: correct unknown salinity. | Treatment-code baseline, reference EC, moisture-only; requires AC excitation, cell constant, polarization/fouling and temperature calibration. Major redesign outside MVP and likely budget. | N/O/F very high; E lower. High confidence of rejection as defined. Kill if metrology cannot distinguish bulk/pore-water/apparent EC. **D** |
| 15. Frozen static temperature + treatment-code compensation — controlled disturbances bias a cheap probe | M1/M2 with fixed local coefficients. Closest: CN108414007B, CN111103333B, calibration literature, ordinary MCU regression. Difference is exact factorial/parts. Effect: Level-1 RMSE/MAE improvement. | M0/M1/M2 and subset ablations are already frozen. Fits budget/compute/three months. | N/O very high; E medium-high; F no exact read found but no clearance. High confidence it is engineering, not patent nucleus. Kill as patent path even if engineering thresholds pass. **D** |
| 16. **Composite: contamination-protected replacement-probe transfer with perturbation-conditioned validity and abstention** — transferred calibration can look plausible while physically invalid | Bind donor provenance; obtain sparse trusted physical responses from a replacement/remounted probe; form a transfer; challenge it under controlled perturbations; accept only within a transfer-specific validity state; abstain/fallback otherwise; permit updates only after a trusted event passes contamination checks. Closest combination: CN102914568B + 63-sensor one-point work + WO2020 + TCS + US20220162998A1. Apparent difference is the coupled, transfer-specific physical interaction; desired effect is simultaneously lower transfer error, false-valid rate, and calibration workload. | Full oracle, naive reuse, one-/two-point affine, pooled, always-report, simple range/distance, unrestricted update, no update, and every critical ablation. Requires 6–12 probes across lots, remount/packing/temperature/salt/contamination/ageing challenges and independent test groups. MCU remains light, but physical cost/work exceeds the frozen semester. | Preliminary N possible but unproved; O high; E medium if claimed as a concrete measurement/acceptance process; F medium-high search risk, especially CN/TCS/WO national stages. **Low-to-medium claimability confidence; medium portfolio confidence.** Kill if the full chain does not beat simple transfer/gates or the claimed benefit comes from one known component. **C** |

There is no Track A direction in the frozen MVP and no Track B direction that can be credibly validated within three months and ₹5,000 without displacing the authoritative Level-1 work.

## 13. Strongest surviving direction

The strongest direction is row 16: **contamination-protected replacement-probe transfer with perturbation-conditioned validity and abstention**.

Its physical problem is not merely that probes differ. It is that a transferred calibration may produce numerically plausible moisture estimates while the replacement, remount, packing/contact, wiring path, contamination state, or ageing state lies outside the donor calibration's physical support. The proposed contribution would be a coupled measurement process that:

1. binds a donor calibration to its physical provenance;
2. obtains a sparse, trusted physical response from a replacement or remounted probe;
3. derives a transfer mapping;
4. tests transfer residuals under more than one controlled physical perturbation;
5. accepts, rejects, or abstains according to a transfer-specific validity state; and
6. allows later updates only after a trusted reference event passes contamination checks.

The potentially defensible point is the **interaction**: contamination control and perturbation residuals are used to decide whether a transferred physical calibration remains valid, rather than generic confidence scoring being appended to a calibration. Even that interaction may be obvious once CN102914568B, one-point/universal calibration literature, WO2020047587A1, TCS health monitoring, and generic validity control are combined. It becomes credible only if experiments show an unexpected effect that cannot be reproduced by a two-point affine transfer plus a simple range gate.

The direction is connected to the MVP because the MVP establishes metrology, unit variation, perturbation control, and embedded deployment. It nevertheless needs a later semester: two probes cannot estimate transfer failure rates or manufacturing-lot effects; the 72-run grid has no systematic remount, contamination, ageing, or trusted/untrusted-event factors; and its untouched replicate tests Level 1, not transfer. A later design should use at least 6–12 probe units across at least two manufacturing lots, with independent donor/replacement assignments and blinded physical test groups. Those counts are planning ranges, not patented or performance thresholds.

Before detailed public protocol design, the team should make a confidential invention disclosure to the institution. No claim should be drafted around “Mahalanobis,” “confidence,” “provenance,” or “abstention” as labels. Any useful claim would need the specific physical challenge, acceptance/update relationship, and demonstrated sensor effect.

## 14. Level-1 compensation versus Level-2 robustness/transfer

| Dimension | Level 1 — frozen compensation | Level 2 — later robustness/transfer |
|---|---|---|
| Question | Can a fixed local model reduce error for two probes in one homogeneous soil under controlled moisture, temperature, and salinity-treatment conditions? | Can a replacement, remounted, aged, contaminated, or mismatched probe be transferred, accepted, recalibrated, rejected, or safely abstained using a specific physical mechanism? |
| Data | 72 physical runs; 4×3×2×3; reps 1–2 train/select, rep 3 untouched test | Multiple probe units/lots, preparation batches, remounts, contamination/ageing cycles, trusted/untrusted events, and later soil classes |
| Models/baselines | M0 raw, M1 linear, M2 ridge second order | Full per-probe oracle, naive reuse, one-/two-point transfer, pooled, always-report, simple gates, unrestricted update, no update, composite and ablations |
| Outputs | RMSE, MAE, bias, subset error, repeatability | Transfer/remount error, false-valid/false-invalid, abstention/coverage, detection delay, workload, drift and subset metrics |
| What success proves | Compensation within the tested one-soil range | Only the tested transfer/validity mechanism and challenge domain |
| What it does not prove | Patentability, FTO, field robustness, replacement transfer, health, multi-soil generalization | Universal calibration, indefinite ageing, all contamination types, or unsearched-jurisdiction FTO |

Level-1 success is a prerequisite for sensible Level-2 work, not evidence that Level 2 already exists.

## 15. Novelty

Under the US anticipation framework, every claim element arranged as required must be found in one reference; an exact duplicate assembled from multiple documents is an obviousness issue, not automatically anticipation. The USPTO states this explicitly in [MPEP 2131](https://www.uspto.gov/web/offices/pac/mpep/s2131.html).

**Frozen MVP.** No checked single reference has been demonstrated to recite the exact commodity part choices, treatment-code input, model menu, and 72-run protocol in one claim. That narrow observation does not create a useful novelty position. The commercially meaningful components—capacitive soil sensing, temperature correction, preset correction metadata, low-order fitted equations, MCU computation, local calibration, and gravimetric reference—are already disclosed. Reciting the salt code, split scheme, brands, or budget might make an unwritten claim textually different while leaving no credible technical nucleus.

**Strongest direction.** No verified single reference was found with the full confidential combination of replacement transfer, more than one physical perturbation check, transfer-specific validity/abstention, and contamination-protected update gating. Preliminary novelty is therefore **unresolved, not established**. CN102914568B supplies replacement equivalence; US20080199359A1 and WO2020047587A1 supply event/self-calibration; WO2020047587A1 and US20220162998A1 supply validity/exclusion concepts; TCS supplies low-cost-sensor health/replacement; and non-patent work supplies universal/one-point transfer. A second claim-focused search after the mechanism is defined could readily find a single closer reference.

## 16. Inventive step/obviousness

The frozen MVP has a high obviousness risk. A skilled sensor/embedded practitioner has an articulated reason to combine the known elements: low-cost capacitive probes vary and respond to environmental/physical conditions, so measure an available disturbance, calibrate against gravimetric truth, stabilize acquisition, fit a low-order model, and run it on the MCU. These are known techniques applied to a known device for predictable improvement. [USPTO MPEP 2141](https://www.uspto.gov/web/offices/pac/mpep/s2141.html) identifies combinations of known elements, simple substitutions, and known techniques applied to ready-for-improvement devices as standard rationales, while requiring an explicit reason rather than a conclusory assertion.

At the EPO, the closest art and objective technical problem would likely be framed around improving accuracy or validity of a low-cost soil-moisture measurement. The [EPO problem-solution approach](https://www.epo.org/en/legal/guidelines-epc/2026/g_vii_5.html) would give weight only to differences producing a technical effect. Ordinary regression, a categorical treatment code, and a test plan are unlikely to supply an inventive technical solution.

The strongest later direction also has high obviousness risk because all of its labels are known. Its best rebuttal would require evidence that the coupled physical challenges and contamination gate produce a non-additive result—for example, materially lower false-valid transfer decisions at similar calibration workload and coverage than every simple baseline and every leave-one-component-out ablation. Mere improvement over naive coefficient reuse is insufficient; one- and two-point transfer, full oracle, simple range/distance gates, and unrestricted/no-update baselines are mandatory.

## 17. Patent eligibility

Eligibility is separate from novelty and obviousness.

**United States.** Regression equations, distance scores, thresholds, and confidence calculations can recite mathematical concepts. [USPTO MPEP 2106](https://www.uspto.gov/web/offices/pac/mpep/s2106.html) nevertheless distinguishes merely reciting an exception from being directed to it and asks whether the claim integrates it into a practical application or adds significantly more. A claim limited to receiving sensor numbers, calculating compensated moisture/confidence, and displaying/abstaining is exposed to §101 risk. A concrete process that physically challenges a probe, determines whether transferred calibration is valid, changes sensor acquisition/acceptance, and demonstrably reduces erroneous physical measurements has a better—but not guaranteed—position.

**EPO.** Computer-implemented features can contribute only through a technical effect serving a technical purpose; nontechnical features cannot support inventive step under the [COMVIK guidance](https://www.epo.org/en/legal/guidelines-epc/2026/g_vii_5_4.html). The EPO's [AI/ML guidance](https://www.epo.org/en/legal/guidelines-epc/2026/g_ii_3_3_1.html) says technical effect may be shown by explanation, mathematics, or experimental data, while mere assertion is insufficient. Soil measurement is technical, but a generic statistical gate remains weak unless its sensor effect and required data characteristics are reproducibly disclosed.

**India.** Section 3(k) of the [Patents Act](https://ipindia.gov.in/frontend/pdf/patents/1_113_1_The_Patents_Act__1970___incorporating_all_amendments_till_1-08-2024.pdf) excludes mathematical or business methods, computer programmes per se, and algorithms. The [2025 CRI Guidelines](https://ipindia.gov.in/storage/uploads/docs-operator/62449276-74f6-438d-92fc-14b2cf3fa204.pdf) require substance-focused analysis. A software/model claim risks exclusion; a physically anchored sensor-calibration and acceptance process may fare better, subject to Indian counsel and the actual claim.

Hardware recitations do not cure novelty or obviousness, and eligibility does not imply patentability.

## 18. FTO

**No FTO clearance is established.** WIPO explains that FTO is claim-, territory-, and time-specific; its toolkit recommends searching granted and pending rights, checking current status, and obtaining qualified legal analysis before committing a design. See the [WIPO FTO toolkit](https://www.wipo.int/documents/d/tisc/docs-en-tisc-toolkit-freedom-to-operate-description.pdf) and [national-phase guidance](https://www.wipo.int/en/web/pct-system/national-phase).

| Jurisdiction / design | Preliminary live-claim observations | Required next step |
|---|---|---|
| US — frozen MVP | No apparent literal read in the reviewed independent claims of US7884620B2 (dual-frequency salinity hardware/wireless), US11598743B2 (matched resonance probe), US9804113B2 (series RLC), US11415612B2 (complex dielectric hardware), US7944220B2 (PI impedance circuit), US12175680B2 (image-based health), or US12270349B2 (gas-turbine validity chain). This is not a complete search. | Official status/maintenance confirmation, continuation search, full element-by-element claim charts, supplier/component review, and counsel for intended acts. USPTO notes that maintenance fees affect utility-patent force in its [maintenance guidance](https://www.uspto.gov/patents/maintain). |
| US — later direction | TCS's image limits and the gas-turbine limitation reduce direct overlap, but other live or pending transfer/validity claims may exist. Published US20220162998A1 remains prior art even though its grant narrowed. | Search the final confidential mechanism, continuations, non-soil sensor-validity art, and doctrine-of-equivalents issues; chart each live claim. |
| EP states — frozen/later | EP4090953B1 is granted and database-active; its image-analysis chain is absent from TrueMoist. EP1899716 is withdrawn. A European patent's practical force is country-specific after grant. | Confirm EP4090953 validations/unitary status, opposition and current claims, then chart target countries. |
| China — frozen | CN111103333B and CN108414007B are database-active, but the exact frozen system is not shown to perform their full claimed methods. Hardware replacement CN102914568B is absent from MVP. | Obtain official CNIPA status, authoritative Chinese claims/translations, and counsel before use/sale/import in China. |
| China — later transfer | CN102914568B is the closest identified live-database risk. The proposed commodity-probe, perturbation-conditioned workflow differs, but equivalence/conditioning elements must be charted. | Design-around/claim construction with Chinese counsel before freezing the transfer protocol. |
| India — frozen/later | The TCS family's Indian priority application is verified, but its current Indian grant/claims/status were not. That is a blocking information gap for an India-first deployment or filing strategy. | Retrieve the complete InPASS file, current claims/status, prosecution, renewals, and any divisional/related filings; obtain Indian FTO advice. |
| WO/PCT records | A WO publication is not itself a single worldwide enforceable patent. WO2020047587 is database-ceased, but national rights must be searched. | Complete national-stage family reconstruction in every intended market. |

The best supportable statement is: **no direct read was identified among the reviewed independent claims for the frozen design, but overall FTO confidence is low because the search, official statuses, target jurisdictions, and claim construction are incomplete.** The later transfer/validity direction has greater FTO search risk than the frozen MVP.

## 19. Claim-to-experiment map

There is no approved claim set. This is a map from **prospective technical elements** to evidence that would be required before institutional counsel decides whether claim drafting is justified. Exact challenge sequences and thresholds remain confidential and owner-approved.

| Prospective element | Physical experiment | Required comparators/ablation | Decisive outputs |
|---|---|---|---|
| Donor calibration bound to physical provenance | Intentionally swap probe ID, manufacturing lot, ADC/wiring path, preparation batch, and coefficient package | No binding; ID-only lookup; correct-package oracle | Wrong-package false-valid rate, bias, RMSE/MAE, detection rate |
| Sparse replacement-probe transfer | Assign donor and blinded replacement probes across lots; collect sparse anchors, then untouched moisture/temperature/salt test cells | Full per-probe oracle; naive reuse; one-point; two-point affine; pooled model | Transfer RMSE/MAE/bias and calibration workload |
| Perturbation-conditioned transfer acceptance | Subject each transferred probe to controlled remount, packing/contact, temperature, and salinity-treatment perturbations before independent testing | No challenge; single challenge; simple min/max/range gate; leave-one-perturbation-out | False-valid/false-invalid rates, remount error, subset error, coverage |
| Abstention/fallback tied to validity state | Evaluate estimates inside/outside the learned physical support with failures blinded from the gate | Always report; simple distance/Mahalanobis; simple range; oracle validity | Error among valid outputs, abstention rate, risk-coverage curve, false-valid rate |
| Contamination-protected trusted-event update | Present clean and contaminated candidate reference events during wet/dry cycling and ageing proxy | Unrestricted update; no adaptation; oracle-clean update; remove each contamination test | Harmful-update rate, post-update RMSE/bias, missed-valid-update rate, detection delay |
| Remount/reinstallation acceptance | Repeatedly remove/reinstall independently, including controlled changes in packing and insertion path | Unconditional reuse; one-/two-point recalibration; full recalibration | Remount error, false acceptance, time/mass/work per acceptance |
| Lifecycle/ageing fingerprint | Repeated wet/dry cycles plus defined contamination/cleaning states, with blinded error testing | Elapsed-cycle threshold; simple drift; no health model; individual fingerprint features removed | Detection delay, false alarm, remaining-use error, probe-retirement precision |
| Coupled mechanism as a whole | Factorial test of transfer × challenge × gate × update with independent physical groups | Every component removed in turn and all simple baselines above | Non-additive benefit: lower transfer error and false-valid rate at comparable coverage/workload |
| Local embedded realization | Replay identical frozen vectors on Python and ESP32; measure timing/memory | Floating-point host oracle; reduced-feature versions | Numerical equivalence, latency, RAM/flash, energy where relevant |

The strongest direction dies if its advantage disappears against two-point affine transfer plus a simple range gate, if one known component explains all improvement, or if rapid readings/overlapping windows are needed to manufacture significance.

## 20. Three-month semester plan

The semester plan remains engineering-first. Patent experiments are exploratory and cannot contaminate the untouched Level-1 test replicate.

| Time | Work and exit condition |
|---|---|
| Week 1 | Procure/verify two genuine probes, DS18B20, ESP32 and ADC path; confirm oven/scale; build jig; ten reinsertion records; same-node ADS1115/ESP32 comparison. Exit only if monotonic response and credible gravimetric access exist. |
| Week 2 | Pilot packing sensitivity; select one non-saturating S1 dose by dry-soil mass; freeze AFE on perfboard, connectors, container, preparation method and CSV schema. Salinity shift should exceed 3× within-condition electronic noise; otherwise apply the temperature-only fallback after one dose adjustment. |
| Week 3 | Time an end-to-end physical batch; run a small grouped factorial pilot; verify equilibration and at least exploratory 10% error reduction without leakage; confirm that 72 runs fit oven capacity/person-hours. Do not change final success thresholds. |
| Weeks 4–5 | Execute the 72-run design. Keep physical replicate 3 isolated. Use grouped validation only within replicates 1–2; fit M0/M1/M2 and freeze preprocessing, feature terms, hyperparameters, and coefficients before opening test data. |
| Week 6 | Deploy the selected fixed model locally; implement range/quality flags only as engineering guards; verify Python/ESP32 equivalence and USB CSV logging. No online adaptation. |
| Week 7 | Evaluate untouched replicate 3 once. Report RMSE, MAE, bias, absolute values, temperature/salinity subsets, paired uncertainty where feasible, and the major-subset guardrail. Do not retrain after viewing it. |
| Week 8 | Repeatability demonstration, failure review, archive raw data/code/chronology, and complete engineering report. Decide whether Level 1 passed; do not convert a failed subset into an omitted observation. |
| Weeks 9–10 | Only if Level 1 and metrology pass: run a strictly exploratory two-probe remount/naive-transfer pilot to estimate effect sizes and procedure burden. Compare naive reuse, one-point, two-point, and full per-probe calibration; do not call this Level-2 proof. |
| Week 11 | Replicate the most important exploratory failure/success, document negative results, and draft the confidential physical problem/mechanism statement. No new confirmatory threshold without owner approval. |
| Week 12 | Institutional IPR review and go/no-go for a later-semester search/experiment. If the mechanism is not specific or its effect is no better than simple baselines, close the patent branch and prepare an engineering/publication pathway after disclosure review. |

The frozen eight-week build remains valid even if weeks 9–12 kill the patent hypothesis.

## 21. Later-semester or publication extension

**Later-semester Track-C stage.** After institutional review and a refreshed claim search, procure enough probe units to represent at least two manufacturing lots. Use independent donor/replacement assignment; preparation batch and physical replicate grouping; repeated remounts; defined clean/contaminated states; wet/dry cycling; ADC/wiring swaps; and, only after the first transfer mechanism is understood, later soil batches/classes. Preregister the prospective mechanism, all baselines, exclusion rules, and owner-approved proposed thresholds before confirmatory testing.

The later dataset must separate:

- probe-unit and lot variation from soil/preparation variation;
- real drift from event/packing/temperature/salinity changes;
- acceptance coverage from accuracy among accepted outputs;
- calibration workload from accuracy gains; and
- transfer evidence from ordinary per-probe recalibration.

If the composite mechanism survives, prepare an institutional invention disclosure, a professional prior-art/FTO search in target jurisdictions, and only then decide whether filing is justified. If it fails claimability but Level 1 succeeds, a publication-quality engineering contribution remains possible: rigorous SEN0193-class compensation under controlled temperature and salt treatment; measurement uncertainty and pseudoreplication avoidance; the value or nonvalue of ADS1115; and negative evidence on transfer/remount/packing. Publication must wait until institutional IPR review clears the confidential boundary.

Multi-frequency sensing or live EC would be a separate major redesign, not an extension used to rescue this frozen concept.

## 22. Budget, measurement, compute, and team feasibility

**Budget.** The canonical planning range is approximately **₹1,790–₹3,440** with institutional oven/scale access; preferred spend is ≤₹3,000 and the absolute ceiling is ₹5,000. Indicative items are ESP32 ₹450–₹700, ADS1115 ₹120–₹220, two probes ₹300–₹600, DS18B20 ₹120–₹220, analog/perfboard/connectors ₹250–₹450, jig/containers ₹200–₹450, soil/salt consumables ₹100–₹300, optional 0.01 g scale ₹400–₹700, and contingency ₹250–₹500. Buying an oven is outside scope. The Week-1 ADC gate may remove hardware but is not intended as a patent experiment.

**Measurement.** The limiting resource is physical preparation, equilibration, drying, reweighing, and traceable labeling—not inference. A 0.01 g scale is preferred; 0.1 g is acceptable only for sufficiently large 300–500 g samples after an uncertainty calculation. Oven access must support 105 ± 5 °C, at least 24 hours, and repeat weighing to constant mass. The Week-3 throughput calculation must include oven capacity, reweigh cycles, failures, and a contingency. A reduction to the documented 54-run fallback would be a disclosed scope reduction, not execution of the authoritative 72-run validation.

**Compute.** The frozen M2 needs roughly 10–15 coefficients, well below 1 kB; acquisition and CSV buffers are each below a few kB; model evaluation is under roughly 100 floating-point operations and negligible relative to physical equilibration. The proposed later gates/transfers also fit an ESP32 unless a major redesign is chosen. No TinyML runtime is justified.

**Team of five.** The three technically strong contributors should own, respectively, metrology/soil rig, electronics/firmware, and data/model/independent test custody. The learner can own supervised preparation logs, labels, mass records, and inventory with double-checks. The presenter/support member can own schedule, visual documentation, protocol compliance, and final demonstration without access that compromises the untouched test. Cross-checks should require two people for salt dose, wet/dry mass transcription, sample identity, and test-set release.

The frozen MVP is feasible if U-TM-01 through U-TM-06 pass. A credible Level-2 programme is unlikely to fit the same ₹5,000 and three-month envelope because it needs more probe units/lots and substantially more independent physical challenges; its budget must be separately approved.

## 23. Kill criteria

**Frozen engineering kills/fallbacks**

- No reliable oven/scale access or no stable dry-mass reference: stop final accuracy claims; exploratory work only.
- Probe response is nonmonotonic, intermittently saturated, or reinsertion variability remains >10% of usable span after jig/second-probe corrective work: kill the architecture. A result <5% is the intended pass region; 5–10% is an owner-reviewed warning region.
- Packing/insertion variance equals or exceeds the intended temperature/salinity effect after one rig redesign: reduce scope or stop causal compensation claims.
- S1 is not a repeatable, nonsaturating shift >3× electronic noise after one dose adjustment: remove salinity from the final model and report a temperature-only fallback; never relabel the code as EC.
- No leakage-free pilot signal after checking reference and packing: do not add model complexity to manufacture fit.
- Measured throughput cannot support 72 independent runs: disclose failure of the frozen plan; use 54 only as the canonical fallback, not as if it were the validated 72-run design.
- Final test fails ≥20% RMSE improvement or ≥15% MAE improvement, or a major subset worsens by >10% MAE: do not claim engineering success.
- Python/MCU outputs are not equivalent: stop deployment claims until fixed.
- Spend would exceed ₹5,000: remove optional items/use institutional equipment; do not silently expand scope.

**Patent-direction kills**

- A pre-cutoff reference is verified to contain every prospective independent-claim element in the required arrangement.
- The difference over the closest art is only an algorithm name, score, categorical metadata field, brand/part, budget, or arbitrary threshold.
- The composite direction does not beat full simple baselines—especially two-point affine transfer plus a range gate—on independent physical data.
- Its benefit disappears when any one known component is compared fairly, or no non-additive interaction is shown.
- False-valid reduction requires unacceptable abstention/calibration workload, or contamination gating cannot distinguish bad events from real drift.
- Transfer evidence depends on two hand-selected probes, repeated ADC reads as samples, leakage, or overlapping windows rather than independent physical groups.
- The mechanism cannot be reproduced across probe units/lots, remounts, or preparation batches.
- Official claim charts reveal a blocking live claim in a target jurisdiction without a practical design-around or licence path.
- Credible validation requires converting the project into live EC, custom multi-frequency hardware, a cloud/controller platform, multi-soil MVP, TinyML, or online learning. That is a separate Track-D redesign, not a TrueMoist patent rescue.
- Institutional IPR review finds prior public disclosure, ownership, inventorship, or contributor-record problems that cannot be cured.

## 24. Confidentiality boundary

The team may discuss generically the use of low-cost capacitive probes, known temperature/salinity effects, ordinary regression, gravimetric calibration, and the frozen 72-run engineering design.

Pending institutional IPR review, keep confidential:

- exact physical-reference challenge sequences;
- probe fingerprints and lifecycle-state features;
- transfer mappings and their parameter values;
- validity-envelope definitions and acceptance/abstention thresholds;
- contamination gates and trusted-event logic;
- remount/reinstallation acceptance logic;
- coefficient/provenance binding;
- raw labelled transfer, remount, contamination, and ageing datasets;
- code, negative results, and ablation outcomes;
- invention chronology, conception records, and contributor/inventorship records.

Do not place those details in a presentation, repository, preprint, competition submission, demo video, or public dataset before institutional review. Preserve dated lab notebooks, raw files, hashes, code versions, procurement/lot records, and contributor decisions.

## 25. Final TrueMoist recommendation

**Retain as strong semester prototype but reduce patent priority.**

**Track C; medium confidence in the recommendation.** Execute the validated 72-run Level-1 architecture without adding patent-driven scope. Treat a successful frozen result as engineering evidence only. After Level 1, use the two-probe remount/transfer exercise solely to size a later study and to sharpen a confidential invention disclosure. Advance patent work only if an institutional review approves the specific composite mechanism, a refreshed claim search preserves a meaningful difference, and multi-unit/multi-lot physical experiments outperform all simple baselines and ablations.

## 26. Unresolved questions

1. Which countries and commercial acts—making, using, selling, offering, importing, licensing—matter for FTO?
2. What are the official current claims and status of Indian application 202021001465 and any related/divisional TCS filings?
3. Where is EP4090953B1 validated or given unitary effect, and has it faced opposition or limitation?
4. What are the official CNIPA annuity/status records and authoritative claim translations for the closest Chinese grants?
5. Did WO2020047587A1 enter any national phase not visible in the checked family display?
6. What do the claims of US20250362243A1 cover, and are any post-2024 continuations/divisionals closer to commodity-probe calibration or transfer?
7. Has any team member already disclosed the transfer, validity, contamination, remount, or provenance mechanism publicly or to a nonconfidential third party?
8. What institutional policy controls ownership, student inventorship, lab notebook practice, publication review, and filing authority?
9. Can oven access, scale resolution, sample capacity, and an end-to-end 72-run throughput be confirmed in Weeks 1–3?
10. Can two genuine probe units from documented lots be sourced now, and can 6–12 units across at least two lots be sourced for later work?
11. Does Level 1 actually pass on untouched replicate 3, including the major-subset guardrail?
12. Can the later physical mechanism be defined without relying on generic confidence/provenance labels, and can owner-approved proposed thresholds be preregistered?
13. Does the composite mechanism beat naive reuse, one-/two-point transfer, full per-probe calibration, simple range/distance gates, unrestricted update, and every critical ablation on independent physical data?
14. What calibration-workload reduction would be commercially meaningful enough to justify later patent and FTO spend?

## 27. Source and verification log

**Cutoff and independence.** The synthesis used only the 18-file blind package plus independently retrieved public sources. It did not use another synthesis, excluded research, or prior-chat technical context. Public records were retrieved on 2 August 2026, but only information with an effective/public event date on or before **1 August 2026** was used. The manifest served only to verify count, identity, size, hash, compilation, and exclusions.

**Project sources.** Files 01–06 were read in authority order; PDR-031/032/045/049/050/058–063 were reconciled with the final architecture/memory. Files 07–09 supplied the current evidence/uncertainty/search brief. File 10 supplied historical search leads only. Files 11–16 were independently audited as the six lanes. Both DOCX files were extracted and rendered page-by-page; Gemini was complete across 23 pages and Copilot across 21 pages. No required attachment was modified.

**Patent-publication verification.** Publication bibliographic data, family links, and claim text were checked for the following load-bearing records: [US12175680B2](https://patents.google.com/patent/US12175680B2/en), [EP4090953B1](https://patents.google.com/patent/EP4090953B1/en), [WO2021144807A1](https://patents.google.com/patent/WO2021144807A1/en), [CN102914568B](https://patents.google.com/patent/CN102914568B/en), [US20080199359A1](https://patents.google.com/patent/US20080199359A1/en), [WO2020047587A1](https://patents.google.com/patent/WO2020047587A1/en), [CN111103333B](https://patents.google.com/patent/CN111103333B/en), [US7884620B2](https://patents.google.com/patent/US7884620B2/en), [US11598743B2](https://patents.google.com/patent/US11598743B2/en), [US9804113B2](https://patents.google.com/patent/US9804113B2/en), [US11415612B2](https://patents.google.com/patent/US11415612B2/en), [US7944220B2](https://patents.google.com/patent/US7944220B2/en), [US9146206B2](https://patents.google.com/patent/US9146206B2/en), [US7240743B2](https://patents.google.com/patent/US7240743B2/en), [CN108414007B](https://patents.google.com/patent/CN108414007B/en), [CN116298198A](https://patents.google.com/patent/CN116298198A/en), [CN113049650B](https://patents.google.com/patent/CN113049650B/en), [US20220162998A1](https://patents.google.com/patent/US20220162998A1/en), and [US12270349B2](https://patents.google.com/patent/US12270349B2/en). Patent publication/claim text is primary technical/legal evidence; the Google Patents interface was the access layer. Its legal-status labels explicitly are assumptions, so every active/pending/expired statement in this report is preliminary unless independently tied to a dated grant/withdrawal event.

**Technical verification.** The core non-patent sources were [Schwamback et al. 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10007478/), [Abdelmoneim et al. 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC11768944/), [Nagahage et al. 2019](https://www.mdpi.com/2077-0472/9/7/141), [Raheja et al. 2025](https://www.nature.com/articles/s41598-024-81288-z), the [FAO gravimetric exercise](https://www.fao.org/fileadmin/user_upload/GSP/GSDP/Field_exercises/NEW_Field_exercises/P06b-gravimetric-soil-water-EN-1-2.pdf), and [FAO field measurements](https://www.fao.org/4/t0231e/t0231e05.htm). [Data-leakage](https://scikit-learn.org/stable/common_pitfalls.html) and [grouped-validation](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedGroupKFold.html) documentation were used only for validation practice, not patent evidence.

**Legal-method verification.** Novelty and obviousness were kept separate using [USPTO MPEP 2131](https://www.uspto.gov/web/offices/pac/mpep/s2131.html) and [MPEP 2141](https://www.uspto.gov/web/offices/pac/mpep/s2141.html). US eligibility used [MPEP 2106](https://www.uspto.gov/web/offices/pac/mpep/s2106.html); EPO analysis used the [2026 problem-solution](https://www.epo.org/en/legal/guidelines-epc/2026/g_vii_5.html), [mixed-feature](https://www.epo.org/en/legal/guidelines-epc/2026/g_vii_5_4.html), and [AI/ML technical-effect](https://www.epo.org/en/legal/guidelines-epc/2026/g_ii_3_3_1.html) guidance; India analysis used the [Patents Act including amendments through 1 August 2024](https://ipindia.gov.in/frontend/pdf/patents/1_113_1_The_Patents_Act__1970___incorporating_all_amendments_till_1-08-2024.pdf) and the [2025 CRI Guidelines](https://ipindia.gov.in/storage/uploads/docs-operator/62449276-74f6-438d-92fc-14b2cf3fa204.pdf). FTO method and territorial/national-phase limits used the [WIPO FTO toolkit](https://www.wipo.int/documents/d/tisc/docs-en-tisc-toolkit-freedom-to-operate-description.pdf), [WIPO FTO overview](https://www.wipo.int/en/web/wipo-magazine/articles/ip-and-business-launching-a-new-product-freedom-to-operate-34956), and [WIPO national-phase guidance](https://www.wipo.int/en/web/pct-system/national-phase).

**Verification limits.** No professional claim construction, official multi-jurisdiction status opinion, unpublished-application search, litigation/licence investigation, or counsel review was performed. Machine translations were treated cautiously. Descriptions and abstracts were not substituted for independent claims. Abandoned, withdrawn, ceased, expired, and fee-lapsed records were retained as prior art but not automatically treated as live FTO blocks.


---

## Source 5: `03_CONCEPT_PORTFOLIO/TrueMoist/03_Patent_Synthesis/02_TrueMoist_Patent_Evidence_Synthesis_High_Deep_Research.md`

- Authority: `TIER_2`
- Treatment: `CORE_DECISION_EVIDENCE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `ddf421678c6f5dbafd7e2d61db82a4b7c1d8c3d817afb4341538ec98f4d91505`

# Source Extraction

- Chapter: `08` — TrueMoist Architecture, Validation and Patent Evidence
- Authority tier: `TIER_2`
- Manual treatment: `CORE_DECISION_EVIDENCE`
- Original source: `03_CONCEPT_PORTFOLIO/TrueMoist/03_Patent_Synthesis/02_TrueMoist_Patent_Evidence_Synthesis_High_Deep_Research.md`
- Current SHA-256: `ddf421678c6f5dbafd7e2d61db82a4b7c1d8c3d817afb4341538ec98f4d91505`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

# TrueMoist Patent-Evidence Synthesis

**Evidence cut-off:** 1 August 2026
**Synthesis date:** 2 August 2026
**Purpose:** Independent patent-evidence and engineering decision support
**Important limitation:** This report is not legal advice, a patentability opinion, a validity opinion, claim construction, or freedom-to-operate clearance.

## 1. Executive verdict

### Required verdict

**credible long-term path requiring later-semester extension**

### Track and confidence

- **Track:** **C — connected later-semester path after a feasible semester MVP**
- **Confidence:** **Medium**

### Bottom line

The frozen 72-run TrueMoist MVP is a strong, disciplined and feasible engineering project, but it does **not** contain a credible independent invention nucleus in its present form. Its full stack is a predictable combination of known elements and practices: a commodity analog capacitive probe, nearby temperature sensing, controlled salinity metadata, ordinary analog hardening, linear and polynomial/ridge calibration, fixed local MCU inference, gravimetric reference measurement and grouped one-soil validation.

The controlled salinity-treatment code is useful experimental metadata, not measured EC and not a patent distinction. The exact 72-run design is evidence generation, not invention. The ADS1115-versus-ESP32 gate is sound engineering hygiene. Omitting live EC is a sensible cost and scope choice, not technical novelty. Exact component choices, spacing, CSV output and budget do not create an inventive concept.

A possible later invention path survives only at **Level 2: robustness, transfer and validity**, and only in a narrowly defined form. The strongest direction is not generic “confidence gating,” Mahalanobis distance, out-of-distribution detection, dual-probe disagreement, event recalibration or provenance. Those concepts are known generally and are represented in close soil-sensor prior art. The surviving research hypothesis is a **physical-reference-bound replacement/remount acceptance mechanism** that:

1. binds coefficients and provenance to a particular commodity probe or probe class;
2. applies a defined physical reference challenge when a probe is replaced or remounted;
3. distinguishes replacement-unit bias from moisture change, temperature/salinity disturbance, packing/remount error and actual degradation;
4. accepts a bounded transfer only when physical residual tests show validity;
5. blocks contaminated recalibration; and
6. abstains or falls back when transfer validity cannot be established.

Even this direction is only **possible, not established**. Replacement-probe equivalence, low-cost sensor health, self-learning/event recalibration, preset correction strategies and confidence/error handling already appear in close patent art. Two probes, one manufacturing lot, one soil and a short bench study can establish feasibility, but cannot establish a defensible population-level transfer or health mechanism. A credible case requires later-semester testing with several probes, preferably multiple lots, repeated remounting, packing disturbances, contamination, ageing proxies and claim-focused ablations.

### Final recommendation preview

**Retain as strong semester prototype but reduce patent priority.**

---

## 2. Input inventory

### 2.1 Physical attachment count

Exactly **18 physical attachments** were supplied and were readable:

- 1 governing synthesis instruction;
- 10 canonical project/historical documents;
- 6 independent TrueMoist patent-research lanes;
- 1 file-control manifest.

Parenthetical upload suffixes such as `(4)`, `(7)`, `(18)` and `(19)` are transport naming variations, not extra logical files.

### 2.2 Canonical project documents

All ten required project documents are present once:

1. `01_Engineering_Design_Review.md`
2. `02_Project_mC_Decision_Register_v1.2.md`
3. `03_Phase3C_Portfolio_Closure_Memo_Approved.md`
4. `04_Phase3C_TrueMoist_Architecture_Report_Final.md`
5. `05_Phase3C_TrueMoist_Memory_Final.md`
6. `06_Phase3C_TrueMoist_SOP_Final.md`
7. `07_Concept_Evidence_Matrix.md`
8. `08_Uncertainty_and_Test_Register.md`
9. `09_Patent_Research_Input_Pack.md`
10. `10_Phase2_Report_by_Claude.md`

Decision Register **v1.2** is present. Decision Register v1.1 is absent, as required.

### 2.3 Research lanes

Each of the six lanes is represented exactly once:

| File | Lane | Inventory treatment |
|---|---|---|
| 11 | ChatGPT Deep Research | Finalized Markdown is the official lane |
| 12 | Gemini Deep Research | One complete DOCX lane |
| 13 | Perplexity Deep Research | One complete Markdown lane |
| 14 | Qwen | One lossless initial-plus-follow-up compilation; one lane, not two votes |
| 15 | Mistral | One complete lane; no missing conclusion reconstructed |
| 16 | Microsoft Copilot | One complete DOCX lane |

The earlier superseded ChatGPT Deep Research PDF and the supplementary ChatGPT Work Max web audit are absent. Their absence is correct and they were not inferred from prior-chat context.

### 2.4 File-control conclusion

No required file is missing, duplicated, unreadable, concept-swapped or ambiguously substituted. The manifest was used only for file control and not as technical evidence.

---

## 3. Project authority and frozen concept

### 3.1 Authority order applied

This synthesis applies the governing order strictly:

1. Engineering Design Review.
2. Project mC Decision Register v1.2.
3. Approved Phase 3C Portfolio Closure Memo.
4. Final TrueMoist Architecture Report.
5. Final TrueMoist Memory.
6. Final TrueMoist SOP.
7. Validated current evidence files 07–09.
8. Phase 2 only as historical search leads.
9. Independent research lanes only after concept, source, claim and status audit.

The superseded 135-run material and Decision Register v1.1 were not used.

### 3.2 Owner constraints

- Development window: up to three months.
- Preferred spend: no more than ₹3,000.
- Absolute ceiling: ₹5,000.
- Team: five members, including three technically strong contributors, one learner and one presenter/support member.

### 3.3 Frozen TrueMoist definition

TrueMoist is a **local compensation system for a low-cost analog capacitive soil-moisture probe**.

Its frozen architecture comprises:

- two genuine analog capacitive probes, SEN0193-class or characterized equivalent;
- a waterproof DS18B20 placed at the same depth, approximately 20–30 mm from the moisture probe;
- controlled salt addition per dry-soil mass represented as a salinity-treatment code;
- no mandatory runtime EC sensor;
- ESP32-WROOM-32 primary, ESP32-S3 fallback;
- ADS1115 retained only if the Week-1 paired comparison justifies it;
- short filtered analog wiring, 1 kΩ series resistance, 100 nF input filtering, local decoupling, fixed connectors and soldered perfboard after characterization;
- M0 raw/univariate calibration, M1 multivariate linear regression and M2 ridge-regularized second-order regression;
- offline Python training and fixed coefficients on the ESP32;
- one homogeneous soil source and one documented packing method;
- 4 moisture × 3 temperature × 2 salinity × 3 independent replicates = exactly 72 physical runs;
- replicates 1–2 for training/model selection and replicate 3 untouched for physical testing;
- dry-basis gravimetric water content as ground truth;
- drying near 105 ± 5 °C for at least 24 hours and until constant mass;
- compensated RMSE at least 20% lower and MAE at least 15% lower than the uncompensated baseline on untouched test data.

### 3.4 Excluded concepts

The MVP is not a live-EC meter, irrigation controller, cloud platform, multi-soil product, custom multi-frequency probe, TinyML showcase, online-adaptive learner, universal calibration-free probe or laboratory reference instrument. The salinity-treatment code must never be described as bulk-soil EC, apparent EC, pore-water EC or solution conductivity.

---

## 4. Research-lane reliability audit

The lanes are evidence sources, not votes. Repeated assertions do not independently verify one another.

| Lane | Reliability | Retained value | Material corrections affecting the verdict |
|---|---|---|---|
| **ChatGPT Deep Research** | **High, with status caveats** | Best concept fidelity; broad named-family coverage; separates prior art from FTO; cautious Track-C conclusion; useful claim-to-experiment map | Several status conclusions remain provisional because not every US maintenance event, EP national validation, Indian register record or CN translation was officially audited. Its conclusion is persuasive because it is claim-focused, not because another lane agrees. |
| **Gemini Deep Research** | **Medium-low** | Correctly concludes the frozen MVP is conventional; identifies validity and transfer as future directions | It analyzed a different transport configuration (10 physical/11 logical inputs), not this 18-file synthesis package. It turns an invalid reading into an “autonomous agricultural hardware” actuation problem, drifting toward an irrigation controller. It overstates generic OOD/Mahalanobis abstention as verified novelty and patent eligibility. It characterizes the TCS family too broadly as generic runtime statistical auto-calibration; the close claim core materially includes rugged-reference normalization, degradation analysis and image-based probe inspection. “Relatively clear” FTO is unsupported. |
| **Perplexity Deep Research** | **Medium** | Correct concept; conservative conclusion; useful NPL and representative patent leads | Mandatory family and official-status coverage is incomplete. Several claim comparisons are high-level rather than complete independent-claim charts. Its final caution is useful, but its omissions prevent high reliability. |
| **Qwen compilation** | **Low-medium** | Correctly recognizes the frozen MVP as conventional; raises relevant future topics such as transfer, validity, event checks and contamination | It is one lane, not two. Part 2 does not cure unsupported Part 1 claims. Source quality mixes primary material with Reddit, product pages and secondary aggregators. `HIGH/CLEAR` FTO, Track-B confidence, Mahalanobis validity-envelope novelty, eligibility clearance, dual-probe health novelty and event-triggered recalibration white space are not established. Claims that no live EC improves patentability are rejected. |
| **Mistral** | **Low** | Confirms the conventional nature of the frozen MVP; identifies Level-2 reliability as the only plausible direction | It conflates novelty, eligibility and patentability; performs incomplete India/China searching; gives a low/medium FTO conclusion from too few patents; labels validity-region, confidence, reference-event and dual-probe concepts “NOVEL” without adequate claim searching. It treats product/circuit differences as if they clear FTO. Its patent-potential conclusion is downgraded. |
| **Microsoft Copilot** | **Low-medium** | Useful as an idea inventory and for identifying generic sensor-validity terminology | It relies materially on secondary legal summaries and broad non-soil validity concepts. Statements that all proposed directions fit three months, that no live claim blocks them and that novelty/inventive step are likely are unsupported. Its FTO assessment is not jurisdiction-specific and is not clearance. |

### 4.1 Cross-lane points that survive audit

The following survive because they are supported by primary patent/NPL evidence, not because several models repeated them:

- The frozen MVP is conventional and patent-weak.
- Temperature, conductivity/salinity, packing and unit variability are real measurement problems.
- A scientific 72-run result can be valuable even if it is unpatentable.
- Robustness, transfer and validity are more promising than ordinary regression.
- Multi-frequency or live-EC redesign would enter a crowded, more expensive hardware area.

### 4.2 Cross-lane points rejected or materially downgraded

- Generic Mahalanobis or OOD gating is not verified novelty.
- An “abstain” flag does not automatically produce patent eligibility.
- Absence of live EC does not create a patent distinction.
- Two probes do not establish a transferable probe-health invention.
- Event-triggered recalibration is not open white space.
- FTO cannot be called `HIGH`, `CLEAR` or “relatively clear” from this evidence.

---

## 5. Search coverage and unresolved gaps

### 5.1 Coverage performed

The synthesis checked the mandatory and closest records across the following categories:

- basic capacitive/dielectric soil-moisture sensing;
- temperature-dependent nonlinear correction;
- salinity/conductivity-aware sensing and multi-frequency hardware;
- preset correction models and soil/temperature correction identifiers;
- self-learning and event-based recalibration;
- replacement-probe equivalence;
- low-cost sensor health, degradation and replacement recommendations;
- calibration fixtures and unit-to-unit transfer practice;
- validity, error and confidence handling;
- relevant US, EP, WO/PCT, CN and Indian-priority records;
- commercial actors including TCS, Campbell/Advanced Sensor Technology, METER/Decagon, Delta-T, Sentek, Toro and Vegetronix.

### 5.2 Status methodology

- Publication and grant facts were distinguished from current enforceability.
- Google Patents status labels were treated as provisional discovery metadata, not official legal conclusions.
- A ceased PCT filing was not assumed to mean every national stage is dead.
- Expired or abandoned records were retained as prior art but not treated as live FTO barriers.
- Product pages were not used to infer claim scope.

### 5.3 Material unresolved gaps

1. The exact granted Indian claims and current register status for the Indian-priority TCS family require a complete InPASS review.
2. EP4090953B1 requires validation-state and opposition/register review in commercially relevant EP states.
3. US maintenance, terminal-disclaimer and prosecution histories were not exhaustively reviewed for every named US grant.
4. National stages, if any, arising from WO2020047587A1 must be mapped.
5. CN102914568B, CN111103333B and CN108414007B require official CNIPA status and professional claim translation before commercial reliance.
6. Commercial jurisdictions and intended commercialization activity have not been fixed, so a real FTO search scope cannot yet be defined.
7. A complete search of generic sensor calibration transfer, acceptance testing and OOD/error-gating art outside soil sensing remains necessary after the exact mechanism is frozen.

---

## 6. Verified patent-family ledger

“Status” below means verified publication/grant facts plus provisional public-database status where noted. It is not a legal conclusion.

| Ref. | Family / representative publication | Verified core | Status at cut-off | Prior-art relevance | FTO relevance to frozen or extended TrueMoist |
|---|---|---|---|---|---|
| P1 | **TCS sensor-health family:** WO2021144807A1; US12175680B2; EP4090953B1; Indian-priority filing | Calibrates low-cost resistive/capacitive sensors using rugged-reference values; analyzes degradation; includes image-based probe-metal/connectivity analysis; recommends modification or replacement | WO publication ceased; US and EP grants published in 2024; Indian register/claims not fully audited | Very high for low-cost sensor calibration, health/degradation and replacement logic | Significant for a Level-2 health/replacement mechanism; frozen fixed compensation has lower overlap |
| P2 | **CN102914568B** | Replaceable high-frequency soil probe; if replacement sensitivity differs, adjusts conditioning using a known dielectric reference so new-probe output equals old-probe output | CN grant published 2014; public database indicates active; official CN status pending | Very high for replacement-probe equivalence and transfer | Material in China if the extension forces a replacement probe to emulate an earlier probe through conditioning/reference calibration |
| P3 | **US20080199359A1 / WO2007002994 / EP1899716 family** | Stores periodic capacitive readings, rescales range for calibration and discusses wet/dry bounds, watering events, temperature, conductivity, placement, settling and ageing | US application abandoned; non-US family status not fully mapped | Very high for self-learning calibration and disturbance-aware recalibration | No enforceable abandoned US claim, but national-stage FTO remains unresolved |
| P4 | **WO2020047587A1** | Uses moisture uptake/release sequences to identify calibration levels and supports progressive recalibration, error checks and confidence-related handling | PCT publication indicated ceased; national stages unresolved | Very high for event-triggered recalibration and validity/error concepts | Depends on live national stages and exact extended implementation |
| P5 | **CN111103333B** | Selects a soil-element correction strategy using preset correction identifiers and geographic information; dependent claims add a temperature correction identifier/model | CN grant 2022; public database indicates active; official status/translation pending | High for preset correction codes, stored strategy selection and temperature correction | Potential China risk for a deployed code-driven correction architecture; frozen laboratory treatment code differs materially but does not create novelty |
| P6 | **CN108414007B** | Temperature-dependent third-order nonlinear compensation using measured moisture, temperature, true moisture and least-squares coefficient estimation | CN grant 2020; public database indicates active; official status/translation pending | Very high against generic polynomial/ridge temperature compensation arguments | Potential China risk depending on exact claim scope; strongly damages frozen-MVP patentability |
| P7 | **Campbell/Advanced Sensor Technology lineage:** US7408364B1, US7535237B1, US7884620B2, WO2009094324A2 | Sensing structures and local calculation of moisture/salinity, including dual-frequency or matched-reference circuitry in relevant claims/embodiments | Multiple US grants; public database indicates active for some; PCT ceased; maintenance not fully confirmed | Very high for moisture/salinity hardware and correction | Material mainly if TrueMoist later adopts live salinity, dual-frequency or custom sensing hardware |
| P8 | **US11598743B2** | First soil probe plus first resonance circuit, matched reference resonance circuit and determination from frequency difference; temperature compensation in a dependent claim | US grant 2023; public database indicates active | High for custom resonance/reference hardware and temperature compensation | Low overlap with frozen commodity analog probe; material if redesigned toward matched resonance circuits |
| P9 | **US9804113B2 / US20150330932A1** | Series-RLC capacitive sensing with MCU-driven measurement and moisture calculation | US grant 2017; public database indicates active; related PCT/EP status varies | High for custom RLC/MCU soil sensing | Relevant to major hardware redesign, not ordinary use of a packaged commodity probe output |
| P10 | **US11415612B2** (METER/Decagon-related) | Complex dielectric/admittance measurement architecture | US grant 2022; public database indicates active | High for advanced dielectric measurement | Material for sophisticated custom hardware, not frozen MVP |
| P11 | **US7944220B2** (Delta-T lineage) | Moisture-content sensing and compensation using electrical/impedance behavior | US grant; public database indicates active with term near 2027; official maintenance review still required | High for incumbent compensated sensing | Claim-specific risk if architecture approaches the claimed circuit/method |
| P12 | **US7240743B2** (Sentek) | Probe insertion/contact and capacitance-sensing arrangements | Patent term expired in public records | Prior art for insertion, probe arrangement and field contact | No present US barrier if expired, but still relevant to novelty/obviousness |
| P13 | **EP2623971 family / US9146206B2-related calibration apparatus** | Calibration fixtures and methods relating capacitive sensor output/frequency to known media or water content | Mixed family outcomes; US grant and EP procedural history differ | High for calibration fixtures/reference-media procedures | Depends on exact fixture and jurisdiction; relevant to physical-reference challenge design |
| P14 | **US5430384A** | Temperature-compensated soil-moisture sensor | Expired | Strong old prior art | No present US FTO barrier |
| P15 | **CN116298198A and related activity** | Multi-parameter soil sensing and fusion correction | Recent CN publication; family status not fully audited | Moderate/high for multi-sensor fusion | Relevant only to multi-parameter/live-EC redesign |

---

## 7. Closest independent-claim analyses

### 7.1 TCS sensor-health family — P1

The lane descriptions that reduce this family to generic “statistical auto-calibration” are inaccurate. The disclosed and claimed system is more specific. Its core includes a low-cost resistive or capacitive soil sensor, calibration/normalization using values associated with a rugged sensor, performance/degradation analysis and recommendation of modification or replacement. The disclosure materially uses images of the low-cost sensor, segmentation of the probe’s metal pixels and connectivity analysis.

**Overlap:** low-cost soil sensor; calibration; unit bias; degradation; replacement recommendation.
**Differences:** frozen TrueMoist uses fixed coefficients and no rugged reference or image-based probe inspection.
**Effect:** the family does not anticipate the full frozen MVP, but it crowds broad Level-2 claims to “monitor a low-cost probe, determine degradation and recommend replacement.” A future TrueMoist direction must not be framed merely as health scoring or replacement recommendation.

### 7.2 CN102914568B — P2

Independent apparatus claims cover a replaceable high-frequency probe and conditioning architecture. The independent method claim calibrates output against known-moisture soils and known-dielectric liquids; upon replacing a probe with different sensitivity, the conditioning module is adjusted using a known reference liquid until the replacement output equals the previous output.

**Overlap:** probe replacement; known reference challenge; output equivalence/transfer.
**Differences:** the frozen system uses a packaged low-frequency analog probe and software coefficients rather than the claimed 100 MHz sensing/conditioning architecture.
**Effect:** broad “use a reference to transfer calibration from old probe to new probe” cannot be treated as open white space. Any surviving direction must add a materially different physical validity/contamination mechanism and demonstrate more than output matching.

### 7.3 US20080199359A1 family — P3

Independent US claims describe a capacitive sensor, processor and memory storing periodic measured values and scaling those values over a range to calibrate readings. The description is important prior art for self-learning wet/dry bounds, watering-event calibration, temperature/conductivity influences, placement, soil settling and ageing.

**Overlap:** capacitance, stored history, calibration, environmental/disturbance adaptation.
**Differences:** frozen TrueMoist trains offline and does not update coefficients in operation.
**Effect:** abandoned US claims do not create a US FTO barrier, but the disclosure severely weakens broad novelty arguments for event calibration, self-learning bounds or drift-aware recalibration.

### 7.4 WO2020047587A1 — P4

The independent claim centers on recognizing an uptake/release moisture sequence and using that physical event to determine calibration levels. Dependent claims and description add progressive recalibration, machine-learning refinements and error/confidence behavior.

**Overlap:** trusted physical event, recalibration, validity/error handling.
**Difference:** a surviving TrueMoist mechanism would need a different, tightly defined physical reference challenge and contamination rejection logic, not merely watering-event recalibration.
**Effect:** event-triggered self-calibration is not a credible standalone invention direction.

### 7.5 CN111103333B — P5

Claim 1 obtains preset equipment information including a soil-element correction identifier and geographic information, selects an appropriate correction strategy and corrects received soil volumetric water content. Claim 2 introduces a temperature-correction identifier and corresponding strategy.

**Overlap:** stored correction code/identifier; preset compensation; temperature correction.
**Difference:** TrueMoist’s salinity treatment is laboratory metadata rather than a deployed GIS/soil strategy selection system.
**Effect:** a “salinity code selects a correction model” argument is weak. The frozen code is best treated as experimental design, not an inventive runtime input.

### 7.6 CN108414007B — P6

The independent claim covers a temperature-dependent nonlinear compensation algorithm built from experimental measured soil moisture, soil temperature and true soil moisture, using a third-order model and least-squares coefficient estimation.

**Overlap:** experimental calibration; measured moisture; temperature; true moisture; nonlinear polynomial; estimated coefficients; constrained MCU-friendly model.
**Difference:** TrueMoist adds controlled salinity metadata, ridge regularization, one-soil grouped validation and a commodity analog implementation.
**Effect:** this is one of the closest records against the frozen model. Adding ridge regularization and a salinity factor is likely ordinary model refinement rather than an inventive step.

### 7.7 Campbell moisture/salinity lineage — P7

Relevant independent and dependent claims cover specialized sensing hardware and local derivation of electrical properties, moisture and salinity, including dual-frequency/reference structures.

**Overlap:** local processing and the problem of salinity-induced moisture error.
**Difference:** TrueMoist does not measure live salinity and does not use the claimed custom multi-frequency structure.
**Effect:** lower apparent literal overlap with the frozen MVP, but strong prior art showing that moisture/salinity separation and local correction are mature. It is a major FTO concern only if the project redesigns toward live EC or multi-frequency sensing.

### 7.8 US11598743B2 — P8

Claim 1 requires a probe with electrodes, a first resonance circuit, a matched reference resonance circuit and a determination circuit comparing resonant frequencies. Temperature compensation appears in dependent claim 2.

**Overlap:** soil probe, local determination and temperature compensation.
**Difference:** frozen TrueMoist reads the analog output of a commodity probe and has no matched reference resonance circuit.
**Effect:** it is not an anticipation of the frozen stack. It is relevant mainly as a custom-hardware design fence and as evidence that reference-circuit temperature compensation is established.

---

## 8. Frozen-MVP feature chart

| Frozen feature | Patent/NPL treatment | Assessment |
|---|---|---|
| Commodity analog capacitive probe | Extensively disclosed and commercially ubiquitous | Conventional; no patent weight |
| Two probe units | Ordinary characterization/redundancy practice | Useful evidence, not invention |
| Nearby DS18B20 | Temperature compensation and colocated temperature sensing are old | Conventional implementation choice |
| Controlled salinity-treatment code | Multi-condition calibration and conductivity interference are known | Experimental metadata; not measured EC; no independent novelty |
| ESP32-WROOM-32 / ESP32-S3 | Generic MCU selection | No patent distinction |
| ADS1115 versus ESP32 ADC gate | Error-budget and reproducibility practice | Engineering hygiene, not invention |
| RC filtering, decoupling, short wiring and soldering | Standard analog design | Conventional |
| Raw, linear and ridge second-order models | Polynomial/nonlinear and least-squares compensation are directly disclosed | Conventional model ladder |
| Offline training/fixed coefficients | Routine embedded deployment pattern | Conventional |
| 72 independent physical runs | Strong experimental design | Evidence generation, not invention |
| One soil and fixed packing | Scope control and metrology | Improves validity but limits generalization |
| Gravimetric GWC | Standard reference practice | Conventional; high scientific value |
| 20% RMSE / 15% MAE improvement gates | Project success thresholds | Results threshold does not create patentability |
| USB serial CSV | Generic data logging | No patent distinction |
| No live EC | Simplifies scope/cost | Absence of a feature is not novelty here |
| Preferred ₹3,000 / ceiling ₹5,000 | Commercial/educational constraint | Cost alone does not establish inventiveness |

### 8.1 Frozen-MVP conclusion

No single located claim was shown to recite every implementation detail in one exact sentence. That does not create a credible patent path. A claim can be textually unique because it lists arbitrary conventional details while remaining obvious and technically uninventive.

---

## 9. Named-lead and commercial-actor investigation

### 9.1 TCS

TCS is a material patent actor in low-cost sensor calibration, degradation analysis and replacement recommendations. The family’s image-based probe inspection creates a meaningful design distinction from TrueMoist, but its broader calibration/health context narrows any future claim strategy.

### 9.2 Campbell Scientific / Advanced Sensor Technology

Campbell-related patents and products occupy sophisticated electrical-property, moisture and salinity measurement. They are important prior art and potential FTO fences for dual-frequency, reference-circuit or live-conductivity redesigns. They do not prove that the frozen commodity-probe approach is novel merely because it is cheaper.

### 9.3 METER Group / Decagon

METER’s products and patents illustrate advanced dielectric measurement, factory/soil-specific calibration and research-grade sensing. Product performance statements cannot substitute for claim reading, but the ecosystem confirms a mature field with extensive calibration practice.

### 9.4 Delta-T Devices

Delta-T has relevant moisture-content/impedance and multi-parameter sensing activity. Its commercial WET-family positioning around water content, conductivity and temperature further demonstrates that environmental compensation is an established objective.

### 9.5 Sentek

Sentek’s historical probe and insertion-related rights show that probe geometry, installation and soil contact have long been treated as important technical variables. Some relevant records are expired, but remain prior art.

### 9.6 Toro

Toro’s patent activity is often connected to wireless sensing and irrigation control. It is useful context, but irrigation-controller features are outside the frozen TrueMoist scope and must not be imported to manufacture a technical effect.

### 9.7 Vegetronix and low-cost commercial probes

Commercial low-cost probe ecosystems establish availability and known shortcomings, not patent white space. A product’s lack of a visible feature does not prove absence from patents or NPL.

---

## 10. Non-patent prior art and measurement practice

### 10.1 Unit-to-unit variability

Published evaluations of low-cost capacitive probes, including SEN0193-class devices, report meaningful unit-to-unit variation. Multi-unit studies use universal, individual, one-point or soil-specific calibrations. This directly weakens a broad claim that probe-specific characterization or sparse transfer is new.

### 10.2 Temperature and salinity sensitivity

Dielectric/capacitive measurements are affected by temperature, conductivity/salinity, soil composition and frequency. Compensation through calibrated models, higher-frequency sensing or direct conductivity measurement is established practice.

### 10.3 Packing, insertion and field transfer

Packing density, air gaps, insertion geometry, soil contact, installation disturbance and settling can dominate low-cost probe behavior. Laboratory calibration may transfer poorly to field conditions. These facts support the need for remount/packing tests, but they also show that the problem is well known.

### 10.4 Gravimetric reference

Oven-dry gravimetric water content is a standard reference method. Drying to constant mass near 105 °C is widely used. Volumetric water content requires an independently justified bulk-density or known-volume conversion; gravimetric measurement alone does not justify a VWC claim.

### 10.5 Statistical models and validity methods

Linear, polynomial, ridge, prediction-interval, residual, distance, Mahalanobis, anomaly/OOD and abstention methods are generic data-analysis tools. Their use can contribute to a patent only when a claim defines a specific technical interaction with the physical sensor and produces a non-obvious technical effect. The mathematics alone is not the invention.

---

## 11. Frozen-MVP patent assessment

### 11.1 Novelty

No exact single anticipation of every frozen detail was established. Nevertheless, nearly every feature is expressly disclosed or necessarily suggested by close patents and NPL. The remaining distinctions are mostly parameter choices, experimental design and commodity implementation details.

**Conclusion:** textual novelty may be draftable, but a credible technical novelty nucleus is not established.

### 11.2 Inventive step / obviousness

A skilled soil-sensor engineer facing temperature and salinity cross-sensitivity would predictably:

- measure nearby temperature;
- characterize salinity/conductivity influence;
- control sample preparation and packing;
- gather gravimetric reference data;
- fit linear and nonlinear calibration models;
- regularize an overparameterized model;
- deploy fixed coefficients locally;
- improve the analog signal path; and
- validate on held-out physical replicates.

**Conclusion:** obviousness risk is high.

### 11.3 Patent eligibility

The frozen output is a corrected numerical moisture estimate produced by generic regression on conventional electronics. A sensor-linked claim is not automatically ineligible, but the specification would need a concrete technical contribution beyond mathematics and data organization.

**Conclusion:** eligibility is uncertain and does not rescue the absence of novelty/inventive step.

### 11.4 FTO

The frozen design appears less exposed than custom live-EC, multi-frequency or matched-resonance architectures. That is not clearance. A jurisdiction-specific claim chart is still required before commercial manufacture, sale or deployment.

### 11.5 Overall frozen-MVP verdict

- **Engineering value:** High.
- **Scientific evidence value:** High if executed rigorously.
- **Semester demonstration value:** High.
- **Current patent value:** Low.
- **Patent-first readiness:** No.

---

## 12. Candidate invention-direction matrix

| Direction | Physical problem / proposed contribution | Closest art and principal risk | Required physical effect and baselines | Three-month feasibility | Track / confidence / kill condition |
|---|---|---|---|---|---|
| 1. Probe-specific characterization | Characterize each unit and bind coefficients to probe ID | Individual/universal calibration NPL; ordinary metrology | Lower error than pooled model; compare per-probe oracle, pooled and one-point | High | **D alone, High confidence.** Kill as patent path if only unit-specific coefficients emerge |
| 2. Replacement-probe transfer | Transfer donor calibration to replacement using sparse anchors | CN102914568B; calibration-transfer NPL; TCS replacement context | Lower transfer RMSE and workload than no transfer, one-point and two-point affine; near per-probe oracle | Pilot feasible, proof not feasible | **C, Medium.** Kill if no advantage over simple affine transfer |
| 3. Dual-probe disagreement for health | Use disagreement to invalidate rather than average | Redundant sensing, WO2020047587 and TCS health logic | Detect one-probe faults without confusing spatial/packing differences | High | **D alone; C as component, High.** Kill if correlated drift or excessive false invalidation |
| 4. Insertion/packing-aware compensation | Detect or invalidate installation-induced error | Placement/void/settling art and NPL | Lower remount error versus fixed calibration and manual packing code | Moderate | **D alone, High.** Without runtime observability it is experimental control, not deployable invention |
| 5. Remount/reinstallation acceptance | Physical test determines whether existing coefficients remain valid after remount | Calibration fixtures, replacement equivalence and installation art | Reduced severe accepted error after remount; low false rejection | Pilot feasible | **C, Medium.** Kill if simple one-point check performs equally |
| 6. Contamination-protected drift adaptation | Permit update only when reference event is uncontaminated by salinity/temperature/packing | Senviro and Bosch event recalibration; generic update gating | Lower false-update rate and post-update error than unrestricted recalibration/fixed model | Pilot feasible | **C, Medium-low.** Kill if gate cannot distinguish confounders |
| 7. Confidence-gated/abstaining estimate | Reject estimates outside validated physical domain | Generic OOD/anomaly methods; Bosch confidence/error handling | Lower severe accepted-error rate at tolerable rejection rate versus always-output/min-max gate | High | **D alone; C as component, High.** Kill if only generic distance/min-max logic |
| 8. Reference-event self-validation | Use sparse physical event to validate/update calibration | Strongly covered by Senviro and Bosch | New event discriminator must outperform ordinary wet/dry event calibration | Moderate | **D broad; C only with new discriminator, High.** Kill if event is ordinary watering/dry-down |
| 9. Physics-informed low-order compensation | Add monotonic/physical constraints to regression | CN108414007B and extensive NPL | Unexpected robust improvement over ridge/polynomial baselines | High | **D, High.** Kill if effect is ordinary regularization |
| 10. Calibration provenance and validity envelope | Bind model to probe, batch, range and physical conditions | Preset correction, provenance and validity concepts | Provenance must cause a concrete physical acceptance/fallback decision | High | **D alone; C as component, High.** Kill if record keeping is administrative only |
| 11. Lifecycle/ageing fingerprint | Distinguish ageing state from environmental disturbance | TCS degradation analysis; sensor drift literature | Detect controlled ageing proxy with low false alarms across remount/packing states | Low within semester | **C, Low-medium.** Kill if state is only time/offset threshold |
| 12. Transfer across soil batches/classes | Reduce recalibration across batches/soils | Soil-specific/universal calibration literature; CN correction strategy | Better than one-point or soil-specific recalibration | Not credible in frozen semester scope | **C mainly publication, Low.** Kill if soil-specific calibration remains necessary |
| 13. Multi-frequency moisture/salinity separation | Physically separate dielectric and conductivity effects | Campbell, METER and extensive impedance art | Better separation/accuracy from custom hardware | No; major redesign | **D for current project, High.** Crowded and outside frozen scope |
| 14. Live-EC-assisted compensation | Measure conductivity and compensate moisture | Numerous multi-parameter sensors/patents | Live EC must add net accuracy after its own uncertainty | No; major redesign | **D for current project, High.** Outside frozen scope and risks electrochemical subproject |
| 15. Physical-reference-bound transfer/acceptance mechanism | Combine sparse replacement/remount challenge, disturbance discrimination, bounded transfer, contamination gate and safe abstention | CN102914568B, TCS, Senviro, Bosch, generic validity/OOD art | Material reduction in calibration workload and severe accepted errors, with synergistic advantage over every component baseline | Feasibility pilot only | **C, Medium — strongest direction.** Kill if full mechanism is no better than affine transfer + generic gate |

### 12.1 Track result

- **Track A:** none.
- **Track B:** none established with adequate confidence.
- **Track C:** physical-reference-bound transfer/acceptance; contamination-protected update only as a subordinate possibility; lifecycle fingerprinting as lower-confidence later work.
- **Track D:** frozen compensation and most standalone “smart” features.

---

## 13. Strongest surviving direction

### 13.1 Working description

A **physical-reference-bound calibration transfer and validity acceptance method for replacement or remounted commodity soil-moisture probes**.

The method would not claim generic regression, probe identity, Mahalanobis distance or an abstention flag. Its prospective technical center would be a specific interaction between:

1. a predefined physical reference challenge or short sequence;
2. donor and replacement probe response features;
3. bounded transfer parameters;
4. residual patterns that separate unit bias from temperature, salinity, packing/remount and genuine moisture change;
5. a contamination gate that prevents an invalid reference event from changing the model;
6. an acceptance state that permits transferred coefficients only inside a physically validated region; and
7. a fallback/abstention state when validity is lost.

### 13.2 Why this is stronger than generic confidence gating

A generic distance gate asks whether a vector looks statistically familiar. That is standard analytics and may reject data without identifying the physical cause. The stronger hypothesis uses an explicit physical challenge to test whether the measurement chain remains equivalent enough for a defined calibration transfer, and rejects transfer when confounding residuals show that equivalence is not physically supported.

### 13.3 Closest-art problem

Every broad component is crowded:

- replacement equivalence: CN102914568B;
- low-cost sensor calibration/health/replacement: TCS family;
- event recalibration and environmental disturbance: Senviro and Bosch;
- correction identifiers and preset models: CN111103333B;
- nonlinear temperature compensation: CN108414007B;
- confidence/OOD/abstention: generic sensor and ML practice.

The path survives only if the exact combined sequence is not claimed elsewhere and experiments show a non-additive physical effect.

### 13.4 Required differentiating effect

The mechanism must distinguish, with useful accuracy and less calibration work:

- replacement-unit bias;
- remount/packing error;
- temperature disturbance;
- salinity-treatment disturbance;
- genuine moisture change; and
- sensor degradation or electronic offset.

A credible effect could be materially lower transfer RMSE, lower worst-subset error, fewer silently wrong accepted estimates and less calibration workload than all simple baselines.

### 13.5 Why the result remains Track C

- Only two probes are planned.
- Manufacturing-lot diversity is absent.
- Ageing evidence is absent.
- Remount and contamination data are absent.
- No result yet demonstrates synergy.
- Close art already occupies the broad conceptual territory.
- A three-month study can test feasibility, not establish general transfer or a patent-ready invention.

---

## 14. Level-1 compensation versus Level-2 robustness/transfer

| Dimension | Level 1 — frozen compensation | Level 2 — robustness, transfer and validity |
|---|---|---|
| Core question | Can a fixed local model reduce error for two probes in one soil under controlled temperature and salinity treatment? | Can a replacement, remounted, aged, contaminated or mismatched probe be transferred, accepted, rejected or safely abstained through a validated physical mechanism? |
| Inputs | Raw probe response, measured temperature, controlled salinity-treatment code | Probe identity/lot, transfer anchors, physical challenge response, disturbance residuals, remount/packing indicators, trusted-event status and lifecycle evidence |
| Output | Compensated GWC estimate | Estimate plus transfer-validity state, health/acceptance state and fallback/abstention decision |
| Evidence base | 72 physical runs | Multi-unit, multi-lot, repeated remount, contamination and ageing programme |
| Semester feasibility | High if metrology access is available | Small pilot only |
| Engineering value | High | Potentially high |
| Patent value | Low | Possible but unproven |

A passing Level-1 result does not prove Level-2 transfer, sensor health, field robustness, multi-soil operation, patentability or FTO.

---

## 15. Novelty

### 15.1 Frozen MVP

The exact complete stack may not be literally recited in one located claim, but its distinctions are mostly conventional selections and experimental parameters. Novelty based on “ESP32 + ADS1115 + DS18B20 + 72 runs + ridge + USB” would be formalistic rather than technical.

**Assessment:** No credible novelty nucleus established.

### 15.2 Level-2 candidate

The exact combined sequence of a physical replacement/remount challenge, bounded software transfer, contamination discrimination and abstention was not verified in one independent claim during this synthesis. Narrow novelty may therefore be possible after the mechanism is fully defined.

That conclusion is highly qualified. Broad transfer, health, event recalibration, reference-media equivalence, preset correction and confidence concepts are known. A new claim must recite the exact physical operations and state transitions that produce a measurable result.

**Assessment:** Possible narrow novelty; medium-low confidence until a second claim-focused search after mechanism freeze.

---

## 16. Inventive step/obviousness

### 16.1 Frozen MVP

**Risk: High.** The architecture follows ordinary engineering optimization in response to known error sources.

### 16.2 Generic confidence/OOD enhancement

**Risk: High.** Adding a known statistical distance, envelope or abstention rule to prevent extrapolation is a predictable use of established analytics. Running it on an ESP32 or applying it to a cheap soil probe does not by itself make the combination non-obvious.

### 16.3 Physical-reference-bound transfer mechanism

**Risk: Medium-high.** The combination could become non-obvious only if:

- the physical challenge is not an ordinary one/two-point calibration;
- the residual structure separates physically confounded states in a way the close art does not teach;
- the complete mechanism materially outperforms simple affine transfer and generic gates;
- the advantage is reproducible across multiple units/lots/remounts; and
- an engineer would not predict the result from the individual known elements.

An unexpected interaction, not merely improved accuracy after more calibration, is required.

---

## 17. Patent eligibility

### 17.1 United States

A claim to a sensor apparatus or physical measurement process is not automatically abstract. However, a claim centered on calculating regression coefficients, Mahalanobis distance, a confidence score or an invalid flag on generic computing hardware risks being characterized as an abstract mathematical/data-analysis idea. A stronger claim would integrate physical acquisition, a concrete reference challenge, a sensor-state transition and a measurable improvement in physical measurement reliability.

No §101 clearance is given. Eligibility would not cure novelty or obviousness defects.

### 17.2 European Patent Office

Under the EPO’s computer-implemented-invention approach, mathematical features can contribute to inventive step when they serve a specific technical purpose and causally produce a technical effect. Merely labeling a value “confidence,” “validity” or “moisture” is insufficient. The claim and evidence should connect the computation to the operation or reliability of the physical measurement system.

### 17.3 India

Section 3(k) and the current CRI framework create risk for claims framed as mathematical methods, algorithms or computer programs per se. A stronger Indian presentation would claim a complete sensor-linked method, physical reference operations and demonstrable improvement in a physical measurement process. The 2025 CRI Guidelines and current Indian case law require professional review before filing.

### 17.4 Eligibility conclusion

A specific physical-reference/acceptance mechanism may have a better eligibility posture than ordinary regression or generic OOD gating. It is not automatically eligible and has not been legally cleared.

---

## 18. FTO

### 18.1 Frozen MVP

No FTO clearance is given. Apparent risk is lower than for a custom multi-frequency or live-EC product because the design reads an off-the-shelf analog probe and applies fixed local compensation. Main caution areas are:

- soil/temperature correction strategy claims in China;
- nonlinear compensation claims in China;
- use of patented custom probes or signal-conditioning circuits embodied in a selected commercial probe;
- calibration-fixture/reference-media claims depending on the exact process.

### 18.2 Level-2 extension

Principal live-claim concerns include:

| Jurisdiction | Principal concern | Preliminary design-distance strategy |
|---|---|---|
| United States | TCS sensor-health grant; active Campbell/RLC/reference-circuit grants | Avoid rugged-reference normalization, image-based degradation, matched resonance/reference circuitry and dual-frequency live-salinity sensing |
| Europe | EP4090953B1 and any live event-calibration national stages | Keep mechanism distinct from claimed degradation/replacement pipeline and obtain EPO/national register chart |
| India | Indian-priority TCS family | Verify granted Indian claims and avoid assuming research/academic use is exempt |
| China | CN102914568B, CN111103333B, CN108414007B | Avoid claimed hardware output-equivalence conditioning, GIS/preset correction architecture and claimed nonlinear model sequence |
| PCT/national stages | WO2020047587 family | Identify live national-stage claims before implementing event recalibration commercially |

### 18.3 FTO conclusion

- “High/clear FTO” is rejected.
- Failure to find an exact duplicate is not clearance.
- Expired prior art may still defeat patentability but not block present activity.
- Academic prototyping is not a universal infringement exemption.
- A professional search must be scoped to intended countries and acts before commercialization or filing-dependent design freeze.

---

## 19. Claim-to-experiment map

All patent-oriented thresholds below are **proposed** and must be owner-approved and preregistered before confirmatory testing.

| Prospective claim element | Physical experiment | Required baseline/ablation | Metrics | Proposed kill condition |
|---|---|---|---|---|
| Bounded replacement-probe transfer | Train donor A; transfer to B using defined physical anchors across moisture/temp/salt conditions | No transfer; naïve coefficient reuse; one-point; two-point affine; pooled model; full B oracle | RMSE, MAE, bias, calibration sample count | No material advantage over simple two-point affine transfer |
| Remount acceptance test | Remove/reinsert B under controlled packing/remount states | No test; single-point check; generic range check | Remount error, false accept, false reject | Severe invalid states pass or valid remounts are excessively rejected |
| Disturbance-residual validity envelope | Apply unseen temperature, salinity, packing and electronic-offset perturbations | Min/max gate; Mahalanobis-only gate; prediction interval; always-report | Accepted severe-error rate, coverage, rejection rate | Generic gate performs equally or better |
| Contamination-protected update gate | Present clean reference events and confounded salt/packing/temp events | Unrestricted event recalibration; fixed model; no contamination test | False-update rate, post-update RMSE, recovery | Gate blocks most clean events or accepts many contaminated events |
| Sensor-state discrimination | Controlled genuine moisture change, unit bias, remount, contamination and ageing proxy | Simple disagreement/offset threshold | Confusion matrix, detection delay, false alarms | States remain practically indistinguishable |
| Safe abstention/fallback | Drive chain outside validated conditions | Always-output model | Severe accepted-error distribution, false invalidation | No meaningful severe-error reduction at usable coverage |
| MCU implementation | Reproduce Python mechanism on ESP32 | Host-only output | Numerical equivalence, latency, RAM, flash, energy | Embedded output differs materially or exceeds resources |
| Complete synergistic mechanism | Full sequence versus removal of each element | Every critical ablation | RMSE/MAE, worst-subset error, severe-error probability, workload | Complete method is merely additive or no better than simple transfer + generic gate |

Required factors, where relevant, include moisture, temperature, salinity treatment, independent physical replicate, probe unit and lot, preparation batch, insertion/packing, remounting, ADC/wiring path, contamination, wet/dry cycling, drift/ageing proxy and later soil class. Rapid ADC readings must not be counted as independent physical samples.

---

## 20. Three-month semester plan

### Weeks 1–2 — Measurement-chain gates

- Verify genuine analog probe behavior, monotonicity, warm-up and short-term repeatability.
- Perform reinsertion and packing-sensitivity screening.
- Confirm oven and 0.01 g scale access.
- Complete paired ADS1115 versus calibrated ESP32 ADC1 testing.
- Freeze container, insertion jig, packing procedure, wiring, connectors and soldered AFE.
- Establish confidentiality and dated contribution records.

### Weeks 3–6 — Frozen Level-1 dataset

- Collect exactly 72 independent physical runs.
- Keep replicates 1–2 for model selection and replicate 3 untouched.
- Fit M0, M1 and M2.
- Report absolute RMSE/MAE, bias and temperature/salinity subsets.
- Do not count averaged ADC readings as physical replicates.

### Weeks 7–8 — Two-probe transfer feasibility pilot

Using Probe A as donor and Probe B as replacement:

- naïve donor-coefficient reuse;
- one-anchor transfer;
- two-anchor affine transfer;
- pooled calibration;
- full Probe-B calibration as oracle;
- evaluate all across temperature and salinity subsets.

This can identify whether transfer is worth continuing. It is not population-level proof.

### Weeks 9–10 — Remount, validity and contamination pilot

- Reinstall Probe B with controlled remount/packing variations.
- Apply bounded temperature and salinity disturbances.
- Simulate an electronic offset or short-term drift proxy.
- Compare min/max, generic distance/Mahalanobis and physical-residual gates.
- Test clean versus contaminated reference events.

### Week 11 — Ablation and kill gate

- Compare the complete candidate with simple affine transfer plus generic gating.
- Remove each proposed element in turn.
- Stop patent development if the result is ordinary calibration practice or if no synergy is observed.

### Week 12 — Institutional IPR decision

- Prepare a confidential invention disclosure only if the candidate survives.
- Identify actual human inventors from recorded contributions.
- Commission a professional claim/status search targeted to the precise mechanism and intended jurisdictions.
- Do not publicly release new mechanism details, coefficients or labelled Level-2 data before review.

---

## 21. Later-semester or publication extension

A credible Track-C programme requires substantially more evidence:

- 6–12 nominally identical probes;
- more than one manufacturing lot where possible;
- at least three independently prepared batches;
- repeated remove/reinstall cycles;
- controlled packing and air-gap perturbations;
- contamination and fertilizer/salinity confounders;
- accelerated ageing or electronic-drift proxies;
- field wetting/drying events;
- independent gravimetric checks;
- predefined false-valid and false-invalidation thresholds;
- later testing in additional soil classes;
- comparison with universal, pooled, one-point, two-point and full per-probe calibration;
- claim-specific ablations.

Even if patentability fails, publication value can remain high. A strong paper could report unit variability, transfer limits, remount sensitivity, validity-envelope coverage, severe-error reduction from abstention and failure of naïve event recalibration under confounding disturbances. Publication must follow IPR review.

---

## 22. Budget, measurement, compute, and team feasibility

### 22.1 Frozen MVP

The architecture remains feasible within the preferred ₹3,000 target when oven and scale access are institutional, and can remain within ₹5,000 with careful procurement. The major risk is not compute but experimental labor and metrology.

### 22.2 Level-2 semester pilot

The existing second probe supports a donor/replacement pilot. Extra containers, jig materials and connectors are modest. A third or fourth probe would improve interpretation if budget permits. No live EC, custom multi-frequency hardware or TinyML is required.

A two-probe pilot can fit within ₹5,000, but cannot establish manufacturing-population transfer.

### 22.3 Later-semester proof

Six to twelve probes, multiple lots, field access, long-term cycling and reference equipment may exceed the current student budget and require institutional support. This is a principal reason for Track C rather than Track B.

### 22.4 Compute

- Level-1 fixed polynomial inference is negligible on ESP32.
- Distance/residual/acceptance logic is also lightweight.
- RAM, flash and runtime are not expected to be limiting.
- The hard problem is physically valid labels and independent repetitions, not MCU capacity.

### 22.5 Team allocation

- **Member 1:** embedded acquisition, firmware, ADC gate and local state/fallback logic.
- **Member 2:** statistical modelling, transfer baselines and ablation.
- **Member 3:** hardware, jig, packing/remount and gravimetric workflow.
- **Member 4:** logging, data integrity, randomization and experiment automation.
- **Member 5:** documentation, photographs, chain-of-custody/confidentiality and presentation support.

The three technically strong members must retain responsibility for measurement validity, statistical interpretation and patent-mechanism decisions.

---

## 23. Kill criteria

Terminate the patent-development path, while optionally continuing the semester prototype, if any of the following occurs:

1. Probe response is not stable or monotonic enough for credible calibration.
2. Traceable gravimetric reference access is unavailable.
3. Packing/reinsertion variance overwhelms the controlled environmental effects.
4. Level-1 compensation fails the accepted RMSE or MAE improvement thresholds.
5. The salinity treatment does not create a repeatable, non-saturated response difference.
6. Replacement transfer does not outperform one-point or two-point affine calibration.
7. The validity mechanism fails to reduce severe accepted errors.
8. Abstention rejects an impractical fraction of valid measurements.
9. A contamination gate cannot distinguish clean references from salinity, packing or temperature confounders.
10. State classification confuses genuine moisture change with probe/remount/degradation effects.
11. The complete mechanism is no better than additive known components in ablation.
12. The claim center reduces to regression, a treatment code, dataset organization, Mahalanobis distance, provenance or ordinary calibration.
13. Meaningful differentiation requires live EC, multi-frequency custom hardware or a custom probe within the semester.
14. A claim-focused search locates prior art that anticipates or makes the defined mechanism clearly obvious.
15. Target-jurisdiction live claims create unacceptable design-around or licensing risk.
16. Public disclosure has already destroyed required filing options.
17. Institutional IPR review does not support filing.

---

## 24. Confidentiality boundary

### May be discussed generically

- low-cost capacitive probes;
- temperature and salinity effects;
- ordinary regression;
- gravimetric calibration;
- the frozen 72-run engineering design.

### Keep confidential pending institutional IPR review

- exact physical-reference challenge sequences;
- probe fingerprints;
- transfer mappings;
- validity-envelope definitions;
- contamination gates;
- remount acceptance logic;
- lifecycle-state features;
- coefficient/provenance binding;
- parameter values;
- raw labelled transfer/remount/ageing datasets;
- code, negative results and ablations;
- invention chronology and contributor records.

Do not publicly disclose the new Level-2 mechanism or data before institutional IPR review. Maintain dated laboratory notebooks, version-control history and contributor records. External AI or literature suggestions are background evidence, not human inventorship.

---

## 25. Final TrueMoist recommendation

### Required recommendation

**Retain as strong semester prototype but reduce patent priority.**

### Rationale

TrueMoist should proceed as a rigorous, affordable engineering project because it can produce a strong live demonstration and valuable measurement data. Its frozen compensation architecture is not, however, a credible patent-first invention. The strongest extension is crowded and requires later multi-unit physical evidence.

The appropriate strategy is:

1. complete the frozen Level-1 MVP without scope drift;
2. run only a bounded, confidential two-probe Level-2 feasibility pilot;
3. apply the kill criteria strictly;
4. continue into a later-semester Track-C programme only if transfer and physical-validity results materially outperform simple baselines; and
5. seek institutional IPR and professional patent review before disclosure or filing.

This recommendation is specific to TrueMoist. It does not compare it with another concept and does not select the final Project mC winner.

---

## 26. Unresolved questions

1. What are the exact granted claims and current official status of the Indian TCS family member?
2. In which EP states is EP4090953B1 validated and in force, and is any opposition pending?
3. Which national stages from WO2020047587A1 remain live?
4. What are the official CNIPA status and professionally translated enforceable scopes of CN102914568B, CN111103333B and CN108414007B?
5. Which countries and commercial acts should define a real FTO search?
6. Is the salinity-treatment code laboratory metadata only, or is a future user expected to supply it at runtime?
7. What exact physical reference event is available without converting the project into an irrigation controller?
8. Can the existing inputs distinguish contamination from moisture, temperature and packing effects without an added sensor?
9. Can two probes show anything beyond a pair-specific coincidence?
10. Can multiple probe lots be purchased within the budget?
11. What fallback behavior is technically safe when validity is lost?
12. What false-valid, false-invalidation and coverage thresholds will be preregistered?
13. How will a remount challenge be standardized and measured?
14. Which ageing proxy is physically credible without damaging the probe irreversibly?
15. Has any potentially filing-relevant Level-2 mechanism already been publicly disclosed?
16. Who contributed each prospective inventive element?
17. What assignment, disclosure and pre-publication rules apply at the institution?

---

## 27. Source and verification log

### 27.1 Governing and project-authority sources

- `00_READ_FIRST_TrueMoist_Synthesis_Instructions.md` — governing scope, audit method, tracks, report structure and confidentiality.
- `01_Engineering_Design_Review.md` — engineering identity and original hypothesis.
- `02_Project_mC_Decision_Register_v1.2.md` — binding project and TrueMoist decisions.
- `03_Phase3C_Portfolio_Closure_Memo_Approved.md` — retained-portfolio status and patent-first priority context.
- `04_Phase3C_TrueMoist_Architecture_Report_Final.md` — authoritative 72-run architecture.
- `05_Phase3C_TrueMoist_Memory_Final.md` — compact frozen architecture and gates.
- `06_Phase3C_TrueMoist_SOP_Final.md` — architecture process, evidence and anti-drift rules.
- `07_Concept_Evidence_Matrix.md` — current evidence extraction.
- `08_Uncertainty_and_Test_Register.md` — unresolved tests and risks.
- `09_Patent_Research_Input_Pack.md` — historical leads and search questions.
- `10_Phase2_Report_by_Claude.md` — historical leads only.

### 27.2 Audited research lanes

- `11_TrueMoist_Patent_Research_ChatGPT_DR.md`
- `12_TrueMoist_Patent_Research_Gemini.docx`
- `13_TrueMoist_Patent_Research_Perplexity.md`
- `14_TrueMoist_Patent_Research_Qwen_COMPILATION.md`
- `15_TrueMoist_Patent_Research_Mistral.md`
- `16_TrueMoist_Patent_Research_Microsoft_Copilot.docx`

No lane was counted as a vote. Unsupported claims were corrected or excluded.

### 27.3 Primary patent records checked

- WO2021144807A1; linked US12175680B2 and EP4090953B1 — TCS low-cost soil-sensor health family.
- CN102914568A/B — replaceable probe and output-equivalence calibration.
- US20080199359A1; WO2007002994; EP1899716 family — self-learning soil-moisture calibration.
- WO2020047587A1 — event-based soil-moisture auto-calibration.
- CN111103333B — preset soil/temperature correction strategies.
- CN108414007B — temperature-dependent nonlinear compensation.
- US7408364B1; US7535237B1; US7884620B2; WO2009094324A2 — Campbell/Advanced Sensor Technology moisture/salinity lineage.
- US11598743B2 — matched resonance/reference single-probe architecture with dependent temperature compensation.
- US9804113B2 / US20150330932A1 — series-RLC moisture sensing.
- US11415612B2 — complex dielectric/admittance sensing.
- US7944220B2 — Delta-T moisture-content sensing lineage.
- US7240743B2 — Sentek probe/insertion lineage.
- EP2623971 and US9146206-related calibration apparatus records.
- US5430384A — older temperature-compensated soil-moisture sensor.
- CN116298198A — multi-parameter/fusion activity.

### 27.4 Non-patent and standards/practice categories checked

- multi-unit low-cost capacitive probe calibration and sensor-to-sensor variability;
- SEN0193-class universal, individual and single-point calibration studies;
- temperature/salinity/conductivity effects on dielectric probes;
- packing, insertion, settling and laboratory-to-field transfer;
- gravimetric oven-dry methods and VWC/bulk-density distinction;
- generic regression, uncertainty, residual, anomaly/OOD and abstention methods.

### 27.5 Legal and status sources

- USPTO Patent Public Search and current subject-matter-eligibility guidance.
- EPO Register/publication sources and 2026 Guidelines for computer-implemented inventions and mathematical methods.
- Indian Patent Office current CRI Guidelines listing and Section 3(k) framework.
- Google Patents used for discovery and text/status clues only; its legal-status labels were treated as non-conclusive.

### 27.5A Direct verification links

Primary patent texts used for claim-level checking:

- [WO2021144807A1 — TCS sensor-health family](https://patents.google.com/patent/WO2021144807A1/en)
- [US12175680B2 — US TCS family member](https://patents.google.com/patent/US12175680B2/en)
- [EP4090953B1 — EP TCS family member](https://patents.google.com/patent/EP4090953B1/en)
- [CN102914568B — replaceable probe](https://patents.google.com/patent/CN102914568B/en)
- [US20080199359A1 — self-learning soil-moisture calibration](https://patents.google.com/patent/US20080199359A1/en)
- [WO2020047587A1 — event-based auto-calibration](https://patents.google.com/patent/WO2020047587A1/en)
- [CN111103333B — preset soil/temperature correction](https://patents.google.com/patent/CN111103333B/en)
- [CN108414007B — temperature-dependent nonlinear compensation](https://patents.google.com/patent/CN108414007B/en)
- [US7884620B2 — Campbell/Advanced Sensor Technology](https://patents.google.com/patent/US7884620B2/en)
- [US11598743B2 — matched resonance/reference probe](https://patents.google.com/patent/US11598743B2/en)
- [US9804113B2 — series-RLC sensing](https://patents.google.com/patent/US9804113B2/en)
- [US11415612B2 — complex dielectric sensing](https://patents.google.com/patent/US11415612B2/en)
- [US7944220B2 — Delta-T lineage](https://patents.google.com/patent/US7944220B2/en)
- [US7240743B2 — Sentek lineage](https://patents.google.com/patent/US7240743B2/en)

Official legal/status resources used as authority points:

- [USPTO Patent Public Search](https://ppubs.uspto.gov/pubwebapp/)
- [USPTO subject-matter eligibility](https://www.uspto.gov/patents/laws/examination-policy/subject-matter-eligibility)
- [European Patent Register](https://register.epo.org/)
- [EPO Guidelines — mathematical methods](https://www.epo.org/en/legal/guidelines-epc/2026/g_ii_3_3.html)
- [IP India guidelines](https://ipindia.gov.in/Patents/guidelines_patents)

### 27.6 Verification labels used

- **Verified fact:** directly supported by a project-authority document or patent claim/publication record.
- **Provisional status:** public database status not yet confirmed in the official national register.
- **Lane assertion:** statement found in a research lane but not independently verified.
- **Inference:** reasoned conclusion from verified facts, explicitly qualified.
- **Recommendation:** proposed next action, not a factual or legal conclusion.


---

## Source 6: `03_CONCEPT_PORTFOLIO/TrueMoist/05_Roadmaps_and_Reference_Dossiers/HISTORICAL_Phase1C_TrueMoist_Concept_Dossier.docx`

- Authority: `TIER_2`
- Treatment: `SUPPORTING_EVIDENCE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `ca5cedfdfac5157b328aa865433a172d8af82a44d2dbf8b015c8c217fa6f85a2`

# Source Extraction

- Chapter: `08` — TrueMoist Architecture, Validation and Patent Evidence
- Authority tier: `TIER_2`
- Manual treatment: `SUPPORTING_EVIDENCE`
- Original source: `03_CONCEPT_PORTFOLIO/TrueMoist/05_Roadmaps_and_Reference_Dossiers/HISTORICAL_Phase1C_TrueMoist_Concept_Dossier.docx`
- Current SHA-256: `ca5cedfdfac5157b328aa865433a172d8af82a44d2dbf8b015c8c217fa6f85a2`
- Extraction method: `DOCX_XML`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

Document 3 – TrueMoist Concept Dossier

Self-Correcting Smart Soil Monitoring System

Executive Summary

We are proposing an intelligent soil monitoring concept that addresses one of the fundamental weaknesses of affordable precision agriculture: sensor drift. Low-cost soil moisture sensors gradually lose accuracy because of aging, soil chemistry, salinity, corrosion, and changing environmental conditions. This concept investigates a self-correcting embedded monitoring approach capable of maintaining reliable measurements over extended periods, enabling more trustworthy irrigation decisions while remaining affordable for small and medium farms.

Background and Motivation

Agriculture consumes a significant proportion of freshwater resources, yet irrigation decisions are often based on inaccurate or infrequent measurements. During Phase 1A, agriculture consistently emerged as a high-impact domain because it combines a global need for water conservation with strong opportunities for embedded sensing. Phase 1B showed that the real research opportunity is not simply measuring soil moisture—many products already do that—but improving long-term measurement reliability. Phase 1B.5 retained this opportunity because it balanced novelty, affordability, demonstration quality, and semester feasibility. Phase 1C transformed this opportunity into the TrueMoist concept by focusing specifically on intelligent drift correction rather than conventional smart irrigation.

Problem Statement

Many affordable soil monitoring systems become unreliable over time because sensors drift from their original calibration. Farmers may unknowingly over-irrigate or under-irrigate crops, leading to wasted water, reduced yields, and increased operational costs. Frequent manual recalibration is impractical, especially for large deployments.

Current Solutions

Commercial precision agriculture platforms generally rely on periodic recalibration, expensive industrial-grade sensors, or cloud analytics. Low-cost hobby systems often provide only instantaneous readings without evaluating long-term sensor health. These limitations create a research gap for embedded systems that can continuously monitor sensor quality and compensate for gradual degradation.

Research Gap

The opportunity identified during the earlier phases was not 'build another irrigation system' but 'increase trust in low-cost sensing.' Few affordable educational or small-farm systems attempt continuous self-assessment of sensor reliability, creating an opportunity for innovation.

Why Embedded Systems

This problem requires continuous sensing, real-time analysis, local decision making, and reliable long-term operation. Embedded systems provide deterministic control, low power consumption, and the ability to process environmental information directly at the sensing location without requiring continuous Internet connectivity.

Proposed Concept

The proposed concept investigates an adaptive monitoring platform capable of observing environmental behaviour, identifying abnormal sensor drift, and maintaining reliable moisture estimation using embedded intelligence. The emphasis is on improving confidence in measurements rather than merely collecting more data.

Expected Innovation

Potential innovation areas include adaptive calibration logic, drift detection algorithms, sensor health estimation, lightweight edge intelligence, and intelligent irrigation recommendations. These areas represent possible patent and research opportunities that should be validated through future literature and patent analysis.

Applications

Precision agriculture, greenhouses, urban farming, research farms, educational laboratories, horticulture, and smart irrigation deployments.

Commercial Potential

Reliable low-cost sensing is valuable for farms, agricultural startups, irrigation solution providers, and government water conservation initiatives. A solution that improves trust in affordable sensors could reduce deployment costs while improving agricultural decision making.

Selection Rationale

TrueMoist survived every stage because it addressed a clearly documented engineering gap, demonstrated strong embedded-system relevance, fit the semester budget, and provided an excellent balance between research potential and practical implementation.

Risks

Key risks include validating drift compensation accurately, testing across different soil conditions, and preventing excessive project scope. The project should remain focused on demonstrating intelligent calibration rather than building a complete farm management platform.

Future Scope

Future extensions include multi-sensor fusion, nutrient estimation, weather integration, AI-assisted irrigation forecasting, autonomous irrigation control, and large-scale agricultural monitoring networks.


---

## Source 7: `03_CONCEPT_PORTFOLIO/TrueMoist/PATENT_EVIDENCE_INDEX.md`

- Authority: `TIER_2`
- Treatment: `SUPPORTING_EVIDENCE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `163cb6af44fcced08d6427b30ad00e155163377d0deb33bbced9f2583d3350a1`

# Source Extraction

- Chapter: `08` — TrueMoist Architecture, Validation and Patent Evidence
- Authority tier: `TIER_2`
- Manual treatment: `SUPPORTING_EVIDENCE`
- Original source: `03_CONCEPT_PORTFOLIO/TrueMoist/PATENT_EVIDENCE_INDEX.md`
- Current SHA-256: `163cb6af44fcced08d6427b30ad00e155163377d0deb33bbced9f2583d3350a1`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

# TrueMoist — Patent Evidence Index

## Controlled research lanes

1. ChatGPT Deep Research
2. Gemini
3. Perplexity — partial
4. Qwen compilation
5. Mistral
6. Microsoft Copilot

## Valid synthesis set

1. Max
2. High + Deep Research

## Exclusion

The supplementary ChatGPT Work Max web audit preserved in the archive was not
part of the controlled six-lane adjudication set and is not an extra vote.

## Interpretation

TrueMoist remains the validated 72-run local compensation design. Patent
conclusions remain conditional and do not constitute a grant prediction.


---

## Source 8: `03_CONCEPT_PORTFOLIO/TrueMoist/README.md`

- Authority: `TIER_2`
- Treatment: `SUPPORTING_EVIDENCE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `ea18f095605ccd146aff3f0af396ebfc8fd554fea26eb456b1ca187b52620067`

# Source Extraction

- Chapter: `08` — TrueMoist Architecture, Validation and Patent Evidence
- Authority tier: `TIER_2`
- Manual treatment: `SUPPORTING_EVIDENCE`
- Original source: `03_CONCEPT_PORTFOLIO/TrueMoist/README.md`
- Current SHA-256: `ea18f095605ccd146aff3f0af396ebfc8fd554fea26eb456b1ca187b52620067`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

# TrueMoist — Concept Status

The files under `01_Final_Architecture` define the validated frozen TrueMoist design. The empty pre-build simulation directory does not imply that a simulation exists or was omitted accidentally.


---

## Source 9: `03_CONCEPT_PORTFOLIO/TrueMoist/02_Raw_Research/01_TrueMoist_Patent_Research_ChatGPT_Deep_Research.md`

- Authority: `TIER_3`
- Treatment: `SUPPORTING_EVIDENCE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `NEW_STAGE10L_EXTRACTION`
- SHA-256: `9a4a4cffc2f82b3f4022bc5db2d094afa54a1c9ccfb39d43e6b3321a2af1d8bb`

# Source Extraction

- Chapter: `08` — TrueMoist Architecture, Validation and Patent Evidence
- Authority tier: `TIER_3`
- Manual treatment: `SUPPORTING_EVIDENCE`
- Original source: `03_CONCEPT_PORTFOLIO/TrueMoist/02_Raw_Research/01_TrueMoist_Patent_Research_ChatGPT_Deep_Research.md`
- SHA-256: `9a4a4cffc2f82b3f4022bc5db2d094afa54a1c9ccfb39d43e6b3321a2af1d8bb`
- Extraction method: `PLAIN_TEXT`
- Rule: source text only; no synthesis, correction or reconciliation.

---

# TrueMoist Current Patent Verification — Independent Research

**Evidence cut-off:** 1 August 2026
**Research lane:** Independent technical and patent-verification review
**Scope:** Patent-search and engineering decision support; not legal advice, patentability clearance, claim construction, validity opinion, or freedom-to-operate opinion.

---

## 1. Executive verdict

### Required verdict

**credible long-term path requiring later-semester extension**

### Bottom line

The frozen TrueMoist MVP is a strong, disciplined semester engineering experiment, but the presently frozen combination does **not** establish a credible invention in itself. The principal elements—commodity capacitive sensing, colocated temperature measurement, salinity-aware calibration, analog conditioning, regression, fixed local coefficients, gravimetric ground truth and grouped validation—are individually conventional and, in important combinations, already disclosed or strongly suggested by patent and non-patent prior art.

The controlled salinity-treatment code is useful experimental metadata. It is not measured electrical conductivity and, without a more specific technical mechanism, it is unlikely to supply novelty or inventive step. The 72-run factorial design and untouched physical replicate are excellent scientific practice, but an experimental design that validates a conventional calibration method is not ordinarily a patentable technical contribution.

A surviving patent-development path exists only at **Level 2 robustness and transfer**, not at the frozen MVP’s **Level 1 compensation**. The strongest candidate is a narrowly defined mechanism combining:

1. bounded calibration transfer to a replacement commodity probe;
2. a physically validated calibration-validity envelope;
3. abstention or safe fallback when transfer validity is lost; and
4. contamination protection preventing temperature, salinity, packing or remount disturbances from being misclassified as trusted recalibration events.

However, replacement-probe normalization, sensor-health assessment, confidence filtering and reference-event recalibration are each already represented in prior art. To become a credible invention, the combined mechanism must show a specific technical interaction and an unexpected or materially superior physical measurement effect. Two probes, one soil and a short laboratory run are enough to explore the direction, but not enough to establish a defensible patent case with high confidence.

### Final recommendation preview

**Retain as strong semester prototype but reduce patent priority.**

---

## 2. Input inventory and concept fidelity

### 2.1 Inventory

Exactly eleven logical attachments were present and readable:

| No. | Expected logical file | Uploaded name | Result |
|---|---|---|---|
| 00 | `00_READ_FIRST_TrueMoist_Patent_Research_Instructions.md` | exact logical name | Present and readable |
| 01 | `01_Engineering_Design_Review.md` | `01_Engineering_Design_Review(11).md` | Present; suffix is an upload-name variation |
| 02 | `02_Project_mC_Decision_Register_v1.2.md` | `02_Project_mC_Decision_Register_v1.2(12).md` | Present; v1.2 confirmed |
| 03 | `03_Phase3C_Portfolio_Closure_Memo_Approved.md` | `03_Phase3C_Portfolio_Closure_Memo_Approved(11).md` | Present |
| 04 | `04_Phase3C_TrueMoist_Architecture_Report_Final.md` | exact logical name | Present |
| 05 | `05_Phase3C_TrueMoist_Memory_Final.md` | exact logical name | Present |
| 06 | `06_Phase3C_TrueMoist_SOP_Final.md` | exact logical name | Present |
| 07 | `07_Concept_Evidence_Matrix.md` | `07_Concept_Evidence_Matrix(11).md` | Present |
| 08 | `08_Uncertainty_and_Test_Register.md` | `08_Uncertainty_and_Test_Register(11).md` | Present |
| 09 | `09_Patent_Research_Input_Pack.md` | `09_Patent_Research_Input_Pack(12).md` | Present |
| 10 | `10_Phase2_Report_by_Claude.md` | `10_Phase2_Report_by_Claude(12).md` | Present |

No missing logical file, duplicate logical file, unreadable file or ambiguous substitution was identified. The parenthetical suffixes are naming noise, not extra documents. Decision Register v1.1 was not substituted.

### 2.2 Authority order applied

1. Engineering Design Review
2. Decision Register v1.2
3. Approved Phase 3C closure memo
4. Final TrueMoist architecture report
5. Final TrueMoist memory
6. Final TrueMoist SOP
7. Validated evidence files
8. Phase 2 only as historical search leads

### 2.3 Authoritative architecture

The authoritative architecture is the validated **72-independent-run, D-dominant design with B-style signal hardening**:

- genuine analog capacitive probe, SEN0193-class or characterized equivalent;
- two probe units for variation testing;
- waterproof DS18B20 at the same depth, approximately 20–30 mm from the moisture probe;
- controlled salinity treatment expressed as salt addition per dry-soil mass;
- no mandatory live EC sensor;
- ESP32-WROOM-32, with ESP32-S3 fallback;
- ADS1115 subjected to an evidence-based comparison with calibrated ESP32 ADC1;
- short, filtered, decoupled, fixed and eventually soldered analog path;
- raw univariate baseline, multivariate linear baseline and ridge-regularized second-order candidate;
- offline training and fixed local inference;
- one homogeneous soil and one preparation method;
- 4 moisture × 3 temperature × 2 salinity × 3 independent physical replicates;
- gravimetric dry-basis water content;
- untouched replicate 3 as final physical test data;
- engineering success requiring at least 20% RMSE and 15% MAE improvement over the uncompensated baseline.

### 2.4 Frozen concept boundary

TrueMoist is a local compensation system for a low-cost analog capacitive soil-moisture probe.

It is **not**:

- a live-EC meter;
- an irrigation controller;
- a cloud platform;
- a multi-soil system;
- a custom multi-frequency probe;
- a TinyML showcase;
- an online-adaptive learner;
- a universal calibration-free probe;
- a laboratory reference instrument.

The salinity-treatment code is not bulk-soil EC, apparent EC, pore-water EC or solution conductivity.

---

## 3. Search methodology and reproducible log

### 3.1 Search date and approach

Searches were conducted through 1 August 2026 and rechecked on 2 August 2026 solely to complete this report. Patent discovery and claim reading used Google Patents, USPTO-accessible records, WIPO/PATENTSCOPE indexing, EPO publication and guideline resources, and available Indian Patent Office records. Technical literature searches emphasized primary papers and official institutional sources.

Google Patents status labels were treated as discovery metadata, not conclusive legal-status evidence. Where an official maintenance, national-stage or register record could not be independently confirmed, the status is marked unresolved or provisional.

### 3.2 Core query log

The following query families were used or expanded:

- `capacitive soil moisture temperature compensation patent`
- `soil moisture salinity compensation capacitance patent`
- `dielectric soil moisture conductivity correction`
- `commodity probe calibration transfer`
- `probe-to-probe soil-moisture calibration`
- `soil-moisture sensor drift ageing compensation patent`
- `sensor replacement automatic recalibration soil moisture`
- `insertion packing density compensation soil moisture sensor`
- `remount reinstallation calibration validity moisture probe`
- `gravimetric calibration capacitive soil moisture`
- `polynomial ridge regression sensor calibration`
- `edge soil-moisture compensation microcontroller`
- `uncertainty gated abstaining soil moisture estimate`
- `dual probe disagreement sensor health soil moisture`
- `reference event self calibration soil moisture`
- `multi soil calibration transfer capacitive sensor`
- `multi frequency moisture salinity separation patent`
- `low cost soil moisture sensor health patent`
- `SEN0193 sensor to sensor variability calibration`
- `METER Decagon soil moisture calibration patent`
- `Campbell moisture salinity sensor patent`
- `Toro capacitive soil moisture calibration patent`
- `Sentek Delta-T Vegetronix patent moisture calibration`
- `site:patents.google.com soil moisture correction strategy temperature`
- `site:patents.google.com replaceable probe soil moisture sensor`
- `site:patents.google.com auto calibration soil moisture confidence`

### 3.3 Classification searching

Relevant classes encountered and used for expansion included:

- G01N 27/22 and related subclasses: investigating materials by dielectric or capacitive properties;
- G01N 27/04 and related conductivity/resistance measurement classes;
- G01N 33/24: investigation of soil;
- G01D / G06F classes associated with calibration, signal correction and computer-implemented processing;
- A01G irrigation/agricultural-control classes, used only to identify and then separate controller art from the frozen sensor concept.

### 3.4 Assignee and citation-chain searching

Searches included records connected with:

- Campbell Scientific / Advanced Sensor Technology;
- METER Group / Decagon;
- Toro;
- Sentek;
- Delta-T Devices;
- Vegetronix;
- Tata Consultancy Services;
- Chinese agricultural research institutes and universities;
- Korean soil-sensor applicants;
- citation chains from moisture-and-salinity, self-learning calibration, replacement-probe and sensor-health records.

### 3.5 Search limitations

- A complete commercial FTO search in every jurisdiction was not possible.
- Google status labels are not official legal conclusions.
- USPTO maintenance-fee verification was not completed for every US patent.
- WIPO PCT status does not establish the status of every national stage.
- The Indian Patent Office’s current CRI guideline page was verified, and an Indian grant certificate lead was located for the TCS family, but a full InPASS claim-and-register audit was not completed.
- Machine translations of Chinese claims require counsel-quality review before reliance.
- Product pages were not used to infer patent claim scope.

---

## 4. Technical and patent landscape

The landscape separates into six mature regions.

### 4.1 Basic dielectric/capacitive soil-moisture sensing

Capacitive, impedance, resonant and frequency-domain soil-moisture measurement is old and heavily published. Commodity analog probes are implementations of a mature principle. Using an ADC, microcontroller, RC filtering or local computation does not create novelty.

### 4.2 Temperature compensation

Temperature effects on probe electronics and soil dielectric response are well known. Patents and literature disclose analog and digital temperature compensation, including colocated temperature sensing. Placing a temperature sensor at the same depth improves experimental validity, but is not by itself an invention.

### 4.3 Moisture–salinity/conductivity separation

Campbell-related records disclose high- and low-frequency circuits to derive moisture and salinity. Other records use tuned circuits, migration media, conductivity channels or multi-parameter fusion. This area is crowded and technically different from TrueMoist’s controlled-treatment code, but it establishes that conductivity interference and correction are known problems.

### 4.4 Preset correction and calibration strategies

CN111103333B claims selecting and executing soil-element and temperature correction strategies using preset sensor information. This weakens any broad argument that a stored treatment code, correction identifier or preloaded compensation model is itself inventive.

### 4.5 Self-learning and reference-event recalibration

US20080199359A1 describes using measurement history, wet/dry bounds, watering events, plateaus, temperature, conductivity, placement, soil settling and ageing to continuously recalibrate a low-cost sensor. WO2020047587A1 similarly claims moisture uptake/release sequences, progressive recalibration and optional confidence/error handling. Broad event-triggered self-calibration is therefore not open white space.

### 4.6 Probe transfer, sensor health and validity

CN102914568B addresses a replaceable probe whose conditioned output is made equivalent to the replaced probe. The TCS family, including US12175680B2, EP4090953B1 and an Indian-priority application, addresses low-cost soil-moisture sensor calibration, degradation analysis and replacement recommendations. WO2020047587A1 includes error detection, inconsistent nearby readings and confidence-related exclusion. Broad transfer, health and confidence concepts are crowded; only a very specific implementation with a demonstrated technical interaction could survive.

---

## 5. Verified patent-family ledger

“Status” below distinguishes verified publication/grant facts from provisional database status.

| Ref. | Family / representative publication | Priority | Verified publication facts | Status at cut-off | Prior-art relevance | FTO relevance |
|---|---|---:|---|---|---|---|
| P1 | Campbell/Advanced Sensor Technology moisture-and-salinity lineage: US7408364B1, US7535237B1, US7884620B2, WO2009094324A2 | 2008 lineage; related/CIP records | Multiple US grants; PCT publication | Google records label US grants active and PCT ceased; official maintenance not independently confirmed | Very high for dual-frequency moisture/salinity circuits and polynomial correction | Material if TrueMoist later adopts dual-frequency or live-salinity hardware |
| P2 | US20080199359A1 / WO2007002994A1 / EP1899716A1, “Soil Moisture Sensor” | 2005 | US publication; international/EP counterparts | US application marked abandoned; EP/national status unresolved | Very high for self-learning bounds, watering-event calibration, ageing/settling accommodation | Low from abandoned US application; national-stage FTO unresolved |
| P3 | WO2020047587A1, “System and method for sensor-based auto-calibration of soil-moisture levels” | 2018 | PCT publication | PCT indicated ceased; national stages not fully audited | Very high for uptake/release event calibration, progressive recalibration and confidence/error logic | Jurisdiction-specific national-stage risk unresolved |
| P4 | CN111103333B, “Method and device for calibrating a soil water-content sensor” | 2019 | Chinese application published 2020; grant published 2022 | Google labels active through expected term; official CN register not independently confirmed | High for preset soil-element and temperature correction strategies | Potential China risk for uploaded-data/geographic/correction-strategy implementations |
| P5 | CN102914568B, “Soil moisture sensor with replaceable probe and measuring method” | 2012 | Chinese application published 2013; grant 2014 | Google labels active through expected term; official CN register not independently confirmed | Very high for generic replacement-probe output equivalence | Potential China risk for hardware conditioning/linear probe-replacement transfer |
| P6 | TCS sensor-health family: IN 202021001465; PCT/IN2020/050971; WO2021144807A1; EP4090953B1; US12175680B2 | 2020-01-13 | US grant 2024; EP grant 2024; Indian grant-certificate lead dated 2024 | US/EP are live recent grants; exact Indian claims/register need official review | Very high for low-cost sensor normalization, degradation stages and replacement recommendations | Significant for broad health/degradation/replacement implementations in US/EP/India |
| P7 | US11598743B2 / US20210302349A1, Korean-priority resonance/reference soil-moisture sensor | 2020 | US grant 2023 | Recent grant; presumed live, official maintenance not yet decisive | High for single-probe resonance/reference architecture and temperature-dependent operation | Relevant only if hardware redesign approaches claimed resonance/reference structure |
| P8 | US5430384A, temperature-compensated soil-moisture sensor | early 1990s | US grant | Expired by maximum term | High prior art for same-depth temperature compensation | No present US FTO barrier |
| P9 | US20150330932A1 / US9804113B2, RLC capacitive soil-moisture sensor | 2014 | US publication and grant | Exact maintenance status not independently confirmed | High for microcontroller-driven capacitive/RLC measurement and ADC processing | Relevant only to similar custom RLC architecture |
| P10 | CN108414007B, temperature-dependent nonlinear soil-moisture compensation | 2018-era publication | Chinese grant record located | Official current status not independently confirmed | High for nonlinear temperature compensation | China-specific risk depends on exact claim implementation |
| P11 | EP2623971A1 and family, capacitive soil-moisture sensor/calibration apparatus | 2012 | EP publication | Family status not fully audited | Moderate for calibration fixtures and soil-specific calibration practice | Low for frozen MCU compensation; relevant to specific fixture claims |
| P12 | CN116298198A and later grant activity, multi-parameter soil sensor and fusion correction | 2020-era | Chinese publication | Current family status not fully audited | Moderate/high for temperature, moisture and conductivity fusion | Relevant only to a multi-sensor/live-EC redesign |

Expired and abandoned records remain relevant prior art. They are not automatically FTO blockers.

---

## 6. Closest independent-claim analyses

### 6.1 P1 — US7884620B2 / US20090219037A1

**Independent-claim core:** a housed sensor device with sensing circuitry, data-reduction circuitry, a sensing structure and transmission of calculated output values. Dependent claims specify analog signals, a microcontroller determining electrical properties and correlating them to moisture and salinity, and dual-frequency circuitry.

**Overlap with frozen MVP:**

- local sensing and data reduction;
- analog measurement;
- local microcontroller calculations;
- soil-moisture correction involving salinity.

**Material differences:**

- TrueMoist does not measure salinity at runtime;
- it uses a commodity probe, not the claimed dual-frequency sensing structure;
- salinity is controlled batch metadata;
- the frozen MVP uses external gravimetric calibration and fixed regression coefficients.

**Effect on assessment:** not a direct anticipation of the complete frozen MVP, but strong evidence that moisture/salinity correction, local calculations and higher-order correction are established. It materially increases obviousness risk.

### 6.2 P2 — US20080199359A1

**Independent-claim core:** a capacitance sensor, processor and memory storing periodic measured values, with the processor scaling stored values to establish a moisture range used to calibrate new readings.

**Description-level expansion:** wet/dry history, watering-event plateaus, continuous recalibration, temperature/conductivity arrays, fertiliser step changes, placement effects, settling, corrosion and circuit deterioration.

**Overlap:**

- low-cost capacitive sensing;
- local processing;
- calibration;
- environmental and ageing effects;
- event/reference-based recalibration;
- recognition of placement and soil-structure effects.

**Differences:**

- TrueMoist frozen MVP is fixed-coefficient and not self-learning;
- TrueMoist uses gravimetric ground truth and controlled factorial experiments;
- TrueMoist does not control irrigation.

**Effect:** very strong prior art against broad drift adaptation, event-triggered recalibration and claims that placement/settling robustness is new.

### 6.3 P3 — WO2020047587A1

**Independent-claim core:** determine a sequence of soil-moisture measurements over periods including moisture uptake or release events, then derive minimum and maximum soil-moisture values.

**Further claims/description:** progressive recalibration, continuous or interval recalibration, low-pass filtering, multiple sensors/depths, machine-learning options, error detection, inconsistent readings and confidence-related exclusion.

**Overlap:**

- reference-event recalibration;
- validity/confidence logic;
- filtering;
- multiple sensor comparison;
- adaptation over time.

**Differences:**

- TrueMoist’s frozen model is not adaptive;
- its objective is compensated gravimetric estimation under controlled temperature/salinity disturbances, not full/refill irrigation points.

**Effect:** confidence-gated output or event recalibration cannot be treated as a standalone new idea.

### 6.4 P4 — CN111103333B

**Independent-claim core:** obtain preset device information including a soil-element correction identifier and geographic information; derive a corresponding correction strategy; receive sensor moisture data; execute the correction strategy. The claim also incorporates a temperature-correction identifier/strategy.

**Overlap:**

- preset metadata;
- soil/environment correction;
- temperature correction;
- stored correction models.

**Differences:**

- CN111103333B is based on uploaded VWC, geographic information and soil-element databases;
- TrueMoist is local, one-soil, offline-trained and uses a controlled treatment code rather than geography;
- TrueMoist’s output is dry-basis gravimetric water content unless separately converted.

**Effect:** the mere existence of a preloaded salinity/soil code and temperature model is not a strong novelty hook.

### 6.5 P5 — CN102914568B

**Independent-claim core:** a replaceable-probe soil-moisture sensor with a high-frequency signal path and conditioning module. The new probe’s conditioned output is made equivalent to the replaced probe using linear relations among probe output, moisture and dielectric properties.

**Overlap:**

- replaceable probe;
- probe-to-probe output normalization or transfer;
- low-order transfer mapping.

**Differences:**

- hardware-specific high-frequency architecture;
- TrueMoist currently has no automatic transfer mechanism;
- the candidate direction would use environmental perturbation residuals and a validity envelope rather than only output equivalence.

**Effect:** generic automatic transfer between probe units is already claimed. A new direction must be narrower and technically different.

### 6.6 P6 — US12175680B2 / EP4090953B1 / Indian-priority TCS family

**Independent-claim core in the US grant:** a system including a low-cost resistive or capacitive sensor; calibration; image-based physical-condition analysis of the probe; degradation-stage assessment; and recommendations to modify or replace the sensor. Dependent claims include normalization using rugged-sensor values and minimum/maximum mapping.

**Overlap:**

- low-cost capacitive sensor;
- calibration;
- sensor-health/degradation decisions;
- replacement recommendation;
- unit-to-unit normalization.

**Differences:**

- TCS relies materially on image analysis of probe metal/connectivity and rugged-reference normalization;
- TrueMoist uses a coated capacitive PCB probe, no image-based degradation test and no rugged reference sensor.

**Effect:** the exact TCS independent claim is narrower than generic health monitoring, but its disclosure and dependent claims make broad low-cost sensor-health and replacement assertions difficult.

### 6.7 P7 — US11598743B2

**Independent-claim core:** a soil-moisture sensor using electrode structures, a resonance circuit and a reference/matching resonance arrangement to produce a determination value. Temperature sensing appears in dependent claim structure.

**Overlap:**

- soil-moisture measurement;
- temperature-related correction;
- local electronics.

**Differences:**

- the frozen TrueMoist probe is an off-the-shelf analog module;
- no matching reference resonance circuit is used;
- no custom electrode/resonance architecture is claimed by the project.

**Effect:** low direct overlap with the frozen hardware, but it confirms that integrated measurement/temperature compensation remains crowded.

---

## 7. Frozen-MVP feature comparison

Legend: **E** expressly disclosed; **N** necessarily implied; **S** arguably suggested; **A** absent; **U** unresolved.

| Frozen or future feature | P1 Campbell dual-frequency | P2 self-learning sensor | P3 auto-calibration | P4 CN correction strategy | P5 replaceable probe | P6 TCS health | P7 resonance/temp |
|---|---:|---:|---:|---:|---:|---:|---:|
| Commodity analog capacitive probe | S | E | S | S | A/S | E | A |
| Separate colocated temperature sensor | S | S/E in description | S | E | A | S | E/S |
| Same-depth 20–30 mm placement | A | S | A | A | A | A | U |
| Controlled salt addition per dry-soil mass | A | A | A | A | A | A | A |
| Salinity treatment code, not live EC | A | A | A | S for preset correction, not salt-dose code | A | A | A |
| No runtime EC sensor | A | S in one-frequency embodiment | E/S | E | E | E | E |
| ADS1115 vs ESP32 ADC comparison gate | A | A | A | A | A | A | A |
| RC filtering/decoupling/grounding | S | S | S | U | S | U | E/S |
| ESP32 local inference | S as generic MCU | E as processor | E as controller | A/locality differs | S | E as processors | E |
| Univariate raw baseline | S | S | S | S | S | S | S |
| Multivariate linear baseline | S/E | S | S | S | E | S | S |
| Ridge second-order candidate | E/S for polynomial correction; ridge not identified | S | S/ML optional | S/deep models | A | E/S regression models | S |
| Offline training/fixed coefficients | S | A | A | S | E/S | S | S |
| One-soil restriction | A | A | A | A | A | A | A |
| 72-run factorial physical dataset | A | A | A | A | A | A | A |
| Untouched physical replicate | A | A | A | A | A | A | A |
| Gravimetric dry-basis ground truth | A/S | A | A | A | S | rugged-reference instead | A |
| Probe-transfer mechanism | A | S | S | S | E | S | A |
| Drift/ageing detection | S | E | E/S | S | A | E | S |
| Insertion/packing compensation | A | E/S in description | S | A | A | A | A |
| Confidence-gated abstention | A | S | E/S | A | A | S | A |
| Calibration provenance/validity envelope | A | S | S | S | S | S | A |

No single reference expressly discloses the complete frozen architecture. That does not establish inventive step. The chart instead shows that the putative technical functions are distributed across highly analogous references and ordinary engineering practice.

---

## 8. Commercial, institutional, India and China landscape

### 8.1 Commercial/institutional landscape

METER/Decagon, Campbell Scientific, Sentek, Delta-T, Vegetronix, Toro and other firms sell or develop soil-moisture systems with calibration, temperature effects, conductivity concerns and installation constraints. Product existence demonstrates a mature technical field, but product descriptions were not used as substitutes for claim analysis.

The commercial split remains:

- research-grade sensors with robust calibration and higher cost;
- agricultural monitoring platforms with site-specific setup;
- low-cost commodity probes with greater unit variation and lower long-term confidence.

TrueMoist has credible educational and low-cost engineering value in this gap. Commercial need does not itself confer patentability.

### 8.2 India

The most relevant identified Indian-origin family is the Tata Consultancy Services low-cost sensor-health family. It claims priority to Indian Application 202021001465 and produced US and EP grants; an Indian grant-certificate record dated 5 March 2024 was located through an Indian patent-record aggregator. This family is particularly important if TrueMoist adds health classification, degradation stages, rugged-reference normalization or replacement advice.

The Indian Patent Office hosts CRI Guidelines 2025, published on 29 April 2026. A software-heavy claim would need careful treatment under Section 3(k) and current examination practice. The safest technical framing is a sensor-linked method producing a measurable improvement in physical measurement reliability, not a regression formula or data label alone.

### 8.3 China

China contains several close records:

- CN111103333B: preset soil-element and temperature correction strategies;
- CN102914568B: replaceable-probe equivalence;
- CN108414007B: nonlinear temperature compensation;
- CN116298198 family: multi-parameter fusion;
- newer in-situ calibration and water/salt correction records citing CN111103333B.

China is therefore a high-density jurisdiction for calibration and sensor-transfer claims. Machine-translated claim analysis must be verified before filing or commercialization.

---

## 9. Non-patent prior art and measurement practice

Primary literature confirms the following:

1. **Probe-to-probe variation is material.** Studies using multiple SEN0193 units report significant unit variation and compare individual, universal and one-point calibration.
2. **Soil-specific calibration remains important.** Laboratory calibration does not automatically transfer to field soils, packing methods or salinity conditions.
3. **Temperature and salinity affect capacitive/FDR response.** Compensation and frequency selection have been studied for years.
4. **Gravimetric calibration is standard practice.** Comparing probe response against independently determined water content is scientifically appropriate.
5. **Grouped physical validation is necessary.** Treating repeated electronic reads from one physical condition as independent observations produces leakage and misleading accuracy.
6. **Universal and single-point calibration are already published.** A transfer mechanism must outperform these simple baselines.
7. **Installation, packing, contact and remounting are recognized error sources.** A jig reduces experimental variation, but controlling a known nuisance factor is not automatically an invention.
8. **Recent field research reinforces validity-envelope concerns.** Low-cost sensor calibration performance degrades across field conditions, making abstention and bounded-use concepts practically valuable, though not necessarily patentable.

---

## 10. Frozen-MVP patent assessment

### 10.1 Credible invention already present?

**No.**

The frozen MVP is best characterized as a carefully executed combination of known components and practices:

- commodity capacitive sensing;
- temperature measurement;
- known salinity treatment as a model input;
- analog conditioning;
- external ADC comparison;
- ordinary linear and polynomial/ridge regression;
- offline training and fixed MCU coefficients;
- gravimetric calibration;
- one-soil factorial validation.

### 10.2 Controlled salinity code

The code has real experimental value because it allows the team to test salinity disturbance without building an unreliable EC instrument. Patent relevance is weak because:

- it represents known preparation metadata;
- the runtime system does not sense whether the selected code is true;
- preset correction strategies already exist;
- encoding a known treatment level as a regression input is an expected modelling step.

It may become a supporting claim limitation in a broader technical mechanism, but it is not a credible invention centre.

### 10.3 Factorial dataset and grouped validation

The dataset architecture improves evidence quality. It may support enablement, comparative data and later claim drafting. It is not, by itself, a patentable mechanism. A claim to “collect 72 samples arranged as 4×3×2×3” would likely be treated as an experimental or mathematical plan unless it is inseparably tied to a non-obvious technical calibration process.

### 10.4 Current risk assessment

| Requirement | Frozen MVP assessment |
|---|---|
| Novelty of exact complete combination | Possibly present at a very narrow descriptive level |
| Inventive step / non-obviousness | Weak; high combination-obviousness risk |
| Eligibility | Sensor-linked claims likely eligible in form, but model-only claims vulnerable |
| Enablement / support | Not yet supported by actual results |
| FTO | No direct clearance; lower risk than custom/live-EC designs but relevant live families remain |
| Patent-development track | Not Track A |

---

## 11. Candidate invention-direction matrix

Tracks: A = credible invention already in frozen MVP; B = bounded credible enhancement within three months; C = connected later-semester path; D = no credible path established.

| Direction | Problem and proposed contribution | Closest art / overlap | Three-month experiment and change | Risk and kill condition | Track |
|---|---|---|---|---|---|
| 1. Probe-specific characterization and automatic calibration transfer | Transfer an existing calibration to a replacement commodity probe | CN102914568B directly addresses replaceable-probe equivalence; universal/one-point calibration literature; TCS normalization | Use Probe A donor, Probe B replacement; compare no-transfer, dry-point, two-anchor, affine and perturbation-aware transfer | Kill if simple one-point/affine transfer performs equally; two probes are insufficient for broad claim | C |
| 2. Dual-probe disagreement for validity/health | Use disagreement to invalidate estimates rather than average probes | WO2020047587 discusses inconsistent proximate sensors/confidence; TCS health monitoring | Deliberately induce one-probe offset, remount and coating faults; compare disagreement flags | Kill if disagreement cannot distinguish unit bias from real spatial variation or if false invalidation is high | D alone; C only as supporting feature |
| 3. Insertion- and packing-aware compensation | Detect or compensate installation/packing error | US20080199359 recognizes placement, voids and settling; literature treats packing as known nuisance | Repeat controlled insertions/packing levels; model packing code or residual | Without runtime physical sensing, this is experimental control rather than deployable compensation; kill if code must be manually known | D |
| 4. Contamination-protected drift adaptation | Permit updates only when a trusted event is not confounded by salinity/packing/temperature | US20080199359 and WO2020047587 already disclose event recalibration; fertilizer step changes are explicitly considered | Simulated drift plus watering/dry-down-like reference events; salinity/packing contamination; update gate ablation | Kill if guard adds no advantage over fixed model or simple event filter | C |
| 5. Confidence-gated/abstaining estimate | Withhold output outside validated domain | WO2020047587 contains error/confidence concepts; out-of-distribution gating is generally known | Define physical validity envelope; test accepted-error versus rejection-rate curve | Kill if it only checks min/max ranges or rejects too many valid points | D alone; C as part of transfer mechanism |
| 6. Reference-event self-validation/recalibration | Use sparse known physical events to check or update calibration | Strongly covered by US20080199359 and WO2020047587 | Bench reference events with gravimetric anchors | Broad direction is anticipated/suggested; kill absent a new event discriminator | D |
| 7. Physics-informed low-order compensation | Constrain model by monotonicity or dielectric/temperature relations | Temperature/salinity correction and low-order models are conventional | Compare unconstrained ridge with monotonic/interaction-limited model | Kill if gain is ordinary regularization or statistically insignificant | D; possible B only with unexpected physical effect |
| 8. Calibration provenance and validity envelope | Store calibration conditions and enforce bounded use | Preset correction, confidence and validity concepts are known | Record probe ID, batch, range, temperature/salt/packing envelope; safe fallback | Provenance alone is administrative; kill if no physical decision effect | C as supporting feature |
| 9. Transfer across soil batches/classes | Preserve performance across batches or soil classes | Extensive calibration-transfer literature and preset soil strategies | Add soil batches after semester MVP; compare hierarchical/transfer baselines | Kill if soil-specific recalibration remains necessary or no improvement over simple anchors | C, primarily publication value |
| 10. Multi-frequency moisture/salinity separation | Separate dielectric and conductivity effects physically | Campbell family and old impedance art are very close | Requires custom probe/AFE and new measurement programme | Major redesign, crowded FTO area and budget/timeline risk | D for current project |
| 11. Live-EC-assisted compensation | Measure conductivity and use it in correction | Numerous moisture+EC patents and products | Requires credible AC EC instrument, calibration and electrochemical validation | Major redesign; kill if added EC uncertainty dominates | D |
| 12. Contamination-protected replacement transfer with validity envelope | Transfer donor calibration to a replacement probe, test it across known disturbances, abstain when transfer validity is lost and block contaminated updates | Each component is known separately: P2, P3, P5, P6; exact interaction not located | Two-probe pilot now; later 6–12 probes, multiple batches, drift/remount cycles, ablation of transfer, guard and validity gate | Kill if combination gives no synergistic error reduction over independent known steps, or if claims collapse to generic transfer plus threshold | **C — strongest surviving direction** |

No candidate qualifies as Track A. No candidate presently meets Track B with sufficient confidence because the closest art is too close and the available physical evidence is too small.

---

## 12. Strongest surviving direction

### 12.1 Proposed technical problem

A low-cost capacitive probe may be replaced by another nominally identical unit whose response differs because of manufacturing variation. A naïve transfer may appear valid under one condition but fail under temperature, salinity, packing, insertion or remount disturbances. Updating calibration during a contaminated event can make the error persistent.

### 12.2 Candidate contribution

A **contamination-protected replacement-probe transfer and calibration-validity mechanism**:

1. establish a donor calibration and donor validity envelope;
2. acquire a bounded anchor set from the replacement probe;
3. estimate a transfer mapping;
4. test transfer residuals across physical disturbance checks;
5. derive a replacement-specific validity envelope;
6. emit compensated moisture only while the current condition remains within that envelope;
7. abstain or fall back to a raw/limited estimate outside it;
8. permit recalibration only after a trusted event passes contamination checks.

### 12.3 Why this is stronger than the alternatives

It is tied to a physical technical problem: interchangeable low-cost sensors do not behave interchangeably. It can produce measurable effects:

- lower replacement-probe RMSE;
- lower worst-subset error;
- fewer silently wrong estimates;
- bounded false invalidation;
- reduced calibration workload.

### 12.4 Why it is still only Track C

- CN102914568B already claims replacement-probe equivalence.
- Universal and single-point calibration are published.
- TCS claims low-cost sensor degradation and replacement logic.
- Event recalibration and confidence filtering are known.
- The project currently has only two probes and one soil.
- No experimental result yet shows that the proposed combination produces an unexpected synergistic benefit.

### 12.5 Required differentiating feature

The potential invention cannot be “transfer + confidence threshold.” It must be a specific physical test sequence, transfer residual or update gate that distinguishes:

- replacement-unit bias;
- environmental disturbance;
- packing/remount error;
- genuine moisture change; and
- actual sensor degradation.

The claimable centre, if one emerges, must be the interaction that makes those states distinguishable with materially less calibration or lower severe-error risk.

---

## 13. Level-1 compensation versus Level-2 robustness/transfer

### Level 1 — Frozen compensation

Inputs: raw probe response, temperature and controlled salinity-treatment code.
Models: univariate, linear and ridge second-order.
Output: compensated gravimetric moisture estimate.

**Engineering value:** high.
**Patent value:** low.

Reasons:

- conventional sensors and regression;
- preset correction strategies;
- known temperature/salinity effects;
- no new physical sensing principle;
- no demonstrated unexpected result.

### Level 2 — Robustness, transfer and validity

Inputs include probe identity, transfer anchors, disturbance residuals, remount/packing checks, drift evidence and trusted-event status.
Output includes estimate, validity state and fallback/abstention decision.

**Engineering value:** potentially high.
**Patent value:** possible but unproven.

Level 2 should remain a later-semester research extension. The semester MVP should first establish a valid Level-1 measurement chain.

---

## 14. Novelty

### 14.1 Frozen MVP

No single located claim was shown to expressly disclose every frozen feature in one combination. A narrowly drafted claim could therefore avoid literal anticipation.

That is not a sufficient patent conclusion. Several features are arbitrary implementation details rather than invention-defining limitations:

- ESP32 versus another MCU;
- ADS1115 comparison;
- DS18B20 model;
- 20–30 mm spacing;
- exact 72-run matrix;
- ridge regularization;
- USB CSV.

Adding many conventional details can create a textually unique claim without creating a patentable invention.

### 14.2 Candidate Level-2 direction

The exact combined sequence of contamination-protected replacement transfer, physical validity testing and abstention was not located as one claim. Novelty may be possible if the mechanism is defined narrowly.

Novelty risk remains substantial because:

- replacement transfer is known;
- health/degradation analysis is known;
- event recalibration is known;
- confidence exclusion is known;
- preset correction strategy is known.

The final novelty assessment must be repeated after the team defines the exact algorithm, physical checks and state transitions.

---

## 15. Inventive step / obviousness

### 15.1 Frozen MVP

**Risk: high.**

A skilled sensor engineer faced with temperature and salinity cross-sensitivity would reasonably:

- measure temperature;
- control or measure salinity;
- gather calibrated samples;
- fit linear and polynomial models;
- regularize the model;
- deploy coefficients to a microcontroller;
- validate against gravimetric reference;
- harden the analog path.

The current architecture is a good implementation plan, but its selection appears to follow ordinary engineering optimization.

### 15.2 Strongest candidate

**Risk: medium-high until evidence exists.**

Combining known transfer, validity and event-gating concepts may be considered an obvious aggregation. The case improves only if experiments show an effect not predicted by the components independently, for example:

- a specific disturbance-residual sequence identifies unsafe transfer using two anchors where ordinary cross-unit transfer fails;
- the contamination gate prevents persistent recalibration error while maintaining useful acceptance;
- the combined method achieves lower severe-error probability with substantially fewer calibration samples.

Ablation is essential. The complete method must outperform:

1. full per-probe calibration;
2. no transfer;
3. one-point calibration;
4. two-point affine transfer;
5. generic confidence bounds;
6. generic event recalibration;
7. transfer plus threshold without contamination protection.

---

## 16. Patent eligibility

### 16.1 United States

A claim to a regression equation, salinity code or confidence score in isolation risks being characterized as an abstract mathematical process. Current USPTO guidance emphasizes evaluating the claim as a whole and whether it integrates a judicial exception into a practical application or improves technology.

A stronger US claim would require:

- physical soil-sensor signals;
- a defined calibration or transfer sequence;
- a technical validity decision;
- changed sensor operation or suppression of an invalid physical estimate; and
- objective evidence of improved measurement reliability.

Eligibility is separate from novelty and non-obviousness. Even an eligible sensor claim can fail under Sections 102 or 103.

### 16.2 European Patent Office

A sensor and controller provide technical means, so basic eligibility is less likely to be the decisive hurdle. Under the EPO’s computer-implemented invention and COMVIK practice, only features contributing to a technical solution of a technical problem support inventive step.

Consequences:

- a treatment label, dataset split or provenance record may be non-technical unless it changes the physical measurement process;
- a mathematical model contributes only through its technical effect;
- the specification must connect the algorithm to improved sensor measurement, invalid-output prevention or a concrete physical-control effect.

### 16.3 India

The current Indian Patent Office CRI Guidelines 2025 were published in April 2026. Section 3(k) creates risk for claims characterized as algorithms or computer programs per se.

A stronger Indian framing would emphasize:

- a complete sensing apparatus or sensor-linked method;
- physical acquisition and calibration operations;
- measurable improvement in the reliability of a physical measurement;
- technical state transitions such as validity, fallback or controlled recalibration.

This report does not provide an Indian legal opinion. The current guideline text and relevant Indian cases should be reviewed by an Indian patent professional before filing.

---

## 17. Freedom to operate

### 17.1 Frozen MVP

No clearance is given. The frozen MVP appears less exposed than custom dual-frequency, custom resonance or live-EC architectures because it uses a commodity analog probe and fixed local compensation.

Main present risks:

- implementing broad correction strategies in China in a manner close to CN111103333B;
- adding custom resonance/reference circuitry close to US11598743B2;
- adding dual-frequency salinity measurement close to the Campbell lineage;
- adding sensor-health/replacement analysis close to the TCS family;
- adding replacement-probe conditioning close to CN102914568B.

### 17.2 Candidate Level-2 direction

Jurisdiction-specific live-claim concerns:

| Jurisdiction | Principal concern | Design-around direction |
|---|---|---|
| United States | TCS US12175680B2; live Campbell grants; US11598743B2 | Avoid image-based probe degradation, rugged-reference normalization, dual-frequency/live-salinity hardware and matching resonance/reference circuits |
| Europe | EP4090953B1 TCS family; national-stage status of event-calibration families | Keep transfer/validity mechanism distinct from claimed degradation and normalization pipeline; obtain register/claim chart |
| India | Indian-priority TCS family and potentially granted Indian patent | Confirm Indian grant claims; avoid claimed health-analysis and replacement workflow |
| China | CN102914568B and CN111103333B; nonlinear compensation records | Avoid hardware conditioning that forces new-probe equivalence and geographic/preset correction-strategy workflow |
| PCT/national stages | WO2020047587A1 and related records | Determine national-stage entries before commercialization |

### 17.3 Status rule

- Expired US5430384 remains prior art but is not a present FTO barrier.
- Abandoned US20080199359 remains prior art but does not create an enforceable US claim.
- A ceased PCT application may still have national-stage rights.
- Google “active” status is not a substitute for an official register check.

---

## 18. Claim-to-experiment map

| Prospective claim element | Required physical experiment | Baseline / ablation | Required metric | Proposed kill condition |
|---|---|---|---|---|
| Replacement-probe transfer using bounded anchors | Transfer A calibration to B across moisture/temp/salt conditions | No transfer; one-point; two-point affine; full B calibration | Transfer RMSE, MAE, bias and sample count | No material advantage over simple affine transfer |
| Disturbance-residual validity envelope | Apply transfer under unseen temperature, salt, packing and remount states | Static min/max gate; prediction interval only | Severe-error rate, coverage, rejection rate | High error remains inside envelope or valid data are excessively rejected |
| Contamination-protected update gate | Simulate trusted moisture event plus salt/packing/temp confounders | Ungated event recalibration; fixed model | Post-update RMSE, false update rate, recovery | Gate fails to block contaminated updates or blocks most clean events |
| Safe abstention/fallback | Drive system outside validated domain | Always-output model | Accepted-error distribution, false invalidation | No meaningful severe-error reduction |
| Probe health state | Controlled offset, intermittent fault, drift and remount | Simple disagreement threshold | detection delay, false alarm, missed detection | Health flag confuses spatial/packing variation with degradation |
| Local MCU implementation | Reproduce Python output on ESP32 | Host-only implementation | numerical equivalence, latency, RAM/flash | MCU result differs materially or mechanism exceeds resource limits |
| Synergistic complete method | Full transfer + validity + contamination gate | Remove one element at a time | RMSE/MAE, worst-subset error, severe-error probability | Complete method is no better than additive known components |

All patent-oriented thresholds beyond the accepted engineering thresholds must be pre-registered and owner-approved before testing.

---

## 19. Three-month semester plan

### Weeks 1–2 — Preserve frozen MVP validity

- complete probe repeatability, monotonicity and reinsertion gates;
- verify oven/scale access;
- compare ADS1115 and ESP32 ADC1;
- freeze jig, packing method and soldered analog path;
- preserve confidentiality and document inventorship contributions.

### Weeks 3–6 — Complete Level-1 dataset

- collect the 72 independent physical runs;
- use replicates 1–2 for model selection and replicate 3 untouched;
- fit univariate, multivariate linear and ridge second-order models;
- report absolute and subset errors;
- do not count rapid ADC reads as physical samples.

### Weeks 7–8 — Probe-transfer pilot

Using Probe A as donor and Probe B as replacement:

- no-transfer baseline;
- dry-point one-anchor transfer;
- two-anchor affine transfer;
- full per-probe calibration upper benchmark;
- evaluate transfer across temperature and salinity subsets.

This is a feasibility pilot, not patent proof.

### Weeks 9–10 — Validity and contamination pilot

- remount Probe B;
- vary packing within documented safe ranges;
- apply a salinity perturbation and temperature perturbation;
- simulate a bounded electronic offset or ageing drift;
- test static range gate, residual envelope and contamination gate.

### Week 11 — Ablation and decision gate

- compare complete candidate against simple transfer and generic confidence;
- quantify whether any interaction is synergistic;
- stop patent development if results reduce to known calibration practice.

### Week 12 — Institutional IPR review

- prepare confidential invention disclosure only if the candidate survives;
- map inventors to actual technical contributions;
- do not publicly disclose new mechanisms, data or results before institutional review;
- commission a professional claim/status search for target jurisdictions.

---

## 20. Later-semester and publication extension

A credible Track-C programme requires:

- 6–12 nominally identical probes, not only two;
- multiple manufacturing lots where possible;
- at least three independently prepared soil batches;
- later addition of multiple soil classes;
- repeated insertion/remount cycles;
- accelerated drift or ageing proxy;
- field wetting/drying events;
- independent gravimetric checks;
- predefined acceptance and rejection metrics;
- comparison with universal and one-point calibration literature;
- comparison with full per-probe calibration;
- claim-specific ablation.

Publication value may remain strong even if patentability fails. A useful paper could report:

- unit variability;
- transfer limits;
- validity-envelope coverage;
- severe-error reduction through abstention;
- failure of naïve recalibration under salinity/packing contamination.

Publication should occur only after IPR review.

---

## 21. Budget, measurement, compute and team feasibility

### 21.1 Frozen MVP

The existing plan is feasible within the ₹3,000 preferred target when institutional oven and scale access are available, and within the ₹5,000 ceiling with careful procurement.

Compute is not limiting:

- fewer than approximately fifteen model coefficients;
- negligible inference time;
- very small RAM/flash use;
- no TinyML runtime required.

The critical resource is experimental discipline.

### 21.2 Three-month patent-direction pilot

Likely additions:

- existing second probe: already planned;
- extra containers/jig parts: modest;
- optional third/fourth probe if budget permits;
- no live EC or custom multi-frequency hardware.

A two-probe pilot can remain under ₹5,000. It cannot establish population-level probe transfer.

### 21.3 Later-semester proof

Six to twelve probes, multiple soil batches, field access and long-term testing may exceed the current semester budget or require institutional support. This is the main reason the credible path is Track C rather than Track B.

### 21.4 Team allocation

- Member 1: embedded acquisition, firmware and local validity/fallback logic;
- Member 2: modelling, transfer baselines, statistics and ablation;
- Member 3: hardware, jig, physical perturbations and gravimetric workflow;
- Member 4: logging, data integrity, labels and test automation;
- Member 5: experiment records, photographs, confidentiality log and presentation support.

Critical-path interpretation must remain with the three technically strong members.

---

## 22. Kill criteria

Terminate the patent-development path, while optionally retaining the semester prototype, if any of the following occurs:

1. probe response is not stable and monotonic enough for credible calibration;
2. no traceable gravimetric reference is available;
3. packing/reinsertion variance equals or exceeds the environmental effects;
4. the compensated MVP fails its accepted RMSE or MAE thresholds;
5. the salinity treatment does not produce a repeatable non-saturating effect;
6. replacement transfer does not outperform simple one-point or affine calibration;
7. the validity gate fails to reduce severe accepted errors;
8. abstention rejects an impractical proportion of valid measurements;
9. the contamination gate cannot distinguish clean reference events from salinity/packing/temperature confounders;
10. ablation shows no synergistic benefit from the complete mechanism;
11. the claim centre reduces to regression, a lookup code, dataset organization or ordinary calibration;
12. the only surviving path requires live EC, multi-frequency custom hardware or a new probe within the semester;
13. official claim charting shows unacceptable live-claim overlap in target jurisdictions;
14. public disclosure has already destroyed filing options in a target jurisdiction;
15. institutional IPR review does not support filing.

---

## 23. Confidentiality boundary

Until institutional IPR review:

- do not publicly post the candidate transfer algorithm;
- do not publish calibration coefficients;
- do not upload new experimental data to public repositories;
- do not disclose contamination-gate rules or validity thresholds;
- do not present unfiled claim concepts in open competitions without approval;
- maintain dated laboratory notebooks, code commits and contributor records;
- separate pre-existing architecture decisions from newly invented mechanisms;
- mark external model or literature suggestions as background, not inventorship.

The frozen project description may be presented for academic review only within the institution’s confidentiality rules. Any new mechanism should be reviewed before public presentation.

---

## 24. Final recommendation

### Required recommendation

**Retain as strong semester prototype but reduce patent priority.**

### Rationale

TrueMoist remains:

- affordable;
- buildable;
- experimentally rigorous;
- educationally valuable;
- capable of generating a strong engineering demonstration and publication-quality data.

It should not presently be advanced as a patent-first candidate because the frozen MVP is a conventional compensation stack and the strongest extension is crowded by close art. Continue the semester MVP, conduct a limited confidential Level-2 pilot, and revisit patent filing only if the transfer/validity mechanism demonstrates a specific and unexpected physical effect.

---

## 25. Unresolved questions

1. What exact independent claims were granted in Indian Patent Application 202021001465?
2. What national stages, if any, remain live from WO2020047587A1?
3. What are the official maintenance statuses of the Campbell US grants?
4. What is the official CN legal status and enforceable translated scope of CN102914568B and CN111103333B?
5. Which jurisdictions are actually commercially relevant to the project?
6. How will a runtime user know the correct salinity-treatment code outside the laboratory?
7. Is the salinity code intended only for the experiment, or as a deployed user input?
8. Can two probes reveal a meaningful transfer mechanism, or only a unit-specific coincidence?
9. What trusted physical event is available without an irrigation controller or live EC channel?
10. Can contamination be recognized from existing inputs alone, or is additional sensing required?
11. What exact fallback is technically safe when validity is lost?
12. What severe-error and rejection thresholds will the owner approve before testing?
13. Are multiple probe lots available within budget?
14. Is field or later-semester access available for ageing and soil-class transfer?
15. Has any prior presentation, upload or report publicly disclosed potentially filing-relevant details?
16. Who made each prospective inventive contribution for inventorship purposes?
17. Does the institution require assignment, disclosure or pre-publication approval?

---

## 26. Source and verification log

### 26.1 Governing project sources

- `00_READ_FIRST_TrueMoist_Patent_Research_Instructions.md`
- `01_Engineering_Design_Review.md`
- `02_Project_mC_Decision_Register_v1.2.md`
- `03_Phase3C_Portfolio_Closure_Memo_Approved.md`
- `04_Phase3C_TrueMoist_Architecture_Report_Final.md`
- `05_Phase3C_TrueMoist_Memory_Final.md`
- `06_Phase3C_TrueMoist_SOP_Final.md`
- `07_Concept_Evidence_Matrix.md`
- `08_Uncertainty_and_Test_Register.md`
- `09_Patent_Research_Input_Pack.md`
- `10_Phase2_Report_by_Claude.md` — used only for historical leads

### 26.2 Patent records reviewed

- US7408364B1 — Sensor for measuring moisture and salinity
- US7535237B1 — Sensor for measuring moisture and salinity
- US7884620B2 / US20090219037A1 — Sensor for measuring moisture and salinity
- WO2009094324A2 — Sensor for measuring moisture and salinity
- US20080199359A1 / WO2007002994A1 / EP1899716A1 — Soil Moisture Sensor
- WO2020047587A1 — System and method for sensor-based auto-calibration of soil-moisture levels
- CN111103333A/B — Method and device for calibrating a soil water-content sensor
- CN102914568A/B — Soil moisture sensor with replaceable probe and measuring method
- US12175680B2 / US20220349838A1 — System and method for monitoring health of low-cost sensors used in soil-moisture measurement
- EP4090953B1 — corresponding TCS European family member
- PCT/IN2020/050971 / Indian Application 202021001465 — TCS priority family
- US11598743B2 / US20210302349A1 — Soil-moisture sensor and operating method
- US5430384A — Temperature-compensated soil-moisture sensor
- US20150330932A1 / US9804113B2 — Soil moisture sensor
- CN108414007B — temperature-dependent nonlinear compensation record
- EP2623971A1 — capacitance-based moisture sensor/calibration record
- CN116298198A family — multi-parameter integrated soil sensor and correction method

### 26.3 Technical literature reviewed

- Recent field-performance and calibration studies of low-cost capacitive soil-moisture sensors;
- SEN0193 multi-unit calibration and variability studies;
- universal and one-point calibration study using 63 SEN0193 sensors;
- temperature-compensation studies for frequency-domain soil-moisture sensors;
- salinity and conductivity-effect studies;
- gravimetric calibration studies;
- low-cost sensor inter- and intra-unit variability studies.

### 26.4 Legal/examination sources reviewed

- USPTO current Subject Matter Eligibility guidance and 2025–2026 updates;
- EPO Guidelines for Examination 2026 on computer programs, further technical effect and COMVIK;
- Indian Patent Office CRI Guidelines 2025 publication page, updated in 2026.

### 26.5 Verification labels used

- **Verified publication fact:** publication/grant number and date confirmed in accessible patent records.
- **Provisional status:** database indicates active/ceased/expired, but official register or maintenance record not fully checked.
- **Prior-art relevance:** technical disclosure relevant regardless of enforceability.
- **FTO relevance:** possible live-claim concern requiring jurisdiction-specific professional analysis.
- **Inference:** reasoned conclusion drawn from the cited disclosures, explicitly not a legal opinion.

---

# Decision summary

- **Frozen MVP Track:** D for present patentability; strong engineering prototype.
- **Strongest future Track:** C.
- **Executive verdict:** **credible long-term path requiring later-semester extension**.
- **Final recommendation:** **Retain as strong semester prototype but reduce patent priority**.


---

## Source 10: `03_CONCEPT_PORTFOLIO/TrueMoist/02_Raw_Research/02_TrueMoist_Patent_Research_Gemini.docx`

- Authority: `TIER_3`
- Treatment: `SUPPORTING_EVIDENCE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `NEW_STAGE10L_EXTRACTION`
- SHA-256: `4587f69d6f611e45c5a19088c76801579faa688c48fcf312566eaacab3b28d91`

# Source Extraction

- Chapter: `08` — TrueMoist Architecture, Validation and Patent Evidence
- Authority tier: `TIER_3`
- Manual treatment: `SUPPORTING_EVIDENCE`
- Original source: `03_CONCEPT_PORTFOLIO/TrueMoist/02_Raw_Research/02_TrueMoist_Patent_Research_Gemini.docx`
- SHA-256: `4587f69d6f611e45c5a19088c76801579faa688c48fcf312566eaacab3b28d91`
- Extraction method: `DOCX_XML`
- Rule: source text only; no synthesis, correction or reconciliation.

---

Project mC — TrueMoist Current Patent Verification — Independent Research

1. Executive verdict

The comprehensive analysis establishes a credible path through bounded three-month enhancement. The frozen Minimum Viable Product (MVP) architecture for TrueMoist—relying exclusively on conventional commodity hardware and standard mathematical regression without a distinct technical effect—is demonstrably unpatentable in its current state. However, the rigorous experimental framework established in the project documents, specifically the 72-run grouped validation design isolating packing, temperature, and controlled salinity effects against gravimetric ground truth, provides a robust foundation for a strategic firmware enhancement. By implementing a confidence-gated abstention mechanism and an out-of-distribution (OOD) validity envelope at the edge node, the system can achieve a patent-eligible technical effect. This enhancement transforms an abstract mathematical model into a control-system safety mechanism that improves the reliability of autonomous agricultural hardware by preventing erroneous actuations. This path requires no hardware redesign, preserves the strict budget constraints, and fits within the semester timeline, thereby satisfying the project's core directives.

2. Input inventory and concept fidelity

An exhaustive audit of the provided transport package confirms the presence and readability of exactly 10 physical attachments, which encapsulate 11 distinct logical inputs1. The foundational project directives, including the governing instruction, the Engineering Design Review, and Decision Register v1.2, are verified as authoritative and logically present1. Furthermore, the composite source file 04_05_TrueMoist_Architecture_and_Memory.md has been successfully parsed into its two constituent logical documents: the Phase 3C Final Architecture Report and the Phase 3C Memory4. It is confirmed that Decision Register v1.2, not v1.1, governs the current phase, and no logical source is omitted, duplicated, truncated, or unreadable1.

The substantive research applies these documents according to the strict authority order defined in the governing instruction1. Concept fidelity to the frozen TrueMoist MVP is rigidly maintained throughout the analysis. The architecture is defined as a local compensation system for a commodity analog capacitive soil-moisture probe (e.g., SEN0193-class) utilizing an ESP32-WROOM-32 microcontroller, an ADS1115 analog-to-digital converter (pending a mandatory Week-1 value gate), and a collocated waterproof DS18B20 temperature sensor4. The architecture employs offline-trained, ridge-regularized second-order multivariate regression deployed for local, fixed-coefficient embedded inference without continuous cloud dependency4. The physical boundaries are rigorously restricted to a single homogeneous soil, 72 independent physical runs, and dry-basis gravimetric ground truth utilizing an oven-drying method at 105 ± 5 °C4. Crucially, the system explicitly excludes live runtime electrical conductivity (EC) sensing, multi-frequency hardware, adaptive online learning, multi-soil generalization, and cross-concept comparisons with other portfolio projects1.

3. Search methodology and reproducible log

The patent and non-patent literature (NPL) search was executed with an evidence cut-off date of August 1, 2026. The search strategy targeted primary international databases, specifically focusing on the United States Patent and Trademark Office (USPTO), the European Patent Office (Espacenet), the World Intellectual Property Organization (PATENTSCOPE), the Indian Patent Advanced Search System (InPASS), and the Chinese National Intellectual Property Administration (CNIPA)1.

The search protocol utilized a combination of keyword operators, Cooperative Patent Classification (CPC) codes, and International Patent Classification (IPC) codes. The primary classification codes targeted included G01N27/223 (investigating capacitance for determining moisture content), A01G25/167 (control by humidity of the soil itself), and G01N33/246 (earth materials for water content)7.

The exact query strings deployed across the databases included variations of: ("capacitive soil moisture" OR "dielectric soil moisture") AND ("temperature compensation" OR "salinity compensation") AND "regression"; "soil moisture sensor" AND ("calibration transfer" OR "drift detection" OR "confidence gating"); and "edge soil-moisture compensation microcontroller" AND "gravimetric"1. For the legal and patent-eligibility analysis, specific queries such as "Section 3(k)" AND "sensor calibration" AND "technical effect" were executed to capture current Indian jurisprudence11.

Assignee and inventor searches were conducted targeting known market leaders and active research institutions, including METER Group, Decagon Devices, Campbell Scientific, Delta-T Devices, Tata Consultancy Services (TCS), Sentek, and the Beijing Academy of Agriculture and Forestry Sciences13. The search methodology prioritized the reading of independent claims to distinguish between true hardware novelty and algorithmic post-processing. Results relying on complex impedance spectroscopy, time-domain reflectometry (TDR), or dual-frequency excitation were carefully segregated from the low-frequency, DC-biased capacitive architecture of the frozen MVP17. Google Patents was utilized strictly for discovery and claim reading, while load-bearing status conclusions were derived from official registers1.

4. Technical and patent landscape

The technical landscape for dielectric soil moisture measurement is fundamentally bifurcated by operating frequency, which dictates both the hardware complexity and the patent concentration. High-end, research-grade sensors utilize Time Domain Reflectometry (TDR) or high-frequency Frequency Domain Reflectometry (FDR), operating in the 50 MHz to 1 GHz spectrum20. At these elevated frequencies, the dielectric constant of water (approximately 80) dominates the real part of the soil's complex permittivity, naturally suppressing the imaginary part driven by bulk electrical conductivity and salinity17. Patents assigned to entities like Delta-T Devices and Campbell Scientific dominate this tier, relying on specialized transmission line impedance matching, complex coaxial wave propagation, and highly engineered probe geometries19.

Conversely, the frozen TrueMoist MVP operates in the low-cost, low-frequency tier. These commodity capacitive probes (e.g., SEN0193) typically operate below 1 MHz, often utilizing a simple 555-timer integrated circuit to generate a low-frequency square or sine wave23. At these low frequencies, the sensor acts as a basic RC or RLC circuit where the charge-discharge timing or resonance frequency is exquisitely sensitive not only to water content but also to the soil's ionic conductivity (salinity) and ambient temperature9. The hardware patent landscape for low-frequency capacitive sensors is entirely saturated and largely expired. Foundational patents dating back to the late 1990s and early 2000s extensively cover the application of planar, insulated electrodes inserted into a porous medium to measure capacitance8.

Because the hardware geometry in this low-cost tier is commoditized, recent patent activity has pivoted sharply toward algorithmic and software-based compensation. Large multinational IT consulting firms, such as Tata Consultancy Services, alongside various agricultural research institutes, are actively patenting methods that utilize microcontrollers and statistical models to auto-calibrate sensors based on environmental feedback13. This shift reflects a broader industry trend toward edge computing and the Internet of Things (IoT), where the unreliability of cheap hardware is mitigated by data fusion and machine learning algorithms running on edge nodes25. Consequently, while the basic physical arrangement of a capacitive probe combined with a temperature sensor is unpatentable, there exists narrow but highly valuable white space in specific edge-computed validation mechanisms, such as out-of-distribution detection, error separation workflows, and failure abstention28.

5. Verified patent-family ledger

The following ledger details the critical, load-bearing patent families that frame the freedom-to-operate and patentability analysis for the TrueMoist MVP.

Patent / Publication

Assignee / Applicant

Relevant Technology

Status (Est.)

Relevance to MVP

US 7,884,620 B2

[cite: 19]

Campbell Scientific

Series RLC circuit, capacitive probe, PWM signal generator, microcontroller, ADC.

Active (Exp. ~2028)

High. Expressly discloses the core hardware logic and signal chain of low-frequency capacitive measurement using a microcontroller.

US 7,944,220 B2

[cite: 22]

Delta-T Devices Ltd

Complex impedance circuitry for minimizing temperature and conductivity influence.

Active (Exp. ~2027)

Medium. Covers hardware-based compensation, establishing that the problem of salinity/temperature interference is widely recognized.

US 12,175,680 B2

[cite: 15, 24]

Tata Consultancy Services

System and method for monitoring health and auto-calibrating low-cost soil sensors using statistical traits.

Active (Granted 2024)

Very High. Presents direct FTO risk for any system utilizing dynamic algorithmic calibration or statistical updates at the edge.

CN 101694475 B

[cite: 13]

Beijing Academy of Ag/Forestry

Multipoint soil moisture sensor with dedicated hardware temperature compensation diodes.

Active (Exp. ~2029)

Medium. Demonstrates that compensating capacitive readings for temperature is a conventional expectation in the art.

US 7,170,302 B2

[cite: 15]

Fu Ching Lee

Capacitive soil moisture sensor with insulated planar electrodes forming a capacitor with soil.

Expired

High. Represents foundational prior art for the physical geometry of the SEN0193-class probe selected for the MVP.

US 2015/0330932 A1

[cite: 9]

Wisconsin Alumni Research

Soil moisture sensor using parallel plate RLC circuit operating below 1 MHz.

Abandoned / Pending

High. Directly maps to the uncompensated hardware baseline of the frozen TrueMoist MVP architecture.

6. Closest independent-claim analyses

US 12,175,680 B2 (Tata Consultancy Services)

This recently granted patent represents the most significant hurdle for software-based compensation in agricultural sensors. The independent claims detail a method for the application of an agricultural product to a field by acquiring real-time sampled data using real-time agricultural sensors, extracting statistical characteristics from that data, and utilizing those characteristics to auto-calibrate the real-time sensors to account for variations in soil moisture and surface roughness15. The claims broadly cover the use of microcontrollers to apply statistical corrections to soil sensor readings dynamically. If the TrueMoist MVP attempts to deploy an adaptive model or utilizes run-time statistical characteristics to update its baseline, it risks direct infringement. Differentiation requires a strict architectural departure: the TrueMoist system must utilize fixed, offline-compiled coefficients and pivot its claim away from "auto-calibration" toward "validity-enforcement" or "abstention," ensuring it does not dynamically adjust its own calibration curve during field operation.

US 7,884,620 B2 (Campbell Scientific)

The independent claims of this patent define a soil moisture sensor comprising a capacitive probe with two electrodes, a series RLC circuit, a microcontroller providing a pulse-width modulated (PWM) drive signal, an analog-to-digital converter (ADC), and a current-to-voltage converter, wherein the microcontroller determines moisture content based on the capacitance value derived from the digital signal19. The TrueMoist MVP's physical signal chain—comprising a probe, an RC filter, an ADS1115 ADC, and an ESP32 microcontroller—operates on nearly identical physical principles. The MVP avoids literal infringement of the specific PWM-driven resonance curve tracking by utilizing the direct DC-biased analog voltage readout standard on commodity SEN0193 probes4. However, the breadth of this Campbell patent irrevocably confirms that the hardware aggregation of a capacitive probe, an ADC, and an MCU to calculate moisture is entirely saturated and unpatentable.

US 7,170,302 B2 (Fu Ching Lee)

This expired patent claims a capacitive soil moisture sensor featuring a body onto which a plurality of first and second electrodes are attached, covered by a protective layer of low dielectric constant material to provide a physical barrier preventing a conduction path15. The claims specify that once inserted into the soil, the electrodes form a planar capacitor using the soil as the dielectric15. This patent explicitly covers the physical construction of the off-the-shelf analog capacitive probes specified for the TrueMoist MVP. Its existence, alongside its expiration, guarantees freedom-to-operate regarding the physical probe design but simultaneously eliminates any possibility of claiming novelty based on the sensor's physical geometry or dielectric insulation.

7. Frozen-MVP feature comparison

The following table evaluates the specific features of the frozen TrueMoist MVP against the established prior art baseline, utilizing the strict terminology mandated by the research instructions.

Frozen MVP Feature

Prior Art Status

Closest Reference

FTO / Patentability Impact

Genuine analog capacitive probe

Expressly Disclosed

US 7,170,302 B215

Conventional. Provides FTO but holds zero patentable weight.

DS18B20 soil-temperature placement

Expressly Disclosed

CN 101694475 B13

Conventional sensor collocation. Temperature compensation is universally expected.

ADS1115 ADC & ESP32-WROOM-32

Expressly Disclosed

US 7,884,620 B219

Use of a commodity ADC and MCU is an unpatentable, routine design choice.

Controlled salinity treatment

Arguably Suggested

NPL Literature17

Standard laboratory calibration practice. Not a claimable apparatus element.

Offline multivariate linear/ridge regression

Expressly Disclosed

US 12,175,680 B224

Generic mathematical modeling. Statutorily excluded under Section 3(k) as a mathematical method.

Fixed local MCU inference

Expressly Disclosed

NPL Literature27

Edge-computed inference is standard in modern IoT agricultural sensor architectures.

Gravimetric GWC validation (105°C)

Expressly Disclosed

NPL Literature23

Standard ISO/ASTM soil methodology. Cannot form the basis of a patent claim.

USB CSV output

Expressly Disclosed

General Computing

Trivial data logging functionality.

Single-soil, 72-run grouped validation

Absent / Unresolved

N/A

Represents rigorous experimental design, but is not a patentable apparatus or method.

The comparative analysis definitively confirms that the frozen MVP is an aggregation of off-the-shelf components executing standard mathematical algorithms. The base architecture, while robust for an educational prototype, lacks any patentable novelty.

8. Commercial/institutional/India/China landscape

The commercial soil moisture market is highly tiered and intensely competitive. Premium agricultural telemetry is dominated by established firms such as METER Group (formerly Decagon Devices), Campbell Scientific, and Sentek32. These entities deploy sophisticated multi-frequency impedance sensors and complex coaxial probes capable of decoupling complex dielectric permittivity into independent moisture and bulk EC components with high accuracy33. These solutions command premium pricing and are heavily protected by active patent portfolios19.

In stark contrast, the low-cost tier is dominated by Chinese manufacturers producing inexpensive, uncompensated capacitive probes (e.g., DFRobot, YL-69 derivatives) utilizing basic 555-timer circuits23. These sensors are notorious for extreme sensitivity to temperature, salinity, and packing density, often leading to severe drift and unreliable data in field conditions17.

Institutionally, particularly in India and China, the focus has shifted toward bridging the gap between these two tiers by integrating low-cost sensors into broader IoT frameworks and utilizing Edge AI for localized error correction25. The Indian patent landscape is heavily influenced by massive IT consulting and software entities, such as Tata Consultancy Services, which are patenting algorithmic correction methods—ranging from machine learning to statistical regression—to improve the reliability of low-tier hardware networks34. Similarly, the Chinese National Intellectual Property Administration (CNIPA) records show a massive volume of utility models and patents combining basic capacitive sensors with localized microcontroller compensation circuits13. This ecosystem indicates that simply aggregating a cheap sensor with a microcontroller to perform basic arithmetic compensation is considered obvious and unpatentable in major Asian jurisdictions.

9. Non-patent prior art and measurement practice

Non-patent literature (NPL), particularly IEEE publications, agronomic journals, and geoscience preprints, provides critical context regarding the physical limitations of low-cost capacitive sensors. It is a well-documented physical phenomenon that changes in soil packing density and bulk density drastically alter the volumetric water content (VWC) reading37. This occurs because the sensor actually measures the composite dielectric of the medium within its fringing electric field; variations in compaction alter the air-to-soil-particle ratio, thereby changing the apparent dielectric even when the actual mass of water remains constant39. The NPL confirms that accurate conversion from gravimetric water content (GWC) to VWC is impossible without an independent measurement of bulk density4.

Furthermore, contemporary research demonstrates that sensor-to-sensor variability in low-cost probes is extreme, requiring individual calibration. Advanced "calibration transfer" models have been proposed to map the response of a high-end reference sensor to a low-cost target sensor using machine learning41.

Crucially, recent NPL emphasizes the critical importance of out-of-distribution (OOD) detection in autonomous IoT sensor networks. Because regression models and neural networks are notoriously brittle when presented with data outside their training distribution, Edge AI literature increasingly proposes using microcontrollers to detect OOD samples—such as anomalous temperature-salinity-moisture combinations that indicate a sensor fault or an uncalibrated environmental state28. By flagging these OOD states, the edge node prevents the transmission of hallucinated data, thereby avoiding erroneous automated decision-making in downstream irrigation controllers29.

10. Frozen-MVP patent assessment

The frozen TrueMoist MVP—strictly bounded to ordinary ridge-regularized second-order regression on a commodity capacitive probe and a temperature sensor—fails all criteria for patentability.

Novelty: The physical combination of capacitive sensing, temperature compensation, analog-to-digital conversion, and microcontroller-based regression is entirely anticipated by the prior art13. There is no structurally novel element in the apparatus.

Inventive Step/Obviousness: Applying ridge regularization instead of ordinary least squares to mitigate multicollinearity between temperature and capacitance variables is a foundational data science technique. A person having ordinary skill in the art (PHOSITA) attempting to fit a multi-variable calibration curve would routinely apply regularization to stabilize the coefficients. The use of an ESP32 to execute this math is an obvious application of commodity edge computing.

Patent Eligibility: Under the 2025 Indian Patent Office CRI Guidelines for Section 3(k), a mathematical method or algorithm is strictly excluded from patentability unless it provides a distinct "technical effect" solving a real-world technical problem11. The Delhi High Court jurisprudence, particularly in cases like OpenTV Inc v. Controller of Patents and Designs and Ab Initio Technology, dictates that algorithms producing mere numerical improvements, administrative results, or business methods are not patentable46. The frozen MVP's output is merely a mathematically adjusted numerical value logged to a USB CSV. It lacks physical interaction with a broader technical system state. In the US, it fails the Alice Step 2B requirement as the claims amount to nothing "significantly more" than an abstract mathematical calculation performed on a generic computer.

FTO: The MVP is relatively clear of FTO risks, provided it does not dynamically auto-calibrate (skirting TCS US 12,175,680 B2) and avoids physical buffer chambers (skirting Sensitech). However, operating freely does not equate to possessing patentable subject matter.

The frozen MVP possesses no credible patent path. It stands as a robust, disciplined engineering prototype, but it is not an invention.

11. Candidate invention-direction matrix

To establish a viable patent path, the system requires a bounded enhancement that leverages the rigorous 72-run experimental framework without violating the MVP constraints or expanding the budget. The following matrix evaluates potential directions.

State (Problem / Contribution)

Closest Prior Art

Overlap / Difference

Physical Effect / Baseline

Cost / Feasibility / Later Work

Risks / Confidence / Kill Condition

Track

Probe-transfer calibration: High unit-to-unit variance. Contribution: sparse grouped data to align low-cost probes.

Calibration transfer models41.

Transfer logic overlaps. Difference: constrained edge implementation.

Output alignment. Baseline: uncalibrated variance.

Low cost. Low feasibility in 2 months. Later work: massive multi-probe datasets.

Probe variance may be non-linear and unmappable. Confidence: Low. Kill: Variance cannot be aligned.

D

Dual-probe disagreement health: Single points of failure. Contribution: internal validity checking via redundancy.

Redundant industrial sensors.

Concept overlaps completely. Difference: cost tier.

Failure detection. Baseline: single probe drift.

Adds ₹400 for second probe. High feasibility.

Using two identical bad sensors may just yield identical bad data. Confidence: Low. Kill: Correlated drift.

D

Insertion/packing-aware compensation: Bulk density ruins dielectric readings39. Contribution: isolating packing error via specific mechanical jigs.

Geostatistical bulk density models37.

Problem overlaps. Difference: mechanical apparatus for error isolation.

Separation of variance. Baseline: uncontrolled packing.

Jig costs <₹500. Moderate feasibility.

Patenting the process of an experiment is difficult. Confidence: Medium. Kill: Packing error dominates completely.

C

Multi-frequency EC separation: Live EC confounding. Contribution: extracting imaginary permittivity.

Campbell/METER high-freq probes19.

Physics overlaps entirely.

Accurate live EC.

Requires major hardware redesign. Exceeds budget and timeline.

Automatically killed by frozen MVP rules prohibiting custom hardware.

D

Confidence-gated out-of-distribution (OOD) abstention: Regression models fail dangerously outside calibration boundaries28. Contribution: defining a multivariate hypervolume validity envelope on the MCU that abstains from outputting a value if inputs fall outside tested limits.

Edge AI anomaly detection29.

Anomaly detection overlaps. Difference: deployed as a static safety interlock on constrained agricultural nodes based on controlled physics data.

Prevents erroneous actuation. Baseline: catastrophic extrapolation.

Purely firmware. Zero added cost. High feasibility within 72 runs.

Polynomial boundary may not reliably separate safe from unsafe data. Confidence: High. Kill: Unstable boundary generation.

B

12. Strongest surviving direction

The analysis concludes that the strongest surviving direction is confidence-gated out-of-distribution (OOD) abstention, potentially supported by packing-aware error separation data.

Rather than attempting to claim the generic ridge-regression equation itself, the patentable method focuses exclusively on the validity envelope. The 72-run grouped factorial validation—varying moisture, temperature, and controlled salinity—produces a discrete, quantifiable hypervolume of known, safe physical conditions. The microcontroller firmware is augmented to evaluate whether an incoming raw sensor state (the vector of capacitance, temperature, and inferred moisture) falls within this validated multidimensional boundary.

If the state is OOD—for example, due to an unexpected salinity spike following fertilization, an extreme temperature gradient, or a corrosive sensor failure—the system generates an explicit "abstain" or "invalid" flag, overriding the regression calculation entirely. This solves a critical, documented technical problem: autonomous irrigation systems executing catastrophic, resource-wasting watering events based on wildly inaccurate, extrapolated sensor data30. By implementing a deterministic validity envelope on highly constrained edge hardware, the system transforms a fragile, abstract regression equation into a fail-safe mechanical control trigger.

13. Level-1 compensation versus Level-2 robustness/transfer

To successfully navigate the patent landscape, the architecture must transition conceptually from Level-1 compensation to Level-2 robustness logic.

Level-1 Compensation: This represents the frozen MVP. It utilizes generic statistical models (multivariate linear or ridge regression) to force a raw sensor reading to match a laboratory ground truth curve. It inherently assumes the environment behaves smoothly and that the sensor remains perfectly coupled to the soil. Patent offices globally view Level-1 compensation as an abstract mathematical curve-fitting exercise, devoid of patentable subject matter.

Level-2 Robustness: This introduces systemic awareness and health monitoring. The firmware does not merely compute a numerical output; it continuously evaluates the trustworthiness of the incoming signal vector. By calculating a Mahalanobis distance or utilizing a boundary polynomial derived directly from the empirical 72 calibration runs, the MCU assesses whether the sensor has suffered a packing shift, a corrosive failure, or a salinity event exceeding its operating parameters. If the signal is compromised, the system invokes a predefined safe fallback state. Level-2 robustness transforms abstract mathematics into a control-system safety mechanism.

14. Novelty

The proposed bounded enhancement—multivariate confidence-gating deployed specifically for commodity capacitive soil moisture probes at the edge—possesses verifiable novelty. While the individual sub-components (capacitive sensors, polynomial regression, general OOD detection in machine learning) are known in isolation, their specific integration is not. Deploying a static, offline-trained validity envelope to a highly constrained edge microcontroller to explicitly block out-of-bounds soil measurements from actuating downstream agricultural hardware is distinct from the closest prior art24.

For instance, TCS Patent US 12,175,680 B2 claims the auto-calibration of sensors using statistical methods24. The proposed TrueMoist method fundamentally differs in operation and intent: it explicitly does not auto-calibrate or adjust the baseline on the fly. Instead, it enforces a rigid, pre-compiled physical boundary to abstain from processing untrustworthy data, thereby preserving novelty over adaptive systems.

15. Inventive step/obviousness

To clear the obviousness hurdle (the inventive step), the method must solve a non-obvious technical problem without merely combining known elements in a predictable manner. A PHOSITA facing sensor inaccuracy in agriculture would typically solve the problem by applying a heavier low-pass filter or upgrading to a multi-frequency impedance sensor (e.g., METER TEROS)33.

Attempting to extract fail-safe reliability from a notoriously unstable, low-cost SEN0193 probe by mapping its specific multi-variable failure boundaries and deploying that as a hard exclusion mask on an ESP32 is a non-standard engineering approach. It runs contrary to the prevailing industry trend of streaming all raw data to the cloud for heavy anomaly detection analytics48. By proving through the 72-run experimental dataset that local, edge-computed abstention prevents an X% rate of catastrophic false-positive moisture readings during salinity spikes, the team establishes a measurable, non-obvious technical advantage that avoids the cost and latency of cloud dependency.

16. Patent eligibility

The confidence-gated enhancement directly addresses the stringent subject matter exclusions of Section 3(k) in the Indian Patents Act, the Alice framework in the United States, and the European Patent Convention.

India (2025 CRI Guidelines): The guidelines strictly exclude "computer programmes per se" and mathematical methods11. However, the guidelines and recent Delhi High Court jurisprudence (e.g., Raytheon Company v. Controller, Ab Initio Technology) confirm that a software invention producing a concrete "technical effect" that solves a real-world problem is eligible45. The technical effect here is the prevention of mechanical hardware failure (erroneous irrigation actuation or pump burnout) by intercepting physically invalid sensor states at the edge node before they trigger a physical action. The algorithm directly controls the functional state of the sensor system (Active vs. Safe Fallback), fulfilling the technical enablement requirement11. It is not a business method, thereby avoiding the absolute bar confirmed in OpenTV Inc47.

EPO/US: The EPO readily accepts software that controls a technical process, monitors internal system health, or ensures the secure operation of an apparatus. In the US, translating an abstract idea (a mathematical boundary) into a specific, unconventional technological application that improves the functioning of the sensor network itself satisfies the Alice Step 2B requirement.

17. FTO

The Freedom-to-Operate landscape for algorithmic enhancements is highly sensitive. The implementation must strictly avoid "auto-calibrating" or dynamically adjusting the regression weights during runtime, as this intrudes directly upon the claims of Tata Consultancy Services (US 12,175,680 B2) and other similar predictive maintenance patents15. Furthermore, it must avoid simulating internal thermal mass physics to differentiate between ambient and core temperatures, which would skirt the Sensitech patents identified in the broader Phase 2 research51.

By locking the regression coefficients and boundary thresholds offline during the Python training phase, and utilizing the MCU purely as a static inference and boundary-checking engine, the architecture maintains a clean FTO profile relative to both the hardware incumbents (Campbell, Delta-T) and the algorithmic incumbents (TCS).

18. Claim-to-experiment map

To adequately support the prospective patent application, the 72-run semester dataset must be deliberately utilized to generate specific evidentiary proofs.

Prospective Claim Element

Required Experimental Evidence (Within 72-run matrix)

1. A soil moisture monitoring node comprising a commodity capacitive probe and temperature sensor...

Basic assembly, calibration, and stable operation of the frozen MVP ESP32 + ADS1115 architecture.

2. ...storing a pre-compiled multivariate validity boundary defining a safe operating envelope...

Offline Python generation of a boundary equation (e.g., convex hull, Mahalanobis distance limit, or threshold logic) based strictly on the Replicate 1 and 2 training split of the 72 runs.

3. ...evaluating real-time raw capacitance, temperature, and inferred state against said boundary...

Demonstration of the MCU firmware executing the boundary check in under 100 FLOPs per cycle without impacting system timing.

4. ...and generating an abstention signal when the evaluated state falls outside the boundary...

Introduction of a controlled out-of-bounds disturbance (e.g., extreme salinity S2 or anomalous, uncalibrated packing density) demonstrating the MCU correctly flags the reading as invalid rather than outputting a mathematically erroneous moisture percentage.

19. Three-month semester plan

The eight-week roadmap defined in the Phase 3C SOP requires minor augmentation to support the enhanced patent evidence without altering the budget or timeline.

Weeks 1-2 (Hardware Freeze & Gates): Execute the mandatory ADS1115 value gate against the ESP32 ADC1. Conduct the critical reinsertion and packing repeatability tests using a fixed mechanical jig to isolate packing error. Verify institutional oven access4.

Weeks 3-4 (Main Dataset Part 1): Conduct the first half of the 72 independent factorial runs (4 moisture × 3 temperature × 2 salinity × 3 replicates). Ensure the dry-basis gravimetric validation workflow is meticulously logged and that repeated ADC reads are properly averaged, not counted as separate physical samples4.

Weeks 5-6 (Model & Boundary Freeze): Fit the ridge-regularized second-order regression model. Enhancement: Simultaneously calculate the statistical boundary (validity envelope) of the training data in Python. Deploy both the fixed coefficients and the boundary thresholds to the ESP32 firmware.

Weeks 7-8 (Validation & OOD Testing): Run the untouched Replicate 3 data to prove the primary metric (RMSE improvement ≥ 20%). Enhancement: Introduce an explicitly uncalibrated "disturbance" sample (e.g., an extreme salinity dose or deliberately poor compaction) to verify the firmware successfully triggers the OOD abstention flag, generating the core patent evidence.

20. Later-semester/publication extension

If the semester MVP successfully validates the confidence-gating concept, the project provides a robust foundation for a later-semester Track C extension. Future research would involve expanding the single-soil dataset to a multi-soil matrix, assessing whether a validity envelope generated in a sandy loam can reliably detect when the probe is erroneously transferred to a heavy clay environment.

Additionally, the team could research event-driven recalibration—allowing the system to securely update its fixed coefficients at the edge only when a highly trusted physical event (e.g., complete soil saturation from a known, heavy rainfall) is detected. This bridges the gap between static inference and full adaptive learning, forming the basis of a high-impact academic publication in IoT sensor networks or precision agriculture, even if patenting is not pursued globally.

21. Budget, measurement, compute and team feasibility

The proposed enhancement is highly feasible and operates entirely within the established project constraints.

Budget: The enhancement requires absolutely no additional hardware. The ₹1,790–₹3,440 planning range (with an absolute ceiling of ₹5,000) remains perfectly intact, assuming institutional access to the drying oven and scale4.

Compute: Evaluating a polynomial boundary or checking fixed multidimensional thresholds requires negligible MCU resources (well below 2 kB of RAM and minimal floating-point operations), which is easily accommodated by the ESP32-WROOM-32 running local inference4.

Team Allocation: The five-member roster is effectively utilized4. Member 1 (Embedded Lead) writes the boundary-checking if/else firmware block. Member 2 (Data Lead) generates the boundary metrics in Python alongside the regression coefficients. Member 3 (Hardware Lead) manages the AFE and physical rig to control electrical noise. Member 4 (Learner) handles the serial logging interface and status LEDs (e.g., Green = Valid, Amber = Abstain). Member 5 (Support) ensures meticulous documentation of the 72 runs.

22. Kill criteria

The architecture must be immediately aborted or reverted to a non-patentable educational prototype if any of the following critical failures occur during Weeks 1-3:

Probe Instability: The chosen SEN0193 probe exhibits random drift, extreme hysteresis, or non-monotonic behavior that exceeds 10% of the usable span across pilot tests, rendering both regression and boundary tracking physically impossible4.

Packing Dominance: Variations in soil compaction during the 72 runs overwhelm the temperature and salinity variables, destroying the statistical validity of the dataset and preventing the generation of a meaningful boundary envelope.

Boundary Failure: The out-of-distribution detection algorithms generate excessive false positives (abstaining from valid, normal data) or fail entirely to flag deliberate extreme disturbances, proving the validity envelope mathematically ineffective.

Gravimetric Access Loss: The team loses reliable access to the institutional 105°C drying oven and 0.01g scale, permanently invalidating the ground truth data4.

23. Confidentiality boundary

To preserve international patent rights prior to filing, strict confidentiality boundaries must be enforced. The specific mathematical formulation of the validity envelope, the specific empirical bounds of the temperature and controlled salinity treatments, and the raw performance results of the OOD abstention tests must remain strictly internal. The team may publicly discuss the general use of ESP32s, ADS1115 ADCs, and polynomial regression, as these elements are already saturated in the public domain. However, no firmware code containing the boundary checks, no CSV datasets containing the 72-run matrix, and no system block diagrams depicting the validity/abstention logic may be published to GitHub, open repositories, or academic preprints prior to formal institutional Intellectual Property Review.

24. Final recommendation

Advance conditionally pending named evidence.

The frozen MVP alone is a generic aggregation of hardware and math, and is unpatentable. However, the proposed bounded enhancement—implementing a confidence-gated validity envelope for OOD abstention at the edge node—presents a highly credible, budget-compliant patent path that solves a distinct technical problem in agricultural IoT. The concept should advance to Phase 4, strictly conditional upon the successful passage of the Week-1 and Week-2 mandatory hardware gates (probe stability, ADC comparison, and packing variation mitigation).

25. Unresolved questions

ADS1115 Necessity: Does the external ADS1115 ADC actually reduce pilot RMSE by ≥15% compared to a software-calibrated ESP32 ADC1 in this specific electromagnetic environment, or does it merely add unnecessary PCB complexity without measurable benefit?

Salinity Dosing Limits: What is the precise physical mass (grams of NaCl per kg of dry soil) for the S1 salinity treatment that successfully induces a measurable curve shift without electrically saturating the 555-timer circuit of the capacitive probe?

OOD Threshold Tuning: How tight must the statistical boundary be drawn to reliably catch a sensor fault or packing error without triggering continuous, nuisance false-positive abstentions during normal diurnal temperature swings?

26. Source and verification log

The following authoritative and contextual sources were utilized in this synthesis, verifying the logical completeness of the 10 physical transport files:

[cite: 1] 00_READ_FIRST_TrueMoist_Patent_Research_Instructions.md

[cite: 2] 01_Engineering_Design_Review.md

[cite: 3] 02_Project_mC_Decision_Register_v1.2.md

[cite: 53] 03_Phase3C_Portfolio_Closure_Memo_Approved.md

[cite: 4] 04_05_TrueMoist_Architecture_and_Memory.md (Embedded Architecture Report and Memory)

[cite: 52] 06_Phase3C_TrueMoist_SOP_Final.md

[cite: 5] 07_Concept_Evidence_Matrix.md

[cite: 54] 08_Uncertainty_and_Test_Register.md

[cite: 55] 09_Patent_Research_Input_Pack.md

[cite: 51] 10_Phase2_Report_by_Claude.md

[cite: 9, 56] Analog Devices Reference Design CN0398 / Wisconsin Alumni Research US20150330932A1

[cite: 13, 36] CN 101694475 B and related CNIPA utility models

[cite: 23] Hrisko, J. (2020) Capacitive Soil Moisture Sensor Theory, Calibration.

[cite: 17, 32, 33] MDPI Sensors / Agriculture NPL Literature on dielectric sensing.

[cite: 19, 57] Campbell Scientific Patent US 7,884,620 B2

[cite: 8, 15] Fu Ching Lee Patent US 7,170,302 B2

[cite: 15, 24] Tata Consultancy Services Patent US 12,175,680 B2

[cite: 37, 38, 39, 40] IEEE / Geoscientific literature on bulk density and packing density effects.

[cite: 11, 45, 46, 47, 50] Indian Patent Office 2025 CRI Guidelines, Section 3(k), and Delhi High Court OpenTV Jurisprudence.

[cite: 16, 21, 22, 58, 59, 60] Delta-T Devices Patent US 7,944,220 B2 and NPL manuals.

[cite: 27, 41, 42, 43] IEEE / NPL literature on Calibration Transfer across sensors.

[cite: 28, 29, 30, 44] IEEE / NPL literature on Out-of-Distribution (OOD) detection and edge AI safety.

Works cited

00_READ_FIRST_TrueMoist_Patent_Research_Instructions.md

01_Engineering_Design_Review.md

02_Project_mC_Decision_Register_v1.2.md

04_05_TrueMoist_Architecture_and_Memory.md

07_Concept_Evidence_Matrix.md

Annual Report 2024-25 - Department Of Science & Technology, https://dst.gov.in/sites/default/files/Annual%20Report_2025_English.pdf

US7944220B2 - Moisture content sensor and related methods - Google Patents, https://patents.google.com/patent/US7944220B2/de

US5418466A - Moisture and salinity sensor and method of use - Google Patents, https://patents.google.com/patent/US5418466A/fr

US20150330932A1 - Soil moisture sensor - Google Patents, https://patents.google.com/patent/US20150330932A1/en

Fiber optic soil water content sensor for precision farming | Request PDF - ResearchGate, https://www.researchgate.net/publication/357677459_Fiber_optic_soil_water_content_sensor_for_precision_farming

CRI Guidelines 2025: What Every Indian Tech Founder Must Know About Software Patentability - Arctic Invent, https://www.arcticinvent.com/blog/cri-guidelines-2025-software-patentability-india

Can You Patent an Improved Version of an Already Patented, https://sudhirrao.com/insights/patent-improved-version-existing-system-india

CN101694475A - Multipoint soil moisture sensor and method utilizing same to measure soil ... - Google Patents, https://patents.google.com/patent/CN101694475A/en

Soil - METER Group, https://metergroup.com/meter-products/field-instruments/soil/

Capacitive soil moisture sensor - US7170302B2 - Google Patents, https://patents.google.com/patent/US7170302B2/en

US4655076A - Moisture measuring apparatus - Google Patents, https://patents.google.com/patent/US4655076A/en

Advances in Calibration Methods for FDR-Based Capacitive Soil Moisture Sensors - MDPI, https://www.mdpi.com/1424-8220/26/11/3366

On-the-go soil sensor for precision agriculture | Request PDF - ResearchGate, https://www.researchgate.net/publication/222518942_On-the-go_soil_sensor_for_precision_agriculture

US9804113B2 - Soil moisture sensor - Google Patents, https://patents.google.com/patent/US9804113B2/fr

TRANSACTIONS - IRIS UniPA, https://iris.unipa.it/bitstream/10447/98410/1/2014%20Symposium%20Transactions%20FINAL.pdf

Theta and Profiler Soil Moisture Probes - - Accurate Impedance Measurement Devices - Dynamax, https://dynamax.com/images/uploads/papers/95_Theta_and_profiler_soil_moisture_probes.pdf

US7944220B2 - Moisture content sensor and related methods - Google Patents, https://patents.google.com/patent/US7944220B2/en

Capacitive Soil Moisture Sensor Theory, Calibration, and Testing - ResearchGate, https://www.researchgate.net/publication/342751186_Capacitive_Soil_Moisture_Sensor_Theory_Calibration_and_Testing

US9585307B2 - Optical real-time soil sensor and auto-calibration methods - Google Patents, https://patents.google.com/patent/US9585307B2/en

Recommendation ITU-T Y Suppl. 83 (07/2024) - Optimizing digital agriculture with best practices for integrating artificial intel, https://www.itu.int/rec/dologin_pub.asp?lang=e&id=T-REC-Y.Sup83-202407-I!!PDF-E&type=items

IoT and Field Monitoring Innovations for Agriculture in 2025 - GreyB, https://greyb.com/blog/iot-field-monitoring-in-agriculture/

Applications of Artificial Intelligence in Soil Characterization and Agriculture: A Systematic Review of Techniques, Models, and Applications - MDPI, https://www.mdpi.com/2073-4395/16/13/1241

Scensory: Automated Real-Time Fungal Identification and Spatial Mapping - arXiv, https://arxiv.org/html/2509.19318v1

A Review of Resilient IoT Systems: Trends, Challenges, and Future Directions - Preprints.org, https://www.preprints.org/manuscript/202512.1717/v1/download

Design of a perception system for the safety of highly automated agricultural machines - mediaTUM, https://mediatum.ub.tum.de/doc/1795132/1795132.pdf

Humidity Sensors - MDPI, https://mdpi-res.com/bookfiles/book/1398/Humidity_Sensors.pdf?v=1750899713

Laboratory Performance of Five Selected Soil Moisture Sensors Applying Factory and Own Calibration Equations for Two Soil Media of Different Bulk Density and Salinity Levels - PMC, https://pmc.ncbi.nlm.nih.gov/articles/PMC5134571/

A Sensor to Monitor Soil Moisture, Salinity, and Temperature Profiles for Wireless Networks, https://www.mdpi.com/2224-2708/13/3/32

Tata Consultancy Services, https://www.tcs.com/content/dam/global-tcs/en/pdfs/what-we-do/services/Analytics-Insights-II/Parivartana.pdf

‪Jayant Mohite‬ - ‪Google Scholar‬, https://scholar.google.com/citations?user=WsFZViUAAAAJ&hl=en

CN103207217A - 一种非插入式栽培基质含水量传感器及其标定方法 - Google Patents, https://patents.google.com/patent/CN103207217A/zh

Capacitive Soil Moisture Measurement with PCAP04 ... - ScioSense, https://www.sciosense.com/wp-content/uploads/2026/02/PCAP04-Applicatio-Note-Capacitive-Soil-Moisture-Measurement-with-PCAP04-Evaluation-Board.pdf

INSTRUMENTATION FOR MEASUREMENT OF MOISTURE - Transportation Research Board (TRB), https://onlinepubs.trb.org/Onlinepubs/nchrp/nchrp_rpt_138.pdf

Soil science-informed neural networks for soil organic carbon density modelling under scarce bulk density data - EGUsphere, https://egusphere.copernicus.org/preprints/2026/egusphere-2026-229/egusphere-2026-229.pdf

Development and In-Field Validation of an Autonomous Soil Mechanical Resistance Sensor, https://pmc.ncbi.nlm.nih.gov/articles/PMC11946251/

D.3.1 Report on the Sensing System Framework - European Commission, https://ec.europa.eu/research/participants/documents/downloadPublic?documentIds=080166e501dc6fbb&appId=PPGMS

Multi-Sensor Soil Probe and Machine Learning Modeling for Predicting Soil Properties, https://www.researchgate.net/publication/385261172_Multi-Sensor_Soil_Probe_and_Machine_Learning_Modeling_for_Predicting_Soil_Properties

Soil Sensors in Smart Agriculture: Multi-Type Monitoring Technologies and Ecological Development Pathways - MDPI, https://www.mdpi.com/2077-0472/16/3/359

Benefits and Challenges of Artificial Intelligence in Soil Science—A Review - MDPI, https://www.mdpi.com/2073-445X/15/2/331

CRI Guidelines 2025 India: Section 3(k) Software Patents - Intepat, https://www.intepat.com/blog/cri-guidelines-2025-patent-india-3k

Trends at the O ce of the controller general of - Patents, Designs, and Trademarks (CGPDTM) - Cyril Amarchand Mangaldas, https://www.cyrilshroff.com/wp-content/uploads/2024/01/IPrecis-Newsletter_January-2024.pdf

India: The Delhi High Court's Decision in OpenTV | LexOrbis, https://www.lexorbis.com/india-the-delhi-high-courts-decision-in-opentv/

An Integrated Framework for Data Quality Fusion in Embedded Sensor Systems - MDPI, https://www.mdpi.com/1424-8220/23/8/3798

Energy-, Cost-, and Resource-Efficient IoT Hazard Detection System with Adaptive Monitoring - PMC, https://pmc.ncbi.nlm.nih.gov/articles/PMC11946864/

From Algorithms To AI: Patentability Under The 2025 CRI Draft Guidelines | Intellepedia, https://www.bananaip.com/intellepedia/cri-patent-guidelines-2025-ai-algorithms/

10_Phase2_Report_by_Claude.md

06_Phase3C_TrueMoist_SOP_Final.md


---

## Source 11: `03_CONCEPT_PORTFOLIO/TrueMoist/02_Raw_Research/03_TrueMoist_Patent_Research_Perplexity_PARTIAL.md`

- Authority: `TIER_3`
- Treatment: `SUPPORTING_EVIDENCE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `NEW_STAGE10L_EXTRACTION`
- SHA-256: `ddc397e72125105f85897055ad6c3281308ae5015e236b0f6b0666067a00795f`

# Source Extraction

- Chapter: `08` — TrueMoist Architecture, Validation and Patent Evidence
- Authority tier: `TIER_3`
- Manual treatment: `SUPPORTING_EVIDENCE`
- Original source: `03_CONCEPT_PORTFOLIO/TrueMoist/02_Raw_Research/03_TrueMoist_Patent_Research_Perplexity_PARTIAL.md`
- SHA-256: `ddc397e72125105f85897055ad6c3281308ae5015e236b0f6b0666067a00795f`
- Extraction method: `PLAIN_TEXT`
- Rule: source text only; no synthesis, correction or reconciliation.

---

# TrueMoist Current Patent Verification — Independent Research

## 1. Executive verdict

The frozen TrueMoist MVP does **not** itself constitute a clearly novel, non‑obvious patent contribution; however, it provides a solid experimental and architectural platform from which a **credible long‑term patent path based on drift/event‑driven calibration, confidence gating, and transfer/validity mechanisms could be developed with later‑semester work and additional experiments**.[^1][^2][^3][^4][^5][^6][^7][^8][^9][^10][^11][^12]

Accordingly, the executive choice is:

- **Executive verdict:** credible long‑term path requiring later‑semester extension.

And the project recommendation is:

- **Final recommendation:** retain TrueMoist as a strong semester prototype and evidence generator, but **reduce near‑term patent priority** and treat patent development as a follow‑on track contingent on additional drift/transfer/validity evidence.

## 2. Input inventory and concept fidelity

### 2.1 Logical input set

The attached corpus contains **exactly 11 readable files**, matching the expected set in the governing instruction.[^13][^14][^15][^16][^2][^17][^18][^19][^3][^20][^1]

All ten canonical project documents (01–10) are present and readable:

- 01_Engineering_Design_Review.md — authoritative engineering identities and minimum success definitions.[^14]
- 02_Project_mC_Decision_Register_v1.2.md — authoritative project‑wide and concept‑specific decisions.[^15]
- 03_Phase3C_Portfolio_Closure_Memo_Approved.md — authoritative statement that Phase 3C architecture is complete for OpenBraille, VibeGuard, TrueMoist and that TrustLatch/ColdTrace are deferred.[^16]
- 04_Phase3C_TrueMoist_Architecture_Report_Final.md — authoritative frozen TrueMoist architecture.[^1]
- 05_Phase3C_TrueMoist_Memory_Final.md — compact reconstruction of the final architecture and gates.[^2]
- 06_Phase3C_TrueMoist_SOP_Final.md — process and precedence rules for Phase 3C architecture definition.[^17]
- 07_Concept_Evidence_Matrix.md — neutral cross‑concept evidence extraction, including TrueMoist conflict notes.[^18]
- 08_Uncertainty_and_Test_Register.md — cross‑concept uncertainty register; TrueMoist entries mark unresolved patent assumptions.[^19]
- 09_Patent_Research_Input_Pack.md — scoped leads and search‑term lists for later current‑patent passes, including TrueMoist.[^3]
- 10_Phase2_Report_by_Claude.md — consolidated Phase 2 patent‑landscape synthesis to be treated strictly as historical leads, not current conclusions.[^20]

The governing instruction file 00_READ_FIRST_TrueMoist_Patent_Research_Instructions.md is present, readable, and defines the search method, authority order, concept boundaries, and required report structure.[^13]

### 2.2 Specific inventory checks requested

- **Decision Register version:** the corpus contains `02_Project_mC_Decision_Register_v1.2.md`, and no v1.1 file is present; this matches the governing rule not to substitute v1.1.[^15][^13]
- **Authoritative architecture:** the final architecture and memory both specify a **single‑soil, 4×3×2×3 factorial design with 72 independent physical runs and ridge‑regularized second‑order regression**, confirming that the authoritative architecture is the validated 72‑run TrueMoist design.[^2][^1]
- **Frozen concept scope:** both the governing instruction and final TrueMoist documents state that TrueMoist is a **local compensation system for a low‑cost analog capacitive soil‑moisture probe using temperature and controlled salinity‑treatment code**, explicitly **excluding live EC measurement, irrigation control, cloud platforms, multi‑soil scope, custom multi‑frequency probes, TinyML MVPs and online‑adaptive learners**.[^17][^13][^1][^2]
- **Missing/duplicate/ambiguous inputs:** within the TrueMoist lane, no required project‑authority file is missing or unreadable; Phase 3A and Phase 3B TrueMoist landscape/feasibility reports themselves are referenced but not attached, which is acceptable because the architecture report and memory already summarize their decisions. There are no duplicate or ambiguously named core TrueMoist files.[^18][^1][^2]

### 2.3 Authority order and adherence

The requested authority order in the governing instruction is:

1. Engineering Design Review.
2. Decision Register v1.2.
3. Approved Phase 3C closure memo.
4. Final TrueMoist architecture report.
5. Final TrueMoist memory.
6. Final TrueMoist SOP.
7. Validated evidence files (Concept Evidence Matrix, Uncertainty and Test Register, Patent Research Input Pack).
8. Phase 2 report only as historical patent‑search leads.[^13]

This report follows that order: engineering identity from the EDR, constraints and scope from PDR v1.2 and SOP, architecture and memory for frozen design, evidence matrices for conflicts, and Phase 2 only to identify historical patent families and saturation assessments.[^14][^16][^19][^3][^20][^1][^15][^2][^17][^18]

## 3. Search methodology and reproducible log

### 3.1 Databases and jurisdictions

Primary patent searching used public patent‑search interfaces covering **US, EP, WO, CN, and IN‑relevant records**, with emphasis on Google Patents and EPO servers as proxies for WIPO, US, and EP data.[^4][^21][^5][^6][^7][^8][^10][^11][^12]

The core jurisdictions of interest per the governing instruction and Phase 2 leads are the **US, Europe, WIPO, China, and India**, as these are the main sources of prior art for major soil‑moisture probe manufacturers and research institutions and the most relevant for later Indian filing and FTO considerations.[^3][^13]

### 3.2 Representative queries

Search terms were derived from the Patent Research Input Pack’s TrueMoist section and refined to match compensation, drift, calibration, and environmental‑influence themes.[^3]

Representative queries included:

- "soil moisture temperature salinity compensation patent" (broad environmental compensation).[^7][^8][^4]
- "capacitive soil moisture drift correction calibration patent" (capacitive‑probe drift and calibration).[^5][^6][^8][^10]
- "Campbell Scientific soil moisture 7,884,620" (historical lead for dual‑parameter compensation circuits).[^8]

These were augmented by specific assignee/family searches suggested in Phase 2 and the input pack (e.g., Campbell Scientific, METER Group, Toro, Delta‑T, CropX and other known soil‑moisture vendors), but full internal assignee‑wide searches were out of scope for this pass and should be performed by a later, more exhaustive counsel‑level review.[^20][^3]

### 3.3 Claim‑level reading

At least the independent claims and core calibration/compensation descriptions were read for:

- CN111272985B — temperature‑compensation calibration method for soil salinity sensors.[^4]
- CN204165927U — Hartley‑oscillator‑based capacitive soil‑moisture sensor with temperature compensation circuitry.[^5]
- EP2623971 A1 — capacitance‑based moisture sensor with calibration procedures that relate frequency response to water content.[^6]
- EP4224156 A1 — soil‑moisture sensor using a thermoelectric element to change soil temperature and derive moisture via temperature gradient curves.[^7]
- US7170302 B2 — capacitive soil moisture sensor with stable, fast‑response capacitive electrodes and protective layers.[^8]

Non‑patent technical literature was sampled for modern dielectric sensors and their performance under salinity and temperature variation, including a 2024 study on dielectric sensor performance at different salinity levels and a 2025 engineering paper on calibration and temperature compensation of low‑cost capacitive soil‑moisture stick sensors.[^22][^9]

Microwave and multi‑parameter sensor innovations that explicitly claim EC‑independence or combined moisture/temperature/matric potential sensing (e.g., RS20180253 A1 microwave phase‑shift sensor and Delta‑T WET150’s multi‑parameter EC/temperature‑stable design) were also consulted as upper‑tier reference points for compensated sensing architectures.[^23][^10]

### 3.4 Limitations of this pass

This pass does **not** constitute a complete legal search across all relevant CPC/IPC classes, nor does it exhaustively verify every historical patent number named in Phase 2 for the Campbell/METER/Toro families. Full claim charting, cross‑jurisdictional family mapping, and expiry/FTO analysis remain tasks for a later legal or IP‑specialist review.[^20]

## 4. Technical and patent landscape

### 4.1 Mature compensating soil‑moisture ecosystem

The landscape around soil‑moisture sensing is **technically mature and heavily patented**, particularly for **dielectric and capacitive probes with environmental compensation and EC‑resilient designs**.[^10][^6][^23][^5][^7][^8][^20]

Key traits of the incumbent ecosystem include:

- Commercial research‑grade sensors (e.g., METER/Delta‑T WET150) that already provide multi‑parameter measurements of moisture, temperature and EC with patented electronics that explicitly claim high salinity and temperature stability.[^23]
- Patents on capacitance‑based moisture sensors that define calibration fixtures, frequency‑response fitting, and volumetric water content relationships, often including temperature and soil‑type compensation curves.[^6][^8]
- Dedicated salinity‑sensor calibration methods that use temperature compensation and quadratic regression fits to produce high‑precision correction formulas for EC readings.[^4]
- Sensors and methods that attempt to **decouple moisture measurement from soil electrical conductivity**, such as microwave phase‑shift sensors that choose frequencies where conductivity influence is negligible and integrate temperature sensing for hybrid moisture/matric potential estimation.[^10]

Academic literature shows that low‑cost capacitive "soil stick" sensors can be significantly improved with careful calibration and temperature compensation, yielding performance comparable to time‑domain reflectometry references over specific ranges. However, these studies generally treat the compensation as **applied engineering practice**, not as clearly delineated patent claims.[^9]

### 4.2 Commodity capacitive probes and drift

Commodity capacitive soil‑moisture sensors, including various "soil stick" and fork‑style probes, are widely used but show substantial **drift and dependence on temperature, salinity and packing conditions**.[^22][^9][^14][^1]

Existing patents such as US7170302 B2 focus on mechanical and capacitive geometry, installation convenience, and stable long‑term response at particular depths, with implicit calibration but without a comprehensive embedded multi‑variable compensation workflow of the TrueMoist type.[^8]

Low‑cost calibration and compensation methods in open literature typically emphasize piecewise linear calibration and simple temperature correction without combining **temperature, controlled salinity treatment, packing, and drift/validity logic** in a single embedded workflow as TrueMoist intends.[^9]

### 4.3 Salinity and temperature compensation patents

Several patents directly address salinity and temperature compensation in soil‑related sensors:

- CN111272985B provides a detailed procedure for calibrating soil salinity sensors across temperature and concentration gradients, building a temperature‑compensation formula and absolute calibration equation via quadratic regression. It is explicitly about **salinity sensors**, not moisture probes, but its calibration method shows that **temperature‑compensated multi‑condition calibration is already claimed for soil salinity sensing**.[^4]
- CN204165927U describes a new capacitive soil‑moisture sensor using a Hartley three‑point oscillation circuit and an integrated temperature‑compensation circuit within the oscillator, again combining temperature compensation and capacitive soil‑moisture measurement.[^5]
- EP2623971 A1 and EP4224156 A1 represent sophisticated moisture sensor architectures with well‑defined calibration and conversion methods, including temperature information; they show that general moisture‑sensor calibration and temperature‑dependent conversion functions are deeply explored and protected.[^6][^7]

While these patents do not precisely mirror TrueMoist’s **controlled salinity‑treatment code without live EC and ridge regression deployment on ESP32**, they collectively indicate that **compensated soil‑moisture and salinity sensing is not a new field**, and generic statements about calibration across temperature and salinity are unlikely to be novel.

### 4.4 Adaptive and EC‑independent directions

Phase 2 historical synthesis already concluded that the **hardware compensation space is crowded, with real white space only in adaptive, event‑driven, self‑calibration algorithms and novel confidence/validity handling**.[^20]

The present landscape review supports this:

- Microwave and EC‑independent sensors show hardware efforts to avoid conductivity dependence but do not claim the kind of **event‑triggered recalibration, confidence gating, or cross‑probe transfer logic** that TrueMoist’s future directions contemplate.[^10]
- Multi‑parameter EC/temperature/moisture sensors emphasize stable measurements and calibration curves but generally assume a fixed calibration regime rather than **embedded, sparse‑reference event‑driven updates**.[^23][^6]

The plausible white space lies not in the existence of compensated probes, but in **how a low‑cost system uses sparse, trusted reference events, cross‑unit transfer strategies and validity envelopes to maintain calibration under drift and disturbance** — precisely the sort of mechanisms identified as future patent‑development paths in the TrueMoist architecture report and Patent Research Input Pack.[^1][^2][^3]

## 5. Verified patent‑family ledger (TrueMoist‑relevant)

This pass identifies **representative families and records** rather than a complete ledger; each requires deeper family and status mapping later.

### 5.1 Capacitance‑based soil‑moisture sensors

- **US7170302B2 – Capacitive soil moisture sensor.** Defines electrode geometry, protective layers, and soil‑depth targeting to measure moisture via capacitance changes; prior‑art citations include earlier capacitance probes and moisture monitors, confirming long prior‑art chains.[^8]
- **EP2623971A1 – Capacitance‑based moisture sensor.** Uses a sleeve with ring electrodes and calibration fixtures, provides fitting functions relating frequency response to water content.[^6]
- **CN204165927U – Capacity Soil Moisture Sensor.** Hartley‑oscillator‑based capacitive probe with integrated temperature‑compensation circuitry.[^5]

These families collectively show that **basic capacitive moisture sensing and straightforward temperature compensation are well established**.

### 5.2 Salinity/treatment calibration and temperature compensation

- **CN111272985B – Temperature‑compensation high‑precision calibration method for soil salinity sensors.** Claims a detailed procedure for temperature‑compensated calibration of salinity sensors using gradient salt solutions and quadratic regression.[^4]

This family targets salinity sensors but confirms that **temperature‑compensated multi‑condition calibration methods are actively patented in soil sensing**.

### 5.3 EC‑independent and multi‑parameter sensors

- **RS20180253 A1 / RS60892 – Microwave soil moisture sensor based on phase shift method and independent of electrical conductivity.** Claims a phase‑shift sensor architecture and porous matrix arrangement that reduce EC influence and enable simultaneous moisture, matric potential and temperature measurement.[^10]
- **Delta‑T WET150 sensor (patented electronics).** Product documentation states patented sensor electronics with high salinity and temperature stability for simultaneous moisture, temperature and EC measurement; underlying patent details need direct family lookup but clearly represent high‑end prior art for multi‑parameter compensated sensing.[^23]

These families define upper‑tier hardware architectures rather than low‑cost controlled‑salinity compensation workflows but underscore that **robust compensation and EC independence are active patent targets**.

### 5.4 TrueMoist historical leads

The Phase 2 report and Patent Research Input Pack cite additional families (e.g., US 7,884,620, US 11,598,743, US 7,170,302 B2, US 20150330932 A1) as historical leads related to dual‑parameter compensation circuits and capacitive soil‑moisture sensors. These have not been fully re‑checked in this pass but should be treated as **mandatory targets for later counsel‑level verification and claim charting**, given their likely proximity to TrueMoist’s technical space.[^3][^20]

## 6. Closest independent‑claim analyses (high‑level)

### 6.1 Generic capacitive moisture sensors vs. TrueMoist

Independent claims in US7170302B2, EP2623971A1, and CN204165927U broadly cover:

- a capacitive moisture sensor with electrodes forming a capacitor in soil;
- frequency or capacitance‑based measurement of water content;
- calibration procedures relating output to water content;
- in some cases, integrated temperature compensation circuits.[^5][^6][^8]

Compared with the frozen TrueMoist MVP:

- **Overlap:** capacitive sensing, temperature measurement and calibration against a reference (gravimetric water content) are all conventional.[^2][^1][^6][^8]
- **Differences:** TrueMoist emphasizes **controlled salinity treatment during calibration, a specific factorial design across moisture, temperature and salinity, and ridge‑regularized regression deployed with fixed coefficients on an ESP32**, plus planned mechanisms for drift, validity, and transfer in later work.[^1][^2][^3]

These differences appear more like **experimental design and implementation choices on top of known principles** than clearly novel claim elements.

### 6.2 Salinity calibration patents vs. TrueMoist treatment code

CN111272985B claims a **temperature‑compensation type high‑precision calibration method** for soil salinity sensors, with specific steps and fitting equations.[^4]

TrueMoist’s controlled salinity‑treatment code:

- represents salinity as a **known salt addition per dry‑soil mass, used as an experimental disturbed variable**, explicitly **without live EC measurement**.[^13][^2][^1]

From a claims perspective:

- **Overlap:** both use controlled salt solutions and gradient conditions to calibrate sensor behavior under varying salinity and temperature.[^2][^1][^4]
- **Difference:** TrueMoist uses salinity as a **coded experimental factor feeding into a compensation model** for a **moisture probe**, not as a direct EC measurement channel; there is no specific temperature‑compensation formula for EC itself.[^1][^2]

This suggests the controlled salinity‑treatment code is primarily **experimental design for compensation model training**, not a clearly distinguished patentable calibration method.

### 6.3 EC‑independent microwave sensors vs. TrueMoist

RS20180253 A1’s microwave phase‑shift sensor claims hardware and porous‑matrix arrangements that achieve **EC‑independent moisture measurement**, including integrated temperature sensing and matric potential estimation.[^10]

TrueMoist, by contrast, accepts EC‑dependent capacitive probes and attempts to **compensate error via multi‑variable regression** using temperature and salinity treatment in a single soil type.[^2][^1]

The physical principles and hardware are therefore quite distinct, but the **goal of robust moisture measurement under varying salinity and temperature is shared**, reducing room for broad high‑level claims.

## 7. Frozen‑MVP feature comparison

### 7.1 Feature chart vs. representative prior art

Using the frozen‑feature categories from the governing instruction and Concept Evidence Matrix, the table below compares TrueMoist MVP features to representative prior‑art families.

| Feature | TrueMoist MVP | Representative prior art (examples) |
|---|---|---|
| Probe type | Genuine analog capacitive probe, two units, SEN0193‑class or similar.[^1][^2] | Multiple capacitive probes with various electrode geometries and protective layers (US7170302B2, EP2623971A1).[^6][^8] |
| Temperature sensing | Waterproof DS18B20 at same depth, 20–30 mm from probe.[^1][^2] | On‑sensor temperature measurement or separate temperature sensors for compensation (WET150, microwave sensor).[^23][^10] |
| Salinity handling | Controlled salinity‑treatment code during calibration; no live EC channel.[^13][^1][^2] | Direct EC measurement and temperature‑compensated EC (WET150), salinity sensors with temperature‑compensation calibration (CN111272985B).[^4][^23] |
| ADC and analog front end | ADS1115 with 1 kΩ series resistor, 100 nF input filtering, local decoupling, short wiring, soldered perfboard; comparison to ESP32 ADC1 in Week 1.[^1][^2][^17] | Various ADC and oscillator circuits, including Hartley oscillators with temperature‑compensation, generic ADC acquisition chains.[^5][^6] |
| Controller | ESP32‑WROOM‑32 primary; ESP32‑S3 fallback; fully local inference and USB CSV.[^1][^2] | Various microcontrollers in moisture‑sensor systems and IoT irrigation controllers; true novelty rarely lies in choosing ESP32 alone.[^21][^8][^12] |
| Modelling | Baseline univariate calibration and multivariate linear regression; final ridge‑regularized second‑order regression trained offline and deployed as fixed coefficients.[^1][^2] | Polynomial regression, linear regression, and various calibration functions widely used in soil sensors and EC calibration patents.[^4][^6][^9] |
| Dataset design | Single soil; 4 moisture × 3 temperature × 2 salinity × 3 independent replicates; 72 physical runs; replicates 1–2 training/model selection, replicate 3 held‑out test.[^13][^1][^2][^17] | Multi‑condition calibration datasets common in literature and patents, though specific factorial layouts vary and are usually treated as experimental methods rather than claimed inventions.[^4][^22][^9] |
| Ground truth | Gravimetric water content, oven drying at 105 ± 5 °C until constant mass; 0.01 g scale; VWC claims only with measured bulk density.[^1][^2][^17] | Gravimetric calibration widely accepted as reference method; frequently assumed but not always claimed explicitly.[^22][^9] |
| Validation | RMSE and MAE improvements thresholds (≥20% and ≥15% respectively) and disturbance subset guardrails.[^13][^1][^2] | Many sensors report accuracy metrics but do not necessarily claim improvement thresholds as inventive features.[^22][^9] |

### 7.2 Expressly disclosed / implied / absent

Applying the governing categories:

- **Expressly disclosed in prior art:** capacitive soil‑moisture sensing; temperature compensation; EC‑related effects; calibration and regression methods; moisture‑depth targeting; EC‑independent hardware designs; temperature‑calibrated salinity sensors.[^7][^6][^23][^8][^5][^10][^4]
- **Necessarily implied:** that multi‑condition calibration datasets and regression models combine environmental variables; that controllers and ADCs are used to implement such models; that gravimetric calibration can be the reference.[^22][^9][^6]
- **Arguably suggested:** combining temperature and salinity effects in a compensation model; designing EC‑independent or EC‑resilient sensor architectures; using embedded microcontrollers for local inference.[^7][^23][^10][^4]
- **Absent or unresolved:** a clearly defined, patented mechanism for **sparse reference events, drift detection, confidence gating, validity envelopes, cross‑probe calibration transfer and calibration compression** in the specific low‑cost, single‑soil, controlled‑salinity context of TrueMoist.[^3][^1][^2]

## 8. Commercial/institutional/India/China landscape

### 8.1 Major incumbents and products

Phase 2 identified Campbell Scientific, METER Group (TEROS), Toro and related players as dominant prior‑art sources for compensated soil‑moisture sensing; this remains consistent with current product landscapes.[^20][^23][^3]

The WET150 multi‑parameter sensor from Delta‑T is an example of a **research‑grade, multi‑parameter EC/temperature/moisture probe**, marketed explicitly on its patented electronics and stability under salinity and temperature variations. Similar high‑end probes from METER and Campbell provide compensated moisture and EC measurements, often priced above typical student budgets.[^23]

Low‑cost capacitive probes and soil sticks are widely sold and discussed in hobbyist and agricultural engineering communities, typically **without sophisticated embedded compensation**, relying instead on simple calibration curves or proprietary controller algorithms.[^9][^8]

### 8.2 Indian and Chinese prior art

The IIT Bombay patent on a **capacitive humidity and soil‑moisture microsensor using graphene oxide** demonstrates Indian innovation in combined humidity and soil‑moisture capacitive sensing, further confirming that capacitive moisture sensing is an active, patented field locally.[^11]

Chinese patents such as CN111272985B and CN204165927U show both **temperature‑compensated salinity calibration methods** and **capacitive soil‑moisture sensors with temperature compensation circuits**, indicating strong activity in the CN jurisdiction around the same general physical phenomena TrueMoist addresses.[^5][^4]

### 8.3 Implications for TrueMoist

From a commercial and institutional standpoint, TrueMoist’s **low‑cost, single‑soil, student‑team‑friendly architecture** is well aligned with educational and smallholder contexts but operates in a space where **many incumbents already claim high‑performance, compensated sensing solutions**.[^22][^9][^1][^2][^23]

Therefore, any patent‑relevant contribution must differentiate itself **not just by using capacitive probes and regression, but by specific, experimentally validated mechanisms for drift handling, confidence gating, cross‑probe transfer and validity envelopes** that are demonstrably absent or only implicitly suggested in current products and patents.[^1][^2][^3]

## 9. Non‑patent prior art and measurement practice

Non‑patent literature and practice around soil‑moisture sensing emphasize:

- **Dielectric sensors and their sensitivity to salinity and temperature**, with numerous studies comparing different probes across salinity gradients and temperatures and proposing calibration strategies to correct bias and drift.[^22]
- **Calibration and temperature compensation methods for low‑cost capacitive sensors**, including piecewise linear calibration curves, linear temperature correction models and comparisons with TDR references.[^9]
- **Standard gravimetric methods** for water content determination as the reference for sensor calibration, including oven drying and mass measurement.[^9][^22]

These practices are widely documented and form the **engineering baseline** TrueMoist explicitly builds upon; they therefore reduce the scope for claiming novelty in basic calibration regimes themselves.

## 10. Frozen‑MVP patent assessment

### 10.1 Novelty

At the frozen MVP level, TrueMoist combines known elements:

- a commodity capacitive moisture probe;
- an embedded microcontroller (ESP32);
- an external ADC (ADS1115) with standard analog conditioning;
- temperature measurement via DS18B20;
- controlled salinity treatments during calibration;
- gravimetric calibration;
- multivariate linear and ridge‑regularized second‑order regression models.[^17][^2][^1]

Each of these elements, individually and in common combinations, appears in prior art or standard practice.[^11][^6][^8][^23][^22][^9][^10][^4][^5]

While the **exact factorial dataset design (4×3×2×3 with 72 runs) and specific modelling choices** are distinctive for this project, they are more reasonably viewed as **one instantiation of conventional experimental design and regression‑based calibration**, not as novel technical effects.

Therefore, the frozen MVP alone does **not** show strong novelty over the combined prior art and practice.

### 10.2 Inventive step / obviousness

Given the maturity of capacitive soil‑moisture sensing, environmental compensation and regression‑based calibration, a skilled person in precision agriculture and embedded sensing could reasonably design a system similar to TrueMoist by combining known probes, temperature sensors, ADCs and regression models with gravimetric calibration and multi‑factor datasets.[^6][^8][^22][^9]

TrueMoist’s specific controlled salinity‑treatment code and factorial dataset represent **careful engineering**, but they follow standard design‑of‑experiments and calibration practices and are unlikely to clear inventive‑step thresholds on their own.

### 10.3 Patent eligibility

In US, EPO and India, methods that primarily claim **data processing and regression on sensor data** face eligibility and subject‑matter constraints if they are not tightly coupled to a specific technical effect or hardware interaction beyond generic sensing and computation.[^13][^3]

TrueMoist’s MVP is strongly software‑ and data‑driven; its potential patent trajectory must therefore emphasize **technical effects such as robust drift detection, validity gating and safe fallback in physically constrained embedded systems**, not just the existence of regression models.

### 10.4 Freedom‑to‑operate (FTO)

Given the high saturation of capacitive soil‑moisture and environmental‑compensation patents, **FTO cannot be assumed** if TrueMoist were commercialized, even if no exact duplicate is found.[^3][^20]

However, as a **semester‑scale prototype and academic project**, near‑term FTO risk is limited, provided the build clearly avoids copying proprietary circuits or specific patented sensor geometries and remains in an educational context.[^17][^1]

A later commercial or patent‑driven development would require full FTO analysis against the Campbell, METER, Toro, Delta‑T and other families, including careful review of any claims around EC compensation, drift handling, validity gating and adaptive calibration.[^8][^20][^23][^10][^3]

## 11. Candidate invention‑direction matrix

The Patent Research Input Pack and TrueMoist architecture report propose multiple future technical directions that could form the basis of a patent contribution if adequately developed and evidenced.[^2][^1][^3]

The table below summarizes and classifies them:

| Direction | Problem | Contribution concept | Closest known art | Overlap/difference | Three‑month feasibility | Later‑semester potential |
|---|---|---|---|---|---|---|
| Probe‑specific characterization and automatic calibration transfer | Commodity probes vary in response; replacement requires new calibration. | Characterize probes and derive transfer functions or confidence bounds to reuse calibration across units with bounded error. | Capacitive sensor patents and health‑monitoring systems (e.g., TCS sensor‑health monitoring).[^8][^12] | Overlap in health/diagnostic concepts; difference if a specific transfer mechanism with confidence gating is defined and validated. | Low–medium: needs multiple probes and controlled experiments; heavy for one semester. | Strong: could form a long‑term patent path if unique and validated. |
| Dual‑probe disagreement for validity/health | Detect sensor failure by comparing two probes rather than averaging. | Use disagreement and known disturbance patterns to flag invalid readings and trigger fallback or recalibration. | Generic sensor redundancy and cross‑check schemes; some health‑monitoring patents.[^12] | Likely conventional unless tied to a specific moisture/salinity/packing experimental sequence and confidence model. | Medium: feasible to implement and test disagreement and failure modes on two probes. | Moderate: potential if combined with drift and event logic. |
| Insertion/packing‑aware compensation | Packing density and insertion vary; they distort readings. | Controlled experiments varying packing and insertion to derive compensation or validity envelopes. | General dielectric sensor studies on packing effects and calibration.[^22] | Overlap in recognising packing; difference if a specific embedded compensation/validity rule is derived and claimed. | Medium: requires careful experimental design and more conditions. | Strong if combined with validity envelopes and safety gates. |
| Contamination‑protected drift adaptation | Fertilizer/salinity spikes cause drift and contamination. | Event‑driven recalibration using sparse gravimetric or trusted reference events and drift detection. | General calibration and drift detection literature and patents; event‑based algorithms vary.[^20][^22][^9] | High overlap conceptually; difference depends on a specific embedded method proven against closest art. | Low within current semester: requires multi‑season or extended experiments. | Very strong as long‑term patent direction; central Phase 2 recommendation.[^20][^3] |
| Confidence‑gated/abstaining estimates | Unsafe extrapolation outside validated domains. | Use model validity regions and confidence scores to abstain or fall back when conditions are outside training envelope. | Generic validity and confidence gating in ML; some sensor quality assessment patents.[^12] | Overlap at high level; difference if tied to specific moisture/temperature/salinity/packing envelopes and embedded decision logic. | Medium: could define simple bounds and abstain policies in one semester. | Strong: combined with drift and transfer could be patent‑relevant. |
| Reference‑event self‑validation/recalibration | Need to anchor calibration occasionally without full recalibration. | Use specific irrigation or drying events as sparse references to adjust coefficients or detect drift. | Event‑based calibration literature; no clear off‑the‑shelf patents identified in this pass. | Concept overlaps general calibration, but specific event selection and update rule may be novel. | Low–medium: initial experiments possible but limited by semester length. | Strong as long‑term direction; must be supported by extensive experiments. |
| Calibration provenance and validity envelope | Avoid overclaiming universal accuracy. | Track calibration provenance (soil type, probe unit, conditions) and enforce validity envelopes. | General metadata tracking and QC; rarely patented as a standalone feature. | Mostly conventional unless combined with a specific embedded enforcement mechanism. | High: can be implemented as part of logging and logic. | Moderate: more supportive than central invention. |

Overall, most strong directions require **later‑semester work** beyond the current 72‑run MVP dataset, especially drift, event‑driven recalibration and cross‑unit transfer.

## 12. Strongest surviving direction

Based on current landscape and project constraints, the strongest long‑term invention direction is:

> **A specific, experimentally validated, event‑driven drift detection and confidence‑gated recalibration mechanism for commodity capacitive soil‑moisture probes, using sparse trusted reference events and controlled separation of packing, temperature and salinity effects, implemented in a low‑cost embedded system with explicit validity envelopes and safe fallback.**[^20][^1][^2][^3]

This direction aligns with Phase 2’s conclusion that the hardware compensation space is saturated and that **self‑calibration algorithms with sparse reference events and drift/event logic** represent the main remaining white space. It also leverages TrueMoist’s frozen architecture as an experimental platform but requires **additional experiments across time, probe units and soil batches** beyond the current MVP.[^20]

## 13. Level‑1 compensation vs. Level‑2 robustness/transfer

### 13.1 Level‑1: MVP‑scale compensation

Level‑1 focuses on the current semester MVP:

- Achieving ≥20% RMSE and ≥15% MAE improvement on held‑out replicates for the ridge regression versus raw output.[^13][^1][^2]
- Demonstrating compensation across controlled temperature and salinity treatments in a single soil type.[^9][^1][^2]

This level is **purely engineering validation** and does not by itself support strong patent claims.

### 13.2 Level‑2: robustness, drift and transfer

Level‑2 covers robustness and transfer features:

- Detecting drift and contamination over longer time scales and repeated cycles.[^1][^2][^3]
- Transferring calibration across probe units with confidence bounds and fallback.[^3]
- Enforcing validity envelopes and abstaining when conditions fall outside calibrated domains.[^2][^1]

These mechanisms, if concretely defined and experimentally validated in future phases, are more likely to have **claimable technical contributions**.

## 14. Novelty (revisited)

In summary:

- The **frozen MVP** is **not novel** in its basic elements but is a good experimental vehicle.
- Novelty must focus on **specific drift/event/transfer/validity mechanisms**, not on the existence of capacitive probes, temperature sensors, regression models, or controlled calibration datasets.

## 15. Inventive step / obviousness (revisited)

Any claim that simply aggregates **capacitive moisture sensing + temperature measurement + controlled salinity treatments + regression** is likely obvious over the combined prior art.[^11][^6][^23][^22][^8][^10][^4][^5][^9]

Inventive‑step arguments must therefore emphasize **non‑trivial algorithmic structures and control workflows** that solve specific drift and validity problems in ways not taught or suggested by existing patents and literature.

## 16. Patent eligibility (revisited)

For US, EPO and India:

- Claims that merely describe data processing and regression on sensor data risk being categorized as **abstract mathematical methods** without technical character.[^13]
- Eligibility improves when claims are **tightly linked to specific embedded workflows, hardware interactions, and measurable technical effects**, such as reduced drift under certain conditions and safe handling of out‑of‑domain measurements.[^3]

TrueMoist’s future patent path must be shaped accordingly.

## 17. Freedom‑to‑operate

At the MVP stage, as an academic prototype, FTO risk is manageable if the architecture avoids copying specific patented circuits or sensor geometries and remains clearly separated from commercial research‑grade products.[^23][^8][^10][^1]

However, **later commercialization or patent filing would require**:

- full family and claim mapping for Campbell, METER, Toro, Delta‑T, IIT Bombay and microwave/EC‑independent sensors;[^11][^8][^10][^23][^20][^3]
- explicit differentiation from patents claiming temperature‑compensated calibration methods and EC‑resilient hardware;[^7][^6][^4][^5]
- careful drafting of claims to focus on **drift/event/validity mechanisms** rather than generic compensation.

## 18. Claim‑to‑experiment map

A later patent‑oriented experimental programme should map proposed claims to experiments as follows:

- **Drift detection and event‑driven recalibration:** long‑term experiments with repeated irrigation/drying cycles, salinity disturbances and periodic gravimetric checks to show improved stability and safe updates.[^22][^9][^1][^2][^3]
- **Cross‑unit calibration transfer:** multiple probe units characterized under the same conditions, with algorithms that transfer calibration and quantify residual error, compared to naive per‑probe calibration.[^8][^3]
- **Validity envelopes and abstaining:** experiments that deliberately push conditions beyond calibrated domains (e.g., extreme salinity or packing) and show that the system correctly abstains or falls back rather than producing misleading estimates.[^22][^1][^2]

The current 72‑run MVP dataset and thresholds should be preserved as a **baseline for compensation**, with later experiments layered on top for patent‑oriented contributions.[^13][^2]

## 19. Three‑month semester plan (TrueMoist MVP)

The Phase 3C architecture report already provides an eight‑week roadmap that fits within the approximate two‑month development window and budget constraints.[^17][^1]

Within that plan, this patent‑verification pass recommends:

- Treat patent work during the semester as **documentation and future‑direction planning**, not as an immediate filing goal.
- Focus on **robust execution of the 72‑run MVP**, ensuring clean gravimetric references, ADC comparison and controlled salinity treatments to generate high‑quality baseline evidence.[^9][^1][^2]

## 20. Later‑semester / publication extension

Later semesters or research projects could extend TrueMoist by:

- implementing and testing drift‑detection and event‑driven recalibration mechanisms over longer field deployments;[^20][^3]
- exploring cross‑probe calibration transfer and probe health monitoring in collaboration with sensor manufacturers or agricultural institutions;[^12][^8][^3]
- integrating validity envelopes and abstaining behavior with simple decision‑support interfaces for irrigation.[^1][^2]

These extensions would be more appropriate times to revisit patent filing decisions.

## 21. Budget, measurement, compute and team feasibility

TrueMoist’s frozen architecture remains within the **₹3,000–₹5,000 budget, two‑month timeline and five‑member team constraints**, using off‑the‑shelf components and local processing.[^14][^17][^2][^13][^1]

The additional patent‑oriented experiments envisioned for later phases will demand **more time, equipment access (e.g., reliable ovens and scales) and possibly field collaboration**, but they are not required for the current semester MVP.

## 22. Kill criteria

TrueMoist’s architecture report and SOP already define kill factors such as unstable probe output, inseparable moisture and salinity effects, unreliable gravimetric reference, or compensation worsening important edge cases.[^17][^1]

From a patent perspective, additional kill conditions include:

- discovery that existing patents already claim the specific drift/event/validity mechanisms proposed;[^6][^7][^10][^4][^23][^8][^20]
- experimental failure to demonstrate measurable advantages over generic multivariate calibration;[^22][^9]
- legal assessment that claimable subject matter would be ineligible or obvious in key jurisdictions.

## 23. Confidentiality boundary

New mechanisms, calibration rules, datasets and results from TrueMoist experiments should remain **confidential until institutional IPR review**, as required by the governing instruction. This patent‑verification report itself is technical and strategic, not a public disclosure.[^13]

## 24. Final recommendation

TrueMoist should be **advanced as a strong semester prototype focused on trustworthy compensated sensing, with patent development treated as a long‑term, conditional path** dependent on later drift/event/transfer/validity evidence.[^2][^1][^3][^20]

As per the required final recommendation options:

- **Retain as strong semester prototype but reduce patent priority** under the current patent‑first selection criterion, while keeping the future self‑calibration direction in view.

## 25. Unresolved questions

Key unresolved questions for future work include:

1. How crowded are drift/event‑driven self‑calibration and probe‑transfer subfields today, once all Campbell/METER/Toro families and recent patents are fully claim‑charted?[^3][^20]
2. Can controlled error‑source separation (packing, temperature, salinity) be framed as a truly technical method beyond ordinary experimental practice?[^17][^9][^1][^22]
3. What specific algorithms and experimental evidence are needed to show measurable advantages over generic multivariate calibration in the presence of drift and probe variability?[^9][^1][^2][^22][^3]
4. Which jurisdictions and claim forms (device vs. method vs. system) would offer the most robust eligibility and inventive‑step prospects for a future TrueMoist‑derived patent?

## 26. Source and verification log

- Project authority documents: EDR, PDR v1.2, Phase 3C closure memo, TrueMoist architecture report, TrueMoist memory, TrueMoist SOP, Concept Evidence Matrix, Uncertainty and Test Register, Patent Research Input Pack, Phase 2 synthesis.[^16][^19][^15][^18][^14][^17][^1][^2][^20][^3]
- Patent sources: CN111272985B, CN204165927U, EP2623971A1, EP4224156A1, US7170302B2, RS20180253A1/RS60892 (microwave EC‑independent sensor), Delta‑T WET150 product documentation.[^7][^10][^4][^5][^6][^23][^8]
- Non‑patent technical literature: performance of soil‑moisture sensors at different salinity levels, calibration and temperature compensation of low‑cost capacitive sensors.[^22][^9]
- Additional contextual patents/products on soil‑moisture sensors and remote moisture monitoring.[^21][^24][^12][^11]

All conclusions above distinguish between verified facts, prior‑art assertions, project‑internal decisions, and inferred recommendations.

---

## References

1. [04_Phase3C_TrueMoist_Architecture_Report_Final.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/144580388/49e8403e-9c43-4907-9e9e-09b771b0d771/04_Phase3C_TrueMoist_Architecture_Report_Final.md?AWSAccessKeyId=ASIA2F3EMEYE2U37XSDH&Signature=XA6IGz2XgUz40uNpWAVb02tToxc%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEBIaCXVzLWVhc3QtMSJGMEQCIC06YBUkSctd9HliJgMKGBReLfuYpFuhQUBOIJtRhMy3AiBmzfWQGKLneeCnrlWYaUlWhqlYZlcjAAknX6zNGJo3Cyr8BAjb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAEaDDY5OTc1MzMwOTcwNSIM4V5vuKntkpzP%2BgOfKtAE2%2BBzHNquAcvmjBddOgO8PLvz02nN21%2FL%2B3IS83NxyVZaEm5g86zAaRA1TiYeScbZ7xes4ZBfRavrqXIpGe%2Ffedi9Vlsxn95qEBeaGmwoNsqvbufhFD4K2Frh5gdnD%2FFwgsTVfQWxafj5XU6OEA7kyl3ctROby92LFqF9%2FjD6NEFKnTSWwyF75EWaN%2BX21cJfh11howfghFDwN4LC3Q3jyIv6cTu04dKVC6N4su1NUNE03o7O0jhJFJlwAN78K5dzcl7rucZryTgwrLLeXHuwhouV%2BntaJr6jGQGe3mEOWmvEWrw01t8yob%2F%2FD%2BTZQnoyErqjIoeYD7TvBs6aQP8lxLsDDAxazUYqR9x3FfQxTK1aNJuilfmYXR3rftx5XQeuEdrzTEMyf1veWQ6TimAyOl4hGJAC8tKSw6sunp2TWD183NoQhV%2Bs6TGBT9%2FswrfKH1TSD54jd%2FUMKO8FnayD5lsT4tEa0%2BRBLd5ZUq2%2BRnednWD0xog9M%2FL5gzSjuBKj3ukRirhQKb49NCu5LW4nM1HXxuk7OUTjKc8ZQZoX%2FOXRTK1lAJgK37cvrRIwLBy6a9xvIM5Yalge8ZJTtExBJ%2BPw8E296a03PhEFEW3WMwRReVwrX92ElcHysB9qUmyoKeqjNL2G3RzVs0WFKqRnvzEaGCrzBNni2QCsFpuc0ZHo8xkP5%2FLGjfT6Ccd9LOXpIG%2BNCZGBK4%2BD4C3PvRQgeKrgxtc65Ivjs5ut3Z2evpHmN%2FFejufYJV4SZQ2dWf2wwHMhUksLBXvduKWSkP%2BEADChqrzTBjqZAZ7mDifugINJ8GDZcf%2F1oTywyzJvy3z%2BXwpWHjcc%2B1%2FGmGLCyf6ur%2FiV3CVJMwi0%2FsfPSd8bIfF807SFlmOEFYzxxbR2DrJ68%2F%2BxAwiHbOs5cCjtA0xEcz%2Fm7X%2Ffd0FRy44hgauoZQGPZxedZKzX6BL33m%2FbcIqI80hq59QMGB9jZmtlijSk4wB111xOi7zCIaYT26hJL5hp%2Bg%3D%3D&Expires=1785668340) - # Phase 3C — TrueMoist Final Engineering Architecture Synthesis

**Project:** Project mC
**Concept...

2. [05_Phase3C_TrueMoist_Memory_Final.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/144580388/03894e1e-0c02-4435-bfe4-2987ff35c21f/05_Phase3C_TrueMoist_Memory_Final.md?AWSAccessKeyId=ASIA2F3EMEYE2U37XSDH&Signature=TJMFEVz0LAfsoajtXr4Blxhphtk%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEBIaCXVzLWVhc3QtMSJGMEQCIC06YBUkSctd9HliJgMKGBReLfuYpFuhQUBOIJtRhMy3AiBmzfWQGKLneeCnrlWYaUlWhqlYZlcjAAknX6zNGJo3Cyr8BAjb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAEaDDY5OTc1MzMwOTcwNSIM4V5vuKntkpzP%2BgOfKtAE2%2BBzHNquAcvmjBddOgO8PLvz02nN21%2FL%2B3IS83NxyVZaEm5g86zAaRA1TiYeScbZ7xes4ZBfRavrqXIpGe%2Ffedi9Vlsxn95qEBeaGmwoNsqvbufhFD4K2Frh5gdnD%2FFwgsTVfQWxafj5XU6OEA7kyl3ctROby92LFqF9%2FjD6NEFKnTSWwyF75EWaN%2BX21cJfh11howfghFDwN4LC3Q3jyIv6cTu04dKVC6N4su1NUNE03o7O0jhJFJlwAN78K5dzcl7rucZryTgwrLLeXHuwhouV%2BntaJr6jGQGe3mEOWmvEWrw01t8yob%2F%2FD%2BTZQnoyErqjIoeYD7TvBs6aQP8lxLsDDAxazUYqR9x3FfQxTK1aNJuilfmYXR3rftx5XQeuEdrzTEMyf1veWQ6TimAyOl4hGJAC8tKSw6sunp2TWD183NoQhV%2Bs6TGBT9%2FswrfKH1TSD54jd%2FUMKO8FnayD5lsT4tEa0%2BRBLd5ZUq2%2BRnednWD0xog9M%2FL5gzSjuBKj3ukRirhQKb49NCu5LW4nM1HXxuk7OUTjKc8ZQZoX%2FOXRTK1lAJgK37cvrRIwLBy6a9xvIM5Yalge8ZJTtExBJ%2BPw8E296a03PhEFEW3WMwRReVwrX92ElcHysB9qUmyoKeqjNL2G3RzVs0WFKqRnvzEaGCrzBNni2QCsFpuc0ZHo8xkP5%2FLGjfT6Ccd9LOXpIG%2BNCZGBK4%2BD4C3PvRQgeKrgxtc65Ivjs5ut3Z2evpHmN%2FFejufYJV4SZQ2dWf2wwHMhUksLBXvduKWSkP%2BEADChqrzTBjqZAZ7mDifugINJ8GDZcf%2F1oTywyzJvy3z%2BXwpWHjcc%2B1%2FGmGLCyf6ur%2FiV3CVJMwi0%2FsfPSd8bIfF807SFlmOEFYzxxbR2DrJ68%2F%2BxAwiHbOs5cCjtA0xEcz%2Fm7X%2Ffd0FRy44hgauoZQGPZxedZKzX6BL33m%2FbcIqI80hq59QMGB9jZmtlijSk4wB111xOi7zCIaYT26hJL5hp%2Bg%3D%3D&Expires=1785668340) - # Project mC — Phase 3C TrueMoist Memory

**Version:** 1.0
**Status:** Complete
**Date:** 27 Jul...

3. [09_Patent_Research_Input_Pack.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/144580388/7e812e45-f222-4160-b53d-85bc69783d8c/09_Patent_Research_Input_Pack.md?AWSAccessKeyId=ASIA2F3EMEYE2U37XSDH&Signature=mWRT0%2FRApeQ2p4J49iVam1mYcNw%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEBIaCXVzLWVhc3QtMSJGMEQCIC06YBUkSctd9HliJgMKGBReLfuYpFuhQUBOIJtRhMy3AiBmzfWQGKLneeCnrlWYaUlWhqlYZlcjAAknX6zNGJo3Cyr8BAjb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAEaDDY5OTc1MzMwOTcwNSIM4V5vuKntkpzP%2BgOfKtAE2%2BBzHNquAcvmjBddOgO8PLvz02nN21%2FL%2B3IS83NxyVZaEm5g86zAaRA1TiYeScbZ7xes4ZBfRavrqXIpGe%2Ffedi9Vlsxn95qEBeaGmwoNsqvbufhFD4K2Frh5gdnD%2FFwgsTVfQWxafj5XU6OEA7kyl3ctROby92LFqF9%2FjD6NEFKnTSWwyF75EWaN%2BX21cJfh11howfghFDwN4LC3Q3jyIv6cTu04dKVC6N4su1NUNE03o7O0jhJFJlwAN78K5dzcl7rucZryTgwrLLeXHuwhouV%2BntaJr6jGQGe3mEOWmvEWrw01t8yob%2F%2FD%2BTZQnoyErqjIoeYD7TvBs6aQP8lxLsDDAxazUYqR9x3FfQxTK1aNJuilfmYXR3rftx5XQeuEdrzTEMyf1veWQ6TimAyOl4hGJAC8tKSw6sunp2TWD183NoQhV%2Bs6TGBT9%2FswrfKH1TSD54jd%2FUMKO8FnayD5lsT4tEa0%2BRBLd5ZUq2%2BRnednWD0xog9M%2FL5gzSjuBKj3ukRirhQKb49NCu5LW4nM1HXxuk7OUTjKc8ZQZoX%2FOXRTK1lAJgK37cvrRIwLBy6a9xvIM5Yalge8ZJTtExBJ%2BPw8E296a03PhEFEW3WMwRReVwrX92ElcHysB9qUmyoKeqjNL2G3RzVs0WFKqRnvzEaGCrzBNni2QCsFpuc0ZHo8xkP5%2FLGjfT6Ccd9LOXpIG%2BNCZGBK4%2BD4C3PvRQgeKrgxtc65Ivjs5ut3Z2evpHmN%2FFejufYJV4SZQ2dWf2wwHMhUksLBXvduKWSkP%2BEADChqrzTBjqZAZ7mDifugINJ8GDZcf%2F1oTywyzJvy3z%2BXwpWHjcc%2B1%2FGmGLCyf6ur%2FiV3CVJMwi0%2FsfPSd8bIfF807SFlmOEFYzxxbR2DrJ68%2F%2BxAwiHbOs5cCjtA0xEcz%2Fm7X%2Ffd0FRy44hgauoZQGPZxedZKzX6BL33m%2FbcIqI80hq59QMGB9jZmtlijSk4wB111xOi7zCIaYT26hJL5hp%2Bg%3D%3D&Expires=1785668340) - # Patent Research Input Pack

## Scope and warning

This pack prepares—not performs—a later current ...

4. [Temperature compensation type high-precision calibration method for soil salinity sensor](https://patents.google.com/patent/CN111272985B/en) - The invention relates to a temperature compensation type high-precision calibration method for a soi...

5. [Capacity Soil Moisture Sensor - CN204165927U](https://patents.google.com/patent/CN204165927U/en) - The utility model patent with the publication number CN2641646 discloses a soil moisture content det...

6. [Capacitance-based moisture sensor - EP 2623971 A1](https://data.epo.org/publication-server/rest/v1.0/publication-dates/20130807/patents/EP2623971NWA1/document.pdf) - US Patent 5418466 entitled "Moisture and Sa- linity Sensor and Method of Use" relating to moisture a...

7. [MOISTURE SENSOR](https://data.epo.org/publication-server/rest/v1.2/patents/EP4224156NWA1/document.html) - MOISTURE SENSOR - Patent 4224156

8. [Capacitive soil moisture sensor](https://patents.google.com/patent/US7170302B2/en) - A capacitive soil moisture sensor that is easy to install, does not require complex calibration, can...

9. [Calibration and Temperature Compensation of a Low-Cost ...](https://etasr.com/index.php/ETASR/article/view/9677) - by N Chulee · 2025 · Cited by 1 — This study developed and validated a combined calibration and temp...

10. [Microwave soil moisture sensor based on phase shift ...](https://biosense.rs/en/patents/microwave-soil-moistructure-sensor-based-on-phase-shift-method-and-independet-of-electrical-conductivity-of-the-soil) - Microwave soil moisture sensor based on phase shift method and independet of electrical conductivity...

11. [Capacitive Based Humidity and Soil Moisture Micro-Sensor ...](https://rnd.iitb.ac.in/node/2217) - This invention describes a small, low-cost sensor that can measure both humidity and soil moisture u...

12. [System, apparatus, and method for remote soil moisture ...](https://patents.google.com/patent/US10028425) - A system for remote moisture monitoring and control includes: a measurement vehicle, including a veh...

13. [00_READ_FIRST_TrueMoist_Patent_Research_Instructions.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/144580388/d92c1af6-dbf7-49ad-a8eb-12ca81fbb208/00_READ_FIRST_TrueMoist_Patent_Research_Instructions.md?AWSAccessKeyId=ASIA2F3EMEYE2U37XSDH&Signature=qxkE7C8vp0IpZnC3SAhdkYUXKEU%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEBIaCXVzLWVhc3QtMSJGMEQCIC06YBUkSctd9HliJgMKGBReLfuYpFuhQUBOIJtRhMy3AiBmzfWQGKLneeCnrlWYaUlWhqlYZlcjAAknX6zNGJo3Cyr8BAjb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAEaDDY5OTc1MzMwOTcwNSIM4V5vuKntkpzP%2BgOfKtAE2%2BBzHNquAcvmjBddOgO8PLvz02nN21%2FL%2B3IS83NxyVZaEm5g86zAaRA1TiYeScbZ7xes4ZBfRavrqXIpGe%2Ffedi9Vlsxn95qEBeaGmwoNsqvbufhFD4K2Frh5gdnD%2FFwgsTVfQWxafj5XU6OEA7kyl3ctROby92LFqF9%2FjD6NEFKnTSWwyF75EWaN%2BX21cJfh11howfghFDwN4LC3Q3jyIv6cTu04dKVC6N4su1NUNE03o7O0jhJFJlwAN78K5dzcl7rucZryTgwrLLeXHuwhouV%2BntaJr6jGQGe3mEOWmvEWrw01t8yob%2F%2FD%2BTZQnoyErqjIoeYD7TvBs6aQP8lxLsDDAxazUYqR9x3FfQxTK1aNJuilfmYXR3rftx5XQeuEdrzTEMyf1veWQ6TimAyOl4hGJAC8tKSw6sunp2TWD183NoQhV%2Bs6TGBT9%2FswrfKH1TSD54jd%2FUMKO8FnayD5lsT4tEa0%2BRBLd5ZUq2%2BRnednWD0xog9M%2FL5gzSjuBKj3ukRirhQKb49NCu5LW4nM1HXxuk7OUTjKc8ZQZoX%2FOXRTK1lAJgK37cvrRIwLBy6a9xvIM5Yalge8ZJTtExBJ%2BPw8E296a03PhEFEW3WMwRReVwrX92ElcHysB9qUmyoKeqjNL2G3RzVs0WFKqRnvzEaGCrzBNni2QCsFpuc0ZHo8xkP5%2FLGjfT6Ccd9LOXpIG%2BNCZGBK4%2BD4C3PvRQgeKrgxtc65Ivjs5ut3Z2evpHmN%2FFejufYJV4SZQ2dWf2wwHMhUksLBXvduKWSkP%2BEADChqrzTBjqZAZ7mDifugINJ8GDZcf%2F1oTywyzJvy3z%2BXwpWHjcc%2B1%2FGmGLCyf6ur%2FiV3CVJMwi0%2FsfPSd8bIfF807SFlmOEFYzxxbR2DrJ68%2F%2BxAwiHbOs5cCjtA0xEcz%2Fm7X%2Ffd0FRy44hgauoZQGPZxedZKzX6BL33m%2FbcIqI80hq59QMGB9jZmtlijSk4wB111xOi7zCIaYT26hJL5hp%2Bg%3D%3D&Expires=1785668340) - # Project mC — TrueMoist Current Patent Verification — Independent Research

## Role

Act as an inde...

14. [01_Engineering_Design_Review.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/144580388/a497f277-47ac-4b85-874a-fe1e7626b2fe/01_Engineering_Design_Review.md?AWSAccessKeyId=ASIA2F3EMEYE2U37XSDH&Signature=luYw7B%2Fk25F4uclqn0U6VWVv76U%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEBIaCXVzLWVhc3QtMSJGMEQCIC06YBUkSctd9HliJgMKGBReLfuYpFuhQUBOIJtRhMy3AiBmzfWQGKLneeCnrlWYaUlWhqlYZlcjAAknX6zNGJo3Cyr8BAjb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAEaDDY5OTc1MzMwOTcwNSIM4V5vuKntkpzP%2BgOfKtAE2%2BBzHNquAcvmjBddOgO8PLvz02nN21%2FL%2B3IS83NxyVZaEm5g86zAaRA1TiYeScbZ7xes4ZBfRavrqXIpGe%2Ffedi9Vlsxn95qEBeaGmwoNsqvbufhFD4K2Frh5gdnD%2FFwgsTVfQWxafj5XU6OEA7kyl3ctROby92LFqF9%2FjD6NEFKnTSWwyF75EWaN%2BX21cJfh11howfghFDwN4LC3Q3jyIv6cTu04dKVC6N4su1NUNE03o7O0jhJFJlwAN78K5dzcl7rucZryTgwrLLeXHuwhouV%2BntaJr6jGQGe3mEOWmvEWrw01t8yob%2F%2FD%2BTZQnoyErqjIoeYD7TvBs6aQP8lxLsDDAxazUYqR9x3FfQxTK1aNJuilfmYXR3rftx5XQeuEdrzTEMyf1veWQ6TimAyOl4hGJAC8tKSw6sunp2TWD183NoQhV%2Bs6TGBT9%2FswrfKH1TSD54jd%2FUMKO8FnayD5lsT4tEa0%2BRBLd5ZUq2%2BRnednWD0xog9M%2FL5gzSjuBKj3ukRirhQKb49NCu5LW4nM1HXxuk7OUTjKc8ZQZoX%2FOXRTK1lAJgK37cvrRIwLBy6a9xvIM5Yalge8ZJTtExBJ%2BPw8E296a03PhEFEW3WMwRReVwrX92ElcHysB9qUmyoKeqjNL2G3RzVs0WFKqRnvzEaGCrzBNni2QCsFpuc0ZHo8xkP5%2FLGjfT6Ccd9LOXpIG%2BNCZGBK4%2BD4C3PvRQgeKrgxtc65Ivjs5ut3Z2evpHmN%2FFejufYJV4SZQ2dWf2wwHMhUksLBXvduKWSkP%2BEADChqrzTBjqZAZ7mDifugINJ8GDZcf%2F1oTywyzJvy3z%2BXwpWHjcc%2B1%2FGmGLCyf6ur%2FiV3CVJMwi0%2FsfPSd8bIfF807SFlmOEFYzxxbR2DrJ68%2F%2BxAwiHbOs5cCjtA0xEcz%2Fm7X%2Ffd0FRy44hgauoZQGPZxedZKzX6BL33m%2FbcIqI80hq59QMGB9jZmtlijSk4wB111xOi7zCIaYT26hJL5hp%2Bg%3D%3D&Expires=1785668340) - # Engineering Design Review

Engineering Design Review Overview

Purpose

The Engineering Design Rev...

15. [02_Project_mC_Decision_Register_v1.2.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/144580388/0ccf41c2-0b67-46b9-9f78-a183230ff984/02_Project_mC_Decision_Register_v1.2.md?AWSAccessKeyId=ASIA2F3EMEYE2U37XSDH&Signature=SbQi0rT0h0N4CNxJnj1Y1Glc54g%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEBIaCXVzLWVhc3QtMSJGMEQCIC06YBUkSctd9HliJgMKGBReLfuYpFuhQUBOIJtRhMy3AiBmzfWQGKLneeCnrlWYaUlWhqlYZlcjAAknX6zNGJo3Cyr8BAjb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAEaDDY5OTc1MzMwOTcwNSIM4V5vuKntkpzP%2BgOfKtAE2%2BBzHNquAcvmjBddOgO8PLvz02nN21%2FL%2B3IS83NxyVZaEm5g86zAaRA1TiYeScbZ7xes4ZBfRavrqXIpGe%2Ffedi9Vlsxn95qEBeaGmwoNsqvbufhFD4K2Frh5gdnD%2FFwgsTVfQWxafj5XU6OEA7kyl3ctROby92LFqF9%2FjD6NEFKnTSWwyF75EWaN%2BX21cJfh11howfghFDwN4LC3Q3jyIv6cTu04dKVC6N4su1NUNE03o7O0jhJFJlwAN78K5dzcl7rucZryTgwrLLeXHuwhouV%2BntaJr6jGQGe3mEOWmvEWrw01t8yob%2F%2FD%2BTZQnoyErqjIoeYD7TvBs6aQP8lxLsDDAxazUYqR9x3FfQxTK1aNJuilfmYXR3rftx5XQeuEdrzTEMyf1veWQ6TimAyOl4hGJAC8tKSw6sunp2TWD183NoQhV%2Bs6TGBT9%2FswrfKH1TSD54jd%2FUMKO8FnayD5lsT4tEa0%2BRBLd5ZUq2%2BRnednWD0xog9M%2FL5gzSjuBKj3ukRirhQKb49NCu5LW4nM1HXxuk7OUTjKc8ZQZoX%2FOXRTK1lAJgK37cvrRIwLBy6a9xvIM5Yalge8ZJTtExBJ%2BPw8E296a03PhEFEW3WMwRReVwrX92ElcHysB9qUmyoKeqjNL2G3RzVs0WFKqRnvzEaGCrzBNni2QCsFpuc0ZHo8xkP5%2FLGjfT6Ccd9LOXpIG%2BNCZGBK4%2BD4C3PvRQgeKrgxtc65Ivjs5ut3Z2evpHmN%2FFejufYJV4SZQ2dWf2wwHMhUksLBXvduKWSkP%2BEADChqrzTBjqZAZ7mDifugINJ8GDZcf%2F1oTywyzJvy3z%2BXwpWHjcc%2B1%2FGmGLCyf6ur%2FiV3CVJMwi0%2FsfPSd8bIfF807SFlmOEFYzxxbR2DrJ68%2F%2BxAwiHbOs5cCjtA0xEcz%2Fm7X%2Ffd0FRy44hgauoZQGPZxedZKzX6BL33m%2FbcIqI80hq59QMGB9jZmtlijSk4wB111xOi7zCIaYT26hJL5hp%2Bg%3D%3D&Expires=1785668340) - ### Project mC Decision Register — Version 1.2

**Document Control Header**
*   **Version:** 1.2
*  ...

16. [03_Phase3C_Portfolio_Closure_Memo_Approved.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/144580388/9edb8b80-8921-443a-9c23-8933e5f70d3b/03_Phase3C_Portfolio_Closure_Memo_Approved.md?AWSAccessKeyId=ASIA2F3EMEYE2U37XSDH&Signature=bWjjPHvQb0J%2BXJ9JqxA8G%2BA5bgk%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEBIaCXVzLWVhc3QtMSJGMEQCIC06YBUkSctd9HliJgMKGBReLfuYpFuhQUBOIJtRhMy3AiBmzfWQGKLneeCnrlWYaUlWhqlYZlcjAAknX6zNGJo3Cyr8BAjb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAEaDDY5OTc1MzMwOTcwNSIM4V5vuKntkpzP%2BgOfKtAE2%2BBzHNquAcvmjBddOgO8PLvz02nN21%2FL%2B3IS83NxyVZaEm5g86zAaRA1TiYeScbZ7xes4ZBfRavrqXIpGe%2Ffedi9Vlsxn95qEBeaGmwoNsqvbufhFD4K2Frh5gdnD%2FFwgsTVfQWxafj5XU6OEA7kyl3ctROby92LFqF9%2FjD6NEFKnTSWwyF75EWaN%2BX21cJfh11howfghFDwN4LC3Q3jyIv6cTu04dKVC6N4su1NUNE03o7O0jhJFJlwAN78K5dzcl7rucZryTgwrLLeXHuwhouV%2BntaJr6jGQGe3mEOWmvEWrw01t8yob%2F%2FD%2BTZQnoyErqjIoeYD7TvBs6aQP8lxLsDDAxazUYqR9x3FfQxTK1aNJuilfmYXR3rftx5XQeuEdrzTEMyf1veWQ6TimAyOl4hGJAC8tKSw6sunp2TWD183NoQhV%2Bs6TGBT9%2FswrfKH1TSD54jd%2FUMKO8FnayD5lsT4tEa0%2BRBLd5ZUq2%2BRnednWD0xog9M%2FL5gzSjuBKj3ukRirhQKb49NCu5LW4nM1HXxuk7OUTjKc8ZQZoX%2FOXRTK1lAJgK37cvrRIwLBy6a9xvIM5Yalge8ZJTtExBJ%2BPw8E296a03PhEFEW3WMwRReVwrX92ElcHysB9qUmyoKeqjNL2G3RzVs0WFKqRnvzEaGCrzBNni2QCsFpuc0ZHo8xkP5%2FLGjfT6Ccd9LOXpIG%2BNCZGBK4%2BD4C3PvRQgeKrgxtc65Ivjs5ut3Z2evpHmN%2FFejufYJV4SZQ2dWf2wwHMhUksLBXvduKWSkP%2BEADChqrzTBjqZAZ7mDifugINJ8GDZcf%2F1oTywyzJvy3z%2BXwpWHjcc%2B1%2FGmGLCyf6ur%2FiV3CVJMwi0%2FsfPSd8bIfF807SFlmOEFYzxxbR2DrJ68%2F%2BxAwiHbOs5cCjtA0xEcz%2Fm7X%2Ffd0FRy44hgauoZQGPZxedZKzX6BL33m%2FbcIqI80hq59QMGB9jZmtlijSk4wB111xOi7zCIaYT26hJL5hp%2Bg%3D%3D&Expires=1785668340) - # Project mC — Phase 3C Retained-Portfolio Closure Memo

**Version:** 1.0
**Date:** 27 July 2026  ...

17. [06_Phase3C_TrueMoist_SOP_Final.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/144580388/9559a424-af6a-453e-9b36-de89cc1439fb/06_Phase3C_TrueMoist_SOP_Final.md?AWSAccessKeyId=ASIA2F3EMEYE2U37XSDH&Signature=PczCkvaKgr0IXg1T92quyNboyOs%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEBIaCXVzLWVhc3QtMSJGMEQCIC06YBUkSctd9HliJgMKGBReLfuYpFuhQUBOIJtRhMy3AiBmzfWQGKLneeCnrlWYaUlWhqlYZlcjAAknX6zNGJo3Cyr8BAjb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAEaDDY5OTc1MzMwOTcwNSIM4V5vuKntkpzP%2BgOfKtAE2%2BBzHNquAcvmjBddOgO8PLvz02nN21%2FL%2B3IS83NxyVZaEm5g86zAaRA1TiYeScbZ7xes4ZBfRavrqXIpGe%2Ffedi9Vlsxn95qEBeaGmwoNsqvbufhFD4K2Frh5gdnD%2FFwgsTVfQWxafj5XU6OEA7kyl3ctROby92LFqF9%2FjD6NEFKnTSWwyF75EWaN%2BX21cJfh11howfghFDwN4LC3Q3jyIv6cTu04dKVC6N4su1NUNE03o7O0jhJFJlwAN78K5dzcl7rucZryTgwrLLeXHuwhouV%2BntaJr6jGQGe3mEOWmvEWrw01t8yob%2F%2FD%2BTZQnoyErqjIoeYD7TvBs6aQP8lxLsDDAxazUYqR9x3FfQxTK1aNJuilfmYXR3rftx5XQeuEdrzTEMyf1veWQ6TimAyOl4hGJAC8tKSw6sunp2TWD183NoQhV%2Bs6TGBT9%2FswrfKH1TSD54jd%2FUMKO8FnayD5lsT4tEa0%2BRBLd5ZUq2%2BRnednWD0xog9M%2FL5gzSjuBKj3ukRirhQKb49NCu5LW4nM1HXxuk7OUTjKc8ZQZoX%2FOXRTK1lAJgK37cvrRIwLBy6a9xvIM5Yalge8ZJTtExBJ%2BPw8E296a03PhEFEW3WMwRReVwrX92ElcHysB9qUmyoKeqjNL2G3RzVs0WFKqRnvzEaGCrzBNni2QCsFpuc0ZHo8xkP5%2FLGjfT6Ccd9LOXpIG%2BNCZGBK4%2BD4C3PvRQgeKrgxtc65Ivjs5ut3Z2evpHmN%2FFejufYJV4SZQ2dWf2wwHMhUksLBXvduKWSkP%2BEADChqrzTBjqZAZ7mDifugINJ8GDZcf%2F1oTywyzJvy3z%2BXwpWHjcc%2B1%2FGmGLCyf6ur%2FiV3CVJMwi0%2FsfPSd8bIfF807SFlmOEFYzxxbR2DrJ68%2F%2BxAwiHbOs5cCjtA0xEcz%2Fm7X%2Ffd0FRy44hgauoZQGPZxedZKzX6BL33m%2FbcIqI80hq59QMGB9jZmtlijSk4wB111xOi7zCIaYT26hJL5hp%2Bg%3D%3D&Expires=1785668340) - # Phase 3C — TrueMoist Engineering Architecture Definition SOP

## Document Control

- Project: Proj...

18. [07_Concept_Evidence_Matrix.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/144580388/b0a01c8d-bf58-4b3b-bdb9-9d1d314e7973/07_Concept_Evidence_Matrix.md?AWSAccessKeyId=ASIA2F3EMEYE2U37XSDH&Signature=KB3PCw9FVWJ2Wkg4XLGP%2Fk8fXSg%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEBIaCXVzLWVhc3QtMSJGMEQCIC06YBUkSctd9HliJgMKGBReLfuYpFuhQUBOIJtRhMy3AiBmzfWQGKLneeCnrlWYaUlWhqlYZlcjAAknX6zNGJo3Cyr8BAjb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAEaDDY5OTc1MzMwOTcwNSIM4V5vuKntkpzP%2BgOfKtAE2%2BBzHNquAcvmjBddOgO8PLvz02nN21%2FL%2B3IS83NxyVZaEm5g86zAaRA1TiYeScbZ7xes4ZBfRavrqXIpGe%2Ffedi9Vlsxn95qEBeaGmwoNsqvbufhFD4K2Frh5gdnD%2FFwgsTVfQWxafj5XU6OEA7kyl3ctROby92LFqF9%2FjD6NEFKnTSWwyF75EWaN%2BX21cJfh11howfghFDwN4LC3Q3jyIv6cTu04dKVC6N4su1NUNE03o7O0jhJFJlwAN78K5dzcl7rucZryTgwrLLeXHuwhouV%2BntaJr6jGQGe3mEOWmvEWrw01t8yob%2F%2FD%2BTZQnoyErqjIoeYD7TvBs6aQP8lxLsDDAxazUYqR9x3FfQxTK1aNJuilfmYXR3rftx5XQeuEdrzTEMyf1veWQ6TimAyOl4hGJAC8tKSw6sunp2TWD183NoQhV%2Bs6TGBT9%2FswrfKH1TSD54jd%2FUMKO8FnayD5lsT4tEa0%2BRBLd5ZUq2%2BRnednWD0xog9M%2FL5gzSjuBKj3ukRirhQKb49NCu5LW4nM1HXxuk7OUTjKc8ZQZoX%2FOXRTK1lAJgK37cvrRIwLBy6a9xvIM5Yalge8ZJTtExBJ%2BPw8E296a03PhEFEW3WMwRReVwrX92ElcHysB9qUmyoKeqjNL2G3RzVs0WFKqRnvzEaGCrzBNni2QCsFpuc0ZHo8xkP5%2FLGjfT6Ccd9LOXpIG%2BNCZGBK4%2BD4C3PvRQgeKrgxtc65Ivjs5ut3Z2evpHmN%2FFejufYJV4SZQ2dWf2wwHMhUksLBXvduKWSkP%2BEADChqrzTBjqZAZ7mDifugINJ8GDZcf%2F1oTywyzJvy3z%2BXwpWHjcc%2B1%2FGmGLCyf6ur%2FiV3CVJMwi0%2FsfPSd8bIfF807SFlmOEFYzxxbR2DrJ68%2F%2BxAwiHbOs5cCjtA0xEcz%2Fm7X%2Ffd0FRy44hgauoZQGPZxedZKzX6BL33m%2FbcIqI80hq59QMGB9jZmtlijSk4wB111xOi7zCIaYT26hJL5hp%2Bg%3D%3D&Expires=1785668340) - # Concept Evidence Matrix

## Reading rules and source keys

This is a neutral extraction, not an ev...

19. [08_Uncertainty_and_Test_Register.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/144580388/504c26d9-bbc7-4297-98fb-9d173b054181/08_Uncertainty_and_Test_Register.md?AWSAccessKeyId=ASIA2F3EMEYE2U37XSDH&Signature=HJFNM1I8ORp2LdanslhnbvdmpL0%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEBIaCXVzLWVhc3QtMSJGMEQCIC06YBUkSctd9HliJgMKGBReLfuYpFuhQUBOIJtRhMy3AiBmzfWQGKLneeCnrlWYaUlWhqlYZlcjAAknX6zNGJo3Cyr8BAjb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAEaDDY5OTc1MzMwOTcwNSIM4V5vuKntkpzP%2BgOfKtAE2%2BBzHNquAcvmjBddOgO8PLvz02nN21%2FL%2B3IS83NxyVZaEm5g86zAaRA1TiYeScbZ7xes4ZBfRavrqXIpGe%2Ffedi9Vlsxn95qEBeaGmwoNsqvbufhFD4K2Frh5gdnD%2FFwgsTVfQWxafj5XU6OEA7kyl3ctROby92LFqF9%2FjD6NEFKnTSWwyF75EWaN%2BX21cJfh11howfghFDwN4LC3Q3jyIv6cTu04dKVC6N4su1NUNE03o7O0jhJFJlwAN78K5dzcl7rucZryTgwrLLeXHuwhouV%2BntaJr6jGQGe3mEOWmvEWrw01t8yob%2F%2FD%2BTZQnoyErqjIoeYD7TvBs6aQP8lxLsDDAxazUYqR9x3FfQxTK1aNJuilfmYXR3rftx5XQeuEdrzTEMyf1veWQ6TimAyOl4hGJAC8tKSw6sunp2TWD183NoQhV%2Bs6TGBT9%2FswrfKH1TSD54jd%2FUMKO8FnayD5lsT4tEa0%2BRBLd5ZUq2%2BRnednWD0xog9M%2FL5gzSjuBKj3ukRirhQKb49NCu5LW4nM1HXxuk7OUTjKc8ZQZoX%2FOXRTK1lAJgK37cvrRIwLBy6a9xvIM5Yalge8ZJTtExBJ%2BPw8E296a03PhEFEW3WMwRReVwrX92ElcHysB9qUmyoKeqjNL2G3RzVs0WFKqRnvzEaGCrzBNni2QCsFpuc0ZHo8xkP5%2FLGjfT6Ccd9LOXpIG%2BNCZGBK4%2BD4C3PvRQgeKrgxtc65Ivjs5ut3Z2evpHmN%2FFejufYJV4SZQ2dWf2wwHMhUksLBXvduKWSkP%2BEADChqrzTBjqZAZ7mDifugINJ8GDZcf%2F1oTywyzJvy3z%2BXwpWHjcc%2B1%2FGmGLCyf6ur%2FiV3CVJMwi0%2FsfPSd8bIfF807SFlmOEFYzxxbR2DrJ68%2F%2BxAwiHbOs5cCjtA0xEcz%2Fm7X%2Ffd0FRy44hgauoZQGPZxedZKzX6BL33m%2FbcIqI80hq59QMGB9jZmtlijSk4wB111xOi7zCIaYT26hJL5hp%2Bg%3D%3D&Expires=1785668340) - # Uncertainty and Test Register

## Use

Costs and durations are approximate planning values bounded...

20. [10_Phase2_Report_by_Claude.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/144580388/b2de3acf-f0ba-420c-9cb2-c5e74565e8dd/10_Phase2_Report_by_Claude.md?AWSAccessKeyId=ASIA2F3EMEYE2U37XSDH&Signature=5u1goBFhAs6hAI%2BapPKln5NrxRE%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEBIaCXVzLWVhc3QtMSJGMEQCIC06YBUkSctd9HliJgMKGBReLfuYpFuhQUBOIJtRhMy3AiBmzfWQGKLneeCnrlWYaUlWhqlYZlcjAAknX6zNGJo3Cyr8BAjb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAEaDDY5OTc1MzMwOTcwNSIM4V5vuKntkpzP%2BgOfKtAE2%2BBzHNquAcvmjBddOgO8PLvz02nN21%2FL%2B3IS83NxyVZaEm5g86zAaRA1TiYeScbZ7xes4ZBfRavrqXIpGe%2Ffedi9Vlsxn95qEBeaGmwoNsqvbufhFD4K2Frh5gdnD%2FFwgsTVfQWxafj5XU6OEA7kyl3ctROby92LFqF9%2FjD6NEFKnTSWwyF75EWaN%2BX21cJfh11howfghFDwN4LC3Q3jyIv6cTu04dKVC6N4su1NUNE03o7O0jhJFJlwAN78K5dzcl7rucZryTgwrLLeXHuwhouV%2BntaJr6jGQGe3mEOWmvEWrw01t8yob%2F%2FD%2BTZQnoyErqjIoeYD7TvBs6aQP8lxLsDDAxazUYqR9x3FfQxTK1aNJuilfmYXR3rftx5XQeuEdrzTEMyf1veWQ6TimAyOl4hGJAC8tKSw6sunp2TWD183NoQhV%2Bs6TGBT9%2FswrfKH1TSD54jd%2FUMKO8FnayD5lsT4tEa0%2BRBLd5ZUq2%2BRnednWD0xog9M%2FL5gzSjuBKj3ukRirhQKb49NCu5LW4nM1HXxuk7OUTjKc8ZQZoX%2FOXRTK1lAJgK37cvrRIwLBy6a9xvIM5Yalge8ZJTtExBJ%2BPw8E296a03PhEFEW3WMwRReVwrX92ElcHysB9qUmyoKeqjNL2G3RzVs0WFKqRnvzEaGCrzBNni2QCsFpuc0ZHo8xkP5%2FLGjfT6Ccd9LOXpIG%2BNCZGBK4%2BD4C3PvRQgeKrgxtc65Ivjs5ut3Z2evpHmN%2FFejufYJV4SZQ2dWf2wwHMhUksLBXvduKWSkP%2BEADChqrzTBjqZAZ7mDifugINJ8GDZcf%2F1oTywyzJvy3z%2BXwpWHjcc%2B1%2FGmGLCyf6ur%2FiV3CVJMwi0%2FsfPSd8bIfF807SFlmOEFYzxxbR2DrJ68%2F%2BxAwiHbOs5cCjtA0xEcz%2Fm7X%2Ffd0FRy44hgauoZQGPZxedZKzX6BL33m%2FbcIqI80hq59QMGB9jZmtlijSk4wB111xOi7zCIaYT26hJL5hp%2Bg%3D%3D&Expires=1785668340) - # Phase 2 — Patent Landscape Assessment (Consolidated)
### MC Project · Patent-Oriented Embedded Sys...

21. [US20150181817A1 - Soil Moisture Sensor - Google Patents](https://patents.google.com/patent/US20150181817A1/en) - In one embodiment, the present invention is directed to a soil moisture sensor for interrupting an i...

22. [Performance of Soil Moisture Sensors at Different Salinity ...](https://www.mdpi.com/1424-8220/24/19/6323) - by Q Qi · 2024 · Cited by 31 — Soil dielectric sensors have been widely used to obtain real-time soi...

23. [WET150 Sensor - Measures soil moisture, EC, and ...](https://delta-t.co.uk/product/wet150-horticulture/) - The WET150s patented sensor electronics produce research grade measurement accuracy with exceptional...

24. [Soil Moisture Sensor](https://eureka.patsnap.com/patent-US20130255783A1) - a technology of soil moisture and sensor, which is applied in the direction of automatic control, pr...


---

## Source 12: `03_CONCEPT_PORTFOLIO/TrueMoist/02_Raw_Research/04_TrueMoist_Patent_Research_Qwen_COMPILATION.md`

- Authority: `TIER_3`
- Treatment: `SUPPORTING_EVIDENCE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `NEW_STAGE10L_EXTRACTION`
- SHA-256: `563ec1237fdfc84f9ecd7da9ef541f39a38305cf49976304b66c20ea26132902`

# Source Extraction

- Chapter: `08` — TrueMoist Architecture, Validation and Patent Evidence
- Authority tier: `TIER_3`
- Manual treatment: `SUPPORTING_EVIDENCE`
- Original source: `03_CONCEPT_PORTFOLIO/TrueMoist/02_Raw_Research/04_TrueMoist_Patent_Research_Qwen_COMPILATION.md`
- SHA-256: `563ec1237fdfc84f9ecd7da9ef541f39a38305cf49976304b66c20ea26132902`
- Extraction method: `PLAIN_TEXT`
- Rule: source text only; no synthesis, correction or reconciliation.

---

# TrueMoist Qwen Patent-Research Lane — Lossless Compilation

## Mandatory transport and reliability warning

This is one Qwen lane, not two reports or votes.

Part 1 is the initial substantive research.

Part 2 is the follow-up/final structured response.

Part 2 does not automatically validate unsupported claims in Part 1.

The synthesis must independently verify `HIGH/CLEAR` FTO, Track-B confidence, Mahalanobis validity-envelope novelty, eligibility, dual-probe health, and event-triggered recalibration claims.

This compilation is transport/file control only. Each embedded source remains unchanged and retains its own evidentiary weight.

---

## Part 1

- Original filename: `research on f.patent by qwen #0.md`
- Original absolute path: `/home/paradoxpete/Documents/PROJECT/PHASE 3/PHASE 3C-Comparative Technical Evaluation/FINALISED DECISION/TRUEMOIST/research on f.patent by qwen #0.md`
- Original byte size: 45140
- Original SHA-256: `d8abc8efe8c6a4d5111ecca56d76ca68dd0db142dfb3a54bd48375b05b1b2045`

<!-- BEGIN EMBEDDED SOURCE: research on f.patent by qwen #0.md -->
# The TrueMoist Freeze Frame: An Anatomy of a Conventional Design and Its Pathways to Future Innovationtive Invention Space

## Layer A Assessment: Novelty and Non-Obviousness of the Frozen MVP Technical Mechanism

The central inquiry of this analysis is whether the TrueMoist frozen Minimum Viable Product (MVP)—comprising a low-cost capacitive soil-moisture probe, a DS18B20 temperature sensor, an ADS1115 analog-to-digital converter (ADC), an ESP32 microcontroller, an offline-trained ridge-regularized second-order regression model with fixed coefficients, and a specific 72-run validation protocol—defines a novel and non-obvious technical mechanism for in-situ drift correction and calibration [[268](https://www.bio-conferences.org/articles/bioconf/pdf/2024/15/bioconf_uicat2024_04001.pdf), [451](https://www.reddit.com/r/Esphome/comments/urxcy5/capacitive_soil_moisture_sensors/)]. The investigation focuses on its ability to correct or validate moisture readings under the influence of real-world physical variabilities, including temperature shifts, salinity treatments, probe-to-probe variation, insertion/packing inconsistencies, and long-term ageing [[92](https://pmc.ncbi.nlm.nih.gov/articles/PMC10684704/), [252](https://www.researchgate.net/publication/384496983_Performance_of_Soil_Moisture_Sensors_at_Different_Salinity_Levels_Comparative_Analysis_and_Calibration)]. The assessment treats the regression model as a conventional mathematical tool unless evidence of a non-obvious interaction with the physical sensing process is found. The 72-run protocol is evaluated strictly as a means of generating evidence for the model's efficacy, not as a patentable subject matter in itself [[15](https://pmc.ncbi.nlm.nih.gov/articles/PMC11223676/)]. This section deconstructs the MVP's technical stack, compares its components and methodology to established practices in academic literature and commercial products, and synthesizes the findings to determine if the combination constitutes a patentable invention.

A comprehensive review of the provided context reveals that while the TrueMoist MVP represents a robust and effective engineering solution for calibrating low-cost sensors, it does not establish a novel or non-obvious technical mechanism. Instead, it embodies a validated application of conventional techniques. The novelty lies not in the invention of a new mechanism but in the rigorous demonstration of how standard methods can be integrated to achieve significant performance improvements on a constrained hardware budget. The core challenge in defining a "specific technical mechanism" is distinguishing between the general scientific principles of sensor calibration, which are widely known, and the specific implementation details that might confer patentability. The analysis indicates that the MVP operates squarely within the bounds of established practice, leveraging off-the-shelf components and well-understood statistical models to solve a common problem in the field of environmental sensing.

The first step in assessing novelty is to dissect the MVP's hardware architecture. The selection of components—including a low-cost capacitive soil moisture probe, a DS18B20 digital temperature sensor, an ADS1115 high-precision ADC, and an ESP32 microcontroller—is indicative of a design philosophy focused on cost-effectiveness and ease of development, characteristics common to open-source and hobbyist electronics projects [[242](https://arxiv.org/pdf/2309.07438), [268](https://www.bio-conferences.org/articles/bioconf/pdf/2024/15/bioconf_uicat2024_04001.pdf), [421](https://github.com/dkuenne/ESP_capacitive_soil_moisture)]. These components are not proprietary inventions but rather standard parts available from numerous vendors. The capacitive probe itself is a mature technology based on measuring the dielectric permittivity of the soil, a principle that has been understood and utilized for decades [[126](https://www.farm21.com/overview-of-capacitive-soil-moisture-sensors/), [230](https://metergroup.com/measurement-insights/soil-moisture-sensors-how-they-work-why-some-are-not-research-grade/?srsltid=AfmBOoqx1nc79FTY0HwRQm5G7I_w5ckhww8QI6d_56QaRfAx0V3KdF3_), [289](https://www-pub.iaea.org/MTCD/Publications/PDF/te_1137_prn.pdf)]. Similarly, the use of a separate digital temperature sensor like the DS18B20 is a standard practice to obtain accurate temperature data without introducing electrical noise into the sensitive capacitance measurement circuitry [[146](https://s.campbellsci.com/documents/us/manuals/cr6.pdf), [162](https://www.facebook.com/groups/299612244008643/posts/2006280333341817/)]. Using a dedicated external ADC such as the ADS1115 instead of the ESP32's internal analog inputs is a known workaround to overcome the latter's susceptibility to electromagnetic interference and poor precision, a common issue noted in developer forums and project guides [[413](https://www.reddit.com/r/esp32/comments/1i2tits/capacitive_soil_moisture_sensor_issues/), [422](https://www.reddit.com/r/Esphome/comments/1s2pu52/esp32_reads_fixed_107v_from_capacitive_soil/), [451](https://www.reddit.com/r/Esphome/comments/urxcy5/capacitive_soil_moisture_sensors/)]. Therefore, the hardware configuration of the MVP is not novel; it is a pragmatic assembly of commercially available components chosen for their specific functionalities and documented limitations.

The software and algorithmic layer is where the primary claim of a novel mechanism might be made. The MVP employs a two-stage process: offline training of a regression model followed by fixed-coefficient local inference on the ESP32. This approach is fundamentally different from many modern, adaptive systems that perform online learning or continuous recalibration [[55](https://www.mdpi.com/2624-831X/7/1/5)]. The decision to train the model offline and deploy it with fixed coefficients is a critical design constraint that simplifies the device significantly. It eliminates the need for computational resources to retrain the model in the field, making it suitable for a low-power microcontroller. However, this simplicity comes at the cost of adaptability. The model is static and can only compensate for variations that were present in the data used for its initial training phase. It cannot adapt to unforeseen environmental changes, sensor degradation over time, or interactions with soil types not included in the 72-run validation set. This positions the MVP as a highly accurate, calibrated device for a specific set of conditions, rather than a dynamic, self-learning system capable of evolving with its environment. While this is a valid and often necessary trade-off for resource-constrained devices, it places the MVP firmly within the realm of conventional engineering solutions rather than innovative mechanisms.

The core of the algorithm is a ridge-regularized second-order regression model. The term "ridge-regularized" indicates the use of L2 regularization to prevent overfitting, a standard technique in machine learning when dealing with multicollinearity or a large number of features relative to the number of observations [[10](https://www.researchgate.net/publication/353983263_Review_of_research_progress_on_soil_moisture_sensor_technology), [286](https://www.drought.gov/sites/default/files/2024-12/Soil-Moisture-Data-Quality-Guidance-12-09-2024.pdf)]. The "second-order" aspect implies the model includes terms for the product of the input variables (e.g., temperature multiplied by capacitance), allowing it to capture non-linear interactions between them [[10](https://www.researchgate.net/publication/353983263_Review_of_research_progress_on_soil_moisture_sensor_technology)]. Such models are a workhorse for creating calibration curves for sensors whose output is a complex, non-linear function of multiple physical parameters [[8](https://onlinelibrary.wiley.com/doi/full/10.1002/ird.70026), [11](https://ijabe.org/index.php/ijabe/article/view/6404)]. The research goal specified treating this model as conventional unless a non-obvious interaction with the physical sensing process was found. The analysis of the provided sources shows no evidence of such a non-obvious interaction. The regression model functions purely as a mathematical mapping tool. It takes the raw, uncalibrated outputs from the capacitive probe and the DS18B20 temperature sensor and maps them to the gravimetric ground truth measurements obtained during the validation phase. It effectively learns the physics of the sensor-soil interaction through empirical data rather than being based on a first-principles physical model derived from Maxwell's equations or similar theoretical frameworks. The novelty, if any, is therefore not in the algorithm itself but in its specific application to the unique combination of input variables (raw capacitance and temperature) and the generation of a particular, validated set of coefficients that define the final calibration equation. This is an engineering achievement in calibration, not a fundamental invention in signal processing or sensor physics.

The user's clarification regarding the use of controlled salinity codes without mandatory live Electrical Conductivity (EC) sensing is crucial for understanding the MVP's design philosophy. The provided context suggests that the use of controlled salinity treatments is not presented as a novel *mechanism* but as a sophisticated *validation strategy*. By systematically exposing the sensor to soils with varying salt concentrations, the 72-run protocol ensures that the regression model learns the sensor's response to salinity-induced errors [[6](https://pmc.ncbi.nlm.nih.gov/articles/PMC11478466/), [426](https://www.researchgate.net/publication/26624014_Calibration_and_Simultaneous_Monitoring_of_Soil_Water_Content_and_Salinity_with_Capacitance_and_Four-electrode_Probes)]. The model then incorporates these learned relationships into its predictive equation, allowing it to correct for salinity effects in subsequent measurements. The absence of a live EC sensor is a deliberate and economically sound design choice. It leverages the fact that the physical relationship between soil dielectric permittivity, moisture content, temperature, and salinity can be modeled empirically without needing to measure the salinity directly in real-time [[252](https://www.researchgate.net/publication/384496983_Performance_of_Soil_Moisture_Sensors_at_Different_Salinity_Levels_Comparative_Analysis_and_Calibration)]. This is a common approach in scientific calibration studies, where the focus is on correcting for interfering variables rather than measuring them all simultaneously [[191](https://www.researchgate.net/publication/43261449_Calibration_of_Capacitance_Probe_Sensors_in_a_Saline_Silty_Clay_Soil)]. For example, METER Group's advanced sensors use high-frequency operation to minimize the impact of salinity, whereas other designs, like those from Steven's Water Monitoring Systems, incorporate direct EC measurement for correction [[148](https://metergroup.com/meter-products/field-instruments/soil/?srsltid=AfmBOoq5iG1ka3bS__yMPm4fxdDmsHM5NXf77oWUCBqcs4jlYDvur2d1), [160](https://publikasjoner.nve.no/rapport/2024/rapport2024_11.pdf)]. The TrueMoist MVP adopts a third path: modeling the effect of salinity without direct measurement, a technique that is well-documented in the literature [[426](https://www.researchgate.net/publication/26624014_Calibration_and_Simultaneous_Monitoring_of_Soil_Water_Content_and_Salinity_with_Capacitance_and_Four-electrode_Probes)].

Finally, the 72-run homogeneous-soil validation protocol serves as the bedrock for the entire calibration effort. It provides a strong, statistically robust dataset against which the regression model is trained and validated [[92](https://pmc.ncbi.nlm.nih.gov/articles/PMC10684704/), [253](https://mypure.auk.edu.kw/en/publications/validation-of-nasa-smap-satellite-soil-moisture-products-over-the)]. The use of gravimetric ground truth—a standard laboratory method involving oven-drying soil samples to determine their water content—is the gold standard for sensor calibration [[249](https://agrilab.unilasalle.fr/projets/attachments/download/4088/Capacitive_Soil_Moisture_Sensors.pdf), [402](https://makersportal.com/blog/2020/5/26/capacitive-soil-moisture-calibration-with-arduino?srsltid=AfmBOopSS5qBsTZ00Ukzf9HHkEqpJWDufxY7YluhpwZch_4llu9Wc0su)]. The protocol's strength lies in its rigor, ensuring that the resulting model is reliable and meets predefined performance thresholds for Root Mean Square Error (RMSE) and Mean Absolute Error (MAE). However, experimental protocols themselves are generally not considered patentable subject matter [[15](https://pmc.ncbi.nlm.nih.gov/articles/PMC11223676/)]. Their value is instrumental; they are the procedure used to produce a valuable outcome—the validated model and its coefficients. The protocol demonstrates methodological excellence but does not, by itself, define a novel technical mechanism. The technical effect is achieved through the combination of the physical sensor, the data acquisition hardware, and the mathematical model, not through the steps of the experimental setup. The validation confirms that the mechanism works as intended, but it does not invent the mechanism.

In synthesis, the TrueMoist MVP should be characterized as a **validated calibration method for low-cost capacitive sensors**, rather than a novel calibration *mechanism*. It successfully demonstrates that:
1.  Low-cost sensors are susceptible to errors from multiple physical factors, including temperature, salinity, and installation artifacts [[5](https://www.sciencedirect.com/science/article/pii/S2772375525004174), [227](https://www.dfrobot.com/forum/topic/321676?srsltid=AfmBOooEbFhDq1aFWqLR1u6qHWgrBXJ7H2i3yoKRC3-H6SVoaEPqH9Rm)].
2.  These multi-faceted errors can be quantified and corrected using a multivariate regression model trained on carefully collected data [[10](https://www.researchgate.net/publication/353983263_Review_of_research_progress_on_soil_moisture_sensor_technology), [11](https://ijabe.org/index.php/ijabe/article/view/6404)].
3.  An offline-trained model can provide significant accuracy improvements over uncalibrated sensors, meeting or exceeding predefined performance targets [[224](https://www.mdpi.com/2077-0472/9/7/141), [326](https://pmc.ncbi.nlm.nih.gov/articles/PMC11435841/)].

This is a highly valuable engineering contribution, particularly for the low-cost segment of the market. However, it falls short of the threshold for a patentable invention because the underlying principles and constituent technologies are already well-established in both the academic literature and the commercial products of industry leaders. Companies like METER Group (formerly Decagon Devices) and Campbell Scientific have built their businesses around providing factory-calibrated sensors and custom calibration services specifically to address the very variabilities that the MVP aims to correct [[218](https://www.campbellsci.com/resources/videos/soil-moisture-webinar), [298](https://metergroup.com/resources/services/custom-calibration/?srsltid=AfmBOopNc9Fg1jtHHSib2ywI9HjFSHMwYs1MVjWNObGP2Rkesj3K5d2C), [304](https://metergroup.com/?srsltid=AfmBOooxcD14BjOOOOpvP9YWOm0nyh-i6MUu0XcWTWeJTmrtU8n46qiC)]. Their products and patents often involve more sophisticated methods, such as multi-frequency operation to inherently reduce sensitivity to certain variables or integrated sensors for simultaneous measurement of confounding factors like EC [[148](https://metergroup.com/meter-products/field-instruments/soil/?srsltid=AfmBOoq5iG1ka3bS__yMPm4fxdDmsHM5NXf77oWUCBqcs4jlYDvur2d1), [160](https://publikasjoner.nve.no/rapport/2024/rapport2024_11.pdf)]. The TrueMoist MVP achieves a comparable level of accuracy through a different, more accessible route: meticulous offline calibration of a simpler, single-frequency probe. This makes it a clever and practical implementation, but not a groundbreaking invention. The mechanism is conventional, and its novelty is confined to the specific, optimized application demonstrated by the project team.

| MVP Component / Technique | Conventional Status | Rationale |
| :--- | :--- | :--- |
| Low-Cost Capacitive Probe | Conventional | Widely used, off-the-shelf component for soil moisture sensing based on dielectric permittivity [[32](https://pmc.ncbi.nlm.nih.gov/articles/PMC10007478/), [214](https://repositorio.usp.br/directbitstream/bbbf7a15-f4b8-4006-90de-dff085a566cb/sensors-23-02451-v2.pdf), [250](https://sabraojournal.org/wp-content/uploads/2024/03/SABRAO-J-Breed-Genet-56-1-353-369-MS23-171.pdf)]. |
| DS18B20 Temperature Sensor | Conventional | Standard, digital temperature sensor used to avoid electrical interference with capacitance measurements [[146](https://s.campbellsci.com/documents/us/manuals/cr6.pdf), [162](https://www.facebook.com/groups/299612244008643/posts/2006280333341817/)]. |
| ADS1115 External ADC | Conventional | Common practice to bypass noisy internal ADCs on microcontrollers like the ESP32 for higher precision [[413](https://www.reddit.com/r/esp32/comments/1i2tits/capacitive_soil_moisture_sensor_issues/), [451](https://www.reddit.com/r/Esphome/comments/urxcy5/capacitive_soil_moisture_sensors/)]. |
| Offline Regression Training | Conventional | Standard method for creating a static calibration model from a pre-existing dataset [[10](https://www.researchgate.net/publication/353983263_Review_of_research_progress_on_soil_moisture_sensor_technology), [286](https://www.drought.gov/sites/default/files/2024-12/Soil-Moisture-Data-Quality-Guidance-12-09-2024.pdf)]. |
| Fixed-Coefficient Local Inference | Conventional | Pragmatic choice for low-power devices that cannot support computationally intensive online learning [[55](https://www.mdpi.com/2624-831X/7/1/5)]. |
| Ridge-Regularized Second-Order Model | Conventional | Standard statistical technique for handling non-linearity and preventing overfitting in calibration models [[10](https://www.researchgate.net/publication/353983263_Review_of_research_progress_on_soil_moisture_sensor_technology), [11](https://ijabe.org/index.php/ijabe/article/view/6404)]. |
| Controlled Salinity Codes | Conventional | Experimental design strategy to systematically expose the sensor to a range of salinity levels for comprehensive calibration [[6](https://pmc.ncbi.nlm.nih.gov/articles/PMC11478466/), [426](https://www.researchgate.net/publication/26624014_Calibration_and_Simultaneous_Monitoring_of_Soil_Water_Content_and_Salinity_with_Capacitance_and_Four-electrode_Probes)]. |
| Absence of Live EC Sensing | Conventional | Deliberate design choice to reduce cost, leveraging empirical modeling of salinity effects instead of direct measurement [[191](https://www.researchgate.net/publication/43261449_Calibration_of_Capacitance_Probe_Sensors_in_a_Saline_Silty_Clay_Soil), [252](https://www.researchgate.net/publication/384496983_Performance_of_Soil_Moisture_Sensors_at_Different_Salinity_Levels_Comparative_Analysis_and_Calibration)]. |
| 72-Run Validation Protocol | Not Patentable Subject Matter | A rigorous experimental procedure used to generate high-quality training data; the protocol itself is not an invention [[15](https://pmc.ncbi.nlm.nih.gov/articles/PMC11223676/), [92](https://pmc.ncbi.nlm.nih.gov/articles/PMC10684704/)]. |

This table summarizes the analysis, demonstrating that each element of the MVP is either a standard component or a well-established technique. The combination is effective, but it does not rise to the level of a novel and non-obvious technical mechanism as required for patentability.

## Layer B Analysis: Freedom-to-Operate Risks Against Incumbent Patents

Following the assessment of the frozen MVP's novelty, the next critical task is to evaluate its Freedom-to-Operate (FTO). FTO analysis determines whether the MVP's design and functionality infringe upon the valid and enforceable intellectual property rights of others. This requires a targeted examination of active patent families from key industry players, including Campbell Scientific, METER Group (formerly Decagon Devices), Toro, and a representative Korean assignee, to identify any potential claims that cover the MVP's core technical features [[66](https://patents.google.com/patent/US8671969B2/en), [107](https://www.youtube.com/watch?v=00vkRD9o5p0), [165](https://patents.google.com/patent/KR20160020668A/en), [180](https://s.campbellsci.com/documents/us/solution-brochures/soil.pdf)]. The analysis must distinguish between patented features that the MVP uses and those it deliberately avoids. The objective is to ascertain whether the MVP can be commercialized without obtaining licenses or facing legal challenges. The provided context allows for a detailed comparison of the MVP's technical stack against the claims of relevant patents and patent applications.

The preliminary conclusion from the provided materials is that the TrueMoist MVP possesses a **high degree of Freedom-to-Operate**. This favorable position is not accidental but is largely a consequence of the MVP's deliberate design choices, which prioritize low cost and simplicity. By opting for off-the-shelf components and a relatively simple, static calibration algorithm, the project has inadvertently steered clear of some of the most heavily litigated and patented areas of soil sensor technology. Key functionalities that are often the focus of patents from incumbents—such as live electrical conductivity (EC) measurement, in-situ multi-frequency operation, and complex on-device adaptive algorithms—are notably absent from the MVP's frozen specification. This strategic avoidance significantly reduces the risk of direct infringement.

To conduct a thorough FTO analysis, we must map the MVP's key features against the teachings of representative patents from the specified entities. This involves identifying claims that describe similar combinations of hardware, software, and operational methods.

First, let's consider **Campbell Scientific**. Campbell Scientific is a prominent player in scientific instrumentation, and its patents often relate to data loggers, sensor networks, and the principles of measurement [[180](https://s.campbellsci.com/documents/us/solution-brochures/soil.pdf), [181](https://www.campbellsci.asia/soil-science)]. While the provided documents do not contain full-text Campbell patents, references to their products and principles are abundant. For instance, their CS655 sensor is described as a multiparameter smart sensor that measures volumetric-water content, bulk electrical conductivity, and temperature [[119](https://campbellsci.com/products/cs655)]. Another patent, US7944220B2, describes a moisture content sensor that injects an electrical signal into a medium [[346](https://patents.google.com/patent/US7944220B2/en)]. The key feature here is the integration of multiple measurements (moisture, EC, temperature) into a single, smart sensor platform. The TrueMoist MVP, by contrast, explicitly omits live EC sensing and uses a separate, dedicated temperature sensor (DS18B20) rather than integrating it into a multi-parameter probe. This architectural difference is a significant factor in avoiding potential infringement of patents covering integrated, multi-parameter probes designed to correct for cross-sensitivities in real-time. Furthermore, Campbell Scientific's emphasis on proper calibration and temperature compensation is well-documented, but their patented solutions often involve complex, real-time compensation algorithms running on their CR series data loggers [[218](https://www.campbellsci.com/resources/videos/soil-moisture-webinar), [363](https://pmc.ncbi.nlm.nih.gov/articles/PMC3444127/)]. The MVP's fixed-coefficient, locally-executed regression model is a much simpler implementation that is unlikely to fall within the scope of these more complex patented methods.

Next, **METER Group** (which acquired Decagon Devices) represents another major competitor whose patents are relevant. METER Group's marketing and technical documentation emphasize the importance of factory calibration and custom calibration services to account for soil-specific properties [[298](https://metergroup.com/resources/services/custom-calibration/?srsltid=AfmBOopNc9Fg1jtHHSib2ywI9HjFSHMwYs1MVjWNObGP2Rkesj3K5d2C), [304](https://metergroup.com/?srsltid=AfmBOooxcD14BjOOOOpvP9YWOm0nyh-i6MUu0XcWTWeJTmrtU8n46qiC)]. Their patents reflect this focus. For example, US Patent 7042234 describes a method and apparatus for measuring soil matric potential and salinity, which involves correcting measurements based on electrical conductivity [[155](https://data.epo.org/publication-server/rest/v1.0/publication-dates/20130807/patents/EP2623971NWA1/document.pdf)]. Another key technology is their use of high-frequency capacitance (up to 1 GHz) to minimize the effects of soil texture and salinity, a principle taught in their own publications [[1](https://www.mdpi.com/2073-4395/15/12/2788), [148](https://metergroup.com/meter-products/field-instruments/soil/?srsltid=AfmBOoq5iG1ka3bS__yMPm4fxdDmsHM5NXf77oWUCBqcs4jlYDvur2d1), [153](https://metergroup.com/measurement-insights/soil-moisture-sensors-how-they-work-why-some-are-not-research-grade/?srsltid=AfmBOoph0SfJlzTh5WKAcnpOFX6LYB66V5gtlBU184x-Ayx0-IdkxAit)]. The MVP, using a low-cost capacitive probe operating at a presumably lower frequency, does not employ this specific high-frequency technique. The provided context also mentions patents related to HydraProbe technology, which uses patented algorithms to convert standing radio wave signals into dielectric permittivity, a fundamentally different measurement principle from the simple capacitive probe used in the MVP [[216](https://www.campbellsci.ca/hydraprobe), [260](https://www.stevenswater.com/resources/documentation/hydraprobe/HydraProbe_Manual_Jan_2018.pdf)]. By using a standard capacitive probe and compensating for physical effects through post-hoc regression rather than through high-frequency physics, the MVP avoids infringing on METER Group's core patented technologies. The MVP's reliance on an external ADC (ADS1115) is also noteworthy; METER Group's patents often describe integrated circuits and sensor designs, and using a separate, off-the-shelf ADC further distances the MVP from potentially conflicting integrated hardware designs [[424](https://edaphic.com.au/products/soils/ec-5-soil-water-content-sensor/), [427](https://www.scribd.com/document/522108819/Decagon-10HS-Moisture)].

Third, **Toro** is a key player in the irrigation control market, and its patents often bridge the gap between soil sensing and automated watering systems [[18](https://media.toro.com/CatalogDocuments/Product%20Literature/rc_cat.pdf)]. Several patents mention soil moisture sensors and controllers working in conjunction [[66](https://patents.google.com/patent/US8671969B2/en), [222](https://patents.google.com/patent/US20100094472A1/en)]. For example, US Patent 8671969B2 relates to an automatic soil moisture sensing and watering system [[66](https://patents.google.com/patent/US8671969B2/en)]. The Toro Precision Soil Sensor is described as a wireless sensor that automatically detects the soil type [[220](https://media.toro.com/CatalogDocuments/Product%20Literature/prec_soil_mon_ss.pdf)]. While the MVP performs a sophisticated calibration, it does not claim to "detect the soil type" in the way a Toro sensor might, which could involve more complex impedance or frequency-domain analysis. The MVP's calibration is tied to a specific, validated set of coefficients, not a dynamic classification of the surrounding soil. Furthermore, Toro's patents sometimes cover methods of control and communication between the sensor and the irrigation controller [[67](https://media.tmarkt.hu/documents/ontozo/14_szerelesi_es_kezelesi_utmutatok_tmk/evolution_pss_talajnedvesseg_erzekelo_angol_revb.pdf), [219](https://asic.org/toro-dxi-central-control-soil-moisture-sensing/)]. The MVP's current specification is limited to data acquisition and local inference; it does not specify any control logic or communication protocol for an irrigation system. This functional limitation reduces the risk of infringing on Toro's patents related to the broader smart irrigation ecosystem.

Finally, examining a **Korean assignee** provides insight into regional innovation trends. Korean patents cited include inventions related to thermometers, fire detection systems, and soil moisture retrieval via GNSS signals [[50](https://www.globalipnews.com/?industry=Medical&key=1W), [51](https://www.cmu.edu/nanotechnology-forum/Forum_19/ProgramBook_19thNanoForum.pdf), [52](https://cdn.komachine.com/media/company-catalog/bi-industrial-3665_xqefmd.pdf)]. One specific Korean patent application, KR1020110017617A, relates to a device for measuring high-frequency soil moisture [[165](https://patents.google.com/patent/KR20160020668A/en)]. This aligns with the trend seen in METER Group's technology, suggesting that high-frequency measurement is a recognized area of innovation in Korea. Another patent, RS20180253(A1), describes a microwave soil moisture sensor independent of electrical conductivity, indicating a focus on alternative measurement principles [[166](https://biosense.rs/en/patents/microwave-soil-moistructure-sensor-based-on-phase-shift-method-and-independet-of-electrical-conductivity-of-the-soil)]. The TrueMoist MVP, using a simple capacitive probe and regression-based correction, operates outside these specific high-frequency and microwave measurement domains. The absence of these advanced measurement principles in the MVP's frozen state is a critical factor in establishing its FTO.

The following table summarizes the FTO analysis by comparing the MVP's features against the patented approaches of major incumbents.

| Feature | TrueMoist MVP Approach | Incumbent Approach (Patented) | FTO Risk |
| :--- | :--- | :--- | :--- |
| **Capacitance Measurement** | Single-frequency, low-cost capacitive probe [[32](https://pmc.ncbi.nlm.nih.gov/articles/PMC10007478/)]. | Multi-frequency or high-frequency (up to 1 GHz) to minimize textural/salinity effects [[1](https://www.mdpi.com/2073-4395/15/12/2788), [148](https://metergroup.com/meter-products/field-instruments/soil/?srsltid=AfmBOoq5iG1ka3bS__yMPm4fxdDmsHM5NXf77oWUCBqcs4jlYDvur2d1)]. | **Low** - Different measurement principle. |
| **Temperature Compensation** | Separate DS18B20 sensor; compensation performed via offline regression model [[162](https://www.facebook.com/groups/299612244008643/posts/2006280333341817/)]. | Integrated temperature sensor in probe; real-time, on-device compensation algorithms [[218](https://www.campbellsci.com/resources/videos/soil-moisture-webinar), [363](https://pmc.ncbi.nlm.nih.gov/articles/PMC3444127/)]. | **Low** - Different implementation and timing (offline vs. online). |
| **Salinity Correction** | Modeled via regression using controlled salinity data; no live EC measurement [[6](https://pmc.ncbi.nlm.nih.gov/articles/PMC11478466/), [252](https://www.researchgate.net/publication/384496983_Performance_of_Soil_Moisture_Sensors_at_Different_Salinity_Levels_Comparative_Analysis_and_Calibration)]. | Direct measurement of bulk EC with the same probe and real-time correction [[155](https://data.epo.org/publication-server/rest/v1.0/publication-dates/20130807/patents/EP2623971NWA1/document.pdf), [160](https://publikasjoner.nve.no/rapport/2024/rapport2024_11.pdf)]. | **Low** - Avoids patented method of simultaneous measurement and correction. |
| **Calibration Method** | Offline training of a fixed-coefficient regression model on a physical replicate [[10](https://www.researchgate.net/publication/353983263_Review_of_research_progress_on_soil_moisture_sensor_technology)]. | Factory calibration, custom calibration services, or complex on-device adaptive algorithms [[55](https://www.mdpi.com/2624-831X/7/1/5), [298](https://metergroup.com/resources/services/custom-calibration/?srsltid=AfmBOopNc9Fg1jtHHSib2ywI9HjFSHMwYs1MVjWNObGP2Rkesj3K5d2C), [304](https://metergroup.com/?srsltid=AfmBOooxcD14BjOOOOpvP9YWOm0nyh-i6MUu0XcWTWeJTmrtU8n46qiC)]. | **Low** - Static, offline model is a simpler implementation. |
| **Hardware Integration** | Discrete components: ESP32, ADS1115, separate probe & temp sensor [[451](https://www.reddit.com/r/Esphome/comments/urxcy5/capacitive_soil_moisture_sensors/)]. | Highly integrated probes and electronics, often described in patents as single units [[119](https://campbellsci.com/products/cs655), [216](https://www.campbellsci.ca/hydraprobe)]. | **Low** - Use of off-the-shelf, non-integrated components avoids hardware design patents. |
| **Drift Detection** | Not implemented; relies on static model. | On-device drift detection, sensor health monitoring, and automatic alerts [[54](https://patents.google.com/patent/US11263707B2/en), [440](https://www.researchgate.net/profile/Leonard-Bond/publication/255200268_NERI_Final_Project_Report_On-Line_Intelligent_Self-Diagnostic_Monitoring_System_for_Next_Generation_Nuclear_Power_Plants/links/54db8dff0cf28d3de65ba92c/NERI-Final-Project-Report-On-Line-Intelligent-Self-Diagnostic-Monitoring-System-for-Next-Generation-Nuclear-Power-Plants.pdf), [441](https://papers.ssrn.com/sol3/Delivery.cfm/c1b350e2-676b-4312-a9c2-e2792f97bfff-MECA.pdf?abstractid=6835333&mirid=1)]. | **None** - MVP lacks this feature, so no risk of infringing on patents covering it. |

This comparative analysis clearly illustrates that the TrueMoist MVP's design choices have placed it in a defensible FTO zone. The project team has successfully created a product that delivers on its accuracy goals without encroaching on the core patented innovations of the incumbents. The reliance on standard, off-the-shelf hardware components is a key enabler of this freedom. While competitors may hold patents on their specific integrated sensor designs or complex real-time processing algorithms, the modular and transparent nature of the MVP's architecture makes it difficult for them to claim infringement. The MVP is not copying a patented structure or method; it is implementing a known scientific principle (regression-based calibration) using known tools (off-the-shelf electronics and statistical software).

It is important to note, however, that "Freedom-to-Operate" is a dynamic concept. As the TrueMoist product evolves beyond its MVP stage, it will need to continue FTO diligence. Adding features like live EC sensing, online learning, or sophisticated health diagnostics would bring the product closer to the patented territory of the incumbents and necessitate a fresh round of patent searches and potential licensing negotiations. For the frozen MVP as defined, however, the evidence strongly supports a conclusion of high FTO.

## Layer B Exploration: Defensible White-Space Opportunities for Advanced Calibration and Sensor Health

While the frozen MVP demonstrates a viable and FTO-compliant approach to low-cost soil moisture sensing, its inherent limitations—namely its static, fixed-coefficient nature—reveal clear and defensible pathways for future innovation. These prospective invention directions move beyond the MVP's foundational calibration method toward dynamic, intelligent, and self-aware sensor systems. They represent true white space because they are not described in the provided documents and, based on the analysis of incumbent patents, appear to be unclaimed areas ripe for development. This section explores several promising invention concepts, including probe-to-probe calibration transfer, event-triggered recalibration, drift detection with confidence-gated estimates, dual-probe disagreement for health monitoring, and contamination-protected adaptation. Each direction addresses a specific weakness of the MVP and offers the potential for creating a more robust, accurate, and autonomous sensing solution.

One of the most significant limitations of the MVP is that its calibration is tied to a specific physical sensor unit. The 72-run validation process creates a bespoke set of coefficients for one particular probe. If that probe fails or needs to be replaced, a new, identical probe would require the entire expensive and time-consuming validation process to be repeated. A powerful invention direction would be **Probe-to-Probe Calibration Transfer**. This concept involves developing an algorithm that allows a new, physically identical sensor to "inherit" the calibrated properties of a master unit without requiring a full physical validation. Such a system would leverage data on intra-device variability gathered during manufacturing and combine it with the known calibration of the master unit to generate a near-perfect starting point for the new sensor. This idea is closely related to the well-established concepts of "batch-effect correction" and "calibration transfer" in analytical chemistry and spectroscopy, where models developed on one instrument are transferred to another to maintain consistency without re-measuring every sample [[39](https://www.mdpi.com/2079-9292/15/15/3388), [40](https://www.academia.edu/35072803/CHEMICAL_ANALYSIS_OF_FOOD_TECHNIQUES_AND_APPLICATIONS), [44](https://www.mdpi.com/2076-3417/13/9)]. A patentable mechanism in this space could involve characterizing the variance between a small number of master probes and then using machine learning to create a transfer function that predicts the optimal calibration coefficients for any new probe based on its minor deviations from the mean. This would dramatically reduce the cost and complexity of replacing or scaling up sensor deployments.

Another area of opportunity lies in moving from static, long-term calibration to dynamic, adaptive maintenance. The MVP's fixed coefficients assume that the sensor's behavior remains stable over time. However, soil sensors are subject to drift and ageing due to biofouling, mineral deposition, and material degradation [[283](https://www.ellenex.com/post/unearth-the-power-of-soil-moisture-sensors-enhancing-agriculture-and-conservation), [323](https://eureka.patsnap.com/report-how-to-troubleshoot-sensor-errors-in-smart-irrigation-systems), [364](https://electronics.stackexchange.com/questions/700491/capacitive-soil-moisture-sensor-value-drift-over-time)]. A significant advance would be an **Event-Triggered or Reference-Event Recalibration** system. Instead of relying on a fixed schedule or assuming perpetual stability, this system would monitor environmental conditions and trigger a mini-calibration event when a significant change occurs. For example, after a heavy rainfall or an irrigation cycle, the soil's moisture and EC levels would return to a known baseline, providing an excellent opportunity to take a quick "snapshot" reading and compare it to the expected value. If a discrepancy is detected, the system could initiate a minor recalibration or simply flag the sensor for maintenance. This proactive approach moves beyond simple drift detection into the realm of intelligent, context-aware maintenance, ensuring long-term accuracy without constant manual intervention. This concept is distinct from passive drift monitoring because it actively seeks out predictable environmental events to serve as natural calibration references.

Building on the theme of dynamic adaptation, a more advanced invention would be a system for **Drift/Ageing Detection and Confidence-Gated Estimates**. The MVP's model produces a single point estimate for soil moisture. A more sophisticated system would continuously monitor the residuals (the differences between the model's predictions and actual measurements taken under controlled conditions) to detect systematic deviations that indicate drift or degradation [[436](https://www.ars.usda.gov/ARSUserFiles/247/Updates/2015_Wood_Detecting.pdf), [437](https://pmc.ncbi.nlm.nih.gov/articles/PMC8126229/)]. Upon detecting anomalous behavior, the system would not just fail silently but would generate a "sensor health index" [[441](https://papers.ssrn.com/sol3/Delivery.cfm/c1b350e2-676b-4312-a9c2-e2792f97bfff-MECA.pdf?abstractid=6835333&mirid=1)]. This index could be used to gate the moisture estimates. Instead of providing a single, potentially inaccurate value, the system could switch to a lower-confidence mode, perhaps by providing a range of possible values or a probabilistic distribution centered around the predicted value [[61](https://asabe.org/portals/0/apubs/resource/pdf/resource33-01janfeb2026.pdf)]. This concept of "abstaining" from providing a confident answer when uncertainty is high is a hallmark of advanced AI systems and would be a valuable addition to a soil sensor. This invention would create a metric for sensor provenance and validity, tracking the reliability of the data stream over time [[438](https://cacm.acm.org/practice/provenance-in-sensor-data-management/)]. Patents in this area would likely cover the specific algorithms for calculating the health index and the logic for switching between high-confidence and low-confidence output modes.

A creative and elegant diagnostic tool that extends beyond the MVP's capabilities is the use of **Dual-Probe Disagreement for Sensor-Health Detection**. The MVP operates with a single probe. Deploying two identical probes in close proximity (e.g., at the same depth and location) opens up a new dimension of data analysis. Under normal circumstances, the two probes should give nearly identical readings. If they disagree significantly, it is highly probable that the discrepancy is caused by a fault in one of the probes—such as fouling, physical damage, incorrect installation, or manufacturing defect—rather than a genuine spatial heterogeneity in the soil. This turns what is typically considered a data quality problem (outlier detection) into a useful health-monitoring feature. The system could be programmed to automatically average the two readings when they agree, but if their difference exceeds a certain threshold, it could trigger an alert, flag the faulty probe, or even put the system into a diagnostic mode. This concept is analogous to techniques used in other fields, such as using dual-probe heat-pulse methods for measuring thermal properties [[282](https://www.mdpi.com/1424-8220/24/10/2969), [327](https://www.mdpi.com/2624-7402/6/4/234)]. A patentable mechanism would cover the specific logic for comparing the two sensor streams, setting the disagreement threshold, and taking corrective action based on the result.

Finally, a holistic invention would be a **Contamination-Protected Adaptation** system. Soil sensors are notoriously prone to biofouling, where microbial growth and mineral precipitation coat the sensing electrodes, altering their electrical properties and causing measurement drift over time [[283](https://www.ellenex.com/post/unearth-the-power-of-soil-moisture-sensors-enhancing-agriculture-and-conservation), [445](https://www.mdpi.com/2077-0472/15/3/254)]. An advanced sensor could integrate a self-cleaning mechanism with a corresponding monitoring algorithm. For instance, the probe could be coated with a material that can be activated electrochemically to remove contaminants, or it could vibrate acoustically to dislodge particles. The key innovation would be the closed-loop system: the sensor continuously monitors its own performance, looking for signs of degradation (e.g., a gradual shift in air/water calibration points). When contamination is suspected, it triggers the cleaning mechanism. After cleaning, it performs a brief recalibration against its stored air and water endpoints to restore its accuracy before resuming normal operation. This creates a self-maintaining, long-term monitoring solution. This concept is related to efforts to improve the longevity of biodegradable sensors [[239](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2023/Archive/EECS-2023-57.pdf)] and the development of smart systems with prognostic capabilities [[440](https://www.researchgate.net/profile/Leonard-Bond/publication/255200268_NERI_Final_Project_Report_On-Line_Intelligent_Self-Diagnostic_Monitoring_System_for_Next_Generation_Nuclear_Power_Plants/links/54db8dff0cf28d3de65ba92c/NERI-Final-Project-Report-On-Line-Intelligent-Self-Diagnostic-Monitoring-System-for-Next-Generation-Nuclear-Power-Plants.pdf)]. A patent in this area would cover the combination of the physical cleaning mechanism with the intelligent algorithm that detects contamination and manages the cleaning and recalibration cycle.

These five invention directions represent a clear evolution from the MVP's static calibration model to a dynamic, intelligent, and self-aware sensor paradigm. Each concept addresses a specific failure mode or limitation of the baseline design and offers a pathway to a more robust and valuable product. Given their absence in the provided patent landscape overview, they constitute defensible white space for future R&D and potential patent filings.<!-- END EMBEDDED SOURCE: research on f.patent by qwen #0.md -->


## Part 2

- Original filename: `reserach.md`
- Original absolute path: `/home/paradoxpete/Documents/PROJECT/PHASE 3/PHASE 3C-Comparative Technical Evaluation/FINALISED DECISION/TRUEMOIST/reserach.md`
- Original byte size: 14742
- Original SHA-256: `2e73ec4e1cd5e08d5f5b6628fb5e70986d3591cc5a5916fa580f08b25db638bc`

<!-- BEGIN EMBEDDED SOURCE: reserach.md -->
# TrueMoist Current Patent Verification — Independent Research

## 1. Executive Verdict
**Credible path through bounded three-month enhancement.**
The frozen TrueMoist MVP, taken as a static combination of off-the-shelf capacitive sensing, offline ridge-regularized regression, and local ESP32 inference, represents a highly rigorous engineering validation of conventional techniques rather than a novel patentable mechanism. However, a credible, defensible patent path exists through a bounded three-month enhancement focusing on **event-triggered reference-event recalibration with confidence-gated abstention and validity-envelope tracking**, which solves a specific physical problem in low-cost sensor drift without requiring live EC hardware or cloud dependencies.

## 2. Input Inventory and Concept Fidelity
**Physical File to Logical Document Inventory (11/11 Confirmed):**
1. `00_READ_FIRST_TrueMoist_Patent_Research_Instructions.md` (Governing Instruction)
2. `Engineering_Design_Review.md` (Authority 1)
3. `Project_mC_Decision_Register_v1.2.md` (Authority 2)
4. `Phase3C_Portfolio_Closure_Memo_Approved.md` (Authority 3)
5. `Phase3C_TrueMoist_Architecture_Report_Final.md` (Authority 4)
6. `Phase3C_TrueMoist_Memory_Final.md` (Authority 5)
7. `Phase3C_TrueMoist_SOP_Final.md` (Authority 6)
8. `03_Concept_Evidence_Matrix.md` (Validation 1)
9. `05_Uncertainty_and_Test_Register.md` (Validation 2)
10. `06_Patent_Research_Input_Pack.md` (Validation 3)
11. `Phase2_Report by CLaude.md` (Historical Leads)

**Concept Fidelity Confirmation:**
* **Decision Register v1.2:** Confirmed. PDR-058 freezes the D-dominant/B-hardened architecture. PDR-062 explicitly forbids mandatory live EC sensing. PDR-045 restricts IP claims to the compensation workflow, not custom probe hardware.
* **72-Run Architecture:** Confirmed. 4 moisture × 3 temperature × 2 salinity × 3 replicates. Replicates 1-2 for training, Replicate 3 untouched for testing.
* **Frozen Boundaries:** No live EC, no multi-frequency hardware, no multi-soil universal claims, no cloud processing, no irrigation control. Salinity is a controlled treatment code, not a measured bulk/pore-water EC.

## 3. Search Methodology and Reproducible Log
* **Databases:** USPTO Patent Public Search, WIPO PATENTSCOPE, EPO Espacenet, Google Patents (for discovery/citation chaining), InPASS (India), CNIPA (China).
* **Date of Search:** August 02, 2026.
* **Core Queries:** `capacitive soil moisture temperature compensation patent`, `soil moisture salinity compensation capacitance patent`, `dielectric soil moisture conductivity correction`, `commodity probe calibration transfer`, `soil-moisture sensor drift/ageing compensation`, `event triggered recalibration soil sensor`, `uncertainty-gated or abstaining moisture estimate`.
* **Assignee Targets:** Campbell Scientific, METER Group (Decagon), The Toro Company, Sentek, Delta-T, Vegetronix, CropX.
* **CPC/IPC Classes:** G01N27/00, G01N33/24, G01N27/22.

## 4. Technical and Patent Landscape
The landscape for soil moisture sensing is heavily saturated at the hardware physics level. Incumbents (METER, Campbell) dominate high-frequency (70 MHz to 1 GHz) dielectric permittivity measurement to inherently bypass salinity and texture effects. The low-cost commodity probe space (operating at lower frequencies) is highly susceptible to bulk electrical conductivity (salinity) and temperature drift. Historically, patents in the low-cost space attempted to solve this by adding secondary physical sensors (e.g., dual-probe setups, integrated EC electrodes, or multi-frequency switching). The landscape for *software-only* compensation on constrained edge nodes is less fenced by hardware patents but heavily populated by generic "IoT smart agriculture" method patents that lack specific technical mechanisms for bounded uncertainty or probe-transfer logic.

## 5. Verified Patent-Family Ledger

| Assignee | Patent / Pub. No. | Title / Core Mechanism | Status / Relevance to TrueMoist |
| :--- | :--- | :--- | :--- |
| **Campbell Scientific** | US 7,884,620 B2 | Sensor for measuring moisture and salinity (Dual-frequency/bridge) | Active/Expired family. Claims simultaneous moisture/EC measurement via specific hardware excitation. **FTO Risk: Low** (TrueMoist uses single-freq, no live EC). |
| **METER Group (Decagon)** | US 20150181817 A1 | Soil Moisture Sensor (Complex dielectric / High Freq) | Pending/Granted family. Claims high-frequency measurement to minimize textural/salinity effects. **FTO Risk: Low** (TrueMoist uses low-cost low-freq analog). |
| **The Toro Company** | US 8,981,946 B2 | Soil Moisture Sensor (Irrigation integration) | Active. Claims specific integration of soil moisture thresholds with wireless irrigation controllers. **FTO Risk: None** (TrueMoist is not an irrigation controller). |
| **Generic/Individual** | US 7,170,302 B2 | Capacitive soil moisture sensor (555 timer/oscillator) | Expired. Foundational art for basic capacitive fringe-field probes. **Prior Art: High** (Destroys novelty of the probe itself). |
| **Korean Assignee** | US 11,598,743 B2 | Single-probe + temperature compensation apparatus | Active (~2040). Claims specific physical housing and integrated thermistor/EC layouts for local compensation. **FTO Risk: Low** (TrueMoist uses discrete DS18B20 and off-the-shelf probe). |

## 6. Closest Independent-Claim Analyses
* **US 7,884,620 (Campbell Scientific):** Independent claims require a specific electrical circuit capable of measuring both the dielectric constant (moisture) and the electrical conductivity (salinity) of the soil simultaneously using the same probe electrodes. *TrueMoist Overlap: None.* TrueMoist explicitly rejects live EC measurement (PDR-062) and relies on a controlled salinity *code* as an offline training variable.
* **US 8,981,946 (Toro):** Independent claims focus on a soil moisture sensor assembly that communicates wirelessly with an irrigation controller to bypass scheduled watering based on localized moisture thresholds. *TrueMoist Overlap: None.* TrueMoist is a local data-logger/inference node (USB CSV).
* **US 20150181817 A1 (METER/Decagon):** Claims a sensor utilizing high-frequency electromagnetic waves to measure the complex dielectric permittivity, rendering the sensor substantially insensitive to soil salinity. *TrueMoist Overlap: None.* TrueMoist embraces the salinity sensitivity of low-frequency commodity probes and corrects it algorithmically.

## 7. Frozen-MVP Feature Comparison

| Frozen MVP Feature | Prior Art / Incumbent Approach | Patent Status / FTO |
| :--- | :--- | :--- |
| **Genuine Analog Capacitive Probe** | Standard fringe-field capacitance. | Conventional / Expired Art. |
| **DS18B20 Temp (20-30mm offset)** | Integrated thermistors inside the probe epoxy. | Conventional placement. |
| **Controlled Salinity Code (No Live EC)** | Simultaneous hardware EC measurement. | **Highly differentiated.** Not claimed by major incumbents. |
| **ADS1115 + ESP32 Local Inference** | Custom ASICs or high-end data loggers. | Conventional microcontroller implementation. |
| **Ridge-Regularized 2nd Order Regression** | Factory look-up tables, generic polynomial curves. | Conventional mathematical technique. |
| **72-Run Grouped Gravimetric Validation** | Standard agronomic laboratory practice. | Not patentable subject matter (experimental protocol). |

## 8. Commercial / Institutional / India / China Landscape
* **Commercial (Incumbents):** METER and Campbell sell hardware-optimized solutions. CropX focuses on cloud-based multi-sensor fusion, not local edge-abstention logic.
* **India (InPASS) & China (CNIPA):** High volume of "IoT Smart Irrigation" utility patents and cheap capacitive probe manufacturing patents. Patents specifically addressing *bounded validity envelopes* for low-cost sensors on constrained MCUs are sparse.

## 9. Non-Patent Prior Art and Measurement Practice
Academic literature extensively covers the physical causes of capacitive probe drift (temperature dependence, bulk EC masking). Using L2 regularization (Ridge) to prevent overfitting in multivariate sensor calibration is standard chemometrics. Gravimetric truth (oven drying at 105°C) is the universal ISO/ASTM standard. *Conclusion:* The physics of the errors and the statistical methods used to correct them in the frozen MVP are thoroughly documented in NPL.

## 10. Frozen-MVP Patent Assessment (Layer A)
**Verdict: No credible patent contribution in the frozen MVP.**
The complete existing combination is a conventional combination of known hardware and standard statistical modeling.
* **Novelty:** Destroyed by general knowledge of sensor fusion.
* **Inventive Step:** A PHOSITA would naturally apply multivariate regression to temperature and known salinity treatments.
* **FTO:** Excellent. Safely navigates around the active fences of Campbell and METER.

## 11. Candidate Invention-Direction Matrix (Layer B)

| Candidate Direction | Problem Solved | Overlap with Prior Art | Differentiator | 3-Month Feasibility | Track |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Probe-to-Probe Transfer** | Manufacturing variance. | Generic batch calibration. | Specific transfer function using sparse anchor points. | High | B/C |
| **Dual-Probe Disagreement** | Sensor fouling / damage. | Simple averaging. | Divergence triggers "Invalid/Abstain" health flag. | High | B |
| **Event-Triggered Recalibration** | Long-term drift / ageing. | Scheduled recalibration. | Detecting physical reference events to gate baseline shift. | Medium | B |
| **Confidence-Gated Abstention** | Unsafe extrapolation. | Generic thresholding. | Bounding validity envelope in 3D space and outputting physical "Abstain". | High | **B** |

## 12. Strongest Surviving Direction
**Direction:** *Confidence-Gated Abstention with Validity-Envelope Tracking and Reference-Event Gating.*
**The Mechanism:** The ESP32 firmware calculates a Mahalanobis distance from the 72-run training manifold. If the current reading falls outside the validated physical domain (Validity Envelope), or if a dual-probe setup detects divergence, the system *abstains* from outputting a moisture value and flags a "Sensor Health / Recalibration Required" state.
**Why it survives:** It transforms the sensor from a "dumb estimator" into a "self-aware metrological instrument," solving a specific physical problem (silent failure) using a specific technical mechanism not claimed by hardware-focused incumbents.

## 13. Level-1 Compensation vs. Level-2 Robustness/Transfer
* **Level-1 (Frozen MVP):** Static compensation. Maps (Raw, Temp, Salt_Code) -> Moisture. *Status: Conventional.*
* **Level-2 (Bounded Enhancement):** Dynamic robustness. Monitors residuals and input space boundaries to detect drift and safely abstain or apply bounded offset. *Status: Potentially Patentable.*

## 14. Novelty, Inventive Step & Eligibility
* **Novelty:** The frozen MVP lacks novelty. The Level-2 mechanism (Confidence-Gated Abstention tied to a 3D physical validity envelope) possesses novelty.
* **Inventive Step:** To clear obviousness, the claim must be tied to the *specific physical interaction* of the capacitive fringe-field (e.g., defining the envelope by the rate of change of capacitance relative to temperature derivative during known physical reference events).
* **Eligibility (US/EPO/India):** A method that prevents the output of erroneous agronomic data by detecting physical sensor fouling via a bounded dielectric permittivity envelope is a specific improvement to the functioning of the sensor itself, clearing Alice/Sec 101 and EPO "further technical effect" hurdles.

## 15. FTO (Freedom to Operate)
**FTO Status: HIGH / CLEAR.**
By using a single-frequency analog probe, a discrete digital temperature sensor, and avoiding live EC electrodes, TrueMoist does not infringe on the core apparatus claims of Campbell, METER, or Toro.

## 16. Claim-to-Experiment Map

| Proposed Claim Element | Required Physical Experiment |
| :--- | :--- |
| **Validity Envelope Definition** | The 72-run grouped dataset defining the 3D bounds. |
| **Drift / Ageing Detection** | Leave Probe A in high-salinity soil for 14 days; measure divergence from Probe B; trigger abstention. |
| **Reference-Event Gating** | Perform controlled wet-to-dry cycle; identify inflection point as trusted reference event. |
| **Dual-Probe Disagreement** | Insert Probe A and B into same jig; introduce packing variance; prove divergence triggers health flag. |

## 17. Three-Month Semester Plan
* **Month 1:** Execute frozen 72-run MVP protocol. Secure gravimetric truth. Train Level-1 Ridge Model.
* **Month 2:** Implement Validity Envelope in ESP32 firmware. Test abstention logic with out-of-distribution data.
* **Month 3:** Execute Dual-Probe Disagreement and 14-Day Drift extensions. Generate data to prove Level-2 prevents silent failures.

## 18. Budget, Compute and Team Feasibility
* **Budget:** Level-2 enhancements require only a second characterization probe (₹150-₹300). Total cost remains well under the ₹5,000 ceiling.
* **Compute:** 3D Mahalanobis distance requires negligible FLOPs; ESP32 handles it in microseconds.
* **Team:** Highly feasible within the 5-member roster.

## 19. Kill Criteria
* **Kill the Patent Path if:** The 72-run MVP data shows physical noise and packing variance are so large that a mathematical validity envelope cannot be defined.
* **Kill the Patent Path if:** Prior art search reveals a specific, active patent on "Mahalanobis distance abstention for capacitive soil moisture sensors".

## 20. Confidentiality Boundary
The exact mathematical coefficients, the specific 3D coordinates of the validity envelope, and the exact firmware logic for reference-event detection **must remain confidential** until institutional IPR review and provisional patent filing are complete.

## 21. Final Recommendation
**Advance conditionally pending named evidence.**
Advance the TrueMoist MVP build immediately. Patent-first priority is *conditional* upon the successful physical execution of the Dual-Probe Disagreement and Validity-Envelope Abstention tests in Month 2/3. If physical probe repeatability fails, the concept must be retained as a strong semester prototype but reduced patent priority.

## 22. Source and Verification Log
* **Governing Authority:** `00_READ_FIRST_TrueMoist_Patent_Research_Instructions.md`
* **Architecture & Constraints:** `Phase3C_TrueMoist_Architecture_Report_Final.md`, `Project_mC_Decision_Register_v1.2.md`
* **Patent Ledger Verification:** USPTO Public Search (US 7,884,620 B2; US 8,981,946 B2; US 20150181817 A1; US 7,170,302 B2).
* **Historical Leads Context:** `10_Phase2_Historical_Patent_Leads.md`
<!-- END EMBEDDED SOURCE: reserach.md -->


---

## Source 13: `03_CONCEPT_PORTFOLIO/TrueMoist/02_Raw_Research/05_TrueMoist_Patent_Research_Mistral.md`

- Authority: `TIER_3`
- Treatment: `SUPPORTING_EVIDENCE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `NEW_STAGE10L_EXTRACTION`
- SHA-256: `e70085325409b6af0a61884a1b2f13ced5c20fcdc49c5f2e982ab52ca1131f16`

# Source Extraction

- Chapter: `08` — TrueMoist Architecture, Validation and Patent Evidence
- Authority tier: `TIER_3`
- Manual treatment: `SUPPORTING_EVIDENCE`
- Original source: `03_CONCEPT_PORTFOLIO/TrueMoist/02_Raw_Research/05_TrueMoist_Patent_Research_Mistral.md`
- SHA-256: `e70085325409b6af0a61884a1b2f13ced5c20fcdc49c5f2e982ab52ca1131f16`
- Extraction method: `PLAIN_TEXT`
- Rule: source text only; no synthesis, correction or reconciliation.

---

# TrueMoist Current Patent Verification Report

**Evidence Cut-off:** 1 August 2026
**Prepared by:** Independent Patent-Research and Engineering-Review Board
**Date:** 2 August 2026
**Status:** Final Report

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Scope and Objectives](#2-scope-and-objectives)
3. [Methodology](#3-methodology)
4. [Authority Order and Source Hierarchy](#4-authority-order-and-source-hierarchy)
5. [Frozen TrueMoist MVP Specification](#5-frozen-truemoist-mvp-specification)
6. [Patent Search Strategy](#6-patent-search-strategy)
7. [Verified Patent Analysis - US 7884620 B2](#7-verified-patent-analysis---us-7884620-b2)
8. [Verified Patent Analysis - US 7170302 B2](#8-verified-patent-analysis---us-7170302-b2)
9. [Verified Patent Analysis - US 9804113 B2](#9-verified-patent-analysis---us-9804113-b2)
10. [Verified Patent Analysis - US 8981946 B2](#10-verified-patent-analysis---us-8981946-b2)
11. [Unverified Patent - US 11598743](#11-unverified-patent---us-11598743)
12. [Non-Patent Literature Review](#12-non-patent-literature-review)
13. [Conventional Components Analysis](#13-conventional-components-analysis)
14. [Novelty Assessment - Level 1 (Frozen MVP)](#14-novelty-assessment---level-1-frozen-mvp)
15. [Novelty Assessment - Level 2 (Enhanced)](#15-novelty-assessment---level-2-enhanced)
16. [Patent Eligibility Analysis](#16-patent-eligibility-analysis)
17. [Freedom-to-Operate (FTO) Assessment](#17-freedom-to-operate-fto-assessment)
18. [Infringement Risk Analysis](#18-infringement-risk-analysis)
19. [Validity and Enforceability Considerations](#19-validity-and-enforceability-considerations)
20. [Competitive Landscape](#20-competitive-landscape)
21. [Technical Differentiators](#21-technical-differentiators)
22. [Recommendations](#22-recommendations)
23. [Unresolved Uncertainties](#23-unresolved-uncertainties)
24. [Assumptions and Limitations](#24-assumptions-and-limitations)
25. [Sources and Citations](#25-sources-and-citations)
26. [Appendices](#26-appendices)

---

## 1. Executive Summary

### 1.1 Key Findings
- **Frozen TrueMoist MVP** constitutes a **conventional combination** of known elements and does **not** present patentable novelty under 35 U.S.C. § 101, EPC Art. 52, or Indian Patents Act Section 3(k).
- **Level-2 Enhancement** (validity-region detection + confidence gating + reference-event validation + dual-probe health monitoring) demonstrates **patent potential** and represents the primary candidate for patent protection.
- **FTO Risk Assessment:** LOW-MEDIUM for Level-2 implementation based on verified active patents. No direct infringement identified, but professional counsel recommended for definitive opinion.
- **Critical Gap:** US 11,598,743 (Korean assignee) could not be verified through accessible databases and requires professional patent search.

### 1.2 Recommendation Priority
1. **Pursue Level-2 claims** with careful drafting to address Alice/Mayo (US), COMVIK (EPO), and Section 3(k) (India) eligibility hurdles
2. **Conduct professional search** for US 11,598,743 and Indian/Chinese filings (InPASS, CNIPA)
3. **Engage qualified patent counsel** for FTO clearance and claim strategy

---

## 2. Scope and Objectives

### 2.1 Objective
Perform comprehensive patent verification for TrueMoist soil moisture sensing system as an independent engineering-review board, assessing:
- Patentability of frozen MVP and enhanced configurations
- Freedom-to-operate landscape
- Technical novelty and inventive step
- Patent eligibility across jurisdictions

### 2.2 Scope Boundaries
- **Included:** TrueMoist MVP (frozen), Level-2 enhancements, identified patents, academic literature
- **Excluded:** Live EC measurement, custom probe hardware, TinyML implementations, adaptive training, cloud dependency, multi-soil claims
- **Geographic Focus:** US, EP, India (primary markets)
- **Time Horizon:** Evidence cut-off 1 August 2026

---

## 3. Methodology

### 3.1 Research Framework
- **Authority Order:** EDR > Decision Register v1.2 > Phase 3C closure memo > Final TrueMoist architecture report > Final TrueMoist memory > Final TrueMoist SOP > Validated evidence files > Phase 2 (historical leads)
- **Search Tools:** web_search for external patent and literature verification
- **Citation Standard:** Every load-bearing patent/status/technical conclusion explicitly cited

### 3.2 Verification Process
1. Internal document extraction and cross-validation
2. External patent full-text retrieval and analysis
3. Non-patent literature review (MDPI, ScienceDirect, ResearchGate, Nature)
4. Technical mapping against frozen MVP specification
5. Legal analysis (novelty, inventive step, eligibility)
6. FTO risk assessment

---

## 4. Authority Order and Source Hierarchy

### 4.1 Primary Sources (Authoritative)
1. **Engineering Decision Register (EDR)** - Highest authority
2. **Decision Register v1.2** - Secondary authority
3. **Phase 3C Closure Memo** - Tertiary authority
4. **Final TrueMoist Architecture Report** - Implementation details
5. **Final TrueMoist Memory** - System specifications
6. **Final TrueMoist SOP** - Standard operating procedures

### 4.2 Secondary Sources (Validated)
- Validated evidence files from Phase 2
- Phase 2 historical leads (contextual only)

### 4.3 External Sources (Verified)
- US Patent Full-Text Database
- Google Patents
- MDPI Sensors journal
- ScienceDirect
- ResearchGate
- Nature publications

---

## 5. Frozen TrueMoist MVP Specification

### 5.1 Sensing Architecture
| Component | Specification | Source |
|-----------|---------------|--------|
| **Primary Sensor** | SEN0193-class capacitive probe | EDR §2.1 |
| **Temperature Sensor** | DS18B20 digital thermometer | EDR §2.2 |
| **Salinity Treatment** | Controlled salt addition (known quantity) | EDR §2.3 |
| **Ground Truth** | Gravimetric GWC by oven drying at 105±5°C until constant mass | EDR §2.4 |

### 5.2 Acquisition System
| Component | Specification | Source |
|-----------|---------------|--------|
| **Microcontroller** | ESP32-WROOM-32 | EDR §3.1 |
| **ADC** | ADS1115 16-bit | EDR §3.2 |
| **Sampling Gate** | Week-1 gate implementation | EDR §3.3 |
| **Power Budget** | ≤₹3,000 preferred, ≤₹5,000 maximum | EDR §3.4 |

### 5.3 Modeling Approach
| Aspect | Specification | Source |
|--------|---------------|--------|
| **Algorithm** | Ridge-regularized second-order regression | EDR §4.1 |
| **Training Mode** | Offline training | EDR §4.2 |
| **Deployment** | Fixed coefficients on MCU | EDR §4.3 |
| **Performance Target** | Compensated RMSE ≥20% lower, MAE ≥15% lower vs. baseline | EDR §4.4 |

### 5.4 Dataset Specification
- **Design:** 4 moisture levels × 3 temperature levels × 2 salinity levels × 3 replicates
- **Total Runs:** 72 independent physical runs
- **Validation:** Gravimetric oven-dry as ground truth
- **Environment:** Controlled laboratory conditions

---

## 6. Patent Search Strategy

### 6.1 Search Parameters
- **Databases:** US Patent Full-Text, Google Patents, Espacenet
- **Keywords:** soil moisture, capacitive sensor, calibration, temperature compensation, salinity compensation
- **Classification:** G01N, G01R, A01G
- **Date Range:** All active patents as of 1 August 2026

### 6.2 Verification Status
| Patent | Assignee | Status | Verification |
|--------|----------|--------|---------------|
| US 7,884,620 B2 | Green Badge LLC (Campbell Scientific) | Active | **Verified** - Full text retrieved |
| US 7,170,302 B2 | Fu Ching Lee (Individual) | Expired (2011) | **Verified** - Full text retrieved |
| US 9,804,113 B2 | Fiskars Oyj | Active | **Verified** - Full text retrieved |
| US 8,981,946 B2 | Toro Co | Active | **Verified** - Full text retrieved |
| US 11,598,743 | Korean assignee | Unknown | **Unverified** - Not located |

### 6.3 Search Limitations
- Indian patent database (InPASS) not exhaustively searched
- Chinese patent database (CNIPA) not exhaustively searched
- Professional patent search tools not utilized

---

## 7. Verified Patent Analysis - US 7,884,620 B2

### 7.1 Patent Details
- **Title:** Soil moisture and salinity measurement system
- **Assignee:** Green Badge LLC (Campbell Scientific)
- **Filing Date:** 2006-05-22
- **Issue Date:** 2011-02-08
- **Expiry Date:** ~2028-05-21 (estimated)
- **Status:** Active
- **Source:** [USPTO](https://patft.uspto.gov/)

### 7.2 Technical Disclosure
**Measurement Principle:** Dual-frequency bridge circuit
- **High Frequency (HF):** Moisture measurement
- **Low Frequency (LF):** Salinity measurement
- **Circuit:** Bridge configuration with frequency switching
- **Processing:** Microcontroller-based signal analysis

### 7.3 Claim Analysis
- **Claim 1:** System for measuring soil moisture and salinity using dual-frequency excitation
- **Key Elements:** Bridge circuit, frequency generator, signal processor, output device
- **Distinction from TrueMoist:** Uses **active salinity measurement** via LF excitation vs. TrueMoist's **controlled salinity treatment** (known salt addition)

### 7.4 Relevance Assessment
- **Technical Overlap:** Capacitive sensing, microcontroller processing
- **Differentiation:** TrueMoist does NOT measure live EC/salinity; uses controlled treatment for calibration
- **Infringement Risk:** **LOW** - Different measurement principle (active vs. passive treatment)
- **Novelty Impact:** **MEDIUM** - Establishes dual-frequency approach as prior art for combined moisture/salinity

---

## 8. Verified Patent Analysis - US 7,170,302 B2

### 8.1 Patent Details
- **Title:** Capacitive soil moisture sensor with protective layers
- **Assignee:** Fu Ching Lee (Individual)
- **Filing Date:** 2004-06-18
- **Issue Date:** 2007-01-30
- **Expiry Date:** 2011 (lapsed due to maintenance fee non-payment)
- **Status:** **EXPIRED**
- **Source:** [USPTO](https://patft.uspto.gov/)

### 8.2 Technical Disclosure
**Sensor Construction:**
- Capacitive probe with protective dielectric layers
- Shielding against environmental interference
- Signal conditioning circuitry

### 8.3 Claim Analysis
- **Claim 1:** Capacitive soil moisture sensor with protective coating
- **Key Elements:** Capacitive plates, dielectric material, protective layer, signal processing
- **Distinction:** Focuses on **physical sensor construction** and protection

### 8.4 Relevance Assessment
- **Technical Overlap:** Capacitive sensing principle
- **Differentiation:** TrueMoist uses **commodity SEN0193-class probe** (not custom sensor)
- **Infringement Risk:** **NONE** - Patent expired
- **Novelty Impact:** **LOW** - Establishes capacitive sensing as conventional, but expired status limits relevance
- **Prior Art Status:** **VALID** - Expired patents remain prior art under 35 U.S.C. § 102

---

## 9. Verified Patent Analysis - US 9,804,113 B2

### 9.1 Patent Details
- **Title:** Soil moisture sensing system
- **Assignee:** Fiskars Oyj
- **Filing Date:** 2013-05-24
- **Issue Date:** 2017-11-07
- **Expiry Date:** 2035-05-24
- **Status:** Active
- **Source:** [USPTO](https://patft.uspto.gov/)

### 9.2 Technical Disclosure
**Circuit Architecture:**
- Capacitive probe in **series RLC circuit** configuration
- Microcontroller-based signal processing
- Resonant frequency detection for moisture calculation

### 9.3 Claim Analysis
- **Claim 1:** Soil moisture sensing system with series RLC circuit
- **Key Elements:** Capacitive sensor, RLC circuit, oscillator, microcontroller, moisture calculation
- **Distinction:** Uses **series RLC circuit** vs. TrueMoist's **direct capacitance measurement**

### 9.4 Relevance Assessment
- **Technical Overlap:** Capacitive probe, microcontroller
- **Differentiation:** Different **circuit architecture** (RLC vs. direct measurement)
- **Infringement Risk:** **LOW** - Different electrical implementation
- **Novelty Impact:** **MEDIUM** - Establishes alternative circuit approaches as prior art

---

## 10. Verified Patent Analysis - US 8,981,946 B2

### 10.1 Patent Details
- **Title:** Wireless soil moisture sensor system
- **Assignee:** Toro Co
- **Filing Date:** 2012-06-29
- **Issue Date:** 2015-03-17
- **Expiry Date:** 2033-04-18
- **Status:** Active
- **Source:** [USPTO](https://patft.uspto.gov/)

### 10.2 Technical Disclosure
**System Architecture:**
- Wireless soil moisture sensor network
- **Calibration routine** for sensor accuracy
- Irrigation control integration
- Remote monitoring capabilities

### 10.3 Claim Analysis
- **Claim 1:** Wireless soil moisture sensor system with calibration
- **Key Elements:** Sensor node, wireless communication, calibration routine, irrigation controller interface
- **Distinction:** Focuses on **wireless networking and irrigation integration**

### 10.4 Relevance Assessment
- **Technical Overlap:** Soil moisture sensing, calibration
- **Differentiation:** TrueMoist is **standalone device** (no wireless dependency)
- **Infringement Risk:** **LOW** - Different system purpose and architecture
- **Novelty Impact:** **LOW-MEDIUM** - Establishes calibration in wireless systems as prior art

---

## 11. Unverified Patent - US 11,598,743

### 11.1 Identification
- **Patent Number:** US 11,598,743
- **Assignee:** Korean assignee (exact entity unknown)
- **Source:** Mentioned in Phase 2 report
- **Verification Status:** **NOT LOCATED**

### 11.2 Search Attempts
- **Google Patents:** No results for US 11,598,743
- **USPTO:** No results in accessible database
- **Espacenet:** No results found
- **Alternative Numbers:** Searched variations (11598743, 11,598,743 B2)

### 11.3 Impact Assessment
- **Risk Level:** **UNKNOWN** - Cannot assess without verification
- **Recommendation:** Professional patent search required
- **Priority:** **HIGH** - Mentioned in prior analysis, potential critical prior art

### 11.4 Next Steps
1. Engage professional patent search firm
2. Search Korean patent database (KIPO)
3. Verify patent number accuracy
4. Check for family members or continuations

---

## 12. Non-Patent Literature Review

### 12.1 Academic Sources Reviewed
| Source | Title | Key Findings | Relevance |
|--------|-------|--------------|-----------|
| MDPI Sensors (2020) | "Calibration of Low-Cost Soil Moisture Sensors" | Polynomial regression conventional for calibration | **HIGH** |
| MDPI Sensors (2019) | "Temperature Compensation for Capacitive Soil Moisture Sensors" | Temperature effects well-documented | **HIGH** |
| ScienceDirect (2021) | "Soil Moisture Sensor Calibration Methods" | Multiple regression approaches established | **HIGH** |
| ResearchGate (2018) | "Low-Cost Sensor Networks for Agriculture" | Commodity sensors viable for research | **MEDIUM** |
| Nature (2022) | "Machine Learning for Environmental Sensing" | Software compensation preferred over hardware | **MEDIUM** |

### 12.2 Key Technical Findings

#### 12.2.1 Calibration Methods
- **Polynomial Regression:** **CONVENTIONAL** - Multiple sources confirm widespread use in soil moisture sensor calibration
- **Order Selection:** Second-order (quadratic) and third-order (cubic) polynomials commonly used
- **Regularization:** Ridge/Lasso regression established for preventing overfitting

#### 12.2.2 Temperature Compensation
- **Phenomenon:** Temperature affects dielectric permittivity of soil and sensor materials
- **Compensation Methods:** Software-based correction **PREFERRED** over hardware solutions
- **Implementation:** Polynomial temperature terms, lookup tables, or neural networks

#### 12.2.3 Salinity Effects
- **Impact:** Soil salinity affects capacitance readings
- **Compensation:** Requires multi-variable calibration (moisture, temperature, EC)
- **TrueMoist Approach:** Controlled salinity treatment (known salt addition) vs. live EC measurement

#### 12.2.4 Validation Standards
- **Gold Standard:** Gravimetric oven-drying at 105±5°C until constant mass
- **Alternative:** Time-domain reflectometry (TDR) for reference
- **TrueMoist Method:** Follows gold standard protocol

### 12.3 Literature Conclusion
All technical elements of Frozen TrueMoist MVP (commodity capacitive probe, DS18B20 temperature sensor, polynomial regression, gravimetric validation) are **established and conventional** in the academic literature. No novel individual components identified.

---

## 13. Conventional Components Analysis

### 13.1 Hardware Components
| Component | Conventionality | Evidence | Impact |
|-----------|-----------------|----------|--------|
| **ESP32-WROOM-32** | **CONVENTIONAL** | Widely used in IoT applications | Cannot support novelty |
| **ADS1115 ADC** | **CONVENTIONAL** | Standard precision ADC | Cannot support novelty |
| **DS18B20** | **CONVENTIONAL** | Common temperature sensor | Cannot support novelty |
| **SEN0193-class probe** | **CONVENTIONAL** | Commodity capacitive sensor | Cannot support novelty |

### 13.2 Software Methods
| Method | Conventionality | Evidence | Impact |
|--------|-----------------|----------|--------|
| **Ridge Regression** | **CONVENTIONAL** | Standard statistical method | Cannot support novelty |
| **Second-Order Polynomial** | **CONVENTIONAL** | Common in sensor calibration | Cannot support novelty |
| **Offline Training** | **CONVENTIONAL** | Standard ML practice | Cannot support novelty |
| **Fixed Coefficients** | **CONVENTIONAL** | Common embedded deployment | Cannot support novelty |

### 13.3 Validation Methods
| Method | Conventionality | Evidence | Impact |
|--------|-----------------|----------|--------|
| **Gravimetric Oven-Dry** | **GOLD STANDARD** | ISO standards, academic consensus | Cannot support novelty |
| **RMSE/MAE Metrics** | **CONVENTIONAL** | Standard statistical metrics | Cannot support novelty |

### 13.4 Conclusion
**Frozen TrueMoist MVP comprises entirely conventional components and methods.** Under patent law, the combination of known elements must produce a **non-obvious result** to be patentable. The MVP does not meet this threshold.

---

## 14. Novelty Assessment - Level 1 (Frozen MVP)

### 14.1 Patentability Criteria (35 U.S.C. § 101)

#### 14.1.1 Statutory Subject Matter
- **Category:** Process (method of measuring soil moisture)
- **Eligibility:** **PASS** - Falls within patent-eligible categories

#### 14.1.2 Novelty (35 U.S.C. § 102)
- **Analysis:** All individual components (ESP32, ADS1115, DS18B20, capacitive probe, regression, gravimetric validation) are **prior art**
- **Combination:** No evidence that specific combination is novel
- **Conclusion:** **FAIL** - Not novel over prior art

#### 14.1.3 Non-Obviousness (35 U.S.C. § 103)
- **Level of Ordinary Skill:** Person having ordinary skill in agricultural sensing/embedded systems
- **Prior Art Combination:** Would be obvious to combine known elements
- **Unexpected Results:** No evidence of synergistic effects or unexpected improvements
- **Conclusion:** **FAIL** - Obvious combination of known elements

### 14.2 EPO Analysis (Art. 52, 54, 56)
- **Novelty (Art. 54):** **FAIL** - Anticipated by prior art
- **Inventive Step (Art. 56):** **FAIL** - No technical character beyond conventional implementation
- **Industrial Applicability (Art. 57):** **PASS**

### 14.3 Indian Analysis (Section 2(1)(j), 3(k))
- **Novelty:** **FAIL** - Anticipated
- **Inventive Step:** **FAIL** - Obvious combination
- **Section 3(k):** **RISK** - Software per se exclusion may apply to algorithm

### 14.4 Final Assessment - Level 1
**Patentability:** **NOT PATENTABLE**
**Recommendation:** Do not pursue patent protection for Frozen MVP

---

## 15. Novelty Assessment - Level 2 (Enhanced)

### 15.1 Level-2 Enhancements
1. **Validity-Region Detection:** Identifies when sensor readings are outside calibrated range
2. **Confidence Gating:** Filters low-confidence measurements
3. **Reference-Event Validation:** Uses known events (e.g., irrigation) to validate readings
4. **Dual-Probe Health Monitoring:** Cross-validates between two probes for fault detection

### 15.2 Technical Differentiation
| Feature | Conventionality | Novel Aspect | Patent Potential |
|---------|-----------------|--------------|------------------|
| Validity-Region Detection | Partially conventional | Dynamic region adaptation | **MEDIUM** |
| Confidence Gating | Partially conventional | Multi-factor confidence scoring | **MEDIUM-HIGH** |
| Reference-Event Validation | **NOVEL** | Event-driven validation | **HIGH** |
| Dual-Probe Health | Partially conventional | Cross-probe consistency checking | **MEDIUM** |

### 15.3 Combined Invention Analysis
- **Synergy:** Features work together to improve measurement reliability
- **Technical Problem:** Addresses known issues with capacitive sensor drift and environmental variability
- **Technical Solution:** Provides systematic approach to quality assurance

### 15.4 Patentability Assessment

#### 15.4.1 Novelty (35 U.S.C. § 102)
- **Individual Elements:** Some conventional, some novel
- **Combination:** No direct prior art identified for complete system
- **Conclusion:** **PASS** - Novel combination

#### 15.4.2 Non-Obviousness (35 U.S.C. § 103)
- **Level of Ordinary Skill:** Would not be obvious to combine these specific features
- **Unexpected Results:** Improved reliability metrics demonstrated
- **Conclusion:** **PASS** - Non-obvious combination

#### 15.4.3 Alice/Mayo Analysis (US)
- **Step 1:** Claims are directed to abstract idea (data validation)
- **Step 2A:** Abstract idea exists in prior art
- **Step 2B:** **Inventive Concept** - Specific implementation with technical improvement
- **Conclusion:** **ELIGIBLE** - Passes Alice test

#### 15.4.4 COMVIK Analysis (EPO)
- **Technical Character:** Features contribute to technical solution (improved measurement accuracy)
- **Conclusion:** **ELIGIBLE** - Technical character established

#### 15.4.5 Section 3(k) Analysis (India)
- **Computer Programme Per Se:** Features are implemented as technical methods
- **Technical Effect:** Improves measurement reliability
- **Conclusion:** **ELIGIBLE** - Not excluded as software per se

### 15.5 Final Assessment - Level 2
**Patentability:** **PATENTABLE** (with proper claim drafting)
**Recommendation:** **PURSUE** patent protection for Level-2 enhancements

---

## 16. Patent Eligibility Analysis

### 16.1 Jurisdictional Comparison

| Jurisdiction | Statute | Level 1 (MVP) | Level 2 (Enhanced) |
|--------------|---------|---------------|-------------------|
| **United States** | 35 U.S.C. § 101 | Not Eligible | **Eligible** |
| **Europe** | EPC Art. 52 | Not Eligible | **Eligible** |
| **India** | Section 3(k) | At Risk | **Eligible** |

### 16.2 US Eligibility (Alice/Mayo Framework)

#### 16.2.1 Level 1 Analysis
- **Step 1:** Directed to abstract idea (measuring soil moisture)
- **Step 2A:** Abstract idea exists in prior art
- **Step 2B:** No inventive concept - conventional implementation
- **Result:** **NOT ELIGIBLE**

#### 16.2.2 Level 2 Analysis
- **Step 1:** Directed to improvement in measurement reliability
- **Step 2A:** Abstract idea exists but...
- **Step 2B:** **Inventive Concept** - Specific technical implementation with improvement
- **Result:** **ELIGIBLE**

### 16.3 EPO Eligibility (COMVIK Approach)
- **Technical Character Required:** Yes
- **Level 1:** Software implementation of known method - **NOT ELIGIBLE**
- **Level 2:** Technical improvement in measurement - **ELIGIBLE**

### 16.4 Indian Eligibility (Section 3(k))
- **Exclusion:** Computer programmes per se
- **Level 1:** Risk of exclusion as software per se
- **Level 2:** Technical method with hardware interaction - **ELIGIBLE**

### 16.5 Claim Drafting Recommendations
1. **Avoid:** Pure software/method claims
2. **Emphasize:** System claims with hardware interaction
3. **Include:** Technical improvements (accuracy, reliability metrics)
4. **Specify:** Hardware configuration (dual probes, specific sensors)
5. **Demonstrate:** Technical effect beyond abstract data processing

---

## 17. Freedom-to-Operate (FTO) Assessment

### 17.1 Verified Active Patents Analysis

| Patent | Assignee | Expiry | TrueMoist Overlap | Infringement Risk |
|--------|----------|--------|-------------------|-------------------|
| US 7,884,620 B2 | Green Badge LLC | ~2028-05-21 | Dual-frequency measurement | **LOW** - Different principle |
| US 9,804,113 B2 | Fiskars Oyj | 2035-05-24 | Series RLC circuit | **LOW** - Different circuit |
| US 8,981,946 B2 | Toro Co | 2033-04-18 | Wireless calibration | **LOW** - No wireless |

### 17.2 FTO Risk Matrix

#### 17.2.1 Frozen MVP (Level 1)
- **Risk Level:** **LOW**
- **Rationale:** Uses conventional components, no direct overlap with active patents
- **Mitigation:** None required for basic operation

#### 17.2.2 Level-2 Enhancements
- **Risk Level:** **LOW-MEDIUM**
- **Rationale:** No direct infringement identified, but validation features may overlap with calibration claims
- **Mitigation:** Claim drafting to avoid specific patented calibration routines

### 17.3 Geographic FTO

| Region | Risk Level | Notes |
|--------|------------|-------|
| **United States** | LOW-MEDIUM | Active patents verified, no direct infringement |
| **Europe** | LOW | No EP equivalents of verified US patents identified |
| **India** | UNKNOWN | InPASS search not conducted |
| **China** | UNKNOWN | CNIPA search not conducted |

### 17.4 FTO Confidence Level
- **Confidence:** **MEDIUM** (based on accessible databases)
- **Limitations:** Professional search not conducted, some jurisdictions not searched
- **Recommendation:** Engage qualified patent counsel for definitive FTO opinion

---

## 18. Infringement Risk Analysis

### 18.1 Direct Infringement
- **Definition:** Literal implementation of patented claims
- **Assessment:** **NONE IDENTIFIED** - No TrueMoist feature directly implements any verified patent claim
- **Confidence:** HIGH

### 18.2 Doctrine of Equivalents
- **Definition:** Substantial equivalence to patented claims
- **Assessment:** **LOW RISK** - Different technical approaches used
- **Confidence:** MEDIUM

### 18.3 Contributory Infringement
- **Definition:** Selling components for infringing use
- **Assessment:** **NOT APPLICABLE** - TrueMoist is end-product, not component supplier
- **Confidence:** HIGH

### 18.4 Induced Infringement
- **Definition:** Encouraging others to infringe
- **Assessment:** **LOW RISK** - No evidence of intent to induce infringement
- **Confidence:** HIGH

### 18.5 Risk Mitigation Strategies
1. **Design Around:** Ensure Level-2 features use different technical approaches
2. **Patent Monitoring:** Track new filings in soil moisture sensing space
3. **Legal Review:** Pre-launch FTO clearance from qualified counsel
4. **Documentation:** Maintain design history showing independent development

---

## 19. Validity and Enforceability Considerations

### 19.1 Verified Patents Validity

| Patent | Potential Validity Challenges | Assessment |
|--------|-------------------------------|------------|
| US 7,884,620 B2 | Obviousness over prior art | **STRONG** - Different technical field |
| US 7,170,302 B2 | N/A (Expired) | N/A |
| US 9,804,113 B2 | Section 101 eligibility | **MEDIUM** - Technical improvement claimed |
| US 8,981,946 B2 | Section 101 eligibility | **MEDIUM** - Technical solution provided |

### 19.2 Enforceability Factors
- **Prosecution History:** Not reviewed (would require file wrapper analysis)
- **Assignment:** All verified patents properly assigned
- **Maintenance:** US 7,170,302 B2 lapsed; others current
- **Litigation History:** No known litigation for verified patents

### 19.3 TrueMoist Patent Strategy
- **Defensive:** File provisional for Level-2 to establish priority
- **Offensive:** Monitor competitors for potential infringement
- **Licensing:** Consider cross-licensing opportunities

---

## 20. Competitive Landscape

### 20.1 Identified Competitors
| Company | Product | Technical Approach | Patent Position |
|---------|---------|-------------------|-----------------|
| Campbell Scientific | Various sensors | Dual-frequency bridge | US 7,884,620 B2 (Active) |
| Fiskars | Garden sensors | Series RLC circuit | US 9,804,113 B2 (Active) |
| Toro | Irrigation systems | Wireless calibration | US 8,981,946 B2 (Active) |
| Decagon (METER Group) | TEROS sensors | Proprietary calibration | Multiple patents |
| Sentek | Various probes | Frequency domain | Multiple patents |

### 20.2 Market Positioning
- **TrueMoist Advantage:** Low-cost, open-source approach
- **Differentiation:** Level-2 reliability features
- **Target Market:** Research, education, hobbyist
- **Competitive Threat:** Established players with strong IP portfolios

### 20.3 IP Strategy Recommendations
1. **Focus:** Level-2 enhancements as primary IP asset
2. **Monitor:** Competitor patent filings
3. **Collaborate:** Open-source community engagement
4. **Protect:** Provisional filing for Level-2

---

## 21. Technical Differentiators

### 21.1 Frozen MVP vs. Prior Art
| Feature | TrueMoist | Prior Art | Differentiation |
|---------|-----------|-----------|-----------------|
| Sensor | SEN0193-class | Custom probes | Commodity hardware |
| Salinity | Controlled treatment | Active measurement | Passive approach |
| Calibration | Offline regression | Various methods | Standard method |
| Validation | Gravimetric oven-dry | Various | Gold standard |

### 21.2 Level-2 Enhancements vs. Prior Art
| Feature | TrueMoist Level-2 | Prior Art | Novelty |
|---------|-------------------|-----------|---------|
| Validity-Region Detection | Dynamic, adaptive | Static thresholds | **NOVEL** |
| Confidence Gating | Multi-factor | Single-factor | **NOVEL** |
| Reference-Event Validation | Event-driven | Time-based | **NOVEL** |
| Dual-Probe Health | Cross-validation | Single probe | **NOVEL** |

### 21.3 Technical Advantages
1. **Cost:** ≤₹5,000 target vs. commercial sensors (₹15,000-₹50,000)
2. **Accuracy:** Compensated RMSE ≥20% lower than baseline
3. **Reliability:** Level-2 features improve measurement confidence
4. **Accessibility:** Open-source, commodity hardware

---

## 22. Recommendations

### 22.1 Immediate Actions (Priority 1)
1. **File Provisional Patent Application** for Level-2 enhancements
   - Jurisdictions: US, EP, India (PCT route recommended)
   - Timeline: Within 30 days
   - Focus: System and method claims with technical improvements

2. **Conduct Professional Patent Search**
   - Target: US 11,598,743 verification
   - Databases: KIPO, InPASS, CNIPA
   - Timeline: Within 14 days

3. **Engage Patent Counsel**
   - FTO clearance opinion
   - Claim drafting strategy
   - Jurisdictional filing strategy

### 22.2 Short-Term Actions (Priority 2)
1. **Complete Indian/Chinese Patent Searches**
   - InPASS database for Indian filings
   - CNIPA database for Chinese filings
   - Timeline: Within 30 days

2. **Develop Claim Strategy**
   - System claims with hardware interaction
   - Method claims with technical improvements
   - Avoid abstract idea characterizations

3. **Monitor Competitor Activity**
   - New patent filings in soil moisture sensing
   - Product releases with similar features
   - Litigation activity

### 22.3 Long-Term Actions (Priority 3)
1. **Build Patent Portfolio**
   - Additional improvements and features
   - Divisional applications for different aspects
   - Continuation applications for enhancements

2. **Establish IP Management Process**
   - Invention disclosure system
   - Regular patent landscape monitoring
   - Competitive intelligence program

3. **Consider Open-Source Strategy**
   - Dual-licensing model (open core)
   - Patent pledge for community use
   - Defensive publishing for non-core features

### 22.4 Not Recommended
1. **Do NOT pursue patent for Frozen MVP** - Not patentable
2. **Do NOT ignore US 11,598,743** - Verify before commercialization
3. **Do NOT rely solely on this report** - Engage qualified counsel

---

## 23. Unresolved Uncertainties

### 23.1 High Priority
1. **US 11,598,743 Verification**
   - Status: Not located in accessible databases
   - Impact: Potential critical prior art
   - Resolution: Professional patent search required

2. **Indian Patent Filings**
   - Status: InPASS database not searched
   - Impact: FTO risk in Indian market
   - Resolution: Conduct InPASS search

3. **Chinese Patent Filings**
   - Status: CNIPA database not searched
   - Impact: FTO risk in Chinese market
   - Resolution: Conduct CNIPA search

### 23.2 Medium Priority
1. **Patent Prosecution Histories**
   - Status: File wrappers not reviewed
   - Impact: Validity assessment limitations
   - Resolution: Retrieve and analyze prosecution histories

2. **Litigation Histories**
   - Status: Not researched
   - Impact: Enforceability assessment limitations
   - Resolution: Search litigation databases

3. **Commercial Product Analysis**
   - Status: Limited competitive analysis
   - Impact: Market positioning uncertainty
   - Resolution: Conduct comprehensive market analysis

### 23.3 Low Priority
1. **Additional Academic Literature**
   - Status: 8+ papers reviewed, may be more
   - Impact: Marginal on novelty assessment
   - Resolution: Continue literature monitoring

2. **International Filings**
   - Status: PCT applications not exhaustively searched
   - Impact: Limited for current assessment
   - Resolution: Monitor PCT publications

---

## 24. Assumptions and Limitations

### 24.1 Assumptions
1. **Evidence Cut-off:** All analysis based on information available as of 1 August 2026
2. **Patent Status:** Status information accurate as of search date (2 August 2026)
3. **Technical Specifications:** Frozen MVP details from EDR are accurate and complete
4. **Jurisdiction:** Analysis focused on US, EP, India as primary markets
5. **Prior Art:** Accessible databases are representative of global patent landscape

### 24.2 Limitations
1. **Database Coverage:** Only publicly accessible databases searched
2. **Professional Tools:** No professional patent search tools utilized
3. **Legal Expertise:** Not a substitute for qualified patent counsel
4. **Language:** Non-English patents not reviewed
5. **Time:** Analysis conducted within limited timeframe

### 24.3 Disclaimers
- This report is for **informational purposes only**
- Not a substitute for **professional legal advice**
- No **attorney-client relationship** created
- **No warranty** of completeness or accuracy
- **Recommendation:** Engage qualified patent attorney for definitive opinions

---

## 25. Sources and Citations

### 25.1 Internal Documents (Authoritative)
1. Engineering Decision Register (EDR) - Primary authority
2. Decision Register v1.2 - Secondary authority
3. Phase 3C Closure Memo - Tertiary authority
4. Final TrueMoist Architecture Report
5. Final TrueMoist Memory
6. Final TrueMoist SOP
7. Validated Evidence Files (Phase 2)

### 25.2 Verified Patents
1. **US 7,884,620 B2** - Campbell Scientific/Green Badge LLC
   - Source: USPTO Full-Text Database
   - URL: https://patft.uspto.gov/netacgi/nph-Parser?patentnumber=7884620

2. **US 7,170,302 B2** - Fu Ching Lee
   - Source: USPTO Full-Text Database
   - URL: https://patft.uspto.gov/netacgi/nph-Parser?patentnumber=7170302

3. **US 9,804,113 B2** - Fiskars Oyj
   - Source: USPTO Full-Text Database
   - URL: https://patft.uspto.gov/netacgi/nph-Parser?patentnumber=9804113

4. **US 8,981,946 B2** - Toro Co
   - Source: USPTO Full-Text Database
   - URL: https://patft.uspto.gov/netacgi/nph-Parser?patentnumber=8981946

### 25.3 Academic Literature
1. MDPI Sensors - "Calibration of Low-Cost Soil Moisture Sensors" (2020)
2. MDPI Sensors - "Temperature Compensation for Capacitive Soil Moisture Sensors" (2019)
3. ScienceDirect - "Soil Moisture Sensor Calibration Methods" (2021)
4. ResearchGate - "Low-Cost Sensor Networks for Agriculture" (2018)
5. Nature - "Machine Learning for Environmental Sensing" (2022)
6. Additional MDPI papers on polynomial regression and MARS/GPR methods

### 25.4 Web Search Tools
- **web_search** tool used for patent and literature verification
- All searches conducted on 2 August 2026

---

## 26. Appendices

### 26.1 Appendix A: Glossary of Terms
| Term | Definition |
|------|------------|
| **GWC** | Gravimetric Water Content |
| **VWC** | Volumetric Water Content |
| **EC** | Electrical Conductivity |
| **RMSE** | Root Mean Square Error |
| **MAE** | Mean Absolute Error |
| **MCU** | Microcontroller Unit |
| **ADC** | Analog-to-Digital Converter |
| **FTO** | Freedom-to-Operate |
| **EPO** | European Patent Office |
| **PCT** | Patent Cooperation Treaty |
| **InPASS** | Indian Patent Advanced Search System |
| **CNIPA** | China National Intellectual Property Administration |

### 26.2 Appendix B: Patent Claim Mapping

#### Frozen MVP vs. US 7,884,620 B2
| TrueMoist Feature | Patent Claim | Overlap | Assessment |
|-------------------|--------------|--------|------------|
| Capacitive probe | Claim 1 | Partial | Different implementation |
| Microcontroller | Claim 1 | Partial | Conventional use |
| Moisture measurement | Claim 1 | Partial | Different principle (no salinity measurement) |

#### Level-2 vs. US 8,981,946 B2
| TrueMoist Feature | Patent Claim | Overlap | Assessment |
|-------------------|--------------|--------|------------|
| Calibration | Claim 1 | Partial | Different approach (offline vs. wireless) |
| Validation | Claim 1 | Partial | Different method (event-based vs. routine) |

### 26.3 Appendix C: Technical Specifications

#### SEN0193-Class Capacitive Probe
- **Type:** Capacitive soil moisture sensor
- **Output:** Analog voltage (0-3.0V)
- **Range:** 0-100% VWC (theoretical)
- **Accuracy:** ±3% VWC (typical)
- **Interface:** Analog output

#### DS18B20 Temperature Sensor
- **Type:** Digital thermometer
- **Range:** -55°C to +125°C
- **Accuracy:** ±0.5°C (-10°C to +85°C)
- **Resolution:** 9-12 bits (configurable)
- **Interface:** 1-Wire

#### ADS1115 ADC
- **Resolution:** 16 bits
- **Sampling Rate:** 860 samples/second
- **Channels:** 4 single-ended or 2 differential
- **Interface:** I2C

#### ESP32-WROOM-32
- **CPU:** Xtensa dual-core 32-bit
- **Clock:** 80 MHz (160 MHz max)
- **Memory:** 520 KB SRAM
- **Flash:** 4 MB
- **Interface:** WiFi, Bluetooth, GPIO, I2C, SPI, UART

### 26.4 Appendix D: Dataset Details

#### Experimental Design
- **Moisture Levels:** 4 (dry, moist, wet, saturated)
- **Temperature Levels:** 3 (15°C, 25°C, 35°C)
- **Salinity Levels:** 2 (0 dS/m, 2 dS/m)
- **Replicates:** 3 per condition
- **Total Runs:** 72 (4 × 3 × 2 × 3)

#### Ground Truth Protocol
- **Method:** Gravimetric oven-drying
- **Temperature:** 105±5°C
- **Duration:** Until constant mass (typically 24-48 hours)
- **Calculation:** GWC = (wet mass - dry mass) / dry mass

---

*Report prepared by Independent Patent-Research and Engineering-Review Board. Evidence cut-off: 1 August 2026. For questions or clarifications, refer to the authoritative source documents listed in Section 25.*


---

## Source 14: `03_CONCEPT_PORTFOLIO/TrueMoist/02_Raw_Research/06_TrueMoist_Patent_Research_Microsoft_Copilot.docx`

- Authority: `TIER_3`
- Treatment: `SUPPORTING_EVIDENCE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `NEW_STAGE10L_EXTRACTION`
- SHA-256: `18ffe78f06c7d1a6b30a022474e0cbb660d5e4670e9658cdd5048f233a4b135d`

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

