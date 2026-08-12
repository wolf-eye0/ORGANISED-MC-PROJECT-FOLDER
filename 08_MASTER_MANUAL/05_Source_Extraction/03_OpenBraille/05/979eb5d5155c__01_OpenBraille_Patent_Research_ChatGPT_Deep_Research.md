# Source Extraction

- Chapter: `05` — OpenBraille Patent Evidence and Future Research Path
- Authority tier: `TIER_3`
- Manual treatment: `SUPPORTING_EVIDENCE`
- Original source: `03_CONCEPT_PORTFOLIO/OpenBraille/02_Raw_Research/01_OpenBraille_Patent_Research_ChatGPT_Deep_Research.md`
- SHA-256: `979eb5d5155c9fe1243f582320f716ca549f267cbc711597dba7287f51b7c257`
- Extraction method: `PLAIN_TEXT`
- Rule: source text only; no synthesis, correction or reconciliation.

---

# OpenBraille Current Patent-Verification Deep Research

## Source-Fidelity Confirmation

**Concept researched.** This report researches **OpenBraille only**: a low-cost refreshable tactile Braille-cell concept intended to replace expensive conventional actuation with a student-buildable electromechanical architecture.

**Frozen MVP architecture understood.** The present semester MVP is one approximately 300%-scale six-dot Braille cell using an ESP32-WROOM-32, six SG90-class servos, one eccentric cam/follower/sliding tactile-pin mechanism per dot, direct GPIO PWM, FDM-printed guides and frame, and an external 5 V supply. I have treated this architecture as frozen for the semester, not automatically as the patent invention. fileciteturn0file0 fileciteturn0file1 fileciteturn0file3

**Budget and implementation window understood.** The preferred prototype budget is ₹3,000 or below, the absolute ceiling is ₹5,000, and the current owner-controlled evaluation window is up to three months for a five-member student team. fileciteturn0file0 fileciteturn0file10

**Primary patent-research question.** The question is not whether an exact photographically identical product already exists. It is whether OpenBraille has a **credible, experimentally supportable patent-development path** in the frozen architecture, through a bounded enhancement, through a technically connected later extension, or not at all.

**Governing instruction followed.** The governing specification was `00_READ_FIRST_OpenBraille_Patent_Deep_Research_Instructions.md`, read before the Engineering Design Review, Decision Register, Phase 3C closure and architecture documents, memory, SOP, evidence matrix, uncertainty register, patent input pack, and historical Phase 2 report. Its authority rules and owner-updated three-month continuation policy control this report. fileciteturn0file0

## Executive Assessment

### Overall classification

**Recommendation — Track B, with a strict evidence gate: credible path only through a bounded enhancement achievable and testable within three months.**

This is **not** a finding that the frozen MVP is patentable. The present combination—commodity servo, PWM control, eccentric cam, follower, sliding pin, and printed guide—is heavily anticipated or suggested by patent and non-patent art. Rotating raised surfaces acting on sliding tactile pins were claimed in the Braille-watch family; independently actuated translational Braille pins and cam-based embodiments were disclosed in the active-Braille-timepiece application; and the 2014 Indian application lead is publicly alleged to cover micro-motors, rotors or cams, direct or interposed pin lifting, cantilevers, and mechanical rotation stops. Open-source projects additionally disclose low-cost micro-motor cams, compliant printed levers, pin guides, SG-class servo control, eccentric magnetic cams, modular printed cells, and the same general affordability objective. citeturn0search0turn0search1turn6search1turn12search5turn12search7

The strongest remaining semester-scale opportunity is therefore **not “a servo-cam Braille cell.”** It is a narrowly integrated physical-control architecture provisionally described in this report as:

> **A per-dot tolerance-compensation and verification system for heterogeneous low-cost rotary actuators, combining mechanically limited pin travel, stored actuator-specific operating endpoints, sequential electrical signature measurement, positive retraction checking, and fault-aware update sequencing.**

This prospective direction is **confidential invention-development material**, not a conclusion that a patentable claim has already been conceived. It survives only because the reviewed art does not clearly disclose the exact proposed combination tied to low-cost actuator-to-actuator variation and measured pin-height reliability. Each constituent element, however, is individually close to known hard stops, self-aligning capture plates, calibration fixtures, state sensing, current-conscious driving, and modular tactile assemblies. Its inventive-step risk is consequently high unless the integrated system produces an unexpectedly strong and reproducible technical effect. citeturn4view0turn11view0turn5view2turn1search5

**Confidence in classification: moderate-low, approximately 45%.** Confidence is limited by the unresolved Indian application, incomplete direct access to several national legal-status registers, absence of any OpenBraille physical data, absence of a practical-scale cell, uncertainty over SG90 return behavior, and the possibility that more precise calibration or servo-current prior art will be found during professional searching.

### Findings at a glance

| Question | Finding |
|---|---|
| Is the frozen SG90/cam/pin MVP itself a credible patent candidate? | **No.** It is a useful engineering demonstrator, but its core elements appear conventional individually and strongly suggested in combination. |
| Is a bounded enhancement possible? | **Possibly.** A physically anchored calibration, tolerance-compensation, state-verification, and fault-aware control layer is testable within three months. |
| Is a major redesign necessary to build the semester MVP? | **No.** The frozen MVP remains buildable. |
| Is a major redesign likely to be needed for the strongest long-term patent position? | **Possibly.** Standard-scale modular mechanics or shared actuation could create more technical substance, but both are crowded fields and exceed the present validated architecture. |
| Is current patent filing recommended? | **No.** Build and test first; obtain institutional IPR review before any public disclosure of a newly integrated mechanism. |
| Should OpenBraille retain unconditional patent-first priority? | **No.** It should remain **conditional** until the claim-to-experiment gates are passed. |

### Repository baseline and unresolved engineering assumptions

The repository correctly freezes a macro-scale semester architecture and identifies manufacturing and control as possible IP directions rather than asserting basic actuator novelty. It also explicitly warns that macro success does not prove standard-scale viability or patent relevance. fileciteturn0file3 fileciteturn0file6 fileciteturn0file8

A material engineering correction remains necessary. The Decision Register identifies the supposed SG90 “integrated torsion spring” return as technically unvalidated and instructs the team to document active servo-driven cam retraction if passive return cannot be confirmed. Accordingly, this report treats **active commanded retraction**, not an assumed internal spring, as the frozen baseline. fileciteturn0file10

The uncertainty register also correctly identifies six-servo current demand, FDM friction and tolerance accumulation, wear over repeated cycles, the bridge from macro scale to a practical invention, patent significance of the servo-cam mechanism, and tactile-validation methodology as unresolved. Those are not secondary implementation details; several are precisely the variables on which any surviving patent direction would depend. fileciteturn0file7

## Research Method and Search Record

### Authority and evidence treatment

The Engineering Design Review and Phase 3C frozen architecture were used to define the concept. The Decision Register controlled accepted project decisions. The historical Phase 2 report and its patent numbers were used only as search leads, consistent with the Patent Research Input Pack’s warning that prior AI conclusions were not independently verified. fileciteturn0file1 fileciteturn0file8 fileciteturn0file9 fileciteturn0file10

