#!/usr/bin/env python3
"""
Generates the VibeGuard Mechanical Lab Field Guide & Fabrication Manual:
- Part 1: Acrylic Sandwich Drilling Protocol (Step-by-step, INDEX A rule, clamping, 2.5/3.3 mm drilling, no-glue rigidity, solvent welding).
- Part 2: Vernier Caliper Precision Measurement Guide (Anatomy, pitch formulas, component protocols, fillable recording ledger, CAD offsets).

4-page publication-grade, print-ready, monochrome/photocopy-optimized PDF.
"""

import cairo
import os
import math

A4_WIDTH = 595.28
A4_HEIGHT = 841.89
MARGIN_L = 36.0
MARGIN_R = 36.0
MARGIN_T = 30.0
MARGIN_B = 28.0
USABLE_W = A4_WIDTH - MARGIN_L - MARGIN_R

# Monochrome / Laser-Printer Friendly Palette
C_BLACK = (0.0, 0.0, 0.0)
C_DARK = (0.12, 0.12, 0.12)
C_GRAY = (0.35, 0.35, 0.35)
C_LIGHT_GRAY = (0.6, 0.6, 0.6)
C_LINE = (0.5, 0.5, 0.5)
C_BG_BOX = (0.96, 0.96, 0.96)
C_BG_HDR = (0.88, 0.88, 0.88)
C_RED = (0.8, 0.0, 0.0)


