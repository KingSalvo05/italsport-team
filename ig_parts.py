# Parti Instagram realistiche per Instagram_Mockup_Italsport.html — ITALSPORT GROUP Ciserano (BG)
# Stringhe normali (non f-string): i token __XXX__ vengono sostituiti in build_interactive_mockup.py

IG_CSS = r"""
/* ===================== INSTAGRAM REALISTICO ===================== */
.ig-shell{max-width:935px;margin:0 auto;background:#fff;border:1px solid #dbdbdb;border-radius:12px;padding:30px 20px 0;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;color:#000}
.ig-profile{display:flex;gap:80px;align-items:flex-start;padding:0 40px 40px}
.ig-avatar-wrap{cursor:pointer;flex-shrink:0}
.ig-ring{width:168px;height:168px;border-radius:50%;padding:4px;background:conic-gradient(from 210deg,#feda75,#fa7e1e,#d62976,#962fbf,#4f5bd5,#feda75)}
.ig-ring.seen{background:#dbdbdb}
.ig-avatar{width:100%;height:100%;border-radius:50%;background:#fff;border:4px solid #fff;display:flex;align-items:center;justify-content:center;overflow:hidden}
.ig-avatar img{width:86%;object-fit:contain}
.ig-info{flex:1;min-width:0}
.ig-row1{display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin-bottom:20px}
.ig-username{font-size:20px;font-weight:400;margin-right:12px;display:flex;align-items:center;gap:6px}
.ig-btn{border:none;border-radius:8px;padding:7px 16px;font-weight:600;font-size:14px;cursor:pointer;background:#efefef;color:#000;font-family:inherit}
.ig-btn:hover{background:#dbdbdb}
.ig-btn-primary{background:#0095f6;color:#fff}
.ig-btn-primary:hover{background:#1877f2}
.ig-stats{display:flex;gap:40px;list-style:none;margin:0 0 20px;padding:0;font-size:16px}
.ig-stats b{font-weight:600}
.ig-bio{font-size:14px;line-height:1.45}
.ig-bio .ig-name{font-weight:600}
.ig-bio .ig-cat{color:#737373}
.ig-bio a{color:#00376b;font-weight:600;text-decoration:none}
.ig-followedby{font-size:12px;color:#737373;margin-top:8px}
.ig-followedby b{color:#000;font-weight:600}
.ig-highlights{display:flex;gap:40px;padding:0 40px 44px;overflow-x:auto}
.ig-hl{display:flex;flex-direction:column;align-items:center;gap:8px;cursor:pointer;flex-shrink:0}
.ig-hl-ring{width:87px;height:87px;border-radius:50%;border:1px solid #dbdbdb;padding:3px;background:#fff}
.ig-hl-ring img{width:100%;height:100%;border-radius:50%;object-fit:cover}
.ig-hl span{font-size:12px;font-weight:600;max-width:90px;text-align:center;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.ig-tabs{display:flex;justify-content:center;gap:60px;border-top:1px solid #dbdbdb}
.ig-tab{display:flex;align-items:center;gap:6px;height:52px;font-size:12px;font-weight:600;letter-spacing:1px;color:#737373;cursor:pointer;border-top:1px solid transparent;margin-top:-1px;background:none;border-left:0;border-right:0;border-bottom:0;font-family:inherit}
.ig-tab.active{color:#000;border-top-color:#000}
.ig-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:4px;padding-bottom:4px}
.ig-cell{position:relative;aspect-ratio:1/1;cursor:pointer;overflow:hidden;background:#efefef}
.ig-cell img{width:100%;height:100%;object-fit:cover;display:block}
.ig-cell .ig-ico{position:absolute;top:10px;right:10px;filter:drop-shadow(0 0 2px rgba(0,0,0,.5))}
.ig-cell .ig-hover{position:absolute;inset:0;background:rgba(0,0,0,.3);display:flex;align-items:center;justify-content:center;gap:28px;color:#fff;font-weight:700;font-size:16px;opacity:0;transition:opacity .15s}
.ig-cell:hover .ig-hover{opacity:1}
.ig-hover span{display:flex;align-items:center;gap:7px}
.ig-empty{text-align:center;padding:60px 20px;color:#737373}
.ig-empty h3{color:#000;font-size:24px;font-weight:800;margin:14px 0 6px}
.ig-reels{display:grid;grid-template-columns:repeat(3,1fr);gap:4px;padding-bottom:4px}
.ig-reel{position:relative;aspect-ratio:9/16;background:#000;cursor:pointer;overflow:hidden}
.ig-reel img{width:100%;height:100%;object-fit:cover;opacity:.92}
.ig-reel .ig-reel-info{position:absolute;left:10px;bottom:10px;color:#fff;font-size:13px;font-weight:600;display:flex;gap:6px;align-items:center;text-shadow:0 1px 3px rgba(0,0,0,.6)}
.ig-reel .ig-reel-title{position:absolute;left:10px;right:10px;top:10px;color:#fff;font-size:13px;font-weight:600;text-shadow:0 1px 3px rgba(0,0,0,.7)}

/* Modal post */
.ig-modal{position:fixed;inset:0;background:rgba(0,0,0,.65);z-index:2000;display:none;align-items:center;justify-content:center;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
.ig-modal.open{display:flex}
.ig-close{position:fixed;top:14px;right:22px;background:none;border:none;color:#fff;font-size:34px;cursor:pointer;line-height:1}
.ig-nav{position:fixed;top:50%;transform:translateY(-50%);width:34px;height:34px;border-radius:50%;border:none;background:#fff;color:#000;font-size:22px;cursor:pointer;display:flex;align-items:center;justify-content:center;box-shadow:0 1px 4px rgba(0,0,0,.3)}
.ig-nav.prev{left:24px}.ig-nav.next{right:24px}
.ig-nav[hidden]{display:none}
.ig-dialog{display:flex;background:#fff;max-width:1100px;width:calc(100% - 140px);height:min(86vh,720px);border-radius:4px;overflow:hidden}
.ig-media{flex:0 0 min(720px,60%);background:#000;position:relative;display:flex;align-items:center;justify-content:center;user-select:none}
.ig-media img{max-width:100%;max-height:100%;object-fit:contain}
.ig-slide-btn{position:absolute;bottom:16px;left:16px;background:rgba(15,23,42,.88);color:#fff;border:1px solid rgba(255,255,255,.35);border-radius:20px;padding:7px 14px;font-size:12.5px;font-weight:700;cursor:pointer;box-shadow:0 4px 12px rgba(0,0,0,.35);display:inline-flex;align-items:center;gap:6px;z-index:4}
.ig-slide-btn:hover{background:#0284c7}
.ig-3d-btn{position:absolute;bottom:16px;right:16px;background:rgba(2,132,199,.95);color:#fff;border:none;border-radius:20px;padding:8px 16px;font-size:13px;font-weight:700;cursor:pointer;box-shadow:0 4px 12px rgba(0,0,0,.35);display:none;align-items:center;gap:6px;z-index:4}
.ig-3d-btn:hover{background:#0369a1}
.ig-bigheart{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%) scale(0);opacity:0;pointer-events:none}
.ig-bigheart.pop{animation:igpop .9s ease forwards}
@keyframes igpop{0%{transform:translate(-50%,-50%) scale(0);opacity:0}15%{transform:translate(-50%,-50%) scale(1.2);opacity:.95}30%{transform:translate(-50%,-50%) scale(.95)}45%,80%{transform:translate(-50%,-50%) scale(1);opacity:.95}100%{transform:translate(-50%,-60%) scale(.2);opacity:0}}
.ig-side{flex:1;display:flex;flex-direction:column;min-width:0;border-left:1px solid #efefef}
.ig-side-head{display:flex;align-items:center;gap:12px;padding:14px 16px;border-bottom:1px solid #efefef}
.ig-mini{width:32px;height:32px;border-radius:50%;border:1px solid #dbdbdb;object-fit:contain;background:#fff;padding:2px;flex-shrink:0}
.ig-head-txt{font-size:14px;line-height:1.25}
.ig-head-txt .u{font-weight:600}
.ig-head-txt .loc{font-size:12px;color:#000}
.ig-link-btn{color:#0095f6;font-weight:600;cursor:pointer;background:none;border:none;font-size:14px;padding:0;font-family:inherit}
.ig-link-btn.following{color:#000}
.ig-comments{flex:1;overflow-y:auto;padding:16px}
.ig-c{display:flex;gap:14px;margin-bottom:18px;font-size:14px;line-height:1.4}
.ig-c-av{width:32px;height:32px;border-radius:50%;flex-shrink:0;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:13px}
.ig-c-body{flex:1;min-width:0;word-wrap:break-word}
.ig-c-body .u{font-weight:600;margin-right:4px}
.ig-c-meta{font-size:12px;color:#737373;margin-top:6px;display:flex;gap:12px}
.ig-c-meta button{background:none;border:none;color:#737373;font-weight:600;font-size:12px;cursor:pointer;padding:0;font-family:inherit}
.ig-c-heart{background:none;border:none;cursor:pointer;padding:4px;align-self:center}
.ig-actions{display:flex;align-items:center;padding:6px 10px 0;border-top:1px solid #efefef}
.ig-act{background:none;border:none;cursor:pointer;padding:8px;display:flex;transition:transform .1s}
.ig-act:active{transform:scale(.85)}
.ig-act.beat{animation:igbeat .35s ease}
@keyframes igbeat{0%{transform:scale(1)}40%{transform:scale(1.25)}100%{transform:scale(1)}}
.ig-likes{font-size:14px;font-weight:600;padding:2px 16px}
.ig-date{font-size:10px;color:#737373;letter-spacing:.2px;padding:6px 16px 12px;text-transform:uppercase}
.ig-add{display:flex;align-items:center;gap:12px;border-top:1px solid #efefef;padding:10px 16px}
.ig-add input{flex:1;border:none;outline:none;font-size:14px;font-family:inherit}
.ig-add button{background:none;border:none;color:#0095f6;font-weight:600;font-size:14px;cursor:pointer;font-family:inherit}
.ig-add button:disabled{opacity:.35;cursor:default}

/* Story viewer */
.ig-story{position:fixed;inset:0;background:#1a1a1a;z-index:2100;display:none;align-items:center;justify-content:center;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
.ig-story.open{display:flex}
.ig-story-box{position:relative;width:min(420px,92vw);aspect-ratio:9/16;max-height:92vh;background:#000;border-radius:10px;overflow:hidden;display:flex;align-items:center;justify-content:center}
.ig-story-box img{width:100%;height:100%;object-fit:contain;background:#111}
.ig-story-bars{position:absolute;top:8px;left:8px;right:8px;display:flex;gap:4px;z-index:3}
.ig-story-bars div{flex:1;height:2px;background:rgba(255,255,255,.35);border-radius:2px;overflow:hidden}
.ig-story-bars i{display:block;height:100%;width:0;background:#fff}
.ig-story-head{position:absolute;top:20px;left:12px;right:12px;display:flex;align-items:center;gap:10px;color:#fff;font-size:14px;z-index:3;text-shadow:0 1px 2px rgba(0,0,0,.5)}
.ig-story-head .t{color:rgba(255,255,255,.75)}
.ig-story-head .x{margin-left:auto;background:none;border:none;color:#fff;font-size:28px;cursor:pointer}
.ig-story-cap{position:absolute;left:16px;right:16px;bottom:78px;background:rgba(255,255,255,.94);color:#000;border-radius:10px;padding:10px 14px;font-size:14px;font-weight:600;text-align:center;z-index:3}
.ig-story-tap{position:absolute;top:0;bottom:60px;width:50%;z-index:2;cursor:pointer}
.ig-story-tap.l{left:0}.ig-story-tap.r{right:0}
.ig-story-reply{position:absolute;bottom:14px;left:12px;right:12px;display:flex;gap:12px;align-items:center;z-index:3}
.ig-story-reply input{flex:1;background:transparent;border:1px solid rgba(255,255,255,.7);border-radius:22px;padding:10px 16px;color:#fff;font-size:14px;outline:none;font-family:inherit}
.ig-story-reply input::placeholder{color:rgba(255,255,255,.85)}
.ig-story-reply button{background:none;border:none;cursor:pointer;display:flex}

.ig-toast{position:fixed;left:50%;bottom:30px;transform:translateX(-50%) translateY(20px);background:#262626;color:#fff;padding:12px 20px;border-radius:8px;font-size:14px;opacity:0;transition:all .25s;z-index:3000;pointer-events:none;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}
.ig-toast.show{opacity:1;transform:translateX(-50%) translateY(0)}

@media (max-width:820px){
 .ig-shell{padding:16px 0 0;border-radius:0}
 .ig-profile{gap:24px;padding:0 16px 20px}
 .ig-ring{width:86px;height:86px;padding:3px}
 .ig-stats{gap:18px;font-size:14px}
 .ig-highlights{gap:16px;padding:0 16px 20px}
 .ig-hl-ring{width:64px;height:64px}
 .ig-tabs{gap:30px}
 .ig-dialog{flex-direction:column;width:100%;height:100%;border-radius:0}
 .ig-media{flex:0 0 auto;max-height:50vh}
 .ig-nav{display:none}
}
"""

