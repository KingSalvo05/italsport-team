import os, io, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# Helper to load fonts safely
def get_font(size, bold=False):
    font_name = 'segoeuib.ttf' if bold else 'segoeui.ttf'
    path = os.path.join('C:\\Windows\\Fonts', font_name)
    if os.path.exists(path):
        return ImageFont.truetype(path, size)
    font_name = 'arialbd.ttf' if bold else 'arial.ttf'
    path = os.path.join('C:\\Windows\\Fonts', font_name)
    if os.path.exists(path):
        return ImageFont.truetype(path, size)
    return ImageFont.load_default()

logo_img = Image.open('cropped-cropped-italsportlogo.png').convert('RGBA')

# -------------------------------------------------------------
# POST 1: 30 Anni di Passione (Real Locker Room Jersey)
# -------------------------------------------------------------
def make_post1():
    base = Image.open('real_post1_jersey.jpg').convert('RGBA')
    # Crop to 1080x1080
    w, h = base.size
    min_dim = min(w, h)
    left = (w - min_dim) // 2
    top = (h - min_dim) // 2
    base = base.crop((left, top, left + min_dim, top + min_dim)).resize((1080, 1080), Image.Resampling.LANCZOS)
    
    # Create dark gradient overlay
    overlay = Image.new('RGBA', (1080, 1080), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    # Top gradient
    for y in range(250):
        alpha = int(180 * (1 - y / 250))
        draw.line([(0, y), (1080, y)], fill=(10, 15, 25, alpha))
        
    # Bottom gradient
    for y in range(450):
        alpha = int(220 * (y / 450))
        draw.line([(0, 1080 - 450 + y), (1080, 1080 - 450 + y)], fill=(9, 13, 22, alpha))
        
    composite = Image.alpha_composite(base, overlay)
    draw = ImageDraw.Draw(composite)
    
    # Top bar badge
    draw.rounded_rectangle([60, 50, 290, 95], radius=8, fill=(16, 185, 129, 230))
    f_badge = get_font(20, bold=True)
    draw.text((78, 62), "MANIFATTURA ITALIANA", font=f_badge, fill=(255, 255, 255))
    
    # Tricolor bar
    draw.rectangle([60, 105, 110, 110], fill=(0, 146, 70))
    draw.rectangle([110, 105, 160, 110], fill=(241, 242, 241))
    draw.rectangle([160, 105, 210, 110], fill=(206, 43, 55))
    
    # Logo on top right
    l_w = 200
    l_h = int(logo_img.size[1] * (l_w / logo_img.size[0]))
    resized_logo = logo_img.resize((l_w, l_h), Image.Resampling.LANCZOS)
    composite.paste(resized_logo, (1080 - l_w - 60, 50), resized_logo)
    
    # Bottom text
    f_title = get_font(52, bold=True)
    f_sub = get_font(28, bold=True)
    f_body = get_font(22, bold=False)
    
    draw.text((60, 810), "30 ANNI IN CAMPO", font=f_sub, fill=(52, 211, 153))
    draw.text((60, 850), "LA PASSIONE CHE DIVENTA DIVISA", font=f_title, fill=(255, 255, 255))
    draw.text((60, 925), "Sartoria sportiva, personalizzazione HD e qualità al servizio del tuo club.", font=f_body, fill=(203, 213, 225))
    draw.text((60, 960), '"Tu scegli Italsport, al resto pensiamo noi."', font=f_body, fill=(148, 163, 184))
    
    composite.convert('RGB').save('img_post1_jersey.jpg', quality=90)
    print("Post 1 created successfully.")

# -------------------------------------------------------------
# POST 2: Configuratore 3D (Clean Digital Interface Mockup)
# -------------------------------------------------------------
def make_post2():
    # Create high-tech dark studio background
    im = Image.new('RGBA', (1080, 1080), (13, 17, 28, 255))
    draw = ImageDraw.Draw(im)
    
    # Background subtle grid lines
    for x in range(0, 1080, 60):
        draw.line([(x, 0), (x, 1080)], fill=(25, 33, 50, 120), width=1)
    for y in range(0, 1080, 60):
        draw.line([(0, y), (1080, y)], fill=(25, 33, 50, 120), width=1)
        
    # Ambient radial glow in center
    glow = Image.new('RGBA', (1080, 1080), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow)
    for r in range(400, 0, -5):
        alpha = int(45 * (1 - r / 400))
        glow_draw.ellipse([540 - r, 500 - r, 540 + r, 500 + r], fill=(16, 185, 129, alpha))
    im = Image.alpha_composite(im, glow)
    draw = ImageDraw.Draw(im)
    
    # Top header
    draw.rounded_rectangle([60, 50, 310, 95], radius=8, fill=(14, 165, 233, 230))
    f_badge = get_font(20, bold=True)
    draw.text((78, 62), "INNOVAZIONE DIGITALE", font=f_badge, fill=(255, 255, 255))
    
    # Logo top right
    l_w = 200
    l_h = int(logo_img.size[1] * (l_w / logo_img.size[0]))
    resized_logo = logo_img.resize((l_w, l_h), Image.Resampling.LANCZOS)
    im.paste(resized_logo, (1080 - l_w - 60, 50), resized_logo)
    
    # 3D Viewport Box
    draw.rounded_rectangle([120, 150, 960, 780], radius=16, fill=(19, 26, 43, 240), outline=(56, 189, 248, 180), width=2)
    
    # Top bar of viewport
    draw.rectangle([120, 150, 960, 205], fill=(30, 41, 59, 255))
    draw.ellipse([140, 172, 152, 184], fill=(239, 68, 68))
    draw.ellipse([162, 172, 174, 184], fill=(245, 158, 11))
    draw.ellipse([184, 172, 196, 184], fill=(16, 185, 129))
    draw.text((220, 168), "italsport-group.it/configuratore-3d • Vista 360° Live", font=get_font(18, bold=False), fill=(148, 163, 184))
    
    # Inside Viewport: Clean Soccer Jersey Graphic
    # Jersey body
    jersey_center_x = 540
    jersey_center_y = 480
    
    # Draw realistic stylized 3D sports jersey
    body_poly = [
        (430, 290), (490, 290), (520, 330), (560, 330), (590, 290), (650, 290),
        (720, 380), (670, 430), (640, 400), (640, 680), (440, 680), (440, 400),
        (410, 430), (360, 380)
    ]
    # Jersey base (Emerald green & Navy modern split)
    draw.polygon(body_poly, fill=(16, 185, 129), outline=(13, 148, 136), width=3)
    # Right half dark navy
    draw.polygon([
        (540, 330), (560, 330), (590, 290), (650, 290),
        (720, 380), (670, 430), (640, 400), (640, 680), (540, 680)
    ], fill=(15, 23, 42))
    
    # Collar
    draw.polygon([(490, 290), (520, 330), (560, 330), (590, 290), (540, 350)], fill=(245, 158, 11))
    # Vertical stripe
    draw.rectangle([532, 350, 548, 680], fill=(255, 255, 255))
    
    # Shield crest on chest
    draw.polygon([(465, 380), (505, 380), (505, 420), (485, 440), (465, 420)], fill=(239, 68, 68), outline=(255, 255, 255), width=2)
    # Sponsor text
    draw.text((455, 480), "ITALSPORT", font=get_font(28, bold=True), fill=(255, 255, 255))
    
    # 3D Orbit ring around jersey
    draw.arc([300, 610, 780, 720], start=0, end=360, fill=(56, 189, 248, 200), width=3)
    draw.ellipse([760, 660, 776, 676], fill=(56, 189, 248))
    draw.text((500, 725), "Ruota 360°", font=get_font(18, bold=True), fill=(56, 189, 248))
    
    # Floating control tools on right side of viewport
    tools_x = 800
    tools_y = 260
    draw.rounded_rectangle([tools_x, tools_y, tools_x + 130, tools_y + 360], radius=10, fill=(30, 41, 59, 220), outline=(71, 85, 105))
    draw.text((tools_x + 15, tools_y + 15), "COLORI", font=get_font(14, bold=True), fill=(148, 163, 184))
    
    # Swatches
    colors = [(16, 185, 129), (15, 23, 42), (239, 68, 68), (245, 158, 11), (59, 130, 246), (255, 255, 255)]
    for i, col in enumerate(colors):
        cy = tools_y + 50 + i * 36
        draw.ellipse([tools_x + 20, cy, tools_x + 48, cy + 28], fill=col, outline=(255, 255, 255), width=1)
        draw.text((tools_x + 60, cy + 5), f"Col. 0{i+1}", font=get_font(13), fill=(203, 213, 225))
    
    draw.rounded_rectangle([tools_x + 10, tools_y + 285, tools_x + 120, tools_y + 340], radius=6, fill=(16, 185, 129))
    draw.text((tools_x + 22, tools_y + 300), "CARICA LOGO", font=get_font(13, bold=True), fill=(255, 255, 255))
    
    # Bottom text
    f_title = get_font(50, bold=True)
    f_sub = get_font(26, bold=True)
    f_body = get_font(22, bold=False)
    
    draw.text((60, 825), "CONFIGURATORE 3D ONLINE", font=f_sub, fill=(56, 189, 248))
    draw.text((60, 865), "DISEGNA IL TUO KIT IN TEMPO REALE", font=f_title, fill=(255, 255, 255))
    draw.text((60, 935), "Scegli modello, colori sociali e loghi a 360° prima di mandare in stampa.", font=f_body, fill=(203, 213, 225))
    draw.text((60, 970), "Dalla tua creatività al fischio d'inizio della domenica.", font=f_body, fill=(148, 163, 184))
    
    im.convert('RGB').save('img_post2_3d.jpg', quality=90)
    print("Post 2 created successfully.")

# -------------------------------------------------------------
# POST 3: Tessera Fedeltà Pro-Club (Clean Luxury Physical Card)
# -------------------------------------------------------------
def make_post3():
    im = Image.new('RGBA', (1080, 1080), (11, 15, 25, 255))
    draw = ImageDraw.Draw(im)
    
    # Ambient background lighting
    glow = Image.new('RGBA', (1080, 1080), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow)
    for r in range(450, 0, -5):
        alpha = int(40 * (1 - r / 450))
        glow_draw.ellipse([540 - r, 460 - r, 540 + r, 460 + r], fill=(217, 119, 6, alpha))
    im = Image.alpha_composite(im, glow)
    draw = ImageDraw.Draw(im)
    
    # Top header badge
    draw.rounded_rectangle([60, 50, 310, 95], radius=8, fill=(217, 119, 6, 230))
    f_badge = get_font(20, bold=True)
    draw.text((78, 62), "VANTAGGI ESCLUSIVI", font=f_badge, fill=(255, 255, 255))
    
    # Logo top right
    l_w = 200
    l_h = int(logo_img.size[1] * (l_w / logo_img.size[0]))
    resized_logo = logo_img.resize((l_w, l_h), Image.Resampling.LANCZOS)
    im.paste(resized_logo, (1080 - l_w - 60, 50), resized_logo)
    
    # LUXURY FIDELITY CARD
    card_w, card_h = 760, 460
    card_x, card_y = 160, 200
    
    # Card drop shadow
    shadow = Image.new('RGBA', (1080, 1080), (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(shadow)
    s_draw.rounded_rectangle([card_x + 10, card_y + 20, card_x + card_w + 10, card_y + card_h + 20], radius=24, fill=(0, 0, 0, 180))
    shadow = shadow.filter(ImageFilter.GaussianBlur(15))
    im = Image.alpha_composite(im, shadow)
    draw = ImageDraw.Draw(im)
    
    # Card base: Obsidian navy gradient
    card_img = Image.new('RGBA', (card_w, card_h), (0, 0, 0, 0))
    c_draw = ImageDraw.Draw(card_img)
    
    # Card background gradient
    for y in range(card_h):
        r = int(15 + (30 - 15) * (y / card_h))
        g = int(23 + (41 - 23) * (y / card_h))
        b = int(42 + (59 - 42) * (y / card_h))
        c_draw.line([(0, y), (card_w, y)], fill=(r, g, b, 255))
        
    # Gold border
    c_draw.rounded_rectangle([0, 0, card_w - 1, card_h - 1], radius=24, outline=(217, 119, 6), width=3)
    # Subtle inner gold border
    c_draw.rounded_rectangle([6, 6, card_w - 7, card_h - 7], radius=20, outline=(245, 158, 11, 100), width=1)
    
    # Card Header
    c_draw.text((50, 45), "ITALSPORT GROUP", font=get_font(26, bold=True), fill=(245, 158, 11))
    c_draw.text((50, 80), "OFFICIAL PARTNER NETWORK", font=get_font(14, bold=True), fill=(148, 163, 184))
    
    # Gold EMV Chip
    chip_x, chip_y = 50, 130
    c_draw.rounded_rectangle([chip_x, chip_y, chip_x + 75, chip_y + 60], radius=8, fill=(234, 179, 8), outline=(180, 83, 9), width=2)
    c_draw.line([(chip_x + 25, chip_y), (chip_x + 25, chip_y + 60)], fill=(180, 83, 9), width=1)
    c_draw.line([(chip_x + 50, chip_y), (chip_x + 50, chip_y + 60)], fill=(180, 83, 9), width=1)
    c_draw.line([(chip_x, chip_y + 30), (chip_x + 75, chip_y + 30)], fill=(180, 83, 9), width=1)
    
    # Contactless wave symbol
    c_draw.arc([chip_x + 100, chip_y + 10, chip_x + 140, chip_y + 50], start=-45, end=45, fill=(245, 158, 11), width=2)
    c_draw.arc([chip_x + 108, chip_y + 10, chip_x + 148, chip_y + 50], start=-45, end=45, fill=(245, 158, 11), width=2)
    
    # PRO-CLUB GOLD BADGE on right
    c_draw.rounded_rectangle([card_w - 240, 40, card_w - 45, 95], radius=12, fill=(217, 119, 6), outline=(245, 158, 11), width=1)
    c_draw.text((card_w - 220, 52), "PRO-CLUB", font=get_font(26, bold=True), fill=(255, 255, 255))
    c_draw.text((card_w - 220, 78), "VIP MEMBER CARD", font=get_font(11, bold=True), fill=(254, 243, 199))
    
    # Card Number / Member Code
    c_draw.text((50, 230), "CARD NUMBER", font=get_font(12, bold=True), fill=(100, 116, 139))
    c_draw.text((50, 250), "IS-2026 • 8849 • 1092 • PRO", font=get_font(28, bold=True), fill=(255, 255, 255))
    
    # Society Name & Expiry
    c_draw.text((50, 320), "INTESTATARIO CONVENZIONE", font=get_font(12, bold=True), fill=(100, 116, 139))
    c_draw.text((50, 342), "ASD SPORTING CLUB & ACADEMY", font=get_font(22, bold=True), fill=(241, 245, 249))
    
    c_draw.text((50, 395), "VALIDITÀ STAGIONE", font=get_font(11, bold=True), fill=(100, 116, 139))
    c_draw.text((50, 412), "2026 / 2027", font=get_font(16, bold=True), fill=(245, 158, 11))
    
    c_draw.text((card_w - 280, 395), "CIRCUITO FORNITURE", font=get_font(11, bold=True), fill=(100, 116, 139))
    c_draw.text((card_w - 280, 412), "STORE.ITALSPORT-GROUP.IT", font=get_font(14, bold=True), fill=(203, 213, 225))
    
    # Paste card onto base
    im.paste(card_img, (card_x, card_y), card_img)
    draw = ImageDraw.Draw(im)
    
    # Features Pills below card
    pills = [
        ("Listini & Sconti Dedicati", (16, 185, 129)),
        ("Priorità Riassortimenti", (56, 189, 248)),
        ("Convenzioni per Famiglie", (245, 158, 11))
    ]
    px = 160
    for p_text, p_col in pills:
        draw.rounded_rectangle([px, 690, px + 235, 735], radius=8, fill=(30, 41, 59, 240), outline=p_col, width=1)
        draw.ellipse([px + 15, 707, px + 25, 717], fill=p_col)
        draw.text((px + 35, 703), p_text, font=get_font(14, bold=True), fill=(241, 245, 249))
        px += 250
        
    # Bottom text
    f_title = get_font(48, bold=True)
    f_sub = get_font(26, bold=True)
    f_body = get_font(22, bold=False)
    
    draw.text((60, 825), "TESSERA FEDELTÀ & PRO-CLUB", font=f_sub, fill=(245, 158, 11))
    draw.text((60, 865), "LA FORNITURA CHE PREMIA LA TUA SOCIETÀ", font=f_title, fill=(255, 255, 255))
    draw.text((60, 935), "Condizioni speciali, listini bloccati e vantaggi per dirigenti, atleti e famiglie.", font=f_body, fill=(203, 213, 225))
    draw.text((60, 970), "Attiva subito la convenzione Pro-Club per la tua squadra.", font=f_body, fill=(148, 163, 184))
    
    im.convert('RGB').save('img_post3_fidelity.jpg', quality=90)
    print("Post 3 created successfully.")

# -------------------------------------------------------------
# POST 4: Riassortimenti Sempre Garantiti (Real Warehouse Storage)
# -------------------------------------------------------------
def make_post4():
    base = Image.open('real_post4_warehouse.jpg').convert('RGBA')
    w, h = base.size
    min_dim = min(w, h)
    left = (w - min_dim) // 2
    top = (h - min_dim) // 2
    base = base.crop((left, top, left + min_dim, top + min_dim)).resize((1080, 1080), Image.Resampling.LANCZOS)
    
    # Create dark gradient overlay
    overlay = Image.new('RGBA', (1080, 1080), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    # Top gradient
    for y in range(250):
        alpha = int(180 * (1 - y / 250))
        draw.line([(0, y), (1080, y)], fill=(10, 15, 25, alpha))
        
    # Bottom gradient
    for y in range(480):
        alpha = int(230 * (y / 480))
        draw.line([(0, 1080 - 480 + y), (1080, 1080 - 480 + y)], fill=(9, 13, 22, alpha))
        
    composite = Image.alpha_composite(base, overlay)
    draw = ImageDraw.Draw(composite)
    
    # Top bar badge
    draw.rounded_rectangle([60, 50, 310, 95], radius=8, fill=(16, 185, 129, 230))
    f_badge = get_font(20, bold=True)
    draw.text((78, 62), "GARANZIA CONTINUITÀ", font=f_badge, fill=(255, 255, 255))
    
    # Logo top right
    l_w = 200
    l_h = int(logo_img.size[1] * (l_w / logo_img.size[0]))
    resized_logo = logo_img.resize((l_w, l_h), Image.Resampling.LANCZOS)
    composite.paste(resized_logo, (1080 - l_w - 60, 50), resized_logo)
    
    # Center floating warranty seal
    seal_x, seal_y = 60, 640
    draw.rounded_rectangle([seal_x, seal_y, seal_x + 420, seal_y + 110], radius=12, fill=(15, 23, 42, 230), outline=(16, 185, 129), width=2)
    draw.text((seal_x + 25, seal_y + 20), "ARCHIVIO STORICO ITALSPORT", font=get_font(16, bold=True), fill=(16, 185, 129))
    draw.text((seal_x + 25, seal_y + 50), "Codici pantone e modelli memorizzati per sempre", font=get_font(15), fill=(203, 213, 225))
    draw.text((seal_x + 25, seal_y + 75), "Riordini anche per 1 solo capo di nuovo iscritto", font=get_font(15, bold=True), fill=(255, 255, 255))
    
    # Bottom text
    f_title = get_font(48, bold=True)
    f_sub = get_font(26, bold=True)
    f_body = get_font(22, bold=False)
    
    draw.text((60, 785), "MAI PIÙ DIVISE FUORI PRODUZIONE", font=f_sub, fill=(52, 211, 153))
    draw.text((60, 825), "RIASSORTIMENTI SEMPRE GARANTITI", font=f_title, fill=(255, 255, 255))
    draw.text((60, 905), "I nuovi tesserati riceveranno l'esatta divisa della squadra, anche a distanza di anni.", font=f_body, fill=(203, 213, 225))
    draw.text((60, 940), "Nessun obbligo di rifare il kit societario ogni stagione.", font=f_body, fill=(148, 163, 184))
    
    composite.convert('RGB').save('img_post4_stack.jpg', quality=90)
    print("Post 4 created successfully.")

# -------------------------------------------------------------
# POST 5: Portale My Italsport (Clean Mobile Responsive Interface)
# -------------------------------------------------------------
def make_post5():
    im = Image.new('RGBA', (1080, 1080), (13, 17, 28, 255))
    draw = ImageDraw.Draw(im)
    
    # Background pattern
    for x in range(0, 1080, 60):
        draw.line([(x, 0), (x, 1080)], fill=(25, 33, 50, 120), width=1)
    for y in range(0, 1080, 60):
        draw.line([(0, y), (1080, y)], fill=(25, 33, 50, 120), width=1)
        
    glow = Image.new('RGBA', (1080, 1080), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow)
    for r in range(400, 0, -5):
        alpha = int(45 * (1 - r / 400))
        glow_draw.ellipse([540 - r, 480 - r, 540 + r, 480 + r], fill=(59, 130, 246, alpha))
    im = Image.alpha_composite(im, glow)
    draw = ImageDraw.Draw(im)
    
    # Top header badge
    draw.rounded_rectangle([60, 50, 310, 95], radius=8, fill=(59, 130, 246, 230))
    f_badge = get_font(20, bold=True)
    draw.text((78, 62), "LOGISTICA SENZA STRESS", font=f_badge, fill=(255, 255, 255))
    
    # Logo top right
    l_w = 200
    l_h = int(logo_img.size[1] * (l_w / logo_img.size[0]))
    resized_logo = logo_img.resize((l_w, l_h), Image.Resampling.LANCZOS)
    im.paste(resized_logo, (1080 - l_w - 60, 50), resized_logo)
    
    # SMARTPHONE MOCKUP IN CENTER
    phone_w, phone_h = 420, 620
    phone_x, phone_y = 330, 140
    
    # Shadow
    shadow = Image.new('RGBA', (1080, 1080), (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(shadow)
    s_draw.rounded_rectangle([phone_x + 10, phone_y + 15, phone_x + phone_w + 10, phone_y + phone_h + 15], radius=32, fill=(0, 0, 0, 180))
    shadow = shadow.filter(ImageFilter.GaussianBlur(14))
    im = Image.alpha_composite(im, shadow)
    draw = ImageDraw.Draw(im)
    
    # Phone Chassis
    draw.rounded_rectangle([phone_x, phone_y, phone_x + phone_w, phone_y + phone_h], radius=32, fill=(15, 23, 42), outline=(100, 116, 139), width=3)
    
    # Screen area
    sx, sy, sw, sh = phone_x + 10, phone_y + 10, phone_w - 20, phone_h - 20
    draw.rounded_rectangle([sx, sy, sx + sw, sy + sh], radius=24, fill=(248, 250, 252))
    
    # Dynamic Island / Notch
    draw.rounded_rectangle([phone_x + 150, phone_y + 16, phone_x + 270, phone_y + 36], radius=10, fill=(15, 23, 42))
    
    # Screen Content: Clean Web Store
    # Header bar
    draw.rectangle([sx, sy + 35, sx + sw, sy + 85], fill=(15, 23, 42))
    draw.text((sx + 20, sy + 48), "MY ITALSPORT", font=get_font(18, bold=True), fill=(255, 255, 255))
    draw.text((sx + sw - 80, sy + 50), "ACCEDI", font=get_font(14, bold=True), fill=(56, 189, 248))
    
    # Club Welcome Banner
    draw.rectangle([sx, sy + 85, sx + sw, sy + 155], fill=(224, 242, 254))
    draw.text((sx + 20, sy + 95), "AREA RISERVATA SOCIETÀ", font=get_font(11, bold=True), fill=(3, 105, 161))
    draw.text((sx + 20, sy + 115), "ASD Polisportiva Virtus", font=get_font(18, bold=True), fill=(15, 23, 42))
    
    # Item 1: Kit Gara
    iy1 = sy + 170
    draw.rounded_rectangle([sx + 15, iy1, sx + sw - 15, iy1 + 95], radius=10, fill=(255, 255, 255), outline=(226, 232, 240), width=1)
    # Thumbnail
    draw.rectangle([sx + 25, iy1 + 10, sx + 95, iy1 + 85], fill=(16, 185, 129))
    draw.text((sx + 45, iy1 + 40), "KIT", font=get_font(16, bold=True), fill=(255, 255, 255))
    draw.text((sx + 110, iy1 + 15), "Kit Ufficiale Gara 26/27", font=get_font(15, bold=True), fill=(15, 23, 42))
    draw.text((sx + 110, iy1 + 38), "Maglia + Calzoncini + Calzettoni", font=get_font(12), fill=(100, 116, 139))
    draw.text((sx + 110, iy1 + 62), "Taglie: XS • S • M • L • XL", font=get_font(12, bold=True), fill=(16, 185, 129))
    
    # Item 2: Tuta Allenamento
    iy2 = sy + 275
    draw.rounded_rectangle([sx + 15, iy2, sx + sw - 15, iy2 + 95], radius=10, fill=(255, 255, 255), outline=(226, 232, 240), width=1)
    draw.rectangle([sx + 25, iy2 + 10, sx + 95, iy2 + 85], fill=(15, 23, 42))
    draw.text((sx + 35, iy2 + 40), "TUTA", font=get_font(15, bold=True), fill=(255, 255, 255))
    draw.text((sx + 110, iy2 + 15), "Tuta Training Invernale", font=get_font(15, bold=True), fill=(15, 23, 42))
    draw.text((sx + 110, iy2 + 38), "Giacca termica + Pantalone zip", font=get_font(12), fill=(100, 116, 139))
    draw.text((sx + 110, iy2 + 62), "Personalizzata con stemma club", font=get_font(12, bold=True), fill=(59, 130, 246))
    
    # Action Button
    by = sy + 390
    draw.rounded_rectangle([sx + 20, by, sx + sw - 20, by + 50], radius=10, fill=(16, 185, 129))
    draw.text((sx + 75, by + 14), "ORDINA IL KIT ONLINE", font=get_font(16, bold=True), fill=(255, 255, 255))
    
    # Subtext on screen
    draw.text((sx + 30, by + 65), "Spedizione diretta o ritiro al club convenzionato", font=get_font(11), fill=(100, 116, 139))
    
    # Feature Callouts on Left and Right of Phone
    # Left callout
    draw.rounded_rectangle([60, 260, 280, 360], radius=10, fill=(15, 23, 42, 230), outline=(56, 189, 248), width=1)
    draw.text((80, 275), "ZERO BUROCRAZIA", font=get_font(14, bold=True), fill=(56, 189, 248))
    draw.text((80, 300), "Le famiglie ordinano online", font=get_font(13), fill=(241, 245, 249))
    draw.text((80, 322), "Niente più raccolte taglie a mano", font=get_font(13), fill=(148, 163, 184))
    
    # Right callout
    draw.rounded_rectangle([800, 260, 1020, 360], radius=10, fill=(15, 23, 42, 230), outline=(16, 185, 129), width=1)
    draw.text((820, 275), "DASHBOARD CLUB", font=get_font(14, bold=True), fill=(16, 185, 129))
    draw.text((820, 300), "Monitora lo stato ordini", font=get_font(13), fill=(241, 245, 249))
    draw.text((820, 322), "Fatturazione chiara e tracciata", font=get_font(13), fill=(148, 163, 184))
    
    # Bottom text
    f_title = get_font(50, bold=True)
    f_sub = get_font(26, bold=True)
    f_body = get_font(22, bold=False)
    
    draw.text((60, 825), "PORTALE MY ITALSPORT", font=f_sub, fill=(56, 189, 248))
    draw.text((60, 865), "L'AREA E-COMMERCE DEDICATA AL TUO CLUB", font=f_title, fill=(255, 255, 255))
    draw.text((60, 935), "Ogni società ha la propria pagina riservata: atleti e genitori acquistano in un click.", font=f_body, fill=(203, 213, 225))
    draw.text((60, 970), "La soluzione intelligente che azzera la burocrazia per i dirigenti.", font=f_body, fill=(148, 163, 184))
    
    im.convert('RGB').save('img_post5_portal.jpg', quality=90)
    print("Post 5 created successfully.")

# -------------------------------------------------------------
# POST 6: Winter Training (Real Winter Pitch Photography)
# -------------------------------------------------------------
def make_post6():
    base = Image.open('real_post6_winter.jpg').convert('RGBA')
    w, h = base.size
    min_dim = min(w, h)
    left = (w - min_dim) // 2
    top = (h - min_dim) // 2
    base = base.crop((left, top, left + min_dim, top + min_dim)).resize((1080, 1080), Image.Resampling.LANCZOS)
    
    overlay = Image.new('RGBA', (1080, 1080), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    # Top gradient
    for y in range(250):
        alpha = int(180 * (1 - y / 250))
        draw.line([(0, y), (1080, y)], fill=(10, 15, 25, alpha))
        
    # Bottom gradient
    for y in range(460):
        alpha = int(225 * (y / 460))
        draw.line([(0, 1080 - 460 + y), (1080, 1080 - 460 + y)], fill=(9, 13, 22, alpha))
        
    composite = Image.alpha_composite(base, overlay)
    draw = ImageDraw.Draw(composite)
    
    # Top bar badge
    draw.rounded_rectangle([60, 50, 310, 95], radius=8, fill=(14, 165, 233, 230))
    f_badge = get_font(20, bold=True)
    draw.text((78, 62), "FORNITURA INVERNALE", font=f_badge, fill=(255, 255, 255))
    
    # Logo top right
    l_w = 200
    l_h = int(logo_img.size[1] * (l_w / logo_img.size[0]))
    resized_logo = logo_img.resize((l_w, l_h), Image.Resampling.LANCZOS)
    composite.paste(resized_logo, (1080 - l_w - 60, 50), resized_logo)
    
    # Items Pills
    pills = ["Giacconi Termici", "K-way Antivento", "Pantaloni Tecnici Zip", "Scaldacollo Club"]
    px = 60
    for p in pills:
        draw.rounded_rectangle([px, 730, px + 215, 775], radius=8, fill=(15, 23, 42, 230), outline=(56, 189, 248), width=1)
        draw.text((px + 20, 743), p, font=get_font(15, bold=True), fill=(241, 245, 249))
        px += 235
        
    # Bottom text
    f_title = get_font(48, bold=True)
    f_sub = get_font(26, bold=True)
    f_body = get_font(22, bold=False)
    
    draw.text((60, 815), "STAGIONE FREDDA 2026/27", font=f_sub, fill=(56, 189, 248))
    draw.text((60, 855), "WINTER TRAINING: NON FERMARTI MAI", font=f_title, fill=(255, 255, 255))
    draw.text((60, 930), "Capi tecnici imbottiti, resistenti all'acqua e traspiranti per affrontare l'inverno in campo.", font=f_body, fill=(203, 213, 225))
    draw.text((60, 965), "Personalizzazione completa con colori sociali e stemma societario.", font=f_body, fill=(148, 163, 184))
    
    composite.convert('RGB').save('img_post6_winter.jpg', quality=90)
    print("Post 6 created successfully.")

# -------------------------------------------------------------
# POST 7: Community & Auguri Fine Anno (Real Team Celebration)
# -------------------------------------------------------------
def make_post7():
    base = Image.open('real_post7_celebrate.jpg').convert('RGBA')
    w, h = base.size
    min_dim = min(w, h)
    left = (w - min_dim) // 2
    top = (h - min_dim) // 2
    base = base.crop((left, top, left + min_dim, top + min_dim)).resize((1080, 1080), Image.Resampling.LANCZOS)
    
    overlay = Image.new('RGBA', (1080, 1080), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    # Top gradient
    for y in range(250):
        alpha = int(180 * (1 - y / 250))
        draw.line([(0, y), (1080, y)], fill=(10, 15, 25, alpha))
        
    # Bottom gradient
    for y in range(480):
        alpha = int(230 * (y / 480))
        draw.line([(0, 1080 - 480 + y), (1080, 1080 - 480 + y)], fill=(9, 13, 22, alpha))
        
    composite = Image.alpha_composite(base, overlay)
    draw = ImageDraw.Draw(composite)
    
    # Top bar badge
    draw.rounded_rectangle([60, 50, 310, 95], radius=8, fill=(239, 68, 68, 230))
    f_badge = get_font(20, bold=True)
    draw.text((78, 62), "COMMUNITY SPORTIVA", font=f_badge, fill=(255, 255, 255))
    
    # Logo top right
    l_w = 200
    l_h = int(logo_img.size[1] * (l_w / logo_img.size[0]))
    resized_logo = logo_img.resize((l_w, l_h), Image.Resampling.LANCZOS)
    composite.paste(resized_logo, (1080 - l_w - 60, 50), resized_logo)
    
    # Bottom text
    f_title = get_font(48, bold=True)
    f_sub = get_font(26, bold=True)
    f_body = get_font(22, bold=False)
    
    draw.text((60, 785), "INSIEME SUI CAMPI DI GIOCO", font=f_sub, fill=(252, 165, 165))
    draw.text((60, 825), "GRAZIE A CHI FA VIVERE LO SPORT", font=f_title, fill=(255, 255, 255))
    draw.text((60, 905), "A presidenti, dirigenti, allenatori, famiglie e atleti: grazie per la passione.", font=f_body, fill=(203, 213, 225))
    draw.text((60, 940), "Buone Feste e un grande 2027 ricco di vittorie da Italsport Group!", font=f_body, fill=(148, 163, 184))
    
    composite.convert('RGB').save('img_post7_celebration.jpg', quality=90)
    print("Post 7 created successfully.")

if __name__ == '__main__':
    make_post1()
    make_post2()
    make_post3()
    make_post4()
    make_post5()
    make_post6()
    make_post7()
    print("All 7 realistic posts generated successfully!")
