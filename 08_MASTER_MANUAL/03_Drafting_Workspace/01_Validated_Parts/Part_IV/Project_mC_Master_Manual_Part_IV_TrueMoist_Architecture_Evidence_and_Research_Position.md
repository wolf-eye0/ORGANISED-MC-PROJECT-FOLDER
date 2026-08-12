# Project mC Master Manual

## Part IV — TrueMoist Architecture, Evidence and Research Position

## Document control

| Field | Value |
|---|---|
| Document | Project mC Master Manual — Part IV |
| Controlled filename | `Project_mC_Master_Manual_Part_IV_TrueMoist_Architecture_Evidence_and_Research_Position.md` |
| Status | Controlled draft |
| Scope | Chapter 08 — TrueMoist Architecture, Evidence and Research Position; Part IV evidence-status, open-decision, contradiction and source registers |
| Source boundary | Only the ten attachments in the controlled Part IV drafting package |
| Input inventory | Exactly ten physical attachments were readable. The nine externally hash-controlled inputs matched the manifest byte counts and SHA-256 values. The self-referential manifest was used only for file control. Upload transport suffixes did not create additional logical sources. |
| Current implementation status | Not an implementation, Phase 4 or procurement authorization |
| Approval status | Not a teacher-approval record; final concept and course-platform acceptance remain unresolved |
| Experimental status | The validated 72-run architecture is a selected experimental design, not proof that 72 physical runs, model fitting or held-out validation were completed |
| Patent status | No patentability, filing, infringement or freedom-to-operate conclusion |
| External verification | No fresh web, market, manufacturer, patent-register, legal-status or specification verification was performed; those activities are reserved for a later controlled stage |
| Relationship to Part I | Part I controls the current project state: TrueMoist is retained but neither finally selected nor rejected; VibeGuard is the strongest semester-build recommendation; the proposed OpenBraille-to-VibeGuard shift is not proved teacher-approved; platform acceptance, Phase 4 and procurement remain unresolved; no frozen MVP is established as patentable; the final adjudications disagree on the preferred future patent route |
| Relationship to Parts II and III | Parts II and III were used only for manual style and cross-concept consistency. They are not TrueMoist technical evidence. |

The ten-file package was complete and readable. The reconciliation controls resolved wording; the source packet preserves underlying evidence. No prior-chat context, memory, web research or unstated assumption was used.

## How to read Part IV

Part IV preserves six boundaries.

**Architecture and refinement.** The frozen MVP is a one-soil local compensation design using a genuine analog probe, nearby DS18B20, known S0/S1 batch metadata, evidence-gated acquisition, offline fitting, fixed local coefficients, USB CSV and gravimetric GWC. Jig, wiring, factor values, ADC choice and model stability may be refined without adding live EC, actuation, cloud dependency or online learning.

**Design and evidence.** The 4 × 3 × 2 × 3 plan defines 72 independent physical runs; it does not prove that the runs, fitting or held-out test were completed.

**Metadata and sensing.** S0/S1 records the prepared treatment. It is not conductivity measurement or autonomous salinity estimation.

**Baseline and compensation.** Compensated models must beat the same probe’s uncompensated calibration against the same held-out physical reference.

**Semester and future research.** Replacement, remount, transfer, contamination, validity and fallback mechanisms are later hypotheses, not MVP features.

**Research and filing.** Patent research supports a cautious technical position. It does not establish novelty, patentability, FTO or filing approval.

# Chapter 08 — TrueMoist Architecture, Evidence and Research Position

## 08.1 Chapter purpose

This chapter defines the controlled TrueMoist architecture, experimental method, evidence boundaries and current research position. It is intended to serve as a practical engineering reference after authorization and as a durable record of what the concept does—and does not—claim.

TrueMoist addresses a narrow measurement problem. Low-cost analog capacitive soil-moisture probes can be influenced by temperature, salinity-related treatment, nonlinearity, insertion geometry, packing, unit variation and drift. The project asks whether a carefully controlled local compensation method can produce estimates that are more trustworthy than an uncompensated calibration under a bounded one-soil experiment. It does not seek to create a universal agricultural sensor, a field-ready irrigation system or a general soil-chemistry platform.

The chapter therefore combines four forms of control. It locks the semester architecture; specifies how independent physical evidence is to be produced; distinguishes proposed criteria from measured results; and separates the ordinary engineering project from a later, speculative transfer-and-validity research path. Nothing in this chapter authorizes procurement, Phase 4, public claim-focused disclosure or patent filing.

## 08.2 Current TrueMoist identity

> **TRUEMOIST ARCHITECTURE LOCK**
>
> For the frozen semester architecture, **TrueMoist means only**:
>
> - one genuine analog capacitive soil-moisture probe used for the final dataset;
> - a second nominally identical probe used as a spare and for unit-variation characterization, not as a permanent dual-probe runtime requirement;
> - one nearby waterproof DS18B20 measuring soil temperature at controlled depth and spacing;
> - a known S0/S1 salinity-treatment code assigned from prepared-batch metadata;
> - one homogeneous soil and one controlled preparation procedure;
> - ADS1115 as the primary acquisition design, subject to a paired evidence gate against calibrated ESP32 ADC1;
> - an ESP32-class controller;
> - offline fitting of supported low-order models;
> - fixed coefficients evaluated locally on the controller;
> - USB serial CSV output and optional simple local status indication;
> - dry-basis gravimetric water content as the physical reference; and
> - an authoritative design of 72 independent physical condition runs.
>
> TrueMoist is **not** a live-EC instrument, autonomous salinity estimator, irrigation controller, pump or valve system, cloud platform, farm-telemetry service, universal or multi-soil model, custom multi-frequency probe, TinyML showcase, online-adaptive learner, field-validated product, patent-ready mechanism or teacher-approved semester implementation.

The identity lock prevents older broad descriptions and lower-authority research proposals from changing the selected architecture. Historical references to a self-correcting platform, live conductivity sensing or autonomous action remain useful as origin records only. They do not control the semester MVP.

TrueMoist remains a legitimate retained Phase 3C concept. The controlled project record neither selects it as the final semester build nor rejects it. Its concept-level architecture is ready only with mandatory early validation, while project-wide authorization, platform acceptance and procurement remain open.

## 08.3 Bounded semester objective

The semester objective is to test whether local compensation improves the trustworthiness of one low-cost analog capacitive probe under controlled disturbances in one homogeneous soil. Two estimates must be produced from the same physical observations:

1. an **uncompensated estimate** based only on raw probe response; and
2. a **compensated estimate** that also uses measured soil temperature and the known salinity-treatment code.

Both estimates must be evaluated against the same dry-basis gravimetric reference. Training and model selection must use only the designated training replicates. The final comparison must use an untouched physical replicate and must report absolute error as well as relative improvement.

A successful semester outcome would establish a bounded technical result: on the team’s tested soil, preparation method, temperature range, treatment range, probe configuration and held-out replicate, the selected compensated method improved error relative to the uncompensated baseline without unacceptable degradation in a major subset. It would not establish universal accuracy, cross-soil transfer, long-term field reliability, production calibration, live chemistry measurement, autonomous irrigation or patentability.

A partial or negative result can still be valuable. Evidence that packing variance dominates the intended disturbance, that the probe cannot be reinserted repeatably, that the external ADC adds no value, or that compensation fails on held-out physical samples would be legitimate engineering findings when the test procedure and raw records are preserved.

## 08.4 System architecture overview

The controlling architecture is described as **D-dominant with B-style signal hardening**: model fitting occurs offline, inference remains local, and the low-cost analog path is strengthened through controlled acquisition, filtering, physical geometry and evidence gates.

```text
Prepared-batch metadata
(batch ID, replicate, target condition, S0/S1 code, recorded dose)
                              ┐
Analog capacitive probe ──────┼─> filtered analog node ─> selected ADC path ─┐
Nearby DS18B20 temperature ───┘                                              │
                                                                              v
                                                                        ESP32-class MCU
                                                                    acquisition and checks
                                                                    Model 0 raw estimate
                                                                    selected compensated estimate
                                                                    range and quality flags
                                                                              │
                                                                              v
                                                                       USB serial CSV

Wet/dry mass records ─> dry-basis gravimetric reference ─> offline Python fit,
                                                         grouped validation and
                                                         coefficient freeze
```

