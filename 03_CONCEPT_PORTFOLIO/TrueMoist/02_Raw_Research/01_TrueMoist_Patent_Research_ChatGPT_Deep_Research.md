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
