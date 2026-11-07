"""Genera i 7 post Instagram (1080x1080) per ITALSPORT GROUP — Ciserano (BG)
usando ESCLUSIVAMENTE le vere foto/grafiche di Italsport (@italsportgroup e italsport-group.it)
migliorate e impaginate in modo pulito, senza alcuna scritta tagliata o sovrapposta.
"""
import os, shutil
from PIL import Image, ImageEnhance, ImageDraw, ImageFont, ImageFilter

W, H = 1080, 1080
PHOTO_H = 760
NAVY = (15, 23, 42)
SLATE = (71, 85, 105)
BLUE = (2, 132, 199)
DEEP_BLUE = (30, 58, 138)
AMBER = (217, 119, 6)
GREEN = (5, 150, 105)
FONTS = r"C:\Windows\Fonts"

D_IG = r"C:\Users\salvo\.gemini\antigravity\brain\dc9abd1d-f990-4c44-a20b-bd6ec7f9af7d\scratch\ig_real"
D_WP1 = r"C:\Users\salvo\.gemini\antigravity\brain\dc9abd1d-f990-4c44-a20b-bd6ec7f9af7d\scratch\wp_dl"
D_WP2 = r"C:\Users\salvo\.gemini\antigravity\brain\dc9abd1d-f990-4c44-a20b-bd6ec7f9af7d\scratch\wp_dl2"

LOGO = Image.open("cropped-cropped-italsportlogo.png").convert("RGBA")

gif_src = os.path.join(D_WP1, "wp_config_gif2.gif")
if os.path.exists(gif_src):
    shutil.copy2(gif_src, "configuratore3d_real.gif")


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


def enhance(im):
    im = ImageEnhance.Contrast(im).enhance(1.06)
    im = ImageEnhance.Color(im).enhance(1.06)
    return im.filter(ImageFilter.UnsharpMask(radius=1.3, percent=65, threshold=2))


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


def band_post(photo, tag, tag_color, title, subtitle):
    canvas = Image.new("RGB", (W, H), (255, 255, 255))
    canvas.paste(photo, (0, 0))
    d = ImageDraw.Draw(canvas)
    d.rectangle([0, PHOTO_H, W, PHOTO_H + 6], fill=tag_color)

    x, max_w = 52, 790
    y = PHOTO_H + 30
    tf = font(True, 20)
    tw = d.textlength(tag, font=tf)
    d.rounded_rectangle([x, y, x + tw + 28, y + 36], radius=18, fill=tag_color)
    d.text((x + 14, y + 5), tag, font=tf, fill=(255, 255, 255))
    y += 50

    f_t = font(True, 38)
    for line in wrap(d, title, f_t, max_w)[:2]:
        d.text((x, y), line, font=f_t, fill=NAVY)
        y += 46
    y += 6
    f_s = font(False, 23)
    for line in wrap(d, subtitle, f_s, max_w)[:2]:
        d.text((x, y), line, font=f_s, fill=SLATE)
        y += 30

    lg = LOGO.copy()
    lg.thumbnail((170, 84))
    canvas.paste(lg, (W - lg.width - 44, H - lg.height - 38), lg)
    return canvas


def rounded_paste(dst, src_im, xy, radius=18, shadow=True):
    x, y = xy
    w, h = src_im.size
    if shadow:
        sh = Image.new("RGBA", dst.size, (0, 0, 0, 0))
        ImageDraw.Draw(sh).rounded_rectangle([x + 4, y + 10, x + w + 4, y + h + 10], radius, fill=(15, 23, 42, 45))
        sh = sh.filter(ImageFilter.GaussianBlur(12))
        dst.paste(sh, (0, 0), sh)
    mask = Image.new("L", (w, h), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, w, h], radius, fill=255)
    dst.paste(src_im, (x, y), mask)


# POST 1: Produzione Custom & Divise Italsport (3 vere maglie/kit Italsport su manichino senza testo tagliato)
def post1():
    bg = Image.new("RGB", (W, PHOTO_H), (18, 27, 46))
    im_left = Image.open(os.path.join(D_IG, "sbi_17885178626300926.jpg")).convert("RGB")
    im_mid = Image.open(os.path.join(D_IG, "ig_post_17.jpg")).convert("RGB")
    im_mid = im_mid.crop((0, 0, im_mid.width, int(im_mid.height * 0.85)))  # via l'url in basso
    im_right = Image.open(os.path.join(D_IG, "sbi_17909215715015535.jpg")).convert("RGB")

    c1 = enhance(cover(im_left, 310, 660, 0.5))
    c2 = enhance(cover(im_mid, 350, 660, 0.45))
    c3 = enhance(cover(im_right, 310, 660, 0.5))

    rounded_paste(bg, c1, (36, 50), 20)
    rounded_paste(bg, c2, (365, 50), 20)
    rounded_paste(bg, c3, (734, 50), 20)

    return band_post(
        bg,
        "PRODUZIONE CUSTOM • CISERANO (BG)",
        BLUE,
        "Divise personalizzate col tuo logo, fatte per durare",
        "30 anni di forniture sportive: stampa, ricamo e capi resistenti ai lavaggi ripetuti."
    )


