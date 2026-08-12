# Project mC Organized Workspace

## Current project status

- **VibeGuard — FINAL semester selection**
- **Phase 3C — CLOSED**
- **Phase 4 — OPEN**
- Active work: the frozen **Level-1 VibeGuard** semester architecture and Phase 4 execution package.
- PIRG remains separate post-semester/future research.
- OpenBraille and TrueMoist remain retained research/history, not the semester implementation.

Current state is controlled by the [Final Selection and Phase 4 Entry Memo](07_SEMESTER_EXECUTION/01_Selected_Project/Project_mC_Final_Selection_and_Phase4_Entry_Memo.md) and [Decision Register v1.3](01_GOVERNANCE_AND_CONTROL/02_Decision_Registers/Project_mC_Decision_Register_v1.3.md).

## How to navigate

| Document | Use it for |
|---|---|
| This `README.md` | High-level status and repository map. |
| [WHERE_TO_LOOK.md](00_START_HERE/WHERE_TO_LOOK.md) | “I need X—which document do I open?” Start here for practical navigation. |
| [FILE_CATALOG.md](FILE_CATALOG.md) | Detailed file-by-file metadata, classification, hashes and use warnings. |
| [MAINTENANCE_GUIDE.md](MAINTENANCE_GUIDE.md) | Safe rules for adding, versioning, archiving and cataloging files. |
| [Master Manual v1.0](08_MASTER_MANUAL/10_Final_Assembly_Workspace/03_Final_Controlled_Releases/v1.0/Project_mC_Master_Manual_FINAL_CONTROLLED_RELEASE.md) | Frozen comprehensive historical release—not the live Phase 4 operating manual. |

## Current-use shortcuts

- **Learn VibeGuard:** [Team Orientation and Project Primer](07_SEMESTER_EXECUTION/01_Selected_Project/CURRENT/VibeGuard_Team_Orientation_and_Project_Primer.md)
- **Know what to do next:** [Semester Execution Playbook](07_SEMESTER_EXECUTION/01_Selected_Project/CURRENT/VibeGuard_Semester_Execution_Playbook.md)
- **Buy/accept hardware:** [Procurement, Component Acceptance and Lab Setup Checklist](07_SEMESTER_EXECUTION/02_BOM_and_Procurement/CURRENT/VibeGuard_Procurement_Component_Acceptance_and_Lab_Setup_Checklist.md)
- **Log experiments/evidence:** [Lab Evidence and Engineering Logbook](07_SEMESTER_EXECUTION/05_Test_Protocols_and_Data/CURRENT_Protocols/VibeGuard_Lab_Evidence_and_Engineering_Logbook.md)
- **See the package:** [Phase 4 Execution Package Index](07_SEMESTER_EXECUTION/01_Selected_Project/CURRENT/00_VibeGuard_Phase4_Execution_Package_Index.md)
- **Current selection/status:** [Final Selection Memo](07_SEMESTER_EXECUTION/01_Selected_Project/Project_mC_Final_Selection_and_Phase4_Entry_Memo.md)
- **Current decisions:** [Decision Register v1.3](01_GOVERNANCE_AND_CONTROL/02_Decision_Registers/Project_mC_Decision_Register_v1.3.md)
- **Comprehensive controlled snapshot:** [Master Manual v1.0](08_MASTER_MANUAL/10_Final_Assembly_Workspace/03_Final_Controlled_Releases/v1.0/Project_mC_Master_Manual_FINAL_CONTROLLED_RELEASE.md)

## Major folder overview

| Folder | What it contains | Status | When to open it |
|---|---|---|---|
| `00_START_HERE/` | Documentation navigation, inventories, release-validation records and organization history. | Mixed: current navigation plus historical controls. | Open first when locating a document or auditing repository documentation. |
| `01_GOVERNANCE_AND_CONTROL/` | Requirements, Decision Registers, authority map, phase context and repository controls. | Current governance plus preserved predecessors. | Open for current decisions; use v1.3, not v1.2, for live state. |
| `02_PHASE_HISTORY/` | Chronological Phase 1–3 research, reports, memories and raw evidence. | Historical. | Open to reconstruct how concepts and decisions developed. |
| `03_CONCEPT_PORTFOLIO/` | Concept-specific final architectures, research, syntheses, simulations and roadmaps. | Mixed current reference and historical/research evidence. | Open for OpenBraille, VibeGuard, TrueMoist or deferred-concept technical history. |
| `04_COMPARATIVE_DECISION/` | Shared evidence, adjudications, change request and team review material. | Decision context. | Open to understand why VibeGuard was recommended and selected; these files are not votes. |
| `05_TEACHER_AND_REVIEWS/` | Teacher-facing documents, official OpenBraille zeroth-review submission, drafts and peer references. | Mixed presentation/history. | Open for review/submission material; no controlled VibeGuard zeroth-review PPTX is currently present. |
| `06_TRANSPORT_AND_PROVENANCE/` | Upload instructions, manifests, launchers, bundles and validation. | Provenance/transport. | Open to verify package identity—not for technical authority. |
| `07_SEMESTER_EXECUTION/` | Current VibeGuard Phase 4 package, BOM, lab controls and execution destinations. | Current execution plus superseded Phase 4 drafts. | Open for daily semester work. |
| `08_MASTER_MANUAL/` | Master Manual source maps, drafting/review history, assembly and controlled v1.0 release. | Controlled historical release and work products. | Open for the comprehensive snapshot and provenance, not daily Phase 4 instructions. |
| `09_ARCHIVE/` | Superseded, exact-duplicate, failed/partial, ZIP and quarantined material. | Archive. | Open only for audit, provenance or recovery; do not treat as current authority. |

## Current architecture boundary

The semester implementation is the controlled Level-1 VibeGuard system: one rigidly mounted ADXL345-class tri-axis accelerometer, one authorized ESP32-family controller, SPI acquisition, local preprocessing/DC removal, RMS plus persistence, triggered Hann-windowed FFT/bands, optional ordinary Mahalanobis comparator, RGB indication, USB logging and a guarded low-voltage motor/fan normal-versus-induced-abnormal rig.

PIRG, a permanent second accelerometer, dense-machine attribution, cloud dependence, active cancellation and industrial RUL claims are outside the semester MVP.

## Important historical-data warning

**What exists is not always what is current.** Older files may correctly describe earlier Project mC stages, rankings or architectures. Decision Register v1.2 is a valid predecessor, old OpenBraille and TrueMoist work remains useful, and Phase-1C VibeGuard material may discuss spatial isolation or bearing-fault ideas. None overrides Decision Register v1.3, the Final Selection Memo, final VibeGuard architecture, or the current Phase 4 package.

Authority follows controlled content and provenance—not filename date, model agreement or copy location. Raw research is evidence, adjudications are decision context, and transport copies are not independent authority.

## Master Manual

The [Project mC Master Manual v1.0](08_MASTER_MANUAL/10_Final_Assembly_Workspace/03_Final_Controlled_Releases/v1.0/Project_mC_Master_Manual_FINAL_CONTROLLED_RELEASE.md) is a major comprehensive controlled release dated 2026-08-06. Verified SHA-256: `4700c630c21c73d7709bfc317c7e6eba155ed768d60d40ff2781e76cb5c787e8`.

It remains valuable for history, evidence, reasoning and provenance. Later Decision Register v1.3 and Phase 4 records supersede its state-specific wording. Never edit the controlled release silently.
