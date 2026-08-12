# VibeGuard Semester Execution Playbook

**Document status:** Operational baseline, revision 1.1  
**Audience:** Technical members first; executable by the full five-person team  
**Current status:** VibeGuard is the final semester project; Phase 3C is closed, Phase 4 is open, and Phase 4A is active. This manual begins at Day Zero and does not reopen concept choice.  
**Research/price basis:** Fresh checks dated 9 August 2026; recheck before purchasing.

**Current project-state control:** `Project_mC_Final_Selection_and_Phase4_Entry_Memo.md` and `Project_mC_Decision_Register_v1.3.md`. Decision Register v1.2 remains an unchanged historical predecessor.

**Revision 1.1 — team-role synchronization:** Sreeprada K S retains Experimental Operations/Test/Inventory ownership and adds a supervised Firmware & Data Learning track with Sreehari K, including progressive beginner coding opportunities. Archa Pramod retains Documentation/Communication/Demonstration ownership and adds lightweight Hardware Familiarization with Amith Krishna Das. Subsystem ownership, architecture and technical execution boundaries are unchanged.

## 1. Execution contract

The frozen semester system is one rigidly mounted ADXL345 three-axis accelerometer, one accepted ESP32-WROOM-32 DevKit or authorized ESP32-S3 DevKit, SPI acquisition, local preprocessing/DC removal, mandatory RMS plus persistence, triggered Hann-windowed FFT with selected bands, an optional ordinary Mahalanobis comparator, common-cathode RGB output, USB logging and a guarded low-voltage 12 V motor/fan rig. No cloud dependency is required.

The team must not add a microphone, a microphone array, permanent second accelerometer, active cancellation, dense source attribution, PIRG, bearing/RUL claims or industrial-performance promises. Ordinary Mahalanobis is not required novelty and is dropped if it threatens the critical path.

No step below says or implies that a purchase, test, measurement, pass or teacher condition already exists. An unchecked box is pending. Numeric settings marked **PROPOSED** or **TO BE FROZEN AFTER PILOT** are not final results.

### Gate rule

A stage exits only when:

1. the listed deliverable exists;
2. the acceptance evidence is linked by ID;
3. the owner and reviewer sign/date the gate;
4. the backup can locate and explain the current files;
5. the observer records what actually happened; and
6. open failures are either closed or explicitly accepted with a dated fallback/limitation decision.

Safety gates and locked-test gates require two-person review. The person performing the work cannot be the sole approver.

## 2. Roles and continuity

| Member | Primary ownership | Review/backup obligation |
|---|---|---|
| **Nihad P C — Technical Integration Lead / Project Manager / Configuration & Evidence Lead** | Integration, architecture/configuration, interfaces, schedule, risk, evidence, gates, coordination and system review | Keeps backups current; never becomes sole safety or locked-validation approver. |
| **Sreehari K — Firmware, DSP & Data Lead / Software Systems Mentor** | ESP32, SPI/ADXL345 acquisition, integrity, RMS/persistence, FFT, optional comparator, USB/data tools, scripts, splits and metrics | Retains firmware/DSP/data ownership; primary mentor/reviewer for Sreeprada's learning work. |
| **Amith Krishna Das — Hardware, Power, Rig & Safety Lead** | Procurement, acceptance, wiring, power, motor/supply, switch/fuse, base, mount, fixture, guard and safety | Retains heavy hardware/safety ownership; provides selected familiarization to Archa. |
| **Sreeprada K S — Experimental Operations, Test & Inventory Coordinator / Firmware & Data Learning Associate & Technical Observer** | Independent experiment/inventory/test/run ownership plus progressive approved firmware/data/coding learning | Paired with Sreehari; no independent controlled firmware/settings/split changes or self-merging. |
| **Archa Pramod — Documentation, Communication & Demonstration Lead / Hardware Familiarization Associate & Technical Observer** | Independent documentation/communication/evidence/media/report/demo ownership plus observational hardware familiarization | Paired with Amith; no hardware design, critical modification or safety approval. |

Secondary technical participation supplements rather than replaces each member's primary role. Sreeprada's Firmware & Data Learning track is intended for progressive hands-on learning, including beginner coding under Sreehari's review. Archa's Hardware Familiarization track is primarily observational and explanatory, intended to make her documentation and demonstration technically accurate. Neither track transfers subsystem ownership away from Sreehari or Amith.

Learning must not interfere with critical-path implementation. The subsystem owner remains responsible for deciding when an activity is safe and appropriate for a Learning/Familiarization Associate. Sreeprada ↔ Sreehari and Archa ↔ Amith are not managerial reporting relationships.

### Development milestones

- **Sreeprada:** can execute one frozen low-risk firmware/data procedure independently and explain the basic code/data flow; may contribute a reviewed isolated beginner coding task if ready. Learning outcome only, not a performance criterion.
- **Archa:** can identify and explain every major physical component, signal path, power separation, mount, abnormal fixture and guard. Familiarization outcome only, not technical ownership.

## 3. Configuration, IDs and storage

Use one complete configuration identity on every run:

`CFG-### = HW-REV-### + MOUNT-### + RIG-### + FW-vX.Y.Z@commit + PARAM-### + SCHEMA-###`

Use the detailed ID rules and templates in the Logbook. Raw data is immutable. A correction is a new dated record; it never replaces history.

### Required folder tree

```text
07_SEMESTER_EXECUTION/
├── 01_Selected_Project/
│   ├── CURRENT/
│   ├── Authority_and_Decisions/
│   └── Orientation_and_Minutes/
├── 02_BOM_and_Procurement/
│   ├── CURRENT/
│   ├── Quotes_and_URL_Captures/
│   ├── Orders_Invoices_Delivery/
│   ├── Component_IDs_and_Acceptance/
│   └── Rejected_or_Returned/
├── 03_Hardware_and_CAD/
│   ├── CURRENT/
│   ├── HW_Revisions/
│   ├── Wiring_and_Pinouts/
│   ├── Mounts/
│   ├── Rig_and_Guard/
│   ├── Safety_Inspections/
│   └── Photos/
├── 04_Firmware/
│   ├── CURRENT/
│   ├── Source/
│   ├── Releases/
│   ├── Toolchain_and_Dependencies/
│   ├── Unit_and_Bench_Tests/
│   └── Host_Capture_and_Analysis/
├── 05_Test_Protocols_and_Data/
│   ├── CURRENT_Protocols/
│   ├── RAW_IMMUTABLE/
│   ├── Processed/
│   ├── Failed_Experiments/
│   ├── Dataset_Manifests/
│   ├── Calibration/
│   ├── Pilot_Results/
│   └── Locked_Validation/
├── 06_Reports_and_Demonstration/
│   ├── CURRENT/
│   ├── Evidence_Index/
│   ├── Plots_and_Tables/
│   ├── Demo_Scripts/
│   ├── Media/
│   ├── Final_Report/
│   └── Handover_Archive/
└── FUTURE_RESEARCH_CONFIDENTIAL/
    ├── Observations/
    ├── Separate_Branches/
    ├── Disclosure_Log/
    └── README_ACCESS_CONTROL.md
```

`CURRENT` contains pointers/copies identified as current, not silently replaced history. Release binaries, source archives, raw data and final manifests receive SHA-256 hashes. Failed experiments remain in place and are linked to `ERR-###` records.

## 4. Day-Zero configuration register

Before programming, create these pending records:

| Record | Initial content | Freeze condition |
|---|---|---|
| `DEC-001` | VibeGuard Level-1 frozen architecture and exclusions | Signed by Nihad; reviewed by all members. |
| `RISK-001` | Motor/eccentric ejection and guard controls | Amith owner, Nihad reviewer, Sreeprada observer. |
| `PROC-001` | BOM and current-source capture | Approved before any order. |
| `TOOL-001` | Arduino IDE, ESP32 core, Git, host OS, serial capture, analysis dependencies | After two-computer smoke test. |
| `PIN-001` | Proposed preferred-board pin map | After exact board SKU acceptance and readback test. |
| `PROTO-001` | Pilot acquisition protocol | Before pilot data. |
| `PROTO-LOCK-001` | Locked validation protocol | Before held-out test access. |
| `CRIT-001` | Quantitative acceptance criteria | Approved/revised before labeled collection. |

## 5. Stage-by-stage execution

### Stage 0 — Project freeze and team onboarding

**Objective:** Make every member capable of explaining the system, boundaries, safety, roles, IDs and basic tool flow before hardware work.

**People:** Nihad leads integration; Sreehari owns firmware/data orientation and mentors Sreeprada; Amith owns safety/hardware orientation and familiarizes Archa; both associates retain independent primary roles.

**Prerequisites/inputs:** Governing package; Orientation Primer; this playbook; Logbook; a shared storage/repository location; two computers if available.

**Knowledge/tools:** Plain-language architecture, Arduino IDE, Git basics, serial capture, folder/ID rules, lab safety presentation.

**Exact actions:**

1. Nihad reads the project claim, frozen architecture and exclusions aloud; each member paraphrases one block and one prohibited claim.
2. Walk through sensor → SPI → DC removal → RMS → persistence → triggered FFT → state/USB.
3. Amith gives the motor-rig briefing and Archa's component/function/layout familiarization walkthrough.
4. Create the folder tree and a repository. Restrict `FUTURE_RESEARCH_CONFIDENTIAL` access; do not expose it in public semester material.
5. Demonstrate ID assignment and an append-only correction. Sreeprada fills a practice run record clearly marked `TRAINING-ONLY`; Archa indexes it.
6. Sreehari opens Sreeprada's progressive learning record and explains Arduino IDE, firmware structure, ADXL345/SPI, serial capture, RMS/persistence, FFT and sensor-to-file flow; training code remains isolated.
7. Install or schedule Arduino IDE, Espressif Arduino core, Git and serial capture. Do not call a version “frozen” until a flash/capture smoke test succeeds on two computers or the documented fallback computer.
8. Assign primary roles, secondary tracks and backups; record that pairings do not transfer ownership.

