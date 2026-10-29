import re
import os
import subprocess
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls

def set_cell_shading(cell, color_hex):
    tcPr = cell._element.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=80, bottom=80, left=120, right=120):
    tcPr = cell._element.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('w:top', top), ('w:bottom', bottom), ('w:left', left), ('w:right', right)]:
        node = OxmlElement(m)
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_cell_border(cell, **kwargs):
    """
    kwargs: top, bottom, left, right
    values: dict(sz=12, val='single', color='0B2C5A', space='0')
    """
    tcPr = cell._element.get_or_add_tcPr()
    tcBorders = parse_xml(f'<w:tcBorders {nsdecls("w")}/>')
    for edge in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        edge_data = kwargs.get(edge)
        if edge_data:
            tag = f'<w:{edge} {nsdecls("w")} w:val="{edge_data.get("val","single")}" w:sz="{edge_data.get("sz",4)}" w:space="0" w:color="{edge_data.get("color","CCCCCC")}"/>'
            tcBorders.append(parse_xml(tag))
        else:
            tag = f'<w:{edge} {nsdecls("w")} w:val="none"/>'
            tcBorders.append(parse_xml(tag))
    tcPr.append(tcBorders)

def add_header_footer(doc):
    for s in doc.sections:
        footer = s.footer
        p_ft = footer.paragraphs[0]
        p_ft.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        r_ft = p_ft.add_run("VibeGuard | ASD-STE100 Specification & Defense Guide | APJ KTU 2026")
        r_ft.font.size = Pt(8.5)
        r_ft.font.color.rgb = RGBColor(120, 120, 120)

