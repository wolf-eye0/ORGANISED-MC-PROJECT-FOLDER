# VibeGuard Lab Evidence and Engineering Logbook

**Document status:** Ready-to-use logging system, revision 1.1  
**Audience:** All five team members  
**Rule:** Every success, failure, unusual observation, change and decision is recorded. Raw data and prior records are never silently overwritten.

**Current project-state control:** `Project_mC_Final_Selection_and_Phase4_Entry_Memo.md` and `Project_mC_Decision_Register_v1.3.md`. Decision Register v1.2 remains an unchanged historical predecessor. VibeGuard is final, Phase 3C is closed, Phase 4 is open, Phase 4A is active, and PIRG remains outside the semester MVP.

**Revision 1.1 — team-role synchronization:** Sreeprada K S retains Experimental Operations/Test/Inventory ownership and adds supervised Firmware & Data Learning with Sreehari K, including beginner coding. Archa Pramod retains Documentation/Communication/Demonstration ownership and adds lightweight Hardware Familiarization with Amith Krishna Das. Subsystem ownership and technical boundaries are unchanged.

## 1. Evidence integrity rules

1. Record work on the day it occurs. Use local time with timezone (`Asia/Kolkata`, `IST`, UTC+05:30) and, where the capture system supports it, UTC as well.
2. Never backdate. If an old record is wrong, append `CORRECTION-YYYYMMDD-HHMM` with author, reason and link to the original. Preserve the original text/file.
3. Never edit raw acquisition files. Copy originals into `05_Test_Protocols_and_Data/RAW_IMMUTABLE/`, calculate SHA-256 and make them read-only where supported. All cleaning/feature work creates a derivative in `Processed/`.
4. Never delete a failed experiment. Mark validity and link `ERR-###`/corrective action. Keep incomplete/corrupt files with their hashes if safe and legally appropriate.
5. A result is formal only if it links to run/test, dataset, complete configuration, firmware/commit, parameters/schema, raw hashes and analysis version.
6. A configuration change is a new traceable record. Do not replace a pinout, threshold, mount, rig, firmware or script while keeping its old ID.
7. Separate facts from interpretation. Use `EXPECTED`, `ACTUAL`, `HYPOTHESIS`, `TEST` and `OUTCOME` fields.
8. Use `NOT PERFORMED`, `NOT MEASURED`, `UNKNOWN` or `NOT APPLICABLE`; never fill a blank with a guess.
9. Record negative evidence and protocol deviations. A pass/fail criterion must have been declared before the result it judges.
10. Public semester material contains Level-1 VibeGuard only. Potentially claim-oriented or PIRG-related material goes only to `FUTURE_RESEARCH_CONFIDENTIAL/` with the disclosure log.

## 2. Identifier and filename convention

| Object | ID pattern | Example format (not an actual record) |
|---|---|---|
| Component | `COMP-###` | `COMP-001` |
| Procurement event/order | `PROC-###` | `PROC-001` |
| Incoming acceptance | `ACCEPT-###` | `ACCEPT-001` |
| Hardware revision | `HW-REV-###` | `HW-REV-001` |
| Wiring/pinout | `PIN-###` | `PIN-001` |
| Sensor mount/remount | `MOUNT-###` | `MOUNT-001` |
| Motor rig configuration | `RIG-###` | `RIG-001` |
| Toolchain | `TOOL-###` | `TOOL-001` |
| Firmware release | `FW-vMAJOR.MINOR.PATCH` | `FW-v0.1.0` |
| USB schema | `SCHEMA-###` | `SCHEMA-001` |
| Parameter set | `PARAM-###` | `PARAM-001` |
| Full configuration | `CFG-###` | `CFG-001` |
| Experiment session | `SESSION-YYYYMMDD-###` | `SESSION-20260809-001` |
| Run | `RUN-YYYYMMDD-###` | `RUN-20260809-001` |
| Formal test | `TEST-YYYYMMDD-###` | `TEST-20260809-001` |
| Dataset | `DATASET-###` | `DATASET-001` |
| Calibration | `CAL-YYYYMMDD-###` | `CAL-20260809-001` |
| Error/failure/incident | `ERR-###` | `ERR-001` |
| Corrective action | `CA-###` | `CA-001` |
| Milestone | `MILESTONE-###` | `MILESTONE-001` |
| Decision | `DEC-###` | `DEC-001` |
| Risk | `RISK-###` | `RISK-001` |
| Safety inspection | `SAFE-YYYYMMDD-###` | `SAFE-20260809-001` |
| Photograph/video | `PHOTO-###`, `VIDEO-###` | `PHOTO-001` |
| Meeting | `MEET-YYYYMMDD-###` | `MEET-20260809-001` |
| Faculty communication | `COMM-###` | `COMM-001` |
| Public disclosure | `DISC-###` | `DISC-001` |
| Future-research observation | `OBS-###` | `OBS-001` |
| Protocol deviation | `DEV-###` | `DEV-001` |

IDs are never reused. Maintain `ID_MASTER.csv` with ID, type, title, creator, creation timestamp, status and path. Assignment can be serialized by Nihad or a controlled issue tracker. A reserved but unused ID remains marked `VOID—NOT REUSED` with reason.

### Filename rules

- Controlled record: `ID__short-slug__YYYYMMDD.md`
- Raw run: `RUN-YYYYMMDD-###__CFG-###__GROUNDTRUTH__RAW.csv`
- Serial log: `RUN-YYYYMMDD-###__SCHEMA-###__SERIAL.log`
- Media: `PHOTO-###__RUN-or-CFG__view__YYYYMMDD-HHMMSS.jpg`
- Firmware archive: `FW-vX.Y.Z__commit-short__YYYYMMDD.zip`
- Corrections/addenda: original ID plus `__ADDENDUM-YYYYMMDD-HHMM__author.md`

Use only letters, digits, hyphens and underscores. Do not use `final-final`, `new`, `latest` or ambiguous names. The controlled pointer may be called `CURRENT`, but it points to an immutable identified version.

## 3. Configuration and provenance chain

Every run header must resolve this chain:

```text
RUN → SESSION → TEST/PROTOCOL → CFG
CFG → HW-REV + PIN + MOUNT + RIG + FW@commit + PARAM + SCHEMA
RUN → raw file(s) + SHA-256 → DATASET → analysis commit → result row/figure
```

If any link is missing, label the output exploratory or unresolved. Do not include it as a formal metric.

## 4. Review and signature convention

A signature line is an evidence review, not a claim that the reviewer personally performed every action.

```text
Prepared by: NAME | role | YYYY-MM-DD HH:MM IST | signature/approved commit
Reviewed by: NAME | scope reviewed | YYYY-MM-DD HH:MM IST | signature/approved commit
Observer: NAME | physically present? YES/NO | YYYY-MM-DD HH:MM IST
Correction/addendum links: ...
```

Electronic approval may be a signed PDF, authenticated repository approval/commit or dated institutional system entry. Record the method. Safety and locked-test gates need a second person. Archa/Sreeprada may record technical facts; a technical member reviews technical claims.

## 5. Member-specific logging duties

| Member | Maintains at minimum | Reviews/constraints |
|---|---|---|
| **Nihad P C — Technical Integration Lead / Project Manager / Configuration & Evidence Lead** | Architecture/configuration, interfaces, schedule, decisions, failures, risk, gates, coordination, weekly freeze and evidence integrity | Not sole safety/locked-test approver; keeps backup access current. |
| **Sreehari K — Firmware, DSP & Data Lead / Software Systems Mentor** | Firmware/commits, sensor/SPI, integrity, RMS/persistence, FFT, comparator, USB schema, scripts, splits, metrics and Sreeprada learning reviews | Retains firmware/DSP/data ownership and decides whether isolated contributions enter controlled work. |
| **Amith Krishna Das — Hardware, Power, Rig & Safety Lead** | Procurement, IDs, power/wiring, rig/mounts, dimensions, safety, failures/repairs, photos and Archa familiarization acknowledgements | Retains heavy hardware/safety ownership; familiarization does not make Archa alternate owner. |
| **Sreeprada K S — Experimental Operations, Test & Inventory Coordinator / Firmware & Data Learning Associate & Technical Observer** | **Primary:** inventory, preparation, checklists, run IDs, remounts, observations, repeated tests, failures, conformance and learning notes. **Secondary:** firmware procedure observed/executed, Arduino/ESP32, serial capture, approved scripts, isolated coding exercises, Sreehari review and controlled contributions. | Independent primary role; no independent controlled firmware/settings/split/locked-script changes or merges. |
| **Archa Pramod — Documentation, Communication & Demonstration Lead / Hardware Familiarization Associate & Technical Observer** | **Primary:** minutes, faculty communication, evidence index, revisions, media, progress, report, presentation/demo. **Familiarization:** observed hardware sessions, component functions, diagram, safety, mount/rig/guard and Amith acknowledgement. | Independent primary role; observational/explanatory only; no hardware design, critical soldering, rig modification or safety approval. |

