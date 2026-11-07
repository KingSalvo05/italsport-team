import os
from PIL import Image, ImageEnhance, ImageFilter

D_IG = r"C:\Users\salvo\.gemini\antigravity\brain\dc9abd1d-f990-4c44-a20b-bd6ec7f9af7d\scratch\ig_real"
D_WP2 = r"C:\Users\salvo\.gemini\antigravity\brain\dc9abd1d-f990-4c44-a20b-bd6ec7f9af7d\scratch\wp_dl2"

def enh(im):
    im = ImageEnhance.Contrast(im).enhance(1.06)
    im = ImageEnhance.Color(im).enhance(1.05)
    return im

# 1. Tessera Pro-Club ufficiale da slider_5.jpg
sl5 = Image.open(os.path.join(D_WP2, "slider_5.jpg")).convert("RGB")
card_real = enh(sl5.crop((3345, 830, 4445, 1345)).resize((660, 326), Image.Resampling.LANCZOS))
card_real.save("card_proclub_real.jpg", quality=92)

# 2. Foto reali prodotti per la Vetrina Squadra con Password
# Kit Gara (da sbi_17885178626300926.jpg e ig_post_17.jpg e sbi_17909215715015535.jpg)
j_blue = Image.open(os.path.join(D_IG, "ig_post_17.jpg")).convert("RGB")
j_blue = enh(j_blue.crop((0, 0, j_blue.width, int(j_blue.height * 0.85))).resize((480, 480), Image.Resampling.LANCZOS))
j_blue.save("prod_kit_blue.jpg", quality=90)

j_red = Image.open(os.path.join(D_IG, "sbi_17885178626300926.jpg")).convert("RGB")
j_red = enh(j_red.resize((480, 480), Image.Resampling.LANCZOS))
j_red.save("prod_kit_red.jpg", quality=90)

j_gold = Image.open(os.path.join(D_IG, "sbi_17909215715015535.jpg")).convert("RGB")
j_gold = enh(j_gold.resize((480, 480), Image.Resampling.LANCZOS))
j_gold.save("prod_kit_gold.jpg", quality=90)

# Griglia collezione club da ig_post_12.jpg (1080x1350)
g12 = Image.open(os.path.join(D_IG, "ig_post_12.jpg")).convert("RGB")
W, H = g12.size
# Riquadri nella griglia di ig_post_12.jpg:
# Riga 1 (y: 0.32..0.60): Borsa Bauletto (x: 0.04..0.28), Giubbotto Nepal (x: 0.29..0.52), Rain K-Way (x: 0.53..0.75), T-Shirt Classic (x: 0.76..0.97)
# Riga 2/3: Scotland Giacca (x: 0.04..0.33, y: 0.61..0.82), Polo Rom (x: 0.34..0.66, y: 0.82..0.97), Tuta Rom (x: 0.67..0.96, y: 0.61..0.97)
crops = {
    "prod_borsa.jpg": (int(W*0.04), int(H*0.32), int(W*0.28), int(H*0.595)),
    "prod_nepal.jpg": (int(W*0.29), int(H*0.32), int(W*0.52), int(H*0.595)),
    "prod_kway.jpg": (int(W*0.525), int(H*0.32), int(W*0.755), int(H*0.595)),
    "prod_tshirt.jpg": (int(W*0.76), int(H*0.32), int(W*0.97), int(H*0.595)),
    "prod_scotland.jpg": (int(W*0.04), int(H*0.605), int(W*0.34), int(H*0.815)),
    "prod_tuta.jpg": (int(W*0.675), int(H*0.605), int(W*0.965), int(H*0.975)),
}
for fn, box in crops.items():
    c = enh(g12.crop(box))
    c.save(fn, quality=90)

# Felpa tecnica e Showroom Ciserano per Storie/Reel
shw = Image.open(os.path.join(D_IG, "sbi_18095471020372884.jpg")).convert("RGB")
enh(shw.resize((720, 720), Image.Resampling.LANCZOS)).save("real_showroom_ciserano.jpg", quality=88)

man = Image.open(os.path.join(D_IG, "sbi_18221788846012402.jpg")).convert("RGB")
enh(man.resize((720, 900), Image.Resampling.LANCZOS)).save("real_manichini_ciserano.jpg", quality=88)

print("Extracted all real Vetrina & Pro-Club assets successfully.")
