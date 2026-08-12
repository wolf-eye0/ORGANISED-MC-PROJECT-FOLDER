# TrueMoist Limited Upload Package Validation

- Creation time: 2026-08-02T11:03:32+02:00
- Gemini output: `/home/paradoxpete/Documents/PROJECT_UPLOAD_PACKS/TrueMoist_Patent_Research_Input_GEMINI_10`
- Qwen output: `/home/paradoxpete/Documents/PROJECT_UPLOAD_PACKS/TrueMoist_Patent_Research_Input_QWEN_5`
- Gemini physical file count: 10
- Qwen physical file count: 5
- Logical inputs represented in each package: 11, exactly once
- Canonical project documents represented in each package: 10, exactly once
- Governing instruction represented in each package: once

## Source control

| Key | Original absolute path | Bytes | SHA-256 |
|---|---|---:|---|
| 00 `00_READ_FIRST_TrueMoist_Patent_Research_Instructions.md` | `/home/paradoxpete/Documents/PROJECT/00_READ_FIRST_TrueMoist_Patent_Research_Instructions.md` | 12812 | `e201944a6a67caa64c06cd95aeb3ccee4c2c9413e137da2ed6a73d99f0d6aca4` |
| 01 `Engineering_Design_Review.md` | `/home/paradoxpete/Documents/PROJECT/PHASE 3/Engineering_Design_Review.md` | 31205 | `46f017501ac3ff9ebd6c1fb1e5ee8c068c22ddb08ae204c5609f2b759090295e` |
| 02 `Project_mC_Decision_Register_v1.2.md` | `/home/paradoxpete/Documents/PROJECT/Project_mC_Decision_Register_v1.2.md` | 56071 | `9678c5072d86ef38e48372f940ec91396b7ac7bcbeed0124ac8e2485307f408c` |
| 03 `Phase3C_Portfolio_Closure_Memo_Approved.md` | `/home/paradoxpete/Documents/PROJECT/PHASE 3/PHASE 3C-Comparative Technical Evaluation/Phase3C_Portfolio_Closure_Memo_Approved.md` | 3149 | `3c6e6f568c06099251b4b71d4f35cf668ee23a40c8214c95e4a12fe36cf4845a` |
| 04 `Phase3C_TrueMoist_Architecture_Report_Final.md` | `/home/paradoxpete/Documents/PROJECT/PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_Architecture_Report_Final.md` | 46897 | `6c71f1d618e0575d127b10f05e91d06ea4b1f0b8a2fe63e78d4022ee75234610` |
| 05 `Phase3C_TrueMoist_Memory_Final.md` | `/home/paradoxpete/Documents/PROJECT/PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_Memory_Final.md` | 5232 | `c84bc0e08c8c96cfe410d8c690df35c6b7996e5ffda7703ceff37a424bf02df1` |
| 06 `Phase3C_TrueMoist_SOP_Final.md` | `/home/paradoxpete/Documents/PROJECT/PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_SOP_Final.md` | 18712 | `993caf1a05f3fdc3937efb634e2f2e467488e973eb71454db8e3c3f53d178d00` |
| 07 `03_Concept_Evidence_Matrix.md` | `/home/paradoxpete/Documents/PROJECT/PHASE 3/PHASE 3C-Comparative Technical Evaluation/FINAL_DOWNSELECTION/03_Concept_Evidence_Matrix.md` | 19491 | `8f999b878cfc7f863227682f141a278a4dfa4ee7705e49e1d55ef147c27a1975` |
| 08 `05_Uncertainty_and_Test_Register.md` | `/home/paradoxpete/Documents/PROJECT/PHASE 3/PHASE 3C-Comparative Technical Evaluation/FINAL_DOWNSELECTION/05_Uncertainty_and_Test_Register.md` | 22484 | `125c057229524532b115391fbba948023684ad61d0153fb28ac29e6031e8ee3b` |
| 09 `06_Patent_Research_Input_Pack.md` | `/home/paradoxpete/Documents/PROJECT/PHASE 3/PHASE 3C-Comparative Technical Evaluation/FINAL_DOWNSELECTION/06_Patent_Research_Input_Pack.md` | 16069 | `969d6bd97f0a726186d0f9bae405248ed82ef6314e3d5618166a0a1185411428` |
| 10 `Phase2_Report by CLaude.md` | `/home/paradoxpete/Documents/PROJECT/PHASE 2/Phase2_Report by CLaude.md` | 44493 | `783729d0e07e725236db5296dae8504ce782c294b8c61cfab40ea172cfa6943e` |

