# TrueMoist Current Patent Verification — Independent Research

**Evidence cut-off:** 1 August 2026  
**Search performed:** 2 August 2026  
**Current-status snapshot:** 2 August 2026; any post-cut-off register event is administrative status information, not substantive prior art  
**Scope:** independent technical, patent-landscape and project-decision research; **not legal advice, patentability/FTO clearance, claim construction or an infringement opinion**

## Reading key

- **Verified fact** — supported by a cited project record, patent publication, official source or primary technical source.
- **Source assertion** — a claim made by a manufacturer, aggregator or author and reported as such.
- **Inference** — this report's reasoned conclusion from the cited evidence.
- **Recommendation** — proposed project action.
- **Unresolved** — not established from the accessible record and requiring a register search, experiment, translation or counsel.

Google Patents was used for discovery, family mapping and claim reading. Its own pages state that legal-status and assignee fields are assumptions, not legal conclusions. Accordingly, every “active”, “pending”, “expired” or anticipated-expiry label below that is not separately confirmed by an official register is expressly marked **GP provisional**. Publication/grant existence is not the same as a currently enforceable right. Conversely, an expired or abandoned record remains potentially effective prior art.

---

## 1. Executive verdict

### Required verdict

**credible long-term path requiring later-semester extension**

### Board finding

**Verified fact:** The complete logical input set is present and the controlling design is the validated 72-run TrueMoist architecture: a local, fixed-coefficient compensation system for a genuine low-cost analog capacitive probe, using a nearby DS18B20 and a controlled salinity-treatment **code**, with no live EC measurement.

**Inference:** The frozen MVP is a credible, useful and well-controlled semester engineering experiment. It does **not**, on the evidence found, establish a credible invention in its present compensation formula, hardware selection or validation protocol. Low-cost capacitive-probe calibration, sensor-specific polynomial mapping, temperature correction, salinity/conductivity sensitivity analysis, local microcontroller processing, gravimetric reference measurement and probe-to-probe variability were all disclosed before the cut-off. The 72-run grouped design improves evidential quality but is not itself a demonstrated technical mechanism.

No reviewed independent claim was found that literally requires the complete frozen feature set. That is only a preliminary search observation; it is **not** a finding of novelty, non-obviousness, patentability or FTO.

The strongest connected research hypothesis is a **mechanism-tied calibration-validity and replacement/remount transfer system**: characterize a commodity probe with controlled physical reference challenges, create a probe fingerprint and validity envelope, and locally accept, transfer, recalibrate or abstain based on a measurable physical mismatch. This is not in the current MVP, is crowded by prior work on replaceable-probe conditioning, reference-media calibration, sensor-health monitoring, event-based recalibration and commercial verification tools, and needs a substantially larger blinded probe/remount/aging study. It therefore belongs to Track C, not Track A or B.

### Decision summary

| Question | Finding |
|---|---|
| Frozen MVP contribution | No credible patent contribution established; conventional combination risk is high. |
| Controlled salinity code | Strong experimental factor; weak patent distinction because it is a known label, not a runtime physical measurement. |
| 72-run grouped validation | Good science and essential for trustworthy claims; not independently inventive on this record. |
| Bounded three-month enhancement | Useful health/validity experiments are possible, but two probes cannot substantiate general transfer, replacement or aging claims. |
| Strongest path | Later-semester physical-reference fingerprint plus calibration-validity/replacement/remount transfer gate. |
| Hardware redesign required | Not for the Track-C hypothesis; multi-frequency or live-EC paths would be major redesigns and are not recommended for the frozen semester. |
| Preliminary FTO | No obvious literal read of the analyzed independent claims on the frozen MVP, but no clearance is given; several live-claim families require jurisdiction-specific counsel if scope changes. |

---

## 2. Input inventory and concept fidelity

### 2.1 Attachment inventory

Exactly **11** visible attached project files were inventoried. Each is non-empty, readable as UTF-8 Markdown and has a distinct SHA-256 digest. Parenthetical suffixes such as `(2)`, `(13)` and `(14)` are upload/copy suffixes; the leading index and base title give one unambiguous logical mapping to canonical files 00–10.

| # | Canonical logical input | Attached filename | Readable | Digest prefix | Authority role |
|---:|---|---|---|---|---|
| 00 | `00_READ_FIRST_TrueMoist_Patent_Research_Instructions.md` | `00_READ_FIRST_TrueMoist_Patent_Research_Instructions(2).md` | Yes | `e201944a6a67` | Governing task specification |
| 01 | `01_Engineering_Design_Review.md` | `01_Engineering_Design_Review(13).md` | Yes | `46f017501ac3` | Authority 1 |
| 02 | `02_Project_mC_Decision_Register_v1.2.md` | `02_Project_mC_Decision_Register_v1.2(14).md` | Yes | `9678c5072d86` | Authority 2; **v1.2 confirmed** |
| 03 | `03_Phase3C_Portfolio_Closure_Memo_Approved.md` | `03_Phase3C_Portfolio_Closure_Memo_Approved(13).md` | Yes | `3c6e6f568c06` | Authority 3 |
| 04 | `04_Phase3C_TrueMoist_Architecture_Report_Final.md` | `04_Phase3C_TrueMoist_Architecture_Report_Final(2).md` | Yes | `6c71f1d618e0` | Authority 4 |
| 05 | `05_Phase3C_TrueMoist_Memory_Final.md` | `05_Phase3C_TrueMoist_Memory_Final(2).md` | Yes | `c84bc0e08c8c` | Authority 5 |
| 06 | `06_Phase3C_TrueMoist_SOP_Final.md` | `06_Phase3C_TrueMoist_SOP_Final(2).md` | Yes | `993caf1a05f3` | Authority 6 |
| 07 | `07_Concept_Evidence_Matrix.md` | `07_Concept_Evidence_Matrix(13).md` | Yes | `8f999b878cfc` | Authority 7, validated evidence |
| 08 | `08_Uncertainty_and_Test_Register.md` | `08_Uncertainty_and_Test_Register(13).md` | Yes | `125c05722952` | Authority 7, validated evidence |
| 09 | `09_Patent_Research_Input_Pack.md` | `09_Patent_Research_Input_Pack(14).md` | Yes | `969d6bd97f0a` | Authority 7, research input |
| 10 | `10_Phase2_Report_by_Claude.md` | `10_Phase2_Report_by_Claude(14).md` | Yes | `783729d0e07e` | Authority 8, untrusted historical leads only |

**Inventory conclusion:** no required logical input is missing, duplicated, unreadable or ambiguously named. Decision Register **v1.2**, not v1.1, is present. The governing instruction is readable. All ten canonical project documents 01–10 are present.

### 2.2 Authority handling

The project authority order was applied exactly as specified: Engineering Design Review; Decision Register v1.2; approved closure memo; final architecture report; final memory; final SOP; validated evidence files; then Phase 2 only as historical patent-search leads. Where older broad language mentioned adaptation, irrigation or wider systems, the later validated freeze controlled. Portfolio comparison material was not used to rank TrueMoist against any other concept. No Phase 2 conclusion was accepted as a current verified fact.

### 2.3 Authoritative concept freeze

**Verified architecture:**

- genuine SEN0193-class analog capacitive probe; two units for variation checks;
- waterproof DS18B20 at the same depth and approximately 20–30 mm away;
- known salt addition per dry-soil mass represented as a controlled treatment code;
- **no live bulk-soil EC, apparent EC, pore-water EC or solution-conductivity channel**;
- ESP32-WROOM-32, with ESP32-S3 fallback;
- ADS1115 primary subject to a mandatory Week-1 paired comparison with calibrated ESP32 ADC1;
- approximately 1 kΩ series resistance, 100 nF input filtering, 100 nF plus 10 µF local decoupling, short fixed analog wiring, deliberate grounding and soldered perfboard after characterization;
- USB 5 V and serial CSV; no cloud/app dependency and no irrigation control;
- M0 raw univariate mapping, M1 multivariate linear regression, M2 ridge-regularized second-order regression;
- raw probe response, temperature and controlled salinity-treatment code as model inputs;
- offline Python training and fixed local ESP32 coefficients; no TinyML requirement or online adaptation;
- one homogeneous soil and one documented preparation/packing method;
- 4 moisture × 3 temperature × 2 salinity × 3 independent replicates = **72 physical runs**;
- replicates 1–2 for fitting/selection and replicate 3 untouched; rapid ADC readings are averages, never independent samples;
- dry-basis gravimetric water content (GWC), drying near 105 ± 5 °C for at least 24 hours and to constant mass; no VWC claim without independently measured bulk density;
- engineering success remains at least 20% held-out RMSE reduction and 15% held-out MAE reduction, with absolute and subset errors reported.

The frozen concept is therefore a local compensation system—not a live-EC meter, irrigation controller, cloud platform, multi-soil system, custom multi-frequency probe, TinyML showcase or online-adaptive learner.

---

## 3. Search methodology and reproducible log

### 3.1 Method

Searches were run independently on 2 August 2026, with substantive evidence restricted to material available by 1 August 2026. The workflow was:

1. phrase and synonym searching in Google Patents and web search;
2. CPC/IPC and assignee searching;
3. family normalization by earliest priority and representative publications;
4. independent-claim reading for the closest records;
5. backward/forward citation and related-application chaining;
6. official publication/register checks where dynamically accessible;
7. primary technical literature and manufacturer-practice review;
8. feature-chart, novelty, inventive-step, eligibility and claim-by-claim FTO separation.

