#!/usr/bin/env python3
"""
Generates 4 high-resolution, publication-grade, color-coded CAD illustrations
and a multi-page PDF field guide showing EXACTLY where and how to place Vernier
Caliper jaws for every single parameter in the lab measurement ledger:

Sheet 1: N20 Micro Gear Motor (Rows 1-4)
Sheet 2: N20 U-Bracket & ADXL345 Sensor Board (Rows 5-8)
Sheet 3: Acrylic Baseplate Blanks & Stack (Rows 9-14)
Sheet 4: M3 Fasteners & DIN 125 Washers (Rows 15-16)

Also combines them into VibeGuard_Vernier_Caliper_Measurement_Visual_Guide.pdf
and mirrors all files to ~/Downloads/.
"""

import cairo
import math
import os

IMG_W = 1920
IMG_H = 1280

# Color Palette
C_BG = (0.97, 0.98, 0.99)
C_CARD_BG = (1.0, 1.0, 1.0)
C_CARD_BORDER = (0.80, 0.84, 0.88)
C_BANNER_BG = (0.08, 0.12, 0.18)
C_BANNER_TXT = (1.0, 1.0, 1.0)
C_TITLE = (0.1, 0.14, 0.2)
C_BODY = (0.25, 0.3, 0.35)
C_MUTED = (0.45, 0.5, 0.55)

# CAD Colors
C_STEEL_LIGHT = (0.90, 0.92, 0.94)
C_STEEL_MID = (0.75, 0.78, 0.82)
C_STEEL_DARK = (0.50, 0.55, 0.60)
C_BRASS_LIGHT = (0.95, 0.85, 0.50)
C_BRASS_MID = (0.85, 0.72, 0.35)
C_PCB_BLUE = (0.05, 0.35, 0.65)
C_PCB_GOLD = (0.88, 0.75, 0.30)
C_ACRYLIC = (0.85, 0.92, 0.96)
C_ACRYLIC_BORDER = (0.40, 0.65, 0.85)

# Highlighting & Dimensioning
C_RED = (0.88, 0.12, 0.12)
C_RED_BG = (1.0, 0.92, 0.92)
C_JAW_FILL = (0.85, 0.87, 0.90)
C_JAW_OUTLINE = (0.25, 0.28, 0.32)
C_ZOOM_RING = (0.15, 0.20, 0.30)
C_TAG_BG = (0.92, 0.95, 0.98)
C_TAG_TXT = (0.05, 0.25, 0.55)


def draw_header_banner(cr, title_text, subtitle_text, sheet_badge):
    cr.save()
    # Dark header banner
    cr.set_source_rgb(*C_BANNER_BG)
    cr.rectangle(0, 0, IMG_W, 110)
    cr.fill()

    # Accent line
    cr.set_source_rgb(*C_RED)
    cr.rectangle(0, 106, IMG_W, 4)
    cr.fill()

    # Title
    cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    cr.set_font_size(28.0)
    cr.set_source_rgb(*C_BANNER_TXT)
    cr.move_to(45, 48)
    cr.show_text(title_text)

    # Subtitle
    cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    cr.set_font_size(16.0)
    cr.set_source_rgb(0.8, 0.85, 0.9)
    cr.move_to(45, 82)
    cr.show_text(subtitle_text)

    # Sheet badge on right
    cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    cr.set_font_size(18.0)
    ext = cr.text_extents(sheet_badge)
    bw = ext.width + 30
    bh = 38
    bx = IMG_W - 45 - bw
    by = 36
    cr.set_source_rgb(0.2, 0.28, 0.38)
    cr.rectangle(bx, by, bw, bh)
    cr.fill()
    cr.set_source_rgb(*C_RED)
    cr.set_line_width(2.0)
    cr.rectangle(bx, by, bw, bh)
    cr.stroke()
    cr.set_source_rgb(1.0, 1.0, 1.0)
    cr.move_to(bx + 15, by + 26)
    cr.show_text(sheet_badge)

    cr.restore()


def draw_panel_card(cr, x, y, w, h, row_id_str, title_str, nominal_str, tool_str):
    cr.save()
    # Card Background
    cr.set_source_rgb(*C_CARD_BG)
    cr.rectangle(x, y, w, h)
    cr.fill()

    # Card Border
    cr.set_source_rgb(*C_CARD_BORDER)
    cr.set_line_width(1.5)
    cr.rectangle(x, y, w, h)
    cr.stroke()

    # Card Header Strip
    cr.set_source_rgb(*C_TAG_BG)
    cr.rectangle(x, y, w, 52)
    cr.fill()
    cr.set_source_rgb(*C_CARD_BORDER)
    cr.set_line_width(1.0)
    cr.move_to(x, y + 52)
    cr.line_to(x + w, y + 52)
    cr.stroke()

    # Table Row Badge
    cr.set_source_rgb(*C_RED)
    cr.rectangle(x + 16, y + 12, 120, 28)
    cr.fill()
    cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    cr.set_font_size(13.0)
    cr.set_source_rgb(1.0, 1.0, 1.0)
    cr.move_to(x + 24, y + 31)
    cr.show_text(row_id_str)

    # Title
    cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    cr.set_font_size(17.0)
    cr.set_source_rgb(*C_TITLE)
    cr.move_to(x + 148, y + 32)
    cr.show_text(title_str)

    # Nominal & Tool Sub-header
    cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    cr.set_font_size(13.5)
    cr.set_source_rgb(*C_RED)
    cr.move_to(x + 18, y + 78)
    cr.show_text(f"EXPECTED NOMINAL:  {nominal_str}")

    cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    cr.set_font_size(13.0)
    cr.set_source_rgb(*C_MUTED)
    cr.move_to(x + w - 380, y + 78)
    cr.show_text(f"TOOLING:  {tool_str}")

    cr.restore()


def draw_dimension_arrow(cr, x1, y1, x2, y2, text_str, text_offset=(0, -12), is_vertical=False):
    cr.save()
    cr.set_source_rgb(*C_RED)
    cr.set_line_width(2.5)

    # Line
    cr.move_to(x1, y1)
    cr.line_to(x2, y2)
    cr.stroke()

    # Arrowheads
    arr_size = 8.0
    if not is_vertical:
        # Left arrow
        cr.new_path()
        cr.move_to(x1, y1)
        cr.line_to(x1 + arr_size, y1 - arr_size/2)
        cr.line_to(x1 + arr_size, y1 + arr_size/2)
        cr.close_path()
        cr.fill()

        # Right arrow
        cr.new_path()
        cr.move_to(x2, y2)
        cr.line_to(x2 - arr_size, y2 - arr_size/2)
        cr.line_to(x2 - arr_size, y2 + arr_size/2)
        cr.close_path()
        cr.fill()
    else:
        # Top arrow
        cr.new_path()
        cr.move_to(x1, y1)
        cr.line_to(x1 - arr_size/2, y1 + arr_size)
        cr.line_to(x1 + arr_size/2, y1 + arr_size)
        cr.close_path()
        cr.fill()

        # Bottom arrow
        cr.new_path()
        cr.move_to(x2, y2)
        cr.line_to(x2 - arr_size/2, y2 - arr_size)
        cr.line_to(x2 + arr_size/2, y2 - arr_size)
        cr.close_path()
        cr.fill()

    # Text Box
    mx = (x1 + x2) / 2.0 + text_offset[0]
    my = (y1 + y2) / 2.0 + text_offset[1]

    cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    cr.set_font_size(15.0)
    ext = cr.text_extents(text_str)

    cr.set_source_rgb(1.0, 1.0, 1.0)
    cr.rectangle(mx - ext.width/2 - 6, my - ext.height - 2, ext.width + 12, ext.height + 6)
    cr.fill()
    cr.set_source_rgb(*C_RED)
    cr.set_line_width(1.5)
    cr.rectangle(mx - ext.width/2 - 6, my - ext.height - 2, ext.width + 12, ext.height + 6)
    cr.stroke()

    cr.move_to(mx - ext.width/2, my)
    cr.show_text(text_str)
    cr.restore()


