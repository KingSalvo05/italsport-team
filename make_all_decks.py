import os, base64, subprocess, pymupdf, shutil, zipfile

def get_b64(fname):
    if os.path.exists(fname):
        with open(fname, 'rb') as f:
            b64 = base64.b64encode(f.read()).decode('utf-8')
            ext = 'png' if fname.endswith('.png') else 'jpeg'
            return f"data:image/{ext};base64,{b64}"
    return ""

print("Encoding real Italsport Ciserano (BG) images for Tech & Master Decks...")
logo_b64 = get_b64("cropped-cropped-italsportlogo.png")
post1_b64 = get_b64("img_post1_jersey.jpg")
post2_b64 = get_b64("img_post2_3d.jpg")
post3_b64 = get_b64("img_post3_fidelity.jpg")
post4_b64 = get_b64("img_post4_stack.jpg")
post5_b64 = get_b64("img_post5_portal.jpg")
post6_b64 = get_b64("img_post6_winter.jpg")
post7_b64 = get_b64("img_post7_celebration.jpg")
shw_b64 = get_b64("real_showroom_ciserano.jpg")

css_common = """<style>
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
</style>"""

print("Building Tech Presentation HTML (Ciserano BG)...")

tech_slides = [
    # Slide 1: Cover Tech (Light Corporate Executive)
    f"""<div class="slide" style="background: linear-gradient(135deg, #ffffff 0%, #f0f9ff 60%, #f0fdf4 100%); color: #0f172a; border-top: 6px solid #0284c7;">
    <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1.5px solid #cbd5e1; padding-bottom: 10px;">
        <div style="display: inline-flex; align-items: center; gap: 12px;">
            <img src="{logo_b64}" style="height: 42px; width: auto;" alt="Italsport Logo">
            <span style="font-size: 10px; font-weight: 800; color: #0284c7; background: #e0f2fe; padding: 4px 10px; border-radius: 6px;">CISERANO — ZINGONIA (BG)</span>
        </div>
        <div style="display: flex; gap: 8px;">
            <span style="background: #f1f5f9; border: 1px solid #cbd5e1; color: #334155; font-size: 9px; font-weight: 700; padding: 4px 10px; border-radius: 5px; text-transform: uppercase;">PROPOSTA TECNICO-GESTIONALE 2026/2027</span>
            <span style="background: #10b981; color: #ffffff; font-size: 9px; font-weight: 700; padding: 4px 10px; border-radius: 5px; text-transform: uppercase;">ECOSISTEMA DIGITALE</span>
        </div>
    </div>

    <div style="display: flex; flex-direction: column; gap: 12px; margin: 12px 0;">
        <div style="font-size: 11px; font-weight: 800; color: #0369a1; text-transform: uppercase; letter-spacing: 1.2px;">
            ITALSPORT GROUP (Italsport di Locatelli Vincenzo) • VIA PROVINCIALE FRANCESCA 2H/I, CISERANO (BG)
        </div>
        <h1 style="font-size: 31px; font-weight: 800; line-height: 1.15; margin: 0; color: #0f172a; letter-spacing: -0.5px;">
            EVOLUZIONE GESTIONALE ERP, VETRINE SQUADRE<br>CON PASSWORD & ARCHIVIO LOCALE NAS
        </h1>
        <p style="font-size: 12px; color: #334155; max-width: 880px; margin: 0; line-height: 1.45;">
            Analisi delle esigenze operative emerse a Ciserano (BG): unificazione gestionale/magazzino, <b>Vetrine Squadra protette da password</b> (dove ogni club vede solo i propri capi e trova sempre le stesse cose) e custodia sicura dell'archivio grafico aziendale.
        </p>

        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px; margin-top: 8px;">
            <div class="card-white" style="border-top: 3.5px solid #0284c7;">
                <span class="pill pill-blue" style="margin-bottom: 4px;">CARDINE 01</span>
                <div style="font-size: 12px; font-weight: 800; color: #0f172a;">Ecosistema ERP Unificato</div>
                <div style="font-size: 9px; color: #475569; margin-top: 2px;">Centralizzazione real-time di contabilità ordinaria, giacenze magazzino (2.600 articoli attivi) e distinte base.</div>
            </div>
            <div class="card-white" style="border-top: 3.5px solid #10b981;">
                <span class="pill pill-green" style="margin-bottom: 4px;">CARDINE 02</span>
                <div style="font-size: 12px; font-weight: 800; color: #0f172a;">Vetrine Squadra con Password</div>
                <div style="font-size: 9px; color: #475569; margin-top: 2px;">Ogni squadra accede con una <b>password dedicata</b> e vede <b>solo le cose relative al proprio club</b>, trovando sempre gli stessi articoli senza problemi.</div>
            </div>
            <div class="card-white" style="border-top: 3.5px solid #f59e0b;">
                <span class="pill pill-gold" style="margin-bottom: 4px;">CARDINE 03</span>
                <div style="font-size: 12px; font-weight: 800; color: #0f172a;">NAS Locale & Sicurezza Dati</div>
                <div style="font-size: 9px; color: #475569; margin-top: 2px;">Archivio ad alta velocità nella sede di Ciserano per file grafici e loghi di 30 anni di attività, con backup RAID e zero canoni cloud.</div>
            </div>
        </div>
    </div>

    <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #cbd5e1; padding-top: 8px; font-size: 8.5px; color: #475569;">
        <div><b>COMMITTENTE:</b> Italsport Group (Via Provinciale Francesca 2H/I, Ciserano — BG)</div>
        <div><b>CONTATTI:</b> Tel. 035 4191221 • info@italsport-group.it</div>
        <div><b>P.IVA:</b> 01778490167</div>
        <div><span class="slide-num">SLIDE 01 / 10</span></div>
    </div>
</div>""",

    # Slide 2: Executive Summary & Diagnosi
    f"""<div class="slide">
    <div class="slide-header">
        <div class="header-left">
            <img src="{logo_b64}" class="header-logo" alt="Italsport Logo">
            <div class="header-title-box">
                <span class="category-tag">DIAGNOSI AZIENDALE & SCENARIO</span>
                <h2 class="slide-title">Executive Summary: Superare la Frammentazione dei Sistemi a Ciserano</h2>
                <p class="slide-subtitle">Unificare l'infrastruttura software per abbattere i costi, tutelare la contabilità e velocizzare la gestione delle società sportive.</p>
            </div>
        </div>
        <div class="header-right">
            <span class="chapter-badge">CAPITOLO 01 | DIAGNOSI</span>
        </div>
    </div>

    <div class="slide-body">
        <div class="grid-3" style="align-items: stretch;">
            <div class="card" style="border-top: 3.5px solid #ef4444; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <span class="pill" style="background: #fee2e2; color: #b91c1c;">SITUAZIONE ATTUALE</span>
                    <div style="font-size: 11.5px; font-weight: 800; color: #0f172a; margin: 5px 0 3px 0;">Ecosistema IT Frammentato</div>
                    <div style="font-size: 8.5px; color: #475569; line-height: 1.4;">
                        Attualmente l'azienda opera con sistemi separati: <b>TeamSystem Alyante</b> per la contabilità, <b>PrestaShop</b> per lo store (`store.italsport-group.it`), WordPress per il sito vetrina e un CRM con oltre <b>4.600 aziende/società</b> (di cui circa 1.600 attive negli ultimi 2 anni).
                    </div>
                </div>
                <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 5px; padding: 5px 7px; margin-top: 6px; font-size: 8px; color: #b91c1c; font-weight: 700;">
                    CRITICITÀ: Doppi inserimenti e sistemi non comunicanti.
                </div>
            </div>

            <div class="card" style="border-top: 3.5px solid #f59e0b; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <span class="pill pill-gold">LE PRESSIONI DEL MOMENTO</span>
                    <div style="font-size: 11.5px; font-weight: 800; color: #0f172a; margin: 5px 0 3px 0;">Scadenze & Costi Fuori Scala</div>
                    <div style="font-size: 8.5px; color: #475569; line-height: 1.4;">
                        La scadenza del rinnovo annuale di gennaio e i preventivi esterni spropositati per nuovi ERP (es. Odoo con fornitori terzi fino a <b>25.000 € – 35.000 €</b> e assistenza a 60 €/ora) richiedono una soluzione trasparente e sostenibile.
                    </div>
                </div>
                <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 5px; padding: 5px 7px; margin-top: 6px; font-size: 8px; color: #d97706; font-weight: 700;">
                    URGENZA: Presidiare gennaio senza spese sproporzionate.
                </div>
            </div>

            <div class="card-green" style="border-top: 3.5px solid #10b981; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <span class="pill pill-green">LA NOSTRA RISPOSTA</span>
                    <div style="font-size: 11.5px; font-weight: 800; color: #0f172a; margin: 5px 0 3px 0;">Approccio Modulare a Tappe</div>
                    <div style="font-size: 8.5px; color: #334155; line-height: 1.4;">
                        Verifichiamo la tenuta fiscale e la distinta base in ambiente controllato, presidiando la scadenza di gennaio, potenziando le <b>Vetrine Squadra con Password</b> e tagliando oltre il 60% dei costi di implementazione.
                    </div>
                </div>
                <div style="background: #dcfce7; border: 1px solid #bbf7d0; border-radius: 5px; padding: 5px 7px; margin-top: 6px; font-size: 8px; color: #166534; font-weight: 700;">
                    SOLUZIONE: Partnership chiara e formazione interna.
                </div>
            </div>
        </div>

        <div class="grid-4" style="margin-top: 4px;">
            <div class="stat-box">
                <div class="stat-val">&gt; 60%</div>
                <div class="stat-lbl">Risparmio sui Preventivi Esterni</div>
            </div>
            <div class="stat-box">
                <div class="stat-val">4.600+</div>
                <div class="stat-lbl">Realtà Registrate nel CRM</div>
            </div>
            <div class="stat-box">
                <div class="stat-val">2.600</div>
                <div class="stat-lbl">Articoli Attivi (su 8.650 totali)</div>
            </div>
            <div class="stat-box">
                <div class="stat-val">GEN 2027</div>
                <div class="stat-lbl">Scadenza Fiscale Presidiata</div>
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <div class="footer-left">
            <span class="footer-pill">ITALSPORT GROUP — CISERANO (BG)</span>
            <span>PIANO STRATEGICO GESTIONALE & IT 2026/2027</span>
        </div>
        <div>CAPITOLO 01: DIAGNOSI AZIENDALE</div>
        <div class="slide-num">Slide 02 / 10</div>
    </div>
</div>""",

    # Slide 3: 5 Non-negotiable requirements
    f"""<div class="slide">
    <div class="slide-header">
        <div class="header-left">
            <img src="{logo_b64}" class="header-logo" alt="Italsport Logo">
            <div class="header-title-box">
                <span class="category-tag">ANALISI REQUISITI CHIAVE</span>
                <h2 class="slide-title">I 5 Requisiti Aziendali Irrinunciabili per Italsport</h2>
                <p class="slide-subtitle">I vincoli tecnici, fiscali e commerciali richiesti da Vincenzo Locatelli e dallo staff di Ciserano.</p>
            </div>
        </div>
        <div class="header-right">
            <span class="chapter-badge">CAPITOLO 01 | REQUISITI</span>
        </div>
    </div>

    <div class="slide-body">
        <div class="grid-5" style="align-items: stretch;">
            <div class="card-white" style="border-top: 3.5px solid #0284c7; display: flex; flex-direction: column; justify-content: space-between; padding: 11px 11px;">
                <div>
                    <span class="pill pill-blue">REQUISITO 01</span>
                    <div style="font-size: 10.5px; font-weight: 800; color: #0f172a; margin: 4px 0 3px 0;">Piattaforma Unica Real-Time</div>
                    <div style="font-size: 8px; color: #475569; line-height: 1.35;">
                        Eliminare database multipli: ogni movimento su web o in negozio a Ciserano deve aggiornare istantaneamente scorte, impegni di magazzino e contabilità.
                    </div>
                </div>
                <div style="font-size: 7.5px; font-weight: 700; color: #0284c7; margin-top: 6px;">• Zero doppi inserimenti</div>
            </div>

            <div class="card-white" style="border-top: 3.5px solid #10b981; display: flex; flex-direction: column; justify-content: space-between; padding: 11px 11px;">
                <div>
                    <span class="pill pill-green">REQUISITO 02</span>
                    <div style="font-size: 10.5px; font-weight: 800; color: #0f172a; margin: 4px 0 3px 0;">Regime Fiscale Ordinario</div>
                    <div style="font-size: 8px; color: #475569; line-height: 1.35;">
                        Gestione contabile completa: piano dei conti italiano, fatturazione elettronica SDI, collegamento al cassetto fiscale e carico/scarico automatico a fattura.
                    </div>
                </div>
                <div style="font-size: 7.5px; font-weight: 700; color: #16a34a; margin-top: 6px;">• Conformità SDI 100%</div>
            </div>

            <div class="card-white" style="border-top: 3.5px solid #f59e0b; display: flex; flex-direction: column; justify-content: space-between; padding: 11px 11px;">
                <div>
                    <span class="pill pill-gold">REQUISITO 03</span>
                    <div style="font-size: 10.5px; font-weight: 800; color: #0f172a; margin: 4px 0 3px 0;">Distinta Base Personalizzazioni</div>
                    <div style="font-size: 8px; color: #475569; line-height: 1.35;">
                        Per i capi personalizzati: distinta base che calcola capo neutro + stampa/ricamo + manodopera + scarto, tracciando i costi reali di commessa.
                    </div>
                </div>
                <div style="font-size: 7.5px; font-weight: 700; color: #d97706; margin-top: 6px;">• Calcolo costi commessa</div>
            </div>

            <div class="card-white" style="border-top: 3.5px solid #8b5cf6; display: flex; flex-direction: column; justify-content: space-between; padding: 11px 11px;">
                <div>
                    <span class="pill pill-purple">REQUISITO 04</span>
                    <div style="font-size: 10.5px; font-weight: 800; color: #0f172a; margin: 4px 0 3px 0;">Catalogo Padre-Figlio</div>
                    <div style="font-size: 8px; color: #475569; line-height: 1.35;">
                        Gestione ordinata dei 2.600 articoli attivi con varianti taglia/colore, sovrapprezzi taglia (es. XXL > M) e listini dedicati ai 4 livelli Pro-Club.
                    </div>
                </div>
                <div style="font-size: 7.5px; font-weight: 700; color: #9333ea; margin-top: 6px;">• Listini Basic..Diamond</div>
            </div>

            <div class="card-white" style="border-top: 3.5px solid #0284c7; display: flex; flex-direction: column; justify-content: space-between; padding: 11px 11px;">
                <div>
                    <span class="pill pill-blue">REQUISITO 05</span>
                    <div style="font-size: 10.5px; font-weight: 800; color: #0f172a; margin: 4px 0 3px 0;">Vetrina Squadra con Password</div>
                    <div style="font-size: 8px; color: #475569; line-height: 1.35;">
                        Ogni squadra ha la sua vetrina protetta da password dove vede <b>solo le cose relative alla sua società</b> e ritrova sempre le stesse cose nel tempo senza errori.
                    </div>
                </div>
                <div style="font-size: 7.5px; font-weight: 700; color: #0284c7; margin-top: 6px;">• Accesso con password club</div>
            </div>
        </div>

        <div class="card" style="background: #f8fafc; padding: 8px 12px; margin-top: 4px;">
            <div style="font-size: 8.5px; color: #334155;">
                <b>Vincolo Fondamentale Condiviso con la Proprietà:</b> Qualsiasi piattaforma adottata dovrà superare il collaudo pratico su questi 5 requisiti prima di andare in produzione, garantendo continuità totale alle società sportive servite da Italsport.
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <div class="footer-left">
            <span class="footer-pill">ITALSPORT GROUP — CISERANO (BG)</span>
            <span>PIANO STRATEGICO GESTIONALE & IT 2026/2027</span>
        </div>
        <div>CAPITOLO 01: I 5 REQUISITI IRRINUNCIABILI</div>
        <div class="slide-num">Slide 03 / 10</div>
    </div>
</div>""",

    # Slide 4: Benchmark with Complete Evaluation Matrix
    f"""<div class="slide">
    <div class="slide-header">
        <div class="header-left">
            <img src="{logo_b64}" class="header-logo" alt="Italsport Logo">
            <div class="header-title-box">
                <span class="category-tag">BENCHMARK TECNOLOGICO & SOFTWARE</span>
                <h2 class="slide-title">Analisi Comparativa delle Soluzioni Gestionali</h2>
                <p class="slide-subtitle">Valutazione oggettiva di costi, tempi di implementazione e gestione delle Vetrine con Password tra le 3 opzioni.</p>
            </div>
        </div>
        <div class="header-right">
            <span class="chapter-badge">CAPITOLO 02 | BENCHMARK</span>
        </div>
    </div>

    <div class="slide-body">
        <div class="grid-3" style="align-items: stretch; margin-bottom: 2px;">
            <div class="card-white" style="border-top: 3.5px solid #64748b; padding: 10px 12px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span class="pill pill-slate">OPZIONE A • PONTE</span>
                    <span style="font-size: 8.5px; font-weight: 700; color: #475569;">€ 3.000 – 4.000</span>
                </div>
                <div style="font-size: 11px; font-weight: 800; color: #0f172a; margin: 4px 0 2px 0;">Mantenimento Alyante + Store</div>
                <div style="font-size: 8px; color: #475569; line-height: 1.3;">Tamponare il vecchio gestionale per superare gennaio mantenendo PrestaShop.</div>
            </div>

            <div class="card-green" style="border-top: 3.5px solid #10b981; padding: 10px 12px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span class="pill pill-green">OPZIONE B • CONSIGLIATA</span>
                    <span style="font-size: 8.5px; font-weight: 700; color: #15803d;">CANONI MODULARI</span>
                </div>
                <div style="font-size: 11px; font-weight: 800; color: #0f172a; margin: 4px 0 2px 0;">Piattaforma Integrata Moderna</div>
                <div style="font-size: 8px; color: #166534; line-height: 1.3;">ERP cloud modulare unificato con Vetrine Squadra protette da password e SDI fiscale.</div>
            </div>

            <div class="card-white" style="border-top: 3.5px solid #ef4444; padding: 10px 12px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span class="pill" style="background: #fee2e2; color: #b91c1c;">OPZIONE C • SCONSIGLIATA</span>
                    <span style="font-size: 8.5px; font-weight: 700; color: #b91c1c;">&gt; € 40.000</span>
                </div>
                <div style="font-size: 11px; font-weight: 800; color: #0f172a; margin: 4px 0 2px 0;">Software Custom da Zero</div>
                <div style="font-size: 8px; color: #475569; line-height: 1.3;">Programmare tutto su misura: tempi lunghissimi e dipendenza da programmatori.</div>
            </div>
        </div>

        <table class="deck-table">
            <thead>
                <tr>
                    <th style="width: 25%;">Parametro di Valutazione</th>
                    <th style="width: 25%;">Opzione A: Alyante + PrestaShop</th>
                    <th style="width: 25%; background: #dcfce7; color: #166534;">Opzione B: ERP Moderno Integrato</th>
                    <th style="width: 25%;">Opzione C: Custom da Zero</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><b>Integrazione Magazzino Ciserano & Web</b></td>
                    <td>Parziale / sincronizzazione manuale</td>
                    <td style="background: #f0fdf4;"><b>100% nativa in tempo reale</b></td>
                    <td>Da sviluppare interamente da zero</td>
                </tr>
                <tr>
                    <td><b>Fatturazione Elettronica & SDI</b></td>
                    <td>Inclusa (ma costosa da manutenere)</td>
                    <td style="background: #f0fdf4;"><b>Certificata italiana e automatica</b></td>
                    <td>Da programmare e aggiornare a spese proprie</td>
                </tr>
                <tr>
                    <td><b>Vetrine Squadra con Password</b></td>
                    <td>Gestione macchinosa per ogni club</td>
                    <td style="background: #f0fdf4;"><b>Accesso con password per ogni squadra nativo</b></td>
                    <td>Custom ma con tempi di rilascio biblici</td>
                </tr>
                <tr>
                    <td><b>Tempi di Rilascio Operativo</b></td>
                    <td>Immediato (ma senza miglioramenti)</td>
                    <td style="background: #f0fdf4;"><b>4 – 6 settimane per moduli pilota</b></td>
                    <td>6 – 12 mesi di sviluppo incerto</td>
                </tr>
                <tr>
                    <td><b>Verdetto Strategico</b></td>
                    <td>Soluzione ponte temporanea</td>
                    <td style="background: #f0fdf4;"><b>SCELTA OTTIMALE PER RAPPORTO ROI/COSTI</b></td>
                    <td>Fortemente sconsigliata per rischi</td>
                </tr>
            </tbody>
        </table>

        <div class="card" style="background: #f8fafc; padding: 7px 11px; margin-top: 2px;">
            <div style="font-size: 8.5px; color: #334155;">
                <b>Raccomandazione Tecnica:</b> Adottare l'<b>Opzione B</b> con approccio graduale, proteggendo la contabilità e semplificando la creazione delle Vetrine con Password per tutte le società partner.
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <div class="footer-left">
            <span class="footer-pill">ITALSPORT GROUP — CISERANO (BG)</span>
            <span>PIANO STRATEGICO GESTIONALE & IT 2026/2027</span>
        </div>
        <div>CAPITOLO 02: BENCHMARK GESTIONALI A CONFRONTO</div>
        <div class="slide-num">Slide 04 / 10</div>
    </div>
</div>""",

    # Slide 5: Target Architecture
    f"""<div class="slide">
    <div class="slide-header">
        <div class="header-left">
            <img src="{logo_b64}" class="header-logo" alt="Italsport Logo">
            <div class="header-title-box">
                <span class="category-tag">ARCHITETTURA APPLICATIVA INTEGRATA</span>
                <h2 class="slide-title">L'Architettura Target Integrata per Italsport Group (Ciserano)</h2>
                <p class="slide-subtitle">Un flusso continuo di dati in tempo reale tra Vetrine con Password, Configuratore 3D, gestionale e magazzino di Ciserano.</p>
            </div>
        </div>
        <div class="header-right">
            <span class="chapter-badge">CAPITOLO 02 | ARCHITETTURA</span>
        </div>
    </div>

    <div class="slide-body">
        <div style="display: flex; flex-direction: column; gap: 8px; justify-content: space-between; flex-grow: 1;">
            <div class="card-white" style="border-left: 4px solid #0284c7; padding: 9px 12px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 5px;">
                    <span style="font-size: 9.5px; font-weight: 800; color: #0284c7; text-transform: uppercase;">LIVELLO 1: CANALI DIGITALI & VETRINE SQUADRA CON PASSWORD</span>
                    <span class="pill pill-blue">FRONT-END WEB</span>
                </div>
                <div class="grid-3" style="font-size: 8.5px;">
                    <div style="background: #f8fafc; padding: 6px 9px; border-radius: 5px; border: 1px solid #e2e8f0;">
                        <b>Sito Vetrina & Catalogo (italsport-group.it)</b><br><span style="color: #64748b;">Presentazione linee, Tessera Pro-Club e contatti</span>
                    </div>
                    <div style="background: #f0fdf4; padding: 6px 9px; border-radius: 5px; border: 1px solid #bbf7d0;">
                        <b>Vetrine Squadra con Password (My Italsport)</b><br><span style="color: #15803d;">Ogni club entra con password e vede solo i propri capi</span>
                    </div>
                    <div style="background: #f0f7ff; padding: 6px 9px; border-radius: 5px; border: 1px solid #bfdbfe;">
                        <b>Configuratore 3D a 360°</b><br><span style="color: #0369a1;">Personalizzazione divise con rotazione a 360°</span>
                    </div>
                </div>
            </div>

            <div style="text-align: center; font-size: 8px; color: #0284c7; font-weight: 700; margin: -2px 0;">
                ↕ Sincronizzazione Real-Time Bidirezionale ↕
            </div>

            <div class="card-blue" style="border-left: 4px solid #0369a1; padding: 10px 12px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                    <span style="font-size: 9.5px; font-weight: 800; color: #0369a1; text-transform: uppercase;">LIVELLO 2: MOTORE CENTRALE GESTIONALE ERP (REAL-TIME CORE)</span>
                    <span class="pill pill-blue">DATABASE UNIFICATO</span>
                </div>
                <div class="grid-4" style="font-size: 8.5px;">
                    <div style="background: #ffffff; padding: 6px 8px; border-radius: 5px; border: 1px solid #cbd5e1;">
                        <b>Magazzino Ciserano</b><br><span style="color: #475569;">2.600 articoli attivi, varianti taglia/colore</span>
                    </div>
                    <div style="background: #ffffff; padding: 6px 8px; border-radius: 5px; border: 1px solid #cbd5e1;">
                        <b>Commesse & Distinta Base</b><br><span style="color: #475569;">Capi neutri + stampe/ricami + tempi lavorazione</span>
                    </div>
                    <div style="background: #ffffff; padding: 6px 8px; border-radius: 5px; border: 1px solid #cbd5e1;">
                        <b>Contabilità Ordinaria SDI</b><br><span style="color: #475569;">Fatture elettroniche, cassetto fiscale e scadenze</span>
                    </div>
                    <div style="background: #ffffff; padding: 6px 8px; border-radius: 5px; border: 1px solid #cbd5e1;">
                        <b>CRM Unificato (4.600+ Realtà)</b><br><span style="color: #475569;">Società sportive, oratori, scuole e aziende</span>
                    </div>
                </div>
            </div>

            <div style="text-align: center; font-size: 8px; color: #16a34a; font-weight: 700; margin: -2px 0;">
                ↕ Rete Locale Gigabit & Archivio Storico a Ciserano (BG) ↕
            </div>

            <div class="card-white" style="border-left: 4px solid #10b981; padding: 9px 12px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 5px;">
                    <span style="font-size: 9.5px; font-weight: 800; color: #16a34a; text-transform: uppercase;">LIVELLO 3: SEDE OPERATIVA, SHOWROOM & NAS LOCALE (CISERANO — BG)</span>
                    <span class="pill pill-green">SEDE VIA PROV. FRANCESCA 2H/I</span>
                </div>
                <div class="grid-3" style="font-size: 8.5px;">
                    <div style="background: #f0fdf4; padding: 6px 9px; border-radius: 5px; border: 1px solid #bbf7d0;">
                        <b>NAS Locale Aziendale</b><br><span style="color: #166534;">Custodia veloce di loghi, impianti stampa e file grafici</span>
                    </div>
                    <div style="background: #f8fafc; padding: 6px 9px; border-radius: 5px; border: 1px solid #e2e8f0;">
                        <b>Reparto Personalizzazioni</b><br><span style="color: #475569;">Stampa, ricamo e preparazione linee societarie</span>
                    </div>
                    <div style="background: #f8fafc; padding: 6px 9px; border-radius: 5px; border: 1px solid #e2e8f0;">
                        <b>Showroom & Magazzino Scorte Club</b><br><span style="color: #475569;">Consegna rapida per i club Pro-Club del territorio</span>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <div class="footer-left">
            <span class="footer-pill">ITALSPORT GROUP — CISERANO (BG)</span>
            <span>PIANO STRATEGICO GESTIONALE & IT 2026/2027</span>
        </div>
        <div>CAPITOLO 02: ARCHITETTURA APPLICATIVA TARGET</div>
        <div class="slide-num">Slide 05 / 10</div>
    </div>
</div>""",

    # Slide 6: Local NAS Infrastructure
    f"""<div class="slide">
    <div class="slide-header">
        <div class="header-left">
            <img src="{logo_b64}" class="header-logo" alt="Italsport Logo">
            <div class="header-title-box">
                <span class="category-tag">INFRASTRUTTURA IT & SICUREZZA DATI</span>
                <h2 class="slide-title">Protezione dell'Archivio Storico a Ciserano: Server NAS Locale Dedicato</h2>
                <p class="slide-subtitle">Velocità Gigabit in rete locale per i file grafici, totale riservatezza aziendale e zero canoni cloud ricorrenti.</p>
            </div>
        </div>
        <div class="header-right">
            <span class="chapter-badge">CAPITOLO 03 | ARCHIVIO NAS</span>
        </div>
    </div>

    <div class="slide-body">
        <div class="grid-2" style="align-items: stretch;">
            <div class="card-white" style="display: flex; flex-direction: column; justify-content: space-between; padding: 12px 14px;">
                <div>
                    <span class="pill pill-slate">LA SPECIFICITÀ DI ITALSPORT GROUP</span>
                    <div style="font-size: 12px; font-weight: 800; color: #0f172a; margin: 4px 0 3px 0;">30 Anni di Loghi e Grafiche Societarie</div>
                    <img src="{shw_b64}" style="width: 100%; height: 95px; object-fit: cover; border-radius: 6px; border: 1px solid #cbd5e1; margin-bottom: 6px;" alt="Showroom Italsport Ciserano">
                    <p style="font-size: 8.5px; color: #475569; line-height: 1.4; margin: 0 0 6px 0;">
                        In 30 anni di attività a Ciserano, Italsport ha accumulato migliaia di file vettoriali, stemmi di società sportive, impianti di stampa e ricamo. Tenerli su un NAS locale garantisce accesso istantaneo per i riordini anche a distanza di anni.
                    </p>
                </div>
                <div style="background: #f0f7ff; border: 1px solid #bfdbfe; border-radius: 5px; padding: 6px 9px; margin-top: 4px; font-size: 8.5px; color: #0369a1; font-weight: 700;">
                    LA RISPOSTA: Server NAS on-premise nella sede di Ciserano (BG) con snapshot e backup automatico.
                </div>
            </div>

            <div style="display: flex; flex-direction: column; gap: 7px; justify-content: space-between;">
                <div class="card-white" style="border-left: 3.5px solid #0284c7; padding: 9px 12px;">
                    <div style="font-size: 9.5px; font-weight: 800; color: #0284c7;">1. Velocità Locale di Rete Gigabit (1.000 Mbps)</div>
                    <div style="font-size: 8px; color: #475569; margin-top: 2px;">Apertura immediata dei file grafici pesanti direttamente dalle postazioni dell'ufficio di Ciserano: zero attese di caricamento.</div>
                </div>

                <div class="card-white" style="border-left: 3.5px solid #10b981; padding: 9px 12px;">
                    <div style="font-size: 9.5px; font-weight: 800; color: #16a34a;">2. Riservatezza Totale & Proprietà Fisica del Dato</div>
                    <div style="font-size: 8px; color: #475569; margin-top: 2px;">Le 4.600 anagrafiche clienti, i loghi societari e i documenti contabili restano fisicamente custoditi nella sede di Via Provinciale Francesca 2H/I.</div>
                </div>

                <div class="card-white" style="border-left: 3.5px solid #f59e0b; padding: 9px 12px;">
                    <div style="font-size: 9.5px; font-weight: 800; color: #d97706;">3. Ridondanza RAID & Protezione da Guasti</div>
                    <div style="font-size: 8px; color: #475569; margin-top: 2px;">Dischi gemelli in mirroring RAID: se un disco si guasta, nessun file viene perso e l'operatività non si ferma mai.</div>
                </div>

                <div class="card-white" style="border-left: 3.5px solid #8b5cf6; padding: 9px 12px;">
                    <div style="font-size: 9.5px; font-weight: 800; color: #9333ea;">4. Zero Canoni Mensili Ricorrenti</div>
                    <div style="font-size: 8px; color: #475569; margin-top: 2px;">Investimento hardware una tantum (es. Synology/QNAP con dischi enterprise) senza abbonamenti cloud mensili.</div>
                </div>
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <div class="footer-left">
            <span class="footer-pill">ITALSPORT GROUP — CISERANO (BG)</span>
            <span>PIANO STRATEGICO GESTIONALE & IT 2026/2027</span>
        </div>
        <div>CAPITOLO 03: SICUREZZA IT & ARCHIVIO NAS</div>
        <div class="slide-num">Slide 06 / 10</div>
    </div>
</div>""",

    # Slide 7: Data Migration
    f"""<div class="slide">
    <div class="slide-header">
        <div class="header-left">
            <img src="{logo_b64}" class="header-logo" alt="Italsport Logo">
            <div class="header-title-box">
                <span class="category-tag">MIGRAZIONE & BONIFICA DATI</span>
                <h2 class="slide-title">Piano di Bonifica & Migrazione Dati Senza Rischi</h2>
                <p class="slide-subtitle">I 4 passaggi per trasferire le anagrafiche attive e i 2.600 articoli operativi senza bloccare il lavoro quotidiano.</p>
            </div>
        </div>
        <div class="header-right">
            <span class="chapter-badge">CAPITOLO 03 | MIGRAZIONE</span>
        </div>
    </div>

    <div class="slide-body">
        <div class="grid-4" style="align-items: stretch;">
            <div class="card-white" style="border-top: 3.5px solid #0284c7; padding: 12px 14px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <span class="pill pill-blue">STEP 01</span>
                    <div style="font-size: 11px; font-weight: 800; color: #0f172a; margin: 4px 0 2px 0;">Estrazione Strutturata</div>
                    <div style="font-size: 8px; color: #475569; line-height: 1.35;">
                        Estrazione da Alyante TeamSystem e CRM dello storico recente: le ~1.600 realtà attive sulle 4.600 storiche e i listini club concordati.
                    </div>
                </div>
                <div style="font-size: 7.5px; font-weight: 700; color: #0284c7; margin-top: 6px;">• Export CSV/Excel certificato</div>
            </div>

            <div class="card-white" style="border-top: 3.5px solid #10b981; padding: 12px 14px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <span class="pill pill-green">STEP 02</span>
                    <div style="font-size: 11px; font-weight: 800; color: #0f172a; margin: 4px 0 2px 0;">Bonifica & Pulizia</div>
                    <div style="font-size: 8px; color: #475569; line-height: 1.35;">
                        Isolamento dei <b>2.600 articoli realmente movimentati</b> sugli 8.650 totali in archivio, pulizia duplicati e normalizzazione varianti taglia/colore.
                    </div>
                </div>
                <div style="font-size: 7.5px; font-weight: 700; color: #16a34a; margin-top: 6px;">• Solo articoli realmente attivi</div>
            </div>

            <div class="card-white" style="border-top: 3.5px solid #f59e0b; padding: 12px 14px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <span class="pill pill-gold">STEP 03</span>
                    <div style="font-size: 11px; font-weight: 800; color: #0f172a; margin: 4px 0 2px 0;">Vetrine con Password</div>
                    <div style="font-size: 8px; color: #475569; line-height: 1.35;">
                        Associazione di ciascuna società alla propria <b>Vetrina Protetta da Password</b> con i soli articoli approvati per quella squadra.
                    </div>
                </div>
                <div style="font-size: 7.5px; font-weight: 700; color: #d97706; margin-top: 6px;">• Linea bloccata per ogni club</div>
            </div>

            <div class="card-white" style="border-top: 3.5px solid #8b5cf6; padding: 12px 14px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <span class="pill pill-purple">STEP 04</span>
                    <div style="font-size: 11px; font-weight: 800; color: #0f172a; margin: 4px 0 2px 0;">Allineamento Parallelo</div>
                    <div style="font-size: 8px; color: #475569; line-height: 1.35;">
                        Periodo di collaudo con doppio controllo prima dello switch definitivo: le forniture alle società sportive proseguono senza interruzioni.
                    </div>
                </div>
                <div style="font-size: 7.5px; font-weight: 700; color: #9333ea; margin-top: 6px;">• Zero fermi operativi</div>
            </div>
        </div>

        <div class="card" style="background: #f0fdf4; border: 1.5px solid #bbf7d0; padding: 9px 13px; margin-top: 3px;">
            <div style="font-size: 8.5px; color: #166534; line-height: 1.35;">
                <b>Garanzia di Continuità Aziendale:</b> La migrazione avviene per gradi. Alyante continuerà a garantire la regolare emissione delle fatture fino a quando il nuovo sistema non sarà validato al 100% dalla direzione di Italsport.
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <div class="footer-left">
            <span class="footer-pill">ITALSPORT GROUP — CISERANO (BG)</span>
            <span>PIANO STRATEGICO GESTIONALE & IT 2026/2027</span>
        </div>
        <div>CAPITOLO 03: MIGRAZIONE & BONIFICA DATI</div>
        <div class="slide-num">Slide 07 / 10</div>
    </div>
</div>""",

    # Slide 8: Financial Plan
    f"""<div class="slide">
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
        <div class="grid-2" style="align-items: stretch; margin-bottom: 2px;">
            <div class="card" style="border-top: 3.5px solid #ef4444; background: #fffaf0; padding: 10px 13px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span class="pill" style="background: #fee2e2; color: #b91c1c;">FORNITORI TRADIZIONALI ESTERNI</span>
                    <span style="font-size: 9.5px; font-weight: 800; color: #b91c1c;">€ 25.000 – 35.000</span>
                </div>
                <div style="font-size: 11px; font-weight: 800; color: #0f172a; margin: 3px 0 2px 0;">Il Modello "A Pacchetto Chiuso"</div>
                <div style="font-size: 8px; color: #475569; line-height: 1.35;">Preventivo elevato a pacchetto chiuso, tariffe a 60 €/ora gonfiate a forfait e vincolo contrattuale rigido.</div>
            </div>

            <div class="card-green" style="border-top: 3.5px solid #10b981; padding: 10px 13px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span class="pill pill-green">IL NOSTRO MODELLO DI PARTNERSHIP</span>
                    <span style="font-size: 9.5px; font-weight: 800; color: #15803d;">TAGLIO COSTI &gt; 60%</span>
                </div>
                <div style="font-size: 11px; font-weight: 800; color: #0f172a; margin: 3px 0 2px 0;">Consulenza & Affiancamento Interno</div>
                <div style="font-size: 8px; color: #334155; line-height: 1.35;">Investimento frazionato per stati d'avanzamento, canoni certi e formazione delle risorse interne a Ciserano.</div>
            </div>
        </div>

        <table class="deck-table">
            <thead>
                <tr>
                    <th style="width: 25%;">Voce di Spesa</th>
                    <th style="width: 25%;">Fornitore Tradizionale Esterno</th>
                    <th style="width: 25%; background: #dcfce7; color: #166534;">Nostro Modello di Partnership</th>
                    <th style="width: 25%; background: #e0f2fe; color: #0369a1;">Vantaggio per Italsport</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><b>Costo Avvio & Setup</b></td>
                    <td>25.000 € – 35.000 € a forfait</td>
                    <td style="background: #f0fdf4;"><b>Investimento a tappe modulate</b></td>
                    <td>Liquidità aziendale protetta</td>
                </tr>
                <tr>
                    <td><b>Assistenza Tecnica Oraria</b></td>
                    <td>60 € / ora (gonfiata a forfait fino a 300 €)</td>
                    <td style="background: #f0fdf4;"><b>Supporto diretto senza intermediari</b></td>
                    <td>Zero costi occulti a sorpresa</td>
                </tr>
                <tr>
                    <td><b>Competenze del Personale</b></td>
                    <td>Nessuna: lock-in e dipendenza totale</td>
                    <td style="background: #f0fdf4;"><b>Formazione sul campo (es. Martina)</b></td>
                    <td>Autonomia operativa a Ciserano</td>
                </tr>
                <tr>
                    <td><b>Aggiornamenti Fiscali & SDI</b></td>
                    <td>A pagamento ad ogni novità normativa</td>
                    <td style="background: #f0fdf4;"><b>Inclusi negli standard cloud certificati</b></td>
                    <td>Zero rincari normativi annuali</td>
                </tr>
            </tbody>
        </table>

        <div class="card-white" style="padding: 7px 11px; margin-top: 2px;">
            <div class="grid-3" style="font-size: 8.5px; text-align: center;">
                <div>
                    <span style="font-weight: 700; color: #64748b;">PREVENTIVO ESTERNO: </span>
                    <b style="color: #dc2626; font-size: 11px;">€ 30.000 + canoni</b>
                </div>
                <div>
                    <span style="font-weight: 700; color: #64748b;">RISPARMIO NETTO: </span>
                    <b style="color: #16a34a; font-size: 12px;">&gt; € 18.000 risparmiati</b>
                </div>
                <div>
                    <span style="font-weight: 700; color: #64748b;">DESTINAZIONE: </span>
                    <b style="color: #0284c7; font-size: 10px;">Sviluppo commerciale e Vetrine Club</b>
                </div>
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <div class="footer-left">
            <span class="footer-pill">ITALSPORT GROUP — CISERANO (BG)</span>
            <span>PIANO STRATEGICO GESTIONALE & IT 2026/2027</span>
        </div>
        <div>CAPITOLO 04: TRASPARENZA COSTI & RISPARMIO</div>
        <div class="slide-num">Slide 08 / 10</div>
    </div>
</div>""",

    # Slide 9: Implementation Roadmap
    f"""<div class="slide">
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
        <div class="grid-4" style="align-items: stretch;">
            <div class="card-white" style="border-top: 3.5px solid #0284c7; padding: 12px 14px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <span class="pill pill-blue">FASE 1 • AUTUNNO</span>
                    <div style="font-size: 11px; font-weight: 800; color: #0f172a; margin: 4px 0 3px 0;">Demo & Verifica Fiscale</div>
                    <div style="font-size: 8.5px; color: #475569; line-height: 1.35;">
                        Dimostrazione pratica del cassetto fiscale, fattura SDI e distinte base; installazione e configurazione del NAS locale a Ciserano (BG).
                    </div>
                </div>
                <div style="font-size: 7.5px; font-weight: 700; color: #0284c7; margin-top: 6px;">• Validazione fiscale</div>
            </div>

            <div class="card-white" style="border-top: 3.5px solid #10b981; padding: 12px 14px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <span class="pill pill-green">FASE 2 • DICEMBRE</span>
                    <div style="font-size: 11px; font-weight: 800; color: #0f172a; margin: 4px 0 3px 0;">Bonifica & Vetrine Pilota</div>
                    <div style="font-size: 8.5px; color: #475569; line-height: 1.35;">
                        Estrazione anagrafiche attive e 2.600 articoli operativi; setup ambiente di test e attivazione Vetrine Squadra con Password pilota.
                    </div>
                </div>
                <div style="font-size: 7.5px; font-weight: 700; color: #16a34a; margin-top: 6px;">• Setup test & prime vetrine</div>
            </div>

            <div class="card-white" style="border-top: 3.5px solid #f59e0b; padding: 12px 14px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <span class="pill pill-gold">FASE 3 • GENNAIO</span>
                    <div style="font-size: 11px; font-weight: 800; color: #0f172a; margin: 4px 0 3px 0;">Presidio Fiscale & Parallelo</div>
                    <div style="font-size: 8.5px; color: #475569; line-height: 1.35;">
                        Gestione guidata della scadenza fiscale annuale; avvio parallelo del magazzino e collaudo flusso fatturazione elettronica.
                    </div>
                </div>
                <div style="font-size: 7.5px; font-weight: 700; color: #d97706; margin-top: 6px;">• Chiusura anno presidiata</div>
            </div>

            <div class="card-white" style="border-top: 3.5px solid #8b5cf6; padding: 12px 14px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <span class="pill pill-purple">FASE 4 • FEB – MARZO</span>
                    <div style="font-size: 11px; font-weight: 800; color: #0f172a; margin: 4px 0 3px 0;">Go-Live & Formazione</div>
                    <div style="font-size: 8.5px; color: #475569; line-height: 1.35;">
                        Rilascio completo della piattaforma, formazione operativa del personale interno su distinte base e gestione Vetrine con Password.
                    </div>
                </div>
                <div style="font-size: 7.5px; font-weight: 700; color: #9333ea; margin-top: 6px;">• Autonomia aziendale</div>
            </div>
        </div>

        <div class="card" style="background: #f8fafc; padding: 8px 12px; margin-top: 3px;">
            <div style="font-size: 8.5px; color: #334155;">
                <b>Flessibilità Operativa:</b> Le fasi sono pianificate per non interferire con i picchi di lavoro delle forniture sportive. Ogni avanzamento viene approvato insieme a Vincenzo Locatelli prima di procedere allo step successivo.
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <div class="footer-left">
            <span class="footer-pill">ITALSPORT GROUP — CISERANO (BG)</span>
            <span>PIANO STRATEGICO GESTIONALE & IT 2026/2027</span>
        </div>
        <div>CAPITOLO 05: CRONOPROGRAMMA DI ESECUZIONE</div>
        <div class="slide-num">Slide 09 / 10</div>
    </div>
</div>""",

    # Slide 10: Next Steps Tech
    f"""<div class="slide">
    <div class="slide-header">
        <div class="header-left">
            <img src="{logo_b64}" class="header-logo" alt="Italsport Logo">
            <div class="header-title-box">
                <span class="category-tag">SINTESI DELLA PARTNERSHIP & AZIONI IMMEDIATE</span>
                <h2 class="slide-title">Prossimi Passi Operativi a Ciserano (BG)</h2>
                <p class="slide-subtitle">Costruire una collaborazione duratura fondata sulla trasparenza, sul controllo dei costi e sui risultati concreti.</p>
            </div>
        </div>
        <div class="header-right">
            <span class="chapter-badge">CAPITOLO 05 | PROSSIMI PASSI</span>
        </div>
    </div>

    <div class="slide-body">
        <div class="grid-3" style="align-items: stretch;">
            <div class="card-white" style="border-top: 3.5px solid #0284c7; padding: 12px 14px;">
                <div style="font-size: 9.5px; font-weight: 800; color: #0284c7; text-transform: uppercase;">STEP 1 • VERIFICA TECNICA</div>
                <div style="font-size: 11.5px; font-weight: 800; color: #0f172a; margin: 4px 0 3px 0;">Sessione Demo Operativa</div>
                <div style="font-size: 8.5px; color: #475569; line-height: 1.35;">
                    Incontro operativo per dimostrare dal vivo la tenuta della contabilità ordinaria, del cassetto fiscale, della distinta base e delle Vetrine con Password.
                </div>
            </div>

            <div class="card-white" style="border-top: 3.5px solid #10b981; padding: 12px 14px;">
                <div style="font-size: 9.5px; font-weight: 800; color: #16a34a; text-transform: uppercase;">STEP 2 • CAMPIONATURA DATI</div>
                <div style="font-size: 11.5px; font-weight: 800; color: #0f172a; margin: 4px 0 3px 0;">Audit Articoli & Vetrine Club</div>
                <div style="font-size: 8.5px; color: #475569; line-height: 1.35;">
                    Test pratico su un campione di articoli (es. Tuta Rom, Giacca Scotland, Giubbotto Nepal) e configurazione di una Vetrina Squadra con Password.
                </div>
            </div>

            <div class="card-white" style="border-top: 3.5px solid #f59e0b; padding: 12px 14px;">
                <div style="font-size: 9.5px; font-weight: 800; color: #d97706; text-transform: uppercase;">STEP 3 • AVVIO IMMEDIATO</div>
                <div style="font-size: 11.5px; font-weight: 800; color: #0f172a; margin: 4px 0 3px 0;">Piano Social @italsportgroup</div>
                <div style="font-size: 8.5px; color: #475569; line-height: 1.35;">
                    Avvio immediato dei 7 post su Instagram con le vere foto di Italsport per promuovere Vetrina con Password, Configuratore 3D e Tessera Pro-Club.
                </div>
            </div>
        </div>

        <div class="card" style="background: #f0f7ff; border: 1.5px solid #bfdbfe; padding: 8px 12px;">
            <div style="font-size: 9px; font-weight: 800; color: #0369a1; text-transform: uppercase;">IL NOSTRO IMPEGNO AL FIANCO DI ITALSPORT:</div>
            <div class="grid-3" style="font-size: 8.5px; color: #334155; margin-top: 3px;">
                <div><b>1. Concretezza Operativa:</b> soluzioni reali pensate per le forniture sportive e le esigenze delle società.</div>
                <div><b>2. Controllo Rigoroso dei Costi:</b> totale trasparenza su licenze, tempi e attività.</div>
                <div><b>3. Affiancamento Costante:</b> supporto diretto in sede a Ciserano e da remoto fino alla piena autonomia.</div>
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
            <span>PIANO STRATEGICO GESTIONALE & IT 2026/2027</span>
        </div>
        <div>CAPITOLO 05: SINTESI PARTNERSHIP & PROSSIMI PASSI</div>
        <div class="slide-num">Slide 10 / 10</div>
    </div>
</div>"""
]

