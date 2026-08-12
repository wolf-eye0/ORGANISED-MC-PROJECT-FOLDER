# Stage 10R-R — Provenance, Archive and Integrity Coverage Repair Audit

Generated: 2026-08-04T21:17:49.155873+02:00

## Why this audit was required

Stage 10R passed its extraction mechanics, but the frozen chapter assignments produced insufficient substantive coverage:

- Chapter 12 mapped Tier 1–4 sources: **0**
- Chapter 13 mapped Tier 1–4 sources: **0**
- Chapter 14 mapped Tier 1–4 sources: **2**

A zero-error extraction result does not by itself establish that a chapter has enough evidence for reconciliation. This audit searches the organized workspace for cross-cutting provenance, archive and integrity controls without changing the frozen source map or deleting any file.

## Candidate coverage

| Chapter | Existing mapped Tier 1–4 | Candidate rows | Already represented | Unmapped/post-freeze controls |
|---:|---:|---:|---:|---:|
| 12 | 0 | 101 | 92 | 9 |
| 13 | 0 | 150 | 130 | 20 |
| 14 | 2 | 231 | 130 | 101 |

## Highest-scoring candidates

### Chapter 12 — Provenance and AI-Use Controls

| Score | Source-map status | Existing chapter | Authority | Relative path |
|---:|---|---:|---|---|
| 76 | YES | 12 | `TIER_5` | `06_TRANSPORT_AND_PROVENANCE/03_Launchers_and_Checklists/VibeGuard_Synthesis_Launcher_FINAL.txt` |
| 71 | YES | 12 | `TIER_5` | `06_TRANSPORT_AND_PROVENANCE/01_Governing_Instructions/TrueMoist_Synthesis_Instructions_CANONICAL.md` |
| 63 | YES | 12 | `TIER_5` | `06_TRANSPORT_AND_PROVENANCE/02_Input_Manifests/VibeGuard_Synthesis_INPUT_MANIFEST.md` |
| 62 | YES | 12 | `TIER_5` | `06_TRANSPORT_AND_PROVENANCE/02_Input_Manifests/OpenBraille_PreBuild_INPUT_MANIFEST.md` |
| 62 | YES | 12 | `TIER_5` | `06_TRANSPORT_AND_PROVENANCE/03_Launchers_and_Checklists/TrueMoist_Synthesis_Launcher_FINAL.txt` |
| 61 | YES | 12 | `TIER_5` | `06_TRANSPORT_AND_PROVENANCE/01_Governing_Instructions/Project_mC_Final_Adjudication_Instructions_CANONICAL.md` |
| 59 | YES | 12 | `TIER_5` | `06_TRANSPORT_AND_PROVENANCE/02_Input_Manifests/VibeGuard_PreBuild_INPUT_MANIFEST.md` |
| 58 | YES | 12 | `TIER_5` | `06_TRANSPORT_AND_PROVENANCE/03_Launchers_and_Checklists/OpenBraille_PreBuild_Launcher_FINAL.txt` |
| 57 | YES | 12 | `TIER_5` | `06_TRANSPORT_AND_PROVENANCE/02_Input_Manifests/Final_Adjudication_EXCLUSION_AND_PROVENANCE_REGISTER.md` |
| 57 | YES | 12 | `TIER_5` | `06_TRANSPORT_AND_PROVENANCE/03_Launchers_and_Checklists/Codex_Workflows/CODEX_ORGANIZE_VIBEGUARD_SYNTHESIS_PACKAGE.txt` |
| 56 | YES | 12 | `TIER_5` | `06_TRANSPORT_AND_PROVENANCE/02_Input_Manifests/TrueMoist_Synthesis_INPUT_MANIFEST.md` |
| 55 | YES | 12 | `TIER_5` | `06_TRANSPORT_AND_PROVENANCE/01_Governing_Instructions/TrueMoist_Patent_Research_Instructions_CANONICAL.md` |
| 55 | YES | 12 | `TIER_5` | `06_TRANSPORT_AND_PROVENANCE/03_Launchers_and_Checklists/Project_mC_Teacher_Document_Master_Launcher_FINAL.txt` |
| 55 | YES | 12 | `TIER_5` | `06_TRANSPORT_AND_PROVENANCE/03_Launchers_and_Checklists/VibeGuard_PreBuild_Launcher_FINAL.txt` |
| 54 | YES | 12 | `TIER_5` | `06_TRANSPORT_AND_PROVENANCE/03_Launchers_and_Checklists/TrueMoist_Patent_Research_Launcher_GEMINI_10.txt` |
| 53 | YES | 12 | `TIER_5` | `06_TRANSPORT_AND_PROVENANCE/02_Input_Manifests/OpenBraille_Synthesis_INPUT_MANIFEST.md` |
| 53 | YES | 12 | `TIER_5` | `06_TRANSPORT_AND_PROVENANCE/03_Launchers_and_Checklists/Project_mC_Final_Adjudication_Launcher_FINAL.txt` |
| 52 | YES | 12 | `TIER_5` | `06_TRANSPORT_AND_PROVENANCE/03_Launchers_and_Checklists/Codex_Workflows/CODEX_CREATE_TRUEMOIST_GEMINI10_QWEN5_PACKAGES.txt` |
| 50 | YES | 12 | `TIER_5` | `06_TRANSPORT_AND_PROVENANCE/01_Governing_Instructions/Historical_Upload_Pack_Variants/OpenBraille_Patent_Synthesis_Input__00_READ_FIRST_OpenBraille_Synthesis_Instructions.md` |
| 50 | YES | 12 | `TIER_5` | `06_TRANSPORT_AND_PROVENANCE/01_Governing_Instructions/Historical_Upload_Pack_Variants/VibeGuard_Patent_Research_Input__00_READ_FIRST_VibeGuard_Patent_Research_Instructions.md` |
| 50 | YES | 12 | `TIER_5` | `06_TRANSPORT_AND_PROVENANCE/01_Governing_Instructions/OpenBraille_PreBuild_Patent_Simulation_Instructions.md` |
| 49 | YES | 12 | `TIER_5` | `06_TRANSPORT_AND_PROVENANCE/03_Launchers_and_Checklists/Codex_Workflows/CODEX_ORGANIZE_PROJECT_MC_FINAL_ADJUDICATION_PACKAGE.txt` |
| 48 | YES | 12 | `TIER_5` | `06_TRANSPORT_AND_PROVENANCE/01_Governing_Instructions/VibeGuard_Synthesis_Instructions_CANONICAL.md` |
| 48 | YES | 12 | `TIER_5` | `06_TRANSPORT_AND_PROVENANCE/03_Launchers_and_Checklists/Codex_Workflows/CODEX_ORGANIZE_TRUEMOIST_SYNTHESIS_PACKAGE.txt` |
| 47 | YES | 12 | `TIER_5` | `06_TRANSPORT_AND_PROVENANCE/01_Governing_Instructions/VibeGuard_PreBuild_Patent_Simulation_Instructions.md` |

