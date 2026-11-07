import os, base64

def get_base64_image(filename):
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            b64 = base64.b64encode(f.read()).decode('utf-8')
            ext = 'png' if filename.endswith('.png') else 'jpeg'
            return f"data:image/{ext};base64,{b64}"
    return ""

print("Encoding real Italsport Ciserano (BG) images for PDF...")
logo_b64 = get_base64_image("cropped-cropped-italsportlogo.png")
post1_b64 = get_base64_image("img_post1_jersey.jpg")
post2_b64 = get_base64_image("img_post2_3d.jpg")
post3_b64 = get_base64_image("img_post3_fidelity.jpg")
post4_b64 = get_base64_image("img_post4_stack.jpg")
post5_b64 = get_base64_image("img_post5_portal.jpg")
post6_b64 = get_base64_image("img_post6_winter.jpg")
post7_b64 = get_base64_image("img_post7_celebration.jpg")
card_real_b64 = get_base64_image("card_proclub_real.jpg")

print("Generating full_pdf_template.html (Light Corporate Executive Theme — Ciserano BG)...")

html_pdf = f"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<title>Italsport Group Ciserano (BG) - Piano Strategico Social & Crescita B2B 2026</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap');

@page {{
    size: A4 portrait;
    margin: 0;
}}

* {{
    box-sizing: border-box;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
}}

body {{
    margin: 0;
    padding: 0;
    background: #e2e8f0;
    font-family: 'Plus Jakarta Sans', 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    color: #0f172a;
    line-height: 1.4;
    font-size: 13px;
}}

.page {{
    width: 210mm;
    height: 297mm;
    max-height: 297mm;
    overflow: hidden;
    box-sizing: border-box;
    padding: 13mm 16mm 11mm 16mm;
    background: #ffffff;
    margin: 0 auto;
    page-break-after: always;
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}}

/* Header */
.page-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-bottom: 8px;
    border-bottom: 1.5px solid #e2e8f0;
    margin-bottom: 12px;
}}

.header-brand {{
    display: flex;
    align-items: center;
    gap: 12px;
}}

.header-brand img {{
    height: 26px;
    object-fit: contain;
}}

.header-title-box {{
    display: flex;
    flex-direction: column;
}}

.header-category {{
    font-size: 9px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: #0284c7;
}}

.header-subtitle {{
    font-size: 11px;
    font-weight: 600;
    color: #334155;
}}

.header-badge {{
    background: #f1f5f9;
    color: #475569;
    font-size: 10px;
    font-weight: 600;
    padding: 4px 10px;
    border-radius: 6px;
    border: 1px solid #e2e8f0;
}}

/* Footer */
.page-footer {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-top: 8px;
    border-top: 1px solid #e2e8f0;
    margin-top: 10px;
    font-size: 10px;
    color: #64748b;
}}

.page-footer .meta-left {{
    font-weight: 600;
    color: #0f172a;
}}

.page-footer .page-number {{
    font-weight: 700;
    color: #0284c7;
    background: #f0f9ff;
    padding: 2px 8px;
    border-radius: 4px;
    border: 1px solid #bae6fd;
}}

/* Page Content Container */
.page-content {{
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    gap: 10px;
}}

/* Typography */
h1.page-title {{
    font-size: 22px;
    font-weight: 800;
    color: #0f172a;
    margin: 0 0 3px 0;
    line-height: 1.2;
    letter-spacing: -0.5px;
}}

p.page-intro {{
    font-size: 12px;
    color: #475569;
    margin: 0 0 8px 0;
    line-height: 1.45;
}}

/* Cards & Surfaces */
.card {{
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    padding: 12px 14px;
}}

.card-white {{
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    padding: 12px 14px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.02);
}}

.card-accent-blue {{
    background: #f0f9ff;
    border: 1px solid #bae6fd;
    border-radius: 10px;
    padding: 12px 14px;
}}

.card-accent-gold {{
    background: #fefce8;
    border: 1px solid #fef08a;
    border-radius: 10px;
    padding: 12px 14px;
}}

.card-accent-emerald {{
    background: #ecfdf5;
    border: 1px solid #a7f3d0;
    border-radius: 10px;
    padding: 12px 14px;
}}

.grid-2 {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
}}

.grid-3 {{
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 10px;
}}

.grid-4 {{
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr;
    gap: 8px;
}}

/* Badges */
.badge {{
    display: inline-block;
    padding: 3px 8px;
    border-radius: 5px;
    font-size: 10px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}}

