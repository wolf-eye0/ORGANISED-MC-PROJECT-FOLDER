# Phase 3C Naming Proposal

**Scope:** `PHASE 3/PHASE 3C-Comparative Technical Evaluation/` only  
**Mode:** Naming audit and proposal only; no directory or file was renamed, moved, edited, deleted, or merged.

## Proposed convention

Use:

```text
Phase3C_<Concept>_<DocumentType>_<SourceOrStatus>.<extension>
```

Controlled values proposed here:

- `<Concept>`: `OpenBraille`, `VibeGuard`, `TrueMoist`, or `Portfolio` for the cross-concept closure memo.
- `<DocumentType>`:
  - `ArchitectureReport`
  - `Memory`
  - `SOP`
  - `DeepResearchPrompt`
  - `SynthesisPrompt`
  - `RawResearch`
  - `FailedResearch`
  - `PDRPatch`
  - `ClosureMemo`
- `<SourceOrStatus>`:
  - `Final` for completed authoritative/supporting project artifacts;
  - `Approved` for the approved portfolio closure memo;
  - the source name (`Claude`, `Gemini`, `Mistral`, `Perplexity`, `Qwen`, `ChatGPT`) for prompts and independent research.

The convention deliberately keeps the original extension. It does not assert cross-format equivalence and does not authorize consolidation.

## Proposed directory names

| Current directory | Proposed directory | Reason | Risk | Classification |
|---|---|---|---|---|
| `.../openbraille/` | `.../OpenBraille/` | Standard concept casing. | **High:** case-only rename; unsafe as a one-step operation on case-insensitive filesystems. Use a unique temporary directory and two `git mv` operations if approved. | Cosmetic |
| `.../vibeguard/` | `.../VibeGuard/` | Standard concept casing. | **High:** case-only rename; use a unique temporary directory and two `git mv` operations. | Cosmetic |
| `.../TrueMoist/` | unchanged | Already uses standard concept casing. | Low. | No change |
| `.../openbraille/Researches/` | `.../OpenBraille/research/` | Standard raw-research folder name; removes plural inconsistency. | Medium: parent is also case-renamed; sequence operations carefully. | Cosmetic |
| `.../vibeguard/research/` | `.../VibeGuard/research/` | Folder name already standard; only parent casing changes. | High only because of parent case-only rename. | Cosmetic |
| `.../TrueMoist/Research/` | `.../TrueMoist/research/` | Standard raw-research folder casing. | **High:** case-only rename; use a unique temporary directory and two `git mv` operations. | Cosmetic |

`CURRENT_FOLDER_STRUCTURE.txt` must be regenerated after any approved naming implementation. Root README links and all path-bearing references identified below must then be updated.

## Portfolio-level file

| Current path | Proposed path | Reason | Authority level | References requiring update | Risk | Mandatory or cosmetic |
|---|---|---|---|---|---|---|
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/Phase3C_Retained_Portfolio_Closure_Memo.md` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/Phase3C_Portfolio_ClosureMemo_Approved.md` | Fits the convention and makes cross-concept scope and approved status explicit. | Level 3 — retained-portfolio closure memo | `AGENTS.md:48`; `README.md:28,44`; `CURRENT_FOLDER_STRUCTURE.txt:127`. Historical audit mention: `REPOSITORY_AUDIT/04_AUTHORITY_AMBIGUITIES.md:7`. | Medium: high-authority path used by governance/navigation. | Mandatory for the proposed system |

## OpenBraille files

All proposed paths below use `.../OpenBraille/` and `.../OpenBraille/research/`.