**Deliverable:** Signed onboarding minutes, `DEC-001`, role/backup table, folder screenshot/listing, training log example and tool-readiness status.

**Acceptance/exit:** Five acknowledgements; every member correctly states one architecture invariant, one claim boundary and one safety stop; storage is accessible to the right members; no critical artifact exists only on one personal device.

**Evidence/logs:** Daily log; weekly minutes; engineering decision; risk register; safety briefing attendance; photo/screenshot index; tool record.

**Failure modes/fallback:** Missing member → recorded make-up session before their lab participation. Shared repository unavailable → use a controlled local repository on two encrypted/managed computers plus daily checksumed backup, then migrate without rewriting history.

**Explicit prohibition:** No component order, motor spin, sensor wiring, threshold tuning, feature addition or selection debate during this stage.

### Stage 1 — Procurement

**Objective:** Approve an exact, budgeted and traceable BOM, then place orders in dependency order after same-day rechecks.

**People:** Amith owns procurement; Nihad reviews; Sreehari reviews MCU/sensor interfaces; Sreeprada coordinates inventory/component IDs/checklists and may observe electronics identity tests; Archa controls source/invoice evidence and receives Amith-led component familiarization.

**Prerequisites/inputs:** Procurement checklist, ₹3,000 preferred target and ₹5,000 ceiling, current Indian supplier pages, delivery postcode, available lab stock list.

**Knowledge/tools:** Seller/MPN comparison, GST/shipping arithmetic, return windows, screenshots/PDF invoice capture, spreadsheet or register.

**Exact actions:**

1. Inventory reusable lab items first. Give each reusable item a component/equipment ID and condition note; never assume it is available.
2. Reopen each preferred and backup URL on order day. Record seller, exact title/MPN, SKU, quantity, unit price including/excluding GST, stock text, delivery estimate, shipping, URL and timestamp.
3. Resolve variants before carting: preferred MCU must be exact Espressif `ESP32-DEVKITC-32E`; the ADXL listing must expose SPI pins; motor must be 12 V, approximately 600 RPM, compact and capable of positive shaft coupling; adapter must be enclosed 12 V DC.
4. Price core items plus wiring/protection/base/guard/fasteners and shipping. If projected total exceeds ₹5,000, stop and seek owner/team approval rather than deleting safety items.
5. Order long-lead/critical items first: MCU and sensor; then motor/supply; then safety/mechanical and passives. Consolidate sellers only if exact parts and return terms remain acceptable.
6. Save cart capture before purchase and invoice/order confirmation after an authorized team member actually orders. Do not mark `PURCHASED` from a product page alone.
7. Track dispatch/delivery and return deadline. Plan one spare ADXL345 only if budget and first-unit acceptance justify it; low-cost LED/resistor/fastener spares are preferred.

**Deliverable:** Approved BOM with current captures, actual order records if/when placed, projected/actual totals separated and delivery tracker.

**Acceptance/exit:** Every purchased line has purpose, exact specification, quantity, price basis, source, backup, acceptance/rejection test and spare decision; projected total ≤₹5,000; safety hardware is not omitted.

**Evidence/logs:** Procurement register, component/inventory register, daily log, decision log, invoices, seller captures, correspondence and cost variance.

**Failure modes/fallback:** Price/stock change → use listed backup only after equivalence review. Exact DevKitC unavailable → Nihad may authorize a documented ESP32-S3 DevKit; new BOM, pinout and firmware target required. Delivery slips → advance documentation/toolchain/simulated unit tests, never invent hardware results.

**Explicit prohibition:** No counterfeit-looking/generic MCU substitution under the exact-board line, no open-frame mains supply, no unsecured eccentric parts and no statement that planning prices are purchases.

### Stage 2 — Incoming component inspection

**Objective:** Assign identities and accept, quarantine or reject every received item before integration.

**People:** Amith owns physical acceptance; Nihad reviews; Sreehari owns electronics identity procedures; Sreeprada records IDs/checklists and may shadow those tests; Archa indexes evidence and observes Amith's component/function explanation.

**Prerequisites/inputs:** Delivered package, invoice/order record, anti-static handling, multimeter, current-limited bench source if available, official board/sensor documentation.

**Exact actions:**

1. Photograph sealed package, shipping label with unnecessary personal details masked in public copies, internal packing and both sides of every component.
2. Assign `COMP-###` before powered testing. Record markings, module/board revision, connectors, pin labels, visible damage, seller/order/batch and quantity.
3. Verify ESP32 silkscreen/module can and USB connector against exact ordered SKU. Check bent headers, solder bridges and damage; do not energize a suspect board.
4. Verify the ADXL breakout exposes VCC, GND, SCLK/SCL, SDA/SDI/MOSI, SDO/MISO and CS; record level-shifter/regulator layout without assuming schematic equivalence.
5. Inspect motor body, cable, shaft diameter/D-flat, gearbox play, lead insulation and free manual rotation with power disconnected.
6. Verify adapter label, enclosure, plug size and stated output. With nothing connected, use a meter to record polarity and no-load voltage; then perform only the checklist's controlled dummy/actual-load test.
7. Inspect switch, fuse/holder, connector, wiring, base, clamp, guard stock and captive fixture parts for ratings and mechanical integrity.
8. Mark `ACCEPTED`, `CONDITIONAL`, `QUARANTINED` or `REJECTED`. A conditional part cannot enter locked hardware until its open acceptance item closes.

**Tools:** Camera, labels, caliper/ruler, multimeter, anti-static surface, current-limited supply where available, acceptance templates.

**Deliverable:** Component IDs, incoming acceptance records, photographs, quarantine/rejection list and replacement action.

**Acceptance/exit:** All critical components trace to an order/batch; no visible damage; MCU and sensor identity reach their later powered acceptance gates; supply polarity/voltage is documented; rejected parts are physically segregated.

**Evidence/logs:** Inventory, incoming acceptance, procurement, photo index, error/failure and corrective-action records.

**Failure modes/fallback:** Marking mismatch or uncertain breakout → quarantine and test as an unknown module using current limiting; do not copy seller pinout blindly. Wrong polarity/voltage → reject adapter. Damaged return-window item → notify seller immediately and preserve packaging/evidence.

**Explicit prohibition:** No motor eccentric, no unguarded spin, no direct motor connection to ESP32/USB and no acceptance by appearance alone.

### Stage 3 — ESP32 bring-up

**Objective:** Establish a reproducible toolchain, flash/USB/serial path and board-power baseline.

**People:** Sreehari owns firmware/toolchain decisions and mentors Sreeprada; Nihad reviews; Amith backs up interfaces; Sreeprada shadows Arduino IDE, reviewed upload, identity and serial capture and may progressively execute approved steps; Archa documents evidence.

**Prerequisites/inputs:** Accepted/conditionally accepted exact ESP32 board, data-capable USB cable, official DevKitC guide, two computers if possible.

**Exact actions:**

1. Record host OS, Arduino IDE, Espressif board package, board target, USB driver, compiler/core and serial capture versions in `TOOL-001`. Current official Arduino-ESP32 documentation identifies core 3.3.11; use the installed version that passes this gate and freeze it—do not silently auto-upgrade.
2. Keep all external wiring removed. Power by Micro-USB only. The official DevKitC guide forbids simultaneous USB and header power sources.
3. Identify serial port; upload a minimal sketch that prints firmware test ID, build timestamp/commit and a monotonic counter at a bounded rate and exercises the RGB only after it is separately wired.
4. Reset and power-cycle at least five times. Capture complete boot/log output, noting manual BOOT intervention if required.
5. Verify computer file capture creates a nonempty timestamped file and does not silently overwrite an earlier file.
6. Repeat flash/reset/capture by the backup or on the fallback computer from the written instructions.
7. Tag `FW-v0.1.0` only after review; archive source, compiled binary if available, tool record and SHA-256 hashes.

**Tools:** Arduino IDE, Espressif board package, Git, terminal/serial capture, SHA-256 utility, multimeter optional.

**Deliverable:** Reproducible `FW-v0.1.0` bring-up release and serial capture evidence.

**Acceptance/exit:** Five consecutive boots produce the expected identity/counter; upload and capture work; backup reproduces one boot/capture; exact tool versions and board target are frozen; no unexplained reset loop or overheating.

**Evidence/logs:** Firmware change/release, component acceptance, daily log, successful milestone or error record, photo/screenshot index.

**Failure modes/fallback:** No port → replace cable/port, inspect driver/device manager and record each attempt. Upload requires BOOT → document exact sequence. Reset/brownout → remove external loads and test another known data cable/computer before considering board replacement.

**Explicit prohibition:** No motor supply connection, no Wi-Fi/cloud feature, no sensor-dependent result and no toolchain upgrade after freeze without a change record and repeat gate.

### Stage 4 — ADXL345 bench bring-up

**Objective:** Prove correct SPI identity, register configuration, plausible axes, timing integrity and bounded stationary behavior before motor mounting.

**People:** Sreehari owns SPI/ADXL345 and mentors Sreeprada; Nihad reviews; Amith backs up setup; Sreeprada learns and may execute approved identity/readback/capture; Archa indexes evidence.

**Prerequisites/inputs:** Stage 3 pass; accepted ADXL module; exact board accepted; short wires/breadboard; proposed `PIN-001`; official ADXL345 data sheet.

**Exact wiring for preferred DevKitC-32E (pending pin-map gate):** 3V3→VCC, GND→GND, GPIO18→SCLK, GPIO23→SDI/MOSI, GPIO19←SDO/MISO, GPIO21→CS, optional GPIO4←INT1. Each RGB channel later uses its own measured/selected resistor. If the exact board differs, stop and create a new map from official documentation.

**Exact actions:**

