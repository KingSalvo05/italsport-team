"""Genera i 7 post Instagram (1080x1080) + slide carosello per ITALSPORT GROUP — Ciserano (BG)
usando le foto ufficiali ad alta risoluzione da https://store.italsport-group.it/it/,
https://italsport-group.it/ e gli asset condivisi su GitHub (vertexstudiolab / teamwear),
con totale aderenza al lavoro reale di Italsport e all'incontro con il titolare.
"""
import os, shutil
from PIL import Image, ImageEnhance, ImageDraw, ImageFont, ImageFilter

W, H = 1080, 1080
NAVY = (15, 23, 42)
DARK_BLUE = (23, 37, 84)
SLATE = (71, 85, 105)
BLUE = (2, 132, 199)
CYAN = (56, 189, 248)
AMBER = (217, 119, 6)
GOLD = (245, 158, 11)
GREEN = (5, 150, 105)
RED = (185, 28, 28)
FONTS = r"C:\Windows\Fonts"

D_IG = r"C:\Users\salvo\.gemini\antigravity\brain\dc9abd1d-f990-4c44-a20b-bd6ec7f9af7d\scratch\ig_real"
D_WP1 = r"C:\Users\salvo\.gemini\antigravity\brain\dc9abd1d-f990-4c44-a20b-bd6ec7f9af7d\scratch\wp_dl"
D_STORE = r"C:\Users\salvo\.gemini\antigravity\brain\d4b6995e-3462-4b71-a9e5-bc767dc50afb\scratch\store_assets"

LOGO = Image.open("cropped-cropped-italsportlogo.png").convert("RGBA")

def font(bold=False, size=30):
    return ImageFont.truetype(os.path.join(FONTS, "segoeuib.ttf" if bold else "segoeui.ttf"), size)

def cover(im, tw, th, focus_y=0.5, focus_x=0.5):
    r, tr = im.width / im.height, tw / th
    if r > tr:
        nw = int(im.height * tr)
        x = int((im.width - nw) * focus_x)
        im = im.crop((x, 0, x + nw, im.height))
    else:
        nh = int(im.width / tr)
        y = int((im.height - nh) * focus_y)
        im = im.crop((0, y, im.width, y + nh))
    return im.resize((tw, th), Image.Resampling.LANCZOS)

def contain_card(im, tw, th, bg_color=(255, 255, 255), pad=12):
    card = Image.new("RGB", (tw, th), bg_color)
    cp = im.copy()
    cp.thumbnail((tw - pad * 2, th - pad * 2), Image.Resampling.LANCZOS)
    x = (tw - cp.width) // 2
    y = (th - cp.height) // 2
    if cp.mode == "RGBA":
        card.paste(cp, (x, y), cp)
    else:
        card.paste(cp, (x, y))
    return card

def enhance(im):
    im = ImageEnhance.Contrast(im).enhance(1.06)
    im = ImageEnhance.Color(im).enhance(1.06)
    return im.filter(ImageFilter.UnsharpMask(radius=1.2, percent=60, threshold=2))

def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def rounded_paste(dst, src_im, xy, radius=20, shadow=True, border_color=None, border_w=2):
    x, y = xy
    w, h = src_im.size
    if shadow:
        sh = Image.new("RGBA", dst.size, (0, 0, 0, 0))
        ImageDraw.Draw(sh).rounded_rectangle([x + 4, y + 8, x + w + 4, y + h + 8], radius, fill=(15, 23, 42, 55))
        sh = sh.filter(ImageFilter.GaussianBlur(12))
        dst.paste(sh, (0, 0), sh)
    mask = Image.new("L", (w, h), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, w, h], radius, fill=255)
    dst.paste(src_im, (x, y), mask)
    if border_color:
        d = ImageDraw.Draw(dst)
        d.rounded_rectangle([x, y, x + w, y + h], radius, outline=border_color, width=border_w)

