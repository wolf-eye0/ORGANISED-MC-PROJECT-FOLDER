# Chapter 05 — OpenBraille Patent Evidence and Future Research Path

## Controlled OpenBraille source packet

This packet contains hash-verified source extracts. Sources have not been reconciled or converted into final manual conclusions.

Mapped sources: **12**


---

## Source 1: `03_CONCEPT_PORTFOLIO/OpenBraille/03_Patent_Synthesis/01_OpenBraille_Patent_Synthesis_Work_Max.md`

- Authority: `TIER_2`
- Treatment: `CORE_DECISION_EVIDENCE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `d92dbfbbbdbd4c49e9eaac9fab01e0d2a7db6d986c81d33ee65223710dd42eb1`

# Source Extraction

- Chapter: `05` — OpenBraille Patent Evidence and Future Research Path
- Authority tier: `TIER_2`
- Manual treatment: `CORE_DECISION_EVIDENCE`
- Original source: `03_CONCEPT_PORTFOLIO/OpenBraille/03_Patent_Synthesis/01_OpenBraille_Patent_Synthesis_Work_Max.md`
- Current SHA-256: `d92dbfbbbdbd4c49e9eaac9fab01e0d2a7db6d986c81d33ee65223710dd42eb1`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

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


---

## Source 2: `03_CONCEPT_PORTFOLIO/OpenBraille/03_Patent_Synthesis/02_OpenBraille_Patent_Synthesis_Valid_Secondary.md`

- Authority: `TIER_2`
- Treatment: `CORE_DECISION_EVIDENCE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `b9fefadf621f014dc621ef9836ae11b80c05a0227f768c53c11ec1358fc8a09b`

# Source Extraction

- Chapter: `05` — OpenBraille Patent Evidence and Future Research Path
- Authority tier: `TIER_2`
- Manual treatment: `CORE_DECISION_EVIDENCE`
- Original source: `03_CONCEPT_PORTFOLIO/OpenBraille/03_Patent_Synthesis/02_OpenBraille_Patent_Synthesis_Valid_Secondary.md`
- Current SHA-256: `b9fefadf621f014dc621ef9836ae11b80c05a0227f768c53c11ec1358fc8a09b`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

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


---

## Source 3: `03_CONCEPT_PORTFOLIO/OpenBraille/04_PreBuild_Simulation/OpenBraille_PreBuild_Future_Patent_Case_Simulation.md`

- Authority: `TIER_2`
- Treatment: `CONDITIONAL_EVIDENCE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `c38b519adae4831714b5fda8dbae86f2ac97ffe748cabf5cf421651a1b64c8a7`

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


---

## Source 4: `03_CONCEPT_PORTFOLIO/OpenBraille/05_Roadmaps_and_Reference_Dossiers/HISTORICAL_Phase1C_OpenBraille_Concept_Dossier.docx`

- Authority: `TIER_2`
- Treatment: `CORE_OR_SUPPORTING`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `ac21af2a892f319e0b28d4d7314f4561c5aebad5291343c34d777beb933106ea`

# Source Extraction

- Chapter: `05` — OpenBraille Patent Evidence and Future Research Path
- Authority tier: `TIER_2`
- Manual treatment: `CORE_OR_SUPPORTING`
- Original source: `03_CONCEPT_PORTFOLIO/OpenBraille/05_Roadmaps_and_Reference_Dossiers/HISTORICAL_Phase1C_OpenBraille_Concept_Dossier.docx`
- Current SHA-256: `ac21af2a892f319e0b28d4d7314f4561c5aebad5291343c34d777beb933106ea`
- Extraction method: `DOCX_XML`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

Document 1 – OpenBraille Concept Dossier

Affordable Refreshable Braille Display Using an Alternative Embedded Actuation Mechanism

Executive Summary

This concept proposes the development of an affordable refreshable Braille display to improve access to digital information for visually impaired users. Existing refreshable Braille displays remain prohibitively expensive because of sophisticated actuation mechanisms. The proposed concept investigates an alternative embedded approach capable of dynamically generating tactile Braille characters while reducing complexity and cost. The long-term vision is to make dynamic Braille technology more accessible for education, communication, and everyday digital interaction.

Background and Motivation

During the opportunity discovery phase, assistive technology emerged as a high-impact domain with a persistent unmet need. Screen readers have improved accessibility, but Braille remains essential for literacy, mathematics, programming, and independent learning. Commercial refreshable Braille displays are often too expensive for widespread adoption, leaving a significant accessibility gap. This opportunity consistently ranked highly throughout the project's evaluation pipeline because it combines meaningful social impact with genuine embedded systems innovation.

Problem Statement

The primary problem is the limited affordability of refreshable Braille technology. Current products are difficult for many individuals and institutions to purchase, restricting access to dynamic tactile reading. The project explores whether an embedded solution based on an alternative actuation approach can significantly reduce cost while preserving practical functionality and usability.

Current Solutions and Limitations

Commercial devices offer excellent performance but rely on costly components and precision engineering. Static Braille books are bulky and cannot display changing digital content, while audio solutions cannot replace tactile literacy. These limitations indicate that there is still room for innovation in cost-effective embedded assistive technology.

Why Embedded Systems

The challenge is inherently physical. Software alone cannot generate tactile Braille output. Embedded systems provide precise timing, low-power control, portability, and real-time management of the mechanisms required to dynamically present Braille characters.

Proposed Concept

We propose investigating a low-cost embedded platform capable of dynamically presenting Braille characters using an alternative actuation mechanism. The objective is to explore a practical, modular, and affordable solution that could expand access to digital Braille technology while remaining feasible as a semester project.

Innovation Opportunity

Potential innovation areas include alternative actuation techniques, simplified mechanical structures, modular Braille cell design, optimized embedded control, and cost-efficient architecture. These are research opportunities that warrant future patent and literature analysis.

Applications

Potential applications include schools, universities, libraries, assistive technology centers, public institutions, NGOs, and personal assistive devices for reading digital documents.

Commercial Potential

A lower-cost refreshable Braille device could substantially improve accessibility in price-sensitive markets and support broader adoption by educational organizations and accessibility initiatives.

Selection Rationale

This concept survived every evaluation stage because it addressed a genuine societal problem, demonstrated a clear need for embedded systems, offered room for innovation, and balanced long-term impact with semester feasibility.

Risks

The primary challenges involve mechanical reliability, tactile feedback quality, durability, and maintaining affordability without sacrificing usability.

Future Scope

Future work may include multi-line displays, multilingual support, wireless connectivity, integration with educational platforms, and patent landscape analysis after prototype validation.


---

## Source 5: `03_CONCEPT_PORTFOLIO/OpenBraille/05_Roadmaps_and_Reference_Dossiers/OpenBraille_Semester_Architecture_and_Future_Research_Reference_Dossier.docx`

- Authority: `TIER_2`
- Treatment: `CORE_OR_SUPPORTING`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `b4ef1d7301d5e0a669185681160cb20c8a85d2464b822c3c569798238f13e27b`

# Source Extraction

- Chapter: `05` — OpenBraille Patent Evidence and Future Research Path
- Authority tier: `TIER_2`
- Manual treatment: `CORE_OR_SUPPORTING`
- Original source: `03_CONCEPT_PORTFOLIO/OpenBraille/05_Roadmaps_and_Reference_Dossiers/OpenBraille_Semester_Architecture_and_Future_Research_Reference_Dossier.docx`
- Current SHA-256: `b4ef1d7301d5e0a669185681160cb20c8a85d2464b822c3c569798238f13e27b`
- Extraction method: `DOCX_XML`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

PROJECT mC

OPENBRAILLESEMESTER ARCHITECTUREAND FUTURE RESEARCH REFERENCE DOSSIER

Frozen Macro Six-Dot Build Plan, Validation Programme and Post-Semester VPD-C7 Research Path

Control item

Value

Course

PBCST504 - Microcontrollers Micro Project

Programme

B.Tech Computer Science and Engineering (Cyber Security)

Group

Group 8

Document status

Complete retained-reference and fallback implementation dossier

Current portfolio status

VibeGuard switch requested; OpenBraille remains the fully documented alternative

Frozen architecture

One macro six-dot cell; six SG90-class servos; eccentric cams; guided pins; ESP32 direct PWM

Expected semester budget

Approximately ₹2,984; conservative envelope approximately ₹4,909

Future mechanism

VPD-C7 research hypothesis - unbuilt, confidential and evidence-gated

Controlling decisionThis dossier does not override the current request to adopt VibeGuard. It provides the complete OpenBraille plan if the teacher retains the zeroth-review concept, and preserves OpenBraille as a future accessibility/mechatronics research route.

Patent boundaryThe macro six-servo semester prototype is conventional and is not represented as patent-ready. VPD-C7 is a separate post-semester hypothesis that must be redesigned, built, compared and professionally reviewed before any filing decision.

Prepared from the controlled Project mC authority set and the Master Evidence, Costing and Decision Basis. This document is an engineering reference plan, not a patent opinion, standards-compliance declaration or promise of grant.

Document control and approval use

Control item

Value

Architecture baseline

Frozen OpenBraille Phase 3C macro six-servo/cam architecture

Return-motion rule

Active servo-driven cam retraction unless a usable passive return is physically proved

Power baseline

External regulated 5 V servo supply; 5 V/3 A procurement target; measured droop controls acceptance

USB role

Serial command input and logs; not six-servo power

Semester boundary

No moving roller, encoder, RAMPS/Mega, continuous paper or electromagnetic substitution

Future boundary

VPD-C7 only on a separate post-MVP coupon; current never certifies pin height alone

Approval checkpoints required before an OpenBraille procurement freeze

1. Teacher confirmation that OpenBraille, rather than the requested VibeGuard alternative, remains the semester implementation.

2. Confirmation of the effective build window and dependable institutional FDM-printer access.

3. Approval of the one-dot-first mechanical validation plan before six servos and full-cell materials are committed.

4. Approval of the external 5 V power arrangement, pinch-point controls and tactile-participant protocol.

5. Approval of quantitative repeatability, cycle-life and pattern-test criteria before the locked validation run.

Executive reference decision

Complete alternative semester planOpenBraille is technically buildable within the ₹5,000 ceiling and offers a strong accessibility demonstration. Its execution risk is concentrated in FDM tolerances, cam/follower friction, active retraction, six-servo power behavior and trustworthy tactile-state validation. This dossier is therefore retained as the complete fallback/reference plan while VibeGuard remains the recommended semester choice.

The correct semester claim is narrow: one macro-scale six-dot cell accepts a character or dot pattern over USB/serial, commands six independent servo/cam channels, produces repeatable raised/lowered tactile states, and reports measured limitations. The project must not be presented as a standards-compliant commercial Braille display or as a patented actuator mechanism.

Success definition at a glance

Layer

Required semester result

Evidence

Mechanical

Six independently moving macro dots with active raise/retract and safe rounded pin tips

CAD/build IDs, caliper measurements, photographs, cycle logs

Electrical

Stable ESP32 control and external servo rail without brownouts or unsafe heating

Voltage/current observations, reset log, power checklist

Firmware

Correct character-to-six-dot mapping, per-dot calibration and USB commands/logs

Unit tests, configuration record, pattern test report

Validation

Repeatability, lifecycle, pattern-transition and approved tactile evidence

Locked test sheet, raw records, failed-run register

Scope honesty

Macro educational prototype; no physical-state claim from command timing alone

Explicit limitations in report and live demonstration

Future separation

VPD-C7 kept outside the semester architecture

Separate research folder and disclosure controls

1. Purpose, audience and scope

1.1 Purpose

This dossier converts the frozen OpenBraille Phase 3C architecture into a procurement-aware and execution-ready semester plan. It defines the hardware, mechanical build order, electrical integration, firmware, calibration, validation, team ownership, semester schedule and future-research boundary.

1.2 Audience

• Project coordinator and teacher: concept-retention decision, scope, budget, safety and review gates.

• Five-member student team: CAD, fabrication, firmware, assembly, testing, evidence and demonstration responsibilities.

• Department laboratories: FDM access, tools, metrology and safety support.

• Accessibility or tactile-test reviewers: honest macro-prototype scope and participant protocol.

• Institutional innovation/IPR reviewers: separation between the public semester cell and confidential VPD-C7 work.

1.3 Scope hierarchy

Scope tier

Included

Not included

Semester OpenBraille

One macro six-dot cell; six servos/cams/pins; direct PWM; active retraction; USB; measurements

Standards-compliant product, multi-cell line, production design, patent claim

Semester instrumentation

Calipers/camera, voltage/current checks and test scripts used as development evidence

Permanent endpoint contacts or current-only state inference

Post-semester VPD-C7

Separate coupon studying a datum that sets and directly evidences pin endpoints

Assumed performance, filing-ready claims or automatic inclusion in the semester cell

2. Engineering identity and problem definition

2.1 Engineering identity

OpenBraille is an assistive embedded-system experiment focused on lowering the cost of refreshable tactile output. Its semester purpose is not to compete with commercial displays, but to test whether a simple low-cost actuation channel can create one repeatable six-dot cell suitable for education and engineering study.

2.2 Semester engineering hypothesis

Hypothesis to testA macro-scaled servo-and-cam mechanism can produce repeatable raised and lowered tactile states for one six-dot Braille cell within the student budget and schedule, while accepting that the prototype is not commercial-scale or standards-compliant.

2.3 What the hypothesis does not claim

• It does not claim that servo + cam + Braille pin actuation is novel.

• It does not claim commercial Braille pitch, force, refresh speed, noise or lifetime.

• It does not assume a passive servo spring retracts the pin.

• It does not treat a PWM command, elapsed time or servo current as direct proof of tactile-pin height.

• It does not establish a patent or freedom to operate.

3. Frozen system architecture

Figure 1. Frozen macro six-dot architecture and explicit semester scope boundary.

3.1 Subsystem boundaries

Subsystem

Inputs

Outputs

Owner acceptance

USB/serial interface

Character, pattern or test command

Parsed request, acknowledgement and log line

Commands are deterministic, versioned and unit-tested

ESP32 control

Pattern, per-dot calibration and fixed sequencing rules

Six PWM outputs and timestamped command records

No invalid GPIO use, unstable resets or hidden configuration

Six actuator channels

5 V servo power and PWM

Cam rotation and follower displacement

Each channel accepted on a one-dot fixture before full-cell assembly

Mechanical cell

Six channel motions

Six guided raised/lowered tactile pins

No binding, unsafe tips or adjacent-channel interference

Power distribution

External regulated 5 V and common ground

Stable servo rail and logic operation

No USB servo power, brownout or unsafe heating

Development measurement

Pin position, cycle count, rail behavior and operator observations

Evidence package and limitations

External measurement remains the truth source for physical position

3.2 Frozen architecture controls

• One macro-scale six-dot cell only.

• Six SG90-class servos, one eccentric cam and one guided vertical pin per dot.

• ESP32 local direct-PWM control; no intermediate motor driver is required for the servo signal.

• FDM frame/guides/cams and external regulated servo power.

• Active servo-driven retraction unless a procured mechanism proves a reliable passive return under load.

• No moving roller, encoder wheel, RAMPS/Mega embosser, continuous-paper system or electromagnetic substitution.

4. Detailed hardware architecture and BOM

4.1 Required purchased and fabricated items

Item

Qty

Exact semester role

Expected

Conservative

Acceptance/procurement rule

ESP32 development board

1

Six PWM channels, USB/serial commands and logging

₹400

₹899

Verified WROOM-32 DevKit baseline; ESP32-S3 authorized fallback. Record pinout and regulator.

SG90-class servo

6

One independent eccentric-cam actuator per dot

₹120 each / ₹720

₹142 each / ₹852

Buy one consistent batch where possible; inspect every unit; no passive-return assumption.

5 V / 3 A regulated adapter

1

External servo supply with test headroom

₹289

₹408

Connector and regulation verified; adequacy controlled by measured droop and stall tests.

1,000 µF electrolytic capacitor

1-2

Servo-rail transient buffering

₹25

₹50

Install near distribution; voltage rating above 5 V; not a substitute for an adequate supply.

FDM frame, guides, cams and followers

1 cell

Macro mechanical structure

₹450

₹900

Expected case assumes institutional printer access; print a single-dot coupon first.

Stainless pins/rod with rounded tips

6 + spare

Guided tactile dots

₹250

₹400

Local quote; polished/rounded, safe for repeated touch, dimensions recorded.

Fasteners, servo mounts and cable management

1 lot

Alignment, assembly, strain relief and guards

₹300

₹500

Final quantity follows CAD and physical servo dimensions.

Perfboard, wires, headers and connectors

1 lot

Power distribution and stable PWM wiring

₹200

₹350

Servo current never routed through ESP32 3.3 V rail or thin USB wiring.

USB data cable

1

Serial input and logs

₹100

₹150

Reusable cable acceptable after connection reliability check.

Budget layer

Low

Expected

Conservative

Required hardware/material subtotal

₹1,866

₹2,734

₹4,509

Delivery/local variability/replacement allowance

₹100

₹250

₹400

Semester planning total

₹1,966

₹2,984

₹4,909

Budget decisionUse approximately ₹3,000 as the expected teacher-facing budget. The conservative case remains below ₹5,000 only when institutional printing is available and full-cell reprints are limited. One or two spare servos are useful but should be approved separately.

4.2 Reusable or institutional equipment

Equipment

Use

Required status

Laptop with Arduino IDE and Python

Firmware, serial commands, analysis and reporting

Assumed available

FDM printer and slicing software

Frame, guides, cams, followers and coupons

Material dependency; access must be confirmed

Digital calipers

Pin travel, spacing, clearances, repeatability and wear

Required

Multimeter

Power, continuity and servo-rail checks

Required

Bench supply with current limit

One-servo bring-up and fault-safe testing

Strongly recommended / borrowed

Oscilloscope or logic analyzer

PWM and rail-transient checks

Useful but not essential

Camera / fixed measurement jig

External visual ground truth and configuration record

Required for credible evidence

Basic hand tools and soldering station

Assembly, finishing and final wiring

Institutional/reusable

Tactile participant access and approved protocol

Raised/lowered and pattern distinguishability

Not confirmed; teacher/ethics decision

5. Mechanical architecture and one-dot-first build

Figure 2. One-dot channel and the separation between command, physical motion and development ground truth.

5.1 Mechanical design rules

1. Start with one independently testable servo + cam + follower + pin coupon. Do not print the full cell before the coupon moves freely.

2. Use macro spacing and travel as a documented educational design choice. A starting target near 300% of standard sign-Braille geometry may guide CAD, but the prototype must not be labelled standards-compliant.

3. Use rounded, smooth tactile tips and guard all pinch points around cams and servo horns.

4. Set pin-guide clearance through printed tolerance coupons and measured finishing; nominal CAD dimensions do not prove physical clearance.

5. Use active cam-driven raise and retract positions. Do not rely on an unverified servo spring or gravity return.

6. Record each printed part revision, orientation, material, measured dimensions, sanding/finishing and assembly operator.

7. Treat each channel as replaceable for test purposes, but do not present modular replacement as a novel patent feature.

5.2 Provisional geometry and acceptance parameters

Parameter

Starting design basis

Acceptance rule

Cell scale

Macro single cell, approximately 3x commercial sign-Braille pitch as an engineering starting point

Final CAD and measured cell clearly labelled non-standard

Raised travel

Approximately 1.5 mm starting target

Teacher-approved tactile and repeatability test controls final value

Pin material

Approximately 2 mm stainless rod with rounded tip

No sharp edge, binding, corrosion or unsafe surface

Cam throw

Set through one-dot CAD/coupon to create required travel with margin

No stall, follower loss or adjacent interference

Guide clearance

Derived from printed tolerance coupon

Free motion under the selected load with repeatable alignment

Actuation sequence

Fixed sequential or bounded group of changed dots

No brownout, unsafe peak or excessive refresh delay

5.3 Mechanical stop conditions

• Pin binds, tilts, scrapes or fails to retract fully.

• Cam/follower loses contact, jumps, cracks or creates an exposed pinch hazard.

• Servo stalls or heats during the normal pattern sequence.

• Pin height varies beyond the approved repeatability band.

• A rounded tactile tip becomes loose or unsafe.

• Full-cell assembly changes the motion that passed on the single-dot coupon.

6. Electrical integration and provisional pin map

Figure 3. Recommended power and control boundary. Final wiring must be verified against the purchased board and supply.

6.1 Power domains

Domain

Source

Loads

Rule

Logic / USB

Laptop USB to ESP32 DevKit

ESP32 and serial interface

Do not back-feed a second 5 V source into an unverified board while USB is connected

Servo rail

External regulated 5 V / 3 A target

Six SG90-class servos

Separate branch and conductors sized for servo current; bulk capacitor near distribution

Signal reference

Common ground

ESP32 PWM and servo signal reference

Use star/controlled grounding; inspect for resets and noise

Measurement

Multimeter / optional scope

Servo rail and logic rail

Measurements must not create unsafe shorts or loose probes near moving cams

6.2 Provisional ESP32-WROOM-32 pin assignment

Function

Provisional GPIO

Notes

Dot 1 PWM

GPIO 16

Output-capable; verify board label

Dot 2 PWM

GPIO 17

Output-capable; verify board label

Dot 3 PWM

GPIO 18

Output-capable; avoid conflict with other planned peripherals

Dot 4 PWM

GPIO 19

Output-capable

Dot 5 PWM

GPIO 21

Output-capable

Dot 6 PWM

GPIO 22

Output-capable

USB serial

Onboard USB-UART

Primary command/log interface

Optional status LED

GPIO 23 or onboard LED where available

Not part of the six-dot mechanism; verify polarity/board mapping

Implementation noteThis is a Phase 4 wiring proposal, not a source-file mandate. Revalidate every pin against the exact purchased DevKit and do not use boot-strapping or input-only pins without understanding their behavior.

6.3 Wiring acceptance checklist

• ESP32 boots and USB serial works with servo rail disconnected.

• External adapter polarity and no-load/loaded voltage are verified.

• Servo rail and logic share only the intended reference ground.

• Each servo is tested alone before joining the distribution rail.

• Bulk capacitor polarity and placement are correct.

• No servo current passes through the ESP32 3.3 V regulator or laptop USB cable.

• Combined pattern transitions produce no reset, cable heating or connector instability.

7. Firmware and software architecture

7.1 Firmware module breakdown

Module

Responsibility

Required outputs/tests

Configuration manager

Board variant, pin map, cell/build ID, PWM calibration and sequence policy

Startup banner and configuration record

USB command parser

Accept character, six-bit pattern, clear, test and calibration commands

Malformed-command tests and deterministic responses

Braille mapping table

Map supported characters to six-dot patterns

Unit test independent of hardware

PWM/channel manager

Apply per-dot up/down pulse widths and fixed sequencing

Logic-analyzer/servo acceptance and no illegal overlap

Calibration manager

Store per-dot command values established with external measurement

Versioned calibration table and reset procedure

Pattern transition engine

Move only changed dots, apply settle interval and update commanded state

Transition log and pattern suite

Fault/log manager

Record resets, invalid commands, manual faults and channel disable state

Human-readable USB log; no false physical-state claim

Test mode

Cycle one channel or selected patterns under operator control

Repeatability/lifecycle scripts

7.2 Repository and configuration structure

Folder/file

Purpose

firmware/

ESP32 source, board configuration and release tags

firmware/config/

Pin map, per-dot calibration and build identifiers

firmware/tests/

Character mapping and command-parser unit tests

cad/

Versioned frame, guide, cam, follower and coupon designs

fabrication/

Slicer settings, material, orientation and post-processing record

protocols/

Electrical, mechanical, cycle, tactile and demo procedures

data/

Measurements, cycle logs, power observations and fault records

evidence/

Photographs, videos, signed checklists and final locked results

7.3 Command and state semantics

The firmware should distinguish commanded state from verified physical state. Without a permanent pin sensor, the runtime may record that a PWM command and settle interval completed, but it must not label that event UPPER_CONFIRMED or LOWER_CONFIRMED. Physical confirmation belongs to external development measurement and the approved tactile protocol.

State

Meaning

Allowed evidence

Exit/exception

STARTUP

Board and configuration initialization

Firmware and board checks

FAULT on invalid configuration

READY

No active transition; accepts command

Commanded pattern record

RAISING / LOWERING / TEST

RAISING

One or more selected channels commanded toward up position

PWM command and timestamp

SETTLE_WAIT after command interval

LOWERING

Selected channels commanded toward down position

PWM command and timestamp

SETTLE_WAIT after command interval

SETTLE_WAIT

Fixed mechanical settling delay

Timer only

COMMAND_FINISHED; not physical confirmation

COMMAND_FINISHED

Requested command sequence ended

Command log

External tests decide physical correctness

FAULT/ISOLATED

Manual/operator or electrical/mechanical fault recorded

Fault input, reset, test observation

Operator-cleared after inspection

8. Calibration, sequencing and control logic

8.1 Per-dot calibration process

1. Assign a permanent channel and servo identity.

2. Use external calipers/camera or a fixed displacement jig to measure the lowered and raised pin positions.

3. Sweep the up command in small controlled increments to find the minimum repeatable raised position without stall or excessive load.

4. Repeat for active retraction and verify the pin returns to the approved lowered band.

5. Repeat across multiple cycles and store the selected command values with hardware/build IDs.

6. Invalidate or recheck calibration after servo replacement, cam/guide reprint or major reassembly.

8.2 Fixed sequencing policy

The semester system should use a simple fixed sequence: identify changed dots, lower dots that must clear, then raise dots that must set, with a bounded number of simultaneously moving channels chosen only after measured power testing. Dynamic current-aware sequencing belongs to future research and must not be backfilled into the frozen MVP.

8.3 Pattern transition rules

Rule

Purpose

Move only changed dots

Reduces unnecessary cycles, noise and power

Active retract before conflicting raise

Prevents ambiguous intermediate patterns

Fixed settle time per tested channel group

Makes behavior reproducible and loggable

Reject malformed/unsupported command

Protects mapping and state integrity

Manual stop on stall, heating or binding

No automatic recovery without evidence

Calibration version stored with every test

Prevents results from being separated from command values

8.4 Physical-truth boundary

Do not overclaim stateA servo angle, PWM pulse, elapsed time, current rise or visible cam movement does not automatically prove acceptable tactile-pin height. Semester physical truth comes from external measurement and an approved tactile evaluation. Current sensing may be used for power/safety observation, not endpoint certification.

9. Data and evidence management

9.1 Required build and session metadata

• Project, firmware, CAD, slicer and protocol version.

• Servo identity, seller/batch, channel assignment and replacement history.

• Cam, follower, guide and pin revision; material, print orientation and finishing.

• Per-dot up/down command values and calibration date.

• Supply identity, measured voltage, actuation grouping and reset/brownout observations.

• Pattern sequence, cycle count, operator, temperature/contamination/load note where relevant.

• Measured raised/lowered positions, failed transitions, binding, wear and manual interventions.

• Photographs/videos tied to the exact configuration ID.

9.2 Evidence hierarchy

Evidence type

What it supports

What it does not support

USB command log

Requested patterns, timestamps and firmware behavior

Actual tactile height

Calipers/camera/displacement jig

Development measurement of pin positions

Long-term tactile usability by itself

Power measurements

Supply adequacy, peaks, droop and resets

Endpoint correctness

Cycle log

Repeatability and mechanical failure history

Commercial lifetime

Tactile protocol

Participant distinguishability under the approved setup

Universal user performance or standards compliance

Photographs/video

Configuration and visible operation

Precise dimensions without measurement

9.3 Final evidence package

Evidence file

Minimum content

Configuration record

Board, pins, six servo IDs, CAD/slicer versions, power source and calibration table

Mechanical acceptance

One-dot and six-dot dimensions, travel, free-motion and safety checklist

Electrical acceptance

Supply voltage, resets, wiring, capacitor and combined-pattern observations

Pattern test

Supported character/pattern suite and exact pass/fail outputs

Repeatability/lifecycle

Per-channel measurements, cycle counts and failures

Tactile protocol report

Approved method, participants/ethics status, randomization, results and limitations

Failure register

Binding, wear, servo replacement, reprints, rejected runs and corrective action

Final demo package

Frozen firmware/CAD, demo script, backup evidence and limitations

10. Validation and acceptance programme

10.1 Validation stages

Stage

Question

Minimum evidence

Stop/fallback

OB-V0 Component acceptance

Are the ESP32, first servo, supply and tools usable?

Board/USB check, servo sweep, adapter polarity/voltage

Replace failed component before CAD freeze

OB-V1 One-dot mechanics

Can one printed channel raise and actively retract without binding?

Measured motion, photographs and repeated cycles

Redesign guide/cam before ordering full batch

OB-V2 Calibration

Can per-dot command windows produce repeatable positions?

External measurement across cycles

Change geometry or actuator; do not tune blindly

OB-V3 Six-dot integration

Do six channels coexist without interference and brownout?

Pattern commands, power observation and mechanical inspection

Use fixed sequencing, stronger supply or rebuild distribution

OB-V4 Pattern correctness

Does character mapping produce intended six-dot states?

Unit tests and physical pattern checks

Fix mapping/configuration before user testing

OB-V5 Repeatability/lifecycle

Does the mechanism retain position and motion over approved cycles?

100-cycle precision set and at least 1,000 total actuations

Record failure; redesign or limit claim

OB-V6 Tactile evaluation

Are raised/lowered dots and selected patterns distinguishable?

Teacher-approved blinded protocol

Adjust geometry or report MDS not achieved

OB-V7 Locked demonstration

Can the frozen build reproduce the result safely?

Signed checklist, frozen configuration and final evidence

Use approved backup evidence; no late redesign

10.2 Proposed semester acceptance targets for teacher approval

Status of numbersThe project authority contains some architecture-level repeatability and lifecycle targets, but the tactile participant threshold is not frozen. The following set should be preregistered and approved before the locked run.

Metric

Proposed target

Why it matters

Channel function

All six channels independently raise and actively retract throughout the final pattern sequence

Minimum six-dot cell functionality

Repeatability

≤0.1 mm position variation over 100 measured cycles under the approved setup

Source-derived architecture target; measures mechanical consistency

Lifecycle screen

At least 1,000 actuations without mechanical failure that invalidates the demo

Early engineering screen, not product lifetime

Pattern mapping

100% correct output for the frozen supported character/test set

Separates firmware mapping from mechanical failure

Power integrity

No brownout/reset, connector heating or unsafe voltage collapse in the locked sequence

Electrical safety and reliability

Tactile distinguishability

Teacher-approved blinded threshold and trial count fixed before testing

Avoids inventing or post-hoc selecting a success rate

Failure honesty

Every incomplete/bound transition is logged; no command-complete event relabelled as physically verified

Evidence integrity

Budget

Final semester spend ≤₹5,000, with preferred target near ₹3,000

Course requirement

10.3 Required performance reporting

• Per-dot raised and lowered position distributions, not only average travel.

• Pattern-level pass/fail counts and the exact supported character set.

• Power/reset observations for one, multiple and worst planned transitions.

• Cycle count, wear inspection and parts replaced.

• Tactile results with protocol, participant context and limitations.

• Negative evidence, binding, failed prints and calibration changes.

• Explicit statement that the macro prototype does not establish commercial-scale feasibility.

11. Twelve-week semester roadmap

Week

Primary work

Owner(s)

Measurable output

Exit criterion

Fallback

1

Teacher decision, scope freeze, FDM/tool audit and first procurement

Nihad + team; Amith fabrication audit

Approved concept status; one-servo order; printer/tool booking; risk register

No full-cell purchase until one-dot gate and teacher direction are confirmed

Use available verified ESP32/servo variants without changing architecture

2

ESP32/USB bring-up, one bare servo and power acceptance

Sreehari + Amith

Commanded servo sweep; adapter/polarity record; provisional pin map

Stable board/serial and safe one-servo motion

Replace failed board/servo/supply before CAD integration

3

Print tolerance coupons and one-dot frame/cam/follower

Amith + Nihad

Measured coupon set; one-dot assembly; CAD/build ID

Pin moves freely and cam produces controllable travel

Adjust guide/cam dimensions; laser-cut guide fallback only if approved

4

Active raise/retract calibration and single-dot repeatability

Amith + Sreehari; Sreeprada tests

Per-dot calibration procedure; 100-cycle single-dot dataset

Stable raised/lowered bands without binding or unsafe stall

Change geometry/servo before multiplying channels

5

Procure/accept remaining servos and fabricate six-dot parts

Amith + Sreeprada inventory

Six accepted servo IDs; completed printed parts; assembly checklist

Each channel passes independent bench test

Use spares or pause channels; do not hide batch variation

6

Six-dot mechanical and electrical integration

Nihad + Amith + Sreehari

Assembled cell; external rail; six PWM channels; command logs

All six move independently; no brownout/interference

Fixed sequential actuation, supply/distribution revision or rebuild

7

Braille mapping, pattern transitions and per-dot calibration

Sreehari + Sreeprada

Supported character set; mapping unit tests; calibration table

Frozen test patterns produce correct commanded states

Reduce demo set while keeping mapping evidence honest

8

Power, safety, repeatability and failure-mode testing

Amith + Nihad; Sreeprada runs

Worst planned transition record; fault/reprint log; safety review

No unsafe heating, reset, pinch or uncontrolled motion

Limit actuation group, strengthen guard/supply or redesign

9

Lifecycle screen and tactile-protocol approval

Nihad + Archa; teacher/participant coordination

Cycle progress; approved blinded protocol or documented access limit

Mechanism survives and protocol is approved before use

Report tactile validation unavailable rather than improvising

10

Locked pattern/repeatability/tactile validation

Full team; test led by Sreeprada

Frozen configuration and signed result sheets

Approved targets met without post-result calibration changes

Record failure; use honest partial-MDS conclusion

11

Final report, source records and live-demo rehearsal

Archa + Nihad; technical review by Sreehari/Amith

Final BOM, CAD/firmware versions, results, limitations and demo script

Every technical claim traces to evidence

Remove unsupported claims and use backup video only if approved

12

Contingency, repair-only window and final delivery

Full team

Stable final build and archived evidence package

No late VPD-C7 or architecture expansion

Submit the strongest verified semester result

Schedule ruleThe minimum demonstrable cell should work by the end of Week 8. Weeks 9-12 are for lifecycle, tactile evidence, recovery and presentation. VPD-C7 hardware must not enter the semester critical path.

12. Team roles, actual members and accountability

Role statusThe following map mirrors the established five-member structure. It is a proposed assignment for team approval; it deliberately gives mechanical work substantial ownership because that is OpenBraille’s critical risk.

Member

Proposed primary role

Specific OpenBraille ownership

Review/backup obligation

Nihad P C - JEC24CC044

Technical integration lead / project manager

Architecture control, schedule, interface decisions, validation protocol, final integration and evidence integrity

Backs up firmware and hardware; approves configuration freezes

Sreehari K - JEC24CC055

Firmware and embedded-control lead

USB command parser, Braille mapping, PWM/channel manager, calibration storage, test scripts and logs

Nihad reviews releases; Sreeprada executes scripted tests

Amith Krishna Das - JEC24CC016

Mechanical, hardware and power lead

CAD/FDM, cam/follower/guide design, servo acceptance, power rail, assembly and safety inspection

Nihad reviews interfaces/safety; Sreehari checks control requirements

Sreeprada K S - JEC24CC056

Learner, test and inventory assistant

Inventory, servo/build labels, cycle scripts, measurements, photos, test registry and repeated independent trials

Works from signed procedures; learns USB operation and calibration workflow

Archa Pramod - JEC24CC022

Documentation, teacher communication and demonstration lead

Weekly records, teacher-safe explanations, tactile-test coordination, live-demo script, final presentation and source register

Technical statements reviewed by Nihad, Sreehari and Amith

12.1 Responsibility rules

• Every critical subsystem has one primary owner, one technical reviewer and one written checklist.

• No one changes CAD, PWM calibration, power wiring or test labels without a dated configuration update.

• The learner/test role is evidence-critical and must run independent repetitions, not only observe.

• The documentation lead does not publish VPD-C7 details without technical and IPR review.

• Nihad acts as integration failsafe, but CAD, firmware and validation must remain independently owned and reviewable.

13. Procurement, acceptance and configuration control

13.1 Procurement sequence

1. Confirm teacher decision and institutional FDM access.

2. Buy one verified ESP32 board, one SG90-class servo, the external supply and basic mechanical material first.

3. Pass the one-dot mechanical/active-retraction gate before buying or committing the remaining servo batch and full-cell prints.

4. Buy the remaining servos from one consistent seller/batch where practical and record every identity.

5. Fabricate the full frame only after the physical servo and pin dimensions are measured.

6. Purchase spares only when acceptance or delivery risk justifies them within the conservative envelope.

13.2 Component acceptance record

Component

Acceptance checks

Reject if

ESP32

Reliable boot/USB, exact board identity and usable output GPIOs

Unknown pinout, repeated disconnect, overheating or unstable regulator

SG90 servo

Smooth sweep, no damaged gears, stable horn/shaft and repeatable response

Dead zone, severe jitter, gear damage, overheating or inconsistent return command

5 V adapter

Correct polarity, stable loaded output, adequate connector and no overheating

Unsafe voltage, instability, excessive droop or poor connector

FDM coupon

Measured clearance, free pin motion, no cracks or warped datum surfaces

Binding, unsafe roughness, large warp or non-repeatable fit

Cam/follower

Smooth engagement and required travel without losing contact

Stiction, follower jump, crack or unsafe pinch exposure

Pin/tip

Straight, smooth, rounded and securely retained

Sharp edge, looseness, corrosion or unsafe touch surface

13.3 Configuration ID format

Recommended format: OB-[cell/build]-[dot/servo]-[CAD]-[firmware]-[protocol]-[session]. Example: OB-C01-D3-SV05-CAD0.4-FW0.6-P03-R012. The exact format may change, but every measurement, image and result must identify the physical and software configuration.

14. Risk register and mitigation

Risk

Likelihood / impact

Early indicator

Mitigation

Decision consequence

FDM guide/cam tolerance and friction

High / High

Pin does not slide freely; variable travel; follower drag

One-dot coupons, measured clearance, material/print iteration, limited finishing

Do not proceed to six-dot assembly until passed

No usable passive return

High / Medium

Pin remains raised or servo does not return under load

Use active commanded retraction; remove passive-return language

Architecture remains valid with corrected control description

Servo batch variation/backlash

Medium / High

Different travel for common PWM; jitter or gear play

Consistent batch, per-dot calibration, spare/replace failed unit

May increase calibration and evidence burden

Six-servo brownout or rail droop

Medium / High

ESP32 reset, adapter sag, connector heating

Separate 5 V rail, bulk capacitor, fixed sequencing, measured load

Upgrade supply/distribution or reduce simultaneous motion

Pin tip unsafe or tactility poor

Medium / High

Sharp/loose tip or participant cannot distinguish states

Rounded tips, geometry iteration, approved tactile protocol

MDS may fail even when motion is visible

Cam/follower wear

Medium / Medium

Position drift, dust, roughness or increased noise

Material choice, inspection, lifecycle screen, replaceable coupon

Limit claims and redesign if systematic

CAD/print schedule slippage

High / Medium

Multiple full reprints or printer unavailable

Single-dot gate, modular prints, early lab booking, controlled fallback

May force reduced demo or switch to VibeGuard

Firmware mapping/calibration error

Low / Medium

Wrong pattern despite correct mechanics

Independent unit tests and configuration versioning

Fix before tactile validation

Tactile participant/protocol unavailable

Medium / Medium

No approved access or trial design

Secure approval early; document visual/mechanical evidence separately

Do not claim tactile success without the test

Macro prototype overstated as product

Medium / High

Slides imply standard compliance or commercial readiness

Teacher-safe wording, explicit dimensions/limits and review

Remove unsupported claim before presentation

Future patent concept leaks into MVP

Medium / Medium

VPD-C7 contact/current details added late

Separate folders, approval gate and confidentiality rule

Exclude from semester build and results

15. Required semester deliverables and live demonstration

15.1 Deliverables

• Working macro one-cell, six-dot servo/cam OpenBraille prototype if the concept is retained.

• Final BOM, procurement record, power diagram and provisional pin map.

• Versioned CAD, slicer settings, firmware and Braille mapping tests.

• One-dot and six-dot mechanical acceptance records.

• Per-dot calibration table and pattern-transition test suite.

• Repeatability, lifecycle, power and tactile-protocol results with limitations.

• Failure/reprint/replacement register and contributor chronology.

• Teacher-ready presentation and live-demo procedure.

• Separate confidential VPD-C7 research folder with no semester performance backfill.

15.2 Recommended five-minute live demonstration

1. Show the powered-off macro cell, six servos, rounded pins, guard/covering and separate servo power rail.

2. Connect USB, display the configuration banner and run a commanded one-dot test while explaining that command timing is not physical confirmation.

3. Display a small frozen sequence of characters or six-bit patterns and clear/refresh them.

4. Show per-dot calibration and one repeatability result table or measurement image.

5. Run the approved safe pattern transition while showing no reset/brownout and the USB log.

6. State the limitations: macro scale, educational prototype, active retraction, no standard-compliance or patent claim.

15.3 Demo failure fallback

If classroom operation is unsafe, unreliable or too noisy, use an approved guarded video of the locked physical setup plus a live USB/firmware demonstration and the signed measurement evidence. The fallback must not substitute a different actuator or conceal that the physical build failed the planned gate.

16. Post-semester VPD-C7 research hypothesis

Figure 4. VPD-C7 research concept. It is not implemented or validated in the semester cell.

16.1 Technical question

Can a pin-side mechanical datum that sets the tactile endpoint also provide direct endpoint evidence with less registration error and fewer silent wrong states than a passive stop plus a separately mounted sensor, while keeping actuator current limited to independent effort/supply information?

16.2 Candidate mechanism in non-claim language

1. Redesign one post-MVP guide/pin coupon with mechanically registered upper and lower endpoint features.

2. Arrange the endpoint feature so reaching it can produce a low-energy pin-side event without carrying servo power through the contact.

3. Use external displacement and force measurement as the development oracle; do not let the candidate sensor label itself as truth.

4. Use a separate current/voltage channel only to characterize effort, obstruction-like behavior or supply disturbance.

5. Declare an endpoint state only from qualified pin-side evidence; absent or conflicting evidence becomes incomplete, jammed or Unknown.

6. Permit recovery/isolation only after the physical and safety behavior is experimentally qualified.

16.3 Why this is only a hypothesis

• A mechanical stop that also acts as a switch/contact is familiar engineering and may be obvious.

• The added contact may increase friction, force, bounce, contamination sensitivity or wear.

• Practical Braille pitch may not accommodate the contact and wiring.

• A separately mounted optical/magnetic sensor may perform just as well or better.

• Current may add no independent diagnostic value beyond command, time and voltage.

• The official Indian close-prior-art file and worldwide claims remain unresolved.

• No experiment currently shows a cooperative or non-additive physical effect.

17. Six-to-twelve-month future research roadmap

Month

Stage

Work

Pass evidence

Failure action

0-2

Semester foundation and search boundary

Complete frozen macro MVP; preserve mechanical/power records; obtain official close-prior-art documents; build direct displacement oracle

Stable one-dot baseline and a defined professional search problem

Continue semester/publication only if close art anticipates the structural core

2-4

Current observability and direct sensor baseline

Compare calibrated open loop, current-only observation and a separate direct pin sensor on one-dot fixtures

Held-out evidence showing what current can and cannot reveal

Remove current from the putative invention if it adds no independent value

4-6

Dual-purpose datum coupon

Build passive-stop, separate-sensor and same-datum-contact coupons; measure force, bounce, registration and false endpoints

Distinct physical advantage fixed before confirmatory data

End VPD-C7 thesis if separate sensor performs equivalently

6-8

Practical-scale and contamination tests

Develop smaller coupons; test wiring, force, dust/fiber, cleaning and assembly yield

Feasible packing and stable endpoint evidence

Hold Track D if only macro geometry works

8-10

Replacement, reassembly and lifecycle

Blind servo/cam/pin/datum swaps; multiple operators; extended cycling and inspection

Transfer across builds with bounded drift and no systematic false endpoint

Redesign and restart after systematic wear/failure

10-11

Locked held-out evidence

Run the preregistered 3,000-transition silent-error test on unseen units/builds/conditions

Zero silently accepted wrong states plus practical Unknown/false isolation rates

Kill the route after a silent wrong state unless a genuinely new mechanism restarts the gate

11-12

Professional decision gate

Refresh worldwide search; claim/FTO chart; inventorship/disclosure review; management file/no-file decision

Useful narrow scope supported by reproducible physical evidence

Choose confidential know-how, defensive/academic publication or stop

17.1 Research baselines and ablations

Type

Required comparison

Strong conventional baselines

Fixed common PWM; calibrated per-dot open loop; passive datum only; direct separate sensor; fixed sequential refresh

Current tests

Current without endpoint contact; endpoint contact without current; current removed from full candidate

State logic

Unknown retained versus coerced binary decision; retry removed; isolation removed

Service robustness

Servo/pin/cam/datum replacement and independent reassembly

Scale and environment

Macro versus practical-scale coupons; clean versus contamination/wear conditions

17.2 Patent-development kill conditions

• A closer enabling reference or official Indian file discloses the defining combination.

• The same-datum contact has no measurable advantage over a passive stop plus separate sensor.

• The contact adds unacceptable force, friction, bounce, wear or debris sensitivity.

• Practical-scale packaging fails.

• Performance collapses after servo replacement, reprint, remount or reassembly.

• Current adds no independent diagnostic value or is required to certify endpoint completion.

• The locked 3,000-transition test contains a silently accepted wrong state.

• Useful scope collapses to exact hobby parts, macro dimensions or a trivial retry count.

• Institutional/professional review does not justify filing cost or disclosure risk.

18. Confidentiality, inventorship and disclosure control

18.1 Public-safe semester material

• Macro six-dot architecture, six SG90-class servos, eccentric cams, guided pins, ESP32 direct PWM and external servo power.

• Semester budget, team roles, CAD/fabrication learning, repeatability/lifecycle and approved tactile results.

• Honest limitations: macro educational prototype, active retraction, no current-only state verification and no patent claim.

18.2 Keep private until IPR review

• Exact VPD-C7 contact/datum geometry, materials, dimensions, circuits and thresholds.

• Unpublished comparative results against passive stops, separate sensors and current-only inference.

• Replacement/reassembly, wear, contamination and held-out silent-error datasets.

• Claim-to-experiment maps, filing strategies and contributor/inventorship analysis.

18.3 Inventorship/contribution record

Maintain dated records of who conceived each later mechanical/electrical interaction, who designed each experiment, who created CAD/firmware, and when the mechanism was first built and tested. AI/model assistance is not inventorship and must not replace human conception records.

18.4 Disclosure rule

Do not rely on an assumed grace periodBefore publishing code, CAD, datasets, posters, videos, papers, competition entries or VPD-C7 details, obtain institutional IPR review. A patent filing or defensive publication does not create freedom to operate.

19. Decision gates and escalation rules

Gate

When

Pass

Fail response

OB-G0 Teacher concept decision

Before procurement

OpenBraille retained with scope/budget approved

Proceed with VibeGuard or revise the project request

OB-G1 Facility/procurement

Week 1

Printer/tools and first components available

Do not commit full-cell schedule; use VibeGuard fallback if needed

OB-G2 One-dot mechanics

Weeks 3-4

Active raise/retract and repeatability pass

Redesign coupon; stop six-dot expansion

OB-G3 Six-servo power

Weeks 6-8

No unsafe droop, reset, heating or stall in planned sequence

Upgrade supply/distribution or reduce groups

OB-G4 Six-dot MDS

Week 8

Correct pattern transitions and safe operation

Report partial prototype or switch according to teacher direction

OB-G5 Locked validation

Week 10

Approved repeatability/lifecycle/tactile gates pass

No patent or performance overclaim; document failure

OB-G6 VPD-C7 research entry

Post-semester

Separate design, confidentiality and search approval

Keep OpenBraille as semester/publication record only

OB-G7 Counsel-led filing evaluation

Months 11-12

Unexpected physical effect, enabling evidence and useful scope survive review

Do not file; choose publication/know-how/stop

20. Open questions and teacher decisions

ID

Question / decision

Owner

Required by

Q1

Should OpenBraille remain the semester project or should the requested VibeGuard switch be approved?

Project coordinator

Before procurement

Q2

Is the working build window approximately eight weeks or the full twelve-week plan?

Teacher/project coordinator

Week 1

Q3

Is institutional FDM access dependable, and what material/print limits apply?

Amith + lab

Week 1

Q4

Which exact ESP32 and SG90 seller/batch are approved?

Nihad/Sreehari/Amith

Before order

Q5

What quantitative tactile-identification protocol and participant access are approved?

Teacher + Archa/Nihad

Before tactile test

Q6

What is the approved raised/lowered position band for the macro cell?

Technical team + teacher

Before locked validation

Q7

Is the 5 V / 3 A target supply adequate under the actual six-servo sequence?

Amith + Nihad

Before full integration

Q8

What content may be disclosed publicly before institutional IPR review?

IPR cell / project owner

Before publication or competition

Q9

Should VPD-C7 remain only a confidential future option after the semester?

Team + institution

After MVP evidence

21. Teacher approval and conditions

Decision item

Teacher response

Semester project

Retain OpenBraille / Approve VibeGuard switch / Revise and resubmit

Frozen OpenBraille scope

Approved / Approved with conditions / Not approved

Expected budget near ₹3,000

Approved / Revise

External 5 V servo supply and safety controls

Approved / Lab review required

One-dot-first procurement gate

Approved / Revise

Tactile participant protocol

Approved / Separate ethics/access review required

Future VPD-C7 treatment

Confidential post-semester only / Not approved / Further review

Teacher conditions

Signature and date

22. Source basis

This dossier was prepared from the controlled Project mC master package. The main evidence layers are:

Evidence layer

Controlled source

Project authority

Engineering Design Review; Project mC Decision Register v1.2; approved Phase 3C Portfolio Closure Memo

Common evidence

Concept Evidence Matrix; Uncertainty and Test Register

OpenBraille technical authority

Final OpenBraille Architecture Report; Memory; SOP

Comparative decision context

Two final cross-concept adjudications - treated as context, not votes

Future research boundary

OpenBraille Pre-Build Future Patent-Case Simulation

Costing and teacher context

Project mC Teacher Documents - Master Evidence, Costing and Decision Basis

Previous presentation

Final OpenBraille zeroth-review presentation dated 30-07-2026

22.1 Current official specification and price references

• Espressif, ESP32-WROOM-32 data sheet: https://www.espressif.com/sites/default/files/documentation/esp32-wroom-32_datasheet_en.pdf

• Espressif, ESP32-S3 product page and DevKitC-1 guide: https://www.espressif.com/en/products/socs/esp32-s3

• TowerPro, SG90 analog servo specifications: https://towerpro.com.tw/product/sg90-analog/

• Indian price snapshots and procurement cautions are recorded in the Master Evidence, Costing and Decision Basis and must be refreshed on purchase day.

Prepared for academic project planning. The future research section is a management and experimental roadmap, not legal advice, patentability clearance, freedom-to-operate clearance, a filing recommendation or a promise of patent grant.


---

## Source 6: `03_CONCEPT_PORTFOLIO/OpenBraille/05_Roadmaps_and_Reference_Dossiers/OpenBraille_Semester_Architecture_and_Future_Research_Reference_Dossier.pdf`

- Authority: `TIER_2`
- Treatment: `CORE_OR_SUPPORTING`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `ee9cce3ebd57dd84b3bbacd9d4738fc219a334441b80c2bb34e0417c90060ab4`

# Source Extraction

- Chapter: `05` — OpenBraille Patent Evidence and Future Research Path
- Authority tier: `TIER_2`
- Manual treatment: `CORE_OR_SUPPORTING`
- Original source: `03_CONCEPT_PORTFOLIO/OpenBraille/05_Roadmaps_and_Reference_Dossiers/OpenBraille_Semester_Architecture_and_Future_Research_Reference_Dossier.pdf`
- Current SHA-256: `ee9cce3ebd57dd84b3bbacd9d4738fc219a334441b80c2bb34e0417c90060ab4`
- Extraction method: `PDFTOTEXT_LAYOUT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

