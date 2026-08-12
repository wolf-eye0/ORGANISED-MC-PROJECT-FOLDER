# OpenBraille Current Patent Evidence Synthesis

**Evidence date:** 31 July 2026  
**Project:** Project mC — OpenBraille  
**Purpose:** neutral patent-evidence synthesis, adversarial audit, and project decision support  
**Legal notice:** this is technical research, not legal advice, a patentability opinion, a validity opinion, claim construction, or a freedom-to-operate opinion.

---

## 1. Executive verdict

### Primary classification

**Credible path through bounded three-month enhancement.**

- **Track:** **Track B**
- **Confidence:** **moderate-low, 42%**
- **Most important limitation:** the only plausible near-term direction is a *newly integrated, experimentally unproven* physical-control system. Its constituent ideas are individually close to known calibration, mechanical-stop, modular-guide, sensor, and power-management practices. No final claim-language search has yet been performed, and the Indian application `5559/CHE/2014` remains unresolved at the official-record and claim-text level.
- **Should the current frozen MVP alone be treated as the invention?** **No.** The frozen combination of six SG90-class servos, PWM, eccentric cams, followers, vertically translating pins, printed guides, macro scaling, and ordinary character mapping is a useful engineering demonstrator but is not presently supported as a credible patent contribution.

### Board conclusion

The evidence does **not** support patent-first treatment of “a low-cost servo/cam Braille cell,” “a 3D-printed Braille cell,” macro scaling, ordinary per-servo PWM calibration, simple sequential actuation, or modularity by themselves. Rotary raised surfaces driving sliding Braille pins, motor-driven Braille mechanisms, individual translational pins, modular pin guides, travel-limiting plates, replaceable assemblies, low-cost open hardware, and shared-actuator architectures are all established in patent or non-patent prior art.

A conditional path remains only if OpenBraille develops and validates a narrowly integrated architecture that addresses a specific technical defect of heterogeneous commodity actuators rather than merely automating them. The strongest surviving formulation is:

> **Confidential prospective direction:** a per-dot tolerance-compensation and verified-refresh architecture for heterogeneous low-cost rotary actuators, combining mechanically bounded tactile-pin travel, stored actuator-specific operating windows, controlled sequential electrical-signature measurement, positive up/down state verification, and fault-aware refresh sequencing that demonstrably reduces out-of-spec tactile states, stalls, retraction failures, or supply-induced errors relative to fixed-PWM servo control.

This is an **invention-development hypothesis**, not a patentability conclusion. It survives because no reviewed independent claim clearly recites that exact physically anchored combination for a low-cost refreshable Braille cell. It remains highly vulnerable to obviousness unless the combined system produces a reproducible and material technical effect that would not be expected from routine servo setup.

### Decision consequence

- Build the frozen MVP.
- Do not file on the frozen MVP as such.
- Integrate only the bounded measurement and verification features needed to test the prospective direction.
- Keep new geometry, calibration data, control logic, and results confidential until institutional IPR review.
- Kill or downgrade the patent path promptly if the named evidence gates in Sections 18 and 22 fail.

---

## 2. Input inventory

### 2.1 Control result

The attached set contains **18 files**, matching the manifest’s expected count:

- 1 governing instruction;
- 10 numbered project/historical inputs, `01` through `10`;
- 6 independent current patent-research reports, `11` through `16`;
- 1 manifest.

The governing instruction is readable. Every required project-authority file is readable. The stop condition is therefore **not triggered**.

### 2.2 File-by-file inventory

| No. | Uploaded file | Normalized role | Classification | Readability / control finding |
|---:|---|---|---|---|
| 00 | `00_READ_FIRST_OpenBraille_Synthesis_Instructions(3).md` | Governing synthesis specification | Governing authority | Readable and internally complete; uploaded-name suffix is non-substantive. **Control discrepancy:** actual uploaded size is 16,780 bytes and SHA-256 is `b487647fb66611fa626ab2115f3b30e9d5e14398e02bbf430ade127d957af2ad`, whereas the manifest records 18,120 bytes and SHA-256 `9037c212…`. The actual readable upload is used as governing, and the mismatch is retained as a provenance warning. |
| 01 | `01_Engineering_Design_Review(4).md` | Engineering Design Review | Current project authority, priority 1 | Present and readable. |
| 02 | `02_Project_mC_Decision_Register_v1.2(4).md` | Project mC Decision Register v1.2 | Current project authority, priority 2 | Present, readable, and expressly version **1.2**. No v1.1 file is supplied. |
| 03 | `03_Phase3C_Portfolio_Closure_Memo_Approved(4).md` | Approved Phase 3C closure memo | Current project authority, priority 3 | Present and readable. |
| 04 | `04_Phase3C_OpenBraille_Architecture_Report_Final(4).md` | Final OpenBraille architecture | Current project authority, priority 4 | Present and readable. |
| 05 | `05_Phase3C_OpenBraille_Memory_Final(4).md` | Final OpenBraille memory | Current project authority, priority 5 | Present and readable. |
| 06 | `06_Phase3C_OpenBraille_SOP_Final(4).md` | OpenBraille Phase 3C SOP | Current project authority, priority 6 | Present and readable. |
| 07 | `07_Concept_Evidence_Matrix(4).md` | Concept evidence matrix | Validated evidence file | Present and readable. Filename numbering differs from the internal historical source key, but identity is unambiguous. |
| 08 | `08_Uncertainty_and_Test_Register(4).md` | Uncertainty and test register | Validated evidence file | Present and readable. Filename numbering differs from the internal historical source key, but identity is unambiguous. |
| 09 | `09_Patent_Research_Input_Pack(4).md` | Patent research input pack | Search-preparation evidence | Present and readable; expressly a lead pack, not a patent conclusion. |
| 10 | `10_Phase2_Report_by_Claude(4).md` | Historical Phase 2 synthesis | Historical search leads only | Present and readable; not treated as current verified patent truth. |
| 11 | `11_OpenBraille_Patent_Research_ChatGPT_DR(2).md` | ChatGPT Deep Research | Independent current research | Present and readable. |
| 12 | `12_OpenBraille_Patent_Research_Gemini(2).docx` | Gemini Deep Research | Independent current research | Present, readable, and text-extractable. |
| 13 | `13_OpenBraille_Patent_Research_Perplexity(2).docx` | Perplexity Deep Research | Independent current research | Present and readable, but **partial**. Substantive text ends in Section 8.2, “Low-Cost Per-Dot Calibration,” and then changes to references. No complete final verdict is present or inferred. |
| 14 | `14_OpenBraille_Patent_Research_Qwen(2).md` | Qwen Deep Research | Independent current research | Present and readable. |
| 15 | `15_OpenBraille_Patent_Research_Mistral(2).md` | Mistral | Independent current research | Present and readable. |
| 16 | `16_OpenBraille_Patent_Research_Microsoft_Copilot(2).docx` | Microsoft Copilot | Independent current research | Present, readable, and text-extractable. |
| 99 | `99_INPUT_MANIFEST(2).md` | Input manifest | File-control checklist only | Present and readable. Not used as technical evidence. |

### 2.3 Required confirmations

1. **Total attached files:** 18 — confirmed.  
2. **Governing instruction readable:** yes — confirmed, with the manifest hash/size discrepancy noted.  
3. **All project/historical files 01–10:** present and readable.  
4. **All six independent reports:** present and attributable to ChatGPT Deep Research, Gemini Deep Research, Perplexity Deep Research, Qwen Deep Research, Mistral, and Microsoft Copilot.  
5. **Decision Register:** v1.2 is present; v1.1 is not used.  
6. **Perplexity:** partial, ending during §8.2 without a final verdict; no missing conclusion is inferred.  
7. **Missing / duplicate / unreadable:** no required file is missing or unreadable; no byte-identical duplicates were found. Upload suffixes `(2)`, `(3)`, and `(4)` are naming artifacts, not substantive ambiguity. The governing-file hash/size mismatch is the only material file-control discrepancy.

---

## 3. Research-report reliability audit

The reports were audited separately. Model reputation and apparent confidence were ignored.

| Report | Reliability assignment | Retained value | Material defects and exclusions |
|---|---|---|---|
| **ChatGPT Deep Research** | **Medium reliability — highest usable report in this set** | Strong concept fidelity; explicit separation of disclosure, claim scope, database-reported status, prior-art relevance, and FTO relevance; claim-first analysis of several close records; candid Indian and status limitations; coherent three-month experiment path. | Still relies materially on Google Patents/family navigation for several statuses; national status was not professionally docket-verified; the proposed integrated direction has not been searched using final claim language; some family coverage is broader than direct official verification. No conclusion is accepted merely because this report reached it. |
| **Gemini Deep Research** | **Low reliability; Indian/legal-status sections excluded** | Useful search terms, mechanism categories, and experimental ideas where independently corroborated. | Treats the unresolved Indian filing as a settled fatal or public-domain event at different points; overstates “zero novelty” and FTO conclusions without complete claim charts; mixes publication disclosure with blocking claim scope; citation/extraction traceability is inconsistent. Its final Track C label is not adopted by vote. |
| **Perplexity Deep Research** | **Low reliability and partial** | Broad list of potentially relevant families and candidate directions through §8.2; useful as a lead index only. | No complete verdict. Several family/status assertions lack official support; some identifiers and relationships require correction; claim and status confidence is too high for the available sources. Everything after the actual substantive stopping point is excluded; no conclusion is reconstructed. |
| **Qwen Deep Research** | **Low reliability; retained only in corroborated engineering portions** | Highlights compliant printed guides and manufacturability as testable engineering questions. | Relies on weak or tertiary sources for load-bearing assertions; mischaracterizes or conflates some patents; poor claim traceability; presents an “exhaustive” search without a reproducible official-record trail; compliant-guide proposal is largely ordinary mechanical optimization absent unexpected results. |
| **Mistral** | **Low reliability; status and Indian conclusions excluded** | Useful structured candidate list, experiment framing, and recognition that the frozen MVP is not the patent target. | Repeatedly calls `5559/CHE/2014` a blocking disclosure despite no claim text or official status; makes overconfident assignee, expiry, and family statements; sometimes treats project allegations as patent facts; its 8.5/10 confidence is unsupported by the acknowledged gaps. |
| **Microsoft Copilot** | **Low reliability; Indian conclusion excluded** | Concise identification of manufacturing and control directions; recognizes conditionality. | Shallow claim analysis; says `5559/CHE/2014` is expired/non-blocking without an official record; includes inaccurate family associations found in other reports; conflates mechanism-space density with claim coverage; limited reproducibility. |

