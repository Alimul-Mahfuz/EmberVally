html_content = '''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>Amber Valley</title>
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<link href="https://fonts.googleapis.com/css2?family=Gaegu:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{--ink:#4a2c1a;--paper:#fff3dc;--accent:#c2562b;color-scheme:light dark}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--ink:#ffe9c7;--paper:#3a2216;--accent:#ff9a57}}
:root[data-theme="dark"]{--ink:#ffe9c7;--paper:#3a2216;--accent:#ff9a57}
html,body{height:100%;margin:0;overflow:hidden;background:#0b0f17;font-family:Gaegu,'Comic Sans MS',cursive;color:var(--ink)}
canvas{display:block;width:100%;height:100%;touch-action:none}
#hud{position:fixed;top:calc(12px + env(safe-area-inset-top));left:14px;background:var(--paper);padding:6px 14px;border-radius:14px;font-size:24px;font-weight:700;box-shadow:0 3px 0 rgba(0,0,0,.15);z-index:10}
#hud small{display:block;font-size:17px;font-weight:400;opacity:.88}
#top-right-bar{position:fixed;top:calc(12px + env(safe-area-inset-top));right:14px;display:flex;gap:8px;z-index:25}
.top-btn{background:var(--paper);color:var(--ink);padding:6px 13px;border-radius:14px;font-size:22px;font-weight:700;border:0;cursor:pointer;box-shadow:0 3px 0 rgba(0,0,0,.15);transition:transform .15s}
.top-btn:hover{transform:scale(1.05)}
#toast{position:fixed;left:50%;top:22%;transform:translateX(-50%);font-size:28px;font-weight:700;color:#fff6df;text-shadow:0 2px 0 #7a3a1a,0 0 14px #7a3a1a;opacity:0;transition:opacity .4s;pointer-events:none;text-align:center;padding:0 14px;z-index:15}
.ov{position:fixed;inset:0;display:flex;align-items:center;justify-content:center;background:rgba(18,14,16,.58);padding:env(safe-area-inset-top) 16px env(safe-area-inset-bottom);z-index:30}
.ov[hidden]{display:none}
.card{background:var(--paper);max-width:440px;padding:26px 28px;border-radius:22px;text-align:center;box-shadow:0 6px 0 rgba(0,0,0,.18)}
.card h1{margin:0 0 8px;font-size:48px;line-height:1}
.card p{margin:8px 0;font-size:21px;line-height:1.25}
button{font:inherit;font-size:24px;font-weight:700;background:var(--accent);color:#fff;border:0;border-radius:14px;padding:8px 24px;margin-top:10px;cursor:pointer}
button:focus-visible{outline:3px solid var(--ink);outline-offset:3px}
.settings-card{max-width:450px;width:100%;text-align:left;padding:20px 24px;max-height:90vh;overflow-y:auto}
.settings-card h2{margin:0;font-size:36px;color:var(--ink)}
.setting-group{margin:10px 0}
.setting-label{font-size:19px;font-weight:700;display:block;margin-bottom:5px;color:var(--ink)}
.btn-row{display:flex;gap:6px;flex-wrap:wrap}
.btn-row button{flex:1 1 20%;min-width:65px;margin-top:0;padding:6px 8px;font-size:17px;border-radius:10px;background:rgba(0,0,0,.08);color:var(--ink);box-shadow:none;transition:all .15s}
.btn-row button.active{background:var(--accent);color:#fff}
.check-label{display:inline-flex;align-items:center;gap:8px;font-size:17px;margin-top:5px;cursor:pointer;user-select:none;color:var(--ink)}
.check-label input{accent-color:var(--accent);width:18px;height:18px;cursor:pointer}
#interact-prompt{position:fixed;bottom:26px;left:50%;transform:translateX(-50%);background:var(--accent);color:#fff;font-size:21px;font-weight:700;border:0;border-radius:16px;padding:10px 24px;box-shadow:0 4px 16px rgba(0,0,0,.4);cursor:pointer;z-index:20;transition:transform .15s;animation:promptBounce 1.8s infinite ease-in-out}
#interact-prompt:hover{transform:translateX(-50%) scale(1.05)}
@keyframes promptBounce{0%,100%{transform:translateX(-50%) translateY(0)}50%{transform:translateX(-50%) translateY(-6px)}}
.cabin-card{max-width:480px;width:100%;text-align:left;padding:22px 26px;border-radius:24px}
.hearth-box{background:rgba(194,86,43,.12);border:2px dashed var(--accent);border-radius:16px;padding:14px;margin:10px 0;text-align:center}
.cabin-actions{display:flex;gap:10px;margin:12px 0}
.cabin-btn{flex:1;background:var(--paper);border:2px solid var(--accent);color:var(--ink);font-size:18px;padding:10px 6px;border-radius:14px;cursor:pointer;transition:all .15s;text-align:center}
.cabin-btn:hover{background:var(--accent);color:#fff}
</style></head><body>
<canvas id="c"></canvas>
<div id="hud">
 <div>Leaves <span id="n">0</span> / 12 &nbsp;|&nbsp; Critters <span id="cn">0</span></div>
 <small id="season-hud">🍂 Autumn Valley</small>
 <small id="obj">Find the glowing leaves</small>
 <small id="pw"></small>
</div>
<div id="top-right-bar">
 <button id="sound-btn" class="top-btn" title="Toggle Sound">🔊</button>
 <button id="menu-btn" class="top-btn" title="Settings">☰</button>
</div>
<button id="interact-prompt" hidden>🏡 Enter Cabin (Press E)</button>
<div id="toast"></div>
<div class="ov" id="start"><div class="card"><h1>Amber Valley</h1>
 <p>Twelve glowing leaves lie scattered across the valley. Gather them to light the ancient cabin hearth.</p>
 <p>Roam the valley, discover the <b>Whispering Monolith</b> for leaf guidance, drink from the <b>Moon Shrine</b> to walk on water, and spring launch from <b>Fairy Mushrooms</b>!</p>
 <p>At night, explore under the starry sky with your warm lantern. Change seasons and weather anytime in the <b>☰ Settings</b> menu.</p>
 <p><b>W / S</b> walk &nbsp; <b>A / D</b> turn &nbsp; <b>Shift</b> run &nbsp; <b>Space</b> jump<br>Drag to look around. Scroll wheel to zoom.</p>
 <button id="go">Start walking</button></div></div>
<div class="ov" id="win" hidden><div class="card"><h1>Hearth lit</h1><p>The chimney is smoking and the window glows through the dark valley. The valley is yours to wander through all seasons.</p><button id="again">Keep exploring</button></div></div>
<div class="ov" id="settings-modal" hidden>
 <div class="card settings-card">
  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px">
   <h2>Settings</h2>
   <button id="close-settings" style="margin:0;padding:2px 14px;font-size:22px;border-radius:10px">✕</button>
  </div>
  <div class="setting-group">
   <span class="setting-label">Season Shift</span>
   <div class="btn-row" id="season-btns">
    <button data-s="spring">🌸 Spring</button>
    <button data-s="summer">☀️ Summer</button>
    <button data-s="autumn" class="active">🍂 Autumn</button>
    <button data-s="winter">❄️ Winter</button>
   </div>
   <label class="check-label"><input type="checkbox" id="auto-season"> Dynamic season shift cycle</label>
  </div>
  <div class="setting-group">
   <span class="setting-label">Time of Day</span>
   <div class="btn-row" id="tod-btns">
    <button data-t="0.5" class="active">☀️ Day</button>
    <button data-t="0.75">🌅 Sunset</button>
    <button data-t="0.0">🌙 Dark Night</button>
    <button data-t="0.25">🌄 Dawn</button>
   </div>
   <label class="check-label"><input type="checkbox" id="auto-time"> Cycle day/night automatically</label>
  </div>
  <div class="setting-group">
   <span class="setting-label">Weather Simulation</span>
   <div class="btn-row" id="weather-btns">
    <button data-w="clear" class="active">✨ Clear</button>
    <button data-w="fog">🌫️ Fog</button>
    <button data-w="rain">🌧️ Rain</button>
    <button data-w="storm">⚡ Storm</button>
   </div>
   <label class="check-label"><input type="checkbox" id="auto-weather"> Dynamic changing weather</label>
  </div>
  <div class="setting-group">
   <span class="setting-label">Sound & Atmosphere</span>
   <div class="btn-row">
    <button id="toggle-audio-btn" style="flex:1">🔊 Sound: ON</button>
   </div>
  </div>
  <div class="setting-group" style="margin-top:8px">
   <button id="travel-cabin-btn" style="width:100%;margin-top:0;font-size:18px;padding:8px 14px;background:#8b482b">🏡 Fast Travel to Woodland Cabin</button>
  </div>
  <div class="setting-group">
   <span class="setting-label">Graphics Quality</span>
   <div class="btn-row" id="quality-btns">
    <button data-q="0.45">⚡ Fast</button>
    <button data-q="0.65" class="active">⚖️ Balanced</button>
    <button data-q="1.0">🌟 Ultra</button>
   </div>
   <div id="fps-display" style="font-size:15px;opacity:.85;margin-top:6px">FPS: 60</div>
  </div>
 </div>
</div>
<div class="ov" id="cabin-view" hidden>
 <div class="card cabin-card">
  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:4px">
   <h2 style="margin:0;font-size:38px">🏡 Woodland Cabin</h2>
   <button id="exit-cabin-top" style="margin:0;padding:2px 14px;font-size:22px;border-radius:10px">✕</button>
  </div>
  <p style="margin:4px 0 10px;font-size:20px;opacity:.9">Warm cedar beams and crackling pine embers shelter you from the valley wind.</p>
  
  <div class="hearth-box">
   <div id="hearth-status" style="font-size:24px;font-weight:700;color:var(--accent)">🔥 Hearth: <span id="hearth-leaves">0</span> / 12 Leaves Burning</div>
   <div id="hearth-desc" style="font-size:18px;margin-top:4px">Leaves placed in the hearth keep the valley warm and illuminated.</div>
   <button id="add-leaves-btn" style="margin-top:10px;font-size:20px;padding:8px 22px">🍂 Feed Leaves to Fire (<span id="avail-leaves">0</span> ready)</button>
  </div>

  <div class="cabin-actions">
   <button id="cider-btn" class="cabin-btn">☕ Spiced Cider<small style="display:block;font-size:14px;opacity:.8">Swift & Leap vitality</small></button>
   <button id="sleep-btn" class="cabin-btn">🛌 Rest by Fire<small style="display:block;font-size:14px;opacity:.8">Advance time & clear storm</small></button>
  </div>

  <div id="cabin-outside-note" style="font-size:18px;margin:8px 0;opacity:.85;text-align:center">Window: Autumn leaves dancing outside</div>
  <button id="exit-cabin-btn" style="width:100%;margin-top:8px;background:var(--ink);color:var(--paper)">🚪 Step Outside into the Valley</button>
 </div>
</div>
<script>
const cv=document.getElementById('c'),g=cv.getContext('2d');
let W,H,DPR;
let qualityScale=0.65;
const offCv=document.createElement('canvas'),offG=offCv.getContext('2d');
let offW=0,offH=0,offImg=null,offBuf=null;
function rs(){
 DPR=Math.min(devicePixelRatio||1,2);
 W=innerWidth;H=innerHeight;
 cv.width=W*DPR;cv.height=H*DPR;
 g.setTransform(DPR,0,0,DPR,0,0);
 const targetW=Math.max(360,Math.round(W*qualityScale));
 offW=Math.min(targetW,qualityScale>=1?W:960);
 offH=Math.max(120,Math.round(offW*(H/W)));
 offCv.width=offW;offCv.height=offH;
 offImg=offG.createImageData(offW,offH);
 offBuf=new Uint32Array(offImg.data.buffer);
}
addEventListener('resize',rs);rs();

// --- Procedural Web Audio Engine ---
class ProceduralAudio {
 constructor(){this.ctx=null;this.enabled=true;this.lastStep=0;}
 init(){
  if(this.ctx)return;
  const AudioCtx=window.AudioContext||window.webkitAudioContext;
  if(AudioCtx){this.ctx=new AudioCtx();if(this.ctx.state==='suspended')this.ctx.resume()}
 }
 playTone(freq,type='sine',dur=0.2,vol=0.15,delay=0){
  if(!this.enabled||!this.ctx)return;
  try{
   const t=this.ctx.currentTime+delay;
   const osc=this.ctx.createOscillator(),gn=this.ctx.createGain();
   osc.type=type;osc.frequency.setValueAtTime(freq,t);
   gn.gain.setValueAtTime(vol,t);
   gn.gain.exponentialRampToValueAtTime(0.0001,t+dur);
   osc.connect(gn);gn.connect(this.ctx.destination);
   osc.start(t);osc.stop(t+dur);
  }catch(e){}
 }
 playChime(freqs=[523,659,784,1046],dur=0.4){
  if(!this.enabled||!this.ctx)return;
  freqs.forEach((f,i)=>this.playTone(f,'sine',dur+i*0.08,0.12,i*0.07));
 }
 playEthereal(root=440){
  if(!this.enabled||!this.ctx)return;
  [root,root*1.25,root*1.5,root*2].forEach((f,i)=>this.playTone(f,'triangle',1.4,0.08,i*0.05));
 }
 playSpring(){
  if(!this.enabled||!this.ctx)return;
  try{
   const t=this.ctx.currentTime,osc=this.ctx.createOscillator(),gn=this.ctx.createGain();
   osc.type='sine';osc.frequency.setValueAtTime(260,t);
   osc.frequency.exponentialRampToValueAtTime(950,t+0.35);
   gn.gain.setValueAtTime(0.18,t);
   gn.gain.exponentialRampToValueAtTime(0.001,t+0.38);
   osc.connect(gn);gn.connect(this.ctx.destination);
   osc.start(t);osc.stop(t+0.38);
  }catch(e){}
 }
 playStep(surface='grass'){
  if(!this.enabled||!this.ctx)return;
  const now=performance.now();
  if(now-this.lastStep<260)return;
  this.lastStep=now;
  try{
   const t=this.ctx.currentTime;
   const buf=this.ctx.createBuffer(1,this.ctx.sampleRate*0.05,this.ctx.sampleRate);
   const d=buf.getChannelData(0);
   for(let i=0;i<d.length;i++)d[i]=(Math.random()*2-1)*Math.exp(-i/(this.ctx.sampleRate*0.012));
   const src=this.ctx.createBufferSource();src.buffer=buf;
   const filter=this.ctx.createBiquadFilter();
   filter.type='lowpass';
   filter.frequency.value=surface==='water'?600:surface==='snow'?1100:450;
   const gn=this.ctx.createGain();
   gn.gain.setValueAtTime(surface==='water'?0.14:0.06,t);
   src.connect(filter);filter.connect(gn);gn.connect(this.ctx.destination);
   src.start(t);
  }catch(e){}
 }
 playThunder(){
  if(!this.enabled||!this.ctx)return;
  try{
   const t=this.ctx.currentTime,len=this.ctx.sampleRate*1.8;
   const buf=this.ctx.createBuffer(1,len,this.ctx.sampleRate);
   const d=buf.getChannelData(0);
   for(let i=0;i<len;i++)d[i]=(Math.random()*2-1)*Math.exp(-i/(this.ctx.sampleRate*0.6));
   const src=this.ctx.createBufferSource();src.buffer=buf;
   const filter=this.ctx.createBiquadFilter();
   filter.type='lowpass';filter.frequency.value=180;
   const gn=this.ctx.createGain();
   gn.gain.setValueAtTime(0.45,t);gn.gain.linearRampToValueAtTime(0.01,t+1.8);
   src.connect(filter);filter.connect(gn);gn.connect(this.ctx.destination);
   src.start(t);
  }catch(e){}
 }
}
const audio=new ProceduralAudio();
const initAudio=()=>{audio.init()};
addEventListener('pointerdown',initAudio,{once:true});
addEventListener('keydown',initAudio,{once:true});

let seed=11;const R=()=>(seed=(seed*16807)%2147483647)/2147483647;
const mix=(a,b,t)=>[Math.round(a[0]+(b[0]-a[0])*t),Math.round(a[1]+(b[1]-a[1])*t),Math.round(a[2]+(b[2]-a[2])*t)];
let currentHaze=[8,12,22],hazeMaxDist=125;
const col=(c,d,light=1.0)=>{
 const t=Math.min(.88,Math.max(0,(d-10)/hazeMaxDist));
 const r=Math.min(255,c[0]*light),g0=Math.min(255,c[1]*light),b=Math.min(255,c[2]*light);
 return`rgb(${Math.round(r+(currentHaze[0]-r)*t)},${Math.round(g0+(currentHaze[1]-g0)*t)},${Math.round(b+(currentHaze[2]-b)*t)})`;
};
const PAL=[[232,120,40],[240,160,50],[226,98,38],[246,190,70]];
const CABIN={x:0,z:48},POND={x:-42,z:24,rx:17,rz:17};
const MONOLITH={x:36,z:-48},SHRINE={x:-54,z:10},FAIRYRING={x:-24,z:-56};
const WATER=-.9,LAKE={x:-42,z:24},DES={x:68,z:-5},FOR={x:-10,z:-60};
const sm=(a,b,x)=>{const t=Math.max(0,Math.min(1,(x-a)/(b-a)));return t*t*(3-2*t)};
function wts(x,z){return[sm(26,9,Math.hypot(x-LAKE.x,z-LAKE.z)),sm(44,24,Math.hypot(x-DES.x,(z-DES.z)*.8)),sm(40,22,Math.hypot(x-FOR.x,z-FOR.z))]}
function ht(x,z){let h=2.6*Math.sin(x*.042+1)*Math.cos(z*.037)+1.2*Math.sin(x*.1+z*.085)+.5*Math.sin(x*.22-z*.17)+1.6;
 const w=wts(x,z);h+=w[1]*(2.4*Math.sin(x*.13+z*.04)*Math.sin(z*.09)+1.5)+w[2]*Math.sin(x*.07)*Math.cos(z*.08)*1.6;
 const fl=Math.max(sm(14,5,Math.hypot(x,z)),sm(14,6,Math.hypot(x-CABIN.x,z-CABIN.z)));h*=1-fl;
 return h*(1-w[0])-4*w[0]}
const inPond=(x,z,m=1)=>ht(x,z)<WATER+(m>1?.5:0);

// --- Seasonal Grids Precomputation ---
const GRID_N=512,GRID_MIN=-140,GRID_MAX=140,GRID_SCALE=(GRID_N-1)/(GRID_MAX-GRID_MIN);
const gridH=new Float32Array(GRID_N*GRID_N);
for(let iz=0;iz<GRID_N;iz++){const z=GRID_MIN+iz/GRID_SCALE;for(let ix=0;ix<GRID_N;ix++)gridH[iz*GRID_N+ix]=ht(GRID_MIN+ix/GRID_SCALE,z)}

function computeSeasonGrid(season){
 const buf=new Uint32Array(GRID_N*GRID_N);
 for(let iz=0;iz<GRID_N;iz++){
  const z=GRID_MIN+iz/GRID_SCALE;
  for(let ix=0;ix<GRID_N;ix++){
   const x=GRID_MIN+ix/GRID_SCALE,y=gridH[iz*GRID_N+ix],w=wts(x,z);
   const n=.5+.5*Math.sin(x*.33+z*.21)*Math.sin(z*.29-x*.1);
   const n2=.5+.5*Math.sin(x*.8+z*.3);
   let c;
   if(season==='spring'){
    c=mix(mix([118,185,82],[145,205,96],n),mix([65,125,62],[82,142,68],n),w[2]);
    c=mix(c,mix([215,198,148],[195,178,128],n2),w[1]);
    if(y<WATER+.5)c=mix(c,[225,212,160],.7);
   }else if(season==='summer'){
    c=mix(mix([88,162,65],[115,188,78],n),mix([52,110,55],[68,128,64],n),w[2]);
    c=mix(c,mix([225,195,130],[210,175,115],n2),w[1]);
    if(y<WATER+.5)c=mix(c,[230,210,155],.7);
   }else if(season==='autumn'){
    c=mix(mix([204,140,64],[228,176,88],n),mix([120,92,50],[100,112,56],n),w[2]);
    c=mix(c,mix([228,194,132],[212,172,110],n2),w[1]);
    if(y<WATER+.5)c=mix(c,[216,192,132],.7);
   }else{
    c=mix(mix([236,242,252],[222,234,248],n),mix([175,196,214],[155,178,198],n),w[2]);
    c=mix(c,mix([210,218,228],[195,204,216],n2),w[1]);
    if(y<WATER+.5)c=mix(c,[205,222,238],.85);
   }
   const ix2=Math.min(GRID_N-1,ix+3),iz2=Math.min(GRID_N-1,iz+2);
   const s=1+Math.max(-.25,Math.min(.25,(y-gridH[iz2*GRID_N+ix2])*.17));
   const cr=Math.min(255,Math.max(0,Math.round(c[0]*s))),cg=Math.min(255,Math.max(0,Math.round(c[1]*s))),cb=Math.min(255,Math.max(0,Math.round(c[2]*s)));
   buf[iz*GRID_N+ix]=(255<<24)|(cb<<16)|(cg<<8)|cr;
  }
 }
 return buf;
}

const SEASON_NAMES={spring:'🌸 Spring Valley',summer:'☀️ Summer Valley',autumn:'🍂 Autumn Valley',winter:'❄️ Winter Valley'};
const SEASONS=['spring','summer','autumn','winter'];
let currentSeason='autumn',autoSeason=false,seasonTimer=60.0;
const seasonGrids={
 spring:computeSeasonGrid('spring'),
 summer:computeSeasonGrid('summer'),
 autumn:computeSeasonGrid('autumn'),
 winter:computeSeasonGrid('winter')
};
let gridC=seasonGrids[currentSeason];

function sampleH(x,z){
 let gx=(x-GRID_MIN)*GRID_SCALE,gz=(z-GRID_MIN)*GRID_SCALE;
 if(gx<0)gx=0;else if(gx>GRID_N-2)gx=GRID_N-2;
 if(gz<0)gz=0;else if(gz>GRID_N-2)gz=GRID_N-2;
 const ix=gx|0,iz=gz|0,fx=gx-ix,fz=gz-iz,r0=iz*GRID_N,r1=r0+GRID_N;
 return(gridH[r0+ix]*(1-fx)+gridH[r0+ix+1]*fx)*(1-fz)+(gridH[r1+ix]*(1-fx)+gridH[r1+ix+1]*fx)*fz;
}
function sampleC(x,z){
 let gx=(x-GRID_MIN)*GRID_SCALE,gz=(z-GRID_MIN)*GRID_SCALE;
 if(gx<0)gx=0;else if(gx>GRID_N-1)gx=GRID_N-1;
 if(gz<0)gz=0;else if(gz>GRID_N-1)gz=GRID_N-1;
 return gridC[(gz|0)*GRID_N+(gx|0)];
}

let timeOfDay=0.5,autoTime=false;
let weather='clear',autoWeather=false,weatherTimer=30;
let lightningTimer=4.0,lightningFlash=0;

// Darker, moodier night settings (Midnight amb: 0.12, dark navy haze & sky)
const TOD_KEYS=[
 {t:0.0,haze:[8,12,22],sky:[[2,4,10],[5,10,22],[10,16,32]],amb:0.12,sun:0},
 {t:0.25,haze:[175,140,125],sky:[[38,48,82],[108,86,112],[240,172,122]],amb:0.72,sun:0.55},
 {t:0.5,haze:[238,196,150],sky:[[102,127,176],[169,169,180],[239,207,166]],amb:1.0,sun:1.0},
 {t:0.75,haze:[195,95,65],sky:[[50,36,92],[145,52,70],[235,120,60]],amb:0.80,sun:0.72},
 {t:1.0,haze:[8,12,22],sky:[[2,4,10],[5,10,22],[10,16,32]],amb:0.12,sun:0}
];
function getTOD(tm){
 tm=((tm%1)+1)%1;let i=0;
 while(i<TOD_KEYS.length-1&&TOD_KEYS[i+1].t<tm)i++;
 const k0=TOD_KEYS[i],k1=TOD_KEYS[i+1],f=(tm-k0.t)/(k1.t-k0.t);
 return{
  haze:mix(k0.haze,k1.haze,f),
  sky0:mix(k0.sky[0],k1.sky[0],f),
  sky1:mix(k0.sky[1],k1.sky[1],f),
  sky2:mix(k0.sky[2],k1.sky[2],f),
  amb:k0.amb+(k1.amb-k0.amb)*f,
  sun:k0.sun+(k1.sun-k0.sun)*f
 };
}

const stars=[];
for(let i=0;i<130;i++)stars.push({az:Math.random()*6.283,el:0.04+Math.random()*0.85,s:1+Math.random()*2.2,ph:Math.random()*6.28});
const raindrops=[];
for(let i=0;i<220;i++)raindrops.push({x:Math.random()*2000,y:Math.random()*1200,len:14+Math.random()*20,speed:750+Math.random()*450});
const splashes=[];
const fogBands=[];
for(let i=0;i<5;i++)fogBands.push({yFrac:0.38+i*0.12,speed:(i%2===0?1:-1)*(18+i*8),offset:Math.random()*1000,h:40+i*22,alpha:0.18+i*0.05});

function applyHaze(col32,r,lightFactor=1.0,lanternLight=0){
 let r0=col32&255,g0=(col32>>8)&255,b0=(col32>>16)&255;
 if(lightFactor<0.99||lanternLight>0){
  r0=Math.min(255,Math.round(r0*lightFactor+lanternLight*36));
  g0=Math.min(255,Math.round(g0*lightFactor+lanternLight*20));
  b0=Math.min(255,Math.round(b0*lightFactor));
 }
 const t=Math.min(.88,Math.max(0,(r-10)/hazeMaxDist));if(t<=0)return(255<<24)|(b0<<16)|(g0<<8)|r0;
 return(255<<24)|(Math.round(b0+(currentHaze[2]-b0)*t)<<16)|(Math.round(g0+(currentHaze[1]-g0)*t)<<8)|Math.round(r0+(currentHaze[0]-r0)*t);
}

function waterCol(x,z,yRaw,r,lightFactor=1.0,lanternLight=0){
 const dep=Math.min(1,(WATER-yRaw)/2.4);
 let cr,cg,cb;
 if(currentSeason==='winter'){
  cr=170-40*dep;cg=205-45*dep;cb=235-30*dep;
 }else{
  cr=128-82*dep;cg=182-90*dep;cb=200-72*dep;
 }
 if(Math.sin(x*2.1+T*1.7)*Math.sin(z*2.5-T*1.3)>.72){cr+=(255-cr)*.28;cg+=(255-cg)*.28;cb+=(255-cb)*.28}
 return applyHaze((255<<24)|(((cb|0))<<16)|(((cg|0))<<8)|(cr|0),r,lightFactor,lanternLight);
}

// RESTORED ORIGINAL CAMERA CONSTANTS (NO VERTICAL UPLIFT)
const CD=7,CH=3.4;
let camDist=7;
const F=()=>H*.95,hz=()=>H*.42;
let cam={x:0,z:0},camY=3.4,curB='';
const proj=(x,z)=>{const dx=x-cam.x,dz=z-cam.z,s=Math.sin(ca),c=Math.cos(ca);return[dx*c-dz*s,dx*s+dz*c]};

function terrain(){
 if(!offW||!offH)return;
 offBuf.fill(0);
 const Fo_off=offH*.95,h0_off=offH*.42;
 const curAmb=Math.min(1.0,getTOD(timeOfDay).amb+(lightningFlash>0?lightningFlash*0.8:0));
 const isNight=curAmb<0.75;
 const plX=player.x,plZ=player.z;
 for(let px=0;px<offW;px++){
  const da=Math.atan((px+.5-offW/2)/Fo_off),dx=Math.sin(ca+da),dz=Math.cos(ca+da),ck=Math.cos(da);
  let top=offH,r=1.5,prevY=sampleH(cam.x+dx*r,cam.z+dz*r),prevR=r,prevX=cam.x+dx*r,prevZ=cam.z+dz*r;
  while(r<140&&top>0){
   const x=cam.x+dx*r,z=cam.z+dz*r,yRaw=sampleH(x,z),wt=yRaw<WATER;
   let light=curAmb,lantern=0;
   if(isNight){
    const dPlSq=(x-plX)*(x-plX)+(z-plZ)*(z-plZ);
    if(dPlSq<169){
     const dPl=Math.sqrt(dPlSq);
     lantern=Math.max(0,1-dPl/13);
     light=Math.min(1.0,light+lantern*0.85);
    }
    const dCabSq=(x-CABIN.x)*(x-CABIN.x)+(z-CABIN.z)*(z-CABIN.z);
    if(dCabSq<256){
     const dCab=Math.sqrt(dCabSq);
     light=Math.min(1.0,light+Math.max(0,1-dCab/16)*(lit?0.7:0.4));
    }
   }
   if(prevR!==r&&((prevY<WATER)!==wt)){
    const tE=(WATER-prevY)/(yRaw-prevY),rE=prevR+tE*(r-prevR);
    const syE=Math.max(0,Math.floor(h0_off+(camY-WATER)*Fo_off/(rE*ck)));
    if(syE<top){
     const colE=prevY<WATER?waterCol(prevX,prevZ,prevY,rE,light,lantern):applyHaze(sampleC(prevX,prevZ),rE,light,lantern);
     for(let py=syE;py<top;py++)offBuf[py*offW+px]=colE;
     top=syE;
    }
   }
   const y=wt?WATER:yRaw,sy=Math.max(0,Math.floor(h0_off+(camY-y)*Fo_off/(r*ck)));
   if(sy<top){
    const colP=wt?waterCol(x,z,yRaw,r,light,lantern):applyHaze(sampleC(x,z),r,light,lantern);
    for(let py=sy;py<top;py++)offBuf[py*offW+px]=colP;
    top=sy;
   }
   prevY=yRaw;prevR=r;prevX=x;prevZ=z;
   r+=Math.max(.2,r*.022);
  }
 }
 offG.putImageData(offImg,0,0);
 g.imageSmoothingEnabled=true;
 g.imageSmoothingQuality='high';
 g.drawImage(offCv,0,0,W,H);
}

function seen(o){const ty=(o.y||0)+((o.t==='oak'||o.t==='pine'||o.t==='cabin'||o.t==='monolith')?3.2:.8),dx=o.x-cam.x,dz=o.z-cam.z;
 for(let i=1;i<8;i++){const t=i/8;if(sampleH(cam.x+dx*t,cam.z+dz*t)>camY+(ty-camY)*t+.15)return false}return true}
const objs=[];
function spot(minR,maxR,tall){for(;;){const r=minR+R()*(maxR-minR),a=R()*6.283,x=Math.cos(a)*r,z=Math.sin(a)*r;
 if(Math.hypot(x-CABIN.x,z-CABIN.z)<9||inPond(x,z,1.3)||Math.hypot(x,z)<5)continue;
 if(tall&&Math.abs(x)<4&&z>2&&z<44)continue;return[x,z]}}
function canopy(P){P=P||PAL;const a=[];for(let i=0;i<9;i++){const an=R()*6.28,rr=R()*1.9;a.push({dx:Math.cos(an)*rr,dy:Math.sin(an)*rr*.7+R()*.6,r:1.1+R()*.9,c:P[(R()*4)|0]})}return a.sort((p,q)=>p.dy-q.dy)}

const SEASON_OAKS={
 spring:[[255,185,198],[255,198,210],[250,160,185],[242,138,172]],
 summer:[[68,142,58],[85,160,70],[58,126,50],[98,174,78]],
 autumn:PAL,
 winter:[[245,248,255],[228,236,248],[210,224,240],[185,205,225]]
};
const FPAL=[[96,136,66],[120,150,70],[200,150,60],[222,120,44]];

for(let i=0;i<40;i++){const[x,z]=spot(8,96,1);objs.push({t:'oak',x,z,s:.8+R()*.55,r:.9,cn:canopy()})}
for(let i=0;i<95;i++){const[x,z]=spot(6,98,1);objs.push({t:'pine',x,z,s:.7+R()*.8,r:.7})}
for(let i=0;i<30;i++){const[x,z]=spot(5,95,1);objs.push({t:'rock',x,z,s:.5+R()*.8,r:.6})}
for(let i=0;i<520;i++){const[x,z]=spot(1,95,0);objs.push({t:'speck',x,z,c:[[255,230,150],[255,255,255],[240,150,70]][(R()*3)|0]})}
const leaves=[];for(let i=0;i<12;i++){const[x,z]=spot(14,88,0);const o={t:'leaf',x,z,got:0,ph:R()*6};leaves.push(o);objs.push(o)}
objs.push({t:'cabin',x:CABIN.x,z:CABIN.z,r:4.6});
objs.push({t:'monolith',x:MONOLITH.x,z:MONOLITH.z,r:2.0});
objs.push({t:'shrine',x:SHRINE.x,z:SHRINE.z,r:2.2});
objs.push({t:'fairyring',x:FAIRYRING.x,z:FAIRYRING.z,r:1.8});

const animalList=[],KINDS=[['bunny',8.5,7],['fox',10.5,4],['hedgehog',4.5,4]];let caughtN=0;
for(const[kind,fast,n]of KINDS)for(let i=0;i<n;i++){const[x,z]=spot(12,90,0);const o={t:'animal',kind,fast,x,z,ang:R()*6.28,tm:0,go:0,hp:R()*6,gone:0,vx:0,vz:0,ph:R()*6,dir:1};animalList.push(o);objs.push(o)}
for(const[kind,fast,n]of[['glimmerpuff',9,3],['moonbun',10,3],['sunwisp',11,1]])for(let i=0;i<n;i++){const[x,z]=spot(15,90,0);const o={t:'animal',kind,fast,mystic:1,x,z,ang:R()*6.28,tm:0,go:0,hp:R()*6,gone:0,vx:0,vz:0,ph:R()*6,dir:1};animalList.push(o);objs.push(o)}
for(let i=objs.length-1;i>=0;i--){const o=objs[i];if(((o.t==='oak'||o.t==='pine')&&wts(o.x,o.z)[1]>.4)||(o.t==='speck'&&wts(o.x,o.z)[1]>.3))objs.splice(i,1)}

function put(n,ok,mk){let c=0,t=0;while(c<n&&t++<6000){const x=(R()*2-1)*96,z=(R()*2-1)*96;if(Math.hypot(x,z)>96||inPond(x,z,1.3)||!ok(wts(x,z)))continue;const o=mk();o.x=x;o.z=z;objs.push(o);c++}}
put(36,w=>w[1]>.5,()=>({t:'cactus',s:.8+R()*.7,r:.5}));
put(30,w=>w[1]>.4,()=>({t:'shrub',s:.7+R()*.6}));
put(150,w=>w[2]>.4&&w[1]<.3,()=>({t:'pine',s:.8+R()*1,r:.7}));
put(45,w=>w[2]>.4&&w[1]<.3,()=>({t:'oak',s:.9+R()*.6,r:.9,cn:canopy(FPAL)}));

const spiritWisps=[]; // Flying guidance particles from monolith

const player={t:'player',x:0,z:0};objs.push(player);
for(const o of objs)o.y=sampleH(o.x,o.z);

let jh=0,pjv=0,jumpLatch=0,tapJump=0;const pw={speed:0,jump:0,starlight:0,lakeStrider:0};
let a=0,ca=0,walk=0,moving=0,started=false,won=false,lit=false,got=0,T=0,toastT=0;
let inCabin=false,hearthLeaves=0;
const keys={};addEventListener('keydown',e=>{keys[e.code]=1});addEventListener('keyup',e=>{keys[e.code]=0});
const ptr={};let joy=null;

// Clean, natural horizontal camera rotation
cv.addEventListener('pointerdown',e=>{cv.setPointerCapture(e.pointerId);
 ptr[e.pointerId]={x:e.clientX,y:e.clientY,x0:e.clientX,t0:performance.now(),t:e.pointerType==='touch'&&e.clientX<W*.5?'joy':'look'};
 if(ptr[e.pointerId].t==='joy')joy={ox:e.clientX,oy:e.clientY,x:e.clientX,y:e.clientY,id:e.pointerId}});
cv.addEventListener('pointermove',e=>{const p=ptr[e.pointerId];if(!p)return;
 if(p.t==='joy'){
  joy.x=e.clientX;joy.y=e.clientY;
 }else{
  const dx=e.clientX-p.x;
  ca+=dx*0.0055;
  p.x=e.clientX;p.y=e.clientY;
 }});
const up=e=>{const p=ptr[e.pointerId];if(p&&p.t==='look'&&Math.abs(e.clientX-p.x0)<8&&performance.now()-p.t0<250)tapJump=1;if(joy&&joy.id===e.pointerId)joy=null;delete ptr[e.pointerId]};
cv.addEventListener('pointerup',up);cv.addEventListener('pointercancel',up);

const toast=t=>{const el=document.getElementById('toast');el.textContent=t;el.style.opacity=1;toastT=2.4};

const parts=[];for(let i=0;i<55;i++)parts.push({x:Math.random()*2000,y:Math.random()*1200,s:3+Math.random()*4,p:Math.random()*6,c:PAL[(Math.random()*4)|0]});
const bursts=[];
let fpsCount=0,fpsTime=0;

function setSeason(s,silent=false){
 if(!SEASONS.includes(s))return;
 currentSeason=s;
 gridC=seasonGrids[s];
 document.querySelectorAll('#season-btns button').forEach(b=>{
  b.classList.toggle('active',b.dataset.s===s);
 });
 document.getElementById('season-hud').textContent=SEASON_NAMES[s];
 if(!silent)toast('Season shifting to '+SEASON_NAMES[s]);
}

function update(dt){
 T+=dt;
 fpsCount++;fpsTime+=dt;
 if(fpsTime>=0.5){
  const curFps=Math.round(fpsCount/fpsTime);
  fpsCount=0;fpsTime=0;
  const el=document.getElementById('fps-display');
  if(el)el.textContent=`FPS: ${curFps} | Resolution: ${offW}×${offH}`;
 }

 if(autoSeason){
  seasonTimer-=dt;
  if(seasonTimer<=0){
   seasonTimer=50.0;
   const nextIdx=(SEASONS.indexOf(currentSeason)+1)%SEASONS.length;
   setSeason(SEASONS[nextIdx]);
  }
 }

 if(autoTime)timeOfDay=(timeOfDay+dt*0.011)%1.0;
 if(autoWeather){
  weatherTimer-=dt;
  if(weatherTimer<=0){
   weatherTimer=24+Math.random()*20;
   const wl=['clear','fog','rain','storm'];
   setWeather(wl[(wl.indexOf(weather)+1+((Math.random()*2)|0))%wl.length]);
  }
 }
 if(weather==='storm'){
  lightningTimer-=dt;
  if(lightningTimer<=0){
   lightningFlash=1.0;lightningTimer=3.5+Math.random()*5.0;
   audio.playThunder();
  }
 }
 if(lightningFlash>0)lightningFlash=Math.max(0,lightningFlash-dt*3.8);

 if((keys.Space||tapJump)&&!jumpLatch&&jh<=0){
  pjv=pw.jump>0?13:7.2;jumpLatch=1;
  audio.playTone(320,'sine',0.15,0.1);
 }
 if(!keys.Space)jumpLatch=0;tapJump=0;jh+=pjv*dt;pjv-=22*dt;if(jh<=0){jh=0;pjv=0}

 pw.speed=Math.max(0,pw.speed-dt);
 pw.jump=Math.max(0,pw.jump-dt);
 pw.starlight=Math.max(0,pw.starlight-dt);
 pw.lakeStrider=Math.max(0,pw.lakeStrider-dt);

 {
  const t=[];
  if(pw.speed>0)t.push('Swift '+Math.ceil(pw.speed)+'s');
  if(pw.jump>0)t.push('Moon leap '+Math.ceil(pw.jump)+'s');
  if(pw.lakeStrider>0)t.push('Lake Strider '+Math.ceil(pw.lakeStrider)+'s');
  if(pw.starlight>0)t.push('Starlight Sight '+Math.ceil(pw.starlight)+'s');
  document.getElementById('pw').textContent=t.join('   ');
 }

 let fx=0,fz=0,sp=(keys.ShiftLeft||keys.ShiftRight)?1.75:1;
 if(keys.KeyW) { fx+=Math.sin(ca); fz+=Math.cos(ca); }
 if(keys.KeyS) { fx-=Math.sin(ca); fz-=Math.cos(ca); }
 if(keys.KeyA) { fx-=Math.cos(ca); fz+=Math.sin(ca); }
 if(keys.KeyD) { fx+=Math.cos(ca); fz-=Math.sin(ca); }
 if(keys.ArrowUp)   { fx+=Math.sin(ca); fz+=Math.cos(ca); }
 if(keys.ArrowDown) { fx-=Math.sin(ca); fz-=Math.cos(ca); }
 if(keys.ArrowLeft)  ca-=dt*2.2;
 if(keys.ArrowRight) ca+=dt*2.2;

 if(joy){
  const jx=(joy.x-joy.ox)/55,jy=(joy.y-joy.oy)/55,jLen=Math.hypot(jx,jy);
  if(jLen>0.15){
   const c=Math.cos(ca),s=Math.sin(ca);
   fx=jx*c-jy*s;fz=-jx*s-jy*c;
   sp=jLen>1.3?1.75:1;
  }
 }
 if(!started){ca+=dt*0.12;}
 const mLen=Math.hypot(fx,fz);
 if(mLen>0.05){
  const nx=fx/mLen,nz=fz/mLen,tAngle=Math.atan2(nx,nz);
  let da=tAngle-a;da=Math.atan2(Math.sin(da),Math.cos(da));
  a+=da*Math.min(1,dt*12);
  const onWater=inPond(player.x,player.z);
  const slow=(onWater&&pw.lakeStrider<=0)?.45:1;
  const v=7.2*sp*slow*(pw.speed>0?1.75:1);
  player.x+=nx*v*dt;player.z+=nz*v*dt;
  moving=1;walk+=v*dt*1.5;
  if(jh<=0.1){
   audio.playStep(onWater?'water':currentSeason==='winter'?'snow':'grass');
  }
 }else{
  moving=0;
 }

 for(const o of objs){
  if(!o.r||(o.t==='rock'&&jh>.8))continue;
  const dx=player.x-o.x,dz=player.z-o.z,d=Math.hypot(dx,dz),m=o.r+.45;
  if(d<m&&d>.001){player.x=o.x+dx/d*m;player.z=o.z+dz/d*m}
 }
 const rd=Math.hypot(player.x,player.z);if(rd>98){player.x*=98/rd;player.z*=98/rd}
 player.y=ht(player.x,player.z);

 {
  const w=wts(player.x,player.z),b=w[0]>.5?'the lake shore':w[1]>.5?'the dusty desert':w[2]>.5?'the old forest':'the meadow';
  if(b!==curB){curB=b;if(started)toast('Entering '+b)}
 }

 // EXACT ORIGINAL CAMERA (NO VERTICAL UPLIFT)
 cam.x=player.x-Math.sin(ca)*camDist;
 cam.z=player.z-Math.cos(ca)*camDist;
 camY+=(Math.max(player.y+CH+jh*.4,sampleH(cam.x,cam.z)+1.4)-camY)*Math.min(1,dt*5);

 updateInteractionPrompts();
 animals(dt);

 for(const l of leaves)if(!l.got&&Math.hypot(player.x-l.x,player.z-l.z)<2.2){
  l.got=1;got++;document.getElementById('n').textContent=got;
  audio.playChime([523,659,784,1046]);
  for(let i=0;i<16;i++)bursts.push({x:W/2,y:H*.62,vx:(Math.random()-.5)*420,vy:-Math.random()*400,l:1});
  if(got<12)toast(got+' of 12 leaves found');else{toast('All 12 found! Carry them to the cabin hearth!');document.getElementById('obj').textContent='Bring them to the cabin'}
 }
 if(got>=12&&!won&&Math.hypot(player.x-CABIN.x,player.z-CABIN.z)<9){
  won=lit=true;document.getElementById('win').hidden=false;document.getElementById('obj').textContent='The hearth is lit';
  audio.playChime([440,554,659,880,1108],0.6);
 }

 if(toastT>0&&(toastT-=dt)<=0)document.getElementById('toast').style.opacity=0;

 const stormWind=weather==='storm'?-90:weather==='rain'?-40:-25;
 for(const p of parts){
  p.y+=(26+p.s*7*(weather==='storm'?1.8:1))*dt;
  p.x+=(Math.sin(T*1.5+p.p)*28+stormWind)*dt;
  if(p.y>H+10){p.y=-10;p.x=Math.random()*W}
  if(p.x<-10)p.x=W+10;
 }
 for(const b of bursts){b.x+=b.vx*dt;b.y+=b.vy*dt;b.vy+=700*dt;b.l-=dt*1.3}
 while(bursts.length&&bursts[0].l<=0)bursts.shift();

 for(let i=spiritWisps.length-1;i>=0;i--){
  const w=spiritWisps[i];
  w.life-=dt*0.8;
  if(w.life<=0){spiritWisps.splice(i,1);continue}
  const wdx=w.tx-w.x,wdz=w.tz-w.z,wd=Math.hypot(wdx,wdz);
  if(wd>1.5){
   w.x+=wdx/wd*18*dt+Math.sin(T*6+w.ph)*5*dt;
   w.z+=wdz/wd*18*dt+Math.cos(T*6+w.ph)*5*dt;
   w.y=ht(w.x,w.z)+2.0+Math.sin(T*4+w.ph)*0.8;
  }
 }
}

let activePromptAction=null;
function updateInteractionPrompts(){
 const promptBtn=document.getElementById('interact-prompt');
 if(!promptBtn)return;
 if(!started||inCabin){promptBtn.hidden=true;return}
 
 const dCabin=Math.hypot(player.x-CABIN.x,player.z-CABIN.z);
 const dMono=Math.hypot(player.x-MONOLITH.x,player.z-MONOLITH.z);
 const dShrine=Math.hypot(player.x-SHRINE.x,player.z-SHRINE.z);
 const dRing=Math.hypot(player.x-FAIRYRING.x,player.z-FAIRYRING.z);

 if(dRing<2.6){
  if(jh<=0.2){
   jh=1.2;pjv=17;
   audio.playSpring();
   toast('✨ Fairy Mushroom Spring! Soaring high!');
   for(let i=0;i<18;i++)bursts.push({x:W/2,y:H*.55,vx:(Math.random()-.5)*350,vy:-Math.random()*420,l:1,c:'#d27eff'});
  }
  promptBtn.hidden=true;
  activePromptAction=null;
  return;
 }

 if(dCabin<8.5){
  promptBtn.textContent='🏡 Enter Cabin (Press E)';
  promptBtn.hidden=false;
  activePromptAction='cabin';
 }else if(dMono<6.5){
  promptBtn.textContent='✨ Listen to Whispering Monolith (Press E)';
  promptBtn.hidden=false;
  activePromptAction='monolith';
 }else if(dShrine<6.5){
  promptBtn.textContent='🌙 Pray at Moon Shrine (Press E)';
  promptBtn.hidden=false;
  activePromptAction='shrine';
 }else{
  promptBtn.hidden=true;
  activePromptAction=null;
 }
}

function activateInteraction(){
 if(activePromptAction==='cabin')openCabin();
 else if(activePromptAction==='monolith')activateMonolith();
 else if(activePromptAction==='shrine')activateShrine();
}
document.getElementById('interact-prompt').onclick=activateInteraction;

function activateMonolith(){
 audio.playEthereal(520);
 let nearest=null,minD=999999;
 for(const l of leaves){
  if(!l.got){
   const d=Math.hypot(l.x-player.x,l.z-player.z);
   if(d<minD){minD=d;nearest=l}
  }
 }
 if(nearest){
  pw.starlight=28;
  spiritWisps.length=0;
  for(let i=0;i<12;i++){
   spiritWisps.push({
    x:MONOLITH.x+(Math.random()-0.5)*2,
    y:ht(MONOLITH.x,MONOLITH.z)+3,
    z:MONOLITH.z+(Math.random()-0.5)*2,
    tx:nearest.x,tz:nearest.z,
    life:1.0,ph:i*0.5
   });
  }
  toast(`✨ The Monolith speaks: 'A spirit wisp flies toward a leaf (~${Math.round(minD)} paces away)!'`);
 }else{
  toast('✨ The Monolith resonates: All 12 leaves are gathered!');
 }
}

function activateShrine(){
 audio.playEthereal(440);
 pw.lakeStrider=50;
 toast('🌙 Blessed by the Moon Shrine! You can sprint across the lake waters!');
 for(let i=0;i<16;i++)bursts.push({x:W/2,y:H*.55,vx:(Math.random()-.5)*340,vy:-Math.random()*380,l:1,c:'#68d8d6'});
}

function hillH(an,k){return Math.sin(an*3+k)*.5+Math.sin(an*7+k*2)*.3+Math.sin(an*13+k*3)*.2}

const SEASON_HILLS={
 spring:[[120,170,115],[140,185,130],[165,205,148]],
 summer:[[95,155,90],[115,172,105],[138,192,120]],
 autumn:[[200,166,140],[214,172,128],[226,182,132]],
 winter:[[210,225,240],[225,235,248],[238,245,255]]
};

function sky(){
 const h=hz(),tod=getTOD(timeOfDay);
 let sky0=tod.sky0,sky1=tod.sky1,sky2=tod.sky2;
 currentHaze=[...tod.haze];hazeMaxDist=125;

 if(weather==='fog'){
  sky0=mix(sky0,[205,212,218],.5);sky1=mix(sky1,[195,202,208],.55);sky2=mix(sky2,[185,192,198],.6);
  currentHaze=mix(currentHaze,[200,208,214],.7);hazeMaxDist=45;
 }else if(weather==='rain'){
  sky0=mix(sky0,[85,100,120],.5);sky1=mix(sky1,[115,125,135],.5);sky2=mix(sky2,[140,145,150],.5);
  currentHaze=mix(currentHaze,[130,140,150],.6);hazeMaxDist=75;
 }else if(weather==='storm'){
  sky0=mix(sky0,[22,25,38],.75);sky1=mix(sky1,[34,36,48],.75);sky2=mix(sky2,[48,49,60],.75);
  currentHaze=mix(currentHaze,[38,40,52],.8);hazeMaxDist=52;
 }

 if(lightningFlash>0){
  const lf=lightningFlash*.65;
  sky0=mix(sky0,[235,245,255],lf);sky1=mix(sky1,[235,245,255],lf);sky2=mix(sky2,[235,245,255],lf);
  currentHaze=mix(currentHaze,[240,248,255],lf);
 }

 const gr=g.createLinearGradient(0,0,0,h);
 gr.addColorStop(0,`rgb(${sky0.join(',')})`);
 gr.addColorStop(.6,`rgb(${sky1.join(',')})`);
 gr.addColorStop(1,`rgb(${sky2.join(',')})`);
 g.fillStyle=gr;g.fillRect(0,0,W,h+2);

 const starVis=(1-tod.sun)*(weather==='storm'||weather==='rain'?0.05:weather==='fog'?0.3:1.0);
 if(starVis>0.08){
  for(const s of stars){
   const d=Math.atan2(Math.sin(s.az-ca),Math.cos(s.az-ca));
   if(Math.abs(d)<1.35){
    const sx=W/2+Math.tan(d)*F(),sy=h-s.el*H*.9;
    if(sy>4&&sy<h){
     const tw=.6+.4*Math.sin(T*3+s.ph);
     g.fillStyle=`rgba(255,255,255,${starVis*tw*.9})`;
     g.fillRect(sx,sy,s.s,s.s);
    }
   }
  }
 }

 const isSun=tod.sun>.15,bodyAz=.7+(isSun?0:Math.PI),diff=Math.atan2(Math.sin(bodyAz-ca),Math.cos(bodyAz-ca));
 if(Math.abs(diff)<1.3&&weather!=='storm'){
  const bx=W/2+Math.tan(diff)*F(),by=h-H*(isSun?.18+tod.sun*.16:.26);
  if(isSun){
   const sAlpha=tod.sun*(weather==='rain'?.3:weather==='fog'?.5:1);
   const sg=g.createRadialGradient(bx,by,5,bx,by,H*.35);
   sg.addColorStop(0,`rgba(255,240,200,${.85*sAlpha})`);sg.addColorStop(1,'rgba(255,220,170,0)');
   g.fillStyle=sg;g.fillRect(0,0,W,h);
  }else{
   const mg=g.createRadialGradient(bx,by,6,bx,by,H*.22);
   mg.addColorStop(0,'rgba(215,232,255,.45)');mg.addColorStop(1,'rgba(200,225,255,0)');
   g.fillStyle=mg;g.fillRect(0,0,W,h);
   g.fillStyle='#eaf2ff';g.beginPath();g.arc(bx,by,17,0,7);g.fill();
   g.fillStyle=`rgb(${sky1.join(',')})`;g.beginPath();g.arc(bx+6,by-3,14,0,7);g.fill();
  }
 }

 const cloudAlpha=weather==='storm'?.8:weather==='rain'?.65:weather==='fog'?.35:.45;
 const cloudCol=weather==='storm'?'38,40,52':weather==='rain'?'135,145,158':(tod.sun>.4?'255,255,255':'85,96,120');
 g.fillStyle=`rgba(${cloudCol},${cloudAlpha})`;
 for(let i=0;i<6;i++){
  const az=i*1.05+T*(weather==='storm'?.035:.01),d=Math.atan2(Math.sin(az-ca),Math.cos(az-ca));
  if(Math.abs(d)>1.3)continue;
  const x=W/2+Math.tan(d)*F(),y=H*(.08+.05*((i*37)%5)/5);
  for(let j=0;j<4;j++){g.beginPath();g.arc(x+j*38-60,y+(j%2)*10,34+j*6%16,0,7);g.fill()}
 }

 const hillPals=SEASON_HILLS[currentSeason]||SEASON_HILLS.autumn;
 const L=[[.6,0,70,mix(hillPals[0],currentHaze,.35)],
          [1.7,2,46,mix(hillPals[1],currentHaze,.25)],
          [2.9,5,26,mix(hillPals[2],currentHaze,.15)]];
 for(const[ph,k,A,c]of L){
  g.fillStyle=`rgb(${c.join(',')})`;g.beginPath();g.moveTo(0,h+2);
  for(let x=0;x<=W+8;x+=8){const an=ca+Math.atan((x-W/2)/F());g.lineTo(x,h-8-A*(hillH(an,ph+k)*.5+.5))}
  g.lineTo(W,h+2);g.fill();
 }

 const gBase0=mix(hillPals[0],currentHaze,.45),gBase1=mix(hillPals[1],currentHaze,.35),gBase2=mix(hillPals[2],currentHaze,.25);
 const gg=g.createLinearGradient(0,h,0,H);
 gg.addColorStop(0,`rgb(${gBase0.join(',')})`);gg.addColorStop(.35,`rgb(${gBase1.join(',')})`);gg.addColorStop(1,`rgb(${gBase2.join(',')})`);
 g.fillStyle=gg;g.fillRect(0,h,W,H-h);
}

function drawObj(o,sx,gy,k,d){
 const dPl=Math.hypot(o.x-player.x,o.z-player.z);
 const isNight=getTOD(timeOfDay).sun<0.6;
 const objLight=Math.min(1.0,getTOD(timeOfDay).amb+(lightningFlash>0?lightningFlash*0.8:0)+(isNight&&dPl<13?(1-dPl/13)*0.85:0));

 switch(o.t){
 case'oak':{
  const s=o.s;
  // Contact grounding shadow
  g.fillStyle='rgba(38,20,10,.35)';
  g.beginPath();g.ellipse(sx,gy,1.5*s*k,0.42*s*k,0,0,7);g.fill();
  // Oak trunk with root flare anchoring into the terrain
  const trunkCol=col([100,64,52],d,objLight);
  g.fillStyle=trunkCol;
  g.beginPath();
  g.moveTo(sx-.22*s*k, gy-4.8*s*k);
  g.lineTo(sx+.22*s*k, gy-4.8*s*k);
  g.lineTo(sx+.26*s*k, gy-.3*s*k);
  g.quadraticCurveTo(sx+.42*s*k, gy, sx+.55*s*k, gy+.22*s*k);
  g.lineTo(sx-.55*s*k, gy+.22*s*k);
  g.quadraticCurveTo(sx-.42*s*k, gy, sx-.26*s*k, gy-.3*s*k);
  g.closePath();
  g.fill();
  const oakColors=SEASON_OAKS[currentSeason]||PAL;
  for(let idx=0;idx<o.cn.length;idx++){
   const c=o.cn[idx],cx=sx+c.dx*s*k,cy=gy-(5.2+c.dy)*s*k,r=c.r*s*k;
   const clr=oakColors[idx%oakColors.length];
   g.fillStyle=col(clr,d,objLight);g.beginPath();g.arc(cx,cy,r,0,7);g.fill();
   g.fillStyle='rgba(255,235,170,.3)';g.beginPath();g.arc(cx-r*.25,cy-r*.25,r*.55,0,7);g.fill();
  }
  break;
 }
 case'pine':{
  const s=o.s;
  // Contact grounding shadow
  g.fillStyle='rgba(38,20,10,.32)';
  g.beginPath();g.ellipse(sx,gy,1.1*s*k,0.32*s*k,0,0,7);g.fill();
  // Sturdy pine trunk with root flare extending into the ground
  const trunkCol=col([88,58,42],d,objLight);
  g.fillStyle=trunkCol;
  g.beginPath();
  g.moveTo(sx-.16*s*k, gy-1.4*s*k);
  g.lineTo(sx+.16*s*k, gy-1.4*s*k);
  g.lineTo(sx+.20*s*k, gy-.2*s*k);
  g.quadraticCurveTo(sx+.32*s*k, gy, sx+.42*s*k, gy+.2*s*k);
  g.lineTo(sx-.42*s*k, gy+.2*s*k);
  g.quadraticCurveTo(sx-.32*s*k, gy, sx-.20*s*k, gy-.2*s*k);
  g.closePath();
  g.fill();
  for(let i=0;i<3;i++){
   const by=gy-(.85+i*1.6)*s*k,w=(1.5-i*.35)*s*k;
   let pColor=currentSeason==='winter'?(i%2?[180,210,225]:[140,175,190]):(i%2?[78,116,78]:[62,100,70]);
   g.fillStyle=col(pColor,d,objLight);
   g.beginPath();g.moveTo(sx-w,by);g.lineTo(sx,by-2.4*s*k);g.lineTo(sx+w,by);g.fill();
   if(currentSeason==='winter'){
    g.fillStyle=col([245,250,255],d,objLight);
    g.beginPath();g.moveTo(sx-w*.6,by-1.1*s*k);g.lineTo(sx,by-2.4*s*k);g.lineTo(sx+w*.6,by-1.1*s*k);g.fill();
   }
  }
  break;
 }
 case'rock':{
  g.fillStyle=col([150,132,120],d,objLight);g.beginPath();g.ellipse(sx,gy-.3*o.s*k,.8*o.s*k,.5*o.s*k,0,0,7);g.fill();
  g.fillStyle=currentSeason==='winter'?'rgba(240,245,255,.55)':'rgba(255,255,255,.2)';
  g.beginPath();g.ellipse(sx-.2*o.s*k,gy-.45*o.s*k,.4*o.s*k,.2*o.s*k,0,0,7);g.fill();
  break;
 }
 case'speck':{
  if(d>38)break;
  let spCol=o.c;
  if(currentSeason==='spring')spCol=[[255,185,200],[210,180,240],[255,255,255]][((o.x*13)%3)|0];
  else if(currentSeason==='winter')spCol=[[245,250,255],[220,235,250],[255,255,255]][((o.x*7)%3)|0];
  g.fillStyle=col(spCol,d,objLight);g.beginPath();g.arc(sx,gy,Math.max(1,.07*k),0,7);g.fill();
  break;
 }
 case'leaf':{
  if(o.got)break;
  const y=gy-(1.2+Math.sin(T*2+o.ph)*.25)*k,r=.55*k;
  const gr=g.createRadialGradient(sx,y,0,sx,y,r*3.2);
  gr.addColorStop(0,'rgba(255,220,120,.85)');gr.addColorStop(1,'rgba(255,200,90,0)');
  g.fillStyle=gr;g.fillRect(sx-r*3.2,y-r*3.2,r*6.4,r*6.4);

  if(pw.starlight>0){
   const beamGrad=g.createLinearGradient(sx,y-140,sx,y);
   beamGrad.addColorStop(0,'rgba(160,230,255,0)');
   beamGrad.addColorStop(0.5,'rgba(160,230,255,0.4)');
   beamGrad.addColorStop(1,'rgba(255,220,120,0.85)');
   g.fillStyle=beamGrad;g.fillRect(sx-3,y-140,6,140);
  }

  g.save();g.translate(sx,y);g.rotate(T*1.5+o.ph);g.scale(Math.cos(T*2+o.ph)*.6+.7,1);
  g.fillStyle='#ffb43a';g.beginPath();g.ellipse(0,0,r*.55,r,0,0,7);g.fill();
  g.strokeStyle='#c2561f';g.lineWidth=Math.max(1,r*.12);g.beginPath();g.moveTo(0,-r);g.lineTo(0,r);g.stroke();
  g.restore();break;
 }
 case'monolith':{
  const s=o.s||1.4;
  g.fillStyle=col([95,98,115],d,objLight);
  g.beginPath();g.moveTo(sx-0.9*s*k,gy);g.lineTo(sx-0.6*s*k,gy-7.5*s*k);g.lineTo(sx,gy-8.5*s*k);g.lineTo(sx+0.6*s*k,gy-7.5*s*k);g.lineTo(sx+0.9*s*k,gy);g.fill();
  const runePulse=0.5+0.5*Math.sin(T*3);
  g.strokeStyle=`rgba(120,225,255,${0.6+runePulse*0.35})`;g.lineWidth=Math.max(1,0.12*k);
  g.beginPath();g.moveTo(sx,gy-1.5*s*k);g.lineTo(sx,gy-6.8*s*k);g.stroke();
  for(let i=0;i<4;i++){
   const ry=gy-(2.2+i*1.3)*s*k;
   g.strokeRect(sx-0.2*s*k,ry,0.4*s*k,0.2*s*k);
  }
  const cy=gy-(9.2+Math.sin(T*2.5)*0.3)*s*k;
  g.fillStyle='#9cf0ff';g.beginPath();g.moveTo(sx,cy-0.7*s*k);g.lineTo(sx+0.4*s*k,cy);g.lineTo(sx,cy+0.7*s*k);g.lineTo(sx-0.4*s*k,cy);g.fill();
  break;
 }
 case'shrine':{
  g.fillStyle=col([130,135,145],d,objLight);
  g.beginPath();g.ellipse(sx,gy-0.3*k,1.6*k,0.8*k,0,0,7);g.fill();
  const sg=g.createRadialGradient(sx,gy-0.35*k,0,sx,gy-0.35*k,1.4*k);
  sg.addColorStop(0,'rgba(110,235,245,.85)');sg.addColorStop(1,'rgba(50,140,180,.6)');
  g.fillStyle=sg;g.beginPath();g.ellipse(sx,gy-0.35*k,1.3*k,0.65*k,0,0,7);g.fill();
  g.fillStyle='#ffc4e0';g.beginPath();g.arc(sx,gy-0.45*k,0.35*k,0,7);g.fill();
  break;
 }
 case'fairyring':{
  for(let i=0;i<7;i++){
   const an=i*(6.28/7)+T*0.5,mx=sx+Math.cos(an)*1.3*k,my=gy-0.2*k+Math.sin(an)*0.5*k;
   g.fillStyle='rgba(210,130,255,.9)';g.beginPath();g.arc(mx,my-0.3*k,0.25*k,Math.PI,0);g.fill();
   g.fillStyle='#fff';g.fillRect(mx-0.05*k,my-0.3*k,0.1*k,0.3*k);
  }
  break;
 }
 case'cabin':{
  const x=sx-3.5*k,wy=gy-3.5*k;g.fillStyle=col([176,120,78],d,objLight);g.fillRect(x,wy,7*k,3.5*k);
  g.strokeStyle='rgba(80,40,20,.35)';g.lineWidth=Math.max(1,.05*k);for(let i=1;i<7;i++){g.beginPath();g.moveTo(x,wy+i*.5*k);g.lineTo(x+7*k,wy+i*.5*k);g.stroke()}
  g.fillStyle=col([110,70,60],d,objLight);g.fillRect(sx+1.5*k,gy-7*k,.9*k,2.4*k);
  g.fillStyle=col([146,76,66],d,objLight);g.beginPath();g.moveTo(sx-4.7*k,wy+.1*k);g.lineTo(sx,gy-6.6*k);g.lineTo(sx+4.7*k,wy+.1*k);g.fill();
  const isDark=getTOD(timeOfDay).sun<.45||weather==='storm';
  g.fillStyle=(lit||isDark)?'#ffd778':col([176,196,208],d,objLight);g.fillRect(sx-2.4*k,gy-2.6*k,1.3*k,1.2*k);
  if(lit||isDark){
   const gr=g.createRadialGradient(sx-1.75*k,gy-2*k,0,sx-1.75*k,gy-2*k,4*k);
   gr.addColorStop(0,'rgba(255,200,100,.55)');gr.addColorStop(1,'rgba(255,200,100,0)');
   g.fillStyle=gr;g.fillRect(sx-6*k,gy-6*k,8*k,8*k);
  }
  g.fillStyle=col([98,60,48],d,objLight);g.fillRect(sx+.9*k,gy-2.5*k,1.4*k,2.5*k);
  const n=lit?9:4;for(let i=0;i<n;i++){const p=(T*.25+i/n)%1;g.fillStyle=`rgba(245,240,235,${(1-p)*(lit?.5:.3)})`;g.beginPath();g.arc(sx+1.95*k+Math.sin(p*5+i)*.5*k+p*k,gy-7.2*k-p*3.5*k,(.3+p*.7)*k,0,7);g.fill()}
  break;
 }
 case'cactus':{
  const s=o.s;
  g.fillStyle='rgba(38,20,10,.25)';g.beginPath();g.ellipse(sx,gy,0.55*s*k,0.18*s*k,0,0,7);g.fill();
  const c=col([84,138,84],d,objLight),w=.42*s*k;g.fillStyle=c;g.beginPath();g.roundRect(sx-w/2,gy-3.2*s*k,w,3.2*s*k+0.15*s*k,w/2);g.fill();
  g.strokeStyle=c;g.lineWidth=.3*s*k;g.lineCap='round';g.beginPath();g.moveTo(sx-.2*s*k,gy-1.4*s*k);g.lineTo(sx-.8*s*k,gy-1.4*s*k);g.lineTo(sx-.8*s*k,gy-2.3*s*k);g.moveTo(sx+.2*s*k,gy-1.9*s*k);g.lineTo(sx+.75*s*k,gy-1.9*s*k);g.lineTo(sx+.75*s*k,gy-2.6*s*k);g.stroke();
  g.fillStyle='rgba(255,240,200,.25)';g.fillRect(sx-.05*s*k,gy-3*s*k,.08*s*k,2.8*s*k);break;
 }
 case'shrub':{
  const s=o.s;
  g.fillStyle='rgba(38,20,10,.25)';g.beginPath();g.ellipse(sx,gy,0.7*s*k,0.22*s*k,0,0,7);g.fill();
  for(const[dx,dy,r,cl]of[[-.4,.35,.5,[196,160,96]],[.3,.3,.45,[170,130,70]],[0,.6,.4,[204,170,104]]]){
   g.fillStyle=col(cl,d,objLight);g.beginPath();g.arc(sx+dx*s*k,gy-dy*s*k,r*s*k,0,7);g.fill();
  }
  break;
 }
 case'animal':drawAnimal(o,sx,gy,k,d);break;
 case'player':{
  const tod=getTOD(timeOfDay);
  if(tod.sun<.65||weather==='storm'||weather==='fog'){
   const lg=g.createRadialGradient(sx,gy-.8*k,0,sx,gy-.8*k,4.2*k);
   lg.addColorStop(0,'rgba(255,215,120,.58)');
   lg.addColorStop(.4,'rgba(255,175,70,.22)');
   lg.addColorStop(1,'rgba(255,140,50,0)');
   g.fillStyle=lg;g.beginPath();g.arc(sx,gy-.8*k,4.2*k,0,7);g.fill();
  }
  if(pw.speed>0||pw.jump>0||pw.lakeStrider>0){
   const c=pw.lakeStrider>0?'105,225,245':pw.speed>0&&pw.jump>0?'255,214,110':pw.speed>0?'110,235,255':'200,160,255';
   const yy=gy-(1.1+jh)*k,rr2=(1.6+Math.sin(T*6)*.15)*k;
   g.globalCompositeOperation='lighter';const ag=g.createRadialGradient(sx,yy,0,sx,yy,rr2);
   ag.addColorStop(0,'rgba('+c+',.5)');ag.addColorStop(1,'rgba('+c+',0)');
   g.fillStyle=ag;g.fillRect(sx-rr2,yy-rr2,rr2*2,rr2*2);g.globalCompositeOperation='source-over';
  }
  drawPlayer(sx,gy,k);
  break;
 }
 }
}

function animals(dt){for(const o of animalList){
 if(o.gone>0){o.gone-=dt;if(o.gone<=0){const s=spot(20,90,0);o.x=s[0];o.z=s[1]}continue}
 const dx=o.x-player.x,dz=o.z-player.z,d=Math.hypot(dx,dz);let sp=0;
 if(started&&d<10){o.ang=Math.atan2(dx,dz)+Math.sin(T*3+o.ph)*.6;sp=o.fast}
 else{o.tm-=dt;if(o.tm<=0){o.tm=1+Math.random()*2.5;o.go=Math.random()<.55;o.ang=Math.random()*6.283}sp=o.go?1.6:0}
 o.vx=Math.sin(o.ang)*sp;o.vz=Math.cos(o.ang)*sp;o.x+=o.vx*dt;o.z+=o.vz*dt;
 const rd=Math.hypot(o.x,o.z);if(rd>96){o.x*=96/rd;o.z*=96/rd;o.ang+=2}
 if(inPond(o.x,o.z)){o.x-=o.vx*dt*2;o.z-=o.vz*dt*2;o.ang+=1.5}
 o.y=ht(o.x,o.z);o.mv=sp>0;if(o.mv)o.hp+=dt*(sp>3?14:7);
 if(started&&d<1.7){
  o.gone=8;caughtN++;document.getElementById('cn').textContent=caughtN;
  toast(o.mystic?power(o):'Caught a '+o.kind+'!');
  audio.playChime([659,784,988,1318]);
  for(let i=0;i<14;i++)bursts.push({x:W/2,y:H*.55,vx:(Math.random()-.5)*360,vy:-Math.random()*400,l:1,c:o.mystic?'#8ff0ff':'#ff7aa8'});
 }
}}

function drawAnimal(o,sx,gy,k,d){
 if(o.gone>0)return;if(o.mystic)return drawMystic(o,sx,gy,k,d);
 const dPl=Math.hypot(o.x-player.x,o.z-player.z);
 const isNight=getTOD(timeOfDay).sun<0.6;
 const objLight=Math.min(1.0,getTOD(timeOfDay).amb+(isNight&&dPl<13?(1-dPl/13)*0.85:0));
 const rx=o.vx*Math.cos(ca)-o.vz*Math.sin(ca);if(Math.abs(rx)>.05)o.dir=rx>0?1:-1;
 const hop=o.mv&&o.kind!=='hedgehog'?Math.abs(Math.sin(o.hp))*.45*k:0,c=x=>col(x,d,objLight),D=[40,30,30];
 g.fillStyle='rgba(60,30,10,.25)';g.beginPath();g.ellipse(sx,gy,.5*k,.14*k,0,0,7);g.fill();
 g.save();g.translate(sx,gy-hop);g.scale(o.dir,1);
 const E=(x,y,w,h,cl,rot)=>{g.fillStyle=c(cl);g.beginPath();g.ellipse(x*k,y*k,w*k,h*k,rot||0,0,7);g.fill()};
 if(o.kind==='bunny'){
  const B=currentSeason==='winter'?[255,255,255]:[246,236,222];
  E(-.3,-.05,.2,.08,B);E(.2,-.05,.15,.07,B);E(0,-.35,.4,.3,B);E(-.4,-.4,.13,.13,[255,255,255]);E(.35,-.6,.23,.21,B);
  E(.3,-1,.08,.27,B,-.15);E(.42,-.98,.08,.27,B,.15);E(.3,-1,.04,.2,[240,170,180],-.15);E(.43,-.64,.03,.03,D);E(.57,-.58,.04,.03,[240,130,150]);E(.45,-.52,.06,.04,[255,190,190]);
 }else if(o.kind==='fox'){
  const O=[228,118,48],W2=[255,245,230];g.strokeStyle=c([60,40,40]);g.lineWidth=.1*k;g.lineCap='round';
  for(const x of[-.4,-.2,.25,.45]){g.beginPath();g.moveTo(x*k,-.4*k);g.lineTo((x+Math.sin(o.hp+x*5)*.12*(o.mv?1:0))*k,0);g.stroke()}
  E(-.85,-.7,.45,.17,O,-.4);E(-1.2,-.85,.15,.12,W2,-.4);E(0,-.6,.6,.3,O);E(.7,-.85,.26,.22,[232,126,54]);E(.82,-.76,.18,.1,W2);E(.93,-.82,.12,.08,[240,150,80]);E(1.03,-.84,.04,.035,D);
  g.fillStyle=c(O);g.beginPath();g.moveTo(.55*k,-1*k);g.lineTo(.62*k,-1.35*k);g.lineTo(.78*k,-1.03*k);g.fill();g.beginPath();g.moveTo(.68*k,-1.03*k);g.lineTo(.82*k,-1.33*k);g.lineTo(.9*k,-1*k);g.fill();E(.76,-.9,.03,.035,D);
 }else{
  const F2=[240,214,180];E(-.2,-.04,.1,.05,[200,160,130]);E(.2,-.04,.1,.05,[200,160,130]);E(-.05,-.35,.5,.34,[110,82,64]);
  g.strokeStyle=c([70,50,40]);g.lineWidth=.06*k;for(let i=0;i<8;i++){const an=Math.PI*(1+i/7),x=Math.cos(an)*.5,y=Math.sin(an)*.34;g.beginPath();g.moveTo(x*k,(-.35+y)*k);g.lineTo(x*1.18*k,(-.35+y*1.2)*k);g.stroke()}
  E(.45,-.2,.2,.16,F2);E(.38,-.38,.07,.07,F2);E(.62,-.2,.05,.045,D);E(.5,-.27,.03,.03,D);
 }
 g.restore();
}

function power(o){
 if(o.kind==='glimmerpuff'){pw.speed=12;return'Swift! You feel light on your feet'}
 if(o.kind==='moonbun'){pw.jump=14;return'Moon leap! Press Space or tap to soar high'}
 pw.speed=18;pw.jump=18;return'Sunwisp! Blazing speed and radiant leap together!';
}

function drawMystic(o,sx,gy,k,d){
 const pul=.5+.5*Math.sin(T*3+o.ph),hov=1.1+Math.sin(T*2+o.ph)*.25+(o.kind==='moonbun'&&o.mv?Math.abs(Math.sin(o.hp))*.4:0),y=gy-hov*k;
 const C=o.kind==='glimmerpuff'?'110,235,255':o.kind==='moonbun'?'200,160,255':'255,214,110';
 const rx=o.vx*Math.cos(ca)-o.vz*Math.sin(ca);if(Math.abs(rx)>.05)o.dir=rx>0?1:-1;
 g.fillStyle='rgba(40,20,60,.2)';g.beginPath();g.ellipse(sx,gy,.45*k,.13*k,0,0,7);g.fill();
 const gr=(1.7+pul*.5)*k*(o.kind==='sunwisp'?1.35:1);
 g.globalCompositeOperation='lighter';const gg=g.createRadialGradient(sx,y,0,sx,y,gr);gg.addColorStop(0,'rgba('+C+',.65)');gg.addColorStop(1,'rgba('+C+',0)');g.fillStyle=gg;g.fillRect(sx-gr,y-gr,gr*2,gr*2);g.globalCompositeOperation='source-over';
 g.save();g.translate(sx,y);g.scale(o.dir,1);
 const E=(x,yy,w,h,cl,rot)=>{g.fillStyle=cl;g.beginPath();g.ellipse(x*k,yy*k,w*k,h*k,rot||0,0,7);g.fill()},EY=(x,yy)=>{E(x,yy,.07,.09,'#3c2850');E(x+.02,yy-.03,.025,.03,'#fff')};
 if(o.kind==='glimmerpuff'){
  const f=Math.sin(T*14)*.25;E(-.5,-.1,.3,.12,'rgba(190,250,255,.7)',-.6+f);E(.5,-.1,.3,.12,'rgba(190,250,255,.7)',.6-f);
  for(let i=0;i<8;i++){const an=i*.785;E(Math.cos(an)*.38,Math.sin(an)*.38,.2,.2,'#a8f0ff')}
  E(0,0,.45,.45,'#dcfcff');EY(-.16,-.02);EY(.16,-.02);E(-.28,.1,.07,.045,'#ffb3d0');E(.28,.1,.07,.045,'#ffb3d0');E(0,-.55,.06,.14,'#a8f0ff',.3);
 }else if(o.kind==='moonbun'){
  E(-.4,.05,.12,.12,'#fff');E(0,0,.4,.32,'#e2d2ff');E(.32,-.25,.23,.21,'#e8dcff');E(.28,-.68,.08,.28,'#e8dcff',-.15);E(.4,-.66,.08,.28,'#e8dcff',.15);E(.28,-.68,.04,.2,'#ffbfe6',-.15);E(.37,-.4,.045,.045,'#fff0a0');EY(.4,-.28);E(.54,-.2,.035,.03,'#ff9bc4');
 }else{
  g.strokeStyle='rgba(255,230,140,.8)';g.lineWidth=.06*k;g.lineCap='round';for(let i=0;i<8;i++){const an=T+i*.785,c=Math.cos(an),s=Math.sin(an);g.beginPath();g.moveTo(c*.6*k,s*.6*k);g.lineTo(c*.88*k,s*.88*k);g.stroke()}
  E(0,0,.5,.5,'#fff0a8');E(0,0,.34,.34,'#ffe070');EY(-.14,-.02);EY(.14,-.02);E(0,.12,.08,.04,'#e0705a');
 }
 g.restore();g.globalCompositeOperation='lighter';g.fillStyle='rgba(255,255,255,.85)';
 for(let i=0;i<5;i++){const an=T*1.5+i*1.26+o.ph;g.beginPath();g.arc(sx+Math.cos(an)*.9*k,y+Math.sin(an*1.3)*.7*k,(.04+.02*Math.sin(T*5+i))*k,0,7);g.fill()}
 g.globalCompositeOperation='source-over';
}

function drawPlayer(sx,gy,k){
 const ph=walk*2,mv=moving,bob=mv?Math.abs(Math.cos(ph))*.035*k:0,j=1/(1+jh*.3),wade=inPond(player.x,player.z);
 g.fillStyle='rgba(50,25,10,.3)';g.beginPath();g.ellipse(sx,gy,.5*k*j,.14*k*j,0,0,7);g.fill();
 g.save();g.translate(0,-jh*k);
 const X=x=>sx+x*k,Y=y=>gy-y*k-bob;
 const L=(x1,y1,x2,y2,w,c)=>{g.strokeStyle=c;g.lineWidth=w*k;g.lineCap='round';g.beginPath();g.moveTo(X(x1),Y(y1));g.lineTo(X(x2),Y(y2));g.stroke()};
 const E=(x,y,w,h,c,r)=>{g.fillStyle=c;g.beginPath();g.ellipse(X(x),Y(y),w*k,h*k,r||0,0,7);g.fill()};

 for(const s of[-1,1]){const st=mv?Math.sin(ph+(s>0?0:Math.PI)):0,lf=Math.max(0,st)*.16,kx=s*.1;
  L(kx,.95,kx*1.05,.52+lf*.4,.17,'#3d4a68');L(kx*1.05,.52+lf*.4,kx*1.1,.1+lf,.14,'#33405a');E(kx*1.1,.05+lf,.09,.055,'#3a2a20')}
 if(wade&&pw.lakeStrider<=0){g.fillStyle='rgba(90,140,170,.55)';g.fillRect(X(-.3),Y(.42),.6*k,.42*k)}
 for(const s of[-1,1]){const st=mv?Math.sin(ph+(s>0?Math.PI:0)):0;L(s*.25,1.4,s*.29,1.12,.1,'#a8432a');L(s*.29,1.12,s*.28,.88+st*.05,.085,'#b5482c')}
 const jg=g.createLinearGradient(X(-.25),0,X(.25),0);jg.addColorStop(0,'#d4623a');jg.addColorStop(1,'#a8432a');
 g.fillStyle=jg;g.beginPath();g.moveTo(X(-.17),Y(.98));g.lineTo(X(.17),Y(.98));g.quadraticCurveTo(X(.26),Y(1.2),X(.25),Y(1.42));g.quadraticCurveTo(X(0),Y(1.5),X(-.25),Y(1.42));g.quadraticCurveTo(X(-.26),Y(1.2),X(-.17),Y(.98));g.fill();
 E(0,.98,.17,.03,'#2f3446');
 g.fillStyle='#7d5634';g.beginPath();g.roundRect(X(-.18),Y(1.42),.36*k,.5*k,.07*k);g.fill();
 g.fillStyle='#936a40';g.beginPath();g.roundRect(X(-.15),Y(1.42),.3*k,.17*k,.05*k);g.fill();
 L(-.1,1.2,.1,1.2,.025,'#5a3b22');E(0,1.52,.2,.06,'#5d7a62');L(-.19,1.4,-.17,1.08,.04,'#3a2a1e');L(.19,1.4,.17,1.08,.04,'#3a2a1e');
 for(const s of[-1,1])E(s*.28,.84+(mv?Math.sin(ph+(s>0?Math.PI:0))*.05:0),.045,.05,'#e0aa84');
 E(0,1.5,.05,.05,'#d9a07c');E(0,1.5,.12,.045,'#efe2c4');
 g.strokeStyle='#efe2c4';g.lineWidth=.05*k;g.beginPath();g.moveTo(X(.08),Y(1.48));g.quadraticCurveTo(X(.2),Y(1.38),X(.2+Math.sin(T*6)*.04*(mv+.3)),Y(1.22));g.stroke();
 E(0,1.64,.115,.125,'#5a3a28');E(-.115,1.62,.025,.04,'#d9a07c');E(.115,1.62,.025,.04,'#d9a07c');
 g.fillStyle='#e9a23a';g.beginPath();g.ellipse(X(0),Y(1.67),.125*k,.125*k,0,Math.PI,0);g.fill();g.fillStyle='#c9832a';g.fillRect(X(-.125),Y(1.68),.25*k,.045*k);E(0,1.8,.035,.035,'#f4dc9a');

 const isNight=getTOD(timeOfDay).sun<.65;
 if(isNight){
  const lx=X(.35),ly=Y(.72);
  g.fillStyle='#85522b';g.fillRect(lx-.04*k,ly-.12*k,.08*k,.05*k);
  g.fillStyle='#ffc952';g.beginPath();g.arc(lx,ly,.08*k,0,7);g.fill();
  g.strokeStyle='#422713';g.lineWidth=.025*k;g.strokeRect(lx-.06*k,ly-.08*k,.12*k,.16*k);
  L(.28,.86,.35,.72,.025,'#422713');
 }
 g.restore();
}

function minimap(){const r=Math.min(62,H*.1),cx=W-r-16,cy=H-r-16,sc=r/38;
 g.save();g.beginPath();g.arc(cx,cy,r,0,7);g.fillStyle='rgba(255,243,220,.72)';g.fill();g.clip();
 const m=(x,z)=>{const dx=x-player.x,dz=z-player.z;return[cx+(dx*Math.cos(a)-dz*Math.sin(a))*sc,cy-(dx*Math.sin(a)+dz*Math.cos(a))*sc]};
 let p=m(POND.x,POND.z);g.fillStyle='rgba(120,160,180,.7)';g.beginPath();g.ellipse(p[0],p[1],POND.rx*sc,POND.rz*sc,-a,0,7);g.fill();
 p=m(CABIN.x,CABIN.z);g.fillStyle='#a33d2a';g.fillRect(p[0]-5,p[1]-5,10,10);
 p=m(MONOLITH.x,MONOLITH.z);g.fillStyle='#5fc8ff';g.beginPath();g.arc(p[0],p[1],4,0,7);g.fill();
 p=m(SHRINE.x,SHRINE.z);g.fillStyle='#72efdd';g.fillRect(p[0]-3,p[1]-3,6,6);
 for(const l of leaves)if(!l.got){p=m(l.x,l.z);g.fillStyle='#f2a21c';g.beginPath();g.arc(p[0],p[1],3.5,0,7);g.fill()}
 for(const o of animalList)if(!o.gone){p=m(o.x,o.z);g.fillStyle=o.mystic?(o.kind==='glimmerpuff'?'#5fe3ff':o.kind==='moonbun'?'#b98cff':'#ffd24a'):'#e0507f';g.beginPath();g.arc(p[0],p[1],o.mystic?4:2.5,0,7);g.fill()}
 g.fillStyle='#4a2c1a';g.beginPath();g.moveTo(cx,cy-7);g.lineTo(cx+5,cy+5);g.lineTo(cx-5,cy+5);g.fill();g.restore();
 g.strokeStyle='#4a2c1a';g.lineWidth=3;g.beginPath();g.arc(cx,cy,r,0,7);g.stroke()}

function drawWeather(dt){
 if(weather==='rain'||weather==='storm'){
  const isStorm=weather==='storm',wind=isStorm?-260:-110,count=isStorm?220:150;
  const isSnow=currentSeason==='winter';
  g.strokeStyle=isSnow?'rgba(240,248,255,.8)':isStorm?'rgba(205,225,255,.65)':'rgba(215,235,255,.5)';
  g.lineWidth=isStorm?1.8:1.2;
  g.beginPath();
  for(let i=0;i<count;i++){
   const p=raindrops[i];p.y+=p.speed*dt*(isSnow?0.5:isStorm?1.3:1);p.x+=(isSnow?wind*0.4:wind)*dt;
   if(p.y>H+20){
    p.y=-20;p.x=Math.random()*(W+300);
    if(Math.random()<0.25&&!isSnow)splashes.push({x:p.x,y:H*.45+Math.random()*H*.55,r:1,l:1});
   }
   if(p.x<-50)p.x=W+50;
   g.moveTo(p.x,p.y);
   if(isSnow){
    g.lineTo(p.x+2,p.y+2);
   }else{
    g.lineTo(p.x+wind*.04,p.y+p.len*(isStorm?1.35:1));
   }
  }
  g.stroke();

  for(let i=splashes.length-1;i>=0;i--){
   const sp=splashes[i];sp.r+=22*dt;sp.l-=3.5*dt;
   if(sp.l<=0){splashes.splice(i,1);continue}
   g.strokeStyle=`rgba(220,240,255,${sp.l*.4})`;g.lineWidth=1;
   g.beginPath();g.ellipse(sp.x,sp.y,sp.r,sp.r*.35,0,0,7);g.stroke();
  }
 }
 if(weather==='fog'){
  for(const b of fogBands){
   b.offset+=b.speed*dt;const y=H*b.yFrac;
   const fg=g.createLinearGradient(0,y-b.h,0,y+b.h);
   fg.addColorStop(0,'rgba(230,235,245,0)');
   fg.addColorStop(.5,`rgba(225,230,240,${b.alpha})`);
   fg.addColorStop(1,'rgba(230,235,245,0)');
   g.fillStyle=fg;g.fillRect(0,y-b.h,W,b.h*2);
  }
 }
 if(lightningFlash>0){
  g.fillStyle=`rgba(240,248,255,${lightningFlash*.55})`;g.fillRect(0,0,W,H);
 }
}

function render(){
 g.clearRect(0,0,W,H);sky();terrain();
 const h=hz(),Fo=F(),list=[];
 for(const o of objs){
  const[rx,rz]=proj(o.x,o.z);
  if(rz<.8||rz>130)continue;
  const k=Fo/rz,sx=W/2+rx*k;
  if(sx<-400||sx>W+400)continue;
  if(rz>9&&!seen(o))continue;
  list.push([o,sx,h+(camY-(o.y||0))*k,k,rz]);
 }

 for(const w of spiritWisps){
  const[rx,rz]=proj(w.x,w.z);
  if(rz>=.8&&rz<=120){
   const k=Fo/rz,sx=W/2+rx*k,sy=h+(camY-w.y)*k;
   g.fillStyle='rgba(130,235,255,.85)';g.beginPath();g.arc(sx,sy,Math.max(2,0.2*k),0,7);g.fill();
  }
 }

 list.sort((p,q)=>q[4]-p[4]);
 for(const[o,sx,gy,k,d]of list){
  if((o.t==='oak'||o.t==='pine')&&d<5.5){
   g.globalAlpha=Math.max(0.25,Math.min(1.0,(d-1.6)/3.9));
  }else{
   g.globalAlpha=1.0;
  }
  drawObj(o,sx,gy,k,d);
  g.globalAlpha=1.0;
 }

 for(const p of parts){
  g.save();g.translate(p.x,p.y);g.rotate(p.p+T*2);
  let pCol;
  if(currentSeason==='spring')pCol=[255,192,203];
  else if(currentSeason==='summer')pCol=[255,235,110];
  else if(currentSeason==='winter')pCol=[245,250,255];
  else pCol=p.c;
  g.fillStyle=`rgb(${pCol[0]},${pCol[1]},${pCol[2]})`;
  g.beginPath();g.ellipse(0,0,p.s,p.s*(currentSeason==='winter'?.8:.4),0,0,7);g.fill();
  g.restore();
 }

 for(const b of bursts){g.globalAlpha=Math.max(0,b.l);g.fillStyle=b.c||'#ffb43a';g.beginPath();g.ellipse(b.x,b.y,6,3,b.l*8,0,7);g.fill()}g.globalAlpha=1;
 drawWeather(1/60);
 if(started)minimap();
 if(joy){
  g.strokeStyle='rgba(255,255,255,.6)';g.lineWidth=3;g.beginPath();g.arc(joy.ox,joy.oy,45,0,7);g.stroke();
  g.fillStyle='rgba(255,255,255,.5)';g.beginPath();g.arc(joy.ox+Math.max(-45,Math.min(45,joy.x-joy.ox)),joy.oy+Math.max(-45,Math.min(45,joy.y-joy.oy)),20,0,7);g.fill();
 }
}

let last=performance.now();
(function loop(n){const dt=Math.min(.05,(n-last)/1000);last=n;update(dt);render();requestAnimationFrame(loop)})(last);
document.getElementById('go').onclick=()=>{started=true;document.getElementById('start').hidden=true;initAudio()};
document.getElementById('again').onclick=()=>{document.getElementById('win').hidden=true};

const setTOD=t=>{
 timeOfDay=t;
 document.querySelectorAll('#tod-btns button').forEach(b=>{
  b.classList.toggle('active',Math.abs(parseFloat(b.dataset.t)-t)<.05);
 });
};
const setWeather=w=>{
 weather=w;
 document.querySelectorAll('#weather-btns button').forEach(b=>{
  b.classList.toggle('active',b.dataset.w===w);
 });
 if(w==='storm')toast('Thunderstorm rolling in');
 else if(w==='rain')toast(currentSeason==='winter'?'Snow flurry falling':'Gentle rain falling');
 else if(w==='fog')toast('Misty fog descending');
 else toast('Skies clearing up');
};
const setQuality=q=>{
 qualityScale=q;
 rs();
 document.querySelectorAll('#quality-btns button').forEach(b=>{
  b.classList.toggle('active',Math.abs(parseFloat(b.dataset.q)-q)<.05);
 });
};

document.getElementById('season-btns').onclick=e=>{
 const b=e.target.closest('button');if(!b)return;
 autoSeason=false;document.getElementById('auto-season').checked=false;
 setSeason(b.dataset.s);
};
document.getElementById('auto-season').onchange=e=>{autoSeason=e.target.checked};

document.getElementById('tod-btns').onclick=e=>{
 const b=e.target.closest('button');if(!b)return;
 autoTime=false;document.getElementById('auto-time').checked=false;
 setTOD(parseFloat(b.dataset.t));
};
document.getElementById('weather-btns').onclick=e=>{
 const b=e.target.closest('button');if(!b)return;
 autoWeather=false;document.getElementById('auto-weather').checked=false;
 setWeather(b.dataset.w);
};
document.getElementById('quality-btns').onclick=e=>{
 const b=e.target.closest('button');if(!b)return;
 setQuality(parseFloat(b.dataset.q));
};
document.getElementById('auto-time').onchange=e=>{autoTime=e.target.checked};
document.getElementById('auto-weather').onchange=e=>{autoWeather=e.target.checked};

// Mouse wheel basic zoom (CD adjusts between 4.5 and 11, NO vertical uplift)
addEventListener('wheel',e=>{
 const delta=Math.sign(e.deltaY)*0.7;
 camDist=Math.max(4.5,Math.min(11.0,camDist+delta));
},{passive:true});

const soundBtn=document.getElementById('sound-btn');
const toggleAudioBtn=document.getElementById('toggle-audio-btn');
const toggleSound=()=>{
 initAudio();
 audio.enabled=!audio.enabled;
 soundBtn.textContent=audio.enabled?'🔊':'🔇';
 toggleAudioBtn.textContent=audio.enabled?'🔊 Sound: ON':'🔇 Sound: OFF';
 toast(audio.enabled?'Sound effects enabled':'Sound muted');
};
soundBtn.onclick=toggleSound;
toggleAudioBtn.onclick=toggleSound;

const menuBtn=document.getElementById('menu-btn');
const settingsModal=document.getElementById('settings-modal');
const closeSettings=document.getElementById('close-settings');
const toggleMenu=()=>{settingsModal.hidden=!settingsModal.hidden};
menuBtn.onclick=toggleMenu;
closeSettings.onclick=()=>{settingsModal.hidden=true};
addEventListener('keydown',e=>{
 if(e.code==='KeyM'||(e.code==='Escape'&&!settingsModal.hidden)){toggleMenu()}
});
cv.addEventListener('pointerdown',e=>{
 if(!settingsModal.hidden){settingsModal.hidden=true}
});

const cabinView=document.getElementById('cabin-view');
const openCabin=()=>{
 inCabin=true;
 document.getElementById('hearth-leaves').textContent=hearthLeaves;
 document.getElementById('avail-leaves').textContent=Math.max(0,got-hearthLeaves);
 const wNote=weather==='storm'?'Fierce thunderstorm howling outside the cedar walls':weather==='rain'?(currentSeason==='winter'?'Soft snowfall blanketing the windowsill':'Gentle rain tapping against the window'):weather==='fog'?'Misty fog blanketing the quiet pine trees':'Golden valley light streaming through the glass';
 document.getElementById('cabin-outside-note').textContent='Window: '+wNote;
 cabinView.hidden=false;
};
const closeCabin=()=>{inCabin=false;cabinView.hidden=true};

document.getElementById('exit-cabin-top').onclick=closeCabin;
document.getElementById('exit-cabin-btn').onclick=closeCabin;
document.getElementById('travel-cabin-btn').onclick=()=>{
 player.x=CABIN.x;player.z=CABIN.z-6.5;
 settingsModal.hidden=true;
 openCabin();
};

document.getElementById('add-leaves-btn').onclick=()=>{
 if(got>hearthLeaves){
  hearthLeaves=got;lit=true;
  document.getElementById('hearth-leaves').textContent=hearthLeaves;
  document.getElementById('avail-leaves').textContent=0;
  toast('Leaves added! The hearth blazes warmly');
  audio.playChime([523,659,784,1046]);
  if(hearthLeaves>=12){won=true;toast('All 12 leaves! The eternal hearth is lit!');document.getElementById('obj').textContent='The hearth is lit'}
 }else{
  toast('No new leaves collected yet. Search the valley!');
 }
};

document.getElementById('cider-btn').onclick=()=>{
 pw.speed=35;pw.jump=35;
 audio.playTone(600,'sine',0.3,0.15);
 toast('Warm spiced cider! Swiftness and high jump granted!');
};

document.getElementById('sleep-btn').onclick=()=>{
 timeOfDay=(timeOfDay+0.35)%1.0;
 if(weather==='storm')setWeather('clear');
 toast('Rested by the warm fire. A new time of day begins');
 const wNote=weather==='storm'?'Fierce thunderstorm howling outside the cedar walls':weather==='rain'?(currentSeason==='winter'?'Soft snowfall blanketing the windowsill':'Gentle rain tapping against the window'):weather==='fog'?'Misty fog blanketing the quiet pine trees':'Golden valley light streaming through the glass';
 document.getElementById('cabin-outside-note').textContent='Window: '+wNote;
};

addEventListener('keydown',e=>{
 if(e.code==='KeyE'){
  if(inCabin)closeCabin();
  else if(activePromptAction)activateInteraction();
 }
});
</script></body></html>
'''
with open('Amber Valley.html', 'w', encoding='utf-8') as f: f.write(html_content)