# POST 2: Configuratore 3D Reale (vera maglia 3D Italsport + schermata configuratore)
def post2():
    bg = Image.new("RGB", (W, PHOTO_H), (241, 245, 249))
    im_cfg = Image.open("site_configuratore.jpg").convert("RGB")
    im_cfg = im_cfg.crop((0, int(im_cfg.height * 0.21), im_cfg.width, im_cfg.height))
    c_left = enhance(cover(im_cfg, 620, 660, 0.5))
    rounded_paste(bg, c_left, (38, 50), 22)

    gif = Image.open(os.path.join(D_WP1, "wp_config_gif2.gif"))
    gif.seek(10)
    fr_front = enhance(cover(gif.convert("RGB"), 350, 318, 0.5))
    gif.seek(185)
    fr_back = enhance(cover(gif.convert("RGB"), 350, 318, 0.5))
    rounded_paste(bg, fr_front, (688, 50), 18)
    rounded_paste(bg, fr_back, (688, 392), 18)

    d = ImageDraw.Draw(bg)
    d.rounded_rectangle([704, 64, 830, 98], 10, fill=BLUE)
    d.text((767, 71), "VISTA 360°", font=font(True, 18), fill=(255, 255, 255), anchor="ma")
    d.rounded_rectangle([704, 406, 830, 440], 10, fill=NAVY)
    d.text((767, 413), "RETRO 3D", font=font(True, 18), fill=(255, 255, 255), anchor="ma")

    return band_post(
        bg,
        "CONFIGURATORE 3D ONLINE",
        BLUE,
        "Disegna la divisa in 3D e girala a 360° prima dell'ordine",
        "Scegli modello, colori, colletto, numeri e sponsor su italsport-group.it"
    )