def draw_header_bar(canvas, pill_text, pill_bg, right_text="STORE.ITALSPORT-GROUP.IT"):
    d = ImageDraw.Draw(canvas)
    f_p = font(True, 19)
    pw = int(d.textlength(pill_text, font=f_p)) + 32
    d.rounded_rectangle([42, 32, 42 + pw, 72], 20, fill=pill_bg)
    d.text((42 + 16, 39), pill_text, font=f_p, fill=(255, 255, 255))

    lg_box_w, lg_box_h = 176, 54
    lx = W - 42 - lg_box_w
    ly = 25
    d.rounded_rectangle([lx, ly, lx + lg_box_w, ly + lg_box_h], 14, fill=(255, 255, 255), outline=(226, 232, 240), width=2)
    lg = LOGO.copy()
    lg.thumbnail((148, 42), Image.Resampling.LANCZOS)
    canvas.paste(lg, (lx + (lg_box_w - lg.width) // 2, ly + (lg_box_h - lg.height) // 2), lg)

def draw_footer_band(canvas, tag, tag_color, title, subtitle, pills=None):
    PHOTO_H = 770
    d = ImageDraw.Draw(canvas)
    d.rectangle([0, PHOTO_H, W, H], fill=(255, 255, 255))
    d.rectangle([0, PHOTO_H, W, PHOTO_H + 7], fill=tag_color)

    x = 46
    max_w = 780
    y = PHOTO_H + 24

    tf = font(True, 19)
    tw = int(d.textlength(tag, font=tf))
    d.rounded_rectangle([x, y, x + tw + 28, y + 34], radius=17, fill=tag_color)
    d.text((x + 14, y + 4), tag, font=tf, fill=(255, 255, 255))

    if pills:
        px = x + tw + 40
        pf = font(True, 17)
        for ptxt in pills:
            ptw = int(d.textlength(ptxt, font=pf))
            if px + ptw + 26 < W - 46:
                d.rounded_rectangle([px, y + 1, px + ptw + 24, y + 33], radius=16, fill=(241, 245, 249), outline=(203, 213, 225), width=1)
                d.text((px + 12, y + 5), ptxt, font=pf, fill=NAVY)
                px += ptw + 34

    y += 46
    f_t = font(True, 36)
    for line in wrap(d, title, f_t, max_w)[:2]:
        d.text((x, y), line, font=f_t, fill=NAVY)
        y += 43
    y += 6
    f_s = font(False, 22)
    for line in wrap(d, subtitle, f_s, max_w)[:2]:
        d.text((x, y), line, font=f_s, fill=SLATE)
        y += 28

    lg = LOGO.copy()
    lg.thumbnail((175, 84), Image.Resampling.LANCZOS)
    canvas.paste(lg, (W - lg.width - 42, H - lg.height - 34), lg)
    return canvas

# ==============================================================================
# POST 1: STAMPA DTF (Direct-to-Film) & REPARTO GRAFICO INTERNO
# ==============================================================================
def post1():
    canvas = Image.new("RGB", (W, H), (15, 23, 42))
    # Hero: Stampa DTF ad alta definizione (dal sito store.italsport-group.it)
    dtf_im = Image.open("store_dtf_real.jpg").convert("RGB")
    hero = enhance(cover(dtf_im, 640, 650, focus_y=0.45, focus_x=0.5))
    rounded_paste(canvas, hero, (36, 92), 22, border_color=BLUE, border_w=3)

    # Destra top: Graphic designer at work dal repo condiviso GitHub
    des_im = Image.open("gh_persona_preview.jpg").convert("RGB")
    c_top = enhance(cover(des_im, 348, 314, focus_y=0.4))
    rounded_paste(canvas, c_top, (696, 92), 20, border_color=(255, 255, 255), border_w=2)

    # Destra bottom: Reparto grafico interno mazzetta colori Pantone dal sito store
    rep_graf = Image.open("store_reparto_grafico.jpg").convert("RGB")
    c_bot = enhance(cover(rep_graf, 348, 314, focus_y=0.5))
    rounded_paste(canvas, c_bot, (696, 428), 20, border_color=AMBER, border_w=2)

    d = ImageDraw.Draw(canvas)
    d.rounded_rectangle([54, 668, 526, 720], 14, fill=(15, 23, 42))
    d.text((72, 680), "PELLICOLA TERMICA DTF AD ALTA RISOLUZIONE", font=font(True, 18), fill=CYAN)

    d.rounded_rectangle([712, 106, 1026, 146], 12, fill=(15, 23, 42))
    d.text((869, 115), "DESIGN & VETTORIALE INTERNO", font=font(True, 16), fill=(255, 255, 255), anchor="ma")

    draw_header_bar(canvas, "1 • TECNOLOGIA STAMPA DTF (DIRECT-TO-FILM)", BLUE)

    return draw_footer_band(
        canvas,
        "STAMPA DTF • STORE.ITALSPORT-GROUP.IT",
        BLUE,
        "DTF: Colori che durano, dettagli che contano su ogni tessuto",
        "Stampa morbida e indelebile su capi chiari e scuri già confezionati, resistente ai lavaggi ripetuti.",
        pills=["• Capi Chiari e Scuri", "• Morbida al Tatto", "• Alta Risoluzione"]
    )

def post1_s2():
    canvas = Image.new("RGB", (W, H), (241, 245, 249))
    tee_im = Image.open("gh_prod_training_tee.jpg").convert("RGB")
    left = enhance(contain_card(tee_im, 490, 650, (255, 255, 255), 10))
    rounded_paste(canvas, left, (38, 92), 22, border_color=BLUE, border_w=2)

    coll = Image.open(os.path.join(D_IG, "ig_post_11.jpg")).convert("RGB")
    right = enhance(contain_card(coll, 490, 650, (255, 255, 255), 6))
    rounded_paste(canvas, right, (552, 92), 22)

    draw_header_bar(canvas, "LABORATORIO STAMPA & PERSONALIZZAZIONI CISERANO", NAVY)
    return draw_footer_band(
        canvas,
        "REPARTO GRAFICO & STAMPA INTERNO",
        NAVY,
        "Dal file vettoriale al capo finito: zero limiti di cuciture",
        "Personalizziamo divise, tute, borse, k-way e abbigliamento da lavoro con impianti interni.",
        pills=["• Vetrofanie & Transfer", "• Quadricromia", "• Ricamo & DTF"]
    )

# ==============================================================================
# POST 2: STAMPA IN SUBLIMAZIONE & FULL PRINT ALL-OVER
# ==============================================================================
def post2():
    canvas = Image.new("RGB", (W, H), (15, 23, 42))

    # Sinistra: Splendida maglia tecnica da gara custom (dal repo condiviso GitHub, 1024x1024)
    jersey_custom = Image.open("gh_prod_match_jersey.jpg").convert("RGB")
    hero_left = enhance(cover(jersey_custom, 510, 650, focus_y=0.5))
    rounded_paste(canvas, hero_left, (36, 92), 22, border_color=GREEN, border_w=3)

    # Destra top: Foto ufficiale Stampa Sublimatica da store.italsport-group.it
    sub_macro = Image.open("store_sublimazione.jpg").convert("RGB")
    c_top = enhance(cover(sub_macro, 476, 314, focus_y=0.5))
    rounded_paste(canvas, c_top, (568, 92), 20, border_color=(255, 255, 255), border_w=2)

    # Destra bottom: Foto ufficiale Stampa Full Print prima della confezione
    fp_im = Image.open("store_full_print.jpg").convert("RGB")
    c_bot = enhance(cover(fp_im, 476, 314, focus_y=0.5))
    rounded_paste(canvas, c_bot, (568, 428), 20, border_color=CYAN, border_w=2)

    d = ImageDraw.Draw(canvas)
    d.rounded_rectangle([586, 110, 915, 150], 10, fill=(5, 150, 105))
    d.text((602, 117), "SUBLIMAZIONE 100% TRASPIRANTE", font=font(True, 17), fill=(255, 255, 255))

    d.rounded_rectangle([586, 446, 895, 486], 10, fill=BLUE)
    d.text((602, 453), "STAMPA FULL PRINT ALL-OVER", font=font(True, 17), fill=(255, 255, 255))

    draw_header_bar(canvas, "2 • STAMPA IN SUBLIMAZIONE & FULL PRINT", GREEN)

    return draw_footer_band(
        canvas,
        "STAMPA SUBLIMATICA • STORE.ITALSPORT-GROUP.IT",
        GREEN,
        "Sublimazione & Full Print: 100% traspirante e indelebile",
        "L'inchiostro entra nella fibra del poliestere senza ostruire i pori: impercettibile al tatto, non sbiadisce mai.",
        pills=["• Pori Liberi di Traspirare", "• Impercettibile al Tatto", "• All-Over Senza Limiti"]
    )

def post2_s2():
    canvas = Image.new("RGB", (W, H), (241, 245, 249))
    rodi = Image.open(os.path.join(D_STORE, "store_rodi_sublim.jpg")).convert("RGB")
    left = enhance(contain_card(rodi, 500, 650, (255, 255, 255), 14))
    rounded_paste(canvas, left, (36, 92), 22, border_color=GREEN, border_w=2)

    shorts = Image.open("gh_prod_shorts_velocity.jpg").convert("RGB")
    athene = Image.open(os.path.join(D_STORE, "store_athene_sublim.jpg")).convert("RGB")
    c1 = enhance(contain_card(shorts, 480, 314, (255, 255, 255), 10))
    c2 = enhance(contain_card(athene, 480, 314, (255, 255, 255), 14))
    rounded_paste(canvas, c1, (560, 92), 20, border_color=(203, 213, 225))
    rounded_paste(canvas, c2, (560, 428), 20, border_color=(203, 213, 225))

    d = ImageDraw.Draw(canvas)
    d.rounded_rectangle([578, 108, 860, 144], 10, fill=NAVY)
    d.text((592, 114), "PANTALONCINO SUBLIMATICO", font=font(True, 16), fill=(255, 255, 255))
    d.rounded_rectangle([578, 444, 880, 480], 10, fill=BLUE)
    d.text((592, 450), "MAGLIA ATHENE SUBLIM (STORE)", font=font(True, 16), fill=(255, 255, 255))

    draw_header_bar(canvas, "DIVISE SUBLIMATICHE & CATALOGO STORE", GREEN)
    return draw_footer_band(
        canvas,
        "LINEA CUSTOM & SUBLIMATICA ITALSPORT",
        GREEN,
        "Disegni esclusivi stampati sul tessuto prima della confezione",
        "Ideale per divise da calcio, volley, basket e running ad asciugatura rapida.",
        pills=["• Zero Imperfezioni", "• Colori Brillanti", "• Lavaggi Infiniti"]
    )

# ==============================================================================
# POST 3: SIMULATORE / CONFIGURATORE 3D ONLINE A 360°
# ==============================================================================
def post3():
    canvas = Image.new("RGB", (W, H), (241, 245, 249))

    # Sinistra: Grafica ufficiale "CONFIGURATORE 3D" di Italsport
    im_cfg = Image.open("site_configuratore.jpg").convert("RGB")
    c_left = enhance(contain_card(im_cfg, 616, 650, (255, 255, 255), 8))
    rounded_paste(canvas, c_left, (36, 92), 22, border_color=BLUE, border_w=3)

    # Destra: Vera rotazione 3D a 360° fronte e retro catturata dal configuratore Italsport
    gif = Image.open(os.path.join(D_WP1, "wp_config_gif2.gif"))
    gif.seek(10)
    fr_front = enhance(cover(gif.convert("RGB"), 372, 314, 0.5))
    gif.seek(185)
    fr_back = enhance(cover(gif.convert("RGB"), 372, 314, 0.5))
    rounded_paste(canvas, fr_front, (672, 92), 20, border_color=(203, 213, 225))
    rounded_paste(canvas, fr_back, (672, 428), 20, border_color=(203, 213, 225))

    d = ImageDraw.Draw(canvas)
    d.rounded_rectangle([690, 108, 916, 146], 10, fill=BLUE)
    d.text((803, 115), "360° VISTA 3D FRONTE", font=font(True, 17), fill=(255, 255, 255), anchor="ma")
    d.rounded_rectangle([690, 444, 916, 482], 10, fill=NAVY)
    d.text((803, 451), "360° VISTA 3D RETRO", font=font(True, 17), fill=(255, 255, 255), anchor="ma")

    draw_header_bar(canvas, "3 • SIMULATORE & CONFIGURATORE 3D ONLINE", BLUE)

    return draw_footer_band(
        canvas,
        "SIMULATORE 3D A 360° • ITALSPORT-GROUP.IT",
        BLUE,
        "Crea la divisa nel Simulatore 3D e ruotala a 360° prima dell'ordine",
        "Personalizza modello, colori societari, colletto, numeri e sponsor e segui lo stato di produzione.",
        pills=["• Rotazione 360° Live", "• Loghi & Sponsor", "• Tracking Produzione"]
    )

def post3_s2():
    canvas = Image.new("RGB", (W, H), (241, 245, 249))
    # 3D layout interface preview dal repo condiviso GitHub
    layout_3d = Image.open("gh_socialmedia3d_preview.jpg").convert("RGB")
    left = enhance(contain_card(layout_3d, 620, 650, (255, 255, 255), 6))
    rounded_paste(canvas, left, (36, 92), 22, border_color=BLUE, border_w=2)

    gif1 = Image.open(os.path.join(D_WP1, "wp_config_gif1.gif"))
    gif1.seek(5)
    b_front = enhance(cover(gif1.convert("RGB"), 368, 314, 0.5))
    gif1.seek(95)
    b_back = enhance(cover(gif1.convert("RGB"), 368, 314, 0.5))
    rounded_paste(canvas, b_front, (676, 92), 20, border_color=(203, 213, 225))
    rounded_paste(canvas, b_back, (676, 428), 20, border_color=(203, 213, 225))

    draw_header_bar(canvas, "COME FUNZIONA IL CONFIGURATORE IN 3 STEP", BLUE)
    return draw_footer_band(
        canvas,
        "DAL LAYOUT ALLA MESSA IN PRODUZIONE",
        BLUE,
        "1. Scegli lo sport • 2. Personalizza il capo • 3. Vai in produzione",
        "Calcio, basket, volley, rugby, tute e felpe: vedi l'anteprima 3D reale prima di confermare.",
        pills=["• Conferma -> Layout", "• Approvato -> Ordine", "• In Produzione"]
    )

# ==============================================================================
# POST 4: VETRINA DEDICATA ALLA PROPRIA SQUADRA E AI PROPRI CAPI (MY ITALSPORT)
# ==============================================================================
def post4():
    canvas = Image.new("RGB", (W, H), (15, 23, 42))

    # Top: Banner ufficiale "DIVENTA MEMBRO MY ITALSPORT - LA TUA VETRINA ONLINE" (store_myitalsport_banner.jpg)
    mem = Image.open("store_myitalsport_banner.jpg").convert("RGB")
    top_card = enhance(contain_card(mem, 1008, 326, (25, 28, 35), 4))
    rounded_paste(canvas, top_card, (36, 92), 22, border_color=CYAN, border_w=3)

    # In basso a sinistra: Giacca tuta ufficiale del club ad alta risoluzione (da GitHub condiviso)
    jacket_im = Image.open("gh_prod_track_jacket.jpg").convert("RGB")
    bot_left = enhance(contain_card(jacket_im, 492, 306, (255, 255, 255), 6))
    rounded_paste(canvas, bot_left, (36, 436), 20, border_color=(255, 255, 255), border_w=2)

    # In basso a destra: Maglia ufficiale da gara approvata per la squadra
    jersey_im = Image.open("gh_prod_match_jersey.jpg").convert("RGB")
    bot_right = enhance(contain_card(jersey_im, 492, 306, (255, 255, 255), 6))
    rounded_paste(canvas, bot_right, (552, 436), 20, border_color=GREEN, border_w=2)

    draw_header_bar(canvas, "4 • VETRINA DEDICATA SQUADRA • MY ITALSPORT", BLUE)

    return draw_footer_band(
        canvas,
        "MY ITALSPORT • STORE.ITALSPORT-GROUP.IT",
        DARK_BLUE,
        "Una Vetrina Online dedicata solo alla tua squadra e ai tuoi capi",
        "Ogni società accede con password riservata: atleti e genitori vedono e ordinano solo il kit ufficiale del club.",
        pills=["• Accesso con Password", "• Solo i Capi del Club", "• Zero Costi Magazzino"]
    )

def post4_s2():
    canvas = Image.new("RGB", (W, H), (241, 245, 249))
    vet_banner = Image.open(os.path.join(D_WP1, "wp_vetrina_proclub.jpg")).convert("RGB")
    top_b = enhance(contain_card(vet_banner, 1008, 290, (255, 255, 255), 4))
    rounded_paste(canvas, top_b, (36, 92), 20, border_color=DARK_BLUE, border_w=2)

    partner_im = Image.open("store_partner_affidabile.jpg").convert("RGB")
    bot_l = enhance(contain_card(partner_im, 492, 340, (245, 226, 168), 4))
    rounded_paste(canvas, bot_l, (36, 402), 20)

    solo_vant = Image.open(os.path.join(D_IG, "sbi_17876753447512708.jpg")).convert("RGB")
    bot_r = enhance(contain_card(solo_vant, 492, 340, (255, 255, 255), 4))
    rounded_paste(canvas, bot_r, (552, 402), 20)

    draw_header_bar(canvas, "PORTALE SOCIETÀ SPORTIVE • MY ITALSPORT", DARK_BLUE)
    return draw_footer_band(
        canvas,
        "TU SCEGLI ITALSPORT, AL RESTO PENSIAMO NOI",
        DARK_BLUE,
        "Basta fogli Excel e scatoloni in segreteria: gestiamo tutto noi",
        "Confezionamento singolo per atleta, scarico barcode e consegne puntuali per tutta la stagione.",
        pills=["• Ordina il Kit Online", "• Consegne Rapide", "• Dashboard Documenti"]
    )

# ==============================================================================
# POST 5: CONTINUITÀ NEGLI ANNI, ZERO MAGAZZINO & TESSERA PRO-CLUB
# ==============================================================================
def post5():
    canvas = Image.new("RGB", (W, H), (15, 23, 42))

    # Top: Slider ufficiale ad alta risoluzione "ITALSPORT FORNITURE: IL TUO MAGAZZINO LO FACCIAMO NOI!" (store_prezzo_misura.jpg)
    sl_forn = Image.open("store_prezzo_misura.jpg").convert("RGB")
    top_im = enhance(contain_card(sl_forn, 1008, 300, (238, 242, 246), 4))
    rounded_paste(canvas, top_im, (36, 92), 20, border_color=AMBER, border_w=3)

    # In basso a sinistra: Card ufficiale Pro-Club
    cards_im = Image.open("card_proclub_real.jpg").convert("RGB")
    bot_left = enhance(contain_card(cards_im, 492, 330, (251, 224, 91), 4))
    rounded_paste(canvas, bot_left, (36, 412), 20, border_color=GOLD, border_w=2)

    # In basso a destra: La linea continuativa club da ig_post_12.jpg
    coll_12 = Image.open(os.path.join(D_IG, "ig_post_12.jpg")).convert("RGB")
    bot_right = enhance(contain_card(coll_12, 492, 330, (38, 38, 38), 4))
    rounded_paste(canvas, bot_right, (552, 412), 20, border_color=(255, 255, 255), border_w=2)

    draw_header_bar(canvas, "5 • CONTINUITÀ RIASSORTIMENTI & TESSERA PRO-CLUB", AMBER)

    return draw_footer_band(
        canvas,
        "TESSERA PRO-CLUB & CONTINUITÀ GARANTITA",
        AMBER,
        "Il tuo magazzino a Ciserano lo facciamo noi: continuità negli anni",
        "Nuovo iscritto a metà stagione o dopo 3 anni? Ritrovi sempre la stessa linea, stessi colori e listino bloccato.",
        pills=["• Basic • Silver • Gold • Diamond", "• Riassortimenti Garantiti", "• Zero Rimanenze"]
    )

def post5_s2():
    canvas = Image.new("RGB", (W, H), (241, 245, 249))
    coll_12 = Image.open(os.path.join(D_IG, "ig_post_12.jpg")).convert("RGB")
    left = enhance(contain_card(coll_12, 620, 650, (38, 38, 38), 6))
    rounded_paste(canvas, left, (36, 92), 22)

    part_aff = Image.open("store_partner_affidabile.jpg").convert("RGB")
    r_top = enhance(contain_card(part_aff, 368, 314, (245, 226, 168), 4))
    rounded_paste(canvas, r_top, (676, 92), 20)

    linea_im = Image.open("store_la_tua_linea.jpg").convert("RGB")
    r_bot = enhance(contain_card(linea_im, 368, 314, (24, 34, 48), 4))
    rounded_paste(canvas, r_bot, (676, 428), 20)

    draw_header_bar(canvas, "COLLEZIONI PERMANENTI NEL TEMPO • LINEA CLUB", AMBER)
    return draw_footer_band(
        canvas,
        "FORNITURE CONTINUATIVE SENZA SORPRESE",
        AMBER,
        "Tuta Rom, Polo, Giacca Scotland, Giubbotto Nepal, K-Way e Borsa",
        "Tutta la linea ufficiale della tua società sempre disponibile a magazzino in tutte le taglie.",
        pills=["• Taglie Bambino/Uomo/Donna", "• Listino Parametrico Club"]
    )

# ==============================================================================
# POST 6: 30 ANNI DI STORIA, 4.600+ REALTÀ IN CRM, LINEA FLAME & MULTI-BRAND
# ==============================================================================
def post6():
    canvas = Image.new("RGB", (W, H), (15, 23, 42))

    # 1. Slider alta risoluzione "SCEGLI LA TUA LINEA DI PRODOTTI E SERVIZI ITALSPORT"
    linea_im = Image.open("store_la_tua_linea.jpg").convert("RGB")
    top_b = enhance(contain_card(linea_im, 1008, 310, (24, 34, 48), 2))
    rounded_paste(canvas, top_b, (36, 92), 20, border_color=BLUE, border_w=3)

    # 2. Slider alta risoluzione MULTI-BRAND da store.italsport-group.it
    mb_im = Image.open("store_multibrand.jpg").convert("RGB")
    bot_l = enhance(contain_card(mb_im, 540, 322, (255, 255, 255), 6))
    rounded_paste(canvas, bot_l, (36, 420), 20, border_color=(203, 213, 225), border_w=2)

    # 3. Splendida foto reale showroom teamwear e abbigliamento sportivo dal repo condiviso GitHub (2560x1428)
    apparel_im = Image.open("gh_abbigliamento.jpeg").convert("RGB")
    bot_r = enhance(cover(apparel_im, 448, 322, focus_y=0.45, focus_x=0.5))
    rounded_paste(canvas, bot_r, (596, 420), 20, border_color=GREEN, border_w=2)

    draw_header_bar(canvas, "6 • 30 ANNI DI STORIA • LINEA FLAME & MULTI-BRAND", BLUE)

    return draw_footer_band(
        canvas,
        "OLTRE 4.600 SOCIETÀ, ORATORI, SCUOLE & AZIENDE",
        BLUE,
        "L'esclusiva Linea Flame Italsport e i migliori Brand in un unico partner",
        "Da 30 anni vestiamo calcio, volley, basket, rugby, atletica, oratori e aziende con logistica puntuale.",
        pills=["• Linea Flame Custom", "• Multi-Brand & Multi-Sport", "• 2.600+ Articoli Attivi"]
    )

def post6_s2():
    canvas = Image.new("RGB", (W, H), (241, 245, 249))
    # Sinistra: I settori sportivi reali serviti da Italsport (site_settori.jpg)
    sett_im = Image.open("site_settori.jpg").convert("RGB")
    left = enhance(contain_card(sett_im, 492, 650, (255, 255, 255), 6))
    rounded_paste(canvas, left, (36, 92), 22, border_color=BLUE, border_w=2)

    apparel_im = Image.open("gh_abbigliamento.jpeg").convert("RGB")
    r_top = enhance(cover(apparel_im, 492, 314, 0.45, 0.5))
    rounded_paste(canvas, r_top, (552, 92), 20)

    prom_im = Image.open(os.path.join(D_WP1, "wp_promozionale.jpg")).convert("RGB")
    r_bot = enhance(cover(prom_im, 492, 314, 0.5))
    rounded_paste(canvas, r_bot, (552, 428), 20)

    draw_header_bar(canvas, "SPORT, SCUOLE, ORATORI, LAVORO & PROMOZIONALE", BLUE)
    return draw_footer_band(
        canvas,
        "SHOWROOM CISERANO (BG) • VIA PROV. FRANCESCA 2H/I",
        BLUE,
        "Abbigliamento sportivo, da lavoro, promozionale, coppe e trofei",
        "Un unico referente per vestire la tua società sportiva, il tuo evento o la tua azienda.",
        pills=["• Sport & Oratori", "• Aziende & Lavoro", "• Premiazioni & Gadget"]
    )

# ==============================================================================
# POST 7: AUGURI DI NATALE & IDEE REGALO PERSONALIZZATE PER LE SQUADRE
# ==============================================================================
def post7():
    canvas = Image.new("RGB", (W, H), (12, 24, 56))

    xmas_im = Image.open(os.path.join(D_IG, "sbi_18099813430370704.jpg")).convert("RGB")
    hero_l = enhance(contain_card(xmas_im, 530, 650, (14, 28, 64), 4))
    rounded_paste(canvas, hero_l, (36, 92), 22, border_color=GOLD, border_w=3)

    reg_im = Image.open(os.path.join(D_IG, "ig_post_02.jpg")).convert("RGB")
    c_top = enhance(contain_card(reg_im, 456, 314, (255, 255, 255), 4))
    rounded_paste(canvas, c_top, (588, 92), 20, border_color=(255, 255, 255), border_w=2)

    sw_im = Image.open(os.path.join(D_IG, "ig_post_03.jpg")).convert("RGB")
    c_bot = enhance(contain_card(sw_im, 456, 314, (21, 41, 56), 4))
    rounded_paste(canvas, c_bot, (588, 428), 20, border_color=RED, border_w=2)

    draw_header_bar(canvas, "7 • AUGURI DI NATALE & REGALI SQUADRA • ITALSPORT", RED)

    return draw_footer_band(
        canvas,
        "BUON NATALE E BUONE FESTE DAL TEAM DI ITALSPORT",
        RED,
        "Tanti auguri di Buon Natale a tutte le società sportive e agli atleti!",
        "Grazie a chi scende in campo con noi: vi aspettiamo a Ciserano per un 2027 ricco di sport e vittorie.",
        pills=["• Buone Feste dal Team Italsport", "• Gadget & Regali Club", "• Ciserano (BG)"]
    )

def post7_s2():
    canvas = Image.new("RGB", (W, H), (241, 245, 249))
    reg_im = Image.open(os.path.join(D_IG, "ig_post_02.jpg")).convert("RGB")
    left = enhance(contain_card(reg_im, 492, 650, (255, 255, 255), 4))
    rounded_paste(canvas, left, (36, 92), 22)

    sw_im = Image.open(os.path.join(D_IG, "ig_post_03.jpg")).convert("RGB")
    right = enhance(contain_card(sw_im, 492, 650, (20, 41, 58), 4))
    rounded_paste(canvas, right, (552, 92), 22)

    draw_header_bar(canvas, "IDEE REGALO NATALIZIE & INVERNALI PER IL TUO CLUB", RED)
    return draw_footer_band(
        canvas,
        "GADGET, FELPE, SCIARPE & MAGLIONI NATALIZI CUSTOM",
        RED,
        "Rendi unico il Natale della tua società sportiva col vostro logo",
        "Zainetti, berretti, sciarpe, borracce, felpe e maglioni natalizi personalizzati nel nostro showroom.",
        pills=["• Maglioni Custom 360°", "• Sciarpe & Cappellini", "• Regali Societari"]
    )

posts = [
    ("img_post1_jersey.jpg", post1),
    ("img_post1_s2.jpg", post1_s2),
    ("img_post2_3d.jpg", post2),
    ("img_post2_s2.jpg", post2_s2),
    ("img_post3_fidelity.jpg", post3),
    ("img_post3_s2.jpg", post3_s2),
    ("img_post4_stack.jpg", post4),
    ("img_post4_s2.jpg", post4_s2),
    ("img_post5_portal.jpg", post5),
    ("img_post5_s2.jpg", post5_s2),
    ("img_post6_winter.jpg", post6),
    ("img_post6_s2.jpg", post6_s2),
    ("img_post7_celebration.jpg", post7),
    ("img_post7_s2.jpg", post7_s2),
]

for fn, f in posts:
    f().save(fn, quality=93)
    print("Generated", fn)