| Subsystem | Frozen role | Principal control | Evidence boundary |
|---|---|---|---|
| Prepared soil batch | Produces one controlled physical condition | Fixed soil, mass, water addition, treatment dose, mixing, equilibration and packing record | Metadata does not prove the intended physical state was achieved; measurements and deviations must be recorded |
| Analog moisture probe | Provides the raw electrical response used by all models | Genuine capacitive unit, electrical characterization, fixed insertion geometry and unit identity | A seller label or one stable reading does not establish authenticity, monotonicity or repeatability |
| DS18B20 temperature channel | Measures nearby soil temperature as a model input and factor record | Same depth, controlled separation, equilibration and error checks | Ambient temperature is not a substitute; measured temperature does not automatically prove effective compensation |
| Salinity-treatment metadata | Supplies known S0/S1 preparation state | Recorded NaCl dose in g/kg oven-dry-equivalent soil | Not live EC, conductivity or autonomous salinity estimation |
| Analog acquisition | Converts the probe node to digital observations | ADS1115 primary design with paired ESP32 ADC1 comparison; short filtered path; decoupling | Nominal bit depth is not evidence of better effective accuracy |
| ESP32-class controller | Acquires, evaluates fixed models, flags states and logs records | Versioned firmware, fixed coefficients, local processing, radios disabled during final acquisition | Controller output must be numerically checked against offline calculations |
| Offline analysis | Fits and selects M0/M1/M2 using grouped physical records | Leakage prevention, grouped validation and untouched replicate | A fitted training curve is not held-out performance |
| Gravimetric reference | Supplies dry-basis physical reference | Wet mass, constant dry mass and traceable calculation | No credible accuracy claim exists without oven/scale access and constant-mass control |
| USB evidence path | Exports raw observations, estimates, metadata and quality flags | Versioned CSV schema, batch and run identifiers | Logs must remain linked to physical preparation and reference records |

## 08.5 Authoritative 72-run experimental architecture

The selected experimental design contains four moisture conditions, three temperature conditions, two controlled salinity treatments and three independent physical replicates:

```text
4 moisture conditions
× 3 temperature conditions
× 2 salinity-treatment states
× 3 independent physical replicates
= 72 independent physical condition runs
```

| Factor | Authoritative design position |
|---|---|
| Moisture | Four dry-basis target regions spanning a safe and usable response range identified by pilot work. Exact percentages are not frozen before the selected soil’s behavior, field capacity and probe response are characterized. |
| Temperature | Recommended nominal conditions are 20 °C, 30 °C and 40 °C. A documented 20/28/36 °C fallback is permitted if 40 °C cannot be produced safely and uniformly. Actual soil temperature, not the nominal chamber or ambient value, controls the record. |
| Salinity treatment | S0 contains no deliberately added salt. S1 uses one pilot-selected NaCl dose that creates a repeatable, non-saturating effect. The frozen dose must be recorded in grams per kilogram of oven-dry-equivalent soil. |
| Replicate | Three independently prepared or independently reset physical samples for each factor combination. Replicates 1 and 2 support training and model selection; replicate 3 remains untouched for final physical testing. |

### Definition of an independent physical run

One run is one separately prepared or independently reset physical soil condition. Repeated ADC conversions, multiple serial lines or rapid rereads from an undisturbed container do not create additional runs. They are electronic observations within one physical record and must be aggregated before model splitting.

Independence therefore depends on physical preparation, not sample count in software. Each record must preserve the soil batch, factor levels, replicate identity, probe identity, geometry, mass records, preparation timings, ADC configuration, temperature observation, accepted raw statistics and deviations.

### Training and held-out roles

Replicates 1 and 2 are reserved for training and model selection. Grouped cross-validation must keep all electronic observations and repeated measurements from the same physical batch together. Replicate 3 is reserved as the untouched final test set. It must not influence factor tuning, feature selection, coefficient choice, threshold selection or model-complexity decisions.

The package requires physical independence and leakage prevention but does not freeze a complete random run order. Blocking, randomization, practical oven scheduling and deviation handling must be preregistered before main data collection. Convenience ordering must not be allowed to align a factor with time, probe drift or equipment state without documentation.

> **DESIGN DOES NOT EQUAL COMPLETION**
>
> The 72-run structure is a validated experimental architecture. The controlled attachments do **not** prove that:
>
> - 72 independent physical conditions were completed;
> - a complete physical run ledger or dataset exists;
> - the final model was fitted or selected;
> - coefficients were frozen;
> - Python-to-MCU numerical equivalence was demonstrated;
> - the untouched replicate was tested; or
> - any RMSE, MAE, accuracy or error-reduction threshold was measured.
>
> Until direct records exist, Chapter 08 uses terms such as *design*, *planned run*, *required test*, *proposed criterion* and *unavailable result*.

A documented 54-run contingency exists as a schedule fallback, but it is not equivalent to the authoritative 72-run design. Any reduction requires explicit change control, a revised split plan and transparent reporting of the loss in evidence.

## 08.6 Analog probe and acquisition architecture

The final dataset uses one genuine analog capacitive probe; a second nominally identical unit is a spare and unit-variation check, not a permanent dual-probe product. Before acceptance, the selected unit must show credible capacitive construction, usable analog range, stable warm-up behavior, monotonic pilot response and controlled reinsertion repeatability. YL-69/HL-69-style resistive probes are not the selected sensor.

The short analog path uses a 1 kΩ series resistor and 100 nF input capacitor. The ADS1115 path is decoupled with 100 nF ceramic and 10 µF bulk capacitance. Characterization may begin on breadboard, but the main dataset requires a documented soldered path.

For each physical record, the design requires equilibration; a valid DS18B20 reading; discard of the first ADC conversion after reconfiguration; 64 electronic observations; median-based or three-MAD rejection; an accepted mean and dispersion summary; evaluation of raw and compensated estimates; and logging of metadata and quality flags. The 64 observations remain one physical sample.

ADS1115 is primary but evidence-gated. Week 1 compares it with calibrated ESP32 ADC1 on the same analog node using noise, drift, reinsertion and pilot-error evidence. ADC1 is the fallback when the external module offers no practical value or is unsuitable.

## 08.7 Temperature-measurement role

The waterproof DS18B20 measures soil temperature near the active probe region. Its purpose is twofold: it records the actual experimental temperature condition and supplies a measured compensation input to Models 1 and 2.

The probe and temperature sensor must share a controlled geometry. The DS18B20 is placed at the same depth as the active moisture-sensing region, approximately 20–30 mm away, without touching the moisture-probe board. A fixed jig controls depth, separation and cable strain. Ambient temperature may be recorded as context, but it cannot replace the soil measurement.

The designed firmware uses 12-bit conversion, obtains three readings and retains the median, checks known error values, and records temperature at the start and end of the acquisition interval. The actual implementation must also preserve sensor identity and timing so that a stale, disconnected or invalid reading cannot silently enter the model.

Including temperature in an equation does not prove temperature compensation. A useful result requires adequate equilibration, limited spatial gradients, valid sensor behavior and improved held-out error attributable to the temperature term or its interactions. The controlled package contains the design and proposed procedure, not a completed temperature calibration or measured compensation result.

## 08.8 Controlled salinity-treatment code

TrueMoist does not measure live salinity or electrical conductivity. Its salinity variable is known experimental metadata assigned from the batch-preparation record.

- **S0** means that no salt was deliberately added.
- **S1** means that one pilot-selected NaCl treatment was deliberately added.
- The actual S1 dose is frozen after pilot testing and recorded in grams of NaCl per kilogram of oven-dry-equivalent soil.
- The treatment state, exact dose, batch identifier and preparation record are supplied to offline model fitting and to fixed local inference.

The S1 pilot must identify a treatment that produces a repeatable effect greater than electronic noise without saturating the probe or creating uncontrolled physical changes. The dose may be adjusted once during the pilot under the defined gate. If no valid treatment can be established, the project may use the documented temperature-only fallback, but the scope reduction and resulting evidence limitation must be explicit.

The treatment code does not represent bulk-soil EC, apparent EC, pore-water EC, solution conductivity or a universal chemistry state. It cannot be described as an autonomous sensor channel. Outside the controlled prepared-batch experiment, the operational source of the code is unresolved. It may remain laboratory metadata or, in a later deployment concept, require user-supplied information. Chapter 08 does not resolve that future deployment question by inventing a live capability.

## 08.9 One-soil preparation and geometry controls

The semester architecture is restricted to one homogeneous soil and one controlled preparation method. This restriction is a validity control, not an inconvenience to be hidden. Different soil texture, organic content, density, mineral composition and salinity behavior can alter probe response; the present design does not support cross-soil transfer or universal calibration.

The planned physical preparation uses approximately 300–500 g of soil in a 500–1000 mL nonconductive container. The exact container, dry-soil mass and geometry are frozen after pilot work. Water is added by mass, mixed through one documented procedure and allowed to equilibrate under a defined sealed or covered condition. Salinity treatment is prepared from known mass records. Compaction is performed by a repeatable method rather than by subjective hand packing.

A fixed jig controls probe insertion depth, angle, separation from the DS18B20, container position and insertion path. Probe-board markings and sample identifiers provide visual confirmation. The operator records any void, tilt, unusual resistance, visible damage, incomplete mixing or departure from the procedure instead of silently correcting the record after measurement.

Packing and reinsertion are major error sources. Early trials must quantify whether independently prepared and packed samples vary less than the intended temperature or S1 disturbance. If packing variance dominates, the project must improve the jig, container, sample mass or compaction method before collecting the main dataset. Increasing model complexity is not an acceptable substitute for uncontrolled preparation.

## 08.10 Gravimetric reference method

The controlling physical reference is **dry-basis gravimetric water content**:

```text
GWC = (wet soil mass - dry soil mass) / dry soil mass
```

The planned constant-mass procedure is:

1. label the container and sample with a unique batch and replicate identifier;
2. tare the clean, dry container;
3. record wet soil plus container mass;
4. dry the sample at 105 ± 5 °C for at least 24 hours;
5. cool it in a dry, covered environment;
6. weigh the container and dry soil;
7. return the sample to the oven for a further 1–2 hours;
8. cool and reweigh;
9. accept constant mass only when the difference is within the chosen scale-based tolerance; and
10. calculate dry-basis GWC from the traceable wet and dry masses.

A 0.01 g scale is preferred. A 0.1 g scale may be usable only with sufficiently large samples and an explicit uncertainty calculation. Scale resolution, tare stability, container handling, cooling conditions and oven throughput are part of the evidence chain.

The project must not report volumetric water content unless bulk density or a controlled known-volume core is independently measured. Dry-basis GWC is the authoritative reference for the frozen design. Conversion by assumption would create an unsupported result.

Access to an appropriate oven, scale and constant-mass workflow is an entry gate. Purchase of a laboratory oven is outside the project budget. Without credible institutional or laboratory access, TrueMoist may remain a qualitative or conditional experiment, but final accuracy and error-reduction claims are prohibited.

## 08.11 Calibration and validation design

Training occurs offline in Python. The supported model ladder is deliberately simple so that the project tests compensation rather than hides physical weaknesses behind excessive model flexibility:

- **Model 0:** uncompensated univariate raw-probe calibration;
- **Model 1:** multivariate linear compensation using raw response, measured temperature and S0/S1 code;
- **Model 2:** ridge-regularized second-order candidate using selected quadratic and interaction terms.

Replicates 1 and 2 supply the model-development data. All repeated readings from one physical batch remain grouped. Model selection uses grouped cross-validation by physical batch and must preserve preparation independence. Replicate 3 remains untouched until the complete model form, features, coefficients, numerical scaling and pass criteria are frozen.

Model 2 may be selected only when it improves grouped held-out performance over Model 1, avoids unstable coefficients, preserves sensible monotonic behavior over the tested moisture range, does not materially worsen a major temperature or salinity subset and can be reproduced numerically on the MCU. Otherwise Model 1 is deployed.

After selection, the coefficients are fixed. The firmware evaluates the same frozen equation locally. Online coefficient changes, recursive self-learning, automatic runtime retraining and event-triggered adaptation are outside the semester architecture.

A valid analysis must preserve the distinction between model-development evidence and final evidence. Training fit, cross-validation performance and the untouched replicate should be reported separately. Any excluded run, corrected metadata item or deviation must be traceable to the physical ledger.

## 08.12 Uncompensated baseline

Model 0 is the controlling uncompensated comparison:

```text
GWC_hat_raw = a0 + a1 × raw
```

It maps the accepted raw probe statistic to estimated dry-basis GWC without temperature or treatment information. Its purpose is not merely to provide a weak straw model. It represents the ordinary calibration that the compensated architecture claims to improve.

The baseline and compensated methods must use the same physical records, reference values and held-out replicate. Relative improvement cannot be computed by comparing different samples, different preparation rules or differently filtered data. Absolute baseline RMSE and MAE must be reported so that a percentage improvement is not used to disguise large remaining errors.

The attached evidence defines the model form and comparison logic but contains no fitted `a0` or `a1`, no calibration curve and no measured baseline performance.

## 08.13 Compensated linear model

Model 1 is the first compensated method:

```text
GWC_hat_linear =
b0 + b1 × raw + b2 × temperature + b3 × salinity_code
```

The salinity term receives the known S0/S1 batch code. The temperature term receives the measured nearby soil temperature. Model 1 provides the main interpretable compensated baseline and is the required fallback when the second-order model does not show stable, meaningful benefit.

The model remains bounded to the tested soil, geometry, probe unit or documented unit configuration, temperature range, treatment range and preparation procedure. A coefficient attached to S1 is not a live conductivity calibration, and a coefficient attached to temperature does not imply general compensation outside the observed range.

No fitted `b` coefficients, feature scaling, measured residuals or held-out result are present in the controlled package.

## 08.14 Ridge second-order candidate

Model 2 is the most complex supported candidate:

```text
GWC_hat_comp =
c0
+ c1 × raw
+ c2 × T
+ c3 × S
+ c4 × raw²
+ c5 × T²
+ c6 × raw × T
+ c7 × raw × S
+ c8 × T × S
```

Ridge regularization is used to reduce coefficient instability. Terms may be removed when they are unstable, unsupported by the data or unnecessary for held-out performance. The architecture does not authorize adding an undisclosed equation, neural network, random forest, generic TinyML model or online learner merely to obtain a better training score.

The controlling selection rule requires Model 2 to improve held-out RMSE over Model 1 by at least 5%, preserve monotonic behavior over the tested moisture range, avoid unstable coefficients, avoid material worsening in either major salinity subset and reproduce offline output on the MCU. If those conditions are not met, Model 1 controls.

The equation defines a candidate family only. The attachments do not provide fitted `c` coefficients, the selected term set, regularization strength, scaling rules, statistical significance, residual plots or measured error reduction.

## 08.15 Error metrics and comparison criteria

The project uses error against dry-basis gravimetric GWC as its primary evidence. Improvement ratios are secondary to complete absolute reporting.

| Evidence item | Controlled criterion | Current evidence status |
|---|---|---|
| Primary metric | Held-out RMSE against gravimetric GWC | Defined as the principal metric; no measured value attached |
| Primary improvement criterion | Compensated held-out RMSE at least 20% lower than uncompensated RMSE | Proposed engineering pass criterion, not an achieved result |
| Secondary metric | Held-out MAE | Defined; no measured value attached |
| Secondary improvement criterion | Compensated held-out MAE at least 15% lower than uncompensated MAE | Proposed engineering pass criterion, not an achieved result |
| Subset guardrail | No more than 10% MAE worsening in a major tested temperature or salinity subset | Proposed guardrail; no subset result attached |
| Model 2 selection criterion | At least 5% RMSE improvement over Model 1 plus stability, monotonicity, subset and MCU-equivalence conditions | Proposed selection rule; no model-selection result attached |
| Absolute reporting | RMSE and MAE in the reference units must accompany percentage improvement | Required final reporting practice |
| R² | Supplementary only | Must not replace RMSE and MAE |
| Confidence procedure | Paired bootstrap interval or paired permutation test where feasible | Proposed analysis support; not completed |
| Calibration result | Separate from final test | Unavailable |
| Untouched replicate result | Final physical evidence | Unavailable |
| Simulated performance | No controlled simulation source exists | Unavailable and must not be invented |

Passing the proposed thresholds would support only the bounded conclusion that the compensated method improved error within the tested experimental configuration. It would not establish universal accuracy, field performance, patentability or FTO. Failing the thresholds would not invalidate the integrity of the project if the experiment was properly controlled and the negative result was reported.

## 08.16 Hardware architecture

The hardware is intentionally modest and measurement-focused.

| Element | Controlled role | Validation need |
|---|---|---|
| ESP32-WROOM-32 | Primary acquisition, fixed inference and USB logging controller | Purchased-board identity, pin map, ADC behavior and course acceptance |
| ESP32-S3 / STM32F401-class | Same-family fallback / conditional authorized platform alternative | Formal substitution and complete implementation revalidation |
| ADS1115 | Primary external ADC design | Same-node comparison with calibrated ESP32 ADC1 |
| Two genuine capacitive probes | One final-model unit; one spare/unit-variation unit | Authenticity, monotonicity, stability, reinsertion and unit variation |
| Waterproof DS18B20 | Nearby soil-temperature input | Placement, gradients, equilibration and error handling |
| Filtered analog path | Short, decoupled and eventually soldered measurement path | Documented values and noise/drift evidence |
| Containers and jig | Fix preparation and sensor geometry | Repeatability, cleaning, dimensions and revision control |
| USB 5 V power | Passive bench supply | Stable supply; no actuator load |
| Scale and oven access | Gravimetric reference infrastructure | Resolution, constant mass, availability and throughput |

No pump, relay, valve, motor, cloud connection or mandatory display belongs to the frozen hardware. Optional LEDs may indicate quality states but do not replace the USB and physical evidence records. Compute and memory are minor constraints; physical preparation, reference quality and throughput dominate.

## 08.17 Firmware and local-output architecture

Firmware is separated into configuration, probe acquisition, temperature acquisition, filtering, model evaluation, quality flags, logging and self-test. The versioned configuration must identify the board, probe, ADC path, acquisition rule, geometry revision, model and coefficient revision, valid ranges, batch and replicate.

During final acquisition, Wi-Fi and Bluetooth are disabled. The controller reads temperature and analog observations, forms the accepted raw statistic, evaluates Model 0 and the selected compensated model, applies approved quality rules and emits a versioned USB CSV record. Records should preserve the physical identifier, actual temperature, treatment metadata, raw statistic, dispersion, both estimates, model revision and quality flags. Optional LEDs or a host plot are presentation aids only.

Python-to-MCU numerical equivalence is a release gate. Fixed test vectors must reproduce the offline equation within the approved numerical tolerance before replicate 3 is processed. No completed equivalence report is attached.

## 08.18 BOM and budget evidence

The attached values are historical Phase 3C planning evidence, not current quotations.