Sreeprada ↔ Sreehari supports active firmware/coding/data learning. Archa ↔ Amith supports documentation-oriented hardware familiarization. These are not managerial reporting relationships and do not transfer subsystem ownership.

### Lightweight learning/familiarization record

This traces training and qualification; it is not an academic grading system.

```yaml
learning_mode: OBSERVED | ASSISTED | SUPERVISED_EXECUTION | QUALIFIED_FROZEN_PROCEDURE
learning_area: FIRMWARE_DATA | HARDWARE_FAMILIARIZATION | EXPERIMENT_OPERATION
mentor_or_technical_owner:
procedure_or_topic:
date:
evidence:
review:
```

Training code stays separate from controlled firmware until Sreehari reviews it. Hardware familiarization records understanding, not authority to design, change or approve hardware.

## 6. Completed-example warning

Every example below is marked **SYNTHETIC TRAINING EXAMPLE—NOT PROJECT EVIDENCE**. The names, IDs, values, actions and outcomes demonstrate form completion only. They do not state that a purchase, experiment, pass, measurement, teacher condition or disclosure occurred. Delete the example block when copying a template into a real identified record; never copy synthetic values into project evidence.

## 7. Ready-to-copy templates

### Template 1 — Master Project Daily Lab Log

**Who/when:** The day's activity lead opens it before work and closes it the same day; everyone adds their own action.  
**Reviewer/sign:** Nihad daily or next working day; relevant technical owner reviews technical claims.  
**Storage/name:** `01_Selected_Project/Orientation_and_Minutes/DAILY-YYYYMMDD__daily-log.md`.

**Mandatory fields/template:**

```yaml
record: DAILY-YYYYMMDD
date/timezone: YYYY-MM-DD | Asia/Kolkata UTC+05:30
opened_by:
people_present_and_times:
planned_objectives:
safety_brief/check_required: YES/NO | SAFE-ID/N-A
timeline:
  - HH:MM | person | action | exact IDs/files | observed outcome
successes_and_milestone_links:
failures/unusual_observations: ERR/OBS/RISK IDs or NONE
configuration_changes: DEC/HW/PIN/MOUNT/RIG/FW/PARAM/SCHEMA IDs or NONE
raw/processed/media_files_and_hashes:
decisions_made/pending:
next_actions: action | owner | due | reviewer
open_safety_items:
prepared/reviewed/observer_signatures:
```

**SYNTHETIC TRAINING EXAMPLE—NOT PROJECT EVIDENCE:**

```yaml
record: DAILY-TRAINING-ONLY
date/timezone: 2026-08-09 | Asia/Kolkata UTC+05:30
opened_by: Archa Pramod
people_present_and_times: Archa 10:00-10:20; Sreeprada 10:00-10:20
planned_objectives: Practise ID assignment; no hardware present
safety_brief/check_required: NO | N-A
timeline: 10:05 | Sreeprada | created fictitious TRAINING-RUN form | no experiment performed
successes_and_milestone_links: Training form located and reviewed
failures/unusual_observations: NONE
configuration_changes: NONE
raw/processed/media_files_and_hashes: NONE
decisions_made/pending: NONE
next_actions: Delete synthetic values when copying | all | before real use | Nihad
open_safety_items: NONE
prepared/reviewed/observer_signatures: Archa / Nihad to review training only / Sreeprada
```

### Template 2 — Component/Inventory Register

**Who/when:** Amith assigns hardware IDs at receipt; Sreeprada maintains location/quantity after every movement.  
**Reviewer/sign:** Nihad for critical components; Sreehari for MCU/sensor identity.  
**Storage/name:** `02_BOM_and_Procurement/Component_IDs_and_Acceptance/COMPONENT_MASTER.csv` plus `COMP-###__slug__YYYYMMDD.md`.

```yaml
component_id:
generic_function:
manufacturer/brand:
exact_part_number_or_unknown:
seller_sku/order/procurement_id:
quantity_received/accepted/spare:
markings_and_batch/lot/serial:
physical_description_and_photos:
claimed_specification_source/date:
actual_acceptance_record/status:
assigned_configuration_ids:
storage_location/custodian:
condition/history:
invoice/warranty/return_deadline:
last_inventory_check:
prepared/reviewed_signatures:
```

**SYNTHETIC TRAINING EXAMPLE—NOT PROJECT EVIDENCE:**

```yaml
component_id: COMP-TRAINING-001
generic_function: Placeholder RGB indicator
manufacturer/brand: UNKNOWN—TRAINING
exact_part_number_or_unknown: UNKNOWN
seller_sku/order/procurement_id: NO PURCHASE—TRAINING
quantity_received/accepted/spare: 0/0/0
markings_and_batch/lot/serial: NOT APPLICABLE
physical_description_and_photos: NONE
claimed_specification_source/date: NONE
actual_acceptance_record/status: NOT RECEIVED
assigned_configuration_ids: NONE
storage_location/custodian: NONE
condition/history: Training entry only
invoice/warranty/return_deadline: NONE
last_inventory_check: 2026-08-09 training exercise
prepared/reviewed_signatures: Sreeprada / Amith (training review only)
```

### Template 3 — Procurement Register

**Who/when:** Amith creates before cart approval and updates at order, dispatch, delivery, return/refund and final cost.  
**Reviewer/sign:** Nihad approves specification/budget before purchase; Sreehari reviews MCU/sensor equivalence; Archa checks source capture.  
**Storage/name:** `02_BOM_and_Procurement/Orders_Invoices_Delivery/PROC-###__slug__YYYYMMDD.md`.

```yaml
procurement_id/status: PLANNED|APPROVED|ORDERED|DISPATCHED|DELIVERED|CLOSED|CANCELLED
request_date/requester:
component/function/required_specification:
exact_title/manufacturer/MPN/SKU:
quantity_and_spare_reason:
preferred_seller/url/access_timestamp:
backup_seller/url/access_timestamp:
unit_price_ex_GST/GST/unit_price_inc_GST:
shipping/discount/projected_landed_total:
stock_text/delivery_estimate/return_window:
same_day_recheck_by/time:
technical_equivalence_review:
budget_before/after/projected_vs_actual:
authorization_to_order:
actual_order/invoice/date/payment_custodian: DO NOT FILL UNTIL REAL
dispatch/tracking/delivery:
linked_COMP/ACCEPT/return/refund:
notes/risks:
prepared/reviewed_signatures:
```

**SYNTHETIC TRAINING EXAMPLE—NOT PROJECT EVIDENCE:**

```yaml
procurement_id/status: PROC-TRAINING-001 | PLANNED
request_date/requester: 2026-08-09 | Amith
component/function/required_specification: Fictitious test resistor; form practice only
exact_title/manufacturer/MPN/SKU: UNKNOWN
quantity_and_spare_reason: 0 | no order
preferred_seller/url/access_timestamp: NONE
backup_seller/url/access_timestamp: NONE
unit_price_ex_GST/GST/unit_price_inc_GST: NOT PRICED
shipping/discount/projected_landed_total: NOT PRICED
stock_text/delivery_estimate/return_window: UNKNOWN
same_day_recheck_by/time: NOT PERFORMED
technical_equivalence_review: NOT PERFORMED
budget_before/after/projected_vs_actual: NOT APPLICABLE
authorization_to_order: NOT AUTHORIZED
actual_order/invoice/date/payment_custodian: NO PURCHASE
dispatch/tracking/delivery: NONE
linked_COMP/ACCEPT/return/refund: NONE
notes/risks: Synthetic example must not be copied
prepared/reviewed_signatures: Amith / Nihad (training only)
```

### Template 4 — Incoming Component Acceptance Record

**Who/when:** Amith opens immediately at receipt, before integration; Sreeprada photographs/labels under supervision.  
**Reviewer/sign:** Nihad; Sreehari additionally reviews MCU/sensor electrical identity.  
**Storage/name:** `02_BOM_and_Procurement/Component_IDs_and_Acceptance/ACCEPT-###__COMP-###__YYYYMMDD.md`.

