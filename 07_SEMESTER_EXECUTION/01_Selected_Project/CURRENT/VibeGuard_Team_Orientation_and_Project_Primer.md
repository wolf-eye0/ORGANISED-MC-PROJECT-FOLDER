# VibeGuard Team Orientation and Project Primer

**Document status:** Semester execution baseline, revision 1.1  
**Prepared for:** Nihad P C, Sreehari K, Amith Krishna Das, Sreeprada K S and Archa Pramod  
**Research/price check date:** 9 August 2026 (India)  
**Project status:** VibeGuard is the final semester project; Phase 3C is closed, Phase 4 is open, and Phase 4A is active.

**Revision 1.1 — team-role synchronization:** Sreeprada K S retains Experimental Operations/Test/Inventory ownership and adds a supervised Firmware & Data Learning track with Sreehari K, including progressive beginner coding opportunities. Archa Pramod retains Documentation/Communication/Demonstration ownership and adds a lightweight Hardware Familiarization track with Amith Krishna Das. Subsystem ownership, architecture and technical execution boundaries are unchanged.

## 1. Read this first

VibeGuard is a small, local vibration-condition monitor. One rigidly mounted ADXL345 three-axis accelerometer observes a guarded low-voltage motor or fan rig. An ESP32 reads the sensor over SPI, removes the static/DC part of the signal, calculates simple time-domain features, and decides whether the current behavior looks normal or abnormal. The mandatory decision baseline is **RMS plus persistence**. A triggered FFT adds supporting frequency information. A common-cathode RGB LED and USB serial output show and record state. The semester system is local and does not use a cloud service.

The demonstrable semester claim is deliberately narrow:

> On a controlled teaching rig, under a documented configuration and test protocol, VibeGuard can learn a normal vibration baseline and flag a deliberately introduced, safe, repeatable abnormal condition.

That sentence is a target to test, not a statement that the team has already succeeded. All quantitative results remain **NOT YET MEASURED** until locked testing is completed.

### Evidence-status labels used in this package

| Label | Meaning |
|---|---|
| **FROZEN** | Required by the governing project package; do not change without a dated controlled engineering decision and the required technical review. |
| **SOURCE-DERIVED** | Taken from an authoritative attached project document. |
| **WEB-VERIFIED 2026-08-09** | Checked against a linked official or Indian supplier page on that date. Price and stock can change. |
| **ENGINEERING RECOMMENDATION** | A reasoned implementation choice that still needs normal team review. |
| **PROPOSED FOR APPROVAL** | A numeric criterion or protocol proposed before measurement; it is not a result. |
| **TO BE MEASURED / TO BE FROZEN AFTER PILOT** | Hardware-dependent value that must be measured using the stated procedure and then approved. |
| **UNRESOLVED** | A choice the named owner/team must close and log. |

## 2. Governing authority and change control

Current project-state control:

1. `Project_mC_Final_Selection_and_Phase4_Entry_Memo.md`
2. `Project_mC_Decision_Register_v1.3.md`

Technical and engineering control:

1. `00_Engineering_Design_Review.md`
2. `Project_mC_Decision_Register_v1.3.md`, including the inherited v1.2 history and PDR-068 through PDR-078
3. `Phase3C_VibeGuard_Architecture_Report_Final.md`
4. `Phase3C_VibeGuard_Memory_Final.md`
5. `Phase3C_VibeGuard_SOP_Final.md`
6. `05_Uncertainty_and_Test_Register.md`
7. `VibeGuard_Semester_Implementation_and_Future_Research_Roadmap.pdf`
8. `Project_mC_Teacher_Documents_Master_Evidence_Costing_and_Decision_Basis.md`
9. `VibeGuard_PreBuild_Future_Patent_Case_Simulation.md`, for future research only
10. Current official specifications and price checks where required

Decision Register v1.2 remains a valid historical predecessor and is preserved unchanged. Current status is controlled by the 2026-08-09 memo and Decision Register v1.3: the teacher verbally delegated concept choice to the team, the team selected VibeGuard, Phase 3C is closed, and Phase 4A is active. This does not imply that purchasing or building has already occurred.

Older text that made ordinary Mahalanobis the main classifier is superseded. In this semester package it is only an optional comparator after the baseline works. Older improvised-mass suggestions are also superseded by the guarded, mechanically retained eccentric requirement.

## 3. The problem in plain English

Rotating objects vibrate. A motor that is firmly mounted and turning consistently creates a repeatable vibration pattern. If the mounting, load or balance changes, the pattern may change. A human can sometimes hear or feel that change, but those judgments are subjective and difficult to reproduce.

VibeGuard turns the vibration into numbers. It establishes a baseline from documented normal runs, watches later windows of data, and raises a local abnormal indication only when the evidence remains above a threshold for a defined number of consecutive windows. The persistence rule helps reject a single bump or brief disturbance.

This is a computer-science and embedded-systems project because it combines:

- sensor communication and firmware;
- streaming data integrity;
- digital signal processing;
- a simple, explainable decision rule;
- leakage-resistant validation;
- versioned data and software evidence; and
- a human-readable physical demonstration.

## 4. Frozen Level-1 architecture

| Block | Semester implementation | Status and boundary |
|---|---|---|
| Sensing | One permanently used ADXL345 three-axis accelerometer breakout, rigidly mounted | **FROZEN.** No permanent second accelerometer. |
| Controller | ESP32-WROOM-32 DevKit; an explicitly authorized ESP32-S3 DevKit is fallback | **FROZEN MCU family.** Exact board SKU must be recorded. |
| Sensor bus | Four-wire SPI plus optional DATA_READY interrupt | **FROZEN.** I²C is not the semester sensor interface. |
| Acquisition | Timestamped, counted blocks with drop/overrun indicators | Required for credible evidence. |
| Preprocessing | Unit conversion, DC/mean removal and controlled windowing | **FROZEN functional step.** Exact constants are versioned. |
| Mandatory features | Per-axis and/or vector RMS, plus persistence | **FROZEN minimum baseline.** |
| Supporting features | Triggered Hann-windowed FFT and selected bands | **FROZEN role:** supporting/triggered, not a dense diagnostic system. |
| Optional comparator | Ordinary Mahalanobis distance | Optional only; remove if schedule, stability or explainability suffers. |
| Local state | Start/Self-check, Calibrating, Normal, Abnormal and Fault/Invalid | State transitions and reasons must be logged. |
| Visible output | Common-cathode RGB: blue Calibrating, green Normal, red Abnormal | **FROZEN.** Fault/Invalid uses a documented distinct blink pattern. |
| Data output | USB serial logging to a computer | **FROZEN.** The USB cable must support data, not charging only. |
| Demonstration plant | Guarded low-voltage 12 V DC motor or fan on a stable base, with a safely retained repeatable abnormal fixture | **FROZEN safety boundary.** |
| Connectivity | Local operation; no cloud dependency | **FROZEN.** Wi-Fi/Bluetooth are not needed for the minimum system. |

### Signal flow

1. The motor rig reaches its documented operating condition.
2. The ADXL345 samples acceleration on X, Y and Z.
3. The ESP32 reads complete samples by SPI and attaches counters/timing metadata.
4. Firmware removes each window's DC component.
5. Firmware calculates RMS and the baseline decision score.
6. Persistence requires abnormal evidence in multiple consecutive windows.
7. When configured trigger conditions occur, a Hann-windowed FFT calculates selected band evidence.
8. The state machine drives the RGB LED and emits a structured USB record.
9. A host computer saves the stream with the run, firmware, hardware, mount and rig IDs.

## 5. What the hardware does

### ADXL345 accelerometer

