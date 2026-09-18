#!/usr/bin/env python3
"""
VibeGuard Interim Firmware Technical Specification & Demonstration Guide
Generates a 3-page, publication-grade PDF and companion Markdown document specifying:
- Page 1: Technical Overview & Verified Real-Time DSP Implementation
- Page 2: Review Objectives & Explicit Critical Anti-Scope Callout Box
- Page 3: Complete Hardware Pinout Table & Step-by-Step Operator Guide Table
"""

import cairo
import os

A4_WIDTH = 595.28
A4_HEIGHT = 841.89
MARGIN_LEFT = 42.0
MARGIN_RIGHT = 42.0
MARGIN_TOP = 44.0
MARGIN_BOTTOM = 44.0
USABLE_WIDTH = A4_WIDTH - MARGIN_LEFT - MARGIN_RIGHT
USABLE_HEIGHT = A4_HEIGHT - MARGIN_TOP - MARGIN_BOTTOM

# Color Palette
COLOR_NAVY = (0.10, 0.21, 0.36)       # #1A365D - Primary headings
COLOR_SLATE = (0.17, 0.42, 0.69)      # #2B6CB0 - Secondary headings
COLOR_CHARCOAL = (0.18, 0.22, 0.28)   # #2D3748 - Body text
COLOR_MUTED = (0.44, 0.50, 0.59)      # #718096 - Muted captions/footers
COLOR_BG_LIGHT = (0.96, 0.97, 0.98)   # #F7FAFC - Light container fill
COLOR_BORDER = (0.80, 0.84, 0.88)     # #CBD5E0 - Borders
COLOR_GREEN = (0.15, 0.55, 0.30)      # #276749 - Success/Healthy
COLOR_RED = (0.75, 0.15, 0.15)        # #C53030 - Danger/Alarm/Anti-Scope
COLOR_WHITE = (1.00, 1.00, 1.00)

