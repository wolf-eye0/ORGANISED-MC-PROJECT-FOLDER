# Project mC Master Manual

## Appendices A3 and A4

## Document control

| Field | Value |
|---|---|
| Document | Project mC Master Manual — Appendices A3 and A4 |
| Controlled filename | `Project_mC_Master_Manual_Appendices_A3_Glossary_and_A4_Open_Decisions_Change_Log.md` |
| Status | Controlled draft |
| Scope | Glossary, consolidated open decisions and major controlled change log |
| Input control | Exactly 13 physical Markdown attachments were present and readable; all externally hash-controlled files matched the manifest byte counts and SHA-256 values; the self-referential manifest was used only for file control |
| Source boundary | Only the attached governing controls, validated Parts I–VI, mechanically generated Appendices A1–A2, required template and manifest were used |
| Technical effect | Does not amend validated Parts I–VI or any frozen concept architecture |
| Approval effect | Does not approve a concept, platform, Phase 4, procurement, safety plan or validation protocol |
| Patent effect | No patentability, filing, infringement, novelty, inventive-step or freedom-to-operate conclusion |
| External verification | Not performed; current prices, specifications, standards, legal status, facilities and physical performance remain unverified |
| Relationship to A1/A2 | Appendices A1 and A2 are mechanically generated and are not rewritten here |

# Appendix A3 — Glossary and Acronyms

## A3.1 Purpose and use

This glossary provides controlled reading definitions for terms materially used across the Project mC Master Manual. It is interpretive support, not a substitute for the controlling chapter, architecture lock, decision register, test protocol or source ledger. Where a term has a general technical meaning, the definition below states the narrower Project mC use. Definitions do not convert proposed targets into measured results, recommendations into approvals, or future research hypotheses into implemented features.

## A3.2 Project governance and lifecycle terms

| Term | Expansion | Project mC meaning | Scope or caution | Principal location |
|---|---|---|---|---|
| Authority hierarchy | — | Ordered rule for resolving disagreement among teacher records, Decision Register v1.2, final architectures, memories/SOPs, comparative evidence, syntheses, research lanes and historical/archive material. | A lower source cannot silently override a higher source. | Part I, Chapter 01; Part VI, Chapter 14 |
| Authority tiers | TIER_1–TIER_5 | Source classes descending from current governance/architecture authority through decision support, research, historical material and procedural/archive controls. | Lower tiers cannot override higher ones; TIER_5 proves procedure or identity only. | Parts I and VI |
| Decision Register v1.2 | Project mC Decision Register version 1.2 | Canonical project decision record for current documented controls, including portfolio, architecture and governance decisions. | Versions 1.0 and 1.1 are historical or superseded and cannot override v1.2. | Part I, Chapter 01; Part VI, Chapter 13 |
| PDR | Project Decision Record | Identifier used for individual recorded decisions within the Decision Register. | A PDR controls only the decision it actually records. | Part I, Chapter 01 |
| REFERENCE_ONLY | Reference-only authority class | Peer or class-project material retained for contextual comparison. | Does not vote on concept selection or override Project mC architecture. | Appendix A2 |
| Frozen architecture | — | The one authoritative Phase 3C architecture selected for a retained concept. | May receive allowed refinements, but replacement requires formal change control. | Parts II–IV |
| Architecture lock | — | Explicit boundary stating what a frozen concept is and is not. | Prevents concept swaps, hybrids and later patent hypotheses from being backfilled into the semester MVP. | Parts II–IV |
| Semester MVP | Minimum Viable Prototype | Bounded student implementation used to demonstrate the frozen concept’s ordinary engineering objective. | A successful MVP does not prove novelty, patentability, product readiness or later research mechanisms. | Parts I–V |
| Discovery and analysis phases | Phases 1A, 1B and 1B.5 | Progression from problem discovery to clustering/ranking and practical portfolio gates. | Historical 22 survivors were corrected to 16 valid Phase 1C inputs. | Part I, Chapter 02 |
| Concept and landscape phases | Phases 1C and 2 | Creation of one high-level concept per valid survivor followed by historical patent-landscape work. | Broad names and early patent impressions do not define current architecture or legal status. | Part I, Chapter 02 |
| Engineering and architecture phases | Phase 3A, EDR, Phase 3B and Phase 3C | Engineering landscape, hypothesis stabilization, feasibility assessment and one frozen architecture for each retained concept. | Phase 3C is complete for OpenBraille, VibeGuard and TrueMoist only. | Part I, Chapter 02 |
| Phase 4 | Implementation phase | Future project-wide execution stage covering authorized procurement, build, integration and evidence generation. | Not proved started in the attached record. | Parts I and V |
| Hard gate | — | Predefined pass/fail decision point requiring named evidence before a branch may advance. | A failed gate requires iteration, narrowing, closure or change control—not hidden substitution. | Parts I–V |
| Kill criterion | — | Pre-registered condition requiring a hypothesis, mechanism or route to stop or be redesigned. | Prevents post-hoc preservation of an unsupported patent or performance narrative. | Parts II–V |
| Change control | — | Logged process for revising architecture, source mapping, approval state, tests, BOM or release material while preserving the prior state. | Canonical files and frozen maps must not be silently overwritten. | Parts V and VI |
| Teacher approval | — | Explicit recorded acceptance, conditional acceptance or rejection by the teacher or course authority. | A deck, request, roadmap or adjudication is not approval. | Parts I and V |
| Course-platform acceptance | — | Explicit authorization of the exact board/toolchain or an approved controlled substitution. | ESP32-class architectures exist, but final ESP32/STM32 acceptance remains unresolved. | Parts I and V |
| Chapter 11 zero-source boundary | — | Record that Chapter 11 has zero directly mapped execution sources and is therefore a future framework. | It does not prove procurement, coding, fabrication, testing or completion. | Part V, Chapter 11; Part VI, Chapter 14 |
| BOM | Bill of Materials | Controlled list of exact parts, quantities, specifications, suppliers and cost assumptions for an authorized build. | Historical BOMs are planning evidence; procurement requires current verification and approval. | Parts II–V |
| Configuration ID | Configuration Identifier | Versioned identifier linking hardware, firmware, CAD, calibration, wiring, rig and test records. | Unversioned evidence cannot support final acceptance claims. | Parts II–V |