### Chapter 13 — Superseded, Failed, Partial and Archived Material

| Score | Source-map status | Existing chapter | Authority | Relative path |
|---:|---|---:|---|---|
| 97 | YES | 13 | `TIER_5` | `09_ARCHIVE/03_Failed_or_Partial_Research/VibeGuard/FAILED_CONCEPT_SWAP_VibeGuard_Deep_Research_Synthesis.md` |
| 82 | YES | 13 | `TIER_5` | `09_ARCHIVE/03_Failed_or_Partial_Research/OpenBraille/FAILED_CONCEPT_SWAP_OpenBraille_Deep_Research_Synthesis.md` |
| 76 | YES | 13 | `TIER_5` | `09_ARCHIVE/03_Failed_or_Partial_Research/README.md` |
| 72 | YES | 13 | `TIER_5` | `09_ARCHIVE/03_Failed_or_Partial_Research/VibeGuard/Legacy_Fragments_and_Variants/research_on_f.patent_by_qwen2.md` |
| 70 | NO | — | `UNMAPPED_CONTROL_OR_POST_FREEZE` | `08_MASTER_MANUAL/02_Chapter_Source_Maps/13_Superseded_Failed_Partial_and_Archived_Routes_SOURCES.md` |
| 69 | YES | 13 | `TIER_5` | `09_ARCHIVE/03_Failed_or_Partial_Research/TrueMoist/SUPPLEMENTARY_EXCLUDED_TrueMoist_Work_Max_Web_Audit.md` |
| 68 | YES | 13 | `TIER_5` | `09_ARCHIVE/03_Failed_or_Partial_Research/TrueMoist/Legacy_Fragments_and_Variants/research on f.patent by qwen #0.md` |
| 67 | YES | 13 | `TIER_5` | `09_ARCHIVE/03_Failed_or_Partial_Research/VibeGuard/Legacy_Fragments_and_Variants/research on f. patent by chatgpt.md` |
| 63 | YES | 13 | `TIER_5` | `09_ARCHIVE/03_Failed_or_Partial_Research/TrueMoist/Legacy_Fragments_and_Variants/research on f.patent by chatgpt high deeprserach.pdf` |
| 63 | YES | 13 | `TIER_5` | `09_ARCHIVE/03_Failed_or_Partial_Research/TrueMoist/Legacy_Fragments_and_Variants/reserach.md` |
| 63 | YES | 13 | `TIER_5` | `09_ARCHIVE/03_Failed_or_Partial_Research/VibeGuard/Legacy_Fragments_and_Variants/research on f.patent by mistral 2.md` |
| 63 | YES | 13 | `TIER_5` | `09_ARCHIVE/03_Failed_or_Partial_Research/VibeGuard/Legacy_Fragments_and_Variants/research on f.patent by mistral 3.md` |
| 63 | YES | 13 | `TIER_5` | `09_ARCHIVE/03_Failed_or_Partial_Research/VibeGuard/Legacy_Fragments_and_Variants/research on f.patent by mistral.pdf` |
| 63 | YES | 13 | `TIER_5` | `09_ARCHIVE/03_Failed_or_Partial_Research/VibeGuard/Legacy_Fragments_and_Variants/research on f.patent by qwen.md` |
| 61 | YES | 13 | `TIER_5` | `09_ARCHIVE/05_Unrelated_Quarantine/INTENTIONAL_EXCLUSIONS.md` |
| 59 | YES | 13 | `TIER_5` | `09_ARCHIVE/01_Superseded/Convenience_Folder_Variants/COPY PASTE FOLDER/Project_mC_Decision_Register_v1.0.md` |
| 59 | YES | 13 | `TIER_5` | `09_ARCHIVE/01_Superseded/TrueMoist/Earlier_Claude_Architecture/Project_mC_Decision_Register_v1_1.md` |
| 58 | YES | 13 | `TIER_5` | `09_ARCHIVE/03_Failed_or_Partial_Research/OpenBraille/Phase3C_Failed_Raw_Research/Phase3C_OpenBraille_Failed_Research_ChatGPT.pdf` |
| 57 | YES | 13 | `TIER_5` | `09_ARCHIVE/ARCHIVE_INDEX.md` |
| 56 | YES | 13 | `TIER_5` | `09_ARCHIVE/01_Superseded/TrueMoist/Phase3C_TrueMoist_PDR_Patch_Historical.md` |
| 55 | YES | 13 | `TIER_5` | `09_ARCHIVE/01_Superseded/TrueMoist/Earlier_Claude_Architecture/Phase3C_TrueMoist_Architecture_Report_by_Claude.md` |
| 54 | YES | 13 | `TIER_5` | `09_ARCHIVE/01_Superseded/Convenience_Folder_Variants/COPY PASTE FOLDER/MC_Project_PHASE_DOC.md` |
| 54 | YES | 13 | `TIER_5` | `09_ARCHIVE/01_Superseded/Convenience_Folder_Variants/every sop and memory/MC_Project_PHASE_DOC.md` |
| 54 | YES | 13 | `TIER_5` | `09_ARCHIVE/01_Superseded/Convenience_Folder_Variants/every sop and memory/README.md` |
| 50 | YES | 13 | `TIER_5` | `09_ARCHIVE/01_Superseded/Convenience_Folder_Variants/COPY PASTE FOLDER/README.md` |