def draw_caliper_jaw_pair_horizontal(cr, left_x, right_x, y_level, jaw_height=70.0):
    cr.save()
    cr.set_source_rgb(*C_JAW_FILL)
    cr.set_line_width(2.0)

    # Left Jaw (Fixed Anvil)
    cr.new_path()
    cr.move_to(left_x - 35, y_level - jaw_height/2)
    cr.line_to(left_x, y_level - jaw_height/2 + 8)
    cr.line_to(left_x, y_level + jaw_height/2 - 8)
    cr.line_to(left_x - 35, y_level + jaw_height/2)
    cr.close_path()
    cr.fill_preserve()
    cr.set_source_rgb(*C_JAW_OUTLINE)
    cr.stroke()

    # Right Jaw (Sliding Anvil)
    cr.set_source_rgb(*C_JAW_FILL)
    cr.new_path()
    cr.move_to(right_x + 35, y_level - jaw_height/2)
    cr.line_to(right_x, y_level - jaw_height/2 + 8)
    cr.line_to(right_x, y_level + jaw_height/2 - 8)
    cr.line_to(right_x + 35, y_level + jaw_height/2)
    cr.close_path()
    cr.fill_preserve()
    cr.set_source_rgb(*C_JAW_OUTLINE)
    cr.stroke()

    # Jaw contact points (red dots)
    cr.set_source_rgb(*C_RED)
    cr.arc(left_x, y_level, 4.5, 0, 2*math.pi)
    cr.fill()
    cr.arc(right_x, y_level, 4.5, 0, 2*math.pi)
    cr.fill()

    cr.restore()


def draw_caliper_jaw_pair_vertical(cr, x_level, top_y, bottom_y, jaw_width=70.0):
    cr.save()
    cr.set_source_rgb(*C_JAW_FILL)
    cr.set_line_width(2.0)

    # Top Jaw
    cr.new_path()
    cr.move_to(x_level - jaw_width/2, top_y - 30)
    cr.line_to(x_level - jaw_width/2 + 8, top_y)
    cr.line_to(x_level + jaw_width/2 - 8, top_y)
    cr.line_to(x_level + jaw_width/2, top_y - 30)
    cr.close_path()
    cr.fill_preserve()
    cr.set_source_rgb(*C_JAW_OUTLINE)
    cr.stroke()

    # Bottom Jaw
    cr.set_source_rgb(*C_JAW_FILL)
    cr.new_path()
    cr.move_to(x_level - jaw_width/2, bottom_y + 30)
    cr.line_to(x_level - jaw_width/2 + 8, bottom_y)
    cr.line_to(x_level + jaw_width/2 - 8, bottom_y)
    cr.line_to(x_level + jaw_width/2, bottom_y + 30)
    cr.close_path()
    cr.fill_preserve()
    cr.set_source_rgb(*C_JAW_OUTLINE)
    cr.stroke()

    # Contact points
    cr.set_source_rgb(*C_RED)
    cr.arc(x_level, top_y, 4.5, 0, 2*math.pi)
    cr.fill()
    cr.arc(x_level, bottom_y, 4.5, 0, 2*math.pi)
    cr.fill()

    cr.restore()


def draw_inside_nibs(cr, left_x, right_x, y_level, nib_len=35.0):
    cr.save()
    cr.set_source_rgb(*C_JAW_FILL)
    cr.set_line_width(2.0)

    # Left nib pointing left outwards
    cr.new_path()
    cr.move_to(left_x + 18, y_level - nib_len)
    cr.line_to(left_x, y_level)
    cr.line_to(left_x + 18, y_level + 10)
    cr.close_path()
    cr.fill_preserve()
    cr.set_source_rgb(*C_JAW_OUTLINE)
    cr.stroke()

    # Right nib pointing right outwards
    cr.set_source_rgb(*C_JAW_FILL)
    cr.new_path()
    cr.move_to(right_x - 18, y_level - nib_len)
    cr.line_to(right_x, y_level)
    cr.line_to(right_x - 18, y_level + 10)
    cr.close_path()
    cr.fill_preserve()
    cr.set_source_rgb(*C_JAW_OUTLINE)
    cr.stroke()

    # Red contact points
    cr.set_source_rgb(*C_RED)
    cr.arc(left_x, y_level, 4.0, 0, 2*math.pi)
    cr.fill()
    cr.arc(right_x, y_level, 4.0, 0, 2*math.pi)
    cr.fill()

    cr.restore()


