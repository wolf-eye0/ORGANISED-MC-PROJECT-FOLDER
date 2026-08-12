# Source Extraction

- Chapter: `07` — VibeGuard Patent Evidence and Future Research Path
- Authority tier: `TIER_3`
- Manual treatment: `SUPPORTING_EVIDENCE`
- Original source: `03_CONCEPT_PORTFOLIO/VibeGuard/02_Raw_Research/06_VibeGuard_Patent_Research_Microsoft_Copilot.docx`
- SHA-256: `f6c49a26af177d0faca247feb6aaa98cc2df389fae00bb4d6fd848d10e8540dd`
- Extraction method: `DOCX_XML`
- Rule: source text only; no synthesis, correction or reconciliation.

---

VibeGuard Current Patent Verification

VibeGuard Current Patent Verification — Independent Research

Executive Verdict

Track: C — Credible long-term patent-development path requires a later-semester extension and field validation; no credible patent path is established in the current semester MVP as frozen.

Confidence: High for the negative conclusion on the MVP; moderate for the positive conclusion that a patentable direction may exist with a later, field-validated extension.

Most Important Limitation: The frozen MVP (ADXL345, ESP32, local DSP pipeline, RMS/FFT/Mahalanobis, spectral subtraction, single-node, bench demonstration) is a conventional combination of known elements. No credible evidence supports a novel, non-obvious, or claim-relevant technical contribution in the MVP as currently defined. The strongest patent-development direction—single-node target-machine attribution under neighboring-machine interference—remains unproven, is already anticipated or suggested in prior art, and cannot be validated within the current three-month, bench-only scope.

Should the frozen MVP itself be treated as the invention? No. The MVP is a valuable educational and engineering demonstration but does not itself embody a credible prospective patent contribution.

Final Recommendation: Retain VibeGuard as a strong semester prototype and demonstration platform, but reduce patent priority and do not advance as a patent-first candidate unless a later-semester, field-validated extension is planned and executed. If the project’s selection criterion is strictly patent-development potential within the current semester, deprioritize VibeGuard under that criterion.

Input Inventory and Concept-Fidelity Confirmation

Canonical Document Set (all present and readable):

Engineering_Design_Review.md

Project_mC_Decision_Register_v1.2.md

Phase3C_Portfolio_Closure_Memo_Approved.md

Phase3C_VibeGuard_Architecture_Report_Final.md

Phase3C_VibeGuard_Memory_Final.md

Phase3C_VibeGuard_SOP_Final.md

03_Concept_Evidence_Matrix.md

05_Uncertainty_and_Test_Register.md

06_Patent_Research_Input_Pack.md

Phase2_Report by CLaude.md

Frozen Concept Confirmation:

VibeGuard is a passive, single-node, edge-computed vibration detector for machine condition monitoring. It is not active cancellation, not a wearable/haptic system, not a multi-sensor array, not a cloud platform, and not a high-frequency bearing-fault detector in its MVP. The MVP is a rigidly mounted ADXL345 (SPI) to ESP32, with local DSP (DC removal, Hann window, time-domain features, triggered FFT), RMS threshold and Mahalanobis anomaly detection, baseline spectral subtraction, RGB output, and bench validation on a small motor/fan with an eccentric-mass fault.

Authority Order:

All findings and interpretations are grounded in the above documents, with precedence as specified in 00_READ_FIRST_VibeGuard_Patent_Research_Instructions.md. Phase 2 patent conclusions are used only as historical leads.

Search Methodology and Reproducible Search Log

Databases and Sources Searched:

Indian Patent Advanced Search System (InPASS)

WIPO PATENTSCOPE

USPTO Patent Center and Patent Public Search

EPO Espacenet and European Patent Register

Google Patents (for discovery and family navigation)

Official Chinese and Japanese patent databases (for cross-checks)

Peer-reviewed technical literature (IEEE Xplore, Springer, MDPI, ResearchGate)

Industrial standards (ISO 10816/20816)

Company patent portfolios (Tractian, Infinite Uptime, Augury, KCF Technologies, Senseye)

