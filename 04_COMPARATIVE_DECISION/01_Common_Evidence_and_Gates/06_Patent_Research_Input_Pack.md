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