| Current path | Proposed path | Reason | Authority level | References requiring update | Risk | Mandatory or cosmetic |
|---|---|---|---|---|---|---|
| `.../openbraille/Claudes report for openbraille phase 3c.md` | `.../OpenBraille/Phase3C_OpenBraille_ArchitectureReport_Final.md` | Identifies the Level-4 artifact as the final architecture report rather than a conversational “Claude report.” | Level 4 — final Phase 3C architecture report | `Project_mC_Decision_Register_v1.2.md:162,383,397,411,425,439,453,467,482,965`; `README.md:48`; `CURRENT_FOLDER_STRUCTURE.txt:110`. Historical v1.0 and convenience-register mentions should be reviewed under historical-record policy, not silently rewritten. | High: many PDR source-evidence references. | Mandatory |
| `.../openbraille/Phase3C_OpenBraille_Claude_Synthesis_Prompt.md` | `.../OpenBraille/Phase3C_OpenBraille_SynthesisPrompt_Claude.md` | Standard prompt document type and source ordering. | Supporting Phase 3C prompt | `Project_mC_Decision_Register_v1.2.md:965`; `CURRENT_FOLDER_STRUCTURE.txt:111`. Historical v1.0 and convenience-register references also exist. | Medium. | Cosmetic |
| `.../openbraille/Phase3C_OpenBraille_DeepResearch_Prompt.md` | `.../OpenBraille/Phase3C_OpenBraille_DeepResearchPrompt_Final.md` | Standard prompt tokenization and completed status. | Supporting Phase 3C prompt | `CURRENT_FOLDER_STRUCTURE.txt:112`. | Low. | Cosmetic |
| `.../openbraille/Phase3C_OpenBraille_Memory.md` | `.../OpenBraille/Phase3C_OpenBraille_Memory_Final.md` | Aligns memory status with the completed Phase 3C portfolio. | Level 5 — Phase 3C memory | `Project_mC_Decision_Register_v1.2.md:383,397,411,425,439,453,482`; `README.md:54`; `CURRENT_FOLDER_STRUCTURE.txt:113`; current synthesis prompt line 790; current architecture report line 323. Historical v1.0 and convenience-register references also exist. | High: multiple current PDR and internal references. | Mandatory |
| `.../openbraille/Phase3C_OpenBraille_SOP.md` | `.../OpenBraille/Phase3C_OpenBraille_SOP_Final.md` | Makes the completed SOP status explicit. | Phase 3C methodology/SOP | `CURRENT_FOLDER_STRUCTURE.txt:114`; current Mistral raw research line 1172. | Medium: raw-research text contains a filename reference. | Cosmetic |
| `.../openbraille/Researches/FAILED_ChatGPT_Generic_Deep_Research_Framework.pdf` | `.../OpenBraille/research/Phase3C_OpenBraille_FailedResearch_ChatGPT.pdf` | Preserves failed evidence while making phase, concept, role, and source explicit. | Level 10 — failed/mis-scoped research; excluded as valid evidence | `CURRENT_FOLDER_STRUCTURE.txt:105`. Historical cleanup records in `REORGANIZATION_LOG.md`, `CLEANUP_VALIDATION_REPORT.md`, and `REPOSITORY_AUDIT/07_MINIMAL_CLEANUP_PROPOSAL.md` should normally retain the path they recorded. | Medium: prior cleanup history intentionally records the current path. | Mandatory |
| `.../openbraille/Researches/Perplexity research on phase 3C.docx` | `.../OpenBraille/research/Phase3C_OpenBraille_RawResearch_Perplexity.docx` | Standard raw-research role and source. | Level 10 — raw research | `CURRENT_FOLDER_STRUCTURE.txt:106`. | Low. | Cosmetic |
| `.../openbraille/Researches/gemini research on phase 3c.docx` | `.../OpenBraille/research/Phase3C_OpenBraille_RawResearch_Gemini.docx` | Standard raw-research role/source; removes ambiguous same-name collision with VibeGuard. | Level 10 — raw research | `CURRENT_FOLDER_STRUCTURE.txt:107` (basename also matches VibeGuard at line 118; update by full path, not blind replacement). | Medium: identical basename exists under VibeGuard. | Cosmetic |
| `.../openbraille/Researches/mistral research on phase 3c.md` | `.../OpenBraille/research/Phase3C_OpenBraille_RawResearch_Mistral.md` | Standard raw-research role and source. | Level 10 — raw research | `CURRENT_FOLDER_STRUCTURE.txt:108`. | Low. | Cosmetic |
| `.../openbraille/Researches/qwen Research on phase 3C.md` | `.../OpenBraille/research/Phase3C_OpenBraille_RawResearch_Qwen.md` | Standard raw-research role and source. | Level 10 — raw research | `CURRENT_FOLDER_STRUCTURE.txt:109`. | Low. | Cosmetic |

