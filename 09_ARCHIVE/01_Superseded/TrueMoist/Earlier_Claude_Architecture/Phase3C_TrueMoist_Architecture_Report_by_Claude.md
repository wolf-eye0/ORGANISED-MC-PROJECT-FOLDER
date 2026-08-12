# Phase 3C — TrueMoist Final Engineering Architecture Synthesis
## Patent-Oriented Embedded Systems Innovation Pipeline — Project mC

**Prepared by:** Chief Engineering Review Board (synthesis of four independent Phase 3C Deep Research passes)
**Concept:** TrueMoist (Drift-Self-Correcting Soil Moisture Controller)
**Authoritative specification:** Engineering_Design_Review.md (EDR) → Phase3C_TrueMoist_SOP.md, taking precedence over Phase 3B, Phase 3A, Phase 2, the Decision Register, and PROJECT_CONCEPT_CONTEXT.md wherever they differ, per standing project convention
**Independent research inputs:** Mistral, Gemini, Perplexity, ChatGPT (commissioned Phase 3C Deep Research reports)
**Status:** Final — mandatory input to Phase 4 (Prototype Engineering)
**Date:** July 28, 2026

---

## How to read this report

This is a synthesis, not new research. Per the Phase 3C SOP, the mandate is to audit four independent research reports for concept fidelity, exclude (not average) mis-scoped material, resolve every disagreement the SOP names, and freeze one buildable architecture with a companion memory file. Unlike Phase 3A/3B, TrueMoist enters this phase with the tightest, least-contested evidence base in the portfolio (Phase 3B: "Very High" prototype success probability, the only concept with no live feasibility disagreement). That pattern holds here: all four Phase 3C reports converge on the same broad architecture family. There are exactly two live, named engineering disagreements — the EC/salinity strategy and the ADC decision — both resolved below with an explicit evidence trail, not a vote count.

---

## 1. Executive Architecture Decision

**Selected architecture:** Offline-trained, ridge-regularized second-order polynomial regression (Architecture D) running as static embedded inference on an ESP32-WROOM-32, reading a commodity capacitive soil-moisture probe and a waterproof DS18B20 through a mandatory external ADS1115 16-bit ADC (Architecture B-style measurement hardening), with soil salinity represented as a **controlled calibration variable** rather than a live runtime EC channel.

This is a **D+B hybrid**: Architecture D supplies the training/inference discipline (offline modeling, deterministic embedded coefficients, no on-device learning risk); Architecture B contributes only the external-ADC measurement rigor, not its live-EC subsystem. Architecture C (adaptive on-device recalibration) is explicitly rejected for the MVP and preserved as the concept's genuine long-term patent path.

**Readiness Classification:** ✅ **Architecture Ready with Mandatory Early Validation**

**Cost:** ₹2,080 (preferred, core build) / up to ₹2,330 with optional OLED / ₹3,180–3,380 worst-case (if a precision scale and drying equipment must also be purchased) — comfortably inside both the ₹3,000 preferred and ₹5,000 maximum ceilings.

---

## 2. Canonical Concept Restatement

TrueMoist is an affordable embedded intelligent sensing system whose engineering contribution is **not** moisture sensing itself but **local compensation of predictable measurement error** — temperature-driven dielectric drift, salinity/EC interference, sensor nonlinearity, drift, and repeatability limits — in an inexpensive capacitive soil-moisture probe. Per the EDR: the innovation is "not the soil moisture sensor itself, but the intelligent compensation of measurement errors and environmental influences affecting inexpensive sensors."

TrueMoist must **not** become a generic irrigation controller, a premium laboratory-grade probe, a universal calibration-free sensor, a cloud analytics platform, or a full precision-agriculture suite.

## 3. Engineering Hypothesis

Per the EDR (verbatim): *"A low-cost embedded system can intelligently compensate for sensor drift and environmental influences, allowing inexpensive soil moisture sensors to produce consistently reliable measurements suitable for practical irrigation support."* The Phase 3C SOP sharpens this to a testable form: a compensated moisture estimate must perform measurably better than the uncompensated estimate against the *same* gravimetric reference, under controlled disturbance.

## 4. Minimum Demonstrable Success (MDS)