| Item | Quantity | Historical planning range |
|---|---:|---:|
| ESP32 development board | 1 | ₹450–₹700 |
| ADS1115 module | 1 | ₹120–₹220 |
| Genuine analog capacitive probes | 2 | ₹300–₹600 |
| Waterproof DS18B20 | 1 | ₹120–₹220 |
| Perfboard, connectors, cables and passives | 1 set | ₹250–₹450 |
| Containers and jig materials | 1 set | ₹200–₹450 |
| Soil and salinity consumables | 1 set | ₹100–₹300 |
| Optional 0.01 g scale | 1 | ₹400–₹700 |
| Contingency | — | ₹250–₹500 |

Historical aggregate planning is approximately **₹1,790–₹3,440** when institutional scale and oven access are available. The preferred target is **≤₹3,000** and the absolute hardware ceiling is **₹5,000**. Buying a laboratory oven is outside the budget.

The embedded BOM may fit the student limit, but the reference method depends on institutional facilities. A later controlled stage must verify manufacturer specifications, authenticity, availability and current Indian prices before procurement or final publication.

## 08.19 Minimum demonstrable success

The frozen MVP reaches minimum demonstrable success only when the complete physical-to-digital chain is shown. It must:

1. acquire stable and interpretable raw analog probe output;
2. measure nearby soil temperature through a controlled geometry;
3. represent the known S0/S1 treatment rigorously from batch metadata;
4. produce the uncompensated Model 0 estimate;
5. produce the selected compensated estimate locally with fixed coefficients;
6. compare both estimates with the same traceable gravimetric GWC reference;
7. preserve independent physical replicates and prevent batch leakage;
8. demonstrate preregistered improvement on the untouched physical replicate while respecting subset guardrails;
9. reproduce the offline model numerically on the MCU;
10. preserve one-soil, tested-range and prepared-treatment limits; and
11. emit enough local evidence through USB CSV to reconstruct the result.

A live graph, a moisture percentage on a screen or a serial value that changes when water is added is not sufficient. Those demonstrations show responsiveness, not validated compensation. The project’s strongest evidence is the relationship among controlled preparation, gravimetric reference, grouped analysis and held-out local inference.

When the pass criteria are not met, the result must be described according to the failure mode. For example, the team may demonstrate a functional measurement chain but no compensation benefit; a valid one-soil dataset but inadequate held-out improvement; or a preparation system whose physical variance prevents model evaluation. These are different outcomes and should not be collapsed into a simple success/failure label.

## 08.20 Early validation gates

The architecture is classified as **Ready with Mandatory Early Validation**. Main data collection must not begin merely because the circuit operates.

### Week 1 gates

| Gate | Required evidence | Pass interpretation | Fallback or consequence |
|---|---|---|---|
| Probe authenticity and basic stability | Manufacturer/supplier identity where available, electrical inspection, warm-up record and fixed-sample observations | Probe behaves as a usable analog capacitive sensor | Inspect the second unit or replace the sensor |
| Monotonic pilot response | Ordered response across pilot moisture states | A calibration hypothesis is physically plausible | Reject or replace a non-monotonic or saturated unit |
| Reinsertion repeatability | Controlled repeated insertion using the jig | Reinsertion variation remains within the usable response span | Improve jig and procedure before factor testing |
| ADC paired comparison | Same analog node measured by ADS1115 and calibrated ESP32 ADC1 | Acquisition path selected by observed noise, drift and pilot error | Use calibrated ADC1 when ADS1115 adds no practical value |
| Gravimetric access | Confirm oven, scale, containers, constant-mass procedure and responsible access | Ground-truth path is feasible | Prohibit final accuracy claims until credible access exists |

### Week 2 gates

| Gate | Required evidence | Pass interpretation | Fallback or consequence |
|---|---|---|---|
| Packing sensitivity | Independently prepared samples show controlled variation | Preparation noise does not overwhelm the intended effects | Improve compaction, container, sample mass or jig; reduce scope if necessary |
| Temperature feasibility | Soil reaches safe, measurable and sufficiently uniform conditions | Three temperature states can be executed | Use the documented 20/28/36 °C fallback when justified |
| S1 feasibility | Pilot-selected dose creates a repeatable, non-saturating shift greater than electronic noise | S0/S1 factor is usable | Adjust once; otherwise use a transparent temperature-only fallback |
| Pilot grouped analysis | Preliminary comparison without physical-batch leakage | Measurement and reference chain is coherent enough to proceed | Repair preparation/reference problems before adding model complexity |
| Analog front end and jig freeze | Soldered path, controlled geometry and versioned procedure | Main dataset can begin under one stable configuration | Do not collect main data while hardware or geometry remains fluid |

Passing an early gate does not establish final accuracy. It only supports entry into the next evidence stage. Gate evidence must be archived even when it causes a sensor replacement or scope reduction.

## 08.21 Main experimental and held-out sequence

After authorization and early-gate passage, the intended sequence is:

1. freeze the probe, ADC path, controller, firmware, analog values, jig, containers, soil procedure and gravimetric method;
2. freeze the four moisture regions, three achievable temperatures and S1 dose from pilot evidence;
3. preregister run order or blocking, replicate preparation, identifiers, exclusions and the untouched-replicate boundary;
4. collect independent replicates 1 and 2 with matching preparation, acquisition and mass records;
5. audit identifiers, deviations, equilibration, reference quality and leakage risk;
6. fit Model 0 and Model 1 under grouped validation;
7. evaluate Model 2 under the complexity, stability, monotonicity and subset rules;
8. freeze the selected features, coefficients, valid range and firmware before accessing replicate 3;
9. prove Python-to-MCU numerical equivalence with fixed vectors;
10. process untouched replicate 3 without retuning;
11. report absolute RMSE/MAE, relative improvement, subset results, guardrails, exclusions, repeatability and drift; and
12. archive raw logs, mass sheets, run ledger, code, coefficients and configuration revisions.

Practical oven scheduling may require blocking, but factor levels must not become inseparable from time, drift or equipment state. No step in this sequence is proved complete by the controlled attachments.

## 08.22 Experimental, measurement and generalization risks

| Risk | Present state | Required control or interpretation |
|---|---|---|
| Probe authenticity and unit variation | Open | Characterize purchased units; do not infer population transfer |
| Warm-up, drift and reinsertion | Open | Freeze timing and geometry; report repeatability and drift |
| Packing and preparation | Open | Quantify independent preparation variance before main data collection |
| ADC path | Open | Select by paired ADS1115/ESP32 ADC1 evidence, not nominal resolution |
| Temperature gradients | Open | Use same-depth placement, controlled spacing and equilibration checks |
| S1 treatment | Open | Pilot and freeze a repeatable non-saturating dose in g/kg dry soil |
| Gravimetric access | Open | Confirm scale, oven and constant-mass workflow before accuracy claims |
| Drying throughput | Open | Trial the workflow; use formal change control for any run reduction |
| Data leakage | Controlled by design, not audited | Group by physical batch and preserve untouched replicate 3 |
| Model overfit | Open | Use grouped validation, ridge control, monotonicity and linear fallback |
| Python/MCU mismatch | Open | Complete fixed-vector equivalence before final testing |
| Treatment-code deployment | Unresolved | Keep S0/S1 as laboratory metadata; no autonomous field claim |
| One-soil limitation | Fixed | Report only within the tested soil, range and preparation |
| Current parts and prices | Unverified | Conduct later manufacturer and market verification |

The dominant uncertainties are metrology, preparation and throughput, not compute. A weak physical reference cannot be repaired by a more complex model.

## 08.23 Allowed refinements

The following changes remain within the frozen TrueMoist identity when formally documented:

- selecting an electrically characterized genuine analog capacitive probe equivalent to the reference class;
- using the second unit as a spare or for unit-variation characterization;
- retaining ADS1115 or selecting calibrated ESP32 ADC1 according to the paired gate;
- using ESP32-S3 as the same-family controller fallback;
- using an STM32F401-class board only after an explicit authorized platform and toolchain decision;
- adjusting the exact four moisture targets after pilot characterization while retaining four controlled levels;
- using the documented 20/28/36 °C temperature fallback when the higher condition is unsafe or nonuniform;
- freezing the exact S1 NaCl dose after the controlled pilot;
- improving wiring, decoupling, shielding, perfboard layout, connectors, jig, container geometry or sample-control procedure;
- removing unstable Model 2 terms;
- selecting Model 1 when Model 2 does not satisfy the complexity gate;
- adding sensor-failure, missing-metadata and range flags;
- adding optional local LEDs or a host-side plot; and
- using the 54-run contingency only through explicit change control and transparent evidence reduction.

A refinement must preserve the local one-soil compensation question and the same physical reference. Changes that add a new sensing principle, automatic chemistry estimation, actuation, cloud dependency or runtime learning create a different architecture and require a new decision record.

## 08.24 Prohibited substitutions and overclaims

The following substitutions and statements are outside the controlled design:

- using YL-69/HL-69 as though it were the selected corrosion-resistant capacitive probe;
- describing S0/S1 metadata as live EC or conductivity measurement;
- claiming autonomous salinity estimation or compensation for unknown field chemistry;
- adding irrigation advice, pumps, relays or valve control;
- converting the project into cloud analytics, remote-farm telemetry or a mobile-app platform;
- requiring TinyML, a neural network or an undisclosed advanced model;
- adding online, recursive or event-triggered coefficient adaptation to the MVP;
- replacing the commodity probe with custom impedance or multi-frequency hardware;
- claiming universal, calibration-free, multi-soil or field-wide performance;
- reporting laboratory-grade accuracy or production agronomic readiness;
- reporting volumetric water content without independent bulk-density evidence;
- treating rapid electronic observations as independent physical samples;
- claiming that the 72-run design was executed without a physical run ledger;
- reporting RMSE, MAE, accuracy or error reduction without results;
- treating ADS1115 as superior solely because of nominal resolution;
- treating two probes as proof of transferable calibration or lifecycle health;
- presenting generic Mahalanobis, OOD, confidence or abstention logic as verified novelty;
- describing the ordinary MVP as patent-ready, likely patentable or cleared for FTO;
- claiming teacher approval, final semester selection, Phase 4 entry or procurement authorization without an explicit controlling record; or
- describing a TrueMoist pre-build simulation that does not exist.

## 08.25 Current implementation and approval status

TrueMoist is a retained Phase 3C architecture. Its final architecture, memory and SOP provide a coherent design and implementation sequence, but concept-level readiness does not equal project authorization.

The current controlled state is:

- TrueMoist is neither finally selected nor finally rejected;
- VibeGuard is the strongest semester-build recommendation in both final adjudications;
- the proposed OpenBraille-to-VibeGuard change is not proved teacher-approved;
- the exact course platform remains unresolved despite ESP32 being frozen in the concept architecture and STM32 appearing in the broader teacher context;
- project-wide Phase 4 entry and procurement are not proved authorized;
- no completed TrueMoist build, 72-run dataset or held-out result is attached; and
- no frozen MVP is established as patentable.

The final TrueMoist memory’s concept-level instruction to proceed toward implementation is interpreted as architecture readiness within the concept. It does not override the current Decision Register or validated Part I on teacher approval, final selection, platform acceptance or procurement.

## 08.26 Ordinary MVP patent position

The ordinary frozen MVP has strong engineering, experimental and publication value. It is not, on the controlled evidence, a credible independent patent nucleus.

The following elements are treated by the valid syntheses as conventional or insufficient by themselves:

- commodity capacitive soil-moisture sensing;
- nearby temperature measurement;
- known salinity-treatment metadata;
- RC filtering, decoupling and an external ADC;
- low-order linear, polynomial or ridge regression;
- offline training and fixed embedded coefficients;
- gravimetric reference measurement;
- grouped one-soil validation;
- USB CSV logging;
- the 72-run factorial arrangement;
- low cost; and
- omission of live EC.

A specific list of commodity parts and experimental parameters may be textually distinctive without producing an inventive technical interaction. Failure to find one document that copies every detail is not proof of useful novelty.

> **NO CURRENT FILING COMMITMENT**
>
> The controlled TrueMoist record does not establish:
>
> - confirmed novelty;
> - inventive step;
> - patent eligibility;
> - a useful independent claim;
> - filing approval;
> - infringement clearance;
> - freedom to operate; or
> - probable patent grant.
>
> The ordinary semester MVP should proceed, if authorized, as an engineering and measurement project. Any later filing decision requires direct physical evidence, a frozen future mechanism, current primary-source prior-art verification, official legal-status review, institutional IPR control and professional claim analysis.

The allowed conclusion is that the ordinary MVP has low current patent value and no patent-first readiness. This is a conservative technical and evidentiary assessment, not a binding legal declaration that every possible claim is unpatentable.

## 08.27 Controlled patent-research evidence

The controlled patent record contains six research lanes and two valid syntheses. Lanes are evidence sources, not votes, and were audited for concept fidelity, source quality, claim support, legal-status limits and unsupported certainty.

| Lane | Reconciled reliability | Retained value and limitation |
|---|---|---|
| ChatGPT Deep Research | High with legal-status caveats | Strong concept fidelity and conservative Track-C direction; official national status work remains incomplete |
| Gemini | Medium-low | Recognizes the conventional MVP and transfer/validity problem; autonomous-actuation drift and novelty/FTO overclaims are excluded |
| Perplexity — partial | Medium | Useful literature and patent leads; mandatory family, status and claim work is incomplete |
| Qwen compilation | Low-medium | Useful future-topic inventory; treated as one lane and stripped of clear-FTO/novelty claims |
| Mistral | Low | Supports the conventional-MVP conclusion; legal concepts and future novelty are overstated |
| Microsoft Copilot | Low-medium | Useful terminology; unsupported semester-feasibility, novelty and clearance claims are excluded |

The stronger common position is that temperature, treatment, packing and unit variation are real physical problems; the frozen stack is scientifically useful but patent-weak; and transfer or validity is a more relevant future question than ordinary regression. Generic Mahalanobis/OOD gating, abstention alone, omission of live EC, two probes, event recalibration and any `HIGH` or `CLEAR` FTO statement are not retained as verified patent conclusions. The Patent Evidence Index controls the six-lane set; a supplementary audit outside that set is not an extra vote.

## 08.28 Valid synthesis conclusions

The two valid syntheses materially agree on the ordinary MVP while using slightly different language for the strongest future direction.

### Max synthesis

`03_CONCEPT_PORTFOLIO/TrueMoist/03_Patent_Synthesis/01_TrueMoist_Patent_Evidence_Synthesis_Max.md` assigns **Track C** and describes a credible long-term path requiring later-semester extension. It gives medium confidence to the track classification and low-to-medium confidence that a useful claim would survive complete search and experiment. It treats the frozen MVP as a coherent engineering experiment without a credible independent technical nucleus. Its strongest future hypothesis is contamination-protected replacement-probe transfer coupled to perturbation-conditioned validity and abstention or fallback. It recommends retaining TrueMoist as a strong semester prototype while reducing patent priority.

### High + Deep Research synthesis

`03_CONCEPT_PORTFOLIO/TrueMoist/03_Patent_Synthesis/02_TrueMoist_Patent_Evidence_Synthesis_High_Deep_Research.md` also assigns **Track C**, with medium confidence. It describes the frozen architecture as high in engineering and scientific value, low in current patent value and not patent-first ready. Its strongest future hypothesis is a physical-reference-bound calibration-transfer and validity-acceptance method for replacement or remounted commodity probes. It likewise recommends retaining the semester prototype while reducing patent priority.

The syntheses are not votes and their agreement does not prove the future hypothesis. Their role is to establish a controlled research position: execute the ordinary MVP without patent-driven scope expansion; treat any two-probe transfer exercise as feasibility work; and advance filing-related work only after stronger multi-unit evidence and refreshed legal review.

## 08.29 Comparative adjudication context

The comparative record gives TrueMoist a distinctive strength: among the retained concepts, it has the most explicit quantitative validation architecture and substantial measurement or publication value. Its burden is also distinctive. Oven and scale access, drying throughput, probe repeatability, packing control, treatment preparation and early acquisition gates can determine feasibility before firmware sophistication matters.

Both final adjudications identify VibeGuard as the strongest semester-build recommendation. That common recommendation does not reject TrueMoist. It reflects a comparison of semester execution risk, demonstration clarity, team alignment and experimental burden.

The adjudications diverge on the later patent-development route:

- **Work Max** identifies TrueMoist as the best presently evidenced post-MVP patent-development candidate and fallback after its proposed VibeGuard signal-and-access gate.
- **Deep Research High** deprioritizes TrueMoist for the current patent-first choice, preserving it as a rigorous engineering and publication project while conditionally preferring an OpenBraille D11 route after a separate gate.

No higher authority resolves this disagreement. The manual therefore preserves both conditional positions rather than averaging them. TrueMoist cannot be described as the preferred patent route, the rejected patent route, the final semester choice or a teacher-approved build.

## 08.30 Future replacement, remount, transfer and validity hypothesis

The strongest supported future direction is separate from the frozen semester MVP. Its candidate sequence is:

1. bind donor calibration, probe identity and measurement provenance to a controlled configuration;
2. obtain sparse trusted physical reference responses when a commodity probe is replaced or remounted;
3. derive a bounded transfer mapping from the donor configuration to the replacement or remounted configuration;
4. challenge the mapping under controlled moisture, temperature, S0/S1, packing, remount and contamination perturbations;
5. analyze residual behavior to distinguish unit bias from real moisture change, treatment or temperature disturbance, packing/remount error, contamination, electronic offset or degradation;
6. accept transferred coefficients only when the physical challenge establishes a valid transfer state;
7. prevent contaminated or untrusted reference events from updating calibration; and
8. abstain or use a safe fallback when validity cannot be established.

This sequence is a **candidate research hypothesis**, not an implemented invention. Its broad components are crowded. The potentially differentiating question is whether the physical-reference-bound interaction creates a non-additive and materially superior result compared with simple alternatives.

The required simple baselines include donor-coefficient reuse, one-point transfer, two-point affine transfer, pooled calibration, full per-probe calibration, simple range checks, generic distance or confidence gates, unrestricted update, no update and the critical component ablations. If the complete mechanism does not outperform two-point affine transfer plus a simple range gate on independent physical data, the strongest hypothesis fails.

