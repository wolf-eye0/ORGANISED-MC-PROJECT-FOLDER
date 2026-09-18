#!/usr/bin/env python3
"""
Generates 3-page, publication-grade, ready-to-print, 100% monochrome/photocopy-friendly PDFs:
- Page 1: Format A - Official Inter-Departmental Requisition to HOD Mechanical through HOD Cyber Security
- Page 2: Format B - Internal Departmental Application to Dr. Geethu Mary George (HOD Cyber Security)
- Page 3: Format C - Mechanical Machine Shop & Tool-Crib Requisition Issue Slip

Generates two student pairing variants:
1. Mohammed Nihad P C (JEC24CC044) & Sreehari K (JEC24CC055)
2. Mohammed Nihad P C (JEC24CC044) & Sreeprada K S (JEC24CC056)
"""

import cairo
import os

A4_WIDTH = 595.28
A4_HEIGHT = 841.89
MARGIN_LEFT = 48.0
MARGIN_RIGHT = 48.0
MARGIN_TOP = 42.0
MARGIN_BOTTOM = 42.0
USABLE_WIDTH = A4_WIDTH - MARGIN_LEFT - MARGIN_RIGHT

# Monochrome / Black & White / Photocopy-Optimized Palette
COLOR_BLACK = (0.00, 0.00, 0.00)       # 100% Pure Black for crisp laser printing
COLOR_DARK = (0.12, 0.12, 0.12)        # High-contrast body text
COLOR_MUTED = (0.32, 0.32, 0.32)       # Subtle secondary labels
COLOR_BORDER = (0.45, 0.45, 0.45)      # Clean distinct borders that photocopy sharply
COLOR_BG_LIGHT = (0.96, 0.96, 0.96)    # 4% gray tint for subtle distinction without toner blotch
COLOR_TABLE_HDR = (0.90, 0.90, 0.90)   # 10% clean gray for table headers with bold black text