An accelerometer reports acceleration along three perpendicular axes. The bare ADXL345 supports ±2 g, ±4 g, ±8 g and ±16 g ranges, 3- or 4-wire SPI, I²C, a FIFO, and output data rates up to 3200 Hz. Its official supply range is 2.0–3.6 V and its I/O voltage is 1.7 V to the supply voltage. The official device ID register at address `0x00` returns `0xE5`. [[Analog Devices ADXL345 data sheet](https://www.analog.com/media/en/technical-documentation/data-sheets/ADXL345.PDF), accessed 2026-08-09]

The selected low-cost breakout may include a regulator and level shifting, but breakout layouts vary. The team will power it from the ESP32's 3.3 V rail, photograph both sides, record markings and verify device ID/readback before accepting it. A seller description is not proof that the received board is electrically identical to a photograph.

The initial acquisition setting is an **ENGINEERING RECOMMENDATION**: full-resolution ±4 g and 800 Hz output data rate, 256-sample windows, subject to pilot evidence. The ADXL345 data sheet states that bandwidth is half the output data rate. It also recommends at least 400 kHz SPI for 800 Hz and at least 2 MHz SPI for 1600/3200 Hz. The team should start SPI at 2 MHz after correct low-speed readback, then document whether timing and drop counters remain sound. Range, ODR, SPI rate and window length remain **TO BE FROZEN AFTER PILOT**.

### ESP32 development board

The preferred exact board is the Espressif `ESP32-DEVKITC-32E` containing an ESP32-WROOM-32E module. The official DevKitC V4 documentation identifies its Micro-USB port as both power and USB-to-UART communication and warns that Micro-USB, 5 V/GND-header and 3.3 V/GND-header power options are mutually exclusive. Only one board-power method may be used. [[Espressif ESP32-DevKitC V4 user guide](https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32/esp32-devkitc/user_guide.html), accessed 2026-08-09]

The semester pin map is frozen only after the exact received SKU is accepted. For the preferred DevKitC-32E, the proposed map avoids ESP32 strapping pins for chip select:

| Signal | Proposed DevKitC-32E pin | Note |
|---|---:|---|
| ADXL345 SCLK | GPIO18 | VSPI clock-capable pin |
| ADXL345 MOSI/SDI | GPIO23 | Controller-to-sensor data |
| ADXL345 MISO/SDO | GPIO19 | Sensor-to-controller data |
| ADXL345 CS | GPIO21 | Deliberately avoids GPIO5 strapping-pin dependency |
| ADXL345 INT1/DATA_READY | GPIO4 | Input; pilot first without interrupt if needed |
| RGB green | GPIO25 through resistor | Normal |
| RGB blue | GPIO26 through resistor | Calibrating |
| RGB red | GPIO27 through resistor | Abnormal |
| Grounds | Common logic ground | Sensor and RGB logic only |

This table is **PROPOSED FOR APPROVAL**, not proof of completed wiring. If an ESP32-S3 board is authorized, do not reuse these numbers: create a new wiring record from that exact board's official header documentation and a new firmware target.

### Motor, supply, base and abnormal fixture

The rig is a test plant, not part of the ESP32 power circuit. The motor uses its own switched and fused 12 V supply. The ESP32 remains USB-powered. The motor must never be powered from the ESP32, its 3.3 V rail or a computer USB port.

The preferred current part is a compact 12 V, 600 RPM N20 metal gear motor with a 3 mm D shaft. Retailer speed and mechanical claims are vendor claims; actual no-load current, startup behavior, speed consistency and temperature are **TO BE MEASURED**. A 12 V/1 A plug-in adapter is a starting source, subject to polarity, loaded-voltage and temperature acceptance.

The abnormal fixture must be repeatable and captive: for example, a clamping/set-screw 3 mm hub or keyed disc carrying an off-axis bolt, washers and a nyloc nut or equivalent positive retention, fully enclosed by a clear guard. Exact mass, radius and fastening method are **TO BE FROZEN AFTER A LOW-ENERGY PILOT**. Tape, hot glue, a binder clip, an unsecured washer, press-fit-only mass or a loose object is prohibited.

## 6. Vibration and sampling: the minimum theory

### Vibration

Vibration is repeated motion around an equilibrium position. An accelerometer sees the resulting acceleration. The measured pattern contains the behavior of the motor, gearbox, mounting structure, sensor orientation, cable forces and disturbances. Therefore, a score is not a universal property of “the motor”; it belongs to a documented configuration.

### Sampling and aliasing

Sampling converts a continuous signal into values at discrete times. If the sampling rate is too low, higher-frequency motion can appear as a false lower-frequency pattern. This is aliasing. The ADXL345's internal bandwidth is tied to output data rate, but that does not remove the need to choose an ODR that covers the controlled rig's useful content and to state the bandwidth boundary honestly.

At an 800 Hz ODR, the nominal Nyquist frequency is 400 Hz and the sensor's −3 dB bandwidth is also about 400 Hz. The team must confirm actual achieved sample timing and dropped-sample counts. “Configured at 800 Hz” is not enough.

### Windowing

A decision is made from a block or window of samples. A proposed 256-sample window at 800 Hz spans 0.32 seconds. Shorter windows respond faster but are noisier; longer windows are steadier but add latency. The chosen length and overlap must be frozen before locked testing.

## 7. The mandatory decision baseline

### DC removal

Gravity, orientation and static offset contribute a large slowly varying component. For each axis in each analysis window, calculate the mean and subtract it:

\[
x'_i = x_i - \bar{x}
\]

The same is done for Y and Z. Save enough metadata to reconstruct whether values are raw counts, g units, or DC-removed units. Raw acquired samples must remain immutable.

### RMS

Root-mean-square measures the energy-like magnitude of a zero-mean sequence:

\[
\operatorname{RMS}(x')=\sqrt{\frac{1}{N}\sum_{i=1}^{N}(x'_i)^2}
\]

The firmware may calculate per-axis RMS and/or vector RMS. The exact feature definition, scaling, numeric type and test vector belong in the firmware and parameter registers. RMS is explainable: larger repeated acceleration generally produces a larger value. It does not identify a bearing defect or prove a physical root cause.

### Calibration and threshold

Calibration observes documented normal windows after warm-up and checks sensor validity before producing baseline statistics. A threshold must be derived only from training/calibration sessions, never from the held-out final test. A robust initial form may be a normal-data percentile or a median-plus-scaled-MAD rule. The actual formula and coefficient are **TO BE FROZEN AFTER PILOT** by Sreehari, reviewed by Nihad, with Amith confirming hardware configuration.

### Persistence

A single threshold crossing can be caused by a bump. Persistence declares Abnormal only after `K` qualifying windows out of a defined sequence, and it may require a separate clear rule to return to Normal. `K`, window overlap and clear behavior are **TO BE FROZEN AFTER PILOT**. Every transition must include time, prior state, new state, score, threshold and reason code in the USB record.

## 8. Triggered FFT and selected bands

The fast Fourier transform separates a window into frequency components. Before the FFT, the DC-removed samples receive a Hann window to reduce edge discontinuity. The FFT runs only when the documented trigger fires—for example, near a baseline warning region, at periodic diagnostic intervals, or while Abnormal is being confirmed.

The team will:

1. verify the embedded FFT against an offline reference vector;
2. measure execution time and memory use;
3. inspect pilot spectra without using held-out final labels to tune them;
4. propose a small number of bands with physical or empirical justification;
5. freeze band edges and trigger logic before locked validation; and
6. report bands as supporting evidence, not as diagnosis of a named fault.

FFT size (initially 256 or 512), band limits and trigger rules are **TO BE MEASURED / TO BE FROZEN AFTER PILOT**.

## 9. Optional ordinary Mahalanobis comparator

Mahalanobis distance measures how far a feature vector is from the normal-data center while accounting for feature scale and covariance. It is useful only if there are enough independent normal sessions and the covariance estimate is stable.

For this semester:

- it is not required for minimum success;
- it cannot replace RMS plus persistence;
- it begins only after the baseline passes bench and pilot gates;
- it uses ordinary, documented features rather than a novel claim;
- it gets its own parameter/configuration ID and leakage-free split; and
- it is removed if it threatens schedule, numerical stability or explanation.

The project must not describe ordinary Mahalanobis distance as the invention or as proof of patentability.

## 10. Normal and abnormal experiments

### Normal condition

“Normal” is a physical configuration, not simply a label in a CSV file. Its record includes motor ID, base, motor clamp, supply, mount ID, sensor orientation, firmware, parameter set, warm-up, operator, run duration and environmental notes. Multiple independent sessions on separated times/days are required.

### Controlled abnormal condition

The abnormal condition is a safely introduced, repeatable change such as the approved guarded eccentric configuration. It must have a physical ground-truth definition—mass ID, radius, hub/fastener arrangement, guard ID and inspection—not “the run looked abnormal.” It must not be destructive, uncontrolled or adjusted while powered.

### Split by session, not by random window

Adjacent windows from the same run are highly similar. Randomly splitting those windows between training and test leaks information and can make results look better than they are. Keep complete sessions, days and remount events together. At least one day/remount combination should remain held out and untouched until the locked test.

### Proposed validation criteria

The roadmap's draft numbers are carried forward only as **PROPOSED FOR TECHNICAL-TEAM/PROJECT-LEAD REVIEW AND FREEZE**, not as results:

- data from at least three separated session days, including a held-out day/remount;
- sensitivity at least 90%;
- specificity at least 90%;
- no more than one false alert in a 10-minute stable-normal run;
- alert latency at most 2 seconds;
- zero unexplained lost acquisition blocks in a locked run; and
- a second operator can execute the frozen procedure.

Before labeled locked-validation use, the technical team/project lead must record whether these criteria are frozen, revised or rejected. If revised, the decision must state why. Faculty/teacher review is required only if the course, lab or faculty explicitly requires it, and any such requirement must be supported by a communication record. No criterion may be retuned after held-out results are seen, and no metric may be claimed until the corresponding raw run IDs, analysis version and confusion matrix exist.

## 11. State and output behavior

| State | RGB behavior | Meaning |
|---|---|---|
| Start/Self-check | All channels brief documented lamp test, then off or a defined pattern | Firmware has started; sensor/readback and configuration checks are running. |
| Calibrating | Blue | Normal baseline acquisition is in progress; no Normal/Abnormal claim is valid yet. |
| Normal | Green | Current score and persistence state satisfy the frozen normal rule. |
| Abnormal | Red | Frozen threshold and persistence rule have been met. It is not a fault diagnosis. |
| Fault/Invalid | Distinct documented blink pattern, never steady green | Missing sensor, wrong device ID, saturation, sample integrity failure, invalid calibration or configuration fault. |

The USB schema should contain at minimum: schema version, UTC/local timestamp basis, boot/session/run IDs, firmware version/commit, hardware revision, mount ID, rig ID, parameter ID, sample/block sequence, achieved timing/drop flags, state, scores, thresholds, FFT-trigger flag and reason code. Exact field order is frozen with a schema version.

## 12. Major build risks and how to think about them

| Risk | Why it matters | Planned response |
|---|---|---|
| Loose or changing sensor mount | Mount changes can look like machine changes. | Rigid mount, dimensions/photos, torque/fastener notes, remount register and held-out remount test. |
| Incomplete samples or overruns | Corrupts features and latency claims. | DATA_READY/FIFO or timed acquisition, sequence counters, block counters and explicit invalidation. |
| Sensor saturation | Clipped data hides actual vibration. | Saturation counter; increase range only by recorded parameter decision. |
| USB logging backpressure | Serial printing can disturb acquisition. | Buffered summaries, bounded raw-stream mode, measured throughput and separate acquisition/print counters. |
| Unsafe eccentric fixture | Can detach and injure people or damage equipment. | Positive retention, guard, low-energy pilot, power-off adjustment and pre-run inspection. |
| Unrepeatable motor speed/configuration | Normal and abnormal labels become ambiguous. | Stable supply, warm-up, configuration IDs and speed proxy/tachometer if available. |
| Window leakage | Inflates evaluation metrics. | Split whole sessions/days/remounts; freeze test set before tuning. |
| Nihad becomes a single point of failure | Integration knowledge is lost or work stops. | Named reviewer/backup for every stage, weekly handover and two-person reproducibility. |
| Scope growth | Delays credible end-to-end evidence. | Minimum system by Week 8; later weeks validate, recover and document only. |

## 13. Motor-rig safety rules

These rules apply before every powered run:

- Use only the approved low-voltage DC motor supply. Do not expose mains wiring or use an open-frame mains supply.
- Bolt or clamp the motor to a heavy, stable base. Clamp or otherwise restrain the base to the bench if needed.
- Use a mechanically retained eccentric with redundant retention appropriate to the fixture; enclose all rotating parts in a guard.
- Wear eye protection during initial and abnormal-fixture runs. Keep hands, hair, clothing, badge lanyards, tools and cables outside the guard.
- Do not leave loose test objects on the base or bench.
- Disconnect motor power and verify the shaft has stopped before adjustment. Never tighten, reposition or touch the fixture while powered.
- Use current-limited initial bring-up where lab facilities permit; include a reachable switch/emergency disconnect and a correctly selected fuse.
- Inspect guard, base, motor clamp, eccentric retention, sensor mount, strain relief and wiring before every run.
- Stop immediately for excessive heating, new harsh noise, loose hardware, visible wobble beyond the approved envelope, base motion, guard contact, smell, smoke or damaged wiring.
- After an emergency stop, quarantine the rig and create an incident/corrective-action record before another run.

Sreeprada and Archa may observe and record these checks, but they must not independently perform or approve safety-critical wiring, rotating-fixture changes or unsupervised energized tests.

## 14. What counts as semester success

Minimum credible success is not a beautiful enclosure or a sophisticated algorithm. It is a traceable end-to-end chain:

1. accepted exact components and a safe guarded rig;
2. repeatable SPI acquisition with integrity counters;
3. immutable raw normal and controlled-abnormal sessions;
4. a frozen RMS-plus-persistence baseline;
5. triggered FFT supporting evidence;
6. leakage-free held-out testing with honest metrics and failures;
7. green/blue/red behavior plus a distinct invalid state;
8. USB records that link every result to exact configurations; and
9. another trained member can reproduce the boot, calibration, run and archive procedure.

A negative result can still support a good engineering semester if the protocol is sound, the failure is preserved, the cause is investigated and claims are narrowed. Never tune after seeing locked-test labels and then report the same run as held out.

## 15. What VibeGuard does not claim

The semester project does **not** claim:

- dense factory-wide source attribution;
- bearing diagnosis, remaining useful life, predictive-maintenance certification or industrial readiness;
- universal performance across different machines, mounts or speeds;
- active vibration cancellation;
- microphone, microphone-array or acoustic diagnosis;
- cloud analytics or remote production monitoring;
- a permanent second accelerometer;
- successful PIRG operation;
- patentability, a patent grant or freedom to operate; or
- that proposed thresholds or purchased components already exist.

## 16. Team operating model

| Member | Primary responsibility | Mandatory reviewer/backup behavior | Lab role and restrictions |
|---|---|---|---|
| **Nihad P C — Technical Integration Lead / Project Manager / Configuration & Evidence Lead** | Project/system integration, architecture/configuration control, interfaces, scheduling, risk, evidence integrity, gates, coordination and system-level review | Sreehari backs up firmware/configuration; Amith backs up hardware/safety; Nihad keeps handover material current | Does not self-approve safety or locked validation; another named technical reviewer signs each such gate. |
| **Sreehari K — Firmware, DSP & Data Lead / Software Systems Mentor** | ESP32 firmware, SPI/ADXL345 acquisition, timing/integrity, RMS, persistence, FFT, optional ordinary Mahalanobis, USB schema, tools, scripts, splits and metrics | Retains firmware/DSP/data design ownership; Nihad reviews releases/parameters | Primary technical-learning mentor for Sreeprada and reviewer of all training code before controlled use. |
| **Amith Krishna Das — Hardware, Power, Rig & Safety Lead** | Procurement, acceptance, wiring, power, motor/supply, switch/fuse, base, mount, fixture, guard, repeatability and physical safety | Retains technically heavy hardware ownership | Provides selected familiarization to Archa for accurate documentation/presentation; does not train her as an alternate hardware engineer. |
| **Sreeprada K S — Experimental Operations, Test & Inventory Coordinator / Firmware & Data Learning Associate & Technical Observer** | Experiment organization, inventory, preparation, checklists/IDs, operator procedures, remounts, photographs, repeated runs, observations, failures, conformance, reproducibility and learning notes | Independent primary role; secondary pairing with Sreehari for progressive firmware/data/coding learning | May execute approved low-risk procedures and reviewed isolated training tasks; never independently alters controlled firmware/settings/splits. |
| **Archa Pramod — Documentation, Communication & Demonstration Lead / Hardware Familiarization Associate & Technical Observer** | Controlled documents, progress/minutes, faculty communication, evidence/media index, diagrams, report/presentation/demo, revision history and claim traceability | Independent primary role; secondary pairing with Amith for lightweight hardware familiarization | Observes selected work to understand components/layout/safety; does not design, modify or approve critical hardware. |

Every major task must name an owner, reviewer, backup and observer. The owner performs; the reviewer checks evidence; the backup can repeat the procedure; the observer records what actually happened. A person may fill more than one non-conflicting role, but the owner cannot be the only approver of a safety or locked-test gate.

### Secondary development tracks

Secondary technical participation supplements rather than replaces each member's primary role. Sreeprada's Firmware & Data Learning track is intended for progressive hands-on learning, including beginner coding under Sreehari's review. Archa's Hardware Familiarization track is primarily observational and explanatory, intended to make her documentation and demonstration technically accurate. Neither track transfers subsystem ownership away from Sreehari or Amith.

Learning must not interfere with critical-path implementation. The subsystem owner remains responsible for deciding when an activity is safe and appropriate for a Learning/Familiarization Associate. Sreeprada ↔ Sreehari and Archa ↔ Amith are learning pairings, not managerial reporting relationships.

**Sreeprada — progressive firmware/data learning:**

1. **Observe and understand:** Arduino IDE, ESP32 firmware structure, ADXL345/SPI, serial/data flow, RMS/persistence, FFT and how a physical run becomes a data file.
2. **Operate approved procedures:** after instruction, connect the accepted ESP32, select the approved board/port, upload an already-reviewed release, verify firmware/configuration identity, perform approved ADXL345 readback and serial capture, save run IDs, execute unmodified approved scripts and generate predefined plots.
3. **Beginner coding/test work:** after Sreehari confirms readiness, read explained firmware sections; create isolated `TRAINING` sketches, sensor/readback or serial utilities; test isolated functions; reproduce simple offline calculations; and follow written diagnostics. Training code stays separate from controlled firmware until reviewed.
4. **Controlled contribution:** if competent, submit one isolated non-safety-critical firmware/data task. Sreehari alone decides whether it enters controlled firmware; authorship is recorded honestly.

Sreeprada does not independently change controlled firmware, SPI, ODR/range, RMS, thresholds, persistence, FFT bands, validation splits or locked scripts; merge her own code; or retune after held-out results. Desired outcome: independently execute one frozen low-risk firmware/data procedure and explain its code/data flow. An isolated reviewed coding contribution is optional. This is learning, not a semester success criterion.

**Archa — hardware familiarization:**

Archa learns the names, purposes and block-level relationships of the ESP32, ADXL345/SPI, RGB indicator, USB/logic power, separate 12 V motor supply, motor, base, rigid mount/orientation, wiring logic, switch/disconnect, fuse/protection, eccentric fixture, guard and strain relief. She learns why rigid mounting/remounts matter and the safe startup/shutdown sequence.

She observes selected Amith-led inspection, assembly, mounting, power-domain, guard, abnormal-fixture and revision-review sessions. She may photograph revisions, maintain evidence links, label reviewed diagrams, document before/after configurations, create architecture diagrams, rehearse physical-system explanations and record safety checklists. She does not design power wiring, choose ratings, solder critical circuits, modify the rig/fixture, approve safety, make energized adjustments or become an alternate hardware owner.

Desired outcome: identify every major physical VibeGuard component and accurately explain its function, physical signal path, power separation and safety logic. This is familiarization, not technical ownership.

## 17. High-level semester roadmap

| Period | Outcome |
|---|---|
| Week 1 | Project/roles/folders frozen; BOM approved; orders placed only after price/stock recheck. |
| Week 2 | Components received, photographed, identified and accepted/rejected; ESP32 USB/toolchain smoke test. |
| Week 3 | ADXL345 SPI identity, register readback and stationary/acquisition integrity evidence. |
| Week 4 | Guarded motor rig and rigid sensor mount pass documented safety inspection. |
| Week 5 | Normal sessions acquired under locked configuration. |
| Week 6 | Safe repeatable abnormal sessions acquired; labels and physical ground truth reviewed. |
| Week 7 | RMS-plus-persistence end-to-end baseline and RGB/USB state behavior. |
| Week 8 | Triggered FFT integrated; minimum credible end-to-end system exists. |
| Week 9 | Remount, startup, transient and invalid-sensor tests; no unapproved features. |
| Week 10 | Final stable hardware assembly, strain relief, guard, labels and as-built pinout; regression and any required recalibration; final HW/PIN/MOUNT/RIG/FW/PARAM/SCHEMA configuration freeze; non-held-out dry run. |
| Week 11 | Locked held-out tests and signed deviation handling; no post-result tuning. |
| Week 12 | Demonstration, report, handover, checksums and final archive. |

The compressed plan reaches the same end-to-end system and validation-design preparation by Week 6. Within Week 7, final hardware stabilization, regression and configuration freeze must finish before the locked held-out test begins. Week 8 is reserved for demonstration, report, handover and archive. Detailed weekly gates are in the Execution Playbook.

## 18. Future research and PIRG boundary

PIRG and any related multi-sensor/reference research are post-semester possibilities only. They are not silently added to firmware, BOM, demo claims or Level-1 datasets. If the team later investigates future ideas, it must:

- preserve the Level-1 semester baseline unchanged;
- create a separate future-research branch and confidential directory;
- write a new hypothesis and protocol before testing;
- add any additional hardware only under a new configuration identity;
- record negative and contradictory results; and
- make no patentability statement without qualified professional review.

Good contemporaneous evidence matters even if a future idea fails. A failure can reveal a different real technical problem worth researching, but only if the original timestamps, people, configurations, raw data, photographs, code versions and negative results remain intact. Never backdate or rewrite an earlier record; append a dated correction.

## 19. Day-Zero orientation checklist

- [ ] All five members read this primer and the safety rules.
- [ ] Nihad explains the frozen Level-1 architecture without adding excluded features.
- [ ] Each member states their official primary/secondary title and confirms that learning pairings are not reporting relationships or ownership transfers.
- [ ] Sreehari explains sampling, RMS, persistence and data leakage, then opens Sreeprada's Arduino/ESP32/serial firmware-data learning record.
- [ ] Amith explains isolation, guard, disconnect and power-off adjustment, then gives Archa a component/function and physical-layout familiarization walkthrough.
- [ ] Sreeprada demonstrates ID/run-checklist use and records her first supervised firmware/data activity.
- [ ] Archa creates the meeting/source index and a technically reviewed hardware component map.
- [ ] Each primary role names a backup and performs a short handover.
- [ ] Arduino IDE, the Espressif board package, Git and a serial capture method are installed or scheduled; exact versions are recorded only after the smoke test.
- [ ] The team agrees that no purchase, pass, measurement or teacher condition will be recorded unless it actually occurs.

## 20. Glossary

| Term | Plain-English meaning |
|---|---|
| Accelerometer | A sensor that measures acceleration along axes. |
| Axis | One direction of measurement: X, Y or Z. |
| ODR | Output data rate: how often the sensor produces a new sample. |
| Bandwidth | Frequency range the sensor can meaningfully pass; for ADXL345 it is nominally ODR/2 at the −3 dB point. |
| SPI | A clocked digital link using SCLK, MOSI, MISO and chip select. |
| Sample | One X/Y/Z measurement at a point in time. |
| Window/block | A finite group of samples analyzed together. |
| DC removal | Subtracting the window mean so static gravity/offset does not dominate vibration features. |
| RMS | Root-mean-square; an energy-like magnitude of a signal window. |
| Persistence | Requiring evidence across multiple windows before changing state. |
| FFT | A calculation that estimates how signal energy is distributed over frequency. |
| Hann window | A taper applied before FFT to reduce edge-discontinuity leakage. |
| Mahalanobis distance | A multifeature distance from the normal-data center that accounts for covariance. Optional here. |
| Calibration | A controlled process that creates/checks a normal reference before monitoring. |
| Ground truth | The documented physical condition that justifies a label. |
| Data leakage | Information from the test condition entering training/tuning, invalidating an honest test. |
| Held-out test | Data kept untouched until firmware, parameters and protocol are frozen. |
| Configuration | A complete identified combination of hardware, mount, rig, firmware and parameters. |
| Immutable raw data | Original acquired files that are never edited or overwritten. |
| PIRG | A future-research concept outside the semester Level-1 implementation. |

## 21. FAQ and common misconceptions

**“The LED turned red, so we diagnosed a bearing fault.”**  
No. Red means the frozen score and persistence rule judged this controlled configuration abnormal. It does not name a fault.

**“Can we add another accelerometer to improve the demo?”**  
No permanent second sensor belongs in the semester architecture. A later research protocol is separate.

**“Why not train and test on randomly shuffled windows?”**  
Because neighboring windows from one run share speed, mounting, noise and history. Keep whole sessions/days/remounts together.

**“Is FFT the classifier?”**  
No. RMS plus persistence is mandatory. FFT is triggered supporting evidence and may add selected band features.

**“Is Mahalanobis required?”**  
No. It is an optional comparator only after the baseline works, and it is the first algorithm removed when time is tight.

**“Can the motor and ESP32 share the USB supply?”**  
No. The motor has a separate switched/fused 12 V source. The ESP32 is powered by its data-capable USB cable.

**“Can we hold a washer on the shaft with glue or tape?”**  
No. The eccentric must have positive mechanical retention and a guard.

**“Can Sreeprada learn coding and contribute?”**  
Yes. She may progressively operate frozen procedures, create isolated training code and submit a small non-safety-critical contribution under Sreehari's review. Training code stays separate until reviewed; Sreehari retains firmware/DSP/data ownership.

**“Is Archa expected to become a hardware builder?”**  
No. Amith familiarizes her with components, layout, power separation, mounting and safety so her documentation and demonstration are accurate. Amith retains hardware/safety ownership and the heavy technical work.

**“Can Sreeprada or Archa make a quick threshold or wiring change?”**  
They may record and propose a change. Sreeprada cannot independently change controlled firmware/thresholds; Archa cannot independently change wiring/rig hardware. The subsystem owner controls implementation and review.

**“A failed experiment is embarrassing—can we remove it?”**  
No. Preserve it, mark it failed, link the error/corrective-action record and keep raw evidence. Honest failure strengthens engineering traceability.

**“Do live supplier prices prove we bought the parts?”**  
No. They are dated planning estimates. Only an actual invoice and receiving record establishes purchase.

**“Does the future patent-case simulation mean VibeGuard is patentable?”**  
No. It only motivates careful evidence preservation. This package makes no patentability or grant claim.

## 22. Current official and market references

Specifications and prices below were checked on 9 August 2026; recheck immediately before ordering.

- [Analog Devices ADXL345 data sheet, Rev. G](https://www.analog.com/media/en/technical-documentation/data-sheets/ADXL345.PDF)
- [Espressif ESP32-DevKitC V4 user guide](https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32/esp32-devkitc/user_guide.html)
- [Espressif ESP32-WROOM-32E/32UE data sheet](https://documentation.espressif.com/esp32-wroom-32e_esp32-wroom-32ue_datasheet_en.html)
- [Espressif Arduino-ESP32 installation guide](https://docs.espressif.com/projects/arduino-esp32/en/latest/installing.html)
- [Arduino-ESP32 3.3.11 documentation](https://docs.espressif.com/projects/arduino-esp32/)
- [Robu: Espressif ESP32-DevKitC-32E, ₹1,079 including GST, listed in stock](https://robu.in/product/espressif-esp32-devkitc-esp32-wroom-3-2e-development-board/)
- [Evelta: exact DevKitC-32E alternate listing, ₹947.54 including GST; orderability must be reconfirmed](https://evelta.com/esp32-devkitc-32e-esp32-wroom-32e-development-board-4mb-flash-pcb-antenna/)
- [Robocraze: ADXL345 breakout, ₹249 including GST, 148 listed](https://robocraze.com/products/adxl-345)
- [Probots: alternate GY-291 ADXL345 module, ₹199 including GST, listed in stock](https://probots.co.in/gy-291-adxl345-3-axis-digital-accelerometer-sensor-module.html)
- [Robocraze: 12 V 600 RPM N20 motor, ₹233 including GST, 62 listed](https://robocraze.com/products/600-rpm-12v-n20-dc-metal-gear-motor-with-cable)
- [Robu: alternate 12 V 600 RPM N20 motor, ₹229 including GST, listed in stock](https://robu.in/product/n20-12v-600-rpm-micro-metal-gear-motor/)
- [Robocraze: 12 V/1 A adapter, ₹115 including GST, 72 listed](https://robocraze.com/products/12v-1a-power-adapter)
- [Robocraze: common-cathode RGB LED pack, ₹30 including GST, 4 listed](https://robocraze.com/products/rgb-led-common-cathode-pack-of-10)

## 23. Unresolved team questions

These are not blockers to orientation, but they must be closed by dated records before the relevant gate:

1. **Quantitative-criteria control:** the technical team/project lead must review and freeze or revise the proposed criteria before labeled locked-validation use. Faculty/teacher review applies only if explicitly required and supported by a communication record.
2. **Procurement:** confirm delivery postcode, shipping/GST invoice total, exact stock and return window on order day.
3. **Lab:** confirm availability and calibration/status of multimeter, bench current-limited supply, tachometer/stroboscope (optional), soldering station, eye protection and guard fabrication facilities.
4. **Mechanical:** select the exact base, motor clamp, 3 mm captive eccentric hub and guard design; freeze mass/radius only after low-energy inspection and pilot.
5. **Firmware:** freeze Arduino IDE, Espressif Arduino core (current official documentation is 3.3.11), FFT implementation and host capture versions after a reproducible smoke test.
6. **Timing:** confirm the actual semester start date, lab access days and whether the 12-week or 8-week calendar is active.
7. **Data governance:** select the approved shared repository/storage location and access/backup owners without placing confidential future-research notes in the public semester report.