## A3.3 OpenBraille terms

| Term | Expansion | Project mC meaning | Scope or caution | Principal location |
|---|---|---|---|---|
| OpenBraille | — | Retained accessibility/mechatronics concept: one non-standard macro six-dot tactile cell using six servo/cam/pin channels and ESP32 control. | Not an ISO-compliant cell, commercial display, fluent-reading device or approved build. | Part II, Chapter 04 |
| Macro six-dot cell | — | Enlarged permanent six-dot educational tactile cell selected to reduce fabrication risk. | Macro scale does not establish practical Braille pitch, product density or user readiness. | Part II, Chapter 04 |
| SG90-class servo | — | Commodity micro-servo class used as one actuator per tactile dot. | Seller label, commanded angle or current spike does not prove torque, endpoint or tactile state. | Part II, Chapter 04 |
| Eccentric cam/follower | — | Mechanical conversion channel that translates servo rotation into guided vertical pin motion. | Geometry, friction, coupling, wear and return require physical testing. | Part II, Chapter 04 |
| Guided tactile pin | — | Rounded vertical pin constrained by a guide to represent a raised or lowered dot. | Physical state must be established by external measurement during calibration and validation. | Part II, Chapter 04 |
| Active retraction | — | Deliberate servo-and-cam command that drives a dot to its lowered state. | Controlling fallback because passive return is unproved. | Part II, Chapter 04 |
| Single-dot-first commissioning | — | Mandatory one-channel coupon build and validation before six-dot integration. | Prevents replication of the same mechanical, power or calibration defect across six channels. | Part II, Chapter 04 |
| Physical-state oracle | — | Independent displacement, force or equivalent ground truth used to determine actual pin state. | Servo angle, elapsed time and current alone are insufficient. | Part II, Chapters 04–05 |
| D11 | — | Separate post-MVP hypothesis for mechanically referenced, individually calibrated, sensor-minimal tactile-state verification and bounded recovery. | Current/voltage may support diagnosis but never certify tactile state; D11 is not part of the frozen MVP. | Part II, Chapter 05 |
| VPD-C7 | Verified Pin-Datum Cell | Separate guide/pin/datum coupon hypothesis in which a pin-side datum may also provide low-energy endpoint evidence. | Must remain separate from D11 and the semester cell; no built or validated C7 result exists. | Part II, Chapter 05 |

## A3.4 VibeGuard terms

| Term | Expansion | Project mC meaning | Scope or caution | Principal location |
|---|---|---|---|---|
| VibeGuard | — | Retained industrial-monitoring concept using one rigid ADXL345-class sensor, an ESP32, local features, RMS/persistence, supporting FFT, RGB and USB evidence on a controlled rig. | Strongest semester-build recommendation, but not proved teacher-approved. | Part III, Chapter 06; Part I, Chapter 09 |
| ADXL345-class | — | Low-cost tri-axis accelerometer class used as the permanent target-mounted vibration sensor. | Exact purchased module, authenticity, range, bandwidth and mounting require verification. | Part III, Chapter 06 |
| SPI | Serial Peripheral Interface | Digital bus used for accelerometer acquisition in the frozen VibeGuard architecture. | Achieved sampling and data integrity must be measured on the exact configuration. | Part III, Chapter 06 |
| RMS | Root Mean Square | Mandatory minimum time-domain vibration magnitude feature used against a calibrated baseline. | Threshold values and session structure remain to be pre-registered. | Part III, Chapter 06 |
| Persistence | — | Requirement that an abnormal condition continue across a defined duration or number of windows before alerting. | Reduces transient false alerts; exact values are not yet approved. | Part III, Chapter 06 |
| FFT | Fast Fourier Transform | Supporting frequency-domain analysis triggered or scheduled to explain and compare vibration changes. | It is supporting evidence, not automatic bearing diagnosis or a patent mechanism. | Part III, Chapter 06 |
| Mahalanobis comparator | — | Optional ordinary multivariate distance comparison against a normal baseline. | Added only after acquisition integrity and basic baseline gates pass; drop if unstable or non-incremental. | Part III, Chapter 06 |
| Level 1 | — | Semester scope: controlled normal-versus-induced-abnormal detection on a bounded rig. | Does not establish diagnosis, source attribution or dense-machine operation. | Part III, Chapter 06 |
| Level 2 | — | Later research scope involving target attribution, interference, remounting, transfer and protected updating. | Level-1 success is a prerequisite, not proof of Level-2 observability. | Part III, Chapter 07 |
| Target attribution | — | Determining whether a detected change originates in the monitored target rather than an interferer, load, mount or structure. | A one-sensor anomaly detector may detect change without identifying the source. | Part III, Chapter 07 |
| Non-identifiability | — | Condition in which target and interferer effects cannot be separated reliably from the available one-sensor observations. | A legitimate negative result; must not trigger a silent sensor-array or concept substitution. | Part III, Chapter 07 |
| Paired intervention contrast | — | Narrowed future test comparing target-change and interference-change structures while the other factor is held fixed. | Requires independent labels, controlled interventions and blocked held-out evaluation. | Part III, Chapter 07 |
| Abstention / Unknown | — | Explicit future output used when attribution is ambiguous, out of support or mount-invalid. | Valuable only if wrong-source error falls while useful decision coverage remains. | Part III, Chapter 07 |
| Remount invalidation | — | Default rule that a model becomes invalid after an unvalidated sensor remount and requires recommissioning. | Transfer across mounts is a separate hypothesis, not an established feature. | Part III, Chapter 07 |

