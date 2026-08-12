# Project mC — Master Manual Opening and Decision Reconciliation

## 1. Attachment inventory

All ten physical attachments required for Stage 10D are present and readable. Nine files match the byte sizes and SHA-256 values stated in the manifest exactly. The tenth attachment is the self-referential manifest itself; its uploaded transport name is `99_INPUT_MANIFEST(17).md`, while its controlled logical filename inside the manifest is `99_INPUT_MANIFEST.md`. The suffix does not create a second version or replace a missing technical source.

| No. | Physical attachment | Controlled role | Inventory result |
|---:|---|---|---|
| 1 | `00_READ_FIRST_Opening_Decision_Reconciliation_Instructions.md` | Governing task specification | Present, readable, 3,779 bytes, SHA-256 matched |
| 2 | `01_MASTER_MANUAL_AUTHORITY_AND_CONTRADICTION_PROTOCOL.md` | Authority and contradiction control | Present, readable, 2,565 bytes, SHA-256 matched |
| 3 | `02_MASTER_MANUAL_BLUEPRINT.md` | Manual structure and scope | Present, readable, 5,264 bytes, SHA-256 matched |
| 4 | `03_MASTER_MANUAL_MAPPING_SUMMARY.md` | Frozen source-mapping summary | Present, readable, 1,881 bytes, SHA-256 matched |
| 5 | `04_CHAPTER_01_GOVERNANCE_SOURCE_PACKET.md` | Chapter 01 complete controlled source packet | Present, readable, 364,535 bytes, SHA-256 matched; 26 mapped sources |
| 6 | `05_CHAPTER_02_PHASE_HISTORY_SOURCE_PACKET.md` | Chapter 02 complete controlled source packet | Present, readable, 2,196,393 bytes, SHA-256 matched; 52 mapped sources |
| 7 | `06_CHAPTER_03_PORTFOLIO_EVOLUTION_SOURCE_PACKET.md` | Chapter 03 complete controlled source packet | Present, readable, 811,108 bytes, SHA-256 matched; 21 mapped sources |
| 8 | `07_CHAPTER_09_COMPARATIVE_DECISION_SOURCE_PACKET.md` | Chapter 09 complete controlled source packet | Present, readable, 353,876 bytes, SHA-256 matched; 18 mapped sources |
| 9 | `08_REQUIRED_OUTPUT_TEMPLATE.md` | Required reconciliation output structure | Present, readable, 3,879 bytes, SHA-256 matched |
| 10 | `99_INPUT_MANIFEST(17).md` | File-control manifest | Present and readable; treated only as attachment identity control, not technical evidence |

Inventory conclusion: exactly ten physical attachments are present. The governing instruction, authority protocol, blueprint, mapping summary, all four chapter packets, output template and manifest are readable. No attachment is missing, duplicated, partial, or replaced by prior-chat context. The manifest is not counted as technical evidence. This reconciliation uses only the attached files.

## 2. Reconciliation method

The attached Stage 10D authority protocol controls this document. Material claims were resolved in the following order:

1. current teacher requirements and formally recorded approvals;
2. `Project_mC_Decision_Register_v1.2.md`;
3. authoritative final Phase 3C architectures;
4. final memories and SOPs;
5. current comparative evidence, gates and uncertainty registers;
6. valid syntheses and adjudications;
7. controlled research lanes;
8. historical phase records and concept dossiers;
9. transport, launcher, manifest and archived material.

A lower-authority record was not permitted to silently override a higher-authority record. Where two sources of comparable decision-support status disagree, the disagreement is preserved as an unresolved decision rather than converted into a vote. Every material conclusion below identifies an original organized-workspace path and its authority tier. Historical sources are explicitly labelled as historical; recommendations, requests and simulations are not described as approvals or completed experiments.

The reconciliation also enforces the three architecture identity locks:

- OpenBraille is the frozen six-servo macro-cell architecture.
- VibeGuard is the frozen ADXL345-plus-ESP32 vibration-monitoring MVP.
- TrueMoist is the validated local compensation architecture using measured temperature and controlled salinity-treatment coding.

Moving-roller OpenBraille, software-security VibeGuard, live-EC TrueMoist and other rejected or superseded variants are excluded from current design truth. Patent-development paths such as D11, VPD-C7 and PIRG remain hypotheses requiring experiments, current prior-art verification and institutional IPR review.

# Chapter 01 — Project Mandate, Requirements and Governance

## 01.1 Controlling project mandate

Project mC is a patent-oriented embedded-systems innovation pipeline whose immediate academic purpose is to select and execute one semester-scale microcontroller project while preserving credible longer-term research, publication, patent-development and commercialization paths. It is not a promise that the semester MVP will itself be novel or patentable.  
**Source basis:** `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Original_Repository_README.md` (**TIER_1**); `01_GOVERNANCE_AND_CONTROL/03_Project_Context_and_Phase_Map/MC_Project_PHASE_DOC.md` (**TIER_1**); `01_GOVERNANCE_AND_CONTROL/02_Decision_Registers/Project_mC_Decision_Register_v1.2.md` (**TIER_1**).

The current controlled portfolio contains OpenBraille, VibeGuard and TrueMoist. TrustLatch and ColdTrace are deferred, not technically rejected, and may re-enter only under the recorded re-entry conditions. Phase 3C is complete for the retained three-concept shortlist, not for all five original concepts.  
**Source basis:** `01_GOVERNANCE_AND_CONTROL/02_Decision_Registers/Project_mC_Decision_Register_v1.2.md` (**TIER_1**, PDR-064 to PDR-067); `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/AGENTS.md` (**TIER_1**); `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Original_Repository_README.md` (**TIER_1**).

The present governance state is not a confirmed change to VibeGuard. The team has prepared and preserved a formal request to change the semester implementation from OpenBraille to VibeGuard, but the attached sources contain no completed teacher-decision field, signature or separate controlling approval record.  
**Source basis:** `01_GOVERNANCE_AND_CONTROL/01_Project_Requirements/Teacher_Project_Requirements_and_Change_Context.md` (**TIER_1**, request state); `04_COMPARATIVE_DECISION/03_Change_Request/Project_mC_Request_to_Change_from_OpenBraille_to_VibeGuard.docx` (**TIER_2**, request only); `01_GOVERNANCE_AND_CONTROL/AUTHORITY_MAP.md` (**TIER_1**, selection not finally authorized unless separately recorded).

## 01.2 Teacher and course constraints

The controlling teacher/course constraints are:

| Constraint | Reconciled requirement | Source and authority |
|---|---|---|
| Project context | B.Tech CSE Cyber Security microcontroller semester project; five-member group | `01_GOVERNANCE_AND_CONTROL/01_Project_Requirements/Teacher_Project_Requirements_and_Change_Context.md` — **TIER_1** |
| Team structure | Three technically strong members, one learner, one presentation/documentation/support member | same source — **TIER_1**; confirmed by PDR-038 in `01_GOVERNANCE_AND_CONTROL/02_Decision_Registers/Project_mC_Decision_Register_v1.2.md` — **TIER_1** |
| Time | Teacher context permits up to three months; the internal baseline remains approximately two months unless an approved schedule uses the full period | teacher context — **TIER_1**; PDR-002 — **TIER_1** |
| Budget | Preferred hardware cost at or below ₹3,000; absolute ceiling ₹5,000 | teacher context — **TIER_1**; PDR-001 — **TIER_1** |
| Platform | Arduino-board or Arduino-IDE-compatible embedded implementation | teacher context — **TIER_1** |
| Cybersecurity | Preferred, but not recorded as a mandatory final-selection criterion | teacher context — **TIER_1**; PDR-065 — **TIER_1** |
| Power | Low-power components; very high-power components not permitted | teacher context — **TIER_1** |
| Interface/evidence | USB sample, interface or logging capability should be included | teacher context — **TIER_1** |
| STM32 | STM32 was mentioned, but the final board must follow the authoritative project records and teacher approval | teacher context — **TIER_1** |
| Demonstration | A strong live demonstration is required | teacher context — **TIER_1** |

The teacher context expressly frames the OpenBraille-to-VibeGuard move as a request for approval. It also states that the change must not be justified by claiming that VibeGuard is guaranteed to receive a patent, and that the ordinary frozen VibeGuard MVP is conventional.  
**Source basis:** `01_GOVERNANCE_AND_CONTROL/01_Project_Requirements/Teacher_Project_Requirements_and_Change_Context.md` (**TIER_1**).

## 01.3 Authority hierarchy

For the Master Manual, the controlling hierarchy is the attached Stage 10D protocol:

1. current teacher requirements and explicit approvals;
2. Decision Register v1.2;
3. authoritative final Phase 3C architectures;
4. final concept memories and SOPs;
5. current comparative evidence and gates;
6. valid patent syntheses and final adjudications;
7. controlled independent research;
8. historical phase records and concept dossiers;
9. archived, transport and provenance material.

Older repository instructions sometimes place the Engineering Design Review before the Decision Register. For this reconciliation, that older ordering is subordinated to the attached Stage 10D protocol. The Engineering Design Review remains the principal source for concept identity, mission, hypothesis and minimum demonstrable success, but it cannot override later teacher constraints or accepted Decision Register entries.  
**Source basis:** `01_GOVERNANCE_AND_CONTROL/AUTHORITY_MAP.md` (**TIER_1**); `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/AGENTS.md` (**TIER_1**, older repository order); `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/02_Authoritative_Source_Manifest.md` (**TIER_2**, EDR identity boundary).

## 01.4 Current decision-register controls

`Project_mC_Decision_Register_v1.2.md` is canonical and controlling. Version 1.0 is retained only for historical traceability and must not be used operationally.  
**Source basis:** `01_GOVERNANCE_AND_CONTROL/02_Decision_Registers/Project_mC_Decision_Register_v1.2.md` (**TIER_1**); `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Legacy_Repository_Audit/04_AUTHORITY_AMBIGUITIES.md` (**TIER_1**); `01_GOVERNANCE_AND_CONTROL/AUTHORITY_MAP.md` (**TIER_1**).

The principal current controls are:

- **PDR-001:** preferred budget ≤₹3,000 and maximum ₹5,000.
- **PDR-002:** internal planning baseline of approximately two months for a five-member team.
- **PDR-004:** concept-swapped or materially mis-scoped AI sections are excluded rather than averaged.
- **PDR-006:** future research passes must restate and confirm the concept against the authoritative definition.
- **PDR-039 and PDR-041:** use multiple independent research systems and preserve duplicate findings before consolidation for confidence analysis; this does not turn models into votes.
- **PDR-043:** Phase 3C must select one architecture for each completed concept rather than preserve unresolved architecture forks.
- **PDR-064:** only OpenBraille, VibeGuard and TrueMoist enter final comparative down-selection.
- **PDR-065:** credible patent-development potential is the primary final-selection priority, with feasibility, budget, timeline, demonstrability and team fit still mandatory.
- **PDR-066:** TrustLatch and ColdTrace re-enter only after a decisive retained-concept failure, material stakeholder change, or significant new evidence.
- **PDR-067:** Phase 3C is complete only for the retained three-concept shortlist.
- **PDR-038:** the roster is five members, not six.

The frozen architecture controls relevant to the opening chapters are:

- OpenBraille: servo-plus-cam, permanent macro scale, ESP32 direct PWM, FDM manufacture, external 5 V servo supply, single-dot-first validation. The claimed SG90 passive-return mechanism remains technically unvalidated; active servo-driven cam retraction is the required fallback.  
  **Source basis:** PDR-015 to PDR-022 in `01_GOVERNANCE_AND_CONTROL/02_Decision_Registers/Project_mC_Decision_Register_v1.2.md` (**TIER_1**).
- VibeGuard: ADXL345 over SPI to an ESP32, time-domain features with triggered FFT, calibrated RMS baseline with optional Mahalanobis comparison, rigid mounting, local RGB output and controlled eccentric-mass rig. Noise isolation and dense-machine attribution remain validation tasks rather than demonstrated capabilities.  
  **Source basis:** PDR-023 to PDR-030 and PDR-054 to PDR-055 in the same register (**TIER_1**).
- TrueMoist: one-soil local compensation system using a genuine analog capacitive probe, measured temperature, controlled salinity-treatment coding, ADS1115-versus-ESP32 ADC gate, fixed offline-trained regression coefficients, 72 independent physical runs and gravimetric reference. It is not a live-EC meter or universal multi-soil controller.  
  **Source basis:** PDR-031, PDR-032, PDR-045, PDR-048 to PDR-050 and PDR-058 to PDR-063 in the same register (**TIER_1**).

No Decision Register entry records a final team or teacher selection of VibeGuard over OpenBraille. The register closes the retained portfolio and defines evaluation rules; it does not complete the later approval step.

## 01.5 Repository and evidence-control rules

The repository structure is owner-designed and should be changed only through an approved, minimally invasive process. File cleanup must not rewrite technical conclusions, merge same-looking filenames without content comparison, delete failed research, renumber PDR entries casually, or allow convenience copies and ZIP members to override canonical files.  
**Source basis:** `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/AGENTS.md` (**TIER_1**).

Canonical files must be distinguished from convenience packages such as `COPY PASTE FOLDER/`, `every sop and memory/`, `contexts.zip` and phase ZIPs. Byte-identical convenience copies have no independent authority.  
**Source basis:** `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Original_Repository_README.md` (**TIER_1**); `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Legacy_Repository_Audit/04_AUTHORITY_AMBIGUITIES.md` (**TIER_1**).

Raw AI research is evidence requiring audit, not project authority and not a vote. Failed or concept-swapped outputs are retained for methodology traceability but excluded from substantive synthesis. Missing conclusions must not be reconstructed from fragments.  
**Source basis:** `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/AGENTS.md` (**TIER_1**); `01_GOVERNANCE_AND_CONTROL/02_Decision_Registers/Project_mC_Decision_Register_v1.2.md` (**TIER_1**, PDR-004/PDR-006); `04_COMPARATIVE_DECISION/COMPARATIVE_DECISION_INDEX.md` (**TIER_2**).

Repository snapshots, manifests, naming logs and launchers are provenance or administration records. They may prove identity, location, hashes or historical movement; they do not independently establish technical truth, feasibility, patentability or approval.

## 01.6 Material contradictions

| ID | Issue | Higher-authority source | Conflicting source | Resolution | Residual uncertainty |
|---|---|---|---|---|---|
| C01-01 | Two-month versus three-month timeline | `01_GOVERNANCE_AND_CONTROL/01_Project_Requirements/Teacher_Project_Requirements_and_Change_Context.md` — **TIER_1**, up to three months | PDR-002 in `.../Project_mC_Decision_Register_v1.2.md` — **TIER_1**, approximately two months | Treat three months as the permitted outer boundary and two months as the internal baseline used for feasibility screening. | The teacher-approved execution calendar is not attached. |
| C01-02 | EDR-first older repository order versus Stage 10D order | Attached authority protocol; `01_GOVERNANCE_AND_CONTROL/AUTHORITY_MAP.md` — **TIER_1** | `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/AGENTS.md` — **TIER_1** | Stage 10D order controls; EDR remains authoritative for identity but is below current teacher constraints and Decision Register v1.2 for conflicting decisions. | None for this stage. |
| C01-03 | Roadmap says Phase 3 pending | Decision Register v1.2, PDR-067 — **TIER_1** | `01_GOVERNANCE_AND_CONTROL/03_Project_Context_and_Phase_Map/MC_Project_PHASE_DOC.md` — **TIER_1**, stale progress block | Phase 3C is complete for the retained three only. The roadmap remains methodological, not current status authority. | Roadmap status block requires an approved documentation update. |
| C01-04 | All five concepts appear active in older context | Decision Register v1.2, PDR-064/PDR-067 — **TIER_1** | `01_GOVERNANCE_AND_CONTROL/03_Project_Context_and_Phase_Map/PROJECT_CONCEPT_CONTEXT.md` — **TIER_1**, historical high-level context | Use the older file only for original definitions. TrustLatch and ColdTrace are deferred. | Re-entry remains conditional under PDR-066. |
| C01-05 | Decision Register v1.0 versus v1.2 | `.../Project_mC_Decision_Register_v1.2.md` — **TIER_1** | `.../HISTORICAL_Project_mC_Decision_Register_v1.0.md` — **TIER_1**, superseded | v1.2 controls; v1.0 is historical only. | None. |
| C01-06 | Claim that STM32 is strictly mandatory and ESP32 is a fatal violation | Current teacher requirements — **TIER_1** | `04_COMPARATIVE_DECISION/04_Team_Audits_and_Objections/03_Team_Submission_IDK.pdf` — **TIER_2**, team-submitted claim | The attached teacher record says STM32 was mentioned, not that ESP32 is categorically forbidden; final board choice requires teacher approval. Frozen architectures may retain ESP32 as project truth, but academic acceptance remains open. | Current official syllabus and explicit teacher ruling are not established by the attachment set and require later primary-source verification/approval. |
| C01-07 | OpenBraille 5 V/2 A supply marked accepted versus six-servo peak-current concern | PDR-020 — **TIER_1**, accepted architecture | Team objection and uncertainty register — **TIER_2** | Preserve 5 V/2 A as the frozen design baseline, but do not describe adequacy as experimentally proven. Run staged current, brownout and stall testing before full integration. | Actual servo current distribution and safe supply margin remain unknown. |
| C01-08 | Passive SG90 torsion-spring reset | PDR-021 required correction — **TIER_1** | Earlier architecture wording and memory — lower architecture/memory authority | Passive return is unproven. Active servo-driven cam retraction controls unless physical inspection proves a usable passive return. | Requires inspection and prototype test. |
| C01-09 | Proposed shift versus approved shift | Teacher context and Authority Map — **TIER_1** | Change-request document — **TIER_2** | The change request is formally prepared but not approved in the attached record. | Teacher decision, conditions, signature and date remain open. |
| C01-10 | Folder placement implies final selection | `01_GOVERNANCE_AND_CONTROL/AUTHORITY_MAP.md` — **TIER_1**; `04_COMPARATIVE_DECISION/COMPARATIVE_DECISION_INDEX.md` — **TIER_2** | Repository organization containing both directions | Folder placement preserves records; it does not finalize the semester concept. | A separate approval/change record is required. |

## 01.7 Open approvals or governance actions

| Item | Current status | Supporting source | Required action |
|---|---|---|---|
| OpenBraille-to-VibeGuard semester change | Formally requested; no explicit approval attached | `04_COMPARATIVE_DECISION/03_Change_Request/Project_mC_Request_to_Change_from_OpenBraille_to_VibeGuard.docx` — **TIER_2**; teacher context — **TIER_1** | Obtain and preserve the teacher decision, conditions, signature/date or equivalent explicit controlling record. |
| Final MCU/platform acceptance | Frozen concept records use ESP32; STM32 was mentioned by teacher | teacher context — **TIER_1**; PDR-017/PDR-025 — **TIER_1** | Obtain explicit confirmation that the selected board satisfies the course/project requirement, or authorize a controlled board substitution. |
| Project-wide final concept selection | Not conclusively recorded | Decision Register v1.2 — **TIER_1**; two adjudications — **TIER_2** | Resolve the conflicting gate recommendations and record one authorized selection decision. |
| Phase 4 start | Not started in controlling repository status | `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Original_Repository_README.md` — **TIER_1** | Start only after selection/approval and concept-specific entry gates are formally authorized. |
| Procurement authorization | Not established | change request — **TIER_2** | Refresh prices/specifications, confirm board and concept approval, then freeze a procurement BOM. |
| Five-person role-to-name map | Proposed, not signed | change request — **TIER_2**; PDR-038 — **TIER_1** | Assign named ownership and cross-training after approval. |
| Patent-development disclosure and filing route | Hypothetical and evidence-gated | authority protocol; adjudications — **TIER_2** | Complete experiments, current prior-art verification and institutional ownership/inventorship review before disclosure or filing decision. |

## 01.8 Draft-safe Chapter 01 statements

- Project mC is a patent-oriented embedded-systems project-selection and development pipeline, but patent grant, novelty, inventive step and freedom to operate are not established.
- The project is governed by current teacher constraints, Decision Register v1.2, frozen concept architectures and controlled evidence rules.
- The preferred prototype budget is at or below ₹3,000, with an absolute ceiling of ₹5,000.
- The team has five members: three strong technical contributors, one learner and one presentation/documentation/support contributor.
- The teacher context permits an implementation period of up to three months, while the project’s internal feasibility baseline has generally been approximately two months.
- OpenBraille, VibeGuard and TrueMoist are the retained Phase 3C concepts; TrustLatch and ColdTrace are deferred rather than technically rejected.
- Phase 3C is complete only for the retained three-concept shortlist.
- The team has formally requested approval to change the semester build from OpenBraille to VibeGuard; the attached records do not prove that approval has been granted.
- OpenBraille, VibeGuard and TrueMoist must retain their separate frozen identities and must not be combined into a hybrid architecture.
- Raw AI research and adjudications are evidence sources, not votes or automatic authority.

