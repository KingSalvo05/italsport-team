import os, base64, json
from ig_parts import IG_CSS, IG_TAB, IG_MODAL, IG_JS

def get_base64_image(filename):
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            b64 = base64.b64encode(f.read()).decode('utf-8')
            if filename.endswith('.png'):
                ext = 'png'
            elif filename.endswith('.gif'):
                ext = 'gif'
            else:
                ext = 'jpeg'
            return f"data:image/{ext};base64,{b64}"
    return ""

print("Encoding real Italsport Ciserano (BG) assets for web app mockup...")
logo_b64 = get_base64_image("cropped-cropped-italsportlogo.png")
post1_b64 = get_base64_image("img_post1_jersey.jpg")
post2_b64 = get_base64_image("img_post2_3d.jpg")
post3_b64 = get_base64_image("img_post3_fidelity.jpg")
post4_b64 = get_base64_image("img_post4_stack.jpg")
post5_b64 = get_base64_image("img_post5_portal.jpg")
post6_b64 = get_base64_image("img_post6_winter.jpg")
post7_b64 = get_base64_image("img_post7_celebration.jpg")

post1_s2_b64 = get_base64_image("img_post1_s2.jpg")
post2_s2_b64 = get_base64_image("img_post2_s2.jpg")
post3_s2_b64 = get_base64_image("img_post3_s2.jpg")
post4_s2_b64 = get_base64_image("img_post4_s2.jpg")
post5_s2_b64 = get_base64_image("img_post5_s2.jpg")
post6_s2_b64 = get_base64_image("img_post6_s2.jpg")
post7_s2_b64 = get_base64_image("img_post7_s2.jpg")

gif3d_b64 = get_base64_image("configuratore3d_web.gif")
card_real_b64 = get_base64_image("card_proclub_real.jpg")
shw_b64 = get_base64_image("real_showroom_ciserano.jpg")
man_b64 = get_base64_image("real_manichini_ciserano.jpg")

prod_kit_blue_b64 = get_base64_image("prod_kit_blue.jpg")
prod_kit_red_b64 = get_base64_image("prod_kit_red.jpg")
prod_kit_gold_b64 = get_base64_image("prod_kit_gold.jpg")
prod_tuta_b64 = get_base64_image("prod_tuta.jpg")
prod_scotland_b64 = get_base64_image("prod_scotland.jpg")
prod_nepal_b64 = get_base64_image("prod_nepal.jpg")
prod_kway_b64 = get_base64_image("prod_kway.jpg")
prod_borsa_b64 = get_base64_image("prod_borsa.jpg")

_extra = {
    'p1': post1_b64, 'p2': post2_b64, 'p3': post3_b64, 'p4': post4_b64,
    'p5': post5_b64, 'p6': post6_b64, 'p7': post7_b64,
    'p1_s2': post1_s2_b64, 'p2_s2': post2_s2_b64, 'p3_s2': post3_s2_b64,
    'p4_s2': post4_s2_b64, 'p5_s2': post5_s2_b64, 'p6_s2': post6_s2_b64,
    'p7_s2': post7_s2_b64,
    'gif3d': gif3d_b64, 'card': card_real_b64, 'shw': shw_b64, 'man': man_b64
}
IG_TAB = IG_TAB.replace('__LOGO__', logo_b64)
IG_MODAL = IG_MODAL.replace('__LOGO__', logo_b64)
IG_JS = IG_JS.replace('__LOGO__', logo_b64).replace('__IMGS__', json.dumps(_extra))

html_mockup = f"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Italsport Group Ciserano (BG) - Piattaforma Strategica & Mockup Instagram 2026</title>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>
:root {{
    --bg-primary: #f8fafc;
    --bg-card: #ffffff;
    --border-color: #e2e8f0;
    --text-primary: #0f172a;
    --text-secondary: #475569;
    --text-muted: #94a3b8;
    --brand-blue: #0284c7;
    --brand-navy: #1e3a8a;
    --brand-gold: #d97706;
    --brand-green: #059669;
    --shadow-sm: 0 1px 3px rgba(0,0,0,0.05);
    --shadow-md: 0 4px 6px -1px rgba(0,0,0,0.07), 0 2px 4px -2px rgba(0,0,0,0.05);
    --shadow-lg: 0 10px 15px -3px rgba(0,0,0,0.08), 0 4px 6px -4px rgba(0,0,0,0.04);
}}

* {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}}

body {{
    font-family: 'Plus Jakarta Sans', 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    background-color: var(--bg-primary);
    color: var(--text-primary);
    line-height: 1.5;
    -webkit-font-smoothing: antialiased;
}}

/* Top Navigation Bar */
.top-nav {{
    background: #ffffff;
    border-bottom: 1px solid var(--border-color);
    position: sticky;
    top: 0;
    z-index: 100;
    box-shadow: var(--shadow-sm);
}}

.nav-container {{
    max-width: 1200px;
    margin: 0 auto;
    padding: 12px 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 15px;
}}

.brand-area {{
    display: flex;
    align-items: center;
    gap: 12px;
}}

.brand-area img {{
    height: 38px;
    object-fit: contain;
}}

.brand-tag {{
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    color: var(--brand-blue);
    background: #e0f2fe;
    padding: 4px 8px;
    border-radius: 6px;
}}

.nav-tabs {{
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
}}

.nav-btn {{
    background: #f1f5f9;
    border: 1px solid var(--border-color);
    color: var(--text-secondary);
    padding: 8px 14px;
    border-radius: 8px;
    font-size: 12.5px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s ease;
    display: flex;
    align-items: center;
    gap: 7px;
    text-decoration: none;
}}

.nav-btn:hover {{
    background: #e2e8f0;
    color: var(--text-primary);
}}

.nav-btn.active {{
    background: var(--brand-navy);
    color: #ffffff;
    border-color: var(--brand-navy);
}}

.nav-btn.btn-gold {{
    background: #fef3c7;
    color: #b45309;
    border-color: #fde68a;
}}

.nav-btn.btn-gold:hover {{
    background: #fde68a;
}}

.btn-pdf {{
    background: #0284c7;
    color: #ffffff;
    border-color: #0284c7;
}}

.btn-pdf:hover {{
    background: #0369a1;
}}

/* Main Container */
.main-wrapper {{
    max-width: 1200px;
    margin: 25px auto;
    padding: 0 20px 60px 20px;
}}

/* Executive Banner */
.executive-banner {{
    background: linear-gradient(135deg, #ffffff 0%, #f0fdf4 50%, #f0f9ff 100%);
    border: 1.5px solid var(--border-color);
    border-radius: 16px;
    padding: 24px 28px;
    margin-bottom: 30px;
    box-shadow: var(--shadow-sm);
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 20px;
}}

.exec-text h1 {{
    font-size: 22px;
    font-weight: 800;
    color: var(--text-primary);
    margin-bottom: 6px;
}}

.exec-text p {{
    font-size: 13.5px;
    color: var(--text-secondary);
    max-width: 720px;
}}

.exec-badges {{
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
}}

.pill-badge {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 6px 12px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 700;
}}

/* Sections */
.tab-content {{
    display: none;
}}

.tab-content.active {{
    display: block;
}}

/* 3D Configurator Interactive Tool */
.configurator-panel {{
    background: #ffffff;
    border: 1px solid var(--border-color);
    border-radius: 16px;
    padding: 28px;
    box-shadow: var(--shadow-md);
}}