## A3.5 TrueMoist terms

| Term | Expansion | Project mC meaning | Scope or caution | Principal location |
|---|---|---|---|---|
| TrueMoist | — | Retained one-soil measurement concept using analog moisture response, nearby temperature, known treatment metadata, fixed local compensation and gravimetric reference. | Not a live-EC meter, irrigation controller, universal model, online learner or approved build. | Part IV, Chapter 08 |
| Analog capacitive probe | — | Low-cost soil-moisture probe whose analog response is used by both uncompensated and compensated models. | Authenticity, coating, monotonicity, insertion repeatability and unit variation require testing. | Part IV, Chapter 08 |
| DS18B20 | — | Nearby waterproof digital temperature sensor used to measure soil temperature at controlled depth and spacing. | Ambient temperature is not a substitute; temperature input does not itself prove compensation. | Part IV, Chapter 08 |
| S0 / S1 | Salinity-treatment states 0 and 1 | Prepared-batch metadata: S0 has no deliberately added salt; S1 has one pilot-selected recorded NaCl dose. | Metadata only; not live electrical conductivity or autonomous salinity estimation. | Part IV, Chapter 08 |
| ADS1115 | — | Primary external analog-to-digital acquisition design for the probe node. | Must be compared on the same node against calibrated ESP32 ADC1; nominal resolution is not proof of better effective accuracy. | Part IV, Chapter 08 |
| 72-run design | — | Factorial design of four moisture conditions, three temperature conditions, two treatment states and three independent physical replicates. | A selected design, not proof that 72 runs were completed. | Part IV, Chapter 08 |
| Independent physical run | — | One separately prepared or independently reset soil condition with its own physical identity and records. | Repeated ADC samples from one undisturbed container are observations, not additional runs. | Part IV, Chapter 08 |
| Held-out replicate | — | Replicate 3, kept untouched during fitting and model selection for final physical evaluation. | Opening it early or tuning against it destroys the held-out claim. | Part IV, Chapter 08 |
| Grouped cross-validation | — | Model-selection method keeping all observations from one physical batch together. | Prevents electronic rereads from leaking across train and validation groups. | Part IV, Chapter 08 |
| GWC | Gravimetric Water Content | Dry-basis physical reference calculated from wet and constant dry mass. | Requires suitable scale, oven access and dry-to-constant-mass control. | Part IV, Chapter 08 |
| M0 | Model 0 | Uncompensated baseline using raw probe response only. | Compensated models must beat this baseline on the same held-out physical reference. | Part IV, Chapter 08 |
| M1 | Model 1 | Supported low-order compensated linear model using probe response, measured temperature and S0/S1 treatment code. | Final selection must be frozen before replicate 3 is opened. | Part IV, Chapter 08 |
| M2 | Model 2 | Ridge-regularized second-order candidate model evaluated only if justified by grouped training evidence. | Greater complexity is not automatically better and must not be selected post hoc. | Part IV, Chapter 08 |
| Transfer mapping | — | Future hypothesis for adapting donor calibration to a replacement or remounted probe using sparse trusted physical references. | Separate from the semester MVP; requires multi-unit evidence and strong baselines. | Part IV, Chapter 08 |

## A3.6 Patent, legal and research terms

| Term | Expansion | Project mC meaning | Scope or caution | Principal location |
|---|---|---|---|---|
| Patent hypothesis | — | Cautious statement that a specific future mechanism may contain a differentiating technical interaction worth testing and searching. | Not a claim of novelty, patentability or grant. | Parts II–IV |
| Prior art | — | Earlier patents, publications, products or public technical disclosures relevant to a mechanism. | Current primary-source review is required after the mechanism is frozen. | Parts II–IV |
| Patentability terms | Novelty; inventive step; patent eligibility | Legal requirements considered only after a mechanism is frozen and searched. | None is established for a Project mC MVP or future hypothesis. | Parts I–IV |
| FTO | Freedom to Operate | Jurisdiction- and activity-specific assessment of whether intended acts may infringe enforceable claims. | Different from patentability; unavailable without current claim-level professional review. | Parts I–IV |
| File/no-file gate | — | Decision point on whether evidence justifies preparing or pursuing a patent filing. | No positive gate has been passed for the current concepts. | Parts II–IV |
| Inventorship | — | Legal identification of human contributors to the claimed inventive conception. | Model use, authorship and project membership do not automatically determine inventorship. | Parts II–VI |
| Confidentiality boundary | — | Separation of ordinary public semester work from claim-focused or invention-sensitive future research. | Public disclosure may affect later rights; no blanket confidentiality rule is yet recorded. | Parts II–V |