## VibeGuard files

All proposed paths below use `.../VibeGuard/` and `.../VibeGuard/research/`.

| Current path | Proposed path | Reason | Authority level | References requiring update | Risk | Mandatory or cosmetic |
|---|---|---|---|---|---|---|
| `.../vibeguard/Phase3C_VibeGuard_Architecture_Report_By_Claude.md` | `.../VibeGuard/Phase3C_VibeGuard_ArchitectureReport_Final.md` | Standard architecture-report token and authoritative final status. | Level 4 — final Phase 3C architecture report | `Project_mC_Decision_Register_v1.2.md:497,511,525,539,553,567,581,595,609,623,951,965`; `README.md:49`; `CURRENT_FOLDER_STRUCTURE.txt:121`. Cleanup/audit records should normally retain historical mappings. | High: many current PDR source-evidence references. | Mandatory |
| `.../vibeguard/Phase3C_VibeGuard_DeepResearch_Prompt.md` | `.../VibeGuard/Phase3C_VibeGuard_DeepResearchPrompt_Final.md` | Standard prompt tokenization and completed status. | Supporting Phase 3C prompt | `CURRENT_FOLDER_STRUCTURE.txt:122`; current VibeGuard SOP line 489. | Medium. | Cosmetic |
| `.../vibeguard/Phase3C_VibeGuard_Memory.md` | `.../VibeGuard/Phase3C_VibeGuard_Memory_Final.md` | Makes completed memory status explicit. | Level 5 — Phase 3C memory | `Project_mC_Decision_Register_v1.2.md:497,581,595,609,623`; `README.md:55`; `CURRENT_FOLDER_STRUCTURE.txt:123`; current SOP line 493; current Mistral raw research line 1255. Historical v1.0 and convenience-register references also exist. | High. | Mandatory |
| `.../vibeguard/claude_synthesis_prompt.md` | `.../VibeGuard/Phase3C_VibeGuard_SynthesisPrompt_Claude.md` | Standard phase/concept/document/source naming. | Supporting Phase 3C prompt | `CURRENT_FOLDER_STRUCTURE.txt:124`. Historical audit mention: `REPOSITORY_AUDIT/03_DUPLICATE_REPORT.md:57`. | Medium: paired with a text-identical `.mmd`; do not merge. | Cosmetic |
| `.../vibeguard/claude_synthesis_prompt.mmd` | `.../VibeGuard/Phase3C_VibeGuard_SynthesisPrompt_Claude.mmd` | Standardizes the basename while preserving the separate file and extension. | Supporting Phase 3C prompt/alternate representation | `CURRENT_FOLDER_STRUCTURE.txt:125`. Historical audit mentions: `REPOSITORY_AUDIT/03_DUPLICATE_REPORT.md:58`, `REPOSITORY_AUDIT/05_NAMING_AND_PLACEMENT_ISSUES.md:14`. | **High:** `.mmd` usually implies Mermaid, while prior audit found prose identical to `.md`; manual tool-use review required. No merge authorized. | Cosmetic, manual review first |
| `.../vibeguard/vibeguard_sop.md` | `.../VibeGuard/Phase3C_VibeGuard_SOP_Final.md` | Standard phase/concept/SOP/status naming. | Phase 3C methodology/SOP | `Project_mC_Decision_Register_v1.2.md:950`; `CURRENT_FOLDER_STRUCTURE.txt:126`; current memory lines 27,81,90; current architecture report lines 6,21,160. Historical v1.0 and convenience-register references also exist. | High: internal and governance references. | Mandatory |
| `.../vibeguard/research/Perplexity research on phase 3c.md` | `.../VibeGuard/research/Phase3C_VibeGuard_RawResearch_Perplexity.md` | Standard raw-research role and source. | Level 10 — raw research | `CURRENT_FOLDER_STRUCTURE.txt:117`. | Low. | Cosmetic |
| `.../vibeguard/research/gemini research on phase 3c.docx` | `.../VibeGuard/research/Phase3C_VibeGuard_RawResearch_Gemini.docx` | Standard raw-research role/source; removes ambiguous same-name collision with OpenBraille. | Level 10 — raw research | `CURRENT_FOLDER_STRUCTURE.txt:118` (basename also matches OpenBraille at line 107; update by full path). | Medium: identical basename exists under OpenBraille. | Cosmetic |
| `.../vibeguard/research/mistral reserach on phase 3c.md` | `.../VibeGuard/research/Phase3C_VibeGuard_RawResearch_Mistral.md` | Standard raw-research role/source and corrects filename typo only. | Level 10 — raw research | `CURRENT_FOLDER_STRUCTURE.txt:119`. | Low. | Cosmetic |
| `.../vibeguard/research/qwens research on phase 3c.md` | `.../VibeGuard/research/Phase3C_VibeGuard_RawResearch_Qwen.md` | Standard raw-research role and source spelling. | Level 10 — raw research | `CURRENT_FOLDER_STRUCTURE.txt:120`. | Low. | Cosmetic |