Patent evidence was separated into four levels:

1. **Patent disclosure:** what the specification teaches.
2. **Issued independent-claim scope:** what an issued claim actually requires.
3. **Database-reported legal status:** useful for screening but not a legal conclusion.
4. **Officially confirmable event:** such as publication of a grant, a recorded B1/B2 document, or an office event accessible in an official source.

Google Patents was used principally for document retrieval, family navigation, claim review, and event discovery. Its own pages warn that assignee and legal-status data may be inaccurate and are not legal conclusions. Current infringement analysis therefore requires a jurisdiction-specific official register and prosecution-history review immediately before any commercial decision. citeturn9view0turn10view3

### Representative search log

Searches were performed on **July 31, 2026**, using a substantive cutoff of information available through **July 30, 2026**, as directed by the governing specification.

| Database or source | Jurisdiction | Exact search strings or identifiers | Classifications or screening logic | Result treatment |
|---|---|---|---|---|
| Indian Patent Office resources and general web index | India | `"5559/CHE/2014"`; `"5559/CHE/2014" granted`; `"5559/CHE/2014" abandoned OR withdrawn OR refused OR published`; `"Paul D'Souza" "Refreshable Braille" patent`; `"micro-motor actuated pins" patent` | Number, applicant, filing date, title, publication, claims, current status | No official bibliographic or prosecution record was retrieved; public statements retained only as non-official evidence. |
| WIPO PATENTSCOPE and PCT-family navigation | WO/PCT | `WO2016074170`; `WO2020106855`; `WO2013130534`; `WO2015189863`; `WO2022238981`; `"refreshable braille" motor cam`; `"tactile pin" actuator modular` | G09B21/003; G09B21/004; family and priority tracing | PCT publications and national family members screened separately; “PCT ceased” not treated as death of national patents. |
| USPTO Patent Public Search, Patent Center links, and US patent texts | United States | `US20130149674`; `US8483018`; `US20130017516`; `US11854423`; `US11410574`; `US11915607`; `US12080182`; `US8690576`; `US9424759`; `US7410359`; `US6902403`; `US6692255` | Independent claims first; specification searched for cam, disk, follower, lever, guide, stop, calibration, modular, sensor, current, state | Issued claims distinguished from unclaimed embodiments. Active/expired labels treated as database-generated unless an official event was independently visible. |
| European Patent Register/Espacenet discovery and EP texts | Europe | `EP3884363`; `EP4049116`; publication-number and family searches | G09B21/003; G09B21/004; G06F3/016 | B1 grant publications confirmed; national validation and lapse status not exhaustively verified state by state. |
| Google Patents family navigation | CN, JP, KR | Family members of `WO2020106855`, `WO2016074170`, `WO2013130534`, `WO2022238981`; keyword combinations in English and available translated records | Country-family coverage and equivalent claims | Used to establish that relevant families entered China, Japan, and Korea; official CNIPA, J-PlatPat, and KIPRIS live legal status remains a follow-up requirement. |
| Scholarly databases and publisher pages | Global non-patent literature | `"servo cam refreshable braille display"`; `"3D printed refreshable Braille display micro motor cam"`; `"MagnePins"`; `"MOLBED"`; `"eccentric cam" Braille`; `"micro servo" Braille` | Mechanism-level relevance, date, public availability, measured performance | Public projects treated as possible prior art regardless of whether patented. |
| Open-hardware repositories | Global non-patent art | MOLBED; MagnePins; Hackaday refreshable Braille micro-motor project; electromechanical refreshable Braille module | Public disclosure date, diagrams, mechanical teaching, downloadable fabrication details | Relevant to novelty and obviousness; not itself an infringement right. |
| Patent-eligibility guidance | India, US, EP | Current CRI guidance; USPTO MPEP §2104 and §2106; EPO 2026 CII and COMVIK guidance | Technical effect and statutory category | Used only for eligibility analysis, not novelty or FTO. |

USPTO’s current public-search page identifies Patent Public Search as the public system for patents and applications and Patent Center as the system for application status. The current Indian Patent Office resources page lists 2025 CRI Guidelines as the latest published examination guidance, alongside the 2017 guidance. citeturn17search1turn16search0

### Screening method

Records were first screened for at least one of five mechanical relationships: a rotary actuator acting on a pin; a cam, disk, raised surface, lever, or interposer; a guided or captured tactile pin; a modular or replaceable cell; or a physical-control feature such as calibration, sensing, sequencing, latching, or tolerance compensation.

For close records, independent claims were reviewed before dependent claims and embodiments. A disclosure appearing only in a specification was not represented as issued claim scope. An expired patent was retained as prior art but not treated as a current exclusionary right. Conversely, an active patent was not treated as an infringement problem unless its claim limitations could plausibly map to a proposed OpenBraille embodiment.

### Search limitations

**Uncertainty.** Direct, stable access to the complete Indian 5559/CHE/2014 file wrapper, current CNIPA/J-PlatPat/KIPRIS status records, and complete USPTO maintenance/prosecution histories was not achieved. Several family and status conclusions therefore remain database-supported rather than professionally docket-verified.

**Recommendation.** Before filing, licensing, manufacture, or publication, commission a patent professional to repeat the search in InPASS/Indian Patent Advanced Search, USPTO Patent Center and maintenance-fee records, the EPO Register and national validation registers, CNIPA, J-PlatPat, and KIPRIS, using the final proposed claim language rather than the present concept description.

## Verified Patent and Technical Landscape

### Family and status table

“DB status” below means a database-generated status useful for screening. “Confirmed event” means the publication or grant event itself was visible, but does not necessarily establish enforceability in every designated territory.

