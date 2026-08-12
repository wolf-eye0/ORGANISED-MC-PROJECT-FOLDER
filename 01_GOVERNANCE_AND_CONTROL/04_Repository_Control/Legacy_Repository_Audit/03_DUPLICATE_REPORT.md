# Duplicate Report

## Method

- SHA-256 over each working-tree file identified exact binary duplicates.
- PDF text was extracted with the already-installed `pdftotext`.
- DOCX text was read from the package’s `word/document.xml`; packages were not expanded into the repository.
- Extracted text was whitespace/case normalized and compared with word-trigram overlap.
- Similar names alone were never used as duplicate evidence.

## Exact binary duplicates

There are **20 exact-duplicate groups**, covering **40 working-tree files**. Convenience copies are not proposed as canonical when an identical phase/root copy exists.

| Group | SHA-256 | Paths | Probable canonical file |
|---|---|---|---|
| ED-01 | `14c19ac85b56e4e27da03de534a2a574ab7220d90005b4a7a0afb868f6390478` | `COPY PASTE FOLDER/Phase3B_Report_by_Claude.md`<br>`PHASE 3/PHASE 3B-Engineering Feasibility Analysis/Phase3B_Report_by_Claude.md` | `PHASE 3/PHASE 3B-Engineering Feasibility Analysis/Phase3B_Report_by_Claude.md` |
| ED-02 | `2ecf77fbbba9966a7769a2e715034f6b9ff7362d7aa51261219ee118085d22d3` | `COPY PASTE FOLDER/Project_mC_Decision_Register_v1.0.md`<br>`Project_mC_Decision_Register_v1.0.md.save` | `Project_mC_Decision_Register_v1.0.md.save` |
| ED-03 | `305f0f568081ad8a01affc02d252a681f84abde5c23c2a9421fb69369ecc5540` | `PHASE 1/PHASE 1B.5/Phase1B5_Opportunity_Portfolio_Optimization.md`<br>`every sop and memory/Phase1B5_Opportunity_Portfolio_Optimization.md` | `PHASE 1/PHASE 1B.5/Phase1B5_Opportunity_Portfolio_Optimization.md` |
| ED-04 | `46f017501ac3ff9ebd6c1fb1e5ee8c068c22ddb08ae204c5609f2b759090295e` | `COPY PASTE FOLDER/Engineering_Design_Review.md`<br>`PHASE 3/Engineering_Design_Review.md` | `PHASE 3/Engineering_Design_Review.md` |
| ED-05 | `5a8943e1e556e1db0644cc7b75e2b4c8000b1a9506d673406c9c70cf7bb4a213` | `PHASE 1/PHASE 1.A/Phase1A_Memory.md`<br>`every sop and memory/Phase1A_Memory.md` | `PHASE 1/PHASE 1.A/Phase1A_Memory.md` |
| ED-06 | `783729d0e07e725236db5296dae8504ce782c294b8c61cfab40ea172cfa6943e` | `COPY PASTE FOLDER/Phase2_Report by CLaude.md`<br>`PHASE 2/Phase2_Report by CLaude.md` | `PHASE 2/Phase2_Report by CLaude.md` |
| ED-07 | `7b6532c779867e9d6064473de4ba1b4799a0c385361cf27dc4616888fb0ac7ad` | `COPY PASTE FOLDER/Phase3B_MEMORY.md`<br>`PHASE 3/PHASE 3B-Engineering Feasibility Analysis/Phase3B_MEMORY.md` | `PHASE 3/PHASE 3B-Engineering Feasibility Analysis/Phase3B_MEMORY.md` |
| ED-08 | `7d0202fb62476a0212e594af473ad8d796eecd853e53e7f0952de90908cec611` | `COPY PASTE FOLDER/Claudes report on the research Phases 3a.pdf`<br>`PHASE 3/PHASE 3A-Engineering Landscape Discovery/Claudes report on the research Phases 3a.pdf` | `PHASE 3/PHASE 3A-Engineering Landscape Discovery/Claudes report on the research Phases 3a.pdf` |
| ED-09 | `8e41493ddbc8b8b3c3ad8a00995b6ae3f8a5645351f8086a6b8ded92623853e4` | `PHASE 1/PHASE 1C/Phase1C.md`<br>`every sop and memory/Phase1C.md` | `PHASE 1/PHASE 1C/Phase1C.md` |
| ED-10 | `973519f45bc075c296d4302b94933288496bd9bc12fae708aac1fb7020158ce8` | `COPY PASTE FOLDER/Phase2_Memory.md`<br>`PHASE 2/Phase2_Memory.md` | `PHASE 2/Phase2_Memory.md` |
| ED-11 | `993caf1a05f3fdc3937efb634e2f2e467488e973eb71454db8e3c3f53d178d00` | `COPY PASTE FOLDER/Phase3C_TrueMoist_SOP.md`<br>`PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_SOP.md` | `PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_SOP.md` |
| ED-12 | `acd3b4178143ca918ed4cce43d3d853acc994c0178dc8efdc406fb014e1ec997` | `COPY PASTE FOLDER/Phase3A_MEMORY.md`<br>`PHASE 3/PHASE 3A-Engineering Landscape Discovery/Phase3A_MEMORY.md` | `PHASE 3/PHASE 3A-Engineering Landscape Discovery/Phase3A_MEMORY.md` |
| ED-13 | `c4b6c4a56bf8ba3066c5b426dce5ae4d50da4774478b5074566e9c79812e3ece` | `COPY PASTE FOLDER/MC_Project_PHASE_DOC.md`<br>`MC_Project_PHASE_DOC.md` | `MC_Project_PHASE_DOC.md` |
| ED-14 | `c52bed09fdfd1a860471bfc6d56cd41411f730362d12ee0348e07ad0939909c9` | `PHASE 1/PHASE 1.A/Phase1A_Summary.md`<br>`every sop and memory/Phase1A_Summary.md` | `PHASE 1/PHASE 1.A/Phase1A_Summary.md` |
| ED-15 | `d200473fd85a3cc910e3532bb2be662e0fcbdeab363fe988a948fd81d129c537` | `PHASE 1/PHASE 1B.5/Phase1B5_Memory.md`<br>`every sop and memory/Phase1B5_Memory.md` | `PHASE 1/PHASE 1B.5/Phase1B5_Memory.md` |
| ED-16 | `d58c91eead60c5abdb4e38c1e9b87c7449f4b3b68ccd7a23f5d4816fea16ff76` | `PHASE 1/PHASE 1.B/Phase1B_Memory.md`<br>`every sop and memory/Phase1B_Memory.md` | `PHASE 1/PHASE 1.B/Phase1B_Memory.md` |
| ED-17 | `e10d76b80c78554ff7e2ea75f3b263bfe82333c54418e7f794d249610f8fe130` | `PHASE 1/PHASE 1.B/Phase1B_Opportunity_Analysis.md`<br>`every sop and memory/Phase1B_Opportunity_Analysis.md` | `PHASE 1/PHASE 1.B/Phase1B_Opportunity_Analysis.md` |
| ED-18 | `e3b320245bc20d4312edc22b62fc9584059111e8fd38442277a3e5544ae019c1` | `PHASE 1/PHASE 1C/Phase1C_Memory.md`<br>`every sop and memory/Phase1C_Memory.md` | `PHASE 1/PHASE 1C/Phase1C_Memory.md` |
| ED-19 | `f520cb5201e299fb0f9185bd2b79318229b898e5a8ad7822deb9a073e8f6cae4` | `COPY PASTE FOLDER/PROJECT_CONCEPT_CONTEXT.md`<br>`PROJECT_CONCEPT_CONTEXT.md` | `PROJECT_CONCEPT_CONTEXT.md` |
| ED-20 | `f9a4184850435aba3ec26e480e802d1ba39f17037f0f368520a625c6f8e84f78` | `COPY PASTE FOLDER/Document_4_TrustLatch_Concept_Dossier.docx`<br>`PHASE 1/PHASE 1C/INDEPTH OF EACH FIVE IDEA/Document_4_TrustLatch_Concept_Dossier.docx` | `PHASE 1/PHASE 1C/INDEPTH OF EACH FIVE IDEA/Document_4_TrustLatch_Concept_Dossier.docx` |

