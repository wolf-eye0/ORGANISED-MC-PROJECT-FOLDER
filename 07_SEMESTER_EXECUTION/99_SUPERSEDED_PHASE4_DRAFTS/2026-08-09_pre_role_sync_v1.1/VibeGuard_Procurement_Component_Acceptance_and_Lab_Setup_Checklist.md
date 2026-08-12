# VibeGuard Procurement, Component Acceptance and Lab Setup Checklist

**Document status:** Procurement-ready planning baseline, revision 1.0  
**Audience:** Nihad P C, Sreehari K and Amith Krishna Das; Sreeprada K S and Archa Pramod act as Lab Assistants/Technical Observers and recorders  
**Price/specification check:** 9 August 2026, India  
**Truth statement:** Nothing in this document means that an item has been purchased, delivered, accepted or tested. Product pages are dated planning evidence only.

**Current project-state control:** `Project_mC_Final_Selection_and_Phase4_Entry_Memo.md` and `Project_mC_Decision_Register_v1.3.md`. Decision Register v1.2 remains an unchanged historical predecessor.

## 1. Procurement rules

- Target the preferred ₹3,000 project budget and never exceed the ₹5,000 ceiling without a new authorized decision. Shipping, GST, local fabrication and replacements count.
- Reopen every preferred and backup URL on the actual order day. Record time, postcode availability, exact stock, price, GST, shipping, delivery estimate and return deadline in `PROC-###`.
- Match exact manufacturer part number/SKU where specified. A similar photo or “ESP32 board” title is not an equivalent part.
- Inventory and accept usable lab stock before buying duplicates. Reused/donated items still receive `COMP-###` and acceptance records; their purchase cost is ₹0 with source stated, not silently omitted.
- Do not delete safety hardware to reach the preferred budget. If cost must be reduced, reuse a verified breadboard/cable/tools or consolidate shipping.
- Product specifications from generic module/motor sellers are vendor claims. The received part must pass the tests below.
- Only an invoice/order confirmation changes status to `ORDERED`; only receiving/acceptance records change status to `DELIVERED`/`ACCEPTED`.

## 2. Frozen procurement boundary

Required semester hardware remains:

- one permanent ADXL345 three-axis accelerometer breakout;
- one exact ESP32-WROOM-32 DevKit, with an authorized ESP32-S3 DevKit only as fallback;
- SPI wiring;
- common-cathode RGB LED plus resistors;
- USB data/serial cable;
- a separate guarded low-voltage 12 V motor/fan rig with stable base, rigid sensor mount, captive eccentric/equivalent, switch/disconnect and protection.

Do not purchase a microphone, microphone array, permanent second accelerometer, industrial vibration sensor, cloud gateway or PIRG hardware for the semester system.

## 3. Procurement-ready BOM

Prices include GST where the page explicitly says so. `Allowance` means a budget reservation, not a quote. Stock can change after the research date.