class VibeGuardPDF:
    def __init__(self, filename):
        self.filename = filename
        self.surface = cairo.PDFSurface(filename, A4_WIDTH, A4_HEIGHT)
        self.cr = cairo.Context(self.surface)
        self.page = 1
        self.total_pages = 3
        self.y = MARGIN_TOP + 15.0

    def new_page(self):
        self.draw_footer()
        self.surface.show_page()
        self.page += 1
        self.draw_header()
        self.y = MARGIN_TOP + 15.0

    def draw_header(self):
        cr = self.cr
        cr.save()
        cr.set_source_rgb(*COLOR_NAVY)
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        cr.set_font_size(8.0)
        cr.move_to(MARGIN_LEFT, MARGIN_TOP - 14)
        cr.show_text("VIBEGUARD™ TECHNICAL SPECIFICATION | INTERIM DEMONSTRATOR FIRMWARE")
        
        cr.set_source_rgb(*COLOR_MUTED)
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
        cr.set_font_size(7.5)
        cr.move_to(A4_WIDTH - MARGIN_RIGHT - 100, MARGIN_TOP - 14)
        cr.show_text("DOC-ID: VG-FW-INT-01")
        
        cr.set_source_rgb(*COLOR_BORDER)
        cr.set_line_width(0.75)
        cr.move_to(MARGIN_LEFT, MARGIN_TOP - 7)
        cr.line_to(A4_WIDTH - MARGIN_RIGHT, MARGIN_TOP - 7)
        cr.stroke()
        cr.restore()

    def draw_footer(self):
        cr = self.cr
        cr.save()
        cr.set_source_rgb(*COLOR_BORDER)
        cr.set_line_width(0.75)
        cr.move_to(MARGIN_LEFT, A4_HEIGHT - MARGIN_BOTTOM + 12)
        cr.line_to(A4_WIDTH - MARGIN_RIGHT, A4_HEIGHT - MARGIN_BOTTOM + 12)
        cr.stroke()

        cr.set_source_rgb(*COLOR_MUTED)
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
        cr.set_font_size(7.5)
        cr.move_to(MARGIN_LEFT, A4_HEIGHT - MARGIN_BOTTOM + 24)
        cr.show_text("Confidential / Academic Review Demonstrator - Team VibeGuard - Amrita Vishwa Vidyapeetham")
        
        page_str = f"Page {self.page} of {self.total_pages}"
        cr.move_to(A4_WIDTH - MARGIN_RIGHT - 55, A4_HEIGHT - MARGIN_BOTTOM + 24)
        cr.show_text(page_str)
        cr.restore()

    def wrap_text(self, text, font_size, max_width, bold=False):
        cr = self.cr
        cr.save()
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD if bold else cairo.FONT_WEIGHT_NORMAL)
        cr.set_font_size(font_size)
        
        # Clean special chars that lack glyphs in Type 1 fonts
        clean = (text.replace("≈", "~")
                     .replace("µ", "u")
                     .replace("Ω", " Ohm")
                     .replace("±", "+/-")
                     .replace("—", " - ")
                     .replace("™", ""))
        
        paragraphs = clean.split("\n")
        lines = []
        for p in paragraphs:
            words = p.split(" ")
            curr = []
            for w in words:
                if not w:
                    continue
                test_str = " ".join(curr + [w]) if curr else w
                ext = cr.text_extents(test_str)
                if ext.width <= max_width:
                    curr.append(w)
                else:
                    if curr:
                        lines.append(" ".join(curr))
                        curr = [w]
                    else:
                        lines.append(w)
                        curr = []
            if curr:
                lines.append(" ".join(curr))
            elif not words:
                lines.append("")
        cr.restore()
        return lines

    def add_title(self, title, subtitle):
        self.draw_header()
        cr = self.cr
        cr.save()
        
        cr.set_source_rgb(*COLOR_SLATE)
        cr.rectangle(MARGIN_LEFT, self.y, USABLE_WIDTH, 3.5)
        cr.fill()
        self.y += 12.0
        
        cr.set_source_rgb(*COLOR_NAVY)
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        cr.set_font_size(16.0)
        cr.move_to(MARGIN_LEFT, self.y)
        cr.show_text(title)
        self.y += 15.0
        
        cr.set_source_rgb(*COLOR_SLATE)
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
        cr.set_font_size(9.5)
        cr.move_to(MARGIN_LEFT, self.y)
        cr.show_text(subtitle)
        self.y += 12.0
        cr.restore()

    def add_meta_box(self, meta_items):
        cr = self.cr
        cr.save()
        box_height = 42.0
        cr.set_source_rgb(*COLOR_BG_LIGHT)
        cr.rectangle(MARGIN_LEFT, self.y, USABLE_WIDTH, box_height)
        cr.fill()
        cr.set_source_rgb(*COLOR_BORDER)
        cr.set_line_width(0.75)
        cr.rectangle(MARGIN_LEFT, self.y, USABLE_WIDTH, box_height)
        cr.stroke()

        col_w = USABLE_WIDTH / float(len(meta_items))
        for i, (k, v) in enumerate(meta_items):
            x_pos = MARGIN_LEFT + 8.0 + i * col_w
            cr.set_source_rgb(*COLOR_MUTED)
            cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
            cr.set_font_size(7.0)
            cr.move_to(x_pos, self.y + 13.0)
            cr.show_text(k.upper())
            
            cr.set_source_rgb(*COLOR_CHARCOAL)
            cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
            cr.set_font_size(8.0)
            cr.move_to(x_pos, self.y + 27.0)
            cr.show_text(v)
            
        self.y += box_height + 12.0
        cr.restore()

    def add_heading_1(self, text):
        cr = self.cr
        cr.save()
        self.y += 4.0
        cr.set_source_rgb(*COLOR_NAVY)
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        cr.set_font_size(11.5)
        cr.move_to(MARGIN_LEFT, self.y)
        cr.show_text(text)
        self.y += 5.0
        
        cr.set_source_rgb(*COLOR_SLATE)
        cr.set_line_width(1.5)
        cr.move_to(MARGIN_LEFT, self.y)
        cr.line_to(MARGIN_LEFT + 40.0, self.y)
        cr.stroke()
        
        cr.set_source_rgb(*COLOR_BORDER)
        cr.set_line_width(0.5)
        cr.move_to(MARGIN_LEFT + 44.0, self.y)
        cr.line_to(A4_WIDTH - MARGIN_RIGHT, self.y)
        cr.stroke()
        
        self.y += 10.0
        cr.restore()

    def add_paragraph(self, text, bold_prefix=None, space_after=6.0):
        font_size = 8.5
        line_height = 11.5
        full_text = f"{bold_prefix} {text}" if bold_prefix else text
        lines = self.wrap_text(full_text, font_size, USABLE_WIDTH)
        
        cr = self.cr
        cr.save()
        for i, l in enumerate(lines):
            cr.move_to(MARGIN_LEFT, self.y)
            if i == 0 and bold_prefix:
                cr.set_source_rgb(*COLOR_NAVY)
                cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
                cr.set_font_size(font_size)
                prefix_str = bold_prefix + " "
                cr.show_text(prefix_str)
                ext = cr.text_extents(prefix_str)
                
                rest = l[len(prefix_str):]
                cr.set_source_rgb(*COLOR_CHARCOAL)
                cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
                cr.move_to(MARGIN_LEFT + ext.x_advance, self.y)
                cr.show_text(rest)
            else:
                cr.set_source_rgb(*COLOR_CHARCOAL)
                cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
                cr.set_font_size(font_size)
                cr.show_text(l)
            self.y += line_height
            
        self.y += space_after
        cr.restore()

    def add_bullet(self, bold_part, text_part, bullet_color=COLOR_SLATE):
        font_size = 8.0
        line_height = 11.0
        indent = 12.0
        content_w = USABLE_WIDTH - indent
        
        full_text = f"{bold_part} {text_part}"
        lines = self.wrap_text(full_text, font_size, content_w)
        
        cr = self.cr
        cr.save()
        cr.set_source_rgb(*bullet_color)
        cr.arc(MARGIN_LEFT + 4.5, self.y - 3.0, 1.8, 0, 2 * 3.14159)
        cr.fill()
        
        for i, l in enumerate(lines):
            cr.move_to(MARGIN_LEFT + indent, self.y)
            if i == 0:
                cr.set_source_rgb(*COLOR_NAVY)
                cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
                cr.set_font_size(font_size)
                b_str = bold_part + " "
                cr.show_text(b_str)
                ext = cr.text_extents(b_str)
                
                rest = l[len(b_str):]
                cr.set_source_rgb(*COLOR_CHARCOAL)
                cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
                cr.move_to(MARGIN_LEFT + indent + ext.x_advance, self.y)
                cr.show_text(rest)
            else:
                cr.set_source_rgb(*COLOR_CHARCOAL)
                cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
                cr.set_font_size(font_size)
                cr.show_text(l)
            self.y += line_height
        self.y += 2.0
        cr.restore()

    def add_callout_box(self, title, items, box_type="alert"):
        theme = {
            "alert": (COLOR_RED, (0.99, 0.94, 0.94)),
            "info": (COLOR_SLATE, COLOR_BG_LIGHT),
            "success": (COLOR_GREEN, (0.94, 0.98, 0.95))
        }[box_type]
        
        border_col, bg_col = theme
        font_size = 8.0
        line_height = 11.0
        
        total_h = 20.0
        computed_items = []
        for bold_t, body_t in items:
            lines = self.wrap_text(f"{bold_t} {body_t}", font_size, USABLE_WIDTH - 22.0)
            computed_items.append((bold_t, body_t, lines))
            total_h += len(lines) * line_height + 3.0
        total_h += 6.0
        
        cr = self.cr
        cr.save()
        
        cr.set_source_rgb(*bg_col)
        cr.rectangle(MARGIN_LEFT, self.y, USABLE_WIDTH, total_h)
        cr.fill()
        
        cr.set_source_rgb(*border_col)
        cr.rectangle(MARGIN_LEFT, self.y, 4.0, total_h)
        cr.fill()
        
        cr.set_source_rgb(*COLOR_BORDER)
        cr.set_line_width(0.75)
        cr.rectangle(MARGIN_LEFT, self.y, USABLE_WIDTH, total_h)
        cr.stroke()
        
        cr.set_source_rgb(*border_col)
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        cr.set_font_size(9.0)
        cr.move_to(MARGIN_LEFT + 10.0, self.y + 13.0)
        cr.show_text(title.upper())
        
        curr_y = self.y + 24.0
        for bold_t, body_t, lines in computed_items:
            cr.set_source_rgb(*border_col)
            cr.arc(MARGIN_LEFT + 12.0, curr_y - 3.0, 1.6, 0, 2*3.14159)
            cr.fill()
            
            for idx, ln in enumerate(lines):
                cr.move_to(MARGIN_LEFT + 20.0, curr_y)
                if idx == 0:
                    cr.set_source_rgb(*COLOR_NAVY)
                    cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
                    cr.set_font_size(font_size)
                    b_str = bold_t + " "
                    cr.show_text(b_str)
                    ext = cr.text_extents(b_str)
                    
                    cr.set_source_rgb(*COLOR_CHARCOAL)
                    cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
                    cr.move_to(MARGIN_LEFT + 20.0 + ext.x_advance, curr_y)
                    cr.show_text(ln[len(b_str):])
                else:
                    cr.set_source_rgb(*COLOR_CHARCOAL)
                    cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
                    cr.set_font_size(font_size)
                    cr.show_text(ln)
                curr_y += line_height
            curr_y += 3.0
            
        self.y += total_h + 10.0
        cr.restore()

    def add_table(self, headers, rows, col_ratios):
        font_size = 7.5
        line_height = 10.5
        col_widths = [USABLE_WIDTH * r for r in col_ratios]
        
        computed_rows = []
        for row in rows:
            max_lines = 1
            wrapped_cells = []
            for idx, cell in enumerate(row):
                w = col_widths[idx] - 8.0
                lines = self.wrap_text(str(cell), font_size, w)
                wrapped_cells.append(lines)
                if len(lines) > max_lines:
                    max_lines = len(lines)
            row_h = max(16.0, max_lines * line_height + 6.0)
            computed_rows.append((wrapped_cells, row_h))
            
        cr = self.cr
        cr.save()
        
        # Header
        cr.set_source_rgb(*COLOR_NAVY)
        cr.rectangle(MARGIN_LEFT, self.y, USABLE_WIDTH, 17.0)
        cr.fill()
        
        cr.set_source_rgb(*COLOR_WHITE)
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        cr.set_font_size(7.5)
        cur_x = MARGIN_LEFT
        for idx, h in enumerate(headers):
            cr.move_to(cur_x + 5.0, self.y + 11.5)
            cr.show_text(h.upper())
            cur_x += col_widths[idx]
        self.y += 17.0
        
        # Rows
        for r_idx, (wrapped_cells, r_h) in enumerate(computed_rows):
            if r_idx % 2 == 1:
                cr.set_source_rgb(*COLOR_BG_LIGHT)
                cr.rectangle(MARGIN_LEFT, self.y, USABLE_WIDTH, r_h)
                cr.fill()
                
            cr.set_source_rgb(*COLOR_BORDER)
            cr.set_line_width(0.5)
            cr.rectangle(MARGIN_LEFT, self.y, USABLE_WIDTH, r_h)
            cr.stroke()
            
            cur_x = MARGIN_LEFT
            for c_idx, lines in enumerate(wrapped_cells):
                cell_y = self.y + 9.0
                for ln in lines:
                    is_bold = (c_idx == 0)
                    is_green = ("GREEN" in ln or "NORMAL" in ln or "VERIFIED" in ln)
                    is_red = ("RED" in ln or "ALARM" in ln)
                    
                    if is_green:
                        cr.set_source_rgb(*COLOR_GREEN)
                        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
                    elif is_red:
                        cr.set_source_rgb(*COLOR_RED)
                        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
                    else:
                        cr.set_source_rgb(*COLOR_CHARCOAL)
                        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD if is_bold else cairo.FONT_WEIGHT_NORMAL)
                        
                    cr.set_font_size(font_size)
                    cr.move_to(cur_x + 5.0, cell_y)
                    cr.show_text(ln)
                    cell_y += line_height
                cur_x += col_widths[c_idx]
            self.y += r_h
            
        self.y += 10.0
        cr.restore()

    def finish(self):
        self.draw_footer()
        self.surface.finish()

