# Project mC Master Manual

## Part III — VibeGuard Architecture and Patent Research Path

## Document control

| Field | Value |
|---|---|
| Document | Project mC Master Manual — Part III |
| Controlled filename | `Project_mC_Master_Manual_Part_III_VibeGuard_Architecture_and_Patent_Path.md` |
| Status | Controlled draft |
| Scope | Chapters 06 and 07, followed by Part III registers and source ledger |
| Source boundary | Only the ten attachments in the controlled Part III package |
| Input inventory | Exactly ten physical attachments were readable. The nine externally hash-controlled inputs matched the manifest; the self-referential manifest was used only for file control. Upload suffixes did not create additional logical sources. |
| Implementation status | Not an implementation, Phase 4 or procurement authorization |
| Approval status | Not a teacher-approval record; concept and course-platform acceptance remain unresolved |
| Patent status | No patentability, filing, infringement or FTO conclusion |
| External verification | No fresh web, manufacturer, market, patent-register or legal-status work was performed |
| Relationship to Part I | Part I controls the current decision: VibeGuard is the strongest semester-build recommendation, but the shift, platform, Phase 4 and procurement are not proved approved; retained concepts remain legitimate; no MVP is established as patentable; the adjudications disagree on the future patent gate |
| Relationship to Part II | Style and cross-concept consistency reference only; not VibeGuard evidence |

The drafting package was complete. The validated VibeGuard reconciliation controls resolved wording and contradictions; the Chapter 06 and 07 packets preserve underlying evidence and original source paths. No prior-chat context, memory, web research or unstated assumption was used.

## How to read Part III

Part III preserves five boundaries.

**Architecture versus refinement.** The locked design is one rigid ADXL345-class sensor, one ESP32-class controller, SPI, a controlled rotating rig, RMS plus persistence, supporting FFT/bands, optional ordinary Mahalanobis, RGB, USB and fixed configuration records. Conventional tuning may refine this design; a different concept requires change control.

**Level 1 versus Level 2.** Chapter 06 covers controlled normal-versus-induced-abnormal detection. Chapter 07 covers later target attribution under interference, remounting and operating change. Level-1 success does not prove Level-2 observability.

**Detection versus attribution.** A classifier may detect a controlled state change without identifying which physical source caused it.

**Targets versus results.** Rates, windows, thresholds, performance figures and session counts are proposals unless approved or measured.

**Patent evidence versus filing.** The ordinary stack is not established as patentable. Future mechanisms remain hypotheses requiring experiments, current primary-source review and institutional IPR control.

# Chapter 06 — VibeGuard Frozen Architecture and Semester Scope

## 06.1 Chapter purpose

This chapter defines the controlled VibeGuard semester architecture, the boundaries within which implementation may proceed after authorization, and the evidence required before the team may make performance claims. It is an engineering reference, not permission to purchase components, enter Phase 4 or represent the project as teacher-approved.

VibeGuard asks a deliberately bounded semester question: can a student team use one low-cost target-mounted accelerometer and one ESP32-class controller to acquire reliable vibration data, establish a normal baseline, detect a safe and repeatable induced abnormal state through local lightweight analysis, and preserve enough configuration-controlled evidence for another person to reproduce and audit the result? This is an embedded measurement and controlled-classification problem. It is not a complete industrial predictive-maintenance product and does not promise diagnosis of a particular bearing defect, universal thresholds, remaining-useful-life estimation, automatic maintenance action or source attribution in a dense machine environment.

The architecture was selected because it offers a clear division between hardware, firmware, signal processing, validation and presentation work. Its apparent simplicity must not be mistaken for triviality. A vibration result can be invalidated by counterfeit or unsuitable sensor hardware, soft mounting, unstable sampling, hidden data loss, an unsafe or drifting abnormality fixture, leakage between calibration and test data, or post-hoc threshold tuning. The value of the semester project therefore lies as much in disciplined evidence control as in the live red/green demonstration.

## 06.2 Current architecture identity

> **VIBEGUARD ARCHITECTURE LOCK**
>
> For the frozen semester architecture, **VibeGuard means only**:
>
> - one rigidly mounted ADXL345-class tri-axis accelerometer;
> - one ESP32-class controller, with the exact board variant subject to course approval and purchased-board verification;
> - SPI acquisition from the accelerometer;
> - one controlled low-voltage motor, fan or comparable rotating test article;
> - repeatable normal and deliberately induced, safe abnormal operating states;
> - continuous or windowed time-domain features;
> - RMS plus persistence as the mandatory minimum classifier;
> - triggered or scheduled FFT and selected frequency bands as supporting evidence;
> - optional ordinary Mahalanobis comparison only after the baseline and acquisition-integrity gates pass;
> - local RGB state indication;
> - USB serial logging and exportable evidence; and
> - fixed records for the sensor, mounting, orientation, sampling configuration, firmware, rig and test session.
>
> This is a passive Level-1 monitoring and alerting demonstrator. It is **not** active vibration cancellation, software-security scanning, cloud monitoring, a permanent sensor array, fleet management, remaining-useful-life prediction, automatic maintenance decision-making, industrial certification, demonstrated bearing diagnosis, dense-machine source attribution, automatic adaptive learning or PIRG.

The identity lock prevents three kinds of drift. First, it prevents earlier or failed concept substitutions from re-entering the semester design. Software-security or configuration scanning may be cybersecurity work, but it is not the frozen VibeGuard concept. Second, it prevents optional analytical features from becoming new architecture requirements merely because they sound advanced. Ordinary Mahalanobis, extra statistical features or an optional display may be compared, but they do not replace RMS plus persistence or the RGB/USB evidence path. Third, it prevents post-semester patent-development hypotheses from being backfilled into the MVP. PIRG, ambiguity handling, protected updating and remount transfer belong to Chapter 07 and require separate authorization, equipment, evidence and confidentiality controls.

The frozen identity is passive. The system observes vibration and reports a controlled state. It does not actuate against the vibration, shut down the machine, command maintenance or claim that the source of the vibration has been identified. The sensor is permanently singular in the product architecture described here; temporary laboratory instruments may be used to validate the experiment, but they may not be hidden as permanent product dependencies.

## 06.3 Bounded semester objective

The bounded semester objective is to determine whether the locked architecture can **consistently distinguish a documented normal state from a deliberately introduced, safe and repeatable abnormal-vibration state using local lightweight processing without cloud dependence**.

A satisfactory project result must demonstrate the complete chain rather than an isolated algorithm. The team must show that the selected sensor is authentic enough for the intended test, that the mount is rigid and repeatable, that the ESP32 acquires samples with recorded timing and integrity, that the two physical states are independently labelled, that a baseline is calibrated without contaminating the held-out test, that persistence suppresses short transients, that local state indication follows the frozen logic, and that USB logs allow the result to be reconstructed after the demonstration.

A successful result is bounded. It may establish that a low-cost target-mounted sensing chain can detect the controlled state change on the team’s rig. It does not establish that the same threshold generalizes to every motor, that FFT identifies a fault type, that the abnormal state represents a real bearing failure, that one sensor can reject neighbouring-machine interference, that the system is safe for industrial deployment or that the ordinary feature stack is patentable.

VibeGuard remains the strongest supported semester-build recommendation in the attached comparative record because its hardware chain is comparatively simple, the firmware and signal-processing tasks align with the team’s technical strengths, subsystem failures can be isolated, and the demonstration can be backed by controlled logs. That recommendation is not the same as approval. The proposed shift from OpenBraille, the exact course platform, entry into Phase 4 and procurement remain unresolved until an explicit controlling decision is recorded.

## 06.4 System architecture overview

| Subsystem | Frozen role | Evidence boundary |
|---|---|---|
| Controlled rig | Produces documented normal and safe induced-abnormal states | Experimental label, not proof of a real industrial fault |
| ADXL345-class sensor | Converts target vibration into X/Y/Z samples | Module claims do not replace incoming, saturation or measured-limit checks |
| ESP32-class controller | Acquires, processes, indicates and logs | Exact board and pin map require purchased-board verification |
| Acquisition layer | Maintains timing, windows, buffers and integrity counters | Configured rate is not achieved-rate evidence |
| Time-feature layer | Calculates RMS and approved statistics | Conventional support for the bounded classifier |
| Minimum decision | Applies calibrated RMS threshold and persistence | Post-hoc test tuning invalidates evidence |
| Supporting analysis | FFT/bands and optional Mahalanobis comparison | No automatic diagnosis, attribution or novelty |
| RGB and USB | Provides live state and exportable evidence | LED-only demonstration is insufficient |
| Configuration control | Links results to sensor, mount, firmware, rig and session | Mixed or unknown configurations must not be pooled |

The layers prevent one type of evidence from substituting for another. A clean plot cannot repair unsafe labels or sample loss, and a red LED cannot prove valid sensing. A controlled negative result may still be valuable when the measurement chain and failure are documented.

## 06.5 Sensor and mounting architecture

The frozen sensor class is ADXL345-class. Higher-bandwidth sensing remains a later possibility, not the semester identity. Current datasheet values, availability and module authenticity were not reverified in this stage.

