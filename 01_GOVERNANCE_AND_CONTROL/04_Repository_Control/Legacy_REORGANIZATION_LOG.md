# Project mC Reorganization Log

This log records the owner-approved minimal cleanup. No general reorganization is authorized.

| Old path | New path | Reason | Action status |
|---|---|---|---|
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/research/Phase3C_VibeGuard_Architecture_Report By Claude.md` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/vibeguard/Phase3C_VibeGuard_Architecture_Report_By_Claude.md` | The authoritative final Phase 3C architecture report belongs at the VibeGuard concept root, not among raw research. | Completed with `git mv` |
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Researches/DEEpr research on phase 3c openbraille by chatgpt` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/openbraille/Researches/FAILED_ChatGPT_Generic_Deep_Research_Framework.pdf` | Preserve the extensionless, generic, mis-scoped PDF as clearly marked failed evidence. | Completed with `git mv` |
| `PHASE 3/PHASE 3A-Engineering Landscape Discovery/phase3B_report_and_summary.zip` | `PHASE 3/PHASE 3A-Engineering Landscape Discovery/Phase3A_report_and_memory.zip` | The archive contains Phase 3A report and memory files, not Phase 3B files. | Completed with `git mv` |
| `Project_mC_Decision_Register_v1.0.md.save` | `Project_mC_Decision_Register_v1.0_HISTORICAL.md` | Preserve v1.0 for traceability while clearly distinguishing it from authoritative v1.2. | Completed with `git mv`; historical banner added |

## Non-file item awaiting owner review

- `main/` is an empty, untracked directory. It was not removed or modified and remains awaiting owner review.

## Reference-update note

- Source-evidence references in the current `Project_mC_Decision_Register_v1.2.md` were updated to the new VibeGuard report filename.
- Matching old filename text remains intentionally preserved inside the historical v1.0 register and its convenience duplicate because historical PDR entries and convenience duplicates were explicitly out of scope for content changes.