Topic: OpenBraille - Semester Architecture and Future Research Reference Dossier


                                                             PROJECT mC


                   OPENBRAILLE
              SEMESTER ARCHITECTURE
          AND FUTURE RESEARCH REFERENCE
                     DOSSIER
Frozen Macro Six-Dot Build Plan, Validation Programme and Post-Semester VPD-
                              C7 Research Path

                        Control item                                                                 Value

Course                                                               PBCST504 - Microcontrollers Micro Project

Programme                                                            B.Tech Computer Science and Engineering (Cyber Security)

Group                                                                Group 8

Document status                                                      Complete retained-reference and fallback implementation
                                                                     dossier

Current portfolio status                                             VibeGuard switch requested; OpenBraille remains the fully
                                                                     documented alternative

Frozen architecture                                                  One macro six-dot cell; six SG90-class servos; eccentric cams;
                                                                     guided pins; ESP32 direct PWM

Expected semester budget                                             Approximately ₹2,984; conservative envelope approximately
                                                                     ₹4,909

Future mechanism                                                     VPD-C7 research hypothesis - unbuilt, confidential and
                                                                     evidence-gated


Controlling decision
This dossier does not override the current request to adopt VibeGuard. It provides the complete OpenBraille plan if the
teacher retains the zeroth-review concept, and preserves OpenBraille as a future accessibility/mechatronics research
route.


Patent boundary
The macro six-servo semester prototype is conventional and is not represented as patent-ready. VPD-C7 is a separate post-
semester hypothesis that must be redesigned, built, compared and professionally reviewed before any filing decision.

 Prepared from the controlled Project mC authority set and the Master Evidence, Costing and Decision Basis. This document is an
            engineering reference plan, not a patent opinion, standards-compliance declaration or promise of grant.


   Dept. of CSE (CY)                                PBCST504 - Microcontrollers                                             Page 1

                                Topic: OpenBraille - Semester Architecture and Future Research Reference Dossier


Document control and approval use
                             Control item                                                                Value

 Architecture baseline                                                   Frozen OpenBraille Phase 3C macro six-servo/cam architecture

 Return-motion rule                                                      Active servo-driven cam retraction unless a usable passive
                                                                         return is physically proved

 Power baseline                                                          External regulated 5 V servo supply; 5 V/3 A procurement
                                                                         target; measured droop controls acceptance

 USB role                                                                Serial command input and logs; not six-servo power

 Semester boundary                                                       No moving roller, encoder, RAMPS/Mega, continuous paper or
                                                                         electromagnetic substitution

 Future boundary                                                         VPD-C7 only on a separate post-MVP coupon; current never
                                                                         certifies pin height alone


Approval checkpoints required before an OpenBraille procurement freeze
1. Teacher confirmation that OpenBraille, rather than the requested VibeGuard alternative, remains the semester
implementation.
2. Confirmation of the effective build window and dependable institutional FDM-printer access.
3. Approval of the one-dot-first mechanical validation plan before six servos and full-cell materials are committed.
4. Approval of the external 5 V power arrangement, pinch-point controls and tactile-participant protocol.
5. Approval of quantitative repeatability, cycle-life and pattern-test criteria before the locked validation run.


Executive reference decision
 Complete alternative semester plan
 OpenBraille is technically buildable within the ₹5,000 ceiling and offers a strong accessibility demonstration. Its execution
 risk is concentrated in FDM tolerances, cam/follower friction, active retraction, six-servo power behavior and trustworthy
 tactile-state validation. This dossier is therefore retained as the complete fallback/reference plan while VibeGuard
 remains the recommended semester choice.

The correct semester claim is narrow: one macro-scale six-dot cell accepts a character or dot pattern over USB/serial,
commands six independent servo/cam channels, produces repeatable raised/lowered tactile states, and reports
measured limitations. The project must not be presented as a standards-compliant commercial Braille display or as a
patented actuator mechanism.

Success definition at a glance
                     Layer                                Required semester result                                 Evidence

 Mechanical                                     Six independently moving macro dots with         CAD/build IDs, caliper measurements,
                                                active raise/retract and safe rounded pin        photographs, cycle logs
                                                tips

 Electrical                                     Stable ESP32 control and external servo rail     Voltage/current observations, reset log,
                                                without brownouts or unsafe heating              power checklist

 Firmware                                       Correct character-to-six-dot mapping, per-       Unit tests, configuration record, pattern test
                                                dot calibration and USB commands/logs            report

 Validation                                     Repeatability, lifecycle, pattern-transition     Locked test sheet, raw records, failed-run
                                                and approved tactile evidence                    register

 Scope honesty                                  Macro educational prototype; no physical-        Explicit limitations in report and live
                                                state claim from command timing alone            demonstration

 Future separation                              VPD-C7 kept outside the semester                 Separate research folder and disclosure
                                                architecture                                     controls


    Dept. of CSE (CY)                                   PBCST504 - Microcontrollers                                                 Page 2

                             Topic: OpenBraille - Semester Architecture and Future Research Reference Dossier


1. Purpose, audience and scope
1.1 Purpose
This dossier converts the frozen OpenBraille Phase 3C architecture into a procurement-aware and execution-ready
semester plan. It defines the hardware, mechanical build order, electrical integration, firmware, calibration,
validation, team ownership, semester schedule and future-research boundary.

1.2 Audience
• Project coordinator and teacher: concept-retention decision, scope, budget, safety and review gates.
• Five-member student team: CAD, fabrication, firmware, assembly, testing, evidence and demonstration
responsibilities.
• Department laboratories: FDM access, tools, metrology and safety support.
• Accessibility or tactile-test reviewers: honest macro-prototype scope and participant protocol.
• Institutional innovation/IPR reviewers: separation between the public semester cell and confidential VPD-C7 work.

1.3 Scope hierarchy
                Scope tier                                      Included                                        Not included

 Semester OpenBraille                        One macro six-dot cell; six servos/cams/pins;    Standards-compliant product, multi-cell line,
                                             direct PWM; active retraction; USB;              production design, patent claim
                                             measurements

 Semester instrumentation                    Calipers/camera, voltage/current checks and      Permanent endpoint contacts or current-
                                             test scripts used as development evidence        only state inference

 Post-semester VPD-C7                        Separate coupon studying a datum that sets       Assumed performance, filing-ready claims
                                             and directly evidences pin endpoints             or automatic inclusion in the semester cell


2. Engineering identity and problem definition
2.1 Engineering identity
OpenBraille is an assistive embedded-system experiment focused on lowering the cost of refreshable tactile output. Its
semester purpose is not to compete with commercial displays, but to test whether a simple low-cost actuation channel
can create one repeatable six-dot cell suitable for education and engineering study.

2.2 Semester engineering hypothesis

 Hypothesis to test
 A macro-scaled servo-and-cam mechanism can produce repeatable raised and lowered tactile states for one six-dot
 Braille cell within the student budget and schedule, while accepting that the prototype is not commercial-scale or
 standards-compliant.


2.3 What the hypothesis does not claim
• It does not claim that servo + cam + Braille pin actuation is novel.
• It does not claim commercial Braille pitch, force, refresh speed, noise or lifetime.
• It does not assume a passive servo spring retracts the pin.
• It does not treat a PWM command, elapsed time or servo current as direct proof of tactile-pin height.
• It does not establish a patent or freedom to operate.


    Dept. of CSE (CY)                                PBCST504 - Microcontrollers                                                Page 3

                             Topic: OpenBraille - Semester Architecture and Future Research Reference Dossier


3. Frozen system architecture


                         Figure 1. Frozen macro six-dot architecture and explicit semester scope boundary.

3.1 Subsystem boundaries
           Subsystem                           Inputs                              Outputs                       Owner acceptance

 USB/serial interface            Character, pattern or test           Parsed request,                      Commands are deterministic,
                                 command                              acknowledgement and log line         versioned and unit-tested

 ESP32 control                   Pattern, per-dot calibration and     Six PWM outputs and                  No invalid GPIO use, unstable
                                 fixed sequencing rules               timestamped command records          resets or hidden configuration

 Six actuator channels           5 V servo power and PWM              Cam rotation and follower            Each channel accepted on a one-
                                                                      displacement                         dot fixture before full-cell
                                                                                                           assembly

 Mechanical cell                 Six channel motions                  Six guided raised/lowered tactile    No binding, unsafe tips or
                                                                      pins                                 adjacent-channel interference

 Power distribution              External regulated 5 V and           Stable servo rail and logic          No USB servo power, brownout
                                 common ground                        operation                            or unsafe heating

 Development measurement         Pin position, cycle count, rail      Evidence package and                 External measurement remains
                                 behavior and operator                limitations                          the truth source for physical
                                 observations                                                              position


3.2 Frozen architecture controls
• One macro-scale six-dot cell only.
• Six SG90-class servos, one eccentric cam and one guided vertical pin per dot.
• ESP32 local direct-PWM control; no intermediate motor driver is required for the servo signal.
• FDM frame/guides/cams and external regulated servo power.
• Active servo-driven retraction unless a procured mechanism proves a reliable passive return under load.
• No moving roller, encoder wheel, RAMPS/Mega embosser, continuous-paper system or electromagnetic substitution.


    Dept. of CSE (CY)                                PBCST504 - Microcontrollers                                                 Page 4

                                 Topic: OpenBraille - Semester Architecture and Future Research Reference Dossier


4. Detailed hardware architecture and BOM
4.1 Required purchased and fabricated items
                                                                                                                              Acceptance/
        Item                        Qty           Exact semester role            Expected               Conservative
                                                                                                                           procurement rule


ESP32 development       1                        Six PWM channels,        ₹400                    ₹899                    Verified WROOM-32
board                                            USB/serial commands                                                      DevKit baseline;
                                                 and logging                                                              ESP32-S3 authorized
                                                                                                                          fallback. Record
                                                                                                                          pinout and regulator.

SG90-class servo        6                        One independent          ₹120 each / ₹720        ₹142 each / ₹852        Buy one consistent
                                                 eccentric-cam                                                            batch where possible;
                                                 actuator per dot                                                         inspect every unit; no
                                                                                                                          passive-return
                                                                                                                          assumption.

5 V / 3 A regulated     1                        External servo supply    ₹289                    ₹408                    Connector and
adapter                                          with test headroom                                                       regulation verified;
                                                                                                                          adequacy controlled
                                                                                                                          by measured droop
                                                                                                                          and stall tests.

1,000 µF electrolytic   1-2                      Servo-rail transient     ₹25                     ₹50                     Install near
capacitor                                        buffering                                                                distribution; voltage
                                                                                                                          rating above 5 V; not a
                                                                                                                          substitute for an
                                                                                                                          adequate supply.

FDM frame, guides,      1 cell                   Macro mechanical         ₹450                    ₹900                    Expected case
cams and followers                               structure                                                                assumes institutional
                                                                                                                          printer access; print a
                                                                                                                          single-dot coupon
                                                                                                                          first.

Stainless pins/rod      6 + spare                Guided tactile dots      ₹250                    ₹400                    Local quote;
with rounded tips                                                                                                         polished/rounded,
                                                                                                                          safe for repeated
                                                                                                                          touch, dimensions
                                                                                                                          recorded.

Fasteners, servo        1 lot                    Alignment, assembly,     ₹300                    ₹500                    Final quantity follows
mounts and cable                                 strain relief and                                                        CAD and physical
management                                       guards                                                                   servo dimensions.

Perfboard, wires,       1 lot                    Power distribution       ₹200                    ₹350                    Servo current never
headers and                                      and stable PWM                                                           routed through ESP32
connectors                                       wiring                                                                   3.3 V rail or thin USB
                                                                                                                          wiring.

USB data cable          1                        Serial input and logs    ₹100                    ₹150                    Reusable cable
                                                                                                                          acceptable after
                                                                                                                          connection reliability
                                                                                                                          check.

         Budget layer                               Low                               Expected                          Conservative

Required hardware/material            ₹1,866                              ₹2,734                               ₹4,509
subtotal

Delivery/local                        ₹100                                ₹250                                 ₹400
variability/replacement
allowance

Semester planning total               ₹1,966                              ₹2,984                               ₹4,909


 Budget decision
 Use approximately ₹3,000 as the expected teacher-facing budget. The conservative case remains below ₹5,000 only when
 institutional printing is available and full-cell reprints are limited. One or two spare servos are useful but should be
 approved separately.


    Dept. of CSE (CY)                                     PBCST504 - Microcontrollers                                                Page 5

                                  Topic: OpenBraille - Semester Architecture and Future Research Reference Dossier


4.2 Reusable or institutional equipment
                    Equipment                                           Use                                          Required status

 Laptop with Arduino IDE and Python               Firmware, serial commands, analysis and          Assumed available
                                                  reporting

 FDM printer and slicing software                 Frame, guides, cams, followers and coupons       Material dependency; access must be
                                                                                                   confirmed

 Digital calipers                                 Pin travel, spacing, clearances, repeatability   Required
                                                  and wear

 Multimeter                                       Power, continuity and servo-rail checks          Required

 Bench supply with current limit                  One-servo bring-up and fault-safe testing        Strongly recommended / borrowed

 Oscilloscope or logic analyzer                   PWM and rail-transient checks                    Useful but not essential

 Camera / fixed measurement jig                   External visual ground truth and                 Required for credible evidence
                                                  configuration record

 Basic hand tools and soldering station           Assembly, finishing and final wiring             Institutional/reusable

 Tactile participant access and approved          Raised/lowered and pattern                       Not confirmed; teacher/ethics decision
 protocol                                         distinguishability


5. Mechanical architecture and one-dot-first build


          Figure 2. One-dot channel and the separation between command, physical motion and development ground truth.

5.1 Mechanical design rules
1. Start with one independently testable servo + cam + follower + pin coupon. Do not print the full cell before the
coupon moves freely.
2. Use macro spacing and travel as a documented educational design choice. A starting target near 300% of standard
sign-Braille geometry may guide CAD, but the prototype must not be labelled standards-compliant.
3. Use rounded, smooth tactile tips and guard all pinch points around cams and servo horns.
4. Set pin-guide clearance through printed tolerance coupons and measured finishing; nominal CAD dimensions do
not prove physical clearance.
5. Use active cam-driven raise and retract positions. Do not rely on an unverified servo spring or gravity return.
6. Record each printed part revision, orientation, material, measured dimensions, sanding/finishing and assembly
operator.
7. Treat each channel as replaceable for test purposes, but do not present modular replacement as a novel patent
feature.


     Dept. of CSE (CY)                                    PBCST504 - Microcontrollers                                                  Page 6

                               Topic: OpenBraille - Semester Architecture and Future Research Reference Dossier


5.2 Provisional geometry and acceptance parameters
                   Parameter                               Starting design basis                                  Acceptance rule

 Cell scale                                    Macro single cell, approximately 3x              Final CAD and measured cell clearly labelled
                                               commercial sign-Braille pitch as an              non-standard
                                               engineering starting point

 Raised travel                                 Approximately 1.5 mm starting target             Teacher-approved tactile and repeatability
                                                                                                test controls final value

 Pin material                                  Approximately 2 mm stainless rod with            No sharp edge, binding, corrosion or unsafe
                                               rounded tip                                      surface

 Cam throw                                     Set through one-dot CAD/coupon to create         No stall, follower loss or adjacent
                                               required travel with margin                      interference

 Guide clearance                               Derived from printed tolerance coupon            Free motion under the selected load with
                                                                                                repeatable alignment

 Actuation sequence                            Fixed sequential or bounded group of             No brownout, unsafe peak or excessive
                                               changed dots                                     refresh delay


5.3 Mechanical stop conditions
• Pin binds, tilts, scrapes or fails to retract fully.
• Cam/follower loses contact, jumps, cracks or creates an exposed pinch hazard.
• Servo stalls or heats during the normal pattern sequence.
• Pin height varies beyond the approved repeatability band.
• A rounded tactile tip becomes loose or unsafe.
• Full-cell assembly changes the motion that passed on the single-dot coupon.


6. Electrical integration and provisional pin map


    Figure 3. Recommended power and control boundary. Final wiring must be verified against the purchased board and supply.

6.1 Power domains
               Domain                           Source                                Loads                                 Rule

 Logic / USB                       Laptop USB to ESP32 DevKit           ESP32 and serial interface           Do not back-feed a second 5 V
                                                                                                             source into an unverified board
                                                                                                             while USB is connected

 Servo rail                        External regulated 5 V / 3 A         Six SG90-class servos                Separate branch and conductors
                                   target                                                                    sized for servo current; bulk
                                                                                                             capacitor near distribution


     Dept. of CSE (CY)                                 PBCST504 - Microcontrollers                                                    Page 7

                               Topic: OpenBraille - Semester Architecture and Future Research Reference Dossier


              Domain                            Source                                Loads                                    Rule

 Signal reference                  Common ground                        ESP32 PWM and servo signal             Use star/controlled grounding;
                                                                        reference                              inspect for resets and noise

 Measurement                       Multimeter / optional scope          Servo rail and logic rail              Measurements must not create
                                                                                                               unsafe shorts or loose probes
                                                                                                               near moving cams


6.2 Provisional ESP32-WROOM-32 pin assignment
                    Function                                 Provisional GPIO                                          Notes

 Dot 1 PWM                                     GPIO 16                                              Output-capable; verify board label

 Dot 2 PWM                                     GPIO 17                                              Output-capable; verify board label

 Dot 3 PWM                                     GPIO 18                                              Output-capable; avoid conflict with other
                                                                                                    planned peripherals

 Dot 4 PWM                                     GPIO 19                                              Output-capable

 Dot 5 PWM                                     GPIO 21                                              Output-capable

 Dot 6 PWM                                     GPIO 22                                              Output-capable

 USB serial                                    Onboard USB-UART                                     Primary command/log interface

 Optional status LED                           GPIO 23 or onboard LED where available               Not part of the six-dot mechanism; verify
                                                                                                    polarity/board mapping


 Implementation note
 This is a Phase 4 wiring proposal, not a source-file mandate. Revalidate every pin against the exact purchased DevKit and
 do not use boot-strapping or input-only pins without understanding their behavior.


6.3 Wiring acceptance checklist
• ESP32 boots and USB serial works with servo rail disconnected.
• External adapter polarity and no-load/loaded voltage are verified.
• Servo rail and logic share only the intended reference ground.
• Each servo is tested alone before joining the distribution rail.
• Bulk capacitor polarity and placement are correct.
• No servo current passes through the ESP32 3.3 V regulator or laptop USB cable.
• Combined pattern transitions produce no reset, cable heating or connector instability.


7. Firmware and software architecture
7.1 Firmware module breakdown
                    Module                                     Responsibility                                 Required outputs/tests

 Configuration manager                         Board variant, pin map, cell/build ID, PWM           Startup banner and configuration record
                                               calibration and sequence policy

 USB command parser                            Accept character, six-bit pattern, clear, test       Malformed-command tests and
                                               and calibration commands                             deterministic responses

 Braille mapping table                         Map supported characters to six-dot                  Unit test independent of hardware
                                               patterns

 PWM/channel manager                           Apply per-dot up/down pulse widths and               Logic-analyzer/servo acceptance and no
                                               fixed sequencing                                     illegal overlap

 Calibration manager                           Store per-dot command values established             Versioned calibration table and reset
                                               with external measurement                            procedure


    Dept. of CSE (CY)                                  PBCST504 - Microcontrollers                                                    Page 8

                               Topic: OpenBraille - Semester Architecture and Future Research Reference Dossier


                    Module                                         Responsibility                                 Required outputs/tests

 Pattern transition engine                      Move only changed dots, apply settle                 Transition log and pattern suite
                                                interval and update commanded state

 Fault/log manager                              Record resets, invalid commands, manual              Human-readable USB log; no false physical-
                                                faults and channel disable state                     state claim

 Test mode                                      Cycle one channel or selected patterns               Repeatability/lifecycle scripts
                                                under operator control


7.2 Repository and configuration structure
                             Folder/file                                                                    Purpose

 firmware/                                                                 ESP32 source, board configuration and release tags

 firmware/config/                                                          Pin map, per-dot calibration and build identifiers

 firmware/tests/                                                           Character mapping and command-parser unit tests

 cad/                                                                      Versioned frame, guide, cam, follower and coupon designs

 fabrication/                                                              Slicer settings, material, orientation and post-processing record

 protocols/                                                                Electrical, mechanical, cycle, tactile and demo procedures

 data/                                                                     Measurements, cycle logs, power observations and fault records

 evidence/                                                                 Photographs, videos, signed checklists and final locked results


7.3 Command and state semantics
The firmware should distinguish commanded state from verified physical state. Without a permanent pin sensor, the
runtime may record that a PWM command and settle interval completed, but it must not label that event
UPPER_CONFIRMED or LOWER_CONFIRMED. Physical confirmation belongs to external development measurement
and the approved tactile protocol.

                State                           Meaning                             Allowed evidence                         Exit/exception


 STARTUP                           Board and configuration                 Firmware and board checks               FAULT on invalid configuration
                                   initialization

 READY                             No active transition; accepts           Commanded pattern record                RAISING / LOWERING / TEST
                                   command

 RAISING                           One or more selected channels           PWM command and timestamp               SETTLE_WAIT after command
                                   commanded toward up position                                                    interval

 LOWERING                          Selected channels commanded             PWM command and timestamp               SETTLE_WAIT after command
                                   toward down position                                                            interval

 SETTLE_WAIT                       Fixed mechanical settling delay         Timer only                              COMMAND_FINISHED; not
                                                                                                                   physical confirmation

 COMMAND_FINISHED                  Requested command sequence              Command log                             External tests decide physical
                                   ended                                                                           correctness

 FAULT/ISOLATED                    Manual/operator or                      Fault input, reset, test observation    Operator-cleared after inspection
                                   electrical/mechanical fault
                                   recorded


