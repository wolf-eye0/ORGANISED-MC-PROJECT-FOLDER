# VibeGuard Current Patent Evidence Synthesis

**Project:** Project mC — VibeGuard  
**Audit date:** 1 August 2026  
**Status:** Independent patent-evidence synthesis and adversarial audit  
**Scope:** VibeGuard only  
**Decision boundary:** This report does not compare VibeGuard with another Project mC concept and does not select the final Project mC winner.

> **Important limitation:** This is technical research and project decision support. It is not legal advice, a patentability opinion, a validity opinion, claim construction, an infringement conclusion, or a freedom-to-operate opinion. Any filing or commercial deployment requires qualified patent counsel, official-register checks, and a claim-specific analysis.

---

## 1. Executive verdict

### Required verdict

**Credible long-term path requiring later-semester extension.**

### Classification

- **Track:** **Track C**
- **Confidence:** **Medium**
- **Most important limitation:** The frozen semester MVP can test whether one mounted sensor distinguishes normal operation from a deliberately introduced abnormal condition on a controlled rig. It cannot establish that the same node reliably attributes an abnormal vibration to its mounted target machine when a neighbouring machine, speed/load variation, mounting variation, and environmental vibration change independently.
- **Should the frozen MVP itself be treated as the invention?** **No.**

The frozen VibeGuard MVP is a technically coherent and affordable semester system. Its sensor, embedded processor, preprocessing, time-domain features, triggered FFT, baseline comparison, Mahalanobis anomaly score, local alert, and eccentric-mass test method are individually conventional or close to established vibration-monitoring practice. The audited record does not support a credible Track A invention in that combination.

A bounded three-month programme can implement and bench-test stronger logic—particularly guarded baseline updating, an explicit **unknown/abstain** state, a dual-motor interference rig, and a remount-validity check. That work is useful and may expose a narrower technical contribution. It is not yet enough to justify Track B because the strongest patent-oriented proposition is **target-machine attribution under independently varying interference**, and the record itself requires repeated remounting, independently labelled target/interferer states, speed/load variation, and ultimately field-like or real-site validation. Those are not merely additional software tasks; they are the evidence needed to distinguish a specific technical mechanism from ordinary anomaly detection.

The strongest surviving direction is therefore a later-validated integrated method:

> **A confidence-gated, contamination-resistant target-fingerprint and baseline-management method for a single vibration node, including known-state calibration, quarantine of untrusted update samples, explicit abstention under source ambiguity, and a mounting-validity/recalibration rule.**

No verified item in the present audit was shown to anticipate that exact full sequence. That absence does not establish novelty. Most sub-elements are known or arguably suggested, so inventive-step risk remains high unless the method is precisely defined and demonstrates a reproducible physical/diagnostic effect over the closest conventional baselines.

---

## 2. Input inventory

### 2.1 Inventory result

The complete logical input set is present:

- exactly **18 uploaded files**;
- one readable governing instruction;
- all **ten** canonical project/historical documents;
- all **six** independent current research lanes;
- one readable file-control manifest;
- Project mC Decision Register **v1.2**, not v1.1.

The upload suffixes such as `(4)`, `(5)`, `(10)`, and `(11)` decorate filenames but do not create logical duplicates. File 15 is one Mistral lane represented by a compilation of three sequential incomplete fragments.

### 2.2 File-by-file control table

| No. | Uploaded file | Logical role | Format | Readability | Completeness / use |
|---:|---|---|---|---|---|
| 1 | `00_READ_FIRST_VibeGuard_Synthesis_Instructions(5).md` | Governing instruction | MD | Readable | Complete; controlling task specification |
| 2 | `01_Engineering_Design_Review(10).md` | Project authority | MD | Readable | Complete |
| 3 | `02_Project_mC_Decision_Register_v1.2(11).md` | Project authority | MD | Readable | Complete; v1.2 confirmed |
| 4 | `03_Phase3C_Portfolio_Closure_Memo_Approved(10).md` | Project authority | MD | Readable | Complete |
| 5 | `04_Phase3C_VibeGuard_Architecture_Report_Final(4).md` | Project authority | MD | Readable | Complete |
| 6 | `05_Phase3C_VibeGuard_Memory_Final(6).md` | Project authority | MD | Readable | Complete |
| 7 | `06_Phase3C_VibeGuard_SOP_Final(4).md` | Project authority | MD | Readable | Complete |
| 8 | `07_Concept_Evidence_Matrix(10).md` | Validated evidence | MD | Readable | Complete |
| 9 | `08_Uncertainty_and_Test_Register(10).md` | Validated evidence | MD | Readable | Complete |
| 10 | `09_Patent_Research_Input_Pack(11).md` | Validated evidence/search commissioning | MD | Readable | Complete; directions are leads, not conclusions |
| 11 | `10_Phase2_Report_by_Claude(11).md` | Historical patent lead | MD | Readable | Complete; historical leads only |
| 12 | `11_VibeGuard_Patent_Research_ChatGPT_DR(5).md` | Independent research lane | MD | Readable | Complete selected report |
| 13 | `12_VibeGuard_Patent_Research_Gemini(4).docx` | Independent research lane | DOCX | Readable | Structurally complete |
| 14 | `13_VibeGuard_Patent_Research_Perplexity(4).md` | Independent research lane | MD | Readable | Main report complete; appended export payload retained |
| 15 | `14_VibeGuard_Patent_Research_Qwen(4).md` | Independent research lane | MD | Readable | Structurally complete; methodology admits “simulated current” searching |
| 16 | `15_VibeGuard_Patent_Research_Mistral_PARTIAL_COMPILATION(5).md` | Independent research lane | MD compilation | Readable | **Partial; one lane; no final verdict; supporting leads only** |
| 17 | `16_VibeGuard_Patent_Research_Microsoft_Copilot(4).docx` | Independent research lane | DOCX | Readable | Structurally complete; claim/family assertions require correction |
| 18 | `99_INPUT_MANIFEST(8).md` | File-control manifest | MD | Readable | Complete; file control only, not technical evidence |

### 2.3 Authority order applied

For project identity, requirements, and architecture, this audit applies the governing precedence:

1. Engineering Design Review;
2. Project mC Decision Register v1.2;
3. approved Phase 3C closure memo;
4. final VibeGuard architecture report;
5. final VibeGuard memory;
6. final VibeGuard SOP;
7. validated down-selection evidence;
8. Phase 2 report only as historical search leads;
9. independent current research lanes as evidence requiring audit.

The owner’s current overrides—up to three months, preferred budget at or below ₹3,000, absolute ceiling ₹5,000, and the stated five-member team—control over older timeline language. The manifest is not used as technical or patent evidence.

---

## 3. Research-report reliability audit

Reliability is assigned by the quality of the material actually present, not model reputation or agreement.

| Lane | Fidelity | Search/claim quality | Major defects | Reliability assignment | Permitted use |
|---|---|---|---|---|---|
| ChatGPT Deep Research | Passed | Strongest integrated claim/experiment reasoning; identifies Track C boundary | Some family/status conclusions still depend on non-official aggregators; no counsel-grade live-claim chart | **Medium** | Main analytical evidence, subject to primary verification |
| Gemini | Passed | Useful engineering plan and proposed contamination-protection experiment | Treats a proposed rule as more patent-ready than the evidence supports; Track B depends on a bench threshold and later admits field validation is needed; patentability/FTO language overconfident | **Medium for engineering; Low/excluded in part for legal conclusions** | Use technical protocol ideas; do not adopt patentability/FTO verdict |
| Perplexity | Passed | Strong distinction between conventional MVP and later attribution; balanced experiments and risk analysis | Legal-status verification incomplete; some company-family coverage remains broad | **Medium** | Main analytical evidence, especially experimental framing |
| Qwen | Passed | Captures project architecture and candidate directions | Search date described as “simulated current”; vague family references; overconfident patentability/FTO terminology | **Low** | General corroboration and search leads only |
| Mistral partial compilation | Partial pass | Retrieves useful named patent leads and some descriptive passages | Three fragments are incomplete; no final verdict; calls ordinary features “likely novel”; treats a descriptive Mahalanobis example as direct infringement; legal/family work unfinished | **Low; excluded in part** | Retrieval leads only after independent verification |
| Microsoft Copilot | Passed | Correctly recognises conventional MVP and later evidence burden | Materially misstates some independent claims and family relationships; overstates anticipation and obviousness from non-equivalent art; lists unverified later Tractian numbers | **Low; excluded in part** | General conventionality and validation cautions only |

