#!/usr/bin/env python3
"""
Generates the VibeGuard Assembly, Sensitivity Tuning & Web Dashboard Handoff Guide PDF.
Standard Operating Procedure (SOP) & Teammate Handoff Manual.
"""

import os
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

PDF_PATH = "07_SEMESTER_EXECUTION/04_Firmware/VibeGuard_Assembly_Tuning_and_Dashboard_Handoff_Guide.pdf"

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, total_pages):
        self.saveState()
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#4A5568"))
        
        # Header (pages > 1)
        if self._pageNumber > 1:
            self.drawString(40, 808, "VIBEGUARD: ASSEMBLY, TUNING & DASHBOARD HANDOFF GUIDE")
            self.setFont("Helvetica", 8)
            self.drawRightString(555, 808, "SOP-ENG-2026-V1")
            self.setStrokeColor(colors.HexColor("#CBD5E0"))
            self.setLineWidth(0.75)
            self.line(40, 802, 555, 802)

        # Footer (all pages)
        self.setFont("Helvetica", 8)
        self.drawString(40, 30, "VibeGuard Project Team | College Engineering Lab Handoff Document")
        page_str = f"Page {self._pageNumber} of {total_pages}"
        self.drawRightString(555, 30, page_str)
        self.setStrokeColor(colors.HexColor("#CBD5E0"))
        self.setLineWidth(0.75)
        self.line(40, 42, 555, 42)
        
        self.restoreState()