class PrintableLetterPDF:
    def __init__(self, filename, student1=("Mohammed Nihad P C", "JEC24CC044"), student2=("Sreehari K", "JEC24CC055")):
        self.filename = filename
        self.surface = cairo.PDFSurface(filename, A4_WIDTH, A4_HEIGHT)
        self.cr = cairo.Context(self.surface)
        self.page = 1
        self.s1_name, self.s1_roll = student1
        self.s2_name, self.s2_roll = student2

    def wrap_text(self, text, font_size, max_width, bold=False):
        cr = self.cr
        cr.save()
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD if bold else cairo.FONT_WEIGHT_NORMAL)
        cr.set_font_size(font_size)
        
        words = text.split(" ")
        lines = []
        curr = []
        for w in words:
            if not w: continue
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
        cr.restore()
        return lines

    def draw_letterhead(self):
        cr = self.cr
        cr.save()
        
        # Institutional top banner
        cr.set_source_rgb(*COLOR_BLACK)
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        cr.set_font_size(12.0)
        cr.move_to(MARGIN_LEFT, MARGIN_TOP + 12.0)
        cr.show_text("JYOTHI ENGINEERING COLLEGE (AUTONOMOUS)")
        
        cr.set_source_rgb(*COLOR_DARK)
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
        cr.set_font_size(8.2)
        cr.move_to(A4_WIDTH - MARGIN_RIGHT - 116.0, MARGIN_TOP + 12.0)
        cr.show_text("CHERUTHURUTHY, THRISSUR")
        
        cr.move_to(MARGIN_LEFT, MARGIN_TOP + 24.0)
        cr.show_text("DEPARTMENT OF CYBER SECURITY | B.TECH PROJECT WORKBENCH")
        
        # Crisp solid divider rule
        cr.set_source_rgb(*COLOR_BLACK)
        cr.set_line_width(1.2)
        cr.move_to(MARGIN_LEFT, MARGIN_TOP + 30.0)
        cr.line_to(A4_WIDTH - MARGIN_RIGHT, MARGIN_TOP + 30.0)
        cr.stroke()
        
        cr.restore()

    def draw_footer_note(self, note_text):
        cr = self.cr
        cr.save()
        cr.set_source_rgb(*COLOR_BORDER)
        cr.set_line_width(0.75)
        cr.move_to(MARGIN_LEFT, A4_HEIGHT - MARGIN_BOTTOM - 6.0)
        cr.line_to(A4_WIDTH - MARGIN_RIGHT, A4_HEIGHT - MARGIN_BOTTOM - 6.0)
        cr.stroke()

        cr.set_source_rgb(*COLOR_MUTED)
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
        cr.set_font_size(7.5)
        cr.move_to(MARGIN_LEFT, A4_HEIGHT - MARGIN_BOTTOM + 5.0)
        cr.show_text(note_text)
        
        page_str = f"Page {self.page} of 3"
        cr.move_to(A4_WIDTH - MARGIN_RIGHT - 50.0, A4_HEIGHT - MARGIN_BOTTOM + 5.0)
        cr.show_text(page_str)
        cr.restore()

    # =========================================================================
    # PAGE 1: FORMAT A - INTER-DEPARTMENTAL (RECOMMENDED)
    # =========================================================================
    def render_page_1(self):
        self.draw_letterhead()
        cr = self.cr
        y = MARGIN_TOP + 46.0

        # Date & Header label
        cr.set_source_rgb(*COLOR_BLACK)
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        cr.set_font_size(8.5)
        cr.move_to(MARGIN_LEFT, y)
        cr.show_text("FORMAT A: INTER-DEPARTMENTAL REQUISITION LETTER")
        
        cr.set_source_rgb(*COLOR_BLACK)
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
        cr.set_font_size(9.0)
        cr.move_to(A4_WIDTH - MARGIN_RIGHT - 100.0, y)
        cr.show_text("Date: 15 / 09 / 2026")
        y += 18.0

        # FROM Block
        cr.set_source_rgb(*COLOR_BLACK)
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        cr.set_font_size(9.0)
        cr.move_to(MARGIN_LEFT, y)
        cr.show_text("From,")
        y += 13.0

        from_lines = [
            (self.s1_name, f" (Roll No: {self.s1_roll})"),
            (self.s2_name, f" (Roll No: {self.s2_roll})"),
            ("S5, Department of Cyber Security", ""),
            ("Jyothi Engineering College, Cheruthuruthy", "")
        ]
        for name, roll in from_lines:
            cr.set_source_rgb(*COLOR_BLACK)
            cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD if roll else cairo.FONT_WEIGHT_NORMAL)
            cr.set_font_size(9.0)
            cr.move_to(MARGIN_LEFT + 10.0, y)
            cr.show_text(name)
            if roll:
                ext = cr.text_extents(name)
                cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
                cr.move_to(MARGIN_LEFT + 10.0 + ext.x_advance, y)
                cr.show_text(roll)
            y += 13.0

        y += 4.0
        # TO Block
        cr.set_source_rgb(*COLOR_BLACK)
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        cr.set_font_size(9.0)
        cr.move_to(MARGIN_LEFT, y)
        cr.show_text("To,")
        y += 13.0

        to_lines = [
            "The Head of the Department,",
            "Department of Mechanical Engineering,",
            "Jyothi Engineering College, Cheruthuruthy."
        ]
        for l in to_lines:
            cr.set_source_rgb(*COLOR_DARK)
            cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
            cr.set_font_size(9.0)
            cr.move_to(MARGIN_LEFT + 10.0, y)
            cr.show_text(l)
            y += 13.0

        y += 3.0
        # THROUGH Block
        cr.set_source_rgb(*COLOR_BLACK)
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        cr.set_font_size(9.0)
        cr.move_to(MARGIN_LEFT, y)
        cr.show_text("Through,")
        y += 13.0

        through_lines = [
            "The Head of the Department (Dr. Geethu Mary George),",
            "Department of Cyber Security, Jyothi Engineering College."
        ]
        for l in through_lines:
            cr.set_source_rgb(*COLOR_DARK)
            cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
            cr.set_font_size(9.0)
            cr.move_to(MARGIN_LEFT + 10.0, y)
            cr.show_text(l)
            y += 13.0

        y += 6.0
        # Subject
        cr.set_source_rgb(*COLOR_BLACK)
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        cr.set_font_size(9.2)
        cr.move_to(MARGIN_LEFT, y)
        cr.show_text("Subject: Requisition for Vernier Caliper & Machine Shop Drilling Access for Project Testbed")
        y += 16.0

        # Salutation
        cr.set_source_rgb(*COLOR_BLACK)
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        cr.set_font_size(9.0)
        cr.move_to(MARGIN_LEFT, y)
        cr.show_text("Respected Sir / Madam,")
        y += 15.0

        # Body Paragraphs - Natural, direct, professional
        cr.set_source_rgb(*COLOR_DARK)
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
        cr.set_font_size(8.8)
        line_h = 12.5

        p1 = ("As part of our project work titled \"VibeGuard: Machine Vibration & Industrial Predictive Maintenance Testbed\" "
              "(S5 Cyber Security), we are currently fabricating the physical motor-sensor testing rig on an acrylic baseplate.")
        for ln in self.wrap_text(p1, 8.8, USABLE_WIDTH):
            cr.move_to(MARGIN_LEFT, y)
            cr.show_text(ln)
            y += line_h
        y += 5.0

        p2 = ("To ensure accurate fabrication and avoid assembly errors during mounting, we respectfully request "
              "permission to utilize the following facilities in the Department of Mechanical Engineering:")
        for ln in self.wrap_text(p2, 8.8, USABLE_WIDTH):
            cr.move_to(MARGIN_LEFT, y)
            cr.show_text(ln)
            y += line_h
        y += 4.0

        bullets = [
            "1. Issue of a Vernier Caliper (0.01 mm resolution) to measure motor D-shaft dimensions, fastener tolerances, and sensor PCB mounting pitches.",
            "2. Access to the Workshop Bench / Pillar Drill Press facility (with 2.5 mm and 3.2 mm HSS drill bits) to drill precision mounting holes in our acrylic plate."
        ]
        for b in bullets:
            for idx, ln in enumerate(self.wrap_text(b, 8.5, USABLE_WIDTH - 12.0)):
                cr.move_to(MARGIN_LEFT + 12.0, y)
                cr.show_text(ln)
                y += line_h
            y += 2.0
        y += 4.0

        p3 = ("We assure you that all workshop safety guidelines will be strictly followed, tools will be handled with utmost care, "
              "and instruments will be safely returned to the Tool Crib immediately upon completion.")
        for ln in self.wrap_text(p3, 8.8, USABLE_WIDTH):
            cr.move_to(MARGIN_LEFT, y)
            cr.show_text(ln)
            y += line_h
        y += 4.0

        cr.move_to(MARGIN_LEFT, y)
        cr.show_text("Kindly grant us permission to access the requested measuring tools and drilling facility.")
        y += 15.0

        cr.move_to(MARGIN_LEFT, y)
        cr.show_text("Thank you.")
        y += 18.0

        # Signatures
        cr.move_to(MARGIN_LEFT, y)
        cr.show_text("Yours sincerely,")
        y += 26.0

        col_w = USABLE_WIDTH / 2.0
        cr.set_source_rgb(*COLOR_BLACK)
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        cr.move_to(MARGIN_LEFT, y)
        cr.show_text(self.s1_name)
        cr.move_to(MARGIN_LEFT + col_w, y)
        cr.show_text(self.s2_name)
        y += 12.0

        cr.set_source_rgb(*COLOR_DARK)
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
        cr.set_font_size(8.0)
        cr.move_to(MARGIN_LEFT, y)
        cr.show_text(f"Roll No: {self.s1_roll}  |  (Signature)")
        cr.move_to(MARGIN_LEFT + col_w, y)
        cr.show_text(f"Roll No: {self.s2_roll}  |  (Signature)")
        y += 18.0

        # Endorsement Box for Dr. Geethu Mary George (Clean, high-contrast, laser-friendly)
        box_h = 58.0
        cr.set_source_rgb(*COLOR_BG_LIGHT)
        cr.rectangle(MARGIN_LEFT, y, USABLE_WIDTH, box_h)
        cr.fill()
        
        cr.set_source_rgb(*COLOR_BORDER)
        cr.set_line_width(0.75)
        cr.rectangle(MARGIN_LEFT, y, USABLE_WIDTH, box_h)
        cr.stroke()

        cr.set_source_rgb(*COLOR_BLACK)
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        cr.set_font_size(8.0)
        cr.move_to(MARGIN_LEFT + 10.0, y + 14.0)
        cr.show_text("RECOMMENDATION & FORWARDING OF DEPUTED HOD (DEPARTMENT OF CYBER SECURITY):")

        cr.set_source_rgb(*COLOR_DARK)
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
        cr.set_font_size(8.0)
        cr.move_to(MARGIN_LEFT + 10.0, y + 27.0)
        cr.show_text("Recommended and forwarded to the Head of the Department, Mechanical Engineering.")
        
        cr.set_source_rgb(*COLOR_BLACK)
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        cr.move_to(MARGIN_LEFT + 10.0, y + 42.0)
        cr.show_text("Dr. Geethu Mary George")
        
        cr.set_source_rgb(*COLOR_DARK)
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
        cr.move_to(MARGIN_LEFT + 10.0, y + 51.0)
        cr.show_text("Head of the Department, Cyber Security")

        cr.move_to(A4_WIDTH - MARGIN_RIGHT - 140.0, y + 46.0)
        cr.show_text("(Signature & Department Seal)")

        self.draw_footer_note("Official Inter-Departmental Requisition - Ready for Print & Submission")
        self.surface.show_page()
        self.page += 1

    # =========================================================================
    # PAGE 2: FORMAT B - INTERNAL REQUEST TO DR. GEETHU MARY GEORGE
    # =========================================================================
    def render_page_2(self):
        self.draw_letterhead()
        cr = self.cr
        y = MARGIN_TOP + 46.0

        cr.set_source_rgb(*COLOR_BLACK)
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        cr.set_font_size(8.5)
        cr.move_to(MARGIN_LEFT, y)
        cr.show_text("FORMAT B: INTERNAL DEPARTMENTAL APPLICATION TO HOD")
        
        cr.set_source_rgb(*COLOR_BLACK)
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
        cr.set_font_size(9.0)
        cr.move_to(A4_WIDTH - MARGIN_RIGHT - 100.0, y)
        cr.show_text("Date: 15 / 09 / 2026")
        y += 20.0

        # FROM Block
        cr.set_source_rgb(*COLOR_BLACK)
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        cr.set_font_size(9.0)
        cr.move_to(MARGIN_LEFT, y)
        cr.show_text("From,")
        y += 14.0

        from_lines = [
            (self.s1_name, f" (Roll No: {self.s1_roll})"),
            (self.s2_name, f" (Roll No: {self.s2_roll})"),
            ("S5, Department of Cyber Security", ""),
            ("Jyothi Engineering College, Cheruthuruthy", "")
        ]
        for name, roll in from_lines:
            cr.set_source_rgb(*COLOR_BLACK)
            cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD if roll else cairo.FONT_WEIGHT_NORMAL)
            cr.set_font_size(9.0)
            cr.move_to(MARGIN_LEFT + 10.0, y)
            cr.show_text(name)
            if roll:
                ext = cr.text_extents(name)
                cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
                cr.move_to(MARGIN_LEFT + 10.0 + ext.x_advance, y)
                cr.show_text(roll)
            y += 14.0

        y += 8.0
        # TO Block
        cr.set_source_rgb(*COLOR_BLACK)
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        cr.set_font_size(9.0)
        cr.move_to(MARGIN_LEFT, y)
        cr.show_text("To,")
        y += 14.0

        to_lines = [
            "The Head of the Department,",
            "Dr. Geethu Mary George,",
            "Department of Cyber Security,",
            "Jyothi Engineering College, Cheruthuruthy."
        ]
        for idx, l in enumerate(to_lines):
            cr.set_source_rgb(*COLOR_BLACK if idx==1 else COLOR_DARK)
            cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD if idx==1 else cairo.FONT_WEIGHT_NORMAL)
            cr.set_font_size(9.0)
            cr.move_to(MARGIN_LEFT + 10.0, y)
            cr.show_text(l)
            y += 14.0

        y += 10.0
        # Subject
        cr.set_source_rgb(*COLOR_BLACK)
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        cr.set_font_size(9.2)
        cr.move_to(MARGIN_LEFT, y)
        cr.show_text("Subject: Request for Official Endorsement / Forwarding for Mechanical Workshop Access")
        y += 18.0

        # Salutation
        cr.set_source_rgb(*COLOR_BLACK)
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        cr.set_font_size(9.0)
        cr.move_to(MARGIN_LEFT, y)
        cr.show_text("Respected Madam,")
        y += 16.0

        # Body - Natural, direct to their own HOD who knows them
        cr.set_source_rgb(*COLOR_DARK)
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
        cr.set_font_size(9.0)
        line_h = 14.0

        p1 = ("As part of our project work on \"VibeGuard: Machine Vibration & Industrial Predictive Maintenance Testbed\", "
              "we are currently setting up the physical hardware testbed rig. For this, we require precision measurements "
              "using a Vernier Caliper and need to drill mounting holes into our acrylic baseplate using the pillar drill press "
              "in the Mechanical Workshop.")
        for ln in self.wrap_text(p1, 9.0, USABLE_WIDTH):
            cr.move_to(MARGIN_LEFT, y)
            cr.show_text(ln)
            y += line_h
        y += 8.0

        p2 = ("The Department of Mechanical Engineering has indicated that inter-departmental equipment loan and workshop access "
              "require an official recommendation and forwarding letter from our Head of Department.")
        for ln in self.wrap_text(p2, 9.0, USABLE_WIDTH):
            cr.move_to(MARGIN_LEFT, y)
            cr.show_text(ln)
            y += line_h
        y += 8.0

        p3 = ("We kindly request you to endorse and forward our attached requisition letter to the Head of the Department, "
              "Mechanical Engineering, so that we may obtain the measuring instruments and complete our fabrication work.")
        for ln in self.wrap_text(p3, 9.0, USABLE_WIDTH):
            cr.move_to(MARGIN_LEFT, y)
            cr.show_text(ln)
            y += line_h
        y += 8.0

        p4 = ("We assure you that all workshop activities will be carried out safely in adherence to institutional guidelines, "
              "and without disruption to our scheduled academic classes.")
        for ln in self.wrap_text(p4, 9.0, USABLE_WIDTH):
            cr.move_to(MARGIN_LEFT, y)
            cr.show_text(ln)
            y += line_h
        y += 20.0

        cr.move_to(MARGIN_LEFT, y)
        cr.show_text("Thank you.")
        y += 24.0

        cr.move_to(MARGIN_LEFT, y)
        cr.show_text("Yours respectfully,")
        y += 34.0

        col_w = USABLE_WIDTH / 2.0
        cr.set_source_rgb(*COLOR_BLACK)
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        cr.move_to(MARGIN_LEFT, y)
        cr.show_text(self.s1_name)
        cr.move_to(MARGIN_LEFT + col_w, y)
        cr.show_text(self.s2_name)
        y += 13.0

        cr.set_source_rgb(*COLOR_DARK)
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
        cr.set_font_size(8.5)
        cr.move_to(MARGIN_LEFT, y)
        cr.show_text(f"Roll No: {self.s1_roll}  |  (Signature)")
        cr.move_to(MARGIN_LEFT + col_w, y)
        cr.show_text(f"Roll No: {self.s2_roll}  |  (Signature)")

        self.draw_footer_note("Internal Department Application - Addressed to Dr. Geethu Mary George")
        self.surface.show_page()
        self.page += 1

    # =========================================================================
    # PAGE 3: FORMAT C - WORKSHOP REQUISITION & TOOL-CRIB ISSUE SLIP
    # =========================================================================
    def render_page_3(self):
        self.draw_letterhead()
        cr = self.cr
        y = MARGIN_TOP + 46.0

        cr.set_source_rgb(*COLOR_BLACK)
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        cr.set_font_size(8.5)
        cr.move_to(MARGIN_LEFT, y)
        cr.show_text("FORMAT C: MECHANICAL WORKSHOP TOOL & FACILITY ISSUE SLIP")
        
        cr.set_source_rgb(*COLOR_BLACK)
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
        cr.set_font_size(9.0)
        cr.move_to(A4_WIDTH - MARGIN_RIGHT - 100.0, y)
        cr.show_text("Date: 15 / 09 / 2026")
        y += 20.0

        # Project Metadata Card (Clean bordered card)
        card_h = 62.0
        cr.set_source_rgb(*COLOR_BG_LIGHT)
        cr.rectangle(MARGIN_LEFT, y, USABLE_WIDTH, card_h)
        cr.fill()
        cr.set_source_rgb(*COLOR_BORDER)
        cr.set_line_width(0.75)
        cr.rectangle(MARGIN_LEFT, y, USABLE_WIDTH, card_h)
        cr.stroke()

        col1_x = MARGIN_LEFT + 10.0
        col2_x = MARGIN_LEFT + 250.0
        
        meta = [
            ("Project Title:", "VibeGuard (Vibration Monitoring Testbed)", col1_x, y + 16.0),
            ("Department:", "Cyber Security (Semester S5)", col1_x, y + 33.0),
            ("Faculty Guide:", "Project Coordinator / Mentor", col1_x, y + 50.0),
            ("Student 1:", f"{self.s1_name} ({self.s1_roll})", col2_x, y + 16.0),
            ("Student 2:", f"{self.s2_name} ({self.s2_roll})", col2_x, y + 33.0),
            ("Contact:", "Student Project Team Workbench", col2_x, y + 50.0),
        ]
        for label, val, px, py in meta:
            cr.set_source_rgb(*COLOR_BLACK)
            cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
            cr.set_font_size(8.0)
            cr.move_to(px, py)
            cr.show_text(label)
            
            ext = cr.text_extents(label)
            cr.set_source_rgb(*COLOR_DARK)
            cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
            cr.move_to(px + ext.x_advance + 5.0, py)
            cr.show_text(val)
        y += card_h + 16.0

        # Section Header
        cr.set_source_rgb(*COLOR_BLACK)
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        cr.set_font_size(9.5)
        cr.move_to(MARGIN_LEFT, y)
        cr.show_text("ITEMS & WORKSHOP MACHINERY REQUESTED:")
        y += 12.0

        # Table - 100% Monochrome / Grayscale Laser-Printer Optimized
        headers = ["Sl", "Item / Facility Description", "Required Specification", "Purpose in Assembly"]
        widths = [26.0, 160.0, 150.0, 163.28]

        # Table Header Box with subtle 10% gray and black border
        cr.set_source_rgb(*COLOR_TABLE_HDR)
        cr.rectangle(MARGIN_LEFT, y, USABLE_WIDTH, 18.0)
        cr.fill()
        cr.set_source_rgb(*COLOR_BLACK)
        cr.set_line_width(0.75)
        cr.rectangle(MARGIN_LEFT, y, USABLE_WIDTH, 18.0)
        cr.stroke()

        cr.set_source_rgb(*COLOR_BLACK)
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        cr.set_font_size(8.0)
        cx = MARGIN_LEFT
        for idx, h in enumerate(headers):
            cr.move_to(cx + 6.0, y + 12.0)
            cr.show_text(h)
            cx += widths[idx]
        y += 18.0

        table_rows = [
            ("1", "Digital / Vernier Caliper", "0–150 mm, 0.01 mm resolution", "Measure N20 D-shaft & hole pitches"),
            ("2", "Pillar / Bench Drill Press", "Fixed vertical quill press", "Drill 90° holes in acrylic baseplate"),
            ("3", "HSS Drill Bit (Pilot)", "2.5 mm High Speed Steel", "Pilot centering to prevent drill walk"),
            ("4", "HSS Drill Bit (Clearance)", "3.2 mm High Speed Steel", "Standard M3 bolt clearance through-hole"),
            ("5", "Machine Vise & Wood Backing", "Plywood backing block", "Clamp acrylic without cracking sheet"),
            ("6", "Hand Deburring / Chamfer Tool", "90° countersink or scraper", "Lightly deburr holes to prevent cracks")
        ]

        for r_idx, (s, desc, spec, purp) in enumerate(table_rows):
            row_h = 24.0
            if r_idx % 2 == 1:
                cr.set_source_rgb(*COLOR_BG_LIGHT)
                cr.rectangle(MARGIN_LEFT, y, USABLE_WIDTH, row_h)
                cr.fill()

            cr.set_source_rgb(*COLOR_BORDER)
            cr.set_line_width(0.5)
            cr.rectangle(MARGIN_LEFT, y, USABLE_WIDTH, row_h)
            cr.stroke()

            cr.set_source_rgb(*COLOR_DARK)
            cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
            cr.set_font_size(8.0)

            cx = MARGIN_LEFT
            row_vals = [s, desc, spec, purp]
            for c_idx, val in enumerate(row_vals):
                cr.move_to(cx + 6.0, y + 15.0)
                cr.show_text(val)
                cx += widths[c_idx]
            y += row_h

        y += 18.0

        # Safety Undertaking
        cr.set_source_rgb(*COLOR_BLACK)
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        cr.set_font_size(8.5)
        cr.move_to(MARGIN_LEFT, y)
        cr.show_text("STUDENT UNDERTAKING:")
        y += 12.0

        undertaking = ("We undertake to abide by all mechanical workshop safety regulations, wear appropriate protective eye gear, "
                       "operate machinery strictly under technician guidance, and return all checked-out tools in sound working condition.")
        cr.set_source_rgb(*COLOR_DARK)
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
        cr.set_font_size(8.0)
        for ln in self.wrap_text(undertaking, 8.0, USABLE_WIDTH):
            cr.move_to(MARGIN_LEFT, y)
            cr.show_text(ln)
            y += 11.5
        y += 24.0

        # Signatures Area
        col_w = USABLE_WIDTH / 3.0
        
        cr.set_source_rgb(*COLOR_BLACK)
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        cr.set_font_size(8.2)
        cr.move_to(MARGIN_LEFT, y)
        cr.show_text(self.s1_name)
        cr.move_to(MARGIN_LEFT + col_w, y)
        cr.show_text(self.s2_name)
        cr.move_to(MARGIN_LEFT + 2*col_w, y)
        cr.show_text("Lab Staff / Technician")
        y += 12.0

        cr.set_source_rgb(*COLOR_DARK)
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
        cr.set_font_size(7.5)
        cr.move_to(MARGIN_LEFT, y)
        cr.show_text(f"{self.s1_roll}  (Signature)")
        cr.move_to(MARGIN_LEFT + col_w, y)
        cr.show_text(f"{self.s2_roll}  (Signature)")
        cr.move_to(MARGIN_LEFT + 2*col_w, y)
        cr.show_text("Tool Issue & Inspection (Sign)")
        y += 28.0

        # Return Acknowledgement Box (Clean, sharp monochrome)
        box_h = 36.0
        cr.set_source_rgb(*COLOR_BG_LIGHT)
        cr.rectangle(MARGIN_LEFT, y, USABLE_WIDTH, box_h)
        cr.fill()
        cr.set_source_rgb(*COLOR_BORDER)
        cr.set_line_width(0.75)
        cr.rectangle(MARGIN_LEFT, y, USABLE_WIDTH, box_h)
        cr.stroke()

        cr.set_source_rgb(*COLOR_BLACK)
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        cr.set_font_size(7.5)
        cr.move_to(MARGIN_LEFT + 10.0, y + 14.0)
        cr.show_text("TOOL CRIB RETURN VERIFICATION (FOR OFFICE USE):")

        cr.set_source_rgb(*COLOR_DARK)
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
        cr.move_to(MARGIN_LEFT + 10.0, y + 26.0)
        cr.show_text("Returned in good condition on Date: ____ / ____ / 2026   |   Technician Signature: ___________________________")

        self.draw_footer_note("Tool Issue & Machine Access Slip - Mechanical Workshop Copy")
        self.surface.show_page()
        self.page += 1

    def finish(self):
        self.surface.finish()