1. With USB unplugged, continuity-check 3V3-to-GND for an obvious short and verify every wire against pin labels and `PIN-001`; photograph the connection.
2. Power by USB only. Start SPI slowly (for example 400 kHz) and read register `0x00` repeatedly. Accept only stable `0xE5`; record actual bytes for failures.
3. Write and read back `DATA_FORMAT (0x31)`, `BW_RATE (0x2C)`, `POWER_CTL (0x2D)` and relevant FIFO/interrupt registers. Do not rely on library defaults.
4. Initial **PROPOSED** setting: full resolution, ±4 g, normal-power 800 Hz ODR, 256-sample blocks. The official data sheet recommends SPI ≥400 kHz for 800 Hz; after readback, test 2 MHz SPI and use it if stable. 1600/3200 Hz may be evaluated only with SPI ≥2 MHz and a documented need.
5. Read complete six-byte X/Y/Z bursts. At six stationary orientations, check that the gravity axis changes sign/magnitude plausibly and cross axes remain bounded. This is a plausibility test, not calibration proof.
6. Record at least three stationary sessions of a predeclared duration (recommended 60 s each) with timestamps, sequence counters, FIFO/overrun status, min/max/mean/RMS and saturation counts.
7. Introduce only gentle hand rotations/taps while bench-mounted to confirm axes and saturation flags; do not use these labeled data for classifier results.
8. Measure achieved block timing. A block with missing sequence/FIFO/overrun evidence is invalid, not silently interpolated.
9. Disconnect/reconnect and let the backup reproduce device ID, readback and one stationary capture.

**Tools:** Multimeter, short jumpers/breadboard, firmware debugger/serial capture, offline plotting/check script, official data sheet.

**Deliverable:** `HW-REV-001`, frozen `PIN-001`, sensor bench firmware, stationary raw sessions, timing/drop report and accepted component record.

**Acceptance/exit:** Stable `0xE5`; configuration readback matches intended values; six-axis plausibility observed; no saturation while stationary; achieved sample/block rate within a predeclared tolerance (recommended ±1% over a sufficiently long capture); zero unexplained drop/overrun events in the acceptance capture; backup reproduction succeeds. Numeric stationary-noise limits remain **TO BE MEASURED / FROZEN AFTER PILOT**, not invented here.

**Evidence/logs:** Wiring/pinout, firmware release, sensor configuration, experiment/session/run logs, calibration/bench record, raw-data manifest, drop report, photos and any errors.

**Failure modes/fallback:** `0xFF/0x00` ID → power off; check CS, grounds, MISO direction and breakout pin naming. Intermittent ID → shorten wiring/lower SPI then isolate module/cable. Drops → reduce serial verbosity, use FIFO/DATA_READY, buffer outputs or reduce ODR only by decision. Saturation → verify units/wiring before changing range.

**Explicit prohibition:** No final threshold, no random deletion of bad samples, no I²C substitution, no seller-code acceptance without register readback and no statement that configured ODR equals achieved ODR.

### Stage 5 — Mechanical motor rig

**Objective:** Build a stable, guarded, low-voltage and fully identified rig with a rigid sensor mount and safe repeatable abnormal fixture.

**People:** Amith owns heavy rig/hardware/safety work; Nihad and a second technical/safety reviewer review; Sreehari backs interfaces; Archa receives hardware familiarization and documents configuration; Sreeprada participates through experiment coordination, not a hardware apprenticeship.

**Prerequisites/inputs:** Accepted motor/adapter/switch/protection; stable base; motor clamp; sensor bracket; strain relief; captive 3 mm eccentric fixture; transparent/solid guard; eye protection; disconnect; caliper/ruler; current-limited supply where available.

**Exact actions:**

1. Draw and dimension `RIG-001`: base material/mass/dimensions, foot/clamp arrangement, motor position/fasteners, guard envelope, switch/disconnect, power connector and cable paths.
2. Build the motor circuit separately from logic: enclosed 12 V adapter → accessible disconnect/switch → fuse → motor. Confirm polarity. Do not connect to ESP32 power.
3. Clamp/bolt motor and base. Pull-test wiring/strain relief with power removed. Verify shaft rotates without guard contact.
4. Design a rigid accelerometer bracket with defined orientation and fasteners or a documented rigid adhesive method. The sensor must not sit on a solderless breadboard during vibration runs. Record mount dimensions, surface preparation and cure time.
5. Build the abnormal fixture using positive mechanical retention (set-screw/clamp/keyed hub plus captive bolt/nyloc or equivalent). Assign mass and fastener component IDs. Tape, hot glue, binder clips, loose washers and press-fit-only attachments are rejected.
6. Enclose the full rotating envelope. The guard must remain secured during operation and allow an emergency stop without reaching inside.
7. With no eccentric installed, use a current-limited low-voltage/short pulse first, then advance toward rated voltage only if current, sound, base and temperature are acceptable. Record voltage/current and duration; all values are measurements, not vendor assumptions.
8. Perform a guarded low-energy eccentric pilot using the smallest approved mass/radius. Increase only through a dated protocol amendment after inspection. Freeze mass, radius, hub, fastener, guard and voltage as `RIG-###` after review.
9. Photograph all sides before/after changes; mark fastener reference lines if useful; create pre-run and emergency-stop procedures.

**Tools:** Hand tools, torque tool if available, caliper/ruler, multimeter, current-limited supply, eye protection, guard materials, camera, temperature measurement if available.

**Deliverable:** Accepted `RIG-###`, `MOUNT-###`, motor circuit/wiring record, dimensions/photos, safety inspection and stop procedure.

**Acceptance/exit:** Motor/base/mount/guard do not visibly loosen in the predeclared guarded run; disconnect works; no guard contact, base walking, excessive heat, damaged wiring or uncontrolled vibration; eccentric has positive retention; sensor/cable strain relief is stable. Actual current, temperature and repeatability are recorded. Approval requires Amith plus reviewer signature.

**Evidence/logs:** Hardware revision, motor-rig configuration, mount/remount register, safety inspection, power measurements, photos/video, run and incident/corrective-action records.

**Failure modes/fallback:** Base moves → stop and increase restraint/mass, not motor speed. Eccentric cannot be safely retained → use a safer guarded fan/fixture or postpone abnormal data; never improvise. Motor current exceeds source/protection → stop, remeasure and select suitable source/fuse under review. Mount variability → redesign bracket before classifier work.

**Explicit prohibition:** No exposed rotating mass, no adjustment while powered, no loose object as “fault,” no mains-side construction, no destructive imbalance and no unsupervised safety-critical work by observers.

### Stage 6 — Normal-state data acquisition

**Objective:** Collect independent, traceable normal sessions under a locked pilot configuration without tuning on future test sessions.

**People:** Sreehari owns data/firmware; Nihad reviews; Amith owns physical configuration; Sreeprada is supervised experiment operator applying firmware/data knowledge; Archa indexes and accurately documents setup.

**Prerequisites/inputs:** Stages 4–5 pass; `CFG-PILOT-###`; approved pilot protocol; synchronized time basis; adequate storage; raw-file write protection/backup; pre-run safety checklist.

**Exact actions:**

1. Define a session as one setup/start sequence by one operator after an inspection and warm-up. Define runs, duration and rest interval before starting. Initial recommendation: several 60–120 s runs per session; exact count/duration **TO BE FROZEN AFTER A SHORT CAPACITY PILOT**.
2. Record room/date/time, people, motor/supply, `RIG`, `MOUNT`, `HW`, `FW`, `PARAM`, schema, warm-up duration, operator and ground-truth condition.
3. Inspect guard/fasteners/wiring; power ESP32 and verify self-check; start host capture before motor; start motor; wait the frozen warm-up; mark run boundaries with structured events.
4. Do not touch rig, base, mount, guard or cable during a stable run. If disturbed, mark the exact time and run validity; do not trim it invisibly.
5. End capture after motor stop and post-run state; record file size, sample/block counts, drops, saturation and stop reason.
6. Compute SHA-256, copy raw file to `RAW_IMMUTABLE`, set read-only access where supported and create a manifest. Processed derivatives go elsewhere.
7. Repeat on separated sessions/days/operators. Reserve at least one complete day/remount for later held-out testing and hide its labels/content from tuning personnel as practical.

**Tools:** Accepted rig, firmware release, host capture, clock, storage/checksum tool, safety/run templates.

**Deliverable:** Manifested normal pilot/training sessions and a session-level split plan.

**Acceptance/exit:** Each accepted run has complete IDs/ground truth, pre/post checks, valid capture, explicit drop/saturation status and immutable hash; required independent sessions are reached per approved protocol; no held-out session is used for tuning.

**Evidence/logs:** Safety, session/run, dataset manifest, raw hashes, photos, operator checklist, failures and daily log.

**Failure modes/fallback:** Drop/serial backlog → invalidate affected run, fix acquisition, repeat under new firmware/config. Base/mount change → stop, create new IDs and do not merge as same configuration. Schedule shortage → reduce run count only through predeclared protocol change before seeing final results.

**Explicit prohibition:** No random-window split, no hand-labeled “cleaning,” no silent deletion, no threshold tuning on held-out data and no late feature addition.

### Stage 7 — Controlled abnormal condition

**Objective:** Acquire safe, repeatable abnormal sessions with physical ground truth, using the same data discipline as normal sessions.

**People:** Amith owns physical abnormal condition; Sreehari owns data; Nihad reviews; Sreeprada is supervised experiment operator; Archa indexes and documents the familiarized physical setup.

**Prerequisites/inputs:** Normal protocol operating; approved guarded `RIG-NORMAL` and `RIG-ABN`; eccentric mass/radius/retention frozen; safety inspection; pilot config.

**Exact actions:**