Per the EDR: demonstrate that the prototype can detect and compensate for controlled sensor drift or environmental influences, producing more stable and repeatable soil-moisture estimates than an uncompensated low-cost sensor under equivalent test conditions. Concretely (synthesizing the SOP's seven-point MDS test): acquire raw sensor data → measure/represent temperature and salinity → produce both a raw and a compensated estimate → compare both against the same gravimetric reference → show a predefined, quantitative improvement under controlled disturbance → do all inference locally, with no continuous cloud dependency.

---

## 5. Evidence Audit of the Four Reports

All four reports performed an explicit "Canonical Concept Restatement" (or equivalent) before researching, and all four restated the EDR's Engineering Identity, Hypothesis, and MDS correctly — no concept-swap, no drift toward a generic irrigation controller or universal probe. This continues TrueMoist's unbroken track record across Phase 2, 3A, and 3B as the portfolio's most concept-faithful, least-contested concept. No sections are excluded on fidelity grounds.

| Report | Concept fidelity | Architecture family selected | Notable posture |
|---|---|---|---|
| **Mistral** | Correct, high specificity | Architecture B (live EC + mandatory ADS1115) | Only report to select live two-electrode EC sensing as the MVP path |
| **Gemini** | Correct, high specificity | Architecture D (calibration-only EC + mandatory ADS1115); explicitly rejects B and C outright | Most rigorous error-budget argument for the ADC; sharpest rejection of live EC on cost/complexity grounds |
| **Perplexity** | Correct, high specificity | Architecture B+D hybrid (calibration-only EC, **optional** ADS1115) | Only report treating the ADC as a Week-1/2 empirical question rather than a default |
| **ChatGPT** | Correct, high specificity | Architecture D-dominant with B-style hardening (calibration-only EC, ADS1115 included by default) | Explicitly rejects AD5933 as an over-engineered MVP default; frames itself as synthesizing competing Phase 3B viewpoints |

**Confidence per report:** All four are treated at **High** confidence — none exhibits the hallucination, source-quality, or completeness problems that depressed confidence for other concepts/reports in Phase 2/3A/3B. Differences between them are substantive engineering disagreements, not fidelity problems, and are resolved by evidence below, not by discarding any report.

---

## 6. Cross-Report Agreement Map

Unanimous across all four reports (treated as decision-grade, not re-litigated):

1. **Moisture sensor:** commodity capacitive probe (v2.0/YL-69/HL-69-class), analog output, low corrosion risk vs. resistive alternatives, directly suitable for compensation experiments precisely *because* its temperature/salinity sensitivity gives the algorithm a real error surface to correct.
2. **Temperature sensing:** soil temperature (not ambient) via waterproof DS18B20, co-located with the moisture probe.
3. **MCU:** ESP32-WROOM-32 primary, STM32F103 ("Blue Pill") fallback.
4. **Training paradigm:** offline training (Python/scikit-learn-class tooling), static coefficients deployed to firmware, embedded inference only — no on-device learning in the MVP.
5. **Compensation algorithm family:** multivariate linear/polynomial regression; TinyML and full adaptive recalibration explicitly out of scope for the MVP.
6. **Gravimetric ground truth:** 105°C oven-drying to constant mass as the non-negotiable physical reference; dehydrator/microwave fallback documented as increasing uncertainty, not a substitute of equal standing.
7. **Single homogeneous soil type** for the entire MVP calibration (per PDR-049), with grouped (not random-row) train/validation splitting to prevent data leakage.
8. **Power:** USB 5V benchtop power; no battery required for the MVP.
9. **Patent posture:** IP effort must stay on the software/compensation layer; custom probe or EC hardware risks the saturated Toro/Meter/Campbell/US 11,598,743 patent estate identified in Phase 2 (PDR-045).
10. **Analog front-end discipline:** breadboard only for Week-1 characterization, soldered perfboard connections from Week 2 onward to eliminate contact-resistance noise (PDR-050).

## 7. Disagreement Resolution

### 7.1 EC/Salinity Strategy — **RESOLVED: controlled calibration variable, no live runtime EC sensing in the MVP**

Three of four reports (Gemini, Perplexity, ChatGPT), working independently, converged on treating salinity as a **known, controlled experimental condition** during calibration rather than a live-instrumented soil channel. Only Mistral selected a live two-electrode galvanic EC measurement.

The three-report position is adopted as the MVP decision, for reasons that go beyond a vote count:
- **Technical:** reliable live soil-EC measurement requires AC bipolar-pulse excitation to avoid electrode polarization and electrolysis — a genuine analog-electronics design problem, not a firmware problem.
- **Team-fit evidence:** Phase 3B's own cross-report finding named "analog front-end electrical engineering" as the team's *one* real skill gap for this concept specifically. Adding a custom AC-excited EC circuit is exactly the kind of task that gap predicts will fail under a two-month deadline.
- **Patent-posture evidence:** Phase 2 (PDR-045) already directs TrueMoist's engineering effort away from custom sensing hardware and onto the software layer; a bespoke EC electrode circuit sits awkwardly close to "custom hardware probe" even though it measures a different variable than moisture.
- **Cost evidence:** Gemini's sourcing shows commercial lab-grade EC probes run ₹5,895–7,860 — enough alone to blow the ₹5,000 ceiling — while DIY electrodes reintroduce the same AC-excitation problem above.

Mistral's live-EC path is not discarded; it is preserved explicitly as the **first-listed Phase 6+ upgrade path** (Section 29), since it is the only path toward closing the loop with real field soil-EC rather than lab-prepared salinity bands.

### 7.2 External ADC (ADS1115) — **RESOLVED: mandatory by default, confirmed by a Week-1 gate rather than left open**

Three of four reports (Mistral, Gemini, ChatGPT) mandate the ADS1115; only Perplexity treats it as an optional Week-1/2 comparison. The SOP requires an error-budget argument rather than a bit-count assumption, so here it is:

| Parameter | ESP32 internal ADC | ADS1115 external ADC |
|---|---|---|
| Nominal resolution | 12-bit | 16-bit |
| Effective number of bits (ENOB), practical | ~9 bits (RF-coupled noise, reference-voltage drift, documented nonlinearity) | 16-bit differential, stable internal reference |
| LSB @ 3.3V | ~0.81 mV | ~0.06 mV (with PGA) |
| Approx. total error band | ±6.4 mV | ±0.3 mV |

The capacitive probe's active signal swing that encodes a ~0.1% moisture change is on the order of 10–50 mV — within an order of magnitude of the internal ADC's own error band. If the compensation regression is fit against a signal that size while the acquisition noise floor is comparable, the model risks fitting acquisition noise rather than the physical Maxwell-Wagner/salinity effect it exists to correct — precisely the failure mode Gemini's error-budget argument and Mistral's SNR calculation (1.56:1 internal vs. ~30:1 external) both independently reach.

Perplexity's caution is not wrong in principle — it correctly notes that sensor/soil variability can dominate ADC resolution in some designs — but it is the minority position on a question this synthesis board treats as cheap to de-risk: the ADS1115 costs ~₹120–150, a rounding error against the ₹3,000 preferred ceiling. Per the SOP's instruction to resolve ADC choice via error budget "or a mandatory Week-1 comparison gate" rather than leaving it open indefinitely: **the ADS1115 is included in the frozen architecture by default**, and Perplexity's internal-vs-external comparison is retained as **Week-1 Validation Gate 2** (Section 8) — an empirical confirmation of a decision already made on error-budget grounds, not a decision left pending.

### 7.3 Compensation model order and regularization — minor refinement, not a hard disagreement

All four converge on offline-trained regression; they differ on polynomial order and whether to regularize (Mistral: 2nd-order, 9 cross-terms, unregularized; Gemini: 1st-order baseline + 2nd-order with interaction terms; Perplexity: linear/low-order, ridge as an "optional upgrade"; ChatGPT: ridge-regularized 2nd-order as the primary MVP choice). Given the calibration dataset size settled on below (135 samples, Section 12) relative to a full 2nd-order model with cross-terms (~10 coefficients), the risk of overfitting flagged as "Medium" by three of four reports is real. **Ridge-regularized second-order polynomial regression is adopted as the primary model**, following ChatGPT's position — it strictly dominates an unregularized 2nd-order fit at negligible added firmware cost (a fixed regularization constant baked into the offline-trained coefficients; the MCU still just evaluates a polynomial) and directly addresses the overfitting risk the other three reports flag but do not fully mitigate.

### 7.4 Dataset scale — resolved toward the convergent mid-point

Proposed sample counts ranged from Perplexity's deliberately-reduced 72 (cut from an explicitly-computed "ambitious" 216) up to Gemini's 180, with Mistral (135) and ChatGPT (108) in between. Perplexity's reduction came at the cost of temperature levels (3→2) — but temperature is, per Phase 3A/3B/EDR, one of the *two* named confounders this entire concept exists to correct, so under-sampling it to capture project-management convenience is the wrong place to cut. **Mistral's design (5 moisture × 3 temperature × 3 salinity × 3 replicates = 135 samples) is adopted**: it preserves full 3-level coverage on both confounders, sits at the convergent mid-point of the four proposals, and matches the only report (Mistral) that also verified its own 8-week roadmap explicitly hits this number by Week 4.

---

## 8. Required Early Validation Gates (Week 1–2)

| Gate | Procedure | Pass threshold | Fail threshold | Fallback |
|---|---|---|---|---|
| **1. Raw sensor repeatability** | Fixed soil sample, 10 consecutive probe insertions, log raw ADC counts | σ < 50 counts (or equivalent stable-plateau behavior) | σ ≥ 50 counts / no stable plateau within 20 min | Swap probe unit (2 purchased for exactly this reason); re-characterize |
| **2. Internal vs. external ADC comparison** | Read the identical probe state via ESP32 internal ADC and ADS1115 side by side | ADS1115 noise band measurably narrower; internal ADC error ≥1 mV confirms mandate | Internal ADC error <1 mV *and* regression residuals dominated by sensor/soil noise, not ADC noise | Retain ADS1115 regardless (cost is trivial; gate is confirmatory, not a go/no-go on inclusion) |
| **3. Gravimetric workflow repeatability** | Three independent dry/wet/dry cycles of the same soil batch through the full weigh→dry→weigh pipeline | σ < 0.5% VWC across replicates | σ ≥ 0.5% VWC | Extend drying time to strict constant-mass criterion; verify scale calibration |
| **4. Soil-packing sensitivity** | Same moisture/temperature/salinity condition, 3 independently packed containers | Variance attributable to packing is smaller than the temperature/salinity effect being measured | Packing variance swamps the confounder signal | Introduce a fixed-mass compaction jig (Section 20) before proceeding to full dataset collection |
| **5. Probe insertion sensitivity** | 10 repeated insertions into one stable sample with a fixed depth guide | Variability does not exceed Gate 1's baseline repeatability | Insertion variability materially exceeds Gate 1 | Adopt/refine the insertion jig; mark fixed depth on probe body |
| **6. Pilot dataset feasibility** | Run ~15–20 samples end-to-end through the full pipeline (Week 3) before committing to the full 135-sample plan | Full pipeline (electrical → gravimetric → CSV) completes without protocol breakage | Any stage (electrical, mechanical, or gravimetric) fails repeatedly | Revise protocol before Week 4 full collection begins |

If Gates 1, 3, or 4 fail and cannot be resolved by Week 2, the architecture falls back to Architecture A (Section 9) with temperature-only compensation, dropping salinity as a modeled variable entirely rather than as a runtime sensor — this preserves the MDS (a compensated-vs-uncompensated comparison still exists) at reduced scope.

---

## 9. Candidate Architecture Families

| Family | Summary | Verdict |
|---|---|---|
| **A — Minimal Compensation Demonstrator** | Capacitive probe + DS18B20, internal ADC, controlled salinity, static/linear regression, USB serial | Retained as the **sole fallback** if Section 8's gates fail |
| **B — Measurement-Focused Compensated Sensor** | Adds live EC instrumentation + external ADC | **Rejected as a whole**; its external-ADC half is retained, its live-EC half is rejected (Section 7.1) |
| **C — Adaptive Embedded Calibration** | On-device recursive recalibration | **Rejected for the MVP** — overfitting, catastrophic-forgetting, and compute-stability risk under a two-month timeline (unanimous across reports that considered it); preserved as the concept's genuine long-term patent direction (Section 30) |
| **D — Offline Training / Embedded Inference** | Offline-trained coefficients, static embedded inference | **Selected as the primary paradigm**, hardened with B's external ADC |

---

## 10. Comparative Decision Matrix

| Criterion | A (fallback) | B (rejected) | C (rejected) | **D+B-hardened (selected)** |
|---|---|---|---|---|
| Hypothesis validation | Medium | High | High | **High** |
| Cost | Lowest (~₹700) | Highest (custom EC pushes toward/over ceiling) | Moderate | **Low (~₹2,080)** |
| Team fit (CS/Cybersecurity) | High | Low (analog EE gap) | Low (edge-ML risk) | **Very High** |
| Validation clarity | High | Low (live EC noise confounds) | Low (moving target) | **Very High** |
| Overfitting/failure risk | Low | Moderate | Very High | **Low (ridge-regularized)** |
| Patent-angle preservation | Low | Moderate | High (but unbuildable in 2 months) | **Adequate for MVP; true angle deferred (Section 30)** |

---

## 11. Final Selected Architecture

| Subsystem | Selection |
|---|---|
| Moisture sensor | Commodity capacitive soil-moisture probe (v2.0/YL-69/HL-69-class), analog output; **2 units purchased** to characterize sensor-to-sensor variability (Gate 1) |
| Temperature sensor | Waterproof DS18B20, 1-Wire, co-located with the moisture probe at soil depth |
| EC/salinity | **Controlled calibration variable only** — no live runtime EC channel (Section 7.1) |
| ADC | **ADS1115 16-bit external ADC, mandatory by default** (Section 7.2) |
| MCU | ESP32-WROOM-32 (primary); STM32F103 "Blue Pill" (fallback) |
| Analog front end | Breadboard in Week 1 only; soldered perfboard from Week 2; optional MCP6002/LMV358 buffer stage; RC low-pass filtering; short leads, decoupling capacitors |
| Compensation algorithm | Offline-trained, **ridge-regularized 2nd-order polynomial regression** (Temp, Raw, controlled-salinity-class as inputs; cross-terms retained) |
| Training method | Offline (Python/scikit-learn-class tooling); coefficients hard-coded to firmware as a static array |
| Embedded inference | Local polynomial evaluation only, <1 ms per sample, no on-device training |
| Calibration procedure | Single homogeneous soil; 5 moisture × 3 temperature × 3 salinity × 3 replicates = 135 samples (Section 12) |
| Gravimetric reference | 105°C oven-drying to constant mass (Section 13) |
| Mechanical test rig | Rigid plastic container, fixed insertion jig, mass-controlled compaction (Section 15) |
| Logging/output | USB serial CSV, mandatory; 0.96" I²C OLED, optional for live demo only |
| Power | USB 5V; no battery |
| Cost | ~₹2,080 preferred core; ~₹3,380 worst-case (Section 21) |
| Readiness | Architecture Ready with Mandatory Early Validation |

## 12. System Block Diagram

```
┌────────────────────────────────────────────────────────────────────┐
│                         TRUEMOIST ARCHITECTURE                      │
├────────────────────────────────────────────────────────────────────┤
│  Capacitive Probe ×2   DS18B20 (soil temp)   Controlled salinity    │
│  (analog voltage)      (1-Wire, soil depth)   (calibration prep     │
│         │                    │                only — no soil       │
│         └──────────┬─────────┘                runtime channel)     │
│                     ▼                                               │
│              ┌─────────────────┐                                    │
│              │  ADS1115 16-bit │  ◄── mandatory (Section 7.2)        │
│              │  ext. ADC (I2C) │                                    │
│              └────────┬────────┘                                    │
│                       ▼                                             │
│              ┌───────────────────────┐                              │
│              │   ESP32-WROOM-32      │                              │
│              │  static poly-regr.    │  ◄── ridge coeffs, offline-  │
│              │  inference (<1ms)     │       trained (Section 7.3)  │
│              └──────────┬────────────┘                              │
│         ┌───────────────┼───────────────┐                          │
│         ▼                                ▼                          │
│  USB Serial (CSV)                  Optional OLED (demo only)        │
│         │                                                            │
│         ▼                                                            │
│  Offline: gravimetric ground truth ↔ raw vs. compensated comparison  │
└────────────────────────────────────────────────────────────────────┘
```

## 13. Moisture Sensing Subsystem

Commodity capacitive probe, PCB-based, epoxy/solder-mask-shielded electrodes to avoid galvanic corrosion (unlike bare resistive probes, unanimously rejected across all four reports). Output: analog voltage inversely proportional to soil dielectric permittivity, roughly 3.0V dry-air down to a lower saturated-soil voltage. Two units purchased to characterize probe-to-probe variability before committing to the full dataset (Gate 1). This sensor's known temperature/salinity sensitivity is not a defect to engineer away — it is precisely the error surface the compensation algorithm exists to correct.

## 14. Temperature Sensing Subsystem

Waterproof DS18B20, ±0.5°C accuracy (−10 to 85°C range), 1-Wire digital interface (single GPIO, 4.7kΩ pull-up). Placed ~1–2 cm from the moisture probe at the same depth — close enough to capture the thermal state of the exact soil volume the moisture probe senses, far enough to avoid its metal tip perturbing the probe's fringing electric field. Ambient-air temperature sensing is explicitly rejected as a substitute: soil's thermal inertia means ambient air lags soil temperature, breaking the correlation the compensation model depends on.

## 15. EC / Salinity Strategy

**Controlled calibration variable, not a live runtime sensor** (resolved in Section 7.1). During dataset preparation, soil batches are mixed with distilled water (baseline), a moderate salt/fertilizer-equivalent solution (~1–2 mS/cm), and a high-salinity solution (~4–5 mS/cm) using known NaCl concentrations. The regression model is trained with a coded salinity-class term (not a live-measured EC value), proving that compensation works when the salinity state is known — which directly satisfies the MDS requirement to "measure or rigorously represent" salinity — without requiring a fragile, AC-excited electrode circuit in the runtime hardware.

## 16. Analog Front End and ADC Decision

ADS1115 mandatory by default per the error-budget argument in Section 7.2, confirmed (not decided) by Week-1 Gate 2. Front end: breadboard for Week 1 characterization only; soldered perfboard from Week 2 (PDR-050); optional MCP6002/LMV358 high-input-impedance buffer between probe and ADC to prevent loading; RC low-pass filtering tuned so step changes in moisture appear as smooth multi-second transitions rather than noise spikes; short leads and local decoupling capacitors near ADS1115 and ESP32 power pins to suppress Wi-Fi-radio-coupled digital noise (present even with Wi-Fi disabled in firmware, per Gemini's specific finding).

## 17. MCU and Embedded Architecture

ESP32-WROOM-32 (dual-core Tensilica, 240 MHz, hardware FPU, 520 KB SRAM, 4 MB flash). Chosen over STM32F103 for its integrated FPU (STM32F103 requires slower software floating-point emulation for the polynomial math) and the team's existing Arduino-ecosystem familiarity — reducing implementation friction directly matters given the team's one acknowledged gap is analog EE, not firmware. STM32F103 remains the documented fallback if ESP32 procurement fails.

## 18. Sampling and Preprocessing

Raw ADC sampling at ~1–10 Hz; a moving-average filter (10–50 samples) applied in firmware before the regression is evaluated, to suppress high-frequency electrical noise without distorting the slower thermal/salinity drift signal the model needs to see. Minimum 5–20 minute post-insertion equilibration before any reading is logged (probe warm-up behavior, confirmed across three reports).

## 19. Compensation Algorithm

Offline-trained, ridge-regularized second-order multivariate polynomial regression (Section 7.3):

```
VWC_comp = a + b·Raw + c·Temp + d·Sal + e·Raw² + f·Temp² + g·Raw·Temp + h·Raw·Sal + i·Temp·Sal
```

where `Raw` is the ADS1115-stabilized probe reading, `Temp` is DS18B20 soil temperature, and `Sal` is the coded (not live-measured) calibration salinity class. Coefficients are fit offline (Python/scikit-learn-class ridge regression), validated via grouped/held-out-condition cross-validation, then hard-coded into ESP32 firmware as a fixed array (~10 coefficients, well under 1 KB). Baseline comparator: unregularized first-order linear regression, retained to demonstrate the compensated model's incremental value rather than asserting it. TinyML, random forests, and full adaptive recalibration are explicitly out of scope for the MVP (Section 22).

## 20. Calibration Dataset Design

Single homogeneous, sieved local soil (e.g., a sandy loam or loam, documented once for the batch used). Design (Section 7.4): **5 moisture levels × 3 temperature levels × 3 salinity levels × 3 replicates = 135 samples.**

- Moisture: 5 levels spanning air-dry to near-saturation (e.g., 5%, 15%, 25%, 35%, 45% gravimetric water content).
- Temperature: 3 controlled levels (e.g., ~15°C, ~25°C, ~35°C).
- Salinity: 3 controlled classes (baseline/distilled, moderate, high — known NaCl concentrations).
- Replicates: 3 independent physical soil preparations per condition, to separate physical repeatability from electronic noise.

**Split:** grouped by physical batch — all readings from one physical soil preparation stay entirely in either training or validation, never split across both (prevents leakage). Target split ~100 training / ~35 validation samples. One temperature or salinity block is additionally held out entirely (leave-one-condition-out, per Gemini/Perplexity) as a generalization check beyond the standard split.

## 21. Gravimetric Ground-Truth Procedure

Standard soil-science reference: θ_g = (m_wet − m_dry) / m_dry, on a dry-mass basis. Procedure: tare container → weigh wet soil+container → oven-dry at 105 ± 5°C for ≥24 hours or to constant mass → cool in a desiccator → weigh dry soil+container → compute θ_g. Scale resolution of 0.01 g preferred; a 1 g resolution kitchen scale is an acceptable fallback with explicitly documented increased uncertainty. If a 105°C lab oven is unavailable, a food dehydrator (60–80°C, extended time, repeated weighing to <0.1 g change) is the preferred fallback; microwave drying is a last-resort option only, with explicitly flagged bias risk from uneven heating/organic combustion.

## 22. Mechanical Soil-Test Rig

Rigid plastic or PVC container, ~500 mL–1 L (approx. 8–12 cm diameter, 10–15 cm depth) — deformable containers are rejected, since compaction-induced volume change corrupts the packing-density control this rig exists to provide. Soil sieved and mixed to target moisture/salinity in a separate container before transfer, to avoid vertical gradients. Packing controlled via a fixed-mass compaction plate/jig applied for a consistent duration, to a marked depth. Probe inserted vertically via a 3D-printed or drilled alignment guide, to a fixed depth (~6–8 cm), avoiding container walls. DS18B20 inserted ~1–2 cm laterally from the probe at the same depth. Equilibration: 20–30 minutes post-packing before any reading; each container uniquely labeled and traceable to its gravimetric measurement pair.

## 23. Data Logging and Dataset Schema

USB serial, mandatory. CSV schema: `sample_id, timestamp, raw_adc_value, temp_C, salinity_class, raw_uncomp_VWC, comp_VWC, reference_VWC, model_version`. No SD card and no cloud connectivity required for the MVP. An optional 0.96" I²C OLED may display raw/compensated/reference values side-by-side for live demonstrations (recommended, not mandatory — avoids "gold-plating" the prototype per the SOP's own caution against over-scoping the interface).

## 24. Validation Metrics and Pass Criteria

**Primary metric: RMSE** between the compensated moisture estimate and gravimetric reference, on the validation split (3-of-4 report convergence: Gemini, Perplexity, ChatGPT all select RMSE as primary; Mistral's MAE-based framing is retained as a secondary/equivalent check). **Secondary metrics:** MAE, R², and disturbance-specific sensitivity (change in error per °C temperature step; change in error per salinity class step) — the MDS explicitly requires improvement to be demonstrated under controlled disturbance, not just in aggregate.

**Success threshold:** ≥25% reduction in RMSE for the compensated estimate vs. the uncompensated raw estimate, against the same gravimetric reference, across the validation set — the convergent point across the four reports' proposed ranges (20–30%). Minimum acceptable floor: 20% reduction (below which the improvement is not considered demonstrated). This is an engineering target set by this synthesis, not a published external standard, chosen because it sits inside every individual report's own proposed range.

## 25. Prototype Test Matrix

| # | Test | Purpose | Pass rule |
|---|---|---|---|
| 1 | Same moisture, varying temperature | Isolate temperature-compensation effectiveness | Compensated RMSE and temperature-sensitivity both materially lower than raw |
| 2 | Same moisture, varying (calibration) salinity | Isolate salinity-compensation effectiveness | Compensated error less sensitive to salinity class than raw |
| 3 | Full moisture sweep, fixed temp/salinity | Overall calibration-curve quality | RMSE reduction ≥25%; R² improved |
| 4 | Repeated wetting/drying cycle | Hysteresis and drift across cycles | Compensated estimate shows reduced hysteresis/drift vs. raw |
| 5 | Sensor warm-up / short-term drift | Characterize post-insertion stabilization | Stable window identified; model uses only the stable region |
| 6 | Repeated insertion/repositioning | Sensitivity to insertion technique | Compensation does not amplify insertion-induced noise |
| 7 | Raw vs. compensated global comparison | Headline demonstration | Global RMSE reduction ≥25%; clear plot |
| 8 | Held-out condition (LOCO) | Generalization beyond trained conditions | Held-out RMSE stays within a reasonable margin of training RMSE — no overfitting collapse |
| 9 | Internal vs. external ADC (Gate 2, formalized) | Confirm ADC decision empirically | ADS1115 shows a measurably narrower noise band |
| 10 | Fresh-batch transfer | Calibration applies to an independently-prepared batch of the same soil | Performance comparable to original validation batches |

## 26. Electrical and Power Architecture

USB 5V input; ESP32 onboard LDO regulates 3.3V for MCU, DS18B20, ADS1115, and probe supply as needed. Estimated current draw: ESP32 ~80–200 mA (Wi-Fi-dependent, though Wi-Fi is unused at runtime), DS18B20 ~1 mA per conversion, capacitive probe ~5–20 mA, ADS1115 ~150 µA — comfortably under a standard 500 mA–2A USB supply, giving at minimum a 2–10× safety margin. No battery required for this benchtop MVP; if a battery is added later for field demonstration, a separate regulator and brownout-monitoring circuit would be needed (explicitly deferred).

## 27. User Interface and Demonstration

USB serial + CSV is the required, sufficient interface. Optional 0.96" I²C OLED for standalone live demos, showing raw/compensated/reference values and current condition. No LCD, buzzer, smartphone app, or cloud dashboard — avoiding unnecessary scope per the SOP's own caution against interface "gold-plating" distracting from the measurement/compensation chain that is the actual engineering content.

## 28. Costed BOM

| Component | Qty | Price (₹) |
|---|---|---|
| ESP32-WROOM-32 DevKitC | 1 | 450 |
| ADS1115 16-bit ADC module | 1 | 140 |
| Capacitive soil-moisture probe (v2.0-class) | 2 | 200 |
| DS18B20 waterproof probe | 1 | 220 |
| Op-amp buffer (MCP6002/LMV358) | 1 | 70 |
| Perfboard, headers, resistors, capacitors | 1 set | 200 |
| Breadboard + jumper wires (Week 1 only) | 1 set | 150 |
| Soil containers (~12, plastic, 500 mL–1 L) | 12 | 250 |
| Insertion/compaction jig materials | 1 set | 150 |
| Lab-grade NaCl (500 g, salinity prep) | 1 | 250 |
| USB cable | 1 | 100 |
| Contingency (~10%) | — | 200 |
| **Core Preferred Total** | | **≈ ₹2,080** |
| *Optional:* 0.96" I²C OLED | 1 | +200–250 |
| *If needed:* 0.01 g precision scale | 1 | +350–400 |
| *If needed:* fallback dehydrator | 1 | +650–700 |
| **Worst-Case Total** (OLED + purchased scale + dehydrator) | | **≈ ₹3,180–3,380** |

Both totals sit comfortably inside the ₹5,000 ceiling; the core preferred total is well under the ₹3,000 preferred target even before accounting for the likely availability of institutional oven/scale access.

## 29. Compute, Memory, Storage, and Power Budget

Flash: firmware, drivers (1-Wire, I2C, ADS1115 library), and coefficient storage total ~200–250 KB of the ESP32's 4 MB flash (~6% utilization). SRAM: moving-average buffer plus coefficient array use well under 15 KB of 520 KB SRAM (~2–3%). CPU: polynomial evaluation with ~10 coefficients executes in well under 1 ms using the hardware FPU — negligible relative to any timing budget. Power: see Section 26. All four reports agree this concept carries essentially zero compute/memory/power risk; the entire engineering risk of the project sits in calibration discipline, not resource constraints (consistent with Phase 3B's own finding that TrueMoist's dominant risk dimension is "empirical calibration discipline").

## 30. Risk Register

| Risk | Severity | Mitigation |
|---|---|---|
| Inability to establish repeatable gravimetric ground truth | **High** (universal top risk, all four reports) | Strict 105°C/24h protocol; replicate drying cycles (Gate 3); document any fallback-method uncertainty explicitly |
| Electrical noise masking the fine compensation signal | High (addressed, not eliminated, by ADS1115) | Mandatory external ADC; soldered AFE from Week 2; decoupling capacitors; short leads |
| Soil packing/insertion variability | High | Fixed-mass compaction jig; fixed-depth insertion guide; Gates 4–5 |
| Moisture-salinity confounding | Medium-High | Salinity strictly controlled per-batch, never mixed mid-run; interaction terms in the regression |
| Model overfitting given ~135-sample dataset | Medium (mitigated) | Ridge regularization; grouped + held-out-condition validation; 2nd-order ceiling (no higher-order/ML escalation in MVP) |
| Sensor-to-sensor variability | Medium | Two probe units purchased and characterized (Gate 1) before full dataset collection |
| Calibration workload/schedule overrun | Medium-High | Structured 8-week roadmap (Section 32) with hard Week-4 dataset-complete gate |
| Failure to demonstrate measurable improvement | **Critical if triggered** | Kill criterion below; fallback to Architecture A, narrower temperature-only claim |

**Kill factors:**
1. Gravimetric ground truth cannot be made repeatable (σ persistently ≥0.5% VWC after mitigation).
2. Analog noise floor cannot be brought under the compensation signal even with the ADS1115 and soldered AFE.
3. No model (baseline through ridge-regularized 2nd-order) achieves ≥20% RMSE reduction by the end of Week 7 — this is the hard floor below which the MDS is not considered met.

## 31. Rejected Alternatives

- **Live/direct soil EC sensing** (two-electrode galvanic, four-electrode Wenner array, or AD5933 frequency-domain impedance analysis) — rejected for the MVP on AC-excitation complexity, team analog-EE skill gap, and (for commercial EC probes) budget grounds (Section 7.1). AD5933 specifically rejected as an over-engineered MVP default per ChatGPT's analysis: it "adds excitation design, calibration, spectral interpretation, and extra integration work" without eliminating the underlying calibration burden. Preserved as a Phase 6+ upgrade path.
- **ESP32 internal ADC as the sole ADC** — rejected on error-budget grounds (Section 7.2); Gate 2 is confirmatory, not decisional.
- **Adaptive/recursive on-device recalibration (Architecture C)** — rejected for the MVP timeline; overfitting and catastrophic-forgetting risk on a two-month schedule. This is the concept's actual long-term patent direction, deliberately deferred (Section 33).
- **Custom moisture-probe hardware** — rejected per Phase 2/PDR-045; the Toro/Meter/Campbell/US 11,598,743 patent estate makes this a Freedom-to-Operate risk, not merely an engineering-effort question.
- **TinyML / random forest / neural-network compensation** — rejected for the MVP; overfitting risk on a 135-sample dataset and unnecessary interpretability loss for no demonstrated accuracy gain at this scale.
- **SD-card logging** — rejected as unnecessary; USB serial CSV is sufficient and simpler.
- **Battery power** — rejected for the MVP; adds brownout-analysis risk with no benefit to proving the compensation hypothesis on a benchtop rig.

## 32. Patent and Innovation Implications

**Engineering differentiation (real, but bounded):** rigorous gravimetric calibration of a commodity capacitive probe, explicit dual-confounder (temperature + controlled salinity) modeling, and a documented, honest improvement claim over raw output — this is a genuine measurement-chain contribution, not a basic sensor-integration exercise.

**Semester-project novelty:** the disciplined dataset design (grouped splits, held-out-condition validation, gravimetric traceability per sample) and the demonstrated embedded deployment of a ridge-regularized regression on a sub-₹500 MCU are legitimate, presentable academic contributions.

**Actual patentability — the honest limit:** per the SOP's explicit instruction, ordinary multivariate/polynomial regression compensating a commodity sensor is **not, on its own, patentable** — this matches every report's own caution and Phase 2's finding that the hardware-compensation-circuit space is already saturated by Toro/Meter/Campbell, with the sharpest named fence (US 11,598,743, active to ~2040) squarely covering dual-parameter (temperature+EC) compensation circuits of exactly this shape.

**The real patent path, explicitly deferred, not abandoned:** Phase 2's independent, two-source-corroborated finding (Kimi and Gemini in Phase 2, working independently) is that the *only* defensible white space is an **on-node, event-driven, self-updating recalibration algorithm** — precisely Architecture C, which this Phase 3C synthesis rejects for the MVP on timeline/overfitting grounds (Section 9). This is a genuine, load-bearing tension worth stating plainly: **the MVP selected here is the right engineering choice for a two-month prototype, but it is deliberately not the concept's actual patent-bearing feature.** The static regression's role is to first prove the compensation hypothesis at all, cheaply and reliably; the adaptive self-calibration layer that would carry real IP weight remains a Phase 6+/post-validation-sprint research item, exactly as Phase 2 (PDR-045, and the Phase 2 "Hold pending validation sprint" recommendation) already anticipated. **Freedom-to-operate:** staying on the software side, avoiding custom probe/EC hardware, and avoiding replication of dual-frequency bridge-type circuits keeps FTO risk low; any future filing still requires formal claim-charting against US 11,598,743 and the broader Campbell/Meter/Toro estate.

## 33. Team Allocation

| Member | Role | Primary responsibilities | Critical path? |
|---|---|---|---|
| 1 | Embedded Integration Lead | ESP32 firmware, ADS1115/DS18B20 drivers, polynomial inference, CSV logging | ✅ Yes |
| 2 | Data & Compensation Lead | Dataset design execution, offline ridge-regression training, held-out validation, metrics | ✅ Yes |
| 3 | Hardware & Validation Lead | Analog front-end soldering, mechanical rig, gravimetric protocol, sensor characterization | ✅ Yes |
| 4 | Learner (support) | CSV/logging utilities, optional OLED UI, assists soil weighing/mixing | ❌ No |
| 5 | Documentation & Support | BOM tracking, lab records, figures, presentation, demo coordination | ❌ No |

No critical-path task is assigned solely to Members 4 or 5, consistent across all four source reports.

## 34. Eight-Week Roadmap

| Week | Focus | Key deliverable | Gate |
|---|---|---|---|
| 1 | Component verification; Gates 1–2 (repeatability, ADC comparison); breadboard AFE | ADC decision confirmed; probe characterization | ✅ Gate 1–2 |
| 2 | Solder AFE to perfboard; build mechanical rig; Gates 3–5 (gravimetric, packing, insertion) | Stable hardware chain; rig ready | ✅ Gate 3–5 |
| 3 | Pilot dataset (~15–20 samples) end-to-end | Pipeline validated; protocol refined | ✅ Gate 6 |
| 4 | Full calibration dataset collection | 135 samples collected and labeled | ✅ M4 |
| 5 | Offline model training (baseline linear → ridge-regularized 2nd-order); grouped + held-out validation | Trained model, validation metrics | ✅ M5 |
| 6 | Embedded deployment; firmware/offline cross-check | Working on-device compensation matching offline predictions | ✅ M6 |
| 7 | Full prototype test matrix (Section 25); comparative demonstration | RMSE-reduction result against the ≥25%/≥20% threshold | ✅ M7 |
| 8 | Repeatability/fresh-batch tests; documentation; final demo | Final report, presentation, working demo | ✅ M8 |

## 35. Phase 4 Readiness Decision

**✅ Architecture Ready with Mandatory Early Validation.**

All required architecture-selection inputs are frozen: sensing subsystem, EC strategy, ADC decision, MCU, compensation algorithm, calibration dataset design, gravimetric procedure, mechanical rig, logging, power, costed BOM, resource budget, risk register, rejected alternatives, and patent posture. The two genuine engineering disagreements the four independent reports raised (EC strategy, ADC necessity) are resolved with an explicit evidence trail rather than deferred. The only work explicitly left to Phase 4 is empirical confirmation via the Week 1–2 gates (Section 8) — which is a validation step, not an open architecture question.

---

## 36. Project Decision Register Updates

**Existing PDR entries — status changes:**

- **PDR-031** (TrueMoist Compensation Method): **Accepted.** Finalized as offline-trained, ridge-regularized 2nd-order multivariate polynomial regression (Temp, Raw, coded-salinity-class inputs). Supersedes the prior "provisional architecture selection" status.
- **PDR-032** (TrueMoist ADC Selection): **Accepted — resolved.** ADS1115 is mandatory by default, justified by error-budget analysis (Section 7.2); Week-1 Gate 2 is confirmatory only. Supersedes prior "open question" status.
- **PDR-045** (TrueMoist Custom Hardware IP Abandonment): **Reaffirmed and extended.** All IP effort remains confined to the software/compensation layer; this Phase 3C synthesis additionally excludes custom live-EC electrode hardware from the MVP runtime scope for the same reason (Section 7.1), not just custom moisture-probe hardware.
- **PDR-048** (TrueMoist Gravimetric Validation Standard): **Accepted — finalized.** 105°C/24h-to-constant-mass, 0.01g preferred scale resolution, dehydrator/microwave fallback explicitly documented as increasing (not equalizing) uncertainty.
- **PDR-049** (TrueMoist Single-Soil Limit): **Accepted — finalized.** Soil scope is one homogeneous, sieved local soil (e.g., sandy loam or loam), documented once per calibration batch.
- **PDR-050** (TrueMoist AFE Soldering): **Accepted — finalized.** Breadboard permitted only for Week 1 characterization; soldered perfboard mandatory from Week 2 onward.

**New PDR entries:**

- **PDR-058 — TrueMoist EC/Salinity Strategy.** *Decision:* Represent salinity as a controlled calibration variable only; no live runtime soil-EC channel in the MVP. *Rationale:* AC-excitation/electrode-polarization complexity exceeds team's analog-EE capability; commercial EC probes alone risk the budget ceiling; keeps IP effort off custom sensing hardware. *Source:* This report, Section 7.1. *Decision type:* Final decision. *Related:* PDR-031, PDR-045.
- **PDR-059 — TrueMoist Moisture Sensor Selection.** *Decision:* Commodity capacitive probe (v2.0/YL-69/HL-69-class); 2 units purchased for sensor-to-sensor characterization. *Source:* This report, Section 13. *Decision type:* Final decision. *Related:* PDR-031.
- **PDR-060 — TrueMoist Temperature Sensor & Placement.** *Decision:* Waterproof DS18B20, soil-depth co-located ~1–2 cm from the moisture probe; ambient-air sensing explicitly rejected as a substitute. *Source:* This report, Section 14. *Decision type:* Final decision. *Related:* PDR-031.
- **PDR-061 — TrueMoist Calibration Dataset Design.** *Decision:* 5 moisture × 3 temperature × 3 salinity × 3 replicates = 135 samples; grouped train/validation split plus one held-out (LOCO) block. *Source:* This report, Section 20. *Decision type:* Final decision. *Related:* PDR-031, PDR-049, PDR-048.
- **PDR-062 — TrueMoist Validation Metrics & Success Threshold.** *Decision:* RMSE primary metric; ≥25% reduction target (≥20% minimum floor) vs. gravimetric reference, compensated vs. uncompensated. *Source:* This report, Section 24. *Decision type:* Final decision. *Related:* PDR-031, PDR-048.
- **PDR-063 — TrueMoist Mechanical Test Rig Standard.** *Decision:* Rigid plastic container (~500 mL–1 L), fixed-depth insertion jig, mass-controlled compaction, 20–30 min equilibration. *Source:* This report, Section 22. *Decision type:* Final decision. *Related:* PDR-049.
- **PDR-064 — TrueMoist Interface & Logging.** *Decision:* USB serial CSV mandatory; OLED optional/demo-only; no SD card, no cloud. *Source:* This report, Section 23. *Decision type:* Final decision. *Related:* None.
- **PDR-065 — TrueMoist Power Architecture.** *Decision:* USB 5V only; no battery for the MVP. *Source:* This report, Section 26. *Decision type:* Final decision. *Related:* None.
- **PDR-066 — TrueMoist Phase 3C Architecture Selection.** *Decision:* Primary architecture = Offline-trained/embedded-inference (D) hardened with an external ADC (B-style), controlled-salinity EC strategy; fallback = Architecture A (temperature-only) if Section 8 gates fail. *Source:* This report, Sections 1, 9–11. *Decision type:* Final decision. *Related:* PDR-031, PDR-032, PDR-058.
- **PDR-067 — TrueMoist Compensation Model Regularization.** *Decision:* Ridge-regularized 2nd-order polynomial regression adopted over an unregularized fit, given ~135-sample dataset size relative to model complexity. *Source:* This report, Section 7.3, 19. *Decision type:* Final decision. *Related:* PDR-031.
- **PDR-068 — TrueMoist Patent Scope Refinement.** *Decision/Open question:* The Phase 3C MVP (static regression) is confirmed as not independently patentable; the concept's actual patent path (on-node adaptive self-calibration, per Phase 2) is explicitly deferred to Phase 6+/a post-MVP validation sprint, not abandoned. *Source:* This report, Section 32. *Decision type:* Recommendation / carried-forward open question. *Related:* PDR-045, PDR-012.

---

## 37. Phase 3C TrueMoist Memory

See companion file `Phase3C_TrueMoist_MEMORY.md` for the concise continuity record.

---

*Document Version: 1.0 | Date: July 28, 2026 | Status: Final — Phase 3C TrueMoist Complete*