.cfg-header {{
    margin-bottom: 24px;
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    flex-wrap: wrap;
    gap: 15px;
}}

.cfg-header h2 {{
    font-size: 22px;
    font-weight: 800;
    color: var(--text-primary);
}}

.cfg-header p {{
    font-size: 13.5px;
    color: var(--text-secondary);
}}

.cfg-workspace {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 30px;
    align-items: start;
}}

.jersey-stage {{
    background: radial-gradient(circle at center, #ffffff 0%, #f1f5f9 100%);
    border: 1px solid var(--border-color);
    border-radius: 16px;
    padding: 24px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 460px;
    position: relative;
    box-shadow: inset 0 2px 4px rgba(0,0,0,0.02);
}}

.jersey-canvas-box {{
    width: 270px;
    height: 325px;
    position: relative;
    transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}}

.jersey-svg {{
    width: 100%;
    height: 100%;
    filter: drop-shadow(0 15px 20px rgba(0,0,0,0.15));
}}

.controls-panel {{
    background: #f8fafc;
    border: 1px solid var(--border-color);
    border-radius: 12px;
    padding: 22px;
    display: flex;
    flex-direction: column;
    gap: 16px;
}}

.control-group h4 {{
    font-size: 12.5px;
    font-weight: 700;
    color: var(--text-primary);
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 8px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}}

.color-swatches {{
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
}}

.swatch {{
    width: 32px;
    height: 32px;
    border-radius: 50%;
    cursor: pointer;
    border: 2px solid #ffffff;
    box-shadow: 0 0 0 1px #cbd5e1;
    transition: transform 0.15s, box-shadow 0.15s;
}}

.swatch:hover {{
    transform: scale(1.15);
}}

.swatch.active {{
    transform: scale(1.18);
    box-shadow: 0 0 0 2.5px #0284c7;
}}

.pattern-options, .collar-options {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 8px;
}}

.opt-btn {{
    background: #ffffff;
    border: 1px solid var(--border-color);
    padding: 8px;
    border-radius: 6px;
    font-size: 11px;
    font-weight: 600;
    color: var(--text-secondary);
    cursor: pointer;
    text-align: center;
    transition: all 0.2s;
}}

.opt-btn.active {{
    background: #e0f2fe;
    color: #0369a1;
    border-color: #bae6fd;
    font-weight: 700;
}}

.rotation-toolbar {{
    display: flex;
    gap: 10px;
    margin-top: 15px;
    width: 100%;
    justify-content: center;
    flex-wrap: wrap;
}}

.tool-btn {{
    background: #ffffff;
    border: 1px solid var(--border-color);
    padding: 6px 14px;
    border-radius: 6px;
    font-size: 12px;
    font-weight: 600;
    color: var(--text-secondary);
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 6px;
    box-shadow: var(--shadow-sm);
}}

.tool-btn:hover {{
    background: #f1f5f9;
    color: var(--text-primary);
}}

/* Dedicated Club Storefront (My Italsport) with Password Gate */
.club-storefront {{
    background: #ffffff;
    border: 1px solid var(--border-color);
    border-radius: 16px;
    overflow: hidden;
    box-shadow: var(--shadow-md);
}}

.pwd-selector-bar {{
    background: #0f172a;
    color: #ffffff;
    padding: 18px 28px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 15px;
    border-bottom: 2px solid #0284c7;
}}

.pwd-club-pills {{
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
}}

.pwd-pill {{
    background: #1e293b;
    border: 1px solid #475569;
    color: #e2e8f0;
    padding: 8px 14px;
    border-radius: 8px;
    font-size: 12.5px;
    font-weight: 700;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 8px;
    transition: all 0.2s;
}}

.pwd-pill:hover {{
    background: #334155;
}}

.pwd-pill.active {{
    background: #0284c7;
    border-color: #38bdf8;
    color: #ffffff;
}}

.pwd-login-overlay {{
    padding: 45px 25px;
    background: linear-gradient(135deg, #f8fafc 0%, #e0f2fe 100%);
    display: none;
    justify-content: center;
    align-items: center;
}}

.pwd-login-card {{
    background: #ffffff;
    border: 1.5px solid #cbd5e1;
    border-radius: 16px;
    padding: 32px;
    max-width: 480px;
    width: 100%;
    box-shadow: var(--shadow-lg);
    text-align: center;
}}

.store-header {{
    background: #1e3a8a;
    color: #ffffff;
    padding: 24px 30px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 15px;
}}

.store-club-info {{
    display: flex;
    align-items: center;
    gap: 18px;
}}

.club-crest-box {{
    width: 60px;
    height: 60px;
    background: #ffffff;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #1e3a8a;
    font-size: 26px;
    font-weight: 800;
}}

.vetrina-pillars {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
    padding: 22px 28px 0 28px;
}}

.v-pillar {{
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-left: 4px solid #0284c7;
    border-radius: 10px;
    padding: 14px 16px;
}}

.v-pillar h4 {{
    font-size: 13.5px;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 4px;
    display: flex;
    align-items: center;
    gap: 7px;
}}

.v-pillar p {{
    font-size: 12px;
    color: #475569;
    line-height: 1.45;
}}

.store-products-grid {{
    padding: 24px 28px 30px 28px;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
}}

.product-item {{
    background: #ffffff;
    border: 1px solid var(--border-color);
    border-radius: 12px;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    transition: transform 0.2s, box-shadow 0.2s;
}}

.product-item:hover {{
    transform: translateY(-4px);
    box-shadow: var(--shadow-md);
}}

.product-img-box {{
    height: 210px;
    background: #1e293b;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 12px;
    border-bottom: 1px solid var(--border-color);
    position: relative;
}}

.product-img-box img {{
    max-height: 100%;
    max-width: 100%;
    object-fit: contain;
    border-radius: 6px;
}}

.locked-line-badge {{
    position: absolute;
    top: 10px;
    left: 10px;
    background: rgba(5, 150, 105, 0.95);
    color: #ffffff;
    font-size: 10px;
    font-weight: 800;
    padding: 4px 9px;
    border-radius: 6px;
}}

.product-info {{
    padding: 15px;
    display: flex;
    flex-direction: column;
    flex: 1;
    justify-content: space-between;
}}

.product-info h5 {{
    font-size: 14px;
    font-weight: 800;
    color: var(--text-primary);
    margin-bottom: 4px;
}}

.product-info .code-tag {{
    font-size: 11px;
    font-weight: 700;
    color: #0284c7;
    margin-bottom: 6px;
}}

.btn-buy {{
    background: var(--brand-navy);
    color: #ffffff;
    border: none;
    padding: 8px 12px;
    border-radius: 6px;
    font-size: 12px;
    font-weight: 600;
    cursor: pointer;
    text-align: center;
    transition: background 0.2s;
}}

.btn-buy:hover {{
    background: #0284c7;
}}

/* Pro-Club Fidelity Section */
.fidelity-card-section {{
    background: #ffffff;
    border: 1px solid var(--border-color);
    border-radius: 16px;
    padding: 30px;
    box-shadow: var(--shadow-md);
}}

@media (max-width: 820px) {{
    .cfg-workspace, .vetrina-pillars {{
        grid-template-columns: 1fr;
    }}
    .store-products-grid {{
        grid-template-columns: 1fr 1fr;
    }}
}}
{IG_CSS}
</style>
</head>
<body>

