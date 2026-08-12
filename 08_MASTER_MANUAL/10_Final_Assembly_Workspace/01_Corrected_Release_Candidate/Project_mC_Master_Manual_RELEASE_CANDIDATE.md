# Project mC Master Manual

## Corrected Controlled Release Candidate

## Document control

| Field | Value |
|---|---|
| Document | Project mC Master Manual |
| Assembly status | Corrected controlled release candidate; targeted re-review pending |
| Candidate assembly date | `2026-08-05T19:47:44.541310+02:00` |
| Main parts | Parts I–VI |
| Chapters | 00–14 |
| Appendices | A1–A4 |
| Current semester recommendation | VibeGuard |
| Teacher approval of proposed shift | Not proved |
| Phase 4 / procurement | Not proved started |
| Patent effect | No patentability, filing, infringement or FTO conclusion |
| Source effect | Corrected component hashes and paths preserved in assembly markers |
| External verification | Current external facts remain reserved for later verification |
| Embedded component status | Part- and appendix-level “Controlled draft” labels preserve the status of the validated source components at assembly; the root release status controls the integrated manual. |
| Final release metadata | Deferred until targeted re-review and named reviewer/sign-off are complete |

## Current-state notice

VibeGuard remains the strongest semester-build recommendation. The proposed
OpenBraille-to-VibeGuard shift is not proved teacher-approved. OpenBraille,
VibeGuard and TrueMoist remain separate controlled records. Final course-
platform acceptance remains unresolved. Chapter 11 remains a future execution
framework with zero directly mapped execution sources. Project-wide Phase 4
and procurement are not proved started. No frozen MVP is established as
patentable.

## Contents

- Part I — Opening, Governance, History and Decision
  - Chapter 00 — Executive Overview
  - Chapter 01 — Project Mandate, Requirements and Governance
  - Chapter 02 — Methodology and Phase History
  - Chapter 03 — Portfolio Evolution
  - Chapter 09 — Comparative Decision and Proposed Shift
- Part II — OpenBraille Architecture and Patent Path
  - Chapter 04 — OpenBraille Frozen Architecture
  - Chapter 05 — OpenBraille Patent and Future Research Path
- Part III — VibeGuard Architecture and Patent Path
  - Chapter 06 — VibeGuard Frozen Architecture
  - Chapter 07 — VibeGuard Patent and Future Research Path
- Part IV — TrueMoist Architecture, Evidence and Research Position
  - Chapter 08 — TrueMoist
- Part V — Teacher Review and Semester Execution
  - Chapter 10 — Teacher Reviews and Presentation Record
  - Chapter 11 — Semester Execution Framework
- Part VI — Provenance, Archive and Source Integrity
  - Chapter 12 — Research Provenance and AI Workflow Control
  - Chapter 13 — Superseded, Failed, Partial and Archived Routes
  - Chapter 14 — Source Integrity Audit and Reproducibility
- Appendix A1 — Complete Source Register
- Appendix A2 — Peer Project and Reference Register
- Appendix A3 — Glossary and Acronyms
- Appendix A4 — Open Decisions and Change Log

**Controlled reading-order note:** Chapter numbers retain the blueprint
identifiers. The integrated reading order follows validated Part grouping, so
Chapter 09 appears in Part I before Chapters 04–08; this is intentional and
does not indicate omission or duplication.


---

<!-- BEGIN CONTROLLED COMPONENT: PART_I_RELEASE_CORRECTED -->
<!-- SOURCE PATH: /home/paradoxpete/Documents/PROJECT_ORGANIZED/08_MASTER_MANUAL/10_Final_Assembly_Workspace/01_Corrected_Release_Candidate/01_Corrected_Components/Project_mC_Master_Manual_Part_I_Opening_Governance_History_and_Decision_RELEASE_CORRECTED.md -->
<!-- SOURCE SHA-256: 00055290da6a36eee8aacd4a32b1b26fe76f4a7438a03fc632623b4eed57a3b0 -->

## Part I — Opening, Governance, History and Comparative Decision

## Document control

| Field | Value |
|---|---|
| Document | Project mC Master Manual — Part I |
| Controlled filename | `Project_mC_Master_Manual_Part_I_Opening_Governance_History_and_Decision.md` |
| Status | Controlled draft |
| Scope | Chapters 00, 01, 02, 03 and 09, followed by consolidated open-decision, contradiction and source-ledger sections |
| Source boundary | The validated Stage 10D reconciliation and the original organized-workspace sources reproduced in the four attached chapter packets |
| Input inventory | Exactly ten physical attachments were present and readable; the nine hash-controlled attachments matched the manifest; the self-referential manifest was used only for file control |
| Approval status | This document is not a teacher-approval record and does not prove final concept authorization |
| Patent status | No conclusion of patent grant, novelty, inventive step, patent eligibility, infringement clearance or freedom to operate |
| External verification | Not performed in this drafting stage; current specifications, prices, course-board rules, patent status and experimental performance remain reserved for later verification |

The drafting package was complete. The governing instruction, authority protocol, blueprint, Stage 10D reconciliation, four chapter source packets, required output template and manifest were all readable. The transport suffixes attached to several uploaded filenames did not create duplicate logical sources because their sizes and SHA-256 hashes matched the controlled filenames in the manifest. No prior-chat context or web research was used.

## How to read Part I

Part I separates five kinds of information that must not be blended.

**Current project authority** means the teacher requirements and explicit approvals, Decision Register v1.2, frozen Phase 3C architectures, final memories and SOPs, and the controlled comparative evidence. When these conflict with older records, the higher-authority source controls.

**Historical project development** explains how Project mC moved from broad opportunity research to a narrowed portfolio. Historical rankings and earlier concept descriptions remain useful for traceability, but they do not override current architecture or approval status.

**Recommendations and approvals** are different. A research report, adjudication, change request or team preference may recommend an action. Only an explicit controlling record can prove that the teacher or project authority approved it.

**Semester MVPs and future research** are also different. The frozen MVP defines what may be built for the semester. D11, VPD-C7, PIRG, replacement/remount transfer and similar mechanisms are later hypotheses. They must not be presented as completed features or demonstrated inventions.

**Evidence sources and votes** are not the same. Independent research lanes and syntheses can improve coverage and expose recurring findings, but they are not votes. Concept-swapped, materially mis-scoped or inseparable unsupported sections are excluded rather than averaged into a conclusion.

# Chapter 00 — Executive Overview and Decision Snapshot

## 00.1 What Project mC is

Project mC is a controlled embedded-systems innovation pipeline created to identify and execute one strong semester microcontroller project while preserving credible longer-term research options. It combines problem discovery, opportunity analysis, portfolio gates, concept synthesis, historical patent-landscape work, engineering-landscape study, feasibility analysis, architecture selection and comparative decision support.

The project is patent-oriented, but it is not a promise that the semester MVP is novel or patentable. The immediate obligation is a technically honest, affordable and measurable student build. Any later patent-development path requires physical evidence, current prior-art verification and institutional IPR review.

## 00.2 Current portfolio

| Concept | Frozen semester identity | Current status |
|---|---|---|
| OpenBraille | Non-standard macro six-dot cell using six servos, eccentric cams/followers, guided pins, ESP32 direct PWM and external servo power | Retained Phase 3C concept; valid accessibility/mechatronics path; proposed to be replaced as the semester implementation, but not rejected |
| VibeGuard | One rigid ADXL345-class sensor plus ESP32 Level-1 local vibration monitor using RMS/persistence, triggered FFT, RGB and USB on a controlled rig | Retained Phase 3C concept; strongest semester-build recommendation; proposed replacement build |
| TrueMoist | One-soil local compensation experiment using analog moisture sensing, temperature, controlled salinity-treatment coding, fixed regression and gravimetric validation | Retained Phase 3C concept; rigorous measurement/publication path |
| TrustLatch | No completed retained Phase 3C architecture | Deferred, not technically rejected |
| ColdTrace | No completed retained Phase 3C architecture | Deferred, not technically rejected |

The three retained architectures must remain separate. Broad early concept names, raw research candidates and rejected concept swaps do not override the frozen identities.

## 00.3 Current decision state

> **PROJECT mC CURRENT-STATE BOX**
>
> **Completed work**
>
> - Opportunity discovery, analysis, portfolio optimization and corrected 16-concept synthesis.
> - Historical Top Five selection.
> - Historical patent-landscape, engineering-landscape and feasibility work.
> - Engineering Design Review for the five concepts.
> - Phase 3C architecture work for OpenBraille, VibeGuard and TrueMoist.
> - Retained-portfolio closure deferring TrustLatch and ColdTrace.
> - Common comparative evidence, uncertainty register and two final adjudications.
> - Formal OpenBraille-to-VibeGuard change request.
>
> **Recommended action**
>
> - Both final adjudications support VibeGuard as the strongest semester-build candidate.
>
> **Formally requested action**
>
> - Replace the OpenBraille semester implementation with the frozen VibeGuard Level-1 architecture while preserving OpenBraille as documented accessibility/mechatronics work.
>
> **Unapproved or unresolved**
>
> - No explicit teacher approval is attached.
> - No final board/course acceptance is attached.
> - The adjudications disagree on the first pre-selection gate and later patent-development candidate.
> - Phase 4, procurement freeze, named role assignment and final concept authorization are not proved complete.
> - No frozen MVP is established as patentable.

## 00.4 Semester-build recommendation

VibeGuard has the strongest semester-build case because its physical architecture is comparatively simple, its firmware and signal-processing work fit the team, its subsystems can be isolated, its demonstration is clear, and its validation can be organized through controlled sessions and USB logs.

OpenBraille remains valuable but carries coupled mechanical, power, reset and tactile risks. TrueMoist remains rigorous but carries facility, throughput and physical-repeatability burdens.

The recommendation must be described precisely: **VibeGuard is supported as the strongest semester-build candidate. It has not been proved teacher-approved in the attached record.**

## 00.5 Patent-development boundary

The ordinary frozen MVPs are not established inventions.

- OpenBraille D11 and VPD-C7 are later physical-state/datum hypotheses.
- VibeGuard PIRG and dense-machine attribution are later hypotheses.
- TrueMoist replacement/remount transfer and validity-state mechanisms are later hypotheses.

The two final adjudications disagree on the preferred later patent-development route. Work Max favors TrueMoist after a VibeGuard signal-and-access gate. Deep Research High favors conditional OpenBraille D11 after a physical-state observability gate, with VibeGuard as fallback. Neither adjudication proves novelty, inventive step, patent eligibility or FTO.

## 00.6 Major open decisions

1. Will the teacher approve, conditionally approve or reject the proposed VibeGuard shift?
2. Is the frozen ESP32 platform accepted for the course, or is an authorized STM32 substitution required?
3. Which adjudication gate, if any, will govern final patent-first selection?
4. What quantitative success and kill criteria will be pre-registered for the authorized build?
5. When may procurement and Phase 4 begin?
6. Who owns each critical subsystem, and who is the backup owner?
7. Which later mechanism, if any, survives physical experiments and current primary-source patent review?
8. What institutional rules govern confidentiality, ownership, inventorship and disclosure?

## 00.7 Guide to the rest of the manual

Chapter 01 establishes mandate, constraints, team structure, authority and approval status. Chapter 02 explains the staged methodology and its historical corrections. Chapter 03 traces the portfolio from opportunity clusters to frozen architectures. Chapter 09 records the comparative evidence, adjudication disagreement, team objections and proposed concept shift.

Parts II–VI and Appendices A1–A4 of this assembled Master Manual cover the detailed frozen architectures, patent-evidence paths, teacher-review records, semester execution framework, provenance controls, superseded routes and controlled appendices.

# Chapter 01 — Project Mandate, Requirements and Governance

## 01.1 Project mandate

Project mC is a patent-oriented embedded-systems innovation and project-selection pipeline. Its immediate academic responsibility is narrower than its long-term ambition: the team must select, authorize and execute one semester-scale microcontroller project that is affordable, buildable, measurable and demonstrable. The larger pipeline preserves the possibility of later research, publication, patent-development and commercialization work, but none of those outcomes is guaranteed by completing the semester MVP.

This distinction governs the whole manual. The semester project must first succeed as an honest engineering prototype. A useful semester result may be conventional in patent terms. Conversely, a promising future patent hypothesis may be unsuitable as the immediate class build if it depends on inaccessible facilities, unresolved mechanics, unavailable labels or unverified prior-art assumptions.

The controlled portfolio at the end of Phase 3C consists of **OpenBraille, VibeGuard and TrueMoist**. **TrustLatch and ColdTrace are deferred, not technically rejected.** Their records remain preserved and they may re-enter only under the conditions recorded in Decision Register v1.2: decisive failure of the retained concepts, a material change in stakeholder requirements, or significant new evidence that improves their implementation and patent-development case.

Phase 3C is complete for the retained three-concept shortlist. It is not complete for all five historical Top Five concepts. Phase 4, procurement freeze and final implementation authorization must not be described as complete unless a later explicit controlling source records them.

**Source basis:** `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Original_Repository_README.md` (**TIER_1**); `01_GOVERNANCE_AND_CONTROL/03_Project_Context_and_Phase_Map/MC_Project_PHASE_DOC.md` (**TIER_1**, methodology only where its progress block is stale); `01_GOVERNANCE_AND_CONTROL/02_Decision_Registers/Project_mC_Decision_Register_v1.2.md` (**TIER_1**, especially PDR-064 to PDR-067).

## 01.2 Teacher and course constraints

The following constraints control semester planning. Historical estimates may assist planning, but final purchasing and board acceptance require later verification and approval.

| Constraint | Controlled interpretation |
|---|---|
| Academic context | B.Tech CSE Cyber Security microcontroller semester project |
| Team | Five members |
| Time | Teacher context permits up to three months; approximately two months remains the internal feasibility baseline unless an approved schedule uses the full period |
| Preferred budget | At or below ₹3,000 |
| Absolute hardware ceiling | ₹5,000 |
| Platform | Arduino-board or Arduino-IDE-compatible embedded implementation |
| Cybersecurity | Preferred, but not recorded as a mandatory final-selection criterion |
| Power | Low-power components; very high-power components are not permitted |
| Interface and evidence | USB sample, interface or logging capability should be included |
| STM32 | Mentioned in the teacher context; final board choice must follow authoritative project records and explicit teacher/course acceptance |
| Demonstration | A strong live demonstration is required |

The two-month/three-month wording is not treated as a fatal contradiction. The three-month teacher context is the permitted outer boundary. The two-month Decision Register baseline is the stricter internal planning assumption used to reduce schedule risk. A final calendar remains open because no teacher-approved execution schedule is attached.

The teacher context also defines the proposed concept change carefully. The team wishes to request approval to move the semester implementation from OpenBraille to VibeGuard. That request must not be justified by claiming guaranteed patent grant. The ordinary frozen VibeGuard MVP is treated as conventional; any later VibeGuard invention-development route is separate, confidential and evidence-gated.

**Source basis:** `01_GOVERNANCE_AND_CONTROL/01_Project_Requirements/Teacher_Project_Requirements_and_Change_Context.md` (**TIER_1**); PDR-001, PDR-002, PDR-038 and PDR-065 in `01_GOVERNANCE_AND_CONTROL/02_Decision_Registers/Project_mC_Decision_Register_v1.2.md` (**TIER_1**).

## 01.3 Team structure

The controlled roster is five members, not six. The teacher context describes:

- three technically strong members;
- one learner who can perform bounded implementation, testing, logging and inventory work; and
- one member strongest in presentation, documentation and project support.

This structure is a planning constraint, not a judgement of individual value. A viable semester architecture must divide into work packages that permit meaningful contribution without leaving a critical subsystem known by only one person.

The change request proposes five functional roles after approval:

| Proposed role | Main responsibility |
|---|---|
| Technical integration lead | Architecture control, interfaces, safety, schedule and final integration |
| Firmware/data lead | Acquisition, feature pipeline, USB logs, analysis and held-out protocol |
| Hardware/rig lead | Procurement, wiring, mechanical base or rig, mounting, guarding and power |
| Learner/test assistant | Inventory, scripted sessions, labels, photographs and repeatable test records |
| Documentation/communication lead | Teacher communication, reports, source log, demonstration script and slide updates |

This role map is proposed rather than signed. Named ownership, backup ownership and cross-training should be frozen only after the semester concept and platform are authorized.

**Source basis:** `01_GOVERNANCE_AND_CONTROL/01_Project_Requirements/Teacher_Project_Requirements_and_Change_Context.md` (**TIER_1**); PDR-038 in Decision Register v1.2 (**TIER_1**); `04_COMPARATIVE_DECISION/03_Change_Request/Project_mC_Request_to_Change_from_OpenBraille_to_VibeGuard.docx` (**TIER_2**, proposed role structure only).

## 01.4 Authority hierarchy

Whenever sources disagree, Part I uses this order:

1. current teacher requirements and formally recorded approvals;
2. Project mC Decision Register v1.2;
3. authoritative final Phase 3C architecture reports;
4. final concept memories and SOPs;
5. current comparative evidence, gates and uncertainty registers;
6. valid patent-evidence syntheses and final adjudications;
7. controlled independent research lanes;
8. historical phase records and concept dossiers;
9. launchers, manifests, transport packages and archived material.

A lower-authority source cannot silently override a higher one. Sources of equal or comparable decision-support status may legitimately disagree. When no higher authority resolves that disagreement, the manual preserves it as an open decision instead of manufacturing a consensus.

Some older repository instructions placed the Engineering Design Review before the Decision Register. For this manual, the attached authority protocol controls. The EDR remains the principal source for a concept’s identity, mission, engineering hypothesis, fixed principles and minimum demonstrable success, but later teacher constraints and accepted Decision Register entries control conflicting current decisions.

**Source basis:** `01_GOVERNANCE_AND_CONTROL/AUTHORITY_MAP.md` (**TIER_1**); `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/AGENTS.md` (**TIER_1**, older repository order); `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/02_Authoritative_Source_Manifest.md` (**TIER_2**, EDR identity boundary).

## 01.5 Decision Register v1.2 controls

`01_GOVERNANCE_AND_CONTROL/02_Decision_Registers/Project_mC_Decision_Register_v1.2.md` is canonical. Version 1.0 is retained only to show decision history and must not be used operationally.

The opening chapters depend particularly on the following controls:

| Decision control | Effect on Part I |
|---|---|
| PDR-001 | Preferred budget ≤₹3,000; absolute maximum ₹5,000 |
| PDR-002 | Internal planning baseline of approximately two months for the five-member team |
| PDR-004 | Concept-swapped or materially mis-scoped AI sections are excluded rather than averaged |
| PDR-006 | Research must restate and confirm the concept against its authoritative definition |
| PDR-039 and PDR-041 | Multiple independent research systems are used for coverage; duplicate findings may be preserved before consolidation, but models do not become votes |
| PDR-043 | Phase 3C selects one architecture for each completed concept rather than preserving unresolved architecture forks |
| PDR-064 | Final comparative down-selection is limited to OpenBraille, VibeGuard and TrueMoist |
| PDR-065 | Credible patent-development potential is the primary strategic priority, while feasibility, budget, timeline, demonstrability and team fit remain mandatory |
| PDR-066 | TrustLatch and ColdTrace have controlled re-entry conditions |
| PDR-067 | Phase 3C is complete only for the retained three |
| PDR-038 | The team roster is five members |

The Decision Register also locks the three current architectures at opening-chapter level:

**OpenBraille:** one permanent macro-scale six-dot cell; six SG90-class servos; six eccentric cams/followers and guided vertical pins; ESP32 direct PWM; FDM manufacture; external regulated 5 V servo supply; single-dot-first validation. Passive torsion-spring return is unproven, so active servo-driven cam retraction is the controlling fallback unless physical inspection proves otherwise.

**VibeGuard:** one ADXL345-class accelerometer connected to an ESP32 over SPI; rigid mounting; local time-domain features; calibrated RMS baseline with persistence; triggered FFT for explanation and comparison; optional ordinary Mahalanobis comparison; RGB output; USB logging; controlled motor/fan rig. Noise isolation and dense-machine attribution remain validation or later-research tasks, not demonstrated semester capabilities.

**TrueMoist:** one-soil local compensation experiment using a genuine analog capacitive probe, measured temperature, controlled salinity-treatment coding, ESP32, an ADS1115-versus-ESP32-ADC gate, fixed offline-trained regression coefficients, 72 independent physical runs and dry-basis gravimetric reference. It is not a live-EC meter, universal multi-soil controller or irrigation system.

No Decision Register entry records final teacher approval of VibeGuard over OpenBraille. The register closes the retained portfolio and controls evaluation; it does not complete the later authorization step.

**Source basis:** `01_GOVERNANCE_AND_CONTROL/02_Decision_Registers/Project_mC_Decision_Register_v1.2.md` (**TIER_1**); `01_GOVERNANCE_AND_CONTROL/02_Decision_Registers/HISTORICAL_Project_mC_Decision_Register_v1.0.md` (**TIER_1**, historical/superseded only).

## 01.6 Repository and evidence-control rules

The repository is part of the project’s engineering control system. Reorganization must not change technical meaning.

The principal rules are:

- do not rewrite technical conclusions during file cleanup;
- do not merge same-looking filenames without comparing content and authority;
- do not delete failed research merely because it is inconvenient;
- do not renumber accepted PDR entries casually;
- do not allow convenience copies, ZIP members, launchers or transport packages to override canonical files;
- preserve failed and concept-swapped outputs for methodology traceability, while excluding them from substantive synthesis;
- distinguish proof of identity or hash from proof of technical truth;
- preserve original organized-workspace paths in source notes.

Convenience collections such as `COPY PASTE FOLDER/`, `every sop and memory/`, `contexts.zip` and phase ZIPs may contain byte-identical copies. Such copies have no independent authority. A filename’s location alone does not prove final selection, technical validity or approval.

Repository snapshots, manifests, naming logs and launchers can establish provenance, identity, hash, movement or intended use. They do not independently establish architecture feasibility, patentability, experimental success or teacher approval.

**Source basis:** `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/AGENTS.md` (**TIER_1**); `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Original_Repository_README.md` (**TIER_1**); `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Legacy_Repository_Audit/04_AUTHORITY_AMBIGUITIES.md` (**TIER_1**).

## 01.7 Model-output and research-lane rules

Project mC used multiple AI research systems, but the governing method rejects model-majority decision-making.

Independent recurrence can improve confidence only after three checks:

1. the reports analyzed the same authoritative concept;
2. their claims are supported by credible evidence; and
3. the repeated conclusion survives contradiction and minority-risk review.

A fluent report can still be concept-swapped. The project therefore requires explicit concept restatement and confirmation. If a section analyzes a different invention—such as a moving-roller Braille mechanism, software-security VibeGuard, live-EC TrueMoist or another substituted concept—it must be excluded rather than blended with valid evidence.

A technically justified minority concern must not be averaged away merely because more reports omitted it. Missing conclusions must not be reconstructed from partial fragments. Adjudications and syntheses are evidence sources and decision-support outputs; they are not approvals and do not become authority through repetition.

**Source basis:** PDR-004, PDR-005, PDR-006, PDR-039 and PDR-041 in Decision Register v1.2 (**TIER_1**); `04_COMPARATIVE_DECISION/COMPARATIVE_DECISION_INDEX.md` (**TIER_2**).

## 01.8 Current governance state

> **CURRENT GOVERNANCE STATE**
>
> **Completed:** the retained portfolio has been narrowed to OpenBraille, VibeGuard and TrueMoist; one Phase 3C architecture has been frozen for each; common comparative evidence and two final adjudications exist; a formal change request has been prepared.
>
> **Recommended:** VibeGuard is supported by both final adjudications as the strongest semester-build candidate.
>
> **Formally requested:** the team requested permission to replace the OpenBraille semester implementation with the frozen VibeGuard Level-1 architecture while preserving OpenBraille as documented accessibility/mechatronics work.
>
> **Not proved approved:** the attachments contain no completed teacher-decision field, signature, date or separate controlling approval record.
>
> **Still open:** final concept authorization, board/course acceptance, selection-gate choice, Phase 4 entry, procurement freeze, named role assignment and future patent-development route.

The formal request is dated 03 August 2026 and asks the project coordinator to approve the switch. Its teacher-decision area still lists “Approved / Approved with conditions / Not approved” with blank conditions, signature and date. Therefore, the manual must call it a request, not a decision.

## 01.9 Open approvals and actions

| Item | Current status | Required action |
|---|---|---|
| OpenBraille-to-VibeGuard change | Formally requested; no explicit approval attached | Obtain and preserve the teacher’s written decision, conditions, signature/date or equivalent controlling record |
| Final MCU/platform acceptance | Frozen retained architectures use ESP32; STM32 was mentioned | Obtain explicit confirmation that the selected board satisfies the course requirement, or authorize a controlled substitution |
| Project-wide final concept authorization | Not conclusively recorded | Resolve the gate-choice disagreement and record one authorized selection |
| Phase 4 entry | Not started in controlling repository status | Begin only after selection, platform and entry gates are authorized |
| Procurement freeze | Not established | Refresh prices/specifications, confirm approval, then freeze a procurement-ready BOM |
| Named role map | Proposed, not signed | Assign primary and backup owners after approval |
| Experiment thresholds | Several remain unfrozen | Pre-register concept-specific quantitative success and kill criteria |
| Patent-development disclosure | Hypothetical and evidence-gated | Complete experiments, current prior-art verification and institutional ownership/inventorship review before public disclosure or filing decision |

## 01.10 Chapter conclusion

Project mC has a controlled governance system, but its final semester authorization is not complete. The retained portfolio, authority order, architecture identities, budget limits and evidence rules are clear. VibeGuard has the strongest semester-build recommendation, yet the shift from OpenBraille remains unapproved in the attached record. The next valid step is not to rewrite history or assume approval; it is to obtain the controlling decision, confirm the platform, choose or replace the unresolved gate rule, and record authorization before procurement and Phase 4.

## 01.S Source notes

**TIER_1 — controlling governance and current-state sources**

- `01_GOVERNANCE_AND_CONTROL/01_Project_Requirements/Teacher_Project_Requirements_and_Change_Context.md`
- `01_GOVERNANCE_AND_CONTROL/02_Decision_Registers/Project_mC_Decision_Register_v1.2.md`
- `01_GOVERNANCE_AND_CONTROL/03_Project_Context_and_Phase_Map/MC_Project_PHASE_DOC.md` — methodology; current progress block is superseded where it conflicts with PDR-067
- `01_GOVERNANCE_AND_CONTROL/03_Project_Context_and_Phase_Map/PROJECT_CONCEPT_CONTEXT.md` — original concept context only
- `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/AGENTS.md`
- `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Legacy_Repository_Audit/04_AUTHORITY_AMBIGUITIES.md`
- `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Original_Repository_README.md`
- `01_GOVERNANCE_AND_CONTROL/AUTHORITY_MAP.md`

**Historical/superseded comparison only**

- `01_GOVERNANCE_AND_CONTROL/02_Decision_Registers/HISTORICAL_Project_mC_Decision_Register_v1.0.md`

**TIER_2 — request and comparative context, not approval**

- `04_COMPARATIVE_DECISION/03_Change_Request/Project_mC_Request_to_Change_from_OpenBraille_to_VibeGuard.docx`
- `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/02_Authoritative_Source_Manifest.md`
- `04_COMPARATIVE_DECISION/COMPARATIVE_DECISION_INDEX.md`

# Chapter 02 — Research Methodology and Phase History

## 02.1 Methodological purpose

Project mC used a staged funnel designed to prevent a common project-development failure: selecting an attractive solution before proving that the underlying problem, engineering need and execution conditions justify it.

The pipeline separates discovery, analysis, concept creation, patent-landscape history, engineering-landscape study, feasibility assessment and architecture selection. Each phase has a different question:

| Stage | Core question |
|---|---|
| Phase 1A | Which real problems and research gaps are worth investigating? |
| Phase 1B | Which discovered opportunities are distinct, credible and strong enough to rank? |
| Phase 1B.5 | Which opportunities survive practical engineering gates? |
| Phase 1C | What single high-level concept best represents each valid survivor, and which concepts should advance? |
| Phase 2 | What did the historical patent landscape suggest, and where did concept-fidelity failures occur? |
| Phase 3A | What is the engineering state of the art and what problems remain open? |
| Engineering Design Review | What is each concept’s stable identity, hypothesis and minimum demonstrable success? |
| Phase 3B | Can this team demonstrate the hypothesis within budget, time and available capability? |
| Phase 3C | Which one architecture should be frozen for each retained concept, and which concepts should enter final comparison? |

The stages are related but not interchangeable. Phase 1C names do not define current architecture. Phase 2 patent impressions do not establish current patent status. Phase 3B candidate technologies do not override Phase 3C. “Ready” language in a historical report does not prove physical validation, teacher approval or Phase 4 authorization.

**Source basis:** `02_PHASE_HISTORY/HISTORICAL_RESEARCH_INDEX.md` and `02_PHASE_HISTORY/PHASE_HISTORY_INDEX.md` (**TIER_4**, historical boundary); `01_GOVERNANCE_AND_CONTROL/03_Project_Context_and_Phase_Map/MC_Project_PHASE_DOC.md` (**TIER_1**, methodology); Decision Register v1.2 (**TIER_1**, current phase controls).

## 02.2 Phase 1A — Opportunity discovery

Phase 1A intentionally did **not** invent products. Multiple independent research systems explored real-world engineering problems, academic gaps, industrial pain points and domains where embedded hardware could provide an advantage that software alone could not.

The explored domains included healthcare, agriculture, industrial automation, cybersecurity, accessibility, environmental monitoring, smart infrastructure, energy, manufacturing, transportation, logistics, IoT and edge AI. The desired outputs were opportunity statements, evidence of unresolved limitations and research gaps.

Three principles guided the phase:

- problems before solutions;
- evidence before assumptions; and
- novelty before complexity.

The phase produced broad opportunity material and recurring problem spaces. It did not produce final concepts, circuits, architectures, component choices or claims of patentability.

Historical narrative sometimes states that overlapping findings increased confidence. Under the current protocol, recurrence may justify closer attention only after concept fidelity and source quality are audited. It never creates model votes.

**Source basis:** `02_PHASE_HISTORY/Phase_1/Phase_1A_Opportunity_Discovery/Phase1A_Memory.md` (**TIER_4**).

## 02.3 Phase 1B — Opportunity analysis

Phase 1B transformed the broad discovery set into a structured decision framework without generating new ideas or designing solutions.

Its sequence was:

1. extract every distinct opportunity from the research reports;
2. preserve duplicates before consolidation so independent recurrence remained visible;
3. merge true duplicates;
4. group related opportunities into engineering clusters;
5. assign cluster IDs;
6. create structured records;
7. evaluate the clusters with a weighted framework; and
8. produce a ranked opportunity portfolio.

The criteria included novelty, patent potential, market demand, embedded-systems advantage, AI integration, cybersecurity relevance, prototype feasibility, budget feasibility, semester feasibility, research gap and startup potential. Each score required an engineering justification.

The historical output was a **32-cluster dataset** with a ranked **Top 20**, plus parked or eliminated lower-ranked opportunities. The stage also produced an opportunity database, cluster database, evaluation matrix, patent-opportunity matrix and rejected-opportunity appendix.

The method deliberately penalized weak embedded justification, excessive cost and schedules unsuitable for approximately two months. It favored real problems, irreplaceable hardware value and identifiable research gaps over feature count.

**Source basis:** `02_PHASE_HISTORY/Phase_1/Phase_1B_Opportunity_Analysis/Phase1B_Memory.md` (**TIER_4**); PDR-041 in Decision Register v1.2 (**TIER_1**, preservation of duplicate findings before consolidation).

## 02.4 Phase 1B.5 — Portfolio optimization

Phase 1B.5 was an engineering decision gate, not a concept-generation stage. It evaluated the validated opportunity portfolio through eight gates:

1. semester feasibility;
2. budget feasibility;
3. embedded-systems necessity;
4. patent/research white space;
5. demonstration impact;
6. team capability;
7. learning return; and
8. innovation density.

The review treated practical execution as important as theoretical novelty. Patent opportunity alone was insufficient if the team could not demonstrate the project within the semester. Scope restriction was allowed when it increased the chance of a convincing prototype without destroying the underlying opportunity.

The original Phase 1B.5 survivor record reported 22 entries. A later consistency audit found that six of those entries had come from outside the Phase 1B Top 20 and had improperly re-entered, while four Top-20 clusters had been legitimately removed by the hard gates. The valid Phase 1C input was therefore **16 clusters**, confirmed two ways:

- `20 - 4 = 16`; and
- `22 - 6 = 16`.

The historical 22-survivor record remains preserved, but it must be labelled as the uncorrected intermediate result. It is not the valid input count for Phase 1C.

**Source basis:** `02_PHASE_HISTORY/Phase_1/Phase_1B5_Portfolio_Optimization/Phase1B5_Memory.md` (**TIER_4**); `02_PHASE_HISTORY/Phase_1/Phase_1C_Concept_Synthesis/Phase1C_Concept_Synthesis.pdf` (**TIER_4**, correction).

## 02.5 Phase 1C — Concept synthesis

Phase 1C was the first stage allowed to create solutions. It generated exactly one high-level engineering concept for each of the 16 valid survivor clusters.

Each concept record included the originating cluster, project title, problem statement, limitations of existing solutions, why embedded systems were essential, high-level innovation, target users, expected prototype scope, estimated cost, patent-opportunity summary, technical risks, demonstration value and commercial potential.

The concepts were compared using originality, patent potential, semester feasibility, budget feasibility, demonstration impact, embedded necessity, team capability and commercial potential. The output was a ranked concept portfolio and a historical Top Five for faculty presentation and later investigation.

Phase 1C explicitly excluded patent searches, prior-art analysis, circuit design, component selection, PCB design, software architecture, firmware architecture, bills of materials and detailed implementation planning. Therefore, its broad titles and claims must not be read as frozen technical definitions.

A historical transition sentence stated that no implementation would begin before patent validation. That wording controlled the next step at that time; it is not a permanent prohibition on building a conventional semester MVP. Current governance permits a semester build without representing it as patentable.

**Source basis:** `02_PHASE_HISTORY/Phase_1/Phase_1C_Concept_Synthesis/Phase1C.md`, `02_PHASE_HISTORY/Phase_1/Phase_1C_Concept_Synthesis/Phase1C_Memory.md` and `02_PHASE_HISTORY/Phase_1/Phase_1C_Concept_Synthesis/Phase1C_Concept_Synthesis.pdf` (**TIER_4**).

## 02.6 Phase 2 — Historical patent landscape

Phase 2 commissioned four research passes for the five Phase 1C concepts, but only three contained usable patent-landscape findings. One file was a task specification rather than an independent research result.

The most important methodological event was a concept-fidelity failure. One report interpreted:

- OpenBraille as a Braille embossing printer rather than a refreshable tactile display;
- VibeGuard as a phone anti-theft alarm rather than an industrial vibration monitor; and
- TrustLatch as a physical smart door lock rather than a secure-boot/signed-update toolkit.

Those three sections were excluded. The correctly scoped TrueMoist and ColdTrace portions were retained with reduced weight. This established the exclusion-over-averaging rule and motivated mandatory concept restatement in later research.

Phase 2 produced historically useful warnings and candidate directions, but its rankings were later overtaken by engineering and architecture evidence. It cannot establish current novelty, claim scope, legal status or freedom to operate.

Examples of historical concerns included:

- OpenBraille’s actuation/manufacturing prior-art density;
- VibeGuard’s single-node attribution uncertainty;
- TrueMoist’s demanding validation burden;
- TrustLatch’s split between strong product value and weak patent white space; and
- ColdTrace’s thermal-model and FTO concerns.

These findings explain why later work was structured as it was. They are not current patent opinions.

**Source basis:** `02_PHASE_HISTORY/Phase_2_Patent_Landscape/Phase2_Memory.md` (**TIER_4**); PDR-004 and PDR-006 in Decision Register v1.2 (**TIER_1**).

## 02.7 Phase 3A — Engineering landscape

Phase 3A shifted the question from patents to engineering. It mapped mature parent domains, dominant approaches, technology ecosystems, hardware and software categories, standards, reliability concerns and unresolved engineering problems.

The phase intentionally stopped before implementation planning. It did not select components, communication protocols, circuits, bills of materials or final architectures.

A four-stage method was used:

1. multiple independent engineering-landscape research lanes;
2. concept-grounding documents and mandatory validation;
3. synthesis-board audit for fidelity, hallucination, conflict and unsupported claims; and
4. one consolidated engineering-landscape report.

The phase found that all five concepts belonged to mature engineering domains and did not require new scientific principles. Their innovation opportunities were narrower subproblems:

- OpenBraille: low-cost reliable tactile actuation;
- VibeGuard: local interpretation of machine vibration;
- TrueMoist: compensation for environmental/sensor effects;
- TrustLatch: accessible secure firmware-deployment practice; and
- ColdTrace: reliable low-cost cold-chain event interpretation.

Phase 3A strengthened the lesson that broad domain maturity does not eliminate opportunity, but it shifts the burden toward a specific, measurable contribution.

**Source basis:** `02_PHASE_HISTORY/Phase_3/Phase_3A_Engineering_Landscape/Phase3A_MEMORY.md` and `02_PHASE_HISTORY/Phase_3/Phase3_SOP.md` (**TIER_4**).

## 02.8 Engineering Design Review

The Engineering Design Review was the stabilizing gate between landscape analysis and feasibility analysis. It required each concept to have:

- a clear engineering problem;
- a measurable engineering hypothesis;
- an appropriate prototype scope;
- fixed design principles;
- defined major risks and open questions; and
- a minimum demonstrable success.

The EDR approved all five concepts to proceed to Phase 3B and explicitly stated that no concept was eliminated at that review. It reduced ambiguity without selecting an implementation.

For later work, the EDR is authoritative for concept identity and purpose. A research lane must analyze the EDR-defined concept, not infer meaning from the project name.

**Source basis:** `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/00_Engineering_Design_Review.md` (**TIER_2**).

## 02.9 Phase 3B — Feasibility analysis

Phase 3B asked whether each engineering hypothesis could realistically be demonstrated by the actual team within the budget and timeline. It compared candidate technologies and minimum viable prototype routes but intentionally did not select final architectures, finalize bills of materials or eliminate concepts.

Its research method repeated the multi-lane, concept-grounded and audited structure. The EDR was supplied as the primary grounding source. Reports were checked for explicit restatement and confirmation, concept drift, unsupported claims and full concept swaps.

The synthesis identified one dominant risk dimension for each concept:

| Concept | Dominant Phase 3B risk |
|---|---|
| OpenBraille | Mechanical fabrication tolerance, alignment and team mechanical fit |
| VibeGuard | Signal interpretation and isolation from noise/interference |
| TrueMoist | Calibration discipline, physical repeatability and validation throughput |
| TrustLatch | Low-level flash/memory correctness and scope control |
| ColdTrace | Physical thermal test conditions and cold-temperature power behavior |

At this stage, VibeGuard, TrueMoist, TrustLatch and ColdTrace showed high or very high prototype feasibility in the historical synthesis, while OpenBraille retained a genuine strategic fork around precision mechanics and macro scaling. All five were still allowed to proceed toward Phase 3C.

Concept-fidelity failures recurred. A research section reframed VibeGuard as active vibration cancellation and another reframed ColdTrace away from cold-chain monitoring. Both were excluded. The phase also reinforced two methodology rules: failure to perform concept restatement is a reliability warning, and a well-argued minority risk cannot be dismissed by counting model labels.

**Source basis:** `02_PHASE_HISTORY/Phase_3/Phase_3B_Feasibility_Analysis/Phase3B_MEMORY.md` and `02_PHASE_HISTORY/Phase_3/Phase_3B_Feasibility_Analysis/Phase3B_Report_by_Claude.md` (**TIER_4**).

## 02.10 Phase 3C — Architecture selection and portfolio closure

Phase 3C moved from candidate comparison to architecture commitment. Under PDR-043, a completed concept could not carry unresolved architecture forks forward indefinitely.

One architecture was frozen for each retained concept:

- OpenBraille: macro six-dot, six-servo, cam/follower/guided-pin architecture;
- VibeGuard: ADXL345-class sensor plus ESP32 Level-1 vibration monitor; and
- TrueMoist: one-soil local compensation experiment using temperature and controlled salinity-treatment coding.

TrustLatch and ColdTrace were deferred before completing concept-specific Phase 3C architecture work. The closure memo explains that the retained three already provided enough decision diversity, while completing two more architecture packages would impose additional research, synthesis, memory, PDR and source-audit costs with diminishing decision value.

The deferral was strategic and reversible. It was not a finding that TrustLatch or ColdTrace was impossible, useless or technically failed.

The immediate next action identified by the closure record was a formal comparative down-selection among the retained three. That comparison was later performed as decision support, but the attached sources still do not prove final teacher authorization or Phase 4 entry.

**Source basis:** `02_PHASE_HISTORY/Phase_3/Phase_3C_Comparative_Evaluation/Original_Phase3C_README.md` and `02_PHASE_HISTORY/Phase_3/Phase_3C_Comparative_Evaluation/Phase3C_Portfolio_Closure_Memo_Approved.md` (**TIER_4**, historical record); PDR-043 and PDR-064 to PDR-067 (**TIER_1**, current control).

## 02.11 Research-lane integrity and exclusions

The mature Project mC research method requires:

- multiple independent lanes for breadth, not voting;
- preservation of recurrence before consolidation;
- concept restatement against authoritative definitions;
- complete exclusion of concept-swapped or inseparably mis-scoped sections;
- explicit separation of facts, inferences, recommendations, simulations and decisions;
- preservation of technically justified minority risks;
- no reconstruction of missing conclusions from fragments;
- source-quality and fidelity review before confidence is assigned; and
- clear subordination of raw research to teacher requirements, the Decision Register, frozen architectures and audited comparative evidence.

The method should not be misunderstood as “more models equal more truth.” It is a controlled error-detection strategy. Independent lanes are valuable because they can expose missing evidence, conflicting assumptions and recurring mechanisms. Their output remains subordinate to authority and physical tests.

## 02.12 Historical limitations

The phase history supports traceability, not unrestricted present-tense claims.

The following limitations apply:

- early rankings do not establish current selection;
- Phase 2 searches do not establish current patent status or FTO;
- Phase 3A and Phase 3B candidates do not override Phase 3C architecture locks;
- historical readiness labels do not prove a physical build;
- dated cost estimates are not procurement-ready;
- old progress blocks may be stale;
- broad early names such as “controller,” “spatially isolated” or “standard Braille” must be reconciled to later scope; and
- historical confidence language cannot convert model agreement into a vote.

The TrueMoist history illustrates the rule. Early records contemplated broader multi-soil or multi-season validation. The frozen semester architecture is one-soil, fixed-model compensation with early gates. Broader transfer remains later research.

The same applies to the Phase 1C sequencing statement that implementation should wait for patent validation. Current project authority allows an honest conventional MVP while preserving patent claims for a later evidence-gated stage.

## 02.13 Chapter conclusion

Project mC’s methodology became progressively stricter as it encountered real research failures. It began with broad opportunity discovery, then added clustering, hard gates, concept synthesis, patent-landscape caution, engineering grounding, feasibility analysis and architecture locks. The process did not eliminate uncertainty; it made uncertainty visible and assigned it to named tests and decisions.

The valid historical sequence is: problems first, then opportunities, concepts, landscapes, feasibility and frozen architectures. The valid current boundary is equally important: historical reports explain the route, while teacher requirements, Decision Register v1.2 and frozen architectures control the present.

## 02.S Source notes

**TIER_4 — historical phase records materially relied upon**

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

**Cross-chapter controlling sources**

- `01_GOVERNANCE_AND_CONTROL/02_Decision_Registers/Project_mC_Decision_Register_v1.2.md` — **TIER_1**
- `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/00_Engineering_Design_Review.md` — **TIER_2**

# Chapter 03 — Portfolio Evolution and Concept Origins

## 03.1 From opportunity clusters to concepts

The Project mC portfolio did not begin as five named products. It began as a broad evidence collection of real-world problems. Phase 1B organized that evidence into an historical 32-cluster dataset and ranked a Top 20. Phase 1B.5 applied feasibility and innovation gates. A later scope audit corrected the survivor set to 16 valid inputs for Phase 1C.

This history matters because it prevents hindsight distortion. The final concepts were not chosen from an unstructured brainstorm, and their current architectures were not present at the beginning. The portfolio passed through three different levels:

1. **opportunity clusters** describing problem spaces;
2. **high-level concepts** expressing possible solutions; and
3. **frozen architectures** defining the current semester scope.

A name at one level must not be used to import features from another.

**Source basis:** Phase 1A, Phase 1B and corrected Phase 1C records under `02_PHASE_HISTORY/Phase_1/` (**TIER_4**).

## 03.2 Corrected Phase 1C portfolio

The 16 valid Phase 1C concepts were:

| No. | Historical concept |
|---:|---|
| 1 | SignalGuard — Offline Vital-Sign Confidence Monitor |
| 2 | FallSense — Privacy-Preserving Ambient Fall & Distress Monitor |
| 3 | AuscultAI — Offline Acoustic Screening Assistant |
| 4 | ColdTrace — Multi-Modal Cold-Chain Integrity Logger |
| 5 | OpenBraille — Low-Cost Refreshable Braille Display Module |
| 6 | VibeGuard — Spatially-Isolated Bearing Fault Early-Warning Node |
| 7 | OTShield — Inline Legacy-Protocol Anomaly Gateway |
| 8 | ToolPulse — Real-Time Tool-Wear Signature Monitor |
| 9 | GasPrint — Multi-Gas Fingerprinting Safety Monitor |
| 10 | PanelWatch — Solar Panel Micro-Crack & Degradation Early-Warning Node |
| 11 | TrueMoist — Drift-Self-Correcting Soil Moisture Controller |
| 12 | CalibNet — Peer-Referenced Self-Calibrating Air Quality Node |
| 13 | FloodPulse — Debris-Resistant Flood Water-Level Early-Warning Node |
| 14 | TrustLatch — Accessible Secure-Boot & Signed-OTA Toolkit |
| 15 | SiliconFingerprint — SRAM-Based Physical Unclonable Function |
| 16 | SpanSense — Edge-Computed Fatigue-Tracking Bridge Monitor |

These are historical concept labels. They do not define current hardware or claim scope. In particular, “spatially isolated,” “controller” and “refreshable display” were broad ambitions that were later narrowed.

**Source basis:** `02_PHASE_HISTORY/Phase_1/Phase_1C_Concept_Synthesis/Phase1C_Concept_Synthesis.pdf` (**TIER_4**).

## 03.3 Historical Top Five

Phase 1C recommended:

1. OpenBraille;
2. VibeGuard;
3. TrueMoist;
4. TrustLatch; and
5. ColdTrace.

That order was an early recommendation for faculty presentation and subsequent patent analysis. It is not the current final project decision.

The portfolio later narrowed to three retained Phase 3C concepts. OpenBraille, VibeGuard and TrueMoist completed concept-specific architecture work. TrustLatch and ColdTrace were deferred because the completed trio already represented sufficient decision diversity, and the additional research burden was judged to offer diminishing decision value.

The current status is therefore:

| Concept | Current portfolio status |
|---|---|
| OpenBraille | Retained; frozen Phase 3C architecture; active comparative record |
| VibeGuard | Retained; frozen Phase 3C architecture; strongest semester-build recommendation |
| TrueMoist | Retained; frozen Phase 3C architecture; active comparative record |
| TrustLatch | Deferred; no completed retained Phase 3C architecture |
| ColdTrace | Deferred; no completed retained Phase 3C architecture |

**Source basis:** `02_PHASE_HISTORY/Phase_1/Phase_1C_Concept_Synthesis/Phase1C_Concept_Synthesis.pdf` (**TIER_4**); PDR-064 to PDR-067 in `01_GOVERNANCE_AND_CONTROL/02_Decision_Registers/Project_mC_Decision_Register_v1.2.md` (**TIER_1**); `02_PHASE_HISTORY/Phase_3/Phase_3C_Comparative_Evaluation/Phase3C_Portfolio_Closure_Memo_Approved.md` (**TIER_4**, historical closure record).

## 03.4 OpenBraille origin and scope evolution

OpenBraille originated from **OC-08, “Low-Cost Assistive Communication & Mobility Devices.”** Its Phase 1C form proposed a low-cost refreshable Braille display module without selecting the actuator, mechanism, controller or manufacturing path.

The enduring engineering identity was later stabilized by the EDR: demonstrate that a lower-cost actuation strategy can produce refreshable tactile output for at least one cell with acceptable basic tactile and repeatability performance. The prototype was not required to compete with commercial displays.

Phase 3C exploration considered multiple actuation and mechanical arrangements. The current design is no longer an open candidate set. It is frozen as:

- one permanent macro-scale six-dot cell;
- six SG90-class servos;
- six eccentric cams/followers;
- six guided vertical pins;
- ESP32 direct PWM;
- FDM manufacture;
- external regulated servo power; and
- active servo-driven retraction unless a passive return is physically proved.

The macro scale deliberately abandons dimensional compliance. This reduces the semester fabrication burden but restricts what can be claimed. The build may be described as a **non-standard mechanical/tactile proof-of-concept**. It must not be called an ISO-compliant commercial Braille cell or a device ready for fluent reading.

Moving-roller, encoder-wheel, RAMPS/Mega embosser, continuous-paper and electromagnetic alternatives are historical or concept-swapped routes, not current OpenBraille.

The scope evolution is therefore not evidence that the original concept was a hoax or wasted work. It is evidence that the broad accessibility objective was translated into a buildable but claim-limited mechanism experiment.

**Source basis:** Phase 1C synthesis (**TIER_4**); `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/00_Engineering_Design_Review.md` (**TIER_2**); PDR-015 to PDR-022 (**TIER_1**); historical Phase 3C OpenBraille prompts (**TIER_4**, exploration only).

## 03.5 VibeGuard origin and scope evolution

VibeGuard originated from **OC-10, “Vibration-Based Predictive Maintenance for Rotating Machinery.”** The Phase 1C title, “Spatially-Isolated Bearing Fault Early-Warning Node,” carried an ambitious single-node source-discrimination idea.

The EDR retained the core purpose: affordable local interpretation of machine vibration, with minimum success defined as distinguishing normal operation from a deliberately introduced abnormal condition without cloud processing.

Phase 3C narrowed the semester MVP to a Level-1 controlled system:

- one rigidly mounted ADXL345-class tri-axis accelerometer;
- ESP32 over SPI;
- continuous time-domain features;
- RMS plus persistence as the minimum classifier;
- triggered FFT and selected bands for explanation and comparison;
- optional ordinary Mahalanobis score as a comparator;
- local RGB indication;
- USB logging; and
- a guarded low-voltage motor/fan rig with controlled normal and abnormal states.

This scope is strong for a semester demonstration because sensor, firmware, feature extraction, output, logging and rig states can be tested as separable subsystems.

The original “spatially isolated” ambition is not a current demonstrated capability. Dense-machine attribution, ambiguity handling, protected updates and PIRG-style learning remain later research. A software-security scanner or configuration-security project is a rejected concept swap and must not re-enter VibeGuard’s identity.

**Source basis:** Phase 1C synthesis (**TIER_4**); EDR (**TIER_2**); PDR-023 to PDR-030 and PDR-054/PDR-055 (**TIER_1**).

## 03.6 TrueMoist origin and scope evolution

TrueMoist originated from **OC-15, “Precision Irrigation & Drift-Self-Correcting Soil Sensing.”** Its Phase 1C title, “Drift-Self-Correcting Soil Moisture Controller,” suggested a broad sensing-and-control product.

Phase 3C narrowed the semester project to a controlled measurement and compensation experiment:

- one homogeneous soil source;
- a genuine analog capacitive moisture probe;
- DS18B20 temperature measurement;
- salinity treatment defined by controlled salt addition per dry-soil mass;
- ESP32;
- an early evidence gate comparing the internal ADC with ADS1115;
- fixed offline-trained regression coefficients;
- USB CSV logging;
- 72 independent physical runs; and
- dry-basis gravimetric ground truth.

The salinity value is a treatment code, not live soil EC, pore-water EC, apparent EC or solution conductivity. The MVP does not control irrigation. It does not claim universal transfer across soils, custom multi-frequency probe hardware, online adaptive learning or a TinyML showcase.

This narrowing increased experimental clarity. It changed TrueMoist from a broad controller narrative into a falsifiable one-soil compensation study with defined physical reference.

**Source basis:** Phase 1C synthesis (**TIER_4**); PDR-031, PDR-032, PDR-045, PDR-048 to PDR-050 and PDR-058 to PDR-063 (**TIER_1**).

## 03.7 TrustLatch and ColdTrace

TrustLatch and ColdTrace remain part of Project mC’s historical Top Five and retained knowledge base, but they are not active final down-selection candidates.

**TrustLatch** retains value as a secure-boot/firmware-integrity educational concept. Phase 3B found strong team fit but also scope and flash-layout constraints. Its patent landscape was comparatively crowded, and its strongest value may be academic/product execution rather than immediate patent development. No retained Phase 3C architecture was completed.

**ColdTrace** retains value as a cold-chain sensing and event-interpretation concept. Historical evidence identified thermal-model, battery and FTO burdens. No retained Phase 3C architecture was completed.

Neither was technically rejected. Re-entry is controlled by PDR-066. Their records should remain archived and available, but they should not be described as equally active with the retained three.

**Source basis:** `03_CONCEPT_PORTFOLIO/Other_Concepts/README.md` and `03_CONCEPT_PORTFOLIO/Other_Concepts/TrustLatch/HISTORICAL_Phase1C_TrustLatch_Concept_Dossier.docx` (**TIER_4**); PDR-064/PDR-066/PDR-067 (**TIER_1**).

## 03.8 Other retained historical concepts

The eleven non-Top-Five Phase 1C concepts remain useful evidence of portfolio breadth. They represent healthcare, industrial, cybersecurity, environmental and infrastructure opportunities that passed the corrected survivor process but did not reach the historical Top Five.

Their preservation serves three purposes:

- traceability of the opportunity-to-concept funnel;
- evidence that the final portfolio emerged from comparison rather than a single idea; and
- a controlled archive for possible future projects.

Their presence does not authorize active development, grant them equal current status or imply that their historical claims remain technically current.

## 03.9 Early concepts versus frozen architectures

| Concept | Early framing | Frozen current semester identity | Must not be presented as current |
|---|---|---|---|
| OpenBraille | Low-cost refreshable Braille module; actuator open | Non-standard macro six-dot cell with six servos, eccentric cams, guided pins, ESP32 direct PWM and external servo supply | Moving roller/encoder/RAMPS embosser; electromagnetic substitution; standard-size compliance; proven passive reset |
| VibeGuard | Spatially isolated bearing-fault node | ADXL345-class sensor + ESP32 Level-1 local normal/abnormal monitor; RMS/persistence; triggered FFT; controlled rig | Software-security scanner; cloud/RUL platform; sensor array; demonstrated dense-machine attribution; PIRG as built |
| TrueMoist | Drift-self-correcting soil moisture controller | One-soil local compensation experiment with temperature, salinity-treatment code, fixed coefficients and gravimetric validation | Live EC meter; irrigation controller; universal multi-soil system; online learner; custom multi-frequency probe |
| TrustLatch | Secure-boot and signed-OTA toolkit | No completed retained Phase 3C architecture | Treating Phase 1C/3B suggestions as a frozen implementation |
| ColdTrace | Multi-modal cold-chain integrity logger | No completed retained Phase 3C architecture | Treating provisional thermal, RTC or battery choices as a current authorized design |

The final three concepts must remain separate. A hybrid that combines their sensors, mechanisms or future patent paths would be a new concept requiring a new authorized decision.

## 03.10 Architecture identity locks

The following identity statements are mandatory throughout the Master Manual:

> **OpenBraille identity lock:** frozen macro six-dot, six-servo, cam/follower/guided-pin design.

> **VibeGuard identity lock:** frozen ADXL345-class sensor plus ESP32 Level-1 vibration monitor.

> **TrueMoist identity lock:** frozen one-soil local compensation design using measured temperature and controlled salinity-treatment coding.

These locks prevent raw Phase 3C explorations, failed syntheses and broad early names from re-entering current truth. They also preserve the boundary between semester implementation and later research.

For OpenBraille, D11 and VPD-C7 are not part of the frozen MVP. For VibeGuard, PIRG and dense-machine attribution are not part of Level 1. For TrueMoist, replacement/remount transfer and validity-state mechanisms are not part of the 72-run one-soil study.

## 03.11 Chapter conclusion

Project mC evolved from a 32-cluster historical opportunity dataset to a corrected 16-concept Phase 1C portfolio, then a historical Top Five and finally three retained Phase 3C architectures. The portfolio did not collapse because the other ideas were fraudulent or useless. It narrowed because the project imposed stronger evidence, feasibility and decision-value controls.

OpenBraille, VibeGuard and TrueMoist each changed scope as uncertainty became clearer. That narrowing is a strength when it is recorded honestly. The current manual therefore preserves the social and research value of earlier concepts while refusing to let early titles override frozen design.

## 03.S Source notes

**TIER_4 — origins and historical exploration**

- `02_PHASE_HISTORY/Phase_1/Phase_1C_Concept_Synthesis/Phase1C_Concept_Synthesis.pdf`
- `03_CONCEPT_PORTFOLIO/OpenBraille/06_Historical_Phase3C_Research_and_Prompts/Prompts/Phase3C_OpenBraille_Deep_Research_Prompt_Final.md`
- `03_CONCEPT_PORTFOLIO/VibeGuard/06_Historical_Phase3C_Research_and_Prompts/Prompts/Phase3C_VibeGuard_Deep_Research_Prompt_Final.md`
- `03_CONCEPT_PORTFOLIO/TrueMoist/06_Historical_Phase3C_Research_and_Prompts/Prompts/Phase3C_TrueMoist_Deep_Research_Prompt_Final.md`
- `03_CONCEPT_PORTFOLIO/Other_Concepts/README.md`
- `03_CONCEPT_PORTFOLIO/Other_Concepts/TrustLatch/HISTORICAL_Phase1C_TrustLatch_Concept_Dossier.docx`

**Controlling cross-chapter sources**

- `01_GOVERNANCE_AND_CONTROL/02_Decision_Registers/Project_mC_Decision_Register_v1.2.md` — **TIER_1**
- `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/00_Engineering_Design_Review.md` — **TIER_2**

# Chapter 09 — Comparative Decision and Proposed Concept Shift

## 09.1 Purpose of the comparison

The final comparison had two related but different tasks:

1. identify the strongest semester implementation; and
2. decide how, or whether, Project mC should pursue a later patent-development path.

Those tasks can produce different winners. A concept may be the safest build while having a conventional patent position. Another may offer a more specific future mechanism while imposing a greater semester risk. The comparison therefore separates the frozen MVP from later invention-development hypotheses.

The original common evidence package intentionally did not choose a winner. It created a neutral framework, prechecked gates, recorded uncertainties, prepared a scoring worksheet and identified missing evidence. Later adjudications populated conditional decision models, but they remain decision support rather than votes or approval.

**Source basis:** `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/01_Comparison_Protocol.md`, `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/07_Scoring_Worksheet.md` and `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/09_Final_Downselection_README.md` (**TIER_2**).

## 09.2 Comparative method and hard gates

The common framework defined seven hard gates:

| Gate | Meaning |
|---|---|
| G1 | Budget compliance |
| G2 | Timeline compliance |
| G3 | Executability by the actual team |
| G4 | Measurable minimum demonstrable success |
| G5 | Access to parts, fabrication, facilities and validation |
| G6 | Credible patent-development path |
| G7 | No fatal unresolved dependency |

It also defined a 100-point rubric:

| Criterion | Weight |
|---|---:|
| Patent-development potential | 35 |
| Two-month buildability | 20 |
| Validation strength | 15 |
| Team fit | 10 |
| Demonstration | 8 |
| Budget/procurement certainty | 7 |
| Commercial/social significance | 5 |

The precheck eliminated no concept. All three had provisional implementation paths, but all three initially received **G6: Insufficient Evidence** because current patent status, claim scope and FTO were not established.

The high-reasoning audit confirmed that the initial scores were blank, procurement quotes and physical data were incomplete, and current patent-family status was unavailable. It judged the package ready for a later verification/adjudication stage, not ready to claim patentability.

**Source basis:** `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/04_Hard_Gate_Precheck.md`, `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/05_Uncertainty_and_Test_Register.md` and `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/08_High_Reasoning_Audit.md` (**TIER_2**).

## 09.3 Common evidence limitations

The comparison is limited by the absence of controlling physical and external evidence in this drafting package.

Common limitations include:

- no completed semester build;
- no attached locked experimental dataset;
- no final procurement-ready BOM with fresh supplier verification;
- no explicit teacher decision on the proposed shift;
- no categorical attached resolution of ESP32 versus STM32 acceptance;
- no current primary-source patent-status or FTO clearance;
- no institutional IPR decision; and
- no proof that D11, VPD-C7, PIRG or TrueMoist transfer/validity mechanisms work.

This means every recommendation is conditional. The manual may state that evidence favors a concept for a purpose, but it must not convert a ranking into a completed authorization or legal conclusion.

## 09.4 OpenBraille comparative position

### Semester strengths

OpenBraille offers strong social impact and a highly visible physical demonstration. A successful six-dot cell directly connects CAD, fabrication, actuation, power, control and tactile output. The architecture is bounded to one cell and historical cost estimates remained below the ceiling.

### Semester weaknesses

Its risks are coupled. A change in guide tolerance can affect friction, pin travel, cam geometry, servo load, power behavior and tactile reliability. The team must manage precision FDM mechanics, six-channel alignment, active retraction, current peaks, wear and a valid tactile protocol.

The current record does not prove that 5 V/2 A is adequate under staged six-servo operation, nor that passive return works. Those are test requirements, not reasons to silently replace the frozen architecture.

### Patent-development position

The ordinary macro six-servo MVP is not established as an invention. D11 and VPD-C7 are later physical-state verification/datum hypotheses. Their value depends on direct physical ground truth, ablation, robustness across servos and reassembly, safe retry/fault handling and practical-scale evidence.

The two adjudications disagree sharply:

- Work Max deprioritizes OpenBraille for patent-first selection unless later D11-type evidence passes.
- Deep Research High calls OpenBraille D11 the best conditional post-MVP candidate and proposes a ten-day physical-state observability gate.

Neither result proves patentability, and no higher authority chooses between them.

**Source basis:** Decision Register v1.2 (**TIER_1**); uncertainty register and both adjudications (**TIER_2**).

## 09.5 VibeGuard comparative position

### Semester strengths

Both adjudications independently identify VibeGuard as the best semester-build candidate. Its frozen Level-1 architecture has:

- the simplest physical build of the retained three;
- strong alignment with ESP32 programming, acquisition, signal processing and data testing;
- a clear live state-change demonstration;
- separable subsystems;
- low historical cost; and
- a recovery path that does not require repeated precision mechanical rework or a 72-run drying campaign.

The requested implementation uses one rigidly mounted sensor, controlled normal and induced-abnormal states, RMS plus persistence, triggered FFT, RGB indication and USB evidence.

### Semester weaknesses

VibeGuard still requires disciplined engineering. Sensor authenticity, rigid-mount reproducibility, safe fault injection, sampling integrity, dropped-block reporting, threshold freezing and held-out validation are open. A visually impressive RGB change without locked quantitative criteria would not satisfy the intended evidence standard.

### Patent-development position

The ordinary feature stack is treated as conventional. Dense-machine source attribution, ambiguity handling, protected updates and PIRG are later hypotheses. Their decisive evidence depends on target-specific information surviving interference and remounts and on obtaining independently labelable field-like access.

Work Max recommends a VibeGuard Level-2A Signal-and-Access Gate, with TrueMoist as fallback. Deep Research High instead makes VibeGuard the fallback after an OpenBraille gate. The semester-build agreement is strong; the overall patent-first route is not settled.

**Source basis:** Decision Register v1.2 (**TIER_1**); uncertainty register and both final adjudications (**TIER_2**).

## 09.6 TrueMoist comparative position

### Semester strengths

TrueMoist has the most explicit quantitative validation architecture. It uses physical gravimetric ground truth, defined treatment factors, fixed coefficients, controlled one-soil scope and 72 independent runs. It offers strong measurement and publication value.

### Semester weaknesses

Its burden is experimental rather than algorithmic. It depends on oven and scale access, probe repeatability, insertion and packing control, drying throughput, salinity-treatment effect and successful early ADC/probe gates. A 72-run plan is only feasible if the physical workflow is disciplined.

### Patent-development position

The frozen compensation regression is not automatically patentable. Later replacement/remount transfer, physical reference challenges, validity-state logic and contaminated-update blocking are hypotheses requiring multiple probes, lots, remounts and current prior-art review.

Work Max identifies TrueMoist as the best presently evidenced post-MVP patent-development candidate and fallback to VibeGuard. Deep Research High deprioritizes it for the current patent-first choice while preserving it as a rigorous engineering/publication project. No higher authority resolves this disagreement.

**Source basis:** Decision Register v1.2 (**TIER_1**); hard-gate precheck, uncertainty register and final adjudications (**TIER_2**).

## 09.7 Final adjudications and their disagreement

The adjudications are concept-faithful, detailed and later than the neutral precheck, but they use different decision models.

| Decision point | Work Max | Deep Research High | Reconciled status |
|---|---|---|---|
| Best semester build | VibeGuard | VibeGuard | Strong agreement; recommendation, not approval |
| Best later patent-development candidate | TrueMoist | OpenBraille D11, conditionally | Unresolved |
| Immediate gate | VibeGuard Level-2A Signal-and-Access Gate | OpenBraille D11 Physical-State Observability Gate | Unresolved |
| Fallback | TrueMoist if VibeGuard gate fails | VibeGuard if OpenBraille gate fails | Unresolved |
| Patent-first deprioritized concept | OpenBraille | TrueMoist | Unresolved |

The Work Max gate asks whether a one-sensor VibeGuard system can preserve target-attribution improvement under controlled interference, held-out sessions/remounts and local ESP32 execution, while also securing field-like access. The Deep Research High gate asks whether a one-dot OpenBraille module can verify actual physical pin state, avoid silent wrong states and outperform fixed common-PWM control using physical ground truth.

The gates answer different strategic questions. Averaging them would destroy their meaning. An authorized project decision must choose one, define a replacement rule or explicitly prioritize semester completion over patent-first gating.

The narrow conclusion supported by both is:

1. VibeGuard is the strongest semester build.
2. No frozen MVP is established as a patentable invention.
3. Patent-first selection is sensitive to a short named gate.
4. The attachments contain no authorized choice of gate.
5. The attachments contain no explicit approval of the OpenBraille-to-VibeGuard shift.

**Source basis:** `04_COMPARATIVE_DECISION/02_Final_Adjudications/01_Project_mC_Final_Adjudication_Work_Max.md` and `04_COMPARATIVE_DECISION/02_Final_Adjudications/02_Project_mC_Final_Adjudication_Deep_Research_High.md` (**TIER_2**); `04_COMPARATIVE_DECISION/COMPARATIVE_DECISION_INDEX.md` (**TIER_2**, adjudications are context, not votes).

## 09.8 Team objections and challenge evidence

Team-submitted audits and objections are preserved because they expose practical concerns. They are not automatic authority.

### OpenBraille feasibility disagreement

One team-submitted analysis using a narrower source set described OpenBraille as the least risky semester build. A later submission that included the change request and VibeGuard roadmap reversed the result. The reversal demonstrates source-set sensitivity. Neither submission should be treated as an independent vote.

The broader comparative record and both adjudications support VibeGuard as the strongest semester-build candidate, while retaining OpenBraille as buildable only with explicit mechanical, power, reset and tactile gates.

### Macro Braille objection

The objection that the macro cell is not standards-compliant is correct as a limitation and already reflected in PDR-016. It becomes overstated when non-compliance is treated as proof that the mechanism experiment has no value.

The controlled description is: a non-standard macro tactile/mechanical proof-of-concept that must not claim ISO compliance, fluent reading or commercial-display functionality.

### ESP32/STM32 objection

The claim that ESP32 is automatically a fatal course violation is not established by the attached teacher requirements. The record says STM32 was mentioned and the final board must follow authoritative records and teacher approval.

Therefore, the issue is unresolved platform acceptance, not a proved fatal defect. The frozen architectures remain project truth, while academic acceptance requires explicit confirmation or a controlled substitution.

### Power objection

The concern that six SG90-class servos may exceed a practical 5 V/2 A margin is material. It does not silently cancel PDR-020, but it prevents the manual from describing the supply as proven.

The required resolution is physical staged testing: one-servo current, multiple-servo sequences, brownout monitoring, stall conditions and safe margin before full integration.

### Presentation-quality objections

Terminology errors, omitted block diagrams and weak presentation structure can harm review quality, but they do not decide technical feasibility by themselves. They belong primarily in the teacher-review and presentation chapter, not as substitutes for comparative engineering evidence.

**Source basis:** the three team-submitted files under `04_COMPARATIVE_DECISION/04_Team_Audits_and_Objections/` (**TIER_2**), reconciled against teacher requirements and Decision Register v1.2 (**TIER_1**).

## 09.9 Proposed OpenBraille-to-VibeGuard shift

### What the evidence recommends

Both adjudications identify VibeGuard as the best semester-build candidate. The teacher-context record and formal request give consistent reasons:

- stronger feasibility within the permitted semester period;
- simpler physical implementation;
- better fit with the team’s embedded, ESP32, cybersecurity and signal-processing strengths;
- clearer quantitative bench validation;
- stronger live demonstration;
- lower dependence on precision FDM mechanics, repeated cam/guide fabrication, tactile verification and multi-servo power behavior; and
- a comfortable expected semester budget.

The formal request historically estimated approximately ₹2,200 expected and approximately ₹3,900 protected envelope for VibeGuard, compared with approximately ₹3,000 expected and approximately ₹4,900 conservative envelope for OpenBraille. Those values are dated planning evidence inside the attachment; this drafting stage did not refresh them.

### What the team formally requested

The team requested approval to:

- replace the frozen OpenBraille semester implementation with the frozen VibeGuard Level-1 architecture;
- retain OpenBraille as documented accessibility/mechatronics work and a possible future project;
- keep the two concepts’ folders, evidence and claims separate; and
- freeze VibeGuard procurement and role assignment only after approval.

The request is transparent that neither frozen semester MVP is being presented as patent-ready.

### What has not been approved

No explicit teacher approval is proved. The teacher-decision field remains blank. There is no attached signature, date, conditions or separate controlling approval document.

### What remains unresolved

- teacher approval or rejection of the change;
- ESP32 acceptance or an authorized STM32 substitution;
- the adjudication gate to run, if any;
- final concept authorization;
- procurement and Phase 4 entry;
- named role assignment; and
- which future patent-development hypothesis, if any, survives experiments and current prior-art review.

**Source basis:** `01_GOVERNANCE_AND_CONTROL/01_Project_Requirements/Teacher_Project_Requirements_and_Change_Context.md` (**TIER_1**); formal change request and both adjudications (**TIER_2**).

## 09.10 Semester-build versus future-patent decision

The safest current decision statement is not “VibeGuard won everything.” It is:

- **For semester execution:** VibeGuard has the strongest support.
- **For later patent development:** the evidence is unresolved.
- **For approval:** no teacher decision is attached.
- **For legal/IP conclusions:** no current clearance exists.

The concept boundaries are:

| Concept | Frozen semester MVP | Later research only |
|---|---|---|
| OpenBraille | Macro six-dot cell, six servos/cams, guided pins, ESP32 control and validated active retraction/power/tactile workflow | D11 current/physical-state observability, VPD-C7 pin-side datum, practical-scale claim-focused work |
| VibeGuard | One ADXL345-class sensor, ESP32, RMS/persistence, triggered FFT, RGB/USB and controlled rig | PIRG, target/interferer attribution, ambiguity/abstention, protected updates and field-like remount studies |
| TrueMoist | One-soil compensation using temperature, salinity-treatment code, fixed regression, USB logs, 72 runs and gravimetric truth | Probe replacement/remount transfer, reference challenges, validity/contamination gating, lot/population and multi-soil studies |

A successful semester MVP does not prove the later mechanism. A later mechanism should not be added late to the semester scope merely to preserve a patent narrative.

## 09.11 Open gates, experiments and approvals

| Item | Current status | Required next action |
|---|---|---|
| Teacher approval of VibeGuard shift | Open | Obtain explicit approval, conditional approval or rejection |
| Selection-gate choice | Two conflicting recommendations | Authorize one gate or a documented replacement rule |
| VibeGuard Level-1 thresholds | Not fully frozen in controlling register | Pre-register session split, false-alert, missed-detection and repeatability criteria |
| VibeGuard later attribution/site access | Unverified | Secure independently labelable access before later research |
| OpenBraille reset | Pending physical inspection | Prove passive return or freeze active cam retraction |
| OpenBraille power | Unvalidated | Measure current, voltage, brownout and stall behavior |
| OpenBraille tactile protocol | Open | Approve blinded method, participant plan and quantitative threshold |
| TrueMoist facilities | Pending | Confirm oven/scale access and dry-to-constant-mass workflow |
| TrueMoist early gates | Pending | Run ADC, probe repeatability, packing and salinity pilots |
| Current patent status/FTO | Unavailable | Perform current primary-source search and institutional/professional review after mechanism freeze |
| Current prices and supplier authenticity | Not refreshed in this stage | Verify manufacturer specifications and reputable Indian supply before procurement |
| Phase 4 and procurement | Not authorized | Start only after concept, board and gate decisions are recorded |

## 09.12 Conservative current-state conclusion

The comparative evidence supports **VibeGuard as the strongest semester-build recommendation**. It does so because the frozen Level-1 architecture is simpler to assemble, better aligned with the team, easier to divide into subsystems, quantitatively testable and safer to recover when a component or method fails.

That conclusion does not erase OpenBraille. OpenBraille remains a valid accessibility/mechatronics prototype and a documented future research path. Its macro scale and mechanical risks limit current claims, but they do not prove that the concept was fraudulent or wasted.

TrueMoist remains a rigorous measurement and publication path with strong controlled-experiment value. Its workload and facility requirements distinguish it from VibeGuard rather than invalidate it.

The two final adjudications agree only on the semester-build winner. They disagree on the best later patent path, first gate and fallback. The attached record therefore supports a proposed OpenBraille-to-VibeGuard shift, not a completed shift. Final authorization, platform acceptance, gate choice, procurement and Phase 4 remain open.

## 09.S Source notes

**TIER_2 — common evidence, gates and audits**

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

**TIER_2 — adjudications, request and team challenges**

- `04_COMPARATIVE_DECISION/02_Final_Adjudications/01_Project_mC_Final_Adjudication_Work_Max.md`
- `04_COMPARATIVE_DECISION/02_Final_Adjudications/02_Project_mC_Final_Adjudication_Deep_Research_High.md`
- `04_COMPARATIVE_DECISION/03_Change_Request/Project_mC_Request_to_Change_from_OpenBraille_to_VibeGuard.docx`
- `04_COMPARATIVE_DECISION/03_Change_Request/Project_mC_Request_to_Change_from_OpenBraille_to_VibeGuard.pdf`
- `04_COMPARATIVE_DECISION/04_Team_Audits_and_Objections/01_Team_Submission_6222246419165853974.pdf`
- `04_COMPARATIVE_DECISION/04_Team_Audits_and_Objections/02_Team_Submission_6282084529079524834.pdf`
- `04_COMPARATIVE_DECISION/04_Team_Audits_and_Objections/03_Team_Submission_IDK.pdf`
- `04_COMPARATIVE_DECISION/COMPARATIVE_DECISION_INDEX.md`

**Controlling cross-chapter TIER_1 sources**

- `01_GOVERNANCE_AND_CONTROL/02_Decision_Registers/Project_mC_Decision_Register_v1.2.md`
- `01_GOVERNANCE_AND_CONTROL/01_Project_Requirements/Teacher_Project_Requirements_and_Change_Context.md`
- `01_GOVERNANCE_AND_CONTROL/AUTHORITY_MAP.md`

# Part I Consolidated Open-Decision Register

| ID | Decision or uncertainty | Current status | Controlling source | Required next action |
|---|---|---|---|---|
| OD-01 | Teacher decision on OpenBraille-to-VibeGuard shift | Open; request prepared, approval absent | Teacher context (**TIER_1**); change request (**TIER_2**) | Obtain written approval, conditions or rejection |
| OD-02 | Final semester concept authorization | Not conclusively recorded | Decision Register v1.2 (**TIER_1**) | Record one authorized concept decision |
| OD-03 | ESP32/STM32 course acceptance | Unresolved | Teacher context (**TIER_1**) | Obtain explicit teacher/course confirmation or controlled substitution |
| OD-04 | Pre-selection gate | Work Max and Deep Research High disagree | Two adjudications (**TIER_2**) | Authorize one gate or a replacement rule |
| OD-05 | Phase 4 entry | Not started in controlling status | Original repository README (**TIER_1**) | Start only after approval and entry conditions |
| OD-06 | Procurement freeze | Not authorized; prices not refreshed in this stage | Change request (**TIER_2**) and governance protocol | Refresh specs/prices after approval and freeze BOM |
| OD-07 | Named role map | Proposed, not signed | Change request (**TIER_2**) | Assign primary/backup owners |
| OD-08 | OpenBraille reset method | Passive return unproven | PDR-021 (**TIER_1**) | Inspect/test; use active cam retraction unless proved |
| OD-09 | OpenBraille power adequacy | Frozen 5 V/2 A baseline, experimentally unvalidated | PDR-020 (**TIER_1**); U-OB-03 (**TIER_2**) | Run staged current/brownout/stall tests |
| OD-10 | OpenBraille tactile acceptance | Protocol and threshold open | EDR and uncertainty register (**TIER_2**) | Approve blinded protocol and quantitative criterion |
| OD-11 | VibeGuard Level-1 thresholds | Not fully frozen | EDR/uncertainty register (**TIER_2**) | Pre-register session splits and error/repeatability metrics |
| OD-12 | VibeGuard later attribution access | Unverified | Adjudications/uncertainty register (**TIER_2**) | Secure independently labelable field-like access before later work |
| OD-13 | TrueMoist facility access | Pending | PDR-048/PDR-061 (**TIER_1**) | Confirm oven/scale and dry-to-constant-mass workflow |
| OD-14 | TrueMoist early physical gates | Pending | PDR-061 (**TIER_1**) | Run ADC, probe, packing and salinity pilots |
| OD-15 | Current patent status and FTO | Unavailable | Authority protocol; comparative audit | Conduct current primary-source and professional/institutional review |
| OD-16 | Confidentiality, ownership and inventorship | Unresolved | Adjudications (**TIER_2**) | Obtain institutional IPR guidance before public claim-focused disclosure |

# Part I Contradiction Summary

| ID | Chapters | Issue | Controlling resolution | Residual uncertainty |
|---|---|---|---|---|
| CT-01 | 01, 02 | Roadmap/older records show Phase 3 pending | PDR-067 controls: Phase 3C complete for retained three only | Formal Phase 4 authorization |
| CT-02 | 01, 03, 09 | Five historical concepts appear active | PDR-064/PDR-066: active comparison is OpenBraille, VibeGuard and TrueMoist; TrustLatch/ColdTrace deferred | Conditional re-entry |
| CT-03 | 01, 09 | Change request appears beside current project records | Request exists; attached approval does not | Teacher decision |
| CT-04 | 01, 03, 09 | OpenBraille broad/standard/alternative-mechanism descriptions | Frozen current design is the non-standard macro six-servo cam/guided-pin cell | Reset, power and tactile tests |
| CT-05 | 01, 03, 09 | VibeGuard “spatially isolated” or PIRG described as current | Frozen current design is Level-1 ADXL345-class sensor + ESP32 monitoring; attribution is later | Field/site evidence |
| CT-06 | 01, 03, 09 | TrueMoist described as controller/live-EC/universal system | Frozen current design is one-soil local compensation with temperature and treatment code | Early gates and later transfer evidence |
| CT-07 | 02, 03 | Phase 1B.5 has 22 survivors | Corrected valid Phase 1C input is 16 | Historical files require annotation |
| CT-08 | 02, 09 | Model recurrence described as confidence or votes | Recurrence may inform audited confidence; models never vote or override authority | Claim-specific source quality |
| CT-09 | 09 | Best later patent candidate: TrueMoist versus OpenBraille D11 | Preserve both conditional adjudication results | Gate results and current patent verification |
| CT-10 | 09 | First gate: VibeGuard signal/access versus OpenBraille observability | No controlling resolution; explicit authorization required | Gate selection and execution |
| CT-11 | 01, 09 | ESP32 is either certainly allowed or certainly prohibited | Teacher record says STM32 was mentioned; no categorical attached resolution | Official teacher/course confirmation |
| CT-12 | 01, 09 | Optimistic patent language | All routes remain hypotheses; no grant, novelty, inventive-step or FTO promise | Experiments, search and IPR review |

# Part I Source Ledger

Only original organized-workspace paths materially relied upon are listed. The attachment manifest and packet filenames are not technical evidence.

## Chapter 01 — TIER_1

- `01_GOVERNANCE_AND_CONTROL/01_Project_Requirements/Teacher_Project_Requirements_and_Change_Context.md`
- `01_GOVERNANCE_AND_CONTROL/02_Decision_Registers/HISTORICAL_Project_mC_Decision_Register_v1.0.md` — historical/superseded comparison only
- `01_GOVERNANCE_AND_CONTROL/02_Decision_Registers/Project_mC_Decision_Register_v1.2.md`
- `01_GOVERNANCE_AND_CONTROL/03_Project_Context_and_Phase_Map/MC_Project_PHASE_DOC.md` — methodology; stale status caveat
- `01_GOVERNANCE_AND_CONTROL/03_Project_Context_and_Phase_Map/PROJECT_CONCEPT_CONTEXT.md` — original context only
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

## Chapter 02/03 — controlling cross-chapter sources

- `01_GOVERNANCE_AND_CONTROL/02_Decision_Registers/Project_mC_Decision_Register_v1.2.md` — **TIER_1**
- `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/00_Engineering_Design_Review.md` — **TIER_2**

## Chapter 03 — TIER_4 historical sources

- `02_PHASE_HISTORY/Phase_1/Phase_1C_Concept_Synthesis/Phase1C_Concept_Synthesis.pdf`
- `03_CONCEPT_PORTFOLIO/OpenBraille/06_Historical_Phase3C_Research_and_Prompts/Prompts/Phase3C_OpenBraille_Deep_Research_Prompt_Final.md`
- `03_CONCEPT_PORTFOLIO/VibeGuard/06_Historical_Phase3C_Research_and_Prompts/Prompts/Phase3C_VibeGuard_Deep_Research_Prompt_Final.md`
- `03_CONCEPT_PORTFOLIO/TrueMoist/06_Historical_Phase3C_Research_and_Prompts/Prompts/Phase3C_TrueMoist_Deep_Research_Prompt_Final.md`
- `03_CONCEPT_PORTFOLIO/Other_Concepts/README.md`
- `03_CONCEPT_PORTFOLIO/Other_Concepts/TrustLatch/HISTORICAL_Phase1C_TrustLatch_Concept_Dossier.docx`

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

## Chapter 09 — controlling cross-chapter TIER_1

- `01_GOVERNANCE_AND_CONTROL/02_Decision_Registers/Project_mC_Decision_Register_v1.2.md`
- `01_GOVERNANCE_AND_CONTROL/01_Project_Requirements/Teacher_Project_Requirements_and_Change_Context.md`
- `01_GOVERNANCE_AND_CONTROL/AUTHORITY_MAP.md`

<!-- END CONTROLLED COMPONENT: PART_I_RELEASE_CORRECTED -->

---

<!-- BEGIN CONTROLLED COMPONENT: PART_II -->
<!-- SOURCE PATH: /home/paradoxpete/Documents/PROJECT_ORGANIZED/08_MASTER_MANUAL/03_Drafting_Workspace/01_Validated_Parts/Part_II/Project_mC_Master_Manual_Part_II_OpenBraille_Architecture_and_Patent_Path.md -->
<!-- SOURCE SHA-256: be5411283bef7c768abc034ff69fb7fe39c1f3777427102f3a68380c0c61a162 -->

## Part II — OpenBraille Architecture and Patent Research Path

## Document control

| Field | Value |
|---|---|
| Document | Project mC Master Manual — Part II |
| Controlled filename | `Project_mC_Master_Manual_Part_II_OpenBraille_Architecture_and_Patent_Path.md` |
| Status | Controlled draft |
| Scope | Chapter 04 — OpenBraille Frozen Architecture and Semester Scope; Chapter 05 — OpenBraille Patent Evidence and Future Research Path; Part II open-decision, contradiction and source-ledger sections |
| Source boundary | Only the nine attachments in the controlled Part II drafting package |
| Input inventory | Exactly nine physical attachments were present and readable. The eight hash-controlled files matched the manifest byte counts and SHA-256 values. The self-referential manifest was used only for file control. Upload transport suffixes did not create additional logical sources. |
| Current implementation status | This document is not an implementation, procurement or Phase 4 authorization |
| Approval status | This document is not a teacher-approval record and does not establish the authorized semester concept or platform |
| Patent status | No patentability, filing, infringement or freedom-to-operate conclusion |
| External verification | No fresh web, market, manufacturer, standards, legal-status or patent research was performed in this drafting stage |
| Relationship to Part I | Part I remains controlling for the current comparative decision: VibeGuard is the strongest semester-build recommendation; OpenBraille remains retained and legitimate; the proposed shift is not proved teacher-approved; Phase 4 and procurement are not proved started; no frozen MVP is established as patentable; and the two adjudications disagree on the preferred later patent-development route |

The Part II drafting package was complete. The governing instruction, authority and contradiction protocol, Master Manual blueprint, validated Part I, validated OpenBraille reconciliation, Chapter 04 and Chapter 05 source packets, required output template and manifest were readable. No prior-chat context, memory, web research or unstated technical assumption was used. The reconciliation controls resolved wording and contradictions; the source packets provide the underlying evidence; validated Part I controls the current project state.

## How to read Part II

Part II preserves four boundaries.

**Frozen architecture versus refinements.** OpenBraille means one non-standard macro six-dot cell with six SG90-class servos, six cam/follower channels, six guided pins, ESP32 direct PWM, FDM structure, external servo power, USB command/logging, active retraction and single-dot-first validation. Calibration, tolerance, guarding, sequencing, logging and power-distribution changes may refine this architecture; replacing it requires formal change control.

**Semester MVP versus future research.** The semester MVP is an educational embedded/mechatronics prototype. D11 and VPD-C7 are separate post-MVP hypotheses and must not be backfilled into the semester result.

**Targets versus results.** Dimensions, supply ratings, costs, repeatability thresholds, lifecycle screens and tactile criteria are planning values until configuration-controlled tests establish results.

**Patent evidence versus filing.** Research identifies prior art, uncertainties and experiments. It does not prove novelty, authorize filing or provide FTO. The current decision is no filing commitment.

# Chapter 04 — OpenBraille Frozen Architecture and Semester Scope

## 04.1 Chapter purpose

This chapter defines the controlled OpenBraille semester architecture, the boundary of permissible engineering work and the evidence required before implementation claims may be made. It is an implementation reference, not permission to purchase parts or enter Phase 4.

OpenBraille asks a bounded question: can a five-member student team use commodity actuation, embedded control and accessible FDM fabrication to produce one repeatable refreshable macro six-dot cell and document its limits? The project does not claim to solve the commercial refreshable-Braille problem. A successful result would demonstrate controlled electromechanical integration at educational geometry; a partial or negative result remains valuable when recorded honestly.

## 04.2 Current architecture identity

> **OPENBRAILLE ARCHITECTURE LOCK**
>
> For the frozen semester architecture, **OpenBraille means only**:
>
> - one permanent, non-standard macro-scale six-dot tactile cell;
> - six SG90-class micro servos, one actuator per dot;
> - six eccentric cam/follower channels;
> - six guided vertical tactile pins with safe rounded tips;
> - one ESP32-WROOM-32-class controller using six direct PWM signal channels;
> - FDM-manufactured frame, guides, cams/followers and related structure;
> - an external regulated servo-power branch with measured current headroom;
> - a shared electrical reference ground between the ESP32 signal domain and servo-power domain;
> - USB/serial command input and evidence logging;
> - active servo-driven raise and retract positions; and
> - mandatory single-dot-first commissioning before six-dot integration.
>
> This is an educational tactile/mechanical proof-of-concept. It is **not** an ISO-compliant cell, commercial refreshable Braille display, fluent-reading device, validated assistive product, patent-ready mechanism or approved semester implementation.

The architecture lock exists because earlier OpenBraille work contained several alternative mechanisms and because later patent work introduced separate experimental hypotheses. Those records remain useful as history or research context, but they do not change the frozen semester identity.

The most important correction concerns return motion. Earlier Phase 3C wording assumed that an internal servo spring or passive mechanical effect would reliably reset the pin. The controlling rule is now active retraction. Firmware and cam geometry must deliberately command and produce both raise and lower motion. A passive contribution may be observed and documented, but it may control the architecture only after the procured, fully coupled servo/cam/follower/pin channel proves repeatable return under the intended load. Until then, passive return is an unproved possibility, not a design fact.

Macro scale is equally important. The enlarged cell is not a temporary presentation mock-up within the semester architecture; it is the selected fabrication strategy for that architecture. Post-semester research may explore smaller practical geometry, but such work is a separate configuration and cannot be reported as the frozen semester cell.

## 04.3 Bounded semester objective

The semester objective is to build and evaluate one macro six-dot cell that accepts a supported character or six-bit pattern through USB/serial, independently commands six channels, actively raises and retracts the intended pins, and records enough physical and digital evidence to distinguish commanded behavior from actual behavior.

The interface may remain small and versioned: raw six-bit pattern, clear/all-down, one-dot diagnostic, calibration/test commands and a frozen character subset. A complete language interface, screen reader, multi-cell line or fluent-reading benchmark is outside scope.

Evidence must cover mechanics, electrical power, firmware mapping, repeatability and—only through an approved protocol—tactile distinguishability. Macro scaling reduces fabrication risk but cannot establish practical Braille pitch, product thickness, speed, noise, durability, array density or user readiness.

## 04.4 System architecture overview

| Subsystem | Frozen role | Principal interfaces | Evidence boundary |
|---|---|---|---|
| Host computer | Sends characters, six-bit patterns and controlled test commands; receives logs | USB data connection to ESP32 | Host acknowledgement proves data exchange only, not physical pin state |
| ESP32 controller | Parses commands, applies mapping, generates six PWM signals, sequences transitions and logs state | USB serial; six servo signal lines; shared reference ground | GPIO map and board behavior require validation on the exact purchased board |
| Servo channels | Six SG90-class servos provide rotary actuation, one per dot | Direct PWM signal; external regulated servo rail; mechanical coupling | Commanded angle does not prove output torque, cam position or pin endpoint |
| Cam/follower conversion | Six eccentric cams/followers convert servo rotation into vertical motion | Servo horn/coupling; follower; guided pin | Geometry and friction require coupon measurement; no passive reset assumption |
| Guided pin assembly | Produces the raised or lowered tactile state | Follower, guide, rounded tip and frame datum | Raised/lowered bands require external displacement evidence |
| FDM structure | Maintains pitch, alignment, guides, actuator mounting, guarding and cable management | All mechanical channels and fasteners | Printed dimensions and finishing must be measured and versioned |
| Servo-power branch | Supplies actuator energy independently of laptop USB | External regulated 5 V-class supply, distribution, conductors and bulk capacitance | A 2 A or 3 A label is not proof of adequacy; measured headroom controls |
| Development ground truth | Measures physical travel, force where available, current/voltage and visible failure | Calipers, camera/fixed jig, multimeter and approved test fixtures | External measurement supports development; it is not a permanent semester endpoint sensor |
| Evidence and configuration system | Associates commands and measurements with firmware, CAD, calibration and BOM revisions | USB logs, photographs, test sheets and repository records | Unversioned results cannot support final acceptance statements |

The subsystem boundaries deliberately prevent one type of evidence from substituting for another. For example, servo current may reveal effort, a stall-like condition or supply disturbance, but it does not by itself show that a tactile pin reached the correct height. A camera may show motion but cannot automatically establish user distinguishability. A successful character mapping test proves software logic, not mechanical correctness. The final demonstration must bring these evidence streams together without confusing them.

## 04.5 Functional and control flow

The controlled functional sequence is as follows:

1. The host transmits a supported character, explicit six-dot pattern or controlled service command over USB serial.
2. The ESP32 validates syntax, command length and permitted range. Invalid commands are rejected and logged without moving the mechanism.
3. A versioned mapping table converts a supported character into a six-bit target pattern. Raw dot-pattern commands bypass the character mapping but remain range checked.
4. The controller compares the target pattern with its last commanded pattern and identifies only the channels that require a state change.
5. The transition engine applies the frozen sequencing policy. It may actuate changed channels sequentially or in a bounded group if that policy has passed power and timing tests.
6. For every selected channel, the PWM manager issues the versioned raise or retract command value derived from external calibration.
7. The servo rotates its eccentric cam. The cam/follower interface converts rotary movement into constrained vertical pin travel.
8. A raise command drives the pin toward its measured upper band. A lower command actively drives the pin toward its measured retracted band.
9. Firmware records the command, target pattern, channel sequence, timing, configuration ID, reset events and declared faults.
10. Development measurements determine whether the physical state matched the command. Where direct physical evidence is absent, the correct runtime statement is `COMMAND_FINISHED`, `INCOMPLETE`, `FAULT` or `UNKNOWN`, not `UPPER_CONFIRMED` or `LOWER_CONFIRMED`.

The distinction between commanded and measured state is a core design rule. The controller may maintain a **command-state model** for sequencing, but that model is not a physical-state oracle. Servo pulse width, elapsed time, visible rotation and a current transient can all occur while a pin binds, a follower disengages, a horn slips or the mechanism stops short. Acceptance therefore depends on an independently measured physical band during calibration and locked validation.

The ordinary semester design does not include a permanent six-pin endpoint-sensing system. External calipers, a fixed camera/displacement fixture or other approved measurement method may provide ground truth during development. Those fixtures remain test equipment unless a later authorized architecture change states otherwise. Permanent D11 or VPD-C7 hardware must not be added late to the semester cell.

## 04.6 Mechanical architecture

The cell contains six independently testable channels. Each channel uses an SG90-class servo, horn/coupling, eccentric cam, follower, guided vertical pin and local support geometry. A shared FDM frame maintains the macro six-dot arrangement, provides alignment and mounting, and carries guarding and cable-management features.

Historical architecture work used approximately three times a cited sign-Braille geometry, with roughly 7 mm pitch and 1.5 mm raised travel as starting targets. These values are provisional CAD/test references, not standards claims or achieved measurements. Final dimensions must come from printed tolerance coupons, procured-part measurements and controlled travel tests.

A raised state is a measured protrusion band accepted by the approved macro tactile protocol. A lowered state is a measured retracted band that avoids an unintended dot. Neither may be inferred from PWM, servo angle, elapsed time or visible cam motion alone.

**Active retraction controls.** The lower command and cam geometry must return the pin to the measured lower band. Gravity, elastic effects or servo construction may assist only after the complete coupled mechanism proves reliable loaded return.

**Single-dot-first construction is mandatory.** Before a six-dot frame is committed, one coupon must reveal guide binding, pin tilt, follower loss, cam-profile error, coupling slip, unsafe stall, raised/lowered overlap, return failure, pinch hazards and repeatability. Six-dot fabrication follows only after measured motion, safe operation and a versioned calibration are established.

Allowed mechanical development includes tolerance coupons, controlled finishing, print-orientation/material changes within the FDM route, cam-profile iteration, rounded tips, guards and replaceable channel fixtures. A new actuation principle requires formal change control. Smaller practical-scale work is separate post-semester research.

## 04.7 Electronics and power architecture

The baseline controller is an ESP32-WROOM-32-class development board. It supplies six independent PWM control signals directly to the integrated electronics of the six SG90-class servos. The architecture does not require an H-bridge, Darlington array or external motor driver for these servo signal inputs. A different board or actuator may be considered only through explicit change control and complete revalidation.

The exact GPIO allocation remains provisional until checked against the exact purchased board and its manufacturer documentation. The final mapping must avoid input-only pins, boot-strapping conflicts and clashes with any required serial or peripheral function. The configuration record should identify board variant, GPIO map, firmware build and wiring revision.

USB serves two controlled roles:

- host-to-controller command input; and
- controller-to-host logs and evidence metadata.

USB is not the servo-power source. Servo current must not pass through the laptop cable or the ESP32 3.3 V regulator. The six servos require an external regulated 5 V-class supply connected through suitable distribution, conductor sizing and protection. The ESP32 signal ground and servo-power ground must share the intended reference point so that PWM levels are meaningful, while the high-current branch remains physically separate from the USB and logic-power path. The wiring must be inspected for accidental back-feed before a laptop is connected.

Historical records mention both 5 V/2 A and 5 V/3 A planning values. Neither is accepted solely because it appears on an adapter label. The controlling requirement is an external regulated supply with measured headroom under the frozen worst planned transition. Acceptance should consider:

- minimum rail voltage during transitions;
- aggregate and channel current;
- ESP32 reset or serial-disconnect events;
- servo chatter and incomplete motion;
- connector, conductor and regulator heating;
- supply protection behavior;
- repeated transition stability; and
- behavior during a jam or bounded fault test.

Bulk capacitance near the servo distribution is an allowed transient-control refinement. It cannot compensate for an undersized or unsafe supply. Similarly, sequential actuation may reduce peak demand and make faults easier to attribute, but it must still meet the approved refresh-time requirement and cannot be presented as proof of a novel power architecture.

## 04.8 Firmware architecture and operating sequence

The firmware should be deterministic and inspectable. Its required modules are:

| Module | Required function | Controlled output |
|---|---|---|
| Configuration manager | Board/GPIO, channel, build, CAD, calibration and sequencing identity | Configuration ID at boot and in logs |
| USB/serial parser | Validates character, raw-pattern, clear, test and calibration commands | Accepted command or explicit rejection |
| Mapping table | Converts the frozen character set to six-dot patterns | Unit-tested pattern and table version |
| PWM/channel manager | Applies bounded per-dot raise/retract values | Commanded state and timing record |
| Calibration manager | Stores externally measured operating windows | Versioned values; no runtime physical-state claim |
| Transition engine | Changes required dots using the locked sequence | Ordered transition record |
| Fault/log manager | Records invalid input, reset, timeout, isolation and bounded retry | Machine-readable event log |
| Test mode | Runs one-dot, repeatability and lifecycle procedures | Test ID, cycle count and stop reason |

Normal operation is: verify wiring; boot and emit identifiers; initialize a safe commanded state; validate the host command; calculate the target pattern; actuate changed channels using the frozen sequence; log completion and faults; and use external measurement for physical confirmation during tests. Absent or conflicting evidence remains `UNKNOWN`.

A boot sweep or timeout may prove that software issued commands; it cannot verify pin travel, height, retraction or tactile correctness. Mapping tests must cover the complete frozen set before physical validation. Automatic retries must remain within a physically qualified bounded policy.

## 04.9 Build materials and manufacturing control

FDM printing is the frozen manufacturing route. ABS-class frame material, PETG/Nylon-class cam/follower material and stainless-steel pins are candidate recommendations, not validated specifications. Final choices must follow actual print behavior, friction, wear and availability.

Configuration control must retain CAD/print-file versions, printer and material identity, print settings, measured dimensions, post-processing, assembly operator, photographs, replacement history and failed coupons. A tolerance matrix should establish guide fits and cam/follower clearances before full fabrication.

Dependable FDM access is an entry gate because cost and schedule assume institutional printing. Changing manufacturing route requires authorization. Rounded tips, guarded pinch points, restrained wiring and immediate power isolation are required safety controls; sharp pins, ejected parts, overheating or uncontrolled force are stop conditions.

## 04.10 BOM and budget evidence

The attached record contains several historical planning layers. They show that the frozen architecture may fit the project ceiling under stated assumptions, but none is a current supplier quotation.

| Evidence layer | Included basis | Historical amount | Correct treatment in Part II |
|---|---|---:|---|
| Phase 3C architecture estimate | ESP32, six SG90-class servos, 5 V/2 A planning supply, capacitor, FDM structure, pins, wiring and assembly materials | ₹2,060–₹2,850 | Order-of-magnitude architecture estimate only |
| Patent-synthesis MVP plus optional experiment envelope | Frozen MVP plus datum/guide variants, current-sense parts, substitute test servos, ground-truth fixture and contingency | ₹2,910–₹4,700 | Conditional research planning; must not consume the semester MVP budget without authorization |
| Reference-dossier expected semester plan | Detailed required purchased/fabricated items with institutional printing | approximately ₹2,984 | Preferred internal planning figure in the attached record; not a current quotation |
| Reference-dossier conservative envelope | Higher component/material allowances, delivery/replacement margin and controlled reprints | approximately ₹4,909 | Conservative planning envelope below the ₹5,000 maximum only under stated printing assumptions |
| Controlling project constraint | Preferred budget and absolute hardware ceiling | ≤₹3,000 preferred; ≤₹5,000 maximum | Actual procurement must be controlled by current verification, authorization and invoices |

### Reconciled planning BOM

The frozen architecture requires, at planning level:

- one ESP32-WROOM-32-class development board;
- six SG90-class micro servos, with any spare purchase separately justified;
- one external regulated 5 V-class supply with measured current headroom;
- bulk capacitor or capacitors appropriate to measured transient behavior;
- FDM-printed frame, guides, cams/followers and guards;
- six rounded tactile pins plus controlled spares;
- fasteners, servo horns/couplings and mounting hardware;
- perfboard or equivalent distribution, wiring, headers and connectors;
- one reliable USB data cable; and
- labels or other means to preserve channel and configuration identity.

Required capabilities such as digital calipers, multimeter, laptop, printer, fixed camera/displacement jig, hand tools and approved tactile-test resources may be institutional or reusable. They should not be hidden from the feasibility assessment simply because they are not purchased as project hardware.

Final procurement requires a later external-verification stage covering exact manufacturer specifications, current Indian prices, availability, supplier authenticity, delivery time and institutional printing cost. Purchased, borrowed, donated and institutional items must be recorded separately. The final cost statement should use actual invoices and document exclusions rather than repeating a historical estimate as a current total.

## 04.11 Minimum demonstrable success

The controlled minimum demonstrable success is:

> One non-standard macro six-dot cell, built within the approved budget and schedule, accepts a controlled character or dot pattern through USB/serial; independently commands all six servo/cam/pin channels; actively raises and retracts the intended dots; reproduces the frozen supported patterns without unsafe power behavior; and provides measured mechanical, electrical, firmware and tactile evidence under a preregistered protocol while reporting all limitations and failures.

The attached architecture work proposes the following acceptance targets. Their status must remain explicit.

| Proposed target | Purpose | Present status |
|---|---|---|
| All six channels independently raise and actively retract | Basic six-dot function | Proposed; no physical result attached |
| No brownout, unsafe rail collapse, connector heating or servo stall in the frozen sequence | Electrical and power acceptance | Proposed; supply adequacy unmeasured |
| 100% correct mapping for the frozen supported pattern set | Firmware correctness | Proposed; supported set not finally frozen |
| Position variation at or below 0.1 mm over a 100-cycle measured set | Early repeatability screen | Proposed; method and threshold require preregistration/approval |
| At least 1,000 actuations | Early wear/lifecycle screen | Proposed; cycle definition and failure rules not executed |
| Teacher/institution-approved blinded tactile threshold and trial count | Bounded tactile distinguishability | Unresolved; participant, consent and stop rules not attached |

These targets are not achieved results and are not automatically the final acceptance criteria. They should be preregistered before locked validation, including measurement method, exclusion rules, uncertainty, stop conditions and how negative data will be reported.

A visually correct pattern is not sufficient for tactile success. If an approved tactile route is unavailable, the team may report mechanical travel and visual pattern formation but must state that tactile validation was not conducted. Team-member visual judgement or informal touching cannot be represented as user validation.

## 04.12 Validation and entry-gate sequence

| Gate | Question | Required evidence | Pass consequence | Fail consequence |
|---|---|---|---|---|
| OB-G0 | Is OpenBraille and its platform authorized? | Explicit teacher/project decision | Permit procurement planning | Do not assume approval |
| OB-V0 | Are the exact board, first servo, supply, FDM access and tools usable? | Board/USB check, controlled sweep, supply and facility confirmation | Freeze coupon inputs | Resolve before CAD commitment |
| OB-V1 | Can one channel raise and actively retract freely and safely? | Versioned coupon, measured travel, repeated cycles and inspection | Authorize remaining channels | Redesign; stop six-dot expansion |
| OB-V2 | Do measured command windows create repeatable upper/lower bands? | External displacement evidence | Store versioned values | Change geometry/actuator; do not tune blindly |
| OB-V3 | Do six channels coexist without interference or power failure? | Pattern tests, rail/reset log and inspection | Freeze integrated configuration | Improve distribution/sequence or rebuild |
| OB-V4 | Does firmware produce the intended states? | Unit tests and physical checks | Permit locked pattern evaluation | Correct mapping/configuration |
| OB-V5 | Does travel remain acceptable through cycle screening? | 100-cycle dataset, ≥1,000-actuation record and wear log | Permit final validation | Redesign, narrow or report failure |
| OB-V6 | Are states/patterns distinguishable under an approved tactile protocol? | Preregistered blinded method and raw results | Support bounded macro tactile conclusion | Adjust or report tactile MDS not achieved |
| OB-V7 | Can the frozen build reproduce verified behavior safely? | Frozen CAD, firmware, calibration, BOM and signed checklist | Demonstrate verified capabilities | Use approved fallback evidence and disclose failure |

Single-dot-first validation prevents six copies of the same defect and keeps mechanical, power and firmware failures separable. The final demonstration must use the same controlled configuration that produced the acceptance evidence; late changes require revalidation.

## 04.13 Mechanical, electrical and tactile risks

| Risk | Current evidence state | Required control |
|---|---|---|
| Printed guide/cam tolerance | Macro scaling helps; no coupon result attached | Tolerance matrix, measurement, finishing record and one-dot gate |
| Pin tilt/follower loss | Identified, untested | Stop and redesign before expansion |
| Active retraction | Passive return unproved | Loaded raise/retract measurement; retain active command |
| Servo torque/stall | Plausible actuator, untested geometry | One-dot travel/current/force tests; no automatic upgrade |
| Cam/follower wear | Materials proposed only | ≥1,000-actuation screen and inspection log |
| Six-servo power demand | 2 A/3 A are planning values | External supply, measured droop/current, resets and heat |
| USB/grounding error | Wiring boundary unverified | Shared reference, separated current path and back-feed inspection |
| Command-state confusion | Conceptually resolved, implementation risk remains | External evidence and `UNKNOWN` state |
| Tactile distinguishability | No approved validation | Blinded approved protocol and limitations |
| Repeatability drift | Proposed threshold only | Preregister method and report distribution |
| Pin/pinch safety | Foreseeable hazards | Rounded tips, guards, isolation and supervision |
| Facility/schedule dependency | FDM access assumed | Confirm printer, material and queue |
| Scope overclaim | Strong visible demo can mislead | Use controlled current-state language |

A failed gate must trigger documented iteration within scope, formal change control, a narrowed result or route closure—not a hidden architecture substitution.

## 04.14 Allowed refinements

The following work may be performed without changing the frozen architecture, provided every change is versioned, remains inside the approved budget/schedule and is revalidated where necessary:

- per-dot PWM calibration derived from external displacement evidence;
- measured active raise and retract command windows;
- FDM tolerance coupons and controlled guide-clearance changes;
- cam-profile iteration within the eccentric cam/follower principle;
- documented post-processing and print-orientation changes;
- suitable FDM material substitutions that retain the same architecture;
- rounded pin-tip refinement and pinch-point guards;
- fixed sequential or bounded-group actuation of changed dots;
- improved external power distribution, conductor sizing and bulk capacitance based on measurement;
- deterministic USB commands, mapping tests, configuration IDs and fault logs;
- external camera, caliper, displacement or force fixtures used as development ground truth;
- one-dot and replaceable channel test fixtures within the same servo/cam/pin structure; and
- mounting, cable-management and serviceability changes that do not create a new actuator or cell architecture.

These are ordinary engineering refinements unless later physical evidence shows a distinct non-additive effect and Chapter 05’s patent-development gates are satisfied. Their presence does not make the semester MVP patentable.

## 04.15 Prohibited substitutions

The following must not be introduced or described as the frozen OpenBraille semester design:

- moving-roller or rotating encoder-wheel actuation;
- continuous-paper Braille printing or embossing;
- RAMPS/Mega motion-control architecture;
- electromagnetic latching, non-latching solenoid, SMA, pneumatic or other replacement actuation;
- a commercial-scale standard Braille cell or multi-cell reading line;
- PCA9685 or multi-cell expansion represented as part of the current one-cell scope;
- STM32, ESP32-S3, MG996R or another board/actuator substituted without explicit project and teacher change control;
- passive spring or gravity return stated as proven without coupled-mechanism evidence;
- permanent D11 or VPD-C7 sensing/datum hardware added to the semester cell;
- a hybrid with VibeGuard or TrueMoist; or
- any architecture change disguised as a refinement to preserve schedule or patent narrative.

Alternatives may be revisited only in a later authorized change record. They must remain labelled as new or superseded designs rather than being backfilled into the Phase 3C identity.

## 04.16 Current implementation and approval status

> **OPENBRAILLE CURRENT-STATE BOX**
>
> **Established by the attached record**
>
> - The six-servo macro-cell architecture is frozen and sufficiently reconciled for controlled manual drafting.
> - OpenBraille remains a retained, legitimate accessibility/mechatronics concept.
> - Historical planning evidence indicates possible fit within the ₹5,000 hardware ceiling under institutional-printing assumptions.
> - Single-dot-first validation, active retraction, external servo power and command-versus-physical-state separation are controlling requirements.
>
> **Not established by the attached record**
>
> - Teacher approval of OpenBraille as the semester implementation.
> - Teacher/course acceptance of the ESP32 platform.
> - Phase 4 entry, procurement freeze or named role ownership.
> - A built one-dot coupon or integrated six-dot cell.
> - Mechanical, electrical, lifecycle, tactile or user validation.
> - Current manufacturer specifications, Indian prices, availability or supplier authenticity.
> - Standards compliance, commercial readiness or patent readiness.
>
> Validated Part I records VibeGuard as the strongest semester-build recommendation and the OpenBraille-to-VibeGuard change as a request rather than a proved approval. This chapter therefore preserves OpenBraille as a complete retained/fallback implementation path without claiming current authorization.

Before implementation, the project requires an explicit decision on concept and platform, confirmation of FDM and measurement access, current specification and price verification, a controlled budget, named subsystem ownership and approval of safety and tactile-testing procedures. Drafting readiness is not implementation readiness.

## 04.17 Chapter conclusion

OpenBraille is one non-standard macro six-dot cell using six SG90-class servos, six cam/follower channels, six guided pins, ESP32 direct PWM, FDM structure, external servo power, USB command/logging, active retraction and single-dot-first validation. It can support a disciplined student engineering programme only if command state is kept separate from physical truth and the one-dot, power, repeatability, safety and tactile gates are enforced.

A successful result is a bounded educational proof-of-concept, not a commercial Braille product or patent conclusion. This chapter does not authorize procurement, establish semester selection or prove standards compliance.

## 04.S Source notes

The material conclusions in Chapter 04 rely on the following original organized-workspace paths. The attached packet and manifest are not cited as original technical sources.

### TIER_1 — Current architecture and project authority

- `03_CONCEPT_PORTFOLIO/OpenBraille/01_Final_Architecture/Phase3C_OpenBraille_Architecture_Report_Final.md` — frozen servo/cam/pin identity, macro-scale architecture, initial BOM, firmware organization and milestone sequence; corrected where higher authority requires active retraction and measured-state wording.
- `03_CONCEPT_PORTFOLIO/OpenBraille/01_Final_Architecture/Phase3C_OpenBraille_Memory_Final.md` — concise frozen architecture record; passive-return language is not controlling.
- `03_CONCEPT_PORTFOLIO/OpenBraille/01_Final_Architecture/Phase3C_OpenBraille_SOP_Final.md` — architecture-selection and implementation-reference procedure.
- `01_GOVERNANCE_AND_CONTROL/02_Decision_Registers/Project_mC_Decision_Register_v1.2.md` — current owner decisions, active-retraction control, portfolio and phase status.
- `01_GOVERNANCE_AND_CONTROL/01_Project_Requirements/Teacher_Project_Requirements_and_Change_Context.md` — budget, course, platform, team and proposed-change context; not proof of approval.

### TIER_2 — Supporting status and evidence

- `03_CONCEPT_PORTFOLIO/OpenBraille/05_Roadmaps_and_Reference_Dossiers/OpenBraille_Semester_Architecture_and_Future_Research_Reference_Dossier.docx` — corrected command/state semantics, power-domain boundary, implementation gates, detailed planning BOM and configuration-control guidance.
- `03_CONCEPT_PORTFOLIO/OpenBraille/05_Roadmaps_and_Reference_Dossiers/OpenBraille_Semester_Architecture_and_Future_Research_Reference_Dossier.pdf` — duplicate publication format of the same dossier; not independent corroboration.
- `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/05_Uncertainty_and_Test_Register.md` — unresolved mechanical, power, quantitative and tactile evidence.
- `04_COMPARATIVE_DECISION/02_Final_Adjudications/01_Project_mC_Final_Adjudication_Work_Max.md` — semester-build and later-research context only.
- `04_COMPARATIVE_DECISION/02_Final_Adjudications/02_Project_mC_Final_Adjudication_Deep_Research_High.md` — semester-build and later-research context only.
- `04_COMPARATIVE_DECISION/COMPARATIVE_DECISION_INDEX.md` — treatment of adjudications as context rather than votes.
- `03_CONCEPT_PORTFOLIO/OpenBraille/PATENT_EVIDENCE_INDEX.md` — controlled research-set status and exclusion of the failed concept-swapped synthesis.
- `03_CONCEPT_PORTFOLIO/OpenBraille/README.md` — concept-folder status and navigation only where consistent with higher authority.

# Chapter 05 — OpenBraille Patent Evidence and Future Research Path

## 05.1 Chapter purpose and legal boundary

This chapter records the controlled patent-evidence position and a conservative future research path. It is not legal advice, claim construction, a patentability opinion, an infringement conclusion or FTO clearance, and it does not update the historical research cut-offs.

Four layers remain separate: the frozen semester MVP; ordinary refinements; post-semester experiments concerning datum, calibration, observability, wear, replacement and scale; and speculative D11/VPD-C7 mechanisms. Progress between layers requires enabled hardware, direct evidence, strong baselines, transfer and current primary-source/IPR review. Semester engineering value does not imply patent value.

## 05.2 Ordinary MVP patent position

> **OPENBRAILLE PATENT CURRENT-STATUS BOX**
>
> - The frozen macro six-servo MVP is **not established as a credible patent target**.
> - The current decision is **no filing commitment**.
> - No novelty, inventive step, patent eligibility, useful claim scope, infringement clearance, freedom to operate or probable grant is established.
> - D11 and VPD-C7 are separate, unbuilt research hypotheses outside the semester architecture.
> - A later positive experiment may become eligible only for institutional or professional file/no-file evaluation after current primary-source prior-art, legal-status, FTO, confidentiality, ownership and inventorship review.

The ordinary MVP combines known or crowded functional elements: motor-driven or cam-driven Braille pin movement, independently actuated tactile dots, mechanical guides and stops, modular structures, commodity embedded control, PWM, calibration, fixed sequencing, printed fabrication and low-cost open-hardware construction. The reviewed evidence did not show a persuasive technical interaction that transforms this combination into a presently credible invention.

No reviewed independent claim was shown to contain every exact procurement and dimensional detail of the project. That absence is not a positive novelty result. A claim restricted to six SG90 servos, an ESP32 board, FDM parts and an enlarged cell would likely be narrow, predictable and easy to design around. Low cost and student accessibility are valuable project attributes, but they do not themselves establish inventive step.

Macro scale further limits the patent case. It reduces fabrication risk and supports a visible class demonstration, but it does not enable broad claims to standard-scale Braille geometry, compact cell thickness, practical array density, acceptable force, noise, speed, durability or fluent reading. Broad mechanical claims require practical-scale construction and disclosure.

The correct present treatment is therefore:

- preserve the MVP as an engineering prototype;
- collect honest mechanical, power, repeatability and tactile evidence;
- do not file on the baseline architecture as such;
- do not describe it as patented, patent pending, novel or inventive;
- do not infer FTO from a different actuator, low price or an expired/abandoned database label; and
- consider future patent development only around a specifically enabled physical mechanism that survives the gates in this chapter.

## 05.3 Research-lane integrity and limitations

Six lanes are evidence sources, not votes.

| Lane | Permitted use | Material limitation |
|---|---|---|
| ChatGPT Deep Research | Strong patent/publication leads, claim comparisons and experiment framing | Some status and current-signature conclusions need verification |
| Gemini | Search leads and experiment ideas | Several record/family/status descriptions unreliable; positive conclusions downgraded |
| Perplexity — partial | Completed material only | No complete verdict; missing conclusions cannot be reconstructed |
| Qwen | Limited independently supported prompts | Concept contamination and unreliable family/status reasoning in parts |
| Mistral | Conventionality warnings and possible tests | Shallow primary-claim support; status/FTO claims not controlling |
| Microsoft Copilot | High-level calibration/testing prompts | Weak traceability and false/unsupported relationships in material places |

The failed moving-roller/encoder-wheel/RAMPS/Mega synthesis is excluded. The dossier’s DOCX and PDF are one source in two formats. Controlled conclusions depend on audited evidence, not model agreement.

## 05.4 Valid synthesis conclusions and disagreement

The two valid OpenBraille patent syntheses agree on the main present position:

- the frozen MVP alone is not a credible filing target;
- mechanical stops, calibration, sequencing, modularity, printed guides and current monitoring are individually known or predictable;
- the official file and current legal effect of Indian application `5559/CHE/2014` remain unresolved;
- the generic actuator-current, position and anomaly field was not searched to complete professional claim-language depth;
- no OpenBraille experiment demonstrates a non-additive interaction; and
- institutional IPR review and a refreshed primary-source search are mandatory before any filing decision.

They disagree on the classification of D11 before physical evidence exists.

| Valid synthesis | Current classification | Treatment of D11 | Controlled interpretation |
|---|---|---|---|
| Work Max | Track D; no credible patent path established, moderate confidence | D11 is the least-weak experiment but remains Track D until physical-state, ablation, transfer, practical-scale and search gates pass | Controls the conservative current statement because it does not turn an unsearched exact combination into a positive case |
| Valid Secondary / Standard High | Conditional Track B, moderate-low confidence | Allows the integrated mechanism to advance as a bounded candidate if it demonstrates a material physical-control effect | Preserved as a legitimate research hypothesis, not as consensus, filing authority or proof |

The reconciled result is not an average. D11 may be worth a bounded post-MVP experiment, but the current status remains experimental and no-filing. The phrase **advance conditionally** means that engineering research may be authorized under strict controls; it does not mean patentability is established or that a filing should be prepared.

The disagreement is useful because it defines the evidence burden. A permissive interpretation asks whether integration might produce a technical effect. The conservative interpretation asks whether the mechanism can first show direct physical truth, non-additive benefit, transfer and useful scope. Part II adopts the conservative current state while preserving the experiment as an open research question.

## 05.5 Cross-concept adjudication context

Both final cross-concept adjudications support VibeGuard as the strongest semester-build candidate. They disagree on the best later patent-development path.

- The Work Max adjudication favors TrueMoist after a VibeGuard signal-and-access gate and deprioritizes OpenBraille unless later D11-type evidence passes.
- The Deep Research High adjudication identifies conditional OpenBraille D11 as the best post-MVP candidate and proposes a short physical-state-observability gate, with VibeGuard as fallback.

These adjudications use different strategic models. They are decision context, not votes. Neither proves teacher approval, patentability or a project-wide patent winner. No higher-authority record chooses one patent-first gate.

The later OpenBraille pre-build simulation is narrower. It stress-tests the OpenBraille patent case and treats the broad D11 bundle as an aggregation on current evidence. It then selects VPD-C7 as the best hypothesis for redesign and testing within that simulation. This does not override the unresolved cross-concept decision. It means only that, if OpenBraille future research is authorized, the simulation considers direct pin-side endpoint evidence a more coherent technical question than current-led state inference.

The manual must therefore preserve three distinct decisions:

1. which concept, if any, is authorized for the semester build;
2. which short patent-first evidence gate, if any, is authorized after or alongside the semester programme; and
3. whether a mechanism that passes an experiment should proceed to institutional file/no-file evaluation.

None is proved complete in the attached record.

## 05.6 D11 research hypothesis

### Proposed mechanism

D11 is an earlier proposed **mechanically referenced, individually calibrated, sensor-minimal tactile-state verification and bounded-recovery architecture** using the six servo/cam/pin channels. Its prospective relationship combines: upper/lower mechanical datums; per-channel reliable command windows; isolated shared current/voltage observation; independent displacement/force labels; `COMPLETED`, incomplete/jammed or `UNKNOWN` states; at most one qualified low-energy retry followed by isolation; supply-aware sequencing; and recalibration after replacement, remount or drift.

D11 asks whether these familiar controls create a reproducible non-additive physical advantage. A command or current spike may never be treated as proof of tactile state.

### Relationship to the MVP

D11 is outside the frozen semester cell. It retains the actuator channels but adds datum, instrumentation, labelled state logic and recovery experiments. Ordinary per-dot calibration remains routine engineering unless a specifically defined integrated relationship is tested in a separate configuration after the MVP gates.

### Required evidence, baselines and ablations

Required evidence includes direct displacement and preferably force ground truth; labelled normal, incomplete, jam and ambiguous events; held-out data; multiple units/rebuilds; voltage, temperature, load, friction, contamination and wear variation; retry safety; practical-scale evidence; current prior-art search; and institutional IPR review.

Baselines must include fixed PWM, calibrated open loop, datum-only, calibration-only, current-only, fixed sequencing and a direct-sensor oracle. Ablation must remove each claimed indispensable element. The proposed 3,000-transition, zero-silent-wrong-state gate is a research threshold, not an achieved or automatically approved requirement.

### Failure conditions and current status

D11 fails as a patent direction if current reveals only generic effort, a current-only rule silently accepts a wrong state, the full system equals the best partial baseline, thresholds require ad hoc retuning, replacement/reassembly or practical-scale transfer fails, retry is unsafe, closer art is found or useful scope collapses to exact hobby parts.

No D11 hardware, datum, waveform dataset, classifier, ablation, replacement trial, practical-scale coupon or held-out result is attached. No cooperative effect, novelty, inventive step, eligibility, useful scope or FTO is established.

## 05.7 VPD-C7 research hypothesis

### Proposed pin-side datum mechanism

VPD-C7 is a later, separate **Verified Pin-Datum Cell** hypothesis for a post-MVP guide/pin coupon. It asks whether the same pin-side datum that sets an endpoint can also provide direct, low-energy endpoint evidence with less registration error and fewer silent wrong states than a passive stop plus separately mounted sensor.

The proposed coupon uses registered upper/lower endpoint features; a low-energy pin-side event that does not carry servo power; external displacement/force as the oracle; current/voltage only for effort, overload or supply disturbance; endpoint declaration only from qualified pin-side evidence; `UNKNOWN` for absent/conflicting evidence; bounded recovery; and the existing servo/cam/pin actuation. The simulation’s twelve contacts plus one shared current channel are planning architecture, not a mandate or claim.

### Relationship to the MVP

VPD-C7 changes the guide/pin/datum relationship and adds endpoint evidence. It therefore requires separate configuration, budget, folder and disclosure status. Work should begin with one coupon; C7 results may not be represented as frozen-cell results.

### Required evidence and baselines

Required comparisons are passive datum only, calibrated open loop, passive datum plus separate direct sensor, contact without current, current without contact and full C7. Measurements must cover registration error, force, friction, bounce, contact resistance, debounce, false endpoints, energy, practical-scale packing, wear, debris/cleaning, blind replacement and independent reassembly. A locked held-out run must expose silent errors, and current must be removed if it adds no independent diagnostic value.

The decisive baseline is the passive stop plus separate sensor. A dual-purpose datum/contact must provide a measurable physical advantage without unacceptable friction, bounce, wear, contamination or manufacturing cost.

### Failure conditions and current status

C7 fails if it is equivalent or worse than a separate sensor, cannot fit practical geometry, fails lifecycle or transfer, accepts a silent wrong state, depends on current for endpoint certification, is defeated by closer art or has only trivial hobby-part scope.

No C7 datum/contact has been built. Stops and switches are familiar, creating strong obviousness risk. No registration, silent-error, scale, lifecycle, novelty, inventive-step, useful-scope or FTO result exists.

## 05.8 Relationship between D11 and VPD-C7

| Dimension | D11 | VPD-C7 |
|---|---|---|
| Origin | Two valid syntheses | Later pre-build stress test |
| State link | Datum, calibration and shared current/voltage; physical truth remains difficult | Datum itself is intended to provide pin-side endpoint evidence |
| Current role | Possible diagnostic input, never sufficient alone | Effort/overload/supply evidence only |
| Configuration | Post-MVP overlay/research build | Separate guide/pin/datum coupon |
| Main test | Cooperation, observability and transfer | Advantage over passive stop plus separate sensor |
| Current status | Track D or conditional early exploration | Redesign-before-testing hypothesis |

D11 is the earlier integrated verification hypothesis. VPD-C7 is a later, separate pin-datum redesign intended to address D11’s weak physical-state link. D11 configurations may be baselines for C7, but the mechanisms must not be merged or described as one invention. Either may fail and leave only conventional engineering value.

## 05.9 Pre-build simulation boundary

> **PRE-BUILD SIMULATION CAUTION**
>
> The OpenBraille pre-build future patent-case simulation is conditional planning evidence. It did not build hardware, observe a physical effect, conduct a legal opinion, establish novelty or predict patent grant.
>
> It supports only the following management boundaries:
>
> - build and assess the ordinary macro six-servo MVP first;
> - preserve active retraction unless passive return is proved;
> - develop VPD-C7 only on a separate post-MVP coupon;
> - use external physical ground truth;
> - never let current alone certify pin height or completion;
> - preserve `UNKNOWN` for absent or conflicting evidence;
> - compare against strong baselines and ablations;
> - stop when kill criteria are met;
> - protect future CAD, circuits, thresholds and data until IPR review; and
> - do not substitute another OpenBraille architecture.

The simulation’s scenario labels, rough incremental hardware allowance and twelve-month research sequence are planning tools. They are not probabilities of grant, spending approval or a direction to compress future work into the semester. The simulation may prioritize VPD-C7 for redesign/testing inside its own analysis, but this is not project or institutional authorization.

## 05.10 Experimental evidence roadmap

Future research proceeds only through evidence gates:

1. **MVP truth baseline:** versioned one-dot and six-dot travel, power/reset, 100-cycle repeatability, ≥1,000-actuation wear screen and honest tactile record. MVP failure leads to engineering learning, not forced patent work.
2. **Datum/calibration:** compare frozen geometry, datum-only, calibration-only and combined configurations across rebuilds.
3. **Current observability:** collect labelled events with direct displacement oracle across units, voltage, load, temperature, friction and wear; prohibit current-only completion.
4. **D11 cooperation:** compare the full configuration with the best partials using preregistered interaction and kill rules.
5. **VPD-C7 coupon:** measure registration, force, friction, bounce, contact behavior and silent error against a passive stop plus separate sensor.
6. **Practical-scale/lifecycle:** test smaller coupons, packing, wear, dust/fibre, cleaning and contact degradation.
7. **Replacement/reassembly:** use blind component swaps and independent rebuilds to expose hidden tuning.
8. **Locked silent-error gate:** freeze oracle, thresholds, `UNKNOWN` handling and stop rule; any silently accepted wrong tactile state requires genuine redesign.
9. **Search/IPR/FTO:** only after enablement, retrieve the official Indian file, refresh worldwide claims/NPL, document human contribution and conduct ownership, disclosure and FTO review.

| Programme | Strong baseline | Positive gate | Kill/hold outcome |
|---|---|---|---|
| MVP | Fixed PWM plus external measurement | Safe repeatable one/six-dot evidence | Preserve learning; no patent rescue |
| D11 datum/calibration | Datum-only and calibration-only | Transferable reduction in scatter/stall | Routine tuning → no patent lead |
| D11 current | Command/time/voltage and direct oracle | Held-out multi-unit diagnostic value | Ambiguous/silent error → remove current |
| D11 cooperation | Best partial configurations | Non-additive improvement and transfer | Equality with partial → aggregation |
| VPD-C7 | Passive stop plus separate sensor | Better registration/truth without burden | Equivalent/worse → end thesis |
| Practical scale | Macro and smaller coupons | Reproducible practical geometry | Macro-only → no broad claim |
| Lifecycle/transfer | Clean/new and original tuned build | Stable wear, contamination and rebuild results | False endpoint or transfer failure → redesign/kill |
| Search/IPR | Final enabled disclosure | Useful scope after official search/FTO/ownership review | Closer art or unacceptable risk → no filing |

Motion videos, model agreement, low BOM or generic classifier accuracy do not substitute for these gates.

## 05.11 Prior-art and legal-status limitations

The attached patent record remains materially incomplete in several areas.

1. The official specification, claims, prosecution history, descendants, ownership and current legal effect of Indian application `5559/CHE/2014` were not obtained.
2. Official current status was not established for every cited US, EP or national right. Historical database labels are leads, not legal conclusions.
3. The generic actuator-current, position, anomaly-detection and motor-control field was not exhaustively searched at professional claim-language depth.
4. Hidden, non-English, differently classified or later-published references may contain closer combinations.
5. A mechanism that has not been physically enabled cannot support a positive novelty or inventive-step case.
6. Macro-scale evidence cannot enable broad standard-scale mechanical claims.
7. Patentability and FTO are different. An old or expired disclosure can destroy novelty while posing no current claim risk; a live narrow claim can create FTO risk even when a broad concept is old.
8. Jurisdictional eligibility rules differ, especially for software-only calibration, scheduling or classification language.
9. Filing, publication or student construction does not create freedom to operate.
10. The project must not assume that experimental use in India is exempt from infringement without qualified advice.

The manual may identify cited publications as research leads and explain why the field appears crowded. It must not declare a right live, expired, abandoned, irrelevant or non-infringed without official current verification.

## 05.12 Freedom-to-operate boundary

Freedom to operate concerns whether the actual acts of making, using, supplying, selling or importing the final design in particular territories could fall within enforceable claims. It is distinct from whether the team might obtain a patent on an improvement.

No FTO clearance exists for the frozen MVP, D11 or VPD-C7. A meaningful review requires:

- the final geometry, materials, electronics and firmware behavior;
- intended suppliers and manufacturing route;
- intended countries and commercial acts;
- official current legal status and prosecution histories;
- claim charts addressing literal scope and relevant equivalents; and
- documented design-around decisions.

Differences such as using a servo rather than an electromagnetic actuator do not automatically avoid claims. An expired publication may still be prior art. A patent filing by the project would not neutralize third-party rights. Academic publication or defensive publication would not create FTO.

Until counsel-led review is complete, the correct statements are **FTO not assessed** and **no non-infringement conclusion**. The semester team may build only under the institution’s approved educational rules and should not make a commercialization claim from the current record.

## 05.13 Confidentiality, contribution and institutional IPR control

The public-safe semester baseline may include the macro six-dot architecture, six SG90-class servos, cams, guided pins, ESP32 direct PWM, external power, general historical budget, approved build results and honest limitations, subject to course and institutional rules.

The following should remain confidential until institutional IPR review if future research proceeds:

- exact D11 datum/guide geometry;
- calibration procedure and stored operating windows asserted as part of a future mechanism;
- current/voltage waveform definitions, features, thresholds and transfer results;
- retry, derating, isolation and fault-state logic proposed as indispensable;
- exact VPD-C7 contact/datum geometry, materials, dimensions, circuitry, protection and debounce;
- comparative results against passive stops, separate sensors and current-only inference;
- replacement/reassembly, wear, contamination and held-out silent-error data;
- claim-to-experiment maps and draft claim language; and
- contribution, inventorship and disclosure chronology.

Human conception and contribution records should begin before future-mechanism work. Records should identify who conceived each technical feature, who designed the experiment, who created CAD or firmware and who reduced the mechanism to practice. AI/model assistance is not inventorship and must not replace dated human contribution evidence.

Before publishing code, CAD, videos, posters, papers, competition entries or details of D11/VPD-C7, the team should obtain the institution’s IPR and disclosure decision. The project must not rely on an assumed grace period. If the patent route is killed, the institution may later choose academic publication, defensive publication or confidential know-how after appropriate review.

## 05.14 File/no-file decision gate

The present decision is **no filing commitment**. A later counsel-led file/no-file evaluation may be opened only when all of the following are satisfied.

| Gate | Required condition | Evidence needed |
|---|---|---|
| Engineering baseline | Frozen MVP succeeds without architecture substitution | Versioned one-dot and six-dot mechanical, power, firmware and tactile evidence |
| Enabled mechanism | One specifically defined D11 or VPD-C7 configuration is actually built | Complete dimensions, materials, circuitry, firmware/state chart and test setup |
| Physical effect | Mechanism produces a preregistered reproducible advantage | Direct displacement/force ground truth and comparison with strong baselines |
| Ablation | Every asserted indispensable feature contributes materially | Controlled removal studies and interaction analysis |
| Transfer | Effect survives component replacement, independent reassembly and ordinary variation | Blind swaps, rebuilds, environmental and practical-scale results |
| Truthfulness | No locked test silently accepts an incorrect tactile state | Held-out dataset with explicit `UNKNOWN`/isolation outcomes |
| Prior-art status | Official close-prior-art file and current worldwide search are resolved | Official register documents, professional claim-language search and NPL review |
| FTO | Actual design and intended territories are reviewed | Counsel-led claim chart and design-around analysis |
| Ownership/inventorship | Human contribution, ownership and disclosure records are complete | Dated contribution log and institutional determination |
| Institutional value decision | Expected useful scope justifies cost and disclosure risk | IPR cell/counsel recommendation and authorized budget decision |

Failure at the evidence gate should normally produce one of three outcomes: retain the work as a strong semester prototype, convert it into a rigorous engineering/publication study, or close/reduce patent priority. It must not produce a weak filing merely to preserve the original aspiration.

Even if every gate passes, the correct statement is **eligible for counsel-led file/no-file evaluation**. It is not **patentable**, **approved for filing** or **likely to be granted**.

## 05.15 Current patent-development state

The baseline MVP is closed as a present filing target and remains valuable engineering work. No D11 or VPD-C7 experiment is authorized or proved started; no direct ground-truth rig, baseline suite, dataset, contact coupon, practical-scale evidence, transfer trial or silent-error gate is attached. The official Indian file, current worldwide search, legal status, FTO, adjudication gate and institutional confidentiality/ownership rules remain unresolved.

The route must be allowed to fail. Non-informative current should be removed; a C7 datum equivalent to a separate sensor should be closed; macro-only or non-transferable results should not support broad claims; closer art or trivial scope should lead to no filing. The current decision remains no filing commitment.

## 05.16 Chapter conclusion

The macro six-servo MVP is not established as a credible patent target. D11 is an earlier integrated verification hypothesis; VPD-C7 is a later separate pin-datum redesign. Neither is implemented, proved cooperative, novel or part of the semester cell.

Future work requires direct ground truth, strong baselines, ablation, practical-scale and lifecycle evidence, replacement/reassembly and a locked silent-error gate. Only a final enabled mechanism that survives current prior-art, FTO, confidentiality, ownership and institutional review may become eligible for professional file/no-file evaluation. The current state is no filing commitment.

## 05.S Source notes

The material conclusions in Chapter 05 rely on the following original organized-workspace paths. Raw research lanes are supporting leads only; the packet and manifest are not original patent evidence.

### TIER_2 — Valid syntheses, simulation and controlled reference sources

- `03_CONCEPT_PORTFOLIO/OpenBraille/03_Patent_Synthesis/01_OpenBraille_Patent_Synthesis_Work_Max.md` — conservative Track D conclusion, evidence audit, D11 definition, research gates and unresolved legal/search limits.
- `03_CONCEPT_PORTFOLIO/OpenBraille/03_Patent_Synthesis/02_OpenBraille_Patent_Synthesis_Valid_Secondary.md` — conditional Track B interpretation and integrated-mechanism hypothesis; not proof or filing authority.
- `03_CONCEPT_PORTFOLIO/OpenBraille/04_PreBuild_Simulation/OpenBraille_PreBuild_Future_Patent_Case_Simulation.md` — later stress test, D11 aggregation attack, VPD-C7 redesign hypothesis, baseline/ablation roadmap and simulation boundaries.
- `03_CONCEPT_PORTFOLIO/OpenBraille/05_Roadmaps_and_Reference_Dossiers/OpenBraille_Semester_Architecture_and_Future_Research_Reference_Dossier.docx` — controlled separation of semester/public work and confidential future research, non-claim mechanism descriptions and practical management rules.
- `03_CONCEPT_PORTFOLIO/OpenBraille/05_Roadmaps_and_Reference_Dossiers/OpenBraille_Semester_Architecture_and_Future_Research_Reference_Dossier.pdf` — duplicate publication format; not independent corroboration.
- `03_CONCEPT_PORTFOLIO/OpenBraille/05_Roadmaps_and_Reference_Dossiers/HISTORICAL_Phase1C_OpenBraille_Concept_Dossier.docx` — historical concept origin only; not current architecture or patent authority.
- `03_CONCEPT_PORTFOLIO/OpenBraille/PATENT_EVIDENCE_INDEX.md` — controlled lane/synthesis identity and exclusion record.
- `04_COMPARATIVE_DECISION/02_Final_Adjudications/01_Project_mC_Final_Adjudication_Work_Max.md` — cross-concept context, not vote or approval.
- `04_COMPARATIVE_DECISION/02_Final_Adjudications/02_Project_mC_Final_Adjudication_Deep_Research_High.md` — cross-concept context, not vote or approval.
- `04_COMPARATIVE_DECISION/COMPARATIVE_DECISION_INDEX.md` — treatment rule for adjudications.

### TIER_3 — Controlled raw research lanes

- `03_CONCEPT_PORTFOLIO/OpenBraille/02_Raw_Research/01_OpenBraille_Patent_Research_ChatGPT_Deep_Research.md`
- `03_CONCEPT_PORTFOLIO/OpenBraille/02_Raw_Research/02_OpenBraille_Patent_Research_Gemini.docx`
- `03_CONCEPT_PORTFOLIO/OpenBraille/02_Raw_Research/03_OpenBraille_Patent_Research_Perplexity_PARTIAL.docx`
- `03_CONCEPT_PORTFOLIO/OpenBraille/02_Raw_Research/04_OpenBraille_Patent_Research_Qwen.md`
- `03_CONCEPT_PORTFOLIO/OpenBraille/02_Raw_Research/05_OpenBraille_Patent_Research_Mistral.md`
- `03_CONCEPT_PORTFOLIO/OpenBraille/02_Raw_Research/06_OpenBraille_Patent_Research_Microsoft_Copilot.docx`

These lanes are evidence sources rather than votes. The Perplexity lane is partial. The separate moving-roller/encoder-wheel/RAMPS/Mega synthesis is invalid and excluded.

# Part II Open-Decision Register

| ID | Decision or uncertainty | Current status | Required next action |
|---|---|---|---|
| OB-OD01 | Semester concept and ESP32 acceptance | Open; VibeGuard recommended and shift not proved approved | Obtain explicit teacher/project concept and platform decision |
| OB-OD02 | Phase 4 and procurement | Not proved started or frozen | Complete authorization, current verification, budget and ownership record |
| OB-OD03 | FDM and measurement access | Assumed | Confirm printer, material, operator, tools and schedule |
| OB-OD04 | One-dot mechanics and passive return | No result; passive return unproved | Build/version coupon and retain active retraction until loaded evidence passes |
| OB-OD05 | Cam/guide and servo operating windows | Provisional/unmeasured | Print tolerance matrix and establish safe measured upper/lower bands |
| OB-OD06 | Power and grounding | 2 A/3 A planning only | Validate exact wiring, no back-feed, rail droop/current, resets and heating |
| OB-OD07 | Six-dot integration and mapping set | Not tested/frozen | Run interference/power tests and freeze unit-tested patterns |
| OB-OD08 | Repeatability and lifecycle | Proposed thresholds only | Preregister 100-cycle method and ≥1,000-actuation screen |
| OB-OD09 | Tactile and safety protocol | Open blocker | Obtain approved participant, consent, randomization, guards and stop rules |
| OB-OD10 | Current BOM/prices | Historical planning evidence | Verify exact specifications, suppliers, availability and invoices |
| OB-OD11 | Team role ownership | Proposed only | Assign named primary and backup owners after authorization |
| OB-OD12 | Patent-first adjudication gate | Unresolved | Authorize one gate, define replacement rule or defer |
| OB-OD13 | D11 authorization and evidence | Not authorized/started | Decide after MVP baseline; build oracle, baselines and preregistered tests |
| OB-OD14 | VPD-C7 authorization and evidence | Not authorized/started | Create separate configuration, budget, confidentiality and coupon plan if pursued |
| OB-OD15 | Official `5559/CHE/2014` file and legal status | Not obtained/verified | Retrieve official file and check relevant official registers |
| OB-OD16 | Current worldwide search and FTO | Incomplete/not assessed | Search final enabled mechanism and commission target-country claim review |
| OB-OD17 | Practical-scale and transfer evidence | Absent | Build smaller coupons; conduct blind replacement and independent rebuilds |
| OB-OD18 | Locked silent-error gate | Not run | Freeze oracle, thresholds, `UNKNOWN` handling and kill rule |
| OB-OD19 | Confidentiality, ownership and contribution record | Required, not documented | Separate public/private work and obtain institutional IPR rules |
| OB-OD20 | File/no-file decision | No positive gate passed; no commitment | Revisit only after technical, search, FTO and ownership gates |

# Part II Contradiction Summary

| ID | Chapter | Issue | Controlling resolution | Residual uncertainty |
|---|---:|---|---|---|
| OB-C01 | 04 | Passive reset versus active retraction | Active command controls unless coupled return is physically proved | Passive assistance may exist but is untested |
| OB-C02 | 04–05 | Command/current versus physical state | Direct external or qualified pin-side evidence controls | Current’s independent diagnostic value is unknown |
| OB-C03 | 04 | 2 A versus 3 A supply | External regulated power with measured headroom; figures are provisional | Exact current depends on parts/sequence |
| OB-C04 | 04 | Multiple BOM totals | All are dated planning layers, not current totals | Current prices and printing cost unverified |
| OB-C05 | 04 | “Ready for Phase 4” versus approval open | Architecture is frozen; implementation authorization is not proved | Teacher/platform decision missing |
| OB-C06 | 04 | Precise dimensions/ISO language | Values are provisional non-standard targets | Final geometry and tactile threshold experimental |
| OB-C07 | 04 | Fallback boards/actuators | Any substitution requires authorization and revalidation | Availability and course acceptance open |
| OB-C08 | 04–05 | MVP refinements versus future mechanism | Ordinary calibration/tolerance/logging remain MVP work; D11/C7 are separate | Repository/configuration boundary must be enforced |
| OB-C09 | 05 | MVP aspiration versus evidence | Baseline is not a credible current patent target | No positive patent case exists |
| OB-C10 | 05 | Track D versus conditional Track B | Preserve synthesis disagreement; current status is experimental/no-filing | Future data/search may reclassify |
| OB-C11 | 05 | D11 cooperation versus aggregation | No cooperation demonstrated; use as hypothesis/ablation programme | Interaction data absent |
| OB-C12 | 05 | D11 versus VPD-C7 | Historically related, technically separate | Useful feature subset unknown |
| OB-C13 | 05 | Adjudication or simulation as approval | They are context/planning, not votes or authorization | Patent-first gate unselected |
| OB-C14 | 05 | Raw-lane legal-status claims | Audited synthesis treatment controls; raw lanes are leads | Official status unresolved |
| OB-C15 | 05 | Macro evidence supporting broad claims | Practical-scale evidence is mandatory | No practical-scale coupon |
| OB-C16 | 05 | “Advance conditionally” as filing language | Bounded research only; no filing commitment | Search, FTO, ownership and evidence open |
| OB-C17 | 04–05 | Successful prototype versus patent evidence | Engineering success and patent case are separate | Future work may remain conventional |
| OB-C18 | 04–05 | Public MVP versus confidential research | Separate configurations, access/disclosure and contribution records | Institutional IPR process not attached |

# Part II Source Ledger

The following original organized-workspace paths were materially relied upon. They are grouped by chapter and authority tier. The attachment manifest is excluded because it is file control only. The validated reconciliation controls resolved wording but is not substituted for the original evidence paths below.

## Chapter 04 — TIER_1 current architecture and project authority

- `03_CONCEPT_PORTFOLIO/OpenBraille/01_Final_Architecture/Phase3C_OpenBraille_Architecture_Report_Final.md`
- `03_CONCEPT_PORTFOLIO/OpenBraille/01_Final_Architecture/Phase3C_OpenBraille_Memory_Final.md`
- `03_CONCEPT_PORTFOLIO/OpenBraille/01_Final_Architecture/Phase3C_OpenBraille_SOP_Final.md`
- `01_GOVERNANCE_AND_CONTROL/02_Decision_Registers/Project_mC_Decision_Register_v1.2.md`
- `01_GOVERNANCE_AND_CONTROL/01_Project_Requirements/Teacher_Project_Requirements_and_Change_Context.md`

## Chapter 04 — TIER_2 supporting status and evidence

- `03_CONCEPT_PORTFOLIO/OpenBraille/PATENT_EVIDENCE_INDEX.md`
- `03_CONCEPT_PORTFOLIO/OpenBraille/README.md`
- `03_CONCEPT_PORTFOLIO/OpenBraille/05_Roadmaps_and_Reference_Dossiers/OpenBraille_Semester_Architecture_and_Future_Research_Reference_Dossier.docx`
- `03_CONCEPT_PORTFOLIO/OpenBraille/05_Roadmaps_and_Reference_Dossiers/OpenBraille_Semester_Architecture_and_Future_Research_Reference_Dossier.pdf` — duplicate publication format of the same controlled dossier; not independent corroboration
- `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/05_Uncertainty_and_Test_Register.md`
- `04_COMPARATIVE_DECISION/02_Final_Adjudications/01_Project_mC_Final_Adjudication_Work_Max.md`
- `04_COMPARATIVE_DECISION/02_Final_Adjudications/02_Project_mC_Final_Adjudication_Deep_Research_High.md`
- `04_COMPARATIVE_DECISION/COMPARATIVE_DECISION_INDEX.md`

## Chapter 05 — TIER_2 valid synthesis, simulation and controlled reference sources

- `03_CONCEPT_PORTFOLIO/OpenBraille/03_Patent_Synthesis/01_OpenBraille_Patent_Synthesis_Work_Max.md`
- `03_CONCEPT_PORTFOLIO/OpenBraille/03_Patent_Synthesis/02_OpenBraille_Patent_Synthesis_Valid_Secondary.md`
- `03_CONCEPT_PORTFOLIO/OpenBraille/04_PreBuild_Simulation/OpenBraille_PreBuild_Future_Patent_Case_Simulation.md`
- `03_CONCEPT_PORTFOLIO/OpenBraille/05_Roadmaps_and_Reference_Dossiers/HISTORICAL_Phase1C_OpenBraille_Concept_Dossier.docx` — historical origin only; not current architecture or patent authority
- `03_CONCEPT_PORTFOLIO/OpenBraille/05_Roadmaps_and_Reference_Dossiers/OpenBraille_Semester_Architecture_and_Future_Research_Reference_Dossier.docx`
- `03_CONCEPT_PORTFOLIO/OpenBraille/05_Roadmaps_and_Reference_Dossiers/OpenBraille_Semester_Architecture_and_Future_Research_Reference_Dossier.pdf` — duplicate publication format; not independent corroboration
- `03_CONCEPT_PORTFOLIO/OpenBraille/PATENT_EVIDENCE_INDEX.md`
- `04_COMPARATIVE_DECISION/02_Final_Adjudications/01_Project_mC_Final_Adjudication_Work_Max.md`
- `04_COMPARATIVE_DECISION/02_Final_Adjudications/02_Project_mC_Final_Adjudication_Deep_Research_High.md`
- `04_COMPARATIVE_DECISION/COMPARATIVE_DECISION_INDEX.md`

## Chapter 05 — TIER_3 controlled raw research lanes

- `03_CONCEPT_PORTFOLIO/OpenBraille/02_Raw_Research/01_OpenBraille_Patent_Research_ChatGPT_Deep_Research.md`
- `03_CONCEPT_PORTFOLIO/OpenBraille/02_Raw_Research/02_OpenBraille_Patent_Research_Gemini.docx`
- `03_CONCEPT_PORTFOLIO/OpenBraille/02_Raw_Research/03_OpenBraille_Patent_Research_Perplexity_PARTIAL.docx`
- `03_CONCEPT_PORTFOLIO/OpenBraille/02_Raw_Research/04_OpenBraille_Patent_Research_Qwen.md`
- `03_CONCEPT_PORTFOLIO/OpenBraille/02_Raw_Research/05_OpenBraille_Patent_Research_Mistral.md`
- `03_CONCEPT_PORTFOLIO/OpenBraille/02_Raw_Research/06_OpenBraille_Patent_Research_Microsoft_Copilot.docx`

## Explicit exclusions and non-evidence controls

- The failed moving-roller/encoder-wheel/RAMPS/Mega concept-swapped OpenBraille synthesis is excluded and was not attached.
- The attachment manifest is file control only and is not technical or patent evidence.
- The validated Master Manual Part I controls terminology and current project status; it does not replace the original sources above.
- Independent research lanes and syntheses are evidence sources, not votes.
- No prior-chat context, memory, web research, current pricing, fresh patent searching or unstated assumption was used in this drafting stage.

<!-- END CONTROLLED COMPONENT: PART_II -->

---

<!-- BEGIN CONTROLLED COMPONENT: PART_III -->
<!-- SOURCE PATH: /home/paradoxpete/Documents/PROJECT_ORGANIZED/08_MASTER_MANUAL/03_Drafting_Workspace/01_Validated_Parts/Part_III/Project_mC_Master_Manual_Part_III_VibeGuard_Architecture_and_Patent_Path.md -->
<!-- SOURCE SHA-256: 902e8a67aa119aaf446d0fbc194ce20ff3d5abc9e1f77c991fff8b233abca180 -->

## Part III — VibeGuard Architecture and Patent Research Path

## Document control

| Field | Value |
|---|---|
| Document | Project mC Master Manual — Part III |
| Controlled filename | `Project_mC_Master_Manual_Part_III_VibeGuard_Architecture_and_Patent_Path.md` |
| Status | Controlled draft |
| Scope | Chapters 06 and 07, followed by Part III registers and source ledger |
| Source boundary | Only the ten attachments in the controlled Part III package |
| Input inventory | Exactly ten physical attachments were readable. The nine externally hash-controlled inputs matched the manifest; the self-referential manifest was used only for file control. Upload suffixes did not create additional logical sources. |
| Implementation status | Not an implementation, Phase 4 or procurement authorization |
| Approval status | Not a teacher-approval record; concept and course-platform acceptance remain unresolved |
| Patent status | No patentability, filing, infringement or FTO conclusion |
| External verification | No fresh web, manufacturer, market, patent-register or legal-status work was performed |
| Relationship to Part I | Part I controls the current decision: VibeGuard is the strongest semester-build recommendation, but the shift, platform, Phase 4 and procurement are not proved approved; retained concepts remain legitimate; no MVP is established as patentable; the adjudications disagree on the future patent gate |
| Relationship to Part II | Style and cross-concept consistency reference only; not VibeGuard evidence |

The drafting package was complete. The validated VibeGuard reconciliation controls resolved wording and contradictions; the Chapter 06 and 07 packets preserve underlying evidence and original source paths. No prior-chat context, memory, web research or unstated assumption was used.

## How to read Part III

Part III preserves five boundaries.

**Architecture versus refinement.** The locked design is one rigid ADXL345-class sensor, one ESP32-class controller, SPI, a controlled rotating rig, RMS plus persistence, supporting FFT/bands, optional ordinary Mahalanobis, RGB, USB and fixed configuration records. Conventional tuning may refine this design; a different concept requires change control.

**Level 1 versus Level 2.** Chapter 06 covers controlled normal-versus-induced-abnormal detection. Chapter 07 covers later target attribution under interference, remounting and operating change. Level-1 success does not prove Level-2 observability.

**Detection versus attribution.** A classifier may detect a controlled state change without identifying which physical source caused it.

**Targets versus results.** Rates, windows, thresholds, performance figures and session counts are proposals unless approved or measured.

**Patent evidence versus filing.** The ordinary stack is not established as patentable. Future mechanisms remain hypotheses requiring experiments, current primary-source review and institutional IPR control.

# Chapter 06 — VibeGuard Frozen Architecture and Semester Scope

## 06.1 Chapter purpose

This chapter defines the controlled VibeGuard semester architecture, the boundaries within which implementation may proceed after authorization, and the evidence required before the team may make performance claims. It is an engineering reference, not permission to purchase components, enter Phase 4 or represent the project as teacher-approved.

VibeGuard asks a deliberately bounded semester question: can a student team use one low-cost target-mounted accelerometer and one ESP32-class controller to acquire reliable vibration data, establish a normal baseline, detect a safe and repeatable induced abnormal state through local lightweight analysis, and preserve enough configuration-controlled evidence for another person to reproduce and audit the result? This is an embedded measurement and controlled-classification problem. It is not a complete industrial predictive-maintenance product and does not promise diagnosis of a particular bearing defect, universal thresholds, remaining-useful-life estimation, automatic maintenance action or source attribution in a dense machine environment.

The architecture was selected because it offers a clear division between hardware, firmware, signal processing, validation and presentation work. Its apparent simplicity must not be mistaken for triviality. A vibration result can be invalidated by counterfeit or unsuitable sensor hardware, soft mounting, unstable sampling, hidden data loss, an unsafe or drifting abnormality fixture, leakage between calibration and test data, or post-hoc threshold tuning. The value of the semester project therefore lies as much in disciplined evidence control as in the live red/green demonstration.

## 06.2 Current architecture identity

> **VIBEGUARD ARCHITECTURE LOCK**
>
> For the frozen semester architecture, **VibeGuard means only**:
>
> - one rigidly mounted ADXL345-class tri-axis accelerometer;
> - one ESP32-class controller, with the exact board variant subject to course approval and purchased-board verification;
> - SPI acquisition from the accelerometer;
> - one controlled low-voltage motor, fan or comparable rotating test article;
> - repeatable normal and deliberately induced, safe abnormal operating states;
> - continuous or windowed time-domain features;
> - RMS plus persistence as the mandatory minimum classifier;
> - triggered or scheduled FFT and selected frequency bands as supporting evidence;
> - optional ordinary Mahalanobis comparison only after the baseline and acquisition-integrity gates pass;
> - local RGB state indication;
> - USB serial logging and exportable evidence; and
> - fixed records for the sensor, mounting, orientation, sampling configuration, firmware, rig and test session.
>
> This is a passive Level-1 monitoring and alerting demonstrator. It is **not** active vibration cancellation, software-security scanning, cloud monitoring, a permanent sensor array, fleet management, remaining-useful-life prediction, automatic maintenance decision-making, industrial certification, demonstrated bearing diagnosis, dense-machine source attribution, automatic adaptive learning or PIRG.

The identity lock prevents three kinds of drift. First, it prevents earlier or failed concept substitutions from re-entering the semester design. Software-security or configuration scanning may be cybersecurity work, but it is not the frozen VibeGuard concept. Second, it prevents optional analytical features from becoming new architecture requirements merely because they sound advanced. Ordinary Mahalanobis, extra statistical features or an optional display may be compared, but they do not replace RMS plus persistence or the RGB/USB evidence path. Third, it prevents post-semester patent-development hypotheses from being backfilled into the MVP. PIRG, ambiguity handling, protected updating and remount transfer belong to Chapter 07 and require separate authorization, equipment, evidence and confidentiality controls.

The frozen identity is passive. The system observes vibration and reports a controlled state. It does not actuate against the vibration, shut down the machine, command maintenance or claim that the source of the vibration has been identified. The sensor is permanently singular in the product architecture described here; temporary laboratory instruments may be used to validate the experiment, but they may not be hidden as permanent product dependencies.

## 06.3 Bounded semester objective

The bounded semester objective is to determine whether the locked architecture can **consistently distinguish a documented normal state from a deliberately introduced, safe and repeatable abnormal-vibration state using local lightweight processing without cloud dependence**.

A satisfactory project result must demonstrate the complete chain rather than an isolated algorithm. The team must show that the selected sensor is authentic enough for the intended test, that the mount is rigid and repeatable, that the ESP32 acquires samples with recorded timing and integrity, that the two physical states are independently labelled, that a baseline is calibrated without contaminating the held-out test, that persistence suppresses short transients, that local state indication follows the frozen logic, and that USB logs allow the result to be reconstructed after the demonstration.

A successful result is bounded. It may establish that a low-cost target-mounted sensing chain can detect the controlled state change on the team’s rig. It does not establish that the same threshold generalizes to every motor, that FFT identifies a fault type, that the abnormal state represents a real bearing failure, that one sensor can reject neighbouring-machine interference, that the system is safe for industrial deployment or that the ordinary feature stack is patentable.

VibeGuard remains the strongest supported semester-build recommendation in the attached comparative record because its hardware chain is comparatively simple, the firmware and signal-processing tasks align with the team’s technical strengths, subsystem failures can be isolated, and the demonstration can be backed by controlled logs. That recommendation is not the same as approval. The proposed shift from OpenBraille, the exact course platform, entry into Phase 4 and procurement remain unresolved until an explicit controlling decision is recorded.

## 06.4 System architecture overview

| Subsystem | Frozen role | Evidence boundary |
|---|---|---|
| Controlled rig | Produces documented normal and safe induced-abnormal states | Experimental label, not proof of a real industrial fault |
| ADXL345-class sensor | Converts target vibration into X/Y/Z samples | Module claims do not replace incoming, saturation or measured-limit checks |
| ESP32-class controller | Acquires, processes, indicates and logs | Exact board and pin map require purchased-board verification |
| Acquisition layer | Maintains timing, windows, buffers and integrity counters | Configured rate is not achieved-rate evidence |
| Time-feature layer | Calculates RMS and approved statistics | Conventional support for the bounded classifier |
| Minimum decision | Applies calibrated RMS threshold and persistence | Post-hoc test tuning invalidates evidence |
| Supporting analysis | FFT/bands and optional Mahalanobis comparison | No automatic diagnosis, attribution or novelty |
| RGB and USB | Provides live state and exportable evidence | LED-only demonstration is insufficient |
| Configuration control | Links results to sensor, mount, firmware, rig and session | Mixed or unknown configurations must not be pooled |

The layers prevent one type of evidence from substituting for another. A clean plot cannot repair unsafe labels or sample loss, and a red LED cannot prove valid sensing. A controlled negative result may still be valuable when the measurement chain and failure are documented.

## 06.5 Sensor and mounting architecture

The frozen sensor class is ADXL345-class. Higher-bandwidth sensing remains a later possibility, not the semester identity. Current datasheet values, availability and module authenticity were not reverified in this stage.

Incoming acceptance must preserve supplier and module identity, verify communication and plausible axis response, and inspect instability, noise, clipping or saturation. A failed module must be replaced or explicitly bounded; the classifier must not be tuned around defective hardware.

SPI is the controlling interface. Clock, range, output-data rate and final wiring must be established through measured integrity tests. Short, secure wiring and a stable final interconnect are required for locked evidence.

The sensor must be rigidly coupled to the target housing or a documented rigid bracket. Foam, loose breadboard placement, hand pressure and variable soft coupling are unacceptable because mounting changes amplitude, orientation and spectral response.

Records must include module identity, range/rate, axis convention, mount ID and method, orientation photographs, remount history, clipping/noise observations and session configuration. At least one untouched session, day or remount must be evaluated without threshold changes. The result need not prove universal transfer, but it must disclose tested remount sensitivity.

## 06.6 ESP32 and acquisition pipeline

The controller is ESP32-class, but the exact course-approved board is unresolved. Before final wiring, record board identity, schematic/pinout, regulator, USB interface, framework and toolchain. Roadmap pin maps are provisional.

The pipeline must declare sensor range and output-data rate, measure achieved effective rate and timing, freeze window length and overlap, and document FIFO/interrupt/timer or polling behavior. It must count read errors, saturation, delayed or lost blocks and buffer overruns. Silent loss invalidates the affected evidence.

Optional processing must not corrupt acquisition. FFT execution time, RAM, flash and worst-case processing use should be recorded. If timing is unstable, reduce rate or complexity, improve wiring or buffering, or replace unsuitable hardware.

A controlled sequence is: verify board/sensor; pilot raw X/Y/Z acquisition; measure timing/loss/saturation; inspect both physical states; freeze the lowest stable sufficient configuration; validate FFT scheduling; and emit a configuration banner with every session.

USB records should identify firmware, board, sensor settings, achieved-rate summary, windows, threshold/persistence version, mount, rig state, session and integrity counters. Exported data must permit offline checking; screenshots and LED behavior alone are insufficient.

## 06.7 Time-domain feature pipeline

The permitted time-domain feature family includes RMS, peak, standard deviation or variance, crest factor and kurtosis, calculated on a predeclared axis or magnitude representation. RMS is mandatory because it is the minimum magnitude feature for the frozen classifier. The other features are allowed only when they are implemented, versioned and evaluated without delaying the core system.

Preprocessing must be declared. Mean or DC removal may be applied before features where appropriate. The team must specify whether features are calculated per axis, on a vector magnitude, on a selected axis or through another fixed combination. The choice should be made through calibration and development evidence, then frozen before held-out evaluation. Trying many combinations after examining the test result would inflate apparent performance and weaken the evidence.

Feature proliferation is not a measure of intelligence. A compact, interpretable feature set with stable acquisition and clean session separation is preferable to a large list of statistics that cannot be explained or reproduced. Time-domain features are conventional analytical elements. They support the semester classifier; they do not constitute patent evidence by themselves.

## 06.8 RMS baseline and persistence logic

RMS plus persistence is the controlling minimum classifier. The architecture does not require the team to begin with machine learning or multivariate distance. It requires a physically honest baseline that can be calibrated, frozen, executed locally and tested on untouched sessions.

A controlled procedure is:

1. collect multiple approved normal calibration sessions under a stable, documented sensor, mount, rig and operating configuration;
2. derive an RMS baseline and threshold through a predeclared rule;
3. use separate development sessions to choose the persistence and recovery logic;
4. freeze the threshold, persistence, hysteresis or recovery rule before reviewing held-out results;
5. require threshold exceedance for consecutive windows or a declared duration before entering the abnormal state;
6. log the first physical abnormal-state timestamp where available, the first threshold crossing, the confirmed state transition and the resulting latency;
7. report false alerts, missed abnormal states and invalid sessions without post-hoc threshold repair.

Persistence is not a cosmetic delay. It is the minimum control against momentary shocks, startup transients, handling events and single-window noise. The exact persistence duration is not approved in the attached record. It must be selected and preregistered after pilot evidence. A recovery rule or hysteresis may be added to prevent rapid red/green oscillation, but it must be documented and tested rather than tuned during the final demonstration.

Calibration, development and held-out sessions must remain separated. Windows from one continuous run are not independent simply because they are numerous. Randomly splitting overlapping windows across training and testing can allow nearly identical signal segments into both sets and create misleading performance. The locked evaluation should therefore hold out complete sessions, days and remounts as appropriate.

Sensor, timing or mount faults must be separated from normal and abnormal classification. A failed sensor read, saturated stream or invalid configuration should not be forced into the normal state. An explicit fault/invalid condition may be implemented as an allowed refinement and should be logged even if the RGB demonstration remains centered on calibration, normal and abnormal.

## 06.9 Triggered FFT and selected frequency bands

Triggered or scheduled FFT is supporting evidence. It may help explain how the controlled abnormal state differs from the normal state, reveal repeatable energy redistribution, compare selected bands or support a stronger conventional baseline. It does not automatically diagnose a bearing fault or identify the physical source of the change.

The analysis record must disclose the actual effective sample rate, window length, window function, FFT length, frequency resolution, overlap or hop, selected bands and the physical or empirical reason for selecting them. It must also record execution time, memory use, whether FFT runs only after a pre-trigger or on a schedule, and whether the processing causes delayed or lost acquisition blocks.

Triggered analysis creates its own risk. A trigger may miss a short event, begin after important onset information or bias the set of windows that receive spectral analysis. The team should therefore preserve enough continuous time-domain evidence to explain when and why the FFT was executed. Spectral plots should be tied to session and configuration IDs, not presented as isolated images.

Selected bands must remain bounded by the sensor and acquisition evidence. If the module, mount or sample rate does not reliably observe a band, the team must not claim meaningful energy there. Aliasing, clipping, sensor noise and structural resonances can produce apparently informative peaks. The proper conclusion may be that a band is not trustworthy under the tested configuration.

FFT and band features are conventional. They may improve explanation or held-out discrimination, but they do not establish novelty, source attribution, industrial diagnosis or patentability. Their inclusion is justified only by measurable explanatory or comparative value under the same locked protocol used for the minimum classifier.

## 06.10 Optional Mahalanobis comparator

Ordinary Mahalanobis distance may be implemented as an optional normal-space comparator over a small declared feature vector. It is not mandatory AI, a novelty claim or a source-attribution mechanism.

The comparator should be attempted only after the acquisition-integrity, normal-repeatability, abnormal-repeatability and RMS/persistence gates pass. It should use a documented normal calibration set and the same complete-session held-out protocol as the baseline. If the covariance estimate is unstable, regularization may be used only when declared and versioned. The feature vector must remain small enough to estimate and execute reliably.

The comparator should be dropped if it delays the minimum build, creates unstable covariance, exceeds resource limits, complicates the demonstration without adding value or fails to outperform or clarify the simpler baseline. A more complex score is not automatically a better project result. In Chapter 07, ordinary Mahalanobis also serves as a mandatory conventional baseline against which any future mechanism must be compared; it is never the invention by itself.

## 06.11 Controlled rig and induced abnormal state

The semester rig must be a low-voltage motor, fan or comparable rotating system mounted on a stable base. The normal and abnormal states must be independently defined in physical terms. The preferred abnormality identified in the evidence is a mechanically retained eccentric mass; loosened mounting appears as another possible route. The exact method remains subject to safety and repeatability approval.

The induced state must be deliberate, safe, retained and repeatable. The project must not depend on causing a real machine failure or using an unguarded rotating mass for presentation effect. A successful classifier built around an unsafe or drifting fixture is not an acceptable success.

Required rig controls include:

- a heavy or rigid base that does not walk during operation;
- a rigid motor/fan mount;
- a mechanically retained abnormality fixture;
- a guard around the shaft, fan or rotating mass;
- an immediate power-disconnect method;
- low-speed or current-limited bring-up;
- strain relief and protected wiring;
- a pre-run check of fasteners, guard, sensor mount and electrical connections;
- recorded abnormality mass, radius, position, supply voltage and a speed/load proxy where available;
- an unambiguous rig configuration ID;
- stop rules for movement, loosening, cracking, heating, smell, sparking, repeated controller resets, detached wiring or faculty instruction.

The physical label must be more than “motor looked abnormal.” The team must be able to state what was changed, how it was retained and how the same state was reproduced in another session. Speed, load, supply variation and base movement can alter the vibration independently of the abnormality fixture, so they should be stabilized or recorded.

Normal repeatability must be established before classifier tuning. If normal sessions vary more than the difference between normal and induced-abnormal states, the priority is to repair the mount, rig or acquisition process. Similarly, if the abnormal state cannot be reproduced safely, the fixture must be redesigned rather than compensated through increasingly flexible thresholds.

## 06.12 RGB state indication and USB evidence

The local interface must communicate the state clearly while preserving an auditable digital record. A reconciled state model is:

- **startup/self-check:** the controller reports firmware/configuration identity and checks communication;
- **calibrating:** blue indication and USB status while an approved calibration operation is active;
- **normal:** green after the baseline and state machine are valid;
- **abnormal:** red only after the persistence requirement is satisfied;
- **fault/invalid:** a separately logged condition and, if implemented, a visibly distinct indication.

The RGB output is a live human interface, not the evidence archive. USB logging should include timestamps, raw X/Y/Z samples or declared processed values, feature values, threshold and persistence version, state transitions, sensor-read errors, clipping/saturation, dropped blocks, achieved-rate summaries and session metadata. The logs should be exportable to CSV or another documented format and should preserve enough information to reconstruct the decision.

The final demonstration should show the relationship between the physical state, digital evidence and local indication. A reviewer should be able to identify the rig configuration, see the state transition, inspect the feature or threshold evidence and confirm that no integrity fault occurred. A demonstration in which only the LED is visible is insufficient because the same behavior could be produced without valid sensing.

An Unknown or Interfered state belongs to later attribution research. It must not silently replace or redefine the Level-1 semester output. Fault/invalid handling in Chapter 06 concerns sensor, timing, configuration or mount validity; it does not claim source ambiguity analysis.

## 06.13 BOM and budget evidence

The architecture class is frozen, but the procurement-ready BOM is not. The attached cost values are dated planning evidence and must not be represented as current quotations.

| Cost layer | Controlled interpretation |
|---|---|
| Historical Phase 3C estimate | The corrected ADXL345 route was approximately ₹1,700–₹2,200. A higher-bandwidth route approached ₹4,000. These are historical engineering estimates, not current supplier prices. |
| Teacher-facing roadmap plan | Approximately ₹2,200 expected and approximately ₹3,900 as a protected conservative envelope, dated 3 August 2026. The protected envelope excluded post-semester PIRG work, a second research motor, temporary reference instruments, patent searching and professional fees. |
| Project limits | Preferred spend at or below ₹3,000 and controlling maximum of ₹5,000, subject to teacher requirements and final authorization. |
| Current procurement status | Not frozen. Current specifications, availability, authenticity, delivery, taxes, replacement allowance and exact Indian prices require a later controlled verification pass. |

The provisional semester BOM class includes one ESP32 board, one ADXL345 module, a low-voltage motor or fan, a separate regulated motor supply, RGB LED and resistors, short final wiring or perfboard materials, a rigid base and motor/sensor mount, a retained eccentric fixture and guard, protection/passive components and an allowance for delivery or replacement. Exact models, ratings, sellers and pin maps remain unapproved.

Budget evidence must remain layered. A low historical total does not prove that an authentic sensor, safe rig and suitable power source can be purchased today at the same price. Conversely, a protected planning envelope is not a requirement to spend the full amount. Procurement should occur only after approval, current manufacturer and supplier verification, safety review and a frozen bill of materials.

Post-semester research must have a separate budget. A dual-machine interference bench, temporary synchronized references, field access, patent searching and professional IPR work are not hidden semester expenses. Keeping these costs separate prevents the future patent hypothesis from distorting the feasibility of the ordinary MVP.

## 06.14 Minimum demonstrable success

Minimum demonstrable success requires the complete bounded system, not merely a classifier score:

1. the selected ESP32 and accelerometer pass incoming acceptance and self-check;
2. the sensor is rigidly mounted with recorded orientation and configuration;
3. stable timestamped acquisition is demonstrated with integrity counters;
4. the rig produces a safe, repeatable and independently labelled normal state and induced-abnormal state;
5. multiple normal calibration sessions establish a baseline;
6. RMS plus persistence separates the controlled states locally under a frozen rule;
7. RGB indicates the state clearly and consistently with the log;
8. USB produces an auditable configuration and evidence record;
9. at least one untouched session, day or remount is evaluated without threshold changes;
10. false alerts, missed detections, latency, acquisition loss, remount sensitivity and bandwidth limits are reported honestly;
11. another team member can operate the setup through a checklist and explain the evidence boundary;
12. the final report states that the result proves only the bounded Level-1 task.

FFT, selected bands and ordinary Mahalanobis may enrich the result but are not required for semester success if the minimum classifier and evidence package are complete. A simple, reproducible system that reports its limitations is stronger than an expanded system that cannot demonstrate acquisition integrity or held-out validity.

## 06.15 Validation and entry gates

| Gate | Question | Required evidence | Failure response |
|---|---|---|---|
| Authorization | Has the teacher approved the proposed concept shift, course platform and safe Level-1 scope? | Explicit controlling decision, conditions and date | Do not freeze procurement, claim Phase 4 entry or present VibeGuard as finally selected |
| V0 — Component acceptance | Are the board, sensor, motor and supply usable? | Board identity, USB operation, sensor identity/axis response, stable rails and rig inspection | Replace or redesign the failing component before integration |
| V1 — Acquisition integrity | Can stable timestamped data be collected? | Achieved rate, timing record, read/loss/saturation counters and stable wiring | Reduce rate/clock, shorten wiring, move to final interconnect or replace the sensor |
| V2 — Normal repeatability | Is normal behavior stable across independent sessions and remounts? | Complete-session feature distributions, rig records and mount photographs | Repair the rig or mount before classifier tuning |
| V3 — Abnormal repeatability | Is the induced state safe, labelled and repeatable? | Repeated abnormal sessions and physical configuration metadata | Redesign the fixture; do not tune around unstable labels |
| V4 — Minimum classifier | Does RMS plus persistence work locally? | Frozen calibration/development results, state logs and latency | Simplify features or improve physical repeatability |
| V5 — Supporting comparisons | Do FFT/bands or ordinary Mahalanobis add useful evidence? | Same held-out protocol and resource comparison | Drop the optional comparator if it adds no value or threatens baseline integrity |
| V6 — Locked held-out run | Does the frozen system generalize to untouched sessions, days or remounts? | Pre-registered metrics, immutable split and no post-hoc threshold changes | Report failure honestly and preserve the measurement-study result |
| V7 — Demonstration and documentation | Can a second operator run and explain the system safely? | Checklist, rehearsal, logs, configuration record and source-backed report | Freeze feature growth and correct only essential defects |

The authorization gate precedes procurement. The technical gates then proceed from physical and acquisition validity toward classification. This order prevents the team from spending time optimizing algorithms on unreliable hardware or unstable labels.

## 06.16 Quantitative evidence categories

No final Level-1 numeric gate is approved. Roadmap figures are preregistration proposals only. The following categories are mandatory:

| Category | Required report |
|---|---|
| Independent units | Sessions, days, remounts, operators and physical repetitions |
| Detection | Sensitivity/missed abnormal states and class counts |
| False alerts | Specificity, stable-normal duration and alert count |
| Outcomes | Confusion matrix including invalid sessions |
| Latency | Physical label/change time, threshold crossing and persistence confirmation |
| Integrity | Achieved rate, timing, errors, saturation and dropped/delayed blocks |
| Reproducibility | Second-operator and untouched session/day/remount result |
| Resources | RAM, flash, worst-case processing and logging behavior |
| Exclusions | Every excluded session and predeclared reason |
| Limits | Mount, sensor band, rig dependence and unsupported generalization |

Before a locked run, the authorized owner must approve threshold derivation, persistence/recovery, counts, hold-out structure, exclusions, latency and kill rules. Failure must be reported rather than repaired through post-hoc tuning.

## 06.17 Mounting, sampling, rig and classification risks

| Risk | Why it matters | Controlling treatment |
|---|---|---|
| Counterfeit or poor-quality sensor | Communication may work while noise, bandwidth or axis response is unsuitable | Preserve supplier/module records, run incoming checks and replace failed hardware |
| Mount-dependent result | Coupling changes amplitude, orientation and spectrum | Use a rigid documented mount, mark orientation and test at least one remount |
| Sampling or SPI loss | Irregular timing can corrupt RMS and FFT while producing plausible outputs | Use short wiring, conservative settings, explicit counters and an acquisition gate |
| Saturation or bandwidth mismatch | The sensor may clip or fail to observe the useful band | Pilot range/rate, disclose measured limits and avoid unobserved fault claims |
| Unsafe abnormality fixture | A loose mass or moving base creates physical danger and invalid labels | Retain and guard the fixture, inspect before each run and stop on defined hazards |
| Unrepeatable state labels | Speed, load, voltage or fixture position may drift | Stabilize or record the physical state before classifier tuning |
| Data leakage | Overlapping windows from one run can inflate performance | Hold out complete sessions, days and remounts |
| Startup or handling transients | Short shocks may exceed the magnitude threshold | Use persistence, controlled startup handling and event logs |
| Comparator expansion | Extra features, FFT, Mahalanobis or ML may delay the baseline | Baseline first; drop optional work if schedule or integrity is threatened |
| Team bottleneck | One person may become the only operator or evidence owner | Use primary/reviewer ownership, checklists and cross-training |
| Patent expectation distortion | Future mechanisms may enter the semester scope without evidence | Separate repositories, budgets, claims and approval gates |
| Overclaiming from isolated rig | The demo may be mistaken for industrial source diagnosis | State the Level-1 boundary in the report, poster and presentation |

Risk controls should be treated as design requirements, not final-report disclaimers. The project is strongest when a risk is prevented or measured before the demonstration, rather than mentioned after the result has already been compromised.

## 06.18 Allowed refinements

The following refinements are permitted within the frozen architecture when they do not delay the minimum build or change the concept identity:

- select the exact approved ESP32 variant and revalidate its pin map;
- tune range, rate, window and overlap through pilot integrity tests;
- improve rigid mounting, base, guard, strain relief and final interconnect;
- add explicit sensor, timing, saturation or mount fault/invalid handling;
- choose and freeze a documented axis or magnitude combination;
- add peak, variance or standard deviation, crest factor or kurtosis;
- use triggered or scheduled FFT and selected bands;
- implement ordinary Mahalanobis as a comparator;
- add better metadata, integrity counters and reproducible analysis scripts;
- add a nonessential display provided RGB and USB remain the required interface;
- use temporary laboratory instruments for validation without making them permanent product hardware;
- refine checklists, session registries and second-operator procedures.

Supervised TinyML, online learning, adaptive threshold promotion, automatic baseline updating, source separation or a permanent second product sensor are not ordinary refinements. They require a new authorized scope and belong, if anywhere, to later research. A change that alters the central physical or analytical identity must be recorded through formal change control rather than described as an implementation detail.

## 06.19 Prohibited substitutions and overclaims

The Chapter 06 implementation and final presentation must not substitute or silently add:

- software-security or configuration scanning;
- active vibration cancellation;
- cloud dependence or required wireless service;
- a multi-sensor deployed array;
- remote fleet management;
- remaining-useful-life prediction;
- automatic maintenance decisions;
- industrial safety or condition-monitoring certification;
- demonstrated bearing diagnosis;
- dense-machine target-source attribution or source separation;
- automatic self-learning or online adaptive production behavior;
- PIRG, protected updating or remount transfer;
- teacher approval, Phase 4 entry or procurement authorization not present in a controlling record;
- exact current prices, supplier specifications or authenticity not verified in the procurement stage;
- patent-ready, novel, inventive, eligible or FTO-cleared claims;
- unapproved numerical targets presented as measured or binding facts.

The project should also avoid softer overclaims. “AI-powered,” “industrial-grade,” “predictive maintenance,” “fault isolation” and “real-time diagnosis” can imply capabilities beyond the evidence. The draft-safe description is a controlled local vibration monitor that distinguishes a documented normal state from a safely induced abnormal-vibration state on the project rig using RMS plus persistence, with supporting spectral evidence.

## 06.20 Current implementation and approval status

> **VIBEGUARD CURRENT IMPLEMENTATION STATUS**
>
> - VibeGuard is the strongest supported semester-build recommendation in the attached Project mC record.
> - A formal request exists to shift the semester implementation from OpenBraille to VibeGuard.
> - The attachments do not prove that the teacher approved the shift.
> - The attachments do not prove final acceptance of the ESP32 platform or resolve the earlier STM32/course-platform context.
> - Phase 4 entry, procurement, final BOM freeze, named subsystem ownership and locked quantitative criteria are not proved complete.
> - No physical VibeGuard acquisition, rig, classifier or held-out result is attached to this drafting package.
> - Historical planning evidence indicates that the architecture was intended to fit the ₹5,000 ceiling, but current prices, specifications, availability and authenticity require later verification.
> - The ordinary semester MVP is not established as patentable.

The chapter may therefore guide an authorized build, but it must not be treated as proof that implementation has begun. The next controlling action is an explicit project and platform decision followed by a current specification, safety and procurement pass.

## 06.21 Chapter conclusion

VibeGuard’s semester strength comes from a disciplined boundary. One rigid sensor, one controller, one controlled rotating rig and one minimum classifier create a project that can be built, measured and explained without pretending to solve industrial predictive maintenance. The architecture is only credible when physical mounting, acquisition integrity, state labels, baseline separation and held-out testing receive the same attention as the signal-processing code.

RMS plus persistence is the minimum classifier. Triggered FFT and selected bands may support explanation; ordinary Mahalanobis may be compared after the baseline works. RGB provides a clear local demonstration, while USB and configuration control preserve the evidence. A successful isolated-rig result proves only the bounded Level-1 task. It does not prove bearing diagnosis, target attribution, industrial readiness or patentability.

The chapter is ready to support controlled implementation after approval. It does not itself authorize the concept shift, platform, Phase 4 or procurement. Those decisions, along with current component verification and a preregistered quantitative protocol, remain open.

## 06.S Source notes

The following original organized-workspace sources materially support Chapter 06. The validated reconciliation controls resolved wording and contradictions. Packet filenames and the attachment manifest are not cited as original technical evidence.

### TIER_1 — Current architecture and governance

- `01_GOVERNANCE_AND_CONTROL/01_Project_Requirements/Teacher_Project_Requirements_and_Change_Context.md` — teacher/course constraints, budget context and proposed-change status.
- `01_GOVERNANCE_AND_CONTROL/02_Decision_Registers/Project_mC_Decision_Register_v1.2.md` — retained portfolio, VibeGuard frozen identity and current decision state.
- `03_CONCEPT_PORTFOLIO/VibeGuard/01_Final_Architecture/Phase3C_VibeGuard_Architecture_Report_Final.md` — authoritative Phase 3C engineering selection, sensing chain, processing architecture, rig and historical cost evidence.
- `03_CONCEPT_PORTFOLIO/VibeGuard/01_Final_Architecture/Phase3C_VibeGuard_Memory_Final.md` — final architecture memory, minimum implementation and continuity control.
- `03_CONCEPT_PORTFOLIO/VibeGuard/01_Final_Architecture/Phase3C_VibeGuard_SOP_Final.md` — mission, constraints, evidence rules, validation requirements and phase boundary.

### TIER_2 — Supporting, historical and conditional implementation evidence

- `03_CONCEPT_PORTFOLIO/VibeGuard/05_Roadmaps_and_Reference_Dossiers/HISTORICAL_Phase1C_VibeGuard_Concept_Dossier.docx` — historical concept origin only; does not override the frozen architecture.
- `03_CONCEPT_PORTFOLIO/VibeGuard/05_Roadmaps_and_Reference_Dossiers/VibeGuard_Semester_Implementation_and_Future_Research_Roadmap.pdf` — conditional implementation, BOM, safety, validation, schedule and future-boundary proposal.
- `03_CONCEPT_PORTFOLIO/VibeGuard/PATENT_EVIDENCE_INDEX.md` — controlled research-lane and synthesis identity, status and exclusion context.
- `03_CONCEPT_PORTFOLIO/VibeGuard/README.md` — concept-folder status and navigation support.
- `04_COMPARATIVE_DECISION/03_Change_Request/Project_mC_Request_to_Change_from_OpenBraille_to_VibeGuard.docx` — formal change request and proposed roles; not approval.

# Chapter 07 — VibeGuard Patent Evidence and Future Research Path

## 07.1 Chapter purpose and legal boundary

This chapter explains what the controlled patent-evidence record does and does not support, why the ordinary VibeGuard MVP is not the current invention, and what physical research would be required before a later mechanism could become eligible for an institutional file/no-file review. It is not legal advice and does not authorize a patent filing.

The evidence must be read in four layers:

1. the ordinary frozen Level-1 semester MVP;
2. conventional refinements and comparators within that MVP;
3. post-semester interference, ambiguity, remount and transfer experiments;
4. speculative patent-development mechanisms, including PIRG.

The attached syntheses and simulation are time-bounded research records. They do not establish an exhaustive worldwide search, current national legal status, novelty, inventive step, patent eligibility, useful claim scope, infringement clearance, FTO, filing approval or probable grant. Patent-family and non-patent-literature conclusions require a fresh primary-source pass immediately before any material patent decision.

Raw research lanes are evidence sources, not votes. A conclusion does not become reliable because several models repeat it. Unsupported legal confidence, simulated searches, incomplete fragments, abstract-only readings, invented performance thresholds and concept-swapped content are excluded or downgraded. The valid syntheses control the audited interpretation, while the raw lanes remain provenance and lead sources.

## 07.2 Ordinary MVP patent position

> **VIBEGUARD PATENT STATUS — NO CURRENT FILING BASIS**
>
> - The ordinary ADXL345-plus-ESP32 Level-1 stack is not established as patentable.
> - Its rigid sensing, local acquisition, DC/mean removal, common time features, RMS threshold, persistence, FFT, selected bands, static baseline comparison, ordinary Mahalanobis, RGB alerting, USB logging and controlled rig are conventional individually and, on the attached evidence, form a predictable monitoring aggregation.
> - Low cost, edge-only operation, one sensor, absence of cloud service and a student-friendly implementation do not by themselves create novelty or inventive step.
> - No filing commitment is justified by the current record.
> - PIRG is not implemented or validated and is not part of the semester MVP.
> - Any later positive mechanism would still require physical evidence, current primary-source prior-art review, FTO analysis, field-like evidence, confidentiality control and ownership/inventorship review before institutional or professional file/no-file consideration.

The ordinary MVP nevertheless has important research value. It creates a stable measurement chain, establishes the sensor and mounting limits, produces controlled labelled data, exposes timing and resource constraints, and provides conventional baselines against which later mechanisms can be falsified. It also produces contemporaneous evidence of what was actually implemented and what failed.

The MVP should not be filed or presented as the invention merely because it is inexpensive, local, subscription-free or implemented on an ESP32. The patent syntheses place the ordinary feature stack in a crowded field. Triggered processing, confidence scores, baseline learning, FFT bands and ordinary Mahalanobis are also crowded directions when claimed in isolation. The future case, if any, must arise from a specific enabled physical-control relationship that produces a measurable technical effect beyond these baselines.

## 07.3 Research-lane integrity and limitations

Six controlled research lanes are preserved, but they are not equal and are not votes.

| Lane | Useful contribution | Treatment |
|---|---|---|
| ChatGPT DR | Search leads, Level-1/Level-2 separation, claim-to-test framing | Medium; retain audited leads |
| Gemini | Project fidelity and guarded bench/field framing | Medium-low for legal conclusions; optimistic novelty/FTO and invented numbers excluded |
| Perplexity | Located-document leads and conservative gaps | Medium for located records; low completeness |
| Qwen | Some kill-test and remount prompts | Low; simulated search and unsupported legal/quantitative claims excluded |
| Mistral partial | Actor and document-number leads | One partial low-reliability lane, no final verdict; missing conclusions not reconstructed |
| Copilot | Frozen architecture and Level-1/Level-2 framing | Medium for project fidelity, low for patent/legal analysis |

The valid syntheses control audited readings. Raw lanes remain provenance or search leads; repetition cannot repair an unsupported conclusion. Patent-family and status statements remain time-bounded and require official verification.

## 07.4 Valid synthesis conclusions

The two valid VibeGuard patent syntheses converge on a conservative core:

- the frozen MVP is buildable as a research platform but is not the invention;
- isolated Level-1 normal/abnormal classification cannot prove target attribution;
- one target-mounted accelerometer observes a mixture shaped by the target, neighbours, structure, speed/load, mounting and sensor limits;
- ordinary FFT, selected bands, Mahalanobis, baseline learning, triggered processing and confidence scores are crowded standalone directions;
- a surviving research direction must connect independently known physical states to a specific mechanism and a measurable reduction in wrong-source decisions or contaminated learning;
- strong conventional baselines, complete-session/remount holdouts and field-like labels are mandatory;
- the broad integrated direction faces high obviousness risk, unresolved novelty and FTO, enablement gaps and a field-access dependency;
- the future route is at best a Track-C-style long-term research path requiring later extension, not a patent-first semester claim.

The syntheses describe a broad label-aware, contamination-protected, confidence-gated single-node target-attribution loop. In that map, independently known target and interferer states support separate representations; target departure and ambiguity are scored separately; the system may abstain rather than force a target-fault label; baseline updates are guarded against contamination; and mount validity determines whether a model remains usable.

This broad description is not proof that the elements cooperate non-obviously. It is a research map. The later pre-build simulation therefore narrows the first test and defers update and transfer claims. The distinction between the broad synthesis-level direction and the narrow first experiment is central to this chapter.

## 07.5 Cross-concept adjudication context

Both final comparative adjudications identify VibeGuard as the strongest semester-build candidate. This agreement supports the Chapter 06 recommendation because VibeGuard offers the most manageable combination of hardware simplicity, embedded processing, validation and demonstration.

The adjudications do not agree on the preferred future patent-development gate:

- the Work Max adjudication favors a VibeGuard Level-2A signal-and-access gate and uses TrueMoist as fallback if that gate fails;
- the Deep Research High adjudication favors an OpenBraille D11 physical-state observability gate first and retains VibeGuard as fallback.

The adjudications are decision context, not votes. Their disagreement means the project has no resolved patent-first route. It would be incorrect to average the two documents, select VibeGuard merely because both prefer its semester build, or treat either conditional gate as proof that PIRG works. A controlling project authority must choose a gate, define a replacement rule or defer patent-first selection.

OpenBraille and TrueMoist remain legitimate retained concepts. Chapter 07 does not import their mechanisms into VibeGuard or use their existence to strengthen the VibeGuard patent case. The only cross-concept conclusion used here is the unresolved decision state recorded in validated Part I.

## 07.6 PIRG research hypothesis

The controlling sources do not define an expansion of **PIRG**. This manual uses the acronym only.

### Broad synthesis-level mechanism

The valid syntheses describe a label-aware, contamination-protected, confidence-gated single-node attribution loop. Independently known target/interferer states support target and interference representations; target departure and ambiguity are scored separately; unsupported cases may be Unknown; baseline admission is guarded; and mount validity determines whether the model remains usable. This is a research map, not an enabled or patentable system.

### Narrowed paired-intervention candidate

The pre-build simulation says the broad mechanism should be redesigned before testing. Its narrower first candidate is:

1. form a target-change contrast from paired measurements where the target changes and the interferer is fixed;
2. form an interference-change contrast where the interferer changes and the target remains normal;
3. produce a runtime deviation vector from the one permanent target-mounted sensor;
4. compare it with both contrast structures through projection residuals or an equivalent frozen test;
5. require an anomaly gate;
6. output Target-Abnormal only when the event is anomalous and fits target change materially better;
7. output Unknown when ambiguous, out of support or mount-invalid;
8. keep RMS/persistence, FFT/bands, Mahalanobis and a strong frequency-domain classifier as baselines;
9. defer baseline promotion/rollback;
10. default to model invalidation and recommissioning after an unvalidated remount.

### Relationship to Level 1

PIRG reuses the target-mounted sensing platform but is not part of the semester MVP. It requires a separate dual-source/factorial rig, independently controlled target and interferer states, temporary synchronized references for ground truth, blocked held-out sessions/remounts and later field-like evidence. A negative result does not invalidate the semester monitor.

### Baselines and ablations

All methods must use identical blocked splits. Baselines include RMS/persistence, FFT/bands, ordinary Mahalanobis, static spectral comparison, naive adaptation where relevant and a strong one-sensor frequency-domain classifier. Ablations must remove the contrast, anomaly/Unknown gate, mount rule and any later update protection separately.

### Required evidence

Required evidence includes independent target/interferer labels; repeated paired interventions; multiple sessions, days, speed/load regimes and remounts; immutable data and metadata; held-out contrast stability; wrong-source errors, missed target faults, false target alerts, Unknown coverage and latency; edge integrity/resources; strongest-baseline comparison; ablations; and later field-like labels if the bench gate passes.

### Failure conditions

Kill or redesign the hypothesis if contrasts are collinear or unstable; held-out geometry fails; gains depend on leakage or near-universal abstention; a permanent reference sensor is required; the useful band is unobserved; edge execution loses data; the effect disappears against baseline/ablation; field-like labels are unavailable; or current primary prior art defeats the mechanism.

### Current unproved status

No source proves observability, novelty, non-obvious cooperation, enabling parameters, useful Unknown coverage, remount transfer, contamination-safe updating, field generalization, claim value or FTO. PIRG remains a candidate mechanism, not an implemented invention or filing basis.

## 07.7 Target-source attribution and non-identifiability

A single target-mounted accelerometer measures a mixture. The observed signal is shaped by the target, neighbouring sources, structural coupling, speed and load, mounting orientation and stiffness, sensor range and bandwidth, noise and the acquisition pipeline. A classifier can perform well on an isolated target rig while learning only the difference between two convenient experimental states.

Target attribution asks a different question: when the sensor reports a change, is the target itself abnormal, or did the measured vibration change because a neighbour, load, mount or structure changed? Without independent labels, a target-only classifier cannot answer that question reliably.

The research design must therefore vary target and interferer states independently. Temporary references or command logs should establish ground truth without becoming permanent product hardware. The evaluation must report wrong-source attribution—not merely binary anomaly accuracy. A system that detects “something changed” but frequently blames the target for an interferer is not a successful attribution system.

Non-identifiability is a legitimate possible result. If target and interferer effects occupy the same subspace, if the contrast changes unpredictably after remounting, or if the sensor lacks sufficient bandwidth or coupling information, one sensor may be unable to support the desired attribution. The project must not respond by silently changing to a sensor array, cloud service or different product concept. It should record the boundary and terminate or narrow the hypothesis.

## 07.8 Ambiguity, abstention and useful coverage

A future attribution mechanism may use an explicit **Unknown** or **Interfered** state when the evidence does not support a target-fault decision. This is a post-semester research hypothesis, not a frozen RGB state for the ordinary MVP.

Abstention can be valuable only when it reduces wrong target-fault decisions while retaining useful coverage. A mechanism that labels nearly every difficult case Unknown may show low error among the few decided cases but provide little practical value. The experiment must therefore report risk/coverage or error/coverage behavior, calibration of the ambiguity score and the proportion of observations assigned to each state.

A valid Unknown gate should:

- use a separately defined ambiguity, contrast or support measure;
- block Target-Abnormal for out-of-support, ambiguous or mount-invalid observations;
- remain distinct from ordinary sensor/read/timing faults;
- reduce wrong-source labels on held-out interference and remount blocks;
- preserve useful decision coverage;
- expose rather than hide failure cases.

The user-interface meaning of Unknown is unresolved. It must not be silently mapped to the Level-1 green or red output. Any future UI should distinguish “target appears abnormal,” “target attribution unsupported” and “sensor/configuration invalid.”

## 07.9 Protected update and contamination-control hypothesis

Protected updating addresses a real risk: a target fault, changed neighbour or invalid mount may be admitted into the trusted normal model. A naive adaptive baseline can then learn the abnormal state as normal and suppress future alerts.

The broad syntheses describe buffering or quarantine, confidence and stability admission, separate target/interference envelopes, promotion, lockout, rollback and audit logs. These elements are not established as novel or effective. Generic guarded adaptation is heavily crowded and obviousness-prone.

The pre-build simulation therefore defers automatic promotion from the first PIRG experiment. The attribution contrast must pass independently before update logic is added. A later separate experiment may test:

- clean normal drift;
- changed neighbour or interference conditions;
- seeded target faults;
- wrong, delayed or missing labels;
- power interruption;
- quarantine duration and evidence;
- promotion, freeze, lockout and rollback behavior;
- auditability of every update decision;
- comparison with static and naive adaptive baselines.

Protected updating survives only if it produces a measurable cooperative effect beyond conventional alternatives. It must not be assumed to prevent contamination merely because the design includes words such as confidence, quarantine or rollback.

## 07.10 Remount validity and transfer boundary

Remounting can change orientation, coupling, amplitude and spectral structure. The Level-1 semester project must report remount sensitivity. The future attribution project must use blind held-out remounts and complete sessions rather than random windows from a single mounting.

The safest initial rule is:

1. record or detect a mount-domain change;
2. invalidate the previous model when validity is not established;
3. require controlled recommissioning;
4. test transfer mapping only as a separately preregistered hypothesis;
5. reject a transfer claim if it suppresses genuine target-fault evidence or does not outperform full recalibration.

No source proves cross-mount or cross-machine transfer. A later transfer mechanism would need to preserve fault sensitivity while correcting mount-induced variation. It would also require strong baselines and ablations because normalization and domain adaptation are crowded areas.

Mount invalidation is a validity control, not automatically a patent mechanism. Transfer is a separate hypothesis and must not be merged with the first PIRG core simply to create a larger claim narrative.

## 07.11 Relationship among future mechanisms

| Future element | Reconciled status | Relationship and boundary |
|---|---|---|
| Target/interference contrast attribution | First narrowed PIRG candidate | Test first against conventional baselines and ablations |
| Anomaly gate | Part of the narrowed decision | Prevents ordinary in-support variation from becoming Target-Abnormal; effect must be measured |
| Unknown/abstention | Part of the narrowed attribution output | Valid only if wrong-source error falls at useful coverage |
| Mount validity/invalidation | Required evidence control | Initial default is invalidation and recommissioning |
| Remount transfer mapping | Separate later hypothesis | Test only after basic invalidation is reliable |
| Quarantined shadow baseline | Separate later hypothesis | Deferred until attribution core passes |
| Promotion/rollback | Part of later protected-update experiment | Must be auditable and contamination-resistant |
| Speed/load conditioning | Conventional control or component | Strong prior-art risk; not a standalone invention story |
| Triggered FFT/resource scheduling | Ordinary implementation refinement | Baseline engineering, not the patent mechanism |
| Dense-machine field attribution | External-validity requirement | Not a mechanism and not proved by a bench rig |

These elements may appear in one research roadmap, but they must not be treated as one implemented cooperative system. The first experiment should answer the narrowest decisive question. Adding update, transfer and field claims before the attribution core works would make failure analysis harder and encourage unsupported patent language.

## 07.12 Pre-build simulation boundary

The pre-build simulation is conditional planning evidence. Its examiner, opponent, claim, cost and filing scenarios are simulations, not current legal outcomes. It does not prove that PIRG works or that a claim would survive examination.

Its controlling posture is:

- preserve the ordinary Level-1 semester build unchanged;
- redesign the broad future mechanism before testing;
- carry forward only the paired target-change/interference-change contrast question initially;
- obtain owner approval for a quantitative gate;
- use blocked, randomized, independently labelled experiments;
- compare against strong conventional baselines and ablations;
- stop or narrow the patent route when kill conditions are met;
- avoid claim drafting or material filing spend before the mechanism and evidence are concrete;
- maintain confidentiality and contemporaneous records;
- refresh patent, non-patent-literature and legal-status evidence before a filing decision;
- obtain institutional and professional review.

The simulation does not authorize a late semester feature, a hidden permanent reference sensor, public novelty claims or a patent filing. Its “redesign before testing” conclusion controls the relationship between the broad syntheses and the narrow first candidate.

## 07.13 Experimental evidence roadmap

A credible programme is gated; later stages do not begin merely because earlier plots are interesting.

### Level 1 — semester foundation

Establish stable one-sensor acquisition, controlled normal/abnormal separation, RMS/persistence, conventional FFT/Mahalanobis baselines, timing/loss/resource records and immutable configuration-linked data. This is a platform gate, not attribution evidence.

### Level 2A — controlled interference bench

Control target and interferer independently; retain one permanent product sensor; use temporary references or command logs for ground truth; randomize factorial states; collect multiple days, sessions, speeds/loads and remounts; block calibration/development/held-out partitions; select the strongest baseline prospectively; and report contrast stability, wrong-source attribution, false target alerts, missed target faults, Unknown coverage, latency, resources and ablations.

### Level 2B — field-like or real-site evidence

Use at least one independently labelable realistic coupled-frame or dense-machine setting with lawful access, safety approval, unseen conditions/remounts and ground truth independent of the product sensor. If reliable labels cannot be obtained, narrow or terminate the attribution claim.

### Quantitative gate

No final gate is approved. Pilot variance should support an owner-approved preregistration covering the primary endpoint, coverage, recall, class balance, blocked holdouts, exclusions and kill rule. Windows within one run are not independent trials.

### Suggested gated sequence

| Gate | Decision | Stop condition |
|---|---|---|
| P0 | Authorization, confidentiality and contributor control | No private mechanism work/public detail without approval |
| P1 | Reliable Level-1 platform | Repair platform before attribution work |
| P2 | Independent, repeatable target/interferer labels | Stop if labels cannot be controlled |
| P3 | Stable separable contrast geometry | Kill/redesign if collinear or unstable |
| P4 | Improvement over strongest conventional baseline | Stop patent route if gain is absent or leakage-dependent |
| P5 | Useful Unknown risk/coverage | Reject near-universal abstention |
| P6 | Correct remount validity/invalidation | Default to recommissioning when validity fails |
| P7 | Added value from protected updating | Drop update claim if no cooperative effect |
| P8 | Field-like externally valid evidence | Terminate/narrow if access or effect fails |
| P9 | Current patent, FTO, ownership and value gate | No filing when any material gate fails |

## 07.14 Prior-art and legal-status limitations

The attached syntheses reviewed a broad set of vibration-monitoring, baseline, Mahalanobis, source-attribution, speed-conditioned, remote-learning and industrial patent/non-patent-literature leads. They found substantial overlap with ordinary elements and high obviousness risk for the integrated direction.

The record remains limited:

- the search is not exhaustive;
- evidence dates are time-bounded;
- patent-family membership and legal status are jurisdiction-specific;
- status of one family member cannot be transferred automatically to another;
- an abstract or descriptive passage is not a claim chart;
- a granted claim, pending claim and abandoned claim have different implications;
- prosecution history may change the meaning or scope of a claim;
- the actual future firmware, mechanical implementation and intended jurisdictions are not frozen;
- non-patent literature on paired-intervention contrast attribution requires refresh;
- no professional patentability opinion is attached.

Before material patent spend, the project must freeze the implemented mechanism, search current official patent registers and primary literature, retrieve the actual independent and relevant dependent claims, review prosecution histories and chart every necessary element. The search should focus on the enabled mechanism and experimentally demonstrated effect rather than broad words such as vibration monitoring, confidence or adaptation.

A later search may defeat the hypothesis even after a technical success. That outcome should be accepted. Engineering value and patent value are separate gates.

## 07.15 Freedom-to-operate boundary

FTO asks whether making, using, selling, offering or importing the actual implementation in the intended jurisdiction may fall within live claims. It is not answered by showing that the project is academic, local, low-cost or different in overall purpose.

The attached record does not provide:

- a frozen commercial product implementation;
- intended countries and acts;
- a complete current live-claim set;
- element-by-element claim charts;
- dependent-claim and doctrine-of-equivalents analysis;
- prosecution-history review;
- a professional written FTO opinion.

A project may be unpatentable yet still infringe a live claim, or patentable yet still require a licence to practice another claim. Novelty and FTO are separate analyses. A local-only ESP32 implementation is not automatically safe, and an educational prototype is not assumed exempt.

Before productization, the team must freeze the implementation, identify jurisdictions and activities, retrieve current official claims, chart every required element and obtain professional advice. Any design-around must be evaluated against actual claim language and equivalents, not inferred from a high-level difference.

## 07.16 Confidentiality, contribution and institutional IPR control

The ordinary Level-1 problem statement and conventional stack may be described generically with honest boundaries. The future mechanism and evidence require stronger control pending institutional IPR review.

Potentially sensitive material includes:

- exact paired commissioning and intervention sequences;
- contrast/subspace definitions and projector construction;
- target and interference representations;
- anomaly, ambiguity, Unknown and mount-validity rules;
- update quarantine, promotion, lockout and rollback logic;
- selected bands, parameters and experimentally optimized thresholds;
- firmware, test automation and labelled mixed-source datasets;
- raw field/site data and site identity;
- negative results and ablations;
- invention notebooks, contributor chronology and draft claims.

The team should preserve repository history, hashes, firmware and toolchain versions, BOM and purchase records, photographs, calibration and timing tests, raw signals, randomization seeds, protocol versions, exclusions, baseline outputs, remount geometry and signed contribution records. Old records must not be rewritten to make a later idea appear earlier.

Ownership and inventorship are not the same as project membership. Inventorship depends on contribution to the claimed conception, while ownership depends on institutional, contractual and legal rules. The attachment set does not resolve either. The institution should review contributor records, disclosure obligations and public-release plans before a filing decision.

No detailed paper, public repository, poster, unrestricted demo video, competition submission, vendor pitch or field trial should disclose the future mechanism before institutional review. Confidentiality preserves options; it does not prove patentability or trade-secret status.

## 07.17 File/no-file decision gate

The current record supports **no filing commitment**.

### Do not file on

- the ordinary ADXL345/ESP32 MVP;
- RMS, FFT, selected bands, Mahalanobis, static baseline or triggered processing alone;
- low cost, one sensor, edge-only operation, absence of cloud or RGB/USB positioning;
- a broad desired result called single-node source attribution without an enabled mechanism;
- simulation-only evidence;
- target-only or isolated-rig accuracy;
- generic confidence gating, adaptation, remount handling or abstention language without a measured cooperative effect.

### Consider institutional or counsel review only if

- the exact future mechanism is frozen and implemented;
- paired target/interference contrast geometry is identifiable and stable;
- the mechanism beats the strongest conventional baseline on untouched interference and remount blocks at useful coverage;
- every critical element survives ablation;
- the result repeats beyond one fixture and includes independently labelled field-like evidence;
- edge resource and measurement integrity are proven;
- current primary patent and non-patent-literature searching does not defeat the mechanism;
- ownership, inventorship, confidentiality and disclosure status are resolved;
- claim value and resistance to simple design-around justify the cost;
- professional novelty, obviousness, eligibility and FTO review supports proceeding.

A negative gate should terminate or narrow the patent route while preserving the semester prototype, measurement study and publication value. A positive gate would only make the mechanism eligible for institutional/professional evaluation. It would not promise grant, validity, commercial value or FTO.

## 07.18 Current patent-development state

> **VIBEGUARD PATENT-DEVELOPMENT CURRENT STATE**
>
> - The ordinary frozen MVP is a conventional research platform and is not established as patentable.
> - Six raw research lanes are preserved as evidence sources, not votes; several legal and quantitative conclusions were downgraded or excluded.
> - Two valid syntheses support only a guarded long-term research route with high obviousness and enablement risk.
> - The broad future direction combines labelled source states, target/interference representations, ambiguity handling, protected updating and mount validity.
> - The later pre-build simulation narrows the first test to paired target-change and interference-change contrast structures, projection residuals, an anomaly gate and Unknown for unsupported observations.
> - Protected baseline promotion and remount transfer are separate later hypotheses, not implemented parts of the first PIRG core.
> - No physical Level-2 interference, attribution, ambiguity, update, transfer or field-like evidence is attached.
> - The two comparative adjudications disagree on the first patent-development gate.
> - Fresh official prior-art, non-patent-literature, legal-status and FTO review is required before material patent action.
> - Institutional ownership, inventorship, confidentiality and disclosure rules remain unresolved.
> - The present decision is no filing commitment.

The next meaningful patent-development action is not claim drafting. It is an authorized, confidential, independently labelled physical observability experiment with strong baselines and explicit kill conditions.

## 07.19 Chapter conclusion

VibeGuard’s ordinary semester architecture is valuable because it can produce a disciplined embedded prototype and a reliable measurement foundation. It is not the invention. Its sensor, feature, baseline, spectral and alerting elements are conventional, and the attached evidence does not support filing on their aggregation.

The only surviving long-term direction is a difficult and falsifiable attribution problem. The broad synthesis-level map includes source-conditioned representations, ambiguity handling, protected updating and mount validity. The later pre-build simulation appropriately narrows the first candidate to paired target-change and interference-change contrast structures with an anomaly gate and Unknown outcome. Even this narrowed mechanism remains unproved and may fail because the one-sensor observation is non-identifiable.

A credible path requires independent target/interferer labels, complete-session and remount holdouts, strong conventional baselines, critical ablations, useful abstention coverage, field-like access, edge-resource evidence and current primary-source patent review. Protected updating and remount transfer should be studied only after the attribution core passes. A negative result should stop or narrow the patent route without diminishing the semester project.

No filing decision is justified now. Only a later implemented mechanism that survives physical, legal, ownership, confidentiality and value gates should reach institutional or professional file/no-file evaluation.

## 07.S Source notes

The following original organized-workspace sources materially support Chapter 07. The validated reconciliation controls resolved wording and contradictions. The packet and attachment manifest are not substitutes for the original evidence paths.

### TIER_2 — Valid syntheses, simulation and adjudication context

- `03_CONCEPT_PORTFOLIO/VibeGuard/03_Patent_Synthesis/01_VibeGuard_Patent_Synthesis_Work_Max.md` — audited current patent-evidence synthesis, conventional-MVP conclusion, Track-C hypothesis, reliability treatment and kill criteria.
- `03_CONCEPT_PORTFOLIO/VibeGuard/03_Patent_Synthesis/02_VibeGuard_Patent_Synthesis_Standard_High.md` — independent valid synthesis, reliability audit, guarded mechanism definition and proposed evidence programme.
- `03_CONCEPT_PORTFOLIO/VibeGuard/04_PreBuild_Simulation/VibeGuard_PreBuild_Future_Patent_Case_Simulation.md` — conditional simulation, redesign-before-testing posture, narrowed paired-intervention candidate, evidence roadmap and filing boundary.
- `04_COMPARATIVE_DECISION/02_Final_Adjudications/01_Project_mC_Final_Adjudication_Work_Max.md` — VibeGuard signal/access gate and TrueMoist fallback context; not a vote or technical proof.
- `04_COMPARATIVE_DECISION/02_Final_Adjudications/02_Project_mC_Final_Adjudication_Deep_Research_High.md` — OpenBraille-first gate and VibeGuard fallback context; not a vote or technical proof.
- `04_COMPARATIVE_DECISION/COMPARATIVE_DECISION_INDEX.md` — adjudication provenance and non-voting treatment.

### TIER_3 — Controlled independent research lanes

- `03_CONCEPT_PORTFOLIO/VibeGuard/02_Raw_Research/01_VibeGuard_Patent_Research_ChatGPT_Deep_Research.md` — audited supporting lane with search leads and Level-1/Level-2 framing.
- `03_CONCEPT_PORTFOLIO/VibeGuard/02_Raw_Research/02_VibeGuard_Patent_Research_Gemini.docx` — audited supporting lane; optimistic novelty, FTO and invented quantitative conclusions excluded.
- `03_CONCEPT_PORTFOLIO/VibeGuard/02_Raw_Research/03_VibeGuard_Patent_Research_Perplexity.md` — audited supporting lane with useful located-document leads and conservative gap reporting.
- `03_CONCEPT_PORTFOLIO/VibeGuard/02_Raw_Research/04_VibeGuard_Patent_Research_Qwen.md` — low-reliability prompts and limited ideas only; simulated searches, unsupported portfolios and legal assurances excluded.
- `03_CONCEPT_PORTFOLIO/VibeGuard/02_Raw_Research/05_VibeGuard_Patent_Research_Mistral_PARTIAL_COMPILATION.md` — one partial lane with no complete verdict; unsupported patentability, Mahalanobis, infringement and FTO assertions excluded.
- `03_CONCEPT_PORTFOLIO/VibeGuard/02_Raw_Research/06_VibeGuard_Patent_Research_Microsoft_Copilot.docx` — project-fidelity support where confirmed; patent and legal conclusions downgraded.

# Part III Open-Decision Register

| ID | Decision or uncertainty | Current status | Required next action |
|---|---|---|---|
| VG-OD01 | Teacher approval of VibeGuard shift | Open; request/recommendation only | Obtain explicit approval, conditions or rejection |
| VG-OD02 | ESP32/course-platform acceptance | Open | Obtain written platform decision before procurement |
| VG-OD03 | Phase 4 and procurement | Not proved started/frozen | Authorize, verify current parts/prices/safety, then freeze BOM |
| VG-OD04 | Exact board, module and pin map | Provisional/unverified | Select approved hardware and run incoming checks |
| VG-OD05 | Rigid mount and remount repeatability | Untested | Build, version and test independent remounts |
| VG-OD06 | Sampling/timestamp integrity | Untested | Measure achieved rate, loss, saturation and FFT interference |
| VG-OD07 | Safe abnormal-state fixture | Proposed only | Obtain safety review and repeated physical acceptance |
| VG-OD08 | Level-1 classifier and numeric protocol | Logic fixed; numbers open | Preregister threshold, persistence, counts, holdouts and kill rules |
| VG-OD09 | FFT and Mahalanobis incremental value | Untested/optional | Compare after baseline; drop if non-incremental or unstable |
| VG-OD10 | Team ownership and demo fallback | Proposed only | Assign primary/backups and approve any playback fallback |
| VG-OD11 | Patent-first portfolio gate | Adjudications disagree | Select a gate/replacement rule or defer |
| VG-OD12 | Exact PIRG mechanism | Narrow candidate, not experiment-frozen | Version inputs, outputs, contrast construction and exclusions |
| VG-OD13 | Independent target/interferer ground truth | Not available | Build safe factorial rig with temporary references |
| VG-OD14 | PIRG quantitative gate and strongest baseline | Unapproved/unselected | Pilot variance, benchmark identical blocked splits, preregister |
| VG-OD15 | Contrast identifiability | Central risk, untested | Kill if held-out contrasts are collinear or unstable |
| VG-OD16 | Unknown/coverage value | Hypothesis only | Report risk/coverage; reject near-universal abstention |
| VG-OD17 | Remount validity and transfer | Invalidation proposed; transfer unproved | Blind remount study; keep recommissioning default |
| VG-OD18 | Protected updating | Deferred | Test contamination/promotion/rollback only after attribution passes |
| VG-OD19 | Edge execution of future mechanism | Unprofiled | Verify timing, memory and acquisition integrity |
| VG-OD20 | Field-like labelled access | Unsecured | Obtain authorized site or terminate/narrow attribution path |
| VG-OD21 | Fresh patent/NPL/legal-status/FTO work | Time-bounded/incomplete | Refresh official sources and obtain professional review |
| VG-OD22 | Confidentiality, ownership and inventorship | Unresolved | Apply institutional controls and preserve contribution records |
| VG-OD23 | File/no-file decision | No filing justified | Revisit only after technical, legal, ownership and value gates |

# Part III Contradiction Summary

| ID | Chapter | Issue | Controlling resolution | Residual uncertainty |
|---|---:|---|---|---|
| VG-C01 | 06 | Mahalanobis primary versus optional | RMS/persistence mandatory; Mahalanobis optional comparator | Incremental held-out value |
| VG-C02 | 06 | Proposed rate/bandwidth versus achieved performance | Pilot and measure exact hardware; record achieved limits | Module noise, aliasing and stability |
| VG-C03 | 06 | “Procurement-ready” versus approval open | Roadmap is conditional planning only | Teacher/platform/safety decision |
| VG-C04 | 06–07 | Proposed numbers presented as authoritative | Bind only after preregistration and approval | Final Level-1/2 gates |
| VG-C05 | 06 | Provisional pins/components versus frozen interface | Revalidate purchased hardware | Final board and wiring |
| VG-C06 | 06–07 | Detection language blurs attribution | Chapter 06 detects controlled state; Chapter 07 tests attribution | Single-sensor observability |
| VG-C07 | 06 | Recommended/selected versus teacher-approved | Use strongest recommendation/proposed shift wording | Written approval |
| VG-C08 | 06–07 | Historical prices/specifications/status treated as current | Preserve dates and require fresh verification | Current facts |
| VG-C09 | 06–07 | Level-1 result treated as invention | Conventional foundation and baseline only | Later technical effect |
| VG-C10 | 07 | Broad loop versus narrow first PIRG test | Broad map retained; paired contrast core tested first | Core observability/value |
| VG-C11 | 07 | Protected updating integrated versus deferred | Separate experiment after attribution passes | Cooperative effect |
| VG-C12 | 07 | Remount transfer versus invalidation | Recommissioning default; transfer separate | Transfer feasibility |
| VG-C13 | 07 | Undefined PIRG expansion | Use acronym only | Definition outside package unknown |
| VG-C14 | 07 | Adjudications choose different patent gates | Preserve both; no vote counting | Authorized gate |
| VG-C15 | 07 | Raw-lane novelty/FTO confidence | Audited syntheses control; unsupported claims excluded | Fresh official/professional review |
| VG-C16 | 07 | Simulation treated as proof | Conditional planning and redesign guidance only | Physical/legal outcome |
| VG-C17 | 07 | Unknown assumed beneficial | Require useful risk/coverage evidence | Practical coverage |
| VG-C18 | 06–07 | PIRG enters semester scope/budget | Separate scope, repository, budget and approval | Authorization of later work |

# Part III Source Ledger

The following original organized-workspace paths were materially relied upon. They are grouped by chapter and authority tier. The attachment manifest is excluded because it is file control only. The validated reconciliation controls resolved wording but is not substituted for the original evidence paths. Validated Part I controls the current project state, and validated Part II is a style and cross-concept consistency reference rather than VibeGuard technical evidence.

## Chapter 06 — TIER_1 current architecture and governance

- `01_GOVERNANCE_AND_CONTROL/01_Project_Requirements/Teacher_Project_Requirements_and_Change_Context.md`
- `01_GOVERNANCE_AND_CONTROL/02_Decision_Registers/Project_mC_Decision_Register_v1.2.md`
- `03_CONCEPT_PORTFOLIO/VibeGuard/01_Final_Architecture/Phase3C_VibeGuard_Architecture_Report_Final.md`
- `03_CONCEPT_PORTFOLIO/VibeGuard/01_Final_Architecture/Phase3C_VibeGuard_Memory_Final.md`
- `03_CONCEPT_PORTFOLIO/VibeGuard/01_Final_Architecture/Phase3C_VibeGuard_SOP_Final.md`

## Chapter 06 — TIER_2 supporting, historical and implementation evidence

- `03_CONCEPT_PORTFOLIO/VibeGuard/05_Roadmaps_and_Reference_Dossiers/HISTORICAL_Phase1C_VibeGuard_Concept_Dossier.docx` — historical concept origin only; not current architecture authority.
- `03_CONCEPT_PORTFOLIO/VibeGuard/05_Roadmaps_and_Reference_Dossiers/VibeGuard_Semester_Implementation_and_Future_Research_Roadmap.pdf` — conditional implementation, BOM, safety, validation and future-boundary proposal.
- `03_CONCEPT_PORTFOLIO/VibeGuard/PATENT_EVIDENCE_INDEX.md` — research-lane/synthesis index and exclusion context.
- `03_CONCEPT_PORTFOLIO/VibeGuard/README.md` — folder status and navigation support.
- `04_COMPARATIVE_DECISION/03_Change_Request/Project_mC_Request_to_Change_from_OpenBraille_to_VibeGuard.docx` — formal change request; not approval.

## Chapter 07 — TIER_2 valid syntheses, simulation and adjudication context

- `03_CONCEPT_PORTFOLIO/VibeGuard/03_Patent_Synthesis/01_VibeGuard_Patent_Synthesis_Work_Max.md`
- `03_CONCEPT_PORTFOLIO/VibeGuard/03_Patent_Synthesis/02_VibeGuard_Patent_Synthesis_Standard_High.md`
- `03_CONCEPT_PORTFOLIO/VibeGuard/04_PreBuild_Simulation/VibeGuard_PreBuild_Future_Patent_Case_Simulation.md`
- `04_COMPARATIVE_DECISION/02_Final_Adjudications/01_Project_mC_Final_Adjudication_Work_Max.md`
- `04_COMPARATIVE_DECISION/02_Final_Adjudications/02_Project_mC_Final_Adjudication_Deep_Research_High.md`
- `04_COMPARATIVE_DECISION/COMPARATIVE_DECISION_INDEX.md`

## Chapter 07 — TIER_3 controlled independent research lanes

- `03_CONCEPT_PORTFOLIO/VibeGuard/02_Raw_Research/01_VibeGuard_Patent_Research_ChatGPT_Deep_Research.md`
- `03_CONCEPT_PORTFOLIO/VibeGuard/02_Raw_Research/02_VibeGuard_Patent_Research_Gemini.docx`
- `03_CONCEPT_PORTFOLIO/VibeGuard/02_Raw_Research/03_VibeGuard_Patent_Research_Perplexity.md`
- `03_CONCEPT_PORTFOLIO/VibeGuard/02_Raw_Research/04_VibeGuard_Patent_Research_Qwen.md`
- `03_CONCEPT_PORTFOLIO/VibeGuard/02_Raw_Research/05_VibeGuard_Patent_Research_Mistral_PARTIAL_COMPILATION.md`
- `03_CONCEPT_PORTFOLIO/VibeGuard/02_Raw_Research/06_VibeGuard_Patent_Research_Microsoft_Copilot.docx`

## Explicit exclusions and non-evidence controls

- Software-security/configuration-scanning substitutions and active-vibration-cancellation routes are not the frozen VibeGuard design and are excluded.
- PIRG, target attribution, protected updating and remount transfer are post-semester hypotheses and are not part of the ordinary MVP.
- The attachment manifest is file control only and is not technical or patent evidence.
- Validated Part II is a style and cross-concept consistency reference only; it is not VibeGuard evidence.
- Independent research lanes, syntheses and adjudications are evidence sources or decision context, not votes.
- The Mistral transport compilation is one partial lane with no final verdict; missing conclusions were not reconstructed.
- No prior-chat context, memory, web research, current pricing, fresh patent searching or unstated assumption was used in this drafting stage.

---

**End of Project mC Master Manual — Part III.**

<!-- END CONTROLLED COMPONENT: PART_III -->

---

<!-- BEGIN CONTROLLED COMPONENT: PART_IV -->
<!-- SOURCE PATH: /home/paradoxpete/Documents/PROJECT_ORGANIZED/08_MASTER_MANUAL/03_Drafting_Workspace/01_Validated_Parts/Part_IV/Project_mC_Master_Manual_Part_IV_TrueMoist_Architecture_Evidence_and_Research_Position.md -->
<!-- SOURCE SHA-256: 97a2d6f9b07512771f6d7670e4ad9ea4eeb24b7e81673dda1e968f2884370230 -->

## Part IV — TrueMoist Architecture, Evidence and Research Position

## Document control

| Field | Value |
|---|---|
| Document | Project mC Master Manual — Part IV |
| Controlled filename | `Project_mC_Master_Manual_Part_IV_TrueMoist_Architecture_Evidence_and_Research_Position.md` |
| Status | Controlled draft |
| Scope | Chapter 08 — TrueMoist Architecture, Evidence and Research Position; Part IV evidence-status, open-decision, contradiction and source registers |
| Source boundary | Only the ten attachments in the controlled Part IV drafting package |
| Input inventory | Exactly ten physical attachments were readable. The nine externally hash-controlled inputs matched the manifest byte counts and SHA-256 values. The self-referential manifest was used only for file control. Upload transport suffixes did not create additional logical sources. |
| Current implementation status | Not an implementation, Phase 4 or procurement authorization |
| Approval status | Not a teacher-approval record; final concept and course-platform acceptance remain unresolved |
| Experimental status | The validated 72-run architecture is a selected experimental design, not proof that 72 physical runs, model fitting or held-out validation were completed |
| Patent status | No patentability, filing, infringement or freedom-to-operate conclusion |
| External verification | No fresh web, market, manufacturer, patent-register, legal-status or specification verification was performed; those activities are reserved for a later controlled stage |
| Relationship to Part I | Part I controls the current project state: TrueMoist is retained but neither finally selected nor rejected; VibeGuard is the strongest semester-build recommendation; the proposed OpenBraille-to-VibeGuard shift is not proved teacher-approved; platform acceptance, Phase 4 and procurement remain unresolved; no frozen MVP is established as patentable; the final adjudications disagree on the preferred future patent route |
| Relationship to Parts II and III | Parts II and III were used only for manual style and cross-concept consistency. They are not TrueMoist technical evidence. |

The ten-file package was complete and readable. The reconciliation controls resolved wording; the source packet preserves underlying evidence. No prior-chat context, memory, web research or unstated assumption was used.

## How to read Part IV

Part IV preserves six boundaries.

**Architecture and refinement.** The frozen MVP is a one-soil local compensation design using a genuine analog probe, nearby DS18B20, known S0/S1 batch metadata, evidence-gated acquisition, offline fitting, fixed local coefficients, USB CSV and gravimetric GWC. Jig, wiring, factor values, ADC choice and model stability may be refined without adding live EC, actuation, cloud dependency or online learning.

**Design and evidence.** The 4 × 3 × 2 × 3 plan defines 72 independent physical runs; it does not prove that the runs, fitting or held-out test were completed.

**Metadata and sensing.** S0/S1 records the prepared treatment. It is not conductivity measurement or autonomous salinity estimation.

**Baseline and compensation.** Compensated models must beat the same probe’s uncompensated calibration against the same held-out physical reference.

**Semester and future research.** Replacement, remount, transfer, contamination, validity and fallback mechanisms are later hypotheses, not MVP features.

**Research and filing.** Patent research supports a cautious technical position. It does not establish novelty, patentability, FTO or filing approval.

# Chapter 08 — TrueMoist Architecture, Evidence and Research Position

## 08.1 Chapter purpose

This chapter defines the controlled TrueMoist architecture, experimental method, evidence boundaries and current research position. It is intended to serve as a practical engineering reference after authorization and as a durable record of what the concept does—and does not—claim.

TrueMoist addresses a narrow measurement problem. Low-cost analog capacitive soil-moisture probes can be influenced by temperature, salinity-related treatment, nonlinearity, insertion geometry, packing, unit variation and drift. The project asks whether a carefully controlled local compensation method can produce estimates that are more trustworthy than an uncompensated calibration under a bounded one-soil experiment. It does not seek to create a universal agricultural sensor, a field-ready irrigation system or a general soil-chemistry platform.

The chapter therefore combines four forms of control. It locks the semester architecture; specifies how independent physical evidence is to be produced; distinguishes proposed criteria from measured results; and separates the ordinary engineering project from a later, speculative transfer-and-validity research path. Nothing in this chapter authorizes procurement, Phase 4, public claim-focused disclosure or patent filing.

## 08.2 Current TrueMoist identity

> **TRUEMOIST ARCHITECTURE LOCK**
>
> For the frozen semester architecture, **TrueMoist means only**:
>
> - one genuine analog capacitive soil-moisture probe used for the final dataset;
> - a second nominally identical probe used as a spare and for unit-variation characterization, not as a permanent dual-probe runtime requirement;
> - one nearby waterproof DS18B20 measuring soil temperature at controlled depth and spacing;
> - a known S0/S1 salinity-treatment code assigned from prepared-batch metadata;
> - one homogeneous soil and one controlled preparation procedure;
> - ADS1115 as the primary acquisition design, subject to a paired evidence gate against calibrated ESP32 ADC1;
> - an ESP32-class controller;
> - offline fitting of supported low-order models;
> - fixed coefficients evaluated locally on the controller;
> - USB serial CSV output and optional simple local status indication;
> - dry-basis gravimetric water content as the physical reference; and
> - an authoritative design of 72 independent physical condition runs.
>
> TrueMoist is **not** a live-EC instrument, autonomous salinity estimator, irrigation controller, pump or valve system, cloud platform, farm-telemetry service, universal or multi-soil model, custom multi-frequency probe, TinyML showcase, online-adaptive learner, field-validated product, patent-ready mechanism or teacher-approved semester implementation.

The identity lock prevents older broad descriptions and lower-authority research proposals from changing the selected architecture. Historical references to a self-correcting platform, live conductivity sensing or autonomous action remain useful as origin records only. They do not control the semester MVP.

TrueMoist remains a legitimate retained Phase 3C concept. The controlled project record neither selects it as the final semester build nor rejects it. Its concept-level architecture is ready only with mandatory early validation, while project-wide authorization, platform acceptance and procurement remain open.

## 08.3 Bounded semester objective

The semester objective is to test whether local compensation improves the trustworthiness of one low-cost analog capacitive probe under controlled disturbances in one homogeneous soil. Two estimates must be produced from the same physical observations:

1. an **uncompensated estimate** based only on raw probe response; and
2. a **compensated estimate** that also uses measured soil temperature and the known salinity-treatment code.

Both estimates must be evaluated against the same dry-basis gravimetric reference. Training and model selection must use only the designated training replicates. The final comparison must use an untouched physical replicate and must report absolute error as well as relative improvement.

A successful semester outcome would establish a bounded technical result: on the team’s tested soil, preparation method, temperature range, treatment range, probe configuration and held-out replicate, the selected compensated method improved error relative to the uncompensated baseline without unacceptable degradation in a major subset. It would not establish universal accuracy, cross-soil transfer, long-term field reliability, production calibration, live chemistry measurement, autonomous irrigation or patentability.

A partial or negative result can still be valuable. Evidence that packing variance dominates the intended disturbance, that the probe cannot be reinserted repeatably, that the external ADC adds no value, or that compensation fails on held-out physical samples would be legitimate engineering findings when the test procedure and raw records are preserved.

## 08.4 System architecture overview

The controlling architecture is described as **D-dominant with B-style signal hardening**: model fitting occurs offline, inference remains local, and the low-cost analog path is strengthened through controlled acquisition, filtering, physical geometry and evidence gates.

```text
Prepared-batch metadata
(batch ID, replicate, target condition, S0/S1 code, recorded dose)
                              ┐
Analog capacitive probe ──────┼─> filtered analog node ─> selected ADC path ─┐
Nearby DS18B20 temperature ───┘                                              │
                                                                              v
                                                                        ESP32-class MCU
                                                                    acquisition and checks
                                                                    Model 0 raw estimate
                                                                    selected compensated estimate
                                                                    range and quality flags
                                                                              │
                                                                              v
                                                                       USB serial CSV

Wet/dry mass records ─> dry-basis gravimetric reference ─> offline Python fit,
                                                         grouped validation and
                                                         coefficient freeze
```

| Subsystem | Frozen role | Principal control | Evidence boundary |
|---|---|---|---|
| Prepared soil batch | Produces one controlled physical condition | Fixed soil, mass, water addition, treatment dose, mixing, equilibration and packing record | Metadata does not prove the intended physical state was achieved; measurements and deviations must be recorded |
| Analog moisture probe | Provides the raw electrical response used by all models | Genuine capacitive unit, electrical characterization, fixed insertion geometry and unit identity | A seller label or one stable reading does not establish authenticity, monotonicity or repeatability |
| DS18B20 temperature channel | Measures nearby soil temperature as a model input and factor record | Same depth, controlled separation, equilibration and error checks | Ambient temperature is not a substitute; measured temperature does not automatically prove effective compensation |
| Salinity-treatment metadata | Supplies known S0/S1 preparation state | Recorded NaCl dose in g/kg oven-dry-equivalent soil | Not live EC, conductivity or autonomous salinity estimation |
| Analog acquisition | Converts the probe node to digital observations | ADS1115 primary design with paired ESP32 ADC1 comparison; short filtered path; decoupling | Nominal bit depth is not evidence of better effective accuracy |
| ESP32-class controller | Acquires, evaluates fixed models, flags states and logs records | Versioned firmware, fixed coefficients, local processing, radios disabled during final acquisition | Controller output must be numerically checked against offline calculations |
| Offline analysis | Fits and selects M0/M1/M2 using grouped physical records | Leakage prevention, grouped validation and untouched replicate | A fitted training curve is not held-out performance |
| Gravimetric reference | Supplies dry-basis physical reference | Wet mass, constant dry mass and traceable calculation | No credible accuracy claim exists without oven/scale access and constant-mass control |
| USB evidence path | Exports raw observations, estimates, metadata and quality flags | Versioned CSV schema, batch and run identifiers | Logs must remain linked to physical preparation and reference records |

## 08.5 Authoritative 72-run experimental architecture

The selected experimental design contains four moisture conditions, three temperature conditions, two controlled salinity treatments and three independent physical replicates:

```text
4 moisture conditions
× 3 temperature conditions
× 2 salinity-treatment states
× 3 independent physical replicates
= 72 independent physical condition runs
```

| Factor | Authoritative design position |
|---|---|
| Moisture | Four dry-basis target regions spanning a safe and usable response range identified by pilot work. Exact percentages are not frozen before the selected soil’s behavior, field capacity and probe response are characterized. |
| Temperature | Recommended nominal conditions are 20 °C, 30 °C and 40 °C. A documented 20/28/36 °C fallback is permitted if 40 °C cannot be produced safely and uniformly. Actual soil temperature, not the nominal chamber or ambient value, controls the record. |
| Salinity treatment | S0 contains no deliberately added salt. S1 uses one pilot-selected NaCl dose that creates a repeatable, non-saturating effect. The frozen dose must be recorded in grams per kilogram of oven-dry-equivalent soil. |
| Replicate | Three independently prepared or independently reset physical samples for each factor combination. Replicates 1 and 2 support training and model selection; replicate 3 remains untouched for final physical testing. |

### Definition of an independent physical run

One run is one separately prepared or independently reset physical soil condition. Repeated ADC conversions, multiple serial lines or rapid rereads from an undisturbed container do not create additional runs. They are electronic observations within one physical record and must be aggregated before model splitting.

Independence therefore depends on physical preparation, not sample count in software. Each record must preserve the soil batch, factor levels, replicate identity, probe identity, geometry, mass records, preparation timings, ADC configuration, temperature observation, accepted raw statistics and deviations.

### Training and held-out roles

Replicates 1 and 2 are reserved for training and model selection. Grouped cross-validation must keep all electronic observations and repeated measurements from the same physical batch together. Replicate 3 is reserved as the untouched final test set. It must not influence factor tuning, feature selection, coefficient choice, threshold selection or model-complexity decisions.

The package requires physical independence and leakage prevention but does not freeze a complete random run order. Blocking, randomization, practical oven scheduling and deviation handling must be preregistered before main data collection. Convenience ordering must not be allowed to align a factor with time, probe drift or equipment state without documentation.

> **DESIGN DOES NOT EQUAL COMPLETION**
>
> The 72-run structure is a validated experimental architecture. The controlled attachments do **not** prove that:
>
> - 72 independent physical conditions were completed;
> - a complete physical run ledger or dataset exists;
> - the final model was fitted or selected;
> - coefficients were frozen;
> - Python-to-MCU numerical equivalence was demonstrated;
> - the untouched replicate was tested; or
> - any RMSE, MAE, accuracy or error-reduction threshold was measured.
>
> Until direct records exist, Chapter 08 uses terms such as *design*, *planned run*, *required test*, *proposed criterion* and *unavailable result*.

A documented 54-run contingency exists as a schedule fallback, but it is not equivalent to the authoritative 72-run design. Any reduction requires explicit change control, a revised split plan and transparent reporting of the loss in evidence.

## 08.6 Analog probe and acquisition architecture

The final dataset uses one genuine analog capacitive probe; a second nominally identical unit is a spare and unit-variation check, not a permanent dual-probe product. Before acceptance, the selected unit must show credible capacitive construction, usable analog range, stable warm-up behavior, monotonic pilot response and controlled reinsertion repeatability. YL-69/HL-69-style resistive probes are not the selected sensor.

The short analog path uses a 1 kΩ series resistor and 100 nF input capacitor. The ADS1115 path is decoupled with 100 nF ceramic and 10 µF bulk capacitance. Characterization may begin on breadboard, but the main dataset requires a documented soldered path.

For each physical record, the design requires equilibration; a valid DS18B20 reading; discard of the first ADC conversion after reconfiguration; 64 electronic observations; median-based or three-MAD rejection; an accepted mean and dispersion summary; evaluation of raw and compensated estimates; and logging of metadata and quality flags. The 64 observations remain one physical sample.

ADS1115 is primary but evidence-gated. Week 1 compares it with calibrated ESP32 ADC1 on the same analog node using noise, drift, reinsertion and pilot-error evidence. ADC1 is the fallback when the external module offers no practical value or is unsuitable.

## 08.7 Temperature-measurement role

The waterproof DS18B20 measures soil temperature near the active probe region. Its purpose is twofold: it records the actual experimental temperature condition and supplies a measured compensation input to Models 1 and 2.

The probe and temperature sensor must share a controlled geometry. The DS18B20 is placed at the same depth as the active moisture-sensing region, approximately 20–30 mm away, without touching the moisture-probe board. A fixed jig controls depth, separation and cable strain. Ambient temperature may be recorded as context, but it cannot replace the soil measurement.

The designed firmware uses 12-bit conversion, obtains three readings and retains the median, checks known error values, and records temperature at the start and end of the acquisition interval. The actual implementation must also preserve sensor identity and timing so that a stale, disconnected or invalid reading cannot silently enter the model.

Including temperature in an equation does not prove temperature compensation. A useful result requires adequate equilibration, limited spatial gradients, valid sensor behavior and improved held-out error attributable to the temperature term or its interactions. The controlled package contains the design and proposed procedure, not a completed temperature calibration or measured compensation result.

## 08.8 Controlled salinity-treatment code

TrueMoist does not measure live salinity or electrical conductivity. Its salinity variable is known experimental metadata assigned from the batch-preparation record.

- **S0** means that no salt was deliberately added.
- **S1** means that one pilot-selected NaCl treatment was deliberately added.
- The actual S1 dose is frozen after pilot testing and recorded in grams of NaCl per kilogram of oven-dry-equivalent soil.
- The treatment state, exact dose, batch identifier and preparation record are supplied to offline model fitting and to fixed local inference.

The S1 pilot must identify a treatment that produces a repeatable effect greater than electronic noise without saturating the probe or creating uncontrolled physical changes. The dose may be adjusted once during the pilot under the defined gate. If no valid treatment can be established, the project may use the documented temperature-only fallback, but the scope reduction and resulting evidence limitation must be explicit.

The treatment code does not represent bulk-soil EC, apparent EC, pore-water EC, solution conductivity or a universal chemistry state. It cannot be described as an autonomous sensor channel. Outside the controlled prepared-batch experiment, the operational source of the code is unresolved. It may remain laboratory metadata or, in a later deployment concept, require user-supplied information. Chapter 08 does not resolve that future deployment question by inventing a live capability.

## 08.9 One-soil preparation and geometry controls

The semester architecture is restricted to one homogeneous soil and one controlled preparation method. This restriction is a validity control, not an inconvenience to be hidden. Different soil texture, organic content, density, mineral composition and salinity behavior can alter probe response; the present design does not support cross-soil transfer or universal calibration.

The planned physical preparation uses approximately 300–500 g of soil in a 500–1000 mL nonconductive container. The exact container, dry-soil mass and geometry are frozen after pilot work. Water is added by mass, mixed through one documented procedure and allowed to equilibrate under a defined sealed or covered condition. Salinity treatment is prepared from known mass records. Compaction is performed by a repeatable method rather than by subjective hand packing.

A fixed jig controls probe insertion depth, angle, separation from the DS18B20, container position and insertion path. Probe-board markings and sample identifiers provide visual confirmation. The operator records any void, tilt, unusual resistance, visible damage, incomplete mixing or departure from the procedure instead of silently correcting the record after measurement.

Packing and reinsertion are major error sources. Early trials must quantify whether independently prepared and packed samples vary less than the intended temperature or S1 disturbance. If packing variance dominates, the project must improve the jig, container, sample mass or compaction method before collecting the main dataset. Increasing model complexity is not an acceptable substitute for uncontrolled preparation.

## 08.10 Gravimetric reference method

The controlling physical reference is **dry-basis gravimetric water content**:

```text
GWC = (wet soil mass - dry soil mass) / dry soil mass
```

The planned constant-mass procedure is:

1. label the container and sample with a unique batch and replicate identifier;
2. tare the clean, dry container;
3. record wet soil plus container mass;
4. dry the sample at 105 ± 5 °C for at least 24 hours;
5. cool it in a dry, covered environment;
6. weigh the container and dry soil;
7. return the sample to the oven for a further 1–2 hours;
8. cool and reweigh;
9. accept constant mass only when the difference is within the chosen scale-based tolerance; and
10. calculate dry-basis GWC from the traceable wet and dry masses.

A 0.01 g scale is preferred. A 0.1 g scale may be usable only with sufficiently large samples and an explicit uncertainty calculation. Scale resolution, tare stability, container handling, cooling conditions and oven throughput are part of the evidence chain.

The project must not report volumetric water content unless bulk density or a controlled known-volume core is independently measured. Dry-basis GWC is the authoritative reference for the frozen design. Conversion by assumption would create an unsupported result.

Access to an appropriate oven, scale and constant-mass workflow is an entry gate. Purchase of a laboratory oven is outside the project budget. Without credible institutional or laboratory access, TrueMoist may remain a qualitative or conditional experiment, but final accuracy and error-reduction claims are prohibited.

## 08.11 Calibration and validation design

Training occurs offline in Python. The supported model ladder is deliberately simple so that the project tests compensation rather than hides physical weaknesses behind excessive model flexibility:

- **Model 0:** uncompensated univariate raw-probe calibration;
- **Model 1:** multivariate linear compensation using raw response, measured temperature and S0/S1 code;
- **Model 2:** ridge-regularized second-order candidate using selected quadratic and interaction terms.

Replicates 1 and 2 supply the model-development data. All repeated readings from one physical batch remain grouped. Model selection uses grouped cross-validation by physical batch and must preserve preparation independence. Replicate 3 remains untouched until the complete model form, features, coefficients, numerical scaling and pass criteria are frozen.

Model 2 may be selected only when it improves grouped held-out performance over Model 1, avoids unstable coefficients, preserves sensible monotonic behavior over the tested moisture range, does not materially worsen a major temperature or salinity subset and can be reproduced numerically on the MCU. Otherwise Model 1 is deployed.

After selection, the coefficients are fixed. The firmware evaluates the same frozen equation locally. Online coefficient changes, recursive self-learning, automatic runtime retraining and event-triggered adaptation are outside the semester architecture.

A valid analysis must preserve the distinction between model-development evidence and final evidence. Training fit, cross-validation performance and the untouched replicate should be reported separately. Any excluded run, corrected metadata item or deviation must be traceable to the physical ledger.

## 08.12 Uncompensated baseline

Model 0 is the controlling uncompensated comparison:

```text
GWC_hat_raw = a0 + a1 × raw
```

It maps the accepted raw probe statistic to estimated dry-basis GWC without temperature or treatment information. Its purpose is not merely to provide a weak straw model. It represents the ordinary calibration that the compensated architecture claims to improve.

The baseline and compensated methods must use the same physical records, reference values and held-out replicate. Relative improvement cannot be computed by comparing different samples, different preparation rules or differently filtered data. Absolute baseline RMSE and MAE must be reported so that a percentage improvement is not used to disguise large remaining errors.

The attached evidence defines the model form and comparison logic but contains no fitted `a0` or `a1`, no calibration curve and no measured baseline performance.

## 08.13 Compensated linear model

Model 1 is the first compensated method:

```text
GWC_hat_linear =
b0 + b1 × raw + b2 × temperature + b3 × salinity_code
```

The salinity term receives the known S0/S1 batch code. The temperature term receives the measured nearby soil temperature. Model 1 provides the main interpretable compensated baseline and is the required fallback when the second-order model does not show stable, meaningful benefit.

The model remains bounded to the tested soil, geometry, probe unit or documented unit configuration, temperature range, treatment range and preparation procedure. A coefficient attached to S1 is not a live conductivity calibration, and a coefficient attached to temperature does not imply general compensation outside the observed range.

No fitted `b` coefficients, feature scaling, measured residuals or held-out result are present in the controlled package.

## 08.14 Ridge second-order candidate

Model 2 is the most complex supported candidate:

```text
GWC_hat_comp =
c0
+ c1 × raw
+ c2 × T
+ c3 × S
+ c4 × raw²
+ c5 × T²
+ c6 × raw × T
+ c7 × raw × S
+ c8 × T × S
```

Ridge regularization is used to reduce coefficient instability. Terms may be removed when they are unstable, unsupported by the data or unnecessary for held-out performance. The architecture does not authorize adding an undisclosed equation, neural network, random forest, generic TinyML model or online learner merely to obtain a better training score.

The controlling selection rule requires Model 2 to improve held-out RMSE over Model 1 by at least 5%, preserve monotonic behavior over the tested moisture range, avoid unstable coefficients, avoid material worsening in either major salinity subset and reproduce offline output on the MCU. If those conditions are not met, Model 1 controls.

The equation defines a candidate family only. The attachments do not provide fitted `c` coefficients, the selected term set, regularization strength, scaling rules, statistical significance, residual plots or measured error reduction.

## 08.15 Error metrics and comparison criteria

The project uses error against dry-basis gravimetric GWC as its primary evidence. Improvement ratios are secondary to complete absolute reporting.

| Evidence item | Controlled criterion | Current evidence status |
|---|---|---|
| Primary metric | Held-out RMSE against gravimetric GWC | Defined as the principal metric; no measured value attached |
| Primary improvement criterion | Compensated held-out RMSE at least 20% lower than uncompensated RMSE | Proposed engineering pass criterion, not an achieved result |
| Secondary metric | Held-out MAE | Defined; no measured value attached |
| Secondary improvement criterion | Compensated held-out MAE at least 15% lower than uncompensated MAE | Proposed engineering pass criterion, not an achieved result |
| Subset guardrail | No more than 10% MAE worsening in a major tested temperature or salinity subset | Proposed guardrail; no subset result attached |
| Model 2 selection criterion | At least 5% RMSE improvement over Model 1 plus stability, monotonicity, subset and MCU-equivalence conditions | Proposed selection rule; no model-selection result attached |
| Absolute reporting | RMSE and MAE in the reference units must accompany percentage improvement | Required final reporting practice |
| R² | Supplementary only | Must not replace RMSE and MAE |
| Confidence procedure | Paired bootstrap interval or paired permutation test where feasible | Proposed analysis support; not completed |
| Calibration result | Separate from final test | Unavailable |
| Untouched replicate result | Final physical evidence | Unavailable |
| Simulated performance | No controlled simulation source exists | Unavailable and must not be invented |

Passing the proposed thresholds would support only the bounded conclusion that the compensated method improved error within the tested experimental configuration. It would not establish universal accuracy, field performance, patentability or FTO. Failing the thresholds would not invalidate the integrity of the project if the experiment was properly controlled and the negative result was reported.

## 08.16 Hardware architecture

The hardware is intentionally modest and measurement-focused.

| Element | Controlled role | Validation need |
|---|---|---|
| ESP32-WROOM-32 | Primary acquisition, fixed inference and USB logging controller | Purchased-board identity, pin map, ADC behavior and course acceptance |
| ESP32-S3 / STM32F401-class | Same-family fallback / conditional authorized platform alternative | Formal substitution and complete implementation revalidation |
| ADS1115 | Primary external ADC design | Same-node comparison with calibrated ESP32 ADC1 |
| Two genuine capacitive probes | One final-model unit; one spare/unit-variation unit | Authenticity, monotonicity, stability, reinsertion and unit variation |
| Waterproof DS18B20 | Nearby soil-temperature input | Placement, gradients, equilibration and error handling |
| Filtered analog path | Short, decoupled and eventually soldered measurement path | Documented values and noise/drift evidence |
| Containers and jig | Fix preparation and sensor geometry | Repeatability, cleaning, dimensions and revision control |
| USB 5 V power | Passive bench supply | Stable supply; no actuator load |
| Scale and oven access | Gravimetric reference infrastructure | Resolution, constant mass, availability and throughput |

No pump, relay, valve, motor, cloud connection or mandatory display belongs to the frozen hardware. Optional LEDs may indicate quality states but do not replace the USB and physical evidence records. Compute and memory are minor constraints; physical preparation, reference quality and throughput dominate.

## 08.17 Firmware and local-output architecture

Firmware is separated into configuration, probe acquisition, temperature acquisition, filtering, model evaluation, quality flags, logging and self-test. The versioned configuration must identify the board, probe, ADC path, acquisition rule, geometry revision, model and coefficient revision, valid ranges, batch and replicate.

During final acquisition, Wi-Fi and Bluetooth are disabled. The controller reads temperature and analog observations, forms the accepted raw statistic, evaluates Model 0 and the selected compensated model, applies approved quality rules and emits a versioned USB CSV record. Records should preserve the physical identifier, actual temperature, treatment metadata, raw statistic, dispersion, both estimates, model revision and quality flags. Optional LEDs or a host plot are presentation aids only.

Python-to-MCU numerical equivalence is a release gate. Fixed test vectors must reproduce the offline equation within the approved numerical tolerance before replicate 3 is processed. No completed equivalence report is attached.

## 08.18 BOM and budget evidence

The attached values are historical Phase 3C planning evidence, not current quotations.

| Item | Quantity | Historical planning range |
|---|---:|---:|
| ESP32 development board | 1 | ₹450–₹700 |
| ADS1115 module | 1 | ₹120–₹220 |
| Genuine analog capacitive probes | 2 | ₹300–₹600 |
| Waterproof DS18B20 | 1 | ₹120–₹220 |
| Perfboard, connectors, cables and passives | 1 set | ₹250–₹450 |
| Containers and jig materials | 1 set | ₹200–₹450 |
| Soil and salinity consumables | 1 set | ₹100–₹300 |
| Optional 0.01 g scale | 1 | ₹400–₹700 |
| Contingency | — | ₹250–₹500 |

Historical aggregate planning is approximately **₹1,790–₹3,440** when institutional scale and oven access are available. The preferred target is **≤₹3,000** and the absolute hardware ceiling is **₹5,000**. Buying a laboratory oven is outside the budget.

The embedded BOM may fit the student limit, but the reference method depends on institutional facilities. A later controlled stage must verify manufacturer specifications, authenticity, availability and current Indian prices before procurement or final publication.

## 08.19 Minimum demonstrable success

The frozen MVP reaches minimum demonstrable success only when the complete physical-to-digital chain is shown. It must:

1. acquire stable and interpretable raw analog probe output;
2. measure nearby soil temperature through a controlled geometry;
3. represent the known S0/S1 treatment rigorously from batch metadata;
4. produce the uncompensated Model 0 estimate;
5. produce the selected compensated estimate locally with fixed coefficients;
6. compare both estimates with the same traceable gravimetric GWC reference;
7. preserve independent physical replicates and prevent batch leakage;
8. demonstrate preregistered improvement on the untouched physical replicate while respecting subset guardrails;
9. reproduce the offline model numerically on the MCU;
10. preserve one-soil, tested-range and prepared-treatment limits; and
11. emit enough local evidence through USB CSV to reconstruct the result.

A live graph, a moisture percentage on a screen or a serial value that changes when water is added is not sufficient. Those demonstrations show responsiveness, not validated compensation. The project’s strongest evidence is the relationship among controlled preparation, gravimetric reference, grouped analysis and held-out local inference.

When the pass criteria are not met, the result must be described according to the failure mode. For example, the team may demonstrate a functional measurement chain but no compensation benefit; a valid one-soil dataset but inadequate held-out improvement; or a preparation system whose physical variance prevents model evaluation. These are different outcomes and should not be collapsed into a simple success/failure label.

## 08.20 Early validation gates

The architecture is classified as **Ready with Mandatory Early Validation**. Main data collection must not begin merely because the circuit operates.

### Week 1 gates

| Gate | Required evidence | Pass interpretation | Fallback or consequence |
|---|---|---|---|
| Probe authenticity and basic stability | Manufacturer/supplier identity where available, electrical inspection, warm-up record and fixed-sample observations | Probe behaves as a usable analog capacitive sensor | Inspect the second unit or replace the sensor |
| Monotonic pilot response | Ordered response across pilot moisture states | A calibration hypothesis is physically plausible | Reject or replace a non-monotonic or saturated unit |
| Reinsertion repeatability | Controlled repeated insertion using the jig | Reinsertion variation remains within the usable response span | Improve jig and procedure before factor testing |
| ADC paired comparison | Same analog node measured by ADS1115 and calibrated ESP32 ADC1 | Acquisition path selected by observed noise, drift and pilot error | Use calibrated ADC1 when ADS1115 adds no practical value |
| Gravimetric access | Confirm oven, scale, containers, constant-mass procedure and responsible access | Ground-truth path is feasible | Prohibit final accuracy claims until credible access exists |

### Week 2 gates

| Gate | Required evidence | Pass interpretation | Fallback or consequence |
|---|---|---|---|
| Packing sensitivity | Independently prepared samples show controlled variation | Preparation noise does not overwhelm the intended effects | Improve compaction, container, sample mass or jig; reduce scope if necessary |
| Temperature feasibility | Soil reaches safe, measurable and sufficiently uniform conditions | Three temperature states can be executed | Use the documented 20/28/36 °C fallback when justified |
| S1 feasibility | Pilot-selected dose creates a repeatable, non-saturating shift greater than electronic noise | S0/S1 factor is usable | Adjust once; otherwise use a transparent temperature-only fallback |
| Pilot grouped analysis | Preliminary comparison without physical-batch leakage | Measurement and reference chain is coherent enough to proceed | Repair preparation/reference problems before adding model complexity |
| Analog front end and jig freeze | Soldered path, controlled geometry and versioned procedure | Main dataset can begin under one stable configuration | Do not collect main data while hardware or geometry remains fluid |

Passing an early gate does not establish final accuracy. It only supports entry into the next evidence stage. Gate evidence must be archived even when it causes a sensor replacement or scope reduction.

## 08.21 Main experimental and held-out sequence

After authorization and early-gate passage, the intended sequence is:

1. freeze the probe, ADC path, controller, firmware, analog values, jig, containers, soil procedure and gravimetric method;
2. freeze the four moisture regions, three achievable temperatures and S1 dose from pilot evidence;
3. preregister run order or blocking, replicate preparation, identifiers, exclusions and the untouched-replicate boundary;
4. collect independent replicates 1 and 2 with matching preparation, acquisition and mass records;
5. audit identifiers, deviations, equilibration, reference quality and leakage risk;
6. fit Model 0 and Model 1 under grouped validation;
7. evaluate Model 2 under the complexity, stability, monotonicity and subset rules;
8. freeze the selected features, coefficients, valid range and firmware before accessing replicate 3;
9. prove Python-to-MCU numerical equivalence with fixed vectors;
10. process untouched replicate 3 without retuning;
11. report absolute RMSE/MAE, relative improvement, subset results, guardrails, exclusions, repeatability and drift; and
12. archive raw logs, mass sheets, run ledger, code, coefficients and configuration revisions.

Practical oven scheduling may require blocking, but factor levels must not become inseparable from time, drift or equipment state. No step in this sequence is proved complete by the controlled attachments.

## 08.22 Experimental, measurement and generalization risks

| Risk | Present state | Required control or interpretation |
|---|---|---|
| Probe authenticity and unit variation | Open | Characterize purchased units; do not infer population transfer |
| Warm-up, drift and reinsertion | Open | Freeze timing and geometry; report repeatability and drift |
| Packing and preparation | Open | Quantify independent preparation variance before main data collection |
| ADC path | Open | Select by paired ADS1115/ESP32 ADC1 evidence, not nominal resolution |
| Temperature gradients | Open | Use same-depth placement, controlled spacing and equilibration checks |
| S1 treatment | Open | Pilot and freeze a repeatable non-saturating dose in g/kg dry soil |
| Gravimetric access | Open | Confirm scale, oven and constant-mass workflow before accuracy claims |
| Drying throughput | Open | Trial the workflow; use formal change control for any run reduction |
| Data leakage | Controlled by design, not audited | Group by physical batch and preserve untouched replicate 3 |
| Model overfit | Open | Use grouped validation, ridge control, monotonicity and linear fallback |
| Python/MCU mismatch | Open | Complete fixed-vector equivalence before final testing |
| Treatment-code deployment | Unresolved | Keep S0/S1 as laboratory metadata; no autonomous field claim |
| One-soil limitation | Fixed | Report only within the tested soil, range and preparation |
| Current parts and prices | Unverified | Conduct later manufacturer and market verification |

The dominant uncertainties are metrology, preparation and throughput, not compute. A weak physical reference cannot be repaired by a more complex model.

## 08.23 Allowed refinements

The following changes remain within the frozen TrueMoist identity when formally documented:

- selecting an electrically characterized genuine analog capacitive probe equivalent to the reference class;
- using the second unit as a spare or for unit-variation characterization;
- retaining ADS1115 or selecting calibrated ESP32 ADC1 according to the paired gate;
- using ESP32-S3 as the same-family controller fallback;
- using an STM32F401-class board only after an explicit authorized platform and toolchain decision;
- adjusting the exact four moisture targets after pilot characterization while retaining four controlled levels;
- using the documented 20/28/36 °C temperature fallback when the higher condition is unsafe or nonuniform;
- freezing the exact S1 NaCl dose after the controlled pilot;
- improving wiring, decoupling, shielding, perfboard layout, connectors, jig, container geometry or sample-control procedure;
- removing unstable Model 2 terms;
- selecting Model 1 when Model 2 does not satisfy the complexity gate;
- adding sensor-failure, missing-metadata and range flags;
- adding optional local LEDs or a host-side plot; and
- using the 54-run contingency only through explicit change control and transparent evidence reduction.

A refinement must preserve the local one-soil compensation question and the same physical reference. Changes that add a new sensing principle, automatic chemistry estimation, actuation, cloud dependency or runtime learning create a different architecture and require a new decision record.

## 08.24 Prohibited substitutions and overclaims

The following substitutions and statements are outside the controlled design:

- using YL-69/HL-69 as though it were the selected corrosion-resistant capacitive probe;
- describing S0/S1 metadata as live EC or conductivity measurement;
- claiming autonomous salinity estimation or compensation for unknown field chemistry;
- adding irrigation advice, pumps, relays or valve control;
- converting the project into cloud analytics, remote-farm telemetry or a mobile-app platform;
- requiring TinyML, a neural network or an undisclosed advanced model;
- adding online, recursive or event-triggered coefficient adaptation to the MVP;
- replacing the commodity probe with custom impedance or multi-frequency hardware;
- claiming universal, calibration-free, multi-soil or field-wide performance;
- reporting laboratory-grade accuracy or production agronomic readiness;
- reporting volumetric water content without independent bulk-density evidence;
- treating rapid electronic observations as independent physical samples;
- claiming that the 72-run design was executed without a physical run ledger;
- reporting RMSE, MAE, accuracy or error reduction without results;
- treating ADS1115 as superior solely because of nominal resolution;
- treating two probes as proof of transferable calibration or lifecycle health;
- presenting generic Mahalanobis, OOD, confidence or abstention logic as verified novelty;
- describing the ordinary MVP as patent-ready, likely patentable or cleared for FTO;
- claiming teacher approval, final semester selection, Phase 4 entry or procurement authorization without an explicit controlling record; or
- describing a TrueMoist pre-build simulation that does not exist.

## 08.25 Current implementation and approval status

TrueMoist is a retained Phase 3C architecture. Its final architecture, memory and SOP provide a coherent design and implementation sequence, but concept-level readiness does not equal project authorization.

The current controlled state is:

- TrueMoist is neither finally selected nor finally rejected;
- VibeGuard is the strongest semester-build recommendation in both final adjudications;
- the proposed OpenBraille-to-VibeGuard change is not proved teacher-approved;
- the exact course platform remains unresolved despite ESP32 being frozen in the concept architecture and STM32 appearing in the broader teacher context;
- project-wide Phase 4 entry and procurement are not proved authorized;
- no completed TrueMoist build, 72-run dataset or held-out result is attached; and
- no frozen MVP is established as patentable.

The final TrueMoist memory’s concept-level instruction to proceed toward implementation is interpreted as architecture readiness within the concept. It does not override the current Decision Register or validated Part I on teacher approval, final selection, platform acceptance or procurement.

## 08.26 Ordinary MVP patent position

The ordinary frozen MVP has strong engineering, experimental and publication value. It is not, on the controlled evidence, a credible independent patent nucleus.

The following elements are treated by the valid syntheses as conventional or insufficient by themselves:

- commodity capacitive soil-moisture sensing;
- nearby temperature measurement;
- known salinity-treatment metadata;
- RC filtering, decoupling and an external ADC;
- low-order linear, polynomial or ridge regression;
- offline training and fixed embedded coefficients;
- gravimetric reference measurement;
- grouped one-soil validation;
- USB CSV logging;
- the 72-run factorial arrangement;
- low cost; and
- omission of live EC.

A specific list of commodity parts and experimental parameters may be textually distinctive without producing an inventive technical interaction. Failure to find one document that copies every detail is not proof of useful novelty.

> **NO CURRENT FILING COMMITMENT**
>
> The controlled TrueMoist record does not establish:
>
> - confirmed novelty;
> - inventive step;
> - patent eligibility;
> - a useful independent claim;
> - filing approval;
> - infringement clearance;
> - freedom to operate; or
> - probable patent grant.
>
> The ordinary semester MVP should proceed, if authorized, as an engineering and measurement project. Any later filing decision requires direct physical evidence, a frozen future mechanism, current primary-source prior-art verification, official legal-status review, institutional IPR control and professional claim analysis.

The allowed conclusion is that the ordinary MVP has low current patent value and no patent-first readiness. This is a conservative technical and evidentiary assessment, not a binding legal declaration that every possible claim is unpatentable.

## 08.27 Controlled patent-research evidence

The controlled patent record contains six research lanes and two valid syntheses. Lanes are evidence sources, not votes, and were audited for concept fidelity, source quality, claim support, legal-status limits and unsupported certainty.

| Lane | Reconciled reliability | Retained value and limitation |
|---|---|---|
| ChatGPT Deep Research | High with legal-status caveats | Strong concept fidelity and conservative Track-C direction; official national status work remains incomplete |
| Gemini | Medium-low | Recognizes the conventional MVP and transfer/validity problem; autonomous-actuation drift and novelty/FTO overclaims are excluded |
| Perplexity — partial | Medium | Useful literature and patent leads; mandatory family, status and claim work is incomplete |
| Qwen compilation | Low-medium | Useful future-topic inventory; treated as one lane and stripped of clear-FTO/novelty claims |
| Mistral | Low | Supports the conventional-MVP conclusion; legal concepts and future novelty are overstated |
| Microsoft Copilot | Low-medium | Useful terminology; unsupported semester-feasibility, novelty and clearance claims are excluded |

The stronger common position is that temperature, treatment, packing and unit variation are real physical problems; the frozen stack is scientifically useful but patent-weak; and transfer or validity is a more relevant future question than ordinary regression. Generic Mahalanobis/OOD gating, abstention alone, omission of live EC, two probes, event recalibration and any `HIGH` or `CLEAR` FTO statement are not retained as verified patent conclusions. The Patent Evidence Index controls the six-lane set; a supplementary audit outside that set is not an extra vote.

## 08.28 Valid synthesis conclusions

The two valid syntheses materially agree on the ordinary MVP while using slightly different language for the strongest future direction.

### Max synthesis

`03_CONCEPT_PORTFOLIO/TrueMoist/03_Patent_Synthesis/01_TrueMoist_Patent_Evidence_Synthesis_Max.md` assigns **Track C** and describes a credible long-term path requiring later-semester extension. It gives medium confidence to the track classification and low-to-medium confidence that a useful claim would survive complete search and experiment. It treats the frozen MVP as a coherent engineering experiment without a credible independent technical nucleus. Its strongest future hypothesis is contamination-protected replacement-probe transfer coupled to perturbation-conditioned validity and abstention or fallback. It recommends retaining TrueMoist as a strong semester prototype while reducing patent priority.

### High + Deep Research synthesis

`03_CONCEPT_PORTFOLIO/TrueMoist/03_Patent_Synthesis/02_TrueMoist_Patent_Evidence_Synthesis_High_Deep_Research.md` also assigns **Track C**, with medium confidence. It describes the frozen architecture as high in engineering and scientific value, low in current patent value and not patent-first ready. Its strongest future hypothesis is a physical-reference-bound calibration-transfer and validity-acceptance method for replacement or remounted commodity probes. It likewise recommends retaining the semester prototype while reducing patent priority.

The syntheses are not votes and their agreement does not prove the future hypothesis. Their role is to establish a controlled research position: execute the ordinary MVP without patent-driven scope expansion; treat any two-probe transfer exercise as feasibility work; and advance filing-related work only after stronger multi-unit evidence and refreshed legal review.

## 08.29 Comparative adjudication context

The comparative record gives TrueMoist a distinctive strength: among the retained concepts, it has the most explicit quantitative validation architecture and substantial measurement or publication value. Its burden is also distinctive. Oven and scale access, drying throughput, probe repeatability, packing control, treatment preparation and early acquisition gates can determine feasibility before firmware sophistication matters.

Both final adjudications identify VibeGuard as the strongest semester-build recommendation. That common recommendation does not reject TrueMoist. It reflects a comparison of semester execution risk, demonstration clarity, team alignment and experimental burden.

The adjudications diverge on the later patent-development route:

- **Work Max** identifies TrueMoist as the best presently evidenced post-MVP patent-development candidate and fallback after its proposed VibeGuard signal-and-access gate.
- **Deep Research High** deprioritizes TrueMoist for the current patent-first choice, preserving it as a rigorous engineering and publication project while conditionally preferring an OpenBraille D11 route after a separate gate.

No higher authority resolves this disagreement. The manual therefore preserves both conditional positions rather than averaging them. TrueMoist cannot be described as the preferred patent route, the rejected patent route, the final semester choice or a teacher-approved build.

## 08.30 Future replacement, remount, transfer and validity hypothesis

The strongest supported future direction is separate from the frozen semester MVP. Its candidate sequence is:

1. bind donor calibration, probe identity and measurement provenance to a controlled configuration;
2. obtain sparse trusted physical reference responses when a commodity probe is replaced or remounted;
3. derive a bounded transfer mapping from the donor configuration to the replacement or remounted configuration;
4. challenge the mapping under controlled moisture, temperature, S0/S1, packing, remount and contamination perturbations;
5. analyze residual behavior to distinguish unit bias from real moisture change, treatment or temperature disturbance, packing/remount error, contamination, electronic offset or degradation;
6. accept transferred coefficients only when the physical challenge establishes a valid transfer state;
7. prevent contaminated or untrusted reference events from updating calibration; and
8. abstain or use a safe fallback when validity cannot be established.

This sequence is a **candidate research hypothesis**, not an implemented invention. Its broad components are crowded. The potentially differentiating question is whether the physical-reference-bound interaction creates a non-additive and materially superior result compared with simple alternatives.

The required simple baselines include donor-coefficient reuse, one-point transfer, two-point affine transfer, pooled calibration, full per-probe calibration, simple range checks, generic distance or confidence gates, unrestricted update, no update and the critical component ablations. If the complete mechanism does not outperform two-point affine transfer plus a simple range gate on independent physical data, the strongest hypothesis fails.

The second probe in the semester BOM can support only an exploratory feasibility study. It cannot establish transfer across a population, manufacturing lots, ageing states or field conditions. A successful 72-run Level-1 compensation result is a prerequisite for sensible Level-2 work, not evidence that Level 2 already exists.

## 08.31 No-pre-build-simulation boundary

No TrueMoist pre-build simulation exists in the controlled source set. The concept directory record states that the validated design resides under `01_Final_Architecture` and that the pre-build simulation directory is empty.

Accordingly:

- no simulation result may be reconstructed from a synthesis, research lane or future experiment plan;
- no later mechanism may be described as having passed a pre-build simulation;
- no hypothetical transfer, validity or recalibration result may be inserted into the evidence register; and
- the empty directory is an intentional no-file state in the evidence presented, not proof that an expected result was accidentally omitted.

TrueMoist differs from the concepts that possess controlled pre-build simulation documents. Its future research path is supported only as a conditional hypothesis derived from audited patent evidence and comparative reasoning.

## 08.32 Experimental evidence required for the future hypothesis

A credible later transfer-and-validity programme would require evidence beyond the two-month Level-1 design and beyond the present two-probe BOM. At minimum, it would need:

- several commodity probes, preferably **6–12 units** across at least two manufacturing lots where feasible;
- a defined donor-calibration procedure and blinded replacement or remount assignments;
- sparse trusted physical anchors with traceable gravimetric reference;
- repeated remounting under controlled depth, angle, packing and container changes;
- temperature and S0/S1 perturbations separated from probe-unit effects;
- contamination challenges and rules that prevent contaminated reference events from updating the mapping;
- ageing or drift proxies with dated, repeated observations;
- independent test groups not used to define the transfer or validity rule;
- comparison with naive reuse, one-point transfer, two-point affine transfer, pooled calibration and full per-probe calibration;
- comparison with always-report, simple range-gate, generic distance-gate, no-update and unrestricted-update policies;
- claim-specific ablations that remove transfer mapping, physical challenges, contamination control, validity acceptance and fallback one at a time;
- reporting of transfer RMSE, MAE, bias, severe accepted-error rate and calibration workload; and
- evidence that any improvement is not produced by one conventional component alone.

A two-probe one-soil pilot may estimate effect size, workload and procedural difficulty. It must be labelled exploratory. It cannot support general transfer, lifecycle health, multi-lot robustness, field reliability or a patent-ready claim.

The future direction should be killed or substantially revised when its advantage disappears against simple affine transfer and range gating, when one component explains all apparent benefit, when results depend on repeated electronic samples rather than independent physical challenges, or when the physical-reference burden makes the mechanism impractical.

## 08.33 Prior-art and legal-status limitations

The controlled patent research is useful for technical direction but incomplete as a legal foundation.

- Public database status labels are not official legal opinions.
- Indian, Chinese, European national-state and PCT national-stage details remain incomplete.
- No professional claim construction was performed.
- No search of unpublished applications is possible from the attached record.
- Litigation, licensing, prosecution history and commercial practice were not comprehensively reviewed.
- Target countries, products and commercial acts are not fixed.
- Expired or abandoned records may remain prior art even when they do not create present exclusion rights.
- Failure to locate an exact duplicate does not establish novelty or clearance.
- Academic prototyping is not a universal infringement exemption.

Before claim-dependent design freeze or filing, the exact mechanism would require refreshed primary-source searches, family consolidation, jurisdiction-specific claim charts, official register verification, professional translation where necessary and institutional or qualified-counsel review.

## 08.34 Freedom-to-operate boundary

Freedom to operate is different from patentability. A project may contain a patentable improvement and still fall within another party’s active claim; it may also be unpatentable while remaining free to practice because the relevant rights expired or do not cover the intended acts. The controlled research does not resolve either question.

FTO depends on the exact product or method, claim wording, territory, legal status and commercial acts. The current record does not fix a commercialization configuration, target jurisdiction or claim construction. Statements such as `LOW`, `CLEAR`, `relatively clear` or “no direct infringement identified” are therefore excluded as clearance conclusions.

No filing, commercialization or public deployment decision should rely on the present research as FTO advice. Jurisdiction-specific professional analysis is required after the actual mechanism and intended use are frozen.

## 08.35 Confidentiality, contribution and institutional IPR control

The ordinary semester design may be discussed at a general educational level: low-cost capacitive probes, temperature and treatment effects, low-order regression, gravimetric calibration and the planned 72-run one-soil experiment.

Pending institutional IPR review, claim-focused future details should remain controlled, including:

- exact physical-reference challenge sequences;
- probe fingerprints and transfer mappings;
- validity-envelope definitions;
- contamination gates;
- remount acceptance logic;
- lifecycle or degradation features;
- coefficient and provenance binding;
- detailed parameter values;
- labelled transfer, remount, contamination and ageing datasets;
- code, negative results and ablations; and
- invention chronology and contribution records.

The team should maintain dated laboratory notebooks, version-control history, test authorship, code contributions, design decisions and human interpretation records. AI and literature outputs are background evidence; they do not establish human inventorship. Institutional rules on ownership, inventorship, assignment, disclosure, publication timing and student contribution remain unresolved and require written guidance.

## 08.36 File/no-file decision gate

The current patent decision is **no filing commitment**. A later TrueMoist mechanism may enter institutional or professional file/no-file review only when the following conditions are met:

1. the Level-1 measurement chain and gravimetric method are physically credible;
2. the exact Level-2 mechanism is frozen rather than described as a collection of generic ideas;
3. multi-unit and, where feasible, multi-lot experiments are complete;
4. simple transfer and validity baselines are directly outperformed on independent physical data;
5. critical ablations show that the proposed interaction—not one conventional component—creates the effect;
6. negative results, accepted-error rates, calibration workload and failure states are preserved;
7. refreshed primary-source prior-art and claim searching retains a meaningful difference;
8. official legal-status and jurisdiction-specific FTO work is complete enough for the intended decision;
9. institutional confidentiality, ownership and inventorship requirements are satisfied; and
10. the authorized IPR body or qualified professional recommends proceeding.

Failure at an early physical or baseline gate should stop claim-focused escalation. The team may still publish or present the engineering result subject to institutional rules, but it must not use a patent filing to compensate for weak experimental evidence.

## 08.37 Current patent-development state

TrueMoist currently occupies a controlled **Track-C** position. The semester architecture is coherent, affordable at the historical planning level and capable of producing rigorous measurement evidence if the physical gates are passed. Its ordinary components and their straightforward combination are not established as a patent-first invention.

The replacement/remount transfer and physical-validity sequence is the strongest retained future hypothesis. It remains unimplemented, unsimulated, unverified against complete prior art and unsupported by the multi-unit evidence needed for a credible file/no-file decision.

The comparative portfolio does not resolve whether TrueMoist should become the later patent-development priority. Work Max conditionally favors it; Deep Research High conditionally favors another route. The governing project state preserves that disagreement.

The controlled current statement is therefore:

> TrueMoist should be retained as a rigorous semester engineering and publication path. Its ordinary MVP has low current patent value and no filing commitment. A later physical-reference-bound transfer-and-validity mechanism may be investigated confidentially after Level-1 success, but it must survive multi-unit experiments, simple baselines, ablations, refreshed prior-art review and institutional IPR control before any filing decision.

## 08.38 Chapter conclusion

TrueMoist is a disciplined local compensation experiment, not a general agricultural platform. Its frozen semester architecture combines one genuine analog capacitive probe, nearby soil-temperature measurement, known S0/S1 prepared-batch metadata, an evidence-gated ADC path, an ESP32-class controller, offline fitting, fixed local inference, USB CSV evidence and dry-basis gravimetric reference.

Its strongest design feature is not algorithmic complexity. It is the planned separation of physical factors, independent preparation, leakage-controlled model development and untouched held-out validation. The authoritative 72-run structure provides a credible framework, but the controlled attachments do not prove execution, fitted coefficients or measured improvement.

TrueMoist remains retained but not finally selected or rejected. VibeGuard remains the strongest semester-build recommendation, and project-wide approval, platform choice, Phase 4 and procurement remain open. The ordinary TrueMoist MVP has high engineering and scientific value but low current patent value. Replacement/remount transfer and physical validity remain post-semester hypotheses without a pre-build simulation or filing commitment.

A technically honest TrueMoist result will depend on the quality of the physical reference, probe and preparation controls, not on promotional claims. The project should proceed only through the defined gates, preserve negative evidence and keep future claim-focused work under institutional control.

## 08.S Source notes

Material conclusions in Chapter 08 are tied to original organized-workspace sources, not to the packet or reconciliation filenames. TIER_1 controls architecture and project state; TIER_2 controls audited patent and comparative evidence; TIER_3 lanes provide supporting research only. Exact paths and roles are consolidated in the Part IV Source Ledger below. The manifest is file control only.

# Part IV Evidence-Status Register

| Evidence item | Design, proposed, completed or unavailable | Controlling source | Allowed conclusion |
|---|---|---|---|
| Frozen TrueMoist identity | Current controlled design | Final architecture, memory and SOP (**TIER_1**) | TrueMoist is a one-soil local compensation experiment with fixed local inference |
| DS18B20 role | Current design | Final architecture (**TIER_1**) | Nearby measured soil temperature is a compensation input |
| S0/S1 treatment code | Current design with pilot-selected S1 dose | Final architecture and memory (**TIER_1**) | Known prepared-batch metadata may be used; no live EC claim |
| ADS1115 architecture | Primary design subject to evidence gate | Final architecture and memory (**TIER_1**) | External ADC is comparison-gated, not inherently authoritative |
| ESP32 controller | Current concept design | Final architecture (**TIER_1**) | Local fixed-coefficient inference is the selected path; course acceptance remains open |
| 72-run factorial | Current authoritative experimental design | Final architecture and memory (**TIER_1**) | Target is 4 × 3 × 2 × 3 independent physical runs |
| Complete 72-run execution | Unavailable | No completed physical dataset or run ledger in the controlled source set | Do not claim completion |
| Independent run definition | Current experimental control | Final architecture and SOP (**TIER_1**) | Rapid electronic readings from one condition are not independent runs |
| Training/model-selection split | Current design | Final architecture (**TIER_1**) | Replicates 1–2 are for development; replicate 3 remains untouched |
| Gravimetric GWC method | Planned controlling reference procedure | Final architecture (**TIER_1**) | Dry-basis GWC is the required physical reference |
| Oven and scale access | Unavailable as completed facility evidence | Final architecture and memory (**TIER_1**) | Accuracy claims remain conditional on credible access and constant mass |
| Model 0 | Current supported model specification | Final architecture (**TIER_1**) | Uncompensated univariate baseline may be described |
| Model 1 | Current supported model specification | Final architecture (**TIER_1**) | Multivariate linear compensation may be described |
| Model 2 | Proposed supported candidate with selection gate | Final architecture (**TIER_1**) | Ridge second-order model may be evaluated conditionally |
| Fitted coefficients | Unavailable | No result source | Do not invent or publish coefficients |
| Python-to-MCU equivalence | Required test, not completed | Final architecture and SOP (**TIER_1**) | Equivalence is a release gate; no passing result exists |
| RMSE criterion | Proposed project criterion | Final architecture (**TIER_1**) | May state 20% held-out improvement as a target only |
| MAE criterion | Proposed project criterion | Final architecture (**TIER_1**) | May state 15% held-out improvement as a target only |
| Subset guardrail | Proposed project criterion | Final architecture (**TIER_1**) | May state no more than 10% MAE worsening as a guardrail only |
| Model 2 complexity gate | Proposed selection rule | Final architecture (**TIER_1**) | Model 2 requires at least 5% RMSE benefit plus stability and equivalence conditions |
| Measured RMSE/MAE improvement | Unavailable | No completed result source | Do not claim performance |
| Probe/ADC/packing gates | Designed; completion unavailable | Final architecture and memory (**TIER_1**) | Architecture is ready only with mandatory early validation |
| Historical BOM | Completed planning estimate, not current market evidence | Final architecture and memory (**TIER_1**) | Historical ₹1,790–₹3,440 range may be reported with date/status limitations |
| Current specifications and prices | Unavailable in this stage | Authority protocol and governing instruction | Later manufacturer and market verification is required |
| TrueMoist implementation approval | Unresolved | Decision Register and validated Part I (**TIER_1**) | Do not claim teacher approval or final selection |
| Project-wide Phase 4/procurement | Unresolved and not authorized by the attached record | Decision Register and validated Part I (**TIER_1**) | Do not begin or claim authorization |
| Patent research | Completed document research | Valid syntheses and controlled lanes (**TIER_2/3**) | Supports a cautious technical position, not legal clearance |
| Ordinary MVP patent value | Reconciled research conclusion | Valid syntheses (**TIER_2**) | High engineering value, low current patent value and no patent-first readiness |
| Future transfer/validity mechanism | Proposed research hypothesis | Valid syntheses (**TIER_2**) | May be described conditionally and separately from the MVP |
| Multi-unit Level-2 evidence | Unavailable | No completed future experiment source | Do not claim transfer, remount validity, contamination control or lifecycle performance |
| TrueMoist pre-build simulation | No file | TrueMoist README (**TIER_2**) | No simulation evidence exists and none may be reconstructed |
| Comparative semester ranking | Completed decision support | Final adjudications and validated Part I (**TIER_2/TIER_1 representation**) | VibeGuard is the strongest recommendation; this is not teacher approval |
| Preferred future patent route | Conflicting completed decision support | Two final adjudications (**TIER_2**) | Preserve disagreement; do not average it |
| Patentability, eligibility and novelty | Unavailable as legal conclusions | Valid syntheses and authority protocol | No confirmed conclusion may be stated |
| Freedom to operate | Unavailable | Valid syntheses and authority protocol | Jurisdiction-specific professional review is required |
| Institutional ownership/inventorship rules | Unavailable | Valid syntheses (**TIER_2**) | Obtain written institutional IPR guidance before claim-focused disclosure |

# Part IV Open-Decision Register

| ID | Decision or uncertainty | Current status | Controlling source | Required next action |
|---|---|---|---|---|
| TM-OD-01 | Final semester concept selection | Unresolved; TrueMoist retained, VibeGuard recommended | Decision Register and validated Part I (**TIER_1**) | Record explicit authorized concept selection |
| TM-OD-02 | Teacher approval of the proposed OpenBraille-to-VibeGuard shift | Not proved | Validated Part I (**TIER_1**) | Obtain and record explicit teacher decision |
| TM-OD-03 | ESP32 or STM32 course-platform acceptance | Unresolved | Teacher context, Decision Register and validated Part I (**TIER_1**) | Obtain written course/platform confirmation |
| TM-OD-04 | Project-wide Phase 4 entry | Not authorized by the attached record | Decision Register and validated Part I (**TIER_1**) | Enter Phase 4 only after recorded authorization |
| TM-OD-05 | Procurement freeze | Not authorized; current prices unverified | Validated Part I and authority protocol (**TIER_1/control**) | Verify current parts/prices and approve BOM before purchase |
| TM-OD-06 | Purchased probe authenticity | Open | Final architecture and memory (**TIER_1**) | Verify identity, coating and analog behavior; reject unsuitable units |
| TM-OD-08 | Reinsertion repeatability | Open | Final architecture and memory (**TIER_1**) | Perform controlled repeated insertion using the frozen jig |
| TM-OD-09 | Final analog acquisition path | Open comparison gate | Final architecture and memory (**TIER_1**) | Compare ADS1115 and calibrated ESP32 ADC1 on the same node |
| TM-OD-10 | Oven, scale and constant-mass access | Unconfirmed | Final architecture and memory (**TIER_1**) | Confirm facility, responsible access, resolution and throughput |
| TM-OD-11 | Final soil and preparation procedure | Pilot-dependent | Final architecture and SOP (**TIER_1**) | Freeze homogeneous soil, masses, container, mixing, equilibration and compaction |
| TM-OD-12 | Exact four moisture target regions | Open until pilot | Final architecture (**TIER_1**) | Freeze targets after soil field-capacity and probe-response characterization |
| TM-OD-14 | Exact S1 NaCl dose | Open until pilot | Final architecture and memory (**TIER_1**) | Select and freeze a repeatable non-saturating dose in g/kg dry soil |
| TM-OD-15 | Packing sensitivity | Open | Final architecture and memory (**TIER_1**) | Quantify independent preparation variance and improve controls if necessary |
| TM-OD-16 | Run order and blocking plan | Incomplete | Final architecture/reconciliation (**TIER_1**) | Preregister randomization/blocking and deviation handling |
| TM-OD-17 | Feasibility of the full 72-run schedule | Unproved | Final architecture and memory (**TIER_1**) | Trial physical throughput before freezing the execution calendar |
| TM-OD-18 | Use of 54-run contingency | Not authorized | Final architecture and reconciliation (**TIER_1**) | Apply formal change control and report reduced evidence if required |
| TM-OD-19 | Completion of main dataset | Not proved started or completed | No completed source | Execute with complete physical run ledger and identifiers |
| TM-OD-22 | Final model choice | Unresolved | Final architecture (**TIER_1**) | Freeze M1 or M2 before opening replicate 3 |
| TM-OD-23 | Python-to-MCU numerical equivalence | Open | Final architecture and SOP (**TIER_1**) | Run fixed-vector equivalence tests and archive results |
| TM-OD-24 | Untouched replicate-3 validation | Not performed in attached evidence | Final architecture (**TIER_1**) | Test only after complete model and firmware freeze |
| TM-OD-25 | Measured RMSE, MAE and subset performance | Unavailable | No completed result source | Report absolute and relative metrics after held-out testing |
| TM-OD-26 | Drift and repeatability reporting | Open | Final architecture and SOP (**TIER_1**) | Define and execute repeatability/drift observations |
| TM-OD-27 | Operational meaning of S0/S1 outside the laboratory | Unresolved | Final architecture plus valid syntheses (**TIER_1/2**) | Keep as laboratory metadata unless a later authorized deployment design defines the input |
| TM-OD-29 | Current component specifications and Indian prices | Unverified in this stage | Authority protocol and governing instruction | Conduct a later controlled manufacturer/supplier verification pass |
| TM-OD-30 | Exact future replacement/remount mechanism | Unfrozen hypothesis | Valid syntheses (**TIER_2**) | Define only after Level-1 feasibility and confidential institutional review |
| TM-OD-31 | Multi-unit and multi-lot Level-2 experiment | Not designed as an authorized programme | Valid syntheses (**TIER_2**) | Develop a separate approved budget, sample plan and evidence protocol |
| TM-OD-32 | Whether the future mechanism beats simple affine transfer and gating | Unknown | Valid syntheses (**TIER_2**) | Run independent baseline and ablation comparisons |
| TM-OD-33 | Current patent-family legal status | Incomplete | Valid syntheses and controlled lanes (**TIER_2/3**) | Refresh official registers and family data for the exact mechanism |
| TM-OD-34 | Jurisdiction-specific FTO | Unavailable | Authority protocol and valid syntheses | Freeze intended acts/territories and obtain professional claim analysis |
| TM-OD-35 | Institutional confidentiality, ownership and inventorship rules | Unresolved | Valid syntheses (**TIER_2**) | Obtain written institutional IPR guidance before claim-focused disclosure |
| TM-OD-36 | Preferred future patent-development concept | Adjudications disagree | Final adjudications (**TIER_2**) | Apply an authorized gate and new physical evidence; preserve disagreement until resolved |

# Part IV Contradiction Summary

| ID | Issue | Controlling resolution | Residual uncertainty |
|---|---|---|---|
| TM-C01 | Historical self-correcting/adaptive platform versus fixed offline-trained MVP | Final architecture, memory and SOP control: fixed coefficients and local inference; adaptive updating is future only | Whether a trusted-event update mechanism is technically viable later |
| TM-C02 | Live EC sensing versus controlled salinity-treatment code | Known S0/S1 prepared-batch metadata controls; no live EC or autonomous chemistry measurement | Operational source of the code outside the controlled experiment |
| TM-C03 | YL-69/HL-69 presented as the selected capacitive sensor | Genuine analog capacitive probe controls; resistive YL-69/HL-69 is rejected as primary sensor | Authenticity and behavior of purchased units |
| TM-C04 | 72 runs versus research-lane plans for 135 or 180 samples | Authoritative target is 72 independent physical runs | Throughput and whether later change control is necessary |
| TM-C05 | Internal ADC by default versus external ADC mandatory | ADS1115 is primary but comparison-gated against calibrated ESP32 ADC1 | Paired physical gate result |
| TM-C06 | Volumetric water content versus dry-basis gravimetric water content | GWC controls; VWC requires independent bulk-density evidence | Whether bulk density will ever be measured |
| TM-C07 | “Architecture Ready” versus unconditional readiness | Correct status is Architecture Ready with Mandatory Early Validation | Outcomes of probe, ADC, packing, treatment and reference gates |
| TM-C08 | “Validated 72-run design” read as completed experiment | Validation refers to architecture selection; physical completion and results are unproved | Actual run ledger, dataset and result report |
| TM-C09 | Ordinary MVP framed as a patent opportunity versus conventional engineering stack | Valid syntheses control under patent-evidence role: high engineering value, low current patent value | Whether a later exact mechanism survives experiment and prior art |
| TM-C10 | Generic OOD, Mahalanobis, confidence or abstention framed as novelty | Generic statistical gating is not verified novelty; only a specific physical interaction may be studied | Whether the composite physical-reference-bound mechanism produces a non-additive effect |
| TM-C11 | Final memory says proceed to Phase 4 versus current project authorization | Concept-level architecture readiness does not override Decision Register/Part I; project-wide Phase 4 remains open | Teacher, concept and platform authorization |
| TM-C12 | Two-month semester path versus three-month patent-extension proposals | Two-month Level-1 MVP controls; Level-2 extension is separate conditional research | Actual authorized future schedule and budget |
| TM-C13 | TrueMoist preferred as future patent path versus deprioritized patent-first route | No higher resolution; preserve both adjudications without averaging | Authorized future gate and new evidence |
| TM-C14 | TrueMoist described as finally selected or rejected | Retained Phase 3C concept; neither selection nor rejection is proved | Explicit teacher/final concept decision |

# Part IV Source Ledger

Only original organized-workspace paths materially relied upon are listed. The attachment manifest is file control only and is not technical evidence. The attached Chapter 08 packet and reconciliation are not listed as substitutes for the original sources.

## TIER_1 — Current architecture and project authority

### Frozen TrueMoist architecture

- `03_CONCEPT_PORTFOLIO/TrueMoist/01_Final_Architecture/Phase3C_TrueMoist_Architecture_Report_Final.md` — controlling hardware, acquisition, model, dataset, metrics, BOM, risks and readiness.
- `03_CONCEPT_PORTFOLIO/TrueMoist/01_Final_Architecture/Phase3C_TrueMoist_Memory_Final.md` — compact frozen architecture, exclusions, early gates and fallbacks.
- `03_CONCEPT_PORTFOLIO/TrueMoist/01_Final_Architecture/Phase3C_TrueMoist_SOP_Final.md` — canonical identity, evidence-quality rules, anti-drift controls, validation stages and exit conditions.

### Project and approval state

- `01_GOVERNANCE_AND_CONTROL/01_Project_Requirements/Teacher_Project_Requirements_and_Change_Context.md` — teacher constraints and approval boundary.
- `01_GOVERNANCE_AND_CONTROL/02_Decision_Registers/Project_mC_Decision_Register_v1.2.md` — canonical project decisions and retained-concept state.
- `01_GOVERNANCE_AND_CONTROL/AUTHORITY_MAP.md` — project authority control used by validated Part I.

## TIER_2 — Controlled decision and patent evidence

### Valid TrueMoist syntheses

- `03_CONCEPT_PORTFOLIO/TrueMoist/03_Patent_Synthesis/01_TrueMoist_Patent_Evidence_Synthesis_Max.md` — Track-C assessment, ordinary-MVP patent position and future composite transfer/validity hypothesis.
- `03_CONCEPT_PORTFOLIO/TrueMoist/03_Patent_Synthesis/02_TrueMoist_Patent_Evidence_Synthesis_High_Deep_Research.md` — audited lane reliability, patent limitations, physical-reference-bound transfer hypothesis and recommendation.

### TrueMoist evidence-control records

- `03_CONCEPT_PORTFOLIO/TrueMoist/PATENT_EVIDENCE_INDEX.md` — controlled six-lane set, two valid syntheses and excluded supplementary audit.
- `03_CONCEPT_PORTFOLIO/TrueMoist/README.md` — frozen-architecture location and no-pre-build-simulation boundary.

### Comparative evidence and adjudications

- `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/00_Engineering_Design_Review.md` — concept identity and comparative engineering boundary.
- `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/04_Hard_Gate_Precheck.md` — neutral gate context.
- `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/05_Uncertainty_and_Test_Register.md` — current unresolved tests and evidence gaps.
- `04_COMPARATIVE_DECISION/02_Final_Adjudications/01_Project_mC_Final_Adjudication_Work_Max.md` — VibeGuard semester recommendation and conditional TrueMoist future route.
- `04_COMPARATIVE_DECISION/02_Final_Adjudications/02_Project_mC_Final_Adjudication_Deep_Research_High.md` — VibeGuard semester recommendation and conditional OpenBraille-first future route.
- `04_COMPARATIVE_DECISION/COMPARATIVE_DECISION_INDEX.md` — adjudications controlled as decision context rather than votes.

### Historical supporting record

- `03_CONCEPT_PORTFOLIO/TrueMoist/05_Roadmaps_and_Reference_Dossiers/HISTORICAL_Phase1C_TrueMoist_Concept_Dossier.docx` — historical origin and adaptive/self-correcting aspirations only; superseded where inconsistent with the frozen architecture.

## TIER_3 — Controlled independent research lanes

- `03_CONCEPT_PORTFOLIO/TrueMoist/02_Raw_Research/01_TrueMoist_Patent_Research_ChatGPT_Deep_Research.md`
- `03_CONCEPT_PORTFOLIO/TrueMoist/02_Raw_Research/02_TrueMoist_Patent_Research_Gemini.docx`
- `03_CONCEPT_PORTFOLIO/TrueMoist/02_Raw_Research/03_TrueMoist_Patent_Research_Perplexity_PARTIAL.md`
- `03_CONCEPT_PORTFOLIO/TrueMoist/02_Raw_Research/04_TrueMoist_Patent_Research_Qwen_COMPILATION.md`
- `03_CONCEPT_PORTFOLIO/TrueMoist/02_Raw_Research/05_TrueMoist_Patent_Research_Mistral.md`
- `03_CONCEPT_PORTFOLIO/TrueMoist/02_Raw_Research/06_TrueMoist_Patent_Research_Microsoft_Copilot.docx`

These lanes are supporting evidence only. Their recurring assertions do not establish truth. Unsupported, overconfident or concept-swapped conclusions are excluded rather than averaged into the controlled position.

<!-- END CONTROLLED COMPONENT: PART_IV -->

---

<!-- BEGIN CONTROLLED COMPONENT: PART_V -->
<!-- SOURCE PATH: /home/paradoxpete/Documents/PROJECT_ORGANIZED/08_MASTER_MANUAL/03_Drafting_Workspace/01_Validated_Parts/Part_V/Project_mC_Master_Manual_Part_V_Teacher_Review_and_Semester_Execution.md -->
<!-- SOURCE SHA-256: 19811337e31915f53449191bd5728aec3f2f5dc06fc6f7c8b579224ae870404f -->

## Part V — Teacher Review and Semester Execution

## Document control

| Field | Value |
|---|---|
| Document | Project mC Master Manual — Part V |
| Controlled filename | `Project_mC_Master_Manual_Part_V_Teacher_Review_and_Semester_Execution.md` |
| Status | Controlled draft |
| Scope | Chapters 10 and 11 plus Part V approval, execution-control, contradiction and source registers |
| Input inventory | Exactly 13 physical Markdown attachments were present and readable. The 12 externally hash-controlled files matched the manifest byte counts and SHA-256 values; the self-referential manifest was used only for file control. |
| Source boundary | Only the attached Part V drafting package was used. No prior-chat context, memory, web research or unstated external assumption was used. |
| Approval effect | Not a teacher-approval record |
| Execution effect | Not Phase 4, procurement or implementation authorization |
| Chapter 11 evidence state | Zero directly mapped sources; future framework only |
| Patent effect | No patentability, filing, infringement or freedom-to-operate conclusion |
| External verification | Reserved for a later controlled stage |

The Part V drafting package passed its manifest control. The governing instruction, authority and contradiction protocol, Master Manual blueprint, validated Parts I–IV, validated teacher/execution reconciliation, Chapter 10 evidence packet, Chapter 11 zero-source packet, visual and boundary-control record, required template and manifest were present and readable. Filename transport suffixes did not create duplicate logical sources because the controlled files matched the manifest identities. The manifest is not used as technical evidence.

## How to read Part V

Part V records two related but different subjects. Chapter 10 preserves what Project mC prepared and submitted for teacher-facing review, how that material developed, which later support documents were created, and which decisions remain unrecorded. Chapter 11 defines the controls that would be required to execute one authorized semester concept. Chapter 10 therefore concerns presentation and review history; Chapter 11 concerns a conditional future execution system.

Five distinctions govern the reading of both chapters.

**Proposal is not approval.** A presentation, roadmap, recommendation, adjudication or change request can show what the team proposed and why. It cannot prove that the teacher or course authority accepted the proposal. Approval exists only when an explicit controlling decision record states it.

**Presentation is not architecture authority.** The official OpenBraille deck controls the identity of the submitted zeroth-review presentation. It does not replace the final OpenBraille architecture, memory and SOP controlled in Part II. The same principle applies across the portfolio: validated Parts II–IV control the current technical identities and claim boundaries of OpenBraille, VibeGuard and TrueMoist.

**Recommendation is not an authorized concept.** Comparative evidence supports VibeGuard as the strongest semester-build recommendation, and a formal request proposed replacing the OpenBraille semester implementation with VibeGuard. The present package does not prove that the shift was approved. OpenBraille, VibeGuard and TrueMoist therefore remain legitimate controlled records, while the final semester concept remains unresolved.

**A framework is not completed execution.** Chapter 11 has no directly mapped Tier 1–4 execution records. Its gates, role structure, milestones, validation controls and fallback rules define what would be required after authorization. They must not be read as a history of purchases, fabrication, coding, testing, demonstration or completion.

**Historical planning evidence is not current procurement evidence.** Earlier prices, power values, component labels and schedule estimates may explain how a proposal was framed. Final purchasing requires a later controlled check of the exact authorized platform, current manufacturer specifications, Indian prices, supplier authenticity, delivery, facility access and approved budget.

# Chapter 10 — Teacher Reviews and Presentation Record

## 10.1 Chapter purpose and evidence boundary

This chapter preserves the teacher-facing record of Project mC while protecting the boundary between submission, review, approval and execution. Its direct mapped evidence consists of fifteen controlled teacher/review sources: the teacher-delivery index; the official OpenBraille zeroth-review presentation; eight earlier presentation drafts or working files; two historical visual files; two internal presentation-instruction hubs; and the teacher/review index.

The chapter establishes the following matters:

- the identity of the official OpenBraille zeroth-review submission;
- the content and scope that the team presented on 30 July 2026;
- the relationship between that presentation and the later frozen OpenBraille architecture;
- the development trail from early drafts to the official deck;
- the role of internal authoring and hardware-audit instructions;
- the existence and intended use of later teacher-facing support documents;
- the formal proposal to shift the semester implementation from OpenBraille to VibeGuard; and
- the controlled disposition of the two historical PNG visuals.

The same evidence does **not** establish that the zeroth review was delivered, that comments were issued, that OpenBraille was approved, that the VibeGuard shift was accepted, that ESP32 or STM32 was authorized, that procurement began, that a physical prototype was built, or that validation or patent filing was completed. No teacher comment sheet, marked rubric, signed decision, approval email, meeting minute or equivalent outcome record appears in the package.

Chapter 10 therefore functions as a presentation and decision-boundary record. It documents what the team placed before the teacher and what later request was prepared, while refusing to infer a result that the source set does not contain.

## 10.2 Teacher requirements and review context

The teacher-facing material belongs to a B.Tech CSE Cyber Security microcontroller semester project undertaken by a five-member team. Current requirements and approval state are controlled by validated Part I, not by presentation wording or lower-authority roadmaps.

| Requirement or context | Controlled Part V treatment |
|---|---|
| Academic setting | B.Tech CSE Cyber Security microcontroller semester project |
| Team size | Five members |
| Time boundary | Teacher context permits up to three months; approximately two months is the stricter internal feasibility baseline. The final calendar remains open. |
| Budget | Preferred total at or below ₹3,000; absolute hardware ceiling ₹5,000. Historical concept estimates are not current quotations. |
| Platform | Arduino-board or Arduino-IDE-compatible embedded implementation is required. |
| STM32 context | STM32 was mentioned, but no categorical board decision is attached. |
| Cybersecurity fit | Preferred in the project context, not recorded as an absolute final-selection rule that overrides all other gates. |
| Power | Low-power components are required; very high-power components are not permitted. |
| Interface and evidence | A USB sample, interface or logging path should be included. |
| Demonstration | A strong live demonstration is required, but no successful demonstration is proved by the present record. |

The official deck is labelled “Micro Project — Zeroth Review” and dated 30 July 2026. That label identifies the intended review stage and the official presentation file. It does not establish a teacher response. The absence of a response record matters because later project work produced a different semester-build recommendation. Without an explicit decision, the official OpenBraille presentation and the later VibeGuard request must coexist in the manual as distinct historical and current-decision records.

## 10.3 Official zeroth-review presentation identity

The controlling official presentation record is:

`05_TEACHER_AND_REVIEWS/02_Zeroth_Review_OpenBraille/01_Official_Submission/OpenBraille_Zeroth_Review_OFFICIAL_2026-07-30.pptx`

Its controlled SHA-256 identity is:

`8503780624e86aaabe94e67d90ce565633bea3f66ec018d27fc5d104ec0e5c9e`

| Field | Official presentation record |
|---|---|
| Course | `PBCST504 – MICROCONTROLLERS` |
| Review label | `MICRO PROJECT — Zeroth Review` |
| Date shown | 30 July 2026 |
| Topic | `Affordable Refreshable Single-Cell Braille Display` |
| Project title | `OpenBraille: Affordable Refreshable Single-Cell Braille Display` |
| Group | Group 8 |
| Members | Amith Krishna Das — JEC24CC016; Archa Pramod — JEC24CC22; Nihad P C — JEC24CC044; Sreehari K — JEC24CC055; Sreeprada K S — JEC24CC056 |
| Project coordinator shown | Ms. Sagna L T, Asst. Prof. CSE(CY) |
| Slide count | 16 |
| Institutional section | Department Vision, Mission, PEOs, POs and PSOs in Slides 3–8 |
| Technical section | Contents, motivation, introduction, problem statement, proposed method, basic block diagram, conclusion and references |

Only this dated `OFFICIAL` file controls the submitted deck identity. The earlier templates, drafts, alternate-format files and pre-submission versions explain the preparation history but are not substitutes for the official submission. Repository ordering is not treated as an independently verified creation-time sequence unless a date is directly supported.

The official presentation proves that OpenBraille was the subject selected for the zeroth-review submission. It does not prove that OpenBraille was finally authorized after the review. Later comparative evidence and a formal change request must therefore be recorded without rewriting the 30 July presentation history.

## 10.4 What the presentation proposed

The presentation framed OpenBraille as a bounded assistive-technology prototype proposal. It did not report a completed product or a validated device.

The motivation section described commercial refreshable Braille systems as expensive because their actuation and manufacturing demand precision. It connected tactile Braille to literacy and access, particularly in schools, libraries and resource-constrained institutions. This gave the project a social and educational problem context rather than merely presenting a mechanical novelty exercise.

The proposed semester objective was narrower than the broad product title. The team proposed testing whether readily available electromechanical components could create refreshable tactile output in one six-dot cell. The cell was intentionally macro-scaled so that ordinary FDM printing could be used without pretending that the semester prototype met commercial Braille-cell geometry.

The proposed mechanism used six SG90-class positional micro servos, one for each dot, with eccentric cams moving tactile pins. An ESP32-WROOM-32 was shown as the controller producing six separate servo-control signals. The deck included a text or USB input path and an external 5 V servo-power concept with common ground. A 1,000 µF bulk capacitor was described as planned, while the historical diagram included a provisional 2 A supply value.

The presentation also proposed a practical fabrication and commissioning strategy. College FDM printing and readily available components were expected to support the macro-scale build. Development would begin with one dot, establish basic motion, and only then proceed to all six channels. This single-dot-first sequence remains compatible with the current frozen architecture, although the deck itself contains no evidence that the gate was executed.

A historical bill-of-materials estimate of ₹2,060–₹2,850 was reported, subject to part prices and design changes. That range is part of the presentation record. It is not a current supplier quotation, approved purchase total or actual spend.

The conclusion and future direction allowed later exploration of multi-cell work and possible intellectual-property options after experiments. Such language is retained only as future exploration. Multi-cell development is outside the frozen semester architecture, and the source set does not establish novelty, inventive step, patent eligibility, filing authorization or freedom to operate.

## 10.5 OpenBraille architecture as presented

The official presentation and the later frozen architecture share the same high-level concept, but they do not have equal technical authority. The presentation records the teacher-facing explanation. Validated Part II controls the exact current OpenBraille identity, mandatory safeguards and claim boundary.

| Architecture point | Teacher-facing presentation | Current controlled position |
|---|---|---|
| Cell form | One macro-scaled six-dot cell | One permanent, non-standard macro six-dot tactile cell |
| Actuation | Six SG90-class servos | Six SG90-class servos, one actuator per dot |
| Motion conversion | Eccentric cams move tactile pins | Six eccentric cam/follower channels with guided vertical pins and safe rounded tips |
| Controller | ESP32-WROOM-32 | ESP32-WROOM-32-class controller, subject to course acceptance and purchased-board verification |
| Servo control | Six separate servo-control signals | Six direct PWM signal channels; controller signals do not power the servo motors |
| Power | External 5 V line, common ground and planned capacitor | External regulated servo-power branch with measured current headroom, shared electrical reference ground and evidence-selected capacitance |
| Return motion | General up-and-down movement | Active servo-driven raise and retract positions are mandatory unless coupled passive assistance is physically proved |
| Input and evidence | Text/USB path | USB/serial command input and evidence logging |
| Build sequence | One-dot-first, then six dots | Mandatory single-dot-first commissioning before six-channel integration |
| Product status | Affordable refreshable single-cell Braille display framing | Educational non-standard macro tactile/mechanical proof-of-concept; not a commercial or ISO-compliant display |

The active-retraction rule is particularly important. The presentation’s general statement that cams produce up-and-down movement does not establish a reliable reset mechanism. The controlled architecture requires the servo and cam system to command both raise and retract motion. Gravity, elasticity or an internal servo effect may assist, but no passive-return assumption controls unless the procured, fully coupled channel proves repeatable return under the intended load.

The macro scale is also a permanent feature of the frozen semester architecture, not merely an early mock-up that may be reported as commercial geometry. It is a deliberate fabrication strategy for an educational proof-of-concept. Any later practical-scale or multi-cell work would be a separate configuration requiring new authorization and evidence.

The architecture boundary preserves the value of the presentation without allowing historical simplifications to override engineering controls. Chapter 10 may describe what was shown; technical execution must use the Part II architecture lock.

## 10.6 Presentation claims requiring qualification

The official deck was designed for a zeroth review and therefore used short, accessible language. In the Master Manual, several phrases require a more exact interpretation.

| Presentation wording or implication | Controlled qualification |
|---|---|
| “Refreshable Braille display” | Retain as the historical project title. The controlled technical description is a non-standard macro single-cell tactile/mechanical proof-of-concept, not a commercial display or fluent-reading device. |
| “Usable tactile Braille” as a hypothesis | Unproved. Tactile distinguishability requires an approved blinded protocol; no user-validation result is attached. |
| ISO 17049:2013 reference | Dimensional context only. The macro cell must not be described as ISO-compliant. |
| Six-servo up/down motion | Does not prove reliable reset. Active raise and retract control remains mandatory until physical evidence proves otherwise. |
| External 5 V, provisional 2 A and 1,000 µF capacitor | Historical planning values only. Current, droop, reset, stall, heating, conductor capacity and capacitance require staged measurement. |
| ESP32-WROOM-32 selection | Part of the frozen concept identity, but final course acceptance of ESP32 versus an authorized STM32 substitution remains open. |
| ₹2,060–₹2,850 estimate | Dated planning evidence, not a current Indian quotation, procurement total or actual spend. |
| One-dot-to-six-dot plan | A valid proposed commissioning sequence; no gate execution is proved. |
| Multi-cell future work | Outside semester scope and subject to a new configuration, budget and authorization. |
| Possible IP options | Future exploration only; no patentability, filing or FTO conclusion. |
| Official submission status | Proves the submitted deck identity, not teacher approval, review outcome or implementation. |

The internal presentation-instruction hubs reinforce this cautious treatment. They directed the authors to rely on controlled project sources, retain the required institutional slide structure, audit hardware claims and prepare speakers. They also prohibited unsupported price-heavy statements, over-precise repeatability claims presented as results, declarations that risks had been eliminated, and patent-guarantee language.

Those instruction files are evidence of internal quality control. They are not teacher feedback. Their significance is that the official deck emerged from a documented correction process that attempted to separate planned values from demonstrated facts.

## 10.7 Teacher-facing support documents and roadmaps

The teacher-delivery index identifies a compact set of canonical teacher-facing documents. It points to the editable and rendered OpenBraille-to-VibeGuard change request, the VibeGuard semester implementation and future-research roadmap, the OpenBraille retained-reference dossier and the official OpenBraille zeroth-review presentation.

| Document class | Proper teacher-facing role | Boundary |
|---|---|---|
| OpenBraille-to-VibeGuard change request | Presents the formal request, rationale and proposed decision | A request only; the attached record does not contain teacher acceptance, conditional approval or rejection |
| VibeGuard roadmap | Defines a conditional path for the frozen VibeGuard Level-1 architecture | Becomes an implementation plan only after concept, platform and scope approval |
| OpenBraille retained-reference dossier | Preserves a coherent accessibility/mechatronics fallback and future reference | Does not prove that OpenBraille remains or ceases to be the authorized build |
| Official zeroth-review deck | Records the submitted OpenBraille presentation | Does not prove construction, validation or review outcome |
| Presentation instruction hubs | Internal authoring, hardware-audit and speaker-preparation guidance | Working material, not teacher feedback or technical authority |
| Teacher/review indexes | Navigation, official-versus-draft separation and exclusions | Do not independently establish approval or technical truth |

This structure supports a decision-consistent teacher pack. Before a final decision, the change request and both concept references may explain the options. After a decision, only the approved implementation document should be described as controlling, while the other concept remains clearly labelled as fallback, retained reference or historical material.

The indexes also protect the evidence set from unrelated or non-authoritative files. They separate the official deck from the draft folder and exclude unrelated presentations, scripts, virtual-environment content, office lock files and coursework from Project mC teacher-review evidence.

## 10.8 Proposed OpenBraille-to-VibeGuard shift

Later comparative work changed the project’s recommended semester direction without erasing the OpenBraille review history. Both final adjudications support VibeGuard as the strongest semester-build candidate. The recorded reasons include a simpler physical architecture, stronger alignment with the team’s embedded and signal-processing capabilities, clearer quantitative bench validation, a recoverable live demonstration and lower dependence on precision FDM mechanics, coupled six-servo power behavior and tactile evaluation.

A formal request dated 3 August 2026 proposed replacing the OpenBraille semester implementation with the frozen VibeGuard Level-1 architecture. The request preserved OpenBraille as documented accessibility/mechatronics work and as a possible future project rather than treating the earlier work as invalid or fraudulent.

The exact current decision state is:

- **Current fact:** VibeGuard is the strongest semester-build recommendation.
- **Current fact:** A formal OpenBraille-to-VibeGuard change request exists.
- **Current fact:** OpenBraille remains a legitimate controlled architecture and retained body of work.
- **Open decision:** No explicit teacher approval, conditional approval or rejection of the shift is attached.
- **Required future action:** Preserve a written teacher decision, including conditions and date, before VibeGuard is treated as the authorized build or procurement is frozen.
- **Prohibited claim:** The manual must not state that “the project was changed to VibeGuard” or that “the teacher approved VibeGuard” from the present evidence.

The semester recommendation must also remain separate from the future patent-development decision. The two final adjudications agree that VibeGuard is the strongest semester option but disagree on the preferred first future patent gate. Part V therefore records semester preference without declaring a patent winner.

## 10.9 Approval and unresolved-decision boundary

> **PART V APPROVAL-STATUS BOX**
>
> **What is proved:** The official OpenBraille zeroth-review deck exists; VibeGuard is the strongest semester-build recommendation; a formal request proposed the OpenBraille-to-VibeGuard shift; all three retained concepts have controlled architectures.
>
> **What is not proved:** No attached record establishes teacher feedback on the zeroth review, approval of OpenBraille after review, approval of the VibeGuard shift, a final authorized concept, ESP32 or STM32 course acceptance, project-wide Phase 4 entry, procurement, named role assignments, completed build work, quantitative validation, successful demonstration or patent-filing authorization.
>
> **Control rule:** Only an explicit higher-authority decision or direct execution record may change these states. Presentation files, roadmaps, recommendations, repository placement and model agreement do not substitute for approval.

| Item | Current supported state | Classification |
|---|---|---|
| Official OpenBraille zeroth-review deck | Present | **CURRENT FACT** |
| Teacher feedback from zeroth review | Not attached | **MISSING RECORD / OPEN** |
| Teacher approval of OpenBraille after review | Not attached | **OPEN DECISION** |
| Formal request to change to VibeGuard | Present in the controlled project record | **CURRENT FACT** |
| Teacher approval of VibeGuard shift | Not attached | **OPEN DECISION** |
| Final semester concept | Not conclusively authorized | **OPEN DECISION** |
| ESP32 or STM32 platform acceptance | Unresolved | **OPEN DECISION** |
| Project-wide Phase 4 entry | Not proved | **OPEN DECISION** |
| Procurement and current BOM freeze | Not established | **OPEN DECISION** |
| Named primary/reviewer/backup ownership | Proposed only | **OPEN DECISION** |
| Completed build or validation | No direct completed record | **PROHIBITED CLAIM** |
| Patent readiness or filing authorization | Not established | **PROHIBITED CLAIM** |

The teacher-review narrative closes at this boundary. Part V does not infer approval from the official appearance of a deck, from the existence of a delivery index, from the consistency of two adjudications, or from a roadmap labelled implementation-ready.

## 10.10 Draft and working-file provenance

The presentation package preserves a controlled development trail. The file numbering establishes repository order; it does not independently prove exact creation times.

| Repository order | Working source | Treatment |
|---:|---|---|
| 1 | `01_Initial_Template_or_Early_Draft.pptx` | Early template or draft; historical only |
| 2 | `02_OpenBraille_Draft_0.1.pptx` | Historical draft revision |
| 3 | `03_OpenBraille_Draft_0.2.pptx` | Historical draft revision |
| 4 | `04_OpenBraille_Draft_0.2.odp` | Historical alternate-format draft |
| 5 | `05_Sreehari_Working_Draft.pptx` | Working draft containing price-heavy and over-precise material later targeted for correction |
| 6 | `06_Group8_Working_Draft.pptx` | Historical group working draft |
| 7 | `07_PreSubmission_Finalised_Draft_1.pptx` | Pre-submission revision; not official |
| 8 | `08_PreSubmission_Finalised_Draft_2.pptx` | Later pre-submission revision; not official |
| 9 | `09_OpenBraille_Block_Diagram.png` | Historical working/presentation diagram; limited use |
| 10 | `10_OpenBraille_Generated_Visual.png` | Generated working visual; provenance only |
| 11 | `11_Presentation_Instructions_Early.html` | Internal authoring and audit guidance |
| 12 | `12_Presentation_Instructions_2.0.html` | Revised internal authoring and audit guidance |
| Official | `OpenBraille_Zeroth_Review_OFFICIAL_2026-07-30.pptx` | Controlling submitted deck |

The instruction hubs coordinated presentation production, hardware auditing and speaker preparation. They preserved the sixteen-slide institutional structure, directed authors toward the Decision Register, Engineering Design Review and final OpenBraille architecture, and discouraged raw-model research from appearing as slide fact. Their presence documents disciplined preparation, but no teacher comment or acceptance may be inferred from them.

The provenance trail is retained because it shows how unsupported or overconfident wording was progressively corrected. It is not retained to multiply evidence: eight drafts do not count as eight independent validations, and two publication formats of the same content do not create independent corroboration.

## 10.11 Resolved visual-review record

The two historical PNG items were directly inspected under SHA-256 control before Part V drafting. Their disposition is final for this manual stage. Neither visual overrides validated Part II.

### 10.11.1 Historical OpenBraille block diagram

The original source is:

`05_TEACHER_AND_REVIEWS/02_Zeroth_Review_OpenBraille/02_Drafts_and_Working_Files/09_OpenBraille_Block_Diagram.png`

Its controlled identity is `d9203a9b237b35005df2ee3d58f0ea5761186c65b9cf5466843b6af1faaf0d48`, and its recorded dimensions are 2752 × 1536. The disposition is **historical context only**.

The diagram communicates a high-level path from text or USB serial input to ESP32-WROOM-32 lookup and PWM control, six control signals, six SG90-class servos, six cam-and-follower mechanisms, six tactile pins and one macro-scale cell. It also shows an external 5 V supply, servo rail, common ground, a 1,000 µF bulk capacitor and a 2 A value marked provisional.

The diagram may be described as evidence of what the teacher-review working material communicated. It must not be used to prove teacher approval, physical implementation, multi-servo power adequacy, active-retraction performance, final wiring, current capacity, current component specifications or current prices.

### 10.11.2 Generated OpenBraille visual

The original source is:

`05_TEACHER_AND_REVIEWS/02_Zeroth_Review_OpenBraille/02_Drafts_and_Working_Files/10_OpenBraille_Generated_Visual.png`

Its controlled identity is `e34d60d0250848dd9099b2d2e27bb3e2d302677f813331f592b3becf21f8eb3c`, and its recorded dimensions are 1536 × 1024. The disposition is **exclude from technical and final-figure use**.

The image presents a simplified text-input, Unicode-conversion, ESP32/PWM, servo-cam and six-dot path with a 5 V/2 A supply and common ground. Direct visual review found a large transparent area that may render black, malformed or placeholder text, and simplified illustrative relationships.

The visual may remain in provenance as an example of generated presentation-working material. It must not be reproduced as a final technical figure or cited for an exact capacitor value, final power design, mechanical geometry, architecture authority, implementation status, teacher approval or validated performance.

## 10.12 Review chronology

The defensible teacher-review chronology is document-based rather than outcome-based.

1. **Draft-development period — exact dates not established in this package.** The repository preserves an early template, Draft 0.1, two Draft 0.2 formats, individual and group working drafts, and two pre-submission revisions.
2. **Internal correction and audit period — exact dates not established in this package.** Two instruction hubs guided slide production, hardware verification, source selection and speaker preparation. They required conservative handling of price, standards, reset motion, power, repeatability and patent language.
3. **30 July 2026 — official zeroth-review submission identity.** The sixteen-slide OpenBraille file is the official submitted deck.
4. **3 August 2026 — formal proposed shift.** The controlled project record requested a change from OpenBraille to VibeGuard while retaining OpenBraille as documented fallback and future reference work.
5. **4 August 2026 — visual and source-boundary control.** The two PNG items were directly reviewed under hash control; Chapter 10 was confirmed to have fifteen mapped sources and Chapter 11 zero mapped sources.

This chronology proves document evolution and the existence of a later request. It does not prove when teacher feedback occurred, whether the zeroth review was accepted, whether the change request was approved, or whether implementation began.

## 10.13 Current teacher-facing state

The current teacher-facing state can be summarized without prejudging the missing decision.

OpenBraille remains the historical zeroth-review subject and a valid retained architecture. The official deck provides a concise record of the proposed macro six-servo concept, but any technical implementation description must now follow validated Part II, including active retraction, staged power validation, single-dot-first commissioning and a strict non-commercial claim boundary.

VibeGuard is the strongest semester-build recommendation. The teacher-facing package includes a formal change request and a conditional VibeGuard roadmap. These documents provide a reasoned basis for a decision; they do not supply the decision itself.

TrueMoist remains a legitimate retained architecture and controlled alternative, although the Chapter 10 packet contains no direct teacher-review presentation for it. Its status is neither selected nor rejected.

The next teacher-facing record should therefore capture one explicit outcome: approval of VibeGuard, retention or reauthorization of OpenBraille, authorization of TrueMoist, a conditional comparison gate, or rejection of the present options with a new recorded direction. The same record should resolve the course platform and any conditions that must be met before procurement or Phase 4.

Until that record exists, the proper teacher-facing language is “recommended,” “requested,” “retained,” “conditional” and “open.” The words “approved,” “selected,” “started,” “built” and “validated” remain unsupported.

## 10.14 Chapter conclusion

Chapter 10 preserves a coherent and auditable teacher-review history. The official OpenBraille presentation dated 30 July 2026 is the controlling record of the zeroth-review submission. Earlier drafts and instruction hubs explain the development and correction process. The historical block diagram is retained only as contextual presentation evidence, while the generated visual is excluded from technical and final-figure use.

Later comparative work supports VibeGuard as the strongest semester-build recommendation, and a formal request dated 3 August 2026 proposed the shift while preserving OpenBraille. The present package does not contain the teacher’s decision. It also does not establish course-platform acceptance, procurement, Phase 4, completed implementation, validation, demonstration or patent authorization.

The chapter therefore ends with an explicit separation: Project mC has a controlled presentation record and a well-supported recommendation, but its final semester authorization remains open.

## 10.S Source notes

Chapter 10 relies materially on the original organized-workspace teacher/review paths listed in the Part V Source Ledger. The official submission path controls what was submitted. Draft and working-file paths establish provenance only. The teacher-delivery index and teacher/review index provide navigation and decision boundaries. The two visuals are used only according to the direct visual-review disposition. Current architecture and approval statements are controlled by the original governance, comparative-decision and final architecture paths listed for validated Parts I–IV, not by the packet filenames.

# Chapter 11 — Semester Execution Framework

## 11.1 Chapter purpose and zero-source boundary

> **CHAPTER 11 ZERO-SOURCE BOUNDARY**
>
> The controlled Chapter 11 source packet contains **zero directly mapped Tier 1–4 execution sources**. The complete source-map review recorded no hash failure and no extraction or copy error. The absence is therefore a genuine evidence state, not a missing-file problem.
>
> Chapter 11 is a **future controlled semester-execution framework only**. It may define authorization gates, purchasing controls, roles, build stages, validation rules, safety requirements, milestones, fallback procedures and record-change controls. It must not imply that any of those actions have already occurred.

This chapter converts the current project state and the three frozen concept architectures into a disciplined execution system that may be activated only after authorization. It is assembled from the current approval and comparative state in Part I, the concept-specific implementation boundaries in Parts II–IV, the authority and contradiction protocol, the teacher-facing evidence in Chapter 10, and the explicit zero-source limitation.

The purpose is not to predict success. It is to prevent ambiguous project status, premature purchase, concept mixing, unreviewed platform changes, uncontrolled testing, unsafe demonstration and unsupported performance claims. The framework is designed so that a full success, partial result or negative result can all be reported honestly and reproducibly.

Throughout this chapter, words such as **required**, **planned**, **proposed**, **conditional**, **open** and **future** indicate controls that would apply after authorization. They are not statements of completion.

## 11.2 Current authorization state

The current project state supports planning but not execution claims.

| Execution question | Current state | Control consequence |
|---|---|---|
| Is VibeGuard the strongest semester-build recommendation? | Yes | It is the preferred branch for decision-making, not yet an authorized build. |
| Has the teacher approved the OpenBraille-to-VibeGuard shift? | Not proved | The shift must remain described as proposed. |
| Has one final semester concept been authorized? | Not conclusively recorded | No branch may be represented as selected. |
| Has ESP32 or STM32 been accepted for the course? | Unresolved | Exact board-specific procurement and final design remain blocked. |
| Has project-wide Phase 4 begun? | Not proved | No Phase 4 progress claim is permitted. |
| Has procurement begun or a current BOM been frozen? | Not proved | Historical cost layers remain planning evidence only. |
| Have named owners, reviewers and backups been assigned? | Not proved | The role framework remains proposed. |
| Has any concept been physically built or validated? | No completed execution record is mapped | Build and performance claims are prohibited. |
| Is any frozen MVP established as patentable? | No | Patentability, filing and FTO claims are prohibited. |

The first controlled execution act must be the creation of an authorization record. Buying components, writing exploratory code or preparing CAD may occur only as explicitly authorized preliminary work and must not be represented as project-wide Phase 4. No lower-authority roadmap or concept memory can silently open the execution stage.

The authorization record should identify the concept, exact scope, platform, budget boundary, permitted facilities, public-disclosure boundary and any conditions imposed by the teacher or course authority. If authorization is conditional, each condition should be converted into a gate with a responsible owner and evidence requirement.

## 11.3 Concept and course-platform decision gate

Execution begins with two linked decisions.

### Gate E0 — Final concept authorization

A controlling teacher or project record must select one of the following outcomes:

1. authorize the frozen VibeGuard Level-1 semester build;
2. retain or reauthorize the frozen OpenBraille macro six-servo build;
3. authorize the frozen TrueMoist one-soil compensation experiment;
4. approve a time-bounded conditional gate process before final selection; or
5. reject the present options and require a new formally documented decision.

The decision must name the concept in its frozen form. OpenBraille, VibeGuard and TrueMoist may not be blended into a hybrid because different parts appear convenient. A new hybrid, replacement mechanism or concept substitution requires a new architecture record and explicit authorization.

### Gate E1 — Course-platform acceptance

The course authority must confirm the exact controller path. The frozen concepts use ESP32-class controllers, but the teacher context also mentions STM32. Neither fact by itself settles academic acceptance.

An approved platform record should include:

- exact board family and purchased-board identity;
- Arduino IDE, Arduino-core or other permitted toolchain;
- USB interface and driver requirements;
- voltage levels, pin restrictions and power assumptions;
- timer, PWM, SPI, ADC or memory consequences relevant to the selected concept;
- whether a substitution from the frozen architecture is being authorized;
- firmware, wiring and test work that must be repeated because of the substitution; and
- cost and schedule effects.

A silent STM32 substitution would break configuration control. Assuming ESP32 acceptance merely because it appears in the architecture would break approval control. Procurement and project-wide Phase 4 remain blocked until E0 and E1 are recorded.

## 11.4 Later current-specification and Indian-price verification gate

No fresh external verification was performed while drafting Part V. After concept and platform authorization, the project requires a separate controlled verification pass before purchasing.

| Verification area | Required future evidence |
|---|---|
| Exact controller board | Current manufacturer documentation, exact board marking, USB interface, supported pins and power limits |
| Exact sensors and actuators | Manufacturer documentation, module identity, supplier record and incoming test plan |
| Power sources and protection | Rated output, connector/conductor suitability, protection assumptions and measured project-load plan |
| Current Indian prices | Dated quotations from reputable Indian suppliers, including delivery and tax where relevant |
| Supplier authenticity | Seller identity, markings, return policy, replacement availability and incoming acceptance evidence |
| Availability and lead time | Stock and delivery information compatible with the approved schedule |
| Institutional facilities | Recorded access to the FDM printer, tools, rotating-rig area, oven, scale or other concept-dependent resources |
| Standards and patent status | Separate later work using official issuer, patent-office and institutional/professional sources |

Historical component labels and cost estimates may define a preliminary envelope. They must not be copied into a final purchase order without refresh. A nominally compatible module may still be unsuitable because of clone variation, board layout, noise, bandwidth, voltage level, connector quality or seller authenticity.

The verification record should be versioned and dated. Each quoted component should be linked to the exact authorized architecture function. Alternatives should be classified as approved substitutes, conditional substitutes or prohibited substitutions. A cheaper part is not automatically acceptable when it changes the sensor, actuator, power or timing behavior on which the validation plan depends.

## 11.5 Procurement and BOM freeze

The bill of materials may be frozen only after concept authorization, platform acceptance, current verification, safety review and budget approval.

A controlled BOM should include:

- exact part name, model, quantity and architecture function;
- manufacturer or responsible supplier identity;
- approved substitute rule and conditions for substitution;
- quotation date, unit price, delivery, tax and replacement allowance;
- separation of purchased, borrowed, donated and institutional resources;
- power ratings, connector assumptions, conductors, protection and required accessories;
- fabricated parts, material quantities and institutional printing assumptions;
- facility-dependent items that are not purchased but are necessary for execution;
- total against the preferred ₹3,000 target and the absolute ₹5,000 ceiling;
- invoice, receipt or issue-note reference after purchase;
- incoming acceptance owner and backup; and
- BOM/configuration revision identifier.

The preferred budget is a design pressure, while the ₹5,000 ceiling is a hard boundary unless an explicit exception is granted. Hidden costs must not be removed from the record merely because a component is borrowed or a facility is institutional. Such dependencies should be shown separately so that another team can understand the true resource requirement.

Future patent-development equipment, professional searching, field access and temporary laboratory references belong to a separate budget. They must not be used to make the ordinary semester MVP appear cheaper or more self-contained than it is.

Purchase alone does not establish component suitability; incoming acceptance remains mandatory.

## 11.6 Team roles, reviewers and backup operators

Project mC has five members. The framework assigns functions rather than names because the present package does not prove final named ownership.

| Required function | Primary responsibility | Reviewer and backup requirement |
|---|---|---|
| Technical integration lead | Architecture integrity, interfaces, safety, schedule and final integration | A named technical reviewer must be able to reproduce the configuration and challenge scope drift. |
| Firmware/data lead | Acquisition, control logic, features, USB logs, analysis and held-out protocol | A backup must be able to build firmware, run analysis and recover the project without undocumented local state. |
| Hardware/rig or mechanics lead | Procurement, wiring, structure/rig, mounting, guarding and power | A backup must be able to inspect wiring, mounting and safety checklists. |
| Learner/test assistant | Inventory, scripted sessions, labels, photographs and run sheets | Work must be checklist-driven and bounded so that records remain repeatable. |
| Documentation/communication lead | Teacher communication, source log, report, demonstration script and slides | Every performance claim must be reviewed by the relevant technical owner. |

Every critical subsystem requires three forms of accountability: a primary owner, a reviewer and a backup operator. One person may hold more than one function only if the workload and review independence remain credible. No subsystem should depend on a single member’s memory, uncommitted code, private device or undocumented calibration.

The named role matrix should include contact responsibility, deliverables, review checkpoints, absence coverage and authority to trigger a safety or evidence stop. At least one person other than the primary owner must be able to:

- assemble or inspect the essential configuration;
- build and load the firmware;
- start a controlled test;
- locate the raw evidence and configuration record;
- run the final demonstration; and
- explain the claim boundary and known failures.

Cross-training controls absence and single-person bottlenecks.

## 11.7 Configuration, repository and change control

Before the first controlled test, the project should establish a configuration record containing:

- the authorized concept and platform decision;
- the BOM revision and exact hardware identifiers;
- wiring diagram, power architecture and pin map;
- CAD, rig or jig revision where applicable;
- firmware version or commit identifier;
- calibration and configuration file;
- test-procedure version;
- raw-data naming convention and immutable run/session identifiers;
- success, failure, exclusion and stop rules;
- named owners, reviewers and backups; and
- safety and facility approval references.

The repository should separate at least five classes of material: authority and decisions; hardware/CAD/configuration; firmware and analysis; raw evidence; and reports/presentations. Raw evidence should be append-only or otherwise protected from accidental overwriting. Derived graphs and summaries should remain reproducible from the preserved raw data and analysis version.

A change after configuration freeze must record:

1. what changed;
2. why it changed;
3. who requested and approved it;
4. which earlier evidence is no longer comparable;
5. which tests must be repeated;
6. whether the change affects budget, safety or schedule; and
7. the new configuration identifier.

Boards, actuators, sensors, mechanisms, power supplies, fixtures, sample plans, models and thresholds may not change silently. A change that alters the concept identity requires return to Gate E0, not merely a new commit.

## 11.8 Common semester entry gates

The following gates apply before concept-specific execution.

| Gate | Required evidence | Pass consequence | Fail or unresolved consequence |
|---|---|---|---|
| E0 — Concept authorization | Written teacher/project decision | Activate one concept branch | Do not represent any branch as selected |
| E1 — Platform acceptance | Written exact-controller decision | Freeze board/toolchain path | No board-specific final design or procurement |
| E2 — Current verification | Manufacturer/specification and Indian-supplier record | Create candidate procurement list | Replace, reprice or narrow before purchase |
| E3 — Budget/BOM approval | Controlled BOM within approved ceiling | Permit purchase | Reduce scope or obtain explicit exception |
| E4 — Safety/facility approval | Hazard controls and concept-dependent access | Permit physical work | Stop until safe access exists |
| E5 — Roles/backups | Named primary, reviewer and backup ownership | Release accountable work packages | Do not create single-person critical dependencies |
| E6 — Quantitative protocol | Preregistered success, holdout, exclusion and kill rules | Permit locked validation | Pilot only; no final performance claims |
| E7 — Repository/evidence readiness | Configuration IDs, run naming, backup and archival path | Permit final evidence collection | Repair controls before final data collection |
| E8 — Patent-scope separation | MVP and future research separated in scope, budget and claims | Permit ordinary semester build | Remove future patent features from MVP |

Bounded pilot checks may occur only when explicitly labelled and separated from final evidence. Final validation begins only after E6 and E7.

## 11.9 OpenBraille execution branch

This branch becomes active only if OpenBraille is explicitly authorized. Its semester identity remains one non-standard macro six-dot tactile cell using six SG90-class servos, six eccentric cam/follower channels, six guided vertical pins, ESP32-class direct PWM control, an external regulated servo-power branch, USB command/logging, active raise/retract control and mandatory single-dot-first commissioning.

| Stage | Required future evidence | Stop or fallback rule |
|---|---|---|
| OB-G0 — Authorization | Teacher concept and platform decision | No procurement or build claim without authorization |
| OB-V0 — Incoming/facility check | Exact board, first servo, supply, USB, FDM access and tools verified | Resolve failures before final CAD commitment |
| OB-V1 — One-channel coupon | Versioned channel raises and actively retracts safely under repeated operation | Redesign; do not print or build the remaining five channels |
| OB-V2 — Operating bands | External displacement evidence for upper and lower states | Change geometry or actuator; do not tune blindly |
| OB-V3 — Six-channel coexistence | Pattern tests, rail/reset record and interference inspection | Improve power, sequencing or mechanics before expansion |
| OB-V4 — Mapping verification | Unit-tested pattern mapping plus physical state checks | Correct mapping/configuration before evaluation |
| OB-V5 — Repeatability/lifecycle screen | Approved cycle and wear datasets | Redesign, narrow the claim or report failure |
| OB-V6 — Tactile evaluation | Approved blinded protocol, raw results and stop rules | Report only mechanical/visual evidence if unavailable |
| OB-V7 — Frozen demonstration | Same CAD, firmware, calibration, BOM and checklist as validation | Show highest passed gate and disclose failed capabilities |

The one-channel coupon is the decisive early risk-reduction stage. It should include the real servo class, cam/follower geometry, pin guidance, intended load, active raise and retract commands, measured motion and safe guarding. Printing or assembling all six channels before this coupon passes would multiply an unresolved mechanism risk.

Power validation should proceed from one channel to staged multi-channel patterns. The controller signal domain and servo-power domain must share the required reference without using the controller rail to power the servo motors. Current headroom, droop, reset behavior, stall, heating, conductors and connectors require measurement. The historical 5 V/2 A and capacitor values do not control the final design.

Allowed refinements include per-dot calibration, tolerance coupons, cam-profile iteration within the same mechanism, guards, measured power-distribution changes, deterministic USB commands and temporary external ground-truth instruments. Moving rollers, solenoids, shape-memory alloy, pneumatics, a commercial-scale cell, permanent D11/VPD-C7 hardware, silent actuator or STM32 substitution, and cross-concept hybrids require new authorization.

A partial OpenBraille result remains valid when reported at the highest passed gate. A repeatable one-dot channel with honest failure analysis is preferable to an unstable six-dot demonstration presented as success.

## 11.10 VibeGuard execution branch

VibeGuard is the strongest supported semester-build branch, but it becomes active only after approval. Its frozen Level-1 identity remains one rigidly mounted ADXL345-class tri-axis accelerometer, one ESP32-class controller, SPI acquisition, a guarded low-voltage rotating test article, safe repeatable normal and induced-abnormal states, RMS plus persistence as the mandatory minimum classifier, optional supporting FFT/bands and ordinary Mahalanobis, RGB indication, USB logging and fixed configuration records.

| Stage | Required future evidence | Stop or fallback rule |
|---|---|---|
| VG-G0 — Authorization | Teacher approval of concept, platform and safe Level-1 scope | Do not call VibeGuard selected or procurement-ready |
| VG-V0 — Component acceptance | Board identity/USB, sensor axis response, stable rails and rig inspection | Replace or redesign failing hardware |
| VG-V1 — Acquisition integrity | Achieved rate, timestamps, read/loss/saturation counters and stable wiring | Reduce rate/clock, shorten wiring or replace module |
| VG-V2 — Normal repeatability | Independent sessions and at least one remount with metadata | Repair mount or rig before tuning |
| VG-V3 — Abnormal repeatability | Safely and independently labelled repeated abnormal sessions | Redesign fixture; do not tune around unstable labels |
| VG-V4 — Minimum classifier | Frozen RMS plus persistence operates locally | Improve physical repeatability or simplify analysis |
| VG-V5 — Optional comparison | FFT/bands or ordinary Mahalanobis tested on the same protocol | Drop if unstable, non-incremental or schedule-threatening |
| VG-V6 — Locked holdout | Untouched session, day or remount tested without threshold change | Preserve and report failure; do not retune the holdout |
| VG-V7 — Demonstration/documentation | Second operator, checklist, configuration, logs and source-backed report | Freeze feature growth and repair only essential defects |

The branch is a measurement and controlled-classification project, not merely an LED alarm. Acquisition integrity and repeatable physical states precede algorithm tuning. A sensor module that communicates but saturates, loses samples, drifts or is mounted on a flexible surface does not pass VG-V1. A visually different abnormal state that is not mechanically repeatable does not pass VG-V3.

RMS plus persistence is the mandatory baseline because it creates a clear local classifier that can be explained and audited. FFT bands may provide diagnostic context, and ordinary Mahalanobis may be compared only after the baseline and acquisition gates pass. Optional analysis must use the same held-out protocol so that added complexity is not rewarded by easier data.

The final protocol should define independent sessions, sensitivity or missed-state rate, false alerts, invalid-session handling, confusion matrix, latency, acquisition loss, holdout structure, exclusions, resource use and kill rules. No final numerical target is approved in the current record.

The branch must not claim predictive maintenance, bearing diagnosis, remaining useful life, dense-machine source attribution, online self-learning, PIRG, cloud dependence or industrial certification. Level-1 detection of a controlled state change does not prove which physical source caused it.

## 11.11 TrueMoist execution branch

This branch becomes active only if TrueMoist is explicitly authorized. Its frozen identity remains one genuine analog capacitive moisture probe for the final dataset, a second nominally identical unit for spare and unit-variation characterization, a nearby waterproof DS18B20, known S0/S1 prepared-treatment metadata, one homogeneous soil, ADS1115 as the primary acquisition design subject to comparison against calibrated ESP32 ADC1, offline low-order fitting, fixed local coefficients, USB CSV, dry-basis gravimetric reference and an authoritative design of 72 independent physical runs.

| Stage | Required future evidence | Stop or fallback rule |
|---|---|---|
| TM-G0 — Authorization/platform/facilities | Teacher decision plus credible oven, scale and constant-mass access | No accuracy or compensation programme without ground truth |
| TM-V0 — Probe gate | Authenticity/basic stability, monotonic pilot and reinsertion repeatability | Improve jig, inspect spare or replace probe |
| TM-V1 — ADC gate | Same analog node compared through ADS1115 and calibrated ESP32 ADC1 | Select by evidence, not nominal resolution |
| TM-V2 — Preparation gate | Packing sensitivity, safe temperature feasibility, S1 feasibility and grouped pilot analysis | Improve preparation, adjust S1 once or use a transparent temperature-only fallback |
| TM-V3 — Hardware/jig freeze | Soldered path, fixed geometry and versioned procedure | Do not collect the main dataset while configuration is fluid |
| TM-V4 — Training collection | Independent physical replicates 1 and 2 with complete mass/run records | Repair identifiers or reference failures before modelling |
| TM-V5 — Model freeze/equivalence | Baseline and supported compensated models evaluated; coefficients frozen; Python/MCU fixed-vector equivalence | Use stable linear fallback or report inability to freeze |
| TM-V6 — Untouched replicate 3 | No retuning; report absolute errors, relative improvement, subsets, drift and exclusions | Report bounded failure; do not reopen and retune |
| TM-C1 — 54-run contingency | Explicit approval and transparent reduction in evidence | Never describe 54 runs as the authoritative 72-run design |

TrueMoist depends on physical reference quality. A live serial value or graph is not minimum success. Each independent run requires traceable preparation, geometry, temperature, treatment metadata, probe reading and gravimetric reference. S0/S1 is known batch metadata, not live conductivity measurement or autonomous salinity estimation.

The compensated result must be compared with the same probe’s uncompensated baseline against the same untouched physical reference. Replicate 3 remains closed until hardware, coefficients and firmware are frozen. Failure on the holdout cannot be repaired by reopening it and retuning.

Live EC, irrigation control, cloud telemetry, multi-soil universality, a custom multi-frequency probe, TinyML and online adaptation are prohibited substitutions. If facility throughput or ground truth is unavailable, the dependent accuracy and compensation claims must be removed rather than simulated by weaker evidence.

## 11.12 Quantitative validation and held-out evidence

All three branches require a common evidence discipline.

1. Define the independent physical unit before analysis.
2. Separate calibration and development evidence from the locked holdout.
3. Preregister thresholds, exclusions, success criteria, stop rules and failure reporting.
4. Retain invalid and failed sessions; do not silently delete inconvenient evidence.
5. Freeze hardware, firmware, geometry, model and configuration before final evaluation.
6. Preserve raw logs and physical labels independently of derived metrics.
7. Report absolute performance, limitations and failure modes, not only relative improvement or a best-case graph.
8. Use a second operator, independent rebuild, remount or physical replicate where the concept requires it.
9. Treat negative results as legitimate engineering evidence.

| Concept | Minimum independent evidence structure |
|---|---|
| OpenBraille | Repeated physical actuation sets, lifecycle/wear record, frozen pattern mapping and—only if approved—blinded tactile trials |
| VibeGuard | Complete sessions, days or remounts held out; no leakage through overlapping windows from the same physical run |
| TrueMoist | Independent physical preparation replicates; replicate 3 untouched until model and firmware freeze |

A proposed number becomes a result only when it is part of an approved protocol and is measured under the frozen configuration. Values appearing in a presentation, roadmap, EDR, memory or draft gate remain planning targets.

The validation report should include the planned protocol, deviations, raw-evidence index, configuration identity, exclusions, invalid cases, metric definitions, full outputs, uncertainty and a claim table stating exactly what passed, failed or remained untested. A successful live demonstration cannot replace the locked validation report.

## 11.13 Safety and facility dependencies

Safety and facility access are entry gates, not after-the-fact sections of the report.

| Concept | Main dependency | Required future control |
|---|---|---|
| OpenBraille | Servo pinch points, rounded pins, stall/current behavior, external power, FDM access and possible participant-based tactile test | Guards, power isolation, staged current tests, printer/tool confirmation, supervision and an approved participant/consent/stop procedure |
| VibeGuard | Rotating motor or fan, retained eccentric fixture, loose-mass hazard, separate motor supply and repeated abnormal-state setup | Rigid base, guard, pre-run inspection, safe low-voltage operation, stop conditions and independent physical labels |
| TrueMoist | Oven and scale access, controlled temperature states, sample containers, constant-mass workflow and repeatable soil preparation | Responsible facility access, safe handling procedure, fixed sensor geometry, throughput trial and traceable mass records |

A live-demonstration requirement never overrides safety. Unsafe motion, exposed rotation, heating, unstable power, a loose abnormality fixture or a facility-rule breach triggers an immediate stop. The event should be recorded as evidence, not hidden to preserve presentation continuity.

Facility confirmation should identify responsible persons, booking limitations, operating rules, calibration status where relevant and fallback options. A concept that depends on unavailable ground truth or fabrication access is not execution-ready merely because its electronics are available.

## 11.14 Schedule and milestone control

The project supports an internal planning baseline of approximately two months within a teacher-context outer boundary of up to three months. No approved calendar or actual milestone performance is attached.

| Relative milestone | Required completion condition |
|---|---|
| M0 — Authorization | Concept, platform, scope and entry conditions recorded |
| M1 — Verification and procurement freeze | Current specifications/prices, facilities, safety, roles and BOM approved |
| M2 — Incoming and early gates | Exact parts and facilities pass concept-specific acceptance checks |
| M3 — Minimum subsystem proof | OpenBraille one-dot channel, VibeGuard stable acquisition/rig, or TrueMoist probe/reference chain demonstrated |
| M4 — Integrated configuration freeze | Hardware, firmware, geometry, protocol and evidence naming frozen |
| M5 — Locked quantitative validation | Held-out protocol executed without post-hoc configuration changes |
| M6 — Demonstration and archival | Second-operator rehearsal, fallback package, report and immutable evidence archive completed |

The calendar should be created only after authorization and lead-time verification. Each milestone requires an owner, reviewer, due date, evidence link, pass/fail status and effect on later work. Completion percentage alone is insufficient because a project can appear “80% complete” while its decisive evidence gate has not passed.

Optional features are scheduled only after baseline gates have time and contingency. For VibeGuard, optional FFT, Mahalanobis or display work is dropped before acquisition and holdout quality. For OpenBraille, multi-cell or advanced future mechanisms remain outside the schedule. For TrueMoist, advanced model terms are dropped before ground-truth quality and replicate independence.

Schedule pressure does not authorize silent scope reduction. A reduced branch must be explicitly approved, relabelled and linked to a narrower claim boundary.

## 11.15 Demonstration, fallback and evidence package

The final demonstration should use the same controlled configuration that produced the validation evidence. A polished display without traceable evidence is insufficient; a strong evidence archive without an understandable demonstration is also incomplete.

| Concept | Primary demonstration | Controlled fallback |
|---|---|---|
| OpenBraille | USB command produces independently controlled, actively raised and retracted six-dot patterns under safe power | Show the highest passed gate, such as a verified one-dot coupon, with logs and failure evidence; do not claim six-dot or tactile success |
| VibeGuard | Safe normal and abnormal rig states produce local RMS/persistence indication consistent with USB logs | A pre-approved, clearly labelled playback or preserved-log explanation may support presentation continuity but cannot be represented as live detection or replace physical validation |
| TrueMoist | Frozen local model produces baseline and compensated estimates, with held-out comparison reconstructed from USB CSV and gravimetric records | Present the validated measurement-chain portion and explain the failed gate; do not claim compensation benefit without the holdout result |

The common evidence package should contain:

- authorization and platform decision;
- final BOM, invoices and facility record;
- configuration index and change log;
- wiring, CAD, rig or jig files and revision IDs;
- firmware/source code and build instructions;
- calibration and test procedures;
- raw logs, physical labels and run/session ledger;
- analysis scripts and fixed outputs;
- pass, fail, exclusion and invalid-case record;
- safety checklist and demonstration script;
- second-operator checklist;
- photographs or video where approved and useful;
- final limitations and claim-boundary statement; and
- immutable archive/checksum record.

Fallbacks exist to preserve honest communication when a live element fails. They do not upgrade a failed gate. Playback must be labelled playback; a one-dot OpenBraille coupon is not a six-dot result; a TrueMoist measurement chain without held-out improvement is not validated compensation.

## 11.16 Stop, failure and scope-reduction rules

The following rules control future execution.

1. **Authorization stop:** No procurement or project-wide Phase 4 claim before concept and platform authorization.
2. **Safety stop:** Stop immediately on unsafe motion, heating, exposed pinch or rotating hazard, unstable power or facility-rule breach.
3. **Gate stop:** Do not expand a failed subsystem into full integration. Correct it, narrow the objective or report failure.
4. **No silent substitution:** Board, actuator, sensor, mechanism, model, sample plan, fixture or power-design changes require change control.
5. **Budget stop:** If the verified BOM exceeds the approved ceiling, reduce scope or obtain an explicit exception. Do not hide borrowed or institutional dependencies.
6. **Schedule stop:** Drop optional analysis, displays and future research before compromising baseline evidence.
7. **Held-out stop:** Do not retune thresholds or models after opening the locked holdout. A failed holdout remains a result.
8. **Facility stop:** If essential FDM, tactile-protocol approval, safe rig access, oven or scale access is unavailable, use the documented bounded fallback or remove the dependent claim.
9. **Evidence stop:** No final metric without raw data, identifiers, configuration and reproducible analysis.
10. **Scope-reduction rule:** Any reduction—such as an OpenBraille one-dot result, a VibeGuard baseline-only result or a TrueMoist 54-run contingency—must be authorized, explicitly labelled and reflected in the claim boundary.

A stop is not automatically project failure. It is a control point that prevents a local problem from corrupting the entire result. The final report should state the highest passed gate, the reason execution stopped, the evidence preserved and the minimum next action required to continue.

## 11.17 Patent-research separation

Semester implementation and future patent-development work must remain separated in architecture, schedule, budget, repository, disclosure and claims.

| Concept | Frozen semester boundary | Future research only |
|---|---|---|
| OpenBraille | Macro six-servo/cam/guided-pin cell with active retraction and evidence controls | D11 physical-state observability, VPD-C7 pin-side datum and practical-scale claim-focused work |
| VibeGuard | One-sensor Level-1 controlled-state monitor using RMS/persistence and supporting spectral evidence | PIRG, target/interferer attribution, ambiguity or abstention, protected updating and remount transfer |
| TrueMoist | One-soil fixed local compensation experiment with known treatment metadata and gravimetric truth | Probe replacement/remount transfer, validity/contamination gating, multi-unit/lot and multi-soil research |

A successful ordinary MVP does not prove that a future mechanism works. Conversely, a speculative patent story may not be inserted late into the semester build to make the project appear more novel. Any future claim-focused programme requires separate authorization, confidentiality decisions, contribution records, physical experiments, current prior-art verification and institutional IPR review.

No frozen MVP is established as patentable. The final adjudications disagree on the preferred future patent gate. Part V therefore preserves multiple controlled research paths without selecting one by model count or semester preference.

## 11.18 Future execution-record change control

When direct execution records become available, Chapter 11 may be updated only through controlled evidence entry.

Each new record should be:

1. copied into the appropriate organized-workspace location;
2. assigned a stable filename and immutable identity;
3. hashed and entered through source-map change control;
4. classified by authority tier and manual treatment;
5. extracted or directly reviewed, including visual review where required;
6. checked against the authorized concept and configuration;
7. reconciled with existing claims and contradictions; and
8. incorporated into a new controlled Part V revision.

Likely future records include the teacher decision, platform approval, Phase 4 entry record, current verification worksheet, frozen BOM, invoices, role matrix, safety approvals, facility confirmations, configuration index, firmware commits, CAD/rig revisions, test protocols, run ledgers, raw logs, validation reports, demonstration record and final submission.

A new file does not become authority merely because it is placed in the repository. Its role depends on who issued it, what it directly proves, whether its configuration is identifiable and whether it conflicts with a higher source. Drafts, exports and duplicate formats should not be counted as independent evidence.

Chapter 11 status statements must be revised item by item. For example, a procurement invoice may prove that a component was purchased but not that it passed incoming acceptance; a video may prove that motion occurred but not repeatability; a teacher approval may authorize VibeGuard but not automatically approve every optional feature or patent experiment.

## 11.19 Current implementation-status statement

> **CURRENT IMPLEMENTATION STATUS**
>
> The attached Project mC record contains frozen architectures, implementation guidance, teacher-facing material, comparative evidence and a proposed shift to VibeGuard. It contains no direct mapped Chapter 11 execution record proving final concept authorization, platform acceptance, project-wide Phase 4 entry, procurement, named role assignments, physical build progress, completed firmware, fabricated mechanics or rigs, completed datasets, quantitative validation, milestone performance, safety approval, successful live demonstration or patent-filing authorization.
>
> Chapter 11 is therefore ready only as a controlled future execution framework. Its branches, gates, roles, schedule and validation rules are requirements for later work, not claims that the work has been performed.

## 11.20 Chapter conclusion

Chapter 11 establishes a common execution discipline while keeping the three concepts separate. Authorization and platform acceptance precede procurement. Current specifications and Indian prices precede BOM freeze. Roles, safety, facilities, quantitative protocol and repository readiness precede final evidence collection. Each concept then follows its own architecture-specific gates and stop rules.

VibeGuard remains the strongest semester-build recommendation, but its branch is conditional on approval. OpenBraille remains a legitimate macro six-servo branch with strict one-channel-first and active-retraction controls. TrueMoist remains a legitimate one-soil compensation branch whose value depends on traceable gravimetric evidence and untouched physical replication.

The framework protects honest outcomes. It permits success to be claimed only at passed gates, preserves negative and partial results, prevents optional or patent-focused features from weakening the baseline, and requires the final demonstration to match the validated configuration. Until direct execution records enter through change control, no completed execution history may be inferred.

## 11.S Source notes

Chapter 11 has no direct mapped execution sources. Its framework is derived from the original organized-workspace governance, teacher-requirement, comparative-decision and final architecture paths listed in the Part V Source Ledger. The Chapter 10 official submission and change-request paths establish the review and authorization boundary. The OpenBraille, VibeGuard and TrueMoist final architecture, memory and SOP paths control the three separate execution branches. Historical roadmaps provide conditional planning support only. No packet filename or manifest is treated as technical evidence.

# Part V Approval and Open-Decision Register

| ID | Decision or approval | Current state | Controlling source | Required next action |
|---|---|---|---|---|
| PV-01 | Zeroth-review outcome | Official OpenBraille deck exists; teacher comments/outcome not attached | Official submission and teacher/review control | Preserve any teacher feedback, rubric, conditions or decision if it exists |
| PV-02 | OpenBraille-to-VibeGuard shift | Formally requested; not proved approved | Validated Part I and change-request record | Record approval, conditional approval or rejection with date and conditions |
| PV-03 | Final semester concept | Open | Decision Register v1.2, comparative evidence and teacher authority | Authorize one frozen concept or a formal conditional gate process |
| PV-04 | Course platform | ESP32-class architectures exist; STM32 context unresolved | Teacher requirements and final architecture records | Approve exact board/toolchain or a controlled substitution |
| PV-05 | Project-wide Phase 4 entry | Not proved authorized | Current project-state control | Create a controlling entry record after E0–E5 |
| PV-06 | Current specifications and Indian prices | Not verified in this drafting stage | Authority protocol | Perform a dated manufacturer/supplier verification pass after approval |
| PV-07 | Procurement-ready BOM | Not frozen | Historical BOM layers and budget constraints | Approve current BOM, safety assumptions and budget before purchase |
| PV-08 | Facility access | Not confirmed | Concept architecture dependencies | Confirm FDM/tools, rig area or oven/scale access as required |
| PV-09 | Named owners, reviewers and backups | Proposed only | Part I role framework | Record named ownership and cross-training |
| PV-10 | Quantitative success and kill criteria | Concept-specific proposals exist; final criteria not approved | Parts II–IV | Preregister the authorized branch protocol before locked validation |
| PV-11 | Safety approval | Not proved complete | Concept-specific hazard controls | Complete and approve the relevant safety/facility checklist |
| PV-12 | Demonstration and fallback | Framework only | Chapter 11 control | Approve a primary and clearly labelled fallback configuration |
| PV-13 | Evidence archive | Framework only | Repository/change-control rules | Create paths, run ledger, checksum and backup procedure |
| PV-14 | OpenBraille tactile protocol | Open | Part II boundary | Approve blinded method, participant conditions and stop rules or omit the claim |
| PV-15 | VibeGuard held-out structure | Open | Part III boundary | Freeze independent sessions/day/remount, thresholds and integrity criteria |
| PV-16 | TrueMoist facilities and 72-run throughput | Open | Part IV boundary | Confirm gravimetric facilities and pilot throughput before main collection |
| PV-17 | Schedule/calendar | No approved dates | Teacher time boundary and milestone framework | Convert relative milestones into an approved calendar |
| PV-18 | Future patent-development gate | Adjudications disagree | Final adjudications and authority protocol | Obtain new physical evidence, current prior-art review and institutional IPR decision |
| PV-19 | Confidentiality, ownership and inventorship | Unresolved | Authority and patent-language controls | Obtain institutional guidance and preserve contribution records |

# Part V Execution-Control Matrix

| Area | Current fact | Open decision | Required future action | Prohibited claim |
|---|---|---|---|---|
| Teacher review | Official OpenBraille deck dated 30 July 2026 exists | Review outcome | Add explicit teacher feedback or decision record | “The deck proves approval” |
| Proposed shift | VibeGuard is strongest recommendation; change request exists | Teacher acceptance | Record approval/conditions/rejection | “The project has changed to VibeGuard” |
| Concept | Three frozen retained architectures exist | Final authorized concept | Pass Gate E0 | Any branch is already selected |
| Platform | Frozen architectures use ESP32-class controllers | ESP32 acceptance or STM32 substitution | Pass Gate E1 with exact-board record | Platform acceptance is settled |
| Budget | Preferred ≤₹3,000; absolute ceiling ₹5,000 | Current verified total | Refresh prices and approve BOM | Historical estimates are actual spend |
| Procurement | Historical planning BOMs exist | Purchase authorization | Pass E2–E4 and freeze BOM | Procurement has begun |
| Roles | Five-member functional structure exists | Named ownership | Assign primary, reviewer and backup | Roles are already finalized |
| Repository | Governance and source controls exist | Execution archive details | Create configuration IDs and immutable evidence path | Files in a folder automatically prove execution |
| OpenBraille | Frozen macro six-servo architecture exists | Whether branch is authorized | Follow OB-G0 to OB-V7 | Built, tactile-validated or power-proved |
| VibeGuard | Frozen one-sensor Level-1 architecture exists | Whether shift is approved | Follow VG-G0 to VG-V7 | Predictive maintenance or source attribution proved |
| TrueMoist | Frozen one-soil 72-run design exists | Whether branch/facilities are authorized | Follow TM-G0 to TM-V6 | Seventy-two runs or compensation success completed |
| Validation | Concept-specific gate structures exist | Final thresholds/holdouts | Preregister and protect held-out evidence | Proposed values are achieved results |
| Safety | Hazards and dependencies are known | Actual responsible approval/access | Complete concept-specific controls | Safety approval is complete |
| Schedule | Two-month internal baseline within three-month outer context | Actual dates | Approve milestone calendar | Milestones are completed |
| Demonstration | Strong live demonstration is required | Final primary/fallback setup | Rehearse frozen configuration with second operator | Playback is live detection or partial work is full success |
| Patent | Future hypotheses are documented | Whether any route survives experiments and review | Separate later programme and IPR control | MVP or future mechanism is patentable, filed or FTO-cleared |
| Change records | Future evidence-entry procedure is defined | When direct records become available | Hash, classify, review and reconcile each record | New files silently change current status |

# Part V Contradiction Summary

| ID | Chapter | Issue | Controlling resolution | Residual uncertainty |
|---|---:|---|---|---|
| PV-C01 | 10 | Official title suggests a commercial refreshable Braille display | Preserve the historical title; use the Part II non-standard macro proof-of-concept boundary | Whether an approved tactile protocol will pass |
| PV-C02 | 10 | Macro cell and ISO reference may imply compliance | ISO is contextual only; no compliance claim | Final geometry and tactile interpretation |
| PV-C03 | 10 | General up/down wording versus unproved reset | Active servo-driven raise and retract control governs | Actual coupled return behavior |
| PV-C04 | 10 | 5 V/2 A and 1,000 µF appear definite | Historical provisional values only; staged measurement governs | Purchased supply and safe headroom |
| PV-C05 | 10–11 | ESP32 appears in architectures while STM32 appears in teacher context | Preserve frozen architecture; obtain explicit platform approval or controlled substitution | Exact board/toolchain decision |
| PV-C06 | 10–11 | Historical cost ranges appear procurement-ready | Treat as dated planning; verify current Indian prices and authenticity | Current total and availability |
| PV-C07 | 10 | Official OpenBraille submission versus later VibeGuard recommendation | Preserve both: OpenBraille was submitted; VibeGuard is later recommended and requested | Teacher decision |
| PV-C08 | 10 | Multiple drafts may be mistaken for multiple approvals or validations | Only the official file controls submission; drafts are provenance | Exact internal creation dates |
| PV-C09 | 10 | Generated visual resembles a technical figure | Provenance only; exclude from technical/final-figure use | None for disposition |
| PV-C10 | 10–11 | Roadmaps and change request may look like authorization | Roadmaps are conditional and requests are not decisions | Written teacher response |
| PV-C11 | 11 | Chapter title may imply execution history exists | Zero directly mapped sources; future framework only | Timing of future record entry |
| PV-C12 | 11 | Concept memories may say implementation-ready | Concept-level architecture readiness does not open project-wide Phase 4 | Authorization state |
| PV-C13 | 11 | Proposed thresholds may appear achieved | Values remain proposals until preregistered and measured | Final approved metrics/results |
| PV-C14 | 11 | Strong live demonstration may be treated as validation | Demonstration must match the frozen validated configuration and evidence package | Whether final gates pass |
| PV-C15 | 11 | Optional analysis may appear mandatory | Baseline architecture controls; optional work is dropped first | Incremental value and schedule |
| PV-C16 | 11 | Future patent mechanisms may enter the semester build | Separate architecture, schedule, budget, repository and claims | Whether later research is authorized |
| PV-C17 | 10–11 | Semester winner may be treated as patent winner | VibeGuard is strongest for semester; future patent route remains unresolved | Authorized future gate |
| PV-C18 | 11 | Partial success may be hidden as complete success | Report highest passed gate and reduced claim boundary | Actual future failure mode |

# Part V Source Ledger

Only original organized-workspace paths materially relied upon are listed. Packet filenames and the attachment manifest are not technical evidence. The validated reconciliation controls resolved wording, while the paths below preserve original evidence identity.

## Chapter 10 — TIER_1 project and approval control

- `01_GOVERNANCE_AND_CONTROL/01_Project_Requirements/Teacher_Project_Requirements_and_Change_Context.md`
- `01_GOVERNANCE_AND_CONTROL/02_Decision_Registers/Project_mC_Decision_Register_v1.2.md`
- `01_GOVERNANCE_AND_CONTROL/AUTHORITY_MAP.md`

## Chapter 10 — TIER_2 teacher-facing and comparative evidence

- `05_TEACHER_AND_REVIEWS/01_Teacher_Documents/TEACHER_DELIVERY_INDEX.md`
- `05_TEACHER_AND_REVIEWS/02_Zeroth_Review_OpenBraille/01_Official_Submission/OpenBraille_Zeroth_Review_OFFICIAL_2026-07-30.pptx`
- `05_TEACHER_AND_REVIEWS/02_Zeroth_Review_OpenBraille/02_Drafts_and_Working_Files/01_Initial_Template_or_Early_Draft.pptx`
- `05_TEACHER_AND_REVIEWS/02_Zeroth_Review_OpenBraille/02_Drafts_and_Working_Files/02_OpenBraille_Draft_0.1.pptx`
- `05_TEACHER_AND_REVIEWS/02_Zeroth_Review_OpenBraille/02_Drafts_and_Working_Files/03_OpenBraille_Draft_0.2.pptx`
- `05_TEACHER_AND_REVIEWS/02_Zeroth_Review_OpenBraille/02_Drafts_and_Working_Files/04_OpenBraille_Draft_0.2.odp`
- `05_TEACHER_AND_REVIEWS/02_Zeroth_Review_OpenBraille/02_Drafts_and_Working_Files/05_Sreehari_Working_Draft.pptx`
- `05_TEACHER_AND_REVIEWS/02_Zeroth_Review_OpenBraille/02_Drafts_and_Working_Files/06_Group8_Working_Draft.pptx`
- `05_TEACHER_AND_REVIEWS/02_Zeroth_Review_OpenBraille/02_Drafts_and_Working_Files/07_PreSubmission_Finalised_Draft_1.pptx`
- `05_TEACHER_AND_REVIEWS/02_Zeroth_Review_OpenBraille/02_Drafts_and_Working_Files/08_PreSubmission_Finalised_Draft_2.pptx`
- `05_TEACHER_AND_REVIEWS/02_Zeroth_Review_OpenBraille/02_Drafts_and_Working_Files/09_OpenBraille_Block_Diagram.png`
- `05_TEACHER_AND_REVIEWS/02_Zeroth_Review_OpenBraille/02_Drafts_and_Working_Files/10_OpenBraille_Generated_Visual.png`
- `05_TEACHER_AND_REVIEWS/02_Zeroth_Review_OpenBraille/02_Drafts_and_Working_Files/11_Presentation_Instructions_Early.html`
- `05_TEACHER_AND_REVIEWS/02_Zeroth_Review_OpenBraille/02_Drafts_and_Working_Files/12_Presentation_Instructions_2.0.html`
- `05_TEACHER_AND_REVIEWS/TEACHER_AND_REVIEW_INDEX.md`
- `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/00_Engineering_Design_Review.md`
- `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/05_Uncertainty_and_Test_Register.md`
- `04_COMPARATIVE_DECISION/02_Final_Adjudications/01_Project_mC_Final_Adjudication_Work_Max.md`
- `04_COMPARATIVE_DECISION/02_Final_Adjudications/02_Project_mC_Final_Adjudication_Deep_Research_High.md`
- `04_COMPARATIVE_DECISION/03_Change_Request/Project_mC_Request_to_Change_from_OpenBraille_to_VibeGuard.docx`
- `04_COMPARATIVE_DECISION/03_Change_Request/Project_mC_Request_to_Change_from_OpenBraille_to_VibeGuard.pdf`
- `04_COMPARATIVE_DECISION/COMPARATIVE_DECISION_INDEX.md`

## Chapter 11 — TIER_1 current architecture and governance

### Common project control

- `01_GOVERNANCE_AND_CONTROL/01_Project_Requirements/Teacher_Project_Requirements_and_Change_Context.md`
- `01_GOVERNANCE_AND_CONTROL/02_Decision_Registers/Project_mC_Decision_Register_v1.2.md`
- `01_GOVERNANCE_AND_CONTROL/AUTHORITY_MAP.md`

### OpenBraille architecture

- `03_CONCEPT_PORTFOLIO/OpenBraille/01_Final_Architecture/Phase3C_OpenBraille_Architecture_Report_Final.md`
- `03_CONCEPT_PORTFOLIO/OpenBraille/01_Final_Architecture/Phase3C_OpenBraille_Memory_Final.md`
- `03_CONCEPT_PORTFOLIO/OpenBraille/01_Final_Architecture/Phase3C_OpenBraille_SOP_Final.md`

### VibeGuard architecture

- `03_CONCEPT_PORTFOLIO/VibeGuard/01_Final_Architecture/Phase3C_VibeGuard_Architecture_Report_Final.md`
- `03_CONCEPT_PORTFOLIO/VibeGuard/01_Final_Architecture/Phase3C_VibeGuard_Memory_Final.md`
- `03_CONCEPT_PORTFOLIO/VibeGuard/01_Final_Architecture/Phase3C_VibeGuard_SOP_Final.md`

### TrueMoist architecture

- `03_CONCEPT_PORTFOLIO/TrueMoist/01_Final_Architecture/Phase3C_TrueMoist_Architecture_Report_Final.md`
- `03_CONCEPT_PORTFOLIO/TrueMoist/01_Final_Architecture/Phase3C_TrueMoist_Memory_Final.md`
- `03_CONCEPT_PORTFOLIO/TrueMoist/01_Final_Architecture/Phase3C_TrueMoist_SOP_Final.md`

## Chapter 11 — TIER_2 conditional planning and decision context

- `03_CONCEPT_PORTFOLIO/OpenBraille/05_Roadmaps_and_Reference_Dossiers/OpenBraille_Semester_Architecture_and_Future_Research_Reference_Dossier.docx`
- `03_CONCEPT_PORTFOLIO/OpenBraille/05_Roadmaps_and_Reference_Dossiers/OpenBraille_Semester_Architecture_and_Future_Research_Reference_Dossier.pdf`
- `03_CONCEPT_PORTFOLIO/VibeGuard/05_Roadmaps_and_Reference_Dossiers/VibeGuard_Semester_Implementation_and_Future_Research_Roadmap.pdf`
- `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/00_Engineering_Design_Review.md`
- `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/04_Hard_Gate_Precheck.md`
- `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/05_Uncertainty_and_Test_Register.md`
- `04_COMPARATIVE_DECISION/02_Final_Adjudications/01_Project_mC_Final_Adjudication_Work_Max.md`
- `04_COMPARATIVE_DECISION/02_Final_Adjudications/02_Project_mC_Final_Adjudication_Deep_Research_High.md`
- `04_COMPARATIVE_DECISION/03_Change_Request/Project_mC_Request_to_Change_from_OpenBraille_to_VibeGuard.docx`
- `04_COMPARATIVE_DECISION/COMPARATIVE_DECISION_INDEX.md`

## Chapter 11 direct-source status

No original organized-workspace execution record was directly mapped to Chapter 11 in the frozen 301-record source map. The chapter is therefore a future framework assembled from the controlling project and concept sources above. Direct records must enter through the change-control process in Section 11.18 before any implementation-status statement is revised.

---

**End of Project mC Master Manual — Part V.**

<!-- END CONTROLLED COMPONENT: PART_V -->

---

<!-- BEGIN CONTROLLED COMPONENT: PART_VI -->
<!-- SOURCE PATH: /home/paradoxpete/Documents/PROJECT_ORGANIZED/08_MASTER_MANUAL/03_Drafting_Workspace/01_Validated_Parts/Part_VI/Project_mC_Master_Manual_Part_VI_Provenance_Archive_and_Source_Integrity.md -->
<!-- SOURCE SHA-256: ed0f5a9257aa5645fc4b502265b0d3df5e21766f5869984eb45ae074aa9aa559 -->

## Part VI — Provenance, Archive and Source Integrity

## Document control

| Field | Value |
|---|---|
| Document | Project mC Master Manual — Part VI |
| Controlled filename | `Project_mC_Master_Manual_Part_VI_Provenance_Archive_and_Source_Integrity.md` |
| Status | Controlled draft |
| Scope | Chapters 12–14 plus Part VI provenance, archive, source-integrity, open-decision, contradiction and source registers |
| Source boundary | Only the fifteen Markdown attachments in the controlled Part VI drafting package |
| Input inventory | Exactly fifteen physical Markdown attachments were present and readable. The fourteen externally hash-controlled files matched the manifest byte counts and SHA-256 values; the self-referential manifest was used only for file control. Parenthetical upload suffixes did not create additional logical sources. |
| Technical effect | Does not override validated Parts I–V |
| Approval effect | Not a teacher, Phase 4 or procurement approval |
| Patent effect | No patentability, filing, infringement or freedom-to-operate conclusion |
| External verification | Not performed in this drafting stage; reserved for a later controlled stage |
| Archive handling | No legacy archive was opened or expanded |
| Relationship to Parts I–V | Validated Parts I–V remain controlling for current project, architecture, comparative-decision, teacher-review and execution-framework state |

The drafting package passed its own manifest. The governing instruction, authority and contradiction protocol, Master Manual blueprint, validated Parts I–V, validated Chapters 12–14 reconciliation, three repaired Stage 10S source packets, Stage 10S coverage-repair and selection control, required output template and manifest were present and readable. The validated reconciliation controls resolved wording and contradiction treatment; the repaired packets preserve the underlying evidence and original organized-workspace paths. No prior-chat context, memory, web research or unstated external assumption was used.

## How to read Part VI

Part VI is a governance, provenance and reproducibility manual. It explains how Project mC’s evidence was created, transported, audited, selected, excluded, frozen, mapped and prepared for controlled use. It does not repeat the technical architecture chapters and does not elevate workflow records into engineering evidence.

Five distinctions govern the reading of this Part.

**Source identity is not technical truth.** A matching path, size or SHA-256 value can establish which bytes were reviewed. It cannot establish that the statements inside those bytes are correct, current, authorized or experimentally validated.

**AI evidence is not model voting.** Independent research lanes, syntheses and adjudications can broaden search coverage, expose disagreement and support analysis. Their evidentiary value depends on concept fidelity, source quality, claim-level reasoning, completeness and human review—not on how many systems repeat a conclusion.

**Current, historical, superseded, failed, partial and excluded material are different states.** A historical or archived file may be valuable for chronology or failure learning while having no authority over the current project. A failed concept swap remains invalid for the frozen concept. A partial lane remains partial. An excluded supplement remains outside the controlled set from which it was excluded.

**Source freeze is not permanent immobility.** The freeze defines a time-bounded accounting state. Later evidence and corrections may be added only through a separately logged revision that preserves the earlier release and makes the change visible.

**Reproducibility is not identical generative output.** A reproducible AI-assisted workflow allows another reviewer to inspect the instruction, source package, exclusions, outputs, audits, contradictions and human decisions. It does not guarantee that a generative system will reproduce identical words or conclusions on a later run.

Throughout Part VI, TIER_5 provenance, archive, transport and audit records prove only their own procedural roles. They do not override TIER_1–2 technical, architecture or decision evidence. Post-freeze controls explain construction of the Master Manual; they do not rewrite pre-freeze project history.

# Chapter 12 — Research Provenance and AI Workflow Control

## 12.1 Chapter purpose and evidence boundary

Project mC used AI-assisted research, synthesis, adversarial review, organization and comparative decision support across a large evidence set. Chapter 12 establishes the controls needed to use that work accurately and conservatively. Its purpose is not to praise or reject AI assistance. Its purpose is to make every model-assisted step traceable, bounded and subordinate to the project’s human authority system.

The chapter may explain how research lanes were commissioned, how packages were assembled, how reports were audited, how valid syntheses were selected, how adjudications were used and how failed or partial outputs were handled. It may also state the minimum disclosure and reproducibility records needed for later review.

The chapter may not use a manifest, launcher, model count, repeated conclusion, transport bundle or audit label to prove an architecture, performance result, approval, patent right or technical proposition. Current project identity remains controlled by the authority hierarchy and validated Parts I–V. In particular:

- teacher requirements and explicitly recorded approvals control their own domain;
- Decision Register v1.2 controls current recorded project decisions;
- final Phase 3C architecture reports, memories and SOPs control frozen concept identity;
- comparative evidence supports analysis but does not create approval;
- valid syntheses and final adjudications remain decision support;
- independent research lanes remain supporting evidence after audit;
- transport, archive and audit records remain procedural records.

The repaired Chapter 12 packet contains seventeen selected sources. It includes one Tier 1 source-policy control, Tier 2 patent-evidence and comparative-control records, representative governing instructions, manifests, a launcher, provenance/exclusion controls, a Stage 5 transport validation and a post-freeze chapter map. All seventeen were extracted successfully, with no review-required or hash-failure items. These facts establish that the selected procedural evidence was available for reconciliation; they do not prove that every Project mC source was semantically exhausted or that any model conclusion was correct.

## 12.2 Project research and synthesis workflow

The controlled Project mC workflow is best understood as a sequence of evidence transformations, each with a separate purpose and human gate.

### 12.2.1 Authority and frozen identity come first

Before a research or synthesis task can be interpreted, the project must identify the controlling requirements, current decision register and frozen architecture. This prevents a model from defining a concept merely from its short name. For Project mC, the current controlled concept identities remain:

- OpenBraille: the six-servo, eccentric-cam, guided-pin macro-cell architecture controlled in Part II;
- VibeGuard: the ADXL345-class accelerometer and ESP32-class vibration-monitoring architecture controlled in Part III;
- TrueMoist: the validated 72-run local temperature and salinity-treatment compensation architecture controlled in Part IV.

The research workflow may analyze prior art, implementation risks, patent hypotheses and future experiments around those identities. It may not silently substitute a moving-roller Braille mechanism, a software-security scanner, a live-EC system, a universal multi-soil platform or another architecture.

### 12.2.2 Independent lanes receive a defined task

Concept-specific governing instructions define the evidence cut-off, authority order, architecture-fidelity tripwires, required searches, legal distinctions, output structure, exclusions and prohibited claims. This converts a broad instruction such as “research the patent potential” into a controlled task with explicit boundaries.

A sound instruction separates at least four questions:

1. What is the frozen semester MVP?
2. Which conventional refinements remain within that MVP?
3. Which later mechanisms are only post-semester research hypotheses?
4. Which legal or institutional conclusions are outside the model’s authority?

The instruction also identifies which project files are controlling, historical, supporting, partial, excluded or prohibited. This is essential because a technically detailed lower-authority report can otherwise appear more persuasive than a shorter controlling record.

### 12.2.3 A physical package is assembled

Each workflow receives a defined physical package. The package may contain governing instructions, architecture records, memories, SOPs, prior research lanes, evidence matrices, adjudication inputs and file-control records. An input manifest records expected filenames, sizes, hashes and roles. Where upload limits require a reduced-file or merged bundle, the bundle serves transport convenience only. The original separate sources retain their identity and authority.

Package construction is a human-controlled step. A correct model cannot compensate for a concept-swapped, incomplete or contaminated package. Conversely, a complete package cannot guarantee a correct model response. Package completeness and output validity must be tested separately.

### 12.2.4 Synthesis audits rather than counts the lanes

A synthesis configuration is asked to inspect the independent lanes under the higher project authority. It should inventory the package, evaluate concept fidelity, trace load-bearing claims, distinguish primary from secondary support, separate facts from inferences, identify unsupported legal conclusions, compare frozen features with cited prior art and propose experiments or kill conditions.

The controlled OpenBraille and VibeGuard synthesis instructions prohibited one synthesis from seeing, predicting or imitating another synthesis. The TrueMoist synthesis similarly excluded prior-chat context, other synthesis outputs and cross-concept ranking. These controls sought to reduce direct contamination. They do not establish statistical independence or equal reliability.

### 12.2.5 Invalid material is excluded rather than averaged

When an output analyzes the wrong architecture, the correct treatment is exclusion, not averaging. When a lane is incomplete, the correct treatment is a partial label and restricted use, not reconstruction. When a claim lacks source support, recurrence in other model outputs does not repair it. A well-supported minority view may carry more evidentiary weight than several weak or derivative statements.

This rule prevents the workflow from becoming a popularity contest. It also protects the frozen architecture from being replaced by a superficially plausible alternative generated under the same concept name.

### 12.2.6 Controlled syntheses enter comparative review

Each retained concept has two controlled valid syntheses. Their number is a diversity and audit feature, not a vote count. Separate failed, partial or supplementary outputs remain outside the valid synthesis set according to their recorded status.

The selected syntheses then enter cross-concept adjudication together with the higher authority and common comparative evidence. The adjudication is expected to normalize the semester MVP and later research route, audit synthesis reliability, separate build feasibility from patent-development potential and identify experiments, risks and kill conditions.

### 12.2.7 Humans retain decision and accountability

At the end of the workflow, AI outputs remain inputs to human judgment. Humans freeze architectures, approve instructions, select source packages, classify outputs, verify sources, run physical tests, record teacher decisions, control procurement, preserve contribution chronology and decide whether institutional IPR review should begin.

This is the decisive boundary: model-assisted work can organize and challenge the evidence, but it cannot authorize the project, prove a physical result, establish a legal right or accept responsibility for the final manual.

## 12.3 Independent research lanes

Project mC preserved multiple named research lanes for each retained concept to broaden search coverage and expose disagreement. The controlled records identify six lanes per concept: ChatGPT Deep Research, Gemini, Perplexity, Qwen, Mistral and Microsoft Copilot. The existence of six labels does not imply six complete, equally reliable or statistically independent reports.

| Concept | Controlled lane treatment | Known completeness boundary | Controlled valid synthesis set |
|---|---|---|---|
| OpenBraille | Six research lanes retained as evidence sources | Perplexity is partial | Work Max and Valid Secondary / Standard High |
| VibeGuard | Six research lanes retained; three Mistral fragments are one lane | Mistral is a partial compilation with no final verdict | Work Max and Standard High |
| TrueMoist | Six research lanes retained; compiled outputs remain one lane | Perplexity is partial; Qwen combines an initial output and follow-up from one lane | Max and High + Deep Research |

“Independent” in this context describes the intended workflow separation: one lane or synthesis was not supposed to copy another lane’s conclusion. It does not mean that the outputs used unrelated project facts or unrelated prompting. They shared concept authority, task framing and often the same source corpus. Some were also transported through derivative bundles. Each output therefore requires individual fidelity and source review.

Independent recurrence has a limited but useful role. When unrelated lanes identify the same patent family, technical risk, prior-art feature or experiment, the recurrence may signal that the item deserves closer examination. It does not establish truth. A reviewer must still determine whether the lanes cite the same underlying source, repeat the same unsupported assertion, rely on a derivative summary, misunderstand the architecture or refer to a legally stale status.

Earlier project wording about preserving duplicate findings for confidence scoring is controlled by the later no-vote rule. Recurrence may raise a review priority; it may not determine a conclusion. Exact duplicates, PDF/Markdown renderings of the same report, copied transport bundles and multiple fragments from one session add no independent evidentiary weight.

## 12.4 Model outputs as evidence, not votes

> **NO-VOTE CONTROL**
>
> Project mC does not decide technical truth, patentability, approval or concept selection by counting model outputs.
>
> - Six research lanes are not six votes.
> - Two valid syntheses are not two votes.
> - Two final adjudications are not two votes.
> - A compiled follow-up remains part of the same lane.
> - Several fragments from one session remain one partial lane.
> - Duplicate files and alternate formats remain one logical source.
> - Repeated unsupported claims do not become reliable through recurrence.
>
> Every conclusion must be resolved through authority, concept fidelity, source traceability, claim-level reasoning, technical realism, completeness and human verification.

A model output can have evidentiary value. It may locate a primary source, identify a contradiction, explain a mechanism, expose an experimental confound, propose a baseline, identify claim language that requires legal review or show that an apparent novelty argument is weaker than first assumed. That value is claim-specific. A report may be strong in hardware analysis and weak in legal status; complete in prior-art search and incomplete in experiment design; concept-faithful overall but unsupported in one conclusion.

The controlled workflow therefore avoids report-level “pass/fail” simplification where section-level treatment is possible. However, when a concept swap is inseparable from the report’s reasoning, the output is invalid for the frozen concept as a whole. This was the case for the failed OpenBraille moving-roller synthesis and failed VibeGuard software-security synthesis.

Model agreement cannot override the current authority set. Architecture facts come from the final architecture, memory and SOP. Approval state comes from an explicit controlling record. Physical performance comes from configured tests. Patent-family and legal status require current official-source verification. Freedom-to-operate requires claim-focused legal analysis. No number of model outputs substitutes for these sources.

## 12.5 Synthesis and adjudication roles

### 12.5.1 Synthesis role

A concept synthesis is a controlled analytical transformation. It takes current project authority and independent research as inputs, audits their relationship and produces a structured technical and patent-evidence assessment.

A valid synthesis may:

- confirm the physical inventory and identify missing or duplicated inputs;
- restate and lock the current architecture;
- audit each lane for concept fidelity, source quality, completeness and reliability;
- verify load-bearing technical and patent assertions;
- distinguish source statements, analysis, inference, recommendation and unresolved uncertainty;
- compare frozen features against cited prior art;
- keep novelty, inventive step, patent eligibility, infringement and FTO separate;
- identify what the semester MVP can and cannot demonstrate;
- propose controlled experiments, baselines, ablations and kill conditions;
- describe a conditional later patent-development path.

A synthesis may not:

- override Decision Register v1.2 or a final architecture;
- import another synthesis where blindness is required;
- reconstruct a missing conclusion;
- treat convergence as majority proof;
- promise patent grant, novelty, inventive step, eligibility or FTO;
- substitute a different concept;
- state that hypothetical mechanisms have been built or validated;
- create teacher, procurement, Phase 4 or filing authorization.

A valid synthesis is therefore neither a raw model answer nor a final project decision. It is an audited intermediate evidence product.

### 12.5.2 Adjudication role

The final adjudication process compares the selected concept-faithful syntheses under the common authority and evidence set. Its role is cross-concept normalization and decision support. It should ask whether each synthesis fairly represents the frozen MVP, whether later patent routes are being compared at the same maturity level, whether semester buildability is being confused with speculative future value and whether the proposed experiments are capable of killing weak hypotheses.

The two final adjudications can recommend a semester direction and identify competing future research paths. They remain decision context. They do not:

- prove the teacher accepted the proposed OpenBraille-to-VibeGuard shift;
- amend Decision Register v1.2;
- replace a final architecture;
- authorize procurement or Phase 4;
- prove that D11, VPD-C7, PIRG, transfer/remount or another future mechanism works;
- authorize a patent filing;
- determine inventorship.

Where adjudications disagree, the disagreement must be preserved. It is not resolved by counting which concept each adjudication preferred. The project must examine the authority, assumptions, evidence and required experiments behind the disagreement.

## 12.6 Governing instructions

Governing instructions are workflow authority for a named task. They define the intended scope, permitted inputs, source hierarchy, concept-fidelity requirements, evidence cut-off, exclusions, required output and prohibited claims. They are essential provenance because they allow a reviewer to compare what an output was asked to do with what it actually did.

Representative instructions imposed the following safeguards:

- OpenBraille synthesis had to preserve the six-servo macro-cell and treat earlier Phase 2 work as historical search leads rather than current architecture authority.
- VibeGuard synthesis had to preserve passive single-node vibration monitoring and exclude software-security, active-cancellation, cloud predictive-maintenance and comparable substitutions.
- TrueMoist synthesis had to preserve the validated 72-run local compensation architecture and exclude Decision Register v1.1 and the superseded 135-run branch.
- Final adjudication had to use Decision Register v1.2, common comparative evidence and only the six selected syntheses, while holding failed concept swaps and the supplementary TrueMoist audit outside the blind package.

An instruction proves what was required. It does not prove downstream compliance. A perfectly written prompt can produce a non-compliant report. A model may ignore exclusions, confuse a filename, overstate legal status or substitute a more familiar architecture. Human review must compare the report against the instruction, the package and the higher authority.

For reproducibility, the instruction should be preserved without silent rewriting. Later corrections should be versioned, dated and linked to the affected output. A revised instruction cannot retroactively change what an earlier output was asked to do.

## 12.7 Manifests, launchers and transport files

Project mC distinguishes transport control from substantive evidence.

| File class | What it may establish | What it may not establish |
|---|---|---|
| Input manifest | Expected attachments, filenames, roles, sizes, hashes and package completeness | Truth, technical validity, novelty, approval, performance or research completeness |
| Exclusion/provenance register | Selected and excluded identities, paths, hashes, filename crossing and package composition | Correctness of a selected report merely because it was selected |
| Launcher | The initiating prompt or instruction used to begin a workflow | That the platform followed the prompt or produced a correct result |
| Upload checklist | Delivery and operator checks | Technical corroboration |
| Reduced-file bundle | A transport representation created for upload limits | A replacement for original sources or an independent source |
| Package validation | Copy, hash and delivery status | Architecture, patent, approval or experimental proof |

A manifest answers “what was delivered?” It does not answer “is the content true?” A launcher answers “what instruction was sent?” It does not answer “was the instruction followed?” A transport bundle answers “how was the material moved under platform limits?” It does not create a new source.

Merged or reduced bundles must retain traceability to their original files. The bundle should not become the citation target when the original organized-workspace path is available. Exact content already represented elsewhere should be logged, not counted again. Credentials, private keys and sensitive files must remain excluded from transport packages.

This separation is particularly important in AI workflows because a detailed manifest or launcher can appear authoritative. Their authority is procedural. They support auditability but carry no independent technical weight.

## 12.8 Provenance and exclusion registers

A provenance register records the identity and controlled status of evidence entering or leaving a workflow. The final adjudication exclusion/provenance register demonstrates the required standard. It recorded source paths, byte counts and SHA-256 values; avoided selecting convenience copies for common authority; selected Decision Register v1.2 while excluding v1.1; identified each selected synthesis by original filename, source path, controlled destination, model/mode, hash, completeness and concept fidelity; separated failed outputs; kept the supplementary TrueMoist audit outside the blind package; and resolved the OpenBraille filename crossing without renaming the originals.

This record supports conclusions about identity, inclusion, exclusion and workflow sequence. It does not make a selected synthesis technically authoritative. Selection can mean only that the report was the intended input for a controlled comparison. The report’s technical claims remain subordinate to the current project authority and claim-level audit.

An exclusion record should state:

1. exact identity and original path;
2. reason for exclusion;
3. whether exclusion is technical, procedural, completeness-related, security-related or scope-related;
4. whether any residual use is permitted;
5. which canonical source controls instead;
6. whether the exclusion applies to the entire report or separable sections;
7. whether later authorized review is allowed.

Exclusion must not become silent deletion. Preserving a failed or excluded record can be necessary to demonstrate that it was recognized and prevented from contaminating the current evidence set.

## 12.9 Partial, fragmented and incomplete model outputs

Project mC preserves partiality rather than disguising it.

OpenBraille’s Perplexity lane is marked partial. VibeGuard’s Mistral material is one partial compilation of three sequential fragments; its third fragment is a commercial-actor appendix, not a final report, and no final verdict exists. TrueMoist’s Perplexity lane is partial. The TrueMoist Qwen compilation contains an initial substantive output and a follow-up response from one lane. The follow-up does not transform unsupported statements in the initial output into verified evidence.

A partial source may still be useful. Complete and traceable sections can provide:

- primary-source leads;
- technical terminology;
- known actors or patent families requiring verification;
- experimental risks;
- alternative baselines;
- questions that the final synthesis should investigate.

Its use must remain proportional to what is actually present. A fragment cannot be described as a complete report. A partial lane cannot be said to have reached a final conclusion. Several fragments cannot be counted as several independent sources. A compiled file is a preservation device, not additional corroboration.

The reviewer should record the missing section, whether the source ends abruptly, whether the absent material is a conclusion or appendix, whether any claims depend on the missing text and which complete portions remain usable. This record should travel with the source into later syntheses.

## 12.10 Missing-conclusion and non-reconstruction rule

The non-reconstruction rule is mandatory:

> A conclusion absent from the source remains absent. It must not be inferred from fragments, report structure, other models, prior-chat context or the reviewer’s expectation.

Accordingly, the reviewer must not:

- infer a verdict from the direction of an incomplete analysis;
- combine unrelated fragments into a conclusion the original lane never gave;
- treat an appendix as a missing conclusion;
- use the majority view of other models to fill a gap;
- assume that a continuation existed because a heading sequence suggests one;
- import a conclusion from a different synthesis or conversation;
- silently complete unfinished prose.

The correct labels are “partial,” “unavailable,” “unresolved” or “no final verdict.” These labels are not weaknesses to be hidden; they are accurate evidence states.

Non-reconstruction protects provenance and authorship. A reconstructed conclusion would be new content created by the later reviewer while being falsely attributed to the original lane. It would also conceal the degree of uncertainty entering the synthesis.

## 12.11 Filename crossing and concept-swap controls

### 12.11.1 OpenBraille filename crossing

The OpenBraille workflow contained an accidental crossing between two mode filenames. The file named `OpenBraille_Patent_Synthesis_ChatGPT_Standard_High_no_deeprsearch.md` is the valid concept-faithful secondary/Deep Research synthesis and is controlled as `02_OpenBraille_Patent_Synthesis_Valid_Secondary.md`. It preserves the six-servo and eccentric-cam architecture.

The file named `OpenBraille_Patent_Synthesis_ChatGPT_Deep_Research.md` is the failed Standard High output. It substitutes an Arduino Mega/RAMPS moving-roller, encoder-wheel and dimpled-roller embosser. It is excluded.

The resolution is based on content, original path, hash, architecture fidelity and controlled destination—not on the misleading mode name. The original names remain preserved for provenance. Renaming history must not be used to obscure which bytes were reviewed.

### 12.11.2 Concept-swap detection

Every research and synthesis task should include a concept restatement and architecture-fidelity tripwires. A concept swap is material when the output’s mechanism, controller, sensing method, actuation, objective or validation logic no longer describes the frozen project.

Controlled tripwires include:

- OpenBraille must remain the six-servo macro-cell, not a moving roller, encoder wheel, RAMPS/Mega system or embosser architecture.
- VibeGuard must remain target-mounted vibration monitoring, not artifact, dependency, configuration or secret scanning.
- TrueMoist must remain the 72-run local compensation experiment using known S0/S1 treatment metadata, not a live-EC, universal multi-soil, cloud or online-adaptive system.

A concept-swapped output is retained as negative provenance. It may show why the failure happened and how future prompts should improve. It may not be averaged with valid syntheses, mined for favorable patent statements about the frozen concept or presented as an alternate current architecture.

## 12.12 Human verification and final accountability

Human control is required wherever information becomes authority, evidence or action.

Humans must:

- define project requirements and approve the governing task;
- freeze the architecture and record the current version;
- assemble and verify the package;
- classify sources by authority and lifecycle;
- audit model fidelity, completeness and sourcing;
- decide whether an output is valid, partial, failed, supplementary or excluded;
- verify hardware identity, wiring, configuration and measurements;
- conduct and sign off physical experiments;
- record teacher and institutional decisions;
- control procurement and Phase 4 entry;
- preserve contributor chronology and confidential invention records;
- decide whether institutional IPR or legal review is warranted;
- accept responsibility for every statement released in the Master Manual.

A model may suggest a mechanism or claim direction. That suggestion alone does not determine inventorship, authorship or ownership. The workflow records do not establish who conceived a patent claim, who contributed to reduction to practice, who should be named as an inventor or who owns resulting rights. Those questions require dated human contribution records, institutional policy and appropriate IPR review. Part VI makes no determination on them.

Human review should not be reduced to approving polished prose. The reviewer must verify load-bearing claims against the cited source, check that current architecture is not replaced by archived detail, confirm that partiality is visible, preserve disagreement and reject statements that exceed the evidence boundary.

## 12.13 AI-use disclosure requirements

A controlled AI-use disclosure should be specific enough to support audit without claiming that AI work is self-validating. At minimum, it should disclose:

- the workflow purposes for which AI systems were used;
- the named model lanes and modes where controlled records exist;
- the governing instruction and evidence cut-off;
- the exact input package or manifest;
- major exclusions and concept-fidelity rules;
- the distinction between independent lanes, synthesis and adjudication;
- the fact that model outputs were not counted as votes;
- the presence of partial, failed, fragmented or supplementary outputs;
- the treatment of filename crossings and concept swaps;
- the human review and acceptance responsibility;
- the external-verification and physical-testing limits.

The disclosure should state that AI systems supported research, synthesis, adversarial audit, organization and decision support. It should not state that the AI systems approved the concept, established patentability, supplied legal advice or became inventors.

Disclosure must also preserve confidentiality boundaries. A reproducibility record does not require public release of private keys, credentials, sensitive personal information or confidential invention material. Such items should be excluded or referenced through controlled internal records.

## 12.14 Reproducibility package for AI-assisted workflows

A minimum reproducibility package should contain:

1. the governing instruction;
2. the exact input manifest and original source paths;
3. file hashes or immutable identifiers;
4. the launcher or initiating prompt where relevant;
5. model, mode and date where recorded;
6. the complete output without silent editing;
7. a reliability and concept-fidelity assessment;
8. an exclusion and provenance register;
9. the selected synthesis or adjudication record;
10. a contradiction and unresolved-item register;
11. a human review record;
12. a change log for later revisions.

For fragmented outputs, the package should preserve sequence and label the compilation as one lane. For crossed filenames, it should preserve original names and record the content-based resolution. For reduced-file bundles, it should retain a map to the original separate files. For excluded outputs, it should preserve the exclusion reason and permitted residual use.

A reviewer attempting reproduction should be able to answer:

- What task was the model asked to perform?
- Which exact sources were available?
- Which sources were excluded?
- Which architecture controlled?
- Was the output complete?
- Which claims were verified?
- Which conclusions remained unresolved?
- Which human decision admitted or excluded the output?
- What changed after the run?

Reproducibility does not mean identical prose. Model behavior, platform state and sampling can change. The controlled objective is process inspectability and claim traceability.

## 12.15 Chapter conclusion

Project mC’s AI-assisted workflow is credible only when its limits are visible. Independent lanes broaden coverage but do not vote. Syntheses audit and transform evidence but do not control architecture. Adjudications compare and recommend but do not create approval. Manifests prove package identity, launchers prove prompt transport and provenance registers prove selection or exclusion; none of these proves technical truth.

Failed concept swaps are excluded, partial lanes remain partial and missing conclusions are not reconstructed. Human reviewers control architecture, evidence admission, testing, approval, procurement, IPR escalation and final publication. The resulting workflow is not a substitute for engineering or legal verification. It is a disciplined method for preserving what was asked, what was supplied, what was produced, what was accepted, what was rejected and why.

## 12.S Source notes

The following original organized-workspace paths were materially relied upon for Chapter 12.

### Current source-policy and decision-evidence controls

- `08_MASTER_MANUAL/01_Source_Index/MASTER_MANUAL_SOURCE_POLICY.md` — authority tiers, TIER_5 limitation and manual-writing rule.
- `03_CONCEPT_PORTFOLIO/OpenBraille/PATENT_EVIDENCE_INDEX.md` — OpenBraille lane and synthesis set, partial status and failed-output exclusion.
- `03_CONCEPT_PORTFOLIO/VibeGuard/PATENT_EVIDENCE_INDEX.md` — VibeGuard lane and synthesis set, partial Mistral treatment and failed-output exclusion.
- `03_CONCEPT_PORTFOLIO/TrueMoist/PATENT_EVIDENCE_INDEX.md` — TrueMoist lane and synthesis set and supplementary-audit exclusion.
- `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/02_Authoritative_Source_Manifest.md` — comparative authority roles and non-authoritative exclusions.

### Provenance and workflow controls

- `06_TRANSPORT_AND_PROVENANCE/TRANSPORT_AND_PROVENANCE_INDEX.md` — role of instructions, manifests, launchers, bundles and validation.
- `06_TRANSPORT_AND_PROVENANCE/01_Governing_Instructions/Project_mC_Final_Adjudication_Instructions_CANONICAL.md` — blind adjudication, no-vote rule, confidentiality and inventorship boundary.
- `06_TRANSPORT_AND_PROVENANCE/02_Input_Manifests/Final_Adjudication_EXCLUSION_AND_PROVENANCE_REGISTER.md` — selected/excluded synthesis provenance, hashes and OpenBraille filename-crossing resolution.
- `06_TRANSPORT_AND_PROVENANCE/01_Governing_Instructions/OpenBraille_Synthesis_Instructions_CANONICAL.md` — architecture fidelity and synthesis independence.
- `06_TRANSPORT_AND_PROVENANCE/01_Governing_Instructions/VibeGuard_Synthesis_Instructions_CANONICAL.md` — architecture fidelity, partial-lane handling and synthesis independence.
- `06_TRANSPORT_AND_PROVENANCE/01_Governing_Instructions/TrueMoist_Synthesis_Instructions_CANONICAL.md` — six-lane treatment, compilations, partiality and supplementary exclusion.
- `06_TRANSPORT_AND_PROVENANCE/02_Input_Manifests/OpenBraille_Synthesis_INPUT_MANIFEST.md`
- `06_TRANSPORT_AND_PROVENANCE/02_Input_Manifests/VibeGuard_Synthesis_INPUT_MANIFEST.md`
- `06_TRANSPORT_AND_PROVENANCE/02_Input_Manifests/TrueMoist_Synthesis_INPUT_MANIFEST.md`
- `06_TRANSPORT_AND_PROVENANCE/03_Launchers_and_Checklists/VibeGuard_Synthesis_Launcher_FINAL.txt`
- `00_START_HERE/07_STAGE5_TRANSPORT_PROVENANCE_VALIDATION.md` — transport/provenance copy validation and role limits.

### Post-freeze mapping control

- `08_MASTER_MANUAL/02_Chapter_Source_Maps/12_Research_Provenance_and_AI_Workflow_Control_SOURCES.md` — chapter mapping only; not technical evidence.

# Chapter 13 — Superseded, Failed, Partial and Archived Routes

## 13.1 Chapter purpose and archive boundary

Project mC’s archive is a controlled historical and negative-evidence system. It preserves prior project states, discarded architecture branches, failed research outputs, incomplete lanes, intentionally excluded supplements, convenience copies, duplicate formats, legacy packages and unrelated exclusions. Its purpose is traceability: a reviewer should be able to understand how the project changed, which errors were detected, which sources were rejected and which current records replaced them.

Archive presence does not grant current authority. A detailed archived report may be more verbose than the current canonical source and still have no operational effect. A failed report may contain technically plausible statements and still be invalid for the frozen concept. A superseded decision register may accurately describe an earlier state and still be prohibited from controlling the current state.

The repaired Chapter 13 packet selected seventeen sources: archive controls, failed OpenBraille and VibeGuard outputs, the excluded TrueMoist supplementary audit, superseded decision and architecture records, legacy fragments and variants, the intentional-exclusion register, Stage 8 archival validation and log, and a post-freeze chapter map. All seventeen were extracted successfully. Their evidentiary role is limited to archive classification, chronology, negative provenance, exclusion, duplicate history and canonical replacement.

This chapter does not reopen or expand legacy ZIPs. It does not revalidate archived patent assertions. It does not merge superseded and current architectures. When an archived record is consulted, the archive class, current replacement and permitted residual purpose must be stated.

## 13.2 Archive classification system

| Archive class | Definition | Permitted residual use | Authority effect |
|---|---|---|---|
| Superseded governance record | Earlier decision, status or authority record replaced by a later controlling version | Decision chronology and explanation of changed status | No current operational authority |
| Superseded architecture or patch | Earlier architecture, memory, patch or design branch replaced by the final architecture | Historical engineering rationale and discarded alternatives | Must not define current build, BOM, validation or patent route |
| Failed concept-swapped output | Report that materially analyzed a different mechanism or concept | Negative provenance and workflow-failure analysis | Invalid for the frozen concept |
| Partial or fragmented lane | Incomplete output or fragment without a complete final conclusion | Verified complete portions and research leads only | Partial status remains; no reconstructed verdict |
| Excluded supplementary report | Substantive report intentionally held outside a controlled package | Only separately authorized later use with disclosure | No effect on the set from which it was excluded |
| Historical draft or convenience variant | Draft, copied-folder version or older presentation/report variant | Development history and availability | Canonical source controls |
| Exact duplicate or format derivative | Byte-identical copy or alternate rendering of the same logical content | Preservation and presentation | No independent corroborative weight |
| Legacy ZIP | Original archive package retained as received | Package history and disaster-recovery reference | Members do not override canonical files |
| Unrelated quarantine or intentional exclusion | Non-project, sensitive, temporary or excluded content | Proof of boundary and exclusion decision | Not Project mC evidence |

These classifications prevent a common archival error: treating all preserved files as equally usable. Preservation answers whether a record remains available. Authority answers whether it can control a present claim. The two questions must be kept separate.

## 13.3 Superseded governance and decision records

Decision Register v1.2 controls current recorded Project mC decisions. Decision Register v1.0 and v1.1 remain historical records only.

### 13.3.1 Decision Register v1.0

The archived convenience-folder v1.0 is byte-identical to the historical saved v1.0 record. It describes an earlier project state in which Phase 3C completion and portfolio status differed from the later controlled position. It may be used to explain what the team believed or had completed at that time and to show why explicit version control became necessary.

It may not be used to:

- describe the current completion state;
- omit later TrueMoist completion;
- restore earlier portfolio status;
- override v1.2;
- prove a teacher decision made after its date.

When a manual statement relies on a decision register, the version should be named where ambiguity could matter. The phrase “the Decision Register” is inadequate if an archived version might support a different result.

### 13.3.2 Decision Register v1.1

The archived v1.1 is located within the earlier TrueMoist Claude architecture branch. It belongs to the same superseded route as the 135-run design. Current synthesis controls expressly exclude it from governing the validated TrueMoist architecture.

Its residual use is limited to tracing that branch and explaining the transition to v1.2. It cannot be cited as an alternate current authority or merged with later decisions.

## 13.4 Superseded concept architectures and patches

The principal superseded architecture branch in the repaired Chapter 13 packet concerns TrueMoist. The archived branch includes a historical PDR patch, an earlier Claude architecture report, an earlier memory and Decision Register v1.1.

That branch selected a D+B hybrid, treated ADS1115 as mandatory and used a 135-sample design formed from five moisture levels, three temperature levels, three salinity levels and three replicates. The historical patch also records the later accepted PDR-058 direction: a 72-run design formed from four moisture levels, three temperature levels, two salinity treatments and three independent replicates.

Validated Part IV controls the current TrueMoist identity:

- one genuine analog capacitive probe for the final dataset;
- a nearby DS18B20;
- known S0/S1 treatment metadata rather than live conductivity measurement;
- evidence-gated acquisition;
- offline fitting and fixed local coefficients;
- USB CSV evidence;
- gravimetric water-content validation;
- 72 independent physical runs as the selected design, not proof that those runs were completed.

The superseded 135-run branch remains useful for understanding earlier design preferences, ADC assumptions, model choices, cost reasoning and the disagreement that led to revision. It may not define the current sample count, mandatory ADC, model, platform, cost, readiness or validation status when those points conflict with Part IV.

No archived design should be blended with a current architecture to create an undocumented hybrid. A former component choice can re-enter the project only through formal change control based on current engineering justification, not because it appears in a detailed historical report.

## 13.5 Failed OpenBraille concept-swap output

The archived OpenBraille failed synthesis analyzes an Arduino Mega/RAMPS moving-roller, encoder-wheel and dimpled-roller embosser. It reaches favorable novelty, FTO and implementation conclusions about that substituted mechanism. It is not an alternate valid OpenBraille architecture.

Validated Part II controls OpenBraille as one non-standard macro six-dot cell using six SG90-class servos, six eccentric-cam/follower channels, six guided pins, ESP32 direct PWM, external servo power, USB evidence logging, active raise/retract and single-dot-first commissioning.

The failed output is retained unchanged for the following residual uses:

- demonstrating that a short concept name is insufficient to preserve architecture;
- showing how a misleading filename and familiar mechanism can cause drift;
- training future reviewers to require an architecture restatement;
- documenting why content and fidelity must override mode labels;
- preserving the exclusion decision.

It is prohibited to cite the failed report’s patent, FTO, feasibility or status conclusions as evidence for the six-servo design. Apparently generic passages must also be excluded when they are inseparable from the substituted mechanism. The report is not an additional synthesis, alternative architecture or vote.

## 13.6 Failed VibeGuard concept-swap output

The archived VibeGuard failed synthesis substitutes a software-security publishing gate that uses artifact, configuration, secret and dependency scanners. Its prior-art analysis concerns static analysis and secret scanning, not target-mounted vibration monitoring.

Validated Part III controls VibeGuard as one rigidly mounted ADXL345-class tri-axis accelerometer, one ESP32-class controller, SPI acquisition, a controlled rotating test article, repeatable normal and safe induced-abnormal states, RMS plus persistence, supporting FFT or band analysis, optional ordinary Mahalanobis only after baseline gates, RGB indication and USB evidence logging.

The failed scanner report is retained as negative provenance. It illustrates name-driven concept drift and the need to restate the sensor, controller, measured phenomenon, analysis pipeline and test article before substantive research begins. Its scanner taxonomy, novelty assessment, FTO discussion and recommendations are not VibeGuard vibration evidence. It is not counted among the two valid syntheses.

Generic cybersecurity wording cannot be extracted from the failed report to make it appear relevant. The controlling question is whether the reasoning concerns the frozen vibration-monitoring system. If not, the passage has no current evidentiary role.

## 13.7 Partial and fragmented research lanes

Partial and fragmented records require more careful treatment than either valid complete reports or failed concept swaps. Their useful portions may remain concept-faithful, but their evidentiary scope is limited.

Three representative legacy records illustrate the rules.

**VibeGuard Qwen2 variant.** The Qwen2 file is an earlier or duplicate variant. The controlled VibeGuard Qwen path under the concept portfolio defines the selected lane identity. The archived variant may support filename and version chronology but adds no independent weight.

**VibeGuard Mistral fragment.** The archived “mistral 2” file is one fragment in a three-fragment lane. The controlled partial compilation preserves the fragments as one source. No final verdict exists. Complete passages can supply verified leads, but the fragment cannot be used as a standalone report or combined with assumptions to create a missing conclusion.

**TrueMoist Qwen #0.** The #0 file is the initial part of a later compilation that includes a follow-up response. Both belong to one lane. The follow-up does not make unsupported earlier statements reliable, and the two components are not separate votes.

The general rule is that compilation preserves sequence; it does not multiply evidence. A later editor must not create a more complete report than the source record supports.

## 13.8 Excluded supplementary TrueMoist audit

The supplementary TrueMoist Work Max web audit is complete and concept-faithful, but it was deliberately held outside the blind synthesis package and outside the controlled six-lane adjudication set. Its exclusion is procedural. It does not mean that every statement in the audit is false, nor does its apparent quality permit silent inclusion.

The audit may establish only that a separate supplementary review existed and that it described itself as technical and patent research rather than legal advice. It may be considered later only under the adversarial role expressly authorized by a controlling record, with clear disclosure that it was not part of the blind set.

It must not be:

- counted as a seventh TrueMoist lane;
- merged into either valid TrueMoist synthesis;
- described as a source used by the blind syntheses or adjudications;
- imported from prior-chat context;
- used to change the earlier controlled comparison retroactively.

If later authorized, its findings must be evaluated as a separately disclosed supplement with their own source and reliability audit.

## 13.9 Historical drafts, convenience variants and duplicate formats

Historical drafts and convenience files preserve development and guard against accidental loss. They do not create multiple independent sources.

The legacy duplicate audit identified twenty exact-duplicate groups covering forty working-tree files. Examples included convenience and canonical copies of the Engineering Design Review, copied Phase 2 and Phase 3 reports and memories, v1.0 decision-register copies, material duplicated under an “every SOP and memory” folder and a TrustLatch convenience copy.

The audit also identified cross-format and near-equivalent cases:

- a Claude Phase 2 PDF and Markdown were strong near-equivalents, with Markdown the probable editable source and PDF the presentation derivative;
- a Qwen Phase 2 PDF and Markdown substantially overlapped but were not equivalent and therefore remained separate;
- VibeGuard `.md` and `.mmd` prompts normalized to identical text while differing as binary files, requiring manual confirmation;
- six ZIPs contained twenty-three members, twenty-two of which were byte-identical to normal working-tree files; the unmatched `contexts.zip/MC_Project_PHASE_DOC.md` was an older roadmap variant.

These findings establish the following controls:

- similar names do not prove duplication;
- exact SHA-256 equality proves byte identity but not authority;
- format derivatives normally remain one logical evidentiary source when content-equivalent;
- substantial overlap alone is insufficient to collapse sources;
- canonical paths control over convenience folders;
- no candidate should be deleted solely from filename or partial text similarity;
- legacy ZIPs remain preserved and unopened in this stage.

A duplicate copy may be important for transport history or publication, but it cannot strengthen the underlying technical claim.

## 13.10 Unrelated quarantine and intentional exclusions

The intentional-exclusion record identifies three unrelated files that remained in the untouched original repository and were not admitted to the organized Project mC evidence collection:

- `/home/paradoxpete/Documents/PROJECT/ZEROTH PRESENTATION/panicker.pptx`;
- `/home/paradoxpete/Documents/PROJECT/ZEROTH PRESENTATION/panicker.py`;
- `/home/paradoxpete/Documents/PROJECT/Tentative Course List (July - Dec 2026) - Google Drive.html`.

The first two were unrelated OOMD or seminar material. The third was an unrelated course-planning export. Sensitive credentials, private keys, office lock files and temporary files were also excluded under security and hygiene rules.

An exclusion record proves that the boundary was deliberate. It does not convert the excluded content into evidence, require its reproduction or imply that sensitive material should be opened. The correct manual treatment is to record the exclusion category and reason, not summarize unrelated content.

## 13.11 Canonical replacement rules

Canonical replacement is determined by authority, identity and current status—not by the newest modification timestamp, the longest report or the most convenient folder.

| Archived material | Current canonical control | Permitted residual use |
|---|---|---|
| Decision Register v1.0 and v1.1 | `01_GOVERNANCE_AND_CONTROL/02_Decision_Registers/Project_mC_Decision_Register_v1.2.md` | Earlier decision chronology |
| Earlier TrueMoist 135-run architecture, memory and patch | Final TrueMoist architecture, memory and SOP under `03_CONCEPT_PORTFOLIO/TrueMoist/01_Final_Architecture/` | Explain discarded branch and transition |
| Failed OpenBraille moving-roller synthesis | Two controlled concept-faithful OpenBraille syntheses and validated Part II | Negative provenance only |
| Failed VibeGuard scanner synthesis | Two controlled concept-faithful VibeGuard syntheses and validated Part III | Negative provenance only |
| TrueMoist supplementary Work Max audit | No replacement inside the blind set; the controlled valid syntheses remain Max and High + Deep Research | Later separately authorized adversarial reference |
| VibeGuard Mistral fragment | `05_VibeGuard_Patent_Research_Mistral_PARTIAL_COMPILATION.md` | Verified fragment-level leads only |
| TrueMoist Qwen #0 | `04_TrueMoist_Patent_Research_Qwen_COMPILATION.md` | Initial-lane chronology |
| Convenience copies | Matching canonical governance, phase or concept path | Availability and folder history |
| Historical presentation drafts | Official controlled submission identified in Part V | Presentation-development history |
| Exact ZIP members | Normal canonical working-tree source | Package preservation |

A canonical replacement does not erase history. It establishes which record governs a present statement. The archived source remains available to explain what changed.

## 13.12 Conditions for consulting archived material

Archived material may be consulted only for a declared purpose, including:

- reconstructing chronology;
- explaining why a decision changed;
- identifying a superseded assumption;
- analyzing a concept-fidelity or workflow failure;
- tracing an original filename or path;
- checking duplicate or variant status;
- preserving negative results and discarded alternatives;
- identifying an exclusion or quarantine boundary;
- confirming the current canonical replacement.

Before citing an archived record, the reviewer must:

1. identify its archive class;
2. identify the current canonical replacement, where one exists;
3. state the residual purpose;
4. use past-tense or historical wording;
5. preserve failed, partial, supplementary or excluded labels;
6. check for conflict with validated Parts I–V;
7. avoid importing technical conclusions beyond the residual purpose;
8. avoid opening or expanding archives unless a later authorized stage requires it.

This procedure allows the archive to remain useful without becoming a hidden second authority system.

## 13.13 Prohibited resurrection of archived claims

The following actions are prohibited:

- using Decision Register v1.0 or v1.1 to override v1.2;
- restoring the TrueMoist 135-run branch as current;
- describing OpenBraille as a moving-roller, RAMPS or Mega design;
- describing VibeGuard as a software-security scanner;
- importing novelty or FTO language from a failed concept swap;
- inventing a Mistral final verdict;
- counting Qwen fragments or follow-ups as separate lanes;
- adding the supplementary TrueMoist audit to the blind set;
- treating a convenience copy as corroboration;
- treating a byte-identical ZIP member as a new source;
- using unrelated quarantine as Project mC evidence;
- inferring approval or Phase 4 status from an old roadmap or presentation draft;
- silently merging old and current architectures.

A later team may revisit an abandoned idea, but that would require a new authorized project branch, new architecture control and new evidence. It cannot occur through casual citation of the archive.

## 13.14 Chapter conclusion

Project mC’s archive is valuable because it preserves both successful and unsuccessful development. Its value depends on disciplined status labels and canonical replacement. Decision Register v1.2 controls over earlier versions. The 72-run TrueMoist design controls over the 135-run branch. The failed OpenBraille and VibeGuard syntheses remain invalid for the frozen concepts. Partial lanes remain partial. The supplementary TrueMoist audit remains outside the blind set. Duplicate copies and format derivatives add no independent weight.

The archive may explain chronology, error, exclusion and change. It may not supply current architecture, approval, patent or performance claims. Every archived citation must identify what replaced it and why it is being consulted.

## 13.S Source notes

The following original organized-workspace paths were materially relied upon for Chapter 13.

### Archive controls

- `09_ARCHIVE/ARCHIVE_INDEX.md`
- `09_ARCHIVE/03_Failed_or_Partial_Research/README.md`

### Failed concept-swapped outputs

- `09_ARCHIVE/03_Failed_or_Partial_Research/OpenBraille/FAILED_CONCEPT_SWAP_OpenBraille_Deep_Research_Synthesis.md`
- `09_ARCHIVE/03_Failed_or_Partial_Research/VibeGuard/FAILED_CONCEPT_SWAP_VibeGuard_Deep_Research_Synthesis.md`

### Excluded supplementary report

- `09_ARCHIVE/03_Failed_or_Partial_Research/TrueMoist/SUPPLEMENTARY_EXCLUDED_TrueMoist_Work_Max_Web_Audit.md`

### Superseded governance and architecture

- `09_ARCHIVE/01_Superseded/Convenience_Folder_Variants/COPY PASTE FOLDER/Project_mC_Decision_Register_v1.0.md`
- `09_ARCHIVE/01_Superseded/TrueMoist/Earlier_Claude_Architecture/Project_mC_Decision_Register_v1_1.md`
- `09_ARCHIVE/01_Superseded/TrueMoist/Phase3C_TrueMoist_PDR_Patch_Historical.md`
- `09_ARCHIVE/01_Superseded/TrueMoist/Earlier_Claude_Architecture/Phase3C_TrueMoist_Architecture_Report_by_Claude.md`
- `09_ARCHIVE/01_Superseded/TrueMoist/Earlier_Claude_Architecture/Phase3C_TrueMoist_MEMORY.md`

### Partial fragments and variants

- `09_ARCHIVE/03_Failed_or_Partial_Research/VibeGuard/Legacy_Fragments_and_Variants/research_on_f.patent_by_qwen2.md`
- `09_ARCHIVE/03_Failed_or_Partial_Research/VibeGuard/Legacy_Fragments_and_Variants/research on f.patent by mistral 2.md`
- `09_ARCHIVE/03_Failed_or_Partial_Research/TrueMoist/Legacy_Fragments_and_Variants/research on f.patent by qwen #0.md`

### Quarantine and archival audit

- `09_ARCHIVE/05_Unrelated_Quarantine/INTENTIONAL_EXCLUSIONS.md`
- `00_START_HERE/09_STAGE8_FINAL_ARCHIVAL_SWEEP_VALIDATION.md`
- `00_START_HERE/09_STAGE8_FINAL_ARCHIVAL_SWEEP_LOG.tsv`

### Post-freeze mapping control

- `08_MASTER_MANUAL/02_Chapter_Source_Maps/13_Superseded_Failed_Partial_and_Archived_Routes_SOURCES.md` — chapter mapping only; not technical evidence.

# Chapter 14 — Source Integrity Audit and Reproducibility

## 14.1 Chapter purpose and evidence boundary

Chapter 14 defines what the Project mC integrity system proves about source identity, preservation, mapping, exclusion and reproducibility. It also defines the limits of those controls.

The system may establish:

- a documented source-freeze boundary;
- exact byte identity through SHA-256;
- controlled source paths and canonical/duplicate decisions;
- stage-by-stage copy, rename, archive and exclusion records;
- chapter mapping for frozen sources;
- intentional-exclusion and quarantine boundaries;
- post-freeze construction records for the Master Manual;
- the package another reviewer needs to audit the process.

The system may not establish technical correctness, semantic completeness, teacher approval, physical success, patentability, legal status, FTO, supplier authenticity, current prices or specifications, or identical future model output.

Integrity and authority are separate dimensions. A perfectly preserved obsolete file remains obsolete. A current architecture can be authentic and still require testing. An adjudication can be complete and correctly hashed while remaining decision support. A teacher-facing document can be genuine without proving teacher acceptance.

The repaired Chapter 14 packet selected twenty-three sources. All twenty-three were extracted successfully as plain text, with no review-required or hash-failure item. The selected sources support the source-freeze, policy, duplicate, naming, mapping, archival, extraction and change-control account below. Their successful extraction does not prove exhaustive semantic coverage of the repository.

## 14.2 Frozen source state

The Project mC source freeze was established at `2026-08-03T21:59:10.355043+02:00`.

The freeze notice records that the organized workspace accounted for non-sensitive unique source content discovered in:

- `/home/paradoxpete/Documents/PROJECT`;
- `/home/paradoxpete/Documents/PROJECT_UPLOAD_PACKS`;
- the verified OpenBraille submission in Downloads.

A source was accounted for through either an exact SHA-256 representation inside `PROJECT_ORGANIZED` or a recorded and verified intentional exclusion.

The frozen source map contains 301 represented records, all verified unchanged at mapping time. New evidence created after the freeze must enter through a new logged stage. Existing canonical files must not be silently replaced.

The freeze is an accounting boundary, not a prohibition on development. It separates the known historical source state from later evidence and later manual-construction controls. A future revision can add evidence, correct a mapping or supersede a source, but the revision must preserve the prior release and show exactly what changed.

## 14.3 Physical files, unique content and represented-source accounting

Several different counts appear in the Project mC records. They measure different things and must not be merged.

| Count | Meaning | Controlled figure |
|---|---|---:|
| Frozen source-map records | Represented source paths and hashes assigned under the frozen map | 301 |
| Frozen chapter assignments | Chapter assignments in that map | 301 |
| Supplemental Stage 10S assignments | Additional representative assignments for Chapters 12–14 without changing the frozen map | 57 |
| Unique Stage 10S selected physical paths | Distinct source paths in the repaired selection | 53 |
| Stage 10S Chapter 12 selection | Selected and successfully extracted sources | 17 |
| Stage 10S Chapter 13 selection | Selected and successfully extracted sources | 17 |
| Stage 10S Chapter 14 selection | Selected and successfully extracted sources | 23 |
| Exact duplicate files in the legacy working tree | Multiple physical paths with identical SHA-256 | 20 groups / 40 files |
| Named unrelated Stage 8 exclusions | Files not admitted to organized evidence | 3, plus sensitive and temporary classes |

A physical file is a stored object at a path. Unique content is a byte sequence. A represented source is content accounted for in the organized system. A chapter assignment is a classification decision. One physical source may support more than one conceptual purpose, while several physical files may represent one logical source.

Represented-source accounting therefore establishes traceability, not truth. It shows that a specific byte sequence or exclusion record was accounted for. It does not prove that every relevant meaning was captured, that the source was interpreted correctly or that the source is technically reliable.

## 14.4 Canonical and duplicate resolution

Canonical selection follows authority and context.

- Current governance paths control over convenience copies.
- Current versioned records control over earlier versions.
- Final architecture paths control over raw research and superseded branches.
- Selected concept-faithful syntheses control over failed variants.
- An editable source and rendered derivative may both be retained for publication, but content-equivalent forms remain one logical source.
- Substantial overlap without equivalence is not enough to collapse two files.
- Similar filenames alone never prove duplication.

The legacy duplicate audit used SHA-256 for exact binary identity and format-aware extraction for cross-format comparison. It considered PDF text, DOCX XML, normalized text, word-trigram similarity and manual review. This method identified exact duplicates, near-equivalents, overlapping but distinct files and ZIP-member matches.

Duplicate detection guides canonical selection and cleanup. It does not determine authority without the hierarchy. A byte-identical old convenience copy and current canonical copy contain the same content, but only the controlled path may be appropriate for present citation. A high text-similarity score does not authorize deletion. Cross-format equivalence must be reviewed in context, especially when diagrams, tables, formatting or appendices may differ.

## 14.5 Hash and stable-path controls

> **HASH LIMITATION CONTROL**
>
> A SHA-256 match proves that two compared byte sequences are identical.
>
> It can support copy validation, silent-modification detection, exact-duplicate grouping and source selection.
>
> It does **not** prove:
>
> - technical truth or semantic accuracy;
> - authority or approval;
> - novelty, inventive step, patent eligibility or FTO;
> - current patent-family or legal status;
> - experimental performance;
> - equivalence between different file formats;
> - correct interpretation of the file.
>
> Identity must be followed by authority review, claim-level source audit and, where required, physical or external verification.

Stable paths add context to a hash. They indicate where the source belonged, which branch it represented and whether it was current, historical or archived. Path control is therefore part of reproducibility.

The Phase 3C naming validation demonstrates controlled path change. All thirty-one pre-existing Phase 3C files were mapped to final paths. No file was deleted or merged. Twenty-four remained byte-identical. Seven operational documents changed because approved filename references were updated. All thirteen raw or failed research files retained their hashes. Before-and-after hashes and rename mappings were recorded. Historical references retained old paths where changing them would alter the provenance record.

A path change is not automatically a content change. A hash change is not automatically a substantive change. Both require a logged explanation.

## 14.6 Frozen source map and unmapped-file register

The frozen source map assigns represented sources across the planned manual:

| Destination | Mapped sources |
|---|---:|
| Chapter 00 | 1 |
| Chapter 01 | 26 |
| Chapter 02 | 52 |
| Chapter 03 | 21 |
| Chapter 04 | 5 |
| Chapter 05 | 12 |
| Chapter 06 | 7 |
| Chapter 07 | 9 |
| Chapter 08 | 14 |
| Chapter 09 | 18 |
| Chapter 10 | 15 |
| Chapter 11 | 0 |
| Chapter 12 | 50 |
| Chapter 13 | 32 |
| Chapter 14 | 20 |
| Appendix A2 | 18 |
| Appendices A1, A3 and A4 | 0 direct mappings |

The map includes Tier 1 through Tier 5 and reference-only records. It is a chapter-classification system, not a claim-validity ranking.

The unmapped register contains one organized-workspace file:

`03_CONCEPT_PORTFOLIO/CONCEPT_PORTFOLIO_INDEX.md`

The recorded reason is that no frozen chapter rule matched its path. This does not mean the file was absent or lost. It means source accounting and chapter mapping are distinct controls. The file exists in the organized workspace with a recorded identity but did not receive a chapter assignment under the frozen rule.

A future mapping revision may assign it to a chapter or appendix. The frozen map must not be silently altered to hide the earlier unmapped state.

Chapter 11’s zero directly mapped sources is also significant. It confirms the status preserved in Part V: Chapter 11 is a future execution framework, not a history of procurement, fabrication, coding, testing or completion.

## 14.7 Original-repository preservation

The integrity system distinguishes:

1. original repositories and submissions;
2. organized canonical representations;
3. archives and exclusions;
4. post-freeze Master Manual controls and outputs.

Stage 10S recorded that the frozen source map was not modified, the original repository was not modified, no archive was expanded and no file was deleted. Earlier organization stages had their own logs and validations. Controlled moves and renames occurred before the freeze and were documented. The final archival sweep copied, deduplicated or intentionally excluded the Stage 7 records without silently overwriting conflicting destinations.

The correct preservation claim is not that every historical path remained unchanged forever. The records show that some controlled renames and reference-only edits occurred. The stronger and accurate claim is that the frozen state, organized representation, exclusions and later changes are distinguishable and auditable.

Original-repository preservation also supports rollback and forensic review. If a question arises about a canonical copy, the reviewer can compare hashes, naming logs and stage records rather than relying on memory.

## 14.8 Archive, exclusion and quarantine accounting

A complete integrity account includes material that was not admitted to the current evidence set.

Project mC separately accounted for:

- failed and concept-swapped research;
- fragmented and incomplete outputs;
- superseded architectures and decision registers;
- convenience variants and historical drafts;
- legacy ZIPs;
- peer projects treated as reference-only;
- unrelated files intentionally excluded;
- sensitive credentials, private keys, temporary files and office lock files excluded from the evidence collection.

An exclusion record proves deliberate boundary control. It does not establish that an excluded file was technically reviewed or that it should be exposed. A quarantine record protects the project from accidental contamination and protects sensitive material from unnecessary reproduction.

Archive and exclusion accounting should therefore be included in release checks. A release is incomplete if it lists only admitted sources while omitting known failed or excluded records that could later be mistaken for valid evidence.

## 14.9 Extraction and visual-review controls

The Stage 10S repaired packets used plain-text extraction for all selected sources:

- Chapter 12: 17 of 17;
- Chapter 13: 17 of 17;
- Chapter 14: 23 of 23;
- review-required items: zero;
- hash failures: zero.

For the repaired Chapter 14 selection, plain text was appropriate because the selected sources were Markdown and TSV controls. No visual review was required for that selection.

This result is local, not universal. The organized repository also contains PDFs, DOCX, PPTX and images. Text extraction may omit slide layout, diagrams, table structure, annotations, visual hierarchy or image content. A successful extraction flag proves that text was obtained. It does not prove that all visual meaning was captured.

Format-aware review should be required when:

- a diagram contains architecture information not represented in text;
- a slide’s ordering or visual emphasis affects interpretation;
- a table is garbled by extraction;
- an image is the primary evidence;
- a PDF or DOCX has materially different content from its editable source;
- a signature, approval mark or visible revision status matters.

Visual review establishes that the relevant visual content was inspected. It still does not prove technical truth.

## 14.10 Post-freeze Master Manual controls and outputs

Post-freeze controls include source maps, the mapping summary, unmapped register, Stage 10R extraction records, the Stage 10R-R coverage-repair audit, Stage 10S selection and repaired packets, validated Parts I–V, the validated Chapters 12–14 reconciliation and this Part VI draft.

Their role is to document how the Master Manual was constructed and controlled. They may explain:

- which sources were selected;
- which hashes were checked;
- why additional representative sources were needed;
- how contradictions were resolved;
- which files were excluded;
- how a chapter was drafted.

They may not be presented as pre-freeze project evidence. Stage 10S did not add its selected sources to the frozen 301-record source map. Validated Parts I–V and Part VI do not replace the original organized-workspace sources. A post-freeze reconciliation cannot retroactively change what the project knew or approved before the freeze.

The Stage 10R and Stage 10S sequence illustrates why process controls require interpretation. Stage 10R passed its extraction mechanics, but Chapters 12 and 13 had zero substantive Tier 1–4 mapped sources and Chapter 14 had only two. Stage 10S repaired representative coverage by selecting seventeen, seventeen and twenty-three sources without changing the frozen map. Zero extraction errors were therefore compatible with inadequate substantive coverage.

## 14.11 Change-control and revision requirements

Any revision after the freeze should record:

1. a unique stage or revision identifier;
2. date and responsible author or reviewer;
3. purpose and scope;
4. exact new, changed, superseded or removed paths;
5. before-and-after hashes where applicable;
6. reason for change;
7. approving authority;
8. effect on chapter mapping;
9. effect on contradictions and open decisions;
10. external-verification date where current facts are involved;
11. duplicate, archive and exclusion effects;
12. preservation location for the prior release.

Canonical files must not be silently overwritten. A correction should create an auditable revision. A source-map change should produce a new map version and preserve the old one. A revised technical source should state what it supersedes. A later external-verification pass should be dated because prices, specifications, standards and legal status can change.

Change control should also distinguish editorial corrections from substantive changes. Typographical corrections may not affect evidence. A change to architecture, approval state, sample count, patent status or source selection does.

## 14.12 Authority, contradiction and approval boundaries

Identity control answers “which record is this?” Authority control answers “what may this record decide?” Contradiction control answers “what happens when records disagree?”

After identity is established, the authority protocol applies:

1. current teacher requirements and explicit approvals;
2. Decision Register v1.2;
3. final Phase 3C architectures;
4. final memories and SOPs;
5. current comparative evidence;
6. valid syntheses and final adjudications;
7. controlled independent lanes;
8. earlier phase reports;
9. transport, manifests and archived material.

A lower source cannot silently override a higher one.

Material contradictions should record:

- the claim or design point;
- higher-authority source;
- conflicting source;
- resolution;
- residual uncertainty;
- required test or approval.

This system preserves disagreement rather than hiding it. It also prevents authenticity from being mistaken for approval. An authentic change request proves that a request existed, not that it was accepted. An authentic presentation proves what was submitted, not the teacher’s decision. A valid adjudication proves that a comparative review occurred, not that its recommendation became project authority.

The current state remains: VibeGuard is the strongest semester-build recommendation; the proposed OpenBraille-to-VibeGuard shift is not proved teacher-approved; OpenBraille, VibeGuard and TrueMoist remain controlled records; Chapter 11 remains a future execution framework; Phase 4 and procurement are not proved started; and no frozen MVP is established as patentable.

## 14.13 External-verification boundaries

No fresh web research was performed for Part VI. The following remain reserved for a later controlled verification stage:

- current Indian prices and availability;
- exact current manufacturer specifications;
- board and component authenticity;
- standards status;
- patent-family and legal status;
- official-register events;
- claim scope, infringement and FTO;
- current course-board rules;
- facility and equipment availability;
- physical experimental performance.

Historical prices or specifications may remain as dated planning evidence. They must not be presented as current procurement facts without later verification.

A later external-verification pass should record source, access date, product or patent identifier, jurisdiction or market, status, reviewer and effect on the manual. It should not silently edit old planning records.

## 14.14 Reproducibility and release requirements

A controlled Part VI release should include or reference:

- the source-freeze notice;
- Master Manual source policy;
- frozen 301-record source map;
- mapping summary and unmapped register;
- authority and contradiction protocol;
- original organized-workspace paths;
- source hashes;
- archive index and intentional-exclusion record;
- stage validation records;
- Stage 10S selection freeze and repaired packets;
- contradiction and open-decision registers;
- exact manual filename, version and release date;
- external-verification status;
- change log;
- reviewer sign-off.

Before release, the reviewer should confirm:

- no silent path substitution;
- no manifest or launcher cited as technical evidence;
- no TIER_5 source overriding Tier 1–2;
- no partial conclusion reconstructed;
- no failed or excluded output reintroduced;
- no duplicate counted as corroboration;
- current state matches validated Parts I–V;
- approval and patent-language boundaries are preserved;
- source notes use original organized-workspace paths;
- post-freeze controls are labeled as such;
- no archive was opened or expanded without authorization.

A reproducible release should allow another reviewer to trace a material sentence from the manual to the original source path and then understand that source’s authority, lifecycle and verification status.

## 14.15 Limitations of the integrity system

The integrity system has unavoidable limits.

- Hashes prove byte identity, not truth.
- Represented-source coverage does not prove semantic completeness.
- A source freeze establishes a time-bounded accounting state, not that no later evidence exists.
- Chapter mapping is a classification decision and may miss a cross-cutting role.
- Stage 10R showed that zero extraction errors do not prove adequate chapter coverage.
- Stage 10S repaired representative coverage, not the frozen source map.
- Post-freeze controls cannot become pre-freeze evidence.
- Text extraction can miss visual meaning.
- Cross-format duplicate detection is probabilistic unless binary hashes match.
- A repository can preserve an error perfectly.
- Model-assisted reconciliation remains dependent on human review.
- Current external facts can become stale.
- Reproducible process does not guarantee identical generative output.
- Integrity control does not replace legal, patent, safety, accessibility, metrology or engineering validation.

These limits do not make the system useless. They define the boundary within which its conclusions are reliable.

## 14.16 Chapter conclusion

Project mC has a documented, inspectable source-integrity system. It records a source-freeze boundary, represents or excludes discovered source content, uses hashes and stable paths, distinguishes canonical sources from duplicates, preserves archives and quarantine, maps sources to chapters and records post-freeze changes.

The system’s credibility depends on refusing to overclaim. A hash is not truth. A mapped source is not semantic completeness. A successful extraction is not adequate coverage. Stage 10S repaired Chapters 12–14 without changing the frozen map. Post-freeze controls explain manual construction but do not rewrite project history.

Reproducibility therefore means that another reviewer can inspect the same identities, authority rules, exclusions, mappings, contradictions and revision trail. Final technical, approval, procurement, patent and performance claims still require their own controlling evidence.

## 14.S Source notes

The following original organized-workspace paths were materially relied upon for Chapter 14.

### Source and repository controls

- `08_MASTER_MANUAL/01_Source_Index/SOURCE_FREEZE_NOTICE.md`
- `08_MASTER_MANUAL/01_Source_Index/MASTER_MANUAL_SOURCE_POLICY.md`
- `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Legacy_Audits_and_Snapshots/CLEANUP_VALIDATION_REPORT.md`
- `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Legacy_Repository_Audit/04_AUTHORITY_AMBIGUITIES.md`
- `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Legacy_Repository_Audit/03_DUPLICATE_REPORT.md`
- `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Naming_History/PHASE3C_NAMING_VALIDATION_REPORT.md`

### Organization-stage validation

- `00_START_HERE/01_STAGE1_GOVERNANCE_VALIDATION.md`
- `00_START_HERE/02_STAGE2_PHASE_HISTORY_VALIDATION.md`
- `00_START_HERE/03_STAGE3A_CONCEPT_ARCHITECTURE_VALIDATION.md`
- `00_START_HERE/04_STAGE3B_PATENT_EVIDENCE_VALIDATION.md`
- `00_START_HERE/05_STAGE4A_COMPARATIVE_DECISION_VALIDATION.md`
- `00_START_HERE/06_STAGE4B_TEACHER_AND_REVIEW_VALIDATION.md`
- `00_START_HERE/07_STAGE5_TRANSPORT_PROVENANCE_VALIDATION.md`
- `00_START_HERE/08_STAGE6A_HISTORICAL_RESEARCH_VALIDATION.md`
- `00_START_HERE/09_STAGE8_FINAL_ARCHIVAL_SWEEP_VALIDATION.md`
- `00_START_HERE/09_STAGE8_FINAL_ARCHIVAL_SWEEP_LOG.tsv`

### Post-freeze map and process controls

- `08_MASTER_MANUAL/02_Chapter_Source_Maps/MASTER_MANUAL_SOURCE_MAP.tsv`
- `08_MASTER_MANUAL/00_Blueprint/MASTER_MANUAL_MAPPING_SUMMARY.md`
- `08_MASTER_MANUAL/02_Chapter_Source_Maps/MASTER_MANUAL_UNMAPPED_FILES.tsv`
- `08_MASTER_MANUAL/02_Chapter_Source_Maps/14_Source_Integrity_Audit_and_Reproducibility_SOURCES.md`
- `08_MASTER_MANUAL/02_Chapter_Source_Maps/A1_Appendix_A_Complete_Source_Register_SOURCES.md`
- `00_START_HERE/29_STAGE10R_PROVENANCE_ARCHIVE_INTEGRITY_PACKETS_VALIDATION.md`
- `00_START_HERE/30_STAGE10R_R_PROVENANCE_ARCHIVE_INTEGRITY_COVERAGE_REPAIR_AUDIT.md`

# Part VI Provenance and AI-Use Register

| ID | Workflow element | Evidence role | Human control | Prohibited inference |
|---|---|---|---|---|
| PA-01 | Governing instruction | Defines task scope, authority order, exclusions, evidence cut-off and required output | Approve and version the instruction; audit the output against it | That a correct instruction proves downstream compliance |
| PA-02 | Independent research lane | Broadens search coverage and supplies competing analysis or source leads | Audit concept fidelity, sources, completeness and claim quality | That each lane is equally reliable or constitutes a vote |
| PA-03 | Lane compilation | Preserves sequential fragments or follow-up from one lane | Preserve sequence and one-lane identity | That fragments or follow-ups are independent reports |
| PA-04 | Input manifest | Proves expected attachment identity and package completeness | Verify names, paths, roles, sizes and hashes | Technical truth, novelty, approval or research completeness |
| PA-05 | Launcher | Preserves the initiating prompt or instruction | Record platform/date metadata where available | That the model followed the instruction or produced a valid answer |
| PA-06 | Reduced-file bundle | Transports original content under upload limits | Retain mapping to original separate sources | That the bundle is a new or canonical evidence source |
| PA-07 | Concept synthesis | Audits and integrates project authority and independent research | Verify architecture lock, primary support and legal distinctions | That synthesis overrides architecture or proves patentability |
| PA-08 | Final adjudication | Supplies cross-concept decision context, normalization and kill conditions | Decide whether recommendations enter governance | Teacher approval, filing authority or a vote |
| PA-09 | Provenance/exclusion register | Records selection, exclusion, hash, path and completeness status | Confirm classification and residual use | That selected content is correct merely because selected |
| PA-10 | Concept-swap exclusion | Prevents substituted architecture from contaminating current evidence | Identify the swap and whether any section is inseparable | That favorable passages from the failed report remain usable |
| PA-11 | Partial-source label | Preserves the true completeness state | Restrict use to complete, verified portions | A reconstructed or implied final verdict |
| PA-12 | Human architecture freeze | Controls current technical identity | Formal decision and change control | Model consensus as architecture authority |
| PA-13 | Physical validation | Produces empirical implementation evidence | Configuration, safety, measurement and sign-off | That a pre-build simulation or model report proves performance |
| PA-14 | IPR escalation | Opens institutional/legal review of protected subject matter | Preserve human contribution chronology and confidentiality | AI assistance as inventorship, ownership or legal advice |
| PA-15 | Final manual drafting | Converts controlled evidence into a readable record | Human authors accept responsibility for every statement | That polished prose or source count makes a claim true |

# Part VI Archive and Canonical-Replacement Register

| ID | Archived material | Archive class | Current canonical control | Permitted residual use |
|---|---|---|---|---|
| AR-01 | Decision Register v1.0 | Superseded governance | Decision Register v1.2 | Earlier project-state chronology |
| AR-02 | Decision Register v1.1 in earlier TrueMoist branch | Superseded governance | Decision Register v1.2 | Trace the superseded TrueMoist branch |
| AR-03 | TrueMoist historical PDR patch | Superseded architecture/patch | Final TrueMoist architecture, memory, SOP and v1.2 | Explain transition to the 72-run design |
| AR-04 | Earlier TrueMoist 135-run architecture and memory | Superseded architecture | Validated Part IV and final TrueMoist files | Historical design alternative and disagreement record |
| AR-05 | OpenBraille moving-roller synthesis | Failed concept swap | Valid OpenBraille syntheses and validated Part II | Negative provenance and fidelity-failure example |
| AR-06 | VibeGuard software-security synthesis | Failed concept swap | Valid VibeGuard syntheses and validated Part III | Negative provenance and name-drift example |
| AR-07 | VibeGuard Qwen2 variant | Duplicate/earlier variant | Controlled VibeGuard Qwen lane | Filename and version chronology |
| AR-08 | VibeGuard Mistral fragment | Partial fragment | Controlled Mistral partial compilation | Verified fragment-level leads only |
| AR-09 | TrueMoist Qwen #0 | Compilation component | Controlled TrueMoist Qwen compilation | Initial-lane chronology |
| AR-10 | TrueMoist supplementary Work Max audit | Excluded supplement | No replacement inside blind set; two valid syntheses remain controlled | Later separately authorized adversarial review |
| AR-11 | Convenience-folder copies | Duplicate/convenience variant | Canonical governance, phase or concept path | Availability and folder history |
| AR-12 | Historical presentation drafts | Historical draft | Official controlled submission identified in Part V | Presentation-development history |
| AR-13 | Byte-identical ZIP members | Legacy package duplicate | Normal canonical working-tree source | Package preservation |
| AR-14 | Unrelated quarantine | Intentional exclusion | None | Evidence that exclusion boundary was applied |
| AR-15 | Sensitive and temporary files | Security/hygiene exclusion | Controlled internal handling as applicable | Exclusion accounting only |

# Part VI Source-Integrity and Reproducibility Register

| ID | Integrity control | What it proves | What it does not prove | Release requirement |
|---|---|---|---|---|
| SI-01 | SHA-256 match | Exact byte identity | Truth, authority or cross-format equivalence | Record hash and compared paths |
| SI-02 | File size | Basic identity check | Semantic completeness | Use with hash, not alone |
| SI-03 | Stable original path | Location, branch and version context | Correctness | Preserve path history and rename log |
| SI-04 | Manifest match | Package identity and completeness | Technical validity | Label manifest as file control only |
| SI-05 | Source-freeze notice | Time-bounded accounting state | That no later evidence exists | State freeze timestamp and revision boundary |
| SI-06 | Canonical-path rule | Which source controls present citation | That the source is technically correct | Apply authority hierarchy |
| SI-07 | Duplicate audit | Exact and candidate duplicate relationships | Authority or safe deletion by itself | Preserve manual review for cross-format cases |
| SI-08 | Intentional-exclusion record | Deliberate boundary and reason | Technical review of excluded material | Preserve exclusion without exposing sensitive content |
| SI-09 | Frozen source map | Chapter assignment and treatment under the frozen rule | Exhaustive semantic coverage | Preserve map version and unmapped register |
| SI-10 | Unmapped register | Which organized file lacked a chapter rule | Absence from the repository | Resolve only through controlled revision |
| SI-11 | Stage copy/archival validation | Recorded copy, deduplication, archive and exclusion actions | Engineering, patent or approval conclusions | Retain logs and hashes |
| SI-12 | Stage 10S repaired extraction | Selected source text was extracted successfully | Exhaustive chapter evidence | Preserve selection freeze and coverage limitation |
| SI-13 | Visual review | Relevant visual content was inspected | Technical truth | Require when layout, diagram or image meaning is material |
| SI-14 | Authority protocol | How conflicts are resolved | Physical validation | Carry contradictions and residual uncertainty |
| SI-15 | Change log | What changed between releases | Approval unless the approver is recorded | Preserve prior release and before/after identities |
| SI-16 | External-verification pass | Current facts checked to its stated scope and date | Permanent validity | Record source, date, identifier and reviewer |
| SI-17 | Human sign-off | Named reviewer accepted release responsibility | That every underlying claim is correct without audit | Complete release checklist and unresolved-item review |

# Part VI Open-Decision Register

| ID | Open item | Current state | Required evidence or authority |
|---|---|---|---|
| OD-01 | Teacher decision on proposed OpenBraille-to-VibeGuard shift | Proposed; not proved approved | Explicit teacher or course-authority record |
| OD-02 | Final authorized semester concept and MCU/platform | Unresolved | Controlling approval naming concept, platform and scope |
| OD-03 | Project-wide Phase 4 and procurement start | Not proved started | Approved phase gate, procurement record and configuration baseline |
| OD-04 | Chapter 11 execution evidence | Zero directly mapped execution sources | Build logs, approved BOM, firmware versions, test records and sign-offs |
| OD-05 | Physical validation of frozen MVPs | Not established by Part VI | Configuration-controlled experiments and measured results |
| OD-06 | Patentability, filing, infringement and FTO | No authorized conclusion | Current official-source search, claim analysis, experiments and institutional/counsel review |
| OD-07 | Human inventorship and contribution | Not determined | Dated contribution chronology, invention records and institutional IPR process |
| OD-08 | Mapping of `03_CONCEPT_PORTFOLIO/CONCEPT_PORTFOLIO_INDEX.md` | One organized file remains unmapped | Controlled map revision or appendix assignment |
| OD-09 | Current prices, specifications and supplier authenticity | Not verified in this stage | Dated manufacturer and Indian-market verification |
| OD-10 | Cross-format duplicate candidates | Some require case-specific review | Manual content and visual equivalence review before collapse or deletion |
| OD-11 | Later use of supplementary TrueMoist audit | Excluded from blind set | Explicit adversarial-review authorization with separate disclosure |
| OD-12 | Final controlled release of Part VI | Draft produced; reviewer sign-off not recorded here | Release checklist, contradiction review, version/date and approving reviewer |

# Part VI Contradiction Summary

| ID | Chapter | Issue | Controlling resolution | Residual uncertainty |
|---|---:|---|---|---|
| CT-01 | 12 | Repeated model findings may appear to be votes | Recurrence is a search signal; authority and claim-level evidence decide | Draft wording must continue to avoid majority implications |
| CT-02 | 12 | Manifest presence may appear to validate content | Manifest proves package identity only | None if role labels remain visible |
| CT-03 | 12 | Launcher may appear to prove compliance | Launcher proves initiating prompt transport only | Platform execution metadata may be incomplete |
| CT-04 | 12–13 | OpenBraille mode filenames cross valid and failed outputs | Resolve by content, path, hash, architecture fidelity and controlled destination | Cause of crossing is historical and non-material |
| CT-05 | 12–13 | VibeGuard Mistral fragments may appear to form a complete report | One partial lane; no final verdict reconstruction | Intended final conclusion remains unavailable |
| CT-06 | 12–13 | TrueMoist Qwen components may appear to be two lanes | One compilation and one lane | Section-level reliability still requires audit |
| CT-07 | 13 | TrueMoist 135-run branch conflicts with final design | Validated 72-run architecture and v1.2 control | Physical completion of 72 runs remains unproved |
| CT-08 | 13 | Supplementary TrueMoist audit is complete but excluded | Keep outside blind set; disclose any later authorized use | Later adversarial value is unassessed |
| CT-09 | 13–14 | Duplicate files multiply physical paths | Count one logical source and cite canonical path | Some cross-format cases need manual review |
| CT-10 | 14 | Stage 10R passed mechanically despite weak substantive coverage | Stage 10S repaired packets control the substantive Part VI basis | Representative coverage is not exhaustive semantics |
| CT-11 | 14 | 301 mapped records coexist with one unmapped organized file | Source accounting and chapter mapping are separate | Future mapping treatment remains open |
| CT-12 | 14 | Hash and integrity success may appear to prove approval or patentability | Apply authority and external-verification controls after identity | Approval, testing and legal conclusions remain open |
| CT-13 | 12–14 | Two adjudications disagree on preferred later patent route | Preserve disagreement and resolve through evidence, experiments and authority—not vote count | Preferred future route remains unresolved |
| CT-14 | 12–14 | Historical status files may imply Phase 4 or procurement began | Validated Parts I and V control: start is not proved | Actual authorization remains open |

# Part VI Source Ledger

The following original organized-workspace paths were materially relied upon. They are grouped by chapter and evidence role. The Part VI attachment manifest is omitted because it is file control only.

## Chapter 12 — Workflow and AI-use control

**TIER_1 source policy**

- `08_MASTER_MANUAL/01_Source_Index/MASTER_MANUAL_SOURCE_POLICY.md`

**TIER_2 concept and comparative evidence control**

- `03_CONCEPT_PORTFOLIO/OpenBraille/PATENT_EVIDENCE_INDEX.md`
- `03_CONCEPT_PORTFOLIO/VibeGuard/PATENT_EVIDENCE_INDEX.md`
- `03_CONCEPT_PORTFOLIO/TrueMoist/PATENT_EVIDENCE_INDEX.md`
- `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/02_Authoritative_Source_Manifest.md`

**TIER_5 provenance and transport controls**

- `06_TRANSPORT_AND_PROVENANCE/TRANSPORT_AND_PROVENANCE_INDEX.md`
- `06_TRANSPORT_AND_PROVENANCE/01_Governing_Instructions/Project_mC_Final_Adjudication_Instructions_CANONICAL.md`
- `06_TRANSPORT_AND_PROVENANCE/02_Input_Manifests/Final_Adjudication_EXCLUSION_AND_PROVENANCE_REGISTER.md`
- `06_TRANSPORT_AND_PROVENANCE/01_Governing_Instructions/OpenBraille_Synthesis_Instructions_CANONICAL.md`
- `06_TRANSPORT_AND_PROVENANCE/01_Governing_Instructions/VibeGuard_Synthesis_Instructions_CANONICAL.md`
- `06_TRANSPORT_AND_PROVENANCE/01_Governing_Instructions/TrueMoist_Synthesis_Instructions_CANONICAL.md`
- `06_TRANSPORT_AND_PROVENANCE/02_Input_Manifests/OpenBraille_Synthesis_INPUT_MANIFEST.md`
- `06_TRANSPORT_AND_PROVENANCE/02_Input_Manifests/VibeGuard_Synthesis_INPUT_MANIFEST.md`
- `06_TRANSPORT_AND_PROVENANCE/02_Input_Manifests/TrueMoist_Synthesis_INPUT_MANIFEST.md`
- `06_TRANSPORT_AND_PROVENANCE/03_Launchers_and_Checklists/VibeGuard_Synthesis_Launcher_FINAL.txt`
- `00_START_HERE/07_STAGE5_TRANSPORT_PROVENANCE_VALIDATION.md`
- `08_MASTER_MANUAL/02_Chapter_Source_Maps/12_Research_Provenance_and_AI_Workflow_Control_SOURCES.md` — post-freeze mapping control only

## Chapter 13 — Archive and canonical replacement

**Archive, failure and exclusion controls**

- `09_ARCHIVE/ARCHIVE_INDEX.md`
- `09_ARCHIVE/03_Failed_or_Partial_Research/README.md`
- `09_ARCHIVE/03_Failed_or_Partial_Research/OpenBraille/FAILED_CONCEPT_SWAP_OpenBraille_Deep_Research_Synthesis.md`
- `09_ARCHIVE/03_Failed_or_Partial_Research/VibeGuard/FAILED_CONCEPT_SWAP_VibeGuard_Deep_Research_Synthesis.md`
- `09_ARCHIVE/03_Failed_or_Partial_Research/TrueMoist/SUPPLEMENTARY_EXCLUDED_TrueMoist_Work_Max_Web_Audit.md`
- `09_ARCHIVE/05_Unrelated_Quarantine/INTENTIONAL_EXCLUSIONS.md`

**Superseded governance and architecture**

- `09_ARCHIVE/01_Superseded/Convenience_Folder_Variants/COPY PASTE FOLDER/Project_mC_Decision_Register_v1.0.md`
- `09_ARCHIVE/01_Superseded/TrueMoist/Earlier_Claude_Architecture/Project_mC_Decision_Register_v1_1.md`
- `09_ARCHIVE/01_Superseded/TrueMoist/Phase3C_TrueMoist_PDR_Patch_Historical.md`
- `09_ARCHIVE/01_Superseded/TrueMoist/Earlier_Claude_Architecture/Phase3C_TrueMoist_Architecture_Report_by_Claude.md`
- `09_ARCHIVE/01_Superseded/TrueMoist/Earlier_Claude_Architecture/Phase3C_TrueMoist_MEMORY.md`

**Partial and duplicate variants**

- `09_ARCHIVE/03_Failed_or_Partial_Research/VibeGuard/Legacy_Fragments_and_Variants/research_on_f.patent_by_qwen2.md`
- `09_ARCHIVE/03_Failed_or_Partial_Research/VibeGuard/Legacy_Fragments_and_Variants/research on f.patent by mistral 2.md`
- `09_ARCHIVE/03_Failed_or_Partial_Research/TrueMoist/Legacy_Fragments_and_Variants/research on f.patent by qwen #0.md`
- `00_START_HERE/09_STAGE8_FINAL_ARCHIVAL_SWEEP_VALIDATION.md`
- `00_START_HERE/09_STAGE8_FINAL_ARCHIVAL_SWEEP_LOG.tsv`
- `08_MASTER_MANUAL/02_Chapter_Source_Maps/13_Superseded_Failed_Partial_and_Archived_Routes_SOURCES.md` — post-freeze mapping control only

## Chapter 14 — Source integrity and reproducibility

**TIER_1 source and repository controls**

- `08_MASTER_MANUAL/01_Source_Index/SOURCE_FREEZE_NOTICE.md`
- `08_MASTER_MANUAL/01_Source_Index/MASTER_MANUAL_SOURCE_POLICY.md`
- `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Legacy_Audits_and_Snapshots/CLEANUP_VALIDATION_REPORT.md`
- `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Legacy_Repository_Audit/04_AUTHORITY_AMBIGUITIES.md`
- `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Legacy_Repository_Audit/03_DUPLICATE_REPORT.md`
- `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Naming_History/PHASE3C_NAMING_VALIDATION_REPORT.md`

**Organization-stage audit controls**

- `00_START_HERE/01_STAGE1_GOVERNANCE_VALIDATION.md`
- `00_START_HERE/02_STAGE2_PHASE_HISTORY_VALIDATION.md`
- `00_START_HERE/03_STAGE3A_CONCEPT_ARCHITECTURE_VALIDATION.md`
- `00_START_HERE/04_STAGE3B_PATENT_EVIDENCE_VALIDATION.md`
- `00_START_HERE/05_STAGE4A_COMPARATIVE_DECISION_VALIDATION.md`
- `00_START_HERE/06_STAGE4B_TEACHER_AND_REVIEW_VALIDATION.md`
- `00_START_HERE/07_STAGE5_TRANSPORT_PROVENANCE_VALIDATION.md`
- `00_START_HERE/08_STAGE6A_HISTORICAL_RESEARCH_VALIDATION.md`
- `00_START_HERE/09_STAGE8_FINAL_ARCHIVAL_SWEEP_VALIDATION.md`
- `00_START_HERE/09_STAGE8_FINAL_ARCHIVAL_SWEEP_LOG.tsv`

**Post-freeze map and process controls**

- `08_MASTER_MANUAL/02_Chapter_Source_Maps/MASTER_MANUAL_SOURCE_MAP.tsv`
- `08_MASTER_MANUAL/00_Blueprint/MASTER_MANUAL_MAPPING_SUMMARY.md`
- `08_MASTER_MANUAL/02_Chapter_Source_Maps/MASTER_MANUAL_UNMAPPED_FILES.tsv`
- `08_MASTER_MANUAL/02_Chapter_Source_Maps/14_Source_Integrity_Audit_and_Reproducibility_SOURCES.md`
- `08_MASTER_MANUAL/02_Chapter_Source_Maps/A1_Appendix_A_Complete_Source_Register_SOURCES.md`
- `00_START_HERE/29_STAGE10R_PROVENANCE_ARCHIVE_INTEGRITY_PACKETS_VALIDATION.md`
- `00_START_HERE/30_STAGE10R_R_PROVENANCE_ARCHIVE_INTEGRITY_COVERAGE_REPAIR_AUDIT.md`

## Cross-chapter current-state controls

- `01_GOVERNANCE_AND_CONTROL/01_Project_Requirements/Teacher_Project_Requirements_and_Change_Context.md`
- `01_GOVERNANCE_AND_CONTROL/02_Decision_Registers/Project_mC_Decision_Register_v1.2.md`
- `03_CONCEPT_PORTFOLIO/OpenBraille/01_Final_Architecture/Phase3C_OpenBraille_Architecture_Report_Final.md`
- `03_CONCEPT_PORTFOLIO/OpenBraille/01_Final_Architecture/Phase3C_OpenBraille_Memory_Final.md`
- `03_CONCEPT_PORTFOLIO/OpenBraille/01_Final_Architecture/Phase3C_OpenBraille_SOP_Final.md`
- `03_CONCEPT_PORTFOLIO/VibeGuard/01_Final_Architecture/Phase3C_VibeGuard_Architecture_Report_Final.md`
- `03_CONCEPT_PORTFOLIO/VibeGuard/01_Final_Architecture/Phase3C_VibeGuard_Memory_Final.md`
- `03_CONCEPT_PORTFOLIO/VibeGuard/01_Final_Architecture/Phase3C_VibeGuard_SOP_Final.md`
- `03_CONCEPT_PORTFOLIO/TrueMoist/01_Final_Architecture/Phase3C_TrueMoist_Architecture_Report_Final.md`
- `03_CONCEPT_PORTFOLIO/TrueMoist/01_Final_Architecture/Phase3C_TrueMoist_Memory_Final.md`
- `03_CONCEPT_PORTFOLIO/TrueMoist/01_Final_Architecture/Phase3C_TrueMoist_SOP_Final.md`
- `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/00_Engineering_Design_Review.md`
- `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/05_Uncertainty_and_Test_Register.md`
- `04_COMPARATIVE_DECISION/02_Final_Adjudications/01_Project_mC_Final_Adjudication_Work_Max.md`
- `04_COMPARATIVE_DECISION/02_Final_Adjudications/02_Project_mC_Final_Adjudication_Deep_Research_High.md`
- `04_COMPARATIVE_DECISION/03_Change_Request/Project_mC_Request_to_Change_from_OpenBraille_to_VibeGuard.docx`

---

**End of Project mC Master Manual — Part VI.**

<!-- END CONTROLLED COMPONENT: PART_VI -->

---

<!-- BEGIN CONTROLLED COMPONENT: APPENDICES_A1_TO_A4_RELEASE_CANDIDATE -->
<!-- SOURCE PATH: /home/paradoxpete/Documents/PROJECT_ORGANIZED/08_MASTER_MANUAL/10_Final_Assembly_Workspace/01_Corrected_Release_Candidate/Project_mC_Master_Manual_Appendices_A1_to_A4_RELEASE_CANDIDATE.md -->
<!-- SOURCE SHA-256: ce0aa5308d19112ea8f05739f2426ff1f24de363199c3cb5b0f7dac32f5e947b -->

## Appendices A1–A4

## Appendix control

| Field | Value |
|---|---|
| Status | Corrected controlled release-candidate appendices |
| A1 | Mechanically generated complete source register |
| A2 | Mechanically generated peer/reference register |
| A3 | Corrected controlled glossary and acronyms |
| A4 | Corrected controlled open decisions and change log |
| Technical effect | Does not amend validated Parts I–VI |
| Approval effect | Does not approve concept, platform, Phase 4 or procurement |
| Patent effect | No patentability, filing, infringement or FTO conclusion |


---

<!-- BEGIN CONTROLLED COMPONENT: APPENDIX_A1 -->
<!-- SOURCE PATH: /home/paradoxpete/Documents/PROJECT_ORGANIZED/08_MASTER_MANUAL/09_Appendices_Workspace/Appendix_A1_Complete_Source_Register.md -->
<!-- SOURCE SHA-256: 150c4ee42ed83cd7cef4df08e31150272d14551b39d73dae20a7a73b7ece1294 -->

# Appendix A1 — Complete Source Register

## A1.1 Control statement

This appendix is generated mechanically from the frozen `MASTER_MANUAL_SOURCE_MAP.tsv` and the separately controlled unmapped-file register. It is a source-identity and mapping register, not technical evidence and not a statement that every source is correct or semantically complete.

- Frozen source-map records: **301**
- Unmapped-register rows: **1**
- Source-map SHA-256: `ac4105f2e19f256a48a45dd74e684e68c226ab11756a44c1b2d0254d4764b3d7`
- Unmapped-register SHA-256: `41d72d09d0772dd5b367d5177392226c42ab8e20a639fede468e90dbf30f8e6e`

## A1.2 Source-map summary

### Records by destination

| Destination | Records |
|---|---:|
| `UNSPECIFIED` | 1 |
| `00` | 1 |
| `01` | 26 |
| `02` | 52 |
| `03` | 21 |
| `04` | 5 |
| `05` | 12 |
| `06` | 7 |
| `07` | 9 |
| `08` | 14 |
| `09` | 18 |
| `10` | 15 |
| `12` | 50 |
| `13` | 32 |
| `14` | 20 |
| `A2` | 18 |

### Records by authority tier

| Authority tier | Records |
|---|---:|
| `REFERENCE_ONLY` | 18 |
| `TIER_1` | 38 |
| `TIER_2` | 53 |
| `TIER_3` | 18 |
| `TIER_4` | 73 |
| `TIER_5` | 100 |
| `UNSPECIFIED` | 1 |

### Records by manual treatment

| Manual treatment | Records |
|---|---:|
| `ARCHIVE_ONLY` | 32 |
| `AUDIT_APPENDIX` | 18 |
| `CONDITIONAL_EVIDENCE` | 2 |
| `CORE_DECISION_EVIDENCE` | 24 |
| `CORE_NARRATIVE` | 36 |
| `CORE_OR_HISTORICAL` | 15 |
| `CORE_OR_SUPPORTING` | 5 |
| `CORE_SOURCE_CONTROL` | 2 |
| `HISTORICAL_NARRATIVE` | 37 |
| `HISTORICAL_SUPPORT` | 36 |
| `PROVENANCE_ONLY` | 50 |
| `REFERENCE_ONLY` | 18 |
| `SUPPORTING_EVIDENCE` | 25 |
| `UNSPECIFIED` | 1 |

## A1.3 Frozen 301-record source map

| No. | Original organized-workspace path | Destination | Authority tier | Manual treatment | Size bytes | SHA-256 |
|---:|---|---|---|---|---:|---|
| 1 | `00_START_HERE/README.md` | `00` | `TIER_1` | CORE_NARRATIVE | 1140 | `6611c2adecbaf2ca2c99b2ed1d532edec41312a51cad5f8fd10dff1a5a3fa817` |
| 2 | `01_GOVERNANCE_AND_CONTROL/01_Project_Requirements/Teacher_Project_Requirements_and_Change_Context.md` | `01` | `TIER_1` | CORE_NARRATIVE | 2905 | `0711a1a7fca621fa36595eff60a0f61b6a0f3edda0f597aa340f5d316b61fb05` |
| 3 | `01_GOVERNANCE_AND_CONTROL/02_Decision_Registers/HISTORICAL_Project_mC_Decision_Register_v1.0.md` | `01` | `TIER_1` | CORE_NARRATIVE | 42726 | `875acb70b77be4f303107ce37dbc8f5cfb7d4f278089cdf4317f52d1c8ee668d` |
| 4 | `01_GOVERNANCE_AND_CONTROL/02_Decision_Registers/Project_mC_Decision_Register_v1.2.md` | `01` | `TIER_1` | CORE_NARRATIVE | 56071 | `9678c5072d86ef38e48372f940ec91396b7ac7bcbeed0124ac8e2485307f408c` |
| 5 | `01_GOVERNANCE_AND_CONTROL/03_Project_Context_and_Phase_Map/MC_Project_PHASE_DOC.md` | `01` | `TIER_1` | CORE_NARRATIVE | 12219 | `8db62e0893293f93f89c00ab09640b6eb750118e140a820813f9c8aef5d00dde` |
| 6 | `01_GOVERNANCE_AND_CONTROL/03_Project_Context_and_Phase_Map/PROJECT_CONCEPT_CONTEXT.md` | `01` | `TIER_1` | CORE_NARRATIVE | 6646 | `f520cb5201e299fb0f9185bd2b79318229b898e5a8ad7822deb9a073e8f6cae4` |
| 7 | `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/AGENTS.md` | `01` | `TIER_1` | CORE_NARRATIVE | 3305 | `f04384c78d2b342eaccf951dc126ad8df809210b233e199ce06ec169736a5594` |
| 8 | `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Legacy_Audits_and_Snapshots/CLEANUP_DIFF_NAME_STATUS.txt` | `01` | `TIER_1` | CORE_NARRATIVE | 171 | `109a32a0c4f7f991c157fb4743601f6033bea3db415edf5a04b24f5cc64f7f53` |
| 9 | `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Legacy_Audits_and_Snapshots/CLEANUP_VALIDATION_REPORT.md` | `01` | `TIER_1` | CORE_NARRATIVE | 6760 | `975767d50bf28bb29c0ed7b12b3c4949551f7fefc63f4aef9004335a7a18efe5` |
| 10 | `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Legacy_Audits_and_Snapshots/CONTEXT_AND_ZIP_PACKAGES.md` | `01` | `TIER_1` | CORE_NARRATIVE | 944 | `98a9febc897d759037e545cba8424e0bec33243804d0bcda5285b7bd5cfbe16d` |
| 11 | `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Legacy_Audits_and_Snapshots/CURRENT_FOLDER_STRUCTURE.txt` | `01` | `TIER_1` | CORE_NARRATIVE | 8744 | `ba3153f5011ecff39f4eadce191d7941cc29801a3b6eb4761a4e87e9a65fc8b1` |
| 12 | `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Legacy_REORGANIZATION_LOG.md` | `01` | `TIER_1` | CORE_NARRATIVE | 2012 | `fd53bcb50747e4703f60d64c0e3123cd7d1c467c36e1c2917e9da1d1f4198799` |
| 13 | `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Legacy_Repository_Audit/01_CURRENT_STRUCTURE_ANALYSIS.md` | `01` | `TIER_1` | CORE_NARRATIVE | 4421 | `364f2fb74e1ed35bc1024c0185d504618a32e858c621e0937add45d80f03d27b` |
| 14 | `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Legacy_Repository_Audit/02_FILE_MANIFEST.csv` | `01` | `TIER_1` | CORE_NARRATIVE | 45275 | `959fd614ded4de4b178ddf31b03191d1192e34d32ba5575cb678e055df926521` |
| 15 | `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Legacy_Repository_Audit/02_FILE_MANIFEST.pdf` | `01` | `TIER_1` | CORE_NARRATIVE | 502440 | `904d6fb0000cede691fe9b28a897db5e44413e95a2ff5ce6ffcc62bee88fd1af` |
| 16 | `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Legacy_Repository_Audit/03_DUPLICATE_REPORT.md` | `01` | `TIER_1` | CORE_NARRATIVE | 14258 | `e73b55d4f36f630dfc45d61147e0d683a364af1f0e28a95f54c5da972cc24925` |
| 17 | `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Legacy_Repository_Audit/04_AUTHORITY_AMBIGUITIES.md` | `01` | `TIER_1` | CORE_NARRATIVE | 3676 | `2af657ba4e6666650bc2c4c44a13c6ba5b87feb292efa1d4a7349c06835b4fc3` |
| 18 | `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Legacy_Repository_Audit/05_NAMING_AND_PLACEMENT_ISSUES.md` | `01` | `TIER_1` | CORE_NARRATIVE | 3806 | `3cb55e747e4d7b47b7af61a78c627db0ee3cd274618ee32af01ba4e37303176e` |
| 19 | `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Legacy_Repository_Audit/06_SECURITY_AND_UNKNOWN_FILES.md` | `01` | `TIER_1` | CORE_NARRATIVE | 3163 | `e341c54c577ba5bc7f04b97d7c3d11d59dace003914cbd9df3f8995d15977afe` |
| 20 | `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Legacy_Repository_Audit/07_MINIMAL_CLEANUP_PROPOSAL.md` | `01` | `TIER_1` | CORE_NARRATIVE | 5724 | `a4ced05912df7c4a17f117039e8ae12b73601bf12bda2a2a28b0640f5beaafab` |
| 21 | `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Naming_History/PHASE3C_NAMING_CHANGE_LOG.md` | `01` | `TIER_1` | CORE_NARRATIVE | 18986 | `adda533db7e29f86a39f97c517ad9afd47337b6b5edda11571d57f0895923b23` |
| 22 | `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Naming_History/PHASE3C_NAMING_PROPOSAL.md` | `01` | `TIER_1` | CORE_NARRATIVE | 17635 | `9a0a1bfc7a1c3867fa6eea536e7ec288bbec4a0e1289333976d6f025b24fe811` |
| 23 | `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Naming_History/PHASE3C_NAMING_VALIDATION_REPORT.md` | `01` | `TIER_1` | CORE_NARRATIVE | 21443 | `02e3c811b70d3fb0b4f92e784b499093de190dd4c0992987f7da8739bc307353` |
| 24 | `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Original_Project_gitignore.txt` | `01` | `TIER_1` | CORE_NARRATIVE | 8 | `2b6e0de1dd86ba1295c97310b94d4219fff9918576dfd1d750657b696d85afe8` |
| 25 | `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Original_Repository_README.md` | `01` | `TIER_1` | CORE_NARRATIVE | 2945 | `3ee6a965e08443bd8af139f01dbe92794e35af5f7888fd85ba1d6bcea27e7a4f` |
| 26 | `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/PHASE3C_NAMING_FINALIZATION_LOG.md` | `01` | `TIER_1` | CORE_NARRATIVE | 3558 | `beee446e6c6e73fa932c50e08812c4c51ca670a367cb02badc40860667a49a0c` |
| 27 | `01_GOVERNANCE_AND_CONTROL/AUTHORITY_MAP.md` | `01` | `TIER_1` | CORE_NARRATIVE | 862 | `cda01b77e280ffd911540c5a78ad5dda294f12f1f3054888a14950f5fb1b4f5a` |
| 28 | `02_PHASE_HISTORY/HISTORICAL_RESEARCH_INDEX.md` | `02` | `TIER_4` | HISTORICAL_NARRATIVE | 870 | `b9c9e1b25cbbbe9972169c884af02e5385d54a7d74f4d87f0e6c9ce73b2e410e` |
| 29 | `02_PHASE_HISTORY/PHASE_HISTORY_INDEX.md` | `02` | `TIER_4` | HISTORICAL_NARRATIVE | 650 | `cdd41810faba5c55718bbe34e1b67b825dfe03a250066cbe5c5e9a2ea9c3638d` |
| 30 | `02_PHASE_HISTORY/Phase_1/Phase_1A_Opportunity_Discovery/Phase1A_Memory.md` | `02` | `TIER_4` | HISTORICAL_NARRATIVE | 4029 | `5a8943e1e556e1db0644cc7b75e2b4c8000b1a9506d673406c9c70cf7bb4a213` |
| 31 | `02_PHASE_HISTORY/Phase_1/Phase_1A_Opportunity_Discovery/Phase1A_Summary.md` | `02` | `TIER_4` | HISTORICAL_NARRATIVE | 2794 | `c52bed09fdfd1a860471bfc6d56cd41411f730362d12ee0348e07ad0939909c9` |
| 32 | `02_PHASE_HISTORY/Phase_1/Phase_1A_Opportunity_Discovery/Raw_Research/01_ChatGPT_Deep_Research.md` | `02` | `TIER_4` | HISTORICAL_SUPPORT | 20670 | `fa41ec5c0504aada478a754133290458a1333eee99542c4530d3fb2abc8f5ac0` |
| 33 | `02_PHASE_HISTORY/Phase_1/Phase_1A_Opportunity_Discovery/Raw_Research/02_Gemini_Deep_Research.docx` | `02` | `TIER_4` | HISTORICAL_SUPPORT | 3035520 | `e527fa3ab029f3dd3096184c35f90ccd21e61bd520d9eb677f1031abbebd13ad` |
| 34 | `02_PHASE_HISTORY/Phase_1/Phase_1A_Opportunity_Discovery/Raw_Research/03_Kimi_Deep_Research.docx` | `02` | `TIER_4` | HISTORICAL_SUPPORT | 64142 | `c0d4cbeb9099d8a58c4fa6eab7e2f06aa1a0bda76affecb9444f040e8169828f` |
| 35 | `02_PHASE_HISTORY/Phase_1/Phase_1A_Opportunity_Discovery/Raw_Research/04_Qwen_AI_Deep_Research.pdf` | `02` | `TIER_4` | HISTORICAL_SUPPORT | 519844 | `5b3f7270de5bc6a27eba0e458cd2f7f40f55dd0407094f70ccfed6f6fd3f7ed8` |
| 36 | `02_PHASE_HISTORY/Phase_1/Phase_1B5_Portfolio_Optimization/Phase1B5_Memory.md` | `02` | `TIER_4` | HISTORICAL_NARRATIVE | 5302 | `d200473fd85a3cc910e3532bb2be662e0fcbdeab363fe988a948fd81d129c537` |
| 37 | `02_PHASE_HISTORY/Phase_1/Phase_1B5_Portfolio_Optimization/Phase1B5_Opportunity_Portfolio_Optimization.md` | `02` | `TIER_4` | HISTORICAL_NARRATIVE | 6431 | `305f0f568081ad8a01affc02d252a681f84abde5c23c2a9421fb69369ecc5540` |
| 38 | `02_PHASE_HISTORY/Phase_1/Phase_1B5_Portfolio_Optimization/Phase1B5_Portfolio_Optimization_By_Claude.pdf` | `02` | `TIER_4` | HISTORICAL_NARRATIVE | 582050 | `25130fe434ba2962de3ca241374d9823acced92b088ec6562a77140b80551809` |
| 39 | `02_PHASE_HISTORY/Phase_1/Phase_1B_Opportunity_Analysis/Phase1B_Memory.md` | `02` | `TIER_4` | HISTORICAL_NARRATIVE | 3966 | `d58c91eead60c5abdb4e38c1e9b87c7449f4b3b68ccd7a23f5d4816fea16ff76` |
| 40 | `02_PHASE_HISTORY/Phase_1/Phase_1B_Opportunity_Analysis/Phase1B_Opportunity_Analysis.md` | `02` | `TIER_4` | HISTORICAL_NARRATIVE | 5802 | `e10d76b80c78554ff7e2ea75f3b263bfe82333c54418e7f794d249610f8fe130` |
| 41 | `02_PHASE_HISTORY/Phase_1/Phase_1B_Opportunity_Analysis/Phase1B_Opportunity_Analysis_By_Claude.pdf` | `02` | `TIER_4` | HISTORICAL_NARRATIVE | 1484584 | `8e53b914163d8e2685d9edda7422e4c1ac1a01230e60e3a100a0e7ef514dd52c` |
| 42 | `02_PHASE_HISTORY/Phase_1/Phase_1C_Concept_Synthesis/Abstracts_and_Proposal_Derivatives/01_Microcontroller_Project_Abstract_Proposal_5_Ideas.pdf` | `02` | `TIER_4` | HISTORICAL_NARRATIVE | 27986 | `0d0c8ba61f0c5b2ea5ac243a382f1a1ffdb1e75ed27d8f2b1f6fc8b971afd82e` |
| 43 | `02_PHASE_HISTORY/Phase_1/Phase_1C_Concept_Synthesis/Abstracts_and_Proposal_Derivatives/02_Microcontroller_Project_Idea_Abstracts_2.0.pdf` | `02` | `TIER_4` | HISTORICAL_NARRATIVE | 25856 | `9d3f9364213e055715d85c85cf09c1609190c2c32918b60fcfe54f336f4fb8ec` |
| 44 | `02_PHASE_HISTORY/Phase_1/Phase_1C_Concept_Synthesis/Abstracts_and_Proposal_Derivatives/03_Microcontroller_Project_Idea_Abstracts_Initial.pdf` | `02` | `TIER_4` | HISTORICAL_NARRATIVE | 24352 | `8145ccd58cad7eadb15d9f0eb51c3e833cfbe2afe7eff9a174666118752f0874` |
| 45 | `02_PHASE_HISTORY/Phase_1/Phase_1C_Concept_Synthesis/Abstracts_and_Proposal_Derivatives/04_Minimalist_Project_Proposal.pdf` | `02` | `TIER_4` | HISTORICAL_NARRATIVE | 82574 | `19d4198bb4fafc2fbd299a68517551c58e52d319a6c84c4df55c6a41246f44e0` |
| 46 | `02_PHASE_HISTORY/Phase_1/Phase_1C_Concept_Synthesis/Abstracts_and_Proposal_Derivatives/05_Project_Proposal_Booklet.pdf` | `02` | `TIER_4` | HISTORICAL_NARRATIVE | 666060 | `c15f75f4ce0ab6cf6bca5ad7bb1b3c12a4c1e4bfdf662886fd168ba78d67c203` |
| 47 | `02_PHASE_HISTORY/Phase_1/Phase_1C_Concept_Synthesis/Phase1C.md` | `02` | `TIER_4` | HISTORICAL_NARRATIVE | 3009 | `8e41493ddbc8b8b3c3ad8a00995b6ae3f8a5645351f8086a6b8ded92623853e4` |
| 48 | `02_PHASE_HISTORY/Phase_1/Phase_1C_Concept_Synthesis/Phase1C_Concept_Synthesis.pdf` | `02` | `TIER_4` | HISTORICAL_NARRATIVE | 641952 | `4f117f1a7bc0fb5b4ec9e450036566aa5198a08e84a451ad2e7d2dbc8636b084` |
| 49 | `02_PHASE_HISTORY/Phase_1/Phase_1C_Concept_Synthesis/Phase1C_Memory.md` | `02` | `TIER_4` | HISTORICAL_NARRATIVE | 3390 | `e3b320245bc20d4312edc22b62fc9584059111e8fd38442277a3e5544ae019c1` |
| 50 | `02_PHASE_HISTORY/Phase_1/Phase_1C_Concept_Synthesis/Visual_Explanations/01_Visual_Explanation_11_Ideas.html` | `02` | `TIER_4` | HISTORICAL_NARRATIVE | 68141 | `bd36812bff46105a8f6f9b6a38bbc93688b8e3cd2e9146456481b71c880f766d` |
| 51 | `02_PHASE_HISTORY/Phase_1/Phase_1C_Concept_Synthesis/Visual_Explanations/02_Visual_Explanation_Top_5.html` | `02` | `TIER_4` | HISTORICAL_NARRATIVE | 43688 | `a01c1706657b1a5abc76ec22e8e108a2d534608cda5f824fe656f257195d4192` |
| 52 | `02_PHASE_HISTORY/Phase_2_Patent_Landscape/Phase2_DeepResearch_Prompt_v2.md` | `02` | `TIER_4` | HISTORICAL_NARRATIVE | 8965 | `372d5ccbc23bd7b8e444fb6071aea4e4760397b5c1a360201d288609b1efcefd` |
| 53 | `02_PHASE_HISTORY/Phase_2_Patent_Landscape/Phase2_Memory.md` | `02` | `TIER_4` | HISTORICAL_NARRATIVE | 7820 | `973519f45bc075c296d4302b94933288496bd9bc12fae708aac1fb7020158ce8` |
| 54 | `02_PHASE_HISTORY/Phase_2_Patent_Landscape/Phase2_Report_From_Claude.pdf` | `02` | `TIER_4` | HISTORICAL_NARRATIVE | 488517 | `ab93da2c1ad6a9e22678e59da64a8992e4275ac4b01bad1061995dd9a5bf4f04` |
| 55 | `02_PHASE_HISTORY/Phase_2_Patent_Landscape/Phase2_Report_by_Claude.md` | `02` | `TIER_4` | HISTORICAL_NARRATIVE | 44493 | `783729d0e07e725236db5296dae8504ce782c294b8c61cfab40ea172cfa6943e` |
| 56 | `02_PHASE_HISTORY/Phase_2_Patent_Landscape/Phase2_SOP.md` | `02` | `TIER_4` | HISTORICAL_NARRATIVE | 6177 | `c7d7d805d41313dee1dce65d9323c95075a8cde8d61ff2bfce3700510c41dd54` |
| 57 | `02_PHASE_HISTORY/Phase_2_Patent_Landscape/Raw_Research/01_ChatGPT_Patent_Research.docx` | `02` | `TIER_4` | HISTORICAL_SUPPORT | 27850 | `61188e3fc06ca9ab2ddd8c196d217f10a59e077fe9b32687e2c0920d486501d5` |
| 58 | `02_PHASE_HISTORY/Phase_2_Patent_Landscape/Raw_Research/02_Gemini_Phase2_Research.docx` | `02` | `TIER_4` | HISTORICAL_SUPPORT | 3011880 | `5af919473e667c9bae7abbdfc5f98067472f40beb5a3e5f1c793a0f12e4d0f53` |
| 59 | `02_PHASE_HISTORY/Phase_2_Patent_Landscape/Raw_Research/03_Kimi_Patent_Research.pdf` | `02` | `TIER_4` | HISTORICAL_SUPPORT | 1472114 | `33f4539a14653b55c0b73e0fbcd140827e2131ed9c3ca5d9bc896d4553f4a904` |
| 60 | `02_PHASE_HISTORY/Phase_2_Patent_Landscape/Raw_Research/04_Qwen_Patent_Research_Full.pdf` | `02` | `TIER_4` | HISTORICAL_SUPPORT | 752520 | `75d736454cf7362a31e9ae1e2695a7bd793ab98187f2ad51ba9dc44f0d4473a7` |
| 61 | `02_PHASE_HISTORY/Phase_2_Patent_Landscape/Raw_Research/05_Qwen_Phase2_Research_Variant.md` | `02` | `TIER_4` | HISTORICAL_SUPPORT | 92668 | `5593a0581c350814e5567357effb2b1948cd3046a67bf52e00ff7495b9c0afe8` |
| 62 | `02_PHASE_HISTORY/Phase_3/Phase3_DeepResearch_Prompt.md` | `02` | `TIER_4` | HISTORICAL_NARRATIVE | 9989 | `4173379249d0dca88800c04432b71cf1184f958abf2809d72c023363cdd1449c` |
| 63 | `02_PHASE_HISTORY/Phase_3/Phase3_SOP.md` | `02` | `TIER_4` | HISTORICAL_NARRATIVE | 6227 | `3c3bfa374c40280be56adbd22f5ba7e07c3f38254557c0d1885da5708f6c53de` |
| 64 | `02_PHASE_HISTORY/Phase_3/Phase_3A_Engineering_Landscape/Claude_Phase3A_Research_Report.pdf` | `02` | `TIER_4` | HISTORICAL_NARRATIVE | 792034 | `7d0202fb62476a0212e594af473ad8d796eecd853e53e7f0952de90908cec611` |
| 65 | `02_PHASE_HISTORY/Phase_3/Phase_3A_Engineering_Landscape/Phase3A_MEMORY.md` | `02` | `TIER_4` | HISTORICAL_NARRATIVE | 8898 | `acd3b4178143ca918ed4cce43d3d853acc994c0178dc8efdc406fb014e1ec997` |
| 66 | `02_PHASE_HISTORY/Phase_3/Phase_3A_Engineering_Landscape/Raw_Research/01_Gemini_Phase3A_Research.docx` | `02` | `TIER_4` | HISTORICAL_SUPPORT | 53060 | `6d380794c7b52664324a1e4e39dac49f40f50ad269391cbe1f6135175048b944` |
| 67 | `02_PHASE_HISTORY/Phase_3/Phase_3A_Engineering_Landscape/Raw_Research/02_Mistral_Phase3A_Research.md` | `02` | `TIER_4` | HISTORICAL_SUPPORT | 122129 | `ae11e6b64bed09dcde373a21849085dd929a96f045d8a2362d4f07d58daed5c6` |
| 68 | `02_PHASE_HISTORY/Phase_3/Phase_3A_Engineering_Landscape/Raw_Research/03_Perplexity_Phase3A_Research.pdf` | `02` | `TIER_4` | HISTORICAL_SUPPORT | 905522 | `a56c84e5ca354f3e1451fa98cd49d7184247c95b2b1ddf5b7e04a24bd954d19b` |
| 69 | `02_PHASE_HISTORY/Phase_3/Phase_3A_Engineering_Landscape/Raw_Research/04_Qwen_Phase3A_Research.md` | `02` | `TIER_4` | HISTORICAL_SUPPORT | 63435 | `501782f664994ad0cfdeb72f16a975c2abe3a87ee4c456375a703f426437c99b` |
| 70 | `02_PHASE_HISTORY/Phase_3/Phase_3B_Feasibility_Analysis/Phase3B_DeepResearch_Prompt.md` | `02` | `TIER_4` | HISTORICAL_NARRATIVE | 11471 | `2d0a79d6fe7e24bf1cc4c1d4b4a9e2c0cd3c8cead10ad0323b63709eec2811e6` |
| 71 | `02_PHASE_HISTORY/Phase_3/Phase_3B_Feasibility_Analysis/Phase3B_MEMORY.md` | `02` | `TIER_4` | HISTORICAL_NARRATIVE | 18836 | `7b6532c779867e9d6064473de4ba1b4799a0c385361cf27dc4616888fb0ac7ad` |
| 72 | `02_PHASE_HISTORY/Phase_3/Phase_3B_Feasibility_Analysis/Phase3B_Report_by_Claude.md` | `02` | `TIER_4` | HISTORICAL_NARRATIVE | 83718 | `14c19ac85b56e4e27da03de534a2a574ab7220d90005b4a7a0afb868f6390478` |
| 73 | `02_PHASE_HISTORY/Phase_3/Phase_3B_Feasibility_Analysis/Project_mC_Phase3B_SOP.md` | `02` | `TIER_4` | HISTORICAL_NARRATIVE | 8028 | `6ce2ed40885038734faa75018a1caa16d89fcc7f18c7bf8249fe42453f36af4c` |
| 74 | `02_PHASE_HISTORY/Phase_3/Phase_3B_Feasibility_Analysis/Raw_Research/01_Gemini_Phase3B_Research.docx` | `02` | `TIER_4` | HISTORICAL_SUPPORT | 3012247 | `94e1e8e81c3f79f3f426086677841b1b4c2c32da8b50710e080bd0a27b9e2906` |
| 75 | `02_PHASE_HISTORY/Phase_3/Phase_3B_Feasibility_Analysis/Raw_Research/02_Mistral_Phase3B_Research.md` | `02` | `TIER_4` | HISTORICAL_SUPPORT | 81611 | `254d0b0a0df0cdab2fecb7ef65148474faff4f16c440fe4e76d0ada53cb6dc11` |
| 76 | `02_PHASE_HISTORY/Phase_3/Phase_3B_Feasibility_Analysis/Raw_Research/03_Qwen_Phase3B_Research.pdf` | `02` | `TIER_4` | HISTORICAL_SUPPORT | 649615 | `7a8fbde6b8fab93e195deefa716fb3f3724c369aa87deef27256be8fe8b45e1f` |
| 77 | `02_PHASE_HISTORY/Phase_3/Phase_3B_Feasibility_Analysis/Raw_Research/04_Perplexity_Phase3B_Research.md` | `02` | `TIER_4` | HISTORICAL_SUPPORT | 49895 | `65a891eda465cab8f3d1d69e8320497dc8c05c5a2176c25d9c0cb81218f4b4d5` |
| 78 | `02_PHASE_HISTORY/Phase_3/Phase_3C_Comparative_Evaluation/Original_Phase3C_README.md` | `02` | `TIER_4` | HISTORICAL_NARRATIVE | 2573 | `839ebfd63f94bfbbeb7450785e111f3d9225bdb356d40d1404da1f5aebf937eb` |
| 79 | `02_PHASE_HISTORY/Phase_3/Phase_3C_Comparative_Evaluation/Phase3C_Portfolio_Closure_Memo_Approved.md` | `02` | `TIER_4` | HISTORICAL_NARRATIVE | 3149 | `3c6e6f568c06099251b4b71d4f35cf668ee23a40c8214c95e4a12fe36cf4845a` |
| 80 | `03_CONCEPT_PORTFOLIO/OpenBraille/06_Historical_Phase3C_Research_and_Prompts/Prompts/Phase3C_OpenBraille_Deep_Research_Prompt_Final.md` | `03` | `TIER_4` | HISTORICAL_SUPPORT | 19686 | `a59b4743782e0e21e1472b28b116a1bf83a2ede098a28e8d5110a8ab1ce33e42` |
| 81 | `03_CONCEPT_PORTFOLIO/OpenBraille/06_Historical_Phase3C_Research_and_Prompts/Prompts/Phase3C_OpenBraille_Synthesis_Prompt_Claude.md` | `03` | `TIER_4` | HISTORICAL_SUPPORT | 17554 | `7b0ebdef37e932e8d252b397c6fc92010cce79b6805874b1b264dfa171e911d8` |
| 82 | `03_CONCEPT_PORTFOLIO/OpenBraille/06_Historical_Phase3C_Research_and_Prompts/Raw_Engineering_Research/Phase3C_OpenBraille_Raw_Research_Gemini.docx` | `03` | `TIER_4` | HISTORICAL_SUPPORT | 3059479 | `a1d2b01cdbaa412c79251ffec0b7fad9e606aa16609a664a88b6ebd8149b8b7c` |
| 83 | `03_CONCEPT_PORTFOLIO/OpenBraille/06_Historical_Phase3C_Research_and_Prompts/Raw_Engineering_Research/Phase3C_OpenBraille_Raw_Research_Mistral.md` | `03` | `TIER_4` | HISTORICAL_SUPPORT | 75348 | `aff5ebe5ff1fedfc5cc52cb9ef52d6b742ea495ff5304eb5acedaa8ff7e21c83` |
| 84 | `03_CONCEPT_PORTFOLIO/OpenBraille/06_Historical_Phase3C_Research_and_Prompts/Raw_Engineering_Research/Phase3C_OpenBraille_Raw_Research_Perplexity.docx` | `03` | `TIER_4` | HISTORICAL_SUPPORT | 534977 | `6350e11ac346e30fbb3ca252a40367e4394bfcf1cf9e1f2ad8c84fcf1bf3545d` |
| 85 | `03_CONCEPT_PORTFOLIO/OpenBraille/06_Historical_Phase3C_Research_and_Prompts/Raw_Engineering_Research/Phase3C_OpenBraille_Raw_Research_Qwen.md` | `03` | `TIER_4` | HISTORICAL_SUPPORT | 45014 | `3416c5526a1c73e5b29acf0117d45b4a5ee86cc1391eb9a105ca6710d0048f2b` |
| 86 | `03_CONCEPT_PORTFOLIO/Other_Concepts/README.md` | `03` | `TIER_4` | HISTORICAL_NARRATIVE | 376 | `24263bb23e002f3143d034549f9cfbf20de0d0accb1a5aa0c97c47b510186b9a` |
| 87 | `03_CONCEPT_PORTFOLIO/Other_Concepts/TrustLatch/HISTORICAL_Phase1C_TrustLatch_Concept_Dossier.docx` | `03` | `TIER_4` | HISTORICAL_NARRATIVE | 39031 | `f9a4184850435aba3ec26e480e802d1ba39f17037f0f368520a625c6f8e84f78` |
| 88 | `03_CONCEPT_PORTFOLIO/TrueMoist/06_Historical_Phase3C_Research_and_Prompts/Prompts/Phase3C_TrueMoist_Deep_Research_Prompt_Final.md` | `03` | `TIER_4` | HISTORICAL_SUPPORT | 28220 | `da66d2b9259a007d390b7fdc2766b9349bf88497cd60af3bc0c5e6855cddd08e` |
| 89 | `03_CONCEPT_PORTFOLIO/TrueMoist/06_Historical_Phase3C_Research_and_Prompts/Prompts/Phase3C_TrueMoist_Synthesis_Prompt_Final.md` | `03` | `TIER_4` | HISTORICAL_SUPPORT | 10637 | `144617f2efe8ef6db6122d00039fcc3566d8aab03649e003837eea5c0a60618e` |
| 90 | `03_CONCEPT_PORTFOLIO/TrueMoist/06_Historical_Phase3C_Research_and_Prompts/Raw_Engineering_Research/Phase3C_TrueMoist_Raw_Research_ChatGPT.pdf` | `03` | `TIER_4` | HISTORICAL_SUPPORT | 17994349 | `87ccbd3416f3f7bb58e544095a1e20560f9561ffe72db82f868d17bf942812e7` |
| 91 | `03_CONCEPT_PORTFOLIO/TrueMoist/06_Historical_Phase3C_Research_and_Prompts/Raw_Engineering_Research/Phase3C_TrueMoist_Raw_Research_Gemini.docx` | `03` | `TIER_4` | HISTORICAL_SUPPORT | 138980 | `b0eab8009831f5b719bf9d20ad1f25e9bcc549fc260a078a5be2531dc86e5b24` |
| 92 | `03_CONCEPT_PORTFOLIO/TrueMoist/06_Historical_Phase3C_Research_and_Prompts/Raw_Engineering_Research/Phase3C_TrueMoist_Raw_Research_Mistral.md` | `03` | `TIER_4` | HISTORICAL_SUPPORT | 19116 | `706d9ae47b256de0bb01d2836c3b24095b4109fd6c1011491aa88d32799fd1c5` |
| 93 | `03_CONCEPT_PORTFOLIO/TrueMoist/06_Historical_Phase3C_Research_and_Prompts/Raw_Engineering_Research/Phase3C_TrueMoist_Raw_Research_Perplexity.md` | `03` | `TIER_4` | HISTORICAL_SUPPORT | 87503 | `caefe1da05e1963e0cd9c3916fc50d4c2e4b396006cdf39ebf8eee893f0c3187` |
| 94 | `03_CONCEPT_PORTFOLIO/VibeGuard/06_Historical_Phase3C_Research_and_Prompts/Prompts/Phase3C_VibeGuard_Deep_Research_Prompt_Final.md` | `03` | `TIER_4` | HISTORICAL_SUPPORT | 25491 | `af08518f2c65bc8a53ff2520775415d2fd7f3bd5da2fc7e37018ae96a0c412d6` |
| 95 | `03_CONCEPT_PORTFOLIO/VibeGuard/06_Historical_Phase3C_Research_and_Prompts/Prompts/Phase3C_VibeGuard_Synthesis_Prompt_Claude.md` | `03` | `TIER_4` | HISTORICAL_SUPPORT | 16519 | `26b50889394442be4fb22e26fad74b6ca97c7e5765f330b92b241ff8e69c1a2e` |
| 96 | `03_CONCEPT_PORTFOLIO/VibeGuard/06_Historical_Phase3C_Research_and_Prompts/Prompts/Phase3C_VibeGuard_Synthesis_Prompt_Claude.mmd` | `03` | `TIER_4` | HISTORICAL_SUPPORT | 16518 | `59ae97bd4407b3e18cb2fb9ac99abdeeaf9aa3fdc3f5cb5e6f8ea67f330da47e` |
| 97 | `03_CONCEPT_PORTFOLIO/VibeGuard/06_Historical_Phase3C_Research_and_Prompts/Raw_Engineering_Research/Phase3C_VibeGuard_Raw_Research_Gemini.docx` | `03` | `TIER_4` | HISTORICAL_SUPPORT | 3049401 | `39a249ed0b0c9d76b0372e558b04d47a837b6a1849848f84fa9bf88f1ade0921` |
| 98 | `03_CONCEPT_PORTFOLIO/VibeGuard/06_Historical_Phase3C_Research_and_Prompts/Raw_Engineering_Research/Phase3C_VibeGuard_Raw_Research_Mistral.md` | `03` | `TIER_4` | HISTORICAL_SUPPORT | 53102 | `86efffd004de1dd811343d0d6def5c8955189f66aa56af244f6b5d2d4dacc355` |
| 99 | `03_CONCEPT_PORTFOLIO/VibeGuard/06_Historical_Phase3C_Research_and_Prompts/Raw_Engineering_Research/Phase3C_VibeGuard_Raw_Research_Perplexity.md` | `03` | `TIER_4` | HISTORICAL_SUPPORT | 46791 | `0b1a2ea090cbc3630e84f4c4902e307e72751ca531f85bfe473285f74f4df368` |
| 100 | `03_CONCEPT_PORTFOLIO/VibeGuard/06_Historical_Phase3C_Research_and_Prompts/Raw_Engineering_Research/Phase3C_VibeGuard_Raw_Research_Qwen.md` | `03` | `TIER_4` | HISTORICAL_SUPPORT | 42575 | `a16b18b36f221d2a3f4de53d65068de3bb20d253e0d550c60c7735b30ae19f4d` |
| 101 | `03_CONCEPT_PORTFOLIO/OpenBraille/01_Final_Architecture/Phase3C_OpenBraille_Architecture_Report_Final.md` | `04` | `TIER_1` | CORE_NARRATIVE | 46132 | `84c658ba992d729027b1f931f8c20715f5deecf385b78e767e4c32e2b83354e1` |
| 102 | `03_CONCEPT_PORTFOLIO/OpenBraille/01_Final_Architecture/Phase3C_OpenBraille_Memory_Final.md` | `04` | `TIER_1` | CORE_NARRATIVE | 12364 | `5dad0e392cf9c64d7e8f29be09fadb70acde5b965b95744fa066b5f4b4fd30eb` |
| 103 | `03_CONCEPT_PORTFOLIO/OpenBraille/01_Final_Architecture/Phase3C_OpenBraille_SOP_Final.md` | `04` | `TIER_1` | CORE_NARRATIVE | 4746 | `bfee5dc46675d77b318f4a0d4fe864d77a570a1150cc2676a5dd10103f214e50` |
| 104 | `03_CONCEPT_PORTFOLIO/OpenBraille/PATENT_EVIDENCE_INDEX.md` | `04` | `TIER_2` | SUPPORTING_EVIDENCE | 585 | `307cb70cbb5544daf76582082e480e7fa4a22cc50fffa848f9ddd473ecd43255` |
| 105 | `03_CONCEPT_PORTFOLIO/OpenBraille/README.md` | `04` | `TIER_2` | SUPPORTING_EVIDENCE | 225 | `a5b2c7104d3ffdfcc12232ddbea726b8c87c60341d8883395b070736757d6339` |
| 106 | `03_CONCEPT_PORTFOLIO/OpenBraille/02_Raw_Research/01_OpenBraille_Patent_Research_ChatGPT_Deep_Research.md` | `05` | `TIER_3` | SUPPORTING_EVIDENCE | 67307 | `979eb5d5155c9fe1243f582320f716ca549f267cbc711597dba7287f51b7c257` |
| 107 | `03_CONCEPT_PORTFOLIO/OpenBraille/02_Raw_Research/02_OpenBraille_Patent_Research_Gemini.docx` | `05` | `TIER_3` | SUPPORTING_EVIDENCE | 3037768 | `f42e0c020ce6bb38f569bc0757589c5a5410a31b98bb80461355d473afb6434f` |
| 108 | `03_CONCEPT_PORTFOLIO/OpenBraille/02_Raw_Research/03_OpenBraille_Patent_Research_Perplexity_PARTIAL.docx` | `05` | `TIER_3` | SUPPORTING_EVIDENCE | 399503 | `83a53fc7eecf97a9cf76cce718298b24d9cf93a150046ae5bc5a4290730bf74b` |
| 109 | `03_CONCEPT_PORTFOLIO/OpenBraille/02_Raw_Research/04_OpenBraille_Patent_Research_Qwen.md` | `05` | `TIER_3` | SUPPORTING_EVIDENCE | 49399 | `79163acf026753e5fe835be66adc8e7d9fc0e0575b09395fd22f227ce5ee5567` |
| 110 | `03_CONCEPT_PORTFOLIO/OpenBraille/02_Raw_Research/05_OpenBraille_Patent_Research_Mistral.md` | `05` | `TIER_3` | SUPPORTING_EVIDENCE | 46448 | `01f4d8b9f146f2c7989000672b47456628966b705dd06350b3683496df522aad` |
| 111 | `03_CONCEPT_PORTFOLIO/OpenBraille/02_Raw_Research/06_OpenBraille_Patent_Research_Microsoft_Copilot.docx` | `05` | `TIER_3` | SUPPORTING_EVIDENCE | 3028206 | `75e34f06275338189e29373c598afdbd60becb8d1a1e562ef7922a009bae77d6` |
| 112 | `03_CONCEPT_PORTFOLIO/OpenBraille/03_Patent_Synthesis/01_OpenBraille_Patent_Synthesis_Work_Max.md` | `05` | `TIER_2` | CORE_DECISION_EVIDENCE | 113903 | `d92dbfbbbdbd4c49e9eaac9fab01e0d2a7db6d986c81d33ee65223710dd42eb1` |
| 113 | `03_CONCEPT_PORTFOLIO/OpenBraille/03_Patent_Synthesis/02_OpenBraille_Patent_Synthesis_Valid_Secondary.md` | `05` | `TIER_2` | CORE_DECISION_EVIDENCE | 86337 | `b9fefadf621f014dc621ef9836ae11b80c05a0227f768c53c11ec1358fc8a09b` |
| 114 | `03_CONCEPT_PORTFOLIO/OpenBraille/04_PreBuild_Simulation/OpenBraille_PreBuild_Future_Patent_Case_Simulation.md` | `05` | `TIER_2` | CONDITIONAL_EVIDENCE | 90393 | `c38b519adae4831714b5fda8dbae86f2ac97ffe748cabf5cf421651a1b64c8a7` |
| 115 | `03_CONCEPT_PORTFOLIO/OpenBraille/05_Roadmaps_and_Reference_Dossiers/HISTORICAL_Phase1C_OpenBraille_Concept_Dossier.docx` | `05` | `TIER_2` | CORE_OR_SUPPORTING | 38405 | `ac21af2a892f319e0b28d4d7314f4561c5aebad5291343c34d777beb933106ea` |
| 116 | `03_CONCEPT_PORTFOLIO/OpenBraille/05_Roadmaps_and_Reference_Dossiers/OpenBraille_Semester_Architecture_and_Future_Research_Reference_Dossier.docx` | `05` | `TIER_2` | CORE_OR_SUPPORTING | 706017 | `b4ef1d7301d5e0a669185681160cb20c8a85d2464b822c3c569798238f13e27b` |
| 117 | `03_CONCEPT_PORTFOLIO/OpenBraille/05_Roadmaps_and_Reference_Dossiers/OpenBraille_Semester_Architecture_and_Future_Research_Reference_Dossier.pdf` | `05` | `TIER_2` | CORE_OR_SUPPORTING | 792616 | `ee9cce3ebd57dd84b3bbacd9d4738fc219a334441b80c2bb34e0417c90060ab4` |
| 118 | `03_CONCEPT_PORTFOLIO/VibeGuard/01_Final_Architecture/Phase3C_VibeGuard_Architecture_Report_Final.md` | `06` | `TIER_1` | CORE_NARRATIVE | 32583 | `ba7d1824fe1ab260be903aead8d9bac00cee83141b6f7728d0e220b65fd8eeb4` |
| 119 | `03_CONCEPT_PORTFOLIO/VibeGuard/01_Final_Architecture/Phase3C_VibeGuard_Memory_Final.md` | `06` | `TIER_1` | CORE_NARRATIVE | 9527 | `e4b96f7ee53bbc94ec960db281a1a56745fc6c8121133b813ca37b76798da5e5` |
| 120 | `03_CONCEPT_PORTFOLIO/VibeGuard/01_Final_Architecture/Phase3C_VibeGuard_SOP_Final.md` | `06` | `TIER_1` | CORE_NARRATIVE | 15750 | `6386bf6d73bbbbb7127c568692ba09abcbdf6dc4cbac40a97690b4edb0dca974` |
| 121 | `03_CONCEPT_PORTFOLIO/VibeGuard/05_Roadmaps_and_Reference_Dossiers/HISTORICAL_Phase1C_VibeGuard_Concept_Dossier.docx` | `06` | `TIER_2` | CORE_OR_SUPPORTING | 38619 | `8a3c40cdc9ec899934ca9a37b05f9c0df22b583cd3ee259ebc81c1da9f0a0ae7` |
| 122 | `03_CONCEPT_PORTFOLIO/VibeGuard/05_Roadmaps_and_Reference_Dossiers/VibeGuard_Semester_Implementation_and_Future_Research_Roadmap.pdf` | `06` | `TIER_2` | CORE_OR_SUPPORTING | 788462 | `8702d859cdcf816afb2ac31673759a0382348fb69b8e6a4c65120b7c7fe0deff` |
| 123 | `03_CONCEPT_PORTFOLIO/VibeGuard/PATENT_EVIDENCE_INDEX.md` | `06` | `TIER_2` | SUPPORTING_EVIDENCE | 606 | `cb80b048a9238c232ed2b9a37da9f0997ba65cd5eb5f0f303764c42b51c99e4b` |
| 124 | `03_CONCEPT_PORTFOLIO/VibeGuard/README.md` | `06` | `TIER_2` | SUPPORTING_EVIDENCE | 205 | `1c2d6a321bb7c2673eefed788241e515bae213a5e654c3f524f8a6b3dad89b9f` |
| 125 | `03_CONCEPT_PORTFOLIO/VibeGuard/02_Raw_Research/01_VibeGuard_Patent_Research_ChatGPT_Deep_Research.md` | `07` | `TIER_3` | SUPPORTING_EVIDENCE | 52881 | `8614a18e8d7764437315a41b61ed46f4fb3e2dcd6eaa8b12e59a0b57ffdd79a7` |
| 126 | `03_CONCEPT_PORTFOLIO/VibeGuard/02_Raw_Research/02_VibeGuard_Patent_Research_Gemini.docx` | `07` | `TIER_3` | SUPPORTING_EVIDENCE | 3039911 | `45001494bc2c8fa8ea5445776e084772493a034ddfc13423a24000baeb451a74` |
| 127 | `03_CONCEPT_PORTFOLIO/VibeGuard/02_Raw_Research/03_VibeGuard_Patent_Research_Perplexity.md` | `07` | `TIER_3` | SUPPORTING_EVIDENCE | 70205 | `01886aca6ee604cf05f3cc8d082b70e1b1c82c8e4dbccf8ce47e0e5d437be8cc` |
| 128 | `03_CONCEPT_PORTFOLIO/VibeGuard/02_Raw_Research/04_VibeGuard_Patent_Research_Qwen.md` | `07` | `TIER_3` | SUPPORTING_EVIDENCE | 25767 | `f3d0aa97e4f67197fed317503a2959e788d092c3af11d5b909bff344912cd561` |
| 129 | `03_CONCEPT_PORTFOLIO/VibeGuard/02_Raw_Research/05_VibeGuard_Patent_Research_Mistral_PARTIAL_COMPILATION.md` | `07` | `TIER_3` | SUPPORTING_EVIDENCE | 51968 | `2055d44aa9697572c6ef59cfe5f08780cfc8d415bba2beacb9f8f54e54510134` |
| 130 | `03_CONCEPT_PORTFOLIO/VibeGuard/02_Raw_Research/06_VibeGuard_Patent_Research_Microsoft_Copilot.docx` | `07` | `TIER_3` | SUPPORTING_EVIDENCE | 30944 | `f6c49a26af177d0faca247feb6aaa98cc2df389fae00bb4d6fd848d10e8540dd` |
| 131 | `03_CONCEPT_PORTFOLIO/VibeGuard/03_Patent_Synthesis/01_VibeGuard_Patent_Synthesis_Work_Max.md` | `07` | `TIER_2` | CORE_DECISION_EVIDENCE | 111826 | `f61955b09b976a4c445fcdddbc40aada02cae204302876dbfc7cf1825b8cdf72` |
| 132 | `03_CONCEPT_PORTFOLIO/VibeGuard/03_Patent_Synthesis/02_VibeGuard_Patent_Synthesis_Standard_High.md` | `07` | `TIER_2` | CORE_DECISION_EVIDENCE | 70134 | `b32a41ce9f0a3fe3ab17e55657bd14796cc77b401852b730254f1ac580b2adc4` |
| 133 | `03_CONCEPT_PORTFOLIO/VibeGuard/04_PreBuild_Simulation/VibeGuard_PreBuild_Future_Patent_Case_Simulation.md` | `07` | `TIER_2` | CONDITIONAL_EVIDENCE | 97630 | `d57a571391e17021a91abba9932f1ecbc5ab6fb6f3e5abdf9221106d9451f4ca` |
| 134 | `03_CONCEPT_PORTFOLIO/TrueMoist/01_Final_Architecture/Phase3C_TrueMoist_Architecture_Report_Final.md` | `08` | `TIER_1` | CORE_NARRATIVE | 46897 | `6c71f1d618e0575d127b10f05e91d06ea4b1f0b8a2fe63e78d4022ee75234610` |
| 135 | `03_CONCEPT_PORTFOLIO/TrueMoist/01_Final_Architecture/Phase3C_TrueMoist_Memory_Final.md` | `08` | `TIER_1` | CORE_NARRATIVE | 5232 | `c84bc0e08c8c96cfe410d8c690df35c6b7996e5ffda7703ceff37a424bf02df1` |
| 136 | `03_CONCEPT_PORTFOLIO/TrueMoist/01_Final_Architecture/Phase3C_TrueMoist_SOP_Final.md` | `08` | `TIER_1` | CORE_NARRATIVE | 18712 | `993caf1a05f3fdc3937efb634e2f2e467488e973eb71454db8e3c3f53d178d00` |
| 137 | `03_CONCEPT_PORTFOLIO/TrueMoist/02_Raw_Research/01_TrueMoist_Patent_Research_ChatGPT_Deep_Research.md` | `08` | `TIER_3` | SUPPORTING_EVIDENCE | 62032 | `9a4a4cffc2f82b3f4022bc5db2d094afa54a1c9ccfb39d43e6b3321a2af1d8bb` |
| 138 | `03_CONCEPT_PORTFOLIO/TrueMoist/02_Raw_Research/02_TrueMoist_Patent_Research_Gemini.docx` | `08` | `TIER_3` | SUPPORTING_EVIDENCE | 3040693 | `4587f69d6f611e45c5a19088c76801579faa688c48fcf312566eaacab3b28d91` |
| 139 | `03_CONCEPT_PORTFOLIO/TrueMoist/02_Raw_Research/03_TrueMoist_Patent_Research_Perplexity_PARTIAL.md` | `08` | `TIER_3` | SUPPORTING_EVIDENCE | 67500 | `ddc397e72125105f85897055ad6c3281308ae5015e236b0f6b0666067a00795f` |
| 140 | `03_CONCEPT_PORTFOLIO/TrueMoist/02_Raw_Research/04_TrueMoist_Patent_Research_Qwen_COMPILATION.md` | `08` | `TIER_3` | SUPPORTING_EVIDENCE | 61439 | `563ec1237fdfc84f9ecd7da9ef541f39a38305cf49976304b66c20ea26132902` |
| 141 | `03_CONCEPT_PORTFOLIO/TrueMoist/02_Raw_Research/05_TrueMoist_Patent_Research_Mistral.md` | `08` | `TIER_3` | SUPPORTING_EVIDENCE | 38894 | `e70085325409b6af0a61884a1b2f13ced5c20fcdc49c5f2e982ab52ca1131f16` |
| 142 | `03_CONCEPT_PORTFOLIO/TrueMoist/02_Raw_Research/06_TrueMoist_Patent_Research_Microsoft_Copilot.docx` | `08` | `TIER_3` | SUPPORTING_EVIDENCE | 42032 | `18ffe78f06c7d1a6b30a022474e0cbb660d5e4670e9658cdd5048f233a4b135d` |
| 143 | `03_CONCEPT_PORTFOLIO/TrueMoist/03_Patent_Synthesis/01_TrueMoist_Patent_Evidence_Synthesis_Max.md` | `08` | `TIER_2` | CORE_DECISION_EVIDENCE | 84487 | `f43847c672ca9b132a7ef6219a9ce00deb8f0ab657c0bda6a7ed3a930a697900` |
| 144 | `03_CONCEPT_PORTFOLIO/TrueMoist/03_Patent_Synthesis/02_TrueMoist_Patent_Evidence_Synthesis_High_Deep_Research.md` | `08` | `TIER_2` | CORE_DECISION_EVIDENCE | 70087 | `ddf421678c6f5dbafd7e2d61db82a4b7c1d8c3d817afb4341538ec98f4d91505` |
| 145 | `03_CONCEPT_PORTFOLIO/TrueMoist/05_Roadmaps_and_Reference_Dossiers/HISTORICAL_Phase1C_TrueMoist_Concept_Dossier.docx` | `08` | `TIER_2` | SUPPORTING_EVIDENCE | 38768 | `ca5cedfdfac5157b328aa865433a172d8af82a44d2dbf8b015c8c217fa6f85a2` |
| 146 | `03_CONCEPT_PORTFOLIO/TrueMoist/PATENT_EVIDENCE_INDEX.md` | `08` | `TIER_2` | SUPPORTING_EVIDENCE | 572 | `163cb6af44fcced08d6427b30ad00e155163377d0deb33bbced9f2583d3350a1` |
| 147 | `03_CONCEPT_PORTFOLIO/TrueMoist/README.md` | `08` | `TIER_2` | SUPPORTING_EVIDENCE | 228 | `ea18f095605ccd146aff3f0af396ebfc8fd554fea26eb456b1ca187b52620067` |
| 148 | `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/00_Engineering_Design_Review.md` | `09` | `TIER_2` | CORE_DECISION_EVIDENCE | 31205 | `46f017501ac3ff9ebd6c1fb1e5ee8c068c22ddb08ae204c5609f2b759090295e` |
| 149 | `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/01_Comparison_Protocol.md` | `09` | `TIER_2` | CORE_DECISION_EVIDENCE | 3679 | `9711020de0cc5108fb7e4a779e06fdba8e640a2100c098791d1a6b7ead410d7d` |
| 150 | `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/02_Authoritative_Source_Manifest.md` | `09` | `TIER_2` | CORE_DECISION_EVIDENCE | 7049 | `f2d6f77836230780b63ae10353d9bf65f61d43ef2500e0872b5e9a65e57835c6` |
| 151 | `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/03_Concept_Evidence_Matrix.md` | `09` | `TIER_2` | CORE_DECISION_EVIDENCE | 19491 | `8f999b878cfc7f863227682f141a278a4dfa4ee7705e49e1d55ef147c27a1975` |
| 152 | `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/04_Hard_Gate_Precheck.md` | `09` | `TIER_2` | CORE_DECISION_EVIDENCE | 10864 | `6ee8fb1e9570342b58cc1f4facfdce2c61cc1c71d3959dcbdf0951615c0cc02c` |
| 153 | `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/05_Uncertainty_and_Test_Register.md` | `09` | `TIER_2` | CORE_DECISION_EVIDENCE | 22484 | `125c057229524532b115391fbba948023684ad61d0153fb28ac29e6031e8ee3b` |
| 154 | `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/06_Patent_Research_Input_Pack.md` | `09` | `TIER_2` | CORE_DECISION_EVIDENCE | 16069 | `969d6bd97f0a726186d0f9bae405248ed82ef6314e3d5618166a0a1185411428` |
| 155 | `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/07_Scoring_Worksheet.md` | `09` | `TIER_2` | CORE_DECISION_EVIDENCE | 4652 | `e0a1aeea2e7ba0de3e571531bcca2f51f441bca9e860dbb10fa8d6d22a4f744b` |
| 156 | `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/08_High_Reasoning_Audit.md` | `09` | `TIER_2` | CORE_DECISION_EVIDENCE | 12651 | `4243ca6643361946805fcb4f5b3b7feb319ec352149b54664471b2d9cbd9e324` |
| 157 | `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/09_Final_Downselection_README.md` | `09` | `TIER_2` | CORE_DECISION_EVIDENCE | 2991 | `e213c44f71348a07dfa2b0982d5944fa8d4458f4a118531fd8ade6f2bf6e09e2` |
| 158 | `04_COMPARATIVE_DECISION/02_Final_Adjudications/01_Project_mC_Final_Adjudication_Work_Max.md` | `09` | `TIER_2` | CORE_DECISION_EVIDENCE | 90458 | `02baa83e691bf88e5221e20ac92e5be94eb3c71280b48c8338a02401bb173c9f` |
| 159 | `04_COMPARATIVE_DECISION/02_Final_Adjudications/02_Project_mC_Final_Adjudication_Deep_Research_High.md` | `09` | `TIER_2` | CORE_DECISION_EVIDENCE | 48193 | `29d0f85d95f7ef98d1a1a31a395cbbab5511ae25df2eeb15840978d7bfb3590e` |
| 160 | `04_COMPARATIVE_DECISION/03_Change_Request/Project_mC_Request_to_Change_from_OpenBraille_to_VibeGuard.docx` | `09` | `TIER_2` | CORE_DECISION_EVIDENCE | 47190 | `aebf3926dda0cb7dca568e8e0c54dbf4679550c3c3e50c1fd05c94ac5b0810f9` |
| 161 | `04_COMPARATIVE_DECISION/03_Change_Request/Project_mC_Request_to_Change_from_OpenBraille_to_VibeGuard.pdf` | `09` | `TIER_2` | CORE_DECISION_EVIDENCE | 162459 | `e331fcfddd8782336049de278dd58880c408c67a7448ceb02e171ef9792b0aba` |
| 162 | `04_COMPARATIVE_DECISION/04_Team_Audits_and_Objections/01_Team_Submission_6222246419165853974.pdf` | `09` | `TIER_2` | CORE_DECISION_EVIDENCE | 378559 | `80c2ddec1fb68dba305bcbce98a78221170644eb5338c99c4e6dd43242799bc6` |
| 163 | `04_COMPARATIVE_DECISION/04_Team_Audits_and_Objections/02_Team_Submission_6282084529079524834.pdf` | `09` | `TIER_2` | CORE_DECISION_EVIDENCE | 307362 | `fcf17069f5cd3e9ca6bd388792b3c4987b26618876c66991e1076764fc2e3539` |
| 164 | `04_COMPARATIVE_DECISION/04_Team_Audits_and_Objections/03_Team_Submission_IDK.pdf` | `09` | `TIER_2` | CORE_DECISION_EVIDENCE | 46035 | `59a07438163718094c4cd4704016cee80bacce689939eafa52eb9cb91e56f126` |
| 165 | `04_COMPARATIVE_DECISION/COMPARATIVE_DECISION_INDEX.md` | `09` | `TIER_2` | CORE_DECISION_EVIDENCE | 1407 | `ac94cb30df641c577af516da7047e1f2ebbdf1252620755aede08f9f0ed68568` |
| 166 | `05_TEACHER_AND_REVIEWS/01_Teacher_Documents/TEACHER_DELIVERY_INDEX.md` | `10` | `TIER_2` | CORE_OR_HISTORICAL | 1423 | `1b164de4571aaceba1f14dcf73c6f975a0f5dfd3bbd0e665ad9517ad79a78980` |
| 167 | `05_TEACHER_AND_REVIEWS/02_Zeroth_Review_OpenBraille/01_Official_Submission/OpenBraille_Zeroth_Review_OFFICIAL_2026-07-30.pptx` | `10` | `TIER_2` | CORE_OR_HISTORICAL | 1539135 | `8503780624e86aaabe94e67d90ce565633bea3f66ec018d27fc5d104ec0e5c9e` |
| 168 | `05_TEACHER_AND_REVIEWS/02_Zeroth_Review_OpenBraille/02_Drafts_and_Working_Files/01_Initial_Template_or_Early_Draft.pptx` | `10` | `TIER_2` | CORE_OR_HISTORICAL | 218917 | `1b65fdca64a3873c666e7ef777b6c2cbb423676280c762443ca952fdd0e83a99` |
| 169 | `05_TEACHER_AND_REVIEWS/02_Zeroth_Review_OpenBraille/02_Drafts_and_Working_Files/02_OpenBraille_Draft_0.1.pptx` | `10` | `TIER_2` | CORE_OR_HISTORICAL | 1222357 | `5b5c699a582f2a8a338e122f25094f099cf215e7faa61bbf55d7070678d0f1c0` |
| 170 | `05_TEACHER_AND_REVIEWS/02_Zeroth_Review_OpenBraille/02_Drafts_and_Working_Files/03_OpenBraille_Draft_0.2.pptx` | `10` | `TIER_2` | CORE_OR_HISTORICAL | 1522668 | `c749a1154fbfb70df38e30e65620c0f734d8ac98c23892207dcd3e535e8507d1` |
| 171 | `05_TEACHER_AND_REVIEWS/02_Zeroth_Review_OpenBraille/02_Drafts_and_Working_Files/04_OpenBraille_Draft_0.2.odp` | `10` | `TIER_2` | CORE_OR_HISTORICAL | 1498337 | `0900927d4bc12e4358fa213b6d19fd1794b2003181feb54b43689f4c11ea6648` |
| 172 | `05_TEACHER_AND_REVIEWS/02_Zeroth_Review_OpenBraille/02_Drafts_and_Working_Files/05_Sreehari_Working_Draft.pptx` | `10` | `TIER_2` | CORE_OR_HISTORICAL | 1520567 | `4326d708eb56198773dc6f5f7e4bb49407d51c19823a87700a3e390ebcbf5b2a` |
| 173 | `05_TEACHER_AND_REVIEWS/02_Zeroth_Review_OpenBraille/02_Drafts_and_Working_Files/06_Group8_Working_Draft.pptx` | `10` | `TIER_2` | CORE_OR_HISTORICAL | 1223087 | `3b26d17086f86b420a9fce25d4ac17eea063d206981651325313de99d3156225` |
| 174 | `05_TEACHER_AND_REVIEWS/02_Zeroth_Review_OpenBraille/02_Drafts_and_Working_Files/07_PreSubmission_Finalised_Draft_1.pptx` | `10` | `TIER_2` | CORE_OR_HISTORICAL | 1539123 | `f37809889f970377fccfddcb7bf3e2be98663f8b679c015b3f5441955562b5ea` |
| 175 | `05_TEACHER_AND_REVIEWS/02_Zeroth_Review_OpenBraille/02_Drafts_and_Working_Files/08_PreSubmission_Finalised_Draft_2.pptx` | `10` | `TIER_2` | CORE_OR_HISTORICAL | 1539278 | `a58be0d507c57600789074405d9cc48f1cd32094bd9158633a7fa3ed88dd16d7` |
| 176 | `05_TEACHER_AND_REVIEWS/02_Zeroth_Review_OpenBraille/02_Drafts_and_Working_Files/09_OpenBraille_Block_Diagram.png` | `10` | `TIER_2` | CORE_OR_HISTORICAL | 4481236 | `d9203a9b237b35005df2ee3d58f0ea5761186c65b9cf5466843b6af1faaf0d48` |
| 177 | `05_TEACHER_AND_REVIEWS/02_Zeroth_Review_OpenBraille/02_Drafts_and_Working_Files/10_OpenBraille_Generated_Visual.png` | `10` | `TIER_2` | CORE_OR_HISTORICAL | 2261645 | `e34d60d0250848dd9099b2d2e27bb3e2d302677f813331f592b3becf21f8eb3c` |
| 178 | `05_TEACHER_AND_REVIEWS/02_Zeroth_Review_OpenBraille/02_Drafts_and_Working_Files/11_Presentation_Instructions_Early.html` | `10` | `TIER_2` | CORE_OR_HISTORICAL | 35576 | `2bb9890bfc2c9754ae5643d825ff9bea9cfd3f1fcc22c2975dcbbd1553cb1f97` |
| 179 | `05_TEACHER_AND_REVIEWS/02_Zeroth_Review_OpenBraille/02_Drafts_and_Working_Files/12_Presentation_Instructions_2.0.html` | `10` | `TIER_2` | CORE_OR_HISTORICAL | 40539 | `300d2b47feb4995a5fbca41d1c475734d80075d943c14e3adb8f1fcdac1b0274` |
| 180 | `05_TEACHER_AND_REVIEWS/TEACHER_AND_REVIEW_INDEX.md` | `10` | `TIER_2` | CORE_OR_HISTORICAL | 832 | `3a63e255117614d24dd6751a34f071d1c43898e33ba03c947b415dcaabc6bb9d` |
| 181 | `06_TRANSPORT_AND_PROVENANCE/01_Governing_Instructions/Historical_Upload_Pack_Variants/OpenBraille_Patent_Synthesis_Input__00_READ_FIRST_OpenBraille_Synthesis_Instructions.md` | `12` | `TIER_5` | PROVENANCE_ONLY | 16780 | `b487647fb66611fa626ab2115f3b30e9d5e14398e02bbf430ade127d957af2ad` |
| 182 | `06_TRANSPORT_AND_PROVENANCE/01_Governing_Instructions/Historical_Upload_Pack_Variants/VibeGuard_Patent_Research_Input__00_READ_FIRST_VibeGuard_Patent_Research_Instructions.md` | `12` | `TIER_5` | PROVENANCE_ONLY | 19906 | `2be44bcc6702ccabbae554776e32c3aa6faaff26bcc4fd29e053b5ad9ea8b987` |
| 183 | `06_TRANSPORT_AND_PROVENANCE/01_Governing_Instructions/OpenBraille_Patent_Deep_Research_Instructions_LOCATED.md` | `12` | `TIER_5` | PROVENANCE_ONLY | 10055 | `f41208966b1efd4a0bb7462e11b25a54d7a54549a13ba6d1ad3c98131a56ed4e` |
| 184 | `06_TRANSPORT_AND_PROVENANCE/01_Governing_Instructions/OpenBraille_PreBuild_Patent_Simulation_Instructions.md` | `12` | `TIER_5` | PROVENANCE_ONLY | 11502 | `6400dd467d01d4d3c803a743da47ef91700ea3a1df64df6bfa39abe1703e6033` |
| 185 | `06_TRANSPORT_AND_PROVENANCE/01_Governing_Instructions/OpenBraille_Synthesis_Instructions_CANONICAL.md` | `12` | `TIER_5` | PROVENANCE_ONLY | 18120 | `9037c212a5727320911be31060a1f4b0ce590ca8c030b4c97019aa31aab60b67` |
| 186 | `06_TRANSPORT_AND_PROVENANCE/01_Governing_Instructions/Project_mC_Final_Adjudication_Instructions_CANONICAL.md` | `12` | `TIER_5` | PROVENANCE_ONLY | 16558 | `1a06d628347b4ec533a6ccea8f44b933de1295b29d9f4b407a028947c8b34ddc` |
| 187 | `06_TRANSPORT_AND_PROVENANCE/01_Governing_Instructions/Project_mC_Teacher_Document_Instructions.md` | `12` | `TIER_5` | PROVENANCE_ONLY | 9899 | `b01b52932625c877e18596693dac7c616100be5b434008e2f99f139005b5a067` |
| 188 | `06_TRANSPORT_AND_PROVENANCE/01_Governing_Instructions/TrueMoist_Patent_Research_Instructions_CANONICAL.md` | `12` | `TIER_5` | PROVENANCE_ONLY | 12812 | `e201944a6a67caa64c06cd95aeb3ccee4c2c9413e137da2ed6a73d99f0d6aca4` |
| 189 | `06_TRANSPORT_AND_PROVENANCE/01_Governing_Instructions/TrueMoist_Synthesis_Instructions_CANONICAL.md` | `12` | `TIER_5` | PROVENANCE_ONLY | 18024 | `88d6bfa12504b194fd153f8479ddc021d23551a19f6ed06fd0f20707f0146128` |
| 190 | `06_TRANSPORT_AND_PROVENANCE/01_Governing_Instructions/VibeGuard_Patent_Research_Instructions_CANONICAL.md` | `12` | `TIER_5` | PROVENANCE_ONLY | 20339 | `63e31548a3618e6af0503bfbc517c1a528bcc928bab83f0c93397c9f986d6dbc` |
| 191 | `06_TRANSPORT_AND_PROVENANCE/01_Governing_Instructions/VibeGuard_PreBuild_Patent_Simulation_Instructions.md` | `12` | `TIER_5` | PROVENANCE_ONLY | 7477 | `3d1abf8bf6ef471d447934858587f7a7d395c05d490b5bca8ac8242d77e56357` |
| 192 | `06_TRANSPORT_AND_PROVENANCE/01_Governing_Instructions/VibeGuard_Synthesis_Instructions_CANONICAL.md` | `12` | `TIER_5` | PROVENANCE_ONLY | 24526 | `49d7d80c90da3913b0b7ce8db0df4f982324bddc16c8c63d69240d53060414db` |
| 193 | `06_TRANSPORT_AND_PROVENANCE/02_Input_Manifests/Final_Adjudication_EXCLUSION_AND_PROVENANCE_REGISTER.md` | `12` | `TIER_5` | PROVENANCE_ONLY | 11518 | `b56ad079dacaf594fc80307d0a1ac4424c2493e11039290fe2a5666dbd4abfef` |
| 194 | `06_TRANSPORT_AND_PROVENANCE/02_Input_Manifests/OpenBraille_PreBuild_INPUT_MANIFEST.md` | `12` | `TIER_5` | PROVENANCE_ONLY | 14201 | `f7c917e943bbc492fcef160adac7f9a2a834b081684b589d54d2cc05f322eafc` |
| 195 | `06_TRANSPORT_AND_PROVENANCE/02_Input_Manifests/OpenBraille_Synthesis_INPUT_MANIFEST.md` | `12` | `TIER_5` | PROVENANCE_ONLY | 9189 | `f6553815bea3e272e27e5d166134844abfab337e78dc35a1ac3cdef89424b2c9` |
| 196 | `06_TRANSPORT_AND_PROVENANCE/02_Input_Manifests/Teacher_Document_Master_INPUT_MANIFEST.md` | `12` | `TIER_5` | PROVENANCE_ONLY | 16145 | `b5b83523f9079d95193e375f7e6dafc9c2a21deb12590f51f94b8a8961bf58c4` |
| 197 | `06_TRANSPORT_AND_PROVENANCE/02_Input_Manifests/TrueMoist_Synthesis_INPUT_MANIFEST.md` | `12` | `TIER_5` | PROVENANCE_ONLY | 14772 | `29a8c80af05acbcb564251db75650dfc556177efa445c092892c98e72da9f9e2` |
| 198 | `06_TRANSPORT_AND_PROVENANCE/02_Input_Manifests/VibeGuard_PreBuild_INPUT_MANIFEST.md` | `12` | `TIER_5` | PROVENANCE_ONLY | 12434 | `3e44c2dea5251d0be70cd6ad685db4a20967453439bf5a96a0511cdce44b0c47` |
| 199 | `06_TRANSPORT_AND_PROVENANCE/02_Input_Manifests/VibeGuard_Synthesis_INPUT_MANIFEST.md` | `12` | `TIER_5` | PROVENANCE_ONLY | 20501 | `b8034e85b2021d171f943c40d643305570d5b3f8452960e0147eeaf6799bb56a` |
| 200 | `06_TRANSPORT_AND_PROVENANCE/03_Launchers_and_Checklists/Codex_Workflows/CODEX_CREATE_TRUEMOIST_GEMINI10_QWEN5_PACKAGES.txt` | `12` | `TIER_5` | PROVENANCE_ONLY | 11561 | `603b9a2b92c80dbe62e3b4091a29d8f8f6ad88899e654877a29d704699ec4a18` |
| 201 | `06_TRANSPORT_AND_PROVENANCE/03_Launchers_and_Checklists/Codex_Workflows/CODEX_EXTRACTION_VALIDATION.md` | `12` | `TIER_5` | PROVENANCE_ONLY | 10622 | `6c7f24e2e75875b63b940783086006a48cb45d028193c9be45667312ff4c84ad` |
| 202 | `06_TRANSPORT_AND_PROVENANCE/03_Launchers_and_Checklists/Codex_Workflows/CODEX_ORGANIZE_PROJECT_MC_FINAL_ADJUDICATION_PACKAGE.txt` | `12` | `TIER_5` | PROVENANCE_ONLY | 7296 | `ffd3d01b3ee528e4921fb051db4a4d68e74b84909dab1c03d0bbb87102d7e774` |
| 203 | `06_TRANSPORT_AND_PROVENANCE/03_Launchers_and_Checklists/Codex_Workflows/CODEX_ORGANIZE_TRUEMOIST_PATENT_RESEARCH_PACKAGE.txt` | `12` | `TIER_5` | PROVENANCE_ONLY | 2885 | `1d052b3127c45236c58479ffe4236cb450dc5df4c18ec4611916ab1ccc08f2cb` |
| 204 | `06_TRANSPORT_AND_PROVENANCE/03_Launchers_and_Checklists/Codex_Workflows/CODEX_ORGANIZE_TRUEMOIST_SYNTHESIS_PACKAGE.txt` | `12` | `TIER_5` | PROVENANCE_ONLY | 9826 | `24aface26630f4269bbf968d468f8c4aa81fbfd95ba16b720256580149b07fe9` |
| 205 | `06_TRANSPORT_AND_PROVENANCE/03_Launchers_and_Checklists/Codex_Workflows/CODEX_ORGANIZE_VIBEGUARD_SYNTHESIS_PACKAGE.txt` | `12` | `TIER_5` | PROVENANCE_ONLY | 8911 | `5d61f81a36f57ea062a8ccfa08588cfc6e91f383e2eaf5a39d9b4983d3530c3d` |
| 206 | `06_TRANSPORT_AND_PROVENANCE/03_Launchers_and_Checklists/Codex_Workflows/CODEX_SESSION_HANDOFF.md` | `12` | `TIER_5` | PROVENANCE_ONLY | 6902 | `9bf1f632571c2d81d09cc3ca847be329fa8f7b6537c4d7bc1d0754b10c08ae5a` |
| 207 | `06_TRANSPORT_AND_PROVENANCE/03_Launchers_and_Checklists/OpenBraille_PreBuild_Launcher_FINAL.txt` | `12` | `TIER_5` | PROVENANCE_ONLY | 1179 | `1792456d381804d8571946b9a06f4608a3beae99e0c0dc03725fd5ae2f19f0e9` |
| 208 | `06_TRANSPORT_AND_PROVENANCE/03_Launchers_and_Checklists/OpenBraille_Synthesis_UPLOAD_CHECKLIST.txt` | `12` | `TIER_5` | PROVENANCE_ONLY | 670 | `46bcdd0075e2152b6f74b83a493adbf423455fd672bb84ffa66fbe15d75c91ee` |
| 209 | `06_TRANSPORT_AND_PROVENANCE/03_Launchers_and_Checklists/Project_mC_Final_Adjudication_Launcher_FINAL.txt` | `12` | `TIER_5` | PROVENANCE_ONLY | 1428 | `a873f8dfb89eebb878e97eca5c1f29f317fbe03da4227df2cc3c1d2e0abdcd3e` |
| 210 | `06_TRANSPORT_AND_PROVENANCE/03_Launchers_and_Checklists/Project_mC_Teacher_Document_Master_Launcher_FINAL.txt` | `12` | `TIER_5` | PROVENANCE_ONLY | 1639 | `be911c0a398943ee46b8be5efa430e6041a3ffc32926d063b24a82b2d0f14fea` |
| 211 | `06_TRANSPORT_AND_PROVENANCE/03_Launchers_and_Checklists/TrueMoist_Patent_Research_Launcher_GEMINI_10.txt` | `12` | `TIER_5` | PROVENANCE_ONLY | 1314 | `26bdadbd0f1761ba8535ec5057f8a73c5dd5f019f16ac9799a9b7b3ccc9ac17e` |
| 212 | `06_TRANSPORT_AND_PROVENANCE/03_Launchers_and_Checklists/TrueMoist_Patent_Research_Launcher_QWEN_5.txt` | `12` | `TIER_5` | PROVENANCE_ONLY | 1693 | `0ff6adf3da6ded4edd99f62931fc73c11aa886b4da730983ed2759912275088b` |
| 213 | `06_TRANSPORT_AND_PROVENANCE/03_Launchers_and_Checklists/TrueMoist_Synthesis_Launcher_FINAL.txt` | `12` | `TIER_5` | PROVENANCE_ONLY | 1990 | `14e318c177f67f94e3d85bb90c8eb14d161825dd058761092936e2f10680221b` |
| 214 | `06_TRANSPORT_AND_PROVENANCE/03_Launchers_and_Checklists/VibeGuard_Patent_Research_Launcher.txt` | `12` | `TIER_5` | PROVENANCE_ONLY | 907 | `39c5bdeeba8af563ee4fff34094816a2ab912cdbeb55ebff80698fef8db69b65` |
| 215 | `06_TRANSPORT_AND_PROVENANCE/03_Launchers_and_Checklists/VibeGuard_Patent_Research_Launcher_10File_Limit.txt` | `12` | `TIER_5` | PROVENANCE_ONLY | 1553 | `e42b1458cbb74020d6f6bf9547403136fe7de2843f4373fd59e650aa8846355f` |
| 216 | `06_TRANSPORT_AND_PROVENANCE/03_Launchers_and_Checklists/VibeGuard_Patent_Research_Launcher_Qwen_5File.txt` | `12` | `TIER_5` | PROVENANCE_ONLY | 1962 | `fc24a963d63cc4970059e0e8fbd3a5cc423c3aa938556f5e048e4f4f18c45ad2` |
| 217 | `06_TRANSPORT_AND_PROVENANCE/03_Launchers_and_Checklists/VibeGuard_PreBuild_Launcher_FINAL.txt` | `12` | `TIER_5` | PROVENANCE_ONLY | 1020 | `d24df0a09d413806a07a6dbc0245d3922a781a71dac7072bc33049a1da1a97c5` |
| 218 | `06_TRANSPORT_AND_PROVENANCE/03_Launchers_and_Checklists/VibeGuard_Synthesis_Launcher_FINAL.txt` | `12` | `TIER_5` | PROVENANCE_ONLY | 1342 | `97e468c15bccf79f0dabc6e4bd4e05f4c592739148bacc2f7c96cb30809f417c` |
| 219 | `06_TRANSPORT_AND_PROVENANCE/04_Reduced_File_Bundles/TrueMoist_Gemini10_04_05_Architecture_and_Memory.md` | `12` | `TIER_5` | PROVENANCE_ONLY | 53651 | `8f8bf0175b9556a93f0694dad6677247ca2b7c6e5b0b58134648977b288f2941` |
| 220 | `06_TRANSPORT_AND_PROVENANCE/04_Reduced_File_Bundles/TrueMoist_Qwen5_01_03_Project_Authority_Bundle.md` | `12` | `TIER_5` | PROVENANCE_ONLY | 92286 | `99b9feb81f6f32a0f78f21bab825ce085c2508c6fa2d7accfd1827cf60ab5fdb` |
| 221 | `06_TRANSPORT_AND_PROVENANCE/04_Reduced_File_Bundles/TrueMoist_Qwen5_04_06_Phase3C_Bundle.md` | `12` | `TIER_5` | PROVENANCE_ONLY | 72837 | `cff6bf8bceeb8a2c18eb197f8fefd9c2813bab270ee76347480f0e11aa00aa97` |
| 222 | `06_TRANSPORT_AND_PROVENANCE/04_Reduced_File_Bundles/TrueMoist_Qwen5_07_09_Validation_and_Patent_Input_Bundle.md` | `12` | `TIER_5` | PROVENANCE_ONLY | 60028 | `a72308a766a105a1c38903daa99cdcc2027addccefa0e2fa98389acee99fee43` |
| 223 | `06_TRANSPORT_AND_PROVENANCE/04_Reduced_File_Bundles/VibeGuard_Gemini10_07_08_Downselection_Evidence_Bundle.md` | `12` | `TIER_5` | PROVENANCE_ONLY | 42869 | `b9d5e3351860d799848ad5fddc7f4d9863eebd2a49bd14832b7057691d30189e` |
| 224 | `06_TRANSPORT_AND_PROVENANCE/04_Reduced_File_Bundles/VibeGuard_Gemini10_Platform_Instructions.md` | `12` | `TIER_5` | PROVENANCE_ONLY | 21068 | `8832a2d20d0d681bf710bbc7a9af53525855efae2c46734c5d29a3a339136b2e` |
| 225 | `06_TRANSPORT_AND_PROVENANCE/04_Reduced_File_Bundles/VibeGuard_Qwen5_01_03_Project_Authority_Bundle.md` | `12` | `TIER_5` | PROVENANCE_ONLY | 91243 | `cd0a0c317929fd8bff94387c1c30959fa34e1dff16a47466dcaf17760572783f` |
| 226 | `06_TRANSPORT_AND_PROVENANCE/04_Reduced_File_Bundles/VibeGuard_Qwen5_04_06_Phase3C_Bundle.md` | `12` | `TIER_5` | PROVENANCE_ONLY | 58692 | `3d26e9e226395e668b0903d2f5c2472af245216ca272ea049d1b9d291369c8e8` |
| 227 | `06_TRANSPORT_AND_PROVENANCE/04_Reduced_File_Bundles/VibeGuard_Qwen5_07_09_Current_Evidence_and_Patent_Input_Bundle.md` | `12` | `TIER_5` | PROVENANCE_ONLY | 58833 | `4d28351626041438292d90684f811ac0a2f32a9783bc82c53250e524163ea184` |
| 228 | `06_TRANSPORT_AND_PROVENANCE/04_Reduced_File_Bundles/VibeGuard_Qwen5_Platform_Instructions.md` | `12` | `TIER_5` | PROVENANCE_ONLY | 21343 | `4d504bc5199db8e56ed8834a12463b60a2c57ee43bb415d97b35c3e8e652c9eb` |
| 229 | `06_TRANSPORT_AND_PROVENANCE/05_Package_Validation/TrueMoist_Limited_Package_Validation.md` | `12` | `TIER_5` | PROVENANCE_ONLY | 12688 | `d9953007efa2ed64f2c98c7e9d5323dda6a9421fa95a5ce663c423a9502982bd` |
| 230 | `06_TRANSPORT_AND_PROVENANCE/TRANSPORT_AND_PROVENANCE_INDEX.md` | `12` | `TIER_5` | PROVENANCE_ONLY | 1213 | `595aa9235231400376724f6732b38c1460b48845c3b93eb55110c114e7d80f06` |
| 231 | `09_ARCHIVE/01_Superseded/Convenience_Folder_Variants/COPY PASTE FOLDER/MC_Project_PHASE_DOC.md` | `13` | `TIER_5` | ARCHIVE_ONLY | 11868 | `c4b6c4a56bf8ba3066c5b426dce5ae4d50da4774478b5074566e9c79812e3ece` |
| 232 | `09_ARCHIVE/01_Superseded/Convenience_Folder_Variants/COPY PASTE FOLDER/Project_mC_Decision_Register_v1.0.md` | `13` | `TIER_5` | ARCHIVE_ONLY | 42548 | `2ecf77fbbba9966a7769a2e715034f6b9ff7362d7aa51261219ee118085d22d3` |
| 233 | `09_ARCHIVE/01_Superseded/Convenience_Folder_Variants/COPY PASTE FOLDER/README.md` | `13` | `TIER_5` | ARCHIVE_ONLY | 423 | `ce43327e164bd6ae2f11d8d68fe7ffa5cbae97cbe5d189f024502a099b21fe7f` |
| 234 | `09_ARCHIVE/01_Superseded/Convenience_Folder_Variants/every sop and memory/MC_Project_PHASE_DOC.md` | `13` | `TIER_5` | ARCHIVE_ONLY | 6638 | `e7ebf127dac01b63c87713b14c0bd5cf2d4500e60581cc86f783abe92a525f98` |
| 235 | `09_ARCHIVE/01_Superseded/Convenience_Folder_Variants/every sop and memory/README.md` | `13` | `TIER_5` | ARCHIVE_ONLY | 477 | `36791bf0406c8639b6fe5eae16d01cff27ce82ff48605d335cb65392276ccfd3` |
| 236 | `09_ARCHIVE/01_Superseded/TrueMoist/Earlier_Claude_Architecture/Phase3C_TrueMoist_Architecture_Report_by_Claude.md` | `13` | `TIER_5` | ARCHIVE_ONLY | 50145 | `e494a9d8bc1894a1d433deceea8b1a7bc9fc0c05ff5591d28f66fca5249c990c` |
| 237 | `09_ARCHIVE/01_Superseded/TrueMoist/Earlier_Claude_Architecture/Phase3C_TrueMoist_MEMORY.md` | `13` | `TIER_5` | ARCHIVE_ONLY | 12967 | `e19bfa953ec27bbbc3c64a142f81df3c71e2a5fd2e5ff9747fb52e8c061f54f2` |
| 238 | `09_ARCHIVE/01_Superseded/TrueMoist/Earlier_Claude_Architecture/Project_mC_Decision_Register_v1_1.md` | `13` | `TIER_5` | ARCHIVE_ONLY | 54060 | `11efb57dac75c36c80f2d27c17c2689dbae645efca821a1d1b5d4574eeeed112` |
| 239 | `09_ARCHIVE/01_Superseded/TrueMoist/Phase3C_TrueMoist_PDR_Patch_Historical.md` | `13` | `TIER_5` | ARCHIVE_ONLY | 10212 | `fd2965c371701c137897cda021885bce46e5b6b0c0d2e14126d6903c7078b3a1` |
| 240 | `09_ARCHIVE/03_Failed_or_Partial_Research/OpenBraille/FAILED_CONCEPT_SWAP_OpenBraille_Deep_Research_Synthesis.md` | `13` | `TIER_5` | ARCHIVE_ONLY | 16083 | `d9b3fce5d7133d2457dd18c1092fb5eaab43f827e4c0eb864462beab1fdfc822` |
| 241 | `09_ARCHIVE/03_Failed_or_Partial_Research/OpenBraille/Phase3C_Failed_Raw_Research/Phase3C_OpenBraille_Failed_Research_ChatGPT.pdf` | `13` | `TIER_5` | ARCHIVE_ONLY | 151219 | `864e400d3b259157346319b53eb36868b28bf183fb6ac5a1efbcbb6315424e06` |
| 242 | `09_ARCHIVE/03_Failed_or_Partial_Research/README.md` | `13` | `TIER_5` | ARCHIVE_ONLY | 576 | `b7e948d80eddb1ad5bec10684b0214691cf3303a92eb1c12d1ceed2efbcb0111` |
| 243 | `09_ARCHIVE/03_Failed_or_Partial_Research/TrueMoist/Legacy_Fragments_and_Variants/research on f.patent by chatgpt high deeprserach.pdf` | `13` | `TIER_5` | ARCHIVE_ONLY | 133836 | `cb5044f5576556b6f8c0bdbf57658597b5531e246e049b5f4ea0da21be49b505` |
| 244 | `09_ARCHIVE/03_Failed_or_Partial_Research/TrueMoist/Legacy_Fragments_and_Variants/research on f.patent by qwen #0.md` | `13` | `TIER_5` | ARCHIVE_ONLY | 45140 | `d8abc8efe8c6a4d5111ecca56d76ca68dd0db142dfb3a54bd48375b05b1b2045` |
| 245 | `09_ARCHIVE/03_Failed_or_Partial_Research/TrueMoist/Legacy_Fragments_and_Variants/reserach.md` | `13` | `TIER_5` | ARCHIVE_ONLY | 14742 | `2e73ec4e1cd5e08d5f5b6628fb5e70986d3591cc5a5916fa580f08b25db638bc` |
| 246 | `09_ARCHIVE/03_Failed_or_Partial_Research/TrueMoist/SUPPLEMENTARY_EXCLUDED_TrueMoist_Work_Max_Web_Audit.md` | `13` | `TIER_5` | ARCHIVE_ONLY | 107541 | `6efe433b5b86b75830b93ad0a32f5a8db703d0a9740c4481ef4cea7db5a89dec` |
| 247 | `09_ARCHIVE/03_Failed_or_Partial_Research/VibeGuard/FAILED_CONCEPT_SWAP_VibeGuard_Deep_Research_Synthesis.md` | `13` | `TIER_5` | ARCHIVE_ONLY | 11762 | `8dd3e9c2a131c77427f8fd8034e6594a0eddb9080cbb6d1e33abfc99b5bc6134` |
| 248 | `09_ARCHIVE/03_Failed_or_Partial_Research/VibeGuard/Legacy_Fragments_and_Variants/research on f. patent by chatgpt.md` | `13` | `TIER_5` | ARCHIVE_ONLY | 10268 | `0bf20103740b63a5627b583932aed4663914713749b3e9b2732592335957dac0` |
| 249 | `09_ARCHIVE/03_Failed_or_Partial_Research/VibeGuard/Legacy_Fragments_and_Variants/research on f.patent by mistral 2.md` | `13` | `TIER_5` | ARCHIVE_ONLY | 22849 | `cb93eee902cc5e0bd6b6699f6d603fc8fc2830fdf27f1d7a54512f5f6c227a82` |
| 250 | `09_ARCHIVE/03_Failed_or_Partial_Research/VibeGuard/Legacy_Fragments_and_Variants/research on f.patent by mistral 3.md` | `13` | `TIER_5` | ARCHIVE_ONLY | 15289 | `b9fbf2c34ac71d90d682de5b77ba1d5bee0fa7f00cb18a8a8d99f292529e8f1b` |
| 251 | `09_ARCHIVE/03_Failed_or_Partial_Research/VibeGuard/Legacy_Fragments_and_Variants/research on f.patent by mistral.pdf` | `13` | `TIER_5` | ARCHIVE_ONLY | 75874 | `9a0a142735a83a7705d2022ca4219d9232a655483028229e94a43e827f05bdaa` |
| 252 | `09_ARCHIVE/03_Failed_or_Partial_Research/VibeGuard/Legacy_Fragments_and_Variants/research on f.patent by qwen.md` | `13` | `TIER_5` | ARCHIVE_ONLY | 29667 | `f5363b5bd6d7373e5ab5270fa2daf7b7f2b30223650a535f6258a36a90c7726c` |
| 253 | `09_ARCHIVE/03_Failed_or_Partial_Research/VibeGuard/Legacy_Fragments_and_Variants/research_on_f.patent_by_qwen2.md` | `13` | `TIER_5` | ARCHIVE_ONLY | 25768 | `9e510aa8188e46f247342f961467320c62a9a0cba256f3eda50f8b9d757fdb82` |
| 254 | `09_ARCHIVE/04_Legacy_Zips/PHASE 1/PHASE 1.B/Phase1B_Opportunity_Analysis.zip` | `13` | `TIER_5` | ARCHIVE_ONLY | 743098 | `67d556082774dd9223e05d99f6b64eac045d7cc52ae9b60c403bc643a8b15dab` |
| 255 | `09_ARCHIVE/04_Legacy_Zips/PHASE 2/Phase2_docs.zip` | `13` | `TIER_5` | ARCHIVE_ONLY | 20668 | `5b4156e64afaf59c1cc8788ae2c02cbebf8e2c003343dd8c56544219f1377fb6` |
| 256 | `09_ARCHIVE/04_Legacy_Zips/PHASE 3/PHASE 3A-Engineering Landscape Discovery/Phase3A_report_and_memory.zip` | `13` | `TIER_5` | ARCHIVE_ONLY | 522853 | `9d0593bb50717c290ca9c36d135ffc1aebfb70a48d2b058be4c8b421af44ae21` |
| 257 | `09_ARCHIVE/04_Legacy_Zips/PHASE 3/PHASE 3B-Engineering Feasibility Analysis/Phase3B_mem_and_report.zip` | `13` | `TIER_5` | ARCHIVE_ONLY | 35058 | `b4674075c434e818a3579f61f8746dd918ac06e316030e04fa3c9577a36eafb0` |
| 258 | `09_ARCHIVE/04_Legacy_Zips/PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/files.zip` | `13` | `TIER_5` | ARCHIVE_ONLY | 36572 | `26058ea1e362dbd70abb8ac5fdcdc9177bd2b64ee30a5c22e1d47b4fdb30d251` |
| 259 | `09_ARCHIVE/04_Legacy_Zips/contexts.zip` | `13` | `TIER_5` | ARCHIVE_ONLY | 3583134 | `29c21e888bc2ac1fb42514db91bff88a6a67bafde26a05ddc6933010ba3233f6` |
| 260 | `09_ARCHIVE/04_Legacy_Zips/every sop and memory/every_sop_and memory_from phase 1A to 1C and whoel phase overview.zip` | `13` | `TIER_5` | ARCHIVE_ONLY | 19018 | `cdc5acdda096d42498ba49d4bec9451e1cb8cfa5251d295a0412d0e4d9a83668` |
| 261 | `09_ARCHIVE/05_Unrelated_Quarantine/INTENTIONAL_EXCLUSIONS.md` | `13` | `TIER_5` | ARCHIVE_ONLY | 743 | `908a34152f9bd09e1dbf951169f5f452432aaa0bd416d80efe91713c2cf536ce` |
| 262 | `09_ARCHIVE/ARCHIVE_INDEX.md` | `13` | `TIER_5` | ARCHIVE_ONLY | 783 | `ce262a6250572344c465064cf47217b7d539d919c230f3048459d2a4683cae98` |
| 263 | `00_START_HERE/01_STAGE1_GOVERNANCE_COPY_LOG.tsv` | `14` | `TIER_5` | AUDIT_APPENDIX | 3923 | `0cba6a406e9091e6e9ba4ca01f9c0059e62e42473d953df09ee644f20907bf35` |
| 264 | `00_START_HERE/01_STAGE1_GOVERNANCE_VALIDATION.md` | `14` | `TIER_5` | AUDIT_APPENDIX | 5073 | `7be9b6558728c51a8982e30e0e224ad0c7d15fc4be51dfbcea910b45b38121cc` |
| 265 | `00_START_HERE/02_STAGE2_PHASE_HISTORY_COPY_LOG.tsv` | `14` | `TIER_5` | AUDIT_APPENDIX | 10892 | `7df9c1ba0a0ec804f95ec69125a3f9d15105962755fa5aed4b3470b7e2cefaea` |
| 266 | `00_START_HERE/02_STAGE2_PHASE_HISTORY_VALIDATION.md` | `14` | `TIER_5` | AUDIT_APPENDIX | 12653 | `0fe6ba5ac5a1f83278237bc90d3e1b2794c104e0b10bb89526e73626266726d2` |
| 267 | `00_START_HERE/03_STAGE3A_CONCEPT_ARCHITECTURE_COPY_LOG.tsv` | `14` | `TIER_5` | AUDIT_APPENDIX | 7101 | `7959486d4b6834d947e5b2e1d446205e64daa2e37d3556f86c648a072aae7c34` |
| 268 | `00_START_HERE/03_STAGE3A_CONCEPT_ARCHITECTURE_VALIDATION.md` | `14` | `TIER_5` | AUDIT_APPENDIX | 8905 | `d8eb2ac7d5d6749619b869488beb08aecb51eb921f03709cf0c4a7362013c98f` |
| 269 | `00_START_HERE/04_STAGE3B_PATENT_EVIDENCE_COPY_LOG.tsv` | `14` | `TIER_5` | AUDIT_APPENDIX | 14154 | `93e2a900eb1ddf9ea25fb63d0d64c1cc3efb319f2a1f9349fa7be65f1f3cdc0f` |
| 270 | `00_START_HERE/04_STAGE3B_PATENT_EVIDENCE_VALIDATION.md` | `14` | `TIER_5` | AUDIT_APPENDIX | 16807 | `541c275782505f13c66713a86248368ae26d7d31fd215330fb28c7ca3558700f` |
| 271 | `00_START_HERE/05_STAGE4A_COMPARATIVE_DECISION_COPY_LOG.tsv` | `14` | `TIER_5` | AUDIT_APPENDIX | 7839 | `df05d4e0908ba84bc362ddf7911806237286a4248ec605df98906ebf5e5f9209` |
| 272 | `00_START_HERE/05_STAGE4A_COMPARATIVE_DECISION_VALIDATION.md` | `14` | `TIER_5` | AUDIT_APPENDIX | 9767 | `80f2e3c7c9208d11248f85024af60bcd47a97d8a0c7af4e195df6e3e09b6f885` |
| 273 | `00_START_HERE/06_STAGE4B_TEACHER_AND_REVIEW_COPY_LOG.tsv` | `14` | `TIER_5` | AUDIT_APPENDIX | 6625 | `7428ae6eb3851002ba3549d3b7dcf471fa5e3e81856255d6092e4fd9f0d4279c` |
| 274 | `00_START_HERE/06_STAGE4B_TEACHER_AND_REVIEW_VALIDATION.md` | `14` | `TIER_5` | AUDIT_APPENDIX | 8418 | `6781d37ac5513bc5d14095ecde86147376ae2d02ac6e51dff3c90a1bc228a99a` |
| 275 | `00_START_HERE/07_STAGE5_TRANSPORT_PROVENANCE_COPY_LOG.tsv` | `14` | `TIER_5` | AUDIT_APPENDIX | 20324 | `b47c0bb955de979aa0658ff330b15fd332445714671a9838232fff81a8fb6f2f` |
| 276 | `00_START_HERE/07_STAGE5_TRANSPORT_PROVENANCE_VALIDATION.md` | `14` | `TIER_5` | AUDIT_APPENDIX | 23989 | `417bf666f3d6346b0afc2e49a4a71052614a6adadc80f282f90673e20ff77c89` |
| 277 | `00_START_HERE/08_STAGE6A_HISTORICAL_RESEARCH_COPY_LOG.tsv` | `14` | `TIER_5` | AUDIT_APPENDIX | 13879 | `e723fe87f63f5f4fc503d23dcab38953d47e1d34bdf2b7c0e4c928f221f9d864` |
| 278 | `00_START_HERE/08_STAGE6A_HISTORICAL_RESEARCH_VALIDATION.md` | `14` | `TIER_5` | AUDIT_APPENDIX | 16522 | `8fa5419bf7dabdf4d90e29e472638445c516797787134dcdeabeda129fcfc834` |
| 279 | `00_START_HERE/09_STAGE8_FINAL_ARCHIVAL_SWEEP_LOG.tsv` | `14` | `TIER_5` | AUDIT_APPENDIX | 49319 | `78a48b5517f456d15321ca004227a0d67c293b020e1694da335f8278d71e9bf7` |
| 280 | `00_START_HERE/09_STAGE8_FINAL_ARCHIVAL_SWEEP_VALIDATION.md` | `14` | `TIER_5` | AUDIT_APPENDIX | 1516 | `deb56e43a0fe430f14778899d729d4a837f7f526b75fd72d865008cb2a83acc4` |
| 281 | `08_MASTER_MANUAL/01_Source_Index/MASTER_MANUAL_SOURCE_POLICY.md` | `14` | `TIER_1` | CORE_SOURCE_CONTROL | 1521 | `c5433b5d33523548bcd92d3c8628eb0eb7c902daaa19d70df377368d4d82cdc4` |
| 282 | `08_MASTER_MANUAL/01_Source_Index/SOURCE_FREEZE_NOTICE.md` | `14` | `TIER_1` | CORE_SOURCE_CONTROL | 988 | `1b8a3cf0efb1849091a2913e96bad2578e9b122e576ba8fe6f9279e294132743` |
| 283 | `05_TEACHER_AND_REVIEWS/03_Other_Groups/Presentations/10_Fake WiFi access point detection system using ESP32 .pptx` | `A2` | `REFERENCE_ONLY` | REFERENCE_ONLY | 306334 | `81aa854072ec46025b63c89e39c67daf86211f0d9d46473de23ff508d4df63ef` |
| 284 | `05_TEACHER_AND_REVIEWS/03_Other_Groups/Presentations/11_ENVIRONMENTAL TAMPER DETECTION FOR SERVER RACK.pptx` | `A2` | `REFERENCE_ONLY` | REFERENCE_ONLY | 361861 | `f6e57856034b766b2c73c178f38815c329ac22f37ca6a169c0837d7a5f2fd9c9` |
| 285 | `05_TEACHER_AND_REVIEWS/03_Other_Groups/Presentations/12_STM32 Smart Attendance Register Using RFID.pptx` | `A2` | `REFERENCE_ONLY` | REFERENCE_ONLY | 318111 | `0b6f29b594547892b7b5203e407d6bf1bf44645fa1ab609e5dd32126263b2ebe` |
| 286 | `05_TEACHER_AND_REVIEWS/03_Other_Groups/Presentations/13_Secure Confidential Document Storage Box with__Tamper Detection using Arduino Uno.pptx` | `A2` | `REFERENCE_ONLY` | REFERENCE_ONLY | 461605 | `578d7445a628d8042af51e50b8817a6577540b9c880025cd5ab091626145d242` |
| 287 | `05_TEACHER_AND_REVIEWS/03_Other_Groups/Presentations/1_Secure Electronic Voting Machine with Voter Authentication, Encrypted Vote Storage, and Tamper Detection.pptx` | `A2` | `REFERENCE_ONLY` | REFERENCE_ONLY | 312874 | `9636003a782e9e93a243e8ccbdab78ff6e4a01ab20180d1f30f35fb06fa697f2` |
| 288 | `05_TEACHER_AND_REVIEWS/03_Other_Groups/Presentations/2_Biometric Continuous Authentication System.pptx` | `A2` | `REFERENCE_ONLY` | REFERENCE_ONLY | 352275 | `d3b4da9c96003d9299af6b8de67679a21e3e93cdeffec58a5051aa488d52a1de` |
| 289 | `05_TEACHER_AND_REVIEWS/03_Other_Groups/Presentations/3_Distributed IoT Security System for Covert Tracker Detection .pptx` | `A2` | `REFERENCE_ONLY` | REFERENCE_ONLY | 1495407 | `0f06bbd32a9eec061a6fac86c878fd09b627fe431c6773767cadf3bf2c159f53` |
| 290 | `05_TEACHER_AND_REVIEWS/03_Other_Groups/Presentations/4_Smart Examination Hall Mobile Activity Detection and Alert System using STM32.pptx` | `A2` | `REFERENCE_ONLY` | REFERENCE_ONLY | 348228 | `eaba2dcdd566fde6d23b216cba4d407be2c3314e0a9b16e25267b1bbce6999a5` |
| 291 | `05_TEACHER_AND_REVIEWS/03_Other_Groups/Presentations/5_Juice Jacking USB using ESP32.pptx` | `A2` | `REFERENCE_ONLY` | REFERENCE_ONLY | 836202 | `b3f6413167035b5e336925f4658ff1b3b531cfba1b0d87223e0b4eb4d87b9d83` |
| 292 | `05_TEACHER_AND_REVIEWS/03_Other_Groups/Presentations/6_Zeroth review - Presentation-2 (1).pptx` | `A2` | `REFERENCE_ONLY` | REFERENCE_ONLY | 1587449 | `4c718c7e8ffb727fd4e0c2076c341fdabaedcc5728ed9c4753e5f0b109f03e4b` |
| 293 | `05_TEACHER_AND_REVIEWS/03_Other_Groups/Presentations/7_ USB ATTACK DETECTION AND AUTO ISOLATION SYSTEM .pptx` | `A2` | `REFERENCE_ONLY` | REFERENCE_ONLY | 971124 | `a3b9d64d1cd0cb5338c9bdc433290f1af2554226524daa743433e87d1a28a3a2` |
| 294 | `05_TEACHER_AND_REVIEWS/03_Other_Groups/Presentations/9_Air Gapped Hardware token for compromise resilent  multi factor authentication.pptx` | `A2` | `REFERENCE_ONLY` | REFERENCE_ONLY | 409218 | `5c95535ed29b08b67690bdedc672cc4ac252772151653f2c19b262cb60df304e` |
| 295 | `05_TEACHER_AND_REVIEWS/03_Other_Groups/Presentations/GROUP 4 .pptx` | `A2` | `REFERENCE_ONLY` | REFERENCE_ONLY | 348131 | `9ec7f4fecc5cbf1bf9e4551e2a74e0f483e9bc9ebadd0a7cc50b898a9a871c82` |
| 296 | `05_TEACHER_AND_REVIEWS/03_Other_Groups/Reference_Documents/POOJA PROJECT.pdf` | `A2` | `REFERENCE_ONLY` | REFERENCE_ONLY | 98813 | `70a6446354f634cd7501e883e954bcba8f292a6bb91d406713d30c72b9be977d` |
| 297 | `05_TEACHER_AND_REVIEWS/03_Other_Groups/Reference_Documents/Patent Potential of Student Projects.docx` | `A2` | `REFERENCE_ONLY` | REFERENCE_ONLY | 2998348 | `2156803ab9ac9a253fc6e8860c7788d9891af782fcd52e7a9c64249115cf0273` |
| 298 | `05_TEACHER_AND_REVIEWS/03_Other_Groups/Reference_Documents/USB_Powered_Secure_File_Transfer_Authentication_Abstract.pdf` | `A2` | `REFERENCE_ONLY` | REFERENCE_ONLY | 2399 | `ce5b8e3c904a82066e0718abc0e49c6583c5ec37022cc8d4e59cdefb202c526e` |
| 299 | `05_TEACHER_AND_REVIEWS/03_Other_Groups/Reference_Documents/USB_Powered_Smart_Anti_Theft_System_Abstract.pdf` | `A2` | `REFERENCE_ONLY` | REFERENCE_ONLY | 2424 | `6d5a03b4afbec01258f767ae31c592653ce6e5da09a29c62b5e8ec4841e5c5b3` |
| 300 | `05_TEACHER_AND_REVIEWS/03_Other_Groups/Reference_Documents/USB_Powered_Smart_Cabinet_Abstract.pdf` | `A2` | `REFERENCE_ONLY` | REFERENCE_ONLY | 2553 | `97d240350257e89ad533ef3067c7bf41e18362e01f1d43823eb73e68f9049d17` |
| 301 | `03_CONCEPT_PORTFOLIO/CONCEPT_PORTFOLIO_INDEX.md` | `UNSPECIFIED` | `UNSPECIFIED` | UNSPECIFIED | 1546 | `ea78020d45479fdefd6d2aba4c5825bf50199d5b2357a29bf6c0323bf6c5c2b0` |

## A1.4 Separately controlled unmapped-file register

The following register is preserved separately and is not silently merged into the frozen 301-record source map.

| No. | relative_path | size_bytes | sha256 | mapping_note |
|---:|---|---|---|---|
| 1 | 03_CONCEPT_PORTFOLIO/CONCEPT_PORTFOLIO_INDEX.md | 1546 | ea78020d45479fdefd6d2aba4c5825bf50199d5b2357a29bf6c0323bf6c5c2b0 | No chapter rule matched this path. |

## A1.5 Register limitations

- A matching hash proves byte identity, not technical truth.
- A mapped source is not automatically authoritative.
- Source count does not function as a model vote.
- Chapter assignment does not prove exhaustive semantic coverage.
- Post-freeze appendices do not rewrite the frozen project history.
- Current external facts require later dated verification.

<!-- END CONTROLLED COMPONENT: APPENDIX_A1 -->

---

<!-- BEGIN CONTROLLED COMPONENT: APPENDIX_A2 -->
<!-- SOURCE PATH: /home/paradoxpete/Documents/PROJECT_ORGANIZED/08_MASTER_MANUAL/09_Appendices_Workspace/Appendix_A2_Peer_Project_and_Reference_Register.md -->
<!-- SOURCE SHA-256: 0c7b9e6930b4e745052507b8d00d72f062bf2f9c7bd73637ce0d5e9b40b84099 -->

# Appendix A2 — Peer Project and Reference Register

## A2.1 Control statement

The entries below are the eighteen records mapped to Appendix A2 by the frozen source map. They are reference-only unless a higher controlling source assigns a different role. They do not vote on concept selection, prove novelty, establish approval or override Project mC architecture.

- Appendix A2 mapped records: **18**

## A2.2 Reference register

| No. | Original organized-workspace path | Authority tier | Manual treatment | Size bytes | SHA-256 |
|---:|---|---|---|---:|---|
| 1 | `05_TEACHER_AND_REVIEWS/03_Other_Groups/Presentations/10_Fake WiFi access point detection system using ESP32 .pptx` | `REFERENCE_ONLY` | REFERENCE_ONLY | 306334 | `81aa854072ec46025b63c89e39c67daf86211f0d9d46473de23ff508d4df63ef` |
| 2 | `05_TEACHER_AND_REVIEWS/03_Other_Groups/Presentations/11_ENVIRONMENTAL TAMPER DETECTION FOR SERVER RACK.pptx` | `REFERENCE_ONLY` | REFERENCE_ONLY | 361861 | `f6e57856034b766b2c73c178f38815c329ac22f37ca6a169c0837d7a5f2fd9c9` |
| 3 | `05_TEACHER_AND_REVIEWS/03_Other_Groups/Presentations/12_STM32 Smart Attendance Register Using RFID.pptx` | `REFERENCE_ONLY` | REFERENCE_ONLY | 318111 | `0b6f29b594547892b7b5203e407d6bf1bf44645fa1ab609e5dd32126263b2ebe` |
| 4 | `05_TEACHER_AND_REVIEWS/03_Other_Groups/Presentations/13_Secure Confidential Document Storage Box with__Tamper Detection using Arduino Uno.pptx` | `REFERENCE_ONLY` | REFERENCE_ONLY | 461605 | `578d7445a628d8042af51e50b8817a6577540b9c880025cd5ab091626145d242` |
| 5 | `05_TEACHER_AND_REVIEWS/03_Other_Groups/Presentations/1_Secure Electronic Voting Machine with Voter Authentication, Encrypted Vote Storage, and Tamper Detection.pptx` | `REFERENCE_ONLY` | REFERENCE_ONLY | 312874 | `9636003a782e9e93a243e8ccbdab78ff6e4a01ab20180d1f30f35fb06fa697f2` |
| 6 | `05_TEACHER_AND_REVIEWS/03_Other_Groups/Presentations/2_Biometric Continuous Authentication System.pptx` | `REFERENCE_ONLY` | REFERENCE_ONLY | 352275 | `d3b4da9c96003d9299af6b8de67679a21e3e93cdeffec58a5051aa488d52a1de` |
| 7 | `05_TEACHER_AND_REVIEWS/03_Other_Groups/Presentations/3_Distributed IoT Security System for Covert Tracker Detection .pptx` | `REFERENCE_ONLY` | REFERENCE_ONLY | 1495407 | `0f06bbd32a9eec061a6fac86c878fd09b627fe431c6773767cadf3bf2c159f53` |
| 8 | `05_TEACHER_AND_REVIEWS/03_Other_Groups/Presentations/4_Smart Examination Hall Mobile Activity Detection and Alert System using STM32.pptx` | `REFERENCE_ONLY` | REFERENCE_ONLY | 348228 | `eaba2dcdd566fde6d23b216cba4d407be2c3314e0a9b16e25267b1bbce6999a5` |
| 9 | `05_TEACHER_AND_REVIEWS/03_Other_Groups/Presentations/5_Juice Jacking USB using ESP32.pptx` | `REFERENCE_ONLY` | REFERENCE_ONLY | 836202 | `b3f6413167035b5e336925f4658ff1b3b531cfba1b0d87223e0b4eb4d87b9d83` |
| 10 | `05_TEACHER_AND_REVIEWS/03_Other_Groups/Presentations/6_Zeroth review - Presentation-2 (1).pptx` | `REFERENCE_ONLY` | REFERENCE_ONLY | 1587449 | `4c718c7e8ffb727fd4e0c2076c341fdabaedcc5728ed9c4753e5f0b109f03e4b` |
| 11 | `05_TEACHER_AND_REVIEWS/03_Other_Groups/Presentations/7_ USB ATTACK DETECTION AND AUTO ISOLATION SYSTEM .pptx` | `REFERENCE_ONLY` | REFERENCE_ONLY | 971124 | `a3b9d64d1cd0cb5338c9bdc433290f1af2554226524daa743433e87d1a28a3a2` |
| 12 | `05_TEACHER_AND_REVIEWS/03_Other_Groups/Presentations/9_Air Gapped Hardware token for compromise resilent  multi factor authentication.pptx` | `REFERENCE_ONLY` | REFERENCE_ONLY | 409218 | `5c95535ed29b08b67690bdedc672cc4ac252772151653f2c19b262cb60df304e` |
| 13 | `05_TEACHER_AND_REVIEWS/03_Other_Groups/Presentations/GROUP 4 .pptx` | `REFERENCE_ONLY` | REFERENCE_ONLY | 348131 | `9ec7f4fecc5cbf1bf9e4551e2a74e0f483e9bc9ebadd0a7cc50b898a9a871c82` |
| 14 | `05_TEACHER_AND_REVIEWS/03_Other_Groups/Reference_Documents/POOJA PROJECT.pdf` | `REFERENCE_ONLY` | REFERENCE_ONLY | 98813 | `70a6446354f634cd7501e883e954bcba8f292a6bb91d406713d30c72b9be977d` |
| 15 | `05_TEACHER_AND_REVIEWS/03_Other_Groups/Reference_Documents/Patent Potential of Student Projects.docx` | `REFERENCE_ONLY` | REFERENCE_ONLY | 2998348 | `2156803ab9ac9a253fc6e8860c7788d9891af782fcd52e7a9c64249115cf0273` |
| 16 | `05_TEACHER_AND_REVIEWS/03_Other_Groups/Reference_Documents/USB_Powered_Secure_File_Transfer_Authentication_Abstract.pdf` | `REFERENCE_ONLY` | REFERENCE_ONLY | 2399 | `ce5b8e3c904a82066e0718abc0e49c6583c5ec37022cc8d4e59cdefb202c526e` |
| 17 | `05_TEACHER_AND_REVIEWS/03_Other_Groups/Reference_Documents/USB_Powered_Smart_Anti_Theft_System_Abstract.pdf` | `REFERENCE_ONLY` | REFERENCE_ONLY | 2424 | `6d5a03b4afbec01258f767ae31c592653ce6e5da09a29c62b5e8ec4841e5c5b3` |
| 18 | `05_TEACHER_AND_REVIEWS/03_Other_Groups/Reference_Documents/USB_Powered_Smart_Cabinet_Abstract.pdf` | `REFERENCE_ONLY` | REFERENCE_ONLY | 2553 | `97d240350257e89ad533ef3067c7bf41e18362e01f1d43823eb73e68f9049d17` |

## A2.3 Use limitations

- Peer and reference records provide context, examples or comparison.
- They are not Project mC authority records.
- Their presence does not establish technical equivalence.
- They must not be counted as independent validation of a Project mC claim.
- Current external facts require later verification from primary sources.

<!-- END CONTROLLED COMPONENT: APPENDIX_A2 -->

---

<!-- BEGIN CONTROLLED COMPONENT: APPENDICES_A3_A4_RELEASE_CORRECTED -->
<!-- SOURCE PATH: /home/paradoxpete/Documents/PROJECT_ORGANIZED/08_MASTER_MANUAL/10_Final_Assembly_Workspace/01_Corrected_Release_Candidate/01_Corrected_Components/Project_mC_Master_Manual_Appendices_A3_Glossary_and_A4_Open_Decisions_Change_Log_RELEASE_CORRECTED.md -->
<!-- SOURCE SHA-256: 0cf799c03a01703a78bcb8c0a747a61f02169d3b7d15317a3c96e3989153d610 -->

## Appendices A3 and A4

## Document control

| Field | Value |
|---|---|
| Document | Project mC Master Manual — Appendices A3 and A4 |
| Controlled filename | `Project_mC_Master_Manual_Appendices_A3_Glossary_and_A4_Open_Decisions_Change_Log.md` |
| Status | Controlled draft |
| Scope | Glossary, consolidated open decisions and major controlled change log |
| Input control | Exactly 13 physical Markdown attachments were present and readable; all externally hash-controlled files matched the manifest byte counts and SHA-256 values; the self-referential manifest was used only for file control |
| Source boundary | Only the attached governing controls, validated Parts I–VI, mechanically generated Appendices A1–A2, required template and manifest were used |
| Technical effect | Does not amend validated Parts I–VI or any frozen concept architecture |
| Approval effect | Does not approve a concept, platform, Phase 4, procurement, safety plan or validation protocol |
| Patent effect | No patentability, filing, infringement, novelty, inventive-step or freedom-to-operate conclusion |
| External verification | Not performed; current prices, specifications, standards, legal status, facilities and physical performance remain unverified |
| Relationship to A1/A2 | Appendices A1 and A2 are mechanically generated and are not rewritten here |

# Appendix A3 — Glossary and Acronyms

## A3.1 Purpose and use

This glossary provides controlled reading definitions for terms materially used across the Project mC Master Manual. It is interpretive support, not a substitute for the controlling chapter, architecture lock, decision register, test protocol or source ledger. Where a term has a general technical meaning, the definition below states the narrower Project mC use. Definitions do not convert proposed targets into measured results, recommendations into approvals, or future research hypotheses into implemented features.

## A3.2 Project governance and lifecycle terms

| Term | Expansion | Project mC meaning | Scope or caution | Principal location |
|---|---|---|---|---|
| Authority hierarchy | — | Ordered rule for resolving disagreement among teacher records, Decision Register v1.2, final architectures, memories/SOPs, comparative evidence, syntheses, research lanes and historical/archive material. | A lower source cannot silently override a higher source. | Part I, Chapter 01; Part VI, Chapter 14 |
| Authority tiers | TIER_1–TIER_5 | Source classes descending from current governance/architecture authority through decision support, research, historical material and procedural/archive controls. | Lower tiers cannot override higher ones; TIER_5 proves procedure or identity only. | Parts I and VI |
| Decision Register v1.2 | Project mC Decision Register version 1.2 | Canonical project decision record for current documented controls, including portfolio, architecture and governance decisions. | Versions 1.0 and 1.1 are historical or superseded and cannot override v1.2. | Part I, Chapter 01; Part VI, Chapter 13 |
| PDR | Project Decision Record | Identifier used for individual recorded decisions within the Decision Register. | A PDR controls only the decision it actually records. | Part I, Chapter 01 |
| REFERENCE_ONLY | Reference-only authority class | Peer or class-project material retained for contextual comparison. | Does not vote on concept selection or override Project mC architecture. | Appendix A2 |
| Frozen architecture | — | The one authoritative Phase 3C architecture selected for a retained concept. | May receive allowed refinements, but replacement requires formal change control. | Parts II–IV |
| Architecture lock | — | Explicit boundary stating what a frozen concept is and is not. | Prevents concept swaps, hybrids and later patent hypotheses from being backfilled into the semester MVP. | Parts II–IV |
| Semester MVP | Minimum Viable Prototype | Bounded student implementation used to demonstrate the frozen concept’s ordinary engineering objective. | A successful MVP does not prove novelty, patentability, product readiness or later research mechanisms. | Parts I–V |
| Discovery and analysis phases | Phases 1A, 1B and 1B.5 | Progression from problem discovery to clustering/ranking and practical portfolio gates. | Historical 22 survivors were corrected to 16 valid Phase 1C inputs. | Part I, Chapter 02 |
| Concept and landscape phases | Phases 1C and 2 | Creation of one high-level concept per valid survivor followed by historical patent-landscape work. | Broad names and early patent impressions do not define current architecture or legal status. | Part I, Chapter 02 |
| Engineering and architecture phases | Phase 3A, EDR, Phase 3B and Phase 3C | Engineering landscape, hypothesis stabilization, feasibility assessment and one frozen architecture for each retained concept. | Phase 3C is complete for OpenBraille, VibeGuard and TrueMoist only. | Part I, Chapter 02 |
| Phase 4 | Implementation phase | Future project-wide execution stage covering authorized procurement, build, integration and evidence generation. | Not proved started in the attached record. | Parts I and V |
| Hard gate | — | Predefined pass/fail decision point requiring named evidence before a branch may advance. | A failed gate requires iteration, narrowing, closure or change control—not hidden substitution. | Parts I–V |
| Kill criterion | — | Pre-registered condition requiring a hypothesis, mechanism or route to stop or be redesigned. | Prevents post-hoc preservation of an unsupported patent or performance narrative. | Parts II–V |
| Change control | — | Logged process for revising architecture, source mapping, approval state, tests, BOM or release material while preserving the prior state. | Canonical files and frozen maps must not be silently overwritten. | Parts V and VI |
| Teacher approval | — | Explicit recorded acceptance, conditional acceptance or rejection by the teacher or course authority. | A deck, request, roadmap or adjudication is not approval. | Parts I and V |
| Course-platform acceptance | — | Explicit authorization of the exact board/toolchain or an approved controlled substitution. | ESP32-class architectures exist, but final ESP32/STM32 acceptance remains unresolved. | Parts I and V |
| Chapter 11 zero-source boundary | — | Record that Chapter 11 has zero directly mapped execution sources and is therefore a future framework. | It does not prove procurement, coding, fabrication, testing or completion. | Part V, Chapter 11; Part VI, Chapter 14 |
| BOM | Bill of Materials | Controlled list of exact parts, quantities, specifications, suppliers and cost assumptions for an authorized build. | Historical BOMs are planning evidence; procurement requires current verification and approval. | Parts II–V |
| Configuration ID | Configuration Identifier | Versioned identifier linking hardware, firmware, CAD, calibration, wiring, rig and test records. | Unversioned evidence cannot support final acceptance claims. | Parts II–V |

## A3.3 OpenBraille terms

| Term | Expansion | Project mC meaning | Scope or caution | Principal location |
|---|---|---|---|---|
| OpenBraille | — | Retained accessibility/mechatronics concept: one non-standard macro six-dot tactile cell using six servo/cam/pin channels and ESP32 control. | Not an ISO-compliant cell, commercial display, fluent-reading device or approved build. | Part II, Chapter 04 |
| Macro six-dot cell | — | Enlarged permanent six-dot educational tactile cell selected to reduce fabrication risk. | Macro scale does not establish practical Braille pitch, product density or user readiness. | Part II, Chapter 04 |
| SG90-class servo | — | Commodity micro-servo class used as one actuator per tactile dot. | Seller label, commanded angle or current spike does not prove torque, endpoint or tactile state. | Part II, Chapter 04 |
| Eccentric cam/follower | — | Mechanical conversion channel that translates servo rotation into guided vertical pin motion. | Geometry, friction, coupling, wear and return require physical testing. | Part II, Chapter 04 |
| Guided tactile pin | — | Rounded vertical pin constrained by a guide to represent a raised or lowered dot. | Physical state must be established by external measurement during calibration and validation. | Part II, Chapter 04 |
| Active retraction | — | Deliberate servo-and-cam command that drives a dot to its lowered state. | Controlling fallback because passive return is unproved. | Part II, Chapter 04 |
| Single-dot-first commissioning | — | Mandatory one-channel coupon build and validation before six-dot integration. | Prevents replication of the same mechanical, power or calibration defect across six channels. | Part II, Chapter 04 |
| Physical-state oracle | — | Independent displacement, force or equivalent ground truth used to determine actual pin state. | Servo angle, elapsed time and current alone are insufficient. | Part II, Chapters 04–05 |
| D11 | — | Separate post-MVP hypothesis for mechanically referenced, individually calibrated, sensor-minimal tactile-state verification and bounded recovery. | Current/voltage may support diagnosis but never certify tactile state; D11 is not part of the frozen MVP. | Part II, Chapter 05 |
| VPD-C7 | Verified Pin-Datum Cell | Separate guide/pin/datum coupon hypothesis in which a pin-side datum may also provide low-energy endpoint evidence. | Must remain separate from D11 and the semester cell; no built or validated C7 result exists. | Part II, Chapter 05 |

## A3.4 VibeGuard terms

| Term | Expansion | Project mC meaning | Scope or caution | Principal location |
|---|---|---|---|---|
| VibeGuard | — | Retained industrial-monitoring concept using one rigid ADXL345-class sensor, an ESP32, local features, RMS/persistence, supporting FFT, RGB and USB evidence on a controlled rig. | Strongest semester-build recommendation, but not proved teacher-approved. | Part III, Chapter 06; Part I, Chapter 09 |
| ADXL345-class | — | Low-cost tri-axis accelerometer class used as the permanent target-mounted vibration sensor. | Exact purchased module, authenticity, range, bandwidth and mounting require verification. | Part III, Chapter 06 |
| SPI | Serial Peripheral Interface | Digital bus used for accelerometer acquisition in the frozen VibeGuard architecture. | Achieved sampling and data integrity must be measured on the exact configuration. | Part III, Chapter 06 |
| RMS | Root Mean Square | Mandatory minimum time-domain vibration magnitude feature used against a calibrated baseline. | Threshold values and session structure remain to be pre-registered. | Part III, Chapter 06 |
| Persistence | — | Requirement that an abnormal condition continue across a defined duration or number of windows before alerting. | Reduces transient false alerts; exact values are not yet approved. | Part III, Chapter 06 |
| FFT | Fast Fourier Transform | Supporting frequency-domain analysis triggered or scheduled to explain and compare vibration changes. | It is supporting evidence, not automatic bearing diagnosis or a patent mechanism. | Part III, Chapter 06 |
| Mahalanobis comparator | — | Optional ordinary multivariate distance comparison against a normal baseline. | Added only after acquisition integrity and basic baseline gates pass; drop if unstable or non-incremental. | Part III, Chapter 06 |
| Level 1 | — | Semester scope: controlled normal-versus-induced-abnormal detection on a bounded rig. | Does not establish diagnosis, source attribution or dense-machine operation. | Part III, Chapter 06 |
| Level 2 | — | Later research scope involving target attribution, interference, remounting, transfer and protected updating. | Level-1 success is a prerequisite, not proof of Level-2 observability. | Part III, Chapter 07 |
| Target attribution | — | Determining whether a detected change originates in the monitored target rather than an interferer, load, mount or structure. | A one-sensor anomaly detector may detect change without identifying the source. | Part III, Chapter 07 |
| Non-identifiability | — | Condition in which target and interferer effects cannot be separated reliably from the available one-sensor observations. | A legitimate negative result; must not trigger a silent sensor-array or concept substitution. | Part III, Chapter 07 |
| Paired intervention contrast | — | Narrowed future test comparing target-change and interference-change structures while the other factor is held fixed. | Requires independent labels, controlled interventions and blocked held-out evaluation. | Part III, Chapter 07 |
| Abstention / Unknown | — | Explicit future output used when attribution is ambiguous, out of support or mount-invalid. | Valuable only if wrong-source error falls while useful decision coverage remains. | Part III, Chapter 07 |
| Remount invalidation | — | Default rule that a model becomes invalid after an unvalidated sensor remount and requires recommissioning. | Transfer across mounts is a separate hypothesis, not an established feature. | Part III, Chapter 07 |

## A3.5 TrueMoist terms

| Term | Expansion | Project mC meaning | Scope or caution | Principal location |
|---|---|---|---|---|
| TrueMoist | — | Retained one-soil measurement concept using analog moisture response, nearby temperature, known treatment metadata, fixed local compensation and gravimetric reference. | Not a live-EC meter, irrigation controller, universal model, online learner or approved build. | Part IV, Chapter 08 |
| Analog capacitive probe | — | Low-cost soil-moisture probe whose analog response is used by both uncompensated and compensated models. | Authenticity, coating, monotonicity, insertion repeatability and unit variation require testing. | Part IV, Chapter 08 |
| DS18B20 | — | Nearby waterproof digital temperature sensor used to measure soil temperature at controlled depth and spacing. | Ambient temperature is not a substitute; temperature input does not itself prove compensation. | Part IV, Chapter 08 |
| S0 / S1 | Salinity-treatment states 0 and 1 | Prepared-batch metadata: S0 has no deliberately added salt; S1 has one pilot-selected recorded NaCl dose. | Metadata only; not live electrical conductivity or autonomous salinity estimation. | Part IV, Chapter 08 |
| ADS1115 | — | Primary external analog-to-digital acquisition design for the probe node. | Must be compared on the same node against calibrated ESP32 ADC1; nominal resolution is not proof of better effective accuracy. | Part IV, Chapter 08 |
| 72-run design | — | Factorial design of four moisture conditions, three temperature conditions, two treatment states and three independent physical replicates. | A selected design, not proof that 72 runs were completed. | Part IV, Chapter 08 |
| Independent physical run | — | One separately prepared or independently reset soil condition with its own physical identity and records. | Repeated ADC samples from one undisturbed container are observations, not additional runs. | Part IV, Chapter 08 |
| Held-out replicate | — | Replicate 3, kept untouched during fitting and model selection for final physical evaluation. | Opening it early or tuning against it destroys the held-out claim. | Part IV, Chapter 08 |
| Grouped cross-validation | — | Model-selection method keeping all observations from one physical batch together. | Prevents electronic rereads from leaking across train and validation groups. | Part IV, Chapter 08 |
| GWC | Gravimetric Water Content | Dry-basis physical reference calculated from wet and constant dry mass. | Requires suitable scale, oven access and dry-to-constant-mass control. | Part IV, Chapter 08 |
| M0 | Model 0 | Uncompensated baseline using raw probe response only. | Compensated models must beat this baseline on the same held-out physical reference. | Part IV, Chapter 08 |
| M1 | Model 1 | Supported low-order compensated linear model using probe response, measured temperature and S0/S1 treatment code. | Final selection must be frozen before replicate 3 is opened. | Part IV, Chapter 08 |
| M2 | Model 2 | Ridge-regularized second-order candidate model evaluated only if justified by grouped training evidence. | Greater complexity is not automatically better and must not be selected post hoc. | Part IV, Chapter 08 |
| Transfer mapping | — | Future hypothesis for adapting donor calibration to a replacement or remounted probe using sparse trusted physical references. | Separate from the semester MVP; requires multi-unit evidence and strong baselines. | Part IV, Chapter 08 |

## A3.6 Patent, legal and research terms

| Term | Expansion | Project mC meaning | Scope or caution | Principal location |
|---|---|---|---|---|
| Patent hypothesis | — | Cautious statement that a specific future mechanism may contain a differentiating technical interaction worth testing and searching. | Not a claim of novelty, patentability or grant. | Parts II–IV |
| Prior art | — | Earlier patents, publications, products or public technical disclosures relevant to a mechanism. | Current primary-source review is required after the mechanism is frozen. | Parts II–IV |
| Patentability terms | Novelty; inventive step; patent eligibility | Legal requirements considered only after a mechanism is frozen and searched. | None is established for a Project mC MVP or future hypothesis. | Parts I–IV |
| FTO | Freedom to Operate | Jurisdiction- and activity-specific assessment of whether intended acts may infringe enforceable claims. | Different from patentability; unavailable without current claim-level professional review. | Parts I–IV |
| File/no-file gate | — | Decision point on whether evidence justifies preparing or pursuing a patent filing. | No positive gate has been passed for the current concepts. | Parts II–IV |
| Inventorship | — | Legal identification of human contributors to the claimed inventive conception. | Model use, authorship and project membership do not automatically determine inventorship. | Parts II–VI |
| Confidentiality boundary | — | Separation of ordinary public semester work from claim-focused or invention-sensitive future research. | Public disclosure may affect later rights; no blanket confidentiality rule is yet recorded. | Parts II–V |

## A3.7 Validation, evidence and statistics terms

| Term | Expansion | Project mC meaning | Scope or caution | Principal location |
|---|---|---|---|---|
| Preregistration | — | Freezing the test protocol, thresholds, splits, metrics and failure rules before locked validation. | Prevents post-hoc tuning against the final evidence. | Parts II–V |
| Held-out evidence | — | Data or physical sessions excluded from tuning and used only for final evaluation. | Random windows from the same physical session may not be independent held-out evidence. | Parts II–V |
| Baseline | — | Simpler conventional method used as the comparison standard for a proposed improvement. | A mechanism is weak if it does not outperform the strongest relevant baseline. | Parts II–IV |
| Ablation | — | Controlled removal of one claimed element to test whether it contributes independently. | Required for cooperative-effect and patent-development claims. | Parts II–IV |
| Leakage | — | Information from held-out or correlated observations entering training, tuning or threshold selection. | Can create falsely high performance, especially with repeated windows or ADC readings. | Parts III–IV |
| Reproducibility | — | Ability of another reviewer or operator to trace and repeat the documented process with controlled inputs. | Does not guarantee identical generative wording or identical physical outcomes. | Parts V–VI |
| RMSE / MAE | Root Mean Square Error / Mean Absolute Error | TrueMoist held-out error metrics used with subset and baseline comparisons. | Must be measured on untouched physical evidence, not inferred from fit. | Part IV, Chapter 08 |
| External verification | — | Later dated verification of current prices, specifications, suppliers, standards, official legal status or other changing external facts. | Not performed in the A3/A4 drafting stage. | Parts I–VI |
| Evidence source, not vote | — | Rule that repeated model conclusions do not become true by majority count. | Weight depends on concept fidelity, source quality, reasoning and human review. | Parts I and VI |

## A3.8 AI workflow, archive and source-integrity terms

| Term | Expansion | Project mC meaning | Scope or caution | Principal location |
|---|---|---|---|---|
| Independent research lane | — | Separately commissioned model-assisted research output used to broaden coverage and expose disagreement. | Lane count is not a vote count; partial or concept-swapped lanes retain reduced or no authority. | Part VI, Chapter 12 |
| Synthesis | — | Controlled integration of research lanes into a concept-faithful evidence position. | A valid synthesis remains decision support, not architecture or approval authority. | Parts II–IV and VI |
| Adjudication | — | Cross-concept comparative review applying common evidence and gates. | The two final adjudications agree on VibeGuard for semester build but disagree on the future patent gate. | Parts I and VI |
| Concept fidelity | — | Degree to which a report analyzes the authoritative frozen concept rather than a different problem or architecture. | Material concept swaps are excluded rather than averaged. | Parts I and VI |
| Concept swap | — | Research or synthesis that substitutes a materially different design under the same concept name. | Failed OpenBraille moving-roller and VibeGuard software-security outputs cannot re-enter current authority. | Part VI, Chapters 12–13 |
| Manifest | — | File-control list of expected attachments, sizes, hashes and roles. | Establishes package identity only; not technical evidence. | Part VI, Chapter 12; Appendix A1 controls |
| Transport and provenance controls | Launchers, governing instructions, manifests and provenance/exclusion registers | Records defining the intended task, package identity, path history and exclusions. | They support traceability but do not prove execution compliance or technical truth. | Part VI, Chapter 12 |
| Source freeze | — | Time-bounded accounting state preserving source identities, paths and hashes for manual construction. | Does not prohibit later evidence; later evidence requires a logged revision. | Part VI, Chapter 14 |
| Frozen source map | — | 301-record map assigning represented sources to manual destinations and authority/treatment categories. | A classification system, not a claim-validity ranking. | Part VI, Chapter 14; Appendix A1 |
| Unmapped-file register | — | Controlled record of organized files not assigned by the frozen chapter rules. | One concept-portfolio index remains unmapped; absence of mapping is not loss of the file. | Part VI, Chapter 14; Appendix A1 |
| Canonical source | — | Current controlled record selected to govern present citation or state. | Canonical selection preserves, rather than erases, historical variants. | Part VI, Chapters 13–14 |
| Duplicate | — | Multiple physical files representing identical or content-equivalent material. | Exact duplicate copies are one logical source and must not be counted as corroboration. | Part VI, Chapter 14 |
| SHA-256 | Secure Hash Algorithm 256-bit | Byte-identity digest used for copy validation, duplicate grouping and silent-change detection. | Proves identical compared bytes only; not truth, authority, cross-format equivalence or approval. | Part VI, Chapter 14; Appendix A1 |
| Superseded | — | Earlier valid record replaced by a later controlling version. | May be consulted for chronology but cannot override the replacement. | Part VI, Chapter 13 |
| Failed, partial and excluded outputs | — | Controlled lifecycle states for concept-swapped reports, incomplete fragments and supplements outside a blind set. | Failed material is non-evidence; partial conclusions are not reconstructed; excluded supplements need explicit later authorization. | Part VI, Chapter 13 |
| Non-reconstruction rule | — | Missing conclusions remain unavailable or partial rather than being inferred from fragments. | Applies to model outputs, approvals, results and legal conclusions. | Parts I and VI |
| Stage 10R | — | Mechanical provenance/archive/source-integrity packet stage that passed extraction but had inadequate substantive coverage for Chapters 12–14. | Zero extraction errors did not prove adequate coverage. | Part VI, Chapter 14 |
| Stage 10S | — | Controlled coverage-repair stage selecting representative substantive sources for Chapters 12–14 without altering the frozen map. | Repaired representative coverage, not exhaustive semantics or the original 301-record map. | Part VI, Chapter 14 |

## A3.9 Undefined or intentionally unresolved labels

| Label | Expansion | Project mC meaning | Scope or caution | Principal location |
|---|---|---|---|---|
| PIRG | Undefined in the controlling record | Project label for a future VibeGuard research map involving label-aware, contamination-protected, confidence-gated single-node target/interference attribution, later narrowed to paired intervention contrasts. | No expansion is authorized. PIRG is not part of the Level-1 MVP, not implemented, not validated and not a filing basis. | Part III, Chapter 07 |

## A3.10 Glossary limitations

This glossary does not freeze test numbers that the controlling Parts leave open, resolve the ESP32/STM32 course-platform question, approve the OpenBraille-to-VibeGuard shift, authorize Phase 4 or procurement, or create a combined architecture. OpenBraille D11 and VPD-C7 remain separate hypotheses. PIRG remains an undefined project label. TrueMoist’s 72-run design remains a design rather than proof of completed runs. Terms concerning patent law are used conservatively and do not replace institutional or professional legal review.

# Appendix A4 — Open Decisions and Change Log

## A4.1 Purpose and control boundary

Appendix A4 consolidates unresolved decisions and major controlled transitions already present in validated Parts I–VI. It does not create a new decision, select a concept, approve execution, infer missing teacher feedback, certify a prototype or resolve the disagreement between the two final adjudications. Every downstream action remains blocked until the authority or evidence named in the register is obtained.

## A4.2 Consolidated open-decision register

| ID | Open decision or evidence gap | Current state | Controlling part/source | Required authority or evidence | Blocked downstream action | Prohibited inference |
|---|---|---|---|---|---|---|
| A4-OD01 | Teacher decision on proposed OpenBraille-to-VibeGuard shift | Formal request exists; approval, conditions or rejection are absent | Part I, Chapters 00 and 09; Part V, Chapter 10 | Explicit dated teacher/course-authority record | Final concept freeze, concept-specific execution and procurement | “The project has changed to VibeGuard” |
| A4-OD02 | Final authorized semester concept | Open among the retained controlled records | Part I; Decision Register v1.2; Part V | Controlling decision naming one concept and scope, or an authorized conditional gate process | Phase 4 entry and branch-specific scheduling | Recommendation equals authorization |
| A4-OD03 | Exact MCU and course-platform acceptance | ESP32-class architectures are frozen; STM32/course acceptance remains unresolved | Parts I–V | Written acceptance of exact board/toolchain or controlled substitution | Exact pin map, board procurement and final firmware baseline | ESP32 is automatically accepted or automatically prohibited |
| A4-OD04 | Project-wide Phase 4 authorization | Not proved started | Parts I, V and VI | Approved entry record after concept, platform, budget, safety and ownership gates | Procurement, fabrication, coding and formal execution claims | Historical roadmaps prove implementation began |
| A4-OD05 | Procurement-ready BOM and current cost freeze | Historical BOMs exist; current specifications, Indian prices and supplier authenticity are unverified | Parts II–V; authority protocol | Dated manufacturer/supplier verification, approved exact BOM and budget | Purchasing and current-cost publication | Historical estimates are current prices or actual spend |
| A4-OD06 | Named team roles, reviewers and backups | Functional roles proposed; named assignment not signed | Parts I and V | Recorded primary owner, reviewer, backup and cross-training plan | Accountable subsystem execution and continuity | Proposed role table is final team allocation |
| A4-OD07 | Facility and safety approval | Concept dependencies and hazards identified; actual access/approval not proved | Parts II–V | Confirmed FDM/tools, rig area or oven/scale access plus responsible safety sign-off | Concept-specific build and testing | Facility availability or safety clearance is complete |
| A4-OD08 | Final quantitative success, hold-out and kill criteria | Concept-specific frameworks exist; exact approved values remain open | Parts II–V | Preregistered protocol for the authorized branch before locked validation | Acceptance testing and performance claims | Proposed thresholds are achieved results |
| A4-OD09 | Physical prototype and held-out evidence | No project-wide completed prototype or locked validation is established | Parts II–VI | Configuration-controlled hardware, firmware, run ledgers, measurements and sign-offs | Demonstrated performance, completion and publication claims | Architecture documentation proves a working prototype |
| A4-OD10 | Future patent-development gate | Final adjudications disagree on the preferred first gate and later route | Parts I–IV and VI | Authorized gate or replacement rule plus new physical evidence | Patent-first down-selection and claim-focused experiments | Model agreement or one adjudication settles the route |
| A4-OD11 | Current patent, NPL, legal-status and FTO review | Time-bounded or incomplete; no current clearance | Parts II–IV; authority protocol | Current official-source search, exact mechanism freeze and professional/institutional claim review | Filing decision, clearance statements and commercial acts | Search silence proves novelty or FTO |
| A4-OD12 | Confidentiality, ownership, contribution and inventorship | Institutional rules and human contribution chronology are unresolved | Parts I–VI | Written institutional IPR guidance and dated contribution records | Public claim-focused disclosure and filing preparation | Team membership, authorship or model output determines inventorship |
| A4-OD13 | Treatment of unmapped concept-portfolio index | One organized file remains unmapped under the frozen source rules | Part VI, Chapter 14; Appendix A1 | Logged map revision or controlled appendix/chapter assignment preserving the prior map | Claim of complete chapter assignment | Unmapped means missing, irrelevant or silently assignable |
| A4-OD14 | Final manual release and reviewer sign-off | Complete controlled draft mechanically assembled; integrity-review correction closure, final release metadata and reviewer sign-off remain pending | Part VI, Chapter 14; final assembly map and integrity-review report | Closed correction register, regenerated hashes/map, final version/date and approving reviewer | Publication as final controlled Master Manual | Mechanical assembly or draft completion equals final release |
| A4-OD17 | OpenBraille mechanical, power and tactile acceptance | Architecture frozen; one-dot mechanics, six-servo power, lifecycle and approved tactile result absent | Part II | One-dot coupon gates, measured power/grounding, locked pattern/lifecycle tests and approved blinded tactile protocol | Six-dot acceptance and bounded tactile claim | PWM/current/visual motion proves correct tactile state |
| A4-OD18 | VibeGuard acquisition, mount, rig and Level-1 criteria | Logic fixed; exact board, sampling integrity, remount repeatability, fixture and numeric protocol untested | Part III | Incoming hardware checks, rigid-mount study, achieved-rate/loss tests, safety acceptance and blocked hold-outs | Reliable Level-1 performance claim | A red/green demo proves diagnosis or attribution |
| A4-OD19 | VibeGuard PIRG and later attribution feasibility | Candidate research map only; independent labels, identifiability, useful Unknown coverage and field access absent | Part III, Chapter 07 | Separate factorial rig, temporary references, blocked sessions/remounts, strongest baselines and authorized site access | Level-2 continuation and patent-development claim | Level-1 anomaly detection proves target attribution |
| A4-OD20 | TrueMoist facilities, probe validity and 72-run throughput | Architecture selected; probe authenticity, insertion/packing repeatability, oven/scale access and throughput unproved | Part IV | Early pilots, facility confirmation, frozen preparation method and physical run ledger | Main 72-run collection and feasibility claim | Factorial design proves runs were completed |
| A4-OD21 | TrueMoist acquisition path, model freeze and held-out replicate | ADS1115/ADC1 gate, exact targets/dose, M1/M2 choice and replicate-3 test remain open | Part IV | Paired ADC evidence, pilot-frozen factors, grouped model selection, numerical equivalence and untouched final test | Compensation-success and error claims | Training fit or repeated ADC lines are held-out physical evidence |

**Identifier continuity note:** A4-OD15 and A4-OD16 are intentionally unused in this release. Existing identifiers are retained to preserve controlled references; the gap is editorial and does not imply that two decisions are missing.


## A4.3 Concept-specific unresolved items

### A4.3.1 OpenBraille

OpenBraille remains a legitimate retained architecture but is not the strongest current semester recommendation and is not an authorized build. Before any implementation claim, the team must resolve exact platform acceptance, FDM and measurement access, one-dot raise/retract behavior, calibrated command windows, six-channel interference, power distribution, grounding, repeatability, wear, supported pattern set and safety. A tactile claim requires an approved blinded protocol, participant conditions and stop rules; otherwise the claim must be omitted. D11 and VPD-C7 may be considered only as separate post-MVP research configurations. They must not be merged, inserted into the frozen cell or represented as tested.

### A4.3.2 VibeGuard

VibeGuard is the strongest semester-build recommendation, not an approved semester concept. The Level-1 branch still requires an approved board, verified sensor/module, rigid mount, measured sampling and timestamp integrity, a safe repeatable abnormal-state fixture, pre-registered thresholds and persistence, blocked sessions/day/remount structure, and explicit rules for FFT or Mahalanobis retention. PIRG has no authorized expansion and remains a later candidate hypothesis. It requires independent target/interferer labels, contrast identifiability, useful risk/coverage, remount validity, edge-resource evidence and field-like access. Failure of that later path would not invalidate a successful Level-1 semester result.

### A4.3.3 TrueMoist

TrueMoist remains retained but neither selected nor rejected. Its early feasibility depends on genuine probe behavior, controlled reinsertion and packing, a paired ADS1115-versus-ESP32-ADC1 gate, oven/scale access, dry-to-constant-mass workflow, final soil preparation, moisture regions, S1 dose, randomization/blocking and practical throughput. The 72-run structure is authoritative, while a 54-run contingency requires formal change control. M1 or M2 must be frozen before replicate 3 is opened, and Python-to-MCU numerical equivalence must be archived. Future replacement/remount transfer remains a separate Level-2 hypothesis and must beat simple affine-transfer and gating baselines on independent multi-unit evidence.

## A4.4 Teacher, course and execution unresolved items

The record proves the official OpenBraille zeroth-review deck dated 30 July 2026 and the later VibeGuard shift request, but contains no review outcome or approval. Final concept, platform, Phase 4, procurement, ownership, safety, schedule and demonstration decisions remain open. Chapter 11 remains conditional until direct execution records enter through change control.

## A4.5 Patent, confidentiality and IPR unresolved items

No frozen MVP is established as patentable. D11, VPD-C7, PIRG and TrueMoist transfer/validity paths remain hypotheses, and the adjudications disagree on the first later gate. Claim-focused work requires a frozen mechanism, preregistered experiments, baselines/ablations, current official-source review, FTO analysis, institutional IPR guidance, confidentiality control and dated contribution records. No filing commitment is authorized.

## A4.6 Repository, source-map and release unresolved items

The frozen source map contains 301 records and one separately recorded unmapped concept-portfolio index. Appendix A1 preserves both; Appendix A2 preserves 18 reference-only records. Any map revision must preserve the earlier map and record its reviewer and effects. The complete controlled draft has been mechanically assembled. Integrity-review correction closure, final release metadata and reviewer sign-off remain pending.

## A4.7 Major controlled project change log

| Change ID | Date or ordered stage | Previous controlled state | New controlled state | Reason/evidence | Approval or authority effect |
|---|---|---|---|---|---|
| CH-01 | Phase 1A | Broad domains and problem reports | Evidence-grounded opportunity set | Problems were explored before products or architectures | Historical discovery only; no concept approval |
| CH-02 | Phase 1B | Unstructured opportunity findings | 32-cluster dataset with ranked Top 20 | Duplicate preservation, clustering and weighted evaluation | Historical analysis; no solution freeze |
| CH-03 | Phase 1B.5 correction | Intermediate record reported 22 survivors | Valid Phase 1C input corrected to 16 | Six out-of-Top-20 entries had re-entered; four Top-20 entries were legitimately gated out | Corrects historical pipeline count; does not select a final concept |
| CH-04 | Phase 1C | Valid opportunity survivors | One concept per 16 survivor and historical Top Five | First permitted concept-synthesis stage | Broad concepts created; no current architecture authority |
| CH-05 | Phase 2 | Patent research assumed concept labels were understood | Concept-restatement and exclusion-over-averaging rules established | One lane materially swapped OpenBraille, VibeGuard and TrustLatch identities | Failed sections excluded; no current patent conclusion |
| CH-06 | Phase 3A, EDR and Phase 3B | Broad concept and historical patent impressions | Engineering state, stable hypotheses, minimum demonstrable success and feasibility evidence | Needed engineering fidelity before architecture freeze | Decision support strengthened; no final authorization |
| CH-07 | Final Phase 3C | Multiple candidate architectures and five historical concepts | Frozen OpenBraille, VibeGuard and TrueMoist architectures; TrustLatch and ColdTrace deferred | One architecture per completed retained concept and controlled portfolio closure | Current architecture authority established for retained three |
| CH-08 | Decision Register progression | v1.0 and v1.1 preserved earlier governance, including the superseded TrueMoist 135-run branch | v1.2 became canonical and controls the validated 72-run design and current portfolio | Later reconciliation and accepted decisions superseded the earlier states | Earlier versions remain chronology only and cannot override v1.2 |
| CH-09 | Patent synthesis audit | Mixed valid, failed, partial and supplementary outputs | Concept-faithful syntheses retained; failed swaps, partial conclusions and excluded supplement separated | Prevented mis-scoped or incomplete model work from being averaged into conclusions | Evidence quality improved; model outputs remain non-voting support |
| CH-10 | Final adjudications | Separate concept evidence and common gates | Two final comparative adjudications preserved | Both support VibeGuard for semester build but disagree on future patent route | Recommendation strengthened; future patent gate remains unresolved |
| CH-11 | Proposed concept shift | OpenBraille was the submitted semester concept | Formal request proposed VibeGuard Level 1 while retaining OpenBraille records separately | Lower implementation risk, clearer quantitative validation and stronger team fit | Request only; teacher approval absent |
| CH-12 | Repository organization and source freeze | Large working repository with variants, duplicates and archive material | Canonical organized representation, archives/exclusions and frozen accounting state | Needed traceability, duplicate control and reproducible manual construction | Source freeze recorded at `2026-08-03T21:59:10.355043+02:00`; not a technical or approval event |
| CH-13 | Master Manual drafting | Frozen source map and chapter blueprint | Validated Parts I–VI drafted under controlled packages | Converted distributed evidence into governed manual parts | Drafting does not amend source authority or approve execution |
| CH-14 | Stage 10R | Mechanical packet extraction passed | Coverage defect identified: Chapters 12–13 had zero substantive Tier 1–4 mapped sources and Chapter 14 had only two | Extraction success did not ensure substantive chapter coverage | Stage 10R not used as sufficient Part VI basis |
| CH-15 | Stage 10S repair | Inadequate representative coverage for Chapters 12–14 | Repaired selections of 17, 17 and 23 sources, with zero extraction/hash failures | Added representative substantive coverage without changing the frozen map | Post-freeze repair control only; not new pre-freeze project evidence |
| CH-16 | Mechanically generated appendices | Frozen source map and peer-reference assignments existed separately | Appendix A1 generated from 301 mapped records plus one unmapped row; Appendix A2 generated from 18 reference-only records | Required auditable source and peer-reference registers | Mechanical controls only; not technical evidence |
| CH-17 | A3/A4 drafting stage | Parts I–VI and A1/A2 available; A3/A4 pending | Controlled A3 glossary and A4 open-decision/change-log draft produced | Completes the remaining drafted appendix content before assembly | Does not itself release the complete manual |

## A4.8 Master Manual construction change log

| Manual stage | Output or event | Control result | Remaining next action |
|---|---|---|---|
| Blueprint and authority setup | Manual objective, chapter structure, authority hierarchy and contradiction rules established | Frozen concepts, source authority and approval boundaries were separated | Continue to preserve these controls during assembly |
| Validated Part I | Opening, governance, phase history, portfolio and comparative decision | VibeGuard recorded as strongest recommendation; shift, platform, Phase 4 and procurement left open | Obtain controlling teacher/course decisions |
| Validated Parts II–IV | Separate OpenBraille, VibeGuard and TrueMoist architecture/patent-path records | Architecture locks and concept-specific open decisions preserved without hybridization | Authorize one branch before execution; retain later hypotheses separately |
| Validated Part V | Teacher-review history and Chapter 11 execution framework | Official submission and change request recorded; zero-source execution boundary preserved | Add explicit teacher outcome and future direct execution records when available |
| Stage 10R audit | Initial provenance/archive/integrity packets mechanically validated | Revealed substantive coverage defect despite extraction success | Repair representative source coverage |
| Stage 10S repair | Repaired Chapter 12–14 packets and selection controls | Representative coverage restored without editing the frozen 301-record map | Use repaired basis for Part VI drafting and release audit |
| Validated Part VI | Provenance, archive, source integrity and release controls | Source freeze, canonical/duplicate rules, exclusions, limitations and open release items consolidated | Complete appendices and final assembly validation |
| Generated Appendix A1 | Complete source register | Recorded 301 frozen map rows and one unmapped register row | Preserve mechanically; revise only through controlled map versioning |
| Generated Appendix A2 | Peer project and reference register | Recorded 18 reference-only records | Preserve mechanically; do not treat as Project mC authority |
| A3/A4 drafting stage | Glossary and consolidated open decisions/change logs | Remaining non-mechanical appendix content drafted from validated Parts I–VI | Assemble complete manual, run contradiction/source-note checks and obtain reviewer sign-off |

## A4.9 Current-state summary

- VibeGuard remains the strongest semester-build recommendation.
- The proposed OpenBraille-to-VibeGuard shift is not proved teacher-approved.
- The final authorized semester concept and exact course platform remain unresolved.
- OpenBraille, VibeGuard and TrueMoist remain separate controlled records; no hybrid is authorized.
- Chapter 11 remains a future execution framework with zero directly mapped execution sources.
- Project-wide Phase 4, procurement, named role freeze and physical validation are not proved started or complete.
- Current prices, specifications, supplier authenticity, facilities and legal status require later dated verification.
- No frozen MVP is established as patentable, filed or FTO-cleared.
- The two final adjudications disagree on the preferred future patent-development gate.
- Model outputs remain evidence sources, not votes; failed, partial and excluded outputs retain their controlled status.
- The frozen source map retains one explicitly unmapped concept-portfolio index.
- The complete controlled draft has been mechanically assembled; integrity-review correction closure, final release metadata and reviewer sign-off remain pending.

## A4.10 Appendix limitations

This appendix records what is open and what changed; it does not prove that an unresolved action later occurred. It does not authorize a procurement, prototype, participant test, facility use, patent search, disclosure or filing. Dates are included only where the validated sources provide them. Ordered stages are used elsewhere without invented dates. Future decisions should be added through an auditable revision that identifies the authority, evidence, affected architecture or source map, and prior release preserved.

# Appendices A3–A4 Source Note

The following original organized-workspace controlled outputs were materially used:

- `08_MASTER_MANUAL/03_Drafting_Workspace/01_Validated_Parts/Part_I/Project_mC_Master_Manual_Part_I_Opening_Governance_History_and_Decision.md` — governance, phase history, comparative decision and consolidated project open decisions.
- `08_MASTER_MANUAL/03_Drafting_Workspace/01_Validated_Parts/Part_II/Project_mC_Master_Manual_Part_II_OpenBraille_Architecture_and_Patent_Path.md` — OpenBraille architecture, validation, D11/VPD-C7 distinctions and unresolved items.
- `08_MASTER_MANUAL/03_Drafting_Workspace/01_Validated_Parts/Part_III/Project_mC_Master_Manual_Part_III_VibeGuard_Architecture_and_Patent_Path.md` — VibeGuard architecture, Level-1/Level-2 boundaries, PIRG caution and unresolved items.
- `08_MASTER_MANUAL/03_Drafting_Workspace/01_Validated_Parts/Part_IV/Project_mC_Master_Manual_Part_IV_TrueMoist_Architecture_Evidence_and_Research_Position.md` — TrueMoist 72-run architecture, validation design, future transfer hypothesis and unresolved items.
- `08_MASTER_MANUAL/03_Drafting_Workspace/01_Validated_Parts/Part_V/Project_mC_Master_Manual_Part_V_Teacher_Review_and_Semester_Execution.md` — teacher-review boundary, Chapter 11 future execution framework and approval/execution open decisions.
- `08_MASTER_MANUAL/03_Drafting_Workspace/01_Validated_Parts/Part_VI/Project_mC_Master_Manual_Part_VI_Provenance_Archive_and_Source_Integrity.md` — AI workflow, archive states, source freeze, Stage 10R/10S, source-map and release controls.
- `08_MASTER_MANUAL/09_Appendices_Workspace/Appendix_A1_Complete_Source_Register.md` — mechanical source-map and unmapped-register control.
- `08_MASTER_MANUAL/09_Appendices_Workspace/Appendix_A2_Peer_Project_and_Reference_Register.md` — mechanical reference-only peer-project control.

Appendices A1 and A2 were not rewritten.

<!-- END CONTROLLED COMPONENT: APPENDICES_A3_A4_RELEASE_CORRECTED -->

<!-- END CONTROLLED COMPONENT: APPENDICES_A1_TO_A4_RELEASE_CANDIDATE -->