# ==============================================================================
# SHEET 1: N20 MICRO GEAR MOTOR (TABLE ROWS 1 - 4)
# ==============================================================================
def render_sheet_1(filename):
    surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, IMG_W, IMG_H)
    cr = cairo.Context(surf)

    # Background
    cr.set_source_rgb(*C_BG)
    cr.paint()

    draw_header_banner(cr, "VIBEGUARD COMPONENT MEASUREMENT GUIDE",
                       "Field Verification Protocols • Section 2.3 Ledger Rows 1 to 4",
                       "SHEET 01: N20 MOTOR")

    card_w = (IMG_W - 45*3) / 2
    card_h = (IMG_H - 110 - 45*3) / 2
    x1 = 45
    x2 = 45*2 + card_w
    y1 = 110 + 35
    y2 = y1 + card_h + 30

    # --------------------------------------------------------------------------
    # PANEL 1: N20 Shaft Outer Diameter (OD)
    # --------------------------------------------------------------------------
    draw_panel_card(cr, x1, y1, card_w, card_h,
                    "TABLE ROW 1", "N20 Shaft Outer Diameter (OD)",
                    "3.00 mm  (Typical: 2.95 – 2.98 mm)",
                    "Outside Measuring Jaws (Flat Anvils)")

    # Drawing: N20 Motor Outline (Isometric/Side)
    mx = x1 + 140
    my = y1 + 250
    # Motor body
    cr.set_source_rgb(*C_STEEL_LIGHT)
    cr.rectangle(mx, my - 60, 160, 120)
    cr.fill_preserve()
    cr.set_source_rgb(*C_STEEL_DARK)
    cr.set_line_width(2.0)
    cr.stroke()
    # Gearbox face
    cr.set_source_rgb(*C_BRASS_MID)
    cr.rectangle(mx + 160, my - 60, 50, 120)
    cr.fill_preserve()
    cr.set_source_rgb(*C_STEEL_DARK)
    cr.stroke()
    # Brass Collar
    cr.set_source_rgb(*C_BRASS_LIGHT)
    cr.rectangle(mx + 210, my - 25, 15, 50)
    cr.fill_preserve()
    cr.set_source_rgb(*C_STEEL_DARK)
    cr.stroke()
    # Steel Shaft
    cr.set_source_rgb(*C_STEEL_LIGHT)
    cr.rectangle(mx + 225, my - 15, 95, 30)
    cr.fill_preserve()
    cr.set_source_rgb(*C_STEEL_DARK)
    cr.stroke()
    # D-Cut Flat representation
    cr.set_source_rgb(0.85, 0.85, 0.85)
    cr.rectangle(mx + 245, my - 15, 75, 8)
    cr.fill()

    # Zoom Inset: End-On Shaft Diameter
    zx = x1 + card_w - 210
    zy = y1 + 250
    zr = 110.0

    # Loupe guide lines
    cr.set_source_rgb(*C_MUTED)
    cr.set_line_width(1.5)
    cr.set_dash([4.0, 4.0])
    cr.move_to(mx + 270, my - 15)
    cr.line_to(zx - zr, zy - 40)
    cr.move_to(mx + 270, my + 15)
    cr.line_to(zx - zr, zy + 40)
    cr.stroke()
    cr.set_dash([])

    # Loupe circle background
    cr.set_source_rgb(1.0, 1.0, 1.0)
    cr.new_path()
    cr.arc(zx, zy, zr, 0, 2*math.pi)
    cr.fill_preserve()
    cr.set_source_rgb(*C_ZOOM_RING)
    cr.set_line_width(4.0)
    cr.stroke()

    # Loupe label
    cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    cr.set_font_size(13.0)
    cr.set_source_rgb(*C_TAG_TXT)
    cr.move_to(zx - 95, zy - zr - 8)
    cr.show_text("ZOOM: SHAFT CROSS-SECTION")

    # Enlarged round shaft in loupe
    sr = 55.0
    cr.set_source_rgb(*C_STEEL_LIGHT)
    cr.new_path()
    cr.arc(zx, zy, sr, 0, 2*math.pi)
    cr.fill_preserve()
    cr.set_source_rgb(*C_STEEL_DARK)
    cr.set_line_width(2.5)
    cr.stroke()

    # Outside Jaws gripping left and right
    draw_caliper_jaw_pair_horizontal(cr, zx - sr, zx + sr, zy, jaw_height=100)
    draw_dimension_arrow(cr, zx - sr, zy, zx + sr, zy, "OD = 3.00 mm", text_offset=(0, -14))

    # Notes box at bottom of card
    cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    cr.set_font_size(13.5)
    cr.set_source_rgb(*C_BODY)
    cr.move_to(x1 + 25, y1 + card_h - 45)
    cr.show_text("• WHERE TO MEASURE: Clamp jaws across the full cylindrical shaft section near the tip.")
    cr.move_to(x1 + 25, y1 + card_h - 22)
    cr.show_text("• CRITICAL CHECK: Do not measure across the D-flat! Rotor arm bore relies on this exact diameter.")

    # --------------------------------------------------------------------------
    # PANEL 2: N20 D-Flat Chord Thickness
    # --------------------------------------------------------------------------
    draw_panel_card(cr, x2, y1, card_w, card_h,
                    "TABLE ROW 2", "N20 D-Flat Chord Thickness",
                    "2.50 mm  (Typical: 2.45 – 2.48 mm)",
                    "Outside Measuring Jaws (Flat to Curve)")

    # Zoom Inset: End-On D-Profile
    zx2 = x2 + 250
    zy2 = y1 + 250
    zr2 = 120.0

    # Loupe circle
    cr.set_source_rgb(1.0, 1.0, 1.0)
    cr.new_path()
    cr.arc(zx2, zy2, zr2, 0, 2*math.pi)
    cr.fill_preserve()
    cr.set_source_rgb(*C_ZOOM_RING)
    cr.set_line_width(4.0)
    cr.stroke()

    # Loupe title
    cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    cr.set_font_size(13.0)
    cr.set_source_rgb(*C_TAG_TXT)
    cr.move_to(zx2 - 85, zy2 - zr2 - 8)
    cr.show_text("ZOOM: D-CUT PROFILE VIEW")

    # Draw D-Shaft profile (circle truncated at top)
    sr2 = 65.0
    flat_y = zy2 - 30.0
    angle = math.acos(30.0 / sr2)

    cr.save()
    cr.set_source_rgb(*C_STEEL_LIGHT)
    cr.new_path()
    cr.arc(zx2, zy2, sr2, -angle, math.pi + angle)
    cr.line_to(zx2 + sr2 * math.sin(angle), flat_y)
    cr.close_path()
    cr.fill_preserve()
    cr.set_source_rgb(*C_STEEL_DARK)
    cr.set_line_width(3.0)
    cr.stroke()

    # Top flat chord highlight
    cr.set_source_rgb(*C_RED)
    cr.set_line_width(4.0)
    cr.move_to(zx2 - sr2 * math.sin(angle), flat_y)
    cr.line_to(zx2 + sr2 * math.sin(angle), flat_y)
    cr.stroke()
    cr.restore()

    # Caliper Jaws: Top Jaw flat on D-Cut, Bottom Jaw tangent to curved bottom
    draw_caliper_jaw_pair_vertical(cr, zx2, flat_y, zy2 + sr2, jaw_width=110)
    draw_dimension_arrow(cr, zx2 - 80, flat_y, zx2 - 80, zy2 + sr2, "Chord = 2.50 mm",
                         text_offset=(-85, 0), is_vertical=True)

    # Guidance text on right side of card
    gx = x2 + 450
    gy = y1 + 160
    cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    cr.set_font_size(15.0)
    cr.set_source_rgb(*C_TITLE)
    cr.move_to(gx, gy)
    cr.show_text("HOW TO POSITION CALIPER:")

    guide_steps = [
        "1. Rest the fixed flat anvil of caliper directly on the flat face.",
        "2. Ensure the jaw sits 100% flush (do NOT tilt or angle).",
        "3. Gently close moving jaw until it touches the curved back.",
        "4. Nominal reading is exactly 2.50 mm.",
        "-> If measured < 2.44 mm, rotor arm requires smaller CAD flat.",
        "-> If measured > 2.52 mm, rotor arm flat bore must be enlarged."
    ]
    cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    cr.set_font_size(13.0)
    for idx, s in enumerate(guide_steps):
        cr.set_source_rgb(*C_RED if idx >= 4 else C_BODY)
        cr.move_to(gx, gy + 28 + idx * 24)
        cr.show_text(s)

    # --------------------------------------------------------------------------
    # PANEL 3: N20 Usable Shaft Length
    # --------------------------------------------------------------------------
    draw_panel_card(cr, x1, y2, card_w, card_h,
                    "TABLE ROW 3", "N20 Usable Shaft Length",
                    "9.50 mm  (Typical: 9.0 – 10.0 mm)",
                    "Vernier Depth Probe or Stepped Jaws")

    # Motor drawing side elevation
    sx = x1 + 100
    sy = y2 + 250
    # Gearbox
    cr.set_source_rgb(*C_BRASS_LIGHT)
    cr.rectangle(sx, sy - 80, 100, 160)
    cr.fill_preserve()
    cr.set_source_rgb(*C_STEEL_DARK)
    cr.set_line_width(2.0)
    cr.stroke()

    # Front Brass Collar Reference Shoulder
    collar_w = 20
    collar_h = 70
    cr.set_source_rgb(*C_BRASS_MID)
    cr.rectangle(sx + 100, sy - collar_h/2, collar_w, collar_h)
    cr.fill_preserve()
    cr.set_source_rgb(*C_STEEL_DARK)
    cr.stroke()

    # Protruding Shaft
    shaft_len = 220
    cr.set_source_rgb(*C_STEEL_LIGHT)
    cr.rectangle(sx + 100 + collar_w, sy - 22, shaft_len, 44)
    cr.fill_preserve()
    cr.set_source_rgb(*C_STEEL_DARK)
    cr.stroke()

    # Reference Plane Lines
    ref_x = sx + 100 + collar_w
    tip_x = ref_x + shaft_len
    cr.set_source_rgb(*C_RED)
    cr.set_line_width(2.0)
    cr.set_dash([4.0, 3.0])
    cr.move_to(ref_x, sy - 90)
    cr.line_to(ref_x, sy + 90)
    cr.move_to(tip_x, sy - 90)
    cr.line_to(tip_x, sy + 90)
    cr.stroke()
    cr.set_dash([])

    # Caliper Depth Probe / Step Representation
    cr.set_source_rgb(*C_JAW_FILL)
    # Caliper beam butt resting against collar
    cr.rectangle(ref_x - 50, sy - 110, 50, 40)
    cr.fill_preserve()
    cr.set_source_rgb(*C_JAW_OUTLINE)
    cr.set_line_width(1.5)
    cr.stroke()
    # Depth rod extending to tip
    cr.set_source_rgb(0.7, 0.72, 0.75)
    cr.rectangle(ref_x, sy - 95, shaft_len, 10)
    cr.fill_preserve()
    cr.set_source_rgb(*C_JAW_OUTLINE)
    cr.stroke()

    # Dimension Arrow
    draw_dimension_arrow(cr, ref_x, sy + 70, tip_x, sy + 70, "Usable Length = 9.50 mm", text_offset=(0, -14))

    # Notes
    cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    cr.set_font_size(13.5)
    cr.set_source_rgb(*C_BODY)
    cr.move_to(x1 + 25, y2 + card_h - 45)
    cr.show_text("• REFERENCE DATUM: Measure from the front face of the brass collar (where rotor hub stops).")
    cr.move_to(x1 + 25, y2 + card_h - 22)
    cr.show_text("• ROTOR LIMIT: The 3D printed rotor arm hub must not exceed this length to prevent shaft end rubbing.")

    # --------------------------------------------------------------------------
    # PANEL 4: N20 Motor Body Width
    # --------------------------------------------------------------------------
    draw_panel_card(cr, x2, y2, card_w, card_h,
                    "TABLE ROW 4", "N20 Motor Body Width",
                    "12.00 mm  (Typical: 11.9 – 12.1 mm)",
                    "Outside Measuring Jaws (Across Gearbox Flange)")

    # Motor Body Front/End View
    bx = x2 + 230
    by = y2 + 250
    bw = 140.0
    bh = 180.0

    # Gearbox body rectangular shape
    cr.set_source_rgb(*C_BRASS_LIGHT)
    cr.rectangle(bx - bw/2, by - bh/2, bw, bh)
    cr.fill_preserve()
    cr.set_source_rgb(*C_STEEL_DARK)
    cr.set_line_width(2.5)
    cr.stroke()

    # Center bearing & D-shaft
    cr.set_source_rgb(*C_STEEL_LIGHT)
    cr.new_path()
    cr.arc(bx, by, 32, 0, 2*math.pi)
    cr.fill_preserve()
    cr.set_source_rgb(*C_STEEL_DARK)
    cr.stroke()

    # M1.6 Mounting screws on face
    cr.set_source_rgb(0.4, 0.4, 0.4)
    cr.new_path()
    cr.arc(bx - 45, by, 7.0, 0, 2*math.pi)
    cr.fill()
    cr.new_path()
    cr.arc(bx + 45, by, 7.0, 0, 2*math.pi)
    cr.fill()

    # Caliper Outside Jaws clamping across the 12.0 mm width
    draw_caliper_jaw_pair_horizontal(cr, bx - bw/2, bx + bw/2, by, jaw_height=140)
    draw_dimension_arrow(cr, bx - bw/2, by - bh/2 - 30, bx + bw/2, by - bh/2 - 30,
                         "Width = 12.00 mm", text_offset=(0, -14))

    # Guidance text on right
    gx4 = x2 + 430
    gy4 = y2 + 160
    cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    cr.set_font_size(15.0)
    cr.set_source_rgb(*C_TITLE)
    cr.move_to(gx4, gy4)
    cr.show_text("CRITICAL FIT IMPORTANCE:")

    fit_notes = [
        "• Metal U-Bracket Clearance: The stamped metal bracket cradle",
        "  has an internal gap of ~12.2 mm.",
        "• If the motor body is > 12.1 mm, it will bind inside the bracket.",
        "• If the motor body is < 11.9 mm, use thin shim tape to prevent",
        "  radial rocking under 600 RPM eccentric unbalance."
    ]
    cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    cr.set_font_size(13.0)
    for idx, fn in enumerate(fit_notes):
        cr.set_source_rgb(*C_BODY)
        cr.move_to(gx4, gy4 + 28 + idx * 24)
        cr.show_text(fn)

    surf.write_to_png(filename)
    print(f"[Image 1] Generated: {filename}")