## Gemini package mapping and destinations

| Physical file | Logical source(s) | Bytes | Destination SHA-256 | Validation |
|---|---|---:|---|---|
| `00_READ_FIRST_TrueMoist_Patent_Research_Instructions.md` | 00: `00_READ_FIRST_TrueMoist_Patent_Research_Instructions.md` | 12812 | `e201944a6a67caa64c06cd95aeb3ccee4c2c9413e137da2ed6a73d99f0d6aca4` | Direct-copy source/destination SHA-256 MATCH |
| `01_Engineering_Design_Review.md` | 01: `Engineering_Design_Review.md` | 31205 | `46f017501ac3ff9ebd6c1fb1e5ee8c068c22ddb08ae204c5609f2b759090295e` | Direct-copy source/destination SHA-256 MATCH |
| `02_Project_mC_Decision_Register_v1.2.md` | 02: `Project_mC_Decision_Register_v1.2.md` | 56071 | `9678c5072d86ef38e48372f940ec91396b7ac7bcbeed0124ac8e2485307f408c` | Direct-copy source/destination SHA-256 MATCH |
| `03_Phase3C_Portfolio_Closure_Memo_Approved.md` | 03: `Phase3C_Portfolio_Closure_Memo_Approved.md` | 3149 | `3c6e6f568c06099251b4b71d4f35cf668ee23a40c8214c95e4a12fe36cf4845a` | Direct-copy source/destination SHA-256 MATCH |
| `04_05_TrueMoist_Architecture_and_Memory.md` | 04: `Phase3C_TrueMoist_Architecture_Report_Final.md`<br>05: `Phase3C_TrueMoist_Memory_Final.md` | 53651 | `8f8bf0175b9556a93f0694dad6677247ca2b7c6e5b0b58134648977b288f2941` | All marker-bounded source bodies byte-identical; each marker occurs once |
| `06_Phase3C_TrueMoist_SOP_Final.md` | 06: `Phase3C_TrueMoist_SOP_Final.md` | 18712 | `993caf1a05f3fdc3937efb634e2f2e467488e973eb71454db8e3c3f53d178d00` | Direct-copy source/destination SHA-256 MATCH |
| `07_Concept_Evidence_Matrix.md` | 07: `03_Concept_Evidence_Matrix.md` | 19491 | `8f999b878cfc7f863227682f141a278a4dfa4ee7705e49e1d55ef147c27a1975` | Direct-copy source/destination SHA-256 MATCH |
| `08_Uncertainty_and_Test_Register.md` | 08: `05_Uncertainty_and_Test_Register.md` | 22484 | `125c057229524532b115391fbba948023684ad61d0153fb28ac29e6031e8ee3b` | Direct-copy source/destination SHA-256 MATCH |
| `09_Patent_Research_Input_Pack.md` | 09: `06_Patent_Research_Input_Pack.md` | 16069 | `969d6bd97f0a726186d0f9bae405248ed82ef6314e3d5618166a0a1185411428` | Direct-copy source/destination SHA-256 MATCH |
| `10_Phase2_Report_by_Claude.md` | 10: `Phase2_Report by CLaude.md` | 44493 | `783729d0e07e725236db5296dae8504ce782c294b8c61cfab40ea172cfa6943e` | Direct-copy source/destination SHA-256 MATCH |

## Qwen package mapping and destinations