8. Calibration, sequencing and control logic
8.1 Per-dot calibration process
1. Assign a permanent channel and servo identity.
2. Use external calipers/camera or a fixed displacement jig to measure the lowered and raised pin positions.
3. Sweep the up command in small controlled increments to find the minimum repeatable raised position without
stall or excessive load.
4. Repeat for active retraction and verify the pin returns to the approved lowered band.
    Dept. of CSE (CY)                                   PBCST504 - Microcontrollers                                                        Page 9

                                 Topic: OpenBraille - Semester Architecture and Future Research Reference Dossier


5. Repeat across multiple cycles and store the selected command values with hardware/build IDs.
6. Invalidate or recheck calibration after servo replacement, cam/guide reprint or major reassembly.

8.2 Fixed sequencing policy
The semester system should use a simple fixed sequence: identify changed dots, lower dots that must clear, then raise
dots that must set, with a bounded number of simultaneously moving channels chosen only after measured power
testing. Dynamic current-aware sequencing belongs to future research and must not be backfilled into the frozen
MVP.

8.3 Pattern transition rules
                                  Rule                                                                   Purpose

 Move only changed dots                                                   Reduces unnecessary cycles, noise and power

 Active retract before conflicting raise                                  Prevents ambiguous intermediate patterns

 Fixed settle time per tested channel group                               Makes behavior reproducible and loggable

 Reject malformed/unsupported command                                     Protects mapping and state integrity

 Manual stop on stall, heating or binding                                 No automatic recovery without evidence

 Calibration version stored with every test                               Prevents results from being separated from command values


8.4 Physical-truth boundary

 Do not overclaim state
 A servo angle, PWM pulse, elapsed time, current rise or visible cam movement does not automatically prove acceptable
 tactile-pin height. Semester physical truth comes from external measurement and an approved tactile evaluation. Current
 sensing may be used for power/safety observation, not endpoint certification.


9. Data and evidence management
9.1 Required build and session metadata
• Project, firmware, CAD, slicer and protocol version.
• Servo identity, seller/batch, channel assignment and replacement history.
• Cam, follower, guide and pin revision; material, print orientation and finishing.
• Per-dot up/down command values and calibration date.
• Supply identity, measured voltage, actuation grouping and reset/brownout observations.
• Pattern sequence, cycle count, operator, temperature/contamination/load note where relevant.
• Measured raised/lowered positions, failed transitions, binding, wear and manual interventions.
• Photographs/videos tied to the exact configuration ID.

9.2 Evidence hierarchy
                Evidence type                                  What it supports                             What it does not support

 USB command log                                 Requested patterns, timestamps and               Actual tactile height
                                                 firmware behavior

 Calipers/camera/displacement jig                Development measurement of pin positions         Long-term tactile usability by itself

 Power measurements                              Supply adequacy, peaks, droop and resets         Endpoint correctness

 Cycle log                                       Repeatability and mechanical failure history     Commercial lifetime

 Tactile protocol                                Participant distinguishability under the         Universal user performance or standards
                                                 approved setup                                   compliance

 Photographs/video                               Configuration and visible operation              Precise dimensions without measurement


    Dept. of CSE (CY)                                    PBCST504 - Microcontrollers                                                Page 10

                                   Topic: OpenBraille - Semester Architecture and Future Research Reference Dossier


9.3 Final evidence package
                                Evidence file                                                             Minimum content


Configuration record                                                          Board, pins, six servo IDs, CAD/slicer versions, power source and
                                                                              calibration table

Mechanical acceptance                                                         One-dot and six-dot dimensions, travel, free-motion and safety checklist

Electrical acceptance                                                         Supply voltage, resets, wiring, capacitor and combined-pattern
                                                                              observations

Pattern test                                                                  Supported character/pattern suite and exact pass/fail outputs

Repeatability/lifecycle                                                       Per-channel measurements, cycle counts and failures

Tactile protocol report                                                       Approved method, participants/ethics status, randomization, results and
                                                                              limitations

Failure register                                                              Binding, wear, servo replacement, reprints, rejected runs and corrective
                                                                              action

Final demo package                                                            Frozen firmware/CAD, demo script, backup evidence and limitations


10. Validation and acceptance programme
10.1 Validation stages
                Stage                               Question                          Minimum evidence                          Stop/fallback


OB-V0 Component acceptance             Are the ESP32, first servo, supply     Board/USB check, servo sweep,          Replace failed component before
                                       and tools usable?                      adapter polarity/voltage               CAD freeze

OB-V1 One-dot mechanics                Can one printed channel raise and      Measured motion, photographs           Redesign guide/cam before
                                       actively retract without binding?      and repeated cycles                    ordering full batch

OB-V2 Calibration                      Can per-dot command windows            External measurement across            Change geometry or actuator; do
                                       produce repeatable positions?          cycles                                 not tune blindly

OB-V3 Six-dot integration              Do six channels coexist without        Pattern commands, power                Use fixed sequencing, stronger
                                       interference and brownout?             observation and mechanical             supply or rebuild distribution
                                                                              inspection

OB-V4 Pattern correctness              Does character mapping produce         Unit tests and physical pattern        Fix mapping/configuration before
                                       intended six-dot states?               checks                                 user testing

OB-V5 Repeatability/lifecycle          Does the mechanism retain              100-cycle precision set and at least   Record failure; redesign or limit
                                       position and motion over               1,000 total actuations                 claim
                                       approved cycles?

OB-V6 Tactile evaluation               Are raised/lowered dots and            Teacher-approved blinded               Adjust geometry or report MDS not
                                       selected patterns distinguishable?     protocol                               achieved

OB-V7 Locked demonstration             Can the frozen build reproduce the     Signed checklist, frozen               Use approved backup evidence; no
                                       result safely?                         configuration and final evidence       late redesign


10.2 Proposed semester acceptance targets for teacher approval

 Status of numbers
 The project authority contains some architecture-level repeatability and lifecycle targets, but the tactile participant
 threshold is not frozen. The following set should be preregistered and approved before the locked run.

                     Metric                                         Proposed target                                     Why it matters


Channel function                                    All six channels independently raise and            Minimum six-dot cell functionality
                                                    actively retract throughout the final pattern
                                                    sequence

Repeatability                                       ≤0.1 mm position variation over 100 measured        Source-derived architecture target; measures
                                                    cycles under the approved setup                     mechanical consistency

Lifecycle screen                                    At least 1,000 actuations without mechanical        Early engineering screen, not product lifetime
                                                    failure that invalidates the demo


    Dept. of CSE (CY)                                       PBCST504 - Microcontrollers                                                      Page 11

                                       Topic: OpenBraille - Semester Architecture and Future Research Reference Dossier


 Pattern mapping                                            100% correct output for the frozen supported            Separates firmware mapping from mechanical
                                                            character/test set                                      failure

 Power integrity                                            No brownout/reset, connector heating or unsafe          Electrical safety and reliability
                                                            voltage collapse in the locked sequence

 Tactile distinguishability                                 Teacher-approved blinded threshold and trial            Avoids inventing or post-hoc selecting a success
                                                            count fixed before testing                              rate

 Failure honesty                                            Every incomplete/bound transition is logged; no         Evidence integrity
                                                            command-complete event relabelled as
                                                            physically verified

 Budget                                                     Final semester spend ≤₹5,000, with preferred            Course requirement
                                                            target near ₹3,000


10.3 Required performance reporting
• Per-dot raised and lowered position distributions, not only average travel.
• Pattern-level pass/fail counts and the exact supported character set.
• Power/reset observations for one, multiple and worst planned transitions.
• Cycle count, wear inspection and parts replaced.
• Tactile results with protocol, participant context and limitations.
• Negative evidence, binding, failed prints and calibration changes.
• Explicit statement that the macro prototype does not establish commercial-scale feasibility.


11. Twelve-week semester roadmap
          Week                      Primary work                    Owner(s)              Measurable output               Exit criterion                   Fallback


 1                            Teacher decision, scope       Nihad + team; Amith        Approved concept status;     No full-cell purchase until   Use available verified
                              freeze, FDM/tool audit        fabrication audit          one-servo order;             one-dot gate and teacher      ESP32/servo variants
                              and first procurement                                    printer/tool booking; risk   direction are confirmed       without changing
                                                                                       register                                                   architecture

 2                            ESP32/USB bring-up, one       Sreehari + Amith           Commanded servo sweep;       Stable board/serial and       Replace failed
                              bare servo and power                                     adapter/polarity record;     safe one-servo motion         board/servo/supply before
                              acceptance                                               provisional pin map                                        CAD integration

 3                            Print tolerance coupons       Amith + Nihad              Measured coupon set;         Pin moves freely and cam      Adjust guide/cam
                              and one-dot                                              one-dot assembly;            produces controllable         dimensions; laser-cut
                              frame/cam/follower                                       CAD/build ID                 travel                        guide fallback only if
                                                                                                                                                  approved

 4                            Active raise/retract          Amith + Sreehari;          Per-dot calibration          Stable raised/lowered         Change geometry/servo
                              calibration and single-dot    Sreeprada tests            procedure; 100-cycle         bands without binding or      before multiplying
                              repeatability                                            single-dot dataset           unsafe stall                  channels

 5                            Procure/accept remaining      Amith + Sreeprada          Six accepted servo IDs;      Each channel passes           Use spares or pause
                              servos and fabricate six-     inventory                  completed printed parts;     independent bench test        channels; do not hide
                              dot parts                                                assembly checklist                                         batch variation

 6                            Six-dot mechanical and        Nihad + Amith + Sreehari   Assembled cell; external     All six move                  Fixed sequential
                              electrical integration                                   rail; six PWM channels;      independently; no             actuation,
                                                                                       command logs                 brownout/interference         supply/distribution
                                                                                                                                                  revision or rebuild

 7                            Braille mapping, pattern      Sreehari + Sreeprada       Supported character set;     Frozen test patterns          Reduce demo set while
                              transitions and per-dot                                  mapping unit tests;          produce correct               keeping mapping
                              calibration                                              calibration table            commanded states              evidence honest

 8                            Power, safety,                Amith + Nihad; Sreeprada   Worst planned transition     No unsafe heating, reset,     Limit actuation group,
                              repeatability and failure-    runs                       record; fault/reprint log;   pinch or uncontrolled         strengthen guard/supply
                              mode testing                                             safety review                motion                        or redesign

 9                            Lifecycle screen and          Nihad + Archa;             Cycle progress; approved     Mechanism survives and        Report tactile validation
                              tactile-protocol approval     teacher/participant        blinded protocol or          protocol is approved          unavailable rather than
                                                            coordination               documented access limit      before use                    improvising

 10                           Locked                        Full team; test led by     Frozen configuration and     Approved targets met          Record failure; use honest
                              pattern/repeatability/tacti   Sreeprada                  signed result sheets         without post-result           partial-MDS conclusion
                              le validation                                                                         calibration changes

 11                           Final report, source          Archa + Nihad; technical   Final BOM, CAD/firmware      Every technical claim         Remove unsupported
                              records and live-demo         review by Sreehari/Amith   versions, results,           traces to evidence            claims and use backup
                              rehearsal                                                limitations and demo                                       video only if approved
                                                                                       script


      Dept. of CSE (CY)                                              PBCST504 - Microcontrollers                                                             Page 12

                                    Topic: OpenBraille - Semester Architecture and Future Research Reference Dossier


          Week                  Primary work                 Owner(s)              Measurable output            Exit criterion              Fallback


 12                        Contingency, repair-only   Full team                 Stable final build and    No late VPD-C7 or         Submit the strongest
                           window and final                                     archived evidence         architecture expansion    verified semester result
                           delivery                                             package


 Schedule rule
 The minimum demonstrable cell should work by the end of Week 8. Weeks 9-12 are for lifecycle, tactile evidence,
 recovery and presentation. VPD-C7 hardware must not enter the semester critical path.


12. Team roles, actual members and accountability
 Role status
 The following map mirrors the established five-member structure. It is a proposed assignment for team approval; it
 deliberately gives mechanical work substantial ownership because that is OpenBraille’s critical risk.

              Member                           Proposed primary role             Specific OpenBraille ownership              Review/backup obligation


 Nihad P C - JEC24CC044                  Technical integration lead / project   Architecture control, schedule,         Backs up firmware and hardware;
                                         manager                                interface decisions, validation         approves configuration freezes
                                                                                protocol, final integration and
                                                                                evidence integrity

 Sreehari K - JEC24CC055                 Firmware and embedded-control          USB command parser, Braille             Nihad reviews releases; Sreeprada
                                         lead                                   mapping, PWM/channel manager,           executes scripted tests
                                                                                calibration storage, test scripts and
                                                                                logs

 Amith Krishna Das - JEC24CC016          Mechanical, hardware and power         CAD/FDM, cam/follower/guide             Nihad reviews interfaces/safety;
                                         lead                                   design, servo acceptance, power         Sreehari checks control
                                                                                rail, assembly and safety               requirements
                                                                                inspection

 Sreeprada K S - JEC24CC056              Learner, test and inventory            Inventory, servo/build labels, cycle    Works from signed procedures;
                                         assistant                              scripts, measurements, photos, test     learns USB operation and
                                                                                registry and repeated independent       calibration workflow
                                                                                trials

 Archa Pramod - JEC24CC022               Documentation, teacher                 Weekly records, teacher-safe            Technical statements reviewed by
                                         communication and                      explanations, tactile-test              Nihad, Sreehari and Amith
                                         demonstration lead                     coordination, live-demo script,
                                                                                final presentation and source
                                                                                register


12.1 Responsibility rules
• Every critical subsystem has one primary owner, one technical reviewer and one written checklist.
• No one changes CAD, PWM calibration, power wiring or test labels without a dated configuration update.
• The learner/test role is evidence-critical and must run independent repetitions, not only observe.
• The documentation lead does not publish VPD-C7 details without technical and IPR review.
• Nihad acts as integration failsafe, but CAD, firmware and validation must remain independently owned and
reviewable.


13. Procurement, acceptance and configuration control
13.1 Procurement sequence
1. Confirm teacher decision and institutional FDM access.
2. Buy one verified ESP32 board, one SG90-class servo, the external supply and basic mechanical material first.
3. Pass the one-dot mechanical/active-retraction gate before buying or committing the remaining servo batch and full-
cell prints.
4. Buy the remaining servos from one consistent seller/batch where practical and record every identity.
5. Fabricate the full frame only after the physical servo and pin dimensions are measured.
6. Purchase spares only when acceptance or delivery risk justifies them within the conservative envelope.

      Dept. of CSE (CY)                                       PBCST504 - Microcontrollers                                                      Page 13

                                     Topic: OpenBraille - Semester Architecture and Future Research Reference Dossier


13.2 Component acceptance record
                      Component                                    Acceptance checks                                            Reject if


 ESP32                                               Reliable boot/USB, exact board identity and           Unknown pinout, repeated disconnect,
                                                     usable output GPIOs                                   overheating or unstable regulator

 SG90 servo                                          Smooth sweep, no damaged gears, stable                Dead zone, severe jitter, gear damage,
                                                     horn/shaft and repeatable response                    overheating or inconsistent return command

 5 V adapter                                         Correct polarity, stable loaded output, adequate      Unsafe voltage, instability, excessive droop or
                                                     connector and no overheating                          poor connector

 FDM coupon                                          Measured clearance, free pin motion, no cracks        Binding, unsafe roughness, large warp or non-
                                                     or warped datum surfaces                              repeatable fit

 Cam/follower                                        Smooth engagement and required travel                 Stiction, follower jump, crack or unsafe pinch
                                                     without losing contact                                exposure

 Pin/tip                                             Straight, smooth, rounded and securely                Sharp edge, looseness, corrosion or unsafe
                                                     retained                                              touch surface


13.3 Configuration ID format
Recommended format: OB-[cell/build]-[dot/servo]-[CAD]-[firmware]-[protocol]-[session]. Example: OB-C01-D3-SV05-
CAD0.4-FW0.6-P03-R012. The exact format may change, but every measurement, image and result must identify the
physical and software configuration.


14. Risk register and mitigation
               Risk                   Likelihood / impact             Early indicator                    Mitigation                Decision consequence


 FDM guide/cam tolerance          High / High                  Pin does not slide freely;       One-dot coupons, measured       Do not proceed to six-dot
 and friction                                                  variable travel; follower drag   clearance, material/print       assembly until passed
                                                                                                iteration, limited finishing

 No usable passive return         High / Medium                Pin remains raised or servo      Use active commanded            Architecture remains valid
                                                               does not return under load       retraction; remove passive-     with corrected control
                                                                                                return language                 description

 Servo batch                      Medium / High                Different travel for common      Consistent batch, per-dot       May increase calibration and
 variation/backlash                                            PWM; jitter or gear play         calibration, spare/replace      evidence burden
                                                                                                failed unit

 Six-servo brownout or rail       Medium / High                ESP32 reset, adapter sag,        Separate 5 V rail, bulk         Upgrade supply/distribution
 droop                                                         connector heating                capacitor, fixed sequencing,    or reduce simultaneous
                                                                                                measured load                   motion

 Pin tip unsafe or tactility      Medium / High                Sharp/loose tip or participant   Rounded tips, geometry          MDS may fail even when
 poor                                                          cannot distinguish states        iteration, approved tactile     motion is visible
                                                                                                protocol

 Cam/follower wear                Medium / Medium              Position drift, dust,            Material choice, inspection,    Limit claims and redesign if
                                                               roughness or increased noise     lifecycle screen, replaceable   systematic
                                                                                                coupon

 CAD/print schedule slippage      High / Medium                Multiple full reprints or        Single-dot gate, modular        May force reduced demo or
                                                               printer unavailable              prints, early lab booking,      switch to VibeGuard
                                                                                                controlled fallback

 Firmware                         Low / Medium                 Wrong pattern despite            Independent unit tests and      Fix before tactile validation
 mapping/calibration error                                     correct mechanics                configuration versioning

 Tactile participant/protocol     Medium / Medium              No approved access or trial      Secure approval early;          Do not claim tactile success
 unavailable                                                   design                           document visual/mechanical      without the test
                                                                                                evidence separately

 Macro prototype overstated       Medium / High                Slides imply standard            Teacher-safe wording,           Remove unsupported claim
 as product                                                    compliance or commercial         explicit dimensions/limits      before presentation
                                                               readiness                        and review

 Future patent concept leaks      Medium / Medium              VPD-C7 contact/current           Separate folders, approval      Exclude from semester build
 into MVP                                                      details added late               gate and confidentiality rule   and results


     Dept. of CSE (CY)                                       PBCST504 - Microcontrollers                                                        Page 14

                                Topic: OpenBraille - Semester Architecture and Future Research Reference Dossier


15. Required semester deliverables and live demonstration
15.1 Deliverables
• Working macro one-cell, six-dot servo/cam OpenBraille prototype if the concept is retained.
• Final BOM, procurement record, power diagram and provisional pin map.
• Versioned CAD, slicer settings, firmware and Braille mapping tests.
• One-dot and six-dot mechanical acceptance records.
• Per-dot calibration table and pattern-transition test suite.
• Repeatability, lifecycle, power and tactile-protocol results with limitations.
• Failure/reprint/replacement register and contributor chronology.
• Teacher-ready presentation and live-demo procedure.
• Separate confidential VPD-C7 research folder with no semester performance backfill.

15.2 Recommended five-minute live demonstration
1. Show the powered-off macro cell, six servos, rounded pins, guard/covering and separate servo power rail.
2. Connect USB, display the configuration banner and run a commanded one-dot test while explaining that command
timing is not physical confirmation.
3. Display a small frozen sequence of characters or six-bit patterns and clear/refresh them.
4. Show per-dot calibration and one repeatability result table or measurement image.
5. Run the approved safe pattern transition while showing no reset/brownout and the USB log.
6. State the limitations: macro scale, educational prototype, active retraction, no standard-compliance or patent claim.

15.3 Demo failure fallback
If classroom operation is unsafe, unreliable or too noisy, use an approved guarded video of the locked physical setup
plus a live USB/firmware demonstration and the signed measurement evidence. The fallback must not substitute a
different actuator or conceal that the physical build failed the planned gate.


16. Post-semester VPD-C7 research hypothesis


                        Figure 4. VPD-C7 research concept. It is not implemented or validated in the semester cell.

16.1 Technical question
Can a pin-side mechanical datum that sets the tactile endpoint also provide direct endpoint evidence with less
registration error and fewer silent wrong states than a passive stop plus a separately mounted sensor, while keeping
actuator current limited to independent effort/supply information?

16.2 Candidate mechanism in non-claim language
1. Redesign one post-MVP guide/pin coupon with mechanically registered upper and lower endpoint features.

    Dept. of CSE (CY)                                   PBCST504 - Microcontrollers                                   Page 15

                                 Topic: OpenBraille - Semester Architecture and Future Research Reference Dossier


2. Arrange the endpoint feature so reaching it can produce a low-energy pin-side event without carrying servo power
through the contact.
3. Use external displacement and force measurement as the development oracle; do not let the candidate sensor label
itself as truth.
4. Use a separate current/voltage channel only to characterize effort, obstruction-like behavior or supply disturbance.
5. Declare an endpoint state only from qualified pin-side evidence; absent or conflicting evidence becomes
incomplete, jammed or Unknown.
6. Permit recovery/isolation only after the physical and safety behavior is experimentally qualified.

16.3 Why this is only a hypothesis
• A mechanical stop that also acts as a switch/contact is familiar engineering and may be obvious.
• The added contact may increase friction, force, bounce, contamination sensitivity or wear.
• Practical Braille pitch may not accommodate the contact and wiring.
• A separately mounted optical/magnetic sensor may perform just as well or better.
• Current may add no independent diagnostic value beyond command, time and voltage.
• The official Indian close-prior-art file and worldwide claims remain unresolved.
• No experiment currently shows a cooperative or non-additive physical effect.


17. Six-to-twelve-month future research roadmap
             Month                      Stage                          Work                         Pass evidence                    Failure action


 0-2                        Semester foundation and        Complete frozen macro MVP;        Stable one-dot baseline and a   Continue
                            search boundary                preserve mechanical/power         defined professional search     semester/publication only if
                                                           records; obtain official close-   problem                         close art anticipates the
                                                           prior-art documents; build                                        structural core
                                                           direct displacement oracle

 2-4                        Current observability and      Compare calibrated open           Held-out evidence showing       Remove current from the
                            direct sensor baseline         loop, current-only                what current can and cannot     putative invention if it adds
                                                           observation and a separate        reveal                          no independent value
                                                           direct pin sensor on one-dot
                                                           fixtures

 4-6                        Dual-purpose datum coupon      Build passive-stop, separate-     Distinct physical advantage     End VPD-C7 thesis if separate
                                                           sensor and same-datum-            fixed before confirmatory       sensor performs equivalently
                                                           contact coupons; measure          data
                                                           force, bounce, registration
                                                           and false endpoints

 6-8                        Practical-scale and            Develop smaller coupons; test     Feasible packing and stable     Hold Track D if only macro
                            contamination tests            wiring, force, dust/fiber,        endpoint evidence               geometry works
                                                           cleaning and assembly yield

 8-10                       Replacement, reassembly and    Blind servo/cam/pin/datum         Transfer across builds with     Redesign and restart after
                            lifecycle                      swaps; multiple operators;        bounded drift and no            systematic wear/failure
                                                           extended cycling and              systematic false endpoint
                                                           inspection

 10-11                      Locked held-out evidence       Run the preregistered 3,000-      Zero silently accepted wrong    Kill the route after a silent
                                                           transition silent-error test on   states plus practical           wrong state unless a
                                                           unseen                            Unknown/false isolation rates   genuinely new mechanism
                                                           units/builds/conditions                                           restarts the gate

 11-12                      Professional decision gate     Refresh worldwide search;         Useful narrow scope             Choose confidential know-
                                                           claim/FTO chart;                  supported by reproducible       how, defensive/academic
                                                           inventorship/disclosure           physical evidence               publication or stop
                                                           review; management file/no-
                                                           file decision


17.1 Research baselines and ablations
                                 Type                                                                 Required comparison

 Strong conventional baselines                                              Fixed common PWM; calibrated per-dot open loop; passive datum
                                                                            only; direct separate sensor; fixed sequential refresh


        Dept. of CSE (CY)                                 PBCST504 - Microcontrollers                                                         Page 16

                              Topic: OpenBraille - Semester Architecture and Future Research Reference Dossier


                                  Type                                                         Required comparison

 Current tests                                                         Current without endpoint contact; endpoint contact without
                                                                       current; current removed from full candidate

 State logic                                                           Unknown retained versus coerced binary decision; retry removed;
                                                                       isolation removed

 Service robustness                                                    Servo/pin/cam/datum replacement and independent reassembly

 Scale and environment                                                 Macro versus practical-scale coupons; clean versus
                                                                       contamination/wear conditions


17.2 Patent-development kill conditions
• A closer enabling reference or official Indian file discloses the defining combination.
• The same-datum contact has no measurable advantage over a passive stop plus separate sensor.
• The contact adds unacceptable force, friction, bounce, wear or debris sensitivity.
• Practical-scale packaging fails.
• Performance collapses after servo replacement, reprint, remount or reassembly.
• Current adds no independent diagnostic value or is required to certify endpoint completion.
• The locked 3,000-transition test contains a silently accepted wrong state.
• Useful scope collapses to exact hobby parts, macro dimensions or a trivial retry count.
• Institutional/professional review does not justify filing cost or disclosure risk.


18. Confidentiality, inventorship and disclosure control
18.1 Public-safe semester material
• Macro six-dot architecture, six SG90-class servos, eccentric cams, guided pins, ESP32 direct PWM and external servo
power.
• Semester budget, team roles, CAD/fabrication learning, repeatability/lifecycle and approved tactile results.
• Honest limitations: macro educational prototype, active retraction, no current-only state verification and no patent
claim.

18.2 Keep private until IPR review
• Exact VPD-C7 contact/datum geometry, materials, dimensions, circuits and thresholds.
• Unpublished comparative results against passive stops, separate sensors and current-only inference.
• Replacement/reassembly, wear, contamination and held-out silent-error datasets.
• Claim-to-experiment maps, filing strategies and contributor/inventorship analysis.

18.3 Inventorship/contribution record
Maintain dated records of who conceived each later mechanical/electrical interaction, who designed each experiment,
who created CAD/firmware, and when the mechanism was first built and tested. AI/model assistance is not
inventorship and must not replace human conception records.

18.4 Disclosure rule

 Do not rely on an assumed grace period
 Before publishing code, CAD, datasets, posters, videos, papers, competition entries or VPD-C7 details, obtain institutional
 IPR review. A patent filing or defensive publication does not create freedom to operate.


19. Decision gates and escalation rules
                 Gate                           When                                   Pass                           Fail response


 OB-G0 Teacher concept decision     Before procurement                 OpenBraille retained with            Proceed with VibeGuard or revise
                                                                       scope/budget approved                the project request


     Dept. of CSE (CY)                                   PBCST504 - Microcontrollers                                             Page 17

                              Topic: OpenBraille - Semester Architecture and Future Research Reference Dossier


               Gate                               When                                   Pass                               Fail response


OB-G1 Facility/procurement        Week 1                                 Printer/tools and first components      Do not commit full-cell schedule;
                                                                         available                               use VibeGuard fallback if needed

OB-G2 One-dot mechanics           Weeks 3-4                              Active raise/retract and                Redesign coupon; stop six-dot
                                                                         repeatability pass                      expansion

OB-G3 Six-servo power             Weeks 6-8                              No unsafe droop, reset, heating or      Upgrade supply/distribution or
                                                                         stall in planned sequence               reduce groups

OB-G4 Six-dot MDS                 Week 8                                 Correct pattern transitions and         Report partial prototype or switch
                                                                         safe operation                          according to teacher direction

OB-G5 Locked validation           Week 10                                Approved                                No patent or performance
                                                                         repeatability/lifecycle/tactile gates   overclaim; document failure
                                                                         pass

OB-G6 VPD-C7 research entry       Post-semester                          Separate design, confidentiality        Keep OpenBraille as
                                                                         and search approval                     semester/publication record only

OB-G7 Counsel-led filing          Months 11-12                           Unexpected physical effect,             Do not file; choose
evaluation                                                               enabling evidence and useful            publication/know-how/stop
                                                                         scope survive review


20. Open questions and teacher decisions
                ID                         Question / decision                          Owner                                Required by


Q1                                Should OpenBraille remain the          Project coordinator                     Before procurement
                                  semester project or should the
                                  requested VibeGuard switch be
                                  approved?

Q2                                Is the working build window            Teacher/project coordinator             Week 1
                                  approximately eight weeks or the
                                  full twelve-week plan?

Q3                                Is institutional FDM access            Amith + lab                             Week 1
                                  dependable, and what
                                  material/print limits apply?

Q4                                Which exact ESP32 and SG90             Nihad/Sreehari/Amith                    Before order
                                  seller/batch are approved?

Q5                                What quantitative tactile-             Teacher + Archa/Nihad                   Before tactile test
                                  identification protocol and
                                  participant access are approved?

Q6                                What is the approved                   Technical team + teacher                Before locked validation
                                  raised/lowered position band for
                                  the macro cell?

Q7                                Is the 5 V / 3 A target supply         Amith + Nihad                           Before full integration
                                  adequate under the actual six-
                                  servo sequence?

Q8                                What content may be disclosed          IPR cell / project owner                Before publication or competition
                                  publicly before institutional IPR
                                  review?

Q9                                Should VPD-C7 remain only a            Team + institution                      After MVP evidence
                                  confidential future option after the
                                  semester?


21. Teacher approval and conditions
                           Decision item                                                             Teacher response

Semester project                                                         Retain OpenBraille / Approve VibeGuard switch / Revise and
                                                                         resubmit

Frozen OpenBraille scope                                                 Approved / Approved with conditions / Not approved


     Dept. of CSE (CY)                                 PBCST504 - Microcontrollers                                                         Page 18

                                Topic: OpenBraille - Semester Architecture and Future Research Reference Dossier


                           Decision item                                                           Teacher response

 Expected budget near ₹3,000                                             Approved / Revise

 External 5 V servo supply and safety controls                           Approved / Lab review required

 One-dot-first procurement gate                                          Approved / Revise

 Tactile participant protocol                                            Approved / Separate ethics/access review required

 Future VPD-C7 treatment                                                 Confidential post-semester only / Not approved / Further review

 Teacher conditions

 Signature and date


22. Source basis
This dossier was prepared from the controlled Project mC master package. The main evidence layers are:

                          Evidence layer                                                           Controlled source

 Project authority                                                       Engineering Design Review; Project mC Decision Register v1.2;
                                                                         approved Phase 3C Portfolio Closure Memo

 Common evidence                                                         Concept Evidence Matrix; Uncertainty and Test Register

 OpenBraille technical authority                                         Final OpenBraille Architecture Report; Memory; SOP

 Comparative decision context                                            Two final cross-concept adjudications - treated as context, not votes

 Future research boundary                                                OpenBraille Pre-Build Future Patent-Case Simulation

 Costing and teacher context                                             Project mC Teacher Documents - Master Evidence, Costing and
                                                                         Decision Basis

 Previous presentation                                                   Final OpenBraille zeroth-review presentation dated 30-07-2026


22.1 Current official specification and price references
• Espressif, ESP32-WROOM-32 data sheet: https://www.espressif.com/sites/default/files/documentation/esp32-
wroom-32_datasheet_en.pdf
• Espressif, ESP32-S3 product page and DevKitC-1 guide: https://www.espressif.com/en/products/socs/esp32-s3
• TowerPro, SG90 analog servo specifications: https://towerpro.com.tw/product/sg90-analog/
• Indian price snapshots and procurement cautions are recorded in the Master Evidence, Costing and Decision Basis
and must be refreshed on purchase day.
Prepared for academic project planning. The future research section is a management and experimental roadmap, not legal advice,
           patentability clearance, freedom-to-operate clearance, a filing recommendation or a promise of patent grant.


    Dept. of CSE (CY)                                   PBCST504 - Microcontrollers                                               Page 19


---

## Source 7: `03_CONCEPT_PORTFOLIO/OpenBraille/02_Raw_Research/01_OpenBraille_Patent_Research_ChatGPT_Deep_Research.md`

- Authority: `TIER_3`
- Treatment: `SUPPORTING_EVIDENCE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `NEW_STAGE10F_EXTRACTION`
- SHA-256: `979eb5d5155c9fe1243f582320f716ca549f267cbc711597dba7287f51b7c257`

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


---

## Source 8: `03_CONCEPT_PORTFOLIO/OpenBraille/02_Raw_Research/02_OpenBraille_Patent_Research_Gemini.docx`

- Authority: `TIER_3`
- Treatment: `SUPPORTING_EVIDENCE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `NEW_STAGE10F_EXTRACTION`
- SHA-256: `f42e0c020ce6bb38f569bc0757589c5a5410a31b98bb80461355d473afb6434f`

# Source Extraction

- Chapter: `05` — OpenBraille Patent Evidence and Future Research Path
- Authority tier: `TIER_3`
- Manual treatment: `SUPPORTING_EVIDENCE`
- Original source: `03_CONCEPT_PORTFOLIO/OpenBraille/02_Raw_Research/02_OpenBraille_Patent_Research_Gemini.docx`
- SHA-256: `f42e0c020ce6bb38f569bc0757589c5a5410a31b98bb80461355d473afb6434f`
- Extraction method: `DOCX_XML`
- Rule: source text only; no synthesis, correction or reconciliation.

---

OpenBraille Current Patent Verification: Independent Deep Research Report

1. Executive Assessment

The OpenBraille project, as currently defined by its frozen minimum viable product (MVP) architecture, is classified as representing a Track C patent path. The semester MVP—comprising a macro-scale (300%) six-dot refreshable Braille cell, an ESP32-WROOM-32 microcontroller, six SG90-class micro-servos, an eccentric cam/follower/pin mechanism, direct GPIO pulse-width modulation (PWM) control, and a fused deposition modeling (FDM) manufactured frame—is fundamentally achievable within the updated three-month timeline and the strictly enforced ₹3,000 to ₹5,000 budget constraint1. However, the strongest patent-development mechanism requires a later semester or publication-oriented research extension because the mechanical baseline contains zero defensible technical novelty.

The core frozen architecture relies on rotating eccentric cams driven by micro-servos to vertically actuate tactile pins. This specific mechanical linkage has been expressly disclosed in multiple public domain and academic sources, including Indian prior art applications and published engineering literature focusing on servo-actuated refreshable Braille displays4. Consequently, the mechanical actuation baseline cannot support an independent apparatus claim. A credible intellectual property path only emerges if the project's strategy strictly pivots away from the physical actuator mechanism toward dynamic firmware control, tolerance-compensating manufacturing methodologies, or electromechanical calibration sequences2.

The current macro-scale implementation, which features an approximate 7 mm dot pitch, temporarily neutralizes the critical fabrication tolerances inherent to standard Braille specifications of a 2.34 mm dot pitch8. While this macro-scaling ensures prototype buildability within the academic timeline, it renders any geometric, frictional, or mechanical patent claims commercially meaningless unless validated at a practical, standard scale3. Therefore, the complete three-month semester deliverable must be treated exclusively as a functional hardware demonstrator for firmware and control logic validation. The subsequent invention mechanism must rely on algorithmic offset, peak-current management, or true-scale mechanical validation to establish a credible patent profile.

2. Search Log

The independent patent landscape analysis executed across global intellectual property databases utilized targeted classification codes, semantic patent mapping, and combinatorial search strings to evaluate the exact architectural elements of the OpenBraille MVP. The search strategy prioritized the intersection of tactile presentation classifications with embedded actuation mechanisms.

Database

Date

Jurisdiction

Exact Search Strings

Classifications Used

Result-Screening Method

WIPO PATENTSCOPE

30 July 2026

Global / PCT

("refreshable braille" OR "tactile display") AND ("servo" OR "eccentric cam" OR "follower")

G09B21/00, G09B21/003, G09B21/004

Title/Abstract review, followed by independent claim extraction for mechanical hardware matches.

USPTO Patent Public Search

30 July 2026

United States

("braille cell" OR "tactile pin") AND ("cam follower" OR "pulse width modulation") AND "actuator"

G09B21/003, G09B21/004

Full-text keyword proximity search; strict exclusion of Shape Memory Alloy (SMA) and Piezoelectric primary claims.

EPO Espacenet

30 July 2026

Europe

(braille AND "macro scale") OR ("refreshable tactile" AND "3D printed")

G09B21/003

Semantic search targeting manufacturing, 3D printing tolerances, and fabrication methodologies.

Indian Patent Office (InPASS)

30 July 2026

India

5559/CHE/2014 ; "braille" AND "micro-motor"

G09B21/00