tech_full_html = f"""<!DOCTYPE html>
<html lang="it">
<head>
<title>Italsport Group Ciserano (BG) - Proposta Tecnico-Gestionale & Vetrine Squadre 2026</title>
{css_common}
</head>
<body>
{''.join(tech_slides)}
</body>
</html>"""

with open("full_pdf_template_tech.html", "w", encoding="utf-8") as f:
    f.write(tech_full_html)
print("Saved full_pdf_template_tech.html successfully.")

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
pdf_tech_path = os.path.abspath('Proposta_Ecosistema_Digitale_Italsport_2026.pdf')
cmd_tech = [
    chrome, '--headless=new', '--disable-gpu', '--no-sandbox', '--no-pdf-header-footer',
    f'--print-to-pdf={pdf_tech_path}', f'file:///{os.path.abspath("full_pdf_template_tech.html").replace(os.sep, "/")}'
]
subprocess.run(cmd_tech, check=True)
print(f"Generated {pdf_tech_path} successfully!")

# Assemble Master Presentation (22 Slides)
print("Assembling Master Presentation (22 Slides) via PyMuPDF...")
pdf_social_path = os.path.abspath('Piano_Social_Italsport_2026.pdf')
doc_social = pymupdf.open(pdf_social_path)
doc_tech = pymupdf.open(pdf_tech_path)

