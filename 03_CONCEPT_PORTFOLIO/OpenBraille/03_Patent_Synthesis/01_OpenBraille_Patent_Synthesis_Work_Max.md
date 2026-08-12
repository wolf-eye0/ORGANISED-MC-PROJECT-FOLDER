# OpenBraille Current Patent Evidence Synthesis

**Evidence cut-off:** 31 July 2026  
**Project baseline:** the frozen OpenBraille semester MVP specified in the governing instruction  
**Purpose:** technical and patent-evidence synthesis; not a legal opinion, patentability opinion, or freedom-to-operate clearance

## 1. Executive verdict

**Primary classification: no credible patent path established.**

- **Track:** D.
- **Confidence:** Moderate, 0.72.
- **Most important limitation:** the official file, claims, prosecution history, and present legal status of Indian application `5559/CHE/2014` were not retrievable, and a claim-focused search of generic actuator-current/state-verification art could not be completed to professional-search depth. These gaps prevent both a clean negative conclusion and any positive patent recommendation.
- **Current MVP as the invention:** **No.** The frozen combination—ESP32, six commodity micro-servos, direct PWM, individual eccentric cams/followers, guided pins, active cam retraction, an FDM structure, and external 5 V power—is a useful engineering prototype, but its meaningful functional elements converge in earlier patent publications, peer-reviewed work, and public projects.

The least-weak prospective direction is a tightly integrated **mechanically referenced, per-dot calibrated, sensor-minimal verification and fault-recovery architecture**. On the evidence presently available, however, that is an experimental hypothesis rather than a credible patent path. Mechanical height stops, actuator-specific calibration, movement sensing, current-based motor-state inference, sequential control, retries, and modular replacement are individually known. No OpenBraille data yet establishes a non-additive technical effect, and common-rail servo current does not necessarily reveal the tactile pin's physical state. The direction may be reopened as a bounded Track B candidate only if the named search and pre-registered experiments in sections 18–22 pass.

This conclusion does **not** use majority voting. It follows from independent-claim text, dated public disclosures, concept fidelity, and the absence of evidence for a distinct technical interaction. Historical Phase 2 conclusions and all six independent reports were treated as leads, not authority.

## 2. Input inventory

### 2.1 File-control result

The attachment set contains **18 files total**: one governing instruction, ten numbered project/historical inputs (`01`–`10`), six independent reports (`11`–`16`), and the manifest (`99`). The governing instruction is readable. All required project-authority files are readable, including **`Project_mC_Decision_Register_v1.2.md`; v1.1 is not present**. No required input is missing, duplicated, unreadable, or ambiguously assignable.

The upload service added `(1)` or `(2)` before the extension to some names. Those suffixes are unambiguous convenience-name changes, not duplicate versions.

One control discrepancy exists: the uploaded governing file is 16,780 bytes with SHA-256 `b487647fb66611fa626ab2115f3b30e9d5e14398e02bbf430ade127d957af2ad`, whereas the manifest records 18,120 bytes and SHA-256 `9037c212a5727320911be31060a1f4b0ce590ca8c030b4c97019aa31aab60b67`. The file is nevertheless readable and internally complete through its final quality rules. The manifest is a file-control checklist, not technical evidence, so this discrepancy is recorded but is not used to alter technical conclusions.

### 2.2 Complete inventory

| No. | Attached file | Classification | Readability / control result |
|---:|---|---|---|
| 00 | `00_READ_FIRST_OpenBraille_Synthesis_Instructions(1).md` | Governing task specification | Readable; hash/size differ from manifest as stated above; governing for this synthesis |
| 01 | `01_Engineering_Design_Review(2).md` | Highest project authority | Present, readable, manifest hash/size match |
| 02 | `02_Project_mC_Decision_Register_v1.2(2).md` | Current project authority / owner decisions | Present, readable, v1.2 confirmed, manifest hash/size match |
| 03 | `03_Phase3C_Portfolio_Closure_Memo_Approved(2).md` | Current project authority | Present, readable, manifest hash/size match |
| 04 | `04_Phase3C_OpenBraille_Architecture_Report_Final(2).md` | Current project architecture | Present, readable, manifest hash/size match |
| 05 | `05_Phase3C_OpenBraille_Memory_Final(2).md` | Current project memory | Present, readable, manifest hash/size match |
| 06 | `06_Phase3C_OpenBraille_SOP_Final(2).md` | Current project procedure | Present, readable, manifest hash/size match |
| 07 | `07_Concept_Evidence_Matrix(2).md` | Validated down-selection evidence | Present, readable, manifest hash/size match |
| 08 | `08_Uncertainty_and_Test_Register(2).md` | Validated uncertainty/test evidence | Present, readable, manifest hash/size match |
| 09 | `09_Patent_Research_Input_Pack(2).md` | Current patent-research framing | Present, readable, manifest hash/size match |
| 10 | `10_Phase2_Report_by_Claude(2).md` | Historical patent leads only | Present, readable, manifest hash/size match; conclusions not treated as current facts |
| 11 | `11_OpenBraille_Patent_Research_ChatGPT_DR.md` | Independent report — **ChatGPT Deep Research** | Present, readable, complete, manifest hash/size match |
| 12 | `12_OpenBraille_Patent_Research_Gemini.docx` | Independent report — **Gemini Deep Research** | Present, readable after DOCX extraction, complete, manifest hash/size match |
| 13 | `13_OpenBraille_Patent_Research_Perplexity.docx` | Independent report — **Perplexity Deep Research** | Present and readable but **partial**: ends in §8.2 after “Nearest prior art: per-pin calibration in EM-l”; reference material follows; no complete final verdict |
| 14 | `14_OpenBraille_Patent_Research_Qwen.md` | Independent report — **Qwen Deep Research** | Present, readable, complete, manifest hash/size match |
| 15 | `15_OpenBraille_Patent_Research_Mistral.md` | Independent report — **Mistral** | Present, readable, complete, manifest hash/size match |
| 16 | `16_OpenBraille_Patent_Research_Microsoft_Copilot.docx` | Independent report — **Microsoft Copilot** | Present, readable after DOCX extraction, complete, manifest hash/size match |
| 99 | `99_INPUT_MANIFEST.md` | File-control checklist; not technical authority | Present and readable; expected count and model lanes confirmed |

**Partial-report treatment:** Perplexity material through the completed §8.1 was audited on its own merits. Its §8.2 fragment and all absent later analysis are excluded. No missing conclusion or verdict was inferred.

### 2.3 Project-authority reconciliation

The governing owner overrides control this report: up to three months; one approximately 300%-scale six-dot cell; approximately 7 mm pitch and 1.5 mm protrusion; ESP32-WROOM-32; six SG90-class servos; one eccentric cam/follower/sliding pin per dot; direct GPIO PWM; FDM frame/guides/cams; external 5 V; preferred cost at or below ₹3,000 and hard ceiling ₹5,000; five-member team. Retraction is **active servo-driven cam retraction unless physical inspection proves a usable passive return**.

This last point corrects the architecture report's unsupported assumption that an SG90-integral torsion spring will reset the tactile mechanism. The project must inspect the actual servos and test the coupled mechanism. A commanded “self-test” also cannot verify travel without an independent physical observable.

## 3. Research-report reliability audit

Ratings apply to the report as evidence, not to the source model's reputation.

| Report | Concept fidelity and search breadth | Primary-source / claim use | Material defects found | Reliability and permitted use |
|---|---|---|---|---|
| **ChatGPT Deep Research** | High fidelity to the frozen servo/cam architecture; broad US/WO/EP/Indian and non-patent search; correctly separates active retraction and scale | Strongest claim-level treatment; usually distinguishes claim, specification, database status, novelty, and FTO | Current-state conclusions often rely on Google/database status rather than an official register; proposed current-signature sensing is technically plausible but not demonstrated; some broad family/status statements need official confirmation | **Medium reliability overall.** High for located publication text and search leads; medium for family/status; proposed Track B conclusion not adopted without evidence |
| **Gemini Deep Research** | Broad landscape, but several records are mischaracterized | Heavy use of Google/secondary summaries; uneven independent-claim analysis | Treats `US20130017516A1` as input keys rather than an active Braille timepiece; describes `US6902403B1` as a linkage; assigns unsupported/incorrect status to `US8483018B2`, `5559/CHE/2014`, and `US7410359`; routine calibration/sequencing is promoted too readily | **Low reliability.** Retain search leads and experiment ideas only; exclude legal-status and positive patentability conclusions |
| **Perplexity Deep Research** | Good breadth and generally correct frozen-MVP comparison through completed material | Some claim summaries, but several citations resolve to Perplexity mirrors and status labels are not official | Partial document; ends during §8.2; no verdict; overstates live status for old US records and loosely groups technical lineages; older cam leads were not independently retrieved here | **Medium for completed material through §8.1; excluded from §8.2 onward.** No inferred conclusion |
| **Qwen Deep Research** | Material concept contamination with unrelated “OpenBraille”/Marlin material | Weak source discipline and family construction | Misidentifies `US6354839B1`; constructs a false `US6743021/US8690576/US9424759` family; uses unrelated `US20130203022A1` to infer the Indian application's claims; conflates `WO2020106855` with MagnePins; misstates eligibility and family/status findings | **Low; excluded in part.** Exclude family, status, FTO, eligibility, and external-project conclusions; retain compliant-geometry ideas only as unverified prompts |
| **Mistral** | Shallow searches and broad similarity judgments | Limited independent-claim analysis; many uncited or secondary status assertions | Misdescribes MOLBED; infers Indian claims/status; repeats incorrect family/status propositions; treats ordinary calibration and sequencing as stronger than evidence permits | **Low; excluded in part.** Retain only generic conventionality warnings and possible tests |
| **Microsoft Copilot** | Covers requested headings but often substitutes summary confidence for verification | Traceability is weak; multiple tables give conclusions without primary claim support | False family conflations among `US11410574B2`, `WO2015189863`, and `EP4049116`; unsupported assertion that `5559/CHE/2014` expired; unsupported reset assumptions; misleading relationships for `US5685721` and `US6743021` | **Low; excluded in part.** Exclude family, Indian, legal-status, eligibility, and FTO conclusions; retain only high-level need for calibration/testing |

### 3.1 Conflict resolution

The reports agree that the broad low-cost Braille-cell field is crowded, but agreement is not the basis for the verdict. The controlling evidence is:

1. independent claims and dated specifications for the rotary-disk, independent-pin, passive-friction, electromagnetic, capture-plate, modular-block, compliant, and shared-actuation records;
2. dated public demonstrations of micro-motor/cam, micro-servo, printed-guide, and eccentric-cam Braille mechanisms;
3. project evidence showing that passive return, current margin, tolerance, tactile validation, and real state verification remain untested; and
4. the absence of a demonstrated interaction that distinguishes the proposed integrated enhancement from a predictable aggregation.

## 4. Search coverage and evidence gaps

### 4.1 Coverage achieved

- The named US, WO, and EP publications were screened at claim level where readable publication text was available.
- PCT/national-family navigation covered the principal Dot/Enhanced Vision, Freedom Scientific, IIT Delhi, University of Bath, Brailleazy, and early actuator lineages.
- Non-patent searching covered peer-reviewed micro-servo/cam work and public micro-motor, eccentric-cam, MOLBED, and MagnePins projects.
- The exact Indian application number, named individual, filing date, and mechanism phrases were searched in official and public channels.
- Generic actuator-current/position and anomaly-detection patent records were sampled to test whether a “single current sensor verifies position” proposition is field-exclusive. It is not.

### 4.2 Evidence limits that control the conclusion

| Gap | Consequence | Required separate Deep Research / professional verification |
|---|---|---|
| No official file for `5559/CHE/2014` | Exact claim scope, publication, descendants, applicant, and current Indian legal effect are unknown | Retrieve the file from the Indian Patent Office by application number, filing date, applicant/inventor, and any renumbered publication; obtain complete specification, claims, FER/hearing history, renewal/status, and family search |
| Official current status not independently extracted for most US/EP/national records | Google “active/expired/ceased” labels are status signals, not legal conclusions | USPTO Patent Center/maintenance records; European Patent Register and national-validation registers; official CA/JP/KR/CN records |
| No exhaustive CPC/keyword claim search for current-based state sensing in tactile displays and cheap servo mechanisms | The least-weak direction may already be claimed or may be an obvious use of generic motor diagnostics | Search claims and forward/backward citations across G09B21/003, G09B21/004, G06F3/016 plus motor-control/current-signature classes and non-English equivalents |
| `US5685721` and older `US5453012`/`US5766014` claim text was not directly retrievable in this run | These records cannot carry a claim-level anticipation finding | Retrieve official images/OCR and prosecution/family data; until then use only corroborated disclosure leads |
| Foreign-family translations and live national status incomplete | Country-specific FTO cannot be concluded | Native-office claim/status review for each intended manufacture/use/sale territory |
| No OpenBraille hardware measurements | Calibration, current signatures, pin-state inference, fatigue, supply adequacy, tactile recognition, and scale transfer are unproven | Execute the pre-registered experiments in section 18 before any patent-positive statement |

