import os, sys, subprocess, base64, io, shutil
from PIL import Image

print("Starting Client Social Kit Generation...")

# 1. Ottimizza e carica immagini in base64
def get_b64(img_path):
    im = Image.open(img_path)
    im.thumbnail((800, 800), Image.Resampling.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, format='JPEG', quality=88)
    return base64.b64encode(buf.getvalue()).decode('utf-8')

b64_logo = base64.b64encode(open('cropped-cropped-italsportlogo.png', 'rb').read()).decode('utf-8')
b64_post1 = get_b64('img_post1_jersey.jpg')
b64_post2 = get_b64('img_post2_3d.jpg')
b64_post3 = get_b64('img_post3_fidelity.jpg')
b64_post4 = get_b64('img_post4_stack.jpg')
b64_post5 = get_b64('img_post5_portal.jpg')
b64_post6 = get_b64('img_post6_winter.jpg')
b64_post7 = get_b64('img_post7_celebration.jpg')

print("All images encoded successfully.")

# ========================================================
# 2. GENERAZIONE DEL NUOVO MOCKUP HTML CON FOTO REALISTICHE
# ========================================================
html_mockup = f'''<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bozza Instagram Ufficiale - ITALSPORT GROUP</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap');
    body {{
      font-family: 'Plus Jakarta Sans', sans-serif;
    }}
    .custom-scrollbar::-webkit-scrollbar {{
      width: 5px;
      height: 5px;
    }}
    .custom-scrollbar::-webkit-scrollbar-track {{
      background: rgba(0,0,0,0.05);
    }}
    .custom-scrollbar::-webkit-scrollbar-thumb {{
      background: rgba(0,0,0,0.2);
      border-radius: 999px;
    }}
    .post-cover {{
      position: relative;
      background-size: cover;
      background-position: center;
      overflow: hidden;
    }}
    .post-overlay {{
      background: linear-gradient(180deg, rgba(0,0,0,0.2) 0%, rgba(0,0,0,0.1) 40%, rgba(0,0,0,0.92) 100%);
    }}

    /* ANIMAZIONE 3D REEL SIMULATOR */
    @keyframes spin3D {{
      0% {{ transform: rotateY(0deg); }}
      50% {{ transform: rotateY(180deg); }}
      100% {{ transform: rotateY(360deg); }}
    }}
    .jersey-3d-container {{
      perspective: 1000px;
    }}
    .jersey-3d-model {{
      transform-style: preserve-3d;
      animation: spin3D 8s infinite linear;
      transition: filter 0.3s;
    }}
    .jersey-3d-model.paused {{
      animation-play-state: paused;
    }}
    @keyframes vinylSpin {{
      from {{ transform: rotate(0deg); }}
      to {{ transform: rotate(360deg); }}
    }}
    .vinyl-disc {{
      animation: vinylSpin 3s linear infinite;
    }}
  </style>
</head>
<body class="bg-slate-900 text-slate-100 min-h-screen py-8 px-4 flex flex-col items-center justify-start antialiased">

  <!-- Barra Superiore di Controllo -->
  <div class="w-full max-w-4xl mb-6 flex flex-wrap items-center justify-between gap-4 bg-slate-800/80 backdrop-blur border border-slate-700/80 rounded-2xl p-4 shadow-xl">
    <div class="flex items-center gap-3">
      <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-emerald-500 via-emerald-400 to-amber-500 flex items-center justify-center text-white font-bold shadow-md">
        IS
      </div>
      <div>
        <h1 class="text-base font-bold text-white flex items-center gap-2">
          ITALSPORT GROUP — Bozza Ufficiale Feed Instagram <span class="text-xs font-semibold px-2 py-0.5 rounded-full bg-emerald-500/20 text-emerald-400 border border-emerald-500/30">Anteprima Client B2B</span>
        </h1>
        <p class="text-xs text-slate-400">Mockup interattivo del profilo con fotografia reale, caroselli B2B e simulatore Reel 3D</p>
      </div>
    </div>
    
    <div class="flex items-center gap-2 text-xs">
      <button onclick="openReelSimulator()" class="px-3.5 py-1.5 rounded-lg bg-sky-600 text-white font-medium shadow-sm transition hover:bg-sky-500 flex items-center gap-1.5">
        <i class="fa-solid fa-play"></i> Prova Simulatore Reel 3D
      </button>
      <button onclick="toggleView('mobile')" id="btn-mobile" class="px-3.5 py-1.5 rounded-lg bg-emerald-600 text-white font-medium shadow-sm transition hover:bg-emerald-500 flex items-center gap-1.5">
        <i class="fa-solid fa-mobile-screen"></i> Smartphone
      </button>
      <button onclick="toggleView('desktop')" id="btn-desktop" class="px-3.5 py-1.5 rounded-lg bg-slate-700 text-slate-300 font-medium transition hover:bg-slate-600 flex items-center gap-1.5">
        <i class="fa-solid fa-table-cells"></i> Griglia Feed
      </button>
    </div>
  </div>

  <!-- CONTAINER PRINCIPALE SMARTPHONE -->
  <div id="preview-container" class="w-full flex justify-center transition-all duration-300">
    
    <!-- FRAME SMARTPHONE -->
    <div id="phone-wrapper" class="w-[410px] bg-black rounded-[48px] p-3 shadow-2xl border-4 border-slate-700 shadow-emerald-950/30 transition-all duration-300 relative">
      <!-- Dynamic Island -->
      <div class="absolute top-6 left-1/2 -translate-x-1/2 w-28 h-5 bg-black rounded-full z-30 flex items-center justify-center">
        <div class="w-3 h-3 rounded-full bg-slate-900 border border-slate-800 mr-2"></div>
        <div class="w-2 h-2 rounded-full bg-slate-800"></div>
      </div>

      <!-- Schermo Telefono -->
      <div class="w-full bg-slate-950 text-slate-50 rounded-[38px] overflow-hidden border border-slate-800 flex flex-col h-[820px]">
        
        <!-- Status Bar -->
        <div class="pt-3 px-6 pb-2 flex justify-between items-center text-[12px] font-semibold text-slate-300 select-none">
          <span>09:41</span>
          <div class="flex items-center gap-1.5">
            <i class="fa-solid fa-signal text-[10px]"></i>
            <i class="fa-solid fa-wifi text-[10px]"></i>
            <i class="fa-solid fa-battery-full text-[12px]"></i>
          </div>
        </div>

        <!-- Instagram Top Bar -->
        <div class="px-4 py-2 border-b border-slate-800/80 flex items-center justify-between">
          <div class="flex items-center gap-1.5">
            <span class="font-bold text-base tracking-tight text-white">italsportgroup</span>
            <i class="fa-solid fa-circle-check text-emerald-400 text-xs" title="Profilo Ufficiale"></i>
          </div>
          <div class="flex items-center gap-4 text-slate-300 text-base">
            <i class="fa-regular fa-bell hover:text-white cursor-pointer transition"></i>
            <i class="fa-solid fa-ellipsis hover:text-white cursor-pointer transition"></i>
          </div>
        </div>

        <!-- Scrollable Profile Area -->
        <div class="overflow-y-auto flex-1 custom-scrollbar">
          
          <!-- Profile Info Header -->
          <div class="p-4">
            <div class="flex items-center justify-between gap-4">
              <!-- Avatar con cerchio Story verde smeraldo / oro -->
              <div class="relative cursor-pointer group" onclick="openHighlight(0)">
                <div class="w-[78px] h-[78px] rounded-full p-[2.5px] bg-gradient-to-tr from-emerald-500 via-sky-400 to-amber-400 group-hover:scale-105 transition duration-200">
                  <div class="w-full h-full bg-slate-900 rounded-full p-1.5 flex items-center justify-center border border-slate-800">
                    <img src="data:image/png;base64,{b64_logo}" alt="Italsport Logo" class="max-w-full max-h-full object-contain">
                  </div>
                </div>
                <div class="absolute bottom-0 right-0 w-5 h-5 bg-emerald-500 border-2 border-slate-950 rounded-full flex items-center justify-center text-[10px] text-white font-bold">
                  ✓
                </div>
              </div>

              <!-- Stats Numeriche -->
              <div class="flex-1 flex justify-around text-center">
                <div>
                  <div class="font-bold text-base text-white">7</div>
                  <div class="text-[11px] text-slate-400">Post</div>
                </div>
                <div>
                  <div class="font-bold text-base text-white">1.280</div>
                  <div class="text-[11px] text-slate-400">Follower</div>
                </div>
                <div>
                  <div class="font-bold text-base text-white">340</div>
                  <div class="text-[11px] text-slate-400">Seguiti</div>
                </div>
              </div>
            </div>

            <!-- Bio Ufficiale -->
            <div class="mt-3">
              <h2 class="font-bold text-xs text-white flex items-center gap-1">
                ITALSPORT GROUP | Custom Teamwear 🇮🇹
              </h2>
              <p class="text-[11px] text-emerald-400 font-medium">Abbigliamento e articoli sportivi</p>
              
              <div class="mt-1.5 text-[11px] leading-relaxed text-slate-200 space-y-0.5">
                <p>Da oltre 30 anni al servizio dello sport, aziende e scuole</p>
                <p>Crea il kit del tuo club col <span class="font-semibold text-emerald-400">CONFIGURATORE 3D</span></p>
                <p>Tessera Fedeltà & Programma <span class="font-semibold text-amber-300">PRO-CLUB</span> per società</p>
                <p>Portale MY ITALSPORT: <em>"Tu scegli, al resto pensiamo noi"</em></p>
                <p>Richiedi una convenzione o prova il configuratore 👇</p>
              </div>

              <!-- Link In Bio -->
              <a href="https://italsport-group.it" target="_blank" class="mt-1 inline-flex items-center gap-1 text-[11px] font-semibold text-sky-400 hover:text-sky-300 transition">
                <i class="fa-solid fa-link text-[10px]"></i> italsport-group.it
              </a>
            </div>

            <!-- Bottoni d'Azione -->
            <div class="mt-3 grid grid-cols-4 gap-1.5">
              <button class="col-span-2 py-1.5 rounded-lg bg-emerald-600 text-white font-semibold text-[11px] hover:bg-emerald-500 transition shadow-sm">
                Segui
              </button>
              <button class="py-1.5 rounded-lg bg-slate-800 text-slate-200 font-semibold text-[11px] hover:bg-slate-700 transition border border-slate-700/60">
                Messaggio
              </button>
              <button class="py-1.5 rounded-lg bg-slate-800 text-slate-200 font-semibold text-[11px] hover:bg-slate-700 transition border border-slate-700/60" title="Convenzioni">
                Convenzioni
              </button>
            </div>

            <!-- Storie In Evidenza (Highlights) -->
            <div class="mt-4 pt-3 border-t border-slate-800/80">
              <div class="flex items-center gap-3 overflow-x-auto pb-2 custom-scrollbar">
                
                <!-- HL 1: 3D Config -->
                <div class="flex flex-col items-center flex-shrink-0 cursor-pointer group" onclick="openHighlight(0)">
                  <div class="w-14 h-14 rounded-full p-[2px] bg-slate-800 border border-slate-700 group-hover:border-emerald-400 transition">
                    <div class="w-full h-full rounded-full bg-slate-900 flex items-center justify-center text-emerald-400 text-lg">
                      <i class="fa-solid fa-cube"></i>
                    </div>
                  </div>
                  <span class="text-[10px] text-slate-300 mt-1 font-medium group-hover:text-white">3D Config</span>
                </div>

                <!-- HL 2: Tessera Club -->
                <div class="flex flex-col items-center flex-shrink-0 cursor-pointer group" onclick="openHighlight(1)">
                  <div class="w-14 h-14 rounded-full p-[2px] bg-slate-800 border border-slate-700 group-hover:border-amber-400 transition">
                    <div class="w-full h-full rounded-full bg-slate-900 flex items-center justify-center text-amber-400 text-lg">
                      <i class="fa-solid fa-id-card"></i>
                    </div>
                  </div>
                  <span class="text-[10px] text-slate-300 mt-1 font-medium group-hover:text-white">Tessera Club</span>
                </div>

                <!-- HL 3: Kit & Divise -->
                <div class="flex flex-col items-center flex-shrink-0 cursor-pointer group" onclick="openHighlight(2)">
                  <div class="w-14 h-14 rounded-full p-[2px] bg-slate-800 border border-slate-700 group-hover:border-sky-400 transition">
                    <div class="w-full h-full rounded-full bg-slate-900 flex items-center justify-center text-sky-400 text-lg">
                      <i class="fa-solid fa-shirt"></i>
                    </div>
                  </div>
                  <span class="text-[10px] text-slate-300 mt-1 font-medium group-hover:text-white">Kit & Divise</span>
                </div>

                <!-- HL 4: Riassortimenti -->
                <div class="flex flex-col items-center flex-shrink-0 cursor-pointer group" onclick="openHighlight(3)">
                  <div class="w-14 h-14 rounded-full p-[2px] bg-slate-800 border border-slate-700 group-hover:border-indigo-400 transition">
                    <div class="w-full h-full rounded-full bg-slate-900 flex items-center justify-center text-indigo-400 text-lg">
                      <i class="fa-solid fa-rotate"></i>
                    </div>
                  </div>
                  <span class="text-[10px] text-slate-300 mt-1 font-medium group-hover:text-white">Riassortimenti</span>
                </div>

                <!-- HL 5: Produzione -->
                <div class="flex flex-col items-center flex-shrink-0 cursor-pointer group" onclick="openHighlight(4)">
                  <div class="w-14 h-14 rounded-full p-[2px] bg-slate-800 border border-slate-700 group-hover:border-rose-400 transition">
                    <div class="w-full h-full rounded-full bg-slate-900 flex items-center justify-center text-rose-400 text-lg">
                      <i class="fa-solid fa-industry"></i>
                    </div>
                  </div>
                  <span class="text-[10px] text-slate-300 mt-1 font-medium group-hover:text-white">Produzione</span>
                </div>

                <!-- HL 6: My Italsport -->
                <div class="flex flex-col items-center flex-shrink-0 cursor-pointer group" onclick="openHighlight(5)">
                  <div class="w-14 h-14 rounded-full p-[2px] bg-slate-800 border border-slate-700 group-hover:border-emerald-400 transition">
                    <div class="w-full h-full rounded-full bg-slate-900 flex items-center justify-center text-emerald-400 text-lg">
                      <i class="fa-solid fa-boxes-packing"></i>
                    </div>
                  </div>
                  <span class="text-[10px] text-slate-300 mt-1 font-medium group-hover:text-white">My Italsport</span>
                </div>

              </div>
            </div>

          </div>

          <!-- TAB BAR POST / REELS / TAG -->
          <div class="flex border-t border-slate-800 text-slate-400 text-xs">
            <button class="flex-1 py-2.5 border-b-2 border-white text-white flex justify-center items-center gap-1.5 font-semibold">
              <i class="fa-solid fa-table-cells text-sm"></i>
              <span>POST</span>
            </button>
            <button onclick="openReelSimulator()" class="flex-1 py-2.5 border-b-2 border-transparent hover:text-white flex justify-center items-center gap-1.5 transition">
              <i class="fa-solid fa-clapperboard text-sm text-sky-400"></i>
              <span class="text-sky-400 font-semibold">REEL 3D</span>
            </button>
            <button class="flex-1 py-2.5 border-b-2 border-transparent hover:text-white flex justify-center items-center gap-1.5 transition">
              <i class="fa-regular fa-id-badge text-sm"></i>
            </button>
          </div>

          <!-- GRIGLIA POST FOTOGRAFICI (3x2) -->
          <div class="grid grid-cols-3 gap-1 p-1 bg-slate-950" id="posts-grid">
            
            <!-- POST 1: Foto Maglia Custom in Spogliatoio -->
            <div class="aspect-square relative cursor-pointer group rounded-sm overflow-hidden post-cover" style="background-image: url('data:image/jpeg;base64,{b64_post1}');" onclick="openPostModal(0)">
              <div class="absolute inset-0 post-overlay flex flex-col justify-between p-2">
                <div class="flex justify-between items-start">
                  <span class="bg-emerald-600/90 text-white text-[8px] font-bold px-1.5 py-0.5 rounded backdrop-blur">30 ANNI</span>
                  <i class="fa-solid fa-clone text-white text-[11px] drop-shadow"></i>
                </div>
                <div>
                  <div class="text-[9px] font-bold text-white uppercase leading-tight line-clamp-2">La Passione che Diventa Divisa</div>
                  <div class="text-[8px] text-emerald-400 font-medium">31 Ottobre</div>
                </div>
              </div>
            </div>

            <!-- POST 2: Video Reel Configuratore 3D (Badge Play) -->
            <div class="aspect-square relative cursor-pointer group rounded-sm overflow-hidden post-cover border-2 border-sky-500/60 shadow-lg" style="background-image: url('data:image/jpeg;base64,{b64_post2}');" onclick="openReelSimulator()">
              <div class="absolute inset-0 post-overlay flex flex-col justify-between p-2">
                <div class="flex justify-between items-start">
                  <span class="bg-sky-600 text-white text-[8px] font-bold px-1.5 py-0.5 rounded backdrop-blur flex items-center gap-1">
                    <i class="fa-solid fa-play text-[7px]"></i> REEL
                  </span>
                  <span class="text-[9px] bg-slate-900/80 px-1 py-0.5 rounded text-sky-300 font-semibold">360°</span>
                </div>
                <div>
                  <div class="text-[9px] font-bold text-white uppercase leading-tight line-clamp-2">Disegna il tuo Kit in 3D</div>
                  <div class="text-[8px] text-sky-400 font-medium">08 Novembre</div>
                </div>
              </div>
            </div>

            <!-- POST 3: Tessera Fedeltà & Pro-Club -->
            <div class="aspect-square relative cursor-pointer group rounded-sm overflow-hidden post-cover" style="background-image: url('data:image/jpeg;base64,{b64_post3}');" onclick="openPostModal(2)">
              <div class="absolute inset-0 post-overlay flex flex-col justify-between p-2">
                <div class="flex justify-between items-start">
                  <span class="bg-amber-600/90 text-white text-[8px] font-bold px-1.5 py-0.5 rounded backdrop-blur">PRO-CLUB</span>
                  <i class="fa-solid fa-star text-amber-400 text-[11px]"></i>
                </div>
                <div>
                  <div class="text-[9px] font-bold text-white uppercase leading-tight line-clamp-2">Tessera Fedeltà & Sconti</div>
                  <div class="text-[8px] text-amber-300 font-medium">18 Novembre</div>
                </div>
              </div>
            </div>

            <!-- POST 4: Riassortimenti Sempre Garantiti -->
            <div class="aspect-square relative cursor-pointer group rounded-sm overflow-hidden post-cover" style="background-image: url('data:image/jpeg;base64,{b64_post4}');" onclick="openPostModal(3)">
              <div class="absolute inset-0 post-overlay flex flex-col justify-between p-2">
                <div class="flex justify-between items-start">
                  <span class="bg-indigo-600/90 text-white text-[8px] font-bold px-1.5 py-0.5 rounded backdrop-blur">CONTINUITÀ</span>
                  <i class="fa-solid fa-clone text-white text-[11px] drop-shadow"></i>
                </div>
                <div>
                  <div class="text-[9px] font-bold text-white uppercase leading-tight line-clamp-2">Riassortimenti Sempre Garantiti</div>
                  <div class="text-[8px] text-indigo-300 font-medium">27 Novembre</div>
                </div>
              </div>
            </div>

            <!-- POST 5: Portale My Italsport -->
            <div class="aspect-square relative cursor-pointer group rounded-sm overflow-hidden post-cover" style="background-image: url('data:image/jpeg;base64,{b64_post5}');" onclick="openPostModal(4)">
              <div class="absolute inset-0 post-overlay flex flex-col justify-between p-2">
                <div class="flex justify-between items-start">
                  <span class="bg-purple-600/90 text-white text-[8px] font-bold px-1.5 py-0.5 rounded backdrop-blur">DIGITAL</span>
                  <i class="fa-solid fa-mobile-screen text-purple-300 text-[11px]"></i>
                </div>
                <div>
                  <div class="text-[9px] font-bold text-white uppercase leading-tight line-clamp-2">Il Portale My Italsport</div>
                  <div class="text-[8px] text-purple-300 font-medium">06 Dicembre</div>
                </div>
              </div>
            </div>

            <!-- POST 6: Winter Training -->
            <div class="aspect-square relative cursor-pointer group rounded-sm overflow-hidden post-cover" style="background-image: url('data:image/jpeg;base64,{b64_post6}');" onclick="openPostModal(5)">
              <div class="absolute inset-0 post-overlay flex flex-col justify-between p-2">
                <div class="flex justify-between items-start">
                  <span class="bg-teal-600/90 text-white text-[8px] font-bold px-1.5 py-0.5 rounded backdrop-blur">WINTER</span>
                  <i class="fa-solid fa-snowflake text-cyan-300 text-[11px]"></i>
                </div>
                <div>
                  <div class="text-[9px] font-bold text-white uppercase leading-tight line-clamp-2">Winter Training: Non Fermarti</div>
                  <div class="text-[8px] text-teal-300 font-medium">16 Dicembre</div>
                </div>
              </div>
            </div>

          </div>

          <!-- Bottom bar Instagram -->
          <div class="p-3 bg-slate-950 border-t border-slate-900 flex justify-around text-slate-400 text-lg">
            <i class="fa-solid fa-house text-white"></i>
            <i class="fa-solid fa-magnifying-glass"></i>
            <i class="fa-regular fa-square-plus"></i>
            <i class="fa-solid fa-clapperboard text-sky-400" onclick="openReelSimulator()" title="Apri Reel 3D"></i>
            <div class="w-5 h-5 rounded-full border border-white overflow-hidden">
              <img src="data:image/png;base64,{b64_logo}" class="w-full h-full object-cover">
            </div>
          </div>

        </div>

      </div>
    </div>
  </div>

  <!-- ======================================================== -->
  <!-- MODALE DETTAGLIO POST INSTAGRAM (Caption, Like, Commenti) -->
  <!-- ======================================================== -->
  <div id="post-modal" class="fixed inset-0 bg-black/85 backdrop-blur-md z-50 hidden flex items-center justify-center p-4">
    <div class="bg-slate-900 border border-slate-700 max-w-3xl w-full rounded-2xl overflow-hidden shadow-2xl flex flex-col md:flex-row max-h-[90vh]">
      
      <!-- Immagine Post Ingrandita -->
      <div class="md:w-1/2 bg-black flex items-center justify-center relative min-h-[300px]">
        <img id="modal-post-img" src="" alt="Post Preview" class="w-full h-full object-contain">
        <span id="modal-post-badge" class="absolute top-3 left-3 px-2.5 py-1 rounded-md text-xs font-bold text-white shadow"></span>
      </div>

      <!-- Scheda Dettagli e Copywriting -->
      <div class="md:w-1/2 flex flex-col justify-between p-5 bg-slate-900">
        <div>
          <!-- Header Modale -->
          <div class="flex items-center justify-between pb-3 border-b border-slate-800">
            <div class="flex items-center gap-2.5">
              <div class="w-8 h-8 rounded-full bg-slate-800 border border-emerald-500/50 p-1 flex items-center justify-center">
                <img src="data:image/png;base64,{b64_logo}" class="max-w-full max-h-full object-contain">
              </div>
              <div>
                <div class="text-xs font-bold text-white">italsportgroup</div>
                <div id="modal-post-date" class="text-[10px] text-slate-400"></div>
              </div>
            </div>
            <button onclick="closePostModal()" class="w-7 h-7 rounded-full bg-slate-800 hover:bg-slate-700 flex items-center justify-center text-slate-300">
              <i class="fa-solid fa-xmark"></i>
            </button>
          </div>

          <!-- Informazioni di Target & Obiettivo Strategico -->
          <div class="mt-3 p-2.5 rounded-lg bg-slate-800/60 border border-slate-700/60 text-xs">
            <div class="font-bold text-emerald-400 flex items-center gap-1.5 mb-1">
              <i class="fa-solid fa-bullseye"></i> Obiettivo Strategico
            </div>
            <div id="modal-post-objective" class="text-slate-300 leading-snug"></div>
            <div class="mt-1 pt-1 border-t border-slate-700/50 flex justify-between text-[11px] text-slate-400">
              <span id="modal-post-format"></span>
              <span id="modal-post-target" class="text-amber-400 font-semibold"></span>
            </div>
          </div>

          <!-- Testo del Post (Caption Completa) -->
          <div class="mt-3">
            <div class="text-[11px] font-semibold text-slate-400 uppercase tracking-wider mb-1">Testo Pubblicato (Caption):</div>
            <div id="modal-post-caption" class="text-xs text-slate-200 leading-relaxed max-h-[220px] overflow-y-auto pr-2 custom-scrollbar whitespace-pre-line font-normal"></div>
          </div>
        </div>

        <!-- Azioni e Commenti simulati -->
        <div class="pt-3 border-t border-slate-800 mt-3">
          <div class="flex items-center justify-between text-base text-slate-300 mb-2">
            <div class="flex items-center gap-3">
              <i class="fa-solid fa-heart text-rose-500 cursor-pointer"></i>
              <i class="fa-regular fa-comment hover:text-white cursor-pointer"></i>
              <i class="fa-regular fa-paper-plane hover:text-white cursor-pointer"></i>
            </div>
            <i class="fa-regular fa-bookmark hover:text-white cursor-pointer"></i>
          </div>
          <div id="modal-post-likes" class="text-[11px] font-bold text-white"></div>
        </div>

      </div>

    </div>
  </div>

  <!-- ======================================================== -->
  <!-- SIMULATORE INTERATTIVO REEL 3D (Animazione Maglia 360°)   -->
  <!-- ======================================================== -->
  <div id="reel-modal" class="fixed inset-0 bg-black/90 backdrop-blur-md z-50 hidden flex items-center justify-center p-4">
    <div class="relative w-[360px] h-[720px] bg-slate-950 rounded-[40px] border-4 border-sky-500/80 shadow-2xl overflow-hidden flex flex-col justify-between">
      
      <!-- Top Bar Reel -->
      <div class="pt-4 px-4 flex justify-between items-center z-20 text-white">
        <div class="flex items-center gap-2">
          <button onclick="closeReelSimulator()" class="w-8 h-8 rounded-full bg-black/60 flex items-center justify-center text-sm">
            <i class="fa-solid fa-arrow-left"></i>
          </button>
          <span class="font-bold text-sm tracking-wide">Reels</span>
        </div>
        <div class="flex items-center gap-2">
          <span class="text-[10px] bg-sky-500/30 text-sky-300 border border-sky-400/40 px-2 py-0.5 rounded-full font-semibold">Configuratore 3D Live</span>
          <button onclick="closeReelSimulator()" class="text-slate-400 hover:text-white">
            <i class="fa-solid fa-xmark text-lg"></i>
          </button>
        </div>
      </div>

      <!-- Area 3D Simulazione Centrata -->
      <div class="absolute inset-0 flex flex-col items-center justify-center z-10 p-6 pointer-events-none">
        
        <!-- Sfondo griglia 3D con effetto luci da stadio -->
        <div class="absolute inset-0 bg-[radial-gradient(circle_at_center,rgba(14,165,233,0.18)_0%,transparent_70%)]"></div>
        <div class="absolute top-20 text-center">
          <div class="inline-block px-3 py-1 rounded-full bg-slate-900/80 border border-sky-400/50 text-sky-400 font-bold text-xs shadow-lg mb-1">
            <i class="fa-solid fa-arrows-rotate mr-1 animate-spin"></i> ANTEPRIMA ROTAZIONE 360°
          </div>
          <p class="text-[11px] text-slate-300">Come una società disegna la divisa online prima dell'ordine</p>
        </div>

        <!-- MAGLIA 3D INTERATTIVA ANIMATA -->
        <div class="jersey-3d-container w-48 h-56 flex items-center justify-center my-auto pointer-events-auto cursor-grab active:cursor-grabbing" onclick="toggle3DPause()">
          <div id="jersey-3d" class="jersey-3d-model relative w-40 h-52">
            
            <!-- Lato Anteriore Maglia -->
            <div id="jersey-front" class="absolute inset-0 rounded-2xl bg-gradient-to-b from-emerald-600 via-emerald-700 to-slate-900 border-2 border-emerald-400/60 shadow-2xl flex flex-col items-center justify-between p-3">
              <div class="w-full flex justify-between items-center text-[10px]">
                <div class="w-6 h-6 rounded bg-amber-500 flex items-center justify-center text-slate-950 font-black text-[9px] shadow">ASD</div>
                <div class="w-10 h-3 bg-white/20 rounded"></div>
                <div class="text-[8px] font-bold text-white tracking-widest">ITALSPORT</div>
              </div>
              
              <!-- Pattern Geometrico Centrale -->
              <div class="text-center my-auto">
                <div class="text-xl font-black text-white tracking-tighter drop-shadow-md">CUSTOM 3D</div>
                <div class="text-[9px] font-semibold text-emerald-200 uppercase tracking-widest mt-0.5">Sublimazione HD</div>
              </div>

              <!-- Numero Giocatore -->
              <div class="text-center">
                <div class="text-3xl font-black text-amber-300 drop-shadow">10</div>
                <div class="text-[8px] text-slate-300 uppercase font-semibold">Tessuto Tecnico Pro</div>
              </div>
            </div>

          </div>
        </div>

        <!-- Selettore Colori Interattivo per il Cliente -->
        <div class="w-full pointer-events-auto flex flex-col items-center gap-1.5 mb-16">
          <div class="text-[10px] text-slate-300 font-semibold flex items-center gap-1">
            <i class="fa-solid fa-palette text-amber-400"></i> Tocca per cambiare i colori sociali:
          </div>
          <div class="flex items-center gap-2 bg-slate-900/90 backdrop-blur border border-slate-700 p-1.5 rounded-full shadow-lg">
            <button onclick="changeJerseyColor('emerald')" class="w-6 h-6 rounded-full bg-emerald-500 border-2 border-white focus:scale-110 transition shadow"></button>
            <button onclick="changeJerseyColor('blue')" class="w-6 h-6 rounded-full bg-sky-500 border-2 border-slate-700 hover:border-white focus:scale-110 transition shadow"></button>
            <button onclick="changeJerseyColor('red')" class="w-6 h-6 rounded-full bg-rose-500 border-2 border-slate-700 hover:border-white focus:scale-110 transition shadow"></button>
            <button onclick="changeJerseyColor('gold')" class="w-6 h-6 rounded-full bg-amber-400 border-2 border-slate-700 hover:border-white focus:scale-110 transition shadow"></button>
            <button onclick="changeJerseyColor('dark')" class="w-6 h-6 rounded-full bg-slate-800 border-2 border-slate-700 hover:border-white focus:scale-110 transition shadow"></button>
          </div>
        </div>

      </div>

      <!-- Sidebar Azioni Reel (Like, Commenti, Condividi) -->
      <div class="absolute right-3 bottom-24 flex flex-col items-center gap-4 z-20 text-white">
        <button onclick="likeReel()" class="flex flex-col items-center group">
          <div id="reel-heart-btn" class="w-10 h-10 rounded-full bg-slate-900/70 border border-slate-700/60 flex items-center justify-center text-lg group-hover:scale-110 transition">
            <i class="fa-solid fa-heart text-rose-500"></i>
          </div>
          <span id="reel-likes-count" class="text-[11px] font-bold mt-1">428</span>
        </button>

        <button class="flex flex-col items-center group">
          <div class="w-10 h-10 rounded-full bg-slate-900/70 border border-slate-700/60 flex items-center justify-center text-lg group-hover:scale-110 transition">
            <i class="fa-solid fa-comment text-white"></i>
          </div>
          <span class="text-[11px] font-bold mt-1">36</span>
        </button>

        <button class="flex flex-col items-center group">
          <div class="w-10 h-10 rounded-full bg-slate-900/70 border border-slate-700/60 flex items-center justify-center text-lg group-hover:scale-110 transition">
            <i class="fa-solid fa-share text-white"></i>
          </div>
          <span class="text-[11px] font-bold mt-1">89</span>
        </button>

        <!-- Vinile Audio in rotazione -->
        <div class="w-9 h-9 rounded-full bg-slate-950 border-2 border-sky-400 p-1 flex items-center justify-center vinyl-disc shadow-lg">
          <img src="data:image/png;base64,{b64_logo}" class="max-w-full max-h-full object-contain">
        </div>
      </div>

      <!-- Didascalia e Audio Inferiore -->
      <div class="p-4 z-20 bg-gradient-to-t from-black via-black/80 to-transparent">
        <div class="flex items-center gap-2 mb-1.5">
          <div class="w-7 h-7 rounded-full bg-emerald-500 p-0.5 border border-white flex items-center justify-center">
            <img src="data:image/png;base64,{b64_logo}" class="max-w-full max-h-full object-contain">
          </div>
          <span class="font-bold text-xs text-white">italsportgroup</span>
          <span class="text-[10px] text-emerald-400 font-semibold">• Segui</span>
        </div>
        
        <p class="text-xs text-slate-200 line-clamp-2 leading-snug">
          Disegna la divisa del tuo club in 3D in tempo reale: colori, sponsor e stemmi a 360° prima della produzione sartoriale. Provalo al link in bio! 🚀⚽
        </p>

        <div class="mt-2 flex items-center gap-2 text-[10px] text-sky-300 font-medium">
          <i class="fa-solid fa-music text-[9px]"></i>
          <span>Audio Ufficiale • Italsport Custom Studio (Trend)</span>
        </div>
      </div>

    </div>
  </div>

  <script>
    // Dati completi dei Post
    const postsData = [
      {{
        badge: "30 ANNI DI STORIA",
        badgeBg: "bg-emerald-600",
        img: "data:image/jpeg;base64,{b64_post1}",
        date: "Sabato 31 Ottobre 2026",
        objective: "Presentare la solidità e la sartorialità di Italsport Group con un messaggio autorevole. Far percepire ai dirigenti e presidenti il valore di lavorare con una realtà che da 30 anni veste lo sport italiano.",
        format: "Carosello 4 Slide (1080x1350)",
        target: "Target: 3–4 Richieste Campionario",
        likes: "184 Mi piace",
        caption: `Dietro ogni divisa che scende in campo la domenica c’è una storia, ci sono i sacrifici di una società e l’orgoglio di un intero territorio. 🇮🇹⚽\\n\\nDa oltre 30 anni, in Italsport Group mettiamo la nostra esperienza al servizio dello sport, delle scuole e delle aziende.\\nNon ci limitiamo a fornire abbigliamento: affianchiamo presidenti, dirigenti e atleti per creare un’identità unica e duratura.\\n\\nCosa significa scegliere Italsport?\\n✨ Personalizzazione totale con tecniche all'avanguardia (stampa sublimatica HD, DTF, ricami e transfer)\\n✨ Tessuti tecnici resistenti, traspiranti ed ergonomici\\n✨ Un partner affidabile al tuo fianco: dalla bozza grafica alla consegna puntuale dei kit\\n\\nIl nostro motto è semplice e chiaro: "Tu scegli Italsport, al resto pensiamo noi."\\n\\nSei pronto a dare alla tua squadra la divisa che merita?\\n👉 Contattaci in Direct o visita il nostro sito al link in bio per richiedere un campionario per la tua società!\\n\\n#italsportgroup #teamwear #abbigliamentosportivo #societasportive #calciodilettanti #basketitalia #volleylife #passionesportiva #madeinitaly`
      }},
      {{
        badge: "CONFIGURATORE 3D REEL",
        badgeBg: "bg-sky-600",
        img: "data:image/jpeg;base64,{b64_post2}",
        date: "Domenica 08 Novembre 2026",
        objective: "Mostrare a schermo la facilità di utilizzo del Configuratore 3D, spingendo allenatori e dirigenti a provare la rotazione a 360° e a salvare le proprie divise online.",
        format: "Video Reel 9:16 (30 secondi)",
        target: "Target: 15–20 Configurazioni Salvate",
        likes: "428 Mi piace",
        caption: `Vuoi vedere in anteprima la nuova divisa della tua squadra prima ancora di ordinarla? 🚀\\n\\nCon il nostro CONFIGURATORE 3D ONLINE è facilissimo:\\n1️⃣ Scegli il modello che preferisci tra le nostre linee Custom\\n2️⃣ Seleziona i colori sociali del tuo club in tempo reale con un semplice click\\n3️⃣ Carica lo stemma societario e i loghi degli sponsor in alta risoluzione\\n4️⃣ Ruota la divisa a 360° e osserva ogni singolo dettaglio da qualsiasi angolazione\\n\\nUna volta approvato il design, il nostro reparto produttivo si occupa di tutto: taglio laser, stampa sublimatica ad altissima definizione e confezione sartoriale.\\n\\nDalla tua creatività al fischio d'inizio della domenica.\\n\\n👉 Prova subito a creare la maglia del tuo club: clicca sul link in bio ed entra nel Configuratore 3D!\\n\\n#configuratore3d #divisesportive #magliapersonalizzata #teamwear #sublimazione #italsportgroup #calciodilettanti #sportcustom #innovazione`
      }},
      {{
        badge: "TESSERA FEDELTÀ PRO-CLUB",
        badgeBg: "bg-amber-600",
        img: "data:image/jpeg;base64,{b64_post3}",
        date: "Mercoledì 18 Novembre 2026",
        objective: "Promuovere le convenzioni speciali del programma Pro-Club già attivo su store.italsport-group.it, incentivando le società sportive ad affiliarsi per accedere a listini dedicati e corsie preferenziali.",
        format: "Grafica Card (1080x1350)",
        target: "Target: 2–3 Nuove Convenzioni Club",
        likes: "215 Mi piace",
        caption: `Conosci già i vantaggi della nostra TESSERA FEDELTÀ e del programma MY ITALSPORT PRO-CLUB? 💳🏆\\n\\nPer noi di Italsport un accordo di fornitura non si esaurisce con la consegna delle maglie. È l’inizio di una partnership continuativa pensata per premiare la fedeltà delle società sportive e facilitare la vita a dirigenti e famiglie:\\n\\n🔹 Listini e sconti dedicati per tutta la stagione sportiva\\n🔹 Convenzioni speciali estese alle famiglie dei tesserati per l'acquisto del merchandising\\n🔹 Priorità di produzione e riassortimento veloce sui capi a magazzino\\n🔹 Accesso all'area riservata online per monitorare ordini, disponibilità e scaricare le fatture\\n\\nEntrare nella famiglia Italsport come membro Pro-Club significa avere un partner fidato che investe sulla crescita del tuo club, stagione dopo stagione.\\n\\n👉 Vuoi attivare la Tessera Fedeltà e la convenzione Pro-Club per la tua società?\\nScrivici un messaggio in Direct o contattaci all'indirizzo commerciale@italsport-group.it!\\n\\n#tesserafedelta #proclub #myitalsport #societasportive #convenzionisportive #fidelizzazione #dirigentiasd #teamwear #italsportgroup`
      }},
      {{
        badge: "RIASSORTIMENTI GARANTITI",
        badgeBg: "bg-indigo-600",
        img: "data:image/jpeg;base64,{b64_post4}",
        date: "Venerdì 27 Novembre 2026",
        objective: "Eliminare la preoccupazione più diffusa tra i segretari sportivi: 'Se arriva un nuovo iscritto a metà anno, trovo ancora la maglia?'. Con Italsport la risposta è sempre sì.",
        format: "Carosello 4 Slide (1080x1350)",
        target: "Target: 2–3 Richieste Riassortimento",
        likes: "196 Mi piace",
        caption: `Cosa succede quando a metà stagione o all'inizio del nuovo anno arrivano nuovi iscritti nella tua società sportiva? 👦👧⚽\\n\\nCon Italsport la risposta è semplice: riceveranno esattamente la stessa identica divisa dei compagni di squadra.\\n\\nGrazie alla nostra produzione interna e a oltre 30 anni di archivio storico:\\n✅ Memorizziamo i codici tessuto, i pantoni colore e i file vettoriali di ogni singolo club\\n✅ Possiamo riprodurre anche piccoli quantitativi di riassortimento senza costringervi a cambiare modello\\n✅ Nessun rischio di dover rifare le divise da zero ogni anno, tutelando il budget della società e delle famiglie\\n\\nLa tranquillità di una gestione sportiva serena comincia dalla scelta di un partner che vi garantisce continuità nel tempo.\\n\\n👉 Vuoi pianificare la fornitura della tua società con la certezza dei riassortimenti? Parla con un nostro consulente al link in bio!\\n\\n#continuità #riassortimento #societasportive #calciogiovanile #basketgiovanile #pallavoloitaliana #teamwearitaly #italsportgroup #affidabilita`
      }},
      {{
        badge: "PORTALE MY ITALSPORT",
        badgeBg: "bg-purple-600",
        img: "data:image/jpeg;base64,{b64_post5}",
        date: "Domenica 06 Dicembre 2026",
        objective: "Presentare la soluzione digitale per le società: un'area riservata online dove ogni genitore o atleta acquista direttamente il kit approvato, azzerando il caos logistico in sede.",
        format: "Grafica Infografica (1080x1350)",
        target: "Target: 2–3 Richieste Attivazione Portale",
        likes: "248 Mi piace",
        caption: `Magazzini improvvisati, ordini disorganizzati e corse contro il tempo per raccogliere le taglie: sappiamo quanto possa essere impegnativa la gestione logistica di una società sportiva. 📦⏱️\\n\\nProprio ascoltando le esigenze reali di dirigenti e atleti è nato il progetto MY ITALSPORT.\\n\\nCome funziona il servizio?\\n1️⃣ Creiamo uno spazio web riservato ed esclusivo per la tua società\\n2️⃣ I membri e le famiglie accedono con le proprie credenziali e ordinano direttamente online il kit ufficiale approvato\\n3️⃣ Visualizzi lo stato d'avanzamento, gestisci i documenti e scarichi le fatture direttamente da una dashboard intuitiva\\n4️⃣ La merce viene imballata ed etichettata con precisione, pronta per la consegna\\n\\nCon My Italsport rivoluzioni la gestione del tuo materiale sportivo e risparmi tempo prezioso da dedicare al campo.\\n\\n👉 Vuoi scoprire come attivare la piattaforma per il tuo club? Contattaci per una dimostrazione gratuita: commerciale@italsport-group.it!\\n\\n#myitalsport #logisticasportiva #organizzazionesportiva #societasportive #gestioneatleti #abbigliamentosportivo #italsportgroup #soluzionidigitali`
      }},
      {{
        badge: "WINTER TRAINING",
        badgeBg: "bg-teal-600",
        img: "data:image/jpeg;base64,{b64_post6}",
        date: "Mercoledì 16 Dicembre 2026",
        objective: "Promuovere le linee termiche e antipioggia personalizzabili per gli allenamenti invernali, intercettando gli ordini di completamento delle società prima della pausa natalizia.",
        format: "Post Fotografico (1080x1350)",
        target: "Target: 3–4 Richieste Fornitura Invernale",
        likes: "274 Mi piace",
        caption: `Freddo, pioggia o vento: la vera passione per lo sport non si ferma davanti all'inverno. ❄️🏃‍♂️\\n\\nPer accompagnare gli atleti negli allenamenti e nelle sfide più impegnative, abbiamo selezionato e personalizzato i migliori capi tecnici invernali:\\n🧥 Giacconi termici idrorepellenti imbottiti per dirigenti e panchina\\n🌧️ K-way traspiranti e giubbini antivento con vestibilità ergonomica\\n👖 Pantaloni d'allenamento tecnici con zip e fasce elasticizzate\\n🧣 Accessori coordinati con i colori sociali (scaldacollo, cappellini e guanti)\\n\\nProteggi i tuoi atleti e mantieni alto il calore della tua squadra.\\n\\n👉 Scopri le nostre disponibilità invernali su store.italsport-group.it o scrivici in DM!\\n\\n#wintertraining #abbigliamentoinvernale #calciotrain #tutesportive #termiche #asdsport #italsportgroup`
      }}
    ];

    function openPostModal(index) {{
      const p = postsData[index];
      document.getElementById('modal-post-img').src = p.img;
      document.getElementById('modal-post-badge').className = 'absolute top-3 left-3 px-2.5 py-1 rounded-md text-xs font-bold text-white shadow ' + p.badgeBg;
      document.getElementById('modal-post-badge').innerText = p.badge;
      document.getElementById('modal-post-date').innerText = p.date;
      document.getElementById('modal-post-objective').innerText = p.objective;
      document.getElementById('modal-post-format').innerText = p.format;
      document.getElementById('modal-post-target').innerText = p.target;
      document.getElementById('modal-post-caption').innerText = p.caption;
      document.getElementById('modal-post-likes').innerText = p.likes;
      document.getElementById('post-modal').classList.remove('hidden');
    }}

    function closePostModal() {{
      document.getElementById('post-modal').classList.add('hidden');
    }}

    function openReelSimulator() {{
      document.getElementById('reel-modal').classList.remove('hidden');
    }}

    function closeReelSimulator() {{
      document.getElementById('reel-modal').classList.add('hidden');
    }}

    let is3DPaused = false;
    function toggle3DPause() {{
      const m = document.getElementById('jersey-3d');
      is3DPaused = !is3DPaused;
      if (is3DPaused) {{
        m.classList.add('paused');
      }} else {{
        m.classList.remove('paused');
      }}
    }}

    function changeJerseyColor(theme) {{
      const front = document.getElementById('jersey-front');
      if (theme === 'emerald') {{
        front.className = 'absolute inset-0 rounded-2xl bg-gradient-to-b from-emerald-600 via-emerald-700 to-slate-900 border-2 border-emerald-400/60 shadow-2xl flex flex-col items-center justify-between p-3';
      }} else if (theme === 'blue') {{
        front.className = 'absolute inset-0 rounded-2xl bg-gradient-to-b from-sky-600 via-blue-800 to-slate-900 border-2 border-sky-400/60 shadow-2xl flex flex-col items-center justify-between p-3';
      }} else if (theme === 'red') {{
        front.className = 'absolute inset-0 rounded-2xl bg-gradient-to-b from-rose-600 via-red-800 to-slate-900 border-2 border-rose-400/60 shadow-2xl flex flex-col items-center justify-between p-3';
      }} else if (theme === 'gold') {{
        front.className = 'absolute inset-0 rounded-2xl bg-gradient-to-b from-amber-500 via-amber-700 to-slate-900 border-2 border-amber-300/60 shadow-2xl flex flex-col items-center justify-between p-3';
      }} else if (theme === 'dark') {{
        front.className = 'absolute inset-0 rounded-2xl bg-gradient-to-b from-slate-700 via-slate-800 to-black border-2 border-slate-500/60 shadow-2xl flex flex-col items-center justify-between p-3';
      }}
    }}

    let reelLiked = false;
    function likeReel() {{
      reelLiked = !reelLiked;
      const countEl = document.getElementById('reel-likes-count');
      let count = parseInt(countEl.innerText);
      if (reelLiked) {{
        countEl.innerText = count + 1;
        document.getElementById('reel-heart-btn').classList.add('bg-rose-500/20');
      }} else {{
        countEl.innerText = count - 1;
        document.getElementById('reel-heart-btn').classList.remove('bg-rose-500/20');
      }}
    }}

    function openHighlight(idx) {{
      if (idx === 0) {{
        openReelSimulator();
      }} else if (idx === 1) {{
        openPostModal(2);
      }} else if (idx === 2) {{
        openPostModal(0);
      }} else if (idx === 3) {{
        openPostModal(3);
      }} else if (idx === 4) {{
        openPostModal(0);
      }} else if (idx === 5) {{
        openPostModal(4);
      }}
    }}

    function toggleView(mode) {{
      const phone = document.getElementById('phone-wrapper');
      const btnMob = document.getElementById('btn-mobile');
      const btnDsk = document.getElementById('btn-desktop');
      if (mode === 'desktop') {{
        phone.className = 'w-full max-w-4xl bg-black rounded-3xl p-6 shadow-2xl border-4 border-slate-700 transition-all duration-300';
        btnDsk.className = 'px-3.5 py-1.5 rounded-lg bg-emerald-600 text-white font-medium shadow-sm transition';
        btnMob.className = 'px-3.5 py-1.5 rounded-lg bg-slate-700 text-slate-300 font-medium transition hover:bg-slate-600';
      }} else {{
        phone.className = 'w-[410px] bg-black rounded-[48px] p-3 shadow-2xl border-4 border-slate-700 shadow-emerald-950/30 transition-all duration-300 relative';
        btnMob.className = 'px-3.5 py-1.5 rounded-lg bg-emerald-600 text-white font-medium shadow-sm transition';
        btnDsk.className = 'px-3.5 py-1.5 rounded-lg bg-slate-700 text-slate-300 font-medium transition hover:bg-slate-600';
      }}
    }}
  </script>
</body>
</html>
'''

