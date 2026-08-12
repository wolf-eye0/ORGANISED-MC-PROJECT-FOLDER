# Authoritative Source Manifest

## Authority levels

Levels follow the owner-specified precedence. “Used” means used for governance, technical extraction, conflict identification, or a lower-level patent-history gap. Final Phase 3C reports supersede earlier implementation assumptions, but the EDR remains authoritative for identity and hypothesis and Decision Register v1.2 remains authoritative for accepted decisions.

| Exact path | Level | Concept | Role | Status | Criteria supported | Limitations / supersession |
|---|---:|---|---|---|---|---|
| `README.md` | Governance context | Portfolio | Repository status and canonical links | Current | Candidate scope, phase status | Not a technical evidence source; substantive matters governed by listed authorities. |
| `AGENTS.md` | Governance context | Portfolio | Repository policy, authority order, special cases | Current | Source handling and exclusions | Not concept evidence. |
| `PHASE 3/Engineering_Design_Review.md` | 1 | All three | Canonical identity, hypothesis, fixed principles, MDS, project constraints | Current | G2–G4; team fit; significance; validation objective | Predates Phase 3C component selection; does not freeze architecture. |
| `Project_mC_Decision_Register_v1.2.md` | 2 | All three / portfolio | Accepted requirements and PDR decisions | Current, authoritative register | Budget, team, architecture, validation, IP pivots, readiness | Some “verified” component decisions remain physically unvalidated; PDR-021 explicitly corrects the SG90 reset claim. |
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/Phase3C_Portfolio_Closure_Memo_Approved.md` | 3 | Portfolio | Retained shortlist, priorities, next action | Current, approved | Candidate scope, patent-first priority, constraints | High-level only; no detailed architecture evidence. |
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/OpenBraille/Phase3C_OpenBraille_Architecture_Report_Final.md` | 4 | OpenBraille | Frozen Phase 3C architecture, BOM, validation, risk, readiness | Current final | G1–G7; build, validation, demo, team, patent experiment surface | Superseded by PDR-021 where it states an SG90 integrated torsion spring provides passive reset; some exact mechanical/current claims remain untested. |
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/VibeGuard/Phase3C_VibeGuard_Architecture_Report_Final.md` | 4 | VibeGuard | Frozen Phase 3C architecture, cost, DSP, validation, risk, innovation discussion | Current final | G1–G7; build, validation, demo, team, patent experiment surface | Dense-machine attribution and spectral-subtraction adequacy remain empirical; report surfaced a 5-vs-6 roster inconsistency later resolved by PDR-038. |
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_Architecture_Report_Final.md` | 4 | TrueMoist | Frozen architecture, BOM, factorial validation, gates, patent implications | Current final | G1–G7; build, validation, demo, team, patent experiment surface | Procurement estimates need refresh; institutional oven/scale access and physical gates are pending. |
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/OpenBraille/Phase3C_OpenBraille_Memory_Final.md` | 5 | OpenBraille | Concise decision and risk memory | Current final memory | Architecture, BOM, risks, team tasks | Architecture report prevails; repeats passive-reset claim superseded/qualified by PDR-021. It also describes a team allocation that can be read as six roles. |
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/VibeGuard/Phase3C_VibeGuard_Memory_Final.md` | 5 | VibeGuard | Concise architecture and unresolved-question memory | Current final memory | Sensor, pipeline, costs, team, risks | Architecture report and PDR decisions prevail; its ADXL345 bandwidth wording must be read as MVP-limited. |
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_Memory_Final.md` | 5 | TrueMoist | Concise frozen architecture, gates, fallback hierarchy | Current final memory | Architecture, dataset, thresholds, facilities, readiness | Architecture report prevails. |
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/OpenBraille/Phase3C_OpenBraille_SOP_Final.md` | 6 | OpenBraille | Phase procedure and architecture criteria | Current Phase 3C SOP | Process, constraints, success framing | Pre-selection process document; final report/register supersede implementation choices. |
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/VibeGuard/Phase3C_VibeGuard_SOP_Final.md` | 6 | VibeGuard | Canonical Phase 3C mission/MDS and investigation requirements | Current Phase 3C SOP | MDS, budget, validation, innovation preservation | Team categories sum to six despite “five-member”; PDR-038 resolves roster as five. |
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_SOP_Final.md` | 6 | TrueMoist | Canonical Phase 3C identity/MDS, frozen constraints, evidence rules | Current Phase 3C SOP | MDS, validation, patent boundary, team | Header predates frozen decisions; final report/register supersede architecture options. Its internal source order placing the register last is superseded by repository governance. |
| `PHASE 2/Phase2_Report by CLaude.md` | 9 | All three | Historical consolidated patent landscape | Historical evidence, used only for patent-history gap | Named prior art, saturation, IP pivots, search questions | Not current patent verification, not legal advice/FTO; Phase 3C and register supersede old concept scope and recommendations. Its historical ranking is excluded from present comparison. |

## Explicitly excluded or non-authoritative

The following were not treated as current technical authority:

- `COPY PASTE FOLDER/`, `every sop and memory/`, `contexts.zip`, all phase ZIPs, and ZIP members — convenience/context packages.
- `Project_mC_Decision_Register_v1.0_HISTORICAL.md` and other historical registers — traceability only; v1.2 controls.
- Raw independent Gemini, Mistral, Perplexity, Qwen, Kimi, and ChatGPT research — evidence already synthesized where appropriate; it cannot override authoritative documents.
- The failed, mis-scoped ChatGPT OpenBraille Phase 3C research output — failed research preserved for methodology traceability, not OpenBraille evidence.
- Raw VibeGuard research under `VibeGuard/research/` — non-authoritative relative to the final architecture report.
- Repository audit, reorganization, validation, and cleanup files — repository history, not current technical evidence.
- Phase 2’s historical composite ranking and old recommendations — excluded because the task prohibits present ranking and later Phase 3C decisions supersede scope.

## Lower-phase consultation

Phase 3B, Phase 3A, and Phase 1C were not needed for unresolved architecture facts because the final Phase 3C packages and Decision Register covered them. Phase 2 was consulted only to prepare the later patent-search input pack; its claims remain historical and require current primary-source verification.