SVG_HEART = '<svg width="24" height="24" viewBox="0 0 24 24"><path d="M16.79 2.5A5.2 5.2 0 0 0 12 5.44 5.2 5.2 0 0 0 7.21 2.5 5.5 5.5 0 0 0 2 8.24c0 3.97 3.33 6.6 7.26 10.07.77.68 1.6 1.42 2.46 2.2a.42.42 0 0 0 .56 0c.86-.78 1.69-1.52 2.46-2.2C18.67 14.84 22 12.2 22 8.24A5.5 5.5 0 0 0 16.79 2.5Z" fill="none" stroke="#000" stroke-width="2"/></svg>'

IG_TAB = r"""
<div id="tab-feed" class="tab-content active">
  <div class="ig-shell">
    <header class="ig-profile">
      <div class="ig-avatar-wrap" onclick="openStory(0)" title="Guarda le storie">
        <div class="ig-ring" id="igRing"><div class="ig-avatar"><img src="__LOGO__" alt="italsportgroup"></div></div>
      </div>
      <section class="ig-info">
        <div class="ig-row1">
          <h2 class="ig-username">italsportgroup
            <svg width="18" height="18" viewBox="0 0 40 40"><path fill="#0095f6" d="M19.998 3.094 14.638 0l-2.972 5.15H5.432v6.354L0 14.64 3.094 20 0 25.359l5.432 3.137v5.905h5.975L14.638 40l5.36-3.094L25.358 40l3.232-5.6h6.162v-6.01L40 25.359 36.905 20 40 14.641l-5.248-3.03v-6.46h-6.419L25.358 0l-5.36 3.094Zm7.415 11.225 2.254 2.287-11.43 11.5-6.835-6.93 2.244-2.258 4.587 4.581 9.18-9.18Z"/></svg>
          </h2>
          <button class="ig-btn ig-btn-primary" id="followBtn" onclick="toggleFollow()">Segui</button>
          <button class="ig-btn" onclick="toast('I messaggi diretti si aprono nell\'app Instagram')">Messaggio</button>
          <button class="ig-btn" onclick="toast('Link del profilo copiato'); copyLink('')">Condividi profilo</button>
        </div>
        <ul class="ig-stats">
          <li><b>7</b> post</li>
          <li><b id="statFollowers">2.840</b> follower</li>
          <li><b>312</b> profili seguiti</li>
        </ul>
        <div class="ig-bio">
          <div class="ig-name">Italsport Group • Ciserano — Zingonia (BG)</div>
          <div class="ig-cat">Forniture Sportive, Stampa DTF, Sublimazione & Personalizzazioni • Dal 1995</div>
          <div>👕 <i>"Tu scegli Italsport, al resto pensiamo noi."</i></div>
          <div>🎨 Stampa DTF ad alta definizione, Sublimatica 100% traspirante, Full Print & Sartoria interna</div>
          <div>🔄 Simulatore 3D a 360° • 🔒 Vetrina My Italsport dedicata alla squadra con password</div>
          <div>🪪 Tessera PRO-CLUB (Basic, Silver, Gold, Diamond) • Il magazzino a Ciserano lo facciamo noi</div>
          <div>📍 Showroom: Via Provinciale Francesca 2H/I, 24040 Ciserano (BG) • ☎️ 035 4191221</div>
          <a href="https://store.italsport-group.it/it/" target="_blank">🔗 store.italsport-group.it • italsport-group.it</a>
        </div>
        <div class="ig-followedby">Seguito da <b>usd_brevianese</b>, <b>asd_gessate</b> e oltre 4.600 realtà sportive del territorio</div>
      </section>
    </header>

    <div class="ig-highlights" id="igHighlights"></div>

    <div class="ig-tabs">
      <button class="ig-tab active" data-tab="post" onclick="igTab('post')"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18"/><path d="M9 3v18M15 3v18M3 9h18M3 15h18"/></svg> POST</button>
      <button class="ig-tab" data-tab="reel" onclick="igTab('reel')"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5"/><path d="M2 8h20M8 2l3 6M14 2l3 6"/><path d="M10 12v6l5-3z" fill="currentColor"/></svg> REEL</button>
      <button class="ig-tab" data-tab="saved" onclick="igTab('saved')"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21 12 13.44 4 21V3h16z"/></svg> SALVATI</button>
      <button class="ig-tab" data-tab="tagged" onclick="igTab('tagged')"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10 18H5a3 3 0 0 1-3-3V5a3 3 0 0 1 3-3h14a3 3 0 0 1 3 3v10a3 3 0 0 1-3 3h-5l-2 3z"/><circle cx="12" cy="9" r="3"/></svg> TAG</button>
    </div>
    <div id="igPane"></div>
  </div>
</div>
"""

