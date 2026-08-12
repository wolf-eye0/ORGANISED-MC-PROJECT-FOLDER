# Minimal Cleanup Proposal

## Governing approach

Preserve the existing Phase 1 / Phase 2 / Phase 3 hierarchy. Do not merge documents merely because names or extracted text are similar. Treat convenience collections as packages, not canonical sources. Every approved move should use `git mv`, be recorded in `REORGANIZATION_LOG.md`, and be followed by reference/link checks.

No proposal below was executed.

## Mandatory corrections (after explicit owner approval)

### 1. Move the VibeGuard final architecture report out of raw research

`PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/research/Phase3C_VibeGuard_Architecture_Report By Claude.md`  
→ `PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/Phase3C_VibeGuard_Architecture_Report_By_Claude.md`

Reason: it is a Level-4 final architecture report cited by the latest Decision Register, not raw evidence.

### 2. Label and restore the extension of failed OpenBraille research

`PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Researches/DEEpr research on phase 3c openbraille by chatgpt`  
→ `PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Researches/FAILED_ChatGPT_Generic_Deep_Research_Framework.pdf`

Reason: preserve methodology traceability while preventing accidental use as OpenBraille evidence.

### 3. Correct the Phase 3A ZIP’s inaccurate name

`PHASE 3/PHASE 3A-Engineering Landscape Discovery/phase3B_report_and_summary.zip`  
→ `PHASE 3/PHASE 3A-Engineering Landscape Discovery/Phase3A_report_and_memory.zip`

Reason: both archive members are Phase 3A artifacts.

### 4. Clearly label the historical Decision Register

`Project_mC_Decision_Register_v1.0.md.save`  
→ `Project_mC_Decision_Register_v1.0_HISTORICAL.md`

Reason: v1.2 is authoritative; `.save` is ambiguous. Preserve all PDR identifiers and content unchanged.

### 5. Add authority notices without restructuring

Create short notice/README files in `COPY PASTE FOLDER/` and `every sop and memory/`, and a root archive note for ZIPs, stating that these are convenience/context packages and linking to canonical paths. Do not move their existing contents merely to enforce visual tidiness.

### 6. Correct stale navigation/security metadata

- Regenerate `CURRENT_FOLDER_STRUCTURE.txt` after approved moves; explicitly distinguish `main/` as a directory and omit absent `key.txt`.
- Reduce `.gitignore`’s three identical `key.txt` lines to one.
- Expand root `README.md` with the authority order and direct canonical paths.
- Update only the progress/status block of `MC_Project_PHASE_DOC.md` through a controlled owner-approved edit; do not rewrite methodology or technical conclusions.
- Add an explicit “historical/superseded” banner to retained v1.0 Register copies if they remain readily visible.

These are content edits, not path mappings.

## Mandatory manual review before any consolidation

### Phase 2 Qwen formats

Keep both files until a reviewer maps sections and determines why the Markdown is substantially shorter:

`PHASE 2/RESEARCH DOCS/QWen Research on Patent.pdf`  
→ no move proposed yet

`PHASE 2/RESEARCH DOCS/Qwens Research on Phase 2.md`  
→ no move proposed yet

If the Markdown is confirmed as an excerpt, rename it to say so; if it is a revision, add version metadata. Do not delete either based on similarity alone.

### Claude Phase 2 formats

Treat `Phase2_Report by CLaude.md` as the editable canonical source and `Phase2_Report From Claude.pdf` as the rendered companion. Retain both if both formats are useful; a small sidecar note is enough. No move is required.

### VibeGuard `.md` / `.mmd` prompt

The extracted text is identical. Confirm whether `.mmd` has any intended tool-specific use. If not, preserve it in history and remove it from the active working set only under a separately approved, recoverable cleanup; no deletion is authorized by this audit.

## Optional cosmetic renaming — defer by default

These changes improve consistency but do not solve authority or security problems. Undertake only as a single approved batch with reference updates:

`.../openbraille/Researches/` → `.../openbraille/research/`  
`.../TrueMoist/Research/` → `.../TrueMoist/research/`  
`.../PHASE 3C.../openbraille/` → `.../PHASE 3C.../OpenBraille/`  
`.../PHASE 3C.../vibeguard/` → `.../PHASE 3C.../VibeGuard/`

Individual typo corrections (`Reearch`, `Rsearch`, `reserach`, etc.) are also optional. Avoid wholesale Phase 1 folder renaming; the existing hierarchy is owner-designed and understandable.

## Convenience archive policy

- Keep canonical normal files in their existing phase paths.
- Mark ZIPs and convenience folders as non-canonical.
- Do not delete ZIPs merely because 22 of 23 archive members match normal files.
- Record that `contexts.zip` includes a unique older `MC_Project_PHASE_DOC.md` snapshot; preserve it as historical context, not current governance.
- Consider moving convenience ZIPs only if the owner later approves a dedicated archival policy; this audit does not propose a replacement folder structure.

## Empty `main/` directory

Confirm intent. If it is accidental, the owner may remove the empty directory later; Git does not track it and there is no project-file content to preserve. No action was taken and no execution was attempted.

## Recommended order

1. Approve the four material path mappings.
2. Create `REORGANIZATION_LOG.md` and record each approved mapping.
3. Execute approved moves with `git mv`.
4. Add authority notices and minimal governance/status corrections.
5. Update basename references and check links.
6. Re-run hashes/manifest checks.
7. Consider cosmetic renaming only if discoverability remains a real problem.