```yaml
acceptance_id/component_id/procurement_id:
receipt_date/time/persons/package_condition:
invoice/ordered_vs_received_identity:
photos_front/back/markings/packaging:
visual_check_items_and_results:
dimensions/connectors/pin_labels:
test_equipment_ids/calibration_status:
powered_test_preconditions/current_limit:
tests: procedure | predeclared accept/reject | actual observation | PASS/FAIL/NOT RUN
for_ESP32: exact SKU/module | USB enumeration | flash/boot link
for_ADXL345: breakout identity | SPI pins | DEVID 0xE5 link | readback link
for_supply: label | plug | polarity | no-load/load voltage | heating
for_motor: shaft/rotation/leads | voltage/current/speed/temperature links
disposition: ACCEPTED|CONDITIONAL|QUARANTINED|REJECTED
open_conditions/return_deadline/action_owner:
configuration_use_authorized:
prepared/reviewed/observer_signatures:
```

**SYNTHETIC TRAINING EXAMPLE—NOT PROJECT EVIDENCE:**

```yaml
acceptance_id/component_id/procurement_id: ACCEPT-TRAINING-001 / COMP-TRAINING-001 / NONE
receipt_date/time/persons/package_condition: NOT RECEIVED / training exercise
invoice/ordered_vs_received_identity: NOT APPLICABLE
photos_front/back/markings/packaging: NONE
visual_check_items_and_results: NOT PERFORMED
dimensions/connectors/pin_labels: NOT MEASURED
test_equipment_ids/calibration_status: NONE
powered_test_preconditions/current_limit: NOT PERFORMED
tests: no test | no criterion | no observation | NOT RUN
disposition: QUARANTINED—TRAINING PLACEHOLDER
open_conditions/return_deadline/action_owner: Do not use / N-A / Amith
configuration_use_authorized: NO
prepared/reviewed/observer_signatures: Amith / Nihad (training only) / Sreeprada
```

### Template 5 — Hardware Revision Register

**Who/when:** Amith creates before each physical change and closes after inspection/regression.  
**Reviewer/sign:** Nihad for interfaces/configuration; Sreehari for signal/pin effects.  
**Storage/name:** `03_Hardware_and_CAD/HW_Revisions/HW-REV-###__slug__YYYYMMDD.md`.

```yaml
hardware_revision/status: PROPOSED|BUILT|TESTED|FROZEN|RETIRED
parent_revision:
reason/problem/linked_ERR_DEC:
component_ids_added/removed:
exact_changes_before_vs_after:
schematic/wiring/PIN/MOUNT/RIG_links:
power_domains/protection:
dimensions/materials/fasteners/connectors:
photos_before/during/after:
safety_effect_and_review:
required_regression_protocol:
actual_regression_TEST/RUN_results: NOT RUN until real
known_limitations/open_items:
compatible_FW/PARAM/CFG:
build_owner/date/reviewer/signatures:
```

**SYNTHETIC TRAINING EXAMPLE—NOT PROJECT EVIDENCE:**

```yaml
hardware_revision/status: HW-REV-TRAINING-001 | PROPOSED
parent_revision: NONE
reason/problem/linked_ERR_DEC: Practise change documentation; no hardware
component_ids_added/removed: NONE
exact_changes_before_vs_after: Before NONE; after NONE
schematic/wiring/PIN/MOUNT/RIG_links: NONE
power_domains/protection: NOT APPLICABLE
dimensions/materials/fasteners/connectors: NOT MEASURED
photos_before/during/after: NONE
safety_effect_and_review: No physical work
required_regression_protocol: NONE
actual_regression_TEST/RUN_results: NOT RUN
known_limitations/open_items: Synthetic only
compatible_FW/PARAM/CFG: NONE
build_owner/date/reviewer/signatures: Amith / 2026-08-09 / Nihad (training only)
```

### Template 6 — Wiring/Pinout Configuration Record

**Who/when:** Amith prepares before wiring; Sreehari checks firmware mapping; update before any wire moves.  
**Reviewer/sign:** Nihad plus Sreehari; Sreeprada/Archa may observe/photo only.  
**Storage/name:** `03_Hardware_and_CAD/Wiring_and_Pinouts/PIN-###__HW-REV-###__YYYYMMDD.md`.

```yaml
pinout_id/status/exact_board_SKU:
official_board_document_url/version/access_date:
sensor_breakout_id/photo/pin-label-source:
logic_voltage_and_power_source:
motor_power_domain_and_isolation_statement:
connections:
  - signal | source pin | destination pin | wire color/label | series part | direction
strapping/flash/input-only pin review:
RGB_common_type/channel_resistor_ids:
continuity/short/polarity_check_procedure:
actual_check_observations/test_equipment:
firmware_pin_definitions_commit:
photos/diagram/hash:
change_from_parent/reason:
compatible_HW/FW/CFG:
prepared/reviewed/observer_signatures:
```

**SYNTHETIC TRAINING EXAMPLE—NOT PROJECT EVIDENCE:**

```yaml
pinout_id/status/exact_board_SKU: PIN-TRAINING-001 | DRAFT | NO BOARD
official_board_document_url/version/access_date: NONE
sensor_breakout_id/photo/pin-label-source: NONE
logic_voltage_and_power_source: NOT WIRED
motor_power_domain_and_isolation_statement: Training statement: motor must remain separate
connections: signal EXAMPLE_ONLY | source GPIO-X | destination SENSOR-X | no wire | none | N-A
strapping/flash/input-only pin review: NOT PERFORMED
RGB_common_type/channel_resistor_ids: NOT SELECTED
continuity/short/polarity_check_procedure: NOT PERFORMED
actual_check_observations/test_equipment: NONE
firmware_pin_definitions_commit: NONE
photos/diagram/hash: NONE
change_from_parent/reason: NONE / training
compatible_HW/FW/CFG: NONE
prepared/reviewed/observer_signatures: Amith / Sreehari and Nihad (training only) / Sreeprada
```

### Template 7 — Sensor Mount and Remount Register

**Who/when:** Amith records every installation/removal/remount before data; Sreeprada takes labeled photos and procedure checks.  
**Reviewer/sign:** Nihad; Sreehari checks axis/orientation implications.  
**Storage/name:** `03_Hardware_and_CAD/Mounts/MOUNT-###__slug__YYYYMMDD.md`.

```yaml
mount_id/parent_mount/event: INITIAL|REMOUNT|REPAIR
date/time/people/location:
sensor_component_id/rig_id:
surface/bracket/material/dimensions:
orientation: axis arrows and reference drawing/photo
attachment: fastener IDs/size/torque if measured OR adhesive/type/prep/cure
cable_route/strain_relief/clearance:
cleaning/surface_preparation:
photos_before/contact/after/reference_marks:
power_off_confirmed:
procedure_steps_and_deviations:
post_mount_identity/orientation/stationary_checks:
linked_runs/calibration/configuration:
expected_repeatability criterion:
actual comparison: TO BE MEASURED
damage/looseness/open_items:
prepared/reviewed/observer_signatures:
```

**SYNTHETIC TRAINING EXAMPLE—NOT PROJECT EVIDENCE:**

```yaml
mount_id/parent_mount/event: MOUNT-TRAINING-001 / NONE / INITIAL
date/time/people/location: 2026-08-09 / Sreeprada and Amith / classroom training
sensor_component_id/rig_id: NONE / NONE
surface/bracket/material/dimensions: Paper sketch only / NOT MEASURED
orientation: EXAMPLE arrows drawn; no sensor
attachment: NONE
cable_route/strain_relief/clearance: NONE
cleaning/surface_preparation: NOT PERFORMED
photos_before/contact/after/reference_marks: NONE
power_off_confirmed: NO HARDWARE PRESENT
procedure_steps_and_deviations: Training form only
post_mount_identity/orientation/stationary_checks: NOT RUN
linked_runs/calibration/configuration: NONE
expected_repeatability criterion: NOT DEFINED
actual comparison: NOT MEASURED
damage/looseness/open_items: NONE / synthetic
prepared/reviewed/observer_signatures: Amith / Nihad (training only) / Sreeprada
```

### Template 8 — Motor-Rig Configuration Register

**Who/when:** Amith creates for every base/motor/power/fixture/guard combination before operation.  
**Reviewer/sign:** Nihad and safety reviewer; Sreehari reviews sensor/config linkage; a Lab Assistant observes.  
**Storage/name:** `03_Hardware_and_CAD/Rig_and_Guard/RIG-###__slug__YYYYMMDD.md`.