Incoming acceptance must preserve supplier and module identity, verify communication and plausible axis response, and inspect instability, noise, clipping or saturation. A failed module must be replaced or explicitly bounded; the classifier must not be tuned around defective hardware.

SPI is the controlling interface. Clock, range, output-data rate and final wiring must be established through measured integrity tests. Short, secure wiring and a stable final interconnect are required for locked evidence.

The sensor must be rigidly coupled to the target housing or a documented rigid bracket. Foam, loose breadboard placement, hand pressure and variable soft coupling are unacceptable because mounting changes amplitude, orientation and spectral response.

Records must include module identity, range/rate, axis convention, mount ID and method, orientation photographs, remount history, clipping/noise observations and session configuration. At least one untouched session, day or remount must be evaluated without threshold changes. The result need not prove universal transfer, but it must disclose tested remount sensitivity.

## 06.6 ESP32 and acquisition pipeline

The controller is ESP32-class, but the exact course-approved board is unresolved. Before final wiring, record board identity, schematic/pinout, regulator, USB interface, framework and toolchain. Roadmap pin maps are provisional.

The pipeline must declare sensor range and output-data rate, measure achieved effective rate and timing, freeze window length and overlap, and document FIFO/interrupt/timer or polling behavior. It must count read errors, saturation, delayed or lost blocks and buffer overruns. Silent loss invalidates the affected evidence.

Optional processing must not corrupt acquisition. FFT execution time, RAM, flash and worst-case processing use should be recorded. If timing is unstable, reduce rate or complexity, improve wiring or buffering, or replace unsuitable hardware.

A controlled sequence is: verify board/sensor; pilot raw X/Y/Z acquisition; measure timing/loss/saturation; inspect both physical states; freeze the lowest stable sufficient configuration; validate FFT scheduling; and emit a configuration banner with every session.

USB records should identify firmware, board, sensor settings, achieved-rate summary, windows, threshold/persistence version, mount, rig state, session and integrity counters. Exported data must permit offline checking; screenshots and LED behavior alone are insufficient.

## 06.7 Time-domain feature pipeline

The permitted time-domain feature family includes RMS, peak, standard deviation or variance, crest factor and kurtosis, calculated on a predeclared axis or magnitude representation. RMS is mandatory because it is the minimum magnitude feature for the frozen classifier. The other features are allowed only when they are implemented, versioned and evaluated without delaying the core system.

Preprocessing must be declared. Mean or DC removal may be applied before features where appropriate. The team must specify whether features are calculated per axis, on a vector magnitude, on a selected axis or through another fixed combination. The choice should be made through calibration and development evidence, then frozen before held-out evaluation. Trying many combinations after examining the test result would inflate apparent performance and weaken the evidence.

Feature proliferation is not a measure of intelligence. A compact, interpretable feature set with stable acquisition and clean session separation is preferable to a large list of statistics that cannot be explained or reproduced. Time-domain features are conventional analytical elements. They support the semester classifier; they do not constitute patent evidence by themselves.

## 06.8 RMS baseline and persistence logic

RMS plus persistence is the controlling minimum classifier. The architecture does not require the team to begin with machine learning or multivariate distance. It requires a physically honest baseline that can be calibrated, frozen, executed locally and tested on untouched sessions.

A controlled procedure is:

1. collect multiple approved normal calibration sessions under a stable, documented sensor, mount, rig and operating configuration;
2. derive an RMS baseline and threshold through a predeclared rule;
3. use separate development sessions to choose the persistence and recovery logic;
4. freeze the threshold, persistence, hysteresis or recovery rule before reviewing held-out results;
5. require threshold exceedance for consecutive windows or a declared duration before entering the abnormal state;
6. log the first physical abnormal-state timestamp where available, the first threshold crossing, the confirmed state transition and the resulting latency;
7. report false alerts, missed abnormal states and invalid sessions without post-hoc threshold repair.

Persistence is not a cosmetic delay. It is the minimum control against momentary shocks, startup transients, handling events and single-window noise. The exact persistence duration is not approved in the attached record. It must be selected and preregistered after pilot evidence. A recovery rule or hysteresis may be added to prevent rapid red/green oscillation, but it must be documented and tested rather than tuned during the final demonstration.

Calibration, development and held-out sessions must remain separated. Windows from one continuous run are not independent simply because they are numerous. Randomly splitting overlapping windows across training and testing can allow nearly identical signal segments into both sets and create misleading performance. The locked evaluation should therefore hold out complete sessions, days and remounts as appropriate.

Sensor, timing or mount faults must be separated from normal and abnormal classification. A failed sensor read, saturated stream or invalid configuration should not be forced into the normal state. An explicit fault/invalid condition may be implemented as an allowed refinement and should be logged even if the RGB demonstration remains centered on calibration, normal and abnormal.

## 06.9 Triggered FFT and selected frequency bands

Triggered or scheduled FFT is supporting evidence. It may help explain how the controlled abnormal state differs from the normal state, reveal repeatable energy redistribution, compare selected bands or support a stronger conventional baseline. It does not automatically diagnose a bearing fault or identify the physical source of the change.

The analysis record must disclose the actual effective sample rate, window length, window function, FFT length, frequency resolution, overlap or hop, selected bands and the physical or empirical reason for selecting them. It must also record execution time, memory use, whether FFT runs only after a pre-trigger or on a schedule, and whether the processing causes delayed or lost acquisition blocks.

Triggered analysis creates its own risk. A trigger may miss a short event, begin after important onset information or bias the set of windows that receive spectral analysis. The team should therefore preserve enough continuous time-domain evidence to explain when and why the FFT was executed. Spectral plots should be tied to session and configuration IDs, not presented as isolated images.

Selected bands must remain bounded by the sensor and acquisition evidence. If the module, mount or sample rate does not reliably observe a band, the team must not claim meaningful energy there. Aliasing, clipping, sensor noise and structural resonances can produce apparently informative peaks. The proper conclusion may be that a band is not trustworthy under the tested configuration.

FFT and band features are conventional. They may improve explanation or held-out discrimination, but they do not establish novelty, source attribution, industrial diagnosis or patentability. Their inclusion is justified only by measurable explanatory or comparative value under the same locked protocol used for the minimum classifier.

## 06.10 Optional Mahalanobis comparator

Ordinary Mahalanobis distance may be implemented as an optional normal-space comparator over a small declared feature vector. It is not mandatory AI, a novelty claim or a source-attribution mechanism.

The comparator should be attempted only after the acquisition-integrity, normal-repeatability, abnormal-repeatability and RMS/persistence gates pass. It should use a documented normal calibration set and the same complete-session held-out protocol as the baseline. If the covariance estimate is unstable, regularization may be used only when declared and versioned. The feature vector must remain small enough to estimate and execute reliably.

The comparator should be dropped if it delays the minimum build, creates unstable covariance, exceeds resource limits, complicates the demonstration without adding value or fails to outperform or clarify the simpler baseline. A more complex score is not automatically a better project result. In Chapter 07, ordinary Mahalanobis also serves as a mandatory conventional baseline against which any future mechanism must be compared; it is never the invention by itself.

## 06.11 Controlled rig and induced abnormal state

The semester rig must be a low-voltage motor, fan or comparable rotating system mounted on a stable base. The normal and abnormal states must be independently defined in physical terms. The preferred abnormality identified in the evidence is a mechanically retained eccentric mass; loosened mounting appears as another possible route. The exact method remains subject to safety and repeatability approval.

The induced state must be deliberate, safe, retained and repeatable. The project must not depend on causing a real machine failure or using an unguarded rotating mass for presentation effect. A successful classifier built around an unsafe or drifting fixture is not an acceptable success.

Required rig controls include:

- a heavy or rigid base that does not walk during operation;
- a rigid motor/fan mount;
- a mechanically retained abnormality fixture;
- a guard around the shaft, fan or rotating mass;
- an immediate power-disconnect method;
- low-speed or current-limited bring-up;
- strain relief and protected wiring;
- a pre-run check of fasteners, guard, sensor mount and electrical connections;
- recorded abnormality mass, radius, position, supply voltage and a speed/load proxy where available;
- an unambiguous rig configuration ID;
- stop rules for movement, loosening, cracking, heating, smell, sparking, repeated controller resets, detached wiring or faculty instruction.

The physical label must be more than “motor looked abnormal.” The team must be able to state what was changed, how it was retained and how the same state was reproduced in another session. Speed, load, supply variation and base movement can alter the vibration independently of the abnormality fixture, so they should be stabilized or recorded.

Normal repeatability must be established before classifier tuning. If normal sessions vary more than the difference between normal and induced-abnormal states, the priority is to repair the mount, rig or acquisition process. Similarly, if the abnormal state cannot be reproduced safely, the fixture must be redesigned rather than compensated through increasingly flexible thresholds.

## 06.12 RGB state indication and USB evidence

The local interface must communicate the state clearly while preserving an auditable digital record. A reconciled state model is:

- **startup/self-check:** the controller reports firmware/configuration identity and checks communication;
- **calibrating:** blue indication and USB status while an approved calibration operation is active;
- **normal:** green after the baseline and state machine are valid;
- **abnormal:** red only after the persistence requirement is satisfied;
- **fault/invalid:** a separately logged condition and, if implemented, a visibly distinct indication.