| Record or family | Earliest priority and applicant/assignee | Jurisdictions located | Status evidence as of cutoff | Relevance to OpenBraille | Confidence |
|---|---|---|---|---|---|
| **US20130149674A1 / US8483018B2, Braille watch** | 2011-12-08; Wisconsin Alumni Research Foundation | US | US grant confirmed; DB status reports expired for fee reasons. citeturn0search0turn11view3 | Extremely close mechanical art: rotatable disk having raised surfaces beneath guided sliding pins. Different architecture because one disk encodes multiple pins rather than six independent servos. | High for disclosure and claims; medium for current status |
| **US20130017516A1, active Braille timepiece** | 2011-07-11 | US | Publication confirmed; DB status abandoned. citeturn0search1 | Independent translational pins and CPU control; specification includes spring-lever, camshaft, and direct-drive arrangements. Timepiece limitation narrows claim relevance but not prior-art relevance. | High |
| **US11521514B2 / US11854423B1, refreshable Braille display** | Family filings culminating in 2022 continuation/grant; Pramod Kolar/Braille-display development | US | Both US grants confirmed; US11854423 issued 2023-12-26 and is reported active. citeturn0search2turn0search5turn7search3 | Pins passively retained by friction and changed by a motorized impact driver. Important for shared actuation, passive state retention, and friction-managed pins. Less close to independent servo-cams. | High |
| **WO2016074170 / US11410574B2 family** | 2014-11-12; Dot-related electromagnetic architecture | WO, US and other national members | PCT phase ceased; US grant confirmed and DB reports active, with a recorded maintenance event in 2025. citeturn1search0turn1search1turn1search3 | Layered electromagnetic low-profile cell. Less close mechanically, but important for compact construction, power, manufacturing, and active incumbent landscape. | High for family; medium-high for live status |
| **WO2020106855 / EP3884363B1 / US12548467B2 family** | 2018-11-20; Tactile Engineering/Enhanced Vision Systems lineage | WO, EP, US, JP, KR, CA and others | PCT ceased; EP B1 grant 2025-08-06 and US B2 grant 2026-02-10 confirmed. EP and US reported active; national validation not exhaustively checked. citeturn1search2turn1search4turn1search5turn7search7 | Permanent-magnet latching, coil actuation, removable top dot-capture assembly, debris membrane, mechanical collars and layered manufacture. Highly relevant if OpenBraille adopts removable capture plates or latching. | High |
| **US11915607B2, modular refreshable Braille display system** | 2020-05-29; Brailleazy | US | US grant issued 2024-02-27; DB reports active. citeturn2search1 | Modular contact units/cavities, pins and solenoids; relevant to replaceable-cell and modular manufacturing directions. | High |
| **US11645948B2 / US12080182B2, capture-plate assembly family** | 2020-03-10; current assignment reported to Enhanced Vision Systems | US | US grants confirmed; US12080182 issued 2024-09-03 and DB reports active. citeturn3search1turn4view0 | Very close to tolerance-control enhancements: top plate limits stroke; separable capture assembly; self-centering interfaces; alignment and accumulated-tolerance management; dot-state detection and cleaning modes. | High |
| **WO2013130534 / US8690576B2 lineage** | Root priority 2004-01-30; Freedom Scientific | WO, US, EP, JP and others | Later US mechanical patents reported expired by lifetime; EP and JP family members located. citeturn3search2turn5view0turn5view2 | Modular pin blocks, limit plate, removable PCB cell assembly, alignment guide and assembly method. Strong prior art against generic modularity, alignment, pin limits, and manufacturing jigs. | High |
| **US8690576B2 / US9424759B2 relationship** | Same root priority; Freedom Scientific | US | US9424759 is a child continuation in the same extended family. Both reported expired by lifetime. citeturn5view0turn5view2turn5view3 | US8690576 carries the close mechanical/manufacturing claims. US9424759 focuses more on display housing, cursor, rocker, and navigation controls and should not be treated as an equivalent mechanical claim set. | High |
| **WO2015189863A2, compliant Braille mechanism** | 2014-06-10; Indian Institute of Technology Delhi | WO/PCT and possible national paths | PCT reported ceased. citeturn2search0 | SMA wires, cantilever strips, latching, layered/half-cell construction and compliant return. Strong prior art against broadly claiming a compliant printed guide or cantilever return. | High |
| **EP4049116B1 / WO2021079101, tactile pixels** | 2019-10-22; University of Bath | EP, WO, US, GB | EP B1 grant confirmed 2024-05-01; DB reports active. citeturn10view2turn10view3 | One solenoid selectively excites multiple cantilever taxels using different resonant frequencies; 3D-printed integral frames disclosed. Relevant to shared actuation and additive manufacture, although vibrotactile rather than static Braille. | High |
| **US6881063B2 / WO2004077379 / EP1597716** | 2003-02-24; Freedom Scientific lineage | US, WO, EP | US grant confirmed; DB reports expired by lifetime in 2024. citeturn9view0 | EAP hydraulic actuation with latching and support; important for low power, holding force, displacement and response requirements, but mechanically remote from servo-cams. | High |
| **US5685721A, SMA Braille-cell display** | 1990s SMA development | US and possible foreign equivalents | US patent publication confirmed; term expired. citeturn9view1 | Early shape-memory-actuated refreshable Braille art. Relevant background against generic “low-cost non-piezo actuator” claims. | High |
| **US6743021B2, flexible-surface Braille display** | Early 2000s | US | US grant confirmed; expired term expected. citeturn9view2turn10view1 | MEMS valves, piezo or SMA devices deform an elastomeric surface; modular full-page manufacture described. Mechanically remote but relevant to scalable arrays and flexible tactile surfaces. | High |
| **US7410359B1, electromechanical tactile-cell assembly** | 2004-01-30; Freedom Scientific, now assignment reported to Enhanced Vision Systems | US | Grant confirmed; DB reports active through adjusted expiry 2026-12-09. citeturn11view0 | Manufacturability, positive and negative stops, monolithic cap, self-alignment, calibration fixtures, removable components and maintenance. Important near-term FTO review for US manufacture through expiry. | High for disclosure; medium-high for status |
| **US6902403B1, contaminant-tolerant Braille pins** | 2004-08-04; Freedom Scientific | US | Grant identified; complete live-status verification not completed. citeturn17search13 | Pin and guide geometry designed to tolerate contamination. Relevant to friction, wear, guide clearance and reliability. | Medium |
| **US6692255B2, bidirectional relative-movement tactile display** | Earlier tactile-display work | US | Grant confirmed; expired term expected. citeturn11view2 | Shared or scanning actuation using relative movement rather than one actuator per pin. Relevant to long-term shared-actuation redesign. | High |
| **Indian 5559/CHE/2014** | Filing publicly stated as 2014-11-05; Paul D’Souza alleged applicant/inventor | India; no verified foreign family found | Official publication number, claims, prosecution, grant and current status unresolved. citeturn6search0turn6search1 | Publicly alleged coverage is directly relevant to micro-motors, cams/rotors, direct or interposed lifting, cantilevers, rotation stops and low-force selectors. Cannot be ignored in Indian FTO. | Low for legal status; medium for existence and asserted subject matter |
| **MOLBED** | Public project begun 2014, published by 2016 | Non-patent, global internet disclosure | Open-source/public; creator states it was deliberately not patented. citeturn13search2turn13search7turn13search10 | Modular low-cost printed cell, commodity parts, magnetic retention, no hold power, injection-moulding scale-up. Strong obviousness art for affordability, modularity and printable manufacture. | High |
| **MagnePins** | Monash University research project | Non-patent/public technical disclosure | Public ongoing research disclosure. citeturn12search12 | Large staggered electromagnetic actuators, carriage mechanism, locking channels and maker-space fabrication. Strong against generic shared-actuation and low-cost DIY claims. | High |
| **Hackaday micro-motor/cam Braille project** | Publicly documented 2016 | Non-patent/open hardware | Public logs and drawings remain accessible. citeturn12search7turn7search0 | Six motors, cams, followers, printed compliant lever, return action, faceplate guide, modular chaining and tolerance iteration. One of the closest disclosures to the OpenBraille mechanical concept. | High |
| **Electromechanical eccentric-cam module** | Public project 2023 | Non-patent/open hardware | Public CAD/PCB/BOM project. citeturn12search5turn12search9 | Eccentric magnetic cam raises and lowers a Braille pin, resists finger back-drive and requires no hold power. Directly relevant to cam, latching, printed module and power claims. | High |
| **DotSense** | Peer-reviewed/publication record available by 2025–2026 | Scholarly non-patent art | Public abstract indexed by PubMed. citeturn12search3 | 3D-printed, ESP32-based low-cost refreshable Braille device using electromagnetic motors and camshaft mechanisms. Strong against broad ESP32, camshaft, 3D-printing and affordability combinations. | High |