```yaml
rig_id/status/parent:
base: material/mass/dimensions/feet/bench restraint
motor: COMP-ID/label/rated claim/shaft/position/clamp/fasteners
power: adapter/supply ID/switch/disconnect/fuse/wiring/polarity
normal_fixture_definition:
abnormal_fixture: hub/positive retention/mass ID/measured mass/radius/fasteners
guard: material/dimensions/attachment/rotating-envelope clearance
sensor_mount/cable_clearance:
tools/PPE/inspection_equipment:
current_limit/start_sequence/stop_sequence:
predeclared electrical/mechanical/temperature criteria:
measured pilot voltage/current/speed proxy/temperature: TO BE MEASURED
photos/drawings/reference_marks:
safety_inspection/run/test links:
known_limitations/change_history:
prepared/reviewed/observer_signatures:
```

**SYNTHETIC TRAINING EXAMPLE—NOT PROJECT EVIDENCE:**

```yaml
rig_id/status/parent: RIG-TRAINING-001 / DRAFT / NONE
base: no base; dimensions NOT MEASURED
motor: NONE
power: NONE; motor and logic separation stated only
normal_fixture_definition: NONE
abnormal_fixture: NONE; unsecured fixtures prohibited
guard: NOT BUILT
sensor_mount/cable_clearance: NONE
tools/PPE/inspection_equipment: NONE
current_limit/start_sequence/stop_sequence: NOT RUN
predeclared electrical/mechanical/temperature criteria: NOT DEFINED
measured pilot voltage/current/speed proxy/temperature: NOT MEASURED
photos/drawings/reference_marks: training sketch only
safety_inspection/run/test links: NONE
known_limitations/change_history: Synthetic form; cannot be operated
prepared/reviewed/observer_signatures: Amith / Nihad (training only) / Sreeprada
```

### Template 9 — Firmware Change Log

**Who/when:** Sreehari records each meaningful code/configuration change at commit time, before test use.  
**Reviewer/sign:** Nihad reviews interfaces/behavior; Amith reviews hardware effects.  
**Storage/name:** `04_Firmware/Source/CHANGELOG.md` entry plus issue/commit; exported `FWCHANGE-YYYYMMDD-###__slug.md` if needed.

```yaml
change_id/date/author/branch:
parent_commit/new_commit:
linked_issue_ERR_DEC_requirement:
files/functions_changed:
plain_language_reason:
technical_change:
interfaces/schema/pins/parameters affected:
expected behavior/risks:
tests_required/predeclared criteria:
actual unit/bench/run links: NOT RUN until real
result/status: DRAFT|REVIEWED|MERGED|REVERTED
rollback_commit/instructions:
documentation updated:
reviewer/signature:
```

**SYNTHETIC TRAINING EXAMPLE—NOT PROJECT EVIDENCE:**

```yaml
change_id/date/author/branch: FWCHANGE-TRAINING-001 / 2026-08-09 / Sreehari / training-only
parent_commit/new_commit: NONE / NONE
linked_issue_ERR_DEC_requirement: Practise changelog
files/functions_changed: NONE
plain_language_reason: Learn mandatory fields
technical_change: No code changed
interfaces/schema/pins/parameters affected: NONE
expected behavior/risks: None; synthetic
tests_required/predeclared criteria: NONE
actual unit/bench/run links: NOT RUN
result/status: DRAFT
rollback_commit/instructions: NONE
documentation updated: Training form
reviewer/signature: Nihad (training only)
```

### Template 10 — Firmware Release/Commit Register

**Who/when:** Sreehari creates for every firmware version used on hardware or in a formal analysis.  
**Reviewer/sign:** Nihad; backup reproducer signs the flash/capture step.  
**Storage/name:** `04_Firmware/Releases/FW-vX.Y.Z__commit-short__YYYYMMDD.md` plus immutable source/binary/hash files.

```yaml
firmware_version/release_status: PILOT|CANDIDATE|LOCKED|RETIRED
repository/branch/commit/tag:
source_archive/binary/partition/hash:
build_timestamp/build_host/toolchain_id/dependencies:
exact_board_target/SKU:
compatible_HW/PIN/MOUNT/RIG/PARAM/SCHEMA/CFG:
feature/state summary:
known_issues/limitations:
unit/bench/regression_TEST/RUN links:
predeclared release criteria/actual disposition:
flash_and_capture_reproduction: person/computer/date/evidence
rollback_release:
prepared/reviewed/backup_signatures:
```

**SYNTHETIC TRAINING EXAMPLE—NOT PROJECT EVIDENCE:**

```yaml
firmware_version/release_status: FW-v0.0.0-TRAINING / PILOT
repository/branch/commit/tag: NONE / training / NONE / NONE
source_archive/binary/partition/hash: NONE
build_timestamp/build_host/toolchain_id/dependencies: NOT BUILT
exact_board_target/SKU: NO BOARD
compatible_HW/PIN/MOUNT/RIG/PARAM/SCHEMA/CFG: NONE
feature/state summary: No firmware; template practice
known_issues/limitations: Not executable
unit/bench/regression_TEST/RUN links: NONE
predeclared release criteria/actual disposition: No criteria / NOT RELEASED
flash_and_capture_reproduction: NOT PERFORMED
rollback_release: NONE
prepared/reviewed/backup_signatures: Sreehari / Nihad (training only) / Amith
```

### Template 11 — Parameter/Threshold Register

**Who/when:** Sreehari creates before a parameter set is used; every value change creates a new ID.  
**Reviewer/sign:** Nihad; Amith confirms compatible physical configuration; locked set needs freeze sign-off.  
**Storage/name:** `04_Firmware/CURRENT/Parameters/PARAM-###__slug__YYYYMMDD.md` and machine-readable companion.

```yaml
parameter_id/status: PROPOSED|PILOT|CANDIDATE|LOCKED|RETIRED
parent/reason/linked_DEC:
training_DATASET/session IDs only:
sensor: range/ODR/SPI_rate/FIFO/interrupt
window: samples/seconds/overlap/DC_removal
RMS: axes/vector/formula/units/numeric_type
threshold_rule: formula/statistics/coefficient/value/units
persistence: entry K/M/clear/calibration/startup
invalidity: drop/saturation/ID/readback limits and action
FFT: signal/Hann/N/normalization/trigger/bands/aggregation
Mahalanobis_optional: feature/mean/covariance/regularization/threshold OR DISABLED
derivation_script_commit/output_hash:
pilot_evidence/change_rationale:
held_out_data_used: MUST BE NO before lock
compatible_FW/CFG/schema:
approval/freeze_date/signatures:
```

**SYNTHETIC TRAINING EXAMPLE—NOT PROJECT EVIDENCE:**

```yaml
parameter_id/status: PARAM-TRAINING-001 / PROPOSED
parent/reason/linked_DEC: NONE / practise form / NONE
training_DATASET/session IDs only: NONE
sensor: range TO BE MEASURED; ODR TO BE FROZEN; SPI NOT SET; FIFO NOT SET
window: NOT SET
RMS: formula understood; no value/data
threshold_rule: NOT DERIVED
persistence: NOT SET
invalidity: NOT SET
FFT: DISABLED IN TRAINING EXAMPLE
Mahalanobis_optional: DISABLED
derivation_script_commit/output_hash: NONE
pilot_evidence/change_rationale: NONE
held_out_data_used: NO DATA EXISTS
compatible_FW/CFG/schema: NONE
approval/freeze_date/signatures: NOT APPROVED / Sreehari and Nihad training review
```

### Template 12 — Experiment Session Register

**Who/when:** Session lead (Sreehari for data, Amith for rig) opens before setup and closes after all runs; Sreeprada operates/checks under supervision.  
**Reviewer/sign:** Nihad; hardware/safety owner reviews related fields.  
**Storage/name:** `05_Test_Protocols_and_Data/<Pilot_or_Locked>/SESSION-YYYYMMDD-###__slug.md`.

```yaml
session_id/date/time/timezone/location:
purpose/hypothesis/protocol_TEST_ID/revision:
people: lead/operator/reviewer/observer/others and attendance times
ground_truth_condition_and_how_verified:
CFG/HW/PIN/MOUNT/RIG/FW/PARAM/SCHEMA IDs:
tool/equipment IDs/calibration status:
environment/room/bench notes:
pre_session_safety_and_configuration: SAFE-ID/check result
warmup/run_duration/rest/count plan:
sequence_of_RUN_IDs:
deviations/interruptions/disturbances:
post_session inspection:
files/hashes/dataset destination:
overall validity: VALID|PARTIAL|INVALID|PENDING REVIEW
failures/observations/decisions/next action:
prepared/reviewed/observer_signatures:
```

**SYNTHETIC TRAINING EXAMPLE—NOT PROJECT EVIDENCE:**