The RGB output is a live human interface, not the evidence archive. USB logging should include timestamps, raw X/Y/Z samples or declared processed values, feature values, threshold and persistence version, state transitions, sensor-read errors, clipping/saturation, dropped blocks, achieved-rate summaries and session metadata. The logs should be exportable to CSV or another documented format and should preserve enough information to reconstruct the decision.

The final demonstration should show the relationship between the physical state, digital evidence and local indication. A reviewer should be able to identify the rig configuration, see the state transition, inspect the feature or threshold evidence and confirm that no integrity fault occurred. A demonstration in which only the LED is visible is insufficient because the same behavior could be produced without valid sensing.

An Unknown or Interfered state belongs to later attribution research. It must not silently replace or redefine the Level-1 semester output. Fault/invalid handling in Chapter 06 concerns sensor, timing, configuration or mount validity; it does not claim source ambiguity analysis.

## 06.13 BOM and budget evidence

The architecture class is frozen, but the procurement-ready BOM is not. The attached cost values are dated planning evidence and must not be represented as current quotations.

| Cost layer | Controlled interpretation |
|---|---|
| Historical Phase 3C estimate | The corrected ADXL345 route was approximately ₹1,700–₹2,200. A higher-bandwidth route approached ₹4,000. These are historical engineering estimates, not current supplier prices. |
| Teacher-facing roadmap plan | Approximately ₹2,200 expected and approximately ₹3,900 as a protected conservative envelope, dated 3 August 2026. The protected envelope excluded post-semester PIRG work, a second research motor, temporary reference instruments, patent searching and professional fees. |
| Project limits | Preferred spend at or below ₹3,000 and controlling maximum of ₹5,000, subject to teacher requirements and final authorization. |
| Current procurement status | Not frozen. Current specifications, availability, authenticity, delivery, taxes, replacement allowance and exact Indian prices require a later controlled verification pass. |

The provisional semester BOM class includes one ESP32 board, one ADXL345 module, a low-voltage motor or fan, a separate regulated motor supply, RGB LED and resistors, short final wiring or perfboard materials, a rigid base and motor/sensor mount, a retained eccentric fixture and guard, protection/passive components and an allowance for delivery or replacement. Exact models, ratings, sellers and pin maps remain unapproved.

Budget evidence must remain layered. A low historical total does not prove that an authentic sensor, safe rig and suitable power source can be purchased today at the same price. Conversely, a protected planning envelope is not a requirement to spend the full amount. Procurement should occur only after approval, current manufacturer and supplier verification, safety review and a frozen bill of materials.

Post-semester research must have a separate budget. A dual-machine interference bench, temporary synchronized references, field access, patent searching and professional IPR work are not hidden semester expenses. Keeping these costs separate prevents the future patent hypothesis from distorting the feasibility of the ordinary MVP.

## 06.14 Minimum demonstrable success

Minimum demonstrable success requires the complete bounded system, not merely a classifier score:

1. the selected ESP32 and accelerometer pass incoming acceptance and self-check;
2. the sensor is rigidly mounted with recorded orientation and configuration;
3. stable timestamped acquisition is demonstrated with integrity counters;
4. the rig produces a safe, repeatable and independently labelled normal state and induced-abnormal state;
5. multiple normal calibration sessions establish a baseline;
6. RMS plus persistence separates the controlled states locally under a frozen rule;
7. RGB indicates the state clearly and consistently with the log;
8. USB produces an auditable configuration and evidence record;
9. at least one untouched session, day or remount is evaluated without threshold changes;
10. false alerts, missed detections, latency, acquisition loss, remount sensitivity and bandwidth limits are reported honestly;
11. another team member can operate the setup through a checklist and explain the evidence boundary;
12. the final report states that the result proves only the bounded Level-1 task.

FFT, selected bands and ordinary Mahalanobis may enrich the result but are not required for semester success if the minimum classifier and evidence package are complete. A simple, reproducible system that reports its limitations is stronger than an expanded system that cannot demonstrate acquisition integrity or held-out validity.

## 06.15 Validation and entry gates

| Gate | Question | Required evidence | Failure response |
|---|---|---|---|
| Authorization | Has the teacher approved the proposed concept shift, course platform and safe Level-1 scope? | Explicit controlling decision, conditions and date | Do not freeze procurement, claim Phase 4 entry or present VibeGuard as finally selected |
| V0 — Component acceptance | Are the board, sensor, motor and supply usable? | Board identity, USB operation, sensor identity/axis response, stable rails and rig inspection | Replace or redesign the failing component before integration |
| V1 — Acquisition integrity | Can stable timestamped data be collected? | Achieved rate, timing record, read/loss/saturation counters and stable wiring | Reduce rate/clock, shorten wiring, move to final interconnect or replace the sensor |
| V2 — Normal repeatability | Is normal behavior stable across independent sessions and remounts? | Complete-session feature distributions, rig records and mount photographs | Repair the rig or mount before classifier tuning |
| V3 — Abnormal repeatability | Is the induced state safe, labelled and repeatable? | Repeated abnormal sessions and physical configuration metadata | Redesign the fixture; do not tune around unstable labels |
| V4 — Minimum classifier | Does RMS plus persistence work locally? | Frozen calibration/development results, state logs and latency | Simplify features or improve physical repeatability |
| V5 — Supporting comparisons | Do FFT/bands or ordinary Mahalanobis add useful evidence? | Same held-out protocol and resource comparison | Drop the optional comparator if it adds no value or threatens baseline integrity |
| V6 — Locked held-out run | Does the frozen system generalize to untouched sessions, days or remounts? | Pre-registered metrics, immutable split and no post-hoc threshold changes | Report failure honestly and preserve the measurement-study result |
| V7 — Demonstration and documentation | Can a second operator run and explain the system safely? | Checklist, rehearsal, logs, configuration record and source-backed report | Freeze feature growth and correct only essential defects |

The authorization gate precedes procurement. The technical gates then proceed from physical and acquisition validity toward classification. This order prevents the team from spending time optimizing algorithms on unreliable hardware or unstable labels.

## 06.16 Quantitative evidence categories

No final Level-1 numeric gate is approved. Roadmap figures are preregistration proposals only. The following categories are mandatory:

| Category | Required report |
|---|---|
| Independent units | Sessions, days, remounts, operators and physical repetitions |
| Detection | Sensitivity/missed abnormal states and class counts |
| False alerts | Specificity, stable-normal duration and alert count |
| Outcomes | Confusion matrix including invalid sessions |
| Latency | Physical label/change time, threshold crossing and persistence confirmation |
| Integrity | Achieved rate, timing, errors, saturation and dropped/delayed blocks |
| Reproducibility | Second-operator and untouched session/day/remount result |
| Resources | RAM, flash, worst-case processing and logging behavior |
| Exclusions | Every excluded session and predeclared reason |
| Limits | Mount, sensor band, rig dependence and unsupported generalization |

Before a locked run, the authorized owner must approve threshold derivation, persistence/recovery, counts, hold-out structure, exclusions, latency and kill rules. Failure must be reported rather than repaired through post-hoc tuning.

## 06.17 Mounting, sampling, rig and classification risks

| Risk | Why it matters | Controlling treatment |
|---|---|---|
| Counterfeit or poor-quality sensor | Communication may work while noise, bandwidth or axis response is unsuitable | Preserve supplier/module records, run incoming checks and replace failed hardware |
| Mount-dependent result | Coupling changes amplitude, orientation and spectrum | Use a rigid documented mount, mark orientation and test at least one remount |
| Sampling or SPI loss | Irregular timing can corrupt RMS and FFT while producing plausible outputs | Use short wiring, conservative settings, explicit counters and an acquisition gate |
| Saturation or bandwidth mismatch | The sensor may clip or fail to observe the useful band | Pilot range/rate, disclose measured limits and avoid unobserved fault claims |
| Unsafe abnormality fixture | A loose mass or moving base creates physical danger and invalid labels | Retain and guard the fixture, inspect before each run and stop on defined hazards |
| Unrepeatable state labels | Speed, load, voltage or fixture position may drift | Stabilize or record the physical state before classifier tuning |
| Data leakage | Overlapping windows from one run can inflate performance | Hold out complete sessions, days and remounts |
| Startup or handling transients | Short shocks may exceed the magnitude threshold | Use persistence, controlled startup handling and event logs |
| Comparator expansion | Extra features, FFT, Mahalanobis or ML may delay the baseline | Baseline first; drop optional work if schedule or integrity is threatened |
| Team bottleneck | One person may become the only operator or evidence owner | Use primary/reviewer ownership, checklists and cross-training |
| Patent expectation distortion | Future mechanisms may enter the semester scope without evidence | Separate repositories, budgets, claims and approval gates |
| Overclaiming from isolated rig | The demo may be mistaken for industrial source diagnosis | State the Level-1 boundary in the report, poster and presentation |

Risk controls should be treated as design requirements, not final-report disclaimers. The project is strongest when a risk is prevented or measured before the demonstration, rather than mentioned after the result has already been compromised.

## 06.18 Allowed refinements

The following refinements are permitted within the frozen architecture when they do not delay the minimum build or change the concept identity:

- select the exact approved ESP32 variant and revalidate its pin map;
- tune range, rate, window and overlap through pilot integrity tests;
- improve rigid mounting, base, guard, strain relief and final interconnect;
- add explicit sensor, timing, saturation or mount fault/invalid handling;
- choose and freeze a documented axis or magnitude combination;
- add peak, variance or standard deviation, crest factor or kurtosis;
- use triggered or scheduled FFT and selected bands;
- implement ordinary Mahalanobis as a comparator;
- add better metadata, integrity counters and reproducible analysis scripts;
- add a nonessential display provided RGB and USB remain the required interface;
- use temporary laboratory instruments for validation without making them permanent product hardware;
- refine checklists, session registries and second-operator procedures.

Supervised TinyML, online learning, adaptive threshold promotion, automatic baseline updating, source separation or a permanent second product sensor are not ordinary refinements. They require a new authorized scope and belong, if anywhere, to later research. A change that alters the central physical or analytical identity must be recorded through formal change control rather than described as an implementation detail.

## 06.19 Prohibited substitutions and overclaims

The Chapter 06 implementation and final presentation must not substitute or silently add:

- software-security or configuration scanning;
- active vibration cancellation;
- cloud dependence or required wireless service;
- a multi-sensor deployed array;
- remote fleet management;
- remaining-useful-life prediction;
- automatic maintenance decisions;
- industrial safety or condition-monitoring certification;
- demonstrated bearing diagnosis;
- dense-machine target-source attribution or source separation;
- automatic self-learning or online adaptive production behavior;
- PIRG, protected updating or remount transfer;
- teacher approval, Phase 4 entry or procurement authorization not present in a controlling record;
- exact current prices, supplier specifications or authenticity not verified in the procurement stage;
- patent-ready, novel, inventive, eligible or FTO-cleared claims;
- unapproved numerical targets presented as measured or binding facts.

The project should also avoid softer overclaims. “AI-powered,” “industrial-grade,” “predictive maintenance,” “fault isolation” and “real-time diagnosis” can imply capabilities beyond the evidence. The draft-safe description is a controlled local vibration monitor that distinguishes a documented normal state from a safely induced abnormal-vibration state on the project rig using RMS plus persistence, with supporting spectral evidence.

## 06.20 Current implementation and approval status

> **VIBEGUARD CURRENT IMPLEMENTATION STATUS**
>
> - VibeGuard is the strongest supported semester-build recommendation in the attached Project mC record.
> - A formal request exists to shift the semester implementation from OpenBraille to VibeGuard.
> - The attachments do not prove that the teacher approved the shift.
> - The attachments do not prove final acceptance of the ESP32 platform or resolve the earlier STM32/course-platform context.
> - Phase 4 entry, procurement, final BOM freeze, named subsystem ownership and locked quantitative criteria are not proved complete.
> - No physical VibeGuard acquisition, rig, classifier or held-out result is attached to this drafting package.
> - Historical planning evidence indicates that the architecture was intended to fit the ₹5,000 ceiling, but current prices, specifications, availability and authenticity require later verification.
> - The ordinary semester MVP is not established as patentable.

The chapter may therefore guide an authorized build, but it must not be treated as proof that implementation has begun. The next controlling action is an explicit project and platform decision followed by a current specification, safety and procurement pass.

## 06.21 Chapter conclusion

VibeGuard’s semester strength comes from a disciplined boundary. One rigid sensor, one controller, one controlled rotating rig and one minimum classifier create a project that can be built, measured and explained without pretending to solve industrial predictive maintenance. The architecture is only credible when physical mounting, acquisition integrity, state labels, baseline separation and held-out testing receive the same attention as the signal-processing code.

RMS plus persistence is the minimum classifier. Triggered FFT and selected bands may support explanation; ordinary Mahalanobis may be compared after the baseline works. RGB provides a clear local demonstration, while USB and configuration control preserve the evidence. A successful isolated-rig result proves only the bounded Level-1 task. It does not prove bearing diagnosis, target attribution, industrial readiness or patentability.

The chapter is ready to support controlled implementation after approval. It does not itself authorize the concept shift, platform, Phase 4 or procurement. Those decisions, along with current component verification and a preregistered quantitative protocol, remain open.

## 06.S Source notes

The following original organized-workspace sources materially support Chapter 06. The validated reconciliation controls resolved wording and contradictions. Packet filenames and the attachment manifest are not cited as original technical evidence.

### TIER_1 — Current architecture and governance

- `01_GOVERNANCE_AND_CONTROL/01_Project_Requirements/Teacher_Project_Requirements_and_Change_Context.md` — teacher/course constraints, budget context and proposed-change status.
- `01_GOVERNANCE_AND_CONTROL/02_Decision_Registers/Project_mC_Decision_Register_v1.2.md` — retained portfolio, VibeGuard frozen identity and current decision state.
- `03_CONCEPT_PORTFOLIO/VibeGuard/01_Final_Architecture/Phase3C_VibeGuard_Architecture_Report_Final.md` — authoritative Phase 3C engineering selection, sensing chain, processing architecture, rig and historical cost evidence.
- `03_CONCEPT_PORTFOLIO/VibeGuard/01_Final_Architecture/Phase3C_VibeGuard_Memory_Final.md` — final architecture memory, minimum implementation and continuity control.
- `03_CONCEPT_PORTFOLIO/VibeGuard/01_Final_Architecture/Phase3C_VibeGuard_SOP_Final.md` — mission, constraints, evidence rules, validation requirements and phase boundary.

### TIER_2 — Supporting, historical and conditional implementation evidence

- `03_CONCEPT_PORTFOLIO/VibeGuard/05_Roadmaps_and_Reference_Dossiers/HISTORICAL_Phase1C_VibeGuard_Concept_Dossier.docx` — historical concept origin only; does not override the frozen architecture.
- `03_CONCEPT_PORTFOLIO/VibeGuard/05_Roadmaps_and_Reference_Dossiers/VibeGuard_Semester_Implementation_and_Future_Research_Roadmap.pdf` — conditional implementation, BOM, safety, validation, schedule and future-boundary proposal.
- `03_CONCEPT_PORTFOLIO/VibeGuard/PATENT_EVIDENCE_INDEX.md` — controlled research-lane and synthesis identity, status and exclusion context.
- `03_CONCEPT_PORTFOLIO/VibeGuard/README.md` — concept-folder status and navigation support.
- `04_COMPARATIVE_DECISION/03_Change_Request/Project_mC_Request_to_Change_from_OpenBraille_to_VibeGuard.docx` — formal change request and proposed roles; not approval.

# Chapter 07 — VibeGuard Patent Evidence and Future Research Path

## 07.1 Chapter purpose and legal boundary

This chapter explains what the controlled patent-evidence record does and does not support, why the ordinary VibeGuard MVP is not the current invention, and what physical research would be required before a later mechanism could become eligible for an institutional file/no-file review. It is not legal advice and does not authorize a patent filing.

The evidence must be read in four layers:

1. the ordinary frozen Level-1 semester MVP;
2. conventional refinements and comparators within that MVP;
3. post-semester interference, ambiguity, remount and transfer experiments;
4. speculative patent-development mechanisms, including PIRG.

The attached syntheses and simulation are time-bounded research records. They do not establish an exhaustive worldwide search, current national legal status, novelty, inventive step, patent eligibility, useful claim scope, infringement clearance, FTO, filing approval or probable grant. Patent-family and non-patent-literature conclusions require a fresh primary-source pass immediately before any material patent decision.

Raw research lanes are evidence sources, not votes. A conclusion does not become reliable because several models repeat it. Unsupported legal confidence, simulated searches, incomplete fragments, abstract-only readings, invented performance thresholds and concept-swapped content are excluded or downgraded. The valid syntheses control the audited interpretation, while the raw lanes remain provenance and lead sources.

## 07.2 Ordinary MVP patent position

> **VIBEGUARD PATENT STATUS — NO CURRENT FILING BASIS**
>
> - The ordinary ADXL345-plus-ESP32 Level-1 stack is not established as patentable.
> - Its rigid sensing, local acquisition, DC/mean removal, common time features, RMS threshold, persistence, FFT, selected bands, static baseline comparison, ordinary Mahalanobis, RGB alerting, USB logging and controlled rig are conventional individually and, on the attached evidence, form a predictable monitoring aggregation.
> - Low cost, edge-only operation, one sensor, absence of cloud service and a student-friendly implementation do not by themselves create novelty or inventive step.
> - No filing commitment is justified by the current record.
> - PIRG is not implemented or validated and is not part of the semester MVP.
> - Any later positive mechanism would still require physical evidence, current primary-source prior-art review, FTO analysis, field-like evidence, confidentiality control and ownership/inventorship review before institutional or professional file/no-file consideration.

The ordinary MVP nevertheless has important research value. It creates a stable measurement chain, establishes the sensor and mounting limits, produces controlled labelled data, exposes timing and resource constraints, and provides conventional baselines against which later mechanisms can be falsified. It also produces contemporaneous evidence of what was actually implemented and what failed.