doc_master = pymupdf.open()
doc_master.insert_pdf(doc_social)
doc_master.insert_pdf(doc_tech)

pdf_master_path = os.path.abspath('ITALSPORT_Presentazione_Master_2026.pdf')
doc_master.save(pdf_master_path)
print(f"Generated {pdf_master_path} successfully! Pages: {len(doc_master)}")
doc_social.close()
doc_tech.close()
doc_master.close()

# Update README_PACCHETTO_ITALSPORT.txt & Piano_Strategico_Social_Instagram_Italsport.md
readme_content = """================================================================================
ITALSPORT GROUP — CISERANO (BG) • PACCHETTO PRESENTAZIONE & MOCKUP SOCIAL 2026
================================================================================

Dati Aziendali Verificati:
- Ragione Sociale: Italsport Group (Italsport di Locatelli Vincenzo)
- Sede & Showroom: Via Provinciale Francesca 2H/I, 24040 Ciserano — Loc. Zingonia (BG)
- Telefono: 035 4191221 | Cellulare: 335 7001956 | Email: info@italsport-group.it
- P.IVA: 01778490167 | Sito: italsport-group.it | Store: store.italsport-group.it
- Instagram: @italsportgroup | Facebook: @GroupItalsport

--------------------------------------------------------------------------------
1. COSA CONTIENE QUESTO PACCHETTO
--------------------------------------------------------------------------------

[A] Piano_Social_Italsport_2026.pdf (Presentazione Chiara & Professionale)
    - Strategia Instagram basata esclusivamente sulle vere foto di @italsportgroup e italsport-group.it.
    - Focus centrale sulla VETRINA PERSONALIZZATA CON PASSWORD PER OGNI SQUADRA (My Italsport):
      ogni squadra accede con una propria password dedicata e vede SOLO le cose relative alla sua
      squadra, così ritrova sicuramente sempre gli stessi capi nel tempo senza errori o problemi.
    - Focus sul CONFIGURATORE 3D A 360° (con vera rotazione a 360° della maglia) e sulla
      TESSERA PRO-CLUB ufficiale (livelli Basic, Silver, Gold, Diamond — zero magazzino per il club).

[B] Instagram_Mockup_Italsport.html (Sito / Mockup Interattivo Completo)
    - Link Live su GitHub Pages: https://kingsalvo05.github.io/italsport-mockup/
    - Tab 1: Feed Instagram realistico @italsportgroup (clicca per aumentare i Like, doppio clic
      con cuore animato, sfoglia le slide dei caroselli, salva i post, guarda i Reel e le Storie a tutto schermo).
    - Tab 2: Configuratore 3D con vera animazione a 360° della maglia Italsport + simulatore live.
    - Tab 3: Demo interattiva "Vetrina Squadra con Password" (prova a entrare con la password di
      U.S.D. Brevianese, A.S.D. Gessate o Volley Ciserano per vedere solo i capi della squadra).
    - Tab 4: Tessera Pro-Club (Basic, Silver, Gold, Diamond).

[C] I 7 Post Pronti (1080x1080px, con vere foto store.italsport-group.it e @italsportgroup)
    - img_post1_jersey.jpg       -> Post 01: Stampa DTF (Direct-to-Film) & Reparto Grafico Interno (+ img_post1_s2.jpg)
    - img_post2_3d.jpg           -> Post 02: Stampa in Sublimazione 100% Traspirante & Full Print (+ img_post2_s2.jpg)
    - img_post3_fidelity.jpg     -> Post 03: Simulatore / Configuratore 3D a 360° (+ img_post3_s2.jpg + rotazione live)
    - img_post4_stack.jpg        -> Post 04: Vetrina Dedicata alla Squadra con Password - My Italsport (+ img_post4_s2.jpg)
    - img_post5_portal.jpg       -> Post 05: Continuità negli Anni, Zero Magazzino & Tessera Pro-Club (+ img_post5_s2.jpg)
    - img_post6_winter.jpg       -> Post 06: 30 Anni di Storia, 4.600+ Realtà, Linea Flame & Multi-Brand (+ img_post6_s2.jpg)
    - img_post7_celebration.jpg  -> Post 07: Auguri di Natale & Regali Personalizzati per le Squadre (+ img_post7_s2.jpg)
    - configuratore3d_real.gif   -> Animazione 3D a 360° reale della maglia dal configuratore Italsport
================================================================================
"""