with open('Instagram_Mockup_Italsport.html', 'w', encoding='utf-8') as f:
    f.write(html_mockup)

print("Updated Instagram_Mockup_Italsport.html successfully.")

# ========================================================
# 3. GENERAZIONE DEL PDF RIFINITO DA PRESENTARE AL CLIENTE
# ========================================================
html_pdf = f'''<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="UTF-8">
  <title>Piano Strategico Social Media B2B - ITALSPORT GROUP</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap');
    
    @page {{
      size: A4 portrait;
      margin: 0;
    }}
    
    * {{
      box-sizing: border-box;
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
    }}

    body {{
      margin: 0;
      padding: 0;
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
      background-color: #090d16;
      color: #f1f5f9;
      font-size: 11pt;
      line-height: 1.45;
    }}

    .page {{
      width: 210mm;
      height: 297mm;
      page-break-after: always;
      position: relative;
      padding: 16mm 18mm 16mm 18mm;
      overflow: hidden;
      background: #090d16;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}

    .page-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
      padding-bottom: 8px;
      margin-bottom: 14px;
    }}

    .page-header .brand {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .page-header .brand img {{
      height: 26px;
      object-fit: contain;
    }}

    .page-header .doc-title {{
      font-size: 8pt;
      color: #94a3b8;
      text-transform: uppercase;
      letter-spacing: 0.8px;
      font-weight: 600;
    }}

    .page-header .date-badge {{
      font-size: 8pt;
      background: rgba(16, 185, 129, 0.15);
      color: #34d399;
      padding: 3px 8px;
      border-radius: 6px;
      font-weight: 700;
      border: 1px solid rgba(16, 185, 129, 0.3);
    }}

    .page-footer {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-top: 1px solid rgba(255, 255, 255, 0.1);
      padding-top: 8px;
      font-size: 8pt;
      color: #64748b;
    }}

    .page-footer .agency {{
      font-weight: 600;
      color: #94a3b8;
    }}

    h1, h2, h3, h4 {{
      margin-top: 0;
      font-weight: 800;
      letter-spacing: -0.3px;
    }}

    .badge {{
      display: inline-block;
      padding: 2px 7px;
      border-radius: 4px;
      font-size: 7.5pt;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}
    .badge-emerald {{ background: rgba(16, 185, 129, 0.2); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.4); }}
    .badge-gold {{ background: rgba(245, 158, 11, 0.2); color: #fbbf24; border: 1px solid rgba(245, 158, 11, 0.4); }}
    .badge-blue {{ background: rgba(56, 189, 248, 0.2); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.4); }}
    .badge-purple {{ background: rgba(168, 85, 247, 0.2); color: #c084fc; border: 1px solid rgba(168, 85, 247, 0.4); }}

    .card {{
      background: #0f172a;
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 12px;
      padding: 14px 16px;
      margin-bottom: 12px;
    }}

    .table-custom {{
      width: 100%;
      border-collapse: separate;
      border-spacing: 0;
      font-size: 8pt;
      border-radius: 8px;
      overflow: hidden;
      border: 1px solid rgba(255, 255, 255, 0.1);
      margin-bottom: 12px;
    }}

    .table-custom th {{
      background: #1e293b;
      color: #f8fafc;
      font-weight: 700;
      padding: 7px 10px;
      text-align: left;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }}

    .table-custom td {{
      padding: 6px 10px;
      background: rgba(15, 23, 42, 0.6);
      border-bottom: 1px solid rgba(255, 255, 255, 0.05);
      color: #cbd5e1;
      vertical-align: middle;
    }}

    .table-custom tr:nth-child(even) td {{
      background: rgba(30, 41, 59, 0.4);
    }}

    .post-card {{
      display: flex;
      gap: 16px;
      background: #0f172a;
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 14px;
      padding: 14px;
      flex: 1;
      overflow: hidden;
    }}

    .visual-mockup {{
      width: 62mm;
      height: 62mm;
      border-radius: 10px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      position: relative;
      flex-shrink: 0;
      border: 1px solid rgba(255, 255, 255, 0.15);
      box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.5);
      background-size: cover;
      background-position: center;
    }}

    .visual-mockup-overlay {{
      background: linear-gradient(180deg, rgba(0,0,0,0.2) 0%, rgba(0,0,0,0.1) 40%, rgba(0,0,0,0.92) 100%);
      padding: 8px;
      position: absolute;
      inset: 0;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}

    .post-details {{
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      overflow: hidden;
    }}

    .caption-box {{
      background: #020617;
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 8px;
      padding: 10px 12px;
      font-size: 8pt;
      line-height: 1.42;
      color: #cbd5e1;
      font-family: 'Plus Jakarta Sans', monospace;
      white-space: pre-line;
      flex: 1;
      overflow: hidden;
    }}
  </style>
</head>
<body>

  <!-- ==================== PAGINA 1: COPERTINA ESECUTIVA ==================== -->
  <div class="page" style="background: radial-gradient(circle at 80% 20%, rgba(16, 185, 129, 0.15) 0%, rgba(9, 13, 22, 1) 60%), radial-gradient(circle at 10% 80%, rgba(56, 189, 248, 0.12) 0%, rgba(9, 13, 22, 1) 50%), #090d16;">
    <div style="display: flex; justify-content: space-between; align-items: center;">
      <div style="background: rgba(255, 255, 255, 0.05); padding: 8px 18px; border-radius: 12px; border: 1px solid rgba(255, 255, 255, 0.1);">
        <img src="data:image/png;base64,{b64_logo}" style="height: 48px; object-fit: contain;">
      </div>
      <div style="text-align: right;">
        <span class="badge badge-emerald" style="font-size: 8.5pt; padding: 5px 12px;">PROPOSTA ESECUTIVA & PIANO EDITORIALE</span>
        <div style="font-size: 8.5pt; color: #94a3b8; margin-top: 4px;">Periodo: Novembre – Dicembre 2026 (Bimestre Pilota)</div>
      </div>
    </div>

    <div style="margin-top: 40px; margin-bottom: 28px;">
      <div style="display: inline-flex; align-items: center; gap: 8px; background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.3); padding: 4px 12px; border-radius: 999px; margin-bottom: 14px;">
        <span style="width: 7px; height: 7px; background: #10b981; border-radius: 50%;"></span>
        <span style="font-size: 8.5pt; font-weight: 700; color: #34d399; text-transform: uppercase; letter-spacing: 0.8px;">Posizionamento Digitale B2B & Lead Generation Club</span>
      </div>

      <h1 style="font-size: 25pt; line-height: 1.15; margin-bottom: 14px; color: #ffffff;">
        PIANO STRATEGICO SOCIAL MEDIA &<br>
        <span style="background: linear-gradient(90deg, #10b981 0%, #38bdf8 50%, #fbbf24 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">COMUNICAZIONE ISTITUZIONALE B2B</span><br>
        PER ITALSPORT GROUP
      </h1>

      <p style="font-size: 11pt; color: #94a3b8; max-width: 160mm; line-height: 1.5; font-weight: 500;">
        Una strategia mirata per trasformare Instagram nel canale di riferimento per l'acquisizione e la fidelizzazione di società sportive, scuole e aziende: valorizzazione dei <strong>30 anni di storia manifatturiera</strong>, del <strong>Configuratore 3D</strong>, del programma <strong>Tessera Fedeltà Pro-Club</strong> e della certezza dei riassortimenti garantiti nel tempo.
      </p>
    </div>

    <!-- Punti Chiave in Evidenza -->
    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px; margin-bottom: 24px;">
      <div class="card" style="border-top: 3px solid #10b981; margin: 0;">
        <div style="font-size: 8pt; color: #94a3b8; text-transform: uppercase; font-weight: 700;">Asset 1</div>
        <div style="font-size: 11pt; font-weight: 800; color: #ffffff; margin: 4px 0;">30 Anni di Storia</div>
        <p style="font-size: 8pt; color: #94a3b8; margin: 0;">Produzione e personalizzazione sartoriale italiana (DTF, sublimazione HD, ricami e taglio).</p>
      </div>
      <div class="card" style="border-top: 3px solid #38bdf8; margin: 0;">
        <div style="font-size: 8pt; color: #94a3b8; text-transform: uppercase; font-weight: 700;">Asset 2</div>
        <div style="font-size: 11pt; font-weight: 800; color: #ffffff; margin: 4px 0;">Configuratore 3D</div>
        <p style="font-size: 8pt; color: #94a3b8; margin: 0;">Il tool online che consente alle società di creare la divisa e visualizzarla a 360° in anteprima.</p>
      </div>
      <div class="card" style="border-top: 3px solid #f59e0b; margin: 0;">
        <div style="font-size: 8pt; color: #94a3b8; text-transform: uppercase; font-weight: 700;">Asset 3</div>
        <div style="font-size: 11pt; font-weight: 800; color: #ffffff; margin: 4px 0;">Tessera Pro-Club</div>
        <p style="font-size: 8pt; color: #94a3b8; margin: 0;">Programma di affiliazione con listini riservati, convenzioni per atleti e priorità riordini.</p>
      </div>
    </div>

    <!-- Box Obiettivo Realistico Condiviso -->
    <div style="background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.25); border-radius: 12px; padding: 14px 18px; margin-bottom: 20px;">
      <div style="font-size: 9pt; font-weight: 800; color: #34d399; text-transform: uppercase; margin-bottom: 4px;">
        🎯 OBIETTIVO STRATEGICO CONDIVISO (BIMESTRE PILOTA NOVEMBRE – DICEMBRE 2026):
      </div>
      <div style="font-size: 9pt; color: #e2e8f0; line-height: 1.45;">
        Attivare tra le <strong>5 e le 8 nuove società sportive</strong> nel circuito Tessera Fedeltà / Pro-Club, generare <strong>40–50 configurazioni salvate</strong> sul tool 3D, inviare <strong>5–8 campionari gratuiti</strong> a dirigenti profilati e convertire le prime <strong>1–2 forniture complete di club</strong> (valore stimato prudenziale: <strong>€ 3.500 – € 6.500</strong>), avviando una relazione commerciale pluriennale.
      </div>
    </div>

    <div style="display: flex; justify-content: space-between; align-items: flex-end; border-top: 1px solid rgba(255, 255, 255, 0.1); padding-top: 12px;">
      <div>
        <div style="font-size: 8pt; color: #94a3b8; text-transform: uppercase;">Proposta Presentata A:</div>
        <div style="font-size: 10.5pt; font-weight: 800; color: #ffffff;">Direzione Generale — ITALSPORT GROUP</div>
        <div style="font-size: 8pt; color: #64748b;">A cura di: Salvatore & Martina (Consulenza Strategica & Digital Media)</div>
      </div>
      <div style="text-align: right;">
        <div style="font-size: 8pt; color: #94a3b8;">Canale Ufficiale:</div>
        <div style="font-size: 9.5pt; font-weight: 700; color: #34d399;">@italsportgroup • store.italsport-group.it</div>
      </div>
    </div>
  </div>

  <!-- ==================== PAGINA 2: EVOLUZIONE STRATEGICA & TARGET ==================== -->
  <div class="page">
    <div class="page-header">
      <div class="brand">
        <img src="data:image/png;base64,{b64_logo}">
        <span class="doc-title">Analisi di Posizionamento & Strategia 2026</span>
      </div>
      <span class="date-badge">Evoluzione B2B</span>
    </div>

    <div class="page-content">
      <h2 style="font-size: 14pt; margin-bottom: 4px;">1. Il Salto di Qualità: Dalla Vetrina Prodotto al Partner di Riferimento per i Club</h2>
      <p style="font-size: 8.5pt; color: #94a3b8; margin-bottom: 12px;">
        Come valorizzare il patrimonio industriale e tecnologico di Italsport per attrarre presidenti, dirigenti sportivi e comitati organizzatori.
      </p>

      <!-- Confronto Tabellare Feed Oggi vs Domani -->
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 12px;">
        <div class="card" style="margin: 0; background: rgba(148, 163, 184, 0.05); border: 1px solid rgba(148, 163, 184, 0.25);">
          <div style="font-size: 8.5pt; font-weight: 800; color: #cbd5e1; margin-bottom: 6px; display: flex; align-items: center; gap: 6px;">
            <span>📌</span> STATO DELL'ARTE ATTUALE
          </div>
          <ul style="margin: 0; padding-left: 16px; font-size: 8pt; color: #94a3b8; line-height: 1.45;">
            <li>Comunicazione incentrata su singoli prodotti promozionali e fornitura standard.</li>
            <li>Immagini statiche di prodotto senza una narrazione coordinata dell'identità societaria.</li>
            <li>Potenziale del Configuratore 3D non ancora espresso attraverso contenuti video dinamici.</li>
            <li>Servizi esclusivi per club (Tessera Fedeltà, My Italsport) poco visibili al target B2B.</li>
            <li>Interazione limitata con i presidenti e gli allenatori del territorio lombardo e nazionale.</li>
          </ul>
        </div>

        <div class="card" style="margin: 0; background: rgba(16, 185, 129, 0.05); border: 1px solid rgba(16, 185, 129, 0.25);">
          <div style="font-size: 8.5pt; font-weight: 800; color: #34d399; margin-bottom: 6px; display: flex; align-items: center; gap: 6px;">
            <span>🚀</span> LA NUOVA IDENTITÀ DIGITALE ITALSPORT
          </div>
          <ul style="margin: 0; padding-left: 16px; font-size: 8pt; color: #cbd5e1; line-height: 1.45;">
            <li>Fotografia sportiva reale ed emozionale: <strong>divise da gara complete, dettagli tecnici e spogliatoi</strong>.</li>
            <li><strong>Reel dinamici del Configuratore 3D</strong> con simulazione d'uso reale e rotazione a 360°.</li>
            <li>Lancio e promozione della <strong>Tessera Fedeltà Pro-Club</strong> con vantaggi riservati alle ASD.</li>
            <li>Rassicurazione sulla <strong>continuità nel tempo</strong>: archivio storico e riassortimenti garantiti.</li>
            <li>Presentazione del portale <strong>My Italsport</strong> come soluzione che azzera il caos in segreteria.</li>
          </ul>
        </div>
      </div>

      <!-- Tabella Target e Numeri al 31 Dicembre -->
      <div style="font-size: 9.5pt; font-weight: 800; color: #ffffff; margin-bottom: 6px; display: flex; align-items: center; justify-content: space-between;">
        <span>🎯 METRICHE DI PERFORMANCE CONDIVISE (TARGET BIMESTRE NOVEMBRE – DICEMBRE 2026)</span>
        <span style="font-size: 8pt; color: #34d399; font-weight: 600;">Fase Pilota: 9 Settimane</span>
      </div>

      <table class="table-custom">
        <thead>
          <tr>
            <th style="width: 28%;">Metrica / Obiettivo</th>
            <th style="width: 18%;">Target Prudenziale</th>
            <th style="width: 24%;">Metodo di Rilevazione</th>
            <th style="width: 30%;">Valore Strategico per Italsport</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Adesioni Tessera Pro-Club</strong></td>
            <td><span class="badge badge-gold">5 – 8 Società</span></td>
            <td>Registrazioni store.italsport-group.it</td>
            <td>Fidelizza le società sportive per più stagioni azzerando il rischio di cambi fornitore.</td>
          </tr>
          <tr>
            <td><strong>Progetti sul Configuratore 3D</strong></td>
            <td><span class="badge badge-blue">40 – 50 Kit Salvati</span></td>
            <td>Tracking analytics del tool 3D</td>
            <td>Genera contatti commerciali profilati con colori e bozze societarie già pronte.</td>
          </tr>
          <tr>
            <td><strong>Richieste Campionari</strong></td>
            <td><span class="badge badge-emerald">5 – 8 ASD / Club</span></td>
            <td>Messaggi Direct e WhatsApp</td>
            <td>Tasso di conversione stimato prudenzialmente al 15% – 20% sul campionario inviato.</td>
          </tr>
          <tr>
            <td><strong>Riattivazione Clienti CRM</strong></td>
            <td><span class="badge badge-purple">10 – 15 Club Riattivati</span></td>
            <td>Incrocio con anagrafiche CRM</td>
            <td>Riporta in attività società dormienti del database storico tramite le convenzioni Pro-Club.</td>
          </tr>
          <tr>
            <td><strong>Nuove Forniture Club Chiuse</strong></td>
            <td><span class="badge badge-emerald">1 – 2 Forniture Complete</span></td>
            <td>Ordini registrati a gestionale</td>
            <td>Fatturato stimato: € 3.500 – € 6.500 nel primo ciclo pilota, a copertura immediata dei costi.</td>
          </tr>
        </tbody>
      </table>

      <!-- Calendario Uscite -->
      <div style="font-size: 9.5pt; font-weight: 800; color: #ffffff; margin: 8px 0 6px 0;">
        🗓️ CALENDARIO DELLE USCITE (Timeline 31 Ottobre – 24 Dicembre)
      </div>

      <div style="display: grid; grid-template-columns: repeat(7, 1fr); gap: 6px; text-align: center;">
        <div style="background: rgba(16, 185, 129, 0.15); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 8px; padding: 6px 4px;">
          <div style="font-size: 7.5pt; color: #34d399; font-weight: 800;">31 OTT</div>
          <div style="font-size: 8pt; font-weight: 800; color: #fff; margin: 2px 0;">POST 1</div>
          <div style="font-size: 6.5pt; color: #cbd5e1;">30 Anni di Storia</div>
        </div>
        <div style="background: rgba(56, 189, 248, 0.15); border: 1px solid rgba(56, 189, 248, 0.3); border-radius: 8px; padding: 6px 4px;">
          <div style="font-size: 7.5pt; color: #38bdf8; font-weight: 800;">08 NOV</div>
          <div style="font-size: 8pt; font-weight: 800; color: #fff; margin: 2px 0;">POST 2</div>
          <div style="font-size: 6.5pt; color: #cbd5e1;">Reel 3D Live</div>
        </div>
        <div style="background: rgba(234, 179, 8, 0.15); border: 1px solid rgba(234, 179, 8, 0.3); border-radius: 8px; padding: 6px 4px;">
          <div style="font-size: 7.5pt; color: #fde047; font-weight: 800;">18 NOV</div>
          <div style="font-size: 8pt; font-weight: 800; color: #fff; margin: 2px 0;">POST 3</div>
          <div style="font-size: 6.5pt; color: #cbd5e1;">Tessera Fedeltà</div>
        </div>
        <div style="background: rgba(59, 130, 246, 0.15); border: 1px solid rgba(59, 130, 246, 0.3); border-radius: 8px; padding: 6px 4px;">
          <div style="font-size: 7.5pt; color: #60a5fa; font-weight: 800;">27 NOV</div>
          <div style="font-size: 8pt; font-weight: 800; color: #fff; margin: 2px 0;">POST 4</div>
          <div style="font-size: 6.5pt; color: #cbd5e1;">Riassortimenti</div>
        </div>
        <div style="background: rgba(168, 85, 247, 0.15); border: 1px solid rgba(168, 85, 247, 0.3); border-radius: 8px; padding: 6px 4px;">
          <div style="font-size: 7.5pt; color: #c084fc; font-weight: 800;">06 DIC</div>
          <div style="font-size: 8pt; font-weight: 800; color: #fff; margin: 2px 0;">POST 5</div>
          <div style="font-size: 6.5pt; color: #cbd5e1;">My Italsport</div>
        </div>
        <div style="background: rgba(20, 184, 166, 0.15); border: 1px solid rgba(20, 184, 166, 0.3); border-radius: 8px; padding: 6px 4px;">
          <div style="font-size: 7.5pt; color: #2dd4bf; font-weight: 800;">16 DIC</div>
          <div style="font-size: 8pt; font-weight: 800; color: #fff; margin: 2px 0;">POST 6</div>
          <div style="font-size: 6.5pt; color: #cbd5e1;">Winter Pack</div>
        </div>
        <div style="background: rgba(148, 163, 184, 0.15); border: 1px solid rgba(148, 163, 184, 0.3); border-radius: 8px; padding: 6px 4px;">
          <div style="font-size: 7.5pt; color: #cbd5e1; font-weight: 800;">24 DIC</div>
          <div style="font-size: 8pt; font-weight: 800; color: #fff; margin: 2px 0;">POST 7</div>
          <div style="font-size: 6.5pt; color: #cbd5e1;">Auguri Club</div>
        </div>
      </div>
    </div>

    <div class="page-footer">
      <span class="agency">ITALSPORT GROUP — Piano Strategico Social Media B2B</span>
      <span>Pagina 2 di 10</span>
    </div>
  </div>

  <!-- ==================== PAGINA 3: NUOVA BIO ==================== -->
  <div class="page">
    <div class="page-header">
      <div class="brand">
        <img src="data:image/png;base64,{b64_logo}">
        <span class="doc-title">Assetto Profilo Ufficiale</span>
      </div>
      <span class="date-badge">Bio & Highlights</span>
    </div>

    <div class="page-content">
      <h2 style="font-size: 14pt; margin-bottom: 4px;">2. La Nuova Bio Instagram & Setup del Profilo @italsportgroup</h2>
      <p style="font-size: 8.5pt; color: #94a3b8; margin-bottom: 14px;">
        Ottimizziamo il canale Instagram reale dell'azienda (collegato all'icona sul sito <em>@italsportgroup</em>), rendendolo una calamita di contatti B2B per club e dirigenti.
      </p>

      <div style="display: grid; grid-template-columns: 1fr 1.2fr; gap: 14px; margin-bottom: 14px;">
        <div class="card" style="margin: 0; background: #020617; border: 1px solid #1e293b;">
          <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 10px;">
            <div style="width: 50px; height: 50px; border-radius: 50%; background: #0f172a; border: 2px solid #10b981; padding: 4px; display: flex; align-items: center; justify-content: center;">
              <img src="data:image/png;base64,{b64_logo}" style="width: 100%; object-fit: contain;">
            </div>
            <div>
              <div style="font-size: 10.5pt; font-weight: 800; color: #fff;">@italsportgroup</div>
              <div style="font-size: 7.5pt; color: #34d399; font-weight: 600;">Abbigliamento Sportivo Personalizzato</div>
            </div>
          </div>

          <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.06); border-radius: 8px; padding: 8px 10px; font-size: 8pt; line-height: 1.45; color: #e2e8f0;">
            <strong>ITALSPORT GROUP | Custom Teamwear 🇮🇹</strong><br>
            🏭 Da oltre 30 anni al servizio dello sport, aziende e scuole<br>
            🎨 Crea il kit del tuo club col <strong>CONFIGURATORE 3D</strong><br>
            💳 <strong>Tessera Fedeltà & Programma PRO-CLUB</strong> per società<br>
            📦 Portale MY ITALSPORT: <em>"Tu scegli, al resto pensiamo noi"</em><br>
            📲 Richiedi una convenzione o prova il configuratore 👇<br>
            <span style="color: #38bdf8; font-weight: 600;">🔗 italsport-group.it</span>
          </div>

          <div style="display: flex; gap: 6px; margin-top: 10px;">
            <div style="flex: 1; background: #10b981; color: #fff; font-size: 8pt; font-weight: 700; text-align: center; padding: 6px; border-radius: 6px;">Segui</div>
            <div style="flex: 1; background: #1e293b; color: #cbd5e1; font-size: 8pt; font-weight: 600; text-align: center; padding: 6px; border-radius: 6px;">Messaggio</div>
            <div style="flex: 1; background: #1e293b; color: #cbd5e1; font-size: 8pt; font-weight: 600; text-align: center; padding: 6px; border-radius: 6px;">Convenzioni</div>
          </div>
        </div>

        <div style="display: flex; flex-direction: column; justify-content: space-between;">
          <div class="card" style="margin: 0 0 8px 0; padding: 10px 12px;">
            <div style="font-size: 8.5pt; font-weight: 800; color: #10b981;">PERCHÉ QUESTA BIO FUNZIONA:</div>
            <ul style="margin: 4px 0 0 0; padding-left: 16px; font-size: 8pt; color: #cbd5e1; line-height: 1.4;">
              <li><strong>Fedele al Brand:</strong> Utilizza il motto autentico presente sul sito ufficiale di Italsport.</li>
              <li><strong>Integrazione Tessera Fedeltà:</strong> Valorizza il programma Pro-Club, elemento che incentiva le ASD a contattare l'azienda.</li>
              <li><strong>Zero Sminuimenti:</strong> Comunicazione positiva, autorevole e focalizzata sul servizio e sul sollievo organizzativo dei clienti.</li>
              <li><strong>CTA Chiara:</strong> Invita a richiedere la convenzione o a provare il configuratore interattivo.</li>
            </ul>
          </div>

          <div class="card" style="margin: 0; padding: 10px 12px; background: rgba(56, 189, 248, 0.05); border: 1px solid rgba(56, 189, 248, 0.2);">
            <div style="font-size: 8.5pt; font-weight: 800; color: #38bdf8;">ALBERO DEI LINK (Linktree Italsport Group):</div>
            <div style="font-size: 7.5pt; color: #cbd5e1; margin-top: 4px; line-height: 1.4;">
              1. 💻 <strong>Configuratore 3D Online</strong> (Disegna la maglia in tempo reale)<br>
              2. 💳 <strong>Programma Tessera Fedeltà Pro-Club</strong> (Convenzioni e vantaggi ASD)<br>
              3. 📦 <strong>Portale My Italsport</strong> (Area riservata club affiliati)<br>
              4. 💬 <strong>Contatto Diretto Commerciale</strong> (WhatsApp & Richiesta campionari)
            </div>
          </div>
        </div>
      </div>

      <div style="font-size: 9.5pt; font-weight: 800; color: #ffffff; margin-bottom: 8px;">
        🌟 SET DI 6 STORIE IN EVIDENZA (HIGHLIGHTS PERMANENTI)
      </div>

      <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px;">
        <div class="card" style="margin: 0; padding: 8px 10px;">
          <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 4px;">
            <span style="font-size: 14pt;">🌐</span>
            <div style="font-size: 8.5pt; font-weight: 800; color: #34d399;">3D Config</div>
          </div>
          <p style="font-size: 7.5pt; color: #94a3b8; margin: 0;">Video dimostrativo veloce di come creare e ruotare a 360° una divisa col tool 3D.</p>
        </div>

        <div class="card" style="margin: 0; padding: 8px 10px;">
          <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 4px;">
            <span style="font-size: 14pt;">💳</span>
            <div style="font-size: 8.5pt; font-weight: 800; color: #fde047;">Tessera Club</div>
          </div>
          <p style="font-size: 7.5pt; color: #94a3b8; margin: 0;">Come funziona la Tessera Fedeltà e il Pro-Club: vantaggi e sconti dedicati.</p>
        </div>

        <div class="card" style="margin: 0; padding: 8px 10px;">
          <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 4px;">
            <span style="font-size: 14pt;">🎽</span>
            <div style="font-size: 8.5pt; font-weight: 800; color: #60a5fa;">Kit & Divise</div>
          </div>
          <p style="font-size: 7.5pt; color: #94a3b8; margin: 0;">Gallery fotografica di maglie gara, tute e accessori prodotti per i nostri club.</p>
        </div>

        <div class="card" style="margin: 0; padding: 8px 10px;">
          <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 4px;">
            <span style="font-size: 14pt;">🔄</span>
            <div style="font-size: 8.5pt; font-weight: 800; color: #38bdf8;">Riassortimenti</div>
          </div>
          <p style="font-size: 7.5pt; color: #94a3b8; margin: 0;">La certezza della continuità: la stessa maglia ordinabile anche per i nuovi iscritti.</p>
        </div>

        <div class="card" style="margin: 0; padding: 8px 10px;">
          <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 4px;">
            <span style="font-size: 14pt;">🏭</span>
            <div style="font-size: 8.5pt; font-weight: 800; color: #c084fc;">Produzione</div>
          </div>
          <p style="font-size: 7.5pt; color: #94a3b8; margin: 0;">Le nostre tecniche: Stampa DTF, sublimazione, transfer digitale e ricami interni.</p>
        </div>

        <div class="card" style="margin: 0; padding: 8px 10px;">
          <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 4px;">
            <span style="font-size: 14pt;">📦</span>
            <div style="font-size: 8.5pt; font-weight: 800; color: #34d399;">My Italsport</div>
          </div>
          <p style="font-size: 7.5pt; color: #94a3b8; margin: 0;">L'area riservata online per far ordinare direttamente famiglie e atleti.</p>
        </div>
      </div>
    </div>

    <div class="page-footer">
      <span class="agency">ITALSPORT GROUP — Piano Strategico Social Media B2B</span>
      <span>Pagina 3 di 10</span>
    </div>
  </div>

  <!-- ==================== PAGINA 4: POST 1 ==================== -->
  <div class="page">
    <div class="page-header">
      <div class="brand">
        <img src="data:image/png;base64,{b64_logo}">
        <span class="doc-title">Post 1 • Brand & Identità</span>
      </div>
      <span class="date-badge">Sabato 31 Ottobre</span>
    </div>

    <div class="page-content">
      <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
        <h2 style="font-size: 14pt;">POST 1 — "30 Anni di Passione per lo Sport"</h2>
        <span class="badge badge-emerald">STORIA & QUALITÀ</span>
      </div>
      <p style="font-size: 8.5pt; color: #94a3b8; margin-bottom: 10px;">
        <strong>Obiettivo:</strong> Presentare la solidità e la sartorialità di Italsport con un messaggio autorevole. Far percepire ai club il valore di lavorare con una realtà che da 30 anni veste lo sport italiano.
      </p>

      <div class="post-card">
        <div class="visual-mockup" style="background-image: url('data:image/jpeg;base64,{b64_post1}');">
          <div class="visual-mockup-overlay">
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span class="badge badge-emerald" style="font-size: 6.5pt; background: rgba(0,0,0,0.7); border: 1px solid #10b981;">30 ANNI IN CAMPO</span>
              <span style="font-size: 7pt; color: #34d399; font-weight: 800; text-shadow: 0 1px 3px black;">Slide 1/4</span>
            </div>
            <div>
              <div style="font-size: 6.5pt; font-weight: 800; color: #34d399; text-transform: uppercase; letter-spacing: 0.8px; text-shadow: 0 1px 3px black;">PRODUZIONE SARTORIALE</div>
              <div style="font-size: 10.5pt; font-weight: 900; color: #fff; line-height: 1.15; margin: 2px 0; text-shadow: 0 2px 4px black; text-transform: uppercase;">LA PASSIONE CHE DIVENTA DIVISA</div>
              <div style="width: 25px; height: 2px; background: #10b981; margin: 3px 0;"></div>
              <div style="font-size: 6.5pt; color: #cbd5e1; text-shadow: 0 1px 3px black;">Tu scegli Italsport, al resto pensiamo noi</div>
            </div>
          </div>
        </div>

        <div class="post-details">
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-bottom: 8px;">
            <div style="background: rgba(255,255,255,0.03); padding: 5px 8px; border-radius: 6px; font-size: 7.5pt;">
              <strong style="color: #94a3b8;">Data Uscita:</strong> Sabato 31 Ottobre 2026<br>
              <strong style="color: #94a3b8;">Formato:</strong> Carosello 4 Slide (1080x1350)
            </div>
            <div style="background: rgba(255,255,255,0.03); padding: 5px 8px; border-radius: 6px; font-size: 7.5pt;">
              <strong style="color: #94a3b8;">Canali:</strong> Feed + Sponsorizzata Meta Ads<br>
              <strong style="color: #94a3b8;">Target:</strong> 3–4 Richieste Campionario
            </div>
          </div>

          <div class="caption-box">Dietro ogni divisa che scende in campo la domenica c’è una storia, ci sono i sacrifici di una società e l’orgoglio di un intero territorio. 🇮🇹⚽

Da oltre 30 anni, in Italsport Group mettiamo la nostra esperienza al servizio dello sport, delle scuole e delle aziende.
Non ci limitiamo a fornire abbigliamento: affianchiamo presidenti, dirigenti e atleti per creare un’identità unica e duratura.

Cosa significa scegliere Italsport?
✨ Personalizzazione totale con tecniche all'avanguardia (stampa sublimatica HD, DTF, ricami e transfer)
✨ Tessuti tecnici resistenti, traspiranti ed ergonomici
✨ Un partner affidabile al tuo fianco: dalla bozza grafica alla consegna puntuale dei kit

Il nostro motto è semplice e chiaro: "Tu scegli Italsport, al resto pensiamo noi."

Sei pronto a dare alla tua squadra la divisa che merita?
👉 Contattaci in Direct o visita il nostro sito al link in bio per richiedere un campionario per la tua società!

#italsportgroup #teamwear #abbigliamentosportivo #societasportive #calciodilettanti #basketitalia #volleylife #passionesportiva #madeinitaly</div>
        </div>
      </div>

      <div class="card" style="margin-top: 10px; margin-bottom: 0; background: #0c1322; border-left: 3px solid #10b981;">
        <div style="font-size: 8pt; font-weight: 800; color: #34d399; margin-bottom: 2px;">PERCHÉ QUESTO POST FUNZIONA:</div>
        <div style="font-size: 7.5pt; color: #cbd5e1; line-height: 1.35;">
          La fotografia reale della maglia custom nello spogliatoio trasmette calore e appartenenza. Non parla di prezzi stracciati, ma di dignità e identità sportiva, invitando il presidente a toccare con mano la qualità del tessuto con un campionario gratuito.
        </div>
      </div>
    </div>

    <div class="page-footer">
      <span class="agency">ITALSPORT GROUP — Piano Strategico Social Media B2B</span>
      <span>Pagina 4 di 10</span>
    </div>
  </div>

  <!-- ==================== PAGINA 5: POST 2 ==================== -->
  <div class="page">
    <div class="page-header">
      <div class="brand">
        <img src="data:image/png;base64,{b64_logo}">
        <span class="doc-title">Post 2 • Video Reel 3D</span>
      </div>
      <span class="date-badge">Domenica 08 Novembre</span>
    </div>

    <div class="page-content">
      <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
        <h2 style="font-size: 14pt;">POST 2 — Video Reel: "Il Configuratore 3D in Azione"</h2>
        <span class="badge badge-blue">INNOVAZIONE DIGITALE</span>
      </div>
      <p style="font-size: 8.5pt; color: #94a3b8; margin-bottom: 10px;">
        <strong>Obiettivo:</strong> Un video dinamico (Reel) che mostra a schermo come una società crea la propria divisa personalizzata in tempo reale, ruotandola a 360° prima della produzione.
      </p>

      <div class="post-card">
        <div class="visual-mockup" style="background-image: url('data:image/jpeg;base64,{b64_post2}');">
          <div class="visual-mockup-overlay">
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span class="badge badge-blue" style="font-size: 6.5pt; background: rgba(0,0,0,0.7); border: 1px solid #38bdf8;">REEL VIDEO 3D</span>
              <span style="font-size: 7pt; color: #38bdf8; font-weight: 800; text-shadow: 0 1px 3px black;">30s Live</span>
            </div>
            <div>
              <div style="font-size: 6.5pt; font-weight: 800; color: #38bdf8; text-transform: uppercase; letter-spacing: 0.8px; text-shadow: 0 1px 3px black;">INTERATTIVO A 360°</div>
              <div style="font-size: 10.5pt; font-weight: 900; color: #fff; line-height: 1.15; margin: 2px 0; text-shadow: 0 2px 4px black; text-transform: uppercase;">DISEGNA IL TUO KIT IN 3D</div>
              <div style="width: 25px; height: 2px; background: #38bdf8; margin: 3px 0;"></div>
              <div style="font-size: 6.5pt; color: #cbd5e1; text-shadow: 0 1px 3px black;">Dallo schermo al campo di gioco</div>
            </div>
          </div>
        </div>

        <div class="post-details">
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-bottom: 8px;">
            <div style="background: rgba(255,255,255,0.03); padding: 5px 8px; border-radius: 6px; font-size: 7.5pt;">
              <strong style="color: #94a3b8;">Data Uscita:</strong> Domenica 08 Novembre 2026<br>
              <strong style="color: #94a3b8;">Formato:</strong> Reel Verticale 9:16 (1080x1920)
            </div>
            <div style="background: rgba(255,255,255,0.03); padding: 5px 8px; border-radius: 6px; font-size: 7.5pt;">
              <strong style="color: #94a3b8;">Audio:</strong> Track elettronica moderna ritmata<br>
              <strong style="color: #94a3b8;">Target:</strong> 15–20 Configurazioni salvate
            </div>
          </div>

          <div class="caption-box">Vuoi vedere in anteprima la nuova divisa della tua squadra prima ancora di ordinarla? 🚀

Con il nostro CONFIGURATORE 3D ONLINE è facilissimo:
1️⃣ Scegli il modello che preferisci tra le nostre linee Custom
2️⃣ Seleziona i colori sociali del tuo club in tempo reale con un semplice click
3️⃣ Carica lo stemma societario e i loghi degli sponsor in alta risoluzione
4️⃣ Ruota la divisa a 360° e osserva ogni singolo dettaglio da qualsiasi angolazione

Una volta approvato il design, il nostro reparto produttivo si occupa di tutto: taglio laser, stampa sublimatica ad altissima definizione e confezione sartoriale.

Dalla tua creatività al fischio d'inizio della domenica.

👉 Prova subito a creare la maglia del tuo club: clicca sul link in bio ed entra nel Configuratore 3D!

#configuratore3d #divisesportive #magliapersonalizzata #teamwear #sublimazione #italsportgroup #calciodilettanti #sportcustom #innovazione</div>
        </div>
      </div>

      <div class="card" style="margin-top: 10px; margin-bottom: 0; background: #0c1322; border-left: 3px solid #38bdf8;">
        <div style="font-size: 8pt; font-weight: 800; color: #38bdf8; margin-bottom: 2px;">PERCHÉ QUESTO REEL FUNZIONA:</div>
        <div style="font-size: 7.5pt; color: #cbd5e1; line-height: 1.35;">
          I Reel verticali hanno una copertura organica nettamente superiore su Instagram. Vedere a video la maglia che ruota e cambia colore in tempo reale cattura l'attenzione e dimostra il vantaggio tecnologico di Italsport rispetto ai cataloghi cartacei tradizionali.
        </div>
      </div>
    </div>

    <div class="page-footer">
      <span class="agency">ITALSPORT GROUP — Piano Strategico Social Media B2B</span>
      <span>Pagina 5 di 10</span>
    </div>
  </div>

  <!-- ==================== PAGINA 6: POST 3 ==================== -->
  <div class="page">
    <div class="page-header">
      <div class="brand">
        <img src="data:image/png;base64,{b64_logo}">
        <span class="doc-title">Post 3 • Fidelizzazione</span>
      </div>
      <span class="date-badge">Mercoledì 18 Novembre</span>
    </div>

    <div class="page-content">
      <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
        <h2 style="font-size: 14pt;">POST 3 — "La Tessera Fedeltà & Il Pro-Club"</h2>
        <span class="badge badge-gold">VANTAGGI CLUB</span>
      </div>
      <p style="font-size: 8.5pt; color: #94a3b8; margin-bottom: 10px;">
        <strong>Obiettivo:</strong> Lanciare sui social il programma Pro-Club già presente sullo store di Italsport: sconti dedicati alla società, convenzioni per le famiglie e corsia preferenziale per le forniture.
      </p>

      <div class="post-card">
        <div class="visual-mockup" style="background-image: url('data:image/jpeg;base64,{b64_post3}');">
          <div class="visual-mockup-overlay">
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span class="badge badge-gold" style="font-size: 6.5pt; background: rgba(0,0,0,0.7); border: 1px solid #f59e0b;">PRO-CLUB MEMBER</span>
              <span style="font-size: 7pt; color: #fbbf24; font-weight: 800; text-shadow: 0 1px 3px black;">Fidelity Card</span>
            </div>
            <div>
              <div style="font-size: 6.5pt; font-weight: 800; color: #fbbf24; text-transform: uppercase; letter-spacing: 0.8px; text-shadow: 0 1px 3px black;">VANTAGGI ESCLUSIVI</div>
              <div style="font-size: 10.5pt; font-weight: 900; color: #fff; line-height: 1.15; margin: 2px 0; text-shadow: 0 2px 4px black; text-transform: uppercase;">TESSERA FEDELTÀ SOCIETÀ</div>
              <div style="width: 25px; height: 2px; background: #f59e0b; margin: 3px 0;"></div>
              <div style="font-size: 6.5pt; color: #cbd5e1; text-shadow: 0 1px 3px black;">Convenzioni & Sconti per il tuo club</div>
            </div>
          </div>
        </div>

        <div class="post-details">
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-bottom: 8px;">
            <div style="background: rgba(255,255,255,0.03); padding: 5px 8px; border-radius: 6px; font-size: 7.5pt;">
              <strong style="color: #94a3b8;">Data Uscita:</strong> Mercoledì 18 Novembre 2026<br>
              <strong style="color: #94a3b8;">Formato:</strong> Grafica Card 4:5 (1080x1350)
            </div>
            <div style="background: rgba(255,255,255,0.03); padding: 5px 8px; border-radius: 6px; font-size: 7.5pt;">
              <strong style="color: #94a3b8;">Canali:</strong> Feed + Newsletter CRM per sport<br>
              <strong style="color: #94a3b8;">Target:</strong> 2–3 Nuove Convenzioni Pro-Club
            </div>
          </div>

          <div class="caption-box">Conosci già i vantaggi della nostra TESSERA FEDELTÀ e del programma MY ITALSPORT PRO-CLUB? 💳🏆

Per noi di Italsport un accordo di fornitura non si esaurisce con la consegna delle maglie. È l’inizio di una partnership continuativa pensata per premiare la fedeltà delle società sportive e facilitare la vita a dirigenti e famiglie:

🔹 Listini e sconti dedicati per tutta la stagione sportiva
🔹 Convenzioni speciali estese alle famiglie dei tesserati per l'acquisto del merchandising
🔹 Priorità di produzione e riassortimento veloce sui capi a magazzino
🔹 Accesso all'area riservata online per monitorare ordini, disponibilità e scaricare le fatture

Entrare nella famiglia Italsport come membro Pro-Club significa avere un partner fidato che investe sulla crescita del tuo club, stagione dopo stagione.

👉 Vuoi attivare la Tessera Fedeltà e la convenzione Pro-Club per la tua società?
Scrivici un messaggio in Direct o contattaci all'indirizzo commerciale@italsport-group.it!

#tesserafedelta #proclub #myitalsport #societasportive #convenzionisportive #fidelizzazione #dirigentiasd #teamwear #italsportgroup</div>
        </div>
      </div>

      <div class="card" style="margin-top: 10px; margin-bottom: 0; background: #0c1322; border-left: 3px solid #f59e0b;">
        <div style="font-size: 8pt; font-weight: 800; color: #fbbf24; margin-bottom: 2px;">PERCHÉ QUESTO POST FUNZIONA:</div>
        <div style="font-size: 7.5pt; color: #cbd5e1; line-height: 1.35;">
          Presenta la Tessera Fedeltà non come una trovata promozionale da supermercato, ma come un vero accordo quadro societario B2B. Fa sentire i presidenti parte di un circuito privilegiato e incentiva la fidelizzazione continuativa nel tempo.
        </div>
      </div>
    </div>

    <div class="page-footer">
      <span class="agency">ITALSPORT GROUP — Piano Strategico Social Media B2B</span>
      <span>Pagina 6 di 10</span>
    </div>
  </div>

  <!-- ==================== PAGINA 7: POST 4 ==================== -->
  <div class="page">
    <div class="page-header">
      <div class="brand">
        <img src="data:image/png;base64,{b64_logo}">
        <span class="doc-title">Post 4 • Garanzia Riassortimenti</span>
      </div>
      <span class="date-badge">Venerdì 27 Novembre</span>
    </div>

    <div class="page-content">
      <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
        <h2 style="font-size: 14pt;">POST 4 — "Riassortimenti Sempre Garantiti"</h2>
        <span class="badge badge-blue">SERVIZIO CONTINUO</span>
      </div>
      <p style="font-size: 8.5pt; color: #94a3b8; margin-bottom: 10px;">
        <strong>Obiettivo:</strong> Dare una risposta definitiva all'ansia dei nuovi iscritti di metà stagione: con Italsport ogni matricola è salvata e lo stesso capo rimane ordinabile negli anni.
      </p>

      <div class="post-card">
        <div class="visual-mockup" style="background-image: url('data:image/jpeg;base64,{b64_post4}');">
          <div class="visual-mockup-overlay">
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span class="badge badge-blue" style="font-size: 6.5pt; background: rgba(0,0,0,0.7); border: 1px solid #60a5fa;">ARCHIVIO STORICO</span>
              <span style="font-size: 7pt; color: #60a5fa; font-weight: 800; text-shadow: 0 1px 3px black;">Continuità</span>
            </div>
            <div>
              <div style="font-size: 6.5pt; font-weight: 800; color: #60a5fa; text-transform: uppercase; letter-spacing: 0.8px; text-shadow: 0 1px 3px black;">ZERO FUORI SERIE</div>
              <div style="font-size: 10.5pt; font-weight: 900; color: #fff; line-height: 1.15; margin: 2px 0; text-shadow: 0 2px 4px black; text-transform: uppercase;">RIASSORTIMENTI GARANTITI</div>
              <div style="width: 25px; height: 2px; background: #60a5fa; margin: 3px 0;"></div>
              <div style="font-size: 6.5pt; color: #cbd5e1; text-shadow: 0 1px 3px black;">Stessa divisa negli anni per i nuovi iscritti</div>
            </div>
          </div>
        </div>

        <div class="post-details">
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-bottom: 8px;">
            <div style="background: rgba(255,255,255,0.03); padding: 5px 8px; border-radius: 6px; font-size: 7.5pt;">
              <strong style="color: #94a3b8;">Data Uscita:</strong> Venerdì 27 Novembre 2026<br>
              <strong style="color: #94a3b8;">Formato:</strong> Carosello Informativo 4 Slide (1080x1350)
            </div>
            <div style="background: rgba(255,255,255,0.03); padding: 5px 8px; border-radius: 6px; font-size: 7.5pt;">
              <strong style="color: #94a3b8;">Target:</strong> Segretari di Società e Allenatori<br>
              <strong style="color: #94a3b8;">Target:</strong> 2–3 Richieste Riassortimento
            </div>
          </div>

          <div class="caption-box">Cosa succede quando a metà stagione o all'inizio del nuovo anno arrivano nuovi iscritti nella tua società sportiva? 👦👧⚽

Con Italsport la risposta è semplice: riceveranno esattamente la stessa identica divisa dei compagni di squadra.

Grazie alla nostra produzione interna e a oltre 30 anni di archivio storico:
✅ Memorizziamo i codici tessuto, i pantoni colore e i file vettoriali di ogni singolo club
✅ Possiamo riprodurre anche piccoli quantitativi di riassortimento senza costringervi a cambiare modello
✅ Nessun rischio di dover rifare le divise da zero ogni anno, tutelando il budget della società e delle famiglie

La tranquillità di una gestione sportiva serena comincia dalla scelta di un partner che vi garantisce continuità nel tempo.

👉 Vuoi pianificare la fornitura della tua società con la certezza dei riassortimenti? Parla con un nostro consulente al link in bio!

#continuità #riassortimento #societasportive #calciogiovanile #basketgiovanile #pallavoloitaliana #teamwearitaly #italsportgroup #affidabilita</div>
        </div>
      </div>

      <div class="card" style="margin-top: 10px; margin-bottom: 0; background: #0c1322; border-left: 3px solid #60a5fa;">
        <div style="font-size: 8pt; font-weight: 800; color: #60a5fa; margin-bottom: 2px;">PERCHÉ QUESTO POST FUNZIONA:</div>
        <div style="font-size: 7.5pt; color: #cbd5e1; line-height: 1.35;">
          Tocca il punto più doloroso per chi gestisce le divise nelle società sportive: il timore che il grande marchio multinazionale mandi il modello "fuori catalogo" dopo 12 mesi. Qui Italsport si posiziona come la garanzia che difende il portafoglio delle famiglie.
        </div>
      </div>
    </div>

    <div class="page-footer">
      <span class="agency">ITALSPORT GROUP — Piano Strategico Social Media B2B</span>
      <span>Pagina 7 di 10</span>
    </div>
  </div>

  <!-- ==================== PAGINA 8: POST 5 ==================== -->
  <div class="page">
    <div class="page-header">
      <div class="brand">
        <img src="data:image/png;base64,{b64_logo}">
        <span class="doc-title">Post 5 • Portale Società</span>
      </div>
      <span class="date-badge">Domenica 06 Dicembre</span>
    </div>

    <div class="page-content">
      <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
        <h2 style="font-size: 14pt;">POST 5 — "Il Portale My Italsport"</h2>
        <span class="badge badge-purple">GESTIONE DIGITALE</span>
      </div>
      <p style="font-size: 8.5pt; color: #94a3b8; margin-bottom: 10px;">
        <strong>Obiettivo:</strong> Presentare la vetrina e-commerce riservata per ciascuna squadra, dove le famiglie e gli atleti ordinano direttamente online senza gravare sulla segreteria del club.
      </p>

      <div class="post-card">
        <div class="visual-mockup" style="background-image: url('data:image/jpeg;base64,{b64_post5}');">
          <div class="visual-mockup-overlay">
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span class="badge badge-purple" style="font-size: 6.5pt; background: rgba(0,0,0,0.7); border: 1px solid #c084fc;">PORTALE DIGITALE</span>
              <span style="font-size: 7pt; color: #c084fc; font-weight: 800; text-shadow: 0 1px 3px black;">My Italsport</span>
            </div>
            <div>
              <div style="font-size: 6.5pt; font-weight: 800; color: #c084fc; text-transform: uppercase; letter-spacing: 0.8px; text-shadow: 0 1px 3px black;">LOGISTICA SEMPLIFICATA</div>
              <div style="font-size: 10.5pt; font-weight: 900; color: #fff; line-height: 1.15; margin: 2px 0; text-shadow: 0 2px 4px black; text-transform: uppercase;">PORTALE MY ITALSPORT</div>
              <div style="width: 25px; height: 2px; background: #c084fc; margin: 3px 0;"></div>
              <div style="font-size: 6.5pt; color: #cbd5e1; text-shadow: 0 1px 3px black;">La vetrina online dedicata al tuo club</div>
            </div>
          </div>
        </div>

        <div class="post-details">
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-bottom: 8px;">
            <div style="background: rgba(255,255,255,0.03); padding: 5px 8px; border-radius: 6px; font-size: 7.5pt;">
              <strong style="color: #94a3b8;">Data Uscita:</strong> Domenica 06 Dicembre 2026<br>
              <strong style="color: #94a3b8;">Formato:</strong> Grafica Infografica 4:5 (1080x1350)
            </div>
            <div style="background: rgba(255,255,255,0.03); padding: 5px 8px; border-radius: 6px; font-size: 7.5pt;">
              <strong style="color: #94a3b8;">Target:</strong> Presidenti e Responsabili Logistica ASD<br>
              <strong style="color: #94a3b8;">Target:</strong> 2–3 Richieste Attivazione Portale
            </div>
          </div>

          <div class="caption-box">Magazzini improvvisati, ordini disorganizzati e corse contro il tempo per raccogliere le taglie: sappiamo quanto possa essere impegnativa la gestione logistica di una società sportiva. 📦⏱️

Proprio ascoltando le esigenze reali di dirigenti e atleti è nato il progetto MY ITALSPORT.

Come funziona il servizio?
1️⃣ Creiamo uno spazio web riservato ed esclusivo per la tua società
2️⃣ I membri e le famiglie accedono con le proprie credenziali e ordinano direttamente online il kit ufficiale approvato
3️⃣ Visualizzi lo stato d'avanzamento, gestisci i documenti e scarichi le fatture direttamente da una dashboard intuitiva
4️⃣ La merce viene imballata ed etichettata con precisione, pronta per la consegna

Con My Italsport rivoluzioni la gestione del tuo materiale sportivo e risparmi tempo prezioso da dedicare al campo.

👉 Vuoi scoprire come attivare la piattaforma per il tuo club? Contattaci per una dimostrazione gratuita: commerciale@italsport-group.it!

#myitalsport #logisticasportiva #organizzazionesportiva #societasportive #gestioneatleti #abbigliamentosportivo #italsportgroup #soluzionidigitali</div>
        </div>
      </div>

      <div class="card" style="margin-top: 10px; margin-bottom: 0; background: #0c1322; border-left: 3px solid #c084fc;">
        <div style="font-size: 8pt; font-weight: 800; color: #c084fc; margin-bottom: 2px;">PERCHÉ QUESTO POST FUNZIONA:</div>
        <div style="font-size: 7.5pt; color: #cbd5e1; line-height: 1.35;">
          Dimostra la modernità organizzativa di Italsport Group. Non solo fabbrica tessile, ma vero fornitore logistico evoluto: le società non devono fare magazzino né raccogliere i contanti delle famiglie, pensa a tutto la piattaforma web.
        </div>
      </div>
    </div>

    <div class="page-footer">
      <span class="agency">ITALSPORT GROUP — Piano Strategico Social Media B2B</span>
      <span>Pagina 8 di 10</span>
    </div>
  </div>

  <!-- ==================== PAGINA 9: POST 6 & 7 ==================== -->
  <div class="page">
    <div class="page-header">
      <div class="brand">
        <img src="data:image/png;base64,{b64_logo}">
        <span class="doc-title">Post 6 & 7 • Fine Anno</span>
      </div>
      <span class="date-badge">16 & 24 Dicembre</span>
    </div>

    <div class="page-content">
      <h2 style="font-size: 14pt; margin-bottom: 2px;">POST 6 & 7 — Winter Training & Auguri di Fine Anno</h2>
      <p style="font-size: 8.5pt; color: #94a3b8; margin-bottom: 8px;">
        La chiusura della campagna promuove l'abbigliamento tecnico invernale per gli allenamenti all'aperto e consolida il legame umano con la comunità sportiva.
      </p>

      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; flex: 1;">
        
        <div class="card" style="margin: 0; display: flex; flex-direction: column; justify-content: space-between; background: #0c1524; border: 1px solid rgba(20, 184, 166, 0.3);">
          <div>
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
              <span class="badge badge-emerald" style="font-size: 6.5pt;">POST 6 • 16 DICEMBRE</span>
              <span style="font-size: 7pt; color: #2dd4bf; font-weight: 700;">Winter 2026/27</span>
            </div>
            
            <div style="width: 100%; height: 38mm; border-radius: 8px; background-image: url('data:image/jpeg;base64,{b64_post6}'); background-size: cover; background-position: center; position: relative; overflow: hidden;">
              <div style="position: absolute; bottom: 0; inset-x: 0; background: linear-gradient(0deg, rgba(0,0,0,0.85) 0%, transparent 100%); padding: 6px;">
                <div style="font-size: 8pt; font-weight: 900; color: #fff; text-transform: uppercase;">WINTER TRAINING: NON FERMARTI</div>
              </div>
            </div>

            <div class="caption-box" style="height: 115px; font-size: 6.8pt; line-height: 1.35;">Freddo, pioggia o vento: la vera passione per lo sport non si ferma davanti all'inverno. ❄️🏃‍♂️

Per accompagnare gli atleti negli allenamenti e nelle sfide più impegnative, abbiamo selezionato e personalizzato i migliori capi tecnici invernali:
🧥 Giacconi termici idrorepellenti imbottiti per dirigenti e panchina
🌧️ K-way traspiranti e giubbini antivento con vestibilità ergonomica
👖 Pantaloni d'allenamento tecnici con zip e fasce elasticizzate
🧣 Accessori coordinati con i colori sociali (scaldacollo, guanti)

Proteggi i tuoi atleti e mantieni alto il calore della tua squadra!

#wintertraining #abbigliamentoinvernale #calciotrain #tutesportive #termiche #asdsport #italsportgroup</div>
          </div>
          <div style="font-size: 7pt; color: #34d399; font-weight: 700; border-top: 1px solid rgba(255,255,255,0.08); padding-top: 4px; margin-top: 4px;">
            Target: 3–4 Richieste Fornitura Invernale
          </div>
        </div>

        <div class="card" style="margin: 0; display: flex; flex-direction: column; justify-content: space-between; background: #0c1524; border: 1px solid rgba(148, 163, 184, 0.3);">
          <div>
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
              <span class="badge" style="background: rgba(148, 163, 184, 0.2); color: #cbd5e1; font-size: 6.5pt;">POST 7 • 24 DICEMBRE</span>
              <span style="font-size: 7pt; color: #cbd5e1; font-weight: 700;">Chiusura 2026</span>
            </div>

            <div style="width: 100%; height: 38mm; border-radius: 8px; background-image: url('data:image/jpeg;base64,{b64_post7}'); background-size: cover; background-position: center; position: relative; overflow: hidden;">
              <div style="position: absolute; bottom: 0; inset-x: 0; background: linear-gradient(0deg, rgba(0,0,0,0.85) 0%, transparent 100%); padding: 6px;">
                <div style="font-size: 8pt; font-weight: 900; color: #fff; text-transform: uppercase;">GRAZIE A CHI FA VIVERE LO SPORT</div>
              </div>
            </div>

            <div class="caption-box" style="height: 115px; font-size: 6.8pt; line-height: 1.35;">Mentre il 2026 si avvia al termine, desideriamo rivolgere un pensiero speciale a tutti coloro che, giorno dopo giorno, rendono vivo lo sport nei nostri paesi e città. 🏆❤️

Grazie ai presidenti e ai dirigenti per la dedizione instancabile.
Grazie agli allenatori e ai preparatori per la passione che trasmettono ai giovani.
Grazie alle famiglie e a tutti gli atleti che scendono in campo con rispetto ed entusiasmo.

È un onore per Italsport vestire i vostri colori e condividere con voi ogni traguardo.

Da tutta la nostra squadra, i più calorosi auguri di buone feste e un 2027 ricco di vittorie e soddisfazioni!

#buonefeste #natale2026 #famigliasportiva #societasportive #valorisportivi #auguri #italsportgroup</div>
          </div>
          <div style="font-size: 7pt; color: #38bdf8; font-weight: 700; border-top: 1px solid rgba(255,255,255,0.08); padding-top: 4px; margin-top: 4px;">
            Target: Consolidamento Community & Fidelizzazione Territorio
          </div>
        </div>

      </div>

      <div class="card" style="margin-top: 8px; margin-bottom: 0; background: #020617; border: 1px solid #10b981;">
        <div style="display: flex; justify-content: space-between; align-items: center;">
          <div>
            <div style="font-size: 8.5pt; font-weight: 800; color: #34d399;">31 DICEMBRE 2026: REPORT CONSUNTIVO DELLE PERFORMANCE</div>
            <div style="font-size: 7.5pt; color: #cbd5e1;">A fine anno analizzeremo insieme i risultati: visite al configuratore 3D, campionari inviati, adesioni Pro-Club e contratti attivati.</div>
          </div>
          <div style="text-align: right;">
            <span class="badge badge-emerald" style="font-size: 8pt;">REPORT FINALE INCLUSO</span>
          </div>
        </div>
      </div>
    </div>

    <div class="page-footer">
      <span class="agency">ITALSPORT GROUP — Piano Strategico Social Media B2B</span>
      <span>Pagina 9 di 10</span>
    </div>
  </div>

  <!-- ==================== PAGINA 10: PREVENTIVO E CONDIZIONI CHIARE ==================== -->
  <div class="page">
    <div class="page-header">
      <div class="brand">
        <img src="data:image/png;base64,{b64_logo}">
        <span class="doc-title">Proposta Economica Esecutiva</span>
      </div>
      <span class="date-badge">Formula Prezzo Chiuso</span>
    </div>

    <div class="page-content">
      <h2 style="font-size: 14pt; margin-bottom: 4px;">3. Proposta Economica a Prezzo Chiuso (Zero Costi Orari)</h2>
      <p style="font-size: 8.5pt; color: #94a3b8; margin-bottom: 12px;">
        Un capitolato di fornitura trasparente e senza sorprese per il bimestre Novembre – Dicembre 2026, a costo fisso garantito.
      </p>

      <table class="table-custom" style="margin-bottom: 12px;">
        <thead>
          <tr>
            <th style="width: 26%;">Ambito di Intervento</th>
            <th style="width: 44%;">Deliverable & Servizi Inclusi</th>
            <th style="width: 30%;">Valore Operativo per Italsport</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Direzione Creativa & Visual Design</strong></td>
            <td>7 format fotografici e grafici in alta risoluzione (caroselli, infografiche, card fedeltà) e set di 6 copertine per Storie in Evidenza.</td>
            <td>Immagine di marca prestigiosa e coordinata che valorizza la manifattura reale dell'azienda.</td>
          </tr>
          <tr>
            <td><strong>Produzione Reel & Simulatore 3D</strong></td>
            <td>Video verticale dinamico (9:16) con navigazione del Configuratore 3D, animazione rotazione a 360°, testi sovrimpressi e audio in licenza.</td>
            <td>Dimostrazione concreta del vantaggio tecnologico di Italsport rispetto ai concorrenti tradizionali.</td>
          </tr>
          <tr>
            <td><strong>Copywriting & Strategia Editoriale</strong></td>
            <td>Stesura professionale di tutti i testi con tono di voce autorevole e costruttivo, piano hashtag mirati e ottimizzazione bio.</td>
            <td>Messaggi chiari che convertono le visite in richieste di campionario e contatti commerciali.</td>
          </tr>
          <tr>
            <td><strong>Campagne Sponsorizzate Meta Ads</strong></td>
            <td>Configurazione inserzioni, targettizzazione geografica su presidenti/dirigenti di club sportivi, tracciamento link e monitoraggio conversioni.</td>
            <td>Intercettazione qualificata dei decisori d'acquisto sportivi senza dispersione di budget.</td>
          </tr>
          <tr>
            <td><strong>Integrazione Liste CRM (4.600 Club)</strong></td>
            <td>Sinergia tra uscite social e database aziendale per la promozione mirata della convenzione Pro-Club.</td>
            <td>Riattivazione di società dormienti e fidelizzazione dei clienti storici per le prossime stagioni.</td>
          </tr>
          <tr>
            <td><strong>Report Consuntivo al 31 Dicembre</strong></td>
            <td>Documento di sintesi dettagliato con analisi delle metriche, progetti 3D salvati e richieste di fornitura generate.</td>
            <td>Valutazione oggettiva dei risultati per pianificare con anticipo la strategia annuale 2027.</td>
          </tr>
        </tbody>
      </table>

      <div style="display: grid; grid-template-columns: 1.2fr 1fr; gap: 12px; margin-bottom: 12px;">
        <div class="card" style="margin: 0; background: #0c1829; border: 1px solid #10b981;">
          <div style="font-size: 8.5pt; font-weight: 800; color: #34d399; text-transform: uppercase;">COMPENSO PROFESSIONALE FISSO BIMESTRALE</div>
          <div style="font-size: 20pt; font-weight: 900; color: #fff; margin: 4px 0;">
            € 450,00 <span style="font-size: 11pt; font-weight: 600; color: #94a3b8;">/ mese</span>
          </div>
          <div style="font-size: 7.8pt; color: #cbd5e1; line-height: 1.4;">
            Totale bimestre (Novembre – Dicembre 2026): <strong>€ 900,00 + IVA</strong>.<br>
            <strong>Formula a Prezzo Chiuso:</strong> nessun conteggio a tariffa oraria (60 €/ora), nessun extra per revisioni. Comprende tutti i 7 post, montaggio Reel 3D, setup ads e report finale.
          </div>
        </div>

        <div class="card" style="margin: 0; background: #0c1829; border: 1px solid #38bdf8;">
          <div style="font-size: 8.5pt; font-weight: 800; color: #38bdf8; text-transform: uppercase;">BUDGET SPONSORIZZATE CONSIGLIATO</div>
          <div style="font-size: 20pt; font-weight: 900; color: #fff; margin: 4px 0;">
            € 150,00 <span style="font-size: 11pt; font-weight: 600; color: #94a3b8;">/ mese</span>
          </div>
          <div style="font-size: 7.8pt; color: #cbd5e1; line-height: 1.4;">
            Totale bimestre ads: <strong>€ 300,00</strong>.<br>
            Fatturato direttamente da Meta a Italsport Group con carta aziendale. Destinato specificamente alla diffusione del Reel 3D e della Tessera Pro-Club.
          </div>
        </div>
      </div>

      <div class="card" style="margin: 0; background: #020617; border-left: 4px solid #10b981;">
        <div style="font-size: 8.5pt; font-weight: 800; color: #ffffff; margin-bottom: 4px;">
          🚀 PROSSIMI PASSI OPERATIVI PER L'AVVIO:
        </div>
        <div style="font-size: 8pt; color: #cbd5e1; line-height: 1.45;">
          1. <strong>Conferma della proposta</strong> e condivisione accessi tecnici al profilo @italsportgroup.<br>
          2. <strong>Applicazione immediata della nuova Bio</strong> e pubblicazione delle 6 Storie in Evidenza coordinate.<br>
          3. <strong>Pubblicazione Post 1 (30 Anni di Storia)</strong> per inaugurare la campagna ufficiale del brand.<br>
          4. <strong>Lancio e sponsorizzazione mirata del Reel Video</strong> sul Configuratore 3D.
        </div>
      </div>
    </div>

    <div class="page-footer">
      <span class="agency">ITALSPORT GROUP — Piano Strategico Social Media B2B</span>
      <span>Pagina 10 di 10</span>
    </div>
  </div>

</body>
</html>
'''