The MVP should not be filed or presented as the invention merely because it is inexpensive, local, subscription-free or implemented on an ESP32. The patent syntheses place the ordinary feature stack in a crowded field. Triggered processing, confidence scores, baseline learning, FFT bands and ordinary Mahalanobis are also crowded directions when claimed in isolation. The future case, if any, must arise from a specific enabled physical-control relationship that produces a measurable technical effect beyond these baselines.

## 07.3 Research-lane integrity and limitations

Six controlled research lanes are preserved, but they are not equal and are not votes.

| Lane | Useful contribution | Treatment |
|---|---|---|
| ChatGPT DR | Search leads, Level-1/Level-2 separation, claim-to-test framing | Medium; retain audited leads |
| Gemini | Project fidelity and guarded bench/field framing | Medium-low for legal conclusions; optimistic novelty/FTO and invented numbers excluded |
| Perplexity | Located-document leads and conservative gaps | Medium for located records; low completeness |
| Qwen | Some kill-test and remount prompts | Low; simulated search and unsupported legal/quantitative claims excluded |
| Mistral partial | Actor and document-number leads | One partial low-reliability lane, no final verdict; missing conclusions not reconstructed |
| Copilot | Frozen architecture and Level-1/Level-2 framing | Medium for project fidelity, low for patent/legal analysis |

The valid syntheses control audited readings. Raw lanes remain provenance or search leads; repetition cannot repair an unsupported conclusion. Patent-family and status statements remain time-bounded and require official verification.

## 07.4 Valid synthesis conclusions

The two valid VibeGuard patent syntheses converge on a conservative core:

- the frozen MVP is buildable as a research platform but is not the invention;
- isolated Level-1 normal/abnormal classification cannot prove target attribution;
- one target-mounted accelerometer observes a mixture shaped by the target, neighbours, structure, speed/load, mounting and sensor limits;
- ordinary FFT, selected bands, Mahalanobis, baseline learning, triggered processing and confidence scores are crowded standalone directions;
- a surviving research direction must connect independently known physical states to a specific mechanism and a measurable reduction in wrong-source decisions or contaminated learning;
- strong conventional baselines, complete-session/remount holdouts and field-like labels are mandatory;
- the broad integrated direction faces high obviousness risk, unresolved novelty and FTO, enablement gaps and a field-access dependency;
- the future route is at best a Track-C-style long-term research path requiring later extension, not a patent-first semester claim.

The syntheses describe a broad label-aware, contamination-protected, confidence-gated single-node target-attribution loop. In that map, independently known target and interferer states support separate representations; target departure and ambiguity are scored separately; the system may abstain rather than force a target-fault label; baseline updates are guarded against contamination; and mount validity determines whether a model remains usable.

This broad description is not proof that the elements cooperate non-obviously. It is a research map. The later pre-build simulation therefore narrows the first test and defers update and transfer claims. The distinction between the broad synthesis-level direction and the narrow first experiment is central to this chapter.

## 07.5 Cross-concept adjudication context

Both final comparative adjudications identify VibeGuard as the strongest semester-build candidate. This agreement supports the Chapter 06 recommendation because VibeGuard offers the most manageable combination of hardware simplicity, embedded processing, validation and demonstration.

The adjudications do not agree on the preferred future patent-development gate:

- the Work Max adjudication favors a VibeGuard Level-2A signal-and-access gate and uses TrueMoist as fallback if that gate fails;
- the Deep Research High adjudication favors an OpenBraille D11 physical-state observability gate first and retains VibeGuard as fallback.

The adjudications are decision context, not votes. Their disagreement means the project has no resolved patent-first route. It would be incorrect to average the two documents, select VibeGuard merely because both prefer its semester build, or treat either conditional gate as proof that PIRG works. A controlling project authority must choose a gate, define a replacement rule or defer patent-first selection.

OpenBraille and TrueMoist remain legitimate retained concepts. Chapter 07 does not import their mechanisms into VibeGuard or use their existence to strengthen the VibeGuard patent case. The only cross-concept conclusion used here is the unresolved decision state recorded in validated Part I.

## 07.6 PIRG research hypothesis

The controlling sources do not define an expansion of **PIRG**. This manual uses the acronym only.

### Broad synthesis-level mechanism

The valid syntheses describe a label-aware, contamination-protected, confidence-gated single-node attribution loop. Independently known target/interferer states support target and interference representations; target departure and ambiguity are scored separately; unsupported cases may be Unknown; baseline admission is guarded; and mount validity determines whether the model remains usable. This is a research map, not an enabled or patentable system.

### Narrowed paired-intervention candidate

The pre-build simulation says the broad mechanism should be redesigned before testing. Its narrower first candidate is:

1. form a target-change contrast from paired measurements where the target changes and the interferer is fixed;
2. form an interference-change contrast where the interferer changes and the target remains normal;
3. produce a runtime deviation vector from the one permanent target-mounted sensor;
4. compare it with both contrast structures through projection residuals or an equivalent frozen test;
5. require an anomaly gate;
6. output Target-Abnormal only when the event is anomalous and fits target change materially better;
7. output Unknown when ambiguous, out of support or mount-invalid;
8. keep RMS/persistence, FFT/bands, Mahalanobis and a strong frequency-domain classifier as baselines;
9. defer baseline promotion/rollback;
10. default to model invalidation and recommissioning after an unvalidated remount.

### Relationship to Level 1

PIRG reuses the target-mounted sensing platform but is not part of the semester MVP. It requires a separate dual-source/factorial rig, independently controlled target and interferer states, temporary synchronized references for ground truth, blocked held-out sessions/remounts and later field-like evidence. A negative result does not invalidate the semester monitor.

### Baselines and ablations

All methods must use identical blocked splits. Baselines include RMS/persistence, FFT/bands, ordinary Mahalanobis, static spectral comparison, naive adaptation where relevant and a strong one-sensor frequency-domain classifier. Ablations must remove the contrast, anomaly/Unknown gate, mount rule and any later update protection separately.

### Required evidence

Required evidence includes independent target/interferer labels; repeated paired interventions; multiple sessions, days, speed/load regimes and remounts; immutable data and metadata; held-out contrast stability; wrong-source errors, missed target faults, false target alerts, Unknown coverage and latency; edge integrity/resources; strongest-baseline comparison; ablations; and later field-like labels if the bench gate passes.

### Failure conditions

Kill or redesign the hypothesis if contrasts are collinear or unstable; held-out geometry fails; gains depend on leakage or near-universal abstention; a permanent reference sensor is required; the useful band is unobserved; edge execution loses data; the effect disappears against baseline/ablation; field-like labels are unavailable; or current primary prior art defeats the mechanism.

### Current unproved status

No source proves observability, novelty, non-obvious cooperation, enabling parameters, useful Unknown coverage, remount transfer, contamination-safe updating, field generalization, claim value or FTO. PIRG remains a candidate mechanism, not an implemented invention or filing basis.

## 07.7 Target-source attribution and non-identifiability

A single target-mounted accelerometer measures a mixture. The observed signal is shaped by the target, neighbouring sources, structural coupling, speed and load, mounting orientation and stiffness, sensor range and bandwidth, noise and the acquisition pipeline. A classifier can perform well on an isolated target rig while learning only the difference between two convenient experimental states.

Target attribution asks a different question: when the sensor reports a change, is the target itself abnormal, or did the measured vibration change because a neighbour, load, mount or structure changed? Without independent labels, a target-only classifier cannot answer that question reliably.

The research design must therefore vary target and interferer states independently. Temporary references or command logs should establish ground truth without becoming permanent product hardware. The evaluation must report wrong-source attribution—not merely binary anomaly accuracy. A system that detects “something changed” but frequently blames the target for an interferer is not a successful attribution system.

Non-identifiability is a legitimate possible result. If target and interferer effects occupy the same subspace, if the contrast changes unpredictably after remounting, or if the sensor lacks sufficient bandwidth or coupling information, one sensor may be unable to support the desired attribution. The project must not respond by silently changing to a sensor array, cloud service or different product concept. It should record the boundary and terminate or narrow the hypothesis.

## 07.8 Ambiguity, abstention and useful coverage

A future attribution mechanism may use an explicit **Unknown** or **Interfered** state when the evidence does not support a target-fault decision. This is a post-semester research hypothesis, not a frozen RGB state for the ordinary MVP.

Abstention can be valuable only when it reduces wrong target-fault decisions while retaining useful coverage. A mechanism that labels nearly every difficult case Unknown may show low error among the few decided cases but provide little practical value. The experiment must therefore report risk/coverage or error/coverage behavior, calibration of the ambiguity score and the proportion of observations assigned to each state.

A valid Unknown gate should:

- use a separately defined ambiguity, contrast or support measure;
- block Target-Abnormal for out-of-support, ambiguous or mount-invalid observations;
- remain distinct from ordinary sensor/read/timing faults;
- reduce wrong-source labels on held-out interference and remount blocks;
- preserve useful decision coverage;
- expose rather than hide failure cases.

The user-interface meaning of Unknown is unresolved. It must not be silently mapped to the Level-1 green or red output. Any future UI should distinguish “target appears abnormal,” “target attribution unsupported” and “sensor/configuration invalid.”

## 07.9 Protected update and contamination-control hypothesis