## 01.9 Statements that must not be made

- “VibeGuard has been approved by the teacher.”
- “The team has finally selected VibeGuard.”
- “Phase 4 has started.”
- “Phase 3C was completed for all five original concepts.”
- “TrustLatch and ColdTrace failed technically.”
- “Cybersecurity relevance is a mandatory final-selection criterion.”
- “ESP32 is unquestionably accepted by the teacher/course,” or conversely, “ESP32 is conclusively prohibited,” without a current explicit controlling record.
- “The OpenBraille 5 V/2 A supply and passive reset are proven adequate.”
- “Any semester MVP is patent-ready, novel, non-obvious or free to operate.”
- “Agreement among multiple models proves a conclusion.”

# Chapter 02 — Research Methodology and Phase History

## 02.1 Phase framework

Project mC developed through a staged funnel intended to prevent premature solution generation:

- **Phase 1A:** opportunity discovery—problems and research gaps before solutions.
- **Phase 1B:** opportunity extraction, clustering, structured evaluation and ranking.
- **Phase 1B.5:** engineering-gate portfolio optimization.
- **Phase 1C:** high-level concept synthesis and Top Five selection.
- **Phase 2:** historical patent-landscape exploration and white-space assessment.
- **Phase 3A:** engineering-landscape discovery.
- **Engineering Design Review:** identity, mission, hypothesis, fixed principles and minimum demonstrable success.
- **Phase 3B:** feasibility analysis and candidate technology comparison without final architecture selection.
- **Phase 3C:** architecture selection and prototype planning for the retained concepts, followed by retained-portfolio closure and comparative down-selection.

**Source basis:** `02_PHASE_HISTORY/HISTORICAL_RESEARCH_INDEX.md` (**TIER_4**, historical boundary); `02_PHASE_HISTORY/PHASE_HISTORY_INDEX.md` (**TIER_4**); `01_GOVERNANCE_AND_CONTROL/03_Project_Context_and_Phase_Map/MC_Project_PHASE_DOC.md` (**TIER_1**, methodology, with stale status caveat); `01_GOVERNANCE_AND_CONTROL/02_Decision_Registers/Project_mC_Decision_Register_v1.2.md` (**TIER_1**, current phase controls).

## 02.2 Phase 1A through Phase 1C

### Phase 1A — Opportunity Discovery

Phase 1A deliberately avoided creating project ideas. Multiple independent research systems explored real-world problems, academic gaps and industrial pain points across healthcare, agriculture, industry, cybersecurity, accessibility, infrastructure and other embedded domains. Its outputs were opportunity statements and research gaps, not products or architectures.  
**Source basis:** `02_PHASE_HISTORY/Phase_1/Phase_1A_Opportunity_Discovery/Phase1A_Memory.md` (**TIER_4**, historical narrative).

### Phase 1B — Opportunity Analysis

Phase 1B extracted distinct opportunities, preserved cross-model duplicates before consolidation, grouped related findings into clusters, created structured records, and scored the clusters against novelty, patent potential, market demand, embedded advantage, AI/cybersecurity relevance, prototype feasibility, budget, semester feasibility, research gap and startup potential. It performed no new idea generation or solution design.  
**Source basis:** `02_PHASE_HISTORY/Phase_1/Phase_1B_Opportunity_Analysis/Phase1B_Memory.md` (**TIER_4**); PDR-041 in Decision Register v1.2 (**TIER_1**).

### Phase 1B.5 — Portfolio Optimization

Phase 1B.5 applied eight gates: semester feasibility, budget feasibility, embedded-systems necessity, patent/research white space, demonstration impact, team capability, learning return and innovation density. It was a decision gate, not a concept-generation phase.  
**Source basis:** `02_PHASE_HISTORY/Phase_1/Phase_1B5_Portfolio_Optimization/Phase1B5_Memory.md` (**TIER_4**).

A later consistency check found that the Phase 1B.5 survivor list contained 22 entries, six of which had been outside the Phase 1B Top 20 and had re-entered improperly. Four Top-20 clusters were legitimately removed by the hard gates. The corrected Phase 1C input was therefore 16 clusters, verified by both `20 - 4 = 16` and `22 - 6 = 16`.  
**Source basis:** `02_PHASE_HISTORY/Phase_1/Phase_1C_Concept_Synthesis/Phase1C_Concept_Synthesis.pdf` (**TIER_4**, historical correction).

### Phase 1C — Concept Synthesis

Phase 1C created exactly one high-level concept per corrected survivor cluster, compared the 16 concepts and selected five for faculty presentation and later patent analysis. It expressly excluded patent searches, circuit design, component selection, software/firmware architecture and detailed implementation planning.  
**Source basis:** `02_PHASE_HISTORY/Phase_1/Phase_1C_Concept_Synthesis/Phase1C.md` (**TIER_4**); `02_PHASE_HISTORY/Phase_1/Phase_1C_Concept_Synthesis/Phase1C_Memory.md` (**TIER_4**); `02_PHASE_HISTORY/Phase_1/Phase_1C_Concept_Synthesis/Phase1C_Concept_Synthesis.pdf` (**TIER_4**).

The historical Top Five were OpenBraille, VibeGuard, TrueMoist, TrustLatch and ColdTrace. Their Phase 1C order was an early comparative recommendation, not the current final project decision.  
**Source basis:** `02_PHASE_HISTORY/Phase_1/Phase_1C_Concept_Synthesis/Phase1C_Concept_Synthesis.pdf` (**TIER_4**).

## 02.3 Phase 2 patent-landscape work

Phase 2 was a historical patent-landscape consolidation for the five Phase 1C concepts. Four research passes were commissioned, but only three contained usable patent-landscape findings. Three sections of one report were excluded because it interpreted OpenBraille as an embosser, VibeGuard as a phone anti-theft alarm and TrustLatch as a door lock. This was the first major demonstration of the concept-grounding and exclusion-over-averaging rule.  
**Source basis:** `02_PHASE_HISTORY/Phase_2_Patent_Landscape/Phase2_Memory.md` (**TIER_4**); PDR-004/PDR-006 in Decision Register v1.2 (**TIER_1**).

Phase 2 produced historically useful concerns and candidate directions, including OpenBraille manufacturing/firmware emphasis, VibeGuard single-node attribution uncertainty, TrueMoist validation burden, TrustLatch’s product-versus-patent fork and ColdTrace FTO concerns. These are historical inputs only. They do not establish current patent status, novelty, claim scope or freedom to operate.  
**Source basis:** `02_PHASE_HISTORY/Phase_2_Patent_Landscape/Phase2_Memory.md` (**TIER_4**); `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/09_Final_Downselection_README.md` (**TIER_2**, patent warning).

## 02.4 Phase 3A through Phase 3C

### Phase 3A — Engineering Landscape

Phase 3A shifted from patent questions to engineering state of the art, common approaches, standards, hardware/software categories, maturity and unresolved engineering problems. It intentionally avoided implementation selection. The official concept-grounding rule and multi-model audit process were strengthened after recurring concept-fidelity failures.  
**Source basis:** `02_PHASE_HISTORY/Phase_3/Phase_3A_Engineering_Landscape/Phase3A_MEMORY.md` (**TIER_4**); `02_PHASE_HISTORY/Phase_3/Phase3_SOP.md` (**TIER_4**).

### Engineering Design Review

The EDR stabilized each concept’s engineering identity, mission, hypothesis, fixed design principles and minimum demonstrable success before feasibility and architecture work. It approved all five concepts to proceed to Phase 3B and explicitly deferred elimination until objective evidence existed.  
**Source basis:** `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/00_Engineering_Design_Review.md` (**TIER_2**).

### Phase 3B — Engineering Feasibility

Phase 3B compared candidate technologies and feasibility without choosing final architectures. It again excluded concept-swapped report sections rather than averaging them. It identified OpenBraille as the principal mechanical/team-fit strategic fork, VibeGuard as a strong team-fit concept with unresolved single-node attribution, TrueMoist as low-risk but validation-intensive, TrustLatch as feasible with scope/flash constraints and ColdTrace as feasible with thermal-model and battery risks. At that stage, all five were allowed to proceed toward Phase 3C.  
**Source basis:** `02_PHASE_HISTORY/Phase_3/Phase_3B_Feasibility_Analysis/Phase3B_MEMORY.md` (**TIER_4**); `02_PHASE_HISTORY/Phase_3/Phase_3B_Feasibility_Analysis/Phase3B_Report_by_Claude.md` (**TIER_4**).

### Phase 3C — Architecture Selection and Retained-Portfolio Closure

Phase 3C froze one architecture each for OpenBraille, VibeGuard and TrueMoist. TrustLatch and ColdTrace were deferred before completing concept-specific Phase 3C architecture work. The approved closure memo states that the next action was a formal comparison among the retained three.  
**Source basis:** `02_PHASE_HISTORY/Phase_3/Phase_3C_Comparative_Evaluation/Original_Phase3C_README.md` (**TIER_4**, historical record); `02_PHASE_HISTORY/Phase_3/Phase_3C_Comparative_Evaluation/Phase3C_Portfolio_Closure_Memo_Approved.md` (**TIER_4**); Decision Register v1.2 PDR-064 to PDR-067 (**TIER_1**, controlling current state).

The Phase 3C raw research and prompts in the concept portfolio are historical evidence of exploration. They do not override the final architecture decisions and must not be cited as though every explored option remained current.

## 02.5 Research-lane and model-output controls

The controlled methodology requires:

- multiple independent research systems for coverage, not voting;
- preservation of duplicate findings before consolidation when duplicates indicate independent recurrence;
- mandatory restatement/confirmation of the supplied concept before analysis;
- complete exclusion of concept-swapped or inseparably mis-scoped sections;
- preservation of technically justified minority risks rather than averaging them away;
- explicit separation of facts, source inference, recommendations, simulations and final decisions;
- no reconstruction of missing conclusions from fragments;
- raw model research below governing decisions, frozen architectures and audited synthesis.

**Source basis:** PDR-004, PDR-005, PDR-006, PDR-039 and PDR-041 in Decision Register v1.2 (**TIER_1**); `02_PHASE_HISTORY/Phase_3/Phase_3B_Feasibility_Analysis/Phase3B_MEMORY.md` (**TIER_4**); `04_COMPARATIVE_DECISION/COMPARATIVE_DECISION_INDEX.md` (**TIER_2**).