The second probe in the semester BOM can support only an exploratory feasibility study. It cannot establish transfer across a population, manufacturing lots, ageing states or field conditions. A successful 72-run Level-1 compensation result is a prerequisite for sensible Level-2 work, not evidence that Level 2 already exists.

## 08.31 No-pre-build-simulation boundary

No TrueMoist pre-build simulation exists in the controlled source set. The concept directory record states that the validated design resides under `01_Final_Architecture` and that the pre-build simulation directory is empty.

Accordingly:

- no simulation result may be reconstructed from a synthesis, research lane or future experiment plan;
- no later mechanism may be described as having passed a pre-build simulation;
- no hypothetical transfer, validity or recalibration result may be inserted into the evidence register; and
- the empty directory is an intentional no-file state in the evidence presented, not proof that an expected result was accidentally omitted.

TrueMoist differs from the concepts that possess controlled pre-build simulation documents. Its future research path is supported only as a conditional hypothesis derived from audited patent evidence and comparative reasoning.

## 08.32 Experimental evidence required for the future hypothesis

A credible later transfer-and-validity programme would require evidence beyond the two-month Level-1 design and beyond the present two-probe BOM. At minimum, it would need:

- several commodity probes, preferably **6–12 units** across at least two manufacturing lots where feasible;
- a defined donor-calibration procedure and blinded replacement or remount assignments;
- sparse trusted physical anchors with traceable gravimetric reference;
- repeated remounting under controlled depth, angle, packing and container changes;
- temperature and S0/S1 perturbations separated from probe-unit effects;
- contamination challenges and rules that prevent contaminated reference events from updating the mapping;
- ageing or drift proxies with dated, repeated observations;
- independent test groups not used to define the transfer or validity rule;
- comparison with naive reuse, one-point transfer, two-point affine transfer, pooled calibration and full per-probe calibration;
- comparison with always-report, simple range-gate, generic distance-gate, no-update and unrestricted-update policies;
- claim-specific ablations that remove transfer mapping, physical challenges, contamination control, validity acceptance and fallback one at a time;
- reporting of transfer RMSE, MAE, bias, severe accepted-error rate and calibration workload; and
- evidence that any improvement is not produced by one conventional component alone.

A two-probe one-soil pilot may estimate effect size, workload and procedural difficulty. It must be labelled exploratory. It cannot support general transfer, lifecycle health, multi-lot robustness, field reliability or a patent-ready claim.

The future direction should be killed or substantially revised when its advantage disappears against simple affine transfer and range gating, when one component explains all apparent benefit, when results depend on repeated electronic samples rather than independent physical challenges, or when the physical-reference burden makes the mechanism impractical.

## 08.33 Prior-art and legal-status limitations

The controlled patent research is useful for technical direction but incomplete as a legal foundation.

- Public database status labels are not official legal opinions.
- Indian, Chinese, European national-state and PCT national-stage details remain incomplete.
- No professional claim construction was performed.
- No search of unpublished applications is possible from the attached record.
- Litigation, licensing, prosecution history and commercial practice were not comprehensively reviewed.
- Target countries, products and commercial acts are not fixed.
- Expired or abandoned records may remain prior art even when they do not create present exclusion rights.
- Failure to locate an exact duplicate does not establish novelty or clearance.
- Academic prototyping is not a universal infringement exemption.

Before claim-dependent design freeze or filing, the exact mechanism would require refreshed primary-source searches, family consolidation, jurisdiction-specific claim charts, official register verification, professional translation where necessary and institutional or qualified-counsel review.

## 08.34 Freedom-to-operate boundary

Freedom to operate is different from patentability. A project may contain a patentable improvement and still fall within another party’s active claim; it may also be unpatentable while remaining free to practice because the relevant rights expired or do not cover the intended acts. The controlled research does not resolve either question.

FTO depends on the exact product or method, claim wording, territory, legal status and commercial acts. The current record does not fix a commercialization configuration, target jurisdiction or claim construction. Statements such as `LOW`, `CLEAR`, `relatively clear` or “no direct infringement identified” are therefore excluded as clearance conclusions.

No filing, commercialization or public deployment decision should rely on the present research as FTO advice. Jurisdiction-specific professional analysis is required after the actual mechanism and intended use are frozen.

## 08.35 Confidentiality, contribution and institutional IPR control

The ordinary semester design may be discussed at a general educational level: low-cost capacitive probes, temperature and treatment effects, low-order regression, gravimetric calibration and the planned 72-run one-soil experiment.

Pending institutional IPR review, claim-focused future details should remain controlled, including:

- exact physical-reference challenge sequences;
- probe fingerprints and transfer mappings;
- validity-envelope definitions;
- contamination gates;
- remount acceptance logic;
- lifecycle or degradation features;
- coefficient and provenance binding;
- detailed parameter values;
- labelled transfer, remount, contamination and ageing datasets;
- code, negative results and ablations; and
- invention chronology and contribution records.

The team should maintain dated laboratory notebooks, version-control history, test authorship, code contributions, design decisions and human interpretation records. AI and literature outputs are background evidence; they do not establish human inventorship. Institutional rules on ownership, inventorship, assignment, disclosure, publication timing and student contribution remain unresolved and require written guidance.

## 08.36 File/no-file decision gate

The current patent decision is **no filing commitment**. A later TrueMoist mechanism may enter institutional or professional file/no-file review only when the following conditions are met:

1. the Level-1 measurement chain and gravimetric method are physically credible;
2. the exact Level-2 mechanism is frozen rather than described as a collection of generic ideas;
3. multi-unit and, where feasible, multi-lot experiments are complete;
4. simple transfer and validity baselines are directly outperformed on independent physical data;
5. critical ablations show that the proposed interaction—not one conventional component—creates the effect;
6. negative results, accepted-error rates, calibration workload and failure states are preserved;
7. refreshed primary-source prior-art and claim searching retains a meaningful difference;
8. official legal-status and jurisdiction-specific FTO work is complete enough for the intended decision;
9. institutional confidentiality, ownership and inventorship requirements are satisfied; and
10. the authorized IPR body or qualified professional recommends proceeding.

Failure at an early physical or baseline gate should stop claim-focused escalation. The team may still publish or present the engineering result subject to institutional rules, but it must not use a patent filing to compensate for weak experimental evidence.

## 08.37 Current patent-development state

TrueMoist currently occupies a controlled **Track-C** position. The semester architecture is coherent, affordable at the historical planning level and capable of producing rigorous measurement evidence if the physical gates are passed. Its ordinary components and their straightforward combination are not established as a patent-first invention.

The replacement/remount transfer and physical-validity sequence is the strongest retained future hypothesis. It remains unimplemented, unsimulated, unverified against complete prior art and unsupported by the multi-unit evidence needed for a credible file/no-file decision.

The comparative portfolio does not resolve whether TrueMoist should become the later patent-development priority. Work Max conditionally favors it; Deep Research High conditionally favors another route. The governing project state preserves that disagreement.

The controlled current statement is therefore:

> TrueMoist should be retained as a rigorous semester engineering and publication path. Its ordinary MVP has low current patent value and no filing commitment. A later physical-reference-bound transfer-and-validity mechanism may be investigated confidentially after Level-1 success, but it must survive multi-unit experiments, simple baselines, ablations, refreshed prior-art review and institutional IPR control before any filing decision.

## 08.38 Chapter conclusion

TrueMoist is a disciplined local compensation experiment, not a general agricultural platform. Its frozen semester architecture combines one genuine analog capacitive probe, nearby soil-temperature measurement, known S0/S1 prepared-batch metadata, an evidence-gated ADC path, an ESP32-class controller, offline fitting, fixed local inference, USB CSV evidence and dry-basis gravimetric reference.

Its strongest design feature is not algorithmic complexity. It is the planned separation of physical factors, independent preparation, leakage-controlled model development and untouched held-out validation. The authoritative 72-run structure provides a credible framework, but the controlled attachments do not prove execution, fitted coefficients or measured improvement.

TrueMoist remains retained but not finally selected or rejected. VibeGuard remains the strongest semester-build recommendation, and project-wide approval, platform choice, Phase 4 and procurement remain open. The ordinary TrueMoist MVP has high engineering and scientific value but low current patent value. Replacement/remount transfer and physical validity remain post-semester hypotheses without a pre-build simulation or filing commitment.

A technically honest TrueMoist result will depend on the quality of the physical reference, probe and preparation controls, not on promotional claims. The project should proceed only through the defined gates, preserve negative evidence and keep future claim-focused work under institutional control.

## 08.S Source notes

Material conclusions in Chapter 08 are tied to original organized-workspace sources, not to the packet or reconciliation filenames. TIER_1 controls architecture and project state; TIER_2 controls audited patent and comparative evidence; TIER_3 lanes provide supporting research only. Exact paths and roles are consolidated in the Part IV Source Ledger below. The manifest is file control only.

# Part IV Evidence-Status Register