1. With all power disconnected and shaft stopped, install the exact identified abnormal fixture. Record mass, radius, orientation, hub/fasteners, guard and photographs.
2. Two people verify retention, guard, base, clearance and disconnect. Mark/record fastener reference positions.
3. Run a short guarded safety confirmation before any data run. Stop at the first abnormal stop condition.
4. Execute the same warm-up, run lengths, host capture, event markers and metadata as normal data unless the predeclared protocol states otherwise.
5. Label by physical configuration (`ABNORMAL_ECCENTRIC_RIG-###`), not by algorithm output. An algorithm may be wrong without changing ground truth.
6. Repeat independent sessions and operators. Inspect after each run for motion/loosening; any change creates a new rig ID and invalidates direct equivalence.
7. Remove/adjust only with power disconnected. Archive raw files and hashes exactly as normal data.

**Deliverable:** Manifested controlled-abnormal sessions tied to exact physical ground truth.

**Acceptance/exit:** Safety and retention remain intact; every accepted run has complete physical labels/IDs and integrity counters; repeat sessions exist under the approved protocol; no uncontrolled/destructive condition occurred.

**Evidence/logs:** Rig/mount, safety, session/run, ground-truth photos, raw manifest, failures/incidents, corrective action and daily log.

**Failure modes/fallback:** Fixture loosens or guard contact occurs → emergency stop, quarantine, incident/repair and new rig ID after reinspection. Difference too small → do not secretly increase risk; document negative pilot, review sensor/mount/ODR and propose a safer configuration. Difference trivially large → preserve data but add a milder safe level only if predeclared; do not cherry-pick.

**Explicit prohibition:** No dangerous fault injection, no running without guard, no touching/adjusting during motion, no changing labels from model output and no claiming the condition represents a real industrial fault.

### Stage 8 — Minimum classifier

**Objective:** Produce the first complete local Calibrating/Normal/Abnormal pipeline using DC removal, RMS and persistence, with versioned RGB/USB behavior.

**People:** Sreehari owns RMS/persistence and mentors Sreeprada; Nihad reviews; Amith backs reproduction; Sreeprada may run approved scripts, simple calculations and isolated beginner training/test work; Archa records presentation/report evidence.

**Prerequisites/inputs:** Valid training/pilot sessions; frozen feature definition draft; RGB component acceptance; schema draft; held-out data isolated.

**Exact actions:**

1. Define input units and raw-count-to-g conversion. Write a small deterministic test vector for parsing, mean removal and RMS; compare embedded output to an offline reference within a predeclared numeric tolerance.
2. For each window, calculate axis means, DC-removed RMS values and chosen scalar baseline score. Record formula, float/fixed type, window length and overlap in `PARAM-###`.
3. Derive initial thresholds only from designated normal training sessions using a documented rule (for example a percentile or median/MAD). Mark initial thresholds `PILOT`, not final.
4. Define persistence exactly: entry rule (`K` of `M` windows or `K` consecutive), clear rule, calibration length, invalid-data behavior and startup behavior. All remain **TO BE FROZEN AFTER PILOT**.
5. Implement state machine. A missing ID, configuration mismatch, saturation beyond limit, sample overrun or invalid calibration must enter Fault/Invalid, never green.
6. Wire/test each common-cathode RGB channel through its selected resistor with a lamp test. Freeze green Normal, blue Calibrating and red Abnormal.
7. Freeze `SCHEMA-###`: schema/version, timestamps, IDs, sequences, state, scores, thresholds, persistence counters, drop/saturation flags, FFT flag and reason.
8. Replay or run pilot sessions, inspecting false triggers, latency and resource use. Preserve all failures. Tune only with training/pilot data and record each parameter change.
9. Have Amith or the designated backup boot, calibrate and run the pipeline from the SOP without Sreehari performing the steps.

**Tools:** Firmware/analysis environment, unit vectors, Git, host capture, RGB/resistors, accepted rig, resource/timing counters.

**Deliverable:** `FW-v0.x` end-to-end baseline, `PARAM-PILOT-###`, `SCHEMA-###`, deterministic unit evidence and operator SOP.

**Acceptance/exit:** Embedded/offline RMS agreement meets declared tolerance; all state transitions/reasons are visible and logged; Fault/Invalid cannot appear green; pilot normal/abnormal conditions produce data and state output without acquisition integrity loss; backup executes procedure. Classification performance remains pilot-only until locked test.

**Evidence/logs:** Firmware change/release, parameter register, schema/wiring record, calibration, session/run logs, decision changes, screenshots/video and errors.

**Failure modes/fallback:** RMS mismatch → fix units/indexing before tuning. Excess false alerts → inspect mount/data integrity, then threshold/persistence using training only. Latency too high → adjust window/overlap/persistence through measured trade-off. Schedule pressure → keep per-axis/vector RMS minimal; do not add models.

**Explicit prohibition:** No test-set tuning, no mandatory Mahalanobis, no hidden smoothing, no final performance claim and no state color remapping.

### Stage 9 — Triggered spectral analysis

**Objective:** Add bounded, testable frequency evidence without displacing the mandatory baseline or corrupting acquisition timing.

**People:** Sreehari owns FFT/bands and mentors Sreeprada; Nihad reviews; Amith backs up; Sreeprada may execute approved scripts and isolated beginner tests without changing controlled settings; Archa records evidence.

**Prerequisites/inputs:** Stage 8 baseline stable; validated raw windows; offline FFT reference; timing/memory instrumentation; held-out data still isolated.

**Exact actions:**

1. Select one documented input signal (axis or vector-derived) after training-data inspection. Record why; do not select it using held-out performance.
2. Remove DC, multiply by an explicitly defined Hann window and compute an `N`-point FFT. Initial `N=256` or `512` is **PROPOSED**.
3. Validate bin frequency, amplitude/power normalization and one-sided spectrum against synthetic tones, DC, zero input and an offline reference. Include tones exactly on and between bins.
4. Measure execution time, stack/heap impact and acquisition drops on the target ESP32. FFT must not block sample capture; use buffered/post-window computation as required.
5. Inspect training/pilot spectra and propose only a small number of selected bands. Record band edges, aggregation (sum/mean/max), units and physical/empirical rationale in `PARAM-###`.
6. Define the trigger: for example baseline score in a warning zone, periodic diagnostic cadence or Abnormal confirmation. Record worst-case trigger rate and behavior when resources are unavailable.
7. Integrate band values and `fft_trigger_reason` into the versioned USB schema. Verify a non-triggered window does not pretend a spectrum was calculated.
8. Freeze FFT settings before locked validation and preserve rejected band/trigger attempts as negative evidence.

**Tools:** Offline numerical reference, embedded FFT implementation selected/frozen in `TOOL-###`, profiler/timers, Git, captured pilot data.

**Deliverable:** Triggered FFT release, unit/reference comparison, measured resource report and versioned selected-band definition.

**Acceptance/exit:** Synthetic/reference results meet predeclared numeric tolerance; trigger reason and bands log correctly; acquisition integrity does not regress in a stress run; FFT is demonstrably supporting/triggered; settings are traceable.

**Evidence/logs:** Firmware release, dependency/tool record, parameter register, experiment/run logs, resource measurements, plots, decisions and failures.

**Failure modes/fallback:** Numeric mismatch → fix window/normalization/bin mapping. Timing overruns → reduce size/trigger cadence or compute offline; baseline remains valid. No useful band separation → record negative result and keep FFT as a diagnostic display or minimal supporting feature without invented claims.

**Explicit prohibition:** No dense source attribution, fault-name diagnosis, always-on FFT that breaks acquisition, held-out band selection or presentation of spectral peaks as proof of physical cause.

### Stage 10 — Optional ordinary Mahalanobis comparator

**Objective:** If and only if schedule and data support it, compare the baseline with an ordinary normal-profile multifeature distance.

**People:** Owner Sreehari; reviewer Nihad; backup Amith; Lab Assistant/Observer Archa; Sreeprada verifies scripted operation.

**Prerequisites/inputs:** Stages 8–9 passed; minimum end-to-end system exists; adequate independent normal training sessions; written go/no-go decision; at least two weeks of validation/recovery time remain.

**Exact actions:**

1. Nihad records `DEC-MAH-###` with schedule margin, reason and immediate removal trigger.
2. Freeze a small feature vector from already defined RMS/bands. Standardize and estimate mean/covariance using normal training sessions only.
3. Check covariance condition/stability and document any regularization. If the matrix is unstable or sample independence is inadequate, stop and record a negative result.
4. Validate embedded/offline scores with deterministic vectors. Select comparator threshold using training/pilot only.
5. Run it alongside, not instead of, RMS+persistence. Use a separate score/field/config ID.
6. Compare confusion matrix, latency, compute/memory and explanation burden after the same locked split—without post-test retuning.

**Deliverable:** Optional comparator release/report or signed no-go/removal record.

**Acceptance/exit:** Comparator is reproducible, numerically stable, separately identified and has no acquisition impact; or it is explicitly removed with baseline unchanged. Semester completion does not depend on it.

**Evidence/logs:** Decision, feature/parameter register, firmware release, dataset split, reference tests, resource results and failures.

**Failure modes/fallback:** Singular/unstable covariance, schedule slip, confusing output or no benefit → remove comparator, preserve evidence and continue baseline.

**Explicit prohibition:** No claim that ordinary Mahalanobis is novel, no new sensor, no mandatory dependency, no threshold choice from final test and no delay to Stage 11 onward.

### Stage 11 — Dataset and validation design

**Objective:** Pre-register a leakage-resistant test that challenges behavior beyond the exact training sessions.

**People:** Owner Sreehari; reviewer Nihad; backup Amith; Lab Assistant/Observer Archa; Sreeprada checks operator feasibility.

**Prerequisites/inputs:** Valid manifests; configuration history; proposed quantitative criteria ready for technical-team/project-lead review; no access to held-out results during design.

**Exact actions:**