### Chapter 14 — Source Integrity and Evidence Control

| Score | Source-map status | Existing chapter | Authority | Relative path |
|---:|---|---:|---|---|
| 61 | NO | — | `UNMAPPED_CONTROL_OR_POST_FREEZE` | `08_MASTER_MANUAL/02_Chapter_Source_Maps/14_Source_Integrity_Audit_and_Reproducibility_SOURCES.md` |
| 55 | YES | 14 | `TIER_5` | `00_START_HERE/01_STAGE1_GOVERNANCE_VALIDATION.md` |
| 53 | NO | — | `UNMAPPED_CONTROL_OR_POST_FREEZE` | `08_MASTER_MANUAL/02_Chapter_Source_Maps/A1_Appendix_A_Complete_Source_Register_SOURCES.md` |
| 50 | NO | — | `UNMAPPED_CONTROL_OR_POST_FREEZE` | `08_MASTER_MANUAL/00_Blueprint/MASTER_MANUAL_BLUEPRINT.md` |
| 50 | YES | 14 | `TIER_1` | `08_MASTER_MANUAL/01_Source_Index/SOURCE_FREEZE_NOTICE.md` |
| 49 | YES | 14 | `TIER_5` | `00_START_HERE/09_STAGE8_FINAL_ARCHIVAL_SWEEP_LOG.tsv` |
| 44 | YES | 14 | `TIER_5` | `00_START_HERE/01_STAGE1_GOVERNANCE_COPY_LOG.tsv` |
| 41 | YES | 14 | `TIER_5` | `00_START_HERE/02_STAGE2_PHASE_HISTORY_VALIDATION.md` |
| 41 | YES | 14 | `TIER_5` | `00_START_HERE/06_STAGE4B_TEACHER_AND_REVIEW_VALIDATION.md` |
| 41 | YES | 14 | `TIER_5` | `00_START_HERE/07_STAGE5_TRANSPORT_PROVENANCE_VALIDATION.md` |
| 41 | YES | 14 | `TIER_5` | `00_START_HERE/09_STAGE8_FINAL_ARCHIVAL_SWEEP_VALIDATION.md` |
| 40 | YES | 01 | `TIER_1` | `01_GOVERNANCE_AND_CONTROL/04_Repository_Control/Legacy_Audits_and_Snapshots/CLEANUP_VALIDATION_REPORT.md` |
| 40 | YES | 13 | `TIER_5` | `09_ARCHIVE/03_Failed_or_Partial_Research/TrueMoist/SUPPLEMENTARY_EXCLUDED_TrueMoist_Work_Max_Web_Audit.md` |
| 36 | YES | 14 | `TIER_5` | `00_START_HERE/03_STAGE3A_CONCEPT_ARCHITECTURE_VALIDATION.md` |
| 36 | YES | 14 | `TIER_5` | `00_START_HERE/04_STAGE3B_PATENT_EVIDENCE_VALIDATION.md` |
| 36 | YES | 14 | `TIER_5` | `00_START_HERE/05_STAGE4A_COMPARATIVE_DECISION_VALIDATION.md` |
| 36 | YES | 14 | `TIER_5` | `00_START_HERE/08_STAGE6A_HISTORICAL_RESEARCH_VALIDATION.md` |
| 36 | NO | — | `UNMAPPED_CONTROL_OR_POST_FREEZE` | `08_MASTER_MANUAL/05_Source_Extraction/07_Provenance_Archive_Integrity/PROVENANCE_ARCHIVE_INTEGRITY_EXTRACTION_REGISTER.tsv` |
| 35 | YES | 12 | `TIER_5` | `06_TRANSPORT_AND_PROVENANCE/02_Input_Manifests/VibeGuard_Synthesis_INPUT_MANIFEST.md` |
| 35 | YES | 12 | `TIER_5` | `06_TRANSPORT_AND_PROVENANCE/03_Launchers_and_Checklists/Codex_Workflows/CODEX_ORGANIZE_VIBEGUARD_SYNTHESIS_PACKAGE.txt` |
| 35 | NO | — | `UNMAPPED_CONTROL_OR_POST_FREEZE` | `08_MASTER_MANUAL/02_Chapter_Source_Maps/01_Project_Mandate_Requirements_and_Governance_SOURCES.md` |
| 35 | NO | — | `UNMAPPED_CONTROL_OR_POST_FREEZE` | `08_MASTER_MANUAL/02_Chapter_Source_Maps/08_TrueMoist_Architecture_Validation_and_Patent_Evidence_SOURCES.md` |
| 35 | NO | — | `UNMAPPED_CONTROL_OR_POST_FREEZE` | `08_MASTER_MANUAL/02_Chapter_Source_Maps/12_Research_Provenance_and_AI_Workflow_Control_SOURCES.md` |
| 35 | NO | — | `UNMAPPED_CONTROL_OR_POST_FREEZE` | `08_MASTER_MANUAL/05_Source_Extraction/01_Tier1_Tier2_Core/01/9678c5072d86__Project_mC_Decision_Register_v1.2.md` |
| 34 | NO | — | `UNMAPPED_CONTROL_OR_POST_FREEZE` | `08_MASTER_MANUAL/05_Source_Extraction/01_Tier1_Tier2_Core/01/975767d50bf2__CLEANUP_VALIDATION_REPORT.md` |

## Control result

- Frozen source-map records checked: **301**
- Eligible workspace files scanned: **393**
- Candidate chapter assignments produced: **482**
- Candidate register: `08_MASTER_MANUAL/04_Validation/Stage10R_R_Coverage_Repair_Audit/PROVENANCE_ARCHIVE_INTEGRITY_COVERAGE_CANDIDATES.tsv`
- Original repository files modified: **0**
- Frozen source map modified: **No**
- Archives expanded: **0**
- Files deleted: **0**

**STAGE 10R-R AUDIT COMPLETE. Do not begin Chapters 12–14 reconciliation until the candidate register is reviewed and a controlled supplemental source set is frozen.**
