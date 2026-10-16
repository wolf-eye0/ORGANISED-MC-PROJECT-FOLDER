import os
from PIL import Image, ImageDraw, ImageFont

def create_user_journey_graphic(output_path):
    W, H = 2400, 1350
    img = Image.new("RGB", (W, H), "#F8FAFC")
    draw = ImageDraw.Draw(img)

    # Fonts
    f_path = "/usr/share/fonts/google-noto-vf/NotoSans[wght].ttf"

    font_main_title = ImageFont.truetype(f_path, 44)
    font_main_sub = ImageFont.truetype(f_path, 22)
    font_col_title = ImageFont.truetype(f_path, 26)
    font_card_num = ImageFont.truetype(f_path, 20)
    font_card_title = ImageFont.truetype(f_path, 22)
    font_card_body = ImageFont.truetype(f_path, 18)
    font_footer_hdr = ImageFont.truetype(f_path, 20)
    font_footer_val = ImageFont.truetype(f_path, 26)
    font_footer_sub = ImageFont.truetype(f_path, 16)

    # Top Header Banner
    header_h = 130
    draw.rectangle([(0, 0), (W, header_h)], fill="#0B2C5A")
    draw.rectangle([(0, header_h - 6), (W, header_h)], fill="#10B981") # emerald accent strip

    # Title text
    draw.text((60, 26), "VibeGuard: Operational Transformation & User Journey Storyboard", fill="#FFFFFF", font=font_main_title)
    draw.text((60, 84), "Comparative Manufacturing Workflow — Conventional Reactive Run-to-Failure vs. Proactive Edge-Embedded Diagnostics", fill="#93C5FD", font=font_main_sub)

    # Column Layout
    margin_x = 60
    gap_x = 50
    col_w = (W - 2 * margin_x - gap_x) // 2
    top_y = 160
    col1_x = margin_x
    col2_x = margin_x + col_w + gap_x

    # Left Column Header: BEFORE
    draw.rounded_rectangle([(col1_x, top_y), (col1_x + col_w, top_y + 56)], radius=8, fill="#DC2626")
    draw.text((col1_x + 24, top_y + 12), "BEFORE VIBEGUARD: REACTIVE RUN-TO-FAILURE (CONVENTIONAL MSME)", fill="#FFFFFF", font=font_col_title)

    # Right Column Header: AFTER
    draw.rounded_rectangle([(col2_x, top_y), (col2_x + col_w, top_y + 56)], radius=8, fill="#059669")
    draw.text((col2_x + 24, top_y + 12), "AFTER VIBEGUARD: PROACTIVE EDGE-EMBEDDED INTELLIGENCE", fill="#FFFFFF", font=font_col_title)

    # Cards Content
    before_stages = [
        ("1. Daily Startup Routine",
         "Operator switches on rotating equipment blindly. Baseline mechanical vibration is completely unrecorded, and early structural looseness goes unnoticed without instrumented logging.",
         "#991B1B"),
        ("2. Latent Fault Inception",
         "Subtle dynamic mass unbalance or shaft misalignment develops silently inside machine housing. Destructive centrifugal kinetic energy builds exponentially with speed (F = m · r · ω²).",
         "#991B1B"),
        ("3. Dynamic Shock & Stress",
         "Vibration crosses ISO safety boundaries. Periodic harmonic hammering induces bearing raceway fatigue and shaft micro-deflection. Plant operators lack quantitative severity data.",
         "#991B1B"),
        ("4. Catastrophic Breakdown",
         "Unmonitored bearing experiences sudden seizure during peak production shift. Coupling bolts shear off under centrifugal stress, generating flying projectile hazards and line halts.",
         "#991B1B"),
        ("5. Financial & Safety Result",
         "₹1,50,000+ emergency equipment repair bill, 3 weeks lost production output, acute worker safety hazards, and inability to justify commercial ₹2,00,000+ monitoring racks.",
         "#7F1D1D")
    ]

    after_stages = [
        ("1. Autonomous Boot Audit",
         "ESP32 boots in <0.5s, interrogates ADXL345 silicon register 0x00, validates DEVID 0xE5, eliminates static 1.0g Earth gravity bias, and illuminates Solid Green indicating normal baseline.",
         "#065F46"),
        ("2. Real-Time 800 Hz Sensing",
         "ADXL345 rigid L-bracket captures 3-axis vibration at 800 Hz ODR. Dual-core Xtensa processor executes in-place Euclidean Vector RMS, Crest Factor, Kurtosis, and 256-pt FFT in <1.25 ms.",
         "#065F46"),
        ("3. Multi-Stage Warning Engine",
         "Dynamic RMS transitions into ISO Zone C (Amber Alert) at 0.35g, escalating to Zone D Alarm (Solid Red LED + Buzzer) at 0.70g. K-out-of-M persistence filter prevents false alarms.",
         "#065F46"),
        ("4. Targeted Preventive Action",
         "Operator immediately responds to local visual alert, inspects the 3D WebGL Digital Twin showing isolated 10 Hz 1X unbalance peak, and performs scheduled 30-min bolt retorquing.",
         "#065F46"),
        ("5. Financial & Safety Result",
         "Zero unplanned downtime, 100% worker protection from mechanical projectile failures, laboratory-grade diagnostic precision, and complete system hardware cost under ₹3,000.",
         "#064E3B")
    ]

    card_y = top_y + 72
    card_h = 160
    card_gap = 18

    for i in range(5):
        cy = card_y + i * (card_h + card_gap)

        # Left Card (Before)
        is_last = (i == 4)
        bg_col = "#FEF2F2" if not is_last else "#FEE2E2"
        border_col = "#F87171" if not is_last else "#EF4444"
        draw.rounded_rectangle([(col1_x, cy), (col1_x + col_w, cy + card_h)], radius=10, fill=bg_col, outline=border_col, width=2)
        
        # Step tag
        tag_bg = "#DC2626"
        draw.rounded_rectangle([(col1_x + 16, cy + 16), (col1_x + 64, cy + 50)], radius=6, fill=tag_bg)
        draw.text((col1_x + 30, cy + 20), f"S{i+1}", fill="#FFFFFF", font=font_card_num)

        # Title
        b_title, b_desc, b_color = before_stages[i]
        draw.text((col1_x + 80, cy + 20), b_title, fill=b_color, font=font_card_title)

        # Body text wrapping
        # Wrap manually around 78 chars
        words = b_desc.split()
        lines = []
        curr = ""
        for w in words:
            if len(curr + " " + w) <= 68:
                curr = curr + " " + w if curr else w
            else:
                lines.append(curr)
                curr = w
        if curr:
            lines.append(curr)
        
        line_y = cy + 62
        for l in lines:
            draw.text((col1_x + 24, line_y), l, fill="#374151", font=font_card_body)
            line_y += 28

        # Right Card (After)
        bg_col_r = "#ECFDF5" if not is_last else "#D1FAE5"
        border_col_r = "#34D399" if not is_last else "#10B981"
        draw.rounded_rectangle([(col2_x, cy), (col2_x + col_w, cy + card_h)], radius=10, fill=bg_col_r, outline=border_col_r, width=2)

        # Step tag
        tag_bg_r = "#059669"
        draw.rounded_rectangle([(col2_x + 16, cy + 16), (col2_x + 64, cy + 50)], radius=6, fill=tag_bg_r)
        draw.text((col2_x + 30, cy + 20), f"S{i+1}", fill="#FFFFFF", font=font_card_num)

        # Title
        a_title, a_desc, a_color = after_stages[i]
        draw.text((col2_x + 80, cy + 20), a_title, fill=a_color, font=font_card_title)

        # Body text wrapping
        words_r = a_desc.split()
        lines_r = []
        curr_r = ""
        for w in words_r:
            if len(curr_r + " " + w) <= 68:
                curr_r = curr_r + " " + w if curr_r else w
            else:
                lines_r.append(curr_r)
                curr_r = w
        if curr_r:
            lines_r.append(curr_r)

        line_y_r = cy + 62
        for l in lines_r:
            draw.text((col2_x + 24, line_y_r), l, fill="#1F2937", font=font_card_body)
            line_y_r += 28

    # Bottom Summary Metric Banner
    bot_y = card_y + 5 * (card_h + card_gap) + 10
    bot_h = 140
    draw.rounded_rectangle([(margin_x, bot_y), (W - margin_x, bot_y + bot_h)], radius=12, fill="#0F172A")

    # 4 Metric Blocks
    metric_w = (W - 2 * margin_x) // 4
    metrics = [
        ("EQUIPMENT CAPITAL COST", "₹1,50,000+ vs. <₹3,000", "98% Reduction in Capital Expenditure", "#38BDF8"),
        ("UNPLANNED DOWNTIME", "3 Weeks vs. ZERO Hours", "Proactive Scheduled Interventions", "#34D399"),
        ("CLOUD SUBSCRIPTION FEES", "₹24,000/yr vs. ₹0 FREE", "100% Air-Gapped Edge Processing", "#FBBF24"),
        ("DETECTION LATENCY", "Post-Failure vs. <1.6 Seconds", "Real-Time ISO 10816-3 Severity Decision", "#A78BFA")
    ]

    for m_idx, (m_hdr, m_val, m_sub, m_col) in enumerate(metrics):
        mx = margin_x + m_idx * metric_w
        # Vertical divider
        if m_idx > 0:
            draw.line([(mx, bot_y + 20), (mx, bot_y + bot_h - 20)], fill="#334155", width=2)
        
        draw.text((mx + 30, bot_y + 22), m_hdr, fill="#94A3B8", font=font_footer_hdr)
        draw.text((mx + 30, bot_y + 54), m_val, fill=m_col, font=font_footer_val)
        draw.text((mx + 30, bot_y + 96), m_sub, fill="#E2E8F0", font=font_footer_sub)

    img.save(output_path, quality=95)
    print(f"Generated clean high-res user journey graphic: {output_path}")

if __name__ == "__main__":
    out = "/home/paradoxpete/Documents/PROJECT_ORGANIZED/07_SEMESTER_EXECUTION/06_Reports_and_Demonstration/VibeGuard_User_Journey_Before_After.png"
    create_user_journey_graphic(out)
