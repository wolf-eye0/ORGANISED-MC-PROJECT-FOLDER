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