def build_pdf():
    os.makedirs(os.path.dirname(PDF_PATH), exist_ok=True)
    doc = SimpleDocTemplate(
        PDF_PATH,
        pagesize=A4,
        leftMargin=40,
        rightMargin=40,
        topMargin=48,
        bottomMargin=50
    )

    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor('#1A365D'),
        spaceAfter=4
    )
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor('#2B6CB0'),
        spaceAfter=12
    )
    meta_style = ParagraphStyle(
        'MetaStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor('#4A5568')
    )
    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=16,
        textColor=colors.HexColor('#1A365D'),
        spaceBefore=12,
        spaceAfter=6,
        keepWithNext=True
    )
    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=colors.HexColor('#2D3748'),
        spaceBefore=8,
        spaceAfter=4,
        keepWithNext=True
    )
    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor('#2D3748'),
        spaceAfter=6
    )
    body_bold = ParagraphStyle(
        'Body_Bold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor('#1A202C')
    )
    bullet_style = ParagraphStyle(
        'Bullet_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor('#2D3748'),
        leftIndent=14,
        firstLineIndent=-10,
        spaceAfter=3
    )
    code_style = ParagraphStyle(
        'Code_Custom',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=8,
        leading=10.5,
        textColor=colors.HexColor('#1A202C'),
        backColor=colors.HexColor('#EDF2F7'),
        borderPadding=4,
        spaceAfter=6
    )
    callout_text = ParagraphStyle(
        'Callout_Text',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11.5,
        textColor=colors.HexColor('#1A202C')
    )
    table_cell = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=10.5,
        textColor=colors.HexColor('#2D3748')
    )
    table_cell_bold = ParagraphStyle(
        'TableCellBold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10.5,
        textColor=colors.HexColor('#1A202C')
    )

    story = []

    # Title Banner
    story.append(Paragraph("VIBEGUARD: ASSEMBLY, SENSITIVITY TUNING & DASHBOARD HANDOFF GUIDE", title_style))
    story.append(Paragraph("Standard Operating Procedure (SOP) & Lab Handoff Manual | Version 1.0", subtitle_style))
    
    meta_text = "<b>Author:</b> VibeGuard Systems Lead &nbsp;&nbsp;|&nbsp;&nbsp; <b>Date:</b> October 2026 &nbsp;&nbsp;|&nbsp;&nbsp; <b>Target Audience:</b> Assembly & Presentation Team &nbsp;&nbsp;|&nbsp;&nbsp; <b>Status:</b> Ready for Rig Assembly"
    story.append(Paragraph(meta_text, meta_style))
    story.append(Spacer(1, 6))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#1A365D'), spaceBefore=2, spaceAfter=8))

    # Executive Box
    exec_summary = [
        [
            Paragraph("<b>HANDOFF OBJECTIVE & EXECUTIVE SUMMARY:</b><br/>"
                      "All core firmware (ESP32 SPI driver, ISO 10816 DSP) and software (WebSocket bridge, animated web dashboard) are 100% verified and operating. "
                      "This document instructs the teammate handling physical acrylic assembly on <b>how to bolt down the rig properly</b>, <b>how to calibrate and log stepped unbalance data</b>, and <b>how to connect the hardware to the browser dashboard</b> for the viva demonstration.",
                      callout_text)
        ]
    ]
    t_exec = Table(exec_summary, colWidths=[515])
    t_exec.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#EBF8FF')),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#3182CE')),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(t_exec)
    story.append(Spacer(1, 8))

    # =========================================================================
    # PART 1: RIGID MECHANICAL ASSEMBLY PROCEDURE
    # =========================================================================
    story.append(Paragraph("PART 1: RIGID MECHANICAL ASSEMBLY PROCEDURE", h1_style))
    
    # Why Hand-Holding Dampens Vibration
    why_rigid = [
        [
            Paragraph("<b>CRITICAL ENGINEERING NOTE: WHY HAND-HOLDING SKEWS THE READINGS:</b><br/>"
                      "During preliminary testing, holding the motor and sensor stand with human fingers acted as a viscoelastic shock absorber. Human skin and muscle damp out high-frequency mechanical vibration, causing 2-bolt test readings to remain artificially low in the Yellow zone (~0.4g to 0.6g). Bolting the hardware firmly to the acrylic baseplate creates a <b>rigid mechanical transmission bridge</b> ($Motor \\rightarrow Bracket \\rightarrow Acrylic \\rightarrow Stand \\rightarrow Sensor$), producing sharp, repeatable, high-amplitude vibrations that reliably trigger the Red Alarm.",
                      callout_text)
        ]
    ]
    t_why = Table(why_rigid, colWidths=[515])
    t_why.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#FFF5F5')),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#E53E3E')),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(t_why)
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Step-by-Step Bolting Checklist:</b>", h2_style))
    story.append(Paragraph("&bull; <b>1. N20 Motor Bracket:</b> Fasten the steel N20 bracket to the acrylic baseplate using two M3 screws and M3 nuts. Tighten firmly with a screwdriver and pliers so the bracket cannot flex or wobble.", bullet_style))
    story.append(Paragraph("&bull; <b>2. ADXL345 Sensor Stand:</b> Bolt the 3D-printed rigid sensor bracket (FAB-02) onto the acrylic baseplate keeping exactly 20 mm parallel spacing from the motor face. Use M3 screws and nuts through the baseplate through-holes.", bullet_style))
    story.append(Paragraph("&bull; <b>3. Sensor PCB Mounting:</b> Mount the blue ADXL345 PCB upright onto the vertical flange of the sensor stand using M3 standoffs/screws. Ensure the PCB is perpendicular to the baseplate and firmly fastened.", bullet_style))
    story.append(Paragraph("&bull; <b>4. Rotor Arm Press-Fit:</b> Push the 3D-printed eccentric cam arm (FAB-01, 3.40 mm D-shaft) onto the N20 motor output shaft. Align the flat face with the motor D-flat. Push it until seated, leaving 1.0 mm clearance so it does not rub against the gearbox face.", bullet_style))
    story.append(Paragraph("&bull; <b>5. Bench Stability:</b> Place the acrylic baseplate on a flat, sturdy table. Place 4 small rubber feet, foam pads, or a mousepad beneath the acrylic corners to prevent the baseplate from sliding while motor spins.", bullet_style))
    story.append(Spacer(1, 6))

    # =========================================================================
    # PART 2: STEPPED UNBALANCE TESTING & SENSITIVITY TUNING
    # =========================================================================
    story.append(Paragraph("PART 2: FIRMWARE BENCHMARKING & SENSITIVITY TUNING", h1_style))
    story.append(Paragraph("The firmware loaded on the ESP32 (<code>VibeGuard_Benchmark_Logger.ino</code>) contains an interactive calibration and logging engine that computes AC Vector RMS over 128-sample windows (800 Hz ODR) with DC gravity bias removal.", body_style))

    story.append(Paragraph("<b>The 4-Stage Stepped Unbalance Protocol:</b>", h2_style))
    story.append(Paragraph("Open the Arduino IDE Serial Monitor (or terminal) at <b>115200 baud</b>. Execute the following sequential steps:", body_style))

    step_data = [
        [Paragraph("<b>Command</b>", table_cell_bold), Paragraph("<b>Test Stage</b>", table_cell_bold), Paragraph("<b>Mass Configuration</b>", table_cell_bold), Paragraph("<b>Expected VRMS</b>", table_cell_bold), Paragraph("<b>ISO Severity & LED</b>", table_cell_bold)],
        [Paragraph("Send <b>'0'</b>", table_cell_bold), Paragraph("Stage 0: Baseline", table_cell), Paragraph("Bare arm, 0 bolts/nuts (0.0g)", table_cell), Paragraph("0.080 - 0.120 g", table_cell), Paragraph("<b>Zone A (Good)</b> &bull; Solid Green", table_cell)],
        [Paragraph("Send <b>'1'</b>", table_cell_bold), Paragraph("Stage 1: Mild Unbal.", table_cell), Paragraph("1x M3x20 bolt alone (~2.5g)", table_cell), Paragraph("0.220 - 0.340 g", table_cell), Paragraph("<b>Zone B (Acceptable)</b> &bull; Green", table_cell)],
        [Paragraph("Send <b>'2'</b>", table_cell_bold), Paragraph("Stage 2: Mod. Unbal.", table_cell), Paragraph("M3 bolt + 1 nut (~3.4g)", table_cell), Paragraph("0.380 - 0.650 g", table_cell), Paragraph("<b>Zone C (Warning)</b> &bull; Solid Yellow", table_cell)],
        [Paragraph("Send <b>'3'</b>", table_cell_bold), Paragraph("Stage 3: Severe Unbal.", table_cell), Paragraph("M3 bolt + 2 nuts (~4.3g)", table_cell), Paragraph("0.750 - 1.300 g+", table_cell), Paragraph("<b>Zone D (Alarm)</b> &bull; Solid Red", table_cell)],
        [Paragraph("Send <b>'s'</b>", table_cell_bold), Paragraph("Generate Report", table_cell), Paragraph("All stages completed", table_cell), Paragraph("Full comparative ledger", table_cell), Paragraph("Prints Markdown Table for Viva", table_cell)],
        [Paragraph("Send <b>'c'</b>", table_cell_bold), Paragraph("Reset Ledger", table_cell), Paragraph("Clear all recorded stages", table_cell), Paragraph("--", table_cell), Paragraph("Resets baseline for new run", table_cell)]
    ]
    t_steps = Table(step_data, colWidths=[65, 105, 125, 95, 125])
    t_steps.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#EDF2F7')),
        ('BOX', (0, 0), (-1, -1), 0.75, colors.HexColor('#A0AEC0')),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#CBD5E0')),
        ('TOPPADDING', (0, 0), (-1, -1), 3.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(t_steps)
    story.append(Spacer(1, 6))

    # Sensitivity Tuning Guidelines
    story.append(Paragraph("<b>How to Tune Sensitivity Thresholds in Code (If Needed):</b>", h2_style))
    story.append(Paragraph("If you want the <b>Red Alarm LED</b> to trigger at a lower vibration level for your 2-nut test on acrylic, open <code>VibeGuard_Benchmark_Logger.ino</code> (lines 37-38) in Arduino IDE:", body_style))
    
    code_thresh = (
        "// DSP Window & ISO 10816 Thresholds in VibeGuard_Benchmark_Logger.ino\n"
        "#define RMS_WARN_LIMIT   0.35f   // ISO Zone B/C Warning threshold (Yellow LED: >= 0.35g)\n"
        "#define RMS_ALARM_LIMIT  0.70f   // ISO Zone C/D Alarm threshold   (Red LED:    >= 0.70g)\n"
        "\n"
        "// TUNING TIP: If 2 nuts produce ~0.55g on your acrylic setup and you want Red immediately:\n"
        "// Change RMS_ALARM_LIMIT to 0.50f or 0.55f, then re-upload with auto_flash_esp32.sh!"
    )
    story.append(Paragraph(code_thresh.replace("\n", "<br/>").replace(" ", "&nbsp;"), code_style))
    story.append(Spacer(1, 4))

    # =========================================================================
    # PART 3: CONNECTING TO THE LIVE WEB DASHBOARD
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("PART 3: CONNECTING TO THE LIVE WEB DASHBOARD", h1_style))
    
    # Golden Rule Warning Box
    rule_box = [
        [
            Paragraph("<b>CRITICAL GOLDEN RULE & PORT CONFIGURATION:</b><br/>"
                      "<b>YOU MUST CLOSE THE ARDUINO SERIAL MONITOR BEFORE STARTING THE DASHBOARD!</b><br/>"
                      "On Linux and Windows, a serial port (e.g. <code>/dev/ttyUSB0</code> or <code>COM5</code>) can only be opened by <b>one single application at a time</b>. If the Arduino IDE Serial Monitor is open, the web server will fail with <code>Resource busy (EBUSY)</code>. Close the monitor tab first!",
                      callout_text)
        ]
    ]
    t_rule = Table(rule_box, colWidths=[515])
    t_rule.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#FEFCBF')),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#D69E2E')),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(t_rule)
    story.append(Spacer(1, 8))

    story.append(Paragraph("<b>1. Start the Web Dashboard Server:</b>", h2_style))
    story.append(Paragraph("Open a terminal on the laptop and execute the following commands:", body_style))

    cmd_linux = (
        "# 1. Navigate to the dashboard directory:\n"
        "cd ~/Documents/PROJECT_ORGANIZED/07_SEMESTER_EXECUTION/04_Firmware/VibeGuard_Web_Dashboard\n\n"
        "# 2. Start the Node.js server with the ESP32 serial port:\n"
        "SERIAL_PORT=/dev/ttyUSB0 npm start\n"
        "# (Or use auto-detection: AUTO_SERIAL=true npm start)\n\n"
        "# Windows PowerShell alternative:\n"
        "# $env:SERIAL_PORT='COM5'; npm start"
    )
    story.append(Paragraph(cmd_linux.replace("\n", "<br/>").replace(" ", "&nbsp;"), code_style))

    story.append(Paragraph("<b>2. Open the Browser Interface:</b>", h2_style))
    story.append(Paragraph("Open Google Chrome, Chromium, or Firefox to the following URL:", body_style))
    story.append(Paragraph("👉 <b>Live Hardware Mode:</b> <code>http://127.0.0.1:8765/vibeguard-dashboard.html?source=live</code>", bullet_style))
    story.append(Paragraph("👉 <b>Offline Preview Mode:</b> <code>http://127.0.0.1:8765/vibeguard-dashboard.html?source=preview</code>", bullet_style))

    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>3. Presentation & Operation Features:</b>", h2_style))
    story.append(Paragraph("&bull; <b>Full-Screen Presentation Mode:</b> Press the <b>'P'</b> key on the keyboard to enter clean full-screen presentation mode for your viva presentation.", bullet_style))
    story.append(Paragraph("&bull; <b>Pause Button:</b> Click the pause icon in the top header to freeze waveform curves for professor inspection while background acquisition continues.", bullet_style))
    story.append(Paragraph("&bull; <b>Export Session CSV:</b> Click the blue <b>'Export session CSV'</b> button in the readings panel to download all logged timestamped data points as a <code>.csv</code> spreadsheet.", bullet_style))
    story.append(Paragraph("&bull; <b>Animated Digital Twin:</b> The isometric acrylic rig SVG visualizer shakes and changes color in real-time according to measured vibration severity.", bullet_style))

    story.append(Spacer(1, 8))

    # =========================================================================
    # PART 4: HARDWARE PINOUT & LED DIAGNOSTIC REFERENCE
    # =========================================================================
    story.append(Paragraph("PART 4: HARDWARE WIRING & STATUS LED REFERENCE", h1_style))
    
    pinout_data = [
        [Paragraph("<b>Signal</b>", table_cell_bold), Paragraph("<b>ESP32 GPIO</b>", table_cell_bold), Paragraph("<b>ADXL345 / Component</b>", table_cell_bold), Paragraph("<b>Functional Description</b>", table_cell_bold)],
        [Paragraph("<b>CS</b>", table_cell_bold), Paragraph("GPIO 21", table_cell), Paragraph("CS Pin (Pin 7)", table_cell), Paragraph("SPI Chip Select (Active LOW)", table_cell)],
        [Paragraph("<b>SCK</b>", table_cell_bold), Paragraph("GPIO 18", table_cell), Paragraph("SCL Pin (Pin 1)", table_cell), Paragraph("1 MHz Hardware SPI Clock (Mode 2)", table_cell)],
        [Paragraph("<b>MISO</b>", table_cell_bold), Paragraph("GPIO 19", table_cell), Paragraph("SDO Pin (Pin 2)", table_cell), Paragraph("Master In Slave Out (Sensor Data)", table_cell)],
        [Paragraph("<b>MOSI</b>", table_cell_bold), Paragraph("GPIO 23", table_cell), Paragraph("SDA Pin (Pin 3)", table_cell), Paragraph("Master Out Slave In (Commands)", table_cell)],
        [Paragraph("<b>VCC / GND</b>", table_cell_bold), Paragraph("3V3 / GND", table_cell), Paragraph("VCC / GND", table_cell), Paragraph("Regulated 3.3V Logic & Common Ground", table_cell)],
        [Paragraph("<b>LED Green</b>", table_cell_bold), Paragraph("GPIO 25", table_cell), Paragraph("RGB Green Pin", table_cell), Paragraph("Normal Vibration (< 0.35g VRMS)", table_cell)],
        [Paragraph("<b>LED Blue</b>", table_cell_bold), Paragraph("GPIO 26", table_cell), Paragraph("RGB Blue Pin", table_cell), Paragraph("Booting / 4-sec Calibration Average", table_cell)],
        [Paragraph("<b>LED Red</b>", table_cell_bold), Paragraph("GPIO 27", table_cell), Paragraph("RGB Red Pin", table_cell), Paragraph("Critical Unbalance Alarm (>= 0.70g)", table_cell)]
    ]
    t_pin = Table(pinout_data, colWidths=[70, 75, 120, 250])
    t_pin.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#EDF2F7')),
        ('BOX', (0, 0), (-1, -1), 0.75, colors.HexColor('#A0AEC0')),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#CBD5E0')),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(t_pin)
    story.append(Spacer(1, 8))

    # =========================================================================
    # PART 5: RAPID TROUBLESHOOTING MATRIX
    # =========================================================================
    story.append(Paragraph("PART 5: RAPID TROUBLESHOOTING MATRIX", h1_style))
    
    trouble_data = [
        [Paragraph("<b>Observed Symptom</b>", table_cell_bold), Paragraph("<b>Likely Root Cause</b>", table_cell_bold), Paragraph("<b>Prescribed Corrective Action</b>", table_cell_bold)],
        [
            Paragraph("<b>Port busy (EBUSY) error</b> when starting dashboard", table_cell_bold),
            Paragraph("Arduino IDE Serial Monitor is still running and locking <code>/dev/ttyUSB0</code>.", table_cell),
            Paragraph("Close the Serial Monitor window in Arduino IDE. Run <code>lsof /dev/ttyUSB0</code> to find and kill the locking PID.", table_cell)
        ],
        [
            Paragraph("<b>LED stays Yellow</b> during 2-bolt test instead of Red", table_cell_bold),
            Paragraph("Rig is held by hand, dampening vibration; or bolts are loose on acrylic.", table_cell),
            Paragraph("Firmly tighten all M3 screws on acrylic plate. If vibration is ~0.55g, adjust <code>RMS_ALARM_LIMIT</code> to 0.50f in firmware.", table_cell)
        ],
        [
            Paragraph("<b>Sensor flatlined / Blue search light</b>", table_cell_bold),
            Paragraph("ADXL345 jumper wire disconnected or CS wire loose.", table_cell),
            Paragraph("Verify DuPont wires: CS to GPIO 21, SCK to 18, MISO to 19, MOSI to 23. Check 3.3V rail voltage.", table_cell)
        ],
        [
            Paragraph("<b>Garbled characters in terminal</b> during motor start", table_cell_bold),
            Paragraph("Electrical brush noise (EMI) from 12V DC motor commutation.", table_cell),
            Paragraph("Normal transient behavior. Clean ASCII resumes automatically within 200 ms.", table_cell)
        ],
        [
            Paragraph("<b>Browser shows 'Bridge offline'</b>", table_cell_bold),
            Paragraph("Node.js server process stopped or port 8765 blocked.", table_cell),
            Paragraph("Run <code>SERIAL_PORT=/dev/ttyUSB0 npm start</code> in the dashboard folder. Check <code>http://127.0.0.1:8765/health</code>.", table_cell)
        ]
    ]
    t_trouble = Table(trouble_data, colWidths=[125, 140, 250])
    t_trouble.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#EDF2F7')),
        ('BOX', (0, 0), (-1, -1), 0.75, colors.HexColor('#A0AEC0')),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#CBD5E0')),
        ('TOPPADDING', (0, 0), (-1, -1), 3.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(t_trouble)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"[SUCCESS] PDF Generated successfully at: {PDF_PATH}")

if __name__ == "__main__":
    build_pdf()
