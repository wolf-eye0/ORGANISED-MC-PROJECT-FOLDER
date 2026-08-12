# Source Extraction

- Chapter: `05` — OpenBraille Patent Evidence and Future Research Path
- Authority tier: `TIER_2`
- Manual treatment: `CONDITIONAL_EVIDENCE`
- Original source: `03_CONCEPT_PORTFOLIO/OpenBraille/04_PreBuild_Simulation/OpenBraille_PreBuild_Future_Patent_Case_Simulation.md`
- Current SHA-256: `c38b519adae4831714b5fda8dbae86f2ac97ffe748cabf5cf421651a1b64c8a7`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

# OpenBraille Pre-Build Future Patent-Case Simulation

**Simulation date:** 3 August 2026
**Research cutoff:** 3 August 2026
**Decision posture:** pre-build, hypothetical, evidence-gated
**Governing specification:** `00_READ_FIRST_OpenBraille_PreBuild_Patent_Simulation_Instructions.md`

## Executive finding

The controlled input set passes file control. Exactly 12 physical attachments are present, every controlled byte count and SHA-256 digest matches `99_INPUT_MANIFEST(15).md`, and no duplicate, partial, superseded, or concept-swapped attachment was found. Decision Register v1.2, the final six-servo architecture/memory/SOP, both valid OpenBraille patent syntheses, and both final adjudications are present and readable. The adjudications are decision context, not votes. The filename crossing for the valid secondary synthesis is documented. The failed moving-roller/encoder-wheel/RAMPS/Mega synthesis is absent. No standalone VibeGuard or TrueMoist technical or synthesis report is attached. The manifest is file control only.

The frozen semester MVP remains a one-cell, six-dot, six-SG90-class-servo architecture with an ESP32, direct PWM, one eccentric cam per servo, a follower/guided vertical pin, FDM structure, external regulated power, serial/USB input, local refresh/fault logging, and single-dot-first commissioning. It must use active servo-driven retraction unless a usable passive return is experimentally proved. Nothing in this simulation substitutes a moving roller, encoder wheel, RAMPS/Mega controller, continuous-paper mechanism, electromagnetic actuator, or another OpenBraille architecture.