<!-- TOP NAVIGATION -->
<nav class="top-nav">
    <div class="nav-container">
        <div class="brand-area">
            <img src="{logo_b64}" alt="Italsport Group Logo">
            <span class="brand-tag">CISERANO (BG) • PIANO SOCIAL & B2B 2026</span>
        </div>
        <div class="nav-tabs">
            <button class="nav-btn active" onclick="switchTab('feed')"><i class="fa-brands fa-instagram"></i> Mockup Feed Instagram</button>
            <button class="nav-btn" onclick="switchTab('configurator')"><i class="fa-solid fa-shirt"></i> Configuratore 3D + Video 360°</button>
            <button class="nav-btn" onclick="switchTab('storefront')"><i class="fa-solid fa-lock"></i> Vetrina Squadra con Password</button>
            <button class="nav-btn btn-gold" onclick="switchTab('fidelity')"><i class="fa-solid fa-id-card"></i> Tessera Pro-Club</button>
            <a href="Piano_Social_Italsport_2026.pdf" target="_blank" class="nav-btn btn-pdf"><i class="fa-solid fa-file-pdf"></i> Scarica PDF Presentazione</a>
        </div>
    </div>
</nav>

<div class="main-wrapper">

    <!-- EXECUTIVE BANNER -->
    <div class="executive-banner">
        <div class="exec-text">
            <div style="font-size: 11px; font-weight: 700; color: #0284c7; text-transform: uppercase; margin-bottom: 4px;">
                ITALSPORT GROUP • VIA PROVINCIALE FRANCESCA 2H/I, CISERANO — ZINGONIA (BG)
            </div>
            <h1>Strategia Social Instagram & Vetrina Squadre "My Italsport"</h1>
            <p>
                Presentazione interattiva basata sulle vere foto di <b>@italsportgroup</b> e <b>italsport-group.it</b>: Feed Instagram cliccabile, Configuratore 3D con rotazione reale a 360°, <b>Vetrina Dedicata con Password per ogni squadra</b> e Tessera Pro-Club.
            </p>
        </div>
        <div class="exec-badges">
            <span class="pill-badge" style="background: #e0f2fe; color: #0369a1;"><i class="fa-solid fa-camera"></i> Vere Foto @italsportgroup</span>
            <span class="pill-badge" style="background: #dcfce7; color: #15803d;"><i class="fa-solid fa-key"></i> Vetrina Protetta da Password</span>
            <span class="pill-badge" style="background: #fef3c7; color: #b45309;"><i class="fa-solid fa-award"></i> Tessera Pro-Club Ufficiale</span>
        </div>
    </div>