## 02.6 Historical limitations

The phase records explain how Project mC evolved, but they are not unqualified current truth. In particular:

- early rankings do not establish current selection;
- old patent searches do not establish current patent status or FTO;
- Phase 3A/3B candidate technologies do not override Phase 3C frozen architectures;
- “ready” statements do not prove a physical build or authorize Phase 4;
- historical prices and specifications require a fresh verification pass before publication or procurement;
- historical model agreement does not establish truth;
- early broad concept names such as “controller,” “spatially isolated,” or “standard Braille” must be reconciled to later frozen scope.

**Source basis:** `02_PHASE_HISTORY/HISTORICAL_RESEARCH_INDEX.md` (**TIER_4**); `02_PHASE_HISTORY/PHASE_HISTORY_INDEX.md` (**TIER_4**); attached authority protocol.

## 02.7 Material contradictions

| ID | Issue | Higher-authority source | Conflicting source | Resolution | Residual uncertainty |
|---|---|---|---|---|---|
| C02-01 | Phase 1B.5 reported 22 survivors versus corrected 16 | Corrected Phase 1C synthesis — **TIER_4** | Phase 1B.5 survivor record — **TIER_4** | The Phase 1C input was 16; six out-of-scope re-entries were removed and four Top-20 clusters had legitimate gate failures. | Historical Phase 1B.5 deliverables remain preserved and should be labelled before quotation. |
| C02-02 | Phase 2 ranking and warnings versus later engineering/architecture results | Decision Register v1.2 and final architectures — **TIER_1/3** | `Phase2_Memory.md` — **TIER_4** | Phase 2 findings remain historical patent context only. Later architecture and comparative evidence control current scope. | Current patent status still requires new primary-source verification. |
| C02-03 | Phase 3B says all five proceed toward Phase 3C | PDR-064/PDR-067 — **TIER_1** | `Phase3B_MEMORY.md` — **TIER_4** | Later closure narrowed the active set to three and deferred TrustLatch/ColdTrace. | Re-entry remains possible only under PDR-066. |
| C02-04 | Phase roadmap says Phase 3 pending | PDR-067 — **TIER_1** | `MC_Project_PHASE_DOC.md` progress block — **TIER_1**, stale | Use roadmap for method, not current status. | Approved roadmap status correction remains pending. |
| C02-05 | TrueMoist two-season/multi-soil hold versus one-soil semester architecture | PDR-049/PDR-058/PDR-063 — **TIER_1** | Phase 2 historical recommendation and PDR-012 future task | The semester MVP is one-soil, fixed-model compensation with early gates; multi-season/multi-soil remains a later validation task, not an MVP requirement. | Later generalization is untested. |
| C02-06 | “No implementation before patent validation” in early Phase 1C transition language versus later architecture planning | Current phase controls and frozen architectures — **TIER_1/3** | `Phase1C_Memory.md` — **TIER_4** | The statement was a historical sequencing rule for that stage, not a permanent prohibition. Current semester MVPs may be built without representing them as patentable. | Formal Phase 4 authorization remains open. |
| C02-07 | Independent model concurrence treated as confidence versus treated as votes | Decision Register and protocol — **TIER_1** | Some historical narrative language about redundancy increasing confidence — **TIER_4** | Independent recurrence may raise evidentiary confidence after fidelity audit, but models never count as votes or override sources. | Each claim still requires source-quality and concept-fidelity review. |

## 02.8 Draft-safe Chapter 02 statements

- Project mC used a staged problem-to-concept-to-architecture process intended to prevent premature solution generation.
- Phase 1A discovered problems; Phase 1B analyzed and clustered them; Phase 1B.5 applied engineering gates; Phase 1C generated and ranked high-level concepts.
- A later consistency correction established 16 valid Phase 1C survivor clusters, not 22.
- Phase 2 was historical patent-landscape work and included explicit exclusion of concept-swapped research.
- Phase 3A mapped engineering landscapes; the EDR stabilized concept identity; Phase 3B evaluated feasibility; Phase 3C froze architectures for the retained three concepts.
- TrustLatch and ColdTrace were deferred before their Phase 3C architectures were completed; they were not technically rejected.
- Independent research lanes were evidence sources, not votes.
- Historical patent findings, costs and technical assumptions require current verification before being presented as current facts.

## 02.9 Statements that must not be made

- “Phase 1B.5 produced the final correct 22-concept survivor list.”
- “All five concepts completed Phase 3C.”
- “Phase 2 proved patentability or FTO.”
- “The model majority determined the decision.”
- “Phase 3B selected the final hardware architecture.”
- “The Phase 1C concept names define the current technical design.”
- “No project may be built until a patent is verified.”
- “A historical readiness label proves the system was physically validated.”

# Chapter 03 — Portfolio Evolution and Concept Origins

## 03.1 Opportunity discovery and longlist development

The portfolio began with broad opportunity discovery rather than idea generation. Phase 1B organized the research into an historical 32-cluster dataset, ranked a Top 20 and parked or eliminated lower-ranked opportunities. Phase 1B.5 then applied harder feasibility and innovation gates. A later scope audit removed six clusters that had improperly re-entered from outside the Top 20 and confirmed four legitimate Top-20 eliminations, leaving 16 valid Phase 1C inputs.  
**Source basis:** `02_PHASE_HISTORY/Phase_1/Phase_1A_Opportunity_Discovery/Phase1A_Memory.md` (**TIER_4**); `02_PHASE_HISTORY/Phase_1/Phase_1B_Opportunity_Analysis/Phase1B_Memory.md` (**TIER_4**); `02_PHASE_HISTORY/Phase_1/Phase_1C_Concept_Synthesis/Phase1C_Concept_Synthesis.pdf` (**TIER_4**).

The 16 historical Phase 1C concepts were:

1. SignalGuard — Offline Vital-Sign Confidence Monitor;
2. FallSense — Privacy-Preserving Ambient Fall & Distress Monitor;
3. AuscultAI — Offline Acoustic Screening Assistant;
4. ColdTrace — Multi-Modal Cold-Chain Integrity Logger;
5. OpenBraille — Low-Cost Refreshable Braille Display Module;
6. VibeGuard — Spatially-Isolated Bearing Fault Early-Warning Node;
7. OTShield — Inline Legacy-Protocol Anomaly Gateway;
8. ToolPulse — Real-Time Tool-Wear Signature Monitor;
9. GasPrint — Multi-Gas Fingerprinting Safety Monitor;
10. PanelWatch — Solar Panel Micro-Crack & Degradation Early-Warning Node;
11. TrueMoist — Drift-Self-Correcting Soil Moisture Controller;
12. CalibNet — Peer-Referenced Self-Calibrating Air Quality Node;
13. FloodPulse — Debris-Resistant Flood Water-Level Early-Warning Node;
14. TrustLatch — Accessible Secure-Boot & Signed-OTA Toolkit;
15. SiliconFingerprint — SRAM-Based Physical Unclonable Function;
16. SpanSense — Edge-Computed Fatigue-Tracking Bridge Monitor.

These names are historical concept labels, not current architecture definitions.

## 03.2 Portfolio narrowing

Phase 1C recommended the historical Top Five:

1. OpenBraille;
2. VibeGuard;
3. TrueMoist;
4. TrustLatch;
5. ColdTrace.

**Source basis:** `02_PHASE_HISTORY/Phase_1/Phase_1C_Concept_Synthesis/Phase1C_Concept_Synthesis.pdf` (**TIER_4**).

The portfolio later narrowed again. OpenBraille, VibeGuard and TrueMoist completed concept-specific Phase 3C architecture work and entered final comparative down-selection. TrustLatch and ColdTrace were deferred because the retained three already supplied sufficient decision diversity and the additional research burden was judged to have diminishing decision value. The deferral was strategic and reversible, not a technical failure.  
**Source basis:** PDR-064 to PDR-067 in Decision Register v1.2 (**TIER_1**); `02_PHASE_HISTORY/Phase_3/Phase_3C_Comparative_Evaluation/Phase3C_Portfolio_Closure_Memo_Approved.md` (**TIER_4**, historical closure record); `03_CONCEPT_PORTFOLIO/Other_Concepts/README.md` (**TIER_4**).

## 03.3 Origins of OpenBraille

OpenBraille originated from opportunity cluster OC-08, “Low-Cost Assistive Communication & Mobility Devices.” Its Phase 1C concept sought a low-cost refreshable Braille display module, initially at a high level and without a frozen actuator or mechanical architecture. The early concept was selected partly for social impact, demonstration value and an apparent actuation-cost innovation opportunity.  
**Source basis:** `02_PHASE_HISTORY/Phase_1/Phase_1C_Concept_Synthesis/Phase1C_Concept_Synthesis.pdf` (**TIER_4**).

The EDR later defined the enduring identity as affordable refreshable tactile output through a lower-cost actuation strategy, without requiring commercial-display performance. Phase 3C exploration considered multiple actuator and mechanical candidates before the Decision Register froze the present design: one macro-scale six-dot cell, six SG90-class servos, six eccentric cams/followers and guided vertical pins, ESP32 direct PWM, FDM manufacture and external regulated servo power.  
**Source basis:** `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/00_Engineering_Design_Review.md` (**TIER_2**, identity); PDR-015 to PDR-022 in Decision Register v1.2 (**TIER_1**, current architecture); `03_CONCEPT_PORTFOLIO/OpenBraille/06_Historical_Phase3C_Research_and_Prompts/Prompts/Phase3C_OpenBraille_Deep_Research_Prompt_Final.md` (**TIER_4**, historical exploration only).

The macro cell explicitly abandons dimensional compliance. It may be described as a non-standard mechanical/tactile proof-of-concept, not as an ISO-compliant commercial reading cell. Moving-roller, encoder-wheel, RAMPS/Mega and electromagnetic alternatives are not the current OpenBraille design.

## 03.4 Origins of VibeGuard

VibeGuard originated from OC-10, “Vibration-Based Predictive Maintenance for Rotating Machinery.” The Phase 1C name emphasized a spatially isolated bearing-fault early-warning node and presented single-node noise isolation as a differentiating ambition.  
**Source basis:** `02_PHASE_HISTORY/Phase_1/Phase_1C_Concept_Synthesis/Phase1C_Concept_Synthesis.pdf` (**TIER_4**).