Protected updating addresses a real risk: a target fault, changed neighbour or invalid mount may be admitted into the trusted normal model. A naive adaptive baseline can then learn the abnormal state as normal and suppress future alerts.

The broad syntheses describe buffering or quarantine, confidence and stability admission, separate target/interference envelopes, promotion, lockout, rollback and audit logs. These elements are not established as novel or effective. Generic guarded adaptation is heavily crowded and obviousness-prone.

The pre-build simulation therefore defers automatic promotion from the first PIRG experiment. The attribution contrast must pass independently before update logic is added. A later separate experiment may test:

- clean normal drift;
- changed neighbour or interference conditions;
- seeded target faults;
- wrong, delayed or missing labels;
- power interruption;
- quarantine duration and evidence;
- promotion, freeze, lockout and rollback behavior;
- auditability of every update decision;
- comparison with static and naive adaptive baselines.

Protected updating survives only if it produces a measurable cooperative effect beyond conventional alternatives. It must not be assumed to prevent contamination merely because the design includes words such as confidence, quarantine or rollback.

## 07.10 Remount validity and transfer boundary

Remounting can change orientation, coupling, amplitude and spectral structure. The Level-1 semester project must report remount sensitivity. The future attribution project must use blind held-out remounts and complete sessions rather than random windows from a single mounting.

The safest initial rule is:

1. record or detect a mount-domain change;
2. invalidate the previous model when validity is not established;
3. require controlled recommissioning;
4. test transfer mapping only as a separately preregistered hypothesis;
5. reject a transfer claim if it suppresses genuine target-fault evidence or does not outperform full recalibration.

No source proves cross-mount or cross-machine transfer. A later transfer mechanism would need to preserve fault sensitivity while correcting mount-induced variation. It would also require strong baselines and ablations because normalization and domain adaptation are crowded areas.

Mount invalidation is a validity control, not automatically a patent mechanism. Transfer is a separate hypothesis and must not be merged with the first PIRG core simply to create a larger claim narrative.

## 07.11 Relationship among future mechanisms

| Future element | Reconciled status | Relationship and boundary |
|---|---|---|
| Target/interference contrast attribution | First narrowed PIRG candidate | Test first against conventional baselines and ablations |
| Anomaly gate | Part of the narrowed decision | Prevents ordinary in-support variation from becoming Target-Abnormal; effect must be measured |
| Unknown/abstention | Part of the narrowed attribution output | Valid only if wrong-source error falls at useful coverage |
| Mount validity/invalidation | Required evidence control | Initial default is invalidation and recommissioning |
| Remount transfer mapping | Separate later hypothesis | Test only after basic invalidation is reliable |
| Quarantined shadow baseline | Separate later hypothesis | Deferred until attribution core passes |
| Promotion/rollback | Part of later protected-update experiment | Must be auditable and contamination-resistant |
| Speed/load conditioning | Conventional control or component | Strong prior-art risk; not a standalone invention story |
| Triggered FFT/resource scheduling | Ordinary implementation refinement | Baseline engineering, not the patent mechanism |
| Dense-machine field attribution | External-validity requirement | Not a mechanism and not proved by a bench rig |

These elements may appear in one research roadmap, but they must not be treated as one implemented cooperative system. The first experiment should answer the narrowest decisive question. Adding update, transfer and field claims before the attribution core works would make failure analysis harder and encourage unsupported patent language.

## 07.12 Pre-build simulation boundary

The pre-build simulation is conditional planning evidence. Its examiner, opponent, claim, cost and filing scenarios are simulations, not current legal outcomes. It does not prove that PIRG works or that a claim would survive examination.

Its controlling posture is:

- preserve the ordinary Level-1 semester build unchanged;
- redesign the broad future mechanism before testing;
- carry forward only the paired target-change/interference-change contrast question initially;
- obtain owner approval for a quantitative gate;
- use blocked, randomized, independently labelled experiments;
- compare against strong conventional baselines and ablations;
- stop or narrow the patent route when kill conditions are met;
- avoid claim drafting or material filing spend before the mechanism and evidence are concrete;
- maintain confidentiality and contemporaneous records;
- refresh patent, non-patent-literature and legal-status evidence before a filing decision;
- obtain institutional and professional review.

The simulation does not authorize a late semester feature, a hidden permanent reference sensor, public novelty claims or a patent filing. Its “redesign before testing” conclusion controls the relationship between the broad syntheses and the narrow first candidate.

## 07.13 Experimental evidence roadmap

A credible programme is gated; later stages do not begin merely because earlier plots are interesting.

### Level 1 — semester foundation

Establish stable one-sensor acquisition, controlled normal/abnormal separation, RMS/persistence, conventional FFT/Mahalanobis baselines, timing/loss/resource records and immutable configuration-linked data. This is a platform gate, not attribution evidence.

### Level 2A — controlled interference bench

Control target and interferer independently; retain one permanent product sensor; use temporary references or command logs for ground truth; randomize factorial states; collect multiple days, sessions, speeds/loads and remounts; block calibration/development/held-out partitions; select the strongest baseline prospectively; and report contrast stability, wrong-source attribution, false target alerts, missed target faults, Unknown coverage, latency, resources and ablations.

### Level 2B — field-like or real-site evidence

Use at least one independently labelable realistic coupled-frame or dense-machine setting with lawful access, safety approval, unseen conditions/remounts and ground truth independent of the product sensor. If reliable labels cannot be obtained, narrow or terminate the attribution claim.

### Quantitative gate

No final gate is approved. Pilot variance should support an owner-approved preregistration covering the primary endpoint, coverage, recall, class balance, blocked holdouts, exclusions and kill rule. Windows within one run are not independent trials.

### Suggested gated sequence

| Gate | Decision | Stop condition |
|---|---|---|
| P0 | Authorization, confidentiality and contributor control | No private mechanism work/public detail without approval |
| P1 | Reliable Level-1 platform | Repair platform before attribution work |
| P2 | Independent, repeatable target/interferer labels | Stop if labels cannot be controlled |
| P3 | Stable separable contrast geometry | Kill/redesign if collinear or unstable |
| P4 | Improvement over strongest conventional baseline | Stop patent route if gain is absent or leakage-dependent |
| P5 | Useful Unknown risk/coverage | Reject near-universal abstention |
| P6 | Correct remount validity/invalidation | Default to recommissioning when validity fails |
| P7 | Added value from protected updating | Drop update claim if no cooperative effect |
| P8 | Field-like externally valid evidence | Terminate/narrow if access or effect fails |
| P9 | Current patent, FTO, ownership and value gate | No filing when any material gate fails |

## 07.14 Prior-art and legal-status limitations

The attached syntheses reviewed a broad set of vibration-monitoring, baseline, Mahalanobis, source-attribution, speed-conditioned, remote-learning and industrial patent/non-patent-literature leads. They found substantial overlap with ordinary elements and high obviousness risk for the integrated direction.

The record remains limited:

- the search is not exhaustive;
- evidence dates are time-bounded;
- patent-family membership and legal status are jurisdiction-specific;
- status of one family member cannot be transferred automatically to another;
- an abstract or descriptive passage is not a claim chart;
- a granted claim, pending claim and abandoned claim have different implications;
- prosecution history may change the meaning or scope of a claim;
- the actual future firmware, mechanical implementation and intended jurisdictions are not frozen;
- non-patent literature on paired-intervention contrast attribution requires refresh;
- no professional patentability opinion is attached.

Before material patent spend, the project must freeze the implemented mechanism, search current official patent registers and primary literature, retrieve the actual independent and relevant dependent claims, review prosecution histories and chart every necessary element. The search should focus on the enabled mechanism and experimentally demonstrated effect rather than broad words such as vibration monitoring, confidence or adaptation.

A later search may defeat the hypothesis even after a technical success. That outcome should be accepted. Engineering value and patent value are separate gates.

## 07.15 Freedom-to-operate boundary

FTO asks whether making, using, selling, offering or importing the actual implementation in the intended jurisdiction may fall within live claims. It is not answered by showing that the project is academic, local, low-cost or different in overall purpose.

The attached record does not provide:

- a frozen commercial product implementation;
- intended countries and acts;
- a complete current live-claim set;
- element-by-element claim charts;
- dependent-claim and doctrine-of-equivalents analysis;
- prosecution-history review;
- a professional written FTO opinion.

A project may be unpatentable yet still infringe a live claim, or patentable yet still require a licence to practice another claim. Novelty and FTO are separate analyses. A local-only ESP32 implementation is not automatically safe, and an educational prototype is not assumed exempt.

Before productization, the team must freeze the implementation, identify jurisdictions and activities, retrieve current official claims, chart every required element and obtain professional advice. Any design-around must be evaluated against actual claim language and equivalents, not inferred from a high-level difference.

## 07.16 Confidentiality, contribution and institutional IPR control

The ordinary Level-1 problem statement and conventional stack may be described generically with honest boundaries. The future mechanism and evidence require stronger control pending institutional IPR review.

Potentially sensitive material includes:

- exact paired commissioning and intervention sequences;
- contrast/subspace definitions and projector construction;
- target and interference representations;
- anomaly, ambiguity, Unknown and mount-validity rules;
- update quarantine, promotion, lockout and rollback logic;
- selected bands, parameters and experimentally optimized thresholds;
- firmware, test automation and labelled mixed-source datasets;
- raw field/site data and site identity;
- negative results and ablations;
- invention notebooks, contributor chronology and draft claims.