# ==============================================================================
# SHEET 2: N20 U-BRACKET & ADXL345 SENSOR BOARD (TABLE ROWS 5 - 8)
# ==============================================================================
def render_sheet_2(filename):
    surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, IMG_W, IMG_H)
    cr = cairo.Context(surf)

    cr.set_source_rgb(*C_BG)
    cr.paint()

    draw_header_banner(cr, "VIBEGUARD COMPONENT MEASUREMENT GUIDE",
                       "Field Verification Protocols • Section 2.3 Ledger Rows 5 to 8",
                       "SHEET 02: BRACKET & SENSOR")

    card_w = (IMG_W - 45*3) / 2
    card_h = (IMG_H - 110 - 45*3) / 2
    x1 = 45
    x2 = 45*2 + card_w
    y1 = 110 + 35
    y2 = y1 + card_h + 30

    # --------------------------------------------------------------------------
    # PANEL 5: N20 Bracket Base Hole Pitch
    # --------------------------------------------------------------------------
    draw_panel_card(cr, x1, y1, card_w, card_h,
                    "TABLE ROW 5", "N20 Bracket Base Hole Pitch",
                    "17.00 mm  (Pitch Between Base Slots)",
                    "Inside Nibs (Tangent Method: L_outer - D)")

    # Bracket Base Top View
    bx = x1 + 220
    by = y1 + 240
    bw = 280.0
    bh = 100.0

    cr.set_source_rgb(*C_STEEL_LIGHT)
    cr.rectangle(bx - bw/2, by - bh/2, bw, bh)
    cr.fill_preserve()
    cr.set_source_rgb(*C_STEEL_DARK)
    cr.set_line_width(2.5)
    cr.stroke()

    # Bracket upright ears (indicated at ends)
    cr.set_source_rgb(*C_STEEL_MID)
    cr.rectangle(bx - bw/2, by - bh/2, 25, bh)
    cr.fill()
    cr.rectangle(bx + bw/2 - 25, by - bh/2, 25, bh)
    cr.fill()

    # Two mounting slots (pitch = 17.0 mm nom -> represented visually with scale)
    pitch_vis = 120.0
    h1_x = bx - pitch_vis/2
    h2_x = bx + pitch_vis/2
    slot_r = 18.0

    # Draw slots
    for hx in [h1_x, h2_x]:
        cr.set_source_rgb(1.0, 1.0, 1.0)
        cr.arc(hx, by, slot_r, 0, 2*math.pi)
        cr.fill_preserve()
        cr.set_source_rgb(*C_STEEL_DARK)
        cr.set_line_width(2.0)
        cr.stroke()
        # Center mark
        cr.set_source_rgb(*C_RED)
        cr.arc(hx, by, 3.0, 0, 2*math.pi)
        cr.fill()

    # Inside Nibs measuring inside span L_inner
    draw_inside_nibs(cr, h1_x + slot_r, h2_x - slot_r, by, nib_len=40)

    # Dimension Arrow for Pitch
    draw_dimension_arrow(cr, h1_x, by - 60, h2_x, by - 60, "Pitch P = 17.00 mm", text_offset=(0, -14))

    # Formula Callout Box on Right
    fx = x1 + 400
    fy = y1 + 170
    cr.set_source_rgb(*C_TAG_BG)
    cr.rectangle(fx, fy, 440, 150)
    cr.fill()
    cr.set_source_rgb(*C_TAG_TXT)
    cr.set_line_width(1.5)
    cr.rectangle(fx, fy, 440, 150)
    cr.stroke()

    cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    cr.set_font_size(14.0)
    cr.move_to(fx + 18, fy + 28)
    cr.show_text("EXACT CALIPER PITCH FORMULA:")

    cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    cr.set_font_size(12.5)
    cr.set_source_rgb(*C_TITLE)
    cr.move_to(fx + 18, fy + 58)
    cr.show_text("• Method 1: Pitch = L_inner + D_hole")
    cr.move_to(fx + 18, fy + 82)
    cr.show_text("• Method 2: Pitch = L_outer - D_hole")
    cr.set_source_rgb(*C_RED)
    cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    cr.move_to(fx + 18, fy + 115)
    cr.show_text("-> Guarantees ±0.02 mm accuracy without guessing centerlines!")

    # --------------------------------------------------------------------------
    # PANEL 6: ADXL345 PCB Hole Diameter
    # --------------------------------------------------------------------------
    draw_panel_card(cr, x2, y1, card_w, card_h,
                    "TABLE ROW 6", "ADXL345 PCB Hole Diameter",
                    "3.20 mm  (M3 Clearance Check)",
                    "Inside Measuring Nibs (Delicate Insert)")

    # ADXL345 PCB Diagram
    px = x2 + 180
    py = y1 + 240
    pw = 180.0
    ph = 140.0

    cr.set_source_rgb(*C_PCB_BLUE)
    cr.rectangle(px - pw/2, py - ph/2, pw, ph)
    cr.fill_preserve()
    cr.set_source_rgb(0.02, 0.15, 0.35)
    cr.set_line_width(2.0)
    cr.stroke()

    # Corner mounting holes
    hole_inset = 28.0
    hole_r = 14.0
    hx1 = px - pw/2 + hole_inset
    hy1 = py - ph/2 + hole_inset
    hx2 = px + pw/2 - hole_inset
    hy2 = hy1

    for hx, hy in [(hx1, hy1), (hx2, hy2)]:
        cr.set_source_rgb(*C_PCB_GOLD)
        cr.arc(hx, hy, hole_r + 4, 0, 2*math.pi)
        cr.fill()
        cr.set_source_rgb(1.0, 1.0, 1.0)
        cr.arc(hx, hy, hole_r, 0, 2*math.pi)
        cr.fill()

    # Zoom Inset: Close-up of Single Plated Hole
    zx = x2 + card_w - 240
    zy = y1 + 240
    zr = 120.0

    # Loupe circle
    cr.set_source_rgb(1.0, 1.0, 1.0)
    cr.new_path()
    cr.arc(zx, zy, zr, 0, 2*math.pi)
    cr.fill_preserve()
    cr.set_source_rgb(*C_ZOOM_RING)
    cr.set_line_width(4.0)
    cr.stroke()

    cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    cr.set_font_size(13.0)
    cr.set_source_rgb(*C_TAG_TXT)
    cr.move_to(zx - 95, zy - zr - 8)
    cr.show_text("ZOOM: PCB MOUNTING HOLE")

    # Enlarged hole with gold annular ring
    big_hr = 50.0
    cr.set_source_rgb(*C_PCB_GOLD)
    cr.new_path()
    cr.arc(zx, zy, big_hr + 16, 0, 2*math.pi)
    cr.fill()
    cr.set_source_rgb(0.95, 0.95, 0.95)
    cr.new_path()
    cr.arc(zx, zy, big_hr, 0, 2*math.pi)
    cr.fill_preserve()
    cr.set_source_rgb(0.3, 0.3, 0.3)
    cr.set_line_width(2.0)
    cr.stroke()

    # Inside nibs touching hole edges
    draw_inside_nibs(cr, zx - big_hr, zx + big_hr, zy, nib_len=55)
    draw_dimension_arrow(cr, zx - big_hr, zy, zx + big_hr, zy, "ID = 3.20 mm", text_offset=(0, -14))

    # Notes
    cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    cr.set_font_size(13.0)
    cr.set_source_rgb(*C_BODY)
    cr.move_to(x2 + 25, y1 + card_h - 45)
    cr.show_text("• PASS CRITERION: M3 screw shank (OD 2.92 mm) must pass through without catching.")
    cr.move_to(x2 + 25, y1 + card_h - 22)
    cr.show_text("• CAUTION: Do not force inside nibs with high pressure; PCB annular copper ring can deform.")

    # --------------------------------------------------------------------------
    # PANEL 7: ADXL345 Hole Center Pitch
    # --------------------------------------------------------------------------
    draw_panel_card(cr, x1, y2, card_w, card_h,
                    "TABLE ROW 7", "ADXL345 Hole Center Pitch",
                    "15.00 mm  (Dictates Sensor Bracket Spacing)",
                    "Inside Nibs or Outside Tangent Jaws")

    # Dual PCB Holes Close-Up
    p7_x = x1 + 260
    p7_y = y2 + 240
    p7_pitch = 180.0
    p7_h1 = p7_x - p7_pitch/2
    p7_h2 = p7_x + p7_pitch/2
    p7_r = 30.0

    # Board background strip
    cr.set_source_rgb(*C_PCB_BLUE)
    cr.rectangle(p7_x - p7_pitch/2 - 60, p7_y - 70, p7_pitch + 120, 140)
    cr.fill()

    for hx in [p7_h1, p7_h2]:
        cr.set_source_rgb(*C_PCB_GOLD)
        cr.arc(hx, p7_y, p7_r + 8, 0, 2*math.pi)
        cr.fill()
        cr.set_source_rgb(1.0, 1.0, 1.0)
        cr.arc(hx, p7_y, p7_r, 0, 2*math.pi)
        cr.fill_preserve()
        cr.set_source_rgb(0.2, 0.2, 0.2)
        cr.stroke()

    # Caliper Outside Jaws measuring L_outer
    l_outer_left = p7_h1 - p7_r
    l_outer_right = p7_h2 + p7_r
    draw_caliper_jaw_pair_horizontal(cr, l_outer_left, l_outer_right, p7_y, jaw_height=90)

    # Top Arrow: L_outer
    draw_dimension_arrow(cr, l_outer_left, p7_y - 80, l_outer_right, p7_y - 80,
                         "L_outer = 18.20 mm", text_offset=(0, -14))
    # Bottom Arrow: Pitch
    draw_dimension_arrow(cr, p7_h1, p7_y + 80, p7_h2, p7_y + 80,
                         "Pitch = 15.00 mm", text_offset=(0, 18))

    # Right side explanation
    gx7 = x1 + 480
    gy7 = y2 + 160
    cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    cr.set_font_size(15.0)
    cr.set_source_rgb(*C_TITLE)
    cr.move_to(gx7, gy7)
    cr.show_text("VERIFICATION CALCULATION:")

    calc_lines = [
        "1. Measure outside span: L_outer = 18.20 mm",
        "2. Measure single hole ID: D = 3.20 mm",
        "3. Compute True Pitch: P = 18.20 - 3.20 = 15.00 mm",
        "-> CRITICAL CHECK: Sensor bracket upright holes must be designed",
        "   at exactly this measured pitch (15.00 mm) ±0.05 mm."
    ]
    cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    cr.set_font_size(13.0)
    for idx, cl in enumerate(calc_lines):
        cr.set_source_rgb(*C_RED if idx >= 3 else C_BODY)
        cr.move_to(gx7, gy7 + 28 + idx * 24)
        cr.show_text(cl)

    # --------------------------------------------------------------------------
    # PANEL 8: ADXL345 PCB Dimensions (W × L)
    # --------------------------------------------------------------------------
    draw_panel_card(cr, x2, y2, card_w, card_h,
                    "TABLE ROW 8", "ADXL345 PCB Dimensions (W × L)",
                    "15.5 mm × 20.5 mm  (Thickness: 1.6 mm)",
                    "Outside Measuring Jaws (Substrate Outline)")

    # Full PCB Layout
    p8_x = x2 + 240
    p8_y = y2 + 250
    p8_w = 200.0  # representing 20.5 mm
    p8_h = 150.0  # representing 15.5 mm

    cr.set_source_rgb(*C_PCB_BLUE)
    cr.rectangle(p8_x - p8_w/2, p8_y - p8_h/2, p8_w, p8_h)
    cr.fill_preserve()
    cr.set_source_rgb(0.02, 0.15, 0.35)
    cr.set_line_width(2.5)
    cr.stroke()

    # ADXL345 IC chip in center
    cr.set_source_rgb(0.12, 0.12, 0.12)
    cr.rectangle(p8_x - 22, p8_y - 22, 44, 44)
    cr.fill()

    # Header pin pads at bottom
    for i in range(8):
        hpx = p8_x - p8_w/2 + 20 + i * 22
        hpy = p8_y + p8_h/2 - 14
        cr.set_source_rgb(*C_PCB_GOLD)
        cr.arc(hpx, hpy, 6.0, 0, 2*math.pi)
        cr.fill_preserve()
        cr.set_source_rgb(0.2, 0.2, 0.2)
        cr.stroke()

    # Dimension Arrows: Width (Vertical) and Length (Horizontal)
    draw_dimension_arrow(cr, p8_x - p8_w/2, p8_y - p8_h/2 - 25, p8_x + p8_w/2, p8_y - p8_h/2 - 25,
                         "Length = 20.5 mm", text_offset=(0, -14))

    draw_dimension_arrow(cr, p8_x + p8_w/2 + 25, p8_y - p8_h/2, p8_x + p8_w/2 + 25, p8_y + p8_h/2,
                         "Width = 15.5 mm", text_offset=(80, 0), is_vertical=True)

    # Inset: Side View Thickness & Solder Pins
    tx = x2 + 540
    ty = y2 + 180
    cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    cr.set_font_size(14.5)
    cr.set_source_rgb(*C_TITLE)
    cr.move_to(tx, ty)
    cr.show_text("SIDE FLANGE & HEADER CLEARANCE:")

    flange_notes = [
        "• PCB Substrate Thickness: 1.60 mm.",
        "• Rear Solder Joints: Pins protrude 1.0 – 1.5 mm on back.",
        "• 3D Bracket Recess: The vertical mount wall MUST have",
        "  a recessed pocket or standoffs to prevent the solder blobs",
        "  from preventing flush bracket contact."
    ]
    cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    cr.set_font_size(13.0)
    for idx, fn in enumerate(flange_notes):
        cr.set_source_rgb(*C_RED if idx == 2 else C_BODY)
        cr.move_to(tx, ty + 26 + idx * 24)
        cr.show_text(fn)

    surf.write_to_png(filename)
    print(f"[Image 2] Generated: {filename}")