with open("README_PACCHETTO_ITALSPORT.txt", "w", encoding="utf-8") as f:
    f.write(readme_content)

# Rebuild ZIP
zip_name = "ITALSPORT_Piano_Social_e_Mockup_2026.zip"
print(f"Creating updated {zip_name}...")
with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as z:
    for f in [
        'Piano_Social_Italsport_2026.pdf',
        'Proposta_Ecosistema_Digitale_Italsport_2026.pdf',
        'ITALSPORT_Presentazione_Master_2026.pdf',
        'Instagram_Mockup_Italsport.html',
        'README_PACCHETTO_ITALSPORT.txt',
        'configuratore3d_real.gif',
        'img_post1_jersey.jpg', 'img_post1_s2.jpg',
        'img_post2_3d.jpg', 'img_post2_s2.jpg',
        'img_post3_fidelity.jpg', 'img_post3_s2.jpg',
        'img_post4_stack.jpg', 'img_post4_s2.jpg',
        'img_post5_portal.jpg', 'img_post5_s2.jpg',
        'img_post6_winter.jpg', 'img_post6_s2.jpg',
        'img_post7_celebration.jpg', 'img_post7_s2.jpg',
        'cropped-cropped-italsportlogo.png'
    ]:
        if os.path.exists(f):
            z.write(f)
            print(f"Added to zip: {f}")