## A3.7 Validation, evidence and statistics terms

| Term | Expansion | Project mC meaning | Scope or caution | Principal location |
|---|---|---|---|---|
| Preregistration | — | Freezing the test protocol, thresholds, splits, metrics and failure rules before locked validation. | Prevents post-hoc tuning against the final evidence. | Parts II–V |
| Held-out evidence | — | Data or physical sessions excluded from tuning and used only for final evaluation. | Random windows from the same physical session may not be independent held-out evidence. | Parts II–V |
| Baseline | — | Simpler conventional method used as the comparison standard for a proposed improvement. | A mechanism is weak if it does not outperform the strongest relevant baseline. | Parts II–IV |
| Ablation | — | Controlled removal of one claimed element to test whether it contributes independently. | Required for cooperative-effect and patent-development claims. | Parts II–IV |
| Leakage | — | Information from held-out or correlated observations entering training, tuning or threshold selection. | Can create falsely high performance, especially with repeated windows or ADC readings. | Parts III–IV |
| Reproducibility | — | Ability of another reviewer or operator to trace and repeat the documented process with controlled inputs. | Does not guarantee identical generative wording or identical physical outcomes. | Parts V–VI |
| RMSE / MAE | Root Mean Square Error / Mean Absolute Error | TrueMoist held-out error metrics used with subset and baseline comparisons. | Must be measured on untouched physical evidence, not inferred from fit. | Part IV, Chapter 08 |
| External verification | — | Later dated verification of current prices, specifications, suppliers, standards, official legal status or other changing external facts. | Not performed in the A3/A4 drafting stage. | Parts I–VI |
| Evidence source, not vote | — | Rule that repeated model conclusions do not become true by majority count. | Weight depends on concept fidelity, source quality, reasoning and human review. | Parts I and VI |

## A3.8 AI workflow, archive and source-integrity terms

| Term | Expansion | Project mC meaning | Scope or caution | Principal location |
|---|---|---|---|---|
| Independent research lane | — | Separately commissioned model-assisted research output used to broaden coverage and expose disagreement. | Lane count is not a vote count; partial or concept-swapped lanes retain reduced or no authority. | Part VI, Chapter 12 |
| Synthesis | — | Controlled integration of research lanes into a concept-faithful evidence position. | A valid synthesis remains decision support, not architecture or approval authority. | Parts II–IV and VI |
| Adjudication | — | Cross-concept comparative review applying common evidence and gates. | The two final adjudications agree on VibeGuard for semester build but disagree on the future patent gate. | Parts I and VI |
| Concept fidelity | — | Degree to which a report analyzes the authoritative frozen concept rather than a different problem or architecture. | Material concept swaps are excluded rather than averaged. | Parts I and VI |
| Concept swap | — | Research or synthesis that substitutes a materially different design under the same concept name. | Failed OpenBraille moving-roller and VibeGuard software-security outputs cannot re-enter current authority. | Part VI, Chapters 12–13 |
| Manifest | — | File-control list of expected attachments, sizes, hashes and roles. | Establishes package identity only; not technical evidence. | Part VI, Chapter 12; Appendix A1 controls |
| Transport and provenance controls | Launchers, governing instructions, manifests and provenance/exclusion registers | Records defining the intended task, package identity, path history and exclusions. | They support traceability but do not prove execution compliance or technical truth. | Part VI, Chapter 12 |
| Source freeze | — | Time-bounded accounting state preserving source identities, paths and hashes for manual construction. | Does not prohibit later evidence; later evidence requires a logged revision. | Part VI, Chapter 14 |
| Frozen source map | — | 301-record map assigning represented sources to manual destinations and authority/treatment categories. | A classification system, not a claim-validity ranking. | Part VI, Chapter 14; Appendix A1 |
| Unmapped-file register | — | Controlled record of organized files not assigned by the frozen chapter rules. | One concept-portfolio index remains unmapped; absence of mapping is not loss of the file. | Part VI, Chapter 14; Appendix A1 |
| Canonical source | — | Current controlled record selected to govern present citation or state. | Canonical selection preserves, rather than erases, historical variants. | Part VI, Chapters 13–14 |
| Duplicate | — | Multiple physical files representing identical or content-equivalent material. | Exact duplicate copies are one logical source and must not be counted as corroboration. | Part VI, Chapter 14 |
| SHA-256 | Secure Hash Algorithm 256-bit | Byte-identity digest used for copy validation, duplicate grouping and silent-change detection. | Proves identical compared bytes only; not truth, authority, cross-format equivalence or approval. | Part VI, Chapter 14; Appendix A1 |
| Superseded | — | Earlier valid record replaced by a later controlling version. | May be consulted for chronology but cannot override the replacement. | Part VI, Chapter 13 |
| Failed, partial and excluded outputs | — | Controlled lifecycle states for concept-swapped reports, incomplete fragments and supplements outside a blind set. | Failed material is non-evidence; partial conclusions are not reconstructed; excluded supplements need explicit later authorization. | Part VI, Chapter 13 |
| Non-reconstruction rule | — | Missing conclusions remain unavailable or partial rather than being inferred from fragments. | Applies to model outputs, approvals, results and legal conclusions. | Parts I and VI |
| Stage 10R | — | Mechanical provenance/archive/source-integrity packet stage that passed extraction but had inadequate substantive coverage for Chapters 12–14. | Zero extraction errors did not prove adequate coverage. | Part VI, Chapter 14 |
| Stage 10S | — | Controlled coverage-repair stage selecting representative substantive sources for Chapters 12–14 without altering the frozen map. | Repaired representative coverage, not exhaustive semantics or the original 301-record map. | Part VI, Chapter 14 |

