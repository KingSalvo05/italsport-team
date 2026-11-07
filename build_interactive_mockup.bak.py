import os, base64

def get_base64_image(filename):
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            b64 = base64.b64encode(f.read()).decode('utf-8')
            ext = 'png' if filename.endswith('.png') else 'jpeg'
            return f"data:image/{ext};base64,{b64}"
    return ""

print("Encoding images for web app mockup...")
logo_b64 = get_base64_image("cropped-cropped-italsportlogo.png")
post1_b64 = get_base64_image("img_post1_jersey.jpg")
post2_b64 = get_base64_image("img_post2_3d.jpg")
post3_b64 = get_base64_image("img_post3_fidelity.jpg")
post4_b64 = get_base64_image("img_post4_stack.jpg")
post5_b64 = get_base64_image("img_post5_portal.jpg")
post6_b64 = get_base64_image("img_post6_winter.jpg")
post7_b64 = get_base64_image("img_post7_celebration.jpg")

cfg_b64 = get_base64_image("site_configuratore.jpg")
portal_b64 = get_base64_image("site_membro_myitalsport.jpg")

html_mockup = f"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Italsport Group - Piattaforma Strategica & Mockup Instagram 2026</title>
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

/* Instagram UI Layout */
.insta-container {{
    max-width: 820px;
    margin: 0 auto;
    background: #ffffff;
    border: 1px solid var(--border-color);
    border-radius: 16px;
    box-shadow: var(--shadow-md);
    overflow: hidden;
}}

.insta-header {{
    padding: 30px 35px 20px 35px;
    border-bottom: 1px solid var(--border-color);
    display: flex;
    gap: 35px;
    align-items: flex-start;
}}

.insta-avatar {{
    width: 120px;
    height: 120px;
    border-radius: 50%;
    padding: 3px;
    background: linear-gradient(45deg, #f09433, #e6683c, #dc2743, #cc2366, #bc1888);
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
}}

.insta-avatar-inner {{
    width: 100%;
    height: 100%;
    background: #ffffff;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    padding: 8px;
}}

.insta-avatar-inner img {{
    width: 100%;
    height: 100%;
    object-fit: contain;
}}

.insta-profile-info {{
    flex: 1;
}}

.profile-top-line {{
    display: flex;
    align-items: center;
    gap: 16px;
    margin-bottom: 15px;
    flex-wrap: wrap;
}}

.profile-username {{
    font-size: 19px;
    font-weight: 700;
    color: var(--text-primary);
    display: flex;
    align-items: center;
    gap: 6px;
}}

.verified-icon {{
    color: #0284c7;
    font-size: 17px;
}}

.btn-follow {{
    background: #0284c7;
    color: #ffffff;
    border: none;
    padding: 6px 18px;
    border-radius: 8px;
    font-weight: 700;
    font-size: 13px;
    cursor: pointer;
}}

.btn-contact {{
    background: #f1f5f9;
    color: var(--text-primary);
    border: 1px solid var(--border-color);
    padding: 6px 14px;
    border-radius: 8px;
    font-weight: 600;
    font-size: 13px;
    cursor: pointer;
}}

.insta-stats {{
    display: flex;
    gap: 25px;
    margin-bottom: 14px;
    font-size: 14px;
}}

.insta-stats span {{
    font-weight: 700;
    color: var(--text-primary);
}}

.insta-bio {{
    font-size: 13px;
    line-height: 1.45;
    color: #334155;
}}

.insta-bio b {{
    color: #0f172a;
}}

.insta-bio a {{
    color: #0284c7;
    text-decoration: none;
    font-weight: 600;
}}

/* Stories Highlights */
.insta-stories {{
    padding: 16px 25px;
    display: flex;
    gap: 18px;
    overflow-x: auto;
    border-bottom: 1px solid var(--border-color);
    background: #fafafa;
}}

.story-item {{
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 6px;
    cursor: pointer;
    text-align: center;
    flex-shrink: 0;
}}

.story-circle {{
    width: 64px;
    height: 64px;
    border-radius: 50%;
    padding: 2px;
    border: 2px solid #cbd5e1;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #ffffff;
    transition: transform 0.2s;
}}

.story-item:hover .story-circle {{
    transform: scale(1.05);
    border-color: #0284c7;
}}

.story-icon {{
    width: 54px;
    height: 54px;
    border-radius: 50%;
    background: #f1f5f9;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
    color: var(--brand-navy);
}}

.story-label {{
    font-size: 11px;
    font-weight: 600;
    color: #475569;
    max-width: 72px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}}

/* Posts Grid */
.insta-grid-nav {{
    display: flex;
    justify-content: center;
    gap: 40px;
    border-bottom: 1px solid var(--border-color);
    background: #ffffff;
}}

.grid-nav-item {{
    padding: 14px 0;
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: var(--text-muted);
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 6px;
    border-top: 2px solid transparent;
    margin-top: -1px;
}}

.grid-nav-item.active {{
    color: var(--brand-navy);
    border-top-color: var(--brand-navy);
}}

.posts-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 4px;
    padding: 4px;
    background: #ffffff;
}}

.grid-post {{
    position: relative;
    aspect-ratio: 1/1;
    overflow: hidden;
    cursor: pointer;
    background: #f1f5f9;
}}

.grid-post img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.3s ease;
}}

.grid-post:hover img {{
    transform: scale(1.04);
}}

.post-overlay {{
    position: absolute;
    inset: 0;
    background: rgba(15, 23, 42, 0.65);
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 18px;
    color: #ffffff;
    font-weight: 700;
    font-size: 14px;
    opacity: 0;
    transition: opacity 0.2s ease;
}}

.grid-post:hover .post-overlay {{
    opacity: 1;
}}

.post-tag-badge {{
    position: absolute;
    top: 10px;
    right: 10px;
    background: rgba(15, 23, 42, 0.85);
    color: #ffffff;
    font-size: 10px;
    font-weight: 700;
    padding: 3px 8px;
    border-radius: 4px;
    backdrop-filter: blur(4px);
    z-index: 2;
}}

.post-badge-3d {{
    background: #0284c7;
}}

.post-badge-card {{
    background: #d97706;
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
    align-items: center;
}}

