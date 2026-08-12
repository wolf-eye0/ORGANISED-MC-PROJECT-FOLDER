# Naming and Placement Issues

## Material issues

| Path | Finding | Impact | Priority |
|---|---|---|---|
| `.../vibeguard/research/Phase3C_VibeGuard_Architecture_Report By Claude.md` | Final Level-4 report is inside raw-research folder. | Authority and discoverability risk. | Mandatory correction after approval |
| `.../openbraille/Researches/DEEpr research on phase 3c openbraille by chatgpt` | File is actually PDF, lacks extension, name does not identify failed/generic content. | Tooling, security triage, and evidence-validity risk. | Mandatory correction after approval |
| `.../PHASE 3A.../phase3B_report_and_summary.zip` | Contains `Claudes report on the research Phases 3a.pdf` and `Phase3A_MEMORY.md`. | Filename falsely says Phase 3B. | Mandatory correction after approval |
| `Project_mC_Decision_Register_v1.0.md.save` | Historical register has editor-backup suffix rather than a clear historical label. | May be mistaken for recovery debris or current authority. | Mandatory labeling correction |
| `CURRENT_FOLDER_STRUCTURE.txt` | Lists absent `key.txt` and cannot distinguish empty `main/` from a file; predates audit guidance/v1.2 state. | Misleading inventory/security snapshot. | Mandatory regeneration after approved cleanup |
| `PHASE 2/RESEARCH DOCS/QWen Research on Patent.pdf` and `Qwens Research on Phase 2.md` | Substantial but non-equivalent overlap; inconsistent names conceal that Markdown is likely a subset. | Duplicate/scope ambiguity. | Manual review before renaming |
| `PHASE 2/Phase2_Report From Claude.pdf` versus `Phase2_Report by CLaude.md` | Near-equivalent cross-format pair uses inconsistent wording/capitalization. | Minor canonical-format ambiguity. | Label derivative; no deletion |
| `.../vibeguard/claude_synthesis_prompt.mmd` | Extracted prose is text-identical to `.md`; `.mmd` conventionally implies Mermaid. | Misleading extension. | Manual confirmation, then optional removal from active set or rename |

## Inconsistent research folder names

- `PHASE 1/PHASE 1.A/RESEARCHS/`
- `PHASE 2/RESEARCH DOCS/`
- `.../openbraille/Researches/`
- `.../vibeguard/research/`
- `.../TrueMoist/Research/`

These are inconsistent but understandable. Normalizing all of them is cosmetic and would cause link/path churn. Defer unless the owner approves a narrow Phase 3C-only normalization.

## Other naming inconsistencies

- Concept directory casing differs: `openbraille`, `vibeguard`, `TrueMoist`.
- Phase labels differ: `PHASE 1.A`, `PHASE 1.B`, `PHASE 1B.5`, and verbose Phase 3 names.
- Numerous typos exist: `Reearch`, `Rsearch`, `RESEAARCH`, `researon`, `reserach`, `whoel`, `CHATGT`, and inconsistent `QWen/Qwen/QWEN`.
- `Claudes report for openbraille phase 3c.md` is authoritative but its conversational name does not say “Architecture Report.”
- `COPY PASTE FOLDER` and `every sop and memory` describe convenience usage informally rather than signaling non-authority.

These are discoverability issues, not evidence of duplication. Bulk renaming is not recommended.

## Link result

No actual Markdown or HTML local links were found, hence none tested as broken. Filename mentions inside backticks are plain text references. If approved moves occur later, update those references even though they are not clickable links.

## Names that misdescribe content

- The failed OpenBraille ChatGPT output describes a universal research method, not OpenBraille.
- `phase3B_report_and_summary.zip` contains Phase 3A files.
- The `.mmd` VibeGuard file contains prose prompt content, not a Mermaid diagram.
- `CURRENT_FOLDER_STRUCTURE.txt` is not current.
- Root `MC_Project_PHASE_DOC.md` is “Frozen” methodology but its progress table is not current project state; the filename itself is acceptable, while the status content needs controlled correction.
