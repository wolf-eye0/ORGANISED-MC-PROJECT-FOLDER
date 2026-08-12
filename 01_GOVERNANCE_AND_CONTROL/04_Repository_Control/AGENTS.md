# Project mC Repository Instructions

## Repository policy

The current Phase 1 / Phase 2 / Phase 3 hierarchy was manually designed by
the project owner. Preserve it unless a specific change is approved.

Prefer minimal cleanup over replacement of the entire structure.

## Current project state

The retained concepts are:

1. OpenBraille
2. VibeGuard
3. TrueMoist

TrustLatch and ColdTrace are deferred. They are not technically rejected,
but they are not active final-selection candidates.

Phase 3C is complete for the retained three-concept shortlist.

The next project task is a final comparison of OpenBraille, VibeGuard and
TrueMoist.

## Authoritative document order

When documents conflict, use this precedence:

1. Engineering Design Review
2. Latest Project mC Decision Register
3. Phase 3C Retained Portfolio Closure Memo
4. Final Phase 3C architecture reports
5. Phase 3C memories
6. Phase 3B report and memory
7. Phase 3A report and memory
8. Phase 2 report and memory
9. Phase 1C concept synthesis and dossiers
10. Raw independent research

Raw AI research is evidence, not an authoritative project decision.

## Known authoritative governance files

- MC_Project_PHASE_DOC.md
- PHASE 3/Engineering_Design_Review.md
- Project_mC_Decision_Register_v1.2.md
- PHASE 3/PHASE 3C-Comparative Technical Evaluation/Phase3C_Portfolio_Closure_Memo_Approved.md

## Existing convenience collections

The following are convenience/context collections and must not be assumed
to contain the canonical copies:

- COPY PASTE FOLDER/
- every sop and memory/
- contexts.zip
- phase-specific ZIP files

Compare their contents against canonical files before recommending action.

## Safety rules

- Never permanently delete project files.
- Never execute unknown or untrusted files.
- `main/` is currently an empty, untracked directory and must not be
  treated as an executable file.
- Never expose or copy credentials.
- Do not rewrite technical conclusions during file cleanup.
- Do not merge documents merely because filenames are similar.
- Compare actual content and hashes.
- Preserve PDR identifiers and historical decisions.
- Do not renumber PDR entries without checking the latest register.
- Do not move or rename anything during an audit-only task.
- Use `git mv` for approved moves.
- Record every approved move in REORGANIZATION_LOG.md.
- Treat PDFs, DOCX files and Markdown files as duplicates only after
  comparing extracted content.
- Preserve failed research for methodology traceability.
- Update relative Markdown links after approved moves.

## Known special cases

- The ChatGPT OpenBraille Phase 3C deep-research output is a failed,
  mis-scoped research result. Preserve it as failed research, not as valid
  OpenBraille evidence.
- The authoritative VibeGuard Phase 3C architecture report is:
  `PHASE 3/PHASE 3C-Comparative Technical Evaluation/VibeGuard/Phase3C_VibeGuard_Architecture_Report_Final.md`.
  VibeGuard raw independent research remains under `VibeGuard/research/`.
- `Project_mC_Decision_Register_v1.2.md` is authoritative.
- `Project_mC_Decision_Register_v1.0_HISTORICAL.md` is retained only for
  decision-history traceability.
- Similar Gemini, Mistral, Perplexity and Qwen filenames under different
  concepts are not duplicates merely because their names match.