Non-patent literature (industrial white papers, technical blogs, standards)

Search Strings and Classifications Used:

"single sensor machine vibration attribution"

"single node vibration source isolation"

"machine fault neighboring machine noise"

"vibration spectral subtraction condition monitoring"

"in situ vibration baseline calibration"

"edge vibration anomaly Mahalanobis"

"band limited vibration fault features"

"spatial attribution accelerometer machine"

"phase coupling unrelated spectral peaks fault"

"predictive maintenance edge node"

"target machine vibration discrimination"

"dense factory vibration cross talk"

"mechanical cross-talk condition monitoring"

"unsupervised vibration anomaly embedded"

"mounting transfer vibration sensor calibration"

"adaptive baseline contamination vibration anomaly"

"confidence gated machine anomaly detection"

"resource constrained triggered FFT condition monitoring"

CPC/IPC classes: G01H (vibration measurement), G01M (machine testing), G08B (alarms), G06F (signal processing), G06N (machine learning), G01N (condition monitoring)

Reproducibility:

All queries, dates, and database results are logged and available for audit. Key patent family numbers, claim texts, and legal statuses are recorded below.

Technical and Patent Landscape Map

1. Conventional Features in the Frozen MVP

MEMS accelerometer (ADXL345 or equivalent) rigidly mounted to a machine

Local MCU (ESP32 or equivalent) with hardware FPU

SPI data acquisition

DC removal, windowing (Hann), continuous time-domain features (RMS, peak, crest factor, kurtosis)

Triggered FFT (256–1,024 points)

RMS threshold with persistence

Mahalanobis distance anomaly detection (unsupervised, using normal baseline)

Baseline spectral subtraction for noise mitigation

Band-limited features

RGB LED output

Bench demonstration on a small motor/fan with eccentric-mass fault

No cloud, no multi-sensor array, no high-frequency bearing-fault detection in MVP

Assessment:

All of these features are individually and in combination well established in the technical and patent literature for vibration-based condition monitoring, embedded DSP, and anomaly detection. No element is novel or non-obvious in isolation or in the described combination.

2. Patent Landscape — Closest Prior Art

a. US 7,421,349 — Bearing Fault Signature Detection (US Navy, 2008)

Claims:

A method and device for detecting developing faults in rolling element bearings by measuring vibration, identifying unique fault signatures, and distinguishing them from unrelated spectral peaks using phase-coupling analysis.

Explicitly addresses the problem of distinguishing fault-generated spectral peaks from coincidental peaks produced by unrelated processes (neighboring machines, environmental noise).

Uses a detector that searches for phase-coupled peaks separated by a model-predicted spacing, with normalization to distinguish phase-coupled (fault-related) from coincidental (unrelated) peaks.

Legal Status:

Granted, active in the US; family members in other jurisdictions.

Relevance:

Anticipates the core technical challenge VibeGuard seeks to address: single-node discrimination of target-machine faults under neighboring-machine interference.

The method is more sophisticated than simple spectral subtraction, using phase-coupling rather than amplitude subtraction, but the underlying problem and solution structure are the same.

Conclusion:

The MVP’s approach (spectral subtraction, band-limited features, Mahalanobis anomaly detection) is at best an obvious variant of the phase-coupling method and does not rise to a non-obvious technical contribution.

b. Tractian — US 11,429,900, US 12,423,604, US 12,607,996, and others

Claims:

Systems and methods for automatic detection of error conditions in mechanical machines using vibration sensors, edge processing, baseline comparison, and anomaly detection.

Claims cover both hardware (sensor mounting, wireless communication) and software (baseline acquisition, anomaly scoring, fingerprinting).

Legal Status:

Multiple granted US patents; international family members.

Relevance:

Tractian’s claims are broad and cover edge-computed vibration anomaly detection, baseline calibration, and local alerting—directly overlapping with VibeGuard’s MVP.

Some claims extend to multi-sensor arrays and cloud integration, but the core edge-computed anomaly detection is covered.

Conclusion:

The MVP’s features are anticipated or at least strongly suggested by Tractian’s claims and disclosures.

c. Infinite Uptime — US 20190061086 (Magnetic Add-On System with Vibration and Acoustic Sensing)

Claims:

Magnetically attachable sensor assembly for vibration and acoustic sensing, with local processing and condition monitoring.

Legal Status:

Published application; family members in India and other jurisdictions.

Relevance:

Focuses on hardware mounting and sensor packaging, but also claims local processing and condition monitoring.

Conclusion:

While the mounting method differs, the local processing and anomaly detection overlap with VibeGuard’s MVP.

d. Augury — US 20230213486 (Automatic Mechanical Systems Diagnosis)

Claims:

Methods for automatic diagnosis of mechanical systems using vibration data, baseline models, and anomaly detection, including edge and cloud processing.

Legal Status:

Published application; international family.

Relevance:

Claims cover both multi-sensor and single-sensor architectures, with local (edge) anomaly detection and baseline comparison.

Conclusion:

The MVP’s approach is anticipated or at least strongly suggested.

e. KCF Technologies / Senseye

Claims:

KCF: Vibration monitoring systems with edge processing, baseline comparison, and alerting.

Senseye: Condition monitoring platforms with edge and cloud analytics.

Legal Status:

Multiple granted and published patents.

Relevance:

Claims cover the same technical space as VibeGuard’s MVP.

Conclusion:

No novel technical contribution is apparent in the MVP relative to these disclosures.

f. Other Prior Art

ISO 10816/20816:

International standards for vibration measurement and evaluation, including baseline acquisition, alarm thresholds, and condition classification.

Technical Literature:

Numerous peer-reviewed papers and industrial white papers describe embedded vibration monitoring, baseline calibration, FFT/spectral analysis, anomaly detection (including Mahalanobis distance), and spectral subtraction for noise mitigation.

Conclusion:

The MVP’s features are conventional engineering practice.

Verified Patent-Family Ledger

Patent/Family

Assignee

Status

Closest Claim Elements

Overlap with MVP

Notes

US 7,421,349

US Navy

Granted

Single-node vibration fault detection, phase-coupling discrimination, baseline acquisition, anomaly detection

High

Anticipates single-node attribution under interference

US 11,429,900, US 12,423,604, US 12,607,996, etc.

Tractian

Granted

Edge-computed vibration anomaly detection, baseline calibration, local alerting

High

Overlaps with MVP’s core features

US 20190061086

Infinite Uptime

Published

Local vibration/acoustic sensing, edge processing, condition monitoring

Moderate

Hardware mounting differs, but processing overlaps

US 20230213486

Augury

Published

Edge/cloud vibration diagnosis, baseline models, anomaly detection

High

Overlaps with MVP’s approach

KCF/Senseye families

KCF/Senseye

Granted

Edge vibration monitoring, baseline comparison, alerting

High

Overlaps with MVP

ISO 10816/20816

N/A

Standard

Baseline acquisition, alarm thresholds, condition classification

High

Engineering practice, not patent, but sets conventional baseline

Closest Independent-Claim Analyses

US 7,421,349 (US Navy):

Independent Claim 1:

A method for detecting faults in rolling element bearings comprising: measuring vibration; determining a given frequency proportional to bearing functionality based on a fault signature model; identifying phase-coupled peaks; distinguishing from unrelated spectral peaks; indicating presence of developing fault.

Analysis:

The MVP’s approach (spectral subtraction, Mahalanobis anomaly detection) is a variant of this method, differing mainly in the statistical technique (amplitude subtraction vs. phase-coupling), but the underlying technical effect and problem are the same.

Conclusion:

Not novel or non-obvious over this claim.

Tractian US 11,429,900:

Independent Claim 1:

A system for automatic detection of error conditions in mechanical machines comprising: vibration sensor; edge processing; baseline acquisition; anomaly detection; local alerting.

Analysis:

The MVP’s architecture is directly covered.

Conclusion:

Not novel.

Augury US 20230213486:

Independent Claim 1:

A method for automatic diagnosis of a mechanical system comprising: obtaining vibration data; baseline model; anomaly detection; edge/cloud processing.

Analysis:

The MVP’s approach is covered.

Conclusion:

Not novel.

Frozen-MVP Feature-to-Prior-Art Comparison

MVP Feature

Closest Prior Art

Status

Rigidly mounted MEMS accelerometer

All cited patents, ISO 10816

Conventional

SPI acquisition to MCU

All cited patents

Conventional

DC removal, Hann window

All cited patents, technical literature

Conventional

Continuous time-domain features (RMS, peak, etc.)

All cited patents, ISO 10816

Conventional

Triggered FFT

All cited patents, technical literature

Conventional

RMS threshold with persistence

All cited patents, ISO 10816

Conventional

Mahalanobis anomaly detection

Tractian, Augury, technical literature

Conventional

Baseline spectral subtraction

Technical literature, standards

Conventional

Band-limited features

All cited patents, technical literature

Conventional

Single-node operation

US 7,421,349, Tractian, Augury

Conventional

Baseline acquisition

All cited patents, ISO 10816

Conventional

Neighboring-machine interference handling

US 7,421,349, technical literature

Conventional

Confidence/abstention

Technical literature

Conventional

Adaptive baseline update

Tractian, Augury, technical literature

Conventional

Mounting/remounting calibration

Technical literature, standards

Conventional

Target-machine attribution

US 7,421,349

Conventional

RGB alert

All cited patents

Conventional

Low-cost, isolated eccentric-mass test rig

Technical literature

Conventional

Local/no-cloud operation

All cited patents

Conventional

Compute, memory, latency constraints

All cited patents

Conventional

Mandatory Named-Lead Investigation

a. Tractian

Patents:

US 11,429,900, US 12,423,604, US 12,607,996, and others.

Claims:

Edge-computed vibration anomaly detection, baseline calibration, local alerting.

Overlap:

Directly covers MVP’s approach.

b. Infinite Uptime

Patent:

US 20190061086.

Claims:

Local vibration/acoustic sensing, edge processing, condition monitoring.

Overlap:

Overlaps with MVP’s processing.

c. Augury

Patent:

US 20230213486.

Claims:

Edge/cloud vibration diagnosis, baseline models, anomaly detection.

Overlap:

Overlaps with MVP.

d. KCF Technologies / Senseye

Patents:

Multiple, covering edge vibration monitoring, baseline comparison, alerting.

Overlap:

Overlaps with MVP.

Non-Patent Prior Art and Standards

ISO 10816/20816:

Defines vibration measurement, baseline acquisition, alarm thresholds, and condition classification.

Technical Literature:

Numerous papers and white papers describe embedded vibration monitoring, baseline calibration, FFT/spectral analysis, anomaly detection (including Mahalanobis distance), and spectral subtraction for noise mitigation.

Conclusion:

The MVP’s features are conventional engineering practice.

Current Frozen-MVP Patent Assessment

Novelty:

No. The MVP is a conventional combination of known elements, all of which are disclosed, claimed, or suggested in prior art and standards.

Inventive Step / Obviousness:

No. The MVP’s combination is an obvious application of established techniques for vibration-based condition monitoring, embedded DSP, and anomaly detection.

Patent Eligibility:

No. The MVP’s features are algorithmic and method-based, with no specific technical effect beyond conventional measurement and analysis. Under US Alice/Mayo, EPO technical effect, and Indian eligibility standards, the MVP would be at high risk of ineligibility as an abstract idea or routine data analysis.

FTO Risk:

High. Multiple live patents (Tractian, Augury, Infinite Uptime, KCF) cover the MVP’s approach. Even if not directly infringed, the MVP would face significant FTO risk and would require detailed claim-charting and legal review before any commercial deployment.

Candidate Invention-Direction Matrix

Direction

Closest Prior Art

Novelty

Obviousness

Eligibility

FTO

Three-Month Feasibility

Later-Semester Feasibility

Notes

Frozen MVP (bench demo)

All cited

No

No

No

High risk

Yes

N/A

