# Source Extraction

- Chapter: `06` — VibeGuard Frozen Architecture and Semester Scope
- Authority tier: `TIER_2`
- Manual treatment: `CORE_OR_SUPPORTING`
- Original source: `03_CONCEPT_PORTFOLIO/VibeGuard/05_Roadmaps_and_Reference_Dossiers/VibeGuard_Semester_Implementation_and_Future_Research_Roadmap.pdf`
- Current SHA-256: `8702d859cdcf816afb2ac31673759a0382348fb69b8e6a4c65120b7c7fe0deff`
- Extraction method: `PDFTOTEXT_LAYOUT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

Topic: VibeGuard - Semester Implementation and Future Research Roadmap


                                                      PROJECT mC

                     VIBEGUARD
              SEMESTER IMPLEMENTATION
            AND FUTURE RESEARCH ROADMAP
       Frozen Level-1 Build Plan, Validation Programme and Post-Semester PIRG
                                     Research Path

                           Course                                          PBCST504 - Microcontrollers Micro Project

                                                                 B.Tech Computer Science and Engineering (Cyber
Programme
                                                                 Security)

Group                                                            Group 8

Project Coordinator                                              Ms. Sagna L T, Assistant Professor, CSE (CY)

Prepared for                                                     Semester implementation approval and execution

Date                                                             03 August 2026

Document status                                                  Teacher-facing implementation dossier; controlled draft


  Controlling decision
  This dossier implements only the frozen VibeGuard Level-1 semester architecture: one rigidly mounted
  ADXL345-class accelerometer, one ESP32, local normal-versus-induced-abnormal classification, RGB indication
  and USB evidence. PIRG remains a separate, unbuilt post-semester research hypothesis.


  Patent boundary
  The ordinary semester build is conventional and is not represented as a patent-ready invention. Any future
  filing decision requires new physical evidence, refreshed prior-art work, institutional IPR review and
  professional advice.


 Prepared from the controlled Project mC authority set and the Master Evidence, Costing and Decision Basis. This document is an
             engineering implementation plan, not legal advice, a patent opinion or freedom-to-operate clearance.


   Dept. of CSE (CY)                              PBCST504 - Microcontrollers                                         Page 1
                             Dept. of CSE (CY)          PBCST504 - Microcontrollers         Page 1

                                Topic: VibeGuard - Semester Implementation and Future Research Roadmap


Document control and approval use
                            Control item                                                        Value

                                                                    Frozen VibeGuard Level-1, single-node ADXL345-class
Architecture baseline
                                                                    sensor + ESP32

Expected semester budget                                            Approximately ₹2,200

Protected conservative envelope                                     Approximately ₹3,900; below the ₹5,000 ceiling

                                                                    Reach minimum demonstrable system by Week 8; Weeks 9-
Core implementation window
                                                                    12 reserved for validation, recovery and presentation

                                                                    PIRG only after semester foundation; separate folder,
Future research
                                                                    budget, evidence and confidentiality

                                                                    This dossier becomes the controlling build plan after teacher
Primary project record
                                                                    approval


Approval checkpoints required before procurement freeze
 1. Teacher approval of the change from OpenBraille to VibeGuard and the exact Level-1 semester scope.
 2. Confirmation whether the effective build window is approximately eight weeks or the full twelve-week plan.
 3. Approval of the selected ESP32 board variant and procurement source.
 4. Faculty/laboratory safety review of the powered motor, shaft guard and retained eccentric-mass fixture.
 5. Approval of a quantitative Level-1 held-out validation protocol before the locked test.


Executive implementation decision
   Recommended semester build
   Build VibeGuard as a low-cost, single-node embedded vibration-monitoring prototype that distinguishes a
   controlled normal rig state from a repeatable induced-abnormal state. Use RMS plus persistence as the
   minimum classifier; add triggered FFT/bands and ordinary Mahalanobis only as comparisons after the baseline
   works.


VibeGuard is selected because its main risks - sensor authenticity, rigid coupling, stable acquisition, repeatable fault
injection, threshold selection and data leakage - can be isolated through scripted experiments and logs. Its expected
budget leaves more recovery headroom than OpenBraille, and the team’s strongest capabilities align with ESP32
firmware, signal processing, USB evidence and quantitative validation.
The project should not be described as a complete industrial predictive-maintenance product. The correct semester
claim is a controlled proof that a low-cost embedded node can acquire vibration, establish a normal condition, detect
a deliberately introduced abnormal condition and report the result locally without cloud processing.

Success definition at a glance
                    Layer                             Required semester result                           Evidence

                                                                                         Acceptance checklist, axis verification,
                                               Stable ESP32 + ADXL345 SPI acquisition
Hardware                                                                                 ODR record, dropped-block and saturation
                                               on a rigid target mount
                                                                                         counters

                                                                                         Rig configuration IDs, photos, RPM/load
                                               Safe, repeatable normal and induced-
Rig                                                                                      notes, retained eccentric mass and guard
                                               abnormal operating states
                                                                                         inspection

                                                                                         Frozen calibration, state logs,
                                               RMS threshold with persistence works
Minimum decision                                                                         classification latency and held-out
                                               locally
                                                                                         confusion matrix

                                               FFT/bands and ordinary Mahalanobis are    Feature plots/tables, resource use and
Secondary analysis
                                               compared without delaying the baseline    comparator results

      Dept. of CSE (CY)                              PBCST504 - Microcontrollers                                          Page 2
                                Dept. of CSE (CY)          PBCST504 - Microcontrollers         Page 2

                             Topic: VibeGuard - Semester Implementation and Future Research Roadmap


                   Layer                            Required semester result                            Evidence

                                                                                        Live demonstration and exportable
Output                                      Clear RGB state and USB evidence
                                                                                        CSV/log file

                                                                                        Negative-results log, remount records and
Honesty                                     Limitations and failed runs are preserved
                                                                                        scope statement


1. Purpose, audience and scope
1.1 Purpose
This document converts the approved Phase 3C VibeGuard architecture into a procurement-ready and execution-
ready semester plan. It defines the exact hardware, interfaces, mechanical test rig, firmware modules, validation
controls, team responsibilities, budget, schedule, risks, outputs and future-research boundary.

1.2 Audience
 • Project coordinator and teacher: approval, scope control, safety and review gates.
 • Five-member student team: subsystem ownership, integration sequence and evidence requirements.
 • Department laboratories: equipment booking, safety assistance and optional measurement support.
 • Institutional innovation/IPR reviewers: separation of the public semester prototype from confidential future
   research.

1.3 Scope hierarchy
                Scope tier                                  Included                                  Not included

                                            One target-mounted sensor; normal           Mixed-source attribution, field
Semester Level 1                            versus induced abnormal; local              deployment, cloud platform, RUL or
                                            processing; RGB and USB evidence            patent claim

                                            PIRG target/interferer research after a
Post-semester Level 2                                                                   Assumed success or automatic filing
                                            stable Level-1 platform exists

                                            Only after later validation and
Commercial/industrial                                                                   Any promise in the current project
                                            professional review


2. Engineering identity and problem definition
2.1 Engineering identity
VibeGuard is a passive edge condition-monitoring system. Its defining feature is not the accelerometer itself, but the
local interpretation of vibration on constrained embedded hardware. It targets educational and small-enterprise
contexts where expensive industrial monitoring infrastructure may be unavailable.

2.2 Semester engineering hypothesis

   Hypothesis to test
   A low-cost target-mounted accelerometer and ESP32 can consistently distinguish a controlled normal operating
   condition from a deliberately introduced abnormal-vibration condition using lightweight local analysis,
   without cloud processing.


2.3 What the hypothesis does not claim
 • It does not identify a real bearing defect or predict remaining useful life.
 • It does not prove that one sensor can attribute vibration to the correct machine in a dense factory.
 • It does not establish universal thresholds across motors, mounts or environments.
 • It does not claim that FFT, Mahalanobis distance or edge execution is novel.

    Dept. of CSE (CY)                              PBCST504 - Microcontrollers                                         Page 3
                             Dept. of CSE (CY)           PBCST504 - Microcontrollers         Page 3

                             Topic: VibeGuard - Semester Implementation and Future Research Roadmap


3. Frozen system architecture


                           Figure 1. Frozen Level-1 architecture and explicit semester scope boundary.

3.1 Subsystem boundaries
           Subsystem                              Inputs                          Outputs                       Owner acceptance

                                12 V power, normal/abnormal          Repeatable vibration transmitted    Guarded, stable, labelled and
Mechanical target rig
                                fixture state                        to target housing/base              reproducible

                                Mechanical vibration, 3.3 V                                              Correct axes, no saturation,
Sensor/mount                                                         Timestamped X/Y/Z samples
                                power, SPI clock/control                                                 documented mount ID

                                SPI samples and interrupt/FIFO                                           Stable ODR, zero block loss in
Embedded acquisition                                                 Raw windows, integrity counters
                                state                                                                    locked run

                                                                     Time features, triggered            Versioned, deterministic and
Feature pipeline                Raw windows
                                                                     spectra/bands                       reproducible

                                Calibrated baseline and current      Calibrating/Normal/Abnormal         Frozen thresholds and
Decision/state
                                features                             state                               persistence

                                                                                                         Teacher-readable demonstration
Human/evidence interface        State and records                    RGB indication, USB CSV/logs
                                                                                                         and audit trail


    Dept. of CSE (CY)                                  PBCST504 - Microcontrollers                                               Page 4
                              Dept. of CSE (CY)             PBCST504 - Microcontrollers             Page 4

                                Topic: VibeGuard - Semester Implementation and Future Research Roadmap


4. Detailed hardware architecture and BOM
4.1 Required purchased and fabricated items
        Item                    Qty            Exact semester role             Expected          Conservative       Acceptance/
                                                                                                                 procurement rule

                                                                                                                Verified WROOM-32
                                               Main controller: SPI                                             DevKit baseline;
ESP32 development                              acquisition, local                                               ESP32-S3 is
                        1                                               ₹400               ₹899
board                                          processing, RGB and                                              authorized fallback.
                                               USB                                                              Confirm pinout, USB-
                                                                                                                UART and regulator.

                                                                                                                Buy from a reputable
                                                                                                                source; verify board
                                               Rigidly mounted tri-
ADXL345 breakout        1                                               ₹229               ₹350                 layout, axes, ODR,
                                               axis vibration sensor
                                                                                                                noise and saturation
                                                                                                                before integration.

                                                                                                                Choose a stable
                                                                                                                mounting face and
12 V geared motor or                           Controlled target test
                        1                                               ₹215               ₹300                 guarded shaft. RPM is
suitable fan                                   article
                                                                                                                metadata, not the
                                                                                                                differentiator.

                                                                                                                Confirm polarity,
12 V, 1 A regulated                            Separate motor-rig
                        1                                               ₹140               ₹330                 connector and
adapter                                        supply
                                                                                                                current margin.

                                               Green Normal, Blue                                               Three separate LEDs
Common-cathode
                        1 set                  Calibrating, Red         ₹25                ₹65                  are acceptable if
RGB LED + resistors
                                               Abnormal                                                         clearer.

                                                                                                                Breadboard only for
                                               Stable final                                                     bring-up; final SPI
Perfboard               1                      sensor/controller        ₹58                ₹85                  wiring should be
                                               interface                                                        short and strain-
                                                                                                                relieved.

                                               SPI, low-voltage                                                 Separate motor-
Wires, headers and
                        1 lot                  power and USB-           ₹180               ₹250                 current paths from
connectors
                                               support connections                                              sensor/logic paths.

                                                                                                                Local allowance;
                                               Repeatable
Heavy base and rigid                                                                                            preserve
                        1 set                  mechanical coupling      ₹300               ₹500
sensor mount                                                                                                    CAD/measurements,
                                               and safe support
                                                                                                                photos and mount ID.

                                                                                                                Mass must be
                                               Safe, repeatable                                                 mechanically
Eccentric mass,
                        1 set                  induced abnormal         ₹200               ₹350                 retained and
guard and fasteners
                                               condition                                                        operated behind a
                                                                                                                guard.

                                               Decoupling, switch,
Passives and                                                                                                    Finalize ratings after
                        1 lot                  DC jack,                 ₹150               ₹280
protection                                                                                                      motor procurement.
                                               fuse/protection

                                               Logistics and one
Delivery/replacement                                                                                            Not a hidden feature
                     1                         controlled rework        ₹300               ₹500
allowance                                                                                                       budget.
                                               margin


  Budget decision
  Expected semester planning total: approximately ₹2,200. Protected conservative envelope: approximately
  ₹3,900. The future PIRG rig, second motor, temporary reference instruments, patent search and professional
  fees are not included.


    Dept. of CSE (CY)                                 PBCST504 - Microcontrollers                                          Page 5
                                Dept. of CSE (CY)            PBCST504 - Microcontrollers          Page 5

                                 Topic: VibeGuard - Semester Implementation and Future Research Roadmap


4.2 Reusable or institutional equipment
               Equipment                                           Use                                    Required status

                                                Firmware, serial logs, data analysis and
Laptop with Arduino IDE and Python                                                          Assumed available
                                                reports

Soldering station and hand tools                Final perfboard and connectors              Book before Week 3

                                                Supply, continuity and basic current
Digital multimeter                                                                          Required
                                                checks

                                                SPI timing, rail noise and dropped-sample
Oscilloscope or logic analyzer                                                              Strongly useful; borrowed
                                                debugging

Bench supply with current limit                 Safe motor and controller bring-up          Strongly recommended

Tachometer/RPM reference                        Rig metadata and repeatability              Useful but optional

Calipers and fabrication tools                  Bracket, guard and base measurements        Required for mount repeatability

                                                Mount/remount evidence and demo
Camera                                                                                      Required evidence tool
                                                recording


5. Mechanical test rig and safety


            Figure 2. Proposed controlled rig. The final dimensions and motor variant remain procurement-dependent.

5.1 Rig design rules
1. Mount the motor/fan to a heavy base using bolts or a rigid bracket. Do not rely on hand pressure, foam tape or a
   loose table surface.
2. Mount the ADXL345 rigidly to the target housing or a documented target bracket. Magnetic, foam or soft adhesive
   mounts are prohibited for the final evidence run.
3. Create the abnormal state with a small, retained eccentric mass or another repeatable safe method. Record mass,
   radius, position, speed/load and configuration ID.
4. Install a physical shaft guard and an emergency power disconnect before abnormal operation.
5. Run first at low voltage/speed or under current-limited supply. Inspect fasteners and the eccentric fixture before
   every session.
6. Keep the ESP32 and sensor wiring outside the rotating hazard area and strain-relieve the short SPI connection.

5.2 Safety stop conditions
 • Visible movement of the motor base or guard.
 • Loosening, cracking or movement of the eccentric mass or shaft fixture.
   Dept. of CSE (CY)                                   PBCST504 - Microcontrollers                                          Page 6
                                 Dept. of CSE (CY)           PBCST504 - Microcontrollers         Page 6

                           Topic: VibeGuard - Semester Implementation and Future Research Roadmap


 • Abnormal heating, smell, sparking, adapter instability or repeated resets.
 • Sensor/bracket detachment or wiring entering the rotating zone.
 • A faculty/lab reviewer requests suspension or redesign.


6. Electrical integration and provisional pin map
6.1 Power domains
             Domain                         Source                           Loads                              Rule

                                                                                                  Low-voltage only; local
                              ESP32 USB input and 3.3 V                                           decoupling at sensor; do not
Logic/sensor                                                   ESP32, ADXL345, RGB LED
                              regulator                                                           power the motor from USB or
                                                                                                  ESP32 regulator

                                                                                                  Keep motor-current wiring
                                                                                                  separate. A common ground is
                              Separate 12 V adapter with
Motor rig                                                      Motor/fan only                     not required unless a later
                              switch/protection
                                                                                                  controlled interface explicitly
                                                                                                  needs it.

                                                                                                  Data/control only; do not use
Laptop/USB                    Laptop USB                       ESP32 programming and logs
                                                                                                  as the motor power path


6.2 Provisional ESP32-WROOM-32 DevKit pin assignment

  Implementation note
  This is a Phase 4 wiring proposal, not a source-file mandate. Revalidate every pin against the exact purchased
  board. ESP32-S3 uses a different approved pin map.


               Signal                 ADXL345 / output               Provisional ESP32 pin                      Notes

                                                                                                  Use local 0.1 µF decoupling at the
3.3 V                         VCC                              3V3
                                                                                                  breakout

                                                                                                  Short return path; avoid motor-
Ground                        GND                              GND
                                                                                                  current routing

                                                                                                  Start at a conservative clock;
SPI clock                     SCL/SCLK                         GPIO 18                            increase only after integrity
                                                                                                  testing

SPI MOSI                      SDA/SDI                          GPIO 23                            ESP32 to sensor

SPI MISO                      SDO                              GPIO 19                            Sensor to ESP32

SPI chip select               CS                               GPIO 5                             Dedicated output

                                                                                                  Optional but recommended for
Data-ready interrupt          INT1                             GPIO 4
                                                                                                  stable timing

                                                                                                  Common-cathode LED or
RGB green                     LED + resistor                   GPIO 25
                                                                                                  separate indicator

RGB blue                      LED + resistor                   GPIO 26                            Calibrating

RGB red                       LED + resistor                   GPIO 27                            Abnormal/fault indication

                                                                                                  Logging, commands and
USB serial                    On-board USB-UART                Laptop USB
                                                                                                  firmware upload


6.3 Wiring acceptance checklist
 • Board powers without motor connected; 3.3 V rail measured and stable.
 • ADXL345 device ID and axis response verified before high-rate acquisition.
 • SPI wiring kept short; final evidence build soldered or locked in a rigid connector.
    Dept. of CSE (CY)                            PBCST504 - Microcontrollers                                             Page 7
                            Dept. of CSE (CY)         PBCST504 - Microcontrollers            Page 7

                                 Topic: VibeGuard - Semester Implementation and Future Research Roadmap


 • No sensor saturation during normal or induced-abnormal pilot runs.
 • USB logs remain stable while the motor is switched and while the abnormal state is active.


7. Firmware and software architecture


                         Figure 3. Staged pipeline. The minimum RMS/persistence path controls schedule risk.

7.1 Firmware module breakdown
                     Module                                     Responsibility                             Required outputs/tests

                                                 Board variant, pin map, ODR, range, window     Human-readable configuration block printed
Configuration manager
                                                 size, threshold version and build ID           at startup and stored with logs

                                                 Initialization, device ID, range/ODR,          Axis test, known orientation check and read-
ADXL345 driver
                                                 burst/FIFO reads and interrupt status          error counter

                                                 Timestamp samples/windows and maintain         Measured achieved sample rate; zero locked-
Acquisition engine
                                                 loss/overrun counters                          run block loss

                                                 Mean/DC removal; optional Hann window          Deterministic output verified against offline
Preprocessor
                                                 for FFT; scaling and validation                script

                                                 RMS, peak, standard deviation, crest factor
Time-feature engine                                                                             Unit tests on stored windows
                                                 and optional kurtosis

                                                 Normal baseline, threshold and consecutive-    Calibrating/Normal/Abnormal transitions
Persistence classifier
                                                 window logic                                   and threshold log

                                                 Compute spectrum only when scheduled or
Triggered FFT/bands                                                                             Frequency-resolution and latency record
                                                 triggered

                                                 Regularized normal-space score; optional       Offline/embedded agreement and
Mahalanobis comparator
                                                 comparison only                                RAM/timing record

State/output manager                             RGB state and fault behavior                   Visible deterministic indication

                                                 CSV logs, metadata, start/stop/calibrate
USB logger/command interface                                                                    Recoverable files with schema/version
                                                 commands

                                                 Saturation, read errors, timing overruns and
Health monitor                                                                                  No silent acquisition failure
                                                 configuration faults


7.2 Repository and configuration structure
                              Folder/file                                                             Purpose

firmware/                                                                ESP32 source, libraries, board configuration and release tags


    Dept. of CSE (CY)                                   PBCST504 - Microcontrollers                                                Page 8
                                  Dept. of CSE (CY)            PBCST504 - Microcontrollers            Page 8

                                  Topic: VibeGuard - Semester Implementation and Future Research Roadmap


                               Folder/file                                                               Purpose

                                                                          Wiring record, BOM, datasheets, board photos and mount
hardware/
                                                                          CAD/dimensions

rig/                                                                      Motor, base, guard and abnormality configuration IDs

data/raw/                                                                 Immutable raw or minimally transformed session files

data/processed/                                                           Versioned feature exports generated by scripts

analysis/                                                                 Python notebooks/scripts, metrics and plots

tests/                                                                    Unit tests, acceptance checklists and locked-run protocol

docs/                                                                     Teacher reports, weekly reviews, risk and decision logs

                                                                          Access-restricted future-research material; not used in semester
future_pirg_private/
                                                                          grading


8. Signal-processing and decision logic
8.1 Acquisition parameters to resolve in pilot testing
                   Parameter                                    Starting proposal                                  Decision rule

                                                                                                   Increase only if saturation is observed;
Range                                             Start at ±4 g full-resolution mode
                                                                                                   record every change

                                                  Start at 800 Hz; evaluate 1,600 Hz if spectral   Use the lowest rate that captures
Output data rate
                                                  evidence requires it                             discriminating energy with stable SPI timing

                                                                                                   Freeze before locked validation; overlap
Window                                            256 samples at 800 Hz or equivalent duration
                                                                                                   must be reported

                                                                                                   Triggered/periodic comparison; not always-
FFT                                               256 or 512 points with Hann window
                                                                                                   on if it threatens acquisition

                                                  Multiple complete normal sessions, not one       Separate calibration/training sessions from
Normal calibration
                                                  short run                                        held-out sessions

                                                  Derived from normal distribution with
Threshold                                                                                          Do not change after viewing held-out results
                                                  owner-approved rule

                                                  Require abnormal evidence for consecutive        Select on calibration data; report
Persistence
                                                  windows/time                                     classification latency

                                                  Select from pilot evidence and physical
Bands/features                                                                                     Freeze the list before held-out testing
                                                  plausibility


8.2 Minimum classifier
The minimum classifier is a calibrated RMS threshold with persistence. The firmware calculates the vibration
magnitude or a predeclared axis combination, estimates a normal baseline from approved calibration sessions, and
raises the Abnormal state only when the threshold is exceeded for the approved persistence period. A single transient
shock should not automatically become a persistent machine fault.

8.3 Triggered FFT and band features
FFT analysis is used to explain and compare the state change, identify repeatable spectral components and support
later research. It is triggered when the low-cost stage crosses a pre-trigger or at scheduled diagnostic intervals. The
report must disclose sample rate, window length, frequency resolution, overlap and selected bands.

8.4 Ordinary Mahalanobis comparator
Mahalanobis distance may be implemented as an optional normal-space comparator over a small feature vector. It
must use regularized covariance and must be benchmarked against the simpler RMS/persistence baseline. The
semester project succeeds without it if the minimum classifier and evidence programme are complete.


       Dept. of CSE (CY)                                 PBCST504 - Microcontrollers                                                    Page 9
                                   Dept. of CSE (CY)            PBCST504 - Microcontrollers              Page 9

                            Topic: VibeGuard - Semester Implementation and Future Research Roadmap


8.5 State-machine behavior
             State                       Entry condition                      Output                        Exit/exception

                                Power-on, configuration and                                        Fault if sensor or configuration
STARTUP/SELF-CHECK                                               Blue pulse / USB status
                                sensor identity checks                                             is invalid

                                                                                                   Restart if saturation,
                                Approved normal session and
CALIBRATING                                                      Blue                              movement or timing fault
                                stable acquisition
                                                                                                   occurs

                                Features inside calibrated                                         Abnormal evidence enters
NORMAL                                                           Green
                                bounds                                                             persistence counter

                                Threshold/persistence rule                                         Return only after approved
ABNORMAL                                                         Red
                                satisfied                                                          recovery/hysteresis rule

                                Sensor read error, saturation,
                                                                 Logged fault; distinct visible    Requires operator action or
FAULT/INVALID                   timing loss or mount-invalid
                                                                 pattern if implemented            controlled restart
                                condition


9. Data and evidence management
9.1 Required session metadata
 • Project, firmware and configuration version.
 • Sensor board identity, axis orientation, range, ODR and SPI clock.
 • Mount ID, photographs, fasteners/adhesive method and whether the sensor was remounted.
 • Motor/fan identity, supply voltage, speed/load proxy and abnormality-fixture configuration.
 • Session date/time, operator, target state and any transient events.
 • Sample count, lost blocks, read errors, saturation count and timing statistics.
 • Threshold/feature version and whether the session was calibration, development or locked hold-out.

9.2 Data split rule

  Leakage prevention
  Never randomly split windows from the same continuous run into training and test sets. Hold out complete
  sessions, days and remounts so the result tests repeatability rather than memorizing one recording.


9.3 Evidence package for final review
                       Evidence file                                                       Minimum content

                                                                 Exact board, sensor, pin map, sample rate, range, window,
Configuration record
                                                                 feature and threshold version

BOM and procurement record                                       Seller, date, unit cost, delivery and acceptance result

                                                                 Annotated photos, dimensions, safety inspection and state
Rig record
                                                                 definitions

Session register                                                 Every run, including failures and exclusions with reasons

Raw/processed data                                               Immutable original files and reproducible processing scripts

                                                                 Confusion matrix, false alerts, missed detections, latency,
Validation report
                                                                 resource use and limitations

                                                                 Power-up, calibration, normal run, abnormal run, RGB/USB
Demo checklist
                                                                 evidence and shutdown

                                                                 Dated member responsibilities, code commits, hardware
Contribution record
                                                                 changes and experiment ownership


   Dept. of CSE (CY)                              PBCST504 - Microcontrollers                                              Page 10
                             Dept. of CSE (CY)         PBCST504 - Microcontrollers            Page 10

                    Topic: VibeGuard - Semester Implementation and Future Research Roadmap


Dept. of CSE (CY)                        PBCST504 - Microcontrollers                         Page 11
                    Dept. of CSE (CY)         PBCST504 - Microcontrollers         Page 11

                                  Topic: VibeGuard - Semester Implementation and Future Research Roadmap


10. Validation and acceptance programme
10.1 Validation stages
              Stage                               Question                      Minimum evidence                       Stop/fallback

                                     Are the purchased ESP32, sensor,    Device ID, axis response, stable   Replace or redesign the failing
V0 - Component acceptance
                                     motor and supply usable?            rails, motor/guard inspection      component before integration

                                                                         Achieved ODR, error/loss
                                     Can the system collect stable                                          Reduce SPI clock/ODR, shorten
V1 - Acquisition integrity                                               counters, no unexplained
                                     timestamped data?                                                      wiring or move to perfboard
                                                                         saturation

                                     Is the controlled normal state      Multiple sessions and remount      Fix rig/mount before classifier
V2 - Normal repeatability
                                     stable across sessions?             record; feature distributions      tuning

                                     Is the induced state safe and       Repeated labelled abnormal         Redesign the fixture; do not tune
V3 - Abnormal repeatability
                                     distinct?                           sessions and physical metadata     around an unstable fault

                                     Does RMS + persistence work         Frozen threshold, latency and      Simplify features or improve rig
V4 - Minimum classifier
                                     locally?                            development results                labels

                                     Do FFT/bands or Mahalanobis         Same held-out protocol; resource   Drop optional method if it adds
V5 - Comparator evaluation
                                     add useful evidence?                comparison                         no value

                                     Does the frozen system
                                                                         Pre-registered metrics; no         Report failure honestly; retain
V6 - Locked held-out run             generalize to untouched
                                                                         threshold changes                  project as measurement study
                                     sessions/remount?

                                     Can another person operate and      Checklist, rehearsal and source-
V7 - Demo and documentation                                                                                 Freeze features and repair only
                                     explain the project?                backed report


10.2 Proposed Level-1 acceptance targets for teacher approval

  Status of numbers
  The project authority did not freeze quantitative Level-1 accuracy thresholds. The following are proposed pre-
  registration targets and become binding only after teacher/owner approval.


                    Metric                                      Proposed target                                 Why it matters

                                                  At least three days with independently
                                                                                                 Prevents a single-run demonstration from
Independent evidence                              started normal and abnormal sessions; at
                                                                                                 being called reliable
                                                  least one complete day/remount held out

Sensitivity to induced abnormal                   ≥90% on the untouched Level-1 test             Limits missed abnormal states

Specificity for normal                            ≥90% on the untouched Level-1 test             Limits false alarms

                                                  No more than one alert during a 10-minute
Stable-normal false alerts                                                                       Makes the live demonstration credible
                                                  locked stable-normal run

Decision latency                                  ≤2 seconds for the minimum classifier          Maintains interpretable local alerting

                                                  100% for Level-1 unless an explicit            Avoids hiding errors through abstention in
Decision coverage
                                                  sensor/invalid fault is logged                 the semester binary task

                                                  Zero lost analysis blocks during the locked
                                                                                                 Ensures apparent accuracy is not built on
Acquisition integrity                             run; saturation and alias/bandwidth limits
                                                                                                 missing data
                                                  reported

                                                  A second operator can execute the demo         Shows project readiness rather than owner-
Reproducibility
                                                  from the checklist                             only operation


10.3 Required performance reporting
 • Confusion matrix and class counts, not only a single accuracy percentage.
 • Sensitivity, specificity, precision where meaningful, false-alert count and missed-detection count.
 • Decision latency and persistence delay.

    Dept. of CSE (CY)                                    PBCST504 - Microcontrollers                                              Page 12
                                  Dept. of CSE (CY)            PBCST504 - Microcontrollers            Page 12

                                  Topic: VibeGuard - Semester Implementation and Future Research Roadmap


• ESP32 RAM/flash use, feature/FFT timing and dropped-block counters.
• Normal and abnormal plots from untouched sessions with the same axis/range.
• Failure cases, remount sensitivity and known limits of the ADXL345 frequency band.


11. Twelve-week semester roadmap
         Week                 Primary work                Owner(s)               Measurable output              Exit criterion                Fallback


                                                                                                                                      Use available verified
                                                                               Approved scope; final       No purchase until
                         Approval, scope freeze,   Nihad + team; Amith                                                                ESP32/motor variants
1                                                                              order list; lab/tool        change and rig-safety
                         safety and procurement    hardware audit                                                                     without changing
                                                                               inventory; risk register    direction are approved
                                                                                                                                      architecture

                         ESP32/ADXL345             Sreehari firmware;          Device ID/axis test;                                   Return/replace failed
                                                                                                           Sensor and motor pass
2                        acceptance and motor      Amith hardware;             motor/supply inspection;                               module before
                                                                                                           acceptance
                         inspection                Sreeprada checklist         provisional mount plan                                 integration

                                                                               Timestamped X/Y/Z           Continuous stable          Reduce ODR/SPI clock;
                         Stable SPI acquisition
3                                                  Sreehari + Nihad            stream; achieved ODR;       acquisition and USB        shorten wires; move to
                         vertical slice
                                                                               loss/saturation counters    logging                    perfboard

                                                                               Final mount ID; normal      Feature distributions
                         Rigid mount and           Amith rig; Sreeprada                                                               Rebuild mount/base
4                                                                              sessions on separate        repeatable enough to
                         normal-state sessions     records; Nihad review                                                              before classifier tuning
                                                                               starts                      define baseline

                                                                               Guarded eccentric           Safe, reproducible state   Change
                         Safe induced-abnormal     Amith + faculty safety;
5                                                                              fixture; repeated           separation visible in      mass/radius/speed
                         fixture and sessions      team operators
                                                                               abnormal labels             raw/features               within safe limits

                                                                                                           End-to-end                 Simplify to one
                         RMS + persistence and     Sreehari firmware;          Working local minimum
6                                                                                                          Normal/Abnormal            magnitude feature;
                         RGB/USB state             Nihad integration           classifier and logs
                                                                                                           demonstration              improve calibration

                                                                               FFT timing,                 Baseline remains stable;   Drop comparator if
                         Triggered FFT/bands       Sreehari data; Nihad
7                                                                              spectra/bands; optional     comparator does not        timing/data burden is
                         and comparator            review
                                                                               Mahalanobis prototype       break acquisition          excessive

                         Independent sessions      Nihad protocol;             Locked test plan,           Minimum demonstrable       Use Weeks 9-10 to
8                        and held-out protocol     Sreeprada registry;         thresholds, session split   system complete by end     stabilize baseline; no
                         freeze                    Archa documentation         and demo draft              of week                    future-scope expansion

                                                                               Startup/shutdown,
                                                                                                           Known edge cases           Document limitation if
                         Edge cases and fault                                  shock, loose-mount,
9                                                  Team                                                    produce honest             reliable handling is not
                         handling                                              saturation and sensor-
                                                                                                           state/fault evidence       feasible
                                                                               fault logs

                                                                                                           Approved acceptance
                         Locked Level-1                                        Untouched results,                                     No post-hoc threshold
                                                   Nihad + Sreehari;                                       target met or failure
10                       validation and demo                                   metrics, resource profile                              change; repeat only after
                                                   independent operator                                    documented without
                         freeze                                                and frozen release                                     formal redesign
                                                                                                           patching

                                                                               Final dossier updates,
                                                                                                           Teacher-ready package;     Cut nonessential
                         Documentation and         Archa lead; all technical   wiring/BOM, results,
11                                                                                                         second operator can run    content; retain core
                         rehearsal                 review                      demo script and
                                                                                                           demo                       evidence
                                                                               limitations

                                                                               Stable submitted                                       Repair from spares;
                         Contingency repair and                                                            No new feature;
12                                                 Full team                   prototype and archived                                 present validated subset
                         final delivery                                                                    deliver/rehearse
                                                                               evidence                                               honestly


     Schedule rule
     The minimum demonstrable system should work by the end of Week 8. Weeks 9-12 are for validation, recovery,
     documentation and presentation. PIRG is prohibited from becoming a late semester feature.


     Dept. of CSE (CY)                                      PBCST504 - Microcontrollers                                                          Page 13
                                   Dept. of CSE (CY)              PBCST504 - Microcontrollers                    Page 13

                             Topic: VibeGuard - Semester Implementation and Future Research Roadmap


12. Team roles, actual members and accountability
  Role status
  The following name-to-role map is a proposed implementation assignment based on the established five-
  member team and earlier presentation responsibilities. The team and teacher should sign or amend it before
  Week 1 closes.


           Member                        Proposed primary role           Specific VibeGuard ownership           Review/backup obligation

                                                                         Architecture control, schedule,
                                                                         interfaces, safety coordination,    Backs up firmware and
                                    Technical integration lead /
Nihad P C - JEC24CC044                                                   validation protocol, final          hardware; approves
                                    project manager
                                                                         integration and evidence            configuration freezes
                                                                         integrity

                                                                         ADXL345 driver, SPI acquisition,
                                                                         feature pipeline,
                                    Firmware, signal-processing and                                          Nihad reviews releases;
Sreehari K - JEC24CC055                                                  RMS/persistence,
                                    data lead                                                                Sreeprada executes scripted tests
                                                                         FFT/comparators, USB schema
                                                                         and analysis scripts

                                                                         Procurement audit,
                                                                                                             Nihad reviews interfaces/safety;
                                    Hardware, power and physical-        motor/base/guard, rigid sensor
Amith Krishna Das - JEC24CC016                                                                               Sreehari checks signal-integrity
                                    rig lead                             mount, supply wiring, perfboard
                                                                                                             needs
                                                                         and safety inspections

                                                                         Inventory, configuration labels,
                                                                                                             Works from signed procedures;
                                    Learner, test and inventory          scripted sessions, mount photos,
Sreeprada K S - JEC24CC056                                                                                   learns USB logging and basic
                                    assistant                            operator checklists, run registry
                                                                                                             firmware operation
                                                                         and repeated tests

                                                                         Weekly review notes, teacher-
                                    Documentation, teacher               facing explanations, source
                                                                                                             Technical statements reviewed
Archa Pramod - JEC24CC022           communication and                    register, live-demo script,
                                                                                                             by Nihad, Sreehari and Amith
                                    demonstration lead                   presentation coordination and
                                                                         lead communication


12.1 Responsibility rules
 • Every critical subsystem has one primary owner, one technical reviewer and one written checklist.
 • No one may change hardware wiring, firmware thresholds or test labels without a dated configuration update.
 • The learner/test role is substantive: repeated independent runs, inventory control and evidence integrity are
   project-critical.
 • The documentation lead does not publish future-research details without technical and IPR review.
 • Nihad acts as final integration failsafe, but work must remain distributed so the project does not depend on one
   member.


13. Procurement, acceptance and configuration control
13.1 Procurement sequence
1. Obtain teacher approval and freeze the semester architecture.
2. Order the ESP32, one ADXL345 module, motor/fan and power adapter first.
3. Accept or reject the sensor and motor before ordering duplicate or final fabrication items.
4. Fabricate the base, guard and rigid bracket after physical dimensions are known.
5. Buy a spare sensor or motor only when acceptance/delivery risk justifies it within the conservative envelope.

13.2 Component acceptance record
               Component                                     Acceptance checks                                     Reject if

                                                 Boots reliably, USB serial works, board         Unknown board mapping, repeated
ESP32
                                                 identity/pinout recorded, regulator stable      disconnects, overheating or unstable supply
   Dept. of CSE (CY)                                    PBCST504 - Microcontrollers                                               Page 14
                                 Dept. of CSE (CY)            PBCST504 - Microcontrollers             Page 14

                                 Topic: VibeGuard - Semester Implementation and Future Research Roadmap


13.3 Configuration ID format
Recommended format: VG-[rig]-[mount]-[sensor]-[firmware]-[protocol]-[session]. Example: VG-R01-M02-S01-FW0.6-
P03-D2N04. The exact format may change, but every data file and photograph must resolve to one reproducible
physical and software configuration.


14. Risk register and mitigation
            Risk                 Likelihood / impact          Early indicator                Mitigation               Decision consequence

                                                                                     Reputable source, formal
                                                        Wrong device ID, unstable
Counterfeit or poor-quality                                                          acceptance test, preserve      Do not tune algorithms
                              Medium / High             noise, limited ODR or
ADXL345 module                                                                       seller/board photos, replace   around a failed sensor
                                                        clipping
                                                                                     before integration

                                                                                     Retained mass, shaft guard,
Unsafe or unstable                                      Fastener movement, guard     heavy base,                    Stop powered testing until
                              Medium / Critical
abnormality fixture                                     vibration or base walking    low-speed/current-limited      redesigned
                                                                                     bring-up and faculty review

                                                                                     Rigid documented bracket,
                                                        Feature shift after minor                                   Report mount dependence;
Mount-dependent result        High / High                                            mount ID, remount trials
                                                        handling                                                    do not claim generality
                                                                                     and photos

                                                                                     Short wiring, conservative
                                                        Timing overrun, sample                                      No locked result accepted
SPI/acquisition loss          Medium / High                                          clock/ODR, interrupt/FIFO
                                                        gaps, corrupted frames                                      with silent loss
                                                                                     use, perfboard and counters

                                                                                     Adjust range; verify signal
Sensor saturation or                                    Clipped samples or missing   band; limit claims; consider   Do not claim phenomena
                              Medium / High
bandwidth mismatch                                      discriminating frequency     documented future sensor       outside measured band
                                                                                     upgrade

                                                                                     Stabilize base, speed/load
Unrepeatable                                            Overlapping sessions or                                     Redesign rig, not the
                              Medium / High                                          and eccentric fixture before
normal/abnormal labels                                  changing motor behavior                                     classifier
                                                                                     thresholding

                                                                                     Split complete
Data leakage / inflated                                 Random-window split gives    sessions/days/remounts;
                              Medium / High                                                                         Reject leaked metric
accuracy                                                much higher result           freeze thresholds before
                                                                                     hold-out

                                                                                     RMS+persistence first;
                                                        Core demo delayed by                                        Drop comparator, preserve
Late algorithm expansion      High / Medium                                          optional methods after
                                                        ML/feature work                                             minimum system
                                                                                     Week 6

                                                                                     Primary/reviewer/checklist
                                                        One person owns code, rig                                   Reassign before critical
Team bottleneck               Medium / High                                          structure; weekly cross-
                                                        and report knowledge                                        week
                                                                                     training

                                                        PIRG features enter          Separate folders, budgets
Patent expectation distorts                                                                                         Remove future mechanism
                              Medium / High             BOM/schedule or public       and claims; teacher-safe
semester                                                                                                            from semester build
                                                        claims                       wording; IPR review


15. Required semester deliverables and live demonstration
15.1 Deliverables
 • Working guarded VibeGuard Level-1 prototype.
 • Final BOM, source record, wiring/pin map and power-domain diagram.
 • Motor-rig configuration and safety checklist.
 • Versioned ESP32 firmware and reproducible analysis scripts.
 • Raw-session register, configuration metadata and held-out validation results.
 • Final report containing results, limitations, negative evidence and resource use.
 • Teacher-ready presentation and live-demo procedure.
 • Archived OpenBraille zeroth-review package kept separate from VibeGuard implementation evidence.


    Dept. of CSE (CY)                                  PBCST504 - Microcontrollers                                                 Page 15
                                  Dept. of CSE (CY)         PBCST504 - Microcontrollers             Page 15

                              Topic: VibeGuard - Semester Implementation and Future Research Roadmap


15.2 Recommended five-minute live demonstration
1. Show the guarded rig, rigid sensor mount, ESP32 and separate power domains while power is off.
2. Connect USB, show the configuration banner and complete a short calibration/self-check.
3. Run the normal state: green LED and live USB features/logs.
4. Apply the pre-inspected induced-abnormal configuration: red LED after persistence and visible logged
   feature/spectral change.
5. Return to the approved normal configuration and show recovery according to the frozen state rule.
6. Show one held-out result table, resource measurements and the explicit limitations: controlled rig, Level 1 only, no
   patent claim.

15.3 Demo failure fallback
If the powered abnormality demonstration cannot be run safely in the classroom, use an approved guarded video of
the locked setup plus a live sensor/firmware playback only if the teacher accepts that fallback. Do not improvise an
unguarded rotating mass for presentation impact.


16. Post-semester PIRG research hypothesis


                   Figure 4. PIRG research concept. This is not implemented or validated in the semester system.

16.1 Technical question
Can one target-mounted vibration sensor preserve enough information to distinguish a change caused by the target
machine from a change caused by an independently operating neighbouring source, when the system is
commissioned using controlled paired physical interventions?

16.2 Candidate mechanism in non-claim language
1. During commissioning, change the target state while keeping the interferer at the same labelled condition. Form a
   target-change representation from paired differences.
2. Separately change the interferer while the target is independently confirmed normal. Form an interference-
   change representation.
3. At runtime, compare a new deviation against both representations using one permanent target-mounted sensor.
4. Declare Target-Abnormal only when the event is anomalous and fits the target-change structure materially better
   than the interference-change structure.
5. Return Unknown for ambiguous, unsupported or mount-invalid observations rather than forcing a target-fault
   claim.


    Dept. of CSE (CY)                              PBCST504 - Microcontrollers                                     Page 16
                              Dept. of CSE (CY)         PBCST504 - Microcontrollers          Page 16

                                Topic: VibeGuard - Semester Implementation and Future Research Roadmap


6. Defer quarantined baseline updates until the attribution core has independently passed; do not make every
   familiar feature part of one speculative bundle.

16.3 Why this is only a hypothesis
 • One sensor observes a mixture; the two physical sources may be non-identifiable or nearly collinear.
 • Mounting, speed, load and structural coupling may change the contrast structures.
 • Known subspace comparison, open-set rejection, Mahalanobis models and single-sensor classification create high
   obviousness risk.
 • No current experiment shows that PIRG beats strong conventional baselines.
 • A model simulation cannot replace enablement, field labels or professional patent review.


17. Six-to-twelve-month future research roadmap
            Month                       Stage                            Work                        Pass evidence                      Failure action


                                                             Freeze Level-1 platform;
                                                                                                                                Continue
                                                             preserve raw                    Stable Level-1 data; safety-
                           Semester foundation and                                                                              semester/publication only if a
0-2                                                          data/timing/mount records;      approved target/interferer
                           research design                                                                                      reliable scaffold cannot be
                                                             design two-motor coupled rig    scaffold
                                                                                                                                built
                                                             and temporary ground truth

                                                                                             Untouched day/remount
                                                             Collect target
                                                                                             shows ≥30% relative
                                                             normal/abnormal × interferer
                                                                                             reduction in wrong                 Kill PIRG if target/interference
                                                             off/normal/abnormal across
2-4                        Early paired-intervention gate                                    attribution/false target alerts,   directions are inseparable or
                                                             ≥3 days/remounts; compare
                                                                                             ≤5 percentage-point miss-rate      gain is leakage/abstention
                                                             RMS, FFT/bands, Mahalanobis
                                                                                             worsening and ≥80%
                                                             and conventional classifier
                                                                                             coverage

                                                             Freeze PIRG representation;
                                                                                             Complete mechanism
                                                             remove each asserted                                               Remove non-contributing
                           Mechanism and ablation                                            outperforms strongest
4-6                                                          component; test held-out                                           features; kill patent route if
                           phase                                                             baseline and critical ablations
                                                             interferer level, speed/load                                       result is additive/generic
                                                                                             on locked data
                                                             and mount validity

                                                             Test more than one
                                                             motor/arrangement; obtain
                                                                                             Effect survives another
                                                             independently labelled                                             Retain only as bench
6-9                        Field-like replication                                            arrangement without
                                                             target/interferer states; run                                      publication if transfer fails
                                                                                             permanent reference sensors
                                                             local ESP32 timing/resource
                                                             tests

                                                             Lock architecture, datasets,
                                                                                             Reproducible evidence pack
                                                             negative results, contributor                                      Do not file from an outcome-
9-10                       Confidential evidence freeze                                      and clear claim-to-experiment
                                                             chronology and public/private                                      only idea
                                                                                             map
                                                             disclosure log

                                                             Refresh worldwide
                                                             patent/NPL search;
                                                                                             Named useful scope remains
                           Fresh claim-level search and      institutional invention                                            Trade secret/publication/kill if
10-11                                                                                        after closest art and design-
                           IPR review                        disclosure; counsel-led                                            scope is trivial or blocked
                                                                                             around analysis
                                                             novelty, inventive-step,
                                                             eligibility and FTO screen

                                                             Select narrow supported
                                                             filing, confidential            One reasoned written               Archive and publish only
11-12                      File/no-file management gate
                                                             continuation, publication or    decision; no grant promise         after IPR/FTO review
                                                             termination


17.1 Research baselines and ablations
                               Type                                                                   Required comparison

                                                                              RMS+persistence; FFT/bands; ordinary Mahalanobis; static
Strong conventional baselines
                                                                              spectral subtraction; a competent single-sensor classifier

                                                                              Target contrast removed; interference contrast removed;
PIRG component ablations                                                      Unknown forced into binary; mount-validity gate removed;
                                                                              operating-state conditioning removed

                                                                              Hold out complete day/remount and at least one interference
Evidence split
                                                                              condition; never random-window leakage


       Dept. of CSE (CY)                                    PBCST504 - Microcontrollers                                                          Page 17
                                Dept. of CSE (CY)                PBCST504 - Microcontrollers                  Page 17

                            Topic: VibeGuard - Semester Implementation and Future Research Roadmap


                            Type                                                         Required comparison

                                                                   ESP32 acquisition and inference with no locked-run block loss
Local deployment
                                                                   or hidden saturation

                                                                   Temporary reference sensors or independent controls may label
Physical truth
                                                                   experiments but are not permanent product sensors


17.2 Patent-development kill conditions
 • Target and interference changes occupy essentially the same observable signal direction.
 • PIRG does not beat the strongest conventional comparator on held-out sessions.
 • Performance works only by classifying an impractically large fraction as Unknown.
 • A permanent second/reference sensor is required for operation.
 • The ADXL345 misses the discriminating band and a broader sensor change destroys the connected architecture
   case.
 • Remounting, speed/load or another motor arrangement destroys the result.
 • Fresh prior art shows the claim-defining combination or useful scope becomes trivial/easily avoided.
 • Institutional/professional review does not justify filing cost or disclosure risk.


18. Confidentiality, inventorship and disclosure control
18.1 Public-safe semester material
 • ADXL345 + ESP32 architecture, SPI acquisition, time features, triggered FFT, RMS/persistence, ordinary
   Mahalanobis comparison, RGB and guarded eccentric-mass rig.
 • Level-1 normal-versus-induced-abnormal results, provided limitations and configuration are disclosed.
 • Budget, schedule, team roles and educational objectives.

18.2 Keep private until IPR review
 • Exact PIRG paired-intervention representation, residual/fit calculation and thresholds.
 • Any baseline quarantine, update, rollback or mount-validity mechanism that later survives ablation.
 • Labelled interference/remount datasets, field-like results and claim-to-experiment maps.
 • Unpublished negative/positive ablation results and any combination showing an unexpected technical effect.

18.3 Inventorship/contribution record
Maintain a dated record of who conceived each later mechanism, who designed each experiment, who implemented
code/hardware, and when the result was first reduced to practice. Model-generated wording is not a substitute for
human conception. The institutional IPR cell should determine inventorship and disclosure strategy before any filing.

18.4 Disclosure rule

   Do not rely on an assumed grace period
   Before publishing code, datasets, posters, videos, papers, competition entries or detailed teacher material about
   the future mechanism, obtain institutional IPR review. The public semester MVP and confidential future
   research must remain in separate folders and explanations.


19. Decision gates and escalation rules
             Gate                                When                             Pass                        Fail response

                                                                   VibeGuard Level-1 approved        Continue approved concept or
G0 - Teacher approval           Before procurement
                                                                   with scope/budget                 revise request

                                                                   ESP32, ADXL345, motor and
G1 - Component acceptance       Week 2                                                               Replace before integration
                                                                   supply pass checks


    Dept. of CSE (CY)                               PBCST504 - Microcontrollers                                          Page 18
                             Dept. of CSE (CY)           PBCST504 - Microcontrollers            Page 18

                                  Topic: VibeGuard - Semester Implementation and Future Research Roadmap


                Gate                                  When                               Pass                          Fail response

                                                                           Stable ODR/timestamps; visible    Reduce rate/clock, fix wiring or
G2 - Acquisition integrity           Week 3
                                                                           counters; no silent loss          replace sensor

                                                                           Normal and abnormal states are    Redesign mechanical fixture
G3 - Rig repeatability               Weeks 4-5
                                                                           safe and repeatable               before algorithm work

G4 - Minimum demonstrable                                                  Local RMS+persistence, RGB and    Use Weeks 9-10 for stabilization
                                     End Week 8
system                                                                     USB path works                    only; cut optional features

                                                                                                             Submit as controlled
                                                                           Teacher-approved Level-1
G5 - Locked semester validation      Week 10                                                                 measurement study with
                                                                           metrics reported honestly
                                                                                                             documented limitations if missed

                                                                           Attribution improvement
                                                                                                             Stop patent spending; retain
G6 - PIRG early research             Months 2-4 post-semester              survives untouched
                                                                                                             publication/engineering value
                                                                           session/remount

                                                                           Evidence, useful scope, search
G7 - IPR/file-no-file                Months 10-12                          and professional review support   Trade secret, publication or kill
                                                                           action


20. Open questions and teacher decisions
                 ID                          Question / decision                        Owner                          Required by

                                     Approve VibeGuard as the
                                     semester implementation and
Q1                                                                         Project coordinator               Before procurement
                                     this dossier as the controlling
                                     build plan?

                                     Confirm whether the
                                     implementation window is
Q2                                                                         Project coordinator               Week 1
                                     effectively 8 weeks or the full 12-
                                     week roadmap?

                                     Approve verified ESP32-
Q3                                   WROOM-32 DevKit or authorize          Teacher + Nihad/Sreehari          Before order
                                     ESP32-S3 based on availability?

                                     Approve the proposed
                                     quantitative Level-1 validation
Q4                                                                         Teacher + technical leads         Before Week 8
                                     targets or replace them with
                                     another pre-registered protocol?

                                     Which lab tools and safety
Q5                                   reviewer are available for the        Amith + department                Week 1
                                     motor rig?

                                     Approve the proposed name-to-
Q6                                                                         Full team + teacher               Week 1
                                     role map or require changes?

                                     What project information may
Q7                                   be made public before                 Project owner/IPR cell            Before public disclosure
                                     institutional IPR review?

                                     Does the department have a later
                                     field-like site or industry contact
Q8                                                                         Coordinator/department            Post-semester planning
                                     for independently labelled
                                     target/interferer research?


21. Teacher approval and conditions
                             Decision item                                                          Teacher response

Semester project                                                           Approved / Approved with conditions / Not approved

                                                                           ESP32-WROOM-32 DevKit / ESP32-S3 / Other authorized
Approved board
                                                                           board: __________

     Dept. of CSE (CY)                                   PBCST504 - Microcontrollers                                               Page 19
                                  Dept. of CSE (CY)            PBCST504 - Microcontrollers             Page 19

                               Topic: VibeGuard - Semester Implementation and Future Research Roadmap


Approved budget ceiling                                            ₹ __________

Approved implementation window                                     __________ weeks

                                                                   As proposed / Modified as attached / To be submitted by
Approved Level-1 acceptance protocol
                                                                   __________

Safety/facility conditions

Other conditions/comments

Signature and date


22. Source basis
This dossier was prepared from the controlled Project mC master package. The following files are the main evidence
layers:

                          Evidence layer                                                  Controlled source

                                                                   Engineering Design Review; Project mC Decision Register v1.2;
Project authority
                                                                   approved Phase 3C Portfolio Closure Memo

Comparative evidence                                               Concept Evidence Matrix; Uncertainty and Test Register

VibeGuard technical authority                                      Final VibeGuard Architecture Report, Memory and SOP

                                                                   Two final cross-concept adjudications, treated as context rather
Comparative decision context
                                                                   than votes

                                                                   VibeGuard Pre-Build Future Patent-Case Simulation, treated as
Future-research boundary
                                                                   an unbuilt hypothesis

                                                                   Project mC Teacher Documents Master Evidence, Costing and
Current cost/spec basis
                                                                   Decision Basis, price-checked 03 August 2026

                                                                   Final OpenBraille zeroth-review presentation and approved
Previous academic context
                                                                   change request


22.1 Current official specification and price references
 • Analog Devices, ADXL345 product page and data sheet: https://www.analog.com/en/products/adxl345.html
 • Espressif, ESP32-WROOM-32 data sheet: https://www.espressif.com/sites/default/files/documentation/esp32-
   wroom-32_datasheet_en.pdf
 • Espressif, ESP32-S3 product page and DevKitC-1 guide: https://www.espressif.com/en/products/socs/esp32-s3
 • Indian price snapshots and procurement notes are listed in the Master Evidence, Costing and Decision Basis and
   must be refreshed on purchase day.
  Prepared for academic project implementation. The future research section is a management and experimental roadmap, not a
                    patent opinion, filing recommendation, freedom-to-operate clearance or promise of grant.


    Dept. of CSE (CY)                               PBCST504 - Microcontrollers                                         Page 20
                                Dept. of CSE (CY)        PBCST504 - Microcontrollers          Page 20