### What the landscape means

The most damaging prior-art cluster is not one single “blocking patent.” It is the convergence of several independent teachings:

- rotating raised surfaces acting on guided Braille pins;
- independently controlled translational pins;
- micro-motors and cams acting directly or through followers and compliant levers;
- printed frames and guides;
- modular cells and replaceable assemblies;
- mechanical up/down stops and self-alignment;
- latching or frictional retention;
- shared or mobile actuation;
- per-cell manufacture and calibration fixtures.

That convergence makes a claim defined merely by selecting six SG90 servos and assigning one cam to each dot highly vulnerable to an obviousness combination, even if no earlier independent claim recites “SG90” by brand name.

## Claim-Level Comparison and Indian Investigation

### Independent-claim analysis of the closest records

#### Braille-watch disk family

The independent apparatus claim of US8483018B2 requires a first disk with a raised surface, pins that slide through openings in a top plate, and an actuator that rotates the disk so selected pins are raised when the raised disk surface is positioned beneath them. This is a direct claim-level disclosure of the essential rotary-surface-to-guided-pin conversion used by OpenBraille. citeturn0search0turn11view3

**Difference from OpenBraille.** OpenBraille uses one separately commanded servo and eccentric cam for each pin; the watch uses a patterned disk that controls a group of pins. That difference can establish literal novelty over this claim but does not by itself establish inventive step. Substituting separately actuated cams for a patterned disk may be viewed as a predictable way to obtain independent dot control, especially when independently actuated pins were already known.

#### Active Braille timepiece application

US20130017516A1 claims a timepiece with translational pins independently actuated under processor control. Its specification includes spring-lever, camshaft and direct-drive options. Because the cam embodiments may not all be mandatory independent-claim limitations, it is important not to overstate its enforceable scope. As prior-art disclosure, however, it supplies the motivation and engineering alternatives needed to combine independently actuated pins with cam or lever mechanisms. citeturn0search1

#### Passive-friction impact-driver family

US11854423B1’s principal claim requires pins passing through a perforated body, passively held by friction in raised and lowered positions, and a motorized impact driver that changes the pin states. It does not read directly on a servo remaining mechanically coupled to each pin. It is nevertheless close art for passive retention, friction-defined state stability, and reducing actuator count through shared setting hardware. citeturn0search2turn7search3

#### Layered electromagnetic Dot family

US11410574B2 and WO2016074170 disclose layered electromagnetic cells intended to be compact and relatively inexpensive. Their core claimed mechanism is materially different from SG90 rotary actuation. They are therefore more important as evidence of the crowded low-cost tactile-cell problem and as possible FTO constraints on future electromagnetic redesign than as anticipation of the current MVP. citeturn1search0turn1search1

#### Removable capture-assembly family

US12548467B2 claims a removable top dot-capture assembly with aligned top and bottom openings, Braille dots having mechanical constraint collars, a separate actuator-dot assembly, electromagnetic actuators, and a debris membrane. This is significantly narrower than generic modularity, but it demonstrates that removable top mechanics, travel-limiting collars, layered alignment, actuator separation and contamination control are current claimed territory. citeturn7search7

US12080182B2’s capture-plate disclosure is particularly important because it teaches that the top plate can mechanically set dot height and eliminate accumulated actuator-stack tolerances, while self-centering mating features control alignment and friction. It also discusses sensing dot movement and maintenance/cleaning behavior. Consequently, “use a plate to normalize pin height despite actuator variation” is not a safe standalone invention direction. citeturn4view0

#### Modular Brailleazy and Freedom Scientific families

US11915607B2 claims modular refreshable units using pins, cavities and replaceable actuation components. The Freedom Scientific lineage claims modular pin blocks, limit plates, removable PCB assemblies, and methods employing alignment guides. These records make generic “replace one damaged cell rather than the entire display,” “assemble with a jig,” or “use a guide plate and pin stop” claims weak. citeturn2search1turn5view2

#### Compliant IIT Delhi mechanism

WO2015189863’s independent claim centers on a compliant mechanism incorporating SMA actuation, cantilever strips and latching in a layered Braille cell. Its actuator differs, but its cantilever return and compliant layered construction are directly relevant to any proposal for a printed spring, compliant guide, or self-returning tactile structure. citeturn2search0

#### University of Bath shared-taxel family

EP4049116B1 independently claims one solenoid driven at different frequencies to selectively excite multiple cantilever taxels having different mechanical resonances. Dependent claims cover a common frame and 3D printing. It is not a static raised-dot Braille mechanism in the same sense as OpenBraille, but it demonstrates that frequency-selective shared actuation, resonant cantilevers and printed multi-taxel frames are active claimed concepts. citeturn10view2turn10view3

### Frozen-MVP feature chart

The status below asks whether the **general feature**, not the exact OpenBraille dimensions or chosen brand, is present in the reviewed art.

| Frozen-MVP feature | Scale classification | Closest art and comparison | Overall status |
|---|---|---|---|
| Six independent low-cost servos | **Scale-sensitive.** Commodity-servo envelope dominates practical cell pitch. | Independent pin actuation is explicit in US20130017516; public projects use micro-motors and SG-class servos. Exact six-SG90 arrangement is not the meaningful inventive distinction. citeturn0search1turn12search0turn12search11 | **Arguably suggested** |
| PWM control | **Scale-independent** as a control principle; timing and power effects become scale-sensitive. | Routine method for servo positioning; public Arduino/servo Braille projects disclose microcontroller servo control. | **Necessarily implied / conventional** |
| Eccentric cam | **Scale-sensitive.** Radius, eccentricity, contact stress and back-drive change with scale. | Raised disk surfaces, camshafts, micro-motor cams and eccentric magnetic cams are expressly disclosed. citeturn0search0turn0search1turn12search5turn12search7 | **Expressly disclosed** |
| Cam follower | **Scale-sensitive.** Follower stiffness, contact width and print resolution matter. | Printed cam followers and compliant levers are expressly shown in the 2016 public project. citeturn12search7 | **Expressly disclosed** |
| Sliding tactile pin | **Standard-scale validation mandatory** for a commercially meaningful Braille claim. | Guided sliding pins are core features in the watch, friction-pin and capture-plate records. citeturn0search0turn0search2turn4view0 | **Expressly disclosed** |
| Printed guide/frame | **Scale-sensitive.** FDM clearance does not transfer directly to standard pitch. | MOLBED, the Hackaday projects, EP4049116 and other public work disclose printable cells, frames or integral taxel structures. citeturn10view2turn12search5turn13search2 | **Expressly disclosed** |
| Macro scale | **Scale-sensitive by definition.** | Enlarged prototypes are an ordinary development choice; macro scale does not add a useful technical function and may reduce commercial relevance. | **Arguably suggested; not a strong differentiator** |
| Active retraction | **Scale-sensitive.** Retraction force and residual friction change with pitch and pin mass. | Bidirectional motor/cam operation, direct drive and active pin lowering are known. citeturn0search1turn12search5 | **Expressly disclosed** |
| Calibration | **Scale-independent in concept; scale-sensitive in measured parameters.** | Alignment fixtures, calibration positioning and tolerance-limiting plates are disclosed in Freedom Scientific and capture-plate art. citeturn11view0turn4view0 | **Expressly disclosed generally; exact servo method unresolved** |
| Sequencing | **Scale-independent in logic; power result is scale-sensitive.** | Processor-controlled independent pins and low-power electromagnetic architectures imply or disclose selective sequencing. | **Necessarily implied / arguably suggested** |
| Modularity | **Scale-independent concept; scale-sensitive interfaces.** | Expressly claimed or disclosed in US11915607, WO2013130534, US8690576, MOLBED and MagnePins. citeturn2search1turn3search2turn13search7turn12search12 | **Expressly disclosed** |
| Power architecture | **Scale-sensitive.** Servo rail current and brownout behavior depend on actuator size and concurrency. | Separate actuation power, latching, no-hold-power states and power-conscious drive are long-standing concerns. A recent Indian publication even claims dual-channel logic/actuator power, though it is later art for novelty depending on filing date. citeturn1search2turn13search2turn7search4 | **Arguably suggested / crowded** |
| Tactile validation | **Standard-scale validation mandatory** for practical Braille readability. | Prior patents state dot-force, displacement and response targets, and public projects report user testing, but OpenBraille has no current evidence. citeturn9view0turn13search4 | **Known requirement; OpenBraille result unresolved** |