No missing web record was converted into a verified finding. In particular, absence of an indexed Indian record is not evidence of abandonment, and a PCT “ceased” signal says nothing conclusive about live national rights.

## 5. Verified patent-family ledger

“DB signal” below means the bibliographic/legal-event label displayed by Google Patents or a similar discovery database. It is **not** an official current-status conclusion. Grant/publication identifiers and claim text are treated separately from legal effect.

| Identifiers / technical family | Priority; applicant/assignee | Jurisdictions located | Publication / official-status position at cut-off | Independent-claim subject and relevance | Novelty / FTO significance | Confidence and primary publication |
|---|---|---|---|---|---|---|
| `US20130149674A1`, `US8483018B2` | 8 Dec 2011; Wisconsin Alumni Research Foundation | US | US A1 and B2 publications confirmed; DB signal “expired—fee related”; official maintenance status not independently extracted | Braille watch with a rotatable disk having a raised surface, guided sliding pins, and an actuator rotating the disk to raise selected pins; specification expressly identifies a hobby servo | **Very high novelty/obviousness relevance** to rotary surface-to-pin conversion; current US FTO likely lower if lapse confirmed, but unresolved here | High claim confidence; medium status confidence. [US8483018B2](https://patents.google.com/patent/US8483018B2/en) |
| `US20130017516A1` | 11 Jul 2011; Tyler Kelly identified in record | US | A1 publication confirmed; DB signal abandoned; official file status not extracted | Timepiece with processor-controlled, independently actuated translational tactile pins; specification includes spring-lever, camshaft, and direct-drive options | High disclosure/obviousness relevance; timepiece limitations reduce literal claim overlap; FTO low only if abandonment is officially confirmed | High claim/disclosure confidence; medium status. [US20130017516A1](https://patents.google.com/patent/US20130017516A1/en) |
| `US11521514B2`, `US11854423B1` | Later US filings; Pramod Kolar identified | US | Two grant publications confirmed; DB signal active; live scope/status unresolved officially | Perforated body and pins passively held by friction in raised/lowered states, changed by a motorized impact driver | High against friction retention, shared setting, and “no hold power”; frozen continuously coupled per-dot servos differ; future shared hammer raises FTO concern | High claims, medium live status. [US11854423B1](https://patents.google.com/patent/US11854423B1/en), [US11521514B2](https://patents.google.com/patent/US11521514B2/en) |
| `WO2016074170A1`, `US11410574B2` and national family | 12 Nov 2014; Dot-related applicants/assignees | WO, US, CN and other members shown in family data | PCT publication and US grant confirmed; WO phase DB signal ceased; US DB signal active; national live status unresolved | Layered electromagnetic tactile cell; US claim centers on layered module construction and touch-panel/display relationships | Medium background novelty relevance; low literal overlap with servo/cam baseline; significant FTO only for an electromagnetic/layered redesign | High claim/family identification; medium status. [WO2016074170A1](https://patents.google.com/patent/WO2016074170A1/en), [US11410574B2](https://patents.google.com/patent/US11410574B2/en) |
| `WO2020106855A1`, `EP3884363B1`, `US12548467B2`, `CA3120784A1`, `JP2022508168A`, `KR20210092296A` | 20 Nov 2018; Tactile Engineering / Enhanced Vision Systems lineage shown in records | WO, EP, US, CA, JP, KR and others | WO publication; EP B1 dated 6 Aug 2025 and US B2 dated 10 Feb 2026 confirmed; DB signals active for US/EP; official national validation/status unresolved | US claim: removable top dot-capture plates/openings/collars, separate actuator-dot assembly, electromagnetic actuator/driver and membrane; EP claim likewise separates tactile and electromagnetic units with a membrane | High against generic removable top, collar stop, layered alignment, calibration, membrane, and latching directions; material FTO risk if those claimed structures are adopted | High claims/family; medium live status. [WO2020106855A1](https://patents.google.com/patent/WO2020106855A1/en), [EP3884363B1](https://patents.google.com/patent/EP3884363B1/en), [US12548467B2](https://patents.google.com/patent/US12548467B2/en) |
| `US11915607B2` | 29 May 2020; Brailleazy shown in record | US | B2 grant dated 27 Feb 2024 confirmed; DB signal active; official live status unresolved | Mobile-device case/system having cavities, movable pins and a controller; dependent claims narrow to actuators such as solenoids | Medium against broad “modular” or case-integrated claims; title alone does not establish a modular cartridge claim; limited literal overlap with standalone servo cell | High claim text, medium status. [US11915607B2](https://patents.google.com/patent/US11915607B2/en) |
| `US11645948B2`, `US12080182B2` | 10 Mar 2020; assignment signals Enhanced Vision Systems | US | Both grant publications confirmed; `US12080182B2` dated 3 Sep 2024; DB signal active; official status unresolved | `US12080182B2` claim 1 centers on dot capture/top assemblies separated by a membrane and a capacitive layer. Its **specification**, not necessarily the independent claim, teaches dot-height stops, self-centering interfaces, tolerance isolation, cleaning, and movement detection | Very high disclosure/obviousness relevance to tolerance normalization and sensing; live-claim FTO depends on adopting the claimed layered/membrane/capacitive combination | High claim/disclosure distinction; medium status. [US12080182B2](https://patents.google.com/patent/US12080182B2/en), [US11645948B2](https://patents.google.com/patent/US11645948B2/en) |
| `WO2013130534A1` and related modular-display members | Root priority stated in records as 30 Jan 2004; Freedom Scientific / Enhanced Vision Systems lineage | WO, US, EP, JP and others | WO publication confirmed; national legal status not comprehensively verified | Modular mounting blocks, pin collars/stops, removable cell/PCB components, alignment guides, and construction methods | High against generic modular replacement, self-alignment, pin-limit, and jig claims; FTO jurisdiction/status dependent | High disclosure; medium status. [WO2013130534A1](https://patents.google.com/patent/WO2013130534A1/en) |
| `US8690576B2`, `US9424759B2` | Same extended 2004-root Freedom Scientific lineage | US | Grants confirmed; DB signals expired by lifetime; official expiry not independently extracted | `US8690576B2` carries closer modular cell/manufacturing features; `US9424759B2` emphasizes display housing, cursor/rocker/navigation and should not be treated as an identical claim set | High prior-art relevance even if expired; low current FTO only after official expiry confirmation | High claims/relationship; medium status. [US8690576B2](https://patents.google.com/patent/US8690576B2/en), [US9424759B2](https://patents.google.com/patent/US9424759B2/en) |
| `WO2015189863A2` | 10 Jun 2014; Indian Institute of Technology Delhi | WO/PCT; Indian priority `1575/DEL/2014`; any national paths require verification | PCT publication confirmed; DB signal ceased; no conclusion on Indian/national rights | SMA wires with cantilever strips, compliant/latching action, layered construction and modular/half-cell arrangements | High against broad compliant return, cantilever, latch, and layered modularity; different actuator reduces literal overlap with servo baseline | High publication claims; low-to-medium national status. [WO2015189863A2](https://patents.google.com/patent/WO2015189863A2/en) |
| `EP4049116A1/B1`, `WO2021079101` | 22 Oct 2019; University of Bath | EP, WO, GB and other family signals | EP A1/B1 and WO publications confirmed; DB signal granted/active; country validation unresolved | One solenoid driven at different frequencies to selectively excite multiple resonant cantilever taxels; printed integral frames appear in dependent/disclosure material | High against frequency-selective shared actuation; mechanically remote from static servo/cam dots; FTO relevant only to that redesign | High claims/family; medium status. [EP4049116B1](https://patents.google.com/patent/EP4049116B1/en) |
| `US6881063B2`, `WO2004077379`, `EP1597716` | 24 Feb 2003; Freedom Scientific lineage | US, WO, EP | Publications/grant confirmed; DB signal US expired by lifetime; official expiry unresolved | Electroactive-polymer/hydraulic Braille actuation with latching/support, defined displacement/force concerns | Medium general low-power/retention art; low literal servo overlap; prior-art relevance persists after expiry | High claims, medium status. [US6881063B2](https://patents.google.com/patent/US6881063B2/en) |
| `US5685721` | 1990s; American Research Corporation of Virginia shown in secondary record | US; foreign equivalents unresolved | Existence and title corroborated; direct claim image/status not retrieved in this run; term would ordinarily be old but no official conclusion made | Reported SMA-actuated refreshable Braille cell with tubes/modules | Background only; **not load-bearing** for claim anticipation or FTO here | Low-to-medium. Corroborating discussion in [US6743021B2](https://patents.google.com/patent/US6743021B2/en); direct official record required |
| `US6354839B1`, `US6743021B2` | `US6743021` is a continuation-in-part of the Orbital Research `US6354839` line | US | Grant publications confirmed; DB signals old/expired or fee-related; official status unresolved | MEMS valves or piezo/SMA devices deform a continuous elastomeric tactile surface; not a micro-motor/cam “Paul D'Souza” family | Medium general actuator-array art; low literal overlap; useful for correcting report hallucinations | High relationship/claims, medium status. [US6354839B1](https://patents.google.com/patent/US6354839B1/en), [US6743021B2](https://patents.google.com/patent/US6743021B2/en) |
| `US7410359B1` | 30 Jan 2004; Freedom Scientific / Enhanced Vision Systems assignment signals | US | B1 grant confirmed; DB reports adjusted expiry 9 Dec 2026; official live status not extracted | Piezoelectric reeds and conductive supports in a tactile cell; specification/claims address cap, stops, alignment, calibration, and removal | High prior art against generic stops/alignment/calibration; central piezo limitations reduce literal servo overlap; near-term US FTO check warranted if copying interfaces | High claims; medium live status. [US7410359B1](https://patents.google.com/patent/US7410359B1/en) |
| `US6902403B1` | 4 Aug 2004; Freedom Scientific | US | Grant confirmed; DB signal old/expired; official status unresolved | Pin and guide cross-sections, shoulders/overhangs and contact geometry configured to tolerate contamination | High against debris-tolerant clearance/guide geometry; low literal risk unless its claimed geometry is used | High claim text; medium status. [US6902403B1](https://patents.google.com/patent/US6902403B1/en) |
| `US6692255B2` | Earlier tactile-display work; US Government assignee shown | US | Grant confirmed; DB signal expired by lifetime; official status unresolved | Static/shared actuators combined with relative bidirectional movement to set pins that retain state | High against actuator-reduction/shared-carriage ideas; low current FTO if official expiry confirmed | High claims; medium status. [US6692255B2](https://patents.google.com/patent/US6692255B2/en) |
| `5559/CHE/2014` | Publicly stated filing 5 Nov 2014; Paul D'Souza publicly associated | India; no verified family | **No official publication, claims, prosecution, grant, lapse, abandonment, or family was retrieved** | Public statements allege micro-motor-actuated pins, cantilevers, rotor stops, vertical/horizontal motors with rotors/cams, direct/interposed lift, and a low-force selector | Potentially the closest Indian FTO issue; cannot support novelty or infringement conclusions without the file | Medium for public assertion/existence; **low for legal scope/status**. [Contemporaneous project log](https://hackaday.io/project/10849-refreshable-braille-display/log/40208-discontinuing-work-on-current-actuation-method) |

## 6. Closest independent-claim analyses

### 6.1 Rotary raised surface and guided pins — `US8483018B2`

Claim 1 requires a Braille watch, a disk with a raised surface, pins sliding through openings in a top plate, and an actuator that rotates the disk so its raised region raises selected pins. The specification expressly gives an HS-55 sub-micro servo and PWM as an embodiment. This is claim-level evidence for rotary-actuator-to-raised-surface-to-guided-pin conversion, not merely an abstract resemblance.

OpenBraille differs because each of six pins has its own servo/cam rather than one patterned disk controlling four pins in a time display. Those differences can avoid literal anticipation by this claim. They do not, without more, establish inventive step because independently controlled tactile pins and servo/cam alternatives were already public. [Claim text](https://patents.google.com/patent/US8483018B2/en#claims)

### 6.2 Independently actuated pins — `US20130017516A1`

The independent claim is directed to an active Braille timepiece with translational pins independently actuated under processor control. The specification lists spring-lever, camshaft, and direct-drive arrangements. The timepiece context limits literal claim overlap, and not every disclosed cam embodiment is an independent-claim limitation. As a prior-art disclosure, however, it supplies the separate-pin control concept and the express motivation to use cam/lever options. [Claim text](https://patents.google.com/patent/US20130017516A1/en#claims)

### 6.3 Passive friction and shared impact actuation — `US11854423B1`

Claim 1 requires a perforated body, pins movable between front and rear states, friction that passively retains the pins, and a motorized impact mechanism that changes state. OpenBraille's servo remains coupled through its cam and the governing baseline requires active retraction, so the claim is not a direct read on the frozen system. It nevertheless occupies the design space for passively held pins and reduced/shared actuation. A future friction latch or mobile hammer would require a fresh claim chart. [Claim text](https://patents.google.com/patent/US11854423B1/en#claims)

### 6.4 Layered electromagnetic cell — `US11410574B2` / `WO2016074170`

The US independent claim centers on a layered electromagnetic tactile-display module and related interface structure. Coils, magnetic elements, layered stator/actuator construction, and reset springs distinguish it from SG90 rotary cams. It does not anticipate the frozen mechanical combination, but it is active-landscape evidence against treating “low-cost compact non-piezo actuation” as a new problem. It becomes materially closer if the project pivots to electromagnetic layers. [US claim text](https://patents.google.com/patent/US11410574B2/en#claims)

### 6.5 Removable capture assembly — `US12548467B2` / `EP3884363B1`

The recently granted US claim requires a removable top dot-capture assembly with aligned plates/openings, dot collars, a separate actuator-dot capture assembly, electromagnetic actuation/driver structure, and a membrane. The EP claim likewise separates tactile elements from electromagnetic elements across a membrane. The exact claimed combination is narrower than “use a guide plate,” but the family is powerful disclosure and obviousness evidence for dot-height constraints, separable top mechanics, debris control, calibration, and layered alignment. A servo cell does not satisfy the electromagnetic limitations merely because it uses a removable guide. [US claim text](https://patents.google.com/patent/US12548467B2/en#claims), [EP claim text](https://patents.google.com/patent/EP3884363B1/en#claims)

### 6.6 Capture plate, membrane, and sensing — `US12080182B2`

Claim 1 is not a generic tolerance-normalization claim: it requires specified capture/top assemblies, a separating membrane, and a capacitive layer. The specification separately teaches mechanically setting protrusion with top/bottom constraints, self-centering mating surfaces, reducing accumulated actuator-stack tolerance, sensing movement/touch, and cleaning modes. This distinction matters. The claim may not literally cover a simple printed hard stop; the specification still makes a standalone “hard stop normalizes height” contribution difficult to defend as inventive. [Claim and specification](https://patents.google.com/patent/US12080182B2/en)

### 6.7 Modular case/system — `US11915607B2`

Claim 1 concerns a mobile-device case/system with cavities, movable pins, and controller relationships; dependent claims add actuator details. The title “modular refreshable Braille display system” is not proof that every cartridge/self-alignment idea is claimed. The record is relevant to modular pin units and replaceable structures, but any FTO conclusion must map the proposed OpenBraille interface to an actual live claim. [Claim text](https://patents.google.com/patent/US11915607B2/en#claims)

### 6.8 Freedom Scientific modular lineage — `WO2013130534`, `US8690576`, `US9424759`, `US7410359`

The close mechanical teachings include mounting blocks, stop/limit plates, removable cell/PCB components, monolithic caps, self-alignment, and assembly guides. `US8690576B2` contains the closer construction claims. `US9424759B2` is a later continuation with more emphasis on enclosure, navigation, cursor, and controls; it is not interchangeable claim text. `US7410359B1` claims piezo-reed/support structures despite its useful stop/alignment disclosure. Together these records substantially weaken generic modularity, replaceability, assembly-jig, and pin-stop directions, but they do not automatically establish infringement by the frozen servo cell. [US8690576 claims](https://patents.google.com/patent/US8690576B2/en#claims), [US9424759 claims](https://patents.google.com/patent/US9424759B2/en#claims), [US7410359 claims](https://patents.google.com/patent/US7410359B1/en#claims)

### 6.9 Compliant and shared actuation — `WO2015189863`, `EP4049116`, `US6692255`

`WO2015189863` claims SMA wires, cantilever strips, latching, and a layered compliant Braille-cell mechanism. `EP4049116B1` claims one solenoid driving different-frequency resonant cantilever taxels. `US6692255B2` claims relative motion between actuators and passively retaining pins. These mechanisms differ from one servo per dot, but they directly crowd compliant return, printed cantilever, resonant selector, shared-actuator, and moving-carriage proposals. [WO2015189863 claims](https://patents.google.com/patent/WO2015189863A2/en#claims), [EP4049116 claims](https://patents.google.com/patent/EP4049116B1/en#claims), [US6692255 claims](https://patents.google.com/patent/US6692255B2/en#claims)

### 6.10 Older EAP, SMA, MEMS, and contaminant-tolerant cells

`US6881063B2` claims electroactive-polymer/hydraulic tactile actuation and latching; `US6743021B2` claims MEMS/piezo/SMA structures deforming a continuous elastomeric surface; `US6902403B1` claims contaminant-tolerant pin/guide cross-sections and shoulders. These are not close literal servo/cam claims, but they defeat broad propositions such as “replace piezo with a low-cost actuator,” “use compliance,” or “solve print friction with guide clearance” without a more specific technical contribution. `US5685721` was not used for claim-level conclusions because its claim record was not directly retrieved. [US6881063 claims](https://patents.google.com/patent/US6881063B2/en#claims), [US6743021 claims](https://patents.google.com/patent/US6743021B2/en#claims), [US6902403 claims](https://patents.google.com/patent/US6902403B1/en#claims)

## 7. Frozen-MVP closest-art feature chart

The status column uses only the governing categories. It compares the general functional feature, not the exact retail part number or enlarged dimensions.

| Frozen-MVP feature | Closest evidence | Status |
|---|---|---|
| Six independent commodity servos, one per dot | Independent pin control in `US20130017516A1`; micro-servo Braille papers; public micro-motor/cam projects. Exact “six SG90” is a procurement choice, not a meaningful technical boundary | arguably suggested |
| Direct GPIO PWM | Servo/PWM control is express in the Braille-watch specification and routine in micro-servo implementations | expressly disclosed |
| Eccentric cam | Rotating raised surfaces, camshafts, micro-motor cams, and eccentric magnetic cams all predate the project | expressly disclosed |
| Cam follower | Printed follower/compliant lever is shown in the 2016 public project | expressly disclosed |
| Vertically translating tactile pin | Core element of the watch, independent-pin, friction-pin, capture-plate, and modular-cell records | expressly disclosed |
| Printed frame and guide | Public printed Braille projects and printed-taxel patent disclosures | expressly disclosed |
| Approximately 300% macro construction | Enlarged prototypes are an ordinary development choice; no special functional effect was identified | arguably suggested |
| Active servo-driven cam retraction | Bidirectional motor/cam or direct pin actuation is described in earlier disclosures | expressly disclosed |
| Per-dot calibration | Servo endpoint calibration, mechanical calibration, alignment fixtures, and dot-height normalization are known; the exact OpenBraille procedure is not yet defined | arguably suggested |
| Current-aware sequencing | Selective/sequential actuation and generic motor-current control are known; a specific tactile effect is not established | arguably suggested |
| Modular replacement | Modular blocks/cells, removable capture assemblies, MOLBED, and MagnePins | expressly disclosed |
| Tactile-state verification | Movement/touch sensing is disclosed, but the proposed inference of actual pin state from one shared servo-current signal remains unproven | unresolved |
| Tolerance compensation | Stops, collars, capture plates, self-centering interfaces, and contaminant-tolerant guides | expressly disclosed |
| External 5 V logic/actuator power architecture | Separate/managed actuation power and low-power/latching concerns are routine; the adequacy of this specific 5 V source is untested | necessarily implied |
| Character-to-dot mapping | Processor-controlled conversion of information/time/text to raised-dot states is longstanding | expressly disclosed |
| Tactile and mechanical validation | Force, displacement, response, lifecycle, and user-validation requirements are known; OpenBraille's results do not yet exist | unresolved |

The chart does not imply that one item anticipates the entire MVP. Its significance is combinatorial: the differences largely appear to be selection, scaling, substitution, and aggregation of known elements.

## 8. Indian application 5559/CHE/2014 investigation

### 8.1 Confirmed material

A dated public log states that `5559/CHE/2014` was filed in the Chennai Patent Office on **5 November 2014** and attributes it to Paul D'Souza. The same log describes alleged coverage of micro-motor-actuated pins, pin cantilevers, mechanical rotor stops, motors mounted vertically or horizontally, rotors/cams lifting pins directly or through an interposer, and a low-force selector. A contemporaneous Hackaday article reports the project and patent concern. [Project log](https://hackaday.io/project/10849-refreshable-braille-display/log/40208-discontinuing-work-on-current-actuation-method), [contemporaneous article](https://hackaday.com/2016/04/28/refreshable-braille-display-and-braille-keyboard/)

This confirms only that the public assertion existed and was technically specific enough to influence another project. It does not confirm official claim scope or legal effect.

### 8.2 Unresolved official facts

No official Indian Patent Office record was retrieved that established:

- the publication number or whether a complete specification was published;
- the actual applicant and inventor entries;
- independent or dependent claim text;
- a request for examination, First Examination Report, response, hearing, amendment, division, or renumbering;
- grant, refusal, withdrawal, abandonment, deemed abandonment, renewal, lapse, or expiry;
- a PCT or foreign family; or
- present enforceability in India.

The [Indian Patent Office public-search portal](https://iprsearch.ipindia.gov.in/PublicSearch/) did not yield a usable indexed file in this run. That absence is **not** proof that the application was abandoned or never existed. Gemini, Qwen, Mistral, and Copilot assertions that it was abandoned, expired, or otherwise non-blocking are excluded.

### 8.3 Consequence

The public description overlaps the frozen mechanism unusually closely. It is therefore the leading unresolved Indian FTO issue, but it cannot be used as verified novelty-destroying claim evidence and cannot support an infringement conclusion. Before manufacture, public CAD release, licensing, sale, or offer for sale in India, an Indian patent professional or the separate Deep Research synthesis should retrieve the complete official file and descendants.

## 9. Non-patent prior art

| Dated public material | What it actually teaches | Significance and evidence limit |
|---|---|---|
| Aryan et al., **“Refreshable Braille Module Using Cam Actuated Mechanism”** (2021) | Two SG90-class micro-servos drive nested camshafts/cam sets through eight angular states; character-specific calibration is discussed | Strong peer-reviewed evidence against broad servo + cam + character-calibration novelty; architecture differs from six independent cams. [DOI](https://doi.org/10.1088/1757-899X/1123/1/012028) |
| Rahman et al., micro-servo Braille display (2018) | A low-cost single-cell refreshable Braille mechanism using micro servos | Strong against “use micro servos for a Braille cell” as the contribution. [IEEE record](https://ieeexplore.ieee.org/document/8641028/), [DOI](https://doi.org/10.1109/ICIEV.2018.8641028) |
| Brindle, single-cell micro-servo/slider work (2023) | Micro servos and slider mechanics in a low-cost single-cell device | Further crowds servo/slider/low-cost implementation; performance figures require paper-level review. [IEEE record](https://ieeexplore.ieee.org/document/10456453/) |
| Refreshable Braille Display public project (logs public by 2016) | Micro motors/cams, followers/compliant levers, printed faceplate guides, tolerance iterations, modular chaining; earlier micro-servo efforts also discussed | One of the closest public disclosures to the frozen mechanical idea; user-generated project record, so dates/files should be preserved for any formal invalidity search. [Project logs](https://hackaday.io/project/10849-refreshable-braille-display/logs?sort=oldest) |
| Electromechanical Refreshable Braille Module (2023) | Printed module with electromagnetic polarity rotating an eccentric cam containing a magnet; raises/lowers a pin and holds without continuous power | Direct public evidence for eccentric cam, printed module, pin stability, and low hold power; actuator differs. [Project details](https://hackaday.io/project/191181-electromechanical-refreshable-braille-module/details) |
| MOLBED (public by 2016) | Modular low-cost printed display; magnetic retention/solenoid concepts; commodity manufacture and no-hold-power goals | Strong against generic low cost, modularity, printed manufacture, and passive magnetic retention; it is not a servo/cam device. [MOLBED instructions](https://www.instructables.com/MOLBED-Modular-Low-Cost-Braille-Electronic-Display/) |
| MagnePins (UIST 2025) | Shared/moving carriage with staggered electromagnetic actuators sets pins retained in printed locking channels; maker-oriented fabrication and standard-spacing intent | Strong against generic shared carriage, 3D-printed locking, DIY, and actuator-reduction claims. Exact performance numbers require the paper, not promotional summaries. [ACM DOI](https://dl.acm.org/doi/10.1145/3746059.3747692), [project page](https://www.monash.edu/it/hcc/embodied-visualisation/projects/magnepins) |

The non-patent record is decisive for obviousness even where it creates no exclusionary right. It also shows why “low cost,” “3D printed,” “Arduino/ESP32,” “macro prototype,” “servo,” “cam,” or “calibration” cannot carry a patent case by themselves.

## 10. Current MVP patent assessment

### 10.1 Technical contribution actually embodied

The frozen MVP embodies a sensible student-engineering combination: six inexpensive actuators give independent dots without high-voltage piezo electronics; cams translate rotary motion into pin motion; enlarged FDM parts improve buildability; the ESP32 provides simple direct PWM; active retraction avoids relying on an unverified spring; and an external rail isolates actuator power from USB logic.

Those are useful project decisions. They are not yet a demonstrated invention. The project documents themselves identify unresolved return behavior, servo current, print clearance/friction, tactile validation, macro-to-standard transfer, and patent support. The architecture report's proposed calibration and self-test are not physical verification until a sensor or observable is added.

### 10.2 Patent assessment

- **Novelty:** an artificially narrow claim reciting the exact board, SG90 model, scale, and six-channel layout might avoid one-reference anticipation, but would have little useful scope and remain exposed to obviousness.
- **Inventive step:** a skilled person can combine the rotary-disk/cam disclosures, independently actuated pins, public micro-servo/cam modules, printed guides, mechanical stops, and ordinary PWM with predictable results. The current record contains no unexpected result.
- **Eligibility:** a physical electromechanical cell is ordinarily the right kind of subject matter; this is not the main weakness.
- **FTO:** the servo architecture is less aligned with active electromagnetic claim sets, but no clearance is possible, particularly in India, without `5559/CHE/2014` and live-claim verification.
- **Scale:** macro size makes assembly easier but does not prove standard Braille pitch, force, thickness, acoustic behavior, durability, or array density.

**Conclusion:** preserve the frozen MVP as the semester prototype. Do not describe it as patented, patent pending, patentable, novel, infringement-free, or the project invention on the current evidence.

## 11. Candidate invention-direction matrix

Risk labels assess the proposed direction, not the project as a whole. “High novelty risk” means a substantial chance that one earlier item discloses the meaningful combination; “high obviousness risk” means the difference appears predictable when references are combined.

### 11.1 Technical and patent screen

| ID / direction | Exact problem and prospective contribution | Closest verified art; overlap | Apparent difference / contribution type | Physical effect and baseline | Patent risks: novelty / obviousness / eligibility / FTO | Scale; current track; confidence; disposition |
|---|---|---|---|---|---|---|
| **D1 — mechanically normalized pin height** | Servo-angle, cam, print, and assembly variation produce unequal protrusion. Add a shared datum and dot-specific upper/lower seats that define physical output independently of nominal angle | `US12080182` specification; `US7410359`; `US8690576`; `WO2020106855`. All disclose stops, collars, plates, alignment, or tolerance isolation | Exact low-cost FDM/SG90 geometry may differ; **structural**, but otherwise an ordinary stop/fixture optimization | ≥50% reduction in between-dot/rebuild height SD versus the frozen fixed-geometry cell, without more jams | High / high / low / medium if claimed capture interfaces copied | Class 2 with class-3 practical result; **Track D**; 0.90 confidence that it is weak alone; **reject alone** |
| **D2 — per-dot servo calibration** | Commodity servo deadband, backlash, friction, and assembly offsets make one PWM pair unreliable. Discover and store dot-specific raise/retract envelopes | Aryan 2021 cam calibration; ordinary servo endpoints; `US7410359` calibration fixtures; `US12080182` tolerance control | Automated margins and replacement recalibration may differ; **control-based**, but normally calibration/optimization | ≥75% fewer incomplete transitions than one fixed up/down command across swaps, voltage, and wear | Medium-high / high / low-medium / low-to-unresolved | Class 1 logic, class 2 parameters, class 3 tactile result; **Track D**; 0.85; **retain only as engineering feature or part of D11** |
| **D3 — common-rail current-signature state inference** | A PWM command does not prove that a pin moved. Sequentially sample a shared shunt signal during a low-energy seat/retract pulse and classify completion or jam without six encoders | Generic motor-current/position correlation in `US9706716B2`; motor-anomaly inference in `US10879831B1`; actuator/plunger monitoring in `US20170030739A1`; tactile movement detection in `US12080182` | Applying one shared sensor to isolated cheap analog servo/cam/pin channels with dot-specific profiles; **sensing/control** | On blinded data, ≥97.5% sensitivity and specificity for induced raise/retract faults, then zero undetected wrong states in 3,000 held-out transitions | Medium-high / high / low-medium / unresolved until targeted claim search | Class 2; practical claim needs class-3 confirmation; **Track D now; reopen as B only on data/search**; 0.55; **experimental hypothesis** |
| **D4 — compliant printed guide/return** | Lateral cam error and FDM misalignment cause friction; a flexure centers the pin and supplies controlled return | `WO2015189863` compliant cantilevers; `EP4049116` printed cantilevers; 2016 public printed follower/lever; `US6902403` guide geometry | A particular monolithic geometry/material may differ; **structural/manufacturing** | Lower breakaway force and jam rate without fatigue or reduced tactile support | High / high / low / medium depending on geometry | Class 2 and class 3; **Track D**; 0.90; **reject as primary direction** |
| **D5 — scale-transfer design/calibration method** | Macro clearances and forces do not predict standard-pitch behavior. Use dimensionless ratios, coupons, and a transfer protocol linking pitch, guide clearance, cam eccentricity, force, and print process | `US8690576` assembly guide; `US12080182` tolerance isolation; MOLBED scale-up; ordinary design-of-experiments methods | A validated predictive relationship may differ; **manufacturing/experimental method**, not merely “shrink CAD” | Pre-registered model predicts unseen-scale jam rate/height/force within defined error | Medium / high / medium for method claims / low-to-unresolved | Class 1 model plus classes 2–3 effects; **Track D now; potential publication path**; 0.70; **not a patent direction without surprising validated law** |
| **D6 — modular auto-recalibrating cartridge** | Replacing one actuator/cam changes offsets. Use a keyed cartridge with identity data and automatic recalibration/verification after insertion | `US11915607`; `WO2013130534`; `US8690576`; `US12548467`; MOLBED | Automatic physical characterization after replacement may differ; **structural + control**, while generic cartridge/keying is known | Restore height/fault performance after blind cartridge swap without manual trim | High / high / low-medium / medium-high if capture assembly copied | Classes 1–2; class-3 density validation; **Track D**; 0.82; **reject generic modularity; fold only the recalibration event into D11** |
| **D7 — current-budgeted sequencing and brownout recovery** | Six servos may exceed the unverified 5 V supply/current margin. Schedule isolated or grouped moves from measured current and recover safely | Ordinary staggered servo control; low-power/latching tactile art; generic load management | Use measured dot-specific budgets and verified-state dependency; **control optimization** | ≥30% peak reduction, zero ESP32 resets, and bounded refresh latency versus simultaneous actuation | Medium / very high / medium / low-to-unresolved | Class 1 logic, class 2 power effect; **Track D**; 0.92; **retain as engineering safety, not invention** |
| **D8 — dedicated closed-loop travel sensing** | Open-loop servo commands cannot verify pin displacement. Add optical, Hall, capacitive, or mechanical sensing per dot | `US12080182` movement/capacitive sensing and broad closed-loop actuator art | Low-cost sensor layout may differ; **sensing hardware/control** | Directly measure both end states across wear and finger load | High / high / low / medium if layered capacitive/membrane structure adopted | Class 2; class-3 practical validation; **Track D**; 0.90; **reject as patent lead; use as experimental ground truth** |
| **D9 — shared actuation / actuator reduction** | Six servos dominate size and cost. Use a moving setter, nested camshaft, selective transmission, or shared energy source | `US8483018`; `US6692255`; `US11854423`; Aryan 2021 nested cams; MagnePins; `EP4049116` | Only a genuinely different selector/transmission could distinguish; **major structural redesign** | Substantially fewer actuators with equal state reliability, acceptable latency, and no excessive thickness | High / high / low / high in several active families | Classes 2–3; **Track D**; 0.95; **reject for current project; crowded major redesign** |
| **D10 — debris-tolerant replaceable guide liner** | Printed bores bind as debris/wear accumulates. Add sacrificial asymmetric liner/clearance or cleanable insert | `US6902403`; removable capture/cleaning disclosures in `WO2020106855`/`US12080182`; public printed modules | Exact printable liner geometry may differ; **structural/manufacturing** | ≥10× contamination dose before jam and restored performance after tool-less cleaning | High / high / low / medium | Classes 2–3; **Track D**; 0.88; **reject unless a distinct geometry shows an unexpected result** |
| **D11 — integrated datum + calibration + isolated current verification + bounded retry** | Cheap channels vary and fail silently. Couple D1–D3 and D7 so a mechanical datum defines output, dot-specific commands minimize stall, isolated sensing tests contact, and firmware retries or reports an unknown state | Combined teachings of `US8483018`, `US20130017516`, `US12080182`, `US7410359`, Aryan 2021, and generic motor-current diagnostics | No located independent claim was verified to contain the entire specific combination; **structural + sensing + control**. Difference is credible only if the elements interact, not merely coexist | At least 10× lower undetected wrong-state rate than calibrated open loop, while reducing height variation and peak current with bounded latency | Medium / high / low-medium / unresolved | Mostly class 2; class-3 practical confirmation; **Track D now; only candidate to reopen as B**; 0.48 patent-path confidence; **least-weak hypothesis** |
| **D12 — adaptive finger-load/holding control** | Finger pressure can back-drive or stall a raised dot. Detect load and adjust hold/retry without overheating | Tactile force/holding disclosures in `US6881063`, magnetic/friction latches, ordinary servo torque control | Cheap sensorless load discrimination on analog servos; **control optimization** | Maintain height under a pre-set load while limiting current and temperature | Medium-high / high / low-medium / unresolved | Classes 2–3; **Track D**; 0.78; **reject: safety, power, and obviousness concerns** |

Generic low cost, use of FDM, ESP32 character mapping, a lookup table, macro scaling, ordinary servo staggering, passive return, “modularity,” and “self-test” without a physical observable are expressly rejected as invention directions.

### 11.2 Execution screen

| ID | Experiment | Hardware / fabrication | Likely incremental cost | Three-month feasibility | Later work | Kill condition |
|---|---|---|---:|---|---|---|
| D1 | Compare frozen guide against three datum/stop variants over three rebuilds and 100 cycles/dot | Printed coupons, pins, reused servos, borrowed dial indicator or caliper/vision jig | ₹150–₹450 | High | Standard-pitch guide coupon and wear study | <50% reduction in height SD; new jam rate >1%; effect disappears after rebuild |
| D2 | Calibrate six installed plus at least two substitute servos over voltage and induced-friction conditions | Existing servos, two spares/borrowed units, logger | ₹180–₹500 | High | Long-term drift and replacement study | <75% reduction in incomplete moves, sustained stall, or manual tuning still required |
| D3 | Sample amplified shunt current with synchronized independent optical/height ground truth; blinded normal/fault events | 0.05–0.1 Ω shunt, fast current-sense amplifier such as INA180-class device, ESP32 ADC, simple optical fixture | ₹180–₹550 | Medium | Standard-pitch signal study; professional control-art search | Sensitivity or specificity <97.5%; signatures depend on incidental servo unit; false acceptance remains; no stable feature before tactile state changes |
| D4 | Force/clearance/fatigue comparison across PETG/ABS/nylon-compatible flexure coupons | Printed flexures, small weights/scale, reused mechanism | ₹200–₹700 | Medium | Material fatigue and standard-pitch fabrication | Fatigue/binding before 1,000 cycles, excessive force, or no advantage over plain guide |
| D5 | Fit a dimensionless model at macro and intermediate coupon scales; predict a held-out geometry | Two/three scale coupons, caliper, force fixture | ₹300–₹900 | Medium for coupons, low for standard cell | Precision/SLA or machined standard-scale cell, 3–9 months | Model misses held-out height/force/jam threshold; only empirical retuning works |
| D6 | Blindly swap keyed cartridge and run automatic characterization | Printed keyed cartridge, connectors, small ID component if used | ₹250–₹750 | Medium | Standard-density interface and cycle life | Manual trim needed, wrong insertion possible, or copied capture geometry required |
| D7 | Compare simultaneous, fixed sequential, and measured-budget scheduling across 1,000 worst-case patterns | Current logger, 5 V load/supply monitoring, ESP32 reset log | ₹100–₹400 beyond D3 | High | Larger array power model | <30% peak reduction, any reset, >1 s full update without project approval, or no advantage over fixed staggering |
| D8 | Use optical/Hall sensing as ground truth, then assess product cost/space | IR/optical or Hall reference sensors and fixture | ₹200–₹650 | High as test equipment | Miniaturized sensor integration | Sensor burden exceeds budget/space or merely duplicates known architecture |
| D9 | Paper architecture and one selector coupon only | New transmission/carriage prints and possibly motors | ₹500–₹2,000 for coupon | Low for credible patent evidence | 6–12 months; ₹5,000–₹20,000; precision fabrication | It abandons the frozen MVP, fails actuator-count/latency target, or maps closely to shared-actuation claims |
| D10 | Metered dust/fiber contamination and clean/recovery study | Replaceable liners, standardized inert test debris, force/height jig | ₹150–₹500 | Medium | Standard-pitch hygiene testing | No ≥10× contamination tolerance or cleaning damages tactile performance |
| D11 | Factorial comparison: frozen open loop; datum only; calibration only; current verification only; full integration | Combines D1–D3/D7; experimental optical ground truth; automated logs | ₹450–₹1,100 incremental, with reuse | Medium, if frozen cell works by week 3 | Standard-pitch single-dot/cell, broader prior-art search, patent counsel | No statistically and practically superior interaction; result equals sum of components; current signal cannot verify state; Indian/control search finds a close claim |
| D12 | Apply controlled pin load, log height/current/temperature, and test recovery | Force fixture, temperature sensor, current setup | ₹150–₹500 | Medium | Human-contact safety and standard-scale validation | Excessive heat/current, unreliable load inference, or no advantage over fixed safe torque limit |

## 12. Strongest surviving direction

The strongest direction is **D11: mechanically referenced, individually calibrated, sensor-minimal tactile-state verification with bounded recovery**. “Strongest” means least weak and most useful to test; it does not change the Track D verdict.

### 12.1 Precise technical definition

Without drafting legal claims, the prospective system would have all of the following engineering relationships:

1. Each tactile pin is driven by its existing SG90-class servo, eccentric cam, follower, and active raise/retract path.
2. A common mechanical datum defines permitted raised protrusion, and a lower datum or cam relationship defines complete retraction, so output height is not determined solely by nominal servo angle.
3. Commissioning finds, for each channel, the minimum reliable raise and retract command regions plus a margin that avoids continuous hard stall.
4. Only one diagnostic channel moves or seats at a time while a shared, sufficiently fast current-sense circuit records a time-domain response.
5. A dot-specific response model is correlated during development with independent physical ground truth; it may classify “completed,” “jammed/incomplete,” or “unknown,” but must never equate a commanded angle with physical state.
6. The controller permits at most a bounded, low-energy retry, isolates a failed channel, preserves healthy-dot operation, and reports an unknown cell state rather than silently acknowledging success.
7. Update scheduling respects the measured supply budget and keeps diagnostic signatures from being obscured by simultaneous servos.
8. Calibration and verification are repeated after a cartridge/servo replacement or a statistically significant signature drift.

The proposed interaction is physical: the datum creates a repeatable contact event; per-dot calibration reaches that event with minimum overdrive; isolated current sampling attempts to detect it without six product sensors; retry/fault logic turns the measurement into a safer tactile update. Merely placing a stop, a PWM table, a current sensor, and a delay in the same device is not enough.

### 12.2 Why it remains unestablished

An SG90 contains its own potentiometer and control electronics, but direct PWM exposes no position feedback. Rail current can change because of internal control behavior, supply impedance, gear friction, temperature, mechanical contact, finger load, or unit-to-unit electronics. A current pulse may therefore identify “servo experienced load” without identifying “tactile pin is correctly raised.” The proposal survives only as an experiment because the common datum may create a sufficiently distinctive, repeatable terminal-contact signature when channels are isolated.

No located independent claim was verified to recite this whole relationship. That is not proof of novelty. Generic patents already correlate motor current with position or faults: [US9706716B2](https://patents.google.com/patent/US9706716B2/en), [US10879831B1](https://patents.google.com/patent/US10879831B1/en), and [US20170030739A1](https://patents.google.com/patent/US20170030739A1/en). Braille records already teach stops, movement sensing, calibration, and sequencing. Obviousness is therefore high unless the controlled experiment shows a large, non-predictable improvement over each partial configuration.

### 12.3 Evidence threshold for reopening Track B

D11 may be reconsidered as Track B only if all of the following occur before any public disclosure:

- the official `5559/CHE/2014` file and descendants are reviewed;
- a targeted claims/CPC/current-signature search finds no anticipatory or materially closer combination;
- the held-out state-classification and 3,000-transition zero-undetected-error thresholds in section 18 pass;
- the full integration beats each single-feature and additive-control baseline, not just the raw frozen MVP;
- the effect survives servo swap, rebuild, voltage, friction, temperature, and finger-load perturbations;
- no continuous stall, unsafe temperature, repeated impact, or unacceptable update delay is introduced; and
- a standard-scale single-dot embodiment confirms that the signal/mechanical relationship is not a macro-only artifact.

## 13. Macro-scale and standard-scale transfer assessment

Scale classes are: **1 — scale-independent; 2 — scale-sensitive; 3 — standard-scale validation mandatory.** A prospective element may have more than one class at different levels.

| Prospective element | Class | Value of macro evidence | Transfer risk / additional evidence required |
|---|---:|---|---|
| Character-to-dot logic and fault-state machine | 1 | Fully exercises logical correctness | Does not establish mechanical state, patentability, or user readability |
| Per-channel calibration procedure | 1 for logic; 2 for values | Can show automatic search, storage, and retry logic | Endpoint ranges, deadband, current, and force change with actuator and scale; repeat on practical hardware |
| Current-budgeted sequencing | 1 for scheduling rule; 2 for effect | Can prove no resets and lower peak current on the frozen cell | Power density, actuator type, rail impedance, and array concurrency change at standard scale |
| Shared-current state classifier | 2; class-3 practical confirmation | Can test whether a terminal-contact signature exists and generalizes across SG90 units | Signal-to-noise, gear train, cam radius, pin mass, guide friction, and contact force all change; standard-scale single-dot proof is mandatory before useful broad claims |
| Mechanical upper/lower datum | 2; class 3 for usable Braille | Macro test can establish tolerance isolation and rebuild repeatability | FDM resolution becomes a larger fraction of pitch; thin plate stiffness, collar size, debris, and user force differ. Detailed drawings and tolerance stack are required |
| Cam/follower geometry and active retraction | 2; class 3 | Macro cycles reveal gross binding, wear, and active return | Contact stress, back-drive, friction, noise, and achievable thickness do not scale linearly; practical actuator/cam prototype required |
| FDM guide/compliant return | 2 and 3 | Useful for material and fatigue screening at the chosen print process | Feature thickness, anisotropy, clearance, and fatigue may be impossible at standard pitch; SLA/moulding may change the invention and cost |
| Pin protrusion, force, spacing, profile, and tactile readability | 3 | Macro device can support semester demonstration only | Enlarged 7 mm pitch and 1.5 mm protrusion cannot prove standard Braille readability, cell density, or comfort; owner-approved blinded user protocol and standard geometry are required |
| Modular cartridge/self-alignment | 2 and 3 | Macro assembly can show keying and replacement workflow | Connector envelope and accumulated interface tolerance dominate at practical density |
| Scale-transfer model itself | 1 as mathematical formulation; 2–3 as technical effect | Macro/intermediate coupons can fit a candidate model | Must predict a held-out practical-scale result; a formula without verified physical effect is not enough |

The frozen macro cell remains valuable for engineering and for testing scale-independent logic. It provides little commercially useful patent scope if claims must be limited to a 7 mm-pitch educational demonstrator. A standard-scale full six-dot cell is not required to finish the semester MVP, but at least a practical-scale single-dot coupon is mandatory before D11 can become technically credible as a patent direction.

## 14. Novelty analysis

### 14.1 Frozen MVP

No single verified independent claim located in this run recites every procurement and dimensional detail of the frozen MVP. `US8483018B2` uses a patterned disk rather than six separate cams; `US20130017516A1` is a timepiece; the micro-servo papers use different transmissions; the open projects differ in motor/cam layout; electromagnetic patents require different actuation.

That formal distinction supports, at most, a narrow possibility of novelty. A claim limited to “six SG90 servos at approximately 300% scale controlled by an ESP32” would be easy to design around and would not capture the functional value of a Braille cell. The exact retail selection and enlargement do not rescue the useful functional combination.

### 14.2 D11

No verified independent claim was found that simultaneously requires a servo/cam tactile pin, a mechanical terminal datum, channel-specific calibration, one shared current measurement isolated by sequencing, physical-state classification, bounded retry/fault isolation, and supply-aware update control. Novelty is therefore **unresolved, not established**.

Three constraints prevent a positive novelty conclusion:

1. `5559/CHE/2014` claim text is unknown and its public description is close to the mechanism.
2. Generic actuator-current/state-monitoring claims are numerous, and the search was not exhaustive across control classifications.
3. The proposed element “current signature corresponds to verified tactile state” does not yet exist as an enabled OpenBraille result; a speculative relationship cannot carry a patent case.

If D11's current classifier fails and a dedicated optical/Hall sensor is substituted, the direction moves closer to ordinary closed-loop position sensing and becomes still weaker for novelty.

## 15. Inventive-step / obviousness analysis

Obviousness is the principal patentability barrier.

A plausible combination begins with `US8483018B2` or the 2016 public micro-motor/cam project for rotary-to-guided-pin motion. `US20130017516A1` and the micro-servo papers supply independent pin actuation and processor control. `US12080182B2`, `US7410359B1`, and the Freedom Scientific construction lineage supply stops, alignment, tolerance isolation, calibration, maintenance, and movement sensing. Generic motor-control patents supply current/position or anomaly inference. Routine embedded control supplies channel isolation, retries, and current-limited sequencing.

The motivations are explicit and ordinary: compensate cheap actuator variation; prevent jams; define dot height; avoid brownout; confirm completion; and simplify replacement. Each feature performs its expected function. On the present record, D11 looks like an aggregation of workshop responses to known problems.

Evidence that could change this assessment must show more than improvement over an intentionally weak fixed-PWM baseline. The full system must outperform:

- calibrated open loop without a datum;
- datum plus calibration without sensing;
- current classification without a mechanical contact reference;
- fixed one-at-a-time sequencing without measured budgeting; and
- the predicted additive benefit of the parts.

A reproducible ≥10× reduction in undetected wrong states, uniquely caused by the coupled datum/signature relationship across heterogeneous servos and rebuilds, could support a technical argument. It would not guarantee inventive step; it would justify a professional search and drafting assessment. No secondary evidence of unexpected commercial success, long-felt failure, copying, or industry praise exists.

## 16. Patent-eligibility analysis

Eligibility is separate from novelty and inventive step and is not the controlling weakness.

- **Physical apparatus:** a tactile cell with cams, pins, mechanical datums, sensing circuitry, and physical error recovery is ordinarily framed as a machine/apparatus rather than an abstract result.
- **Control method:** a method that samples an actual actuator signal and changes physical pin actuation can have a technical effect. Essential sensor, timing, state, and mechanical relationships should not be replaced by “an algorithm configured to optimize Braille.”
- **Weak software subject matter:** character lookup, generic PWM generation, a calibration table, scheduling policy, or reporting a fault without a specific physical mechanism may face both eligibility and inventive-step objections.
- **India:** computer-program-per-se and algorithm exclusions under section 3(k) require careful drafting around a demonstrable technical process. A bare firmware claim is particularly weak.
- **Europe:** only features contributing to a technical solution to a technical problem materially assist inventive step for a computer-implemented invention.
- **United States:** abstract calculations or data classification must be integrated into a practical physical application.

Current official guidance should be checked at filing: [USPTO subject-matter eligibility resources](https://www.uspto.gov/patents/laws/examination-policy/subject-matter-eligibility), [USPTO MPEP §2106](https://www.uspto.gov/web/offices/pac/mpep/s2106.html), [EPO Guidelines for Examination](https://www.epo.org/en/legal/guidelines-epc), and the [Indian Patent Office](https://ipindia.gov.in/). Eligibility risk for a properly enabled D11 apparatus is **low to medium**; eligibility risk for calibration/sequencing software alone is **medium to high**. These observations require jurisdiction-specific professional review.

## 17. FTO risk analysis

FTO concerns live claims in each country of manufacture, use, sale, offer for sale, or import. It is not answered by whether OpenBraille is itself patentable. Expired or abandoned records can remain devastating prior art while posing less current exclusionary risk; a DB status label is not a clearance.

| Proposed activity/design | Potentially relevant claim sets | Present assessment |
|---|---|---|
| Frozen one-servo/one-cam cell, active retraction | `5559/CHE/2014`; rotary disk/timepiece records; any unidentified servo/cam descendants | **India unresolved and potentially material.** Known US rotary/timepiece claims have limiting watch/disk features, but official status and territorial analysis are incomplete. No clearance |
| Hard stop or simple printed guide | `US7410359`, `US12080182`, `US12548467`, `US6902403`, Freedom modular lineage | A simple stop does not automatically satisfy piezo, membrane, capacitive, electromagnetic, or claimed cross-section limitations. Copying a layered capture assembly, collar, membrane, or contaminant geometry increases risk. Claim chart required in intended territory |
| Passive friction retention/shared hammer | `US11854423`/`US11521514` | Frozen baseline differs. A later impact setter with friction-held pins may move materially closer; high design-review priority |
| Electromagnetic/latching redesign | `US11410574`/`WO2016074170`, `WO2020106855`/`EP3884363`/`US12548467`, `EP4049116`, MagnePins publication | Several relatively recent grant publications occupy layered EM, removable capture, magnet latching, and resonant shared actuation. Country-by-country live-claim review mandatory |
| Modular self-aligning cartridge | `US11915607`, `WO2013130534` lineage, `US12548467`, `US12080182` | Generic modularity is not itself infringement, but specific cavities, top/bottom capture, membrane, collar, guide, and interface relationships may matter. Avoid cloning disclosed interfaces before review |
| D11 shared-current verification | Generic motor-current/position/anomaly families and any tactile-control descendants | Targeted claims search incomplete. Current sensing may be generic prior art and could also fall within live non-Braille control claims depending on claim scope and territory |

No infringement conclusion is made. Experimental student construction in India should not be assumed exempt without legal advice. Do not publish a statement that the design is “FTO,” “non-infringing,” or “safe because the closest patent expired.”

## 18. Claim-to-experiment map

Only D11 remains as a patent-oriented experiment. The tables below are joined by element ID and collectively contain every required field. D1, D2, D3, and D7 are controls/sub-elements, not separate surviving patent directions.

### 18.1 Technical design and variables

| ID / prospective technical element | Nearest verified prior art | Measurable technical effect | Baseline system | Proposed system | Independent variable | Controlled variables |
|---|---|---|---|---|---|---|
| **E1 — common terminal datum** | `US12080182` specification; `US7410359`; `US8690576` | Between-dot/rebuild protrusion SD and jam rate | Frozen cam/guide, height determined by stack and command angle | Interchangeable datum/stop variants defining 1.5 mm target | Stop geometry and presence | Same pins, cams, servos, material, orientation, print settings, voltage, cycle rate |
| **E2 — automatic per-dot command envelope** | Aryan 2021; ordinary servo calibration; Freedom calibration fixtures | Incomplete raise/retract rate, stall duration, calibration time after swap | One global up/down PWM pair | Minimum reliable channel-specific raise/retract regions plus safety margin | Calibration enabled/disabled and margin | Same mechanical variant, supply, load, temperature, character sequence |
| **E3 — isolated shared-current state classification** | `US12080182` movement detection; `US9706716`; `US10879831`; `US20170030739` | Sensitivity, specificity, false acceptance, signature drift | Command/timeout treated as success | Fast shunt trace classified as complete/fault/unknown, one channel at a time | Fault type, classifier, sensing enabled | Ground-truth fixture, sample rate, supply impedance, servo, temperature, command profile |
| **E4 — bounded retry and fault isolation** | General actuator fault control; tactile movement sensing | Undetected wrong-state rate, healthy-dot completion, reset count, energy/fault | Blind command acknowledgement | Max two low-energy retries, channel isolate, explicit unknown-state report | Retry policy and induced fault | Same fault severity, pattern, power rail, sensing threshold, actuator |
| **E5 — measured current-budget sequencing** | Ordinary staggered actuation; low-power tactile art | Peak rail current, energy/update, ESP32 resets, update latency | Simultaneous or fixed delay | Scheduler using measured per-channel current budget and diagnostic isolation | Scheduling strategy | Same patterns, servos, supply, capacitor, firmware clock, mechanical load |
| **E6 — coupled non-additive effect** | Combination of records above | Full-system error reduction beyond predicted/additive partial systems | Frozen, datum-only, calibration-only, sensing-only, datum+calibration | Full E1–E5 integration | Configuration in factorial/ablation comparison | Identical randomized sequence, rebuilds, servos, voltage, temperature, wear stage |
| **E7 — robustness across perturbations** | Known tolerance/contamination/current problems | Generalization across servo swap, rebuild, voltage, friction, temperature, and finger load | Best tuned baseline under nominal conditions | Full system without manual retune except automatic commissioning | Pre-registered perturbation | Pattern distribution, ground-truth method, success thresholds |
| **E8 — practical-scale transfer** | Capture/guide families and scale-transfer prior art | Preservation of terminal signature and reliable physical state at smaller geometry | 300% macro channel | One standard-pitch or closest feasible single-dot coupon using declared process | Scale/actuator/geometry | Same logical algorithm, normalized load ranges, measurement definitions |

### 18.2 Equipment, counts, thresholds, delivery, and confidentiality

| ID | Equipment | Sample / cycle count | Success evidence | Failure evidence | Scale relevance | Three-month deliverability | Later work required | Confidentiality sensitivity |
|---|---|---|---|---|---|---|---|---|
| E1 | Printed variants; caliper plus borrowed dial indicator or calibrated camera jig | 3 variants + frozen baseline; 3 rebuilds; 6 dots; 100 cycles/dot/condition | ≥50% lower height SD; ≥95% raises within 1.50 ± 0.15 mm; jam rate ≤1%; no sustained stall | Effect <50%, rebuild dependence, new jams, damaged pin/cam | Macro supports principle; standard-scale mandatory for useful scope | High | Practical-scale guide/collar tolerance and wear | **High** for new geometry/drawings and raw results |
| E2 | Automated PWM/current/height logger; 6 installed + ≥2 substitute servos | ≥300 raise/retract transitions per servo per nominal/low/high voltage condition | ≥75% fewer incomplete moves than global-PWM baseline; commissioning ≤5 min/channel; no continuous hard stall | Manual tuning, effect disappears on swap, increased wear/current | Logic class 1; values class 2; tactile result class 3 | High | Drift at 10k+ cycles and practical actuator | **High** for algorithm, thresholds, and data |
| E3 | 0.05–0.1 Ω shunt, fast current-sense amplifier, ESP32 ADC/logic capture, independent optical/height ground truth | Development set separated from blinded hold-out; ≥600 normal + 600 induced fault events across raise/retract, six channels, and perturbations | On untouched hold-out: sensitivity and specificity each ≥97.5%; pre-set confidence bounds; unknown output used for ambiguous events | Leakage between training/test, unit-specific classifier, <97.5%, or current predicts servo load but not pin state | Class 2; standard-scale confirmation mandatory | Medium | Wider servo population; practical scale; environmental validation | **Very high**; core possible contribution and raw signatures |
| E4 | Automated obstruction fixture; reset/current/state logs | ≥300 randomized fault episodes plus 3,000 held-out full transitions | Zero undetected wrong states in 3,000 held-out transitions; ≥99% healthy-dot completion; zero MCU resets; ≤2 retries | Any silent false success; retry damage/heat; cascading failure; excessive unknown rate | Control partly class 1; force and detection class 2/3 | Medium | Longer reliability and human-use safety | **Very high** |
| E5 | Current logger/oscilloscope access; 5 V rail and reset monitor | 1,000 worst-case randomized patterns per strategy | ≥30% lower peak than simultaneous baseline; zero resets; full update ≤1.0 s or owner-approved threshold; no error increase | Any reset, no advantage over fixed staggering, latency failure, increased state error | Scheduling rule class 1; power result class 2 | High | Multi-cell array concurrency | High for measured profiles; medium for generic scheduler |
| E6 | Same rig; pre-registered factorial/ablation analysis | Minimum 1,000 transitions/configuration after commissioning; three rebuilds | Full integration achieves ≥10× lower undetected error than calibrated open loop **and** materially exceeds the pre-stated additive expectation; effect size/CI reported | Full system merely equals best partial system; post-hoc metric changes; no reproducible interaction | Macro can show interaction; practical-scale confirmation mandatory | Medium if automation works by week 6 | Replication by second builder/site and practical cell | **Very high**; do not disclose before IPR review |
| E7 | Voltage control 4.75/5.0/5.25 V; controlled added friction; 20–35 °C observation where safely available; 0–1 N pin-load fixture | Pre-register balanced conditions; ≥200 transitions/channel/perturbation, with held-out servo/rebuild | Thresholds remain met without manual retuning; no unsafe temperature or damage | Failure under one ordinary perturbation, ad hoc retuning, classifier drift, unsafe load | Strong scale sensitivity | Medium | Broader environmental/lifetime study | Very high |
| E8 | Practical-scale single-dot coupon; precise dimensional/force measurement; suitable micro-actuator if SG90 geometry cannot fit | ≥3 coupons/rebuilds; ≥1,000 transitions each before patent-positive decision | Same causal datum/signature relationship; reliable height/retraction; no macro-only classifier feature | Cannot fabricate, actuator cannot fit, signal disappears, force/clearance fails | This is the mandatory class-3 gate | Low-to-medium; coupon only, not a full cell | Full standard six-dot cell, user study, 10k–100k cycles | **Very high** |

All thresholds must be frozen before the corresponding test. Raw traces, rejected runs, print files, firmware commits, environmental conditions, calibration versions, and negative results must be retained. A visually successful demo is not patent evidence.

## 19. Three-month semester plan

The semester plan protects the frozen MVP. D11 is a bounded overlay and may be stopped without preventing the one-cell demonstration.

### 19.1 Semester MVP

| Week | Frozen-MVP work and gate | Required record |
|---:|---|---|
| 1 | Freeze dimensions/BOM/firmware baseline. Inspect every SG90 physically. Determine whether any return torque is usable only in the actual coupled mechanism; otherwise retain active cam retraction. Pre-register mechanical and electrical thresholds | Signed baseline sheet; servo photos/part markings; raw return-force/angle observations; configuration tag |
| 2 | Build one single-dot mechanism before the full cell. Resolve cam/follower contact, guide clearance, active raise/retract, and safe angle limits | Dimensioned drawing, print settings, failure log, 100-cycle height trace |
| 3 | Build the frozen six-dot macro cell. Use the 5 V supply and bulk capacitor specified by project authority, but measure rail voltage/current before accepting adequacy | As-built BOM, wiring diagram, current/voltage traces, thermal observations |
| 4 | Implement minimal serial command, character-to-dot mapping, direct GPIO PWM, explicit channel timeout, and error logging. Do not label time elapsed as state verification | Versioned firmware, command tests, channel mapping, reset/error log |
| 5 | Run frozen baseline: 100-cycle repeatability per dot, all requested patterns, active retraction, force/height, and 1,000-actuation durability minimum | Immutable baseline dataset; pass/fail against ≤0.1 mm project repeatability criterion and actual jam/failure counts |
| 6 | Owner approves a blinded tactile-identification protocol and quantitative threshold before any participant testing. If institutional/consent requirements cannot be met, retain mechanical evidence and do not substitute teammates' visual judgments for user evidence | Approved protocol or documented deferral; consent/ethics route where applicable |
| 7–10 | Continue frozen-MVP reliability and integration while the bounded enhancement runs in parallel | Daily build/test log; adverse events and rejected runs retained |
| 11 | Repeat baseline after wear; reconcile BOM and failures; prepare demonstration using only verified capabilities | Final engineering acceptance table and limitation statement |
| 12 | Freeze semester artifact and evidence archive. Demonstrate one cell without patent claims or unverified status statements | Reproducible build package, test report, public-safe demonstration text |

The MVP succeeds as an engineering prototype only if it actively raises and retracts all six dots, does not rely on an unverified servo spring, meets the owner-approved mechanical/tactile criteria, survives the stated cycles, remains under ₹5,000, and reports rather than conceals failures.

### 19.2 Bounded enhancement

| Week | D11 activity | Decision gate |
|---:|---|---|
| 1 | Keep D11 confidential; request Indian file retrieval and targeted control-art search. Freeze hypotheses, metrics, configurations, and data split | Stop patent work if a verified claim reads directly on the meaningful combination or if institutional IPR review forbids disclosure/testing plan |
| 2–3 | Print D1 datum variants around the working single-dot baseline; measure actual protrusion and active retraction | Continue only if a datum variant reduces variance without new jams/stall |
| 4 | Add safe fast shunt/current amplifier and independent optical/height ground truth. Do not use an INA219-class slow monitor as the only waveform sensor without proving bandwidth | Continue only if synchronized traces are valid and sensing does not disturb 5 V operation |
| 5 | Implement automatic per-dot command-envelope discovery with hard angle/current/time limits | Continue only if automatic commissioning beats fixed commands across at least two substitute servos |
| 6 | Collect labeled normal/fault development data; lock signal processing and untouched hold-out set | No post-hoc leakage or threshold tuning on hold-out data |
| 7 | Run blinded E3 classification | Stop D11 if sensitivity or specificity is below 97.5% or if current predicts servo effort but not physical pin state |
| 8 | Add bounded retry, explicit unknown-state response, and measured current-budget scheduler | Stop if retry creates heat/damage or a failure can still be acknowledged as success |
| 9 | Run factorial/ablation comparison across frozen, partial, and full configurations | Stop patent direction if the full configuration has no non-additive effect |
| 10 | Run 3,000 held-out transitions and 1,000 worst-case power patterns | Stop if any silent state error, ESP32 reset, unsafe condition, or unacceptable latency occurs |
| 11 | Attempt three practical-scale single-dot coupons if fabrication/actuator choice is available without replacing the frozen MVP | Do not generalize beyond macro scale if the causal effect does not transfer |
| 12 | Independent internal review of data, negative results, search results, authorship/inventorship contributions, and confidentiality | Reopen Track B only if every section 12.3 gate passes; otherwise close patent track and retain publication/engineering results |

### 19.3 Tactile validation boundary

Human tactile testing supports engineering utility, not novelty by itself. Before testing, the owner/institution should approve participant eligibility, informed consent, randomization, number of patterns/trials, hygiene, stop rules, and a numerical acceptance threshold. Experienced Braille readers are the relevant evaluators; the five project members are not substitutes. Macro-scale recognition must be reported as macro-scale only.

## 20. Later-semester or publication extension

Because the primary track is D, no later patent mechanism is represented as credible today. There is nevertheless a coherent **research/publication extension** if D11 produces useful negative or positive data.

### 20.1 If D11 fails

Publishable work could be a reproducible study of why common-rail current fails to verify state in low-cost analog servo tactile mechanisms, including unit variability, contact ambiguity, supply effects, and recommended ground-truth methods. A well-designed negative result is technically useful and honest. Release only after institutional IPR review and after confirming that publication will not prejudice any retained filing option.

### 20.2 If D11 passes but patent search remains adverse

The team could publish a benchmark dataset and engineering method for comparing open-loop, calibrated, current-inferred, and directly sensed tactile pins. The contribution would be reproducibility and evidence, not an assertion of exclusive rights.

### 20.3 If every Track-B reopening gate passes

A later programme would require:

- **Additional mechanism:** a standard-pitch single dot, followed by a six-dot cell, preserving the datum/signature interaction with a practical micro-actuator and manufacturable guide.
- **Duration:** approximately 4–9 additional months after the semester.
- **Additional cost:** roughly ₹5,000–₹20,000 depending on actuator access, precision printing/machining, measurement fixtures, and replicate cells.
- **Fabrication:** high-resolution additive manufacture or mould/machining trials; tolerance-stack drawings; at least three independent builds; no unrecorded hand finishing.
- **Validation:** 10,000–100,000 cycles, contamination/temperature/load testing, multiple actuator lots, standard-geometry tactile testing, multi-cell power/timing, and replication by a second builder.
- **Patent work:** complete Indian file retrieval, professional novelty/obviousness search, live-claim FTO charts for intended territories, inventorship review, and institution-approved drafting before disclosure.
- **Publication opportunity:** low-cost tactile actuator state verification, scale-transfer evidence, negative-result dataset, or reproducible reliability protocol.
- **Continuity with OpenBraille:** the work keeps the same tactile-pin objective, error modes, calibration logic, and reliability question. It is not a switch to an unrelated actuation concept.

A shared carriage, resonant selector, electromagnetic capture stack, or other actuator-reduction mechanism would be a major redesign, not this extension. The crowded record gives no present reason to prioritize it for patent development.

## 21. Budget and team feasibility

### 21.1 Budget

| Cost block | Expected range | Control |
|---|---:|---|
| Frozen MVP, based on the approved architecture estimate | ₹2,060–₹2,850 | No silent actuator/board substitution; record actual invoice and donated/borrowed items |
| Datum/guide print variants and mechanical coupons | ₹150–₹350 | Reuse servos, pins, frame, and test fixtures; print single-dot coupons before full variants |
| Fast current-sense shunt/amplifier and passive parts | ₹120–₹300 | Verify bandwidth, common-mode range, power rating, and ADC safety before purchase |
| Two substitute/spare SG90-class servos | ₹180–₹300 | Needed to test unit variation; borrow only if provenance is recorded |
| Optical/Hall ground-truth fixture and temperature/load aids | ₹150–₹400 | Experimental equipment only; borrow caliper/dial indicator/oscilloscope where possible |
| Contingency | ₹250–₹500 | Released only against logged failure or replacement need |
| **Expected combined total** | **₹2,910–₹4,700** | Under the ₹5,000 ceiling; the ≤₹3,000 preference is achievable only near the low BOM range with borrowed metrology |

If forecast committed cost exceeds ₹5,000, D11 enhancement work stops before compromising the frozen MVP. A dedicated six-sensor product architecture or precision standard-scale full cell is outside this semester budget.

### 21.2 Five-member team

| Role | Scope | Independence / evidence control |
|---|---|---|
| Technical lead | Architecture freeze, integration, safety, weekly gates | Cannot change thresholds after seeing results without documenting the protocol deviation |
| Mechanical lead | Cam/follower/guide/datum CAD, print settings, metrology | Preserves failed prints and records all sanding/lubrication/manual fit operations |
| Firmware/data lead | PWM, calibration, synchronized ADC, scheduler, immutable logs, analysis | Keeps development and hold-out sets separate; versions algorithms and parameters |
| Test/build member (beginner-supported role) | SOP execution, randomized run order, component lookup, specimen labels | Receives checklists and supervision; independently records observed failures rather than repairing silently |
| Documentation/IPR/presentation lead | Source ledger, notebook custody, confidentiality, participant protocol, public-safe demo | Separates public baseline from confidential D11; tracks contributors for inventorship review |

Three technical members can build and instrument the cell; the beginner and presenter/support roles are useful only with bounded tasks and clear checklists. The plan is feasible within three months if automated logging works by week 6. It is not feasible if the team attempts a full standard-scale six-dot redesign, professional FTO search, and exhaustive human study within the same budget.

## 22. Kill criteria

### 22.1 Immediate patent-path kill criteria

D11 remains Track D, and patent-oriented work should cease or remain closed if any one of the following occurs:

1. An official `5559/CHE/2014` claim or another verified earlier claim discloses the meaningful D11 combination, or a live territorial claim creates an unacceptable design constraint.
2. A targeted professional/Deep Research search finds a closer claim combining tactile terminal contact, per-channel characterization, current-derived position/state, and recovery/sequencing.
3. Shared current cannot distinguish actual tactile state from internal servo effort at ≥97.5% sensitivity and specificity on untouched data.
4. Any commanded-but-wrong physical state is silently accepted in the 3,000-transition held-out test.
5. The full system does not materially outperform datum-only, calibration-only, sensing-only, and predicted additive controls; no non-additive interaction is shown.
6. The effect depends on a particular hand-selected servo, build, threshold, lubricant, or post-hoc retuning.
7. The mechanism requires continuous hard stall, unsafe temperature, damaging repeated impacts, or >₹5,000 total committed cost.
8. A practical-scale single-dot coupon cannot preserve the causal relationship, or standard-scale fabrication requires a fundamentally different mechanism.
9. The only defensible distinction becomes SG90 brand, ESP32 choice, 300% scale, low price, ordinary calibration, 3D printing, or generic modularity.
10. Uncontrolled public disclosure occurs before institutional review and destroys the intended filing strategy in material jurisdictions.

### 22.2 Semester engineering kill / redesign triggers

The frozen MVP must be repaired or re-scoped—not presented as successful—if active retraction sticks, 5 V operation browns out, pin variance exceeds the owner criterion, the cell fails before 1,000 actuations, tactile output does not meet the pre-approved threshold, or cost exceeds ₹5,000. A project engineering failure is not to be hidden by switching the patent story.

### 22.3 Positive gate

No patent-positive classification follows automatically from passing experiments. Passing only authorizes: (a) official/professional search completion; (b) institutional IPR review; and (c) reconsideration from Track D to Track B. Patentability and FTO remain legal questions.

## 23. Confidentiality boundary

### 23.1 Already public or conventional subject matter

The external record already publicly discloses servo/motor-actuated Braille pins, rotating disks/cams, followers/levers, guided pins, FDM/printed modules, ESP32/Arduino-class control, PWM, modular cells, latches, calibration, stops, shared actuation, and low-cost goals. Those general ideas cannot be made confidential again. The project documents also freeze the MVP internally; this report does not assume that the project's exact CAD, firmware, or dimensions have already been publicly disclosed unless a dated disclosure record proves it.

### 23.2 Potentially confidential new material

- **Geometry:** exact datum/seat/cam relationships, low-energy terminal-contact geometry, keyed replacement interfaces, tolerances, and practical-scale embodiments.
- **Control:** per-dot commissioning procedure, waveform features, confidence/unknown logic, retry limits, drift/replacement rules, and measured-budget scheduler when tied to the physical mechanism.
- **Results:** raw current/height/force traces, ablation outcomes, failed configurations, thresholds, classifier performance, perturbation data, scale-transfer models, and unexpected effects.
- **Development record:** dated conception notes, contributor roles, CAD/firmware version history, and inventorship evidence.

### 23.3 Handling rules

Until institutional IPR review decides otherwise:

- keep D11 CAD, firmware, notebooks, and datasets in access-controlled project storage;
- label exports and presentations “confidential project material” and list recipients;
- do not upload D11 details to public Git repositories, Hackaday, video platforms, competition pages, preprints, posters, or model prompts outside approved systems;
- show only the public/conventional frozen baseline in open demonstrations, with no unfiled geometry, waveform, threshold, or result detail;
- record every prior disclosure date and content; do not assume an NDA cures an earlier public disclosure;
- obtain institution advice on ownership, student/institution obligations, inventorship, human testing, and filing sequence; and
- do not say “patent pending” unless a real application covering the stated subject matter has been filed.

## 24. Final project recommendation

**Retain as strong semester prototype but reduce patent priority.**

The frozen cell is coherent, affordable, demonstrable, and well suited to retiring mechanical, power, tactile, and fabrication uncertainties. Its current patent evidence is weak. D11 should be run as a bounded, confidential falsification experiment only if it does not delay the baseline and if the official Indian/control searches are pursued. The project should not be advanced as patent-first on a promise that routine calibration, sequencing, or FDM tolerance work will later become inventive.

No comparison with other Project mC concepts is made, no winner is selected, and no final scoring worksheet is filled.

## 25. Unresolved questions

| Priority | Unresolved question | Evidence needed / owner |
|---:|---|---|
| 1 | What exactly was filed, published, prosecuted, divided, granted, abandoned, or renewed for `5559/CHE/2014`? | Complete Indian Patent Office file and status certificate/event history; Indian patent professional or separate Deep Research synthesis |
| 2 | Does `5559/CHE/2014` have a renumbered publication, patent, divisional, PCT, or foreign descendant? | Applicant/inventor/date/subject family search in official databases |
| 3 | What are the live claims and territorial statuses of the recent US/EP capture, electromagnetic, modular, and friction-pin records? | USPTO Patent Center/maintenance data; EPO Register and national validations; official CA/JP/KR/CN records |
| 4 | Do any claims specifically cover current-signature inference of tactile-pin or cam terminal state, shared sensing by sequential isolation, or retry based on that state? | Focused claim/CPC/citation search across tactile display and generic motor-control classes |
| 5 | What do the independent claims and legal events of `US5685721`, `US5453012`, and `US5766014` actually say? | Official images/OCR and file histories; until retrieved, not load-bearing |
| 6 | Do the six actual SG90-class units exhibit usable return torque when coupled to the selected cam, or must all retraction be active? | Physical inspection and force/angle/cycle data; mechanical lead |
| 7 | Can the specified external 5 V supply support real worst-case patterns without droop, reset, or unsafe connector/wire heating? | Oscilloscope/current log across all patterns and stalls; technical lead |
| 8 | Is the current signature causally tied to correct pin state or merely correlated with servo effort on one build? | Blinded ground-truthed E3/E7 experiments; firmware/data lead |
| 9 | What clearance, finish, material, lubricant, and cam profile meet ≤0.1 mm repeatability and ≥1,000 cycles without undocumented hand fitting? | Three-build dimensional and durability record; mechanical/test leads |
| 10 | What owner-approved tactile identification rate, participants, pattern count, hygiene, and consent process define success? | Pre-registered protocol and institutional approval where required |
| 11 | Can a standard-pitch single dot reproduce the datum/signature relationship and necessary force without changing actuator principle? | E8 coupons, drawings, tolerance/force analysis |
| 12 | What jurisdictions and commercial acts matter for eventual manufacture, demonstration, distribution, and sale? | Written commercialization scope; needed before FTO search |
| 13 | What project material has already been publicly disclosed, when, by whom, and with what enabling detail? | Dated disclosure audit of repositories, presentations, submissions, videos, and messages |
| 14 | Who conceived each D11 element and who reduced it to practice? | Contemporaneous signed/dated contribution records; institution IPR review |
| 15 | Does D11 show an effect beyond the predictable sum of stops, calibration, current sensing, and sequencing? | Pre-registered ablation/factorial result with confidence intervals and negative runs |

Every patent/status item above remains explicitly assigned to the separate Deep Research synthesis or professional verification where primary access was unavailable. None is guessed here.

## 26. Source and verification log

### 26.1 Attached project and report sources

| Source group | Use in this synthesis | Verification boundary |
|---|---|---|
| `01_Engineering_Design_Review` | Mission, hypothesis, minimum demonstrable success, fixed design principles | Project authority, not patent evidence |
| `02_Project_mC_Decision_Register_v1.2` | Current budget, team, frozen servo/cam architecture, macro scale, active-return correction, owner decisions | Controls project facts; its source-verification labels do not replace current patent verification |
| `03`–`06` Phase 3C closure/architecture/memory/SOP | Current architecture, BOM estimate, build sequence, acceptance intentions | Architecture report's passive-return and sensorless “verify travel” propositions were challenged rather than adopted |
| `07_Concept_Evidence_Matrix`, `08_Uncertainty_and_Test_Register`, `09_Patent_Research_Input_Pack` | Validated uncertainties, tests, patent-research framing, conventional-feature warning | Evidence of project state, not proof of patentability |
| `10_Phase2_Report_by_Claude` | Historical identifiers and search leads | No historical conclusion treated as current verified fact |
| Reports `11`–`16` | Search leads, claim/status assertions, candidate directions, experiments | Audited individually in section 3; no report treated as authority; Perplexity excluded after its §8.2 cutoff |
| `99_INPUT_MANIFEST` | Count, expected names, hashes, model-lane labels | File control only; never technical evidence |

### 26.2 Official portals and current-status attempts

All web records below were checked for this synthesis on **31 July 2026**.

| Source | Purpose / result | Limitation |
|---|---|---|
| [Indian Patent Office public search](https://iprsearch.ipindia.gov.in/PublicSearch/) | Exact application number/name/subject search for `5559/CHE/2014` | No usable official application file was retrieved; no inference from absence |
| [WIPO PATENTSCOPE](https://patentscope.wipo.int/search/en/search.jsf) | PCT publication/family/status checking | Publication leads were navigated, but no official live-national-right conclusion was extracted |
| [USPTO Patent Center](https://patentcenter.uspto.gov/) and [Patent Public Search](https://ppubs.uspto.gov/pubwebapp/) | US application, prosecution, and current-status route | Complete official maintenance/prosecution extraction was not available for every record; DB status labels remain non-authoritative |
| [European Patent Register](https://register.epo.org/) | EP grant/prosecution/validation route | EP B1 publications were identified; national validation/lapse was not exhaustively verified |

### 26.3 Patent publication and claim records

Google Patents was used as a readable publication-text and family-navigation source. Its own legal-status disclaimer means the “active,” “expired,” or “ceased” field was logged only as a DB signal.

| Publication record | What was verified from the publication | Unresolved |
|---|---|---|
| [US8483018B2](https://patents.google.com/patent/US8483018B2/en) | Claim 1 disk/raised surface/guided pins/rotary actuator; servo/PWM embodiment; family identifiers | Official maintenance/lapse status |
| [US20130017516A1](https://patents.google.com/patent/US20130017516A1/en) | Independent translational pins/timepiece; cam/lever/direct-drive specification | Official abandonment/event history |
| [US11854423B1](https://patents.google.com/patent/US11854423B1/en), [US11521514B2](https://patents.google.com/patent/US11521514B2/en) | Friction-retained pins and motorized impact-driver claims; relationship | Current live claim/status and any non-US rights |
| [US11410574B2](https://patents.google.com/patent/US11410574B2/en), [WO2016074170A1](https://patents.google.com/patent/WO2016074170A1/en) | Layered electromagnetic independent-claim subject and family | Official national status/claim amendments |
| [WO2020106855A1](https://patents.google.com/patent/WO2020106855A1/en), [EP3884363B1](https://patents.google.com/patent/EP3884363B1/en), [US12548467B2](https://patents.google.com/patent/US12548467B2/en) | Original disclosure; EP/US grant publications; US removable capture/collar/membrane/electromagnetic claim; family members | EP national validations and official US/CA/JP/KR/CN current status |
| [US11915607B2](https://patents.google.com/patent/US11915607B2/en) | Mobile-device case/cavities/pins/controller independent claim; dependent actuator limitations | Official current status and territorial family |
| [US12080182B2](https://patents.google.com/patent/US12080182B2/en), [US11645948B2](https://patents.google.com/patent/US11645948B2/en) | Capture/membrane/capacitive claim; specification's stop, alignment, sensing, cleaning, and tolerance disclosures | Official current status; which disclosed embodiments remain within live claims after prosecution |
| [WO2013130534A1](https://patents.google.com/patent/WO2013130534A1/en), [US8690576B2](https://patents.google.com/patent/US8690576B2/en), [US9424759B2](https://patents.google.com/patent/US9424759B2/en) | Modular blocks, limits, assembly/alignment teachings; distinct focus of later continuation | Official expiry and foreign national status |
| [WO2015189863A2](https://patents.google.com/patent/WO2015189863A2/en) | SMA/cantilever/latching/layered independent claims; Indian priority | Indian/national phase and current legal effect |
| [EP4049116B1](https://patents.google.com/patent/EP4049116B1/en) | One-solenoid/different-frequency/resonant-taxel independent claim; printed-frame disclosure | National validations and any non-EP live claims |
| [US6881063B2](https://patents.google.com/patent/US6881063B2/en) | EAP/hydraulic/latching claim and performance context | Official expiry |
| [US6354839B1](https://patents.google.com/patent/US6354839B1/en), [US6743021B2](https://patents.google.com/patent/US6743021B2/en) | Orbital Research MEMS/EAP lineage; continuation-in-part relationship; continuous-surface claims | Official expiry/status; no micro-motor/D'Souza relationship |
| [US7410359B1](https://patents.google.com/patent/US7410359B1/en) | Piezo-reed/support claims; stop, cap, alignment, calibration, removal disclosure | Official adjusted term and live claims at cut-off |
| [US6902403B1](https://patents.google.com/patent/US6902403B1/en) | Contaminant-tolerant pin/guide cross-section claims | Official expiry/status |
| [US6692255B2](https://patents.google.com/patent/US6692255B2/en) | Relative bidirectional shared actuation and retained-pin claim | Official expiry/status |
| [US9706716B2](https://patents.google.com/patent/US9706716B2/en), [US10879831B1](https://patents.google.com/patent/US10879831B1/en), [US20170030739A1](https://patents.google.com/patent/US20170030739A1/en) | Generic motor current/position, current/anomaly, and actuator/plunger monitoring teachings | Not an exhaustive control-art search; tactile applicability and live territorial claims require analysis |
| `US5685721`, `US5453012`, `US5766014` | Existence/technical leads appeared in reports and citing records | Direct verified claims/status not retrieved; excluded from load-bearing claim conclusions |

### 26.4 Non-patent and public-project records

| Source | Verified use | Limit |
|---|---|---|
| [Aryan et al. 2021 DOI](https://doi.org/10.1088/1757-899X/1123/1/012028) | Peer-reviewed title/record and servo/nested-cam/calibration disclosure | Full experimental replication and all numerical results not independently repeated |
| [Rahman et al. 2018 IEEE](https://ieeexplore.ieee.org/document/8641028/) | Peer-reviewed micro-servo Braille publication record | Full claim-like feature mapping depends on complete paper access |
| [Brindle 2023 IEEE](https://ieeexplore.ieee.org/document/10456453/) | Later low-cost single-cell micro-servo/slider publication record | Promotional cost/speed figures not used as load-bearing findings |
| [Refreshable Braille Display public logs](https://hackaday.io/project/10849-refreshable-braille-display/logs?sort=oldest) | Dated micro-motor/cam/follower/printed-guide/tolerance project disclosures | User-generated; formal prior-art use should archive dated files/pages |
| [Indian application concern log](https://hackaday.io/project/10849-refreshable-braille-display/log/40208-discontinuing-work-on-current-actuation-method) | Exact public assertion about `5559/CHE/2014`, date, and alleged technical coverage | Not an official patent source; cannot establish claims/status |
| [Electromechanical eccentric-cam module](https://hackaday.io/project/191181-electromechanical-refreshable-braille-module/details) | Public printed eccentric magnetic-cam/pin module | Project description, not a patent/status record |
| [MOLBED](https://www.instructables.com/MOLBED-Modular-Low-Cost-Braille-Electronic-Display/) | Public modular/printed/low-cost/magnetic-retention project | Creator-supplied record; exact earliest disclosure archive needed for litigation-grade use |
| [MagnePins ACM record](https://dl.acm.org/doi/10.1145/3746059.3747692), [Monash project](https://www.monash.edu/it/hcc/embodied-visualisation/projects/magnepins) | Shared carriage, electromagnetic setters, printed locking channels, maker fabrication | Performance claims not used beyond accessible primary/project material |

### 26.5 Verification notation used throughout

- **Verified fact:** supported by readable attached authority, patent claim/publication text, or dated primary/public project source.
- **DB signal:** database-generated status/family indication requiring official confirmation.
- **Report assertion:** retained only as a lead unless separately verified.
- **Inference:** a reasoned technical consequence, explicitly not a sourced claim or legal conclusion.
- **Recommendation:** project action under the governing constraints.
- **Unresolved:** evidence was unavailable, incomplete, partial, inaccessible, or insufficient; no gap was filled by guesswork.

The synthesis uses only the material actually present in the partial Perplexity report. It does not use another synthesis model's output, does not count votes, does not revive historical Phase 2 conclusions as facts, and does not treat confidence of writing as evidence quality.