### 3.1 Specific Mistral disposition

The Mistral file is **one partial research lane**, not three reports and not three votes. No Track A/B/C/D conclusion is inferred. The following are excluded unless independently verified:

- statements that DC removal, Hann windowing, triggered FFT, RMS persistence, or the eccentric-mass rig are “likely novel”;
- the assertion that using Mahalanobis distance directly infringes Tractian US 11,429,900;
- unsupported patentability, novelty, infringement, and FTO conclusions;
- any implication that a feature’s absence from one selected patent proves novelty;
- any missing final conclusion.

Its retrieval of US 7,421,349, US 7,346,461, and US 11,429,900 is retained only as a lead.

### 3.2 Critical correction to the Tractian reading

US 11,429,900’s independent claim is not a generic claim to “vibration sensor + edge processing + Mahalanobis + local alert.” Claim 1 requires a more specific distributed sequence: first-device frequency processing and peak selection, transmission to a second device, reconstruction, machine-learning identification, operator confirmation, retraining, schedule determination, and instructed sampling. Mahalanobis distance appears in the specification as one optional model among many, not as the full independent claim. Therefore:

- the patent is relevant prior art for vibration fingerprints, compressed spectra, FFT peak selection, remote learning, and feedback;
- it does **not** establish that every local ESP32 Mahalanobis implementation infringes;
- a commercial FTO conclusion requires element-by-element comparison with live claims and official status records.

---

## 4. Search coverage and evidence gaps

### 4.1 Coverage achieved

The audited reports and independent verification collectively cover:

- core vibration-monitoring classes including G01H, G01M, G05B, and data-analysis classes;
- the two mandatory historical leads, US 7,421,349 and US 7,346,461;
- Tractian US 11,429,900 and its identified US/Brazil counterpart;
- Mahalanobis-based rotating-machine families associated with Mitsubishi Heavy Industries and Valqua;
- speed/frequency-space novelty detection associated with Rolls-Royce/Optimized Systems and Solutions;
- vibration-signature and interference-handling art;
- selected Augury, Infinite Uptime, and KCF families;
- the mandatory KCF identifiers US 9,271,170 and US 10,873,791;
- US 2022/0067020, which is a Ford multidimensional vehicle-sensor anomaly family rather than a KCF vibration-monitoring family;
- current US, EPO, and Indian computer-implemented-invention eligibility guidance.

### 4.2 Coverage limitations

The following remain unresolved or insufficiently verified:

1. **Official live-claim status.** Google Patents is adequate for discovery and readable claims, but its status labels are expressly non-legal assumptions. USPTO Patent Center, EPO Register, InPASS, and national records must be checked before filing or commercialisation.
2. **Indian claim coverage.** An Indian member was surfaced in an Augury family, but no complete InPASS claim/status audit was completed for every commercially relevant family.
3. **Chinese status and claims.** Chinese members were surfaced for several families, but no Chinese-language claim chart was completed.
4. **Senseye.** A GB machine-monitoring lead was surfaced, but no sufficiently reliable claim-level Senseye family ledger was established.
5. **Infinite Uptime.** A magnetic add-on sensor family was identified, but the current record does not establish a close claim overlap with the proposed baseline-protection mechanism.
6. **Non-patent literature.** The conventionality of FFT, statistical features, one-class anomaly detection, baseline learning, and sensor-mount sensitivity is well supported generally. The search is weaker for the exact combination of contamination quarantine, abstention, known-state neighbour calibration, and remount validity on a low-cost single node.
7. **Experimental evidence.** There is no attached VibeGuard dataset demonstrating target attribution, no repeated-remount study, and no independently labelled dense-machine field trial.
8. **Exact claim language for a future invention.** The project has candidate mechanisms, not a frozen invention disclosure or counsel-reviewed claim set.

The evidence gaps prevent a patentability or FTO conclusion. They do not prevent the present Track C project decision.

---

## 5. Verified patent-family ledger

“Status indication” below reports what was available from the reviewed record as of 1 August 2026. Unless explicitly stated as official, it is not a legal-status opinion.