## A3.9 Undefined or intentionally unresolved labels

| Label | Expansion | Project mC meaning | Scope or caution | Principal location |
|---|---|---|---|---|
| PIRG | Undefined in the controlling record | Project label for a future VibeGuard research map involving label-aware, contamination-protected, confidence-gated single-node target/interference attribution, later narrowed to paired intervention contrasts. | No expansion is authorized. PIRG is not part of the Level-1 MVP, not implemented, not validated and not a filing basis. | Part III, Chapter 07 |

## A3.10 Glossary limitations

This glossary does not freeze test numbers that the controlling Parts leave open, resolve the ESP32/STM32 course-platform question, approve the OpenBraille-to-VibeGuard shift, authorize Phase 4 or procurement, or create a combined architecture. OpenBraille D11 and VPD-C7 remain separate hypotheses. PIRG remains an undefined project label. TrueMoist’s 72-run design remains a design rather than proof of completed runs. Terms concerning patent law are used conservatively and do not replace institutional or professional legal review.

# Appendix A4 — Open Decisions and Change Log

## A4.1 Purpose and control boundary

Appendix A4 consolidates unresolved decisions and major controlled transitions already present in validated Parts I–VI. It does not create a new decision, select a concept, approve execution, infer missing teacher feedback, certify a prototype or resolve the disagreement between the two final adjudications. Every downstream action remains blocked until the authority or evidence named in the register is obtained.

## A4.2 Consolidated open-decision register

