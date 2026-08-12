# Authority Ambiguities

## Applied precedence

1. `PHASE 3/Engineering_Design_Review.md`
2. `Project_mC_Decision_Register_v1.2.md`
3. `PHASE 3/PHASE 3C-Comparative Technical Evaluation/Phase3C_Retained_Portfolio_Closure_Memo.md`
4. Final Phase 3C architecture reports
5. Phase 3C memories
6. Phase 3B report and memory
7. Phase 3A report and memory
8. Phase 2 report and memory
9. Phase 1C synthesis and dossiers
10. Raw independent research

## Confirmed ambiguities and resolutions

### EDR canonical versus convenience copy

`COPY PASTE FOLDER/Engineering_Design_Review.md` is byte-identical to `PHASE 3/Engineering_Design_Review.md`. The Phase 3 path is canonical; the convenience copy has no independent authority.

### Decision Register v1.2 versus v1.0

`Project_mC_Decision_Register_v1.2.md` is the current Level-2 authority. `Project_mC_Decision_Register_v1.0.md.save` and `COPY PASTE FOLDER/Project_mC_Decision_Register_v1.0.md` are byte-identical historical copies. v1.0 says Phase 3C was complete only for OpenBraille/VibeGuard and pending for the other three; v1.2 records TrueMoist completion, TrustLatch/ColdTrace deferral, and PDR-064 through PDR-067. Using v1.0 operationally would resurrect superseded state.

### Phase roadmap status is stale

Root `MC_Project_PHASE_DOC.md` is Version 2.0 (Frozen) and is the probable canonical methodology roadmap, but its progress table says Phase 3 is pending. That status conflicts with the EDR, Register v1.2, and closure memo. Under the defined precedence, those newer authorities control. The roadmap should not be used to infer current phase completion until its status block is corrected through an approved documentation update.

Two older roadmap variants also exist:

- `every sop and memory/MC_Project_PHASE_DOC.md` (older v1.0 content)
- `contexts.zip/MC_Project_PHASE_DOC.md` (another, shorter historical v1.0 variant)

They are historical convenience context, not canonical roadmaps.

### Project concept context versus later decisions

`PROJECT_CONCEPT_CONTEXT.md` calls itself canonical high-level context for all five Phase 1C concepts and says the Phase 1C report is ultimate when ambiguity exists. That remains valid for original concept definitions, but it does not override the later EDR or portfolio decisions. It must not be read as evidence that TrustLatch and ColdTrace remain active.

### Final Phase 3C report locations

- OpenBraille final: `.../openbraille/Claudes report for openbraille phase 3c.md`
- VibeGuard final: `.../vibeguard/research/Phase3C_VibeGuard_Architecture_Report By Claude.md`
- TrueMoist final: `.../TrueMoist/Phase3C_TrueMoist_ChatGPT_Final_Synthesis.md`

All three are Level-4 outputs. VibeGuard’s location among raw research falsely lowers its apparent status; its content and the Decision Register citations confirm that it is a final architecture report.

### Failed OpenBraille research

`.../openbraille/Researches/DEEpr research on phase 3c openbraille by chatgpt` is a PDF containing a generic “Universal Deep Research Framework” for an unspecified topic. It is the known failed/mis-scoped output. It remains Level-10 failed evidence for traceability and must never be promoted, averaged, or cited as valid OpenBraille research.

## Governance discoverability gaps

- `README.md` contains only the project title and does not point readers to the authority order.
- Convenience folders and ZIPs contain no warning that they are non-canonical.
- Many governance citations use only backticked basenames, not relative paths, so similarly named copies are easy to select incorrectly.
- `CURRENT_FOLDER_STRUCTURE.txt` is a snapshot, not authority, and is stale.