| Family / lead | Priority | Applicant / assignee | Jurisdictions found | Status indication | Independent-claim or core subject | Novelty significance | FTO significance | Confidence / primary source |
|---|---|---|---|---|---|---|---|---|
| **US 7,421,349 B1 — Bearing fault signature detection** | 15 May 2006 | US Navy | US lead verified | Granted; current official live status unresolved | Phase-coupled frequency-domain bearing-fault signature detection designed to reduce coincidental spectral-peak confusion | Strong prior art against broad “vibration FFT identifies bearing faults” propositions; not an anticipation of VibeGuard’s full proposed protocol | Probably lower than modern live families, but no FTO conclusion without official status | Medium; patent record/research lead |
| **US 7,346,461 B2 — System and method of analysing vibrations and identifying failure signatures** | 2005 filing reported; exact family priority not reverified | NASA / US Government | US | Granted; NTRS public record | IMF/Hilbert-Huang processing, stability spectrum, isolation of unstable vibration behaviour | Strong prior art for advanced vibration-signal analysis; technically more complex than frozen MVP | Current live-claim effect unresolved; important as prior art | High for technical disclosure; NASA NTRS |
| **US 11,429,900 B1 / BR 102022005021 A2 — Tractian** | 26 Oct 2021 | Tractian | US, BR | US aggregator indicates active; official status confirmation required | First-device FFT/modulus/peak selection, transmission, reconstruction and ML at second device, operator confirmation/retraining and scheduled sampling | Strong against broad fingerprinting, FFT peak compression, remote learning, and human-feedback propositions; Mahalanobis is a descriptive option | Relevant if copying claimed distributed sequence; not a basis for saying local Mahalanobis alone infringes | High for US claim text; medium for status |
| **US 11,334,414 B2 — Mitsubishi Heavy Industries** | 4 Mar 2019 | Mitsubishi Heavy Industries | US; Japanese priority identified | Granted; official current status not fully checked | Vibration amplitude and phase represented as complex values; Mahalanobis distance against past-measurement unit space; threshold abnormality | Very close to generic Mahalanobis vibration abnormality detection | Material FTO review item if VibeGuard uses comparable amplitude/phase complex features and thresholded unit-space claims | High for claim text; medium for status |
| **US 12,590,863 B2 / WO 2022/065103 and national members — Valqua** | 25 Sep 2020 | Valqua | US, WO, JP, CN and others surfaced | US grant published 31 Mar 2026; national statuses mixed/unverified | Frequency-band intensities, first Mahalanobis distance, gravity-centre features, second Mahalanobis distance, predicted abnormality period and maintenance actions | Strong against broad frequency-band Mahalanobis prognosis | Material if implementing the two-distance/gravity-centre/prediction sequence; less direct for simple local anomaly flag | High for US claim text; medium for status |
| **US 9,874,472 B2 / US 2012/0035885 / WO 2010/094915 — Rolls-Royce/OSyS** | 18 Feb 2009 | OSyS / Rolls-Royce | US, WO and related | US granted; official live status unresolved | Normal training across speed-frequency space, noise-floor modelling and detection of novel significant spectral content | Strong against generic speed-conditioned spectral fingerprints, adaptive noise floors and novelty indices | Material for future speed/load-normalised methods; exact claims need charting | High for disclosure; medium for current status |
| **US 9,091,588 B2 / US 2011/0290024 — Prognost-related vibration-signature monitoring** | 28 May 2010 | Reported industrial monitoring assignee | US lead | Granted; official current status unresolved | Spectral/signature comparison, background/interference handling and similarity-based diagnosis | Strong against generic subtraction/filtering plus signature comparison | Potentially relevant to any claimed source/noise-discrimination sequence | Medium |
| **US 9,835,594 B2 / WO 2014/064678 and national family — Augury** | 22 Oct 2012 | Augury Systems | US, WO, EP, IN, KR and others surfaced | Mixed family statuses; official national checks incomplete | Diagnosis from vibration/acoustic patterns and learned information across machines, commonly with remote/mobile processing | Strong against broad learned machine fingerprints and cross-machine diagnosis | Relevant where future system uses stored fault patterns or multi-machine training | Medium |
| **WO 2017/151447 / US 2019/0061086 — Infinite Uptime** | 2 Mar 2016 | Infinite Uptime | WO, US lead | Publication/application status requires official check | Add-on/magnetic machine-monitoring device with vibration/acoustic sensing and communications | Strong for commodity add-on sensor architecture; not shown to claim proposed contamination guard | More relevant to hardware enclosure/mounting/commercial node than to current firmware direction | Medium-low |
| **US 9,453,854 B2 / EP 2,913,643 / CA / AU — KCF vibration sensor** | 27 Feb 2014 | KCF Technologies | US, EP, CA, AU | US aggregator indicates active; maintenance events shown; official confirmation required | Specific vibration-sensor base, accelerometer and housing/circuit structure | Strong against treating a mounted wireless vibration sensor as new | Relevant if copying claimed mechanical sensor construction; not close to VibeGuard’s generic module-on-bracket MVP | High for family identity; medium for status |
| **US 9,271,170 B1 — KCF channel adaptation** | 1 May 2012 | KCF Technologies | US | Granted; current status unresolved | Radio/sensor-network channel adaptation | Peripheral; not a close vibration-anomaly claim | Relevant only if future product copies claimed network-channel behaviour | High for identity; low substantive relevance |
| **US 10,873,791 B1 — KCF compression method** | 29 Jul 2019 | KCF Technologies | US | Granted; current status unresolved | Compression for resource-constrained local-area networks | Shows that resource-aware data reduction can be claimed, but it is not a VibeGuard anomaly method | Relevant only if implementing the claimed network-compression sequence | High for identity; low substantive relevance |
| **US 2022/0067020 A1 / US 11,893,004 — Ford** | 26 Aug 2020 | Ford | US, DE, CN members surfaced | US grant indicated; official status check needed | Multidimensional vehicle-sensor anomaly detection using mean/covariance or inverse-covariance/Mahalanobis-like scoring | Strong generic prior art for multivariate statistical anomaly scoring; not a machine-vibration attribution claim | Indirect; relevant to broad statistical claims, not necessarily to the physical vibration protocol | Medium |
| **Senseye machine-monitoring lead** | Unresolved | Senseye-related lead | GB lead surfaced | Unresolved | General machine monitoring | Insufficient for a load-bearing conclusion | Must be completed before commercial FTO | Low |

---

## 6. Closest independent-claim analyses

### 6.1 Tractian US 11,429,900 B1

**Expressly claimed:** vibration acquisition at a first device; modified DFT/FFT frequency representation; modulus calculation; selected peaks; transmission to a second device; reconstruction; ML pattern identification; human alert and confirmation; updating training data; schedule determination; instructed sampling.

**VibeGuard overlap:** vibration sensor, FFT-domain processing, machine error/imbalance context, anomaly/fingerprint concepts.

**Material differences:** VibeGuard’s frozen architecture performs local analysis on an ESP32, does not require remote reconstruction, does not require selected-peak transmission, does not require operator-confirmed retraining, and does not use a remote schedule controller. Mahalanobis is not an independent-claim requirement in the reviewed claim 1.

**Conclusion:** highly relevant prior art and a commercial FTO review item, but not an exact claim read on the frozen MVP from the present evidence.

### 6.2 Mitsubishi US 11,334,414 B2

**Expressly claimed:** a vibration sensor on a rotating machine; acquisition of amplitude and phase; conversion to a complex measured value; Mahalanobis distance relative to a past-measurement unit space; abnormality when a threshold is exceeded.

**VibeGuard overlap:** rotating-machine vibration, normal-data unit space, Mahalanobis anomaly score, thresholded abnormality.

**Differences:** VibeGuard’s proposed feature vector may use RMS, peak, standard deviation, crest factor, kurtosis and selected spectral bands rather than amplitude/phase complex values. Its strongest future mechanism would include interference-state calibration, update quarantine, abstention and remount validity.

**Conclusion:** one of the closest claim sets to a naive Mahalanobis implementation. A future design should not assume that changing the MCU, sensor price, or running locally is a meaningful distinction.

### 6.3 Valqua US 12,590,863 B2

**Expressly claimed:** attached acceleration sensor; signal intensities for multiple frequency bands; first Mahalanobis distance relative to a unit space; gravity-centre data; second Mahalanobis distance; prediction of an abnormality-generation period and maintenance-response timing.

**VibeGuard overlap:** acceleration sensing, band features, Mahalanobis and normal unit space.

**Differences:** the frozen MVP does not use the dual Mahalanobis/gravity-centre/prognostic sequence and does not predict remaining life or maintenance date.

**Conclusion:** strong prior art against broad band-feature Mahalanobis claims; narrower FTO relevance if VibeGuard avoids that claimed prediction sequence.

### 6.4 Rolls-Royce US 9,874,472 B2 family

**Expressly disclosed/claimed theme:** vibration data indexed in speed-frequency regions; modelling the normal noise floor; distinguishing significant or novel spectral content; use of normal training data and speed information.

**VibeGuard overlap:** FFT, band-limited features, baseline/noise treatment, potential speed/load normalisation.

**Differences:** VibeGuard’s strongest proposed mechanism is source ambiguity management at one target-mounted node, including update quarantine and abstention—not simply novelty in a speed-frequency map.

**Conclusion:** major inventive-step reference for target fingerprints, speed-conditioned baselines, and spectral noise modelling.

### 6.5 US 7,421,349 B1

**Claim/disclosure theme:** phase-coupled bearing-fault signatures and expected fault-frequency relationships, designed to distinguish meaningful bearing signatures from coincidental spectral spacing.

**VibeGuard overlap:** vibration-based fault discrimination and frequency processing.

**Differences:** the frozen MVP is lower-frequency normal-versus-deliberate-imbalance classification, not high-frequency bearing diagnosis; it does not implement the phase-coupling detector.

**Conclusion:** strong prior art against broad bearing-fault claims, but not an exact anticipation of the proposed contamination-gated target-attribution sequence.

### 6.6 NASA US 7,346,461 B2

**Claim/disclosure theme:** Intrinsic Mode Functions, Hilbert-Huang analysis, spline-envelope derivative, stability spectrum and unstable-vibration isolation.

**VibeGuard overlap:** physical vibration measurement and failure-signature identification.

**Differences:** materially different signal-processing mechanism and compute burden.

**Conclusion:** landscape breadth evidence, not the closest claim to the frozen implementation.