| ID | Open decision or evidence gap | Current state | Controlling part/source | Required authority or evidence | Blocked downstream action | Prohibited inference |
|---|---|---|---|---|---|---|
| A4-OD01 | Teacher decision on proposed OpenBraille-to-VibeGuard shift | Formal request exists; approval, conditions or rejection are absent | Part I, Chapters 00 and 09; Part V, Chapter 10 | Explicit dated teacher/course-authority record | Final concept freeze, concept-specific execution and procurement | “The project has changed to VibeGuard” |
| A4-OD02 | Final authorized semester concept | Open among the retained controlled records | Part I; Decision Register v1.2; Part V | Controlling decision naming one concept and scope, or an authorized conditional gate process | Phase 4 entry and branch-specific scheduling | Recommendation equals authorization |
| A4-OD03 | Exact MCU and course-platform acceptance | ESP32-class architectures are frozen; STM32/course acceptance remains unresolved | Parts I–V | Written acceptance of exact board/toolchain or controlled substitution | Exact pin map, board procurement and final firmware baseline | ESP32 is automatically accepted or automatically prohibited |
| A4-OD04 | Project-wide Phase 4 authorization | Not proved started | Parts I, V and VI | Approved entry record after concept, platform, budget, safety and ownership gates | Procurement, fabrication, coding and formal execution claims | Historical roadmaps prove implementation began |
| A4-OD05 | Procurement-ready BOM and current cost freeze | Historical BOMs exist; current specifications, Indian prices and supplier authenticity are unverified | Parts II–V; authority protocol | Dated manufacturer/supplier verification, approved exact BOM and budget | Purchasing and current-cost publication | Historical estimates are current prices or actual spend |
| A4-OD06 | Named team roles, reviewers and backups | Functional roles proposed; named assignment not signed | Parts I and V | Recorded primary owner, reviewer, backup and cross-training plan | Accountable subsystem execution and continuity | Proposed role table is final team allocation |
| A4-OD07 | Facility and safety approval | Concept dependencies and hazards identified; actual access/approval not proved | Parts II–V | Confirmed FDM/tools, rig area or oven/scale access plus responsible safety sign-off | Concept-specific build and testing | Facility availability or safety clearance is complete |
| A4-OD08 | Final quantitative success, hold-out and kill criteria | Concept-specific frameworks exist; exact approved values remain open | Parts II–V | Preregistered protocol for the authorized branch before locked validation | Acceptance testing and performance claims | Proposed thresholds are achieved results |
| A4-OD09 | Physical prototype and held-out evidence | No project-wide completed prototype or locked validation is established | Parts II–VI | Configuration-controlled hardware, firmware, run ledgers, measurements and sign-offs | Demonstrated performance, completion and publication claims | Architecture documentation proves a working prototype |
| A4-OD10 | Future patent-development gate | Final adjudications disagree on the preferred first gate and later route | Parts I–IV and VI | Authorized gate or replacement rule plus new physical evidence | Patent-first down-selection and claim-focused experiments | Model agreement or one adjudication settles the route |
| A4-OD11 | Current patent, NPL, legal-status and FTO review | Time-bounded or incomplete; no current clearance | Parts II–IV; authority protocol | Current official-source search, exact mechanism freeze and professional/institutional claim review | Filing decision, clearance statements and commercial acts | Search silence proves novelty or FTO |
| A4-OD12 | Confidentiality, ownership, contribution and inventorship | Institutional rules and human contribution chronology are unresolved | Parts I–VI | Written institutional IPR guidance and dated contribution records | Public claim-focused disclosure and filing preparation | Team membership, authorship or model output determines inventorship |
| A4-OD13 | Treatment of unmapped concept-portfolio index | One organized file remains unmapped under the frozen source rules | Part VI, Chapter 14; Appendix A1 | Logged map revision or controlled appendix/chapter assignment preserving the prior map | Claim of complete chapter assignment | Unmapped means missing, irrelevant or silently assignable |
| A4-OD14 | Final manual release and reviewer sign-off | Parts I–VI and A1/A2 exist; A3/A4 are drafted; final assembled release not signed | Part VI, Chapter 14 | Assembly validation, contradiction review, version/date, source-note check and approving reviewer | Publication as final controlled Master Manual | Draft completion equals final release |
| A4-OD17 | OpenBraille mechanical, power and tactile acceptance | Architecture frozen; one-dot mechanics, six-servo power, lifecycle and approved tactile result absent | Part II | One-dot coupon gates, measured power/grounding, locked pattern/lifecycle tests and approved blinded tactile protocol | Six-dot acceptance and bounded tactile claim | PWM/current/visual motion proves correct tactile state |
| A4-OD18 | VibeGuard acquisition, mount, rig and Level-1 criteria | Logic fixed; exact board, sampling integrity, remount repeatability, fixture and numeric protocol untested | Part III | Incoming hardware checks, rigid-mount study, achieved-rate/loss tests, safety acceptance and blocked hold-outs | Reliable Level-1 performance claim | A red/green demo proves diagnosis or attribution |
| A4-OD19 | VibeGuard PIRG and later attribution feasibility | Candidate research map only; independent labels, identifiability, useful Unknown coverage and field access absent | Part III, Chapter 07 | Separate factorial rig, temporary references, blocked sessions/remounts, strongest baselines and authorized site access | Level-2 continuation and patent-development claim | Level-1 anomaly detection proves target attribution |
| A4-OD20 | TrueMoist facilities, probe validity and 72-run throughput | Architecture selected; probe authenticity, insertion/packing repeatability, oven/scale access and throughput unproved | Part IV | Early pilots, facility confirmation, frozen preparation method and physical run ledger | Main 72-run collection and feasibility claim | Factorial design proves runs were completed |
| A4-OD21 | TrueMoist acquisition path, model freeze and held-out replicate | ADS1115/ADC1 gate, exact targets/dose, M1/M2 choice and replicate-3 test remain open | Part IV | Paired ADC evidence, pilot-frozen factors, grouped model selection, numerical equivalence and untouched final test | Compensation-success and error claims | Training fit or repeated ADC lines are held-out physical evidence |

## A4.3 Concept-specific unresolved items

### A4.3.1 OpenBraille

OpenBraille remains a legitimate retained architecture but is not the strongest current semester recommendation and is not an authorized build. Before any implementation claim, the team must resolve exact platform acceptance, FDM and measurement access, one-dot raise/retract behavior, calibrated command windows, six-channel interference, power distribution, grounding, repeatability, wear, supported pattern set and safety. A tactile claim requires an approved blinded protocol, participant conditions and stop rules; otherwise the claim must be omitted. D11 and VPD-C7 may be considered only as separate post-MVP research configurations. They must not be merged, inserted into the frozen cell or represented as tested.

### A4.3.2 VibeGuard

VibeGuard is the strongest semester-build recommendation, not an approved semester concept. The Level-1 branch still requires an approved board, verified sensor/module, rigid mount, measured sampling and timestamp integrity, a safe repeatable abnormal-state fixture, pre-registered thresholds and persistence, blocked sessions/day/remount structure, and explicit rules for FFT or Mahalanobis retention. PIRG has no authorized expansion and remains a later candidate hypothesis. It requires independent target/interferer labels, contrast identifiability, useful risk/coverage, remount validity, edge-resource evidence and field-like access. Failure of that later path would not invalidate a successful Level-1 semester result.

### A4.3.3 TrueMoist

TrueMoist remains retained but neither selected nor rejected. Its early feasibility depends on genuine probe behavior, controlled reinsertion and packing, a paired ADS1115-versus-ESP32-ADC1 gate, oven/scale access, dry-to-constant-mass workflow, final soil preparation, moisture regions, S1 dose, randomization/blocking and practical throughput. The 72-run structure is authoritative, while a 54-run contingency requires formal change control. M1 or M2 must be frozen before replicate 3 is opened, and Python-to-MCU numerical equivalence must be archived. Future replacement/remount transfer remains a separate Level-2 hypothesis and must beat simple affine-transfer and gating baselines on independent multi-unit evidence.

## A4.4 Teacher, course and execution unresolved items

