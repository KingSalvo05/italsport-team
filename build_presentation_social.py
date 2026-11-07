import os, base64, subprocess, pymupdf

def get_b64(fname):
    if os.path.exists(fname):
        with open(fname, 'rb') as f:
            b64 = base64.b64encode(f.read()).decode('utf-8')
            ext = 'png' if fname.endswith('.png') else 'jpeg'
            return f"data:image/{ext};base64,{b64}"
    return ""

print("Encoding real Italsport Ciserano (BG) images for Social Presentation...")
logo_b64 = get_b64("cropped-cropped-italsportlogo.png")
post1_b64 = get_b64("img_post1_jersey.jpg")
post2_b64 = get_b64("img_post2_3d.jpg")
post3_b64 = get_b64("img_post3_fidelity.jpg")
post4_b64 = get_b64("img_post4_stack.jpg")
post5_b64 = get_b64("img_post5_portal.jpg")
post6_b64 = get_b64("img_post6_winter.jpg")
post7_b64 = get_b64("img_post7_celebration.jpg")

card_real_b64 = get_b64("card_proclub_real.jpg")
shw_b64 = get_b64("real_showroom_ciserano.jpg")
man_b64 = get_b64("real_manichini_ciserano.jpg")

html = f"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<title>Italsport Group Ciserano (BG) - Piano Strategico Social & Vetrina Squadre 2026</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap');

@page {{
    size: 297mm 167.0625mm;
    margin: 0;
}}

* {{
    box-sizing: border-box;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
}}

html, body {{
    margin: 0;
    padding: 0;
    background: #0f172a;
    font-family: 'Plus Jakarta Sans', 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    color: #0f172a;
    -webkit-font-smoothing: antialiased;
}}

.slide {{
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
}}

/* Slide Header */
.slide-header {{
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    padding-bottom: 7px;
    border-bottom: 1.5px solid #e2e8f0;
    margin-bottom: 8px;
    flex-shrink: 0;
}}

.header-left {{
    display: flex;
    align-items: center;
    gap: 14px;
}}

.header-logo {{
    height: 38px;
    width: auto;
    object-fit: contain;
}}

.header-title-box {{
    display: flex;
    flex-direction: column;
}}

.category-tag {{
    font-size: 8.5px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    color: #0284c7;
    margin-bottom: 1px;
}}

.slide-title {{
    font-size: 17px;
    font-weight: 800;
    color: #0f172a;
    margin: 0;
    line-height: 1.2;
    letter-spacing: -0.2px;
}}

.slide-subtitle {{
    font-size: 10px;
    color: #475569;
    margin: 2px 0 0 0;
    font-weight: 500;
}}

.chapter-badge {{
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
}}

/* Slide Body */
.slide-body {{
    flex-grow: 1;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 8px;
    min-height: 0;
    margin: 2px 0;
}}

/* Slide Footer */
.slide-footer {{
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
}}

.footer-left {{
    display: flex;
    align-items: center;
    gap: 8px;
}}

.footer-pill {{
    background: #e0f2fe;
    color: #0369a1;
    padding: 2px 8px;
    border-radius: 4px;
    font-weight: 700;
    font-size: 8px;
}}

.slide-num {{
    background: #f1f5f9;
    border: 1px solid #cbd5e1;
    padding: 2px 8px;
    border-radius: 4px;
    color: #0f172a;
    font-weight: 700;
}}

/* Utility Cards & Grids */
.card {{
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 11px 13px;
}}

.card-white {{
    background: #ffffff;
    border: 1px solid #cbd5e1;
    border-radius: 8px;
    padding: 11px 13px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.03);
}}

.card-blue {{
    background: #f0f7ff;
    border: 1px solid #bfdbfe;
    border-radius: 8px;
    padding: 11px 13px;
}}

.card-green {{
    background: #f0fdf4;
    border: 1px solid #bbf7d0;
    border-radius: 8px;
    padding: 11px 13px;
}}

.card-gold {{
    background: #fffbeb;
    border: 1px solid #fde68a;
    border-radius: 8px;
    padding: 11px 13px;
}}

.grid-2 {{ display: grid; grid-template-columns: 1fr 1fr; gap: 11px; }}
.grid-3 {{ display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 11px; }}
.grid-4 {{ display: grid; grid-template-columns: 1fr 1fr 1fr 1fr; gap: 9px; }}
.grid-2-3 {{ display: grid; grid-template-columns: 2fr 3fr; gap: 12px; }}
.grid-3-2 {{ display: grid; grid-template-columns: 3fr 2fr; gap: 12px; }}
.grid-1-2 {{ display: grid; grid-template-columns: 1fr 2fr; gap: 12px; }}