### 3.1 Conflict resolution

The principal report conflict is not “Track B versus Track C.” It concerns what technical contribution, if any, remains after the frozen MVP is removed from the invention hypothesis.

The evidence supports these resolutions:

- The **frozen MVP is not a credible Track A invention**.
- Ordinary calibration, sequential servo driving, FDM printing, macro scaling, or modularity alone are too close to routine engineering or known art.
- A **bounded integrated physical-control enhancement** remains testable within three months, so the project is not automatically forced to Track C.
- Broader standard-scale manufacturability, shared actuation, or actuator reduction are Track C or major-redesign paths, not the present primary classification.
- The unresolved Indian filing increases uncertainty but cannot be treated either as an active blocker or as expired/non-blocking without the official record and claims.

---

## 4. Search coverage and evidence gaps

### 4.1 Coverage achieved

The audit independently reviewed or re-checked:

- rotary disk / raised-surface mechanisms acting on sliding Braille pins;
- independent translational pin systems;
- impact-driven, friction-held pin arrays;
- layered electromagnetic and bistable magnetic systems;
- modular pin blocks, removable capture/top assemblies, travel-limiting plates, and repairability;
- SMA/compliant mechanisms;
- shared-actuator and moving-write-head architectures;
- macro-scale and standard-scale open-hardware systems;
- public servo-, stepper-, cam-, and micro-motor projects;
- candidate calibration, state-verification, sequencing, manufacturing, and scale-transfer directions.

The mandatory named leads were reviewed at least to the level needed to classify their technical and legal relevance. The closest records were inspected at independent-claim level where retrievable.

### 4.2 Material gaps

1. **Indian application `5559/CHE/2014`:** no official bibliographic record, publication, complete specification, claims, examination history, or current legal status was retrieved. Only public third-party statements confirm the asserted number, filing date, applicant name, and alleged scope. All legal conclusions remain unresolved.
2. **Official national legal status:** complete live status was not independently certified for every US, EP-validation, Canadian, Japanese, Korean, Chinese, and Indian family member. Database labels are screening evidence, not legal opinions.
3. **Current control/calibration art:** final claim-language searching has not been conducted for the proposed integrated enhancement. Search terms such as actuator-specific operating window, electrical-signature state inference, jam detection, endpoint calibration, tactile-pin verification, and fault-aware refresh must be repeated across patents and embedded-control literature after the design is frozen.
4. **OpenBraille data:** no measured force, travel, pin-height distribution, retraction reliability, current waveform, stall signature, cycle life, print-yield, or tactile-user evidence exists yet.
5. **Scale bridge:** no practical-scale cell, detailed tolerance stack, finite-element or kinematic analysis, or manufacturing-yield study connects the 300% prototype to standard Braille dimensions.
6. **FTO geography:** the intended countries for manufacture, use, sale, export, and deployment are not fixed. FTO is jurisdiction- and date-specific.
7. **Inventorship/public disclosure:** no controlled invention log has yet separated pre-existing public MVP content from new confidential improvements.

### 4.3 Status language used in this report

- **“Granted/publication confirmed”** means the grant/publication event is visible in the retrieved record.
- **“Database-reported active/expired/abandoned”** means the database displays that label with its own legal-status disclaimer; it is not a certified opinion.
- **“Unresolved”** means the available record is insufficient for a load-bearing legal conclusion.

---

## 5. Verified patent-family ledger

The ledger focuses on materially relevant families. “FTO significance” does not mean infringement; it identifies whether a later claim chart may be needed.