### Indian application 5559/CHE/2014

#### Facts verified

A public 2016 statement attributed to Paul D’Souza says that application **5559/CHE/2014** was filed at the Chennai Patent Office on **November 5, 2014**. The same statement characterizes its subject matter as covering micro-motor-actuated pins, pin cantilevers, mechanical rotor stops, vertically or horizontally mounted motors with rotors or cams, direct lifting or lifting through an interposer, and a low-force selector. A contemporaneous open-hardware team treated the assertion seriously enough to discontinue that particular actuation approach. citeturn6search0turn6search1turn7search0

Independent reporting about D’Souza’s Touché system describes mobile-phone vibration motors, miniature levers and mass lifting across a multi-cell prototype, which is technically consistent with the public description of the application. citeturn7search6turn7search10

#### Matters not verified

The following were **not** retrieved from an official Indian Patent Office record:

| Required item | Verification result |
|---|---|
| Indian publication number | Not located |
| Published complete specification | Not located |
| Exact independent and dependent claims | Not located |
| Formal applicant and inventor data | Paul D’Souza is publicly identified, but not officially confirmed from the application record |
| Publication date | Not located |
| Request-for-examination history | Not located |
| Examination report, response or hearing record | Not located |
| Grant, refusal, abandonment, withdrawal or deemed-abandonment event | Not located |
| Current legal status | Unresolved |
| Foreign family or PCT equivalent | No reliable equivalent identified |

The Indian Patent Office’s current public resources and e-register pages were searched, as were exact-number and applicant/subject searches. No indexed official file was found. That absence must **not** be interpreted as proof that the application never existed, was never published, or has no enforceable descendant.

#### Consequence for OpenBraille

**FTO uncertainty is substantial in India.** The publicly asserted subject matter maps unusually closely to motors, cams, pins, cantilevers, interposers and rotation stops. Without the complete specification and current register entry, neither literal claim scope nor legal expiry can be established.

If the application remained only an unpublished provisional, was abandoned before publication, or never produced an enforceable grant, it may have little direct FTO significance. If it matured into a grant or related application with claims resembling the public description, it could be highly relevant. Both possibilities remain open.

**Recommendation.** Do not commercialize, license, submit public manufacturing files, or describe a new cam/interposer/cantilever mechanism as “infringement-free” until an Indian patent professional retrieves the official file by application number, applicant, filing date and any renumbered post-2016 identifier.

## Separate Patentability, Eligibility, and FTO Analyses

### Novelty

**Fact.** No reviewed single independent claim was found that expressly requires all of the following in one combination: six SG90-class servos, direct ESP32 GPIO PWM, one eccentric cam/follower/sliding pin per servo, macro-scale FDM guides, and the project’s exact power supply.

**Inference.** That literal difference is unlikely to create commercially meaningful novelty. Patent claims normally protect functional structures and relationships, not the retail model number of a commodity servo. A claim drafted broadly enough to matter would likely read on known rotary raised-surface pin mechanisms, independent translational pin systems, micro-motor cams and public printed lever-guide projects. citeturn0search0turn0search1turn12search7turn12search3

**Conclusion.** The frozen MVP might avoid exact anticipation under an artificially narrow claim, but such a claim would likely be easy to design around and might still fail for obviousness. The basic MVP is therefore **not a credible novelty-led patent position**.

For the proposed integrated calibration/verification direction, novelty is unresolved. The reviewed art contains each broad ingredient—hard stops, alignment, calibration fixtures, movement sensors, modular assemblies and power-conscious control—but no located independent claim clearly recites the proposed combination of:

1. low-cost rotary actuators characterized individually;
2. stored per-dot command endpoints;
3. sequential actuator-current signatures or another low-cost physical state signal;
4. mechanically limited pin height;
5. active retraction verification;
6. update behavior that isolates a failed dot while controlling supply transients.

A professional search using precisely that combination remains mandatory.

### Inventive step and obviousness

This is the largest patentability problem.

A plausible examiner combination would begin with the Braille-watch disk claim or the public micro-motor/cam Braille project for rotary cam-to-pin conversion. It could add the active-timepiece disclosure for independently actuated pins, ordinary microcontroller PWM for servo positioning, Freedom Scientific or capture-plate art for pin-height stops and alignment, and routine electrical monitoring for current-aware operation. Each addition addresses a known problem—independent dot setting, actuator control, accumulated tolerance, jamming or brownout—using a familiar technique. citeturn0search0turn0search1turn4view0turn11view0turn12search7

The open-hardware record worsens the position because it demonstrates that practitioners were already combining low-cost motors, cams, printed followers, flexible returns, faceplate guides and modular chaining. The documented need for four or five tolerance iterations also identifies the same friction and print-clearance problem OpenBraille proposes to solve. citeturn12search7

The integrated enhancement will therefore need more than “better calibration.” It needs an evidence-backed interaction among the mechanical stop, actuator characterization, state signal and sequencing that produces a technical effect not predictable from using each feature separately. Examples of potentially persuasive effects would be:

- materially lower pin-height variation despite swapping heterogeneous commodity servos;
- a large reduction in jammed or incompletely retracted pins after wear;
- reliable detection of pin-state faults without six dedicated position sensors;
- a measurable reduction in peak current or brownouts without increasing refresh latency beyond a defined threshold;
- continued tactile-state accuracy after deliberate backlash, supply-voltage and friction perturbations.