## TrueMoist files

All proposed raw-research paths below use `.../TrueMoist/research/`.

| Current path | Proposed path | Reason | Authority level | References requiring update | Risk | Mandatory or cosmetic |
|---|---|---|---|---|---|---|
| `.../TrueMoist/Phase3C_TrueMoist_ChatGPT_Final_Synthesis.md` | `.../TrueMoist/Phase3C_TrueMoist_ArchitectureReport_Final.md` | Identifies the authoritative synthesis by its Level-4 role rather than model source. | Level 4 — final Phase 3C architecture/synthesis report | `Project_mC_Decision_Register_v1.2.md:250,351,638,651,664,677,691,705,719,733,747,761`; `README.md:50`; `CURRENT_FOLDER_STRUCTURE.txt:97`; current memory line 6; current PDR patch line 6. Historical audit mention: `REPOSITORY_AUDIT/04_AUTHORITY_AMBIGUITIES.md:45`. | High: many current PDR references. | Mandatory |
| `.../TrueMoist/Phase3C_TrueMoist_DeepResearch_Prompt.md` | `.../TrueMoist/Phase3C_TrueMoist_DeepResearchPrompt_Final.md` | Standard prompt tokenization and completed status. | Supporting Phase 3C prompt | `CURRENT_FOLDER_STRUCTURE.txt:98`. | Low. | Cosmetic |
| `.../TrueMoist/Phase3C_TrueMoist_Final_Synthesis_Prompt.md` | `.../TrueMoist/Phase3C_TrueMoist_SynthesisPrompt_Final.md` | Standard document-type ordering. | Supporting Phase 3C prompt | `CURRENT_FOLDER_STRUCTURE.txt:99`. | Low. | Cosmetic |
| `.../TrueMoist/Phase3C_TrueMoist_MEMORY_Final.md` | `.../TrueMoist/Phase3C_TrueMoist_Memory_Final.md` | Standard token casing without changing status. | Level 5 — Phase 3C memory | `Project_mC_Decision_Register_v1.2.md:638,691,705,733,747,761`; `README.md:56`; `CURRENT_FOLDER_STRUCTURE.txt:100`. | **High:** filename change is case-only (`MEMORY`→`Memory`) on a case-insensitive filesystem; use a temporary name. | Mandatory |
| `.../TrueMoist/Phase3C_TrueMoist_PDR_Update_Patch.md` | `.../TrueMoist/Phase3C_TrueMoist_PDRPatch_Final.md` | Clearly identifies the document as a PDR patch while fitting the convention. | Supporting historical PDR patch; not the current Decision Register | `CURRENT_FOLDER_STRUCTURE.txt:101`. | Low. | Cosmetic |
| `.../TrueMoist/Phase3C_TrueMoist_SOP.md` | `.../TrueMoist/Phase3C_TrueMoist_SOP_Final.md` | Makes completed SOP status explicit. | Phase 3C methodology/SOP | `CURRENT_FOLDER_STRUCTURE.txt:13,102`; current Perplexity raw research line 821. Historical exact-copy/audit references also exist. | Medium: convenience copy has the same basename and must not be blindly renamed or edited. | Cosmetic |
| `.../TrueMoist/Research/TrueMoist  3C Gemini REsearch.docx` | `.../TrueMoist/research/Phase3C_TrueMoist_RawResearch_Gemini.docx` | Standard raw-research role/source and removes spacing/capitalization errors. | Level 10 — raw research | `CURRENT_FOLDER_STRUCTURE.txt:93`. | Medium because parent folder rename is case-only. | Cosmetic |
| `.../TrueMoist/Research/TrueMoist Phase 3C  Research By chatgpt.pdf` | `.../TrueMoist/research/Phase3C_TrueMoist_RawResearch_ChatGPT.pdf` | Standard raw-research role/source and removes double spaces. | Level 10 — raw research | `CURRENT_FOLDER_STRUCTURE.txt:94`. | Medium because parent folder rename is case-only. | Cosmetic |
| `.../TrueMoist/Research/TrueMoist Phase 3C By Perplexity.md` | `.../TrueMoist/research/Phase3C_TrueMoist_RawResearch_Perplexity.md` | Standard raw-research role and source. | Level 10 — raw research | `CURRENT_FOLDER_STRUCTURE.txt:95`. | Medium because parent folder rename is case-only. | Cosmetic |
| `.../TrueMoist/Research/phase-3c-truemoist-Research-Mistral.md` | `.../TrueMoist/research/Phase3C_TrueMoist_RawResearch_Mistral.md` | Standard raw-research role/source and separator style. | Level 10 — raw research | `CURRENT_FOLDER_STRUCTURE.txt:96`. | Medium because parent folder rename is case-only. | Cosmetic |

