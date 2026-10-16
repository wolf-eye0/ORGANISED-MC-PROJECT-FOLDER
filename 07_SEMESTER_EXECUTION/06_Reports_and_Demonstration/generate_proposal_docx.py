import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
import os

def set_cell_shading(cell, color_hex):
    tcPr = cell._element.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), color_hex)
    tcPr.append(shd)

def set_cell_margins(cell, top=60, bottom=60, left=100, right=100):
    tcPr = cell._element.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('w:top', top), ('w:bottom', bottom), ('w:left', left), ('w:right', right)]:
        node = OxmlElement(m)
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def make_row_cant_split(row):
    trPr = row._tr.get_or_add_trPr()
    trPr.append(OxmlElement('w:cantSplit'))

def create_proposal_docx(output_path):
    doc = docx.Document()

    # Page Margins: 0.75 inch for crisp layout
    for section in doc.sections:
        section.top_margin = Inches(0.7)
        section.bottom_margin = Inches(0.7)
        section.left_margin = Inches(0.75)
        section.right_margin = Inches(0.75)

    # Styles & Colors
    navy = RGBColor(11, 44, 90)
    emerald = RGBColor(16, 124, 65)
    charcoal = RGBColor(33, 37, 41)

    # ==========================================
    # PAGE 1: TITLE, TEAM BOX, SEC 1, SEC 2
    # ==========================================

    p_header = doc.add_paragraph()
    p_header.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r_track = p_header.add_run("VISHWAKARMA AWARDS 2026–27 | STAGE 1 PROPOSAL\nHOST INSTITUTE: IIT INDORE | THEME: AI IN HARDWARE & MANUFACTURING")
    r_track.font.size = Pt(8.5)
    r_track.font.bold = True
    r_track.font.color.rgb = emerald
    p_header.paragraph_format.space_after = Pt(4)

    p_title = doc.add_paragraph()
    r_title = p_title.add_run("VibeGuard: Ultra-Low-Cost Edge-Embedded Vibration Monitoring and Predictive Machine Diagnostics")
    r_title.font.size = Pt(17.5)
    r_title.font.bold = True
    r_title.font.color.rgb = navy
    p_title.paragraph_format.space_after = Pt(2)

    p_sub = doc.add_paragraph()
    r_sub = p_sub.add_run("Sub-Theme: Predictive Maintenance & Machine Diagnostics | Edge AI & On-Chip Processing")
    r_sub.font.size = Pt(10.5)
    r_sub.font.bold = True
    r_sub.font.color.rgb = emerald
    p_sub.paragraph_format.space_after = Pt(10)

    # Team Box Table (2x2)
    t_team = doc.add_table(rows=2, cols=2)
    t_team.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_team.autofit = False

    t_team.rows[0].cells[0].width = Inches(3.5)
    t_team.rows[0].cells[1].width = Inches(3.5)
    t_team.rows[1].cells[0].width = Inches(3.5)
    t_team.rows[1].cells[1].width = Inches(3.5)

    set_cell_shading(t_team.rows[0].cells[0], "F3F4F6")
    set_cell_shading(t_team.rows[0].cells[1], "F3F4F6")
    set_cell_shading(t_team.rows[1].cells[0], "FAFAFA")
    set_cell_shading(t_team.rows[1].cells[1], "FAFAFA")

    for r in t_team.rows:
        make_row_cant_split(r)
        for c in r.cells:
            set_cell_margins(c, top=60, bottom=60, left=100, right=100)

    p1 = t_team.rows[0].cells[0].paragraphs[0]
    p1.add_run("Team & Institutional Details").bold = True
    p1.runs[0].font.size = Pt(9.5)
    p2 = t_team.rows[0].cells[1].paragraphs[0]
    p2.add_run("Academic Context & Faculty Mentor").bold = True
    p2.runs[0].font.size = Pt(9.5)

    c0 = t_team.rows[1].cells[0].paragraphs[0]
    c0.add_run("• Team Name: Team AIGHT (VibeGuard)\n"
               "• Nihad P C (Team Lead / Integration & Evidence Lead)\n"
               "• Sreehari K (Firmware, Embedded DSP & Data Lead)\n"
               "• Amith Krishna Das (Hardware, Power, Rig & Safety Lead)\n"
               "• Sreeprada K S (Experimental Operations, Test & Inventory Coordinator)\n"
               "• Archa Pramod (Documentation, Communication & Demonstration Lead)")
    c0.runs[0].font.size = Pt(9.0)

    c1 = t_team.rows[1].cells[1].paragraphs[0]
    c1.add_run("• Faculty Mentor: Ms. Sagna L T (Assistant Professor)\n"
               "• Department: Department of Computer Science & Engineering\n"
               "• Academic Affiliation: APJ Abdul Kalam Technological University (KTU), Kerala\n"
               "• Technical Domain: Edge AI, Cyber-Physical Systems & Embedded Hardware\n"
               "• Target Unit Cost: Under ₹3,000 (~$35 USD)\n"
               "• Prototype Status: Bench-Validated Working Prototype")
    c1.runs[0].font.size = Pt(9.0)

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # 1. Title
    h1 = doc.add_heading(level=1)
    r1 = h1.add_run("1. Title of the Project / Product")
    r1.font.color.rgb = navy
    p_t = doc.add_paragraph()
    p_t.add_run("VibeGuard: Ultra-Low-Cost Edge-Embedded Vibration Monitoring and Predictive Machine Diagnostics System")
    p_t.paragraph_format.space_after = Pt(6)

    # 2. Problem Statement
    h2 = doc.add_heading(level=1)
    r2 = h2.add_run("2. Problem Statement")
    r2.font.color.rgb = navy
    p_box = doc.add_paragraph()
    r_ps = p_box.add_run(
        "“Unmonitored rotating machinery in small-scale industries and workshops suffers catastrophic mechanical breakdowns, costly production halts, and severe worker safety hazards due to the prohibitive cost (>₹50,000), network fragility, and complex installation of existing commercial vibration diagnostic systems.”"
    )
    r_ps.font.bold = True
    r_ps.font.italic = True
    r_ps.font.size = Pt(10.5)
    r_ps.font.color.rgb = RGBColor(180, 40, 20)
    p_box.paragraph_format.space_after = Pt(6)

    p_ps_exp = doc.add_paragraph()
    p_ps_exp.add_run(
        "In modern manufacturing plants, machine health revolves around rotating equipment: electric motors, water pumps, blowers, gearboxes, and spindle drives. Mechanical unbalance, shaft misalignment, bearing spalling, and looseness generate distinct periodic kinetic forces that grow exponentially with the square of speed (F = m · r · ω²). Today, over 85% of MSMEs (Micro, Small, and Medium Enterprises) in India cannot afford proprietary condition monitoring suites (such as SKF @ptitude or Bently Nevada 3500), forcing operators into reactive maintenance—waiting until machines physically smoke, screech, or seize. Furthermore, emerging IoT vibration pucks rely heavily on continuous Wi-Fi/cloud streaming, which is brittle on noisy industrial shop floors and introduces recurring cloud subscription expenses that small businesses reject."
    )
    p_ps_exp.paragraph_format.space_after = Pt(6)

    # PAGE BREAK TO PAGE 2
    doc.add_page_break()

    # ==========================================
    # PAGE 2: SEC 3 (SOLUTION PROPOSED) COMPLETE
    # ==========================================
    h3 = doc.add_heading(level=1)
    r3 = h3.add_run("3. Solution Proposed")
    r3.font.color.rgb = navy
    p_sol = doc.add_paragraph()
    p_sol.add_run(
        "VibeGuard is an autonomous, ₹3,000 edge-native vibration condition monitor and predictive diagnostic appliance designed to bolt directly onto rotating machinery frames. It combines high-bandwidth micro-electro-mechanical sensing (Analog Devices ADXL345), dual-core 32-bit embedded digital signal processing (ESP32-WROOM-32E), deterministic ISO 10816-3 severity logic, and an interactive 3D WebGL Digital Twin—delivering laboratory-grade vibration intelligence with 100% air-gapped local execution."
    )
    p_sol.paragraph_format.space_after = Pt(4)

    h3_sub = doc.add_heading("Key Technical Subsystems & Architecture:", level=2)
    h3_sub.paragraph_format.space_after = Pt(3)

    bullets = [
        ("High-Speed Synchronous SPI Sensing: ", "Employs an Analog Devices ADXL345 3-axis MEMS accelerometer communicating over dedicated 4-wire hardware SPI Mode 2 (CPOL=1, CPHA=0) at 1–2 MHz clock rates. Samples at 800 Hz Output Data Rate (ODR), delivering an un-aliased Nyquist bandwidth of 400 Hz that fully captures machine harmonics up to 40X rotational speed for standard 600–1200 RPM motors."),
        ("Authentic Silicon Hardware Auditing: ", "Firmware queries register 0x00 at cold boot and halts until authentic silicon identifier DEVID 0xE5 is validated, eliminating false execution on floating or disconnected buses."),
        ("In-Place Zero-Mean DC Elimination: ", "Raw MEMS accelerometers measure static 1.0g Earth gravity and tilt orientation. VibeGuard dynamically computes window mean acceleration across all three axes (X, Y, Z) and subtracts it in-place (dx_i = x_i - x_mean), isolating pure dynamic AC vibration oscillations without phase distortion."),
        ("Triaxial Euclidean Vector RMS Calculation: ", "Computes true geometric vibration energy across all 3 spatial axes: V_RMS = sqrt( (1/N) * sum(dx_i^2 + dy_i^2 + dz_i^2) ), matching standard physical kinetic energy metrics."),
        ("Impact Shock & Spall Extraction: ", "Calculates Peak Acceleration, Crest Factor (CF = a_peak / a_RMS), and 4th-Order Kurtosis across each 128/256-sample window to reliably flag impulsive bearing spalls and chipped gear teeth long before continuous RMS energy increases."),
        ("Hann-Windowed Cooley-Tukey Radix-2 Real FFT: ", "Pre-conditions vibration windows with a cosine Hann window to eliminate spectral leakage, executing an optimized in-place 256/512-point FFT on the Xtensa DSP core in <1.25 ms to isolate 1X rotational unbalance and 2X/3X harmonics."),
        ("Deterministic ISO 10816-3 Severity Decision Engine: ", "Maps dynamic Vector RMS into international industrial machinery severity zones: Zone A/B Normal (<0.35g, Solid Green LED), Zone C Warning (0.35g–0.70g, Amber LED), and Zone D Alarm (>0.70g, Solid Red LED + Piezo Buzzer)."),
        ("K-out-of-M Persistence Debounce Filter: ", "Requires qualifying abnormal vibration in K=3 out of M=5 consecutive analysis windows (1.6 seconds) before asserting Alarm state, completely rejecting nuisance false trips from accidental bench taps or dropped tools."),
        ("Galvanically Isolated Electrical Domain: ", "Maintains complete galvanic isolation (open-circuit infinity ohms) between 12V 2A motor drive rail (protected by 1A slow-blow fuse, SPST switch, and 1N4007 flyback suppression diode) and sensitive 3.3V ESP32 logic rail (buffered with 100 uF low-ESR bulk electrolytic and 100 nF bypass ceramic capacitors to eliminate brownout resets)."),
        ("Dual Telemetry & WebGL 3D Digital Twin: ", "Simultaneously outputs 115200 baud USB telemetry datagrams and synchronizes with a standalone Three.js 3D WebGL Digital Twin featuring procedural CAD assembly, real-time 3-axis oscilloscope, FFT spectrogram, and 2D/3D Lissajous shaft centerline orbit plotters.")
    ]
    for b_title, b_desc in bullets:
        bp = doc.add_paragraph(style='List Bullet')
        bp.paragraph_format.space_after = Pt(2.5)
        r_bt = bp.add_run(b_title)
        r_bt.bold = True
        r_bt.font.color.rgb = navy
        r_bt.font.size = Pt(8.5)
        r_bd = bp.add_run(b_desc)
        r_bd.font.size = Pt(8.5)

    # PAGE BREAK TO PAGE 3
    doc.add_page_break()

    # ==========================================
    # PAGE 3: FIGURE 1 + SEC 4 (IMPLEMENTATION PLAN)
    # ==========================================
    h_dsp = doc.add_heading("Embedded DSP Signal Processing Pipeline (Architecture):", level=2)
    h_dsp.paragraph_format.space_after = Pt(2)

    img1 = "/home/paradoxpete/Documents/PROJECT_ORGANIZED/05_TEACHER_AND_REVIEWS/04_First_Review_VibeGuard/02_Drafts_and_Working_Files/slide 15 diagrm.png"
    if os.path.exists(img1):
        p_img1 = doc.add_paragraph()
        p_img1.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img1.paragraph_format.space_after = Pt(2)
        p_img1.add_run().add_picture(img1, width=Inches(5.0))
        p_cap1 = doc.add_paragraph()
        p_cap1.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap1.paragraph_format.space_after = Pt(6)
        r_c1 = p_cap1.add_run("Figure 1: VibeGuard Detailed 6-Stage Embedded DSP and SPI Signal Processing Architecture")
        r_c1.font.size = Pt(8.0)
        r_c1.font.italic = True
        r_c1.font.bold = True

    h4 = doc.add_heading(level=1)
    r4 = h4.add_run("4. Implementation Plan")
    r4.font.color.rgb = navy
    h4.paragraph_format.space_after = Pt(2)

    p_imp = doc.add_paragraph()
    p_imp.add_run(
        "VibeGuard's deployment strategy is engineered for rapid, friction-free adoption across real-world operational environments without requiring plant downtime or specialized data science staff."
    )
    p_imp.paragraph_format.space_after = Pt(4)

    t_imp = doc.add_table(rows=4, cols=2)
    t_imp.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_imp.rows[0].cells[0].width = Inches(2.2)
    t_imp.rows[0].cells[1].width = Inches(4.8)
    t_imp.rows[1].cells[0].width = Inches(2.2)
    t_imp.rows[1].cells[1].width = Inches(4.8)
    t_imp.rows[2].cells[0].width = Inches(2.2)
    t_imp.rows[2].cells[1].width = Inches(4.8)
    t_imp.rows[3].cells[0].width = Inches(2.2)
    t_imp.rows[3].cells[1].width = Inches(4.8)

    set_cell_shading(t_imp.rows[0].cells[0], "F3F4F6")
    set_cell_shading(t_imp.rows[1].cells[0], "F3F4F6")
    set_cell_shading(t_imp.rows[2].cells[0], "F3F4F6")
    set_cell_shading(t_imp.rows[3].cells[0], "F3F4F6")

    for r in t_imp.rows:
        make_row_cant_split(r)

    t_imp.rows[0].cells[0].paragraphs[0].add_run("Target Beneficiaries").bold = True
    t_imp.rows[0].cells[1].paragraphs[0].add_run(
        "1. MSME Machine Shops & Fabricators: Small motor-driven lathes, CNC spindles, milling machines, and industrial air blowers operating without dedicated maintenance teams.\n"
        "2. University Laboratories & Technical Institutes: Precision mechanical testbeds, dynamometers, robotics benches, and student maker spaces requiring affordable condition monitoring.\n"
        "3. Agricultural & Rural Processing Units: Flour mills, rice hullers, and irrigation pump sets where mechanical breakdown halts village-level economic livelihoods."
    )

    t_imp.rows[1].cells[0].paragraphs[0].add_run("Deployment Environment").bold = True
    t_imp.rows[1].cells[1].paragraphs[0].add_run(
        "Direct inline magnetic or M3 rigid bolt mounting to motor bearing end-bells, pillow block bearings, and gearbox casings. Operates in electrically noisy industrial environments under 5V USB logic power, completely air-gapped from IT networks."
    )

    t_imp.rows[2].cells[0].paragraphs[0].add_run("Expected Outcomes").bold = True
    t_imp.rows[2].cells[1].paragraphs[0].add_run(
        "• Elimination of Unplanned Machine Stoppages: Early warning at Zone C prevents unexpected bearing seizure.\n"
        "• 90%+ Reduction in Monitoring Capital Cost: Equipping 10 machines costs <₹30,000 total (the price of a single commercial sensor probe).\n"
        "• Zero Subscription Overhead: No monthly cloud fees, API rate limits, or cellular SIM recurring costs."
    )

    t_imp.rows[3].cells[0].paragraphs[0].add_run("Phased Roadmap & Deliverables").bold = True
    t_imp.rows[3].cells[1].paragraphs[0].add_run(
        "• Phase 1 (Completed): Component procurement, dual-trial vernier caliper audit, master circuit schematic, modular C++ DSP firmware, Wokwi WASM simulation, and 3D WebGL Digital Twin.\n"
        "• Phase 2 (Active / Weeks 1–4): Acrylic baseplate drilling (1:1 sticker template), 3D printing of FAB-01 rotor arm and FAB-02 sensor bracket in college FabLab, full benchtop rig assembly.\n"
        "• Phase 3 (Weeks 5–8): Multi-fault calibration baseline collection, ISO 10816-3 threshold tuning on 12V 600 RPM motor rig, session-split held-out validation.\n"
        "• Phase 4 (Weeks 9–12): Field pilot testing in college engineering workshop, enclosure packaging, and final Vishwakarma Grand Finale demonstration."
    )
    for r in t_imp.rows:
        make_row_cant_split(r)
        for c in r.cells:
            set_cell_margins(c, top=35, bottom=35, left=70, right=70)
            for p in c.paragraphs:
                for run in p.runs:
                    run.font.size = Pt(8.0)

    # PAGE BREAK TO PAGE 4
    doc.add_page_break()

    # ==========================================
    # PAGE 4: SEC 5 (SAFETY AND EFFICIENCY ANALYSIS) COMPLETE
    # ==========================================
    h5 = doc.add_heading(level=1)
    r5 = h5.add_run("5. Safety and Efficiency Analysis")
    r5.font.color.rgb = navy
    h5.paragraph_format.space_after = Pt(2)

    p_safe = doc.add_paragraph()
    p_safe.add_run(
        "Industrial rotating equipment poses severe physical and electrical safety risks when operated unmonitored. VibeGuard is architected from the circuit level to physical plant enclosures with uncompromising safety and efficiency controls."
    )
    p_safe.paragraph_format.space_after = Pt(4)

    h5_sub1 = doc.add_heading("Safety Engineering Highlights:", level=2)
    h5_sub1.paragraph_format.space_after = Pt(3)

    s_bullets = [
        ("Galvanic Circuit Isolation: ", "The 12V 2A inductive motor circuit is completely separated from the 3.3V ESP32 microcontroller logic ground (measured open-circuit infinity ohms). Inductive back-EMF flyback spikes are clamped by a dedicated reverse-biased 1N4007 power diode directly across the motor terminals, preventing voltage spikes from reaching the microcontroller or host computer."),
        ("Inline Overcurrent & Inrush Protection: ", "A 5x20 mm inline screw-type fuse holder with a 1A 250V slow-blow cartridge fuse is wired into the positive 12V supply rail, protecting against rotor lockup or short circuits while absorbing inductive startup current inrush."),
        ("Worker Hazard Prevention: ", "In high-speed spinning shafts, uncorrected dynamic unbalance generates destructive centrifugal shear forces that cause coupling bolts to shear, releasing high-velocity projectiles. VibeGuard's instantaneous ISO Zone D alarm and persistence engine trigger visual/audible alarms within <1.6 seconds, permitting safe, controlled operator shutdown."),
        ("Rigid Anti-Vibration Baseplate Assembly: ", "The testbed utilizes an 8.80 mm dual-sheet acrylic stack (Plate 1: 4.20 mm, Plate 2: 4.60 mm) coupled with M3x20 mm Grade 8.8 hex bolts and DIN 985 Nyloc self-locking nuts (engaging 7.4 threads past the locking collar), ensuring zero bolt back-out during extended vibration runs."),
        ("Brownout Immunity: ", "A 100 uF low-ESR bulk electrolytic capacitor in parallel with a 100 nF high-frequency ceramic bypass capacitor across 3.3V/GND buffers against voltage dips below the 2.70V ESP32 brownout threshold (rst:0x10).")
    ]
    for b_title, b_desc in s_bullets:
        bp = doc.add_paragraph(style='List Bullet')
        bp.paragraph_format.space_after = Pt(3)
        r_bt = bp.add_run(b_title)
        r_bt.bold = True
        r_bt.font.color.rgb = navy
        r_bt.font.size = Pt(8.5)
        r_bd = bp.add_run(b_desc)
        r_bd.font.size = Pt(8.5)

    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    h5_sub2 = doc.add_heading("Operational Efficiency Gains:", level=2)
    h5_sub2.paragraph_format.space_after = Pt(3)

    e_bullets = [
        ("Reduction in Machine Downtime: ", "Detecting misalignment and unbalance weeks before mechanical failure allows maintenance to be scheduled during normal shift changeovers rather than halting critical production runs."),
        ("Energy Waste Mitigation: ", "Vibrating machines consume up to 8–15% more electrical energy due to frictional dissipation and eccentric loads. Aligning and balancing machinery via VibeGuard telemetry restores electrical efficiency."),
        ("Zero Bandwidth & Cloud Power Overhead: ", "Computing 800 Hz DSP locally on the dual-core Xtensa processor consumes <160 mA @ 3.3V (~0.5 Watts), avoiding continuous 500 mA Wi-Fi transmission bursts that congest industrial RF bands.")
    ]
    for b_title, b_desc in e_bullets:
        bp = doc.add_paragraph(style='List Bullet')
        bp.paragraph_format.space_after = Pt(3)
        r_bt = bp.add_run(b_title)
        r_bt.bold = True
        r_bt.font.color.rgb = emerald
        r_bt.font.size = Pt(8.5)
        r_bd = bp.add_run(b_desc)
        r_bd.font.size = Pt(8.5)

    # PAGE BREAK TO PAGE 5
    doc.add_page_break()

    # ==========================================
    # PAGE 5: FIGURE 2 + SEC 6 (SCALABILITY)
    # ==========================================
    h_elec = doc.add_heading("Certified Hardware Schematic & Electrical Domain Architecture:", level=2)
    h_elec.paragraph_format.space_after = Pt(2)

    img2 = "/home/paradoxpete/Documents/PROJECT_ORGANIZED/07_SEMESTER_EXECUTION/03_Hardware_and_CAD/VibeGuard_Master_Circuit_Schematic.png"
    if os.path.exists(img2):
        p_img2 = doc.add_paragraph()
        p_img2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img2.paragraph_format.space_after = Pt(2)
        p_img2.add_run().add_picture(img2, width=Inches(6.4))
        p_cap2 = doc.add_paragraph()
        p_cap2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap2.paragraph_format.space_after = Pt(6)
        r_c2 = p_cap2.add_run("Figure 2: Certified VibeGuard Master Electrical Schematic — Logic Domain A (ESP32 & ADXL345 4-Wire SPI), Isolated Power Domain B (12V Motor Drive, 1N4007 Flyback Clamp & 1A Fuse), and Verified Harness Matrix")
        r_c2.font.size = Pt(8.0)
        r_c2.font.italic = True
        r_c2.font.bold = True

    h6 = doc.add_heading(level=1)
    r6 = h6.add_run("6. Scalability and Future Development")
    r6.font.color.rgb = navy
    h6.paragraph_format.space_after = Pt(2)

    p_scale = doc.add_paragraph()
    p_scale.add_run(
        "VibeGuard's modular hardware and software architecture provides an expansive development runway, scaling seamlessly from a single benchtop appliance to a plant-wide industrial telemetry mesh."
    )
    p_scale.paragraph_format.space_after = Pt(3)

    h6_sub = doc.add_heading("Scalability Roadmap & Technical Extensions:", level=2)
    h6_sub.paragraph_format.space_after = Pt(2)

    sc_bullets = [
        ("TinyML On-Chip Anomaly Detection: ", "With the Level-1 RMS + persistence baseline frozen and proven, the secondary Xtensa core can host quantized Edge AI models (e.g., 1D Convolutional Autoencoders or One-Class SVMs via TensorFlow Lite for Microcontrollers) to classify specific defect signatures (bearing inner/outer race flaking BPFO/BPFI, gear mesh friction) without external servers."),
        ("Multi-Drop RS-485 / Modbus RTU Industrial Bus: ", "Adding a low-cost MAX485 transceiver enables daisy-chaining up to 32 VibeGuard pods across a 1,200-meter industrial plant floor, streaming register telemetry directly into existing factory SCADA and PLC systems without cloud dependencies."),
        ("ESP-NOW Ultra-Low-Latency Local Wireless Mesh: ", "For rotating assets where cabling is impractical, ESP-NOW peer-to-peer 2.4 GHz protocol enables battery-backed VibeGuard nodes to transmit 16-byte alert datagrams in <5 ms to a central shop-floor alarm console."),
        ("Universal Asset Adaptability: ", "While demonstrated on an N20 geared plant, VibeGuard's configurable Output Data Rate (up to 3200 Hz) and dynamic g-range (up to +/-16g) allow plug-and-play adaptation to heavy industrial centrifuges, slurry pumps, CNC machine tool spindles, and commercial HVAC fan banks.")
    ]
    for b_title, b_desc in sc_bullets:
        bp = doc.add_paragraph(style='List Bullet')
        bp.paragraph_format.space_after = Pt(2)
        r_bt = bp.add_run(b_title)
        r_bt.bold = True
        r_bt.font.color.rgb = navy
        r_bt.font.size = Pt(8.0)
        r_bd = bp.add_run(b_desc)
        r_bd.font.size = Pt(8.0)

    # PAGE BREAK TO PAGE 6
    doc.add_page_break()

    # ==========================================
    # PAGE 6: SEC 7 (INNOVATION ADVANTAGE) + SEC 8 TABLE
    # ==========================================
    h7 = doc.add_heading(level=1)
    r7 = h7.add_run("7. Innovation Advantage")
    r7.font.color.rgb = navy
    h7.paragraph_format.space_after = Pt(2)

    p_inno = doc.add_paragraph()
    p_inno.add_run(
        "VibeGuard fundamentally disrupts the industrial predictive maintenance market by proving that high-integrity vibration analytics do not require multi-lakh instrumentation racks or recurring cloud SaaS subscriptions."
    )
    p_inno.paragraph_format.space_after = Pt(4)

    # Comparison Table
    t_comp = doc.add_table(rows=6, cols=4)
    t_comp.alignment = WD_TABLE_ALIGNMENT.CENTER
    headers = ["Feature / Capability", "Traditional Industrial (SKF / Bently)", "Generic IoT Cloud Pucks", "VibeGuard (Our System)"]
    for col_idx, text in enumerate(headers):
        cell = t_comp.rows[0].cells[col_idx]
        cell.paragraphs[0].add_run(text).bold = True
        cell.paragraphs[0].runs[0].font.size = Pt(8.5)
        set_cell_shading(cell, "0B2C5A")
        cell.paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 255, 255)

    comp_data = [
        ("Hardware Unit Cost", "₹1,50,000 – ₹5,00,000+", "₹15,000 – ₹40,000", "Under ₹3,000 (~$35 USD)"),
        ("Recurring Subscription", "High Annual Support Fees", "₹500 – ₹2,000 / month / node", "₹0 (100% Free & Open Edge)"),
        ("Computing Location", "Central Server Rack / PC", "Cloud AWS / Azure / IoT Core", "Zero-Latency On-Chip DSP"),
        ("Network Dependency", "Heavy Coaxial / Ind. Ethernet", "Continuous High-Bandwidth Wi-Fi", "Zero (Air-Gapped Autonomous)"),
        ("Real-Time Visualization", "Proprietary Desktop Suites", "Web Graph Dashboard", "3D WebGL Digital Twin + Scope")
    ]

    for row_idx, row_values in enumerate(comp_data):
        row = t_comp.rows[row_idx + 1]
        for col_idx, text in enumerate(row_values):
            cell = row.cells[col_idx]
            p = cell.paragraphs[0]
            r = p.add_run(text)
            r.font.size = Pt(8.0)
            if col_idx == 3:
                r.bold = True
                set_cell_shading(cell, "ECFDF5")
            elif row_idx % 2 == 1:
                set_cell_shading(cell, "F9FAFB")

    for r in t_comp.rows:
        make_row_cant_split(r)
        for c in r.cells:
            set_cell_margins(c, top=35, bottom=35, left=70, right=70)

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # 8. Visual Impact & User Journey (Phase Comparison Table)
    h8 = doc.add_heading(level=1)
    r8 = h8.add_run("8. Visual Impact & User Journey (Operational Transformation)")
    r8.font.color.rgb = navy
    h8.paragraph_format.space_after = Pt(2)

    p_v_intro = doc.add_paragraph()
    p_v_intro.add_run(
        "To illustrate the tangible operational transformation achieved by deploying VibeGuard, the user experience is compared before and after adoption across an industrial plant floor."
    )
    p_v_intro.paragraph_format.space_after = Pt(4)

    t_vj = doc.add_table(rows=6, cols=3)
    t_vj.alignment = WD_TABLE_ALIGNMENT.CENTER
    vj_headers = ["Operational Phase", "BEFORE VibeGuard (Reactive Maintenance)", "AFTER VibeGuard (Continuous Edge Diagnostics)"]
    for col_idx, text in enumerate(vj_headers):
        cell = t_vj.rows[0].cells[col_idx]
        cell.paragraphs[0].add_run(text).bold = True
        cell.paragraphs[0].runs[0].font.size = Pt(8.5)
        set_cell_shading(cell, "1F2937")
        cell.paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 255, 255)

    vj_data = [
        ("1. Daily Machine Startup", "Operator boots motor blindly; baseline vibration is completely unknown; no quantitative health ledger exists.", "ESP32 boots in 0.5s, confirms authentic ADXL345 DEVID 0xE5, illuminates Solid Blue self-check, then turns Solid Green Normal."),
        ("2. Normal Machine Running", "Subtle misalignment or looseness goes unnoticed by human ear; internal fatigue builds silently inside raceways.", "800 Hz SPI sampling continuously computes Vector RMS (VRMS ~0.017g); live serial plot streams clean zero-mean oscillations."),
        ("3. Fault Onset (Unbalance)", "Eccentric wear or loose bolt occurs; machine vibrates heavily; human operator cannot determine severity.", "RMS crosses 0.35g into ISO Zone C Warning (Amber) -> crosses 0.70g into Alarm (Solid Red LED + Buzzer); 3-of-5 persistence eliminates false alarms."),
        ("4. Maintenance Action", "Operator runs machine until catastrophic seizure; coupling snaps, throwing debris; plant halts unexpectedly.", "Operator receives immediate local visual/audible alert; checks 3D Digital Twin showing 10 Hz 1X unbalance peak; schedules 30-min balance fix."),
        ("5. Financial & Safety Result", "₹1,50,000+ repair bill, 3 weeks lost production, severe worker safety hazard.", "Zero unplanned downtime, planned bolt retorquing/balancing, 100% worker safety, capital cost <₹3,000.")
    ]

    for row_idx, row_values in enumerate(vj_data):
        row = t_vj.rows[row_idx + 1]
        for col_idx, text in enumerate(row_values):
            cell = row.cells[col_idx]
            p = cell.paragraphs[0]
            r = p.add_run(text)
            r.font.size = Pt(8.0)
            if col_idx == 1:
                set_cell_shading(cell, "FEF2F2")
            elif col_idx == 2:
                set_cell_shading(cell, "ECFDF5")
                r.bold = True

    for r in t_vj.rows:
        make_row_cant_split(r)
        for c in r.cells:
            set_cell_margins(c, top=30, bottom=30, left=65, right=65)

    # PAGE BREAK TO PAGE 7
    doc.add_page_break()

    # ==========================================
    # PAGE 7: FIGURE 3 (USER JOURNEY STORYBOARD) + NARRATIVE
    # ==========================================
    h_vj_board = doc.add_heading("User Journey Storyboard & Strategic Economic ROI:", level=2)
    h_vj_board.paragraph_format.space_after = Pt(2)

    p_vj_narr = doc.add_paragraph()
    p_vj_narr.add_run(
        "The storyboard below captures the day-to-day workflow transformation for factory operators: eliminating sensory guesswork, preventing sudden catastrophic plant blackouts, and unlocking predictive machine diagnostics at a fraction of legacy capital costs."
    )
    p_vj_narr.paragraph_format.space_after = Pt(4)

    img3 = "/home/paradoxpete/Documents/PROJECT_ORGANIZED/07_SEMESTER_EXECUTION/06_Reports_and_Demonstration/VibeGuard_User_Journey_Before_After.png"
    if os.path.exists(img3):
        p_img3 = doc.add_paragraph()
        p_img3.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img3.paragraph_format.space_after = Pt(2)
        p_img3.add_run().add_picture(img3, width=Inches(6.4))
        p_cap3 = doc.add_paragraph()
        p_cap3.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap3.paragraph_format.space_after = Pt(8)
        r_c3 = p_cap3.add_run("Figure 3: VibeGuard User Journey Map & Operational Transformation — Before vs. After Implementation")
        r_c3.font.size = Pt(8.5)
        r_c3.font.italic = True
        r_c3.font.bold = True

    # Callout Box for Key ROI Takeaways
    t_roi = doc.add_table(rows=1, cols=3)
    t_roi.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_roi.rows[0].cells[0].width = Inches(2.3)
    t_roi.rows[0].cells[1].width = Inches(2.3)
    t_roi.rows[0].cells[2].width = Inches(2.3)
    set_cell_shading(t_roi.rows[0].cells[0], "F0FDF4")
    set_cell_shading(t_roi.rows[0].cells[1], "F0FDF4")
    set_cell_shading(t_roi.rows[0].cells[2], "F0FDF4")
    make_row_cant_split(t_roi.rows[0])

    r0 = t_roi.rows[0].cells[0].paragraphs[0]
    r0.add_run("Capital Cost Reduction\n").bold = True
    r0.add_run("98% CapEx Savings\n₹1,50,000+ vs. <₹3,000 unit cost")
    r0.runs[0].font.size = Pt(8.5)
    r0.runs[1].font.size = Pt(8.0)

    r1 = t_roi.rows[0].cells[1].paragraphs[0]
    r1.add_run("Recurring Fees\n").bold = True
    r1.add_run("₹0 Cloud Overhead\n100% On-Chip Air-Gapped DSP")
    r1.runs[0].font.size = Pt(8.5)
    r1.runs[1].font.size = Pt(8.0)

    r2 = t_roi.rows[0].cells[2].paragraphs[0]
    r2.add_run("Detection Latency\n").bold = True
    r2.add_run("<1.6 Seconds Alert\nImmediate local LED & buzzer alert")
    r2.runs[0].font.size = Pt(8.5)
    r2.runs[1].font.size = Pt(8.0)

    for c in t_roi.rows[0].cells:
        set_cell_margins(c, top=40, bottom=40, left=60, right=60)

    # PAGE BREAK TO PAGE 8
    doc.add_page_break()

    # ==========================================
    # PAGE 8: FIGURE 4 + STAGE 1 CERTIFICATION FOOTER
    # ==========================================
    h_mfg = doc.add_heading("Hardware Rig Fabrication & Mechanical Assembly Specification:", level=2)
    h_mfg.paragraph_format.space_after = Pt(2)

    img4 = "/home/paradoxpete/Documents/PROJECT_ORGANIZED/07_SEMESTER_EXECUTION/03_Hardware_and_CAD/VibeGuard_Mechanical_Rig_Engineering_Assembly.png"
    if os.path.exists(img4):
        p_img4 = doc.add_paragraph()
        p_img4.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img4.paragraph_format.space_after = Pt(2)
        p_img4.add_run().add_picture(img4, width=Inches(6.5))
        p_cap4 = doc.add_paragraph()
        p_cap4.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap4.paragraph_format.space_after = Pt(14)
        r_c4 = p_cap4.add_run("Figure 4: VibeGuard Mechanical Testbed Engineering Drawing — Panel A: 150×150 mm Acrylic Baseplate Drilling Blueprint & Matrix; Panel B: 3D CAD Projections of FAB-01 Rotor Arm & FAB-02 Sensor L-Bracket; Panel C: Structural Assembly & Power Isolation Protocol")
        r_c4.font.size = Pt(8.5)
        r_c4.font.italic = True
        r_c4.font.bold = True

    # Document Footer Summary
    p_end = doc.add_paragraph()
    p_end.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_end = p_end.add_run("— Certified VibeGuard Stage 1 Proposal Document for Vishwakarma Awards 2026–27 —")
    r_end.font.size = Pt(9.5)
    r_end.font.bold = True
    r_end.font.color.rgb = navy

    doc.save(output_path)
    print("Successfully generated Word DOCX at:", output_path)

if __name__ == '__main__':
    out_docx = "/home/paradoxpete/Downloads/VibeGuard_Vishwakarma_Awards_2026_Proposal_Official.docx"
    create_proposal_docx(out_docx)
    mirror_docx = "/home/paradoxpete/Documents/PROJECT_ORGANIZED/07_SEMESTER_EXECUTION/06_Reports_and_Demonstration/VibeGuard_Vishwakarma_Awards_2026_Proposal_Official.docx"
    create_proposal_docx(mirror_docx)
