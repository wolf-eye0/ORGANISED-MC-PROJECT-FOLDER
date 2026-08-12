# Chapter 07 — VibeGuard Patent Evidence and Future Research Path

## Controlled VibeGuard source packet

This packet contains hash-verified source extracts. Sources have not been reconciled or converted into final manual conclusions.

Mapped sources: **9**


---

## Source 1: `03_CONCEPT_PORTFOLIO/VibeGuard/03_Patent_Synthesis/01_VibeGuard_Patent_Synthesis_Work_Max.md`

- Authority: `TIER_2`
- Treatment: `CORE_DECISION_EVIDENCE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `f61955b09b976a4c445fcdddbc40aada02cae204302876dbfc7cf1825b8cdf72`

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


---

## Source 2: `03_CONCEPT_PORTFOLIO/VibeGuard/03_Patent_Synthesis/02_VibeGuard_Patent_Synthesis_Standard_High.md`

- Authority: `TIER_2`
- Treatment: `CORE_DECISION_EVIDENCE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `b32a41ce9f0a3fe3ab17e55657bd14796cc77b401852b730254f1ac580b2adc4`

# Source Extraction

- Chapter: `07` — VibeGuard Patent Evidence and Future Research Path
- Authority tier: `TIER_2`
- Manual treatment: `CORE_DECISION_EVIDENCE`
- Original source: `03_CONCEPT_PORTFOLIO/VibeGuard/03_Patent_Synthesis/02_VibeGuard_Patent_Synthesis_Standard_High.md`
- Current SHA-256: `b32a41ce9f0a3fe3ab17e55657bd14796cc77b401852b730254f1ac580b2adc4`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

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


---

## Source 3: `03_CONCEPT_PORTFOLIO/VibeGuard/04_PreBuild_Simulation/VibeGuard_PreBuild_Future_Patent_Case_Simulation.md`

- Authority: `TIER_2`
- Treatment: `CONDITIONAL_EVIDENCE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `d57a571391e17021a91abba9932f1ecbc5ab6fb6f3e5abdf9221106d9451f4ca`

# Source Extraction

- Chapter: `07` — VibeGuard Patent Evidence and Future Research Path
- Authority tier: `TIER_2`
- Manual treatment: `CONDITIONAL_EVIDENCE`
- Original source: `03_CONCEPT_PORTFOLIO/VibeGuard/04_PreBuild_Simulation/VibeGuard_PreBuild_Future_Patent_Case_Simulation.md`
- Current SHA-256: `d57a571391e17021a91abba9932f1ecbc5ab6fb6f3e5abdf9221106d9451f4ca`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

# VibeGuard Pre-Build Future Patent-Case Simulation

**Research cut-off:** 3 August 2026
**Purpose:** pre-build, adversarial patent-case simulation—not a patentability opinion, freedom-to-operate opinion, valuation, filing recommendation, or promise of grant.
**Working constraint:** the hypothetical later mechanism is not assumed to work. Every technical benefit below is either an experiment target or a hypothesis until measured.

## Executive result

**[FACT]** The attachment gate passes. Exactly 12 files are present; every file is readable; every byte-level SHA-256 digest matches the governing manifest; and the 12 digests are distinct. Decision Register v1.2, the authoritative VibeGuard architecture/memory/SOP, both valid VibeGuard patent syntheses, and both final adjudications are present. The failed software-security concept-swap synthesis and separate OpenBraille or TrueMoist technical reports are absent. The manifest is used only for file control.

**[FACT]** The semester MVP remains the frozen conventional build: one rigidly mounted ADXL345-class sensor, ESP32-WROOM-32 or ESP32-S3, local acquisition and preprocessing, time-domain features, RMS plus persistence, triggered FFT/bands, prospective Mahalanobis scoring, RGB indication, USB, and an isolated motor/fan rig with normal and induced-abnormal operation. It does not expand to a permanent second sensor, cloud service, cancellation array, source-separation array, or remaining-useful-life prediction.

**[SOURCE ASSERTION]** The two attached VibeGuard syntheses converge on a future, label-aware attribution loop with abstention and contamination-protected updates, but they do not establish that such a loop is novel, non-obvious, enabled, or effective. The two adjudications point in different portfolio directions and are treated as decision context, not votes.

**[SIMULATION]** The currently described future concept is not mature enough for a responsible patent filing. Its principal components—single-sensor multi-machine classification, speed/load conditioning, residual anomaly models, Unknown/open-set outputs, mount-integrity detection, and guarded baseline updates—are all individually crowded. No single reviewed reference was found that expressly claims the exact paired-intervention contrast mechanism developed in this report, but the combination faces a high obviousness risk and a severe present enablement gap. This is a search result, not a novelty assurance; the search is not exhaustive.

**[HYPOTHESIS]** A narrower testable architecture may be worth preserving: during labelled commissioning, form one contrast subspace from paired measurements in which target state changes while interferer state is held fixed, and a second contrast subspace from paired measurements in which interferer state changes while target state is held normal. At runtime, one permanent target-mounted sensor supplies a deviation vector; two projection residuals and an anomaly gate produce Target-Abnormal only when the target contrast fits materially better than the interference contrast. Every ambiguous, out-of-support, or mount-invalid case becomes Unknown. A quarantined shadow-baseline mechanism is deferred unless separately proven.

**[UNCERTAINTY]** One sensor observes a mixture. Target and interference contrasts may be collinear, nonstationary, bandwidth-limited, or destroyed by remounting. The mechanism may therefore fail on the first proper factorial experiment. Nothing in this report assumes a positive result.

### Evidence labels

| Label | Meaning in this report |
|---|---|
| **[FACT]** | Directly verified file-control fact or frozen decision from the authoritative project record |
| **[SOURCE ASSERTION]** | A proposition stated by an attachment or primary external source; it is not automatically adopted as true |
| **[HYPOTHESIS]** | A technical proposition requiring experiment |
| **[SIMULATION]** | A prospective examiner, opponent, claim, litigation, cost, or decision scenario |
| **[RECOMMENDATION]** | A project action proposed after the simulation |
| **[UNCERTAINTY]** | A material unresolved fact, legal issue, measurement issue, or search limitation |

## 1. Attachment inventory and file-control gate

### 1.1 Byte-level inventory

**[FACT]** The upload directory contains exactly the following 12 regular files. “Manifest match” means the file's computed SHA-256 digest equals the canonical digest in 99_INPUT_MANIFEST(14).md. The parenthetical filename suffixes are transport naming only; the hashes establish the intended canonical contents.

| # | Attached filename | Bytes | Lines | SHA-256 | Manifest match |
|---:|---|---:|---:|---|---|
| 1 | 00_READ_FIRST_VibeGuard_PreBuild_Patent_Simulation_Instructions.md | 7,477 | 243 | 3d1abf8bf6ef471d447934858587f7a7d395c05d490b5bca8ac8242d77e56357 | Yes |
| 2 | 01_Engineering_Design_Review(19).md | 31,205 | 762 | 46f017501ac3ff9ebd6c1fb1e5ee8c068c22ddb08ae204c5609f2b759090295e | Yes |
| 3 | 02_Project_mC_Decision_Register_v1.2(20).md | 56,071 | 971 | 9678c5072d86ef38e48372f940ec91396b7ac7bcbeed0124ac8e2485307f408c | Yes |
| 4 | 03_Phase3C_VibeGuard_Architecture_Report_Final.md | 32,583 | 207 | ba7d1824fe1ab260be903aead8d9bac00cee83141b6f7728d0e220b65fd8eeb4 | Yes |
| 5 | 04_Phase3C_VibeGuard_Memory_Final.md | 9,527 | 113 | e4b96f7ee53bbc94ec960db281a1a56745fc6c8121133b813ca37b76798da5e5 | Yes |
| 6 | 05_Phase3C_VibeGuard_SOP_Final.md | 15,750 | 530 | 6386bf6d73bbbbb7127c568692ba09abcbdf6dc4cbac40a97690b4edb0dca974 | Yes |
| 7 | 06_Uncertainty_and_Test_Register.md | 22,484 | 263 | 125c057229524532b115391fbba948023684ad61d0153fb28ac29e6031e8ee3b | Yes |
| 8 | 07_VibeGuard_Patent_Synthesis_Work_Max.md | 111,826 | 633 | f61955b09b976a4c445fcdddbc40aada02cae204302876dbfc7cf1825b8cdf72 | Yes |
| 9 | 08_VibeGuard_Patent_Synthesis_Standard_High.md | 70,134 | 1,080 | b32a41ce9f0a3fe3ab17e55657bd14796cc77b401852b730254f1ac580b2adc4 | Yes |
| 10 | 09_Project_mC_Final_Adjudication_Max.md | 90,458 | 586 | 02baa83e691bf88e5221e20ac92e5be94eb3c71280b48c8338a02401bb173c9f | Yes |
| 11 | 10_Project_mC_Final_Adjudication_Deep_Research_High.md | 48,193 | 504 | 29d0f85d95f7ef98d1a1a31a395cbbab5511ae25df2eeb15840978d7bfb3590e | Yes |
| 12 | 99_INPUT_MANIFEST(14).md | 12,434 | 85 | 3e44c2dea5251d0be70cd6ad685db4a20967453439bf5a96a0511cdce44b0c47 | Yes |

**[FACT]** Aggregate: 12 files, 508,142 bytes, 5,977 lines, and 12 distinct SHA-256 digests.

### 1.2 Required confirmations

1. **Exactly 12 attachments are present — confirmed.** No thirteenth file was included in the controlled input directory.
2. **Decision Register v1.2 is present — confirmed.** Its content and canonical manifest digest match.
3. **The authoritative VibeGuard architecture, memory, and SOP are readable — confirmed.** All three opened as complete Markdown files and match the manifest.
4. **Both valid VibeGuard syntheses are present — confirmed.** The Work/Max and Standard/High syntheses are distinct, readable, and hash-matched.
5. **Both final adjudications are present and are decision context, not votes — confirmed.** They disagree in portfolio ordering; neither is counted as a vote or treated as technical proof.
6. **The failed software-security concept-swap synthesis is absent — confirmed.** Its excluded digest is not among the 12 computed digests, and no attached file contains that substitute synthesis.
7. **No OpenBraille or TrueMoist technical report is attached — confirmed.** Those concepts are necessarily mentioned in common governance/adjudication records, but there is no separate OpenBraille or TrueMoist technical, architecture, memory, SOP, uncertainty, or patent-synthesis report in the attachment set.
8. **The manifest is file control only — confirmed.** It establishes inclusion, exclusion, identity, and authority routing; it is not treated as technical evidence or patent analysis.
9. **No file is missing, duplicated, partial, superseded, or concept-swapped — confirmed.** Count, name, readability, size, full digest, distinctness, and internal title/version checks all pass. Decision Register v1.2 and “Final” VibeGuard records are the selected versions.

## 2. Governing record and simulation boundary

### 2.1 Authority applied

**[FACT]** Conflicts were resolved in this order: Engineering Design Review; Decision Register v1.2; final VibeGuard architecture; final VibeGuard memory; final VibeGuard SOP; uncertainty/test register; audited syntheses; final adjudications as context; then fresh research. Patent-source propositions can defeat a synthesis assumption but cannot rewrite the frozen semester MVP.

### 2.2 Frozen semester build

| Dimension | Frozen semester choice | Patent-simulation treatment |
|---|---|---|
| Sensor | One rigid ADXL345-class tri-axis accelerometer | Conventional platform; not asserted as the invention |
| Compute | ESP32-WROOM-32 or ESP32-S3, local | Constraint and implementation evidence; “on an ESP32” alone adds little inventiveness |
| Link | SPI sensor link; USB for bench interaction | Conventional |
| Signal chain | DC removal, Hann window where FFT is used, time features, RMS plus persistence, triggered FFT/bands | Baselines and future feature source; not expanded |
| Future score | Prospective Mahalanobis | Must be benchmarked against ordinary Mahalanobis; no presumption of novelty |
| Output | RGB local indication | Conventional physical output |
| Rig | Isolated 12 V motor/fan, normal and eccentric-mass induced abnormal | Level 1 teaching/verification apparatus, not dense-machine proof |
| Excluded | Cloud dependency, permanent second sensor, array/cancellation, RUL forecasting, industrial reliability promise | Remain excluded |

**[FACT]** Level 1 is normal versus induced abnormal on the isolated rig. Level 2 is target attribution when interference, remounting, and operating state change independently. A successful Level 1 detector does not establish Level 2 attribution.

### 2.3 Open project uncertainties carried forward

**[FACT]** The authoritative register leaves open: ADXL345 bandwidth adequacy; remount repeatability; spectral subtraction with an independently controlled interferer; dense-machine attribution; eccentric-mass repeatability; whether any later mechanism exceeds a conventional monitor; and owner approval of a quantitative bench gate. These are not silently resolved here.

## 3. Legal and evidentiary frame

**[SOURCE ASSERTION]** U.S. eligibility asks whether a claim is directed to a judicial exception and, if so, whether it integrates that exception into a practical application or adds significantly more. A generic computer instruction or field-of-use label is insufficient; a concrete improvement in a machine or technical process is more helpful. See [USPTO MPEP § 2106](https://www.uspto.gov/web/offices/pac/mpep/s2106.html).

**[SOURCE ASSERTION]** U.S. obviousness permits combining familiar elements according to known methods when the result would have been predictable, but the conclusion still needs an articulated reason with rational underpinning. See [MPEP § 2141](https://www.uspto.gov/web/offices/pac/mpep/s2141.html) and [MPEP § 2143](https://www.uspto.gov/web/offices/pac/mpep/s2143.html).

**[SOURCE ASSERTION]** Enablement is evaluated across the claim's full scope, including the quantity of experimentation, predictability, working examples, claim breadth, and state of the art. See [MPEP § 2164](https://www.uspto.gov/web/offices/pac/mpep/s2164.html). A specification that names desired outcomes without teaching a reproducible mechanism is vulnerable even if the idea sounds technically plausible.

**[SOURCE ASSERTION]** At the EPO, mathematical or machine-learning steps can contribute to inventive step when they serve a specific technical purpose and causally produce a technical effect. Generic purpose language or an unsupported assertion of the effect is insufficient; where an effect depends on training data, the disclosure must support the characteristics needed to reproduce it. See the [EPO AI/ML guideline](https://www.epo.org/en/legal/guidelines-epc/2026/g_ii_3_3_1.html), [mathematical-method guideline](https://www.epo.org/en/legal/guidelines-epc/2026/g_ii_3_3.html), [computer-program guideline](https://www.epo.org/en/legal/guidelines-epc/2026/g_ii_3_6.html), and [problem-solution approach](https://www.epo.org/en/legal/guidelines-epc/2026/g_vii_5.html).

**[SOURCE ASSERTION]** India's current Computer Related Inventions guidance treats substance rather than claim form as controlling under Section 3(k). Merely wrapping an algorithm in system hardware is not enough; the claim should disclose a technical solution implemented through technical means that produces a technical effect beyond an incidental effect. The same guidance states that novel hardware is not an absolute prerequisite, but technical character and support remain essential. See the [Indian Patent Office CRI Guidelines](https://ipindia.gov.in/storage/uploads/docs-operator/62449276-74f6-438d-92fc-14b2cf3fa204.pdf) and [Patent Office Manual](https://ipindia.gov.in/frontend/pdf/patents/Manual_for_Patent_Office_Practice_and_Procedure_.pdf).

**[SIMULATION]** “Patentability” and “freedom to operate” are different. Old, expired, abandoned, or geographically irrelevant documents can still defeat novelty or inventive step. Conversely, a feature can be patentable yet infringe a live, broader claim. This report performs neither a complete prior-art search nor a jurisdiction-by-jurisdiction live-rights clearance.

## 4. Fresh primary-source research

### 4.1 Claim-level patent landscape

Patent status labels below are search aids, not legal conclusions. Google Patents' “active” label is not a substitute for the USPTO, EPO, WIPO, or national-register record; continuations, term adjustment, terminal disclaimers, fees, ownership, opposition, and claim construction require counsel.

| Primary patent source | Earliest priority / claim-level relevance | Effect on this simulation |
|---|---|---|
| [KCF Technologies, US 10,873,791 B1](https://patents.google.com/patent/US10873791B1/en) | 29 Jul 2019. Claims sensor nodes, wireless infrastructure, baseline/subsequent vibration sets, differencing, compression/transmission/reconstruction; dependent claims include FFT magnitude/phase baseline subtraction and energy-triggered baseline reset. | Strong against broad baseline subtraction/reset. Its network/compression combination is narrower than the local-only future design, so avoiding it is not a clearance conclusion. |
| [Mitsubishi Heavy Industries, US 11,334,414 B2](https://patents.google.com/patent/US11334414B2/en) | Claims vibration amplitude and phase represented as complex values, Mahalanobis distance against a past-data unit space, thresholding, and methods of the same kind; description contemplates updating with normal data. | Directly weakens generic vibration-plus-Mahalanobis and normal-update claims. |
| [Rolls-Royce, US 2012/0035885 A1](https://patents.google.com/patent/US20120035885A1/en), later US 9,874,472 | Claims vibration amplitude plus rotation speed, frequency/speed subranges, per-bin noise floors, and noise/significant classification; normal training and continuous retraining appear in the disclosure. | Strong against speed-conditioned fingerprints, adaptive noise floors, and normal-only retraining. |
| [Valqua, US 12,590,863 B2](https://patents.google.com/patent/US12590863B2/en) | Japanese-priority attached accelerometer architecture; band intensities, a first Mahalanobis computation, spectral gravity center, a second Mahalanobis computation, abnormality-period handling, and maintenance actions. | Crowds band-feature plus multiple-Mahalanobis implementations and requires Asian-family review. |
| [Tractian, US 11,429,900 B1](https://patents.google.com/patent/US11429900B1/en) | Claims a first device computing FFT/peaks, transmission to a second device, reconstruction, ML trained on other machines, human confirmation, retraining, and instructed sampling. | Avoid remote reconstruction/fleet training/human-confirmed retraining unless cleared. It does not disclose the proposed paired contrast subspaces. |
| [Tractian patent marking page](https://tractian.com/en/patents) and [US 12,553,766 Gazette record](https://patentsgazette.uspto.gov/week07/OG/html/1543-3/US12553766-20260217.html) | The 2026 marking page lists numerous utility and design patents. US 12,553,766 claims baseline-profile instruction, AI failure identification, an optimized sampling profile for a spectrum region, and a repair response. | The field is still filing rapidly. Dynamic sampling, maintenance integration, housings, and mounting hardware require a refreshed claim chart immediately before any build-to-commercialize decision. |
| [Tractian, US 12,581,609 Gazette record](https://patentsgazette.uspto.gov/week11/OG/html/1544-3/US12581609-20260317.html) | Hardware-housing claims. | A software-mechanism redesign does not clear physical enclosure/mount claims. |
| [Oracle, US 12,332,111 B2](https://patents.google.com/patent/US12332111), continuation/family of US 11,740,122 | 20 Oct 2021 priority. Claims automatically choosing vibration frequencies that vary in correlation with load, time-series amplitudes, ML estimates of undegraded amplitudes, residual comparison, anomaly detection, and alerting; some claims accumulate residuals. Family records include EP, CN, and WO publications. | Material fresh-search delta. It weakens “load-conditioned bands plus learned normal residual” as a standalone invention. The redesigned core therefore uses predeclared features/cells and paired physical interventions, not automatic load-correlation frequency selection. |
| [Ford, US 11,893,004 B2](https://patents.google.com/patent/US11893004B2/en) | Vehicle sensor vectors, weighted mean, inverse covariance, squared Mahalanobis distance, anomaly detection, and vehicle operation excluding anomalous data. | Recency weighting plus Mahalanobis is crowded even outside machinery monitoring. |
| [Augury, US 9,835,594 B2](https://patents.google.com/patent/US9835594B2/en) and [US 2014/0114612 A1](https://patents.google.com/patent/US20140114612A1/en) | Portable vibration acquisition plus a remote relation learned from a group of machines and operating data; large international family includes an Indian publication. | Avoid assuming that “vibration plus fleet/model relation” is free in India or elsewhere. Current family status and claim scope need official-register verification. |
| [US 7,027,953 B2](https://patents.google.com/patent/US7027953B2/en) | Legacy machine diagnostics: unknown conditions may be labelled novelty until expert identification; adaptive learning and confidence concepts are disclosed. | “Unknown,” confidence, and later learning are old concepts. |
| [US 6,289,735 B1](https://patents.google.com/patent/US6289735B1/en) | One or more vibration sensors, local processing/FFT, harmonic scanning, and inference of resonance/machine state. | Strong background against generic one-sensor local spectral diagnosis; an expired right can still be prior art. |
| [US 2010/0169030 A1](https://patents.google.com/patent/US20100169030A1/en) | Recognizes that reassembly changes vibration level and uses adaptive thresholds derived from a baseline distribution. | Weakens generic remount-aware threshold adaptation. |
| [US 2005/0072239 A1](https://patents.google.com/patent/US20050072239A1/en) | Attached vibration sensor, local baselines/nominal values that vary with operating mode, stored frequency signatures, thresholds, trends, fuzzy logic, and neural approaches. | Establishes a broad early background for local operating-mode-conditioned monitoring. |
| [US 12,210,340 B2](https://patents.google.com/patent/US12210340B2/en) | A physical vibration probe plus a model-generated virtual second probe. | Avoid a virtual-sensor expansion without a separate claim chart. |

### 4.2 Primary technical sources

| Technical source | Demonstrated or discussed result | Patent-case consequence |
|---|---|---|
| [Seitz et al., 2023, “Single Sensor Multi-Machine Monitoring”](https://link.springer.com/chapter/10.1007/978-3-031-27933-1_17) | One vibration sensor is used to monitor the status of three motors with a one-dimensional convolutional network; frequency transformation improves classification. | Single-sensor multi-machine classification is not itself the inventive concept. A Seitz-like frequency-domain classifier is a required strong baseline. |
| [Gelle et al., 2001, rotating-machine blind source separation](https://www.sciencedirect.com/science/article/pii/S0022460X01938192) | Applies source-separation concepts to rotating machinery using multiple observations. | Separating machine sources is an established objective; the single-observation limitation must be confronted, not hidden. |
| [He et al., 2021, low-rank vibration-source separation](https://www.mdpi.com/2076-3417/11/11/5250) | Reviews denoising/source-separation limitations and uses low-rank constraints; source count and amplitude/phase uncertainty are material. | A single mixed measurement may be non-identifiable. A claim should not imply general separation unless the experiment supports a bounded condition. |
| [Nguyen et al., 2012, single-vibration-sensor subspace method](https://orbilu.uni.lu/handle/10993/2375) | Uses one vibration sensor, PCA/SOBI and block-Hankel subspaces, comparing reference and current subspaces, with industrial examples. | “One sensor plus subspace comparison” is known. Any surviving distinction must reside in the paired target/interferer intervention structure and decision rule, not “subspace” alone. |
| [Kannan, Dao & Li, 2024, one-class SVM for vibration signal-integrity issues](https://link.springer.com/article/10.1007/s42417-024-01435-8) | Detects saturation, distortion, sensor loosening, and detachment using features, PCA, and a one-class SVM trained on good-quality signals across conditions. | Mount-integrity detection is not a standalone invention. Default invalidation and recommissioning are safer than claiming unproven bounded transfer. |
| [Lundgren & Jung, open-set fault classification](https://www.sciencedirect.com/science/article/pii/S0967066121002732) and [author preprint](https://arxiv.org/abs/2009.04756) | Residual-based open-set fault classification using divergence measures addresses unknown and overlapping/ambiguous faults on an engine test bench. | Unknown/abstention and residual-based ambiguity handling are established concepts. |
| [Xu et al., 2025, open-set bearing diagnosis](https://www.mdpi.com/1424-8220/25/10/3019) | Explicitly recognizes unknown bearing-fault categories in an open-set setting. | “Unknown” is a safety feature and evaluation dimension, not a credible novelty anchor by itself. |
| [Analog Devices ADXL345 data sheet](https://www.analog.com/media/en/technical-documentation/data-sheets/adxl345.pdf) | Output data rates extend to 3,200 Hz; bandwidth is tied to output rate and reaches about half the ODR; selectable ranges reach ±16 g. | The frozen sensor can miss higher-frequency signatures. Patent evidence must disclose the tested band and cannot generalize beyond it without support. |
| [Espressif ESP32 data sheet](https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf) and [ESP32-S3 data sheet](https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf) | ESP32 has constrained on-chip SRAM; ESP32-S3 adds vector-oriented instructions useful for signal processing. | Edge feasibility is testable, but “run locally on ESP32” is primarily an implementation constraint, not an inventive concept. |

### 4.3 Research delta from the attachments

**[FACT]** The attached syntheses already identified KCF, Mitsubishi, Rolls-Royce, Valqua, Tractian, Ford, Augury, and older monitoring art. The fresh review read relevant claims rather than relying on titles or abstracts and added material technical and patent context.

**[SIMULATION]** The most consequential delta is the Oracle family: automatic selection of load-correlated vibration frequencies, learned undegraded amplitudes, residual anomaly detection, and alerts occupy a region that a broad VibeGuard “state-conditioned fingerprint” claim might otherwise enter. The Kannan mount-integrity paper, Seitz multi-machine paper, Nguyen single-sensor subspace work, and open-set sources further remove plausible standalone novelty anchors.

**[UNCERTAINTY]** Patent databases can lag, family mappings can change, translations can alter apparent scope, and the 2025–2026 claim landscape is active. The search did not include every dependent claim, prosecution history, non-English document, unpublished application, standards document, thesis, product manual, or national register. No negative search result is proof of novelty or clearance.

## 5. Future architecture funnel

The following six architectures are materially distinct mechanisms, not cosmetic claim variations. Every one preserves one permanently deployed target-mounted vibration sensor and local ESP32-class processing. Temporary sensors or machine-command logs may be used only to establish independent ground-truth labels during commissioning or a controlled service procedure; they are removed before ordinary monitoring.

### 5.1 Fixed labelled envelopes with selective abstention

**Physical problem.** A forced binary detector must label every deviation as target normal or target abnormal even when a changing nearby machine, an unseen speed/load state, or a remount could explain it.

**Exact mechanism and states.** Controlled commissioning records target-normal and seeded target-abnormal windows while an independent target label is available, plus target-normal windows over independently labelled interferer states. The feature extractor and class envelopes are then frozen. The state machine is Uncommissioned → Commissioned. In operation it emits Normal when the sample is inside the commissioned normal envelope, Target-Abnormal only when the sample lies inside a commissioned target-fault envelope with a predeclared margin, and Unknown otherwise. A mount-integrity failure or out-of-support operating condition sends it to Invalid; only recommissioning returns it to Commissioned. There is no runtime learning.

**Sensors.** Permanent: one rigid tri-axis ADXL345-class accelerometer and local ESP32. Temporary: a target reference, interferer reference, tachometer/current probe, or authenticated control-state record only long enough to label commissioning windows.

**Measurable technical effect.** The proposed effect is fewer false target attributions than a forced binary detector at a stated coverage and target-recall level. Coverage—the fraction not rejected as Unknown—must be reported with accuracy. An apparent precision increase obtained by rejecting nearly everything is not success.

**Closest art and patentability.** Seitz already demonstrates one-sensor multi-machine classification; Lundgren/Jung, Xu, and US 7,027,953 cover open-set/Unknown concepts. Augury, Tractian, Rolls-Royce, Mitsubishi, and early local-monitoring patents crowd the sensing and classification context. **[SIMULATION]** A broad claim to “commission labelled fingerprints and abstain when confidence is low” has low novelty strength and high obviousness risk. The only potentially distinguishing details would be unusually specific label interventions, envelopes, and state transitions, which would make the claim narrow and easy to design around.

**Eligibility.** In the United States, a generic confidence classifier plus alert is exposed under § 101; tying the decision to a particular vibration acquisition process and a concrete monitoring-state transition helps but does not cure obviousness. At the EPO, the physical-state decision can have a technical purpose, but the claimed envelope must causally achieve a reproducible monitoring effect. In India, a result-oriented classifier in conventional hardware is vulnerable under § 3(k); formulating it as a “system” does not solve that problem.

**Enablement, FTO, and design-around.** A fixed envelope is comparatively easy to implement, but the record lacks distributions across machines, remounts, state cells, and fault types. Live claims in the vibration-monitoring field still require a claim chart. A competitor can change the confidence metric, use conformal prediction, an ensemble, a reject class, or remote processing and avoid a narrow envelope claim.

**Scope, narrowness, cost, and MVP compatibility.** Plausible scope is limited to independently labelled commissioning, a frozen local model, explicit in-support testing, and a reject output. Compute and bill-of-material effects are low after commissioning. This is compatible with later work around the MVP but is not part of the frozen semester deliverable.

**Experiment, baselines, ablations, and kill.** Test randomized target/interferer states and held-out remounts against RMS plus persistence, FFT/bands, ordinary Mahalanobis, forced binary classification, and a Seitz-like frequency-domain classifier. Ablate the Unknown gate, each feature group, independent interferer labels, and the in-support gate. Kill the standalone patent route if it cannot reduce false target attribution at useful coverage or if the only benefit comes from indiscriminate abstention.

**Confidentiality.** Keep label schedules, envelope definitions, thresholds, raw factorial data, and negative results private until counsel decides whether any tested implementation supports a filing. This architecture is rejected as a standalone patent candidate but retained as a safety behavior.

### 5.2 Paired-intervention contrast subspaces and a residual attribution gate

**Physical problem.** A target-mounted sensor receives a mixed structural response. A simple anomaly score can detect change but cannot tell whether the target or an independently changing interferer caused it.

**Exact mechanism and states.** Commissioning deliberately creates two kinds of paired differences in the same predeclared operating cell:

1. a target contrast, obtained by changing target condition while holding the independently labelled interferer state fixed; and
2. an interference contrast, obtained by changing interferer state while holding the independently labelled target normal.

The system forms a low-dimensional target contrast subspace and an interference contrast subspace from those respective difference vectors. At runtime it computes a deviation from the commissioned target-normal reference, an anomaly score, the residual after projecting the deviation on the target subspace, and the residual after projecting it on the interference subspace. It emits Target-Abnormal only when the anomaly gate passes and the target projection fits by a predeclared margin; otherwise it emits Normal or Unknown. Uncommissioned, Mount-Invalid, and Out-of-Support states cannot emit Target-Abnormal.

**Sensors.** Permanent: one target-mounted ADXL345-class sensor and one local ESP32-class processor/memory. Temporary: independently attached target/interferer references or trustworthy command/tach/current records for paired commissioning labels only.

**Measurable technical effect.** The hypothesis is reduced false attribution to the target, at bounded recall loss and useful coverage, on an independently changing interferer not present in the evaluation fold. A second proposed effect is local execution within a fixed acquisition deadline. Neither is assumed.

**Closest art and patentability.** Nguyen uses one vibration sensor and subspace comparisons; Gelle and He address vibration-source separation; Seitz covers one-sensor multi-machine classification; Oracle claims load-correlated frequency choice and residual anomaly modeling; the remaining monitoring patents cover features, baselines, Mahalanobis scoring, and updates. **[SIMULATION]** No reviewed single reference expressly discloses both paired physical interventions—target changed/interferer fixed and interferer changed/target fixed—followed by two stored contrast subspaces and a local residual-margin attribution gate. That is only a provisional novelty observation. A KSR-style combination of experimental design, known subspace methods, and open-set classification remains a strong obviousness attack.

**Eligibility.** The U.S. case is stronger than for a generic classifier because the claim can recite how controlled physical interventions create machine-response structures and how a measured vibration is assigned to a machine condition. It remains at risk if drafted as mathematical projection plus reporting. At the EPO, deriving a physical source condition from vibration measurements is a plausible specific technical purpose, but the effect must be credibly achieved across the claimed scope. In India, the claim must show a supported technical solution through the sensor, interventions, stored physical-response structures, and local machine-state output; an algorithmic result dressed as apparatus remains vulnerable.

**Enablement, FTO, and design-around.** Enablement is currently poor: there is no working example, stable feature space, subspace rank, threshold, identifiability range, remount evidence, or multi-machine result. The active families listed above must be charted against any final embodiment. A competitor could use a nonlinear manifold, likelihood ratio, neural embedding, matched filters, multiple sensors, online source separation, or a different intervention schedule. A mathematically specific projector claim may be novel yet commercially narrow.

**Scope, narrowness, cost, and MVP compatibility.** A plausible claim is the exact paired-intervention data construction plus dual residual decision and abstention, not “single-sensor attribution” broadly. Commissioning cost is medium to high because the experiment needs independently controllable machines and temporary references. Runtime cost is low to medium and may fit an ESP32 after rank/precision measurements. The semester MVP supplies acquisition, preprocessing, rig discipline, and baselines, but does not implement or validate this future mechanism.

**Experiment, baselines, ablations, and kill.** Run the factorial dual-machine experiment in Section 8. Baselines include every mandated conventional baseline plus a one-sensor frequency-domain classifier. Ablate target pairing, interferer pairing, each subspace, the anomaly gate, the margin, Unknown, each feature group, state conditioning, and remount invalidation. Kill if target and interference contrasts remain too collinear for a stable held-out margin; if the best baseline is statistically indistinguishable; if benefit disappears on a new interferer level or remount; or if permanent reference sensing is required.

**Confidentiality.** Treat the precise intervention matrix, contrast construction, rank-selection rule, margin, and all results as the potential disclosure nucleus. This is the only architecture retained as a possible independent-claim core, subject to redesign and evidence.

### 5.3 Quarantined shadow baseline with promotion, rollback, and lockout

**Physical problem.** Naive adaptive monitoring can absorb a developing fault or interference shift into “normal,” silently destroying sensitivity.

**Exact mechanism and states.** A signed live baseline remains immutable while runtime samples enter a separate candidate buffer. Samples are barred from the buffer when the anomaly or ambiguity gate fires, the mount is invalid, or the state is outside commissioned support. A candidate batch is Eligible only after an independent target-normal label, valid mount, in-support state, and representation across at least two interferer states. It is then evaluated as a Shadow model against stored seeded-challenge and clean-reference windows. Passing a predeclared test permits atomic Promotion with a signed checkpoint; failure causes Discard and Lockout. A post-promotion challenge failure restores the previous checkpoint by Rollback. Candidate data never silently alters the live model.

**Sensors.** Permanent: the same one sensor and ESP32. Temporary or procedural evidence: an authenticated maintenance/commissioning normal label and, where needed, temporary target/interferer references. No permanent source reference is added.

**Measurable technical effect.** Lower rate of seeded-fault admission and lower degradation of target recall after environmental/interference drift than naive adaptive updating, without unacceptable false lockouts.

**Closest art and patentability.** KCF claims reset behavior; Rolls-Royce discusses normal-data retraining; Mitsubishi discusses normal updates; Tractian claims human confirmation/retraining in a remote architecture. Checkpoint, shadow, rollback, quarantine, and approval gates are familiar software-safety patterns. **[SIMULATION]** Baseline governance may be useful engineering, but the standalone novelty and inventive-step position is low. Its best role is a narrowly specified dependent mechanism attached to a technical attribution core.

**Eligibility.** U.S. claims framed as data governance or rules are exposed to abstraction. EPO and Indian cases require proof that the precise admission/rollback mechanism maintains a physical detection capability, not merely data quality. A signed checkpoint or ESP32 limitation does not itself supply inventiveness.

**Enablement, FTO, and design-around.** The state machine is implementable, but no evidence establishes how much drift, how many states, which challenge, or which statistical promotion rule preserves sensitivity. Claims in live monitoring/retraining families require review. A design-around can use dual models, Bayesian forgetting, immutable periodic recalibration, federated approval, or no online update.

**Scope, narrowness, cost, and MVP compatibility.** Plausible scope is the exact eligibility predicates, isolated candidate store, shadow challenge, atomic promotion, and rollback. That is narrow and easy to vary. Compute/storage cost is medium on ESP32 because two models and challenge windows must coexist; flash endurance and atomicity need engineering. It is beyond the semester MVP.

**Experiment, baselines, ablations, and kill.** Inject clean drift, interference drift, seeded faults, mislabeled normal data, mount changes, and power loss. Compare fixed baseline, static subtraction, naive adaptive update, periodic full recalibration, and candidate quarantine. Ablate every eligibility predicate, shadow evaluation, rollback, and lockout. Kill any patent path if protection comes only from requiring a human “normal” approval, if seeded faults are promoted at a materially nonzero rate, or if the edge device cannot retain an auditable rollback image.

**Confidentiality.** Keep promotion predicates, challenge sets, data-signing format, and failure traces confidential. This architecture is rejected as a standalone independent claim and deferred as an optional dependent feature until separately tested.

### 5.4 Mount-integrity validity gate with mandatory recommissioning

**Physical problem.** A loosened, shifted, or reattached accelerometer changes the transfer path. The detector may interpret a mount change as a machine fault or normalize away a real fault.

**Exact mechanism and states.** Commissioning stores a static orientation/gravity envelope and a predeclared run-state spectral checksum. At startup and scheduled intervals the system tests both. Passing yields Mount-Valid. A single discrepancy yields Mount-Suspect and Unknown output; a repeated or large discrepancy yields Mount-Invalid, locks baseline updates, and requires physical inspection plus full labelled recommissioning. The architecture deliberately makes no bounded-transfer claim. A future transfer map may be studied, but it cannot enter a claim until it survives multiple controlled remounts.

**Sensors.** Permanent: one ADXL345-class accelerometer and ESP32. Temporary: none at runtime; temporary reference sensors may validate a service recommissioning procedure.

**Measurable technical effect.** Sensitivity and specificity for mount change, plus prevention of false Target-Abnormal and baseline contamination after a mount event.

**Closest art and patentability.** Kannan, Dao, and Li expressly detect loosening and detachment with vibration features, PCA, and one-class SVM. US 2010/0169030 recognizes reassembly-dependent vibration and adapts thresholds. Hardware mounting and housings are separately patented in the field. **[SIMULATION]** Generic mount detection/invalidation is low-novelty and likely obvious. The precise dual check plus lockout/recommissioning may be a safety fallback, not a credible independent invention.

**Eligibility.** A physical mount-validity decision is a technical use in the U.S./EPO sense, but conventional sensing plus classification remains vulnerable on novelty/obviousness. In India, the physical transfer-path problem improves the § 3(k) narrative, yet the claim must teach a supported technical mechanism rather than an algorithmic checksum alone.

**Enablement, FTO, and design-around.** Gravity cannot detect every rotationally symmetric or translational remount, and a run-state checksum confounds machine changes with mount changes. The discrimination limits are unknown. Enclosure, magnet, adhesive, and mount patents need separate review. Competitors can use torque witnesses, keyed mounts, impedance checks, a dedicated contact sensor, self-test excitation, or mandatory manual recalibration.

**Scope, narrowness, cost, and MVP compatibility.** A narrow claim could require both orientation and controlled-run checks followed by update lockout and recommissioning. Runtime compute is low; controlled run-up and operator burden are medium. The semester rigid-mount protocol and remount-repeatability test create evidence but do not add this future state machine to the MVP.

**Experiment, baselines, ablations, and kill.** Randomize torque, angle, translation, adhesive layer, sensor replacement, genuine fault, and operating state. Compare full recalibration, gravity-only, spectrum-only, one-class mount classifier, and no gate. Ablate each check and the repeated-confirmation rule. Kill any transfer claim if new mounts cannot be distinguished from new machine states, and kill the standalone patent route unless a non-obvious physical test produces a reproducible effect beyond Kannan.

**Confidentiality.** Preserve mount geometry, torque, photos, fixture drawing, checksum definition, and all confused cases. This architecture is retained only as a dependent safety gate and a mandatory experimental control.

### 5.5 Speed/load operating-cell fingerprints

**Physical problem.** Normal vibration and fault signatures vary with speed and load, so one global threshold can cause false alarms or missed faults.

**Exact mechanism and states.** Commissioning partitions a predeclared speed/load domain into cells using temporary tach/current references or an already available machine-control value. Each cell stores normal and target-fault fingerprints and a support bound. Runtime selects a cell without automatically discovering load-correlated frequencies. Samples between cells, beyond a cell's support, or without a trustworthy state label become Unknown; no extrapolated target diagnosis is allowed.

**Sensors.** Permanent: one vibration sensor and ESP32; an existing controller state may be read if available but no new permanent sensing reference is assumed. Temporary: tachometer/current/load references for ground-truth commissioning.

**Measurable technical effect.** Lower false-alarm and miss rates across a declared operating envelope than a global model, with explicit rejection outside that envelope.

**Closest art and patentability.** Rolls-Royce claims speed/frequency subranges and noise floors. Oracle claims automatic load-correlated frequency selection, learned undegraded amplitude, residual anomaly, and alerting. Early local-monitoring art varies baselines with operating mode. **[SIMULATION]** This is the clearest elimination: broad operating-condition fingerprints are crowded, and narrowing to predeclared cells is an avoidance choice, not an inventive leap.

**Eligibility.** Physical speed/load conditioning gives a technical context in the United States and EPO, but eligibility cannot overcome anticipation/obviousness. In India, conventional state-binning plus algorithmic comparison is vulnerable under § 3(k) unless a distinct, supported technical mechanism exists; none is presently identified.

**Enablement, FTO, and design-around.** The number of cells, interpolation policy, state source, transient behavior, and data requirement are unknown. Oracle and Rolls-Royce claim charts are essential if this functionality is commercialized. A competitor can use continuous regression, order tracking, time-synchronous averaging, phase tracking, or a controller-native model.

**Scope, narrowness, cost, and MVP compatibility.** A defensible claim would be very narrow and likely easy to design around. Commissioning cost grows combinatorially with cells, interferer states, faults, and remounts; runtime compute remains modest. State sweeps may be future evidence, but the semester MVP stays at its approved normal/induced-abnormal rig scope.

**Experiment, baselines, ablations, and kill.** Compare global RMS/persistence, global FFT/bands, ordinary Mahalanobis, per-cell static fingerprints, continuous state regression, and full recalibration. Ablate state labels, cell boundaries, out-of-support rejection, and each feature. Kill the standalone patent route now; also kill technical use if cell data demands are impractical or held-out cells require unsafe interpolation.

**Confidentiality.** If explored as know-how, keep the cell map, state acquisition, and thresholds private. It is eliminated as an independent patent architecture and used only as a controlled experimental stratification.

### 5.6 Temporary-reference teacher with a single-sensor deployed student

**Physical problem.** Temporary references can distinguish target and interferer during commissioning, but the deployment must remain a one-sensor local product.

**Exact mechanism and states.** During commissioning, temporary target and interferer sensors or command references feed a multi-input “teacher” that assigns source-conditioned soft labels or embeddings. A compact student receives only the permanent target-sensor feature vector and is trained to reproduce the teacher's attribution and uncertainty. After an independent validation state, every temporary reference is removed. Runtime permits Normal or Target-Abnormal only inside the validated student support; teacher disagreement, low margin, mount invalidity, or state shift yields Unknown. The deployed student does not self-train.

**Sensors.** Permanent: one target sensor and ESP32. Temporary: at least one target reference and one interferer reference during commissioning; possibly a workstation for training. No cloud or extra sensor is required after commissioning.

**Measurable technical effect.** A compact local model approaches the temporary multi-reference attribution performance within a predeclared error/coverage bound after the references are removed.

**Closest art and patentability.** Seitz covers single-sensor multi-machine learning; Tractian covers distributed training/reconstruction contexts; Augury covers relations learned across machine data. Teacher/student compression is itself established in [Hinton, Vinyals & Dean, 2015](https://arxiv.org/abs/1503.02531). **[SIMULATION]** Applying known distillation to temporary vibration references is likely an obvious engineering route absent a highly specific and unexpectedly effective physical commissioning protocol.

**Eligibility.** A student network producing a condition label is exposed under U.S. § 101 and Indian § 3(k) if claimed functionally. The EPO would require the training/reference characteristics that cause a reproducible technical effect. The mechanism is less physically transparent than paired contrast subspaces and creates a larger disclosure burden.

**Enablement, FTO, and design-around.** Architecture, loss, reference placement, synchronization, coverage, quantization, and cross-remount generalization are all unknown. Relevant AI-monitoring claims and international families require searching. A competitor can train directly on hard labels, use privileged-information learning, feature selection, transfer learning, or retain multiple sensors.

**Scope, narrowness, cost, and MVP compatibility.** A broad claim is weak; a narrow synchronization/loss claim could be commercially brittle. Commissioning and data cost are high, edge inference cost is uncertain, and a workstation may be necessary. The frozen MVP can collect prerequisite data but should not be expanded into this program.

**Experiment, baselines, ablations, and kill.** Compare direct one-sensor supervised classification, the teacher, distilled student, classical paired contrasts, ordinary Mahalanobis, and frequency-domain CNN. Ablate each temporary reference, soft labels, uncertainty loss, quantization, and support rejection. Kill if the student does not beat direct supervised training on held-out interferer/remount splits, if it exceeds edge resources, or if it requires deployment references.

**Confidentiality.** Reference placement, synchronization, teacher outputs, training losses, and data remain confidential. This architecture is rejected as a standalone patent candidate because it is compute/data heavy, less explainable, and highly exposed to generic ML obviousness.

### 5.7 Funnel outcome

| Architecture | Independent-claim disposition | Engineering disposition | Principal reason |
|---|---|---|---|
| Fixed labelled envelopes + abstention | Reject | Retain safety behavior | Unknown/open-set classification is crowded |
| Paired-intervention contrast subspaces | Preserve only as redesigned test core | Test before any filing decision | Exact intervention structure was not found in one reviewed reference, but obviousness and enablement risks are high |
| Quarantined shadow baseline | Reject standalone; possible later dependent claim | Defer to separate contamination experiment | Adaptation governance is familiar and currently unproven |
| Mount-integrity validity gate | Reject standalone; possible dependent safety gate | Use as experimental control; default to recommission | Mount fault detection is known |
| Speed/load operating cells | Eliminate standalone | Use only to stratify experiments | Rolls-Royce, Oracle, and older art crowd the field |
| Temporary-reference teacher/student | Reject | Defer/stop unless classical method fails and resources justify it | Generic distillation plus one-sensor learning is obviousness-prone and costly |

**[SIMULATION]** The sole surviving patent-test nucleus is not the entire attached “integrated loop.” It is the narrower paired physical intervention and dual-residual attribution mechanism. Abstention and mount invalidation are safety conditions. Quarantined baseline promotion is a separable future experiment, not an assumed element.

## 6. Redesigned prospective mechanism

For concise reference, the surviving test architecture is called **Paired-Intervention Residual Gate with Quarantined Baseline (PIRG-QB)**. The “QB” portion is an optional later extension; the first experiment tests PIRG with a frozen baseline.

### 6.1 Physical topology

**Permanent deployed hardware**

- exactly one rigidly mounted tri-axis ADXL345-class accelerometer on the monitored target;
- one ESP32-WROOM-32 or ESP32-S3 performing acquisition, feature extraction, inference, state control, and local indication;
- local memory for the commissioned parameters, version identifiers, thresholds, and audit events;
- no permanent target reference, interferer reference, sensor array, cancellation channel, cloud inference, or fleet model.

**Temporary commissioning evidence**

- a reference accelerometer or other independent state reference on the target;
- a reference accelerometer, controller command, tachometer, or current probe for each deliberately manipulated interferer;
- a target speed/load reference where the experiment uses multiple operating cells;
- synchronized acquisition sufficient to label interventions independently of the permanent sensor output.

**[FACT]** Temporary references establish ground truth; they are not inputs during ordinary deployed inference.

### 6.2 Fixed feature and contrast construction

Let $x \in \mathbb{R}^d$ be a predeclared feature vector from the frozen acquisition chain. Candidate components are the semester time features and predeclared FFT-band energies. The bands are selected before evaluating the future mechanism; the core does not automatically search for frequencies correlated with load.

For a commissioned operating cell $c$:

- $\mu_c$ and $\Sigma_c$ describe independently labelled target-normal data;
- paired target contrasts are
  $\Delta^T_{i,j,c}=x(T_i,I_j,c)-x(T_0,I_j,c)$,
  where the target changes from labelled normal $T_0$ to seeded condition $T_i$ while interferer state $I_j$ is held fixed;
- paired interference contrasts are
  $\Delta^I_{j,k,c}=x(T_0,I_j,c)-x(T_0,I_k,c)$,
  where interferer state changes while the target is independently held normal;
- a predeclared rank-selection rule forms orthogonal projectors $P^T_c$ and $P^I_c$ from the two contrast collections.

For runtime feature vector $x$ in a valid, supported cell:

$$z=x-\mu_c$$

$$A=z^\top(\Sigma_c+\lambda I)^{-1}z$$

$$R_T=\lVert z-P^T_c z\rVert_2^2,\qquad
R_I=\lVert z-P^I_c z\rVert_2^2$$

$$M=R_I-R_T$$

Here $A$ is a conventional regularized Mahalanobis-style anomaly score; it is not asserted as the inventive step. If target contrast fits better, $R_T$ should be smaller and $M$ positive. The proposition that this geometry is stable is the central unproven hypothesis.

**[HYPOTHESIS]** Physically paired differences may suppress nuisance variation more effectively than unpaired class means, permitting a dual-residual margin to distinguish a target change from a changing interferer with one deployed sensor.

**[UNCERTAINTY]** If the mechanical transfer path makes $\Delta^T$ and $\Delta^I$ span the same directions, if labels are noisy, or if the system is nonlinear/nonstationary, the projectors will not identify a source. The mechanism then fails even if a generic anomaly detector succeeds.

### 6.3 Runtime state machine

| Current state / condition | Guard | Output | Next state / action |
|---|---|---|---|
| Uncommissioned | No complete signed parameter set | Unknown | Remain Uncommissioned |
| Commissioned, mount check fails once | Suspect-level mount discrepancy | Unknown | Mount-Suspect; lock all updates |
| Any, mount check fails decisively or repeatedly | Invalid mount | Unknown | Mount-Invalid; require inspection and full recommission |
| Commissioned, state outside trained support | Speed/load or feature-support gate fails | Unknown | Out-of-Support; no baseline admission |
| Valid and supported | $A \le \tau_A$ | Normal | Remain valid; baseline remains frozen in first experiment |
| Valid and supported | $A>\tau_A$, $M\ge\tau_M$, and $R_T\le\tau_T$ | Target-Abnormal | Latch/event-log according to persistence rule; no model update |
| Valid and supported | Anomalous but attribution guards do not all pass | Unknown | Log ambiguity; no model update |
| Optional later QB extension | Candidate meets every independent admission predicate | No immediate diagnostic change | Shadow-Evaluation |
| Shadow-Evaluation | Challenge and clean-reference gates pass | No immediate diagnostic change | Atomic Promote; retain rollback checkpoint |
| Shadow-Evaluation or post-promotion | Gate fails | Unknown if safety affected | Discard/Lockout or Rollback |

Thresholds, persistence, rank, regularization, support distance, and mount checks must be fixed using only training/validation runs. Test-fold tuning would invalidate the technical comparison.

### 6.4 What is and is not proposed as the inventive mechanism

| Included in the first mechanism test | Explicitly excluded or deferred |
|---|---|
| Two independently labelled types of paired physical intervention | Generic anomaly detection, RMS, FFT, bands, Mahalanobis, ESP32, RGB, or rigid mounting as inventions |
| Two contrast subspaces formed from those different intervention types | Automatic selection of load-correlated frequencies |
| Dual projection residuals plus a target-favoring margin | A general claim to blind source separation |
| Target-Abnormal only after anomaly, attribution, support, and mount-validity gates | Forced binary decisions |
| Unknown/abstention as a safety constraint | Proof that Unknown is novel |
| One permanent vibration sensor and local processing | Permanent source references, arrays, cancellation, cloud, fleet training, or RUL |
| Frozen baseline in the first evidence stage | Runtime adaptation, baseline promotion, and rollback until separately tested |
| Remount invalidation and recommissioning | Bounded remount transfer until separately demonstrated |

### 6.5 Cost, compute, and build compatibility

**[SIMULATION]** Permanent bill of materials should remain close to the semester architecture because no deployed sensor is added. The main cost is commissioning time, a second controllable machine, temporary references, synchronization, labelled seeded conditions, repeated remounts, and analysis.

**[UNCERTAINTY]** ESP32 feasibility depends on sample rate, FFT length/hop, feature dimension, projector ranks, numerical precision, and whether acquisition and inference share memory safely. The ESP32-S3 is the safer future compute candidate, but changing the semester controller solely for PIRG would expand the MVP and is not authorized.

**[FACT]** The semester build contributes a stable acquisition pipeline, a rigid-mount discipline, Level 1 induced-abnormal data, conventional baselines, and edge timing measurements. It does not claim or prove source attribution.

## 7. Pre-build experiment program

### 7.1 Earliest discriminating experiment

**[RECOMMENDATION]** The earliest experiment is a randomized two-machine factorial test, not further algorithm drafting.

**Rig**

- one target motor/fan and one independently controlled interferer coupled through a common plate or frame;
- the single permanent candidate sensor rigidly mounted on the target;
- temporary synchronized references on target and interferer for ground truth only;
- logged target/interferer commands, speed/load references, sensor identity, mount torque/geometry, temperature, day, operator, and firmware/data-format versions;
- no cancellation, no second deployed inference sensor, and no cloud.

**Minimum factors before a confirmatory design**

| Factor | Pilot levels | Reason |
|---|---|---|
| Target condition | independently verified normal plus at least three seeded-severity settings | Creates target contrasts and tests severity sensitivity |
| Interferer | off plus at least three independently controlled levels/conditions | Creates interference contrasts and a held-out interferer level |
| Target speed | at least three settings if controllable | Tests state dependence without automatic band search |
| Target load | at least two settings if safely controllable | Tests support and Oracle-adjacent conditioning risk |
| Mount | original plus at least four controlled remounts | Tests transfer-path fragility and leakage |
| Day | at least three nonconsecutive days | Exposes day/environment drift |

The pilot determines window independence, variance, safe seeded severities, and sample size. The confirmatory protocol must be preregistered after the pilot; raw windows from the same continuous run must never be split between training and test.

**Hold-outs**

1. a full interferer level or pattern unseen in model fitting;
2. at least one complete remount;
3. a full day/operator block;
4. where data permit, one speed/load cell;
5. one seeded target severity.

This makes generalization claims visible. Random window splits alone would let spectral leakage and repeated operating points masquerade as attribution.

### 7.2 Required baselines

All baselines receive the same raw input, feature budget where applicable, train/validation/test blocks, threshold-selection information, and edge timing protocol.

1. RMS plus persistence.
2. Predeclared FFT/band thresholds.
3. Ordinary Mahalanobis distance on the normal baseline.
4. Static spectral subtraction followed by the same detector.
5. Naive adaptive baseline update.
6. Full recalibration after every remount.
7. Forced binary version of the best classifier.
8. Every candidate with each feature group removed.
9. A Seitz-like one-sensor frequency-domain classifier as the strongest learning baseline, trained only on the permitted labels.
10. The best validated conventional method among items 1–9, selected without access to the final test blocks.

**[SIMULATION]** The “strongest baseline” for the decision is whichever predeclared competitor has the lowest held-out target false-attribution rate at the required target recall and coverage—not whichever baseline is easiest to beat.

### 7.3 PIRG ablations

| Ablation | Question answered |
|---|---|
| Remove paired target differences; use class means | Do physical pairings add anything? |
| Remove paired interference differences | Is explicit interference structure necessary? |
| Replace both subspaces with ordinary Mahalanobis | Is the claimed geometry better than the conventional score? |
| Remove $P^T$ or $P^I$ | Are both contrast models necessary? |
| Remove attribution margin $M$ | Does the relative residual decision matter? |
| Replace projectors with nearest-centroid or logistic classifier | Is the mathematical form special or interchangeable? |
| Remove Unknown; force binary | Does selective rejection produce the apparent gain, and at what coverage? |
| Remove mount gate | Is performance merely protected by detecting/removing remount cases? |
| Pool speed/load cells | Does state conditioning drive the result? |
| Remove each time feature and each band group | Which disclosed features are actually necessary? |
| Randomize target/interferer labels | Does the pipeline exploit leakage rather than physical interventions? |

### 7.4 Metrics and simulated owner gate

**[UNCERTAINTY]** The project uncertainty register requires owner approval of a quantitative gate. The following numbers are simulation parameters, not an authoritative project commitment.

**Proposed confirmatory gate**

- at least 80% diagnostic coverage after Unknown decisions;
- at least 30% relative reduction in target false-attribution rate versus the strongest baseline, with a cluster-aware 95% confidence interval whose lower bound remains above zero;
- no more than 5 percentage points absolute degradation in target-event recall;
- improvement persists separately on the held-out interferer level, remount, and day block;
- no target-seeded abnormal window is admitted to a baseline-candidate store in the separate QB test;
- no missed acquisition deadline, p95 processing time below 25% of the feature-window hop, and measured RAM/flash headroom on the selected ESP32 implementation.

Report false attribution per independent run and, where observation time is meaningful, per hour—not merely per highly overlapping window. Also report target recall, miss rate, precision, calibration, Unknown rate, selective risk-versus-coverage, latency, RAM, flash, mount detection sensitivity/specificity, and every excluded/corrupt run.

**Statistical discipline**

- freeze splits and thresholds before final testing;
- use run/day/mount as the resampling unit, not overlapping windows;
- provide uncertainty intervals and raw counts;
- retain all seeds and failed models;
- distinguish exploratory pilot results from confirmatory results;
- do not pool unseen-state failures into an “other” class that hides coverage loss.

### 7.5 Kill criteria

Stop the patent route for the proposed mechanism if any one of the following remains true after one properly debugged pilot and one preregistered confirmatory attempt:

1. target and interference contrast subspaces are not stably distinguishable across independent runs;
2. PIRG is statistically indistinguishable from the strongest baseline on held-out interferer/remount blocks;
3. an apparent gain disappears when data are split by run rather than window;
4. the gate requires an Unknown rate that makes coverage operationally useless;
5. a permanent target/interferer reference is needed for deployed performance;
6. the ADXL345 bandwidth or dynamic range omits the discriminating content;
7. remount changes cannot be detected and force unpredictable false attribution;
8. the mechanism only works at one contrived operating point or seeded fault;
9. the QB extension admits seeded faults, cannot rollback reliably, or needs hidden human judgement;
10. the edge implementation misses deadlines or cannot preserve an auditable parameter image.

**[FACT]** A killed patent route does not invalidate the semester MVP. It means the later Level 2 mechanism did not earn a patent case.

## 8. Draft future claim simulation

The following claims are deliberately provisional and incomplete. They are not filing-ready, are not legal advice, and should not be copied into an application without a working example, a professional search, inventorship analysis, and jurisdiction-specific drafting.

### 8.1 Illustrative independent apparatus claim

> A vibration-monitoring apparatus comprising:
> a single permanently deployed accelerometer configured for rigid attachment to a target machine and to generate a vibration signal containing responses of the target machine and at least one independently operable interfering machine;
> memory storing (i) a target-response structure derived from first paired commissioning measurements in which a labelled condition of the target machine differs while a labelled state of the interfering machine is held fixed, and (ii) an interference-response structure derived from second paired commissioning measurements in which the labelled state of the interfering machine differs while the target machine is independently labelled normal; and
> a local processor configured to form a feature deviation from the vibration signal, determine an anomaly measure, determine a first residual between the feature deviation and the target-response structure, determine a second residual between the feature deviation and the interference-response structure, and issue a target-abnormal output only when the anomaly measure passes an anomaly threshold and a comparison of the first and second residuals passes a target-attribution threshold, the processor otherwise issuing a normal output or an unknown output according to stored validity rules.

**Immediate weaknesses.** “Structure,” “held fixed,” “independently labelled,” and “validity rules” need objective definitions. The apparatus claim stores the result of commissioning rather than necessarily performing the interventions, making it easier for an examiner to characterize the mathematics as conventional model storage and comparison. Restricting the structure to exact orthogonal projectors improves definiteness but narrows commercial scope.

### 8.2 Illustrative independent method claim

> A method of commissioning and operating a vibration monitor, comprising:
> temporarily obtaining independent target-state and interferer-state references while a single deployment accelerometer is mounted to a target machine;
> acquiring first paired vibration measurements while changing a target condition and holding an interferer state fixed according to the references;
> acquiring second paired vibration measurements while changing the interferer state and holding the target independently normal according to the references;
> forming, from differences within the first and second paired measurements, respective target-contrast and interference-contrast subspaces;
> removing the temporary references from the deployed monitor;
> acquiring a subsequent vibration measurement with the single deployment accelerometer;
> computing an anomaly measure and respective projection residuals for the subsequent measurement relative to the target-contrast and interference-contrast subspaces; and
> locally outputting target-abnormal only when the anomaly measure and a target-favoring relationship between the projection residuals satisfy respective stored thresholds, and outputting unknown when the relationship is ambiguous, the mount is invalid, or the subsequent measurement is outside commissioned support.

**Immediate weaknesses.** The physical intervention sequence is clearer and likely narrower than the apparatus claim. A competitor that uses unpaired labelled data, nonlinear embeddings, likelihood ratios, multiple sensors, or a remote processor could avoid it. “Holding fixed” in a vibrating coupled system must mean a verified commanded state within tolerance, not a claim that the interference contribution is physically invariant.

### 8.3 Ordered fallback positions

| Fallback | Added limitation | Patent-case value | Commercial cost / design-around |
|---:|---|---|---|
| 1 | Exact difference vectors and orthogonal projectors with $R_T$, $R_I$, and $R_I-R_T$ | Improves definiteness and distinguishes generic classifiers | Very narrow; substitute distance/manifold avoids it |
| 2 | Predeclared feature vector and bands fixed before outcome testing | Distinguishes Oracle-style automatic load-correlated frequency choice and limits hindsight | Competitor can learn features or use raw waveform |
| 3 | At least two commissioned interferer states for each target contrast and at least two target-normal interferer contrasts | Strengthens physical factorial character | Commissioning burden rises |
| 4 | One permanent sensor; temporary references removed before monitoring; all inference local | Matches product constraint and separates remote/fleet claims | Product architecture limitation is easy to avoid |
| 5 | Mount-valid and in-support predicates prevent target-abnormal output and all updates | Supplies a safer technical state machine | Mount gating is known and may not add inventive weight |
| 6 | Remount always invalidates the attribution model and requires complete paired recommissioning | Honest to current evidence and definite | High service burden; no bounded-transfer advantage |
| 7 | Candidate data isolated from live baseline, independent target-normal admission, multi-interferer representation, shadow challenge, atomic promotion, signed rollback | May support a later dependent claim if contamination testing is positive | Crowded software-governance concepts; storage and validation cost |
| 8 | ADXL345-class acquisition within a disclosed ODR/bandwidth and an ESP32 timing budget | Supports a concrete embodiment | Risks unnecessary product lock-in; conventional parts add little patent weight |

### 8.4 Simulated examiner/opponent narrowing sequence

| Starting assertion | Likely attack | Responsible response |
|---|---|---|
| One sensor attributes target fault amid interference | Seitz/Nguyen/old monitoring art plus routine classification | Abandon that breadth |
| Labelled target and interferer fingerprints | Routine supervised commissioning; Augury/Tractian/Seitz context | Require the two reciprocal paired interventions |
| State-conditioned residual anomaly | Rolls-Royce plus Oracle | Exclude automatic load-correlated frequency selection; make state cells optional/dependent |
| Unknown output | Lundgren/Jung, Xu, US 7,027,953 | Treat Unknown as a safety limitation, not novelty anchor |
| Protected baseline update | KCF, Rolls-Royce, Mitsubishi, Tractian plus routine shadow/rollback practice | Remove from first independent claim; test separately |
| Remount detection/transfer | Kannan and reassembly art | Default to invalidation/recommissioning; do not claim transfer |
| Paired target/interferer contrasts plus dual projector residual | No exact single reference found in this review | Narrow to the physical pairing, exact construction, and test-supported scope; still expect a multi-reference obviousness rejection |
| Broad “technical effect” of source attribution | Unsupported result across machines/conditions | Limit to the tested topology, bands, interventions, operating envelope, and demonstrated metric—if any |

### 8.5 Claim-element-to-experiment map

Every element of the illustrative independent claims needs a future record. “Code exists” is not evidence that a claimed physical distinction works.

| Claim element | Required experiment or record | Failure consequence |
|---|---|---|
| One permanently deployed accelerometer on the target | BOM, serial number, mount drawing, photographs, wiring, acquisition logs, and explicit proof that temporary references are not inference inputs | Product topology not supported |
| Mixed response from target and independently operable interferer | Independently randomized commands and synchronized reference traces showing both sources affect the deployment sensor | Physical problem not established |
| Independently labelled target condition | Target reference/inspection protocol, seeded-condition definition, blinding where possible, and label audit | Paired target contrast is unreliable |
| Independently labelled interferer state | Interferer reference/command logs and synchronized label audit | Interference contrast is unreliable |
| Target changed while interferer held fixed | Paired runs with tolerance on interferer state and random order; repeat across at least two interferer states | Core intervention limitation unsupported |
| Interferer changed while target held normal | Paired runs with independent proof of target-normal state; repeat over days | Core intervention limitation unsupported |
| Feature vector and predeclared bands | Versioned specification created before final test, reference implementation, unit tests, and raw-to-feature checksums | Hindsight selection / reproducibility defect |
| Target and interference contrast structures | Full construction script, rank rule, singular values/principal angles, repeatability across resamples, and parameter hashes | Written-description and identifiability defect |
| Normal reference and anomaly measure | Ordinary Mahalanobis implementation and calibration curves on independent normal data | Anomaly gate unsupported |
| Two projection residuals and margin | Numeric test vectors, firmware/desktop parity tests, distribution plots by true source, and ablations | Alleged mechanism not actually implemented or causal |
| Target-Abnormal only if all guards pass | State-transition tests, boundary-value tests, forced fault/interference/remount sequences, and event logs | Claim logic unsupported |
| Normal and Unknown outputs | Risk-coverage curves, false-attribution counts, rejection reasons, and forced-binary comparison | Abstention benefit or utility unsupported |
| Mount-invalid guard | Controlled remount/loosening matrix, sensitivity/specificity, confused machine-fault cases | Safety limitation unsupported |
| Out-of-support guard | Held-out speed/load/interferer conditions and deterministic rejection tests | Scope/generalization defect |
| Local processor operation | ESP32 firmware, compiler/version, WCET-style timing measurements, missed-deadline counter, RAM/flash map, and fixed-point parity | Local technical embodiment unsupported |
| Temporary references removed | Deployment test with physical disconnection and logged absence of reference channels | One-sensor deployment claim unsupported |
| Optional quarantine/promotion/rollback | Separate contamination, mislabeled-normal, power-loss, checkpoint, and seeded-challenge campaign | Omit QB from claims and product promise |
| Claimed improvement over conventional monitoring | Locked comparison against strongest baseline on held-out run/remount/interferer blocks with confidence intervals | No evidence of the proposed technical effect |

## 9. Mandatory seven-way attack on the surviving candidate

### 9.1 Anticipation

**Attack.** A single earlier patent or paper may disclose each claim element, particularly in a dependent claim, translated family member, thesis, product manual, or unpublished-at-search application. Nguyen already supplies one-sensor subspace comparison; monitoring patents supply fixed baselines, features, and alerts; open-set art supplies Unknown.

**Present defense.** No single reviewed source was found that expressly combines reciprocal paired physical interventions, two corresponding contrast subspaces, and a target-favoring dual-residual gate with one deployed sensor. This is a limited search observation, not a novelty conclusion.

**Narrowing response.** Require both intervention directions, independently verified labels, difference-derived orthogonal projectors, the exact residual relationship, and removal of temporary references. If one reference later discloses that combination, the independent-claim case should be killed rather than relabelled.

**Assessment:** medium-to-high risk because the search is incomplete and the field is mature.

### 9.2 Obviousness / inventive step

**Attack.** An examiner can start with Nguyen or Seitz for one-sensor machinery discrimination, add routine designed experiments to label target/interferer changes, use known subspace projection/source-separation teachings from Nguyen/Gelle/He, and add open-set rejection from Lundgren/Jung. Oracle/Rolls-Royce supply state conditioning; Kannan supplies mount validity; KCF/Mitsubishi/Tractian supply baseline/update concepts. The motivation is explicit: reduce false alarms caused by other machines. The result—compare which learned source pattern fits better—may be predictable.

**Present defense.** The reciprocal intervention structure imposes a physical causal discipline absent from a generic classifier, and its dual residual compares two nuisance-aware response structures rather than merely classifying a spectrum. But that distinction does not establish non-obviousness.

**Narrowing response.** Claim only a tested construction that demonstrates a non-routine technical effect over the strongest combined baseline. Objective evidence would need a result attributable to the paired structure, supported by ablations and commensurate with claim scope. The simulation cannot invoke unexpected results before they exist.

**Assessment:** high risk and presently the dominant patentability problem.

### 9.3 U.S. subject-matter eligibility

**Attack.** The core can be characterized as collecting data, performing mathematical projection/distance calculations, classifying a condition, and reporting a result—an abstract idea implemented on generic sensor/computer hardware.

**Present defense.** The method recites specific physical commissioning interventions, a sensor attached to a machine, response structures tied to source-specific physical changes, and a constrained target-machine diagnostic output. Those facts support integration into a practical application under [MPEP § 2106](https://www.uspto.gov/web/offices/pac/mpep/s2106.html).

**Narrowing response.** Keep the intervention/acquisition sequence, physical mounting, local monitoring-state transition, and machine-specific residual mechanism in the claim. Do not rely on “apply it to vibration monitoring,” RGB display, or ESP32 naming as the inventive concept.

**Assessment:** moderate-to-high risk; stronger than a generic AI classifier, not assured.

### 9.4 EPO technical effect

**Attack.** Projectors, distances, thresholds, and training rules are mathematical. If the alleged source-attribution effect is merely stated, occurs only on a contrived rig, or depends on undisclosed labels/training characteristics, the distinguishing features may not contribute to inventive step.

**Present defense.** Determining which physical machine condition caused a measured vibration can be a specific technical purpose. The paired interventions define how physical training data relate to that purpose, consistent with the [EPO AI/ML](https://www.epo.org/en/legal/guidelines-epc/2026/g_ii_3_3_1.html) and [mathematical-method](https://www.epo.org/en/legal/guidelines-epc/2026/g_ii_3_3.html) guidance.

**Narrowing response.** Disclose the mechanical topology, acquisition band, intervention tolerances, feature/rank rules, operating envelope, rejection states, and reproducible comparison. Limit any effect to the conditions actually supported. A failed experiment cannot be cured by drafting.

**Assessment:** high until a reproducible technical effect exists; potentially moderate after bounded evidence.

### 9.5 India Section 3(k)

**Attack.** In substance, the claim is an algorithm for feature processing, subspace projection, and classification on known hardware, falling within “mathematical method,” “computer programme per se,” or “algorithms.”

**Present defense.** Current [Indian CRI guidance](https://ipindia.gov.in/storage/uploads/docs-operator/62449276-74f6-438d-92fc-14b2cf3fa204.pdf) does not make novel hardware an absolute condition and evaluates a technical solution, technical means, and technical effect. Reciprocal machine interventions, a physical vibration signal, and a local source-condition decision provide a possible technical-character argument.

**Narrowing response.** Draft the physical commissioning and monitoring process as the substance, disclose how the mechanism improves a physical measurement/diagnostic process, and avoid result-only functional language. Obtain Indian counsel's claim-specific view; do not infer allowability from U.S. or EPO analysis.

**Assessment:** high risk. Apparatus form alone is not a safe harbor.

### 9.6 Enablement and written description

**Attack.** The record has no functioning dual-machine embodiment, no evidence that one observation identifies two source changes, no defined feature set/rank/threshold, no remount or state generalization, no disclosed failure envelope, and no proof that the optional baseline gate resists contamination. Broad language covering many machines, faults, couplings, and operating states would require undue experimentation.

**Present defense.** There is an exact proposed construction and a concrete experiment plan, but a plan is not a working example.

**Narrowing response.** Do not file the broad concept now. If the mechanism works, disclose complete positive and negative examples, parameters, raw-data provenance, principal-angle/identifiability limits, firmware constraints, and the tested machine/coupling/band/state scope. Omit remount transfer, online learning, or fault types not supported. Satisfy the full-scope principles summarized in [MPEP § 2164](https://www.uspto.gov/web/offices/pac/mpep/s2164.html).

**Assessment:** severe present risk and an independent reason not to file now.

### 9.7 FTO and design-around

**Attack.** Commercial implementation can practice live claims even if the paired-contrast improvement is separately patentable. Active-looking families cover vibration/Mahalanobis combinations, baseline differencing/reset, state-conditioned residual models, remote reconstruction/retraining, fleet relations, dynamic sampling, maintenance integration, and housings/mounts. A competitor can also avoid a narrow PIRG claim by changing the mathematical representation.

**Present defense.** The core intentionally excludes KCF-style wireless compression/reconstruction, Oracle-style automatic load-correlated frequency selection plus learned undegraded amplitude, Valqua's claimed dual-Mahalanobis/gravity-center workflow, Tractian's remote reconstruction/fleet/human-retraining pattern, and Augury's remote group-machine relation. Exclusion reduces overlap but does not establish non-infringement.

**Narrowing response.** Before commercial design freeze, prepare limitation-by-limitation charts against live independent and relevant dependent claims in every target country; verify legal status in official registers; document non-infringing alternatives; separately clear the enclosure/mount. Maintain an alternative local fixed-baseline implementation.

**Assessment:** high and unresolved. Patentability testing must not be mistaken for product clearance.

## 10. FTO/design-around map

| Rights area | Feature to avoid pending counsel review | Deliberate present boundary | Residual uncertainty |
|---|---|---|---|
| KCF | Wireless node/server difference compression, reconstruction, FFT magnitude/phase baseline subtraction/reset combinations | Local raw acquisition and local features; no remote reconstruction | Dependent claims and family scope not fully charted |
| Mitsubishi | Vibration amplitude/phase as complex values with Mahalanobis unit-space thresholding and normal updates | No complex amplitude/phase unit-space claim; conventional Mahalanobis used only as baseline/anomaly gate | Doctrine of equivalents and non-U.S. family |
| Rolls-Royce | Speed/frequency subrange noise-floor classification and normal retraining | Predeclared features; no noise-floor invention or continuous retraining | Other family claims and operating-state implementation |
| Oracle | Automatic load-correlation frequency selection, ML undegraded amplitude estimates, residual comparison/accumulation, alert | No automatic load-correlated feature selection in the core; paired intervention structures instead | Continuation claims and EP/CN/WO scope |
| Valqua | Band intensities plus first Mahalanobis, spectral gravity center, second Mahalanobis, abnormality-period/maintenance chain | No gravity-center or claimed dual-Mahalanobis workflow | Asian-family status and translations |
| Tractian | Remote FFT/peak reconstruction, cross-machine training, human confirmation/retraining, instructed dynamic sampling, maintenance integration | One local node, frozen first-stage model, fixed sampling | Rapidly expanding 2025–2026 portfolio |
| Augury | Portable/remote relationship learned from groups of machines and operation data | Site-specific local model; no remote/fleet relation | Indian and other family status |
| Ford | Weighted covariance/Mahalanobis anomaly driving vehicle operation excluding data | Non-vehicle application; no claim to this general score as invention | Broad construction must still be reviewed |
| Mount/housing portfolios | Specific housing, fastening, magnetic/adhesive structures, self-test mechanics | Use off-the-shelf bench fixture during research | Commercial enclosure not designed or cleared |

**[UNCERTAINTY]** “Boundary” means a design instruction for the experiment, not a non-infringement opinion. Claims can read more broadly than their abstracts; means-plus-function, equivalents, divided infringement, method steps performed in commissioning, and induced infringement all require legal analysis.

**[SIMULATION]** The proposed core is easy to design around: replace linear projectors with a nonlinear embedding; use a likelihood ratio instead of residual margin; train on unpaired data; keep two sensors; move inference remotely; or infer source by control-system causality. Narrowness may improve prosecution but reduce exclusion value. That trade-off must be included in any commercial valuation.

## 11. Twelve-month evidence and decision roadmap

The roadmap is gated. A failed kill gate ends patent work on PIRG; it does not authorize a new mechanism by silent scope drift.

| Month | Work | Required output / gate |
|---:|---|---|
| 0–1 | Freeze semester records; write the exact PIRG mechanism specification; conduct counsel-aware claim search focused on paired interventions, contrast/subspace source attribution, commissioned temporary references, and new Tractian/Oracle families | Versioned mechanism, terminology table, search strings/results, initial claim charts, inventorship log, confidentiality list |
| 1–2 | Build dual-machine test fixture without changing the semester MVP; qualify temporary references and synchronization; run safe variance pilot; obtain owner approval for the confirmatory quantitative gate | Rig drawing/BOM, safety approval, label audit, pilot variance, preregistered confirmatory protocol |
| 2–4 | Collect randomized factorial data across target states, interferer states, days, speeds/loads, and remounts; preserve immutable raw data and failures | Complete raw corpus, hashes, exclusion log, intervention balance report |
| 4–5 | Fit only on allowed blocks; run all baselines and ablations; lock final test; assess principal angles/contrast identifiability and risk-coverage | Confirmatory report and an explicit kill/continue decision. No patent drafting if killed |
| 5–6 | If continued, implement the exact frozen feature/projector pipeline on ESP32; verify desktop/firmware numeric parity, timing, memory, persistence, and power-loss behavior | Edge feasibility dossier; claim scope limited to what is implemented |
| 6–8 | Separately test the quarantined shadow-baseline extension with clean drift, interference drift, fault contamination, wrong labels, power loss, promotion, lockout, and rollback | Independent QB gate. Exclude the feature from claims if it fails |
| 8–9 | Complete mount-validity/recommissioning study. Study bounded transfer only as a separately preregistered hypothesis | Default remains invalidation/full recommission unless transfer earns evidence |
| 9–10 | Under NDA, acquire one dense-machine or realistic coupled-frame dataset with independently observable target/interferer conditions | External-validity result; inability to access a valid field environment limits scope |
| 10–11 | Independent internal or third-party replication; refresh U.S./EPO/India and Asian-family searches; official-register status checks; counsel claim charts and inventorship review | Replication package, current legal-status table, scoped draft only if all gates survive |
| 11–12 | Choose filing, narrow trade-secret treatment, publication after clearance, or termination based on evidence, claim value, design-around ease, FTO, budget, and ownership | Written decision with costs, countries, disclosure timing, and residual risks |

**[RECOMMENDATION]** A separate Deep Research verification is required immediately before material patent spend or counsel's final opinion. It should refresh 2025–2026 grants/continuations, read prosecution histories of the closest independent claims, search CPC/IPC neighbors and non-English families, verify official legal status in intended countries, examine Oracle/Tractian/Augury/Valqua Asian coverage, search NPL for paired-intervention/subspace attribution, and update the claim chart against the mechanism actually tested.

## 12. Evidence preservation and confidentiality

### 12.1 Semester records to preserve now

Preservation does not expand the MVP. It creates contemporaneous proof of what was built, when, by whom, and with what result.

- repository commit/tag and source-tree hash for every demonstrated build;
- firmware binary, compiler/toolchain, dependency, board, and configuration hashes;
- BOM, purchase evidence, component/board serials, wiring schematic, PCB/fixture versions;
- dated photographs/video of sensor placement, mount, rig, eccentric mass, isolation, and operator setup;
- calibration/self-test records, sample-rate and timestamp validation, dropped-sample counters, FFT/reference-vector tests;
- immutable raw signals, metadata, experiment protocol, randomization seed, exclusion log, and SHA-256 manifest;
- feature/model generation code, exact environment, fitted parameters, thresholds, training/validation/test split identifiers;
- all baseline outputs, ablations, negative results, debug corrections, and the distinction between pilot and confirmatory data;
- signed operator logs, safety approvals, anomaly seed/severity definition, remount torque/geometry, environmental observations;
- Decision Register amendments and owner approval of the quantitative bench gate;
- names and dated contributions of every possible inventor, plus problem/solution sketches and meeting records;
- disclosure log covering demonstrations, posters, reports, repositories, emails, vendors, advisers, and field partners.

Do not rewrite old records to make a later mechanism appear earlier. Add dated amendments that preserve the original record.

### 12.2 Confidentiality before a filing decision

**[SOURCE ASSERTION]** The EPO generally applies absolute novelty, and public disclosure before filing can destroy novelty outside narrow exceptions; the EPO's [grace-period study](https://link.epo.org/web/the_european_patent_system_and_the_grace_period_study_en.pdf) explains the practical consequences. U.S. law has a limited one-year inventor-originated disclosure exception, summarized in [MPEP § 2153](https://www.uspto.gov/web/offices/pac/mpep/s2153.html), but attribution and foreign rights make it unsafe as a project strategy. [WIPO's patent-protection guidance](https://www.wipo.int/en/web/patents/protection) recommends confidentiality arrangements such as NDAs before prefiling disclosures.

**[RECOMMENDATION]**

- place future mechanism code, protocols, contrast definitions, raw data, and reports in access-controlled repositories;
- disclose on a need-to-know basis under appropriate NDAs and institutional IP rules;
- ask patent counsel before any thesis deposit, poster, public demo, paper, code release, vendor pitch, competition submission, or unrestricted field trial reveals the mechanism;
- demonstrate the frozen conventional MVP publicly only after checking that the demonstration does not disclose the future paired-intervention mechanism;
- do not rely on a U.S. grace period, and do not assume India or any other jurisdiction will rescue an earlier disclosure;
- if the patent route is killed but know-how remains valuable, make a conscious trade-secret/publication decision rather than drifting into accidental disclosure.

## 13. Decision package

### 13.1 Exact mechanism to carry forward

**[RECOMMENDATION]** Carry forward only this question: can reciprocal, independently labelled commissioning interventions create target and interference contrast subspaces whose two projection residuals permit one local target-mounted sensor to reduce false target attribution on held-out interference/remount blocks, while ambiguous cases abstain?

The initial baseline is frozen. Unknown, mount invalidity, and out-of-support states block a target-abnormal decision. Candidate quarantine/promotion/rollback is not part of the first mechanism test. Remount transfer is not claimed; a remount invalidates the model and requires recommissioning.

### 13.2 Semester choices

Keep the approved ADXL345-class sensor, rigid mount, ESP32-WROOM-32/S3 choice, SPI link, local preprocessing, time features, RMS plus persistence, triggered FFT/bands, prospective ordinary Mahalanobis baseline, RGB, USB, and isolated motor/fan Level 1 build. Add no permanent sensor, cloud, cancellation, array, RUL, or Level 2 promise to the semester scope.

### 13.3 Earliest experiment and strongest baseline

The earliest experiment is the randomized two-machine factorial rig with one permanent target sensor and temporary synchronized target/interferer references for labels. The strongest baseline is selected prospectively from all mandated conventional baselines plus a Seitz-like one-sensor frequency-domain classifier using identical blocked splits. Ordinary Mahalanobis and forced-binary variants remain mandatory even if another baseline wins.

### 13.4 Kill condition

Kill the patent route if paired contrast geometry is unstable or collinear, the mechanism does not beat the strongest baseline on held-out interferer/remount blocks at useful coverage and bounded recall loss, the effect depends on data leakage or a permanent reference, the ADXL345 misses the useful band, or edge execution fails. Kill optional QB claims if any seeded fault can enter the promoted baseline or rollback is not auditable.

### 13.5 Unknown before build

Unknowns include observability from one mixed signal; suitable feature dimension and projector rank; transfer-path linearity; bandwidth/dynamic-range adequacy; label tolerance; amount of commissioning data; performance on unseen interference, faults, state cells, machines, and remounts; Unknown coverage; mount-validity discrimination; ESP32 resource headroom; field access; inventorship/ownership; unpublished art; current family status; jurisdictional eligibility; claim value; and FTO. None is assumed favorable.

### 13.6 Verification and filing posture

Maintain confidentiality and contemporaneous evidence. Obtain owner approval for the quantitative gate. Run a separate Deep Research refresh and professional U.S./EPO/India claim/status/FTO review after the mechanism and evidence are fixed, not before the design is concrete and not after public disclosure. Even a positive experiment would not promise grant, validity, commercial value, or freedom to operate.

**B — Redesign the prospective mechanism before testing.**


---

## Source 4: `03_CONCEPT_PORTFOLIO/VibeGuard/02_Raw_Research/01_VibeGuard_Patent_Research_ChatGPT_Deep_Research.md`

- Authority: `TIER_3`
- Treatment: `SUPPORTING_EVIDENCE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `NEW_STAGE10I_EXTRACTION`
- SHA-256: `8614a18e8d7764437315a41b61ed46f4fb3e2dcd6eaa8b12e59a0b57ffdd79a7`

# Source Extraction

- Chapter: `07` — VibeGuard Patent Evidence and Future Research Path
- Authority tier: `TIER_3`
- Manual treatment: `SUPPORTING_EVIDENCE`
- Original source: `03_CONCEPT_PORTFOLIO/VibeGuard/02_Raw_Research/01_VibeGuard_Patent_Research_ChatGPT_Deep_Research.md`
- SHA-256: `8614a18e8d7764437315a41b61ed46f4fb3e2dcd6eaa8b12e59a0b57ffdd79a7`
- Extraction method: `PLAIN_TEXT`
- Rule: source text only; no synthesis, correction or reconciliation.

---

# VibeGuard Current Patent Verification — Independent Research

**Research cut-off:** 31 July 2026
**Prepared as:** an independent patent-and-technical research pass, not a synthesis of other models
**Scope disclaimer:** This is technical research and project decision support. It is not legal advice, a patentability guarantee, a validity opinion, claim construction, an infringement conclusion, or a freedom-to-operate opinion.

---

## Executive verdict

**Required verdict:** **credible long-term path requiring later-semester extension**
**Track:** **Track C**
**Confidence:** **Medium**
**Most important limitation:** The frozen semester MVP can prove normal-versus-deliberately-imbalanced classification on one isolated rig, but it cannot prove that one sensor attributes an abnormal condition to its mounted target machine when neighbouring machines or structural interference vary independently.
**Should the frozen MVP itself be treated as the invention?** **No.**

The frozen VibeGuard MVP—one rigidly mounted accelerometer, local sampling, DC removal, windowing, common time-domain features, triggered FFT, baseline thresholding, Mahalanobis-distance anomaly scoring, band-limited processing and a simple alert—is a technically coherent and affordable semester prototype. However, the reviewed patent and non-patent landscape shows that these elements, separately and in routine combinations, are longstanding condition-monitoring practice. Baseline acquisition, vibration fingerprints, statistical limits, FFT-derived features, operating-state normalization and automatic vibration diagnosis also appear in older and live patent families.

A credible connected patent-development route remains, but only if later work produces a **specific physical measurement method** that demonstrably improves one-sensor target-machine attribution or installation robustness. The strongest route is not generic “spectral subtraction.” It is a narrowly defined **confidence-gated target-fingerprint method** that: (1) calibrates the target under independently known target and interferer states; (2) models permitted speed/load and mounting variation; (3) refuses or abstains from a target-fault label when interference makes attribution unreliable; and (4) prevents contaminated data from entering the normal baseline. That contribution must outperform ordinary RMS, FFT features, fixed subtraction, and ordinary one-class/Mahalanobis baselines across independently controlled target/interferer states and remounting sessions.

No searched reference was verified as an exact anticipation of that full bounded sequence. That absence does **not** establish novelty or inventive step. Several close references occupy most of its building blocks, so obviousness risk remains high until a non-routine update, confidence, or deployment mechanism and its measurable technical effect are defined and tested.

---

## Input inventory and concept-fidelity confirmation

### Inventory result

The governing instruction file was readable. All ten canonical project inputs were attached and readable, although several uploaded filenames contain numbering prefixes and duplicate-name suffixes such as “(5)”. The content corresponds to the canonical documents specified by the governing file.

| Canonical input | Attached file | Result |
|---|---|---|
| Engineering_Design_Review.md | `01_Engineering_Design_Review(5).md` | Present/readable; filename decorated |
| Project_mC_Decision_Register_v1.2.md | `02_Project_mC_Decision_Register_v1.2(5).md` | **v1.2 present/readable; v1.1 not substituted** |
| Phase3C_Portfolio_Closure_Memo_Approved.md | `03_Phase3C_Portfolio_Closure_Memo_Approved(5).md` | Present/readable; filename decorated |
| Phase3C_VibeGuard_Architecture_Report_Final.md | `04_Phase3C_VibeGuard_Architecture_Report_Final.md` | Present/readable |
| Phase3C_VibeGuard_Memory_Final.md | `05_Phase3C_VibeGuard_Memory_Final.md` | Present/readable |
| Phase3C_VibeGuard_SOP_Final.md | `06_Phase3C_VibeGuard_SOP_Final.md` | Present/readable |
| 03_Concept_Evidence_Matrix.md | `07_Concept_Evidence_Matrix(5).md` | Present/readable; renamed and decorated |
| 05_Uncertainty_and_Test_Register.md | `08_Uncertainty_and_Test_Register(5).md` | Present/readable; renamed and decorated |
| 06_Patent_Research_Input_Pack.md | `09_Patent_Research_Input_Pack(5).md` | Present/readable; renamed and decorated |
| Phase2_Report by CLaude.md | `10_Phase2_Report_by_Claude(5).md` | Present/readable; punctuation/case normalized |

**Missing inputs:** none.
**Duplicate inputs:** no duplicate content was identified among the eleven attachments, which comprise one governing instruction file plus ten canonical inputs.
**Unreadable inputs:** none.
**Ambiguity:** only naming decoration; the contents and authority order resolve the identities.

### Frozen concept confirmation

The research treated VibeGuard as:

- passive detection and alerting;
- one rigidly mounted ADXL345 three-axis accelerometer;
- SPI acquisition into an ESP32-WROOM-32 or ESP32-S3-class MCU;
- local edge processing without cloud dependence;
- DC removal, Hann windowing, continuous low-cost features and triggered FFT;
- calibrated RMS/persistence as the minimum classifier;
- multivariate Mahalanobis anomaly detection as the primary target classifier;
- baseline spectral subtraction, proximity mounting and band-limited features as the baseline noise strategy;
- a motor/fan eccentric-mass bench demonstration for Level 1 evidence;
- possible later single-node target attribution under neighbouring-machine interference for Level 2 evidence.

It was **not** treated as active vibration cancellation, haptics, a wearable device, a multi-sensor array, an audio detector, a cloud predictive-maintenance platform, a remaining-useful-life system, or an industrial high-frequency bearing-fault detector using ADXL345.

---

## Search methodology and reproducible search log

### Method

The pass used keyword, assignee, inventor/family, classification and citation-chain searching. Google Patents was used for discovery, readable claims and family navigation. Important legal-status statements were limited to what could be corroborated from displayed prosecution/family data; Google’s status labels are treated as discovery evidence rather than a legal opinion. Official USPTO, EPO, IP India and ISO materials were used for eligibility and standards context.

The principal classes encountered were:

- **G01H** — measurement of mechanical vibrations or ultrasonic/sonic/infrasonic waves;
- **G01M 13/** — testing of machine parts and mechanical structures;
- **G05B 23/** — monitoring or diagnostic arrangements for control systems and machinery;
- **G06N / G06F** subclasses where statistical or learning-based anomaly analysis is claimed;
- condition-monitoring subclasses involving rotating machinery, operating-speed normalization and spectral analysis.

### Representative reproducible search log

| Source/date | Exact or materially equivalent query | Selection rationale |
|---|---|---|
| Google Patents / web, 31 Jul–1 Aug 2026 | `US 7421349 bearing fault signature detection` | Mandatory historical Navy lead |
| Google Patents / web | `single sensor machine vibration attribution patent` | Target-attribution search |
| Google Patents / web | `machine fault neighboring machine noise patent` | Interference/crosstalk search |
| Google Patents / web | `vibration spectral subtraction condition monitoring patent` | Frozen subtraction feature |
| Google Patents / web | `Mahalanobis vibration anomaly machine patent` | Multivariate baseline search |
| Google Patents / web | `baseline vibration features machine operating speed patent` | Baseline/fingerprint and state-normalization search |
| Google Patents / web | `mounting transfer vibration sensor calibration patent` | Mount/remount direction |
| Google Patents / web | `adaptive baseline contamination anomaly vibration patent` | Drift/update safeguard direction |
| Google Patents / web | `resource constrained triggered FFT vibration condition monitoring patent` | Two-stage compute direction |
| Google Patents / web | `Tractian vibration fault detection patent` | Mandatory named lead |
| Google Patents / web | `Infinite Uptime vibration monitoring patent` | Mandatory named lead |
| Google Patents / web | `Augury mechanical vibration patent` | Mandatory named lead |
| Google Patents / web | `KCF Technologies vibration sensor patent` | Mandatory named lead |
| Google Patents / web | `Senseye condition monitoring patent vibration` | Mandatory named lead; no equally close identifiable family found in this pass |
| Google Patents / web | assignee and citation-chain searches around SKF, GE, Siemens, Hitachi and industrial diagnostic patents | Major industrial landscape expansion |
| ISO official site | `ISO 20816 machine vibration` | Current measurement/evaluation standard context |
| USPTO official site | subject-matter eligibility, MPEP 2106 | US eligibility framework |
| EPO official site | CII technical effect guidelines | European eligibility/technical contribution framework |
| IP India official site | CRI Guidelines 2025 | Indian computer-related-invention framework |

Search limitations are recorded in the unresolved-questions section. In particular, this pass did not obtain counsel-grade INPADOC legal-event verification for every family or full official-file wrappers for every national member.

---

## Technical and patent landscape map

The landscape separates into six crowded layers:

1. **Physical vibration acquisition.** Contact-mounted accelerometers and wireless vibration sensors are mature. KCF’s family claims sensor-packaging and wireless-accelerometer structures, while many industrial families cover acquisition arrangements.
2. **Baseline/fingerprint comparison.** Older families compare current vibration with stored base features, operating-speed-indexed fingerprints or statistical norms.
3. **Spectral decomposition and fault features.** FFT, harmonics, order-related components, envelopes, sidebands, kurtosis and spectral peak selection are extensively disclosed.
4. **Automatic diagnosis and learning.** Augury, Tractian, Hitachi and others claim automated analysis using spectral relationships, learned models or condition classifiers.
5. **Operating-state normalization.** Live patents and older art normalize or select baselines by speed, load or other machine operating conditions.
6. **Source discrimination.** The Navy bearing-signature family distinguishes fault-related peaks from unrelated processes using phase relationships. Other source-separation methods are known in vibration and acoustics, although a verified exact one-sensor, target-mounted, neighbour-varying, abstaining method was not found.

The frozen MVP sits inside layers 1–5. A potential contribution must therefore be more specific than “single sensor,” “edge,” “no cloud,” “low cost,” “FFT,” “Mahalanobis” or “spectral subtraction.”

---

## Verified patent-family ledger

“Verified” below means that the publication, assignee/family relationship and relevant disclosed or claimed subject matter were checked in a patent record during this pass. Status remains a research indication, not a legal opinion.

| Family / record | Indicative status | Relevant independent-claim or disclosure focus | Relevance |
|---|---|---|---|
| **US 7,421,349**, *Bearing fault signature detection* (US Navy) | Granted 2008; old patent, expiration/status must be confirmed from official record | Bearing-fault peaks distinguished from coincident peaks of unrelated processes using phase-coupling relationships | Highly relevant prior art to “unrelated process” discrimination; not the same as the frozen subtraction approach |
| **US 7,133,801 B2**, *System and methodology for vibration analysis and condition monitoring* | Expired/fee-related indicated | Base vibration features, contact transducer, operating-speed estimate and comparison to detect faults | Strong novelty/obviousness art for baseline fingerprints and speed-aware comparison |
| **US 9,176,003 B2**, *Machine vibration monitoring* | Active indicated, expiry 2031 | Composite vibration separated into vectors associated with machine frequency and linked to operating conditions/statistical values | Relevant to vector/band analysis and operating-condition normalization; possible FTO concern only if every live-claim element is practiced |
| **US 8,290,630 B2 / EP 2,169,497**, condition-monitoring parameter normalization | US grant and EP publication | Calculate vibration parameters, normalize them and present alarms, including frequency-band scaling | Relevant to normalized vibration features and band alarms |
| **US 11,429,900 B1**, Tractian, automatic detection of error conditions | Granted 2022; assignment to Tractian Technologies recorded in 2026 | Machine-mounted sensor, transmission/compression/reconstruction and remote ML fault model | Commercially close but materially cloud/remote oriented; less direct to local-only MVP |
| **BR 102022005021 A2**, Tractian counterpart | Published | Same broad family subject | Confirms non-US filing activity |
| **US 9,835,594 B2 / US 10,983,097 B2 / EP 2,909,685 / IN2015DN04150A**, Augury automatic diagnosis family | US grants; EP/IN members identified | Vibration/acoustic data, spectral relationships/patterns and automatic mechanical-system diagnosis | Strong art against generic fingerprint-based automatic diagnosis; Indian member identified |
| **WO 2018/198111 / EP 3,615,899**, Augury monitoring machines | Published/pending or national status varies | Monitoring mechanical/electrical machines with sensor data and diagnostic processing | Broad industrial monitoring adjacency |
| **EP 3,877,819 B1**, Augury non-stationary machine performance | Granted January 2026, active indicated | Analysis of non-stationary machine performance | Relevant to variable operating-state normalization |
| **US 12,607,995 B2 / US 2024/0255942**, Augury continuation | Granted April 2026 | Automated analysis of non-stationary performance | Current live family to review before speed/load-normalized design freeze |
| **WO 2017/151447 / US 2019/0061086**, Infinite Uptime/UC, magnetic add-on system | Publication/application status varies | Magnetic add-on with vibration and acoustic sensing for tool condition monitoring | Relevant to mounting, multi-modal sensing and commercial SME node landscape; not a single-sensor attribution claim |
| **US 9,453,854 B2 / EP 2,913,643**, KCF vibration sensor | US grant with maintenance fees indicated; EP publication | Wireless accelerometer/vibration-sensor construction | Hardware/package FTO adjacency, not generic algorithm ownership |
| **KR 2015-0120160 A**, machine-tool abnormal-vibration determination | Published Korean application | Mahalanobis-Taguchi multivariate vibration factors and abnormal-vibration decision, with control response | Direct evidence that Mahalanobis-based vibration abnormality is not new |
| **US 11,333,580 B2** and **US 11,500,965 B2**, anomaly detection using Mahalanobis/MT | Active grants indicated | Mahalanobis normal-space anomaly detection and contribution/localization analysis | Broad evidence that ordinary Mahalanobis anomaly scoring is mature |
| **US 2021/0231528 A1**, separating periodic peaks from non-periodic peaks | Published | Kurtosis-driven separation of periodic candidate peaks in machine vibration spectra | Relevant to kurtosis and peak-selection approaches |
| **US 12,140,507 B2**, vibration detection/abnormality system | Granted 2024, active indicated | Detecting vibration of a target machine and determining abnormality | Recent broad target-machine vibration art requiring claim-level design review |
| **US 12,276,541 B2 / WO 2021/220162**, non-invasive vibration condition monitoring | US grant 2025 | Non-invasive condition monitoring family | Recent landscape evidence; full independent-claim mapping remains unresolved |

### Ledger conclusions

- No identified family grants exclusive ownership of “an accelerometer plus FFT plus Mahalanobis on an ESP32.”
- Multiple families disclose enough of that combination’s ingredients to create **high obviousness risk**.
- Live-claim FTO risk is more likely to arise from a specific diagnosis workflow, remote architecture, sensor package, operating-state relationship or source-discrimination technique than from using common statistical features themselves.

---

## Closest independent-claim analyses

### 1. US 7,421,349 — bearing fault signature detection

**Claim concept reviewed:** determine whether spectral peaks are generated by a bearing fault by examining phase coupling between peaks, thereby separating fault signatures from coincidental peaks caused by unrelated processes.

**Overlap with VibeGuard:** vibration spectrum; machine-fault monitoring; discrimination from unrelated vibration components.

**Differences:** the frozen MVP proposes baseline spectral subtraction, band limits and anomaly scoring, not phase-coupling/bispectral identification. It also does not initially diagnose a bearing fault.

**Effect:** strong novelty and obviousness art against a broad claim to “one sensor distinguishing a machine fault from neighbouring noise.” It is not a verified literal read on the frozen system. Any future method should avoid casually adopting the claimed phase-coupling sequence without a formal live-claim analysis.

### 2. US 7,133,801 B2 — base vibration features and speed estimation

**Claim 1 elements reviewed:** establish base vibration features; acquire time-domain vibration from a contact transducer; estimate machine speed from vibration; obtain vibration at that speed; detect faults by comparison with the base features.

**Overlap:** contact-mounted sensor, stored baseline, local/current vibration and fault/anomaly comparison.

**Differences:** VibeGuard’s frozen MVP need not estimate speed using the claimed continuous-vibration model and does not necessarily maintain speed-indexed base features.

**Effect:** anticipates or strongly suggests broad baseline-fingerprint ideas. Speed/load-normalized fingerprints can only support a new claim if the specific permitted information, update mechanism, attribution logic and technical improvement differ materially.

### 3. US 9,176,003 B2 — vector components and operating conditions

**Claim 1 elements reviewed:** measure composite vibration; measure multiple operating conditions; filter a vibration vector at a measurement time; select an operating-condition state; store and evaluate associated information.

**Overlap:** composite vibration processing, selected frequency/vector features, operating-state context and statistical comparison.

**Differences:** the frozen MVP presently has no separate operating-condition sensor and does not implement the claim’s full state-selection structure.

**Effect:** a future speed/load-normalized design must be claim-charted. Merely adding speed/load labels to a vibration baseline is unlikely to be inventive.

### 4. Augury automatic mechanical-system diagnosis family

**Independent-claim theme:** obtain vibration-related data from a machine, identify spectral relationships or machine-state patterns and automatically diagnose a mechanical condition, in some claims using reference or expert information.

**Overlap:** machine-attached vibration sensing, spectral features, automatic state decision.

**Differences:** VibeGuard is local-only and initially anomaly-oriented, not a remote expert diagnostic platform. The proposed abstention and contaminated-baseline safeguards were not verified as required elements of the reviewed Augury claims.

**Effect:** broad diagnosis/fingerprint claims are unsafe as an invention narrative. A future filing would need to center on a concrete interference/installation mechanism and measured physical effect.

### 5. Tractian US 11,429,900 B1

**Independent-claim theme:** sensor on a mechanical machine; vibration data may be compressed and transmitted; remote processing reconstructs data; a trained ML model detects error-condition patterns.

**Overlap:** machine sensor and automatic fault decision.

**Differences:** remote processing, data reconstruction and trained model are central; frozen VibeGuard is local and unsupervised/statistical.

**Effect:** limited literal overlap with the MVP, but strong evidence that “low-cost sensor + learned fault detection” is commercially and legally occupied.

### 6. KR 2015-0120160 A and general MT/Mahalanobis art

**Independent-claim theme:** receive multiple machine-tool characteristic factors, compute a Mahalanobis/MT abnormal-vibration measure, compare with a limit and determine abnormal vibration, sometimes calculating a speed to avoid it.

**Overlap:** multivariate features, normal-space model, Mahalanobis distance and abnormal-vibration threshold.

**Difference:** VibeGuard’s exact feature set, local hardware and alert-only action differ, but those are ordinary implementation choices.

**Effect:** Mahalanobis distance plus common vibration features should be treated as conventional and not claim-relevant by itself.

---

## Frozen-MVP feature comparison

Legend: **E** expressly disclosed; **I** necessarily implied or routine implementation; **S** arguably suggested; **A** absent from the reviewed closest set; **U** unresolved.

| Frozen feature | Closest-art position | Assessment |
|---|---|---|
| One ADXL345 | U | Exact part is not important to inventive step; accelerometers are ubiquitous |
| SPI to ESP32 | A/I | Ordinary interface/platform selection; no novelty weight |
| Local/no cloud | E/S | Edge/local systems predate the MVP; cannot carry novelty alone |
| DC removal | I | Routine signal preprocessing |
| Hann window | I | Routine FFT practice |
| RMS/peak/std/crest/kurtosis | E/S | Common vibration features; kurtosis and peak methods patented/published |
| Threshold + persistence | E/S | Conventional alarm logic |
| Triggered FFT | S | Resource scheduling is plausible but routine unless tied to a non-obvious measured result |
| Baseline spectral subtraction | E/S | Difference/background subtraction is old; exact contamination-safe update not verified |
| Band-limited features | E | Frequency-band/vector analysis is old |
| Mahalanobis score | E | Directly old in anomaly and vibration contexts |
| Single-node operation | E/S | Common product architecture; not equivalent to attribution |
| Normal-baseline acquisition | E | Old baseline/fingerprint practice |
| Neighbour interference handling | E/S | Navy and broader source-discrimination art exists; frozen method unproven |
| Confidence/abstention | S/U | Confidence and reject options are known generally; exact target-attribution gating not verified |
| Adaptive baseline update | S/E | Adaptive baselines are known; contamination safeguard could be a narrow development area |
| Remounting compensation | S/U | Transfer-function and installation calibration are known fields; exact one-node method unresolved |
| Target attribution | S/U | Broad problem old; exact bounded sequence not found |
| RGB alert | E/I | Trivial output |
| Eccentric-mass rig | E/I | Standard lab fault simulation; evidence tool, not invention |
| Compute/memory limits | I | Design constraint; claim relevance only if a specific scheduling method preserves measured performance |

**Conclusion:** No frozen-MVP feature, and no presently defined combination, supports Track A.

---

## Mandatory named-lead investigation

### US 7,421,349 / US Navy

The lead is real and correctly titled *Bearing fault signature detection*. It is important prior art for distinguishing fault-related peaks from unrelated processes. Its method is more specific than generic subtraction and appears to rely on phase coupling. It therefore narrows, but does not automatically eliminate, a different confidence-gated fingerprint approach.

### Tractian

A directly identified family is US 11,429,900 B1 with Brazilian member BR 102022005021 A2. It claims a machine-mounted vibration sensor feeding remote processing and a trained model for mechanical error detection. Tractian therefore occupies automatic vibration-fault detection and remote learned diagnosis, but the reviewed claim theme is not the same as a local one-class, abstaining attribution method.

### Infinite Uptime

WO 2017/151447 and US 2019/0061086 identify Infinite Uptime and university co-assignees on a magnetic add-on sensing system using vibration and acoustic capabilities for tool condition monitoring. This confirms actual patent-family activity. It is more relevant to mounting/package and multi-modal monitoring than to the proposed one-sensor attribution rule.

### Augury

Augury has a substantial identifiable family set: automatic mechanical diagnosis (US 9,835,594; US 10,983,097; EP 2,909,685; Indian publication IN2015DN04150A), machine monitoring (WO 2018/198111 / EP 3,615,899) and active 2026 grants concerning non-stationary machine performance (EP 3,877,819 B1 and US 12,607,995 B2). These families are load-bearing evidence that spectral fingerprints, automatic diagnosis and operating-state handling are crowded.

### KCF Technologies

KCF’s US 9,453,854 / EP 2,913,643 family concerns a vibration sensor including a wireless accelerometer. It is relevant to sensor/package design and wireless deployment, not a broad right to vibration monitoring algorithms.

### Senseye

Senseye is an identifiable commercial predictive-maintenance platform, but this pass did not verify an equally close Senseye-assigned vibration-attribution patent family. It should not be represented as holding a specific blocking family without further assignee and ownership-chain searching. Siemens/Senseye-related portfolio transfers and parent ownership may complicate assignee-name searching.

### Other industrial actors

SKF, GE, Siemens, Hitachi and other industrial firms have extensive machine-condition and vibration-monitoring portfolios. The selected ledger includes examples of position-correlated Fourier analysis, operating-condition normalization and robotic vibration anomaly detection. This reinforces crowding but does not replace claim mapping for a final design.

---

## Non-patent prior art and standards

1. **ISO 20816-1:2016** provides general procedures for measuring and evaluating machine vibration and uses vibration magnitude and changes for operational monitoring and acceptance. A second edition was in FDIS processing in 2026. This demonstrates that vibration magnitude, change, measurement position, operating conditions and vibration from other sources are standardized engineering concerns, not VibeGuard-specific discoveries.
2. Lab machinery datasets routinely use normal, imbalance, misalignment and bearing-fault conditions with conventional classifiers. Excellent cross-validation on isolated laboratory datasets does not prove source attribution or field robustness.
3. The vibration-diagnostics literature has long used RMS, crest factor, kurtosis, spectra, envelopes, sidebands, order tracking and one-class/statistical anomaly methods.
4. Spectral subtraction is well established in signal denoising generally. Applying a fixed background spectrum to machine vibration is an expected engineering adaptation unless the acquisition/update/contamination rule yields an unexpected technical result.
5. Transfer functions and sensor-position compensation are established measurement concepts. A remounting method would need a narrowly defined calibration stimulus, invariant representation or compensation protocol and evidence that it preserves diagnosis after reinstallation.

The literature strongly supports the engineering feasibility of Level 1 bench classification. It does not support treating the isolated rig as evidence of Level 2 attribution.

---

## Current frozen-MVP patent assessment

### Novelty

The exact bill of materials and exact sequence may not appear verbatim in one searched document. That is insufficient. Every material element is known, and several references combine baseline comparison, machine-state normalization, spectral vectors and automatic anomaly decisions. The frozen MVP therefore has **low prospective novelty confidence**.

### Inventive step

An examiner could plausibly combine:

- ordinary contact accelerometer monitoring;
- baseline/fingerprint comparison;
- time and spectral features;
- a Mahalanobis normal-space detector;
- fixed background subtraction or band selection;
- a resource-motivated two-stage pipeline;
- a local MCU and an alert.

The combination addresses predictable cost and compute constraints with expected techniques. No unexpected result is currently defined. **Obviousness risk: High.**

### Eligibility

A claim limited to calculating features and a distance score risks being characterized as mathematical analysis. Eligibility improves when the claim is tied to a particular sensor-machine relationship, controlled calibration states, a physical interference condition, and a measurable improvement in machine-state measurement or alert reliability. Even then, eligibility does not establish novelty or inventive step.

### FTO

The frozen MVP is unlikely to infringe every element of the closest reviewed claims merely by using an accelerometer and common DSP. However, no safe FTO conclusion is possible. Particular risk areas are adopting a claimed phase-coupling workflow, a live operating-state vector/normalization claim, a patented sensor package, or a commercial remote-diagnosis architecture. **Indicative FTO risk for the bench MVP: Low-to-Medium; uncertainty Medium.**

---

## Candidate invention-direction matrix

| Direction | Exact proposed contribution | Prior-art/ordinary-practice pressure | Three-month fit | Track / verdict |
|---|---|---|---|---|
| Frozen MVP combination | ADXL345 + tiered features + Mahalanobis + subtraction | Very high; routine aggregation | High | Reject as invention; Track D if standing alone |
| Single-node attribution under neighbour interference | Attribute target fault despite independently varying neighbour | Broad problem and phase-coupling art old; exact method unresolved | Low for credible proof | **Track C candidate** |
| In-situ target fingerprint from known states | Build target baseline using known target on/off/speed states | Baseline and speed-indexed fingerprints old | Medium | Weak alone; combine only |
| Contamination-protected subtraction/update | Update noise/target baseline only under verified safe states and reject contaminated windows | Adaptive baselines known; exact gate may be narrow | Medium | Track B experiment, Track C patent confidence |
| Confidence-gated abstention | Output target fault only when target evidence exceeds interference ambiguity; otherwise “unknown” | Reject options known generally; physical attribution effect could matter | Medium | **Strong component of Track C** |
| Remounting compensation | Calibrate mounting transfer and preserve feature meaning after reinstall | Transfer/installation calibration known; exact protocol unresolved | Medium | Secondary Track B/C candidate |
| Resource-aware triggered FFT | Cheap features select FFT bands/windows while preserving attribution performance | Obvious compute optimization unless unexpected result | High | Reject alone |
| Speed/load-normalized fingerprint | Normalize target signature by permitted state input | Strong older/live prior art | Medium | Reject alone; use as necessary control |
| Drift-aware baseline adaptation | Update normal model with anomaly/interference safeguards | Known general concept; exact contamination logic may be narrow | Medium | Component, not standalone |
| Deployment/source-label protocol | Single-node calibration sequence using independently controlled target/interferer states | Experimental protocols often obvious; technical calibration interaction could matter | Medium | Supporting method, not enough alone |

### Direction decisions

- **Rejected clearly:** generic triggered FFT, generic Mahalanobis, generic spectral subtraction, generic adaptive baseline, low-cost edge node and isolated imbalance rig.
- **Retained only as a combined research hypothesis:** confidence-gated target fingerprint with contamination-protected baseline handling and installation/state controls.

---

## Strongest surviving direction

### Working title

**Confidence-gated, contamination-protected single-node target-machine vibration attribution**

### Exact technical problem

A sensor attached to one target machine receives a structural mixture of target vibration, neighbouring-machine vibration, transient shocks and mounting-transfer effects. A conventional anomaly score may rise even when the target remains healthy. The technical problem is not detecting “more vibration”; it is deciding when the measured evidence is sufficiently attributable to the target to issue a target-fault alert.

### Proposed bounded contribution

1. Collect calibration windows under independently known combinations of target state and interferer state.
2. Construct a target fingerprint containing target-coherent bands/features and an interference-ambiguity model.
3. Estimate whether a live window is inside an approved target operating-state and mounting-validity region.
4. Compute target anomaly evidence and interference ambiguity separately.
5. Issue **Normal**, **Target abnormal**, or **Unknown/abstain**, rather than forcing every anomaly into a target-fault label.
6. Update normal/background statistics only when target state, interference confidence and anomaly score satisfy a contamination-protection gate.
7. After remounting, require a short transfer-validation sequence or invalidate the prior baseline.

### Measurable technical effect

Compared with RMS, ordinary FFT features, ordinary Mahalanobis and fixed spectral subtraction, the method should reduce false target-fault alarms and attribution errors when the neighbour changes state, without unacceptable missed detection of the target’s induced imbalance. It should also prevent a neighbour-abnormal or target-abnormal window from being learned as normal.

### Risks

- Confidence/abstention, adaptive updates and validity regions are well-known general techniques.
- Combining them with vibration attribution may be seen as routine unless the exact physical calibration and update sequence produces a substantial, repeatable improvement.
- A real field test with independent ground truth is likely necessary for patent-first confidence.

### Track

**Track C.** A limited two-motor bench implementation can begin within three months, but the strongest evidence requires later field access, repeated mounting sessions and independently controlled/known machine states.

---

## Bench demonstration versus field-attribution evidence

### Level 1 — semester bench demonstration

A single damped motor/fan, normal versus fixed eccentric mass, can validate:

- acquisition stability;
- low-frequency imbalance sensitivity within ADXL345 bandwidth;
- local feature computation;
- threshold and Mahalanobis operation;
- RGB alert behavior;
- compute, RAM, latency and repeatability.

It cannot validate:

- attribution to the target under variable neighbours;
- industrial fault diagnosis;
- bearing-fault detection;
- remounting invariance;
- adaptive-baseline safety;
- field false-alarm rate.

### Level 2 — patent-oriented attribution

A controlled two-motor rig should randomize at least:

- target normal / target imbalanced;
- interferer off / normal / imbalanced;
- target and interferer speed/load;
- mounting and remounting sessions;
- repeated days;
- startup, shutdown and transient shocks.

Independent state labels are mandatory. “The algorithm said the neighbour was abnormal” is not ground truth. Field evidence should follow only after the rig establishes basic feasibility.

---

## Novelty analysis

### Frozen MVP

No credible novelty conclusion. Exact implementation novelty is possible in a literal sense, but patent novelty must be assessed claim by claim, and the meaningful elements are found across close references.

### Strongest direction

Potentially differentiating elements are:

- separate target-anomaly and interference-ambiguity estimates;
- an explicit abstention state tied to physical source ambiguity;
- calibration with independently known target/interferer combinations;
- contamination-protected normal-model updates;
- baseline invalidation or transfer validation after remounting.

No single reviewed reference was confirmed to require all five in combination. Novelty confidence is nevertheless only **Low-to-Medium**, because the search was not exhaustive and each constituent concept is known.

---

## Inventive-step / obviousness analysis

The strongest rejection case would combine:

1. base vibration features and speed/state comparison from older machine-monitoring patents;
2. unrelated-process discrimination from the Navy phase-coupling art;
3. ordinary one-class/Mahalanobis detection;
4. known confidence/reject-option logic;
5. known adaptive-baseline contamination controls;
6. known installation or transfer calibration.

The applicant would need to show more than the predictable result of that combination. The best rebuttal would be a pre-registered experiment demonstrating that a particular calibration/gating sequence achieves a material reduction in target-attribution errors under neighbour state changes while using a constrained single node, and that simpler combinations do not.

**Risk:** High before experiments; potentially Medium if a strong, unexpected effect is reproduced across remounting and field sessions.

---

## Patent-eligibility analysis

### United States

USPTO guidance applies the statutory-category and judicial-exception framework. A bare feature-vector, Mahalanobis and confidence calculation could be treated as an abstract mathematical analysis. Eligibility is stronger where the claim recites a vibration sensor physically coupled to a target machine, specific calibration under independently controlled machine states, technical processing that changes the reliability of the physical measurement, and an alert/abstention operation based on that improved measurement. The specification should describe the technological improvement and evidence, not merely state “use AI.”

### Europe

EPO computer-implemented-invention practice requires claim features essential to the technical effect. Processing sensor data to improve the measurement or monitoring of a physical machine can contribute technically, but mathematical features count toward inventive step only insofar as they cause a technical effect. A claim should define the sensor-machine coupling, calibration states, interference handling and physical monitoring effect.

### India

India’s 2025 CRI Guidelines and the statutory exclusion of mathematical methods/computer programs per se make a pure algorithm claim risky. The strongest presentation is a technical vibration-measurement and machine-monitoring method producing a demonstrable physical/technical effect, implemented through a defined sensor and embedded system. Eligibility remains separate from novelty and obviousness.

---

## FTO risk analysis

### Bench MVP

- **Sensor and interface:** generally low algorithmic FTO concern, but avoid copying proprietary sensor-package claims.
- **Common features/FFT/Mahalanobis:** use is not automatically free merely because mathematically known, but no reviewed live claim was mapped as covering the complete frozen implementation.
- **Phase coupling:** do not adopt the Navy patent’s exact workflow without current official status and claim analysis.
- **Operating-state vector analysis:** review US 9,176,003 and active Augury non-stationary families before adding sophisticated speed/load state logic.
- **Remote learned diagnosis:** remaining local avoids central Tractian claim themes identified here.

### Strongest future direction

FTO risk rises to **Medium** because the method would enter source discrimination, adaptive baselines, machine-state normalization and installation calibration. A professional search should be run on the final exact sequence before public disclosure or productization.

No infringement conclusion is made.

---

## Claim-to-experiment map

| Prospective element | Nearest art | Baseline | Proposed experiment | Success evidence | Failure evidence |
|---|---|---|---|---|---|
| Independently labelled target/interferer calibration | Baseline/fingerprint and phase-coupling art | Target-only calibration | 2×2 target/interferer state calibration and held-out randomized trials | Lower attribution error than target-only calibration | No gain or unstable fingerprints |
| Separate anomaly and ambiguity scores | Mahalanobis and confidence methods | Single anomaly score | Compare forced binary output vs three-state abstention | Fewer false target-fault alarms at controlled abstention rate | Missed faults rise excessively or no false-alarm reduction |
| Contamination-protected update | Adaptive baseline practice | Ungated rolling update | Inject target/neighbor faults during update periods | Normal model does not absorb abnormal windows; recovery after drift | Abnormal data learned as normal or model freezes under benign drift |
| Remount validation/invalidation | Transfer-function calibration art | Reuse old baseline blindly | Reinstall sensor across sessions with defined torque/bracket | Maintains separation or correctly requests recalibration | Old baseline produces overlapping distributions/false alarms |
| Resource-aware selected analysis | Triggered FFT practice | Continuous FFT and RMS only | Measure compute/RAM/energy and attribution metrics | Similar attribution with materially lower compute/power | Performance loss or negligible resource benefit |

### Proposed pre-registration metrics

These are recommendations, not frozen project facts:

- balanced accuracy;
- sensitivity and specificity;
- target-attribution error;
- false target-fault alarms per hour;
- missed detections;
- abstention/unknown rate;
- confidence calibration error;
- detection delay;
- remounting repeatability;
- compute time, RAM, flash, sample rate and power.

Owner-approved numerical pass thresholds should be frozen before final testing.

---

## Three-month semester plan

### Weeks 1–2 — measurement integrity

- Procure and authenticate ESP32, ADXL345 and two safe motor/fan units.
- Build a rigid, repeatable sensor bracket and eccentric-mass fixture.
- Verify sample timing, axes, bandwidth boundary and SPI integrity.
- Log raw data; do not tune on every collected trial.

### Weeks 3–4 — conventional baselines

- Implement RMS/persistence.
- Implement ordinary FFT-band features.
- Implement Mahalanobis normal-space score.
- Measure compute/RAM/latency.

### Weeks 5–6 — interference rig

- Add independently controlled interferer.
- Run randomized target/interferer state combinations.
- Evaluate fixed spectral subtraction and band selection.

### Weeks 7–8 — bounded enhancement

- Add three-state Normal / Target abnormal / Unknown decision.
- Add gated baseline update and contamination tests.
- Add mounting validity check or forced recalibration after remounting.

### Weeks 9–10 — locked evaluation

- Freeze parameters.
- Run held-out sessions and ablations.
- Report false alarms, misses, attribution errors and abstention.

### Weeks 11–12 — documentation and IPR gate

- Separate public conventional implementation from confidential rules/results.
- Prepare claim-to-experiment evidence and failure analysis.
- Conduct institutional IPR review before posters, repositories or papers.

The semester MVP remains viable even if the patent enhancement fails.

---

## Later-semester or publication extension

The Track C extension requires:

- access to at least one real environment containing a target and independently varying neighbouring machinery;
- independently known target/interferer states;
- repeated days and operating regimes;
- a documented mounting/remounting protocol;
- larger datasets and locked external validation;
- possible machine-speed/load inputs, if permitted without changing the single vibration-node product architecture;
- possibly an IIS3DWB or industrial accelerometer only if the research question expands to higher-frequency phenomena; this is not required for low-frequency attribution;
- approximately one additional semester, depending on field access;
- a larger validation budget for mounts, replacement sensors, tachometer/reference instrumentation and travel/site access.

Publication value remains even if patentability fails: a rigorously labelled dataset and negative/positive results on single-node attribution, remounting and baseline contamination would be useful research.

---

## Budget, compute and team feasibility

### Semester MVP

The canonical ₹1,700–₹2,200 ADXL345 route remains plausible; a second motor, tachometer/reference speed sensor, mounting hardware and replacements may bring a stronger dual-rig experiment closer to ₹3,000–₹5,000. Prices require procurement refresh.

### Compute

ESP32-class hardware can support:

- 3-axis acquisition at the selected ADXL345 rate;
- short time features;
- 256–1,024-point FFTs;
- small covariance matrices and Mahalanobis scoring;
- simple confidence/gating state logic.

Complex blind source separation, large neural networks or continuous high-rate multichannel processing are outside the frozen resource profile.

### Team

The five-member team is suitable if responsibilities are separated:

- acquisition/embedded DSP;
- anomaly and experiment software;
- hardware/rig and mounting;
- logging/state machine and beginner tasks;
- validation, documentation and presentation.

The key dependency is not programming skill but disciplined experiment control and access to independently labelled interference conditions.

---

## Kill criteria

Treat the patent direction as killed or downgraded when any of the following occurs:

1. Ordinary RMS/FFT/Mahalanobis performs as well as the proposed method under all controlled interference states.
2. Neighbour changes cannot be distinguished from target abnormality above mounting/session variability.
3. Abstention reduces false alarms only by refusing most useful decisions.
4. The contamination gate either learns faults as normal or cannot track benign drift.
5. Remounting variability destroys the claimed effect and no bounded calibration restores it.
6. The differentiating result exists only on the isolated one-motor rig.
7. A closer patent is found that expressly claims the same calibration, ambiguity, update and remounting sequence.
8. The method requires a sensor array, cloud processing or a fundamentally different sensor architecture, making it a major redesign.
9. Field ground truth cannot be obtained, preventing credible attribution evidence.

Failure of the patent direction does not kill the semester prototype.

---

## Confidentiality boundary

### Already public or conventional

- ADXL345/ESP32 use;
- rigid mounting in general;
- DC removal, Hann windows and FFT;
- RMS, peak, crest factor, kurtosis and standard deviation;
- Mahalanobis anomaly scoring in general;
- generic fixed spectral subtraction;
- eccentric-mass imbalance demonstration;
- RGB normal/abnormal/calibrating display.

### Potentially confidential until IPR review

- exact independently labelled calibration sequence;
- target/interference fingerprint representation;
- ambiguity/confidence computation;
- abstention thresholds and state logic;
- contaminated-window rejection and update gates;
- remounting validity/transfer method;
- feature/band selection derived from the experiments;
- datasets containing target/interferer ground truth;
- comparative field results and ablations;
- any unexpected relationship that becomes the proposed technical contribution.

Do not publish source code, datasets, posters, videos or detailed methods containing these elements before institutional IPR review.

---

## Final VibeGuard recommendation

**Required recommendation:** **Retain as strong semester prototype but reduce patent priority.**

VibeGuard should continue as an engineering prototype because it is affordable, demonstrable and well matched to the team. It should not presently be represented as a patent-bearing invention. Its patent priority should remain below “patent-first” until the team demonstrates a specific confidence-gated, contamination-protected attribution method on independently labelled target/interferer data and survives a refreshed claim search.

The correct project narrative is:

- **Semester claim:** a low-cost local normal-versus-deliberately-imbalanced vibration detector.
- **Research hypothesis:** one sensor may support reliable target attribution with abstention and safe baseline adaptation under interference.
- **Patent status:** unestablished; Track C only.

---

## Unresolved questions

1. What is the official current legal status and enforceable claim scope of US 7,421,349 in every relevant jurisdiction?
2. Do any continuations or non-US members of the Navy family remain live?
3. What exact independent claims are active in the 2026 Augury non-stationary-machine grants?
4. Are there Tractian continuations beyond US 11,429,900 that move processing onto the sensor node?
5. Is there a Senseye-origin family now assigned to Siemens that specifically covers vibration fingerprints, confidence or adaptive baselines?
6. Which Chinese and Indian national families claim single-sensor interference rejection, mounting calibration or abstaining vibration diagnosis?
7. Can the team obtain independently known neighbour states in a real field environment?
8. What machine-state information is available without violating the frozen single-node architecture?
9. Can a repeatable bracket and remounting protocol be built within budget?
10. What owner-approved numerical success and abstention thresholds will be pre-registered?

---

## Source and verification log

### Project sources

- `00_READ_FIRST_VibeGuard_Patent_Research_Instructions.md`
- `01_Engineering_Design_Review(5).md`
- `02_Project_mC_Decision_Register_v1.2(5).md`
- `03_Phase3C_Portfolio_Closure_Memo_Approved(5).md`
- `04_Phase3C_VibeGuard_Architecture_Report_Final.md`
- `05_Phase3C_VibeGuard_Memory_Final.md`
- `06_Phase3C_VibeGuard_SOP_Final.md`
- `07_Concept_Evidence_Matrix(5).md`
- `08_Uncertainty_and_Test_Register(5).md`
- `09_Patent_Research_Input_Pack(5).md`
- `10_Phase2_Report_by_Claude(5).md` — used only as historical leads, not current truth

### Patent records reviewed

- US 7,421,349 — *Bearing fault signature detection*
- US 7,133,801 B2 and US 2007/0032966 A1 — *System and methodology for vibration analysis and condition monitoring*
- US 9,176,003 B2 — *Machine vibration monitoring*
- US 8,290,630 B2 / EP 2,169,497 — condition-monitoring parameter normalization
- US 11,429,900 B1 / BR 102022005021 A2 — Tractian automatic error-condition detection
- US 9,835,594 B2; US 10,983,097 B2; EP 2,909,685; IN2015DN04150A — Augury automatic mechanical diagnosis
- WO 2018/198111 / EP 3,615,899 — Augury machine monitoring
- EP 3,877,819 B1; US 12,607,995 B2 / US 2024/0255942 — Augury non-stationary performance
- WO 2017/151447 / US 2019/0061086 — Infinite Uptime magnetic add-on sensing
- US 9,453,854 B2 / EP 2,913,643 — KCF vibration sensor
- KR 2015-0120160 A — Mahalanobis-Taguchi abnormal vibration determination
- US 11,333,580 B2; US 11,500,965 B2 — Mahalanobis anomaly detection
- US 2021/0231528 A1 — separating periodic and non-periodic vibration peaks
- US 12,140,507 B2 — vibration detection and abnormality determination
- US 12,276,541 B2 / WO 2021/220162 — non-invasive vibration condition monitoring

### Official legal/technical guidance reviewed

- USPTO subject-matter eligibility page and MPEP §2106 framework, current through 2026.
- EPO Guidelines for Examination 2026, computer-implemented inventions and technical effect.
- IP India, Guidelines for Examination of Computer Related Inventions 2025, published 29 April 2026.
- ISO 20816-1:2016 and the 2026 FDIS revision status.

### Verification cautions

- Patent database status labels are not legal opinions.
- Family relationships and live claims should be rechecked in official registers before filing or commercialization.
- This pass did not establish infringement, validity or complete FTO.
- Search completeness is limited by public indexing, translations, assignee changes and the time available for an independent pass.


---

## Source 5: `03_CONCEPT_PORTFOLIO/VibeGuard/02_Raw_Research/02_VibeGuard_Patent_Research_Gemini.docx`

- Authority: `TIER_3`
- Treatment: `SUPPORTING_EVIDENCE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `NEW_STAGE10I_EXTRACTION`
- SHA-256: `45001494bc2c8fa8ea5445776e084772493a034ddfc13423a24000baeb451a74`

# Source Extraction

- Chapter: `07` — VibeGuard Patent Evidence and Future Research Path
- Authority tier: `TIER_3`
- Manual treatment: `SUPPORTING_EVIDENCE`
- Original source: `03_CONCEPT_PORTFOLIO/VibeGuard/02_Raw_Research/02_VibeGuard_Patent_Research_Gemini.docx`
- SHA-256: `45001494bc2c8fa8ea5445776e084772493a034ddfc13423a24000baeb451a74`
- Extraction method: `DOCX_XML`
- Rule: source text only; no synthesis, correction or reconciliation.

---

VibeGuard Current Patent Verification — Independent Research

Executive Verdict

Following an exhaustive independent review of the patent and non-patent literature landscape as of 31 July 2026, the executive verdict for the project is that there is a credible path through a bounded three-month enhancement. The frozen Minimum Viable Product architecture—comprising a single, rigidly mounted ADXL345 accelerometer, an ESP32 microcontroller, and a tiered Digital Signal Processing pipeline relying on Fast Fourier Transform, static baseline spectral subtraction, and Mahalanobis distance anomaly detection—is highly feasible from an engineering perspective. However, every constituent element of this baseline architecture is heavily documented in the public domain and standard industrial practice, rendering the unenhanced prototype legally obvious and unpatentable1. Consequently, the frozen Minimum Viable Product itself must not be treated as the invention.

The project is assigned to Track B, signifying a credible path through a bounded enhancement that is achievable and testable within the three-month schedule and the ₹5,000 budget constraint. The specific technical contribution that elevates the architecture from conventional monitoring to a potentially patentable system is the implementation of an Adaptive Baseline Contamination-Protected Spectral Subtraction rule. This enhancement directly addresses the complex problem of maintaining an accurate environmental noise baseline on a resource-constrained edge node without allowing a slowly developing machine fault to contaminate the learned normal state. The confidence level in this direction is high regarding technical feasibility and medium-high regarding patentability, contingent entirely upon successful physical validation. The most important limitation of this strategy is the fundamental inability to validate true single-node source attribution and acoustic cross-talk rejection using only an isolated laboratory bench rig; genuine validation of the patent claims will absolutely require real-world field testing in a dense-machine environment.

Input Inventory and Concept-Fidelity Confirmation

Before commencing substantive research, a comprehensive inventory of the provided evidence base was conducted to verify the integrity and completeness of the input set. The governing instruction file was confirmed to be readable and was established as the authoritative specification for all subsequent analysis4. The evidence package successfully delivered all ten canonical project documents across nine distinct attachments. Crucially, the combined transport bundle was successfully parsed to yield the two separate logical sources contained within it, ensuring that neither the Concept Evidence Matrix nor the Uncertainty and Test Register was omitted from the technical foundation5.

The version control of the project records was verified, confirming the presence of the authoritative Decision Register version 1.2, which supersedes any prior iterations and establishes the finalized constraints for the architecture6. The research confirms absolute fidelity to the frozen concept: the system under evaluation is strictly a passive, single-node, edge-computed machine-vibration detector. The analysis explicitly rejects and excludes any prior historical drift toward active vibration cancellation, haptic feedback mechanisms, wearable systems, multi-sensor arrays, or cloud-tethered predictive maintenance platforms1. The entire input set is complete, free of duplicate or ambiguously named files, and provides a stable, unambiguous foundation for an independent patent landscape assessment. The regional context of Kochi, Kerala, India, has been integrated into the research methodology, specifically informing the evaluation of freedom-to-operate risks within the Indian industrial sector and the strategic navigation of the Indian Patent Office landscape.

Search Methodology and Reproducible Search Log

The research methodology prioritized a reproducible, multi-jurisdictional examination of the patent and technical literature, focusing on the intersection of embedded edge computing, vibration analysis, and condition monitoring. The search leveraged primary records from the United States Patent and Trademark Office, the European Patent Office, WIPO PATENTSCOPE, and the Indian Patent Advanced Search System. The strategy deliberately expanded beyond simple keyword matching to explore relevant Cooperative Patent Classification and International Patent Classification codes, specifically targeting G01H (Measurement of mechanical vibrations), G01M (Testing static or dynamic balance of machines), and G06N (Machine learning and specific computational models)8. The objective was to separate broad marketing claims of commercial platforms from the actual, legally enforceable boundaries of their granted independent claims.

Database / Source

Date Searched

Exact Query / Keywords

CPC/IPC Classes Explored

Assignee / Inventor Searches

Selected Result

Reason Selected or Rejected

USPTO / WIPO

2026-07-31

("predictive maintenance" OR "condition monitoring") AND "vibration" AND ("cloud" OR "remote")

G01H, G06N

Tractian Limited

US11429900B1

Selected as the primary commercial and FTO lead; defines the cloud-tethered machine learning boundary8.

INPASS / EPO

2026-07-31

"vibration" AND "acoustic" AND "magnetic" AND "monitoring"

G01M, G01H

Infinite Uptime

US20190061086A1

Selected to evaluate the specific hardware apparatus and multi-sensor approach of a regional Indian competitor11.

USPTO

2026-07-31

("anomaly detection" OR "novelty") AND "Mahalanobis" AND "vibration"

G01H, G06N7/01

Bar Ilan University

US20140149806A1

Selected as critical prior art demonstrating the conventional application of Mahalanobis distance to sensor anomaly detection13.

USPTO

2026-07-31

"sensor-agnostic" AND "machine fault" AND "vibration"

G01M5/00

Augury Systems Ltd.

US11768486B2

Selected to validate the scope of sensor-agnostic cloud identification platforms14.

USPTO

2026-07-31

("spectral subtraction" OR "noise reduction") AND "vibration" AND "machine"

G10K11/00, H04R

University of Illinois

US10628484B2

Selected to demonstrate the broad applicability and conventionality of spectral subtraction in electromechanical contexts15.

IEEE / arXiv

2026-07-31

"spectral subtraction" AND "machine vibration" AND "condition monitoring"

N/A

Elbouchikhi, E.

IEEE TEC 28(1):135-144

Selected as definitive non-patent literature proving spectral subtraction is standard practice for bearing fault detection3.

Technical and Patent Landscape Map

The industrial condition monitoring and predictive maintenance patent landscape is characterized by high saturation at the macro level, driven by heavy investment in Industry 4.0 and the Industrial Internet of Things. However, this saturation is not uniformly distributed across all architectural approaches. A nuanced mapping of the landscape reveals three distinct technical vectors, each governed by different engineering constraints and patent strategies.

The first and most densely saturated vector consists of cloud-tethered enterprise platforms. Incumbents operating in this space rely on the continuous transmission of raw, compressed, or lightly processed time-series vibration data to remote, centralized servers. At the cloud level, these platforms employ computationally intensive supervised deep learning models, such as convolutional neural networks and autoencoders, trained on massive historical datasets gathered across global fleets of machinery8. The patent filings in this vector focus heavily on data aggregation, sensor-agnostic platform integration, and the specific architectures of the remote neural networks.

The second vector comprises multi-sensor fusion edge devices. Companies competing in this tier focus their intellectual property on the physical hardware apparatus. Their patents typically claim sophisticated enclosures that combine high-frequency piezoelectric accelerometers, acoustic microphones, temperature probes, and occasionally triaxial gyroscopes, integrated with industrial wireless mesh networking protocols like Zigbee or WirelessHART11. The innovation claimed here usually relates to the physical deployment, the ruggedization of the sensor package, and the synchronization of disparate data streams rather than the localized processing of the signal itself.

The third vector, which is characterized by single-node, resource-constrained edge processing, represents the lowest degree of patent saturation and is the precise operational domain of the current project. While the theoretical application of statistical anomaly detection and digital signal processing to vibration data is extensively documented in academic research, there is a marked scarcity of granted patents that claim these specific methods executed entirely and autonomously on a constrained microcontroller without any cloud intervention or multi-sensor fusion. The available white space within this vector lies specifically in the algorithmic management of the signal processing pipeline, particularly how a standalone node handles environmental interference, adapts to changing operational states, and prevents data contamination using only local computational resources.

Verified Patent-Family Ledger

A verified ledger of the most critical patent families and commercial leads establishes the legal boundaries that the proposed architecture must navigate. This ledger distinguishes between the broad marketing claims of predictive maintenance companies and the actual, legally enforceable scope of their intellectual property.

Assignee / Applicant

Publication ID

Title / Subject

Status

Expiry (Est.)

Relevance to Current Architecture

Tractian Limited

US 11,429,900 B1

Systems and methods for automatic detection of error conditions in mechanical machines

Granted (Active)

2041

High commercial relevance. The independent claims explicitly require transmitting data to a remote processing device for machine learning analysis, defining the cloud-tethered boundary8.

Infinite Uptime

US 2019/0061086 A1

Magnetic add-on system with vibration and acoustic sensing capabilities...

Published App

2038

High relevance for regional freedom-to-operate in India. Defines a hardware-centric approach utilizing magnetic clamping and multi-sensor acoustic integration11.

Augury Systems Ltd.

US 11,768,486 B2

Sensor-agnostic mechanical machine fault identification

Granted (Active)

2040

Medium relevance. Focuses on cloud-based, sensor-agnostic fault identification across disparate industrial deployments14.

Bar Ilan University

US 2014/0149806 A1

Method for detecting an anomaly in operation of a data analysis device

Published App

N/A

High relevance as prior art. Directly claims the use of Mahalanobis distance for multivariate anomaly detection based on sensor data streams13.

KCF Technologies

WO 2014/026755 A3

Vibration processing module based on Zigbee technology

Published App

N/A

Low relevance. The claims are focused heavily on the use of Zigbee mesh networking for data exfiltration18.

Closest Independent-Claim Analyses

To rigorously evaluate freedom-to-operate and establish the boundaries of novelty, an analysis of the independent claims of the most relevant commercial threat and the most relevant algorithmic prior art is required. Examining the specific elements of these claims ensures that the architectural constraints placed upon the project effectively circumvent existing intellectual property fences.

The most prominent commercial incumbent targeting the same market segment is Tractian Limited. Their foundational patent, US 11,429,900 B1, describes a system for the automatic detection of error conditions. A detailed breakdown of the primary independent claim reveals a strict reliance on a distributed architecture. The claim explicitly requires a sensor device coupled to a machine to detect vibrations, followed by the mandatory transmission of that vibration data to a remote processing device. The claim further specifies that the remote processing device must generate a reconstructed version of the data and apply a machine learning model, trained on motion patterns associated with error conditions, to detect a fault8. The architecture currently under development fundamentally diverges from this claim structure. By mandating that all digital signal processing, Fast Fourier Transforms, spectral subtraction, and Mahalanobis distance anomaly detection occur locally on the ESP32 microcontroller, the system never transmits raw or reconstructed vibration data to a cloud or remote processing environment1. This strict edge-only constraint ensures that the architecture literally circumvents the most critical elements of the Tractian claims, neutralizing the primary freedom-to-operate risk.

From an algorithmic perspective, US 2014/0149806 A1 by Bar Ilan University represents highly relevant prior art regarding anomaly detection. The independent claim outlines a method comprising the reception of real-time readings from multiple sensors, maintaining a historical record, determining which sensors are correlated, and computing a deviation metric, which is specified in the dependent claims as the Mahalanobis distance, to identify collective and contextual anomalies13. While the current architecture also utilizes the Mahalanobis distance, it differentiates itself by operating on a single, isolated sensor node. Instead of analyzing correlations between disparate physical sensors, the system computes the anomaly score across an engineered feature vector extracted from a single accelerometer, encompassing metrics such as root mean square, crest factor, kurtosis, and top spectral peaks1. While this specific application circumvents the multi-sensor requirements of the Bar Ilan patent, the broader concept of applying Mahalanobis distance to feature vectors extracted from vibration data is thoroughly documented in non-patent literature, rendering the bare mathematical application conventional and unpatentable on its own.

Frozen-MVP Feature Comparison

The features of the frozen Minimum Viable Product were systematically evaluated against the verified patent landscape and the broader body of academic and industrial literature. This comparison isolates which elements of the system are standard engineering practice and which, if any, possess the potential for novel contribution.

Frozen MVP Feature

Closest Verified Prior Art / NPL

Status and Novelty Assessment

Single ADXL345 Accelerometer with Rigid Mounting

Infinite Uptime hardware; EUSPEN 2023 metrology guidelines.

Completely conventional. Rigid mounting is the standard, requisite practice to prevent the mechanical low-pass filtering of vibration signals1.

Serial Peripheral Interface (SPI) Data Acquisition

Universal embedded systems documentation.

Conventional. Required to sustain the 3.2 kHz output data rate of the accelerometer without buffer overflow, a standard engineering limitation1.

Local Processing via ESP32 Microcontroller

Generic edge computing and IoT literature.

Conventional platform selection, widely utilized across academic prototypes and commercial nodes1.

Signal Preprocessing: DC Removal and Hann Windowing

Fundamental digital signal processing textbooks and IEEE standards.

Ubiquitous necessity. Hann windowing is a standard requirement to mitigate spectral leakage during finite-block Fast Fourier Transforms1.

Time-Domain Features: RMS, Peak, Crest Factor, Kurtosis

IEEE TEC 2013; Tractian "Trend Sample" specifications.

Industry standard metrics universally employed to characterize non-Gaussian vibrational energy3.

Compute-Constrained Triggered FFT

US 10,628,484 B2; general low-power embedded literature.

Known architectural logic utilized to conserve computational overhead and battery life on constrained devices15.

Baseline Spectral Subtraction

IEEE TEC 28(1):135-144; EUSPEN 2023.

An established, highly documented method for removing stationary background noise from acoustic and vibration signatures2.

Mahalanobis Distance Anomaly Score

US 2014/0149806 A1; MDPI Sensors literature.

A highly conventional statistical metric used extensively to account for variance and covariance in multi-dimensional feature spaces13.

Visual Alerting via RGB LED

Standard user interface design practice.

Conventional, fulfilling the minimum demonstrable success criteria without adding complex display overhead1.

Isolated Eccentric-Mass Validation Rig

ISO 10816 and ISO 20816 mechanical vibration standards.

The standard laboratory methodology for simulating rotor imbalance safely1.

The comparative analysis reveals that every individual component of the frozen architecture is deeply rooted in known art. The specific aggregation of an accelerometer feeding an edge microcontroller, which subsequently executes a triggered Fast Fourier Transform, applies spectral subtraction, and calculates a statistical anomaly score, is not only anticipated by theoretical literature but is actively suggested as the logical progression for bringing condition monitoring to constrained devices2. Consequently, the baseline architecture lacks the requisite novelty and inventive step to support a standalone patent application.

Mandatory Named-Lead Investigation

The governing instructions mandated a rigorous investigation into several specific commercial entities and historical patent leads to determine their actual impact on the project's viability. This investigation moves beyond corporate marketing material to analyze the underlying technical claims.

The historical reference to US 7,421,349, assigned to the US Navy, concerns the use of sideband phase-coupling to isolate fault-generated spectral peaks from coincidental background noise. While this addresses the same fundamental problem of noise isolation, it relies on a highly specific, fixed mathematical algorithm. The current architecture's transition toward spectral subtraction effectively avoids the exact phase-coupling mechanism claimed in this patent, navigating around the intellectual property by utilizing a different, albeit known, signal processing technique23.

Tractian represents the most significant commercial incumbent targeting the small and medium-sized enterprise market. Their marketing heavily promotes automated fault detection utilizing artificial intelligence and spectral analysis16. However, a review of their granted patents and technical specifications reveals a strict reliance on cloud infrastructure. Their sensors continuously stream data over cellular or Wi-Fi networks to centralized servers, where the data is benchmarked against millions of historical machine hours to produce supervised diagnoses8. The project's absolute commitment to edge-only, unsupervised anomaly detection without cloud connectivity creates a definitive technical and legal separation from Tractian's protected ecosystem.

Infinite Uptime, an India-based venture-backed company, presents a regional freedom-to-operate consideration. Their platform targets complex industrial environments and offers predictive maintenance solutions. An analysis of their patent filings, specifically US 2019/0061086 A1, indicates a strong focus on the physical form factor of their devices. Their claims center on portable, magnetically attachable housings that integrate piezoelectric vibration sensors, which are required for high-frequency and high-temperature environments, alongside acoustic microphones11. The current project relies on a low-cost MEMS accelerometer (the ADXL345) and explicitly mandates rigid epoxy or bolted mounting to avoid the mechanical low-pass filtering inherent in magnetic mounts1. This divergence in hardware apparatus and mounting methodology ensures that the project does not infringe upon Infinite Uptime's specific physical claims.

Augury Systems is another major player emphasizing machine health diagnostics. Their patent, US 11,768,486 B2, describes a sensor-agnostic approach to fault identification. Similar to Tractian, Augury's intellectual property and commercial platform are predicated on aggregating vast amounts of data across different facilities and applying remote, cloud-based analytics to identify overarching failure patterns14. The project's isolated, localized processing architecture does not intersect with these claims.

Finally, companies like KCF Technologies and Senseye are historically associated with wireless condition monitoring. Their patent footprints generally focus on the complexities of wireless mesh networking, such as Zigbee and WirelessHART, and the synchronization of data across large sensor arrays deployed throughout a facility18. Because the current project is explicitly constrained to a single, standalone node without reliance on an external sensor network or data exfiltration mesh, these patents do not present a barrier to development.

Non-Patent Prior Art and Standards

In the context of software and algorithmic patents, non-patent literature often presents a higher hurdle for establishing an inventive step than granted patents. A review of academic databases, including IEEE Xplore and arXiv, confirms that the core mathematical principles relied upon by the baseline architecture are considered standard practice within the engineering community.

The use of spectral subtraction for noise isolation in machine vibration is well-documented. A 2013 IEEE Transactions on Energy Conversion paper by Elbouchikhi explicitly details "Current Frequency Spectral Subtraction and Its Contribution to Induction Machines' Bearings Condition Monitoring," demonstrating the efficacy of this exact technique in removing stationary background noise3. Furthermore, recent publications from precision engineering conferences, such as EUSPEN 2023, advocate for the application of spectral subtraction specifically to minimize the effect of background vibration noise on machine floors during metrology and manufacturing processes2.

Similarly, the Mahalanobis distance is extensively utilized for anomaly detection across various industrial domains. Research demonstrates its application in everything from wind turbine SCADA data mining to incipient sensor fault diagnosis and unmanned aerial vehicle telemetry monitoring13. This metric is favored because it accounts for the correlations between different variables in a multi-dimensional feature space, making it vastly superior to simple Euclidean distance for identifying collective anomalies. Because the application of both spectral subtraction and Mahalanobis distance to mechanical vibration data is already thoroughly established in the public domain, integrating these algorithms into a single device cannot be claimed as a novel invention.

Current Frozen-MVP Patent Assessment

The frozen Minimum Viable Product represents a robust, highly educational engineering achievement that perfectly satisfies the project's requirement to demonstrate local classification of normal versus abnormal vibration on low-cost hardware1. However, from a legal perspective, it is a routine aggregation of commercially available components programmed to execute standard mathematical operations.

Under the frameworks established by major patent offices, including the USPTO's Alice Corp. precedent (35 U.S.C. § 101) and the European Patent Convention's Article 52, mathematical methods applied to generic data are inherently ineligible for patent protection unless they provide a specific, non-obvious technical solution to a technical problem. Furthermore, Section 3(k) of the Indian Patents Act strictly prohibits the patenting of mathematical methods and computer programs per se, requiring a demonstrable technical advancement tied to hardware. The baseline architecture solves the technical problem of edge condition monitoring by utilizing entirely obvious mathematical techniques that have already been published for that exact purpose2. Therefore, a formal assessment concludes that absolutely no credible patent-development path exists for the frozen Minimum Viable Product in its current, unmodified state.

Candidate Invention-Direction Matrix

Recognizing the legal deficiencies of the baseline architecture, an evaluation was conducted to identify a credible path toward patentability through a bounded enhancement. Nine candidate directions, derived from the project's historical documentation and technical literature, were assessed against the strict constraints of a three-month development timeline, a ₹5,000 budget, and the computational limits of the ESP32 platform1.

Candidate Direction

Feasibility (3 Months)

Novelty / Obviousness Risk

Verdict and Rationale

1. Single-node target attribution

Low. Requires extensive, complex field testing to prove efficacy against dense cross-talk.

High. The concept is claimed in theory, though technically unproven on edge devices.

Rejected as the primary semester goal, though it remains the long-term objective of the platform.

2. In-situ baseline acquisition

High. Easily implemented in firmware.

High. Establishing a baseline upon installation is standard calibration practice across all sensor types.

Rejected due to lack of inventive step.

3. Contamination-Protected Spectral Update Rule

High. Can be executed entirely as a firmware logic loop within the existing DSP pipeline.

Low. Provides a specific, non-obvious solution to the known problem of edge-based baseline drift.

Selected as the strongest viable path for patent development.

4. Confidence-gated abstention

High.

Medium. Common in advanced machine learning but less frequent in constrained DSP.

Merged with direction #3 to form a comprehensive control logic.

5. Mounting-transfer compensation

Low. Mechanically too complex to validate within the semester MVP budget.

High. The mathematics of transfer functions are extensively researched in structural dynamics literature.

Rejected due to timeline and budget constraints.

6. Resource-aware triggered FFT

High. Already implemented in the baseline architecture.

High. Triggering power-intensive operations only when thresholds are met is a standard embedded design pattern15.

Rejected as an invention, though retained as a vital system feature.

7. Speed/load normalized prints

Low. Requires integration with tachometers or motor controllers.

High. Violates the strict single-node, isolated sensor constraint of the project.

Rejected for violating architectural constraints.

8. Drift-aware baseline adaptation

High.

Medium. Requires specific safeguards to prevent learning faults as normal behavior.

Merged with direction #3 to create the adaptive update mechanism.

9. Deployment protocol labeling

Medium.

High. Human deployment protocols and labeling methodologies are rarely eligible for patent protection.

Rejected due to high patent-eligibility risk.

The evaluation clearly indicates that attempting to patent the broad concept of single-node attribution or basic resource conservation is legally hazardous. The only direction that balances the severe constraints of the academic semester with a genuine opportunity for technical novelty is the development of a specific, algorithmic update rule that manages how the device adapts to its environment.

Strongest Surviving Direction: Adaptive Baseline Contamination-Protected Spectral Subtraction

The most credible patent development path lies in solving a highly specific, operational challenge inherent to industrial edge computing. In real-world environments, such as a dense factory floor in Kochi, ambient acoustic noise generated by HVAC systems and neighboring machinery is not static; it drifts and changes continuously. Standard spectral subtraction, as documented in the literature, relies on capturing a fixed background noise profile during an initial calibration phase and subtracting it from all subsequent readings2. If the ambient noise profile changes over time, this fixed subtraction fails, resulting in an influx of false alarms as the changing background is misinterpreted as a machine fault. Conversely, if an edge device is programmed to adaptively update its background profile continuously to accommodate this drift, it faces the critical risk of data contamination. A slowly developing mechanical fault, such as bearing wear, could be erroneously incorporated into the updated baseline, causing the system to learn the fault as the "new normal" and resulting in disastrous missed detections.

The proposed technical contribution is the implementation of an Adaptive Baseline Contamination-Protected Spectral Subtraction algorithm. This involves a deterministic, algorithmically efficient logic loop, executed locally on the ESP32, that governs exactly when and how the background spectral profile is updated. The system employs a multi-band confidence gate. If spectral energy increases uniformly across broad frequency bands, which is characteristic of diffuse ambient noise drift, the system updates its spectral subtraction baseline to maintain accuracy and prevent false alarms. However, if vibrational energy increases sharply within specific, narrow harmonic bins—which is the hallmark of a developing mechanical defect on the target machine—the logic loop triggers an abstention protocol. This protocol halts all baseline updates, deliberately freezing the normal profile to ensure that the growing fault energy forces the Mahalanobis anomaly score past the critical threshold, triggering an alert.

This approach differentiates itself significantly from conventional methods. Rather than assuming stationary noise or relying on massive, cloud-based neural networks to disentangle complex signals16, this algorithm uses deterministic, resource-constrained logic to prevent fault-masking entirely on an edge node. By directly improving the reliability of the monitoring apparatus—drastically reducing false alarms in non-stationary environments without sacrificing sensitivity to actual faults—this method produces a tangible physical technical effect, satisfying the patent-eligibility requirements of both the USPTO and the European Patent Office.

Bench Demonstration versus Field-Attribution Evidence

A critical distinction must be maintained regarding the evidentiary value of the testing environments, as the requirements for proving basic engineering functionality differ vastly from the requirements for proving a patentable claim4.

The initial Level 1 semester validation involves a bench demonstration using a small 12V DC motor or PC fan mounted to a heavy, damped base, with an eccentric mass attached to simulate rotor imbalance. This controlled experiment is perfectly sufficient to validate the engineering hypothesis. It proves that the digital signal processing pipeline functions correctly, that the ESP32 possesses the computational headroom to execute the required algorithms, and that the ADXL345 can successfully capture the low-frequency vibrations associated with imbalance1.

However, this isolated bench test absolutely cannot prove the broader claim of single-node attribution under neighboring-machine interference. The acoustic cross-talk, structural resonance, and complex vibrational interplay of a real industrial floor cannot be adequately simulated by simply placing a second small motor on a plywood bench. To secure a defensible patent on the contamination-protected algorithm, the system requires Level 2 field-attribution evidence. The logic must be tested in a genuine dense-machine environment, proving with empirical data that the edge node successfully updated its baseline when a neighboring machine powered on, but correctly abstained from updating, and subsequently alarmed, when the target machine developed a legitimate fault.

Novelty Analysis

The proposed contamination-protected update algorithm successfully navigates the novelty requirements outlined in 35 U.S.C. § 102 and EPC Article 54. A comprehensive review of the prior art reveals that while remote, cloud-based predictive maintenance models continuously train and adapt to changing conditions8, and static spectral subtraction is thoroughly documented in academic literature2, there is no explicit disclosure of the proposed edge-based logic. A deterministic, frequency-band-gated logic loop that conditionally blocks spectral updates based on distinguishing between harmonic and broadband energy signatures, executed entirely within a constrained microcontroller without the use of labeled training data or cloud connectivity, is not anticipated by the searched patent records or non-patent literature.

Inventive-Step / Obviousness Analysis

Overcoming an obviousness rejection under 35 U.S.C. § 103 and EPC Article 56 requires demonstrating that the enhancement is not merely a routine combination of known elements that would be apparent to a Person Having Ordinary Skill in the Art. An embedded systems engineer tasked with condition monitoring typically relies on static baselines to conserve the severely limited memory of microcontrollers, or alternatively, offloads complex adaptive filtering techniques, such as adaptive Wiener filters or blind source separation algorithms, to the cloud due to their computational intensity28. The realization that a highly constrained edge node can achieve adaptive noise isolation without resorting to complex matrix inversions—simply by utilizing a selectively-frozen spectral subtraction profile triggered by heuristic frequency-band analysis—is non-obvious. It provides an elegant, low-compute solution to the contamination problem that contradicts the industry trend of pushing all adaptive logic to centralized servers.

Patent-Eligibility Analysis

The patent eligibility of algorithmic methods is subject to intense scrutiny across all major jurisdictions. Under the USPTO's Alice framework (35 U.S.C. § 101), the proposed algorithm is considered a mathematical concept, placing it within a statutory exception. However, it securely passes the second step of the Alice test by integrating the mathematical algorithm into a practical application. The algorithm produces a concrete physical technical effect: it dictates the operation of a specific piece of machinery (the alerting mechanism) based on a physically transformed signal (mechanical vibration), directly improving the reliability and functioning of the monitoring device itself by preventing false physical alarms.

Similarly, under the European Patent Convention and Section 3(k) of the Indian Patents Act, the algorithm demonstrates a clear technical effect that elevates it beyond a mere computer program per se. The logic loop dictates the internal control state of an embedded sensor, optimizing the utilization of the microcontroller's memory and ensuring the accurate physical triggering of hardware alerts in the face of environmental interference. This tangible improvement to the hardware's operational capability satisfies the technical effect requirements necessary to secure eligibility.

FTO Risk Analysis

Despite the high degree of saturation in the broader predictive maintenance landscape, the freedom-to-operate risk for the specific architecture and the proposed algorithmic enhancement remains remarkably low. This is entirely due to the strict adherence to the project's architectural constraints. The primary commercial threat, Tractian, holds patents that explicitly require the transmission of data to a remote processing device for machine learning analysis8. The project's absolute edge-only constraint ensures non-infringement. Regional competitors like Infinite Uptime focus their intellectual property heavily on complex physical apparatuses, such as magnetic clamping systems and the integration of piezoelectric and acoustic sensors11. By utilizing a simple, rigid epoxy or bolted mount and a single MEMS accelerometer1, the project completely avoids these hardware claims. Finally, while the underlying mathematical concepts of spectral subtraction and Mahalanobis distance are ubiquitous, they reside in the public domain2, meaning their integration into the proposed novel control logic does not infringe on existing algorithmic patents.

Claim-to-Experiment Map

To rigorously validate the proposed patent direction and generate the necessary empirical evidence for a filing, the following pre-registered experimental protocol must be executed. This maps the prospective legal claims directly to the physical tests required to support them.

Legal / Technical Element

Protocol Specification and Requirements

Prospective Technical Element

The selective freezing of a spectral subtraction baseline based on the differentiation of harmonic versus broadband energy thresholds.

Nearest Verified Prior Art

Static spectral subtraction applied to machine vibration, as documented in EUSPEN 20232.

Measurable Technical Effect

A demonstrable reduction in false alarms during periods of ambient noise drift, coupled with the preservation of anomaly sensitivity during the slow onset of machine faults.

Baseline Comparator System

The frozen VibeGuard MVP utilizing fixed, non-adaptive spectral subtraction.

Proposed Invention System

The VibeGuard architecture running the Adaptive Baseline Contamination-Protected Spectral Subtraction firmware logic.

Independent Variables

The operational state of a controlled interferer (Off, Steady-State, Drifting) and the state of the Target Machine (Normal, Eccentric Mass Imbalance).

Controlled Variables

ESP32 clock speed, ADXL345 sampling rate maintained at 3.2 kHz, and strict rigid mounting protocols.

Required Equipment

A custom dual-motor test rig, featuring both a Target and an Interferer motor mounted to a shared, dense base to simulate acoustic cross-talk.

Pre-registration Success Threshold

The adaptive algorithm must demonstrate a greater than 30% reduction in false alarms compared to the static baseline when the interfering motor's state changes, absolutely without causing an increase in missed detections on the target machine.

Three-Month Semester Plan

The bounded enhancement strategy is entirely feasible within the strict constraints of the academic semester, the available ₹5,000 budget, and the capabilities of the five-member student team1. The execution plan is structured sequentially across the three months.

During the first month, the focus is entirely on hardware construction and establishing the baseline digital signal processing pipeline. The hardware-oriented team members will construct the rigid dual-motor test rig, ensuring a stable platform for simulating both target faults and interfering noise. The beginner programmer is assigned highly isolated, manageable tasks, specifically finalizing the RGB LED state machine and the serial logging protocols. Concurrently, the computer science members will implement the core acquisition architecture, including the ADXL345 SPI direct memory access routines, DC removal, Hann windowing, and the triggered Fast Fourier Transform1.

The second month is dedicated to establishing the baseline analytics. The team will implement the static spectral subtraction routines and calibrate the baseline Mahalanobis distance classifier1. The primary milestone for this month is validating the Minimum Demonstrable Success criteria using the eccentric mass to prove the fundamental engineering hypothesis.

The third month represents the transition from a conventional prototype to a potentially patentable invention. The computer science team will code the Adaptive Baseline Contamination-Protected logic loop into the firmware. The team will then execute the rigorous Claim-to-Experiment protocol, systematically comparing the false alarm and missed detection rates between the static subtraction method and the newly implemented adaptive algorithm while actively manipulating the interfering motor on the test rig.

Later-Semester or Publication Extension

While the three-month semester plan culminates in a highly sophisticated bench prototype, solidifying the patent claims regarding true single-node attribution against real-world interference requires a dedicated post-semester extension phase4.

This extension involves deploying a small pilot fleet of three to five enhanced nodes to a dense manufacturing floor, ideally within the Kochi industrial region to align with the regional context. This field deployment requires meticulous, independent ground-truth labeling of machine states and operator logs to accurately correlate the localized alerts generated by the edge nodes with actual, verified machine events. This endeavor remains true to the core project identity because the architecture itself is unchanged—it remains a passive, single-node, edge-computed system based on the ADXL345. Only the complexity of the testing environment scales. Successfully executing this field trial will yield a high-impact academic publication and generate the definitive, indisputable empirical data required to draft a robust and defensible patent application.

Budget, Compute, and Team Feasibility

An analysis of the resource constraints confirms that the enhanced architecture is highly practical. The combined cost of the primary components, specifically the ADXL345 accelerometer (approximately ₹130–350) and the ESP32 microcontroller (approximately ₹300–500), alongside the materials required for the dual-motor test rig, fits comfortably within the preferred ₹3,000 target and leaves ample contingency before reaching the absolute ₹5,000 ceiling1.

From a computational perspective, the ESP32's 240 MHz dual-core processor, equipped with a hardware Floating Point Unit, is fully capable of executing a 256 to 1024 point Fast Fourier Transform alongside the proposed adaptive logic loop in real-time1. The risk of memory exhaustion, a common failure point in edge computing, is effectively mitigated by the triggered-FFT architecture, which ensures that the memory-intensive spectral calculations are only performed when the lightweight time-domain features cross a predefined threshold.

The five-member team structure is optimally aligned with the workload. The three technically strong computer science members are dedicated to the critical path of digital signal processing and algorithmic logic. The beginner programmer is provided with a genuine, low-risk embedded systems learning opportunity through the management of the user interface and logging systems. The hardware-focused member ensures the mechanical integrity of the rigid sensor mounts and the test rig, a crucial factor in preventing the mechanical attenuation of the vibration signals1.

Kill Criteria

The pursuit of a patent based on this specific algorithmic enhancement must be abandoned, and the project reduced to a standard, non-patent-priority semester prototype, if any of the following critical failures occur during development or testing:

First, if the implementation of the dual spectral profiles—requiring the maintenance of both a current baseline and a candidate baseline in memory simultaneously—demonstrably exhausts the ESP32's static random-access memory, causing system instability or crashes that cannot be resolved through code optimization. Second, if the dual-motor bench test reveals that the ADXL345 is fundamentally incapable of differentiating between the target's eccentric mass and the interferer's vibration due to overwhelming, unfilterable mechanical cross-talk transmitted through the shared base of the test rig. Finally, the patent effort must be killed if the adaptive logic loop consistently fails to accurately distinguish between broadband ambient drift and harmonic fault growth, resulting in either a continuous stream of false alarms or the dangerous, complete masking of a developing fault.

Confidentiality Boundary

While the baseline architecture relies entirely on public-domain concepts, such as the ESP32 platform, the ADXL345 sensor, Fast Fourier Transforms, and generic Mahalanobis distance calculations, which require no strict confidentiality, the elements constituting the invention must be protected. The specific mathematical logic, the precise frequency-band thresholds, and the exact gating rules that comprise the adaptive update mechanism are highly sensitive intellectual property. Furthermore, any datasets generated from the dual-motor experiments or the subsequent field-attribution trials must be treated as confidential trade secrets. The team must strictly refrain from publishing code repositories, exact threshold values, or experimental matrices to GitHub, academic preprint servers, or any public domain prior to a formal institutional intellectual property review and the filing of a provisional application.

Final VibeGuard Recommendation

The final recommendation for the VibeGuard project is to advance conditionally pending named evidence.

The project is highly feasible, budget-compliant, and presents an excellent alignment with the team's capabilities. However, because the frozen baseline prototype is legally obvious and unpatentable, its status as a high-priority patent candidate is strictly conditional upon the successful implementation, and more importantly, the rigorous bench-validation of the Adaptive Baseline Contamination-Protected Spectral Subtraction algorithm. If the planned dual-motor experiment fails to definitively prove the algorithm's advantage over static spectral subtraction, the project should be retained and celebrated as a strong, educational semester prototype, but it must be explicitly deprioritized under the project's patent-first selection criterion.

Unresolved Questions

Several critical questions remain unresolved and must be addressed as the project transitions from research to active prototyping. The exact optimal frequency bandwidths and the specific energy-delta thresholds required to reliably trigger the adaptive logic gate on the ESP32 remain unknown; this is strictly an empirical question that can only be answered through iterative tuning during the final month of bench testing. Furthermore, it is currently unverified whether the project owner has secured access to a suitable, dense-machine industrial environment in the Kochi region, which is an absolute prerequisite for the post-semester field validation required to support the patent claims. Finally, if the adaptive algorithm proves highly successful at isolating low-frequency faults, the team must determine whether they will need to execute the documented sensor upgrade path to the higher-bandwidth IIS3DWB (adding approximately ₹1,000 to the cost)1 in order to legitimately claim applicability to high-frequency bearing faults in the final patent specification.

Source and Verification Log

The conclusions presented in this report are strictly derived from the provided evidence base. The governing instructions, absolute budget ceilings, and definitions of the minimum viable product were verified against 00_READ_FIRST_VibeGuard_Patent_Research_Instructions.md4. The foundational project mission, constraints, and the freezing of the architecture were established using the Engineering_Design_Review.md and Decision_Register_v1.2.md6. The technical specifics of the digital signal processing pipeline, the selection of the ESP32, and the capabilities of the ADXL345 were confirmed through the Phase3C_VibeGuard_Architecture_Report_Final.md1. The critical uncertainties regarding single-node attribution and the necessity of dense-machine testing were validated against the 08_Uncertainty_and_Test_Register.md5. Historical freedom-to-operate leads, including Tractian and Infinite Uptime, were sourced from the Phase2_Report by CLaude.md23. External verification of the patent landscape confirmed that Tractian's relevant intellectual property (US11429900B1) is fundamentally cloud-dependent8, that Infinite Uptime's claims (US20190061086A1) are heavily apparatus-focused11, and that the core algorithms of Mahalanobis distance and spectral subtraction are deeply entrenched in conventional non-patent literature2.

Works cited

04_Phase3C_VibeGuard_Architecture_Report_Final.md

Background noise reduction using spectral subtraction for enhanced vibration analysis in precision manufacturing applications - euspen, https://www.euspen.eu/knowledge-base/LAM23118.pdf

Current Frequency Spectral Subtraction and Its Contribution to Induction Machines' Bearings Condition Monitoring | Request PDF - ResearchGate, https://www.researchgate.net/publication/260619524_Current_Frequency_Spectral_Subtraction_and_Its_Contribution_to_Induction_Machines'_Bearings_Condition_Monitoring

00_READ_FIRST_VibeGuard_Patent_Research_Instructions.md

07-08_Validated_Downselection_Evidence_Bundle.md

02_Project_mC_Decision_Register_v1.2.md

06_Phase3C_VibeGuard_SOP_Final.md

US11429900B1 - Systems and methods for automatic detection of error conditions in mechanical machines - Google Patents, https://patents.google.com/patent/US11429900B1/en

CA3128957A1 - Near real-time detection and classification of machine anomalies using machine learning and artificial intelligence - Google Patents, https://patents.google.com/patent/CA3128957A1/en

(12) Patent Application Publication (10) Pub. No.: US 2023/0288549 A1 - Googleapis.com, https://patentimages.storage.googleapis.com/c2/b8/e1/5306198fedc5d6/US20230288549A1.pdf

Patents Assigned to INFINITE UPTIME, INC., https://patents.justia.com/assignee/infinite-uptime-inc

Infinite Uptime 2026 Company Profile: Valuation, Funding & Investors | PitchBook, https://pitchbook.com/profiles/company/156756-34

US20140149806A1 - Anomaly detection methods, devices and systems - Google Patents, https://patents.google.com/patent/US20140149806A1/en

US11768486B2 - Systems and methods for monitoring potential failure in a machine or a component thereof - Google Patents, https://patents.google.com/patent/US11768486B2/fr

US10628484B2 - Vibrational devices as sound sensors - Google Patents, https://patents.google.com/patent/US10628484B2/en

Real-Time Vibration Analysis For Industrial Plant - Tractian, https://tractian.com/en/solutions/condition-monitoring/vibration-analysis

nexscient_424b3.htm - SEC.gov, https://www.sec.gov/Archives/edgar/data/1976663/000147793223008392/nexscient_424b3.htm

WO2014026755A3 - Wireless sensing device and method - Google, http://www.google.com/patents/WO2014026755A3?cl=en

Acoustic-Based Fault Detection for Robotic Arms - IEEE Xplore, https://ieeexplore.ieee.org/iel8/10057477/11306121/11271558.pdf

Wind Turbine Anomaly Detection Using Mahalanobis Distance and SCADA Alarm Data, https://www.mdpi.com/2076-3417/12/17/8661

Condition monitoring of rotating machinery - DiVA Portal, https://www.diva-portal.org/smash/get/diva2:1608078/FULLTEXT01.pdf

IoT Anomaly Detection Methods and Applications: A Survey - ResearchGate, https://www.researchgate.net/publication/362123668_IoT_Anomaly_Detection_Methods_and_Applications_A_Survey

10_Phase2_Report_by_Claude.md

Demystifying TRACTIAN Technology: Most Common Questions, https://tractian.com/en/blog/demystifying-tractian-technology-most-common-questions

Machine Failure Detection, Powered by AI - Tractian, https://tractian.com/en/solutions/condition-monitoring/failure-detection

Business Glossary: Topical Terms & Definitions You Must Know - Clickworks, https://clickworks.ie/business-glossary/

CN104915568A - Satellite telemetry data abnormity detection method based on DTW - Google Patents, https://patents.google.com/patent/CN104915568A/en

arXiv:2312.08660v2 [cs.SD] 16 Dec 2023, https://arxiv.org/pdf/2312.08660

Quantum Fourier Transform–Based Denoising: Unitary Filtering for Enhanced Speech Clarity - arXiv, https://arxiv.org/pdf/2509.04851

01_Engineering_Design_Review.md


---

## Source 6: `03_CONCEPT_PORTFOLIO/VibeGuard/02_Raw_Research/03_VibeGuard_Patent_Research_Perplexity.md`

- Authority: `TIER_3`
- Treatment: `SUPPORTING_EVIDENCE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `NEW_STAGE10I_EXTRACTION`
- SHA-256: `01886aca6ee604cf05f3cc8d082b70e1b1c82c8e4dbccf8ce47e0e5d437be8cc`

# Source Extraction

- Chapter: `07` — VibeGuard Patent Evidence and Future Research Path
- Authority tier: `TIER_3`
- Manual treatment: `SUPPORTING_EVIDENCE`
- Original source: `03_CONCEPT_PORTFOLIO/VibeGuard/02_Raw_Research/03_VibeGuard_Patent_Research_Perplexity.md`
- SHA-256: `01886aca6ee604cf05f3cc8d082b70e1b1c82c8e4dbccf8ce47e0e5d437be8cc`
- Extraction method: `PLAIN_TEXT`
- Rule: source text only; no synthesis, correction or reconciliation.

---

# VibeGuard Current Patent Verification — Independent Research

## Executive verdict

There is no credible Track A invention fully embodied in the frozen VibeGuard MVP as defined by the authority documents; its feature set is broadly consistent with conventional single-sensor vibration monitoring using FFT-based features, thresholding, and Mahalanobis-distance anomaly detection. However, there is a plausible Track C path based on single-node, interference-tolerant attribution and contamination-aware baseline management, which would require at least one later-semester experimental programme beyond the current three‑month MVP window to generate claim-quality evidence.[^1][^2][^3][^4][^5][^6][^7][^8][^9][^10]

On the Track classification, the recommended status is Track C: semester MVP demonstrator now, with any serious patent-development mechanism depending on subsequent field-like or dense-machine validation and carefully designed calibration/baseline experiments. The frozen MVP itself should not be treated as *the* invention; instead, any patent effort should focus on more specific methods for single-node attribution under neighbouring-machine interference combined with drift-/contamination-aware baseline acquisition, update, and confidence/abstention logic, if those can be shown empirically to outperform the closest claim-level prior art.[^2][^4][^5][^6][^8][^9][^1]

The recommended final project decision is: **Retain VibeGuard as a strong semester prototype and potential publication platform while reducing patent-first priority unless later experiments demonstrate a clearly differentiated single-node attribution or contamination‑aware baseline method relative to the identified patent families and technical literature.**[^3][^5][^6][^8][^1][^2]

## Input inventory and concept-fidelity confirmation

The governing instruction file `00_READ_FIRST_VibeGuard_Patent_Research_Instructions.md` is present and readable, and it clearly defines both the research role and the frozen MVP specification. All ten canonical project documents listed there are present under equivalent filenames: Engineering Design Review, Decision Register v1.2, Phase 3C portfolio-closure memo, VibeGuard architecture report, VibeGuard memory, VibeGuard SOP, Concept Evidence Matrix, Uncertainty and Test Register, Patent Research Input Pack, and Phase 2 Report by Claude.[^11][^12][^13][^14][^15][^16][^4][^17][^1][^2][^3]

The Decision Register version attached is explicitly v1.2, and there is no v1.1 file in the current input set, satisfying the requirement not to substitute earlier versions. The authoritative documents and Concept Evidence Matrix consistently describe VibeGuard as a passive, single-node vibration-monitoring and alerting system using one rigidly mounted ADXL345 accelerometer, SPI connection to an ESP32-class MCU, edge-only processing, and a pipeline of DC removal, Hann windowing, time-domain features, and triggered FFT, with RGB LED output and a small DC motor or fan rig.[^15][^11][^1][^2][^3]

The instructions explicitly forbid scope drift into active vibration cancellation, haptics/wearables, multi-sensor arrays in the MVP, audio-event detection, or cloud predictive-maintenance platforms, and the Phase 3C architecture and memory respect this by fixing a single-node, passive detection-and-alerting design. No attached file attempts to redefine VibeGuard as a cloud platform, multi-node array, or actuator-based system; any such earlier mis-scoped research is already excluded in the Phase 3C synthesis and Concept Evidence Matrix.[^1][^2][^3][^15]

## Search methodology and reproducible search log

The patent search emphasized official patent corpora via the dedicated patent search tool, focusing on CPC/IPC classes and keywords relevant to mechanical vibration monitoring, machine/bearing condition monitoring, signal processing/anomaly detection, and embedded/on-device diagnosis. Initial keyword queries included combinations of "machine vibration" with "Mahalanobis distance", "single sensor", "single node", "spectral subtraction", "baseline", and "source attribution" across US, EP, WO, IN, and CN jurisdictions.[^5][^7][^8][^9][^10][^1]

CPC/IPC classes encountered in relevant families included G01M7/00 and G01M7/025 (testing of machine condition by vibration), G01H1/00 and G01H1/003 (measuring mechanical vibrations), and G06F/G06N classes for data processing and anomaly detection, which align closely with vibration-based condition monitoring of rotating machinery. The search then expanded along citation chains from key families, notably the Mitsubishi Heavy Industries Mahalanobis-based abnormality detection patents and Rolls-Royce vibration novelty detection, to capture related approaches using spectral features, thresholds, and multivariate statistics.[^6][^7][^8][^9][^10][^18][^5]

Non-patent literature and industrial standards were not directly searched here because the earlier Phase 3C architecture synthesis and memory already incorporated major industrial vibration standards and white papers (e.g., ISO 10816/20816, condition-monitoring vendor notes), and the current task emphasises claim-level patent comparison rather than re-deriving the basic vibration-monitoring landscape. Individual patents were read at least at abstract and independent-claim level to map elements such as the number and placement of sensors, type of features, use of Mahalanobis distance, baseline handling, and any explicit source-attribution or interference-rejection mechanisms.[^4][^7][^8][^19][^9][^2][^3][^5][^6]

## Technical and patent landscape map

### Conventional vibration monitoring and anomaly detection

The mainstream condition-monitoring patent landscape is highly mature, covering single and multiple accelerometers, spectral analysis via FFT, threshold-based alarms, trend analysis, and a range of diagnostic indicators such as amplitude, phase, and order-tracked harmonics. Several families use vibration spectra and thresholds per band to detect novel spectral content indicative of faults, with probabilistic noise-floor estimation and novelty indices that resemble generic one-class anomaly detection but without being limited to Mahalanobis distance.[^8][^20][^9][^18]

Recent patents from Mitsubishi Heavy Industries disclose rotating-machine abnormality detection where a vibration sensor measures amplitude and phase, frequency analysis is performed, and Mahalanobis distance is computed relative to a unit space of past measurements, with abnormality declared when the distance exceeds a threshold. Other families, such as Valqua's vibration-analysis system, compute signal intensities for multiple frequency bands and use both a first Mahalanobis distance in the spectral space and a second distance in a gravity-centre feature space to predict abnormality generation periods.[^7][^21][^5][^6]

### Spectral subtraction and noise-floor estimation

Spectral subtraction is well known in acoustic and signal-processing patents, where a spectral subtraction gain function is derived from noisy signals and applied in the time or frequency domain to suppress background noise; these patents demonstrate that subtracting a baseline or noise spectrum is not in itself novel. In vibration-specific contexts, Rolls-Royce’s method for monitoring and analysing vibrations in rotary machines estimates a noise-floor amplitude threshold for each speed–frequency subrange, then uses training data from normal operation to identify "known significant spectral content" and flags new significant content at different speed/frequency combinations as novel.[^19][^22][^9][^8]

A more recent resonance-analysis patent from Sandvik describes determining an operational vibration signal during normal operation, exciting the machine with a test signal, and computing a subtraction signal by subtracting the operational signal from the response before frequency analysis to identify natural frequencies; this is another explicit use of subtraction of a baseline vibration signal, though in a resonance-testing context rather than anomaly detection during normal operation.[^10]

### Single-sensor and multi-sensor arrangements

Multiple patents address machine vibration monitoring using one or more sensors mounted on machines, sometimes integrated into the housing, or distributed at multiple bearings or components to improve coverage and diagnosis. For example, Remy/BorgWarner patents on electric machines with integrated vibration sensors mount the sensor within the housing and use its signal to adjust operating parameters, but they are not focused on single-node attribution in dense environments.[^23][^24][^25][^26][^27]

Other systems, such as mining-machine vibration monitoring, place sensors at selected components and trigger data acquisition during specific operating cycles, often using multiple sensors or test points and sometimes wireless units; again, these designs address operational convenience and coverage, not single-sensor source isolation in mixed-machine environments. The Ebara/EP4361583 family emphasises sensor installation guidance and monitoring in rotary machines, including ensuring sensors are placed at appropriate bearings, but it presumes multiple sensor locations rather than constraining to a single node.[^25][^26][^18][^28][^27]

## Verified patent-family ledger

The key families most relevant to VibeGuard’s frozen MVP and proposed invention directions are:

- **Mitsubishi abnormality detection using Mahalanobis distance**: US20200285531A1 / US11334414B2 and family members (JP7470849B2, CN111649886B, DE102020001020B4) claim acquiring amplitude and phase from a vibration sensor, performing frequency analysis, and computing Mahalanobis distance relative to a unit space of past normal data, with abnormality determined when distance exceeds a threshold. These are granted and live, and they establish that Mahalanobis-based vibration anomaly detection using spectral features is prior art.[^5][^6]

- **Valqua vibration-analysis system with dual Mahalanobis distances**: US20230332979A1 / US12590863B2 and related international filings claim calculation of signal intensities per frequency band, first Mahalanobis distance in that spectral-intensity space, computation of two-dimensional gravity-centre data, and a second Mahalanobis distance in a second unit space, with abnormality prediction based on both distances. This family reinforces that Mahalanobis distance on spectral feature vectors is established practice, though it has extra structure compared with VibeGuard’s proposed simple multivariate Mahalanobis over RMS and selected spectral features.[^21][^7]

- **Rolls-Royce / OSyS novelty detection via spectral noise floors**: WO2010094915A1 / US20120035885A1 / US9874472B2 describe recording vibration amplitude as a function of frequency and rotational speed, estimating noise-floor thresholds in multiple speed–frequency subranges, and using extreme-value distributions to classify novel spectral content relative to training runs. This family underpins noise-floor estimation and novelty detection in time–frequency space but does not focus on single-node attribution under neighbouring-machine interference.[^9][^8]

- **Sandvik resonance-analysis and vibration-measurement families**: US20240369403A1 and US20250027836A1 (and EP/DK/FI counterparts) relate to measuring vibrations of vibrating machines, determining gravity vectors and machine vectors, and, in the resonance-analysis case, subtracting an operational vibration signal from a response signal to isolate natural frequencies. These show that subtraction of an operational baseline vibration signal for analysis is known, though again in resonance testing rather than continuous anomaly detection.[^29][^10]

- **Generic vibration monitoring/machine condition patents**: Families such as US4683542A (vibration monitoring apparatus for multiple rotary machines), US9903090B2 (vibration monitoring of mining machines with triggered acquisition during specific cycles), and US10551243B2 (power-efficient wireless vibration monitoring with multiple sensors) represent the background field of vibration sensing, monitoring, and edge processing. They reinforce that using accelerometers, FFT, thresholds, and local processing for machine health is highly crowded technology.[^30][^18][^27]

No located patent family explicitly claims single-node attribution of a specific target machine under interfering vibrations from neighbouring machines using only one accelerometer while relying solely on baseline spectral subtraction and Mahalanobis distance; however, several families would be strong obviousness and proximity references for any such claim.[^6][^8][^9][^10][^5]

## Closest independent-claim analyses

### Mahalanobis-based rotating-machine abnormality detection (Mitsubishi)

The Mitsubishi family’s independent claims require acquiring a detection signal from a vibration sensor on a rotating machine, performing frequency analysis to obtain amplitude and phase, representing them as complex numbers, constructing a unit space from past measured values, computing Mahalanobis distance for new measurements, and determining abnormality when the distance exceeds a threshold. These claim elements align closely with VibeGuard’s proposed primary classifier: a multivariate Mahalanobis-distance anomaly detector over a feature vector drawn from vibration measurements under normal operation.[^3][^4][^1][^5][^6]

However, the Mitsubishi claims focus on a single rotating machine and do not explicitly state single-node discrimination between multiple machines or neighbour interference; they are primarily about improving Mahalanobis-distance calculation through complex-valued representation and dealing with covariance issues. For VibeGuard, this means Mahalanobis distance itself, applied to vibration features with thresholds, cannot be treated as novel; any patentable feature would need to be in the structure of how baselines are acquired and updated, how interference is handled, or how attribution is decided, rather than in the basic use of Mahalanobis distance for vibration anomaly detection.[^5][^6]

### Spectral noise-floor estimation and novelty detection (Rolls-Royce / OSyS)

The Rolls-Royce family claims a method of monitoring vibration amplitude and frequency by recording data as points in speed–frequency space, estimating a noise floor threshold in each subrange, and using training data from normal operation to identify areas of known significant spectral content; new data with significant content outside these areas is treated as novel significant spectral content and triggers alerts. This is conceptually similar to VibeGuard’s idea of baseline acquisition and spectral subtraction, though the patent’s implementation uses probabilistic noise-floor estimation and novelty indices rather than a simple subtraction and Mahalanobis score.[^8][^9]

The claims do not explicitly limit the number of sensors, but the method is framed in terms of a machine under test rather than attribution within a dense cluster of machines, and it does not discuss single-sensor source discrimination under neighbour interference. Nevertheless, this family would be a key prior art reference against any VibeGuard claim that frames band-limited spectral comparison to a baseline as a novelty or fault-detection mechanism, particularly where training on normal data and detecting out-of-family spectral content is central.[^9][^8]

### Spectral subtraction patents outside vibration

The time-domain spectral-subtraction patents (e.g., US6507623B1 and WO2000062281A1) address speech and communications signals, not machine vibration, but they establish that spectral subtraction with baseline or noise-estimation, including time-domain implementations, is a mature technique. They show procedures for computing a gain function from noisy signals, transforming it between time and frequency domains, and convolving to obtain noise-reduced outputs.[^22][^19]

While these patents are not directly in G01M/G01H vibration-testing classes, they contribute to the general prior art on spectral subtraction and would likely be considered in an obviousness analysis if VibeGuard attempted to claim spectral subtraction of a baseline vibration spectrum in the frequency domain for noise suppression. Combined with vibration-specific noise-floor approaches, they make it difficult to argue that baseline spectral subtraction per se is inventive in VibeGuard’s context.[^19][^22]

## Frozen-MVP feature comparison

The frozen MVP includes the following key technical elements: a single rigidly mounted ADXL345 accelerometer, SPI interface to an ESP32-class MCU, DC removal/mean subtraction, Hann windowing, continuous time-domain features (RMS, peak, standard deviation, crest factor, kurtosis), a calibrated RMS threshold with persistence as a minimum classifier, a primary target classifier based on Mahalanobis distance over features, baseline spectral subtraction and band-limited features for noise mitigation, and an RGB LED output.[^2][^15][^1][^3]

Single MEMS accelerometer monitoring for machine condition, FFT-based feature extraction, and RMS/peak/kurtosis-based thresholds are conventional in both industrial practice and patents; the located prior art repeatedly uses vibration sensors, frequency analysis, and thresholds for condition monitoring. Mahalanobis-based anomaly detection applied to vibration features is explicitly claimed in the Mitsubishi and Valqua families, confirming that such statistical detection on vibration spectrums is established.[^20][^18][^27][^7][^21][^6][^8][^9][^5]

Spectral subtraction and baseline noise-floor estimation are known techniques from both communications and vibration monitoring, and substituting them as a noise-mitigation step in a pipeline that otherwise uses standard features and thresholding would likely be considered an obvious combination for someone skilled in the art. The use of an ESP32 MCU, SPI, Hann windowing, and a small DC motor or fan rig is implementational context rather than a claimable invention; these choices align with low-cost embedded practice but do not appear to introduce non-obvious technical effects by themselves.[^15][^22][^10][^2][^3][^8][^19][^9]

## Mandatory named-lead investigation

The Phase 2 report identified several mandatory leads: US 7,421,349 (described historically as a US Navy phase-coupling lead), and patent families associated with Tractian, Infinite Uptime, Augury, KCF Technologies, and Senseye. Within the time and search-budget constraints of this pass, direct identification of US7,421,349 via number-based search in the available patent corpus was not successful, but the behavioural description suggests it relates to phase coupling or spectral-peak relationships in vibration or acoustic signals.[^4]

However, the Mitsubishi and Rolls-Royce families already provide strong art around phase-inclusive spectral features, Mahalanobis detection, and novelty in speed–frequency maps, which likely capture much of the same conceptual territory around using phase relationships and spectral patterns for fault detection. As for Tractian, Infinite Uptime, Augury, KCF Technologies, and Senseye, this investigation did not directly identify their patent families due to the lack of name-based search in the dedicated patent tool and the current instruction to prefer that tool over general web search for patent data; the Phase 2 Input Pack already warns that their products should not be assumed to imply patent coverage for every feature.[^4][^6][^8][^9][^5]

Given those limitations, the named commercial-lead investigation remains incomplete in terms of specific family numbers, but the generic industrial families reviewed here demonstrate that cloud-based multi-sensor predictive-maintenance platforms rely heavily on known sensing and spectral techniques, with patents often focusing on system-level workflows, dashboards, or multi-sensor fusion rather than single-node edge attribution as in VibeGuard’s baseline. Any serious filing or FTO assessment for VibeGuard would require a deeper, assignee-focused search in full patent databases for these companies’ portfolios, beyond the current tooling.[^18][^27][^20]

## Non-patent prior art and standards

Phase 3C’s earlier research (Perplexity report and Claude synthesis) already documented ISO 10816/20816 vibration-severity standards and industrial white papers from major sensor vendors; these show that using vibration RMS, crest factor, kurtosis, and spectral features to detect machine faults is standard engineering practice. The Concept Evidence Matrix confirms that Phase 3C converged on an ADXL345/ESP32 pipeline precisely because it aligns with mainstream vibration-monitoring practice while staying within student-budget constraints.[^2][^3][^15]

Academic literature on vibration-based condition monitoring commonly uses FFT, envelope analysis, spectral kurtosis, and various statistical or machine-learning classifiers, including one-class methods, making VibeGuard’s frozen pipeline technically conventional at the algorithmic component level. Without new, carefully documented experiments showing that its specific combination of baseline spectral subtraction, band selection, Mahalanobis distance, and confidence/abstention leads to quantifiable performance gains in single-node attribution under realistic interference, it would be difficult to distinguish from this non-patent prior art.[^3][^2]

## Current frozen-MVP patent assessment

Taken as a whole, the frozen MVP appears to be a competent but largely conventional embedded vibration-monitoring design: single MEMS accelerometer, FFT-based features, thresholding, and optional Mahalanobis anomaly detection on an ESP32. Each individual building block—sensor choice, SPI interface, DC removal, Hann window, RMS/peak/crest/kurtosis features, triggered FFT, spectral subtraction, Mahalanobis classifier—has clear antecedents in both patents and technical literature.[^22][^1][^6][^8][^19][^9][^2][^3][^5]

The only elements that might rise above routine engineering combinations are those tied to the more ambitious single-node attribution and baseline-management ideas: in-situ calibration of both target and neighbour spectra, contamination-resistant baseline updating, and explicit confidence/abstention behaviour when interference makes attribution ambiguous. None of these is fully implemented or empirically characterised in the frozen MVP; they are at best documented as planned mitigation techniques and candidate invention directions rather than established functionality.[^1][^15][^4]

Therefore, the frozen MVP alone should not be treated as a patentable invention; instead, it should be seen as a platform for running more advanced experiments on attribution and baseline management that might support narrowly-scoped method claims if a distinctive technical contribution emerges.[^1][^2][^3]

## Candidate invention-direction matrix

### 1. Single-node target-machine attribution under neighbouring-machine interference

- **Problem**: Distinguish abnormal vibration of a specific target machine using only one accelerometer when other machines and environmental sources produce overlapping vibrations.
- **Proposed contribution**: Use rigid mounting on the target machine, in-situ baseline acquisition, band-limited spectral features, and baseline spectral subtraction combined with Mahalanobis distance and confidence/abstention to achieve measurable attribution performance without multi-sensor arrays.[^2][^3][^4][^1]
- **Closest art**: Rolls-Royce novelty detection in speed–frequency space, Mitsubishi Mahalanobis-based abnormality detection, Sandvik resonance-analysis subtraction, and generic multi-sensor monitoring systems.[^27][^10][^30][^18][^6][^8][^9][^5]
- **Differentiators**: Single-node constraint with intentional interference, explicit attribution metric (e.g., correct classification of target vs neighbour faults) tied to specific baseline acquisition and subtraction protocol, and an abstention mechanism.
- **Ordinary practice vs novelty**: Single-sensor monitoring and spectral comparison are ordinary; what may be less conventional is formalising single-node attribution and abstention under designed experiments with neighbour machines.
- **Feasibility**: Difficult to demonstrate convincingly within three months on a real dense machine floor, but a dual-motor rig with controlled interferer could provide intermediate evidence.[^1][^2]

### 2. In-situ target fingerprint/baseline acquisition using known machine operating states

- **Problem**: Acquire robust baseline fingerprints of a machine’s normal vibration across speed/load conditions without multi-sensor setups or offline lab equipment.
- **Proposed contribution**: Structured calibration sequences at known operating speeds/loads, capturing band-limited features and spectra, plus a baseline representation that is used for Mahalanobis or novelty detection and can be updated cautiously.
- **Closest art**: Rolls-Royce training on normal runs at multiple speed–frequency subranges, generic vibration trending and baseline capture, and Mitsubishi’s unit space of past normal measurements.[^6][^8][^9][^5]
- **Differentiators**: Emphasis on single-node, student-scale deployment and explicit calibration protocol rather than industrial test-rig procedures.
- **Feasibility**: Highly feasible within three months on a bench rig if speed/load can be controlled or at least measured.

### 3. Contamination-resistant baseline update and spectral-subtraction rule

- **Problem**: Prevent abnormal or neighbour-contaminated data from being learned as "normal" during baseline updates, leading to missed faults.
- **Proposed contribution**: Define an explicit update rule that uses confidence thresholds, abstention regions, and perhaps separate fast/slow baselines so that suspected abnormal or ambiguous segments are excluded from baseline adaptation and spectral subtraction reference updates.[^4][^1]
- **Closest art**: Generic literature on drift-aware anomaly detection and adaptive noise reduction; prior patents focus more on static baselines and thresholds than on contamination-aware updates in vibration.[^8][^19][^22][^9]
- **Differentiators**: Bringing contamination-aware baseline management explicitly into a resource-constrained, single-node vibration-monitoring edge system with experimentally validated impact on false alarms and missed detections.
- **Feasibility**: Algorithmically feasible within three months on the MVP, provided careful logging and analysis are implemented.

### 4. Confidence-gated or abstaining anomaly decisions

- **Problem**: Avoid mislabeling ambiguous states (e.g., when neighbour interference is strong) as either normal or abnormal, which can mislead operators.
- **Proposed contribution**: Implement a confidence-calibrated anomaly score from Mahalanobis distance or related metrics, with explicit "unknown" or "interfered" states when the score falls into an intermediate range or when spectral signatures suggest overlapping sources.
- **Closest art**: Many anomaly-detection frameworks discuss confidence and thresholds, but explicit abstention modes in embedded vibration monitoring are less frequently formalised in patents.
- **Differentiators**: Grounding abstention decisions in specific spectral and baseline features tied to single-node constraints and demonstrating their value empirically.
- **Feasibility**: Straightforward to implement and test on the MVP; key question is whether the behaviour is technically non-obvious given existing anomaly-detection methods.

### 5. Mounting-transfer or remounting compensation

- **Problem**: Preserve diagnostic meaning when the sensor is remounted, altering the mechanical transfer function between machine and accelerometer.
- **Proposed contribution**: Develop a calibration or normalization method that estimates transfer-function differences between mountings (e.g., via calibration sweeps or comparison to stored baselines) and applies corrections to preserve comparability of features.
- **Closest art**: Patents on sensor-mounting and installation guidance for vibration sensors emphasise placement but do not appear to provide detailed transfer-function remount compensation methods; literature may discuss this more than patents.[^24][^26][^23][^25]
- **Differentiators**: Focused, quantitative method for remount compensation on low-cost single-node hardware, with benchmarked repeatability metrics.
- **Feasibility**: Conceptually demanding and likely beyond single-semester scope for robust results.

## Strongest surviving direction

Among these directions, the most promising candidate for future patent development is **contamination-resistant baseline management combined with confidence-gated single-node attribution**, because it sits at the intersection of VibeGuard’s existing architecture and a less-saturated area of the patent landscape. Mahalanobis-based detection and spectral features are already covered, but the specific way in which baselines are acquired, protected from contamination, and used to gate decisions and abstentions in a resource-constrained single-node setting appears less directly claimed in the identified art.[^9][^3][^5][^6][^8][^2][^4][^1]

However, this direction requires substantial experimental evidence beyond the isolated eccentric-mass rig: tests with controlled neighbour machines, remounting, and drift scenarios are needed to show that the proposed rules materially reduce false alarms and missed detections compared with straightforward thresholds and static baselines. Given the current semester constraints, this direction fits Track C: initial algorithms and simple tests could be implemented now, but a convincing patent story would need a later-semester validation programme.[^16][^15][^1]

## Bench demonstration versus field-attribution evidence

The frozen MVP’s Level 1 demonstration—a single DC motor or fan on a heavy base with an eccentric mass and possibly loosened mounting—can show that a single-node system can distinguish deliberate abnormal conditions from normal operation using local processing and simple classifiers. Such an experiment, while valuable for teaching and feasibility, does not prove single-node attribution under neighbouring-machine interference, because the environment is controlled and there is no competing vibration source.[^3][^2][^1]

Level 2 evidence, required for patent-oriented single-node attribution, would involve at least one additional machine or controlled interferer, with independently known states, speed/load variation, and possibly remounting, to see whether the algorithm correctly attributes abnormal states to the target machine and not to the neighbour. None of the current architecture or memory documents claims that such experiments have been performed; the single-node attribution problem is explicitly flagged as unresolved and deferred to prototype testing and later phases.[^15][^2][^3][^1]

Thus, by design, the current bench MVP serves as a necessary but not sufficient step toward any patentable attribution method; it validates core sensing and processing but not the more ambitious claim of robust source discrimination in realistic environments.[^2][^3][^1]

## Novelty analysis

At the level of individual techniques, none of the MVP’s processing stages appears novel relative to the disclosed patents and likely non-patent literature: DC removal, windowing, FFT, RMS/peak/crest factor/kurtosis, thresholding with persistence, spectral subtraction, and Mahalanobis distance are all well-known. The use of an ESP32, ADXL345, SPI, and RGB LED is standard embedded engineering practice, and many commercial systems use similar microcontrollers and sensors for vibration monitoring.[^20][^18][^27][^19][^22][^5][^6][^8][^9][^2]

Novelty, if any, would therefore need to arise from the *specific combination* of these elements targeted to single-node attribution and contamination-resistant baselines, with well-defined rules and measurable effects on attribution performance under interference, remounting, and drift. Given the breadth of prior art and the lack of current experimental evidence, it is more conservative to treat the MVP as non-novel and to reserve patent ambitions for more tightly scoped methods that can be shown to deliver improvements beyond routine statistical and DSP practices.[^4][^1]

## Inventive-step / obviousness analysis

Combining a MEMS accelerometer, FFT-based features, spectral subtraction, and Mahalanobis distance would likely be considered an obvious application of known techniques in vibration analysis and anomaly detection, especially given direct patents combining vibration spectral analysis and Mahalanobis detection. Using a single sensor instead of multiple sensors is generally seen as a cost/complexity trade-off rather than a non-obvious technical step, absent strong evidence that the single-node design achieves comparable attribution performance to multi-sensor benchmarks.[^5][^6][^8][^9]

To argue non-obviousness, a VibeGuard claim would need to highlight specific technical problems not addressed in the prior art and show that the claimed methods solve them in a non-trivial way; single-node attribution in dense environments and contamination-resistant baselines are plausible candidates, but they must be operationalised in detail and contrasted against existing methods like multi-sensor arrays, order tracking, or sophisticated spectral-noise models.[^10][^8][^9][^1][^4]

Given this, any near-term filing should be framed cautiously as a narrow method claim with detailed steps and conditions rather than a broad platform claim for single-sensor edge vibration monitoring; otherwise, it risks being rejected as an obvious combination of known elements in a crowded field.

## Patent-eligibility analysis

In jurisdictions like the US, Europe, and India, claims purely to mathematical methods or abstract algorithms are generally not patent-eligible unless they are tied to a concrete technical implementation producing a physical technical effect. The cited vibration-monitoring patents solve this by clearly associating their algorithms with specific physical machines and sensors, and by claiming steps of acquiring vibrations from real machines and outputting diagnostic signals or predicted abnormality periods.[^18][^6][^8][^9][^5][^1]

A VibeGuard claim would need to emphasise the connection between the algorithm and the physical behaviour of the machine—the way baseline acquisition, spectral subtraction, and Mahalanobis-based decisions affect detection and attribution of real machine faults—rather than presenting them as generic data-analytics steps. Framing the contribution in terms of improved fault detection or attribution performance for a specific class of machines, under practical constraints like single-node sensing and limited edge compute, would help satisfy technical-effect requirements, but only if supported by experimental evidence.[^1][^4]

## FTO risk analysis

Freedom-to-operate cannot be fully assessed here, but some qualitative risks are apparent. The Mitsubishi and Valqua families show live claims on Mahalanobis-based vibration abnormality detection using frequency-analysis features, so naive implementations of multivariate Mahalanobis classifiers on amplitude/phase or spectral intensities for rotating machines may intersect their claim scope. Likewise, Rolls-Royce’s novelty detection in speed–frequency maps and Sandvik’s subtraction of operational vibration for resonance analysis could overlap with parts of any spectral-subtraction-based attribution method.[^7][^21][^10][^6][^8][^9][^5]

Because VibeGuard’s MVP is educational and experimental, short-term academic prototyping risk may be acceptable, but any commercial deployment or filing would require detailed claim-charting against these families and others owned by major condition-monitoring vendors. Designing around might involve focusing claims on contamination-resistant baseline management and explicit abstention/attribution logic under single-node constraints, in ways that current art does not explicitly cover, though this supposition would need legal confirmation.[^6][^8][^9][^5][^4][^1]

## Claim-to-experiment map

For each candidate invention direction, experiments should be designed to measure specific technical effects relative to baselines:

- **Single-node attribution**: Dual-motor rig with independently controllable target and interferer, known operating states, and conditions where only one machine is faulted; metrics include sensitivity, specificity, and attribution error (incorrectly blaming the wrong machine), compared across RMS-only thresholds, generic FFT features, and the proposed baseline-subtraction/Mahalanobis method.[^15][^1]
- **Contamination-resistant baseline update**: Longitudinal experiments where the target machine experiences drift, temporary faults, and neighbour-state changes, with variants of baseline-update rules (naive moving average vs contamination-aware rules) and measures of error rates and baseline stability.
- **Confidence/abstention logic**: Tests where interference is intentionally high or ambiguous, logging how often the system abstains versus mislabels, and comparing operator decision burden and risk to conventional threshold systems.

These experiments should be pre-registered with clear success/failure conditions and mapped explicitly to prospective claim elements (e.g., specific update rules, threshold ranges, or abstention criteria) so that evidence can support or kill each direction.[^16][^1]

## Three-month semester plan

Within the current semester and budget constraints, VibeGuard should aim for:

1. A robust Level 1 bench MVP using the frozen architecture (ADXL345, ESP32, DC removal, Hann, RMS/peak/crest/kurtosis, triggered FFT, RMS threshold with persistence) validating normal vs eccentric-mass abnormal classification with clear RGB output.[^3][^2][^1]
2. Initial implementation of a multivariate Mahalanobis classifier over the calibrated feature vector, at least on bench data, even if not fully tuned.[^2][^3]
3. A simple dual-motor or motor-with-interferer rig to run preliminary single-node attribution tests, even at small scale, to understand practical challenges.[^15][^1]
4. A first version of contamination-aware baseline update and confidence/abstention logic, tested on bench and dual-motor rigs.

This work would not complete the patent evidence but would lay the technical and experimental foundation for a later, more rigorous validation programme.

## Later-semester or publication extension

A later-semester project or capstone could extend VibeGuard into a more publication-oriented and patent-relevant direction by:

- Collecting dense-machine or multi-motor datasets with realistic interference and remounting scenarios, including independent ground truth for machine states.[^15][^1]
- Systematically comparing baseline spectral subtraction, Mahalanobis-based anomaly detection, and contamination-aware update rules to standard industrial baselines and existing academic methods.[^8][^9][^5][^6]
- Formalising and documenting the best-performing method as a candidate claim, with explicit technical constraints, parameter ranges, and performance metrics.

Such an extension could target a workshop or conference paper on single-node vibration attribution and anomaly detection on constrained hardware, with any patent filing contingent on the novelty and robustness of the results.

## Budget, compute and team feasibility

The selected architecture fits comfortably within the ₹3,000–₹5,000 budget, with estimated BOM costs around ₹1,700–₹2,200 for the ADXL345-based MVP and roughly ₹4,000 if the higher-bandwidth IIS3DWB sensor is used as an upgrade, leaving margin for test-rig materials and replacements. ESP32-class MCUs and ADXL345 modules are widely available and affordable, and the compute requirements of a 256–1,024-point FFT plus basic statistical features are within the capabilities of the selected hardware.[^3][^2][^15]

Team-skill fit is strong, as VibeGuard leans on embedded programming, DSP, and statistical analysis—all aligned with CS/Cybersecurity backgrounds—with mechanical tasks largely limited to building a simple motor/fan rig and rigid sensor mounts. The more advanced attribution and baseline experiments will require additional effort in experimental design, data management, and analysis but remain feasible for a motivated student team over multiple semesters.[^12][^2][^3][^15]

## Kill criteria

VibeGuard’s patent-oriented development should be terminated (or de-prioritised) if:

- Experiments show that single-node attribution under realistic neighbour interference cannot achieve materially better performance than simple thresholds or basic spectral methods, even with sophisticated baseline and abstention rules.[^1][^15]
- Contamination-resistant baseline update rules either fail to improve robustness or are replicated closely by already-patented methods discovered in deeper searches.[^9][^5][^6][^8]
- Assignee-focused searches for Tractian, Infinite Uptime, Augury, KCF Technologies, and Senseye reveal existing claims on the same combination of single-node operation, baseline calibration, spectral subtraction, and anomaly detection.[^4]

In any of these cases, VibeGuard would retain strong value as an educational prototype and possible publication platform but would not justify patent-first investment, and attention could shift to other concepts or to non-patent dissemination routes.

## Confidentiality boundary

The frozen MVP’s basic architecture—ADXL345, ESP32, DC removal, Hann window, standard features, triggered FFT, RMS threshold, Mahalanobis distance, spectral subtraction as a generic idea—is largely conventional and can be discussed openly in teaching or publication, subject to institutional preferences.[^19][^22][^5][^6][^8][^2][^3][^1]

However, any specific contamination-resistant baseline update rules, attribution-focused calibration protocols, abstention logic, and detailed experimental datasets or results that show performance advantages should be treated as confidential until reviewed by the institution’s IPR office. If no patent filing is pursued after such review, these methods could later be disclosed in academic publications with appropriate open-source code and data releases.[^4][^1]

## Final VibeGuard recommendation

VibeGuard should be advanced as a strong semester prototype and research platform but **not** as the primary patent-first candidate unless later experiments clearly demonstrate a technically specific, non-obvious single-node attribution or baseline-management method relative to the identified patent families. Short-term work should prioritize a robust bench MVP, basic Mahalanobis-based anomaly detection, and initial exploration of contamination-aware baselines and confidence/abstention, while deferring any patent decisions until more substantial evidence is available.[^10][^5][^6][^8][^9][^2][^3][^15][^1]

## Unresolved questions

Key unresolved questions include:

- The exact scope and claims of US7,421,349 and any Tractian/Infinite Uptime/Augury/KCF/Senseye families directly relevant to single-node attribution, which require broader patent-database and assignee-name searches than available here.[^4]
- Whether any non-patent literature already describes contamination-resistant baseline management and abstention logic in vibration monitoring in ways that would pre-empt VibeGuard-specific claims.
- The practical limits of single-node attribution on real factory floors with multiple machines, structural coupling, and variable operating conditions.

These questions must be addressed in future research and legal review before any serious commitment to a VibeGuard patent programme.

## Source and verification log

- Governing instructions and frozen MVP definition: 00_READ_FIRST VibeGuard Patent Research Instructions.[^1]
- Project authority and constraints: Project mC Decision Register v1.2.[^11]
- Engineering Design Review, VibeGuard section.[^12]
- Phase 3C VibeGuard architecture report.[^2]
- Phase 3C VibeGuard memory.[^3]
- Phase 3C VibeGuard SOP.[^14]
- Concept Evidence Matrix.[^15]
- Uncertainty and Test Register.[^16]
- Patent Research Input Pack.[^4]
- Phase 2 patent-landscape report by Claude.[^17]
- Mahalanobis-based rotating-machine abnormality detection patents.[^21][^7][^5][^6]
- Vibration spectral novelty and noise-floor estimation patents.[^20][^8][^9]
- Spectral subtraction patents.[^22][^19]
- Generic vibration-monitoring and machine condition patents.[^28][^31][^23][^24][^30][^27][^18]
- Resonance-analysis and vibration-measurement patents using subtraction and vector methods.[^29][^10]

---

## References

1. [00_READ_FIRST_VibeGuard_Patent_Research_Instructions.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/144580388/b78d60c5-0c8e-4108-9307-5edeb1c6cd01/00_READ_FIRST_VibeGuard_Patent_Research_Instructions.md?AWSAccessKeyId=ASIA2F3EMEYE3EDXHSKO&Signature=%2F7TktB2MNW%2Bclxr94VOFrzpwsws%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQCSwumtw0icCRuB%2FTg5Kc9iXqLGjvemNYVtECiGlyG5ngIgdBdvQiJVnNcXeEebwj6kkIsLNP9JpWQtKILofhG0Eq0q%2FAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDKmF3l5FEdGfj4NQUirQBJXUWLC%2FDKrifxGPxd%2B7Lroe0B7V9X7ZCfAk%2BQiH5z5DJGgUcFlorBJnii6EwM9sQi9ifEfpdRLY2zJkbDt95CP8RRIdukZB8m6b0n277PX2GJqRS8sXzCAWv%2FtLZf%2FVQ%2BoH2Dpu%2FkCNFqYDsYUN71yoBy3lak5R7FsrV5FUAsKFPHbcmuRitn6zjHRKtojh3VJIZMl%2BoCjTrRzqDLiFJ78ZkES6vuG58teikYUN%2FTPVJiwqN0eiy4K1PWhTIz6yCo%2B8J9zMjIsukX%2B8s1wBLPzNIMOdWpEDiOjQo3bB%2F9oVuKxWdaKeXJfXcyW6%2BO8ndDCcgryq%2BTW47z2HDm%2BpEwFVdbV%2FeYlz1Yi5YULkAbTmn9a2X9S0IAJ4wWw3BM97luXXZTzPq28UbwA%2BX4pV7EvWgj1eV13NPf6zmGvzl6jan7B16NZfnzYadl9xaqFwjQNbOWLE0AH8LPMp0JtN%2Fv1pnAIZORYTzBnRpiHd0cwkXABgWCXzhTTVl0Zshw9lG5l5ZsWfTrmBvJDrgY%2BBGjdosY1PtI35XXDib%2FEQh%2F%2B%2FdsrP0kV75AFCk779yQp8RP0F81eQRbm5%2BBxrSklqUrmdvE%2Bq4T5HGwOXRXiA7k%2Bl6pcH4tkilSCnixstCR2DRy7Rg%2BujbJqFcJ6dSfg8f6XRAb8Wgzw%2FjdkI2gNdslXfjO0ZlNC1xnZ%2FIGFWRJkSV4jhTuOikLqsuGfFj4C9p%2B2y0liSM6oUmIsEa7Zdj2O%2BgB4ZagpX2YXh8qqAfK%2B7FMMitmTIAWFXUe8E0FUpffMwpKu30wY6mAGSxPLtRVSSGdjB6k9aON0av0%2BhS35aOCirM4MIV5SGJSmkgLActfBMGfAC%2BbKnf%2BeIZ2RKIJ5eC2Hr7y%2F8BPkdiue2ogCAV42cukZdRz2duSHBEp3FIWRde8BclsZA3nPsr8Z618mg2Hg93LCI8I6IsWW%2FzCbz%2FzEW0mEAej9V4njHN5qXwBiZ9tO8vEcQ0xjvmQPL8yogzw%3D%3D&Expires=1785586551) - Project mC — VibeGuard Current Patent Verification — Independent Deep Research

Role

Act as an inde...

2. [04_Phase3C_VibeGuard_Architecture_Report_Final.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/144580388/626361f5-c189-477b-9ced-8e5489c0225a/04_Phase3C_VibeGuard_Architecture_Report_Final.md?AWSAccessKeyId=ASIA2F3EMEYE3EDXHSKO&Signature=JEIDAVGQfoXpjg3X1u1yavIjcuc%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQCSwumtw0icCRuB%2FTg5Kc9iXqLGjvemNYVtECiGlyG5ngIgdBdvQiJVnNcXeEebwj6kkIsLNP9JpWQtKILofhG0Eq0q%2FAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDKmF3l5FEdGfj4NQUirQBJXUWLC%2FDKrifxGPxd%2B7Lroe0B7V9X7ZCfAk%2BQiH5z5DJGgUcFlorBJnii6EwM9sQi9ifEfpdRLY2zJkbDt95CP8RRIdukZB8m6b0n277PX2GJqRS8sXzCAWv%2FtLZf%2FVQ%2BoH2Dpu%2FkCNFqYDsYUN71yoBy3lak5R7FsrV5FUAsKFPHbcmuRitn6zjHRKtojh3VJIZMl%2BoCjTrRzqDLiFJ78ZkES6vuG58teikYUN%2FTPVJiwqN0eiy4K1PWhTIz6yCo%2B8J9zMjIsukX%2B8s1wBLPzNIMOdWpEDiOjQo3bB%2F9oVuKxWdaKeXJfXcyW6%2BO8ndDCcgryq%2BTW47z2HDm%2BpEwFVdbV%2FeYlz1Yi5YULkAbTmn9a2X9S0IAJ4wWw3BM97luXXZTzPq28UbwA%2BX4pV7EvWgj1eV13NPf6zmGvzl6jan7B16NZfnzYadl9xaqFwjQNbOWLE0AH8LPMp0JtN%2Fv1pnAIZORYTzBnRpiHd0cwkXABgWCXzhTTVl0Zshw9lG5l5ZsWfTrmBvJDrgY%2BBGjdosY1PtI35XXDib%2FEQh%2F%2B%2FdsrP0kV75AFCk779yQp8RP0F81eQRbm5%2BBxrSklqUrmdvE%2Bq4T5HGwOXRXiA7k%2Bl6pcH4tkilSCnixstCR2DRy7Rg%2BujbJqFcJ6dSfg8f6XRAb8Wgzw%2FjdkI2gNdslXfjO0ZlNC1xnZ%2FIGFWRJkSV4jhTuOikLqsuGfFj4C9p%2B2y0liSM6oUmIsEa7Zdj2O%2BgB4ZagpX2YXh8qqAfK%2B7FMMitmTIAWFXUe8E0FUpffMwpKu30wY6mAGSxPLtRVSSGdjB6k9aON0av0%2BhS35aOCirM4MIV5SGJSmkgLActfBMGfAC%2BbKnf%2BeIZ2RKIJ5eC2Hr7y%2F8BPkdiue2ogCAV42cukZdRz2duSHBEp3FIWRde8BclsZA3nPsr8Z618mg2Hg93LCI8I6IsWW%2FzCbz%2FzEW0mEAej9V4njHN5qXwBiZ9tO8vEcQ0xjvmQPL8yogzw%3D%3D&Expires=1785586551) - Status Complete Evidence base Four independent Phase 3C Deep Research reports Gemini, Mistral, Perpl...

3. [05_Phase3C_VibeGuard_Memory_Final.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/144580388/773b0daa-d03a-45f4-ba7f-fe0e208136b1/05_Phase3C_VibeGuard_Memory_Final.md?AWSAccessKeyId=ASIA2F3EMEYE3EDXHSKO&Signature=D%2BmAy9sqzBjJ3n7eb%2Fok25lLOl0%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQCSwumtw0icCRuB%2FTg5Kc9iXqLGjvemNYVtECiGlyG5ngIgdBdvQiJVnNcXeEebwj6kkIsLNP9JpWQtKILofhG0Eq0q%2FAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDKmF3l5FEdGfj4NQUirQBJXUWLC%2FDKrifxGPxd%2B7Lroe0B7V9X7ZCfAk%2BQiH5z5DJGgUcFlorBJnii6EwM9sQi9ifEfpdRLY2zJkbDt95CP8RRIdukZB8m6b0n277PX2GJqRS8sXzCAWv%2FtLZf%2FVQ%2BoH2Dpu%2FkCNFqYDsYUN71yoBy3lak5R7FsrV5FUAsKFPHbcmuRitn6zjHRKtojh3VJIZMl%2BoCjTrRzqDLiFJ78ZkES6vuG58teikYUN%2FTPVJiwqN0eiy4K1PWhTIz6yCo%2B8J9zMjIsukX%2B8s1wBLPzNIMOdWpEDiOjQo3bB%2F9oVuKxWdaKeXJfXcyW6%2BO8ndDCcgryq%2BTW47z2HDm%2BpEwFVdbV%2FeYlz1Yi5YULkAbTmn9a2X9S0IAJ4wWw3BM97luXXZTzPq28UbwA%2BX4pV7EvWgj1eV13NPf6zmGvzl6jan7B16NZfnzYadl9xaqFwjQNbOWLE0AH8LPMp0JtN%2Fv1pnAIZORYTzBnRpiHd0cwkXABgWCXzhTTVl0Zshw9lG5l5ZsWfTrmBvJDrgY%2BBGjdosY1PtI35XXDib%2FEQh%2F%2B%2FdsrP0kV75AFCk779yQp8RP0F81eQRbm5%2BBxrSklqUrmdvE%2Bq4T5HGwOXRXiA7k%2Bl6pcH4tkilSCnixstCR2DRy7Rg%2BujbJqFcJ6dSfg8f6XRAb8Wgzw%2FjdkI2gNdslXfjO0ZlNC1xnZ%2FIGFWRJkSV4jhTuOikLqsuGfFj4C9p%2B2y0liSM6oUmIsEa7Zdj2O%2BgB4ZagpX2YXh8qqAfK%2B7FMMitmTIAWFXUe8E0FUpffMwpKu30wY6mAGSxPLtRVSSGdjB6k9aON0av0%2BhS35aOCirM4MIV5SGJSmkgLActfBMGfAC%2BbKnf%2BeIZ2RKIJ5eC2Hr7y%2F8BPkdiue2ogCAV42cukZdRz2duSHBEp3FIWRde8BclsZA3nPsr8Z618mg2Hg93LCI8I6IsWW%2FzCbz%2FzEW0mEAej9V4njHN5qXwBiZ9tO8vEcQ0xjvmQPL8yogzw%3D%3D&Expires=1785586551) - Version 1.0 Status COMPLETE Methodology Version Phase 3C --- TITLE Project mC - Phase 3C Memory Vibe...

4. [09_Patent_Research_Input_Pack.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/144580388/f199564a-054a-4fa4-80a6-db0bb0f8b1bb/09_Patent_Research_Input_Pack.md?AWSAccessKeyId=ASIA2F3EMEYE3EDXHSKO&Signature=W660pODmVATwxpsxlIGjgj97hp8%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQCSwumtw0icCRuB%2FTg5Kc9iXqLGjvemNYVtECiGlyG5ngIgdBdvQiJVnNcXeEebwj6kkIsLNP9JpWQtKILofhG0Eq0q%2FAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDKmF3l5FEdGfj4NQUirQBJXUWLC%2FDKrifxGPxd%2B7Lroe0B7V9X7ZCfAk%2BQiH5z5DJGgUcFlorBJnii6EwM9sQi9ifEfpdRLY2zJkbDt95CP8RRIdukZB8m6b0n277PX2GJqRS8sXzCAWv%2FtLZf%2FVQ%2BoH2Dpu%2FkCNFqYDsYUN71yoBy3lak5R7FsrV5FUAsKFPHbcmuRitn6zjHRKtojh3VJIZMl%2BoCjTrRzqDLiFJ78ZkES6vuG58teikYUN%2FTPVJiwqN0eiy4K1PWhTIz6yCo%2B8J9zMjIsukX%2B8s1wBLPzNIMOdWpEDiOjQo3bB%2F9oVuKxWdaKeXJfXcyW6%2BO8ndDCcgryq%2BTW47z2HDm%2BpEwFVdbV%2FeYlz1Yi5YULkAbTmn9a2X9S0IAJ4wWw3BM97luXXZTzPq28UbwA%2BX4pV7EvWgj1eV13NPf6zmGvzl6jan7B16NZfnzYadl9xaqFwjQNbOWLE0AH8LPMp0JtN%2Fv1pnAIZORYTzBnRpiHd0cwkXABgWCXzhTTVl0Zshw9lG5l5ZsWfTrmBvJDrgY%2BBGjdosY1PtI35XXDib%2FEQh%2F%2B%2FdsrP0kV75AFCk779yQp8RP0F81eQRbm5%2BBxrSklqUrmdvE%2Bq4T5HGwOXRXiA7k%2Bl6pcH4tkilSCnixstCR2DRy7Rg%2BujbJqFcJ6dSfg8f6XRAb8Wgzw%2FjdkI2gNdslXfjO0ZlNC1xnZ%2FIGFWRJkSV4jhTuOikLqsuGfFj4C9p%2B2y0liSM6oUmIsEa7Zdj2O%2BgB4ZagpX2YXh8qqAfK%2B7FMMitmTIAWFXUe8E0FUpffMwpKu30wY6mAGSxPLtRVSSGdjB6k9aON0av0%2BhS35aOCirM4MIV5SGJSmkgLActfBMGfAC%2BbKnf%2BeIZ2RKIJ5eC2Hr7y%2F8BPkdiue2ogCAV42cukZdRz2duSHBEp3FIWRde8BclsZA3nPsr8Z618mg2Hg93LCI8I6IsWW%2FzCbz%2FzEW0mEAej9V4njHN5qXwBiZ9tO8vEcQ0xjvmQPL8yogzw%3D%3D&Expires=1785586551) - This pack preparesnot performsa later current patent search. Historical repository conclusions below...

5. [ABNORMALITY DETECTING APPARATUS, ROTATING MACHINE, ABNORMALITY DETECTION METHOD, AND NON-TRANSITORY COMPUTER READABLE MEDIUM](https://www.perplexity.ai/rest/file-repository/patents/US20200285531A1?lens_id=037-492-234-368-016) - publication_number: US20200285531A1
assignee: MITSUBISHI HEAVY INDUSTRIES LTD
abstract: ...of an abn...

6. [Abnormality detecting apparatus, rotating machine, abnormality detection method, and non- transitory computer readable medium](https://www.perplexity.ai/rest/file-repository/patents/US11334414B2?lens_id=160-292-331-312-084) - publication_number: US11334414B2
assignee: MITSUBISHI HEAVY INDUSTRIES LTD
abstract: ...abnormality ...

7. [VIBRATION ANALYSIS SYSTEM AND VIBRATION ANALYSIS METHOD](https://www.perplexity.ai/rest/file-repository/patents/US20230332979A1?lens_id=054-088-140-763-869) - publication_number: US20230332979A1
assignee: VALQUA LTD
abstract: A vibration analysis system inclu...

8. [METHOD AND APPARATUS FOR MONITORING AND ANALYZING VIBRATIONS IN ROTARY MACHINES](https://www.perplexity.ai/rest/file-repository/patents/WO2010094915A1?lens_id=185-483-229-482-369) - publication_number: WO2010094915A1
abstract: A method of monitoring vibration amplitude and frequenc...

9. [METHOD AND APPARATUS FOR MONITORING AND ANALYZING VIBRATIONS IN ROTARY MACHINES](https://www.perplexity.ai/rest/file-repository/patents/US20120035885A1?lens_id=093-292-459-117-925) - publication_number: US20120035885A1
assignee: ROLLS-ROYCE CONTROLS AND DATA SERVICES LIMITED, OPTIMI...

10. [METHOD FOR RESONANCE ANALYSIS OF A VIBRATION MACHINE](https://www.perplexity.ai/rest/file-repository/patents/US20240369403A1?lens_id=136-559-633-210-550) - publication_number: US20240369403A1
assignee: SANDVIK ROCK PROCESSING AUSTRALIA PTY LIMITED
abstract...

11. [02_Project_mC_Decision_Register_v1.2.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/144580388/0d4d0162-dd91-4800-8219-58a0c74b2ba4/02_Project_mC_Decision_Register_v1.2.md?AWSAccessKeyId=ASIA2F3EMEYE3EDXHSKO&Signature=6%2B9wtcEYMKBuBC68ZztS%2Bsk4csM%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQCSwumtw0icCRuB%2FTg5Kc9iXqLGjvemNYVtECiGlyG5ngIgdBdvQiJVnNcXeEebwj6kkIsLNP9JpWQtKILofhG0Eq0q%2FAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDKmF3l5FEdGfj4NQUirQBJXUWLC%2FDKrifxGPxd%2B7Lroe0B7V9X7ZCfAk%2BQiH5z5DJGgUcFlorBJnii6EwM9sQi9ifEfpdRLY2zJkbDt95CP8RRIdukZB8m6b0n277PX2GJqRS8sXzCAWv%2FtLZf%2FVQ%2BoH2Dpu%2FkCNFqYDsYUN71yoBy3lak5R7FsrV5FUAsKFPHbcmuRitn6zjHRKtojh3VJIZMl%2BoCjTrRzqDLiFJ78ZkES6vuG58teikYUN%2FTPVJiwqN0eiy4K1PWhTIz6yCo%2B8J9zMjIsukX%2B8s1wBLPzNIMOdWpEDiOjQo3bB%2F9oVuKxWdaKeXJfXcyW6%2BO8ndDCcgryq%2BTW47z2HDm%2BpEwFVdbV%2FeYlz1Yi5YULkAbTmn9a2X9S0IAJ4wWw3BM97luXXZTzPq28UbwA%2BX4pV7EvWgj1eV13NPf6zmGvzl6jan7B16NZfnzYadl9xaqFwjQNbOWLE0AH8LPMp0JtN%2Fv1pnAIZORYTzBnRpiHd0cwkXABgWCXzhTTVl0Zshw9lG5l5ZsWfTrmBvJDrgY%2BBGjdosY1PtI35XXDib%2FEQh%2F%2B%2FdsrP0kV75AFCk779yQp8RP0F81eQRbm5%2BBxrSklqUrmdvE%2Bq4T5HGwOXRXiA7k%2Bl6pcH4tkilSCnixstCR2DRy7Rg%2BujbJqFcJ6dSfg8f6XRAb8Wgzw%2FjdkI2gNdslXfjO0ZlNC1xnZ%2FIGFWRJkSV4jhTuOikLqsuGfFj4C9p%2B2y0liSM6oUmIsEa7Zdj2O%2BgB4ZagpX2YXh8qqAfK%2B7FMMitmTIAWFXUe8E0FUpffMwpKu30wY6mAGSxPLtRVSSGdjB6k9aON0av0%2BhS35aOCirM4MIV5SGJSmkgLActfBMGfAC%2BbKnf%2BeIZ2RKIJ5eC2Hr7y%2F8BPkdiue2ogCAV42cukZdRz2duSHBEp3FIWRde8BclsZA3nPsr8Z618mg2Hg93LCI8I6IsWW%2FzCbz%2FzEW0mEAej9V4njHN5qXwBiZ9tO8vEcQ0xjvmQPL8yogzw%3D%3D&Expires=1785586551) - ### Project mC Decision Register — Version 1.2

**Document Control Header**
*   **Version:** 1.2
*  ...

12. [01_Engineering_Design_Review.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/144580388/57beef0f-8d90-4297-87c1-f37b569fe913/01_Engineering_Design_Review.md?AWSAccessKeyId=ASIA2F3EMEYE3EDXHSKO&Signature=BJGEf2PZE0PaAUo4KR3v03kTzfk%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQCSwumtw0icCRuB%2FTg5Kc9iXqLGjvemNYVtECiGlyG5ngIgdBdvQiJVnNcXeEebwj6kkIsLNP9JpWQtKILofhG0Eq0q%2FAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDKmF3l5FEdGfj4NQUirQBJXUWLC%2FDKrifxGPxd%2B7Lroe0B7V9X7ZCfAk%2BQiH5z5DJGgUcFlorBJnii6EwM9sQi9ifEfpdRLY2zJkbDt95CP8RRIdukZB8m6b0n277PX2GJqRS8sXzCAWv%2FtLZf%2FVQ%2BoH2Dpu%2FkCNFqYDsYUN71yoBy3lak5R7FsrV5FUAsKFPHbcmuRitn6zjHRKtojh3VJIZMl%2BoCjTrRzqDLiFJ78ZkES6vuG58teikYUN%2FTPVJiwqN0eiy4K1PWhTIz6yCo%2B8J9zMjIsukX%2B8s1wBLPzNIMOdWpEDiOjQo3bB%2F9oVuKxWdaKeXJfXcyW6%2BO8ndDCcgryq%2BTW47z2HDm%2BpEwFVdbV%2FeYlz1Yi5YULkAbTmn9a2X9S0IAJ4wWw3BM97luXXZTzPq28UbwA%2BX4pV7EvWgj1eV13NPf6zmGvzl6jan7B16NZfnzYadl9xaqFwjQNbOWLE0AH8LPMp0JtN%2Fv1pnAIZORYTzBnRpiHd0cwkXABgWCXzhTTVl0Zshw9lG5l5ZsWfTrmBvJDrgY%2BBGjdosY1PtI35XXDib%2FEQh%2F%2B%2FdsrP0kV75AFCk779yQp8RP0F81eQRbm5%2BBxrSklqUrmdvE%2Bq4T5HGwOXRXiA7k%2Bl6pcH4tkilSCnixstCR2DRy7Rg%2BujbJqFcJ6dSfg8f6XRAb8Wgzw%2FjdkI2gNdslXfjO0ZlNC1xnZ%2FIGFWRJkSV4jhTuOikLqsuGfFj4C9p%2B2y0liSM6oUmIsEa7Zdj2O%2BgB4ZagpX2YXh8qqAfK%2B7FMMitmTIAWFXUe8E0FUpffMwpKu30wY6mAGSxPLtRVSSGdjB6k9aON0av0%2BhS35aOCirM4MIV5SGJSmkgLActfBMGfAC%2BbKnf%2BeIZ2RKIJ5eC2Hr7y%2F8BPkdiue2ogCAV42cukZdRz2duSHBEp3FIWRde8BclsZA3nPsr8Z618mg2Hg93LCI8I6IsWW%2FzCbz%2FzEW0mEAej9V4njHN5qXwBiZ9tO8vEcQ0xjvmQPL8yogzw%3D%3D&Expires=1785586551) - Engineering Design Review Overview Purpose The Engineering Design Review EDR serves as the transitio...

13. [03_Phase3C_Portfolio_Closure_Memo_Approved.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/144580388/7130a352-7c3f-4e60-9906-89e640872cde/03_Phase3C_Portfolio_Closure_Memo_Approved.md?AWSAccessKeyId=ASIA2F3EMEYE3EDXHSKO&Signature=84UhEh4tYW03YcVKygsOTJZSLSs%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQCSwumtw0icCRuB%2FTg5Kc9iXqLGjvemNYVtECiGlyG5ngIgdBdvQiJVnNcXeEebwj6kkIsLNP9JpWQtKILofhG0Eq0q%2FAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDKmF3l5FEdGfj4NQUirQBJXUWLC%2FDKrifxGPxd%2B7Lroe0B7V9X7ZCfAk%2BQiH5z5DJGgUcFlorBJnii6EwM9sQi9ifEfpdRLY2zJkbDt95CP8RRIdukZB8m6b0n277PX2GJqRS8sXzCAWv%2FtLZf%2FVQ%2BoH2Dpu%2FkCNFqYDsYUN71yoBy3lak5R7FsrV5FUAsKFPHbcmuRitn6zjHRKtojh3VJIZMl%2BoCjTrRzqDLiFJ78ZkES6vuG58teikYUN%2FTPVJiwqN0eiy4K1PWhTIz6yCo%2B8J9zMjIsukX%2B8s1wBLPzNIMOdWpEDiOjQo3bB%2F9oVuKxWdaKeXJfXcyW6%2BO8ndDCcgryq%2BTW47z2HDm%2BpEwFVdbV%2FeYlz1Yi5YULkAbTmn9a2X9S0IAJ4wWw3BM97luXXZTzPq28UbwA%2BX4pV7EvWgj1eV13NPf6zmGvzl6jan7B16NZfnzYadl9xaqFwjQNbOWLE0AH8LPMp0JtN%2Fv1pnAIZORYTzBnRpiHd0cwkXABgWCXzhTTVl0Zshw9lG5l5ZsWfTrmBvJDrgY%2BBGjdosY1PtI35XXDib%2FEQh%2F%2B%2FdsrP0kV75AFCk779yQp8RP0F81eQRbm5%2BBxrSklqUrmdvE%2Bq4T5HGwOXRXiA7k%2Bl6pcH4tkilSCnixstCR2DRy7Rg%2BujbJqFcJ6dSfg8f6XRAb8Wgzw%2FjdkI2gNdslXfjO0ZlNC1xnZ%2FIGFWRJkSV4jhTuOikLqsuGfFj4C9p%2B2y0liSM6oUmIsEa7Zdj2O%2BgB4ZagpX2YXh8qqAfK%2B7FMMitmTIAWFXUe8E0FUpffMwpKu30wY6mAGSxPLtRVSSGdjB6k9aON0av0%2BhS35aOCirM4MIV5SGJSmkgLActfBMGfAC%2BbKnf%2BeIZ2RKIJ5eC2Hr7y%2F8BPkdiue2ogCAV42cukZdRz2duSHBEp3FIWRde8BclsZA3nPsr8Z618mg2Hg93LCI8I6IsWW%2FzCbz%2FzEW0mEAej9V4njHN5qXwBiZ9tO8vEcQ0xjvmQPL8yogzw%3D%3D&Expires=1785586551) - # Project mC — Phase 3C Retained-Portfolio Closure Memo

**Version:** 1.0
**Date:** 27 July 2026  ...

14. [06_Phase3C_VibeGuard_SOP_Final.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/144580388/1e5f2ecf-8d85-4c2c-bec5-0a81d4e402c9/06_Phase3C_VibeGuard_SOP_Final.md?AWSAccessKeyId=ASIA2F3EMEYE3EDXHSKO&Signature=zX4gQMJkLMimKZLvgQoaysabWoc%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQCSwumtw0icCRuB%2FTg5Kc9iXqLGjvemNYVtECiGlyG5ngIgdBdvQiJVnNcXeEebwj6kkIsLNP9JpWQtKILofhG0Eq0q%2FAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDKmF3l5FEdGfj4NQUirQBJXUWLC%2FDKrifxGPxd%2B7Lroe0B7V9X7ZCfAk%2BQiH5z5DJGgUcFlorBJnii6EwM9sQi9ifEfpdRLY2zJkbDt95CP8RRIdukZB8m6b0n277PX2GJqRS8sXzCAWv%2FtLZf%2FVQ%2BoH2Dpu%2FkCNFqYDsYUN71yoBy3lak5R7FsrV5FUAsKFPHbcmuRitn6zjHRKtojh3VJIZMl%2BoCjTrRzqDLiFJ78ZkES6vuG58teikYUN%2FTPVJiwqN0eiy4K1PWhTIz6yCo%2B8J9zMjIsukX%2B8s1wBLPzNIMOdWpEDiOjQo3bB%2F9oVuKxWdaKeXJfXcyW6%2BO8ndDCcgryq%2BTW47z2HDm%2BpEwFVdbV%2FeYlz1Yi5YULkAbTmn9a2X9S0IAJ4wWw3BM97luXXZTzPq28UbwA%2BX4pV7EvWgj1eV13NPf6zmGvzl6jan7B16NZfnzYadl9xaqFwjQNbOWLE0AH8LPMp0JtN%2Fv1pnAIZORYTzBnRpiHd0cwkXABgWCXzhTTVl0Zshw9lG5l5ZsWfTrmBvJDrgY%2BBGjdosY1PtI35XXDib%2FEQh%2F%2B%2FdsrP0kV75AFCk779yQp8RP0F81eQRbm5%2BBxrSklqUrmdvE%2Bq4T5HGwOXRXiA7k%2Bl6pcH4tkilSCnixstCR2DRy7Rg%2BujbJqFcJ6dSfg8f6XRAb8Wgzw%2FjdkI2gNdslXfjO0ZlNC1xnZ%2FIGFWRJkSV4jhTuOikLqsuGfFj4C9p%2B2y0liSM6oUmIsEa7Zdj2O%2BgB4ZagpX2YXh8qqAfK%2B7FMMitmTIAWFXUe8E0FUpffMwpKu30wY6mAGSxPLtRVSSGdjB6k9aON0av0%2BhS35aOCirM4MIV5SGJSmkgLActfBMGfAC%2BbKnf%2BeIZ2RKIJ5eC2Hr7y%2F8BPkdiue2ogCAV42cukZdRz2duSHBEp3FIWRde8BclsZA3nPsr8Z618mg2Hg93LCI8I6IsWW%2FzCbz%2FzEW0mEAej9V4njHN5qXwBiZ9tO8vEcQ0xjvmQPL8yogzw%3D%3D&Expires=1785586551) - # Phase 3C — VibeGuard Architecture Definition & Engineering Selection

## Standard Operating Proced...

15. [07_Concept_Evidence_Matrix.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/144580388/e2bb1406-492e-49a5-8441-bdd5119ef95d/07_Concept_Evidence_Matrix.md?AWSAccessKeyId=ASIA2F3EMEYE3EDXHSKO&Signature=Latog9x5ra8TEKtXMp3kHuPTSUQ%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQCSwumtw0icCRuB%2FTg5Kc9iXqLGjvemNYVtECiGlyG5ngIgdBdvQiJVnNcXeEebwj6kkIsLNP9JpWQtKILofhG0Eq0q%2FAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDKmF3l5FEdGfj4NQUirQBJXUWLC%2FDKrifxGPxd%2B7Lroe0B7V9X7ZCfAk%2BQiH5z5DJGgUcFlorBJnii6EwM9sQi9ifEfpdRLY2zJkbDt95CP8RRIdukZB8m6b0n277PX2GJqRS8sXzCAWv%2FtLZf%2FVQ%2BoH2Dpu%2FkCNFqYDsYUN71yoBy3lak5R7FsrV5FUAsKFPHbcmuRitn6zjHRKtojh3VJIZMl%2BoCjTrRzqDLiFJ78ZkES6vuG58teikYUN%2FTPVJiwqN0eiy4K1PWhTIz6yCo%2B8J9zMjIsukX%2B8s1wBLPzNIMOdWpEDiOjQo3bB%2F9oVuKxWdaKeXJfXcyW6%2BO8ndDCcgryq%2BTW47z2HDm%2BpEwFVdbV%2FeYlz1Yi5YULkAbTmn9a2X9S0IAJ4wWw3BM97luXXZTzPq28UbwA%2BX4pV7EvWgj1eV13NPf6zmGvzl6jan7B16NZfnzYadl9xaqFwjQNbOWLE0AH8LPMp0JtN%2Fv1pnAIZORYTzBnRpiHd0cwkXABgWCXzhTTVl0Zshw9lG5l5ZsWfTrmBvJDrgY%2BBGjdosY1PtI35XXDib%2FEQh%2F%2B%2FdsrP0kV75AFCk779yQp8RP0F81eQRbm5%2BBxrSklqUrmdvE%2Bq4T5HGwOXRXiA7k%2Bl6pcH4tkilSCnixstCR2DRy7Rg%2BujbJqFcJ6dSfg8f6XRAb8Wgzw%2FjdkI2gNdslXfjO0ZlNC1xnZ%2FIGFWRJkSV4jhTuOikLqsuGfFj4C9p%2B2y0liSM6oUmIsEa7Zdj2O%2BgB4ZagpX2YXh8qqAfK%2B7FMMitmTIAWFXUe8E0FUpffMwpKu30wY6mAGSxPLtRVSSGdjB6k9aON0av0%2BhS35aOCirM4MIV5SGJSmkgLActfBMGfAC%2BbKnf%2BeIZ2RKIJ5eC2Hr7y%2F8BPkdiue2ogCAV42cukZdRz2duSHBEp3FIWRde8BclsZA3nPsr8Z618mg2Hg93LCI8I6IsWW%2FzCbz%2FzEW0mEAej9V4njHN5qXwBiZ9tO8vEcQ0xjvmQPL8yogzw%3D%3D&Expires=1785586551) - This is a neutral extraction, not an evaluation. Each cell gives the evidence, then source location ...

16. [08_Uncertainty_and_Test_Register.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/144580388/c9fbe340-696b-4e9f-8ffb-dd4877df5e35/08_Uncertainty_and_Test_Register.md?AWSAccessKeyId=ASIA2F3EMEYE3EDXHSKO&Signature=z%2BrIElegS6Kn3h%2BEGI32pyAUAyw%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQCSwumtw0icCRuB%2FTg5Kc9iXqLGjvemNYVtECiGlyG5ngIgdBdvQiJVnNcXeEebwj6kkIsLNP9JpWQtKILofhG0Eq0q%2FAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDKmF3l5FEdGfj4NQUirQBJXUWLC%2FDKrifxGPxd%2B7Lroe0B7V9X7ZCfAk%2BQiH5z5DJGgUcFlorBJnii6EwM9sQi9ifEfpdRLY2zJkbDt95CP8RRIdukZB8m6b0n277PX2GJqRS8sXzCAWv%2FtLZf%2FVQ%2BoH2Dpu%2FkCNFqYDsYUN71yoBy3lak5R7FsrV5FUAsKFPHbcmuRitn6zjHRKtojh3VJIZMl%2BoCjTrRzqDLiFJ78ZkES6vuG58teikYUN%2FTPVJiwqN0eiy4K1PWhTIz6yCo%2B8J9zMjIsukX%2B8s1wBLPzNIMOdWpEDiOjQo3bB%2F9oVuKxWdaKeXJfXcyW6%2BO8ndDCcgryq%2BTW47z2HDm%2BpEwFVdbV%2FeYlz1Yi5YULkAbTmn9a2X9S0IAJ4wWw3BM97luXXZTzPq28UbwA%2BX4pV7EvWgj1eV13NPf6zmGvzl6jan7B16NZfnzYadl9xaqFwjQNbOWLE0AH8LPMp0JtN%2Fv1pnAIZORYTzBnRpiHd0cwkXABgWCXzhTTVl0Zshw9lG5l5ZsWfTrmBvJDrgY%2BBGjdosY1PtI35XXDib%2FEQh%2F%2B%2FdsrP0kV75AFCk779yQp8RP0F81eQRbm5%2BBxrSklqUrmdvE%2Bq4T5HGwOXRXiA7k%2Bl6pcH4tkilSCnixstCR2DRy7Rg%2BujbJqFcJ6dSfg8f6XRAb8Wgzw%2FjdkI2gNdslXfjO0ZlNC1xnZ%2FIGFWRJkSV4jhTuOikLqsuGfFj4C9p%2B2y0liSM6oUmIsEa7Zdj2O%2BgB4ZagpX2YXh8qqAfK%2B7FMMitmTIAWFXUe8E0FUpffMwpKu30wY6mAGSxPLtRVSSGdjB6k9aON0av0%2BhS35aOCirM4MIV5SGJSmkgLActfBMGfAC%2BbKnf%2BeIZ2RKIJ5eC2Hr7y%2F8BPkdiue2ogCAV42cukZdRz2duSHBEp3FIWRde8BclsZA3nPsr8Z618mg2Hg93LCI8I6IsWW%2FzCbz%2FzEW0mEAej9V4njHN5qXwBiZ9tO8vEcQ0xjvmQPL8yogzw%3D%3D&Expires=1785586551) - # Uncertainty and Test Register

## Use

Costs and durations are approximate planning values bounded...

17. [10_Phase2_Report_by_Claude.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/144580388/42bfd6dc-db88-4ddf-91f1-f24e7cc1a62d/10_Phase2_Report_by_Claude.md?AWSAccessKeyId=ASIA2F3EMEYE3EDXHSKO&Signature=0VgyUgyyVanHHQ%2Bc0t2eRcHMn%2Fg%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQCSwumtw0icCRuB%2FTg5Kc9iXqLGjvemNYVtECiGlyG5ngIgdBdvQiJVnNcXeEebwj6kkIsLNP9JpWQtKILofhG0Eq0q%2FAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDKmF3l5FEdGfj4NQUirQBJXUWLC%2FDKrifxGPxd%2B7Lroe0B7V9X7ZCfAk%2BQiH5z5DJGgUcFlorBJnii6EwM9sQi9ifEfpdRLY2zJkbDt95CP8RRIdukZB8m6b0n277PX2GJqRS8sXzCAWv%2FtLZf%2FVQ%2BoH2Dpu%2FkCNFqYDsYUN71yoBy3lak5R7FsrV5FUAsKFPHbcmuRitn6zjHRKtojh3VJIZMl%2BoCjTrRzqDLiFJ78ZkES6vuG58teikYUN%2FTPVJiwqN0eiy4K1PWhTIz6yCo%2B8J9zMjIsukX%2B8s1wBLPzNIMOdWpEDiOjQo3bB%2F9oVuKxWdaKeXJfXcyW6%2BO8ndDCcgryq%2BTW47z2HDm%2BpEwFVdbV%2FeYlz1Yi5YULkAbTmn9a2X9S0IAJ4wWw3BM97luXXZTzPq28UbwA%2BX4pV7EvWgj1eV13NPf6zmGvzl6jan7B16NZfnzYadl9xaqFwjQNbOWLE0AH8LPMp0JtN%2Fv1pnAIZORYTzBnRpiHd0cwkXABgWCXzhTTVl0Zshw9lG5l5ZsWfTrmBvJDrgY%2BBGjdosY1PtI35XXDib%2FEQh%2F%2B%2FdsrP0kV75AFCk779yQp8RP0F81eQRbm5%2BBxrSklqUrmdvE%2Bq4T5HGwOXRXiA7k%2Bl6pcH4tkilSCnixstCR2DRy7Rg%2BujbJqFcJ6dSfg8f6XRAb8Wgzw%2FjdkI2gNdslXfjO0ZlNC1xnZ%2FIGFWRJkSV4jhTuOikLqsuGfFj4C9p%2B2y0liSM6oUmIsEa7Zdj2O%2BgB4ZagpX2YXh8qqAfK%2B7FMMitmTIAWFXUe8E0FUpffMwpKu30wY6mAGSxPLtRVSSGdjB6k9aON0av0%2BhS35aOCirM4MIV5SGJSmkgLActfBMGfAC%2BbKnf%2BeIZ2RKIJ5eC2Hr7y%2F8BPkdiue2ogCAV42cukZdRz2duSHBEp3FIWRde8BclsZA3nPsr8Z618mg2Hg93LCI8I6IsWW%2FzCbz%2FzEW0mEAej9V4njHN5qXwBiZ9tO8vEcQ0xjvmQPL8yogzw%3D%3D&Expires=1785586551) - # Phase 2 — Patent Landscape Assessment (Consolidated)
### MC Project · Patent-Oriented Embedded Sys...

18. [System and method for vibration monitoring of a mining machine](https://www.perplexity.ai/rest/file-repository/patents/US9903090B2?lens_id=145-451-419-947-57X) - publication_number: US9903090B2
assignee: JOY GLOBAL SURFACE MINING INC, HARNISCHFEGER TECHNOLOGIES ...

19. [Signal noise reduction by time-domain spectral subtraction](https://www.perplexity.ai/rest/file-repository/patents/US6507623B1?lens_id=012-022-308-740-391) - publication_number: US6507623B1
assignee: UNWIRED PLANET LLC, CLUSTER LLC, TELEFONAKTIEBOLAGET LM ER...

20. [Vibration spectra window enhancement](https://www.perplexity.ai/rest/file-repository/patents/US11148244B2?lens_id=136-046-334-586-108) - publication_number: US11148244B2
assignee: COMPUTATIONAL SYSTEMS INC
abstract: While monitoring the ...

21. [Vibration analysis system and vibration analysis method](https://www.perplexity.ai/rest/file-repository/patents/US12590863B2?lens_id=064-716-050-936-049) - publication_number: US12590863B2
abstract: A vibration analysis system includes: a signal input port...

22. [SIGNAL NOISE REDUCTION BY TIME-DOMAIN SPECTRAL SUBTRACTION](https://www.perplexity.ai/rest/file-repository/patents/WO2000062281A1?lens_id=059-625-250-039-102) - publication_number: WO2000062281A1
abstract: For purposes of noise suppression, spectral subtraction...

23. [ELECTRIC MACHINE HAVING AN INTEGRATED VIBRATION SENSOR](https://www.perplexity.ai/rest/file-repository/patents/US20120181965A1?lens_id=051-428-548-429-687) - publication_number: US20120181965A1
assignee: REMY TECHNOLOGIES L.L.C, BORGWARNER INC
abstract: An e...

24. [Electric machine having an integrated vibration sensor](https://www.perplexity.ai/rest/file-repository/patents/US8531147B2?lens_id=182-344-661-429-779) - publication_number: US8531147B2
assignee: REMY TECHNOLOGIES L.L.C, BORGWARNER INC
abstract: An elect...

25. [VIBRATION MONITORING SYSTEM FOR ROTARY MACHINE, AND VIBRATION MONITORING METHOD FOR ROTARY MACHINE](https://www.perplexity.ai/rest/file-repository/patents/US20240295432A1?lens_id=103-600-768-860-344) - publication_number: US20240295432A1
assignee: EBARA CORPORATION
abstract: The present application re...

26. [VIBRATION-MONITORING SYSTEM FOR ROTATING MACHINE, AND VIBRATION-MONITORING METHOD FOR ROTATING MACHINE](https://www.perplexity.ai/rest/file-repository/patents/EP4361583A1?lens_id=043-354-717-503-00X) - publication_number: EP4361583A1
abstract: The present invention relates to a system and a method of ...

27. [Power efficient machine diagnostic monitoring using multiple vibration sensor wireless configuration](https://www.perplexity.ai/rest/file-repository/patents/US10551243B2?lens_id=187-321-677-432-753) - publication_number: US10551243B2
assignee: ACOEM RP, ACOEM FRANCE, 01DB-METRAVIB SOCIETE PAR ACTIONS...

28. [SYSTEM AND METHOD FOR VIBRATION MONITORING OF A MINING MACHINE](https://www.perplexity.ai/rest/file-repository/patents/US20130184927A1?lens_id=108-826-546-238-617) - publication_number: US20130184927A1
assignee: JOY GLOBAL SURFACE MINING INC, HARNISCHFEGER TECHNOLOG...

29. [METHOD FOR MEASURING VIBRATIONS OF A VIBRATION MACHINE](https://www.perplexity.ai/rest/file-repository/patents/US20250027836A1?lens_id=075-786-272-257-036) - publication_number: US20250027836A1
assignee: SANDVIK ROCK PROCESSING AUSTRALIA PTY LIMITED
abstract...

30. [Vibration monitoring apparatus](https://www.perplexity.ai/rest/file-repository/patents/US4683542A?lens_id=181-473-728-773-430) - publication_number: US4683542A
assignee: MITSUBISHI DENKI KABUSHIKI KAISHA
abstract: ...Feb. 7, 1985...

31. [Monitoring system for machine vibration](https://www.perplexity.ai/rest/file-repository/patents/US20090188323A1?lens_id=037-870-677-646-316) - publication_number: US20090188323A1
assignee: CATERPILLAR INC
abstract: A system for monitoring an e...


---

## Source 7: `03_CONCEPT_PORTFOLIO/VibeGuard/02_Raw_Research/04_VibeGuard_Patent_Research_Qwen.md`

- Authority: `TIER_3`
- Treatment: `SUPPORTING_EVIDENCE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `NEW_STAGE10I_EXTRACTION`
- SHA-256: `f3d0aa97e4f67197fed317503a2959e788d092c3af11d5b909bff344912cd561`

# Source Extraction

- Chapter: `07` — VibeGuard Patent Evidence and Future Research Path
- Authority tier: `TIER_3`
- Manual treatment: `SUPPORTING_EVIDENCE`
- Original source: `03_CONCEPT_PORTFOLIO/VibeGuard/02_Raw_Research/04_VibeGuard_Patent_Research_Qwen.md`
- SHA-256: `f3d0aa97e4f67197fed317503a2959e788d092c3af11d5b909bff344912cd561`
- Extraction method: `PLAIN_TEXT`
- Rule: source text only; no synthesis, correction or reconciliation.

---

# VibeGuard Current Patent Verification — Independent Research

## 1. Executive verdict
**Credible path through bounded three-month enhancement.**

*   **Track Classification:** Track B (Credible path through a bounded enhancement achievable/testable within three months and ₹5,000).
*   **Confidence:** Medium-High.
*   **Most important limitation:** Single-node target-machine attribution on a dense, acoustically coupled factory floor remains empirically unvalidated and theoretically borderline; the frozen MVP's isolated bench demonstration does not prove this capability.
*   **Is the frozen MVP itself the invention?** No. The frozen MVP (ADXL345 + ESP32 + standard DSP + Mahalanobis) is a conventional aggregation of known edge-computing and condition-monitoring practices. The patentable invention, if any, resides strictly in a bounded enhancement: **Confidence-gated, mounting-aware baseline adaptation** that prevents statistical model contamination in resource-constrained, single-node deployments.

## 2. Input inventory and concept-fidelity confirmation
*   **Governing instruction file:** `00_READ_FIRST_VibeGuard_Patent_Research_Instructions.md` is readable and active.
*   **Ten canonical project documents:** All ten are present, readable, and correctly mapped within the four transport bundles:
    1.  `01_Engineering_Design_Review.md` (in Bundle 01-03)
    2.  `02_Project_mC_Decision_Register_v1.2.md` (in Bundle 01-03) — **Confirmed v1.2, not v1.1.**
    3.  `03_Phase3C_Portfolio_Closure_Memo_Approved.md` (in Bundle 01-03)
    4.  `04_Phase3C_VibeGuard_Architecture_Report_Final.md` (in Bundle 04-06)
    5.  `05_Phase3C_VibeGuard_Memory_Final.md` (in Bundle 04-06)
    6.  `06_Phase3C_VibeGuard_SOP_Final.md` (in Bundle 04-06)
    7.  `07_Concept_Evidence_Matrix.md` (in Bundle 07-09)
    8.  `08_Uncertainty_and_Test_Register.md` (in Bundle 07-09)
    9.  `09_Patent_Research_Input_Pack.md` (in Bundle 07-09)
    10. `10_Phase2_Report_by_Claude.md` (Standalone)
*   **Frozen Concept Fidelity:** Confirmed. The concept is strictly a **passive, single-node, edge-computed machine-vibration detector** (ADXL345, SPI, ESP32, local DSP, Mahalanobis, RGB alert). It is *not* active cancellation, haptics, a wearable, a multi-sensor array, or a cloud platform.
*   **Missing/Duplicate/Ambiguous Input:** None. The input set is complete and authoritative.

## 3. Search methodology and reproducible search log
*   **Databases:** USPTO Patent Public Search, WIPO PATENTSCOPE, EPO Espacenet, InPASS (Indian Patent Office), Google Patents (for family mapping and non-patent literature cross-referencing).
*   **Date of Search:** Simulated current as of 31 July 2026.
*   **CPC/IPC Classes Explored:**
    *   `G01M13/04` (Testing bearings/machine faults)
    *   `G01H17/00` (Mechanical vibration measurement)
    *   `G05B23/02` (Testing/monitoring of control systems)
    *   `G06F18/24` (Pattern recognition/classification)
    *   `G06N20/00` (Machine learning - specifically one-class/anomaly detection)
*   **Query Strings (Iterative):**
    *   `("single node" OR "single sensor") AND "vibration" AND ("attribution" OR "source isolation" OR "crosstalk")`
    *   `"spectral subtraction" AND "condition monitoring" AND "baseline"`
    *   `"Mahalanobis" AND "vibration" AND "edge" AND "anomaly"`
    *   `("mounting" OR "remounting" OR "transfer function") AND "accelerometer" AND "calibration"`
    *   `Assignee: (Infinite Uptime OR Tractian OR Augury)`

## 4. Technical and patent landscape map
The industrial Predictive Maintenance (PdM) landscape is a "red ocean" dominated by enterprise cloud platforms (Augury, Senseye, C3.ai) and high-fidelity sensor networks (Emerson, SKF).
*   **The Cloud-Tethered AI Tier:** Heavily patented. Focuses on fleet-wide data aggregation, deep learning (CNNs/Autoencoders), and prescriptive diagnostics.
*   **The Edge-DSP Tier:** Crowded with conventional RMS/FFT thresholding (ISO 10816 compliance).
*   **The Single-Node Attribution Niche:** Sparse but guarded. US Navy patents (e.g., US 7,421,349) cover advanced mathematical isolation (phase-coupling). Commercial entities (Tractian, Infinite Uptime) patent "fingerprinting" but rely on cloud-training or multi-modal sensor fusion.
*   **White Space:** Resource-constrained, single-node systems that possess *meta-cognitive awareness of their own physical deployment state* (e.g., mounting integrity, baseline contamination) to gate their own learning processes.

## 5. Verified patent-family ledger
| Assignee / Lead | Patent / Family Identifier | Status / Expiry | Core Claim Focus | Relevance to VibeGuard |
| :--- | :--- | :--- | :--- | :--- |
| **US Navy** | US 7,421,349 B1 | Active (Filed 2006) | Distinguishing fault spectral peaks from unrelated noise via sideband phase-coupling. | **High.** Directly addresses the single-node noise isolation problem, but uses computationally heavy phase math. |
| **Tractian** | BR/US/PCT Families (e.g., WO2022...) | Active / Pending | Autonomous fault detection, ML fingerprint generation, cloud-tethered model updating. | **Medium.** Covers "fingerprinting" but relies on cloud compute and multi-modal data. |
| **Infinite Uptime** | IN/US Families | Active | Edge-to-cloud PdM, specific diagnostic algorithms for SME rotating equipment. | **Medium.** Commercial collision is high; patent collision is mitigated by their cloud-dependency. |
| **Augury** | US 10,551,263 B2 (and family) | Active | Machine learning on vibration/acoustic data for automated diagnosis. | **Low/Med.** Broad ML claims, but easily bypassed by VibeGuard's unsupervised, local, non-neural approach. |
| **General DSP** | Various (Boll, etc.) | Expired / Prior Art | Spectral subtraction for noise reduction. | **High.** Baseline spectral subtraction is conventional prior art. |

## 6. Closest independent-claim analyses
**US 7,421,349 (US Navy)**
*   *Independent Claim Element:* A method for monitoring machinery comprising extracting spectral peaks, and determining phase-coupling (e.g., bispectral analysis or sideband coherence) between a fundamental frequency and the spectral peaks to reject unrelated noise.
*   *VibeGuard MVP Mapping:* VibeGuard uses FFT magnitude and Mahalanobis distance. It **does not** calculate phase-coupling or bispectra due to ESP32 compute constraints.
*   *Conclusion:* VibeGuard's base MVP does not infringe and is technically distinct, but US 7,421,349 proves that the *problem* of single-node noise rejection is known, raising the obviousness bar for any simple DSP solution.

**Tractian (Representative ML Fingerprint Claim)**
*   *Independent Claim Element:* A system comprising a sensor, a network interface, and a remote server configured to receive vibration data, extract features, and update a machine-learning fault model using fleet-wide aggregated data.
*   *VibeGuard MVP Mapping:* VibeGuard is strictly local, edge-computed, and uses unsupervised statistical distance (Mahalanobis), not fleet-trained neural networks.
*   *Conclusion:* Clear FTO. VibeGuard's "no cloud" constraint is a strong design-around for enterprise AI patents.

## 7. Frozen-MVP feature comparison
| Feature | Closest Prior Art Status | Inventive Step Contribution |
| :--- | :--- | :--- |
| ADXL345 + ESP32 Edge Node | Known / Routine IoT | None |
| DC Removal + Hann Window + FFT | Standard DSP Practice | None |
| RMS, Peak, Kurtosis Features | Standard ISO 10816 / PdM | None |
| Mahalanobis Anomaly Detection | Standard One-Class Novelty Detection | None |
| Baseline Spectral Subtraction | Known Audio/Vibration DSP | Low (Routine application) |
| **Isolated Bench Demo (Eccentric Mass)** | Standard Lab Validation | None |
| **Mounting-Aware Baseline Gating** | **Absent in low-cost edge art** | **High (Potential Track B)** |

## 8. Mandatory named-lead investigation
*   **US 7,421,349:** Verified. It solves the "neighboring machine" problem mathematically via phase. VibeGuard must solve it via *spectral band-limiting and physical proximity*, which is a different, albeit weaker, technical approach.
*   **Tractian & Infinite Uptime:** Both target the SME market. Their IP moats are built on *data aggregation* and *automated ML pipelines*. VibeGuard's zero-subscription, offline, single-node architecture deliberately steps outside their primary claim boundaries, which require network connectivity and model retraining.
*   **Augury / KCF / Senseye:** Enterprise tier. Their patents focus on multi-sensor fusion (acoustic + vibration + thermal) and cloud dashboards. VibeGuard's single-sensor, RGB-LED-only output avoids these apparatus claims.

## 9. Non-patent prior art and standards
*   **ISO 10816 / ISO 20816:** Standards for evaluating machine vibration by measurements on non-rotating parts. The MVP's RMS thresholding is a direct implementation of these standards. This is prior art and cannot be claimed.
*   **Mahalanobis Distance in SHM:** Widely published in Structural Health Monitoring (SHM) literature as a standard novelty detection metric.
*   **Spectral Subtraction:** Originating in speech enhancement (Boll, 1979), applied to vibration. Using a static baseline for subtraction is conventional.

## 10. Current frozen-MVP patent assessment
The frozen MVP, exactly as defined in the Phase 3C Architecture Report (ADXL345, SPI, ESP32, Hann, FFT, RMS/Mahalanobis, RGB LED, eccentric mass rig), **contains no credible prospective patent contribution.** It is a highly competent, well-scoped engineering prototype that aggregates known sensors, known microcontrollers, and standard DSP/statistical techniques to solve a known problem within strict budget constraints. The constraints (₹3,000, 3 months) make it a brilliant *product/academic* deliverable, but the aggregation of these specific off-the-shelf elements produces no unexpected technical synergy that would survive an obviousness rejection (e.g., *KSR v. Teleflex*).

## 11. Candidate invention-direction matrix
*(Evaluated against the 9 mandated directions. Attributes condensed for readability while retaining all required data points).*

**Direction 1: Single-node target-machine attribution under neighbouring-machine interference**
*   **Problem:** Neighboring machine crosstalk masks target faults.
*   **Contribution:** Math isolation via single sensor.
*   **Closest Art:** US 7,421,349 (Navy).
*   **Ordinary Practice?:** No, but heavily guarded by Navy patents.
*   **Track / Feasibility:** Track D / Low (Requires complex BSS, exceeds ESP32).
*   **Kill Condition:** Spectral subtraction destroys target harmonics.

**Direction 2: In-situ target fingerprint acquisition**
*   **Problem:** Baseline setup requires known states.
*   **Contribution:** Automated state mapping.
*   **Closest Art:** Tractian cloud fingerprinting.
*   **Track / Feasibility:** Track C / Medium.

**Direction 3: Guarded Spectral Subtraction**
*   **Problem:** Subtraction distortion in low SNR.
*   **Contribution:** Variance-gated bin update.
*   **Track / Feasibility:** Track B / High.

**Direction 4: Confidence-Gated Abstention (Baseline Contamination Protection)**
*   **Exact Problem:** Unsupervised anomaly detectors drift; continuous baseline updating assimilates gradual faults or sensor loosening as the "new normal."
*   **Proposed Contribution:** A meta-cognitive gating mechanism that calculates a physical coupling metric alongside statistical features, abstaining from baseline updates unless rigid mounting and high-confidence normalcy are verified.
*   **Closest Patent/NPL:** Standard ML drift correction (NPL); US 7,421,349 (noise rejection, not learning gating).
*   **Overlapping Elements:** Mahalanobis distance, baseline updating.
*   **Differentiating Elements:** Tying the software learning gate to a *physical hardware-state verification* (mechanical transfer function proxy) on a constrained edge node.
*   **Ordinary DSP/Stats?:** Baseline updating is ordinary. Combining it with a physical mounting proxy as a prerequisite gate on a sub-₹2000 node is not.
*   **Required Physical Technical Effect:** Prevents the assimilation of mechanical decoupling artifacts into the statistical model of machine health.
*   **Baseline Comparator:** Continuous unsupervised baseline updating.
*   **Experiments:** Dual-mount test (rigid vs. loose); Slow-fault injection.
*   **Hardware/Software Changes:** Software only (firmware logic addition).
*   **Compute/Memory/Latency:** Negligible (<1ms per epoch, minimal RAM).
*   **Cost:** ₹0 (software).
*   **Three-Month Feasibility:** High.
*   **Later Work:** Field validation on dense floors.
*   **Novelty/Obviousness/Eligibility/FTO Risks:** Medium / Low / Low / Low.
*   **Confidence:** Medium-High.
*   **Kill Condition:** ADXL345 noise floor is too unstable to reliably distinguish loose mount from machine fault.
*   **Track:** **Track B (Strongest Surviving Direction)**.

**Direction 5: Mounting-Transfer Compensation**
*   **Problem:** Sensor remounting alters transfer function.
*   **Contribution:** Physical coupling metric.
*   **Track / Feasibility:** Track B / High (Merged with Direction 4).

**Direction 6: Resource-aware triggered FFT**
*   **Problem:** Compute limits.
*   **Contribution:** Triggered processing.
*   **Track / Feasibility:** Track B / High, but Low Patent Potential (Routine engineering).

**Direction 7: Speed/load normalization**
*   **Problem:** Varying RPM.
*   **Contribution:** Order tracking.
*   **Track / Feasibility:** Track C / Low (Needs tach/hardware).

**Direction 8: Drift-aware adaptation**
*   **Problem:** Model decay.
*   **Contribution:** Contamination protection.
*   **Track / Feasibility:** Track B / High (Merged with Direction 4).

**Direction 9: Deployment protocol**
*   **Problem:** Ground truth.
*   **Contribution:** Source labels.
*   **Track / Feasibility:** Track C / Medium.

## 12. Strongest surviving direction
**Track B: Contamination-Protected, Mounting-Aware Baseline Updating (Confidence-Gated Abstention).**
*   **The Problem:** Unsupervised anomaly detectors (like Mahalanobis) drift. If the baseline is updated continuously, a gradual mechanical fault or a change in sensor mounting (which alters the high-frequency transfer function) will be silently learned as the "new normal," blinding the sensor.
*   **The Contribution:** A specific, resource-constrained method that calculates a *physical coupling metric* (e.g., high-frequency noise floor variance or impulse response decay) alongside the statistical features. The system *abstains* from updating the Mahalanobis baseline unless the coupling metric confirms the sensor is rigidly mounted AND the statistical confidence is exceptionally high.
*   **Why it's patentable:** It moves beyond "routine DSP" into system-level meta-cognition. It ties a software learning gate to a physical hardware-state verification, solving a specific failure mode of edge-deployed one-class classifiers.

## 13. Bench demonstration versus field-attribution evidence
*   **Level 1 (Semester Bench Demo):** One isolated motor. Normal vs. Eccentric Mass. *This validates the MVP engineering hypothesis.* It proves the ESP32 can sample, process, and classify. **It does NOT prove source attribution.**
*   **Level 2 (Patent-Oriented Attribution):** Target motor + Interfering motor on a shared rigid base. The sensor is on the Target. The Interferer is turned on/off or imbalanced. *This is required to validate the Track B/C isolation claims.*
*   **Critical Distinction:** The project must not conflate Level 1 success with Level 2 capability. A patent claim regarding "neighboring machine interference rejection" will be rejected or invalidated if supported only by Level 1 bench data.

## 14. Novelty analysis
The base MVP lacks novelty. The proposed Track B enhancement (Mounting-Aware Gated Updating) possesses novelty. While adaptive baselines are known, and mounting calibration is known in high-end industrial sensors, the specific combination of using a low-cost MEMS sensor's own high-frequency noise floor to verify mechanical coupling *as a prerequisite gate for statistical baseline updating* on a constrained MCU is not expressly disclosed in the identified prior art.

## 15. Inventive-step / obviousness analysis
*   **Risk:** An examiner may argue that combining Mahalanobis distance with a standard "confidence threshold" is obvious to a person skilled in the art of machine learning.
*   **Mitigation:** The claim must emphasize the *physical technical effect*. The gating is not merely a statistical confidence interval; it is a proxy for the *mechanical transfer function* of the sensor mount. By proving that the algorithm prevents the learning of "loose mount" artifacts as "normal machine vibration," the invention solves a specific physical measurement problem, elevating it above routine data science.

## 16. Patent-eligibility analysis
*   **US (Alice/Sec 101):** Pure mathematical algorithms (Mahalanobis, FFT) are abstract ideas. To survive Alice Step 2, the claim must be rooted in a specific improvement to the functioning of the sensor network or the machine monitoring process. Tying the algorithmic gate to the *physical mounting state* of the accelerometer provides the necessary "inventive concept" that transforms the math into a practical application.
*   **Europe (EPO):** Requires a "further technical effect." The prevention of baseline corruption due to mechanical decoupling constitutes a valid technical effect in the field of condition monitoring.
*   **India:** Software per se is excluded, but a system comprising the ESP32, the ADXL345, and the specific gating firmware embedded therein is patentable as an apparatus.

## 17. FTO risk analysis
*   **US 7,421,349:** Low Risk. VibeGuard does not use phase-coupling or bispectral analysis.
*   **Tractian / Infinite Uptime:** Low Risk. VibeGuard does not use cloud-based fleet learning or multi-modal fusion.
*   **Standard DSP:** Zero Risk. FFT, Hann windows, and RMS are public domain / expired.
*   **Conclusion:** The MVP and the Track B enhancement have a clear Freedom to Operate, provided the claims are kept narrow and avoid cloud-tethered ML language.

## 18. Claim-to-experiment map
*(Structured for the surviving Track B direction: Confidence-Gated, Mounting-Aware Baseline Updating)*

*   **Prospective Technical Element:** Physical Coupling Metric (High-frequency noise floor variance).
*   **Nearest Verified Prior Art:** High-end ICP sensor mounting calibration (routine in industrial, absent in low-cost edge).
*   **Measurable Technical Effect:** Detects sensor loosening before classification fails or baseline is corrupted.
*   **Baseline System:** Standard RMS threshold / Continuous Mahalanobis update.
*   **Proposed System:** Metric + Abstention Gate.
*   **Independent Variable:** Mount torque (rigid vs. progressively loose).
*   **Controlled Variables:** Motor speed, eccentric mass, ambient temperature.
*   **Equipment:** Dual-motor rig, torque wrench, ESP32, ADXL345.
*   **Sample/Session Count:** 50 runs per mounting state.
*   **Proposed Pre-registration Threshold:** Metric shifts >3σ from rigid baseline.
*   **Success Evidence:** Gate triggers "Abstain" on loose mount; prevents baseline corruption.
*   **Failure Evidence:** System fails to detect loose mount; assimilates loose-mount vibration as "normal".
*   **Bench Relevance:** High (Directly addresses U-VG-02).
*   **Field-Data Requirement:** Low for MVP, High for later extension.
*   **Three-Month Deliverability:** High.
*   **Later Work:** Automated remounting calibration sequences.
*   **Confidentiality Sensitivity:** High (Core algorithmic threshold).

*   **Prospective Technical Element:** Confidence-Gated Update.
*   **Nearest Verified Prior Art:** Standard ML drift correction.
*   **Measurable Technical Effect:** Prevents "creeping fault" assimilation.
*   **Baseline System:** Continuous baseline update.
*   **Proposed System:** Gated update.
*   **Independent Variable:** Fault severity (slowly increasing imbalance).
*   **Controlled Variables:** Ambient temp, interferer state.
*   **Equipment:** Eccentric mass rig.
*   **Sample/Session Count:** 30 slow-fault sequences.
*   **Proposed Pre-registration Threshold:** Baseline locks when fault > threshold.
*   **Success Evidence:** Baseline remains stable; alerts trigger correctly.
*   **Failure Evidence:** Baseline assimilates fault as "normal"; alert fails.
*   **Bench Relevance:** High.
*   **Field-Data Requirement:** Medium.
*   **Three-Month Deliverability:** High.
*   **Later Work:** Drift-rate modeling.
*   **Confidentiality Sensitivity:** High.

## 19. Three-month semester plan
*   **Month 1:** Hardware build (ADXL345 SPI to ESP32). Rigid mounting. Basic DSP pipeline (DC, Hann, FFT, RMS). Level 1 Bench Demo (Eccentric mass).
*   **Month 2:** Implement Mahalanobis baseline. Develop the "Mounting-Aware Coupling Metric" (analyzing high-frequency noise floor variance). Implement the Abstention Gate.
*   **Month 3:** Dual-motor rig construction (Level 2). Execute Claim-to-Experiment map. Ablation studies (System with Gate vs. System without Gate under loosening/interference conditions).

## 20. Later-semester or publication extension
*   **Track C (Later Extension):** Upgrade to IIS3DWB (6kHz). Perform envelope analysis for actual bearing-race spalling (high-frequency faults).
*   **Field Validation:** Deploy on a real dense-machine floor (e.g., university workshop or local SME) to gather ground-truth attribution data. This is required for a full patent filing but exceeds the 3-month/₹5,000 MVP constraint.

## 21. Budget, compute and team feasibility
*   **Budget:** ADXL345 (₹250) + ESP32 (₹450) + Rig/Misc (₹1,000) = ~₹1,700. Well below the ₹3,000 preferred / ₹5,000 absolute ceiling.
*   **Compute:** ESP32 (240MHz, FPU) easily handles 1024-point FFTs and 4x4 matrix inversions (Mahalanobis) in <10ms.
*   **Team:** 5 members. 3 CS/Cyber (DSP, Mahalanobis, Gating Logic), 1 Beginner (LED state machine, Serial logging), 1 Hardware (Rig fabrication, mounting repeatability tests). Perfectly aligned with PDR-038.

## 22. Kill criteria
*   **Kill the Patent Angle (Track B):** If the "Mounting-Aware Coupling Metric" cannot reliably distinguish between a loose sensor mount and a genuine high-frequency machine fault on the ADXL345 (due to the sensor's inherent noise floor), the Track B enhancement is unbuildable. The project reverts to a standard Track D (strong academic prototype, no patent).
*   **Kill the Attribution Claim:** If the dual-motor test shows that spectral subtraction completely destroys the target machine's fault harmonics when the interferer is active, single-node attribution is deemed infeasible for this hardware class.

## 23. Confidentiality boundary
*   **Public/Conventional:** The use of ESP32, ADXL345, FFT, RMS, and basic Mahalanobis distance.
*   **Confidential (Do not disclose in papers/hackathons prior to filing):** The exact mathematical formulation of the "Mounting-Aware Coupling Metric," the specific variance thresholds used for the Confidence-Gated Abstention, and the spectral subtraction update rules. These constitute the core of the Track B provisional patent application.

## 24. Final VibeGuard recommendation
**Advance conditionally pending named evidence.**
VibeGuard should advance as a strong semester prototype. However, its status as a "patent-first candidate" is strictly conditional upon the team successfully executing the Level 2 (Dual-Motor) bench tests in Month 3 to prove the Track B "Confidence-Gated, Mounting-Aware Baseline" enhancement. If the enhancement fails empirical testing, VibeGuard remains a highly valuable academic/engineering deliverable but must be deprioritized under the patent-first selection criterion in favor of concepts with stronger inherent apparatus claims.

## 25. Unresolved questions
1.  **Sensor Noise Floor:** Can the ADXL345's native noise floor provide a stable enough baseline to calculate a reliable "mechanical coupling metric," or is an IIS3DWB strictly required for this specific Track B invention?
2.  **Matrix Singularity:** In a resource-constrained environment, if the machine operates in a highly stable state, the covariance matrix for the Mahalanobis distance may become singular. What is the specific regularization technique (e.g., Tikhonov) the team will use on the ESP32?
3.  **Ground Truth Access:** Will the team have access to a controlled environment with two independent variable-speed motors to properly generate the Level 2 attribution dataset?

## 26. Source and verification log
*   **USPTO / EPO / WIPO:** Searched CPC G01M13/04, G01H17/00. Verified US 7,421,349 (Navy) claims regarding phase-coupling.
*   **InPASS (India):** Searched assignees "Infinite Uptime" and "Tractian". Confirmed active filings related to cloud-tethered ML and edge-cloud architectures, verifying the FTO design-around of VibeGuard's offline approach.
*   **NPL / Standards:** Verified ISO 10816/20816 as standard prior art for RMS thresholding. Verified Mahalanobis distance as standard one-class novelty detection in SHM literature.
*   **Project Authority:** Cross-referenced all findings against `Project_mC_Decision_Register_v1.2.md` (specifically PDR-023, PDR-027, PDR-028, PDR-030, PDR-038, PDR-055) and `Phase3C_VibeGuard_Architecture_Report_Final.md` to ensure strict adherence to the frozen MVP constraints. Mapped experimental requirements directly to `08_Uncertainty_and_Test_Register.md` (U-VG-01 through U-VG-07).

***
*End of Report. This document is formatted in standard Markdown and can be directly saved as `.md`, or exported to PDF/DOCX using any standard Markdown editor (e.g., Obsidian, Typora, Pandoc).*


---

## Source 8: `03_CONCEPT_PORTFOLIO/VibeGuard/02_Raw_Research/05_VibeGuard_Patent_Research_Mistral_PARTIAL_COMPILATION.md`

- Authority: `TIER_3`
- Treatment: `SUPPORTING_EVIDENCE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `NEW_STAGE10I_EXTRACTION`
- SHA-256: `2055d44aa9697572c6ef59cfe5f08780cfc8d415bba2beacb9f8f54e54510134`

# Source Extraction

- Chapter: `07` — VibeGuard Patent Evidence and Future Research Path
- Authority tier: `TIER_3`
- Manual treatment: `SUPPORTING_EVIDENCE`
- Original source: `03_CONCEPT_PORTFOLIO/VibeGuard/02_Raw_Research/05_VibeGuard_Patent_Research_Mistral_PARTIAL_COMPILATION.md`
- SHA-256: `2055d44aa9697572c6ef59cfe5f08780cfc8d415bba2beacb9f8f54e54510134`
- Extraction method: `PLAIN_TEXT`
- Rule: source text only; no synthesis, correction or reconciliation.

---

# Mistral VibeGuard Patent Research Lane — Partial Fragmented Compilation

## Mandatory reliability warning

This file is a transport compilation of three sequential Mistral outputs.

It is not a complete final independent research report.

The three source fragments must be treated as one research lane, not as three
independent reports or votes.

Known limitations:

- the first fragment identifies itself as work in progress;
- the second fragment expands the VibeGuard analysis but still leaves major
  patent, literature, legal-status, claim-analysis and final-verdict work
  unresolved;
- the third fragment is primarily a commercial-actor patent-retrieval
  appendix and does not complete the required VibeGuard report;
- no complete final Track A/B/C/D verdict should be inferred from the three
  fragments;
- missing conclusions must not be reconstructed;
- unsupported patentability, infringement or FTO conclusions must be
  independently verified or excluded;
- statements regarding Mahalanobis distance, ordinary DSP, novelty,
  patentability and infringement require especially strict re-verification.

The synthesis model must audit, downgrade or exclude unreliable portions and
use only material actually present and supportable.

## Source Fragment 1

- Original filename: `research on f.patent by mistral.pdf`
- Original absolute path: `/home/paradoxpete/Documents/PROJECT/PHASE 3/PHASE 3C-Comparative Technical Evaluation/FINAL_DOWNSELECTION/RESEAERCH/VIBEGUARD/research on f.patent by mistral.pdf`
- Original SHA-256: `9a0a142735a83a7705d2022ca4219d9232a655483028229e94a43e827f05bdaa`
- Original format: PDF; text extracted with `pdftotext -layout`
- Status: partial / work in progress

VibeGuard Patent Verification Analysis
Independent Current Patent Research as of 31 July 2026
Status: Work in Progress - Mandatory Named Leads Retrieved
Last Updated: 1 August 2026
Researcher: NPC (Building on prior model's foundation, performing independent verification)


   Executive Summary

   Completed

 • Retrieved full text of all three mandatory named lead patents:
    ◦ US 7,421,349 (Navy, Jason Stack) - Bearing fault signature detection
    ◦ US 7,346,461 B2 (NASA, Huang & Salvino) - Vibration analysis and failure signature identification
    ◦ US 11,429,900 (Tractian) - Systems and methods for automatic detection of error conditions
 • Claim-level extraction initiated for US 7,421,349 (18 claims) and US 7,346,461 (42 claims)
 • Preliminary mapping of patent elements to VibeGuard frozen architecture

   Pending

 • US 11,429,900 full claims extraction
 • Tractian patent family analysis
 • Other commercial actors (Infinite Uptime, Augury, KCF Technologies, Senseye)
 • Indian/Chinese patent database searches
 • CPC/IPC classification mapping
 • Non-patent literature verification
 • Full novelty, inventive-step, eligibility, and FTO analyses
 • Claim-to-experiment mapping

   Key Preliminary Findings

US 7,421,349 (Navy, 2008): Phase-coupled frequency-domain bearing fault detection. HIGH relevance -
establishes vibration-based fault detection as prior art.

US 7,346,461 (NASA, 2008): IMF/HHT/stability spectrum for failure signature identification. HIGH relevance -
establishes advanced vibration analysis as prior art.

US 11,429,900 (Tractian, 2022): Single-sensor vibration + remote ML processing + data compression. HIGH
relevance - commercial implementation with CRITICAL OVERLAP: Explicitly mentions Mahalanobis distance.

Preliminary Assessment: VibeGuard's edge-based approach with specific preprocessing and feature set
appears to have novel elements, but Mahalanobis-distance detection mode overlaps with US 11,429,900.

     Research Methodology
Following governing instructions from user summary. Independent verification lane - treating all historical
summaries as search leads requiring verification. Frozen VibeGuard architecture preserved.

Sources: Google Patents (primary), Justia Patents (secondary), USPTO (attempted - blocked).


     Patent Analysis: Mandatory Named Leads

1. US 7,421,349 - Bearing Fault Signature Detection

Metadata: Navy, Jason Stack, Filed 2006-05-15, Issued 2008-09-02, Expired 2026-05-15
CPC: G01H 1/00, G01H 1/003, G01M 13/04, G01M 13/045

Key Technical Teaching:

 • Fault signature model based on phase-coupled peaks: F_SB = F_CFF + m*F_S
 • Detector uses expectation operator and Fourier transform
 • Normalized detector produces peaks 0-1.0 indicating phase coupling
 • Addresses problem of coincidental frequency spacing in rich vibration spectra

18 Claims Extracted:

 • Claim 1 (Device): Fault detector with vibration measurement, fault signature model, frequency
   determination, indicator
 • Claim 6 (Method): Monitoring faults by determining frequency, measuring vibration, indicating presence
 • Dependent claims: Define specific detector functions, normalization, pattern recognition

Mapping to VibeGuard:

 •    Vibration measurement: Conventional
 •    FFT use: Conventional
 •    DC removal: Not mentioned - potentially novel
 •    Hann window: Not mentioned - potentially novel
 •    Time-domain features: Not mentioned - potential differentiation
 •    Mahalanobis: Not mentioned - potential differentiation


2. US 7,346,461 B2 - System and Method of Analyzing Vibrations

Metadata: NASA, Huang & Salvino, Filed 2005-09-30, Issued 2008-03-18, Expired 2025-09-30
CPC: G01H 1/00, G01H 1/04, G01H 1/06

Key Technical Teaching:

 • IMF extraction using Hilbert Huang Transform (HHT) and Empirical Mode Decomposition (EMD)
 • Spline fitting to envelope of most energetic IMF
 • Stability spectrum separating stable (positive) and unstable (negative) damping
 • Non-linearity indicator using TEO, NHHT, or GZC
 • Applied to aero-elastic structures (F-15B flight test data)

42 Claims:

 • Claim 1 (Method): Extracting IMFs, selecting IMF, fitting spline to envelope, determining derivative,
     developing stability spectrum

Mapping to VibeGuard:

 •     Sensors: Conventional
 •     DC removal: Not mentioned - potentially novel
 •     Hann window: Not mentioned - potentially novel
 •     Time-domain statistical features: Not mentioned - potential differentiation
 •     Triggered FFT: Not mentioned - potential differentiation


3. US 11,429,900 - Systems and Methods for Automatic Detection

Metadata: Tractian, Igor Vinicius Alvarenga Marinelli, Filed 2021-10-26, Issued 2022-08-30, Active

Key Technical Teaching:

 • Sensor device with 3-axis motion detector + data compression module
 • Remote processing device with vibration reconstruction + ML model
 • Modified DFT/FFT selects N peaks (e.g., 100) based on modulus
 • CRITICAL: Explicitly lists Mahalanobis distance as one of the ML models
 • ML models: Mahalanobis distance, normality test, decision trees, Gaussian Mixture, Neural Networks,
   Random Forest, SVM, etc.
 • Training features: RMS, MAD, peaks, normality, standard deviation, covariance, frequencies, skewness,
   kurtosis
 • Human-in-the-loop verification and continuous learning

Mapping to VibeGuard:

 •     Single-node sensor: Conventional
 •     FFT: Conventional
 •     RMS, kurtosis features: Partially conventional
 •     Edge processing: Not mentioned - VibeGuard uses ESP32 (potential differentiation)
 •     DC removal: Not mentioned - potentially novel
 •     Hann window: Not mentioned - potentially novel
 •     Mahalanobis distance: EXPLICITLY MENTIONED - OVERLAP CONFIRMED
 •     Triggered FFT: Not mentioned - potential differentiation


     VibeGuard Architecture Analysis

Frozen Architecture: ADXL345 → ESP32 → DC removal → Hann window → continuous
time-domain features (RMS, peak, SD, crest factor, kurtosis) → triggered
FFT → calibrated RMS/persistence baseline OR Mahalanobis-distance anomaly
detection → RGB LED → eccentric-mass motor/fan rig

Novelty Matrix

 Element                       US 7,421,349    US 7,346,461     US 11,429,900     Assessment

 ADXL345 Sensor                                                                   Conventional

 ESP32 (Edge)                                                                     Potentially Novel

 DC removal                                                                       Likely Novel

 Hann window                                                                      Likely Novel

 RMS Feature                                                                      Partially Conventional

 Peak Feature                                                                     Partially Conventional

 SD Feature                                                                       Likely Novel

 Crest Factor                                                                     Likely Novel

 Kurtosis                                                                         Partially Conventional

 Triggered FFT                                                                    Partially Conventional

 RMS/Persistence Baseline                                                         Likely Novel

 Mahalanobis Distance                                                             OVERLAP - NOT NOVEL

 RGB LED                                                                          Conventional

 Eccentric-Mass Rig                                                               Likely Novel


Key Differentiators

1. Edge vs. Remote Processing: ESP32 edge computation vs. remote/cloud
2. Preprocessing Pipeline: DC removal + Hann window (not in any patent)
3. Feature Set: Continuous time-domain features (SD, crest factor unique)
4. Triggered FFT: Selective computation
5. Dual Detection Modes: Baseline OR Mahalanobis
6. Test Rig: Eccentric-mass motor/fan

Critical Overlap

1. Mahalanobis Distance: Direct overlap with US 11,429,900


    Patentability Assessment

Novelty

 • Likely Novel: Edge processing, DC removal, Hann window, SD feature, crest factor, RMS/persistence
   baseline, eccentric-mass rig
 • Partially Conventional: Single-node sensor, FFT, RMS, kurtosis
 • Overlap: Mahalanobis distance with US 11,429,900

Inventive Step

 • Likely Inventive: Adapting vibration monitoring for edge devices (prior art uses complex methods or
   remote processing)
 • Potential Obviousness: Combining simple sensor with edge processing might be considered obvious, but
   specific combination may not be

Eligibility (35 U.S.C. § 101)

 • Subject Matter: Machine + Process
 • Not Abstract Idea
 • Significantly More: Physical hardware + specific implementation + technical solution
 • Conclusion: Likely eligible


   Freedom-to-Operate - CRITICAL FINDING

Mahalanobis Distance Overlap

US 11,429,900 explicitly states:


  "Any suitable type of machine learning model may be used, such as Mahalanobis distance, normality
  test, alarm values/tripvalues, decision tree..."


Implication: VibeGuard's Mahalanobis-distance anomaly detection directly infringes Tractian's patent.

Recommendations

1. Prioritize RMS/persistence baseline as primary method
2. Avoid Mahalanobis-distance or obtain license from Tractian
3. Consider alternatives: Isolation forest, one-class SVM, autoencoders
4. Focus novelty arguments on edge-based approach and preprocessing pipeline


   Immediate Next Steps

Priority 1: Complete Mandatory Leads

       US 7,421,349 - Full text + claims ✓
       US 7,346,461 - Full text ✓
       US 11,429,900 - Extract full claims to confirm Mahalanobis scope
       Tractian family - Identify all members

Priority 2: Commercial Actors

       Infinite Uptime - patents
       Augury - patents
       KCF Technologies - US 9,271,170 B1, US 10,873,791 B1
       Senseye - patents
       US 20220067020 A1 - Retrieve (Mahalanobis-specific)

Priority 3: Geographic

       InPASS (India) search
       CNIPA (China) search

Priority 4: Classification & Literature

       CPC/IPC mapping
       ISO 10816, 20964 verification
       Peer-reviewed papers

Priority 5: Advanced Analysis

       Complete novelty analysis
       Inventive step analysis
       Eligibility analysis
       Full FTO analysis
       Claim-to-experiment mapping


    Summary

 Aspect              Status            Key Finding

 Patent Retrieval       2/3 complete   All three located, US 11,429,900 claims pending

 Claim Analysis         In Progress    Preliminary mapping shows novel elements + critical overlap

 Novelty                Preliminary    Edge approach + preprocessing likely novel, Mahalanobis overlaps

 FTO                    CRITICAL       Mahalanobis-distance overlaps with US 11,429,900

 Geographic             Not Started    India/China searches needed

 Non-Patent             Not Started    ISO standards needed


Analysis based on independent verification as of 1 August 2026. All conclusions preliminary - require further
verification.


## Source Fragment 2

- Original filename: `research on f.patent by mistral 2.md`
- Original absolute path: `/home/paradoxpete/Documents/PROJECT/PHASE 3/PHASE 3C-Comparative Technical Evaluation/FINAL_DOWNSELECTION/RESEAERCH/VIBEGUARD/research on f.patent by mistral 2.md`
- Original SHA-256: `cb93eee902cc5e0bd6b6699f6d603fc8fc2830fdf27f1d7a54512f5f6c227a82`
- Original format: Markdown
- Status: expanded partial continuation

# VibeGuard Patent Verification Analysis
## Independent Current Patent Research as of 31 July 2026

**Status**: Work in Progress - Mandatory Named Leads Retrieved
**Last Updated**: 1 August 2026
**Researcher**: NPC (Building on prior model's foundation, performing independent verification)

---

## 📋 Executive Summary

### ✅ Completed
- **Retrieved full text** of all three mandatory named lead patents:
  - **US 7,421,349** (Navy, Jason Stack) - Bearing fault signature detection
  - **US 7,346,461 B2** (NASA, Huang & Salvino) - Vibration analysis and failure signature identification
  - **US 11,429,900** (Tractian) - Systems and methods for automatic detection of error conditions
- **Claim-level extraction** initiated for US 7,421,349 (18 claims) and US 7,346,461 (42 claims)
- **Preliminary mapping** of patent elements to VibeGuard frozen architecture

### ⚠️ Pending
- [ ] US 11,429,900 full claims extraction (partial - description confirms Mahalanobis)
- [ ] Tractian patent family analysis
- [ ] Other commercial actors (Infinite Uptime, Augury, Senseye)
- [x] **KCF Technologies** - US 9,271,170 B1, US 10,873,791 B1 ✓
- [x] **US 20220067020 A1** - Mahalanobis anomaly detection ✓
- [ ] Indian/Chinese patent database searches
- [ ] CPC/IPC classification mapping
- [ ] Non-patent literature verification
- [ ] Full novelty, inventive-step, eligibility, and FTO analyses
- [ ] Claim-to-experiment mapping

### 🎯 Key Preliminary Findings

**US 7,421,349 (Navy, 2008)**: Phase-coupled frequency-domain bearing fault detection. **HIGH relevance** - establishes vibration-based fault detection as prior art.

**US 7,346,461 (NASA, 2008)**: IMF/HHT/stability spectrum for failure signature identification. **HIGH relevance** - establishes advanced vibration analysis as prior art.

**US 11,429,900 (Tractian, 2022)**: Single-sensor vibration + remote ML processing + data compression. **HIGH relevance** - commercial implementation with **CRITICAL OVERLAP**: Explicitly mentions Mahalanobis distance.

**Preliminary Assessment**: VibeGuard's edge-based approach with specific preprocessing and feature set **appears to have novel elements**, but Mahalanobis-distance detection mode **overlaps with US 11,429,900**.

---

## 🔍 Research Methodology

Following governing instructions from user summary. Independent verification lane - treating all historical summaries as search leads requiring verification. Frozen VibeGuard architecture preserved.

**Sources**: Google Patents (primary), Justia Patents (secondary), USPTO (attempted - blocked).

---

## 📊 Patent Analysis: Mandatory Named Leads

### 1. US 7,421,349 - Bearing Fault Signature Detection

**Metadata**: Navy, Jason Stack, Filed 2006-05-15, Issued 2008-09-02, Expired 2026-05-15
**CPC**: G01H 1/00, G01H 1/003, G01M 13/04, G01M 13/045

**Key Technical Teaching**:
- Fault signature model based on phase-coupled peaks: F_SB = F_CFF + m*F_S
- Detector uses expectation operator and Fourier transform
- Normalized detector produces peaks 0-1.0 indicating phase coupling
- Addresses problem of coincidental frequency spacing in rich vibration spectra

**18 Claims Extracted**:
- **Claim 1** (Device): Fault detector with vibration measurement, fault signature model, frequency determination, indicator
- **Claim 6** (Method): Monitoring faults by determining frequency, measuring vibration, indicating presence
- **Dependent claims**: Define specific detector functions, normalization, pattern recognition

**Mapping to VibeGuard**:
- ✅ Vibration measurement: Conventional
- ✅ FFT use: Conventional
- ❌ DC removal: **Not mentioned - potentially novel**
- ❌ Hann window: **Not mentioned - potentially novel**
- ❌ Time-domain features: **Not mentioned - potential differentiation**
- ❌ Mahalanobis: **Not mentioned - potential differentiation**

---

### 2. US 7,346,461 B2 - System and Method of Analyzing Vibrations

**Metadata**: NASA, Huang & Salvino, Filed 2005-09-30, Issued 2008-03-18, Expired 2025-09-30
**CPC**: G01H 1/00, G01H 1/04, G01H 1/06

**Key Technical Teaching**:
- IMF extraction using Hilbert Huang Transform (HHT) and Empirical Mode Decomposition (EMD)
- Spline fitting to envelope of most energetic IMF
- Stability spectrum separating stable (positive) and unstable (negative) damping
- Non-linearity indicator using TEO, NHHT, or GZC
- Applied to aero-elastic structures (F-15B flight test data)

**42 Claims**:
- **Claim 1** (Method): Extracting IMFs, selecting IMF, fitting spline to envelope, determining derivative, developing stability spectrum

**Mapping to VibeGuard**:
- ✅ Sensors: Conventional
- ❌ DC removal: **Not mentioned - potentially novel**
- ❌ Hann window: **Not mentioned - potentially novel**
- ❌ Time-domain statistical features: **Not mentioned - potential differentiation**
- ❌ Triggered FFT: **Not mentioned - potential differentiation**

---

### 3. US 11,429,900 - Systems and Methods for Automatic Detection

**Metadata**: Tractian, Igor Vinicius Alvarenga Marinelli, Filed 2021-10-26, Issued 2022-08-30, Active

**Key Technical Teaching**:
- Sensor device with 3-axis motion detector + data compression module
- Remote processing device with vibration reconstruction + ML model
- Modified DFT/FFT selects N peaks (e.g., 100) based on modulus
- **CRITICAL**: Explicitly lists **Mahalanobis distance** as one of the ML models
- ML models: Mahalanobis distance, normality test, decision trees, Gaussian Mixture, Neural Networks, Random Forest, SVM, etc.
- Training features: RMS, MAD, peaks, normality, standard deviation, covariance, frequencies, skewness, kurtosis
- Human-in-the-loop verification and continuous learning

**Mapping to VibeGuard**:
- ✅ Single-node sensor: Conventional
- ✅ FFT: Conventional
- ✅ RMS, kurtosis features: Partially conventional
- ❌ Edge processing: **Not mentioned - VibeGuard uses ESP32 (potential differentiation)**
- ❌ DC removal: **Not mentioned - potentially novel**
- ❌ Hann window: **Not mentioned - potentially novel**
- ⚠️ **Mahalanobis distance: EXPLICITLY MENTIONED - OVERLAP CONFIRMED**
- ❌ Triggered FFT: **Not mentioned - potential differentiation**

---

## 🎯 VibeGuard Architecture Analysis

**Frozen Architecture**: `ADXL345 → ESP32 → DC removal → Hann window → continuous time-domain features (RMS, peak, SD, crest factor, kurtosis) → triggered FFT → calibrated RMS/persistence baseline OR Mahalanobis-distance anomaly detection → RGB LED → eccentric-mass motor/fan rig`

### Novelty Matrix

| Element | US 7,421,349 | US 7,346,461 | US 11,429,900 | Assessment |
|--------|--------------|--------------|--------------|------------|
| ADXL345 Sensor | ✅ | ✅ | ✅ | Conventional |
| **ESP32 (Edge)** | ⚠️ | ⚠️ | ❌ | **Potentially Novel** |
| **DC removal** | ❌ | ❌ | ❌ | **Likely Novel** |
| **Hann window** | ❌ | ❌ | ❌ | **Likely Novel** |
| RMS Feature | ❌ | ❌ | ✅ | Partially Conventional |
| Peak Feature | ❌ | ❌ | ✅ | Partially Conventional |
| **SD Feature** | ❌ | ❌ | ❌ | **Likely Novel** |
| **Crest Factor** | ❌ | ❌ | ❌ | **Likely Novel** |
| Kurtosis | ❌ | ❌ | ✅ | Partially Conventional |
| Triggered FFT | ✅ | ❌ | ✅ | Partially Conventional |
| **RMS/Persistence Baseline** | ❌ | ❌ | ❌ | **Likely Novel** |
| **Mahalanobis Distance** | ❌ | ❌ | ✅ | **OVERLAP - NOT NOVEL** |
| RGB LED | ✅ | ❌ | ✅ | Conventional |
| **Eccentric-Mass Rig** | ❌ | ❌ | ❌ | **Likely Novel** |

### Key Differentiators
1. **Edge vs. Remote Processing**: ESP32 edge computation vs. remote/cloud
2. **Preprocessing Pipeline**: DC removal + Hann window (not in any patent)
3. **Feature Set**: Continuous time-domain features (SD, crest factor unique)
4. **Triggered FFT**: Selective computation
5. **Dual Detection Modes**: Baseline OR Mahalanobis
6. **Test Rig**: Eccentric-mass motor/fan

### Critical Overlap
1. **Mahalanobis Distance**: Direct overlap with US 11,429,900

---

## 📈 Patentability Assessment

### Novelty
- **Likely Novel**: Edge processing, DC removal, Hann window, SD feature, crest factor, RMS/persistence baseline, eccentric-mass rig
- **Partially Conventional**: Single-node sensor, FFT, RMS, kurtosis
- **Overlap**: Mahalanobis distance with US 11,429,900

### Inventive Step
- **Likely Inventive**: Adapting vibration monitoring for edge devices (prior art uses complex methods or remote processing)
- **Potential Obviousness**: Combining simple sensor with edge processing *might* be considered obvious, but specific combination may not be

### Eligibility (35 U.S.C. § 101)
- **Subject Matter**: Machine + Process ✅
- **Not Abstract Idea** ✅
- **Significantly More**: Physical hardware + specific implementation + technical solution ✅
- **Conclusion**: Likely eligible

---

## 🛡️ Freedom-to-Operate - CRITICAL FINDING

### Mahalanobis Distance Overlap

**US 11,429,900 explicitly states**:
> "Any suitable type of machine learning model may be used, such as **Mahalanobis distance**, normality test, alarm values/tripvalues, decision tree..."

**Implication**: VibeGuard's Mahalanobis-distance anomaly detection **directly infringes** Tractian's patent.

### Recommendations
1. **Prioritize RMS/persistence baseline** as primary method
2. **Avoid Mahalanobis-distance** or obtain license from Tractian
3. **Consider alternatives**: Isolation forest, one-class SVM, autoencoders
4. **Focus novelty arguments** on edge-based approach and preprocessing pipeline

---

## 🎯 Immediate Next Steps

### Priority 1: Complete Mandatory Leads
- [x] US 7,421,349 - Full text + claims ✓
- [x] US 7,346,461 - Full text ✓
- [ ] US 11,429,900 - Extract **full claims** to confirm Mahalanobis scope
- [ ] Tractian family - Identify all members

### Priority 2: Commercial Actors
- [ ] Infinite Uptime - patents
- [ ] Augury - patents
- [ ] KCF Technologies - US 9,271,170 B1, US 10,873,791 B1
- [ ] Senseye - patents
- [ ] US 20220067020 A1 - Retrieve (Mahalanobis-specific)

### Priority 3: Geographic
- [ ] InPASS (India) search
- [ ] CNIPA (China) search

### Priority 4: Classification & Literature
- [ ] CPC/IPC mapping
- [ ] ISO 10816, 20964 verification
- [ ] Peer-reviewed papers

### Priority 5: Advanced Analysis
- [ ] Complete novelty analysis
- [ ] Inventive step analysis
- [ ] Eligibility analysis
- [ ] Full FTO analysis
- [ ] Claim-to-experiment mapping

---

## 📊 Additional Patent Analysis: Commercial Actors

### 4. KCF Technologies Patents

#### US 9,271,170 B1 - Channel Adaptation in Sensor Networks (2016)

**Metadata**: KCF Technologies, Loverich/Wenner/Brown, Filed 2013-03-13, Issued 2016-02-23, Active until 2034-02-15

**Focus**: RF channel adaptation for wireless sensor networks

**Key Technical Teaching**:
- Source node selects transmission states (frequency band, RF power level, data rate)
- Evaluates metrics (RSSI, packet success rate, energy in carrier band)
- Adapts to optimize energy consumption and reliability
- Sensor nodes can measure "temperature, pressure, **vibration**, strain, position, or flow rate"
- Designed for Condition Based Maintenance (CBM) applications

**Relevance to VibeGuard**:
- ⚠️ **Indirect relevance** - Mentions vibration as a measurable quantity
- Focus is on **communication infrastructure**, not vibration analysis
- Not a direct competitor to VibeGuard's analysis methods
- **Assessment**: Low overlap, different technical domain (communications vs. analysis)

---

#### US 10,873,791 B1 - Compression Method for Resource Constrained LANs (2020)

**Metadata**: KCF Technologies, Carl/Loverich, Filed 2019-07-29, Issued 2020-12-22, Active until 2039-07-29

**Focus**: Data compression for IIoT vibration sensors

**Key Technical Teaching**:
- Specifically designed for **wireless vibration sensors** in IIoT
- Uses **FFT on raw vibration signals**
- Creates **baseline from FFT magnitude data**
- Subtracts baseline from subsequent data sets
- Compresses the difference (CARL method)
- Mentions **rolling element bearing defect** as example
- Uses frequency-domain analysis to expose similarities hidden in time domain
- Operates at the **sensor node** (edge) with decompression at base station

**Relevance to VibeGuard**:
- ✅ **HIGH RELEVANCE** - Directly addresses vibration monitoring
- ✅ **FFT usage** - Similar to VibeGuard's triggered FFT
- ✅ **Baseline concept** - Similar to VibeGuard's RMS/persistence baseline
- ✅ **Edge processing** - Compression at node, decompression at base station
- ❌ **No Mahalanobis** - Uses frequency-domain differencing, not statistical anomaly detection

**Overlaps with VibeGuard**:
- FFT for vibration analysis
- Baseline approach
- Edge-based processing

**Differentiators for VibeGuard**:
- Time-domain statistical features (RMS, peak, SD, crest factor, kurtosis)
- Triggered FFT (selective vs. KCF's continuous FFT)
- Dual detection modes (baseline OR Mahalanobis)
- Specific preprocessing (DC removal, Hann window)

**Assessment**: KCF's patent is about **data compression**, while VibeGuard is about **fault detection**. Different purposes, though both use vibration sensors and FFT.

---

### 5. US 20220067020 A1 / US 11,893,004 B2 - Anomaly Detection in Multidimensional Sensor Data

**Metadata**: Ford Global Technologies, Pandey/Buss/Filev, Filed 2020-08-26, Granted 2024-02-06 (as US 11,893,004 B2), Active until 2042-10-04

**Focus**: Mahalanobis distance for real-time anomaly detection

**Key Technical Teaching**:
- Receives **time series of vectors** from a sensor
- Determines **weighted moving mean** of the vectors
- Determines **inverse covariance matrix** of the vectors
- Receives current vector from sensor
- Determines **squared Mahalanobis distance** between current vector and weighted moving mean
- **Outputs anomaly indicator** when squared Mahalanobis distance exceeds threshold
- Uses **chi-square distribution** for threshold selection
- Designed for **real-time, computationally efficient** operation
- Can be used with **accelerometers, gyroscopes, GPS, radar, LIDAR, cameras**
- Originally for autonomous vehicles, but method is general

**Relevance to VibeGuard**:
- ❌ **CRITICAL OVERLAP** - This patent is **ENTIRELY about Mahalanobis distance anomaly detection**
- Directly conflicts with VibeGuard's Mahalanobis-distance anomaly detection method
- Both use identical methodology: time series vectors → weighted moving mean → inverse covariance → squared Mahalanobis distance → threshold comparison
- Ford's patent applies to any multidimensional sensor data, including vibration

**Impact Assessment**:
- **BLOCKING PATENT** for VibeGuard's Mahalanobis-distance detection mode
- The method is explicitly disclosed and claimed
- VibeGuard **cannot use Mahalanobis distance** without licensing or designing around
- This is **separate from and additional to** the Tractian patent (US 11,429,900) which also mentions Mahalanobis

**Design-Around Options**:
1. **Avoid Mahalanobis distance entirely** - Use alternative anomaly detection methods
2. **Use VibeGuard's other mode** - Focus on RMS/persistence baseline (appears novel)
3. **Alternative statistical methods**: Isolation Forest, One-Class SVM, Autoencoders, Z-score, IQR

---

## 🎯 Updated VibeGuard Architecture Analysis

### Critical Overlaps Confirmed

| Method | US 11,429,900 (Tractian) | US 20220067020 (Ford) | Assessment |
|--------|------------------------|------------------------|------------|
| **Mahalanobis Distance** | ✅ Explicitly mentioned | ✅ **Entire patent** | **BLOCKED - Cannot use** |
| Single-node sensor | ✅ | ✅ | Conventional |
| FFT | ✅ | ❌ (uses time-series vectors) | Partially conventional |
| Baseline approach | ❌ | ❌ | Potentially novel |

### Revised Novelty Matrix

| Element | US 7,421,349 | US 7,346,461 | US 11,429,900 | US 10,873,791 | US 20220067020 | Assessment |
|--------|--------------|--------------|--------------|--------------|----------------|------------|
| ADXL345 Sensor | ✅ | ✅ | ✅ | ✅ | ✅ | Conventional |
| **ESP32 (Edge)** | ⚠️ | ⚠️ | ❌ | ✅ | ❌ | **Potentially Novel** |
| **DC removal** | ❌ | ❌ | ❌ | ❌ | ❌ | **Likely Novel** |
| **Hann window** | ❌ | ❌ | ❌ | ❌ | ❌ | **Likely Novel** |
| RMS Feature | ❌ | ❌ | ✅ | ❌ | ❌ | Partially Conventional |
| Peak Feature | ❌ | ❌ | ✅ | ❌ | ❌ | Partially Conventional |
| **SD Feature** | ❌ | ❌ | ❌ | ❌ | ❌ | **Likely Novel** |
| **Crest Factor** | ❌ | ❌ | ❌ | ❌ | ❌ | **Likely Novel** |
| Kurtosis | ❌ | ❌ | ✅ | ❌ | ❌ | Partially Conventional |
| Triggered FFT | ✅ | ❌ | ✅ | ✅ | ❌ | Partially Conventional |
| **RMS/Persistence Baseline** | ❌ | ❌ | ❌ | ✅ (similar) | ❌ | **Likely Novel** |
| **Mahalanobis Distance** | ❌ | ❌ | ✅ | ❌ | ✅ **BLOCKED** | **OVERLAP - Cannot use** |
| RGB LED | ✅ | ❌ | ✅ | ❌ | ❌ | Conventional |
| **Eccentric-Mass Rig** | ❌ | ❌ | ❌ | ❌ | ❌ | **Likely Novel** |

---

## 🛡️ Updated Freedom-to-Operate Analysis

### Mahalanobis Distance - DOUBLE CONFIRMATION

**Two separate patents now confirm Mahalanobis distance is prior art**:

1. **US 11,429,900 (Tractian, 2022)**: Lists Mahalanobis distance as one of many ML models for vibration anomaly detection
2. **US 20220067020 A1 / US 11,893,004 B2 (Ford, 2024)**: **Entire patent is dedicated to Mahalanobis distance anomaly detection** in multidimensional sensor data

**Conclusion**: VibeGuard **cannot use Mahalanobis distance** for anomaly detection without:
- Obtaining licenses from both Tractian and Ford
- Designing around to use alternative methods

### Recommended Action: Remove Mahalanobis from VibeGuard

**Primary Detection Method**: Use **RMS/persistence baseline** only
- This appears to be novel (not found in any retrieved patent)
- Avoids all Mahalanobis-related patent issues

**Alternative Detection Methods** (if dual-mode desired):
- Isolation Forest
- One-Class SVM
- Autoencoders (neural networks)
- Z-score method
- Interquartile Range (IQR) method
- Local Outlier Factor (LOF)

---

## 📈 Updated Patentability Assessment

### Novelty - Stronger Position

**Likely Novel Elements** (no prior art found):
- Edge computation on ESP32 (vs. remote/cloud processing)
- DC removal preprocessing
- Hann window application
- Continuous computation of specific time-domain feature set (SD, crest factor)
- Triggered FFT approach (selective computation)
- **RMS/persistence baseline detection method**
- Eccentric-mass motor/fan test rig

**Partially Conventional Elements**:
- Single-node vibration monitoring (multiple patents)
- FFT for vibration analysis (multiple patents)
- RMS, peak, kurtosis as features (mentioned in some patents)

**Blocked/Overlapping Elements**:
- **Mahalanobis distance anomaly detection** (US 11,429,900 + US 11,893,004)

### Inventive Step - Stronger Position

The inventive step lies in:
1. **Adapting vibration monitoring for edge devices** - Prior art uses complex methods (US 7,421,349, US 7,346,461) or remote processing (US 11,429,900)
2. **Specific preprocessing pipeline** - DC removal + Hann window not found in any patent
3. **Continuous time-domain feature computation** - Unique combination of features
4. **Triggered FFT** - Balances accuracy with computational efficiency
5. **RMS/persistence baseline method** - Appears to be novel approach

### Eligibility - Unchanged

Still satisfies 35 U.S.C. § 101:
- Machine + Process ✅
- Not abstract idea ✅
- Adds significantly more (physical hardware + specific implementation) ✅

---

## 🎯 Updated Immediate Next Steps

### Priority 1: Complete Mandatory Leads
- [x] US 7,421,349 - Full text + claims ✓
- [x] US 7,346,461 - Full text ✓
- [ ] US 11,429,900 - Extract full claims to confirm exact Mahalanobis scope
- [ ] Tractian family - Identify all members (continuations, divisionals, international)

### Priority 2: Commercial Actors
- [x] **KCF Technologies** - US 9,271,170 B1, US 10,873,791 B1 ✓
- [x] **US 20220067020 A1** - Mahalanobis-specific ✓
- [ ] Infinite Uptime - Identify and analyze patents
- [ ] Augury - Identify and analyze patents
- [ ] Senseye - Identify and analyze patents

### Priority 3: Geographic Expansion
- [ ] InPASS (India) search for vibration monitoring patents
- [ ] CNIPA (China) search for vibration monitoring patents

### Priority 4: Classification & Literature
- [ ] CPC/IPC mapping for vibration monitoring domain
- [ ] ISO 10816, ISO 20964 verification
- [ ] Peer-reviewed papers on vibration analysis

### Priority 5: Advanced Analysis
- [ ] Complete novelty analysis (claim-by-claim)
- [ ] Inventive step analysis (problem-solution approach)
- [ ] Eligibility analysis (detailed § 101)
- [ ] Full FTO analysis with commercial products
- [ ] Claim-to-experiment mapping for VibeGuard

### Priority 6: Strategic Decisions
- [ ] **Remove Mahalanobis distance** from VibeGuard implementation
- [ ] Select alternative anomaly detection method
- [ ] Document novel aspects for patent filing

---

## 📊 Updated Summary

| Aspect | Status | Key Finding |
|--------|--------|-------------|
| Patent Retrieval | ✅ 5/5 mandatory + commercial | All key patents located |
| Claim Analysis | 🔄 In Progress | Preliminary mapping shows novel elements + critical overlaps |
| Novelty | 🔄 Stronger Position | Edge approach + preprocessing + baseline method likely novel |
| **FTO** | ❌ **CRITICAL - DOUBLE CONFIRMED** | **Mahalanobis distance BLOCKED by TWO patents** |
| Geographic | ❌ Not Started | India/China searches needed |
| Non-Patent | ❌ Not Started | ISO standards needed |

**Bottom Line**: VibeGuard has strong novel elements, but **Mahalanobis-distance anomaly detection is definitively blocked by prior art**. The RMS/persistence baseline method appears to be the novel, non-infringing path forward.

---

*Analysis based on independent verification as of 1 August 2026. Mahalanobis distance overlap confirmed by two separate patents. All conclusions preliminary - require further verification for complete FTO analysis.*


| Aspect | Status | Key Finding |
|--------|--------|-------------|
| Patent Retrieval | ✅ 2/3 complete | All three located, US 11,429,900 claims pending |
| Claim Analysis | 🔄 In Progress | Preliminary mapping shows novel elements + critical overlap |
| Novelty | 🔄 Preliminary | Edge approach + preprocessing likely novel, Mahalanobis overlaps |
| **FTO** | ⚠️ **CRITICAL** | **Mahalanobis-distance overlaps with US 11,429,900** |
| Geographic | ❌ Not Started | India/China searches needed |
| Non-Patent | ❌ Not Started | ISO standards needed |

---

*Analysis based on independent verification as of 1 August 2026. All conclusions preliminary - require further verification.*

## Source Fragment 3

- Original filename: `research on f.patent by mistral 3.md`
- Original absolute path: `/home/paradoxpete/Documents/PROJECT/PHASE 3/PHASE 3C-Comparative Technical Evaluation/FINAL_DOWNSELECTION/RESEAERCH/VIBEGUARD/research on f.patent by mistral 3.md`
- Original SHA-256: `b9fbf2c34ac71d90d682de5b77ba1d5bee0fa7f00cb18a8a8d99f292529e8f1b`
- Original format: Markdown
- Status: commercial-actor appendix, not a final VibeGuard report

# 📊 Commercial Actor Patent Retrieval Report
## Predictive Maintenance & Industrial IoT Patent Analysis

**Date:** August 1, 2026
**Status:** ✅ COMPLETE
**Scope:** Patent portfolio analysis for three commercial actors in predictive maintenance and industrial IoT

---

## 🎯 Executive Summary

This report completes the patent retrieval and analysis for three commercial actors in the predictive maintenance and Industrial IoT space, building upon previous work. All search steps have been executed across USPTO, Justia, Google Patents, UK IPO, and Espacenet databases.

| Company | Patents Identified | Status | Primary Technology |
|--------|-------------------|--------|-------------------|
| **Augury Systems Ltd** | 15+ US patents | ✅ Complete | Magnetic + Vibration + Acoustic sensors |
| **Infinite Uptime** | 3+ US patents + 2 PCT | ✅ Complete | Tri-axial vibration, edge computing |
| **Senseye Ltd (UK)** | 0 public patents | ✅ Complete | Acoustics-based cloud platform |

---

## 📋 Detailed Findings

### 1. ✅ Augury Systems Ltd *(Israel/US)*

**Company Profile:**
- **Headquarters:** Israel (with US operations)
- **Focus:** Industrial IoT predictive maintenance using magnetic, vibration, and acoustic sensors
- **Key Personnel:** Ori Negri, Daniel Barsky, Gal Ben-Haim, Saar Yoskovitz, Gal Shaul, Eduard Rudyk

**Patent Portfolio: 15+ US Patents**

#### Granted Patents (Recent First)

| Patent Number | Title | Filing Date | Grant Date | Inventors | Key Technology |
|--------------|-------|-------------|------------|-----------|----------------|
| **US 12607995** | Automated analysis of non-stationary machine performance | Feb 8, 2024 | Apr 21, 2026 | Ori Negri, Daniel Barsky, Gal Ben-Haim, Saar Yoskovitz, Gal Shaul | Multi-sensor fusion, non-stationary signal analysis |
| **US 12510403** | Systems and methods for monitoring of mechanical and electrical machines | Nov 8, 2023 | Dec 30, 2025 | Saar Yoskovitz, Gal Shaul, Ori Negri, Eduard Rudyk, Gal Ben-Haim | **Magnetic + vibration sensors (synchronous)** |
| **US 12498710** | Sensor-agnostic mechanical machine fault identification | Nov 9, 2023 | Dec 16, 2025 | Ori Negri, Christopher Bethel, Daniel Barsky, Gal Ben-Haim, Gal Shaul, Saar Yoskovitz | Transfer learning for fault classification |
| **US 11977053** | Systems and methods for acoustic emission monitoring of semiconductor devices | May 4, 2023 | May 7, 2024 | Eduard Rudyk, Ori Negri, Gal Shaul, Saar Yoskovitz | Acoustic emission monitoring |
| **US 11934184** | Automated analysis of non-stationary machine performance | Dec 9, 2022 | Mar 19, 2024 | Ori Negri, Daniel Barsky, Gal Ben-Haim, Saar Yoskovitz, Gal Shaul | Sensor fusion, feature extraction |
| **US 11885667** | Systems and methods for monitoring of mechanical and electrical machines | Sep 22, 2022 | Jan 30, 2024 | Saar Yoskovitz, Gal Shaul, Ori Negri, Eduard Rudyk, Gal Ben-Haim | Magnetic field + vibration synchronous sensing |
| **US 11853047** | Sensor-agnostic mechanical machine fault identification | Sep 3, 2020 | Dec 26, 2023 | Ori Negri, Christopher Bethel, Daniel Barsky, Gal Ben-Haim, Gal Shaul, Saar Yoskovitz | Cross-sensor transfer learning |
| **US 11579122** | Automatic mechanical systems diagnosis | Mar 18, 2021 | Feb 14, 2023 | Saar Yoskovitz, Gal Shaul | Portable device + remote processor |
| **US 11556121** | Automated analysis of non-stationary machine performance | Nov 7, 2019 | Jan 17, 2023 | Ori Negri, Daniel Barsky, Gal Ben-Haim, Saar Yoskovitz, Gal Shaul | Multi-sensor fusion |
| **US 11493379** | Systems and methods for monitoring of mechanical and electrical machines | Apr 9, 2018 | Nov 8, 2022 | Saar Yoskovitz, Gal Shaul, Ori Negri, Eduard Rudyk, Gal Ben-Haim | Magnetic field sensing |
| **US 11493482** | Systems and methods for acoustic emission monitoring of semiconductor devices | Oct 3, 2017 | Nov 8, 2022 | Eduard Rudyk, Ori Negri, Gal Shaul, Saar Yoskovitz | Acoustic sensing for semiconductor devices |

#### Published Applications

| Publication Number | Title | Filing Date | Publication Date |
|-------------------|-------|-------------|-----------------|
| US 20260202836 | Sensor-agnostic mechanical machine fault identification | Nov 18, 2025 | Jul 16, 2026 |
| US 20250035693 | Condition monitoring of electrical devices | Dec 1, 2022 | Jan 30, 2025 |
| US 20240255942 | Automated analysis of non-stationary machine performance | Feb 8, 2024 | Aug 1, 2024 |
| US 20230114296 | Automated analysis of non-stationary machine performance | Dec 9, 2022 | Apr 13, 2023 |
| US 20220011763 | Automated analysis of non-stationary machine performance | Feb 8, 2021 | Jan 13, 2022 |

**Technology Focus:**
- Magnetic field sensing combined with vibration sensors (synchronous)
- Acoustic emission monitoring
- Non-stationary signal analysis
- Transfer learning for sensor-agnostic fault identification
- Multi-sensor fusion algorithms

**Source:** [Justia Patents - Augury Systems Ltd](https://patents.justia.com/assignee/augury-systems-ltd)

---

### 2. ✅ Infinite Uptime *(US/India)*

**Company Profile:**
- **Headquarters:** US (manufacturing base in Pune, India)
- **CEO:** Raunak Bhinge (17 publications, 5+ patents)
- **Product:** vEdge (Industrial Data Enabler)
- **Focus:** Industrial IoT predictive maintenance with edge computing

**Patent Portfolio: 3+ US Patents + 2 PCT Applications**

#### Granted Patents

| Patent Number | Title | Filing Date | Grant Date | Assignee | Inventors | Key Technology |
|--------------|-------|-------------|------------|----------|-----------|----------------|
| **US 10821567** | Acoustic and vibration sensing apparatus and method for monitoring cutting tool operation | May 7, 2018 | Nov 3, 2020 | THE REGENTS OF THE UNIVERSITY OF CALIFORNIA | Raunak Bhinge, Yung-Chih Chen, Jinsu Choi, Jennifer Dai, David Dornfeld, Wojciech Musial, Rhett Gentile | Universal vise jaw plate with acoustic + vibration sensors |

#### Published Applications

| Publication Number | Title | Filing Date | Publication Date | Assignee | Inventors |
|-------------------|-------|-------------|-----------------|----------|-----------|
| **US 20190061086** | MAGNETIC ADD-ON SYSTEM WITH VIBRATION AND ACOUSTIC SENSING CAPABILITIES FOR TOOL CONDITION MONITORING | Aug 30, 2018 | Feb 28, 2019 | THE REGENTS OF THE UNIVERSITY OF CALIFORNIA, **INFINITE UPTIME, INC.** | Raunak Bhinge, Yung-Chih Chen, Kris Winer | Magnetically attachable sensor assembly |
| **US 20180326550** | ACOUSTIC AND VIBRATION SENSING APPARATUS AND METHOD FOR MONITORING CUTTING TOOL OPERATION | May 7, 2018 | Nov 15, 2018 | THE REGENTS OF THE UNIVERSITY OF CALIFORNIA | Raunak Bhinge, Yung-Chih Chen, Jinsu Choi, Jennifer Dai, David Dornfeld, Wojciech Musial, Rhett Gentile | Vise-based monitoring system |

#### International (PCT) Applications

| PCT Number | Title | Filing Date | Publication Date | Assignee |
|------------|-------|-------------|-----------------|----------|
| **WO2017151447A1** | Magnetic add-on system with vibration and acoustic sensing capabilities for tool condition monitoring | Feb 26, 2017 | Sep 8, 2017 | Infinite Uptime Inc, University of California Berkeley, University of California San Diego |
| **WO2017083120A1** | Acoustic and vibration sensing apparatus and method for monitoring cutting tool operation | May 18, 2017 | May 18, 2017 | The Regents of the University of California |

**Product Details:**
- **vEdge (Industrial Data Enabler):** Tri-axial high-frequency mechanical vibration, temperature, and acoustics sensing in real-time
- **Technology:** Edge computing, FFT analysis, magnetic connection, Wi-Fi/Bluetooth connectivity, OTA firmware upgrades
- **Deployment:** Plug-and-play, install on any machine within seconds

**Sources:**
- [Justia - Raunak Bhinge](https://patents.justia.com/inventor/raunak-bhinge)
- [Google Patents - WO2017151447A1](https://patents.google.com/patent/WO2017151447A1/en)
- [Google Patents - WO2017083120A1](https://patents.google.com/patent/WO2017083120A1/en)

---

### 3. ✅ Senseye Ltd *(UK - Acquired by Siemens)*

**Company Profile:**
- **Headquarters:** Southampton, UK
- **Founded:** 2014 by Alexander Hill
- **Acquired:** June 1, 2022 by Siemens Holdings plc (UK)
- **Current Status:** 100% subsidiary of Siemens, part of Digital Industries, Customer Services Business Unit
- **Product:** Senseye Predictive Maintenance (cloud-based SaaS platform)
- **Focus:** Acoustics-based condition monitoring using AI/ML

**Patent Portfolio: 0 Public Patents Found**

#### Search Results Summary

| Database | Search Scope | Results |
|----------|--------------|---------|
| USPTO | "Senseye Ltd", "Senseye Limited" | ❌ No matches |
| Justia Patents | Assignee: Senseye Ltd | ❌ No matches |
| Google Patents | site:patents.google.com "Senseye Ltd" | ❌ No matches |
| UK IPO | Company: Senseye Ltd (09210291) | ❌ No patent filings |
| Espacenet | "Senseye" predictive maintenance | ❌ No matches |
| Siemens Patents (2022-2026) | Predictive maintenance | ❌ No Senseye-branded patents |

#### Key Evidence of Patent Activity

**From SETsquared (University of Southampton incubator):**
> "Senseye has secured personal, investor and grant funding to develop the Sensight product... These key components are also being patented."

**From Tracxn:**
- Company status: Acquired by Siemens
- Focus: Cloud-based platform for acoustics-based condition monitoring solutions
- Funding: $10.3M raised before acquisition

**Conclusion:**
Senseye Ltd **has filed patents**, but they are:
1. **Not yet published** (18-month publication delay from filing)
2. **Filed under Siemens** post-acquisition (June 2022 onwards)
3. **UK/European filings first** (not yet in US databases)
4. **Potentially protected as trade secrets** (proprietary AI/ML algorithms)

**Important Distinction:**
There exists a separate **Senseye, Inc.** (US-based) with 9+ patents, but these are for **ocular/eye-tracking technology** (deception detection, cognitive load measurement, mental health diagnostics) - **completely unrelated** to industrial predictive maintenance.

**Sources:**
- [Siemens Press Release](https://press.siemens.com/global/en/pressrelease/siemens-acquires-senseye)
- [SETsquared Profile](https://www.setsquared.co.uk/company/senseye-ltd/)
- [Companies House - Senseye Ltd](https://find-and-update.company-information.service.gov.uk/company/09210291)
- [Tracxn - Senseye](https://tracxn.com/d/companies/senseye)

---

## 📊 Comparative Analysis

### Technology Comparison

| Feature | Augury Systems | Infinite Uptime | Senseye Ltd |
|---------|---------------|----------------|--------------|
| **Primary Sensor** | Magnetic + Vibration + Acoustic | Tri-axial Vibration + Acoustic + Temperature | Acoustics-based (sensor-agnostic) |
| **Deployment** | On-machine sensors | Magnetic add-on devices | Cloud platform (works with existing data) |
| **Edge Computing** | Yes | Yes (vEdge device) | No (cloud-based) |
| **Patent Count** | 15+ US patents | 3+ US patents + 2 PCT | Unknown (likely filed under Siemens) |
| **Key Innovation** | Magnetic field + vibration synchronous sensing | FFT analysis, edge diagnostics | AI/ML algorithms, acoustics-based monitoring |
| **Target Market** | Industrial machinery | Machine tools, manufacturing | Manufacturing, industrial companies |
| **Acquisition Status** | Independent | Independent | Acquired by Siemens (2022) |

### Patent Filing Activity

| Company | US Patents | PCT Applications | UK/EU Filings | Trade Secrets |
|---------|------------|-----------------|---------------|---------------|
| Augury Systems | 15+ | Multiple | Likely | Some |
| Infinite Uptime | 3+ | 2 | Unknown | Likely |
| Senseye Ltd | 0 (public) | Unknown | Likely | Likely |

---

## 🎯 Key Findings & Insights

### 1. Augury Systems - Patent Leader
- **Most prolific** with 15+ US patents
- **Strong focus** on magnetic sensing combined with vibration
- **Recent activity** continues through 2026 (US 12607995 granted April 2026)
- **Broad portfolio** covering mechanical, electrical, and semiconductor monitoring

### 2. Infinite Uptime - Academic Origins
- Patents originate from **UC Berkeley research** (Raunak Bhinge's PhD work)
- **Joint assignments** between UC Regents and Infinite Uptime, Inc.
- **International protection** via PCT filings
- **Product focus**: vEdge device with magnetic attachment

### 3. Senseye Ltd - The Stealth Player
- **No public patents** found under their own name
- **Acquired by Siemens** in 2022, suggesting IP consolidation
- **Cloud-first approach** - may rely more on software patents and trade secrets
- **Acoustics-based** monitoring differentiates from competitors

---

## 📌 Recommendations

### For Patent Analysis
1. **Augury Systems:** Monitor their continuing patent filings, particularly in sensor fusion and non-stationary signal analysis
2. **Infinite Uptime:** Track PCT applications for international expansion
3. **Senseye Ltd:** Search Siemens patent portfolio (2022 onwards) for Senseye-related filings under different assignee names

### For Competitive Intelligence
1. **Augury** leads in hardware innovation (sensors)
2. **Infinite Uptime** has strong academic backing and edge computing focus
3. **Senseye** (via Siemens) likely has the most scalable software platform

### For IP Strategy
- **Augury:** Strong patent position in multi-sensor monitoring
- **Infinite Uptime:** Good protection for edge devices and tool monitoring
- **Senseye:** Likely protecting cloud algorithms as trade secrets + patents

---

## 🔗 References & Sources

### Primary Sources
- [Justia Patents - Augury Systems Ltd](https://patents.justia.com/assignee/augury-systems-ltd)
- [Justia Patents - Raunak Bhinge](https://patents.justia.com/inventor/raunak-bhinge)
- [Google Patents - WO2017151447A1](https://patents.google.com/patent/WO2017151447A1/en)
- [Google Patents - WO2017083120A1](https://patents.google.com/patent/WO2017083120A1/en)
- [Siemens Press Release - Senseye Acquisition](https://press.siemens.com/global/en/pressrelease/siemens-acquires-senseye)
- [SETsquared - Senseye Ltd Profile](https://www.setsquared.co.uk/company/senseye-ltd/)
- [Companies House - Senseye Ltd](https://find-and-update.company-information.service.gov.uk/company/09210291)

### Secondary Sources
- [Tracxn - Senseye](https://tracxn.com/d/companies/senseye)
- [Siemens - Senseye Predictive Maintenance](https://www.siemens.com/en-us/products/industrial-digitalization-services/senseye-predictive-maintenance/)
- [Infinite Uptime Website](https://us.infinite-uptime.com/)

---

## ✅ Conclusion

All patent retrieval steps have been **completed successfully** for the three commercial actors:

1. **Augury Systems Ltd** - 15+ patents identified and documented
2. **Infinite Uptime** - 3+ patents + 2 PCT applications identified and documented
3. **Senseye Ltd (UK)** - Confirmed no public patents under their name; likely filed under Siemens or as trade secrets

The analysis reveals distinct technology approaches: Augury leads with sensor hardware innovation, Infinite Uptime combines academic research with edge devices, and Senseye (via Siemens) focuses on cloud-based software platforms with acoustics-based monitoring.

**Report Status:** ✅ **FINAL - ALL STEPS COMPLETE**


---

## Source 9: `03_CONCEPT_PORTFOLIO/VibeGuard/02_Raw_Research/06_VibeGuard_Patent_Research_Microsoft_Copilot.docx`

- Authority: `TIER_3`
- Treatment: `SUPPORTING_EVIDENCE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `NEW_STAGE10I_EXTRACTION`
- SHA-256: `f6c49a26af177d0faca247feb6aaa98cc2df389fae00bb4d6fd848d10e8540dd`

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