| Evidence item | Design, proposed, completed or unavailable | Controlling source | Allowed conclusion |
|---|---|---|---|
| Frozen TrueMoist identity | Current controlled design | Final architecture, memory and SOP (**TIER_1**) | TrueMoist is a one-soil local compensation experiment with fixed local inference |
| DS18B20 role | Current design | Final architecture (**TIER_1**) | Nearby measured soil temperature is a compensation input |
| S0/S1 treatment code | Current design with pilot-selected S1 dose | Final architecture and memory (**TIER_1**) | Known prepared-batch metadata may be used; no live EC claim |
| ADS1115 architecture | Primary design subject to evidence gate | Final architecture and memory (**TIER_1**) | External ADC is comparison-gated, not inherently authoritative |
| ESP32 controller | Current concept design | Final architecture (**TIER_1**) | Local fixed-coefficient inference is the selected path; course acceptance remains open |
| 72-run factorial | Current authoritative experimental design | Final architecture and memory (**TIER_1**) | Target is 4 × 3 × 2 × 3 independent physical runs |
| Complete 72-run execution | Unavailable | No completed physical dataset or run ledger in the controlled source set | Do not claim completion |
| Independent run definition | Current experimental control | Final architecture and SOP (**TIER_1**) | Rapid electronic readings from one condition are not independent runs |
| Training/model-selection split | Current design | Final architecture (**TIER_1**) | Replicates 1–2 are for development; replicate 3 remains untouched |
| Gravimetric GWC method | Planned controlling reference procedure | Final architecture (**TIER_1**) | Dry-basis GWC is the required physical reference |
| Oven and scale access | Unavailable as completed facility evidence | Final architecture and memory (**TIER_1**) | Accuracy claims remain conditional on credible access and constant mass |
| Model 0 | Current supported model specification | Final architecture (**TIER_1**) | Uncompensated univariate baseline may be described |
| Model 1 | Current supported model specification | Final architecture (**TIER_1**) | Multivariate linear compensation may be described |
| Model 2 | Proposed supported candidate with selection gate | Final architecture (**TIER_1**) | Ridge second-order model may be evaluated conditionally |
| Fitted coefficients | Unavailable | No result source | Do not invent or publish coefficients |
| Python-to-MCU equivalence | Required test, not completed | Final architecture and SOP (**TIER_1**) | Equivalence is a release gate; no passing result exists |
| RMSE criterion | Proposed project criterion | Final architecture (**TIER_1**) | May state 20% held-out improvement as a target only |
| MAE criterion | Proposed project criterion | Final architecture (**TIER_1**) | May state 15% held-out improvement as a target only |
| Subset guardrail | Proposed project criterion | Final architecture (**TIER_1**) | May state no more than 10% MAE worsening as a guardrail only |
| Model 2 complexity gate | Proposed selection rule | Final architecture (**TIER_1**) | Model 2 requires at least 5% RMSE benefit plus stability and equivalence conditions |
| Measured RMSE/MAE improvement | Unavailable | No completed result source | Do not claim performance |
| Probe/ADC/packing gates | Designed; completion unavailable | Final architecture and memory (**TIER_1**) | Architecture is ready only with mandatory early validation |
| Historical BOM | Completed planning estimate, not current market evidence | Final architecture and memory (**TIER_1**) | Historical ₹1,790–₹3,440 range may be reported with date/status limitations |
| Current specifications and prices | Unavailable in this stage | Authority protocol and governing instruction | Later manufacturer and market verification is required |
| TrueMoist implementation approval | Unresolved | Decision Register and validated Part I (**TIER_1**) | Do not claim teacher approval or final selection |
| Project-wide Phase 4/procurement | Unresolved and not authorized by the attached record | Decision Register and validated Part I (**TIER_1**) | Do not begin or claim authorization |
| Patent research | Completed document research | Valid syntheses and controlled lanes (**TIER_2/3**) | Supports a cautious technical position, not legal clearance |
| Ordinary MVP patent value | Reconciled research conclusion | Valid syntheses (**TIER_2**) | High engineering value, low current patent value and no patent-first readiness |
| Future transfer/validity mechanism | Proposed research hypothesis | Valid syntheses (**TIER_2**) | May be described conditionally and separately from the MVP |
| Multi-unit Level-2 evidence | Unavailable | No completed future experiment source | Do not claim transfer, remount validity, contamination control or lifecycle performance |
| TrueMoist pre-build simulation | No file | TrueMoist README (**TIER_2**) | No simulation evidence exists and none may be reconstructed |
| Comparative semester ranking | Completed decision support | Final adjudications and validated Part I (**TIER_2/TIER_1 representation**) | VibeGuard is the strongest recommendation; this is not teacher approval |
| Preferred future patent route | Conflicting completed decision support | Two final adjudications (**TIER_2**) | Preserve disagreement; do not average it |
| Patentability, eligibility and novelty | Unavailable as legal conclusions | Valid syntheses and authority protocol | No confirmed conclusion may be stated |
| Freedom to operate | Unavailable | Valid syntheses and authority protocol | Jurisdiction-specific professional review is required |
| Institutional ownership/inventorship rules | Unavailable | Valid syntheses (**TIER_2**) | Obtain written institutional IPR guidance before claim-focused disclosure |

# Part IV Open-Decision Register

| ID | Decision or uncertainty | Current status | Controlling source | Required next action |
|---|---|---|---|---|
| TM-OD-01 | Final semester concept selection | Unresolved; TrueMoist retained, VibeGuard recommended | Decision Register and validated Part I (**TIER_1**) | Record explicit authorized concept selection |
| TM-OD-02 | Teacher approval of the proposed OpenBraille-to-VibeGuard shift | Not proved | Validated Part I (**TIER_1**) | Obtain and record explicit teacher decision |
| TM-OD-03 | ESP32 or STM32 course-platform acceptance | Unresolved | Teacher context, Decision Register and validated Part I (**TIER_1**) | Obtain written course/platform confirmation |
| TM-OD-04 | Project-wide Phase 4 entry | Not authorized by the attached record | Decision Register and validated Part I (**TIER_1**) | Enter Phase 4 only after recorded authorization |
| TM-OD-05 | Procurement freeze | Not authorized; current prices unverified | Validated Part I and authority protocol (**TIER_1/control**) | Verify current parts/prices and approve BOM before purchase |
| TM-OD-06 | Purchased probe authenticity | Open | Final architecture and memory (**TIER_1**) | Verify identity, coating and analog behavior; reject unsuitable units |
| TM-OD-08 | Reinsertion repeatability | Open | Final architecture and memory (**TIER_1**) | Perform controlled repeated insertion using the frozen jig |
| TM-OD-09 | Final analog acquisition path | Open comparison gate | Final architecture and memory (**TIER_1**) | Compare ADS1115 and calibrated ESP32 ADC1 on the same node |
| TM-OD-10 | Oven, scale and constant-mass access | Unconfirmed | Final architecture and memory (**TIER_1**) | Confirm facility, responsible access, resolution and throughput |
| TM-OD-11 | Final soil and preparation procedure | Pilot-dependent | Final architecture and SOP (**TIER_1**) | Freeze homogeneous soil, masses, container, mixing, equilibration and compaction |
| TM-OD-12 | Exact four moisture target regions | Open until pilot | Final architecture (**TIER_1**) | Freeze targets after soil field-capacity and probe-response characterization |
| TM-OD-14 | Exact S1 NaCl dose | Open until pilot | Final architecture and memory (**TIER_1**) | Select and freeze a repeatable non-saturating dose in g/kg dry soil |
| TM-OD-15 | Packing sensitivity | Open | Final architecture and memory (**TIER_1**) | Quantify independent preparation variance and improve controls if necessary |
| TM-OD-16 | Run order and blocking plan | Incomplete | Final architecture/reconciliation (**TIER_1**) | Preregister randomization/blocking and deviation handling |
| TM-OD-17 | Feasibility of the full 72-run schedule | Unproved | Final architecture and memory (**TIER_1**) | Trial physical throughput before freezing the execution calendar |
| TM-OD-18 | Use of 54-run contingency | Not authorized | Final architecture and reconciliation (**TIER_1**) | Apply formal change control and report reduced evidence if required |
| TM-OD-19 | Completion of main dataset | Not proved started or completed | No completed source | Execute with complete physical run ledger and identifiers |
| TM-OD-22 | Final model choice | Unresolved | Final architecture (**TIER_1**) | Freeze M1 or M2 before opening replicate 3 |
| TM-OD-23 | Python-to-MCU numerical equivalence | Open | Final architecture and SOP (**TIER_1**) | Run fixed-vector equivalence tests and archive results |
| TM-OD-24 | Untouched replicate-3 validation | Not performed in attached evidence | Final architecture (**TIER_1**) | Test only after complete model and firmware freeze |
| TM-OD-25 | Measured RMSE, MAE and subset performance | Unavailable | No completed result source | Report absolute and relative metrics after held-out testing |
| TM-OD-26 | Drift and repeatability reporting | Open | Final architecture and SOP (**TIER_1**) | Define and execute repeatability/drift observations |
| TM-OD-27 | Operational meaning of S0/S1 outside the laboratory | Unresolved | Final architecture plus valid syntheses (**TIER_1/2**) | Keep as laboratory metadata unless a later authorized deployment design defines the input |
| TM-OD-29 | Current component specifications and Indian prices | Unverified in this stage | Authority protocol and governing instruction | Conduct a later controlled manufacturer/supplier verification pass |
| TM-OD-30 | Exact future replacement/remount mechanism | Unfrozen hypothesis | Valid syntheses (**TIER_2**) | Define only after Level-1 feasibility and confidential institutional review |
| TM-OD-31 | Multi-unit and multi-lot Level-2 experiment | Not designed as an authorized programme | Valid syntheses (**TIER_2**) | Develop a separate approved budget, sample plan and evidence protocol |
| TM-OD-32 | Whether the future mechanism beats simple affine transfer and gating | Unknown | Valid syntheses (**TIER_2**) | Run independent baseline and ablation comparisons |
| TM-OD-33 | Current patent-family legal status | Incomplete | Valid syntheses and controlled lanes (**TIER_2/3**) | Refresh official registers and family data for the exact mechanism |
| TM-OD-34 | Jurisdiction-specific FTO | Unavailable | Authority protocol and valid syntheses | Freeze intended acts/territories and obtain professional claim analysis |
| TM-OD-35 | Institutional confidentiality, ownership and inventorship rules | Unresolved | Valid syntheses (**TIER_2**) | Obtain written institutional IPR guidance before claim-focused disclosure |
| TM-OD-36 | Preferred future patent-development concept | Adjudications disagree | Final adjudications (**TIER_2**) | Apply an authorized gate and new physical evidence; preserve disagreement until resolved |