The fresh claim-level search makes the current patent case weaker, not stronger. Low-cost servo/cam Braille cells are public. More importantly, [US 11,455,910 B2](https://patents.google.com/patent/US11455910B2/en) claims Braille pin actuation by motor-driven cams together with angular-position sensing, and the 2026 [US 12,548,467 B2](https://patents.google.com/patent/US12548467B2/en) claims removable constrained Braille dots and dependent PWM/current-control features in an electromagnetic architecture. Generic current signatures, calibration, homing, retries, modular replacement, and power sequencing are separately crowded by control art. A shared servo-current trace cannot, without validated correlation and ground truth, establish tactile-pin height or correctness; it may reveal only actuator effort, internal servo control behavior, friction, supply variation, or stall.

Accordingly:

- The frozen MVP is a strong semester prototype and a **Track D / no-current-filing** patent position.
- The reports' D11 bundle is presently an **aggregation of known techniques**, not a demonstrated cooperative invention.
- The best technically credible future direction is a separate **Verified Pin-Datum Cell (VPD-C7)**: the physical datum that constrains each pin endpoint also produces pin-side endpoint evidence, while current is retained only as independent effort/overload evidence. Completion is never inferred from current alone.
- VPD-C7 is not assumed to work and is not yet a patentable invention. It first needs a mechanical/electrical redesign, direct displacement ground truth, practical-scale construction, ablations, wear/contamination testing, replacement/reassembly trials, and a refreshed professional search.

This is a management simulation, not legal advice, a patentability opinion, claim construction, infringement analysis, freedom-to-operate clearance, a filing recommendation, or a promise or probability of patent grant.

## 1. Attachment-control audit

### 1.1 Physical inventory against the manifest

All hashes below are complete SHA-256 values computed from the physical attachments. “Exact” means both the byte count and digest match the controlled manifest entry.

| # | Physical attachment | Bytes | SHA-256 | Readability and role | Control result |
|---:|---|---:|---|---|---|
| 1 | `00_READ_FIRST_OpenBraille_PreBuild_Patent_Simulation_Instructions.md` | 11,502 | `6400dd467d01d4d3c803a743da47ef91700ea3a1df64df6bfa39abe1703e6033` | Readable; governing task specification | Exact |
| 2 | `01_Engineering_Design_Review(20).md` | 31,205 | `46f017501ac3ff9ebd6c1fb1e5ee8c068c22ddb08ae204c5609f2b759090295e` | Readable; highest technical authority | Exact |
| 3 | `02_Project_mC_Decision_Register_v1.2(21).md` | 56,071 | `9678c5072d86ef38e48372f940ec91396b7ac7bcbeed0124ac8e2485307f408c` | Readable; Decision Register **v1.2** | Exact |
| 4 | `03_Phase3C_OpenBraille_Architecture_Report_Final.md` | 46,132 | `84c658ba992d729027b1f931f8c20715f5deecf385b78e767e4c32e2b83354e1` | Readable; final six-servo architecture | Exact |
| 5 | `04_Phase3C_OpenBraille_Memory_Final.md` | 12,364 | `5dad0e392cf9c64d7e8f29be09fadb70acde5b965b95744fa066b5f4b4fd30eb` | Readable; final architecture memory | Exact |
| 6 | `05_Phase3C_OpenBraille_SOP_Final.md` | 4,746 | `bfee5dc46675d77b318f4a0d4fe864d77a570a1150cc2676a5dd10103f214e50` | Readable; final architecture SOP | Exact |
| 7 | `06_Uncertainty_and_Test_Register(1).md` | 22,484 | `125c057229524532b115391fbba948023684ad61d0153fb28ac29e6031e8ee3b` | Readable; unresolved engineering/test risks | Exact |
| 8 | `07_OpenBraille_Patent_Synthesis_Work_Max.md` | 113,903 | `d92dbfbbbdbd4c49e9eaac9fab01e0d2a7db6d986c81d33ee65223710dd42eb1` | Readable; valid primary synthesis | Exact |
| 9 | `08_OpenBraille_Patent_Synthesis_Valid_Secondary.md` | 86,337 | `b9fefadf621f014dc621ef9836ae11b80c05a0227f768c53c11ec1358fc8a09b` | Readable; valid secondary synthesis under controlled name | Exact |
| 10 | `09_Project_mC_Final_Adjudication_Max(1).md` | 90,458 | `02baa83e691bf88e5221e20ac92e5be94eb3c71280b48c8338a02401bb173c9f` | Readable; final adjudication, context only | Exact |
| 11 | `10_Project_mC_Final_Adjudication_Deep_Research_High(1).md` | 48,193 | `29d0f85d95f7ef98d1a1a31a395cbbab5511ae25df2eeb15840978d7bfb3590e` | Readable; final adjudication, context only | Exact |
| 12 | `99_INPUT_MANIFEST(15).md` | 14,201 | `f7c917e943bbc492fcef160adac7f9a2a834b081684b589d54d2cc05f322eafc` | Readable; file control only | Exact |

There are 12 distinct digests. Total controlled attachment size is 537,596 bytes.

### 1.2 Required control confirmations

| Required confirmation | Result | Basis |
|---|---|---|
| 1. Exactly 12 physical attachments are present | **Pass** | Twelve controlled files were enumerated; no extra user attachment was present. |
| 2. Decision Register v1.2 is present | **Pass** | File 3 is the manifest-controlled v1.2 register and is readable. |
| 3. Final six-servo architecture, memory, and SOP are readable | **Pass** | Files 4–6 are complete and readable; all describe the same one-cell six-servo/cam architecture. |
| 4. Both valid OpenBraille synthesis reports are present | **Pass** | Files 8 and 9 match the two controlled valid syntheses. |
| 5. Both final adjudications are present and are context, not votes | **Pass** | Files 10 and 11 match; neither is counted or averaged as a patent vote. |
| 6. The OpenBraille filename crossing is documented | **Pass** | The manifest maps the valid secondary source name `OpenBraille_Patent_Synthesis_ChatGPT_Standard_High_no_deeprsearch.md` to controlled file 08. |
| 7. Failed moving-roller/encoder-wheel concept-swap synthesis is absent | **Pass** | The excluded `OpenBraille_Patent_Synthesis_ChatGPT_Deep_Research.md` is not attached. No supplied file adopts that architecture as OpenBraille. |
| 8. No VibeGuard or TrueMoist technical report is attached | **Pass** | Those concepts are mentioned inside cross-project adjudications, but no standalone technical or synthesis report for either concept is present. |
| 9. The manifest is file control only | **Pass** | It is used only for identity, count, checksum, crossing, exclusion, and completeness control—not technical or patent authority. |
| 10. Nothing is missing, duplicated, partial, superseded, or concept-swapped | **Pass** | Counts, sizes, unique hashes, completeness text, version control, and concept-fidelity checks all agree. |

## 2. Governing architecture and conflict resolution

The authority order applied here is: Engineering Design Review; Decision Register v1.2; final Architecture; final Memory; final SOP; Uncertainty/Test Register; the two audited syntheses; the two adjudications as context; then fresh primary patent and technical research.

### 2.1 Frozen semester MVP

| Element | Frozen requirement | Simulation treatment |
|---|---|---|
| Tactile output | One macro-scale six-dot cell | Preserved; useful demonstrator, not claimed as invention merely because it is macro-scale. |
| Actuation | Six SG90-class servos; one eccentric cam per servo; follower/guided vertical pin | Preserved. No roller or substituted actuator. |
| Controller | Local ESP32, direct PWM from GPIO | Preserved. Controller and PWM are ordinary implementation choices. |
| Structure | FDM frame, guides, and cams | Preserved. FDM and exact material/part-number choices are not invention by themselves. |
| Return | Active servo-driven cam retraction unless passive return is proved | Decision Register v1.2 controls. Architecture/memory statements implying an integrated SG90 torsion-spring reset are treated as unverified legacy text. |
| Power | External regulated supply; 5 V class, 2 A or greater, local bulk capacitance | Preserved; actual droop/current data must set the final rating. |
| Interface/logging | USB/serial input; local refresh and fault logging | Preserved. |
| Commissioning | Single-dot first, then staged integration | Preserved. |

The architecture report's statements that a self-test “verifies travel” are not accepted without a travel sensor or external ground truth. A PWM command or motor movement is not evidence that the tactile pin reached the correct physical state.

### 2.2 Patent boundary

The semester prototype can prove engineering feasibility and create an evidentiary record. It does not become an invention through exact SG90 part numbers, low price, macro scaling, FDM manufacture, ESP32 selection, direct PWM, or the combination “servo + cam + Braille pin.” Any patent case must arise, if at all, from a later demonstrated physical interaction that solves silent tactile-state error at practical geometry without merely assembling known calibration, sensing, retry, and scheduling blocks.

## 3. Simulation method and limitations

This simulation separately asks:

1. **Anticipation:** does one reference disclose every material claim element? The USPTO's current anticipation framework requires each and every element in one reference. See [MPEP § 2131](https://www.uspto.gov/web/offices/pac/mpep/s2131.html).
2. **Obviousness/inventive step:** would a skilled person combine known features with a reason and a predictable result? See [MPEP § 2141](https://www.uspto.gov/web/offices/pac/mpep/s2141.html), the [EPO 2026 problem–solution guidance](https://www.epo.org/en/legal/guidelines-epc/2026/g_vii_5.html), and India's official [Patent Office Manual](https://ipindia.gov.in/frontend/pdf/patents/Manual_for_Patent_Office_Practice_and_Procedure_.pdf).
3. **Eligibility/technical character:** is the proposal a physical electromechanical system/control process rather than an abstract classification rule or software per se? See [MPEP § 2106](https://www.uspto.gov/web/offices/pac/mpep/s2106.html), the EPO's [further-technical-effect guidance](https://www.epo.org/en/legal/guidelines-epc/2026/g_ii_3_6_1.html), and sections 3(k) and 3(f) of India's official [Patents Act, updated through 1 August 2024](https://ipindia.gov.in/frontend/pdf/patents/1_113_1_The_Patents_Act__1970___incorporating_all_amendments_till_1-08-2024.pdf).
4. **Enablement/sufficiency:** can the full proposed scope be made and used without undue experimentation? See [MPEP § 2164](https://www.uspto.gov/web/offices/pac/mpep/s2164.html) and the EPO's [sufficiency guidance](https://www.epo.org/en/legal/guidelines-pct/2026/f_iii_1.html).
5. **FTO/design-around:** could making or selling the implementation fall within a live claim? This requires jurisdiction-by-jurisdiction claim construction and official status/file-history review; similarity or an expired reference is not clearance.

Patent publication texts are primary technical/claim sources. Database status flags below are preliminary signals only. Google Patents itself marks legal status and assignee data as non-legal conclusions. Before any commercial build or disclosure-triggered filing decision, counsel should verify United States records in [USPTO Patent Center](https://patentcenter.uspto.gov/), European records in the [European Patent Register](https://register.epo.org/), PCT records in [WIPO PATENTSCOPE](https://patentscope.wipo.int/), and Indian records through [IP India](https://ipindia.gov.in/), including prosecution histories, continuations/divisionals, maintenance, term adjustment, ownership, and territorial coverage.

No experiment has yet established that the frozen MVP or any hypothetical mechanism works. Every performance statement below is a test target, gate, or management scenario—not a finding.

## 4. Fresh patent landscape

### 4.1 Load-bearing claim ledger

| Record/application; priority; applicant/assignee | Claim-level teaching relevant here | Preliminary database signal as of cutoff | Use in this simulation |
|---|---|---|---|
| [US 8,483,018 B2](https://patents.google.com/patent/US8483018B2/en), app. US13/314,835; 8 Dec 2011; WARF | Independent watch claim uses a rotatable disk having a raised region to translate guided tactile pins; description shows servo/PWM implementation. | Fee-related expiry signal; family/status still needs official check. | Strong prior art against broad servo/cam/guided-pin reasoning; watch/disk/four-pin limitations reduce direct FTO overlap. |
| [US 2013/0017516 A1](https://patents.google.com/patent/US20130017516A1/en), app. US13/180,351; 11 Jul 2011; individual | Independent claims cover an active Braille timepiece with independently translated pins and processing; dependent claims recite spring/lever, camshaft, and direct drive. | Abandoned signal. | Prior art remains usable even if abandoned; reinforces ordinary cam/spring/direct-drive choices. |
| [US 11,455,910 B2](https://patents.google.com/patent/US11455910B2/en), app. US16/358,925; 29 Mar 2018; HumanWare/Design 1st | Independent pin-actuation claims recite a motor, a set of cams that place pins in configurations, and angular-position sensing; dependent claims specify magnetic/Hall reference sensing and calibrated position inference. | Active signal; adjusted expiry shown as 28 Jul 2041. | Closest new search hit for cam + sensing. It sharply weakens a broad “cam cell with optical/Hall/encoder verification” claim and creates a real FTO review item. |
| [US 7,410,359 B1](https://patents.google.com/patent/US7410359B1/en), app. US10/711,423; 30 Jan 2004; Freedom Scientific/Enhanced Vision | Claims a piezoelectric tactile-cell electrical/mechanical support assembly; description and family materials teach pin stops, collars, calibration, and serviceable structures. | Active signal through 9 Dec 2026; official maintenance/term check required. | Potentially live near-term FTO context for particular piezo/support structures; broad datum/collar concepts are old. |
| [US 8,690,576 B2](https://patents.google.com/patent/US8690576B2/en), app. US13/407,364; root priority 30 Jan 2004; Freedom Scientific/Enhanced Vision; family includes WO 2013/130534 and US 9,424,759 | Independent claims include releasable mounting blocks, tactile pins with collars, an overlying plate limiting upward travel, modular pin groupings, and removable cell/PCB structures. | Lifetime-expired signal (18 Apr 2025); related US/EP/WO/JP family members must be checked. | Strong prior art against generic physical stops, collars, modular mounting, and replacement; an expired US record is not an FTO veto, but relatives may matter. |
| [US 12,080,182 B2](https://patents.google.com/patent/US12080182B2/en), app. US18/191,091, and [US 11,645,948 B2](https://patents.google.com/patent/US11645948B2/en), app. US17/197,621; 10 Mar 2020; Enhanced Vision; WO 2021/183616 family | Claims a capture-plate/top assembly separated by a membrane, with touch-layer/removability variants. Statements about tolerances, cleaning, movement detection, and remounting must not be mistaken for every claim. | Active signals; US/PCT family shown. | Avoid copying the claimed capture/top/membrane arrangement. General replacement acceptance is still crowded but must be mapped element by element. |
| [US 12,548,467 B2](https://patents.google.com/patent/US12548467B2/en), app. US17/302,988; [WO 2020/106855 A1](https://patents.google.com/patent/WO2020106855A1/en), PCT/US2019/062433; [EP 3,884,363 B1](https://patents.google.com/patent/EP3884363B1/en), app. EP19887358.0; 20 Nov 2018; Enhanced Vision | US claim 1 uses a removable top dot-capture assembly, constrained collars, aligned actuator dots, electromagnetic actuators/driver board, and debris membrane. Dependent claims add PWM, calibrated current-polarity reversal, and bounce reduction. EP claims focus on electromagnetic actuation and separable dot assembly; position/movement discussion is broader than the independent claims. | US grant 10 Feb 2026, active signal to 3 Apr 2042; EP B1 published 6 Aug 2025, active signal. JP/KR/CA relatives shown. | Newly material family. It does not anticipate six independent servos, but it crowds travel constraints, removable dot assemblies, PWM/current control, and service/cleaning combinations. |
| [US 12,374,235 B2](https://patents.google.com/patent/US12374235B2/en), app. US17/668,034 / [WO 2023/154400 A1](https://patents.google.com/patent/WO2023154400A1/en), PCT/US2023/012710; 9 Feb 2022; Enhanced Vision | Claims a contaminant barrier film with indentations beneath pins and actuator contact through the film. | Active US signal to 5 Sep 2043; continuation US19/282,494 and EP family activity indicated. | Avoid an ingress-film arrangement without claim mapping; not central if VPD-C7 uses no membrane. |
| [US 6,776,619 B1](https://patents.google.com/patent/US6776619B1/en); 14 Sep 2001; individual | Rotating wheel with many tactile pins, static actuator rows, and passive retention. | Expired-term inference requires official confirmation. | Prior art only. Also demonstrates why moving-wheel architecture is a different, excluded concept—not a substitute. |
| [US 11,854,423 B1](https://patents.google.com/patent/US11854423B1/en) and [US 11,521,514 B2](https://patents.google.com/patent/US11521514B2/en) | Friction-retained pin arrays reconfigured by shared motorized impact/drive mechanisms. | Active signals require official checks. | Crowds shared-hammer/friction architectures, which are not the frozen OpenBraille design. |
| [US 11,410,574 B2](https://patents.google.com/patent/US11410574B2/en) / [WO 2016/074170 A1](https://patents.google.com/patent/WO2016074170A1/en) | Layered electromagnetic Braille-cell architecture. | Active-family signals. | Alternative-actuator landscape; not a reason to substitute electromagnetics into the MVP. |
| [WO 2015/189863 A2](https://patents.google.com/patent/WO2015189863A2/en); IIT Delhi | Layered/cantilever/latching SMA Braille actuation. | PCT/national status needs official review. | Shows low-cost/latching/cantilever alternatives and narrows broad functional claims. |
| [EP 4,049,116 B1](https://patents.google.com/patent/EP4049116B1/en); University of Bath | Frequency-selective resonant cantilever taxels driven by a common source. | Active EP signal. | Alternative architecture only; strong art against broad “low-actuator-count tactile array” results. |
| [CN 116343558 A](https://patents.google.com/patent/CN116343558A/en); 7 Mar 2023; applicant shown in record | Modular, positioned injection-molded Braille module with electromagnetic drive. | Pending/publication signal; machine translation and national status unresolved. | Supports crowding of modularity/positioning; low claim-mapping confidence pending native-language review. |
| [WO 2024/174030 A1](https://patents.google.com/patent/WO2024174030A1/en); 23 Feb 2023; HumanWare/APH | Equidistant two-dimensional tactile/Braille array and spacing/block arrangements. | PCT ceased signal; national-phase coverage unresolved. | Practical-scale array context; not direct D11 anticipation. |
| Indian application **5559/CHE/2014**; reported filing 5 Nov 2014 | A contemporaneous public project record attributes micro-motor-actuated pins, cantilever/stop, vertical or horizontal motor/cam placement, direct or interposer lift, and low-force selection to the application. | **Official specification, claims, publication number, ownership, and status were not retrieved.** IP India's public system was not usable here for a claim-level verification. | Material unresolved prior-art/FTO blocker. Do not rely on secondary assertions of grant, expiry, or scope. Obtain the official file and prosecution/status record before disclosure or filing decisions. Public context: [2016 project log](https://hackaday.io/project/10849-refreshable-braille-display/discussion-54691); official portal: [IP India](https://ipindia.gov.in/). |

### 4.2 Generic sensing and control art

The following records do not necessarily create literal Braille FTO overlap, but they are powerful obviousness references when combined with Braille-cell art:

- [US 9,706,716 B2](https://patents.google.com/patent/US9706716B2/en) monitors motor current, correlates signatures with known mechanism positions, detects spikes/stall, and drives a mechanism to a home condition. Its independent claim is baler-specific, so it is more important for obviousness than literal OpenBraille FTO.
- [US 10,879,831 B1](https://patents.google.com/patent/US10879831B1/en) samples motor-drive signals, forms signatures, compares them with expected signatures, and identifies anomalies. It crowds generic “learn a normal current trace and classify a fault” language.
- [US 2017/0030739 A1 / US 9,989,383 B2](https://patents.google.com/patent/US20170030739A1/en) stores electromagnetic-actuator measurements indicative of plunger positions, measures an actual value, compares it, reports position, and in dependent claims adjusts drive or uses an additional proximity sensor. It is direct art against broad sensorless-position-plus-retry logic.
- [US 4,965,513 A](https://patents.google.com/patent/US4965513A/en) is older motor-current-signature analysis art. A current waveform as a fault fingerprint is not new.

Circuit implementation is ordinary engineering. Texas Instruments' [current-sensing guide](https://www.ti.com/lit/eb/slyy154a/slyy154a.pdf) and NXP's [AN14164 current-sensing note](https://www.nxp.com/docs/en/application-note/AN14164.pdf) show established high-side/low-side, bandwidth, dynamic-range, common-mode, and layout tradeoffs. These sources support feasibility planning, not novelty.

### 4.3 Non-patent technical evidence

- Aryan et al., [“Refreshable Braille Module Using Cam Actuated Mechanism”](https://doi.org/10.1088/1757-899X/1123/1/012028) (2021), publicly describes an SG90-driven cam arrangement. Rahman et al., [“A Portable Braille Refreshable Display Using Micro Servos”](https://doi.org/10.1109/ICIEV.2018.8641028), likewise crowds low-cost micro-servo actuation. These are not the frozen design, but they defeat broad novelty narratives about using inexpensive servos/cams for Braille.
- The public 2016 [Refreshable Braille Display project](https://hackaday.io/project/10849-refreshable-braille-display) documents FDM tolerance iteration and micro-servo prototypes. It also flags the unresolved Indian micro-motor/cam application.
- Chen et al.'s primary experimental papers on layered electromagnetic Braille actuators report measured force/frequency performance ([2023](https://pubmed.ncbi.nlm.nih.gov/37022849/); [2024](https://pubmed.ncbi.nlm.nih.gov/38324442/)). They are useful comparison baselines, not reasons to change the frozen architecture.
- A 2026 experimental mechanism comparison by Arora and Jain evaluates several low-cost micro-motion approaches ([MATEC paper](https://www.matec-conferences.org/articles/matecconf/abs/2026/01/matecconf_icmme2026_01017/matecconf_icmme2026_01017.html)). It confirms that actuator choice remains a cost/performance trade, not an empty field.
- The [2010 ADA Standards](https://www.ada.gov/law-and-regs/design-standards/2010-stds/) give useful physical Braille geometry for signs: dot-base diameter 1.5–1.6 mm, within-cell center spacing 2.3–2.5 mm, cell separation 6.1–7.6 mm, row separation 10.0–10.2 mm, and dot height 0.6–0.9 mm. [ISO 17049:2013](https://www.iso.org/standard/58086.html) addresses Braille dimensional/material requirements for signage, equipment, and appliances. Neither source should be misrepresented as a universal dynamic-display force or refresh-speed standard.
- Polymer material extrusion has meaningful process-dependent geometric error and surface variation. NIST's [polymer additive-manufacturing measurement roadmap](https://nvlpubs.nist.gov/nistpubs/ams/NIST.AMS.100-5.pdf) and a 2025 experimental [FDM geometric-accuracy study](https://www.mdpi.com/2073-4360/17/3/416) support measuring each printed guide/datum rather than assuming nominal CAD equals the physical part.

## 5. What the fresh search does—and does not—establish

### 5.1 Present novelty position

No reviewed single record was found that expressly claims the entire hypothetical VPD-C7 combination: six independent servo/cam/pin channels; a pin-side endpoint datum that both physically constrains travel and produces an endpoint event; a separate shared current channel used only as effort/overload evidence; a four-outcome state machine including Unknown; and bounded retry/fault isolation. That is **not** a novelty conclusion. The Indian file is unresolved, the search is not exhaustive, non-English claim review is limited, unpublished applications may exist, and a later professional search may find a single anticipating disclosure.

### 5.2 Present obviousness position

The building blocks are individually and jointly crowded:

- physical pin collars/stops and removable mounting: Freedom Scientific/Enhanced Vision families;
- motor/cam Braille actuation plus position sensing: HumanWare US 11,455,910;
- micro-servo/cam Braille actuation: public patent/NPL records;
- current-position/fault signatures and retry: generic actuator-control records;
- current-limited/PWM actuator behavior: Enhanced Vision and generic motor-control art;
- calibration, homing, bounded state machines, power budgeting, and fault isolation: routine control practice.

The most plausible examiner combination is HumanWare's cam/sensor cell plus Freedom Scientific's stop/collar/module teachings plus generic current-signature and anomaly detection. A mere desire to make state estimation more reliable, serviceable, or power efficient supplies an evident reason to combine. Patent viability therefore depends on a narrow, structurally defined cooperative interaction and unexpected measured effect—not a list of familiar functions.

### 5.3 Present FTO position

No FTO clearance is given. The strongest current design-around boundary is to avoid: multi-pin cams on one sensed shaft; HumanWare-style support arms/monolithic pin units; Enhanced Vision capture/top/membrane assemblies; electromagnetic dot/driver structures; and any unverified feature of 5559/CHE/2014. Six independent hobby servos are not a blanket safe harbor: claim scope, equivalents, continuations, national relatives, and the actual implementation still matter.

## 6. Common future-state model

The candidates are deliberately different. They do not imply that every feature belongs in one future product. Where a sensor is development-only, it is removed from the proposed operating architecture but retained as an external oracle during validation.

The common transition vocabulary is:

| State | Meaning | Permitted evidence |
|---|---|---|
| `LOWER_CONFIRMED` | Pin is at the lower physical endpoint within the qualified tolerance. | Direct pin-side endpoint/displacement evidence only. A PWM command is insufficient. |
| `RAISING` | A raise command is in progress. | Command/timestamp, voltage, current, and any direct sensor. |
| `UPPER_CONFIRMED` | Pin is at the upper physical endpoint within the qualified tolerance. | Direct pin-side endpoint/displacement evidence only. Current by itself is insufficient. |
| `LOWERING` | An active-retraction command is in progress. | Same evidence rules as raising. |
| `INCOMPLETE` | The requested transition ended without endpoint evidence, but no validated jam condition was met. | Timeout/window plus direct sensor or absence of required event. |
| `JAMMED` | A pre-registered obstruction/overload condition was met. | Prefer independent position + effort evidence; a current-only jam label remains provisional until validated. |
| `UNKNOWN` | Evidence is absent, conflicting, outside the trained/qualified envelope, or attributable to more than one servo. | Mandatory fail-safe outcome; never silently promoted to completed. |
| `ISOLATED` | The channel is disabled after a bounded retry or safety limit. | Logged transition and fault policy. |

For candidates without permanent direct state sensing, the runtime may report `COMMAND_FINISHED` but may not relabel that event `UPPER_CONFIRMED` or `LOWER_CONFIRMED`. External optical/displacement ground truth supplies those labels during development.

## 7. Seven materially different future architectures

### 7.1 Comparison matrix

Planning cost ranges are rough incremental prototype allowances in INR, excluding the frozen MVP, labor, professional patent work, and test metrology already available. They are not quotations.

| ID | Exact future architecture | Permanent sensor | Claimed physical effect under test | Closest art / primary risk | MVP compatibility | Disposition |
|---|---|---|---|---|---|---|
| **C1 D-CAL** | Physical upper/lower stops; per-dot PWM endpoint and timing calibration; active retraction | None | Reduced height scatter and fewer stalls than a common PWM setting | Pin stops/collars; routine calibration; servo/cam NPL | High; guide/cam tuning only | Engineering baseline; reject as patent lead |
| **C2 D-SHUNT** | C1 plus high-bandwidth shared rail shunt/amplifier/ADC; single-channel diagnostic windows and background accounting | Shared current/voltage | Current trace may distinguish normal motion, obstruction, and supply fault | US 9,706,716; US 10,879,831; servo internal-control confounding | Medium; instrumented rail | Experimental Track D; current cannot certify height |
| **C3 P-POS** | Per-pin linear optical, magnetic, or mechanical endpoint/displacement sensor located on the pin side of compliance | Six direct position channels | Actual pin-state observability independent of servo command | US 11,455,910 plus generic position sensors | Medium-low; packaging change | Best measurement oracle/product fallback; weak patent lead |
| **C4 R-SERVICE** | Keyed removable servo/cam cartridge; identity record; two-end recalibration and acceptance after replacement/remount/reassembly | Optional service fixture or per-pin sensor | Restores qualified travel after service without silent misalignment | US 8,690,576; US 12,080,182; US 12,548,467 | Medium; separate carrier redesign | Dependent feature only; reject standalone claim |
| **C5 PWR-ISO** | Supply-voltage/current budget; measured sequential/group scheduling; brownout guard; per-channel isolation | Shared voltage/current | Lower peak demand and contained faults | Generic power scheduling; Enhanced Vision driver boards/current control | High | Engineering feature; reject standalone patent case |
| **C6 R-D11** | Datum + per-dot bounded drive windows + isolated current evidence + `Unknown` + one bounded retry/isolation; generic service and scheduling removed from inventive core | Shared current/voltage | Reduced unsafe retries and silent actuator-command errors, but not directly verified pin height | Combined HumanWare/Freedom/current-signature art | Medium | Narrow experimental hypothesis; Track D only |
| **C7 VPD-C7** | Each pin's upper/lower physical datum also forms a low-energy pin-side endpoint contact; current separately measures effort; deterministic state machine and bounded isolation | Twelve endpoint contacts plus one shared current/voltage channel | Same datum both constrains travel and generates actual endpoint evidence; separate effort channel distinguishes obstruction from endpoint | Stop/collar + limit-switch + cam-sensor combination; unresolved Indian file | Low-medium; separate post-MVP guide/pin variant | **Redesign and test first; only conditional patent lead** |

### 7.2 C1 — Datum and calibration without current (`D-CAL`)

**Problem and architecture.** FDM guide variation, cam eccentricity, linkage play, servo deadband, and supply differences can make a common PWM command produce inconsistent travel. C1 adds measured lower and upper mechanical datums and stores a minimum reliable active-up and active-down command window for each dot. Commissioning sweeps one dot at a time against an external displacement oracle and locks the smallest repeatable window plus margin. Runtime is open-loop: `LOWER_COMMAND`, `RAISING`, `UPPER_COMMAND`, `LOWERING`, timeout/fault. It never claims physical completion.

**Sensors and effect.** A camera, laser displacement gauge, dial indicator, and force gauge are development-only. There is no permanent current or position sensor. The testable effect is lower height variance, lower peak current, and fewer stalls relative to one fixed PWM value—not verified correctness.

**Patent attack.** Stops/collars are disclosed in the Freedom/Enhanced Vision families; servo/cam Braille is public; per-actuator calibration is ordinary control. A single anticipation reference may depend on claim wording, but a HumanWare/Freedom/servo-NPL combination makes the result predictable. Eligibility is easy in the US/EPO because it is a physical device; India section 3(f) is a serious risk because known parts retain their ordinary functions. Enablement is achievable only for measured servo/print/material ranges, not “all tactile displays.” FTO needs the actual stop/collar structure checked. Any surviving claim would be commercially narrow and easy to design around with a different actuator, sensor, or machined guide.

**Resources, experiment, and kill.** Incremental hardware: ₹150–₹400; compute: trivial table lookup. It is highly MVP-compatible. Compare common PWM against per-dot calibration across servo swaps, three reprints/reassemblies, voltage, temperature, finger-equivalent load, and contamination. Kill any patent thesis immediately if the only advantage is routine tuning; retain C1 as the minimum engineering baseline. Keep CAD/calibration data confidential only until the broader disclosure decision; disposition is **build as baseline, no patent lead**.

### 7.3 C2 — Datum plus shared high-bandwidth current (`D-SHUNT`)

**Problem and architecture.** C2 asks whether current adds information about motion or obstruction without six position sensors. It adds an external shunt, amplifier, voltage measurement, synchronized ADC, and timestamps to C1. Start with one servo physically and electrically isolated on a single-dot fixture. In the six-dot cell, diagnose only during pre-registered windows in which one servo transitions and background current from holding channels is measured. If attribution cannot be bounded, output is `UNKNOWN`; background subtraction is not assumed valid.

**Sensors and effect.** Current/voltage sensing is permanent in the candidate; optical displacement and force are development-only labels. The target effect is classification of normal effort, jam, supply droop, and unclassifiable events. Current is **not** a pin-position sensor. SG90-class servos contain their own feedback electronics, gears, motor, and control loop; rail current can change with motor effort, control pulses, gear friction, temperature, voltage, and load even when the tactile endpoint is wrong.

**Patent attack.** Motor-current position/fault signatures are directly taught by US 9,706,716, US 10,879,831, US 9,989,383, and older signature art. Combining that with a known servo/cam Braille cell is straightforward. US eligibility and EPO technical character are likely satisfied if claims require measured electrical/physical effects, but novelty/inventive step remains weak. In India, a broad classifier risks section 3(k) and an uncooperative sensor-plus-servo aggregation risks section 3(f). Full-scope enablement would require showing transfer across servo lots, voltages, temperatures, wear, and loads; one trained device is not enough. Literal FTO risk from the cited baler claim is low because of its machine context, but other unsearched motor-control claims remain.

**Resources, experiment, kill, and confidentiality.** Incremental hardware: ₹450–₹1,100; compute: moderate fixed-window features, not black-box ML. Compatibility is medium because clean shared-rail attribution may require switching, separate rails, or test-only instrumentation. Kill current-as-state if held-out data show it adds no information beyond command/elapsed time/supply voltage, if models do not transfer after servo replacement, or if any current-only “completed” label yields silent wrong tactile states. Keep raw traces, feature definitions, thresholds, and transfer results confidential until the patent/no-patent gate; preserve negative results. Disposition: **instrumentation and Track D research, not a claim lead**.

### 7.4 C3 — Direct pin-position verification (`P-POS`)

**Problem and architecture.** C3 measures the moving pin itself, downstream of servo backlash, cam/follower compliance, and guide friction. Candidate embodiments are a pin-side optical interrupter, a tiny magnet and stationary Hall sensor, or two low-force mechanical contacts. Sensor thresholds are calibrated against direct tip displacement. A requested transition is complete only after the corresponding pin event; contradictions become `UNKNOWN`; one retry may be allowed only after the first fault model is validated.

**Sensors and effect.** Six direct channels are permanent. External camera/laser and force instrumentation remain development or audit tools. The effect is actual physical-state observability and lower silent-error rate relative to open-loop and current-only operation.

**Patent attack.** HumanWare US 11,455,910 expressly claims motor/cam Braille actuation with angular-position sensing and describes magnetic/Hall implementations. Pin-side linear sensing is structurally different from motor-shaft angular sensing and can detect downstream failures, so that difference matters for anticipation. It may still be obvious to move the sensor to the output when backlash/compliance is the known error source. Generic limit/position sensors add further motivation. Physical eligibility is strong in the US/EPO; India's inventive-step and 3(f) aggregation attacks remain. Enablement must include sensor placement, tolerance stack, drift, debounce, contact wear or magnetic/optical interference, and practical packing. FTO risk is highest for motor/cam sensing language and requires claim construction. A competitor can design around a specific sensor modality.

**Resources, experiment, kill, and confidentiality.** Incremental hardware: ₹900–₹2,500; compute: low. Compatibility is medium-low because practical-scale sensor packaging is hard. Use it first as the reference oracle even if it is later removed. Kill a permanent-sensor product path if the sensor cannot fit practical pitch, changes pin force/height materially, drifts beyond tolerance, or costs more than the proposed actuator saving. Keep sensor placement, calibration, tolerance, and comparative data internal until C7 selection; using C3 as an oracle does not establish inventorship or priority for C7. Disposition: **retain as oracle and product fallback; not the primary patent case**.

### 7.5 C4 — Replacement/remount/reassembly acceptance (`R-SERVICE`)

**Problem and architecture.** Hobby servos and FDM components vary and may be replaced. C4 places each servo/cam in a keyed, hard-datum carrier with an identity/lot record. Its exact service transitions are `REMOVED` → `CALIBRATION_INVALID` → `LOWER_TEST` → `UPPER_TEST` → either `ACCEPTED` or `REJECTED/ISOLATED`. After removal, replacement, or reassembly, firmware invalidates old calibration, runs lower/upper endpoint acceptance against a service fixture or permanent direct sensor, stores new limits, and refuses display service if tolerance, force, or timing is outside the qualified envelope.

**Sensors and effect.** A removable optical/displacement service fixture is preferred during development; a direct sensor can be permanent in a product version. The proposed effect is restoration of qualified output after service, not mere ease of replacement.

**Patent attack.** US 8,690,576 claims removable cells/mounting blocks; US 11,455,910 claims releasable support structures; US 12,080,182 and US 12,548,467 crowd removable dot/capture assemblies. Calibration after replacement is a predictable service response. No broad standalone apparatus or method claim is credible. A narrow dependent feature might survive only if keyed datum transfer and a specific acceptance sequence show an unexpected reduction in recalibration burden or silent errors. Physical eligibility is straightforward; India section 3(f), obviousness, and enablement at full scope are major problems. FTO turns on the exact cartridge, capture, support, and membrane elements.

**Resources, experiment, kill, and confidentiality.** Incremental hardware: ₹300–₹900 plus oracle; compute: low. Compatibility is medium and should not alter the semester build. Conduct blind swaps among at least three servos, repeated removal cycles, three printed carriers, and independent operators. Kill the patent feature if a conventional keyed mount plus ordinary recalibration performs equivalently. Keep carrier datum drawings, acceptance windows, and swap results confidential until the dependent-feature decision. Disposition: **service requirement and possible dependent fallback only**.

### 7.6 C5 — Low-peak coordinated refresh and fault isolation (`PWR-ISO`)

**Problem and architecture.** Six servos can create peak demand, droop, resets, and coupled faults. C5 records rail voltage/current and empirically qualifies safe one-at-a-time or bounded-group transitions. Its scheduler states are `QUEUED`, `ADMITTED`, `TRANSITIONING`, `DEFERRED`, `OVER_LIMIT`, and `ISOLATED`. A scheduler admits a transition only within a measured current/voltage budget, delays lower-priority moves, and disables a repeatedly over-limit channel. It deliberately has no direct state verification.

**Sensors and effect.** Shared voltage/current sensing is permanent. The measured effect is lower peak current, less droop/reset incidence, and containment of a faulty channel relative to simultaneous refresh and fixed one-at-a-time baselines. The output state remains unverified.

**Patent attack.** Load staggering, current budgeting, brownout management, and fault isolation are standard multi-actuator controls; Enhanced Vision's driver-board/current-control disclosures further crowd the tactile field. A Braille use limitation does not create inventiveness. Eligibility/technical effect are strong because supply behavior is physical, but US obviousness, EPO inventive step, and Indian section 3(f) attacks are severe. Enablement requires the admitted group sizes, load envelope, supply impedance, and failure policy. Broad claims are easy to design around with a larger supply, local storage, different schedule, or per-channel driver.

**Resources, experiment, kill, and confidentiality.** Incremental hardware: ₹300–₹700; compute: trivial scheduling. Highly compatible after single-dot commissioning. Compare simultaneous, fixed sequential, current-aware without state verification, and full candidates at identical transition sets. Kill the patent thesis if benefits are fully predicted by elementary supply sizing or fixed sequencing; keep the engineering safeguard. Ordinary supply-characterization data needs no separate patent secrecy once C7 interactions are removed, but do not disclose C7 thresholds or combined results before the common gate. Disposition: **use if data justify it, no standalone patent lead**.

### 7.7 C6 — Reduced indispensable D11 (`R-D11`)

**Problem and exact architecture.** C6 strips D11 to elements that might interact in the frozen actuator context: physical datum; per-dot minimum reliable active-up/down windows; synchronized isolated current/voltage measurement; an explicit `UNKNOWN` state; and one bounded retry followed by isolation. It removes modularity and adaptive power scheduling from the putative inventive core. External direct displacement supplies development truth. Runtime current can label `EFFORT_NORMAL`, `OVERLOAD_LIKE`, `SUPPLY_FAULT`, or `UNCLASSIFIED`; it cannot create `UPPER_CONFIRMED` or `LOWER_CONFIRMED`.

**Effect and evidence.** The possible cooperative effect is not “more data.” It would have to be a reproducible reduction in unsafe repeat actuation or silent commanded-state error caused specifically by the interaction of mechanical bounds, individualized minimum drive, and effort classification—greater than the best calibrated open-loop and current-only baselines. Missing evidence includes transfer across servos/rebuilds, discrimination of endpoint contact from wrong-height friction, practical-scale behavior, and causal ablations.

**Patent attack.** No reviewed reference was identified as a single-document anticipation of this exact restricted bundle, but HumanWare/Freedom plus generic current-signature art creates a strong combination. The proposed output is predictable unless the interaction produces a surprising effect. US eligibility and EPO technical effect are supportable only with physical measurements and control of the mechanism. India 3(k) is addressed by not claiming classification in isolation, but section 3(f) remains until cooperation is proved. Enablement cannot exceed the tested servo/geometry/environment envelope. FTO remains open, especially the Indian file and active HumanWare/Enhanced Vision families. Any claim would be narrow and easy to avoid by direct position sensing, a different actuator, or no retry.

**Resources, experiment, kill, and confidentiality.** Incremental hardware: ₹450–₹1,100; compute: fixed feature extraction and thresholds. Compatibility is medium, on a separate instrumented fixture first. Apply every required baseline and feature-removal ablation in section 11. Kill the patent case if current adds no held-out benefit, any completion inference depends on current, performance collapses after replacement/reassembly, or the full bundle is additive rather than super-additive. Keep the exact D11 implementation, raw labels, thresholds, failures, and ablation results confidential until the refreshed-search decision. Disposition: **Track D evidence only**.

### 7.8 C7 — Verified Pin-Datum Cell (`VPD-C7`), stronger alternative

**Problem and exact architecture.** C7 moves primary evidence to the tactile output rather than the motor. Each guided vertical pin has internal, electrically isolated upper and lower shoulders. Each stationary endpoint datum is a replaceable wear element that both (a) physically sets the pin endpoint and (b) forms a low-energy sense circuit when the corresponding pin shoulder reaches it. The sensing circuit carries no servo power. The six independent SG90-class servos, six eccentric cams, followers, ESP32, direct PWM, external supply, and active retraction remain. A separate shared shunt/voltage channel measures effort and supply behavior only.

For a raise request:

1. verify or establish lower contact; otherwise start in `UNKNOWN`;
2. command the calibrated active-up window and enter `RAISING`;
3. require lower-contact release followed by upper-contact assertion within a bounded time and displacement-qualified tolerance;
4. if upper contact occurs and effort stays within the qualified envelope, enter `UPPER_CONFIRMED`;
5. if effort exceeds a validated obstruction envelope without upper contact, enter `JAMMED`; if evidence is absent or conflicting, enter `UNKNOWN`/`INCOMPLETE`;
6. permit at most one validated unload-and-retry sequence, then `ISOLATED`.

Lowering is symmetrical and always active. Contact bounce, simultaneous contacts, a contact without expected motion, and current from more than one attributable channel are faults—not completion.

**Sensors and claimed physical effect.** Twelve endpoint circuits and shared voltage/current sensing are permanent. External laser/camera displacement, force gauge, temperature, and independent rail instrumentation remain development ground truth. The claim-defining hypothesis is that using the *same mechanically registered datum* to set tactile travel and generate a pin-side endpoint event removes sensor-to-datum registration error while independent effort evidence separates true endpoint arrival from obstruction. The desired measured result is a lower silent wrong-state rate after manufacture, wear, servo replacement, and reassembly than separate-sensor C3 and current-based C6 at practical Braille geometry.

**Patent attack.** A physical stop that also acts as a limit contact is a familiar machine design. Freedom/Enhanced Vision supplies stops/collars/removable structures; HumanWare supplies cam actuation and position sensing; generic motor art supplies effort/fault classification. An examiner has a strong reason to combine them to detect endpoint arrival and prevent overdrive. Pin-side sensing and dual-purpose datum contact distinguish HumanWare's shaft-angle sensing for anticipation, but may be an obvious relocation/use of a known switch. The hypothesis only improves if data show a non-predictable registration, service, or silent-error advantage over a separately mounted pin sensor and a passive stop. No such data exist.

US subject-matter eligibility is likely favorable for a narrowly claimed electromechanical apparatus and physical control method, but §103 is the dominant attack. At the EPO, endpoint contact, reduced registration error, constrained pin height, and bounded energy are technical effects; the problem–solution analysis still likely combines known teachings unless a surprising effect is proved. In India, claims must be anchored in interacting mechanical/electrical structure to avoid 3(k), and the same-datum cooperation must be real—not a juxtaposition vulnerable under section 3(f). Full enablement requires electrode/shoulder geometry, materials, contact force/resistance, isolation, debounce, contamination/wear limits, practical pitch, manufacturing tolerances, calibration, state thresholds, and failure handling. “Any sensor, any datum, any tactile display” is not enabled.

FTO risk includes the live HumanWare cam/sensor record, Enhanced Vision collar/capture/removable families, related continuations/national rights, generic endpoint-switch claims, and 5559/CHE/2014. Design-around options include direct non-contact pin sensing with an independent machined datum, a different actuator, no current classifier, continuous displacement sensing, or a non-removable guide. That easy design-around limits commercial claim breadth.

**Resources, compatibility, experiments, and disposition.** Incremental prototype allowance: ₹900–₹1,800 for datum-contact parts, small interface PCB, shared current channel, protection, and spares; compute: deterministic finite-state logic and fixed thresholds on the ESP32. Compatibility is low-medium: it retains the architecture but redesigns the guide/pin/datum and therefore belongs on a separate post-MVP coupon. First compare passive stop only, separate direct sensor, stop-contact without current, current without contact, and full VPD-C7. Kill if contact wear/contamination creates false endpoints, added friction or force is unacceptable, practical pitch is infeasible, separate sensors perform equivalently, current supplies no independent diagnostic value, or replacement data do not transfer. Keep all drawings and results confidential until the filing/no-filing gate. Disposition: **redesign before testing; conditional patent lead only**.

## 8. D11: cooperative physical effect or aggregation?

### 8.1 Present conclusion

D11, as described in the attached syntheses, is **not yet shown to be a cooperative combination**. It presently reads as a collection of useful but familiar elements:

| D11 element | Ordinary independent function | Present evidentiary gap |
|---|---|---|
| Mechanical datum | Limits or references travel | No practical-scale tolerance/wear data; no proof it creates a sensing advantage. |
| Per-dot calibration | Compensates unit variation | No held-out transfer across servo swaps, reprints, temperature, or wear. |
| High-bandwidth current | Measures electrical demand/effort | No proof it reveals pin height or distinguishes a correct stop from wrong-height friction. |
| Direct ground truth | Labels development outcomes | No synchronized labelled dataset yet. |
| Completed/incomplete/jammed/Unknown | Prevents forced binary decisions | Thresholds and state validity are not qualified. |
| Bounded retry/isolation | Limits repeated energy/fault propagation | No causal evidence that the chosen retry improves outcomes without harm. |
| Power-aware sequencing | Reduces peak load | No proof of interaction with state verification beyond additive benefits. |
| Replacement acceptance | Restores calibration after service | No repeated-remount evidence and strong modularity prior art. |

The two valid syntheses differ mainly in willingness and timing: the primary synthesis keeps D11 in Track D until stringent evidence exists; the secondary permits an earlier bounded Track B exploration. The final adjudications likewise use D11 as conditional context. They are not votes and are not averaged. Fresh HumanWare and 2026 Enhanced Vision claims strengthen the conservative interpretation.

### 8.2 What current can legitimately mean

Until validated against independent displacement and force labels, servo supply current may indicate only:

- internal DC-motor effort and gear friction;
- the servo controller's response to its own potentiometer error;
- supply voltage, wiring resistance, capacitance, and other active/holding servos;
- temperature, lubrication, manufacturing variation, external finger/load, and wear;
- stall or a disturbance somewhere in the transmission.

It does not identify where the pin is, whether the cam follower remained engaged, whether a guide or printed datum is dimensionally correct, or whether a nominally raised dot has acceptable tactile height. A current spike could be a correct endpoint, a premature obstruction, a gear event, or supply coupling. Therefore current-only completion is prohibited in every simulated claim and test.

### 8.3 Required proof of cooperation

The full or reduced bundle becomes more than aggregation only if a preregistered experiment shows all of the following:

1. the complete combination reduces silent wrong tactile states and unsafe retry energy relative to the strongest calibrated open-loop, direct-sensor, and current-only baselines;
2. removing any asserted indispensable element materially degrades that effect;
3. the effect exceeds the sum or predictable union of the individual improvements, with uncertainty intervals and an interaction analysis fixed before the held-out run;
4. the effect transfers across servo replacement, guide/cam reprint, remount/reassembly, supply and temperature variation, load/friction perturbations, and practical-scale geometry;
5. the improvement is caused by a physical interaction, not post-hoc threshold selection or train/test leakage; and
6. a skilled designer could reproduce the effect from disclosed dimensions, materials, circuits, sampling, thresholds, and failure logic.

VPD-C7 creates a more coherent hypothesis because the same registered component sets the endpoint and emits endpoint evidence. Even so, a stop that doubles as a switch is a familiar construction. Only comparative evidence against a passive stop plus separately mounted sensor can reveal whether the dual-purpose datum has a non-predictable benefit.

## 9. Mandatory patent-case attacks on the surviving hypotheses

C1–C5 are useful baselines or product features but do not survive as independent patent candidates. C6 survives only as a research hypothesis; C7 survives only as a redesign hypothesis.

| Attack | C6 reduced D11 | C7 verified pin-datum | Missing evidence that prevents rebuttal |
|---|---|---|---|
| **Anticipation** | No single reviewed reference found with the exact restricted bundle; unresolved Indian/non-English/unpublished art prevents a conclusion. | No single reviewed claim found with independent servo/cam channels plus dual-purpose pin datum, separate current evidence, and the exact state logic. | Official 5559/CHE/2014 claims/file; full CPC/IPC and citation-chain search; native-language CN/JP/KR review; post-cutoff search. |
| **US obviousness (§103)** | HumanWare cam/sensing + Freedom stop/module + motor-current signature/retry yields a strong predictable combination. | Same combination plus an ordinary endpoint/limit contact; moving sensing downstream to detect backlash is an evident design response. | Unexpected interaction effect, comparative registration error, blind rebuild transfer, and objective secondary indicia—not inventor assertion. |
| **US eligibility (§101)** | Physical current measurement and actuator control likely avoid an abstract-only claim; a broad classifier/data claim remains vulnerable. | Narrow apparatus is plainly physical; method should require actual endpoint circuit events and servo control. | A concrete implemented disclosure; avoid result-only language and generic “AI determines.” |
| **EPO technical effect** | Current/voltage measurement, energy limiting, and mechanism control are technical, but only claim-contributing technical features count. | Constrained travel, endpoint circuit event, and bounded actuation are technical; inventive step remains the main barrier. | Credible effect across the claim scope; comparison with closest HumanWare/Freedom starting point. |
| **India eligibility/patentability** | Section 3(k) risk if framed as classification software; section 3(f) risk if sensor, calibration, and retry merely retain separate functions. | Same-datum mechanical/electrical interaction is the best answer to 3(f), but it is unproved; software must remain tied to physical structure/effect. | Cooperative data; complete specification under section 10(4); current examination practice and relevant court/Controller decisions reviewed by Indian counsel. |
| **Enablement/sufficiency** | One servo/dataset cannot support all servos, tactile cells, environments, or classifiers. | Contact force/resistance, wear, debounce, safety, practical pitch, and manufacturing tolerances are unknown. | Drawings, tolerances, component ranges, code/state chart, datasets, confidence intervals, negative results, and reproducible build/test instructions. |
| **Practical scale** | Macro results do not show usable packing, height, force, or reliability. | Twelve contacts and six actuators may not fit or remain reliable at 2.3–2.5 mm pitch. | Practical-scale coupons, multi-dot interactions, force/height under finger-equivalent load, cleaning and lifecycle data. |
| **FTO/design-around** | Potential HumanWare/Enhanced Vision/generic-control overlap; exact claims and live relatives unresolved. | Adds endpoint contacts but retains cam actuation and collars/stops; unresolved Indian file is material. | Official status/file histories, claim charts for target countries, equivalents analysis, supplier/ownership check, and actual bill-of-material/design freeze. |

The simulation cannot rebut these attacks by assuming the mechanism later works. If the missing evidence is never produced, the attacks stand.

## 10. Tentative claim simulation—not filing-ready claims

These clauses are tools for exposing weak scope, not legal drafting. The supplied frozen architecture does not disclose or enable VPD-C7. A later specification would need new inventor-approved drawings and data, and counsel would need to determine inventorship, priority, disclosure history, and jurisdictional form.

### 10.1 Tentative apparatus independent claim

> **1.** A refreshable tactile cell comprising: a frame defining a plurality of vertical pin guides; a plurality of tactile pins movable in the guides between respective lower and upper endpoints; for each tactile pin, a rotary servomotor, an eccentric cam driven by the servomotor, and a follower coupling the cam to the tactile pin for active movement toward both endpoints; an upper datum and a lower datum mechanically registered to the corresponding guide, each datum being arranged both to constrain travel of the tactile pin at the corresponding endpoint and to produce a pin-side electrical endpoint event by contact with an electrically isolated shoulder carried by the tactile pin; a current-and-voltage sensing channel electrically separate from the endpoint-event circuits and coupled to a supply of the servomotors; and a controller configured to declare an endpoint state only from the corresponding pin-side endpoint event, to use the current-and-voltage sensing channel as effort or supply evidence without declaring the endpoint state from that channel alone, and, upon absent or conflicting endpoint evidence, to assign an incomplete, jammed, or unknown state and apply a bounded retry or isolate the corresponding servomotor.

**Immediate attack.** This is structurally specific enough to avoid a pure result claim, but nearly every block is known. HumanWare supplies motor/cam Braille sensing; Freedom/Enhanced Vision supplies pin guides, collars/stops, and modules; an endpoint contact and current channel are ordinary. The likely difference is the datum/contact location and the rule that endpoint state comes only from pin-side contact. Those differences may be predictable. “Electrically isolated shoulder,” “both endpoints,” and “active movement toward both endpoints” also narrow the claim and invite easy design-arounds.

**First narrowing response.** If a broad rejection is supported, retain only the mechanically registered, dual-function datum plus its demonstrated registration/reassembly effect; remove generic current, retry, and modularity from the independent apparatus claim unless ablation proves they cooperate. If current is non-informative, do not preserve it merely for breadth.

### 10.2 Tentative method independent claim

> **2.** A method of refreshing a tactile pin in a servo-and-cam tactile cell, comprising: receiving a requested upper or lower pin state; driving the corresponding servomotor within a stored per-pin command window to move the tactile pin actively toward a datum that sets a physical endpoint; detecting release of a first pin-side datum contact and assertion of a second pin-side datum contact, the second contact being part of the datum that sets the requested endpoint; measuring servomotor supply current and voltage during the movement as evidence of actuator effort or supply condition; declaring the requested endpoint state only when the second pin-side datum contact is asserted within a qualified interval; when endpoint evidence is absent or conflicts with the electrical measurements, assigning an incomplete, jammed, or unknown state; and permitting no more than a predetermined number of recovery movements before isolating the corresponding channel.

**Immediate attack.** The sequence is a conventional closed-loop endpoint-control method applied to Braille. The strongest potential limitation is that the endpoint-setting datum itself supplies the state event. “One retry,” thresholds, and labels are likely routine. The claim needs physical interaction and measured effect; merely changing state names does not create eligibility or inventiveness.

### 10.3 Dependent fallback set

| Fallback | Proposed limitation | Why it might matter | Weakness/design-around |
|---|---|---|---|
| 3 | Each endpoint datum is a replaceable annular wear member mechanically keyed to the pin guide. | Defines registration and service structure. | Modular/wear parts are crowded; use integral/machined guide. |
| 4 | Contact force is outside the tactile load path except at the endpoint and stays within a disclosed qualified range. | Addresses sensor-induced force/height error. | Needs data; non-contact sensor avoids it. |
| 5 | Per-dot calibration finds the minimum up/down drive window that achieves a contact event under a defined load margin. | Links calibration to actual endpoint. | Routine calibration; direct position control avoids PWM table. |
| 6 | A shared shunt is sampled only in an attributable single-channel transition window with measured background bounds. | Avoids false multi-servo attribution. | Per-channel current sensor or no current channel avoids it. |
| 7 | Current may distinguish overload-like from supply-fault-like events but is prohibited from establishing endpoint completion. | Safety/semantic integrity. | A rule/prohibition may have little patent weight; direct sensor alone avoids it. |
| 8 | Conflicting endpoint contacts force `UNKNOWN`, and only one unload-and-retry cycle is permitted before isolation. | Prevents silent wrong state and repeated energy. | Conventional safety state machine; change retry count. |
| 9 | Replacement/remount invalidates calibration and requires two-end acceptance before the channel re-enters service. | Makes service behavior explicit. | Strong modular/recalibration art; non-removable assembly avoids it. |
| 10 | Six independently driven pins form one Braille cell and use active cam-driven retraction. | Maps to the actual architecture. | Six dots and active drive are known and narrow; not an inventive fallback alone. |
| 11 | A development qualification method synchronizes endpoint contacts, direct tip displacement, force, current, voltage, and requested state, then holds out complete servo/build identities from threshold selection. | Supports reproducibility and guards leakage. | A testing protocol is easy to alter and may not be commercially enforceable. |

### 10.4 Claim-element stress map

| Putative element | Current support | Closest art / difference | Claim-defining experiment | Enablement/FTO/design-around consequence |
|---|---|---|---|---|
| Six independent servo/cam/follower/pin channels | Frozen files support planned architecture, not working performance | Public servo/cam Braille; HumanWare uses motors/cams with a different multi-pin arrangement | Demonstrate active up/down travel and repeatability | Narrow product identity; easily changed; Indian file unresolved |
| Registered upper/lower travel datums | General frozen guides/stops are planned | Freedom/Enhanced Vision collars/stops | Measure endpoint tolerance across prints/wear | Exact geometry needed; risk if capture/plate structures overlap |
| Datum also generates pin-side contact event | **Future redesign only; absent from supplied design** | Generic limit switch + known stop; differs from shaft-angle sensing | Compare dual-purpose datum to passive stop + separate sensor | Central but likely obvious; contactless independent sensor designs around |
| Endpoint declaration only from pin contact | Future firmware hypothesis | Generic closed-loop logic | 3,000 held-out transitions; zero silent wrong states | Result-only wording weak; disclose exact state logic |
| Shared current only as independent effort evidence | D11 research concept, no data | Generic current signature/fault art; Enhanced Vision current control | Incremental-information ablation | Delete if no added value; per-channel or no sensor designs around |
| Incomplete/jammed/Unknown + bounded retry/isolation | D11 concept, no thresholds | Routine fault state machines | Safety/energy and false-isolation tests | Narrow policy; retry count easy to change |
| Replacement acceptance | D11/future concept | Strong modular cell/capture art | Blind swaps and rebuilds | Likely dependent only; claim-map live families |
| Practical-scale operation | Not supported by macro plan | Dense piezo/EM commercial/patent art | Qualified practical-scale coupon and multi-dot cell | Macro data cannot enable practical scope |

**Commercial usefulness if it works.** The narrow value is trustworthy physical-state reporting and service acceptance in a low-cost servo/cam cell—not the servo/cam actuation itself. It could reduce silent tactile errors during education or prototyping. The cost, size, noise, refresh time, wear, and easy non-contact design-arounds may limit licensing value even if a narrow claim survives.

## 11. Evidence program, baselines, and kill gates

### 11.1 Ground-truth stack

Synchronize, with one clock and stable dot/build identifiers:

- requested and commanded state, PWM waveform, servo identity, cam/guide/datum revision;
- direct tip displacement at sufficient resolution to resolve the acceptance band;
- upper/lower endpoint contacts where applicable;
- calibrated force under a defined finger-equivalent load protocol;
- raw unfiltered current and supply voltage at a sampling rate justified by observed transients;
- derived current features kept separate from raw data;
- transition timestamps, retries, resets, brownouts, and fault/state labels;
- temperature, print lot/orientation/material, contamination, wear cycle, replacement/remount/reassembly event, and operator;
- negative, ambiguous, and failed runs without deletion.

The external displacement instrument is the primary development oracle. Contact sensors are candidates under test and may not label themselves as truth until validated.

### 11.2 Mandatory baselines

Run identical randomized transition sets against:

1. fixed common PWM;
2. calibrated open-loop per dot;
3. datum-only;
4. current-only;
5. fixed one-at-a-time refresh;
6. current-aware refresh with no state verification;
7. direct per-dot position oracle/control;
8. full D11 as originally proposed;
9. C6 reduced D11;
10. VPD-C7; and
11. every asserted feature removed in turn.

Critical C7 ablations are: passive datum instead of contact datum; separately mounted direct sensor instead of same-datum contact; current removed; per-dot calibration removed; `UNKNOWN` coerced into a binary result; retry removed; isolation removed; replacement acceptance removed; and fixed sequencing substituted for current-aware sequencing. Guarded bench operation is required for deliberately degraded safety variants.

### 11.3 Preregistered metrics

Before looking at held-out outcomes, freeze:

- raised/lowered displacement bands and force acceptance;
- `completed`, `incomplete`, `jammed`, `Unknown`, and silent-wrong definitions;
- current feature windows and thresholds;
- retry and isolation rules;
- primary endpoint: silent wrong tactile state per transition;
- secondary endpoints: sensitivity/specificity for jam/incomplete, Unknown rate, false isolation, transition time, peak/RMS current, energy, minimum rail voltage, height/force variation, wear drift, and recovery success;
- statistical model, interaction term, confidence intervals, excluded-run rules, and missing-data treatment;
- a held-out split by **entire servo identities, print/rebuild identities, and perturbation conditions**, not random waveform rows from the same unit.

The reports' 97.5% sensitivity and specificity thresholds can be retained as research gates only if accompanied by lower confidence bounds and class-balanced test counts. A high Unknown rate cannot be hidden by calculating accuracy only on classified events.

### 11.4 Test sequence

**Stage 0 — metrology and single-dot proof.** Calibrate instruments. Inspect each SG90-class servo rather than assuming passive return. Prove active up/down motion on one dot; measure no-load and loaded travel, current, force, backlash, and rail droop. Do not add D11 features to rescue a mechanically unreliable channel.

**Stage 1 — C1/C2 observability.** Use at least six servo specimens spanning more than one procurement lot where possible, three independently printed/reassembled guide/cam sets, multiple supply points within the safe qualified range, temperature bands, finger-equivalent loads, friction/obstruction perturbations, and clean/contaminated states. Determine whether current provides repeatable information beyond command, elapsed time, and voltage.

**Stage 2 — C3/C7 mechanism comparison.** Build separate passive-stop, separate-sensor, and dual-purpose-datum coupons. Randomize builds and operators. Measure contact resistance/bounce, registration, added friction, endpoint height, force, debris sensitivity, and failure modes. The frozen MVP remains unchanged.

**Stage 3 — practical-scale transfer.** Produce one-dot and six-dot coupons targeting 2.3–2.5 mm within-cell center spacing and 0.6–0.9 mm raised height as physical reference ranges from ADA signage standards, while clearly labeling the device as a dynamic prototype rather than ADA/ISO compliant. Establish a project-specific force target through direct measurement and user/safety requirements; published 150 mN-class actuator results are comparison data, not a universal standard.

**Stage 4 — replacement/lifecycle.** Blindly replace servos, pins, cams, and guide/datum inserts; remount and reassemble with independent operators. Include cleaning, dust/fiber, wear, thermal cycling, and repeated fingertip-equivalent loading. The architecture report's 100- and 1,000-cycle checks are early engineering screens; a later patent/product assertion needs a longer preregistered lifecycle, provisionally at least 10,000 transitions per stressed channel unless earlier wear justifies a stop.

**Stage 5 — 3,000-transition held-out silent-error test.** Lock hardware, firmware, thresholds, and analysis before running. Use unseen servo/build identities and perturbation combinations. Require zero silent wrong tactile states among 3,000 held-out transitions for the patent re-entry gate; report all Unknown and false-isolation events. Zero observed failures does not prove zero risk: the simple rule-of-three gives an approximate one-sided 95% upper bound of 0.1% per transition at 3,000 zero-failure trials.

### 11.5 Kill, hold, and upgrade rules

**Kill the patent path** if any of these occurs:

- the official Indian file or refreshed search discloses the claim-defining combination in one enabling reference;
- current does not add preregistered held-out diagnostic value or cannot be attributed in the full cell;
- any proposed state uses current alone to certify tactile height/correctness;
- VPD contact causes unacceptable force, friction, bounce, wear, debris sensitivity, or false endpoint events;
- same-datum contact performs no better than passive stop plus separately mounted direct sensing;
- practical-scale packaging or output cannot meet the project acceptance envelope;
- performance fails to transfer after servo replacement, reprint, remount, or reassembly;
- the 3,000-transition test has a silent wrong state, unless a genuinely new mechanism is redesigned and the entire gate is restarted rather than thresholds post-hoc patched;
- claim scope collapses to exact hobby part numbers, macro dimensions, FDM material, a price point, state labels, or an easily avoided retry count; or
- counsel finds a material live-claim FTO obstacle without a commercially acceptable design-around.

**Hold in Track D** if engineering benefits exist but are additive, current is useful only for diagnostics, Unknown/false-isolation rates are impractical, or evidence is confined to macro scale.

**Upgrade to a counsel-led filing evaluation** only if C7 shows a reproducible, non-additive same-datum registration/silent-error effect; passes practical-scale, lifecycle, rebuild, and held-out gates; has reproducible disclosure; and survives refreshed claim-level and FTO review. That upgrade is not a promise to file or to receive a patent.

## 12. Twelve-month evidence and decision roadmap

The sequence protects the semester deliverable. Dates are relative to authorization of the post-MVP research; failed gates stop later patent work but need not stop the semester demonstration.

| Month | Work and evidence | Decision gate |
|---|---|---|
| **0–1** | Freeze MVP requirements and configuration IDs. Inspect passive-return assumption; specify active retraction. Create dated contributor/inventor chronology. Obtain the official 5559/CHE/2014 file and claim/status history through an Indian patent professional. Refresh US/EPO/WIPO/CN/JP/KR searches around cam, output-side contact, travel datum, servo current, jam, service acceptance, and tactile state. | If Indian or other art anticipates the structural core, stop the patent track; continue MVP. |
| **1–2** | Build and commission one frozen-MVP dot with external displacement, force, current, voltage, and time capture. Resolve mechanical feasibility, supply droop, guide friction, and active retraction before predictive sensing. Preserve failures. | No future patent experiment until single-dot up/down motion is stable enough to generate meaningful labels. |
| **2–3** | Complete six-dot macro MVP using staged M1–M8 integration. Establish fixed-PWM and calibrated-open-loop baselines. Do not add C7 hardware to the assessed semester configuration. | Semester design review; freeze MVP CAD/firmware/BOM for traceability. |
| **3–4** | Instrument C2 on a separate single-dot fixture. Preregister current features and held-out identities. Test whether current adds information beyond command, time, and voltage. | If current is non-transferable or height-ambiguous, remove it from any claim core; it may remain a safety/logging channel. |
| **4–5** | Produce C3 separate-sensor oracle and at least two C7 contact-datum geometries. Characterize contact force, electrical isolation, bounce, wear, debris, and measurement alignment. | Select one geometry only if it does not destabilize output and has a plausible practical-scale path. |
| **5–6** | Run passive-stop versus separate-sensor versus same-datum-contact comparison, with and without current. Freeze the state machine and causal interaction analysis before confirmatory data. | If same-datum construction has no distinct physical effect, end C7 patent thesis; keep best engineering sensor. |
| **6–7** | Build practical-scale one-dot coupons, then a six-dot coupon only after the one-dot gate. Measure pitch, height, force, sensor fit, wiring, crosstalk, and assembly yield. | Macro-only success is insufficient. Stop patent re-entry if practical scale fails. |
| **7–8** | Replacement/remount/reassembly study across blinded servo/cam/pin/datum swaps and independent operators. Run voltage, temperature, load, friction, and contamination perturbations. | Require recalibration/acceptance transfer within preregistered bounds. |
| **8–9** | Lifecycle and cleaning study; provisional 10,000-transition stressed-channel target, with interim inspections and failure analysis. Freeze the final candidate and test protocol. | Any systematic false endpoint or wear mechanism triggers redesign and restarts qualification. |
| **9–10** | Run the locked 3,000-transition held-out test on unseen servo/build/perturbation combinations. Calculate silent errors, Unknown, sensitivity/specificity, false isolation, energy, time, and confidence intervals. | Zero silent wrong states is necessary, not sufficient. No threshold repair after outcome inspection. |
| **10–11** | Refresh worldwide patent/NPL search to the current date. Counsel performs claim charts, ownership/status/term review, prosecution-history review, inventorship and disclosure audit, and target-country FTO/design-around analysis. Draft only claims supported by the actual data. | Counsel-led file/no-file recommendation; unresolved material claim/status issue means no filing commitment. |
| **11–12** | Management gate among confidential continued development, a narrowly supported application, trade-secret treatment for non-observable process know-how, or defensive/academic publication after counsel review. Archive a reproducible evidence pack. | Record one reasoned decision and a future search date. No grant representation. |

## 13. Semester evidence preservation and confidentiality

For the frozen MVP, preserve:

- versioned CAD and printable files, actual post-print measurements, guide clearances, cam eccentricity/profile, pin dimensions, cell pitch, and raised/lowered protrusion;
- per-dot PWM commands and calibrated windows, voltage/current waveforms, sampling details, timestamps, requested/commanded states, retries, resets, and faults;
- servo make/lot/identity, replacement/remount/reassembly events, external ground-truth displacement and force, cycle count, wear, temperature, load/friction and contamination condition;
- raw data before filtering, scripts/firmware/commit identifiers, calibration certificates, excluded runs and reasons, negative results, photos/video tied to configuration IDs, and blinded/held-out definitions;
- who conceived each feature, who reduced it to practice, dated alternatives and failures, and any assistance from third parties or tools;
- exact public/private disclosure chronology, including presentations, posters, repositories, demonstrations, papers, vendor discussions, competitions, and sponsor reports.

The MVP and future mechanism must have different configuration identifiers and build folders. A C7 result must never be backfilled into the semester architecture record as though it existed at design freeze.

Treat C7 drawings, contact/datum dimensions and materials, state logic, thresholds, datasets, and comparative results as confidential until counsel completes the novelty/inventorship/disclosure review. Limit access to contributors with a documented need; record every external disclosure. Do not rely on an assumed grace period, especially for India and Europe. If the patent path is killed, consider:

- **trade secret** only for process details that can remain non-public, such as calibration fixtures, acceptance thresholds, and manufacturing controls;
- **defensive publication** for clearly enabled, FTO-reviewed material when preventing later exclusivity is valuable; or
- **academic publication** emphasizing validated engineering evidence and limitations.

A defensive publication or patent filing does not create freedom to operate.

## 14. FTO and design-around control map

| Design area | Red line before commercial prototype | Preferred design-around exploration | Required verification |
|---|---|---|---|
| Motor/cam sensing | Do not copy HumanWare multi-pin camshaft, support-arm, magnet/Hall reference, or claimed arrangement without a chart. | Independent servo per pin; pin-side event downstream of compliance; different support architecture. | US 11,455,910 claims, file history, continuations, equivalents, target-country relatives. |
| Pin stops/modules | Do not assume “collar and plate” or removable block is free because one US record expired. | Integral guide/datum, materially different carrier, or non-capture structure. | US 7,410,359; US 8,690,576 and all related US/EP/WO/JP records/status. |
| Capture/membrane/cleaning | Avoid Enhanced Vision top capture, actuator-dot alignment, membrane, film-indent, and cleaning combinations unless mapped. | Open guide with separate internal protected contacts; alternative debris strategy. | US 12,080,182; US 11,645,948; US 12,548,467; EP 3,884,363; US 12,374,235 and continuations. |
| Current control | Do not claim or implement generic signature, PWM bounce control, polarity reversal, or sensorless position inference without mapping. | Use current only for safety/diagnostics; endpoint state from pin-side evidence; omit current if non-informative. | Generic motor-control search plus Enhanced Vision dependent claims and supplier controller IP. |
| Indian micro-motor/cam concept | No claim-scope or status assumption from the public project discussion. | Do not freeze a commercial cam/pin arrangement until official file review; document independently developed alternatives. | Official specification, claims, publication, prosecution, ownership, renewal/term and any family of 5559/CHE/2014. |
| Software/state logic | Avoid result-only “AI detects jam/correctness” language and unqualified automatic retries. | Deterministic disclosed state machine tied to direct physical events; `UNKNOWN` default. | Current control patents, open-source/software licences, cybersecurity/safety review. |

FTO analysis must be repeated after the actual geometry, circuitry, firmware, bill of materials, manufacturing country, sales countries, and suppliers are frozen. Patentability prior art and FTO are different: an expired or abandoned publication can defeat novelty while presenting no live claim; a live narrow claim can create FTO risk even when the broader idea is old.

## 15. Management forecasts—not grant probabilities

### Optimistic evidence scenario

The frozen MVP works with active retraction. C2 shows current is useful for overload/supply diagnosis but not height. VPD-C7 fits practical pitch, survives wear/contamination, and the same-datum contact materially outperforms a separately mounted sensor after replacement/reassembly. Ablations show a genuine interaction; the 3,000 held-out run has no silent wrong states and acceptable Unknown/false-isolation rates. The Indian file and refreshed search do not disclose the narrow structural core, and counsel identifies a design-around from active claims. Management then evaluates a narrow application focused on the registered dual-function datum and demonstrated physical effect. Examination could still reject, narrow, or invalidate the claims; no grant is promised.

### Base evidence scenario

The MVP is a useful macro demonstrator. Calibration improves repeatability, current diagnoses some stalls but is not transferable enough for completion, and direct pin sensing is the reliable oracle. C7 offers an engineering benefit but a passive stop plus separate sensor performs similarly, or the combination is judged obvious over HumanWare/Freedom/generic control art. Management does not file a mechanism patent. It preserves know-how, completes the semester project, and chooses confidential process controls or an evidence-led publication after FTO review.

### Pessimistic evidence scenario

The servo/cam channel has excessive backlash, load sensitivity, supply coupling, wear, or noise; endpoint contacts add friction or false states; practical-scale packing fails; or the Indian/other search reveals closer claims. Patent work stops promptly. The team does not swap in a roller or electromagnetic concept under the OpenBraille name. It completes or documents the frozen MVP at the achievable level, records negative results, and avoids unsupported patent or performance claims.

## 16. Final recommendation — B. Redesign the prospective mechanism before testing

The sole A–E recommendation is **B: redesign the prospective mechanism before testing**.

The selected future candidate is **VPD-C7**, not the frozen semester MVP and not the original full D11 bundle. Its exact claim-defining hypothesis is a pin-side upper/lower datum that both physically constrains tactile-pin travel and produces the corresponding endpoint event, with six independent servo/cam/pin channels retained. A separate current/voltage channel may classify effort, obstruction-like behavior, or supply fault, but it may never certify pin height or completion. Missing/conflicting evidence produces `UNKNOWN`; recovery is bounded; persistent faults are isolated.

The boundary is strict: build and assess the existing macro six-servo MVP first, with active retraction unless passive return is actually proved. Develop VPD-C7 only on a separate post-MVP coupon; do not alter the assessed architecture, substitute a moving roller or other actuator system, or represent C7 results as MVP results.

The earliest evidence capable of defining a credible claim is not a successful motion video. It is a preregistered comparison showing that the same registered datum/contact produces a reproducible, non-additive physical advantage over (i) a passive datum plus calibrated open loop, (ii) current-only inference, and (iii) a passive datum plus separately mounted direct sensor—followed by practical-scale, wear/contamination, blind replacement/reassembly, and 3,000 held-out transition results with zero silent wrong tactile states. The official 5559/CHE/2014 file and a refreshed professional worldwide claim search must also be resolved.

Allow roughly ₹900–₹1,800 incremental prototype hardware for C7, plus metrology and professional-search/counsel cost, and use the 12-month staged plan rather than compressing it into the semester build. Keep the future CAD, datum/contact details, firmware, raw data, and comparative results confidential until the month 10–11 counsel gate.

Kill the patent path if the dual-purpose datum has no advantage over a separate sensor, current adds no independent diagnostic value, practical-scale or lifecycle testing fails, silent error occurs in the locked held-out gate, transfer after replacement/reassembly fails, a closer reference is found, or useful scope collapses to exact parts/dimensions/materials. Upgrade only to a counsel-led filing evaluation after every technical, search, enablement, and FTO gate passes. Even then, do not promise filing, allowance, validity, enforceability, commercial value, or patent grant.
