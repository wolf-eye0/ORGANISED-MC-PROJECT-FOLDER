#!/usr/bin/env python3
"""
Generate professional PDF and DOCX for VibeGuard FabLab Slicer & Printability Guide.
Optimized for Amith Krishna Das and the College FabLab 3D print technician.
"""

import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

def generate_pdf(output_path):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=32,
        bottomMargin=32
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=18,
        textColor=colors.HexColor('#0F2942'),
        alignment=TA_CENTER
    )
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13,
        textColor=colors.HexColor('#1E6091'),
        alignment=TA_CENTER
    )
    meta_style = ParagraphStyle(
        'DocMeta',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor('#4A5568'),
        alignment=TA_CENTER
    )
    h2_style = ParagraphStyle(
        'Heading2',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        textColor=colors.HexColor('#0F2942'),
        spaceBefore=5,
        spaceAfter=3
    )
    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor('#2D3748')
    )
    body_bold = ParagraphStyle(
        'BodyBold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor('#2D3748')
    )
    alert_box_style = ParagraphStyle(
        'AlertBox',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor('#9C4221')
    )
    th_style = ParagraphStyle(
        'TH',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.5,
        leading=9.5,
        textColor=colors.white,
        alignment=TA_CENTER
    )
    td_style = ParagraphStyle(
        'TD',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.2,
        leading=9.5,
        textColor=colors.HexColor('#1A202C')
    )
    td_bold = ParagraphStyle(
        'TDBold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.2,
        leading=9.5,
        textColor=colors.HexColor('#1A202C')
    )

    story = []

    # Title & Header
    story.append(Paragraph("VIBEGUARD: COLLEGE FABLAB 3D PRINTING & SLICER GUIDE", title_style))
    story.append(Spacer(1, 2))
    story.append(Paragraph("Fast Execution Card for Hardware Lead (Amith) & FabLab 3D Printer Technician", subtitle_style))
    story.append(Spacer(1, 3))
    story.append(Paragraph("<b>Target Rig:</b> 10 Hz / 600 RPM Unbalance Testbed &nbsp;|&nbsp; <b>Baseplate:</b> Drilled Acrylic Stack &nbsp;|&nbsp; <b>Total Est. Mass:</b> ~10g PLA (Rs. 40–50) &nbsp;|&nbsp; <b>Print Time:</b> ~40 min", meta_style))
    story.append(Spacer(1, 4))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#1E6091'), spaceAfter=5))

    # CRITICAL ALERT BOX
    alert_data = [[
        Paragraph("<b>CRITICAL TECHNICIAN INSTRUCTIONS (DO NOT SKIP):</b><br/>"
                  "1. <b>ZERO SUPPORTS (0%):</b> All parts are 100% self-supporting. Do NOT add support material inside the D-bore or wire window.<br/>"
                  "2. <b>WALL PERIMETERS = 4 WALLS:</b> Ensures solid plastic around shaft bore and bolt recesses.<br/>"
                  "3. <b>PRINT ORIENTATION:</b> Print all parts flat on their bottom faces (Z=0). Never print on edge.",
                  alert_box_style)
    ]]
    alert_table = Table(alert_data, colWidths=[540])
    alert_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FFF5F5')),
        ('BOX', (0,0), (-1,-1), 1.2, colors.HexColor('#E53E3E')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(alert_table)
    story.append(Spacer(1, 5))

    # Slicer Parameter Table
    story.append(Paragraph("1. QUICK SLICER SETTING MATRIX", h2_style))
    table_data = [
        [
            Paragraph("Parameter", th_style),
            Paragraph("FAB-01: Rotor Cam Arm<br/><code>VibeGuard_Rotor_Arm_D_Shaft.stl</code>", th_style),
            Paragraph("FAB-02: ADXL345 Mount<br/><code>VibeGuard_ADXL345_Rigid_Mount.stl</code>", th_style),
            Paragraph("FAB-03: Motor Shims<br/><code>VibeGuard_N20_Motor_Shim_*.stl</code>", th_style),
        ],
        [
            Paragraph("<b>Function</b>", td_bold),
            Paragraph("Couples to N20 D-shaft; spins at 600 RPM with M3 unbalance mass", td_style),
            Paragraph("Rigid accelerometer stand; rear window passes DuPont jumper wires", td_style),
            Paragraph("Eliminates 1.0–1.2 mm gap under motor cradle for zero vibration damping", td_style),
        ],
        [
            Paragraph("<b>Print Orientation</b>", td_bold),
            Paragraph("<b>Flat on bottom face (Z=0)</b>", td_style),
            Paragraph("<b>Flat on base foot (Z=0)</b>", td_style),
            Paragraph("<b>Flat on build plate</b>", td_style),
        ],
        [
            Paragraph("<b>Support Material</b>", td_bold),
            Paragraph("<b>NONE (0% supports)</b>", td_bold),
            Paragraph("<b>NONE (0% supports — 1mm top arch bridges cleanly)</b>", td_bold),
            Paragraph("<b>NONE (0% supports)</b>", td_bold),
        ],
        [
            Paragraph("<b>Infill Density</b>", td_bold),
            Paragraph("<b>100% Solid</b> (Centrifugal stability)", td_style),
            Paragraph("<b>80% to 100%</b> (Rigid acoustic coupling)", td_style),
            Paragraph("<b>100% Solid</b> (High compressive clamp)", td_style),
        ],
        [
            Paragraph("<b>Perimeter Walls</b>", td_bold),
            Paragraph("<b>Minimum 4 walls</b> (>= 1.6 mm)", td_style),
            Paragraph("<b>Minimum 4 walls</b> (>= 1.6 mm)", td_style),
            Paragraph("3 walls", td_style),
        ],
        [
            Paragraph("<b>Layer Height</b>", td_bold),
            Paragraph("<b>0.16 mm</b> (Bore accuracy)", td_style),
            Paragraph("<b>0.16 mm – 0.20 mm</b>", td_style),
            Paragraph("0.16 mm – 0.20 mm", td_style),
        ],
        [
            Paragraph("<b>Est. Time & PLA</b>", td_bold),
            Paragraph("~12 to 14 min | 3.5 g PLA", td_style),
            Paragraph("~20 to 22 min | 5.5 g PLA", td_style),
            Paragraph("~3 to 4 min | 0.8 g PLA", td_style),
        ],
    ]

    col_widths = [90, 145, 170, 135]
    table = Table(table_data, colWidths=col_widths, repeatRows=1)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0F2942')),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E0')),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F7FAFC')]),
    ]))
    story.append(table)
    story.append(Spacer(1, 5))

    # Critical Part Features Breakdown
    story.append(Paragraph("2. KEY FABRICATION & HARDWARE COMPATIBILITY FEATURES", h2_style))
    
    feats = [
        "<b>FAB-01 Rotor Arm (3.35mm & 3.40mm Failsafe):</b> Standard model features a 3.35 mm D-bore (chord 2.775 mm) for a snug push-fit. A second failsafe model (<code>VibeGuard_Rotor_Arm_D_Shaft_3p40mm.stl</code>) with 3.40 mm bore (chord 2.825 mm) is provided to guarantee zero jamming in case of printer over-extrusion. Both feature 12.0 mm eccentric pitch and 3.20 mm M3 bolt hole.",
        "<b>FAB-02 Sensor Stand with Enlarged Window:</b> Upright M3 holes spaced 15.00 mm pitch at Z=7.0 mm matching ADXL345 PCB. Enlarged 21.6 mm (W) x 10.5 mm (H) rectangular window (Z=10.5 to 21.0 mm) fully clears the 20.32 mm black header base and 8 square DuPont female connectors (20.8 mm span). 1.0 mm top tie-bar bridges cleanly. (OpenTop U-frame variant also included in zip).",
        "<b>FAB-03 Shim Options:</b> 3 options provided (1.0 mm flat, 1.2 mm flat, 1.0 mm cradle with side rails). Amith should print the 1.0 mm cradle shim + 1.0 mm flat shim to ensure perfect motor leveling under the white U-bracket."
    ]
    for feat in feats:
        story.append(Paragraph(f"• {feat}", body_style))
        story.append(Spacer(1, 2))

    story.append(Spacer(1, 4))

    # Handover Checklist
    story.append(Paragraph("3. PRE-HANDOVER INSPECTION CHECKLIST (WHAT AMITH MUST CHECK BEFORE LEAVING LAB)", h2_style))
    checklist = [
        "[ ] <b>1. D-Shaft Push-Fit:</b> Slide FAB-01 onto N20 motor shaft. It should slide on firmly by hand without radial wobble or slipping.",
        "[ ] <b>2. ADXL345 Alignment:</b> Place physical ADXL345 board against FAB-02 upright wall. Dual M3 holes line up (15.0 mm pitch).",
        "[ ] <b>3. Wire Window Clearance:</b> Confirm rectangular window is wide open (21.6x10.5 mm) with no drooping filament strings.",
        "[ ] <b>4. Base Flatness:</b> Confirm base flanges of FAB-02 and FAB-03 sit flat on a table with zero warping.",
        "[ ] <b>5. Part Integrity:</b> 100% solid, monolithic pieces — zero layer separation or splitting along layers."
    ]
    for chk in checklist:
        story.append(Paragraph(chk, body_style))
        story.append(Spacer(1, 2))

    story.append(Spacer(1, 5))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#CBD5E0'), spaceAfter=3))
    story.append(Paragraph("<b>Files inside ZIP:</b> <code>VibeGuard_FabLab_3D_Print_Pack.zip</code> &nbsp;|&nbsp; <b>Team:</b> VibeGuard Hardware Subsystem Baseline &nbsp;|&nbsp; <b>Contact:</b> Amith Krishna Das", meta_style))

    doc.build(story)
    print(f"Successfully generated PDF: {output_path}")