The team should preserve repository history, hashes, firmware and toolchain versions, BOM and purchase records, photographs, calibration and timing tests, raw signals, randomization seeds, protocol versions, exclusions, baseline outputs, remount geometry and signed contribution records. Old records must not be rewritten to make a later idea appear earlier.

Ownership and inventorship are not the same as project membership. Inventorship depends on contribution to the claimed conception, while ownership depends on institutional, contractual and legal rules. The attachment set does not resolve either. The institution should review contributor records, disclosure obligations and public-release plans before a filing decision.

No detailed paper, public repository, poster, unrestricted demo video, competition submission, vendor pitch or field trial should disclose the future mechanism before institutional review. Confidentiality preserves options; it does not prove patentability or trade-secret status.

## 07.17 File/no-file decision gate

The current record supports **no filing commitment**.

### Do not file on

- the ordinary ADXL345/ESP32 MVP;
- RMS, FFT, selected bands, Mahalanobis, static baseline or triggered processing alone;
- low cost, one sensor, edge-only operation, absence of cloud or RGB/USB positioning;
- a broad desired result called single-node source attribution without an enabled mechanism;
- simulation-only evidence;
- target-only or isolated-rig accuracy;
- generic confidence gating, adaptation, remount handling or abstention language without a measured cooperative effect.

### Consider institutional or counsel review only if

- the exact future mechanism is frozen and implemented;
- paired target/interference contrast geometry is identifiable and stable;
- the mechanism beats the strongest conventional baseline on untouched interference and remount blocks at useful coverage;
- every critical element survives ablation;
- the result repeats beyond one fixture and includes independently labelled field-like evidence;
- edge resource and measurement integrity are proven;
- current primary patent and non-patent-literature searching does not defeat the mechanism;
- ownership, inventorship, confidentiality and disclosure status are resolved;
- claim value and resistance to simple design-around justify the cost;
- professional novelty, obviousness, eligibility and FTO review supports proceeding.

A negative gate should terminate or narrow the patent route while preserving the semester prototype, measurement study and publication value. A positive gate would only make the mechanism eligible for institutional/professional evaluation. It would not promise grant, validity, commercial value or FTO.

## 07.18 Current patent-development state

> **VIBEGUARD PATENT-DEVELOPMENT CURRENT STATE**
>
> - The ordinary frozen MVP is a conventional research platform and is not established as patentable.
> - Six raw research lanes are preserved as evidence sources, not votes; several legal and quantitative conclusions were downgraded or excluded.
> - Two valid syntheses support only a guarded long-term research route with high obviousness and enablement risk.
> - The broad future direction combines labelled source states, target/interference representations, ambiguity handling, protected updating and mount validity.
> - The later pre-build simulation narrows the first test to paired target-change and interference-change contrast structures, projection residuals, an anomaly gate and Unknown for unsupported observations.
> - Protected baseline promotion and remount transfer are separate later hypotheses, not implemented parts of the first PIRG core.
> - No physical Level-2 interference, attribution, ambiguity, update, transfer or field-like evidence is attached.
> - The two comparative adjudications disagree on the first patent-development gate.
> - Fresh official prior-art, non-patent-literature, legal-status and FTO review is required before material patent action.
> - Institutional ownership, inventorship, confidentiality and disclosure rules remain unresolved.
> - The present decision is no filing commitment.

The next meaningful patent-development action is not claim drafting. It is an authorized, confidential, independently labelled physical observability experiment with strong baselines and explicit kill conditions.

## 07.19 Chapter conclusion

VibeGuard’s ordinary semester architecture is valuable because it can produce a disciplined embedded prototype and a reliable measurement foundation. It is not the invention. Its sensor, feature, baseline, spectral and alerting elements are conventional, and the attached evidence does not support filing on their aggregation.

The only surviving long-term direction is a difficult and falsifiable attribution problem. The broad synthesis-level map includes source-conditioned representations, ambiguity handling, protected updating and mount validity. The later pre-build simulation appropriately narrows the first candidate to paired target-change and interference-change contrast structures with an anomaly gate and Unknown outcome. Even this narrowed mechanism remains unproved and may fail because the one-sensor observation is non-identifiable.

A credible path requires independent target/interferer labels, complete-session and remount holdouts, strong conventional baselines, critical ablations, useful abstention coverage, field-like access, edge-resource evidence and current primary-source patent review. Protected updating and remount transfer should be studied only after the attribution core passes. A negative result should stop or narrow the patent route without diminishing the semester project.

No filing decision is justified now. Only a later implemented mechanism that survives physical, legal, ownership, confidentiality and value gates should reach institutional or professional file/no-file evaluation.

## 07.S Source notes

The following original organized-workspace sources materially support Chapter 07. The validated reconciliation controls resolved wording and contradictions. The packet and attachment manifest are not substitutes for the original evidence paths.

### TIER_2 — Valid syntheses, simulation and adjudication context

- `03_CONCEPT_PORTFOLIO/VibeGuard/03_Patent_Synthesis/01_VibeGuard_Patent_Synthesis_Work_Max.md` — audited current patent-evidence synthesis, conventional-MVP conclusion, Track-C hypothesis, reliability treatment and kill criteria.
- `03_CONCEPT_PORTFOLIO/VibeGuard/03_Patent_Synthesis/02_VibeGuard_Patent_Synthesis_Standard_High.md` — independent valid synthesis, reliability audit, guarded mechanism definition and proposed evidence programme.
- `03_CONCEPT_PORTFOLIO/VibeGuard/04_PreBuild_Simulation/VibeGuard_PreBuild_Future_Patent_Case_Simulation.md` — conditional simulation, redesign-before-testing posture, narrowed paired-intervention candidate, evidence roadmap and filing boundary.
- `04_COMPARATIVE_DECISION/02_Final_Adjudications/01_Project_mC_Final_Adjudication_Work_Max.md` — VibeGuard signal/access gate and TrueMoist fallback context; not a vote or technical proof.
- `04_COMPARATIVE_DECISION/02_Final_Adjudications/02_Project_mC_Final_Adjudication_Deep_Research_High.md` — OpenBraille-first gate and VibeGuard fallback context; not a vote or technical proof.
- `04_COMPARATIVE_DECISION/COMPARATIVE_DECISION_INDEX.md` — adjudication provenance and non-voting treatment.

### TIER_3 — Controlled independent research lanes

- `03_CONCEPT_PORTFOLIO/VibeGuard/02_Raw_Research/01_VibeGuard_Patent_Research_ChatGPT_Deep_Research.md` — audited supporting lane with search leads and Level-1/Level-2 framing.
- `03_CONCEPT_PORTFOLIO/VibeGuard/02_Raw_Research/02_VibeGuard_Patent_Research_Gemini.docx` — audited supporting lane; optimistic novelty, FTO and invented quantitative conclusions excluded.
- `03_CONCEPT_PORTFOLIO/VibeGuard/02_Raw_Research/03_VibeGuard_Patent_Research_Perplexity.md` — audited supporting lane with useful located-document leads and conservative gap reporting.
- `03_CONCEPT_PORTFOLIO/VibeGuard/02_Raw_Research/04_VibeGuard_Patent_Research_Qwen.md` — low-reliability prompts and limited ideas only; simulated searches, unsupported portfolios and legal assurances excluded.
- `03_CONCEPT_PORTFOLIO/VibeGuard/02_Raw_Research/05_VibeGuard_Patent_Research_Mistral_PARTIAL_COMPILATION.md` — one partial lane with no complete verdict; unsupported patentability, Mahalanobis, infringement and FTO assertions excluded.
- `03_CONCEPT_PORTFOLIO/VibeGuard/02_Raw_Research/06_VibeGuard_Patent_Research_Microsoft_Copilot.docx` — project-fidelity support where confirmed; patent and legal conclusions downgraded.

# Part III Open-Decision Register