| Family / record | Earliest priority; applicant/assignee | Jurisdictions and status as verified | Independent-claim subject | Relevance to OpenBraille | Novelty significance | FTO significance | Confidence / primary source |
|---|---|---|---|---|---|---|---|
| **US20130149674A1 / US8483018B2 — Braille watch** | 8 Dec 2011; Wisconsin Alumni Research Foundation | US grant confirmed 9 Jul 2013; Google database reports fee-related expiry | Rotating disk with raised surface under sliding pins in top-plate holes; actuator rotates disk to form Braille number | Very close kinematic relationship: rotary raised surface/cam, sliding tactile pins, actuator; specification expressly identifies servo and PWM examples | Strong prior art against broad “servo rotates cam/disk to raise Braille pins” concepts | Database-reported lapse reduces present US FTO concern, but status should be professionally confirmed | **High technical / medium status**; [record](https://patents.google.com/patent/US8483018B2/en) |
| **US20130017516A1 — Active Braille timepiece** | 11 Jul 2011; Kelly Tyler | US publication confirmed; database reports abandoned | Active translational Braille pins controlled by processor/actuators; cam-related embodiments appear in disclosure | Prior art for individually controlled moving tactile pins and electronic translation/control; narrower direct claim mapping than the Braille-watch disk | Relevant to novelty/obviousness even if abandoned | Little present FTO weight if abandonment is confirmed; no issued US claim identified | **Medium**; [record](https://patents.google.com/patent/US20130017516A1/en) |
| **US11854423B1 — Refreshable Braille display** | 19 May 2020; Prithu and Pramod Kolar | US grant confirmed 26 Dec 2023; database reports active | Pins in through-perforations are impacted between front/rear positions and passively held by friction; system claims include controller and impact driver | Different actuation, but highly relevant to pin guidance, passive state holding, arrays, 3D-printable body, and moving impact-driver concepts | Crowds friction-based state retention and impact-written arrays | Active US claims may matter if OpenBraille adopts friction-latched bidirectional pins or a moving impact driver | **High technical / medium status**; [record](https://patents.google.com/patent/US11854423B1/en) |
| **WO2016074170 / US11410574B2 — layered electromagnetic display** | 12 Nov 2014; Zhejiang Sci-Tech University | US grant confirmed 9 Aug 2022; WO publication/family confirmed; database reports US active | Three-layer Braille module and touch panel; dependent claims define coil, iron core, articulated driving block, reset spring and pin | Not close to servo/cam; demonstrates dense claimed territory for layered electromagnetic cells and reset mechanics | Strong prior art against a broad “low-cost electromagnetic replacement” pivot | Relevant only if redesign enters the claimed layered electromagnetic architecture | **High technical / medium status**; [US record](https://patents.google.com/patent/US11410574B2/en) |
| **WO2020106855 / EP3884363B1 / related US, CA, JP, KR family — electromagnetic refreshable reader** | 20 Nov 2018; Tactile Engineering / successor lineage | WO publication confirmed; EP grant publication confirmed 6 Aug 2025; family entries in US, CA, JP, KR are visible; national live status not fully certified | Bistable magnetic tactile actuator, coil/stator structures, compact high-density circuitry, removable cleanable top enclosure, and associated control/manufacturing features | Important adjacent family for magnetic latching, calibration by pulse energy, removable top assemblies, manufacturing tolerances, and dense arrays | Crowds magnetic, modular, removable, and actuator-energy optimization directions | High FTO screening importance for any later EM-latching or removable capture assembly; low direct overlap with six servo/cams | **High technical / medium status**; [WO record](https://patents.google.com/patent/WO2020106855A1/en), [EP record](https://patents.google.com/patent/EP3884363B1/en) |
| **US11915607B2 — Modular refreshable Braille display system** | 29 May 2020; Brailleazy Inc. | US grant confirmed 27 Feb 2024; database reports active | Mobile-device case with contact surface, cavities, movable Braille pins, and controller; dependent claim permits removable cavities | Shows that “modular” and “removable” must be tied to specific structure; its main claim is a mobile-device case, not all modular Braille cells | Limits broad claims to removable cavities/modules but does not anticipate the frozen servo/cam cell by itself | Relevant if product is a mobile-device case or copies claimed cavity/controller arrangement | **High technical / medium status**; [record](https://patents.google.com/patent/US11915607B2/en) |
| **US11645948B2 / US12080182B2 — capture plate assembly** | 10 Mar 2020; Freedom Scientific / Enhanced Vision Systems lineage | US grants confirmed; database reports active | Capture plate with display dots, separate top assembly with Braille dots, intervening membrane, and capacitive touch layer; removable variants are dependent | Relevant to self-alignment, separated top assemblies, cleaning, capture plates, and verification surfaces; independent claim is much more specific than “a guide plate” | Crowds removable/self-aligning top-plate concepts when combined with membrane and capacitive layer | Requires claim chart only if OpenBraille adopts comparable capture/top/membrane/capacitive architecture | **High technical / medium status**; [record](https://patents.google.com/patent/US12080182B2/en) |
| **WO2013130534 / US8690576B2 / related EP, JP family; US9424759B2 continuation** | 30 Jan 2004; Freedom Scientific | US grants and international family confirmed; database reports US patents expired by lifetime | Modular mounting blocks containing tactile pins; plate limits upward travel; removable cell assemblies and manufacturing/alignment methods. Continuation claims user controls/display housing | Particularly relevant to modular pin blocks, repairability, travel-limiting plates, tolerance-stack reduction, and alignment fixtures | Strong prior art against generic modular replacement, guide blocks, or hard-stop claims | US expiry reduces current US FTO concern if verified; foreign historical rights require date-specific confirmation | **High technical / medium status**; [US8690576](https://patents.google.com/patent/US8690576B2/en), [US9424759](https://patents.google.com/patent/US9424759B2/en) |
| **WO2015189863 — IIT Delhi compliant SMA Braille cell** | 10 Jun 2014; Indian Institute of Technology Delhi | WO publication confirmed; PCT database reports ceased; national rights were not comprehensively established | Five-layer or half-cell architecture with SMA wires, cantilever strips, latching and snap-fit alignment | Different actuator, but strong prior art for compliant amplification, latching, layered cells, modularity, easy assembly and cap alignment | Crowds compliant guide/return and snap-fit modularity as broad concepts | FTO is redesign-specific and national status remains unresolved | **High technical / low-medium status**; [record](https://patents.google.com/patent/WO2015189863A2/en) |
| **EP4049116B1 — Tactile pixels** | 22 Oct 2019; University of Bath | EP grant publication confirmed 1 May 2024; database reports active | Multiple magnetic cantilever taxels with different mechanical resonances driven selectively by frequency inputs to a shared solenoid | Important for shared actuation, resonance-addressing, printed cantilevers and actuator reduction; **not** part of the IIT Delhi SMA family | Strong adjacent art against frequency-addressed shared-solenoid taxels | Relevant only for a major redesign toward shared solenoid/resonant taxels | **High technical / medium status**; [record](https://patents.google.com/patent/EP4049116A1/en) |
| **US6881063B2 / WO2004077379 — electroactive-polymer Braille cell** | 24 Feb 2003; Peichun Yang / Freedom Scientific lineage | US grant confirmed; database reports expired by lifetime | Fluid-tight housing, diaphragm/support structures and electroactive-polymer bending elements driving tactile output | Different actuator; relevant to latching, compact cell construction and physical support architecture | Prior art against broad low-voltage polymer/compliant actuator claims | Low current FTO concern in US if expiry is confirmed; still prior art | **High technical / medium status**; [record](https://patents.google.com/patent/US6881063B2/en) |
| **US5685721A — SMA Braille cell** | 1994 priority period; assignee shown in record | US grant/publication historical; database reports expired | SMA actuation of refreshable Braille pins | Early evidence that substituting SMA for piezo is old | Strong novelty/obviousness prior art for SMA substitution | Low current FTO significance if expiry confirmed | **Medium-high**; [record](https://patents.google.com/patent/US5685721A/en) |
| **US6743021B2 — flexible-surface/MEMS Braille display** | 1998 priority period | US grant confirmed; database reports expired/fee-related or lifetime depending record | MEMS/valve actuation beneath continuous elastomeric tactile surface; modular row/column concepts in disclosure | Different mechanism but important background for low-cost arrays, continuous surfaces, and multiplexing | Prior art against broad array/manufacturing/system concepts | Low present FTO weight if expiry confirmed | **Medium-high**; [record](https://patents.google.com/patent/US6743021B2/en) |
| **US6692255B2 — bidirectional relative movement tactile display** | 1999 priority period | US grant confirmed; historical status database-reported expired | Moving actuator assembly relative to pin array in either direction; static position retainer; shared actuators and motor/controller | Directly relevant to shared-actuation and actuator-reduction proposals | Strong prior art against a generic moving write head/shared-actuator array | Low present FTO weight if expiry confirmed; important obviousness art | **High technical / medium status**; [record](https://patents.google.com/patent/US6692255B2/en) |
| **US7410359 and related Freedom Scientific tactile-cell family** | 30 Jan 2004; Freedom Scientific | Family and grants confirmed; exact live status varies by member and date and was not professionally certified | Electromechanical tactile cell assemblies, contact alignment, replaceable construction and associated manufacturing | Relevant to assembly fixtures, modular cells, stops and repairability | Crowds ordinary assembly/manufacturing refinements | Claim chart needed for a product that copies the specific cell/contact architecture; less direct for servos | **Medium**; [family lead](https://patents.google.com/patent/US7410359B1/en) |
| **US6902403 and other historical motor/cam Braille leads** | Historical | Exact claim/status confirmation was incomplete in this audit | Reported motorized/mechanical Braille structures | Search leads for rotary/mechanical cell art | Reinforces crowded mechanism background but not used as a sole load-bearing finding | Unresolved until exact record/claims verified | **Low-medium / unresolved** |
| **Indian `5559/CHE/2014`** | Publicly asserted filing 5 Nov 2014; Paul D’Souza | **Official publication, claims, prosecution and current status not retrieved** | Third-party statements allege micro-motor pins, cantilevers, mechanical rotation stops, rotors/cams, direct or interposed lifting and selectors | Potentially extremely close to the frozen mechanism, but only as an allegation until the file is obtained | Cannot be used as a verified anticipation finding; public statements themselves are relevant search leads and may be prior public disclosure depending dates/content | Cannot be called active, expired, abandoned, blocking or non-blocking | **Low official confidence; unresolved**; [public project statement](https://hackaday.io/project/10849-refreshable-braille-display) |

### 5.1 Ledger correction of report errors

- `EP4049116` is the University of Bath **Tactile pixels** family and is **not** the European phase of `WO2015189863`.
- `US11410574B2` belongs to the Zhejiang layered electromagnetic family, not the IIT Delhi SMA compliant-mechanism family.
- PCT “ceased” status does not establish that all national family members are dead.
- A Google “active,” “expired,” or “abandoned” label is not a substitute for official docket verification.
- The main independent claim of `US11915607B2` is a mobile-device case, not an actuator-neutral monopoly over all modular refreshable Braille displays.

---

## 6. Closest independent-claim analyses

### 6.1 US8483018B2 — rotating disk under sliding pins

Independent claim 1 requires a Braille watch with a disk having a raised surface, multiple pins sliding in holes of a top plate, and an actuator rotating the disk so portions of the raised surface elevate selected pins. This is the closest verified issued claim to OpenBraille’s fundamental rotary-to-linear tactile-pin relationship.

**Overlap with frozen MVP:** rotary actuator; rotary raised surface/cam; guided sliding pin; tactile protrusion; electronic actuator control.  
**Differences:** watch/time display; one disk controls multiple numeric pins; OpenBraille uses one eccentric cam and one servo per dot; six-dot character mapping; macro printed cell.  
**Effect:** those differences prevent a simplistic identity conclusion, but they make broad “servo-driven cam raises Braille pin” novelty very weak and create a strong obviousness combination.

### 6.2 US20130017516A1 — active translational pins

The publication describes processor-controlled translational Braille pins and active timepiece output. The application is database-reported abandoned, so no issued US claim was identified. The disclosure remains prior art.

**Overlap:** individually controllable moving tactile pins, processor mapping, active refresh.  
**Difference:** timepiece and disclosed mechanisms differ from six independent SG90/cams.  
**Effect:** reinforces that independent pin control and text/time conversion are not new.

### 6.3 US11854423B1 — friction-held, impact-driven pins

Independent claim 1 requires pins in perforations that can be impacted between front and rear protruding positions and are passively held by friction. The system claim adds a controller and a movable impact driver.

**Overlap:** guided pins, array, raised/lowered tactile pattern, controller, sequential actuation.  
**Difference:** bidirectional impact and friction latching rather than continuous servo/cam positioning.  
**Effect:** not an anticipation of the frozen MVP, but important against later proposals involving passive friction retention, a moving write head, printed pin bores, or actuator reduction.

### 6.4 US11410574B2 — layered electromagnetic cell

Independent claim 1 is a particular three-layer module and touch-panel arrangement. Electromagnetic driving details appear in dependent claims.

**Overlap:** six-dot Braille cells, controller, moving pins, reset.  
**Difference:** layered electromagnetic components, coil/core, spring, articulated driving block; no commodity servo/cam.  
**Effect:** the record does not block the frozen servo architecture merely because both are Braille displays. It strongly limits a future pivot to layered electromagnetics.

### 6.5 WO2020106855 / EP3884363 family — bistable electromagnetic reader

The family discloses and claims dense electromagnetic actuation, permanent-magnet bistability, coil/stator geometry, removable cleanable enclosures, manufacturing alignment, pulse-energy control, and high-density circuitry. Exact claim sets vary by jurisdiction.

**Overlap:** tactile pins, per-dot actuation, pulse control, manufacturing tolerances, maintenance and possible calibration.  
**Difference:** bistable magnet/coil mechanism rather than servo/cam; full-array packaging.  
**Effect:** a later claim to “calibrating energy for reliable tactile movement” may face this family and analogous solenoid/servo art. The OpenBraille direction must be tied to its distinctive physical problem and measured effect, not generic calibration.

### 6.6 US8690576B2 — modular pin blocks and travel limiting

Independent claims include releasable mounting blocks holding tactile pins as modular units and a plate limiting upward travel. Other claims cover removable cell assemblies and alignment/manufacturing structures.

**Overlap:** pin guide/block, modularity, hard travel limit, repairability, tolerance management.  
**Difference:** piezoelectric cell assemblies and multi-cell commercial display.  
**Effect:** a generic “printed modular guide with hard stop” is not a strong invention direction. Any OpenBraille distinction must involve a non-routine interaction between geometry, actuator-specific control and verified tactile state.

### 6.7 US11915607B2 — mobile-device-case display

Independent claim 1 requires a mobile-device case, an exposed contact surface, cavities with movable Braille pins, and a controller responding to the fitted mobile device. Removable cavities appear in a dependent claim.

**Effect:** it is a narrower product architecture than several reports implied. It is relevant to removable modules but does not establish that modularity in all Braille displays is actively claimed.

### 6.8 US12080182B2 — capture/top/membrane/capacitive assembly

Independent claim 1 requires a capture plate with display dots, a top assembly with Braille dots, a membrane physically separating the two, and a capacitive touch layer. Removability is dependent.

**Effect:** a simple printed guide plate is not automatically within this claim, but a future tactile-state sensing top assembly using a membrane/capacitive layer must be claim-charted carefully.

### 6.9 US6692255B2 — moving shared actuator

Independent claim 1 requires a pin display and actuator/display relative movement in either direction; further claims cover static retainers, motors, controllers and shared actuator sets.

**Effect:** shared actuation is not a clean white space. It remains a long-term engineering possibility but is a crowded Track C redesign.

---

## 7. Frozen-MVP closest-art feature chart

Terms are restricted to the governing vocabulary: expressly disclosed, necessarily implied, arguably suggested, absent, or unresolved.

| Frozen-MVP feature | Braille-watch disk family | Active-timepiece publication | Friction-impact family | Freedom Scientific modular family | Public motor/cam projects | Audit conclusion |
|---|---|---|---|---|---|---|
| Six independent commodity servos | Specification expressly identifies servo/PWM examples, but not six one-per-dot SG90 units | Actuator plurality arguably suggested | Absent | Absent | Expressly disclosed in public prototypes in related forms | Exact six-SG90 arrangement may be absent from one claim, but is an obvious implementation choice, not a credible inventive distinction. |
| Direct PWM | Expressly disclosed in specification | Arguably suggested by ordinary actuator control | Absent | Absent | Expressly disclosed in servo projects | Conventional. |
| Eccentric cam / rotating raised surface | Expressly disclosed as disk raised surface; cam relationship necessarily implied | Cam embodiments reported in disclosure | Absent | Absent | Expressly disclosed | Core kinematics are old. |
| Follower | Necessarily implied by pin contacting raised surface | Arguably suggested | Absent | Pin/actuator contact structures disclosed | Expressly or necessarily implied | Conventional mechanical interface. |
| Vertically translating tactile pin | Expressly disclosed | Expressly disclosed | Expressly disclosed | Expressly disclosed | Expressly disclosed | Old. |
| Printed frame and guide | Material-neutral claims; printing not required | Absent | 3D printing appears in disclosure | Molded/modular guides disclosed | Expressly disclosed | 3D printing alone is not inventive. |
| Macro-scale construction | Absent in claims | Absent | Standard spacing preferred | Commercial scale | Public prototypes often enlarged | Macro scaling is a prototyping tactic; no patent weight by itself. |
| Active cam retraction | Raised-surface position and springs disclosed | Active translation disclosed | Bidirectional impact | Piezo return/stop architecture | Public projects disclose active reset variants | Arguably suggested or express in adjacent art. |
| Per-dot calibration | Ordinary actuator positioning arguably suggested; not central claim | Arguably suggested | Absent | Manufacturing alignment disclosed | Common servo practice | Calibration alone is routine unless physically anchored and technically exceptional. |
| Current-aware sequencing | Absent from closest independent claims | Absent | Sequential impact expressly disclosed, not current-aware | Absent | Common power-management practice | Potential supporting element, weak standalone direction. |
| Modularity/replacement | Absent | Absent | Body/frame; not core modular cell | Expressly disclosed | Expressly disclosed by MOLBED/MagnePins and projects | Crowded. |
| Tactile-state verification | Absent | Absent | Pin state is physical but verification not central | Touch/capture families disclose sensing structures | Some projects test state/performance | Possible differentiator only in a specific integrated architecture. |
| Tolerance compensation | Mechanical top plate and geometry imply tolerance handling | Absent | Friction bore dimension necessarily matters | Expressly addresses tolerance stack and alignment | Open hardware addresses print tolerance | Generic tolerance design is old; actuator-specific control interaction may remain testable. |
| External 5 V power / decoupling | Ordinary and absent from claims | Ordinary | Ordinary | Ordinary | Expressly common | No inventive weight. |
| Character-to-dot mapping | Necessarily implied or express | Expressly disclosed | Expressly disclosed | Expressly disclosed | Expressly disclosed | Old. |
| Tactile/mechanical validation | Not a device element | Not a device element | Performance testing implied | Manufacturing/performance testing known | Expressly performed in projects | Evidence method may support claims but is not itself necessarily an invention. |

### 7.1 Feature-chart conclusion

No single verified issued claim was shown to contain every literal frozen-MVP element. That does **not** establish inventive step. The frozen MVP is a predictable aggregation of known tactile-pin kinematics, commodity servo control, printed prototyping, ordinary mapping, and standard power practices.

---

## 8. Indian application 5559/CHE/2014 investigation

### 8.1 Confirmed

The following was confirmed only from dated public third-party project material:

- a public statement identifies application number `5559/CHE/2014`;
- the statement says it was filed at the Chennai Patent Office on 5 November 2014 by Paul D’Souza;
- the statement alleges coverage of micro-motor-actuated pins, cantilevers, mechanical stops limiting rotor rotation, motors with rotors or cams mounted vertically or horizontally, direct or interposed pin lifting, and a low-force selector;
- the public open-hardware team stated that it discontinued its then-current actuation approach after receiving that assertion.

These statements are useful search leads and evidence that motor/cam Braille mechanisms were publicly discussed by 2016. They are **not substitutes for the patent file**.

### 8.2 Not confirmed

The audit did not retrieve from an official Indian source:

- a publication number;
- title and bibliographic record;
- complete specification;
- claims;
- applicant/inventor details beyond the third-party assertion;
- examination report;
- amendments;
- grant, refusal, withdrawal, abandonment or lapse;
- renewal status;
- family members;
- territorial scope.

### 8.3 Required conclusion

`5559/CHE/2014` must be classified **unresolved**.

It cannot responsibly be described as:

- a blocking patent;
- an expired patent;
- an abandoned application;
- public-domain technology;
- non-blocking;
- a verified anticipation of OpenBraille.

### 8.4 Practical consequence

Because the alleged scope is unusually close to OpenBraille’s core mechanism, obtaining the official file is a **pre-filing and pre-commercialization gate**. The project may continue as a confidential student prototype, but no patent or FTO conclusion should rely on either optimistic or pessimistic assumptions about this application.

---

## 9. Non-patent prior art

### 9.1 MOLBED

MOLBED publicly describes a modular low-cost electronic Braille character with magnetic state retention, low part count, reproducibility, scalability, and an explicit decision not to patent the system. It is material prior art for low-cost objectives, modular cells, magnetic retention, and open manufacturing. It does not anticipate the exact servo/cam architecture, but it weakens broad claims to affordability, modularity, or simple state retention. [Project source](https://www.madaeon.design/portfolio/molbed-2016-2019/)

### 9.2 MagnePins

The 2025 MagnePins work describes a 24×89, approximately 2.5 mm-pitch, makerspace-fabricable tactile display using a moving carriage, staggered electromagnetic actuators, printed locking channels, and measured accuracy up to 99.97%. It is highly relevant to actuator reduction, standard-scale feasibility, open fabrication, locking channels, and quantified validation. It materially raises the bar for any claim that low-cost, makerspace-built, standard-scale tactile arrays are unexplored. [Monash publication](https://research.monash.edu/en/publications/magnepins-a-modular-affordable-and-diy-refreshable-braille-and-ta/)

### 9.3 Public servo-, micro-motor-, cam- and stepper-based projects

The Hackaday Refreshable Braille Display project publicly documents micro-motor, servo, stepper and cam concepts; active project discussion includes the Indian application allegation and a stepper-cam design. Other academic/student projects disclosed low-cost servo actuation, printed structures, pin guides and ordinary PWM control before the current OpenBraille work. These sources are less reliable than patents for legal status but can be highly relevant prior art if publicly available before a filing date. [Hackaday project](https://hackaday.io/project/10849-refreshable-braille-display)

### 9.4 Historical rotating-wheel work

NIST’s rotating-wheel Braille display work demonstrates longstanding efforts to reduce actuator count and cost through moving mechanical presentation. [NIST source](https://www.nist.gov/publications/rotating-wheel-braille-display-continuous-refreshable-braille)

### 9.5 NPL conclusion

Non-patent prior art is especially damaging to broad narratives such as:

- “using cheap motors instead of piezo is novel”;
- “3D-printing a cell is novel”;
- “macro scaling makes a patentable mechanism”;
- “a modular low-cost Braille cell is unexplored”;
- “shared actuation is a new direction.”

It does not eliminate a narrowly integrated and experimentally demonstrated physical-control contribution, but it makes the burden of proof high.

---

## 10. Current MVP patent assessment

### 10.1 Novelty of the combination

No verified single independent claim was shown to recite every detail of the exact six-SG90, one-cam-per-dot, 300%-scale, ESP32 architecture. Nevertheless, the central kinematic combination—rotary actuator, raised cam/disk surface, guided translating Braille pin—is expressly claimed or disclosed. Commodity servos, PWM, printed guides, active retraction, character mapping, and 5 V power are routine implementation choices.

**Assessment:** exact literal novelty may remain in a narrow descriptive sense, but no credible patent contribution is established.

### 10.2 Inventive step

A skilled embedded/mechanical team seeking a low-cost demonstrator would predictably consider:

- replacing piezo with commodity motors/servos;
- converting rotary motion to linear pin travel with a cam;
- printing a large guide/frame to relax tolerances;
- controlling each servo by PWM;
- sequencing movement to reduce supply transients;
- storing endpoint offsets;
- adding hard stops or guides.

These are routine substitutions, aggregation, calibration and workshop modifications unless a tightly coupled architecture produces an unexpected technical effect.

### 10.3 Scale

Macro scaling removes the most difficult packaging and tolerance constraints rather than solving them. It improves student buildability but weakens any claim to a practical refreshable Braille cell mechanism. Scale-independent control data may still be useful, but force, friction, actuator packaging, array density, tactile readability and manufacturing yield do not automatically transfer.

### 10.4 Conclusion on current MVP

- **Engineering demonstrator:** credible.
- **Patent invention:** not established.
- **Filing now:** not recommended.
- **Public disclosure:** the already-public architecture is low sensitivity, but new integrated improvements and data should remain confidential.

---

## 11. Candidate invention-direction matrix

Costs are incremental estimates within the current student prototype and require local sourcing. “Track” describes patent-development timing, not guaranteed patentability.

| Direction | Exact problem and prospective contribution | Closest art / overlap | Required measurable effect and baseline | Cost / 3-month feasibility | Patent risks | Scale / Track / confidence / kill condition |
|---|---|---|---|---|---|---|
| **1. Integrated per-dot tolerance compensation and verified refresh** | Commodity servos and printed channels vary in backlash, endpoint, current draw and friction. Combine bounded pin travel, stored per-dot operating windows, controlled one-dot-at-a-time electrical signatures, positive state/retraction verification and fault-aware update logic. | Braille-watch cams; Freedom Scientific stops/guides; EM pulse-energy control; ordinary servo calibration and jam detection. Differentiation is the *specific integration and demonstrated effect*, not any element alone. | Compared with fixed common PWM: materially fewer out-of-range pin heights, stalls, missed retractions and resets across heterogeneous servos/prints; reliable fault detection. | ₹500–1,400 incremental; feasible if scope is one cell and instrumentation is simple. | Novelty medium-high risk; obviousness high; eligibility low-medium if physically claimed; FTO medium until final chart. | Mixed scale; **Track B**; **42%**. Kill if improvement is small, unstable, or explained by routine tuning. |
| **2. Low-cost per-dot calibration alone** | Store unique up/down PWM endpoints for each servo. | Ordinary hobby-servo setup, calibration fixtures and actuator tuning. | Repeatability improvement over common endpoints. | Very low cost; easy. | Very high obviousness; weak technical substance. | Scale-independent; **Track D standalone**; 15%. Kill as patent direction unless integrated with verification and physical constraints. |
| **3. Verified tactile-state detection and correction** | Detect whether each commanded dot is actually up/down and retry or isolate faults. Could use current signatures, a temporary optical gauge, Hall/limit sensing, or a low-cost shared verification fixture. | State sensing, touch/capture assemblies, actuator diagnostics, industrial jam detection. | ≥95% detection of induced stuck/missed states with low false positives; correction without damaging mechanism. | ₹300–1,500; feasible with one-cell scope. | Sensor/control combinations may be obvious; active capture/capacitive families require care. | Partly scale-independent; **Track B** if combined; 35%. Kill if no reliable low-cost signal correlates with pin state. |
| **4. Compliant printed guide or return geometry** | Reduce sticking and accommodate FDM variation using flexures, compliant walls, tapered guides or integrated return elements. | IIT Delhi compliant/cantilever cells; printed flexures; modular guide and travel-stop art. | Large, reproducible reduction in friction/jam rate and print rejection across printers/materials. | ₹100–500; feasible. | Very high obviousness as geometry optimization unless an unexpected tolerance window/yield effect is shown. | Scale-sensitive; **Track B/C supporting direction**; 25%. Kill if benefits vanish with ordinary clearance tuning. |
| **5. Scale-transfer fabrication and calibration method** | Define a verified method that maps macro measurements and tolerance rules to a practical smaller cell. | General tolerance scaling, standard-scale MagnePins, commercial cell manufacturing, compliant/magnetic families. | Predictive model accurately forecasts travel/force/yield at smaller scales; practical-scale specimen validates it. | Likely >₹5,000 or >3 months for meaningful proof. | High prior-art and enablement risk; potentially useful if method is specific and predictive. | Standard-scale validation mandatory; **Track C**; 30%. Kill if no practical-scale embodiment or predictive transfer. |
| **6. Modular replacement and self-alignment** | Replace a failed dot/actuator module without recalibrating the whole cell. | US8690576 modular blocks; US11915607 removable cavities; WO2020106855 removable top; MOLBED/MagnePins. | Demonstrate interchangeability, repeatable alignment and reduced service time without loss of tactile accuracy. | ₹300–1,000; feasible mechanically. | Crowded and likely obvious; active claims exist in specific architectures. | Scale-sensitive; **Track C or D**; 18%. Kill unless module exchange automatically preserves calibrated performance through a distinctive interface. |
| **7. Current-aware actuation sequencing** | Prevent voltage sag, resets and stalls by scheduling servos based on measured current/current envelope. | General servo/robotics power management; sequential impact systems; EM pulse-energy control. | Fewer resets/stalls with shorter or equal refresh time than fixed sequential or simultaneous baselines. | ₹200–700 for current sensor/capacitance; feasible. | Very high obviousness as standalone firmware. | Scale-independent; **Track D standalone**, supporting Track B; 20%. Kill if simple fixed staggering performs equivalently. |
| **8. Closed-loop travel verification** | Measure actual pin travel and adapt commands. | Position sensors, calibration fixtures, tactile-state systems, capture/capacitive layers. | Reduced pin-height error and automatic fault isolation across wear/temperature/servo replacement. | Six permanent sensors may threaten budget/complexity; a shared or removable gauge is feasible. | Better substance than endpoint calibration but still crowded; sensor packaging may drive novelty. | Mixed; **Track B** for shared/removable verification, **Track C** for per-dot miniaturized sensing; 35%. Kill if sensing costs more than actuation or cannot fit practical scale. |
| **9. Shared actuation / actuator reduction** | Reduce six actuators through moving carriage, selector, shared cam or resonant addressing. | US6692255, NIST rotating wheel, MagnePins, EP4049116, impact-driver families. | Major cost/volume reduction while preserving refresh time and reliability. | Major redesign; unlikely within frozen MVP scope. | Dense prior art and high FTO risk. | Standard-scale sensitive; **Track C / major redesign**; 22%. Kill if architecture is merely a known moving write head or selector. |
| **10. Specific FDM process/clearance recipe** | Define material, orientation, guide shape, post-processing and clearance combination that produces repeatable tactile travel at low cost. | Additive manufacturing, printed guides, open-hardware assemblies, Freedom Scientific tolerance solutions. | Statistically significant yield/durability advantage across repeated prints and at least two material/process conditions. | ₹500–1,500; feasible at macro scale. | “3D printing” and normal design-of-experiments are not inventive; process must be narrow and physically consequential. | Scale-sensitive; **Track B supporting / Track C stronger**; 28%. Kill if results are printer-specific or expected from ordinary tuning. |
| **11. Positive active-retraction and jam-safe recovery** | Treat active commanded retraction as the truthful baseline and detect/recover stuck pins without damaging servos. | Bidirectional pin systems, actuator diagnostics, ordinary limit protection. | Reliable retraction under friction/wear; bounded recovery force; fault logging. | Low incremental cost; feasible. | Mostly routine safety/control logic unless integrated with verified state and physical limits. | Scale-independent control plus scale-sensitive friction; **Track B supporting**; 25%. Kill as standalone. |
| **12. Character mapping, serial interface, self-test or ordinary calibration menu** | Firmware convenience features. | Ubiquitous Braille and embedded systems. | No unique physical effect. | Easy. | No credible patent direction. | **Track D**; <10%. Reject. |

### 11.1 Directions rejected as standalone patent targets

The following should not be presented independently as inventions:

- SG90 servo substitution;
- eccentric cam actuation;
- ESP32 direct PWM;
- enlarged Braille geometry;
- FDM printing generally;
- ordinary endpoint calibration;
- ordinary sequential servo movement;
- character lookup/mapping;
- external 5 V supply or capacitor;
- modularity without specific structural and performance consequences.

---

## 12. Strongest surviving direction

### 12.1 Precise technical definition

**Confidential project material — not for public disclosure before IPR review.**

The strongest surviving direction is a **verified heterogeneous-actuator tactile-cell control architecture** comprising, at minimum:

1. **Mechanically bounded tactile travel:** a defined upper and lower physical reference or guide relationship that limits pin travel independently of raw servo command tolerance.
2. **Actuator-specific operating window:** stored up, down and transition parameters for each low-cost rotary actuator, derived from a repeatable calibration procedure rather than hand tuning.
3. **Controlled electrical-signature measurement:** one actuator is characterized or actuated in a measurement-safe sequence so supply current/voltage/time behavior can be associated with free travel, contact, stall, obstruction or incomplete return.
4. **Positive state or retraction verification:** a measurable indication—not merely the command itself—that the tactile pin reached an acceptable state. This may initially use a removable optical/mechanical gauge or a shared low-cost verification fixture; permanent per-dot sensors are not required for the first experiment.
5. **Fault-aware refresh sequencing:** the controller schedules, retries, derates, isolates or reports a dot based on calibrated operating windows and measured response, rather than blindly sending fixed PWM commands.
6. **Physical technical effect:** a reproducible reduction in out-of-spec pin states, supply resets, stalls, failed retractions, calibration time or replacement sensitivity, without unacceptable refresh-time or cost penalty.

### 12.2 Why this is more than ordinary optimization—if successful

The direction would only exceed routine optimization if the evidence shows that the elements interact to solve a distinctive physical problem of ultra-low-cost, heterogeneous actuators and low-tolerance printed mechanics. For example, mechanically bounded travel may make electrical signatures interpretable; sequential signatures may enable low-cost verification without six sensors; actuator-specific windows may allow drop-in servo replacement while preserving tactile performance; fault-aware updates may prevent supply sag and hide defective dots.

Without that interaction and measured effect, it collapses into ordinary servo calibration and must be rejected.

### 12.3 Closest art and residual distinction

- Rotary disk/cam and pins: old.
- Mechanical travel limits and modular guides: old.
- Actuator calibration and current-based jam detection: broadly known engineering practices.
- Sequential actuation and power management: known.
- Tactile-state sensing and removable top/capture structures: known in adjacent families.

The only plausible residual distinction is the **specific integrated architecture and its demonstrated effect in a low-cost refreshable tactile cell using heterogeneous commodity rotary actuators**. A professional search using that exact final formulation is mandatory before filing.

---

## 13. Macro-scale and standard-scale transfer assessment

| Prospective element | Scale class | What macro data can support | What macro data cannot prove | Required later evidence |
|---|---|---|---|---|
| Firmware state machine, fault logging and actuator-specific parameter storage | Scale-independent | Logic correctness, calibration workflow, retry/isolation behavior | Practical sensor packaging and array timing | Code records, reproducible test protocol, broader prior-art search |
| Sequential current/voltage signature acquisition | Partly scale-independent | Whether SG90 travel/contact/stall states are distinguishable; supply behavior | Signature transfer to smaller actuators or dense cells | Multiple actuator lots; temperature/wear tests; practical-scale actuator study |
| Mechanically bounded upper/lower travel | Scale-sensitive | Macro stop repeatability and interaction with servo command | Standard pitch, cell thickness, force, friction and user feel | Tolerance stack and practical-scale specimen |
| Positive state verification with removable/shared gauge | Scale-independent as a calibration method, scale-sensitive as packaging | Whether verification materially improves calibration and fault detection | On-device compact integration | A practical fixture or embedded sensor design |
| Compliant printed guide geometry | Standard-scale validation mandatory for broad claims | Macro friction, print-orientation and material effects | Micro-clearance behavior, fatigue, tactile density | Smaller guides, multi-printer study, wear data |
| FDM process/clearance recipe | Scale-sensitive | Repeatability at one scale and printer class | Generality and practical-scale yield | At least two scales/processes and a predictive tolerance model |
| Current-aware sequencing | Scale-independent in principle | Brownout/stall reduction and timing trade-off | Dense-array performance and other actuator types | Multi-cell or simulated-load validation |
| Shared actuation / actuator reduction | Standard-scale validation mandatory | Conceptual software/control only | Mechanism feasibility, speed, density, FTO | New architecture, larger budget and later semester |

### 13.1 Scope consequence

A claim limited to a large teaching/demo cell may have little commercial value and may be easy to design around. A broader claim to standard Braille cells would require credible enablement and evidence at practical dimensions. The most transferable near-term evidence is control/diagnostic behavior; the least transferable is mechanical clearance, force and packaging.

---

## 14. Novelty analysis

### 14.1 Frozen MVP

The audit did not establish one verified independent claim containing every exact MVP detail. However, the central mechanical relationship is expressly claimed in the Braille-watch family, and all remaining features are old or routine. The frozen MVP therefore lacks a credible novelty position as an invention package.

### 14.2 Strongest direction

A novelty case would require one prospective claim to include the integrated physical-control elements in Section 12. The search did not identify one record that clearly discloses the whole combination. That is a **provisional absence**, not proof of novelty.

Novelty risk remains high because:

- final architecture and terminology are not frozen;
- current-based state inference, servo endpoint calibration, mechanical stops and jam recovery exist in broader actuator fields;
- hidden or non-English patent literature may contain a similar combination;
- the Indian application remains unavailable;
- public student and maker projects may contain undocumented calibration or sensing details.

### 14.3 Novelty gate

No filing recommendation should be made until a search is repeated against a one-page invention disclosure containing exact elements, alternatives and technical effects.

---

## 15. Inventive-step / obviousness analysis

Inventive step is the principal risk.

A likely obviousness argument would combine:

1. the Braille-watch rotating disk/pin relationship;
2. known modular guide/travel-stop structures;
3. standard servo calibration and endpoint storage;
4. known current-based stall/jam detection;
5. ordinary sequential scheduling to avoid supply sag;
6. known tactile-state sensing or calibration fixtures.

A reviewer could characterize the proposed direction as applying familiar actuator-control techniques to a known Braille mechanism. To resist that characterization, OpenBraille would need evidence of a non-additive technical result, such as:

- low-cost current signatures reliably substitute for six position sensors because the mechanical stop architecture creates distinguishable states;
- drop-in actuator replacement preserves pin height without manual mechanical adjustment;
- the integrated method reduces tactile-state defects by an order of magnitude across low-cost actuator variation;
- fault-aware sequencing simultaneously reduces current peaks and detects mechanical failures without a material refresh penalty;
- a defined print/control tolerance window produces unexpectedly high yield across multiple printers or actuator lots.

Incremental improvement, cost reduction alone, or “it works” will not be enough.

---

## 16. Patent-eligibility analysis

### 16.1 Hardware and manufacturing aspects

A physically defined cell, calibration fixture, guide/stop relationship, sensor arrangement, or manufacturing method that changes tactile performance is generally a stronger eligibility posture than a software-only rule. Eligibility is not the main risk; novelty and inventive step are.

### 16.2 Control aspects

A claim framed only as:

- mapping characters;
- storing servo values;
- choosing an actuation order;
- comparing current to a threshold;
- reporting a fault;

could be treated as abstract data processing or ordinary control logic in some jurisdictions. The control contribution should be anchored to:

- specific actuators and tactile pins;
- measured physical signals;
- a defined calibration operation;
- mechanical state transitions;
- an objective improvement in force, travel, reliability, energy or fault detection.

### 16.3 Jurisdictional caution

Eligibility standards differ between India, the EPO, the United States and other jurisdictions. Institutional counsel should decide whether the best formulation is apparatus, control method, manufacturing method, calibration fixture, or a coordinated claim set.

---

## 17. FTO risk analysis

### 17.1 Frozen student MVP

The evidence does not permit a finding of infringement. Several active modern claims use materially different electromagnetic, friction-impact, capture-plate, mobile-case or shared-taxel structures. Older close rotary and modular patents are database-reported expired or abandoned. However:

- `5559/CHE/2014` remains unresolved and is allegedly close;
- active foreign or continuation claims may exist outside the reviewed US claim sets;
- public educational use is not a universal legal exemption;
- commercial manufacture, sale and export create different risk than a private student prototype.

**Screening assessment:** moderate uncertainty; likely lower risk for a one-off confidential educational prototype than for commercialization, but no clearance conclusion.

### 17.2 Bounded enhancement

The integrated enhancement raises new FTO questions:

- a removable or capacitive verification top may approach capture-plate families;
- magnetic/Hall state sensing may interact with EM-latching families;
- friction-held pins may approach US11854423;
- modular replacement interfaces may approach active and expired modular families;
- pulse-energy/current calibration may overlap claims in electromagnetic actuator systems or broader servo diagnostics.

**Screening assessment:** medium risk, design-specific, requiring a final claim chart.

### 17.3 Major redesigns

- Electromagnetic latching: high screening risk.
- Shared moving write head: medium-high, with old and active adjacent art.
- Resonance-addressed taxels: high around EP4049116 and related work.
- SMA/compliant latching: medium-high, with IIT Delhi and historical SMA families.

### 17.4 Required FTO work

Before commercialization:

1. define countries and dates;
2. obtain `5559/CHE/2014` file;
3. search continuations/divisionals and national family members;
4. chart final product elements against live independent claims;
5. consider design-arounds and counsel opinion.

---

## 18. Claim-to-experiment map

The following experiments are designed to produce both engineering and invention-development evidence. Thresholds are proposed pre-registration values, not frozen project requirements.

| Prospective element | Nearest verified art | Measurable effect | Baseline / proposed system | Variables and controls | Equipment and sample/cycles | Success evidence | Failure evidence | Scale relevance / timing / confidentiality |
|---|---|---|---|---|---|---|---|---|
| Mechanically bounded pin travel plus actuator-specific windows | US8483018; US8690576 | Lower pin-height dispersion and fewer over/under-travel events | Common PWM endpoints / per-dot calibrated endpoints with fixed physical references | Servo unit, cam, guide clearance; control supply, pin mass, print material | 6–12 servos from at least two lots if possible; caliper/dial indicator or camera gauge; ≥100 cycles per dot | ≥50% reduction in out-of-range events and stable endpoints after replacement/reassembly | Improvement is minor, achieved by ordinary hand tuning, or disappears across prints | Macro supports interaction; practical-scale mechanics later. Deliverable in 2–3 weeks. Confidential calibration/geometry. |
| Electrical-signature state inference | General actuator diagnostics; WO2020106855 pulse-energy control | Distinguish free travel, contact, stall and jam without six position sensors | Fixed command/no measurement / sequential actuation with current-voltage-time capture | Actuator load and induced fault; control supply, command speed, temperature | INA219/INA226 or shunt/ADC, oscilloscope if available; ≥30 labeled events per state per selected dot | Classification ≥95% on held-out events or a simpler threshold with low false alarms | Large overlap between states, high sensor noise, or signatures drift rapidly | Mostly scale-independent for method, actuator-specific for model. 2–3 weeks. Confidential signatures/threshold logic. |
| Positive retraction verification | Active-pin and capture/sensing art | Detect incomplete return before next character | Command assumed successful / removable optical or mechanical gauge verifies pin state | Induced friction/debris; control command and geometry | Simple light gate/camera/top gauge; ≥100 normal and ≥30 fault events | ≥95% fault detection, <5% false positive, no significant damage | Verification is manual, unreliable, or too slow/costly | Calibration method may transfer; packaging later. 2 weeks. Confidential fixture. |
| Fault-aware refresh sequencing | Sequential impact systems; ordinary power management | Reduce resets/stalls while maintaining refresh time | Simultaneous or fixed sequential / current-budgeted and fault-aware scheduler | Dot pattern, transition count; supply and capacitor fixed | ESP32 logs, voltage/current sensor; all 64 six-dot transitions repeated ≥20 times | No resets, materially reduced peak/sag, fault isolation, acceptable latency | Fixed staggering performs the same or proposed logic adds no physical benefit | Scale-independent logic; array validation later. 1–2 weeks. Confidential scheduler. |
| Active retraction and jam-safe recovery | Bidirectional pin systems; actuator safety controls | Reliable down-state and bounded recovery force | Single reverse command / verified staged return, timeout and isolation | Friction and obstruction; same servo/cam | Force gauge if available, current sensor; ≥500 cycles with induced faults | High retraction reliability and safe fault handling without gear damage | Repeated stalls, no detectable signature, excessive wear | Mixed scale. 2–3 weeks. Confidential recovery sequence. |
| FDM guide/process tolerance window | Open printed projects; US8690576 tolerance structures | Higher print yield, less friction, stable travel | One ad hoc print / designed matrix of clearance, orientation, material and post-process | Clearance, orientation, layer height, material; same actuator/pin | 12–24 guide specimens; travel/friction test; ≥100 cycles each | Statistically clear robust window across at least two print batches | Result is printer-specific, ordinary, or no durability advantage | Scale-sensitive. 3–5 weeks. Confidential process recipe until review. |
| Drop-in actuator/module replacement | Modular families | Preserve calibrated tactile output after replacement | Replacement requires manual rebuild / keyed module plus automated recalibration | Servo/module identity; fixed frame and pin | At least 3 replacement cycles on 3 dots | Restoration within specified pin-height/reliability limits in a bounded automated procedure | Manual adjustment remains necessary or module interface adds instability | Macro proof only; standard packaging later. 2–3 weeks. Confidential interface. |
| Tactile performance | All Braille art; project authority | Demonstrate that engineering metrics correspond to distinguishable tactile output | Uncalibrated / calibrated verified system | Character and dot pattern; blindfolded sighted pilot only until ethics/accessibility review | Force/travel measurements first; qualified Braille-reader study only with approval | Repeatable tactile distinction and no sharp/unsafe surfaces | Metrics improve but tactile usability does not | Standard-scale validation mandatory for product claims. Confidential results until IPR review. |

---

## 19. Three-month semester plan

### Weeks 1–2 — Truthful baseline and instrumentation

- Procure/inspect SG90 variants and confirm that passive return is not assumed.
- Build one single-dot mechanism before the six-dot cell.
- Establish active up/down command, travel measurement, current/voltage logging and safe stall limits.
- Freeze baseline geometry and fixed-PWM comparator.
- Begin dated confidential invention log.

### Weeks 3–4 — Six-dot frozen MVP

- Print and assemble macro cell.
- Implement character mapping, direct PWM and active cam retraction.
- Test power supply under worst credible transitions.
- Measure travel, force, pin height, retraction and current for every dot.
- Do not yet call any calibration or sequencing feature inventive.

### Weeks 5–6 — Per-dot operating windows

- Calibrate individual up/down/transition ranges.
- Add mechanical travel reference where needed.
- Compare fixed common endpoints with calibrated endpoints across multiple servos and reassemblies.
- Stop if repeatability cannot be made adequate within the budget.

### Weeks 7–8 — Measurement and verification

- Add low-cost current/voltage measurement.
- Label free-travel, contact, stall and induced-jam signatures.
- Prototype a removable/shared state-verification gauge.
- Determine whether reliable state inference is possible without six permanent sensors.

### Weeks 9–10 — Integrated fault-aware refresh

- Combine calibrated windows, signature measurement, state verification and fault-aware sequencing.
- Run all character transitions and induced faults.
- Compare against simultaneous, fixed-sequential and fixed-PWM baselines.

### Weeks 11–12 — Durability, documentation and decision gate

- Run 1,000-cycle minimum screening per selected dot/mechanism; extend if time permits.
- Repeat critical tests after actuator replacement and print reassembly.
- Analyze physical effect, cost and latency.
- Prepare invention disclosure and claim-feature search terms.
- Hold institutional IPR review before public presentation of confidential additions.

### Semester deliverable

At minimum, the project should deliver a functioning macro six-dot cell and a rigorous negative or positive result on the integrated enhancement. A well-supported negative result is preferable to a weak patent assertion.

---

## 20. Later-semester or publication extension

If the Track B direction survives, the later programme should not jump immediately to a new actuator. It should extend the same technical thesis:

1. **Practical-scale cell or sub-cell:** reduce pitch and thickness while preserving the verified calibration/diagnostic relationship.
2. **Multi-cell interaction:** test supply, timing, vibration, heat, EMI and fault isolation across several cells.
3. **Manufacturing transfer:** validate tolerances across printers, materials or a higher-precision process; determine whether the method predicts yield.
4. **Embedded sensing refinement:** replace temporary verification fixtures with a shared, compact or low-cost sensor architecture if justified.
5. **User validation:** conduct approved evaluation with Braille readers at practical geometry.
6. **Professional search and claim chart:** search the exact integrated invention and active families in intended jurisdictions.
7. **Publication opportunity:** publish only after filing/IPR decision; negative engineering results may still support an accessibility or low-cost prototyping paper.

Estimated later duration is approximately one additional semester. Cost could exceed ₹5,000 if practical-scale fabrication, multiple actuator lots, sensors, user testing or professional patent work is included. This remains part of OpenBraille because it tests whether the macro cell’s low-cost actuator variation can be controlled and verified at usable tactile scale; it is not an unrelated actuator project.

---

## 21. Budget and team feasibility

### 21.1 Frozen MVP

The authority documents estimate the servo/cam architecture within the preferred ₹3,000–₹5,000 envelope. The audit does not independently validate local prices, but the architecture is plausible for a student prototype.

### 21.2 Incremental bounded enhancement

Indicative additions:

| Item | Indicative incremental cost |
|---|---:|
| Current/voltage sensor module or shunt/ADC components | ₹150–₹500 |
| Additional servos for variation/replacement testing | ₹300–₹900 |
| Printed test coupons/guides/cams | ₹200–₹600 |
| Simple optical/mechanical verification fixture | ₹150–₹600 |
| Wires, connectors, capacitor, fasteners and contingencies | ₹300–₹700 |

The enhancement can remain under ₹5,000 only if the team avoids six permanent high-resolution sensors and expensive precision fabrication.

### 21.3 Team allocation

For five members:

- **Mechanical/CAD owner:** guide, cam, stop, fixture, print matrix.
- **Embedded-control owner:** PWM, calibration storage, scheduler, fault state machine.
- **Instrumentation/data owner:** current/voltage capture, travel measurement, analysis scripts.
- **Test/quality owner:** cycle protocol, fault injection, configuration control, evidence records.
- **Documentation/presentation owner:** source log, experiment records, confidentiality, user-facing explanation.

The three technically strong members can cover the first three roles, while the remaining members support test discipline and documentation. The main feasibility risk is not firmware; it is repeatable mechanical measurement and disciplined testing.

---

## 22. Kill criteria

The patent-oriented path must be killed or reduced in priority if any of the following occurs:

1. The frozen mechanism cannot meet basic tactile force, travel, retraction and repeatability within budget.
2. Per-dot calibration provides only a trivial improvement obtainable by ordinary manual endpoint tuning.
3. Current/voltage signatures cannot reliably distinguish useful physical states or drift excessively across units, temperature or wear.
4. Positive state verification requires per-dot hardware that destroys the cost, size or simplicity advantage.
5. The integrated system does not materially outperform fixed sequential PWM in defect rate, fault detection, current peaks or replacement tolerance.
6. The FDM process result is limited to one printer/one specimen and cannot be reproduced.
7. A later search finds one prior-art reference disclosing every required element of the proposed integrated direction.
8. A routine combination of close references explains the result and no unexpected technical effect is demonstrated.
9. Official `5559/CHE/2014` claims, or another live family, map closely to the planned product with no practical design-around.
10. Macro results cannot be connected to a commercially or educationally useful scope, and no standard-scale continuation is feasible.
11. The project requires a major shared-actuation, EM-latching or SMA redesign to retain patent value; that path must then be reclassified as Track C/major redesign rather than silently substituted.
12. Confidentiality is lost before an invention record and institutional IPR decision are completed.

---

## 23. Confidentiality boundary

### Already public or non-sensitive baseline

- low-cost refreshable Braille objective;
- one macro six-dot cell;
- ESP32 and SG90 servos;
- eccentric cams, followers and pins;
- direct PWM and ordinary character mapping;
- printed frame/guides;
- general student budget and timeline.

### Potentially confidential new mechanical material

- exact upper/lower travel-reference geometry;
- actuator/module keying and replacement interface;
- guide-clearance/flexure combinations;
- verification fixture geometry;
- scale-transfer dimensions and tolerance models.

### Potentially confidential control material

- calibration procedure and stored operating-window representation;
- electrical-signature extraction and decision thresholds;
- state-verification logic;
- retry, derating, isolation and fault-aware sequencing;
- interaction between mechanical stops and diagnostic signals.

### Potentially confidential evidence

- servo-to-servo variation data;
- current/voltage signatures;
- failure-mode datasets;
- pin-height, force, wear and yield results;
- comparative evidence showing an unexpected effect.

**Rule:** do not upload confidential additions to public repositories, present them publicly, or include them in a public paper/demo before institutional IPR review.

---

## 24. Final project recommendation

# **Advance conditionally pending named evidence**

OpenBraille should advance as a strong semester engineering prototype and a conditional patent-development candidate, not as a proven patent-first invention.

The named conditions are:

1. the frozen MVP passes force, travel, retraction, power and repeatability gates;
2. the integrated Track B enhancement is implemented as a coherent physical-control system, not isolated ordinary features;
3. comparative experiments demonstrate a material technical effect;
4. the official `5559/CHE/2014` file is obtained or formally reported unavailable after a professional search;
5. a final claim-language patent/NPL search finds no single anticipation and no overwhelming obviousness combination;
6. active-family FTO is claim-charted for intended jurisdictions;
7. institutional IPR review occurs before disclosure.

Failure of conditions 2 or 3 should normally lead to **Retain as strong semester prototype but reduce patent priority** rather than forcing a weak filing.

---

## 25. Unresolved questions

1. What are the official publication, claims and current status of `5559/CHE/2014`?
2. Does the procured SG90 variant have any useful passive return, or is all return actively driven as expected?
3. What force and pin-height range is tactilely acceptable at the macro prototype, and how will it relate to standard Braille?
4. Can low-cost electrical measurements distinguish contact, free travel, stall and incomplete return across multiple servos?
5. Can a state-verification method avoid six permanent sensors?
6. Does mechanically bounded travel create a distinctive, reproducible diagnostic signature?
7. How much improvement does per-dot calibration provide over careful ordinary setup?
8. Can the system tolerate actuator replacement or print reassembly without manual mechanical adjustment?
9. Which aspect—mechanical interface, calibration method, diagnostic measurement, fault-aware sequencing or manufacturing process—actually carries the technical effect?
10. Does the effect persist across servo lots, print batches, temperature and wear?
11. What exact claim language would be commercially useful but still enabled by macro evidence?
12. Is a practical-scale continuation financially and mechanically feasible for the team?
13. Which jurisdictions matter for filing and FTO?
14. Are there university ownership, inventorship, disclosure or ethics requirements?
15. What public disclosures have already occurred, and on what dates?

---

## 26. Source and verification log

### 26.1 Project authority sources

- `01_Engineering_Design_Review(4).md` — concept identity, hypothesis, fixed principles and minimum demonstrable success.
- `02_Project_mC_Decision_Register_v1.2(4).md` — budget, timeline, authority rules, frozen architecture and active-retraction correction.
- `03_Phase3C_Portfolio_Closure_Memo_Approved(4).md` — project priority and retained status.
- `04_Phase3C_OpenBraille_Architecture_Report_Final(4).md` — selected servo/cam architecture and prior synthesis.
- `05_Phase3C_OpenBraille_Memory_Final(4).md` — concise frozen architecture and BOM estimate.
- `06_Phase3C_OpenBraille_SOP_Final(4).md` — architecture-planning scope.
- `07_Concept_Evidence_Matrix(4).md` — neutral project evidence extraction.
- `08_Uncertainty_and_Test_Register(4).md` — reset, power, force, tolerance, wear and scale uncertainties.
- `09_Patent_Research_Input_Pack(4).md` — current search directions and warning against treating historical findings as truth.
- `10_Phase2_Report_by_Claude(4).md` — historical leads only.

### 26.2 Independent reports audited

- ChatGPT Deep Research — medium reliability.
- Gemini Deep Research — low; Indian/status portions excluded.
- Perplexity Deep Research — low and partial through §8.2 only.
- Qwen Deep Research — low; only corroborated engineering ideas retained.
- Mistral — low; overconfident Indian/status findings excluded.
- Microsoft Copilot — low; unsupported Indian/status finding excluded.

### 26.3 Patent records re-checked

- [US8483018B2 — Braille watch](https://patents.google.com/patent/US8483018B2/en)
- [US20130017516A1 — Active Braille timepiece](https://patents.google.com/patent/US20130017516A1/en)
- [US11854423B1 — Refreshable Braille display](https://patents.google.com/patent/US11854423B1/en)
- [US11410574B2 — Layered electromagnetic Braille display](https://patents.google.com/patent/US11410574B2/en)
- [WO2020106855A1 — Electromagnetic refreshable Braille reader](https://patents.google.com/patent/WO2020106855A1/en)
- [EP3884363B1 — Electromagnetic refreshable Braille reader](https://patents.google.com/patent/EP3884363B1/en)
- [US11915607B2 — Modular refreshable Braille display system](https://patents.google.com/patent/US11915607B2/en)
- [US12080182B2 — Capture plate assembly](https://patents.google.com/patent/US12080182B2/en)
- [US8690576B2 — Braille display and construction](https://patents.google.com/patent/US8690576B2/en)
- [US9424759B2 — continuation](https://patents.google.com/patent/US9424759B2/en)
- [WO2015189863A2 — IIT Delhi SMA compliant mechanism](https://patents.google.com/patent/WO2015189863A2/en)
- [EP4049116A1/B1 — Tactile pixels](https://patents.google.com/patent/EP4049116A1/en)
- [US6881063B2 — Electroactive polymer Braille cell](https://patents.google.com/patent/US6881063B2/en)
- [US5685721A — SMA Braille cell](https://patents.google.com/patent/US5685721A/en)
- [US6743021B2 — MEMS/flexible-surface display](https://patents.google.com/patent/US6743021B2/en)
- [US6692255B2 — Bidirectional shared-actuator tactile display](https://patents.google.com/patent/US6692255B2/en)
- [US7410359B1 — Freedom Scientific tactile-cell family lead](https://patents.google.com/patent/US7410359B1/en)

### 26.4 Non-patent sources re-checked

- [Hackaday Refreshable Braille Display and `5559/CHE/2014` public statements](https://hackaday.io/project/10849-refreshable-braille-display)
- [MOLBED project](https://www.madaeon.design/portfolio/molbed-2016-2019/)
- [MagnePins publication record](https://research.monash.edu/en/publications/magnepins-a-modular-affordable-and-diy-refreshable-braille-and-ta/)
- [NIST rotating-wheel Braille display](https://www.nist.gov/publications/rotating-wheel-braille-display-continuous-refreshable-braille)

### 26.5 Verification cautions

- Google Patents was used for claim text, bibliographic discovery and family navigation where official interfaces were inaccessible. Its legal-status labels expressly carry a disclaimer and are not treated as certified legal conclusions.
- The EPO grant publications visible in the retrieved records confirm publication events, not every national validation or lapse.
- PCT cessation is not equivalent to extinction of all national rights.
- No official Indian record for `5559/CHE/2014` was obtained.
- No statement in this report should be read as a finding of infringement, validity, enforceability, or guaranteed patentability.

---

**End of report**