{IG_TAB}

    <!-- TAB 2: INTERACTIVE 3D CONFIGURATOR + REAL 360° ROTATION -->
    <div id="tab-configurator" class="tab-content">
        <div class="configurator-panel">
            <div class="cfg-header">
                <div>
                    <span class="pill-badge" style="background: #e0f2fe; color: #0369a1; margin-bottom: 6px;">CONFIGURATORE 3D ITALSPORT • CISERANO (BG)</span>
                    <h2>Maglia 3D con Rotazione a 360° Reale & Personalizzazione Live</h2>
                    <p>A sinistra l'animazione 3D a 360° reale del configuratore Italsport e il simulatore interattivo; a destra i controlli per cambiare colori, pattern, colletto e sponsor.</p>
                </div>
                <div style="display: flex; gap: 8px; flex-wrap: wrap;">
                    <button class="tool-btn" style="background: #0f172a; color: #fff; border-color: #0f172a;" onclick="toggleReal3dVideo()"><i class="fa-solid fa-video"></i> <span id="real3dBtnTxt">Mostra Simulatore Interattivo SVG</span></button>
                    <button class="tool-btn" style="background: #0284c7; color: #fff; border-color: #0284c7;" onclick="alert('Bozza grafica salvata! Puoi inviarla al reparto grafico Italsport di Ciserano (info@italsport-group.it).')"><i class="fa-solid fa-floppy-disk"></i> Salva & Invia a Italsport</button>
                </div>
            </div>

            <div class="cfg-workspace">
                
                <!-- Left Column: Both Real 360° Animation & Interactive SVG Stage -->
                <div style="display: flex; flex-direction: column; gap: 18px;">
                    
                    <!-- Box 1: Real 360° 3D Jersey Animation from italsport-group.it -->
                    <div id="real3dVideoBox" style="background: #ffffff; border: 2px solid #0284c7; border-radius: 16px; padding: 18px; text-align: center; box-shadow: var(--shadow-sm);">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                            <span class="pill-badge" style="background: #e0f2fe; color: #0369a1;"><i class="fa-solid fa-rotate"></i> ANIMAZIONE 3D A 360° REALE DAL SITO ITALSPORT</span>
                            <span style="font-size: 11.5px; font-weight: 700; color: #475569;">Vista Fronte / Retro 360°</span>
                        </div>
                        <img src="{gif3d_b64}" alt="Rotazione 3D 360 Maglia Italsport" style="max-width: 100%; height: 290px; object-fit: contain; border-radius: 10px;">
                        <p style="font-size: 12px; color: #475569; margin-top: 8px;">
                            <i class="fa-solid fa-circle-info" style="color: #0284c7;"></i> Vera cattura della maglia 3D dal configuratore ufficiale <b>italsport-group.it</b> mentre ruota a 360° con loghi, numeri e colletto.
                        </p>
                    </div>

                    <!-- Box 2: Interactive Live Customizer -->
                    <div class="jersey-stage" style="min-height: 390px;">
                        <div style="font-size: 11px; font-weight: 800; color: #0f172a; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 8px;">
                            PROVA A MODIFICARE COLORI, PATTERN, COLLETTO E SPONSOR IN TEMPO REALE:
                        </div>
                        <div class="jersey-canvas-box" id="jerseyBox">
                            <svg class="jersey-svg" id="jerseySvg" viewBox="0 0 400 450" xmlns="http://www.w3.org/2000/svg">
                                <defs>
                                    <pattern id="patStripes" width="50" height="400" patternUnits="userSpaceOnUse">
                                        <rect width="25" height="400" fill="var(--color-primary, #1e3a8a)"/>
                                        <rect x="25" width="25" height="400" fill="var(--color-secondary, #ffffff)"/>
                                    </pattern>
                                    <pattern id="patChevron" width="40" height="40" patternUnits="userSpaceOnUse">
                                        <path d="M0 20 L20 40 L40 20 L20 0 Z" fill="var(--color-secondary, #ffffff)" opacity="0.25"/>
                                    </pattern>
                                    <linearGradient id="bodyShade" x1="0%" y1="0%" x2="100%" y2="0%">
                                        <stop offset="0%" stop-color="#000000" stop-opacity="0.2"/>
                                        <stop offset="25%" stop-color="#ffffff" stop-opacity="0.1"/>
                                        <stop offset="75%" stop-color="#ffffff" stop-opacity="0.1"/>
                                        <stop offset="100%" stop-color="#000000" stop-opacity="0.2"/>
                                    </linearGradient>
                                </defs>
                                <path id="leftSleeve" d="M 120 70 L 40 130 L 70 170 L 130 120 Z" fill="var(--color-primary, #1e3a8a)" stroke="#0f172a" stroke-width="2"/>
                                <path id="rightSleeve" d="M 280 70 L 360 130 L 330 170 L 270 120 Z" fill="var(--color-primary, #1e3a8a)" stroke="#0f172a" stroke-width="2"/>
                                <path id="leftCuff" d="M 40 130 L 48 140 L 78 178 L 70 170 Z" fill="var(--color-accent, #eab308)"/>
                                <path id="rightCuff" d="M 360 130 L 352 140 L 322 178 L 330 170 Z" fill="var(--color-accent, #eab308)"/>
                                <path id="jerseyBody" d="M 120 70 Q 200 85 280 70 L 275 390 L 125 390 Z" fill="var(--color-primary, #1e3a8a)" stroke="#0f172a" stroke-width="2.5"/>
                                <path id="jerseyPattern" d="M 120 70 Q 200 85 280 70 L 275 390 L 125 390 Z" fill="none" opacity="0.9"/>
                                <path d="M 120 70 Q 200 85 280 70 L 275 390 L 125 390 Z" fill="url(#bodyShade)" pointer-events="none"/>
                                <path id="jerseyCollar" d="M 160 72 Q 200 115 240 72 Q 200 90 160 72 Z" fill="var(--color-accent, #eab308)" stroke="#0f172a" stroke-width="1.5"/>
                                <circle cx="170" cy="140" r="18" fill="#ffffff" stroke="var(--color-accent, #eab308)" stroke-width="2"/>
                                <text x="170" y="145" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="800" text-anchor="middle" fill="#1e3a8a">CLUB</text>
                                <text x="235" y="144" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="900" text-anchor="middle" fill="var(--color-accent, #eab308)" letter-spacing="1">ITALSPORT</text>
                                <rect id="sponsorBg" x="145" y="210" width="110" height="36" rx="6" fill="rgba(15, 23, 42, 0.78)"/>
                                <text id="sponsorText" x="200" y="233" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="800" text-anchor="middle" fill="#ffffff" letter-spacing="1">U.S.D. BREVIANESE</text>
                                <rect x="235" y="365" width="28" height="14" rx="2" fill="var(--color-accent, #eab308)"/>
                                <text x="249" y="375" font-family="sans-serif" font-size="7" font-weight="700" text-anchor="middle" fill="#0f172a">OFFICIAL</text>
                            </svg>
                        </div>

                        <div class="rotation-toolbar">
                            <button class="tool-btn" onclick="rotateJersey(-25)"><i class="fa-solid fa-arrow-rotate-left"></i> Ruota Sinistra</button>
                            <button class="tool-btn" onclick="resetRotation()"><i class="fa-solid fa-crosshairs"></i> Frontale</button>
                            <button class="tool-btn" onclick="rotateJersey(25)"><i class="fa-solid fa-arrow-rotate-right"></i> Ruota Destra</button>
                            <button class="tool-btn" onclick="toggleAutoSpin()"><i class="fa-solid fa-Sync"></i> <span id="spin-text">Rotazione Auto: OFF</span></button>
                        </div>
                    </div>
                </div>

                <!-- Customization Controls -->
                <div class="controls-panel">
                    <div class="control-group">
                        <h4>1. Colore Primario Maglia</h4>
                        <div class="color-swatches" id="primarySwatches">
                            <div class="swatch active" style="background: #1e3a8a;" onclick="setPrimaryColor('#1e3a8a', this)" title="Blu Navy"></div>
                            <div class="swatch" style="background: #0284c7;" onclick="setPrimaryColor('#0284c7', this)" title="Azzurro Italsport"></div>
                            <div class="swatch" style="background: #991b1b;" onclick="setPrimaryColor('#991b1b', this)" title="Rosso"></div>
                            <div class="swatch" style="background: #059669;" onclick="setPrimaryColor('#059669', this)" title="Verde"></div>
                            <div class="swatch" style="background: #eab308;" onclick="setPrimaryColor('#eab308', this)" title="Giallo"></div>
                            <div class="swatch" style="background: #ffffff;" onclick="setPrimaryColor('#ffffff', this)" title="Bianco"></div>
                            <div class="swatch" style="background: #0f172a;" onclick="setPrimaryColor('#0f172a', this)" title="Nero"></div>
                        </div>
                    </div>

                    <div class="control-group">
                        <h4>2. Colore Dettagli & Colletto</h4>
                        <div class="color-swatches" id="accentSwatches">
                            <div class="swatch active" style="background: #eab308;" onclick="setAccentColor('#eab308', this)" title="Giallo Oro"></div>
                            <div class="swatch" style="background: #ffffff;" onclick="setAccentColor('#ffffff', this)" title="Bianco"></div>
                            <div class="swatch" style="background: #ef4444;" onclick="setAccentColor('#ef4444', this)" title="Rosso"></div>
                            <div class="swatch" style="background: #0284c7;" onclick="setAccentColor('#0284c7', this)" title="Azzurro"></div>
                            <div class="swatch" style="background: #0f172a;" onclick="setAccentColor('#0f172a', this)" title="Nero"></div>
                        </div>
                    </div>

                    <div class="control-group">
                        <h4>3. Grafica / Pattern</h4>
                        <div class="pattern-options">
                            <button class="opt-btn active" onclick="setPattern('solid', this)">Tinta Unita</button>
                            <button class="opt-btn" onclick="setPattern('stripes', this)">Strisce Verticali</button>
                            <button class="opt-btn" onclick="setPattern('chevron', this)">Trama Tecnica</button>
                        </div>
                    </div>

                    <div class="control-group">
                        <h4>4. Tipologia Colletto</h4>
                        <div class="collar-options">
                            <button class="opt-btn active" onclick="setCollar('vneck', this)">Collo a V</button>
                            <button class="opt-btn" onclick="setCollar('crew', this)">Girocollo</button>
                            <button class="opt-btn" onclick="setCollar('polo', this)">Collo Polo</button>
                        </div>
                    </div>

                    <div class="control-group">
                        <h4>5. Nome Società / Sponsor</h4>
                        <input type="text" id="customSponsorInput" value="U.S.D. BREVIANESE" oninput="updateSponsorText(this.value)" style="width: 100%; padding: 8px 12px; border: 1px solid var(--border-color); border-radius: 6px; font-weight: 600; font-size: 13px;">
                    </div>

                    <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 8px; padding: 12px 14px; font-size: 12px; color: #166534; line-height: 1.45;">
                        <i class="fa-solid fa-check-circle"></i> <b>Dal Configuratore 3D alla Vetrina della Squadra:</b> una volta approvata la divisa col direttivo, Italsport la salva e la inserisce nella <b>Vetrina Protetta con Password</b> della società, così rimarrà sempre identica per tutti i riordini futuri.
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- TAB 3: DEDICATED CLUB STOREFRONT WITH PASSWORD (MY ITALSPORT) -->
    <div id="tab-storefront" class="tab-content">
        <div class="club-storefront">
            
            <!-- Interactive Password & Team Selector Bar -->
            <div class="pwd-selector-bar">
                <div>
                    <div style="font-size: 11px; font-weight: 800; color: #38bdf8; text-transform: uppercase; letter-spacing: 0.8px;">
                        <i class="fa-solid fa-key"></i> DEMO INTERATTIVA: OGNI SQUADRA HA LA SUA VETRINA CON PASSWORD DEDICATA
                    </div>
                    <div style="font-size: 13px; color: #cbd5e1; margin-top: 2px;">
                        Clicca su una società per entrare con la sua password e vedere <b>solo ed esclusivamente i capi di quella squadra</b>:
                    </div>
                </div>
                <div class="pwd-club-pills">
                    <button class="pwd-pill active" id="pill-brevianese" onclick="selectClubVetrina('brevianese')">
                        <i class="fa-solid fa-unlock-keyhole"></i> U.S.D. Brevianese <span style="font-size:10px; background:rgba(255,255,255,0.2); padding:2px 6px; border-radius:4px;">Pwd: BREVIANESE2026</span>
                    </button>
                    <button class="pwd-pill" id="pill-gessate" onclick="selectClubVetrina('gessate')">
                        <i class="fa-solid fa-unlock-keyhole"></i> A.S.D. Gessate <span style="font-size:10px; background:rgba(255,255,255,0.2); padding:2px 6px; border-radius:4px;">Pwd: GESSATE2026</span>
                    </button>
                    <button class="pwd-pill" id="pill-ciserano" onclick="selectClubVetrina('ciserano')">
                        <i class="fa-solid fa-unlock-keyhole"></i> Volley Ciserano <span style="font-size:10px; background:rgba(255,255,255,0.2); padding:2px 6px; border-radius:4px;">Pwd: CISERANO2026</span>
                    </button>
                    <button class="pwd-pill" style="background:#b45309; border-color:#f59e0b; color:#fff;" onclick="showPasswordLoginGate()">
                        <i class="fa-solid fa-lock"></i> Simula Schermata Password
                    </button>
                </div>
            </div>

            <!-- Step 1: Simulated Password Login Gate (Shown when clicking "Simula Schermata Password") -->
            <div class="pwd-login-overlay" id="pwdLoginOverlay">
                <div class="pwd-login-card">
                    <div style="width: 56px; height: 56px; border-radius: 50%; background: #e0f2fe; color: #0284c7; display: flex; align-items: center; justify-content: center; font-size: 24px; margin: 0 auto 14px auto;">
                        <i class="fa-solid fa-user-lock"></i>
                    </div>
                    <div style="font-size: 11px; font-weight: 800; color: #0284c7; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 4px;">
                        STORE.ITALSPORT-GROUP.IT • AREA CLIENTI MY ITALSPORT
                    </div>
                    <h3 style="font-size: 20px; font-weight: 800; color: #0f172a; margin-bottom: 8px;">Accesso Vetrina Riservata Squadra</h3>
                    <p style="font-size: 13px; color: #475569; margin-bottom: 20px;">
                        Inserisci la <b>password dedicata della tua società sportiva</b> per visualizzare esclusivamente i capi ufficiali approvati per la tua squadra.
                    </p>
                    <div style="text-align: left; margin-bottom: 14px;">
                        <label style="font-size: 11px; font-weight: 700; color: #475569; text-transform: uppercase;">Seleziona la tua Società Sportiva</label>
                        <select id="gateClubSelect" onchange="syncGatePassword()" style="width: 100%; padding: 10px 12px; border: 1.5px solid #cbd5e1; border-radius: 8px; font-size: 14px; font-weight: 700; margin-top: 4px;">
                            <option value="brevianese">U.S.D. Brevianese (Ciserano / Bergamo)</option>
                            <option value="gessate">A.S.D. Gessate (Linea Polisportiva)</option>
                            <option value="ciserano">Polisportiva Volley Ciserano BG</option>
                        </select>
                    </div>
                    <div style="text-align: left; margin-bottom: 20px;">
                        <label style="font-size: 11px; font-weight: 700; color: #475569; text-transform: uppercase;">Password Dedicata Squadra</label>
                        <input type="text" id="gatePwdInput" value="BREVIANESE2026" style="width: 100%; padding: 10px 12px; border: 1.5px solid #0284c7; border-radius: 8px; font-size: 15px; font-weight: 800; color: #0f172a; letter-spacing: 1px; margin-top: 4px; background: #f0f9ff;">
                    </div>
                    <button class="btn-buy" style="width: 100%; padding: 12px; font-size: 14px; font-weight: 800;" onclick="unlockClubVetrina()">
                        <i class="fa-solid fa-unlock"></i> Accedi alla Vetrina della Squadra
                    </button>
                </div>
            </div>

            <!-- Step 2: Unlocked Dedicated Team Showcase -->
            <div id="unlockedVetrinaBody">
                <div class="store-header" id="clubBannerBg">
                    <div class="store-club-info">
                        <div class="club-crest-box" id="clubCrestIcon">
                            <i class="fa-solid fa-shield-halved"></i>
                        </div>
                        <div>
                            <div style="font-size: 11px; text-transform: uppercase; color: #93c5fd; font-weight: 700; letter-spacing: 1px;" id="clubSubHeader">
                                VETRINA PROTETTA CON PASSWORD • ACCESSO EFFETTUATO (PWD: BREVIANESE2026)
                            </div>
                            <h2 style="font-size: 22px; font-weight: 800; margin: 2px 0;" id="clubTitleHeader">VETRINA UFFICIALE: U.S.D. BREVIANESE</h2>
                            <div style="font-size: 13px; color: #e0f2fe;" id="clubDescHeader">
                                Stai visualizzando <b>SOLO i capi approvati per U.S.D. Brevianese</b>. Ritroverai sempre esattamente questi stessi articoli senza errori.
                            </div>
                        </div>
                    </div>
                    <div style="text-align: right; display: flex; flex-direction: column; gap: 6px; align-items: flex-end;">
                        <span class="pill-badge" style="background: #dcfce7; color: #166534; font-weight: 800;"><i class="fa-solid fa-check-double"></i> LINEA BLOCCATA & SEMPRE DISPONIBILE</span>
                        <span style="font-size: 11.5px; color: #bfdbfe;">store.italsport-group.it/it/158-clienti-my-italsport</span>
                    </div>
                </div>

                <!-- 3 Pillars explaining what "Vetrina Personalizzata con Password" means -->
                <div class="vetrina-pillars">
                    <div class="v-pillar">
                        <h4><i class="fa-solid fa-lock" style="color: #0284c7;"></i> 1. Accesso con Password Dedicata</h4>
                        <p>Ogni squadra accede con la propria password riservata e vede <b>solo ed esclusivamente le cose relative alla propria società</b>, senza confondersi con altri prodotti.</p>
                    </div>
                    <div class="v-pillar" style="border-left-color: #059669;">
                        <h4><i class="fa-solid fa-arrows-rotate" style="color: #059669;"></i> 2. Sempre gli Stessi Capi Senza Problemi</h4>
                        <p>La linea del club è codificata: chi entra oggi, a metà stagione o nei prossimi anni <b>trova sicuramente sempre le stesse cose</b>, stessi modelli e stessi colori senza errori.</p>
                    </div>
                    <div class="v-pillar" style="border-left-color: #d97706;">
                        <h4><i class="fa-solid fa-warehouse" style="color: #d97706;"></i> 3. Magazzino Gestito a Ciserano (BG)</h4>
                        <p>La società non deve anticipare soldi né tenere scatoloni in sede: <b>Italsport tiene il magazzino</b> e prepara ogni ordine con logo e personalizzazione ufficiale.</p>
                    </div>
                </div>

                <!-- 6 Locked-in Team Items using REAL Italsport Photos -->
                <div class="store-products-grid">
                    
                    <!-- Item 1: Kit Gara -->
                    <div class="product-item">
                        <div class="product-img-box">
                            <span class="locked-line-badge"><i class="fa-solid fa-lock"></i> CAPO UFFICIALE SQUADRA</span>
                            <img id="vetrinaKitImg" src="{prod_kit_blue_b64}" alt="Kit Gara Ufficiale">
                        </div>
                        <div class="product-info">
                            <div>
                                <div class="code-tag" id="codeKit">COD. KIT-GARA • LINEA BLOCCATA CLUB</div>
                                <h5 id="titleKit">Kit Gara Ufficiale U.S.D. Brevianese</h5>
                                <div style="font-size: 11.5px; color: #64748b; margin-bottom: 10px;">Maglia gara + pantaloncino con logo societario, sempre riordinabile identico anche per singoli nuovi iscritti.</div>
                            </div>
                            <button class="btn-buy" style="width: 100%;" onclick="openOrderModal('Kit Gara Ufficiale della Squadra')"><i class="fa-solid fa-check"></i> Seleziona Taglia (Sempre Disponibile)</button>
                        </div>
                    </div>

                    <!-- Item 2: Tuta Rom -->
                    <div class="product-item">
                        <div class="product-img-box">
                            <span class="locked-line-badge"><i class="fa-solid fa-lock"></i> CAPO UFFICIALE SQUADRA</span>
                            <img src="{prod_tuta_b64}" alt="Tuta Rom">
                        </div>
                        <div class="product-info">
                            <div>
                                <div class="code-tag">COD. TUTA ROM • RAPPRESENTANZA & ALLENAMENTO</div>
                                <h5>Tuta Completa "Rom" Personalizzata Club</h5>
                                <div style="font-size: 11.5px; color: #64748b; margin-bottom: 10px;">Giacca + pantalone coordinato nei colori ufficiali della società con stemma e stampa Italsport.</div>
                            </div>
                            <button class="btn-buy" style="width: 100%;" onclick="openOrderModal('Tuta Completa Rom')"><i class="fa-solid fa-check"></i> Seleziona Taglia (Sempre Disponibile)</button>
                        </div>
                    </div>

                    <!-- Item 3: Giacca Scotland V05041 -->
                    <div class="product-item">
                        <div class="product-img-box">
                            <span class="locked-line-badge"><i class="fa-solid fa-lock"></i> CAPO UFFICIALE SQUADRA</span>
                            <img src="{prod_scotland_b64}" alt="Giacca Tuta 1/2 Zip Scotland V05041">
                        </div>
                        <div class="product-info">
                            <div>
                                <div class="code-tag">COD. V05041 • SCOTLAND GIACCA 1/2 ZIP</div>
                                <h5>Giacca Allenamento 1/2 Zip "Scotland"</h5>
                                <div style="font-size: 11.5px; color: #64748b; margin-bottom: 10px;">Articolo codificato nella vetrina della squadra: nessuna variazione di modello o tonalità nel tempo.</div>
                            </div>
                            <button class="btn-buy" style="width: 100%;" onclick="openOrderModal('Giacca Scotland V05041')"><i class="fa-solid fa-check"></i> Seleziona Taglia (Sempre Disponibile)</button>
                        </div>
                    </div>

                    <!-- Item 4: Giubbotto Nepal V0202 -->
                    <div class="product-item">
                        <div class="product-img-box">
                            <span class="locked-line-badge"><i class="fa-solid fa-lock"></i> CAPO UFFICIALE SQUADRA</span>
                            <img src="{prod_nepal_b64}" alt="Giubbotto Sportivo Nepal V0202">
                        </div>
                        <div class="product-info">
                            <div>
                                <div class="code-tag">COD. V0202-PK5099 • NEPAL GIUBBOTTO</div>
                                <h5>Giubbotto Invernale "Nepal" con Logo Club</h5>
                                <div style="font-size: 11.5px; color: #64748b; margin-bottom: 10px;">Giaccone termico invernale approvato dalla società, disponibile in tutte le taglie giovanili e adulto.</div>
                            </div>
                            <button class="btn-buy" style="width: 100%;" onclick="openOrderModal('Giubbotto Sportivo Nepal V0202')"><i class="fa-solid fa-check"></i> Seleziona Taglia (Sempre Disponibile)</button>
                        </div>
                    </div>

                    <!-- Item 5: Rain K-Way A0600 -->
                    <div class="product-item">
                        <div class="product-img-box">
                            <span class="locked-line-badge"><i class="fa-solid fa-lock"></i> CAPO UFFICIALE SQUADRA</span>
                            <img src="{prod_kway_b64}" alt="Rain K-Way A0600">
                        </div>
                        <div class="product-info">
                            <div>
                                <div class="code-tag">COD. A0600 • RAIN K-WAY ANTIVENTO</div>
                                <h5>K-Way Antipioggia Ufficiale della Squadra</h5>
                                <div style="font-size: 11.5px; color: #64748b; margin-bottom: 10px;">Sempre presente nella vetrina protetta del club per riordini rapidi senza mai sbagliare modello.</div>
                            </div>
                            <button class="btn-buy" style="width: 100%;" onclick="openOrderModal('Rain K-Way A0600')"><i class="fa-solid fa-check"></i> Seleziona Taglia (Sempre Disponibile)</button>
                        </div>
                    </div>

                    <!-- Item 6: Borsa Bauletto V12027 -->
                    <div class="product-item">
                        <div class="product-img-box">
                            <span class="locked-line-badge"><i class="fa-solid fa-lock"></i> CAPO UFFICIALE SQUADRA</span>
                            <img src="{prod_borsa_b64}" alt="Borsa Bauletto V12027">
                        </div>
                        <div class="product-info">
                            <div>
                                <div class="code-tag">COD. V12027 • BORSA BAULETTO CLUB</div>
                                <h5>Borsa Bauletto Personalizzata con Stemma</h5>
                                <div style="font-size: 11.5px; color: #64748b; margin-bottom: 10px;">Borsa ufficiale della linea societaria con vano scarpe, pronta a magazzino presso Italsport Ciserano.</div>
                            </div>
                            <button class="btn-buy" style="width: 100%;" onclick="openOrderModal('Borsa Bauletto V12027')"><i class="fa-solid fa-check"></i> Ordina dalla Vetrina Squadra</button>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <!-- TAB 4: PRO-CLUB FIDELITY CARD (BASIC, SILVER, GOLD, DIAMOND) -->
    <div id="tab-fidelity" class="tab-content">
        <div class="fidelity-card-section">
            <div style="text-align: center; max-width: 740px; margin: 0 auto 25px auto;">
                <span class="pill-badge" style="background: #fef3c7; color: #b45309; margin-bottom: 8px;">PROGRAMMA FEDELTÀ UFFICIALE ITALSPORT GROUP • CISERANO (BG)</span>
                <h2 style="font-size: 24px; font-weight: 800; color: #0f172a;">Tessera "PRO-CLUB" (Basic, Silver, Gold, Diamond)</h2>
                <p style="font-size: 13.5px; color: #475569;">
                    La vera Card Pro-Club di Italsport garantisce alle società sportive partner <b>Disponibilità, Servizio, Qualità e Continuità</b> insieme alla Vetrina Online protetta da password.
                </p>
            </div>

            <!-- Real Pro-Club Card + 4 Official Tiers -->
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px; align-items: center; margin-bottom: 30px;">
                <div style="background: #f8fafc; border: 1px solid var(--border-color); border-radius: 16px; padding: 20px; text-align: center;">
                    <img src="{card_real_b64}" alt="Tessera Pro-Club Ufficiale Italsport" style="max-width: 100%; height: 220px; object-fit: contain; border-radius: 12px; box-shadow: var(--shadow-md);">
                    <div style="font-size: 12px; font-weight: 700; color: #475569; margin-top: 10px;">
                        Grafica ufficiale "TESSERA pro club" dal sito <b>italsport-group.it</b>
                    </div>
                </div>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
                    <div style="background: #1e40af; color: #fff; padding: 18px; border-radius: 12px;">
                        <span style="font-size: 10px; font-weight: 800; background: #dbeafe; color: #1e40af; padding: 3px 8px; border-radius: 6px;">1° LIVELLO</span>
                        <h4 style="font-size: 16px; font-weight: 800; margin-top: 10px;">PRO CLUB BASIC</h4>
                        <p style="font-size: 12px; color: #bfdbfe; margin-top: 4px;">Listino riservato al club, codifica linea societaria e riassortimenti garantiti.</p>
                    </div>
                    <div style="background: #475569; color: #fff; padding: 18px; border-radius: 12px;">
                        <span style="font-size: 10px; font-weight: 800; background: #e2e8f0; color: #334155; padding: 3px 8px; border-radius: 6px;">2° LIVELLO</span>
                        <h4 style="font-size: 16px; font-weight: 800; margin-top: 10px;">PRO CLUB SILVER</h4>
                        <p style="font-size: 12px; color: #e2e8f0; margin-top: 4px;">Sconto extra sulle forniture, Vetrina Squadra con password e zero costi di magazzino.</p>
                    </div>
                    <div style="background: #b45309; color: #fff; padding: 18px; border-radius: 12px;">
                        <span style="font-size: 10px; font-weight: 800; background: #fef3c7; color: #b45309; padding: 3px 8px; border-radius: 6px;">3° LIVELLO</span>
                        <h4 style="font-size: 16px; font-weight: 800; margin-top: 10px;">PRO CLUB GOLD</h4>
                        <p style="font-size: 12px; color: #fde68a; margin-top: 4px;">Priorità sulle consegne di inizio stagione e bonus fornitura per la società.</p>
                    </div>
                    <div style="background: #0f172a; color: #fff; padding: 18px; border-radius: 12px; border: 1.5px solid #38bdf8;">
                        <span style="font-size: 10px; font-weight: 800; background: #e0f2fe; color: #0369a1; padding: 3px 8px; border-radius: 6px;">4° LIVELLO TOP</span>
                        <h4 style="font-size: 16px; font-weight: 800; margin-top: 10px;">PRO CLUB DIAMOND</h4>
                        <p style="font-size: 12px; color: #cbd5e1; margin-top: 4px;">Partnership completa pluriennale con condizioni top e supporto dedicato a 360°.</p>
                    </div>
                </div>
            </div>

            <!-- 4 Official Pillars of Italsport Pro-Club -->
            <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 15px;">
                <div style="background: #f8fafc; border: 1px solid var(--border-color); border-radius: 12px; padding: 16px;">
                    <div style="font-size: 20px; color: #0284c7; margin-bottom: 8px;"><i class="fa-solid fa-boxes-stacked"></i></div>
                    <h4 style="font-size: 13px; font-weight: 700; color: #0f172a; margin-bottom: 4px;">1. Disponibilità (Zero Magazzino)</h4>
                    <p style="font-size: 11.5px; color: #475569; line-height: 1.4;">Facciamo noi il magazzino a Ciserano per la tua società: zero anticipi di cassa e zero rimanenze invendute.</p>
                </div>
                <div style="background: #f8fafc; border: 1px solid var(--border-color); border-radius: 12px; padding: 16px;">
                    <div style="font-size: 20px; color: #059669; margin-bottom: 8px;"><i class="fa-solid fa-headset"></i></div>
                    <h4 style="font-size: 13px; font-weight: 700; color: #0f172a; margin-bottom: 4px;">2. Servizio + Vetrina Password</h4>
                    <p style="font-size: 11.5px; color: #475569; line-height: 1.4;">Vetrina dedicata su store.italsport-group.it protetta da password dove ogni squadra vede solo i propri capi.</p>
                </div>
                <div style="background: #f8fafc; border: 1px solid var(--border-color); border-radius: 12px; padding: 16px;">
                    <div style="font-size: 20px; color: #d97706; margin-bottom: 8px;"><i class="fa-solid fa-medal"></i></div>
                    <h4 style="font-size: 13px; font-weight: 700; color: #0f172a; margin-bottom: 4px;">3. Qualità Garantita 30 Anni</h4>
                    <p style="font-size: 11.5px; color: #475569; line-height: 1.4;">Tessuti tecnici, stampe e ricami selezionati da Italsport per resistere agli allenamenti e ai lavaggi frequenti.</p>
                </div>
                <div style="background: #f8fafc; border: 1px solid var(--border-color); border-radius: 12px; padding: 16px;">
                    <div style="font-size: 20px; color: #7c3aed; margin-bottom: 8px;"><i class="fa-solid fa-arrows-rotate"></i></div>
                    <h4 style="font-size: 13px; font-weight: 700; color: #0f172a; margin-bottom: 4px;">4. Continuità negli Anni</h4>
                    <p style="font-size: 11.5px; color: #475569; line-height: 1.4;">La squadra ritrova sempre esattamente gli stessi articoli e gli stessi colori anche per i riordini futuri.</p>
                </div>
            </div>

            <div style="text-align: center; margin-top: 25px;">
                <button class="nav-btn btn-pdf" style="display: inline-flex; padding: 10px 24px; font-size: 14px;" onclick="alert('Richiesta Tessera Pro-Club inviata a Italsport Group — Via Provinciale Francesca 2H/I, Ciserano (BG) • Tel. 035 4191221 • info@italsport-group.it')">
                    <i class="fa-solid fa-id-card"></i> Richiedi la Tessera Pro-Club e la Vetrina con Password per la Tua Società
                </button>
            </div>
        </div>
    </div>