## Reference-update policy if approved

### Operational references that should be updated

- `README.md`
- `AGENTS.md` where it names the closure memo path
- `Project_mC_Decision_Register_v1.2.md`, changing only source-evidence filenames
- Internal Phase 3C filename/path references in SOPs, memories, prompts, reports, raw-research text, and the TrueMoist PDR patch
- `CURRENT_FOLDER_STRUCTURE.txt`, by regeneration after all approved changes

### Historical records that should not be blindly rewritten

- `Project_mC_Decision_Register_v1.0_HISTORICAL.md`
- `COPY PASTE FOLDER/Project_mC_Decision_Register_v1.0.md`
- `REORGANIZATION_LOG.md`
- `CLEANUP_VALIDATION_REPORT.md`
- `REPOSITORY_AUDIT/`

These record earlier names or historical decisions. If the owner wants current-path annotations, add them explicitly rather than replacing historical evidence silently.

## Case-insensitive filesystem safety

The following are case-only renames and must not be attempted as a single rename on case-insensitive filesystems:

1. `openbraille/` → `OpenBraille/`
2. `vibeguard/` → `VibeGuard/`
3. `TrueMoist/Research/` → `TrueMoist/research/`
4. `Phase3C_TrueMoist_MEMORY_Final.md` → `Phase3C_TrueMoist_Memory_Final.md`

If approved, use collision-free temporary paths, for example:

```text
git mv openbraille __tmp_OpenBraille
git mv __tmp_OpenBraille OpenBraille
```

Use a different unique temporary name for each operation, verify the destination does not exist, and record both steps in the reorganization log. Directory renames should occur before final file renames or be planned as one explicit mapping set to avoid path ambiguity.

## Summary

- Files inventoried: **31**
- Portfolio-level file: **1**
- OpenBraille files: **10**
- VibeGuard files: **10**
- TrueMoist files: **10**
- Proposed content changes: **none**
- Proposed deletions/merges: **none**
- Case-only operations requiring special handling: **4**

The highest-value mandatory changes are the names of the three final architecture reports, the three memories, the VibeGuard SOP, the failed OpenBraille research file, and the approved closure memo. Directory casing and most raw-research filename normalization are cosmetic; they should be approved as a single bounded batch or deferred together.