.jersey-stage {{
    background: radial-gradient(circle at center, #ffffff 0%, #f1f5f9 100%);
    border: 1px solid var(--border-color);
    border-radius: 16px;
    padding: 30px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 480px;
    position: relative;
    box-shadow: inset 0 2px 4px rgba(0,0,0,0.02);
}}

.jersey-canvas-box {{
    width: 280px;
    height: 340px;
    position: relative;
    transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}}

/* Interactive SVG Shirt */
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
    gap: 18px;
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

/* Dedicated Club Storefront (My Italsport) */
.club-storefront {{
    background: #ffffff;
    border: 1px solid var(--border-color);
    border-radius: 16px;
    overflow: hidden;
    box-shadow: var(--shadow-md);
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

.store-products-grid {{
    padding: 28px;
    display: grid;
    grid-template-columns: repeat(4, 1fr);
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
    height: 180px;
    background: #f8fafc;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 15px;
    border-bottom: 1px solid var(--border-color);
}}

.product-img-box img {{
    max-height: 100%;
    max-width: 100%;
    object-fit: contain;
}}

.product-info {{
    padding: 14px;
    display: flex;
    flex-direction: column;
    flex: 1;
    justify-content: space-between;
}}

.product-info h5 {{
    font-size: 13px;
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: 4px;
}}

.product-info .price {{
    font-size: 16px;
    font-weight: 800;
    color: #0284c7;
    margin-bottom: 10px;
}}

.btn-buy {{
    background: var(--brand-navy);
    color: #ffffff;
    border: none;
    padding: 7px 12px;
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

.vip-card-wrap {{
    display: flex;
    justify-content: center;
    margin: 25px 0 35px 0;
}}

.vip-card-box {{
    width: 480px;
    height: 270px;
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #334155 100%);
    border-radius: 20px;
    padding: 24px;
    color: #ffffff;
    position: relative;
    box-shadow: 0 20px 25px -5px rgba(0,0,0,0.2), 0 8px 10px -6px rgba(0,0,0,0.1);
    border: 1px solid #475569;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}}

.vip-card-box::after {{
    content: "";
    position: absolute;
    top: 0;
    right: 0;
    width: 140px;
    height: 100%;
    background: linear-gradient(135deg, rgba(217, 119, 6, 0.15) 0%, transparent 100%);
    border-radius: 0 20px 20px 0;
    pointer-events: none;
}}

/* Modal Post Detail */
.modal-backdrop {{
    position: fixed;
    inset: 0;
    background: rgba(15, 23, 42, 0.75);
    backdrop-filter: blur(4px);
    z-index: 1000;
    display: none;
    align-items: center;
    justify-content: center;
    padding: 20px;
}}

.modal-backdrop.active {{
    display: flex;
}}

.modal-content {{
    background: #ffffff;
    border-radius: 16px;
    max-width: 900px;
    width: 100%;
    max-height: 90vh;
    overflow: hidden;
    display: grid;
    grid-template-columns: 1fr 1fr;
    box-shadow: var(--shadow-lg);
    position: relative;
}}

.modal-img-col {{
    background: #0f172a;
    display: flex;
    align-items: center;
    justify-content: center;
}}

.modal-img-col img {{
    width: 100%;
    height: 100%;
    object-fit: contain;
}}

.modal-info-col {{
    padding: 24px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    overflow-y: auto;
}}

.modal-close {{
    position: absolute;
    top: 14px;
    right: 14px;
    background: #ffffff;
    border: 1px solid var(--border-color);
    width: 32px;
    height: 32px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    font-size: 15px;
    color: var(--text-secondary);
    z-index: 10;
}}

@media (max-width: 768px) {{
    .cfg-workspace {{
        grid-template-columns: 1fr;
    }}
    .store-products-grid {{
        grid-template-columns: 1fr 1fr;
    }}
    .modal-content {{
        grid-template-columns: 1fr;
    }}
    .modal-img-col {{
        max-height: 320px;
    }}
    .insta-header {{
        flex-direction: column;
        align-items: center;
        text-align: center;
    }}
    .insta-stats {{
        justify-content: center;
    }}
    .profile-top-line {{
        justify-content: center;
    }}
}}
</style>
</head>
<body>

<!-- TOP NAVIGATION -->
<nav class="top-nav">
    <div class="nav-container">
        <div class="brand-area">
            <img src="{logo_b64}" alt="Italsport Group Logo">
            <span class="brand-tag">PIANO SOCIAL & COMMERCIALE 2026</span>
        </div>
        <div class="nav-tabs">
            <button class="nav-btn active" onclick="switchTab('feed')"><i class="fa-brands fa-instagram"></i> Mockup Feed Instagram</button>
            <button class="nav-btn" onclick="switchTab('configurator')"><i class="fa-solid fa-shirt"></i> Configuratore 3D Live</button>
            <button class="nav-btn" onclick="switchTab('storefront')"><i class="fa-solid fa-store"></i> Vetrina Club "My Italsport"</button>
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
                PRESENTAZIONE UFFICIALE PER IL CLIENTE • PALETTE CHIARA & ASSET REALI
            </div>
            <h1>ITALSPORT GROUP — Strategia Social & Posizionamento B2B</h1>
            <p>
                Piattaforma interattiva per la presentazione del piano editoriale Instagram. Include il simulatore 3D della maglia modificabile in tempo reale, la dimostrazione della vetrina online My Italsport per le squadre e il programma fedeltà Pro-Club.
            </p>
        </div>
        <div class="exec-badges">
            <span class="pill-badge" style="background: #e0f2fe; color: #0369a1;"><i class="fa-solid fa-check"></i> 7 Post con Foto dal Sito</span>
            <span class="pill-badge" style="background: #dcfce7; color: #15803d;"><i class="fa-solid fa-cubes"></i> Maglia 3D Interattiva</span>
            <span class="pill-badge" style="background: #fef3c7; color: #b45309;"><i class="fa-solid fa-award"></i> Tessera Fedeltà B2B</span>
        </div>
    </div>

    <!-- TAB 1: INSTAGRAM FEED MOCKUP -->
    <div id="tab-feed" class="tab-content active">
        <div class="insta-container">
            
            <!-- Profile Header -->
            <div class="insta-header">
                <div class="insta-avatar">
                    <div class="insta-avatar-inner">
                        <img src="{logo_b64}" alt="Italsport Profile">
                    </div>
                </div>
                <div class="insta-profile-info">
                    <div class="profile-top-line">
                        <div class="profile-username">
                            italsport_group
                            <i class="fa-solid fa-circle-check verified-icon" title="Verificato"></i>
                        </div>
                        <button class="btn-follow">Segui già</button>
                        <button class="btn-contact">Contatta</button>
                        <button class="btn-contact" onclick="switchTab('configurator')"><i class="fa-solid fa-shirt"></i> Configura 3D</button>
                    </div>

                    <div class="insta-stats">
                        <div><span>7</span> post</div>
                        <div><span>2.840</span> follower</div>
                        <div><span>310</span> seguiti</div>
                    </div>

                    <div class="insta-bio">
                        <b>ITALSPORT GROUP | Sartoria & Forniture Sportive</b><br>
                        🏆 Da oltre 30 anni vestiamo lo sport con manifattura diretta a Palermo.<br>
                        👕 Stampa a sublimazione full-print & DTF ad alta tenuta.<br>
                        🎨 Progetta la divisa della tua squadra con il nostro Configuratore 3D.<br>
                        🛒 Vetrina online My Italsport riservata per ogni club affiliato.<br>
                        🔗 <a href="https://store.italsport-group.it" target="_blank">store.italsport-group.it</a>
                    </div>
                </div>
            </div>

            <!-- Stories Highlights -->
            <div class="insta-stories">
                <div class="story-item" onclick="switchTab('configurator')">
                    <div class="story-circle">
                        <div class="story-icon"><i class="fa-solid fa-cubes"></i></div>
                    </div>
                    <span class="story-label">Configuratore 3D</span>
                </div>
                <div class="story-item" onclick="switchTab('storefront')">
                    <div class="story-circle">
                        <div class="story-icon"><i class="fa-solid fa-store"></i></div>
                    </div>
                    <span class="story-label">Vetrine Club</span>
                </div>
                <div class="story-item" onclick="switchTab('fidelity')">
                    <div class="story-circle">
                        <div class="story-icon"><i class="fa-solid fa-id-card"></i></div>
                    </div>
                    <span class="story-label">Tessera Pro</span>
                </div>
                <div class="story-item" onclick="openPostModal(1)">
                    <div class="story-circle">
                        <div class="story-icon"><i class="fa-solid fa-industry"></i></div>
                    </div>
                    <span class="story-label">Manifattura</span>
                </div>
                <div class="story-item" onclick="openPostModal(4)">
                    <div class="story-circle">
                        <div class="story-icon"><i class="fa-solid fa-arrows-rotate"></i></div>
                    </div>
                    <span class="story-label">Riassortimenti</span>
                </div>
                <div class="story-item" onclick="openPostModal(7)">
                    <div class="story-circle">
                        <div class="story-icon"><i class="fa-solid fa-users"></i></div>
                    </div>
                    <span class="story-label">Community</span>
                </div>
            </div>

            <!-- Grid Nav -->
            <div class="insta-grid-nav">
                <div class="grid-nav-item active"><i class="fa-solid fa-table-cells"></i> POST PUBBLICATI</div>
                <div class="grid-nav-item" onclick="switchTab('configurator')"><i class="fa-solid fa-clapperboard"></i> REEL 3D</div>
                <div class="grid-nav-item"><i class="fa-regular fa-bookmark"></i> SALVATI</div>
            </div>

            <!-- Posts Grid (7 Real Posts) -->
            <div class="posts-grid">
                
                <!-- Post 1 -->
                <div class="grid-post" onclick="openPostModal(1)">
                    <span class="post-tag-badge">MANIFATTURA</span>
                    <img src="{post1_b64}" alt="Post 1">
                    <div class="post-overlay">
                        <div><i class="fa-solid fa-heart"></i> 142</div>
                        <div><i class="fa-solid fa-comment"></i> 18</div>
                    </div>
                </div>

                <!-- Post 2 (3D Configurator) -->
                <div class="grid-post" onclick="openPostModal(2)">
                    <span class="post-tag-badge post-badge-3d"><i class="fa-solid fa-cube"></i> 3D LIVE</span>
                    <img src="{post2_b64}" alt="Post 2">
                    <div class="post-overlay">
                        <div><i class="fa-solid fa-heart"></i> 265</div>
                        <div><i class="fa-solid fa-comment"></i> 44</div>
                    </div>
                </div>

                <!-- Post 3 (Tessera Fedeltà) -->
                <div class="grid-post" onclick="openPostModal(3)">
                    <span class="post-tag-badge post-badge-card"><i class="fa-solid fa-award"></i> PRO-CLUB</span>
                    <img src="{post3_b64}" alt="Post 3">
                    <div class="post-overlay">
                        <div><i class="fa-solid fa-heart"></i> 198</div>
                        <div><i class="fa-solid fa-comment"></i> 31</div>
                    </div>
                </div>

                <!-- Post 4 (Riassortimenti) -->
                <div class="grid-post" onclick="openPostModal(4)">
                    <span class="post-tag-badge">ZERO MINIMI</span>
                    <img src="{post4_b64}" alt="Post 4">
                    <div class="post-overlay">
                        <div><i class="fa-solid fa-heart"></i> 173</div>
                        <div><i class="fa-solid fa-comment"></i> 22</div>
                    </div>
                </div>

                <!-- Post 5 (Vetrina Squadre) -->
                <div class="grid-post" onclick="openPostModal(5)">
                    <span class="post-tag-badge post-badge-3d">PORTALE CLUB</span>
                    <img src="{post5_b64}" alt="Post 5">
                    <div class="post-overlay">
                        <div><i class="fa-solid fa-heart"></i> 214</div>
                        <div><i class="fa-solid fa-comment"></i> 39</div>
                    </div>
                </div>

                <!-- Post 6 (Linea Invernale) -->
                <div class="grid-post" onclick="openPostModal(6)">
                    <span class="post-tag-badge">COLLEZIONE</span>
                    <img src="{post6_b64}" alt="Post 6">
                    <div class="post-overlay">
                        <div><i class="fa-solid fa-heart"></i> 156</div>
                        <div><i class="fa-solid fa-comment"></i> 14</div>
                    </div>
                </div>

                <!-- Post 7 (Community) -->
                <div class="grid-post" onclick="openPostModal(7)">
                    <span class="post-tag-badge">PARTNER</span>
                    <img src="{post7_b64}" alt="Post 7">
                    <div class="post-overlay">
                        <div><i class="fa-solid fa-heart"></i> 289</div>
                        <div><i class="fa-solid fa-comment"></i> 52</div>
                    </div>
                </div>

            </div>
        </div>
    </div>

    <!-- TAB 2: INTERACTIVE 3D CONFIGURATOR -->
    <div id="tab-configurator" class="tab-content">
        <div class="configurator-panel">
            <div class="cfg-header">
                <div>
                    <span class="pill-badge" style="background: #e0f2fe; color: #0369a1; margin-bottom: 6px;">SIMULATORE DI PRODUZIONE INTERATTIVO</span>
                    <h2>Configuratore Maglia Ufficiale in Tempo Reale</h2>
                    <p>Modifica colori sociali, pattern sublimatico, tipo di colletto e ruota la maglietta prima di mandarla in stampa.</p>
                </div>
                <div style="display: flex; gap: 8px;">
                    <button class="tool-btn" onclick="toggleAutoSpin()"><i class="fa-solid fa-rotate"></i> <span id="spin-text">Rotazione Automatica: OFF</span></button>
                    <button class="tool-btn" style="background: #0284c7; color: #fff; border-color: #0284c7;" onclick="alert('Bozza grafica salvata con successo! Puoi inviarla direttamente al laboratorio Italsport.')"><i class="fa-solid fa-floppy-disk"></i> Salva Configurazione</button>
                </div>
            </div>

            <div class="cfg-workspace">
                
                <!-- Jersey Stage -->
                <div class="jersey-stage">
                    <div class="jersey-canvas-box" id="jerseyBox">
                        
                        <!-- SVG Custom Soccer Jersey -->
                        <svg class="jersey-svg" id="jerseySvg" viewBox="0 0 400 450" xmlns="http://www.w3.org/2000/svg">
                            <defs>
                                <!-- Stripes Pattern -->
                                <pattern id="patStripes" width="50" height="400" patternUnits="userSpaceOnUse">
                                    <rect width="25" height="400" fill="var(--color-primary, #1e3a8a)"/>
                                    <rect x="25" width="25" height="400" fill="var(--color-secondary, #ffffff)"/>
                                </pattern>
                                <!-- Chevron Pattern -->
                                <pattern id="patChevron" width="40" height="40" patternUnits="userSpaceOnUse">
                                    <path d="M0 20 L20 40 L40 20 L20 0 Z" fill="var(--color-secondary, #ffffff)" opacity="0.25"/>
                                </pattern>
                                <!-- Shading Gradient -->
                                <linearGradient id="bodyShade" x1="0%" y1="0%" x2="100%" y2="0%">
                                    <stop offset="0%" stop-color="#000000" stop-opacity="0.2"/>
                                    <stop offset="25%" stop-color="#ffffff" stop-opacity="0.1"/>
                                    <stop offset="75%" stop-color="#ffffff" stop-opacity="0.1"/>
                                    <stop offset="100%" stop-color="#000000" stop-opacity="0.2"/>
                                </linearGradient>
                            </defs>

                            <!-- Sleeves -->
                            <!-- Left Sleeve -->
                            <path id="leftSleeve" d="M 120 70 L 40 130 L 70 170 L 130 120 Z" fill="var(--color-primary, #1e3a8a)" stroke="#0f172a" stroke-width="2"/>
                            <!-- Right Sleeve -->
                            <path id="rightSleeve" d="M 280 70 L 360 130 L 330 170 L 270 120 Z" fill="var(--color-primary, #1e3a8a)" stroke="#0f172a" stroke-width="2"/>
                            
                            <!-- Sleeve Cuffs -->
                            <path id="leftCuff" d="M 40 130 L 48 140 L 78 178 L 70 170 Z" fill="var(--color-accent, #eab308)"/>
                            <path id="rightCuff" d="M 360 130 L 352 140 L 322 178 L 330 170 Z" fill="var(--color-accent, #eab308)"/>

                            <!-- Main Body -->
                            <path id="jerseyBody" d="M 120 70 Q 200 85 280 70 L 275 390 L 125 390 Z" fill="var(--color-primary, #1e3a8a)" stroke="#0f172a" stroke-width="2.5"/>
                            
                            <!-- Pattern Overlay Layer -->
                            <path id="jerseyPattern" d="M 120 70 Q 200 85 280 70 L 275 390 L 125 390 Z" fill="none" opacity="0.9"/>

                            <!-- Shading Overlay -->
                            <path d="M 120 70 Q 200 85 280 70 L 275 390 L 125 390 Z" fill="url(#bodyShade)" pointer-events="none"/>

                            <!-- Collar (V-neck / Crew) -->
                            <path id="jerseyCollar" d="M 160 72 Q 200 115 240 72 Q 200 90 160 72 Z" fill="var(--color-accent, #eab308)" stroke="#0f172a" stroke-width="1.5"/>

                            <!-- Club Crest (Chest Left) -->
                            <circle cx="170" cy="140" r="18" fill="#ffffff" stroke="var(--color-accent, #eab308)" stroke-width="2"/>
                            <text x="170" y="145" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="800" text-anchor="middle" fill="#1e3a8a">CLUB</text>

                            <!-- Italsport Technical Logo (Chest Right) -->
                            <text x="235" y="144" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="900" text-anchor="middle" fill="var(--color-accent, #eab308)" letter-spacing="1">ITALSPORT</text>

                            <!-- Sponsor Chest Area -->
                            <rect id="sponsorBg" x="150" y="210" width="100" height="36" rx="6" fill="rgba(15, 23, 42, 0.75)"/>
                            <text id="sponsorText" x="200" y="233" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="800" text-anchor="middle" fill="#ffffff" letter-spacing="1">MY ITALSPORT</text>

                            <!-- Bottom Hem Badge -->
                            <rect x="235" y="365" width="28" height="14" rx="2" fill="var(--color-accent, #eab308)"/>
                            <text x="249" y="375" font-family="sans-serif" font-size="7" font-weight="700" text-anchor="middle" fill="#0f172a">OFFICIAL</text>
                        </svg>

                    </div>

                    <!-- Rotation Controls -->
                    <div class="rotation-toolbar">
                        <button class="tool-btn" onclick="rotateJersey(-25)"><i class="fa-solid fa-arrow-rotate-left"></i> Ruota Sinistra</button>
                        <button class="tool-btn" onclick="resetRotation()"><i class="fa-solid fa-crosshairs"></i> Vista Frontale</button>
                        <button class="tool-btn" onclick="rotateJersey(25)"><i class="fa-solid fa-arrow-rotate-right"></i> Ruota Destra</button>
                    </div>
                </div>

                <!-- Customization Controls -->
                <div class="controls-panel">
                    
                    <!-- Color Primary -->
                    <div class="control-group">
                        <h4>1. Colore Primario (Base)</h4>
                        <div class="color-swatches" id="primarySwatches">
                            <div class="swatch active" style="background: #1e3a8a;" onclick="setPrimaryColor('#1e3a8a', this)" title="Navy Blue"></div>
                            <div class="swatch" style="background: #0284c7;" onclick="setPrimaryColor('#0284c7', this)" title="Royal Blue"></div>
                            <div class="swatch" style="background: #991b1b;" onclick="setPrimaryColor('#991b1b', this)" title="Rosso Granata"></div>
                            <div class="swatch" style="background: #059669;" onclick="setPrimaryColor('#059669', this)" title="Verde Smeraldo"></div>
                            <div class="swatch" style="background: #eab308;" onclick="setPrimaryColor('#eab308', this)" title="Giallo Oro"></div>
                            <div class="swatch" style="background: #ffffff;" onclick="setPrimaryColor('#ffffff', this)" title="Bianco"></div>
                            <div class="swatch" style="background: #0f172a;" onclick="setPrimaryColor('#0f172a', this)" title="Nero Antracite"></div>
                        </div>
                    </div>

                    <!-- Color Accent -->
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

                    <!-- Pattern Selection -->
                    <div class="control-group">
                        <h4>3. Pattern Sublimatico</h4>
                        <div class="pattern-options">
                            <button class="opt-btn active" onclick="setPattern('solid', this)">Tinta Unita</button>
                            <button class="opt-btn" onclick="setPattern('stripes', this)">Strisce Verticali</button>
                            <button class="opt-btn" onclick="setPattern('chevron', this)">Geometrico Tech</button>
                        </div>
                    </div>

                    <!-- Collar Style -->
                    <div class="control-group">
                        <h4>4. Tipologia Colletto</h4>
                        <div class="collar-options">
                            <button class="opt-btn active" onclick="setCollar('vneck', this)">Collo a V</button>
                            <button class="opt-btn" onclick="setCollar('crew', this)">Girocollo</button>
                            <button class="opt-btn" onclick="setCollar('polo', this)">Collo Polo</button>
                        </div>
                    </div>

                    <!-- Sponsor Text -->
                    <div class="control-group">
                        <h4>5. Testo Sponsor Petto</h4>
                        <input type="text" id="customSponsorInput" value="MY ITALSPORT" oninput="updateSponsorText(this.value)" style="width: 100%; padding: 8px 12px; border: 1px solid var(--border-color); border-radius: 6px; font-weight: 600; font-size: 13px;">
                    </div>

                    <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 8px; padding: 10px 12px; font-size: 11.5px; color: #166534;">
                        <i class="fa-solid fa-check-circle"></i> <b>Produzione 100% Interna:</b> questa grafica viene acquisita direttamente dal reparto CAD Italsport per la calandra a sublimazione.
                    </div>

                </div>
            </div>
        </div>
    </div>

    <!-- TAB 3: DEDICATED CLUB STOREFRONT (MY ITALSPORT) -->
    <div id="tab-storefront" class="tab-content">
        <div class="club-storefront">
            <div class="store-header">
                <div class="store-club-info">
                    <div class="club-crest-box">
                        <i class="fa-solid fa-shield-halved"></i>
                    </div>
                    <div>
                        <div style="font-size: 11px; text-transform: uppercase; color: #93c5fd; font-weight: 700; letter-spacing: 1px;">
                            PORTALE UFFICIALE MY ITALSPORT • STORE RISERVATO
                        </div>
                        <h2 style="font-size: 20px; font-weight: 800; margin: 0;">A.S.D. CALCIO SICILIA 2026/2027</h2>
                        <div style="font-size: 12.5px; color: #bfdbfe;">Vetrina riservata a dirigenti, tesserati e famiglie per ordinare kit ufficiali e merch</div>
                    </div>
                </div>
                <div style="text-align: right;">
                    <span class="pill-badge" style="background: #ffffff; color: #1e3a8a; font-weight: 800;">ZERO GESTIONE CONTANTI</span>
                </div>
            </div>

            <!-- Notice bar explaining value for managers -->
            <div style="background: #f0fdf4; border-bottom: 1px solid #bbf7d0; padding: 12px 28px; display: flex; align-items: center; justify-content: space-between; font-size: 12.5px; color: #166534;">
                <div>
                    <i class="fa-solid fa-circle-check"></i> <b>Come funziona:</b> Genitori e atleti scelgono taglia, inseriscono nome e numero e pagano online con carta. Italsport confeziona il kit nominale e lo spedisce!
                </div>
                <span style="font-weight: 700;">store.italsport-group.it/calciosicilia</span>
            </div>

            <div class="store-products-grid">
                
                <!-- Item 1 -->
                <div class="product-item">
                    <div class="product-img-box">
                        <img src="{post2_b64}" alt="Kit Gara">
                    </div>
                    <div class="product-info">
                        <div>
                            <h5>Kit Gara Ufficiale 2026/27</h5>
                            <div style="font-size: 11px; color: #64748b; margin-bottom: 8px;">Maglia sublimata + pantaloncino con stemma HD</div>
                        </div>
                        <div>
                            <div class="price">€ 48,00</div>
                            <button class="btn-buy" style="width: 100%;" onclick="openOrderModal('Kit Gara Ufficiale')"><i class="fa-solid fa-cart-shopping"></i> Personalizza & Ordina</button>
                        </div>
                    </div>
                </div>

                <!-- Item 2 -->
                <div class="product-item">
                    <div class="product-img-box">
                        <img src="{post6_b64}" alt="Tuta Rappresentanza">
                    </div>
                    <div class="product-info">
                        <div>
                            <h5>Tuta Rappresentanza Club</h5>
                            <div style="font-size: 11px; color: #64748b; margin-bottom: 8px;">Giacca microfibra + pantalone con zip laterale</div>
                        </div>
                        <div>
                            <div class="price">€ 59,00</div>
                            <button class="btn-buy" style="width: 100%;" onclick="openOrderModal('Tuta Rappresentanza')"><i class="fa-solid fa-cart-shopping"></i> Scegli Taglia & Ordina</button>
                        </div>
                    </div>
                </div>

                <!-- Item 3 -->
                <div class="product-item">
                    <div class="product-img-box">
                        <img src="{post4_b64}" alt="Giubbotto Termico">
                    </div>
                    <div class="product-info">
                        <div>
                            <h5>Giacca Termica Antivento</h5>
                            <div style="font-size: 11px; color: #64748b; margin-bottom: 8px;">Imbottitura tecnica per trasferte invernali</div>
                        </div>
                        <div>
                            <div class="price">€ 65,00</div>
                            <button class="btn-buy" style="width: 100%;" onclick="openOrderModal('Giacca Termica')"><i class="fa-solid fa-cart-shopping"></i> Scegli Taglia & Ordina</button>
                        </div>
                    </div>
                </div>

                <!-- Item 4 -->
                <div class="product-item">
                    <div class="product-img-box">
                        <img src="{post1_b64}" alt="Zaino Tecnico">
                    </div>
                    <div class="product-info">
                        <div>
                            <h5>Zaino Tecnico con Fondo Scarpe</h5>
                            <div style="font-size: 11px; color: #64748b; margin-bottom: 8px;">Personalizzato con logo società e nome atleta</div>
                        </div>
                        <div>
                            <div class="price">€ 28,00</div>
                            <button class="btn-buy" style="width: 100%;" onclick="openOrderModal('Zaino Tecnico')"><i class="fa-solid fa-cart-shopping"></i> Personalizza & Ordina</button>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </div>

    <!-- TAB 4: PRO-CLUB FIDELITY CARD -->
    <div id="tab-fidelity" class="tab-content">
        <div class="fidelity-card-section">
            <div style="text-align: center; max-width: 680px; margin: 0 auto 25px auto;">
                <span class="pill-badge" style="background: #fef3c7; color: #b45309; margin-bottom: 8px;">CONVENZIONE ESCLUSIVA B2B</span>
                <h2 style="font-size: 24px; font-weight: 800; color: #0f172a;">Programma Stagionale "PRO-CLUB 2026/2027"</h2>
                <p style="font-size: 13.5px; color: #475569;">
                    La Tessera Fedeltà di Italsport trasforma il rapporto con la società sportiva in una solida partnership commerciale a lungo termine.
                </p>
            </div>

            <!-- VIP Card Render -->
            <div class="vip-card-wrap">
                <div class="vip-card-box">
                    <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                        <div>
                            <div style="font-size: 10px; font-weight: 800; letter-spacing: 1.5px; color: #d97706; text-transform: uppercase;">CONVENZIONE UFFICIALE</div>
                            <div style="font-size: 18px; font-weight: 800; letter-spacing: -0.5px;">ITALSPORT PRO-CLUB</div>
                        </div>
                        <div style="background: rgba(217, 119, 6, 0.2); border: 1px solid #d97706; color: #fde68a; font-size: 11px; font-weight: 700; padding: 4px 10px; border-radius: 6px;">
                            VIP PARTNER
                        </div>
                    </div>

                    <div style="display: flex; align-items: center; gap: 15px;">
                        <div style="width: 48px; height: 36px; background: linear-gradient(135deg, #eab308, #ca8a04); border-radius: 6px; border: 1px solid #a16207;"></div>
                        <div style="font-family: monospace; font-size: 20px; letter-spacing: 3px; color: #f1f5f9;">5412 •••• •••• 2026</div>
                    </div>

                    <div style="display: flex; justify-content: space-between; align-items: flex-end;">
                        <div>
                            <div style="font-size: 9px; color: #94a3b8; text-transform: uppercase;">SOCIETÀ TITOLARE</div>
                            <div style="font-size: 14px; font-weight: 700; color: #ffffff;">A.S.D. CALCIO SICILIA</div>
                        </div>
                        <div>
                            <div style="font-size: 9px; color: #94a3b8; text-transform: uppercase;">VALIDITÀ ACCORDO</div>
                            <div style="font-size: 14px; font-weight: 700; color: #ffffff;">STAGIONE 2026 / 2027</div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- 4 Concrete Pillars for Managers -->
            <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 15px;">
                <div style="background: #f8fafc; border: 1px solid var(--border-color); border-radius: 12px; padding: 16px;">
                    <div style="font-size: 20px; color: #0284c7; margin-bottom: 8px;"><i class="fa-solid fa-lock"></i></div>
                    <h4 style="font-size: 13px; font-weight: 700; color: #0f172a; margin-bottom: 4px;">Listino Prezzi Bloccato</h4>
                    <p style="font-size: 11.5px; color: #475569; line-height: 1.4;">Costi congelati per 12 mesi senza alcun aumento improvviso durante i campionati.</p>
                </div>
                <div style="background: #f8fafc; border: 1px solid var(--border-color); border-radius: 12px; padding: 16px;">
                    <div style="font-size: 20px; color: #059669; margin-bottom: 8px;"><i class="fa-solid fa-truck-fast"></i></div>
                    <h4 style="font-size: 13px; font-weight: 700; color: #0f172a; margin-bottom: 4px;">Priorità Settembre-Ottobre</h4>
                    <p style="font-size: 11.5px; color: #475569; line-height: 1.4;">Corsia preferenziale negli impianti di stampa nelle settimane cruciali pre-gara.</p>
                </div>
                <div style="background: #f8fafc; border: 1px solid var(--border-color); border-radius: 12px; padding: 16px;">
                    <div style="font-size: 20px; color: #d97706; margin-bottom: 8px;"><i class="fa-solid fa-cart-flatbed"></i></div>
                    <h4 style="font-size: 13px; font-weight: 700; color: #0f172a; margin-bottom: 4px;">Zero Minimi di Riordino</h4>
                    <p style="font-size: 11.5px; color: #475569; line-height: 1.4;">Nuovo tesserato a gennaio? Ristampiamo anche 1 solo capo con la grafica identica.</p>
                </div>
                <div style="background: #f8fafc; border: 1px solid var(--border-color); border-radius: 12px; padding: 16px;">
                    <div style="font-size: 20px; color: #7c3aed; margin-bottom: 8px;"><i class="fa-solid fa-gift"></i></div>
                    <h4 style="font-size: 13px; font-weight: 700; color: #0f172a; margin-bottom: 4px;">Voucher Fine Stagione</h4>
                    <p style="font-size: 11.5px; color: #475569; line-height: 1.4;">Credito spesa riaccreditato al club calcolato sul volume complessivo ordinato.</p>
                </div>
            </div>

            <div style="text-align: center; margin-top: 25px;">
                <button class="nav-btn btn-pdf" style="display: inline-flex; padding: 10px 24px; font-size: 14px;" onclick="alert('Modulo di richiesta convenzione Pro-Club generato. L\'agente commerciale Italsport contatterà la società entro 24 ore.')">
                    <i class="fa-solid fa-file-signature"></i> Richiedi Attivazione Convenzione per la Tua Società
                </button>
            </div>
        </div>
    </div>

</div>

<!-- POST DETAIL MODAL -->
<div class="modal-backdrop" id="postModal" onclick="closePostModal(event)">
    <div class="modal-content" onclick="event.stopPropagation()">
        <button class="modal-close" onclick="closePostModalDirect()"><i class="fa-solid fa-xmark"></i></button>
        
        <div class="modal-img-col">
            <img id="modalImg" src="" alt="Post Visual">
        </div>

        <div class="modal-info-col">
            <div>
                <!-- Header -->
                <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 12px; padding-bottom: 10px; border-bottom: 1px solid var(--border-color);">
                    <img src="{logo_b64}" style="height: 28px; width: 28px; border-radius: 50%; object-fit: contain; border: 1px solid var(--border-color);" alt="avatar">
                    <div>
                        <div style="font-size: 13px; font-weight: 700; color: #0f172a;">italsport_group</div>
                        <div style="font-size: 11px; color: #64748b;" id="modalPostMeta">Palermo, Italia • Sponsorizzato B2B</div>
                    </div>
                </div>

                <!-- Badge -->
                <div style="margin-bottom: 10px;">
                    <span class="pill-badge" id="modalPostBadge" style="background: #e0f2fe; color: #0369a1; font-size: 11px;">POST 01</span>
                </div>

                <!-- Caption -->
                <div style="font-size: 13px; line-height: 1.5; color: #334155; margin-bottom: 14px;" id="modalPostCaption">
                    <!-- Text inserted via JS -->
                </div>

                <!-- Strategic Target Note -->
                <div style="background: #f8fafc; border: 1px solid var(--border-color); border-radius: 8px; padding: 10px; font-size: 11px; color: #475569; margin-bottom: 15px;">
                    <b style="color: #0284c7;">🎯 OBIETTIVO STRATEGICO:</b> <span id="modalPostGoal">Brand Authority</span>
                </div>
            </div>

            <!-- Bottom Action -->
            <div style="border-top: 1px solid var(--border-color); padding-top: 12px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <div style="display: flex; gap: 15px; font-size: 18px; color: #334155;">
                        <i class="fa-regular fa-heart" style="cursor: pointer;"></i>
                        <i class="fa-regular fa-comment" style="cursor: pointer;"></i>
                        <i class="fa-regular fa-paper-plane" style="cursor: pointer;"></i>
                    </div>
                    <i class="fa-regular fa-bookmark" style="font-size: 18px; color: #334155; cursor: pointer;"></i>
                </div>
                <div style="font-size: 12px; font-weight: 700; color: #0f172a;" id="modalPostLikes">245 "Mi piace"</div>
                <div style="font-size: 10px; color: #94a3b8; text-transform: uppercase; margin-top: 2px;">Pubblicato recentemente</div>
            </div>
        </div>
    </div>
</div>

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
        // V-Neck
        collar.setAttribute('d', 'M 160 72 Q 200 115 240 72 Q 200 90 160 72 Z');
    }}
}}

function updateSponsorText(text) {{
    document.getElementById('sponsorText').textContent = text.toUpperCase() || 'SPONSOR';
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
        btnText.textContent = 'Rotazione Automatica: ON';
        spinInterval = setInterval(() => {{
            rotateJersey(4);
        }}, 60);
    }} else {{
        btnText.textContent = 'Rotazione Automatica: OFF';
        clearInterval(spinInterval);
    }}
}}

// Post Modal Details
const postDetails = {{
    1: {{
        img: '{post1_b64}',
        badge: 'POST 01 • BRAND HERITAGE & MANIFATTURA',
        caption: '<b>italsport_group</b> Dal rotolo di tessuto grezzo al campo da gioco. ✂️⚽<br><br>Nel nostro laboratorio di Palermo non rivendiamo cataloghi: produciamo direttamente con stampanti a sublimazione full-print e calandra a caldo.<br><br>✓ Colori brillanti e indelebili<br>✓ Tessuto traspirante a rapida asciugatura<br>✓ Controllo sartoriale su ogni cucitura<br><br>📍 Vieni a toccare con mano la qualità nel nostro showroom in Via Ugo La Malfa 56, Palermo.<br><br>#Italsport #SartoriaSportiva #MadeInSicily #Sublimazione #CalcioSiciliano',
        goal: 'Costruire autorevolezza dimostrando che Italsport è un produttore reale con 30 anni di esperienza a Palermo.',
        likes: '142 "Mi piace"'
    }},
    2: {{
        img: '{post2_b64}',
        badge: 'POST 02 • INNOVAZIONE TECNOLOGICA 3D',
        caption: '<b>italsport_group</b> Disegna la divisa del tuo club prima di ordinarla! 👕💻<br><br>Con il Configuratore 3D di Italsport vedi la maglia modificabile a 360° in tempo reale:<br>1️⃣ Scegli il modello e i colori societari<br>2️⃣ Applica lo stemma del club e gli sponsor in HD<br>3️⃣ Modifica colletto e dettagli<br><br>🔗 Provalo subito al link in bio o sul nostro sito italsport-group.it!<br><br>#Configuratore3D #DiviseCalcio #AbbigliamentoSportivo #Teamwear',
        goal: 'Stimolare l\'interazione e far testare il configuratore online ai dirigenti sportivi per raccogliere lead profilati.',
        likes: '265 "Mi piace"'
    }},
    3: {{
        img: '{post3_b64}',
        badge: 'POST 03 • PROGRAMMA FEDELTÀ PRO-CLUB',
        caption: '<b>italsport_group</b> Non una semplice fornitura, ma un\'alleanza per tutta la stagione. 🤝🏆<br><br>È attivo il programma <b>PRO-CLUB 2026/2027</b> dedicato alle società sportive:<br>🔒 Listino prezzi bloccato per 12 mesi<br>⚡ Priorità assoluta di produzione prima dell\'inizio campionato<br>📦 Vetrina e-commerce dedicata a costo zero per il club<br>🎁 Voucher riassortimento fine anno in base ai volumi ordinati<br><br>📩 Scrivici in DM per attivare la convenzione della tua società!<br><br>#TesseraFedelta #ProClub #SocietaSportive #FornitureSportive',
        goal: 'Fidelizzare i club e chiudere accordi contrattuali stagionali prima del picco estivo.',
        likes: '198 "Mi piace"'
    }},
    4: {{
        img: '{post4_b64}',
        badge: 'POST 04 • SOLUZIONE LOGISTICA RIASSORTIMENTI',
        caption: '<b>italsport_group</b> Nuovo iscritto a gennaio? La maglia è identica al primo giorno. 🔄⚽<br><br>Uno dei maggiori problemi dei dirigenti è trovare gli stessi kit quando la squadra cresce a stagione in corso.<br>Con Italsport la scheda tecnica del tuo club è archiviata per sempre: ristampiamo anche un singolo capo, senza minimi d\'ordine e con gli stessi colori esatti.<br><br>#ArchivioTecnico #ZeroMinimi #Riassortimenti #CalcioDilettanti',
        goal: 'Risolvere un punto di dolore reale e quotidiano dei direttori sportivi e segretari.',
        likes: '173 "Mi piace"'
    }},
    5: {{
        img: '{post5_b64}',
        badge: 'POST 05 • DIGITALIZZAZIONE & VETRINA SQUADRE',
        caption: '<b>italsport_group</b> Dirigenti: basta raccogliere quote in contanti e gestire fogli Excel! 🛒📲<br><br>Con il portale <b>My Italsport</b> ogni società partner ha la propria vetrina online ufficiale.<br>Genitori e atleti scelgono taglia, personalizzano nome e numero e acquistano direttamente dallo smartphone con pagamento tracciato.<br><br>Zero stress per la segreteria, kit pronti per il campo.<br><br>#MyItalsport #VetrinaOnline #ShopSocieta #DigitalSport',
        goal: 'Spiegare il vantaggio chiave della piattaforma e-commerce proprietaria che azzera il carico di lavoro dei club.',
        likes: '214 "Mi piace"'
    }},
    6: {{
        img: '{post6_b64}',
        badge: 'POST 06 • LINEA TECNICA COMPLETA',
        caption: '<b>italsport_group</b> Dalla prima squadra alla scuola calcio: una sola identità visiva coordinata. ❄️🏃‍♂️<br><br>Scopri la collezione completa per allenamento e rappresentanza:<br>✓ Giacche termiche antivento con fodera traspirante<br>✓ Tute microfibra elasticizzate<br>✓ Polo e bermuda di rappresentanza<br>✓ Zaini e borsoni rinforzati con portascarpe<br><br>Richiedi la campionatura per il consiglio direttivo della tua squadra!<br><br>#LineaTecnica #Teamwear #Allenamento #ItalsportGroup',
        goal: 'Aumentare lo scontrino medio proponendo forniture complete (tute, giubbotti, borse) oltre ai kit gara.',
        likes: '156 "Mi piace"'
    }},
    7: {{
        img: '{post7_b64}',
        badge: 'POST 07 • COMMUNITY & VALORI CONDIVISI',
        caption: '<b>italsport_group</b> Più di un fornitore: scendiamo in campo al vostro fianco. 🏟️🤝<br><br>Oltre 150 società sportive in Sicilia e nel Sud Italia scelgono l\'affidabilità e l\'ascolto di Italsport.<br>Dietro ogni divisa c\'è il sogno di un giovane atleta e la passione di dirigenti che dedicano la propria vita allo sport.<br><br>Grazie a tutti i club che condividono il nostro stesso gioco!<br><br>#ItalsportFamily #PartnerAffidabile #PassioneVera #SportDilettantistico',
        goal: 'Umanizzare il brand e generare riprova sociale mostrando la vastità della community reale.',
        likes: '289 "Mi piace"'
    }}
}};

function openPostModal(id) {{
    const data = postDetails[id];
    if(!data) return;

    document.getElementById('modalImg').src = data.img;
    document.getElementById('modalPostBadge').textContent = data.badge;
    document.getElementById('modalPostCaption').innerHTML = data.caption;
    document.getElementById('modalPostGoal').textContent = data.goal;
    document.getElementById('modalPostLikes').textContent = data.likes;

    document.getElementById('postModal').classList.add('active');
}}

function closePostModal(e) {{
    if(e.target === document.getElementById('postModal')) {{
        document.getElementById('postModal').classList.remove('active');
    }}
}}

function closePostModalDirect() {{
    document.getElementById('postModal').classList.remove('active');
}}

function openOrderModal(prodName) {{
    alert(`Aperto selettore rapido per "${{prodName}}":\\n1. Selezione Taglia (XS, S, M, L, XL)\\n2. Inserimento Nome Atleta e Numero Maglia\\n3. Pagamento con Carta/PayPal\\n\\nQuesto è esattamente il flusso d'acquisto su store.italsport-group.it per le famiglie.`);
}}
</script>

</body>
</html>
"""

with open("Instagram_Mockup_Italsport.html", "w", encoding="utf-8") as f:
    f.write(html_mockup)

print(f"Instagram_Mockup_Italsport.html written successfully ({len(html_mockup)} bytes).")