## Cross-format / text-equivalent candidates

### CF-01 — Claude Phase 2 report

- `PHASE 2/Phase2_Report by CLaude.md`
- `PHASE 2/Phase2_Report From Claude.pdf`
- exact Markdown copy at `COPY PASTE FOLDER/Phase2_Report by CLaude.md`

Text was actually extracted and compared. PDF↔Markdown word-trigram Jaccard similarity is **0.9584** and containment is **0.9807**. This is strong evidence that the PDF is a rendered/near-equivalent form of the Markdown, with extraction/formatting differences. Probable canonical editable source: `PHASE 2/Phase2_Report by CLaude.md`; retain the PDF as a presentation derivative if needed.

### CF-02 — Qwen Phase 2 PDF/Markdown

- `PHASE 2/RESEARCH DOCS/QWen Research on Patent.pdf`
- `PHASE 2/RESEARCH DOCS/Qwens Research on Phase 2.md`

Text was extracted and compared. Jaccard similarity is **0.4785**, while **89.55%** of the Markdown’s word trigrams occur in the longer PDF. The PDF is about 160,646 normalized characters; Markdown is about 92,298. They substantially overlap, but are **not equivalent copies**: the Markdown appears to be a subset/variant and requires manual scope comparison. Do not delete or collapse either based on this audit.