1. Create a session-level table: date/day, operator, condition, mount/remount, rig, firmware, parameter set, duration, integrity and intended split.
2. Keep all windows from a session/run in one split. Keep a held-out day and at least one remount event out of training/tuning. Document why each split is independent enough.
3. Predeclare included/excluded runs and exclusion rules. Exclude only for recorded protocol/integrity reasons, never because classification is poor.
4. Define safe tests: stable normal, controlled abnormal, startup/calibration, brief non-destructive transient shock outside the guarded envelope, held-out remount, and loose-mount/sensor-invalidity only through a safe simulated disconnect/configuration test—not a dangerous rotating looseness.
5. Define units of analysis and metric equations: TP, TN, FP, FN; sensitivity `TP/(TP+FN)`; specificity `TN/(TN+FP)`; false alerts per stable-normal duration; missed detections; transition latency; sample/drop/saturation/resource statistics.
6. Freeze how latency begins (physical event marker or run start) and ends (first valid persistent red/Abnormal state). State resolution/uncertainty.
7. Carry the roadmap criteria as **PROPOSED FOR TECHNICAL-TEAM/PROJECT-LEAD REVIEW AND FREEZE** until signed: ≥3 separated session days; ≥1 held-out day/remount; ≥90% sensitivity; ≥90% specificity; ≤1 false alert per 10-minute stable normal; ≤2 s latency; zero unexplained lost blocks in locked run; second-operator reproducibility. Faculty/teacher review applies only if explicitly required by the course, lab or faculty and supported by a communication record.
8. Write `PROTO-LOCK-001`, analysis version, random seed where applicable, dataset IDs and exact result-table shell before test access.

**Tools:** Dataset manifest, analysis scripts, protocol template, source-control review, metric test vectors.

**Deliverable:** Signed frozen split, protocol, criteria and blank results structure.

**Acceptance/exit:** No random-window leakage; held-out IDs are sealed/permission-controlled; all exclusions and metrics predeclared; second operator understands the procedure; owner/reviewer sign before test labels/results are opened.

**Evidence/logs:** Dataset manifest, protocol, criteria decision, weekly minutes, risk and communication logs.

**Failure modes/fallback:** Too few independent sessions → collect more before locking or explicitly narrow claim; never manufacture independence. Remount instability → report it as limitation and test result. Criteria not frozen by the technical team/project lead → run a descriptive protocol but label criteria unresolved, not passed/failed.

**Explicit prohibition:** No random-window split, no result-aware exclusions, no feature/threshold change after freeze and no industrial generalization.

### Stage 12 — Final hardware assembly, regression and configuration freeze

**Objective:** Produce the stable, labeled, reproducibly bootable hardware and freeze the complete controlled configuration before any held-out validation is opened.

**People:** Owner Amith; technical reviewer Sreehari; configuration controller/reviewer Nihad; Lab Assistant/Observer Sreeprada; Archa updates photographs, labels and the freeze manifest. Nihad is not the sole approver: hardware/safety and locked-test readiness require a second technical reviewer.

**Prerequisites/inputs:** Candidate configuration; wiring/mount/rig drawings; perfboard or stable connectors; strain relief; final guard and labels; predeclared regression protocol; Stage 11 protocol and sealed held-out assignments.

**Exact actions:**

1. Photograph and identify the candidate hardware before modification; document every planned physical change.
2. Convert necessary vibration-sensitive breadboard/jumper wiring to stable soldered/perfboard or mechanically stable connectorized wiring. Keep the sensor rigidly mounted and apply final strain relief.
3. Install and inspect the final guard, labels and final mount configuration. Label power, USB, sensor connector, motor disconnect, fuse, board pins and orientation so motor and logic power cannot be confused.
4. Create the as-built pinout and inspect solder joints, polarity, shorts, retention, guard and cable clearance with power off.
5. Run ESP32 boot, sensor identity and configuration readback regression. Repeat a predeclared non-held-out normal/abnormal regression subset and compare feature distributions and states to bounds defined before results.
6. If a material hardware, wiring, mount or rig change requires recalibration, perform it using training/calibration data only and record the reason and new identity. Never inspect held-out labels/results during recalibration.
7. Define final `HW`, `PIN`, `MOUNT`, `RIG`, `FW`, `PARAM` and `SCHEMA`; combine them into final `CFG-LOCK-###`. Record binaries/commits, scripts, protocol and analysis versions in the freeze manifest.
8. Freeze boot/start/stop/shutdown and emergency procedures; have a backup reproduce them. Execute the complete locked protocol as a non-held-out dry run.
9. Seal the final configuration and obtain two-person technical/safety and validation-readiness review before opening held-out validation.

**Deliverable:** Stable final hardware, as-built pinout, final guard/labels/mount, regression and any required calibration evidence, final configuration identity, freeze manifest and successful non-held-out dry run.

**Acceptance/exit:** Stable wiring/mount/guard; no shorts or polarity errors; correct sensor readback; predeclared normal/abnormal regression passes or is transparently resolved under a new revision; final `CFG-LOCK-###` is complete; held-out data remain sealed; backup reproduces boot/run/shutdown. Only after this gate passes may Stage 13 begin.

**Evidence/logs:** Hardware, wiring, pinout, mount and rig revisions; firmware/parameter/schema/configuration links; safety and regression tests; calibration record if required; photographs; freeze manifest; decisions, failures and repairs.

**Failure modes/fallback:** Perfboard or connector work changes behavior → create a new revision, investigate and repeat regression/calibration as required before validation. Connector intermittent → quarantine/repair and repeat regression. Schedule shortage → prioritize stable wiring, strain relief, labels and guard; enclosure aesthetics are optional. The held-out test does not open until stabilization succeeds.

**Explicit prohibition:** No held-out validation before final hardware/configuration freeze; no hidden wiring or mount change; no removal of fuse/guard; no power-source ambiguity; no retained validation claim across an unvalidated material revision.

### Stage 13 — Locked final test

**Objective:** Execute the pre-registered held-out test once on the actual final controlled configuration, with deviations visible.

**People:** If qualified on the frozen procedure, Sreeprada is supervised test operator and cannot tune; Sreehari remains technical/data owner; Nihad controls configuration/review; Amith co-reviews hardware/safety; Archa records chronology/media/evidence without altering results. Nihad is not sole approver.

**Prerequisites/inputs:** Passed Stage 12; final stable hardware; `PROTO-LOCK-001`; `CFG-LOCK-###`; signed two-person safety/readiness review; sealed held-out dataset/session assignments; frozen scripts/result shell; adequate storage and backup plan.

**Exact actions:**

1. Verify the freeze manifest containing firmware commit/binary hash, final hardware/pinout/mount/rig IDs, parameters/thresholds, schema, tool/dependency versions, analysis commit, dataset IDs and protocol hash.
2. Confirm held-out data have not been used for tuning. Each member signs their access declaration.
3. Run the safety and configuration check; execute the protocol exactly. Archa records start/end and deviations; Sreeprada reads checklist items aloud where practical.
4. Copy raw outputs once to immutable storage, calculate hashes and verify counts before analysis.
5. Run the frozen analysis without edits. Generate the confusion matrix, metrics with denominators, false-alert duration, latency definition/results, integrity/resource results and per-session table.
6. Record every unexpected outcome. A script or configuration error pauses the run and invokes the deviation rule; it is not fixed invisibly.
7. If a deviation invalidates the test, preserve the attempt as `TEST-###-INVALID`. A correction creates a new revision and requires appropriate regression and a separately reviewed test using genuinely unseen evidence where a held-out claim is sought.
8. After held-out results are visible, no architecture, hardware, mount, wiring, firmware, threshold or feature change may preserve the same validation claim. Any material change requires a new revision and appropriate new regression and validation evidence.

**Tools:** Final frozen rig/firmware/scripts, checksum utility, read-only storage, camera and signed checklists.

**Deliverable:** Locked-test package for the actual final controlled configuration, with raw hashes, chronology, deviations, exact metrics, failures and signed interpretation.

**Acceptance/exit:** Protocol completed or transparently invalidated; every result traces to raw IDs and the final frozen configuration; no unexplained data loss; claims match evidence; negative outcomes are preserved.

**Evidence/logs:** Formal test, safety, session/run, dataset, final configuration/freeze, deviation/error/corrective action, photos/video and sign-off.

**Failure modes/fallback:** Hardware failure → do not substitute another configuration under the same test ID; preserve the failure, repair under a new revision, repeat regression and use genuinely unseen evidence for any new held-out claim. Criteria missed → report values and limitations; do not tune on test. Data corruption → quarantine, preserve hashes/logs and follow deviation procedure.

**Explicit prohibition:** No post-result tuning, hidden rerun, discarded failure, denominator-free percentage, post-validation material change under the same claim, or claim beyond the controlled rig.

### Stage 14 — Demonstration preparation

**Objective:** Prepare honest 2-minute, 5-minute and fallback demonstrations that show the controlled result and limitations.

**People:** Archa owns documentation/communication/demo and explains hardware, component functions, safety and evidence narrative; Nihad reviews system claims; Sreehari reviews firmware/data explanations and prepares Sreeprada to explain experiment and sensor-to-code/data flow; Amith reviews physical/safety explanation.

**Prerequisites/inputs:** Final hardware/config, locked results, approved plots/photos, exact claims/limitations, prerecorded backup evidence.

**Exact actions:**

1. Write a 2-minute script: problem/boundary (20 s), architecture (20 s), blue calibration (20 s), green normal (20 s), power-off fixture change/safety explanation (20 s), red abnormal plus USB evidence/limitation (20 s). Actual fixture change may be omitted live if time/safety requires separate preconfigured evidence.
2. Write a 5-minute technical script adding SPI/readback, sample integrity, DC removal/RMS/persistence, triggered FFT, session split, confusion matrix/latency and limitations.
3. Write a failure fallback: if rig cannot safely run, do not bypass the guard; show prerecorded, timestamped evidence, final hardware, raw-to-plot trace and explain the current fault honestly.
4. Prepare plots with run IDs, axes, units, firmware/parameter/config IDs and whether pilot or locked. Remove unlabeled decorative charts.
5. Rehearse normal, abnormal, Fault/Invalid and emergency stop. Time at least three rehearsals with two operators.
6. Freeze the claim card: “controlled teaching rig,” measured numbers only, and explicit exclusions. Technical reviewer signs every slide/result.
7. Preserve final demo video and script hashes; distinguish rehearsal from formal evidence.