# Part IV Contradiction Summary

| ID | Issue | Controlling resolution | Residual uncertainty |
|---|---|---|---|
| TM-C01 | Historical self-correcting/adaptive platform versus fixed offline-trained MVP | Final architecture, memory and SOP control: fixed coefficients and local inference; adaptive updating is future only | Whether a trusted-event update mechanism is technically viable later |
| TM-C02 | Live EC sensing versus controlled salinity-treatment code | Known S0/S1 prepared-batch metadata controls; no live EC or autonomous chemistry measurement | Operational source of the code outside the controlled experiment |
| TM-C03 | YL-69/HL-69 presented as the selected capacitive sensor | Genuine analog capacitive probe controls; resistive YL-69/HL-69 is rejected as primary sensor | Authenticity and behavior of purchased units |
| TM-C04 | 72 runs versus research-lane plans for 135 or 180 samples | Authoritative target is 72 independent physical runs | Throughput and whether later change control is necessary |
| TM-C05 | Internal ADC by default versus external ADC mandatory | ADS1115 is primary but comparison-gated against calibrated ESP32 ADC1 | Paired physical gate result |
| TM-C06 | Volumetric water content versus dry-basis gravimetric water content | GWC controls; VWC requires independent bulk-density evidence | Whether bulk density will ever be measured |
| TM-C07 | “Architecture Ready” versus unconditional readiness | Correct status is Architecture Ready with Mandatory Early Validation | Outcomes of probe, ADC, packing, treatment and reference gates |
| TM-C08 | “Validated 72-run design” read as completed experiment | Validation refers to architecture selection; physical completion and results are unproved | Actual run ledger, dataset and result report |
| TM-C09 | Ordinary MVP framed as a patent opportunity versus conventional engineering stack | Valid syntheses control under patent-evidence role: high engineering value, low current patent value | Whether a later exact mechanism survives experiment and prior art |
| TM-C10 | Generic OOD, Mahalanobis, confidence or abstention framed as novelty | Generic statistical gating is not verified novelty; only a specific physical interaction may be studied | Whether the composite physical-reference-bound mechanism produces a non-additive effect |
| TM-C11 | Final memory says proceed to Phase 4 versus current project authorization | Concept-level architecture readiness does not override Decision Register/Part I; project-wide Phase 4 remains open | Teacher, concept and platform authorization |
| TM-C12 | Two-month semester path versus three-month patent-extension proposals | Two-month Level-1 MVP controls; Level-2 extension is separate conditional research | Actual authorized future schedule and budget |
| TM-C13 | TrueMoist preferred as future patent path versus deprioritized patent-first route | No higher resolution; preserve both adjudications without averaging | Authorized future gate and new evidence |
| TM-C14 | TrueMoist described as finally selected or rejected | Retained Phase 3C concept; neither selection nor rejection is proved | Explicit teacher/final concept decision |

# Part IV Source Ledger

Only original organized-workspace paths materially relied upon are listed. The attachment manifest is file control only and is not technical evidence. The attached Chapter 08 packet and reconciliation are not listed as substitutes for the original sources.

## TIER_1 — Current architecture and project authority

### Frozen TrueMoist architecture

- `03_CONCEPT_PORTFOLIO/TrueMoist/01_Final_Architecture/Phase3C_TrueMoist_Architecture_Report_Final.md` — controlling hardware, acquisition, model, dataset, metrics, BOM, risks and readiness.
- `03_CONCEPT_PORTFOLIO/TrueMoist/01_Final_Architecture/Phase3C_TrueMoist_Memory_Final.md` — compact frozen architecture, exclusions, early gates and fallbacks.
- `03_CONCEPT_PORTFOLIO/TrueMoist/01_Final_Architecture/Phase3C_TrueMoist_SOP_Final.md` — canonical identity, evidence-quality rules, anti-drift controls, validation stages and exit conditions.

### Project and approval state

- `01_GOVERNANCE_AND_CONTROL/01_Project_Requirements/Teacher_Project_Requirements_and_Change_Context.md` — teacher constraints and approval boundary.
- `01_GOVERNANCE_AND_CONTROL/02_Decision_Registers/Project_mC_Decision_Register_v1.2.md` — canonical project decisions and retained-concept state.
- `01_GOVERNANCE_AND_CONTROL/AUTHORITY_MAP.md` — project authority control used by validated Part I.

## TIER_2 — Controlled decision and patent evidence

### Valid TrueMoist syntheses

- `03_CONCEPT_PORTFOLIO/TrueMoist/03_Patent_Synthesis/01_TrueMoist_Patent_Evidence_Synthesis_Max.md` — Track-C assessment, ordinary-MVP patent position and future composite transfer/validity hypothesis.
- `03_CONCEPT_PORTFOLIO/TrueMoist/03_Patent_Synthesis/02_TrueMoist_Patent_Evidence_Synthesis_High_Deep_Research.md` — audited lane reliability, patent limitations, physical-reference-bound transfer hypothesis and recommendation.

### TrueMoist evidence-control records

- `03_CONCEPT_PORTFOLIO/TrueMoist/PATENT_EVIDENCE_INDEX.md` — controlled six-lane set, two valid syntheses and excluded supplementary audit.
- `03_CONCEPT_PORTFOLIO/TrueMoist/README.md` — frozen-architecture location and no-pre-build-simulation boundary.

### Comparative evidence and adjudications

- `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/00_Engineering_Design_Review.md` — concept identity and comparative engineering boundary.
- `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/04_Hard_Gate_Precheck.md` — neutral gate context.
- `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/05_Uncertainty_and_Test_Register.md` — current unresolved tests and evidence gaps.
- `04_COMPARATIVE_DECISION/02_Final_Adjudications/01_Project_mC_Final_Adjudication_Work_Max.md` — VibeGuard semester recommendation and conditional TrueMoist future route.
- `04_COMPARATIVE_DECISION/02_Final_Adjudications/02_Project_mC_Final_Adjudication_Deep_Research_High.md` — VibeGuard semester recommendation and conditional OpenBraille-first future route.
- `04_COMPARATIVE_DECISION/COMPARATIVE_DECISION_INDEX.md` — adjudications controlled as decision context rather than votes.

### Historical supporting record

- `03_CONCEPT_PORTFOLIO/TrueMoist/05_Roadmaps_and_Reference_Dossiers/HISTORICAL_Phase1C_TrueMoist_Concept_Dossier.docx` — historical origin and adaptive/self-correcting aspirations only; superseded where inconsistent with the frozen architecture.

## TIER_3 — Controlled independent research lanes

- `03_CONCEPT_PORTFOLIO/TrueMoist/02_Raw_Research/01_TrueMoist_Patent_Research_ChatGPT_Deep_Research.md`
- `03_CONCEPT_PORTFOLIO/TrueMoist/02_Raw_Research/02_TrueMoist_Patent_Research_Gemini.docx`
- `03_CONCEPT_PORTFOLIO/TrueMoist/02_Raw_Research/03_TrueMoist_Patent_Research_Perplexity_PARTIAL.md`
- `03_CONCEPT_PORTFOLIO/TrueMoist/02_Raw_Research/04_TrueMoist_Patent_Research_Qwen_COMPILATION.md`
- `03_CONCEPT_PORTFOLIO/TrueMoist/02_Raw_Research/05_TrueMoist_Patent_Research_Mistral.md`
- `03_CONCEPT_PORTFOLIO/TrueMoist/02_Raw_Research/06_TrueMoist_Patent_Research_Microsoft_Copilot.docx`

These lanes are supporting evidence only. Their recurring assertions do not establish truth. Unsupported, overconfident or concept-swapped conclusions are excluded rather than averaged into the controlled position.