A result such as “software stores a different PWM value for each servo” is probably insufficient. Calibration tables and per-channel correction are standard engineering responses to component variation.

### Patent eligibility

A physical tactile-display apparatus, mechanical cell, manufacturing fixture, or control method that causes verified movement of real pins ordinarily falls within a patent-eligible machine, manufacture or process category in the United States. USPTO guidance nevertheless requires that the claim not merely recite an abstract calculation without significantly more. citeturn15search12turn15search16

Under current EPO guidance, a computer-implemented control claim should include the features essential to its technical effect. Software that controls a physical process can have technical character, but inventive step is supported only by features contributing to a non-obvious technical solution to a technical problem. citeturn15search0turn15search4turn15search5

The Indian Patent Office now lists 2025 CRI Guidelines as its current examination guidance. Section 3(k) risk remains relevant to claims framed as an algorithm or computer program per se; a claim tied to measured actuator behavior and physical control of pins is better positioned than one claiming a Braille translation table, generic PWM calculation or abstract sequencing policy. citeturn16search0turn16search1

**Eligibility conclusion.** Eligibility is not the principal obstacle for a properly drafted electromechanical claim. Novelty, inventive step, sufficiency and experimental support are much more serious. Firmware-only claims that merely convert characters to servo angles would be weak both technically and legally.

### Freedom to operate and infringement

Patentability and FTO are different questions:

- An expired patent can destroy novelty or make an improvement obvious while presenting no continuing patent-infringement risk.
- An active patent can present FTO risk even if the new design is independently patentable as an improvement.
- A relevant disclosure does not create infringement unless a live claim in the relevant territory covers the accused product or method.

#### Current frozen MVP

The most direct known US mechanical claim, US8483018B2, is database-reported expired for fee reasons. It remains relevant prior art but is not presently treated here as an enforceable right. The Freedom Scientific modular-mechanical descendants US8690576 and US9424759 are reported expired by lifetime. citeturn0search0turn5view0

US7410359B1 was reported active through December 9, 2026. Its independent claims are directed to piezoelectric-reed and conductive-support arrangements rather than servo-cams, so the frozen OpenBraille mechanism does not appear to map literally to its central claim limitations. Its related cap, stop, alignment and assembly concepts become more relevant if OpenBraille copies those structures. citeturn11view0

The active electromagnetic Dot/Enhanced Vision patents require electromagnetic, magnet, coil, layered stator or capture-assembly limitations not present in the frozen servo architecture. They are not presently the closest literal FTO concern, but they could become important if the team pivots to latching electromagnets, removable capture plates, actuator-dot layers or debris membranes. citeturn1search1turn7search7turn4view0

US11854423B1 requires passive friction-held pins and a motorized impact driver. The frozen one-servo-per-pin design is materially different, but a later shared hammer or mobile setter could move closer to that family. citeturn0search2

#### Territoriality

A US patent does not by itself establish infringement by experimental construction wholly in India. Importation, manufacture, sale, offer for sale or use in a country where a live corresponding right exists requires a separate territorial analysis. The EP family also requires country-by-country validation and lapse checking after grant.

#### Indian risk

5559/CHE/2014 is the most significant unresolved FTO issue because the public description overlaps the present mechanism and the project is being developed in India. No clearance can be given until the official file and any descendants are located.

#### FTO conclusion

**No FTO guarantee is possible.** The current architecture appears less exposed to the active electromagnetic families than a future electromagnetic redesign, but Indian application uncertainty prevents a clean Indian conclusion. Adoption of capture plates, passive friction retention, mobile impact actuation, resonant shared taxels or specific modular interfaces would require new claim charts.

## Candidate Invention Directions and Scale-Transfer Assessment

All prospective elements below are confidential pre-filing concepts. They should not be placed in a public repository, conference abstract, public demonstration handout, video description, or competition submission until institutional IPR and patent-professional review.

### Comparative direction table