def generate_docx(output_path):
    doc = docx.Document()

    # Set 0.5 in margins
    for sec in doc.sections:
        sec.top_margin = Inches(0.5)
        sec.bottom_margin = Inches(0.5)
        sec.left_margin = Inches(0.5)
        sec.right_margin = Inches(0.5)

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_title = p_title.add_run("VIBEGUARD: COLLEGE FABLAB 3D PRINTING & SLICER GUIDE")
    r_title.bold = True
    r_title.font.size = Pt(14)
    r_title.font.color.rgb = RGBColor(15, 41, 66)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = p_sub.add_run("Fast Execution Card for Hardware Lead (Amith) & FabLab 3D Printer Technician\nTarget Rig: 10 Hz / 600 RPM Unbalance Testbed | Total Est. Mass: ~10g PLA (Rs. 40–50) | Total Print Time: ~40 min")
    r_sub.font.size = Pt(9)
    r_sub.font.color.rgb = RGBColor(30, 96, 145)

    # Critical Box
    p_warn = doc.add_paragraph()
    r_warn_title = p_warn.add_run("CRITICAL TECHNICIAN INSTRUCTIONS (DO NOT SKIP):\n")
    r_warn_title.bold = True
    r_warn_title.font.color.rgb = RGBColor(180, 40, 40)
    p_warn.add_run("1. ZERO SUPPORTS (0%): All parts are 100% self-supporting. Do NOT add support material.\n"
                   "2. WALL PERIMETERS = 4 WALLS (>= 1.6 mm): Guarantees solid plastic around shaft bore and bolt holes.\n"
                   "3. PRINT ORIENTATION: Print all parts flat on their bottom faces (Z=0). Never print on edge.")

    # Section 1
    p_h1 = doc.add_paragraph()
    r_h1 = p_h1.add_run("1. QUICK SLICER SETTING MATRIX")
    r_h1.bold = True
    r_h1.font.size = Pt(11)

    table = doc.add_table(rows=8, cols=4)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.style = 'Table Grid'

    headers = [
        "Parameter",
        "FAB-01: Rotor Cam Arm\n(VibeGuard_Rotor_Arm_D_Shaft.stl)",
        "FAB-02: ADXL345 Mount (Enclosed/OpenTop)\n(VibeGuard_ADXL345_Rigid_Mount.stl)",
        "FAB-03: Under-Motor Shim\n(VibeGuard_N20_Motor_Shim_Pad_*.stl)"
    ]
    for i, h in enumerate(headers):
        cell = table.cell(0, i)
        cell.text = h
        cell.paragraphs[0].runs[0].bold = True

    rows_data = [
        ("Function", "Couples to N20 D-shaft; spins at 600 RPM with M3 unbalance mass", "Rigid accelerometer stand; enlarged 21.6x10.5 mm window fits 20.32 mm header & 8 DuPonts", "Eliminates 1.0–1.2 mm gap under motor cradle for zero vibration damping"),
        ("Print Orientation", "Flat on bottom face (Z=0)", "Flat on base foot (Z=0)", "Flat on build plate"),
        ("Support Material", "NONE (0% supports)", "NONE (0% supports — bridges cleanly)", "NONE (0% supports)"),
        ("Infill Density", "100% Solid (Centrifugal stability)", "80% to 100% (Rigid acoustic coupling)", "100% Solid (High compressive clamp)"),
        ("Perimeter Walls", "Minimum 4 walls (>= 1.6 mm)", "Minimum 4 walls (>= 1.6 mm)", "3 walls"),
        ("Layer Height", "0.16 mm (Bore accuracy)", "0.16 mm – 0.20 mm", "0.16 mm – 0.20 mm"),
        ("Est. Time & PLA", "~12 to 14 min | 3.5 g PLA", "~20 to 22 min | 5.5 g PLA", "~3 to 4 min | 0.8 g PLA")
    ]
    for row_idx, r in enumerate(rows_data):
        for col_idx in range(4):
            table.cell(row_idx + 1, col_idx).text = r[col_idx]

    # Section 2
    p_h2 = doc.add_paragraph()
    p_h2.paragraph_format.space_before = Pt(8)
    r_h2 = p_h2.add_run("2. KEY HARDWARE COMPATIBILITY FEATURES")
    r_h2.bold = True
    r_h2.font.size = Pt(11)

    feats = [
        "FAB-01 Rotor Arm (3.35mm & 3.40mm Failsafe): Standard model features 3.35 mm D-bore (+0.35 mm shrinkage allowance, chord 2.775 mm) for snug push-fit. Failsafe model (VibeGuard_Rotor_Arm_D_Shaft_3p40mm.stl) features 3.40 mm D-bore (chord 2.825 mm) to prevent jamming under heavy shrinkage. Both preserve 12.0 mm pitch and 3.20 mm M3 hole.",
        "FAB-02 Sensor Stand with Enlarged Window: Upright M3 mounting holes spaced 15.00 mm pitch at Z=7.0 mm matching Robocraze ADXL345 PCB. Enlarged 21.6 x 10.5 mm rectangular window allows 20.32 mm black header base and 8 square DuPont female connectors (20.8 mm span) to plug through without binding. OpenTop U-channel variant also included.",
        "FAB-03 Shim Options: 3 options provided (1.0 mm flat, 1.2 mm flat, 1.0 mm cradle with side rails). Amith should print 1.0 mm cradle shim + 1.0 mm flat shim."
    ]
    for feat in feats:
        doc.add_paragraph(f"• {feat}")

    # Section 3
    p_h3 = doc.add_paragraph()
    p_h3.paragraph_format.space_before = Pt(8)
    r_h3 = p_h3.add_run("3. PRE-HANDOVER CHECKLIST (WHAT AMITH MUST CHECK BEFORE LEAVING LAB)")
    r_h3.bold = True
    r_h3.font.size = Pt(11)

    checks = [
        "[ ] 1. D-Shaft Push-Fit: Slide FAB-01 onto N20 motor shaft. Firm hand push-fit without radial play.",
        "[ ] 2. ADXL345 Alignment: Place ADXL345 board against FAB-02 upright wall. Dual M3 holes line up (15.0 mm pitch).",
        "[ ] 3. Wire Window Clearance: Confirm rectangular window is wide open (18x8.5 mm) with no sagging filament strings.",
        "[ ] 4. Base Flatness: Base flanges of FAB-02 and FAB-03 sit flat on a table with zero warping.",
        "[ ] 5. Monolithic Integrity: 100% solid piece — zero layer splitting or delamination."
    ]
    for chk in checks:
        doc.add_paragraph(chk)

    doc.save(output_path)
    print(f"Successfully generated DOCX: {output_path}")

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_out = os.path.join(base_dir, 'VibeGuard_FabLab_Slicer_and_Printability_Guide.pdf')
    docx_out = os.path.join(base_dir, 'VibeGuard_FabLab_Slicer_and_Printability_Guide.docx')

    generate_pdf(pdf_out)
    generate_docx(docx_out)

if __name__ == '__main__':
    main()