### CF-03 — VibeGuard synthesis prompt `.md` / `.mmd`

- `.../vibeguard/claude_synthesis_prompt.md`
- `.../vibeguard/claude_synthesis_prompt.mmd`

Normalized extracted text is identical, but the binaries differ. The `.mmd` extension normally indicates Mermaid content, while this file is a prose synthesis prompt. Probable canonical file: the `.md` version. Manual confirmation is advised before any later cleanup.

## ZIP contents and duplication

Six ZIPs contain **23 members**. **22 of 23** members are byte-identical to normal working-tree files. Archives were listed and streamed for SHA-256 only.

| ZIP | Contained path | Size | Member SHA-256 | Matching normal repository file(s) |
|---|---|---:|---|---|
| `PHASE 1/PHASE 1.B/Phase1B_Opportunity_Analysis.zip` | `Phase1B_Opportunity_Analysis.md` | 5802 | `e10d76b80c78554ff7e2ea75f3b263bfe82333c54418e7f794d249610f8fe130` | `PHASE 1/PHASE 1.B/Phase1B_Opportunity_Analysis.md`<br>`every sop and memory/Phase1B_Opportunity_Analysis.md` |
| `PHASE 1/PHASE 1.B/Phase1B_Opportunity_Analysis.zip` | `Phase1B_Opportunity_Analysis_By_Claude.pdf` | 1484584 | `8e53b914163d8e2685d9edda7422e4c1ac1a01230e60e3a100a0e7ef514dd52c` | `PHASE 1/PHASE 1.B/Phase1B_Opportunity_Analysis_By_Claude.pdf` |
| `PHASE 2/Phase2_docs.zip` | `Phase2_Memory.md` | 7820 | `973519f45bc075c296d4302b94933288496bd9bc12fae708aac1fb7020158ce8` | `COPY PASTE FOLDER/Phase2_Memory.md`<br>`PHASE 2/Phase2_Memory.md` |
| `PHASE 2/Phase2_docs.zip` | `Phase2_Report by CLaude.md` | 44493 | `783729d0e07e725236db5296dae8504ce782c294b8c61cfab40ea172cfa6943e` | `COPY PASTE FOLDER/Phase2_Report by CLaude.md`<br>`PHASE 2/Phase2_Report by CLaude.md` |
| `PHASE 3/PHASE 3A-Engineering Landscape Discovery/phase3B_report_and_summary.zip` | `Claudes report on the research Phases 3a.pdf` | 792034 | `7d0202fb62476a0212e594af473ad8d796eecd853e53e7f0952de90908cec611` | `COPY PASTE FOLDER/Claudes report on the research Phases 3a.pdf`<br>`PHASE 3/PHASE 3A-Engineering Landscape Discovery/Claudes report on the research Phases 3a.pdf` |
| `PHASE 3/PHASE 3A-Engineering Landscape Discovery/phase3B_report_and_summary.zip` | `Phase3A_MEMORY.md` | 8898 | `acd3b4178143ca918ed4cce43d3d853acc994c0178dc8efdc406fb014e1ec997` | `COPY PASTE FOLDER/Phase3A_MEMORY.md`<br>`PHASE 3/PHASE 3A-Engineering Landscape Discovery/Phase3A_MEMORY.md` |
| `PHASE 3/PHASE 3B-Engineering Feasibility Analysis/Phase3B_mem_and_report.zip` | `Phase3B_MEMORY.md` | 18836 | `7b6532c779867e9d6064473de4ba1b4799a0c385361cf27dc4616888fb0ac7ad` | `COPY PASTE FOLDER/Phase3B_MEMORY.md`<br>`PHASE 3/PHASE 3B-Engineering Feasibility Analysis/Phase3B_MEMORY.md` |
| `PHASE 3/PHASE 3B-Engineering Feasibility Analysis/Phase3B_mem_and_report.zip` | `Phase3B_Report_by_Claude.md` | 83718 | `14c19ac85b56e4e27da03de534a2a574ab7220d90005b4a7a0afb868f6390478` | `COPY PASTE FOLDER/Phase3B_Report_by_Claude.md`<br>`PHASE 3/PHASE 3B-Engineering Feasibility Analysis/Phase3B_Report_by_Claude.md` |
| `contexts.zip` | `CHATGPT DEEP RESEARCH.md` | 20670 | `fa41ec5c0504aada478a754133290458a1333eee99542c4530d3fb2abc8f5ac0` | `PHASE 1/PHASE 1.A/RESEARCHS/CHATGPT DEEP RESEARCH.md` |
| `contexts.zip` | `GEMINI DEEP RESEARCH.docx` | 3035520 | `e527fa3ab029f3dd3096184c35f90ccd21e61bd520d9eb677f1031abbebd13ad` | `PHASE 1/PHASE 1.A/RESEARCHS/GEMINI DEEP RESEARCH.docx` |
| `contexts.zip` | `KIMI DEEP RESEARCH.docx` | 64142 | `c0d4cbeb9099d8a58c4fa6eab7e2f06aa1a0bda76affecb9444f040e8169828f` | `PHASE 1/PHASE 1.A/RESEARCHS/KIMI DEEP RESEARCH.docx` |
| `contexts.zip` | `MC_Project_PHASE_DOC.md` | 5872 | `35d5ca312c1e339f7edae9e26f58635762168267b07fd3ae5a6cb25fbd1d7512` | **No binary-identical normal file** |
| `contexts.zip` | `Phase1A_Summary.md` | 2794 | `c52bed09fdfd1a860471bfc6d56cd41411f730362d12ee0348e07ad0939909c9` | `PHASE 1/PHASE 1.A/Phase1A_Summary.md`<br>`every sop and memory/Phase1A_Summary.md` |
| `contexts.zip` | `QWEN AI DEEP RESEARCH.pdf` | 519844 | `5b3f7270de5bc6a27eba0e458cd2f7f40f55dd0407094f70ccfed6f6fd3f7ed8` | `PHASE 1/PHASE 1.A/RESEARCHS/QWEN AI DEEP RESEARCH.pdf` |
| `every sop and memory/every_sop_and memory_from phase 1A to 1C and whoel phase overview.zip` | `MC_Project_PHASE_DOC.md` | 6638 | `e7ebf127dac01b63c87713b14c0bd5cf2d4500e60581cc86f783abe92a525f98` | `every sop and memory/MC_Project_PHASE_DOC.md` |
| `every sop and memory/every_sop_and memory_from phase 1A to 1C and whoel phase overview.zip` | `Phase1A_Memory.md` | 4029 | `5a8943e1e556e1db0644cc7b75e2b4c8000b1a9506d673406c9c70cf7bb4a213` | `PHASE 1/PHASE 1.A/Phase1A_Memory.md`<br>`every sop and memory/Phase1A_Memory.md` |
| `every sop and memory/every_sop_and memory_from phase 1A to 1C and whoel phase overview.zip` | `Phase1A_Summary.md` | 2794 | `c52bed09fdfd1a860471bfc6d56cd41411f730362d12ee0348e07ad0939909c9` | `PHASE 1/PHASE 1.A/Phase1A_Summary.md`<br>`every sop and memory/Phase1A_Summary.md` |
| `every sop and memory/every_sop_and memory_from phase 1A to 1C and whoel phase overview.zip` | `Phase1B5_Memory.md` | 5302 | `d200473fd85a3cc910e3532bb2be662e0fcbdeab363fe988a948fd81d129c537` | `PHASE 1/PHASE 1B.5/Phase1B5_Memory.md`<br>`every sop and memory/Phase1B5_Memory.md` |
| `every sop and memory/every_sop_and memory_from phase 1A to 1C and whoel phase overview.zip` | `Phase1B5_Opportunity_Portfolio_Optimization.md` | 6431 | `305f0f568081ad8a01affc02d252a681f84abde5c23c2a9421fb69369ecc5540` | `PHASE 1/PHASE 1B.5/Phase1B5_Opportunity_Portfolio_Optimization.md`<br>`every sop and memory/Phase1B5_Opportunity_Portfolio_Optimization.md` |
| `every sop and memory/every_sop_and memory_from phase 1A to 1C and whoel phase overview.zip` | `Phase1B_Memory.md` | 3966 | `d58c91eead60c5abdb4e38c1e9b87c7449f4b3b68ccd7a23f5d4816fea16ff76` | `PHASE 1/PHASE 1.B/Phase1B_Memory.md`<br>`every sop and memory/Phase1B_Memory.md` |
| `every sop and memory/every_sop_and memory_from phase 1A to 1C and whoel phase overview.zip` | `Phase1B_Opportunity_Analysis.md` | 5802 | `e10d76b80c78554ff7e2ea75f3b263bfe82333c54418e7f794d249610f8fe130` | `PHASE 1/PHASE 1.B/Phase1B_Opportunity_Analysis.md`<br>`every sop and memory/Phase1B_Opportunity_Analysis.md` |
| `every sop and memory/every_sop_and memory_from phase 1A to 1C and whoel phase overview.zip` | `Phase1C.md` | 3009 | `8e41493ddbc8b8b3c3ad8a00995b6ae3f8a5645351f8086a6b8ded92623853e4` | `PHASE 1/PHASE 1C/Phase1C.md`<br>`every sop and memory/Phase1C.md` |
| `every sop and memory/every_sop_and memory_from phase 1A to 1C and whoel phase overview.zip` | `Phase1C_Memory.md` | 3390 | `e3b320245bc20d4312edc22b62fc9584059111e8fd38442277a3e5544ae019c1` | `PHASE 1/PHASE 1C/Phase1C_Memory.md`<br>`every sop and memory/Phase1C_Memory.md` |

Important exceptions:

- `contexts.zip/MC_Project_PHASE_DOC.md` has no byte-identical normal file and is an older v1-era roadmap.
- All other ZIP members match at least one normal repository file exactly.
- `phase3B_report_and_summary.zip`, located in the Phase 3A folder, contains Phase 3A—not Phase 3B—artifacts. Its filename is inaccurate.

## Non-duplicates worth stating explicitly

- Same-named Gemini, Mistral, Perplexity, Qwen, and ChatGPT files under different concept folders were not grouped merely by name.
- Phase 1 report PDFs and shorter Markdown memories/methodology files showed insufficient extracted-text equivalence and remain separate artifacts.
- Decision Register v1.0 and v1.2 substantially overlap historically but are different versions with materially different decisions; they are not duplicates.
- The failed OpenBraille ChatGPT PDF has negligible overlap with the valid OpenBraille final architecture report and is not valid evidence.
