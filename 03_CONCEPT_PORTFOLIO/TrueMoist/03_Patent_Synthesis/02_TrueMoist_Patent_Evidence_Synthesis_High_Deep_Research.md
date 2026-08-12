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