**Deliverable:** 2-minute script, 5-minute script, fallback script/media, claim card, rehearsal log and operator checklist.

**Acceptance/exit:** Three timed rehearsals; two operators can start/stop; all claims trace to locked results; fallback works without unsafe action; no technical slide lacks reviewer approval.

**Evidence/logs:** Demo scripts, video/photo index, rehearsal runs, weekly minutes, document revisions and review sign-offs.

**Failure modes/fallback:** Live sensor/rig fault → use guarded shutdown and fallback media. Timing overrun → cut optional comparator/extra plots, not safety or limitation. Audience asks industrial diagnosis → state controlled-rig boundary.

**Explicit prohibition:** No guard bypass, no live adjustment, no bearing/RUL/predictive-maintenance certification, no patent claim and no fabricated “live” result.

### Stage 15 — Final report, handover and archive

**Objective:** Deliver a reproducible evidence package containing design, versions, raw/processed lineage, results, failures, limitations and safe operation.

**People:** Owner Archa for assembly; evidence owner/reviewer Nihad; firmware backup Sreehari; hardware backup Amith; Lab Assistant/Observer Sreeprada performs archive checklist.

**Prerequisites/inputs:** All stage gates, final BOM/as-built, frozen versions, manifests, locked results, media, failures/decisions, approved wording.

**Exact actions:**

1. Assemble report sections: narrow problem/claim; frozen architecture; BOM; wiring/pinout; rig/mount/safety; firmware/DSP; protocols/splits; results with denominators; failures; limitations; future work boundary.
2. Link every result to `TEST/RUN/DATASET/CFG/FW/PARAM` IDs. Verify every figure has source file, script version and caption.
3. Include actual purchase totals only from invoices; separate donated/reused items and dated planning prices.
4. Create a manifest of source, release binary, tool/dependencies, hardware revisions, wiring, protocols, raw data, processed outputs, scripts, plots, photos/video, report and logbook. Generate SHA-256 hashes.
5. Run a clean-computer or clean-folder reproduction of one raw run → parsed data → RMS/FFT → result row using the documented environment.
6. Perform handover: Sreehari teaches flashing/capture/analysis; Amith teaches safe inspection/start/stop; Nihad teaches configuration/evidence tracing; Archa teaches document/media archive; Sreeprada executes the operator flow.
7. Copy to at least two controlled storage locations, verify hashes and access. Do not move confidential future-research material into the public archive.
8. Freeze final archive read-only; subsequent corrections are dated addenda/new versions.

**Deliverable:** Final report package, manifest/hashes, handover record, two verified copies and known-issues list.

**Acceptance/exit:** Required artifacts present/readable; a second member reproduces one analysis path and one hardware start/stop; hashes verify; failures/raw data remain; no unsupported claim appears.

**Evidence/logs:** Final archive manifest, document revision, successful milestone, handover/training, source index, disclosure log and unresolved-issues register.

**Failure modes/fallback:** Missing raw/config link → result cannot be a formal claim; mark unresolved and repair provenance. Storage too large → retain immutable raw in approved archive with manifest/path and keep verified backup, never delete failures. Reproduction fails → fix documentation/environment under new revision and rerun.

**Explicit prohibition:** No overwritten raw files, no rewritten history, no deletion of failures, no “patentable” conclusion and no unreviewed technical claim.

### Stage 16 — Post-semester research transition

**Objective:** Preserve Level-1 unchanged while allowing separately governed future research after semester completion.

**People:** Owner Nihad; reviewer full technical team; backup Archa for disclosure/document control; Observer Sreeprada; future work requires a new approved plan.

**Prerequisites/inputs:** Signed final archive and Level-1 baseline; access-controlled future-research directory; disclosure log.

**Exact actions:**

1. Tag/hash the unchanged Level-1 source, binaries, hardware/configuration and dataset manifest.
2. Create a separate branch/repository path for future hypotheses. Never merge experimental PIRG code/hardware into the semester baseline silently.
3. For any potentially important observation, record date/time, people physically involved, problem, configurations, raw/run/photo IDs, expected/actual, first hypothesis, proposed test, outcome, negative results and next action.
4. Do not backdate. Append dated corrections rather than rewriting earlier notes. Record contributors and public/private disclosures.
5. Begin PIRG-related work only after a new hypothesis, additional hardware list, safety review, protocol, independence/data plan and team approval exist. A reference/second sensor, if used, belongs only to that research configuration.
6. If PIRG fails, preserve it. Investigate other technical problems only through new observations/protocols; failure does not establish or eliminate patentability.

**Deliverable:** Frozen semester baseline and separately governed future-research starting point—or a decision to do no future work.

**Acceptance/exit:** Public semester material contains Level-1 only; future material has separate identity/access; evidence chronology is intact; no patent claim drafted here.

**Evidence/logs:** Future research observation, disclosure, engineering decision, contributor chronology, branch/release hashes and negative results.

**Failure modes/fallback:** Access/configuration mixing → stop research, restore from verified Level-1 archive and log incident. No new protocol/hardware → no PIRG experiment begins.

**Explicit prohibition:** No silent PIRG addition, no claim drafting, no patentability assertion, no backdating and no alteration of Level-1 evidence.

## 6. Common executable procedures

### 6.1 Pre-run safety and configuration sequence

1. Two people confirm motor power disconnected and shaft stopped.
2. Match physical labels to `CFG-###`: motor, base, guard, eccentric/normal fixture, mount, sensor, MCU and wiring.
3. Inspect base restraint, motor clamp, guard, eccentric retention, sensor mount, strain relief, switch/fuse and cables; photograph any changed reference mark.
4. Remove tools/loose objects; wear eye protection; clear hair/clothing/lanyards.
5. Verify USB powers logic only and 12 V adapter powers motor only.
6. Start host capture to a new run filename; verify disk space and schema header.
7. Power ESP32; require correct firmware/configuration banner, `0xE5` sensor ID and valid register readback. Fault/Invalid must not show green.
8. Start motor using reachable switch. Stop immediately for heat, harsh/new noise, movement, looseness, guard contact, smell/smoke or damaged wiring.
9. Follow warm-up/run markers; do not touch rig.
10. Stop motor, wait for shaft to stop, then stop capture. Record counts/integrity/stop reason, hash raw file and perform post-run inspection.

### 6.2 Deviation procedure

If a planned step, configuration or timing differs:

1. pause if safe;
2. assign `DEV-###` or `ERR-###` and record exact time;
3. preserve current raw/log/media;
4. state expected versus actual and effect on validity;
5. owner proposes disposition: valid with limitation, invalid/repeat, or new exploratory run;
6. reviewer signs before repeat;
7. repeat under a new run/test ID; and
8. never edit the original record to make it appear compliant.

### 6.3 Configuration-change rule

Any change to sensor/module, pin, wire path, mount, base, motor, eccentric, guard, power, ODR/range/SPI rate, window, feature, threshold, persistence, FFT, schema, firmware or analysis script creates a dated change record. The reviewer decides which IDs increment and which gates/regressions repeat. If uncertain, assume the change is material and assign a new configuration.

## 7. Full 12-week semester plan

Every week ends with a signed review. “Quantitative exit” is a gate target, not a claim of achievement.

### Week 1 — Freeze, onboarding and order readiness

- **Objective/sequence:** Complete Stage 0 → inventory lab stock → recheck BOM URLs → approve projected cost → place authorized critical orders.
- **Owner/reviewer/backup/observer:** Nihad / Sreehari / Amith / Archa, with Sreeprada inventory observer; Amith owns procurement subtask.
- **Inputs:** Governing package, four execution documents, computers, budget, delivery postcode, supplier pages.
- **Expected output:** Signed architecture/roles, folder tree, tool status, approved BOM and order tracker if orders are actually placed.
- **Quantitative exit:** 5/5 orientation acknowledgements; 100% BOM lines have source/backup/test; projected total ≤₹5,000; zero unassigned critical task.
- **Documentation:** `DEC-001`, `RISK-001`, minutes, inventory/procurement, source captures.
- **Risks/fallback:** Missing stock/member; use documented backup/make-up session and work on tool readiness.
- **Prohibited:** Selection debate, unapproved substitute, sensor/motor test, removed safety item, PIRG.

### Week 2 — Receiving and ESP32 readiness

- **Objective/sequence:** Receive/photograph/ID/quarantine → accept obvious mechanical/electrical basics → Stage 3 toolchain/USB/capture.
- **Owner/reviewer/backup/observer:** Amith then Sreehari / Nihad / each other / Sreeprada; Archa indexes.
- **Inputs:** Delivered items, invoices, camera, labels, multimeter, USB data cable, Arduino/Git.
- **Expected output:** Component/acceptance records and `FW-v0.1.0` reproducible bring-up.
- **Quantitative exit:** 100% received items assigned status; five ESP32 boot/counter captures; one backup reproduction.
- **Documentation:** Incoming acceptance, photos, toolchain, firmware release, errors/returns.
- **Risks/fallback:** Late/damaged board; return promptly, use tool/unit-test work and backup seller.
- **Prohibited:** Appearance-only acceptance, simultaneous USB/header power, motor from USB/ESP32, invented purchase/pass.

### Week 3 — ADXL345 SPI bench gate

