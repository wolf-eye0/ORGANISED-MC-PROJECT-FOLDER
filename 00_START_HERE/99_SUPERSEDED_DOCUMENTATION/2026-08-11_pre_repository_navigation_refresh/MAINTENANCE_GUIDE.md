# Project mC — Repository Maintenance Guide

## 1. Repository principles

Maintain `/home/paradoxpete/Documents/PROJECT_ORGANIZED` as a traceable evidence and documentation workspace.

- Preserve chronology, provenance and source identity.
- Prefer minimal, reversible changes.
- Separate current authority, supporting evidence, history, raw research and transport copies.
- Treat hashes as identity controls, not proof of technical truth.
- Keep recommendation, approval, implementation, experimental success and patentability as separate evidence states.
- Do not modify `/home/paradoxpete/Documents/PROJECT` or `/home/paradoxpete/Documents/PROJECT_UPLOAD_PACKS` during organized-workspace maintenance.

## 2. Authority hierarchy

Use `01_GOVERNANCE_AND_CONTROL/AUTHORITY_MAP.md`. The practical order is:

1. Engineering Design Review.
2. Latest accepted Decision Register—currently v1.2.
3. Approved Phase 3C Retained-Portfolio Closure Memo.
4. Final Phase 3C architecture reports.
5. Phase 3C memories.
6. Phase 3C SOPs.
7. Validated down-selection evidence and test controls.
8. Earlier phase outputs in descending phase order.
9. Current syntheses and future-research simulations as supporting analysis.
10. Historical and raw independent research.

Never use filename recency, model identity, upload date or folder convenience as authority. Final adjudications are comparative decision context, not votes.

## 3. Preserve historical documents

Never silently alter an old historical document to make it look current. A statement such as “Phase 3C in progress” or an older ranking may correctly record the author's knowledge at that time. Preserve it and place current truth in current governance, the root README or a later versioned record.

## 4. How to add a new file

1. Confirm it belongs to Project mC and contains no credential or unrelated private material.
2. Record source path, filename, byte size, modification time and SHA-256.
3. Inspect content sufficiently to determine concept, phase, role, completeness and authority.
4. Search the live hash inventory and likely semantic destination.
5. If an exact canonical copy exists, normally do not add another copy.
6. If a transport/provenance copy is required, label it as such.
7. Never overwrite a different-content collision; preserve both and escalate ambiguity.
8. Copy byte-for-byte unless the task explicitly authorizes a generated document.
9. Update indexes, catalog, change register and release controls.

## 5. How to choose the destination folder

- `00_START_HERE/`: repository-validation and documentation-release records.
- `01_GOVERNANCE_AND_CONTROL/`: genuine requirements, accepted decisions, authority maps and repository controls only.
- `02_PHASE_HISTORY/`: historical phase research and outputs.
- `03_CONCEPT_PORTFOLIO/<Concept>/01_Final_Architecture/`: only formally final architecture records.
- `03_CONCEPT_PORTFOLIO/<Concept>/02_Raw_Research/`: raw independent research.
- `03_CONCEPT_PORTFOLIO/<Concept>/03_Patent_Synthesis/`: current patent-evidence syntheses.
- `03_CONCEPT_PORTFOLIO/<Concept>/04_PreBuild_Simulation/`: hypothetical future patent-case simulations.
- `03_CONCEPT_PORTFOLIO/<Concept>/05_Roadmaps_and_Reference_Dossiers/`: semester roadmaps and retained references.
- `04_COMPARATIVE_DECISION/`: shared evidence, adjudications, change requests and supporting audits/syntheses.
- `05_TEACHER_AND_REVIEWS/`: delivery index, official submissions, drafts and peer/reference material.
- `06_TRANSPORT_AND_PROVENANCE/`: instructions, manifests, launchers, bundles and package validation.
- `07_SEMESTER_EXECUTION/`: use only after formal Phase 4 authorization.
- `08_MASTER_MANUAL/`: controlled manual source, drafting, review, assembly and release material.
- `09_ARCHIVE/`: superseded, exact-duplicate, failed/partial, legacy archive and intentionally excluded material.

Do not invent a parallel hierarchy for one file. If two existing folders remain plausible, mark `PENDING OWNER PLACEMENT` instead of guessing.

## 6. Naming rules

- Preserve official filenames for authoritative files unless a controlled naming action is approved.
- Use semantic, stable names with concept, role and version where needed.
- Preserve version numbers and release labels exactly.
- Do not rename failed research to look valid.
- Avoid labels such as `FINAL` unless content and controls support them.
- Keep original filename and source path in provenance when a controlled destination name differs.
- Never renumber PDR entries casually.

## 7. SHA-256 and provenance recording

For every material copy or authorized edit, record:

- source and destination paths;
- before hash for a pre-existing target;
- source and final hashes;
- byte sizes;
- timestamp;
- change type and reason;
- authority and Master Manual effects.

