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
          <div class="ig-name">Italsport Group • Ciserano (BG)</div>
          <div class="ig-cat">Forniture Sportive & Personalizzazioni • Dal 1995</div>
          <div>👕 Divise, tute, borse, stampe, ricami e premi per società sportive, oratori, scuole e aziende</div>
          <div>🔄 Configuratore 3D a 360° e Tessera Pro-Club</div>
          <div>🔒 Vetrina My Italsport con password dedicata per ogni squadra</div>
          <div>📍 Via Provinciale Francesca 2H/I, Ciserano — Zingonia (BG) • ☎️ 035 4191221</div>
          <a href="https://italsport-group.it" target="_blank">🔗 italsport-group.it</a>
        </div>
        <div class="ig-followedby">Seguito da <b>usd_brevianese</b>, <b>asd_gessate</b>, <b>polisportiva_ciserano</b> e altri 18</div>
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
        <button class="ig-act" onclick="document.getElementById('igInput').focus()" title="Commenta"><svg width="24" height="24" viewBox="0 0 24 24"><path d="M20.66 17.04A9.8 9.8 0 1 0 17 20.66L22 22Z" fill="none" stroke="#000" stroke-width="2" stroke-linejoin="round"/></svg></button>
        <button class="ig-act" onclick="sharePost()" title="Condividi"><svg width="24" height="24" viewBox="0 0 24 24"><path d="M22 3 9.22 10.08M10.69 20.3 22 3H2l7.22 7.08Z" fill="none" stroke="#000" stroke-width="2" stroke-linejoin="round"/></svg></button>
        <button class="ig-act" id="igSaveBtn" onclick="toggleSave()" style="margin-left:auto" title="Salva"></button>
      </div>
      <div class="ig-likes" id="igLikes"></div>
      <div class="ig-date" id="igDate"></div>
      <form class="ig-add" onsubmit="addComment(event)">
        <span style="font-size:22px">☺</span>
        <input id="igInput" placeholder="Aggiungi un commento..." autocomplete="off" oninput="document.getElementById('igPost').disabled=!this.value.trim()">
        <button id="igPost" type="submit" disabled>Pubblica</button>
      </form>
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
 {id:1, img:'p1', type:'', likes:89, time:'2 g', date:'15 ottobre', likedBy:'usd_brevianese',
  caption:'Da 30 anni vestiamo lo sport: dalla progettazione grafica alla personalizzazione con stampa e ricamo, realizziamo divise e linee societarie fatte per durare stagione dopo stagione. ⚽🏀🏐\n\nPassa a trovarci nel nostro showroom a Ciserano (Via Provinciale Francesca 2H/I — Zingonia) o scrivici in DM.\n\n#italsportgroup #ciserano #bergamo #fornituresportive #divisepersonalizzate #teamwear',
  comments:[{u:'usd_brevianese',t:'Qualità top, le nostre divise dopo un anno di campionato e lavaggi sono ancora perfette 👏',l:5,time:'1 g'},{u:'asd_gessate',t:'Sempre una garanzia per tutta la società!',l:2,time:'1 g'},{u:'polisportiva_ciserano',t:'Passiamo in settimana in showroom per i campioni invernali 💪',l:3,time:'19 h'}]},
 {id:2, img:'p2', type:'reel', likes:134, time:'4 g', date:'22 ottobre', likedBy:'asd_gessate',
  caption:'Vuoi vedere come sarà la divisa della tua squadra prima di ordinarla? 🔄👕\n\nCon il Configuratore 3D su italsport-group.it scegli modello, colori societari, colletto, numeri e sponsor e ruoti la maglia a 360° da ogni angolazione.\n\nProvalo dal link in bio 🔗 (oppure clicca "Vedi Rotazione 3D a 360°" qui sulla foto!)\n\n#configuratore3d #italsportgroup #divisesportive #customkit #ciserano',
  comments:[{u:'mister_locatelli',t:'Provato ieri sera col direttivo, comodissimo vedere la maglia girare a 360° prima di confermare!',l:7,time:'3 g'},{u:'volley_zingonia',t:'Si possono configurare anche le divise da pallavolo e basket?',l:1,time:'2 g'},{u:'italsportgroup',t:'@volley_zingonia certamente! Trovate i modelli per calcio, volley, basket e rappresentanza 🏐🏀',l:4,time:'2 g'}]},
 {id:3, img:'p3', type:'carousel', likes:104, time:'1 sett.', date:'30 ottobre', likedBy:'polisportiva_ciserano',
  caption:'Scopri la Tessera PRO-CLUB di Italsport (Basic, Silver, Gold, Diamond) pensata per le società sportive 🪪✨\n\n✔️ Disponibilità: facciamo noi il magazzino a Ciserano per la tua società (zero anticipi e zero rimanenze)\n✔️ Servizio e listino riservato con sconti dedicati al club\n✔️ Continuità garantita negli anni sugli stessi modelli e colori\n✔️ Vetrina online dedicata alla squadra inclusa\n\nContattaci allo 035 4191221 o in DM per scoprire il livello Pro-Club per la tua società.\n\n#tesseraproclub #proclub #italsportgroup #societasportive #bergamo',
  comments:[{u:'segreteria.sportbg',t:'Non dover fare magazzino in sede ci ha tolto un peso enorme 👍',l:6,time:'6 g'},{u:'usd_brevianese',t:'Servizio Pro-Club comodissimo per gestire tutta la stagione',l:4,time:'5 g'}]},
 {id:4, img:'p4', type:'', likes:82, time:'1 sett.', date:'6 novembre', likedBy:'mister_locatelli',
  caption:'Nuovo iscritto a metà stagione o riordino l\'anno successivo? Con Italsport ritrovi sempre la stessa linea societaria! 🔁👕\n\nDal Kit Gara alla Tuta Rom, dalla Giacca Scotland al Giubbotto Nepal, fino a Rain K-Way e Borsa Bauletto: garantiamo la continuità dei capi nel tempo, anche per singoli riassortimenti.\n\n#continuità #riassortimenti #italsportgroup #lineasocietaria #ciserano',
  comments:[{u:'mister_locatelli',t:'Fondamentale: avere tutti i ragazzi vestiti uguali anche quando entrano nuovi iscritti a gennaio!',l:6,time:'6 g'},{u:'asd_gessate',t:'Confermo, riordinati 4 kit completi ed erano identici al primo ordine 👌',l:3,time:'5 g'}]},
 {id:5, img:'p5', type:'carousel', likes:146, time:'2 sett.', date:'14 novembre', likedBy:'usd_brevianese',
  caption:'Come funziona la Vetrina Personalizzata "My Italsport" per la tua squadra? 🔒🛒\n\nOgni società sportiva ha una propria vetrina dedicata su store.italsport-group.it protetta da una PASSWORD riservata:\n\n1️⃣ Accedi con la password della tua squadra\n2️⃣ Vedi SOLO ed esclusivamente i capi ufficiali approvati per il tuo club (niente confusione con altri articoli)\n3️⃣ Ritrovi sempre esattamente gli stessi prodotti, stessi colori e stesse taglie nel tempo, senza errori o capi esauriti!\n\nScrivici in DM per attivare la vetrina con password per la tua società.\n\n#myitalsport #vetrinasquadra #italsportgroup #societasportive #ciserano',
  comments:[{u:'usd_brevianese',t:'Da quando abbiamo la vetrina con la nostra password nessuno sbaglia più articolo o colore, comodissima!',l:9,time:'1 sett.'},{u:'elena_genitore',t:'Entrata con la password della società e trovato subito tutta la linea ufficiale 😊',l:4,time:'1 sett.'},{u:'polisportiva_ciserano',t:'Zero errori e troviamo sempre gli stessi capi ogni anno!',l:5,time:'6 g'}]},
 {id:6, img:'p6', type:'', likes:95, time:'3 sett.', date:'24 novembre', likedBy:'polisportiva_ciserano',
  caption:'Oltre 4.600 realtà tra società sportive, oratori, scuole, comuni e aziende hanno scelto Italsport in questi 30 anni. 🏟️🙌\n\nCalcio, volley, basket, rugby, atletica e tempo libero: grazie a chi scende in campo ogni weekend con le nostre divise!\n\n#sulcampoconvoi #italsportgroup #sportlombardia #bergamo #calcio #volley',
  comments:[{u:'asd_gessate',t:'Orgogliosi di scendere in campo con le vostre divise! 💙',l:4,time:'2 sett.'},{u:'volley_zingonia',t:'Disponibilità e qualità sempre al top',l:3,time:'2 sett.'}]},
 {id:7, img:'p7', type:'', likes:138, time:'3 sett.', date:'10 dicembre', likedBy:'asd_gessate',
  caption:'Invernale, felpe, giubbotti e idee regalo col logo della tua squadra per le feste di fine anno! 🎄🎁\n\nPassa nel nostro showroom a Ciserano (Via Provinciale Francesca 2H/I — Loc. Zingonia) per toccare con mano i tessuti, le borse, i cappellini e i gadget personalizzati per la tua società o azienda.\n\n📞 035 4191221 • 📱 335 7001956\n\n#italsportgroup #showroomciserano #gadgetsportivi #abbigliamentoinvernale #buonefeste',
  comments:[{u:'polisportiva_ciserano',t:'Le felpe natalizie col logo della società sono andate a ruba! 🎄👏',l:6,time:'3 sett.'},{u:'usd_brevianese',t:'Passiamo in negozio venerdì mattina!',l:3,time:'3 sett.'}]}
];

