# VibeGuard Mechanical Lab Field Guide & Fabrication Manual
**Document ID:** `VG-MECH-SOP-01`  
**Institutions:** Department of Cyber Security & Department of Mechanical Engineering, Jyothi Engineering College  
**Project:** VibeGuard — Machine Vibration & Predictive Maintenance Testbed  
**Date of Execution:** 17/09/2026  
**Students:** Mohammed Nihad P C (`JEC24CC044`), Sreehari K (`JEC24CC055`) / Sreeprada K S (`JEC24CC056`)  
**Printable Field PDF:** [`VibeGuard_Mechanical_Lab_Fabrication_and_Measurement_Manual.pdf`](file:///home/paradoxpete/Documents/PROJECT_ORGANIZED/VibeGuard_Mechanical_Lab_Fabrication_and_Measurement_Manual.pdf) (mirrored to `~/Downloads/`)

---

## PART 1: BASEPLATE SANDWICH DRILLING MASTER PROTOCOL

### 1.0 Technical Overview & Specifications

| Parameter | Laboratory Baseline Specification |
| :--- | :--- |
| **Material** | Cast Polymethyl Methacrylate (PMMA / Acrylic), Grade A optical |
| **Blank Geometry** | Two (2) square sheets of $150.0\text{ mm} \times 150.0\text{ mm} \times 5.0\text{ mm}$ |
| **Assembled Stack** | Monolithic $150.0\text{ mm} \times 150.0\text{ mm} \times 10.0\text{ mm}$ baseplate chassis |
| **Hole Count** | Exactly eight (8) precision through-holes |
| **Hole Diameter** | $\varnothing 3.30\text{ mm}$ finished (M3 Normal Clearance per ISO 273) |
| **Tooling Sequence** | **Pass 1:** Center Punch $\rightarrow$ **Pass 2:** Pilot Drill $\varnothing 2.5\text{ mm}$ $\rightarrow$ **Pass 3:** Final Ream $\varnothing 3.3\text{ mm}$ |
| **Crucial Warning** | **DO NOT use $\varnothing 3.0\text{ mm}$ bit.** (Hoop tensile stress $\sigma_\theta > 70\text{ MPa}$ causes spiderweb cracking). |

---

### 1.1 Lab Tooling & Equipment Requisition Checklist

Before beginning machining, ensure all items below are at your drill press workstation:

- [ ] **Bench Drill Press** with keyed chuck, depth stop collar, and clean table.
- [ ] **$\varnothing 2.5\text{ mm}$ HSS Twist Drill Bit** (pilot bit; check flutes for sharpness and zero runout).
- [ ] **$\varnothing 3.3\text{ mm}$ HSS Twist Drill Bit** (final clearance bit for M3 fasteners).
- [ ] **Automatic Center Punch** or hardened steel scriber.
- [ ] **Sacrificial Wood Backing Board** (Plywood or MDF, $\ge 12\text{ mm}$ thick, min $160 \times 160\text{ mm}$).
- [ ] **Two (2) Heavy-Duty C-Clamps** or wood screw clamps ($\ge 75\text{ mm}$ throat depth).
- [ ] **1:1 Scale Drill Sticker Template** (printed at 100% scale and verified against $50.0\text{ mm}$ calibration bar).
- [ ] **Masking Tape** or transparent adhesive tape.
- [ ] **Fine-Tip Permanent Marker** (for marking `INDEX A` across both plates).
- [ ] **Safety Goggles** (mandatory personal protective equipment).

---

### 1.2 The "INDEX A" Alignment Principle (Why & How to Mark Both Sheets)

#### A. Why Mark Both Sheets?
1. **Geometric Asymmetry:** Square acrylic sheets cut in workshops or with table saws are never 100.00% geometrically symmetric. One side might be $150.2\text{ mm}$ and another $149.8\text{ mm}$, with corner angles varying between $89.7^\circ$ and $90.3^\circ$.
2. **Asymmetric Hole Pattern:** The VibeGuard drilling template is intentionally non-symmetric:
   * N20 Motor bracket holes are at $X = 31.5\text{ mm}$ and $48.5\text{ mm}$ ($Y = 55.0\text{ mm}$).
   * ADXL345 Sensor bracket holes are at $X = 76.5\text{ mm}$ and $91.5\text{ mm}$ ($Y = 55.0\text{ mm}$).
   * Breadboard zone occupies the upper half ($Y \in [85, 140\text{ mm}]$).
3. **Concentricity Guarantee:** When you clamp both 5 mm sheets together and drill all 8 holes in a single pass, the holes through Sheet 1 and Sheet 2 match each other with **100% collinear concentricity** in that exact relative physical orientation.
4. **The Consequence of Not Marking:** If you unclamp the sheets after drilling and later rotate the bottom sheet $90^\circ$ or $180^\circ$, or flip it over, **none of the 8 holes will align!** The M3 bolts will bind or jam. Marking `INDEX A` on both sheets permanently records their shared orientation.

```
+-------------------------------------------------------------------------+
|                  SIDE / EDGE VIEW OF CLAMPED STACK                      |
|                                                                         |
|                 [ C-CLAMP ]                         [ C-CLAMP ]         |
|                      |                                   |              |
|        +-------------v-----------------------------------v-----------+  |
|INDEX A |  SHEET 1 (TOP 5 mm PMMA)                                    |  |
|  \     +-------------------------------------------------------------+  |
|   \--> |  SHEET 2 (BOTTOM 5 mm PMMA)                                 |  |
|        +-------------------------------------------------------------+  |
|        |  SACRIFICIAL PLYWOOD BACKING (>=12 mm)                      |  |
|        +-------------------------------------------------------------+  |
|                      ^                                   ^              |
|                      |                                   |              |
|                 [ C-CLAMP ]                         [ C-CLAMP ]         |
|                                                                         |
|  * The red diagonal slash physically marks the side edges of BOTH      |
|    plates simultaneously while they are clamped together.               |
+-------------------------------------------------------------------------+
```

#### B. How to Apply the Mark in 3 Quick Steps:
1. Stack both $150 \times 150\text{ mm}$ acrylic plates squarely on top of each other with all four edges perfectly flush.
2. In the top-left corner, take a permanent marker and draw a bold diagonal slash that **runs across the outside edge of Sheet 1 AND the outside edge of Sheet 2 simultaneously**.
3. Write **`INDEX A`** on the top face of Sheet 1 and on the matching corner face of Sheet 2.
4. **Result:** Whenever you separate the sheets for cleaning, deburring, or solvent bonding, simply align the two `INDEX A` markings. The 8 drilled holes will align with micrometer precision.

---

### 1.3 Clamping & Sacrificial Backing Setup (Preventing Breakout Chipping)

1. **Breakout Chipping Physics:** Acrylic (PMMA) is an amorphous, notch-sensitive thermoplastic with very low impact toughness. As a rotating twist drill bit breaks through the underside of an unsupported acrylic sheet, the cutting lips catch on the thin remaining plastic membrane. The upward cutting torque exerts high localized tensile stress ($\sigma > \sigma_{\text{ult}}$), causing the bottom surface to violently fracture outwards in large cone-shaped craters ("exit breakout blowout").
2. **Sacrificial Wood Backing:** Placing a flat, dense piece of scrap plywood or MDF ($\ge 12\text{ mm}$ thick, min $160 \times 160\text{ mm}$) directly beneath the bottom acrylic sheet provides continuous, rigid support. The wood backing acts as a continuous die plate, preventing the acrylic membrane from flexing downward and ensuring a razor-sharp, chip-free hole exit.
3. **Clamping Procedure:**
   * Assemble the stack: `[Drill Press Table] -> [Wood Backing] -> [Bottom Acrylic (5 mm)] -> [Top Acrylic (5 mm)] -> [1:1 Paper Template]`.
   * Place cardboard shims under the clamp jaws to prevent scratching the acrylic surfaces.
   * Tighten two C-clamps near opposite corners. Ensure clamping pressure is firm.
   * **STRICT RULE:** Never loosen, shift, or unclamp the sandwich until all 8 pilot holes have been drilled!

---

### 1.4 Master Baseplate 8-Hole Drilling Coordinates Reference Table

* **Origin (0,0):** Front-Left Corner of the $150.0 \times 150.0\text{ mm}$ board (Datum A).
* **Tolerance:** $\pm 0.2\text{ mm}$ on center punching; bit self-centering guides final ream.

| Hole ID | Subsystem / Mounting Purpose | Datum A: X (mm) | Datum A: Y (mm) | Pilot Drill | Final Drill | Fastener Specification |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| **C1** | Base Standoff Foot (Front-Left) | `10.0` | `10.0` | $\varnothing 2.5\text{ mm}$ | $\varnothing 3.3\text{ mm}$ | M3 $\times 20\text{ mm}$ socket bolt + DIN 125 washer |
| **C2** | Base Standoff Foot (Front-Right) | `140.0` | `10.0` | $\varnothing 2.5\text{ mm}$ | $\varnothing 3.3\text{ mm}$ | M3 $\times 20\text{ mm}$ socket bolt + DIN 125 washer |
| **C3** | Base Standoff Foot (Rear-Left / INDEX A) | `10.0` | `140.0` | $\varnothing 2.5\text{ mm}$ | $\varnothing 3.3\text{ mm}$ | M3 $\times 20\text{ mm}$ socket bolt + DIN 125 washer |
| **C4** | Base Standoff Foot (Rear-Right) | `140.0` | `140.0` | $\varnothing 2.5\text{ mm}$ | $\varnothing 3.3\text{ mm}$ | M3 $\times 20\text{ mm}$ socket bolt + DIN 125 washer |
| **M1** | N20 Motor Bracket (Left Mounting Slot) | `31.5` | `55.0` | $\varnothing 2.5\text{ mm}$ | $\varnothing 3.3\text{ mm}$ | M3 $\times 16\text{ mm}$ bolt + washer |
| **M2** | N20 Motor Bracket (Right Mounting Slot) | `48.5` | `55.0` | $\varnothing 2.5\text{ mm}$ | $\varnothing 3.3\text{ mm}$ | M3 $\times 16\text{ mm}$ bolt (Pitch = $17.0\text{ mm}$) |
| **S1** | ADXL345 Bracket Foot (Left Hole) | `76.5` | `55.0` | $\varnothing 2.5\text{ mm}$ | $\varnothing 3.3\text{ mm}$ | M3 $\times 16\text{ mm}$ bolt + washer |
| **S2** | ADXL345 Bracket Foot (Right Hole) | `91.5` | `55.0` | $\varnothing 2.5\text{ mm}$ | $\varnothing 3.3\text{ mm}$ | M3 $\times 16\text{ mm}$ bolt (Pitch = $15.0\text{ mm}$) |

---

### 1.5 Step-by-Step 4-Stage Precision Drilling Execution

- [ ] **Stage 1: Center Punching & Indentation**
  * Smooth the 1:1 paper template over the top sheet and tape all four borders.
  * Position the hardened tip of an automatic center punch or scriber precisely over each of the 8 crosshair intersections.
  * Apply light vertical pressure until a sharp conical prick dimple is formed in the acrylic face.
  * *Why:* The conical prick seats the rotating drill bit chisel edge, preventing bit "walk" or surface scratching.
- [ ] **Stage 2: Pilot Hole Drilling ($\varnothing 2.5\text{ mm}$ HSS Bit)**
  * Chuck the $\varnothing 2.5\text{ mm}$ bit into the drill press. Tighten with chuck key in all 3 holes.
  * Set spindle speed to **600–800 RPM**. *(Never use $>1200\text{ RPM}$; high speeds overheat PMMA and melt plastic into sticky gum).*
  * Lower the quill until the bit tip engages the center punch dimple.
  * Use the **"pecking" feed technique**: Feed down $1 - 2\text{ mm}$, retract slightly to evacuate white ribbon swarf, and re-advance.
  * Drill completely through both 5 mm sheets ($10\text{ mm}$ total depth) into the wood backing. Repeat for all 8 holes.
- [ ] **Stage 3: Final Clearance Hole Boring ($\varnothing 3.3\text{ mm}$ HSS Bit)**
  * Remove the pilot bit and chuck the $\varnothing 3.3\text{ mm}$ bit.
  * Keep spindle speed at **600–800 RPM**.
  * Slowly lower the spinning bit into each $\varnothing 2.5\text{ mm}$ pilot hole. The bit will act as a precision reamer, cleanly enlarging the bore to the exact ISO 273 clearance dimension ($3.30\text{ mm}$).
  * Feed smoothly and slowly. Do not jerk the quill lever. The bit will exit cleanly into the wood backing with zero chipping.
- [ ] **Stage 4: Deburring & Manual Edge Cleanup**
  * Unclamp the sandwich. Peel off the paper template and separate the two sheets.
  * Wipe away acrylic swarf with a soft brush or cloth.
  * Inspect the hole rims. If a slight raised lip exists, take an oversized drill bit ($\varnothing 5.0\text{ mm}$ or $\varnothing 6.0\text{ mm}$) in your **BARE HAND** (no power tool!) and lightly twist it 1–2 revolutions against the hole rim.
  * This cuts a smooth $0.2\text{ mm}$ micro-chamfer that strips burrs without altering the cylindrical bore diameter.

---

### 1.6 Immediate Mechanical Rigidity (No Glue Needed Today!)

**You do NOT need adhesive today to conduct motor vibration experiments!**

1. **Sandwich Mechanical Bolting:** Align the two sheets using their `INDEX A` markings. Insert four standard M3 $\times 20\text{ mm}$ bolts with DIN 125 flat washers through the four corner holes (`C1`, `C2`, `C3`, `C4`). Thread M3 nylon locknuts onto the bottom face and snug them down using a hex screwdriver and wrench.
2. **Clamping Force Physics:** Four M3 bolts torqued to normal hand tightness ($\approx 0.6\text{ N}\cdot\text{m}$) generate approximately **$3,500\text{ N}$ ($\approx 350\text{ kgf}$)** of uniform compressive clamping force across the $150 \times 150\text{ mm}$ baseplate interface.
3. **Frictional Interlock:** This normal force produces massive frictional resistance between the two smooth PMMA surfaces, eliminating any relative slip, flexure, or resonant chatter. The bolted stack behaves as a 100% rigid monolithic $10\text{ mm}$ chassis.
4. **Immediate Subsystem Mounting:** Mount the N20 motor bracket (holes `M1`, `M2`) and the ADXL345 bracket (holes `S1`, `S2`) using M3 $\times 16\text{ mm}$ bolts. You can begin motor spin-up, frequency sweeps, and ESP32 telemetry data acquisition immediately today without waiting for adhesives to cure.

---

### 1.7 Adhesive Sourcing & Post-Drill Capillary Solvent Welding Protocol

When you are ready to permanently fuse the two sheets into a single monolithic block:

1. **Gold Standard Solvent:** **Dichloromethane (DCM / Methylene Chloride)** or specialized Acrylic Solvent Cement.
   * *How it works:* DCM chemically dissolves PMMA polymer chains at room temperature. When the solvent evaporates, the polymer chains interlock, forming a true water-clear, bubble-free chemical weld with parent-material tensile strength ($70\text{ MPa}$).
   * *Where to source:* Request $15 - 20\text{ mL}$ from the **College Chemistry Lab**, or purchase a small bottle from local **Acrylic Sign-Board Fabricators** in Cheruthuruthy or Shoranur.
2. **Capillary Syringe Application Technique:**
   * Keep the two drilled plates bolted loosely together with `INDEX A` aligned.
   * Draw $2\text{ mL}$ of DCM into a glass or polyethylene medical syringe fitted with a fine blunt needle.
   * Touch the needle tip along the outside perimeter seam between the two sheets.
   * Capillary action will automatically pull the water-thin solvent inward across the entire interface within 3 seconds.
   * Snug down the corner bolts to squeeze out trapped air.
   * *Cure Time:* Handling strength is reached in 15 minutes; full mechanical cure in 24 hours.
3. **Workshop Fallback:** **Araldite Ultra Clear** (2-part epoxy). Apply a paper-thin film between the sheets and clamp for 24 hours.
4. **STRICT PROHIBITION — DO NOT USE FEVIKWIK / CYANOACRYLATE:**
   * Cyanoacrylate rapidly polymerizes on acrylic, releasing airborne monomer vapors that condense into a permanent, milky-white chalky film ("crazing / blooming").
   * Cyanoacrylate forms a brittle crystalline bond that shatters under the dynamic cyclic vibration of a 600 RPM eccentric motor.

---

### 1.8 Workshop Pitfalls & Prohibited Lab Actions Table

| Prohibited Action | Direct Physical Consequence | Correct Workshop Protocol |
| :--- | :--- | :--- |
| **Using $\varnothing 3.0\text{ mm}$ drill bit** | Radial clearance is only $25\text{ \mu m}$. Screw threads bite; hoop tensile stress $\sigma_\theta > 70\text{ MPa}$ causes brittle spiderweb cracking. | **Always use $\varnothing 3.3\text{ mm}$ bit** ($175\text{ \mu m}$ radial clearance per ISO 273). |
| **Drilling without wood backing** | Acrylic tensile tear-out as bit exits; bottom face fractures in large cone craters ("breakout"). | **Always clamp sandwich onto scrap plywood/MDF ($\ge 12\text{ mm}$).** |
| **Spindle speed $>1500\text{ RPM}$** | Frictional heat exceeds PMMA glass transition temp ($105^\circ\text{C}$); acrylic melts, gums up flutes, binds bit violently. | **Drill at 600–800 RPM** using the intermittent "pecking" feed technique. |
| **Unclamping between passes** | Collinearity lost; sheets shift; pilot and final bores will be eccentric and misaligned. | **Keep C-clamps locked** until all 8 pilot holes are finished through both sheets. |
| **Using Cyanoacrylate (Fevikwik)** | Releases volatile vapors that cause white crazing ("frosting"); brittle bond shatters under motor vibration. | **Use DCM solvent capillary weld** or Araldite Ultra Clear 2-part epoxy. |

---

## PART 2: VERNIER CALIPER PRECISION MEASUREMENT MANUAL

### 2.0 Caliper Anatomy, Zero Calibration & Proper Handling

A standard Vernier or digital caliper provides measurement resolution down to $0.02\text{ mm}$ ($20\text{ \mu m}$). Using it correctly ensures that 3D-printed parts and mechanical brackets fit together with zero post-machining filing.

```
                    [ INSIDE NIBS ] (Hole IDs & Slot Widths)
                         \    /
     +--------------------\--/----------------------------------------------+
     |                                                                   ===| [DEPTH PROBE]
     |  [OUTSIDE JAWS]         MAIN BEAM WITH MILLIMETER GRADUATIONS        | (Step heights)
     |    |            |                                                    |
     |    v            v                                                    |
     +----+------------+----------------------------------------------------+
                        \_______/
                    VERNIER SLIDER & THUMB ROLLER (0.02 mm / 0.05 mm scale)
```

1. **Outside Measuring Jaws:** Used for external dimensions (motor outer diameter, D-shaft diameter, PCB width/length, acrylic plate thickness, bolt shank diameter).
   * *Rule:* Place the workpiece deep in the jaws, near the main beam—never at the extreme tips. Ensure the jaws are strictly perpendicular to the workpiece to avoid cosine tilt error.
2. **Inside Measuring Nibs:** Used for internal dimensions (mounting hole diameters, bracket cradle width, slot spacing).
   * *Rule:* Insert the nibs fully into the hole without canting. Gently open the jaws until both cylindrical contact faces touch the hole walls.
3. **Depth Measuring Probe:** Extends from the tail of the main beam; used for step heights, blind pocket depths, and gearbox boss protrusions.
   * *Rule:* Hold the flat end of the caliper beam flush against the reference surface and slide the probe down until it contacts the bottom step.
4. **Zero Calibration Protocol:**
   * Wipe the jaw measuring faces with clean paper or cloth to remove dust and oil.
   * Close the jaws gently using the thumb roller.
   * Look closely at the scale: The `0` mark on the Vernier scale must align perfectly with the `0` mark on the main beam (or the digital display must read `0.00 mm`).
   * *If an offset exists:* Record the zero error ($\pm e$) and subtract it from all subsequent measurements.

---

### 2.1 Hole Pitch Center-to-Center Formulas (Eliminating Tangent Uncertainty)

**NEVER GUESS OR EYEBALL HOLE CENTERS!** Because caliper jaws cannot balance on virtual centerlines, measuring hole pitch directly leads to massive human error. Instead, use the exact tangent dimension formula:

$$\text{Method A (Outside Span):} \quad \text{Pitch } P = L_{\text{outer}} - D_{\text{hole}}$$

$$\text{Method B (Inside Span):} \quad \text{Pitch } P = L_{\text{inner}} + D_{\text{hole}}$$

* Where $L_{\text{outer}}$ is the distance measured across the far outside edges of both holes using the outside jaws.
* Where $L_{\text{inner}}$ is the distance measured across the near inside edges of both holes using the inside nibs.
* Where $D_{\text{hole}}$ is the measured hole diameter.

**Worked Example (ADXL345 PCB Pitch Verification):**
* Measured hole diameter $D = 3.20\text{ mm}$.
* Measured outside span $L_{\text{outer}} = 18.20\text{ mm}$.
* True center-to-center pitch:
  $$P = 18.20 - 3.20 = 15.00\text{ mm} \quad (\text{Exact nominal match!})$$

---

### 2.2 Systematic Component-by-Component Measurement Protocols

#### 1. N20 Micro Metal Gear Motor
- [ ] **Output D-Shaft Outer Diameter (OD):** Measure the round cylindrical section of the shaft using outside jaws. Nominal: $3.00\text{ mm}$ (typical commercial range: $2.95 - 2.98\text{ mm}$).
- [ ] **D-Flat Chord Thickness:** Measure the distance from the flat face across to the curved back of the shaft. Nominal: $2.50\text{ mm}$ (typical commercial range: $2.44 - 2.48\text{ mm}$). *Critical for 3D-printed rotor arm bore fit!*
- [ ] **D-Flat Axial Length:** Measure the length of the flat cutout along the shaft. Nominal: $\approx 7.0\text{ mm}$.
- [ ] **Total Usable Shaft Length:** Measure from the brass gearbox front boss face to the shaft tip. Nominal: $9.5 - 10.0\text{ mm}$. Dictates the maximum height of the rotor arm hub.
- [ ] **Gearbox Casing Dimensions:** Measure body width ($12.0\text{ mm}$ nom), body height ($10.0\text{ mm}$ nom), and gearbox length ($9.0 - 15.0\text{ mm}$ depending on gear ratio).

#### 2. Robocraze ADXL345 Breakout Board
- [ ] **Mounting Hole Inner Diameter:** Measure the plated mounting holes using the inside nibs. Nominal: $3.20\text{ mm}$ ($3.0 - 3.2\text{ mm}$).
- [ ] **Hole Center-to-Center Pitch:** Measure outside span $L_{\text{outer}}$ and calculate $P = L_{\text{outer}} - D$. Target pitch: $15.00\text{ mm}$. *This dictates the hole spacing on the upright sensor bracket.*
- [ ] **PCB Substrate Width & Length:** Measure overall PCB outline with outside jaws. Nominal: $15.5\text{ mm} \times 20.5\text{ mm}$.
- [ ] **PCB Thickness:** Measure substrate thickness. Nominal: $1.60\text{ mm}$. Verify header pin solder joints for vertical clearance.

#### 3. N20 Stamped Metal U-Bracket
- [ ] **Baseplate Mounting Hole Pitch:** Measure center-to-center pitch of the two base mounting slots. Nominal: $17.00\text{ mm}$.
- [ ] **Base Hole Inner Diameter:** Measure slot width with inside nibs. Nominal: $3.20 - 3.50\text{ mm}$ (clears M3 bolt).
- [ ] **Internal Cradle Width:** Measure the internal gap between the metal uprights. Must snugly accommodate the $12.0\text{ mm}$ N20 gearbox body without lateral play.
- [ ] **Motor Face Screws Pitch:** Measure center-to-center spacing of the two M1.6 motor face mounting holes. Nominal: $9.00\text{ mm}$.

#### 4. Acrylic Baseplate Blanks (Dual 5 mm Sheets)
- [ ] **Sheet 1 Thickness (Top Plate):** Measure thickness at all four corners using outside jaws. (Commercial cast PMMA varies from $4.6\text{ mm}$ to $5.2\text{ mm}$).
- [ ] **Sheet 2 Thickness (Bottom Plate):** Measure thickness at all four corners.
- [ ] **Combined Stack Thickness:** Measure clamped sandwich thickness. Nominal: $10.00\text{ mm}$. *Verifies required M3 bolt grip length.*
- [ ] **Blank Width & Length:** Measure outer edges of both sheets. Nominal: $150.0\text{ mm} \times 150.0\text{ mm}$.
- [ ] **Squareness Verification (Diagonals):** Measure diagonal distance $D_1$ (Corner 1 to 4) and $D_2$ (Corner 2 to 3). For a true $150 \times 150\text{ mm}$ square:
  $$D_{\text{nominal}} = \sqrt{150^2 + 150^2} = 212.13\text{ mm}$$
  *If $D_1 \neq D_2$, the blank has a parallelogram skew.*

#### 5. M3 Fasteners, Washers & Nylon Locknuts
- [ ] **M3 Bolt Thread Major Diameter:** Measure outside thread crests. Nominal: $2.92 - 2.95\text{ mm}$ (must slide freely into $\varnothing 3.3\text{ mm}$ holes).
- [ ] **Bolt Length Under Head:** Measure threaded shank length. Standoff bolts: $20.0\text{ mm}$; Bracket bolts: $16.0\text{ mm}$.
- [ ] **DIN 125 M3 Washer Outer Diameter:** Measure outer washer diameter. Nominal: $7.00\text{ mm}$.
- [ ] **DIN 125 M3 Washer Inner Diameter:** Measure hole diameter. Nominal: $3.20\text{ mm}$.
- [ ] **M3 Nylon Locknut Width Across Flats:** Measure hex width. Nominal: $5.50\text{ mm}$.

---

### 2.3 Physical Measurement Recording Ledger (Fillable in Lab)

Print Page 4 of the PDF or use the table below to record your physical vernier caliper readings with a pen in the lab:

| Check | Component Parameter to Measure | Expected Nominal | Trial 1 (mm) | Trial 2 (mm) | Average (mm) | Fit / Action Required |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| [ ] | **N20 Shaft Outer Diameter (OD)** | `3.00 mm` | | | | Rotor hub bore sizing |
| [ ] | **N20 D-Flat Chord Thickness** | `2.50 mm` | | | | Rotor D-flat chord fit |
| [ ] | **N20 Usable Shaft Length** | `9.50 mm` | | | | Max rotor hub thickness |
| [ ] | **N20 Motor Body Width** | `12.00 mm` | | | | Metal bracket clamp fit |
| [ ] | **N20 Bracket Base Hole Pitch** | `17.00 mm` | | | | Baseplate hole M1–M2 spacing |
| [ ] | **ADXL345 PCB Hole Diameter** | `3.20 mm` | | | | M3 screw clearance check |
| [ ] | **ADXL345 Hole Center Pitch** | `15.00 mm` | | | | Sensor bracket upright pitch |
| [ ] | **ADXL345 PCB Dimensions (W × L)** | `15.5 × 20.5 mm` | | | | Sensor bracket face pocket |
| [ ] | **Acrylic Sheet 1 Thickness** | `5.00 mm` | | | | Top plate actual gauge |
| [ ] | **Acrylic Sheet 2 Thickness** | `5.00 mm` | | | | Bottom plate actual gauge |
| [ ] | **Combined Stack Thickness** | `10.00 mm` | | | | M3 bolt grip length verify |
| [ ] | **Acrylic Blank 1 (W × L)** | `150 × 150 mm` | | | | Edge flushness check |
| [ ] | **Acrylic Blank 2 (W × L)** | `150 × 150 mm` | | | | Edge flushness check |
| [ ] | **Acrylic Diagonals ($D_1$ vs $D_2$)** | `212.1 mm` | | | | Squareness check ($D_1 = D_2$) |
| [ ] | **M3 Bolt Shank Major Diameter** | `2.92 mm` | | | | Free slip in 3.3 mm holes |
| [ ] | **DIN 125 Washer Outer Diameter** | `7.00 mm` | | | | Bearing shelf verification |

---

### 2.4 Translating Caliper Data into 3D CAD Print Tolerances

When modifying 3D models (`FAB-01` Rotor Cam Arm and `FAB-02` Sensor Bracket) in CAD before re-printing:

1. **FDM 3D Printing Thermal Shrinkage (PLA / PETG):** Molten extruded thermoplastic contracts inwards as it cools from $205^\circ\text{C}$ to room temperature. Internal cylindrical bores always print smaller than modeled:
   * **Bolt Through-Holes:** Model at **$+0.20\text{ mm}$** over fastener diameter (e.g. for M3 bolt, model bore at $\varnothing 3.20\text{ mm}$ to achieve a print that measures $\approx 3.02\text{ mm}$).
   * **N20 Motor D-Shaft Snug Press-Fit:**
     * If measured shaft OD is $3.00\text{ mm}$, model CAD cylindrical bore at $\varnothing 3.15\text{ mm}$.
     * If measured flat chord is $2.50\text{ mm}$, model CAD flat chord at $2.65\text{ mm}$.
   * **Rotor Fit Tuning Rule:**
     * If previous print was too loose and spun on the flat: Reduce CAD bore diameter by $-0.05\text{ mm}$ (to $\varnothing 3.10\text{ mm}$).
     * If previous print was too tight and could not be pressed on without filing: Increase CAD bore diameter by $+0.05\text{ mm}$ (to $\varnothing 3.20\text{ mm}$).
2. **ADXL345 Bracket Upright Hole Spacing:** The two horizontal holes on the vertical upright flange must match your measured ADXL345 PCB pitch ($15.00\text{ mm}$) within $\pm 0.05\text{ mm}$ to avoid bending the PCB substrate during bolting.

---

### 2.5 Laboratory Session Sign-Off & Attestation

| Role | Name & Roll Number | Date | Signature |
| :--- | :--- | :---: | :---: |
| **Student Lead (Measurement)** | Mohammed Nihad P C (`JEC24CC044`) | 17/09/2026 | _________________________ |
| **Team Member (Fabrication)** | Sreehari K (`JEC24CC055`) / Sreeprada K S (`JEC24CC056`) | 17/09/2026 | _________________________ |
| **Mechanical Lab In-Charge** | Faculty / Lab Instructor | 17/09/2026 | _________________________ |

---

## 3. Printable Field Assets Summary

| File Asset | File Path | Direct Downloads Link | Description |
| :--- | :--- | :--- | :--- |
| **4-Page Lab Manual PDF** | [`VibeGuard_Mechanical_Lab_Fabrication_and_Measurement_Manual.pdf`](file:///home/paradoxpete/Documents/PROJECT_ORGANIZED/VibeGuard_Mechanical_Lab_Fabrication_and_Measurement_Manual.pdf) | [`~/Downloads/VibeGuard_Mechanical_Lab_Fabrication_and_Measurement_Manual.pdf`](file:///home/paradoxpete/Downloads/VibeGuard_Mechanical_Lab_Fabrication_and_Measurement_Manual.pdf) | **Complete 4-page print-ready manual.** Formatted for black-and-white photocopy/laser printing with fillable measurement tables. |
| **1:1 Scale Drill Template PDF** | [`VibeGuard_Baseplate_1to1_Drill_Sticker_Template.pdf`](file:///home/paradoxpete/Documents/PROJECT_ORGANIZED/VibeGuard_Baseplate_1to1_Drill_Sticker_Template.pdf) | [`~/Downloads/VibeGuard_Baseplate_1to1_Drill_Sticker_Template.pdf`](file:///home/paradoxpete/Downloads/VibeGuard_Baseplate_1to1_Drill_Sticker_Template.pdf) | **1:1 scale true A4 printout.** Includes $50.0\text{ mm}$ calibration bar to tape directly onto acrylic for drilling. |
| **Vector CAD Blueprint SVG** | [`VibeGuard_Baseplate_Drilling_Blueprint_Exact.svg`](file:///home/paradoxpete/Documents/PROJECT_ORGANIZED/VibeGuard_Baseplate_Drilling_Blueprint_Exact.svg) | [`~/Downloads/VibeGuard_Baseplate_Drilling_Blueprint_Exact.svg`](file:///home/paradoxpete/Downloads/VibeGuard_Baseplate_Drilling_Blueprint_Exact.svg) | Exact mathematical vector blueprint with dark-mode engineering styling and coordinate matrix. |