Use `sha256sum` on the physical bytes. For PDF/DOCX equivalence, also compare extracted content before calling files content-equivalent; binary inequality does not automatically mean different human content.

## 8. Exact duplicate handling

Files with the same SHA-256 are exact byte duplicates.

- Keep the identified canonical source in its semantic authority location.
- Avoid creating unnecessary new canonical copies.
- Preserve required upload/transport copies only for provenance.
- Mark duplicates as copies and point to the canonical counterpart.
- Do not count duplicates as independent technical corroboration or model votes.

## 9. Near-duplicate and version handling

Similar filenames, extracted text or visual appearance do not prove identity.

1. Compare byte hashes.
2. For Markdown/text, compare normalized text only as a secondary diagnostic; preserve original bytes.
3. For DOCX/PDF, compare extracted content and metadata cautiously.
4. Identify substantive, formatting-only and container-metadata differences separately.
5. Preserve different-content versions until authority and chronology are resolved.

Never merge two different-content sources merely because they look similar.

## 10. Superseded-document handling

- Do not delete the old document.
- Record the controlling successor and decision/event that caused supersession.
- Preserve the original bytes and historical status.
- Move only under an explicitly approved reorganization workflow; otherwise leave it and classify it.
- Update navigation without rewriting old conclusions.
- Do not describe a document as superseded merely because it is older.

## 11. Failed/concept-swap quarantine rules

Failed, partial or concept-swapped research must remain identifiable and auditable.

- Store it under `09_ARCHIVE/03_Failed_or_Partial_Research/` when an approved placement action is performed.
- Preserve source identity and failure reason.
- Never blend it into valid synthesis or architecture evidence.
- Never count it as an independent vote.
- Known wrong-architecture OpenBraille and VibeGuard outputs must remain excluded from current evidence.

## 12. Upload-pack and transport-copy rules

Upload packs, reduced bundles, manifests, launchers and checklists are convenience/provenance artifacts.

- A transport copy does not gain authority because it has a higher sequence number or later modification time.
- Resolve canonical counterparts by exact hash and provenance.
- Do not edit internal source content merely to simplify uploading.
- Preserve bundle wrapper and embedded-source distinctions.
- Do not use an upload manifest as technical evidence.

## 13. Raw AI research treatment

Raw AI research is evidence, not authority and not a vote.

- Record model/lane and completeness where known.
- Audit citations, patent identifiers, legal status and concept fidelity before relying on conclusions.
- Preserve failed lanes for methodology traceability.
- Never treat model consensus as proof.
- Never allow raw research to override current governance or frozen architecture.

## 14. Teacher-facing document handling

- Preserve submitted/rendered PDF and editable DOCX identities.
- Keep teacher requests separate from evidence of teacher approval.
- Keep official submissions separate from drafts.
- Record delivery/approval date, conditions and responsible person only when evidence exists.
- Avoid public disclosure of unnecessary confidential future-mechanism detail.
- Never claim teacher approval without actual approval evidence.

## 15. Source-freeze meaning

Master Manual v1.0 records a controlled source population frozen for that release. The freeze means:

- the released manual and its source register remain unchanged;
- later files do not retroactively become v1.0 sources;
- historical hashes and Appendix A1 must not be rewritten to follow the live repository;
- a live repository may legitimately contain post-release documentation and evidence.

Source freeze does not prohibit future work; it requires transparent versioning.

## 16. Post-freeze change handling

Record every material post-freeze change in `08_MASTER_MANUAL/01_Source_Index/POST_FREEZE_CHANGE_REGISTER.md` with timestamp, path, before/after hashes where meaningful, change type, reason and `Master Manual v1.0 changed: NO` unless a separate authorized release process says otherwise.

Do not back-write the frozen manual or source index. Assess whether each change is navigation-only, supporting, governance-affecting or release-impacting.

## 17. Current-price/current-web-fact handling

Prices, availability, delivery terms and specifications age quickly.

- Record verification date and source.
- Prefer manufacturer documentation for technical specifications.
- Use reputable Indian distributors/retailers and separate delivery/tax assumptions.
- Distinguish bought, borrowed, reusable, optional and contingency items.
- Refresh prices at procurement; do not rewrite old costing records.
- Never infer that procurement began because a BOM exists.

## 18. Patent/legal-status freshness boundaries

Patent publication, family, claims and legal status are time-sensitive and jurisdiction-specific.

- Use primary official sources for load-bearing conclusions where feasible.
- Distinguish prior-art relevance from FTO relevance.
- Record search/status date and unresolved limits.
- Do not call FTO clear.
- Do not treat expired/abandoned documents as irrelevant prior art or automatically blocking FTO.
- No model output is legal advice, a patentability opinion or a grant guarantee.

## 19. Master Manual release policy

The frozen release is:

`08_MASTER_MANUAL/10_Final_Assembly_Workspace/03_Final_Controlled_Releases/v1.0/Project_mC_Master_Manual_FINAL_CONTROLLED_RELEASE.md`

Release date: 2026-08-06  
SHA-256: `4700c630c21c73d7709bfc317c7e6eba155ed768d60d40ff2781e76cb5c787e8`

**Never overwrite the final controlled Master Manual.** Do not create v1.0.1 or v1.1 merely for live navigation changes. A later release requires a meaningful state change, deliberate version decision, new source freeze, source maps, reconciliation, validation, assembly map, release manifest and certificate.

## 20. Decision Register versioning policy

- Decision Register v1.2 remains authoritative and immutable during ordinary documentation maintenance.
- Do not create v1.3 without a real new governing decision.
- Actual teacher approval/final semester authorization is the expected next decision event.
- Preserve all prior registers as history.
- A later version must state what changed and must not silently renumber PDR entries.

## 21. Teacher-approval workflow

1. Submit the controlled request and supporting documents.
2. Capture actual approval, rejection or conditions with date and provenance.
3. Do not infer approval from silence, preparation or a roadmap.
4. If approved, create a controlled Final Selection / Phase 4 Entry Memo.
5. Then create the next Decision Register version.
6. If rejected/conditioned, record that result without rewriting the request.

## 22. Phase-4 entry workflow

Phase 4 begins only after a controlling selection/entry record.

1. Freeze the approved concept and semester scope.
2. Record teacher/platform conditions.
3. Create the Final Selection / Phase 4 Entry Memo.
4. Create Decision Register v1.3 or the next authorized version.
5. Refresh BOM/specifications and authorize procurement separately.
6. Populate `07_SEMESTER_EXECUTION/` with dated implementation evidence.
7. Keep post-semester PIRG/VPD-C7 research outside the semester MVP unless explicitly authorized.

The existence of empty Phase 4 folders is not evidence that Phase 4 started.

## 23. Catalog regeneration procedure

1. Scan every physical regular file, excluding `.git`, caches, locks and temporary staging files.
2. Compute relative path, byte size and SHA-256.
3. Recompute file/directory/byte totals and extension types.
4. Compare paths/hashes with the previous catalog or snapshot.
5. Identify exact hash groups and canonical counterparts conservatively.
6. Infer concept, phase, role, lifecycle and authority from content plus provenance—not filename alone.
7. Use `UNCLASSIFIED / OWNER REVIEW REQUIRED` when uncertain.
8. Finalize README and this guide before cataloging their hashes.
9. Apply the catalog self-hash rule; control `FILE_CATALOG.md` externally in the documentation release manifest.
10. Validate physical counts after installation.

## 24. Validation checklist

- [ ] Frozen Master Manual hash matches the controlled release.
- [ ] Decision Register v1.2 and final architecture hashes are unchanged.
- [ ] No source path was deleted.
- [ ] Original PROJECT and PROJECT_UPLOAD_PACKS snapshots are unchanged.
- [ ] New/imported files have source hashes and classifications.
- [ ] Exact duplicates point to canonical sources where determinable.
- [ ] Failed/concept-swapped material is not marked authoritative.
- [ ] Teacher approval is not falsely claimed.
- [ ] Phase 4/procurement are not falsely claimed started.
- [ ] Patentability/FTO is not falsely claimed.
- [ ] Root documentation and indexes agree on current status.
- [ ] Catalog counts match the physical workspace.
- [ ] All generated Markdown is readable UTF-8.
- [ ] No temporary file remains inside the organized workspace.
- [ ] Post-freeze register, release manifest and validation report are updated.

## 25. Backup and recovery rules

- Preserve original source repositories as provenance references.
- Before replacing an allowed documentation target, record its hash and retain the pre-write snapshot outside the repository.
- Never permanently delete project files as a cleanup shortcut.
- Restore by verified hash, not filename alone.
- Preserve archive/history even when current work no longer uses it.
- Test recovery copies before relying on them.
- Keep credentials and secrets outside documentation backups and catalogs.

## 26. Prohibited actions

- Never overwrite the final controlled Master Manual.
- Never silently alter an old historical document to make it look current.
- Never use filename recency as authority.
- Never merge two different-content sources merely because they look similar.
- Never treat a model consensus as proof.
- Never call a hypothetical patent mechanism implemented unless physically built and tested.
- Never claim teacher approval without actual approval evidence.
- Never turn a recommendation into a final selection without a controlling record.
- Never claim Phase 4 or procurement started from folder structure, BOMs or plans alone.
- Never call patentability established or FTO clear from internal research.
- Never overwrite a different-content collision.
- Never delete failed, superseded or historical evidence to simplify the repository.
- Never create Decision Register v1.3 or Master Manual v1.1 without an authorized decision/release event.

---

**Maintenance principle:** preserve chronology, preserve provenance, separate authority from evidence, and make each post-freeze change reversible and auditable.
