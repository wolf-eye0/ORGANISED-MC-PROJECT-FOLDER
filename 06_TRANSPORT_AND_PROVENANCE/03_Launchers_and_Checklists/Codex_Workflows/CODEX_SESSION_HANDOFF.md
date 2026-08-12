# Codex Session Handoff — Final Down-Selection

> **Operational status only:** This file is a durable continuity aid for a future Codex conversation. It is not technical authority and does not replace the Engineering Design Review, Decision Register, Phase 3C reports, final comparison documents, or owner-approved decisions.

## Status

- Current branch: `analysis/final-downselection`
- Phase 3C is complete for the retained concepts:
  - OpenBraille
  - VibeGuard
  - TrueMoist
- TrustLatch and ColdTrace are deferred.
- Phase 4 has not started.
- No final project has been selected.
- Patent-development potential is the primary selection priority.
- Budget ceiling is ₹5,000; the preferred budget is ₹3,000 or below.
- Target implementation duration is approximately two months.
- Authoritative team size is five:
  - three technically strong members;
  - one beginner;
  - one presenter/support member.

## Work completed in this session

- Created the repository-grounded final down-selection evidence package.
- Completed the Instant-mode extraction pass.
- Applied the bounded human-review corrections:
  - clarified A4 risk-score direction;
  - changed OpenBraille G4 to Provisional Pass;
  - added the threshold-status rule;
  - added the post-review validation record.
- Completed a High-reasoning independent audit.
- High audit verdict: **Ready for current patent verification**.
- The audit added two missing decision-critical uncertainty entries and clarified that TrueMoist PDR-012 remains future multi-soil work outside the semester MVP.
- No scoring, ranking, recommendation, elimination, or winner was produced.
- No online patent research has been completed yet.

## Package files

- `README.md` — package purpose, workflow, authority policy, file index, and patent warning.
- `01_Comparison_Protocol.md` — hard gates, future 100-point rubric, scoring rules, and required later outputs.
- `02_Authoritative_Source_Manifest.md` — authority levels, source roles, limitations, supersession, and exclusions.
- `03_Concept_Evidence_Matrix.md` — neutral three-concept evidence comparison with sources, confidence, and conflicts.
- `04_Hard_Gate_Precheck.md` — repository-only G1–G7 precheck without elimination.
- `05_Uncertainty_and_Test_Register.md` — unresolved technical, validation, patent, and resource questions with resolving actions.
- `06_Patent_Research_Input_Pack.md` — neutral input for the later current primary-source patent pass.
- `07_Scoring_Worksheet.md` — blank scoring and ranking worksheet for use only after patent verification.
- `CODEX_EXTRACTION_VALIDATION.md` — extraction trail, safeguards, corrections, gaps, and terminal-check record.
- `HIGH_REASONING_AUDIT.md` — independent audit, additional minimal corrections, neutrality check, and readiness verdict.
- `CODEX_SESSION_HANDOFF.md` — non-authoritative operational continuity file for resuming work in a future Codex conversation.

## Authority order

1. `PHASE 3/Engineering_Design_Review.md`
2. `Project_mC_Decision_Register_v1.2.md`
3. `PHASE 3/PHASE 3C-Comparative Technical Evaluation/Phase3C_Portfolio_Closure_Memo_Approved.md`
4. Final Phase 3C architecture reports
5. Final Phase 3C memories
6. Phase 3C SOPs
7. Phase 3B
8. Phase 3A
9. Phase 2
10. Phase 1C
11. Raw research

Lower-authority evidence cannot override higher-authority decisions. Raw research, convenience copies, ZIP members, historical registers, audit files, and this handoff are not current technical authority.

## Important confirmed issues

### OpenBraille

- The SG90 passive-return claim is unverified.
- Active servo-driven cam retraction may be the truthful architecture if no usable passive return is physically confirmed.
- Adequacy of the 5 V/2 A supply for six-servo demand remains unverified.
- The blinded tactile-identification protocol, participant plan, and quantitative acceptance rate remain provisional and require owner approval.
- The macro-scale semester MVP and long-term practical-scale invention path must remain separate.
- The carried patent direction is manufacturing/firmware development, not presumed novelty of the servo-cam mechanism.

### VibeGuard

- ADXL345 is limited to the low-frequency MVP scope; IIS3DWB is the documented later bearing-fault bandwidth path.
- Quantitative bench success thresholds remain unfrozen.
- Bench abnormal-condition detection is not dense-machine attribution.
- Spectral subtraction and Mahalanobis differentiation remain unvalidated.
- Conventional vibration-monitor and single-node prior-art risk requires current verification.

### TrueMoist

- ADS1115 remains evidence-gated against calibrated ESP32 ADC1.
- Institutional oven and scale access remain pending.
- The 72-run target means independent physical condition runs; repeated ADC readings are averaged and are not independent runs.
- Controlled salinity treatment is not live EC measurement.
- The fixed-coefficient, single-soil semester MVP is separate from future adaptive and multi-soil work.
- PDR-012 remains a future two-season, multi-soil validation task outside the semester MVP.

## Patent status

- G6 remains **Insufficient Evidence** for OpenBraille, VibeGuard, and TrueMoist.
- Historical Phase 2 conclusions are research leads only.
- Current patent-family status, independent claims, legal status, novelty, obviousness/inventive step, patent eligibility, and FTO/infringement risk remain unverified.
- No concept should be scored or selected before the current primary-source patent pass.
- No statement in this package establishes patentability or provides a legal FTO conclusion.

## Next workflow

1. Commit the completed evidence package as a checkpoint.
2. Conduct current primary-source patent verification outside this Codex extraction session.
3. Review the patent results against the frozen architectures.
4. Complete the scoring worksheet.
5. Produce patent-first, buildability, validation, demonstration, and balanced rankings.
6. Select exactly one primary project, one runner-up, and one reserve.
7. Perform an adversarial audit of that selection.
8. Use Codex later to integrate the approved decision into the repository.

## Repository safety

- `ZEROTH PRESENTATION/` is unrelated and untracked; it must not be inspected, modified, or staged as part of this work.
- Do not use `git add -A` while that unrelated directory is untracked.
- Do not modify authoritative documents without an approved bounded patch.
- Do not treat this handoff as technical authority.
- Preserve the existing hierarchy and do not stage, commit, or push unless the owner explicitly authorizes the next action.

## Resume instruction

Read `CODEX_SESSION_HANDOFF.md`, `README.md`, `CODEX_EXTRACTION_VALIDATION.md` and `HIGH_REASONING_AUDIT.md` first. Then inspect `git status` and the current branch. Do not alter files until the owner gives the next approved task.