| Physical file | Logical source(s) | Bytes | Destination SHA-256 | Validation |
|---|---|---:|---|---|
| `00_READ_FIRST_TrueMoist_Patent_Research_Instructions.md` | 00: `00_READ_FIRST_TrueMoist_Patent_Research_Instructions.md` | 12812 | `e201944a6a67caa64c06cd95aeb3ccee4c2c9413e137da2ed6a73d99f0d6aca4` | Direct-copy source/destination SHA-256 MATCH |
| `01_03_Project_Authority_Bundle.md` | 01: `Engineering_Design_Review.md`<br>02: `Project_mC_Decision_Register_v1.2.md`<br>03: `Phase3C_Portfolio_Closure_Memo_Approved.md` | 92286 | `99b9feb81f6f32a0f78f21bab825ce085c2508c6fa2d7accfd1827cf60ab5fdb` | All marker-bounded source bodies byte-identical; each marker occurs once |
| `04_06_TrueMoist_Phase3C_Bundle.md` | 04: `Phase3C_TrueMoist_Architecture_Report_Final.md`<br>05: `Phase3C_TrueMoist_Memory_Final.md`<br>06: `Phase3C_TrueMoist_SOP_Final.md` | 72837 | `cff6bf8bceeb8a2c18eb197f8fefd9c2813bab270ee76347480f0e11aa00aa97` | All marker-bounded source bodies byte-identical; each marker occurs once |
| `07_09_Validation_and_Patent_Input_Bundle.md` | 07: `03_Concept_Evidence_Matrix.md`<br>08: `05_Uncertainty_and_Test_Register.md`<br>09: `06_Patent_Research_Input_Pack.md` | 60028 | `a72308a766a105a1c38903daa99cdcc2027addccefa0e2fa98389acee99fee43` | All marker-bounded source bodies byte-identical; each marker occurs once |
| `10_Phase2_Historical_Patent_Leads.md` | 10: `Phase2_Report by CLaude.md` | 44493 | `783729d0e07e725236db5296dae8504ce782c294b8c61cfab40ea172cfa6943e` | Direct-copy source/destination SHA-256 MATCH |

## Merged-source containment

| Package file | Embedded logical source | Original SHA-256 | Extracted SHA-256 | Result |
|---|---|---|---|---|
| `04_05_TrueMoist_Architecture_and_Memory.md` | `Phase3C_TrueMoist_Architecture_Report_Final.md` | `6c71f1d618e0575d127b10f05e91d06ea4b1f0b8a2fe63e78d4022ee75234610` | `6c71f1d618e0575d127b10f05e91d06ea4b1f0b8a2fe63e78d4022ee75234610` | MATCH |
| `04_05_TrueMoist_Architecture_and_Memory.md` | `Phase3C_TrueMoist_Memory_Final.md` | `c84bc0e08c8c96cfe410d8c690df35c6b7996e5ffda7703ceff37a424bf02df1` | `c84bc0e08c8c96cfe410d8c690df35c6b7996e5ffda7703ceff37a424bf02df1` | MATCH |
| `01_03_Project_Authority_Bundle.md` | `Engineering_Design_Review.md` | `46f017501ac3ff9ebd6c1fb1e5ee8c068c22ddb08ae204c5609f2b759090295e` | `46f017501ac3ff9ebd6c1fb1e5ee8c068c22ddb08ae204c5609f2b759090295e` | MATCH |
| `01_03_Project_Authority_Bundle.md` | `Project_mC_Decision_Register_v1.2.md` | `9678c5072d86ef38e48372f940ec91396b7ac7bcbeed0124ac8e2485307f408c` | `9678c5072d86ef38e48372f940ec91396b7ac7bcbeed0124ac8e2485307f408c` | MATCH |
| `01_03_Project_Authority_Bundle.md` | `Phase3C_Portfolio_Closure_Memo_Approved.md` | `3c6e6f568c06099251b4b71d4f35cf668ee23a40c8214c95e4a12fe36cf4845a` | `3c6e6f568c06099251b4b71d4f35cf668ee23a40c8214c95e4a12fe36cf4845a` | MATCH |
| `04_06_TrueMoist_Phase3C_Bundle.md` | `Phase3C_TrueMoist_Architecture_Report_Final.md` | `6c71f1d618e0575d127b10f05e91d06ea4b1f0b8a2fe63e78d4022ee75234610` | `6c71f1d618e0575d127b10f05e91d06ea4b1f0b8a2fe63e78d4022ee75234610` | MATCH |
| `04_06_TrueMoist_Phase3C_Bundle.md` | `Phase3C_TrueMoist_Memory_Final.md` | `c84bc0e08c8c96cfe410d8c690df35c6b7996e5ffda7703ceff37a424bf02df1` | `c84bc0e08c8c96cfe410d8c690df35c6b7996e5ffda7703ceff37a424bf02df1` | MATCH |
| `04_06_TrueMoist_Phase3C_Bundle.md` | `Phase3C_TrueMoist_SOP_Final.md` | `993caf1a05f3fdc3937efb634e2f2e467488e973eb71454db8e3c3f53d178d00` | `993caf1a05f3fdc3937efb634e2f2e467488e973eb71454db8e3c3f53d178d00` | MATCH |
| `07_09_Validation_and_Patent_Input_Bundle.md` | `03_Concept_Evidence_Matrix.md` | `8f999b878cfc7f863227682f141a278a4dfa4ee7705e49e1d55ef147c27a1975` | `8f999b878cfc7f863227682f141a278a4dfa4ee7705e49e1d55ef147c27a1975` | MATCH |
| `07_09_Validation_and_Patent_Input_Bundle.md` | `05_Uncertainty_and_Test_Register.md` | `125c057229524532b115391fbba948023684ad61d0153fb28ac29e6031e8ee3b` | `125c057229524532b115391fbba948023684ad61d0153fb28ac29e6031e8ee3b` | MATCH |
| `07_09_Validation_and_Patent_Input_Bundle.md` | `06_Patent_Research_Input_Pack.md` | `969d6bd97f0a726186d0f9bae405248ed82ef6314e3d5618166a0a1185411428` | `969d6bd97f0a726186d0f9bae405248ed82ef6314e3d5618166a0a1185411428` | MATCH |