.pill {{
    display: inline-block;
    padding: 2px 7px;
    border-radius: 4px;
    font-size: 8px;
    font-weight: 700;
    text-transform: uppercase;
}}
.pill-blue {{ background: #e0f2fe; color: #0284c7; }}
.pill-green {{ background: #dcfce7; color: #16a34a; }}
.pill-gold {{ background: #fef3c7; color: #d97706; }}
.pill-purple {{ background: #f3e8ff; color: #9333ea; }}
.pill-slate {{ background: #f1f5f9; color: #475569; }}

.stat-box {{
    background: #ffffff;
    border: 1px solid #cbd5e1;
    border-radius: 7px;
    padding: 8px 10px;
    text-align: center;
    box-shadow: 0 1px 2px rgba(0,0,0,0.02);
}}
.stat-val {{
    font-size: 17px;
    font-weight: 800;
    color: #0284c7;
    line-height: 1.1;
}}
.stat-lbl {{
    font-size: 8px;
    color: #64748b;
    font-weight: 600;
    text-transform: uppercase;
    margin-top: 2px;
}}

/* Tables */
table.deck-table {{
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    font-size: 9.5px;
    border: 1px solid #cbd5e1;
    border-radius: 7px;
    overflow: hidden;
}}
table.deck-table th {{
    background: #f1f5f9;
    color: #0f172a;
    font-weight: 700;
    padding: 6.5px 8px;
    text-align: left;
    border-bottom: 1px solid #cbd5e1;
    font-size: 9px;
    text-transform: uppercase;
    letter-spacing: 0.4px;
}}
table.deck-table td {{
    padding: 6px 8px;
    border-bottom: 1px solid #e2e8f0;
    color: #334155;
    vertical-align: middle;
}}
table.deck-table tr:last-child td {{
    border-bottom: none;
}}
table.deck-table tr:nth-child(even) td {{
    background: #f8fafc;
}}

/* Post Cards */
.post-deck-card {{
    background: #ffffff;
    border: 1px solid #cbd5e1;
    border-radius: 8px;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    box-shadow: 0 1px 3px rgba(0,0,0,0.03);
}}
.post-deck-img {{
    width: 100%;
    aspect-ratio: 1;
    object-fit: cover;
    display: block;
    border-bottom: 1px solid #e2e8f0;
}}
.post-deck-body {{
    padding: 7px 9px;
    display: flex;
    flex-direction: column;
    gap: 3px;
    flex-grow: 1;
}}
.post-deck-title {{
    font-size: 10.5px;
    font-weight: 800;
    color: #0f172a;
    line-height: 1.2;
}}
.post-deck-copy {{
    font-size: 8.5px;
    color: #475569;
    line-height: 1.35;
    margin: 0;
}}
.post-deck-tag {{
    font-size: 7.5px;
    color: #0284c7;
    font-weight: 600;
}}
</style>
</head>
<body>

<!-- SLIDE 1: COVER (LIGHT CORPORATE EXECUTIVE PALETTE) -->
<div class="slide" style="background: linear-gradient(135deg, #ffffff 0%, #f0f9ff 60%, #f0fdf4 100%); color: #0f172a; border-top: 6px solid #0284c7;">
    <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1.5px solid #cbd5e1; padding-bottom: 10px;">
        <div style="display: inline-flex; align-items: center; gap: 12px;">
            <img src="{logo_b64}" style="height: 42px; width: auto;" alt="Italsport Logo">
            <span style="font-size: 10px; font-weight: 800; color: #0284c7; background: #e0f2fe; padding: 4px 10px; border-radius: 6px;">CISERANO — ZINGONIA (BG) • DAL 1995</span>
        </div>
        <div style="display: flex; gap: 8px;">
            <span style="background: #f1f5f9; border: 1px solid #cbd5e1; color: #334155; font-size: 9px; font-weight: 700; padding: 4px 10px; border-radius: 5px; text-transform: uppercase;">PIANO SOCIAL & VETRINA SQUADRE 2026</span>
            <span style="background: #0284c7; color: #ffffff; font-size: 9px; font-weight: 700; padding: 4px 10px; border-radius: 5px; text-transform: uppercase;">@ITALSPORTGROUP</span>
        </div>
    </div>

    <div style="display: flex; flex-direction: column; gap: 12px; margin: 12px 0;">
        <div style="font-size: 11px; font-weight: 800; color: #0369a1; text-transform: uppercase; letter-spacing: 1.2px;">
            ITALSPORT GROUP (Italsport di Locatelli Vincenzo) • VIA PROVINCIALE FRANCESCA 2H/I, CISERANO (BG)
        </div>
        <h1 style="font-size: 31px; font-weight: 800; line-height: 1.15; margin: 0; color: #0f172a; letter-spacing: -0.5px;">
            STRATEGIA SOCIAL INSTAGRAM &<br>VALORIZZAZIONE VETRINA SQUADRE "MY ITALSPORT"
        </h1>
        <p style="font-size: 12px; color: #334155; max-width: 890px; margin: 0; line-height: 1.45;">
            Piano editoriale basato esclusivamente sulle <b>vere foto di @italsportgroup e italsport-group.it</b> per promuovere i tre punti di forza distintivi dell'azienda: la <b>Vetrina Dedicata con Password per ogni squadra</b>, il <b>Configuratore 3D a 360°</b> e la <b>Tessera Pro-Club</b>.
        </p>

        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px; margin-top: 8px;">
            <div class="card-white" style="border-top: 3.5px solid #10b981;">
                <span class="pill pill-green" style="margin-bottom: 4px;">ASSET 01 • FOCUS</span>
                <div style="font-size: 12px; font-weight: 800; color: #0f172a;">Vetrina Squadra con Password</div>
                <div style="font-size: 9px; color: #475569; margin-top: 2px;">Ogni squadra entra con una <b>password dedicata</b> e vede <b>solo le cose relative alla sua società</b>, trovando sempre gli stessi capi senza errori.</div>
            </div>
            <div class="card-white" style="border-top: 3.5px solid #0284c7;">
                <span class="pill pill-blue" style="margin-bottom: 4px;">ASSET 02</span>
                <div style="font-size: 12px; font-weight: 800; color: #0f172a;">Configuratore 3D a 360°</div>
                <div style="font-size: 9px; color: #475569; margin-top: 2px;">Disegna la divisa sul sito scegliendo modello, colori, colletto e sponsor con <b>rotazione 3D a 360°</b> prima di ordinarla.</div>
            </div>
            <div class="card-white" style="border-top: 3.5px solid #f59e0b;">
                <span class="pill pill-gold" style="margin-bottom: 4px;">ASSET 03</span>
                <div style="font-size: 12px; font-weight: 800; color: #0f172a;">Tessera Pro-Club (4 Livelli)</div>
                <div style="font-size: 9px; color: #475569; margin-top: 2px;">Livelli Basic, Silver, Gold e Diamond: <b>Italsport fa da magazzino a Ciserano</b> (zero anticipi per il club), listino riservato e continuità negli anni.</div>
            </div>
        </div>
    </div>

    <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #cbd5e1; padding-top: 8px; font-size: 8.5px; color: #475569;">
        <div><b>SEDE & SHOWROOM:</b> Via Provinciale Francesca 2H/I, 24040 Ciserano — Loc. Zingonia (BG)</div>
        <div><b>CONTATTI:</b> Tel. 035 4191221 • Cell. 335 7001956 • info@italsport-group.it</div>
        <div><b>P.IVA:</b> 01778490167</div>
        <div><span class="slide-num">SLIDE 01 / 12</span></div>
    </div>
</div>

<!-- SLIDE 2: EXECUTIVE SUMMARY -->
<div class="slide">
    <div class="slide-header">
        <div class="header-left">
            <img src="{logo_b64}" class="header-logo" alt="Italsport Logo">
            <div class="header-title-box">
                <span class="category-tag">CONTESTO AZIENDALE & VISIONE</span>
                <h2 class="slide-title">30 Anni di Forniture Sportive a Ciserano (BG) e in Lombardia</h2>
                <p class="slide-subtitle">Valorizzare su Instagram il patrimonio reale di Italsport: oltre 4.600 realtà nel CRM e servizi su misura per le società sportive.</p>
            </div>
        </div>
        <div class="header-right">
            <span class="chapter-badge">CAPITOLO 01 | IDENTITÀ</span>
        </div>
    </div>

    <div class="slide-body">
        <div class="grid-2-3" style="align-items: stretch;">
            <div class="card-blue" style="display: flex; flex-direction: column; justify-content: space-between; padding: 14px 16px;">
                <div>
                    <span class="pill pill-blue">LA FORZA DI ITALSPORT GROUP</span>
                    <h3 style="font-size: 13px; font-weight: 800; color: #0c4a6e; margin: 6px 0 8px 0;">Più di un Fornitore: Il Partner Tecnico del Club</h3>
                    <p style="font-size: 9.5px; color: #334155; line-height: 1.45; margin: 0;">
                        Attiva dal 1995 a Ciserano — Zingonia (BG), Italsport serve società sportive (calcio, volley, basket, rugby, atletica), oratori, scuole, comuni e aziende. L'obiettivo del piano social non è pubblicare foto generiche, ma far conoscere i servizi esclusivi che tolgono ogni problema organizzativo ai direttivi.
                    </p>
                </div>
                <div style="border-top: 1.5px solid #bfdbfe; padding-top: 8px; margin-top: 10px;">
                    <div style="font-size: 9px; font-weight: 800; color: #0369a1;">PERCHÉ LE SOCIETÀ SCELGONO ITALSPORT:</div>
                    <div style="font-size: 8.5px; color: #475569; margin-top: 2px;">Disponibilità immediata (magazzino a Ciserano), Vetrina riservata con password, Configuratore 3D e continuità garantita negli anni.</div>
                </div>
            </div>

            <div style="display: flex; flex-direction: column; gap: 8px; justify-content: space-between;">
                <div class="card-white" style="padding: 11px 14px;">
                    <div style="display: flex; align-items: center; gap: 10px;">
                        <span style="background: #dcfce7; color: #16a34a; width: 26px; height: 26px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 11px; flex-shrink: 0;">1</span>
                        <div>
                            <div style="font-size: 11px; font-weight: 800; color: #0f172a;">Vetrina Dedicata con Password per Ogni Squadra</div>
                            <div style="font-size: 8.5px; color: #475569; margin-top: 2px;">Ogni squadra accede con la sua password su `store.italsport-group.it` e vede <b>solo i propri capi ufficiali</b>, ritrovando sempre le stesse cose nel tempo senza errori.</div>
                        </div>
                    </div>
                </div>
                <div class="card-white" style="padding: 11px 14px;">
                    <div style="display: flex; align-items: center; gap: 10px;">
                        <span style="background: #e0f2fe; color: #0284c7; width: 26px; height: 26px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 11px; flex-shrink: 0;">2</span>
                        <div>
                            <div style="font-size: 11px; font-weight: 800; color: #0f172a;">Configuratore 3D con Maglia Ruotabile a 360°</div>
                            <div style="font-size: 8.5px; color: #475569; margin-top: 2px;">Sul sito `italsport-group.it` il direttivo personalizza colori, colletto e sponsor vedendo la divisa 3D girare a 360° prima di confermare l'ordine.</div>
                        </div>
                    </div>
                </div>
                <div class="card-white" style="padding: 11px 14px;">
                    <div style="display: flex; align-items: center; gap: 10px;">
                        <span style="background: #fef3c7; color: #d97706; width: 26px; height: 26px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 11px; flex-shrink: 0;">3</span>
                        <div>
                            <div style="font-size: 11px; font-weight: 800; color: #0f172a;">Tessera Pro-Club (Basic, Silver, Gold, Diamond)</div>
                            <div style="font-size: 8.5px; color: #475569; margin-top: 2px;">Facciamo noi il magazzino a Ciserano per la società (zero anticipi e zero rimanenze), con listino bloccato e riassortimenti sempre disponibili.</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="grid-4" style="margin-top: 4px;">
            <div class="stat-box">
                <div class="stat-val">30+ ANNI</div>
                <div class="stat-lbl">Attività a Ciserano (Dal 1995)</div>
            </div>
            <div class="stat-box">
                <div class="stat-val">4.600+</div>
                <div class="stat-lbl">Società, Scuole e Aziende in CRM</div>
            </div>
            <div class="stat-box">
                <div class="stat-val">2.600</div>
                <div class="stat-lbl">Articoli Attivi a Magazzino</div>
            </div>
            <div class="stat-box">
                <div class="stat-val">4 LIVELLI</div>
                <div class="stat-lbl">Card Pro-Club (Basic..Diamond)</div>
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <div class="footer-left">
            <span class="footer-pill">ITALSPORT GROUP — CISERANO (BG)</span>
            <span>PIANO STRATEGICO SOCIAL & VETRINA SQUADRE 2026</span>
        </div>
        <div>CAPITOLO 01: IDENTITÀ & NUMERI CHIAVE</div>
        <div class="slide-num">Slide 02 / 12</div>
    </div>
</div>

<!-- SLIDE 3: COMPETITIVE POSITIONING -->
<div class="slide">
    <div class="slide-header">
        <div class="header-left">
            <img src="{logo_b64}" class="header-logo" alt="Italsport Logo">
            <div class="header-title-box">
                <span class="category-tag">POSIZIONAMENTO SUL MERCATO</span>
                <h2 class="slide-title">Perché Scegliere Italsport Rispetto ai Cataloghi Generici</h2>
                <p class="slide-subtitle">Come risolviamo i problemi reali delle società sportive di Bergamo e della Lombardia.</p>
            </div>
        </div>
        <div class="header-right">
            <span class="chapter-badge">CAPITOLO 01 | VANTAGGI</span>
        </div>
    </div>

    <div class="slide-body">
        <table class="deck-table">
            <thead>
                <tr>
                    <th style="width: 22%;">Esigenza della Società</th>
                    <th style="width: 38%;">Fornitori Tradizionali / Cataloghi Standard</th>
                    <th style="width: 40%; background: #e0f2fe; color: #0369a1;">ITALSPORT GROUP — CISERANO (BG)</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><b>Vetrina Dedicata della Squadra</b></td>
                    <td>Cataloghi dispersivi con migliaia di articoli dove si rischia di ordinare il modello o il colore sbagliato.</td>
                    <td style="background: #f0f7ff;"><b>Vetrina con Password (My Italsport):</b> ogni squadra accede con la sua password e vede <b>SOLO le cose relative alla sua squadra</b>, trovando sempre gli stessi capi senza problemi.</td>
                </tr>
                <tr>
                    <td><b>Continuità negli Anni</b></td>
                    <td>Linee che vanno fuori produzione l'anno dopo; difficoltà a vestire i nuovi iscritti a metà stagione.</td>
                    <td style="background: #f0f7ff;"><b>Continuità Garantita:</b> la linea della squadra (Kit Gara, Tuta Rom, Giacca Scotland, Giubbotto Nepal, K-Way, Borsa) resta sempre riordinabile identica.</td>
                </tr>
                <tr>
                    <td><b>Gestione Magazzino & Costi</b></td>
                    <td>Il club deve anticipare migliaia di euro e tenere scatoloni di taglie invendute in segreteria.</td>
                    <td style="background: #f0f7ff;"><b>Magazzino Gestito da Italsport a Ciserano:</b> teniamo noi le scorte per la società, zero anticipi finanziari e zero rimanenze per il club.</td>
                </tr>
                <tr>
                    <td><b>Progettazione & Condizioni</b></td>
                    <td>Nessuna anteprima 3D; listini variabili senza premialità per i club storici.</td>
                    <td style="background: #f0f7ff;"><b>Configuratore 3D a 360° + Tessera Pro-Club:</b> 4 livelli (Basic, Silver, Gold, Diamond) con listino riservato e sconti dedicati.</td>
                </tr>
            </tbody>
        </table>

        <div class="grid-2" style="margin-top: 4px;">
            <div class="card" style="border-left: 4px solid #ef4444; padding: 10px 13px;">
                <div style="font-size: 9.5px; font-weight: 800; color: #b91c1c;">COSA EVITARE SUI SOCIAL:</div>
                <div style="font-size: 8.5px; color: #475569; line-height: 1.4; margin-top: 3px;">
                    Evitare foto prese a caso da internet o testi esagerati: chi segue `@italsportgroup` vuole vedere i veri capi, il vero showroom di Ciserano e capire subito i vantaggi pratici per la propria squadra.
                </div>
            </div>
            <div class="card" style="border-left: 4px solid #10b981; padding: 10px 13px;">
                <div style="font-size: 9.5px; font-weight: 800; color: #047857;">LA LINEA DEL NUOVO PIANO:</div>
                <div style="font-size: 8.5px; color: #475569; line-height: 1.4; margin-top: 3px;">
                    Foto 100% reali di `@italsportgroup` e `italsport-group.it`, impaginazione pulita senza scritte sovrapposte e focus chiaro su <b>Vetrina con Password</b>, <b>Configuratore 3D</b> e <b>Tessera Pro-Club</b>.
                </div>
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <div class="footer-left">
            <span class="footer-pill">ITALSPORT GROUP — CISERANO (BG)</span>
            <span>PIANO STRATEGICO SOCIAL & VETRINA SQUADRE 2026</span>
        </div>
        <div>CAPITOLO 01: VANTAGGI PER LE SOCIETÀ SPORTIVE</div>
        <div class="slide-num">Slide 03 / 12</div>
    </div>
</div>

<!-- SLIDE 4: THE 3 CORE PILLARS (WITH REAL IMAGES) -->
<div class="slide">
    <div class="slide-header">
        <div class="header-left">
            <img src="{logo_b64}" class="header-logo" alt="Italsport Logo">
            <div class="header-title-box">
                <span class="category-tag">I 3 PILASTRI DA VALORIZZARE</span>
                <h2 class="slide-title">Vetrina con Password, Configuratore 3D a 360° e Tessera Pro-Club</h2>
                <p class="slide-subtitle">I tre servizi esclusivi di Italsport rappresentati con le vere grafiche e foto del sito ufficiale.</p>
            </div>
        </div>
        <div class="header-right">
            <span class="chapter-badge">CAPITOLO 02 | I 3 PILASTRI</span>
        </div>
    </div>

    <div class="slide-body">
        <div class="grid-3" style="align-items: stretch;">
            <!-- PILLAR 1: VETRINA CON PASSWORD -->
            <div class="card-white" style="border-top: 3.5px solid #10b981; display: flex; flex-direction: column; justify-content: space-between; padding: 10px 12px;">
                <div>
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 5px;">
                        <span class="pill pill-green">PILASTRO 01 • FOCUS</span>
                        <span style="font-size: 8.5px; font-weight: 700; color: #16a34a;">PASSWORD CLUB</span>
                    </div>
                    <img src="{post4_b64}" style="width: 100%; height: 82px; object-fit: cover; object-position: top; border-radius: 5px; border: 1px solid #e2e8f0; margin-bottom: 6px;" alt="Vetrina con Password">
                    <div style="font-size: 11.5px; font-weight: 800; color: #0f172a; margin-bottom: 3px;">Vetrina Squadra con Password</div>
                    <p style="font-size: 8.5px; color: #475569; line-height: 1.35; margin: 0 0 6px 0;">
                        Ogni squadra ha una vetrina dedicata a sé dove accede con una <b>password riservata</b> e vede <b>solo le cose relative alla sua squadra</b>.
                    </p>
                </div>
                <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 5px; padding: 5px 7px; font-size: 8px;">
                    <b style="color: #16a34a;">CERTEZZA:</b> Chi entra trova sicuramente sempre le stesse cose nel tempo senza errori o confusione.
                </div>
            </div>

            <!-- PILLAR 2: CONFIGURATORE 3D -->
            <div class="card-white" style="border-top: 3.5px solid #0284c7; display: flex; flex-direction: column; justify-content: space-between; padding: 10px 12px;">
                <div>
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 5px;">
                        <span class="pill pill-blue">PILASTRO 02</span>
                        <span style="font-size: 8.5px; font-weight: 700; color: #0284c7;">ROTAZIONE 360°</span>
                    </div>
                    <img src="{post3_b64}" style="width: 100%; height: 82px; object-fit: cover; object-position: top; border-radius: 5px; border: 1px solid #e2e8f0; margin-bottom: 6px;" alt="Configuratore 3D">
                    <div style="font-size: 11.5px; font-weight: 800; color: #0f172a; margin-bottom: 3px;">Simulatore Maglia 3D a 360°</div>
                    <p style="font-size: 8.5px; color: #475569; line-height: 1.35; margin: 0 0 6px 0;">
                        Sul sito `italsport-group.it` si sceglie modello, colori, colletto, numeri e sponsor e si vede la maglia 3D ruotare a 360° fronte e retro.
                    </p>
                </div>
                <div style="background: #f0f7ff; border: 1px solid #bfdbfe; border-radius: 5px; padding: 5px 7px; font-size: 8px;">
                    <b style="color: #0284c7;">INTERATTIVO:</b> Nel mockup abbiamo integrato sia la vera animazione 3D a 360° del sito sia il simulatore live.
                </div>
            </div>

            <!-- PILLAR 3: TESSERA PRO-CLUB -->
            <div class="card-white" style="border-top: 3.5px solid #f59e0b; display: flex; flex-direction: column; justify-content: space-between; padding: 10px 12px;">
                <div>
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 5px;">
                        <span class="pill pill-gold">PILASTRO 03</span>
                        <span style="font-size: 8.5px; font-weight: 700; color: #d97706;">4 LIVELLI CARD</span>
                    </div>
                    <img src="{post5_b64}" style="width: 100%; height: 82px; object-fit: cover; object-position: top; background: #f8fafc; border-radius: 5px; border: 1px solid #e2e8f0; margin-bottom: 6px;" alt="Tessera Pro-Club">
                    <div style="font-size: 11.5px; font-weight: 800; color: #0f172a; margin-bottom: 3px;">Tessera Ufficiale PRO-CLUB</div>
                    <p style="font-size: 8.5px; color: #475569; line-height: 1.35; margin: 0 0 6px 0;">
                        Articolata in 4 livelli (<b>Basic, Silver, Gold, Diamond</b>) fondati su Disponibilità, Servizio, Qualità e Continuità garantita nel tempo.
                    </p>
                </div>
                <div style="background: #fffbeb; border: 1px solid #fde68a; border-radius: 5px; padding: 5px 7px; font-size: 8px;">
                    <b style="color: #d97706;">ZERO MAGAZZINO:</b> Italsport tiene le scorte a Ciserano per la società, con listino bloccato e sconti dedicati.
                </div>
            </div>
        </div>

        <div class="card" style="background: #f1f5f9; padding: 8px 12px; margin-top: 3px;">
            <div style="font-size: 8.5px; color: #334155;">
                <b>Come Lavorano Insieme:</b> La società disegna la divisa col <b>Configuratore 3D</b>, sottoscrive la <b>Tessera Pro-Club</b> (zero magazzino) e riceve la sua <b>Vetrina con Password</b> dove ritrova sempre gli stessi capi senza errori.
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <div class="footer-left">
            <span class="footer-pill">ITALSPORT GROUP — CISERANO (BG)</span>
            <span>PIANO STRATEGICO SOCIAL & VETRINA SQUADRE 2026</span>
        </div>
        <div>CAPITOLO 02: VETRINA CON PASSWORD, 3D & TESSERA PRO-CLUB</div>
        <div class="slide-num">Slide 04 / 12</div>
    </div>
</div>

<!-- SLIDE 5: FOCUS VETRINA CON PASSWORD & TARGET -->
<div class="slide">
    <div class="slide-header">
        <div class="header-left">
            <img src="{logo_b64}" class="header-logo" alt="Italsport Logo">
            <div class="header-title-box">
                <span class="category-tag">APPROFONDIMENTO VETRINA SQUADRA</span>
                <h2 class="slide-title">Cosa Intendiamo per "Vetrina Personalizzata per Ogni Squadra"</h2>
                <p class="slide-subtitle">Un'area riservata con password dove ogni squadra vede solo le proprie cose e ritrova sempre gli stessi articoli nel tempo.</p>
            </div>
        </div>
        <div class="header-right">
            <span class="chapter-badge">CAPITOLO 03 | VETRINA PASSWORD</span>
        </div>
    </div>

    <div class="slide-body">
        <div class="grid-2" style="align-items: stretch;">
            <!-- LEFT: HOW PASSWORD VETRINA WORKS -->
            <div style="display: flex; flex-direction: column; gap: 8px; justify-content: space-between;">
                <div style="font-size: 10px; font-weight: 800; color: #0f172a; text-transform: uppercase; letter-spacing: 0.5px;">I 3 Vantaggi Pratici dell'Accesso con Password</div>
                
                <div class="card-white" style="border-left: 3.5px solid #0284c7; padding: 11px 13px;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span style="font-size: 10px; font-weight: 800; color: #0284c7;">1. Accesso con Password Dedicata alla Squadra</span>
                        <span class="pill pill-blue">AREA PROTETTA</span>
                    </div>
                    <div style="font-size: 8.5px; color: #475569; margin-top: 3px; line-height: 1.35;">
                        Ogni società (es. <i>U.S.D. Brevianese</i>, <i>A.S.D. Gessate</i>) riceve una password esclusiva per accedere alla propria vetrina su `store.italsport-group.it`.
                    </div>
                </div>

                <div class="card-white" style="border-left: 3.5px solid #10b981; padding: 11px 13px;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span style="font-size: 10px; font-weight: 800; color: #16a34a;">2. Vede SOLO le Cose Relative alla Sua Squadra</span>
                        <span class="pill pill-green">ZERO CONFUSIONE</span>
                    </div>
                    <div style="font-size: 8.5px; color: #475569; margin-top: 3px; line-height: 1.35;">
                        Una volta entrati con la password, compaiono <b>solo ed esclusivamente i capi approvati per quella squadra</b> (con i suoi colori e il suo logo), senza vedere prodotti di altri club.
                    </div>
                </div>

                <div class="card-white" style="border-left: 3.5px solid #f59e0b; padding: 11px 13px;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span style="font-size: 10px; font-weight: 800; color: #d97706;">3. Trova Sempre le Stesse Cose Senza Problemi</span>
                        <span class="pill pill-gold">CONTINUITÀ 100%</span>
                    </div>
                    <div style="font-size: 8.5px; color: #475569; margin-top: 3px; line-height: 1.35;">
                        Poiché la vetrina contiene la linea codificata del club, chi accede oggi, a metà campionato o l'anno prossimo <b>trova sicuramente sempre gli stessi articoli senza problemi</b>.
                    </div>
                </div>
            </div>

            <!-- RIGHT: TARGETS & PILLARS -->
            <div style="display: flex; flex-direction: column; gap: 8px; justify-content: space-between;">
                <div style="font-size: 10px; font-weight: 800; color: #0f172a; text-transform: uppercase; letter-spacing: 0.5px;">A Chi Parliamo su Instagram (@italsportgroup)</div>

                <div class="card-white" style="padding: 10px 13px;">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 4px; font-size: 9px;">
                        <span><b>Società Sportive & Oratori</b> (Calcio, Volley, Basket, Rugby, Atletica)</span>
                        <span style="font-weight: 800; color: #0284c7;">45%</span>
                    </div>
                    <div style="height: 6px; background: #e2e8f0; border-radius: 3px; overflow: hidden;">
                        <div style="width: 45%; height: 100%; background: #0284c7;"></div>
                    </div>
                </div>

                <div class="card-white" style="padding: 10px 13px;">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 4px; font-size: 9px;">
                        <span><b>Tesserati, Mister & Famiglie</b> (Utilizzatori della Vetrina con Password)</span>
                        <span style="font-weight: 800; color: #10b981;">30%</span>
                    </div>
                    <div style="height: 6px; background: #e2e8f0; border-radius: 3px; overflow: hidden;">
                        <div style="width: 30%; height: 100%; background: #10b981;"></div>
                    </div>
                </div>

                <div class="card-white" style="padding: 10px 13px;">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 4px; font-size: 9px;">
                        <span><b>Scuole, Comuni, Associazioni & Aziende</b> (Forniture, Felpe, Premi e Gadget)</span>
                        <span style="font-weight: 800; color: #f59e0b;">25%</span>
                    </div>
                    <div style="height: 6px; background: #e2e8f0; border-radius: 3px; overflow: hidden;">
                        <div style="width: 25%; height: 100%; background: #f59e0b;"></div>
                    </div>
                </div>

                <div class="card-green" style="padding: 10px 13px;">
                    <div style="font-size: 9px; font-weight: 800; color: #166534;">ESEMPIO REALE DI LINEA BLOCCATA NELLA VETRINA:</div>
                    <div style="font-size: 8px; color: #334155; margin-top: 2px;">
                        Kit Gara Ufficiale • Tuta Completa Rom • Giacca 1/2 Zip Scotland (V05041) • Giubbotto Nepal (V0202) • Rain K-Way (A0600) • Borsa Bauletto (V12027).
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <div class="footer-left">
            <span class="footer-pill">ITALSPORT GROUP — CISERANO (BG)</span>
            <span>PIANO STRATEGICO SOCIAL & VETRINA SQUADRE 2026</span>
        </div>
        <div>CAPITOLO 03: FUNZIONAMENTO VETRINA CON PASSWORD</div>
        <div class="slide-num">Slide 05 / 12</div>
    </div>
</div>

<!-- SLIDE 6: SYNOPTIC TABLE OF 7 PILLAR POSTS -->
<div class="slide">
    <div class="slide-header">
        <div class="header-left">
            <img src="{logo_b64}" class="header-logo" alt="Italsport Logo">
            <div class="header-title-box">
                <span class="category-tag">STORYBOARD EDITORIALE (OTTOBRE – DICEMBRE)</span>
                <h2 class="slide-title">Quadro Sinottico dei 7 Post Realizzati con le Vere Foto di Italsport</h2>
                <p class="slide-subtitle">Ogni post usa le vere immagini di @italsportgroup e italsport-group.it con fascia tipografica pulita e zero scritte sovrapposte.</p>
            </div>
        </div>
        <div class="header-right">
            <span class="chapter-badge">CAPITOLO 04 | I 7 POST</span>
        </div>
    </div>

    <div class="slide-body">
        <table class="deck-table">
            <thead>
                <tr>
                    <th style="width: 7%;">Post</th>
                    <th style="width: 21%;">Tema & Vera Foto Usata</th>
                    <th style="width: 13%;">Periodo</th>
                    <th style="width: 37%;">Messaggio Chiave & Contenuto Reale</th>
                    <th style="width: 22%;">Call to Action (CTA)</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><b>#01</b></td>
                    <td><b>Stampa DTF & Reparto Grafico</b><br><span style="font-size: 7.5px; color: #64748b;">store.italsport-group.it/it/servizi/post/6-stampa-dtf</span></td>
                    <td><span class="pill pill-blue">METÀ OTTOBRE</span></td>
                    <td>Stampa DTF ad alta risoluzione su tessuti chiari e scuri già confezionati, morbida al tatto e resistente ai lavaggi.</td>
                    <td><b>Scopri il laboratorio stampa</b> a Ciserano o su store.italsport-group.it.</td>
                </tr>
                <tr>
                    <td><b>#02</b></td>
                    <td><b>Sublimazione & Full Print</b><br><span style="font-size: 7.5px; color: #64748b;">store.italsport-group.it/it/servizi/post/4-stampa-sublimatica</span></td>
                    <td><span class="pill pill-green">FINE OTTOBRE</span></td>
                    <td>Stampa sublimatica 100% traspirante (non ostruisce i pori del poliestere) e Full Print all-over prima della confezione.</td>
                    <td><b>Personalizza le divise gara</b> (linee Rodi e Athene Sublim).</td>
                </tr>
                <tr>
                    <td><b>#03</b></td>
                    <td><b>Simulatore 3D a 360°</b><br><span style="font-size: 7.5px; color: #64748b;">italsport-group.it/configuratore3d</span></td>
                    <td><span class="pill pill-blue">INIZIO NOV.</span></td>
                    <td>Crea la divisa nel Simulatore 3D scegliendo colori, colletto, numeri e sponsor e ruotala a 360° prima dell'ordine.</td>
                    <td><b>Prova la rotazione 3D a 360°</b> e segui lo stato di produzione.</td>
                </tr>
                <tr>
                    <td><b>#04</b></td>
                    <td><b>Vetrina Dedicata Squadra</b><br><span style="font-size: 7.5px; color: #64748b;">store.italsport-group.it/it/158-clienti-my-italsport</span></td>
                    <td><span class="pill pill-green">METÀ NOV.</span></td>
                    <td>Vetrina online My Italsport protetta da password riservata: atleti e genitori vedono e ordinano solo i capi del club.</td>
                    <td><b>Richiedi l'attivazione</b> della vetrina con password per la tua squadra.</td>
                </tr>
                <tr>
                    <td><b>#05</b></td>
                    <td><b>Continuità & Tessera Pro-Club</b><br><span style="font-size: 7.5px; color: #64748b;">Basic, Silver, Gold, Diamond + Linea Club</span></td>
                    <td><span class="pill pill-gold">FINE NOV.</span></td>
                    <td>"Il tuo magazzino a Ciserano lo facciamo noi": continuità garantita negli anni (Tuta Rom, Scotland, Nepal, K-Way, Borsa).</td>
                    <td><b>Attiva la Tessera Pro-Club</b> con listino bloccato e zero rimanenze.</td>
                </tr>
                <tr>
                    <td><b>#06</b></td>
                    <td><b>30 Anni, Linea Flame & Multi-Brand</b><br><span style="font-size: 7.5px; color: #64748b;">store.italsport-group.it/it/content/4-chi-siamo</span></td>
                    <td><span class="pill pill-purple">INIZIO DIC.</span></td>
                    <td>Oltre 4.600 realtà servite, i 5 pilastri Italsport, l'esclusiva Linea Flame e i migliori marchi (Erreà, Joma, Jako, Givova, Macron...).</td>
                    <td><b>Un unico partner tecnico</b> per sport, oratori, scuole e aziende.</td>
                </tr>
                <tr>
                    <td><b>#07</b></td>
                    <td><b>Auguri di Natale & Regali Club</b><br><span style="font-size: 7.5px; color: #64748b;">Buone Feste dal Team Italsport + Maglioni 360°</span></td>
                    <td><span class="pill pill-gold">20 DICEMBRE</span></td>
                    <td>Auguri di Buon Natale a tutte le società sportive e idee regalo personalizzate (maglioni custom 360°, felpe, sciarpe, zainetti).</td>
                    <td><b>Passa in showroom a Ciserano</b> per i regali natalizi del tuo club.</td>
                </tr>
            </tbody>
        </table>
    </div>

    <div class="slide-footer">
        <div class="footer-left">
            <span class="footer-pill">ITALSPORT GROUP — CISERANO (BG)</span>
            <span>PIANO STRATEGICO SOCIAL & VETRINA SQUADRE 2026</span>
        </div>
        <div>CAPITOLO 04: QUADRO SINOTTICO DEI 7 POST</div>
        <div class="slide-num">Slide 06 / 12</div>
    </div>
</div>

<!-- SLIDE 7: POSTS 1, 2, 3 DETAIL -->
<div class="slide">
    <div class="slide-header">
        <div class="header-left">
            <img src="{logo_b64}" class="header-logo" alt="Italsport Logo">
            <div class="header-title-box">
                <span class="category-tag">SCHEDE OPERATIVE POST (1/2)</span>
                <h2 class="slide-title">Post 01, 02 e 03: Stampa DTF, Sublimazione & Full Print, Simulatore 3D a 360°</h2>
                <p class="slide-subtitle">Visual realizzati con le vere immagini dei servizi di store.italsport-group.it e @italsportgroup.</p>
            </div>
        </div>
        <div class="header-right">
            <span class="chapter-badge">CAPITOLO 04 | POST 1 - 3</span>
        </div>
    </div>

    <div class="slide-body">
        <div class="grid-3" style="align-items: stretch;">
            <!-- POST 1 -->
            <div class="post-deck-card">
                <img src="{post1_b64}" class="post-deck-img" alt="Post 01">
                <div class="post-deck-body">
                    <span class="pill pill-blue" style="align-self: flex-start;">POST 01 • STAMPA DTF</span>
                    <div class="post-deck-title">DTF: Colori che Durano, Dettagli che Contano</div>
                    <p class="post-deck-copy">
                        <b>Copy:</b> «Nel nostro reparto grafico interno a Ciserano (BG) realizziamo stampe DTF ad altissima risoluzione su capi chiari e scuri già confezionati, morbide al tatto e resistenti ai lavaggi.»
                    </p>
                    <div class="post-deck-tag">#stampadtf #dtfprinting #italsportgroup #ciserano</div>
                </div>
            </div>

            <!-- POST 2 -->
            <div class="post-deck-card">
                <img src="{post2_b64}" class="post-deck-img" alt="Post 02">
                <div class="post-deck-body">
                    <span class="pill pill-green" style="align-self: flex-start;">POST 02 • SUBLIMAZIONE & FULL PRINT</span>
                    <div class="post-deck-title">Sublimazione 100% Traspirante & Full Print</div>
                    <p class="post-deck-copy">
                        <b>Copy:</b> «L'inchiostro entra nella fibra del poliestere senza ostruire i pori del tessuto: impercettibile al tatto, totalmente indelebile e stampato su tutta la superficie prima della confezione!»
                    </p>
                    <div class="post-deck-tag">#sublimazione #fullprint #italsportgroup #divisepersonalizzate</div>
                </div>
            </div>

            <!-- POST 3 -->
            <div class="post-deck-card">
                <img src="{post3_b64}" class="post-deck-img" alt="Post 03">
                <div class="post-deck-body">
                    <span class="pill pill-blue" style="align-self: flex-start;">POST 03 • SIMULATORE 3D</span>
                    <div class="post-deck-title">Crea la Divisa nel Simulatore 3D a 360°</div>
                    <p class="post-deck-copy">
                        <b>Copy:</b> «Personalizza modello, colori societari, colletto, numeri e sponsor su italsport-group.it, ruota la divisa a 360° da ogni angolazione e segui lo stato di produzione!»
                    </p>
                    <div class="post-deck-tag">#simulatore3d #configuratore3d #italsportgroup #customkit</div>
                </div>
            </div>
        </div>

        <div class="card" style="background: #f8fafc; padding: 7px 11px; margin-top: 2px;">
            <div style="font-size: 8.5px; color: #475569;">
                <b>Coerenza Tecnica Verificata su store.italsport-group.it:</b> I post 1, 2 e 3 mostrano le reali tecnologie produttive di Italsport (Stampa DTF, Stampa Sublimatica, Stampa Full Print All-Over, Reparto Grafico Interno e Configuratore 3D a 360°).
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <div class="footer-left">
            <span class="footer-pill">ITALSPORT GROUP — CISERANO (BG)</span>
            <span>PIANO STRATEGICO SOCIAL & VETRINA SQUADRE 2026</span>
        </div>
        <div>CAPITOLO 04: SCHEDE POST 01 - 03</div>
        <div class="slide-num">Slide 07 / 12</div>
    </div>
</div>

<!-- SLIDE 8: POSTS 4, 5, 6, 7 DETAIL -->
<div class="slide">
    <div class="slide-header">
        <div class="header-left">
            <img src="{logo_b64}" class="header-logo" alt="Italsport Logo">
            <div class="header-title-box">
                <span class="category-tag">SCHEDE OPERATIVE POST (2/2)</span>
                <h2 class="slide-title">Post 04, 05, 06 e 07: Vetrina Squadra, Continuità Pro-Club, Linea Flame e Natale</h2>
                <p class="slide-subtitle">Dal progetto My Italsport a quanto emerso nell'incontro (continuità forniture, zero magazzino, 4.600+ realtà) fino agli auguri di Natale.</p>
            </div>
        </div>
        <div class="header-right">
            <span class="chapter-badge">CAPITOLO 04 | POST 4 - 7</span>
        </div>
    </div>

    <div class="slide-body">
        <div class="grid-4" style="align-items: stretch;">
            <!-- POST 4 -->
            <div class="post-deck-card">
                <img src="{post4_b64}" class="post-deck-img" alt="Post 04">
                <div class="post-deck-body">
                    <span class="pill pill-blue" style="align-self: flex-start;">POST 04 • MY ITALSPORT</span>
                    <div class="post-deck-title">Vetrina Dedicata alla Squadra</div>
                    <p class="post-deck-copy">
                        <b>Copy:</b> «Una Vetrina Online su store.italsport-group.it protetta da password riservata: atleti e genitori vedono solo i capi del club.»
                    </p>
                    <div class="post-deck-tag">#myitalsport #vetrinasquadra</div>
                </div>
            </div>

            <!-- POST 5 -->
            <div class="post-deck-card">
                <img src="{post5_b64}" class="post-deck-img" alt="Post 05">
                <div class="post-deck-body">
                    <span class="pill pill-gold" style="align-self: flex-start;">POST 05 • PRO-CLUB & CONTINUITÀ</span>
                    <div class="post-deck-title">Zero Magazzino & Continuità</div>
                    <p class="post-deck-copy">
                        <b>Copy:</b> «Il tuo magazzino a Ciserano lo facciamo noi: continuità negli anni (Tuta Rom, Scotland, Nepal, K-Way) e Card Pro-Club.»
                    </p>
                    <div class="post-deck-tag">#tesseraproclub #continuità</div>
                </div>
            </div>

            <!-- POST 6 -->
            <div class="post-deck-card">
                <img src="{post6_b64}" class="post-deck-img" alt="Post 06">
                <div class="post-deck-body">
                    <span class="pill pill-green" style="align-self: flex-start;">POST 06 • LINEA FLAME & BRAND</span>
                    <div class="post-deck-title">30 Anni, 4.600+ Realtà & Flame</div>
                    <p class="post-deck-copy">
                        <b>Copy:</b> «I 5 pilastri di Italsport: Forniture, Logistica, Identità, l'esclusiva Linea Flame e i migliori marchi Multi-Brand.»
                    </p>
                    <div class="post-deck-tag">#lineaflame #multibrand #30anni</div>
                </div>
            </div>

            <!-- POST 7 -->
            <div class="post-deck-card">
                <img src="{post7_b64}" class="post-deck-img" alt="Post 07">
                <div class="post-deck-body">
                    <span class="pill pill-purple" style="align-self: flex-start;">POST 07 • AUGURI DI NATALE</span>
                    <div class="post-deck-title">Buon Natale & Regali Club</div>
                    <p class="post-deck-copy">
                        <b>Copy:</b> «Buone Feste dal Team di Italsport! Programma i regali societari e i maglioni natalizi custom a 360° nel nostro showroom.»
                    </p>
                    <div class="post-deck-tag">#buonnatale #italsportgroup</div>
                </div>
            </div>
        </div>

        <div class="grid-3" style="margin-top: 3px;">
            <div class="card-white" style="border-left: 3.5px solid #10b981; padding: 7px 10px;">
                <div style="font-size: 8.5px; font-weight: 800; color: #047857;">1. Accesso con Password Dedicata:</div>
                <div style="font-size: 8px; color: #475569;">Ogni squadra entra con la sua password su `store.italsport-group.it`.</div>
            </div>
            <div class="card-white" style="border-left: 3.5px solid #0284c7; padding: 7px 10px;">
                <div style="font-size: 8.5px; font-weight: 800; color: #0369a1;">2. Vede Solo le Cose della Squadra:</div>
                <div style="font-size: 8px; color: #475569;">Visualizza esclusivamente gli articoli approvati per il proprio club.</div>
            </div>
            <div class="card-white" style="border-left: 3.5px solid #d97706; padding: 7px 10px;">
                <div style="font-size: 8.5px; font-weight: 800; color: #b45309;">3. Sempre le Stesse Cose Senza Problemi:</div>
                <div style="font-size: 8px; color: #475569;">Ritrova sempre gli stessi modelli e colori nel tempo senza errori.</div>
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <div class="footer-left">
            <span class="footer-pill">ITALSPORT GROUP — CISERANO (BG)</span>
            <span>PIANO STRATEGICO SOCIAL & VETRINA SQUADRE 2026</span>
        </div>
        <div>CAPITOLO 04: SCHEDE POST 04 - 07</div>
        <div class="slide-num">Slide 08 / 12</div>
    </div>
</div>

<!-- SLIDE 9: REELS & STORIES STRATEGY -->
<div class="slide">
    <div class="slide-header">
        <div class="header-left">
            <img src="{logo_b64}" class="header-logo" alt="Italsport Logo">
            <div class="header-title-box">
                <span class="category-tag">FORMAT VIDEO REELS & STORIE IN EVIDENZA</span>
                <h2 class="slide-title">I 3 Video Reels Realistici e le 6 Storie in Evidenza su @italsportgroup</h2>
                <p class="slide-subtitle">Contenuti semplici e concreti da pubblicare insieme ai 7 post per mostrare il 3D a 360°, la Vetrina con Password e lo Showroom.</p>
            </div>
        </div>
        <div class="header-right">
            <span class="chapter-badge">CAPITOLO 05 | REELS & STORIES</span>
        </div>
    </div>

    <div class="slide-body">
        <div class="grid-2-3" style="align-items: stretch;">
            <!-- REELS COLUMN -->
            <div style="display: flex; flex-direction: column; gap: 8px; justify-content: space-between;">
                <div style="font-size: 10px; font-weight: 800; color: #0f172a; text-transform: uppercase;">I 3 Video Reels (Già Integrati nel Mockup)</div>

                <div class="card-white" style="border-left: 3.5px solid #0284c7; padding: 9px 12px;">
                    <span class="pill pill-blue">REEL 01 • GIÀ PRONTO</span>
                    <div style="font-size: 10.5px; font-weight: 800; color: #0f172a; margin-top: 3px;">Rotazione 3D a 360° della Maglia</div>
                    <div style="font-size: 8.5px; color: #475569; margin: 2px 0;">L'animazione reale a 360° (`configuratore3d_real.gif`) dal sito Italsport con vista fronte, maniche e numero 27 sul retro.</div>
                    <div style="font-size: 8px; color: #0284c7; font-weight: 700;">Testo: «Disegna la divisa in 3D e girala a 360° prima dell'ordine.»</div>
                </div>

                <div class="card-white" style="border-left: 3.5px solid #10b981; padding: 9px 12px;">
                    <span class="pill pill-green">REEL 02 • TUTORIAL CLUB</span>
                    <div style="font-size: 10.5px; font-weight: 800; color: #0f172a; margin-top: 3px;">Accesso con Password alla Vetrina Squadra</div>
                    <div style="font-size: 8.5px; color: #475569; margin: 2px 0;">Registrazione schermo: la squadra inserisce la sua password e vede solo i propri capi ufficiali sempre disponibili.</div>
                    <div style="font-size: 8px; color: #16a34a; font-weight: 700;">Testo: «Una password per ogni squadra: trovi sempre le stesse cose.»</div>
                </div>

                <div class="card-white" style="border-left: 3.5px solid #f59e0b; padding: 9px 12px;">
                    <span class="pill pill-gold">REEL 03 • SHOWROOM CISERANO</span>
                    <div style="font-size: 10.5px; font-weight: 800; color: #0f172a; margin-top: 3px;">Dentro lo Showroom di Via Prov. Francesca</div>
                    <div style="font-size: 8.5px; color: #475569; margin: 2px 0;">Breve video tra i manichini vestiti con i kit gara, le tute, le borse e i gadget nello showroom di Ciserano (BG).</div>
                    <div style="font-size: 8px; color: #d97706; font-weight: 700;">Testo: «30 anni al fianco delle società sportive a Ciserano (BG).»</div>
                </div>
            </div>

            <!-- STORIES COLUMN -->
            <div style="display: flex; flex-direction: column; gap: 8px; justify-content: space-between;">
                <div style="font-size: 10px; font-weight: 800; color: #0f172a; text-transform: uppercase;">Routine Settimanale delle Stories</div>

                <div class="grid-2">
                    <div class="card" style="background: #ffffff; border-top: 2.5px solid #0284c7; padding: 9px 11px;">
                        <div style="font-size: 9.5px; font-weight: 800; color: #0284c7;">LUNEDÌ • SQUADRE IN CAMPO</div>
                        <div style="font-size: 8px; color: #334155; margin-top: 3px; line-height: 1.35;">
                            Repost delle foto del weekend delle società partner del territorio (es. Brevianese, Gessate, Ciserano).
                        </div>
                    </div>

                    <div class="card" style="background: #ffffff; border-top: 2.5px solid #10b981; padding: 9px 11px;">
                        <div style="font-size: 9.5px; font-weight: 800; color: #16a34a;">MERCOLEDÌ • CONFIGURATORE 3D</div>
                        <div style="font-size: 8px; color: #334155; margin-top: 3px; line-height: 1.35;">
                            Storia con la maglia 3D che gira a 360° e sticker link diretto a `italsport-group.it`.
                        </div>
                    </div>

                    <div class="card" style="background: #ffffff; border-top: 2.5px solid #f59e0b; padding: 9px 11px;">
                        <div style="font-size: 9.5px; font-weight: 800; color: #d97706;">VENERDÌ • VETRINA & PRO-CLUB</div>
                        <div style="font-size: 8px; color: #334155; margin-top: 3px; line-height: 1.35;">
                            Domande/risposte su come attivare la Vetrina con Password e i 4 livelli della Tessera Pro-Club.
                        </div>
                    </div>

                    <div class="card" style="background: #ffffff; border-top: 2.5px solid #8b5cf6; padding: 9px 11px;">
                        <div style="font-size: 9.5px; font-weight: 800; color: #8b5cf6;">SABATO • SHOWROOM CISERANO</div>
                        <div style="font-size: 8px; color: #334155; margin-top: 3px; line-height: 1.35;">
                            Nuovi arrivi in showroom a Ciserano: giubbotti invernali, tute, borse, premi e gadget personalizzati.
                        </div>
                    </div>
                </div>

                <div class="card-blue" style="margin-top: 3px; padding: 9px 12px;">
                    <div style="font-size: 9px; font-weight: 800; color: #0369a1;">6 CARTELLE STORIE IN EVIDENZA (HIGHLIGHTS):</div>
                    <div style="font-size: 8px; color: #475569; margin-top: 3px;">
                        <b>1. Configuratore</b> • <b>2. Vetrina Club</b> • <b>3. Pro-Club</b> • <b>4. Divise Custom</b> • <b>5. Showroom BG</b> • <b>6. Sul Campo</b>.
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <div class="footer-left">
            <span class="footer-pill">ITALSPORT GROUP — CISERANO (BG)</span>
            <span>PIANO STRATEGICO SOCIAL & VETRINA SQUADRE 2026</span>
        </div>
        <div>CAPITOLO 05: FORMAT VIDEO REELS & STORIES</div>
        <div class="slide-num">Slide 09 / 12</div>
    </div>
</div>

<!-- SLIDE 10: WEB PLATFORM & INTERACTIVE MOCKUP -->
<div class="slide">
    <div class="slide-header">
        <div class="header-left">
            <img src="{logo_b64}" class="header-logo" alt="Italsport Logo">
            <div class="header-title-box">
                <span class="category-tag">PROTOTIPO WEB INTERATTIVO LIVE</span>
                <h2 class="slide-title">Mockup Instagram Realistico, Maglia 3D a 360° e Demo Vetrina con Password</h2>
                <p class="slide-subtitle">Una web app interattiva pronta all'uso per mostrare dal vivo a Italsport tutti i contenuti e le funzionalità.</p>
            </div>
        </div>
        <div class="header-right">
            <span class="chapter-badge">CAPITOLO 05 | DEMO LIVE</span>
        </div>
    </div>

    <div class="slide-body">
        <div class="grid-2-3" style="align-items: stretch;">
            <!-- LEFT COLUMN: LIVE URL & FEATURES -->
            <div style="display: flex; flex-direction: column; gap: 8px; justify-content: space-between;">
                <div class="card-green" style="padding: 12px 14px;">
                    <div style="font-size: 9.5px; font-weight: 800; color: #16a34a; text-transform: uppercase;">SITO DEMO PUBBLICATO SU GITHUB PAGES</div>
                    <div style="font-size: 14px; font-weight: 800; color: #0f172a; margin: 4px 0;">Mockup Interattivo Online</div>
                    <div style="font-size: 9px; color: #334155; word-break: break-all; font-family: monospace; background: #ffffff; padding: 5px 8px; border-radius: 5px; border: 1px solid #cbd5e1;">
                        https://kingsalvo05.github.io/italsport-mockup/
                    </div>
                    <div style="font-size: 8.5px; color: #15803d; margin-top: 5px; font-weight: 600;">
                        ✓ Consultabile sia online che offline tramite il file `Instagram_Mockup_Italsport.html`.
                    </div>
                </div>

                <div class="card-white" style="padding: 12px 14px;">
                    <div style="font-size: 10px; font-weight: 800; color: #0f172a; margin-bottom: 5px;">COSA PUOI PROVARE NEL MOCKUP INTERATTIVO:</div>
                    <div style="display: flex; flex-direction: column; gap: 4px; font-size: 8.5px; color: #475569;">
                        <div>• <b>Feed Instagram Realistico (@italsportgroup):</b> clicca sui post per mettere "Mi piace" (il numero aumenta), fai doppio clic per il cuore grande, sfoglia le slide dei caroselli, salva i post e apri le Storie.</div>
                        <div>• <b>Configuratore 3D + Video 360° Reale:</b> vedi sia la vera animazione a 360° della maglia 3D dal sito Italsport sia il simulatore interattivo per cambiare colori, pattern, colletto e sponsor.</div>
                        <div>• <b>Simulatore Vetrina Squadra con Password:</b> prova a cambiare squadra (<i>U.S.D. Brevianese</i>, <i>A.S.D. Gessate</i>, <i>Volley Ciserano</i>) o simula l'inserimento della password per vedere solo i capi di quella squadra!</div>
                    </div>
                </div>
            </div>

            <!-- RIGHT COLUMN: THREE REAL ASSET HIGHLIGHTS -->
            <div style="display: flex; flex-direction: column; gap: 8px; justify-content: space-between;">
                <div style="font-size: 10px; font-weight: 800; color: #0f172a; text-transform: uppercase;">Solo Vere Foto di @italsportgroup e italsport-group.it</div>

                <div class="grid-3">
                    <div class="card-white" style="text-align: center; padding: 8px;">
                        <img src="{shw_b64}" style="width: 100%; height: 80px; object-fit: cover; border-radius: 5px; border: 1px solid #e2e8f0;" alt="Showroom Ciserano">
                        <div style="font-size: 9px; font-weight: 800; color: #0f172a; margin-top: 5px;">Showroom Ciserano</div>
                        <div style="font-size: 8px; color: #64748b;">Vera foto negozio @italsportgroup</div>
                    </div>
                    <div class="card-white" style="text-align: center; padding: 8px;">
                        <img src="{man_b64}" style="width: 100%; height: 80px; object-fit: cover; border-radius: 5px; border: 1px solid #e2e8f0;" alt="Manichini Divise">
                        <div style="font-size: 9px; font-weight: 800; color: #0f172a; margin-top: 5px;">Divise su Manichino</div>
                        <div style="font-size: 8px; color: #64748b;">Vere maglie calcio e basket</div>
                    </div>
                    <div class="card-white" style="text-align: center; padding: 8px;">
                        <img src="{card_real_b64}" style="width: 100%; height: 80px; object-fit: contain; background: #f8fafc; border-radius: 5px; border: 1px solid #e2e8f0;" alt="Tessera Pro-Club">
                        <div style="font-size: 9px; font-weight: 800; color: #0f172a; margin-top: 5px;">Tessera Pro-Club</div>
                        <div style="font-size: 8px; color: #64748b;">Grafica ufficiale dal sito</div>
                    </div>
                </div>

                <div class="card" style="background: #f8fafc; font-size: 8.5px; color: #334155; line-height: 1.4; padding: 10px 13px;">
                    <b>Impatto durante la Presentazione al Cliente:</b> Il titolare Vincenzo Locatelli e il team di Italsport vedranno immediatamente le proprie vere foto, il proprio showroom di Ciserano e la dimostrazione pratica della Vetrina con Password.
                </div>
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <div class="footer-left">
            <span class="footer-pill">ITALSPORT GROUP — CISERANO (BG)</span>
            <span>PIANO STRATEGICO SOCIAL & VETRINA SQUADRE 2026</span>
        </div>
        <div>CAPITOLO 05: PIATTAFORMA WEB & PROTOTIPO LIVE</div>
        <div class="slide-num">Slide 10 / 12</div>
    </div>
</div>

<!-- SLIDE 11: TERRITORIAL ACTION & CRM SYNERGY -->
<div class="slide">
    <div class="slide-header">
        <div class="header-left">
            <img src="{logo_b64}" class="header-logo" alt="Italsport Logo">
            <div class="header-title-box">
                <span class="category-tag">AZIONE COMMERCIALE SUL TERRITORIO & CRM</span>
                <h2 class="slide-title">Sinergia tra Instagram, Showroom di Ciserano e le 4.600 Anagrafiche</h2>
                <p class="slide-subtitle">Come usare i contenuti social e una promozione locale mirata per attivare nuove Vetrine con Password e Tessere Pro-Club.</p>
            </div>
        </div>
        <div class="header-right">
            <span class="chapter-badge">CAPITOLO 06 | TERRITORIO & KPI</span>
        </div>
    </div>

    <div class="slide-body">
        <div class="grid-3" style="margin-bottom: 3px;">
            <div class="card-green" style="padding: 12px 14px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span class="pill pill-green">AZIONE 01</span>
                    <span style="font-weight: 800; font-size: 11px; color: #15803d;">VETRINE PASSWORD</span>
                </div>
                <div style="font-size: 11px; font-weight: 800; color: #0f172a; margin: 4px 0 2px 0;">Proposta Diretta alle Società</div>
                <div style="font-size: 8.5px; color: #475569; line-height: 1.35;">
                    Usare il Post #05 e la demo interattiva per proporre alle società sportive del territorio l'apertura della propria <b>Vetrina con Password</b> su `store.italsport-group.it`.
                </div>
            </div>

            <div class="card-blue" style="padding: 12px 14px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span class="pill pill-blue">AZIONE 02</span>
                    <span style="font-weight: 800; font-size: 11px; color: #0369a1;">RAGGIO 35 KM DA CISERANO</span>
                </div>
                <div style="font-size: 11px; font-weight: 800; color: #0f172a; margin: 4px 0 2px 0;">Sponsorizzazione Locale Mirata</div>
                <div style="font-size: 8.5px; color: #475569; line-height: 1.35;">
                    Promozione geolocalizzata su Bergamo, Treviglio, Dalmine, Gessate e provincia verso dirigenti sportivi, oratori e scuole sul Configuratore 3D e la Card Pro-Club.
                </div>
            </div>

            <div class="card-gold" style="padding: 12px 14px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span class="pill pill-gold">AZIONE 03</span>
                    <span style="font-weight: 800; font-size: 11px; color: #b45309;">4.600 CONTATTI CRM</span>
                </div>
                <div style="font-size: 11px; font-weight: 800; color: #0f172a; margin: 4px 0 2px 0;">Riattivazione Clienti Storici</div>
                <div style="font-size: 8.5px; color: #475569; line-height: 1.35;">
                    Affiancare ai post di novembre e dicembre un contatto diretto verso le anagrafiche già presenti in CRM per forniture invernali e gadget natalizi.
                </div>
            </div>
        </div>

        <table class="deck-table">
            <thead>
                <tr>
                    <th style="width: 26%;">Obiettivo Operativo</th>
                    <th style="width: 22%;">Situazione Attuale</th>
                    <th style="width: 24%;">Target Trimestrale (Ott – Dic)</th>
                    <th style="width: 28%;">Vantaggio Concreto per Italsport</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><b>Vetrine Squadra con Password Attive</b></td>
                    <td>Servizio presente ma poco conosciuto sui social</td>
                    <td><b>+15 / 20 Squadre con Vetrina</b></td>
                    <td>Ogni squadra ordina solo i suoi capi codificati senza errori</td>
                </tr>
                <tr>
                    <td><b>Adesioni Tessera PRO-CLUB</b></td>
                    <td>Forniture gestite singolarmente</td>
                    <td><b>+12 / 15 Società Pro-Club</b></td>
                    <td>Fidelizzazione pluriennale nei 4 livelli (Basic, Silver, Gold, Diamond)</td>
                </tr>
                <tr>
                    <td><b>Prove Configuratore 3D a 360°</b></td>
                    <td>Traffico solo diretto sul sito</td>
                    <td><b>80+ Bozze Divisa Configurate</b></td>
                    <td>Contatti caldi di direttivi pronti a rinnovare le divise</td>
                </tr>
                <tr>
                    <td><b>Affluenza Showroom Ciserano (BG)</b></td>
                    <td>Passaparola storico locale</td>
                    <td><b>Aumento visite e ordini fine anno</b></td>
                    <td>Vendita di tute, giubbotti invernali, borse e gadget natalizi</td>
                </tr>
            </tbody>
        </table>
    </div>

    <div class="slide-footer">
        <div class="footer-left">
            <span class="footer-pill">ITALSPORT GROUP — CISERANO (BG)</span>
            <span>PIANO STRATEGICO SOCIAL & VETRINA SQUADRE 2026</span>
        </div>
        <div>CAPITOLO 06: AZIONE TERRITORIALE & OBIETTIVI</div>
        <div class="slide-num">Slide 11 / 12</div>
    </div>
</div>

<!-- SLIDE 12: ROADMAP & NEXT STEPS -->
<div class="slide">
    <div class="slide-header">
        <div class="header-left">
            <img src="{logo_b64}" class="header-logo" alt="Italsport Logo">
            <div class="header-title-box">
                <span class="category-tag">CRONOPROGRAMMA OPERATIVO & CONTATTI</span>
                <h2 class="slide-title">Tabella di Marcia da Ottobre al 31 Dicembre e Sintesi Finale</h2>
                <p class="slide-subtitle">Un calendario ordinato e realistico per accompagnare @italsportgroup lungo tutta la stagione autunnale e natalizia.</p>
            </div>
        </div>
        <div class="header-right">
            <span class="chapter-badge">CAPITOLO 07 | ROADMAP</span>
        </div>
    </div>

    <div class="slide-body">
        <div class="grid-4" style="margin-bottom: 4px;">
            <div class="card-white" style="border-top: 3.5px solid #0284c7; padding: 10px 12px;">
                <span class="pill pill-blue">FASE 1 • METÀ OTTOBRE</span>
                <div style="font-size: 10.5px; font-weight: 800; color: #0f172a; margin: 3px 0 2px 0;">Stampa DTF & Sublimazione</div>
                <div style="font-size: 8px; color: #475569; line-height: 1.35;">
                    Ottimizzazione bio `@italsportgroup`, <b>Post #01</b> (Stampa DTF & Reparto Grafico Ciserano) e <b>Post #02</b> (Stampa Sublimatica 100% traspirante & Full Print All-Over).
                </div>
            </div>

            <div class="card-white" style="border-top: 3.5px solid #0284c7; padding: 10px 12px;">
                <span class="pill pill-blue">FASE 2 • INIZIO NOV.</span>
                <div style="font-size: 10.5px; font-weight: 800; color: #0f172a; margin: 3px 0 2px 0;">Simulatore 3D & Vetrina Club</div>
                <div style="font-size: 8px; color: #475569; line-height: 1.35;">
                    <b>Post #03 + Reel 360°</b> (Simulatore 3D con rotazione della divisa a 360°) e <b>Post #04</b> (Vetrina My Italsport protetta da Password per ogni squadra).
                </div>
            </div>

            <div class="card-white" style="border-top: 3.5px solid #10b981; padding: 10px 12px;">
                <span class="pill pill-green">FASE 3 • FINE NOV.</span>
                <div style="font-size: 10.5px; font-weight: 800; color: #0f172a; margin: 3px 0 2px 0;">Pro-Club & Linea Flame</div>
                <div style="font-size: 8px; color: #475569; line-height: 1.35;">
                    <b>Post #05</b> (Continuità negli anni, Zero Magazzino a Ciserano & Card Pro-Club) e <b>Post #06</b> (30 Anni di Storia, 4.600+ Realtà in CRM, Linea Flame & Multi-Brand).
                </div>
            </div>

            <div class="card-white" style="border-top: 3.5px solid #8b5cf6; padding: 10px 12px;">
                <span class="pill pill-purple">FASE 4 • DICEMBRE</span>
                <div style="font-size: 10.5px; font-weight: 800; color: #0f172a; margin: 3px 0 2px 0;">Auguri di Natale & Regali</div>
                <div style="font-size: 8px; color: #475569; line-height: 1.35;">
                    <b>Post #07</b> (Auguri di Buon Natale dal Team Italsport, Showroom Ciserano, Maglioni Natalizi Custom a 360° e idee regalo per le squadre).
                </div>
            </div>
        </div>

        <div class="card" style="background: #f0f7ff; border: 1px solid #bfdbfe; padding: 8px 12px;">
            <div style="font-size: 9px; font-weight: 800; color: #0369a1; text-transform: uppercase;">I 3 PUNTI FERMI DI QUESTO PIANO:</div>
            <div class="grid-3" style="font-size: 8.5px; color: #334155; margin-top: 3px;">
                <div><b>1. Solo Vere Foto Italsport:</b> scatti reali da `@italsportgroup` e `italsport-group.it`, zero foto generiche e zero testi tagliati.</div>
                <div><b>2. Vetrina con Password Chiara:</b> ogni squadra accede con la sua password e vede solo le cose relative al proprio club, trovando sempre le stesse cose.</div>
                <div><b>3. Stile Chiaro e Professionale:</b> impaginazione pulita, descrizioni realistiche e mockup interattivo pronto da mostrare al cliente.</div>
            </div>
        </div>

        <div class="card-white" style="padding: 8px 12px; margin-top: 2px;">
            <div class="grid-2" style="align-items: center; font-size: 9px;">
                <div>
                    <div style="font-weight: 800; color: #0f172a; font-size: 10px;">ITALSPORT GROUP (Italsport di Locatelli Vincenzo)</div>
                    <div style="color: #475569;">Sede & Showroom: <b>Via Provinciale Francesca 2H/I — 24040 Ciserano, Loc. Zingonia (BG)</b></div>
                    <div style="color: #475569;">Tel. <b>035 4191221</b> • Cell. <b>335 7001956</b> • Email: <b>info@italsport-group.it</b> • P.IVA <b>01778490167</b></div>
                </div>
                <div style="text-align: right;">
                    <div style="font-weight: 800; color: #0284c7;">Siti Ufficiali: italsport-group.it | store.italsport-group.it</div>
                    <div style="color: #64748b; font-size: 8px;">Instagram: <b>@italsportgroup</b> • Facebook: <b>@GroupItalsport</b></div>
                </div>
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <div class="footer-left">
            <span class="footer-pill">ITALSPORT GROUP — CISERANO (BG)</span>
            <span>PIANO STRATEGICO SOCIAL & VETRINA SQUADRE 2026</span>
        </div>
        <div>CAPITOLO 07: CRONOPROGRAMMA & CONTATTI</div>
        <div class="slide-num">Slide 12 / 12</div>
    </div>
</div>

</body>
</html>
"""

html_path = os.path.abspath('full_pdf_template.html')
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"full_pdf_template.html written successfully ({len(html)} bytes).")

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
pdf_path = os.path.abspath('Piano_Social_Italsport_2026.pdf')

cmd = [
    chrome, '--headless=new', '--disable-gpu', '--no-sandbox', '--no-pdf-header-footer',
    f'--print-to-pdf={pdf_path}', f'file:///{html_path.replace(os.sep, "/")}'
]
res = subprocess.run(cmd, capture_output=True, text=True)
print("Chrome output:", res.stderr.strip() or res.stdout.strip())

doc = pymupdf.open(pdf_path)
print(f"Regenerated Piano_Social_Italsport_2026.pdf: {len(doc)} pages, size: {os.path.getsize(pdf_path)} bytes")

out_dir = r'C:\Users\salvo\.gemini\antigravity\brain\dc9abd1d-f990-4c44-a20b-bd6ec7f9af7d\scratch'
for i in [0, 3, 4, 6, 7, 9, 11]:
    pix = doc[i].get_pixmap(dpi=120)
    pix.save(os.path.join(out_dir, f'ciserano_slide_{i+1}.png'))
doc.close()
print("Rendered Ciserano slides to scratch!")
