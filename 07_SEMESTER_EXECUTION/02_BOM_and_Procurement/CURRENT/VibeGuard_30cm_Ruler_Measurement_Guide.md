# VibeGuard: 30 cm Ruler (Scale) Measurement Guide

**Project:** VibeGuard — Edge AI Mechanical Vibration Diagnostic Testbed  
**Document ID:** VG-GUIDE-RULER-30  
**Target Tool:** Standard 30 cm / 12-inch Flat School / Engineering Ruler (Metric Scale)  
**Resolution:** 1 cm Major Divisions, 1 mm Minor Divisions (9 small ticks between numbers)  
**Target Hardware:** N20 Micro Metal Gear Motor, Robocraze ADXL345 Breakout (#TJFKQXJUQ), M3 Fasteners, 12 mm Wooden Baseplate

---

## 1. How Your 30 cm Ruler Scale is Structured

A standard 30 cm ruler is divided into centimeters ($1\text{ cm} = 10\text{ mm}$). Between every centimeter number, there are **9 small tick lines** dividing the centimeter into 10 intervals of **$1\text{ mm}$ ($0.1\text{ cm}$)** each:

```
  |   |   |   |   |   |   |   |   |   |   |
 10   .1  .2  .3  .4  .5  .6  .7  .8  .9  11 cm
  |                   |                   |
 0mm                 5mm                10mm
```

### Quick Decimal & Tick Translation Table

| Ruler Reading (Counting from an integer line) | Equivalent Millimeters | Typical VibeGuard Component Matching This Size |
| :--- | :--- | :--- |
| **0 lines (on the line)** | $0.0\text{ mm}$ | Starting Reference Mark |
| **1 small tick line** | $1.0\text{ mm}$ | PCB thickness ($1.6\text{ mm} \approx 1.5$ ticks) |
| **2 small tick lines** | $2.0\text{ mm}$ | U-bracket metal thickness |
| **2 ticks + halfway to 3rd** | $2.5\text{ mm}$ | **N20 D-Shaft Flat Thickness** ($T_{\text{flat}}$) |
| **3 small tick lines** | $3.0\text{ mm}$ | **N20 Shaft Round Diameter** ($D_{\text{shaft}}$) |
| **3 ticks + tiny hair past** | $3.2\text{ mm}$ | **M3 Clearance Hole Diameter** |
| **5 small tick lines (taller middle mark)** | $5.0\text{ mm}$ | M3 bolt head diameter |
| **7 small tick lines** | $7.0\text{ mm}$ | Standard M3 washer outer diameter |
| **9 small tick lines** | $9.0\text{ mm}$ | Wide M3 washer outer diameter |
| **9 ticks + halfway to 10** | $9.5\text{ mm}$ | N20 usable shaft length |
| **1 full cm + 2 small ticks** | $12.0\text{ mm}$ | **Rotor Arm Pitch & Baseplate Thickness** |
| **1 full cm + 5 small ticks** | $15.0\text{ mm}$ | **ADXL345 Mounting Hole Pitch** |
| **1 full cm + 7 small ticks** | $17.0\text{ mm}$ | **N20 Motor U-Bracket Hole Pitch** |
| **2 full cm marks** | $20.0\text{ mm}$ | **Motor-to-Sensor Separation Gap** |

---

## 2. The 4 Golden Rules for Measuring Small Parts with a Ruler

Measuring tiny mechanical components ($2\text{ to }15\text{ mm}$) with a 30 cm ruler requires special care to avoid large errors:

### Rule 1: Never Use the "0" End of the Ruler (The Offset Origin Rule)
Plastic and wooden rulers have worn, rounded, or chipped corners at the "0" end, and many rulers have a blank $2\text{–}5\text{ mm}$ dead margin before the zero mark.  
> **Always start measuring from a clean integer line inside the ruler, such as the $10.0\text{ cm}$ or $5.0\text{ cm}$ mark!**  
> *Example:* To measure a $15\text{ mm}$ hole pitch, align the first hole with the **$10.0\text{ cm}$** mark. The second hole will line up at **$11.5\text{ cm}$** ($11.5 - 10.0 = 1.5\text{ cm} = 15\text{ mm}$).

### Rule 2: Avoid Parallax Error (Look Strictly 90° from Above)
Because a ruler has thickness ($1\text{–}2\text{ mm}$), looking at the tick lines from an angle will shift your reading by up to $1\text{ mm}$.  
* Always look directly perpendicular down onto the ruler line.
* Stand the ruler on its thin edge if possible so the tick marks touch the surface of the component directly.

### Rule 3: The "Paper & Pin Puncture" Trick for Hole Spacing
Ruler tick lines cannot reach inside small $3\text{ mm}$ holes. Trying to guess the center of a hole by hovering a ruler above it causes $1\text{–}2\text{ mm}$ errors.  
**Use this foolproof optical transfer method:**
1. Take a plain white piece of paper or cardboard index card.
2. Place the ADXL345 PCB or N20 bracket flat on top of the paper.
3. Take a sharp sewing needle, safety pin, or mechanical pencil tip ($0.5\text{ mm}$) and press straight down through the center of both holes to puncture two clean tiny pinpricks into the paper.
4. Remove the PCB. Place your 30 cm ruler flat across the two pinholes on the paper.
5. Align Pinhole 1 exactly on the **$10.0\text{ cm}$** line. Read the exact tick mark where Pinhole 2 lands!

```
   PCB on Paper:        [Pin 1]                 [Pin 2]
                          v                       v
                         ( O )------------------( O )
   Paper Punctures:        *                       *
                          |                       |
   Ruler Alignment:     10.0 cm                11.5 cm  --> Exactly 15 mm!
```

### Rule 4: The "Edge-to-Edge" Method for Holes
If you measure directly on the component:
* Do NOT try to guess where the center of the circle is.
* Instead, align the **left inner edge** of Hole 1 with a full centimeter line (e.g. $10.0\text{ cm}$).
* Look at the **left inner edge** of Hole 2. Because both holes are identical circles, the distance between their left edges equals the exact center-to-center pitch!

---

## 3. Step-by-Step Component Measurement Walkthrough

### 3.1 N20 Micro Gear Motor Output D-Shaft

```
      [ GEARBOX ]
          |====|      ======== ROUND SHAFT ========
          |====|     |                             |
          +----+-----|-----------------------------+--
                     |====== D-FLAT PROFILE =======|
                     |<------- Usable Length ----->|
```

#### Step 1: Shaft Round Outer Diameter ($D_{\text{shaft}}$)
1. Lay the N20 motor flat on a table so the shaft lies horizontally.
2. Stand your 30 cm ruler vertically on edge against the shaft tip.
3. Align the bottom edge of the cylindrical shaft with the **$10.0\text{ cm}$** line.
4. Look across the top of the shaft:
   * It will cover exactly **3 small millimeter spaces** ($10.3\text{ cm}$).
   * If it covers 3 full millimeter spaces, your shaft is standard **$3.0\text{ mm}$**.
   * If it covers noticeably more than 3 ticks (reaching 4 ticks), note it down immediately.

#### Step 2: Shaft Flat Thickness ($T_{\text{flat}}$)
1. Rotate the shaft so the flat face is facing directly upwards toward the ceiling.
2. Hold the ruler on edge against the end of the shaft.
3. Align the curved bottom of the shaft with the **$10.0\text{ cm}$** line.
4. Look at the flat top face:
   * It should sit **exactly halfway between the 2nd and 3rd tick lines** ($10.25\text{ cm} = 2.5\text{ mm}$).
   * If it reaches 3 full ticks, there is almost no flat cut! If it only reaches 2 ticks, the flat cut is very deep ($2.0\text{ mm}$).

#### Step 3: Usable Shaft Length ($L_{\text{shaft}}$)
1. Lay the motor flat. Place the ruler parallel along the length of the shaft.
2. Align the **$10.0\text{ cm}$** line with the front brass collar where the shaft emerges from the gearbox.
3. Look at where the steel shaft terminates:
   * It should reach 9 small ticks plus halfway to the 10th mark (**$10.95\text{ cm}$**, or approximately **$9.5\text{ mm}$**).

---

### 3.2 Robocraze ADXL345 Accelerometer Breakout Board

```
      +-------------------------------------------------+
      |   ( O ) <---------- Pitch P ----------> ( O )   |
      |     |                                     |     |  <-- Mounting Holes
      |   [Edge]                                [Edge]  |
      |                                                 |
      |              [ ADXL345 IC CHIP ]                |
      |                                                 |
      |       [ O   O   O   O   O   O   O   O ]         |  <-- 8-pin Header
      +-------------------------------------------------+
```

#### Step 4: Mounting Hole Pitch ($P_{\text{hole}}$)
* **Method:** Use the **Paper & Pin Puncture Trick** (Section 2, Rule 3).
* Place the ADXL345 board on a paper sheet, puncture through both mounting holes with a needle/pin, and measure the distance between the two punctures.
* **Reading on Ruler:**
  * Align Pin 1 on **$10.0\text{ cm}$**.
  * Pin 2 should land on **$11.5\text{ cm}$** (exactly 1 full cm mark plus the 5th taller millimeter tick mark).
  * **Result:** $1.5\text{ cm} = 15.0\text{ mm}$.
  * *(If it lands slightly past 11.5 cm at roughly 11.52 cm, it is standard 0.6 inch / 15.24 mm breadboard grid).*

#### Step 5: Mounting Hole Diameter ($D_{\text{pcb\_hole}}$)
1. Lay the ruler flat across the top of the hole.
2. The clear hole opening should span just over **3 small tick lines** (approx. $3.2\text{ mm}$).
3. **Quick Test Without Ruler:** Take an M3 machine screw from your hardware kit. Does the threaded shank pass smoothly through the hole without force?
   * If **YES:** The hole is $\ge 3.1\text{ mm}$ (confirmed M3 clearance).
   * If **NO (binds or won't enter):** The hole is $2.5\text{ mm}$ or $2.6\text{ mm}$ (M2.5 size).

#### Step 6: Backside Solder Blobs / Header Pins
1. Turn the board sideways so you can see the back profile.
2. Hold the ruler against the back fiberglass plane.
3. Inspect how far the solder joints or clipped pin stubs stick out:
   * Typically **1 small tick to 1.5 ticks** ($1.0\text{–}1.5\text{ mm}$).

---

### 3.3 N20 Aluminum U-Bracket

#### Step 7: U-Bracket Mounting Hole Pitch ($P_{\text{bracket}}$)
1. Use the **Paper & Pin Puncture Trick**: Place the aluminum bracket flat on paper, poke a pin through both bottom mounting holes.
2. Align Pin 1 on **$10.0\text{ cm}$**.
3. Pin 2 should land on **$11.7\text{ cm}$** (1 full cm plus 7 small ticks).
4. **Result:** $1.7\text{ cm} = 17.0\text{ mm}$.

---

### 3.4 M3 Hardware & Baseplate

#### Step 8: Steel Washer Outer Diameter ($D_{\text{washer}}$)
1. Place a washer flat on a white sheet.
2. Align the left edge of the washer with **$10.0\text{ cm}$**.
3. Look at the right edge:
   * If it reaches **7 small ticks** ($10.7\text{ cm}$), you have a standard $7.0\text{ mm}$ DIN 125 washer.
   * If it reaches **9 small ticks** ($10.9\text{ cm}$), you have a wide $9.0\text{ mm}$ DIN 9021 washer.
   * *(Both work! Our $15\text{ mm}$ riser block gives $+7.5\text{ mm}$ clearance for $7\text{ mm}$ washers, and $+6.5\text{ mm}$ clearance for $9\text{ mm}$ washers).*

#### Step 9: Wooden Baseplate Thickness ($T_{\text{plank}}$)
1. Hold the ruler against the outer cut edge of the wooden board.
2. Align the bottom face with a full centimeter line (e.g. $5.0\text{ cm}$).
3. Count the ticks to the top face:
   * Should be 1 full cm plus 2 small ticks (**$1.2\text{ cm} = 12.0\text{ mm}$**).

---

## 4. 30 cm Ruler Audit Sheet (Fill & Send Back)

Align each feature with the **$10.0\text{ cm}$** reference mark on your 30 cm ruler, record the second mark you see, and fill in the table below:

| # | Component & Feature | Start Mark on Ruler | End Mark on Ruler | Your Ruler Reading (cm + ticks) | Converted mm | Expected Nominal |
| :-: | :--- | :---: | :---: | :--- | :--- | :--- |
| **1** | **N20 Shaft Round OD** | 10.0 cm | 10._ cm | 10 cm + __ ticks | __.__ mm | $3.0\text{ mm}$ (3 ticks) |
| **2** | **N20 Shaft Flat Thickness** | 10.0 cm | 10._ cm | 10 cm + __ ticks | __.__ mm | $2.5\text{ mm}$ (2.5 ticks) |
| **3** | **N20 Shaft Usable Length** | 10.0 cm | 10._ cm | 10 cm + __ ticks | __.__ mm | $9.5\text{ mm}$ (9.5 ticks) |
| **4** | **N20 Bracket Hole Pitch** | 10.0 cm | 11._ cm | 11 cm + __ ticks | __.__ mm | $17.0\text{ mm}$ (1.7 cm) |
| **5** | **ADXL345 PCB Hole Pitch** | 10.0 cm | 11._ cm | 11 cm + __ ticks | __.__ mm | $15.0\text{ mm}$ (1.5 cm) |
| **6** | **ADXL345 PCB Hole Size** | M3 bolt test: Does an M3 screw slide smoothly through the hole? | `[ ] YES  [ ] NO` | $3.2\text{ mm}$ |
| **7** | **ADXL345 Solder Protrusion** | 10.0 cm | 10._ cm | 10 cm + __ ticks | __.__ mm | $1.0\text{–}1.5\text{ mm}$ |
| **8** | **M3 Washer Outer Diameter**| 10.0 cm | 10._ cm | 10 cm + __ ticks | __.__ mm | $7.0\text{ or }9.0\text{ mm}$ |
| **9** | **Wood Baseplate Thickness**| 10.0 cm | 11._ cm | 11 cm + __ ticks | __.__ mm | $12.0\text{ mm}$ (1.2 cm) |

---