IG_MODAL = r"""
<div class="ig-modal" id="igModal" onclick="if(event.target===this)closeIg()">
  <button class="ig-close" onclick="closeIg()" aria-label="Chiudi">&times;</button>
  <button class="ig-nav prev" id="igPrev" onclick="navIg(-1)">&#8249;</button>
  <button class="ig-nav next" id="igNext" onclick="navIg(1)">&#8250;</button>
  <div class="ig-dialog">
    <div class="ig-media" ondblclick="dblLike()">
      <img id="igImg" src="" alt="post">
      <button class="ig-slide-btn" id="igSlideToggle" onclick="toggleModalSlide(event)">▶️ Vedi Slide 2 (2/2)</button>
      <button class="ig-3d-btn" id="ig3dToggle" onclick="toggleModal3dGif(event)">🔄 Vedi Rotazione 3D a 360° Reale</button>
      <div class="ig-bigheart" id="igBigHeart"><svg width="110" height="110" viewBox="0 0 24 24"><path fill="#fff" d="M16.79 2.5A5.2 5.2 0 0 0 12 5.44 5.2 5.2 0 0 0 7.21 2.5 5.5 5.5 0 0 0 2 8.24c0 3.97 3.33 6.6 7.26 10.07.77.68 1.6 1.42 2.46 2.2a.42.42 0 0 0 .56 0c.86-.78 1.69-1.52 2.46-2.2C18.67 14.84 22 12.2 22 8.24A5.5 5.5 0 0 0 16.79 2.5Z"/></svg></div>
    </div>
    <div class="ig-side">
      <div class="ig-side-head">
        <img class="ig-mini" src="__LOGO__" alt="">
        <div class="ig-head-txt"><span class="u">italsportgroup</span> • <button class="ig-link-btn" id="igFollowLink" onclick="toggleFollow()">Segui</button><div class="loc">Ciserano — Zingonia (BG)</div></div>
      </div>
      <div class="ig-comments" id="igComments"></div>
      <div class="ig-actions">
        <button class="ig-act" id="igLikeBtn" onclick="toggleLike()" title="Mi piace"></button>
        <button class="ig-act" onclick="sharePost()" title="Condividi"><svg width="24" height="24" viewBox="0 0 24 24"><path d="M22 3 9.22 10.08M10.69 20.3 22 3H2l7.22 7.08Z" fill="none" stroke="#000" stroke-width="2" stroke-linejoin="round"/></svg></button>
        <button class="ig-act" id="igSaveBtn" onclick="toggleSave()" style="margin-left:auto" title="Salva"></button>
      </div>
      <div class="ig-likes" id="igLikes"></div>
      <div class="ig-date" id="igDate"></div>
    </div>
  </div>
</div>

<div class="ig-story" id="igStory">
  <div class="ig-story-box" onmousedown="pauseStory(true)" onmouseup="pauseStory(false)" onmouseleave="pauseStory(false)">
    <div class="ig-story-bars" id="igBars"></div>
    <div class="ig-story-head">
      <img class="ig-mini" src="__LOGO__" alt="">
      <b>italsportgroup</b><span class="t" id="igStoryName"></span>
      <button class="x" onclick="closeStory()">&times;</button>
    </div>
    <img id="igStoryImg" src="" alt="">
    <div class="ig-story-cap" id="igStoryCap"></div>
    <div class="ig-story-tap l" onclick="storyStep(-1)"></div>
    <div class="ig-story-tap r" onclick="storyStep(1)"></div>
    <div class="ig-story-reply">
      <input placeholder="Rispondi a italsportgroup..." onfocus="pauseStory(true)" onblur="pauseStory(false)" onkeydown="if(event.key==='Enter'&&this.value.trim()){toast('Messaggio inviato');this.value='';this.blur()}">
      <button onclick="toast('Ti piace questa storia')"><svg width="24" height="24" viewBox="0 0 24 24"><path d="M16.79 2.5A5.2 5.2 0 0 0 12 5.44 5.2 5.2 0 0 0 7.21 2.5 5.5 5.5 0 0 0 2 8.24c0 3.97 3.33 6.6 7.26 10.07.77.68 1.6 1.42 2.46 2.2a.42.42 0 0 0 .56 0c.86-.78 1.69-1.52 2.46-2.2C18.67 14.84 22 12.2 22 8.24A5.5 5.5 0 0 0 16.79 2.5Z" fill="none" stroke="#fff" stroke-width="2"/></svg></button>
    </div>
  </div>
</div>
<div class="ig-toast" id="igToast"></div>
"""