| Direction | Nearest art | Prospective differentiating elements and scale class | Track and physical advantage required | Experiment, timing and component impact | Assessment |
|---|---|---|---|---|---|
| **Integrated tolerance-compensating mechanical/control architecture** | US12080182 capture plate; US7410359 stops/alignment; US8690576 limit plate and assembly jig. citeturn4view0turn11view0turn5view2 | A compliant or hard-limited pin guide plus stored servo-specific endpoints and fault-aware control. Mechanical stop: **scale-sensitive**. Calibration logic: **scale-independent**. Demonstrated pin-height uniformity: **standard-scale validation mandatory** for broad commercial claims. | **Track B.** Must outperform a fixed-geometry/fixed-PWM baseline across servo swaps, print variation and wear—not merely work. | Two to three weeks after baseline. Add interchangeable guide inserts, measuring jig and possibly force/current sensor. Approx. ₹300–₹900. | **Survives conditionally.** Strongest when integrated with verification; weak as a plate or guide alone. |
| **Low-cost per-dot calibration** | Freedom Scientific calibration fixture; routine servo endpoint calibration; capture-plate mechanical normalization. citeturn11view0turn4view0 | Automated discovery of minimum reliable raise/retract commands for each dot, stored with confidence margins and recalibrated after replacement. Algorithm: **scale-independent**. Endpoint values: **scale-sensitive**. Tactile outcome: **standard-scale validation mandatory**. | **Track B.** Must reduce variation or failures by a predefined, substantial amount. | One to two weeks. Height gauge, camera/metrology fixture or dial indicator; no expensive actuator change. ₹200–₹800. | **Survives only as part of an integrated system.** Per-channel PWM tables alone should be rejected. |
| **Verified tactile-state control** | US12080182 dot movement detection; broader closed-loop tactile systems; friction-pin state mechanisms. citeturn4view0turn0search2 | Verify actual raised/retracted state from a low-cost common electrical or optical signal rather than trusting command angle; identify failed dot and retry or isolate it. Sensing principle: **scale-independent**. Signal thresholds: **scale-sensitive**. Proof of real pin state: **standard-scale validation mandatory** for a practical claim. | **Track B** if one shared rail-current sensor plus sequential actuation is sufficient; otherwise may become Track C. | Two to four weeks. INA219/INA226-class current sensor or equivalent; optional optical calibration hood. ₹150–₹700. | **Survives conditionally.** Stronger than open-loop calibration, but state inference must be experimentally reliable. |
| **Compliant printed guide/return geometry** | WO2015189863 cantilevers; public printed spring lever; EP4049116 printed cantilever taxels. citeturn2search0turn12search7turn10view2 | Printed compliance that both centers a pin and supplies controlled return while decoupling lateral cam error. Compliance concept: **scale-sensitive**; fatigue and tactile force: **standard-scale validation mandatory**. | **Track B** for macro experimentation, but **Track C** for a meaningful standard-scale claim. | Three to six weeks including fatigue coupons. Material and print iterations ₹300–₹1,000. | **Weak alone; reject as primary direction.** Crowded and highly dependent on material/scale. Retain only as a subsystem of the integrated path. |
| **Scale-transfer manufacturing method** | US8690576 alignment-guide assembly; US12080182 accumulated-tolerance control; MOLBED injection-moulding plan. citeturn5view2turn4view0turn13search2 | Dimensionless design rules linking pin pitch, guide clearance, cam eccentricity, compliance and actuator offset; standardized test coupons and calibration procedure. Ratios and method: **scale-independent in formulation**; actual clearances and friction: **scale-sensitive**; practical embodiment: **standard-scale validation mandatory**. | **Track C.** Semester delivers models and test coupons; later work requires a practical-scale cell. | Semester: tolerance study and two scales, ₹500–₹1,200. Later: SLA/machining/micro-actuation likely ₹5,000–₹20,000 and three to nine additional months. | **Potential research contribution, not yet a credible standalone patent.** Manufacturing rules must produce a surprising transfer benefit. |
| **Modular replaceable architecture** | US11915607; US8690576; US12548467 removable capture assembly; MOLBED. citeturn2search1turn5view2turn7search7turn13search7 | Tool-less servo/cam/pin cartridge with automatic identity and recalibration after replacement. Mechanical cartridge: **scale-sensitive**. Identity/calibration protocol: **scale-independent**. Commercial density: **standard-scale validation mandatory**. | **Track B** at macro scale, but likely **Track C** for patent significance. | Two to four weeks, connectors and printed cartridge ₹300–₹900. | **Reject generic modularity.** Retain only if replacement automatically triggers a distinctive physical recalibration/verification process. |
| **Current-aware sequencing** | Low-power/latching families; ordinary servo power management; separate actuator/logic supply art. citeturn1search2turn7search4turn13search2 | Characterize per-servo current signatures; schedule only combinations within measured supply margin; detect abnormal friction and retry. Scheduling logic: **scale-independent**. Current model and simultaneous-dot capacity: **scale-sensitive**. | **Track B.** Must lower peak current/brownouts while preserving acceptable refresh time and state accuracy. | One to two weeks; current sensor, oscilloscope or logger, controlled supply. ₹200–₹700 beyond existing BOM. | **Weak alone but useful in combination.** Generic staggered actuation is likely obvious. |
| **Shared-actuation architecture** | US11854423 impact driver; US6692255 relative-movement display; MagnePins carriage; EP4049116 shared solenoid. citeturn0search2turn11view2turn12search12turn10view2 | One actuator selects or sets several pins through a novel routing or energy-storage mechanism. Almost all mechanical elements: **scale-sensitive** and **standard-scale validation mandatory**. | **Track C or major redesign.** Must cut actuator count and cost without unacceptable refresh time, thickness or complexity. | More than three months for a credible design; likely ₹4,000–₹15,000 depending on fabrication. | **Reject for current semester patent path.** Crowded, abandons frozen architecture and carries substantial FTO risk. |
| **Passive latching/return** | WO2020106855 permanent-magnet latching; MOLBED magnetic retention; WO2015189863 latching; eccentric magnetic-cam open project; US11854423 friction retention. citeturn1search2turn13search2turn2search0turn12search5turn0search2 | Servo cam moves through an over-center geometry or compliant detent and can be electrically released. Geometry: **scale-sensitive**; holding force/readability: **standard-scale validation mandatory**. | Track B mechanically, but patent prospects poor. | Two to four weeks, printed cam variants and force tests, ₹200–₹700. | **Reject as primary patent direction.** Dense prior art across magnetic, frictional, compliant and over-center retention. |

### Strongest surviving direction

The strongest candidate is the **integrated tolerance-compensation, calibration and verified-state architecture**, specifically because it remains technically connected to the frozen servo/cam MVP and can be tested without changing the basic actuator principle.

A credible prospective claim would need to be narrower and more physical than “calibrate each servo.” A possible claim concept for professional review—not public disclosure—would require:

1. a tactile pin whose maximum protrusion is mechanically limited independently of nominal actuator angle;
2. a low-cost rotary actuator driving the pin through a cam;
3. an initialization procedure that sequentially determines raising and retracting command regions for that individual actuator;
4. sensing of an electrical or mechanical response associated with pin/cam contact or completed travel;
5. storage of actuator-specific operating commands with margins that avoid sustained stall;
6. re-verification during refresh and controlled retry or fault isolation when the expected response is absent;
7. sequencing based jointly on requested Braille state, measured current budget and verified dot state.

The prospective interaction is that the mechanical limit defines physical output, calibration compensates commodity-servo variation, electrical verification detects failure without a full position encoder on every pin, and sequencing prevents the measurement from being obscured by simultaneous actuators while controlling the supply peak.

This is still vulnerable to an obviousness argument. It becomes credible only if experiments demonstrate that the combination solves a practical low-cost tactile-cell problem significantly better than the predictable sum of its parts.

### Semester and later-scale boundaries

#### Three-month semester deliverable

The semester deliverable should remain the frozen macro cell, augmented by:

- six independently replaceable or at least individually characterized servo-cam channels;
- a mechanically defined up-stop and explicit active-retraction path;
- common-rail current measurement with one-at-a-time diagnostic actuation;
- automated per-dot endpoint characterization;
- stored calibration and fault codes;
- fixed-PWM baseline firmware for comparison;
- measurement of dot height, retraction residual, latency, current and failures;
- at least 1,000 refresh cycles per dot, with deliberate servo swap, voltage variation and friction perturbation;
- a tolerance model and one reduced-scale guide/cam/pin test coupon.

This can plausibly remain within ₹5,000 if the existing projected BOM is near ₹2,060–₹2,850 and the team adds only current sensing, measurement fixtures, replacement servos and print iterations. The repository’s current BOM estimate and bottom-up single-dot-first sequence support that feasibility, although prices must be confirmed at procurement. fileciteturn0file3 fileciteturn0file5

#### Later technically connected work

A later extension would build a near-standard or standard-scale cell using micro-actuators or a redesigned transmission while preserving the same invention hypothesis: mechanical output normalization plus per-channel characterization and state verification for low-cost heterogeneous actuators.

Likely additions would include SLA printing or precision machining, practical-scale pins and guides, smaller actuators, force metrology, contamination testing, tactile-reader evaluation, and multi-cell density testing. This might require an additional ₹5,000–₹20,000 and three to nine months depending on institutional fabrication access.

The later work is technically connected because it tests whether the same tolerance-compensation and verification principle survives the transition from large SG90 mechanics to practical pitch. It would become an unrelated project if it abandoned rotary actuation and the calibration/verification principle entirely in favor of a conventional electromagnetic capture-plate system.

## Claim-to-Experiment Map and Final Verdict

### Claim-to-experiment map