The EDR retained the core identity of local, low-cost embedded analysis of machine vibration and defined success as distinguishing normal from deliberately abnormal operation without cloud processing. Phase 3C then froze a narrower semester MVP: one rigidly mounted ADXL345-class accelerometer, ESP32, local time-domain features, RMS-plus-persistence minimum classification, triggered FFT for explanation/comparison, optional ordinary Mahalanobis comparison, RGB indication, USB logging and a controlled motor/fan rig.  
**Source basis:** `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/00_Engineering_Design_Review.md` (**TIER_2**); PDR-023 to PDR-030/PDR-054 in Decision Register v1.2 (**TIER_1**).

Dense-machine source attribution, advanced interference handling and PIRG-style guarded learning are later research paths. They are not completed capabilities of the semester MVP. A software-security or configuration-scanner concept is a rejected concept swap and must not re-enter VibeGuard’s identity.

## 03.5 Origins of TrueMoist

TrueMoist originated from OC-15, “Precision Irrigation & Drift-Self-Correcting Soil Sensing.” The Phase 1C title “Drift-Self-Correcting Soil Moisture Controller” was broad and suggested a possible controller/product direction.  
**Source basis:** `02_PHASE_HISTORY/Phase_1/Phase_1C_Concept_Synthesis/Phase1C_Concept_Synthesis.pdf` (**TIER_4**).

Phase 3C narrowed the semester project to a measurement and compensation experiment, not irrigation control. The frozen architecture uses a genuine analog capacitive probe, DS18B20 temperature measurement, controlled salt addition per dry soil mass as a treatment code, ESP32, an evidence-gated ADS1115 path, fixed offline-trained regression coefficients, USB CSV logging, one homogeneous soil source and 72 independent physical runs against dry-basis gravimetric truth.  
**Source basis:** PDR-031/PDR-032/PDR-045/PDR-048 to PDR-050/PDR-058 to PDR-063 in Decision Register v1.2 (**TIER_1**).

The salinity code is not live soil EC, pore-water EC, apparent EC or solution conductivity. The MVP is not universal across soils, does not use online adaptive learning, does not require custom multi-frequency probe hardware and does not include irrigation control.

## 03.6 Retained non-finalist concepts

TrustLatch and ColdTrace are the two historical Top Five concepts that did not become final Phase 3C comparison candidates.

- **TrustLatch** remains a documented secure-boot/firmware-integrity concept with strong cybersecurity and educational value, but its Phase 3C architecture was not completed. Its historical dossier should be used only to explain origin and retained value.  
  **Source basis:** `03_CONCEPT_PORTFOLIO/Other_Concepts/TrustLatch/HISTORICAL_Phase1C_TrustLatch_Concept_Dossier.docx` (**TIER_4**); PDR-064/PDR-066 (**TIER_1**).
- **ColdTrace** remains a deferred cold-chain sensing/modeling concept with preserved Phase 2/3B evidence. It was not technically rejected, but it is dormant unless PDR-066 re-entry conditions are met.  
  **Source basis:** closure memo (**TIER_4**); Decision Register v1.2 (**TIER_1**).

The other eleven Phase 1C concepts remain historical portfolio material, not active final-selection candidates. Their presence demonstrates breadth and preserves traceability; it does not authorize further work or grant them equal current status.

## 03.7 Early concepts versus frozen architectures

| Concept | Early concept framing | Frozen current semester identity | Historical elements that must not be presented as current |
|---|---|---|---|
| OpenBraille | Low-cost refreshable Braille module; actuator not yet selected | Six-servo macro cell with eccentric cams, guided pins, direct ESP32 PWM and external servo power | Moving roller/encoder/RAMPS embosser; electromagnetic substitution; standard-size compliance; unproven passive reset |
| VibeGuard | Spatially isolated bearing-fault node with ambitious single-node discrimination | ADXL345 + ESP32 Level-1 local normal/abnormal vibration monitor; RMS/persistence baseline; triggered FFT; controlled rig | Software-security scanner; sensor array; cloud/RUL system; completed dense-machine attribution; PIRG as built functionality |
| TrueMoist | Drift-self-correcting soil moisture controller, broadly framed | One-soil local compensation instrument with temperature and controlled salinity-treatment code, fixed coefficients and gravimetric validation | Live EC meter; irrigation controller; universal/multi-soil system; TinyML showcase; online adaptive learner; custom multi-frequency probe |
| TrustLatch | Secure-boot and signed-OTA toolkit concept | No completed Phase 3C frozen architecture in the retained comparison | Treating provisional Phase 1C/3B ideas as a final implementation |
| ColdTrace | Multi-modal cold-chain integrity logger | No completed Phase 3C frozen architecture in the retained comparison | Treating provisional thermal-mass/RTC choices as final active architecture |

**Controlling source:** Decision Register v1.2 (**TIER_1**) for the retained three; Phase 1C and historical concept records (**TIER_4**) for origins only.

## 03.8 Material contradictions

| ID | Issue | Higher-authority source | Conflicting source | Resolution | Residual uncertainty |
|---|---|---|---|---|---|
| C03-01 | Phase 1B.5 22 survivors versus Phase 1C 16 | Corrected Phase 1C synthesis — **TIER_4** | Phase 1B.5 survivor list — **TIER_4** | Use 16 as the valid concept-synthesis input. | Historical reports need explicit annotation when reused. |
| C03-02 | Phase 1C Top Five ranking versus current portfolio/selection state | Decision Register v1.2 — **TIER_1** | Phase 1C synthesis — **TIER_4** | Top Five ranking is historical; only three reached retained Phase 3C comparison, and no final teacher-approved winner is attached. | Final selection remains open. |
| C03-03 | OpenBraille portrayed as easy without mechanical expertise | Later EDR/Phase 3B/current uncertainty register — **TIER_2/4** | Phase 1C recommendation language — **TIER_4** | Later evidence controls: OpenBraille is buildable only with explicit mechanical, power and tactile gates; team-fit risk is material. | Physical coupon results are absent. |
| C03-04 | OpenBraille as standard readable Braille versus permanent macro scale | PDR-016 — **TIER_1** | Early concept/presentation language and team objections | Describe it as a non-standard macro proof-of-concept. Do not claim ISO compliance or fluent commercial reading performance. | Human tactile protocol and acceptance threshold remain open. |
| C03-05 | VibeGuard “spatially isolated” as current capability | PDR-026/PDR-027 and uncertainty register — **TIER_1/2** | Phase 1C title and later patent-route language — **TIER_4/2** | Level-1 bench normal/abnormal classification is current; source attribution is later and unvalidated. | Field-like labels and site access remain unavailable. |
| C03-06 | TrueMoist “controller” and broad self-correction versus frozen measurement scope | PDR-049/PDR-058/PDR-062 — **TIER_1** | Phase 1C title and early research prompts — **TIER_4** | Current MVP is a one-soil measurement/compensation experiment with fixed coefficients and controlled salinity treatment. | Later transfer/generalization remains a hypothesis. |
| C03-07 | TrustLatch/ColdTrace as active Top Five versus deferred concepts | PDR-064/PDR-067 — **TIER_1** | Phase 1C/Phase 3B records — **TIER_4** | Preserve as deferred historical concepts, not active final candidates. | Re-entry conditional under PDR-066. |
| C03-08 | Raw Phase 3C candidate architectures versus final designs | Decision Register/final architecture hierarchy — **TIER_1/3** | Concept-packet prompts/raw research — **TIER_4** | Raw candidates show design exploration only and cannot override frozen architecture. | None. |

## 03.9 Draft-safe Chapter 03 statements

- The opportunity funnel moved from a broad 32-cluster historical dataset to a corrected 16-concept Phase 1C portfolio.
- Phase 1C selected OpenBraille, VibeGuard, TrueMoist, TrustLatch and ColdTrace as the historical Top Five.
- OpenBraille, VibeGuard and TrueMoist later completed Phase 3C architecture work; TrustLatch and ColdTrace were deferred.
- OpenBraille began as a broad low-cost refreshable Braille concept and was later frozen as a non-standard macro six-servo cell.
- VibeGuard began with a broader single-node spatial-attribution ambition and was narrowed to a controlled Level-1 bench MVP, with attribution retained as later research.
- TrueMoist began as a broad self-correcting/controller concept and was narrowed to one-soil local compensation with temperature and controlled salinity-treatment coding.
- Early concept names and raw research do not override later frozen architectures.
- Deferred concepts and non-finalist ideas remain valuable historical portfolio records without current active-candidate status.

## 03.10 Statements that must not be made

- “The Phase 1B.5 survivor count was unambiguously 22.”
- “The Phase 1C ranking is the final Project mC decision.”
- “OpenBraille is an ISO-compliant Braille display.”
- “VibeGuard already performs proven dense-machine source attribution.”
- “TrueMoist measures live soil EC or controls irrigation.”
- “TrustLatch and ColdTrace were technically rejected.”
- “Raw Phase 3C research options are still approved alternatives to the frozen architecture.”
- “The three retained concepts may be merged into one project.”

# Chapter 09 — Comparative Decision and Proposed Concept Shift

## 09.1 Comparative method

The common comparison package defined seven hard gates:

- G1 budget;
- G2 timeline;
- G3 team executability;
- G4 measurable minimum demonstrable success;
- G5 access to parts/fabrication/facilities/validation;
- G6 credible patent-development path;
- G7 absence of a fatal unresolved dependency.

It also defined a future 100-point rubric weighted toward patent-development potential (35), two-month buildability (20), validation strength (15), team fit (10), demonstration (8), budget/procurement certainty (7) and commercial/social significance (5). The initial evidence package intentionally left all score and ranking cells blank and did not select a winner.  
**Source basis:** `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/01_Comparison_Protocol.md` (**TIER_2**); `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/07_Scoring_Worksheet.md` (**TIER_2**); `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/09_Final_Downselection_README.md` (**TIER_2**).

The later adjudications added scoring and conditional decision models, but they remain independent decision-support outputs rather than votes or approvals. Their disagreement must be preserved.

## 09.2 Common evidence and hard gates

The repository-only precheck eliminated no concept. It found:

- all three had provisional implementation paths;
- all three had G6 **Insufficient Evidence** until current patent verification;
- OpenBraille depended on mechanical coupon, power, reset and tactile tests;
- VibeGuard depended on repeatable mounting/rig data, quantitative success thresholds and later attribution/site access;
- TrueMoist depended on probe repeatability, gravimetric facilities, dataset throughput and early model gates.

**Source basis:** `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/04_Hard_Gate_Precheck.md` (**TIER_2**); `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/05_Uncertainty_and_Test_Register.md` (**TIER_2**).