with open('full_pdf_template.html', 'w', encoding='utf-8') as f:
    f.write(html_pdf)

print("Saved full_pdf_template.html successfully.")

# ========================================================
# 4. RENDERIZZAZIONE DEL PDF CON GOOGLE CHROME HEADLESS
# ========================================================
chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
html_path = os.path.abspath('full_pdf_template.html')
pdf_path = os.path.abspath('Piano_Social_Italsport_2026.pdf')

cmd = [
    chrome, '--headless', '--disable-gpu', '--no-sandbox', '--no-pdf-header-footer',
    f'--print-to-pdf={pdf_path}', f'file:///{html_path}'
]
res = subprocess.run(cmd, capture_output=True, text=True)

import fitz
doc = fitz.open(pdf_path)
page_count = len(doc)
doc.close()
file_size = os.path.getsize(pdf_path)

print(f"PDF GENERATED SUCCESSFULLY! Pages: {page_count}, Size: {file_size} bytes")

# Copia nell'artifact directory
artifact_dir = r'C:\Users\salvo\.gemini\antigravity\brain\dc9abd1d-f990-4c44-a20b-bd6ec7f9af7d'
if os.path.exists(artifact_dir):
    dest_pdf = os.path.join(artifact_dir, 'Piano_Social_Italsport_2026.pdf')
    shutil.copyfile(pdf_path, dest_pdf)
    print(f"Copied PDF to artifact directory: {dest_pdf}")

print("Build Complete!")