---

## 7. Frozen-MVP closest-art feature chart

Status vocabulary is limited to **expressly disclosed**, **necessarily implied**, **arguably suggested**, **absent**, or **unresolved**. “Absent” in one reference does not imply inventive step.

| Frozen feature | Closest-art status | Audit conclusion |
|---|---|---|
| One accelerometer rigidly mounted on a machine | **Expressly disclosed** across multiple families | Conventional |
| ADXL345 specifically | **Absent** from closest reviewed claims | Commodity sensor choice; absence is not inventive |
| SPI acquisition | **Absent / unresolved** in closest claims | Routine interface choice |
| ESP32 local processing | **Absent** as a named MCU | Routine implementation platform |
| DC removal / mean subtraction | **Arguably suggested** by standard signal conditioning; claim-level presence unresolved | Ordinary DSP |
| Hann window | **Arguably suggested** by standard FFT practice; claim-level presence unresolved | Ordinary DSP |
| RMS, peak, standard deviation, crest factor, kurtosis | **Expressly disclosed or arguably suggested** in vibration literature/patent descriptions | Conventional features |
| Threshold plus persistence | Threshold **expressly disclosed**; persistence **arguably suggested** | Conventional alarm stabilisation |
| Triggered FFT | FFT **expressly disclosed**; conditional/triggered scheduling **arguably suggested** | Resource engineering, not established invention |
| Spectral subtraction | Baseline/noise subtraction and spectral comparison **expressly disclosed or arguably suggested** in adjacent vibration art | Generic subtraction is not novel |
| Band-limited features | **Expressly disclosed** | Conventional |
| Mahalanobis anomaly score | **Expressly disclosed and claimed** in Mitsubishi/Valqua families; described in Tractian | High prior-art density |
| Single-node operation | **Expressly disclosed** in multiple sensor-node contexts | Not inherently novel |
| Normal-baseline acquisition | **Expressly disclosed** | Conventional |
| Neighbouring-machine interference handling | Interference/noise handling **expressly disclosed or arguably suggested**; exact target attribution unresolved | Broad problem known |
| Confidence/abstention | Generic confidence is **arguably suggested**; explicit target-attribution abstention in closest claims **unresolved** | Possible component only when integrated and evidenced |
| Adaptive baseline update | **Arguably suggested / expressly disclosed** in learning and monitoring art | Standalone adaptation is weak |
| Contamination-protected update quarantine | **Unresolved** as the exact proposed sequence | Candidate differentiator, not yet proven |
| Mounting/remounting calibration | Placement importance **expressly known**; quantitative transfer/remount compensation **unresolved** | Candidate but evidence-heavy |
| Target-machine attribution under independently varying neighbour states | Fault/source differentiation broadly known; exact proposed protocol **unresolved** | Strongest technical problem, not solved by MVP |
| RGB alert | **Absent** from many claims but functionally ordinary | Non-inventive presentation |
| Eccentric-mass motor/fan test rig | Deliberate imbalance testing **arguably suggested** and conventional | Experimental apparatus, not invention by itself |
| Local/no-cloud operation | Local processing **expressly disclosed or suggested** in the field | Commercial/architectural advantage, not automatic novelty |
| ADXL345 bandwidth limit | **Absent** as a claim contribution | Scope constraint, not invention |
| RAM/flash/latency limits | Resource constraints **arguably suggested** | Must be measured; not automatically inventive |

---

## 8. Mandatory named-lead investigation

### 8.1 US 7,421,349

Retained as a high-relevance historical prior-art lead for frequency-domain bearing-fault discrimination. It does not establish that VibeGuard’s frozen low-frequency imbalance MVP is a bearing-fault detector, and the project must not make that claim with ADXL345 evidence.

### 8.2 US 7,346,461

NASA’s official NTRS record confirms the patent and its IMF/Hilbert-Huang/stability-spectrum mechanism. It establishes that sophisticated vibration failure-signature extraction predates VibeGuard. It is not an exact implementation match.

### 8.3 Tractian US 11,429,900 and family

The verified family in the reviewed record contains the US grant and a Brazilian publication. Assertions that US 12,423,604 and US 12,607,996 are family members were not independently substantiated and are excluded from this ledger.

The patent’s independent claim is narrower and more structured than several reports stated. Mahalanobis appears as a possible model in the description. This is prior-art evidence, not a direct infringement conclusion.

### 8.4 KCF US 9,271,170

The verified title is **Channel adaptation in sensor networks**. It is relevant to radio-channel behaviour, not a close claim on vibration anomaly detection.

### 8.5 KCF US 10,873,791

The verified title is **Compression method for resource constrained local area networks**. It may matter if a future product adopts the claimed compression/network sequence. It does not establish ownership of local Mahalanobis vibration classification.

### 8.6 US 2022/0067020

This is associated with Ford and multidimensional vehicle-sensor anomaly detection. It is relevant to generic covariance/Mahalanobis anomaly scoring but is not a VibeGuard-specific single-node machine-vibration attribution patent.

### 8.7 Named commercial actors

- **Tractian:** verified close family for remote fingerprint/error-condition detection.
- **Augury:** relevant learned machine-pattern/diagnosis family with multiple national members, including an Indian lead; live claims need official review.
- **KCF:** verified sensor-hardware and networking/compression families; no verified close KCF claim to VibeGuard’s proposed baseline-quarantine method.
- **Infinite Uptime:** relevant add-on sensor-node hardware lead; close firmware-claim overlap not established.
- **Senseye:** insufficiently verified; remains an explicit search gap.
- **Major industrial actors:** Mitsubishi, Valqua, Rolls-Royce and NASA/Navy art materially narrow broad algorithmic claims.

---

## 9. Non-patent prior art and standards

### 9.1 Engineering standards

ISO 10816/20816-type machine-vibration evaluation standards and industrial condition-monitoring guidance support the following engineering propositions:

- machine condition is commonly assessed using vibration magnitude, frequency content, operating state and trends;
- sensor placement and mechanical coupling materially affect measurements;
- machine class, speed/load and measurement location matter;
- a laboratory imbalance demonstration is not equivalent to industrial fault diagnosis.

Standards do not establish novelty or FTO. They are evidence that core vibration evaluation and operational normalisation are established practice.

### 9.2 Technical literature

The research lanes consistently surface extensive literature using:

- FFT and frequency bands;
- RMS, peak, crest factor, kurtosis and related features;
- one-class and multivariate anomaly detection;
- learned normal baselines;
- spectral/noise filtering;
- edge condition monitoring;
- bearing and rotating-machine classifiers.

That literature makes the frozen component-level pipeline conventional. The most important literature gap is not whether anomaly detection exists; it is whether an exact, experimentally bounded single-node method combines:

1. independent target/interferer calibration;
2. source-ambiguity estimation;
3. update quarantine;
4. abstention rather than forced labelling;
5. remount validity;
6. a measurable improvement under repeated interference and remounting.

This gap must be closed with a dedicated peer-reviewed literature search before a filing decision.

---

## 10. Current frozen-MVP patent assessment

### 10.1 What the MVP can prove

The MVP can credibly demonstrate:

- low-cost local acquisition from an ADXL345;
- reliable communication to an ESP32-class MCU;
- DC removal, Hann windowing, time features and triggered FFT;
- a calibrated threshold/persistence baseline;
- an initial Mahalanobis normal-space model;
- normal-versus-deliberately-imbalanced classification on a controlled motor/fan rig;
- RGB local output;
- compute, memory and latency feasibility.

### 10.2 What it cannot prove

The MVP does not by itself prove:

- high-frequency bearing-fault diagnosis;
- dense-machine target attribution;
- rejection of independently changing neighbour vibration;
- robustness to speed/load changes;
- transfer across machines;
- robustness after remounting;
- contamination-safe online learning;
- a non-obvious technical effect;
- novelty, patentability or FTO.

### 10.3 Patent conclusion on the frozen combination

The frozen combination should be treated as a **research platform**, not as the invention. Low cost, no cloud, one sensor, an ESP32, an ADXL345, FFT, Mahalanobis and a local LED do not create novelty merely by being combined. No credible Track A case is established.

---

## 11. Candidate invention-direction matrix

| Direction | Exact technical problem | Prospective contribution | Three-month status | Patent risk | Track / confidence | Kill condition |
|---|---|---|---|---|---|---|
| 1. Single-node target attribution under neighbour interference | Determine whether the mounted target, rather than a neighbour, is abnormal | Target/interferer-conditioned fingerprints, ambiguity detection and source-specific decision | Preliminary dual-rig work possible; decisive validation later | Novelty unresolved; obviousness high | **C / Medium** | Cannot beat best conventional baseline across neighbour states/remounts |
| 2. Known-state target fingerprint acquisition | Build a normal target model across operating states | Structured calibration using known target and neighbour states | Feasible | Calibration and speed-conditioned baselines are crowded | **D standalone; C when integrated / Medium** | Protocol adds no measurable robustness |
| 3. Contamination-protected baseline update | Prevent faults or neighbour changes from being learned as normal | Trusted baseline plus candidate/quarantine buffer; update only when target-normal confidence and source confidence pass | Implementable | Generic guarded adaptation is likely obvious; exact physical sequence unresolved | **B to prototype, C for patent evidence / Medium** | Same results as static or naive adaptive baseline |
| 4. Confidence-gated abstention | Avoid falsely assigning ambiguous vibration to target fault | Explicit Normal / Target abnormal / Unknown state tied to source ambiguity and update lockout | Implementable | Confidence thresholds are known; value depends on integration and evidence | **B to prototype, C integrated / Medium-low** | Abstention merely hides errors or coverage becomes unusably low |
| 5. Remounting compensation or validity check | Detect when coupling changes invalidate the model | Mount signature, validity score, forced recalibration or transfer correction | Basic validity check feasible; transfer correction later | Strong engineering value; novelty uncertain | **C / Medium-low** | Mount variation remains inseparable or rule is ordinary recalibration |
| 6. Resource-aware two-stage processing | Reduce compute/energy using cheap features before FFT | Trigger selected spectral analysis only when cheap features indicate need | Already largely in MVP | Triggered processing is routine | **D / High** | No measurable technical effect beyond expected resource saving |
| 7. Speed/load-normalised fingerprints | Avoid confusing operating-state change with fault | State-conditioned/order-related feature model | Bench version possible if speed reference available | Strong Rolls-Royce/order-tracking prior art | **C only if part of integrated attribution / Low-medium** | Improvement disappears against standard order/speed baselines |
| 8. Drift-aware adaptation | Maintain sensitivity over gradual normal drift | Slow/fast baseline layers with abnormal-data exclusion | Implementable | Large anomaly-detection literature | **D standalone; C integrated / Medium-low** | Existing methods reproduce result |
| 9. Deployment/calibration protocol for source labels | Create independent ground truth without a multi-sensor product architecture | Temporary reference instrumentation and randomized known-state calibration | Bench feasible; field later | A protocol alone may be routine; technical integration required | **C / Medium** | No source-specific model or reproducible effect emerges |
| 10. Mahalanobis plus ordinary DSP | Detect deviation from normal feature space | Standard feature vector and thresholded Mahalanobis score | Feasible | Directly crowded by patents and literature | **D / High** | Automatically rejected as standalone invention direction |

### 11.1 Rejected weak directions

The following should not be maintained as standalone patent stories:

- “edge AI vibration monitoring”;
- “low-cost/no-cloud monitoring”;
- ADXL345 plus ESP32;
- DC removal, Hann and ordinary FFT;
- common statistical features;
- Mahalanobis distance;
- ordinary static spectral subtraction;
- triggered FFT;
- RGB alerting;
- the eccentric-mass bench rig;
- generic baseline learning;
- generic confidence scores;
- generic sensor remount recalibration.

---

## 12. Strongest surviving direction

### 12.1 Working technical definition

**Confidential working title:** *Confidence-Gated Contamination-Resistant Target-Fingerprint Maintenance for a Single Mounted Vibration Node.*

The prospective mechanism is a coordinated sequence, not a list of algorithms:

1. **Known-state commissioning.** Record the target in known normal states while independently controlling or labelling the interferer as off, normal and abnormal, with permitted speed/load ranges recorded.
2. **Target-conditioned fingerprint.** Build a target model from band-limited/time-domain features tied to the permitted target operating state.
3. **Interference/validity estimate.** Determine whether the current observation is consistent with a valid target measurement or is dominated by neighbour change, mounting change, or an unmodelled regime.
4. **Three-way decision.** Output Normal, Target abnormal, or Unknown/Interfered rather than forcing every sample into a binary label.
5. **Baseline quarantine.** New observations enter a candidate buffer, not the trusted normal baseline.
6. **Guarded promotion.** Promote candidate data to the trusted baseline only after target-normal evidence, acceptable source confidence, persistence, and mounting validity are satisfied.
7. **Fault/update separation.** Suspected target faults, ambiguous source states and neighbour-state transitions cannot update the normal model.
8. **Remount rule.** A changed mounting signature invalidates the baseline or invokes a separately validated transfer/recalibration procedure.
9. **Resource-constrained implementation.** Execute the mechanism locally using a small feature vector, selected FFT bands and measured compute/memory limits.

### 12.2 Why this is stronger than “adaptive spectral subtraction”

“Adaptive spectral subtraction” alone is too broad and too close to established noise estimation, background subtraction and adaptive filtering. The potentially differentiating idea is the **decision-and-update coupling**:

- source ambiguity controls whether the system labels a fault;
- the same ambiguity controls whether data may alter the normal model;
- mounting validity controls both inference and learning;
- independently known target/interferer states provide testable physical ground truth.

### 12.3 Closest art and remaining distinction

The mechanism sits near:

- Rolls-Royce speed/frequency normal training and noise-floor novelty;
- Mitsubishi and Valqua Mahalanobis unit spaces;
- Tractian machine fingerprints and iterative learning;
- generic drift-aware anomaly detection;
- established vibration sensor placement/mounting practice.

The apparent distinction is the exact integrated sequence under a **single target-mounted node**, especially the quarantine/promotion rule and explicit abstention tied to source ambiguity and remount validity. That distinction is presently an **unverified hypothesis**.

### 12.4 Required technical effect

The method must demonstrate, relative to the strongest conventional baseline:

- fewer false target-fault labels when the neighbour changes;
- no material increase in missed target faults;
- reduced contamination of the normal baseline;
- repeatable performance after controlled remounting;
- acceptable decision coverage despite abstention;
- execution within the measured ESP32 resource envelope.

### 12.5 Classification

- **Track:** C
- **Novelty risk:** Medium-high
- **Inventive-step risk:** High
- **Eligibility risk:** Medium unless tightly tied to physical measurement and technical effect
- **FTO risk:** Medium and unresolved
- **Three-month deliverability:** Prototype and initial dual-rig evidence only
- **Later work:** field-like and field validation, complete prior-art search and counsel review
- **Confidence:** Medium

---

## 13. Bench demonstration versus field-attribution evidence

### Level 1 — Semester bench demonstration

**Setup:** one target motor/fan, rigid sensor mount, normal state and controlled eccentric-mass/looseness state.

**Can establish:** reliable acquisition, normal/abnormal separation, classifier implementation, repeatability on that rig, resource feasibility.

