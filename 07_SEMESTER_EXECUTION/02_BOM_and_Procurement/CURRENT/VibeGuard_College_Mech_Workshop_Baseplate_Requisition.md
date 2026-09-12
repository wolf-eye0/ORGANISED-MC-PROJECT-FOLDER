# VibeGuard: Mechanical Workshop & Carpentry Job Requisition
**Component:** Rig Baseplate (G4-1) & Mechanical Mounting Preparation  
**Institution:** Jyothi Engineering College (Autonomous), Cheruthuruthy, Kerala  
**Department:** Computer Science & Engineering / Electronics & Communication Engineering  
**Target Facility:** Mechanical Workshop (Carpentry & Fitting Section)  
**Primary Contact:** Amith Krishna Das (Hardware & Mechanical Lead)  

---

## 1. Work Order Overview for Workshop Superintendent / Technician

> [!NOTE]
> **Engineering Purpose:** VibeGuard is an embedded edge vibration monitor. We are building a benchtop machine fault testbed using a 12V N20 gear motor that spins an off-center unbalance weight.  
> **Physical Requirement:** The motor and sensor must be anchored to a **stiff, dense, flat plate** so mechanical vibration transfers efficiently through the solid material into the ADXL345 sensor without flexing, warping, or acoustic resonance.

---

## 2. Material Options (Scrap Bin Offcut is Acceptable)

Please provide and cut one piece from workshop scrap stock matching either of these specifications:

| Preference | Material Type | Dimensions ($L \times W \times T$) | Notes |
|:---:|---|---|---|
| **Option 1** | **Hard Plywood or Marine Plywood** | **$150 \times 150\text{ mm}$** ($\approx 6 \times 6\text{ inches}$), **$10\text{ mm}$ to $12\text{ mm}$ thick** | High stiffness, dampens tabletop rattle, holds wood screws firmly. |
| **Option 2** | **Dense Hardwood Plank (Teak / Mahogany / Rubberwood)** | **$150 \times 150\text{ mm}$**, **$12\text{ mm}$ to $15\text{ mm}$ thick** | Must be planed flat on both faces. Zero warping. |
| **Option 3 (FULFILLED)** | **Clear Cast Acrylic Sheet (Acrylite / PMMA)** | **$150 \times 150\text{ mm}$**, **$2\times 5\text{ mm}$ sheets ($10\text{ mm}$ stacked)** | **ACQUIRED & IN HAND:** Two 5mm sheets stacked/laminated provide high rigidity, zero grain resonance, and transparent exhibition aesthetics. |

> [!NOTE]
> **Fulfillment Status (2026-09-12):** Baseplate material has been successfully acquired as **Two $150 \times 150 \times 5.0\text{ mm}$ Acrylite (Cast Acrylic) plates**. When bonded or clamped with the corner standoffs, they form a solid $10.0\text{ mm}$ rigid vibration-conducting baseplate.

> [!CAUTION]
> **Prohibited Materials:** Do NOT use soft cardboard, styrofoam, low-density packing wood, or thin sheet metal ($\le 3\text{ mm}$). Thin metal flexes like a drumhead (membrane resonance), creating spurious harmonics.

---

## 3. Baseplate Layout & Drilling / Marking Template

```
+-----------------------------------------------------------------------+
|  [O] 4 mm Mounting Hole (Corner 1)              Corner 2 [O]          |
|                                                                       |
|                     +---------------------------+                     |
|                     |   BREADBOARD & ESP32      |                     |
|                     |   ELECTRONICS ZONE        |                     |
|                     |   (85 mm x 55 mm)         |                     |
|                     +---------------------------+                     |
|                                                                       |
|        N20 MOTOR POSITION                  ADXL345 SENSOR             |
|       +-------------------+               +---------------+           |
|       |  [O]  (17 mm) [O] |               |  [O] (15) [O] |           |
|       |   Motor U-Bracket | <--- 20 mm -->|  Sensor Mount |           |
|       +-------------------+               +---------------+           |
|                 |                                                     |
|                 v                                                     |
|          Rotating Cam Area                                            |
|                                                                       |
|  [O] Corner 3                                   Corner 4 [O]          |
+-----------------------------------------------------------------------+
|<------------------------------ 150 mm ------------------------------->|
```

### Drilling & Machining Operations Requested:
1. **Cutting & Squaring:**
   * Cut baseplate stock to square dimensions: **$150\text{ mm} \times 150\text{ mm} \ (\pm 2\text{ mm})$**.
   * Lightly sand/deburr all 4 edges and corners to prevent splinters.
2. **Motor Bracket Pilot Holes (2 Holes):**
   * **Location:** Center-left quadrant of the board.
   * **Center-to-Center Spacing:** **$17.0\text{ mm}$** (matches the pre-punched holes in the aluminum N20 U-bracket).
   * **Pilot Drill Bit:** **$2.0\text{ mm}$ or $2.5\text{ mm}$ drill bit** to a depth of $8\text{ mm}$ (prevents wood from splitting when tightening M3 wood screws).
3. **Sensor Mount Pilot Holes (2 Holes):**
   * **Location:** Exactly **$20.0\text{ mm}$ parallel distance** from the motor bracket.
   * **Center-to-Center Spacing:** **$15.0\text{ mm}$** (or $16.0\text{ mm}$ for 3D bracket base).
   * **Pilot Drill Bit:** **$2.0\text{ mm}$ drill bit** to a depth of $8\text{ mm}$.
4. **Base Isolation Feet (Optional, 4 Holes):**
   * Four $3.5\text{ mm}$ holes, 10 mm inset from each corner, to attach small rubber feet or standoffs so the rig does not vibrate across the table during tests.

---

## 4. Requisition Dialogue Script for Students

**Whom to Approach:** Carpentry Workshop Instructor or Fitting/Machine Shop Superintendent.

> *"Good morning Sir,*  
> *We are final-year students working on our microcontroller semester project (VibeGuard Vibration Fault Diagnostic Rig).*  
> *We need a small, sturdy baseboard from the workshop scrap bin to mount our test motor and vibration sensor:*  
> *1. Could you help us cut a scrap offcut piece of **plywood or dense wood, roughly 15 cm by 15 cm, 10 to 12 mm thick**?*  
> *2. Could you help us drill two small 2 mm pilot holes with 17 mm spacing so we can screw down our miniature motor bracket?*  
> *3. Do you also have **2 or 4 small self-tapping wood screws (around 10 mm length)** to fasten the bracket into the wood?*  
> *Here is the dimension drawing. Thank you very much, Sir!"*

---

## 5. Acceptance Criteria Checklist (Before Leaving Workshop)

- [ ] **Flatness:** Baseplate rests flat on a granite surface plate or workshop table with zero rock/wobble.
- [ ] **Dimensions:** Length and width are between $140\text{ mm}$ and $160\text{ mm}$.
- [ ] **Hole Spacing:** Bracket mounting holes align cleanly with the aluminum N20 U-bracket slots.
- [ ] **Screws Included:** 2 to 4 small wood screws received and tested for grip into the pilot holes.