The high-reasoning audit confirmed that scores and rankings in the original package remained blank, current procurement quotes and experimental data were unavailable, and current patent-family/claim/FTO information was not established. It declared the package ready for a later current patent-verification pass, not ready to claim patentability.  
**Source basis:** `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/08_High_Reasoning_Audit.md` (**TIER_2**).

## 09.3 OpenBraille comparative position

**Semester strengths:** strong social and visual/tactile demonstration; bounded one-cell architecture; direct connection between build and physical evidence; BOM historically below the ceiling.  
**Semester weaknesses:** precision FDM mechanics, cam/guide friction, repeatability, active retraction, six-servo power, tactile protocol and team mechanical fit.  
**Current patent position:** the ordinary six-servo macro-cell MVP is not established as an invention. D11 and VPD-C7 are later physical-state verification/datum hypotheses requiring ground truth, ablation, robustness, practical-scale work and refreshed prior-art/IPR review.  
**Source basis:** Decision Register v1.2 (**TIER_1**); hard-gate precheck and uncertainty register (**TIER_2**); both final adjudications (**TIER_2**, conditional evidence).

The two adjudications treat OpenBraille differently:

- Work Max deprioritizes it for patent-first selection unless later D11-type gates pass.
- Deep Research High identifies OpenBraille D11 as the best conditional post-MVP patent-development candidate and recommends a ten-day physical-state observability gate.

Neither adjudication establishes patentability or teacher selection.

## 09.4 VibeGuard comparative position

**Semester strengths:** both adjudications independently identify VibeGuard as the best semester-build candidate. Its frozen Level-1 system has the simplest physical build, low historical BOM, strong team fit, clear live state-change demonstration and modular electronics/firmware/test workflow.  
**Semester weaknesses:** sensor authenticity, rigid-mount reproducibility, safe fault injection, sampling integrity, locked thresholds and honest held-out validation still require work.  
**Current patent position:** the ordinary feature stack is treated as conventional. The later PIRG/source-attribution/ambiguity-guarded path is a prospective research mechanism whose decisive evidence depends on target-specific information surviving interference/remounts and on independently labelled field-like access.  
**Source basis:** Decision Register v1.2 (**TIER_1**); uncertainty register (**TIER_2**); `01_Project_mC_Final_Adjudication_Work_Max.md` and `02_Project_mC_Final_Adjudication_Deep_Research_High.md` (**TIER_2**).

The Work Max adjudication recommends a VibeGuard Level-2A Signal-and-Access Gate and makes TrueMoist the fallback if it fails. The Deep Research High adjudication instead makes VibeGuard the fallback after an OpenBraille gate. This difference is unresolved.

## 09.5 TrueMoist comparative position

**Semester strengths:** most explicit quantitative validation design, gravimetric ground truth, fixed thresholds, strong publication value and a well-defined one-soil factorial experiment.  
**Semester weaknesses:** oven/scale access, probe repeatability, packing/insertion control, drying throughput, salinity-treatment effect and 72-run workload.  
**Current patent position:** the semester regression/compensation MVP is not automatically patentable. Later replacement/remount transfer, reference-challenge, validity-state and contaminated-update-blocking mechanisms are hypotheses requiring multi-unit/lots evidence and current prior-art/FTO review.  
**Source basis:** Decision Register v1.2 (**TIER_1**); hard-gate precheck/uncertainty register (**TIER_2**); final adjudications (**TIER_2**).

The Work Max adjudication identifies TrueMoist as the best post-MVP patent-development candidate and fallback to VibeGuard. The Deep Research High adjudication deprioritizes it for the current patent-first choice while retaining it as a rigorous measurement/publication path. No higher authority resolves this disagreement.

## 09.6 Final adjudication context

The two final adjudications are both concept-faithful, but their decision models differ materially:

| Decision point | Work Max adjudication | Deep Research High adjudication | Reconciled status |
|---|---|---|---|
| Best semester build | VibeGuard | VibeGuard | Strong agreement: VibeGuard is the best semester-build candidate within the adjudication evidence. This is still a recommendation, not approval. |
| Best later patent-development candidate | TrueMoist | OpenBraille D11, conditionally | Unresolved. Neither output overrides the other or proves patentability. |
| Immediate action | Run VibeGuard Level-2A Signal-and-Access Gate | Run OpenBraille D11 Physical-State Observability Gate | Unresolved gate choice. Requires authorized project decision. |
| Fallback | TrueMoist if VibeGuard gate fails | VibeGuard if OpenBraille gate fails | Unresolved because it follows the unresolved gate choice. |
| Deprioritized patent-first path | OpenBraille | TrueMoist | Unresolved. Both preserve the deprioritized concept as a strong prototype/publication/research option. |

**Source basis:** `04_COMPARATIVE_DECISION/02_Final_Adjudications/01_Project_mC_Final_Adjudication_Work_Max.md` (**TIER_2**); `04_COMPARATIVE_DECISION/02_Final_Adjudications/02_Project_mC_Final_Adjudication_Deep_Research_High.md` (**TIER_2**); `04_COMPARATIVE_DECISION/COMPARATIVE_DECISION_INDEX.md` (**TIER_2**, adjudications are context, not votes).

The common defensible conclusion is narrower than either adjudication’s complete recommendation:

1. VibeGuard has the strongest semester-build case.
2. No frozen MVP is established as a patentable invention.
3. The patent-first decision is sensitive to a short, named feasibility gate.
4. The attachments do not contain an authorized decision choosing which gate controls.
5. The attachments do not contain explicit teacher approval of the OpenBraille-to-VibeGuard shift.

## 09.7 Team objections and challenges

The team-submitted audit/challenge files are preserved as evidence of concerns, not automatic authority.

### OpenBraille feasibility disagreement

One team-submitted analysis, based on a subset of the evidence, initially described OpenBraille as the least risky semester build. A later team-submitted update that included the change request and VibeGuard roadmap reversed the conclusion toward VibeGuard. This demonstrates source-set sensitivity and cannot be treated as an independent deciding vote.  
**Source basis:** `04_COMPARATIVE_DECISION/04_Team_Audits_and_Objections/01_Team_Submission_6222246419165853974.pdf` and `02_Team_Submission_6282084529079524834.pdf` (**TIER_2**, team-submitted context).

### Macro Braille objection

The objection that macro scaling is not standards-compliant is consistent with PDR-016, which explicitly abandons dimensional compliance. The objection becomes overstated when it treats non-compliance as proof that the semester mechanism experiment has no value. The controlled resolution is to call the device a non-standard macro tactile/mechanical proof-of-concept and not claim standard Braille readability or commercial functionality.  
**Source basis:** PDR-016 (**TIER_1**); `03_Team_Submission_IDK.pdf` (**TIER_2**).

### ESP32/STM32 objection

The claim that the course strictly mandates STM32 and therefore makes ESP32 a fatal failure is not established by the controlling teacher-requirements attachment. The teacher record says STM32 was mentioned and final board choice requires authoritative records and teacher approval. The issue therefore remains an approval/verification item, not a settled fatal defect.  
**Source basis:** teacher context (**TIER_1**); `03_Team_Submission_IDK.pdf` (**TIER_2**).

### Power objection

The objection that six SG90-class servos may exceed the practical 5 V/2 A supply margin is materially relevant. It does not automatically overturn the frozen architecture, but it prevents the manual from describing the supply as experimentally validated. Staged one-servo and six-servo current/brownout/stall tests remain mandatory.  
**Source basis:** PDR-020/PDR-022 (**TIER_1**); uncertainty register U-OB-03 (**TIER_2**); team objection (**TIER_2**).

### Presentation-quality objections

Hardware terminology and a missing block diagram may be valid presentation/document-quality issues, but they do not themselves determine concept feasibility or the comparative selection. They belong primarily in Chapter 10’s presentation record and quality-control treatment.

## 09.8 Proposed OpenBraille-to-VibeGuard shift

### What was recommended

- Both adjudications recommend VibeGuard as the best semester-build candidate.
- The teacher-context document records the team’s reasons for preferring VibeGuard: stronger three-month feasibility, simpler physical implementation, better team fit, clearer quantitative validation, stronger live demonstration and lower dependence on precision mechanics.
- The formal change-request document recommends VibeGuard as the lower-risk, better-aligned semester implementation while preserving OpenBraille as documented accessibility/mechatronics work.

**Source basis:** teacher context (**TIER_1**); both adjudications and change request (**TIER_2**).

### What was formally requested

The team formally requested approval to replace the frozen OpenBraille semester implementation with the frozen VibeGuard Level-1 architecture, retain OpenBraille as a future accessibility/mechatronics path, and freeze VibeGuard procurement and roles only after approval.  
**Source basis:** `04_COMPARATIVE_DECISION/03_Change_Request/Project_mC_Request_to_Change_from_OpenBraille_to_VibeGuard.docx` (**TIER_2**).

### What was approved

No explicit teacher approval is proved by the attached sources. The change-request teacher-decision field remains an uncompleted choice among “Approved / Approved with conditions / Not approved,” with blank conditions, signature and date. No separate approval record is attached.

### What remains unresolved

- whether the teacher approves the change;
- whether ESP32 is accepted for the selected course implementation or an STM32 substitution is required;
- whether the team adopts the Work Max VibeGuard gate, the Deep Research High OpenBraille gate, or a different authorized selection rule;
- whether procurement, Phase 4 entry and named role allocation may begin;
- which future patent-development hypothesis, if any, survives physical experiments and current prior-art review.

## 09.9 Material contradictions