**Cannot establish:** source attribution when a neighbour changes; robustness to independent speed/load variation; remount transfer; field false alarms; patent-oriented technical effect.

### Level 2A — Controlled interference bench

**Setup:** target and interferer motors mechanically coupled through a common base or structure, independently controlled and independently labelled.

**Required state combinations:**

- target normal / abnormal;
- interferer off / normal / abnormal;
- target speed/load regimes;
- interferer speed/load regimes;
- at least three remounting conditions;
- repeated sessions on different days.

**Can establish:** preliminary attribution error, effect of neighbour states, update contamination, abstention behaviour and remount sensitivity.

**Still cannot fully establish:** dense industrial transfer and commercial reliability.

### Level 2B — Field-like or real-site validation

**Setup:** target-mounted node in an environment with independently varying neighbouring equipment and reference ground truth.

**Required:** independent target/interferer labels, operator/reference instrumentation, repeated operating regimes, remounting, held-out days, locked parameters and comparison against conventional methods.

Only this level can support a serious target-attribution patent narrative.

---

## 14. Novelty analysis

### 14.1 Frozen MVP

Strict novelty asks whether one prior-art item discloses every required element of a proposed claim. The project has no final claim, so a definitive novelty determination is impossible.

The audit nevertheless finds:

- virtually every important functional element is expressly disclosed or conventional;
- several close families disclose overlapping combinations of sensor acquisition, FFT/spectral features, normal baselines, thresholding, Mahalanobis scoring, machine fingerprints and alerts;
- implementation details such as ADXL345, ESP32, Hann window, RGB LED and a cheap rig would ordinarily be viewed as routine choices unless functionally tied to an unexpected effect.

**Conclusion:** novelty is **not established** for the frozen MVP, and it should not be presented as the invention.

### 14.2 Strongest integrated direction

No verified single item was shown to disclose the exact complete sequence of known-state target/interferer commissioning, source-confidence estimation, three-way abstention, quarantined baseline promotion, fault/update separation and remount validity on one constrained node.

**Conclusion:** exact anticipation was **not established**, but novelty remains unresolved. A deeper claim-directed search may find the sequence in patents or literature, and the current absence is not positive proof.

---

## 15. Inventive-step / obviousness analysis

### 15.1 Frozen MVP

Obviousness risk is **very high**. A skilled vibration-monitoring engineer would know:

- mount an accelerometer;
- condition and window the signal;
- calculate common features;
- perform FFT/band analysis;
- compare against a normal baseline;
- apply thresholds or a one-class statistical distance;
- trigger an alert;
- use an embedded MCU for low-cost local operation.

The combination presently behaves as the expected aggregation of known measures.

### 15.2 Standalone extensions

The following are also likely obvious alone:

- changing a static baseline to an adaptive baseline;
- refusing updates when anomaly score is high;
- adding a confidence band;
- recalibrating after remounting;
- triggering FFT to save resources;
- conditioning features on speed/load;
- subtracting a recorded background spectrum.

### 15.3 Integrated direction

The integrated mechanism has a possible inventive-step path only if the team can show that the particular interaction among source-confidence, abstention, update quarantine and mounting validity solves a physical measurement problem in a non-routine way.

Evidence that would help:

- conventional methods fail specifically because neighbour changes enter the target model;
- the proposed promotion rule prevents that failure;
- an ablation shows each claimed element contributes;
- improvement repeats across mounts, days and target/interferer regimes;
- the effect is not obtained by a routine fixed threshold, static subtraction, ordinary Mahalanobis, or generic drift detector.

Even with such evidence, obviousness risk remains high because the sub-elements are individually familiar.

---

## 16. Patent-eligibility analysis

Eligibility is separate from novelty and inventive step.

### United States

A claim merely reciting mathematical scoring, FFT, covariance or Mahalanobis on generic data risks treatment as an abstract idea. The stronger framing is a practical machine-measurement method:

- acquire vibration from a specified physical target;
- determine source/mount validity;
- control whether an observation changes the trusted physical baseline;
- abstain from a target-fault output under defined physical ambiguity;
- produce a demonstrable improvement in target-fault attribution or false-alarm behaviour.

The specification would need to explain the technological improvement, not merely assert “AI” or “edge processing.”

### Europe

An abstract FFT or mathematical method is excluded as such, but a mathematical method may contribute when functionally tied to a specific technical purpose. Deriving or predicting the physical state of a real machine from physical measurements is capable of technical contribution. The claim must remain limited to the specific physical measurement purpose and technical effect.

### India

The current CRI framework requires identification of the technical problem, essential technical features, technical solution and technical effect. Novel hardware is not necessarily required, but a computer-program-per-se or purely mathematical presentation remains vulnerable. Real-time sensor-based monitoring of physical devices can support technical character when the contribution extends beyond incidental computer use.

### Eligibility conclusion

The strongest direction has a plausible eligibility framing in all three regions, but eligibility will not rescue an obvious or unsupported method. The decisive evidence is a specific physical diagnostic effect and a claim that is functionally limited to it.

---

## 17. FTO risk analysis

### 17.1 Frozen educational prototype

The present academic prototype does not justify an infringement conclusion. Patent rights are jurisdictional and claim-specific; the record lacks a complete official-status and live-claim chart. Educational use should not be described as automatically exempt.

### 17.2 Material commercial risk areas

1. **Mahalanobis vibration diagnosis:** Mitsubishi and Valqua claims require close review.
2. **Speed/frequency novelty and noise floors:** Rolls-Royce family may affect future state-conditioned fingerprints.
3. **Remote compression/reconstruction/learning:** Tractian is relevant if the architecture evolves away from local-only operation.
4. **Learned machine-pattern diagnosis:** Augury-related families require national claim review.
5. **Sensor housing and mount structure:** KCF and other hardware families matter if the team designs a commercial enclosure.
6. **Interference/signature handling:** Prognost-like art may affect broad source-discrimination claims.
7. **Networking/compression:** KCF’s channel/compression patents are relevant only if those sequences are adopted.

### 17.3 Design-around observations—not legal conclusions

The current local-only design appears factually different from Tractian’s reviewed remote reconstruction/feedback claim. A future design should also avoid casually reproducing:

- Mitsubishi’s exact amplitude/phase complex-value Mahalanobis sequence;
- Valqua’s dual-distance gravity-centre prognosis;
- Rolls-Royce’s claimed speed-frequency noise-floor sequence;
- proprietary sensor-housing structures;
- remote peak-compression and operator-confirmed retraining sequences.

A contamination-quarantine and abstention mechanism may provide a different focus, but no safe design-around is established.

### 17.4 Required FTO next step

Before productisation:

- freeze the actual implementation;
- identify target jurisdictions;
- retrieve official live claims and prosecution histories;
- chart every implemented element;
- review equivalents and dependent claims;
- obtain counsel’s written FTO analysis.

---

## 18. Claim-to-experiment map

The values below are **research recommendations requiring owner approval**, not frozen project requirements.

### 18.1 Prospective element map

| Prospective element | Baseline comparator | Proposed system | Independent variable | Required evidence | Failure evidence |
|---|---|---|---|---|---|
| Known-state target/interferer commissioning | Target-only normal baseline | Calibration across target and interferer states | Interferer state and speed/load | Lower attribution error on held-out state combinations | No gain over target-only baseline |
| Source-confidence estimate | Binary Mahalanobis output | Valid/ambiguous source score | Mechanical coupling and neighbour amplitude | Confidence correlates with actual attribution correctness | Poor calibration or no relation to correctness |
| Three-way abstention | Forced Normal/Abnormal | Normal/Target abnormal/Unknown | Ambiguity level | Fewer wrong target labels at reported coverage | Error merely replaced by excessive abstention |
| Baseline quarantine | Naive moving update | Candidate buffer plus guarded promotion | Fault and neighbour drift episodes | Lower baseline drift and preserved fault sensitivity | Same or worse misses/false alarms |
| Remount validity | Reuse old model blindly | Mount check and forced recalibration/transfer | Mount torque/location/session | Repeatable performance after remount or reliable invalidation | Mount effect overlaps fault and cannot be detected |
| Resource-constrained execution | Continuous full FFT | Cheap feature gate plus selected spectral analysis | Trigger rate and window size | Lower measured compute/energy without diagnostic loss | Expected saving only or degraded attribution |