</div>

{IG_MODAL}

<script>
// Switch Tabs
function switchTab(tabId) {{
    document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
    document.querySelectorAll('.nav-btn').forEach(el => {{
        if(!el.classList.contains('btn-pdf')) el.classList.remove('active');
    }});

    const targetTab = document.getElementById('tab-' + tabId);
    if(targetTab) targetTab.classList.add('active');

    const activeBtn = Array.from(document.querySelectorAll('.nav-btn')).find(b => b.getAttribute('onclick') && b.getAttribute('onclick').includes(tabId));
    if(activeBtn) activeBtn.classList.add('active');

    window.scrollTo({{ top: 0, behavior: 'smooth' }});
}}

// Toggle Real 3D Video Box highlight
function toggleReal3dVideo() {{
    const box = document.getElementById('real3dVideoBox');
    const txt = document.getElementById('real3dBtnTxt');
    if (box.style.display === 'none') {{
        box.style.display = 'block';
        txt.textContent = 'Mostra Solo Simulatore Interattivo';
    }} else {{
        box.style.display = 'none';
        txt.textContent = 'Mostra Animazione 3D 360° Reale';
    }}
}}

// Interactive Password-Protected Club Showcase (My Italsport)
const CLUB_VETRINE = {{
    brevianese: {{
        name: 'U.S.D. BREVIANESE',
        pwd: 'BREVIANESE2026',
        bg: '#1e3a8a',
        kitImg: '{prod_kit_blue_b64}',
        kitTitle: 'Kit Gara Ufficiale U.S.D. Brevianese (Blu/Bianco)',
        desc: 'Stai visualizzando <b>SOLO i capi approvati per U.S.D. Brevianese</b>. Ritroverai sempre esattamente questi stessi articoli senza errori.'
    }},
    gessate: {{
        name: 'A.S.D. GESSATE',
        pwd: 'GESSATE2026',
        bg: '#991b1b',
        kitImg: '{prod_kit_red_b64}',
        kitTitle: 'Kit Gara Ufficiale A.S.D. Gessate (Rosso/Bianco)',
        desc: 'Stai visualizzando <b>SOLO i capi approvati per A.S.D. Gessate</b>. Ritroverai sempre esattamente questi stessi articoli senza errori.'
    }},
    ciserano: {{
        name: 'VOLLEY CISERANO BG',
        pwd: 'CISERANO2026',
        bg: '#0f172a',
        kitImg: '{prod_kit_gold_b64}',
        kitTitle: 'Kit Gara Ufficiale Volley Ciserano (Antracite/Oro)',
        desc: 'Stai visualizzando <b>SOLO i capi approvati per Volley Ciserano BG</b>. Ritroverai sempre esattamente questi stessi articoli senza errori.'
    }}
}};

