# ITALSPORT 2026 - Guida e Contesto per Google Gemini & AI Assistant

Benvenuto nel workspace di **ITALSPORT 2026**. Questo file serve come base di conoscenza e memoria condivisa per Google Gemini, Antigravity e qualsiasi assistente AI che collabora a questo progetto.

---

## 1. Chi è il Cliente (ITALSPORT GROUP)
- **Azienda:** Italsport Group (Showroom & Headquarter a Ciserano, Bergamo).
- **Settore:** Abbigliamento sportivo personalizzato (calcio, volley, basket, running) e teamwear per società sportive, dilettantistiche e professionistiche.
- **Punti di Forza Unici:**
  - Reparto grafico interno e sartoria per stampa sublimatica full-print ad altissima definizione e termoadesivi DTF.
  - **Configuratore 3D Online** su `italsport-group.it` (permette ai club di ruotare a 360° la divisa con i propri colori e sponsor prima di ordinare).
  - Showroom fisico e gestione B2B personalizzata per presidenti e dirigenti sportivi.

---

## 2. Obiettivi del Progetto & Deliverable
Il nostro obiettivo congiunto è digitalizzare la presenza del brand, automatizzare la produzione di materiale commerciale e gestire la campagna social e B2B:

1. **Piano Strategico Social & Instagram:**
   - Documento strategico: `Piano_Strategico_Social_Instagram_Italsport.md`
   - Feed Instagram realistico e mockup interattivo: `Instagram_Mockup_Italsport.html` (visualizzabile direttamente nel browser con like, swipe caroselli e preview animata 3D).
2. **Presentazioni Master per il Cliente (Decks):**
   - `ITALSPORT_Presentazione_Master_2026.pdf` (Deck completo per la dirigenza)
   - `Piano_Social_Italsport_2026.pdf` (Piano editoriale e strategia contenuti)
   - `Proposta_Ecosistema_Digitale_Italsport_2026.pdf` (Architettura tecnica e portale B2B)
3. **Analisi e Verbali Riunione:**
   - `Analisi_Incontro_Italsport.md` e `Relazione Incontro e Piano d'Azione.pdf`

---

## 3. Architettura del Codice e Script di Automazione
Tutti i deliverable sono generati via codice Python per garantire riproducibilità immediata:

- **`make_all_decks.py` / `build_all_presentations.py`**:
  Genera i PDF e i template HTML delle presentazioni unificando grafica, statistiche e mockup.
- **`build_interactive_mockup.py`**:
  Compila l'HTML interattivo del feed Instagram (`Instagram_Mockup_Italsport.html`) incorporando immagini in base64 e animazioni (`configuratore3d_web.gif`).
- **`extract_vetrina_assets.py` & `create_real_post_images.py`**:
  Script per estrarre e processare le immagini dei prodotti reali e dello showroom di Ciserano.

---

## 4. Linee Guida di Brand e Stile per l'AI
Quando generi o modifichi codice, presentazioni o testi per Italsport:
- **Palette Colori:**
  - Blu Primario: `#0284c7` / `#0369a1`
  - Navy / Dark Slate: `#0f172a` / `#1e293b`
  - Accento Oro/Ambra: `#f59e0b` / `#d97706`
  - Sfondo chiaro: `#f8fafc` / `#ffffff`
- **Tipografia:** Font moderni e puliti sans-serif (`Inter`, `Montserrat`, `Roboto`).
- **Tono di Voce:** Professionale, B2B ma vicino al mondo del calcio e dello sport locale, orientato all'innovazione (3D, personalizzazione totale) e all'affidabilità (consegne puntuali per inizio stagione).

---

## 5. Regole di Collaborazione e Sicurezza
- **MAI salvare chiavi API o dati sensibili nel repository.** I file contenenti credenziali (come `.xlsx` con token API) sono esclusi tramite `.gitignore`.
- Se generi nuovi script, rendili modulari e documentati.
- Per il deploy del mockup web pubblico viene utilizzata la cartella `deploy_site/` pubblicata su GitHub Pages.