## Exclusions and safety

- Decision Register v1.1 is absent.
- The superseded `TrueMoist/by claude/` 135-run files and `TrueMoist/files.zip` are absent.
- No separately selected OpenBraille or VibeGuard file is present. Required shared portfolio documents remain unmodified.
- No ZIP, README, manifest, launcher, checklist or hidden file is inside either upload directory.
- Gemini launcher is outside its upload folder: `/home/paradoxpete/Documents/PROJECT_UPLOAD_PACKS/TrueMoist_Patent_Research_Launcher_GEMINI_10.txt`.
- Qwen launcher is outside its upload folder: `/home/paradoxpete/Documents/PROJECT_UPLOAD_PACKS/TrueMoist_Patent_Research_Launcher_QWEN_5.txt`.
- The authoritative 72-run TrueMoist architecture, memory, SOP and Decision Register v1.2 are used.
- Every original source hash remained unchanged after package generation.
- `ZEROTH PRESENTATION/` was not accessed or modified.

## Repository status before

```text
?? 00_READ_FIRST_OpenBraille_Patent_Deep_Research_Instructions.md
?? 00_READ_FIRST_OpenBraille_Synthesis_Instructions.md
?? 00_READ_FIRST_TrueMoist_Patent_Research_Instructions.md
?? 00_READ_FIRST_VibeGuard_Patent_Research_Instructions.md
?? 00_READ_FIRST_VibeGuard_Synthesis_Instructions.md
?? CODEX_CREATE_TRUEMOIST_GEMINI10_QWEN5_PACKAGES.txt
?? CODEX_ORGANIZE_TRUEMOIST_PATENT_RESEARCH_PACKAGE.txt
?? CODEX_ORGANIZE_VIBEGUARD_SYNTHESIS_PACKAGE.txt
?? "OTHER PEOPLES IDEA/"
?? "PHASE 3/PHASE 3C-Comparative Technical Evaluation/FINALISED DECISION/"
?? "PHASE 3/PHASE 3C-Comparative Technical Evaluation/FINAL_DOWNSELECTION/RESEAERCH/"
?? "PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/by claude/"
?? "PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/files.zip"
?? "ZEROTH PRESENTATION/"
?? "amith arguments/"
```

## Repository status after

```text
?? 00_READ_FIRST_OpenBraille_Patent_Deep_Research_Instructions.md
?? 00_READ_FIRST_OpenBraille_Synthesis_Instructions.md
?? 00_READ_FIRST_TrueMoist_Patent_Research_Instructions.md
?? 00_READ_FIRST_VibeGuard_Patent_Research_Instructions.md
?? 00_READ_FIRST_VibeGuard_Synthesis_Instructions.md
?? CODEX_CREATE_TRUEMOIST_GEMINI10_QWEN5_PACKAGES.txt
?? CODEX_ORGANIZE_TRUEMOIST_PATENT_RESEARCH_PACKAGE.txt
?? CODEX_ORGANIZE_VIBEGUARD_SYNTHESIS_PACKAGE.txt
?? "OTHER PEOPLES IDEA/"
?? "PHASE 3/PHASE 3C-Comparative Technical Evaluation/FINALISED DECISION/"
?? "PHASE 3/PHASE 3C-Comparative Technical Evaluation/FINAL_DOWNSELECTION/RESEAERCH/"
?? "PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/by claude/"
?? "PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/files.zip"
?? "ZEROTH PRESENTATION/"
?? "amith arguments/"
```

- Status unchanged: PASS
- `git diff --check` before/after unchanged and empty: PASS
- No original was modified: PASS