# ==============================================================================
# SHEET 3: ACRYLIC BASEPLATE & STACK (TABLE ROWS 9 - 14)
# ==============================================================================
def render_sheet_3(filename):
    surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, IMG_W, IMG_H)
    cr = cairo.Context(surf)

    cr.set_source_rgb(*C_BG)
    cr.paint()

    draw_header_banner(cr, "VIBEGUARD COMPONENT MEASUREMENT GUIDE",
                       "Field Verification Protocols • Section 2.3 Ledger Rows 9 to 14",
                       "SHEET 03: ACRYLIC BASEPLATE")

    card_w = (IMG_W - 45*3) / 2
    card_h = (IMG_H - 110 - 45*3) / 2
    x1 = 45
    x2 = 45*2 + card_w
    y1 = 110 + 35
    y2 = y1 + card_h + 30

    # --------------------------------------------------------------------------
    # PANEL 9 & 10: Acrylic Sheet 1 & 2 Thickness
    # --------------------------------------------------------------------------
    draw_panel_card(cr, x1, y1, card_w, card_h,
                    "TABLE ROWS 9 & 10", "Acrylic Sheet 1 & 2 Individual Thickness",
                    "5.00 mm per sheet  (Expected: 4.6 – 5.2 mm)",
                    "Outside Measuring Jaws (Check All 4 Corners)")

    # Drawing: Edge profile of single sheet
    ex = x1 + 200
    ey = y1 + 250
    ew = 160.0
    eh = 80.0  # representing 5 mm

    cr.set_source_rgb(*C_ACRYLIC)
    cr.rectangle(ex - ew/2, ey - eh/2, ew, eh)
    cr.fill_preserve()
    cr.set_source_rgb(*C_ACRYLIC_BORDER)
    cr.set_line_width(2.5)
    cr.stroke()

    # Jaws clamping vertically on edge
    draw_caliper_jaw_pair_vertical(cr, ex, ey - eh/2, ey + eh/2, jaw_width=80)
    draw_dimension_arrow(cr, x1 + 310, ey - eh/2, x1 + 310, ey + eh/2, "T1 = 5.00 mm",
                         text_offset=(0, 0), is_vertical=True)

    # Guidance text on right
    tx1 = x1 + 420
    ty1 = y1 + 160
    cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    cr.set_font_size(14.5)
    cr.set_source_rgb(*C_TITLE)
    cr.move_to(tx1, ty1)
    cr.show_text("4-CORNER THICKNESS PROTOCOL:")

    thk_steps = [
        "1. Measure Sheet 1 at Corner 1, 2, 3, 4.",
        "2. Record average in Trial 1 column.",
        "3. Repeat independently for Sheet 2 in Trial 2 column.",
        "• Cast PMMA Tolerance: Cast acrylic has ±10% thickness variation.",
        "• A sheet labeled '5 mm' often measures 4.75 mm or 5.15 mm.",
        "-> Knowing true gauge prevents bolt thread bottoming!"
    ]
    cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    cr.set_font_size(13.0)
    for idx, ts in enumerate(thk_steps):
        cr.set_source_rgb(*C_RED if idx >= 4 else C_BODY)
        cr.move_to(tx1, ty1 + 26 + idx * 24)
        cr.show_text(ts)

    # --------------------------------------------------------------------------
    # PANEL 11: Combined Stack Thickness
    # --------------------------------------------------------------------------
    draw_panel_card(cr, x2, y1, card_w, card_h,
                    "TABLE ROW 11", "Combined Stack Thickness (Dual 5 mm PMMA)",
                    "10.00 mm Total  (Determines M3 Bolt Grip)",
                    "Outside Measuring Jaws (Clamped Sandwich)")

    # Drawing: Two stacked sheets
    sx = x2 + 200
    sy = y1 + 250
    sw = 160.0
    sh1 = 60.0
    sh2 = 60.0

    # Top sheet
    cr.set_source_rgb(*C_ACRYLIC)
    cr.rectangle(sx - sw/2, sy - sh1, sw, sh1)
    cr.fill_preserve()
    cr.set_source_rgb(*C_ACRYLIC_BORDER)
    cr.set_line_width(2.0)
    cr.stroke()

    # Bottom sheet
    cr.set_source_rgb(0.78, 0.88, 0.94)
    cr.rectangle(sx - sw/2, sy, sw, sh2)
    cr.fill_preserve()
    cr.set_source_rgb(*C_ACRYLIC_BORDER)
    cr.stroke()

    # Seam line (dashed muted line)
    cr.set_source_rgb(*C_MUTED)
    cr.set_line_width(1.5)
    cr.set_dash([4.0, 3.0])
    cr.move_to(sx - sw/2, sy)
    cr.line_to(sx + sw/2, sy)
    cr.stroke()
    cr.set_dash([])

    # Caliper clamping across both sheets
    draw_caliper_jaw_pair_vertical(cr, sx, sy - sh1, sy + sh2, jaw_width=80)
    draw_dimension_arrow(cr, x2 + 310, sy - sh1, x2 + 310, sy + sh2, "Stack = 10.00 mm",
                         text_offset=(0, 0), is_vertical=True)

    # Guidance text
    tx2 = x2 + 420
    ty2 = y1 + 160
    cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    cr.set_font_size(14.5)
    cr.set_source_rgb(*C_TITLE)
    cr.move_to(tx2, ty2)
    cr.show_text("FASTENER ENGAGEMENT CALCULATION:")

    fast_steps = [
        "• Clamped Stack Thickness = 10.00 mm",
        "• Bracket Foot Flange = 3.50 mm",
        "• DIN 125 Washer = 0.50 mm",
        "• M3 Nylon Locknut Height = 4.00 mm",
        "-> TOTAL GRIP LENGTH REQUIRED = 18.0 mm",
        "-> VERIFICATION: Standard M3 x 20 mm bolts provide",
        "   exactly 2 mm thread protrusion past the nylon ring (SAFE)!"
    ]
    cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    cr.set_font_size(13.0)
    for idx, fs in enumerate(fast_steps):
        cr.set_source_rgb(*C_RED if idx >= 4 else C_BODY)
        cr.move_to(tx2, ty2 + 26 + idx * 24)
        cr.show_text(fs)

    # --------------------------------------------------------------------------
    # PANEL 12 & 13: Acrylic Blank 1 & 2 Width × Length
    # --------------------------------------------------------------------------
    draw_panel_card(cr, x1, y2, card_w, card_h,
                    "TABLE ROWS 12 & 13", "Acrylic Blank 1 & 2 Width × Length",
                    "150.0 mm × 150.0 mm  (Square Cut Check)",
                    "Caliper Long Beam (Check Edge Flushness)")

    # Plate Outline
    px = x1 + 200
    py = y2 + 260
    pw = 150.0
    ph = 150.0

    cr.set_source_rgb(*C_ACRYLIC)
    cr.rectangle(px - pw/2, py - ph/2, pw, ph)
    cr.fill_preserve()
    cr.set_source_rgb(*C_ACRYLIC_BORDER)
    cr.set_line_width(2.5)
    cr.stroke()

    # Dimension arrows
    draw_dimension_arrow(cr, px - pw/2, py - ph/2 - 25, px + pw/2, py - ph/2 - 25,
                         "Width = 150.0 mm", text_offset=(0, -14))

    draw_dimension_arrow(cr, x1 + 310, py - ph/2, x1 + 310, py + ph/2,
                         "Length = 150.0 mm", text_offset=(0, 0), is_vertical=True)

    # Notes
    tx3 = x1 + 420
    ty3 = y2 + 160
    cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    cr.set_font_size(14.5)
    cr.set_source_rgb(*C_TITLE)
    cr.move_to(tx3, ty3)
    cr.show_text("EDGE FLUSHNESS CHECK:")

    edge_steps = [
        "1. Stack Blank 1 on Blank 2.",
        "2. Run finger along all 4 perimeter seams.",
        "3. Measure edge overhang (step mismatch).",
        "• PASS CRITERION: Overhang must be < 0.5 mm.",
        "• If edges differ, file the wider edge flush BEFORE drilling",
        "  to ensure 1:1 sticker template lines up on both plates."
    ]
    cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    cr.set_font_size(13.0)
    for idx, es in enumerate(edge_steps):
        cr.set_source_rgb(*C_RED if idx >= 3 else C_BODY)
        cr.move_to(tx3, ty3 + 26 + idx * 24)
        cr.show_text(es)

    # --------------------------------------------------------------------------
    # PANEL 14: Acrylic Diagonals (D1 vs D2)
    # --------------------------------------------------------------------------
    draw_panel_card(cr, x2, y2, card_w, card_h,
                    "TABLE ROW 14", "Acrylic Squareness Diagonals (D1 vs D2)",
                    "212.13 mm  (sqrt(150² + 150²))",
                    "Caliper Diagonal Span")

    # Square with diagonal cross
    dx = x2 + 200
    dy = y2 + 260
    dw = 150.0
    dh = 150.0

    c1 = (dx - dw/2, dy - dh/2)
    c2 = (dx + dw/2, dy - dh/2)
    c3 = (dx - dw/2, dy + dh/2)
    c4 = (dx + dw/2, dy + dh/2)

    cr.set_source_rgb(*C_ACRYLIC)
    cr.rectangle(c1[0], c1[1], dw, dh)
    cr.fill_preserve()
    cr.set_source_rgb(*C_ACRYLIC_BORDER)
    cr.set_line_width(2.5)
    cr.stroke()

    # Diagonal D1 (C1 to C4)
    cr.set_source_rgb(*C_RED)
    cr.set_line_width(2.5)
    cr.move_to(c1[0], c1[1])
    cr.line_to(c4[0], c4[1])
    cr.stroke()

    # Diagonal D2 (C2 to C3)
    cr.set_source_rgb(*C_TAG_TXT)
    cr.set_line_width(2.5)
    cr.set_dash([4.0, 3.0])
    cr.move_to(c2[0], c2[1])
    cr.line_to(c3[0], c3[1])
    cr.stroke()
    cr.set_dash([])

    # Diagonal Labels
    cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    cr.set_font_size(13.5)
    cr.set_source_rgb(*C_RED)
    cr.move_to(dx - 35, dy - 20)
    cr.show_text("D1 = 212.1 mm")
    cr.set_source_rgb(*C_TAG_TXT)
    cr.move_to(dx - 35, dy + 35)
    cr.show_text("D2 = 212.1 mm")

    # Right side explanation
    tx4 = x2 + 420
    ty4 = y2 + 160
    cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    cr.set_font_size(14.5)
    cr.set_source_rgb(*C_TITLE)
    cr.move_to(tx4, ty4)
    cr.show_text("SQUARENESS VERIFICATION RULE:")

    diag_rules = [
        "• Pythagorean Theorem: sqrt(150^2 + 150^2) = 212.13 mm.",
        "• If D1 == D2 (within ±0.5 mm): The blank is a TRUE SQUARE.",
        "• If D1 != D2 (e.g. D1=213.5, D2=210.7):",
        "  The blank has PARALLELOGRAM SKEW.",
        "-> If skewed, do NOT use outside edges for hole reference;",
        "   use the taped 1:1 sticker template crosshairs exclusively!"
    ]
    cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    cr.set_font_size(13.0)
    for idx, dr in enumerate(diag_rules):
        cr.set_source_rgb(*C_RED if idx >= 2 else C_BODY)
        cr.move_to(tx4, ty4 + 26 + idx * 24)
        cr.show_text(dr)

    surf.write_to_png(filename)
    print(f"[Image 3] Generated: {filename}")