- **Objective/sequence:** Verify exact board/pin map → wire powered-off → `0xE5` → register readback → orientation/stationary/timing/drop tests.
- **Owner/reviewer/backup/observer:** Sreehari / Nihad / Amith / Sreeprada; Archa indexes plots.
- **Inputs:** Accepted MCU/sensor, short wiring, data sheet, capture/analysis.
- **Expected output:** `PIN-001`, `HW-REV-001`, raw stationary sessions and acquisition-integrity report.
- **Quantitative exit:** Stable `0xE5`; intended readbacks; six orientation plausibility positions; achieved rate within proposed ±1%; zero unexplained drops in acceptance capture.
- **Documentation:** Wiring, firmware, runs, raw manifest, timing report, photos/errors.
- **Risks/fallback:** Intermittent SPI/drops; shorten wires, lower speed for diagnosis, FIFO/buffering, replace quarantined module.
- **Prohibited:** I²C substitution, final threshold, deletion/interpolation of bad data, ODR claim without timing.

### Week 4 — Guarded rig and rigid mount

- **Objective/sequence:** Dimension base/motor circuit → mount/strain relief → captive eccentric → guard → no-eccentric pilot → low-energy guarded abnormal pilot → safety gate.
- **Owner/reviewer/backup/observer:** Amith / Nihad / Sreehari / Sreeprada; Archa photographs.
- **Inputs:** Accepted motor/supply/protection, base/clamp/guard/hub, tools and PPE.
- **Expected output:** Approved `RIG-###`, `MOUNT-###`, motor wiring, stop procedure.
- **Quantitative exit:** 100% rotating envelope guarded; disconnect works; predeclared pilot completes with zero loosening/contact/base movement/stop-condition event.
- **Documentation:** Dimensions, hardware/mount/rig revisions, safety/run logs, measurements/media.
- **Risks/fallback:** Unsafe retention or base motion; stop, redesign or use safer guarded fan fixture.
- **Prohibited:** Loose/glued/taped mass, live adjustment, open mains, destructive imbalance, unsupervised observer work.

### Week 5 — Normal sessions

- **Objective/sequence:** Freeze pilot config/protocol → run capacity check → acquire separated normal sessions → hash/manifest → protect held-out allocation.
- **Owner/reviewer/backup/observer:** Sreehari / Nihad / Amith / Sreeprada operator; Archa indexes.
- **Inputs:** Passed rig/acquisition, storage, run/safety checklists.
- **Expected output:** Valid immutable normal sessions and split plan.
- **Quantitative exit:** Protocol-approved number/duration; each accepted run 100% metadata/IDs/hash; zero unexplained integrity event; at least one future day/remount reserved.
- **Documentation:** Sessions/runs, safety, raw manifest, operator/photos, failures.
- **Risks/fallback:** Drops/mount change; invalidate visibly, fix under new version/ID and repeat.
- **Prohibited:** Random-window split, hidden trimming, held-out tuning, late features.

### Week 6 — Controlled abnormal sessions

- **Objective/sequence:** Power-off fixture installation → two-person retention/guard check → short safety confirmation → repeated abnormal sessions → post-run inspection/hash.
- **Owner/reviewer/backup/observer:** Amith+Sreehari / Nihad / reciprocal / Sreeprada; Archa indexes.
- **Inputs:** Approved abnormal `RIG`, physical ground-truth record, same acquisition protocol.
- **Expected output:** Valid immutable controlled-abnormal sessions with exact labels.
- **Quantitative exit:** Protocol-approved repeated sessions; 100% physical labels/IDs; zero uncontrolled fixture change/guard contact.
- **Documentation:** Rig/safety/session/run/manifests/photos/incidents.
- **Risks/fallback:** Too little separation or loosening; preserve negative result, review safer configuration or redesign—never add risk secretly.
- **Prohibited:** Algorithm-derived ground truth, dangerous injection, live adjustment, industrial fault-name claim.

### Week 7 — RMS/persistence end-to-end baseline

- **Objective/sequence:** Unit vectors → DC removal/RMS → training-only threshold → persistence/state → RGB/schema → pilot replay/live run → backup operation.
- **Owner/reviewer/backup/observer:** Sreehari / Nihad / Amith / Sreeprada; Archa checks claim wording.
- **Inputs:** Training/pilot data, RGB/resistors, schema draft, held-out seal.
- **Expected output:** Complete baseline release and operator procedure.
- **Quantitative exit:** Embedded/offline RMS within declared tolerance; all five states/reasons exercised; zero regression in acquisition; backup completes one scripted run.
- **Documentation:** Firmware/parameter/schema/calibration/runs/unit evidence/decisions.
- **Risks/fallback:** False alerts or latency; inspect integrity/mount then tune training-only; minimize features.
- **Prohibited:** Test tuning, mandatory Mahalanobis, hidden smoothing, final claim.

### Week 8 — Triggered FFT and minimum system milestone

- **Objective/sequence:** Hann/FFT reference tests → resource measurement → training-only bands/trigger → integrate schema → freeze minimum system.
- **Owner/reviewer/backup/observer:** Sreehari / Nihad / Amith / Archa; Sreeprada operates.
- **Inputs:** Baseline, synthetic/offline vectors, timing/memory counters.
- **Expected output:** Triggered FFT release and `MILESTONE-MIN-END2END` evidence.
- **Quantitative exit:** Reference tolerance met; no unexplained acquisition drop in stress test; trigger/reason logs; guarded normal/abnormal demo works under script.
- **Documentation:** Firmware/parameters/resource tests/plots/milestone/failures.
- **Risks/fallback:** FFT cost/no useful bands; reduce/compute offline and retain baseline.
- **Prohibited:** Always-on disruptive FFT, dense attribution, fault diagnosis, new features after milestone.

### Week 9 — Challenge testing and optional comparator decision

- **Objective/sequence:** Remount/startup/transient/invalid-sensor tests → finalize split/metrics → only then optional Mahalanobis go/no-go.
- **Owner/reviewer/backup/observer:** Sreehari / Nihad / Amith / Sreeprada; Archa records decision.
- **Inputs:** Minimum system, manifests, uncertainties/test register.
- **Expected output:** Challenge-test evidence, validation design, comparator decision.
- **Quantitative exit:** At least one held-out remount protocol rehearsal; all invalid conditions produce non-green Fault/Invalid; split has zero window leakage.
- **Documentation:** Tests, mounts, failures, split, decision/risk updates.
- **Risks/fallback:** Mount sensitivity or schedule; report limitation, drop comparator.
- **Prohibited:** Permanent second sensor, unsafe loose-mount rotating test, new classifier dependency, test access.

### Week 10 — Final stable hardware, regression and configuration freeze

- **Objective/sequence:** Complete final stable wiring/perfboard or connectorization, strain relief, guard, labels and mount → create as-built pinout → boot/readback and normal/abnormal regression → recalibrate on training data if a material change requires it → technical-team/project-lead criteria review → freeze HW/PIN/MOUNT/RIG/FW/PARAM/SCHEMA/analysis/test IDs → create final CFG → execute dry run on non-held-out data.
- **Owner/reviewer/backup/observer:** Nihad / full technical review / Sreehari+Amith / Archa; Sreeprada dry-run operator.
- **Inputs:** Validation protocol, final candidates, blank result tables.
- **Expected output:** Stable final hardware, as-built pinout, regression/calibration evidence where required, `CFG-LOCK-###`, `PROTO-LOCK-001`, freeze manifest and successful non-held-out rehearsal.
- **Quantitative exit:** 100% freeze-manifest fields/hashes; two-person sign-off; dry run completes without unhandled deviation; held-out remains sealed.
- **Documentation:** Freeze, protocol, criteria, rehearsal, access declarations.
- **Risks/fallback:** Hardware/regression/dry-run fault; repair under a new revision, repeat required regression/calibration and refreeze before opening held-out validation, reducing optional scope.
- **Prohibited:** Held-out inspection, post-freeze change without new version, feature addition.

### Week 11 — Locked held-out validation

- **Objective/sequence:** Verify the final frozen configuration from Week 10 → execute locked held-out test → preserve/verify hashes → frozen analysis → signed results/deviations. The locked test uses the actual final controlled hardware; no post-test hardware stabilization is permitted under the same validation claim.
- **Owner/reviewer/backup/observer:** Sreeprada supervised operator + Sreehari technical / Nihad / Amith / Archa chronology.
- **Inputs:** Locked configuration/test, safety approval, sealed data, storage.
- **Expected output:** Traceable locked result package for the final frozen hardware/configuration.
- **Quantitative exit:** Protocol completion or explicit invalidation; every metric denominator and run ID present; zero unexplained data loss; no post-result tuning.
- **Documentation:** Formal test, raw/manifest, deviations, metrics, hardware/safety/media.
- **Risks/fallback:** Failure/criteria miss; report honestly, use new unseen data only for any true retest.
- **Prohibited:** Hidden rerun, result-aware exclusion, threshold change, same-data rebranding.

### Week 12 — Demonstration, report and archive

- **Objective/sequence:** Rehearse 2/5-minute/fallback → finalize report/evidence links → clean reproduction → handover → two-copy hash verification.
- **Owner/reviewer/backup/observer:** Archa / Nihad / Sreehari+Amith / Sreeprada.
- **Inputs:** Final hardware/results, scripts, archive tools.
- **Expected output:** Honest demo, final report, manifest, handover and verified archive.
- **Quantitative exit:** Three timed rehearsals; two operators; one clean raw-to-result reproduction; 100% manifest hashes verify at two locations.
- **Documentation:** Demo/rehearsal, report revision, archive/handover, disclosures/unresolved issues.
- **Risks/fallback:** Live failure/missing link; use prerecorded evidence, narrow claim, fix provenance before inclusion.
- **Prohibited:** New features, unsafe demo workaround, unsupported claim, deletion/rewriting, public future-research detail.

## 8. Compressed 8-week critical-path plan

### Week 1 — Freeze, order and toolchain

