import os, struct, math
from PIL import Image, ImageDraw, ImageFont

def render_stl_to_image(stl_path, size=(600, 420), rot_x=22, rot_y=-35, base_col=(56, 189, 248), edge_col=(14, 116, 144)):
    with open(stl_path, 'rb') as f:
        f.read(80)
        count = struct.unpack('<I', f.read(4))[0]
        facets = []
        for _ in range(count):
            d = struct.unpack('<3f 3f 3f 3f H', f.read(50))
            facets.append((d[0:3], d[3:6], d[6:9], d[9:12]))

    all_v = [v for facet in facets for v in facet[1:]]
    cx = sum(v[0] for v in all_v) / len(all_v)
    cy = sum(v[1] for v in all_v) / len(all_v)
    cz = sum(v[2] for v in all_v) / len(all_v)

    rad_x, rad_y = math.radians(rot_x), math.radians(rot_y)

    def proj(v):
        x, y, z = v[0] - cx, v[1] - cy, v[2] - cz
        x1 = x * math.cos(rad_y) + z * math.sin(rad_y)
        y1 = y
        z1 = -x * math.sin(rad_y) + z * math.cos(rad_y)
        x2 = x1
        y2 = y1 * math.cos(rad_x) - z1 * math.sin(rad_x)
        z2 = y1 * math.sin(rad_x) + z1 * math.cos(rad_x)
        return x2, y2, z2

    proj_facets = []
    for norm, v1, v2, v3 in facets:
        p1, p2, p3 = proj(v1), proj(v2), proj(v3)
        ax, ay, az = p2[0]-p1[0], p2[1]-p1[1], p2[2]-p1[2]
        bx, by, bz = p3[0]-p1[0], p3[1]-p1[1], p3[2]-p1[2]
        nx, ny, nz = ay*bz - az*by, az*bx - ax*bz, ax*by - ay*bx
        length = math.sqrt(nx*nx + ny*ny + nz*nz) or 1.0
        nx, ny, nz = nx/length, ny/length, nz/length
        avg_z = (p1[2] + p2[2] + p3[2]) / 3.0
        proj_facets.append((avg_z, nz, p1, p2, p3))

    max_d = max(max(abs(p[0]) for f in proj_facets for p in f[2:]),
                max(abs(p[1]) for f in proj_facets for p in f[2:]))
    scale = (min(size) * 0.44) / (max_d or 1.0)
    proj_facets.sort(key=lambda x: x[0])

    img = Image.new('RGBA', size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    for avg_z, nz, p1, p2, p3 in proj_facets:
        dot = max(0.18, min(1.0, 0.42 + 0.58 * nz))
        col = (int(base_col[0] * dot), int(base_col[1] * dot), int(base_col[2] * dot), 255)
        pts = [
            (size[0]/2 + p1[0]*scale, size[1]/2 - p1[1]*scale),
            (size[0]/2 + p2[0]*scale, size[1]/2 - p2[1]*scale),
            (size[0]/2 + p3[0]*scale, size[1]/2 - p3[1]*scale)
        ]
        draw.polygon(pts, fill=col, outline=edge_col)
    return img

def create_figure4(output_path):
    W, H = 3200, 1800
    sheet = Image.new('RGB', (W, H), '#07111E')
    draw = ImageDraw.Draw(sheet)

    # Fonts
    f_path = '/usr/share/fonts/google-noto-vf/NotoSans[wght].ttf'
    font_main_hdr = ImageFont.truetype(f_path, 42)
    font_sub_hdr = ImageFont.truetype(f_path, 20)
    font_sec_hdr = ImageFont.truetype(f_path, 26)
    font_sub_sec = ImageFont.truetype(f_path, 18)
    font_body = ImageFont.truetype(f_path, 18)
    font_bold = ImageFont.truetype(f_path, 20)
    font_small = ImageFont.truetype(f_path, 16)

    # Header Banner
    header_h = 120
    draw.rectangle([(0, 0), (W, header_h)], fill='#0B1E36')
    draw.rectangle([(0, header_h - 4), (W, header_h)], fill='#0284C7')

    draw.text((60, 24), "VIBEGUARD MECHANICAL TESTBED: RIGID BASEPLATE BLUEPRINT & RAPID FABRICATION SPECIFICATION", fill='#FFFFFF', font=font_main_hdr)
    draw.text((60, 78), "Precision Acrylic Drilling Datum, 3D CAD Component Projections (FAB-01 & FAB-02) & Structural Vibration Coupling Architecture", fill='#38BDF8', font=font_sub_hdr)

    # Left Section: Acrylic Baseplate Blueprint
    margin = 50
    left_w = 1600
    panel_y = 150
    panel_h = H - panel_y - margin

    draw.rounded_rectangle([(margin, panel_y), (margin + left_w, panel_y + panel_h)], radius=12, fill='#0B1728', outline='#1E293B', width=2)
    draw.rounded_rectangle([(margin, panel_y), (margin + left_w, panel_y + 56)], radius=12, fill='#112240')
    draw.text((margin + 24, panel_y + 12), "PANEL A: 150 × 150 mm ACRYLIC BASEPLATE DRILLING BLUEPRINT & HOLE LOCATION MATRIX", fill='#38BDF8', font=font_sec_hdr)

    # Embed Blueprint
    bp_path = 'VibeGuard_Baseplate_Drilling_Blueprint_Exact.png'
    if os.path.exists(bp_path):
        bp_img = Image.open(bp_path)
        # fit inside left panel: available w = left_w - 40, h = panel_h - 80
        avail_w = left_w - 40
        avail_h = panel_h - 80
        bp_ratio = min(avail_w / bp_img.width, avail_h / bp_img.height)
        new_w, new_h = int(bp_img.width * bp_ratio), int(bp_img.height * bp_ratio)
        bp_resized = bp_img.resize((new_w, new_h), Image.Resampling.LANCZOS)
        paste_x = margin + 20 + (avail_w - new_w) // 2
        paste_y = panel_y + 68 + (avail_h - new_h) // 2
        sheet.paste(bp_resized, (paste_x, paste_y))

    # Right Section: CAD Models and Assembly Specs
    right_x = margin + left_w + 30
    right_w = W - right_x - margin

    # Right Box 1: FAB-01 Eccentric Arm
    box1_h = 480
    draw.rounded_rectangle([(right_x, panel_y), (right_x + right_w, panel_y + box1_h)], radius=12, fill='#0B1728', outline='#1E293B', width=2)
    draw.rounded_rectangle([(right_x, panel_y), (right_x + right_w, panel_y + 50)], radius=12, fill='#064E3B')
    draw.text((right_x + 20, panel_y + 10), "FAB-01: ECCENTRIC ROTOR ARM (3D CAD PROJECTION & UNBALANCE EXCITATION)", fill='#34D399', font=font_sec_hdr)

    stl1 = '07_SEMESTER_EXECUTION/03_Hardware_and_CAD/VibeGuard_Rotor_Arm_D_Shaft.stl'
    if os.path.exists(stl1):
        im_fab01 = render_stl_to_image(stl1, size=(520, 360), rot_x=28, rot_y=42, base_col=(52, 211, 153), edge_col=(5, 150, 105))
        sheet.paste(im_fab01, (right_x + 20, panel_y + 70), im_fab01)

    # FAB-01 Specs Text
    tx_fab01 = right_x + 550
    ty1 = panel_y + 70
    draw.text((tx_fab01, ty1), "CAD GEOMETRIC SPECIFICATIONS:", fill='#A7F3D0', font=font_bold)
    lines_fab01 = [
        "• Part Envelope: 20.25 mm (L) × 8.50 mm (W) × 8.00 mm (D)",
        "• Material & Density: PLA / PETG @ 100% Solid Infill (Rigid)",
        "• Motor Shaft Bore: Ø3.00 mm with 2.50 mm D-flat chord",
        "  - Tight interference press-fit onto N20 motor output shaft",
        "• Counterweight Offset Bore: Ø3.20 mm at 15.00 mm pitch",
        "  - Retains M3 bolt & nut for adjustable eccentric mass (m)",
        "• Centrifugal Unbalance Function: F_c = m · r · ω²",
        "  - Induces calibrated 10.0 Hz 1X harmonic vibration at 600 RPM"
    ]
    for idx, l in enumerate(lines_fab01):
        draw.text((tx_fab01, ty1 + 32 + idx * 30), l, fill='#E2E8F0', font=font_body)

    # Right Box 2: FAB-02 Sensor L-Bracket
    box2_y = panel_y + box1_h + 20
    box2_h = 510
    draw.rounded_rectangle([(right_x, box2_y), (right_x + right_w, box2_y + box2_h)], radius=12, fill='#0B1728', outline='#1E293B', width=2)
    draw.rounded_rectangle([(right_x, box2_y), (right_x + right_w, box2_y + 50)], radius=12, fill='#0C4A6E')
    draw.text((right_x + 20, box2_y + 10), "FAB-02: RIGID SENSOR L-BRACKET (ACOUSTIC COUPLING & ZERO DAMPING)", fill='#38BDF8', font=font_sec_hdr)

    stl2 = '07_SEMESTER_EXECUTION/03_Hardware_and_CAD/VibeGuard_ADXL345_Rigid_Mount.stl'
    if os.path.exists(stl2):
        im_fab02 = render_stl_to_image(stl2, size=(520, 390), rot_x=22, rot_y=-35, base_col=(56, 189, 248), edge_col=(14, 116, 144))
        sheet.paste(im_fab02, (right_x + 20, box2_y + 70), im_fab02)

    # FAB-02 Specs Text
    tx_fab02 = right_x + 550
    ty2 = box2_y + 70
    draw.text((tx_fab02, ty2), "CAD GEOMETRIC SPECIFICATIONS:", fill='#BAE6FD', font=font_bold)
    lines_fab02 = [
        "• Part Envelope: 24.00 mm (W) × 18.00 mm (D) × 22.00 mm (H)",
        "• Material & Density: PLA / PETG @ 100% Solid Infill (Rigid)",
        "• Baseplate Mount Holes (S1, S2): 2× Ø3.30 mm at 15.00 mm pitch",
        "  - Rigidly bolted directly into acrylic 20 mm adjacent to motor",
        "• Upright Sensor Mount Holes: 2× Ø3.20 mm at 15.00 mm pitch",
        "  - Retains ADXL345 PCB flush to vertical wall with M3 hardware",
        "• Triangular Gusset Reinforcement: 90° structural web",
        "  - Elevates bracket natural resonance (>1.6 kHz) far above Nyquist",
        "• ZERO DAMPING MANDATE: Direct rigid mechanical bolting;",
        "  NO rubber/foam grommets. Ensures 100% vibration transmission."
    ]
    for idx, l in enumerate(lines_fab02):
        draw.text((tx_fab02, ty2 + 32 + idx * 30), l, fill='#E2E8F0', font=font_body)

    # Right Box 3: Hardware Integration & Fastener Matrix
    box3_y = box2_y + box2_h + 20
    box3_h = panel_y + panel_h - box3_y
    draw.rounded_rectangle([(right_x, box3_y), (right_x + right_w, panel_y + panel_h)], radius=12, fill='#0B1728', outline='#1E293B', width=2)
    draw.rounded_rectangle([(right_x, box3_y), (right_x + right_w, box3_y + 50)], radius=12, fill='#78350F')
    draw.text((right_x + 20, box3_y + 10), "STRUCTURAL RIG ASSEMBLY & POWER ISOLATION INTEGRATION PROTOCOL", fill='#FDE68A', font=font_sec_hdr)

    # 6 Verified Integration Checkpoints in a 2-column grid
    col_w_b3 = (right_w - 40) // 2
    c1_x = right_x + 15
    c2_x = right_x + 25 + col_w_b3

    items_c1 = [
        ("1. Acrylic Baseplate Sandwich", "Dual-sheet cast acrylic (4.20 mm + 4.60 mm = 8.80 mm net) clamped rigidly at 4 corners. No flexing under 600 RPM."),
        ("2. Grade 8.8 Fasteners & Nyloc", "M3×20 mm hex bolts clamped with DIN 985 Nyloc locking nuts (7.4 thread collar engagement; zero back-out under vibration)."),
        ("3. Low-Noise Sensor Ribbon", "5-wire shielded ribbon harness (3.3V, GND, CS, SCL, SDO) routed directly to MB-102 breadboard; strain-relieved.")
    ]

    items_c2 = [
        ("4. 100% Galvanic Motor Isolation", "12V inductive motor domain has zero electrical return to 3.3V logic (measured open-circuit infinity ohms)."),
        ("5. Back-EMF Flyback Protection", "1N4007 diode clamped anti-parallel directly across N20 motor terminals (+ to -), eliminating inductive kickback."),
        ("6. Inrush & Short-Circuit Safety", "5×20 mm inline 1.0A 250V time-delay fuse and KCD1 master power toggle switch on positive 12V rail.")
    ]

    card_h_b3 = 110
    card_gap_b3 = 14
    start_y_b3 = box3_y + 66

    for idx, (title, desc) in enumerate(items_c1):
        cy = start_y_b3 + idx * (card_h_b3 + card_gap_b3)
        draw.rounded_rectangle([(c1_x, cy), (c1_x + col_w_b3, cy + card_h_b3)], radius=8, fill='#111C2E', outline='#1E293B', width=1)
        draw.text((c1_x + 14, cy + 10), title, fill='#FCD34D', font=font_bold)
        # wrap desc at 58 chars
        words = desc.split()
        l1, l2 = "", ""
        for w in words:
            if len(l1 + " " + w) <= 52:
                l1 = l1 + " " + w if l1 else w
            else:
                l2 = l2 + " " + w if l2 else w
        draw.text((c1_x + 14, cy + 42), l1, fill='#E2E8F0', font=font_small)
        if l2:
            draw.text((c1_x + 14, cy + 70), l2, fill='#E2E8F0', font=font_small)

    for idx, (title, desc) in enumerate(items_c2):
        cy = start_y_b3 + idx * (card_h_b3 + card_gap_b3)
        draw.rounded_rectangle([(c2_x, cy), (c2_x + col_w_b3, cy + card_h_b3)], radius=8, fill='#111C2E', outline='#1E293B', width=1)
        draw.text((c2_x + 14, cy + 10), title, fill='#FCD34D', font=font_bold)
        words = desc.split()
        l1, l2 = "", ""
        for w in words:
            if len(l1 + " " + w) <= 52:
                l1 = l1 + " " + w if l1 else w
            else:
                l2 = l2 + " " + w if l2 else w
        draw.text((c2_x + 14, cy + 42), l1, fill='#E2E8F0', font=font_small)
        if l2:
            draw.text((c2_x + 14, cy + 70), l2, fill='#E2E8F0', font=font_small)

    sheet.save(output_path, quality=95)
    print(f"Successfully generated authentic Figure 4 engineering drawing: {output_path}")

if __name__ == '__main__':
    out_fig4 = '/home/paradoxpete/Documents/PROJECT_ORGANIZED/07_SEMESTER_EXECUTION/03_Hardware_and_CAD/VibeGuard_Mechanical_Rig_Engineering_Assembly.png'
    create_figure4(out_fig4)
