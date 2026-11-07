import os, base64, subprocess, pymupdf

def get_b64(fname):
    if os.path.exists(fname):
        with open(fname, 'rb') as f:
            b64 = base64.b64encode(f.read()).decode('utf-8')
            ext = 'png' if fname.endswith('.png') else 'jpeg'
            return f"data:image/{ext};base64,{b64}"
    return ""

print("Encoding images for Tech Presentation...")
logo_b64 = get_b64("cropped-cropped-italsportlogo.png")
cfg_b64 = get_b64("site_configuratore.jpg")
portal_b64 = get_b64("site_membro_myitalsport.jpg")
fullprint_b64 = get_b64("store_full_print.jpg")
reparto_b64 = get_b64("store_reparto_grafico.jpg")
linea_b64 = get_b64("store_la_tua_linea.jpg")
partner_b64 = get_b64("store_partner_affidabile.jpg")
dtf_b64 = get_b64("store_dtf.jpg")
site_home_b64 = get_b64("site_homepage.png")

html = f"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<title>Italsport Group - Piano Strategico Ecosistema Digitale & Gestionale B2B 2026</title>
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
    padding: 8mm 14mm 7mm 14mm;
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
    padding-bottom: 6px;
    border-bottom: 1.5px solid #e2e8f0;
    margin-bottom: 7px;
    flex-shrink: 0;
}}

.header-left {{
    display: flex;
    align-items: center;
    gap: 14px;
}}

.header-logo {{
    height: 36px;
    width: auto;
    object-fit: contain;
}}

.header-title-box {{
    display: flex;
    flex-direction: column;
}}

.category-tag {{
    font-size: 8px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    color: #0284c7;
    margin-bottom: 1px;
}}

.slide-title {{
    font-size: 16px;
    font-weight: 800;
    color: #0f172a;
    margin: 0;
    line-height: 1.2;
    letter-spacing: -0.2px;
}}

.slide-subtitle {{
    font-size: 9.5px;
    color: #475569;
    margin: 1px 0 0 0;
    font-weight: 500;
}}

.chapter-badge {{
    background: #f1f5f9;
    border: 1px solid #cbd5e1;
    color: #334155;
    padding: 3.5px 9px;
    border-radius: 5px;
    font-size: 8px;
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
    justify-content: center;
    gap: 7px;
    min-height: 0;
}}

/* Slide Footer */
.slide-footer {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-top: 5px;
    border-top: 1px solid #e2e8f0;
    font-size: 8px;
    color: #64748b;
    font-weight: 600;
    flex-shrink: 0;
    margin-top: 5px;
}}

.footer-left {{
    display: flex;
    align-items: center;
    gap: 8px;
}}

.footer-pill {{
    background: #e0f2fe;
    color: #0369a1;
    padding: 2px 7px;
    border-radius: 4px;
    font-weight: 700;
    font-size: 7.5px;
}}

.slide-num {{
    background: #f1f5f9;
    border: 1px solid #cbd5e1;
    padding: 2px 7px;
    border-radius: 4px;
    color: #0f172a;
    font-weight: 700;
}}

/* Utility Cards & Grids */
.card {{
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 7px;
    padding: 9px 11px;
}}

.card-white {{
    background: #ffffff;
    border: 1px solid #cbd5e1;
    border-radius: 7px;
    padding: 9px 11px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.03);
}}

.card-blue {{
    background: #f0f7ff;
    border: 1px solid #bfdbfe;
    border-radius: 7px;
    padding: 9px 11px;
}}

.card-green {{
    background: #f0fdf4;
    border: 1px solid #bbf7d0;
    border-radius: 7px;
    padding: 9px 11px;
}}

.card-gold {{
    background: #fffbeb;
    border: 1px solid #fde68a;
    border-radius: 7px;
    padding: 9px 11px;
}}

.grid-2 {{ display: grid; grid-template-columns: 1fr 1fr; gap: 9px; }}
.grid-3 {{ display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 9px; }}
.grid-4 {{ display: grid; grid-template-columns: 1fr 1fr 1fr 1fr; gap: 8px; }}
.grid-5 {{ display: grid; grid-template-columns: repeat(5, 1fr); gap: 7px; }}
.grid-2-3 {{ display: grid; grid-template-columns: 2fr 3fr; gap: 10px; }}
.grid-3-2 {{ display: grid; grid-template-columns: 3fr 2fr; gap: 10px; }}

.pill {{
    display: inline-block;
    padding: 1.5px 6px;
    border-radius: 3px;
    font-size: 7.5px;
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
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    padding: 6px 8px;
    text-align: center;
}}
.stat-val {{
    font-size: 15px;
    font-weight: 800;
    color: #0284c7;
    line-height: 1.1;
}}
.stat-lbl {{
    font-size: 7.5px;
    color: #64748b;
    font-weight: 600;
    text-transform: uppercase;
    margin-top: 1px;
}}