| Prospective technical element | Closest art | Measurable technical effect | Baseline comparison | Equipment and pass/fail evidence | Macro relevance and scale requirement |
|---|---|---|---|---|---|
| Mechanically normalized maximum pin height | US12080182 top/capture plate; US7410359 positive stop | Lower between-dot and between-build protrusion variance | Existing cam geometry with pin height determined only by servo angle and print stack | Digital caliper, dial indicator or camera gauge. **Pass:** at least 50% lower standard deviation across six channels and three rebuilds without increased jamming. | Macro evidence relevant to principle; **standard-scale validation mandatory** for practical claim. |
| Individual raise/retract endpoint calibration | Calibration fixtures and ordinary servo calibration | Lower failed-raise and failed-retract rate across servo substitutions | One fixed PWM-up and PWM-down value for all six servos | Automated cycling and height/state log. **Pass:** at least 75% fewer incomplete transitions after swapping two servos and varying supply between defined limits. | Logic transfers; endpoint values do not. Reduced-scale validation required. |
| Common-sensor verified tactile state | US12080182 movement sensing; broader closed-loop art | Detect commanded-but-not-achieved state without six encoders | Open-loop assumption that commanded angle equals pin state | Rail current sensor, synchronized ADC logging and independent camera/height ground truth. **Pass:** ≥95% sensitivity and ≥95% specificity for induced jam, incomplete raise and incomplete retract over at least 300 fault-labelled events. | Macro evidence relevant to signal concept; signal separability must be revalidated at practical scale. |
| Fault-aware retry and channel isolation | General fault-control methods | Prevent one jammed channel from corrupting cell output or browning out MCU | Firmware that blindly sends commands | Inject mechanical obstruction and electrical load. **Pass:** fault identified, retry limited, MCU remains operational, healthy dots complete update. | Mostly scale-independent, but current thresholds and retry force are scale-sensitive. |
| Measured-current-aware sequencing | Low-power/latching and routine staggered control | Lower peak rail current and zero brownouts with bounded latency | Simultaneous six-servo transition | Current probe/logger, oscilloscope, ESP32 reset log. **Pass:** at least 30% peak-current reduction and zero resets over 1,000 worst-case patterns, with refresh latency below the project’s user-defined threshold. | Macro power evidence is useful but does not predict micro-actuator power density. |
| Automatic recalibration after actuator replacement | Modular prior art plus calibration | Restored height/state accuracy without manual mechanical adjustment | Replace servo and retain old common PWM values | Swap servos with measurably different deadband/endpoints. **Pass:** post-auto-calibration error returns within 10% of pre-swap calibrated performance. | Procedure is scale-independent; connector, cartridge and mechanical repeatability are scale-sensitive. |
| Wear-adaptive margin adjustment | Contaminant-tolerant pins, stops and calibration art | Maintain reliability as friction/backlash changes | Static calibration performed once | 1,000–5,000 cycles, controlled dust or added guide friction, periodic force/height/current measurements. **Pass:** calibrated system retains ≥95% valid transitions and detects degradation before functional failure. | Macro establishes algorithmic behavior; standard-scale wear/contamination testing mandatory. |
| Reduced-scale transfer rule | Alignment and manufacturing-method art | Predictable performance after geometric reduction | Direct uniform scaling without tolerance redesign | Two-scale test coupons, dimensional inspection and friction/force measurement. **Pass:** model predicts required clearance and actuation margin within predeclared error, and reduced coupon operates repeatably. | Macro plus coupon can support feasibility, but **a standard-scale cell is mandatory** before a strong commercial claim. |

The numerical thresholds above are **recommendations**, not established patent-law standards. They are intended to force the project to produce clear comparative evidence rather than attractive demonstrations.

### Evidence that would kill the patent path

The bounded patent path should be terminated or demoted if any of the following occurs:

- the official 5559/CHE/2014 claims are located and broadly cover the proposed motor/cam/interposer/calibration architecture in a still-live Indian right;
- the integrated calibrated system offers no substantial improvement over a fixed-PWM, fixed-guide baseline;
- rail-current signatures cannot reliably distinguish completed movement from jam or partial travel;
- the same results require six conventional position sensors, leaving no meaningful low-cost technical distinction;
- performance collapses after ordinary servo replacement or fewer than 1,000 cycles;
- a reduced-scale coupon shows that FDM-derived clearances and force relationships do not transfer;
- the only surviving claim language is “store a different PWM value for each servo” or “operate servos sequentially”;
- a more targeted search locates an earlier patent or public project disclosing the same combination of mechanically limited pin travel, per-actuator calibration, current-based state verification and fault-aware sequencing;
- no commercially meaningful embodiment can be described beyond the 300%-scale demonstrator.

### Direct answers to the governing questions

**Is the current servo/cam MVP itself a credible patent candidate?**
**No.** The frozen MVP is a credible semester engineering demonstrator but not, on the evidence reviewed, a defensible patent invention. The mechanical conversion, guided pins, independent control, printed fabrication and modular objectives are all known or strongly suggested.

**Must the team invent an additional mechanism?**
**Yes, if patent potential remains a primary objective.** The additional contribution need not replace the frozen servo/cam architecture during the semester, but it must be a real technical mechanism or control-mechanical interaction that produces measured physical improvement. Documentation, cost reduction, ESP32 selection and Braille encoding alone are insufficient.

**What is the strongest surviving direction?**
A tightly integrated **tolerance-normalizing, per-dot calibration and verified-state control architecture**, preferably using one shared low-cost diagnostic signal and mechanically defined pin travel, combined with current/fault-aware sequencing. No subelement should be presented alone as the invention.

**Is it achievable within ₹5,000 and the three-month window?**
A macro-scale experimental implementation is probably achievable within the absolute ceiling if the existing BOM is controlled and sensing is limited to a common current monitor, measurement jig and printed mechanical revisions. A fully persuasive practical-scale embodiment is unlikely within the same budget and window. The owner-updated three-month policy supersedes the older two-month references in earlier documents. fileciteturn0file0 fileciteturn0file3

**What evidence could kill the path?**
Failure to outperform fixed PWM, inability to verify real state, weak wear performance, non-transfer to reduced scale, direct earlier disclosure of the integrated combination, or an adverse live Indian claim.

**Should OpenBraille advance, remain conditional, or lose patent-first priority?**
**Remain conditional.** It should advance as an engineering MVP and as a bounded invention-discovery experiment, but it should not receive unconditional patent-first portfolio priority until the comparative tests show a reproducible technical effect and the Indian application is resolved. The Phase 3C portfolio decision to prioritize patent potential was a selection criterion, not proof that OpenBraille already possesses patentable subject matter. fileciteturn0file2 fileciteturn0file10

### Final research verdict

**Fact.** The prior-art field is dense across rotary pin actuation, motor/cam mechanisms, compliant returns, modular cells, additive manufacture, pin stops, latching, shared actuation and low-cost control.

**Inference.** The likelihood of obtaining useful claims on the frozen MVP is low. A narrow integrated enhancement may remain available, but only if its physical interaction and measured benefit are stronger than routine calibration and power management.

**Uncertainty.** The Indian application, several current national statuses, and the exact prior-art boundary around current-signature-based tactile-state verification remain unresolved.

**Recommendation.** Build the frozen MVP, correct the active-retraction assumption, add the minimum bounded calibration/verification architecture, execute the claim-to-experiment plan, and conduct an institutional patent-professional review before public disclosure. Do not file on “SG90 + eccentric cam + Braille pin” alone, do not describe the current design as patentable or FTO-cleared, and do not publish any newly integrated calibration/verification mechanism until the confidentiality review is complete.