IG_JS = r"""
// ===================== INSTAGRAM REALISTICO — ITALSPORT CISERANO (BG) =====================
const IMG = __IMGS__;
const LOGO_SRC = '__LOGO__';
const BASE_FOLLOWERS = 2840;
const HEART_EMPTY = '<svg width="24" height="24" viewBox="0 0 24 24"><path d="M16.79 2.5A5.2 5.2 0 0 0 12 5.44 5.2 5.2 0 0 0 7.21 2.5 5.5 5.5 0 0 0 2 8.24c0 3.97 3.33 6.6 7.26 10.07.77.68 1.6 1.42 2.46 2.2a.42.42 0 0 0 .56 0c.86-.78 1.69-1.52 2.46-2.2C18.67 14.84 22 12.2 22 8.24A5.5 5.5 0 0 0 16.79 2.5Z" fill="none" stroke="#000" stroke-width="2"/></svg>';
const HEART_FULL = '<svg width="24" height="24" viewBox="0 0 24 24"><path d="M16.79 2.5A5.2 5.2 0 0 0 12 5.44 5.2 5.2 0 0 0 7.21 2.5 5.5 5.5 0 0 0 2 8.24c0 3.97 3.33 6.6 7.26 10.07.77.68 1.6 1.42 2.46 2.2a.42.42 0 0 0 .56 0c.86-.78 1.69-1.52 2.46-2.2C18.67 14.84 22 12.2 22 8.24A5.5 5.5 0 0 0 16.79 2.5Z" fill="#ff3040"/></svg>';
const SAVE_EMPTY = '<svg width="24" height="24" viewBox="0 0 24 24"><path d="M20 21 12 13.44 4 21V3h16z" fill="none" stroke="#000" stroke-width="2" stroke-linejoin="round"/></svg>';
const SAVE_FULL = '<svg width="24" height="24" viewBox="0 0 24 24"><path d="M20 22a1 1 0 0 1-.66-.25L12 15.33l-7.34 6.42A1 1 0 0 1 3 21V3a1 1 0 0 1 1-1h16a1 1 0 0 1 1 1v18a1 1 0 0 1-1 1z"/></svg>';
const SMALL_HEART = (on) => `<svg width="12" height="12" viewBox="0 0 24 24"><path d="M16.79 2.5A5.2 5.2 0 0 0 12 5.44 5.2 5.2 0 0 0 7.21 2.5 5.5 5.5 0 0 0 2 8.24c0 3.97 3.33 6.6 7.26 10.07.77.68 1.6 1.42 2.46 2.2a.42.42 0 0 0 .56 0c.86-.78 1.69-1.52 2.46-2.2C18.67 14.84 22 12.2 22 8.24A5.5 5.5 0 0 0 16.79 2.5Z" fill="${on?'#ff3040':'none'}" stroke="${on?'#ff3040':'#737373'}" stroke-width="2"/></svg>`;
const ICO_CAROUSEL = '<svg class="ig-ico" width="20" height="20" viewBox="0 0 24 24" fill="#fff"><path d="M19 4H9a2 2 0 0 0-2 2v10a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2Z"/><path d="M5 8v11a1 1 0 0 0 1 1h11" fill="none" stroke="#fff" stroke-width="2"/></svg>';
const ICO_REEL = '<svg class="ig-ico" width="20" height="20" viewBox="0 0 24 24" fill="#fff"><path d="M12 2.5c-4.7 0-6.9.4-8.2 1.8C2.4 5.6 2 7.8 2 12.5s.4 6.9 1.8 8.2c1.3 1.4 3.5 1.8 8.2 1.8s6.9-.4 8.2-1.8c1.4-1.3 1.8-3.5 1.8-8.2s-.4-6.9-1.8-8.2C18.9 2.9 16.7 2.5 12 2.5Zm-2 6.5 6 3.5-6 3.5Z"/></svg>';

const POSTS = [
 {id:1, img:'p1', img2:'p1_s2', type:'carousel', likes:112, time:'2 g', date:'15 ottobre', likedBy:'usd_brevianese',
  caption:'🎨 STAMPA DTF (Direct-to-Film): Colori che durano, dettagli che contano!\n\nNel nostro laboratorio e reparto grafico interno a Ciserano (BG) realizziamo stampe DTF ad altissima risoluzione:\n✔️ Applicabili sia su tessuti chiari che su capi scuri già confezionati\n✔️ Morbida ed elastica al tatto, zero problemi su cuciture o pieghe\n✔️ Resistente a numerosi lavaggi senza sbiadire né screpolarsi\n\nScopri tutti i nostri servizi di stampa su 🔗 store.italsport-group.it/it/servizi/post/6-stampa-dtf\n\n#stampadtf #dtfprinting #italsportgroup #ciserano #bergamo #personalizzazionisportive #repartografico'},
 {id:2, img:'p2', img2:'p2_s2', type:'carousel', likes:128, time:'4 g', date:'22 ottobre', likedBy:'asd_gessate',
  caption:'👕 STAMPA IN SUBLIMAZIONE & FULL PRINT ALL-OVER: 100% traspirante e totalmente indelebile!\n\nPer l\'abbigliamento tecnico e le divise gara (come le nostre linee Rodi Sublim e Athene Sublim su store.italsport-group.it) utilizziamo la Stampa Sublimatica e Full Print:\n✔️ L\'inchiostro si fonde direttamente nella fibra del poliestere senza ostruire i pori del tessuto\n✔️ Impercettibile al tatto: lascia traspirare la pelle dell\'atleta al 100%\n✔️ Stampiamo il tessuto prima di confezionare il capo: grafiche su tutta la superficie e zero limiti di colore!\n\n🔗 store.italsport-group.it/it/servizi/post/4-stampa-sublimatica\n\n#sublimazione #stampasublimatica #fullprint #italsportgroup #divisepersonalizzate #ciserano #teamwear'},
 {id:3, img:'p3', img2:'p3_s2', type:'reel', likes:154, time:'1 sett.', date:'30 ottobre', likedBy:'polisportiva_ciserano',
  caption:'🔄 SIMULATORE 3D ONLINE: Crea la divisa della tua squadra e ruotala a 360° prima di ordinarla!\n\nCon il nostro Configuratore 3D su italsport-group.it personalizzi il capo in 3 semplici step:\n1️⃣ Scegli lo sport (calcio, volley, basket, rugby, running) e il modello\n2️⃣ Personalizza colori societari, colletto, trame, numeri, nomi e loghi sponsor girando la divisa a 360°\n3️⃣ Conferma il layout e segui in tempo reale lo stato dell\'ordine (Conferma -> Layout -> Approvato -> Ordine -> In Produzione)\n\n👉 Clicca "🔄 Vedi Rotazione 3D a 360° Reale" qui sulla foto per vedere la maglia ruotare!\n\n#simulatore3d #configuratore3d #italsportgroup #customkit #divisesportive #ciserano #bergamo'},
 {id:4, img:'p4', img2:'p4_s2', type:'carousel', likes:146, time:'1 sett.', date:'6 novembre', likedBy:'usd_brevianese',
  caption:'🔒 VETRINA DEDICATA ALLA TUA SQUADRA E AI TUOI CAPI ("MY ITALSPORT")\n\nSu store.italsport-group.it/it/158-clienti-my-italsport creiamo una Vetrina Online esclusiva per la tua società sportiva:\n✔️ Accesso protetto con PASSWORD riservata alla tua squadra\n✔️ Atleti, genitori e dirigenti vedono SOLO i capi ufficiali approvati per il proprio club, già codificati con loghi e colori societari\n✔️ Zero costi di magazzino per la società, zero fogli Excel in segreteria e riordini singoli sempre disponibili!\n\nTu scegli Italsport, al resto pensiamo noi.\n\n#myitalsport #vetrinasquadra #storeitalsport #societasportive #ciserano #bergamo'},
 {id:5, img:'p5', img2:'p5_s2', type:'carousel', likes:119, time:'2 sett.', date:'14 novembre', likedBy:'asd_gessate',
  caption:'🪪 CONTINUITÀ NEGLI ANNI, ZERO MAGAZZINO & TESSERA PRO-CLUB (Basic, Silver, Gold, Diamond)\n\n"Il tuo magazzino a Ciserano lo facciamo noi!" 📦\nNon lasciamo mai le società a piedi a metà stagione con modelli fuori produzione:\n✔️ Continuità garantita negli anni su tutta la tua linea (Kit Gara, Tuta Rom, Polo Rom, Giacca Scotland, Giubbotto Nepal, Rain K-Way, Borsa Bauletto)\n✔️ Anche per 1 solo nuovo iscritto a gennaio o dopo 3 stagioni ritrovi esattamente gli stessi capi e gli stessi colori\n✔️ Con la Tessera PRO-CLUB costruisci il tuo prezzo su misura con sconti e vantaggi crescenti\n\n#tesseraproclub #proclub #continuità #riassortimenti #italsportgroup #ciserano #societasportive'},
 {id:6, img:'p6', img2:'p6_s2', type:'carousel', likes:108, time:'3 sett.', date:'24 novembre', likedBy:'polisportiva_ciserano',
  caption:'🔥 30 ANNI DI STORIA, OLTRE 4.600 REALTÀ SERVITE, LINEA ESCLUSIVA "FLAME" & MULTI-BRAND!\n\nI 5 pilastri di Italsport su store.italsport-group.it:\n1️⃣ FORNITURE continuative e su misura (Basic, Star, Pro, Premium, Elite)\n2️⃣ LOGISTICA puntuale con scarico barcode e preparazione per singolo atleta\n3️⃣ IDENTITÀ unica per ogni club\n4️⃣ PRODOTTI CUSTOM & l\'esclusiva LINEA FLAME Italsport\n5️⃣ MULTI-BRAND: Erreà, Joma, Jako, Givova, Legea, Patrick, Macron, Umbro, Craft, Malfini, Payper, JHK, Roly, Clique, Sixtus in un unico partner!\n\nVestiamo calcio, volley, basket, rugby, atletica, danza, nuoto, oratori, scuole, comuni e aziende.\n\n#lineaflame #multibrand #italsportgroup #30anni #ciserano #bergamo #fornituresportive'},
 {id:7, img:'p7', img2:'p7_s2', type:'carousel', likes:162, time:'3 sett.', date:'20 dicembre', likedBy:'asd_gessate',
  caption:'🎄✨ BUON NATALE E FELICE ANNO NUOVO DAL TEAM DI ITALSPORT!\n\nUn grazie di cuore a tutte le società sportive, ai presidenti, ai dirigenti, agli allenatori, agli atleti, agli oratori, alle scuole e alle aziende che anche quest\'anno sono scesi in campo con noi! ⚽🏐🏀🎁\n\nProgramma i tuoi regali societari, i maglioni natalizi custom a 360°, le felpe, le sciarpe e i cappellini invernali col logo del tuo club nel nostro showroom di Ciserano (Via Provinciale Francesca 2H/I — Zingonia).\n\nTanti auguri di Buone Feste da tutta la squadra Italsport! 🥂🎅\n\n#buonefeste #buonnatale #italsportgroup #ciserano #bergamo #regalisportivi #maglionicustom'}
];

const REELS = [
 {img:'gif3d', title:'Simulatore 3D: rotazione divisa a 360°', views:'3.120', post:3},
 {img:'p1', title:'Laboratorio Stampa DTF ad alta risoluzione', views:'2.450', post:1},
 {img:'p2', title:'Stampa Sublimatica & Full Print 100% traspirante', views:'2.180', post:2}
];

const HIGHLIGHTS = [
 {name:'Stampa DTF', cover:'p1', slides:[{img:'p1',cap:'Stampa DTF ad alta risoluzione su capi chiari e scuri'},{img:'p1_s2',cap:'Reparto grafico interno a Ciserano: dal file vettoriale al capo finito'}]},
 {name:'Sublimazione', cover:'p2', slides:[{img:'p2',cap:'Stampa Sublimatica e Full Print: pori liberi di traspirare al 100%'},{img:'p2_s2',cap:'Linee Rodi Sublim e Athene Sublim su store.italsport-group.it'}]},
 {name:'Simulatore 3D', cover:'p3', slides:[{img:'gif3d',cap:'Gira la tua divisa in 3D a 360° prima di ordinarla'},{img:'p3_s2',cap:'1. Scegli lo sport • 2. Personalizza • 3. Vai in produzione'}]},
 {name:'Vetrina Club', cover:'p4', slides:[{img:'p4',cap:'Vetrina My Italsport dedicata alla tua squadra con password'},{img:'p4_s2',cap:'Zero costi di magazzino e solo i capi ufficiali del tuo club'}]},
 {name:'Pro-Club', cover:'p5', slides:[{img:'p5',cap:'Il tuo magazzino a Ciserano lo facciamo noi: continuità negli anni'},{img:'p5_s2',cap:'Tessera Pro-Club Basic, Silver, Gold, Diamond e Linea Club'}]},
 {name:'Linea Flame', cover:'p6', slides:[{img:'p6',cap:'30 anni di storia, 4.600+ realtà, Linea Flame & Multi-Brand'},{img:'p6_s2',cap:'Sport, oratori, scuole, lavoro, gadget e premiazioni'}]},
 {name:'Buon Natale', cover:'p7', slides:[{img:'p7',cap:'Buone Feste e Felice Anno Nuovo dal Team di Italsport!'},{img:'p7_s2',cap:'Maglioni natalizi custom a 360° e idee regalo per le squadre'}]}
];

const AV_COLORS = ['#f56040','#833ab4','#fcaf45','#405de6','#c13584','#5851db','#e1306c','#0095f6'];
let S = {};
try { S = JSON.parse(localStorage.getItem('italsport_ig_v3') || '{}'); } catch(e) { S = {}; }
S.liked = S.liked || {}; S.saved = S.saved || {}; S.extra = S.extra || {}; S.cLiked = S.cLiked || {}; S.follow = !!S.follow; S.seen = !!S.seen;
const persist = () => { try { localStorage.setItem('italsport_ig_v3', JSON.stringify(S)); } catch(e) {} };
const fmt = n => String(n).replace(/\B(?=(\d{3})+(?!\d))/g, '.');
const esc = s => s.replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const fmtText = s => esc(s).replace(/(#[\wàèéìòù]+|@[\w.]+)/g, '<a style="color:#00376b;text-decoration:none">$1</a>').replace(/\n/g,'<br>');
const likes = p => p.likes + (S.liked[p.id] ? 1 : 0);
const allComments = p => p.comments.concat(S.extra[p.id] || []);
function avatar(u) {
  if (u === 'italsportgroup') return `<img class="ig-mini" src="${LOGO_SRC}" alt="">`;
  let h = 0; for (const ch of u) h = (h * 31 + ch.charCodeAt(0)) >>> 0;
  return `<div class="ig-c-av" style="background:${AV_COLORS[h % AV_COLORS.length]}">${u[0].toUpperCase()}</div>`;
}
function toast(msg) { const t = document.getElementById('igToast'); t.textContent = msg; t.classList.add('show'); clearTimeout(t._h); t._h = setTimeout(() => t.classList.remove('show'), 1900); }
function copyLink(suffix) { try { navigator.clipboard.writeText(location.href.split('#')[0] + suffix); } catch(e) {} }

// ---------- Profilo ----------
function renderFollow() {
  const b = document.getElementById('followBtn');
  b.textContent = S.follow ? 'Segui già' : 'Segui';
  b.className = 'ig-btn' + (S.follow ? '' : ' ig-btn-primary');
  document.getElementById('statFollowers').textContent = fmt(BASE_FOLLOWERS + (S.follow ? 1 : 0));
  const l = document.getElementById('igFollowLink');
  l.textContent = S.follow ? 'Segui già' : 'Segui';
  l.classList.toggle('following', S.follow);
}
function toggleFollow() { S.follow = !S.follow; persist(); renderFollow(); }

function renderHighlights() {
  document.getElementById('igHighlights').innerHTML = HIGHLIGHTS.map((h, i) =>
    `<div class="ig-hl" onclick="openStory(${i})"><div class="ig-hl-ring"><img src="${IMG[h.cover]}" alt=""></div><span>${h.name}</span></div>`).join('');
  document.getElementById('igRing').classList.toggle('seen', S.seen);
}

let currentTab = 'post';
function cell(p) {
  const ico = p.type === 'carousel' ? ICO_CAROUSEL : p.type === 'reel' ? ICO_REEL : '';
  return `<div class="ig-cell" onclick="openIg(${p.id})"><img src="${IMG[p.img]}" alt="" loading="lazy">${ico}
    <div class="ig-hover"><span>${HEART_FULL.replace('#ff3040','#fff').replace('24','19').replace('24','19')} ${fmt(likes(p))}</span></div></div>`;
}
function igTab(t) {
  currentTab = t;
  document.querySelectorAll('.ig-tab').forEach(b => b.classList.toggle('active', b.dataset.tab === t));
  const pane = document.getElementById('igPane');
  if (t === 'post') pane.innerHTML = `<div class="ig-grid">${POSTS.map(cell).join('')}</div>`;
  else if (t === 'reel') pane.innerHTML = `<div class="ig-reels">${REELS.map(r => `<div class="ig-reel" onclick="openIg(${r.post})"><img src="${IMG[r.img]}" alt=""><div class="ig-reel-title">${r.title}</div><div class="ig-reel-info"><svg width="16" height="16" viewBox="0 0 24 24" fill="#fff"><path d="M5 3l15 9-15 9z"/></svg>${r.views}</div></div>`).join('')}</div>`;
  else if (t === 'saved') {
    const sv = POSTS.filter(p => S.saved[p.id]);
    pane.innerHTML = sv.length ? `<div class="ig-grid">${sv.map(cell).join('')}</div>` :
      `<div class="ig-empty">${SAVE_EMPTY.replace(/24/g,'56')}<h3>Salva</h3><p>Tocca l'icona del segnalibro su un post per salvarlo qui.</p></div>`;
  } else pane.innerHTML = `<div class="ig-empty"><svg width="56" height="56" viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="1.5"><path d="M10 18H5a3 3 0 0 1-3-3V5a3 3 0 0 1 3-3h14a3 3 0 0 1 3 3v10a3 3 0 0 1-3 3h-5l-2 3z"/><circle cx="12" cy="9" r="3"/></svg><h3>Foto in cui appare italsportgroup</h3><p>Quando le società sportive di Bergamo e della Lombardia taggano @italsportgroup nelle foto, compaiono qui.</p></div>`;
}

// ---------- Modal post ----------
let cur = null;
let showingGif3d = false;
let showingSlide2 = false;
function openIg(id) { cur = POSTS.findIndex(p => p.id === id); showingGif3d = false; showingSlide2 = false; renderModal(); document.getElementById('igModal').classList.add('open'); document.body.style.overflow = 'hidden'; }
const openPostModal = openIg;
function closeIg() { document.getElementById('igModal').classList.remove('open'); document.body.style.overflow = ''; cur = null; igTab(currentTab); }
function navIg(d) { const n = cur + d; if (n >= 0 && n < POSTS.length) { cur = n; showingGif3d = false; showingSlide2 = false; renderModal(); } }
function toggleModalSlide(e) {
  if (e) e.stopPropagation();
  showingGif3d = false;
  showingSlide2 = !showingSlide2;
  renderModalMedia();
}
function toggleModal3dGif(e) {
  if (e) e.stopPropagation();
  showingSlide2 = false;
  showingGif3d = !showingGif3d;
  renderModalMedia();
}
function renderModalMedia() {
  const p = POSTS[cur];
  const imgEl = document.getElementById('igImg');
  if (showingGif3d) imgEl.src = IMG['gif3d'];
  else if (showingSlide2 && p.img2 && IMG[p.img2]) imgEl.src = IMG[p.img2];
  else imgEl.src = IMG[p.img];

  const btnSlide = document.getElementById('igSlideToggle');
  if (btnSlide) {
    btnSlide.style.display = (p.img2 && IMG[p.img2]) ? 'inline-flex' : 'none';
    btnSlide.textContent = showingSlide2 ? '◀️ Torna a Slide 1 (1/2)' : '▶️ Vedi Slide 2 (2/2)';
  }
  const btn3d = document.getElementById('ig3dToggle');
  if (btn3d) {
    btn3d.style.display = (p.id === 3) ? 'inline-flex' : 'none';
    btn3d.textContent = showingGif3d ? '🖼️ Torna alla Scheda Post' : '🔄 Vedi Rotazione 3D a 360° Reale';
  }
}
function renderModal() {
  const p = POSTS[cur];
  renderModalMedia();
  document.getElementById('igPrev').hidden = cur === 0;
  document.getElementById('igNext').hidden = cur === POSTS.length - 1;
  const cap = `<div class="ig-c">${avatar('italsportgroup')}<div class="ig-c-body"><span class="u">italsportgroup</span>${fmtText(p.caption)}<div class="ig-c-meta"><span>${p.time}</span></div></div></div>`;
  const box = document.getElementById('igComments'); box.innerHTML = cap;
  renderActions();
  document.getElementById('igDate').textContent = p.date;
  renderFollow();
}
function renderActions() {
  const p = POSTS[cur];
  document.getElementById('igLikeBtn').innerHTML = S.liked[p.id] ? HEART_FULL : HEART_EMPTY;
  document.getElementById('igSaveBtn').innerHTML = S.saved[p.id] ? SAVE_FULL : SAVE_EMPTY;
  const n = likes(p);
  document.getElementById('igLikes').innerHTML = S.liked[p.id]
    ? `Piace a <b>te</b> e ad altre ${fmt(n - 1)} persone`
    : `Piace a <b>${p.likedBy}</b> e ad altre ${fmt(n - 1)} persone`;
}
function beat(id) { const b = document.getElementById(id); b.classList.remove('beat'); void b.offsetWidth; b.classList.add('beat'); }
function toggleLike() { const p = POSTS[cur]; S.liked[p.id] = !S.liked[p.id]; persist(); renderActions(); beat('igLikeBtn'); }
function dblLike() {
  const p = POSTS[cur]; const h = document.getElementById('igBigHeart');
  h.classList.remove('pop'); void h.offsetWidth; h.classList.add('pop');
  if (!S.liked[p.id]) { S.liked[p.id] = true; persist(); renderActions(); beat('igLikeBtn'); }
}
function toggleSave() { const p = POSTS[cur]; S.saved[p.id] = !S.saved[p.id]; persist(); renderActions(); beat('igSaveBtn'); toast(S.saved[p.id] ? 'Post salvato' : 'Rimosso dai salvati'); }
function sharePost() { copyLink('#post' + POSTS[cur].id); toast('Link copiato negli appunti'); }

// ---------- Storie ----------
const STORY_MS = 5000;
let st = null;
function openStory(h) { st = {h, s:0, t:0, paused:false, last:performance.now()}; S.seen = true; persist(); renderHighlights(); document.getElementById('igStory').classList.add('open'); showSlide(); requestAnimationFrame(tickStory); }
function closeStory() { document.getElementById('igStory').classList.remove('open'); st = null; }
function showSlide() {
  const h = HIGHLIGHTS[st.h], sl = h.slides[st.s];
  document.getElementById('igStoryImg').src = IMG[sl.img];
  document.getElementById('igStoryCap').textContent = sl.cap;
  document.getElementById('igStoryName').textContent = h.name;
  document.getElementById('igBars').innerHTML = h.slides.map((_, i) => `<div><i style="width:${i < st.s ? 100 : 0}%"></i></div>`).join('');
  st.t = 0;
}
function storyStep(d) {
  if (!st) return;
  const h = HIGHLIGHTS[st.h];
  st.s += d;
  if (st.s < 0) { if (st.h > 0) { st.h--; st.s = HIGHLIGHTS[st.h].slides.length - 1; } else st.s = 0; }
  else if (st.s >= h.slides.length) { if (st.h < HIGHLIGHTS.length - 1) { st.h++; st.s = 0; } else return closeStory(); }
  showSlide();
}
function pauseStory(v) { if (st) st.paused = v; }
function tickStory(now) {
  if (!st) return;
  const dt = now - st.last; st.last = now;
  if (!st.paused) {
    st.t += dt;
    const bar = document.querySelectorAll('#igBars i')[st.s];
    if (bar) bar.style.width = Math.min(100, st.t / STORY_MS * 100) + '%';
    if (st.t >= STORY_MS) storyStep(1);
  }
  if (st) requestAnimationFrame(tickStory);
}

document.addEventListener('keydown', e => {
  if (document.activeElement && document.activeElement.tagName === 'INPUT') return;
  if (st) { if (e.key === 'Escape') closeStory(); if (e.key === 'ArrowRight') storyStep(1); if (e.key === 'ArrowLeft') storyStep(-1); return; }
  if (cur !== null) { if (e.key === 'Escape') closeIg(); if (e.key === 'ArrowRight') navIg(1); if (e.key === 'ArrowLeft') navIg(-1); }
});

renderHighlights(); renderFollow(); igTab('post');
const m = location.hash.match(/^#post(\d)$/); if (m) openIg(+m[1]);
"""
