import os, base64, subprocess, pymupdf, shutil

def get_b64(fname):
    if os.path.exists(fname):
        with open(fname, 'rb') as f:
            b64 = base64.b64encode(f.read()).decode('utf-8')
            ext = 'png' if fname.endswith('.png') else 'jpeg'
            return f"data:image/{ext};base64,{b64}"
    return ""

print("Encoding images...")
logo_b64 = get_b64("cropped-cropped-italsportlogo.png")
post1_b64 = get_b64("img_post1_jersey.jpg")
post2_b64 = get_b64("img_post2_3d.jpg")
post3_b64 = get_b64("img_post3_fidelity.jpg")
post4_b64 = get_b64("img_post4_stack.jpg")
post5_b64 = get_b64("img_post5_portal.jpg")
post6_b64 = get_b64("img_post6_winter.jpg")
post7_b64 = get_b64("img_post7_celebration.jpg")

cfg_b64 = get_b64("site_configuratore.jpg")
portal_b64 = get_b64("site_membro_myitalsport.jpg")
fullprint_b64 = get_b64("store_full_print.jpg")
reparto_b64 = get_b64("store_reparto_grafico.jpg")
linea_b64 = get_b64("store_la_tua_linea.jpg")
partner_b64 = get_b64("store_partner_affidabile.jpg")
dtf_b64 = get_b64("store_dtf.jpg")
site_home_b64 = get_b64("site_homepage.png")

print("Building shared presentation CSS...")