# ==============================================================================
# SHEET 4: M3 FASTENERS & DIN 125 WASHERS (TABLE ROWS 15 - 16)
# ==============================================================================
def render_sheet_4(filename):
    surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, IMG_W, IMG_H)
    cr = cairo.Context(surf)

    cr.set_source_rgb(*C_BG)
    cr.paint()

    draw_header_banner(cr, "VIBEGUARD COMPONENT MEASUREMENT GUIDE",
                       "Field Verification Protocols • Section 2.3 Ledger Rows 15 to 16",
                       "SHEET 04: HARDWARE FASTENERS")

    card_w = (IMG_W - 45*3) / 2
    card_h = (IMG_H - 110 - 45*3)
    x1 = 45
    x2 = 45*2 + card_w
    y1 = 110 + 35

    # --------------------------------------------------------------------------
    # PANEL 15: M3 Bolt Shank Major Diameter
    # --------------------------------------------------------------------------
    draw_panel_card(cr, x1, y1, card_w, card_h,
                    "TABLE ROW 15", "M3 Bolt Thread Shank Major Diameter",
                    "2.92 mm  (Commercial Range: 2.87 – 2.98 mm)",
                    "Outside Measuring Jaws (Across Thread Crests)")

    # Large M3 Bolt Drawing
    bx = x1 + card_w/2 - 50
    by = y1 + 360

    # Bolt Head (Socket Head Cap Screw)
    head_w = 90
    head_h = 130
    cr.set_source_rgb(*C_STEEL_MID)
    cr.rectangle(bx - 140, by - head_h/2, head_w, head_h)
    cr.fill_preserve()
    cr.set_source_rgb(*C_STEEL_DARK)
    cr.set_line_width(3.0)
    cr.stroke()

    # Hex socket in head
    cr.set_source_rgb(0.2, 0.2, 0.2)
    cr.rectangle(bx - 120, by - 35, 40, 70)
    cr.fill()

    # Threaded Shank
    shank_len = 380
    shank_h = 75  # representing 2.92 mm
    cr.set_source_rgb(*C_STEEL_LIGHT)
    cr.rectangle(bx - 50, by - shank_h/2, shank_len, shank_h)
    cr.fill_preserve()
    cr.set_source_rgb(*C_STEEL_DARK)
    cr.stroke()

    # Thread ridges representation
    cr.set_source_rgb(0.65, 0.7, 0.75)
    for i in range(18):
        tx = bx - 40 + i * 20
        cr.move_to(tx, by - shank_h/2)
        cr.line_to(tx + 8, by + shank_h/2)
        cr.stroke()

    # Caliper Outside Jaws clamping vertically on thread crests
    meas_x = bx + 160
    draw_caliper_jaw_pair_vertical(cr, meas_x, by - shank_h/2, by + shank_h/2, jaw_width=100)
    draw_dimension_arrow(cr, meas_x + 80, by - shank_h/2, meas_x + 80, by + shank_h/2,
                         "Major OD = 2.92 mm", text_offset=(100, 0), is_vertical=True)

    # Detailed Explanation Below
    ey = by + 160
    cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    cr.set_font_size(17.0)
    cr.set_source_rgb(*C_TITLE)
    cr.move_to(x1 + 35, ey)
    cr.show_text("CRITICAL CLEARANCE PHYSICS (M3 IN Ø3.3 mm HOLE):")

    bolt_rules = [
        "1. Free Slip Verification: Thread major OD must measure < 2.98 mm.",
        "   In our Ø3.30 mm drilled hole, this yields exactly 175 µm radial clearance.",
        "2. Zero Binding: The bolt will slide through both 5 mm acrylic sheets without",
        "   requiring any clockwise twisting or forcing.",
        "3. Brittle Failure Prevention: If an M3 screw is forced into a Ø3.0 mm hole, the",
        "   thread crests bite and exert hoop tensile stress > 70 MPa, cracking acrylic!",
        "-> RESULT: Ø3.3 mm hole + 2.92 mm bolt = 100% reliable, crack-free mounting."
    ]
    cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    cr.set_font_size(14.0)
    for idx, br in enumerate(bolt_rules):
        cr.set_source_rgb(*C_RED if idx >= 5 else C_BODY)
        cr.move_to(x1 + 35, ey + 32 + idx * 26)
        cr.show_text(br)

    # --------------------------------------------------------------------------
    # PANEL 16: DIN 125 Washer Outer Diameter
    # --------------------------------------------------------------------------
    draw_panel_card(cr, x2, y1, card_w, card_h,
                    "TABLE ROW 16", "DIN 125 M3 Flat Washer Dimensions",
                    "Outer Diameter: 7.00 mm  •  Bore ID: 3.20 mm",
                    "Outside Jaws (OD) & Inside Nibs (ID)")

    # Large Washer Drawing
    wx = x2 + card_w/2
    wy = y1 + 360
    wash_or = 175.0  # representing 7.00 mm
    wash_ir = 80.0   # representing 3.20 mm

    # Annular ring
    cr.set_source_rgb(*C_STEEL_LIGHT)
    cr.new_path()
    cr.arc(wx, wy, wash_or, 0, 2*math.pi)
    cr.fill_preserve()
    cr.set_source_rgb(*C_STEEL_DARK)
    cr.set_line_width(3.0)
    cr.stroke()

    # Inner hole
    cr.set_source_rgb(*C_CARD_BG)
    cr.new_path()
    cr.arc(wx, wy, wash_ir, 0, 2*math.pi)
    cr.fill_preserve()
    cr.set_source_rgb(*C_STEEL_DARK)
    cr.set_line_width(2.5)
    cr.stroke()

    # Solid Bearing Shelf Highlight (Greenish / Red tint)
    cr.set_source_rgb(0.2, 0.7, 0.3)
    cr.set_line_width(3.0)
    cr.new_path()
    cr.arc(wx, wy, (wash_or + wash_ir)/2, -0.3, 0.3)
    cr.stroke()

    # Caliper Outside Jaws measuring OD
    draw_caliper_jaw_pair_horizontal(cr, wx - wash_or, wx + wash_or, wy, jaw_height=180)
    draw_dimension_arrow(cr, wx - wash_or, wy - wash_or - 35, wx + wash_or, wy - wash_or - 35,
                         "Outer Diameter = 7.00 mm", text_offset=(0, -16))

    # Inside nibs measuring ID
    draw_inside_nibs(cr, wx - wash_ir, wx + wash_ir, wy, nib_len=55)
    draw_dimension_arrow(cr, wx - wash_ir, wy + wash_ir + 35, wx + wash_ir, wy + wash_ir + 35,
                         "Inner Bore ID = 3.20 mm", text_offset=(0, 20))

    # Bearing Shelf Annotation
    cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    cr.set_font_size(15.0)
    cr.set_source_rgb(*C_RED)
    cr.move_to(wx + wash_ir + 15, wy - 10)
    cr.show_text("Solid Shelf = 1.85 mm")

    # Detailed Explanation Below
    cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    cr.set_font_size(17.0)
    cr.set_source_rgb(*C_TITLE)
    cr.move_to(x2 + 35, ey)
    cr.show_text("BEARING SURFACE AREA & PULL-THROUGH SAFETY:")

    wash_rules = [
        "1. Bearing Shelf per Side = (OD - Hole_Dia) / 2 = (7.00 - 3.30) / 2 = 1.85 mm.",
        "2. Effective Bearing Area = π/4 * (7.0^2 - 3.3^2) = 29.93 mm².",
        "3. Contact Retention: Retains 98.4% of standard ISO bearing area.",
        "4. Clamping Force Distribution: 4 tightened corner M3 washers distribute",
        "   ~3,500 N force uniformly across 120 mm² of acrylic, preventing crazing.",
        "-> ZERO RISK OF BOLT PULL-THROUGH even under intense motor vibration!"
    ]
    cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    cr.set_font_size(14.0)
    for idx, wr in enumerate(wash_rules):
        cr.set_source_rgb(*C_RED if idx >= 4 else C_BODY)
        cr.move_to(x2 + 35, ey + 32 + idx * 26)
        cr.show_text(wr)

    surf.write_to_png(filename)
    print(f"[Image 4] Generated: {filename}")