/* Tables */
table.deck-table {{
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    font-size: 9px;
    border: 1px solid #cbd5e1;
    border-radius: 6px;
    overflow: hidden;
}}
table.deck-table th {{
    background: #f1f5f9;
    color: #0f172a;
    font-weight: 700;
    padding: 5px 7px;
    text-align: left;
    border-bottom: 1px solid #cbd5e1;
    font-size: 8.5px;
    text-transform: uppercase;
    letter-spacing: 0.4px;
}}
table.deck-table td {{
    padding: 5px 7px;
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
</style>
</head>
<body>

<!-- SLIDE 1: COVER TECH -->
<div class="slide" style="background: linear-gradient(135deg, #0f172a 0%, #0369a1 100%); color: #ffffff;">
    <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.15); padding-bottom: 10px;">
        <div style="background: #ffffff; padding: 6px 14px; border-radius: 8px; display: inline-flex; align-items: center;">
            <img src="{logo_b64}" style="height: 38px; width: auto;" alt="Italsport Logo">
        </div>
        <div style="display: flex; gap: 8px;">
            <span style="background: rgba(255,255,255,0.15); color: #ffffff; font-size: 9px; font-weight: 700; padding: 4px 10px; border-radius: 5px; text-transform: uppercase; letter-spacing: 0.5px;">PROPOSTA TECNICO-COMMERCIALE 2026/2027</span>
            <span style="background: #10b981; color: #ffffff; font-size: 9px; font-weight: 700; padding: 4px 10px; border-radius: 5px; text-transform: uppercase;">CONFIDENZIALE</span>
        </div>
    </div>

    <div style="display: flex; flex-direction: column; gap: 10px; margin: 15px 0;">
        <div style="font-size: 11px; font-weight: 700; color: #38bdf8; text-transform: uppercase; letter-spacing: 1.5px;">
            ITALSPORT GROUP S.R.L. • RIORGANIZZAZIONE INFRASTRUTTURA IT & COMMERCIALE
        </div>
        <h1 style="font-size: 30px; font-weight: 800; line-height: 1.15; margin: 0; color: #ffffff; letter-spacing: -0.5px;">
            PIANO STRATEGICO DI EVOLUZIONE DIGITALE,<br>GESTIONALE ERP & E-COMMERCE B2B
        </h1>
        <p style="font-size: 12px; color: #cbd5e1; max-width: 850px; margin: 0; line-height: 1.45;">
            Analisi delle esigenze operative, benchmark software gestionale, architettura integrata di magazzino/produzione e soluzione ad alta sicurezza per la custodia dell'archivio tecnico aziendale.
        </p>

        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px; margin-top: 8px;">
            <div style="background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.15); border-radius: 8px; padding: 9px 12px;">
                <span class="pill pill-blue" style="margin-bottom: 4px;">CARDINE 01</span>
                <div style="font-size: 11px; font-weight: 700; color: #ffffff;">Ecosistema ERP Unificato</div>
                <div style="font-size: 8.5px; color: #94a3b8; margin-top: 2px;">Centralizzazione real-time di contabilità ordinaria, giacenze magazzino e distinte base.</div>
            </div>
            <div style="background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.15); border-radius: 8px; padding: 9px 12px;">
                <span class="pill pill-green" style="margin-bottom: 4px;">CARDINE 02</span>
                <div style="font-size: 11px; font-weight: 700; color: #ffffff;">Vetrine B2B per Società</div>
                <div style="font-size: 8.5px; color: #94a3b8; margin-top: 2px;">Aree riservate con catalogo e listino dedicato: ordini atleti autonomi e zero contanti.</div>
            </div>
            <div style="background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.15); border-radius: 8px; padding: 9px 12px;">
                <span class="pill pill-gold" style="margin-bottom: 4px;">CARDINE 03</span>
                <div style="font-size: 11px; font-weight: 700; color: #ffffff;">NAS Locale & Protezione Dati</div>
                <div style="font-size: 8.5px; color: #94a3b8; margin-top: 2px;">Archivio ad altissima velocità locale per file grafici pesanti, backup sicuro e zero canoni cloud.</div>
            </div>
        </div>
    </div>

    <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid rgba(255,255,255,0.15); padding-top: 8px; font-size: 8.5px; color: #94a3b8;">
        <div><b>COMMITTENTE:</b> Italsport Group S.r.l. (Via Ugo La Malfa, 56 — Palermo)</div>
        <div><b>DESTINATARI:</b> Proprietà & Direzione Amministrativa</div>
        <div><b>VERSIONE:</b> 2.0 Executive Deck • Novembre 2026</div>
        <div><span style="background: rgba(255,255,255,0.2); padding: 2px 8px; border-radius: 4px; color: #fff; font-weight: 700;">SLIDE 01 / 10</span></div>
    </div>
</div>

<!-- SLIDE 2: EXECUTIVE SUMMARY & DIAGNOSI -->
<div class="slide">
    <div class="slide-header">
        <div class="header-left">
            <img src="{logo_b64}" class="header-logo" alt="Italsport Logo">
            <div class="header-title-box">
                <span class="category-tag">DIAGNOSI AZIENDALE & SCENARIO</span>
                <h2 class="slide-title">Executive Summary: Superare la Frammentazione dei Sistemi</h2>
                <p class="slide-subtitle">Unificare l'infrastruttura software per abbattere i costi, tutelare la contabilità e velocizzare la produzione.</p>
            </div>
        </div>
        <div class="header-right">
            <span class="chapter-badge">CAPITOLO 01 | DIAGNOSI</span>
        </div>
    </div>

    <div class="slide-body">
        <div class="grid-3">
            <div class="card" style="border-top: 3px solid #ef4444;">
                <span class="pill" style="background: #fee2e2; color: #b91c1c;">SITUAZIONE ATTUALE</span>
                <div style="font-size: 11px; font-weight: 800; color: #0f172a; margin: 4px 0 2px 0;">Ecosistema IT Frammentato</div>
                <div style="font-size: 8.5px; color: #475569; line-height: 1.4;">
                    Attualmente l'azienda opera con sistemi separati: <b>TeamSystem Alyante</b> per la contabilità, <b>PrestaShop</b> per il web, un configuratore 3D esterno e un CRM isolato con circa 1.600 clienti. Database non sincronizzati che costringono a doppie registrazioni manuali e rischio di disallineamento giacenze.
                </div>
            </div>

            <div class="card" style="border-top: 3px solid #f59e0b;">
                <span class="pill pill-gold">LE PRESSIONI DEL MOMENTO</span>
                <div style="font-size: 11px; font-weight: 800; color: #0f172a; margin: 4px 0 2px 0;">Scadenze & Costi Fuori Scala</div>
                <div style="font-size: 8.5px; color: #475569; line-height: 1.4;">
                    Cambi dirigenziali del fornitore storico e scadenza fiscale di gennaio impongono decisioni rapide. I preventivi esterni per nuovi ERP tradizionali (es. Odoo con fornitori terzi) toccano cifre proibitive (<b>25.000 € – 35.000 €</b>) con tariffe orarie di assistenza fino a <b>60 € / ora</b> (gonfiate a 300 € ad intervento).
                </div>
            </div>

            <div class="card-green" style="border-top: 3px solid #10b981;">
                <span class="pill pill-green">LA NOSTRA RISPOSTA</span>
                <div style="font-size: 11px; font-weight: 800; color: #0f172a; margin: 4px 0 2px 0;">Approccio Modulare a Tappe</div>
                <div style="font-size: 8.5px; color: #334155; line-height: 1.4;">
                    Nessun salto nel buio: verifichiamo la tenuta fiscale e la distinta base in ambiente controllato, presidiando la scadenza di gennaio. Proponiamo un modello di consulenza e partnership trasparente che <b>taglia oltre il 60% dei costi di implementazione</b> e forma le risorse interne dell'azienda.
                </div>
            </div>
        </div>

        <div class="grid-4" style="margin-top: 2px;">
            <div class="stat-box">
                <div class="stat-val">&gt; 60%</div>
                <div class="stat-lbl">Risparmio sui Preventivi Tradizionali</div>
            </div>
            <div class="stat-box">
                <div class="stat-val">1.600</div>
                <div class="stat-lbl">Aziende e Società Sportive nel CRM</div>
            </div>
            <div class="stat-box">
                <div class="stat-val">2.000+</div>
                <div class="stat-lbl">Articoli Attivi a Catalogo</div>
            </div>
            <div class="stat-box">
                <div class="stat-val">GEN 2027</div>
                <div class="stat-lbl">Scadenza Fiscale Presidiata</div>
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <div class="footer-left">
            <span class="footer-pill">ITALSPORT GROUP S.R.L.</span>
            <span>PIANO STRATEGICO GESTIONALE & IT 2026/2027</span>
        </div>
        <div>CAPITOLO 01: DIAGNOSI AZIENDALE</div>
        <div class="slide-num">Slide 02 / 10</div>
    </div>
</div>

<!-- SLIDE 3: 5 NON-NEGOTIABLE REQUIREMENTS -->
<div class="slide">
    <div class="slide-header">
        <div class="header-left">
            <img src="{logo_b64}" class="header-logo" alt="Italsport Logo">
            <div class="header-title-box">
                <span class="category-tag">ANALISI REQUISITI CHIAVE</span>
                <h2 class="slide-title">I 5 Requisiti Aziendali Irrinunciabili per Italsport</h2>
                <p class="slide-subtitle">I vincoli tecnici, fiscali e produttivi che qualsiasi soluzione adottata deve garantire al 100%.</p>
            </div>
        </div>
        <div class="header-right">
            <span class="chapter-badge">CAPITOLO 01 | REQUISITI</span>
        </div>
    </div>

    <div class="slide-body">
        <div class="grid-5">
            <!-- REQ 1 -->
            <div class="card-white" style="border-top: 3px solid #0284c7; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <span class="pill pill-blue">REQUISITO 01</span>
                    <div style="font-size: 10px; font-weight: 800; color: #0f172a; margin: 3px 0 2px 0;">Piattaforma Unica Real-Time</div>
                    <div style="font-size: 8px; color: #475569; line-height: 1.35;">
                        Eliminare database multipli: ogni vendita su web o negozio fisico deve aggiornare istantaneamente scorte, impegni di magazzino e scritture contabili.
                    </div>
                </div>
                <div style="font-size: 7.5px; font-weight: 700; color: #0284c7; margin-top: 4px;">• Zero doppi inserimenti</div>
            </div>

            <!-- REQ 2 -->
            <div class="card-white" style="border-top: 3px solid #10b981; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <span class="pill pill-green">REQUISITO 02</span>
                    <div style="font-size: 10px; font-weight: 800; color: #0f172a; margin: 3px 0 2px 0;">Regime Fiscale Ordinario</div>
                    <div style="font-size: 8px; color: #475569; line-height: 1.35;">
                        Gestione contabile completa: piano dei conti italiano, fatturazione elettronica SDI, collegamento al cassetto fiscale e carico/scarico automatico a fattura.
                    </div>
                </div>
                <div style="font-size: 7.5px; font-weight: 700; color: #16a34a; margin-top: 4px;">• Conformità SDI 100%</div>
            </div>

            <!-- REQ 3 -->
            <div class="card-white" style="border-top: 3px solid #f59e0b; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <span class="pill pill-gold">REQUISITO 03</span>
                    <div style="font-size: 10px; font-weight: 800; color: #0f172a; margin: 3px 0 2px 0;">Distinta Base di Produzione</div>
                    <div style="font-size: 8px; color: #475569; line-height: 1.35;">
                        Per capi personalizzati: distinta base multilivello (tessuto, carta transfer, calandra, cucitura), calcolo tempi/costi e monitoraggio avanzamento commessa.
                    </div>
                </div>
                <div style="font-size: 7.5px; font-weight: 700; color: #d97706; margin-top: 4px;">• Tracciabilità fabbrica</div>
            </div>

            <!-- REQ 4 -->
            <div class="card-white" style="border-top: 3px solid #8b5cf6; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <span class="pill pill-purple">REQUISITO 04</span>
                    <div style="font-size: 10px; font-weight: 800; color: #0f172a; margin: 3px 0 2px 0;">Catalogo Padre-Figlio</div>
                    <div style="font-size: 8px; color: #475569; line-height: 1.35;">
                        Gestione matrici complesse con centinaia di migliaia di varianti taglia/colore, sovrapprezzi taglia (es. XXL > M) e listini parametrici per volume o club.
                    </div>
                </div>
                <div style="font-size: 7.5px; font-weight: 700; color: #9333ea; margin-top: 4px;">• Listini personalizzati</div>
            </div>

            <!-- REQ 5 -->
            <div class="card-white" style="border-top: 3px solid #0284c7; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <span class="pill pill-blue">REQUISITO 05</span>
                    <div style="font-size: 10px; font-weight: 800; color: #0f172a; margin: 3px 0 2px 0;">Vetrine Club Blindate</div>
                    <div style="font-size: 8px; color: #475569; line-height: 1.35;">
                        Aree B2B riservate per ciascuna società convenzionata: visualizzazione esclusiva dei capi sociali approvati e stato ordine per singolo atleta.
                    </div>
                </div>
                <div style="font-size: 7.5px; font-weight: 700; color: #0284c7; margin-top: 4px;">• E-commerce Club My Italsport</div>
            </div>
        </div>

        <div class="card" style="background: #f8fafc; padding: 7px 11px; margin-top: 2px;">
            <div style="font-size: 8px; color: #334155;">
                <b>Vincolo Fondamentale Condiviso con la Proprietà:</b> Qualsiasi piattaforma o percorso adottato NON potrà essere messo in produzione se non supera il collaudo pratico su questi 5 requisiti, con particolare riguardo alla quadratura contabile e alla gestione distinta base.
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <div class="footer-left">
            <span class="footer-pill">ITALSPORT GROUP S.R.L.</span>
            <span>PIANO STRATEGICO GESTIONALE & IT 2026/2027</span>
        </div>
        <div>CAPITOLO 01: I 5 REQUISITI IRRINUNCIABILI</div>
        <div class="slide-num">Slide 03 / 10</div>
    </div>
</div>

<!-- SLIDE 4: BENCHMARK DELLE 3 STRADE -->
<div class="slide">
    <div class="slide-header">
        <div class="header-left">
            <img src="{logo_b64}" class="header-logo" alt="Italsport Logo">
            <div class="header-title-box">
                <span class="category-tag">BENCHMARK TECNOLOGICO & SOFTWARE</span>
                <h2 class="slide-title">Analisi Comparativa delle Soluzioni Gestionali</h2>
                <p class="slide-subtitle">Valutazione oggettiva di costi, tempi di implementazione e rischi operativi tra le 3 opzioni possibili.</p>
            </div>
        </div>
        <div class="header-right">
            <span class="chapter-badge">CAPITOLO 02 | BENCHMARK</span>
        </div>
    </div>

    <div class="slide-body">
        <div class="grid-3">
            <!-- OPTION A -->
            <div class="card-white" style="border-top: 3px solid #64748b; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span class="pill pill-slate">OPZIONE A • PONTE</span>
                        <span style="font-size: 8px; font-weight: 700; color: #475569;">€ 3.000 – 4.000</span>
                    </div>
                    <div style="font-size: 11px; font-weight: 800; color: #0f172a; margin: 4px 0 2px 0;">Mantenimento Alyante + Sito</div>
                    <p style="font-size: 8px; color: #475569; line-height: 1.35; margin: 0 0 6px 0;">
                        Tamponare il gestionale attuale TeamSystem per superare la scadenza di gennaio, mantenendo PrestaShop e i connettori attuali.
                    </p>
                    <div style="font-size: 8px; color: #334155; line-height: 1.3;">
                        <div><b>Vantaggi:</b> Nessun impatto immediato sui processi contabili consolidati.</div>
                        <div style="margin-top: 3px;"><b>Limiti:</b> Resta la frammentazione; connettori fragili e costosi; tariffe orarie pesanti del fornitore; non risolve i problemi del web.</div>
                    </div>
                </div>
                <div style="background: #f1f5f9; padding: 4px 6px; border-radius: 4px; font-size: 7.5px; font-weight: 700; color: #475569; text-align: center; margin-top: 6px;">
                    VERDETTO: Utile solo per prendere tempo verso la transizione.
                </div>
            </div>

            <!-- OPTION B -->
            <div class="card-green" style="border-top: 3px solid #10b981; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span class="pill pill-green">OPZIONE B • CONSIGLIATA</span>
                        <span style="font-size: 8px; font-weight: 700; color: #15803d;">CANONI MODULARI</span>
                    </div>
                    <div style="font-size: 11px; font-weight: 800; color: #0f172a; margin: 4px 0 2px 0;">Piattaforma Integrata Moderna</div>
                    <p style="font-size: 8px; color: #334155; line-height: 1.35; margin: 0 0 6px 0;">
                        Transizione a ERP modulare cloud nativo (es. Odoo assistito / Shopify B2B + motore fiscale certificato italiano Danea/SDI).
                    </p>
                    <div style="font-size: 8px; color: #334155; line-height: 1.3;">
                        <div><b>Vantaggi:</b> Gestionale ed e-commerce condividono lo stesso database; vetrine club native; aggiornamenti fiscali inclusi; interfaccia moderna.</div>
                        <div style="margin-top: 3px;"><b>Pianificazione:</b> Richiede migrazione guidata dello storico dati (clienti e catalogo).</div>
                    </div>
                </div>
                <div style="background: #dcfce7; padding: 4px 6px; border-radius: 4px; font-size: 7.5px; font-weight: 700; color: #166534; text-align: center; margin-top: 6px;">
                    VERDETTO: Scelta strategica con il miglior ROI e longevità.
                </div>
            </div>

            <!-- OPTION C -->
            <div class="card-white" style="border-top: 3px solid #ef4444; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span class="pill" style="background: #fee2e2; color: #b91c1c;">OPZIONE C • SCONSIGLIATA</span>
                        <span style="font-size: 8px; font-weight: 700; color: #b91c1c;">&gt; € 40.000</span>
                    </div>
                    <div style="font-size: 11px; font-weight: 800; color: #0f172a; margin: 4px 0 2px 0;">Software Custom da Zero</div>
                    <p style="font-size: 8px; color: #475569; line-height: 1.35; margin: 0 0 6px 0;">
                        Sviluppare un software gestionale ed e-commerce proprietario interamente su misura tramite team di programmatori dedicati.
                    </p>
                    <div style="font-size: 8px; color: #334155; line-height: 1.3;">
                        <div><b>Vantaggi:</b> Totale libertà grafica e logica su misura.</div>
                        <div style="margin-top: 3px;"><b>Limiti:</b> Tempi lunghissimi (6-12 mesi); costi enormi; forte dipendenza dagli sviluppatori; obbligo di programmare a pagamento ogni cambio fiscale.</div>
                    </div>
                </div>
                <div style="background: #fee2e2; padding: 4px 6px; border-radius: 4px; font-size: 7.5px; font-weight: 700; color: #991b1b; text-align: center; margin-top: 6px;">
                    VERDETTO: Fortemente sconsigliata per rischi e costi.
                </div>
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <div class="footer-left">
            <span class="footer-pill">ITALSPORT GROUP S.R.L.</span>
            <span>PIANO STRATEGICO GESTIONALE & IT 2026/2027</span>
        </div>
        <div>CAPITOLO 02: BENCHMARK GESTIONALI A CONFRONTO</div>
        <div class="slide-num">Slide 04 / 10</div>
    </div>
</div>

<!-- SLIDE 5: TARGET ARCHITECTURE -->
<div class="slide">
    <div class="slide-header">
        <div class="header-left">
            <img src="{logo_b64}" class="header-logo" alt="Italsport Logo">
            <div class="header-title-box">
                <span class="category-tag">ARCHITETTURA APPLICATIVA INTEGRATA</span>
                <h2 class="slide-title">L'Architettura Target Integrata per Italsport Group</h2>
                <p class="slide-subtitle">Un flusso continuo di dati in tempo reale tra canali web, motore gestionale centrale e produzione in fabbrica.</p>
            </div>
        </div>
        <div class="header-right">
            <span class="chapter-badge">CAPITOLO 02 | ARCHITETTURA</span>
        </div>
    </div>

    <div class="slide-body">
        <div style="display: flex; flex-direction: column; gap: 8px;">
            <!-- TIER 1: FRONT END -->
            <div class="card-white" style="border-left: 3px solid #0284c7; padding: 7px 10px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                    <span style="font-size: 9px; font-weight: 800; color: #0284c7; text-transform: uppercase;">LIVELLO 1: FRONT-END & CANALI DI VENDITA DIGITALI</span>
                    <span class="pill pill-blue">CANALI ESTERNI</span>
                </div>
                <div class="grid-3" style="font-size: 8px;">
                    <div style="background: #f8fafc; padding: 4px 7px; border-radius: 4px; border: 1px solid #e2e8f0;">
                        <b>Store Istituzionale & Retail</b><br><span style="color: #64748b;">Catalogo pubblico e vendite dirette al dettaglio</span>
                    </div>
                    <div style="background: #f0fdf4; padding: 4px 7px; border-radius: 4px; border: 1px solid #bbf7d0;">
                        <b>Vetrine B2B Riservate My Italsport</b><br><span style="color: #15803d;">Aree protette club per ordini famiglie e atleti</span>
                    </div>
                    <div style="background: #f0f7ff; padding: 4px 7px; border-radius: 4px; border: 1px solid #bfdbfe;">
                        <b>Configuratore 3D Vettoriale Live</b><br><span style="color: #0369a1;">Simulatore divise e generazione bozza grafica</span>
                    </div>
                </div>
            </div>

            <!-- TIER 2: CORE ERP -->
            <div class="card-blue" style="border-left: 3px solid #0369a1; padding: 8px 10px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 5px;">
                    <span style="font-size: 9px; font-weight: 800; color: #0369a1; text-transform: uppercase;">LIVELLO 2: MOTORE CENTRALE GESTIONALE ERP (REAL-TIME CORE)</span>
                    <span class="pill pill-blue">DATABASE UNIFICATO</span>
                </div>
                <div class="grid-4" style="font-size: 8px;">
                    <div style="background: #ffffff; padding: 5px 7px; border-radius: 4px; border: 1px solid #cbd5e1;">
                        <b>Magazzino & Scorte</b><br><span style="color: #475569;">Giacenze sincronizzate, lotti e varianti padre/figlio</span>
                    </div>
                    <div style="background: #ffffff; padding: 5px 7px; border-radius: 4px; border: 1px solid #cbd5e1;">
                        <b>Commesse & Distinta Base</b><br><span style="color: #475569;">Lancio produzione, consumo tessuto e tempi sartoria</span>
                    </div>
                    <div style="background: #ffffff; padding: 5px 7px; border-radius: 4px; border: 1px solid #cbd5e1;">
                        <b>Contabilità Ordinaria SDI</b><br><span style="color: #475569;">Fatture elettroniche, cassetto fiscale e scadenziario</span>
                    </div>
                    <div style="background: #ffffff; padding: 5px 7px; border-radius: 4px; border: 1px solid #cbd5e1;">
                        <b>CRM Unificato B2B</b><br><span style="color: #475569;">Anagrafiche 1.600 club, accordi e storico forniture</span>
                    </div>
                </div>
            </div>

            <!-- TIER 3: PRODUCTION & NAS -->
            <div class="card-white" style="border-left: 3px solid #10b981; padding: 7px 10px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                    <span style="font-size: 9px; font-weight: 800; color: #16a34a; text-transform: uppercase;">LIVELLO 3: REPARTO PRODUTTIVO & ARCHIVIO DATI PROTETTO (PALERMO)</span>
                    <span class="pill pill-green">INFRASTRUTTURA ON-PREMISE</span>
                </div>
                <div class="grid-3" style="font-size: 8px;">
                    <div style="background: #f0fdf4; padding: 4px 7px; border-radius: 4px; border: 1px solid #bbf7d0;">
                        <b>NAS Locale Aziendale</b><br><span style="color: #166534;">Archivio ad altissima velocità per gigabyte di file grafici (.AI, .PSD)</span>
                    </div>
                    <div style="background: #f8fafc; padding: 4px 7px; border-radius: 4px; border: 1px solid #e2e8f0;">
                        <b>Plotter & Calandra 200°C</b><br><span style="color: #475569;">Stampa a sublimazione diretta e trasferimento transfer</span>
                    </div>
                    <div style="background: #f8fafc; padding: 4px 7px; border-radius: 4px; border: 1px solid #e2e8f0;">
                        <b>Confezione & Spedizioni</b><br><span style="color: #475569;">Cucitura sartoriale, controllo qualità e kit nominativi per atleta</span>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <div class="footer-left">
            <span class="footer-pill">ITALSPORT GROUP S.R.L.</span>
            <span>PIANO STRATEGICO GESTIONALE & IT 2026/2027</span>
        </div>
        <div>CAPITOLO 02: ARCHITETTURA APPLICATIVA TARGET</div>
        <div class="slide-num">Slide 05 / 10</div>
    </div>
</div>

<!-- SLIDE 6: LOCAL NAS INFRASTRUCTURE & SECURITY -->
<div class="slide">
    <div class="slide-header">
        <div class="header-left">
            <img src="{logo_b64}" class="header-logo" alt="Italsport Logo">
            <div class="header-title-box">
                <span class="category-tag">INFRASTRUTTURA IT & SICUREZZA DATI</span>
                <h2 class="slide-title">Protezione dell'Archivio Storico: La Soluzione NAS Locale Dedicato</h2>
                <p class="slide-subtitle">Velocità Gigabit per i grafici, totale riservatezza aziendale e abbattimento dei canoni cloud commerciali.</p>
            </div>
        </div>
        <div class="header-right">
            <span class="chapter-badge">CAPITOLO 03 | ARCHIVIO NAS</span>
        </div>
    </div>

    <div class="slide-body">
        <div class="grid-2">
            <!-- LEFT: THE NEED -->
            <div class="card" style="display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <span class="pill pill-slate">LA SPECIFICITÀ IT DI ITALSPORT</span>
                    <div style="font-size: 11px; font-weight: 800; color: #0f172a; margin: 4px 0 3px 0;">30 Anni di File Grafici Pesanti</div>
                    <p style="font-size: 8.5px; color: #475569; line-height: 1.4; margin: 0 0 6px 0;">
                        Italsport custodisce un patrimonio enorme di file vettoriali di produzione (.AI, .EPS, .PSD, matrici per calandra da centinaia di megabyte ciascuna). Affidarsi esclusivamente a servizi cloud commerciali esterni (Drive, Dropbox) comporta due gravi limiti:
                    </p>
                    <div style="font-size: 8px; color: #334155; line-height: 1.35;">
                        <div>• <b>Rallentamenti operativi:</b> il download continuo di file da 300-500 MB blocca il lavoro dei grafici.</div>
                        <div style="margin-top: 3px;">• <b>Costi e dipendenza:</b> canoni mensili crescenti per i terabyte di spazio e rischi di privacy sui disegni industriali.</div>
                    </div>
                </div>
                <div style="border-top: 1px solid #cbd5e1; padding-top: 5px; margin-top: 6px; font-size: 8px; color: #0284c7; font-weight: 700;">
                    LA RISPOSTA: Un server NAS on-premise in sede a Palermo affiancato da snapshot di backup.
                </div>
            </div>

            <!-- RIGHT: THE 4 NAS PILLARS -->
            <div style="display: flex; flex-direction: column; gap: 5px;">
                <div class="card-white" style="border-left: 3px solid #0284c7; padding: 5px 8px;">
                    <div style="font-size: 8.5px; font-weight: 800; color: #0284c7;">1. Velocità Locale di Rete Gigabit (1.000 Mbps)</div>
                    <div style="font-size: 7.5px; color: #475569;">Apertura istantanea dei file di stampa direttamente dai computer del reparto grafico: zero tempi di upload.</div>
                </div>

                <div class="card-white" style="border-left: 3px solid #10b981; padding: 5px 8px;">
                    <div style="font-size: 8.5px; font-weight: 800; color: #16a34a;">2. Riservatezza Totale & Proprietà Fisica del Dato</div>
                    <div style="font-size: 7.5px; color: #475569;">I dati dei clienti, i loghi societari e i documenti contabili restano fisicamente nei locali aziendali a Palermo.</div>
                </div>

                <div class="card-white" style="border-left: 3px solid #f59e0b; padding: 5px 8px;">
                    <div style="font-size: 8.5px; font-weight: 800; color: #d97706;">3. Ridondanza RAID & Protezione da Guasti</div>
                    <div style="font-size: 7.5px; color: #475569;">Dischi ridondati in mirroring/RAID: se un disco si guasta, nessun dato viene perso e la produzione non si ferma.</div>
                </div>

                <div class="card-white" style="border-left: 3px solid #8b5cf6; padding: 5px 8px;">
                    <div style="font-size: 8.5px; font-weight: 800; color: #9333ea;">4. Zero Canoni Mensili Ricorrenti</div>
                    <div style="font-size: 7.5px; color: #475569;">Investimento hardware una tantum (es. Synology/QNAP con dischi enterprise IronWolf/WD Red) che dura anni senza abbonamenti.</div>
                </div>
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <div class="footer-left">
            <span class="footer-pill">ITALSPORT GROUP S.R.L.</span>
            <span>PIANO STRATEGICO GESTIONALE & IT 2026/2027</span>
        </div>
        <div>CAPITOLO 03: SICUREZZA IT & ARCHIVIO NAS</div>
        <div class="slide-num">Slide 06 / 10</div>
    </div>
</div>

<!-- SLIDE 7: DATA MIGRATION PLAN -->
<div class="slide">
    <div class="slide-header">
        <div class="header-left">
            <img src="{logo_b64}" class="header-logo" alt="Italsport Logo">
            <div class="header-title-box">
                <span class="category-tag">MIGRAZIONE & BONIFICA DATI</span>
                <h2 class="slide-title">Piano di Bonifica & Migrazione Dati Senza Rischi</h2>
                <p class="slide-subtitle">I 4 passaggi per trasferire e normalizzare 1.600 anagrafiche e oltre 2.000 articoli attivi senza bloccare l'operatività.</p>
            </div>
        </div>
        <div class="header-right">
            <span class="chapter-badge">CAPITOLO 03 | MIGRAZIONE</span>
        </div>
    </div>

    <div class="slide-body">
        <div class="grid-4">
            <div class="card-white" style="border-top: 3px solid #0284c7;">
                <span class="pill pill-blue">STEP 01</span>
                <div style="font-size: 10px; font-weight: 800; color: #0f172a; margin: 3px 0 2px 0;">Estrazione Strutturata</div>
                <div style="font-size: 8px; color: #475569; line-height: 1.35;">
                    Estrazione completa da Alyante TeamSystem e CRM dello storico vendite ultimi 2-3 anni: anagrafiche, contatti e listini club concordati.
                </div>
                <div style="font-size: 7.5px; font-weight: 700; color: #0284c7; margin-top: 4px;">• Export CSV/Excel certificato</div>
            </div>

            <div class="card-white" style="border-top: 3px solid #10b981;">
                <span class="pill pill-green">STEP 02</span>
                <div style="font-size: 10px; font-weight: 800; color: #0f172a; margin: 3px 0 2px 0;">Bonifica & Pulizia</div>
                <div style="font-size: 8px; color: #475569; line-height: 1.35;">
                    Filtraggio degli articoli obsoleti (isolando i 2.000 attivi sugli 8.650 totali), normalizzazione codici fiscali, PEC e standardizzazione varianti.
                </div>
                <div style="font-size: 7.5px; font-weight: 700; color: #16a34a; margin-top: 4px;">• Eliminazione duplicati e refusi</div>
            </div>

            <div class="card-white" style="border-top: 3px solid #f59e0b;">
                <span class="pill pill-gold">STEP 03</span>
                <div style="font-size: 10px; font-weight: 800; color: #0f172a; margin: 3px 0 2px 0;">Caricamento Guidato</div>
                <div style="font-size: 8px; color: #475569; line-height: 1.35;">
                    Importazione nel nuovo ambiente ERP, configurazione matrici padre-figlio e attivazione dei listini parametrici per ogni società sportiva.
                </div>
                <div style="font-size: 7.5px; font-weight: 700; color: #d97706; margin-top: 4px;">• Allineamento listini club</div>
            </div>

            <div class="card-white" style="border-top: 3px solid #8b5cf6;">
                <span class="pill pill-purple">STEP 04</span>
                <div style="font-size: 10px; font-weight: 800; color: #0f172a; margin: 3px 0 2px 0;">Allineamento Parallelo</div>
                <div style="font-size: 8px; color: #475569; line-height: 1.35;">
                    Periodo di collaudo con doppio controllo prima del distacco definitivo: le forniture delle divise continuano regolarmente senza alcun fermo macchina.
                </div>
                <div style="font-size: 7.5px; font-weight: 700; color: #9333ea; margin-top: 4px;">• Zero interruzioni operative</div>
            </div>
        </div>

        <div class="card" style="background: #f0fdf4; border: 1px solid #bbf7d0; padding: 7px 11px; margin-top: 2px;">
            <div style="font-size: 8px; color: #166534;">
                <b>Garanzia di Continuità Aziendale:</b> La migrazione viene svolta a blocchi logici. Alyante continuerà a garantire la regolare emissione delle fatture e delle consegne fino a quando il nuovo sistema non sarà validato al 100% dalla direzione amministrativa di Italsport.
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <div class="footer-left">
            <span class="footer-pill">ITALSPORT GROUP S.R.L.</span>
            <span>PIANO STRATEGICO GESTIONALE & IT 2026/2027</span>
        </div>
        <div>CAPITOLO 03: MIGRAZIONE & BONIFICA DATI</div>
        <div class="slide-num">Slide 07 / 10</div>
    </div>
</div>

<!-- SLIDE 8: FINANCIAL PLAN & COST OPTIMIZATION -->
<div class="slide">
    <div class="slide-header">
        <div class="header-left">
            <img src="{logo_b64}" class="header-logo" alt="Italsport Logo">
            <div class="header-title-box">
                <span class="category-tag">ANALISI ECONOMICA & TRASPARENZA COSTI</span>
                <h2 class="slide-title">Piano Economico: Un Risparmio Reale di Oltre il 60% sul Budget</h2>
                <p class="slide-subtitle">Superare i preventivi sproporzionati dei grandi integratori software attraverso un modello collaborativo e sostenibile.</p>
            </div>
        </div>
        <div class="header-right">
            <span class="chapter-badge">CAPITOLO 04 | COSTI & RISPARMIO</span>
        </div>
    </div>

    <div class="slide-body">
        <div class="grid-2">
            <!-- TRADITIONAL -->
            <div class="card" style="border-top: 3px solid #ef4444; background: #fffaf0;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span class="pill" style="background: #fee2e2; color: #b91c1c;">FORNITORI TRADIZIONALI ESTERNI</span>
                    <span style="font-size: 9px; font-weight: 800; color: #b91c1c;">€ 25.000 – 35.000</span>
                </div>
                <div style="font-size: 11px; font-weight: 800; color: #0f172a; margin: 4px 0 3px 0;">Il Modello "A Pacchetto Chiuso"</div>
                <div style="font-size: 8px; color: #475569; line-height: 1.35;">
                    <div>• <b>Costo iniziale sproporzionato:</b> preventivi da 25k-35k € che drenano la liquidità aziendale.</div>
                    <div style="margin-top: 3px;">• <b>Tariffe orarie gonfiate:</b> fatturazione a 60 €/ora che spesso si trasforma in forfait da 300 € per semplici chiarimenti tecnici.</div>
                    <div style="margin-top: 3px;">• <b>Lock-in contrattuale:</b> l'azienda rimane dipendente da tecnici esterni senza internalizzare competenze.</div>
                </div>
            </div>

            <!-- OUR PROPOSAL -->
            <div class="card-green" style="border-top: 3px solid #10b981;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span class="pill pill-green">IL NOSTRO MODELLO DI PARTNERSHIP</span>
                    <span style="font-size: 9px; font-weight: 800; color: #15803d;">TAGLIO COSTI &gt; 60%</span>
                </div>
                <div style="font-size: 11px; font-weight: 800; color: #0f172a; margin: 4px 0 3px 0;">Consulenza & Affiancamento Interno</div>
                <div style="font-size: 8px; color: #334155; line-height: 1.35;">
                    <div>• <b>Investimento frazionato:</b> costi legati solo agli stati di avanzamento verificati.</div>
                    <div style="margin-top: 3px;">• <b>Canoni software trasparenti:</b> piattaforme moderne con costi certi e aggiornamenti fiscali inclusi.</div>
                    <div style="margin-top: 3px;">• <b>Valorizzazione risorse interne:</b> affiancamento formativo sul campo (es. Martina in apprendistato) per rendere il team Italsport autonomo.</div>
                </div>
            </div>
        </div>

        <div class="card-white" style="margin-top: 2px; padding: 7px 11px;">
            <div class="grid-3" style="font-size: 8.5px; text-align: center;">
                <div>
                    <div style="font-weight: 700; color: #64748b;">PREVENTIVO ESTERNO CLASSICO:</div>
                    <div style="font-size: 14px; font-weight: 800; color: #dc2626; margin-top: 1px;">€ 30.000 + canoni</div>
                </div>
                <div>
                    <div style="font-weight: 700; color: #64748b;">RISPARMIO NETTO PER ITALSPORT:</div>
                    <div style="font-size: 14px; font-weight: 800; color: #16a34a; margin-top: 1px;">&gt; € 18.000 risparmiati</div>
                </div>
                <div>
                    <div style="font-weight: 700; color: #64748b;">DESTINAZIONE RISORSE:</div>
                    <div style="font-size: 11px; font-weight: 700; color: #0284c7; margin-top: 2px;">Crescita commerciale e social</div>
                </div>
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <div class="footer-left">
            <span class="footer-pill">ITALSPORT GROUP S.R.L.</span>
            <span>PIANO STRATEGICO GESTIONALE & IT 2026/2027</span>
        </div>
        <div>CAPITOLO 04: TRASPARENZA COSTI & RISPARMIO</div>
        <div class="slide-num">Slide 08 / 10</div>
    </div>
</div>

<!-- SLIDE 9: IMPLEMENTATION ROADMAP -->
<div class="slide">
    <div class="slide-header">
        <div class="header-left">
            <img src="{logo_b64}" class="header-logo" alt="Italsport Logo">
            <div class="header-title-box">
                <span class="category-tag">ROADMAP DI IMPLEMENTAZIONE</span>
                <h2 class="slide-title">Cronoprogramma di Riorganizzazione: Da Novembre a Marzo</h2>
                <p class="slide-subtitle">Una tabella di marcia pragmatica che presidia la scadenza fiscale di gennaio e guida l'avvio a tappe.</p>
            </div>
        </div>
        <div class="header-right">
            <span class="chapter-badge">CAPITOLO 05 | CRONOPROGRAMMA</span>
        </div>
    </div>

    <div class="slide-body">
        <div class="grid-4">
            <div class="card-white" style="border-top: 3px solid #0284c7;">
                <span class="pill pill-blue">NOVEMBRE 2026</span>
                <div style="font-size: 10px; font-weight: 800; color: #0f172a; margin: 3px 0 2px 0;">Demo & Verifica Fiscale</div>
                <div style="font-size: 8px; color: #475569; line-height: 1.35;">
                    Dimostrazione pratica del cassetto fiscale, fattura SDI e distinte base; installazione e configurazione del NAS locale a Palermo.
                </div>
            </div>

            <div class="card-white" style="border-top: 3px solid #10b981;">
                <span class="pill pill-green">DICEMBRE 2026</span>
                <div style="font-size: 10px; font-weight: 800; color: #0f172a; margin: 3px 0 2px 0;">Bonifica & Setup Ambiente</div>
                <div style="font-size: 8px; color: #475569; line-height: 1.35;">
                    Estrazione anagrafiche Alyante (1.600 clienti, 2.000 articoli attivi); setup ambiente di test e attivazione prime 3 vetrine club pilota.
                </div>
            </div>

            <div class="card-white" style="border-top: 3px solid #f59e0b;">
                <span class="pill pill-gold">GENNAIO 2027</span>
                <div style="font-size: 10px; font-weight: 800; color: #0f172a; margin: 3px 0 2px 0;">Presidio Fiscale & Parallelo</div>
                <div style="font-size: 8px; color: #475569; line-height: 1.35;">
                    Gestione guidata della scadenza fiscale annuale; avvio parallelo del magazzino e collaudo flusso fatturazione elettronica.
                </div>
            </div>

            <div class="card-white" style="border-top: 3px solid #8b5cf6;">
                <span class="pill pill-purple">FEB – MARZO 2027</span>
                <div style="font-size: 10px; font-weight: 800; color: #0f172a; margin: 3px 0 2px 0;">Go-Live & Formazione</div>
                <div style="font-size: 8px; color: #475569; line-height: 1.35;">
                    Rilascio completo della piattaforma, formazione operativa del personale interno su distinte base e vetrine e-commerce club.
                </div>
            </div>
        </div>

        <div class="card" style="background: #f8fafc; padding: 7px 11px; margin-top: 2px;">
            <div style="font-size: 8px; color: #334155;">
                <b>Flessibilità Contrattuale:</b> Le fasi sono modulate per non interferire con i picchi di lavoro della produzione. Ogni avanzamento viene approvato congiuntamente con la proprietà prima di procedere allo step successivo.
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <div class="footer-left">
            <span class="footer-pill">ITALSPORT GROUP S.R.L.</span>
            <span>PIANO STRATEGICO GESTIONALE & IT 2026/2027</span>
        </div>
        <div>CAPITOLO 05: CRONOPROGRAMMA DI ESECUZIONE</div>
        <div class="slide-num">Slide 09 / 10</div>
    </div>
</div>

<!-- SLIDE 10: NEXT STEPS & PARTNERSHIP -->
<div class="slide">
    <div class="slide-header">
        <div class="header-left">
            <img src="{logo_b64}" class="header-logo" alt="Italsport Logo">
            <div class="header-title-box">
                <span class="category-tag">SINTESI DELLA PARTNERSHIP & AZIONI IMMEDIATE</span>
                <h2 class="slide-title">Prossimi Passi Operativi e Proposta di Incontro</h2>
                <p class="slide-subtitle">Costruire una partnership duratura fondata sulla trasparenza, sul controllo dei costi e sui risultati sul campo.</p>
            </div>
        </div>
        <div class="header-right">
            <span class="chapter-badge">CAPITOLO 05 | PROSSIMI PASSI</span>
        </div>
    </div>

    <div class="slide-body">
        <div class="grid-3">
            <div class="card-white" style="border-top: 3px solid #0284c7;">
                <div style="font-size: 9px; font-weight: 800; color: #0284c7; text-transform: uppercase;">STEP 1 • ENTRO 7 GIORNI</div>
                <div style="font-size: 11px; font-weight: 800; color: #0f172a; margin: 3px 0 2px 0;">Sessione Demo Operativa</div>
                <div style="font-size: 8px; color: #475569; line-height: 1.35;">
                    Incontro tecnico (di persona o da remoto) per dimostrare dal vivo la tenuta della contabilità ordinaria, del cassetto fiscale e della distinta base.
                </div>
            </div>

            <div class="card-white" style="border-top: 3px solid #10b981;">
                <div style="font-size: 9px; font-weight: 800; color: #16a34a; text-transform: uppercase;">STEP 2 • ENTRO 14 GIORNI</div>
                <div style="font-size: 11px; font-weight: 800; color: #0f172a; margin: 3px 0 2px 0;">Audit Dati & Campionatura</div>
                <div style="font-size: 8px; color: #475569; line-height: 1.35;">
                    Estrazione campione di 50 articoli e 20 anagrafiche per verificare la compatibilità della struttura padre-figlio e preparare lo script di bonifica.
                </div>
            </div>

            <div class="card-white" style="border-top: 3px solid #f59e0b;">
                <div style="font-size: 9px; font-weight: 800; color: #d97706; text-transform: uppercase;">STEP 3 • AVVIO IMMEDIATO</div>
                <div style="font-size: 11px; font-weight: 800; color: #0f172a; margin: 3px 0 2px 0;">Attivazione Canale Social</div>
                <div style="font-size: 8px; color: #475569; line-height: 1.35;">
                    Lanciare contestualmente la presenza su Instagram e il Configuratore 3D per generare nuovi contratti con società sportive mentre si prepara la transizione IT.
                </div>
            </div>
        </div>

        <div class="card" style="background: #f0f7ff; border: 1px solid #bfdbfe; padding: 7px 11px;">
            <div style="font-size: 8.5px; font-weight: 800; color: #0369a1; text-transform: uppercase;">LA NOSTRA PROMESSA DI PARTNERSHIP:</div>
            <div class="grid-3" style="font-size: 8px; color: #334155; margin-top: 3px;">
                <div><b>1. Nessuna Teoria Astratta:</b> solo soluzioni collaudate e direttamente applicabili ai processi del settore tessile sportivo.</div>
                <div><b>2. Controllo Rigoroso dei Costi:</b> totale trasparenza su licenze, tempi e attività di sviluppo.</div>
                <div><b>3. Presenza al Vostro Fianco:</b> affiancamento costante alla segreteria e alla direzione fino a piena autonomia.</div>
            </div>
        </div>

        <div class="card-white" style="padding: 7px 11px; margin-top: 1px;">
            <div class="grid-2" style="align-items: center; font-size: 8.5px;">
                <div>
                    <div style="font-weight: 800; color: #0f172a; font-size: 9.5px;">ITALSPORT GROUP S.R.L.</div>
                    <div style="color: #475569;">Sede & Stabilimento: Via Ugo La Malfa, 56 — 90146 Palermo (PA)</div>
                    <div style="color: #475569;">Sito Istituzionale: <b>italsport-group.it</b> | Store: <b>store.italsport-group.it</b></div>
                </div>
                <div style="text-align: right;">
                    <div style="font-weight: 800; color: #0284c7;">Consulenza Strategica Sistemi IT & Digital B2B</div>
                    <div style="color: #64748b; font-size: 8px;">Documento riservato predisposto per la Proprietà • Anno 2026/2027</div>
                </div>
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <div class="footer-left">
            <span class="footer-pill">ITALSPORT GROUP S.R.L.</span>
            <span>PIANO STRATEGICO GESTIONALE & IT 2026/2027</span>
        </div>
        <div>CAPITOLO 05: SINTESI PARTNERSHIP & PROSSIMI PASSI</div>
        <div class="slide-num">Slide 10 / 10</div>
    </div>
</div>

</body>
</html>
"""

html_path = os.path.abspath('full_pdf_template_tech.html')
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"full_pdf_template_tech.html written successfully ({len(html)} bytes).")

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
pdf_path = os.path.abspath('Proposta_Ecosistema_Digitale_Italsport_2026.pdf')

cmd = [
    chrome, '--headless=new', '--disable-gpu', '--no-sandbox', '--no-pdf-header-footer',
    f'--print-to-pdf={pdf_path}', f'file:///{html_path.replace(os.sep, "/")}'
]
res = subprocess.run(cmd, capture_output=True, text=True)
print("Chrome output:", res.stderr.strip() or res.stdout.strip())

doc = pymupdf.open(pdf_path)
print(f"Generated Proposta_Ecosistema_Digitale_Italsport_2026.pdf: {len(doc)} pages, size: {os.path.getsize(pdf_path)} bytes")
for i, page in enumerate(doc):
    print(f"Slide {i+1}: {page.rect.width:.2f} x {page.rect.height:.2f}")

# Render slides to scratch for inspection
out_dir = r'C:\Users\salvo\.gemini\antigravity\brain\d9f75e76-e15f-416d-9381-da9c50a6061e\scratch'
for i, page in enumerate(doc):
    pix = page.get_pixmap(dpi=130)
    pix.save(os.path.join(out_dir, f'tech_slide_{i+1}.png'))
print("Rendered all 10 tech slides to scratch!")