def generate_doc(pdf_ws, pdf_down, student1, student2):
    doc = PrintableLetterPDF(pdf_ws, student1=student1, student2=student2)
    doc.render_page_1()
    doc.render_page_2()
    doc.render_page_3()
    doc.finish()
    print(f"Generated 3-page PDF: {pdf_ws}")
    
    os.system(f"cp {pdf_ws} {pdf_down}")
    print(f"Mirrored to: {pdf_down}")

def main():
    s_nihad = ("Mohammed Nihad P C", "JEC24CC044")
    s_sreehari = ("Sreehari K", "JEC24CC055")
    s_sreeprada = ("Sreeprada K S", "JEC24CC056")
    
    # Variant 1: Mohammed Nihad P C & Sreehari K
    pdf1_ws = "/home/paradoxpete/Documents/PROJECT_ORGANIZED/VibeGuard_Mechanical_Lab_Request_Letters.pdf"
    pdf1_down = "/home/paradoxpete/Downloads/VibeGuard_Mechanical_Lab_Request_Letters.pdf"
    generate_doc(pdf1_ws, pdf1_down, s_nihad, s_sreehari)

    # Variant 2: Mohammed Nihad P C & Sreeprada K S
    pdf2_ws = "/home/paradoxpete/Documents/PROJECT_ORGANIZED/VibeGuard_Mechanical_Lab_Request_Letters_Sreeprada.pdf"
    pdf2_down = "/home/paradoxpete/Downloads/VibeGuard_Mechanical_Lab_Request_Letters_Sreeprada.pdf"
    generate_doc(pdf2_ws, pdf2_down, s_nihad, s_sreeprada)

if __name__ == "__main__":
    main()
