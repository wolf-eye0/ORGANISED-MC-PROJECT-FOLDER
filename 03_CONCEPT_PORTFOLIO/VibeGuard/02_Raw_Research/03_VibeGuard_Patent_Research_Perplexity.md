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