```yaml
session_id/date/time/timezone/location: SESSION-TRAINING-001 / 2026-08-09 / 11:00 / IST / classroom
purpose/hypothesis/protocol_TEST_ID/revision: Form practice / no hypothesis / NONE
people: Sreeprada operator trainee; Archa observer
ground_truth_condition_and_how_verified: NO PHYSICAL CONDITION
CFG/HW/PIN/MOUNT/RIG/FW/PARAM/SCHEMA IDs: NONE
tool/equipment IDs/calibration status: NONE
environment/room/bench notes: No lab work
pre_session_safety_and_configuration: NOT REQUIRED—no hardware
warmup/run_duration/rest/count plan: NONE
sequence_of_RUN_IDs: NONE
deviations/interruptions/disturbances: NONE
post_session inspection: NOT APPLICABLE
files/hashes/dataset destination: NONE
overall validity: INVALID FOR ENGINEERING USE—TRAINING ONLY
failures/observations/decisions/next action: Copy blank template for real session
prepared/reviewed/observer_signatures: Sreeprada / Nihad (training only) / Archa
```

### Template 13 — Individual Run Log

**Who/when:** Operator opens before capture and completes immediately after; Sreeprada may operate only under the frozen supervised procedure.  
**Reviewer/sign:** Session lead and Nihad for formal/locked runs; safety owner for rig runs.  
**Storage/name:** `05_Test_Protocols_and_Data/<area>/RUN-YYYYMMDD-###__CFG-###__condition.md`; raw name follows Section 2.

```yaml
run_id/session_id/test_protocol/revision:
planned_or_exploratory/ground_truth_label:
date/start/end/timezone/operator/observer:
complete_CFG_and_component IDs:
pre_run_SAFE-ID/config banner/sensor ID/readback:
host capture file/schema/start confirmed:
motor/supply/warmup/physical event markers:
planned duration/window/count:
actual start/stop_reason/duration:
operator actions/touch/disturbance timeline:
sample/block expected/actual/drop/overrun/saturation/reset counts:
state transition summary:
raw/serial/event/media files/sizes/SHA-256:
post_run inspection/temperature/noise/looseness:
validity and predeclared rule:
ERR/DEV/OBS/CA links:
next action/no tuning declaration:
prepared/reviewed/observer signatures:
```

**SYNTHETIC TRAINING EXAMPLE—NOT PROJECT EVIDENCE:**

```yaml
run_id/session_id/test_protocol/revision: RUN-TRAINING-001 / SESSION-TRAINING-001 / NONE
planned_or_exploratory/ground_truth_label: TRAINING / NO CONDITION
date/start/end/timezone/operator/observer: 2026-08-09 / NOT RUN / NOT RUN / IST / Sreeprada / Archa
complete_CFG_and_component IDs: NONE
pre_run_SAFE-ID/config banner/sensor ID/readback: NOT PERFORMED
host capture file/schema/start confirmed: NONE
motor/supply/warmup/physical event markers: NONE
planned duration/window/count: NONE
actual start/stop_reason/duration: NOT RUN / training form / 0
operator actions/touch/disturbance timeline: No hardware action
sample/block expected/actual/drop/overrun/saturation/reset counts: NOT MEASURED
state transition summary: NONE
raw/serial/event/media files/sizes/SHA-256: NONE
post_run inspection/temperature/noise/looseness: NOT APPLICABLE
validity and predeclared rule: INVALID FOR ENGINEERING USE—synthetic
ERR/DEV/OBS/CA links: NONE
next action/no tuning declaration: Use blank form for real work / no data used
prepared/reviewed/observer signatures: Sreeprada / Nihad (training only) / Archa
```

### Template 14 — Dataset Manifest

**Who/when:** Sreehari creates when runs are grouped or frozen; update by a new manifest version, never by silently replacing membership.  
**Reviewer/sign:** Nihad; Archa checks evidence paths; locked dataset needs access/freeze sign-off.  
**Storage/name:** `05_Test_Protocols_and_Data/Dataset_Manifests/DATASET-###__slug__YYYYMMDD.md` plus CSV/JSON manifest and hashes.

```yaml
dataset_id/version/status: ASSEMBLING|PILOT|TRAINING|VALIDATION_SEALED|LOCKED|RETIRED
purpose/claim_boundary:
creation_date/creator/source_protocols:
membership: RUN_ID | SESSION_ID | condition | day | operator | remount | CFG | validity | raw path | SHA-256
inclusion_rules_predeclared:
exclusion_rules_and_each_excluded_RUN/ERR:
raw_file_format/schema/units/timebase:
labels/physical_ground_truth_source:
split_assignment_by_whole_session/day/remount:
leakage_review:
class/session/duration counts:
missing/drop/saturation/quality summary:
processed_derivatives/scripts/commits/parameters/hashes:
random_seed_if_used:
access_control/seal_date/people_with_access:
changes_from_prior_version:
known_limitations:
prepared/reviewed/freeze_signatures:
```

**SYNTHETIC TRAINING EXAMPLE—NOT PROJECT EVIDENCE:**

```yaml
dataset_id/version/status: DATASET-TRAINING-001 / 0 / ASSEMBLING
purpose/claim_boundary: Learn manifest fields; no result claim
creation_date/creator/source_protocols: 2026-08-09 / Sreehari / NONE
membership: NONE—no runs
inclusion_rules_predeclared: Not defined
exclusion_rules_and_each_excluded_RUN/ERR: NONE
raw_file_format/schema/units/timebase: NONE
labels/physical_ground_truth_source: NONE
split_assignment_by_whole_session/day/remount: Not assigned
leakage_review: NOT PERFORMED
class/session/duration counts: 0/0/0
missing/drop/saturation/quality summary: NOT MEASURED
processed_derivatives/scripts/commits/parameters/hashes: NONE
random_seed_if_used: NONE
access_control/seal_date/people_with_access: Training file / not sealed
changes_from_prior_version: NONE
known_limitations: Synthetic, empty and unusable
prepared/reviewed/freeze_signatures: Sreehari / Nihad (training only) / NOT FROZEN
```

### Template 15 — Calibration Record

**Who/when:** Sreehari opens before every baseline calibration; operator records events, and Amith verifies physical configuration.  
**Reviewer/sign:** Nihad; locked calibration requires configuration/criteria sign-off.  
**Storage/name:** `05_Test_Protocols_and_Data/Calibration/CAL-YYYYMMDD-###__CFG-###.md`.

```yaml
calibration_id/session/run/date/time/operator:
purpose: sensor sanity|normal baseline|post-remount|regression
protocol/revision/predeclared acceptance:
complete_CFG/component/tool IDs:
physical normal ground truth/warmup/environment:
sensor ID/register readback/range/ODR/SPI:
window/count/duration/data integrity:
raw file/hash:
calculation script/commit/PARAM candidate:
statistics: per-axis means/RMS/distribution/robust statistics WITH units
threshold/persistence derivation rule and candidate values:
saturation/drop/invalidity:
comparison with prior CAL and allowed bounds:
outcome: ACCEPTED|REJECTED|EXPLORATORY|PENDING
reason/limitations/next action:
held_out_data_used: MUST BE NO for derivation
prepared/reviewed/hardware/observer signatures:
```

**SYNTHETIC TRAINING EXAMPLE—NOT PROJECT EVIDENCE:**

```yaml
calibration_id/session/run/date/time/operator: CAL-TRAINING-001 / NONE / NONE / 2026-08-09 / NOT RUN / Sreeprada
purpose: Template practice
protocol/revision/predeclared acceptance: NONE
complete_CFG/component/tool IDs: NONE
physical normal ground truth/warmup/environment: NO HARDWARE
sensor ID/register readback/range/ODR/SPI: NOT MEASURED
window/count/duration/data integrity: NOT MEASURED
raw file/hash: NONE
calculation script/commit/PARAM candidate: NONE
statistics: NOT MEASURED
threshold/persistence derivation rule and candidate values: NOT DERIVED
saturation/drop/invalidity: NOT MEASURED
comparison with prior CAL and allowed bounds: NONE
outcome: REJECTED FOR ENGINEERING USE—TRAINING ONLY
reason/limitations/next action: No experiment / use blank form later
held_out_data_used: NO DATA
prepared/reviewed/hardware/observer signatures: Sreehari / Nihad (training only) / Amith / Sreeprada
```

### Template 16 — Error/Failure/Incident Register

**Who/when:** The first person who notices the event opens it immediately; safety events are reported/stopped before documentation continues.  
**Reviewer/sign:** Nihad for integration; Amith for safety/hardware; Sreehari for firmware/data. Safety incident closure needs two-person review.  
**Storage/name:** `05_Test_Protocols_and_Data/Failed_Experiments/ERR-###__slug__YYYYMMDD-HHMM.md`; safety copies/links also under `03_Hardware_and_CAD/Safety_Inspections/`.