function selectClubVetrina(clubKey) {{
    const c = CLUB_VETRINE[clubKey];
    if (!c) return;
    document.getElementById('pwdLoginOverlay').style.display = 'none';
    document.getElementById('unlockedVetrinaBody').style.display = 'block';

    document.querySelectorAll('.pwd-pill').forEach(b => b.classList.remove('active'));
    const pill = document.getElementById('pill-' + clubKey);
    if (pill) pill.classList.add('active');

    document.getElementById('clubBannerBg').style.background = c.bg;
    document.getElementById('clubCrestIcon').style.color = c.bg;
    document.getElementById('clubSubHeader').textContent = `VETRINA PROTETTA CON PASSWORD • ACCESSO EFFETTUATO (PWD: ${{c.pwd}})`;
    document.getElementById('clubTitleHeader').textContent = `VETRINA UFFICIALE: ${{c.name}}`;
    document.getElementById('clubDescHeader').innerHTML = c.desc;
    document.getElementById('vetrinaKitImg').src = c.kitImg;
    document.getElementById('titleKit').textContent = c.kitTitle;
}}

function showPasswordLoginGate() {{
    document.getElementById('pwdLoginOverlay').style.display = 'flex';
    document.getElementById('unlockedVetrinaBody').style.display = 'none';
}}