| Line | Function and required specification | Qty | Preferred current source, price and availability on 2026-08-09 | Backup/equivalence rule | Acceptance/rejection summary | Spare strategy |
|---:|---|---:|---|---|---|---|
| 1 | **MCU:** genuine Espressif `ESP32-DEVKITC-32E`, ESP32-WROOM-32E, 4 MB, Micro-USB USB-UART | 1 | [Robu exact DevKitC-32E](https://robu.in/product/espressif-esp32-devkitc-esp32-wroom-3-2e-development-board/), **₹1,079**, listed **In Stock** | [Evelta exact MPN](https://evelta.com/esp32-devkitc-32e-esp32-wroom-32e-development-board-4mb-flash-pcb-antenna/), ₹947.54 incl. GST; page shows conflicting orderability text, so confirm cart/stock. ESP32-S3 requires explicit authorization/new pin map. | Exact board/module markings; no damage; USB enumerates; flash/capture; five clean boots; no overheating/reset loop. Reject/quarantine mismatch or unstable board. | No spare initially; replacement source identified. |
| 2 | **Sensor:** ADXL345 breakout exposing 4-wire SPI pins, 3.3 V compatible | 1 | [Robocraze ADXL345](https://robocraze.com/products/adxl-345), **₹249**, 148 listed; seller claims regulator/level shifting | [Probots GY-291 ADXL345](https://probots.co.in/gy-291-adxl345-3-axis-digital-accelerometer-sensor-module.html), ₹199, listed in stock; recheck | Photograph both sides/pins; 3.3 V only; stable SPI `DEVID=0xE5`; register readback; six-orientation plausibility; timing/drop check. Quarantine wrong/intermittent ID. | Buy second only after first acceptance and budget review; it is a spare, not a permanent second sensor. |
| 3 | **Rig motor:** compact 12 V N20 metal gear motor, about 600 RPM, 3 mm D shaft, positive coupling possible | 1 | [Robocraze 600 RPM 12 V N20 with cable](https://robocraze.com/products/600-rpm-12v-n20-dc-metal-gear-motor-with-cable), **₹233**, 62 listed | [Robu N20 12 V 600 RPM](https://robu.in/product/n20-12v-600-rpm-micro-metal-gear-motor/), ₹229 incl. GST, listed in stock | Inspect shaft/leads/gearbox; manual rotation powered-off; current-limited low-voltage start; measure no-load/start behavior at approved voltage; reject severe wobble/noise/heat/current beyond source/protection. | No spare initially; do not substitute contradictory speed listing. |
| 4 | **Motor supply:** enclosed plug-in 12 V DC, 1 A, insulated mains side, 5.5×2.1 mm plug preferred | 1 | [Robocraze 12 V/1 A adapter](https://robocraze.com/products/12v-1a-power-adapter), **₹115**, 72 listed; seller claims OVP/OCP/OTP/short protection | [Robu Pro-range 12 V/1 A adapter](https://robu.in/product/orange-12v-1a-power-adapter-with-5-5-x-2-1mm-dc-plug/), ₹349 incl. GST, listed in stock | Enclosure/label/plug; meter polarity; no-load and motor-load voltage; temperature/smell/noise; reject wrong polarity, exposed mains, damage, unstable voltage or overheating. | One only; lab bench supply is diagnostic fallback, not permanent demo source unless approved. |
| 5 | **Reachable DC switch/disconnect:** SPST with documented DC suitability at the intended voltage and safely above measured motor startup/operating current | 1 | [Evelta/Daier ASW-07D](https://evelta.com/illuminated-toggle-switch-red-spst-2-pin-on-off-asw-07d/), **₹160.48 incl. GST**, 100 listed. Its seller page conflicts between 25 A and 20 A at 12 VDC. **NOT YET APPROVED FOR ORDER — RATING MUST BE RESOLVED.** Do not adopt either value without credible supplier/manufacturer documentation. | [Robocraze mini SPST pack](https://robocraze.com/products/2-pin-mini-on-off-spst-rocker-switch-19-x-13mm), ₹25, 63 listed, but its page gives an AC rating. **NOT YET APPROVED FOR ORDER — RATING MUST BE RESOLVED.** An AC-only rating is not automatically a DC rating. | Documentation must establish intended DC voltage/current duty; then verify continuity, insulation, reachability, contact stability and absence of abnormal heating/drop. Bench tests do not prove certified interruption/rating capability. | Pack/backup only after documented equivalence. |
| 6 | **Fuse holder:** covered holder documented as suitable for the intended low-voltage DC circuit, matching fuse format and wiring current | 1 | [Electronic Spices 12 V inline blade holder](https://electronicspices.com/product/12v-30a-waterproof-power-socket-inline-blade-fuse-holder), **₹39 incl. tax**, buy button shown; retain as a planning example pending exact documentation and matching fuse selection | 5×20 mm covered holder only with documented low-voltage DC suitability and a matching accepted fuse; capture exact rating/price on order day | Verify documented voltage suitability, exact fuse fit, covered live metal, wire gauge/strain relief and contact condition; continuity/load tests supplement but do not establish interruption rating. No bypass. | Buy one extra only after the system is accepted. |
| 7 | **Motor fuse:** candidate only; final format, voltage suitability, current rating and fast/slow/time-delay characteristic follow holder choice and measured startup/operating behavior | 3 | [Probots 1 A 5×20 mm fuse](https://probots.co.in/1a-250vac-fuse-glass-tube-5x20mm.html), **₹6 each**. Its 250 VAC marking alone does not prove appropriate DC interruption performance. **NOT YET APPROVED FOR ORDER — RATING MUST BE RESOLVED.** | Source a fuse matching the selected holder, with documented suitability for the intended low-voltage DC circuit and measured motor behavior. Do not mix glass and blade systems. Budget **₹18** remains planning-only. | Verify format, documented voltage suitability, rating and time-current characteristic before controlled motor testing. If nuisance opening occurs, investigate motor current, fixture, wiring faults and characteristic; never bypass or increase rating merely to stop opening. | Three identical accepted fuses only after selection is resolved. |
| 8 | **DC input connector:** 5.5×2.1 mm female screw terminal or wired jack matching adapter, shrouded and polarity-labeled | 1 | [Robocraze female plug adapter](https://robocraze.com/products/dc-power-female-plug-jack-adapter-connector), **₹19** | Matching panel/wired jack; verify exact dimensions and polarity | Plug fit, polarity, screw retention, pull test, no exposed short risk. | One spare if pack/local stock is low cost. |
| 9 | **Status indicator:** 5 mm common-cathode RGB LED | 1 used | [Robocraze common-cathode pack of 10](https://robocraze.com/products/rgb-led-common-cathode-pack-of-10), **₹30**, 4 packs listed | Equivalent common-cathode LED only after diode/pin identification | Diode-test each channel; verify common cathode; record channel pins and forward voltage; reject wrong common type/dead channel. | Pack provides low-cost spares. |
| 10 | **RGB current limiting:** 220 Ω and 330 Ω, ¼ W or suitable resistor selection; one per channel | ≥3 plus spares | [Robocraze 220 Ω pack](https://robocraze.com/products/220-ohm-resistor-pack-of-10), page search price range ₹9–₹14; reserve **₹30** for 220/330 Ω packs and recheck | Lab resistor stock if measured/labeled | Measure resistance; choose each channel for visible operation and target a conservative few mA from measured LED Vf; every channel must have a resistor. Reject unknown/short. | At least two spares/value. |
| 11 | **Bench prototype:** 830-point solderless breadboard, only for stationary electronics bring-up | 1 | [Robocraze MB102](https://robocraze.com/products/mb102-830-points-solderless-breadboard), **₹64**, 246 listed | Existing accepted lab breadboard | Rail/row continuity and grip test; label split rails. It cannot be final vibration wiring. | Reuse if accepted. |
| 12 | **Bench jumpers:** M-M, M-F and F-F, 20 cm, 40 each | 1 set | [Robocraze 120-piece set](https://robocraze.com/products/jumper-wire-set-m2m-m2f-f2f-40-pcs-each), **₹123**, 122 listed. Record the final resolved URL at order time. | Individual accepted packs; current M-F pack is ₹43 with 237 listed | Sample continuity/wiggle test; correct gender/length; use shortest reliable sensor wires. Not for final rig. | Set contains spares; discard/quarantine intermittent lead. |
| 13 | **USB data cable:** USB-A to Micro-B, known data capable, about 1 m | 1 | [Robocraze ERD UC-252 data/charging cable](https://robocraze.com/products/erd-uc-252-micro-usb-data-charging-cable-1-meter), **₹69** | Existing known data cable; another current data-rated listing | Board enumerates, uploads and captures data; five flex/wiggle checks without disconnect. Reject charge-only/intermittent cable. | Keep one known-good alternate if already available. |
| 14 | **Stable final electronics:** 3×4 inch Vero/stripboard or suitable perfboard | 1 | [Robocraze 3×4 Vero board](https://robocraze.com/products/vero-board-3-x4), **₹28**, 488 listed | [Robu 10×10 cm universal board](https://robu.in/product/10-x-10-cm-universal-pcb-prototype-board-single-sided-2-54mm-hole-pitch/), ₹68; recheck stock | No cracked board/lifted copper; continuity/isolation after solder; strain relief and regression required. | One extra only if layout risk warrants. |
| 15 | **Wiring/termination kit:** red/black insulated wire, heat-shrink, headers/connectors/terminal block, solder | 1 lot | Current pages vary; reserve **₹150 allowance**, but capture every actual line price/quantity before order | Accepted lab stock preferred | Correct wire gauge/insulation, continuity, color/polarity labels, pull test, insulated solder joints. | Small wire/heat-shrink/header spares. |
| 16 | **Mechanical/safety fabrication:** heavy stable base; N20 clamp; rigid sensor bracket; 3 mm set-screw/clamping hub with captive off-axis M3 bolt/washers/nyloc; fasteners; strain relief; full rotating-envelope polycarbonate/robust guard | 1 rig | Local fabrication after received-part dimensions; reserve **₹650 allowance** and obtain dated local/online quote before purchase | Safer guarded fan/equivalent only by decision; imported 3 mm hubs are too costly unless budget permits | Dimension/material/fastener records; powered-off pull/clearance checks; low-energy current-limited pilot; no loosening/contact/base movement; two-person safety sign-off. | Spare nyloc/set screws/washers; no spare loose mass left near rig. |
| 17 | **Shipping/price-change contingency** | 1 | **₹300 allowance**, not an actual charge | Consolidate accepted exact parts; never remove safety items | Replace allowance with invoices; investigate >10% variance. | Not a component. |

**Important link correction:** Some storefronts change product slugs. On the order day, save the final resolved URL and screenshot. If the mixed-jumper URL in Line 12 does not resolve, use the current product page titled “Jumper Wire Set - M2M, M2F, F2F (40 pcs each)” and do not infer equivalence from the slug.

### Controlled DC switch/disconnect and fuse rule

**Switch/disconnect:** The selected switch or disconnect must have manufacturer or credible supplier documentation explicitly supporting the intended DC voltage and a current safely above the measured motor operating and startup requirement. An AC-only rating is not automatically accepted as a DC rating. If a retailer page contains conflicting DC ratings, do not use the highest value: mark the listing unresolved, prefer another clearly documented component, or obtain manufacturer documentation before acceptance. Continuity and short-duration bench load tests are useful receiving checks but do not prove certified electrical interruption or rating capability.

**Fuse and holder:** The fuse and holder must be suitable for the intended low-voltage DC circuit. Fuse format, voltage suitability, current rating and fast/slow/time-delay characteristic must match the holder and measured motor startup/operating behavior. A 250 VAC marking alone does not prove appropriate DC interruption performance. Never bypass a fuse. Do not increase its rating merely because nuisance opening occurs; first investigate motor current, fixture condition, wiring faults and the required time-current characteristic.

## 4. Budget scenarios

The arithmetic below is a planning estimate from the table, not an invoice.

| Scenario | Planning total | Interpretation |
|---|---:|---|
| All listed new items plus local allowances and ₹300 shipping contingency | **₹3,356.48** | Below ₹5,000; about ₹356 above the preferred target. Actual line 7/15/16/shipping must replace allowances/estimates. |
| Reuse accepted breadboard, jumper set, USB cable, Vero board and wiring kit | **₹2,922.48** | Meets preferred ₹3,000 target while retaining safety items. |
| All new plus one accepted spare ADXL345 after first-unit gate | **₹3,605.48** | Still below ceiling; spare is optional and not a second permanent sensor. |
| Authorized S3 fallback at current Evelta price, all else new, no spare | **₹4,914.78** | Only ₹85.22 below ceiling before any unexpected shipping/price change; therefore full re-cost/approval is mandatory. |

The current exact S3 contingency is [Evelta `ESP32-S3-DEVKITC-1-N32R8V`](https://evelta.com/esp32-s3-devkitc-1-wi-fi-bluetooth-le-development-board/) at ₹2,637.30 including GST with “shipped in 24 hours” but ambiguous orderability text. It is not the default BOM and its pin map/software target must be rebuilt from official S3 documentation.

## 5. Order sequence

### Gate A — Before any order

- [ ] Nihad confirms architecture and budget boundary.
- [ ] Amith completes lab-stock inventory with IDs and condition.
- [ ] Sreehari confirms preferred board/sensor interfaces against official documentation.
- [ ] Sreeprada checks every BOM row has quantity, purpose, current preferred/backup, test and spare strategy.
- [ ] Archa stores dated source captures and prepares the procurement register.
- [ ] Delivery postcode, GST invoice details, payment authority and receiving address are confirmed.
- [ ] Mechanical allowance has at least a rough dimension-dependent quote or is explicitly held until parts arrive.

### Order group 1 — Critical electronics

1. Exact `ESP32-DEVKITC-32E`.
2. One ADXL345 breakout.
3. Data cable only if no accepted lab cable exists.

Do not order an S3 substitute automatically if Group 1 is unavailable. Record stock failure and obtain authorization.

### Order group 2 — Rig drive and protection

1. 12 V 600 RPM N20 motor.
2. Enclosed 12 V/1 A adapter.
3. DC-rated switch/disconnect.
4. Matching covered fuse holder and candidate fuse set.
5. Matching DC jack.

The holder and fuse must be one compatible system. Do not order a blade holder with only glass fuses.

### Order group 3 — Prototyping/status

1. Common-cathode RGB pack and measured resistors.
2. Breadboard/jumpers if not reusable.
3. Perfboard, wire, heat-shrink, headers/terminal blocks and solder.

### Order group 4 — Dimension-dependent mechanical parts

Wait until motor/sensor dimensions and mounting holes are recorded. Then select base, clamp, sensor bracket, 3 mm positive-retention hub, captive mass fasteners and guard. This prevents buying a coupling that does not fit the received D shaft.

## 6. Receiving and quarantine workflow

1. Preserve packaging and return label until acceptance closes.
2. Photograph sealed package, contents and both sides/markings of every item; mask personal data in any public copy.
3. Assign `COMP-###` and link invoice/order/batch before powered testing.
4. Compare exact ordered title/MPN/SKU to received marking. Record discrepancies; do not “correct” the order record.
5. Mark one of: `ACCEPTED`, `CONDITIONAL`, `QUARANTINED`, `REJECTED`.
6. Physically separate quarantined/rejected parts. Do not place them in the general component bin.
7. Complete return/replacement before the seller window closes; retain seller communication.
8. A visually accepted MCU/sensor remains conditional until powered identity/functional tests pass.

## 7. Component acceptance procedures

### 7.1 Exact ESP32-DevKitC-32E

**Required:** Board, known data cable, ESD-aware bench, camera, Arduino IDE/Espressif core, serial capture.

- [ ] Markings show Espressif DevKitC and ESP32-WROOM-32E/expected module; record board revision and connector.
- [ ] No bent pins, solder bridges, damaged antenna area, cracked connector or loose component.
- [ ] With no external wiring, power through Micro-USB only. The [official DevKitC guide](https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32/esp32-devkitc/user_guide.html) states USB, 5 V/GND header and 3.3 V/GND header options are mutually exclusive.
- [ ] Board enumerates; correct target selected; minimal identity/counter sketch uploads.
- [ ] New capture file contains boot identity and monotonic counter.
- [ ] Five reset/power-cycle boots complete without unexplained reset loop, brownout or abnormal heat.
- [ ] Backup person reproduces upload/capture from written steps.

**Accept:** Exact identity plus reproducible flash/serial/five boots.  
**Reject/quarantine:** Marking/SKU mismatch, physical damage, no enumeration after known-good cable/computer, repeated unexplained reset/heat, flash failure on two verified setups.

### 7.2 ADXL345 breakout

**Official facts:** Bare ADXL345 supply 2.0–3.6 V; 3-/4-wire SPI; `DEVID` register `0x00` returns `0xE5`; bandwidth is ODR/2. At 800 Hz the official data sheet recommends SPI ≥400 kHz; at 1600/3200 Hz it recommends SPI ≥2 MHz. [Analog Devices data sheet](https://www.analog.com/media/en/technical-documentation/data-sheets/ADXL345.PDF).

- [ ] Photograph both sides, silkscreen, regulator/level-shifter layout and pins.
- [ ] Required pins exposed: VCC, GND, SCLK, SDI/MOSI, SDO/MISO and CS; INT1 preferred.
- [ ] Power from ESP32 3.3 V, not 5 V, despite seller claims of regulator support.
- [ ] With power removed, inspect continuity/short risk and verify proposed pinout against exact board documentation.
- [ ] Read `0x00` repeatedly at conservative SPI; actual byte must be stable `0xE5`.
- [ ] Write/read back `BW_RATE 0x2C`, `POWER_CTL 0x2D`, `DATA_FORMAT 0x31` and used FIFO/interrupt registers.
- [ ] Initial **PROPOSED** setting: full-resolution ±4 g, 800 Hz, 256 samples; final values are frozen after pilot.
- [ ] Six stationary orientations produce plausible gravity-axis sign/magnitude changes; record raw, do not impose invented numeric noise limits.
- [ ] Run declared stationary timing capture; log achieved rate, sequence, FIFO/overrun, saturation and drops.

**Accept:** Stable `0xE5`, readback, plausible axes and zero unexplained acquisition-integrity event in acceptance capture.  
**Reject/quarantine:** Wrong/intermittent ID after wiring isolation, missing SPI pins, damage/heat, implausible fixed/saturated data or repeatable failures across known-good wiring/board.

### 7.3 N20 motor

- [ ] Photograph label/body/leads/gearbox/3 mm D shaft; measure shaft and body.
- [ ] With power disconnected, rotate shaft gently; record binding, excessive play or damage.
- [ ] Clamp motor before any power. No coupling/eccentric for electrical acceptance.
- [ ] Use current-limited bench source where available. Begin at low voltage/brief pulse; increase in controlled steps toward rated 12 V only if stable.
- [ ] Measure voltage, no-load current, startup peak if equipment supports it, speed proxy/tachometer if available, sound, visible shaft wobble and temperature versus time.
- [ ] Freeze allowable current/temperature/run duration only after measured pilot and source/fuse review.

**Accept:** Starts/restarts consistently, current remains within approved source/protection, shaft has no dangerous wobble, no harsh gearbox noise/rapid heating/damaged insulation.  
**Reject/quarantine:** Binding, intermittent lead, excessive current/heat, severe wobble/noise or physical damage. Do not fit eccentric to “see if it improves.”

### 7.4 12 V adapter, DC jack, switch and fuse system

- [ ] Adapter enclosure/cable/plug undamaged; label states 12 V DC and adequate current; no exposed mains access.
- [ ] Meter identifies center polarity and no-load voltage. Label connector polarity on rig.
- [ ] **PROPOSED acceptance band:** 12 V ±10% at no load and during approved no-eccentric motor load, unless manufacturer specification is tighter. Record actual; do not adjust inside sealed adapter.
- [ ] Verify switch continuity/open circuit, mounted reachability and insulation.
- [ ] Before order/acceptance, obtain manufacturer or credible supplier documentation for switch operation at the intended DC voltage and above measured startup/operating current. An AC-only or internally conflicting listing remains `NOT YET APPROVED FOR ORDER — RATING MUST BE RESOLVED`.
- [ ] Verify fuse holder/fuse format compatibility, documented low-voltage DC suitability, current rating, required fast/slow/time-delay characteristic, secure cover and wire strain relief. A 250 VAC marking alone is insufficient proof of DC interruption suitability.
- [ ] Motor circuit order: adapter positive → disconnect/switch → fuse → motor; return to adapter negative. Place protection where a short downstream is interrupted.
- [ ] Run a controlled load; record voltage/current and inspect connector/switch/holder for heat, arcing, looseness or drop. Treat this as a functional check, not proof of a certified DC rating or interruption capability.
- [ ] Emergency disconnect stops motor without reaching into guard.

**Accept:** Correct polarity/stable voltage; documented DC-suitable switch/disconnect; compatible, documented DC-suitable fuse and holder with appropriate format/rating/characteristic; reachable disconnect; and no damage, heat or contact instability.  
**Reject/quarantine:** Wrong polarity/plug, exposed mains, unstable/out-of-band voltage, arcing/heat, ambiguous or AC-only switch rating, conflicting unresolved DC claims, incompatible or inadequately documented fuse/holder, reliance on bench testing as rating proof, or any bypass.

### 7.5 RGB LED and resistors

- [ ] Diode-test and map pins; verify common cathode rather than common anode.
- [ ] Measure/record forward voltage for red/green/blue at meter-test current.
- [ ] Measure each resistor. Select one per channel to keep current conservative (target a few mA) using `I=(3.3−Vf)/R`; actual GPIO high and brightness are checked on the received LED.
- [ ] Wire common cathode to logic ground; each anode through its own resistor to GPIO.
- [ ] Lamp test: green, blue, red separately and off; no channel stuck or incorrectly mapped.

**Accept:** Correct common type, all channels visible/stable with resistors and firmware mapping recorded.  
**Reject:** Dead/intermittent/wrong-common LED or omitted resistor.

### 7.6 Breadboard, jumpers, USB cable and perfboard

- [ ] Map split breadboard rails; check sample row/rail continuity and absence of adjacent shorts.
- [ ] Continuity/wiggle-test a sample of each jumper type; quarantine intermittent leads.
- [ ] USB cable must enumerate, flash and log during five gentle flex checks; reject charge-only cable.
- [ ] Perfboard has no cracks/lifted copper; after soldering, inspect magnified joints, polarity, continuity and isolation; clean residue as appropriate.
- [ ] Breadboard/jumpers are bench-only. Final vibration hardware uses stable soldered/connectorized wiring plus strain relief and a regression test.

### 7.7 Base, mount, captive eccentric and guard

- [ ] Base dimensions/material/mass and bench restraint recorded; no rocking/sliding.
- [ ] Motor clamp uses mechanical fasteners; wiring has strain relief.
- [ ] Sensor bracket fixes orientation rigidly using bolts/clamp or approved rigid attachment; no foam/double-sided tape/loose breadboard.
- [ ] Eccentric uses 3 mm set-screw/clamping/keyed hub and captive off-axis bolt/washers with nyloc/locking method. Mass and radius are measured and identified.
- [ ] Tape, hot glue, binder clips, loose washers and press-fit-only masses are rejected.
- [ ] Robust guard encloses the full rotating envelope and remains fastened; verify shaft/fixture clearance through manual rotation with power disconnected.
- [ ] Two-person powered low-energy pilot, eye protection, current limiting and reachable disconnect.
- [ ] Stop immediately for heating, new harsh noise, looseness, base movement, guard contact, smell/smoke or wiring damage.

**Accept:** Dimensioned, guarded, stable and repeatable configuration passes declared low-energy pilot and post-run inspection.  
**Reject:** Any exposed/unretained rotating part, live-adjustment requirement, unstable base, guard contact or configuration that cannot be repeated safely.

## 8. Proposed preferred-board pin map gate

Do not freeze this table until the exact `ESP32-DEVKITC-32E` is received/accepted and the [official header guide](https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32/esp32-devkitc/user_guide.html) is checked.

| Signal | Proposed GPIO | Acceptance action |
|---|---:|---|
| ADXL SCLK | 18 | Verify header label; continuity; SPI clock readback. |
| ADXL MOSI/SDI | 23 | Verify direction and register write/readback. |
| ADXL MISO/SDO | 19 | Verify `0xE5`/data reads. |
| ADXL CS | 21 | Ordinary GPIO selected to avoid ESP32 strapping-pin dependency. |
| ADXL INT1 | 4 | Optional DATA_READY; input behavior measured before enabling. |
| RGB green | 25 | Resistor/channel lamp test. |
| RGB blue | 26 | Resistor/channel lamp test. |
| RGB red | 27 | Resistor/channel lamp test. |

The ESP32's GPIO0, GPIO2, GPIO5, GPIO12 and GPIO15 are strapping pins; GPIO6–11 are normally connected to module flash and must not be used. [Espressif GPIO guidance](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/peripherals/gpio.html). A fallback S3 board requires a new `PIN-###`; never copy this map.

## 9. Required lab equipment and readiness

Equipment is not automatically a project purchase. Record `AVAILABLE/ACCEPTED`, `AVAILABLE/NEEDS CHECK`, `NOT AVAILABLE` and custodian/location before ordering anything.

| Equipment | Required/optional | Readiness/acceptance check | Owner |
|---|---|---|---|
| Computer with USB and storage | Required; second computer strongly preferred | Arduino/Git/capture installed; port access; free space; backup/restore test | Sreehari/Archa |
| Calibrated/checked digital multimeter | Required | Known source/resistor sanity check; leads/fuse intact; equipment ID/status recorded | Amith |
| Current-limited bench DC supply | Strongly preferred for first motor bring-up | Output/polarity/current-limit verified; local lab instructions followed | Amith |
| Soldering station, stand, solder, extraction/ventilation | Required for final stable wiring | Tip/earth/stand condition; trained operator; eye/heat safety | Amith |
| Wire stripper/cutter, screwdrivers, hex keys, spanners | Required | Correct size, undamaged, controlled storage | Amith |
| Caliper/ruler and mass scale | Required for repeatable fixture/mount | Zero/reference check; resolution/ID recorded | Amith/Sreeprada |
| Clamps/vice/drill/guard fabrication tools | Required or fabrication service | Safe tool access and trained operator; local rules | Amith |
| Eye protection | Required for rig pilots/runs | Undamaged, fits each person in operating area | Amith |
| Camera/phone and stable timestamp | Required | Storage/timezone set; original files retained; privacy procedure | Archa/Sreeprada |
| Tachometer or stroboscope | Optional but useful | Known reference/check; safe non-contact use outside guard | Amith |
| Oscilloscope/logic analyzer | Optional diagnostic | Probe condition/reference test; not required for minimum success | Sreehari |
| Thermometer/IR thermometer | Useful | Emissivity/limitations noted; reference check | Amith |
| Fire-safe normal lab provisions/emergency contact | Required under local lab rules | Location/access briefing; do not invent or replace institutional rules | Nihad/Amith |

## 10. Lab layout checklist

- [ ] Stable bench with rig zone physically separated from electronics/computer zone.
- [ ] Motor base is restrained; guard faces away from people and fragile equipment.
- [ ] Emergency disconnect is reachable without crossing the rotating envelope.
- [ ] Logic USB and motor 12 V paths are color/label separated.
- [ ] Cable routes cannot enter guard or pull sensor/motor; strain relief installed.
- [ ] No loose screws, washers, tools or test objects near the rig.
- [ ] PPE location and stop signal are known to everyone.
- [ ] Quarantine bin, component labels and return packaging area exist.
- [ ] Raw capture destination has adequate space, new-file protection and backup.
- [ ] Sreeprada/Archa observer position is outside the guard/hazard zone.

## 11. First-week setup procedure

### Day 0 — Governance and no-power readiness

1. All five read the Primer safety/boundaries.
2. Create folder/ID system and component/procurement registers.
3. Inventory lab tools/stock; record unknowns rather than assumptions.
4. Install Arduino IDE, Espressif board package, Git and serial capture; record versions as pending until smoke test.
5. Review current supplier pages/BOM and approve budget/order sequence.

**Exit:** 5/5 acknowledgements, complete pending BOM, no unassigned critical role.  
**Do not:** order unauthorized substitute, power a motor, wire a sensor or set thresholds.

### Day 1 — Orders/source evidence

1. Recheck stock/price/postcode/GST/shipping/return window.
2. Save dated captures; obtain technical/budget approval.
3. Place authorized critical orders only; save real invoice/confirmation if placed.
4. Start delivery tracker and local mechanical quote requests.

**Exit:** Every ordered line has `PROC`; actual/projected cost separated.  
**Do not:** mark product page as purchase or buy dimension-dependent hub blindly.

### Day 2 — Toolchain without external wiring

If the exact board is received/accepted visually:

1. Use known data cable; Micro-USB only.
2. Upload identity/counter sketch; capture log; reset five times.
3. Freeze tool versions after backup reproduction.

If board has not arrived, build deterministic host-side parser/RMS test scaffolding with synthetic vectors clearly separated from measurements.

**Exit:** Reproducible MCU smoke test or documented tool readiness, never an invented pass.

### Day 3 — Sensor bench preparation

1. Accept/photograph/ID sensor and board.
2. Check exact board official pinout; draft `PIN-001`.
3. With USB disconnected, wire short SPI paths; two-person check and photograph.
4. Power logic only; read `0xE5`; read/write/readback registers.

**Exit:** Stable identity/readback or quarantined fault record.  
**Do not:** mount on motor, use I²C, power 5 V or infer final ODR achievement.

### Day 4 — Stationary acquisition gate

1. Exercise six orientations; record plausibility.
2. Acquire predeclared stationary captures with sequence/drop/saturation/timing fields.
3. Hash raw files and compare embedded/offline parsing/RMS on test vectors.
4. Backup person repeats ID/capture.

**Exit:** Timing/integrity evidence or visible failure/corrective plan.  
**Do not:** derive final classifier threshold or delete invalid blocks.

### Day 5 — Mechanical design review, not an automatic spin

1. Measure received motor/sensor; finish base/clamp/mount/hub/guard drawing.
2. Verify switch/fuse/jack compatibility and motor/logic isolation.
3. Build/inspect unpowered rig; manually rotate for clearance.
4. Only if the full safety checklist and reviewer approval exist, perform the staged no-eccentric current-limited pilot. Otherwise stop at inspection.

**Exit:** Approved unpowered rig or a safely recorded pilot; no requirement to force a powered result in Week 1.

## 12. Every-run rig safety checklist

- [ ] Exact `RIG/MOUNT/HW/CFG` labels match the run sheet.
- [ ] Motor power disconnected and shaft stopped during inspection/adjustment.
- [ ] Base restraint, motor clamp and fastener reference marks intact.
- [ ] Eccentric/normal fixture is the identified configuration with positive retention.
- [ ] Guard is attached and covers full rotating envelope; manual clearance check complete.
- [ ] Sensor mount and strain relief are rigid/intact.
- [ ] Switch/disconnect, fuse, connector and wiring are intact and correctly rated.
- [ ] USB logic power and 12 V motor power remain separate.
- [ ] Eye protection worn; hands/hair/clothing/lanyards/tools/cables clear.
- [ ] No loose object on base/bench.
- [ ] Host capture starts before motor and uses a new run filename.
- [ ] Stop conditions and stop operator verbally confirmed.
- [ ] Post-run power-off, shaft-stop and inspection completed.

Any failed item means **DO NOT ENERGIZE**. Create `ERR/CA` and reinspection; observers may call stop without permission.

## 13. Reject, replace and substitution rules

| Situation | Required action |
|---|---|
| Wrong exact MCU SKU/module | Quarantine/return. Do not pretend pin/software equivalence. |
| ADXL wrong/intermittent `DEVID` after known-good isolation | Quarantine/replace; preserve attempts. |
| Generic listing contradicts itself (for example title speed differs from description) | Do not select as preferred; require clarification or different seller. |
| Adapter wrong polarity/unstable/damaged/hot | Reject; no opening or mains-side repair. |
| Motor excessive current/wobble/noise/heat | Stop/quarantine; inspect under no power; do not compensate with larger fuse. |
| Fuse nuisance operation | Stop and investigate motor startup/operating current, fixture condition, wiring fault and required time-current characteristic. Document findings. Never bypass or increase the rating merely to prevent opening. |
| Mount/guard cannot be made stable | Redesign or use safer equivalent rig; no data run. |
| Preferred item unavailable | Recheck backup spec/price/stock and run equivalence decision. New board variant requires new pinout/toolchain gate. |
| Cost projects above ₹5,000 | Stop order; seek reuse/alternate exact source or owner/team approval. Do not drop protection/PPE/guard. |

## 14. Procurement closure checklist

- [ ] Every planning price replaced by actual invoice amount or explicitly left `NOT PURCHASED`.
- [ ] Shipping/GST/discount/refund and reused/donated value/status are separated.
- [ ] Every delivered critical part has `COMP` and `ACCEPT` with photos and test links.
- [ ] Quarantined/rejected items are separated and return/replace status recorded.
- [ ] Actual total reconciles to budget; variance explained.
- [ ] Spare inventory and locations recorded.
- [ ] Warranties/return deadlines and invoices archived.
- [ ] Exact as-built BOM links to final hardware configuration.

## 15. Unresolved procurement/lab questions

1. Which delivery postcode and institutional GST/invoice details apply?
2. Which listed tools, PPE, base/guard materials and fabrication services are already available and accepted in the lab?
3. What exact local base, motor clamp, sensor bracket and 3 mm captive hub can be fabricated after received-part measurement, and at what dated price?
4. Does the selected fuse system use blade or 5×20 mm glass format, and what final type/rating follows measured startup/current evidence?
5. Does the local lab require a faculty/lab-technician safety approval beyond the team signatures? No condition is assumed until documented.
6. Is the current exact DevKitC-32E orderable to the delivery postcode on purchase day, or must the approved backup be used?
7. Is a spare ADXL345 justified after first-unit acceptance while remaining inside budget?

## 16. Source notes

Official specifications take precedence over retailer descriptions:

- [Analog Devices ADXL345 data sheet](https://www.analog.com/media/en/technical-documentation/data-sheets/ADXL345.PDF), accessed 2026-08-09.
- [Espressif ESP32-DevKitC V4 user guide](https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32/esp32-devkitc/user_guide.html), accessed 2026-08-09.
- [Espressif ESP32-WROOM-32E/32UE data sheet](https://documentation.espressif.com/esp32-wroom-32e_esp32-wroom-32ue_datasheet_en.html), accessed 2026-08-09.
- [Espressif Arduino-ESP32 installation guide](https://docs.espressif.com/projects/arduino-esp32/en/latest/installing.html), accessed 2026-08-09.

Supplier pages were accessed 2026-08-09. Prices/stock are volatile, seller specifications may be incomplete, and no supplier listing is treated as acceptance evidence.