const REELS = [
 {img:'gif3d', title:'Configuratore 3D: rotazione maglia a 360°', views:'2.640', post:2},
 {img:'p5', title:'Vetrina Squadra con Password su My Italsport', views:'1.980', post:5},
 {img:'shw', title:'Il nostro Showroom a Ciserano (BG)', views:'1.750', post:7}
];

const HIGHLIGHTS = [
 {name:'Configuratore', cover:'p2', slides:[{img:'gif3d',cap:'Gira la tua divisa in 3D a 360° prima di ordinarla'},{img:'p2',cap:'Personalizza colori, colletto, numeri e sponsor'}]},
 {name:'Vetrina Club', cover:'p5', slides:[{img:'p5',cap:'Ogni squadra entra con la sua password e vede solo i suoi capi'},{img:'p4',cap:'Ritrovi sempre gli stessi articoli nel tempo senza problemi'}]},
 {name:'Pro-Club', cover:'p3', slides:[{img:'p3',cap:'Tessera Pro-Club: Basic, Silver, Gold e Diamond'},{img:'card',cap:'Zero magazzino per il club e listino bloccato'}]},
 {name:'Divise Custom', cover:'p1', slides:[{img:'p1',cap:'Stampa, ricamo e tessuti tecnici fatti per durare'},{img:'man',cap:'Forniture per calcio, basket, volley e rappresentanza'}]},
 {name:'Showroom BG', cover:'shw', slides:[{img:'shw',cap:'Ti aspettiamo a Ciserano (BG) in Via Provinciale Francesca 2H/I'},{img:'p7',cap:'Felpe, giubbotti, borse e gadget col tuo logo'}]},
 {name:'Sul Campo', cover:'p6', slides:[{img:'p6',cap:'Oltre 4.600 società, oratori, scuole e aziende servite'}]}
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
    <div class="ig-hover"><span>${HEART_FULL.replace('#ff3040','#fff').replace('24','19').replace('24','19')} ${fmt(likes(p))}</span>
    <span><svg width="19" height="19" viewBox="0 0 24 24"><path d="M20.66 17.04A9.8 9.8 0 1 0 17 20.66L22 22Z" fill="#fff"/></svg> ${allComments(p).length}</span></div></div>`;
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
function openIg(id) { cur = POSTS.findIndex(p => p.id === id); showingGif3d = false; renderModal(); document.getElementById('igModal').classList.add('open'); document.body.style.overflow = 'hidden'; }
const openPostModal = openIg;
function closeIg() { document.getElementById('igModal').classList.remove('open'); document.body.style.overflow = ''; cur = null; igTab(currentTab); }
function navIg(d) { const n = cur + d; if (n >= 0 && n < POSTS.length) { cur = n; showingGif3d = false; renderModal(); } }
function toggleModal3dGif(e) {
  if (e) e.stopPropagation();
  showingGif3d = !showingGif3d;
  const p = POSTS[cur];
  document.getElementById('igImg').src = showingGif3d ? IMG['gif3d'] : IMG[p.img];
  document.getElementById('ig3dToggle').textContent = showingGif3d ? '🖼️ Torna alla Scheda Post' : '🔄 Vedi Rotazione 3D a 360° Reale';
}
function renderModal() {
  const p = POSTS[cur];
  document.getElementById('igImg').src = showingGif3d ? IMG['gif3d'] : IMG[p.img];
  const btn3d = document.getElementById('ig3dToggle');
  if (btn3d) {
    btn3d.style.display = (p.id === 2) ? 'inline-flex' : 'none';
    btn3d.textContent = showingGif3d ? '🖼️ Torna alla Scheda Post' : '🔄 Vedi Rotazione 3D a 360° Reale';
  }
  document.getElementById('igPrev').hidden = cur === 0;
  document.getElementById('igNext').hidden = cur === POSTS.length - 1;
  const cap = `<div class="ig-c">${avatar('italsportgroup')}<div class="ig-c-body"><span class="u">italsportgroup</span>${fmtText(p.caption)}<div class="ig-c-meta"><span>${p.time}</span></div></div></div>`;
  const list = allComments(p).map((c, i) => {
    const key = p.id + '_' + i, on = !!S.cLiked[key], n = c.l + (on ? 1 : 0);
    return `<div class="ig-c">${avatar(c.u)}<div class="ig-c-body"><span class="u">${c.u}</span>${fmtText(c.t)}
      <div class="ig-c-meta"><span>${c.time}</span>${n ? `<span>${n} Mi piace</span>` : ''}<button onclick="replyTo('${c.u}')">Rispondi</button></div></div>
      <button class="ig-c-heart" onclick="toggleCLike('${key}')">${SMALL_HEART(on)}</button></div>`;
  }).join('');
  const box = document.getElementById('igComments'); box.innerHTML = cap + list;
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
function toggleCLike(key) { S.cLiked[key] = !S.cLiked[key]; persist(); const st = document.getElementById('igComments').scrollTop; renderModal(); document.getElementById('igComments').scrollTop = st; }
function replyTo(u) { const i = document.getElementById('igInput'); i.value = '@' + u + ' '; i.focus(); document.getElementById('igPost').disabled = false; }
function sharePost() { copyLink('#post' + POSTS[cur].id); toast('Link copiato negli appunti'); }
function addComment(e) {
  e.preventDefault();
  const i = document.getElementById('igInput'), t = i.value.trim(); if (!t) return;
  const p = POSTS[cur]; (S.extra[p.id] = S.extra[p.id] || []).push({u:'il_tuo_profilo', t, l:0, time:'Adesso'});
  persist(); i.value = ''; document.getElementById('igPost').disabled = true;
  renderModal(); const box = document.getElementById('igComments'); box.scrollTop = box.scrollHeight;
}

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
