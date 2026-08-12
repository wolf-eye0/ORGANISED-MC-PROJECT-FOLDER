# Project mC Repository Organization Audit

**Audit date:** 2026-07-29  
**Scope:** Current working tree, excluding `.git/` internals and the newly created `REPOSITORY_AUDIT/` outputs.  
**Mode:** Audit only; no existing project file or directory was moved, renamed, edited, deleted, or executed.

## Executive finding

The owner-designed Phase 1 / Phase 2 / Phase 3 hierarchy is coherent and should be preserved. The main organization problem is not the hierarchy; it is ambiguity created by convenience copies, embedded ZIP copies, stale governance/context snapshots, one misplaced final report, one extensionless failed-research PDF, and inconsistent naming.

At audit start, the repository had **124 files**, all tracked, with a clean Git working tree. The population comprises 74 Markdown files, 21 PDFs, 16 DOCX files, 6 ZIP files, 2 HTML files, one MMD file, one `.save`, one TXT file, `.gitignore`, and the extensionless-PDF special case. The seven audit outputs are intentionally excluded from those counts and from the manifest population.

## Current hierarchy assessment

```text
PROJECT/
├── PHASE 1/
│   ├── PHASE 1.A/
│   ├── PHASE 1.B/
│   ├── PHASE 1B.5/
│   └── PHASE 1C/
├── PHASE 2/
│   └── RESEARCH DOCS/
├── PHASE 3/
│   ├── PHASE 3A-Engineering Landscape Discovery/
│   ├── PHASE 3B-Engineering Feasibility Analysis/
│   └── PHASE 3C-Comparative Technical Evaluation/
│       ├── openbraille/
│       ├── vibeguard/
│       └── TrueMoist/
├── COPY PASTE FOLDER/                 # convenience/context copies
├── every sop and memory/              # convenience/context copies
├── contexts.zip                       # convenience/context package
├── main/                              # empty directory, not a file
└── root governance/context files
```

This structure correctly preserves the project’s chronological pipeline. Phase 3C contains only the retained concepts OpenBraille, VibeGuard, and TrueMoist; TrustLatch and ColdTrace remain represented historically in earlier phases and governance records, consistent with deferral rather than rejection.

## What is working

- Canonical phase artifacts generally live in their phase directories.
- The four highest-priority governance records are present at their expected canonical paths.
- The current Decision Register is clearly versioned as v1.2 and records Phase 3C closure for the retained shortlist.
- Raw research remains preserved for methodology traceability.
- Exact hashing makes most convenience duplication unambiguous.
- All 21 `.pdf` files plus the extensionless PDF were text-extractable with the installed `pdftotext`; all 16 DOCX packages passed ZIP-integrity checks and their text was inspected directly from `word/document.xml`. No software was installed.

## Main structural risks

1. `COPY PASTE FOLDER/`, `every sop and memory/`, and ZIPs repeat canonical artifacts without local warning labels.
2. `MC_Project_PHASE_DOC.md` v2.0 still says Phase 3 is pending, conflicting with the newer EDR, Decision Register v1.2, and closure memo.
3. `CURRENT_FOLDER_STRUCTURE.txt` is stale: it lists `key.txt` and visually lists `main` without revealing that `main` is an empty directory.
4. The VibeGuard final architecture report is placed under `vibeguard/research/` beside raw evidence.
5. OpenBraille’s failed ChatGPT output is a PDF with no `.pdf` extension and a generic, mis-scoped research framework as its content.
6. Phase/folder naming is inconsistent but mostly cosmetic; wholesale normalization would create needless churn.

## Link audit

No Markdown inline links/images or HTML `href`/`src` references were present in the audited files, so no syntactically broken relative links were found. Backticked filenames in governance documents are references, not clickable Markdown links; their basename-only form is a discoverability weakness but not a broken-link result.

## Audit limitations

- Binary equality is definitive; cross-format equivalence is not assumed.
- PDF and DOCX text extraction can lose layout, tables, footnotes, and images.
- ZIP members were streamed for listing and hashing only; no archive was extracted into the repository.
- The empty `main/` directory has no file hash and is not represented in the file-only CSV; it is covered in the security report.