# ==============================================================================
# MASTER PDF COMPILATION (COMBINING ALL 4 SHEETS INTO PRINTABLE A4 LANDSCAPE)
# ==============================================================================
def compile_visual_guide_pdf(pdf_path, png_files):
    # A4 Landscape: 841.89 x 595.28 pt
    PAGE_W = 841.89
    PAGE_H = 595.28

    surf = cairo.PDFSurface(pdf_path, PAGE_W, PAGE_H)
    cr = cairo.Context(surf)

    for png in png_files:
        img_surf = cairo.ImageSurface.create_from_png(png)
        cr.save()
        scale_x = PAGE_W / IMG_W
        scale_y = PAGE_H / IMG_H
        cr.scale(scale_x, scale_y)
        cr.set_source_surface(img_surf, 0, 0)
        cr.paint()
        cr.restore()
        cr.show_page()

    surf.finish()
    print(f"[PDF Visual Guide] Generated: {pdf_path}")


def main():
    ws_dir = "/home/paradoxpete/Documents/PROJECT_ORGANIZED"
    dl_dir = "/home/paradoxpete/Downloads"

    png_names = [
        "VibeGuard_Caliper_Guide_01_N20_Motor.png",
        "VibeGuard_Caliper_Guide_02_Bracket_and_Sensor.png",
        "VibeGuard_Caliper_Guide_03_Acrylic_Baseplate.png",
        "VibeGuard_Caliper_Guide_04_Hardware_Fasteners.png"
    ]

    ws_pngs = [os.path.join(ws_dir, name) for name in png_names]
    dl_pngs = [os.path.join(dl_dir, name) for name in png_names]

    # Generate the 4 master images
    render_sheet_1(ws_pngs[0])
    render_sheet_2(ws_pngs[1])
    render_sheet_3(ws_pngs[2])
    render_sheet_4(ws_pngs[3])

    # Mirror PNGs to Downloads
    for ws_p, dl_p in zip(ws_pngs, dl_pngs):
        with open(ws_p, "rb") as src, open(dl_p, "wb") as dst:
            dst.write(src.read())
        print(f"[Mirror PNG] Copied to: {dl_p}")

    # Generate combined visual guide PDF
    pdf_ws = os.path.join(ws_dir, "VibeGuard_Vernier_Caliper_Measurement_Visual_Guide.pdf")
    pdf_dl = os.path.join(dl_dir, "VibeGuard_Vernier_Caliper_Measurement_Visual_Guide.pdf")

    compile_visual_guide_pdf(pdf_ws, ws_pngs)

    with open(pdf_ws, "rb") as src, open(pdf_dl, "wb") as dst:
        dst.write(src.read())
    print(f"[Mirror PDF] Copied to: {pdf_dl}")


if __name__ == "__main__":
    main()