# Copy to Desktop folders and Current Conversation Artifact Directory
target_dirs = [
    r"C:\Users\salvo\Desktop\ITALSPORT_Kit_Cliente_2026",
    r"C:\Users\salvo\Desktop",
    r"C:\Users\salvo\OneDrive\Desktop",
    r"C:\Users\salvo\.gemini\antigravity\brain\dc9abd1d-f990-4c44-a20b-bd6ec7f9af7d",
    r"C:\Users\salvo\.gemini\antigravity\brain\d4b6995e-3462-4b71-a9e5-bc767dc50afb",
]

for d in target_dirs:
    if os.path.exists(d):
        for fn in [
            'Piano_Social_Italsport_2026.pdf',
            'Instagram_Mockup_Italsport.html',
            'ITALSPORT_Piano_Social_e_Mockup_2026.zip'
        ]:
            shutil.copy2(fn, os.path.join(d, fn))
        if d.endswith("ITALSPORT_Kit_Cliente_2026"):
            for fn in [
                'Proposta_Ecosistema_Digitale_Italsport_2026.pdf',
                'ITALSPORT_Presentazione_Master_2026.pdf',
                'README_PACCHETTO_ITALSPORT.txt',
                'configuratore3d_real.gif',
                'img_post1_jersey.jpg', 'img_post2_3d.jpg', 'img_post3_fidelity.jpg',
                'img_post4_stack.jpg', 'img_post5_portal.jpg', 'img_post6_winter.jpg',
                'img_post7_celebration.jpg'
            ]:
                if os.path.exists(fn):
                    shutil.copy2(fn, os.path.join(d, fn))
        print(f"Updated files in: {d}")

print("\nAll Ciserano (BG) decks, ZIP, Desktop files, and Artifacts updated successfully!")