class LabManualPDF:
    def __init__(self, filename):
        self.filename = filename
        self.surface = cairo.PDFSurface(filename, A4_WIDTH, A4_HEIGHT)
        self.cr = cairo.Context(self.surface)

    def wrap_text(self, text, font_size, max_w, bold=False):
        self.cr.save()
        self.cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL,
                                 cairo.FONT_WEIGHT_BOLD if bold else cairo.FONT_WEIGHT_NORMAL)
        self.cr.set_font_size(font_size)
        words = text.split(" ")
        lines = []
        curr = []
        for w in words:
            if not w:
                continue
            test_line = " ".join(curr + [w]) if curr else w
            ext = self.cr.text_extents(test_line)
            if ext.width <= max_w:
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
        self.cr.restore()
        return lines

    def draw_header(self, page_num, title_text, subtitle_text):
        cr = self.cr
        cr.save()
        # Top banner line
        cr.set_source_rgb(*C_BLACK)
        cr.set_line_width(1.5)
        cr.move_to(MARGIN_L, MARGIN_T)
        cr.line_to(A4_WIDTH - MARGIN_R, MARGIN_T)
        cr.stroke()

        # College & Department line
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        cr.set_font_size(8.0)
        cr.set_source_rgb(*C_GRAY)
        cr.move_to(MARGIN_L, MARGIN_T + 12.0)
        cr.show_text("JYOTHI ENGINEERING COLLEGE • DEPARTMENT OF CYBER SECURITY & MECHANICAL LAB")
        page_str = f"PAGE {page_num} OF 4"
        ext = cr.text_extents(page_str)
        cr.move_to(A4_WIDTH - MARGIN_R - ext.width, MARGIN_T + 12.0)
        cr.show_text(page_str)

        # Title
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        cr.set_font_size(12.5)
        cr.set_source_rgb(*C_BLACK)
        cr.move_to(MARGIN_L, MARGIN_T + 27.0)
        cr.show_text(title_text)

        # Subtitle
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
        cr.set_font_size(8.0)
        cr.set_source_rgb(*C_DARK)
        cr.move_to(MARGIN_L, MARGIN_T + 39.0)
        cr.show_text(subtitle_text)

        # Bottom header line
        cr.set_source_rgb(*C_LINE)
        cr.set_line_width(0.75)
        cr.move_to(MARGIN_L, MARGIN_T + 44.0)
        cr.line_to(A4_WIDTH - MARGIN_R, MARGIN_T + 44.0)
        cr.stroke()
        cr.restore()
        return MARGIN_T + 52.0

    def draw_footer(self, page_num):
        cr = self.cr
        cr.save()
        cr.set_source_rgb(*C_LINE)
        cr.set_line_width(0.5)
        cr.move_to(MARGIN_L, A4_HEIGHT - MARGIN_B - 10.0)
        cr.line_to(A4_WIDTH - MARGIN_R, A4_HEIGHT - MARGIN_B - 10.0)
        cr.stroke()

        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
        cr.set_font_size(7.0)
        cr.set_source_rgb(*C_GRAY)
        cr.move_to(MARGIN_L, A4_HEIGHT - MARGIN_B)
        cr.show_text("VibeGuard Capstone Project • SOP-MECH-01 • Verified for Lab Execution • Date: 17/09/2026")

        pg_text = f"Page {page_num} of 4"
        ext = cr.text_extents(pg_text)
        cr.move_to(A4_WIDTH - MARGIN_R - ext.width, A4_HEIGHT - MARGIN_B)
        cr.show_text(pg_text)
        cr.restore()

    def draw_section_banner(self, y, num_str, title_str):
        cr = self.cr
        cr.save()
        box_h = 16.0
        cr.set_source_rgb(*C_BG_HDR)
        cr.rectangle(MARGIN_L, y, USABLE_W, box_h)
        cr.fill()

        cr.set_source_rgb(*C_BLACK)
        cr.set_line_width(0.75)
        cr.rectangle(MARGIN_L, y, USABLE_W, box_h)
        cr.stroke()

        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        cr.set_font_size(8.5)
        cr.move_to(MARGIN_L + 6.0, y + 11.5)
        cr.show_text(f"{num_str}  {title_str.upper()}")
        cr.restore()
        return y + box_h + 6.0

    def render_page_1(self):
        y = self.draw_header(1, "PART 1: ACRYLIC SANDWICH DRILLING MASTER PROTOCOL",
                             "Pre-Drilling Setup, Hole Locations, INDEX A Alignment Principle & Clamping Physics")
        cr = self.cr

        # Section 1.0: Baseplate Engineering Specifications & Hole Matrix
        y = self.draw_section_banner(y, "1.0", "Baseplate Engineering Specifications & 8-Hole Matrix")
        
        # Spec box
        box_h = 52.0
        cr.save()
        cr.set_source_rgb(*C_BG_BOX)
        cr.rectangle(MARGIN_L, y, USABLE_W, box_h)
        cr.fill()
        cr.set_source_rgb(*C_LINE)
        cr.set_line_width(0.5)
        cr.rectangle(MARGIN_L, y, USABLE_W, box_h)
        cr.stroke()

        specs_left = [
            ("Dimensions:", "150.0 mm × 150.0 mm × 10.0 mm (Dual 5.0 mm PMMA)"),
            ("Through-Holes:", "Exactly 8 holes • All finished to Ø3.3 mm"),
            ("Tooling Bits:", "Pilot: Ø2.5 mm HSS • Final: Ø3.3 mm HSS"),
            ("Crucial Warning:", "DO NOT use Ø3.0 mm bit! (Causes acrylic fracture)")
        ]
        specs_right = [
            ("Corner Standoffs (C1–C4):", "X=10, 140 mm; Y=10, 140 mm (Span 130×130 mm)"),
            ("Motor Mount (M1, M2):", "X=31.5, 48.5 mm; Y=55.0 mm (Pitch = 17.0 mm)"),
            ("Sensor Mount (S1, S2):", "X=76.5, 91.5 mm; Y=55.0 mm (Pitch = 15.0 mm)"),
            ("Bracket Clearance Gap:", "20.0 mm parallel gap between motor & sensor")
        ]
        
        col_w = USABLE_W / 2.0
        for i in range(4):
            sy = y + 10.0 + (i * 10.5)
            # Left
            lbl_l, val_l = specs_left[i]
            cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
            cr.set_font_size(7.0)
            cr.set_source_rgb(*C_BLACK)
            cr.move_to(MARGIN_L + 6.0, sy)
            cr.show_text(lbl_l)
            cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
            cr.set_source_rgb(*C_DARK)
            cr.move_to(MARGIN_L + 78.0, sy)
            cr.show_text(val_l)

            # Right
            lbl_r, val_r = specs_right[i]
            cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
            cr.set_font_size(7.0)
            cr.set_source_rgb(*C_BLACK)
            cr.move_to(MARGIN_L + col_w + 6.0, sy)
            cr.show_text(lbl_r)
            cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
            cr.set_source_rgb(*C_DARK)
            cr.move_to(MARGIN_L + col_w + 105.0, sy)
            cr.show_text(val_r)

        cr.restore()
        y += box_h + 8.0

        # Section 1.1: Lab Tooling & Equipment Requisition Checklist
        y = self.draw_section_banner(y, "1.1", "Mechanical Lab Tooling & PPE Requisition Checklist")
        
        tools_col1 = [
            "[  ] Bench drill press with chuck key & depth stop",
            "[  ] Ø2.5 mm HSS twist drill bit (sharp flutes for pilot)",
            "[  ] Ø3.3 mm HSS twist drill bit (for M3 clearance)",
            "[  ] Automatic center punch or hardened steel scriber",
            "[  ] Sacrificial backing board (Plywood / MDF >= 12 mm)"
        ]
        tools_col2 = [
            "[  ] 2x C-clamps or wood screw clamps (>= 75 mm throat)",
            "[  ] 1:1 scale drill template (verified with 50 mm bar)",
            "[  ] Masking tape or transparent adhesive tape",
            "[  ] Permanent fine marker (for INDEX A mark on both sheets)",
            "[  ] Safety goggles / eye protection (mandatory in lab)"
        ]
        cr.save()
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
        cr.set_font_size(7.2)
        for i in range(len(tools_col1)):
            ty = y + 9.0 + (i * 10.5)
            cr.set_source_rgb(*C_DARK)
            cr.move_to(MARGIN_L + 6.0, ty)
            cr.show_text(tools_col1[i])
            cr.move_to(MARGIN_L + col_w + 6.0, ty)
            cr.show_text(tools_col2[i])
        cr.restore()
        y += (len(tools_col1) * 10.5) + 12.0

        # Section 1.2: The "INDEX A" Alignment Principle
        y = self.draw_section_banner(y, "1.2", "The 'INDEX A' Alignment Principle (Why & How to Mark Both Sheets)")

        p1 = ("WHAT IS THE 'INDEX A' RULE? Acrylic sheet blanks cut in the workshop are never 100.00% geometrically symmetric. "
              "Furthermore, our 8-hole pattern is intentionally asymmetric: the motor mount sits at X=31.5 & 48.5 mm, the sensor "
              "mount at X=76.5 & 91.5 mm, and the breadboard zone is towards the rear. When you sandwich both 5 mm sheets together and "
              "drill all 8 holes in a single pass, the holes across both plates match each other with 100% concentricity IN THAT EXACT ORIENTATION.")

        p2 = ("WHY MUST YOU MARK BOTH SHEETS? If you unclamp the plates after drilling and later rotate the bottom sheet by 90° or 180°, "
              "or flip it upside down, NOT A SINGLE HOLE WILL ALIGN! The M3 bolts will bind or jam. Marking 'INDEX A' permanently establishes "
              "the identical reference corner on BOTH sheets so they can be separated, cleaned, and reassembled with zero error.")

        for p in [p1, p2]:
            lines = self.wrap_text(p, 7.2, USABLE_W)
            cr.save()
            cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
            cr.set_font_size(7.2)
            cr.set_source_rgb(*C_DARK)
            for ln in lines:
                cr.move_to(MARGIN_L + 4.0, y + 7.5)
                cr.show_text(ln)
                y += 9.0
            cr.restore()
            y += 2.0

        # Visual Diagram Box: Showing Stacked Sheets, Edge Marking & Top View
        diag_h = 98.0
        cr.save()
        cr.set_source_rgb(*C_BG_BOX)
        cr.rectangle(MARGIN_L, y, USABLE_W, diag_h)
        cr.fill()
        cr.set_source_rgb(*C_LINE)
        cr.set_line_width(0.5)
        cr.rectangle(MARGIN_L, y, USABLE_W, diag_h)
        cr.stroke()

        # Left Diagram: Side/Edge View of Clamped Stack
        dx = MARGIN_L + 14.0
        dy = y + 14.0
        # Sheet 1
        cr.set_source_rgb(0.92, 0.92, 0.92)
        cr.rectangle(dx, dy, 120.0, 15.0)
        cr.fill()
        cr.set_source_rgb(0.1, 0.1, 0.1)
        cr.set_line_width(0.8)
        cr.rectangle(dx, dy, 120.0, 15.0)
        cr.stroke()
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        cr.set_font_size(6.8)
        cr.move_to(dx + 6.0, dy + 10.5)
        cr.show_text("SHEET 1 (TOP 5 mm PMMA)")

        # Sheet 2
        cr.set_source_rgb(0.86, 0.86, 0.86)
        cr.rectangle(dx, dy + 15.0, 120.0, 15.0)
        cr.fill()
        cr.set_source_rgb(0.1, 0.1, 0.1)
        cr.set_line_width(0.8)
        cr.rectangle(dx, dy + 15.0, 120.0, 15.0)
        cr.stroke()
        cr.move_to(dx + 6.0, dy + 25.5)
        cr.show_text("SHEET 2 (BOTTOM 5 mm PMMA)")

        # Sacrificial wood backing
        cr.set_source_rgb(0.78, 0.72, 0.65)
        cr.rectangle(dx - 6.0, dy + 30.0, 136.0, 18.0)
        cr.fill()
        cr.set_source_rgb(0.1, 0.1, 0.1)
        cr.set_line_width(0.8)
        cr.rectangle(dx - 6.0, dy + 30.0, 136.0, 18.0)
        cr.stroke()
        cr.move_to(dx + 2.0, dy + 42.0)
        cr.show_text("SACRIFICIAL PLYWOOD BACKING")

        # INDEX A Slash across edge
        cr.set_source_rgb(*C_RED)
        cr.set_line_width(2.5)
        cr.move_to(dx + 4.0, dy - 4.0)
        cr.line_to(dx - 4.0, dy + 30.0)
        cr.stroke()
        cr.move_to(dx - 14.0, dy - 6.0)
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        cr.set_font_size(7.2)
        cr.show_text("INDEX A")

        # Clamp symbols
        cr.set_source_rgb(0.2, 0.2, 0.2)
        cr.set_line_width(1.0)
        cr.move_to(dx + 110.0, dy - 8.0)
        cr.line_to(dx + 110.0, dy + 52.0)
        cr.stroke()
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
        cr.set_font_size(6.5)
        cr.move_to(dx + 94.0, dy + 58.0)
        cr.show_text("[C-CLAMP]")

        # Middle Diagram: Top Face View showing corner slash
        mx = dx + 148.0
        my = y + 14.0
        cr.set_source_rgb(0.94, 0.94, 0.94)
        cr.rectangle(mx, my, 64.0, 64.0)
        cr.fill()
        cr.set_source_rgb(0.1, 0.1, 0.1)
        cr.set_line_width(0.8)
        cr.rectangle(mx, my, 64.0, 64.0)
        cr.stroke()

        # Draw diagonal slash in top-left corner
        cr.set_source_rgb(*C_RED)
        cr.set_line_width(2.0)
        cr.move_to(mx, my + 14.0)
        cr.line_to(mx + 14.0, my)
        cr.stroke()
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        cr.set_font_size(6.5)
        cr.move_to(mx + 2.0, my - 3.0)
        cr.show_text("INDEX A")

        # Draw 4 corner holes and center indication
        cr.set_source_rgb(0.3, 0.3, 0.3)
        cr.set_line_width(0.5)
        for hx, hy in [(mx+6, my+6), (mx+58, my+6), (mx+6, my+58), (mx+58, my+58)]:
            cr.arc(hx, hy, 2.0, 0, 2*math.pi)
            cr.stroke()
        cr.move_to(mx + 4.0, my + 72.0)
        cr.show_text("TOP VIEW (150×150 mm)")

        # Right Text: Step-by-step marking protocol
        rx = mx + 78.0
        marking_steps = [
            "HOW TO APPLY THE MARK IN 3 QUICK STEPS:",
            "1. Stack both 150×150 mm acrylic plates squarely with all edges flush.",
            "2. In the top-left corner, take a permanent fine marker and draw a bold",
            "   diagonal slash ACROSS THE SIDE EDGES OF BOTH SHEETS.",
            "3. Write 'INDEX A' on the top face of Sheet 1 AND on the face of Sheet 2.",
            "-> GUARANTEE: Even when sheets are separated, matching the 'INDEX A'",
            "   marks guarantees 100% hole concentricity and zero screw binding!"
        ]
        ry = y + 12.0
        for s in marking_steps:
            cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL,
                               cairo.FONT_WEIGHT_BOLD if s.startswith("HOW") or s.startswith("->") else cairo.FONT_WEIGHT_NORMAL)
            cr.set_font_size(6.8)
            cr.set_source_rgb(*C_BLACK if s.startswith("HOW") or s.startswith("->") else C_DARK)
            cr.move_to(rx, ry)
            cr.show_text(s)
            ry += 9.5
        cr.restore()
        y += diag_h + 8.0

        # Section 1.3: Clamping & Sacrificial Backing Setup
        y = self.draw_section_banner(y, "1.3", "Clamping & Sacrificial Backing Setup (Preventing Breakout Chipping)")
        
        setup_text = (
            "• BREAKOUT PREVENTION PHYSICS: Acrylic (PMMA) is an amorphous thermoplastic with low impact toughness. When a twist drill "
            "breaks through the bottom exit face, the cutting lips catch the unsupported thin membrane, exerting high localized tensile stress "
            "that shatters the underside in large cone-shaped craters ('breakout blowout'). Placing a flat scrap plywood or MDF board beneath "
            "the bottom acrylic sheet provides continuous solid backing, acting as a die to produce perfectly crisp, chip-free hole bottoms.\n"
            "• FIRM C-CLAMPING: Clamp the 3-layer sandwich (Wood Backing + Bottom Acrylic + Top Acrylic) firmly to the drill press table "
            "using at least two C-clamps. Place cardboard shims under clamp pads to prevent marring. NEVER shift or unclamp between passes!"
        )
        for para in setup_text.split("\n"):
            lines = self.wrap_text(para, 7.2, USABLE_W)
            cr.save()
            cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
            cr.set_font_size(7.2)
            cr.set_source_rgb(*C_DARK)
            for ln in lines:
                cr.move_to(MARGIN_L + 4.0, y + 7.5)
                cr.show_text(ln)
                y += 9.0
            cr.restore()
            y += 2.0

        # Section 1.4: Master 8-Hole Drilling Coordinates Matrix
        y = self.draw_section_banner(y, "1.4", "Master Baseplate 8-Hole Coordinates Reference Matrix")
        
        hole_headers = ["Hole ID", "Subsystem / Mounting Purpose", "X (mm)", "Y (mm)", "Pilot Bit", "Final Bit", "Fastener Specification"]
        col_wh = [44.0, 165.0, 42.0, 42.0, 52.0, 52.0, 126.0]
        
        hole_matrix = [
            ("C1", "Base Standoff (Front-Left)", "10.0", "10.0", "Ø2.5 mm", "Ø3.3 mm", "M3 × 20 mm bolt + DIN 125 washer"),
            ("C2", "Base Standoff (Front-Right)", "140.0", "10.0", "Ø2.5 mm", "Ø3.3 mm", "M3 × 20 mm bolt + DIN 125 washer"),
            ("C3", "Base Standoff (Rear-Left / INDEX A)", "10.0", "140.0", "Ø2.5 mm", "Ø3.3 mm", "M3 × 20 mm bolt + DIN 125 washer"),
            ("C4", "Base Standoff (Rear-Right)", "140.0", "140.0", "Ø2.5 mm", "Ø3.3 mm", "M3 × 20 mm bolt + DIN 125 washer"),
            ("M1", "N20 Motor Bracket (Left Hole)", "31.5", "55.0", "Ø2.5 mm", "Ø3.3 mm", "M3 × 16 mm bolt + washer"),
            ("M2", "N20 Motor Bracket (Right Hole)", "48.5", "55.0", "Ø2.5 mm", "Ø3.3 mm", "M3 × 16 mm bolt (Pitch = 17.0 mm)"),
            ("S1", "ADXL345 Bracket (Left Hole)", "76.5", "55.0", "Ø2.5 mm", "Ø3.3 mm", "M3 × 16 mm bolt + washer"),
            ("S2", "ADXL345 Bracket (Right Hole)", "91.5", "55.0", "Ø2.5 mm", "Ø3.3 mm", "M3 × 16 mm bolt (Pitch = 15.0 mm)")
        ]
        
        row_hh = 11.5
        cr.save()
        # Header
        cr.set_source_rgb(*C_BG_HDR)
        cr.rectangle(MARGIN_L, y + 2.0, USABLE_W, row_hh)
        cr.fill()
        cr.set_source_rgb(*C_BLACK)
        cr.set_line_width(0.5)
        cr.rectangle(MARGIN_L, y + 2.0, USABLE_W, row_hh)
        cr.stroke()

        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        cr.set_font_size(6.6)
        cx = MARGIN_L
        for idx, th in enumerate(hole_headers):
            cr.move_to(cx + 3.0, y + 10.5)
            cr.show_text(th)
            cx += col_wh[idx]
        y += row_hh + 2.0

        # Rows
        cr.set_font_size(6.4)
        for r_idx, r_data in enumerate(hole_matrix):
            if r_idx % 2 == 1:
                cr.set_source_rgb(0.98, 0.98, 0.98)
                cr.rectangle(MARGIN_L, y, USABLE_W, row_hh)
                cr.fill()

            cr.set_source_rgb(*C_LINE)
            cr.set_line_width(0.3)
            cr.move_to(MARGIN_L, y + row_hh)
            cr.line_to(MARGIN_L + USABLE_W, y + row_hh)
            cr.stroke()

            # Vertical grid lines
            vx = MARGIN_L
            for w in col_wh[:-1]:
                vx += w
                cr.move_to(vx, y)
                cr.line_to(vx, y + row_hh)
                cr.stroke()

            # Data
            cx = MARGIN_L
            for idx, c_val in enumerate(r_data):
                cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL,
                                   cairo.FONT_WEIGHT_BOLD if idx in [0, 4, 5] else cairo.FONT_WEIGHT_NORMAL)
                cr.set_source_rgb(*C_BLACK if idx in [0, 4, 5] else C_DARK)
                cr.move_to(cx + 3.0, y + 8.5)
                cr.show_text(c_val)
                cx += col_wh[idx]
            y += row_hh

        cr.restore()

        self.draw_footer(1)
        cr.show_page()

    def render_page_2(self):
        y = self.draw_header(2, "PART 1 (CONTINUED): DRILLING EXECUTION & RIGIDITY PROTOCOL",
                             "Two-Stage Drilling Passes, Deburring, Immediate Clamping & Solvent Bonding")
        cr = self.cr

        # Section 1.5: 4-Stage Precision Drilling Execution
        y = self.draw_section_banner(y, "1.5", "Step-by-Step 4-Stage Precision Drilling Execution")

        stages = [
            ("Stage 1: Center Punching & Indentation",
             "Tape the 1:1 scale drilling template onto the top acrylic sheet. Align crosshairs. Place the sharp tip of an automatic "
             "center punch or scriber precisely at each hole center. Apply light downward pressure to create a distinct conical prick dimple. "
             "This prevents the drill bit point from 'skating' or 'walking' across the slick acrylic surface. Repeat for all 8 holes."),
            ("Stage 2: Pilot Hole Drilling (Ø2.5 mm HSS Bit)",
             "Chuck the Ø2.5 mm bit into the bench drill press. Set spindle speed to 600–800 RPM. (Never use high speeds >1200 RPM, which "
             "frictionally overheat acrylic and cause melting). Use the 'pecking' feed technique: gently lower the bit 1–2 mm, retract slightly "
             "to evacuate white ribbon swarf, and re-enter. Drill completely through both sheets into the wood backing. Clear all chips."),
            ("Stage 3: Final Clearance Hole Boring (Ø3.3 mm HSS Bit)",
             "Chuck the Ø3.3 mm bit. Keep spindle speed at 600–800 RPM. Slowly lower the bit into each Ø2.5 mm pilot hole. The 3.3 mm bit "
             "acts as a precision reamer, cleanly enlarging the hole to the exact ISO 273 clearance dimension (3.30 mm). Maintain slow, uniform "
             "feed pressure without forcing. The bit will exit smoothly into the wood backing with zero chipping."),
            ("Stage 4: Deburring & Manual Edge Cleanup",
             "Unclamp the sandwich. Separate the two sheets. If you feel a slight raised edge around the hole mouths, take an oversized "
             "drill bit (Ø5.0 mm or Ø6.0 mm) in your BARE HAND (no power drill!) and lightly twist it 1–2 revolutions against the hole rim. "
             "This cuts a smooth 0.2 mm chamfer that strips burrs without altering the cylindrical bore diameter.")
        ]

        for st_title, st_desc in stages:
            cr.save()
            cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
            cr.set_font_size(7.8)
            cr.set_source_rgb(*C_BLACK)
            cr.move_to(MARGIN_L + 4.0, y + 7.5)
            cr.show_text(st_title)
            y += 9.5

            lines = self.wrap_text(st_desc, 7.2, USABLE_W - 8.0)
            cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
            cr.set_font_size(7.2)
            cr.set_source_rgb(*C_DARK)
            for ln in lines:
                cr.move_to(MARGIN_L + 12.0, y + 7.5)
                cr.show_text(ln)
                y += 9.0
            cr.restore()
            y += 3.0

        # Section 1.6: Immediate Rigidity Without Glue Today
        y = self.draw_section_banner(y, "1.6", "Immediate Mechanical Rigidity (No Glue Needed Today!)")
        
        rig_text = (
            "YOU DO NOT NEED GLUE TODAY TO RUN MOTOR VIBRATION EXPERIMENTS!\n"
            "• Sandwich Mechanical Bolting: Insert 4 standard M3 × 20 mm bolts with DIN 125 flat washers through corner holes C1, C2, C3, C4. "
            "Thread M3 nylon locknuts onto the bottom face and snug them down using a screwdriver and wrench.\n"
            "• Clamping Force Physics: Four M3 bolts torqued to normal hand tightness (~0.6 N·m) generate approximately 3,500 N (~350 kgf) "
            "of uniform compressive clamping force across the 150×150 mm baseplate. This creates massive frictional interlock between the two "
            "5 mm sheets, eliminating any relative slip or resonant flutter. The stack behaves as a 100% rigid monolithic 10 mm chassis!\n"
            "• Subsystem Mounting: Mount the N20 motor bracket (holes M1, M2) and ADXL345 bracket (holes S1, S2) with M3 × 16 mm bolts. "
            "You can begin data acquisition and FFT vibration testing immediately today without waiting for adhesives to cure."
        )
        for r_para in rig_text.split("\n"):
            is_bold = r_para.startswith("YOU DO NOT")
            lines = self.wrap_text(r_para, 7.2, USABLE_W, bold=is_bold)
            cr.save()
            cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL,
                               cairo.FONT_WEIGHT_BOLD if is_bold else cairo.FONT_WEIGHT_NORMAL)
            cr.set_font_size(7.2)
            cr.set_source_rgb(*C_BLACK if is_bold else C_DARK)
            for ln in lines:
                cr.move_to(MARGIN_L + 4.0, y + 7.5)
                cr.show_text(ln)
                y += 9.0
            cr.restore()
            y += 2.0

        # Section 1.7: Post-Drill Adhesive Sourcing & Capillary Welding
        y = self.draw_section_banner(y, "1.7", "Adhesive Sourcing & Post-Drill Capillary Solvent Welding Protocol")
        
        adh_text = (
            "• GOLD STANDARD: Dichloromethane (DCM / Methylene Chloride). Chemically dissolves PMMA surface polymer chains, fusing them "
            "into a monolithic, bubble-free, water-clear optical weld. Sourced from the College Chemistry Lab (request 15 mL) or local Acrylic "
            "Sign-Board fabricators in Cheruthuruthy / Shoranur.\n"
            "• CAPILLARY APPLICATION METHOD: Keep the two plates loosely bolted together with 'INDEX A' aligned. Fill a 2 mL medical syringe "
            "fitted with a fine blunt needle. Touch the needle tip along the perimeter seam between the two sheets. Capillary pressure will "
            "automatically pull the water-thin solvent inward across the entire interface within 3 seconds. Snug the corner bolts down. "
            "The weld reaches 80% handling strength in 15 minutes and achieves full cure in 24 hours.\n"
            "• WORKSHOP FALLBACK: Araldite Ultra Clear (2-part epoxy). Apply a paper-thin film between plates and clamp for 24 hours.\n"
            "• STRICT PROHIBITION: NEVER use Cyanoacrylate (Fevikwik / Super Glue). Rapid polymerization releases volatile vapors that cause "
            "permanent white crazing ('blooming'), severely embrittles PMMA, and shatters under dynamic motor vibration."
        )
        for a_para in adh_text.split("\n"):
            lines = self.wrap_text(a_para, 7.2, USABLE_W)
            cr.save()
            cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
            cr.set_font_size(7.2)
            cr.set_source_rgb(*C_DARK)
            for ln in lines:
                cr.move_to(MARGIN_L + 4.0, y + 7.5)
                cr.show_text(ln)
                y += 9.0
            cr.restore()
            y += 2.0

        # Section 1.8: Prohibited Actions & Common Workshop Pitfalls Table
        y = self.draw_section_banner(y, "1.8", "Workshop Pitfalls & Prohibited Lab Actions Table")
        
        pitfalls = [
            ("Prohibited Action", "Direct Consequence", "Correct Protocol"),
            ("Using Ø3.0 mm drill bit", "M3 screw binds; hoop stress >70 MPa cracks acrylic", "Use Ø3.3 mm bit (175 µm radial clearance)"),
            ("Drilling without wood backing", "Brittle cone tear-out & blowout on bottom face", "Always clamp firmly onto scrap MDF/plywood"),
            ("Spindle speed >1500 RPM", "Acrylic melts, gums up flutes, binds bit violently", "Drill at 600–800 RPM with pecking feed"),
            ("Unclamping between passes", "Collinearity lost; sheets shift; holes misalign", "Keep clamped until all 8 pilots finished"),
            ("Using Fevikwik / Superglue", "Severe white frosting & brittle shock failure", "Use DCM solvent or Araldite epoxy")
        ]
        
        col_ws = [150.0, 190.0, 183.0]
        row_h = 13.0
        cr.save()
        # Header row
        cr.set_source_rgb(*C_BG_HDR)
        cr.rectangle(MARGIN_L, y + 3.0, USABLE_W, row_h)
        cr.fill()
        cr.set_source_rgb(*C_BLACK)
        cr.set_line_width(0.5)
        cr.rectangle(MARGIN_L, y + 3.0, USABLE_W, row_h)
        cr.stroke()

        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        cr.set_font_size(7.0)
        cx = MARGIN_L + 4.0
        for idx, h_text in enumerate(pitfalls[0]):
            cr.move_to(cx, y + 12.0)
            cr.show_text(h_text)
            cx += col_ws[idx]
        y += row_h + 3.0

        # Body rows
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
        cr.set_font_size(6.8)
        for r in pitfalls[1:]:
            cr.set_source_rgb(*C_LINE)
            cr.set_line_width(0.3)
            cr.move_to(MARGIN_L, y + row_h)
            cr.line_to(MARGIN_L + USABLE_W, y + row_h)
            cr.stroke()

            cx = MARGIN_L + 4.0
            for idx, c_text in enumerate(r):
                cr.set_source_rgb(*C_BLACK if idx == 0 else C_DARK)
                cr.move_to(cx, y + 9.5)
                cr.show_text(c_text)
                cx += col_ws[idx]
            y += row_h
        cr.restore()

        self.draw_footer(2)
        cr.show_page()

    def render_page_3(self):
        y = self.draw_header(3, "PART 2: VERNIER CALIPER PRECISION MEASUREMENT MANUAL",
                             "Caliper Anatomy, Zero Calibration, Hole-Pitch Formulas & Component Protocols")
        cr = self.cr

        # Section 2.0: Anatomy & Handling of the Caliper
        y = self.draw_section_banner(y, "2.0", "Caliper Anatomy, Zero-Calibration & Proper Handling")
        
        cal_parts = [
            ("Outside Measuring Jaws:",
             "Used for external dimensions (motor OD, shaft diameter, PCB outline, plate thickness). Ensure jaws are perpendicular to "
             "the workpiece to avoid cosine tilt error."),
            ("Inside Measuring Nibs:",
             "Used for internal dimensions (hole diameters, bracket cradle width, slot spacing). Insert nibs fully into the hole without "
             "canting to capture the true diameter."),
            ("Depth Measuring Probe:",
             "Extends from the beam end; used for step heights, blind pocket depths, and gearbox collar protrusion. Hold beam face flush."),
            ("Zero Calibration Check:",
             "Wipe jaws with clean paper. Close gently. Verify the '0' mark on the Vernier scale aligns exactly with '0' on the main beam "
             "(or press ZERO on a digital caliper). If an offset exists, record the zero error (±e) and subtract it from all subsequent readings.")
        ]
        for p_title, p_desc in cal_parts:
            cr.save()
            cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
            cr.set_font_size(7.5)
            cr.set_source_rgb(*C_BLACK)
            cr.move_to(MARGIN_L + 4.0, y + 7.5)
            cr.show_text(p_title)

            # Properly wrapped description to eliminate horizontal clipping
            lines = self.wrap_text(p_desc, 7.0, USABLE_W - 120.0)
            cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
            cr.set_font_size(7.0)
            cr.set_source_rgb(*C_DARK)
            py = y + 7.5
            for idx, ln in enumerate(lines):
                if idx == 0:
                    cr.move_to(MARGIN_L + 120.0, py)
                else:
                    py += 8.5
                    cr.move_to(MARGIN_L + 120.0, py)
                cr.show_text(ln)
            cr.restore()
            y = max(y + 12.0, py + 10.0)
        y += 2.0

        # Section 2.1: Hole Pitch Measurement Formula
        y = self.draw_section_banner(y, "2.1", "Hole Pitch Center-to-Center Formulas (Eliminating Tangent Uncertainty)")

        pitch_desc = (
            "NEVER GUESS OR EYEBALL HOLE CENTERS! Because caliper jaws cannot balance on virtual centerlines, use the exact "
            "tangent dimension formula to calculate true pitch (P) with ±0.02 mm precision:"
        )
        lines = self.wrap_text(pitch_desc, 7.2, USABLE_W)
        cr.save()
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
        cr.set_font_size(7.2)
        cr.set_source_rgb(*C_DARK)
        for ln in lines:
            cr.move_to(MARGIN_L + 4.0, y + 7.5)
            cr.show_text(ln)
            y += 9.0
        cr.restore()
        y += 3.0

        # Formula callout box
        box_h = 38.0
        cr.save()
        cr.set_source_rgb(*C_BG_BOX)
        cr.rectangle(MARGIN_L, y, USABLE_W, box_h)
        cr.fill()
        cr.set_source_rgb(*C_LINE)
        cr.set_line_width(0.5)
        cr.rectangle(MARGIN_L, y, USABLE_W, box_h)
        cr.stroke()

        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        cr.set_font_size(7.8)
        cr.set_source_rgb(*C_BLACK)
        cr.move_to(MARGIN_L + 10.0, y + 14.0)
        cr.show_text("METHOD A (Outside Span):  Pitch P = L_outer - D_hole")
        cr.move_to(MARGIN_L + 10.0, y + 27.0)
        cr.show_text("METHOD B (Inside Span):   Pitch P = L_inner + D_hole")

        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
        cr.set_font_size(7.0)
        cr.set_source_rgb(*C_GRAY)
        cr.move_to(MARGIN_L + 255.0, y + 14.0)
        cr.show_text("Where L_outer = distance across far outer edges of two holes")
        cr.move_to(MARGIN_L + 255.0, y + 27.0)
        cr.show_text("Where L_inner = distance across near inner edges of two holes")
        cr.restore()
        y += box_h + 8.0

        # Section 2.2: Systematic Component-by-Component Measurement Protocols
        y = self.draw_section_banner(y, "2.2", "Systematic Component Measurement Protocols (What & How to Measure)")

        components = [
            ("1. N20 Micro Metal Gear Motor", [
                "• Output D-Shaft OD: Measure cylindrical diameter with outside jaws. Nominal: 3.00 mm (typically 2.96–2.98 mm).",
                "• D-Flat Chord Thickness: Measure flat face to curved back. Nominal: 2.50 mm (typically 2.45–2.48 mm). Critical for rotor arm bore.",
                "• Flat Length & Usable Shaft: Measure length of flat section (nominal ~7.0 mm) and total shaft protrusion (nominal 9.5 mm).",
                "• Motor Gearbox Casing: Measure width (nom 12.0 mm), height (nom 10.0 mm), and gearbox length (nom 9.0–15.0 mm)."
            ]),
            ("2. Robocraze ADXL345 Breakout Board", [
                "• Mounting Hole Diameter: Measure inside diameter of both mounting holes with inside nibs. Nominal: 3.20 mm.",
                "• Mounting Hole Pitch: Measure L_outer across both holes, subtract diameter. Target pitch: 15.00 mm. Dictates sensor bracket upright.",
                "• Board Width & Length: Measure PCB substrate outline with outside jaws. Nominal: 15.5 mm × 20.5 mm.",
                "• Substrate Thickness: Measure PCB thickness. Nominal: 1.60 mm. Verify header pin vertical clearance."
            ]),
            ("3. N20 Stamped Metal U-Bracket", [
                "• Baseplate Hole Pitch: Measure center-to-center distance between the two base mounting slots. Nominal: 17.00 mm.",
                "• Base Hole Diameter: Measure slot width with inside nibs. Nominal: 3.20–3.50 mm (clears M3 screw).",
                "• Cradle Internal Width: Measure internal gap between metal uprights. Must snugly accommodate 12.0 mm gearbox."
            ]),
            ("4. Acrylic Baseplate Blanks (Dual 5 mm Sheets)", [
                "• Thickness per Sheet: Measure thickness of Sheet 1 and Sheet 2 at all 4 corners. (Cast acrylic varies from 4.6 to 5.2 mm).",
                "• Combined Stack Thickness: Measure clamped sandwich thickness. Nominal: 10.00 mm (determines required M3 bolt length).",
                "• Blank Width & Length: Measure outer edges of both sheets. Nominal: 150.0 mm × 150.0 mm.",
                "• Squareness Diagonals: Measure diagonal D1 and D2. If square, D1 = D2 = 212.1 mm. Difference indicates skew."
            ]),
            ("5. M3 Fasteners, Washers & Nylon Locknuts", [
                "• M3 Bolt Shank Major Diameter: Measure outside thread crests. Nominal: 2.92–2.95 mm (must slip into 3.3 mm hole).",
                "• Bolt Length Under Head: Measure threaded length. Standoff bolts: 20.0 mm; Bracket bolts: 16.0 mm.",
                "• DIN 125 M3 Washer OD & ID: Measure outer diameter (nominal 7.00 mm) and inner hole (nominal 3.20 mm)."
            ])
        ]

        for comp_name, comp_steps in components:
            cr.save()
            cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
            cr.set_font_size(7.5)
            cr.set_source_rgb(*C_BLACK)
            cr.move_to(MARGIN_L + 4.0, y + 7.5)
            cr.show_text(comp_name)
            y += 9.0

            cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
            cr.set_font_size(6.8)
            cr.set_source_rgb(*C_DARK)
            for step in comp_steps:
                cr.move_to(MARGIN_L + 10.0, y + 7.0)
                cr.show_text(step)
                y += 8.2
            cr.restore()
            y += 2.0

        self.draw_footer(3)
        cr.show_page()

    def render_page_4(self):
        y = self.draw_header(4, "PART 2 (CONTINUED): LAB MEASUREMENT LOG & TOLERANCE LEDGER",
                             "Printable Fillable Data Sheet, CAD Offsets & Laboratory Attestation")
        cr = self.cr

        # Section 2.3: Printable Field Measurement Recording Ledger
        y = self.draw_section_banner(y, "2.3", "Physical Measurement Recording Ledger (Fill In with Pen in Lab)")

        table_headers = ["Check", "Component Parameter to Measure", "Expected", "Trial 1 (mm)", "Trial 2 (mm)", "Average", "Fit / Action Required"]
        col_w = [30.0, 180.0, 52.0, 52.0, 52.0, 52.0, 105.0]
        
        meas_items = [
            ("N20 Shaft Outer Diameter (OD)", "3.00 mm", "Rotor hub bore sizing"),
            ("N20 D-Flat Chord Thickness", "2.50 mm", "Rotor D-flat chord fit"),
            ("N20 Usable Shaft Length", "9.50 mm", "Max rotor hub thickness"),
            ("N20 Motor Body Width", "12.00 mm", "Metal bracket clamp fit"),
            ("N20 Bracket Base Hole Pitch", "17.00 mm", "Baseplate hole M1-M2 spacing"),
            ("ADXL345 PCB Hole Diameter", "3.20 mm", "M3 screw clearance check"),
            ("ADXL345 Hole Center Pitch", "15.00 mm", "Sensor bracket upright pitch"),
            ("ADXL345 PCB Dimensions (W × L)", "15.5 × 20.5", "Sensor bracket face pocket"),
            ("Acrylic Sheet 1 Thickness", "5.00 mm", "Top plate actual gauge"),
            ("Acrylic Sheet 2 Thickness", "5.00 mm", "Bottom plate actual gauge"),
            ("Combined Stack Thickness", "10.00 mm", "M3 bolt grip length verify"),
            ("Acrylic Blank 1 (W × L)", "150 × 150 mm", "Edge flushness check"),
            ("Acrylic Blank 2 (W × L)", "150 × 150 mm", "Edge flushness check"),
            ("Acrylic Diagonals (D1 vs D2)", "212.1 mm", "Squareness check (D1=D2)"),
            ("M3 Bolt Shank Major Diameter", "2.92 mm", "Free slip in 3.3 mm holes"),
            ("DIN 125 Washer Outer Diameter", "7.00 mm", "Bearing shelf verification")
        ]

        # Generous row height for easy pen writing
        row_h = 16.0
        cr.save()
        # Draw table header
        cr.set_source_rgb(*C_BG_HDR)
        cr.rectangle(MARGIN_L, y + 2.0, USABLE_W, row_h)
        cr.fill()
        cr.set_source_rgb(*C_BLACK)
        cr.set_line_width(0.6)
        cr.rectangle(MARGIN_L, y + 2.0, USABLE_W, row_h)
        cr.stroke()

        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        cr.set_font_size(6.8)
        cx = MARGIN_L
        for idx, th in enumerate(table_headers):
            cr.move_to(cx + 4.0, y + 12.5)
            cr.show_text(th)
            cx += col_w[idx]
        y += row_h + 2.0

        # Draw measurement rows
        cr.set_font_size(6.5)
        for r_idx, (p_name, p_nom, p_action) in enumerate(meas_items):
            if r_idx % 2 == 1:
                cr.set_source_rgb(0.98, 0.98, 0.98)
                cr.rectangle(MARGIN_L, y, USABLE_W, row_h)
                cr.fill()

            cr.set_source_rgb(*C_LINE)
            cr.set_line_width(0.3)
            cr.move_to(MARGIN_L, y + row_h)
            cr.line_to(MARGIN_L + USABLE_W, y + row_h)
            cr.stroke()

            # Vertical grid lines
            vx = MARGIN_L
            for w in col_w[:-1]:
                vx += w
                cr.move_to(vx, y)
                cr.line_to(vx, y + row_h)
                cr.stroke()

            # Checkbox square
            cr.set_source_rgb(*C_BLACK)
            cr.rectangle(MARGIN_L + 10.0, y + 4.5, 7.5, 7.5)
            cr.stroke()

            # Param Name
            cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
            cr.move_to(MARGIN_L + col_w[0] + 4.0, y + 11.0)
            cr.show_text(p_name)

            # Nominal
            cr.move_to(MARGIN_L + col_w[0] + col_w[1] + 4.0, y + 11.0)
            cr.show_text(p_nom)

            # Action / Notes hint (light gray)
            cr.set_source_rgb(*C_GRAY)
            cr.move_to(MARGIN_L + sum(col_w[:6]) + 4.0, y + 11.0)
            cr.show_text(p_action)

            y += row_h
        cr.restore()
        y += 8.0

        # Section 2.4: Translating Caliper Data into 3D CAD Print Offsets
        y = self.draw_section_banner(y, "2.4", "Translating Caliper Data into 3D CAD Print Tolerances")
        
        cad_text = (
            "• FDM 3D PRINT SHRINKAGE RULES (PLA): Molten plastic contracts upon cooling. Apply these systematic offsets:\n"
            "  1. Bolt Through-Holes: Add +0.20 mm over bolt diameter (e.g. for M3 bolt, design hole at Ø3.20 mm to print at ~3.02 mm).\n"
            "  2. N20 Motor D-Shaft Bore: Shaft OD is 3.00 mm -> Model bore at Ø3.15 mm; Shaft flat is 2.50 mm -> Model chord at 2.65 mm.\n"
            "  3. ADXL345 Upright Bracket Holes: Spacing must exactly match measured PCB pitch (nom 15.00 mm) ±0.05 mm.\n"
            "• ROTOR FIT TUNING: If measured shaft OD is 2.95 mm, model D-bore at Ø3.08 mm. If 2.99 mm, model bore at Ø3.18 mm."
        )
        for c_para in cad_text.split("\n"):
            lines = self.wrap_text(c_para, 7.0, USABLE_W)
            cr.save()
            cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
            cr.set_font_size(7.0)
            cr.set_source_rgb(*C_DARK)
            for ln in lines:
                cr.move_to(MARGIN_L + 4.0, y + 7.5)
                cr.show_text(ln)
                y += 8.5
            cr.restore()
            y += 1.5

        # Section 2.5: Laboratory Sign-Off & Verification Block
        y = self.draw_section_banner(y, "2.5", "Laboratory Session Sign-Off & Attestation")

        sign_box_h = 42.0
        cr.save()
        cr.set_source_rgb(*C_BG_BOX)
        cr.rectangle(MARGIN_L, y, USABLE_W, sign_box_h)
        cr.fill()
        cr.set_source_rgb(*C_LINE)
        cr.set_line_width(0.5)
        cr.rectangle(MARGIN_L, y, USABLE_W, sign_box_h)
        cr.stroke()

        col_s = USABLE_W / 3.0
        sign_labels = [
            ("Student Lead (Measurement)", "Mohammed Nihad P C (JEC24CC044)", "Signature: ______________________"),
            ("Team Member (Fabrication)", "Sreehari K / Sreeprada K S", "Signature: ______________________"),
            ("Mechanical Lab In-Charge", "Faculty / Lab Instructor", "Signature: ______________________")
        ]
        for idx, (role, name, sig) in enumerate(sign_labels):
            sx = MARGIN_L + (idx * col_s) + 6.0
            cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
            cr.set_font_size(7.0)
            cr.set_source_rgb(*C_BLACK)
            cr.move_to(sx, y + 10.5)
            cr.show_text(role)

            cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
            cr.set_font_size(6.8)
            cr.set_source_rgb(*C_DARK)
            cr.move_to(sx, y + 21.0)
            cr.show_text(name)

            cr.move_to(sx, y + 33.5)
            cr.show_text(sig)
        cr.restore()

        self.draw_footer(4)
        cr.show_page()

    def build(self):
        self.render_page_1()
        self.render_page_2()
        self.render_page_3()
        self.render_page_4()
        self.surface.finish()
        print(f"[PDF] Successfully generated: {self.filename}")


def main():
    workspace_dir = "/home/paradoxpete/Documents/PROJECT_ORGANIZED"
    downloads_dir = "/home/paradoxpete/Downloads"

    pdf_ws = os.path.join(workspace_dir, "VibeGuard_Mechanical_Lab_Fabrication_and_Measurement_Manual.pdf")
    pdf_dl = os.path.join(downloads_dir, "VibeGuard_Mechanical_Lab_Fabrication_and_Measurement_Manual.pdf")

    generator = LabManualPDF(pdf_ws)
    generator.build()

    # Mirror to Downloads
    with open(pdf_ws, "rb") as src, open(pdf_dl, "wb") as dst:
        dst.write(src.read())
    print(f"[PDF Mirror] Successfully copied to: {pdf_dl}")


if __name__ == "__main__":
    main()