### 18.2 Recommended controlled protocol

**Rig:** two independently driven motors on a shared dense base, one designated target and one interferer; one product sensor remains mounted on the target. Temporary reference sensors or tachometers may be used for ground truth and are not part of the final product architecture.

**Minimum condition design:**

- target: normal and eccentric-mass abnormal;
- interferer: off, normal and abnormal;
- at least two target operating regimes;
- at least two interferer regimes where practical;
- at least three sensor remounts;
- at least five independent sessions/days.

A practical starting design is 12 principal target/interferer state cells, repeated across three remounts and five sessions. Windows from one continuous run must not be misrepresented as independent trials.

**Locked evaluation:**

- use early sessions for calibration/development;
- freeze parameters before held-out evaluation;
- hold out at least one remount and one day/session;
- report both window-level and session-level results;
- retain raw data and immutable experiment metadata.

### 18.3 Mandatory baselines

Compare against:

1. RMS threshold plus persistence;
2. ordinary FFT/band features;
3. ordinary Mahalanobis normal-space classifier;
4. static baseline spectral subtraction;
5. naive adaptive baseline;
6. the complete proposed mechanism.

### 18.4 Required ablations

Remove individually:

- source-confidence gate;
- abstention;
- quarantine buffer;
- mounting-validity rule;
- operating-state conditioning;
- selected spectral subtraction/band rule.

### 18.5 Metrics

- sensitivity and missed-detection rate;
- specificity;
- balanced accuracy;
- false target-fault alerts per hour/session;
- target-attribution error;
- neighbour-to-target confusion;
- abstention rate and coverage;
- confidence calibration;
- detection delay;
- baseline drift;
- remount repeatability;
- compute time;
- RAM and flash use;
- sample loss;
- sample rate and usable bandwidth;
- energy/power where material.

### 18.6 Proposed success threshold

For the primary controlled-interference endpoint, pre-register one of the following before locked testing:

- at least **30% relative reduction** in attribution error or false target-fault alerts versus the strongest conventional baseline, with no more than a **5 percentage-point** worsening in missed target faults; or
- another statistically and operationally justified threshold approved by the owner and institutional reviewer.

Additionally:

- the direction must improve results across at least three remounts;
- the primary difference should have an uncertainty interval that excludes no improvement, using an analysis appropriate to independent sessions;
- abstention coverage must be reported and cannot be tuned after seeing the test data;
- success on isolated target-only data does not count as attribution success.

---

## 19. Three-month semester plan

### Weeks 1–2 — Frozen MVP hardware and data integrity

- build the single target motor/fan rig;
- create a rigid repeatable bracket;
- verify ADXL345 sample rate, usable bandwidth and SPI integrity;
- implement timestamped logging and dropped-sample detection;
- define a repeatable eccentric-mass fixture;
- confirm normal and abnormal conditions are mechanically stable.

**Gate:** no classifier work is accepted until acquisition and labels are repeatable.

### Weeks 3–4 — Conventional baselines

- implement DC removal, Hann window, time features and triggered FFT;
- implement RMS threshold plus persistence;
- implement ordinary band features and Mahalanobis;
- lock a Level 1 test protocol;
- measure RAM, flash, compute time and latency.

**Gate:** demonstrate controlled normal/abnormal separation without claiming attribution or patent value.

### Weeks 5–6 — Controlled interference rig

- add independently controlled interferer;
- record randomized state combinations;
- add reference speed/state logging;
- test static spectral subtraction and band selection;
- quantify neighbour-to-target confusion.

**Gate:** determine whether the single node contains usable target-specific information.

### Weeks 7–8 — Bounded enhancement prototype

- add Normal / Target abnormal / Unknown;
- add candidate/quarantine baseline buffer;
- implement guarded promotion;
- add mount-validity or forced-recalibration logic;
- preserve conventional baselines for comparison.

### Weeks 9–10 — Locked experiments and ablation

- freeze parameters;
- run held-out sessions and remounts;
- perform ablations;
- report attribution error, false alarms, misses, abstention and resource use;
- document failures, not only best cases.

### Weeks 11–12 — Evidence and IPR gate

- determine whether the integrated method survives kill criteria;
- prepare an invention disclosure only if a specific mechanism and reproducible effect exist;
- segregate public conventional material from confidential rules/results;
- obtain institutional IPR review before repository, poster, paper or public demonstration of the potentially novel method.

**Three-month outcome:** a strong semester MVP plus preliminary evidence. A patent filing should not be assumed.

---

## 20. Later-semester or publication extension

A serious Track C extension requires:

- access to a field-like or real dense-machine environment;
- independently known target and interferer states;
- repeated days and operating regimes;
- controlled remounting;
- locked external validation;
- reference instrumentation;
- a complete literature and patent update;
- a counsel-reviewed invention disclosure.

### Expected duration

Approximately one additional semester is a reasonable planning assumption, but the actual duration depends on site access, permission, machine-state labels and dataset quality.

### Expected cost

Additional cost is unresolved. It may include:

- stronger mounts and replacement sensors;
- reference accelerometer or tachometer;
- data-logging hardware;
- travel/site access;
- safety controls;
- possible IIS3DWB or industrial sensor only if the research scope moves to higher-frequency phenomena.

The IIS3DWB is not required merely to study low-frequency source attribution.

### Publication opportunity

Even a negative result can support a useful publication if the experiment is rigorous:

- a labelled single-node target/interferer dataset;
- comparison of static and guarded baselines;
- remount sensitivity;
- abstention calibration;
- limits of low-cost single-node attribution.

Patent review must occur before public disclosure of a surviving mechanism.

---

## 21. Budget, compute, and team feasibility

### 21.1 Budget

The repository-supported ADXL345 MVP estimate is approximately **₹1,700–₹2,200**. A second motor, reference speed sensor, stronger mounting, replacements and test materials may move the controlled-interference programme toward **₹3,000–₹5,000**. Prices require a procurement refresh.

The frozen semester MVP is therefore feasible within the stated ceiling. A field extension is not budgeted reliably in the current record.

### 21.2 Sensor and bandwidth

The ADXL345 is retained for the lower-frequency imbalance, looseness and misalignment demonstration. The project must verify that discriminating energy lies inside the measured usable band. It must not claim high-frequency industrial bearing diagnosis from the current MVP.

### 21.3 Compute

An ESP32-class MCU can reasonably support:

- three-axis acquisition;
- common time-domain features;
- 256–1,024-point FFTs;
- small covariance matrices and Mahalanobis scoring;
- simple confidence, quarantine and state-machine logic.

The project must measure actual:

- window processing time;
- sampling jitter and dropped samples;
- RAM/flash use;
- covariance stability;
- latency;
- power if later claimed as an advantage.

Large neural networks, blind source separation and continuous high-rate multichannel processing are outside the frozen resource profile.

### 21.4 Team

The five-member structure is suitable if work is separated:

1. acquisition and embedded DSP;
2. anomaly logic and data analysis;
3. rig, mounting and reference instrumentation;
4. logging, RGB/state machine and beginner-safe tasks;
5. experiment control, documentation and presentation.