def build_complete_documentation():
    pdf_path_doc = "/home/paradoxpete/Documents/PROJECT_ORGANIZED/VibeGuard_Interim_Firmware_Documentation.pdf"
    pdf_path_down = "/home/paradoxpete/Downloads/VibeGuard_Interim_Firmware_Documentation.pdf"
    md_path_doc = "/home/paradoxpete/Documents/PROJECT_ORGANIZED/VibeGuard_Interim_Firmware_Documentation.md"
    
    doc = VibeGuardPDF(pdf_path_doc)
    
    # =========================================================================
    # PAGE 1: Executive Summary & Active DSP Implementation
    # =========================================================================
    doc.add_title(
        "VIBEGUARD - INTERIM FIRMWARE SPECIFICATION",
        "Hardware Bring-Up, Real-Time DSP Telemetry, Demonstration Scope & Anti-Scope Specification"
    )
    
    doc.add_meta_box([
        ("Document ID", "VG-FW-INT-01"),
        ("Firmware Revision", "v1.0-INTERIM-DEMO"),
        ("Target MCU", "7Semi ESP32-DEVKIT-E"),
        ("Sensor Protocol", "ADXL345 SPI Mode 2"),
        ("Author / Team", "VibeGuard Project Team")
    ])
    
    doc.add_heading_1("1. Executive Summary & Context of Existence")
    doc.add_paragraph(
        "This specification establishes the technical baseline, operating principles, and rigorous operational boundaries for the interim demonstration firmware (VibeGuard_Presentation_Demo.ino). The software has been compiled and burned directly into the onboard non-volatile SPI flash memory (address 0x00010000) of the 7Semi ESP32-DEVKIT-E microcontroller to support the Semester First Review presentation.",
        bold_prefix="Purpose:"
    )
    doc.add_paragraph(
        "Because custom 3D-printed mechanical components (the FAB-01 eccentric rotor arm and FAB-02 rigid sensor bracket) are presently undergoing fabrication in the college FabLab, this firmware serves as a physical proof-of-concept. It bridges bare-metal hardware assembly with mathematical signal processing, proving genuine silicon sensor interfacing, rigorous electrical galvanic isolation, dynamic gravity DC bias removal, and ISO 10816-3 severity classification on real hardware without waiting for finished mechanical tooling."
    )
    
    doc.add_heading_1("2. What the Program IS Doing (Active Implementation Details)")
    doc.add_paragraph(
        "The flashed firmware is actively executing the following verifiable physical and digital operations in real time:",
        bold_prefix="Active Functions:"
    )
    
    doc.add_bullet(
        "1. Certified SPI Bus Interfacing (Mode 2):",
        "Communicates with the ADXL345 3-axis accelerometer over a 1 MHz 4-wire hardware SPI bus (GPIO 18 SCK, GPIO 19 MISO, GPIO 23 MOSI, GPIO 21 CS). Rigorous hardware audits verified that SPI Mode 2 (CPOL=1, CPHA=0) achieves 100% bit-perfect register write and read-back latching on this breakout module."
    )
    doc.add_bullet(
        "2. Genuine Silicon Verification:",
        "Queries register 0x00 at startup and halts until the authentic Analog Devices silicon identifier DEVID 0xE5 is received, preventing execution against disconnected or floating buses."
    )
    doc.add_bullet(
        "3. High-Rate Digital Acquisition:",
        "Configures the ADXL345 for 800 Hz Output Data Rate (BW_RATE = 0x0D, Nyquist frequency = 400 Hz) and Full-Resolution +/-16g measurement range (DATA_FORMAT = 0x0B, 3.9 mg/LSB scale factor)."
    )
    doc.add_bullet(
        "4. Synchronous Burst Transfers:",
        "Gathers real acceleration data in 128-sample windows (160 ms per analysis window) using multibyte burst reads (register 0x32 with Read [0x80] and Multibyte [0x40] bits asserted), completely eliminating register skew."
    )
    doc.add_bullet(
        "5. Dynamic DC Gravity Elimination:",
        "Dynamically calculates window mean acceleration across all 3 axes (X, Y, Z) and subtracts it from every instantaneous sample (dx = x - mean_x). This cleanly filters out the static 1.0g Earth gravity vector and physical bench tilt, isolating pure dynamic AC mechanical vibration."
    )
    doc.add_bullet(
        "6. Dynamic Vector RMS Calculation:",
        "Computes the true 3-axis geometric magnitude Root Mean Square (V_RMS) across the 128-point sample window using double-precision float Euclidean summation."
    )
    doc.add_bullet(
        "7. ISO 10816-3 Decision Engine:",
        "Evaluates V_RMS against an alarm threshold of 0.350g (boundary between ISO Class I/II acceptable vibration and unacceptable severity). Incorporates a 2-stage persistence debounce filter (K-of-M counter) to prevent transient mechanical bench noise from causing nuisance trips."
    )
    doc.add_bullet(
        "8. Autonomous Standalone Operation:",
        "Executes immediately upon receiving 5V USB power (from laptop, power bank, or phone charger). Powers the onboard tri-color LED solid GREEN for Good Health / Normal baseline, and switches to solid RED under anomaly conditions."
    )
    doc.add_bullet(
        "9. Dual Telemetry Streaming:",
        "Outputs both high-readability formatted diagnostic logs and high-speed Arduino Serial Plotter datagrams (>VRMS:...,AlarmThresh:...,State:...) over /dev/ttyUSB0 at 115200 baud."
    )

    # =========================================================================
    # PAGE 2: Review Objectives & Critical Anti-Scope Box
    # =========================================================================
    doc.new_page()
    
    doc.add_heading_1("3. What the Program IS SUPPOSED To Do (Review Objectives)")
    doc.add_paragraph(
        "For tomorrow's academic and faculty evaluation, the firmware is specifically tasked with meeting four core demonstration objectives:",
        bold_prefix="Evaluation Criteria:"
    )
    doc.add_bullet(
        "Objective A - Live Sensor & DSP Proof:",
        "Demonstrate to reviewers that the team has successfully brought up real physical sensors, established clean high-speed SPI communication, and validated real-time mathematical vibration DSP on an embedded 32-bit RTOS architecture."
    )
    doc.add_bullet(
        "Objective B - Healthy Baseline Verification:",
        "Show that under normal resting conditions or decoupled motor spinning, the baseline vibration rests at V_RMS ~ 0.017g, well within the ISO 10816-3 permissible envelope with a solid GREEN indicator."
    )
    doc.add_bullet(
        "Objective C - Multi-Channel Fault Injection:",
        "Provide interactive, verifiable means to simulate mechanical unbalance and trigger the ALARM condition (Solid RED LED + telemetry warning) without requiring physical unbalance weights (see Section 6)."
    )
    doc.add_bullet(
        "Objective D - Electrical Domain Isolation:",
        "Demonstrate that the 12V 2A motor drive circuit is 100% galvanically isolated from the sensitive 3.3V ESP32 logic, preventing inductive flyback spikes or brownout resets."
    )

    doc.add_heading_1("4. What the Program IS NOT (Explicit Anti-Scope)")
    doc.add_paragraph(
        "To ensure complete academic transparency and prevent misconceptions, the following boundaries define what this interim program is explicitly NOT doing:",
        bold_prefix="Scope Boundaries:"
    )
    
    doc.add_callout_box(
        "CRITICAL BOUNDARIES & EXPLICIT ANTI-SCOPE (WHAT THIS IS NOT)",
        [
            ("NOT the Frozen Production Firmware:", "This code is strictly an isolated scratch demonstrator (VibeGuard_Presentation_Demo.ino). It does NOT alter, overwrite, or merge into the frozen master firmware directory (07_SEMESTER_EXECUTION/03_Firmware_and_Simulation/VibeGuard_ESP32_Firmware/)."),
            ("NOT Physical Mass Unbalance:", "Because the FAB-01 eccentric rotor arm is not yet installed on the N20 motor shaft, the current bad health state is demonstrated via interactive mechanical tap or hardware button injection, NOT centrifugal mass displacement."),
            ("NOT Full FFT Spectral Decomposition:", "This demonstrator evaluates statistical time-domain Vector RMS. Full 512-point Fast Fourier Transform (FFT) for isolating 1X rotational frequency and harmonic bearing peaks is scheduled for Phase 4 after rigid mounting."),
            ("NOT Cloud / MQTT / IoT Connected:", "Wi-Fi transmission and MQTT cloud publishing are deliberately held dormant to prevent RF power bursts (500 mA) and ensure 100% stable, zero-latency execution on the podium without college Wi-Fi login issues."),
            ("NOT an Electrical Diagnostic Tool:", "It measures mechanical acceleration only; it does not sense motor armature current, winding thermal dissipation, or supply voltage ripple."),
            ("NOT a Synthetic Mock / PC Simulation:", "Unlike earlier Python test scripts, every single acceleration bit is physically acquired in real time from genuine ADXL345 MEMS silicon over the physical SPI bus.")
        ],
        box_type="alert"
    )
    
    doc.add_paragraph(
        "These boundaries guarantee that tomorrow's presentation accurately portrays current semester progress: 100% physical bring-up completed, DSP verified, and software architecture validated, awaiting final 3D mechanical press-fit parts for full unbalance characterization.",
        bold_prefix="Engineering Rigor Note:"
    )

    # =========================================================================
    # PAGE 3: Hardware Pinout & Operator Demonstration Guide
    # =========================================================================
    doc.new_page()
    
    doc.add_heading_1("5. Hardware Pinout & Wiring Interface Reference")
    doc.add_paragraph(
        "The following pinout reflects the physical bench assembly verified and active on the hardware carrier:",
        bold_prefix="Interface Mapping:"
    )
    
    headers = ["Signal", "ESP32 Pin", "Breadboard", "ADXL345 Pin", "Electrical Domain", "Function"]
    rows = [
        ["GND", "GND", "Blue Rail (-)", "Pin 1 (GND)", "3.3V Logic Ground", "Common reference"],
        ["VCC", "3.3V Out", "Red Rail (+)", "Pin 2 (VCC)", "3.3V Regulated (AMS1117)", "Sensor supply (140 uA)"],
        ["CS", "GPIO 21", "Col 22, Row F", "Pin 3 (CS)", "3.3V CMOS Logic", "SPI Chip Select (Active Low)"],
        ["SDO", "GPIO 19", "Col 25, Row F", "Pin 6 (SDO)", "3.3V CMOS Logic", "SPI MISO (Master In Slave Out)"],
        ["SDA", "GPIO 23", "Col 26, Row F", "Pin 7 (SDA)", "3.3V CMOS Logic", "SPI MOSI (Master Out Slave In)"],
        ["SCL", "GPIO 18", "Col 27, Row F", "Pin 8 (SCL)", "3.3V CMOS Logic", "SPI SCLK (1 MHz Mode 2)"],
        ["LED GREEN", "GPIO 25", "Col 12, Row F", "Cathode (330 Ohm)", "3.3V PWM / Digital", "Normal State Indicator"],
        ["LED BLUE", "GPIO 26", "Col 14, Row F", "Cathode (330 Ohm)", "3.3V PWM / Digital", "Boot Self-Check Indicator"],
        ["LED RED", "GPIO 27", "Col 15, Row F", "Cathode (330 Ohm)", "3.3V PWM / Digital", "Alarm State Indicator"],
        ["BOOT BTN", "GPIO 0", "Onboard Button", "N/A", "Internal Pull-Up", "Interactive Fault Injection"],
        ["MOTOR +", "External 12V", "Screw Terminal", "N20 (+) Wire", "12V 2A Isolated Domain", "Isolated Drive Rail"],
        ["MOTOR -", "External GND", "Rocker / Fuse", "N20 (-) Wire", "12V 2A Isolated Domain", "1N4007 Clamped Return"]
    ]
    doc.add_table(headers, rows, [0.15, 0.15, 0.18, 0.18, 0.20, 0.14])

    doc.add_heading_1("6. Presentation Demonstration Script & Operator Guide")
    doc.add_paragraph(
        "Follow this exact step-by-step procedure during tomorrow's presentation to demonstrate complete system capability:",
        bold_prefix="Demonstration Flow:"
    )
    
    op_headers = ["Phase", "Operator Action", "Telemetry Output", "Visual LED", "Reviewer Takeaway"]
    op_rows = [
        [
            "1. Cold Boot",
            "Plug 5V USB cable into ESP32",
            "[SENSOR] ADXL345 DEVID: 0xE5 ... VERIFIED\nPOWER_CTL=0x08, DATA_FORMAT=0x0B",
            "Solid BLUE (0.5s)\nthen Solid GREEN",
            "MCU boots from internal flash; verifies silicon over Mode 2 SPI."
        ],
        [
            "2. Baseline Good Health",
            "Motor running or bench resting",
            ">VRMS:0.017,AlarmThresh:0.35,State:0\nStatus: [NORMAL / GOOD HEALTH]",
            "Solid GREEN",
            "Proves dynamic DC gravity removal and smooth Class I/II baseline."
        ],
        [
            "3. Physical Vibration Tap",
            "Gently tap bench near sensor",
            ">VRMS:0.420,AlarmThresh:0.35,State:1\nStatus: [ALARM / UNHEALTHY]",
            "Solid RED",
            "Proves physical dynamic sensing and ISO 10816-3 thresholding."
        ],
        [
            "4. Electronic Fault Injection",
            "Press & hold ESP32 BOOT button (GPIO 0)",
            ">VRMS:0.719,AlarmThresh:0.35,State:1\nStatus: [ALARM / UNHEALTHY] <-- [BOOT]",
            "Solid RED",
            "Demonstrates simulated rotor unbalance (+0.70g) without 3D parts."
        ],
        [
            "5. Recovery",
            "Release BOOT button",
            ">VRMS:0.018,AlarmThresh:0.35,State:0\nStatus: [NORMAL / GOOD HEALTH]",
            "Solid GREEN",
            "Validates 2-stage persistence debounce preventing nuisance trips."
        ],
        [
            "6. Serial Control (Optional)",
            "Type 'a' or 'n' in Serial Monitor",
            ">>> [SERIAL COMMAND] FORCED FAULT INJECTED / CLEARED <<<",
            "RED on 'a'\nGREEN on 'n'",
            "Demonstrates interactive supervisory command interface."
        ]
    ]
    doc.add_table(op_headers, op_rows, [0.15, 0.22, 0.28, 0.15, 0.20])

    doc.finish()
    print(f"Successfully generated 3-page PDF: {pdf_path_doc}")

    # Mirror to Downloads
    os.system(f"cp {pdf_path_doc} {pdf_path_down}")
    print(f"Successfully mirrored PDF to: {pdf_path_down}")

    # Generate matching Markdown document
    with open(md_path_doc, "w") as f:
        f.write("""# VibeGuard™ Technical Specification & Interim Firmware Documentation
**Document ID:** VG-FW-INT-01 | **Revision:** v1.0-INTERIM-DEMO | **Target MCU:** 7Semi ESP32-DEVKIT-E | **Sensor:** ADXL345 SPI Mode 2

---

## 1. Executive Summary & Context of Existence
This specification establishes the technical baseline, operating principles, and rigorous operational boundaries for the interim demonstration firmware (`VibeGuard_Presentation_Demo.ino`). The software has been compiled and burned directly into the onboard non-volatile SPI flash memory (`0x00010000`) of the 7Semi ESP32-DEVKIT-E microcontroller to support the Semester First Review presentation.

Because custom 3D-printed mechanical components (the FAB-01 eccentric rotor arm and FAB-02 rigid sensor bracket) are presently undergoing fabrication in the college FabLab, this firmware serves as a physical proof-of-concept. It bridges bare-metal hardware assembly with mathematical signal processing, proving genuine silicon sensor interfacing, rigorous electrical galvanic isolation, dynamic gravity DC bias removal, and ISO 10816-3 severity classification on real hardware without waiting for finished mechanical tooling.

---

## 2. What the Program IS Doing (Active Implementation Details)
The flashed firmware is actively executing the following verifiable physical and digital operations in real time:

1. **Certified SPI Bus Interfacing (Mode 2):** Communicates with the ADXL345 3-axis accelerometer over a 1 MHz 4-wire hardware SPI bus (`GPIO 18` SCK, `GPIO 19` MISO, `GPIO 23` MOSI, `GPIO 21` CS). Rigorous hardware audits verified that SPI Mode 2 (`CPOL=1, CPHA=0`) achieves 100% bit-perfect register write and read-back latching on this breakout module.
2. **Genuine Silicon Verification:** Queries register `0x00` at startup and halts until the authentic Analog Devices silicon identifier DEVID `0xE5` is received, preventing execution against disconnected or floating buses.
3. **High-Rate Digital Acquisition:** Configures the ADXL345 for 800 Hz Output Data Rate (`BW_RATE = 0x0D`, Nyquist frequency = 400 Hz) and Full-Resolution ±16g measurement range (`DATA_FORMAT = 0x0B`, 3.9 mg/LSB scale factor).
4. **Synchronous Burst Transfers:** Gathers real acceleration data in 128-sample windows (160 ms per analysis window) using multibyte burst reads (register `0x32` with Read `0x80` and Multibyte `0x40` bits asserted), completely eliminating register skew.
5. **Dynamic DC Gravity Elimination:** Dynamically calculates window mean acceleration across all 3 axes (X, Y, Z) and subtracts it from every instantaneous sample ($dx = x - \bar{x}$). This cleanly filters out the static 1.0g Earth gravity vector and physical bench tilt, isolating pure dynamic AC mechanical vibration.
6. **Dynamic Vector RMS Calculation:** Computes the true 3-axis geometric magnitude Root Mean Square ($V_{\\text{RMS}}$) across the 128-point sample window using double-precision float Euclidean summation:
   $$V_{\\text{RMS}} = \\sqrt{\\frac{1}{N} \\sum_{i=0}^{N-1} (dx_i^2 + dy_i^2 + dz_i^2)}$$
7. **ISO 10816-3 Decision Engine:** Evaluates $V_{\\text{RMS}}$ against an alarm threshold of $0.350\\text{g}$ (boundary between ISO Class I/II acceptable vibration and unacceptable severity). Incorporates a 2-stage persistence debounce filter (K-of-M counter) to prevent transient mechanical bench noise from causing nuisance trips.
8. **Autonomous Standalone Operation:** Executes immediately upon receiving 5V USB power (from laptop, power bank, or phone charger). Powers the onboard tri-color LED solid **GREEN** for Good Health / Normal baseline, and switches to solid **RED** under anomaly conditions.
9. **Dual Telemetry Streaming:** Outputs both high-readability formatted diagnostic logs and high-speed Arduino Serial Plotter datagrams (`>VRMS:...,AlarmThresh:...,State:...`) over `/dev/ttyUSB0` at 115200 baud.

---

## 3. What the Program IS SUPPOSED To Do (Review Objectives)
For tomorrow's academic and faculty evaluation, the firmware is specifically tasked with meeting four core demonstration objectives:

* **Objective A — Live Sensor & DSP Proof:** Demonstrate to reviewers that the team has successfully brought up real physical sensors, established clean high-speed SPI communication, and validated real-time mathematical vibration DSP on an embedded 32-bit RTOS architecture.
* **Objective B — Healthy Baseline Verification:** Show that under normal resting conditions or decoupled motor spinning, the baseline vibration rests at $V_{\\text{RMS}} \\approx 0.017\\text{g}$, well within the ISO 10816-3 permissible envelope with a solid GREEN indicator.
* **Objective C — Multi-Channel Fault Injection:** Provide interactive, verifiable means to simulate mechanical unbalance and trigger the ALARM condition (Solid RED LED + telemetry warning) without requiring physical unbalance weights.
* **Objective D — Electrical Domain Isolation:** Demonstrate that the 12V 2A motor drive circuit is 100% galvanically isolated from the sensitive 3.3V ESP32 logic, preventing inductive flyback spikes or brownout resets.

---

## 4. What the Program IS NOT (Explicit Anti-Scope)

> ### ⚠️ CRITICAL BOUNDARIES & EXPLICIT ANTI-SCOPE (WHAT THIS IS NOT)
> 1. **NOT the Frozen Production Firmware:** This code is strictly an isolated scratch demonstrator (`VibeGuard_Presentation_Demo.ino`). It does NOT alter, overwrite, or merge into the frozen master firmware directory (`07_SEMESTER_EXECUTION/03_Firmware_and_Simulation/VibeGuard_ESP32_Firmware/`).
> 2. **NOT Physical Mass Unbalance:** Because the FAB-01 eccentric rotor arm is not yet installed on the N20 motor shaft, the current bad health state is demonstrated via interactive mechanical tap or hardware button injection, NOT centrifugal mass displacement.
> 3. **NOT Full FFT Spectral Decomposition:** This demonstrator evaluates statistical time-domain Vector RMS. Full 512-point Fast Fourier Transform (FFT) for isolating 1X rotational frequency and harmonic bearing peaks is scheduled for Phase 4 after rigid mounting.
> 4. **NOT Cloud / MQTT / IoT Connected:** Wi-Fi transmission and MQTT cloud publishing are deliberately held dormant to prevent RF power bursts (500 mA) and ensure 100% stable, zero-latency execution on the podium without college Wi-Fi login issues.
> 5. **NOT an Electrical Diagnostic Tool:** It measures mechanical acceleration only; it does not sense motor armature current, winding thermal dissipation, or supply voltage ripple.
> 6. **NOT a Synthetic Mock / PC Simulation:** Unlike earlier Python test scripts, every single acceleration bit is physically acquired in real time from genuine ADXL345 MEMS silicon over the physical SPI bus.

---

## 5. Hardware Pinout & Wiring Interface Reference

| Signal | ESP32 Pin | Breadboard Location | ADXL345 Pin | Electrical Domain | Function / Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GND** | `GND` | Blue Rail (-) | Pin 1 (GND) | 3.3V Logic Ground | Common circuit ground reference |
| **VCC** | `3.3V Out` | Red Rail (+) | Pin 2 (VCC) | 3.3V Regulated (AMS1117) | Sensor supply voltage (140 µA) |
| **CS** | `GPIO 21` | Col 22, Row F | Pin 3 (CS) | 3.3V CMOS Logic | Hardware SPI Chip Select (Active Low) |
| **SDO** | `GPIO 19` | Col 25, Row F | Pin 6 (SDO) | 3.3V CMOS Logic | Hardware SPI MISO |
| **SDA** | `GPIO 23` | Col 26, Row F | Pin 7 (SDA) | 3.3V CMOS Logic | Hardware SPI MOSI |
| **SCL** | `GPIO 18` | Col 27, Row F | Pin 8 (SCL) | 3.3V CMOS Logic | Hardware SPI SCLK (1 MHz Mode 2) |
| **LED GREEN**| `GPIO 25` | Col 12, Row F | Cathode (330 Ω) | 3.3V PWM / Digital | Normal State Indicator |
| **LED BLUE** | `GPIO 26` | Col 14, Row F | Cathode (330 Ω) | 3.3V PWM / Digital | Boot Self-Check Indicator |
| **LED RED** | `GPIO 27` | Col 15, Row F | Cathode (330 Ω) | 3.3V PWM / Digital | Alarm State Indicator |
| **BOOT BTN** | `GPIO 0` | Onboard Button | N/A | Internal Pull-Up | Interactive Fault Injection |
| **MOTOR +** | External 12V | Screw Terminal | N20 (+) Wire | 12V 2A Isolated Domain | Galvanically isolated drive rail |
| **MOTOR -** | External GND | Rocker / Fuse | N20 (-) Wire | 12V 2A Isolated Domain | 1N4007 Clamped Return |

---

## 6. Presentation Demonstration Script & Operator Guide

| Phase | Operator Action | Telemetry Output (Serial 115200) | Visual LED | Reviewer Takeaway |
| :--- | :--- | :--- | :--- | :--- |
| **1. Cold Boot** | Plug 5V USB cable into ESP32 | `[SENSOR] ADXL345 DEVID: 0xE5 ... VERIFIED`<br>`POWER_CTL=0x08, DATA_FORMAT=0x0B` | Solid BLUE (0.5s)<br>then Solid **GREEN** | MCU boots from internal flash; establishes Mode 2 SPI. |
| **2. Baseline Good Health** | Motor running or bench resting | `>VRMS:0.017,AlarmThresh:0.35,State:0`<br>`Status: [NORMAL / GOOD HEALTH]` | Solid **GREEN** | Proves dynamic DC gravity removal and smooth baseline. |
| **3. Physical Vibration Tap** | Gently tap bench near sensor | `>VRMS:0.420,AlarmThresh:0.35,State:1`<br>`Status: [ALARM / UNHEALTHY]` | Solid **RED** | Proves physical dynamic sensing and ISO 10816-3 limits. |
| **4. Fault Injection** | Press & hold ESP32 `BOOT` button (GPIO 0) | `>VRMS:0.719,AlarmThresh:0.35,State:1`<br>`Status: [ALARM / UNHEALTHY] <-- [BOOT]` | Solid **RED** | Demonstrates simulated rotor unbalance (+0.70g) without 3D parts. |
| **5. Recovery** | Release `BOOT` button | `>VRMS:0.018,AlarmThresh:0.35,State:0`<br>`Status: [NORMAL / GOOD HEALTH]` | Solid **GREEN** | Validates 2-stage persistence debounce preventing nuisance trips. |
| **6. Serial Control** | Type `'a'` or `'n'` in Serial Monitor | `>>> [SERIAL COMMAND] FORCED FAULT INJECTED / CLEARED <<<` | **RED** on `'a'`<br>**GREEN** on `'n'` | Demonstrates interactive supervisory command interface. |
""")
    print(f"Successfully generated Markdown doc: {md_path_doc}")

if __name__ == "__main__":
    build_complete_documentation()
