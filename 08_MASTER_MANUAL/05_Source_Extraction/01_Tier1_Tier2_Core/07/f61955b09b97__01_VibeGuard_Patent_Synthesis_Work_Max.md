# Source Extraction

- Chapter: `07` — VibeGuard Patent Evidence and Future Research Path
- Authority tier: `TIER_2`
- Manual treatment: `CORE_DECISION_EVIDENCE`
- Original source: `03_CONCEPT_PORTFOLIO/VibeGuard/03_Patent_Synthesis/01_VibeGuard_Patent_Synthesis_Work_Max.md`
- Current SHA-256: `f61955b09b976a4c445fcdddbc40aada02cae204302876dbfc7cf1825b8cdf72`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

# VibeGuard Current Patent Evidence Synthesis

**Evidence date:** 1 August 2026
**Scope:** VibeGuard only. This report does not compare VibeGuard with any other Project mC concept, does not select a Project mC winner, and is not a legal opinion.

## 1. Executive verdict

**credible long-term path requiring later-semester extension**

- **Track:** C — the semester MVP is buildable within the owner-approved three-month and ₹5,000 ceilings, but the only technically coherent patent-development bridge requires later field research.
- **Confidence:** Medium-low. The negative conclusion on the frozen MVP is high-confidence; survival of the later direction is only low-to-medium confidence because no Level-2 target-attribution data, complete jurisdictional status review, or professional claim/FTO opinion exists.
- **Most important limitation:** VibeGuard has no evidence that one accelerometer can distinguish a target-machine fault from neighbouring-machine interference across independently known target/interferer states, speed and load changes, remounts, and realistic coupling. An isolated imbalance demonstration is not that evidence.
- **Frozen MVP as the invention:** **No.** Its sensor, preprocessing, time features, triggered FFT, band features, baseline subtraction, threshold/persistence logic, optional Mahalanobis score, local alert, and test rig are conventional individually and form a predictable monitoring aggregation.

The only surviving research hypothesis is a **label-aware, contamination-protected, confidence-gated single-node target-attribution mechanism**. It would acquire target and interferer fingerprints under independently known operating states, separately score target abnormality and attribution ambiguity, abstain rather than mislabel ambiguous interference, and update a baseline only when normality and admissible interference are independently established. That mechanism is not in the frozen MVP, is not yet shown novel or non-obvious, and cannot be treated as an invention unless it produces a reproducible technical effect over simpler baselines in Level-2 trials.

## 2. Input inventory

The complete logical input set is present and readable. Parenthetical suffixes in uploaded names are transport disambiguators; the content hashes match the canonical entries in `99_INPUT_MANIFEST.md`. The manifest was used only for file control, never as technical evidence. Hidden transport artifacts were not treated as inputs.

The actual attached basenames were: `00_READ_FIRST_VibeGuard_Synthesis_Instructions(3).md`; `01_Engineering_Design_Review(8).md`; `02_Project_mC_Decision_Register_v1.2(9).md`; `03_Phase3C_Portfolio_Closure_Memo_Approved(8).md`; `04_Phase3C_VibeGuard_Architecture_Report_Final(2).md`; `05_Phase3C_VibeGuard_Memory_Final(4).md`; `06_Phase3C_VibeGuard_SOP_Final(2).md`; `07_Concept_Evidence_Matrix(8).md`; `08_Uncertainty_and_Test_Register(8).md`; `09_Patent_Research_Input_Pack(9).md`; `10_Phase2_Report_by_Claude(9).md`; `11_VibeGuard_Patent_Research_ChatGPT_DR(3).md`; `12_VibeGuard_Patent_Research_Gemini(2).docx`; `13_VibeGuard_Patent_Research_Perplexity(2).md`; `14_VibeGuard_Patent_Research_Qwen(2).md`; `15_VibeGuard_Patent_Research_Mistral_PARTIAL_COMPILATION(3).md`; `16_VibeGuard_Patent_Research_Microsoft_Copilot(2).docx`; and `99_INPUT_MANIFEST(6).md`.

| No. | Controlled input | Role | Readability / integrity result |
|---:|---|---|---|
| 00 | `00_READ_FIRST_VibeGuard_Synthesis_Instructions.md` | Governing specification | Readable; SHA-256 `49d7d80c…414db`; governing authority applied |
| 01 | `01_Engineering_Design_Review.md` | Canonical project authority 1 | Readable; hash matched manifest |
| 02 | `02_Project_mC_Decision_Register_v1.2.md` | Canonical project authority 2 | Readable; v1.2 confirmed; hash matched |
| 03 | `03_Phase3C_Portfolio_Closure_Memo_Approved.md` | Canonical project authority 3 | Readable; approved version confirmed |
| 04 | `04_Phase3C_VibeGuard_Architecture_Report_Final.md` | Canonical project authority 4 | Readable; final version confirmed |
| 05 | `05_Phase3C_VibeGuard_Memory_Final.md` | Canonical project authority 5 | Readable; final version confirmed |
| 06 | `06_Phase3C_VibeGuard_SOP_Final.md` | Canonical project authority 6 | Readable; final version confirmed |
| 07 | `07_Concept_Evidence_Matrix.md` | Validated evidence file | Readable; hash matched |
| 08 | `08_Uncertainty_and_Test_Register.md` | Validated evidence file | Readable; hash matched |
| 09 | `09_Patent_Research_Input_Pack.md` | Validated patent-research input | Readable; hash matched |
| 10 | `10_Phase2_Report_by_Claude.md` | Historical leads only | Readable; hash matched; no current conclusion adopted |
| 11 | `11_VibeGuard_Patent_Research_ChatGPT_DR.md` | Independent research lane 1 | Readable; complete report |
| 12 | `12_VibeGuard_Patent_Research_Gemini.docx` | Independent research lane 2 | DOCX ZIP valid; extracted and all 24 rendered pages inspected |
| 13 | `13_VibeGuard_Patent_Research_Perplexity.md` | Independent research lane 3 | Readable; main report plus export/reference payload distinguished |
| 14 | `14_VibeGuard_Patent_Research_Qwen.md` | Independent research lane 4 | Readable; complete as transported |
| 15 | `15_VibeGuard_Patent_Research_Mistral_PARTIAL_COMPILATION.md` | Independent research lane 5 | Readable transport compilation of three incomplete fragments; **one partial lane, no final verdict** |
| 16 | `16_VibeGuard_Patent_Research_Microsoft_Copilot.docx` | Independent research lane 6 | DOCX ZIP valid; text/tables readable; all 17 pages inspected despite poor rendered contrast |
| 99 | `99_INPUT_MANIFEST.md` | File control only | Readable; logical count 18 confirmed; self-hash not treated as a control requirement |

All 17 externally hashable controlled files matched the manifest; the manifest itself had SHA-256 `b8034e85…bb56a`. Thus the governing instruction, ten canonical project documents, six independent research lanes, and file-control manifest are present. The substantive audit was permitted to proceed.

### Applied project authority order

1. Engineering Design Review.
2. Decision Register v1.2.
3. Approved Phase 3C closure memo.
4. Final VibeGuard architecture report.
5. Final VibeGuard memory.
6. Final VibeGuard SOP.
7. Validated evidence files 07–09.
8. Phase 2 report only as historical search leads.
9. Research lanes 11–16 only after source and claim audit.

Owner overrides control: up to three months; preferred spend no more than ₹3,000 and absolute ceiling ₹5,000; team of five comprising three strong CS/cyber contributors, one learner, and one presenter/support member.

## 3. Research-report reliability audit

The six lanes are evidence sources, not votes. Agreement does not cure a bad citation, an abstract-only reading, a family error, or a legal-status error.

| Lane | Useful contribution | Material defects found | Evidentiary treatment |
|---|---|---|---|
| ChatGPT Deep Research | Broadest reproducible family list; correctly separates frozen MVP from target attribution; useful Track-C mechanism and claim-to-test framing | Some status conclusions rely on Google family navigation; official-source granularity is uneven; India CRI publication-date metadata was not reconciled; several later portfolios were not claim-charted | **Medium reliability.** Leads and claim readings retained after independent verification; legal/status conclusions remain provisional |
| Gemini | Good project fidelity, bench/field distinction, and guarded-baseline experiment concept | Weak family ledger; optimistic novelty, eligibility and FTO conclusions; “edge-only” cannot guarantee non-infringement; a numerical false-alarm threshold was invented; official searches were not reproducibly documented | **Medium-low.** Technical experiment ideas retained; legal confidence and numerical criterion rejected |
| Perplexity | Located Mitsubishi, Valqua, and Rolls-Royce families; candid about several gaps | Did not independently search non-patent literature; incomplete mandatory actor/lead coverage; no robust India/China or FTO work | **Medium for located documents, low for coverage.** Verified leads retained; completeness claims rejected |
| Qwen | Some useful kill-test and remounting prompts | Search represented as “simulated”; no reliable citations; unsupported patent portfolios, “clear FTO,” “zero risk,” compute timings, sample counts, performance and novelty claims; omitted mandatory leads | **Low.** Used only as an idea prompt; patent, status, quantitative and legal assertions excluded |
| Mistral partial compilation | Actor names and document numbers supplied search leads | Three incomplete fragments from one lane; no final VibeGuard verdict; description passages treated as claims; prior art confused with infringement; US 2022/0067020 and Tractian were read as blanket Mahalanobis blocks; routine DSP was called potentially novel; licences were asserted without a claim chart | **Partial/low.** It is one partial source, never three reports or votes. Patentability, novelty, infringement, Mahalanobis and FTO conclusions are excluded unless independently established |
| Microsoft Copilot | Preserved frozen architecture and Level-1/Level-2 distinction; generally recognised Track C | No usable citation log; Tractian claim 1 was materially mischaracterised; separate Tractian patents were called one family; an abandoned Augury application was called active; KCF/Senseye overlap and numerical thresholds were invented or unsupported | **Low for patent/legal work; medium for project fidelity.** Only independently confirmed technical framing retained |

### Specific corrections with decision impact