function syncGatePassword() {{
    const k = document.getElementById('gateClubSelect').value;
    if (CLUB_VETRINE[k]) {{
        document.getElementById('gatePwdInput').value = CLUB_VETRINE[k].pwd;
    }}
}}

function unlockClubVetrina() {{
    const k = document.getElementById('gateClubSelect').value;
    selectClubVetrina(k);
}}

// 3D Configurator State
let currentPrimary = '#1e3a8a';
let currentAccent = '#eab308';
let currentPattern = 'solid';
let currentAngle = 0;
let isSpinning = false;
let spinInterval = null;

function setPrimaryColor(color, el) {{
    currentPrimary = color;
    document.querySelectorAll('#primarySwatches .swatch').forEach(s => s.classList.remove('active'));
    if(el) el.classList.add('active');

    document.getElementById('leftSleeve').setAttribute('fill', color);
    document.getElementById('rightSleeve').setAttribute('fill', color);
    document.getElementById('jerseyBody').setAttribute('fill', color);
    updatePatternVisual();
}}

function setAccentColor(color, el) {{
    currentAccent = color;
    document.querySelectorAll('#accentSwatches .swatch').forEach(s => s.classList.remove('active'));
    if(el) el.classList.add('active');

    document.getElementById('leftCuff').setAttribute('fill', color);
    document.getElementById('rightCuff').setAttribute('fill', color);
    document.getElementById('jerseyCollar').setAttribute('fill', color);
}}