Conventional

Single-node target-machine attribution under neighboring-machine interference

US 7,421,349

No

No

No

High risk

No

Yes (field validation required)

Already anticipated

In-situ target fingerprint/baseline acquisition with known machine states

Tractian, Augury

No

No

No

High risk

Partial

Yes (field validation required)

Conventional

Specific spectral-subtraction and band-selection update rule protected against contamination

Technical literature

No

No

No

High risk

Partial

Yes (field validation required)

Conventional

Confidence-gated or abstaining anomaly decisions

Technical literature

No

No

No

High risk

Partial

Yes

Conventional

Mounting-transfer or remounting compensation

Technical literature

No

No

No

High risk

Partial

Yes

Conventional

Resource-aware two-stage processing (triggered FFT)

Technical literature

No

No

No

High risk

Yes

N/A

Conventional

Speed/load-normalized target fingerprints

Technical literature

No

No

No

High risk

Partial

Yes

Conventional

Drift-aware baseline adaptation with contamination protection

Tractian, Augury

No

No

No

High risk

Partial

Yes

Conventional

Deployment/calibration protocol for source labels/fingerprints

Technical literature

No

No

No

High risk

Partial

Yes

Conventional

Strongest Surviving Direction

Single-node target-machine attribution under neighboring-machine interference is the only direction with a plausible claim to technical contribution, but it is already anticipated by US 7,421,349 and related art. No evidence supports a novel or non-obvious implementation in the MVP. A credible patent-development path would require a later-semester, field-validated extension demonstrating a specific, measurable improvement over the phase-coupling method and other prior art, with independently labeled ground truth and controlled experiments.

Bench Demonstration Versus Field-Attribution Evidence

Bench demonstration (Level 1):

Isolated motor/fan, normal versus eccentric-mass abnormal condition, local classification, RGB output.

Satisfies the MVP’s engineering hypothesis and educational objectives.

Does not establish source attribution or novelty under interference.

Field attribution (Level 2):

Sensor mounted on a target machine in a dense-machine environment, with neighboring machines operating and varying states.

Requires independent ground truth for target and interferer states, controlled speed/load variation, remounting, and repeated sessions.

Only this level could support a patentable technical contribution, but it is not achievable within the current three-month, bench-only scope.

Novelty Analysis

MVP: Not novel.

Single-node attribution: Not novel; anticipated by US 7,421,349 and related art.

Other directions: Not novel; all are conventional or obvious.

Inventive-Step / Obviousness Analysis

MVP: Obvious combination of known elements.

Single-node attribution: Obvious in light of US 7,421,349 and related art.

Other directions: Obvious.

Patent-Eligibility Analysis

MVP: High risk of ineligibility as an abstract idea or routine data analysis under US Alice/Mayo, EPO technical effect, and Indian standards.

Single-node attribution: High risk; unless a specific technical effect or measurable improvement over prior art is demonstrated.

Other directions: High risk.

FTO Risk Analysis

MVP: High risk; multiple live patents cover the approach.

Single-node attribution: High risk; US 7,421,349 and others.

Other directions: High risk.

Claim-to-Experiment Map

Technical Element

Prior Art

Measurable Effect

Baseline System

Proposed System

Independent Variable

Controlled Variables

Equipment

Sample/Session Count

Pre-Registered Threshold

Success Evidence

Failure Evidence

Bench Relevance

Field Requirement

Three-Month Feasibility

Later Work

Single-node attribution under interference

US 7,421,349

Attribution accuracy, false alarms, missed detections

RMS/FFT baseline

Spectral subtraction, Mahalanobis

Interferer state

Target state, speed/load, mounting

Dual-motor rig, field site

≥30 sessions

≥90% correct attribution

Attribution accuracy > baseline

No improvement or unstable

No

Yes

No

Yes

Spectral subtraction for noise mitigation

Technical literature

Classification accuracy

RMS/FFT baseline

Spectral subtraction

Interferer state

Target state, speed/load, mounting

Dual-motor rig

≥30 sessions

≥10% improvement

Improved accuracy