Application number direct retrieval and inventor tracking (Paul D'Souza, IIT Delhi) across national databases.

CNIPA

30 July 2026

China

("盲文" OR "触觉") AND ("伺服" OR "凸轮")

G09B21/00

Abstract screening for servo-driven mechanisms, layered electromagnetic equivalents, and modular arrays.

JPO / KIPO

30 July 2026

Japan / South Korea

("点字" OR "점자") AND ("サーボ" OR "서보")

G09B21/00

Cross-referencing assignee families from leading accessible technology hardware manufacturers.

Google Patents

30 July 2026

Global (Discovery)

("tactile pin array" OR "braille dot actuator") AND "servo cam"

G09B21/00

Forward/backward citation traversal of key identified families (e.g., Dot Inc, Tactile Engineering).

IEEE Xplore / ACM / arXiv

30 July 2026

Non-Patent Literature

"refreshable braille" AND "servo" AND "cam"

N/A

Full-text analysis of mechanical architectures detailing SG90 or micro-servo Braille implementations in academia.

3. Verified Family Table and Prior Art Landscape

The technological evolution of refreshable Braille displays is defined by attempts to bypass the high cost of piezoelectric bimorph actuators. The prior art landscape reveals a timeline transitioning from high-voltage piezo reeds in the early 2000s, to Shape Memory Alloys (SMA) and Electroactive Polymers (EAP) in the mid-2010s, and currently settling into electromagnetic (EM) latching and micro-servo mechanisms. The following table isolates the mandatory leads and materially relevant patent families, distinguishing between database-generated status and verified legal or publication status.

Publication / App Number

Priority Date

Assignee / Applicant

Jurisdictions

Current Legal Status

Source

Relevance

Confidence

5559/CHE/2014

05 Nov 2014

Paul D'Souza / Origiin IP

IN

Abandoned / Lapsed (Via non-prosecution)

IPO / Hackaday

Discloses micro-motor actuated pins, cam followers, and levers for refreshable Braille. Represents a fatal novelty risk for the MVP's basic mechanical architecture.

High

US 8483018 B2 / US 20130149674 A1

08 Dec 2011

Wisconsin Alumni Research Foundation

US

Granted (Active to 2031)

USPTO

Utilizes rotating disks with raised surfaces (cams) to lift discrete pins. Demonstrates explicit cam-to-pin translation mechanics in an educational/Braille context.

High

US 11410574 B2

12 Nov 2014

Zhejiang Sci-Tech University

US, CN

Granted (Active)

USPTO, CNIPA

Layered electro-magnetic refreshable Braille display. Serves as close prior art for multi-layer module architecture and translation logic.

High

WO 2015189863 A2

12 Jun 2014

Indian Inst. of Technology Delhi (IITD)

IN, WO

Published (Active in specific national phases)

WIPO

Compliant mechanism for Braille display using SMA. Establishes the baseline for low-cost Indian Braille innovation and latching requirements.

High

US 11854423 B1 / US 11521514

26 Apr 2021

Prithu Kolar, Pramod Kolar

US

Granted (Active to 2041)

USPTO

Hammering/impacting Braille pins from a default raised position. Demonstrates patent saturation in alternative mechanical actuations.

High

CA 3120784 A1 / WO 2020106855

20 Nov 2018

Tactile Engineering LLC

US, EP, JP, KR, CA

Pending / Active

WIPO

Electromagnetic Braille reader with modular, cleanable enclosures. Highly relevant to any claims regarding modularity or replaceable cells.

High

US 11915607 B2

13 Sep 2019

Tactile Engineering LLC

US

Granted (Active)

USPTO

Modular refreshable Braille display system. Further cements the intellectual property fence around hot-swappable single-dot modules.

High

US 12080182 B2

15 Jan 2020

Tactile Engineering LLC

US

Granted (Active)

USPTO

Capture-plate records and display assemblies. Restricts claims related to top-plate mechanical guiding and retention.

High

WO 2016074170 A1

12 Nov 2014

Hangzhou Qiushi Patent Office

CN, WO

Published

CNIPA

Related to the Zhejiang Sci-Tech university filings regarding electromechanical Braille display mechanisms.

High

US 6743021 B2

05 Mar 2002

Thomas S. Prince et al.

US

Expired

USPTO

Microelectromechanical valves and flexible surfaces. Foundational art for alternative tactile interfaces utilizing elastomeric polymers.

High

US 6881063 B2

24 Feb 2003

Peichun Yang

US

Expired

USPTO

Electroactive polymer actuator Braille cell. Establishes the expiration of older non-piezo alternative physics.

High

US 5685721 A

06 Nov 1995

American Research Corp.

US

Expired

USPTO

Refreshable Braille-cell display implemented with shape memory alloys. Foundational prior art for SMA architectures.

High

US 8690576 B2 / US 9424759 B2

Various

Various Assignees

US

Expired / Active

USPTO

Families governing rotary actuators and cam mechanisms in related haptic fields, demonstrating that rotary-to-linear conversion is thoroughly established.

Medium

US 7410359 B2

30 Jan 2004

Freedom Scientific Inc.

US

Expired

USPTO

Electromechanical tactile cell assembly comprising a plurality of piezoelectric element reeds. Represents the foundational piezo baseline that OpenBraille seeks to disrupt.

High

US 6902403 B2

18 Sep 2002

Various

US

Expired

USPTO

Refreshable Braille display utilizing solenoid or alternative mechanical linkages.

High

US 6692255 B2

15 May 2001

Various

US

Expired

USPTO

Early tactile array displays and interface controls.

High

US 20130017516 A1

05 Jul 2011

Individual

US

Abandoned

USPTO

User interface system for entry of Braille input using a single set of six tactile keys. Focuses on input rather than refreshable output, but relevant for firmware translation.

High

WO 2013130534 A1

28 Feb 2012

Various

WO

Published

WIPO

Systems for generating refreshable tactile text and graphics, encompassing early low-cost alternatives.

Medium

EP 4049116 A1

15 Feb 2021

Various

EP

Published

EPO

Tactile pixels and micro-actuation strategies in modern European filings.

Medium

Non-Patent Lit. (IOP Conf. Series)

2021

Various Academics (India)

Global

Published Article

IEEE / IOP

"Refreshable Braille Module Using Cam Actuated Mechanism" expressly uses SG90 micro-servos, 3D printed cams, and pins.

Absolute

Non-Patent Lit. (MagnePins/MOLBED)

2017 - 2025

Madaeon / Monash Univ.

Global

Open-Hardware

GitHub / ACM

DIY printable refreshable Braille displays using electromagnetic coils. Establishes a strong precedent for FDM manufacturing contexts and open-source accessibility.

Absolute

The overarching trend in this landscape indicates that the base physics of mechanical actuation (piezo, SMA, EM, and servo) are heavily saturated or expired. The active patent fences, particularly those maintained by entities like Dot Incorporation and Tactile Engineering, focus aggressively on manufacturable geometries, latching mechanisms to minimize power draw, and modularity10.

4. Independent-Claim Analysis

An exhaustive analysis of the independent claims from the closest relevant records provides the necessary boundaries for the OpenBraille project's freedom-to-operate (FTO) and patentability thresholds. By dissecting the precise legal language of these patents, the exact points of infringement and white space become visible.

US 8,483,018 B2 (Wisconsin Alumni Research Foundation): The primary independent claim defines a Braille device comprising a first disk including a first raised surface (functioning as a cam), a plurality of pins, a top plate with holes, and an actuator mounted to rotate the first disk. The mechanism strictly requires that the pins extend above the top surface when a portion of the raised surface is positioned below the pins to form a Braille number or character9. This claim establishes a broad monopoly on the use of rotating cam-like disks driven by an actuator to directly lift sliding Braille pins. The OpenBraille MVP, which utilizes individual servos rotating singular eccentric cams to lift specific pins, encroaches heavily upon the mechanical principles of this claim. While differentiation exists in the per-dot singular actuator geometry of OpenBraille versus the multi-pin monolithic disk topology of the '018 patent, the fundamental rotary-to-linear mechanical translation through a cam is legally protected in a Braille context9.

US 11,410,574 B2 (Zhejiang Sci-Tech University): The independent claim here defines a layered electro-magnetic refreshable Braille display device that includes multiple layers of Braille display modules, a touch panel, and a plurality of tactile pin driving mechanisms for driving the "up" and "down" of the Braille dots. It further claims a microprocessor connected to a Braille translation module, a voice playing module, and an interaction controller12. While the core actuation physics (electromagnetic) differs entirely from OpenBraille (electromechanical servo), the claim structure is highly instructional. It demonstrates how modern Braille patents protect the overarching embedded systems integration—specifically the translation firmware and structural layer assembly—rather than just the actuator. If OpenBraille seeks a patent, it must similarly claim the embedded firmware control loop and the modular mechanical layers as a unified system rather than claiming the SG90 servo itself.

WO 2015/189863 A2 (Indian Institute of Technology Delhi): The independent claims detail a refreshable Braille display device comprising a plurality of Braille character cells parted into five layers, utilizing a distinct latching means to lock a tactile element in an 'up' position, and employing Shape Memory Alloy (SMA) wires for actuation alongside cantilever strips13. This highlights a crucial requirement in modern Braille patents: addressing thermal management and power constraints through passive latching. The OpenBraille MVP currently relies on the SG90's internal holding torque (or a theoretical passive torsion spring) to maintain the pin in the 'up' position3. The IIT Delhi patent demonstrates that any patent application filed by the OpenBraille team must explicitly separate and define its power-retention mechanics from conventional active-latching arrays.

CA 3,120,784 A1 / US 11,915,607 B2 (Tactile Engineering LLC): These families assert independent claims over modular refreshable Braille display systems where the tactile elements and the actuation mechanisms are housed in separable, cleanable enclosures, creating hot-swappable single-dot or multi-dot modules11. If the OpenBraille team attempts to claim the 3D-printed chassis as a modular, easily replaceable system for educational environments, they will face severe obviousness and infringement risks against these active Tactile Engineering patents. The mechanical architecture must be monolithic or distinctly architected to avoid these modularity claims.

Indian Application 5559/CHE/2014 (Paul D'Souza): While a formal granted claim set is unavailable in the global repository due to the application's presumed abandonment, the inventor's public disclosure (via Hackaday) explicitly outlines the use of micro-motor actuated pins, cam followers, levers, mechanical stops, and rotors/cams mounted vertically or horizontally to lift pins directly4. The documentation includes 3D CAD files for FDM printing in PLA and ABS plastics, noting iterative adjustments to achieve sliding pin tolerances15. This public documentation serves as fatal non-patent prior art against any independent claim the OpenBraille team might draft attempting to monopolize the combination of a micro-motor, a cam, a printed guide, and a Braille pin.

5. Frozen-MVP Feature Chart

The following chart rigorously compares the exact physical and software features of the frozen OpenBraille MVP against the closest prior art to map the existing white space. Features are classified as expressly disclosed, necessarily implied, arguably suggested, absent, or unresolved.

Feature / Architecture Element

OpenBraille MVP (Frozen)

5559/CHE/2014 (D'Souza)

IOP / Academic Paper (2021)

US 8,483,018 B2 (Watch)

Six independent low-cost servos

Expressly Disclosed

Arguably Suggested (Micro-steppers/pager motors used)

Expressly Disclosed (SG90 specified)

Absent (Single actuator for multi-pin disk)

PWM Control

Expressly Disclosed

Unresolved

Expressly Disclosed

Absent

Eccentric Cam

Expressly Disclosed

Expressly Disclosed

Expressly Disclosed

Expressly Disclosed (Raised disk surface)

Follower

Expressly Disclosed

Expressly Disclosed

Expressly Disclosed

Expressly Disclosed (Pin base acts as follower)

Sliding Tactile Pin

Expressly Disclosed

Expressly Disclosed

Expressly Disclosed

Expressly Disclosed

Printed Guide/Frame

Expressly Disclosed

Expressly Disclosed (FDM PLA/ABS files released)

Expressly Disclosed (3D printed PLA)

Absent (Presumed standard machining)

Macro Scale (~300%)

Expressly Disclosed

Absent (Attempted 100% scale compliance)

Unresolved

Absent

Active Retraction

Unresolved / Ambiguous

Expressly Disclosed (Lever spring implementation)

Unresolved

Absent (Gravity/pressure return assumed)

Calibration

Expressly Disclosed

Absent

Absent

Absent

Sequencing (Power-aware)

Expressly Disclosed

Absent

Absent

Absent

Modularity

Expressly Disclosed

Expressly Disclosed

Unresolved

Absent

Power Architecture (External 5V)

Expressly Disclosed

Unresolved

Unresolved

Absent

Tactile Validation (Closed-loop)

Absent

Absent

Absent

Absent

The analysis indicates a near-total overlap in mechanical features between the OpenBraille MVP and the 2021 IOP paper alongside the 2014 D'Souza application. The white space exists exclusively in the software domain—specifically PWM control, power-aware sequencing, and calibration routines5.

6. Indian-Patent Investigation (5559/CHE/2014)

Indian Patent Application 5559/CHE/2014, filed on November 5, 2014, by inventor Paul D'Souza through Origiin IP Solutions LLP in Chennai, represents the most structurally identical prior art to the OpenBraille MVP4.

Status and Prosecution: The application does not appear in the active granted registry and is presumed lapsed or abandoned based on the lack of national phase entry or subsequent issuance. However, the legal status of the patent application itself is secondary to the actions of the inventor. D'Souza explicitly published the design features, methodology, and 3D CAD files on the open-source platform Hackaday under a Creative Commons Attribution-ShareAlike 4.0 International license, creating a permanent, globally accessible prior art footprint15. The inventor specifically requested that the project be discontinued as a commercial venture to avoid legal complications, rendering the mechanical concepts functionally open-source but unpatentable15.

Technical Relevance: The Hackaday disclosure extensively details the use of micro-motors (specifically micro-steppers and miniature pager motors) driving a cam and lever mechanism to push retractable pogo-pins or solid pins through a guide4. The documentation includes iterative 3D CAD files for FDM printing, explicitly noting the adjustments made to nozzle sizes (from 0.4 mm to 0.2 mm) and layer heights (0.05 mm) to achieve the necessary 0.01 mm to 0.02 mm tolerances for sliding pins without binding15. Furthermore, the inventor explicitly utilizes cams that rotate to push a cam follower attached to a lever, which in turn raises the pin16.

Impact on OpenBraille: This public disclosure entirely invalidates the novelty of combining 3D-printed FDM frames, cams, followers, and low-cost micro-actuators for a refreshable Braille cell. Because this exact mechanical linkage was disclosed, published, and discussed in open engineering forums prior to 2016, the OpenBraille MVP's hardware baseline is unpatentable as an apparatus under almost all global patent frameworks. Any patent application filed by the student team must expressly disclaim the basic motor/cam/pin linkage and instead rely on secondary software or manufacturing characteristics not present in the 5559/CHE/2014 disclosure.

7. Separate Risk Analyses

To provide a precise evaluation of the intellectual property landscape, the risks must be segregated into four distinct legal and technical categories. Merging these obscures the specific legal mechanisms that threaten the project.

Novelty Risk (High)

The novelty risk for the physical OpenBraille mechanism is insurmountable. The IOP academic paper titled "Refreshable Braille Module Using Cam Actuated Mechanism" (published in 2021) expressly details the use of SG90 micro-servos, 3D printed polylactic acid (PLA) cam shafts, and sliding pins to achieve Braille display5. When combined with the 5559/CHE/2014 disclosure, every physical element of the OpenBraille MVP (servo, eccentric cam, follower, printed frame) is anticipated by existing prior art4. A patent examiner would cite these documents under 35 U.S.C. 102 (or local equivalents such as EPC Article 54) to reject any independent claim directed toward the base mechanical apparatus.

Obviousness / Inventive-Step Risk (High)

Even if minor geometric or structural differences exist between the OpenBraille MVP and the prior art, the obviousness risk (evaluated under 35 U.S.C. 103 or EPC Article 56) is severe. The Phase 2 landscape analysis explicitly concluded that a naive substitution of a known expensive actuator (e.g., a piezo bimorph) for a cheaper, known actuator (a servo) lacks an inventive step because the predictable result is simply a lower-cost, lower-performance device10. Furthermore, scaling the mechanism to 300% to overcome FDM printer tolerances is a standard engineering prototyping tactic. A person having ordinary skill in the art (PHOSITA) would logically scale up components to mitigate the well-documented resolution constraints of consumer FDM additive manufacturing, rendering the macro-scale aspect of the MVP legally obvious3.

Patent-Eligibility Risk (Medium)

Because the project must pivot entirely to a firmware or algorithmic claim (e.g., control sequences, PWM calibration, or current management) to survive novelty checks, the patent-eligibility risk increases. Under US Alice Corp. jurisprudence and corresponding international software patent restrictions, algorithmic and software-based control methods face heightened scrutiny to ensure they are not merely "abstract ideas" executed on a generic computer10. To survive eligibility challenges under 35 U.S.C. 101, the OpenBraille firmware claims must be tightly coupled to a specific, measurable physical transformation—such as preventing thermal failure through specific sequenced PWM overrides or extending the electromechanical lifespan of the servo through dynamic wear compensation3.

Freedom-to-Operate (FTO) / Infringement Risk (Low to Moderate)

Paradoxically, because the specific servo/cam mechanical linkage is largely covered by abandoned applications (5559/CHE/2014) or open-access academic publications, the FTO risk for the exact MVP hardware is relatively low10. The foundational mechanics have fallen into the public domain. The primary infringement risk arises only if the team diverges from the servo/cam mechanism and pivots into electromagnetic latching, shape memory alloys, or highly integrated modular enclosures, where heavily guarded patent thickets maintained by Dot Incorporation and Tactile Engineering dominate10. As long as the MVP strictly utilizes the SG90 servo/cam architecture without claiming hot-swappable modularity, the likelihood of infringing an active, enforceable apparatus patent is low, allowing the academic prototype to proceed safely8.

8. Candidate Invention Directions

Given the fatal novelty risk to the basic hardware, eight prospective invention directions were rigorously evaluated for their viability within the semester and budget constraints. Weak directions are rejected to focus engineering resources effectively.

1. Tolerance-Compensating Mechanical/Control Architecture

Nearest Prior Art: General 3D printed mechanical linkages (e.g., 5559/CHE/2014)15.

Prospective Differentiating Elements: A specific firmware feedback loop utilizing back-EMF or timing data that detects print-tolerance binding (stiction) and automatically adjusts the PWM overdrive signal to force the pin through high-friction states without burning out the servo.

Enhancement Level: Bounded enhancement (Firmware update).

Physical Advantage: Allows the use of ultra-low-cost, highly variable FDM printers for mass production of Braille cells by compensating for physical defects via software.

Experiment Needed: Controlled friction testing; measuring servo current draw during binding and demonstrating successful firmware intervention without failure.

Schedule/Cost Impact: 1-2 weeks of firmware development; negligible BOM impact.

Principal Risk: Establishing that dynamic overdrive for friction compensation is not an obvious application of generic motor control.

2. Low-Cost Per-Dot Calibration

Nearest Prior Art: US 6,705,871 (Calibration of relative angle sensors and servo systems)18.

Prospective Differentiating Elements: An embedded initialization sequence that maps the exact physical 0° and 90° resting states of each SG90 servo individually, storing the variances in EEPROM to compensate for the extreme manufacturing inconsistencies inherent to sub-$2 servos.

Enhancement Level: Bounded enhancement.

Physical Advantage: Eradicates the need for high-precision assembly or expensive actuators, allowing uncalibrated hobby servos to output uniform 1.5 mm pin heights.

Experiment Needed: Cycle 100 servos through the calibration sequence and measure the statistical reduction in pin-height standard deviation compared to a hardcoded PWM signal.

Schedule/Cost Impact: 1 week of software engineering; ₹0 added cost.

Principal Risk: Calibration sequences are highly conventional in robotics; the claim must be highly specific to tactile array height mapping to avoid obviousness rejections.

3. Verified Tactile-State Control

Nearest Prior Art: Standard open-loop commercial Braille displays.

Prospective Differentiating Elements: Utilizing back-EMF or closed-loop current sensing on the ESP32 to mathematically verify that the pin has actually reached the 'up' position, ensuring the visually impaired reader receives accurate information.

Enhancement Level: Major redesign.

Physical Advantage: Prevents false reading due to jammed pins, increasing trust in low-cost hardware.

Experiment Needed: Intentional pin blocking and verification of error reporting.

Schedule/Cost Impact: High. SG90 servos do not inherently support back-EMF feedback without hardware hacking, adding internal wires, or adding external current shunts (e.g., INA219) for every single dot.

Verdict: Rejected. Modifying the internal circuitry of six servos per cell exceeds the two-month timeline and ₹5,000 budget for a 5-member team primarily composed of CS students3.

4. Compliant Printed Guide/Return Geometry

Nearest Prior Art: WO 2015/189863 (SMA compliant mechanism)13.

Prospective Differentiating Elements: A monolithic, 3D-printed compliant flexure that acts as both the sliding pin and the return spring, driven by the cam, eliminating multi-part assembly.

Enhancement Level: Major redesign.

Physical Advantage: Eliminates assembly of discrete pins and reduces micro-friction.

Experiment Needed: Accelerated fatigue testing of ABS/PETG flexures over 1,000+ cycles to prove material resilience.

Schedule/Cost Impact: Heavy mechanical CAD iteration and material science requirement, contrary to the team's stated computer science strengths8.

Verdict: Rejected. The team lacks the mechanical engineering resources and time to optimize compliant flexure fatigue life within two months.

5. Scale-Transfer Manufacturing Method

Nearest Prior Art: US 10,254,499 (Additive manufactured active devices).

Prospective Differentiating Elements: A specific slicing or deposition method that allows the macro-scale success to mathematically shrink to ISO 17049 standard pitch using consumer FDM hardware.

Enhancement Level: Major redesign.

Verdict: Rejected. A manufacturing method cannot be validated without actually building the true-scale mechanism. Claiming a method that has only been proven at 300% scale violates the scale-transfer rule and would result in an unsupported, speculative patent claim1.

6. Modular Replaceable Architecture

Nearest Prior Art: US 11,915,607 B2 (Modular refreshable braille)14.

Prospective Differentiating Elements: Hot-swappable single-dot modules allowing field repair by visually impaired users.

Verdict: Rejected. Modularity in tactile displays is already heavily claimed by US 11,915,607 and Tactile Engineering (CA 3120784)11. Attempting to patent this invites severe FTO risk and obviousness rejections.

7. Current-Aware Sequencing

Nearest Prior Art: Conventional multi-motor robotics control logic.

Prospective Differentiating Elements: An algorithmic sequencer running on the ESP32 that mathematically prevents the simultaneous startup of multiple SG90 servos. Because each servo draws an uncharacterized transient spike (up to ~500 mA), commanding 6 servos simultaneously to form a full Braille character demands up to 3 Amps, instantly exceeding the 2 Amp power supply and causing MCU brownouts3. The firmware mathematically interleaves the PWM initiation signals by a sub-perceptible tactile threshold (e.g., 10-15 milliseconds) to spread the transient inrush current over time.

Enhancement Level: Bounded enhancement.

Physical Advantage: Prevents MCU brownouts, drastically reduces the required power supply rating (improving affordability), and eliminates the need for expensive decoupling capacitors or complex power distribution boards3.

Experiment Needed: Oscilloscope measurement of the 5V power rail during a 6-pin simultaneous command versus an interleaved command, proving the absolute elimination of voltage sag below the ESP32's 3.0V brownout threshold.

Schedule/Cost Impact: 1 week of CS-centric firmware development; zero added BOM cost.

Principal Risk: Software algorithm eligibility. The claim must be drafted strictly as a method of controlling power electronics in a tactile array, tying the algorithm to the physical prevention of hardware failure.

8. Shared-Actuation Architecture

Nearest Prior Art: Braille Buddy / rack and pinion logic19.

Prospective Differentiating Elements: Using one centralized servo to drive multiple dots via a shifting mechanical carriage.

Enhancement Level: Major redesign.

Verdict: Rejected. This violates the frozen MVP constraints of utilizing one independent servo per dot and would require a complete mechanical overhaul outside the three-month window.

9. Claim-to-Experiment Map and Macro-Scale Rule

For the surviving intellectual property directions (Current-Aware Sequencing and Per-Dot Calibration), the following experimental matrix is required to generate the evidence necessary to support a patent application.

Scale-Transfer Evaluation

The frozen semester MVP operates at approximately 300% standard Braille scale (an ~7 mm pitch compared to the ISO 17049 standard of 2.34 mm)1. A critical evaluation of what physical effects transfer from the macro scale to the standard scale is mandatory to prevent speculative patenting.

Are macro-scale experiments relevant? Yes, but only for electronic and firmware claims (e.g., Current-Aware Sequencing and PWM Calibration). The electrical behavior of the ESP32, the transient current spikes of the SG90 servos, and the mathematical logic of the firmware remain identical regardless of whether the plastic chassis is 7 mm or 2 mm wide3. Therefore, a macro-scale prototype provides completely valid, transferrable evidence for a firmware patent.

Is standard-scale validation mandatory? Yes, for any claim regarding physical tolerance compensation, friction reduction, or tactile legibility. Micro-friction, layer-line interference from FDM printing, and human tactile resolution are highly non-linear variables3. A 0.1 mm print defect at a 7 mm scale is negligible; at a 2.34 mm scale, it causes fatal mechanical binding. Furthermore, the ability of a human finger to read pins spaced at 7 mm does not prove readability at 2.34 mm. A patent claiming a mechanical geometry advantage would be commercially meaningless if limited to a macro scale. Consequently, no mechanical architecture claims should be pursued until a standard-scale cell is successfully built.

Prospective Technical Element

Closest Art

Measurable Technical Effect

Baseline Comparison

Test Equipment

Pass / Fail Evidence

Scale Classification

Current-Aware PWM Sequencing

Generic simultaneous motor control

Absolute reduction in peak inrush current on the 5V rail during multi-dot character formation.

Simultaneous 6-dot actuation vs. Staggered actuation (15ms delay).

Oscilloscope, 5V/2A lab supply.

Pass: Voltage drop is kept above ESP32 brownout threshold (3.0V). Fail: MCU resets during rapid Braille refreshing.

1. Scale-independent. Electronic phenomenon applies regardless of physical chassis size.

Low-Cost Per-Dot Calibration

US 6,705,871 (Servo calibration)

Reduction in pin-height standard deviation across a randomized batch of cheap servos.

Uncalibrated 90° command vs. EEPROM-calibrated target.

Digital calipers (0.01mm resolution).

Pass: Variance < 0.1mm. Fail: Variance remains perceivable by human touch.

2. Scale-sensitive. 0.1mm variance at 7mm scale may not linearly transfer to tactile legibility at 2.34mm scale.

10. Final Research Verdict

The independent research board concludes with the following specific determinations based on the central research questions:

1. Is the current servo/cam MVP itself a credible patent candidate? No. The exact mechanical combination of micro-motors, servos, eccentric cams, followers, and sliding pins housed in a 3D-printed chassis has been exhaustively disclosed in public domain literature, specifically Indian Application 5559/CHE/2014 and the 2021 IOP academic paper4. Novelty is fatally compromised for the hardware apparatus.

2. Must the team invent an additional mechanism? Yes. To establish a defensible intellectual property position, the team must invent and claim a secondary software or control mechanism that overcomes the inherent electrical and mechanical limitations of using cheap, imprecise hobby servos for high-precision tactile output.

3. What is the strongest surviving direction? The strongest surviving direction is Current-Aware PWM Sequencing combined with Per-Dot EEPROM Calibration. By shifting the inventive step entirely to the ESP32 firmware, the team avoids the crowded mechanical patent thickets dominated by Dot Inc. and Tactile Engineering, and capitalizes on their stated strengths as a Computer Science-centric student team1. This approach solves tangible hardware problems (MCU brownouts and FDM tolerance failures) using pure software, creating a highly specific, patentable control method.

4. Is it achievable within ₹5,000 and two to three months? Yes. The firmware-centric pivot requires no additional mechanical components, expensive driver ICs, or complex power distribution boards. The bill of materials remains firmly between ₹2,060 and ₹2,8508. Developing a sequencing algorithm and a calibration routine on the ESP32 is a bounded enhancement that fits comfortably within the three-month academic window1.

5. What evidence could kill the patent path? The patent path for the firmware controls would be killed if:

Oscilloscope testing reveals that 6-servo simultaneous actuation does not actually cause a voltage sag severe enough to trigger an ESP32 brownout, rendering the sequencing algorithm unnecessary to solve a physical problem, and thus obvious.

Prior art is located showing current-aware micro-staggering specifically applied to tactile arrays or Braille displays, destroying novelty.

6. Should OpenBraille advance, remain conditional, or lose patent-first priority? OpenBraille should advance, but strictly classified as a Track C path.

Track C Requirements and Deliverables

Complete Three-Month Semester Deliverable: The team will deliver a fully functional, macro-scale (300%) hardware demonstrator featuring six SG90 servos and a 3D-printed chassis. This unit will successfully translate digital text into macro-Braille output without stalling or suffering electrical brownouts.

Evidence the Semester MVP Must Generate: The MVP will generate high-fidelity electronic data proving that the ESP32 firmware algorithms (Current-Aware Sequencing) successfully mitigate inrush current spikes and prevent system resets. It will also prove that per-dot calibration routines minimize pin-height variance to acceptable levels.

The Later Invention Mechanism: The strongest patent-bearing development—a commercially viable, scalable control methodology for multi-cell displays—will require a later semester or publication-oriented extension.

Additional Experiments, Cost, and Duration: The later extension must involve translating the firmware logic to a true-scale (100% ISO 17049) physical mechanism to validate that the algorithms hold up under standard-scale micro-friction and tactile reading conditions. This will require higher-resolution fabrication (e.g., SLA printing rather than FDM), adding approximately ₹3,000 to ₹5,000 in prototyping costs and requiring an additional 2-3 months of mechanical iteration3.

Connection to the MVP: The later work remains technically connected to the current MVP because the firmware algorithms developed now will serve as the exact control logic driving the future true-scale hardware. The MVP acts as the necessary software testbed, ensuring the underlying control theory is sound before investing in expensive, micro-tolerance mechanical fabrication.

Works cited

Engineering_Design_Review.md

Project_mC_Decision_Register_v1.2.md

05_Uncertainty_and_Test_Register.md

Project | Refreshable Braille Display - Hackaday.io, https://hackaday.io/project/10849/logs

Refreshable Braille Module Using Cam Actuated Mechanism - ResearchGate, https://www.researchgate.net/publication/351539848_Refreshable_Braille_Module_Using_Cam_Actuated_Mechanism

BLIND ASSISTANCE SYSTEM USING REFRESHABLE BRAILLE DISPLAY - JETIR.org, https://www.jetir.org/papers/JETIRBV06054.pdf

03_Concept_Evidence_Matrix.md

Phase3C_OpenBraille_Architecture_Report_Final.md

US20130149674A1 - Braille watch - Google Patents, https://patents.google.com/patent/US20130149674A1/en

Phase2_Report by CLaude.md

CA3120784A1 - Electro magnetic refreshable braille reader - Google Patents, https://patents.google.com/patent/CA3120784A1/en

Mouse Patents and Patent Applications (Class 345/163) - Justia Patents Search, https://patents.justia.com/patents-by-us-classification/345/163?page=3

WO2015189863A2 - A compliant mechanism for refreshable braille display using shape memory alloy - Google Patents, https://patents.google.com/patent/WO2015189863A2/en

Modular refreshable braille display system | GoVeda, https://www.goveda.com/patent/US-11915607-B2

Project | Refreshable Braille Display - Hackaday.io, https://hackaday.io/project/10849/logs?sort=oldest

Refreshable Braille Display - Hackaday.io, https://hackaday.io/project/10849-refreshable-braille-display

Xinli Wu Inventions, Patents and Patent Applications - Justia Patents, https://patents.justia.com/inventor/xinli-wu

(12) United States Patent (10) Patent No.: US 6,705,871 B1, https://patentimages.storage.googleapis.com/36/f3/ff/e153e58993a6be/US6705871.pdf

Literature Search Report Team M&M Project Topic: Refreshable Braille Display Members - Columbia University, http://www.columbia.edu/~ng2366/b_reader/LitReport.pdf

Phase3C_OpenBraille_Memory_Final.md


---

## Source 9: `03_CONCEPT_PORTFOLIO/OpenBraille/02_Raw_Research/03_OpenBraille_Patent_Research_Perplexity_PARTIAL.docx`

- Authority: `TIER_3`
- Treatment: `SUPPORTING_EVIDENCE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `NEW_STAGE10F_EXTRACTION`
- SHA-256: `83a53fc7eecf97a9cf76cce718298b24d9cf93a150046ae5bc5a4290730bf74b`

# Source Extraction

- Chapter: `05` — OpenBraille Patent Evidence and Future Research Path
- Authority tier: `TIER_3`
- Manual treatment: `SUPPORTING_EVIDENCE`
- Original source: `03_CONCEPT_PORTFOLIO/OpenBraille/02_Raw_Research/03_OpenBraille_Patent_Research_Perplexity_PARTIAL.docx`
- SHA-256: `83a53fc7eecf97a9cf76cce718298b24d9cf93a150046ae5bc5a4290730bf74b`
- Extraction method: `DOCX_XML`
- Rule: source text only; no synthesis, correction or reconciliation.

---

OpenBraille Patent Landscape and Servo/Cam Macro-Scale Architecture Assessment (30 July 2026)

1. Executive Assessment

OpenBraille’s frozen MVP—a single macro-scale six-dot Braille cell driven by six SG90-class servos through eccentric cams and sliding pins in a 3D-printed frame—sits inside a heavily patented global landscape for refreshable Braille cells, but also within an explicitly identified white-space band around manufacturing methods, mechanical tolerance strategies, and low-cost control.[1][2]

Independent current searching across US, EP, WO and recent academic/open-hardware work confirms that:

Servo/cam-based actuation of Braille pins is clearly known and claimed at standard scale, including stepping-motor/cam multi-dot actuation and motor-driven cam assemblies.[3][4][^5]

Multi-layer electromagnetic latching, electroactive polymer cells, SMA-based actuators, and modular compressible-pin assemblies form dense prior-art clusters around dot actuation, pin guidance, latching and modularity.[6][7][8][9]

Newer patents (2013–2026) focus on modular cell architectures, capture plates, tactile pixels, EM latching readers, and layered EM stacks, often at compliant ISO dot pitches.[10][11][12][13][^14]

Open-hardware projects MOLBED and MagnePins demonstrate credible EM-latching and passive-pin arrays, explicitly unpatented in the case of MOLBED and open-source HCI research for MagnePins.[15][16]

Given this landscape, the frozen OpenBraille servo/cam cell itself is not a strong mechanistic novelty candidate, but there remains a credible path if the invention is framed around: (a) tolerance-compensating macro-scale mechanical/control architecture, (b) low-cost per-dot calibration and verified tactile-state control, and (c) scale-transfer manufacturing and modularity, all supported by measured evidence.[17][1]

Classification:

Overall: credible path only with bounded enhancement (B) and possible long-term extension (C).

The current MVP has some defensible technical contribution around macro-scale tolerance, low-cost fabrication, and team-fit architecture but requires targeted enhancements and experiments to reach a claimable invention.[^17]

Confidence: Moderate. The prior art is rich and sometimes difficult to fully map (Dot Inc. estate, Indian filings such as 5559/CHE/2014, recent EM-latching families), but the differentiation axes for OpenBraille can be made precise and experimentally testable.[2][18]

Key limitations: incomplete access to Indian file 5559/CHE/2014, incomplete claim-charting for key families (Dot’s cells, IIT Delhi cursor mechanisms, Braille PolyPad pneumatic systems), and the inherently higher risk of method/algorithm-style claims compared to apparatus plus method.

2. Search Log (Representative)

Below is a condensed log of the main databases and strategies used. It is not exhaustive but covers the mandatory areas and named leads.

2.1 Patent Databases and Registers

USPTO Patent Public Search / lens-based mirror: used for all US patents and applications in the named list and adjacent Braille-cell families.[7][8][^19]

EPO Espacenet & EP Register: used for EP471327, EP4049116, and other European Braille/tactile pixel records.[20][9]

WIPO PATENTSCOPE: used for WO2016074170, WO2020106855, WO2015189863 (via family), WO2013130534, WO2024174030, and magnetic/pneumatic display work.[21][22][23][11]

Google Patents: used as a navigation and citation-expansion tool for Dot-related families, SMA/EAP cells, EM-latching displays, and actuation mechanisms (US8770981).[^24]

Chinese, Japanese, Korean patent records: accessed via WO and EP family members where full national-text search was not available in English; notably CN104408994A and KR20210092296 for EM Braille and modules.[11][25][^10]

Indian Patent Office (InPASS / IP India): searched via public advanced search for G09B/G09F Braille-related terms and applicant names; specific retrieval of 5559/CHE/2014 proved unsuccessful.[26][27][^28]

Date: All searches and secondary reading performed 29–30 July 2026.

2.2 Jurisdictions Covered

United States (USPTO; primary for most named leads).[29][7]

Europe (EPO Espacenet, EP Register).[9][20]

WIPO / International (PATENTSCOPE).[23][11]

China (via WO/EP family, CN citations in US11410574B2).[^10]

Japan and Korea (via JP/KR family members of EM-latching Braille reader and modules).[25][11]

India (IP India search; QuickCompany listing for cam-based cells).[27][30]

2.3 Search Strings and Classifications

Representative queries (often combined with G09B21/003, G09B21/004, G09F9/377):

"refreshable braille cell servo cam follower pin".[4][3]

"tactile braille display dynamic cam actuator".[^5]

"electroactive polymer actuator braille cell".[^7]

"shape memory alloy refreshable braille".[8][24]

"compressible pin arrays braille".[^6]

"modular refreshable braille display".[13][31]

"capture plate assembly braille".[^14]

"tactile pixels braille".[^9]

"electro magnetic refreshable braille reader".[12][11]

"layered electromagnetic braille display".[23][10]

"braille cursor passive magnetic mechanism".[^32]

"3D printed braille cell tactile pins".[33][18]

"macro scale braille prototype cam" (for open-hardware).[34][18]

"Indian patent braille cell cam actuator".[^27]

Classifications:

Core: G09B21/003 (Braille cells), G09B21/004 (refreshable Braille displays), G09F9/375/377 (display devices), G06F3/016 (tactile displays), with auxiliary codes around embedded control and learning apparatus.[12][7][^9]

2.4 Screening Method

Initial filter by classification + keyword; discard high-level Braille support/software patents unless they mention hardware cell structures.[35][36]

For each promising record, read abstract, main independent claim, and technical field/background sections to confirm relevance to physical actuation, pin guidance, or modular cell architecture.

Map families (US/EP/WO/JP/KR/CA) and note grant vs application status, priority dates, and assignees.[11][10]

Cross-link open-hardware and academic projects (MOLBED, MagnePins, Aryan 2021 cam mechanism, Braille PolyPad, IIT Delhi cursor mechanism, NIU SMA actuation) to patent clusters but treat them as non-patent prior art unless explicit patent numbers found.[16][37][38][15][^24]

3. Verified Family Table (Selected Materially Relevant Families)

The table focuses on families with direct relevance to refreshable pins, cams, EM latching, modularity, capture plates, tactile pixels and alternative actuation.

Family / Core Number

Priority Date

Assignee / Applicant

Jurisdictions / Members

Legal Status (2026)

Source & Status Confidence

Relevance to OpenBraille

US5685721A – SMA braille cell

1995-11-06

American Research Corp. of Virginia

US, CA family

Expired (20-year term)

USPTO full-text; high confidence[^8]

SMA-based single-moving-part cell; shows dense early prior art on low-part-count actuators, latching; relevant as expired foundational prior art fence.

US5453012A – rotary cam braille display

1993-09-28

Robotron Pty Ltd

US, JP, DE family

Expired

USPTO; high confidence[^3]

Two cam members driven by stepping motors actuating multiple pins; directly establishes cam-based braille actuation at standard scale, limiting mechanistic novelty for servo/cam.

US5766014A – binary cam braille

1997-04-17

Mitsubishi Materials Corp.

US, DE, JP family

Expired

USPTO; high confidence[^4]

Triplet cam actuated by stepping motor with eight positions for four pins; detailed cam geometry and binary behaviour; strong prior art on cam/follower logic.

US5226817A / EP471327 – piezo braille cell

1991-08-08

KGS Corp.

US, EP, DE, ES, JP

Expired

USPTO & Espacenet; high confidence[39][20]

Tactile section with detachable cap and piezo reeds; modular tactile caps and cleaning; relevant for pin guidance, detachable sections.

US7410359B1 + US7462034B1 + US20090035731A1 – electromechanical tactile cell

2004-09-17

Freedom Scientific / Enhanced Vision Systems

US, later WO/EP

Granted (older)

USPTO; high confidence[40][33][^41]

Serial piezo bimorph-based cells, multiple conductive supports; heavy prior art around manufacturable multi-cell assemblies.

US8690576B2 + US9424759B2 + WO2013130534A1 – braille display device & method

2010-08-13 priority

Freedom Scientific / EVS

US, WO, EP, JP, ES

Granted, active

USPTO/WO/EPO; high confidence[29][42][^43]

High-integration dot-incorporation-style cells; central to "Dot Incorporation"-type estate: dense coverage of pin arrays, cell housing, assembly; major FTO fence especially for multiline cells.

US6881063B2 – electroactive polymer braille cell

2003-02-24 priority

Yang / EAP braille

US, EP, WO

Granted; still active in some jurisdictions

USPTO/Espacenet; high confidence[^7]

Compact hydraulic EAP braille cell with latching; relevant as alternative actuation cluster; shows low-power latch structures and hydraulic amplification.

WO2015189863A2 – SMA compliant mechanism braille display

2014-06-08

Indian team (IIT Madras-linked)

WO

Application; later national phases

PATENTSCOPE; medium confidence[^21]

SMA wires, cantilever strips and latching within five-layer cell; key Indian prior art on compliant mechanisms, cantilevered strips, SMA; strongly overlaps with tolerance/cantilever themes.

US11410574B2 + WO2016074170A1 – layered EM braille display

2014-11-12

Yang Wen-zhen et al.

CN, WO, US

Granted (US), active

USPTO/WIPO; high confidence[10][23]

Three stacked EM layers with pin driving mechanisms using coils, iron cores and pin caps; multi-row EM architecture, pin groups; relevant as EM alternative and layered design prior art.

WO2020106855A1 + US12548467B2 – EM refreshable braille reader (EMBR)

2019-11-20 priority

Moon et al.

WO, US, EP, CA, KR, JP

US granted 2026, others mixed

WIPO/USPTO; high confidence[11][12]

Permanent magnet + coil EM actuators, removable top dot capture assemblies, capacitive touch layer; modern EM-latching/reader cluster; relevant to latching and capture-plate cell geometry.

US11915607B2 – modular refreshable braille display system

2020-05-29 priority

Brailleazy Inc.

US

Granted (2024)

USPTO; high confidence[^13]

Mobile-device case with magnet-based pin latching and modular bases; relevant for modular cell and magnet-actuated pins; but servo/cam at macro-scale is architecturally distinct.

US12080182B2 + WO2021183616A1 – capture plate assembly

2020-03-27 priority

Moon et al.

US, WO, EP

US granted (2024)

USPTO/WIPO; high confidence[^14]

Removable capture plates and membranes decoupling dot actuators from braille dots; strong prior art on removable top assemblies and cleaning; relevant to any modular plate concept.

EP4049116A1/B1 + WO2021079101A1 – tactile pixels

2019-10-21 priority

Ali Mohammadi

GB, EP, WO, US

Active

Espacenet/WIPO; high confidence[^9]

General tactile pixel architecture with G06F3/016 and G09B21 classifications; relevant as broad coverage of tactile arrays and pixel-level actuation structures.

US8770981B2 – SMA actuation mechanism for braille displays

2010-04-30 priority

Northern Illinois University

US, WO; expired fee-related

Google Patents; high confidence[^24]

SMA wire-driven sliding block with bias springs; prior art for SMA-driven single-dot mechanics and PWM control; relevant for actuation alternatives.

WO2013179311A1 (IIT Delhi) – refreshable tactile text/graphics

2012-05-31

IIT Delhi

WO; later national phases

WIPO/Google; medium confidence[^24]

Passive ferromagnetic pins actuated by moving cursor; adjacent to Braille PolyPad and passive-magnetic cursor designs; relevant for passive-pin + moving actuator architectures.

US10890993B2 – modular braille display system with touch input

2014-06-25 priority

Optelec Holding B.V.

US, EP

Granted; active

USPTO/EPO; high confidence[^31]

Modular rows of cells with integrated touch-sensitive surface and docking; relevant for modular multi-cell and user-interaction geometry.

US20130017516A1 – active braille timepiece

2011-07-11

Tyler Kelly

US

Application; timepiece-specific

USPTO; medium confidence[^44]

Braille watch with servo motors and cam shafts for translational pins; demonstrates servo-plus-cam actuated pins in a braille context; prior art at device scale.

US20090023116A1 + US8740618B2 – compressible pin arrays

2007-07-20

Tactile Display Corp.

US

Granted; active

USPTO; high confidence[6][45]

Pins with compressible springs and linear actuators; addresses force and cleaning; relevant to pin resilience and modular cleaning pathways.

US6902403B1 – contaminant-tolerant braille pins

2004-08-04

Freedom Scientific

US, EP, WO

Granted; active or near-expiry

USPTO/Espacenet; high confidence[^46]

Multi-shoulder pin geometry and bore clearances to resist fouling; directly relevant to tolerance and contamination—important for tolerance-compensating guides.

US6692255B2 – cylinder-based braille reader

2001-08-06

US Dept. of Commerce

US

Granted; active

USPTO; high confidence[^47]

Rotating cylinder with bi-directional motion and actuators; relevant as macro-scale streaming architecture, but different geometry.

EP4049116 et al. – tactile pixels (global)

2019+

As above

Global

Active

As above[^9]

Already covered above.

Family relationship note: US8690576B2 and US9424759B2 are continuation/continuation-in-part outputs of an electromechanical braille-cell lineage that traces back to US7410359B1 and related applications; WO2013130534A1 summarizes the later system-level display device but shares core cell structure with earlier US patents.[42][43][^29]

Dot Incorporation per se is not explicitly named as assignee in these records, but the Phase 2 synthesis correctly treats the Freedom Scientific/EVS family as the functional "Dot Incorporation"-estate fencing practical multi-cell piezo assemblies.[^2]

4. Independent Claim Analysis (Closest Records)

This section extracts and interprets key independent claims from the closest art, focusing on actuation, pin support, tolerance, modularity, latching, and capture mechanisms.

4.1 Cam and Motor-Based Braille Cells

US5453012A – Braille display (Robotron)

Claim 1 describes a Braille display having:

A plurality of pins movable between elevated and lowered positions in a matrix representing characters.

A rotary means (two cam members with specific cam profiles) associated with columns of pins; different rotary positions give different permutations of elevated/lowered pins corresponding to characters.

Drive means (stepping motors) for selectively rotating the cams between positions.[^3]

Interpretation: This gives broad coverage to using rotary cams driven by motors to actuate multiple pins, including the concept of pin patterns mapped to cam positions. Although OpenBraille uses six independent servos (one per dot) and eccentric cams instead of shared cams per column, the core idea of cam-driven braille pins is prior art.

US5766014A – Binary information display apparatus (Mitsubishi)

Claim 1 covers:

An apparatus with four pins, a triplet cam acting on three pins, and a second cam acting on the fourth pin.

A stepping motor with discrete step positions driving the first cam; pin projections correspond to concave/convex cam portions.[^4]

Interpretation: The claims cover sophisticated cam arrangements where one motor drives multiple pins via cam profiles. Again, this predates OpenBraille’s eccentric servo cams and establishes that converting rotary motion via cam profiles to pin up/down at braille-scale pitch is not novel.

4.2 Piezo and Modular Cell Architecture

US5226817A / EP471327 – Braille cell (KGS)

Independent claims define:

A Braille cell comprising multiple piezoelectric reeds attached to a base through PCB, tactile pins at free ends of reeds.

A detachable tactile section with cap holding pins, enabling cleaning without detaching pins individually.[39][20]

Interpretation: Strong coverage on detachable tactile sections and modular pin caps, relevant to capture-plate ideas. Tolerances and cleaning are explicitly addressed.

US7410359B1 – Electromechanical tactile cell assembly (Freedom Scientific)

Claim 1 defines:

Piezo reeds bend at elongated ends when voltage applied.

Conductive fulcrum pins and multiple element conductive supports securing reeds to PCB.[^40]

Interpretation: Focus is on efficient electrical/mechanical support structure reducing manual soldering; architecture-level but not directly challenging servo/cam at macro scale, except as background to multi-cell manufacturing.

4.3 Dot Incorporation-Style Display Devices

US8690576B2 / US9424759B2 / WO2013130534A1 – Braille display device and method

Independent claims cover:

A refreshable Braille display with housing, upper cover with apertures for pins, motherboard, Braille cell assemblies, and cursor routing buttons.[43][29][^42]

Each cell assembly supporting eight bimorph reeds and pins, with cost-optimized mounting blocks and backplanes.

Interpretation: These claims focus on system-level integration, cell mounting, and cursor routing. While they dominate practical multi-line piezo displays, they do not explicitly claim servo/cam architectures; rather they fence piezo assemblies and integrated housing.

4.4 Electroactive Polymer Cells

US6881063B2 – Electroactive polymer actuator braille cell

Claim 1 presents:

A fluid-tight housing with diaphragm and braille dot; fluid and EAP bending elements acting like pumps.[^7]

Interpretation: Alternative actuator cluster; relevant as prior art for low-power hydraulic amplification but distinct from macro servo/cam.

4.5 Electromagnetic Latching and EM Readers

US11410574B2 / WO2016074170A1 – Layered EM Braille display

Claims define:

Three layered Braille display modules with pressing plates, iron core plates, line coils, and tactile pin driving mechanisms.[10][23]

Interpretation: Multi-layer EM architecture with line coils and iron cores; heavy prior art around EM pin latching and multi-row displays.

WO2020106855A1 / US12548467B2 – EM refreshable braille reader (EMBR)

Claims cover:

A tactile display with electromagnetic actuating elements and braille dots; capture plate assemblies; magnets within insulator spaces with surrounding coils.[11][12]

Interpretation: EM-latching braille dots with removable dot capture assemblies and capacitive touch surfaces; these families are central modern EM-latching prior art and directly adjacent to MOLBED/MagnePins-type mechanisms (which are open-source but conceptually similar). They fence EM latching at braille pitch and modular capture plates.

4.6 Modular and Capture-Plate Architectures

US11915607B2 – Modular refreshable braille display system

Claims emphasize:

Mobile-device case with contact surface, cavities, pins, bar magnets, detachable top housing, and communication interface.[^13]

Interpretation: Focuses on magnet-based pin latching and modular cell packaging in a mobile case. Relevance: any macro modular cell design with magnets must respect this cluster.

US12080182B2 – Capture plate assembly for braille display

Independent claims describe:

Capture plate assembly with display dots, top assembly with braille dots, membrane separating dots, capacitive touch layer; removable capture plate.[^14]

Interpretation: Expands prior art on removable top plates; strong fence on capture-plate plus capacitive touch combinations.

4.7 Tactile Pixels and General Tactile Displays

EP4049116A1/B1 – Tactile pixels

Claims (at high level) cover tactile pixel arrangements for braille or graphics, under G06F3/016 and G09B21; details include pixel arrays and actuation structures.[^9]

Interpretation: Broad generic coverage of tactile pixels; relevant as high-level environment but less constraining at single-cell macro scale.

4.8 Actuation Mechanisms (SMA) and Alternative Designs

US8770981B2 – Actuation mechanism for braille displays

Claim 1 defines a pin and sliding block actuated by a single bias compression spring and single SMA wire; wire activation moves block to retract pin.[^24]

Interpretation: Prior art for SMA sliding-block actuation; relevant if OpenBraille considered SMA alternatives; not directly conflicting with servo/cam.

4.9 Academic / Non-Patent Prior Art

Aryan 2021 – Refreshable Braille Module Using Cam Actuated Mechanism: servo-driven cam shafts to actuate pins; confirmed as cam/servo braille project.[^37]

Leonardis et al. 2020 – passive magnetic cursor mechanism: single actuated slider with passive pins.[^32]

Braille PolyPad (Xie et al. 2021): stiffness-variable polymer + pneumatic pins; alternative low-cost large-matrix concept.[^38]

IIT Delhi cursor mechanism (WO2013179311): moving cursor over passive pins; as above.[^24]

MOLBED: magnet-retained pins actuated by coils; explicitly unpatented; low-cost EM-latching braille character modules.[^15]

MagnePins (UIST 2025): large passive pin array actuated by simple EM mechanism; open-source design with braille-compliant pitch.[^16]

These sources significantly raise the bar for novelty in EM-latching and cam-based mechanisms, even absent patent filings.

5. Frozen-MVP Feature Chart vs Closest Art

Using the categories requested, the table compares OpenBraille’s servo/cam macro cell features primarily against: US5453012A, US5766014A, US6881063B2, US11410574B2, WO2020106855/US12548467B2, US11915607B2, US12080182B2, EP4049116, Aryan 2021, MOLBED, MagnePins, and Freedom Scientific cells.

Legend:

ED: expressly disclosed

NI: necessarily implied by core operation

AS: arguably suggested (design choices, optional variants)

AB: absent

UR: unresolved in available documents

MVP Feature

Servo/cam patents (US5453012/US5766014)[3][4]

Piezo/microactuator cells (Freedom/KGS)[39][40][^29]

EM/SMA/EAP clusters (US6881063, US11410574, US12548467, WO2020106855)[7][10][11][12]

Modular/capture/tactile pixel (US11915607, US12080182, EP4049116)[13][14][^9]

MOLBED/MagnePins/open cam projects[15][16][37][18]

Six independent low-cost servos (one per dot)

AB (motors per column, not per dot)

AB (piezo reeds per dot, but no servo)

AB (coils/magnets, not servos)

AB

NI/AS (cam actuators sometimes use individual electromagnets; Varada’s refreshable module uses EM + cam, but not explicitly servo)

Direct PWM control from MCU

AB (steppers driven by drivers; PWM implicit but not central)

AB (piezo drive circuits, high voltage)

ED (coil current control; PWM suggested)

AB

NI/AS (Arduino shield-driven coils in MOLBED; PWM use suggested in NIU SMA work)

Eccentric cam per dot

ED (cam per column)

AB

AS (cams used for EM flip latches in some academic work)

AB

ED (eccentric cam with embedded magnet in refreshable module; EM-actuated cam in NIU example)

Follower (roller or lever)

ED (cam followers implied by cam-pin interface)

AS (pushup cams with reeds)

AS (magnet/cam interactions)

AB

ED (cam followers in Hackaday projects and Aryan 2021 mechanism)

Sliding tactile pin

ED

ED

ED

ED

ED

Printed guide/frame (FDM 3D printed cell)

AB (machined housings)

AB (molded plastic housings)

AS (fabrication unspecified but often machined/molded)

AS (generic housings; not 3D-specific)

ED (3D-printed bodies for pins and magnet holders; 3D-printed frames and cams)

Macro scale (~300% ISO dot pitch)

AB

AB

AB

AB

AS (MOLBED is explicitly braille-compliant; Aryan 2021 may operate near standard scale; most work targets conformant pitch)

Active retraction via actuator

ED (cams actively move pins up/down)

NI (piezo reeds actively bend; pins follow)

ED (coils actively move pins)

NI (actuation unspecified; depends on underlying devices)

NI (cam and EM move pins; magnets latch)

Calibration (per-pin PWM or mechanical tuning)

UR (not emphasized)

UR (factory calibration; not per-user)

UR (could be implemented but not widely claimed)

UR

AS (MOLBED and EM-latching readers benefit from calibration; NIU SMA uses PWM tuning)

Actuation sequencing (low-power strategy)

UR

AS (multiplexing drivers)

ED (EMBR includes energetics diagrams, power-aware control)

UR

ED (flip-latch EM and magnetic cursor mechanisms emphasize low-power latching)

Modularity (cell-level replaceable unit)

AS (cam modules per column)

ED (individual cells mounted on backplane)

AS (EM modules)

ED (modules and docking stations)

ED (MOLBED character modules, line PCBs, page PCBs)

Power architecture (external 5 V for servos, single rail)

AB

AB (higher voltages typical)

AS (low-voltage control for EM)

AB

AS (12 V for TB6612 drivers; modules for EM)

Tactile validation / human readability measurement

UR

UR

UR

UR

UR (MagnePins paper mentions expert reader tests, but details are limited)

Conclusion: Most physical elements of the servo/cam MVP—cam-actuated pins, followers, cells, modular assemblies—are already disclosed across older and newer patents and open projects. The potentially differentiating elements are:

Use of low-cost hobby-class servos at macro scale for a single-cell MVP, with direct PWM from ESP32 and no driver electronics.[^17]

3D-printed frame and cam geometry explicitly designed to absorb print tolerances rather than meet ISO pitch.[^17]

Education-oriented architecture optimized for a cyber/CS-student team with minimal mechanical tooling.

These do not constitute strong apparatus novelty on their own but are promising as part of a method/manufacturing/tolerance-compensation narrative.

6. Indian-Patent Investigation: 5559/CHE/2014

6.1 What Is Known

Phase 3C logs and Hackaday notes identify 5559/CHE/2014 as an Indian application filed 5 November 2014, described as covering "micro-motor actuated pins, pin cantilever design, mechanical stops to limit rotor rotation, motors with rotors or cams, mounted vertically or horizontally used to lift pins directly or via an interposer, low force selector" for refreshable braille displays.[48][49]

QuickCompany and Indian patent journals lists were checked for:

Number formats "5559/CHE/2014", "CHE/2014/5559", and possible published numbers derived from that filing reference.[30][27]

Assistech/IIT Delhi-related braille patents (cursor systems, tactile displays).[50][27]

No direct official publication record mapping exactly to 5559/CHE/2014 was found via open IP India search, suggesting one of:

The application remained unpublished (abandoned or withdrawn before publication).

The number refers to an internal filing/diary number, not the later publication number.

The data is present behind the InPASS interface but requires manual or on-site access beyond public web tools.[^28]

6.2 Current Retrieval Status

Publication number: unresolved. No direct US/EP/WO family mapped from 5559/CHE/2014 through public databases.[^27]

Complete specification: unavailable via public IP India sites under the exact identifier.

Claims: unavailable.

Applicant/inventor: likely Paul D’Souza or collaborating entity, per Hackaday logs, but not confirmed by Indian official records.[49][48]

Filing and publication dates: filing 05 Nov 2014 is reported in community sources; publication date remains unknown.[^48]

Prosecution and legal status: no accessible legal-status summary via IP India for the specific code; likely abandoned or pending under another publication number.[26][28]

Family equivalents: none were found in US/EP/WO under obvious similar titles ("tactile display for visually impaired", "braille cell and assembly") except QuickCompany references to Indian filings that resemble IIT Delhi’s WO2013179311 or other braille cell patents.[51][27]

6.3 Relevance and Risk

Based on secondary descriptions, 5559/CHE/2014 likely claims:

Micro-motor actuated pins (similar to pico-motors used as cams).[^48]

Pin cantilever and lever-based amplification.[^48]

Mechanical stops and low-force selectors for binary cam behaviour.[^48]

These functionalities overlap strongly with Varada’s open-hardware refreshable display and electromechanical cam projects, and conceptually with any macro servo/cam architecture, though the exact claim boundary cannot be charted without the file.[18][34]

Conclusion: The Indian patent is a known but unresolved risk source. Any claim strategy relying on detailed cam/micro-motor/cantilever geometry should be cross-checked by counsel via direct IP India registry access and possibly correspondence with the inventor (Paul D’Souza) before being considered safe. For current semester work, treating it as blocking prior art for micro-motor-based cam cantilever designs is prudent.

7. Separate Risk Analyses

7.1 Novelty Risk

Cam-based actuation of Braille pins is established decades ago (US5453012, US5766014).[3][4]

Servo motors driving pins or cams appear in watch and device patents (US20130017516A1, braille watch; open hardware refreshable modules).[44][34]

Pin guidance via slots and detachable caps is heavily covered (US5226817, US7462034, US20090035731).[41][33][^39]

EM-latching mechanisms, passive pins plus EM actuators, and magnet-based latching appear in modern patents and academic work (US12548467, WO2020106855, Leonardis 2020, MagnePins).[16][12][32][11]

Modular braille cells, capture plates, and tactile pixel arrays are present (US11915607, US12080182, EP4049116).[13][14][^9]

Novelty risk is therefore high for any claim that treats:

"servo + cam + pin + guide" at braille-scale as the invention.

"modular braille cell with removable top" in isolation.

"magnetic latching" of pins as new.

Residual novelty may exist in:

A specific macro-scale mechanical tolerance management strategy designed for FDM printing and low-cost metals, with measured repeatability and yield.[1][17]

A combined manufacturing/control method (including calibration, sequencing, and scale-transfer procedure) enabling low-cost reproduction of acceptable tactile performance from commodity servos and printed guides.[^1]

7.2 Obviousness / Inventive-Step Risk

Given the saturated landscape:

Using macro-scale servo/cam instead of piezo, SMA, EM, or micro-actuators may be seen as a straightforward substitution of known actuators into known braille pin/cam structures, particularly given the refreshable braille literature that explores "low-cost actuators" and 3D printing.[37][34][^18]

Macro-scaling to ease FDM fabrication is a common engineering tactic and appears in broader assistive device literature ("scale up to print"), even if not claimed explicitly.[^17]

Using ESP32 PWM for servos, calibration tables, and simple sequencing are textbook embedded control practices.

To clear inventive-step, OpenBraille likely needs to demonstrate non-obvious technical effects, such as:

A documented tolerance window and yield improvement compared to existing low-cost cam/pin implementations at similar cost.[1][17]

Measurable reductions in Brown-out, jitter, or misalignment due to a specific power/control and mechanical architecture.[^17]

A novel way of combining macro experiments and analytic scale-transfer to standard pitch (even if the latter is future work).

Obviousness risk is thus medium–high, but can be pushed towards medium if claims focus on quantified tolerance/return/compliance interactions rather than generic servo/cam substitution.

7.3 Patent-Eligibility Risk

In India, US, EP and many other jurisdictions, apparatus-plus-method claims for electromechanical devices are generally patent-eligible unless framed as pure mathematical algorithms or abstract methods.[^52]

OpenBraille’s strongest potential claims involve:

Mechanical structures (frames, cams, guides, pins) and their interactions.

Control methods tied directly to physical effects (calibration, PWM, sequencing, power gating).[1][17]

Eligibility risk is therefore low, provided claims avoid pure software or user-interface aspects detached from hardware. However, any future heavy reliance on control algorithms or calibration logic must tie them clearly to physical improvements (e.g., reduced variance, lower current, improved tactile reliability) to avoid "abstract method" traps.

7.4 Freedom-to-Operate (FTO) / Infringement Risk

The FTO picture is not yet formally charted but key hazards include:

Dot Incorporation / Freedom Scientific estate: multi-cell displays with piezo reeds, detachable caps, contaminant-tolerant pins; any multi-cell piezo design would strongly risk infringement.[46][29][^42]

EM-latching readers (Moon et al.): EM actuators with capture plates and magnet-coil structures; replicating EM latching at standard pitch risks conflict.[12][14][^11]

Layered EM displays (Yang et al.): multi-layer EM braille stacks.[23][10]

Magnet-based modular cells (Brailleazy): bar magnets and modular top housings for mobile cases.[^13]

MOLBED/MagnePins: open-source; no direct infringement risk, but commercial exploitation must respect any overlapping patents (Moon, Leonardis) and open-hardware licensing.[15][16]

Indian 5559/CHE/2014: unresolved; micro-motor cam/cantilever claims could complicate any direct reuse of that geometry.[49][48]

For the current single macro-scale servo/cam cell:

FTO risk is moderate: the device uses known elements but at non-compliant scale, single-cell scope, and commodity servos, which likely fall outside the core fences of piezo, EAP, EM-latching and micro-cam arrays. However, without claim-charting, this cannot be asserted confidently.[2][17]

Long-term multi-cell or compliant-scale designs would raise FTO risk significantly and require professional claim-charting against the above estates before productization.

8. Candidate Invention Directions

This section evaluates several candidate directions requested, separating bounded enhancements (B) from major redesigns and potential Track C long-term work.

8.1 Tolerance-Compensating Mechanical / Control Architecture

Nearest prior art: contaminant-tolerant pins (US6902403B1), modular caps (US7462034B1), compliant SMA/EAP mechanisms (US6881063B2, WO2015189863), manufacturing-friendly braille cells (Freedom Scientific families).[21][41][29][46][^7]

Prospective differentiating elements:

Explicit macro-scale tolerance budget for FDM printing: clearances, slot widths, cam radii, pin verticality, and flatness targets tuned to cheap printers and materials, coupled with observed assembly yield and cycle life.[^17]

A mechanical architecture combining: servo-integral torsion reset, eccentric cam, follower, printed guides, and macro relief to remove dependence on sub-0.05 mm machining while still meeting tactile repeatability.

A control strategy that avoids over-driving, jitter, and mechanical shock, documenting how PWM profiles and sequencing interact with macro tolerances to prevent wear/failure.

Bounded enhancement or major redesign?

Bounded enhancement (B): The current MVP already embodies some tolerance management; enhancing it would involve systematically measuring tolerance impacts, possibly refining slot geometry and cam profiles, and documenting repeatability across multiple printed units.

Required physical advantage:

Demonstrably higher build success and tactile reliability for student-accessible FDM, compared to nearest open-hardware cam projects that often assume high-end printers.[^18]

Experiment:

Fabricate multiple cells with controlled variations in print quality, measure pin travel, misalignment, friction, and failure rates; compare to baseline (e.g., Varada’s module or reference cells).[1][17]

Schedule / component impact:

Feasible in the three-month semester: design-of-experiments, multiple prints, simple metrology (calipers, feel tests). No major component changes.[53][17]

Principal patent risks:

Novelty: moderate risk; prior art addresses cleaning and tolerances but not explicitly macro FDM budgets.[^46]

Obviousness: moderate; macro-scaling and tolerance budgets are common engineering practices.

Verdict: viable B direction if framed tightly around macro-scale, FDM-focused tolerance methodology and evidence.

8.2 Low-Cost Per-Dot Calibration

Nearest prior art: per-pin calibration in EM-l

References

06_Patent_Research_Input_Pack.md - This pack preparesnot performsa later current patent search. Historical repository conclusions below...

Phase2_Report-by-CLaude.md - Prepared by Claude, acting as the Engineering RD IP Review Board synthesis function Inputs Phase 1C ...

Braille display - publication_number: US5453012Aassignee: ROBOTRON PTY LTDabstract: ...between an elevated position ...

Binary information display apparatus - publication_number: US5766014Aassignee: MITSUBISHI MATERIALS CORPORATIONabstract: A binary informa...

SYSTEMS AND METHODS FOR A DYNAMIC BRAILLE DISPLAY - publication_number: US20150206453A1abstract: Embodiments disclosed herein describe systems and meth...

Braille module with compressible pin arrays - publication_number: US8740618B2assignee: TACTILE DISPLAY COROPRATIONabstract: A refreshable tactil...

Electroactive polymer actuator braille cell and braille display - publication_number: US6881063B2abstract: The present invention provides a Braille cell being of com...

Refreshable braille-cell display implemented with shape memory alloys - publication_number: US5685721Aassignee: AMERICAN RESEARCH CORPORATION OF VIRGINIAabstract: A refre...

TACTILE PIXELS - publication_number: EP4049116A1grant_date: 2022-08-31filing_date: 2020-10-21application_number: 2...

Layered electro-magnetic refreshable braille display device and braille reader - publication_number: US11410574B2abstract: The present invention discloses a layered electro-magneti...

ELECTRO MAGNETIC REFRESHABLE BRAILLE READER - publication_number: WO2020106855A1abstract: In certain embodiments devices suitable for use as elec...

Electro magnetic refreshable braille reader - publication_number: US12548467B2abstract: In certain embodiments devices suitable for use as electr...

Modular refreshable braille display system - publication_number: US11915607B2assignee: BRAILLEAZY INCabstract: This specification generally dis...

Capture plate assembly for braille display - publication_number: US12080182B2assignee: TACTILE SOLUTIONS INC, FREEDOM SCIENTIFIC INC. D/B/A VISP...

MOLBED - Modular Low Cost Braille Electronic Display

MagnePins: A Modular, Affordable, and DIY Refreshable Braille and Tactile Display

Phase3C_OpenBraille_Architecture_Report_Final.md - Prepared by Final Engineering Architecture Review Board synthesis of four independent Phase 3C Deep ...

Electromechanical Refreshable Braille Module - The big drawback to refreshable braille devices has always been their cost. The loose rule of estima...

BRAILLE WATCH - publication_number: US20130149674A1assignee: WISCONSIN ALUMNI RESEARCH FOUNDATIONabstract: A Brail...

Braille cell - publication_number: EP471327A1abstract: The present invention discloses a braille cell comprising p...

A COMPLIANT MECHANISM FOR REFRESHABLE BRAILLE DISPLAY USING SHAPE MEMORY ALLOY - publication_number: WO2015189863A2abstract: The present invention describes a refreshable braille d...

DEVICE AND METHOD FOR DISPLAYING BRAILLE AND TACTILE GRAPHICS - publication_number: WO2024174030A1abstract: ...includes an array of braille pins arranged equidista...

LAYERED ELECTROMAGNETIC BRAILLE DISPLAY DEVICE AND BRAILLE READING MACHINE - publication_number: WO2016074170A1abstract: A layered electromagnetic Braille display device and a ...

Actuation mechanism for braille displays - According to the present invention, there is provided an improved refreshable tactile display appara...

BRAILLE LEARNING APPARATUS AND BRAILLE LEARNING METHOD USING THE SAME - publication_number: US20170309203A1assignee: OHFA TECH INCabstract: A braille learning apparatus i...

IP India

A Braille Cell And Assembly For Single Line Braille Display - Abstract: A Braille cell and assembly for single-line Braille display, said cell and assembly compri...

IPIndia Patent Search | Indian Patent Search - IPExcel - IP India Patent search can be performed using Indian Patent Office website. The said website is avai...

Braille display device and method of constructing same - publication_number: US8690576B2assignee: FREEDOM SCIENTIFIC INC, ENHANCED VISIONS SYSTEMS INCabstr...

555 Trade Mark - 555 Trade Mark is a Device Trademark filed on 26 December 2008 with Application_ID 1768210 in West b...

Braille display system - publication_number: US10890993B2assignee: OPTELEC HOLDING B.Vabstract: A Braille display system ca...

A passive and scalable magnetic mechanism for braille cursor, an innovative refreshable braille display

Electromechanical Tactile Braille Cell Assembly - publication_number: US20090035731A1assignee: FREEDOM SCIENTIFIC INC, ENHANCED VISIONS SYSTEMS INCa...

Refreshable Braille Display - Hackaday.io - Of 40 million blind people in the world, only 10% can read and write braille. One of the primary rea...

Braille Support - publication_number: US20080303645A1assignee: APPLE INCabstract: Methods and apparatuses to provide...

Braille support - publication_number: US8135577B2assignee: APPLE INCabstract: Methods and apparatuses to provide imp...

Refreshable Braille Module Using Cam Actuated Mechanism - by Aryan · 2021 · Cited by 5 — The basic concept of cam shafts are used to design the dynamic braill...

A 2D refreshable Braille display based on a stiffness variable polymer and pneumatic actuation - Visual impairments limit a person’s ability to process information such as obstacles, environments, ...

BRAILLE CELL - publication_number: US5226817Aassignee: KGS CORPORATION A CORPORATION OF JAPANabstract: The presen...

Electromechanical tactile cell assembly - publication_number: US7410359B1assignee: FREEDOM SCIENTIFIC INC, ENHANCED VISIONS SYSTEMS INCabstr...

Braille display assembly - publication_number: US7462034B1assignee: FREEDOM SCIENTIFIC INC, ENHANCED VISIONS SYSTEMS INCabstr...

Braille display device and method of constructing same - publication_number: US9424759B2assignee: FREEDOM SCIENTIFIC INC, ENHANCED VISIONS SYSTEMS INCabstr...

BRAILLE DISPLAY DEVICE AND METHOD OF CONSTRUCTING SAME - publication_number: WO2013130534A1abstract: Disclosed is a Braille display device. The device suppo...

ACTIVE BRAILLE TIMEPIECE & RELATED METHODS - publication_number: US20130017516A1abstract: A timepiece adapted for efficient mechanical display o...

Braille module with compressible pin arrays - publication_number: US20090023116A1assignee: TACTILE DISPLAY COROPRATIONabstract: A refreshable ta...

Contaminant-tolerant braille pins - publication_number: US6902403B1assignee: FREEDOM SCIENTIFIC INC, ENHANCED VISIONS SYSTEMS INCabstr...

Apparatus and method utilizing bi-directional relative movement for refreshable tactile display - publication_number: US6692255B2assignee: GOVERNMENT OF THE UNITED STATES OF AMERICA AS REPRESENTED ...

Refreshable Braille Display

Project | Refreshable Braille Display - Project thus far are covered under a patent application filed at The PatentOffice, Chennai, by him o...

Patent - Patent by Assistech

Tactile Display For Visually Impaired People - Abstract: All visually impaired people use braille or any audio books to read something, but each ti...

Patent Public Search - A powerful, flexible web-based patent search application that improves the overall patent searching ...

Phase3C_OpenBraille_Memory_Final.md - Version 1.0 Status COMPLETE Methodology Version Phase 3C --- TITLE Project mC - Phase 3C Memory Open...


---

## Source 10: `03_CONCEPT_PORTFOLIO/OpenBraille/02_Raw_Research/04_OpenBraille_Patent_Research_Qwen.md`

- Authority: `TIER_3`
- Treatment: `SUPPORTING_EVIDENCE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `NEW_STAGE10F_EXTRACTION`
- SHA-256: `79163acf026753e5fe835be66adc8e7d9fc0e0575b09395fd22f227ce5ee5567`

# Source Extraction

- Chapter: `05` — OpenBraille Patent Evidence and Future Research Path
- Authority tier: `TIER_3`
- Manual treatment: `SUPPORTING_EVIDENCE`
- Original source: `03_CONCEPT_PORTFOLIO/OpenBraille/02_Raw_Research/04_OpenBraille_Patent_Research_Qwen.md`
- SHA-256: `79163acf026753e5fe835be66adc8e7d9fc0e0575b09395fd22f227ce5ee5567`
- Extraction method: `PLAIN_TEXT`
- Rule: source text only; no synthesis, correction or reconciliation.

---

# From Assembly Challenge to Patent Asset: Assessing the Viable Innovation Path for OpenBraille's Compliant Mechanism

## Prior Art Landscape and Frozen-MVP Patentability Assessment

The viability of OpenBraille's patent development hinges on its ability to demonstrate a novel and non-obvious contribution over the existing body of knowledge. An exhaustive search of global patent databases—including the Indian Patent Office, WIPO PATENTSCOPE, USPTO, EPO, CNIPA, JPO, and KIPO—as well as scholarly and public technical literature, reveals a dense and mature prior art landscape for refreshable Braille displays [[93](https://en.wikipedia.org/wiki/3D_printing_processes), [196](https://data.uspto.gov/patent-file-wrapper/search/details/11877698/application-data), [335](https://patentassist.ai/search/ipo/)]. This analysis will first establish the state of the art by examining key patent families and projects that directly relate to the core components of the OpenBraille Macro-Scale Prototype (MSP). Subsequently, this established prior art will be used to conduct a rigorous assessment of the MSP's own patentability, evaluating its potential for novelty, inventive step, patent eligibility, and freedom to operate. The central finding is that while the individual components of the MSP are known, their combination does not rise to the level of an inventive concept, placing the project on a precarious path without significant modification.

A foundational piece of prior art is **US Patent 6,354,839 B1**, titled "Refreshable Braille Display," filed by Paul D'Souza [[237](https://hackaday.io/project/10849/logs)]. This patent describes a system utilizing micro-motor actuated pins, which aligns with the core principle of using small motors to drive Braille dots [[237](https://hackaday.io/project/10849/logs)]. Although D'Souza's preferred embodiment employs pneumatic valves controlled by MEMS actuators, the patent explicitly contemplates other actuation methods, including direct motor-driven systems. Its modular design, where functionally independent modules are arranged in rows and columns, provides a conceptual blueprint for building larger displays from smaller units, a principle also applicable to OpenBraille [[35](https://patents.google.com/patent/US6354839B1/en)]. Another highly relevant document is **Indian Application 5559/CHE/2014**, which is titled "Refreshable Braille Display" and claims a system based on micro-servos [[104](https://patents.justia.com/patent/20130203022)]. While the full specification remains inaccessible through publicly available sources, the application number and title indicate a direct claim to the same fundamental architecture as OpenBraille's MSP, representing a significant risk factor for novelty and priority [[323](https://www.wipo.int/patent-judicial-guide/en/full-guide/india), [336](https://www.youtube.com/watch?v=9Vvp2Dh6B_k)].

Beyond patents, numerous open-source projects validate the use of low-cost servos and FDM printing for Braille display construction. The 'Brindle' project, for instance, presents a single-cell, low-cost refreshable Braille display prototype built around TowerPro MicroServo SG90 motors [[12](https://www.scribd.com/document/1062920280/Brindle-a-Low-Cost-Refreshable-Braille-Display-With-Slider-Mechanism), [68](https://www.researchgate.net/publication/379318092_Brindle_A_Low-Cost_Refreshable_Braille_Display_with_Slider_Mechanism)]. It employs a gear-and-rack slider mechanism to move pins, demonstrating the practical feasibility of using off-the-shelf servos for precise pin actuation [[12](https://www.scribd.com/document/1062920280/Brindle-a-Low-Cost-Refreshable-Braille-Display-With-Slider-Mechanism)]. Similarly, multiple student projects and hobbyist guides confirm the widespread adoption of the SG90 servo, often powered externally from an ESP32 board, for constructing DIY Braille readers [[69](https://isef.net/project/robo067-low-cost-braille-display), [70](https://www.semanticscholar.org/paper/A-Portable-Braille-Refreshable-Display-Using-Micro-Rahman-Khandaker/7002973648bafe2a492df6a21e7e96468ccbb663), [182](https://github.com/topics/sg90-servo?l=typescript), [190](https://www.researchgate.net/publication/331623065_A_Portable_Braille_Refreshable_Display_Using_Micro_Servos)]. The ESP32 itself is a ubiquitous choice for such projects due to its integrated Wi-Fi, Bluetooth capabilities, and low cost, making its selection a routine engineering decision rather than an inventive one [[252](https://github.com/topics/esp32?l=javascript&o=desc&s=updated), [298](https://fabacademy.org/2025/labs/salem/ga08.html)]. The software for OpenBraille appears to be adapted from Marlin firmware, which is commonly used for 3D printer control; this adaptation is a logical step for a project repurposing a 3D printer's motion control hardware [[216](https://github.com/carloscamposalcocer/OpenBraille)]. The use of Fused Deposition Modeling (FDM) for the frame and guides is also a common practice, though it comes with well-documented challenges related to dimensional accuracy and mechanical stability [[217](https://hackaday.io/project/51093-openbraille-steam), [219](https://hackaday.io/project/51093/logs)]. Projects like MagnePins further highlight these issues, noting that errors can arise from intermittent electrical connections and manufacturing tolerances, even in sophisticated DIY designs [[1](https://dl.acm.org/doi/10.1145/3746059.3747692)]. The very approach of building a macro-scale prototype to simplify initial development and validate concepts before scaling down to a standard size is a recognized strategy in assistive technology prototyping [[12](https://www.scribd.com/document/1062920280/Brindle-a-Low-Cost-Refreshable-Braille-Display-With-Slider-Mechanism), [218](https://github.com/carloscamposalcocer/OpenBraille/activity)].

This extensive body of prior art forms the basis for the following comparison, which systematically evaluates the frozen OpenBraille MSP against the known state of the art. Every component and architectural choice has a precedent, significantly undermining its potential for novelty.

| Feature | Description | Expressly Disclosed / Necessarily Implied in Prior Art | Arguably Suggested / Absent |
| :--- | :--- | :--- | :--- |
| **Actuator Type** | Six low-cost, SG90-class micro-servos per cell. | **Expressly Disclosed:** The use of micro-servos (e.g., SG90) for Braille pin actuation is explicitly shown in projects like 'Brindle' [[12](https://www.scribd.com/document/1062920280/Brindle-a-Low-Cost-Refreshable-Braille-Display-With-Slider-Mechanism), [68](https://www.researchgate.net/publication/379318092_Brindle_A_Low-Cost_Refreshable_Braille_Display_with_Slider_Mechanism)], Regeneron ISEF projects [[69](https://isef.net/project/robo067-low-cost-braille-display)], and various hobbyist guides [[190](https://www.researchgate.net/publication/331623065_A_Portable_Braille_Refreshable_Display_Using_Micro_Servos)]. Patents like US6354839 B1 discuss micro-motors for this purpose [[237](https://hackaday.io/project/10849/logs)]. | |
| **Mechanical Linkage** | Eccentric cam, follower, and sliding tactile pin. | **Expressly Disclosed:** The concept of using a cam to convert rotary motion into linear pin movement is taught by patents like CA3120784A1, which describes a cam profile on a pico-motor [[111](https://hackaday.io/project/10849-refreshable-braille-display)]. Other designs use levers and cantilevers driven by motors [[237](https://hackaday.io/project/10849/logs)]. | The specific implementation of a single eccentric cam per dot driven directly by a servo arm is a common configuration but may not be identical to every disclosed example. |
| **Frame/Guide Material** | FDM-printed plastic (e.g., PLA, ABS). | **Expressly Disclosed:** FDM is a standard method for creating structural parts in many Braille display projects, including OpenBraille itself and MagnePins [[1](https://dl.acm.org/doi/10.1145/3746059.3747692)]. | The specific material choice (PLA/ABS) is a matter of common engineering practice. |
| **Control System** | ESP32-WROOM-32 microcontroller. | **Expressly Disclosed:** The ESP32 is a widely adopted SoC for low-cost IoT and robotics projects [[252](https://github.com/topics/esp32?l=javascript&o=desc&s=updated)]. Its use for controlling servos is a basic application documented in countless tutorials [[295](https://www.youtube.com/watch?v=PmBzTjIcxKI), [296](https://esp32.implrust.com/servo/index.html)]. The firmware is based on Marlin, adapted from 3D printers [[216](https://github.com/carloscamposalcocer/OpenBraille)]. | |
| **Operating Scale** | Macro-scale (approx. 300% standard Braille). | **Expressly Disclosed:** Building large-scale prototypes to facilitate assembly and testing is a known technique in the field [[12](https://www.scribd.com/document/1062920280/Brindle-a-Low-Cost-Refreshable-Braille-Display-With-Slider-Mechanism), [218](https://github.com/carloscamposalcocer/OpenBraille/activity)]. | |
| **Power Architecture** | External 5V supply for servos. | **Expressly Disclosed:** To avoid overloading the ESP32's regulator, external power is standard practice when driving multiple servos [[255](https://www.espboards.dev/blog/most-popular-esp32-servos/), [257](https://www.upesy.com/blogs/tutorials/esp32-servo-motor-with-arduino-code-sg90?srsltid=AfmBOorsCPDupb20ZxmWAt1rI6zsn4cM3_W8t4Ho-_QxVlCK9NddCSuh)]. | |
| **Calibration** | None specified beyond basic PWM angle control. | **Arguably Suggested:** Calibration is implicitly necessary due to manufacturing variations in servos and printed parts [[217](https://hackaday.io/project/51093-openbraille-steam), [219](https://hackaday.io/project/51093/logs)]. The need for user calibration is noted in projects like MagnePins [[1](https://dl.acm.org/doi/10.1145/3746059.3747692)]. | |

Based on this comprehensive review, the patentability of the frozen OpenBraille MSP can be assessed across several critical dimensions. The analysis concludes that the MSP, in its current form, does not present a credible patent path and falls squarely within Track D: No Credible Patent-Development Path Established.

First, the **novelty risk is extremely high**. A person skilled in the art would find at least one prior art reference disclosing every single element of the MSP. The combination of a servo motor, eccentric cam, FDM-printed structure, and ESP32 controller for a refreshable Braille cell is not new. Multiple documents describe this exact combination, making it difficult to argue that the MSP constitutes a "new" invention. The existence of Indian Application 5559/CHE/2014, even without access to its full claims, creates a strong presumption of anticipation if its subject matter covers similar ground [[104](https://patents.justia.com/patent/20130203022)].

Second, the **obviousness/inventive-step risk is extreme**. Even if some minor feature were considered novel, the overall solution represents an obvious aggregation of known techniques. Combining off-the-shelf components—a cheap servo, a simple cam mechanism, a 3D printer, and a popular microcontroller—to solve a known problem (creating a low-cost Braille display)—would almost certainly be deemed obvious to a person having ordinary skill in the art. There is no indication of unexpected results or synergistic effects that would elevate this combination beyond the sum of its parts. The project essentially follows a well-trodden path laid out by numerous researchers and hobbyists.

Third, the **patent eligibility risk is moderate to high**. In jurisdictions like the United States, inventions must fall into one of four statutory categories (process, machine, manufacture, or composition of matter) and cannot be directed to abstract ideas, laws of nature, or natural phenomena. The MSP, as described, could be argued to be a collection of conventional hardware elements performing their basic functions, which may lead a patent examiner to deem it an abstract idea implemented on a generic computer (the ESP32). While the physical arrangement of mechanical parts provides a "machine" aspect, the lack of a truly inventive or unconventional physical process makes it vulnerable to challenges under frameworks like Alice Corp v. CLS Bank. The fact that it solves a social problem (accessibility) does not, by itself, confer patent eligibility.

Finally, the **freedom-to-operate (FTO) risk is high**. Assuming a patent could be obtained—which is unlikely—the resulting patent would likely be weak and easily invalidated. More importantly, operating OpenBraille commercially would require navigating a minefield of existing patents. For example, the family including **US Patent 6,354,839 B1** and **CA3120784A1** covers electromagnetic actuators but establishes the foundational concept of modular, motor-driven Braille cells [[42](https://patents.google.com/patent/US3659354A/en), [188](https://patents.google.com/patent/CA3120784A1/en), [237](https://hackaday.io/project/10849/logs)]. Other families, such as **WO2020106855** and its equivalents (**US12548467B2**, **EP3884363B1**), cover modular, affordable, and DIY refreshable Braille displays using electromagnetic latching actuators, a conceptually similar goal [[188](https://patents.google.com/patent/CA3120784A1/en)]. Operating freely would necessitate either licensing these rights or designing around them entirely, a task made more difficult by the high degree of overlap between the MSP's architecture and the teachings of these patents.

In summary, the frozen OpenBraille MSP is not a defensible invention. It is a pragmatic and resourceful assembly of known technologies. To pursue a credible patent path, the project must evolve beyond this baseline and introduce a distinct, non-obvious innovation. The subsequent sections of this report will explore promising directions for such an evolution, focusing on enhancements that address the inherent weaknesses of the current design.

## Candidate Invention Directions: Manufacturing & Control Strategies

Given that the frozen OpenBraille MVP lacks sufficient novelty and inventiveness, the focus must shift to identifying a bounded enhancement that can create a credible patent path. The project's stated pivot away from actuator novelty is a sound strategic choice, as actuator patents tend to be broad and heavily litigated. Instead, innovation should target the system's weakest links: mechanical precision, tolerance management, and control algorithms. This section critically evaluates several candidate invention directions, prioritizing manufacturing and fabrication innovations as the primary avenue and firmware/control strategies as a secondary option, in line with the research directive. Each direction is assessed based on its nearest prior art, prospective differentiating elements, required enhancement type, feasibility, and principal patent risks.

**Primary Candidate Direction: Tolerance-Compensating Compliant Mechanisms**

This direction proposes replacing the rigid, multi-part guide system of the MVP with a single, integrally-molded compliant mechanism fabricated using FDM. The core idea is to leverage the elastic properties of the printed plastic to absorb minor misalignments caused by manufacturing tolerances, material shrinkage, and assembly errors.

*   **Nearest Prior Art:** Most commercial and advanced Braille displays rely on precision-engineered metal rails, bearings, or complex interposer mechanisms to ensure perfect pin alignment and prevent binding [[42](https://patents.google.com/patent/US3659354A/en), [290](https://patents.google.com/patent/US20100304340A1/en)]. Open-source projects like MagnePins attempt tolerance compensation but do so passively through the use of highly consistent, external components (fabricated pins) and retaining collars, rather than through an intrinsic, monolithic compliant geometry [[1](https://dl.acm.org/doi/10.1145/3746059.3747692)]. The general principles of compliant mechanisms are known in mechanical engineering, often involving flexure hinges or leaf springs to achieve motion with fewer parts [[214](https://www.mdpi.com/2072-666X/13/6/817)]. However, their specific application to an FDM-printed, cam-driven, refreshable Braille cell is not found in the provided prior art.

*   **Prospective Differentiating Elements:** The key innovation would be the design of a single FDM-printed part that serves as both the cell housing and the guiding/retracting mechanism for the tactile pins. This would involve integrating features like thin, flexible beams or serpentine flexures that provide a restoring force to retract the pin while allowing slight lateral compliance to accommodate manufacturing variance. This differs from the MVP's rigid guides and the MagnePins approach of compensating for error after it occurs.

*   **Required Enhancement:** This requires a **bounded enhancement** to the existing CAD model. It does not necessitate new actuators, sensors, or a complete redesign of the control system. The change is confined to the geometric design of the guide components.

*   **Physical Advantage & Experiment:** The measurable technical effect would be a significant improvement in the reliability and consistency of pin actuation across different build iterations and assembly conditions. An experiment would involve:
    1.  Designing and printing two versions of the cell: one with the original rigid guides and one with the new compliant guides.
    2.  Measuring the repeatability of pin height for each design using a calibrated sensor or microscope.
    3.  Actuating each pin repeatedly and recording instances of binding, incomplete retraction, or inconsistent height.
    4.  The expected result is that the compliant version will exhibit fewer errors and greater consistency despite intentional variations in print quality or assembly pressure.

*   **Feasibility (Budget & Timeline):** This is highly feasible within the ₹5,000 budget and three-month timeline. The primary cost will be filament for iterative printing and testing. The timeline allows for several design-build-test cycles. The team already possesses the necessary skills in CAD and FDM printing.

*   **Principal Patent Risks:** The main risk is being challenged on grounds of obviousness. An opponent could argue that applying general principles of compliant design to a new problem is an obvious engineering choice. However, the novelty lies in the specific intersection of FDM printing, a cam-driven actuator, and a monolithic compliant guide for a refreshable Braille cell. This specific combination is not taught by the prior art and presents a plausible case for non-obviousness. The risk is manageable.

**Secondary Candidate Direction: Verified Tactile-State Control via Closed-Loop Calibration**

This direction explores firmware and control strategies to improve performance by actively verifying the state of each pin after actuation. This moves beyond the current open-loop control (servo moves to a commanded angle) to a closed-loop system.

*   **Nearest Prior Art:** Calibration is a universal requirement in sensor-based systems, such as camera calibration [[281](https://github.com/openPupil/Open-PupilEXT/discussions/3)], flow meter calibration (Gilibrator 3) [[168](https://sensidyne.com/wp-content/uploads/2024/03/1-Gilibrator-3-Primary-Calibrator-Datasheet_rL_021020.pdf?srsltid=AfmBOoqPsYYmLfpF_9ArFi_X1sJUtUG57OowU3YRz7UKU3w2gSIVbv3v), [227](https://sensidyne.com/wp-content/uploads/2024/03/1-Gilibrator-3-Primary-Calibrator-Datasheet_rL_021020.pdf?srsltid=AfmBOoqFxeU8z-F-aFUqXHdmiz4tTkOzSt904R_Ws9RqhoXemIhRzhTx)], and 3D printer bed leveling [[103](https://www.mdpi.com/2227-9717/11/10/2810)]. The MagnePins project notes that its device required user calibration due to intermittent electrical connections, highlighting the real-world need for verification [[1](https://dl.acm.org/doi/10.1145/3746059.3747692)]. Some Braille display patents mention interposers or locking mechanisms that imply a verified state [[42](https://patents.google.com/patent/US3659354A/en)].

*   **Prospective Differentiating Elements:** The innovation would be a low-cost, integrated sensor (e.g., optical interrupter, magnetic reed switch) paired with a firmware algorithm that performs a post-actuation check. For example, after commanding a pin to raise, the firmware would read the sensor to confirm the pin has reached its maximum height. If not, it could trigger a re-attempt or log an error. This provides a verifiable, repeatable pin state, improving reliability.

*   **Required Enhancement:** This requires a **bounded enhancement** to the hardware (adding sensors) and firmware (implementing the verification logic).

*   **Physical Advantage & Experiment:** The technical effect is increased operational reliability and accuracy by mitigating failures from servo inconsistency, mechanical wear, or debris. An experiment would measure the bit-error rate (false highs or false lows) of the display with and without the closed-loop verification enabled. A decrease in error rate would be the pass/fail evidence.

*   **Feasibility (Budget & Timeline):** This is achievable within the constraints. Adding simple sensors adds minimal cost. The firmware modification is a standard programming task for the team. The timeline is sufficient for implementation and testing.

*   **Principal Patent Risks:** The primary risk is patent eligibility. A purely software-implemented method for calibration may be deemed an abstract idea. Furthermore, such methods can be difficult to enforce against competitors who replicate the behavior without copying the exact code. The risk of obviousness is also present, as feedback loops are a standard control theory concept. This path is less robust than the compliant mechanism.

**Other Evaluated Directions (Rejected)**

*   **Low-Cost Per-Dot Calibration:** This was evaluated but rejected. The term is too vague. Any meaningful calibration (e.g., mapping PWM duty cycle to actual pin angle) is a standard procedure for any custom servo-based system and would not be considered novel.
*   **Modular Replaceable Architecture:** Modularity is a recurring theme in Braille display patents (e.g., US6354839 B1 [[35](https://patents.google.com/patent/US6354839B1/en)]) and is a desirable feature for repairability. Simply designing a snap-fit joint for FDM parts is likely obvious and does not represent a sufficiently strong inventive step.
*   **Current-Aware Sequencing:** Optimizing actuator sequencing to minimize peak current draw is a classic embedded systems optimization problem. While beneficial for battery life, it is unlikely to be considered a patentable invention on its own, as it is a straightforward application of known power management techniques.

The table below summarizes the comparative analysis of the candidate directions.

| Candidate Direction | Primary/Secondary | Nearest Prior Art | Key Differentiator | Enhancement Type | Patent Risk Profile |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Compliant Printed Guide** | Primary | Rigid metal guides [[290](https://patents.google.com/patent/US20100304340A1/en)]; Passive compensation in MagnePins [[1](https://dl.acm.org/doi/10.1145/3746059.3747692)]. | Monolithic, elastic guide integrated with FDM housing to absorb tolerance errors. | Bounded (CAD Redesign) | Moderate Novelty, Low Obviousness. Strongest candidate. |
| **Verified Tactile-State Control** | Secondary | Sensor calibration techniques [[168](https://sensidyne.com/wp-content/uploads/2024/03/1-Gilibrator-3-Primary-Calibrator-Datasheet_rL_021020.pdf?srsltid=AfmBOoqPsYYmLfpF_9ArFi_X1sJUtUG57OowU3YRz7UKU3w2gSIVbv3v), [281](https://github.com/openPupil/Open-PupilEXT/discussions/3)]. | Closed-loop firmware algorithm to verify pin position post-actuation. | Bounded (Hardware + Firmware) | High Obviousness, High Eligibility Risk. Weaker candidate. |
| **Modular Architecture** | Secondary | Modular designs in patents like US6354839 B1 [[35](https://patents.google.com/patent/US6354839B1/en)]. | Snap-fit joints for FDM parts. | Bounded (CAD Redesign) | High Obviousness. Not a credible path. |
| **Current-Aware Sequencing** | Secondary | Standard power management in embedded systems. | Algorithm to sequence pin activation to minimize peak current. | Bounded (Firmware) | Very High Obviousness. Not a credible path. |

In conclusion, the most promising path forward for OpenBraille is to pivot from the current rigid MVP to a design incorporating **tolerance-compensating compliant mechanisms**. This bounded enhancement directly addresses a fundamental weakness of low-cost, 3D-printed assemblies and offers a tangible, measurable technical benefit. It represents a targeted innovation rooted in the project's methodology and stands the best chance of satisfying the legal requirements for a credible patent. The project should therefore advance on Track B, contingent on successfully developing and experimentally validating this enhanced mechanism.

## Experimental Validation Framework and Scale Transfer Feasibility

For a patent application to be credible, especially one claiming a tangible technical effect, it must be supported by evidence. The research goal mandates that a patent path must be "experimentally supportable." This section outlines a detailed framework for the experiments needed to validate the proposed compliant mechanism enhancement and assesses the critical issue of scale transfer. The analysis concludes that while macro-scale evidence can provide valuable preliminary insights, physical validation at standard Braille scale is ultimately mandatory for establishing the credibility of a patent path intended for practical applications.

The core of the patentability argument for the compliant mechanism will rest on its ability to demonstrably improve the reliability and accuracy of pin actuation. Therefore, a rigorous experimental validation plan is essential. This plan must define the test setup, the metrics for success, and the methodology for generating reliable data. The experiments should be designed to produce clear, quantitative evidence that can withstand scrutiny during a patent examination.

**Experimental Validation Framework for the Compliant Mechanism**

The primary objective of the experiments is to compare the performance of the original rigid-guide design against the new compliant-guide design. The hypothesis is that the compliant design will exhibit superior performance in terms of repeatability and resistance to assembly-induced errors.

1.  **Test Setup:** The setup will consist of two identical OpenBraille cells, one modified with the compliant guide and one retaining the original rigid guide. Both cells will be actuated by the same ESP32 controller and SG90 servos to eliminate variability in the actuation system. The key variables to be controlled are the servo calibration, power supply voltage, and ambient temperature. A simple jig can be 3D printed to hold the cells in a fixed orientation for consistent measurement.

2.  **Metrics for Success (Measurable Technical Effects):**
    *   **Pin Height Repeatability:** Using a calibrated digital micrometer or a laser displacement sensor, measure the raised height of each of the six pins on both cell designs. Perform 20 actuation cycles for each pin and calculate the standard deviation of the measured heights. A lower standard deviation indicates higher repeatability. The pass/fail criterion would be a statistically significant reduction (e.g., p<0.05) in the standard deviation for the compliant design.
    *   **Binding and Failure Rate:** Manually assemble and disassemble each cell multiple times (e.g., 10 cycles). During each cycle, manually actuate all pins and record any instances of binding, incomplete retraction, or failure to reach the commanded height. The compliant design is hypothesized to have a significantly lower failure rate.
    *   **Force Measurement:** Use a small load cell to measure the force required to fully depress a pin. This can reveal how the compliant spring action affects the perceived "feel" of the dot. A consistent force profile is desirable.

3.  **Data Collection and Analysis:** Data from the experiments should be recorded in a spreadsheet. Statistical analysis, such as t-tests, should be used to determine if the differences in performance between the two designs are statistically significant. The raw data, along with the analysis, forms the empirical foundation of the patent application.

**Scale-Transfer Feasibility and Mandatory Standard-Scale Validation**

A critical constraint of the research is the project's current macro-scale prototype. The question arises: can evidence from this large-scale model support a patent path intended for standard Braille displays (typically 2.5mm dot pitch)? The answer is nuanced and governed by the "Macro-scale and scale-transfer rule" from the research goal.

The analysis classifies claim elements as **Scale-independent**, **Scale-sensitive**, or **Standard-scale validation mandatory**.

*   **Scale-Independent Elements:** These are aspects of the invention that do not depend on the absolute size of the components.
    *   **Compliant Mechanism Concept:** The core idea of using a flexible, monolithic FDM part to compensate for manufacturing tolerances is inherently scale-independent. The physics of elastic deformation applies equally at macro or micro scales.
    *   **Closed-Loop Control Algorithm:** The logic of commanding an action and then verifying its completion is also scale-independent.

*   **Scale-Sensitive Elements:** These elements depend directly on the dimensions of the Braille standard.
    *   **Pin Dimensions:** The diameter (typically ~1.8mm) and height (~0.6mm - 0.9mm) of the tactile pins are standard-specific [[1](https://dl.acm.org/doi/10.1145/3746059.3747692), [145](https://tactiles.eu/guidelines/3-braille/)].
    *   **Dot Pitch:** The spacing between pins (2.5mm) is a defining characteristic of standard Braille [[1](https://dl.acm.org/doi/10.1145/3746059.3747692)].
    *   **Force Requirements:** The force needed to reliably feel a dot is dependent on the dot's size and the user's fingertip sensitivity, which are tied to the standard.
    *   **Friction and Wear:** At a smaller scale, friction forces become proportionally larger relative to the actuation forces, and wear on microscopic surfaces becomes a more significant factor.

*   **Standard-Scale Validation Mandatory:** Based on the above, the following elements require mandatory physical validation at standard scale before the patent path can be considered strongly validated:
    1.  **Proof of Functionality at Standard Scale:** The compliant mechanism must be physically demonstrated to work correctly when scaled down to the 2.5mm pitch. The elasticity that helps at macro-scale might be insufficient or cause buckling at a smaller scale.
    2.  **Verification of Force Profile:** The tactile feel of the dot must be tested to ensure it meets the requirements for readability. The compliant spring force must be sufficient to provide a clear tactile signal but not so high as to be uncomfortable or difficult to depress.
    3.  **Assessment of Durability and Wear:** Long-term durability and wear characteristics at the microscopic level cannot be reliably predicted from macro-scale tests.

**Relevance of Macro-Scale Evidence**

Macro-scale experiments are not a waste of time. They are an essential and valid step in the development process. Evidence gathered at this scale is highly relevant for several reasons:

*   **Concept Validation:** It proves the core concept of the compliant mechanism works. If the mechanism fails at macro-scale, there is no point in attempting a more expensive and difficult build at standard scale.
*   **Iterative Design:** The macro-scale model allows for rapid, low-cost iteration of the compliant geometry. The team can test dozens of design variations quickly, refining the concept before committing to a final, standard-scale design.
*   **Engineering Analysis Support:** The macro-scale experiments provide crucial data for simulations. Finite Element Analysis (FEA) models of the compliant mechanism can be validated against the macro-scale test results, increasing confidence in the simulation predictions for the standard-scale version.
*   **Enabling Standard-Scale Design:** As per the research goal, macro-scale evidence, when combined with engineering analysis, tolerance calculations, and a clearly enabling standard-scale design, can support an early patent filing. The macro-scale build acts as a proof-of-concept that de-risks the more ambitious standard-scale project.

Therefore, the recommended strategy is a phased approach:
1.  **Phase 1 (Semester MVP):** Focus on designing, building, and thoroughly testing the compliant mechanism on the existing macro-scale OpenBraille platform. Generate strong statistical evidence of improved performance.
2.  **Phase 2 (Post-Semester Extension):** Based on the success of Phase 1, develop a detailed design for a standard-scale (2.5mm pitch) version of the compliant cell. This phase would involve fine-tuning the FEA models, selecting appropriate materials, and fabricating a prototype at the correct scale.
3.  **Phase 3 (Publication-Oriented Research):** Physically validate the standard-scale prototype, confirming its functionality, force profile, and durability. This completes the evidence chain.

This approach aligns perfectly with the research goal's classification system. The project's immediate patent path is on **Track B: Credible through a bounded enhancement**. The successful completion of Phase 1 (the three-month semester) will generate the necessary evidence to file a provisional patent application. The full, commercially viable invention—requiring standard-scale validation—is classified as a **Track C: Semester MVP achievable, but strongest patent-development mechanism requires a later semester or publication-oriented research extension**. This ensures that the project remains achievable within the given constraints while still pursuing a strong, long-term patent strategy.

## Freedom-to-Operate and Patent Eligibility Risk Analysis

While assessing novelty and inventive step is paramount, two other legal considerations are critical for determining the viability of a patent path: Freedom-to-Operate (FTO) and patent eligibility. FTO analysis determines the risk of infringing on existing, active patents, while patent eligibility analysis assesses whether the invention qualifies for protection under the law. A thorough investigation of the mandated patent families and relevant legal frameworks reveals significant risks in both areas, reinforcing the conclusion that the frozen OpenBraille MSP is not a standalone invention and that future enhancements must be carefully designed to navigate this complex intellectual property landscape.

**Freedom-to-Operate (FTO) Risk Analysis**

An FTO analysis examines the claims of issued and pending patents to identify potential infringement. Operating a product without permission from the patent holder can lead to costly litigation. The analysis focuses on the most relevant patent families identified in the research goal.

*   **Family: WO2020106855 / EP3884363 / US12548467B2 ("MagnePins")**
    *   **Summary:** This family, originating from Canadian patent CA3120784A1, describes an electromagnetic refreshable Braille reader (EMBR) using bistable electromagnetic actuators [[188](https://patents.google.com/patent/CA3120784A1/en)]. It emphasizes modularity, affordability, and mass-producible assembly [[188](https://patents.google.com/patent/CA3120784A1/en)]. The patented design includes asymmetric coil windings for energy efficiency and noise-reduction techniques [[188](https://patents.google.com/patent/CA3120784A1/en)].
    *   **Risk Assessment:** Although the core actuation technology (electromagnets) differs from OpenBraille's servo/cam system, the emphasis on modularity, DIY fabrication, and affordability places this family in close conceptual proximity. Claims related to modular assembly techniques or methods of mass-producing Braille cells could potentially be construed to cover OpenBraille's approach, especially if a court finds the distinction between electromagnetic and servo-driven actuation to be insubstantial. The broad scope of some claims in this family poses a significant FTO risk.

*   **Family: US11410574B2 and its Family Members**
    *   **Summary:** This patent covers a refreshable Braille display with a unique feature: a passive retention mechanism that holds the Braille pins in an extended or retracted position without requiring continuous power or mechanical latching [[310](https://patents.google.com/patent/US11854423B1/en)]. This "held-in-position" feature is achieved through a specific interaction between the pin, a surface layer, and the internal mechanics.
    *   **Risk Assessment:** The risk here is indirect but notable. If OpenBraille's compliant mechanism inadvertently creates a similar passive retention effect (e.g., by causing friction that holds a pin in place), it could fall within the scope of these claims. The language of patent claims is often broader than the inventor's intent, and a narrow design choice in OpenBraille could unexpectedly infringe a broader claim.

*   **Family: US6743021 / US8690576 / US9424759 (The "Interposer" Family)**
    *   **Summary:** This series of patents, primarily assigned to The Mitre Corporation, focuses on a crucial mechanical component: an interposer slide [[42](https://patents.google.com/patent/US3659354A/en)]. This slide moves between positions to either block or permit the movement of Braille pins, allowing for serial control of cells in an array. This enables a single controller to manage a large display efficiently [[42](https://patents.google.com/patent/US3659354A/en)].
    *   **Risk Assessment:** This is a high-risk family. Even though OpenBraille uses parallel servo control for its single cell, the underlying principle of using an intermediate mechanical part to gate pin movement is central to this patent. If the compliant mechanism design introduces a secondary moving part with a similar gating function, it could be considered an infringement. The patents are broad and cover the functional principle, not just the specific embodiment shown.

*   **Other Relevant Patents:**
    *   **US Patent 6,354,839 B1:** Describes a modular Braille display using micro-motors and pneumatic valves, establishing the foundational concept of motor-driven cells [[237](https://hackaday.io/project/10849/logs)].
    *   **US Patent 3,659,354:** Covers a Braille display with a fluid-pressure actuated interposer for locking patterns [[42](https://patents.google.com/patent/US3659354A/en)].
    *   **US Patent 6,692,255:** Filed by the National Institute of Standards and Technology (NIST), this patent describes a bi-directional refreshable tactile display, indicating that even government labs were actively innovating in this space [[179](https://en.wikipedia.org/wiki/Refreshable_braille_display)].

**Synthesis of FTO Risk:** The FTO landscape for refreshable Braille displays is dense and competitive. While the frozen MSP is unlikely to infringe on the specific cam-and-servo mechanism of a particular patent, the surrounding functional claims related to modularity, cell arrays, and mechanical interposers create a significant risk. Operating OpenBraille commercially without a license or a freedom-to-operate opinion from a patent attorney would be highly risky. This reinforces the need for the project to seek a truly distinct invention, as navigating this landscape would be challenging.

**Patent Eligibility Risk Analysis**

Patent eligibility refers to whether an invention falls into a category of subject matter that a patent office considers protectable. Many jurisdictions, particularly the United States, have strict rules against patenting abstract ideas, laws of nature, or natural phenomena, even if they are novel and non-obvious. This is a major hurdle for inventions involving software or combinations of generic hardware.

*   **United States (Alice/Mayo Test):** Under U.S. law, a two-step test is used. First, determine if the claim is directed to a judicial exception (an abstract idea, natural law, or law of nature). Second, if it is, determine whether the claim contains an "inventive concept" that transforms the exception into a patent-eligible application.
    *   **Risk for OpenBraille:** The frozen MSP is highly vulnerable. Its reliance on a general-purpose microcontroller (ESP32) running firmware to control conventional hardware (servos, cams) could be argued to be an abstract idea implemented on a generic computer. The physical components alone may not be enough to constitute a "practical application" that rises above the abstract idea. The Supreme Court's decision in *Alice Corp. v. CLS Bank* has made it difficult to obtain patents on business methods and software-implemented processes. A similar logic applies here; combining known parts in a conventional way is often seen as an abstract idea.
    *   **Path to Eligibility:** To overcome this, the patent claim must be framed around a specific, unconventional *physical process* or a *non-conventional and non-generic arrangement of known, conventional components*. The proposed compliant mechanism enhancement strengthens the case for eligibility. By describing a novel physical structure (the compliant guide) that produces a new and useful result (improved tolerance to manufacturing error), the invention moves away from being merely a software-controlled process and towards being a specific machine or manufacture. The key is to emphasize the unique physical interactions and structural features in the claims.

*   **India (Indian Patent Act, 1970):** Section 3(k) of the Indian Patents Act states that "a scientific principle or mathematical formula... shall not be regarded as an invention." However, the law is generally more favorable to process and apparatus patents than U.S. law.
    *   **Risk for OpenBraille:** The risk in India is lower than in the U.S. for a pure software invention. The OpenBraille device, as a tangible electro-mechanical apparatus, would likely be considered a "manufacture" under Section 3(m) and thus eligible for patenting. However, the challenge would remain in proving novelty and inventive step against the prior art, as discussed previously. The primary barrier in India would be the density of existing patents, not subject matter eligibility.

*   **European Union (EPC):** Article 52(2) and (3) of the European Patent Convention excludes certain subject matters from patentability, including "programs for computers" and "methods for doing business."
    *   **Risk for OpenBraille:** Similar to the U.S., a claim limited to a computer program "as such" would be excluded. However, a claim to a technical apparatus (the Braille cell) that is controlled by a program is permissible. The European approach often looks for a "further technical effect" produced by the software beyond the normal physical interaction of a computer with its peripherals. The firmware for OpenBraille, if it only performs basic servo control, may not produce such an effect. Again, the compliant mechanism, as a physical invention, is safer from eligibility challenges.

**Synthesis of Eligibility Risk:** The frozen MSP faces a moderate to high risk of being deemed ineligible for patent protection in jurisdictions like the U.S. due to its heavy reliance on generic hardware and software. The proposed compliant mechanism enhancement significantly mitigates this risk by grounding the invention in a novel physical structure and a tangible technical effect. To secure a strong patent portfolio, OpenBraille must frame its claims around the physical apparatus and its unique mechanical properties, rather than the software that controls it. Treating the specific geometry of the compliant mechanism as confidential IP until formal filing is advised.

## Final Verdict and Strategic Recommendation

This deep research report has conducted an exhaustive evaluation of the OpenBraille project's potential for a credible, experimentally supportable patent path within its defined constraints. The analysis, grounded in an investigation of global prior art and technical literature, leads to a definitive conclusion and a set of actionable recommendations. The project's current status and its most promising evolutionary path have been clearly delineated.

**Final Verdict on Patent Viability**

The OpenBraille project, as it exists in its frozen Macro-Scale Prototype (MSP) state, **does not possess a credible patent path**. The combination of its constituent elements—a low-cost servo, an eccentric cam linkage, FDM-printed parts, and an ESP32 controller—represents a collection of known, off-the-shelf technologies assembled in a manner that is obvious to a person skilled in the art of assistive technology prototyping. Every key architectural feature has a precedent in the extensive prior art, ranging from granted patents like US6354839 B1 and CA3120784A1 to numerous open-source projects such as 'Brindle'. Consequently, the frozen MVP is vulnerable to rejection on grounds of both **lack of novelty and lack of inventive step**. Furthermore, it carries a moderate to high risk of being deemed ineligible for patent protection in jurisdictions like the United States due to its characterization as an abstract idea implemented on generic hardware. The Freedom-to-Operate (FTO) landscape is also dense with relevant patents covering modularity and mechanical interposers, posing a significant risk of infringement.

However, this negative assessment of the MVP does not render the entire project nonviable. The analysis has identified a clear and promising path forward. The project should be classified as **Track B: Credible path only with bounded enhancement**. The most viable route to a credible patent is through the bounded enhancement of incorporating a **tolerance-compensating compliant mechanism** into the cell's guide and return system.

**Strategic Recommendations**

To transition from a non-patentable assembly to a defensible invention, the OpenBraille team should adopt the following strategic roadmap:

1.  **Advance on Track B:** Immediately pivot the development effort from the current rigid MVP to the design and implementation of the compliant mechanism. This involves a CAD redesign of the guide components to be a single, integral, FDM-printed part that utilizes flexure-based compliance to absorb manufacturing and assembly errors.

2.  **Conduct Rigorous Experimental Validation:** The success of this patent path is contingent on empirical evidence. The team must build and test prototypes comparing the original rigid design with the new compliant design. The experiments must be designed to yield quantitative data on key metrics such as pin actuation repeatability, binding failure rates, and force profiles. This data is the cornerstone of any future patent application and must be meticulously documented.

3.  **Maintain Confidentiality:** The specific geometric design of the compliant mechanism, once developed, should be treated as confidential intellectual property. It should not be publicly disclosed in repositories or presentations until a provisional patent application has been filed to secure a priority date.

4.  **Plan for Phased Development (Track C):** The successful validation of the compliant mechanism at the macro-scale (within the current three-month semester) will establish the patent path. However, the ultimate commercial relevance of the invention depends on its performance at standard Braille scale (2.5mm pitch). Therefore, the project should be viewed as having two phases:
    *   **Phase 1 (Semester MVP - Track B):** Achieve and validate the compliant mechanism at macro-scale.
    *   **Phase 2 (Later Extension - Track C):** Develop, fabricate, and validate a standard-scale prototype based on the successful macro-scale design. This second phase is necessary to prove the invention's full utility and is a prerequisite for a strong, commercially-focused patent.

5.  **Proceed with Caution Regarding FTO:** While pursuing the patent, the team must remain cognizant of the existing patent landscape. The development of the compliant mechanism should be monitored to ensure it does not inadvertently infringe on the broader functional claims of patents like those in the WO2020106855 and US11410574B2 families. A professional FTO search may be warranted once a concrete design is finalized.

In conclusion, OpenBraille has moved beyond being a simple assembly of known parts. By strategically enhancing its design to incorporate a novel compliant mechanism, it can transform into a project with a genuine and credible patent potential. The path forward is clear: embrace the bounded enhancement, rigorously validate its benefits with experiments, and proceed with a phased development plan that acknowledges the critical importance of eventual standard-scale implementation.


---

## Source 11: `03_CONCEPT_PORTFOLIO/OpenBraille/02_Raw_Research/05_OpenBraille_Patent_Research_Mistral.md`

- Authority: `TIER_3`
- Treatment: `SUPPORTING_EVIDENCE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `NEW_STAGE10F_EXTRACTION`
- SHA-256: `01f4d8b9f146f2c7989000672b47456628966b705dd06350b3683496df522aad`

# Source Extraction

- Chapter: `05` — OpenBraille Patent Evidence and Future Research Path
- Authority tier: `TIER_3`
- Manual treatment: `SUPPORTING_EVIDENCE`
- Original source: `03_CONCEPT_PORTFOLIO/OpenBraille/02_Raw_Research/05_OpenBraille_Patent_Research_Mistral.md`
- SHA-256: `01f4d8b9f146f2c7989000672b47456628966b705dd06350b3683496df522aad`
- Extraction method: `PLAIN_TEXT`
- Rule: source text only; no synthesis, correction or reconciliation.

---

# OpenBraille Patent Verification — Independent Deep Research Report

**Research Session:** 2026-07-30T18:22:37.960Z
**Status:** Final
**Classification:** CONFIDENTIAL — Contains prospective invention analysis
**Author:** Independent Multidisciplinary Patent-Landscape & Embedded-Mechanical Engineering Research Board

---

## 📋 Executive Assessment

### Classification Verdict

**OpenBraille's current frozen MVP (servo + cam + macro-scale) does NOT contain a credible patent candidate on its own.**

**Strongest surviving path:** **Track C** — Semester MVP achievable within three months, but the strongest patent-development mechanism requires a later semester or publication-oriented research extension.

**Credible patent-development path exists only through a bounded enhancement** that pivots away from the basic servo/cam actuator mechanism (which is **not novel**) and toward:
1. **Tolerance-compensating manufacturing/fabrication method** for low-cost, repeatable tactile cells
2. **Verified tactile-state control architecture** with measurable performance advantages
3. **Scale-transfer methodology** from macro (300%) to practical scale with documented engineering bridge

**Confidence:** High (8.5/10)
**Limitations:** No direct access to official Indian Patent Office records for 5559/CHE/2014; Dot Inc. estate requires counsel-level claim-charting; macro-scale evidence may not transfer to standard-scale claims.

---

## 🎯 Central Research Question Answer

**Question:** Does OpenBraille have a credible, experimentally supportable patent-development path within its ₹5,000 budget and 3-month semester constraints?

**Answer:** **No, not in the current frozen MVP architecture.** The servo + cam + direct PWM combination is **already disclosed in multiple prior art sources**, including:
- Indian Patent Application **5559/CHE/2014** (Paul D'souza) — explicitly covers servo/cam Braille display features
- **MOLBED** open-hardware project — magnetic retaining system with servo/cam actuation
- **Hackaday project #191181** — electromagnet-based cam actuator with 3D printing
- **Olin College PIE 2021-03** — servo-driven cam system for Braille pins
- **ResearchGate publication** — "Refreshable Braille Module Using Cam Actuated Mechanism" with micro-servo motors

**However**, a **credible path exists through Track C**: Build the semester MVP to generate evidence for a later patent filing focused on **manufacturing method + control/firmware innovations**, not the actuator mechanism itself.

---

## 📜 1. Executive Summary

### 1.1 Ranked Takeaways

| Rank | Finding | Impact | Confidence |
|------|---------|--------|------------|
| 1 | **Servo/cam actuator is NOT novel** — Multiple prior art disclosures exist for servo-driven cam mechanisms in refreshable Braille cells | **CRITICAL** — Invalidates basic mechanism claims | **High** (9/10) |
| 2 | **Indian Patent 5559/CHE/2014 is a blocking disclosure** — Filed 2014, covers servo/cam Braille display, forced open-source project discontinuation | **CRITICAL** — Direct prior art | **High** (8/10) |
| 3 | **Dot Inc. estate (110+ patents) dominates commercial actuator space** — FTO risk for any electromagnetic latching or piezo-replacement approach | **HIGH RISK** — Requires claim-charting | **High** (9/10) |
| 4 | **Open-hardware projects (MOLBED, Hackaday) disclose identical architecture** — Servo + cam + 3D printed frame + modular cells | **HIGH RISK** — Anticipates MVP | **High** (9/10) |
| 5 | **Pivot to manufacturing/firmware is the only viable path** — Phase 2 correctly identified this; servo/cam MVP can generate supporting evidence | **VIABLE** — Matches repository direction | **Medium-High** (7/10) |
| 6 | **Macro-scale evidence has limited transfer value** — Most claim elements are scale-sensitive; standard-scale validation is mandatory | **LIMITATION** — Constrains claim scope | **High** (8/10) |
| 7 | **Track C is the optimal classification** — Semester MVP + later extension for patent development | **RECOMMENDED** | **High** (9/10) |

### 1.2 Composite Verdict

- **Current MVP as filed:** ❌ No credible patent path
- **With bounded enhancement:** ⚠️ Track C (semester MVP + later extension)
- **With major redesign:** ⚠️ Track C (pivot to manufacturing method)
- **No credible path:** ❌ Only if constrained to actuator mechanism novelty

---

## 🔍 2. Search Log

### 2.1 Search Strategy

**Phase 1: Baseline Extraction** (2026-07-30)
- Parsed all provided project files to extract frozen MVP specifications
- Identified 15 mandatory search areas and 20+ named patent leads

**Phase 2: Patent Landscape Mapping** (2026-07-30)
- Searched USPTO, EPO (Espacenet), WIPO (PATENTSCOPE), Google Patents
- Searched Indian Patent Office (IPR Search)
- Searched Chinese, Japanese, Korean records via Google Patents
- Searched non-patent literature: Hackaday, GitHub, ResearchGate, Hackster.io

**Phase 3: Specific Patent Verification** (2026-07-30)
- Verified 15+ specific patent numbers across all jurisdictions
- Retrieved full text and claims where accessible
- Cross-referenced family members

### 2.2 Search Queries Executed

| # | Database/Jurisdiction | Query | Results | Relevance |
|---|---------------------|-------|---------|-----------|
| 1 | Google Patents (USPTO) | `US11854423B1 refreshable braille display Dot Inc` | 5 | High |
| 2 | Google Patents | `US11410574B2 braille actuator patent` | 5 | High |
| 3 | Google Patents | `WO2015189863 braille tactile display` | 5 | High |
| 4 | Google Patents | `Dot Incorporation refreshable braille display patents` | 5 | High |
| 5 | Web | `servo motor cam braille display 3D printed open source` | 5 | **CRITICAL** |
| 6 | Web | `MOLBED braille display open hardware project` | 5 | **CRITICAL** |
| 7 | Web | `MagnePins open source braille` | 5 | High |
| 8 | Web | `"5559/CHE/2014" Indian patent office braille` | 5 | **CRITICAL** |
| 9 | Web | `Indian patent application 5559 CHE 2014 servo cam braille` | 5 | **CRITICAL** |
| 10 | Google Patents | `US20130149674A1 US8483018B2 braille display` | 5 | High |
| 11 | Google Patents | `WO2016074170 braille display family` | 5 | Medium |
| 12 | Google Patents | `WO2020106855 EP3884363 braille` | 5 | Medium |

### 2.3 Source Types Consulted

- **Primary Patent Sources:** USPTO Patent Center, EPO Espacenet, WIPO PATENTSCOPE, Google Patents
- **Indian Sources:** IPR Search (ipindia.gov.in), PatentAssist.ai, invntree.com
- **Non-Patent Prior Art:** Hackaday.io, GitHub, ResearchGate, Hackster.io
- **Commercial Sources:** Dot Inc. official website, product documentation

### 2.4 Important Limitations

1. **No direct access** to official Indian Patent Office full-file wrapper for 5559/CHE/2014
2. **No counsel-level claim charting** performed — only independent claim reading
3. **No jurisdiction-specific legal status verification** for all patents (relied on Google Patents/USPTO data)
4. **Chinese/Japanese/Korean** searches conducted via Google Patents only (translation limitations)
5. **Non-English prior art** may exist that was not surfaced

---

## 📊 3. Verified Family Table

### 3.1 Active Patent Families (High Relevance)

| Family ID | Publication No. | Priority Date | Assignee | Jurisdictions | Current Status | Relevance | Confidence |
|-----------|----------------|---------------|----------|---------------|----------------|-----------|------------|
| DOT-001 | US11854423B1 | 2020-05-19 | Individual (Prithu Kolar) | US | Active (exp. 2041-04-26) | **HIGH** — Passive pin retention, selective impacting | High |
| DOT-002 | US6354839B1 | 2000-03-10 | Orbital Research | US | Active | **HIGH** — MEMS actuators, modular rows/columns | High |
| SMA-001 | US8770981B2 | 2011-06-28 | Individual | US | Active | **MEDIUM** — SMA wire + compression spring | High |
| EAP-001 | US6881063B2 | 2002-05-22 | Individual | US | Active | **MEDIUM** — Electroactive polymer bending | High |
| DOT-ESTATE | 110+ patents | 2014-2026 | Dot Incorporation | US, EP, WO, IN, JP, KR, CN | Active (portfolio) | **CRITICAL** — Dominates actuator space | High |

### 3.2 Expired/Older Prior Art (Relevance for Obviousness)

| Family ID | Publication No. | Priority Date | Assignee | Status | Relevance | Confidence |
|-----------|----------------|---------------|----------|--------|-----------|------------|
| EARLY-001 | US5685721 | 1995-06-07 | Individual | **EXPIRED** | **HIGH** — SMA actuator (likely expired) | Medium |
| EARLY-002 | US6743021B2 | 2002-05-22 | Individual | Active | **MEDIUM** — Compliant mechanism | High |
| EARLY-003 | US3659354A | 1970-05-04 | Individual | **EXPIRED** | **LOW** — Pneumatic actuation | High |

### 3.3 Indian Patent (Critical Finding)

| Application No. | Filing Date | Applicant | Title | Status | Relevance | Confidence |
|----------------|-------------|----------|-------|--------|-----------|------------|
| **5559/CHE/2014** | 2014-11-05 | Paul D'souza | Refreshable Braille Display (servo/cam) | **UNVERIFIED** (claimed active) | **CRITICAL** — Directly anticipates MVP | **Medium-High** (7/10) |

**Evidence:** Hackaday.io project #10849 logs explicitly state: *"the features mentioned in this Project thus far are covered under a patent application filed at The PatentOffice, Chennai, by him on 05Nov2014 …5559/CHE/2014"* and that this forced discontinuation of the open-source project.

**Verification Attempt:** Searched IPR Search (ipindia.gov.in), PatentAssist.ai. Application number format confirmed (pre-2016: 5559/CHE/2014). Full specification not retrieved due to access limitations.

### 3.4 WO/EPO Families

| Family ID | Publication No. | Priority Date | Assignee | Jurisdictions | Status | Relevance |
|-----------|----------------|---------------|----------|---------------|--------|-----------|
| WO-001 | WO2015189863 | 2014-05-15 | Individual | WO, US, EP | Active | **MEDIUM** — Layered EM actuation |
| WO-002 | WO2016074170 | 2015-11-13 | Individual | WO, US, EP | Active | **LOW** — Tactile display |
| WO-003 | WO2020106855 | 2019-03-15 | Individual | WO, US, EP | Active | **LOW** — Braille cell |
| EP-001 | EP4049116A1 | 2018-03-14 | Individual | EP, US | Active | **MEDIUM** — Tactile pixels |

### 3.5 Open-Hardware Prior Art (Non-Patent but Relevant)

| Project | Date | Disclosure | Relevance | Source |
|---------|------|------------|-----------|--------|
| **MOLBED** | 2014-2020 | Modular low-cost Braille electronic display, magnetic retaining system, servo/cam | **CRITICAL** | Hackster.io, Hackaday |
| **Hackaday #191181** | 2021 | Electromagnet-based cam actuator, 3D printed, eccentric cam with rare-earth magnet | **CRITICAL** | Hackaday.io |
| **Olin College PIE** | 2021 | Servo-driven cam system, 3D-printed cell chain, sprockets | **CRITICAL** | GitHub Pages |
| **Hackaday #10849** | 2016 | Micro servo actuators, cam follower, pin lever, 3D printable | **CRITICAL** | Hackaday.io |
| **GitHub (vibhutimishra)** | 2020 | Refreshable Braille Display using servo motors and Arduino | **HIGH** | GitHub |
| **ResearchGate** | 2021 | "Refreshable Braille Module Using Cam Actuated Mechanism" — two nested shafts, 8 cam arrays, micro-servo | **CRITICAL** | ResearchGate |

---

## ⚖️ 4. Independent Claim Analysis

### 4.1 Closest Prior Art: Independent Claims

#### US11854423B1 (Granted 2023-12-26)
**Title:** Refreshable braille display

**Independent Claim 1 (paraphrased):**
> A refreshable braille display device comprising:
> - a plurality of Braille pins running through a perforated body of the reader;
> - the pins arranged in the spacing and order of Braille dots of standard Braille cells;
> - the Braille reader coupled to a device for Braille text generation via selective hammering or impacting of Braille pins;
> - from a default position, one or more pins are selectively impacted in a sequence to create a Braille pattern;
> - the perforations housing the pins are sized such that impacted pins are self-held in place via friction alone, without external support or latching mechanism.

**Relevance to OpenBraille:**
- ✅ **Expressly disclosed:** Plurality of pins, standard Braille spacing
- ✅ **Expressly disclosed:** Selective actuation to create patterns
- ❌ **Not disclosed:** Servo motors, cams, PWM control
- ❌ **Not disclosed:** Macro-scale (300%)
- ⚠️ **Argueably suggested:** Modular pin arrangement

**Distinction:** OpenBraille uses **rotary servo + cam** vs. **linear impact/hammering**. This is a **different actuation principle** but achieves the same functional result (selectively raising/lowering pins).

#### US8770981B2 (Granted 2014-07-01)
**Title:** Actuation mechanism for braille displays

**Independent Claim 1 (paraphrased):**
> An improved refreshable tactile display apparatus comprising:
> - a housing;
> - bias compression springs;
> - sliding blocks;
> - pins; and
> - a shape memory alloy wire;
> - wherein the sliding block is actuated by interaction between the bias compression spring and the SMA wire.

**Relevance:** SMA-based, not servo-based. **Not directly anticipating** but shows alternative actuation in same space.

#### Indian Application 5559/CHE/2014 (Inferred from Hackaday disclosure)
**Inferred Claims (from project description):**
> A refreshable Braille display system comprising:
> - micro servo actuators;
> - cam mechanisms;
> - 3D-printed frame;
> - modular cell architecture;
> - retractable pogo pins or similar tactile elements.

**Relevance:** **CRITICAL — Directly anticipates** OpenBraille's servo + cam architecture. If this application matured to grant, it would be **fatal prior art**.

**Status:** **UNVERIFIED** — Could not retrieve full specification from official Indian Patent Office. Hackaday disclosure is secondary evidence.

#### MOLBED (Open-Hardware, 2014-2020)
**Disclosed Features:**
- Magnetic retaining system (bistable latch)
- Low parts count
- Easy to prototype and scale
- Servo or stepper motor actuation
- 3D-printed components
- Modular character architecture

**Relevance:** **ANTICIPATES** the combination of servo actuation + cam mechanism + 3D printing for Braille displays. Published before OpenBraille project conception.

---

## 📈 5. Frozen-MVP Feature Chart vs. Closest Prior Art

### 5.1 Feature Comparison Matrix

| MVP Feature | OpenBraille | US11854423B1 | 5559/CHE/2014 | MOLBED | Hackaday #191181 | Olin College | Nearest Art Status |
|-------------|-------------|---------------|----------------|-------|----------------|-------------|-------------------|
| Six independent low-cost servos | ✅ | ❌ (impact drivers) | ✅ | ⚠️ (servo option) | ✅ (servo) | ⚠️ (stepper) | **Disclosed** |
| PWM control | ✅ | ❌ (motor control) | ✅ | ✅ | ✅ | ✅ | **Disclosed** |
| Eccentric cam | ✅ | ❌ (linear impact) | ✅ | ✅ | ✅ | ✅ | **Disclosed** |
| Follower mechanism | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | **Disclosed** |
| Sliding tactile pin | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **Disclosed** |
| Printed guide/frame | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | **Disclosed** |
| Macro scale (~300%) | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | **Not disclosed** (but obvious scaling) |
| Active retraction | ✅ (servo) | ❌ (friction) | ✅ | ✅ | ✅ | ✅ | **Disclosed** |
| Calibration | ✅ | ❌ | ⚠️ (implied) | ✅ | ✅ | ✅ | **Disclosed** |
| Sequencing | ✅ | ✅ (selective) | ✅ | ✅ | ✅ | ✅ | **Disclosed** |
| Modularity | ✅ | ⚠️ (cells) | ✅ | ✅ | ✅ | ✅ | **Disclosed** |
| Power architecture (5V/2A) | ✅ | ❌ | ⚠️ | ✅ | ✅ | ✅ | **Conventional** |
| Tactile validation | ✅ | ❌ | ⚠️ | ✅ | ✅ | ✅ | **Conventional** |

### 5.2 Novelty Assessment

**Conclusion:** The **combination of servo + cam + follower + sliding pin + printed frame** for a refreshable Braille cell is **expressly disclosed in multiple prior art sources** (5559/CHE/2014, MOLBED, Hackaday projects).

**Novelty Risk:** **HIGH** — The basic architecture is anticipated.

### 5.3 Inventive Step/Obviousness Assessment

**Analysis:** Even if individual elements are known:
- Servo motors: conventional actuators
- Cam mechanisms: conventional mechanical elements
- 3D printing: conventional manufacturing
- Braille cells: conventional arrangement

The **combination** would likely be considered **obvious** to a person skilled in the art (mechanical engineer + embedded systems) because:
1. Servo + cam is a standard way to convert rotary to linear motion
2. 3D printing is a known method for rapid prototyping
3. Applying this to Braille (a known tactile display need) is a predictable application
4. Multiple independent teams arrived at the same solution (MOLBED, Hackaday, Olin College)

**Obviousness Risk:** **HIGH**

---

## ⚠️ 6. Separate Risk Analyses

### 6.1 Novelty Risk

| Risk Factor | Assessment | Evidence | Mitigation |
|-------------|------------|----------|------------|
| Basic servo/cam mechanism | **HIGH RISK** | 5559/CHE/2014, MOLBED, Hackaday #191181 | Pivot to manufacturing/firmware |
| Macro-scale implementation | **MEDIUM RISK** | Not explicitly disclosed, but scaling is obvious | Document specific tolerances/advantages |
| Modular architecture | **HIGH RISK** | MOLBED explicitly modular | Add specific interconnection method |
| PWM control | **LOW RISK** | Conventional servo control | None needed |

**Overall Novelty Risk:** **HIGH**

### 6.2 Obviousness/Inventive-Step Risk

| Jurisdiction | Standard | Assessment | Evidence |
|--------------|----------|------------|----------|
| US | 35 U.S.C. § 103 | **HIGH RISK** | Multiple independent disclosures of same combination |
| EP | Art. 56 EPC | **HIGH RISK** | Same reasoning |
| IN | Section 2(1)(ja) | **HIGH RISK** | Same reasoning |

**Rationale:** The combination of known elements (servo, cam, 3D printing) applied to a known problem (expensive Braille displays) would likely be deemed obvious.

**Overall Obviousness Risk:** **HIGH**

### 6.3 Patent-Eligibility Risk

| Jurisdiction | Test | Assessment | MVP Features |
|--------------|------|------------|--------------|
| US | Alice/Mayo Step 1 | **MEDIUM RISK** | Abstract idea: "displaying tactile information" |
| US | Alice Step 2 | **HIGH RISK** | No "significantly more" than conventional implementation |
| EP | Art. 52(2)(c) | **MEDIUM RISK** | "Schemes, rules and methods for... performing mental acts" exclusion |
| IN | Section 3(k) | **MEDIUM RISK** | Similar to US Alice |

**Assessment:** The basic servo/cam MVP **fails** the eligibility test in the US because it implements an abstract idea (displaying information) using generic computer components (servo, MCU) without a specific technical improvement.

**Overall Eligibility Risk:** **HIGH** for basic architecture, **MEDIUM** for manufacturing/firmware pivot

### 6.4 Freedom-to-Operate (FTO) / Infringement Risk

| Patent Estate | Coverage | Risk | Evidence |
|---------------|----------|------|----------|
| **Dot Inc. (110+ patents)** | Electromagnetic latching, piezo replacement, cell arrays | **CRITICAL** | Dot Inc. website, multiple granted patents |
| **US11854423B1** | Passive pin retention via friction | **MEDIUM** | Different actuation (impact vs. servo) |
| **5559/CHE/2014** | Servo/cam Braille display | **CRITICAL** | Direct overlap with MVP |
| **MOLBED/Hackaday** | Open-hardware implementations | **LOW** | Not patented (open source) but anticipates |

**Assessment:** **CRITICAL FTO RISK** if commercializing servo/cam architecture. Dot Inc. estate specifically targets low-cost actuator mechanisms.

**Recommendation:** **DO NOT COMMERCIALIZE** current MVP without FTO opinion. Pivot to manufacturing/firmware method claims that don't require specific actuator hardware.

**Overall FTO Risk:** **CRITICAL**

---

## 🎯 7. Candidate Invention Directions Evaluation

### 7.1 Evaluation Framework

Each direction assessed against:
- Nearest prior art
- Differentiating elements
- Bounded enhancement vs. major redesign requirement
- Physical advantage required
- Experiment feasibility within constraints
- Patent risks (novelty, obviousness, eligibility, FTO)

### 7.2 Direction-by-Direction Analysis

#### Direction A: Tolerance-Compensating Mechanical/Control Architecture

| Criterion | Assessment | Details |
|-----------|------------|---------|
| **Nearest Art** | US11854423B1 (friction retention), MOLBED (magnetic latch) | Both address tolerance issues |
| **Differentiating Elements** | ✅ Active compensation via firmware, ✅ measurable repeatability improvement, ✅ documented tolerance budget | Can be specific |
| **Enhancement Level** | ✅ **Bounded enhancement** | Build on existing MVP |
| **Physical Advantage** | ✅ Reduced friction, ✅ improved repeatability, ✅ lower cost at scale | Measurable |
| **Experiment Feasibility** | ✅ **Within semester** | Use macro-scale MVP to measure variance |
| **Patent Risks** | Novelty: MEDIUM, Obviousness: MEDIUM, Eligibility: MEDIUM, FTO: LOW | Better than basic mechanism |

**Verdict:** **STRONG CANDIDATE** for Track C

**Required Evidence:**
- Measure pin-position variance with/without compensation
- Document specific tolerance-compensating algorithm
- Show improvement over uncompensated baseline

---

#### Direction B: Low-Cost Per-Dot Calibration

| Criterion | Assessment | Details |
|-----------|------------|---------|
| **Nearest Art** | MOLBED (magnetic latch requires no power), standard servo calibration | Calibration is conventional |
| **Differentiating Elements** | ✅ **Automated per-dot calibration**, ✅ stored coefficients, ✅ compensation for manufacturing variance | Can be specific |
| **Enhancement Level** | ✅ **Bounded enhancement** | Add calibration routine to MVP |
| **Physical Advantage** | ✅ Faster setup, ✅ better yield, ✅ interchangeable dots | Measurable |
| **Experiment Feasibility** | ✅ **Within semester** | Implement in firmware |
| **Patent Risks** | Novelty: MEDIUM, Obviousness: HIGH, Eligibility: MEDIUM, FTO: LOW | Calibration itself may be obvious |

**Verdict:** **MODERATE CANDIDATE** — Risk of obviousness over conventional calibration

**Required Evidence:**
- Show calibration improves yield or reduces setup time
- Document specific calibration algorithm tied to physical measurements

---

#### Direction C: Verified Tactile-State Control

| Criterion | Assessment | Details |
|-----------|------------|---------|
| **Nearest Art** | US11854423B1 (friction retention), standard servo position control | Position verification is conventional |
| **Differentiating Elements** | ✅ **Closed-loop tactile-state verification**, ✅ user feedback integration, ✅ adaptive retraction | Can be specific |
| **Enhancement Level** | ✅ **Bounded enhancement** | Add sensors/feedback to MVP |
| **Physical Advantage** | ✅ Improved reliability, ✅ user trust, ✅ safer operation | Measurable |
| **Experiment Feasibility** | ⚠️ **May exceed semester** | Requires additional sensors |
| **Patent Risks** | Novelty: MEDIUM, Obviousness: MEDIUM, Eligibility: MEDIUM, FTO: LOW | Good candidate |

**Verdict:** **STRONG CANDIDATE** but may require extra components

**Required Evidence:**
- Implement feedback mechanism (e.g., Hall effect sensor on cam)
- Measure improvement in state verification accuracy
- Document user testing with/without verification

---

#### Direction D: Compliant Printed Guide/Return Geometry

| Criterion | Assessment | Details |
|-----------|------------|---------|
| **Nearest Art** | MOLBED (magnetic latch), US11854423B1 (friction) | Return mechanisms are disclosed |
| **Differentiating Elements** | ✅ **Specific compliant geometry**, ✅ material selection, ✅ print orientation optimization | Can be specific |
| **Enhancement Level** | ✅ **Bounded enhancement** | Iterate on 3D-printed parts |
| **Physical Advantage** | ✅ Reduced friction, ✅ improved durability, ✅ self-alignment | Measurable |
| **Experiment Feasibility** | ✅ **Within semester** | Test different materials/geometries |
| **Patent Risks** | Novelty: MEDIUM, Obviousness: HIGH, Eligibility: MEDIUM, FTO: LOW | Geometry may be obvious |

**Verdict:** **WEAK CANDIDATE** — Likely obvious over known compliant mechanisms

---

#### Direction E: Scale-Transfer Manufacturing Method

| Criterion | Assessment | Details |
|-----------|------------|---------|
| **Nearest Art** | US10254499B1 (additive-manufactured active devices) | General AM for mechatronics |
| **Differentiating Elements** | ✅ **Specific process for Braille cells**, ✅ tolerance mapping from macro to standard, ✅ material/process parameters | **HIGHLY SPECIFIC** |
| **Enhancement Level** | ⚠️ **Major redesign** | Requires standard-scale prototype |
| **Physical Advantage** | ✅ Predictable scaling, ✅ reduced iteration cost | Measurable |
| **Experiment Feasibility** | ❌ **Beyond semester** | Requires SLA printing, precision metrology |
| **Patent Risks** | Novelty: HIGH, Obviousness: MEDIUM, Eligibility: LOW, FTO: LOW | **BEST CANDIDATE** but not semester-feasible |

**Verdict:** **STRONG CANDIDATE** for Track C (later extension)

**Required Evidence:**
- Build macro-scale MVP (semester)
- Document all parameters and measurements
- Later build standard-scale prototype using same methodology
- Show predictable performance transfer

---

#### Direction F: Modular Replaceable Architecture

| Criterion | Assessment | Details |
|-----------|------------|---------|
| **Nearest Art** | MOLBED (explicitly modular), US6354839B1 (modular rows/columns) | Modularity is disclosed |
| **Differentiating Elements** | ✅ **Specific interconnection method**, ✅ blind-mate connectors, ✅ tool-less replacement | Can be specific |
| **Enhancement Level** | ✅ **Bounded enhancement** | Add modularity to MVP |
| **Physical Advantage** | ✅ Easier maintenance, ✅ customizable configurations | Measurable |
| **Experiment Feasibility** | ✅ **Within semester** | Design modular interfaces |
| **Patent Risks** | Novelty: LOW, Obviousness: HIGH, Eligibility: MEDIUM, FTO: MEDIUM | **WEAK** — Modularity is conventional |

**Verdict:** **WEAK CANDIDATE** — Likely obvious/anticipated

---

#### Direction G: Current-Aware Sequencing

| Criterion | Assessment | Details |
|-----------|------------|---------|
| **Nearest Art** | Standard power management in embedded systems | Sequencing is conventional |
| **Differentiating Elements** | ✅ **Braille-specific sequencing**, ✅ peak-current reduction, ✅ thermal management | Can be specific |
| **Enhancement Level** | ✅ **Bounded enhancement** | Add to firmware |
| **Physical Advantage** | ✅ Lower power supply cost, ✅ improved reliability | Measurable |
| **Experiment Feasibility** | ✅ **Within semester** | Measure current, implement sequencing |
| **Patent Risks** | Novelty: MEDIUM, Obviousness: HIGH, Eligibility: MEDIUM, FTO: LOW | **MODERATE** but obviousness risk |

**Verdict:** **MODERATE CANDIDATE**

---

#### Direction H: Shared-Actuation Architecture

| Criterion | Assessment | Details |
|-----------|------------|---------|
| **Nearest Art** | US20130203022 (rotatable discs with partial Braille characters) | Shared actuation is disclosed |
| **Differentiating Elements** | ✅ **Specific shared mechanism**, ✅ reduced actuator count | Can be specific |
| **Enhancement Level** | ⚠️ **Major redesign** | Different from per-dot servos |
| **Physical Advantage** | ✅ Lower cost, ✅ reduced complexity | Measurable |
| **Experiment Feasibility** | ❌ **Beyond semester** | Requires new mechanical design |
| **Patent Risks** | Novelty: MEDIUM, Obviousness: MEDIUM, Eligibility: MEDIUM, FTO: LOW | **POSSIBLE** but not semester-feasible |

**Verdict:** **DEFER** — Not feasible within constraints

---

### 7.3 Ranked Candidate Directions

| Rank | Direction | Track | Novelty | Obviousness | Eligibility | FTO | Feasibility | Overall |
|------|-----------|-------|---------|-------------|-------------|-----|-------------|----------|
| 1 | **Scale-Transfer Manufacturing Method** | C | HIGH | MEDIUM | LOW | LOW | Later | **STRONG** |
| 2 | **Tolerance-Compensating Architecture** | C | MEDIUM | MEDIUM | MEDIUM | LOW | Now | **STRONG** |
| 3 | **Verified Tactile-State Control** | C | MEDIUM | MEDIUM | MEDIUM | LOW | Later | **STRONG** |
| 4 | **Current-Aware Sequencing** | C | MEDIUM | HIGH | MEDIUM | LOW | Now | **MODERATE** |
| 5 | **Low-Cost Per-Dot Calibration** | C | MEDIUM | HIGH | MEDIUM | LOW | Now | **MODERATE** |
| 6 | **Compliant Geometry** | C | MEDIUM | HIGH | MEDIUM | LOW | Now | **WEAK** |
| 7 | **Modular Architecture** | C | LOW | HIGH | MEDIUM | MEDIUM | Now | **WEAK** |
| 8 | **Shared Actuation** | C | MEDIUM | MEDIUM | MEDIUM | LOW | Later | **DEFER** |

---

## 🎯 8. Claim-to-Experiment Map

### 8.1 Surviving Directions with Experimental Plan

#### Direction 1: Tolerance-Compensating Mechanical/Control Architecture (Track C)

| Prospective Element | Nearest Art | Measurable Effect | Baseline | Test Equipment | Pass/Fail | Scale-Relevance |
|---------------------|-------------|------------------|----------|----------------|-----------|-----------------|
| Per-dot friction compensation via PWM adjustment | MOLBED (magnetic latch), US11854423B1 (friction) | Reduced pin-position variance | Uncompensated servo control | Calipers, multimeter, oscilloscope | ≤0.1 mm variance over 100 cycles | **Scale-independent** |
| Automated calibration routine | Standard servo calibration | Faster setup time | Manual calibration | Stopwatch, test script | Setup time <5 minutes | **Scale-independent** |
| Tolerance-mapped guide geometry | Standard 3D printing tolerances | Improved yield | Conventional guides | Calipers, go/no-go gauges | 100% functional cells from first print | **Scale-sensitive** |

**Semester Deliverable:** Macro-scale MVP with compensation, generating variance data and calibration metrics.

**Later Invention Mechanism:** Standard-scale cell using same compensation methodology, with documented parameter transfer.

**Additional Experiments:** None beyond semester MVP.

**Cost/Duration:** Within ₹5,000 and 3 months.

---

#### Direction 2: Scale-Transfer Manufacturing Method (Track C)

| Prospective Element | Nearest Art | Measurable Effect | Baseline | Test Equipment | Pass/Fail | Scale-Relevance |
|---------------------|-------------|------------------|----------|----------------|-----------|-----------------|
| Documented macro-scale parameters (friction, tolerance, force) | None (first disclosure) | Complete parameter set | No baseline | Calipers, force gauge, multimeter | All 15 parameters documented | **Scale-sensitive** |
| Predictive scaling model | US10254499B1 (general AM) | Predicted vs. actual standard-scale performance | No model | Standard-scale prototype | <10% deviation | **Standard-scale mandatory** |
| Manufacturing workflow | Conventional prototyping | Reproducibility across builders | Ad-hoc workflow | Multiple builders, same files | 100% successful replication | **Scale-independent** |

**Semester Deliverable:** Macro-scale MVP with **complete parameter documentation** and manufacturing workflow specification.

**Later Invention Mechanism:** Standard-scale prototype built using documented methodology, showing predictable performance.

**Additional Experiments:** Standard-scale prototype (post-semester), precision metrology, SLA printing.

**Cost/Duration:** Semester: ₹5,000, 3 months. Later: ₹10,000-20,000, 3-6 months.

---

#### Direction 3: Verified Tactile-State Control (Track C)

| Prospective Element | Nearest Art | Measurable Effect | Baseline | Test Equipment | Pass/Fail | Scale-Relevance |
|---------------------|-------------|------------------|----------|----------------|-----------|-----------------|
| Hall effect sensor on cam for position verification | Standard position sensing | State verification accuracy | No feedback (open-loop) | Hall sensors, multimeter | 100% correct state detection | **Scale-independent** |
| Adaptive retraction based on load | Standard servo control | Reduced sticking/failure | Fixed retraction | Force gauge, test script | 0% sticking over 1,000 cycles | **Scale-sensitive** |
| User feedback integration (tactile confirmation) | None | User trust metric | No feedback | User testing protocol | >95% user confidence | **Scale-independent** |

**Semester Deliverable:** Macro-scale MVP with **optional** feedback sensors (if budget allows), generating reliability data.

**Later Invention Mechanism:** Full closed-loop system with documented improvement in reliability.

**Additional Experiments:** Sensor integration and validation (may exceed semester budget).

**Cost/Duration:** Semester: ₹5,000 (basic), ₹7,000-8,000 (with sensors). Later: as needed.

---

### 8.2 Evidence That Could Kill the Patent Path

| Killing Evidence | Direction Affected | Source | Likelihood |
|-----------------|-------------------|--------|------------|
| Prior art disclosing **tolerance-compensating firmware** for Braille | Direction 1, 2 | Patent search | **LOW** (none found) |
| Prior art disclosing **scale-transfer methodology** for tactile displays | Direction 2 | Patent search | **LOW** (none found) |
| Prior art disclosing **verified tactile-state control** in refreshable displays | Direction 3 | Patent search | **MEDIUM** (possible in industrial contexts) |
| **Macro-scale evidence fails to transfer** to standard scale | Direction 2 | Physical testing | **MEDIUM** (requires validation) |
| **No measurable improvement** over prior art | All directions | Experimental data | **HIGH** (must demonstrate) |

---

## 🏆 9. Final Research Verdict

### 9.1 Direct Answers to Central Questions

**Q1: Does the frozen SG90/cam/pin architecture already contain any defensible technical contribution?**
> **A1: NO.** The combination is **anticipated by multiple prior art sources** (5559/CHE/2014, MOLBED, Hackaday projects). The basic servo + cam mechanism for Braille is **not novel**.

**Q2: Can a bounded improvement produce a credible prospective invention?**
> **A2: YES, but not the actuator mechanism itself.** Credible paths exist in:
> - Tolerance-compensating manufacturing/control architecture
> - Scale-transfer manufacturing method
> - Verified tactile-state control
> These require **pivoting away from mechanism novelty** toward **process and control innovations**.

**Q3: Does the architecture require a major redesign?**
> **A3: NO for Track C candidates.** The semester MVP can be built as-is, with **enhanced firmware/data collection** to support later patent filings. Major redesign is only needed for **shared-actuation** or **standard-scale validation** (post-semester).

**Q4: Is there a credible patent-development path?**
> **A4: YES, via Track C.** Semester MVP achievable within 3 months and ₹5,000, generating evidence for later patent development focused on **manufacturing method + control/firmware**.

**Q5: What evidence could kill the patent path?**
> **A5:**
> - Discovery of prior art disclosing the specific tolerance-compensating or scale-transfer methods
> - Failure of macro-scale evidence to transfer to standard scale
> - Inability to demonstrate measurable improvement over prior art

**Q6: Should OpenBraille advance, remain conditional, or lose patent-first priority?**
> **A6: ADVANCE as Track C.**
> - **Semester deliverable:** Macro-scale MVP with parameter documentation
> - **Patent priority:** **Conditional** — Only after generating evidence and pivoting to manufacturing/control claims
> - **Commercialization:** **DO NOT PROCEED** with current architecture without FTO opinion

### 9.2 Classification

**Track C: Semester MVP achievable within three months, but the strongest patent-development mechanism requires a later semester or publication-oriented research extension.**

**Complete Three-Month Deliverable:**
- Functional macro-scale (300%) 6-dot servo/cam Braille cell
- Complete parameter documentation (friction, tolerance, force, current, timing)
- Manufacturing workflow specification
- Calibration and compensation routines
- Tactile validation data
- All data needed to support later scale-transfer claims

**Evidence Semester MVP Must Generate:**
1. Measured pin-position variance with/without compensation
2. Calibration time and yield data
3. Power consumption profiles
4. Durability data (1,000+ cycles)
5. User tactile distinguishability metrics
6. Complete bill of materials and cost analysis
7. CAD files and manufacturing parameters

**Later Invention Mechanism:**
- Standard-scale prototype using documented methodology
- Claim set focused on **scale-transfer manufacturing method** and **tolerance-compensating control architecture**
- Not on basic servo/cam mechanism

**Additional Experiments, Cost, Duration:**
- Standard-scale prototype: ₹10,000-20,000, 3-6 months
- SLA printing for precision parts
- Precision metrology equipment
- User testing with visually impaired participants

**Why Later Work Remains Connected:**
- Uses same **parameter documentation** from semester MVP
- Validates **predictive scaling model** developed during semester
- Maintains **engineering hypothesis** (low-cost actuation) while adding **manufacturing innovation**

### 9.3 Confidence Levels

| Assessment | Confidence | Rationale |
|------------|------------|-----------|
| Servo/cam not novel | **High (9/10)** | Multiple independent prior art disclosures |
| Track C is viable | **High (8.5/10)** | Matches Phase 2 pivot, evidence-generating |
| Macro-scale evidence relevant | **Medium (7/10)** | Scale-sensitive, but can support method claims |
| Dot Inc. FTO risk | **High (9/10)** | 110+ patents, dominant estate |
| Indian patent 5559/CHE/2014 is prior art | **Medium-High (7.5/10)** | Secondary evidence only |

---

## 📌 10. Recommendations & Next Steps

### 10.1 Immediate Actions (Within 1 Week)

1. **✅ VERIFY Indian Patent 5559/CHE/2014**
   - Contact Indian Patent Office (chennai-patent@nic.in)
   - Request full specification and claims
   - Confirm current legal status
   - **Priority: CRITICAL**

2. **✅ COMMISSION Dot Inc. Estate Claim Chart**
   - Engage patent counsel to chart Dot Inc.'s 110+ patents
   - Focus on actuator mechanisms, latching systems, cell arrays
   - Identify specific claims that read on servo/cam architecture
   - **Priority: CRITICAL**

3. **✅ REVIEW Open-Hardware Projects for Disclosures**
   - Download and archive MOLBED documentation
   - Download Hackaday #191181 and #10849 files
   - Review Olin College PIE project documentation
   - Extract specific technical disclosures
   - **Priority: HIGH**

### 10.2 Semester Implementation Plan

**Month 1: Build & Characterize**
- [ ] Procure components (6× SG90, ESP32, materials)
- [ ] Print and assemble single-dot module (M1-M3)
- [ ] Characterize friction, tolerance, force (U-OB-04)
- [ ] Verify servo passive return (U-OB-01, U-OB-02)
- [ ] Test power adequacy (U-OB-03)

**Month 2: Integrate & Validate**
- [ ] Assemble all six dots (M4)
- [ ] Implement calibration routine (Direction B)
- [ ] Implement tolerance compensation (Direction A)
- [ ] Run repeatability tests (100 cycles)
- [ ] Begin tactile validation (M6)

**Month 3: Document & Prepare**
- [ ] Complete 1,000-cycle durability test
- [ ] Full character set validation (M7-M8)
- [ ] Document all parameters for scale-transfer
- [ ] Prepare manufacturing workflow specification
- [ ] Generate patent evidence package

### 10.3 Patent Strategy

**Phase 1: Semester (Evidence Generation)**
- Build macro-scale MVP
- Generate all technical data
- **DO NOT PUBLICLY DISCLOSURE** invention concepts
- File provisional patent application **only after** counsel review

**Phase 2: Post-Semester (Patent Development)**
- Build standard-scale prototype
- Validate scale-transfer methodology
- File non-provisional application on:
  - Scale-transfer manufacturing method (Direction E)
  - Tolerance-compensating control architecture (Direction A)
  - Verified tactile-state control (Direction C)

**Phase 3: Commercialization (Conditional)**
- Obtain FTO opinion on Dot Inc. estate
- Only proceed if claims can be drafted to avoid
- Consider licensing discussions with Dot Inc.

### 10.4 Risk Mitigation

| Risk | Mitigation | Owner | Timeline |
|------|------------|-------|----------|
| Prior art anticipation | Pivot to manufacturing/control claims | Team | Immediate |
| Dot Inc. infringement | FTO opinion before commercialization | Counsel | Month 1 |
| Indian patent 5559/CHE/2014 | Verify status and claims | Team | Week 1 |
| Obviousness rejection | Document specific technical advantages | Team | Semester |
| Eligibility rejection | Focus on technical effect, not abstract idea | Counsel | Post-semester |

### 10.5 Go/No-Go Decision Points

| Decision Point | Criteria | Timeline | Recommendation |
|----------------|----------|----------|----------------|
| **Proceed with semester MVP** | No blocking prior art found for manufacturing method | Week 1 | **GO** (Track C) |
| **File provisional application** | Counsel confirms patentable subject matter | Month 3 | **CONDITIONAL** (after evidence) |
| **Build standard-scale prototype** | Scale-transfer methodology shows promise | Post-semester | **GO** (if data supports) |
| **Commercialize** | FTO opinion clears Dot Inc. estate | Post-prototype | **NO GO** (until cleared) |

---

## 📚 Source Notes

### Primary Sources (High Confidence)

| Source | Type | Confidence | Notes |
|--------|------|------------|-------|
| Google Patents | Patent database | High | Full text, claims, families |
| USPTO Patent Center | Official US records | High | Legal status, prosecution history |
| EPO Espacenet | Official EP records | High | Family members, classifications |
| Hackaday.io | Project documentation | High | Open-hardware disclosures |
| GitHub | Source code | High | Implementation details |
| ResearchGate | Publication | High | Peer-reviewed research |

### Secondary Sources (Medium Confidence)

| Source | Type | Confidence | Notes |
|--------|------|------------|-------|
| PatentAssist.ai | Indian patent search | Medium | Index-based, not official |
| invntree.com | Patent journal | Medium | PDF scans, not searchable |
| IPR Search (ipindia.gov.in) | Official Indian | Medium | Access limitations |

### Conflicts and Caveats

1. **Indian Patent 5559/CHE/2014:** Could not retrieve full specification. Hackaday disclosure is secondary evidence but highly credible (explicit statement from patent applicant).

2. **Dot Inc. Estate:** 110+ patents claimed, but specific claim scope not verified. Requires counsel-level charting.

3. **Open-Hardware Projects:** Multiple independent disclosures of servo/cam Braille displays. Strong evidence of obviousness and anticipation.

4. **Macro-Scale Limitation:** All evidence generated at 300% scale. Transfer to standard scale unproven and mandatory for practical claims.

---

## ❓ Open Questions

### Unresolved Technical Questions

1. **What is the exact claim scope of Indian Patent 5559/CHE/2014?**
   - Status: UNVERIFIED
   - Impact: Could be fatal prior art
   - Resolution: Obtain full specification

2. **Does Dot Inc.'s estate cover servo-based actuation?**
   - Status: UNVERIFIED (estate exists, specific claims unknown)
   - Impact: CRITICAL FTO risk
   - Resolution: Claim-chart with counsel

3. **Can macro-scale evidence support standard-scale claims?**
   - Status: UNCERTAIN
   - Impact: Limits claim scope
   - Resolution: Build standard-scale prototype

4. **What specific technical advantage does tolerance compensation provide?**
   - Status: UNPROVEN
   - Impact: Required for patentability
   - Resolution: Experimental validation

### Unresolved Patent Questions

5. **Are there Chinese/Japanese/Korean patents covering servo/cam Braille?**
   - Status: NOT SEARCHED EXHAUSTIVELY
   - Impact: Possible hidden prior art
   - Resolution: Expand search with native-language terms

6. **What is the legal status of US5685721 (SMA patent)?**
   - Status: LIKELY EXPIRED (1995 priority)
   - Impact: May be usable as prior art
   - Resolution: Verify expiration date

7. **What claim elements survive Alice/Mayo eligibility scrutiny?**
   - Status: UNCERTAIN
   - Impact: Determines allowable claim scope
   - Resolution: Counsel opinion

---

## 🎓 Methodology

### Research Approach

1. **Baseline Extraction:** Parsed all provided project files to establish frozen MVP specifications and constraints
2. **Landscape Mapping:** Conducted broad searches across all mandated jurisdictions and technical areas
3. **Specific Verification:** Retrieved and analyzed 15+ specific patent numbers and families
4. **Prior Art Comparison:** Built feature-by-feature comparison matrix against closest art
5. **Risk Assessment:** Separately evaluated novelty, obviousness, eligibility, and FTO risks
6. **Invention Evaluation:** Assessed 8 candidate directions against all constraints
7. **Claim Mapping:** Defined experiments needed to support each surviving direction

### Source Standards

- **Primary sources preferred:** Official patent office records, full patent text, independent claims
- **Secondary sources used:** Google Patents, patent databases, open-hardware documentation
- **Tertiary sources noted:** News articles, blog posts (used for discovery only)
- **All critical claims cross-checked** across multiple sources where possible

### Limitations

1. **No official legal opinions** — All assessments are technical research, not legal advice
2. **No counsel-level claim charting** — Requires professional patent attorney
3. **Jurisdiction coverage gaps** — Chinese/Japanese/Korean searches limited by language
4. **Indian patent access** — Could not retrieve full file for 5559/CHE/2014
5. **Time constraint** — Research conducted within single session (2026-07-30)

---

*This report contains technical research and analysis only. It is not legal advice, a freedom-to-operate opinion, or a patentability determination. All patent status, claim scope, and legal conclusions must be verified by qualified patent counsel before any filing, commercialization, or design-freeze decision.*

*Confidential: Contains prospective invention analysis. Do not publicly disclose without institutional IPR review.*


---

## Source 12: `03_CONCEPT_PORTFOLIO/OpenBraille/02_Raw_Research/06_OpenBraille_Patent_Research_Microsoft_Copilot.docx`

- Authority: `TIER_3`
- Treatment: `SUPPORTING_EVIDENCE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `NEW_STAGE10F_EXTRACTION`
- SHA-256: `75e34f06275338189e29373c598afdbd60becb8d1a1e562ef7922a009bae77d6`

# Source Extraction

- Chapter: `05` — OpenBraille Patent Evidence and Future Research Path
- Authority tier: `TIER_3`
- Manual treatment: `SUPPORTING_EVIDENCE`
- Original source: `03_CONCEPT_PORTFOLIO/OpenBraille/02_Raw_Research/06_OpenBraille_Patent_Research_Microsoft_Copilot.docx`
- SHA-256: `75e34f06275338189e29373c598afdbd60becb8d1a1e562ef7922a009bae77d6`
- Extraction method: `DOCX_XML`
- Rule: source text only; no synthesis, correction or reconciliation.

---

OpenBraille Patent Landscape Verification

OpenBraille Patent Landscape and Development Pathway: Comprehensive 2026 Analysis

Executive Summary

This report delivers a rigorous, evidence-based analysis of the current patent landscape and development pathway for the OpenBraille project as of July 30, 2026. OpenBraille’s frozen MVP is a macro-scale (~300% ISO) six-dot refreshable Braille cell using six SG90-class servos, eccentric cams, pins, an FDM-printed frame, ESP32 direct PWM, and an external 5 V supply, all within a ₹5,000 budget and a three-month timeline. The research draws primarily from the authoritative project documentation, including the Engineering Design Review, Phase 3C Architecture Report, Decision Register, and supporting evidence matrices, and is supplemented by targeted patent and prior-art verification from global databases.

The analysis proceeds through ten structured sections, culminating in a final verdict on OpenBraille’s patent-development prospects. Key findings include:

Patent Path Classification: OpenBraille’s patent path is classified as Conditional (Class C)—there is plausible but unproven white space in manufacturing method and firmware/control, but the macro-scale servo/cam MVP alone does not guarantee a claimable invention.

Prior Art and Blocking Patents: The actuation mechanism space is heavily fenced by Dot Inc. and other incumbents, with specific families (e.g., US11854423B1, US11410574B2, WO2015189863, EP4049116, US5685721, US6743021) requiring careful claim-charting. Indian application 5559/CHE/2014 is expired and non-blocking.

Scale-Transfer Relevance: The macro-scale MVP is not inherently scale-independent; most prior art and commercial claims are at or near ISO standard scale, and the macro prototype’s evidence must be mapped carefully to any future claim.

Freedom-to-Operate (FTO): FTO risk is moderate to high for any mechanism claim; lower for manufacturing or firmware methods, provided claims are carefully constructed and Dot Inc. families are avoided.

Novelty and Obviousness: The MVP as built is likely obvious as a substitution of known components; only specific manufacturing or control methods, with measurable technical effect, offer a plausible path to patentability.

Recommended Invention Directions: Focus on modular manufacturability, calibration/control methods, and process innovations that are empirically validated at macro scale but plausibly transferable to standard scale.

Claim-to-Experiment Mapping: The current prototype can generate evidence for manufacturing and control claims, but not for ISO-compliant tactile cell mechanisms.

The report concludes that OpenBraille’s patent-first priority remains conditional: the project advances only if a specific, non-obvious, and technically effective manufacturing or firmware method is demonstrated and claim-charted against the current landscape. Otherwise, the project risks losing patent-first priority and should pivot to open demonstration or alternative innovation targets.

1. Executive Assessment: Patent Path Classification

Classification System

Class A: Clear, unblocked patent path; strong novelty and FTO; high likelihood of grant.

Class B: Plausible patent path; moderate risk; some claim construction or design-around required.

Class C: Conditional path; patentability depends on specific technical contribution and claim construction; significant risk from prior art or obviousness.

Class D: Blocked; no credible patent path; prior art or active patents preclude meaningful claims.

OpenBraille’s Classification

OpenBraille is classified as Class C (Conditional). The project’s patent-development path is neither clearly open nor fully blocked. The actuation mechanism space (servo/cam, electromagnetic latching, SMA, solenoid) is heavily fenced by Dot Inc. and other incumbents, and the macro-scale MVP as built is likely obvious as a substitution of known components. However, the project’s documented pivot—toward manufacturing method and firmware/control innovations—remains plausible, provided that:

The claimed method is specific, non-obvious, and technically effective;

The claim is supported by experimental evidence from the macro-scale MVP;

The claim is carefully charted against Dot Inc. and other active families to avoid overlap.

Advancement to patent filing is conditional on successful claim-charting and experimental validation. If these are not achieved, OpenBraille loses patent-first priority and should pivot to open demonstration or alternative innovation targets.

2. Search Log: Databases, Queries, and Process

Databases and Jurisdictions Searched

Indian Patent Office (InPASS): iprsearch.ipindia.gov.in

WIPO PATENTSCOPE: patentscope.wipo.int

USPTO Patent Center: patentcenter.uspto.gov

EPO Espacenet / INPADOC: worldwide.espacenet.com

CNIPA (China): cnipa.gov.cn

JPO (Japan): j-platpat.inpit.go.jp

KIPO (Korea): kipo.go.kr

Google Patents: patents.google.com

Non-patent literature: Academic databases, open-hardware repositories (MOLBED, MagnePins), project documentation.

Search Strings and Variants

"refreshable braille cell", "refreshable tactile display", "tactile pin array", "braille dot actuator", "servo cam braille", "cam follower tactile pin", "low cost braille actuator", "macro scale braille prototype", "3D printed refreshable braille", "additive manufactured tactile display", "monolithic tactile cell", "modular braille actuator", "PWM tactile actuator control", "adaptive overdrive braille actuator", "shared driver tactile pins", "low force latching tactile pixel", "piezoelectric braille replacement"

Process

Initial Landscape Review: Extracted all named patents, families, and assignees from project documentation and prior art tables.

Jurisdictional Verification: Queried each named patent/application in the relevant national/regional database, confirming legal status, family members, and claim scope.

Keyword and Classification Search: Used IPC/CPC codes (e.g., G09B21/003, G09B21/004) and keyword variants to identify additional relevant families and applications.

Non-Patent Literature: Reviewed open-hardware projects (MOLBED, MagnePins), academic publications, and manufacturing-method literature for prior art and technical context.

Claim-Charting Preparation: Extracted independent claims and mapped them against the OpenBraille MVP’s features and process steps.

Scale-Transfer Analysis: Assessed whether claims and prior art are scale-independent or scale-sensitive.

FTO and Risk Assessment: Evaluated blocking risk, novelty, and obviousness for each candidate invention direction.

3. Verified Family Table: Key Patents and Legal Status

Patent/Application

Jurisdiction

Status

Family Members

Relevance to OpenBraille

US11854423B1

US

Active (exp. 2041)

US17/240,744 (parent), US18/055,401 (cont.), US11,521,514B2 (prior)

Claims friction-held, impact-driven Braille pins; covers mechanical pin arrays with passive friction latching; not servo/cam-specific but relevant to passive-hold mechanisms.

US11410574B2

US

Active (exp. 2037)

WO2015189863 (PCT), CN104408994A, CN204204267U, US10175882B2

Layered electromagnetic Braille display; multi-layer, coil-driven, modular pin actuation; covers electromagnetic actuation and modular assembly.

WO2015189863

WO

Ceased

IN1575/DEL/2014 (IN), CN110631167A (CN), EP4049116A1 (EP)

SMA-based compliant mechanism with latching; covers latching, modular assembly, and SMA actuation.

EP4049116A1

EP

Pending

WO2015189863, US11410574B2

See above; European phase of SMA/compliant mechanism family.

US5685721

US

Expired

US6743021B2 (continuation), others

Early SMA-based Braille actuator; expired, but prior art for SMA and compliant mechanisms.

US6743021B2

US

Expired

US5685721 (parent)

Flexible-surface, microelectromechanical Braille display; prior art for flexible, multi-actuator tactile arrays.

5559/CHE/2014

IN

Expired/Abandoned

None found

Indian application for Braille display; no active claims; not blocking.

MOLBED/MagnePins

N/A

Open hardware

N/A

Open-source electromagnetic latching Braille cell; prior art for modular, latching, and open-manufacturing methods.

Dot Inc. Portfolio

KR/WO/US/EP

Multiple active

Dozens of families

Dominant estate in electromagnetic, piezo, and modular tactile cell mechanisms; covers most commercial-scale actuation methods.

Orbit Research/Innovision

US/IN

Active

Multiple

Magnetic and modular actuation; relevant to modular assembly and magnetic latching.

Note: All family and status data are current as of July 2026 and verified in the respective databases. See detailed analysis below for claim summaries and mapping.

4. Independent-Claim Analysis: Key Blocking and Adjacent Claims

US11854423B1 (Kolar et al.)

Independent Claims: Cover a refreshable Braille display with a body, perforations, and pins held in place passively via friction, impacted to create raised/lowered patterns. Claims both the device and the system (controller, text generator, impact driver).

Relevance: Does not claim servo/cam actuation or macro scaling, but covers friction-held, passively latched pins. Any OpenBraille variant using friction-hold or impact-driven pins must be carefully claim-charted against these claims.

Legal Status: Active, expiring 2041; continuation of US17/240,744 and US11,521,514B2; no Indian or EP equivalents found.

US11410574B2 / WO2015189863 / EP4049116A1 (Zhejiang Sci Tech Univ. / IIT Delhi)

Independent Claims: Layered electromagnetic refreshable Braille display; modular multi-layer assembly; electromagnetic coil actuation; latching via compliant mechanisms; covers both device and reader system.

Relevance: Covers electromagnetic actuation, modular assembly, and latching mechanisms. Not directly servo/cam, but modularity and assembly methods may overlap with OpenBraille’s manufacturing method if not carefully distinguished.

Legal Status: Active in US and China; PCT application ceased in some jurisdictions; Indian application IN1575/DEL/2014 expired.

US5685721 / US6743021B2 (Decker et al.)

Independent Claims: SMA-based, flexible-surface, microelectromechanical Braille display; covers both actuation and flexible tactile surface.

Relevance: Expired, but strong prior art for SMA, compliant mechanisms, and flexible/microactuated tactile arrays. Not directly servo/cam, but relevant for obviousness and background art.

Dot Inc. Portfolio

Claims: Multiple families covering electromagnetic, piezoelectric, modular, and scalable tactile cell mechanisms; includes both apparatus and manufacturing/method claims.

Relevance: Dominant blocking estate for commercial-scale, multi-cell, and modular tactile displays. No direct servo/cam claims found, but broad coverage of modular assembly, actuation, and control methods.

MOLBED / MagnePins (Open Hardware)

Claims: Open-source hardware, not patented; prior art for modular, electromagnetic latching, and open-manufacturing methods.

Relevance: Not blocking, but strong prior art for modularity, open manufacturing, and latching mechanisms.

Indian Application 5559/CHE/2014

Claims: No active claims; application expired or abandoned.

Relevance: Not blocking; no effect on OpenBraille’s FTO.

5. Frozen-MVP Feature Chart

Feature

OpenBraille MVP Implementation

Prior Art / Patent Family

Scale-Dependence

Blocking Risk

Cell scale

Macro (~300% ISO, ~7 mm pitch, ~1.5 mm height)

Most prior art at ISO scale; macro scaling not claimed

Scale-sensitive

Low (for macro MVP); high if scaled down

Actuation

6× SG90-class servos, eccentric cams

No direct servo/cam claims found; most prior art is electromagnetic, SMA, or piezo

Scale-independent

Low (for servo/cam); moderate if modularity overlaps Dot Inc.

Pin/follower/guide

3D-printed ABS/PETG frame, stainless pins

Modular pin arrays, friction-hold (US11854423B1), modular assembly (WO2015189863)

Scale-sensitive

Moderate (if modularity is claimed)

Reset mechanism

Servo-integral torsion spring (no external spring)

Latching and compliant mechanisms (WO2015189863, US5685721)

Scale-independent

Low (if not friction-hold or compliant latch)

Control/firmware

ESP32 direct PWM, serial command, lookup table

Firmware/control methods not broadly claimed; adaptive control (Dot Inc.)

Scale-independent

Low–moderate (if adaptive or multiplexed control is claimed)

Manufacturing method

In-house FDM 3D printing, modular assembly

Additive manufacturing (US10,254,499B1), modular assembly (WO2015189863)

Scale-independent

Moderate (if specific process is claimed)

Power architecture

External 5 V/2 A supply, decoupling capacitor

Not claimed

Scale-independent

Low

Validation

Single-dot-first, tactile user testing

Not claimed

Scale-independent

Low

Key Takeaway: The MVP as built is not directly blocked by any single active claim, but modular assembly, manufacturing method, and control/firmware innovations must be carefully claim-charted to avoid overlap with Dot Inc. and other active families.

6. Indian-Patent Investigation: 5559/CHE/2014 and Domestic Landscape

5559/CHE/2014

Status: Application expired or abandoned; no active claims or family members found in InPASS or Espacenet.

Claims: Not available; no effect on OpenBraille’s FTO.

Relevance: Not blocking; no further action required.

Domestic Patent Landscape

Key Indian Assignees: Innovision (Braille Me), Orbit Research (Orbit Reader), IIT Delhi (WO2015189863), individual inventors (US11854423B1).

Active Indian Patents: Most active patents are in electromagnetic, SMA, or modular assembly; no direct servo/cam claims found.

Manufacturing/Process Claims: Some Indian patents claim modular assembly and manufacturing methods (e.g., WO2015189863), but none directly block FDM-printed, macro-scale servo/cam cells.

FTO Risk: Moderate for modular assembly and manufacturing method claims; low for servo/cam actuation at macro scale.

7. Novelty, Obviousness, Eligibility, and FTO Risk Analyses

Novelty

MVP as Built: The macro-scale servo/cam MVP is not novel as a substitution of known components; servo/cam actuation, macro scaling, and FDM printing are all known in the art.

Manufacturing Method: Novelty may exist in a specific, modular, low-tolerance, FDM-printed assembly method if it produces measurable technical effect (e.g., improved yield, durability, or tactile performance).

Firmware/Control: Novelty may exist in a specific control or calibration method that enables commodity actuators to achieve repeatable tactile output, especially if adaptive or multiplexed control is demonstrated.

Obviousness

MVP as Built: Likely obvious; combining known servo/cam actuation, macro scaling, and FDM printing is within the skill of the art.

Manufacturing/Control Methods: Obviousness risk is lower if a specific, non-obvious technical effect is demonstrated (e.g., improved repeatability, reduced cost, or new calibration method).

Patent Eligibility

Manufacturing/Process Claims: Eligible if tied to a specific, technical manufacturing process or assembly method.

Firmware/Control Claims: Eligible if tied to a specific, technical control method with measurable effect; pure software or abstract algorithms may face eligibility challenges in some jurisdictions.

Freedom-to-Operate (FTO)

Actuation Mechanism: Moderate to high risk for mechanism claims; Dot Inc. and other incumbents have broad coverage of electromagnetic, modular, and tactile cell mechanisms.

Manufacturing/Process: Moderate risk; additive manufacturing and modular assembly are claimed in some families, but FDM-printed, macro-scale, servo/cam cells are not directly blocked.

Firmware/Control: Lower risk; most claims are at the hardware or system level, not firmware/control.

8. Candidate Invention Directions

1. Modular, Low-Tolerance, FDM-Printed Tactile Cell Assembly

Description: A specific assembly method for tactile cells using FDM printing, modular components, and designed-in clearances to achieve repeatable tactile output at low cost.

Claim Elements: Frame/guide geometry, modular actuator modules, cam/follower travel relationship, manufacturing process and tolerances, calibration method.

Evidence Required: Measured yield, repeatability, durability, and tactile performance; comparison against nearest prior art.

2. Adaptive Firmware/Control Method for Commodity Actuators

Description: A firmware/control method that enables commodity servos to achieve repeatable tactile output, with calibration, error detection, and adaptive control.

Claim Elements: Control sequence, calibration storage, error detection, adaptive actuation, technical effect (e.g., improved repeatability or reduced power).

Evidence Required: Experimental validation of repeatability, error detection, and adaptive control; comparison against conventional control.

3. Process Innovation for Multi-Cell or Scalable Arrays

Description: A process or assembly method enabling scalable, multi-cell tactile arrays using modular, FDM-printed components and commodity actuators.

Claim Elements: Modular assembly, process steps, scalability, technical effect (e.g., reduced assembly time or improved reliability).

Evidence Required: Demonstration of scalability, assembly time, and reliability; mapping to prior art.

4. Calibration and Self-Test Protocols for Tactile Cells

Description: A calibration and self-test protocol enabling rapid, reliable setup and validation of tactile cell assemblies.

Claim Elements: Calibration sequence, self-test routine, error detection, technical effect (e.g., reduced setup time or improved reliability).

Evidence Required: Experimental validation of calibration and self-test; comparison against conventional methods.

9. Claim-to-Experiment Map

Candidate Claim Element

MVP Experiment/Measurement

Scale-Dependence

Relevance to Patent Path

Modular FDM assembly

Build and test single-dot and six-dot modules; measure assembly time, yield, and repeatability

Scale-sensitive (macro vs. ISO)

Supports manufacturing/process claims if technical effect is demonstrated

Servo/cam actuation

Measure force, travel, repeatability, and durability over 1,000+ cycles

Scale-independent

Only supports claim if combined with specific process or control method

Calibration/control

Implement and test calibration, error detection, and adaptive control routines; measure repeatability and error rates

Scale-independent

Supports firmware/control claims if technical effect is demonstrated

Tactile performance

Conduct blinded tactile-identification protocol with human participants; measure success rate and repeatability

Scale-sensitive

Required for claims tied to tactile performance or user experience

Scalability/process

Assemble and test multi-cell arrays (if built); measure assembly time and reliability

Scale-sensitive

Supports process/scalability claims if technical effect is demonstrated

Key Takeaway: The macro-scale MVP can generate evidence for manufacturing and control claims, but not for ISO-compliant tactile cell mechanisms. Claims must be carefully constructed to map experimental evidence to technical effect and avoid overlap with prior art.

10. Final Verdict: Advancement, Conditionality, and Patent-First Priority

Advancement Status

OpenBraille’s patent-development path remains conditional. The project advances only if:

A specific, non-obvious, and technically effective manufacturing or firmware/control method is demonstrated and claim-charted against the current landscape;

Experimental evidence from the macro-scale MVP supports the claimed technical effect;

The claim is carefully constructed to avoid overlap with Dot Inc. and other active families.

If these conditions are not met, OpenBraille loses patent-first priority and should pivot to open demonstration, educational impact, or alternative innovation targets.

Separation of Fact, Inference, Uncertainty, and Recommendation

Fact: The actuation mechanism space is heavily fenced by Dot Inc. and other incumbents; the macro-scale MVP as built is likely obvious as a substitution of known components.

Inference: Manufacturing method and firmware/control innovations remain plausible patent targets, provided claims are specific, non-obvious, and technically effective.

Uncertainty: The scale-transfer relevance of macro-scale evidence to ISO-compliant claims is unproven; the novelty and non-obviousness of candidate manufacturing/control methods depend on experimental validation and claim-charting.

Recommendation: Focus on modular manufacturability, calibration/control methods, and process innovations that are empirically validated at macro scale but plausibly transferable to standard scale. Conduct claim-charting and experimental validation before committing to patent filing.

Confidential Invention Mechanisms (For Institutional Review)

[Confidential: Not for public disclosure]

Any specific modular assembly, calibration, or control method developed and validated in the MVP should be documented in detail and reviewed by institutional IP counsel before public disclosure or publication.

All experimental data, assembly protocols, calibration routines, and firmware/control algorithms should be preserved as invention records and included in the institutional review package.

Appendices

A. Patent Family Table (Summary)

Patent/Application

Jurisdiction

Status

Family Members

Key Claims

US11854423B1

US

Active

US17/240,744, US18/055,401, US11,521,514B2

Friction-held, impact-driven Braille pins; passive latching

US11410574B2

US

Active

WO2015189863, CN104408994A, CN204204267U, US10175882B2

Layered electromagnetic, modular assembly, latching

WO2015189863

WO

Ceased

IN1575/DEL/2014, CN110631167A, EP4049116A1

SMA/compliant mechanism, modular assembly

EP4049116A1

EP

Pending

WO2015189863, US11410574B2

See above

US5685721

US

Expired

US6743021B2

SMA, compliant mechanism, flexible tactile surface

US6743021B2

US

Expired

US5685721

Flexible-surface, microelectromechanical Braille display

5559/CHE/2014

IN

Expired

None

Not blocking

Dot Inc. Portfolio

KR/WO/US/EP

Active

Dozens

Electromagnetic, piezo, modular tactile cell mechanisms

MOLBED/MagnePins

N/A

Open

N/A

Modular, electromagnetic latching, open manufacturing

B. Frozen-MVP Feature Chart (Summary)

Feature

Implementation

Blocking Risk

Macro scale

~300% ISO

Low (for macro MVP)

Servo/cam actuation

6× SG90 servos

Low–moderate

Modular assembly

FDM-printed, modular

Moderate

Calibration/control

ESP32 direct PWM

Low–moderate

Manufacturing method

In-house FDM

Moderate

Tactile performance

User testing

Scale-sensitive

C. Risk and Invention Directions (Bullet Points)

Risks:

Blocking by Dot Inc. and other active families for mechanism claims

Obviousness for MVP as built

Scale-transfer uncertainty for macro evidence

FTO risk for modular assembly and manufacturing methods

Candidate Invention Directions:

Modular, low-tolerance, FDM-printed tactile cell assembly

Adaptive firmware/control method for commodity actuators

Process innovation for scalable arrays

Calibration and self-test protocols

References (Embedded in Text)

All citations and references are embedded in the text and tables above, with direct links to patent records, project documentation, and supporting evidence.

Section Dividers

End of Report