The record proves the official OpenBraille zeroth-review deck dated 30 July 2026 and the later VibeGuard shift request, but contains no review outcome or approval. Final concept, platform, Phase 4, procurement, ownership, safety, schedule and demonstration decisions remain open. Chapter 11 remains conditional until direct execution records enter through change control.

## A4.5 Patent, confidentiality and IPR unresolved items

No frozen MVP is established as patentable. D11, VPD-C7, PIRG and TrueMoist transfer/validity paths remain hypotheses, and the adjudications disagree on the first later gate. Claim-focused work requires a frozen mechanism, preregistered experiments, baselines/ablations, current official-source review, FTO analysis, institutional IPR guidance, confidentiality control and dated contribution records. No filing commitment is authorized.

## A4.6 Repository, source-map and release unresolved items

The frozen source map contains 301 records and one separately recorded unmapped concept-portfolio index. Appendix A1 preserves both; Appendix A2 preserves 18 reference-only records. Any map revision must preserve the earlier map and record its reviewer and effects. Final assembly, contradiction review, release metadata and sign-off remain pending.

## A4.7 Major controlled project change log

| Change ID | Date or ordered stage | Previous controlled state | New controlled state | Reason/evidence | Approval or authority effect |
|---|---|---|---|---|---|
| CH-01 | Phase 1A | Broad domains and problem reports | Evidence-grounded opportunity set | Problems were explored before products or architectures | Historical discovery only; no concept approval |
| CH-02 | Phase 1B | Unstructured opportunity findings | 32-cluster dataset with ranked Top 20 | Duplicate preservation, clustering and weighted evaluation | Historical analysis; no solution freeze |
| CH-03 | Phase 1B.5 correction | Intermediate record reported 22 survivors | Valid Phase 1C input corrected to 16 | Six out-of-Top-20 entries had re-entered; four Top-20 entries were legitimately gated out | Corrects historical pipeline count; does not select a final concept |
| CH-04 | Phase 1C | Valid opportunity survivors | One concept per 16 survivor and historical Top Five | First permitted concept-synthesis stage | Broad concepts created; no current architecture authority |
| CH-05 | Phase 2 | Patent research assumed concept labels were understood | Concept-restatement and exclusion-over-averaging rules established | One lane materially swapped OpenBraille, VibeGuard and TrustLatch identities | Failed sections excluded; no current patent conclusion |
| CH-06 | Phase 3A, EDR and Phase 3B | Broad concept and historical patent impressions | Engineering state, stable hypotheses, minimum demonstrable success and feasibility evidence | Needed engineering fidelity before architecture freeze | Decision support strengthened; no final authorization |
| CH-07 | Final Phase 3C | Multiple candidate architectures and five historical concepts | Frozen OpenBraille, VibeGuard and TrueMoist architectures; TrustLatch and ColdTrace deferred | One architecture per completed retained concept and controlled portfolio closure | Current architecture authority established for retained three |
| CH-08 | Decision Register progression | v1.0 and v1.1 preserved earlier governance, including the superseded TrueMoist 135-run branch | v1.2 became canonical and controls the validated 72-run design and current portfolio | Later reconciliation and accepted decisions superseded the earlier states | Earlier versions remain chronology only and cannot override v1.2 |
| CH-09 | Patent synthesis audit | Mixed valid, failed, partial and supplementary outputs | Concept-faithful syntheses retained; failed swaps, partial conclusions and excluded supplement separated | Prevented mis-scoped or incomplete model work from being averaged into conclusions | Evidence quality improved; model outputs remain non-voting support |
| CH-10 | Final adjudications | Separate concept evidence and common gates | Two final comparative adjudications preserved | Both support VibeGuard for semester build but disagree on future patent route | Recommendation strengthened; future patent gate remains unresolved |
| CH-11 | Proposed concept shift | OpenBraille was the submitted semester concept | Formal request proposed VibeGuard Level 1 while retaining OpenBraille records separately | Lower implementation risk, clearer quantitative validation and stronger team fit | Request only; teacher approval absent |
| CH-12 | Repository organization and source freeze | Large working repository with variants, duplicates and archive material | Canonical organized representation, archives/exclusions and frozen accounting state | Needed traceability, duplicate control and reproducible manual construction | Source freeze recorded at `2026-08-03T21:59:10.355043+02:00`; not a technical or approval event |
| CH-13 | Master Manual drafting | Frozen source map and chapter blueprint | Validated Parts I–VI drafted under controlled packages | Converted distributed evidence into governed manual parts | Drafting does not amend source authority or approve execution |
| CH-14 | Stage 10R | Mechanical packet extraction passed | Coverage defect identified: Chapters 12–13 had zero substantive Tier 1–4 mapped sources and Chapter 14 had only two | Extraction success did not ensure substantive chapter coverage | Stage 10R not used as sufficient Part VI basis |
| CH-15 | Stage 10S repair | Inadequate representative coverage for Chapters 12–14 | Repaired selections of 17, 17 and 23 sources, with zero extraction/hash failures | Added representative substantive coverage without changing the frozen map | Post-freeze repair control only; not new pre-freeze project evidence |
| CH-16 | Mechanically generated appendices | Frozen source map and peer-reference assignments existed separately | Appendix A1 generated from 301 mapped records plus one unmapped row; Appendix A2 generated from 18 reference-only records | Required auditable source and peer-reference registers | Mechanical controls only; not technical evidence |
| CH-17 | Current appendix stage | Parts I–VI and A1/A2 available; A3/A4 pending | Controlled A3 glossary and A4 open-decision/change-log draft produced | Completes the remaining drafted appendix content before assembly | Does not itself release the complete manual |