- **Objective/sequence:** Stage 0 → lab inventory/BOM recheck → critical orders → tool install/simulated unit scaffolding.
- **Owner/reviewer/backup/observer:** Nihad+Amith / Sreehari / reciprocal / Archa and Sreeprada.
- **Inputs:** Governing package, budget, computers.
- **Expected output:** Signed roles/folders, approved BOM/order tracker and tool status.
- **Quantitative exit:** 5/5 onboarding; all BOM fields complete; ≤₹5,000 projected; no unassigned gate.
- **Documentation:** Decisions, minutes, procurement and tool records.
- **Risks/fallback:** Late parts → advance firmware test vectors and controlled documentation.
- **Prohibited:** Selection, optional algorithms, unsafe purchase, hardware claims.

### Week 2 — Receive, ESP32 and ADXL bench

- **Objective/sequence:** Inspect/ID → ESP32 five-boot/capture → powered-off ADXL wiring → `0xE5`/readback/orientation/timing.
- **Owner/reviewer/backup/observer:** Amith+Sreehari / Nihad / reciprocal / Sreeprada; Archa indexes.
- **Inputs:** Parts, tools and official data sheet.
- **Expected output:** Accepted components, `FW-v0.1.0`, pin/hardware revision and stationary raw/timing report.
- **Quantitative exit:** 100% part status; five boots; stable `0xE5`; proposed ±1% achieved rate; zero unexplained drops in gate capture.
- **Documentation:** Acceptance, firmware, wiring, run and error records.
- **Risks/fallback:** Replace quarantined module or lower SPI temporarily for diagnosis.
- **Prohibited:** Final thresholds, I²C, seller-code-only acceptance, motor from USB.

### Week 3 — Safe rig and mount

- **Objective/sequence:** Motor isolation/protection → base/mount → captive fixture/guard → low-energy normal/abnormal safety pilots.
- **Owner/reviewer/backup/observer:** Amith / Nihad / Sreehari / Sreeprada; Archa media.
- **Inputs:** Motor, supply, mechanical parts, tools and PPE.
- **Expected output:** Approved rig, mount, safety record and start/stop procedure.
- **Quantitative exit:** Guard covers rotating envelope; disconnect works; zero loosening/contact/base motion in declared pilot.
- **Documentation:** Rig, mount, safety, measurement and media records.
- **Risks/fallback:** Unsafe fixture → safer redesign/fan or stop abnormal work.
- **Prohibited:** Loose/glued mass, live adjustment, open mains, unsupervised observer.

### Week 4 — Normal and abnormal data

- **Objective/sequence:** Freeze pilot protocol → normal sessions → power-off fixture → abnormal sessions → hash/manifests/split.
- **Owner/reviewer/backup/observer:** Sreehari+Amith / Nihad / reciprocal / Sreeprada; Archa indexes.
- **Inputs:** Passed configuration, storage and checklists.
- **Expected output:** Immutable labeled training/pilot data and reserved held-out sessions.
- **Quantitative exit:** Approved session count; 100% accepted runs have IDs/ground truth/hash/integrity; zero uncontrolled condition.
- **Documentation:** Safety, session, run, dataset and photo records.
- **Risks/fallback:** Integrity or fixture failure → preserve, invalidate visibly and repeat after an approved fix.
- **Prohibited:** Random-window split, unsafe increase, hidden trimming, model-derived label.

### Week 5 — Baseline and RGB/USB

- **Objective/sequence:** Reference vectors → DC/RMS → training threshold/persistence → states/RGB/schema → pilot end-to-end.
- **Owner/reviewer/backup/observer:** Sreehari / Nihad / Amith / Sreeprada; Archa wording.
- **Inputs:** Pilot data, RGB hardware and unit/reference vectors.
- **Expected output:** Baseline release, parameters/schema and operator SOP.
- **Quantitative exit:** RMS reference tolerance; all states exercised; no acquisition regression; backup run.
- **Documentation:** Firmware, parameter, calibration, run and decision records.
- **Risks/fallback:** Excessive false alarms → training-only simplification after integrity/mount review.
- **Prohibited:** Mahalanobis, held-out tuning, hidden smoothing, final claim.

### Week 6 — Triggered FFT, challenge testing and validation-design preparation

- **Objective/sequence:** FFT reference/resource → minimal bands/trigger → challenge tests → prepare criteria, split, protocol and configuration-freeze records. Do not open held-out validation.
- **Owner/reviewer/backup/observer:** Sreehari+Nihad / technical team / Amith / Archa; Sreeprada dry-run operator.
- **Inputs:** Baseline, FFT reference vectors and data manifests.
- **Expected output:** Minimum end-to-end system, challenge evidence and validation-design package ready for final hardware stabilization.
- **Quantitative exit:** FFT tolerance/no integrity loss; zero split leakage; protocol and freeze fields drafted; held-out assignments remain sealed.
- **Documentation:** FFT, resource, challenge-test and freeze records.
- **Risks/fallback:** FFT trouble → reduce it or compute it offline and freeze the baseline.
- **Prohibited:** Optional comparator, new feature after freeze, test access, dense attribution.

### Week 7 — Final hardware/configuration freeze, then locked validation

- **Objective/sequence:** First complete stable wiring/perfboard or connectorization, final strain relief, guard, labels, mount and as-built pinout → boot/readback and normal/abnormal regression → recalibration on training data if required → technical-team/project-lead criteria freeze → final CFG and non-held-out dry run → only then open and execute locked held-out validation → immutable hashes/frozen analysis/deviations.
- **Owner/reviewer/backup/observer:** Sreeprada+Sreehari / Nihad / Amith / Archa.
- **Inputs:** Sealed test set, locked configuration/protocol and safety approval.
- **Expected output:** Final stable hardware and configuration, regression/calibration evidence as needed, followed by a traceable locked result package for that same configuration.
- **Quantitative exit:** Protocol complete/explicitly invalid; all metrics denominators/IDs; zero unexplained loss; no post-test tuning; regression documented.
- **Documentation:** Formal test, raw hashes, results, deviation and hardware records.
- **Risks/fallback:** If stabilization cannot finish early enough, do not open the held-out test; narrow optional scope or extend the plan. Criterion miss/failure → honest limitation or a separately reviewed test on genuinely unseen evidence only.
- **Prohibited:** Held-out test before hardware stabilization/freeze, hidden rerun, same-data retune, post-test material rebuild under the same validation claim, criterion invention.

### Week 8 — Demonstration, handover and archive

- **Objective/sequence:** Scripts/fallback → three rehearsals → report links → clean reproduction/handover → two verified archive copies.
- **Owner/reviewer/backup/observer:** Archa / Nihad / Sreehari+Amith / Sreeprada.
- **Inputs:** Final hardware, locked evidence, scripts and archive tools.
- **Expected output:** Demo, report, manifest, handover and verified archive.
- **Quantitative exit:** 3 rehearsals; 2 operators; 1 clean raw-to-result reproduction; all manifest hashes verify twice.
- **Documentation:** Demo, report, archive, handover and disclosure records.
- **Risks/fallback:** Live failure → prerecorded traceable evidence and safe shutdown explanation.
- **Prohibited:** New feature, unsafe shortcut, patent/industrial claim, deleted failure.

## 9. Decision priorities under schedule pressure

Remove work in this order:

1. ordinary Mahalanobis comparator;
2. extra spectral bands/visual polish;
3. enclosure aesthetics and nonessential UI;
4. extra pilot variants beyond the approved minimum.

Never remove the guard, motor/logic isolation, sensor identity/readback, acquisition integrity counters, RMS+persistence, immutable raw data, leakage-resistant held-out test, RGB/USB, negative-result preservation or handover.

## 10. Final claim review card

Before any report, slide or statement, ask:

- Does it say “controlled rig” and identify configuration limits?
- Is every number measured, linked and denominated?
- Is a proposed value clearly marked proposed rather than achieved?
- Does Abnormal remain a behavior flag rather than diagnosis?
- Are FFT and Mahalanobis described in their frozen roles?
- Are PIRG, patentability and industrial claims absent?
- Is any technical statement from Archa/Sreeprada reviewed by a technical member?

## 11. Current specification anchors

- ADXL345: official 2.0–3.6 V supply, 3-/4-wire SPI, `DEVID=0xE5`, bandwidth `ODR/2`, ≥400 kHz SPI recommended at 800 Hz and ≥2 MHz at 1600/3200 Hz: [Analog Devices data sheet](https://www.analog.com/media/en/technical-documentation/data-sheets/ADXL345.PDF), accessed 2026-08-09.
- Preferred board: exact `ESP32-DEVKITC-32E`; Micro-USB is power plus USB-UART; USB/5 V-header/3.3 V-header power methods are mutually exclusive: [Espressif DevKitC V4 guide](https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32/esp32-devkitc/user_guide.html), accessed 2026-08-09.
- Avoid the ESP32 strapping pins GPIO0/2/5/12/15 for new dependencies when a safe ordinary GPIO exists: [Espressif ESP-IDF GPIO guide](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/peripherals/gpio.html), accessed 2026-08-09.
- Arduino-ESP32 installation and current documentation: [installation guide](https://docs.espressif.com/projects/arduino-esp32/en/latest/installing.html) and [3.3.11 documentation](https://docs.espressif.com/projects/arduino-esp32/), accessed 2026-08-09.

## 12. Open decisions before their gates

1. Actual calendar/start date and whether the 12- or 8-week plan governs.
2. Technical-team/project-lead review and freeze of quantitative final criteria before labeled locked-validation use; faculty/teacher review only if explicitly required and recorded.
3. Exact lab equipment availability and responsible faculty/lab safety approver, if required by local rules.
4. Exact base, clamp, captive 3 mm hub/eccentric, guard, fuse type/rating and current-limit method after motor measurement.
5. Toolchain/FFT/host capture versions after two-computer smoke test.
6. Pilot-frozen ODR/range/SPI/window/overlap, warm-up, durations, RMS score, thresholds, persistence, FFT trigger/bands and invalidity limits.
7. Approved shared storage, backup and confidential future-research access locations.