| ID | Decision or uncertainty | Current status | Required next action |
|---|---|---|---|
| VG-OD01 | Teacher approval of VibeGuard shift | Open; request/recommendation only | Obtain explicit approval, conditions or rejection |
| VG-OD02 | ESP32/course-platform acceptance | Open | Obtain written platform decision before procurement |
| VG-OD03 | Phase 4 and procurement | Not proved started/frozen | Authorize, verify current parts/prices/safety, then freeze BOM |
| VG-OD04 | Exact board, module and pin map | Provisional/unverified | Select approved hardware and run incoming checks |
| VG-OD05 | Rigid mount and remount repeatability | Untested | Build, version and test independent remounts |
| VG-OD06 | Sampling/timestamp integrity | Untested | Measure achieved rate, loss, saturation and FFT interference |
| VG-OD07 | Safe abnormal-state fixture | Proposed only | Obtain safety review and repeated physical acceptance |
| VG-OD08 | Level-1 classifier and numeric protocol | Logic fixed; numbers open | Preregister threshold, persistence, counts, holdouts and kill rules |
| VG-OD09 | FFT and Mahalanobis incremental value | Untested/optional | Compare after baseline; drop if non-incremental or unstable |
| VG-OD10 | Team ownership and demo fallback | Proposed only | Assign primary/backups and approve any playback fallback |
| VG-OD11 | Patent-first portfolio gate | Adjudications disagree | Select a gate/replacement rule or defer |
| VG-OD12 | Exact PIRG mechanism | Narrow candidate, not experiment-frozen | Version inputs, outputs, contrast construction and exclusions |
| VG-OD13 | Independent target/interferer ground truth | Not available | Build safe factorial rig with temporary references |
| VG-OD14 | PIRG quantitative gate and strongest baseline | Unapproved/unselected | Pilot variance, benchmark identical blocked splits, preregister |
| VG-OD15 | Contrast identifiability | Central risk, untested | Kill if held-out contrasts are collinear or unstable |
| VG-OD16 | Unknown/coverage value | Hypothesis only | Report risk/coverage; reject near-universal abstention |
| VG-OD17 | Remount validity and transfer | Invalidation proposed; transfer unproved | Blind remount study; keep recommissioning default |
| VG-OD18 | Protected updating | Deferred | Test contamination/promotion/rollback only after attribution passes |
| VG-OD19 | Edge execution of future mechanism | Unprofiled | Verify timing, memory and acquisition integrity |
| VG-OD20 | Field-like labelled access | Unsecured | Obtain authorized site or terminate/narrow attribution path |
| VG-OD21 | Fresh patent/NPL/legal-status/FTO work | Time-bounded/incomplete | Refresh official sources and obtain professional review |
| VG-OD22 | Confidentiality, ownership and inventorship | Unresolved | Apply institutional controls and preserve contribution records |
| VG-OD23 | File/no-file decision | No filing justified | Revisit only after technical, legal, ownership and value gates |

# Part III Contradiction Summary

| ID | Chapter | Issue | Controlling resolution | Residual uncertainty |
|---|---:|---|---|---|
| VG-C01 | 06 | Mahalanobis primary versus optional | RMS/persistence mandatory; Mahalanobis optional comparator | Incremental held-out value |
| VG-C02 | 06 | Proposed rate/bandwidth versus achieved performance | Pilot and measure exact hardware; record achieved limits | Module noise, aliasing and stability |
| VG-C03 | 06 | “Procurement-ready” versus approval open | Roadmap is conditional planning only | Teacher/platform/safety decision |
| VG-C04 | 06–07 | Proposed numbers presented as authoritative | Bind only after preregistration and approval | Final Level-1/2 gates |
| VG-C05 | 06 | Provisional pins/components versus frozen interface | Revalidate purchased hardware | Final board and wiring |
| VG-C06 | 06–07 | Detection language blurs attribution | Chapter 06 detects controlled state; Chapter 07 tests attribution | Single-sensor observability |
| VG-C07 | 06 | Recommended/selected versus teacher-approved | Use strongest recommendation/proposed shift wording | Written approval |
| VG-C08 | 06–07 | Historical prices/specifications/status treated as current | Preserve dates and require fresh verification | Current facts |
| VG-C09 | 06–07 | Level-1 result treated as invention | Conventional foundation and baseline only | Later technical effect |
| VG-C10 | 07 | Broad loop versus narrow first PIRG test | Broad map retained; paired contrast core tested first | Core observability/value |
| VG-C11 | 07 | Protected updating integrated versus deferred | Separate experiment after attribution passes | Cooperative effect |
| VG-C12 | 07 | Remount transfer versus invalidation | Recommissioning default; transfer separate | Transfer feasibility |
| VG-C13 | 07 | Undefined PIRG expansion | Use acronym only | Definition outside package unknown |
| VG-C14 | 07 | Adjudications choose different patent gates | Preserve both; no vote counting | Authorized gate |
| VG-C15 | 07 | Raw-lane novelty/FTO confidence | Audited syntheses control; unsupported claims excluded | Fresh official/professional review |
| VG-C16 | 07 | Simulation treated as proof | Conditional planning and redesign guidance only | Physical/legal outcome |
| VG-C17 | 07 | Unknown assumed beneficial | Require useful risk/coverage evidence | Practical coverage |
| VG-C18 | 06–07 | PIRG enters semester scope/budget | Separate scope, repository, budget and approval | Authorization of later work |

# Part III Source Ledger

The following original organized-workspace paths were materially relied upon. They are grouped by chapter and authority tier. The attachment manifest is excluded because it is file control only. The validated reconciliation controls resolved wording but is not substituted for the original evidence paths. Validated Part I controls the current project state, and validated Part II is a style and cross-concept consistency reference rather than VibeGuard technical evidence.

## Chapter 06 — TIER_1 current architecture and governance

- `01_GOVERNANCE_AND_CONTROL/01_Project_Requirements/Teacher_Project_Requirements_and_Change_Context.md`
- `01_GOVERNANCE_AND_CONTROL/02_Decision_Registers/Project_mC_Decision_Register_v1.2.md`
- `03_CONCEPT_PORTFOLIO/VibeGuard/01_Final_Architecture/Phase3C_VibeGuard_Architecture_Report_Final.md`
- `03_CONCEPT_PORTFOLIO/VibeGuard/01_Final_Architecture/Phase3C_VibeGuard_Memory_Final.md`
- `03_CONCEPT_PORTFOLIO/VibeGuard/01_Final_Architecture/Phase3C_VibeGuard_SOP_Final.md`

## Chapter 06 — TIER_2 supporting, historical and implementation evidence

- `03_CONCEPT_PORTFOLIO/VibeGuard/05_Roadmaps_and_Reference_Dossiers/HISTORICAL_Phase1C_VibeGuard_Concept_Dossier.docx` — historical concept origin only; not current architecture authority.
- `03_CONCEPT_PORTFOLIO/VibeGuard/05_Roadmaps_and_Reference_Dossiers/VibeGuard_Semester_Implementation_and_Future_Research_Roadmap.pdf` — conditional implementation, BOM, safety, validation and future-boundary proposal.
- `03_CONCEPT_PORTFOLIO/VibeGuard/PATENT_EVIDENCE_INDEX.md` — research-lane/synthesis index and exclusion context.
- `03_CONCEPT_PORTFOLIO/VibeGuard/README.md` — folder status and navigation support.
- `04_COMPARATIVE_DECISION/03_Change_Request/Project_mC_Request_to_Change_from_OpenBraille_to_VibeGuard.docx` — formal change request; not approval.

## Chapter 07 — TIER_2 valid syntheses, simulation and adjudication context

- `03_CONCEPT_PORTFOLIO/VibeGuard/03_Patent_Synthesis/01_VibeGuard_Patent_Synthesis_Work_Max.md`
- `03_CONCEPT_PORTFOLIO/VibeGuard/03_Patent_Synthesis/02_VibeGuard_Patent_Synthesis_Standard_High.md`
- `03_CONCEPT_PORTFOLIO/VibeGuard/04_PreBuild_Simulation/VibeGuard_PreBuild_Future_Patent_Case_Simulation.md`
- `04_COMPARATIVE_DECISION/02_Final_Adjudications/01_Project_mC_Final_Adjudication_Work_Max.md`
- `04_COMPARATIVE_DECISION/02_Final_Adjudications/02_Project_mC_Final_Adjudication_Deep_Research_High.md`
- `04_COMPARATIVE_DECISION/COMPARATIVE_DECISION_INDEX.md`

## Chapter 07 — TIER_3 controlled independent research lanes

- `03_CONCEPT_PORTFOLIO/VibeGuard/02_Raw_Research/01_VibeGuard_Patent_Research_ChatGPT_Deep_Research.md`
- `03_CONCEPT_PORTFOLIO/VibeGuard/02_Raw_Research/02_VibeGuard_Patent_Research_Gemini.docx`
- `03_CONCEPT_PORTFOLIO/VibeGuard/02_Raw_Research/03_VibeGuard_Patent_Research_Perplexity.md`
- `03_CONCEPT_PORTFOLIO/VibeGuard/02_Raw_Research/04_VibeGuard_Patent_Research_Qwen.md`
- `03_CONCEPT_PORTFOLIO/VibeGuard/02_Raw_Research/05_VibeGuard_Patent_Research_Mistral_PARTIAL_COMPILATION.md`
- `03_CONCEPT_PORTFOLIO/VibeGuard/02_Raw_Research/06_VibeGuard_Patent_Research_Microsoft_Copilot.docx`

## Explicit exclusions and non-evidence controls

- Software-security/configuration-scanning substitutions and active-vibration-cancellation routes are not the frozen VibeGuard design and are excluded.
- PIRG, target attribution, protected updating and remount transfer are post-semester hypotheses and are not part of the ordinary MVP.
- The attachment manifest is file control only and is not technical or patent evidence.
- Validated Part II is a style and cross-concept consistency reference only; it is not VibeGuard evidence.
- Independent research lanes, syntheses and adjudications are evidence sources or decision context, not votes.
- The Mistral transport compilation is one partial lane with no final verdict; missing conclusions were not reconstructed.
- No prior-chat context, memory, web research, current pricing, fresh patent searching or unstated assumption was used in this drafting stage.

---

**End of Project mC Master Manual — Part III.**