Official systems targeted included USPTO Patent Public Search/Patent Center, WIPO PATENTSCOPE, EPO publication/register resources and official Asian sources. USPTO Patent Center pages for applications 17/594,378, 17/215,508 and 12/465,620 rendered as JavaScript-only shells in the accessible environment; they did not provide a citable current transaction/status record. The [USPTO filing-status guidance](https://www.uspto.gov/patents/apply/checking-application-status/check-filing-status-your-patent-application), [USPTO Patent Public Search](https://www.uspto.gov/patents/search/patent-public-search) and [EPO patent-search resources](https://www.epo.org/en/searching-for-patents) identify the official follow-up mechanisms. Those unresolved status points are not silently replaced by Google labels.

### 3.2 Exact mandatory phrase log

All mandatory phrases were searched exactly as written; variants added `claim`, `patent`, `sensor`, `capacitive`, `soil`, `probe`, `calibration`, assignee names and CPC classes.

| # | Database(s), date | Exact query | Selection/rejection result |
|---:|---|---|---|
| 1 | Google Patents + web, 2026-08-02 | `capacitive soil moisture temperature compensation patent` | Selected US11598743, US9949450, CN102944577; rejected temperature-only environmental monitors. |
| 2 | Same | `soil moisture salinity compensation capacitance patent` | Selected US7884620, US5418466, US11415612; rejected generic fertilizer/irrigation control. |
| 3 | Same | `dielectric soil moisture conductivity correction` | Selected METER/Delta-T complex dielectric families and Kizito NPL; rejected remote-sensing dielectric retrieval. |
| 4 | Same | `commodity probe calibration transfer` | Selected CN102914568, Bogena, Kulmány; rejected non-soil gas/air-quality transfer. |
| 5 | Same | `probe-to-probe soil-moisture calibration` | Selected CN102914568, TCS health family, SEN0193 studies; rejected premium-probe factory calibration without transferable method detail. |
| 6 | Same | `soil-moisture sensor drift/ageing compensation` | Selected TCS and Senviro; rejected hydrological-model drift unrelated to sensor health. |
| 7 | Same | `insertion and packing-density compensation` | Selected Sentek insertion family and controlled-calibration NPL; rejected purely mechanical augers without sensing relation. |
| 8 | Same | `remount/reinstallation calibration validity` | Selected METER verification/installation practice and replacement records; no exact frozen mechanism found. |
| 9 | Same | `gravimetric calibration capacitive soil moisture` | Selected SEN0193 studies, CN calibration methods, ISO/FAO practice; rejected papers without physical reference. |
| 10 | Same | `polynomial/ridge regression sensor calibration` | Selected SEN0193 polynomial and data-driven temperature literature; ridge itself treated as generic modeling, not novelty. |
| 11 | Same | `edge soil-moisture compensation microcontroller` | Selected local-MCU patent disclosures; rejected cloud-only systems and irrigation dashboards. |
| 12 | Same | `uncertainty-gated or abstaining moisture estimate` | Selected commercial validity/verification and general uncertainty leads; no soil-specific independent claim matching the proposed gate found. |
| 13 | Same | `dual-probe disagreement sensor health` | Selected TCS health and multi-probe diagnostics leads; simple averaging/redundancy rejected as weak. |
| 14 | Same | `reference-event self-calibration` | Selected Senviro and Toro event-based calibration; rejected irrigation scheduling without recalibration. |
| 15 | Same | `multi-soil calibration transfer` | Selected Kizito, González-Teruel, Kulmány and recent generalized SEN0193 studies; classified outside frozen MVP. |
| 16 | Same | `multi-frequency moisture/salinity separation` | Selected US7884620, US5418466, METER complex-dielectric and dual-frequency NPL; classified major redesign. |
| 17 | Same | `sensor replacement automatic recalibration` | Selected CN102914568, Senviro, TCS and commercial verification practice; no clean Track-B claim space established. |

### 3.3 Classification, assignee and citation-chain log

| Search axis | Exact term(s) | Results retained |
|---|---|---|
| CPC/IPC | `G01N33/246`, `G01N27/223`, `G01N27/22`, `G01R27/26`, `G06T7/136`, `A01G25/16` | Soil water, capacitance/dielectric, complex impedance and TCS image-health records; irrigation-only claims were scope exclusions. |
| METER/Decagon | `assignee:(Decagon Devices)`; `assignee:(METER Group)`; Campbell/Cobos/Castiglione inventor variants | US7884620 related line, US11415612, 70 MHz/commercial verification practice and Kizito literature. |
| Campbell Scientific | `assignee:(Campbell Scientific)` plus `CS650`, `CS655`, `water content reflectometer patent` | Product/technical practice; no claim was inferred from product features. |
| Sentek | `assignee:(Sentek)` plus `soil probe insertion` | US7240743 and related probe/insertion records. |
| Delta-T | `assignee:(Delta-T Devices)` plus `moisture content sensor impedance phase` | US7944220 and WET-family commercial practice. |
| Vegetronix | `assignee:(Vegetronix)` plus `VH400 soil moisture patent calibration` | Product and search leads; no load-bearing independent claim was established. |
| Agriculture/irrigation | `Toro soil moisture field capacity calibration`; `Fiskars soil moisture sensor`; `John Deere soil moisture calibration` | Toro reference-event line, Fiskars RLC family, Deere fixture calibration. |
| India | `India low cost soil moisture sensor health patent`; `TCS soil moisture calibration health`; priority `202021001465` | WO2021144807; US12175680; EP4090953; Indian priority identified but no Indian grant/status established. |
| China/universities | Chinese applicants plus `replaceable probe`, `temperature calibration`, `humidity fusion correction` | CN102914568, CN102944577, CN106248522, CN116298198. |

Citation chains followed included US7884620 into earlier moisture/salinity and later custom-probe families; CN102914568 into replacement/reference calibration; Senviro into event and adaptive-calibration art; and WO2021144807/US12175680 into its cited low-cost-sensor calibration and image-health literature. Closest results were retained even when abandoned or expired. Cloud platforms, remote sensing, crop-decision systems, generic irrigation control, custom spectroscopy and multi-frequency hardware were rejected from literal frozen-MVP comparison but retained where they show a crowded technical principle or a redesign boundary.

---

## 4. Technical and patent landscape

### 4.1 Landscape map

| Cluster | What was already public | Consequence for TrueMoist |
|---|---|---|
| Commodity capacitive calibration | Air/water boundary mapping, soil-specific gravimetric calibration, linear/polynomial fits, low-cost MCU acquisition | Raw-to-GWC regression and low cost are not differentiators. |
| Environmental compensation | Temperature dependence and data-driven correction; salinity/EC effects; frequency-dependent sensitivity | Adding temperature and a controlled salt factor is a predictable calibration design. |
| Complex/multi-frequency sensing | Low/high frequency separation and simultaneous permittivity/conductivity measurement | Strong technical mechanisms exist, but they require custom sensing and/or live EC, outside the freeze. |
| Probe variability/transfer | Unit-to-unit variability, individual calibration, reference-media normalization and replaceable-probe conditioning | Automatic transfer is relevant but already crowded; a new causal mechanism and strong evidence are required. |
| Installation/packing | Air gaps, contact, insertion geometry, repacking and fixtures materially influence readings | A fixed jig is good measurement hygiene; compensating remount state might be researchable if physically measured. |
| Health/drift/validity | Sensor wear monitoring, event recalibration, bounds, verification standards, replace/repair recommendations | Generic “detect drift”, “confidence” or “abstain” logic is unlikely to be enough. |
| Experimental validation | Gravimetric reference, constant-mass drying, held-out metrics, multi-factor calibration | The 72-run protocol supports evidence; protocol rigor alone does not create a new sensor mechanism. |

### 4.2 Central technical finding

The frozen M2 model estimates dry-basis GWC as a second-order function of raw voltage, measured temperature and an assigned salt-treatment code. The salt code carries preparation information that the system already knows; it does not sense the soil's current ionic state. Its compensation can therefore work only within the controlled treatment/preparation domain. A field sample with unknown salt distribution, ion mobility, water chemistry or temperature-dependent conductivity may share the same code while having a different dielectric loss. That limitation is experimentally honest but weakens both universal utility and patent distinction.

The most important technical uncertainty is not MCU compute or ADC bit depth. It is identifiability: can the experiment separate true water content from probe-unit response, packing/contact, temperature and salinity-treatment effects using two units and one preparation? The untouched third physical replicate is valuable, but it does not by itself test new probe replacement, new packing batch, aging, remounting or a new soil.

---

## 5. Verified patent-family ledger

Status legend: **official publication/grant** means the numbered publication exists; **GP provisional** is the non-authoritative Google legal-status indicator on 2 August 2026; **unresolved** means an official current register result was not obtained.

| Family / representative | Earliest priority; applicant | Relevant independent-claim or disclosure core | Publication/grant and provisional status | Prior-art relevance | FTO relevance to frozen MVP |
|---|---|---|---|---|---|
| [US12175680B2](https://patents.google.com/patent/US12175680B2/en); [WO2021144807A1](https://patents.google.com/patent/WO2021144807A1/en); [EP4090953B1](https://patents.google.com/patent/EP4090953B1/en) | 2020-01-13; Tata Consultancy Services; Indian provisional 202021001465 | Low-cost resistive/capacitive sensor, calibration, captured sensor image, edge/contour/silver-pixel/connectivity analysis, degradation stage, corrective modification/replacement | US grant 2024-12-24 and EP grant publication 2024-10-09 verified; US/EP “active” GP provisional; Indian right unresolved | **Very high** for low-cost health, calibration and replacement problem | Frozen system lacks the mandatory image-analysis chain, so no literal read found in claims 1/6; high concern only if optical health logic is added. |
| [CN102914568B](https://patents.google.com/patent/CN102914568B/en) | 2012-10-09; South China Agricultural University | Custom replaceable probe; known-moisture soils and known-dielectric organic solutions; sensitivity relation; adjust new probe in reference solution to old output | CN grant 2014 verified; “active to 2032” GP provisional, CNIPA current status unresolved | **Very high** for replacement transfer/reference conditioning | Frozen purchased probe, voltage model and no replacement conditioning differ; China FTO concern if that mechanism is adopted. |
| [US20080199359A1](https://patents.google.com/patent/US20080199359A1/en) / WO family | 2005-07-04; Senviro Pty Ltd | Capacitance sensor, periodic values and scaling; stable wet/dry extrema, placement/contact/aging discussion, event/history recalibration | US publication verified; US “abandoned” GP provisional; EP/WO family ceased/withdrawn indications require register confirmation | **Very high** against generic self-calibration, adaptive bounds and validity concepts | Dead/ceased members may not block FTO but remain prior art; frozen fixed model avoids online recalibration. |
| [US9146206B2](https://patents.google.com/patent/US9146206B2/en) / EP fixture family | 2012-era Deere line | Known-volume sleeve/ring-electrode fixture; air/water/dry/saturated reference states; oscillator/frequency calibration constants | US grant verified; “active” GP provisional; precise family/status requires official verification | High for controlled reference fixtures and calibration states | Custom fixture/electrodes/frequency output absent from frozen probe; adoption needs claim review. |
| [CN102944577A](https://patents.google.com/patent/CN102944577A/en) | 2012-11-08; Suzhou Nanzee Sensing Technology | Soil column, balance, known water increments, 24-hour stabilization; climate cabinet across 10–50 °C to derive temperature calibration | CN application publication verified; 13-year “pending” indicator is unreliable; current status unresolved | **Very high** for controlled moisture-by-temperature calibration | Specific TDT fixture limits may be absent, but the disclosure crowds the experimental concept. |
| [US11598743B2](https://patents.google.com/patent/US11598743B2/en) / KR family | 2020-03-27; Damoatech | Outer/inner electrodes in a single custom probe; sensing and matched reference resonance circuits; resonant-frequency difference; temperature sensor in dependent claims | US grant 2023 verified; “active to 2041” GP provisional | High for resonance-reference temperature compensation | Frozen off-the-shelf oscillator board plus separate DS18B20 lacks claim-1 structure. |
| [US7884620B2](https://patents.google.com/patent/US7884620B2/en), related US7535237/US7408364; WO2009094324 | 2008-01-21; Green Badge/Advanced Sensor Technology line | HF capacitor divider plus LF resistor divider; MCU correlates electrical properties to moisture and salinity; contacting electrodes and wireless output | US grant 2011 verified; “active to 2028” GP provisional | **Very high** for moisture/salinity separation | Frozen architecture has neither dual-frequency/live-salinity circuit nor wireless output; redesign would raise FTO concern. |
| [US9804113B2](https://patents.google.com/patent/US9804113B2/en) / WO2015177715 / EP3145292 | 2014-05-19; Fiskars; Indian priority record | Capacitive probe coupled to series RLC, driven by MCU; output used to determine capacitance and moisture | US and EP grants/publications verified; US “active to 2035” GP provisional | High for MCU/RLC capacitive sensing | Frozen system buys a probe module and samples its analog output; it does not implement the claimed external RLC probe arrangement. |
| [US11415612B2](https://patents.google.com/patent/US11415612B2/en) | 2019-10-08; METER Group | Voltage source, electrodes, two reference impedances/junction amplitudes and a reactive element; calculate complex admittance/permittivity/conductivity | US grant 2022 verified; “active to 2040” GP provisional | High for simultaneous dielectric/conductivity and validity via sensitivity | Frozen single analog output and no live EC/complex admittance avoid the independent structure. |
| [US7944220B2](https://patents.google.com/patent/US7944220B2/en) / GB/EP family | 2006-era; Delta-T Devices line | Custom impedance/amplitude/phase moisture sensing; temperature/conductivity features in narrower claims/disclosure | US grant verified; “active to 2027” GP provisional | High for custom complex measurement | Frozen probe does not expose or create the claimed complex-impedance signal path. |
| [US7240743B2](https://patents.google.com/patent/US7240743B2/en) | 2001-era; Sentek-related line | Probe insertion/access arrangement designed to obtain smooth contact and reduce air gaps | US grant verified; lifetime-expired indicator GP provisional | High for insertion/contact problem and fixtures | Mechanical claim details require review before copying an insertion arrangement; ordinary documented placement remains distinct. |
| [US9949450B2](https://patents.google.com/patent/US9949450B2/en) | 2014-11-03; Morph2O | Custom multi-conductor PCB probe, wireless system/zone control and temperature-related operation | US grant 2018 verified; fee-related expiry GP provisional | Medium for probe construction and temperature adjustment | Frozen purchased probe, serial logging and no irrigation/wireless avoid central claim limitations. |
| [US8938361B2](https://patents.google.com/patent/US8938361B2/en) | 2011-era; electronic gardening tool line | Analog soil sensor, ADC/MCU/display; startup averaging/zero reference | US grant verified; “active to 2033” GP provisional | Medium for basic MCU acquisition and simple reference routines | Display/configuration and claim-specific routine are absent; generic ADC averaging remains conventional. |
| [US5418466A](https://patents.google.com/patent/US5418466A/en) | 1992-era | High/low-frequency tuned circuits for moisture and salinity | US grant/publication verified; expired | High historical prior art for multi-frequency separation | No FTO block if expired, but later multi-frequency redesign faces strong prior art. |
| [CN116298198A](https://patents.google.com/patent/CN116298198A/en) | 2023-02-21; Chinese applicant | Multi-parameter temperature/moisture/conductivity/organic-matter system; gravimetric multi-soil data and nonlinear fusion correction | CN application publication verified; “pending” GP provisional | **High** against generic multivariate fusion/correction | Frozen lacks live conductivity, organic matter and multi-soil system; China status/claims need official translation. |
| [CN106248522B](https://patents.google.com/patent/CN106248522B/en) | 2016-era; Chinese applicant | Laboratory calibration of a soil-moisture sensor with prepared/repacked samples and gravimetric comparison | CN grant verified; fee-related expiry GP provisional | High for laboratory calibration workflow | Not an obvious frozen-MVP literal read from accessible translation; prior-art effect persists. |

Additional representative art reviewed but not relied on for a closest-claim finding included [US7170302B2](https://patents.google.com/patent/US7170302B2/en) (custom planar PCB probe), [US8947102B1](https://patents.google.com/patent/US8947102B1/en) (TDR moisture/EC/temperature), [US11445275B2](https://patents.google.com/patent/US11445275B2/en) (high/low-frequency environmental sensing), [EP3791161B1](https://patents.google.com/patent/EP3791161B1/en) (multimodal soil spectroscopy) and [US10028425B2](https://patents.google.com/patent/US10028425B2/en) (vehicle/remote multi-frequency sensing). They reinforce the redesign boundary rather than the literal frozen architecture.

---

## 6. Closest independent-claim analyses

### 6.1 TCS low-cost sensor health — US12175680B2 / EP4090953B1

**Claim core verified:** US independent system claim 1 requires the low-cost resistive/capacitive soil sensor and calibration, but also a multimedia component and a particular image-processing chain: denoising/binary edge map, probe contour, specified silver-pixel identification and connectivity, performance/degradation evaluation and correction. Independent method claim 6 follows the same optical-health architecture. The [published claims](https://patents.google.com/patent/US12175680B2/en#claims) are materially narrower than the title.

**Frozen overlap:** low-cost capacitive sensor, calibration, processor and concern about degradation/variation. **Missing limitations:** image capture, threshold/contour/silver-pixel/connectivity features and modification/replacement recommendation. **Literal FTO inference:** no claim-1/6 read found on the frozen MVP. **Patentability effect:** very damaging to a broad claim such as “calibrate and monitor health of a low-cost capacitive soil sensor”; TrueMoist would need a different, specific physical mechanism. **Status:** US and EP grants verified, live status not officially concluded.

### 6.2 Replaceable-probe transfer — CN102914568B

**Claim core verified:** translated independent claim 1 fixes probe geometry, calibrates in known-moisture soil and known-dielectric organic solutions, uses a sensitivity relation for replacement, and—when sensitivities differ—places the replacement probe in the same known solution and adjusts its conditioning output to match the old probe. See the [translated claim text](https://patents.google.com/patent/CN102914568B/en#claims).

**Frozen overlap:** sensor-output calibration, known reference conditions and interest in probe replacement. **Differences:** TrueMoist uses complete commodity modules, GWC regression and no replacement/conditioning step or organic dielectric reference. **Literal FTO inference:** current MVP does not perform the claim sequence. **Patentability effect:** a generic “automatic calibration transfer using a reference state” is crowded. A surviving transfer direction must use a different measurable fingerprint, demonstrate a non-predictable transfer effect and still receive Chinese claim/translation review. **Status:** CN grant verified; “active” is GP provisional.

### 6.3 Senviro self-calibration — US20080199359A1

**Claim/disclosure core:** capacitance sensing, periodic readings and scaling; the specification describes wet/dry extrema learned from stable states, history/event recalibration, placement/contact and aging concerns. [US publication](https://patents.google.com/patent/US20080199359A1/en).

**Frozen overlap:** capacitive reading, bounds/calibration and potential validity/drift extensions. **Differences:** frozen coefficients are fixed and have no history learning or online bound update. **FTO:** the US case is shown abandoned by the aggregator, so it is not treated as a live US blocker; family status still requires official review. **Patentability effect:** extremely strong prior art against generic reference-event self-calibration, bounded adaptation and wet/dry validity concepts.

### 6.4 Deere controlled fixture/reference states — US9146206B2 family

**Claim core:** a fixture of known dimensions and specified electrodes/oscillator is used to determine calibration constants; related claims use known reference states such as air, water, dry and saturated media. [US family record](https://patents.google.com/patent/US9146206B2/en); an [official EPO publication PDF](https://data.epo.org/publication-server/rest/v1.0/publication-dates/20130807/patents/EP2623971NWA1/document.pdf) confirms the European publication line.

**Frozen overlap:** controlled states and fitting calibration constants. **Differences:** SEN0193 voltage output, GWC levels and ordinary container rather than the claimed electrode fixture/frequency arrangement. **FTO inference:** no current literal read identified, but any new reference fixture must be mapped. **Patentability effect:** reference-state calibration is not open territory merely because TrueMoist uses a commodity probe.

### 6.5 Temperature calibration fixture — CN102944577A

**Claim/disclosure core:** a soil column, balance/water-delivery apparatus and TDT probe; the disclosure holds moisture states and varies climate-cabinet temperature from 10–50 °C after stabilization to produce correction curves. [Translated publication](https://patents.google.com/patent/CN102944577A/en).

**Frozen overlap:** controlled moisture × temperature calibration. **Differences:** TDT probe and specific apparatus; TrueMoist adds a salt-treatment factor and grouped held-out test. **FTO:** status is unresolved; Google’s long-running “pending” label is not accepted. **Patentability effect:** a factorial temperature-calibration protocol is old even if the exact factor counts differ.

### 6.6 Damoatech resonance/temperature family — US11598743B2

**Claim core verified:** independent claim 1 requires a custom first probe with outer and inner electrodes, a sensing resonance circuit, a matched reference resonance circuit and a determination based on their resonant frequencies. Temperature sensing appears in dependent claims, including claim 2. [Claims](https://patents.google.com/patent/US11598743B2/en#claims).

**Frozen overlap:** soil state determination and nearby temperature measurement. **Differences:** separate SEN0193 module/DS18B20, no matched resonance reference and no specified electrode geometry. **FTO inference:** no literal claim-1 read. **Patentability effect:** “add temperature compensation to a capacitance-type soil sensor” is too broad; structural limitations drive this family’s claim scope.

### 6.7 Green Badge moisture/salinity family — US7884620B2

**Claim core verified:** independent claim 1 requires both HF capacitor-divider and LF resistor-divider sensing, conductive contacting surfaces, MCU correlation to moisture and salinity, and wireless transmission. [Claim 1](https://patents.google.com/patent/US7884620B2/en#claims).

**Frozen overlap:** MCU processing of an electrical soil signal and salinity as an influence. **Differences:** no LF conductivity channel, no custom conducting surfaces or wireless output; the known salt code is not measured salinity. **FTO inference:** no literal frozen-MVP read. **Patentability effect:** multi-frequency/live-salinity separation is a crowded hardware redesign and cannot be used as an easy escape.

### 6.8 Fiskars MCU/RLC family — US9804113B2

**Claim core verified:** independent claim 1 requires a capacitive probe electrically coupled to a series RLC circuit; an MCU drives the RLC, reads voltage/current, determines capacitance and derives moisture. [Claims](https://patents.google.com/patent/US9804113B2/en#claims).

**Frozen overlap:** capacitive sensing, MCU and analog acquisition. **Differences:** TrueMoist reads a supplier module’s voltage and does not build the claimed series-RLC sensing circuit. **FTO inference:** no literal claim-1 read identified. **Patentability effect:** ESP32/ADC selection and local calculation are ordinary implementation choices.

### 6.9 METER complex dielectric sensor — US11415612B2

**Claim core:** specified voltage-source/electrode/reference-impedance/junction-amplitude structure with a reactive element enables complex-admittance calculation. [US patent](https://patents.google.com/patent/US11415612B2/en).

**Frozen overlap:** dielectric sensing in porous media. **Differences:** single opaque analog probe output, no two reference impedances/amplitudes and no calculated conductivity. **FTO inference:** the frozen MVP does not implement that structure. **Patentability effect:** a later live-EC or complex-dielectric redesign must be mapped to this family and Delta-T/older multi-frequency art before hardware selection.

---

## 7. Frozen-MVP feature comparison

This is a document-disclosure chart, not a claim-construction or infringement chart. Every cell uses only the mandated vocabulary.

| Frozen feature | TCS US12175680 | CN102914568 | Senviro US20080199359 | Deere US9146206 family | CN102944577 | Damoatech US11598743 | Green Badge US7884620 | CN116298198 |
|---|---|---|---|---|---|---|---|---|
| Commodity analog capacitive probe | expressly disclosed | absent | expressly disclosed | absent | absent | absent | absent | arguably suggested |
| Two probe units/variation check | arguably suggested | expressly disclosed | arguably suggested | arguably suggested | absent | arguably suggested | arguably suggested | arguably suggested |
| DS18B20 20–30 mm away at same depth | arguably suggested | absent | arguably suggested | absent | arguably suggested | absent | absent | arguably suggested |
| Controlled salt per dry mass | absent | absent | absent | absent | absent | absent | absent | arguably suggested |
| Salinity-treatment code as model input | absent | absent | absent | absent | absent | absent | absent | arguably suggested |
| No live EC measurement | absent | expressly disclosed | expressly disclosed | unresolved | expressly disclosed | expressly disclosed | absent | absent |
| ADS1115 primary | absent | absent | absent | absent | absent | absent | absent | unresolved |
| Paired ADS1115/calibrated ADC1 gate | absent | absent | absent | absent | absent | absent | absent | absent |
| 1 kΩ/100 nF/decoupling/short fixed wiring | unresolved | expressly disclosed | unresolved | expressly disclosed | unresolved | expressly disclosed | expressly disclosed | unresolved |
| ESP32-class local inference | expressly disclosed | arguably suggested | expressly disclosed | arguably suggested | absent | expressly disclosed | expressly disclosed | expressly disclosed |
| M0 raw univariate mapping | expressly disclosed | expressly disclosed | expressly disclosed | expressly disclosed | expressly disclosed | arguably suggested | expressly disclosed | expressly disclosed |
| M1 multivariate linear model | arguably suggested | arguably suggested | arguably suggested | arguably suggested | arguably suggested | arguably suggested | arguably suggested | expressly disclosed |
| M2 ridge second-order model | absent | absent | absent | absent | absent | absent | arguably suggested | arguably suggested |
| Offline training/fixed coefficients | expressly disclosed | expressly disclosed | absent | expressly disclosed | expressly disclosed | expressly disclosed | expressly disclosed | expressly disclosed |
| One soil/one packing method | unresolved | arguably suggested | unresolved | arguably suggested | expressly disclosed | unresolved | unresolved | absent |
| 4×3×2×3 = 72 physical runs | absent | absent | absent | absent | absent | absent | absent | absent |
| Replicates 1–2 select; replicate 3 untouched | absent | absent | absent | absent | absent | absent | absent | arguably suggested |
| ADC repeats not independent | absent | absent | absent | absent | absent | absent | absent | absent |
| Dry-basis gravimetric truth | arguably suggested | expressly disclosed | arguably suggested | arguably suggested | expressly disclosed | unresolved | arguably suggested | expressly disclosed |
| 105 ± 5 °C, ≥24 h, constant mass | absent | unresolved | absent | unresolved | arguably suggested | absent | absent | arguably suggested |
| Probe replacement/transfer | expressly disclosed | expressly disclosed | arguably suggested | arguably suggested | absent | absent | absent | arguably suggested |
| Drift/aging health | expressly disclosed | arguably suggested | expressly disclosed | absent | absent | arguably suggested | absent | arguably suggested |
| Insertion/packing sensitivity | arguably suggested | arguably suggested | expressly disclosed | expressly disclosed | expressly disclosed | arguably suggested | arguably suggested | arguably suggested |
| Validity/confidence/abstention | arguably suggested | arguably suggested | arguably suggested | arguably suggested | absent | arguably suggested | absent | arguably suggested |
| No cloud/app/irrigation dependency | absent | expressly disclosed | absent | expressly disclosed | expressly disclosed | expressly disclosed | absent | unresolved |

**Inference:** The exact 72-run split and specific component bundle were not located in one record, but most technical functions are individually old or predictable. The chart therefore supports only a possible combination-novelty observation, not inventive step. Several “absent” cells are experimental bookkeeping or negative limitations rather than a new physical mechanism.

---

## 8. Commercial, institutional, India and China landscape

### 8.1 Commercial and institutional practice

- **DFRobot:** The official [SEN0193 page](https://wiki.dfrobot.com/sen0193) describes an analog capacitive, 3.3–5.5 V probe and supplies air/water boundary-calibration examples. This is source evidence that the chosen probe and basic calibration are commodity practice, not a novelty claim.
- **Campbell Scientific:** The official [CS655 page](https://www.campbellsci.com/products/cs655) says it derives water content, bulk EC and temperature from propagation time/attenuation/temperature, uses attenuation correction and is not probe-interchangeable. This shows both the technical importance of conductive loss and the nontriviality of transfer.
- **METER/Decagon:** METER says [TEROS 12](https://metergroup.com/products/teros-12/) uses 70 MHz capacitance technology, reduced sensor-to-sensor variability, an installation tool to minimize air gaps and a physical accuracy-verification standard/clip. These are manufacturer assertions, not patent scope, but they crowd generic “validity check”, “installation robustness” and “probe consistency” narratives.
- **Delta-T:** Delta-T says the [WET150](https://delta-t.co.uk/product/wet150-horticulture/) measures moisture, temperature and EC; its page states that individual sensors are interchangeable and advises recalibration every five years. Again, this is product practice, not a claim reading.

Commercial systems usually solve salinity either by high-frequency design, loss/attenuation correction or direct conductivity estimation. TrueMoist instead uses an experimental treatment label. That keeps cost and scope low, but it is not an equivalent technical measurement.

### 8.2 India

The TCS family is the most important Indian-origin record found: WO2021144807 claims priority to Indian provisional application 202021001465, while US12175680 and EP4090953 are granted publications. No Indian grant or current Indian claim set was established from the accessible record; the priority filing alone does not create a verified enforceable Indian patent.

For computer-related aspects, the official [Indian Patent Office CRI Guidelines available at the cut-off](https://ipindia.gov.in/storage/uploads/docs-operator/62449276-74f6-438d-92fc-14b2cf3fa204.pdf) address the Patents Act’s mathematical-method/algorithm/computer-program-per-se exclusion and emphasize the substance of the claim, specific credible technical effect/contribution, implementation and enablement. This supports careful sensor-system drafting but does not cure novelty or inventive-step weakness.

### 8.3 China

China has particularly close records on replaceable-probe reference conditioning (CN102914568), controlled temperature calibration (CN102944577), laboratory calibration (CN106248522) and recent multi-parameter nonlinear correction (CN116298198). Machine-translated claim language can change scope; official Chinese text and CNIPA status must be reviewed by qualified counsel before any China FTO or filing decision.

The official [CNIPA Patent Law](https://english.cnipa.gov.cn/col/col3068/index.html) defines novelty/inventiveness and excludes rules and methods for intellectual activities in Article 25. A physical sensor method using technical means to solve a technical measurement problem is more likely to have technical character, but eligibility is separate from novelty and inventiveness.

---

## 9. Non-patent prior art and measurement practice

### 9.1 Closest technical literature

| Source | Verified technical teaching | Effect on TrueMoist |
|---|---|---|
| Kizito et al. (2008), [Journal of Hydrology DOI](https://doi.org/10.1016/j.jhydrol.2008.01.021) | Evaluated EC-5/ECH2O-family capacitance sensors over frequency, EC and temperature; reported that frequency governs sensitivity and quantified temperature/EC effects. | Directly crowds generic temperature/salinity correction and explains why a treatment code is an incomplete proxy. |
| Chen et al. (2019), [data-driven temperature calibration](https://www.mdpi.com/1424-8220/19/20/4381) | Models FDR soil-moisture calibration while accounting for temperature. | Multivariate temperature compensation is not new in principle. |
| Bogena et al. (2017), [Effective Calibration](https://pubmed.ncbi.nlm.nih.gov/28117731/) | Calibrated more than 700 SMT100 units using five known dielectric media. | Strong prior art for unit normalization and reference-media transfer at scale. |
| González-Teruel et al. (2019), [low-cost SDI-12 sensor](https://www.mdpi.com/1424-8220/19/3/491) | Low-cost capacitive design/calibration across soils and temperature influences. | Crowds low-cost MCU calibration and cross-soil transfer narratives. |
| Kulmány et al. (2022), [SEN0193 study](https://sciendo.com/pdf/10.2478/johh-2022-0014) | Three SEN0193 units, three soil textures, thermogravimetric truth, repeatability/reproducibility and polynomial fits; unit and soil effects were substantial. | Extremely close NPL for the frozen probe, gravimetric calibration, polynomial modeling and probe variability. |
| Adla et al. (2020), [laboratory evaluation](https://www.mdpi.com/1424-8220/20/2/363) | Repacked-soil calibration of low/very-low-cost sensors with temperature/salinity considerations and absolute error reporting. | Crowds the general controlled-calibration workflow. |
| Abdelmoneim et al. (2025), [PubMed record](https://pubmed.ncbi.nlm.nih.gov/39860712/) | Twelve SEN0193 sensors, multiple replicas and GWC levels; generalized polynomial calibration and documented variability. | Particularly damaging to a broad generalized SEN0193 calibration claim; also shows two probes are too few for transfer evidence. |
| Gómez-Astorga et al. (2024), [PMC full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC11436195/) | Low-cost sensor calibration under multiple salinity/moisture levels; reported deviations up to 30% in the studied media. | Direct evidence that salinity matters and must be specifically calibrated. |
| Thelaidjia et al. (2026), [SEN0193/SEN0308 comparison](https://www.mdpi.com/2073-4441/18/12/1431) | Controlled porous-media texture and salinity comparison of two DFRobot capacitive probes. | Current pre-cut-off evidence further crowds exact low-cost-probe salinity characterization. |
| Sheshadrivasan et al. (2025), [picoSMMS](https://pmc.ncbi.nlm.nih.gov/articles/PMC12656263/) | SEN0193-based low-cost platform with calibration and environmental characterization. | Local low-cost integration and calibration remain conventional. |

**Inference:** M0/M1/M2 comparison and regularization are sensible safeguards against overfit, but the reviewed literature already uses linear, polynomial and data-driven correction. “Ridge” is a standard estimator choice. A surprising, causally tied physical effect—not a better cross-validation score alone—would be needed for a credible inventive contribution.

### 9.2 Gravimetric reference practice

The project’s dry-basis GWC approach is sound if the soil/salt mass accounting is explicit. The historical [ISO 11465:1993](https://www.iso.org/standard/20886.html) public abstract specifies drying to constant mass at 105 °C, but ISO marks that edition withdrawn and replaced by published [ISO 11465:2025](https://www.iso.org/standard/88192.html). The public page for the 2025 edition does not expose the complete test procedure, so the laboratory should consult the current standard rather than represent the withdrawn edition as current.

The [FAO gravimetric field exercise](https://www.fao.org/fileadmin/user_upload/GSP/GSDP/Field_exercises/NEW_Field_exercises/P06b-gravimetric-soil-water-EN-1-2.pdf) supports drying near 105 °C until stable mass and computing mass-basis water content. Historical [ASTM D2216-98](https://store.astm.org/d2216-98.html) warns, in substance, that dissolved salts retained after drying affect the “dry” mass; the current ASTM edition must be consulted before claiming conformity. TrueMoist must therefore record whether salt is included in dry-soil mass, maintain the same convention across all treatments and report the possible bias.

Rapid ADC samples only characterize electronic repeatability and may be averaged within a physical run. They are not independent soil samples and must not inflate (n).

---

## 10. Frozen-MVP patent assessment

### 10.1 Contribution-by-feature

| Frozen element | Engineering value | Patent assessment |
|---|---|---|
| Genuine low-cost analog probe | Ensures a reproducible target and honest cost | Commodity; no novelty. |
| Nearby DS18B20 | Measures a known disturbance near the sensing volume | Predictable sensor pairing; temperature correction is crowded. |
| Controlled salinity-treatment code | Enables a clean laboratory factor without underdesigned EC hardware | Experimental metadata, not a runtime salinity measurement; weak patent relevance. |
| ADS1115 vs calibrated ADC1 gate | Avoids assuming nominal resolution equals system accuracy | Good engineering decision; routine A/B instrumentation selection. |
| RC filtering/decoupling/perfboard | Reduces acquisition noise and wiring variation | Conventional analog hygiene unless an unexpected probe-specific mechanism is demonstrated. |
| ESP32 fixed inference | Low cost and locally deployable | Generic implementation; local processing is widely disclosed. |
| M0/M1/M2 comparison | Establishes benefit beyond raw and simple multivariate baselines | Sound model selection; linear/polynomial/ridge methods are conventional. |
| One soil/72 physical runs | Feasible factorial evidence | Exact count is not a technical mechanism; one soil limits generality. |
| Untouched replicate 3 | Protects final evaluation from tuning leakage | Strong scientific practice, not a patent contribution by itself. |
| Gravimetric GWC | Physical ground truth | Established calibration practice. |
| No cloud/irrigation/live EC | Keeps scope buildable | Negative scope limitations avoid some claims but do not create inventiveness. |

### 10.2 Core questions answered

1. **Frozen MVP credible contribution?** No credible invention established.
2. **Conventional combination?** On current evidence, yes: the functions and motivation to combine them were known.
3. **Controlled salinity patent relevance?** Mainly experimental design. It could support a later mechanism study but is not measured EC.
4. **Factorial/grouped validation patent relevance?** Evidence quality, not demonstrated inventiveness.
5. **Bounded three-month enhancement?** Health/validity pilots are feasible; credible patent evidence is not, with only two probes.
6. **Later transfer/field work?** Required for the best surviving hypothesis.
7. **Replacement/drift/insertion/uncertainty/self-validation?** Relevant problems but individually crowded; only a specific causal combination with measured effect may survive.
8. **Major redesign?** Multi-frequency/live-EC/custom-probe paths require it; not recommended within the frozen semester.
9. **Evidence and kill conditions?** Defined in Sections 18 and 22.
10. **Live claims?** Preliminary risk families identified in Sections 5, 6 and 17; counsel required for clearance.

**Track assignment for frozen MVP:** **Track D** for patent development, while remaining viable as an engineering prototype.

---

## 11. Candidate invention-direction matrix

Risk shorthand: **N** novelty; **O** inventive step/obviousness; **E** eligibility/technical character; **F** FTO. Confidence is confidence in a *credible research path*, not a probability that a patent will issue.

### 11.1 Technical contribution and test design

| ID | Problem | Proposed contribution and physical effect | Closest patent/NPL; overlap and difference | Baseline and decisive experiment |
|---|---|---|---|---|
| D1 — Level-1 compensation | Raw probe response shifts with temperature and salt treatment. | Frozen fixed M2 correction; reduces systematic GWC error inside one validated preparation domain. | Kizito, Chen, CN102944577, SEN0193 NPL and CN116298198 already combine environmental factors/calibration. Difference is exact cheap parts and treatment code, not a new mechanism. | M0 raw, M1 linear, M2 ridge; grouped replicate-3 test and ablations removing temperature or salt code. |
| D2 — probe-specific characterization | Nominally identical probes differ. | Probe-specific characterization and coefficient set; effect is lower within-unit bias. | Kulmány and Abdelmoneim expressly document SEN0193 unit variability; TCS normalizes low-cost units. Difference is the exact 72-run workflow. | Pooled coefficients vs separate probe coefficients; leave-one-probe-out testing. With two probes, report only a pilot. |
| C3 — automatic calibration transfer | Replacing a cheap probe normally requires full recalibration. | **Automatic transfer from a multi-feature physical-reference fingerprint**, not a single air/water span: use differential response, short-term noise, thermal response and recovery to decide whether a fixed map can transform an incoming unit to a population coefficient space. Physical effect: distinguish scalar offset/gain from response-shape or degradation mismatch. | CN102914568 transfers using known media/conditioning; Bogena uses reference media; TCS handles replacement; commercial verification clips check repeatability. Proposed difference is a causal multi-challenge fingerprint plus transfer-or-abstain rule for opaque commodity modules. | Full individual calibration oracle; naive coefficient reuse; DFRobot air/water two-point; scalar offset/gain; pooled model. Blinded leave-one-probe-out replacement across ≥8–12 units and ≥3 batches. |
| D4 — dual-probe disagreement | Two deployed probes can disagree. | Use disagreement as a health flag rather than averaging. Physical effect is rejection of an inconsistent channel. | TCS health monitoring, Senviro bounds and generic redundancy crowd the idea. Difference would require diagnosis tied to a physical challenge, not disagreement alone. | Single-probe, average, median and disagreement gate; independently contaminate/remount one unit while reference GWC is fixed. |
| C5 — insertion- and packing-aware compensation | Insertion depth, air gaps and packing change the sensing volume. | Measure a remount/packing signature and condition validity on it; effect is rejecting contact states outside the calibrated field. | Sentek insertion arrangement, METER installation tool and calibration literature address air gaps/contact. Difference would be a measurable electrical/physical signature using the commodity module. | Fixed jig only; no compensation; measured compaction metadata; blind remounts with standardized and perturbed packing. |
| C6 — contamination-protected drift adaptation | Drift adaptation can absorb real moisture changes or contamination. | Contamination-protected drift update permitted only during a controlled physical reference challenge and only when challenge repeatability passes. Physical effect: update sensor-state parameters without learning from unknown soil moisture. | Senviro event/history recalibration and TCS degradation monitoring are close. Difference is a locked physical-reference update window and contamination rejection. | No adaptation; unconstrained exponential update; event-only update; protected update. Cycle known references, salt fouling, thermal cycling and genuine GWC changes. |
| C7 — confidence-gated/abstaining estimate | Models can emit plausible but invalid values outside the tested domain. | Local validity envelope and abstention based on physical-factor coverage plus probe fingerprint consistency. Effect is preventing a measurement from being reported when the physical sensor state is unvalidated. | Senviro scaling/bounds, TCS performance stages and commercial verification practices crowd generic gating. Difference must be the causal probe-state test and demonstrated false-valid reduction. | Always report; range clipping; regression leverage/distance; proposed combined gate. Use deliberately unseen remount, probe, batch, temperature and salt challenges. |
| D8 | A known wetting/drying event might restore calibration. | Reference-event self-validation/bounded recalibration. | Senviro stable maxima/minima and Toro wetting/field-capacity events are very close. Exact TrueMoist event logic would be an implementation detail unless a new physical effect appears. | Fixed coefficients; event rescale; event-offset-only; repeat controlled wet/dry events and test against gravimetric truth. |
| D9 | Generic polynomial fit may overfit and extrapolate badly. | Physics-informed low-order model with monotonic water-response and bounded temperature/salt interactions. Effect: more physically plausible extrapolation. | Dielectric mixing/calibration literature and constrained regression are established. A constraint is not automatically inventive. | M1, M2 ridge, monotone/constrained model; grouped and out-of-domain tests plus term ablations. |
| C10 | A coefficient file can outlive the probe, wiring or tested physical domain. | Calibration provenance record tied to probe identifier/fingerprint, ADC path, wiring build, soil/preparation version and validity envelope; local output only when provenance matches. Physical effect: prevent use of coefficients with a physically different measurement chain. | TCS health/replacement, Senviro bounds and quality systems are close; proposed difference is automatic binding to measured hardware fingerprint, not metadata alone. | Manual label check; version hash only; fingerprint-plus-provenance gate; intentionally swap probe, ADC, cable length and coefficient set. |
| C11 | Removal/reinstallation can invalidate the original calibration. | Remount acceptance test using a standardized challenge and response fingerprint before soil output resumes. | Sentek insertion, METER verification/installation and CN reference conditioning are close. Difference is a low-cost, local remount validity decision for an opaque analog module. | Resume without test; manual visual/jig check; two-point check; multi-feature challenge. Blind repeated remounts and quantify false accept/reject. |
| C12 | A one-soil model may not transfer to another preparation batch or soil class. | Hierarchical/transfer model with explicit refusal outside represented soil descriptors. Physical effect is bounded transfer rather than universal calibration. | Kizito, González-Teruel, Kulmány and CN116298198 already address multi-soil calibration. Any contribution needs a new transfer mechanism/effect. | Soil-specific, pooled and simple texture-feature models; later ≥2 batches and ≥3 soils with leave-one-soil-out tests. |
| C13 | Aging may change response in ways a new-unit map cannot correct. | Lifecycle state fingerprint that separates recoverable offset/gain drift from non-transferable shape/noise/hysteresis damage and commands recalibration/replacement/abstention. | TCS degradation stages, Senviro aging and commercial recalibration/verification are close. Difference is non-optical causal classification plus measured transfer consequence. | Time-only replacement; raw drift threshold; TCS-like value statistics; proposed fingerprint. Thermal/salt/wet-dry cycles plus blinded endpoint calibration. |
| D14 | ADC/wiring changes may be mistaken for probe drift. | Acquisition-path fingerprint/normalization using paired ADC1/ADS1115 response. Effect is traceable separation of electronics variation from probe variation. | Reference circuits, ADC calibration and ordinary metrology make this predictable. The project’s paired gate is valuable but not a credible invention alone. | ADC1 vs ADS1115, direct vs hardened wiring, paired same-node readings; analyze noise/drift/RMSE. |
| D15 | Moisture and ionic loss are confounded. | Multi-frequency separation. | US7884620, US5418466, US11415612, Delta-T/METER art and Kizito directly occupy this mechanism. Frozen commodity probe does not expose frequency control. | Single analog probe vs purpose-built dual/multi-frequency prototype; outside present experiment. |
| D16 | A treatment code cannot represent unknown field salinity. | Live-EC-assisted compensation. | Green Badge, METER/Delta-T, Campbell and CN116298198 directly measure conductivity or loss. Credible implementation needs excitation, cell constant, polarization and temperature correction. | Treatment-code M2 vs measured-EC model with calibrated reference instrument; outside frozen MVP. |

### 11.2 Execution, risk and disposition

| ID | Required changes; cost | Three-month feasibility and later work | N/O/E/F risks | Confidence; kill condition | Track |
|---|---|---|---|---|---|
| D1 | No architecture change; within ₹1,790–₹3,440 plan | Fully feasible now | N high; O very high; E low/medium if tied to sensor but generic algorithm risk; F low/moderate preliminary | High confidence it is buildable, low patent confidence; kill patent path if only expected regression gain appears | D |
| D2 | Per-unit labels/calibration; no material added cost | Two-unit characterization feasible; population claim requires many more units | N high; O high; E low; F low/moderate | Low; kill if between-unit effect is negligible or full calibration remains necessary | D |
| C3 | Pilot can reuse rig; rigorous study needs ≥8–12 genuine probes, reference fixtures and more batches; later cost must be quoted and is not supported within current ₹5,000 ceiling | Two-probe pilot only in semester; blinded population study later | N medium/high due CN/Bogena; O high; E low if physical; F medium in CN/US/EP depending fixture | Low–medium; kill if transfer is not materially better than scalar normalization or cannot detect non-transferable units | C |
| D4 | Firmware flag; ₹0 incremental | Feasible pilot; many fault modes later | N high; O very high; E low; F low/moderate | Low; kill if disagreement cannot identify which unit is wrong without reference | D |
| C5 | Add controlled perturbations; jig materials already ₹200–₹450 line | Pilot feasible; robust remount claim needs many remounts/units/batches later | N medium/high; O high; E low; F medium due insertion/fixture art | Low; kill if no signature predicts remount error beyond packing metadata | C |
| C6 | Reference-challenge schedule and locked update logic; pilot consumables within plan | Accelerated aging evidence exceeds ordinary 72-run plan; later work required | N medium/high; O high; E low if technically tied; F medium | Low; kill if update corrupts valid calibration or contamination passes the gate | C |
| C7 | Fixed local gate; negligible compute/cost | Feasible as engineering extension; credible patent evidence requires unseen physical challenges and more units | N medium/high; O high; E medium for a pure statistical gate; F low/moderate | Low–medium; kill if false-valid rate remains high or valid coverage collapses | C |
| D8 | Controlled reference events; small consumables | Feasible, but prior art is close | N very high; O very high; E low; F medium depending event/claim | Low; kill absent an unexpected physical mechanism | D |
| D9 | Python/firmware only; ₹0 incremental | Feasible | N high; O very high; E medium; F low | Low; kill if only modest metric gain without technical effect | D |
| C10 | Provenance schema, hashes and fingerprint gate; ₹0–₹200 for fixtures/labels within current contingency | Feasible pilot; population validity evidence later | N medium; O high; E low if physical mismatch changes operation, high if metadata only; F low/moderate | Medium relative to other candidates; kill if hash/manual checks perform equivalently or fingerprint adds no error protection | C |
| C11 | Reference challenge plus remount protocol; use existing jig initially | Limited pilot feasible; ≥3 remounts/unit/condition over many units later | N medium/high; O high; E low; F medium | Low–medium; kill if challenge result does not predict in-soil remount error | C |
| C12 | New soils/classes and measurements; cost unavailable and outside freeze | Not credible within frozen 72 runs; later semester/publication | N high; O high; E low; F medium | Low; kill if transfer is no better than soil-specific calibration | C |
| C13 | Aging fixtures/cycles and more probes; later cost unavailable | Not credible in three months without accelerated-aging validity; later work | N medium/high; O high; E low; F medium/high near TCS | Low; kill if accelerated states do not correspond to real degradation or categories are unstable | C |
| D14 | Existing ADC gate/AFE; no extra cost | Fully feasible | N high; O very high; E low; F low | Low; kill as patent path regardless of modest benefit absent a new circuit effect | D |
| D15 | New frequency-controlled probe/electronics; cost and schedule unavailable, likely scope-breaking | Not feasible under frozen semester | N high; O very high; E low; F high | Very low connected-path confidence; kill for this project scope | D |
| D16 | Calibrated EC channel/reference solutions and redesigned AFE; cost/schedule unavailable | Not feasible without major redesign | N high; O very high; E low; F high | Very low connected-path confidence; kill for frozen scope | D |

**Matrix conclusion:** No Track-A candidate and no sufficiently evidenced Track-B invention were found. C3, C10, C11 and C13 form one connected Track-C research program. They must not be represented as four separate inventions or as presently patentable subject matter.

---

## 12. Strongest surviving direction

### Mechanism-tied calibration-validity envelope with replacement/remount transfer

**Recommendation:** After completing the frozen MVP, investigate a provisioning/verification method for opaque low-cost analog probes that:

1. exposes each probe to a reproducible sequence of at least two physically known dielectric/contact states and a controlled thermal transition;
2. derives a response fingerprint containing differential gain/shape, short-term noise, thermal response and recovery—not merely one dry/wet scalar span;
3. compares that fingerprint with a population validity envelope tied to the exact ADC/wiring build and calibration provenance;
4. either maps the incoming/reinstalled probe to a fixed coefficient space, requests full recalibration, or locally abstains;
5. repeats the check after replacement, remounting or a scheduled/triggered health event; and
6. never updates from unknown soil moisture, thereby preventing contamination of the calibration state.

**Proposed physical effect:** reduce erroneous GWC reports caused by using coefficients with a physically mismatched probe/remount state, while identifying cases in which offset/gain transfer is insufficient because response shape, noise, thermal behavior or hysteresis changed.

**Why it is the strongest:** it addresses the project’s actual weakest link—unit/remount validity—without adding live EC, custom frequencies, cloud control or online learning. It also produces an observable device action (accept/transfer/recalibrate/abstain) tied to measured physical challenges.

**Why it is not yet a credible patent:** CN102914568, Bogena, Senviro, TCS, Deere and commercial verification practice collectively occupy much of the problem and solution space. No unexpected transfer effect has been measured. Two probes cannot define a population envelope, estimate false acceptance or demonstrate replacement generality. The direction therefore remains a **Track-C hypothesis** and must undergo another focused claim/status search after the mechanism and data exist.

### Minimum later evidence package

- at least 8–12 genuine probes from documented lots, with the final number determined by a pre-specified power/precision analysis;
- at least three independent preparation batches and at least three blinded remounts per relevant condition;
- a fully calibrated per-probe oracle, naive reuse, air/water two-point, scalar offset/gain and pooled-model baselines;
- induced but documented thermal, salinity exposure, contamination and wet/dry cycling, plus an unaged control;
- blinded probe replacement and coefficient swapping;
- transfer error, remount error, bias, repeatability, valid/reject rate, false-valid rate, false invalidation and detection delay;
- ablations removing each fingerprint component and the provenance binding;
- official-register/counsel review of CN102914568, TCS US/EP claims, relevant METER/Deere/Senviro families and any new continuations.

---

## 13. Level-1 compensation versus Level-2 robustness/transfer

| Dimension | Level 1 — frozen compensation | Level 2 — proposed robustness/transfer research |
|---|---|---|
| Technical question | Can temperature and known treatment labels reduce error for two probes in one preparation? | Is a new/reinstalled/aged probe physically compatible with an existing calibration, and can invalid use be prevented? |
| Inputs | Raw response, measured temperature, assigned salt-treatment code | Physical-reference response vector, thermal/recovery/noise features, probe/ADC/wiring provenance, plus Level-1 inputs after acceptance |
| Learning | Offline M0/M1/M2; fixed coefficients | Offline population envelope/transfer rule; fixed local decision logic; no learning from unknown soil |
| Validation unit | Independent physical condition run | Probe unit, lot, preparation batch, remount and lifecycle state |
| Main output | GWC estimate | Accept/transfer/recalibrate/abstain, then GWC if valid |
| Core baseline | Univariate raw mapping | Full individual calibration, naive reuse, two-point span, scalar normalization and pooled model |
| Evidence feasible now | 72-run one-soil test | Only a two-probe feasibility pilot |
| Patent posture | Track D; crowded combination | Track C; potentially technical but unproven and crowded |

Level 1 should be completed even if Level 2 is never patented: it establishes whether the inexpensive probe is useful under controlled conditions. Level 2 should not alter the 72-run sample definition or be used to rescue a failed Level-1 engineering result.

---

## 14. Novelty

Under the U.S. framework, novelty is distinct from obviousness; [35 U.S.C. §102](https://uscode.house.gov/view.xhtml?req=%28title%3A35+section%3A102+edition%3Aprelim%29) is the statutory novelty provision. Other jurisdictions apply their own claim-by-claim tests.

**Search observation:** No single reviewed independent claim was found that expressly combines every frozen element: SEN0193-class analog module, a separate nearby DS18B20, a known salt-per-dry-mass code with no live EC, the ADS1115/ADC1 gate, exact AFE hardening, ESP32 fixed M0/M1/M2 inference, one soil, 72 physical grouped runs and dry-basis GWC.

**Not a novelty opinion:**

- A patent claim would not sensibly recite every procurement and validation detail.
- Negative limitations such as “no cloud” or “no live EC” may not distinguish a claim unless supported and technically meaningful.
- A 72-run count and split may be a test protocol, not an apparatus/method limitation that changes sensor operation.
- Unreviewed languages, claims, continuations, non-patent disclosures and earlier public uses can anticipate.
- A broad claim to fixed temperature/salt correction is vulnerable to individual references such as CN102944577, Kizito/Chen and multivariate-correction art.

**Preliminary conclusion:** exact-combination novelty is unresolved and may be arguable only for an artificially narrow claim; meaningful technical novelty in the frozen MVP was not established. The Track-C fingerprint/validity combination also has unresolved novelty because its concrete fingerprint and decision sequence do not yet exist.

---

## 15. Inventive step/obviousness

[35 U.S.C. §103](https://uscode.house.gov/view.xhtml?req=%28title%3A35+section%3A103+edition%3Aprelim%29) addresses U.S. non-obviousness. The EPO’s problem-solution approach similarly asks for the objective technical problem and technical contribution; see the [EPO Guidelines](https://www.epo.org/en/legal/guidelines-epc/2026/g_vii_5_2.html).

### 15.1 Frozen MVP

The likely combination rationale is straightforward:

1. select a known low-cost capacitive probe whose output depends on water and is affected by unit, soil, temperature and conductivity;
2. co-measure temperature and label controlled salt treatments because those are known confounders;
3. use ordinary ADC conditioning and local MCU acquisition;
4. fit linear/polynomial regression against a standard gravimetric reference;
5. validate on held-out physical samples.

Kizito/Chen/CN102944577 supply the motivation for temperature and salinity/conductivity characterization; Kulmány/Abdelmoneim and other SEN0193 work supply sensor-specific gravimetric polynomial calibration and unit variability; basic MCU/ADC and fixed-coefficient deployment are conventional. The expected result—lower in-domain error after modeling measured/assigned confounders—is predictable. Ridge regularization, factorial balance and a held-out replicate improve rigor but do not, without more, create an unexpected technical effect.

**Conclusion:** inventive-step/obviousness risk is **very high** for the frozen MVP.

### 15.2 Strongest Track-C direction

The objective technical problem would be narrower: prevent application of a calibration to a physically incompatible replacement/remount state of an opaque low-cost analog probe without performing a full soil calibration.

The proposed fingerprint is still vulnerable to a combination of CN102914568 (replacement/reference conditioning), Bogena (multi-medium unit calibration), Senviro (history/validity), TCS (low-cost health/replacement) and standard anomaly/uncertainty gating. To improve the inventive-step case, experiments must show that a specifically chosen response vector separates transferable from non-transferable states better than expected scalar normalization, and that the resulting local action prevents a measurable sensor error. Merely concatenating more features or applying a classifier would be weak.

**Conclusion:** current obviousness risk is **high**; it may fall only if a specific causal mechanism and surprising effect are demonstrated.

---

## 16. Patent eligibility

Eligibility is a threshold question, not a substitute for novelty, inventive step or enablement.

### United States

The [USPTO MPEP §2106](https://www.uspto.gov/web/offices/pac/mpep/s2106.html) explains that mathematical relationships/abstract ideas must be integrated into a practical application or accompanied by significantly more, and separately reminds examiners to apply §§102, 103 and 112. A concrete sensor method that acquires physical signals and changes whether/how a measurement is reported has a plausible machine/process character. A claim only to fitting ridge coefficients, computing confidence or selecting a model on a generic ESP32 has **medium-to-high §101 risk**. Eligibility risk is lower for the mechanism-tied physical challenge and local accept/abstain operation, but §§102/103 remain the larger obstacles.

### European Patent Office

The [2026 EPO mathematical-method guidance](https://www.epo.org/en/legal/guidelines-epc/2026/g_ii_3_3.html) states that a mathematical method can contribute when it produces a technical effect serving a specific technical purpose and is causally linked to that effect; indirect determination of a physical state from physical measurements can make a technical contribution. The [AI/ML guidance](https://www.epo.org/en/legal/guidelines-epc/2026/g_ii_3_3_1.html) says assertions alone are insufficient and relevant dataset characteristics must be disclosed when needed to reproduce the effect. Frozen regression may have technical character as a measurement, but only features contributing to a demonstrated technical effect help inventive step. Dataset size and ridge selection alone are weak.

### India

The official [CRI Guidelines](https://ipindia.gov.in/storage/uploads/docs-operator/62449276-74f6-438d-92fc-14b2cf3fa204.pdf) address the Section 3(k) exclusion for mathematical methods, algorithms and computer programs per se and focus on substance, implementation and a specific credible technical effect/contribution. A claimed physical measurement chain with a concrete validity operation is stronger than a coefficient file or algorithm alone. No novel-hardware requirement should be assumed, but neither generic hardware nor an “IoT/AI” label establishes eligibility. The exact current statute, case law and final claim must be reviewed by Indian counsel.

### China

The [CNIPA Patent Law](https://english.cnipa.gov.cn/col/col3068/index.html) excludes rules and methods for intellectual activities, while requiring novelty, inventiveness and practical use. A sensor system using technical means to solve a physical measurement problem and produce a technical effect is more likely to clear subject-matter character than an abstract formula. Machine-translation and current examination guidance must be checked before filing.

### Eligibility conclusion

The system can likely be framed as technical in all four regimes if the claim is limited to physical acquisition and a concrete sensor operation. That does **not** cure the current novelty/obviousness problem. Claiming the algorithm at a high level would increase eligibility and enablement risk while also broadening the prior-art exposure.

---

## 17. Freedom to operate

### 17.1 Preliminary claim-screen result

No obvious literal read of the analyzed independent claims was found on the frozen MVP because the closest live-indicator families require limitations the MVP lacks: TCS image analysis; Damoatech matched resonance circuits and probe geometry; Green Badge dual-frequency/live-salinity/wireless circuitry; Fiskars series-RLC sensing; METER complex-admittance reference impedances; Morph2O custom conductor/wireless-control architecture.

This is a **screen, not clearance**. It does not address doctrine of equivalents, every dependent claim, continuations/divisionals, supplier-probe internals, assignments, national validation, translations, unindexed rights or claims outside the reviewed jurisdictions.

### 17.2 Family-specific watch list

| If TrueMoist adds… | Re-screen at minimum… | Why |
|---|---|---|
| Optical health/degradation or automatic replace recommendation | US12175680 and EP4090953, plus national validations | Independent claims require a detailed image-health chain; nearby additions could move toward them. |
| Known-medium replacement conditioning | CN102914568 and family/current CNIPA status | Close purpose and claim sequence in China. |
| Dual/multi-frequency or live salinity | US7884620 family, US5418466, METER/Delta-T families | Active-indicator and historical claims cover specific separation circuits. |
| Custom MCU-driven RLC probe | US9804113/EP3145292 family | Central independent-claim architecture. |
| Complex impedance/admittance | US11415612 and US7944220 families | Specific reference-impedance/amplitude/phase structures. |
| Physical reference fixture | Deere fixture family, CN102914568 and related calibration fixtures | Reference apparatus/conditioning claims must be mapped. |
| Event/history adaptation | Senviro/Toro and later continuations | Even dead cases remain prior art; current rights must be checked. |

### 17.3 Jurisdiction/status limits

- **United States:** verify Patent Center transaction history, terminal disclaimers, maintenance fees and continuations for every live-indicator family; the [USPTO maintenance-fee portal](https://fees.uspto.gov/MaintenanceFees/) is an official source.
- **Europe:** verify EP register, opposition status and each validated national designation; an EP B1 publication is not one unitary enforceability result across all countries.
- **India:** run InPASS and prosecution-file review for the TCS priority application and relevant Indian filings. No Indian FTO conclusion is made here.
- **China:** obtain official Chinese claims/status and professional translation for CN102914568, CN102944577, CN116298198 and any cited continuations.

Research or educational use is not assumed to create a universal infringement exemption. Experimental-use rules are jurisdiction-specific and narrow in some countries. Procurement of a genuine supplier probe may shift some manufacturing risk but does not automatically license every system or method combination.

**Preliminary FTO posture:** frozen MVP **low-to-moderate identified literal-claim risk**, but overall FTO **unresolved** and unsuitable for commercialization without counsel.

---

## 18. Claim-to-experiment map

This section does not propose filing claims now. It maps the strongest research hypothesis to evidence that could support or kill a later claim concept.

| Hypothetical technical element | Required experiment | Baseline/ablation | Required metric | Proposed owner-approved threshold before testing |
|---|---|---|---|---|
| Commodity analog probe is represented by a reproducible physical-reference fingerprint | Repeat reference sequence across units, days, power cycles and operators | Single reading; air/water span; remove thermal/recovery/noise features | Within-unit repeatability; between-unit separation; fingerprint stability | Within-unit fingerprint variation materially below between-unit/induced-state separation; exact bound set after pilot and locked |
| Fingerprint identifies whether scalar transfer is physically valid | Blind replacement units and induced offset/shape/noise faults | Naive reuse; scalar offset/gain; pooled model | False-valid, false invalidation, transfer RMSE/MAE and bias | **Proposed:** false-valid ≤5% for predeclared harmful states; owner approval required |
| Transfer reduces calibration burden without losing material accuracy | Compare transferred coefficients with full individual-calibration oracle | Full oracle; naive reuse; DFRobot two-point; pooled model | Transfer RMSE ratio and preparation effort | **Proposed:** RMSE no worse than 1.25× oracle and ≥30% lower than naive reuse; owner approval required |
| Provenance binding prevents wrong-chain coefficient use | Swap probe, ADC, cable/wiring and coefficient files blindly | Manual labels; hash-only check | Prevented erroneous reports; false rejection | **Proposed:** detect 100% of intentional identity/configuration swaps in test set; owner approval required |
| Remount challenge predicts in-soil remount error | ≥3 blind remounts per unit/condition with controlled contact perturbations | No check; jig only; two-point check | Remount error, false accept/reject | **Proposed:** ≥25% median remount-error reduction versus no check; owner approval required |
| Gate abstains outside validated physical domain | Unseen probe, batch, remount, temperature and salt challenges | Always report; range clip; leverage/distance-only gate | Valid/reject rate, coverage, false-valid, subset RMSE | **Proposed:** valid-report rate ≥70% within declared domain and false-valid ≤5% on harmful OOD set; owner approval required |
| Protected drift update does not learn real moisture change | Interleave known-reference windows, actual GWC changes and contamination | No update; unconstrained update; event update | Drift-detection delay, calibration error, false update | **Proposed:** false update ≤5% and detection within two scheduled challenge cycles; owner approval required |
| Each allegedly inventive component is causal | Remove one fingerprint component, provenance binding, physical gate and abstention action in turn | Full candidate | Change in false-valid and transfer/remount error with uncertainty | Each retained element must have a predeclared material contribution; no post-hoc claim selection |

The project’s existing engineering thresholds remain unchanged: on untouched replicate 3, compensated RMSE must be at least 20% lower and MAE at least 15% lower than the uncompensated baseline, with no more than 10% MAE worsening in a major disturbance subset. The proposed patent-oriented thresholds above are **not approved project requirements** until the owner approves them before data collection.

Statistical unit discipline:

- one prepared/equilibrated/measured soil condition is one physical run;
- ADC samples nested inside that run quantify acquisition noise only;
- probe, remount and preparation batch must be grouped factors;
- confidence intervals should be by physical run/probe group, not by raw ADC sample;
- all thresholds, exclusions and ablations must be preregistered or time-stamped before the blinded test.

---

## 19. Three-month semester plan

The semester plan preserves the validated architecture and does not pretend the two-probe extension proves transfer patentability.

| Week | Work and gate | Output/decision |
|---:|---|---|
| 0 | Confidentiality/IPR briefing; assign IDs; freeze BOM, schema, salt convention and randomization; confirm no prior public disclosure | Signed access/contributor record; dated protocol; private repository |
| 1 | Incoming inspection of two genuine probes; paired same-node ADS1115 vs calibrated ADC1; verify DS18B20, 0.01 g scale and institutional oven access | U-TM-01/U-TM-02 decisions; retain ADS1115 only on documented value/clean reproducibility |
| 2 | Packing/insertion jig pilot; salinity recipe and dry-mass accounting; drying-to-constant-mass trial; estimate 72-run throughput | Stop/rework if packing equals/exceeds intended disturbance, reference access fails or schedule cannot support physical runs |
| 3 | Finalize containers, fixed wiring/connectors/grounding and perfboard; lock CSV metadata and sample labels | Measurement-chain version and provenance record |
| 4–7 | Execute randomized/blocked 4×3×2×3 physical runs; equilibrate, measure, dry, reweigh and QC each run | 72-run raw/reference dataset; ADC repeats nested, never inflated |
| 8 | Lock replicates 1–2; fit M0/M1/M2; grouped model selection; perform temperature/salt/interaction ablations | Frozen coefficients and pre-test report |
| 9 | Deploy fixed coefficients to ESP32; verify embedded/offline numeric equivalence and resource use | Reproducible firmware and coefficient manifest |
| 10 | Run untouched replicate-3 analysis exactly once; report RMSE, MAE, bias, absolute errors and disturbance subsets | Engineering pass/fail on 20%/15% thresholds |
| 11 | Limited exploratory two-probe remount/fingerprint pilot without changing the frozen result | Feasibility data explicitly labelled insufficient for population transfer/patent claim |
| 12 | Reproduce dataset/analysis; update risk register; institutional IPR review before any public demo; decide later study | Engineering report and Track-C go/no-go brief |

If the documented 72-run throughput fails, use only a formally authorized fallback from the project register; do not manufacture independence from repeated reads. Model complexity is the first scope to reduce, not physical reference integrity.

---

## 20. Later-semester/publication extension

Proceed only if the frozen MVP meets its engineering thresholds and the two-probe pilot shows a stable, physically interpretable fingerprint.

### Stage 1 — population and remount study

- procure/document ≥8–12 genuine probes across lots after a power/precision analysis;
- use ≥3 independent soil-preparation batches;
- conduct ≥3 blinded remounts per selected condition;
- develop a reproducible external reference-challenge fixture without copying a protected claim sequence;
- lock baselines, thresholds and failure-state definitions before the blind test.

### Stage 2 — lifecycle/contamination study

- wet/dry, salt exposure and thermal cycles with unaged controls;
- characterize offset, gain, curvature, noise, hysteresis and recovery;
- test protected updates only in known reference windows;
- distinguish reversible transfer from required full recalibration/replacement.

### Stage 3 — bounded transfer

- add a second preparation batch first, then one additional soil class only as a clearly labelled extension;
- do leave-one-probe, leave-one-batch and later leave-one-soil-out tests;
- report failures and abstentions, not only accepted estimates.

### IP/publication sequence

1. institutional invention disclosure with raw evidence and named contributors;
2. focused updated prior-art/register/counsel review of the concrete mechanism;
3. filing decision, if any;
4. only then submit a paper, release code/data or publicly demonstrate the new mechanism/results.

A good publication remains possible even if the patent hypothesis dies: a careful negative or bounded study of commodity-probe compensation, unit variability, salinity-treatment limitations and grouped physical validation would still be valuable.

---

## 21. Budget, measurement, compute and team feasibility

### 21.1 Frozen semester

**Verified project planning range:** approximately ₹1,790–₹3,440, preferred ≤₹3,000 and absolute ceiling ₹5,000, assuming institutional oven access. The architecture lists ESP32 ₹450–₹700, ADS1115 ₹120–₹220, two probes ₹300–₹600, DS18B20 ₹120–₹220, perfboard/wiring/passives ₹250–₹450, containers/jig ₹200–₹450, consumables ₹100–₹300, optional 0.01 g scale ₹400–₹700 and contingency ₹250–₹500. Purchasing a laboratory oven is outside scope.

**Measurement gates:**

- verified institutional drying access, at least 24 h and constant mass;
- salt-addition convention fixed relative to dry soil and consistently reflected in GWC calculation;
- same probe depth, orientation, spacing and thermal-sensor placement;
- fixed soil mass, fill height and compaction method;
- paired same-node ADC comparison; ADS1115 retained for measured value or documented reproducibility, not nominal bit count;
- final soldered analog path and fixed connectors;
- no VWC claim without bulk density.

**Compute:** project estimates are below 2 kB for acquisition buffers, below 2 kB for CSV/metadata buffers and below 100 floating-point operations per record. M0/M1/M2 and a fixed validity gate are trivial for ESP32. Experimental time, sample consistency and reference quality—not RAM or compute—are the bottlenecks.

### 21.2 Team of five

| Role | Primary responsibility | Required cross-check |
|---|---|---|
| Embedded lead | ESP32, ADC/temperature drivers, filtering, coefficients, CSV and embedded equivalence | Hardware lead witnesses paired ADC and wiring-version tests |
| Data/model lead | Schema, grouped split, M0/M1/M2, metrics, ablations, coefficient export | Another technical member reruns environment-locked analysis |
| Hardware/validation lead | Probe characterization, AFE, jig, ADC gate and measurement hygiene | Data lead audits sample IDs and exclusion reasons |
| Learner/support | Labels, temperature log, CSV checks and supervised sample preparation | No unsupervised critical mass/salt or ground-truth decisions |
| Documentation/presentation | Logbook, photographs, BOM, risk register, traceability and demo narrative | Maintains confidentiality and contribution/disclosure records |

### 21.3 Track-C cost boundary

A rigorous population/remount/aging study needs additional genuine probes, fixtures, batches and elapsed laboratory time. The current project record provides no defensible later-study amount. Obtain written local quotes and a statistical sample-size plan. Do **not** imply that the full Track-C evidence package fits the ₹5,000 frozen-MVP ceiling. A two-probe pilot can use the current rig, but it cannot support general replacement-transfer claims.

---

## 22. Kill criteria

### 22.1 Engineering kill/rework criteria

- genuine probe repeatability is too poor to resolve moisture levels;
- packing/insertion variance equals or exceeds the temperature/salt effect after the jig pilot;
- institutional oven/scale access cannot sustain constant-mass reference work;
- controlled salinity preparation is not homogeneous/reproducible or its dry-mass convention is ambiguous;
- measured throughput cannot support the authorized physical-run design;
- compensated replicate-3 RMSE improvement is <20% or MAE improvement is <15%;
- any major tested subset worsens MAE by >10% without a defensible safety/validity rule;
- improvement disappears when ADC samples are correctly nested by physical run or when replicate 3 remains untouched;
- cost exceeds ₹5,000 or scope requires live EC, custom frequency hardware, cloud, irrigation or multiple soils.

An ADS1115 that adds no useful noise/drift/RMSE/reproducibility benefit is **not** a project kill: use calibrated ADC1 or retain ADS1115 only for a documented reproducibility reason.

### 22.2 Patent-selection kill criteria

- an official-register/counsel search finds a live claim that reads on the proposed implementation and cannot be safely designed around;
- the only distinction is ESP32, ADS1115, DS18B20, low cost, ridge regression, exact factor count or the absence of cloud/live EC;
- the strongest effect is merely a better cross-validation score with no causal physical sensor operation;
- scalar two-point normalization, pooled calibration or a manual provenance check performs equivalently to the proposed fingerprint;
- transfer requires full per-probe soil calibration, eliminating the claimed technical benefit;
- false-valid rate or false invalidation misses the pre-approved threshold, or the gate rejects so much in-domain data that it is not useful;
- remount challenge does not predict actual in-soil remount error;
- protected adaptation learns genuine moisture change or contamination passes as valid drift;
- the result holds for only the two original probes or one preparation batch;
- the path requires live EC, multi-frequency hardware or multi-soil scope merely to escape prior art;
- the proposed mechanism cannot be fully disclosed/reproduced without retaining essential steps as a trade secret;
- no credible claim remains after updated novelty/obviousness and enablement review.

Passing an engineering threshold is never, by itself, a patent pass.

---

## 23. Confidentiality boundary

Until institutional IPR review:

- keep any new fingerprint, transfer rule, validity envelope, fixtures, thresholds, datasets and results in access-controlled storage;
- do not post source, preprints, datasets, videos, posters or detailed public demos of the new mechanism;
- use dated, versioned invention records; list actual contributors and have each review the record;
- preserve raw ADC/temperature/mass metadata, exclusions, calibration certificates and file hashes;
- record probe supplier/lot, wiring/ADC build, salt recipe, preparation batch and operator;
- make the institutional invention disclosure before publication or competition disclosure;
- ask institutional counsel about ownership, student/institution obligations and any already-made disclosure.

The existence of the public prior art and commodity hardware is not confidential. The potentially protectable subject, if any, would be the later concrete mechanism and evidence. Confidentiality does not make an obvious idea patentable, but premature disclosure can destroy options in many jurisdictions. No grace period should be assumed.

---

## 24. Final recommendation

**Retain as strong semester prototype but reduce patent priority**

Build and evaluate the validated 72-run TrueMoist MVP because it is affordable, technically coherent and capable of producing credible engineering evidence. Do not present its fixed temperature/salinity-code regression, component combination or validation design as a current patent contribution. Preserve a separate Track-C research option for mechanism-tied calibration validity and replacement/remount transfer, contingent on a larger probe population, blinded physical tests, an unexpected technical effect and renewed official-register/counsel review.

---

## 25. Unresolved questions

1. What are the official current transaction, maintenance/opposition and national-validation states of each live-indicator US/EP family?
2. Does Indian application 202021001465 or a related complete application have published or granted Indian claims, and what is its current InPASS status?
3. What is the authoritative CNIPA status and professional translation of CN102914568, CN102944577 and CN116298198?
4. Are there unpublished applications, continuations or recent pre-cut-off publications not retrieved by the search interfaces?
5. Does the purchased SEN0193 supplier module internally practice any still-live circuit claim, and what rights accompany authorized sale?
6. Has any team member already publicly disclosed the architecture, new mechanism, dataset or result?
7. What institution owns student-generated IP, and who are the legally correct inventors/contributors?
8. Is the 105 ± 5 °C/constant-mass procedure aligned with the laboratory’s current ISO/ASTM method, especially for salt-treated soil?
9. Is salt added per mass of untreated dry soil or final dry solids, and how is retained salt handled in GWC bias/uncertainty?
10. Do the two genuine probes show a resolvable unit fingerprint after controlling power, ADC, wiring, insertion and packing?
11. Which physical reference challenges are reproducible, safe for the probe coating and sufficiently distinct from CN/Deere claimed fixtures?
12. What probe count is justified by a pre-specified false-valid/transfer-error precision analysis?
13. Are accelerated thermal/salt/wet-dry states representative of real aging rather than artificial damage?
14. What patent-oriented thresholds will the owner approve before blinded testing?
15. Can provenance/fingerprint gating beat manual identity checks and simple two-point normalization by a material amount?
16. Can the 72 physical runs be completed without using the 54-run fallback or compromising equilibration/drying?

---

## 26. Source and verification log

### 26.1 Patent and register sources

| Source checked 2026-08-02 | Use | Verification level / limitation |
|---|---|---|
| [US12175680B2](https://patents.google.com/patent/US12175680B2/en), [WO2021144807A1](https://patents.google.com/patent/WO2021144807A1/en), [EP4090953B1](https://patents.google.com/patent/EP4090953B1/en) | TCS low-cost sensor health family; independent claims, priority/family/grant publications | Claim/publication text verified; Google current status provisional; Indian right unresolved |
| [CN102914568B](https://patents.google.com/patent/CN102914568B/en) | Replaceable probe and known-reference conditioning | Translated claim and grant publication verified; translation and live status unresolved officially |
| [US20080199359A1](https://patents.google.com/patent/US20080199359A1/en) | Senviro event/history calibration, bounds, aging/contact | Publication verified; abandoned indicator provisional; family status unresolved |
| [US9146206B2](https://patents.google.com/patent/US9146206B2/en); [official EPO publication PDF](https://data.epo.org/publication-server/rest/v1.0/publication-dates/20130807/patents/EP2623971NWA1/document.pdf) | Deere fixture/reference calibration | US claim discovery plus official EP publication; current rights require registers |
| [CN102944577A](https://patents.google.com/patent/CN102944577A/en) | Moisture-by-temperature calibration fixture/procedure | Publication/disclosure verified; “pending” rejected as load-bearing status |
| [US11598743B2](https://patents.google.com/patent/US11598743B2/en) | Resonance-reference probe and temperature dependent claims | US grant/claims verified; status provisional |
| [US7884620B2](https://patents.google.com/patent/US7884620B2/en) | Dual-frequency moisture/salinity and wireless output | US grant/claims verified; status provisional |
| [US9804113B2](https://patents.google.com/patent/US9804113B2/en) | MCU-driven series-RLC capacitive probe | US grant/claims verified; family/status provisional |
| [US11415612B2](https://patents.google.com/patent/US11415612B2/en) | METER complex dielectric/admittance structure | US grant/claims verified; status provisional |
| [US7944220B2](https://patents.google.com/patent/US7944220B2/en) | Delta-T complex impedance/amplitude/phase | Publication reviewed; status provisional |
| [US7240743B2](https://patents.google.com/patent/US7240743B2/en) | Sentek insertion/contact arrangement | Publication reviewed; expiry provisional |
| [US9949450B2](https://patents.google.com/patent/US9949450B2/en) | Custom probe, temperature and wireless/irrigation context | Publication/claims reviewed; fee status provisional |
| [CN116298198A](https://patents.google.com/patent/CN116298198A/en) | Recent Chinese multi-parameter nonlinear correction | Publication reviewed; claims/status require official translation/register |
| [USPTO filing-status guidance](https://www.uspto.gov/patents/apply/checking-application-status/check-filing-status-your-patent-application), [Patent Public Search](https://www.uspto.gov/patents/search/patent-public-search), [maintenance fees](https://fees.uspto.gov/MaintenanceFees/) | Official mechanisms for follow-up | Dynamic case records not successfully extracted; listed as required follow-up, not substituted |
| [EPO patent search](https://www.epo.org/en/searching-for-patents) | Official European follow-up mechanism | National validation/opposition not resolved in this report |

### 26.2 Technical, commercial and measurement sources

| Source | Use | Source type |
|---|---|---|
| [Kizito et al., 2008](https://doi.org/10.1016/j.jhydrol.2008.01.021) | Frequency, EC and temperature effects in low-cost capacitance sensing | Primary journal article |
| [Chen et al., 2019](https://www.mdpi.com/1424-8220/19/20/4381) | Data-driven temperature calibration | Primary journal article |
| [Bogena et al., 2017](https://pubmed.ncbi.nlm.nih.gov/28117731/) | >700 units and five reference media | Primary article/index record |
| [González-Teruel et al., 2019](https://www.mdpi.com/1424-8220/19/3/491) | Low-cost SDI-12 calibration and soil/temperature context | Primary journal article |
| [Kulmány et al., 2022](https://sciendo.com/pdf/10.2478/johh-2022-0014) | SEN0193 units, soils, gravimetric truth, polynomial and R&R | Primary open PDF |
| [Adla et al., 2020](https://www.mdpi.com/1424-8220/20/2/363) | Controlled laboratory evaluation | Primary journal article |
| [Abdelmoneim et al., 2025](https://pubmed.ncbi.nlm.nih.gov/39860712/) | Twelve SEN0193 units/generalized calibration | Primary article/index record |
| [Gómez-Astorga et al., 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11436195/) | Salinity/moisture calibration and large deviation | Primary full text |
| [Thelaidjia et al., 2026](https://www.mdpi.com/2073-4441/18/12/1431) | Current SEN0193/SEN0308 texture/salinity study | Primary journal article, pre-cut-off |
| [DFRobot SEN0193](https://wiki.dfrobot.com/sen0193) | Official component specs and air/water example | Manufacturer source; no patent-scope inference |
| [Campbell CS655](https://www.campbellsci.com/products/cs655) | Commercial loss correction, EC/temperature and non-interchangeability | Manufacturer assertion |
| [METER TEROS 12](https://metergroup.com/products/teros-12/) | Verification clip, installation, 70 MHz and unit-variability claims | Manufacturer assertion |
| [Delta-T WET150](https://delta-t.co.uk/product/wet150-horticulture/) | Moisture/temperature/EC, interchangeability and recalibration claim | Manufacturer assertion |
| [ISO 11465:2025](https://www.iso.org/standard/88192.html); [withdrawn 1993 edition](https://www.iso.org/standard/20886.html) | Current standard status and historical 105 °C constant-mass principle | Official standards pages; full current method not publicly inspected |
| [FAO gravimetric exercise](https://www.fao.org/fileadmin/user_upload/GSP/GSDP/Field_exercises/NEW_Field_exercises/P06b-gravimetric-soil-water-EN-1-2.pdf) | Practical mass-basis reference procedure | Intergovernmental technical guidance |
| [ASTM D2216-98 historical page](https://store.astm.org/d2216-98.html) | Salt-retention caution | Historical standards page; not represented as current edition |

### 26.3 Legal/eligibility sources

| Jurisdiction | Source | Use |
|---|---|---|
| US | [USPTO MPEP §2106](https://www.uspto.gov/web/offices/pac/mpep/s2106.html); [35 U.S.C. §102](https://uscode.house.gov/view.xhtml?req=%28title%3A35+section%3A102+edition%3Aprelim%29); [§103](https://uscode.house.gov/view.xhtml?req=%28title%3A35+section%3A103+edition%3Aprelim%29) | Eligibility separated from novelty/non-obviousness |
| EPO | [Mathematical methods](https://www.epo.org/en/legal/guidelines-epc/2026/g_ii_3_3.html); [AI/ML](https://www.epo.org/en/legal/guidelines-epc/2026/g_ii_3_3_1.html); [objective technical problem](https://www.epo.org/en/legal/guidelines-epc/2026/g_vii_5_2.html) | Specific technical purpose/effect and evidence |
| India | [IPO CRI Guidelines](https://ipindia.gov.in/storage/uploads/docs-operator/62449276-74f6-438d-92fc-14b2cf3fa204.pdf) | Section 3(k), technical effect/contribution and implementation |
| China | [CNIPA Patent Law](https://english.cnipa.gov.cn/col/col3068/index.html) | Novelty, inventiveness, practical use and Article 25 exclusion |

### 26.4 Verification limitations

- Search interfaces and machine translation are incomplete; absence from this report is not evidence of absence.
- Google legal-status/assignee indicators were never used as a final legal conclusion.
- No opinion was formed on equivalents, validity, enforceability, ownership or claim construction.
- No other model’s TrueMoist conclusions were used as current evidence; Phase 2 was used only to seed terms and records, each independently rechecked.
- No OpenBraille/VibeGuard research, cross-concept comparison or Project mC ranking was used.
- The report does not infer patentability from failure to find an exact duplicate.

---

**End of independent research report.**