def parse_markdown_to_docx(md_path, docx_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    doc = docx.Document()
    
    # 0.75 in margins
    for section in doc.sections:
        section.top_margin = Inches(0.7)
        section.bottom_margin = Inches(0.7)
        section.left_margin = Inches(0.75)
        section.right_margin = Inches(0.75)
        section.header_distance = Inches(0.4)
        section.footer_distance = Inches(0.4)

    add_header_footer(doc)

    # Palette
    c_navy = RGBColor(11, 44, 90)        # #0B2C5A
    c_emerald = RGBColor(16, 124, 65)    # #107C41
    c_charcoal = RGBColor(33, 37, 41)    # #212529
    c_muted = RGBColor(100, 116, 139)    # #64748B
    c_card_bg = "F8FAFC"
    c_header_bg = "0B2C5A"

    in_code_block = False
    code_lines = []
    in_table = False
    table_lines = []

    def format_runs(p, text, default_color=c_charcoal, is_code=False, font_size=10.0):
        # Parses **bold**, *italic*, `code`, and plain text
        if is_code:
            r = p.add_run(text)
            r.font.name = 'Consolas'
            r.font.size = Pt(8.5)
            r.font.color.rgb = RGBColor(40, 50, 70)
            return

        tokens = re.split(r'(\*\*.*?\*\*|\*.*?\*|`.*?`|\$\$.*?\$\$|\$.*?\$)', text)
        for tok in tokens:
            if not tok:
                continue
            if tok.startswith('**') and tok.endswith('**') and len(tok) >= 4:
                r = p.add_run(tok[2:-2])
                r.bold = True
                r.font.color.rgb = default_color
                r.font.size = Pt(font_size)
            elif tok.startswith('*') and tok.endswith('*') and len(tok) >= 2:
                r = p.add_run(tok[1:-1])
                r.italic = True
                r.font.color.rgb = default_color
                r.font.size = Pt(font_size)
            elif tok.startswith('`') and tok.endswith('`') and len(tok) >= 2:
                r = p.add_run(tok[1:-1])
                r.font.name = 'Consolas'
                r.font.size = Pt(font_size * 0.9)
                r.font.color.rgb = RGBColor(180, 40, 60)
            elif (tok.startswith('$$') and tok.endswith('$$')) or (tok.startswith('$') and tok.endswith('$')):
                clean_math = tok.strip('$')
                r = p.add_run(clean_math)
                r.italic = True
                r.bold = True
                r.font.name = 'Cambria Math'
                r.font.size = Pt(font_size)
                r.font.color.rgb = c_navy
            else:
                r = p.add_run(tok)
                r.font.color.rgb = default_color
                r.font.size = Pt(font_size)

    def flush_table(t_lines):
        if not t_lines:
            return
        rows = [list(map(str.strip, l.strip('|').split('|'))) for l in t_lines if not re.match(r'^[\|\s\-\:\+]+$', l)]
        if not rows:
            return
        col_count = max(len(r) for r in rows)
        t = doc.add_table(rows=len(rows), cols=col_count)
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        t.autofit = True

        for r_idx, row_data in enumerate(rows):
            row_elem = t.rows[r_idx]
            is_header = (r_idx == 0)
            # prevent split
            trPr = row_elem._tr.get_or_add_trPr()
            trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))

            for c_idx in range(col_count):
                cell = row_elem.cells[c_idx]
                cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
                val = row_data[c_idx] if c_idx < len(row_data) else ""
                p = cell.paragraphs[0]
                p.paragraph_format.space_before = Pt(2)
                p.paragraph_format.space_after = Pt(2)
                
                if is_header:
                    set_cell_shading(cell, c_header_bg)
                    format_runs(p, val, default_color=RGBColor(255, 255, 255), font_size=9.0)
                    for r in p.runs:
                        r.bold = True
                else:
                    bg = "F8FAFC" if (r_idx % 2 == 1) else "FFFFFF"
                    set_cell_shading(cell, bg)
                    format_runs(p, val, default_color=c_charcoal, font_size=8.5)
                
                set_cell_margins(cell, top=60, bottom=60, left=100, right=100)
                set_cell_border(cell, 
                                top=dict(sz=2, color='CBD5E1'), 
                                bottom=dict(sz=4 if is_header else 2, color='0B2C5A' if is_header else 'CBD5E1'),
                                left=dict(sz=2, color='E2E8F0'), 
                                right=dict(sz=2, color='E2E8F0'))

        p_spacer = doc.add_paragraph()
        p_spacer.paragraph_format.space_before = Pt(0)
        p_spacer.paragraph_format.space_after = Pt(6)

    def flush_code(c_lines):
        if not c_lines:
            return
        text = "".join(c_lines)
        t = doc.add_table(rows=1, cols=1)
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        t.autofit = False
        cell = t.rows[0].cells[0]
        cell.width = Inches(7.0)
        set_cell_shading(cell, "F1F5F9")
        set_cell_margins(cell, top=100, bottom=100, left=140, right=140)
        set_cell_border(cell, 
                        top=dict(sz=4, color='CBD5E1'), 
                        bottom=dict(sz=4, color='CBD5E1'),
                        left=dict(sz=12, color='0B2C5A'), 
                        right=dict(sz=4, color='CBD5E1'))
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = Pt(11)
        r = p.add_run(text.strip('\n'))
        r.font.name = 'Consolas'
        r.font.size = Pt(8.0)
        r.font.color.rgb = RGBColor(30, 41, 59)

        p_spacer = doc.add_paragraph()
        p_spacer.paragraph_format.space_after = Pt(4)

    i = 0
    while i < len(lines):
        line = lines[i]
        raw = line.rstrip('\r\n')
        stripped = raw.strip()

        # Handle Code blocks
        if stripped.startswith('```'):
            if in_code_block:
                in_code_block = False
                flush_code(code_lines)
                code_lines = []
            else:
                in_code_block = True
                code_lines = []
            i += 1
            continue

        if in_code_block:
            code_lines.append(raw + '\n')
            i += 1
            continue

        # Handle Tables
        if stripped.startswith('|') and stripped.endswith('|'):
            table_lines.append(stripped)
            i += 1
            continue
        else:
            if table_lines:
                flush_table(table_lines)
                table_lines = []

        if not stripped:
            i += 1
            continue

        # Horizontal Rule
        if stripped.startswith('---'):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(4)
            p.paragraph_format.space_after = Pt(6)
            r = p.add_run('━' * 65)
            r.font.color.rgb = RGBColor(203, 213, 225)
            r.font.size = Pt(8)
            i += 1
            continue

        # Heading 1 (# ...)
        if stripped.startswith('# '):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(14)
            p.paragraph_format.space_after = Pt(4)
            p.paragraph_format.keep_with_next = True
            format_runs(p, stripped[2:], default_color=c_navy, font_size=18.0)
            for r in p.runs:
                r.bold = True
            i += 1
            continue

        # Heading 2 (## ...)
        if stripped.startswith('## '):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(12)
            p.paragraph_format.space_after = Pt(3)
            p.paragraph_format.keep_with_next = True
            format_runs(p, stripped[3:], default_color=c_navy, font_size=13.5)
            for r in p.runs:
                r.bold = True
            i += 1
            continue

        # Heading 3 (### ...)
        if stripped.startswith('### '):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(9)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.keep_with_next = True
            format_runs(p, stripped[4:], default_color=c_emerald, font_size=11.5)
            for r in p.runs:
                r.bold = True
            i += 1
            continue

        # Heading 4 (#### ...)
        if stripped.startswith('#### '):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(6)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.keep_with_next = True
            format_runs(p, stripped[5:], default_color=c_charcoal, font_size=10.5)
            for r in p.runs:
                r.bold = True
            i += 1
            continue

        # Blockquote (> ...)
        if stripped.startswith('> '):
            quote_lines = []
            while i < len(lines) and lines[i].strip().startswith('>'):
                quote_lines.append(lines[i].strip()[1:].strip())
                i += 1
            q_text = " ".join(quote_lines)
            
            t = doc.add_table(rows=1, cols=1)
            t.alignment = WD_TABLE_ALIGNMENT.CENTER
            t.autofit = False
            cell = t.rows[0].cells[0]
            cell.width = Inches(7.0)
            set_cell_shading(cell, "F0FDF4")
            set_cell_margins(cell, top=70, bottom=70, left=120, right=120)
            set_cell_border(cell, 
                            top=dict(val='none'), bottom=dict(val='none'), right=dict(val='none'),
                            left=dict(sz=14, color='107C41'))
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            format_runs(p, q_text, default_color=RGBColor(20, 83, 45), font_size=9.5)
            
            p_spacer = doc.add_paragraph()
            p_spacer.paragraph_format.space_after = Pt(2)
            continue

        # Bullet list
        if stripped.startswith('* ') or stripped.startswith('- '):
            p = doc.add_paragraph(style='List Bullet')
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.line_spacing = Pt(12)
            format_runs(p, stripped[2:], default_color=c_charcoal, font_size=9.5)
            i += 1
            continue

        # Numbered list
        m_num = re.match(r'^(\d+)\.\s+(.*)$', stripped)
        if m_num:
            num = m_num.group(1)
            item_text = m_num.group(2)
            p = doc.add_paragraph(style='List Number')
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.line_spacing = Pt(12)
            format_runs(p, item_text, default_color=c_charcoal, font_size=9.5)
            i += 1
            continue

        # Standard Paragraph
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = Pt(13)
        format_runs(p, stripped, default_color=c_charcoal, font_size=9.5)
        i += 1

    if table_lines:
        flush_table(table_lines)

    doc.save(docx_path)
    print(f"Generated DOCX: {docx_path}")

if __name__ == '__main__':
    src_md = "/home/paradoxpete/Documents/PROJECT_ORGANIZED/07_SEMESTER_EXECUTION/06_Reports_and_Demonstration/VIBEGUARD_ASD_STE100_TECHNICAL_SPECIFICATION_AND_DEFENSE_GUIDE.md"
    dst_docx = "/home/paradoxpete/Documents/PROJECT_ORGANIZED/07_SEMESTER_EXECUTION/06_Reports_and_Demonstration/VIBEGUARD_ASD_STE100_TECHNICAL_SPECIFICATION_AND_DEFENSE_GUIDE.docx"
    dst_pdf_dir = "/home/paradoxpete/Documents/PROJECT_ORGANIZED/07_SEMESTER_EXECUTION/06_Reports_and_Demonstration"

    parse_markdown_to_docx(src_md, dst_docx)
    cmd = ["libreoffice", "--headless", "--convert-to", "pdf", dst_docx, "--outdir", dst_pdf_dir]
    print("Converting to PDF via LibreOffice...")
    subprocess.run(cmd, check=True)
    print("PDF Generation Completed successfully!")