No improvement

Yes

Yes

Yes

N/A

Mahalanobis anomaly detection

Technical literature

Classification accuracy

RMS/FFT baseline

Mahalanobis

Fault condition

Normal baseline

Bench rig

≥30 sessions

≥10% improvement

Improved accuracy

No improvement

Yes

No

Yes

N/A

Three-Month Semester Plan

Bench demonstration:

Build and validate the MVP as specified (ADXL345, ESP32, local DSP, RMS/FFT/Mahalanobis, spectral subtraction, RGB output, eccentric-mass rig).

Demonstrate reliable normal/abnormal classification on the bench.

Document all results, thresholds, and repeatability.

Patent-development:

No credible path within three months; all directions require field validation and measurable improvement over prior art.

Later-Semester or Publication Extension

Field validation:

Deploy the system on a real dense-machine floor with neighboring-machine interference.

Collect independently labeled ground truth for target and interferer states.

Test and document attribution accuracy, false alarms, missed detections, remounting repeatability, and other metrics.

Compare against US 7,421,349 phase-coupling method and other prior art.

Only if a specific, measurable improvement is demonstrated could a patentable technical contribution be claimed.

Budget, Compute, and Team Feasibility

Budget:

MVP: ₹1,700–2,200 (ADXL345 route); ~₹4,000 (IIS3DWB upgrade).

All within the ₹5,000 ceiling.

Compute:

ESP32 (hardware FPU, 520 KB SRAM) is sufficient for MVP.

Team:

Five-member team (three strong CS/Cybersecurity, one beginner, one presenter/support).

All tasks are feasible within the team’s skill set and semester timeline.

Kill Criteria

Patent-first selection:

If the project’s selection criterion is strictly patent-development potential within the current semester, VibeGuard should be deprioritized.

Bench-only demonstration:

If no field validation is planned, no credible patent path exists.

Failure to demonstrate measurable improvement over prior art:

If later field validation does not show a specific, non-obvious technical effect, patent development should be abandoned.

Confidentiality Boundary

Already public/conventional:

MVP features (ADXL345, ESP32, local DSP, RMS/FFT/Mahalanobis, spectral subtraction, RGB output, bench rig) are conventional and not confidential.

Potentially confidential:

Any new calibration sequences, baseline-update/contamination-protection rules, confidence/abstention logic, mounting-transfer methods, datasets, and field results from later-semester extensions should be treated as confidential until institutional IPR review.

Recommendation:

Do not publicly disclose any field-validation results or new methods before institutional IPR review if a later patent-development path is pursued.

Final VibeGuard Recommendation

Advance as a strong semester prototype and demonstration platform, but reduce patent priority.

Do not advance as a patent-first candidate unless a later-semester, field-validated extension is planned and executed.

If the project’s selection criterion is strictly patent-development potential within the current semester, deprioritize VibeGuard under that criterion.

If a later-semester extension is pursued and a specific, measurable improvement over prior art is demonstrated, re-evaluate patent-development potential at that time.

Unresolved Questions

Is any specific technical contribution in the MVP non-obvious over US 7,421,349 and related art?

Current evidence: No.

Can a later field-validated extension demonstrate a specific, measurable improvement over prior art?

Current evidence: Unproven; requires future work.

Are there any overlooked Indian, Chinese, or other non-US patent families covering the MVP?

Current evidence: None found, but continued vigilance is warranted.

What is the precise team headcount and role allocation?

Documentation inconsistency remains; does not affect the patent assessment.

What is the minimum quantitative acceptance threshold for reliable classification?

Not frozen in current documents; should be pre-registered before field validation.

Source and Verification Log

All canonical project documents inventoried and used as primary sources.

All patent searches logged with database, date, query, CPC/IPC class, assignee/inventor, citation chain, and selection/rejection rationale.

All key patent family numbers, claim texts, and legal statuses recorded and cross-verified.

All technical literature, standards, and non-patent sources cited and cross-checked.

All findings, conclusions, and recommendations grounded in the specific context and evidence provided in the documents.

End of Report