```yaml
error_id/category/severity/status: observation|data|firmware|hardware|safety | OPEN|CONTAINED|CLOSED|ACCEPTED LIMITATION
detected_date/time/timezone/by/people_present:
activity/STAGE/SESSION/RUN/TEST/CFG:
exact_problem/symptoms:
expected_behavior:
actual_behavior_and_timeline:
immediate_safety_stop/containment:
raw/log/photo/video/file/hash links:
configuration and recent changes:
impact: people/equipment/data/validity/schedule/claim
first_hypothesis (not fact):
diagnostic_test proposed/predeclared criterion:
diagnostic outcome/negative results:
root_cause_status: CONFIRMED|PROBABLE|UNKNOWN and evidence
linked_CA/DEC/RISK:
affected runs/datasets/releases/quarantine:
reporting/faculty notification if applicable:
closure criterion/actual closure evidence:
prepared/reviewed/observer signatures/addenda:
```

**SYNTHETIC TRAINING EXAMPLE—NOT PROJECT EVIDENCE:**

```yaml
error_id/category/severity/status: ERR-TRAINING-001 / documentation / low / CLOSED
detected_date/time/timezone/by/people_present: 2026-08-09 12:00 IST / Archa / Sreeprada
activity/STAGE/SESSION/RUN/TEST/CFG: Template training / NONE
exact_problem/symptoms: Training form initially omitted timezone
expected_behavior: Every timestamp includes timezone
actual_behavior_and_timeline: Omission noticed before any real record
immediate_safety_stop/containment: No safety issue; training file marked synthetic
raw/log/photo/video/file/hash links: NONE
configuration and recent changes: NONE
impact: Training clarity only
first_hypothesis (not fact): Field was overlooked
diagnostic_test proposed/predeclared criterion: Review blank template contains timezone
diagnostic outcome/negative results: Blank template contains timezone; no negative result
root_cause_status: CONFIRMED—training omission
linked_CA/DEC/RISK: CA-TRAINING-001
affected runs/datasets/releases/quarantine: NONE
reporting/faculty notification if applicable: NOT APPLICABLE
closure criterion/actual closure evidence: Template field present / observed in blank form
prepared/reviewed/observer signatures/addenda: Archa / Nihad (training only) / Sreeprada
```

### Template 17 — Repair/Corrective-Action Register

**Who/when:** Assigned technical owner creates before repair/change and closes only after regression.  
**Reviewer/sign:** Nihad; Amith signs hardware/safety repair, Sreehari firmware/data repair; observer records before/after.  
**Storage/name:** `CA-###__ERR-###__slug__YYYYMMDD.md` beside linked failure and relevant hardware/firmware folder.

```yaml
corrective_action_id/status/linked_ERR_RISK:
owner/reviewer/observer/dates:
containment already applied:
confirmed/probable cause:
options considered/risks:
selected action and approval DEC:
power_off/safety prerequisites:
exact repair/change steps:
parts/tools/versions/IDs added_removed:
before/after photos/configuration IDs:
verification/regression protocol and predeclared criteria:
actual TEST/RUN evidence/outcome:
negative/unresolved effects:
affected documents/datasets/releases:
rollback/reopen trigger:
closure decision/signatures:
```

**SYNTHETIC TRAINING EXAMPLE—NOT PROJECT EVIDENCE:**

```yaml
corrective_action_id/status/linked_ERR_RISK: CA-TRAINING-001 / CLOSED / ERR-TRAINING-001
owner/reviewer/observer/dates: Archa / Nihad / Sreeprada / 2026-08-09
containment already applied: Training file labeled synthetic
confirmed/probable cause: Timezone field overlooked in practice
options considered/risks: Add field; no engineering risk
selected action and approval DEC: Add timezone to blank template; training approval
power_off/safety prerequisites: NOT APPLICABLE
exact repair/change steps: Confirm blank form contains timezone
parts/tools/versions/IDs added_removed: NONE
before/after photos/configuration IDs: NONE
verification/regression protocol and predeclared criteria: Visual form review / timezone present
actual TEST/RUN evidence/outcome: No experiment; blank form reviewed
negative/unresolved effects: NONE
affected documents/datasets/releases: Training form only
rollback/reopen trigger: Reopen if real form lacks timezone
closure decision/signatures: Closed for training / Archa and Nihad
```

### Template 18 — Successful Milestone Register

**Who/when:** Stage owner proposes after evidence exists; never before the gate.  
**Reviewer/sign:** Nihad plus relevant technical reviewer; Archa indexes.  
**Storage/name:** `01_Selected_Project/CURRENT/MILESTONE-###__slug__YYYYMMDD.md`.

```yaml
milestone_id/title/date/stage:
predeclared objective/exit criteria/source:
owner/reviewer/backup/observer:
configuration/release/protocol IDs:
evidence: TEST/RUN/DATASET/PHOTO/VIDEO/files/hashes
criteria-by-criterion actual disposition:
failures/limitations still open:
reproducibility by backup:
claims permitted/claims not permitted:
next stage/actions:
approval/signatures:
```

**SYNTHETIC TRAINING EXAMPLE—NOT PROJECT EVIDENCE:**

```yaml
milestone_id/title/date/stage: MILESTONE-TRAINING-001 / Logbook orientation complete / 2026-08-09 / training
predeclared objective/exit criteria/source: Learn forms / identify synthetic warning
owner/reviewer/backup/observer: Archa / Nihad / Sreeprada / Sreeprada
configuration/release/protocol IDs: NONE
evidence: This synthetic entry only; no hardware/data
criteria-by-criterion actual disposition: Training warning identified
failures/limitations still open: This is not a project milestone
reproducibility by backup: Sreeprada located warning
claims permitted/claims not permitted: May say training form reviewed / may not claim engineering success
next stage/actions: Use blank templates for real work
approval/signatures: Archa / Nihad (training only)
```

### Template 19 — Engineering Decision Log

**Who/when:** Decision owner opens before implementation when architecture, configuration, safety, criteria, schedule or interpretation changes.  
**Reviewer/sign:** Nihad controls register; affected owners and one independent reviewer sign.  
**Storage/name:** `01_Selected_Project/Authority_and_Decisions/DEC-###__slug__YYYYMMDD.md`.

```yaml
decision_id/status/date/owner:
decision_question/deadline:
authority/requirement/constraint:
facts_and_sources_with_access_dates:
unknowns/assumptions:
options_considered:
criteria/tradeoffs/safety/budget/schedule:
decision_selected:
rationale:
effective_configuration/date:
artifacts/IDs changed and gates to repeat:
risks/limitations/reversibility/rollback:
dissent/minority view:
review/approval signatures:
supersedes/is_superseded_by:
```

**SYNTHETIC TRAINING EXAMPLE—NOT PROJECT EVIDENCE:**

```yaml
decision_id/status/date/owner: DEC-TRAINING-001 / TRAINING / 2026-08-09 / Nihad
decision_question/deadline: How to label examples? / during orientation
authority/requirement/constraint: Do not confuse examples with results
facts_and_sources_with_access_dates: Governing instruction / attached source
unknowns/assumptions: NONE
options_considered: Unlabeled example; clearly synthetic example
criteria/tradeoffs/safety/budget/schedule: Evidence clarity; no hardware effect
decision_selected: Mark every example SYNTHETIC TRAINING EXAMPLE—NOT PROJECT EVIDENCE
rationale: Prevent accidental claim
effective_configuration/date: Documentation only / 2026-08-09
artifacts/IDs changed and gates to repeat: Logbook examples / no gate
risks/limitations/reversibility/rollback: Readers must still delete synthetic values
dissent/minority view: NONE
review/approval signatures: Nihad / Archa (training only)
supersedes/is_superseded_by: NONE
```

### Template 20 — Risk Register

**Who/when:** Any member may raise; Nihad maintains weekly and before each gate.  
**Reviewer/sign:** Named risk owner; Amith signs safety risks, Sreehari data/firmware risks.  
**Storage/name:** `01_Selected_Project/CURRENT/RISK_MASTER.csv` plus `RISK-###__slug__YYYYMMDD.md`.

```yaml
risk_id/title/category/status/raised_by/date:
cause/event/consequence:
affected_people/equipment/data/schedule/claim:
likelihood_scale/current_score:
impact_scale/current_score:
priority/matrix_method:
existing_controls:
preventive_actions: action/owner/due/evidence
contingency/trigger/stop rule:
residual likelihood/impact after verified control:
linked_SAFE_ERR_CA_DEC_TEST:
review_dates/history:
closure/acceptance rationale and approver:
```