function setPattern(pat, el) {{
    currentPattern = pat;
    document.querySelectorAll('.pattern-options .opt-btn').forEach(b => b.classList.remove('active'));
    if(el) el.classList.add('active');
    updatePatternVisual();
}}

function updatePatternVisual() {{
    const patLayer = document.getElementById('jerseyPattern');
    if (currentPattern === 'stripes') {{
        patLayer.setAttribute('fill', 'url(#patStripes)');
    }} else if (currentPattern === 'chevron') {{
        patLayer.setAttribute('fill', 'url(#patChevron)');
    }} else {{
        patLayer.setAttribute('fill', 'none');
    }}
}}

function setCollar(type, el) {{
    document.querySelectorAll('.collar-options .opt-btn').forEach(b => b.classList.remove('active'));
    if(el) el.classList.add('active');

    const collar = document.getElementById('jerseyCollar');
    if (type === 'crew') {{
        collar.setAttribute('d', 'M 160 72 Q 200 100 240 72 Q 200 85 160 72 Z');
    }} else if (type === 'polo') {{
        collar.setAttribute('d', 'M 155 70 L 200 115 L 245 70 L 220 66 L 200 85 L 180 66 Z');
    }} else {{
        collar.setAttribute('d', 'M 160 72 Q 200 115 240 72 Q 200 90 160 72 Z');
    }}
}}

function updateSponsorText(text) {{
    document.getElementById('sponsorText').textContent = text.toUpperCase() || 'ITALSPORT';
}}

function rotateJersey(delta) {{
    currentAngle += delta;
    document.getElementById('jerseyBox').style.transform = `perspective(1000px) rotateY(${{currentAngle}}deg)`;
}}

function resetRotation() {{
    currentAngle = 0;
    document.getElementById('jerseyBox').style.transform = `perspective(1000px) rotateY(0deg)`;
}}

function toggleAutoSpin() {{
    isSpinning = !isSpinning;
    const btnText = document.getElementById('spin-text');
    if (isSpinning) {{
        btnText.textContent = 'Rotazione Auto: ON';
        spinInterval = setInterval(() => {{
            rotateJersey(4);
        }}, 60);
    }} else {{
        btnText.textContent = 'Rotazione Auto: OFF';
        clearInterval(spinInterval);
    }}
}}

{IG_JS}

function openOrderModal(prodName) {{
    alert(`Vetrina Riservata My Italsport — "${{prodName}}":\\n\\n✔️ Capo ufficiale approvato e bloccato per la tua squadra\\n✔️ Nessun rischio di sbagliare modello o colore\\n✔️ Sempre disponibile nel magazzino Italsport di Ciserano (BG)`);
}}
</script>

</body>
</html>
"""

with open("Instagram_Mockup_Italsport.html", "w", encoding="utf-8") as f:
    f.write(html_mockup)

print(f"Instagram_Mockup_Italsport.html written successfully ({len(html_mockup)} bytes).")