- [Tractian US 11,429,900 claim 1](https://patents.google.com/patent/US11429900B1/en) is not a generic “edge baseline and local alert” claim. It requires a first device that transforms vibration data and sends selected peak information to a second device, reconstruction and model application at that second device, human confirmation, retraining, schedule determination, and sampling instructions. Mahalanobis appears as an optional description example, not as an independent-claim requirement.
- [Ford US 11,893,004](https://patents.google.com/patent/US11893004B2/en) does not prohibit every Mahalanobis implementation. Its independent claims require a vehicle sensor time series, a weighted moving mean, an inverse covariance matrix, a squared Mahalanobis distance, an anomaly indicator, and vehicle operation that excludes indicated data.
- [Augury US 2023/0213486](https://patents.google.com/patent/US20230213486A1/en) is abandoned; a later continuation may remain pending. Application status cannot be transferred across a family without checking each member.
- Separate 2025–2026 Tractian grants are not family members of US 11,429,900. Tractian’s own [patent marking page](https://tractian.com/en/patents) lists them as distinct patents.
- No current numerical VibeGuard success threshold exists. Any accuracy, false-alarm, abstention, session-count, or sigma threshold in a lane is at most a proposed value requiring owner approval and preregistration.

## 4. Search coverage and evidence gaps

### Work performed

The independent search combined:

- exact identifiers and title/assignee searches;
- G01H, G01M, G05B condition-monitoring concepts and keyword combinations covering vibration, target attribution, coupled machinery, interference, baseline subtraction, adaptive baseline, Mahalanobis, abstention/reject, remounting, order/speed normalisation, and edge/resource constraints;
- backward/forward citations and family navigation;
- independent-claim reading rather than abstract substitution;
- assignee/actor review for Tractian, Augury, Infinite Uptime, KCF, Senseye/Siemens and additional industrial actors;
- US, EP, WO, JP, CN, DE, BR and disclosed IN family members;
- non-patent literature, standards, sensor data sheets and official patent-eligibility guidance.

Google Patents was used for discovery, claim text, family navigation and links to official dockets. It was **not** treated as a conclusive legal-status opinion. Key US records were cross-linked to [USPTO Patent Center](https://patentcenter.uspto.gov/); the EP revocation event for EP 2 909 685 was checked in the published EPO event trail; NASA’s patent was checked against [NASA NTRS](https://ntrs.nasa.gov/citations/20080020439); current Indian eligibility materials were checked on the [Indian Patent Office guideline page](https://ipindia.gov.in/resource/patents-resources-guidelines).

### Coverage limits

| Area | Current coverage | Residual gap / consequence |
|---|---|---|
| US claims and families | Strong for named and closest leads | File-wrapper estoppel, claim construction and all continuations were not lawyer-reviewed |
| EPO | Key Augury revocation and selected EP families checked | National validation/lapse status must be checked country by country for FTO |
| India | Section 3(k), 2025 CRI Guidelines, and disclosed IN family leads reviewed | InPASS register status and full-text claim searches were not completed for every actor; Indian FTO is unresolved |
| China | CN family members identified for Ford, Mitsubishi and Valqua | CNIPA register status, translations and Chinese claim scope were not professionally verified; Chinese FTO is unresolved |
| Commercial actors | Tractian, Augury, Infinite Uptime, KCF and Senseye/Siemens searched | Assignee-name changes, unpublished applications and acquisitions can hide relevant rights |
| Non-patent literature | Single-sensor separation, condition monitoring, mounting, adaptive anomaly detection and standards covered | No systematic-review-level bibliography or exhaustive citation network was attempted |
| Product implementation | Frozen architecture and official component limits checked | No source code, bill-of-material receipts, timing trace, RAM trace or measured energy profile exists yet |

An exact-duplicate search is not a novelty opinion. Unpublished applications, mistranslations, recently issued claims, national continuations, doctrine of equivalents and non-patent public use remain outside this evidence review.

## 5. Verified patent-family ledger

Status statements below are current to the evidence date only and carry the stated confidence. “Active” is not a conclusion of infringement; “expired,” “abandoned” or “revoked” does not remove a document from the prior art.

| Family / identifiers | Priority; applicant | Jurisdictions and status checked | Independent-claim subject | Relevance; novelty and FTO significance | Confidence / primary source |
|---|---|---|---|---|---|
| **US 7,421,349 B1** | 15 May 2006; US Navy | US: expired/fee-related; ordinary term also reached May 2026 | Rolling-element-bearing detector that determines a model-based fault frequency, measures vibration and decides whether that frequency is sufficient; dependent claims add phase-coupled sideband logic | Strong prior art against claiming generic peak provenance in coupled/noisy machinery; specialised bearing model does not literally claim general target-vs-neighbour state attribution. No current US FTO concern if expiry is confirmed | High claim relevance; medium status. [Record and claims](https://patents.google.com/patent/US7421349B1/en), [USPTO application](https://patentcenter.uspto.gov/applications/11449185) |
| **US 7,346,461 B2** | 30 Sep 2005; NASA | US grant 18 Mar 2008; term-expiry inference Sep 2025, docket confirmation pending | Empirical mode decomposition/Hilbert-Huang processing: intrinsic mode functions, energetic selection, envelope/derivative and stability/non-linearity signatures | Technical background for sophisticated vibration analysis, but remote from frozen FFT/baseline logic and from target attribution; prior art, not a current FTO flag on present evidence | High identity/claim confidence; medium status. [NASA NTRS](https://ntrs.nasa.gov/citations/20080020439) |
| **Tractian US 11,429,900 B1; BR 10 2022 005021** | 26 Oct 2021; Tractian | US active; BR application discontinued | Two-device peak-selection/reconstruction/ML pipeline with human confirmation, retraining and sampling schedule | Important industrial edge-monitoring family, but frozen no-cloud/local MVP omits multiple required limitations. Destroys no generic feature by itself; requires product-specific claim chart for FTO | High US claim confidence; medium family status. [Claims/family](https://patents.google.com/patent/US11429900B1/en), [USPTO](https://patentcenter.uspto.gov/applications/17511539) |
| **KCF US 10,873,791 B1** | 29 Jul 2019; KCF Technologies | US active; maintenance event shown; anticipated 2039 | Resource-constrained network compression using baseline/subsequent sets; dependent claims cover FFT magnitude/phase, baseline subtraction and baseline regeneration criteria | Closest verified art to frequency-domain baseline subtraction, resource-aware node processing and threshold-controlled rebaselining. Claims also require compression/network elements, reducing literal overlap with local-only VibeGuard; very strong obviousness art | High. [Record/description/claims](https://patents.google.com/patent/US10873791B1/en), [USPTO](https://patentcenter.uspto.gov/applications/16524949) |
| **KCF US 9,271,170 B1** | 13 Mar 2013; KCF Technologies | US grant 23 Feb 2016; current docket status not independently resolved | Channel adaptation in sensor networks | Mandatory lead verified as communications/channel art, not a closest anomaly-classification claim. Potential relevance only if VibeGuard later adds adaptive radio/network behaviour | Medium. [KCF’s identification of the patent](https://kcftech.com/resources/blog/machine-health-solutions/which-wireless-vibration-sensors-can-you-trust/) |
| **Ford US 2022/0067020 A1; US 11,893,004 B2; DE 10 2021 121715; CN 114117334** | 26 Aug 2020; Ford | US active grant; DE/CN publications identified; national status not fully verified | Weighted moving mean and inverse covariance applied to sensor vectors; squared Mahalanobis anomaly indication; vehicle operation excludes anomalous sensor data | Shows broad adaptive Mahalanobis anomaly scoring was known. VibeGuard may omit vehicle operation and weighted adaptive elements, but a moving-baseline implementation needs a professional claim chart; not a blanket Mahalanobis prohibition | High US claim confidence; medium non-US status. [Claims/family](https://patents.google.com/patent/US11893004B2/en), [USPTO](https://patentcenter.uspto.gov/applications/17003088) |
| **Mitsubishi Heavy Industries US 2020/0285531 A1; US 11,334,414 B2; JP 7,470,849; CN 111649886; DE 10 2020 001020** | 4 Mar 2019; MHI | US, JP, CN, DE grants shown active in family navigation | Vibration amplitude and phase converted to a complex measured value; Mahalanobis distance to a past normal unit space; threshold abnormality decision | Very close to vibration-plus-Mahalanobis normal-space scoring. VibeGuard’s frozen features do not require complex amplitude/phase, but generic “Mahalanobis on vibration features” is not novel. CN member is a material FTO-search lead | High US claims; medium other jurisdictions. [Claims/family](https://patents.google.com/patent/US11334414B2/en), [USPTO](https://patentcenter.uspto.gov/applications/16790271) |
| **Valqua WO 2022/065103; US 2023/0332979 A1; US 12,590,863 B2; JP 7,594,599; CN 116209883; KR/TW** | 25 Sep 2020; Valqua | US grant 31 Mar 2026 active; JP/CN/TW grants shown; KR application identified | Frequency-band intensities, first Mahalanobis distance, two-dimensional spectral centre-of-gravity data, second Mahalanobis distance and predicted abnormality time | Strong prior art and potential active-rights lead for frequency-band Mahalanobis vibration analysis. Frozen MVP lacks the dual-distance centre-of-gravity and prognosis limitations | High US claim confidence; medium national status. [Claims/family](https://patents.google.com/patent/US20230332979A1/en), [USPTO](https://patentcenter.uspto.gov/applications/18026210) |
| **Rolls-Royce/OSyS WO 2010/094915; US 2012/0035885; US 9,874,472; EP 2 399 104** | 18 Feb 2009; Optimized Systems and Solutions / Rolls-Royce-related | US and EP grants shown active; WO ceased | Vibration amplitude indexed by frequency and rotational-speed subranges; learned noise-floor thresholds; significant spectral content above threshold | Strong art against speed-conditioned fingerprints, learned spectral noise floors and routine re-training on accepted-normal data. Requires rotation-speed input/tachometer, unlike frozen VibeGuard | High claims; medium current national status. [Claims/family](https://patents.google.com/patent/US20120035885A1/en) |
| **Augury US 9,835,594; US 10,330,647; US 10,983,097; US 11,579,122; EP 2 909 685; IN 2015DN04150** | 22 Oct 2012; Augury Systems | Several US continuations active; EP patent revoked May 2024; IN status unresolved; one later US application abandoned and another continuation pending | Models built from sensor data of multiple machines sharing characteristics and applied for machine-condition prediction/diagnosis | Strong fleet/model prior art but materially different from a single local node. Active US claims and unresolved IN member merit later product claim charts; EP revocation does not revoke US/IN relatives | High US/EP event confidence; low IN status. [US claim example](https://patents.google.com/patent/US10983097B2/en), [EP events](https://patents.google.com/patent/EP2909685B1/en) |
| **Augury US 2024/0255942; US 12,607,995 B2** | 9 Nov 2018; Augury Systems | US grant 21 Apr 2026 active; broader foreign family not fully checked | At least two non-stationary sensor outputs are fused, features tracked, and machine operating parameters adjusted | Relevant to speed/load/non-stationary normalisation, but requires plural sensors and machine adjustment. Separate from the earlier automatic-diagnosis family | High US claims/status. [Record/claims](https://patents.google.com/patent/US20240255942A1/en), [USPTO](https://patentcenter.uspto.gov/applications/18436253) |
| **Infinite Uptime / UCSD WO 2017/151447; US 2019/0061086** | 2 Mar 2016; Infinite Uptime and UCSD | US abandoned; WO ceased; no IN/CN member shown | Magnetic add-on housing containing vibration and acoustic sensors for real-time machine-tool monitoring | Product/packaging and multisensor tool-monitoring prior art; frozen rigid single-accelerometer node omits acoustic sensor, magnetic portable housing and machine-tool focus. No identified live US right in this family | High. [US record](https://patents.google.com/patent/US20190061086A1/en), [WO family](https://patents.google.com/patent/WO2017151447A1/en), [USPTO](https://patentcenter.uspto.gov/applications/16118109) |

Additional background leads—including operating-condition normalisation, triggered acquisition, one-class anomaly detection, peak separation and mounting structures—were reviewed but do not change the ledger conclusion: the frozen feature stack occupies a crowded field, while the exact later attribution mechanism remains an unproved search hypothesis rather than a cleared claim set.

## 6. Closest independent-claim analyses

### 6.1 KCF US 10,873,791 — closest to spectral baseline subtraction and constrained-node processing

Independent claim 1 is directed to compressing a baseline data set and subsequent data sets in a local-area network. The most VibeGuard-like language appears in dependent claims and the description: claim 4 takes a time signal through fixed-point conversion, FFT, magnitude/phase conversion, baseline construction or subtraction, scaling and truncation; claim 9 detects deviation sufficient to impair compression and then nullifies or regenerates the baseline. The description also discusses machine vibration, RMS and peaks, intermittent snapshots, thresholds, temporary changes and resource constraints. See the [KCF record](https://patents.google.com/patent/US10873791B1/en).

**Overlap:** machine-mounted sensor node, FFT, spectral magnitude baseline, subtraction, thresholded deviation, potential rebaselining, constrained computation.
**Missing from VibeGuard:** compression/decompression, radio transmission, LAN/base station, reconstruction and the claim’s communication purpose.
**Result:** no present finding that frozen local VibeGuard literally meets an independent claim, but this is powerful novelty/obviousness evidence against calling spectral subtraction, guarded rebaselining, fixed-point edge DSP, or resource-aware staging inventive by themselves.

### 6.2 Mitsubishi US 11,334,414 — closest to vibration-domain Mahalanobis anomaly scoring

Claim 1 acquires vibration amplitude and phase, converts them to a complex measured value, calculates Mahalanobis distance against a unit space of past measured values, and declares abnormality above a threshold. Method claim 5 follows the same structure. The record expressly says that a single vibration sensor may supply multiple frequency components and describes updating the unit space with measurements classified normal. See the [issued claims](https://patents.google.com/patent/US11334414B2/en).

**Overlap:** vibration sensor, frequency-derived values, normal unit space, Mahalanobis distance, thresholded abnormality, normal-only update concept.
**Frozen differences:** VibeGuard’s Mahalanobis target is based on RMS/peak/std/crest/kurtosis and possibly band features, not a required complex amplitude-phase representation; it does not require the claimed representation.
**Result:** generic Mahalanobis vibration monitoring and thresholding are plainly not a prospective VibeGuard novelty. A final implementation would still need a claim chart, especially in the US, China and Germany.

### 6.3 Rolls-Royce/OSyS US 9,874,472 — closest to operating-state-conditioned spectral baselines

Claim 1 receives vibration amplitude and rotation speed; stores each amplitude as a function of vibration frequency and speed; learns multiple amplitude thresholds representing noise floors for respective frequency/speed subranges; and classifies energy below the relevant threshold as noise and energy above it as significant spectral content. Dependent claims learn from normal runs, exclude non-noise training points and allow retraining. See the [published claims and family](https://patents.google.com/patent/US20120035885A1/en).

**Overlap:** normal-data learning, frequency bands, background/noise discrimination, thresholds and potential updates.
**Differences:** a rotation-speed channel, two-dimensional frequency/speed bins, distribution-derived noise floors and turbine/rotary-machine monitoring are not in the frozen MVP.
**Result:** speed/load-normalised fingerprints and learned band-specific noise floors are crowded directions; merely adding RPM or normal-state bins is unlikely to supply inventive step.

### 6.4 Tractian US 11,429,900 — important commercial family, not a match to the frozen architecture

Independent method claim 1 requires: first-device vibration acquisition; Fourier representation; modulus calculation and peak selection; transmission of peak information to a second device; second-device training using other machines; reconstructed vibration; model-based error identification; human confirmation; pattern addition and retraining; an operating schedule; and instructions back to the first device to sample during operation. Claim 6 recites the corresponding system. See the [claim text](https://patents.google.com/patent/US11429900B1/en).

VibeGuard has vibration acquisition and an FFT, but the frozen MVP has no second device, transmitted peaks, reconstruction, cross-machine training, human-confirmed retraining or schedule-controlled remote sampling. Local/no-cloud operation therefore avoids several literal elements, but it does **not** prove non-infringement of Tractian’s full portfolio or equivalents. The report lanes that paraphrased this claim as generic edge anomaly detection were unreliable.

### 6.5 Ford US 11,893,004 — broad Mahalanobis lead with vehicle limitations

Claim 1 receives vehicle-sensor vectors, determines a weighted moving mean and inverse covariance, computes squared Mahalanobis distance for a current vector, flags an anomalous sensor, and operates the vehicle without the flagged data. Claim 11 is the method counterpart. See the [issued claims](https://patents.google.com/patent/US11893004B2/en).

The patent matters if VibeGuard later adopts a recency-weighted moving baseline with inverse covariance, but its independent claims also require vehicle operation and data exclusion. It is prior art against the statistic and adaptive estimator; it is not evidence that all use of Mahalanobis infringes. The Mistral fragments’ blanket licence/FTO conclusion is excluded.

### 6.6 Valqua US 12,590,863 — frequency-band Mahalanobis prognosis

Claim 1 receives a vibration signal from a sensor on an operating object, calculates intensities for multiple frequency bands, calculates a first Mahalanobis distance, derives a two-dimensional centre of gravity of the intensities, calculates a second Mahalanobis distance, and predicts an abnormality-generation period from both. See the [claims](https://patents.google.com/patent/US20230332979A1/en).

VibeGuard overlaps in vibration bands and a possible first Mahalanobis score but lacks the spectral centre of gravity, second unit space/distance and prognosis. The family nevertheless forecloses any claim that “frequency bands plus Mahalanobis on vibration” is a new VibeGuard concept.

### 6.7 US 7,421,349 — source/provenance logic, but bearing-specific

Claim 1 determines a frequency proportional to rolling-element-bearing functionality from a fault model, measures vibration and determines whether the frequency is sufficient to indicate a developing bearing fault. Dependent claims add the phase-coupling detector. The description directly recognises peaks from mechanically/acoustically coupled systems and uses phase relations to test whether peaks share a generating process. See the [full record](https://patents.google.com/patent/US7421349B1/en).

It therefore raises the inventive-step bar for any claim framed as “use spectral structure to decide whether a peak came from the desired source.” It does **not** anticipate arbitrary normal/abnormal target attribution under independently varied neighbour states: the claim’s physical model, frequencies and output are bearing-fault specific.

### Combined conclusion

No single verified independent claim was shown to disclose every implementation detail of the complete frozen bill of materials and workflow. That is not enough for a patent path. The differentiating leftovers—ADXL345, ESP32, local operation, RGB output, price, the exact feature list and test rig—are ordinary design choices, while the analytical core is disclosed across closely related art. The frozen system has, at best, a narrow literal-novelty argument for an arbitrary combination; it lacks a credible inventive-step contribution.

## 7. Frozen-MVP closest-art feature chart

The chart uses only the required disclosure terms. “Other verified art” includes the Ford, Valqua, Navy and single-sensor literature discussed elsewhere; it does not imply that one combined reference exists.

| Frozen feature | KCF US 10,873,791 | MHI US 11,334,414 | Rolls US 9,874,472 | Tractian US 11,429,900 | Other verified art |
|---|---|---|---|---|---|
| Passive vibration monitoring at one mounted node | expressly disclosed | expressly disclosed | expressly disclosed | expressly disclosed | expressly disclosed |
| One rigid ADXL345 three-axis accelerometer | absent | absent | absent | absent | expressly disclosed |
| SPI sensor interface | unresolved | unresolved | unresolved | unresolved | expressly disclosed |
| ESP32-WROOM-32 or S3 | absent | absent | absent | absent | expressly disclosed |
| All analysis and alerting local; no cloud | absent | arguably suggested | unresolved | absent | expressly disclosed |
| DC removal | unresolved | unresolved | unresolved | unresolved | expressly disclosed |
| Hann window | unresolved | unresolved | unresolved | unresolved | expressly disclosed |
| Continuous RMS, peak, standard deviation, crest factor and kurtosis | arguably suggested | unresolved | unresolved | unresolved | expressly disclosed |
| Cheap time features trigger selected FFT analysis | arguably suggested | absent | absent | arguably suggested | expressly disclosed |
| FFT/frequency representation | expressly disclosed | expressly disclosed | necessarily implied | expressly disclosed | expressly disclosed |
| RMS threshold with persistence as minimum classifier | arguably suggested | expressly disclosed | expressly disclosed | unresolved | expressly disclosed |
| Mahalanobis unsupervised target | absent | expressly disclosed | absent | arguably suggested | expressly disclosed |
| Rigid proximity mounting | arguably suggested | arguably suggested | arguably suggested | arguably suggested | expressly disclosed |
| Band-limited features | expressly disclosed | expressly disclosed | expressly disclosed | arguably suggested | expressly disclosed |
| In-situ normal spectral baseline | expressly disclosed | expressly disclosed | expressly disclosed | arguably suggested | expressly disclosed |
| Baseline spectral subtraction | expressly disclosed | absent | absent | absent | expressly disclosed |
| RGB green/red/blue states | absent | absent | absent | absent | arguably suggested |
| Damped motor/fan rig with eccentric mass and loosened mount | absent | absent | absent | absent | expressly disclosed |
| Low-cost, local, no-subscription deployment | arguably suggested | absent | absent | absent | arguably suggested |
| ADXL345 sample-rate, bandwidth and noise limitations | absent | absent | absent | absent | expressly disclosed |
| RAM, flash, compute-time and latency constraints | expressly disclosed | arguably suggested | arguably suggested | arguably suggested | expressly disclosed |
| Target-machine attribution under neighbour interference | arguably suggested | absent | arguably suggested | arguably suggested | expressly disclosed |
| Calibration using independently known target/interferer states | absent | absent | arguably suggested | absent | expressly disclosed |
| Baseline update blocked during target faults or inadmissible interference | arguably suggested | arguably suggested | arguably suggested | absent | arguably suggested |
| Separate target-anomaly and interference-ambiguity evidence | absent | absent | absent | absent | arguably suggested |
| Confidence-gated abstention/unknown output | absent | absent | absent | absent | arguably suggested |
| Remounting-transfer compensation | absent | absent | absent | absent | arguably suggested |
| Speed/load-normalised target fingerprint | absent | absent | expressly disclosed | absent | expressly disclosed |

The chart shows why feature counting is misleading. Several frozen details are absent from individual patents, but their absence is not an inventive step; component selection, local execution and a coloured LED do not transform known monitoring logic into a non-obvious technical mechanism.

## 8. Mandatory named-lead investigation

### US 7,421,349 and US 7,346,461

- **US 7,421,349** was fully claim-read. It is specialised rolling-element-bearing provenance art using model-derived frequencies and, dependently, phase-coupled sidebands. It is prior art even though the US right appears expired. It is not an exact spatial-attribution patent, and the Phase 2/Kimi and Qwen characterisations of it as the literal VibeGuard problem were too broad.
- **US 7,346,461** was verified through NASA’s official record. Its EMD/Hilbert-Huang stability spectrum and non-linearity indicator are technically remote from the frozen FFT/statistical feature chain. It is a valid historical vibration-analysis lead, not the closest VibeGuard reference.

### Commercial actors and mandatory numbered leads

| Actor / mandatory lead | Investigation result | Present implication |
|---|---|---|
| **Tractian** | Actual US 11,429,900/BR family verified and independently claim-read. Tractian’s [current patent page](https://tractian.com/en/patents) lists separate 2025–2026 grants on sampling, mounts, rotation speed, longitudinal failure analysis, housing and interfaces; these are not continuations of one family merely because they share an assignee | Frozen local MVP omits material US 11,429,900 elements. Later dynamic sampling, mounting and failure-analysis patents require targeted review before productisation; no blanket clearance |
| **KCF** | US 9,271,170 verified as channel-adaptation art; US 10,873,791 verified as active compression/baseline art | The second is a major obviousness and potential implementation lead for spectral subtraction/rebaseline; the first is peripheral unless networking changes |
| **Augury** | US automatic-diagnosis continuations identified; EP 2,909,685 revoked; IN 2015DN04150 status unresolved; non-stationary-machine US 12,607,995 issued 21 Apr 2026 | Fleet/multisensor claims differ from frozen single-node architecture, but US and possible Indian rights require later claim charts. Copilot’s status/family statements were corrected |
| **Infinite Uptime** | WO 2017/151447 ceased and US 2019/0061086 abandoned; claim focus is magnetic housing plus vibration and acoustic sensing on machine tools | Prior art remains; no live US right found in that family. Absence of IN/CN members in family navigation is not a general freedom conclusion |
| **Senseye / Siemens** | Current Senseye is a Siemens cloud predictive-maintenance product. No load-bearing vibration patent family attributable to the searched “Senseye” identity was verified; searches also collide with an unrelated ocular-sensing company | No overlap or freedom conclusion may be drawn from the failed assignee match. Search Siemens portfolios by inventor, acquisition chain and CPC before commercial clearance |
| **US 2022/0067020 / US 11,893,004** | Ford family and US claims verified; CN and DE members identified | Prior art against adaptive Mahalanobis; potential FTO only for implementations meeting all jurisdiction-specific claim limitations |
| **US 10,873,791** | KCF claims, baseline description and current US docket link verified | Directly defeats novelty stories based only on edge FFT, frequency-domain subtraction, resource constraints or thresholded rebaseline |
| **US 9,271,170** | Identity and title verified from KCF’s own technical publication; full current docket review unresolved | Record the gap; do not inflate it into vibration-classification coverage |

### India and China

The search found an Augury Indian national-phase lead and Chinese members of the Ford, MHI and Valqua families. Their existence increases search and FTO diligence; it does not establish claim coverage. InPASS/CNIPA status, prosecution history, translations and local claim construction are unresolved. None of the research lanes supplied a defensible India-or-China clearance opinion.

## 9. Non-patent prior art and standards

| Source | Verified teaching | Consequence for VibeGuard |
|---|---|---|
| [ISO 13373-1](https://www.iso.org/standard/21831.html) | General vibration condition-monitoring measurement/data-collection practice, including transducer choice, location, attachment, operating conditions and continuous/periodic monitoring | Rigid repeatable mounting, labelled operating states and disciplined acquisition are established measurement practice, not presumptive inventions |
| [ISO 13373-2](https://www.iso.org/standard/68128.html) | Common vibration-data processing, signature analysis and signal enhancement | FFT, bands and enhancement must be treated as conventional unless a specific new physical mechanism is shown |
| [ISO 20816-1](https://www.iso.org/standard/89921.html) and [ISO 20816-3](https://www.iso.org/standard/87746.html) | Measurement/evaluation of machine vibration and machine-class context | Useful test discipline; not an automatic algorithm threshold and not a VibeGuard validation substitute |
| Nguyen, Rutten and Golinval, [single-sensor blind-source-separation fault diagnosis](https://onlinelibrary.wiley.com/doi/10.3233/SAV-2012-0688) (2012) | Uses block-Hankel constructions with PCA/SOBI to compare reference and current subspaces from one vibration measurement | A single-sensor fault/source-discrimination problem predates VibeGuard; a stronger differentiating mechanism is required |
| Seitz et al., [single-sensor monitoring of several vibration-emitting motors](https://link.springer.com/chapter/10.1007/978-3-031-27933-1_17) (2023) | One sensor and frequency-domain neural processing classified the running states of three motors in a proof of concept | Direct non-patent evidence that single-sensor multi-source state inference and frequency transformation are known; also shows why Level-2 labels matter |
| Atmaja et al., [lab-scale vibration dataset and baselines](https://scholar.its.ac.id/en/publications/lab-scale-vibration-analysis-dataset-and-baseline-methods-for-mac/) | Lab data for normal, imbalance, misalignment and bearing-fault states with standard classifiers/features | A clean rig can produce excellent scores without proving field attribution or patentability |
| [Accelerometer mounting study/white paper](https://www.pcb.com/Contentstore/MktgContent/WhitePapers/WPL_68_HowSensorMountingAffectsMeasurements.pdf) | Mounting materially changes overall vibration and FFT results | Remounting robustness is necessary evidence; recognising the problem alone is not novel |
| [ADXL345 official data sheet](https://www.analog.com/media/en/technical-documentation/data-sheets/adxl345.pdf) | 3-axis, 13-bit/±16 g device; bandwidth is half ODR; 3200/1600 Hz ODR requires at least 2 MHz SPI | The architecture report’s phrase “1600 Hz Nyquist bandwidth” is imprecise. Maximum nominal bandwidth is 1600 Hz at 3200 Hz ODR; actual useful fault band also depends on noise, mounting and alias control |
| [IIS3DWB official data sheet](https://www.st.com/resource/en/datasheet/iis3dwb.pdf) | Industrial vibration sensor with flat range to about 6 kHz and 26.7 kHz ODR | Correctly remains a later high-frequency/bearing upgrade; ADXL345 tests must not be represented as high-frequency bearing validation |
| [Espressif DSP library](https://docs.espressif.com/projects/esp-dsp/en/latest/index.html) and [FFT examples](https://docs.espressif.com/projects/esp-dsp/en/latest/esp32/esp-dsp-examples.html) | Optimised FFT/window support on ESP32/ESP32-S3, including 1024-sample examples | Frozen time features and triggered FFT are technically feasible; availability of optimised implementation weakens a resource-scheduling novelty story |

Mahalanobis distance, one-class normal modelling, reject/unknown decisions, drift adaptation and spectral/source-separation methods are also mature statistical/DSP subjects. The standards and literature do not supply VibeGuard’s acceptance numbers: false-alarm, miss, attribution, abstention and remount limits must be proposed, owner-approved and preregistered rather than quoted as existing facts.

## 10. Current frozen-MVP patent assessment

| Category | Assessment |
|---|---|
| Technical identity | A useful low-cost teaching prototype for local vibration monitoring: one rigid ADXL345 over SPI to ESP32-WROOM-32/S3; DC removal; Hann; continuous RMS/peak/std/crest/kurtosis; threshold/persistence; triggered FFT; bands/baseline subtraction; optional Mahalanobis; RGB alert; motor/fan rig |
| Correct fidelity | Passive monitoring, not active cancellation; not wearable/haptic or audio; not cloud, RUL or a generic-AI platform; not a multi-sensor MVP; ADXL345 supports lower-frequency imbalance/misalignment/looseness experiments, not a high-frequency bearing claim |
| Novelty | Individual analytical and architectural elements are known. No credible new independent-claim nucleus was identified in the frozen MVP |
| Inventive step | Combining a commodity accelerometer, microcontroller, standard window/FFT/features, threshold or Mahalanobis normal model, spectral baseline and LED gives expected monitoring results. Cost, no cloud and ESP32 selection do not supply non-obviousness |
| Eligibility | A sensor-to-machine-state method can have a physical technical context, but generic mathematical scoring and an alert face US abstract-idea, EPO technical-contribution and India section 3(k) scrutiny. Eligibility would not cure novelty/obviousness |
| FTO | No infringement conclusion. Several active rights have only partial overlap; India/China and later commercial portfolios remain unresolved. A final code/claim chart is required before product release |
| Evidence | Level-1 bench demonstration is feasible but unbuilt/unreported. Level-2 target attribution, remount, speed/load and independent ground truth are absent |
| Patent-development result | **Do not treat the frozen MVP as the invention and do not file a patent-first application on the present feature aggregation.** Preserve it as the experimental platform for a later mechanism |

The frequently proposed differentiators—single sensor, edge-only, low price, no subscription, ESP32, FFT, spectral subtraction and Mahalanobis—are positioning or implementation choices, not a defensible technical contribution on this evidence.

## 11. Candidate invention-direction matrix

The matrix tests each required direction as a *stand-alone patent-development proposition*. “Difference” means only an apparent difference from the cited item, not novelty. Unless a row says otherwise, it retains the frozen ADXL345/SPI/ESP32 hardware, its low-frequency usable band, local processing and the ₹5,000 ceiling. Exact ODR, window, hop, band edges, thresholds and sample counts are experimental variables, not frozen facts. At the ADXL345 maximum setting, 3200 Hz ODR corresponds to a nominal 1600 Hz bandwidth and requires at least 2 MHz SPI; a lower ODR/band should be selected if it gives better noise, energy and attribution performance.

### Technical and evidentiary matrix

| # | Direction; physical problem | Prospective contribution; mechanism type; measurable effect | Closest verified art; overlap; apparent difference | Baseline and required experiment |
|---|---|---|---|---|
| 1 | **Single-node target attribution under neighbour interference.** A target-mounted sensor contains mixed target, neighbour and structural vibration. | Correctly assign an abnormal indication to the target rather than merely detect a changed mixture. As stated, this is a desired diagnostic effect, not yet a mechanism. | Nguyen single-sensor BSS and Seitz multi-motor inference address source/state separation; US 7,421,349 recognises coupled vibration and derives source-related bearing components; Rolls-Royce indexes machine signatures by speed. The phrase “single-node attribution” is not a differentiator without a specific causal procedure. | Compare RMS/persistence, ordinary FFT features, Mahalanobis and subtraction under independently labelled target/interferer states. A dual-motor rig and later dense-machine data must measure attribution error, not only binary accuracy. |
| 2 | **In-situ target fingerprint from known operating states.** Installation and operating-state changes make a generic normal model unreliable. | Acquire a target-conditioned signature while its state is independently known; calibration/statistical modelling; lower false alarms across admissible operating states. | Rolls-Royce uses trained, speed-indexed machine signatures; US 7,421,349 uses model-derived frequency sets; MHI and Ford form normal spaces from reference data. The apparent difference is the proposed single-node target/interferer labelling protocol, but known-state calibration itself is routine. | Compare one pooled normal baseline against state-conditioned fingerprints. Vary target and interferer state/speed/load, holding mount and acquisition fixed; then test held-out sessions. |
| 3 | **Contamination-guarded spectral subtraction/band update.** A fault or changed neighbour can be absorbed into a learned “normal” spectrum. | Update a noise/interference envelope only when target-normal and interferer-admissible evidence is independently established; integrated adaptive-signal mechanism; reduce fault masking and post-drift false alarms. | KCF US 10,873,791 performs FFT magnitude comparison, baseline subtraction and threshold-controlled rebaselining; MHI constructs a normal unit space; drift safeguards are familiar in anomaly detection. The proposed dual-state admission gate and separate interference envelope were not found together in a verified independent claim, but the search is incomplete. | Compare fixed baseline, unconditional exponential update, KCF-like threshold rebaseline and the guarded update. Deliberately introduce target faults and neighbour changes during update; measure model contamination, miss rate and recovery. |
| 4 | **Confidence-gated/abstaining decision.** Mixed-source evidence may be too ambiguous to support a target-fault label. | Produce target-abnormal, target-normal or unknown based on separately calibrated abnormality and ambiguity evidence; statistical decision layer; reduce false target attribution at a declared coverage cost. | Reject options and confidence calibration are established machine-learning practice; Tractian routes detections through cross-machine models and human confirmation. The apparent difference is a target/interference-specific ambiguity score linked to update protection, not abstention alone. | Compare forced binary decisions with calibrated abstention at matched coverage. Report attribution error, false alarms per hour, missed detections, calibration and unknown rate; a result obtained only by abstaining nearly always fails. |
| 5 | **Remounting compensation.** Sensor orientation, coupling and placement shift amplitudes and spectra after service. | Detect a mount-domain change, map an admissible remount to the target representation, or invalidate calibration; calibration/measurement mechanism; preserve diagnostic meaning without learning faults as normal. | ISO 13373 measurement practice and mounting studies make mount sensitivity known; transfer/domain-adaptation literature makes compensation broadly expected. No verified close independent claim was found for this exact low-cost implementation, but a claim-focused remounting search remains incomplete. | Reinstall the same sensor through blinded, independently repeated mounts. Compare no correction, full recalibration, simple axis/vector-normalisation and proposed transfer/invalidation; measure repeatability and fault separation. |
| 6 | **Resource-aware two-stage processing.** Continuous FFT work may be unnecessary on an MCU. | Cheap time features trigger selected FFT/band analysis while maintaining a measured attribution envelope; implementation/scheduling; reduce compute/energy/latency without losing diagnostic performance. | The frozen architecture already contains triggered FFT; KCF expressly targets resource-constrained monitoring and compressed spectral processing; ESP-DSP supplies optimised windows/FFTs. Selecting expensive processing after a cheap detector is routine. | Run continuous FFT, triggered FFT and time-only baselines on identical streams. Measure trigger misses, end-to-end delay, cycles/time, RAM/flash and energy, not just classifier accuracy. |
| 7 | **Speed/load-normalised fingerprints or order features.** A healthy speed/load shift can resemble a fault and move spectral lines. | Condition features on permitted machine-state information or normalise frequency to order; signal-processing/calibration; improve state invariance while retaining fault sensitivity. | Rolls-Royce US 9,874,472 expressly trains vibration/noise-floor measures indexed by rotational speed and frequency; order tracking is standard machinery analysis. A single-node implementation does not overcome that teaching. | With independently measured or commanded speed/load, compare unnormalised bands, state-binned fingerprints and order-related features on unseen conditions. If no state input is available, test only estimators derived from the same sensor and disclose their ambiguity. |
| 8 | **Safeguarded drift-aware adaptation.** Ageing and environment shift the normal distribution, while abnormal samples must not become normal. | Slow baseline adaptation admitted only under normal-state, confidence and stability gates, with rollback/freeze; adaptive statistical mechanism; reduce drift false alarms without increased misses. | KCF has threshold-governed rebaselining; MHI/Ford use reference normal spaces; guarded concept-drift adaptation is established. The exact combination with labelled source ambiguity was not verified, but drift adaptation alone is an obviousness-heavy direction. | Compare frozen, unconditional and guarded adaptive models across gradual drift, abrupt neighbour change and seeded target fault. Measure false alarm, miss, contamination and rollback behaviour. |
| 9 | **Deployment/calibration protocol for independent labels without a multi-sensor product.** Mixed-source training data otherwise lacks truth. | During commissioning, command or observe target/interferer states independently, collect a factorial label set, then deploy one permanent sensor; deployment/calibration practice; make attribution falsifiable. | Controlled calibration, designed experiments and source labels are standard; Rolls-Royce trains state-indexed signatures and Seitz uses labelled motor states. Removing temporary/reference instrumentation from the sold product is not itself inventive. | Use the same algorithm with opportunistic/unverified labels versus the controlled protocol. Blind the test labels; measure label error, attribution and reproducibility. Any temporary tachometer/current reference is test equipment, not frozen product hardware. |
| 10 | **Integrated label-aware, contamination-protected target attribution.** The real problem combines mixed vibration, ambiguous decisions, drift and remount changes. | Commission target/interferer-conditioned fingerprints from independent labels; compute separate target-abnormality and interference-ambiguity evidence; abstain when causal attribution is unsupported; permit baseline/interference-envelope updates only under admissible labelled/confident states; invalidate or transfer on remount. Integrated technical mechanism; reduce *wrong-source* alarms and contaminated learning at useful coverage. | The component teachings above are individually close: Nguyen/Seitz for single-sensor separation, KCF for spectral subtraction/rebaseline, Rolls-Royce for state-indexed signatures, MHI/Ford for normal-space distances, and known reject/adaptation practice. No one verified item was shown to contain this complete causal control loop, but no complete claim or NPL search has established absence either. | Full factorial Level-2 test with ablations of label conditioning, ambiguity gate, update guard and remount handling. Compare all mandatory baselines on blinded held-out sessions and later independently labelled field data. |

### Feasibility, resource and risk matrix

| # | Changes and resource impact | Cost, three-month status and later work | Patent risks; classification; confidence; kill condition |
|---|---|---|---|
| 1 | Software/data-design change; same ODR/band. FFT/fingerprint storage adds modest, configuration-dependent RAM/flash; latency is at least one analysis window; triggered operation can limit energy. Must be profiled on the selected ESP32. | Dual-motor bench enhancement can begin within three months using the existing rig plus a neighbour motor; convincing field attribution cannot. Likely remains under the ceiling if existing computing and test instruments are available. | Very high novelty/obviousness and medium eligibility/FTO uncertainty. **Track D as a bare objective; low confidence.** Kill if no specific mechanism beats the best baseline on wrong-source attribution. |
| 2 | Store fingerprints per known state; no necessary ODR increase. RAM/flash scale with axes × bands/features × state cells; compute is table selection plus normal scoring; little extra energy. | Bench implementation is feasible within three months and budget; broader speed/load coverage is later. | High obviousness, medium eligibility, low-to-medium implementation-specific FTO risk. **Track D alone; medium confidence.** Kill if state conditioning gives no held-out robustness or labels cannot be obtained independently. |
| 3 | Maintain target baseline plus interference envelope and update metadata; no necessary bandwidth change. Adds bounded storage and update checks; negligible latency relative to FFT, small energy increase. Exact footprint must be measured. | A bench prototype is feasible in three months at near-zero incremental hardware cost; proof under natural drift/field contamination is later. | Medium-to-high novelty risk, high obviousness risk due KCF/adaptive practice, medium eligibility and FTO uncertainty. **Track D alone; medium-low confidence.** Kill if gating cannot prevent fault ingestion or performs no better than a fixed baseline. |
| 4 | Add calibrated ambiguity model and unknown output. No sample-rate change; small model/storage and scoring overhead; decision may wait additional windows, increasing delay but potentially reducing unnecessary alerts. RGB semantics would need owner-approved encoding for unknown (for example, a distinct blink), without changing the frozen three-state MVP demonstration. | Bench implementation is feasible and cheap in three months; representative ambiguity calibration is later. | High novelty/obviousness and eligibility risk; generally low FTO exposure in the abstract but claim search incomplete. **Track D alone; medium confidence.** Kill if lower error is explained by unusably low decision coverage or confidence is uncalibrated. |
| 5 | Orientation/coupling checks, calibration metadata and perhaps vector/order features; no necessary ODR change. Storage/compute modest; a remount check adds commissioning latency, not continuous energy. | Repeated bench remounts are feasible within three months; cross-installation transfer needs more fixtures, operators and field time. | High obviousness, medium eligibility, unresolved claim-specific FTO. **Track D alone; low-to-medium confidence.** Kill if full recalibration remains necessary or compensation suppresses real faults. |
| 6 | Already largely frozen: continuous cheap features, triggered FFT. FFT buffers dominate RAM; exact size depends on sample format and transform length. Triggering should reduce average compute/energy but may increase detection delay or miss short events. Profile cycles, stack/heap, flash, latency and power. | Feasible within three months and budget. It is an engineering optimisation, not a later patent programme by itself. | Very high novelty/obviousness; medium software-eligibility; low-to-medium FTO. **Track D; high confidence.** Kill as a patent direction if gains are only expected resource savings with no non-obvious attribution effect. |
| 7 | Needs permitted speed/load metadata or a same-sensor estimator and resampling/order features. May require longer buffers/interpolation and more compute; ODR must cover relevant harmonics without aliasing. Latency/energy rise with tracking complexity. | Commanded-speed bench tests can fit three months; robust variable-speed field work and any additional reference instrument are later. No product sensor may be silently added. | Very high obviousness and meaningful Rolls-Royce FTO-review need; medium eligibility. **Track D alone; high confidence.** Kill if speed/load is unavailable, unreliable, or normalisation removes fault information. |
| 8 | Add age/stability/confidence metadata, bounded update and rollback snapshots. No ODR change; small-to-moderate flash/RAM and compute; update cadence affects energy minimally compared with sampling/FFT. | Simulation and accelerated bench drift are feasible in three months; long-duration natural drift is later. | High obviousness, medium eligibility, medium KCF/MHI/Ford-related FTO uncertainty depending implementation. **Track D alone; medium confidence.** Kill if abnormal data enters the normal model or a frozen model performs as well. |
| 9 | Requires a commissioning state schedule, label capture and traceability; product remains one sensor. Test references may add experimental cost but not product cost. No inherent ODR, bandwidth, RAM, latency or continuous-energy penalty beyond storing/using state-conditioned calibration. | A controlled two-motor protocol is feasible within three months if safe independent controls are available; real-machine permissions and ground truth are later. | Very high novelty/obviousness and high eligibility risk as deployment practice; generally low claim exposure but unresolved. **Track D alone; high confidence.** Kill if independent states cannot be safely obtained or labels are not transferable to deployment. |
| 10 | Combines bounded fingerprints, target and ambiguity scores, gated updates, abstention and remount validity. No required sensor/ODR change, but FFT/band buffers plus multiple state models must fit measured RAM/flash. Latency must remain below the owner-approved alert window; energy and worst-case compute must be profiled. | The frozen Level-1 MVP and a small dual-motor research scaffold fit three months/₹5,000; a credible claim-supporting result requires later field access, more sessions and professional search. | Novelty unresolved; **very high obviousness**, medium-to-high eligibility and medium FTO uncertainty. **Track C; medium-low confidence.** Kill if ablations show no synergistic wrong-source/contamination benefit, if useful coverage collapses, if field evidence fails, or if closer art reads on the complete loop. |

Directions 1–9 are therefore rejected as independent patent stories. They may remain conventional controls or components of direction 10. Direction 10 is the only survivor, and only as a confidential research hypothesis on Track C; that classification is not a patentability conclusion.

## 12. Strongest surviving direction

### Prospective mechanism

The strongest direction is a **label-aware, contamination-protected, confidence-gated target-attribution loop for a single permanently deployed vibration node**:

1. During controlled commissioning, independently establish the target state and the neighbour/interferer state. Acquire a target-conditioned normal fingerprint and a separate admissible interference envelope across permitted speed/load cells. Temporary test references may establish truth, but the deployed product remains the frozen single node.
2. At inference, transform the same target-mounted acceleration stream into two logically separate quantities: (a) evidence that the target departs from its admissible target fingerprint and (b) evidence that the observation is ambiguous because it lies within, or has shifted beyond, the characterised interference envelope.
3. Declare target abnormal only when target-departure evidence is sufficient *and* source ambiguity is acceptably low. Otherwise declare normal or abstain/unknown. “Unknown” needs an owner-approved user-interface state; it cannot silently mean red or green.
4. Admit a sample to target-baseline or interference-envelope adaptation only when the relevant independently established state, confidence/stability checks and mount-validity checks all permit it. Preserve rollback/freeze metadata so a fault or changed neighbour is not irreversibly learned as normal.
5. Detect a remount domain change and either apply a validated transfer mapping or invalidate the affected fingerprint and require controlled recalibration.

The mechanism is not “FFT + Mahalanobis.” It is also not spectral subtraction, calibration, abstention, drift adaptation or remount handling in isolation. Its prospective technical contribution would have to be the *causal coordination* of independently labelled source states, distinct abnormality/ambiguity evidence, update admission and mount validity so that a single physical measurement produces fewer wrong-source alarms and less contaminated learning at a useful decision coverage.

### What is and is not presently established

- **Established:** the physical mixed-vibration problem is real; the frozen platform can collect and locally process the relevant low-frequency signals; each component technique has substantial prior art.
- **Inference:** the integrated loop appears more specific than the complete subject matter of any one independent claim verified in this audit.
- **Not established:** novelty over all patent/NPL art, non-obvious synergy, field-level attribution, an enabling parameterisation, useful abstention coverage, remount transfer, Indian/Chinese clearance or FTO.
- **Required bridge:** the semester build implements the measurement pipeline and a labelled dual-motor scaffold; later work supplies blinded repeated-session and real dense-machine evidence. This remains VibeGuard because it preserves the same target-mounted sensor, edge pipeline, anomaly purpose and local alert rather than becoming a cloud or multi-node maintenance platform.

No final legal claim is drafted here. The mechanism must remain confidential until evidence and institutional IPR review justify claim drafting.

## 13. Bench demonstration versus field-attribution evidence

| Evidence level | Permitted conclusion | Required design | What it cannot establish |
|---|---|---|---|
| **Level 1: isolated semester bench** | The frozen node acquires usable low-frequency vibration; imbalance/controlled looseness changes measured features; the local RMS/persistence and target Mahalanobis pipelines can run; RGB states and compute constraints work | One damped 12 V motor/fan; normal versus safely attached eccentric mass, with looseness secondary; rigid mount; repeated runs; held-out data; RMS/persistence, FFT-feature, Mahalanobis and subtraction comparisons; report ODR, usable band, alias control, RAM, flash, latency and errors | Neighbour robustness, source attribution, real-machine generalisation, remount transfer, patentability, eligibility or FTO |
| **Level 2A: controlled dual-motor research rig** | Whether target/interferer labels, ambiguity gating and contamination protection improve wrong-source decisions under designed interference | One permanent target sensor; separately controlled target and neighbour; factorial target normal/abnormal × interferer off/normal/abnormal; speed/load variation; independent ground truth; repeated days/sessions/remounts; blinded hold-out; all baselines and ablations | Broad industrial applicability or natural field drift; it is an intermediate patent-evidence level, not field proof |
| **Level 2B: dense-machine field evidence** | Whether the same mechanism produces a reproducible technical effect in realistic structural coupling, operating variation and remounting | Authorised target and neighbours; independent state/maintenance truth; representative speeds/loads; repeated installations, operators and days; logged ambiguous states; preregistered metrics and exclusions; no leakage from test labels | A legal patentability or FTO opinion; even positive evidence must be combined with a professional claim search |

At all levels report sensitivity, specificity, balanced accuracy, false alarms per hour, missed detections, target-attribution error, confidence calibration, abstention rate/coverage, detection delay, remount repeatability, compute time, RAM/flash, ODR/usable bandwidth and power where material. A high Level-1 binary score cannot be presented as Level-2 source attribution.

## 14. Novelty analysis

Novelty asks whether a single earlier item contains every required element, not whether the overall idea feels familiar.

### Frozen MVP

The audit did not identify one verified independent claim reciting the frozen bill of materials and every software step verbatim. That absence does not establish novelty. The putative contribution cannot be the product-specific aggregation: accelerometer acquisition, edge DSP, DC removal/windowing, time features, triggered FFT, bands, spectral baseline comparison, Mahalanobis/threshold anomaly scoring and a local alert are individually and collectively conventional monitoring choices. Product part numbers, low price, no cloud and RGB output do not create a credible technical nucleus.

### Direction 10

No single verified patent or NPL item in the completed search was shown to disclose *all* of the following in one arrangement: independently labelled target and interferer commissioning; separate target-abnormality and interference-ambiguity evidence from one permanent node; abstention based on the latter; update admission protected by both source state and confidence; and remount transfer/invalidation. This is only a **provisional search observation**. It is not a novelty conclusion because:

- the search is not exhaustive and official Indian/Chinese claim/status coverage is incomplete;
- remounting-transfer, reject-option, drift/adaptation and source-separation literature was not searched to saturation;
- later continuations and unpublished applications may matter;
- several elements are drafted here at a functional level and must be technically enabled before meaningful claim comparison; and
- a claim omitting the detailed causal coordination would fall back into the known component teachings.

The novelty confidence for direction 10 is therefore **low-to-medium**, with high risk. A professional claim search should be run only after experiments freeze the actual mechanism.

## 15. Inventive-step / obviousness analysis

Obviousness is the principal patent risk even if direction 10 survives a single-reference novelty screen. A skilled condition-monitoring/DSP practitioner has strong reasons to combine:

- one-sensor source/state discrimination from Nguyen or Seitz;
- state/speed-conditioned signatures from Rolls-Royce;
- normal-space distance scoring from MHI, Ford or standard one-class methods;
- spectral baseline subtraction and gated rebaselining from KCF;
- routine confidence/reject decisions;
- standard safeguards against concept-drift contamination; and
- known mounting calibration or domain-transfer practice.

The physical problem itself—neighbour vibration corrupting a target measurement—supplies motivation to combine those teachings. ESP32 resource limits, local operation and a low budget are ordinary design constraints. Merely implementing each known module would predictably yield each module’s expected result.

To rebut that risk, later evidence would need to show a technically specific interaction, not only better classifier accuracy. The most useful showing would be that the coordinated source-label/ambiguity/update/mount loop produces a reproducible reduction in wrong-source alarms and contamination relative to every component and plausible combination, at a preregistered useful coverage and resource envelope, including unseen field states. Ablations must show that the effect disappears when the allegedly cooperative element is removed. If gains are additive, parameter-tuned to one rig, or explained by more labels/model capacity, the obviousness case remains overwhelming.

Current inventive-step confidence is **low**; risk is **very high**.

## 16. Patent-eligibility analysis

Eligibility is separate from novelty, inventive step and FTO. The analysis below is issue-spotting, not a jurisdictional legal opinion.

| Jurisdiction | Principal risk | Technical framing/evidence needed | Current assessment |
|---|---|---|---|
| United States | Mathematical relationships, feature transformation, distance/confidence scores and a generic alert may be characterised as an abstract idea implemented on generic computing under the USPTO’s [MPEP §2106](https://www.uspto.gov/web/offices/pac/mpep/s2106.html). The USPTO’s August 2025 [subject-matter eligibility memorandum](https://www.uspto.gov/sites/default/files/documents/memo-101-20250804.pdf) does not remove the need to analyse a claim as a whole and identify a practical application. | Tie the claimed steps to a particular target-mounted physical measurement and a specific control of measurement validity: source-conditioned acquisition, ambiguity-dependent fault attribution, contamination-blocked model update, remount invalidation and a demonstrated change in machine-monitoring operation. Avoid claiming only “calculate score and display result.” | **Medium-to-high risk.** Physical sensing helps, but generic DSP/ML language remains vulnerable. |
| European Patent Office | Mathematical methods contribute to inventive step only insofar as they serve a technical purpose and produce a technical effect across the claim scope; the EPO’s current guidance addresses [mathematical methods](https://www.epo.org/en/legal/guidelines-epc/2026/g_ii_3_3.html) and [computer programs](https://www.epo.org/en/legal/guidelines-epc/2026/g_ii_3_6.html). | Specify how the method derives or preserves information about a physical machine state from measured vibration and improves the reliability of that technical measurement under coupled interference. Provide causal experimental support for the effect, not a business/maintenance label. | **Medium risk** if narrowly enabled around physical measurement; otherwise high. |
| India | Section 3(k) of the [Patents Act, 1970](https://ipindia.gov.in/writereaddata/Portal/IPOAct/1_31_1_patent-act-1970-11march2015.pdf) excludes a mathematical or business method, computer programme per se or algorithm. The Indian Patent Office’s [CRI Guidelines 2025](https://ipindia.gov.in/storage/uploads/docs-operator/62449276-74f6-438d-92fc-14b2cf3fa204.pdf) require analysis of the substance and claimed technical solution/effect. | Explain a concrete sensor-machine relationship, technical means and experimentally shown improvement in physical condition measurement. Software on an ESP32 is not enough; conversely, eligibility should not be reduced to a slogan that “novel hardware is mandatory.” Indian counsel must assess the actual claim. | **High unresolved risk**, compounded by incomplete Indian family/claim searching. |

Changing Mahalanobis distance to another classifier would not solve eligibility. Any eventual drafting should focus on the enabled physical measurement-control mechanism and its demonstrated technical effect, while leaving legal strategy to qualified counsel.

## 17. FTO risk analysis

FTO asks whether a particular act in a particular country falls within an enforceable claim. It cannot be answered from conceptual similarity, an abstract, company product literature or the absence of a search result. This audit did not obtain a complete current claim set, prosecution history, ownership/licence record or product implementation, so **no clearance or infringement conclusion is given**.

| Family/area | Potential implementation exposure | Material omissions or distinctions in frozen/proposed VibeGuard | Current action/risk |
|---|---|---|---|
| KCF US 10,873,791 B1 | FFT magnitude, baseline spectral subtraction and controlled rebaseline on constrained vibration nodes | Its independent claim includes particular compression, network transmission/storage and spectral processing relationships; frozen local VibeGuard is not shown to contain every limitation | Claim chart the final data path and any networking/compression. **Medium implementation-specific US risk; unresolved elsewhere.** |
| KCF US 9,271,170 B1 | Sensor-network channel adaptation may become relevant if later architecture adapts communication/channel behaviour | Frozen MVP is one local node with no cloud/network dependency; the record’s current enforceability and relevant claim mapping were not fully resolved | Keep peripheral to the frozen build; recheck if networking/adaptation is added. **Low present, unresolved future risk.** |
| MHI US 11,334,414 B2 family | Reference/normal unit space and Mahalanobis abnormality from vibration amplitude and phase | Frozen target classifier may use ordinary multivariate features without the claimed complex amplitude/phase conversion and specified unit-space structure | Preserve exact implementation, then obtain US/JP/CN/DE claim charts. **Medium risk if phase/complex normal-space steps are added; otherwise unresolved.** |
| Ford US 11,893,004 B2 family | Moving mean/inverse covariance and squared Mahalanobis anomaly exclusion | Claims are situated in vehicle-operation sensing and include a defined moving-statistics/exclusion sequence; machine-monitoring context alone does not prove avoidance | Compare actual rolling update/exclusion code to all live claims and family members. **Low-to-medium US/DE/CN uncertainty.** |
| Valqua US 12,590,863 B2 family | Multiple frequency-band intensities, first Mahalanobis distance, spectral centre of gravity, second Mahalanobis distance and abnormality-time prediction | Frozen MVP does not require dual distances, centre-of-gravity sequence or prognosis; later feature additions could increase overlap | Do not add those sequences casually; chart US/JP/CN/TW/KR rights. **Low present to medium if expanded.** |
| Rolls-Royce/OSyS US 9,874,472 / EP family | Vibration amplitude/noise-floor measures indexed by frequency and rotational speed | Frozen MVP has no required RPM-indexed training; direction 7 would approach this subject | Claim chart before speed-indexed/order implementation in covered markets. **Medium enhancement risk.** |
| Tractian US 11,429,900 B1 | FFT/peak information, cross-machine model, human confirmation/retraining and generated maintenance actions | Frozen system lacks the claimed first/second-device workflow, fleet model, human confirmation loop and scheduled instructions. “Uses Mahalanobis” is not the claim | Recheck if cloud/fleet/human feedback is ever added. **Low present conceptual overlap; no clearance conclusion.** |
| Augury US 10,983,097 and US 12,607,995 families | Multi-machine models and, in the later separate family, fusion of two non-stationary sensors/feature tracking | Frozen MVP is single local node, no fleet/cloud model and no two-sensor fusion | Recheck continuations and jurisdictions before major redesign. **Low present, unresolved portfolio risk.** |
| US 7,421,349 B1 | Source-related bearing-frequency/sideband analysis in coupled systems | Expired/term-ended US right is not a present US FTO blocker; it remains strong prior art. Frozen ADXL345 work does not implement its bearing model as established | Use for prior-art/obviousness, not an infringement warning. **No identified current US blocking right; foreign/current family issue not established.** |
| Infinite Uptime WO 2017/151447 / US 2019/0061086 | Magnetic vibration/acoustic machine-tool housing | Frozen rigid ADXL345 node is not shown to use the claimed housing/sensor arrangement; cited US record is abandoned and PCT ceased | Prior-art/design context only unless a live national right is found. **Low verified present risk; IN/CN unresolved.** |
| Senseye/Siemens and broader industrial portfolios | Later portfolios may contain relevant adaptive monitoring, edge, mounting or fleet claims even where no Senseye-named family was verified | Company-name searching is incomplete and product functionality is not claim scope | Run assignee/inventor/CPC/continuation search at code freeze. **Unresolved.** |

No-cloud operation, low price and use in education are not FTO safe harbours. Conversely, an active patent with similar words is not an infringement finding. Before commercial build/use, counsel should search the intended countries as of that date, verify fee/term/claim status, map each final code/hardware element to each live independent claim, and consider experimental-use rules rather than assuming them.

## 18. Claim-to-experiment map

Only direction 10 survives, so the map below treats its sub-elements as prospective technical elements rather than separate inventions.

| Prospective element | Nearest verified art | Proposed system and measurable effect | Baseline/ablation; independent variable | Success and failure evidence |
|---|---|---|---|---|
| Independently labelled target/interferer commissioning | Rolls-Royce state/speed signatures; Seitz labelled motors | Factorial source-state fingerprint intended to reduce wrong-source decisions | Pooled/unlabelled target normal model; remove interferer labels. Vary target state and interferer state independently | Success: held-out attribution improvement not explained by extra training volume. Failure: pooled baseline is equivalent or labels cannot be acquired safely/reliably |
| Separate target-abnormality and interference-ambiguity evidence | Nguyen source separation; standard anomaly/reject methods; Tractian multi-machine decision context | Two evidentiary axes intended to distinguish target departure from source ambiguity | One scalar RMS/Mahalanobis/FFT score; remove ambiguity path. Vary interference level/type | Success: lower wrong-source alarm at useful fixed coverage. Failure: ambiguity score is uncalibrated or merely tracks signal amplitude |
| Confidence-gated abstention | General reject-option practice | Refuse unsupported causal labels, reducing attribution error while reporting coverage and delay | Forced binary classifier; sweep the gate only on validation data, then freeze | Success: preregistered paired improvement at owner-approved minimum coverage. Failure: apparent gain arises from abstaining on most difficult or most samples |
| Contamination-protected target/interference updates | KCF controlled rebaseline; MHI/Ford reference-normal models | Admit updates only under state/confidence/mount validity; reduce fault ingestion and recovery errors | Frozen baseline, unconditional update, threshold-only update; seed faults/abrupt neighbour changes during update | Success: model remains sensitive to seeded target faults and recovers from admissible drift. Failure: fault becomes normal, rollback fails or fixed model matches performance |
| Remount transfer or invalidation | ISO 13373 mounting practice and mounting-effect literature | Preserve calibrated diagnostic meaning or reliably require recalibration after a changed mount | No correction, vector normalisation, full recalibration; independently remount sensor | Success: transfer improves held-out repeatability/fault separation without masking faults, or invalidation reliably blocks use. Failure: silent confident errors after remount |
| Resource-bounded local loop | KCF constrained processing; ESP-DSP FFT support | Same attribution effect within measured ODR/band, RAM/flash, worst-case latency and energy envelope | Continuous FFT, frozen triggered FFT, off-device reference implementation; vary window/hop/model size | Success: worst-case processing completes within each owner-approved hop/deadline without overflow and preserves effect. Failure: missed samples, aliasing, unstable heap or off-device computation is necessary |

### Shared confirmatory protocol

- **Independent variables:** target normal/imbalance (looseness secondary); interferer off/normal/abnormal; target and interferer speed/load; update allowed/blocked; mount/remount condition; session/day; algorithm/ablation.
- **Controlled variables:** sensor identity, declared mount geometry/torque or fixture, acquisition settings, supply, target/interferer separation, base/coupling, fault mass/location, window/hop, train/validation/test partition and software version. Randomise condition order where safe and blind final labels to the analyst.
- **Equipment:** frozen node and damped target rig; independently controlled neighbour motor/fan; safe eccentric masses/guards; state/speed/load reference or command logs used as experimental ground truth; power/timing measurement; repeatable mounting fixture. References are test equipment, not a multi-sensor product.
- **Recommended sample/session plan requiring owner approval:** use a short pilot only to estimate variance; then freeze a power/precision-based confirmatory count. As a minimum feasibility design, use at least five independent sessions/remounts per planned condition across at least three days, with multiple non-overlapping windows nested within—not miscounted as independent trials. Field counts require a separate power plan.
- **Proposed preregistration rule requiring owner approval:** direction 10 succeeds only if the paired 95% confidence interval shows lower target-attribution error than the strongest mandatory baseline and each critical ablation, while owner-approved false-alarm, missed-detection, minimum coverage, delay and resource limits are all met on untouched sessions. Absolute limits are deliberately not invented here; they must be approved and frozen before confirmatory testing.
- **Bench relevance:** Level 1 validates acquisition/classification only. The dual-motor rig can falsify the mechanism and supply preliminary Level 2A evidence.
- **Field requirement:** at least one independently labelled dense-machine deployment with unseen operating and remount conditions is required before treating the direction as credible patent-supporting evidence; broader generalisation will require more than one installation.
- **Delivery split:** rig, baselines, preliminary dual-motor protocol and embedded profiling can fit three months; powered confirmatory field work, remount transfer and claim-grade evidence are later.
- **Confidentiality:** commissioning sequences, fingerprint representations, ambiguity/update gates, transfer rules, code, parameter values, raw labelled data and ablation results are confidential project material pending institutional IPR review.

## 19. Three-month semester plan

The semester objective is a rigorous Level-1 prototype plus a falsifiable Level-2A scaffold. It is not a promise to establish a patent within twelve weeks.

| Time | Semester MVP work | Bounded research work and decision gate |
|---|---|---|
| Weeks 1–2 | Freeze the one-page test specification; assign safety responsibility; buy/inspect the frozen ADXL345, ESP32 and guarded motor/fan rig; document mount geometry; verify SPI integrity, actual ODR, time stamps, dropped samples, DC removal and alias/noise behaviour | Define the dual-motor factorial conditions, independent labels, data schema, confidentiality controls and baseline list. Owner approves proposed metrics, pilot rules and experiment boundaries before data collection |
| Weeks 3–4 | Implement continuous RMS, peak, standard deviation, crest factor and kurtosis; RMS/persistence minimum; Hann and triggered FFT; band features; RGB normal/abnormal/calibrating states; log raw and derived data | Establish a reproducible isolated normal-versus-eccentric-imbalance dataset with train/validation/test separation. Measure RAM, flash, stack/heap, window latency, trigger delay and power where practical |
| Weeks 5–6 | Implement and compare ordinary FFT features, fixed spectral subtraction and calibrated Mahalanobis against RMS/persistence; repeat isolated tests across sessions and safe remounts | Build the independently controlled neighbour rig if cost and safety permit. Pilot target/interferer state labels; do not call this field attribution |
| Weeks 7–8 | Harden acquisition, error handling, calibration persistence, versioning and data export; keep all inference local | Implement the direction-10 *research scaffold*: state-conditioned fingerprints, separate ambiguity score, frozen/guarded update modes and unknown logging. No final algorithm or numeric gate is presumed inventive |
| Weeks 9–10 | Run held-out Level-1 evaluation and correct leakage, mount or alias defects | Run balanced Level-2A pilot cells, fault-during-update contamination tests, abstention/coverage analysis and critical ablations. Stop the patent branch early if the mechanism fails a kill criterion |
| Weeks 11–12 | Freeze a reproducible demonstration; publish the engineering test report internally with BOM, code version, configuration, raw-data provenance, errors and compute profile | Conduct blinded held-out analysis where pilot data justify it; prepare the confidential evidence packet, prior-art update and institutional IPR decision memo. Do not publicly disclose the prospective mechanism or file a patent-first application solely to meet the semester date |

### Three-month deliverables

1. A safe, stable Level-1 VibeGuard node within the frozen architecture and budget.
2. A versioned dataset with independent run/session labels, mount records and untouched hold-out data.
3. Direct comparisons of RMS/persistence, ordinary FFT features, Mahalanobis and fixed spectral subtraction.
4. An embedded resource report covering ODR, usable band, missed samples, RAM/flash, execution/alert latency and power where material.
5. If the neighbour rig is feasible, a preliminary Level-2A dataset and direction-10 ablation result clearly labelled exploratory.
6. A go/stop memo applying section 22, not a patentability or FTO declaration.

## 20. Later-semester or publication extension

Direction 10 requires at least one additional research semester after the MVP. A reasonable planning range is **four to six additional months** for an initial authorised field study and **six to twelve months** for multi-installation, publication-quality replication; these are planning recommendations, not guaranteed durations.

| Required extension | Later requirement |
|---|---|
| Mechanism | Freeze an enabled form of the target/interference fingerprint, abnormality/ambiguity separation, update-admission state machine and remount transfer/invalidation after the bench ablations identify what actually works |
| Field access | Obtain written authorisation for a target machine with at least one relevant neighbour and safe access to multiple operating states; record installation, structural path and maintenance events |
| Ground truth | Independently log target and interferer on/off, normal/abnormal, speed/load and maintenance/fault state. A classifier’s own label is not truth |
| Validation burden | Repeated days, operators, mounts and operating regimes; untouched sessions; at least one replication installation if any general claim is contemplated; preregistered baselines, ablations, coverage and failure reporting |
| Remounting | Test transfer/invalidation across realistic reinstallation rather than only synthetic axis rotation; include full recalibration as an honest baseline |
| Sensor bandwidth | Continue with ADXL345 for low-frequency imbalance/misalignment/looseness. Add IIS3DWB only as a separately documented high-frequency bearing branch if the research question truly requires it; do not merge its results into the frozen-MVP evidence |
| Compute | Retest the final mechanism on the chosen ESP32 with worst-case models/windows and power conditions; an off-device result alone does not establish the edge technical effect |
| Cost | The semester electronics may remain within ₹5,000, but field fixtures, reference instrumentation, travel/site access, additional sensors for *ground truth*, publication and professional patent searching are outside that ceiling and require a separately approved budget. No credible total is presently available |
| Patent diligence | Update prior art to the actual mechanism; search claims and continuations in intended jurisdictions; resolve IN/CN/EP national status; obtain inventorship, ownership, eligibility and FTO advice before disclosure or filing |
| Publication opportunity | If patent evidence remains weak but the mechanism produces reproducible attribution/abstention/remount results, publish a transparent single-node mixed-vibration benchmark, negative results or embedded implementation study after IPR review |

This remains a connected VibeGuard extension because the permanent deployed architecture is still one target-mounted accelerometer, local ESP32 processing and a physical abnormal-condition alert. Cloud fleet analytics, multi-node triangulation, general remaining-life prediction or a replacement sensor array would be major redesigns and require a new project decision.

## 21. Budget, compute, and team feasibility

### Budget

The governing architecture’s consolidated estimate for the ADXL345 route is **₹1,700–₹2,200**, leaving approximately ₹800–₹1,300 within the preferred ₹3,000 target and ₹2,800–₹3,300 below the absolute ₹5,000 ceiling. Those are planning headrooms, not permission to change the architecture or buy unneeded equipment.

| Spend priority | Treatment |
|---|---|
| Frozen node, rigid mount, guarded target rig and basic wiring/power | First priority; preserve the verified ₹1,700–₹2,200 architecture envelope and actual receipts |
| Safer/repeatable fixtures, fasteners, eccentric masses, connectors and spares | Use preferred-budget headroom before adding analytical hardware; itemise and approve |
| Neighbour motor/fan for Level 2A | Bounded enhancement only if it fits after safety and frozen-MVP needs; an existing suitable rig is preferable |
| Reference tachometer/current/second sensor | May be borrowed or used only as test ground truth. It is not a silent change to the one-sensor deployed product; purchase requires owner approval |
| IIS3DWB | Excluded from the semester MVP. Consider only under the separately funded later bearing branch |
| Cloud subscription, GPU or second deployed node | Not required and not authorised by the frozen design |

Stop or rescope before exceeding ₹5,000. The later field/patent programme has no justified cost estimate and must not be hidden inside the semester budget.

### Compute and measurement feasibility

- The selected ESP32-WROOM-32 class is documented in the project architecture as a 240 MHz dual-core MCU with 520 KB SRAM; the ESP32-S3 option differs in memory/configuration, so the exact board must be recorded. Availability of [ESP-DSP](https://docs.espressif.com/projects/esp-dsp/en/latest/index.html) makes FFT/window execution plausible, but not proven for the final pipeline.
- No report-supplied execution time, RAM count, energy number or accuracy figure is accepted as fact. Measure raw buffers, FFT workspace, model tables, stack high-water mark, heap fragmentation, flash image, worst-case cycles/time, end-to-end alert delay and dropped samples on the actual firmware.
- Choose ODR and analogue/digital bandwidth from the demonstrated low-frequency fault content. At 3200 Hz ODR the ADXL345’s nominal 1600 Hz bandwidth requires at least 2 MHz SPI; useful bandwidth may be lower because of noise, mounting and anti-alias limitations. Do not call 1600 Hz the “Nyquist bandwidth.”
- Triggered FFT should reduce average compute, but it can miss short/weak events and add detection delay. Continuous FFT is a required comparator. Direction 10 must complete within the selected hop/deadline under the largest state model, or it fails the embedded-effect proposition.
- Average power is secondary on a mains-adjacent lab rig but still relevant to an edge/resource claim. Profile active sampling, time-only, continuous FFT and triggered/integrated modes rather than estimating from instruction counts alone.

### Five-person allocation

| Team capacity | Primary responsibility | Independence/control |
|---|---|---|
| Strong technical member 1 | Sensor/SPI firmware, timing, buffering, RGB and resource instrumentation | Cannot silently alter preprocessing after hold-out evaluation begins |
| Strong technical member 2 | Baselines, direction-10 research code, ablations and reproducible configuration | Does not see blinded final labels until outputs are frozen |
| Strong technical member 3 | Rig safety/control, ground-truth logging, data pipeline and statistical analysis | Maintains condition randomisation and label key |
| Learner | BOM/receipts, mount/session records, scripted test checklist, dataset integrity and supervised repeat runs | Uses fixed SOP; deviations logged rather than repaired after the fact |
| Presenter/support | Demonstration, diagrams, literature/source ledger, meeting minutes and confidential/public version control | Does not turn exploratory metrics into public claims |

The plan fits the team’s skills if scope remains Level 1 plus a preliminary Level 2A scaffold. It does not fit a full field campaign, professional multi-jurisdiction FTO search and publication-quality replication within the same three months.

## 22. Kill criteria

Apply these as stop or downgrade rules, not as post-hoc explanations:

1. **No attribution gain:** direction 10 does not reduce held-out wrong-source attribution relative to the strongest RMS/FFT/Mahalanobis/subtraction baseline and critical ablations.
2. **Abstention illusion:** error falls only because the system abstains below the owner-approved minimum useful coverage, or confidence is not calibrated on untouched sessions.
3. **Contamination failure:** a seeded target fault or neighbour-state change is admitted to the normal model, materially masking later faults; rollback/freeze cannot recover.
4. **No cooperative effect:** removing independent labels, the ambiguity gate, update guard or mount-validity control produces no material loss. The integrated story then collapses into known modules.
5. **Remount failure:** the system makes confident wrong decisions after realistic remounting, and neither validated transfer nor automatic invalidation works better than full recalibration.
6. **Operating-state confounding:** ordinary healthy speed/load variation causes target alarms or erases the fault effect, with no permitted single-node correction.
7. **Bench-only overfit:** gains disappear on blinded sessions/days or a second fixture/installation; overlapping windows are the only apparent sample size.
8. **Measurement failure:** ADXL345 noise, aliasing, saturation, mounting resonance or bandwidth prevents repeatable detection of the claimed low-frequency condition.
9. **Embedded failure:** the final mechanism overruns RAM/flash, drops samples, misses its owner-approved latency window or needs cloud/off-device analysis, a second deployed sensor or more than ₹5,000 for its core operation.
10. **Prior-art defeat:** a verified earlier claim/publication discloses the complete enabled mechanism, or a well-supported combination makes the result plainly predictable with no unexpected technical effect.
11. **Eligibility defeat:** the only remaining contribution is a mathematical score, classifier label or deployment instruction with no demonstrated improvement in physical machine-state measurement.
12. **FTO blocker:** counsel identifies an enforceable claim in an intended jurisdiction that reads on the necessary implementation and cannot be designed around or licensed within scope.
13. **Ground-truth/field failure:** independent target and interferer states cannot be obtained safely, ethically or with site permission. Without them, Track C cannot advance as an attribution patent programme.
14. **Confidentiality loss:** material public disclosure occurs before institutional review and destroys a required filing option in a relevant jurisdiction; assess promptly with counsel rather than assuming a grace period.

Any of criteria 1–4, 7, 10 or 13 is sufficient to stop the present patent direction while retaining the semester prototype. Criteria 8–9 may require an explicit architecture decision; they do not authorise an unlabelled redesign.

## 23. Confidentiality boundary

**Already public or conventional; safe to describe generically:** the problem of low-cost vibration monitoring; one ADXL345 and ESP32; local acquisition; DC removal, Hann window, common time features, FFT/bands, spectral comparison, threshold/persistence, Mahalanobis anomaly scoring, RGB indication, eccentric-mass rig and a generic statement that neighbour vibration is challenging. Public description should still avoid unsupported performance/patent claims.

**Confidential project material pending institutional IPR review:**

- the exact commissioning state sequence and source-label acquisition procedure;
- the representation and update rules for target-conditioned fingerprints and interference envelopes;
- how target-abnormality evidence and source-ambiguity evidence are constructed, calibrated and combined;
- abstention, rollback, contamination-blocking and mount-validity state-machine logic;
- remount transfer/invalidation tests, mappings and tolerances;
- parameter values, feature/band choices, window/hop and resource optimisations selected from experiments;
- firmware/source code, test automation, labelled mixed-source datasets, field-site details, raw data, negative results and ablation findings; and
- invention records, contributor chronology, notebooks and any draft claims.

Use access-controlled repositories and dated version history; record who conceived and experimentally reduced each element; apply institutional ownership, sponsor and site-confidentiality rules. Do not publish a paper, repository, demonstration video, poster, competition submission or detailed presentation of the prospective mechanism before institutional IPR review. This boundary preserves options; it is not a representation that the material is patentable or a trade secret.

## 24. Final VibeGuard recommendation

**Retain as strong semester prototype but reduce patent priority**

Proceed with the frozen Level-1 build because it is feasible, educational and capable of generating disciplined engineering evidence. Treat direction 10 only as a confidential Track-C research hypothesis, with the section-22 kills and independent field labels as mandatory gates. Do not file on the frozen feature aggregation or represent the planned bench rig as source-attribution proof. This report makes no cross-concept comparison and selects no final Project mC winner.

## 25. Unresolved questions

1. What exact ESP32 board, ADXL345 module provenance, mount geometry, ODR/range, anti-alias strategy, window/hop, feature set and update code will be built?
2. Which target and neighbour machines can be controlled independently, and what external command/reference supplies trustworthy normal/abnormal, speed and load labels without becoming product architecture?
3. What owner-approved false-alarm, miss, attribution-error, minimum-coverage, delay, remount and resource criteria will be frozen before confirmatory tests?
4. Can field access, repeated remounting and intentionally abnormal target states be obtained safely and with written permission?
5. Does a deeper claim/NPL search disclose the complete enabled direction-10 loop, particularly in remount/domain-transfer, selective baseline adaptation, reject/unknown decisions and single-sensor source attribution?
6. What are the current live-claim and national-register statuses for the identified Indian and Chinese family members, EP validations and all relevant continuations as of the eventual build/use date?
7. Do the final KCF, MHI, Ford, Valqua, Rolls-Royce, Tractian, Augury and later industrial-portfolio claim charts change with the actual firmware and intended countries?
8. Who conceived each prospective element, what institutional/sponsor/site ownership terms apply, and has any enabling public disclosure already occurred?
9. Does the proposed unknown/abstention state require a changed RGB user-interface convention, and will the owner approve it as a later enhancement while preserving the frozen MVP demonstration?
10. After pilot variance is known, what independent-session count is justified by a power/precision analysis? Windows from one run must not be treated as independent samples.
11. Can direction 10 show a causal technical effect that survives critical ablations, rather than an accuracy gain due only to more labels, model capacity or parameter search?
12. Is IIS3DWB genuinely required for a separately stated later bearing question, or would it merely expand scope without helping the low-frequency attribution mechanism?

## 26. Source and verification log

### Controlled input record

All 18 attached inputs were opened from the supplied scratch copies. Markdown files were read directly; both DOCX files passed ZIP-integrity checks, were text/table extracted and rendered page-by-page for visual inspection. SHA-256 values were recomputed for file control; all 17 externally controlled files matched `99_INPUT_MANIFEST.md`. The manifest was not cited as technical evidence. The Mistral compilation was logged as one incomplete lane and no missing conclusion was reconstructed.

| Source group | Files used | Evidentiary use |
|---|---|---|
| Governing specification | 00 | Required method, authority, scope, frozen architecture, terminology and 26-section output |
| Project authority | 01–06, in the specified order | Project identity, owner decisions, MVP architecture, budget/team constraints and process rules |
| Validated evidence | 07–09 | Current evidence/uncertainty baseline and search questions, subordinate to project authority |
| Historical leads | 10 | Search leads only; no Phase-2 patent conclusion treated as current truth |
| Independent research lanes | 11–16 | Leads and reasoning audited individually; unsupported assertions excluded rather than voted |
| File control | 99 | Count, names and hash verification only |

### Primary patent and status sources

All online records below were checked for this report with an evidence cutoff of **1 August 2026**. Google Patents links support readable claim text, bibliographic discovery and family navigation; official links were preferred for load-bearing status where accessible. Where an official national register was unavailable or incomplete, the report says unresolved.

| Record/source | What was verified or bounded |
|---|---|
| [USPTO Patent Center](https://patentcenter.uspto.gov/) and the application links in section 5 | US bibliographic/docket cross-checks for Navy, Tractian, KCF, Ford, MHI and Valqua leads; no blanket enforceability opinion |
| [US 7,421,349 B1](https://patents.google.com/patent/US7421349B1/en) | Bearing-model independent claim, phase-coupling dependants, coupled-source description, expiry/fee events |
| [NASA NTRS record for US 7,346,461](https://ntrs.nasa.gov/citations/20080020439) | NASA identity, grant and EMD/Hilbert-Huang technical subject; current docket status remains qualified |
| [Tractian US 11,429,900 B1](https://patents.google.com/patent/US11429900B1/en) and [official patent-marking page](https://tractian.com/en/patents) | Actual multi-device/human-feedback claim and separation of later Tractian patents from this family |
| [KCF US 10,873,791 B1](https://patents.google.com/patent/US10873791B1/en) and [KCF article identifying US 9,271,170](https://kcftech.com/resources/blog/machine-health-solutions/which-wireless-vibration-sensors-can-you-trust/) | Compression/FFT/baseline/rebaseline claims; identity of the channel-adaptation lead |
| [Ford US 11,893,004 B2](https://patents.google.com/patent/US11893004B2/en) | Weighted moving mean, inverse covariance, squared Mahalanobis and vehicle-operation limitations; family leads |
| [MHI US 11,334,414 B2](https://patents.google.com/patent/US11334414B2/en) | Complex amplitude/phase normal-unit-space Mahalanobis claims; JP/CN/DE family leads |
| [Valqua US 2023/0332979 / US 12,590,863](https://patents.google.com/patent/US20230332979A1/en) | Dual Mahalanobis, spectral-centre-of-gravity and prediction sequence; US 2026 grant and national-family leads |
| [Rolls-Royce/OSyS US 2012/0035885 / US 9,874,472](https://patents.google.com/patent/US20120035885A1/en) | Frequency/speed-indexed trained noise-floor claims and family navigation |
| [Augury US 10,983,097 family](https://patents.google.com/patent/US10983097B2/en) and [US 2024/0255942 / US 12,607,995](https://patents.google.com/patent/US20240255942A1/en) | Multi-machine diagnostic family; separate two-non-stationary-sensor family and 2026 grant; abandoned records distinguished per member |
| [Infinite Uptime WO 2017/151447 / US 2019/0061086](https://patents.google.com/patent/US20190061086A1/en) | Magnetic vibration/acoustic housing claims and ceased/abandoned records; no general IN/CN conclusion |

### Technical, standards and legal-framework sources

| Source | Use |
|---|---|
| [ISO 13373-1](https://www.iso.org/standard/21831.html), [ISO 13373-2](https://www.iso.org/standard/68128.html), [ISO 20816-1](https://www.iso.org/standard/89921.html), [ISO 20816-3](https://www.iso.org/standard/87746.html) | Measurement, processing and machine-vibration context; not VibeGuard acceptance thresholds |
| Nguyen, Rutten and Golinval, [Shock and Vibration (2012)](https://onlinelibrary.wiley.com/doi/10.3233/SAV-2012-0688); Seitz et al., [PHM Society European Conference chapter (2023)](https://link.springer.com/chapter/10.1007/978-3-031-27933-1_17); Atmaja et al., [lab dataset/baselines](https://scholar.its.ac.id/en/publications/lab-scale-vibration-analysis-dataset-and-baseline-methods-for-mac/) | Single-sensor source/state inference and clean-rig baseline context |
| [PCB mounting paper](https://www.pcb.com/Contentstore/MktgContent/WhitePapers/WPL_68_HowSensorMountingAffectsMeasurements.pdf) | Physical mounting effects on overall vibration and FFT |
| [ADXL345 data sheet](https://www.analog.com/media/en/technical-documentation/data-sheets/adxl345.pdf), [IIS3DWB data sheet](https://www.st.com/resource/en/datasheet/iis3dwb.pdf), [ESP-DSP documentation](https://docs.espressif.com/projects/esp-dsp/en/latest/index.html) | Sensor ODR/bandwidth/interface limits, later sensor boundary and embedded feasibility |
| [USPTO MPEP §2106](https://www.uspto.gov/web/offices/pac/mpep/s2106.html) and [August 2025 eligibility memorandum](https://www.uspto.gov/sites/default/files/documents/memo-101-20250804.pdf) | US subject-matter-eligibility framework |
| EPO 2026 Guidelines on [mathematical methods](https://www.epo.org/en/legal/guidelines-epc/2026/g_ii_3_3.html) and [computer programs](https://www.epo.org/en/legal/guidelines-epc/2026/g_ii_3_6.html) | European technical-purpose/technical-effect framework |
| India [Patents Act, 1970](https://ipindia.gov.in/writereaddata/Portal/IPOAct/1_31_1_patent-act-1970-11march2015.pdf), section 3(k), and [CRI Guidelines 2025](https://ipindia.gov.in/storage/uploads/docs-operator/62449276-74f6-438d-92fc-14b2cf3fa204.pdf) | India computer-related-invention exclusion and technical solution/effect framework |

### Verification classifications

- **Verified fact:** supported by the controlled project record or a cited primary/official source and stated no more broadly than that source.
- **Report assertion:** retained only as a search lead until independently checked; excluded where unsupported.
- **Inference:** expressly labelled, including term calculations and combination/obviousness reasoning.
- **Recommendation:** a proposed project action, experimental design or planning range; not current evidence.
- **Unresolved:** official status, claim scope, data or implementation detail was unavailable or insufficient and no conclusion was reconstructed.

This is technical research and project decision support, not legal advice, a patentability or validity opinion, claim construction, an infringement conclusion, or an FTO opinion.