**SYNTHETIC TRAINING EXAMPLE—NOT PROJECT EVIDENCE:**

```yaml
risk_id/title/category/status/raised_by/date: RISK-TRAINING-001 / Synthetic values copied / evidence / OPEN / Archa / 2026-08-09
cause/event/consequence: User copies example values / false project record
affected_people/equipment/data/schedule/claim: Evidence credibility
likelihood_scale/current_score: Training scale 1-5 / 2
impact_scale/current_score: Training scale 1-5 / 4
priority/matrix_method: 8 / illustrative only
existing_controls: Bold synthetic warning
preventive_actions: Delete example block when copying / all / before use / review record
contingency/trigger/stop rule: Quarantine any record containing TRAINING in formal data
residual likelihood/impact after verified control: NOT MEASURED
linked_SAFE_ERR_CA_DEC_TEST: DEC-TRAINING-001
review_dates/history: 2026-08-09 training review
closure/acceptance rationale and approver: Keep open through orientation / Nihad
```

### Template 21 — Safety Inspection Log

**Who/when:** Amith leads before every motor run and after any hardware/fixture change; a Lab Assistant reads/records checklist.  
**Reviewer/sign:** Second technical person; formal rig gate by Nihad. Anyone can stop work.  
**Storage/name:** `03_Hardware_and_CAD/Safety_Inspections/SAFE-YYYYMMDD-###__RIG-###__RUN-###.md`.

```yaml
safety_id/date/time/location/RIG/MOUNT/HW/RUN_or_session:
inspector/reviewer/observer/people_in_area:
motor_power_disconnected_and_shaft_stopped_during_inspection:
low_voltage_enclosed_supply/label/polarity:
logic_motor_power_separation:
base restraint/motor clamp/fastener marks:
eccentric positive retention/mass/hub/fasteners:
guard attached/full envelope/clearance:
sensor mount/cable strain relief:
switch/emergency_disconnect/fuse/current_limit:
wiring insulation/connectors/no damage:
area clear/no loose objects/hair/clothing/lanyards/cables:
eye protection/PPE:
temperature/noise/history concerns:
stop_conditions verbally confirmed:
result: PASS FOR SPECIFIED RUN|FAIL—DO NOT ENERGIZE
failed_item/ERR/CA/reinspection required:
post_run inspection/result:
signatures:
```

**SYNTHETIC TRAINING EXAMPLE—NOT PROJECT EVIDENCE:**

```yaml
safety_id/date/time/location/RIG/MOUNT/HW/RUN_or_session: SAFE-TRAINING-001 / 2026-08-09 / 12:30 / classroom / NONE
inspector/reviewer/observer/people_in_area: Amith / Nihad / Sreeprada / training group
motor_power_disconnected_and_shaft_stopped_during_inspection: NO MOTOR PRESENT
low_voltage_enclosed_supply/label/polarity: NOT PRESENT
logic_motor_power_separation: Stated as rule; not inspected
base restraint/motor clamp/fastener marks: NOT PRESENT
eccentric positive retention/mass/hub/fasteners: NOT PRESENT
guard attached/full envelope/clearance: NOT PRESENT
sensor mount/cable strain relief: NOT PRESENT
switch/emergency_disconnect/fuse/current_limit: NOT PRESENT
wiring insulation/connectors/no damage: NOT PRESENT
area clear/no loose objects/hair/clothing/lanyards/cables: Classroom training only
eye protection/PPE: NOT REQUIRED—no operation
temperature/noise/history concerns: NONE
stop_conditions verbally confirmed: YES, as training
result: FAIL—DO NOT ENERGIZE (no rig exists)
failed_item/ERR/CA/reinspection required: Complete real inspection before future run
post_run inspection/result: NO RUN
signatures: Amith / Nihad (training only) / Sreeprada
```

### Template 22 — Photo/Video Evidence Index

**Who/when:** Photographer (usually Sreeprada for lab or Archa for documents/demo) registers immediately after capture and before editing.  
**Reviewer/sign:** Relevant technical owner verifies subject/configuration; Archa controls public/private selection.  
**Storage/name:** `06_Reports_and_Demonstration/Evidence_Index/MEDIA_MASTER.csv`; files follow `PHOTO/VIDEO` naming rule.

```yaml
media_id/type/original_filename/new_filename:
capture_date/time/timezone/device/operator:
people_present/consent_or_institutional_rule:
subject/purpose/view/direction:
linked_COMP/HW/PIN/MOUNT/RIG/CFG/SESSION/RUN/TEST/ERR:
what the image does and does_not prove:
original_path/size/dimensions/duration/SHA-256:
editing/crop/redaction history/derivative hash:
personal/confidential information/redaction:
caption/source/credit:
public_release_status/reviewer:
storage/backup:
```

**SYNTHETIC TRAINING EXAMPLE—NOT PROJECT EVIDENCE:**

```yaml
media_id/type/original_filename/new_filename: PHOTO-TRAINING-001 / no file / NONE / NONE
capture_date/time/timezone/device/operator: NOT CAPTURED / Archa
people_present/consent_or_institutional_rule: NONE
subject/purpose/view/direction: Demonstrate an empty index entry
linked_COMP/HW/PIN/MOUNT/RIG/CFG/SESSION/RUN/TEST/ERR: NONE
what the image does and does_not prove: No image; proves nothing
original_path/size/dimensions/duration/SHA-256: NONE
editing/crop/redaction history/derivative hash: NONE
personal/confidential information/redaction: NONE
caption/source/credit: Synthetic placeholder
public_release_status/reviewer: NOT FOR RELEASE / Archa
storage/backup: Training document only
```

### Template 23 — Weekly Review Minutes

**Who/when:** Archa prepares agenda before the weekly review and minutes within 24 hours.  
**Reviewer/sign:** Nihad; every action owner acknowledges; technical claims reviewed by relevant technical member.  
**Storage/name:** `01_Selected_Project/Orientation_and_Minutes/MEET-YYYYMMDD-###__weekly-review.md`.

```yaml
meeting_id/date/start/end/location/chair/minute_taker:
attendees/absences:
previous_actions: item/owner/due/status/evidence
stage/week_objective_and_gate_status:
configuration_current: HW/PIN/MOUNT/RIG/FW/PARAM/SCHEMA/CFG
work_completed_with_evidence IDs:
failures/negative_results/open_ERR:
safety_review/RISK changes:
budget/procurement/delivery status:
data integrity/split/held_out status:
decisions made/pending DEC links:
teacher/faculty communication links:
next_actions: exact task/owner/reviewer/backup/observer/due/deliverable/acceptance
prohibited_scope reminder:
minutes_corrections/approval signatures:
```

**SYNTHETIC TRAINING EXAMPLE—NOT PROJECT EVIDENCE:**

```yaml
meeting_id/date/start/end/location/chair/minute_taker: MEET-TRAINING-001 / 2026-08-09 / 13:00 / 13:10 / classroom / Nihad / Archa
attendees/absences: Five roles discussed; no attendance claim
previous_actions: NONE
stage/week_objective_and_gate_status: Training only / no gate
configuration_current: NONE
work_completed_with_evidence IDs: Reviewed blank template
failures/negative_results/open_ERR: NONE
safety_review/RISK changes: Safety rules read; no hardware
budget/procurement/delivery status: NO PURCHASE
data integrity/split/held_out status: NO DATA
decisions made/pending DEC links: DEC-TRAINING-001
teacher/faculty communication links: NONE
next_actions: Use real attendance and actions / Archa / Nihad / Sreeprada / Sreeprada / after actual meeting / real minutes / factual review
prohibited_scope reminder: No invented event or condition
minutes_corrections/approval signatures: Archa / Nihad (training only)
```

### Template 24 — Teacher/Faculty Communication Log

**Who/when:** Archa records every sent/received instruction, question, meeting or approval promptly; attach original message/minutes where permitted.  
**Reviewer/sign:** Nihad verifies interpretation; affected technical member checks technical content. The teacher's exact words are not paraphrased as conditions without a source.  
**Storage/name:** `01_Selected_Project/Orientation_and_Minutes/COMM-###__slug__YYYYMMDD.md`.

```yaml
communication_id/date/time/timezone/channel:
faculty/person/role/contact_context:
team_participants:
initiated_by/purpose/question:
exact_message_or_minutes_attachment/path/hash:
short_factual_summary:
instruction/approval/condition/status: NONE|REQUESTED|RECEIVED|NEEDS CONFIRMATION
interpretation_vs_direct_quote distinction:
affected_requirement/DEC/protocol/schedule:
actions: owner/reviewer/due/evidence
reply/followup/status:
privacy/publication restrictions:
prepared/reviewed/technical signatures:
```