.badge-blue {{ background: #e0f2fe; color: #0369a1; border: 1px solid #bae6fd; }}
.badge-navy {{ background: #1e3a8a; color: #ffffff; }}
.badge-gold {{ background: #fef3c7; color: #b45309; border: 1px solid #fde68a; }}
.badge-green {{ background: #dcfce7; color: #15803d; border: 1px solid #bbf7d0; }}
.badge-gray {{ background: #f1f5f9; color: #475569; border: 1px solid #e2e8f0; }}

/* Tables */
table.data-table {{
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    font-size: 11px;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    overflow: hidden;
}}

table.data-table th {{
    background: #f1f5f9;
    color: #1e293b;
    padding: 8px 10px;
    font-weight: 700;
    text-align: left;
    border-bottom: 1.5px solid #cbd5e1;
}}

table.data-table td {{
    padding: 7px 10px;
    border-bottom: 1px solid #f1f5f9;
    color: #334155;
    vertical-align: top;
}}

table.data-table tr:last-child td {{
    border-bottom: none;
}}

table.data-table tr:nth-child(even) td {{
    background: #f8fafc;
}}

/* Post Card for Preview */
.post-card {{
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    overflow: hidden;
    display: flex;
    flex-direction: column;
}}

.post-card img {{
    width: 100%;
    height: 145px;
    object-fit: cover;
    border-bottom: 1px solid #e2e8f0;
}}

.post-body {{
    padding: 9px 11px;
    display: flex;
    flex-direction: column;
    gap: 4px;
}}

.post-body h4 {{
    margin: 0;
    font-size: 11.5px;
    font-weight: 700;
    color: #0f172a;
}}

.post-body p {{
    margin: 0;
    font-size: 10px;
    color: #475569;
    line-height: 1.35;
}}

/* Cover Page Specific Styles */
.cover-hero {{
    background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    padding: 26px 24px;
    position: relative;
    overflow: hidden;
}}

.cover-hero::before {{
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 6px;
    background: linear-gradient(90deg, #1e3a8a, #0284c7, #d97706);
}}

.cover-pillars {{
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 12px;
    margin-top: 14px;
}}

.pillar-box {{
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 14px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.03);
}}

.pillar-box h3 {{
    font-size: 13px;
    font-weight: 700;
    color: #0f172a;
    margin: 6px 0 4px 0;
}}

.pillar-box p {{
    font-size: 11px;
    color: #64748b;
    margin: 0;
    line-height: 1.4;
}}

</style>
</head>
<body>

<!-- PAGE 1: EXECUTIVE COVER -->
<div class="page">
    <div class="page-header" style="border-bottom: none; margin-bottom: 0;">
        <div class="header-brand">
            <img src="{logo_b64}" alt="Italsport Group">
        </div>
        <div class="header-badge">PIANO STRATEGICO SOCIAL & COMMERCIALE 2026</div>
    </div>

    <div class="page-content" style="justify-content: center; gap: 18px;">
        <div class="cover-hero">
            <div style="display: flex; gap: 8px; margin-bottom: 12px;">
                <span class="badge badge-navy">ITALSPORT GROUP • CISERANO (BG)</span>
                <span class="badge badge-blue">@ITALSPORTGROUP</span>
                <span class="badge badge-gold">30+ ANNI DI STORIA (DAL 1995)</span>
            </div>
            <h1 style="font-size: 31px; font-weight: 800; color: #0f172a; margin: 0 0 10px 0; line-height: 1.15; letter-spacing: -0.8px;">
                PIANO EDITORIALE INSTAGRAM E VALORIZZAZIONE SERVIZI CLUB
            </h1>
            <p style="font-size: 13.8px; color: #334155; margin: 0; max-width: 630px; line-height: 1.5;">
                Strategia social basata sulle vere foto di <b>@italsportgroup</b> e <b>italsport-group.it</b> per valorizzare i tre punti di forza unici di Italsport Ciserano (BG): il <b>Configuratore 3D a 360°</b>, la <b>Vetrina Dedicata con Password per ogni squadra</b> e la <b>Tessera Pro-Club</b>.
            </p>
        </div>

        <div class="cover-pillars">
            <div class="pillar-box" style="border-top: 3px solid #0284c7;">
                <span class="badge badge-blue">ASSET 01</span>
                <h3>Configuratore 3D a 360°</h3>
                <p>Permette alle società di disegnare la divisa online scegliendo modello, colori, colletto e sponsor e ruotandola in 3D a 360° prima dell'ordine.</p>
            </div>
            <div class="pillar-box" style="border-top: 3px solid #059669;">
                <span class="badge badge-green">ASSET 02</span>
                <h3>Vetrina Squadra con Password</h3>
                <p>Ogni squadra accede con una <b>password dedicata</b> su My Italsport e vede <b>solo i propri capi ufficiali</b>, ritrovando sempre le stesse cose senza errori.</p>
            </div>
            <div class="pillar-box" style="border-top: 3px solid #d97706;">
                <span class="badge badge-gold">ASSET 03</span>
                <h3>Tessera Pro-Club (4 Livelli)</h3>
                <p>Card Basic, Silver, Gold e Diamond: Italsport gestisce il magazzino a Ciserano (zero anticipi per il club), listino riservato e continuità negli anni.</p>
            </div>
        </div>

        <div class="card" style="background: #ffffff; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 14px 18px;">
            <div style="font-size: 11px; font-weight: 700; text-transform: uppercase; color: #64748b; letter-spacing: 0.5px; margin-bottom: 8px;">
                DATI AZIENDALI VERIFICATI — ITALSPORT GROUP
            </div>
            <div class="grid-4" style="font-size: 11.5px;">
                <div>
                    <div style="color: #64748b; font-size: 10px;">AZIENDA & SEDE</div>
                    <div style="font-weight: 700; color: #0f172a;">Italsport Group</div>
                    <div style="color: #475569; font-size: 10.5px;">Via Prov. Francesca 2H/I, Ciserano (BG)</div>
                </div>
                <div>
                    <div style="color: #64748b; font-size: 10px;">CONTATTI UFFICIALI</div>
                    <div style="font-weight: 700; color: #0f172a;">Tel. 035 4191221</div>
                    <div style="color: #475569; font-size: 10.5px;">Cell. 335 7001956 • info@italsport-group.it</div>
                </div>
                <div>
                    <div style="color: #64748b; font-size: 10px;">NUMERI CHIAVE</div>
                    <div style="font-weight: 700; color: #0f172a;">4.600+ Realtà in CRM</div>
                    <div style="color: #475569; font-size: 10.5px;">2.600 articoli attivi • 30 anni storia</div>
                </div>
                <div>
                    <div style="color: #64748b; font-size: 10px;">CANALI DIGITALI</div>
                    <div style="font-weight: 700; color: #0284c7;">@italsportgroup</div>
                    <div style="color: #475569; font-size: 10.5px;">italsport-group.it • store.italsport-group.it</div>
                </div>
            </div>
        </div>
    </div>

    <div class="page-footer">
        <span class="meta-left">ITALSPORT GROUP — CISERANO (BG) • P.IVA 01778490167</span>
        <span>PIANO STRATEGICO SOCIAL & VETRINA SQUADRE</span>
        <span class="page-number">Pagina 01 / 10</span>
    </div>
</div>

<!-- PAGE 2: ANALISI CONTESTO & DIFFERENZIAZIONE REALE -->
<div class="page">
    <div class="page-header">
        <div class="header-brand">
            <img src="{logo_b64}" alt="Italsport Group">
            <div class="header-title-box">
                <span class="header-category">ANALISI STRATEGICA</span>
                <span class="header-subtitle">Posizionamento di Italsport a Ciserano (BG) e in Lombardia</span>
            </div>
        </div>
        <div class="header-badge">CAPITOLO 01</div>
    </div>

    <div class="page-content">
        <h1 class="page-title">30 Anni di Forniture Sportive e Servizi su Misura per i Club</h1>
        <p class="page-intro">
            Con oltre 30 anni di esperienza a Ciserano — Loc. Zingonia (BG) e più di 4.600 realtà registrate tra società sportive, oratori, scuole, comuni e aziende, Italsport si distingue dai rivenditori generici perché risolve i veri problemi organizzativi dei club.
        </p>

        <div class="card-white" style="margin-bottom: 6px;">
            <div style="font-weight: 700; font-size: 12px; color: #0f172a; margin-bottom: 6px;">
                PERCHÉ LE SOCIETÀ SPORTIVE SCELGONO ITALSPORT GROUP
            </div>
            <table class="data-table">
                <thead>
                    <tr>
                        <th style="width: 24%;">Esigenza del Club</th>
                        <th style="width: 36%;">Fornitori Tradizionali / Cataloghi Standard</th>
                        <th style="width: 40%; background: #e0f2fe; color: #0369a1;">ITALSPORT GROUP — CISERANO (BG)</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><b>Vetrina Dedicata della Squadra</b></td>
                        <td>Cataloghi dispersivi con migliaia di prodotti dove si rischia di ordinare il modello o il colore sbagliato</td>
                        <td style="background: #f0f9ff;"><b>Vetrina Protetta con Password (My Italsport):</b> ogni squadra accede con la sua password e vede <b>SOLO i capi approvati per il proprio club</b>, trovando sempre le stesse cose senza errori</td>
                    </tr>
                    <tr>
                        <td><b>Continuità & Riassortimenti</b></td>
                        <td>Linee fuori produzione dopo una stagione; difficoltà a vestire i nuovi iscritti a metà anno</td>
                        <td style="background: #f0f9ff;"><b>Continuità Garantita negli Anni:</b> la linea della squadra resta codificata e riordinabile identica anche per singoli capi</td>
                    </tr>
                    <tr>
                        <td><b>Gestione Magazzino & Costi</b></td>
                        <td>La società deve anticipare il budget e tenere scatoloni di abbigliamento invenduto in sede</td>
                        <td style="background: #f0f9ff;"><b>Magazzino Gestito da Italsport a Ciserano:</b> facciamo noi da magazzino per il club, zero anticipi e zero rimanenze</td>
                    </tr>
                    <tr>
                        <td><b>Progettazione Divise & Fidelizzazione</b></td>
                        <td>Nessuna anteprima 3D; condizioni economiche variabili di anno in anno</td>
                        <td style="background: #f0f9ff;"><b>Configuratore 3D a 360°</b> + <b>Tessera Pro-Club</b> (Basic, Silver, Gold, Diamond) con listino bloccato e sconti dedicati</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div class="grid-2">
            <div class="card">
                <div style="font-weight: 700; font-size: 12px; color: #dc2626; margin-bottom: 4px;">
                    ⚠ COSA MIGLIORARE NELLA COMUNICAZIONE ATTUALE
                </div>
                <ul style="margin: 0; padding-left: 16px; font-size: 11px; color: #475569; display: flex; flex-direction: column; gap: 4px;">
                    <li>Passare da post solo "vetrina prodotto" a contenuti che spiegano i servizi unici per le società.</li>
                    <li>Far capire subito come funziona la <b>Vetrina con Password</b> (vedere solo i capi della propria squadra senza errori).</li>
                    <li>Mostrare in azione la rotazione a 360° della maglia nel Configuratore 3D.</li>
                    <li>Comunicare con chiarezza i 4 livelli della Tessera Pro-Club e lo showroom di Ciserano.</li>
                </ul>
            </div>

            <div class="card" style="background: #f0fdf4; border-color: #bbf7d0;">
                <div style="font-weight: 700; font-size: 12px; color: #15803d; margin-bottom: 4px;">
                    ★ GLI OBIETTIVI DEL PIANO (OTTOBRE – DICEMBRE)
                </div>
                <ul style="margin: 0; padding-left: 16px; font-size: 11px; color: #166534; display: flex; flex-direction: column; gap: 4px;">
                    <li>Usare esclusivamente le vere foto di <b>@italsportgroup</b> e del sito <b>italsport-group.it</b> migliorate nell'impaginazione.</li>
                    <li>Attirare nuove società sportive di Bergamo e della Lombardia verso il programma Pro-Club.</li>
                    <li>Spiegare la comodità della Vetrina Squadra con password per dirigenti e tesserati.</li>
                    <li>Promuovere lo showroom di Ciserano per le forniture invernali e i gadget natalizi.</li>
                </ul>
            </div>
        </div>
    </div>

    <div class="page-footer">
        <span class="meta-left">ITALSPORT GROUP — CISERANO (BG) • P.IVA 01778490167</span>
        <span>CAPITOLO 01: ANALISI & POSIZIONAMENTO</span>
        <span class="page-number">Pagina 02 / 10</span>
    </div>
</div>

<!-- PAGE 3: I 3 ASSET STRATEGICI DIFFERENZIANTI -->
<div class="page">
    <div class="page-header">
        <div class="header-brand">
            <img src="{logo_b64}" alt="Italsport Group">
            <div class="header-title-box">
                <span class="header-category">I 3 PILASTRI DA VALORIZZARE</span>
                <span class="header-subtitle">Vetrina con Password, Configuratore 3D a 360° e Tessera Pro-Club</span>
            </div>
        </div>
        <div class="header-badge">CAPITOLO 02</div>
    </div>

    <div class="page-content">
        <h1 class="page-title">I 3 Servizi Chiave al Centro della Comunicazione</h1>
        <p class="page-intro">
            Ecco come presentiamo in modo concreto, chiaro e realistico i tre strumenti che rendono Italsport il partner ideale per ogni società sportiva.
        </p>

        <!-- Card 1: Vetrina con Password My Italsport -->
        <div class="card-white" style="border-left: 4px solid #059669; padding: 12px 14px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                <div style="display: flex; align-items: center; gap: 8px;">
                    <span class="badge badge-green">PILASTRO 01 • FOCUS PRINCIPALE</span>
                    <h3 style="margin: 0; font-size: 13.5px; color: #0f172a; font-weight: 700;">
                        La Vetrina Personalizzata con Password per Ogni Squadra (My Italsport)
                    </h3>
                </div>
                <span style="font-size: 10px; color: #059669; font-weight: 600;">store.italsport-group.it</span>
            </div>
            <p style="font-size: 11.5px; color: #334155; margin: 0 0 6px 0; line-height: 1.4;">
                Cosa intendiamo per <b>Vetrina Personalizzata</b>? Ogni squadra (es. <i>U.S.D. Brevianese</i>, <i>A.S.D. Gessate</i>) ha una propria vetrina dedicata sul sito protetta da una <b>password riservata</b>. Accedendo con la password, la società o il tesserato <b>vede SOLO ed esclusivamente gli articoli relativi alla sua squadra</b>: in questo modo <b>troverà sicuramente sempre le stesse cose nel tempo senza problemi</b>, senza confondersi e senza errori di modello o colore.
            </p>
            <div class="grid-3" style="font-size: 10.5px; background: #f0fdf4; padding: 6px 10px; border-radius: 6px; border: 1px solid #bbf7d0;">
                <div><b>1. Accesso con Password:</b> vedi solo i capi approvati per la tua squadra</div>
                <div><b>2. Sempre le Stesse Cose:</b> linea bloccata e identica negli anni senza errori</div>
                <div><b>3. Zero Magazzino Club:</b> le scorte le tiene Italsport a Ciserano (BG)</div>
            </div>
        </div>

        <!-- Card 2: Configuratore 3D -->
        <div class="card-white" style="border-left: 4px solid #0284c7; padding: 12px 14px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                <div style="display: flex; align-items: center; gap: 8px;">
                    <span class="badge badge-blue">PILASTRO 02</span>
                    <h3 style="margin: 0; font-size: 13.5px; color: #0f172a; font-weight: 700;">
                        Il Configuratore 3D con Maglia Ruotabile a 360°
                    </h3>
                </div>
                <span style="font-size: 10px; color: #0284c7; font-weight: 600;">italsport-group.it</span>
            </div>
            <p style="font-size: 11.5px; color: #334155; margin: 0 0 6px 0; line-height: 1.4;">
                Sul sito <b>italsport-group.it</b> i dirigenti possono configurare la divisa in 3D scegliendo sport (calcio, volley, basket), modello, colori societari, colletto, numeri e loghi sponsor, vedendo la maglia 3D ruotare a 360° da ogni angolazione prima di confermare l'ordine.
            </p>
            <div class="grid-3" style="font-size: 10.5px; background: #f8fafc; padding: 6px 10px; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div><b>Rotazione 360° Reale:</b> vista fronte, retro, fianchi e maniche</div>
                <div><b>Personalizzazione Totale:</b> colori, colletti, numeri e sponsor del club</div>
                <div><b>Codifica Immediata:</b> una volta approvata, entra nella vetrina squadra</div>
            </div>
        </div>

        <!-- Card 3: Tessera Fedeltà PRO-CLUB -->
        <div class="card-white" style="border-left: 4px solid #d97706; padding: 12px 14px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                <div style="display: flex; align-items: center; gap: 8px;">
                    <span class="badge badge-gold">PILASTRO 03</span>
                    <h3 style="margin: 0; font-size: 13.5px; color: #0f172a; font-weight: 700;">
                        La Tessera Ufficiale "PRO-CLUB" (Basic, Silver, Gold, Diamond)
                    </h3>
                </div>
                <span style="font-size: 10px; color: #b45309; font-weight: 600;">4 Livelli di Partnership</span>
            </div>
            <p style="font-size: 11.5px; color: #334155; margin: 0 0 6px 0; line-height: 1.4;">
                Il programma fedeltà Pro-Club di Italsport premia le società sportive con 4 livelli di card (<b>Basic, Silver, Gold, Diamond</b>) fondati sui 4 pilastri aziendali: <b>Disponibilità</b> (magazzino gestito da Italsport), <b>Servizio</b>, <b>Qualità</b> e <b>Continuità</b> garantita nel tempo.
            </p>
            <div class="grid-3" style="font-size: 10.5px; background: #f8fafc; padding: 6px 10px; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div><b>Zero Costi Magazzino:</b> nessun anticipo su taglie invendute</div>
                <div><b>Listino e Sconti Riservati:</b> vantaggi crescenti per i 4 livelli</div>
                <div><b>Continuità Garantita:</b> riordini sempre disponibili negli anni</div>
            </div>
        </div>
    </div>

    <div class="page-footer">
        <span class="meta-left">ITALSPORT GROUP — CISERANO (BG) • P.IVA 01778490167</span>
        <span>CAPITOLO 02: VETRINA CON PASSWORD, 3D & PRO-CLUB</span>
        <span class="page-number">Pagina 03 / 10</span>
    </div>
</div>

<!-- PAGE 4: FOCUS APPROFONDITO SULLA VETRINA CON PASSWORD E TARGET -->
<div class="page">
    <div class="page-header">
        <div class="header-brand">
            <img src="{logo_b64}" alt="Italsport Group">
            <div class="header-title-box">
                <span class="header-category">FOCUS VETRINA SQUADRA & TARGET</span>
                <span class="header-subtitle">Come Funziona l'Accesso con Password per Ogni Società Sportiva</span>
            </div>
        </div>
        <div class="header-badge">CAPITOLO 03</div>
    </div>

    <div class="page-content">
        <h1 class="page-title">Come Funziona la Vetrina Dedicata con Password per Ogni Squadra</h1>
        <p class="page-intro">
            Il cuore del servizio My Italsport (`store.italsport-group.it`) è dare a ciascuna società sportiva uno spazio protetto da password dove esistono solo ed esclusivamente i capi scelti da quella squadra.
        </p>

        <div class="card-accent-blue" style="padding: 12px 14px;">
            <div style="font-weight: 800; font-size: 12px; color: #0f172a; margin-bottom: 8px;">
                IL FLUSSO IN 4 PASSI DELLA VETRINA PROTETTA DA PASSWORD
            </div>
            <div class="grid-4" style="font-size: 10.5px;">
                <div class="card-white">
                    <span class="badge badge-navy">PASSO 1</span>
                    <div style="font-weight: 700; margin: 5px 0 3px 0; color: #0f172a;">Scelta della Linea</div>
                    <div style="color: #475569;">La società sceglie con Italsport i propri capi ufficiali (es. Kit Gara, Tuta Rom, Giacca Scotland, Giubbotto Nepal, K-Way, Borsa).</div>
                </div>
                <div class="card-white">
                    <span class="badge badge-blue">PASSO 2</span>
                    <div style="font-weight: 700; margin: 5px 0 3px 0; color: #0f172a;">Password Dedicata</div>
                    <div style="color: #475569;">Italsport crea la vetrina riservata della squadra protetta da una <b>password esclusiva</b> consegnata al club.</div>
                </div>
                <div class="card-white">
                    <span class="badge badge-green">PASSO 3</span>
                    <div style="font-weight: 700; margin: 5px 0 3px 0; color: #0f172a;">Vedi Solo i Tuoi Capi</div>
                    <div style="color: #475569;">Chi entra con la password vede <b>SOLO le cose relative alla sua squadra</b>: impossibile sbagliare articolo, modello o colore.</div>
                </div>
                <div class="card-white">
                    <span class="badge badge-gold">PASSO 4</span>
                    <div style="font-weight: 700; margin: 5px 0 3px 0; color: #0f172a;">Sempre le Stesse Cose</div>
                    <div style="color: #475569;">Anche a distanza di mesi o anni, la squadra <b>ritrova sicuramente sempre gli stessi articoli</b> senza problemi, pronti a Ciserano.</div>
                </div>
            </div>
        </div>

        <div class="grid-3">
            <div class="card">
                <div style="font-weight: 700; font-size: 11.5px; color: #1e3a8a; margin-bottom: 4px;">
                    1. SOCIETÀ SPORTIVE & ORATORI
                </div>
                <div style="font-size: 10px; color: #0284c7; font-weight: 600; margin-bottom: 5px;">Presidenti, Direttivi e Segreterie</div>
                <p style="font-size: 10.5px; color: #475569; margin: 0; line-height: 1.35;">
                    <b>Vantaggio:</b> non devono anticipare budget per il magazzino né gestire rimanenze; hanno la certezza che tutti i tesserati vestano sempre la stessa linea ufficiale.
                </p>
            </div>
            <div class="card">
                <div style="font-weight: 700; font-size: 11.5px; color: #0f172a; margin-bottom: 4px;">
                    2. ATLETI, MISTER & FAMIGLIE
                </div>
                <div style="font-size: 10px; color: #059669; font-weight: 600; margin-bottom: 5px;">Utilizzatori della Vetrina</div>
                <p style="font-size: 10.5px; color: #475569; margin: 0; line-height: 1.35;">
                    <b>Vantaggio:</b> entrano con la password della propria squadra e trovano subito solo i capi del loro club, senza dubbi su quale modello o colore acquistare.
                </p>
            </div>
            <div class="card">
                <div style="font-weight: 700; font-size: 11.5px; color: #b45309; margin-bottom: 4px;">
                    3. SCUOLE, COMUNI & AZIENDE
                </div>
                <div style="font-size: 10px; color: #d97706; font-weight: 600; margin-bottom: 5px;">Forniture & Gadget Personalizzati</div>
                <p style="font-size: 10.5px; color: #475569; margin: 0; line-height: 1.35;">
                    <b>Vantaggio:</b> abbigliamento personalizzato con stampa o ricamo, felpe per istituti scolastici, divise da lavoro, borse, premi e gadget per eventi.
                </p>
            </div>
        </div>
    </div>

    <div class="page-footer">
        <span class="meta-left">ITALSPORT GROUP — CISERANO (BG) • P.IVA 01778490167</span>
        <span>CAPITOLO 03: VETRINA CON PASSWORD & TARGET</span>
        <span class="page-number">Pagina 04 / 10</span>
    </div>
</div>

<!-- PAGE 5: QUADRO SINOTTICO PIANO SOCIAL (7 POST OTTOBRE - DICEMBRE) -->
<div class="page">
    <div class="page-header">
        <div class="header-brand">
            <img src="{logo_b64}" alt="Italsport Group">
            <div class="header-title-box">
                <span class="header-category">STORYBOARD EDITORIALE (OTTOBRE – DICEMBRE)</span>
                <span class="header-subtitle">I 7 Post Realizzati con le Vere Foto di @italsportgroup e italsport-group.it</span>
            </div>
        </div>
        <div class="header-badge">CAPITOLO 04</div>
    </div>

    <div class="page-content">
        <h1 class="page-title">Calendario e Obiettivi dei 7 Post Instagram</h1>
        <p class="page-intro">
            Tutti i 7 post utilizzano esclusivamente vere fotografie dei capi, dei manichini, dello showroom di Ciserano e delle grafiche ufficiali di Italsport, impaginate in modo pulito e senza alcuna scritta sovrapposta.
        </p>

        <div class="card-white" style="padding: 6px;">
            <table class="data-table">
                <thead>
                    <tr>
                        <th style="width: 7%;">Post</th>
                        <th style="width: 18%;">Tema & Vera Foto Usata</th>
                        <th style="width: 13%;">Periodo</th>
                        <th style="width: 38%;">Messaggio Chiave & Contenuto Reale</th>
                        <th style="width: 24%;">Obiettivo & Call to Action</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><b>#1</b></td>
                        <td><b>Divise Custom & Qualità</b><br><span style="font-size: 9.5px; color: #64748b;">3 veri kit su manichino @italsportgroup</span></td>
                        <td><span class="badge badge-navy">Metà Ottobre</span></td>
                        <td>30 anni di forniture sportive a Ciserano (BG): stampa, ricamo e tessuti resistenti ai lavaggi ripetuti.</td>
                        <td><b>Presentazione Qualità:</b> Invito nello showroom di Via Prov. Francesca 2H/I.</td>
                    </tr>
                    <tr>
                        <td><b>#2</b></td>
                        <td><b>Configuratore 3D a 360°</b><br><span style="font-size: 9.5px; color: #64748b;">Vera maglia 3D + schermata sito</span></td>
                        <td><span class="badge badge-blue">Fine Ottobre</span></td>
                        <td>Disegna la divisa in 3D su italsport-group.it: scegli colori, colletto, numeri e sponsor e girala a 360° prima dell'ordine.</td>
                        <td><b>Prova Strumento 3D:</b> Link in bio al configuratore 3D e rotazione 360°.</td>
                    </tr>
                    <tr>
                        <td><b>#3</b></td>
                        <td><b>Tessera PRO-CLUB</b><br><span style="font-size: 9.5px; color: #64748b;">Vera Card Pro-Club + 4 livelli</span></td>
                        <td><span class="badge badge-gold">Inizio Novembre</span></td>
                        <td>I 4 livelli (Basic, Silver, Gold, Diamond): zero costi di magazzino per il club, listino riservato e continuità negli anni.</td>
                        <td><b>Fidelizzazione Club:</b> Contatto DM o 035 4191221 per convenzione.</td>
                    </tr>
                    <tr>
                        <td><b>#4</b></td>
                        <td><b>Continuità & Riordini</b><br><span style="font-size: 9.5px; color: #64748b;">Griglia 9 capi linea club @italsportgroup</span></td>
                        <td><span class="badge badge-green">Metà Novembre</span></td>
                        <td>Nuovo iscritto a metà stagione? Dal Kit Gara alla Tuta Rom, da Giacca Scotland a Giubbotto Nepal ritrovi la stessa linea.</td>
                        <td><b>Continuità Fornitura:</b> Rassicurare i direttivi sui riassortimenti futuri.</td>
                    </tr>
                    <tr>
                        <td><b>#5</b></td>
                        <td><b>Vetrina con Password</b><br><span style="font-size: 9.5px; color: #64748b;">Login Password + veri capi club</span></td>
                        <td><span class="badge badge-blue">Fine Novembre</span></td>
                        <td>Ogni squadra accede con la propria password dedicata e vede SOLO i propri capi: trova sempre le stesse cose senza errori.</td>
                        <td><b>Attivazione Vetrina:</b> Richiedi la vetrina con password per la tua società.</td>
                    </tr>
                    <tr>
                        <td><b>#6</b></td>
                        <td><b>Sul Campo con Voi</b><br><span style="font-size: 9.5px; color: #64748b;">Vera squadra con divise Italsport</span></td>
                        <td><span class="badge badge-gray">Inizio Dicembre</span></td>
                        <td>Oltre 4.600 realtà tra società sportive, oratori e scuole vestite da Italsport a Ciserano, Bergamo e in Lombardia.</td>
                        <td><b>Riprova Sociale:</b> Valorizzare la storicità e le squadre del territorio.</td>
                    </tr>
                    <tr>
                        <td><b>#7</b></td>
                        <td><b>Showroom & Fine Anno</b><br><span style="font-size: 9.5px; color: #64748b;">Vera foto showroom Ciserano + felpe</span></td>
                        <td><span class="badge badge-gold">Metà/Fine Dic.</span></td>
                        <td>Felpe invernali, giubbotti, borse e idee regalo col logo della squadra per le feste: passa in showroom a Ciserano!</td>
                        <td><b>Visite in Negozio:</b> Chiusura d'anno e ordini invernali / natalizi.</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>

    <div class="page-footer">
        <span class="meta-left">ITALSPORT GROUP — CISERANO (BG) • P.IVA 01778490167</span>
        <span>CAPITOLO 04: QUADRO SINOTTICO 7 POST</span>
        <span class="page-number">Pagina 05 / 10</span>
    </div>
</div>

<!-- PAGE 6: SCHEDE DETTAGLIATE POST 1, 2, 3 -->
<div class="page">
    <div class="page-header">
        <div class="header-brand">
            <img src="{logo_b64}" alt="Italsport Group">
            <div class="header-title-box">
                <span class="header-category">ANTEPRIMA POST ESECUTIVI (1/2)</span>
                <span class="header-subtitle">Post 1 (Divise Custom), Post 2 (Configuratore 3D) e Post 3 (Tessera Pro-Club)</span>
            </div>
        </div>
        <div class="header-badge">POST 1, 2, 3</div>
    </div>

    <div class="page-content">
        <h1 class="page-title">Schede Visive Post 1, 2 e 3 (Foto Reali Italsport)</h1>
        <p class="page-intro">
            Ecco i primi tre post realizzati con le vere fotografie dei manichini di `@italsportgroup`, la vera cattura a 360° del Configuratore 3D e la vera grafica della Tessera Pro-Club di `italsport-group.it`.
        </p>

        <div class="grid-3">
            <!-- POST 1 -->
            <div class="post-card">
                <img src="{post1_b64}" alt="Post 1">
                <div class="post-body">
                    <span class="badge badge-navy" style="align-self: flex-start;">POST 01 • PRODUZIONE CUSTOM</span>
                    <h4>Divise Personalizzate col Tuo Logo</h4>
                    <p><b>Copy:</b> «Da 30 anni vestiamo lo sport: dalla progettazione grafica alla personalizzazione con stampa e ricamo, realizziamo divise fatte per durare. Passa in showroom a Ciserano (Via Provinciale Francesca 2H/I).»</p>
                    <div style="font-size: 9.5px; color: #0284c7; font-weight: 600;">#italsportgroup #ciserano #bergamo #divisepersonalizzate</div>
                </div>
            </div>

            <!-- POST 2 -->
            <div class="post-card">
                <img src="{post2_b64}" alt="Post 2">
                <div class="post-body">
                    <span class="badge badge-blue" style="align-self: flex-start;">POST 02 • CONFIGURATORE 3D 360°</span>
                    <h4>Disegna la Divisa e Girala a 360°</h4>
                    <p><b>Copy:</b> «Vuoi vedere come sarà la divisa della tua squadra prima di ordinarla? Con il Configuratore 3D su italsport-group.it scegli modello, colori, colletto e sponsor e ruoti la maglia a 360°!»</p>
                    <div style="font-size: 9.5px; color: #0284c7; font-weight: 600;">#configuratore3d #italsportgroup #divisesportive #ciserano</div>
                </div>
            </div>

            <!-- POST 3 -->
            <div class="post-card">
                <img src="{post3_b64}" alt="Post 3">
                <div class="post-body">
                    <span class="badge badge-gold" style="align-self: flex-start;">POST 03 • TESSERA PRO-CLUB</span>
                    <h4>Card Pro-Club: Basic, Silver, Gold, Diamond</h4>
                    <p><b>Copy:</b> «Scopri la Tessera PRO-CLUB di Italsport: facciamo noi il magazzino a Ciserano per la tua società (zero anticipi e zero rimanenze), listino riservato, continuità negli anni e vetrina con password inclusa.»</p>
                    <div style="font-size: 9.5px; color: #b45309; font-weight: 600;">#tesseraproclub #proclub #italsportgroup #societasportive</div>
                </div>
            </div>
        </div>

        <div class="card" style="margin-top: 4px; padding: 10px 14px; background: #f8fafc;">
            <div style="font-weight: 700; font-size: 11px; color: #0f172a; margin-bottom: 2px;">
                PERCHÉ QUESTE IMMAGINI FUNZIONANO MEGLIO DELLE FOTO DI STOCK
            </div>
            <p style="font-size: 10.5px; color: #475569; margin: 0; line-height: 1.4;">
                Chi conosce Italsport a Ciserano riconosce immediatamente i veri capi su manichino del negozio, la vera interfaccia 3D del sito con la maglia che ruota fronte/retro e la vera grafica ufficiale della <b>Tessera Pro-Club</b>, con fascia tipografica chiara in basso che non copre mai i prodotti.
            </p>
        </div>
    </div>

    <div class="page-footer">
        <span class="meta-left">ITALSPORT GROUP — CISERANO (BG) • P.IVA 01778490167</span>
        <span>POST 1, 2, 3: DIVISE CUSTOM, 3D 360° & TESSERA PRO-CLUB</span>
        <span class="page-number">Pagina 06 / 10</span>
    </div>
</div>

<!-- PAGE 7: SCHEDE DETTAGLIATE POST 4, 5, 6, 7 -->
<div class="page">
    <div class="page-header">
        <div class="header-brand">
            <img src="{logo_b64}" alt="Italsport Group">
            <div class="header-title-box">
                <span class="header-category">ANTEPRIMA POST ESECUTIVI (2/2)</span>
                <span class="header-subtitle">Post 4 (Continuità), Post 5 (Vetrina con Password), Post 6 (Sul Campo) e Post 7 (Showroom)</span>
            </div>
        </div>
        <div class="header-badge">POST 4, 5, 6, 7</div>
    </div>

    <div class="page-content">
        <h1 class="page-title">Schede Visive Post 4, 5, 6 e 7 (Focus Vetrina con Password)</h1>
        <p class="page-intro">
            Questi quattro post mostrano la vera griglia dei 9 capi societari di Italsport, il funzionamento della <b>Vetrina Protetta con Password per ogni squadra</b>, le squadre in campo e il vero showroom di Ciserano.
        </p>

        <div class="grid-4">
            <!-- POST 4 -->
            <div class="post-card">
                <img src="{post4_b64}" alt="Post 4">
                <div class="post-body">
                    <span class="badge badge-green" style="align-self: flex-start;">POST 04 • CONTINUITÀ</span>
                    <h4>Ritrova Sempre la Stessa Linea</h4>
                    <p><b>Copy:</b> «Nuovo iscritto a metà stagione? Con Italsport ritrovi sempre la stessa linea: Tuta Rom, Giacca Scotland, Giubbotto Nepal, K-Way e Borsa Bauletto.»</p>
                    <div style="font-size: 9px; color: #0284c7;">#continuità #riassortimenti</div>
                </div>
            </div>

            <!-- POST 5 -->
            <div class="post-card">
                <img src="{post5_b64}" alt="Post 5">
                <div class="post-body">
                    <span class="badge badge-blue" style="align-self: flex-start;">POST 05 • PASSWORD CLUB</span>
                    <h4>Vetrina con Password Squadra</h4>
                    <p><b>Copy:</b> «Ogni squadra accede con la sua password su My Italsport e vede SOLO i propri capi ufficiali: ritrova sempre le stesse cose nel tempo senza errori!»</p>
                    <div style="font-size: 9px; color: #0284c7;">#myitalsport #vetrinasquadra</div>
                </div>
            </div>

            <!-- POST 6 -->
            <div class="post-card">
                <img src="{post6_b64}" alt="Post 6">
                <div class="post-body">
                    <span class="badge badge-gray" style="align-self: flex-start;">POST 06 • SUL CAMPO</span>
                    <h4>Oltre 4.600 Realtà Servite</h4>
                    <p><b>Copy:</b> «Oltre 4.600 realtà tra società sportive, oratori, scuole e aziende hanno scelto Italsport in 30 anni a Ciserano e in Lombardia.»</p>
                    <div style="font-size: 9px; color: #0284c7;">#sulcampoconvoi #italsportgroup</div>
                </div>
            </div>

            <!-- POST 7 -->
            <div class="post-card">
                <img src="{post7_b64}" alt="Post 7">
                <div class="post-body">
                    <span class="badge badge-gold" style="align-self: flex-start;">POST 07 • SHOWROOM BG</span>
                    <h4>Showroom Ciserano & Regali</h4>
                    <p><b>Copy:</b> «Tute, felpe, giubbotti e gadget col logo della tua squadra per le feste: passa nel nostro showroom a Ciserano (Via Prov. Francesca 2H/I).»</p>
                    <div style="font-size: 9px; color: #b45309;">#showroomciserano #buonefeste</div>
                </div>
            </div>
        </div>

        <div class="card-white" style="margin-top: 6px; padding: 12px 14px;">
            <div style="font-weight: 700; font-size: 11.5px; color: #0f172a; margin-bottom: 6px;">
                IL MESSAGGIO CHIAVE DEL POST 05: COSA SIGNIFICA "VETRINA PERSONALIZZATA PER OGNI SQUADRA"
            </div>
            <div class="grid-3" style="font-size: 10.5px;">
                <div style="background: #f0fdf4; border: 1px solid #bbf7d0; padding: 8px 10px; border-radius: 6px;">
                    <b style="color: #15803d;">1. Accesso Protetto con Password:</b> Ogni squadra ha la sua password riservata per entrare nella propria vetrina su `store.italsport-group.it`.
                </div>
                <div style="background: #f0fdf4; border: 1px solid #bbf7d0; padding: 8px 10px; border-radius: 6px;">
                    <b style="color: #15803d;">2. Vede Solo le Cose della Sua Squadra:</b> Dentro la vetrina ci sono solo i capi approvati per quel club, senza rischio di confondersi.
                </div>
                <div style="background: #f0fdf4; border: 1px solid #bbf7d0; padding: 8px 10px; border-radius: 6px;">
                    <b style="color: #15803d;">3. Trova Sempre le Stesse Cose:</b> Chi accede oggi o nei prossimi anni trova sicuramente sempre gli stessi articoli senza problemi.
                </div>
            </div>
        </div>
    </div>

    <div class="page-footer">
        <span class="meta-left">ITALSPORT GROUP — CISERANO (BG) • P.IVA 01778490167</span>
        <span>POST 4, 5, 6, 7: CONTINUITÀ, VETRINA PASSWORD & SHOWROOM</span>
        <span class="page-number">Pagina 07 / 10</span>
    </div>
</div>

<!-- PAGE 8: FORMAT VIDEO REELS & STORIES -->
<div class="page">
    <div class="page-header">
        <div class="header-brand">
            <img src="{logo_b64}" alt="Italsport Group">
            <div class="header-title-box">
                <span class="header-category">STRATEGIA VIDEO REELS & STORIES</span>
                <span class="header-subtitle">3 Video Semplici e Realistici da Realizzare a Ciserano</span>
            </div>
        </div>
        <div class="header-badge">CAPITOLO 05</div>
    </div>

    <div class="page-content">
        <h1 class="page-title">I 3 Format Video Reels & le Storie in Evidenza</h1>
        <p class="page-intro">
            Oltre ai 7 post del feed, proponiamo 3 Reel concreti e immediati che mostrano la maglia 3D mentre gira a 360°, l'accesso con password alla vetrina della squadra e l'esposizione reale nello showroom di Ciserano.
        </p>

        <div class="grid-3">
            <div class="card-white" style="border-top: 3px solid #0284c7;">
                <span class="badge badge-blue">REEL 01 • GIÀ PRONTO NEL MOCKUP</span>
                <h4 style="margin: 8px 0 4px 0; font-size: 12px; color: #0f172a;">Rotazione 3D a 360° della Divisa</h4>
                <p style="font-size: 10.5px; color: #475569; margin: 0 0 8px 0; line-height: 1.35;">
                    <b>Cosa si vede:</b> L'animazione reale a 360° estratta dal configuratore di `italsport-group.it` (`configuratore3d_real.gif`) dove la maglia personalizzata gira mostrando fronte, maniche, numero 27 e logo sul retro.
                </p>
                <div style="font-size: 10px; background: #f0f9ff; padding: 5px 8px; border-radius: 4px; color: #0369a1;">
                    <b>Testo in sovrimpressione:</b> «Configura la divisa in 3D e girala a 360° prima di ordinarla.»
                </div>
            </div>

            <div class="card-white" style="border-top: 3px solid #059669;">
                <span class="badge badge-green">REEL 02 • TUTORIAL CLUB</span>
                <h4 style="margin: 8px 0 4px 0; font-size: 12px; color: #0f172a;">Entrare con Password nella Vetrina Squadra</h4>
                <p style="font-size: 10.5px; color: #475569; margin: 0 0 8px 0; line-height: 1.35;">
                    <b>Cosa si vede:</b> Breve video dello schermo (25 secondi): si seleziona la società (es. <i>U.S.D. Brevianese</i> o <i>Gessate</i>), si inserisce la password dedicata e si apre la vetrina con i soli capi ufficiali della squadra.
                </p>
                <div style="font-size: 10px; background: #f0fdf4; padding: 5px 8px; border-radius: 4px; color: #15803d;">
                    <b>Testo in sovrimpressione:</b> «Una password per ogni squadra: vedi solo i tuoi capi e trovi sempre gli stessi.»
                </div>
            </div>

            <div class="card-white" style="border-top: 3px solid #d97706;">
                <span class="badge badge-gold">REEL 03 • SHOWROOM CISERANO</span>
                <h4 style="margin: 8px 0 4px 0; font-size: 12px; color: #0f172a;">Dentro lo Showroom di Via Prov. Francesca</h4>
                <p style="font-size: 10.5px; color: #475569; margin: 0 0 8px 0; line-height: 1.35;">
                    <b>Cosa si vede:</b> Panoramica reale dentro lo showroom di Ciserano tra i manichini vestiti con le divise custom, gli espositori di tute, borse, palloni e le pareti con le foto delle squadre locali.
                </p>
                <div style="font-size: 10px; background: #fefce8; padding: 5px 8px; border-radius: 4px; color: #b45309;">
                    <b>Testo in sovrimpressione:</b> «30 anni al fianco delle società sportive a Ciserano (BG).»
                </div>
            </div>
        </div>

        <div class="card" style="margin-top: 6px;">
            <div style="font-weight: 700; font-size: 12px; color: #0f172a; margin-bottom: 6px;">
                ORGANIZZAZIONE DELLE 6 STORIE IN EVIDENZA SU @ITALSPORTGROUP
            </div>
            <div class="grid-3" style="font-size: 10.5px;">
                <div class="card-white">
                    <b style="color: #0284c7;">1. Configuratore 3D:</b><br>
                    Animazione 360° della maglia + link diretto al configuratore su `italsport-group.it`.
                </div>
                <div class="card-white">
                    <b style="color: #059669;">2. Vetrina Club (Password):</b><br>
                    Come funziona l'accesso con password per vedere solo i capi della propria squadra.
                </div>
                <div class="card-white">
                    <b style="color: #d97706;">3. Tessera Pro-Club:</b><br>
                    I 4 livelli (Basic, Silver, Gold, Diamond) e il vantaggio zero magazzino.
                </div>
                <div class="card-white">
                    <b style="color: #0f172a;">4. Divise Custom:</b><br>
                    Le migliori realizzazioni per calcio, basket, volley e rappresentanza.
                </div>
                <div class="card-white">
                    <b style="color: #0f172a;">5. Showroom BG:</b><br>
                    Orari, mappa di Via Provinciale Francesca 2H/I a Ciserano e contatti rapidi.
                </div>
                <div class="card-white">
                    <b style="color: #0f172a;">6. Sul Campo:</b><br>
                    Repost delle società sportive del territorio taggate nel weekend.
                </div>
            </div>
        </div>
    </div>

    <div class="page-footer">
        <span class="meta-left">ITALSPORT GROUP — CISERANO (BG) • P.IVA 01778490167</span>
        <span>CAPITOLO 05: REELS & STORIE IN EVIDENZA</span>
        <span class="page-number">Pagina 08 / 10</span>
    </div>
</div>

<!-- PAGE 9: VALORIZZAZIONE TERRITORIALE & SINERGIA CRM (4.600 REALTÀ) -->
<div class="page">
    <div class="page-header">
        <div class="header-brand">
            <img src="{logo_b64}" alt="Italsport Group">
            <div class="header-title-box">
                <span class="header-category">PIANO COMMERCIALE LOCALE & CRM</span>
                <span class="header-subtitle">Attivazione delle 4.600 Realtà in Anagrafica e Sponsorizzazioni Locali</span>
            </div>
        </div>
        <div class="header-badge">CAPITOLO 06</div>
    </div>

    <div class="page-content">
        <h1 class="page-title">Sinergia tra Instagram, Showroom di Ciserano e le 4.600 Anagrafiche</h1>
        <p class="page-intro">
            Come emerso dall'analisi aziendale, Italsport dispone di un patrimonio unico: oltre 4.600 clienti registrati in 30 anni e una forte presenza territoriale tra Bergamo, Milano Est e tutta la Lombardia.
        </p>

        <div class="card-white" style="margin-bottom: 6px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <div style="font-weight: 700; font-size: 12px; color: #0f172a;">
                    AZIONE COMBINATA: SOCIAL LOCALE (RAGGIO 35 KM DA CISERANO) + CONTATTO DIRETTO
                </div>
                <span class="badge badge-green">BUDGET SOSTENIBILE E MIRATO</span>
            </div>
            <div class="grid-3" style="font-size: 11px;">
                <div class="card" style="border-left: 3px solid #059669;">
                    <b style="color: #15803d;">1. Attivazione Vetrine con Password</b><br>
                    Proporre a ogni società attiva l'apertura gratuita della propria <b>Vetrina con Password</b> su `store.italsport-group.it`, inviando via WhatsApp/Email la grafica del Post #5.
                </div>
                <div class="card" style="border-left: 3px solid #d97706;">
                    <b style="color: #b45309;">2. Campagna Tessera Pro-Club</b><br>
                    Sponsorizzazione geolocalizzata su Bergamo, Treviglio, Dalmine, Gessate e provincia rivolta a dirigenti sportivi e oratori con focus "Zero Magazzino per la Società".
                </div>
                <div class="card" style="border-left: 3px solid #0284c7;">
                    <b style="color: #0369a1;">3. Riattivazione Anagrafiche Storiche</b><br>
                    Usare i contenuti social sul <b>Configuratore 3D a 360°</b> e sui gadget invernali per ricontattare le società, le scuole e le aziende già presenti nel gestionale.
                </div>
            </div>
        </div>

        <div class="card">
            <div style="font-weight: 700; font-size: 12px; color: #0f172a; margin-bottom: 6px;">
                OBIETTIVI CONCRETI E MISURABILI (TRIMESTRE OTTOBRE – DICEMBRE)
            </div>
            <table class="data-table">
                <thead>
                    <tr>
                        <th>Area di Risultato</th>
                        <th>Punto di Partenza</th>
                        <th>Obiettivo Trimestrale Realistico</th>
                        <th>Beneficio Diretto per Italsport</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><b>Vetrine Squadra con Password Attive</b></td>
                        <td>Presenti sul portale ma poco comunicate sui social</td>
                        <td><b>+15 / 20 Squadre con Vetrina Attiva</b></td>
                        <td>Ordini e riassortimenti continui senza errori di articolo o colore</td>
                    </tr>
                    <tr>
                        <td><b>Adesioni Programma Tessera Pro-Club</b></td>
                        <td>Gestione tradizionale delle forniture</td>
                        <td><b>+12 / 15 Nuove Società Partner</b></td>
                        <td>Fidelizzazione pluriennale del club nei livelli Basic, Silver, Gold, Diamond</td>
                    </tr>
                    <tr>
                        <td><b>Utilizzo Configuratore 3D a 360°</b></td>
                        <td>Strumento attivo sul sito ma non spinto su IG</td>
                        <td><b>80+ Bozze Divisa Configurate</b></td>
                        <td>Riduzione dei tempi di preventivo e maggiore chiusura ordini</td>
                    </tr>
                    <tr>
                        <td><b>Visite in Showroom a Ciserano (BG)</b></td>
                        <td>Clientela storica e passaparola</td>
                        <td><b>Incremento visite direttivi e ordini Natale</b></td>
                        <td>Vendita di tute, giubbotti invernali, borse e gadget di fine anno</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>

    <div class="page-footer">
        <span class="meta-left">ITALSPORT GROUP — CISERANO (BG) • P.IVA 01778490167</span>
        <span>CAPITOLO 06: AZIONE TERRITORIALE & OBIETTIVI</span>
        <span class="page-number">Pagina 09 / 10</span>
    </div>
</div>

<!-- PAGE 10: ROADMAP OPERATIVA & RIEPILOGO ESECUTIVO -->
<div class="page">
    <div class="page-header">
        <div class="header-brand">
            <img src="{logo_b64}" alt="Italsport Group">
            <div class="header-title-box">
                <span class="header-category">PIANO DI AZIONE & RIEPILOGO FINALE</span>
                <span class="header-subtitle">Cronoprogramma Operativo da Ottobre al 31 Dicembre</span>
            </div>
        </div>
        <div class="header-badge">CAPITOLO 07</div>
    </div>

    <div class="page-content">
        <h1 class="page-title">Cronoprogramma Operativo (Ottobre – 31 Dicembre)</h1>
        <p class="page-intro">
            Un piano semplice, ordinato e immediatamente eseguibile che accompagna Italsport lungo tutto il trimestre autunnale e invernale fino alle festività di fine anno.
        </p>

        <div class="grid-4" style="margin-bottom: 4px;">
            <div class="card-white" style="border-top: 3px solid #0284c7;">
                <span class="badge badge-blue">FASE 1 • OTTOBRE</span>
                <h4 style="margin: 6px 0 2px 0; font-size: 11px;">Divise Custom & 3D</h4>
                <p style="font-size: 10px; color: #475569; margin: 0; line-height: 1.35;">
                    Aggiornamento bio `@italsportgroup`, pubblicazione <b>Post #1</b> (Divise Custom) e <b>Post #2 + Reel</b> (Configuratore 3D con rotazione a 360°).
                </p>
            </div>
            <div class="card-white" style="border-top: 3px solid #d97706;">
                <span class="badge badge-gold">FASE 2 • INIZIO NOV.</span>
                <h4 style="margin: 6px 0 2px 0; font-size: 11px;">Tessera Pro-Club & Linea</h4>
                <p style="font-size: 10px; color: #475569; margin: 0; line-height: 1.35;">
                    Pubblicazione <b>Post #3</b> (Tessera Pro-Club Basic, Silver, Gold, Diamond) e <b>Post #4</b> (Continuità e riassortimenti sulla linea club).
                </p>
            </div>
            <div class="card-white" style="border-top: 3px solid #059669;">
                <span class="badge badge-green">FASE 3 • FINE NOV.</span>
                <h4 style="margin: 6px 0 2px 0; font-size: 11px;">Vetrina con Password</h4>
                <p style="font-size: 10px; color: #475569; margin: 0; line-height: 1.35;">
                    Pubblicazione <b>Post #5</b> (Vetrina Squadra con Password su My Italsport) e <b>Post #6</b> (Oltre 4.600 realtà sul campo con Italsport).
                </p>
            </div>
            <div class="card-white" style="border-top: 3px solid #1e3a8a;">
                <span class="badge badge-navy">FASE 4 • DICEMBRE</span>
                <h4 style="margin: 6px 0 2px 0; font-size: 11px;">Showroom & Natale</h4>
                <p style="font-size: 10px; color: #475569; margin: 0; line-height: 1.35;">
                    Pubblicazione <b>Post #7</b> (Showroom Ciserano, abbigliamento invernale, felpe e gadget natalizi col logo della squadra).
                </p>
            </div>
        </div>

        <div class="card-accent-blue" style="padding: 12px 16px;">
            <div style="font-weight: 800; font-size: 12.5px; color: #0f172a; margin-bottom: 4px;">
                RIEPILOGO DEI PUNTI DI FORZA IMPLEMENTATI NEL PROGETTO
            </div>
            <div class="grid-3" style="font-size: 10.5px; color: #334155; margin-top: 6px;">
                <div><b>1. Solo Foto Reali Italsport:</b> tutte le immagini provengono da `@italsportgroup` e `italsport-group.it`, senza scritte tagliate o sovrapposte.</div>
                <div><b>2. Vetrina con Password Chiara:</b> spiegato e simulato come ogni squadra entra con la sua password e vede solo i propri capi, trovando sempre le stesse cose.</div>
                <div><b>3. Maglia 3D a 360° + Pro-Club:</b> inclusa la vera animazione 3D a 360° del configuratore e la vera Tessera Pro-Club a 4 livelli.</div>
            </div>
        </div>

        <div class="card" style="background: #ffffff; border: 1.5px solid #cbd5e1; padding: 10px 14px;">
            <div class="grid-2" style="align-items: center; font-size: 11px;">
                <div>
                    <div style="font-weight: 700; color: #0f172a; font-size: 12px;">ITALSPORT GROUP (Italsport di Locatelli Vincenzo)</div>
                    <div style="color: #475569;">Sede & Showroom: <b>Via Provinciale Francesca 2H/I — 24040 Ciserano, Loc. Zingonia (BG)</b></div>
                    <div style="color: #475569;">Tel. <b>035 4191221</b> • Cell. <b>335 7001956</b> • Email: <b>info@italsport-group.it</b> • P.IVA <b>01778490167</b></div>
                </div>
                <div style="text-align: right;">
                    <div style="font-weight: 700; color: #0284c7;">Siti Ufficiali: italsport-group.it | store.italsport-group.it</div>
                    <div style="color: #64748b; font-size: 10px;">Instagram: <b>@italsportgroup</b> • Facebook: <b>@GroupItalsport</b></div>
                </div>
            </div>
        </div>
    </div>

    <div class="page-footer">
        <span class="meta-left">ITALSPORT GROUP — CISERANO (BG) • P.IVA 01778490167</span>
        <span>CAPITOLO 07: CRONOPROGRAMMA & CONTATTI</span>
        <span class="page-number">Pagina 10 / 10</span>
    </div>
</div>

</body>
</html>
"""

with open("full_pdf_template.html", "w", encoding="utf-8") as f:
    f.write(html_pdf)

print(f"full_pdf_template.html written successfully ({len(html_pdf)} bytes).")