## A4.8 Master Manual construction change log

| Manual stage | Output or event | Control result | Remaining next action |
|---|---|---|---|
| Blueprint and authority setup | Manual objective, chapter structure, authority hierarchy and contradiction rules established | Frozen concepts, source authority and approval boundaries were separated | Continue to preserve these controls during assembly |
| Validated Part I | Opening, governance, phase history, portfolio and comparative decision | VibeGuard recorded as strongest recommendation; shift, platform, Phase 4 and procurement left open | Obtain controlling teacher/course decisions |
| Validated Parts II–IV | Separate OpenBraille, VibeGuard and TrueMoist architecture/patent-path records | Architecture locks and concept-specific open decisions preserved without hybridization | Authorize one branch before execution; retain later hypotheses separately |
| Validated Part V | Teacher-review history and Chapter 11 execution framework | Official submission and change request recorded; zero-source execution boundary preserved | Add explicit teacher outcome and future direct execution records when available |
| Stage 10R audit | Initial provenance/archive/integrity packets mechanically validated | Revealed substantive coverage defect despite extraction success | Repair representative source coverage |
| Stage 10S repair | Repaired Chapter 12–14 packets and selection controls | Representative coverage restored without editing the frozen 301-record map | Use repaired basis for Part VI drafting and release audit |
| Validated Part VI | Provenance, archive, source integrity and release controls | Source freeze, canonical/duplicate rules, exclusions, limitations and open release items consolidated | Complete appendices and final assembly validation |
| Generated Appendix A1 | Complete source register | Recorded 301 frozen map rows and one unmapped register row | Preserve mechanically; revise only through controlled map versioning |
| Generated Appendix A2 | Peer project and reference register | Recorded 18 reference-only records | Preserve mechanically; do not treat as Project mC authority |
| Current A3/A4 drafting | Glossary and consolidated open decisions/change logs | Remaining non-mechanical appendix content drafted from validated Parts I–VI | Assemble complete manual, run contradiction/source-note checks and obtain reviewer sign-off |

## A4.9 Current-state summary

- VibeGuard remains the strongest semester-build recommendation.
- The proposed OpenBraille-to-VibeGuard shift is not proved teacher-approved.
- The final authorized semester concept and exact course platform remain unresolved.
- OpenBraille, VibeGuard and TrueMoist remain separate controlled records; no hybrid is authorized.
- Chapter 11 remains a future execution framework with zero directly mapped execution sources.
- Project-wide Phase 4, procurement, named role freeze and physical validation are not proved started or complete.
- Current prices, specifications, supplier authenticity, facilities and legal status require later dated verification.
- No frozen MVP is established as patentable, filed or FTO-cleared.
- The two final adjudications disagree on the preferred future patent-development gate.
- Model outputs remain evidence sources, not votes; failed, partial and excluded outputs retain their controlled status.
- The frozen source map retains one explicitly unmapped concept-portfolio index.
- Final Master Manual assembly, release validation and reviewer sign-off remain pending.

## A4.10 Appendix limitations

This appendix records what is open and what changed; it does not prove that an unresolved action later occurred. It does not authorize a procurement, prototype, participant test, facility use, patent search, disclosure or filing. Dates are included only where the validated sources provide them. Ordered stages are used elsewhere without invented dates. Future decisions should be added through an auditable revision that identifies the authority, evidence, affected architecture or source map, and prior release preserved.

# Appendices A3–A4 Source Note

The following controlled manual outputs were materially used:

- `03_VALIDATED_MASTER_MANUAL_PART_I.md` — governance, phase history, comparative decision and consolidated project open decisions.
- `04_VALIDATED_MASTER_MANUAL_PART_II_OPENBRAILLE.md` — OpenBraille architecture, validation, D11/VPD-C7 distinctions and unresolved items.
- `05_VALIDATED_MASTER_MANUAL_PART_III_VIBEGUARD.md` — VibeGuard architecture, Level-1/Level-2 boundaries, PIRG caution and unresolved items.
- `06_VALIDATED_MASTER_MANUAL_PART_IV_TRUEMOIST.md` — TrueMoist 72-run architecture, validation design, future transfer hypothesis and unresolved items.
- `07_VALIDATED_MASTER_MANUAL_PART_V_TEACHER_EXECUTION.md` — teacher-review boundary, Chapter 11 future execution framework and approval/execution open decisions.
- `08_VALIDATED_MASTER_MANUAL_PART_VI_PROVENANCE_ARCHIVE_INTEGRITY.md` — AI workflow, archive states, source freeze, Stage 10R/10S, source-map and release controls.
- `09_GENERATED_APPENDIX_A1_COMPLETE_SOURCE_REGISTER.md` — mechanical source-map and unmapped-register control.
- `10_GENERATED_APPENDIX_A2_PEER_PROJECT_AND_REFERENCE_REGISTER.md` — mechanical reference-only peer-project control.

Appendices A1 and A2 were not rewritten.