The main risk is not coding capacity. It is experimental discipline and access to independently labelled interference conditions.

---

## 22. Kill criteria

The patent-development direction is killed or downgraded if any of the following occurs:

1. ordinary RMS, FFT/band features or Mahalanobis perform as well as the proposed mechanism under controlled interference;
2. neighbour-state changes cannot be distinguished from target abnormality beyond mounting/session variability;
3. guarded updating does not reduce baseline contamination;
4. abstention lowers apparent error only by refusing an impractical proportion of observations;
5. performance does not repeat across remounts and sessions;
6. the mechanism requires a second permanent product sensor, cloud inference or a fundamentally different architecture without being explicitly reclassified as a major redesign;
7. a closer patent or publication discloses the full proposed sequence;
8. the effect disappears after parameters are frozen or on held-out data;
9. the method exceeds the ESP32 resource or latency envelope without a demonstrated technical reason;
10. no independently labelled field-like validation can be obtained;
11. the team cannot define the prospective contribution more specifically than “adaptive spectral subtraction,” “edge AI,” or “Mahalanobis anomaly detection”;
12. institutional IPR review concludes that the remaining distinction is not worth filing.

If killed, VibeGuard remains a strong semester demonstration and possible publication project.

---

## 23. Confidentiality boundary

### Already public or conventional

The following may generally be discussed as the baseline engineering project, subject to college policy:

- ADXL345 and ESP32 architecture;
- SPI acquisition;
- DC removal and Hann window;
- ordinary time features;
- triggered FFT;
- RMS threshold/persistence;
- ordinary Mahalanobis scoring;
- generic spectral subtraction;
- RGB state output;
- eccentric-mass bench rig.

### Potentially confidential project material

Until institutional IPR review:

- exact known-state calibration sequence;
- target/interferer fingerprint construction;
- source-confidence calculation;
- quarantine and promotion rules;
- abstention thresholds and state logic;
- remount validity or transfer method;
- ablation results;
- labelled interference/remount datasets;
- field results;
- any parameter combination that produces a reproducible unexpected technical effect.

Do not publish a potentially surviving method in a repository, poster, video, paper, competition submission or public demonstration before the IPR gate.

---

## 24. Final VibeGuard recommendation

### Required recommendation

**Retain as strong semester prototype but reduce patent priority.**

Proceed with the frozen MVP because it is feasible, demonstrable, budget-compatible and well matched to the team. Add a controlled dual-motor interference experiment and a first guarded-baseline/abstention prototype only as a bounded research enhancement.

Do not represent the frozen architecture as the invention. Do not file based solely on ADXL345 + ESP32 + FFT + Mahalanobis + spectral subtraction. Re-evaluate patent development only if:

- the integrated mechanism is precisely defined;
- it beats strong conventional baselines under independently labelled interference;
- results survive remounting and held-out sessions;
- the closest patent and literature search remains clear enough;
- institutional IPR review supports filing before disclosure.

This recommendation is limited to VibeGuard and does not select the final Project mC winner.

---

## 25. Unresolved questions

1. Does the target-mounted sensor retain enough target-specific information when the interferer changes independently?
2. What exact physical observable will estimate source ambiguity without a second permanent product sensor?
3. What candidate-buffer promotion rule is specific enough to test and potentially claim?
4. Can the system distinguish slow target degradation from normal drift without learning the fault as normal?
5. Can a remount-validity test reliably detect transfer-function change?
6. Does the proposed mechanism improve the strongest conventional baseline after parameters are frozen?
7. What abstention coverage is operationally acceptable?
8. Does the effect replicate across more than one target motor or machine class?
9. What official live claims exist in India, China, Europe and the US for the closest Mitsubishi, Valqua, Rolls-Royce, Tractian, Augury, Prognost, KCF, Infinite Uptime and Senseye families?
10. Is there peer-reviewed prior art specifically combining baseline quarantine, source ambiguity, abstention and remount validity?
11. What field partner can provide independently labelled target/interferer states?
12. What should the owner approve as the pre-registered primary threshold?
13. Does the team intend only an academic prototype, an Indian filing, or multi-jurisdiction commercialisation?
14. Can an invention disclosure be completed before any public presentation of the enhancement?

---

## 26. Source and verification log

### 26.1 Project sources

- **P-00:** `00_READ_FIRST_VibeGuard_Synthesis_Instructions.md` — governing instruction.
- **P-01:** `01_Engineering_Design_Review.md` — authoritative engineering identity and hypothesis.
- **P-02:** `02_Project_mC_Decision_Register_v1.2.md` — accepted decisions and constraints.
- **P-03:** `03_Phase3C_Portfolio_Closure_Memo_Approved.md`.
- **P-04:** `04_Phase3C_VibeGuard_Architecture_Report_Final.md`.
- **P-05:** `05_Phase3C_VibeGuard_Memory_Final.md`.
- **P-06:** `06_Phase3C_VibeGuard_SOP_Final.md`.
- **P-07:** `07_Concept_Evidence_Matrix.md`.
- **P-08:** `08_Uncertainty_and_Test_Register.md`.
- **P-09:** `09_Patent_Research_Input_Pack.md`.
- **P-10:** `10_Phase2_Report_by_Claude.md` — historical leads only.
- **P-99:** `99_INPUT_MANIFEST.md` — file control only.

### 26.2 Independent research lanes

- **R-11:** ChatGPT Deep Research selected final.
- **R-12:** Gemini.
- **R-13:** Perplexity.
- **R-14:** Qwen.
- **R-15:** Mistral partial fragmented compilation; one lane; no verdict.
- **R-16:** Microsoft Copilot.

### 26.3 Primary/near-primary patent and official records checked

- US 11,429,900 B1 and BR 102022005021 A2 — Tractian.
- US 11,334,414 B2 — Mitsubishi Heavy Industries.
- US 12,590,863 B2 and WO 2022/065103 family — Valqua.
- US 2012/0035885 A1 / US 9,874,472 B2 family — Rolls-Royce/OSyS.
- US 7,346,461 — NASA NTRS official record.
- US 7,421,349 — US Navy lead.
- US 9,453,854 B2 family — KCF vibration sensor.
- US 9,271,170 B1 — KCF channel adaptation.
- US 10,873,791 B1 — KCF compression.
- US 2022/0067020 / US 11,893,004 — Ford anomaly-detection family.
- selected Augury, Infinite Uptime, Prognost and Senseye leads from the audited reports.

### 26.4 Eligibility sources

- EPO Guidelines for Examination 2026, mathematical methods and mixed technical/non-technical claims.
- USPTO MPEP § 2106 and 2025 subject-matter-eligibility update.
- Indian Patent Office, Guidelines for Examination of Computer Related Inventions (CRIs) 2025, published 29 April 2026.

### 26.5 Search themes

Queries and classification-led searching covered combinations of:

- machine vibration, rotating machine, bearing condition;
- single sensor, single node, source attribution;
- neighbour/interference/crosstalk/noise;
- target fingerprint, baseline, unit space;
- Mahalanobis distance, covariance, one-class anomaly;
- FFT, spectral novelty, spectral subtraction, frequency bands;
- adaptive baseline, contamination, drift;
- confidence, abstention, unknown state;
- mounting, remounting, transfer function;
- speed/load normalisation and order tracking;
- edge/local processing and constrained hardware;
- named assignees and mandatory publication numbers.

### 26.6 Verification rule

Where an official national register was not successfully checked, current legal status remains unresolved even if an aggregator labels a patent “active,” “granted,” “expired,” “abandoned,” or “pending.” Prior-art relevance and FTO relevance have been kept separate throughout.

---

# End of report