| ID | Issue | Higher-authority source | Conflicting source | Resolution | Residual uncertainty |
|---|---|---|---|---|---|
| C09-01 | Neutral precheck package versus later populated adjudication scores | Later adjudications — **TIER_2**, decision support | Original comparison package — **TIER_2**, intentionally blank | The package was a preparation stage; adjudications are later analyses. Neither is teacher approval. | Choice between adjudication models remains unresolved. |
| C09-02 | Best later patent candidate: TrueMoist versus OpenBraille D11 | No higher source resolves | Work Max versus Deep Research High — both **TIER_2** | Preserve both as competing conditional assessments. | Requires gate results, current patent search and authorized decision. |
| C09-03 | Which gate should precede selection | No higher source resolves | VG-SAG versus OpenBraille D11 gate — both **TIER_2** | Do not choose silently. Record as an open governance decision. | Project owner/teacher must authorize one route. |
| C09-04 | VibeGuard proposed shift versus current approved project | Teacher/approval rule — **TIER_1** | Change request — **TIER_2** | The shift is proposed, not confirmed. | Teacher decision absent. |
| C09-05 | OpenBraille least-risk claim in one team submission versus VibeGuard best-build adjudication consensus | Controlling comparative evidence/adjudications — **TIER_2**, broader evidence | Team submission based on narrower source set — **TIER_2** | Treat team submission as a challenge, not a controlling result. Both adjudications support VibeGuard for semester build. | Actual build data could still change the result. |
| C09-06 | Macro-scale OpenBraille called unusable/fatal versus deliberate proof-of-concept scope | PDR-016 — **TIER_1** | Team objection — **TIER_2** | It is non-standard by design; this limits claims but does not erase mechanical proof-of-concept value. | Tactile acceptance protocol remains unapproved. |
| C09-07 | ESP32 described as fatal syllabus mismatch versus teacher context | teacher requirements — **TIER_1** | team objection — **TIER_2** | No categorical ban is established in the attachments. Board acceptance requires explicit teacher/course verification. | Current official syllabus and teacher ruling are external/open. |
| C09-08 | OpenBraille 5 V/2 A supply accepted versus peak-current concern | Decision Register — **TIER_1** | uncertainty/team objection — **TIER_2** | Preserve frozen baseline, but classify adequacy as unvalidated and test before integration. | Physical power data absent. |
| C09-09 | Frozen VibeGuard Level-1 versus patent-route source attribution | Decision Register — **TIER_1** | adjudication future mechanisms — **TIER_2** | Keep Level-1 and later PIRG/attribution work separate. | Later mechanism is unbuilt and site-dependent. |
| C09-10 | Frozen TrueMoist one-soil model versus later transfer mechanism | Decision Register — **TIER_1** | adjudication future mechanism — **TIER_2** | Transfer/remount validity is post-MVP research, not part of the 72-run semester architecture. | Multi-unit evidence absent. |

## 09.10 Open decisions, tests and approvals

| Item | Evidence available | Current status | Required next action |
|---|---|---|---|
| Teacher approval of VibeGuard shift | Formal change request and rationale | Open | Obtain explicit written approval/conditions or rejection. |
| Selection-gate choice | Two conflicting final adjudication recommendations | Open | Authorize one gate or a documented replacement rule; do not average the adjudications. |
| VibeGuard Level-1 quantitative success threshold | MDS and uncertainty U-VG-07 | Not frozen in controlling register | Pre-register trial/session split, false-alert, missed-detection and repeatability criteria. |
| VibeGuard future attribution/site access | VG-SAG proposal and U-VG-04/U-VG-06 | Unverified | Secure independently labelable field-like access and run controlled interference/remount tests only as later research. |
| OpenBraille reset | PDR-021 | Pending physical inspection | Confirm passive return or freeze active cam retraction. |
| OpenBraille power | PDR-020 and U-OB-03 | Unvalidated | Measure one-servo and staged six-servo current, brownout and stall conditions. |
| OpenBraille tactile protocol | EDR MDS and U-OB-07 | Open | Approve blinded protocol, participant plan and quantitative acceptance threshold. |
| TrueMoist gravimetric facilities | PDR-048/PDR-061 | Pending | Obtain oven/scale access and complete a dry-to-constant-mass pilot. |
| TrueMoist probe/packing/salinity gates | PDR-061 | Pending | Execute Week-1/Week-2 gates before the main dataset. |
| Current patent status/FTO | Historical reports and adjudications only | Unavailable | Conduct current primary-source claim/status search and institutional/professional review after mechanism freeze. |
| Current prices and supplier authenticity | Historical/dated estimates | Unavailable for final publication/procurement | Refresh manufacturer specifications and Indian market quotes after concept/board approval. |
| Phase 4 and procurement start | No controlling authorization attached | Not started | Begin only after teacher/project authorization and gate/board resolution. |

## 09.11 Draft-safe Chapter 09 statements

- The common comparison framework used seven hard gates and a patent-first weighted rubric, but the initial evidence package intentionally selected no winner.
- All three concepts had provisional build paths and insufficient patent-path evidence before the later verification/adjudication work.
- Both final adjudications identify VibeGuard as the best semester-build candidate.
- The adjudications disagree on the best later patent path, the pre-selection gate and the fallback.
- No frozen semester MVP is established as a patentable invention.
- OpenBraille remains a valid accessibility/mechatronics prototype and future research path despite being lower-ranked for the proposed semester shift.
- VibeGuard’s frozen semester MVP is Level-1 local condition monitoring; dense-machine attribution and PIRG are later hypotheses.
- TrueMoist’s frozen semester MVP is one-soil local compensation; replacement/remount transfer is later research.
- The team has submitted a formal OpenBraille-to-VibeGuard change request, but teacher approval is not proved by the attached evidence.
- Team objections are preserved and reconciled against higher-authority sources rather than accepted or dismissed wholesale.

## 09.12 Statements that must not be made

- “The two adjudications voted for VibeGuard.”
- “VibeGuard has been finally selected or teacher-approved.”
- “The adjudications agree on the patent-development winner.”
- “OpenBraille has been disproved, exposed as a hoax, or abandoned as wasted work.”
- “OpenBraille is standards-compliant or ready for fluent Braille reading.”
- “VibeGuard’s dense-machine source attribution has been demonstrated.”
- “TrueMoist’s transfer/remount patent mechanism has been demonstrated.”
- “Any percentage band in an adjudication is a patentability probability.”
- “A change-request document is an approval record.”
- “The current prices, patent status, course-board rule or experimental performance have been freshly verified in this stage.”

# Cross-Chapter Reconciliation

## X.1 Consolidated contradiction register

| ID | Chapters | Issue | Controlling source | Conflicting source | Resolution | Remaining uncertainty |
|---|---|---|---|---|---|---|
| X-01 | 01, 02 | Current phase status | Decision Register v1.2 PDR-067 — **TIER_1** | stale roadmap and older registers — **TIER_1 historical** | Phase 3C complete for retained three only; Phase 4 not started. | Formal Phase 4 authorization. |
| X-02 | 01, 03, 09 | Active portfolio | PDR-064/PDR-066 — **TIER_1** | Phase 1C/3B five-concept records — **TIER_4** | Active comparison: OpenBraille, VibeGuard, TrueMoist. TrustLatch/ColdTrace deferred. | Conditional re-entry. |
| X-03 | 01, 09 | Proposed shift versus approval | Teacher context/Authority Map — **TIER_1** | change request — **TIER_2** | Request exists; approval does not. | Teacher decision. |
| X-04 | 01, 03, 09 | OpenBraille scope | Decision Register v1.2 — **TIER_1** | early broad concept, moving-roller swap, standard-reading assumptions | Frozen macro six-servo cell; non-standard proof-of-concept. | Reset, power, tactile tests. |
| X-05 | 01, 03, 09 | VibeGuard scope | Decision Register v1.2 — **TIER_1** | early “spatially isolated” framing and future PIRG | Frozen Level-1 ADXL345/ESP32 monitor; attribution is later. | Field/site evidence. |
| X-06 | 01, 03, 09 | TrueMoist scope | Decision Register v1.2 — **TIER_1** | early controller/live-EC/multi-soil implications | Frozen one-soil local compensation with temperature and treatment code. | Early physical gates and later transfer evidence. |
| X-07 | 02, 03 | Portfolio-count history | corrected Phase 1C synthesis — **TIER_4** | Phase 1B.5 22 survivors — **TIER_4** | Corrected Phase 1C input: 16. | Historical annotation. |
| X-08 | 02, 09 | Model-output role | Decision Register/protocol — **TIER_1** | model-majority or repeated-conclusion language | Evidence recurrence may inform confidence after audit; it never creates votes or authority. | Claim-specific source quality. |
| X-09 | 09 | Best patent-development route | no controlling resolution | two final adjudications — **TIER_2** | Preserve TrueMoist and conditional OpenBraille D11 as competing assessments. | Gate results and current patent verification. |
| X-10 | 09 | Pre-selection gate | no controlling resolution | VG-SAG versus OpenBraille D11 gate — **TIER_2** | Open decision requiring authorization. | Gate selection, execution and result. |
| X-11 | 01, 09 | ESP32/STM32 compliance | teacher context — **TIER_1** | team syllabus objection — **TIER_2** | STM32 was mentioned; no categorical resolution attached. Frozen board choice remains project truth pending teacher acceptance. | Official syllabus/teacher confirmation. |
| X-12 | 01, 09 | Patent language | authority protocol and Decision Register — **TIER_1** | optimistic historical/adjudication language | All future routes remain hypotheses; no grant, novelty, inventive-step or FTO promise. | Experiments, search and IPR review. |

## X.2 Current project-state statement

Project mC has completed Phase 3C architecture work for the retained OpenBraille, VibeGuard and TrueMoist concepts and has deferred TrustLatch and ColdTrace without technically rejecting them. The controlled evidence supports VibeGuard as the strongest semester-build candidate, and the team has formally requested permission to change the semester implementation from OpenBraille to VibeGuard while preserving OpenBraille as documented accessibility/mechatronics work. The attached records do not prove teacher approval, do not resolve the two adjudications’ conflicting pre-selection gates or later patent-path rankings, and do not authorize a claim that any frozen MVP is patentable.

## X.3 Semester-build versus future-research boundary

| Concept | Frozen semester build | Allowed implementation refinements | Post-semester/future research | Prohibited conflation |
|---|---|---|---|---|
| OpenBraille | Macro six-dot cell; six servos/cams; guided pins; ESP32 direct PWM; external servo power; active retraction unless passive return is proved | Tolerance tuning, power validation, tactile protocol, calibration and reliability logging within the same architecture | D11 current/physical-state observability; VPD-C7 pin-side datum evidence; practical-scale experiments; claim-focused research | Do not present D11/VPD-C7 as built, proven or part of the frozen MVP; do not substitute moving rollers or other architectures. |
| VibeGuard | One rigid ADXL345-class sensor; ESP32; RMS+persistence; triggered FFT; optional ordinary Mahalanobis comparison; RGB/USB; controlled motor/fan rig | Sensor acceptance, locked sampling, mount documentation, safe rig refinement and quantitative held-out validation | PIRG/source attribution, ambiguity/abstention, protected update, remount validity and field-like dense-machine studies | Do not claim Level-1 proves source attribution; do not convert to a sensor array, cloud/RUL system or software-security project. |
| TrueMoist | One soil; analog capacitive probe; DS18B20; controlled salinity-treatment code; ADS1115 gate; fixed regression; USB logs; 72 physical runs; gravimetric truth | Jig/packing control, ADC comparison, pilot model, documented fallback and threshold-preserving implementation changes | Probe replacement/remount transfer, reference challenges, population/lot studies, validity/contamination gating and multi-soil research | Do not add live EC, irrigation control, universal transfer, custom multi-frequency probes or online learning to the frozen MVP. |