common_head = """
<meta charset="UTF-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap');

@page {
    size: 297mm 167.0625mm;
    margin: 0;
}

* {
    box-sizing: border-box;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
}

html, body {
    margin: 0;
    padding: 0;
    background: #0f172a;
    font-family: 'Plus Jakarta Sans', 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    color: #0f172a;
    -webkit-font-smoothing: antialiased;
}

.slide {
    width: 297mm;
    height: 167.0625mm;
    max-height: 167.0625mm;
    page-break-after: always;
    page-break-inside: avoid;
    box-sizing: border-box;
    padding: 10mm 15mm 9mm 15mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    background: #ffffff;
    position: relative;
    overflow: hidden;
}

/* Slide Header */
.slide-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    padding-bottom: 7px;
    border-bottom: 1.5px solid #e2e8f0;
    margin-bottom: 8px;
    flex-shrink: 0;
}

.header-left {
    display: flex;
    align-items: center;
    gap: 14px;
}

.header-logo {
    height: 38px;
    width: auto;
    object-fit: contain;
}

.header-title-box {
    display: flex;
    flex-direction: column;
}

.category-tag {
    font-size: 8.5px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    color: #0284c7;
    margin-bottom: 1px;
}

.slide-title {
    font-size: 17px;
    font-weight: 800;
    color: #0f172a;
    margin: 0;
    line-height: 1.2;
    letter-spacing: -0.2px;
}

.slide-subtitle {
    font-size: 10px;
    color: #475569;
    margin: 2px 0 0 0;
    font-weight: 500;
}

.chapter-badge {
    background: #f1f5f9;
    border: 1px solid #cbd5e1;
    color: #334155;
    padding: 4px 10px;
    border-radius: 5px;
    font-size: 8.5px;
    font-weight: 700;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    white-space: nowrap;
}

/* Slide Body */
.slide-body {
    flex-grow: 1;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 9px;
    min-height: 0;
    margin: 2px 0;
}

/* Slide Footer */
.slide-footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-top: 6px;
    border-top: 1px solid #e2e8f0;
    font-size: 8.5px;
    color: #64748b;
    font-weight: 600;
    flex-shrink: 0;
    margin-top: 6px;
}

.footer-left {
    display: flex;
    align-items: center;
    gap: 8px;
}

.footer-pill {
    background: #e0f2fe;
    color: #0369a1;
    padding: 2px 8px;
    border-radius: 4px;
    font-weight: 700;
    font-size: 8px;
}

.slide-num {
    background: #f1f5f9;
    border: 1px solid #cbd5e1;
    padding: 2px 8px;
    border-radius: 4px;
    color: #0f172a;
    font-weight: 700;
}

/* Utility Cards & Grids */
.card {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 12px 14px;
}

.card-white {
    background: #ffffff;
    border: 1px solid #cbd5e1;
    border-radius: 8px;
    padding: 12px 14px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.03);
}

.card-blue {
    background: #f0f7ff;
    border: 1px solid #bfdbfe;
    border-radius: 8px;
    padding: 12px 14px;
}

.card-green {
    background: #f0fdf4;
    border: 1px solid #bbf7d0;
    border-radius: 8px;
    padding: 12px 14px;
}

.card-gold {
    background: #fffbeb;
    border: 1px solid #fde68a;
    border-radius: 8px;
    padding: 12px 14px;
}

.grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 11px; }
.grid-3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 11px; }
.grid-4 { display: grid; grid-template-columns: 1fr 1fr 1fr 1fr; gap: 9px; }
.grid-5 { display: grid; grid-template-columns: repeat(5, 1fr); gap: 8px; }
.grid-2-3 { display: grid; grid-template-columns: 2fr 3fr; gap: 12px; }
.grid-3-2 { display: grid; grid-template-columns: 3fr 2fr; gap: 12px; }
.grid-1-2 { display: grid; grid-template-columns: 1fr 2fr; gap: 12px; }

.pill {
    display: inline-block;
    padding: 2px 7px;
    border-radius: 4px;
    font-size: 8px;
    font-weight: 700;
    text-transform: uppercase;
}
.pill-blue { background: #e0f2fe; color: #0284c7; }
.pill-green { background: #dcfce7; color: #16a34a; }
.pill-gold { background: #fef3c7; color: #d97706; }
.pill-purple { background: #f3e8ff; color: #9333ea; }
.pill-slate { background: #f1f5f9; color: #475569; }

.stat-box {
    background: #ffffff;
    border: 1px solid #cbd5e1;
    border-radius: 7px;
    padding: 8px 10px;
    text-align: center;
    box-shadow: 0 1px 2px rgba(0,0,0,0.02);
}
.stat-val {
    font-size: 17px;
    font-weight: 800;
    color: #0284c7;
    line-height: 1.1;
}
.stat-lbl {
    font-size: 8px;
    color: #64748b;
    font-weight: 600;
    text-transform: uppercase;
    margin-top: 2px;
}

/* Tables */
table.deck-table {
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    font-size: 9.5px;
    border: 1px solid #cbd5e1;
    border-radius: 7px;
    overflow: hidden;
}
table.deck-table th {
    background: #f1f5f9;
    color: #0f172a;
    font-weight: 700;
    padding: 6.5px 8px;
    text-align: left;
    border-bottom: 1px solid #cbd5e1;
    font-size: 9px;
    text-transform: uppercase;
    letter-spacing: 0.4px;
}
table.deck-table td {
    padding: 6px 8px;
    border-bottom: 1px solid #e2e8f0;
    color: #334155;
    vertical-align: middle;
}
table.deck-table tr:last-child td {
    border-bottom: none;
}
table.deck-table tr:nth-child(even) td {
    background: #f8fafc;
}

/* Post Cards */
.post-deck-card {
    background: #ffffff;
    border: 1px solid #cbd5e1;
    border-radius: 8px;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    box-shadow: 0 1px 3px rgba(0,0,0,0.03);
}
.post-deck-img {
    width: 100%;
    aspect-ratio: 1;
    object-fit: cover;
    display: block;
    border-bottom: 1px solid #e2e8f0;
}
.post-deck-body {
    padding: 7px 9px;
    display: flex;
    flex-direction: column;
    gap: 3px;
    flex-grow: 1;
}
.post-deck-title {
    font-size: 10.5px;
    font-weight: 800;
    color: #0f172a;
    line-height: 1.2;
}
.post-deck-copy {
    font-size: 8.5px;
    color: #475569;
    line-height: 1.35;
    margin: 0;
}
.post-deck-tag {
    font-size: 7.5px;
    color: #0284c7;
    font-weight: 600;
}
</style>
"""

print("Common CSS ready.")
