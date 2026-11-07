import urllib.request, os
from PIL import Image

site_images = {
    'site_configuratore.jpg': 'https://italsport-group.it/wp-content/uploads/2025/01/CONFIGURATORE-Collage-Chi-siamo-1024x767.jpg',
    'site_membro_myitalsport.jpg': 'https://italsport-group.it/wp-content/uploads/2026/04/10.-Membro-My-Italsport_slide-1024x768.jpg',
    'site_vetrina_servizi.jpg': 'https://italsport-group.it/wp-content/uploads/2025/01/Foto-vetrina-servizi.jpg',
    'site_sublimazione.jpg': 'https://italsport-group.it/wp-content/uploads/2024/12/sublimazione-e1736937052421.jpg',
    'site_creativita_design.jpg': 'https://italsport-group.it/wp-content/uploads/2024/12/creativitaedesign_italsport-840x471.jpeg',
    'site_nuova_linea.jpg': 'https://italsport-group.it/wp-content/uploads/2025/01/NUOVA-LINEA-Collage-Chi-siamo-1024x767.jpg',
    'site_grafica.jpg': 'https://italsport-group.it/wp-content/uploads/2025/01/GRAFICA-Collage-Chi-siamo-1024x767.jpg',
    'site_settori.jpg': 'https://italsport-group.it/wp-content/uploads/2026/01/SETTORI-Collage-Chi-siamo-1024x768.jpg',
    'site_homepage.png': 'https://italsport-group.it/wp-content/uploads/2024/12/Italsport_homepage.png',
    'store_reparto_grafico.jpg': 'https://store.italsport-group.it/img/ets_blog/post/reparto-grafico-interno-nuovo-840x620.jpg',
    'store_full_print.jpg': 'https://store.italsport-group.it/img/ets_blog/post/stampa-full-print.jpg',
    'store_dtf.jpg': 'https://store.italsport-group.it/img/ets_blog/post/impresion-dtf-valencia-graficas-papallona.jpg',
    'store_partner_affidabile.jpg': 'https://store.italsport-group.it/modules/ps_imageslider/images/6da9da477535a1c6398b2cf26308cf350a3685e1_8.%20Partner%20Affidabile_Slide.jpg',
    'store_la_tua_linea.jpg': 'https://store.italsport-group.it/modules/ps_imageslider/images/945517538de5826ed2328870e9b69aa2093b1395_12.La%20tua%20linea_Slide.jpg'
}

for name, url in site_images.items():
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = resp.read()
            with open(name, 'wb') as f:
                f.write(data)
            im = Image.open(name)
            print(f"Downloaded {name:28}: {im.size} ({len(data)} bytes)")
    except Exception as e:
        print(f"Error {name}:", e)