# POST 3: La Vera Tessera PRO-CLUB di Italsport (Basic, Silver, Gold, Diamond)
def post3():
    bg = Image.new("RGB", (W, PHOTO_H), (248, 250, 252))
    d = ImageDraw.Draw(bg)

    # Ritagliamo ESATTAMENTE la tessera Pro-Club ufficiale di Italsport da slider_5.jpg (4625x1417)
    sl5 = Image.open(os.path.join(D_WP2, "slider_5.jpg")).convert("RGB")
    real_card = sl5.crop((3345, 830, 4445, 1345))
    real_card = enhance(real_card.resize((468, 232), Image.Resampling.LANCZOS))
    rounded_paste(bg, real_card, (56, 58), 18)

    # E a destra i 4 livelli ufficiali della Tessera Pro-Club (Basic, Silver, Gold, Diamond)
    tiers = [
        ("PRO CLUB BASIC", "1° Livello • Listino Club", (30, 64, 175), (219, 234, 254)),
        ("PRO CLUB SILVER", "2° Livello • Sconto Extra", (71, 85, 105), (226, 232, 240)),
        ("PRO CLUB GOLD", "3° Livello • Bonus Fornitura", (180, 83, 9), (254, 243, 199)),
        ("PRO CLUB DIAMOND", "4° Livello • Partner Top", (15, 23, 42), (224, 242, 254)),
    ]
    for idx, (tname, tsub, tc, tbg) in enumerate(tiers):
        tx = 554 + (idx % 2) * 240
        ty = 58 + (idx // 2) * 120
        d.rounded_rectangle([tx, ty, tx + 228, ty + 108], 14, fill=tc)
        d.rounded_rectangle([tx + 12, ty + 14, tx + 96, ty + 36], 8, fill=tbg)
        d.text((tx + 54, ty + 17), "TESSERA", font=font(True, 13), fill=tc, anchor="ma")
        d.text((tx + 14, ty + 46), tname, font=font(True, 18), fill=(255, 255, 255))
        d.text((tx + 14, ty + 74), tsub, font=font(False, 14), fill=(203, 213, 225))

    benefits = [
        ("Linea sempre disponibile", "Facciamo noi il magazzino per la tua società: zero anticipi e zero rimanenze."),
        ("Prezzi e sconti dedicati", "Livelli Basic, Silver, Gold e Diamond con listino riservato al club."),
        ("Continuità negli anni", "Stessi modelli e stessi colori garantiti anche per i riordini futuri."),
        ("Vetrina squadra inclusa", "Accesso con password per ordinare solo i capi ufficiali della società.")
    ]
    for i, (bt, bd) in enumerate(benefits):
        bx = 56 if i % 2 == 0 else 554
        by = 336 + (i // 2) * 190
        d.rounded_rectangle([bx, by, bx + 470, by + 168], 16, fill=(255, 255, 255), outline=(226, 232, 240), width=2)
        d.rounded_rectangle([bx, by, bx + 8, by + 168], 4, fill=AMBER)
        d.text((bx + 28, by + 22), bt, font=font(True, 26), fill=NAVY)
        f_b = font(False, 21)
        yy = by + 64
        for line in wrap(d, bd, f_b, 420)[:3]:
            d.text((bx + 28, yy), line, font=f_b, fill=SLATE)
            yy += 28

    return band_post(
        bg,
        "TESSERA PRO-CLUB ITALSPORT",
        AMBER,
        "Card Pro-Club: più vantaggi per la tua società sportiva",
        "Zero costi di magazzino, listino bloccato e continuità garantita sulle forniture."
    )


# POST 4: Continuità e Riassortimenti (i 9 veri capi della linea club da ig_post_12.jpg)
def post4():
    im = Image.open(os.path.join(D_IG, "ig_post_12.jpg")).convert("RGB")
    im_grid = im.crop((0, int(im.height * 0.305), im.width, im.height))
    bg = Image.new("RGB", (W, PHOTO_H), (38, 38, 38))
    fit = enhance(cover(im_grid, W - 80, PHOTO_H - 60, 0.5))
    rounded_paste(bg, fit, (40, 30), 18, shadow=False)

    return band_post(
        bg,
        "CONTINUITÀ & RIASSORTIMENTI",
        GREEN,
        "Nuovo iscritto a metà stagione? Ritrova la stessa linea",
        "Tute, kit gara, giacche, k-way e borse sempre riordinabili identici negli anni."
    )


# POST 5: La Vetrina Dedicata con Password per Ogni Squadra (My Italsport)
def post5():
    bg = Image.new("RGB", (W, PHOTO_H), (241, 245, 249))
    d = ImageDraw.Draw(bg)

    d.rounded_rectangle([40, 48, 496, 712], 22, fill=NAVY)
    d.rounded_rectangle([68, 80, 290, 116], 18, fill=(2, 132, 199))
    d.text((179, 87), "AREA RISERVATA CLUB", font=font(True, 17), fill=(255, 255, 255), anchor="ma")

    d.text((68, 138), "Accesso Vetrina\ndella Tua Squadra", font=font(True, 34), fill=(255, 255, 255))
    d.text((68, 240), "Ogni società entra con la sua\npassword e vede solo i propri capi.", font=font(False, 21), fill=(203, 213, 225))

    d.rounded_rectangle([68, 322, 468, 400], 12, fill=(30, 41, 59), outline=(71, 85, 105), width=2)
    d.text((88, 334), "SOCIETÀ SPORTIVA", font=font(True, 14), fill=(148, 163, 184))
    d.text((88, 358), "U.S.D. Brevianese / Gessate", font=font(True, 22), fill=(255, 255, 255))

    d.rounded_rectangle([68, 418, 468, 496], 12, fill=(30, 41, 59), outline=(2, 132, 199), width=2)
    d.text((88, 430), "PASSWORD DEDICATA SQUADRA", font=font(True, 14), fill=(56, 189, 248))
    d.text((88, 454), "••••••••••••   [ Accesso Protetto ]", font=font(True, 21), fill=(255, 255, 255))

    pts = [
        "Vedi SOLO i capi della tua squadra",
        "Trovi sempre gli stessi articoli",
        "Zero magazzino per la società"
    ]
    yy = 530
    for pt in pts:
        d.ellipse([68, yy + 4, 92, yy + 28], fill=(5, 150, 105))
        d.line([(74, yy + 16), (79, yy + 21), (86, yy + 10)], fill=(255, 255, 255), width=3)
        d.text((104, yy), pt, font=font(True, 20), fill=(241, 245, 249))
        yy += 52

    vet = Image.open("site_vetrina_servizi.jpg").convert("RGB")
    # Solo il riquadro verde con gli 8 capi custom (0..43% dell'altezza, senza la scritta tagliata sotto)
    vet_top = enhance(vet.crop((8, 8, vet.width - 8, int(vet.height * 0.435))).resize((520, 290), Image.Resampling.LANCZOS))
    rounded_paste(bg, vet_top, (520, 48), 18)

    j1 = Image.open(os.path.join(D_IG, "ig_post_17.jpg")).convert("RGB")
    j1 = enhance(cover(j1.crop((0, 0, j1.width, int(j1.height * 0.88))), 248, 275))
    j2 = Image.open(os.path.join(D_IG, "sbi_17942943826533954.jpg")).convert("RGB")
    j2 = enhance(cover(j2.crop((int(j2.width * 0.12), int(j2.height * 0.16), int(j2.width * 0.88), int(j2.height * 0.86))), 248, 275))

    for idx, (jim, lbl) in enumerate([(j1, "Kit Gara Ufficiale Club"), (j2, "Maglia Rappresentanza")]):
        px = 520 + idx * 272
        d.rounded_rectangle([px, 364, px + 248, 712], 18, fill=(255, 255, 255), outline=(226, 232, 240), width=2)
        rounded_paste(bg, jim, (px, 364), 18, shadow=False)
        d.text((px + 124, 654), lbl, font=font(True, 20), fill=NAVY, anchor="ma")
        d.text((px + 124, 682), "Sempre disponibile", font=font(False, 17), fill=GREEN, anchor="ma")

    return band_post(
        bg,
        "MY ITALSPORT • VETRINA CON PASSWORD",
        DEEP_BLUE,
        "Una vetrina con password riservata solo alla tua squadra",
        "Accedi e trovi solo i capi ufficiali del tuo club: sempre gli stessi, senza errori."
    )


# POST 6: In Campo con le Divise Italsport (vera foto squadra con maglie ITALSPORT PRINTSPORT)
def post6():
    im = Image.open(os.path.join(D_WP2, "italsport_11.png")).convert("RGB")
    p = enhance(cover(im, W, PHOTO_H, 0.35))
    return band_post(
        p,
        "SUL CAMPO CON VOI",
        BLUE,
        "Oltre 4.600 realtà tra società sportive, oratori e scuole",
        "Calcio, volley, basket, rugby, atletica: vestiamo lo sport a Ciserano e in Lombardia."
    )


# POST 7: Showroom Ciserano, Invernale & Gadget per le Feste di Fine Anno
def post7():
    bg = Image.new("RGB", (W, PHOTO_H), (18, 27, 46))
    shw = Image.open(os.path.join(D_IG, "sbi_18095471020372884.jpg")).convert("RGB")
    c_left = enhance(cover(shw, 560, 664, 0.5))
    rounded_paste(bg, c_left, (38, 48), 20)

    # Destra in alto: felpa tecnica Italsport su manichino (zero scritte tagliate)
    hood = Image.open(os.path.join(D_IG, "sbi_17923615036652468.jpg")).convert("RGB")
    c_top = enhance(cover(hood, 418, 318, 0.35))
    rounded_paste(bg, c_top, (622, 48), 18)

    # Destra in basso: maglioni/invernale custom da ig_post_03.jpg (solo la parte illustrata superiore)
    win = Image.open(os.path.join(D_IG, "ig_post_03.jpg")).convert("RGB")
    win_crop = win.crop((0, 0, win.width, int(win.height * 0.68)))
    c_bot = enhance(cover(win_crop, 418, 318, 0.5))
    rounded_paste(bg, c_bot, (622, 394), 18)

    return band_post(
        bg,
        "SHOWROOM CISERANO • INVERNALE & GADGET",
        AMBER,
        "Tute, felpe, borse e gadget col logo della tua squadra",
        "Passa in showroom a Ciserano (Via Provinciale Francesca 2H/I) o scrivici in DM."
    )


posts = [
    ("img_post1_jersey.jpg", post1),
    ("img_post2_3d.jpg", post2),
    ("img_post3_fidelity.jpg", post3),
    ("img_post4_stack.jpg", post4),
    ("img_post5_portal.jpg", post5),
    ("img_post6_winter.jpg", post6),
    ("img_post7_celebration.jpg", post7),
]

for fn, f in posts:
    f().save(fn, quality=92)
    print("Generated", fn)