## X.4 Claims requiring fresh external verification

This stage performs no external verification. The following claims must be rechecked before final publication, procurement, legal/IP decisions or teacher-facing assertion:

| Claim | Chapter | Why verification is required | Preferred primary source |
|---|---:|---|---|
| Current component specifications for ESP32 boards, ADXL345, ADS1115, DS18B20, SG90-class servos and power supplies | 01, 04, 06, 08, 09 | Manufacturer documents and available variants can change; historical records include provisional naming/specification assumptions | Current manufacturer datasheets and official board documentation |
| Current Indian prices, availability and supplier authenticity | 01, 09 | Historical or dated estimates are not procurement-ready | Manufacturer-authorized distributors and current reputable Indian retailer quotations |
| Whether PBCST504 or the specific teacher requires STM32 rather than merely allowing Arduino-IDE-compatible boards | 01, 09 | Team objection and teacher context conflict; attachment set contains no current official resolution | Current official university syllabus plus written teacher/project-coordinator decision |
| ISO/Braille dimensional requirements and the permissible description of the macro prototype | 03, 09 | The project intentionally abandons compliance; final wording should accurately distinguish a proof-of-concept from a standards-compliant reader | Current ISO standard text and authoritative accessibility/Braille design guidance |
| Current patent-family status, independent claims, continuations/divisionals and jurisdictional coverage | 02, 05, 07, 08, 09 | Repository research is historical and not a current legal/status search | Official patent-office databases and certified file histories |
| Novelty, inventive step, patent eligibility and FTO for D11, VPD-C7, PIRG and TrueMoist transfer/validity mechanisms | 05, 07, 08, 09 | No attachment provides legal clearance; mechanisms are unbuilt hypotheses | Current primary patent documents, claim charts and qualified institutional/professional review |
| OpenBraille six-servo current demand and 5 V/2 A adequacy | 01, 04, 09 | Accepted design choice is not experimentally validated | Physical current/voltage/brownout/stall measurements on selected parts |
| OpenBraille passive return and tactile-identification performance | 01, 04, 09 | PDR-021 remains pending and tactile acceptance is not frozen | Physical servo inspection, mechanical ground truth and approved blinded user protocol |
| VibeGuard quantitative Level-1 classification and future source attribution | 06, 09 | No locked experimental dataset is attached | Pre-registered bench/field experiments with independently labelled sessions/remounts |
| TrueMoist oven/scale access, probe repeatability, dataset throughput and compensation thresholds | 08, 09 | Architecture is ready only with mandatory early validation | Facility confirmation and pre-registered physical pilot/main experiment |

## X.5 Readiness verdict

| Chapter | Verdict | Source-grounded reason |
|---|---|---|
| Chapter 01 | **READY WITH EXPLICIT OPEN ITEMS** | The mandate, teacher constraints, authority order, Decision Register controls and repository rules are sufficiently reconciled. Teacher approval of the concept shift, board/course acceptance and Phase 4/procurement authorization remain open. |
| Chapter 02 | **READY FOR CONTROLLED DRAFTING** | The phase sequence, historical purpose, correction of the survivor count and authority boundary between historical research and current decisions are clear. Historical claims must retain their labels. |
| Chapter 03 | **READY FOR CONTROLLED DRAFTING** | The portfolio funnel, concept origins, retained/deferred status and frozen-architecture distinctions are clear. Early names must not be used as current design definitions. |
| Chapter 09 | **READY WITH EXPLICIT OPEN ITEMS** | The comparative method, concept positions, adjudication disagreement, team objections and proposed shift are reconciled. The teacher decision, gate choice, final selection and experiment/patent results remain unresolved. |

# Source Ledger

Only original organized-workspace paths materially relied upon in this reconciliation are listed. The four packet filenames and the Stage 10D manifest are not treated as technical sources.

## Chapter 01 — TIER_1

- `01_GOVERNANCE_AND_CONTROL/01_Project_Requirements/Teacher_Project_Requirements_and_Change_Context.md`
- `01_GOVERNANCE_AND_CONTROL/02_Decision_Registers/HISTORICAL_Project_mC_Decision_Register_v1.0.md` — historical/superseded comparison only
- `01_GOVERNANCE_AND_CONTROL/02_Decision_Registers/Project_mC_Decision_Register_v1.2.md`
- `01_GOVERNANCE_AND_CONTROL/03_Project_Context_and_Phase_Map/MC_Project_PHASE_DOC.md` — methodology; current status block superseded
- `01_GOVERNANCE_AND_CONTROL/03_Project_Context_and_Phase_Map/PROJECT_CONCEPT_CONTEXT.md` — original concept context only
- `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/AGENTS.md`
- `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Legacy_Repository_Audit/04_AUTHORITY_AMBIGUITIES.md`
- `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Original_Repository_README.md`
- `01_GOVERNANCE_AND_CONTROL/AUTHORITY_MAP.md`

## Chapter 02 — TIER_4 historical sources

- `02_PHASE_HISTORY/HISTORICAL_RESEARCH_INDEX.md`
- `02_PHASE_HISTORY/PHASE_HISTORY_INDEX.md`
- `02_PHASE_HISTORY/Phase_1/Phase_1A_Opportunity_Discovery/Phase1A_Memory.md`
- `02_PHASE_HISTORY/Phase_1/Phase_1B_Opportunity_Analysis/Phase1B_Memory.md`
- `02_PHASE_HISTORY/Phase_1/Phase_1B5_Portfolio_Optimization/Phase1B5_Memory.md`
- `02_PHASE_HISTORY/Phase_1/Phase_1C_Concept_Synthesis/Phase1C.md`
- `02_PHASE_HISTORY/Phase_1/Phase_1C_Concept_Synthesis/Phase1C_Memory.md`
- `02_PHASE_HISTORY/Phase_1/Phase_1C_Concept_Synthesis/Phase1C_Concept_Synthesis.pdf`
- `02_PHASE_HISTORY/Phase_2_Patent_Landscape/Phase2_Memory.md`
- `02_PHASE_HISTORY/Phase_3/Phase3_SOP.md`
- `02_PHASE_HISTORY/Phase_3/Phase_3A_Engineering_Landscape/Phase3A_MEMORY.md`
- `02_PHASE_HISTORY/Phase_3/Phase_3B_Feasibility_Analysis/Phase3B_MEMORY.md`
- `02_PHASE_HISTORY/Phase_3/Phase_3B_Feasibility_Analysis/Phase3B_Report_by_Claude.md`
- `02_PHASE_HISTORY/Phase_3/Phase_3C_Comparative_Evaluation/Original_Phase3C_README.md`
- `02_PHASE_HISTORY/Phase_3/Phase_3C_Comparative_Evaluation/Phase3C_Portfolio_Closure_Memo_Approved.md`

## Chapter 03 — TIER_4 historical sources

- `02_PHASE_HISTORY/Phase_1/Phase_1C_Concept_Synthesis/Phase1C_Concept_Synthesis.pdf`
- `03_CONCEPT_PORTFOLIO/OpenBraille/06_Historical_Phase3C_Research_and_Prompts/Prompts/Phase3C_OpenBraille_Deep_Research_Prompt_Final.md`
- `03_CONCEPT_PORTFOLIO/VibeGuard/06_Historical_Phase3C_Research_and_Prompts/Prompts/Phase3C_VibeGuard_Deep_Research_Prompt_Final.md`
- `03_CONCEPT_PORTFOLIO/TrueMoist/06_Historical_Phase3C_Research_and_Prompts/Prompts/Phase3C_TrueMoist_Deep_Research_Prompt_Final.md`
- `03_CONCEPT_PORTFOLIO/Other_Concepts/README.md`
- `03_CONCEPT_PORTFOLIO/Other_Concepts/TrustLatch/HISTORICAL_Phase1C_TrustLatch_Concept_Dossier.docx`

## Chapter 03 — controlling cross-chapter TIER_1/TIER_2 sources

- `01_GOVERNANCE_AND_CONTROL/02_Decision_Registers/Project_mC_Decision_Register_v1.2.md` — **TIER_1**
- `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/00_Engineering_Design_Review.md` — **TIER_2**

## Chapter 09 — TIER_2

- `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/00_Engineering_Design_Review.md`
- `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/01_Comparison_Protocol.md`
- `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/02_Authoritative_Source_Manifest.md`
- `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/03_Concept_Evidence_Matrix.md`
- `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/04_Hard_Gate_Precheck.md`
- `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/05_Uncertainty_and_Test_Register.md`
- `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/06_Patent_Research_Input_Pack.md`
- `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/07_Scoring_Worksheet.md`
- `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/08_High_Reasoning_Audit.md`
- `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/09_Final_Downselection_README.md`
- `04_COMPARATIVE_DECISION/02_Final_Adjudications/01_Project_mC_Final_Adjudication_Work_Max.md`
- `04_COMPARATIVE_DECISION/02_Final_Adjudications/02_Project_mC_Final_Adjudication_Deep_Research_High.md`
- `04_COMPARATIVE_DECISION/03_Change_Request/Project_mC_Request_to_Change_from_OpenBraille_to_VibeGuard.docx`
- `04_COMPARATIVE_DECISION/03_Change_Request/Project_mC_Request_to_Change_from_OpenBraille_to_VibeGuard.pdf`
- `04_COMPARATIVE_DECISION/04_Team_Audits_and_Objections/01_Team_Submission_6222246419165853974.pdf`
- `04_COMPARATIVE_DECISION/04_Team_Audits_and_Objections/02_Team_Submission_6282084529079524834.pdf`
- `04_COMPARATIVE_DECISION/04_Team_Audits_and_Objections/03_Team_Submission_IDK.pdf`
- `04_COMPARATIVE_DECISION/COMPARATIVE_DECISION_INDEX.md`

## Chapter 09 — controlling cross-chapter TIER_1 source

- `01_GOVERNANCE_AND_CONTROL/02_Decision_Registers/Project_mC_Decision_Register_v1.2.md`
- `01_GOVERNANCE_AND_CONTROL/01_Project_Requirements/Teacher_Project_Requirements_and_Change_Context.md`
- `01_GOVERNANCE_AND_CONTROL/AUTHORITY_MAP.md`
