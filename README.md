# ITALSPORT 2026 - Digital Strategy & Creative Tech

Progetto collaborativo per la strategia digitale, automazione delle presentazioni e mockup interattivi per **Italsport Group**.

---

## 🚀 Come iniziare (per il Team)

### 1. Clona il repository
```bash
git clone https://github.com/KingSalvo05/italsport-team.git
cd italsport-team
```

### 2. Lavorare con Google Gemini / Antigravity
Questo repository è configurato nativamente per la collaborazione con AI:
- **`GEMINI.md`**: contiene l'intero contesto del cliente, la palette colori, le linee guida di tono di voce e l'architettura dei file. Google Gemini / Antigravity lo carica automaticamente ad ogni sessione.
- **`AGENTS.md`**: guida rapida per agenti autonomi e tool di pair programming.

Quando poni una domanda o chiedi una modifica a Gemini (es. *"Crea un nuovo post per il carosello delle divise invernali"* oppure *"Aggiorna la slide 4 del deck master"*), l'AI saprà già esattamente quali file toccare, quale grafica mantenere e che script eseguire.

---

## 📁 Struttura Principale

- **`Instagram_Mockup_Italsport.html`**: Mockup interattivo completo del feed Instagram (apribile in qualsiasi browser: include animazioni 3D, like, caroselli e storie).
- **`Piano_Strategico_Social_Instagram_Italsport.md`**: Piano editoriale dettagliato e strategia di posizionamento B2B/B2C.
- **`Analisi_Incontro_Italsport.md`**: Sintesi della riunione strategica con la dirigenza e piano d'azione.
- **`make_all_decks.py`**: Script unificato per rigenerare tutti i PDF delle presentazioni client.
- **`build_interactive_mockup.py`**: Compila il mockup HTML a partire dagli asset grafici e dal template.

---

## 🛠️ Requisiti & Esecuzione Script

Per rigenerare i PDF o i file HTML:
```bash
pip install playwright pillow
python make_all_decks.py
```

---

## 🔒 Sicurezza
I dati sensibili del cliente (chiavi API, fatture, audio interni della riunione) sono rigorosamente esclusi dal controllo versione tramite `.gitignore`.