**SYNTHETIC TRAINING EXAMPLE—NOT PROJECT EVIDENCE:**

```yaml
communication_id/date/time/timezone/channel: COMM-TRAINING-001 / 2026-08-09 / NOT SENT / IST / training form
faculty/person/role/contact_context: NO FACULTY COMMUNICATION
team_participants: Archa training author
initiated_by/purpose/question: NONE / learn fields / NONE
exact_message_or_minutes_attachment/path/hash: NONE
short_factual_summary: This is not a teacher instruction
instruction/approval/condition/status: NONE
interpretation_vs_direct_quote distinction: No quote and no interpretation
affected_requirement/DEC/protocol/schedule: NONE
actions: Do not cite this as communication / all / immediate / training warning
reply/followup/status: NONE
privacy/publication restrictions: Training only
prepared/reviewed/technical signatures: Archa / Nihad (training only) / N-A
```

### Template 25 — Public Disclosure Log

**Who/when:** Archa opens before and updates after any presentation, report upload, poster, repository publication, social post, competition submission or external sharing.  
**Reviewer/sign:** Nihad and affected contributors; technical content reviewed by technical owner.  
**Storage/name:** `FUTURE_RESEARCH_CONFIDENTIAL/Disclosure_Log/DISC-###__slug__YYYYMMDD.md`; public copy may omit confidential details.

```yaml
disclosure_id/status: PROPOSED|APPROVED|MADE|CANCELLED
planned/actual date/time/timezone/location/channel/audience:
discloser/team_participants:
title/purpose/event:
exact materials/version/files/hashes/URLs:
technical content summary:
Level-1 only confirmed:
future/PIRG/confidential content present: MUST BE NO unless separately authorized
measured claims/evidence review:
contributor/credit review:
institutional/teacher approval if required:
actual audience/reach/questions/recording:
post-disclosure archived copy/screenshot:
followup/correction/takedown:
prepared/reviewed/contributor signatures:
```

**SYNTHETIC TRAINING EXAMPLE—NOT PROJECT EVIDENCE:**

```yaml
disclosure_id/status: DISC-TRAINING-001 / CANCELLED
planned/actual date/time/timezone/location/channel/audience: No planned disclosure
discloser/team_participants: NONE
title/purpose/event: Template practice only
exact materials/version/files/hashes/URLs: NONE
technical content summary: NONE
Level-1 only confirmed: NOT APPLICABLE
future/PIRG/confidential content present: NO MATERIAL
measured claims/evidence review: NO CLAIM
contributor/credit review: NOT APPLICABLE
institutional/teacher approval if required: NOT REQUESTED
actual audience/reach/questions/recording: NONE
post-disclosure archived copy/screenshot: NONE
followup/correction/takedown: NONE
prepared/reviewed/contributor signatures: Archa / Nihad (training only) / NONE
```

### Template 26 — Future Research Observation Notebook

**Who/when:** The first person observing a potentially important new technical problem records it immediately and contemporaneously; do not wait for a patent narrative.  
**Reviewer/sign:** Nihad plus every person physically involved verifies chronology; Archa controls disclosure; later hypothesis review does not rewrite the original.  
**Storage/name:** `FUTURE_RESEARCH_CONFIDENTIAL/Observations/OBS-###__short-neutral-title__YYYYMMDD-HHMM.md` with restricted access.

```yaml
observation_id/status/date/time/timezone/location:
author/people_physically_involved/other contributors:
access/confidentiality:
neutral_problem_observed:
activity/stage/complete_configuration IDs:
raw_RUN/DATASET/log/photo/video/file/hash IDs:
what_was_expected:
what_actually_happened (fact only):
exact chronology/operator actions/environment:
first_hypothesis (explicitly unverified):
alternative_hypotheses:
proposed_test_before_execution: variables/controls/criterion/safety/new hardware
test_approval/branch/protocol IDs:
experiment_outcome linked evidence:
negative/contradictory results:
interpretation_limits:
next_action/owner/reviewer/due:
public_disclosure links/status:
corrections/addenda (dated; original unchanged):
prepared/witness/reviewer signatures:
```

**SYNTHETIC TRAINING EXAMPLE—NOT PROJECT EVIDENCE:**

```yaml
observation_id/status/date/time/timezone/location: OBS-TRAINING-001 / TRAINING / 2026-08-09 / 14:00 / IST / classroom
author/people_physically_involved/other contributors: Nihad / Archa / Sreeprada
access/confidentiality: Training example; no invention or confidential result
neutral_problem_observed: Students may confuse a later interpretation with a contemporaneous observation
activity/stage/complete_configuration IDs: Documentation training / NONE
raw_RUN/DATASET/log/photo/video/file/hash IDs: NONE
what_was_expected: Example should distinguish fact and hypothesis
what_actually_happened (fact only): The form visibly separates the fields
exact chronology/operator actions/environment: 14:00 blank form reviewed; no experiment
first_hypothesis (explicitly unverified): Clear fields may reduce retrospective rewriting
alternative_hypotheses: Training alone may be insufficient
proposed_test_before_execution: During real work, audit one observation for timestamps; no hardware
test_approval/branch/protocol IDs: NOT APPROVED/NOT RUN
experiment_outcome linked evidence: NOT RUN
negative/contradictory results: NONE—no test
interpretation_limits: This demonstrates documentation only; it says nothing about PIRG or patentability
next_action/owner/reviewer/due: Preserve original and append corrections / all / Nihad / ongoing
public_disclosure links/status: DISC-TRAINING-001 / no disclosure
corrections/addenda (dated; original unchanged): NONE
prepared/witness/reviewer signatures: Nihad / Archa and Sreeprada / training review
```

## 8. Weekly evidence audit

Archa prepares the index; Nihad signs evidence integrity; technical owners close their links.

- [ ] Every physical item has `COMP` and acceptance status.
- [ ] Every order status matches a real invoice/tracking/receipt or remains planning only.
- [ ] Every wiring, mount, rig, firmware, parameter and schema change has a new or updated identified record.
- [ ] Current `CFG` resolves all constituent IDs.
- [ ] Every run has session, protocol, physical ground truth, complete config, safety link, raw path and hash.
- [ ] Raw files are unmodified; a random sample of hashes verifies against the manifest.
- [ ] Processed outputs record source raw hashes, script commit and parameters.
- [ ] Drops, saturation, resets, disturbances and invalid runs are visible.
- [ ] Failed/negative work remains present and links `ERR/CA`.
- [ ] No random-window leakage; held-out access remains controlled.
- [ ] Faculty conditions are backed by an actual communication record.
- [ ] Public material contains no confidential future-research detail or unsupported claim.
- [ ] Backups are readable, not merely copied; at least one restore/hash check was performed.

## 9. Locked-test evidence bundle

Before opening held-out results, create one manifest containing:

- `TEST`, protocol and criteria hashes;
- exact `CFG`, `HW`, `PIN`, `MOUNT`, `RIG`, `FW` commit/binary hash, `PARAM`, `SCHEMA` and `TOOL` IDs;
- sealed held-out `DATASET` and run/session IDs;
- analysis repository commit, dependency versions and any random seed;
- blank result table and metric definitions;
- declarations that held-out data were not used in tuning;
- safety approval and operator/observer assignments; and
- deviation rule.

After execution, add raw hashes, chronology, deviations, frozen output, metrics with denominators, failures and signatures. Do not change the pre-test portion; append the result portion.

## 10. Final archive manifest minimum

The archive is incomplete unless it contains or securely points to:

1. authority/current-status and architecture decision;
2. final BOM, invoices/reuse records and component acceptances;
3. hardware/wiring/mount/rig/guard revisions and safety evidence;
4. firmware source, commits, release binaries, toolchain/dependencies and hashes;
5. protocols, criteria, parameters/schema and all configuration links;
6. immutable raw data, manifests, processed lineage and failed experiments;
7. analysis scripts, result tables/plots and locked-test deviations;
8. logs, decisions, risks, failures/corrective actions and milestones;
9. photos/videos with original hashes and disclosure status;
10. final report/demo/handover/reproduction record; and
11. separate access-controlled future-research observations/disclosures, if any.

## 11. Why this discipline matters

The log is not paperwork added after engineering; it is how the team knows which physical system, code and data produced a result. It prevents accidental test leakage, unsafe “quick fixes,” configuration ambiguity and memory-based reconstruction. It also preserves real technical chronology for future research without asserting that any idea works or is patentable. If a future hypothesis fails, its negative evidence may reveal a different genuine problem—but only if the original facts were not rewritten.
