# Build script that generates the full, breathtaking Three.js version of Amber Valley
import re

threejs_valley = r'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>Amber Valley</title>
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<link href="https://fonts.googleapis.com/css2?family=Gaegu:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{--ink:#4a2c1a;--paper:#fff3dc;--accent:#c2562b;color-scheme:light dark}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--ink:#ffe9c7;--paper:#3a2216;--accent:#ff9a57}}
:root[data-theme="dark"]{--ink:#ffe9c7;--paper:#3a2216;--accent:#ff9a57}
html,body{height:100%;margin:0;overflow:hidden;background:#0d111a;font-family:Gaegu,'Comic Sans MS',cursive;color:var(--ink);user-select:none}
canvas{display:block;width:100%;height:100%;touch-action:none}
#hud{position:fixed;top:calc(12px + env(safe-area-inset-top));left:14px;background:var(--paper);padding:6px 14px;border-radius:14px;font-size:24px;font-weight:700;box-shadow:0 3px 0 rgba(0,0,0,.15);z-index:10;pointer-events:none}
#hud small{display:block;font-size:17px;font-weight:400;opacity:.9}
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
#minimap-canvas{position:fixed;bottom:14px;right:14px;width:110px;height:110px;border-radius:50%;border:3px solid var(--ink);background:rgba(255,243,220,.85);box-shadow:0 3px 10px rgba(0,0,0,.3);z-index:10;pointer-events:none}
</style>
<script src="three.min.js"></script>
</head><body>
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
<canvas id="minimap-canvas" width="110" height="110"></canvas>
<div id="toast"></div>

<div class="ov" id="start"><div class="card"><h1>Amber Valley</h1>
 <p>Twelve glowing leaves lie scattered across the shifting seasons of the valley. Gather them to light the ancient cabin hearth.</p>
 <p>Discover the <b>Whispering Monolith</b> for leaf guidance, pray at the <b>Moon Shrine</b> to walk on water, and spring launch from <b>Fairy Mushrooms</b>!</p>
 <p>At night, wander through the dark starry forest with your warm lantern. Change seasons and weather anytime in the <b>☰ Settings</b> menu.</p>
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
   <div id="fps-display" style="font-size:15px;opacity:.85;margin-top:6px">FPS: 60 (WebGL 3D)</div>
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
// --- Procedural Audio Engine ---
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
   gn.gain.setValueAtTime(vol,t);gn.gain.exponentialRampToValueAtTime(0.0001,t+dur);
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
   gn.gain.setValueAtTime(0.18,t);gn.gain.exponentialRampToValueAtTime(0.001,t+0.38);
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
   const filter=this.ctx.createBiquadFilter();filter.type='lowpass';
   filter.frequency.value=surface==='water'?600:surface==='snow'?1100:450;
   const gn=this.ctx.createGain();gn.gain.setValueAtTime(surface==='water'?0.14:0.06,t);
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
   const filter=this.ctx.createBiquadFilter();filter.type='lowpass';filter.frequency.value=180;
   const gn=this.ctx.createGain();gn.gain.setValueAtTime(0.45,t);gn.gain.linearRampToValueAtTime(0.01,t+1.8);
   src.connect(filter);filter.connect(gn);gn.connect(this.ctx.destination);
   src.start(t);
  }catch(e){}
 }
}
const audio=new ProceduralAudio();
const initAudio=()=>{audio.init()};
addEventListener('pointerdown',initAudio,{once:true});
addEventListener('keydown',initAudio,{once:true});

// --- Mathematical Terrain Functions ---
const CABIN={x:0,z:48},POND={x:-42,z:24,rx:17,rz:17};
const MONOLITH={x:36,z:-48},SHRINE={x:-54,z:10},FAIRYRING={x:-24,z:-56};
const WATER=-0.9,LAKE={x:-42,z:24},DES={x:68,z:-5},FOR={x:-10,z:-60};
const sm=(a,b,x)=>{const t=Math.max(0,Math.min(1,(x-a)/(b-a)));return t*t*(3-2*t)};
function wts(x,z){return[sm(26,9,Math.hypot(x-LAKE.x,z-LAKE.z)),sm(44,24,Math.hypot(x-DES.x,(z-DES.z)*.8)),sm(40,22,Math.hypot(x-FOR.x,z-FOR.z))]}
function ht(x,z){
 let h=2.6*Math.sin(x*.042+1)*Math.cos(z*.037)+1.2*Math.sin(x*.1+z*.085)+.5*Math.sin(x*.22-z*.17)+1.6;
 const w=wts(x,z);h+=w[1]*(2.4*Math.sin(x*.13+z*.04)*Math.sin(z*.09)+1.5)+w[2]*Math.sin(x*.07)*Math.cos(z*.08)*1.6;
 const fl=Math.max(sm(14,5,Math.hypot(x,z)),sm(14,6,Math.hypot(x-CABIN.x,z-CABIN.z)));h*=1-fl;
 return h*(1-w[0])-4*w[0];
}
const inPond=(x,z,m=1)=>ht(x,z)<WATER+(m>1?.5:0);

let seed=11;const R=()=>(seed=(seed*16807)%2147483647)/2147483647;

// --- Three.js Scene Setup ---
const scene=new THREE.Scene();
const camera=new THREE.PerspectiveCamera(50,innerWidth/innerHeight,0.2,350);
const renderer=new THREE.WebGLRenderer({antialias:true,powerPreference:'high-performance'});
renderer.setSize(innerWidth,innerHeight);
renderer.setPixelRatio(Math.min(devicePixelRatio||1,2));
renderer.shadowMap.enabled=true;
renderer.shadowMap.type=THREE.PCFSoftShadowMap;
renderer.toneMapping=THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure=1.05;
document.body.prepend(renderer.domElement);

// Lighting
const ambientLight=new THREE.AmbientLight(0xffffff,0.75);
scene.add(ambientLight);
const sunLight=new THREE.DirectionalLight(0xfff3dc,1.1);
sunLight.position.set(40,80,40);
sunLight.castShadow=true;
sunLight.shadow.mapSize.width=1024;
sunLight.shadow.mapSize.height=1024;
sunLight.shadow.camera.near=10;
sunLight.shadow.camera.far=200;
sunLight.shadow.camera.left=-70;sunLight.shadow.camera.right=70;
sunLight.shadow.camera.top=70;sunLight.shadow.camera.bottom=-70;
sunLight.shadow.bias=-0.001;
scene.add(sunLight);

// Sky dome & Fog
scene.fog=new THREE.FogExp2(0xebd1a8,0.009);

// --- Seasonal Color Palettes ---
const SEASON_NAMES={spring:'🌸 Spring Valley',summer:'☀️ Summer Valley',autumn:'🍂 Autumn Valley',winter:'❄️ Winter Valley'};
const SEASONS=['spring','summer','autumn','winter'];
let currentSeason='autumn',autoSeason=false,seasonTimer=60.0;
let timeOfDay=0.5,autoTime=false;
let weather='clear',autoWeather=false,weatherTimer=30;
let lightningTimer=4.0,lightningFlash=0;

const SEASON_PALETTES={
 spring:{
  meadow:[0.46,0.72,0.32],forest:[0.26,0.48,0.24],desert:[0.82,0.76,0.56],shore:[0.88,0.82,0.62],
  oak:[0xffb7c5,0xffc2d1,0xfb6f92],pine:[0x3d7042,0x4e8554],fog:0xe2f0d9,skyTop:0x6ca0dc,skyBot:0xd5e8d4
 },
 summer:{
  meadow:[0.35,0.62,0.25],forest:[0.22,0.42,0.22],desert:[0.88,0.76,0.5],shore:[0.9,0.82,0.58],
  oak:[0x489638,0x5ba848,0x387e2a],pine:[0x2d5a32,0x3a6e40],fog:0xcde2f2,skyTop:0x4a90e2,skyBot:0xcbe3fb
 },
 autumn:{
  meadow:[0.82,0.56,0.25],forest:[0.48,0.36,0.2],desert:[0.88,0.74,0.5],shore:[0.85,0.75,0.52],
  oak:[0xe87828,0xf09a32,0xd45020],pine:[0x3d5c3f,0x4a6b4c],fog:0xebd1a8,skyTop:0x667fa8,skyBot:0xefcfad
 },
 winter:{
  meadow:[0.92,0.95,0.98],forest:[0.72,0.78,0.85],desert:[0.84,0.86,0.9],shore:[0.82,0.88,0.94],
  oak:[0xedf2f7,0xdce4ec,0xc8d6e5],pine:[0x557a70,0x688e84],fog:0xdfe7f0,skyTop:0x4d658d,skyBot:0xdce4ec
 }
};

// --- Procedural 3D Terrain Mesh ---
const T_SIZE=240,T_SEGS=150;
const terrainGeom=new THREE.PlaneGeometry(T_SIZE,T_SIZE,T_SEGS,T_SEGS);
terrainGeom.rotateX(-Math.PI/2);
const posAttr=terrainGeom.attributes.position;
const colorAttr=new THREE.BufferAttribute(new Float32Array(posAttr.count*3),3);
terrainGeom.setAttribute('color',colorAttr);

for(let i=0;i<posAttr.count;i++){
 const vx=posAttr.getX(i),vz=posAttr.getZ(i);
 posAttr.setY(i,ht(vx,vz));
}
terrainGeom.computeVertexNormals();

function updateTerrainColors(seasonKey){
 const pal=SEASON_PALETTES[seasonKey];
 for(let i=0;i<posAttr.count;i++){
  const vx=posAttr.getX(i),vy=posAttr.getY(i),vz=posAttr.getZ(i);
  const w=wts(vx,vz);
  let r=pal.meadow[0],g=pal.meadow[1],b=pal.meadow[2];
  // Forest blend
  r+=(pal.forest[0]-r)*w[2];g+=(pal.forest[1]-g)*w[2];b+=(pal.forest[2]-b)*w[2];
  // Desert blend
  r+=(pal.desert[0]-r)*w[1];g+=(pal.desert[1]-g)*w[1];b+=(pal.desert[2]-b)*w[1];
  // Shore blend
  if(vy<WATER+0.6){
   r=r*0.3+pal.shore[0]*0.7;g=g*0.3+pal.shore[1]*0.7;b=b*0.3+pal.shore[2]*0.7;
  }
  colorAttr.setXYZ(i,r,g,b);
 }
 colorAttr.needsUpdate=true;
}
updateTerrainColors(currentSeason);

const terrainMat=new THREE.MeshStandardMaterial({
 vertexColors:true,roughness:0.88,metalness:0.08,flatShading:true
});
const terrainMesh=new THREE.Mesh(terrainGeom,terrainMat);
terrainMesh.receiveShadow=true;
scene.add(terrainMesh);

// --- Water Plane ---
const waterGeom=new THREE.CircleGeometry(24,32);
waterGeom.rotateX(-Math.PI/2);
const waterMat=new THREE.MeshStandardMaterial({
 color:0x3a86c8,roughness:0.12,metalness:0.1,transparent:true,opacity:0.75
});
const waterMesh=new THREE.Mesh(waterGeom,waterMat);
waterMesh.position.set(POND.x,WATER+0.05,POND.z);
scene.add(waterMesh);

// --- 3D Objects & Forest Creation ---
const oakMaterials={},pineMaterials={};
for(const s of SEASONS){
 const pal=SEASON_PALETTES[s];
 oakMaterials[s]=pal.oak.map(c=>new THREE.MeshStandardMaterial({color:c,roughness:0.8,flatShading:true}));
 pineMaterials[s]=pal.pine.map(c=>new THREE.MeshStandardMaterial({color:c,roughness:0.8,flatShading:true}));
}
const woodMat=new THREE.MeshStandardMaterial({color:0x5c3a21,roughness:0.9,flatShading:true});
const snowCapMat=new THREE.MeshStandardMaterial({color:0xf0f5fa,roughness:0.7,flatShading:true});

const pineMeshes=[],oakCanopies=[];

function createPineTree(x,z,scale=1){
 const group=new THREE.Group();
 const trunkGeom=new THREE.CylinderGeometry(0.18*scale,0.32*scale,1.5*scale,6);
 const trunk=new THREE.Mesh(trunkGeom,woodMat);
 trunk.position.y=0.75*scale;
 trunk.castShadow=true;trunk.receiveShadow=true;
 group.add(trunk);

 const tiers=[];
 for(let i=0;i<3;i++){
  const r=(1.5-i*0.35)*scale,h=1.8*scale;
  const coneGeom=new THREE.ConeGeometry(r,h,6);
  const matList=pineMaterials[currentSeason];
  const cone=new THREE.Mesh(coneGeom,matList[i%matList.length]);
  cone.position.y=(1.5+i*1.15)*scale;
  cone.castShadow=true;cone.receiveShadow=true;
  group.add(cone);
  tiers.push(cone);

  // Snow cap
  const snowGeom=new THREE.ConeGeometry(r*0.6,h*0.45,6);
  const snowCap=new THREE.Mesh(snowGeom,snowCapMat);
  snowCap.position.y=(1.5+i*1.15+h*0.35)*scale;
  snowCap.visible=(currentSeason==='winter');
  group.add(snowCap);
  cone.snowCap=snowCap;
 }
 group.position.set(x,ht(x,z),z);
 scene.add(group);
 pineMeshes.push(tiers);
 return group;
}

function createOakTree(x,z,scale=1){
 const group=new THREE.Group();
 const trunkGeom=new THREE.CylinderGeometry(0.3*scale,0.55*scale,3.0*scale,6);
 const trunk=new THREE.Mesh(trunkGeom,woodMat);
 trunk.position.y=1.5*scale;
 trunk.castShadow=true;trunk.receiveShadow=true;
 group.add(trunk);

 const canopyGroup=new THREE.Group();
 const matList=oakMaterials[currentSeason];
 for(let i=0;i<6;i++){
  const an=i*1.05,dist=(0.8+R()*0.7)*scale;
  const r=(1.3+R()*0.6)*scale;
  const sphereGeom=new THREE.IcosahedronGeometry(r,1);
  const foliage=new THREE.Mesh(sphereGeom,matList[i%matList.length]);
  foliage.position.set(Math.cos(an)*dist,(3.2+Math.sin(an)*0.5+R()*0.8)*scale,Math.sin(an)*dist);
  foliage.castShadow=true;foliage.receiveShadow=true;
  canopyGroup.add(foliage);
  oakCanopies.push(foliage);
 }
 group.add(canopyGroup);
 group.position.set(x,ht(x,z),z);
 scene.add(group);
 return group;
}

// Populate Forest Trees
function spot(minR,maxR){
 for(;;){
  const r=minR+R()*(maxR-minR),a=R()*6.283,x=Math.cos(a)*r,z=Math.sin(a)*r;
  if(Math.hypot(x-CABIN.x,z-CABIN.z)<9||inPond(x,z,1.3)||Math.hypot(x,z)<6)continue;
  if(Math.abs(x)<4&&z>2&&z<44)continue;
  return[x,z];
 }
}

for(let i=0;i<48;i++){const[x,z]=spot(8,92);createOakTree(x,z,0.85+R()*0.45)}
for(let i=0;i<110;i++){const[x,z]=spot(6,96);createPineTree(x,z,0.8+R()*0.6)}

// Rocks
const rockGeom=new THREE.DodecahedronGeometry(1,1);
const rockMat=new THREE.MeshStandardMaterial({color:0x8a847e,roughness:0.9,flatShading:true});
for(let i=0;i<35;i++){
 const[x,z]=spot(5,95);
 const rMesh=new THREE.Mesh(rockGeom,rockMat);
 const s=0.6+R()*0.9;
 rMesh.scale.set(s,s*0.6,s*1.2);
 rMesh.rotation.set(R()*3,R()*3,R()*3);
 rMesh.position.set(x,ht(x,z)+s*0.2,z);
 rMesh.castShadow=true;rMesh.receiveShadow=true;
 scene.add(rMesh);
}

// --- Woodland Cabin Model ---
const cabinGroup=new THREE.Group();
// Base walls
const cabinWallsGeom=new THREE.BoxGeometry(6.4,3.2,5.2);
const cabinWalls=new THREE.Mesh(cabinWallsGeom,woodMat);
cabinWalls.position.y=1.6;
cabinWalls.castShadow=true;cabinWalls.receiveShadow=true;
cabinGroup.add(cabinWalls);
// Roof
const roofGeom=new THREE.ConeGeometry(4.8,2.2,4);
roofGeom.rotateY(Math.PI/4);
const roofMat=new THREE.MeshStandardMaterial({color:0x8c4328,roughness:0.8,flatShading:true});
const roof=new THREE.Mesh(roofGeom,roofMat);
roof.position.y=4.1;roof.scale.set(1.1,1,1.4);
roof.castShadow=true;cabinGroup.add(roof);
// Chimney
const chimneyGeom=new THREE.BoxGeometry(0.8,2.4,0.8);
const stoneMat=new THREE.MeshStandardMaterial({color:0x6e6865,roughness:0.95,flatShading:true});
const chimney=new THREE.Mesh(chimneyGeom,stoneMat);
chimney.position.set(1.8,4.2,1.2);
chimney.castShadow=true;cabinGroup.add(chimney);
// Window
const windowGeom=new THREE.PlaneGeometry(1.2,1.0);
const windowMat=new THREE.MeshStandardMaterial({color:0xffd166,emissive:0xffa500,emissiveIntensity:0.85,roughness:0.2});
const cabinWindow=new THREE.Mesh(windowGeom,windowMat);
cabinWindow.position.set(-1.6,1.8,2.62);
cabinGroup.add(cabinWindow);
const cabinLight=new THREE.PointLight(0xffa500,1.2,16);
cabinLight.position.set(-1.6,2.0,3.5);
cabinGroup.add(cabinLight);
cabinGroup.position.set(CABIN.x,ht(CABIN.x,CABIN.z),CABIN.z);
scene.add(cabinGroup);

// --- The Whispering Monolith Landmark ---
const monolithGroup=new THREE.Group();
const monoGeom=new THREE.CylinderGeometry(0.6,0.9,6.5,4);
const monoMat=new THREE.MeshStandardMaterial({color:0x4a5568,roughness:0.6,flatShading:true});
const monoMesh=new THREE.Mesh(monoGeom,monoMat);
monoMesh.position.y=3.25;monoMesh.castShadow=true;
monolithGroup.add(monoMesh);
// Floating crystal top
const crystalGeom=new THREE.OctahedronGeometry(0.7,0);
const crystalMat=new THREE.MeshStandardMaterial({color:0x64dfdf,emissive:0x00f5d4,emissiveIntensity:1.0,roughness:0.2});
const crystal=new THREE.Mesh(crystalGeom,crystalMat);
crystal.position.y=7.2;monolithGroup.add(crystal);
const monoLight=new THREE.PointLight(0x00f5d4,1.4,14);
monoLight.position.y=7.2;monolithGroup.add(monoLight);
monolithGroup.position.set(MONOLITH.x,ht(MONOLITH.x,MONOLITH.z),MONOLITH.z);
scene.add(monolithGroup);

// --- The Moon Goddess Shrine Landmark ---
const shrineGroup=new THREE.Group();
const shrineBaseGeom=new THREE.CylinderGeometry(2.4,2.6,0.6,8);
const shrineBase=new THREE.Mesh(shrineBaseGeom,stoneMat);
shrineBase.position.y=0.3;shrineBase.castShadow=true;shrineGroup.add(shrineBase);
const shrinePoolGeom=new THREE.CircleGeometry(2.0,16);
shrinePoolGeom.rotateX(-Math.PI/2);
const shrinePoolMat=new THREE.MeshStandardMaterial({color:0x48cae4,emissive:0x0077b6,emissiveIntensity:0.65,roughness:0.1});
const shrinePool=new THREE.Mesh(shrinePoolGeom,shrinePoolMat);
shrinePool.position.y=0.62;shrineGroup.add(shrinePool);
const shrineLight=new THREE.PointLight(0x48cae4,1.2,12);
shrineLight.position.y=1.2;shrineGroup.add(shrineLight);
shrineGroup.position.set(SHRINE.x,ht(SHRINE.x,SHRINE.z),SHRINE.z);
scene.add(shrineGroup);

// --- Fairy Mushroom Ring Landmark ---
const fairyGroup=new THREE.Group();
for(let i=0;i<8;i++){
 const an=i*(Math.PI/4),r=2.2;
 const mStemGeom=new THREE.CylinderGeometry(0.08,0.12,0.6,6);
 const mCapGeom=new THREE.ConeGeometry(0.35,0.3,6);
 const mCapMat=new THREE.MeshStandardMaterial({color:0xd90429,emissive:0x7209b7,emissiveIntensity:0.7,roughness:0.3});
 const stem=new THREE.Mesh(mStemGeom,woodMat);
 const cap=new THREE.Mesh(mCapGeom,mCapMat);
 stem.position.set(Math.cos(an)*r,0.3,Math.sin(an)*r);
 cap.position.set(Math.cos(an)*r,0.65,Math.sin(an)*r);
 stem.castShadow=true;fairyGroup.add(stem);fairyGroup.add(cap);
}
fairyGroup.position.set(FAIRYRING.x,ht(FAIRYRING.x,FAIRYRING.z),FAIRYRING.z);
scene.add(fairyGroup);

// --- 12 Collectible Glowing Leaves ---
const leaves=[];
const leafGeom=new THREE.ConeGeometry(0.35,0.7,4);
leafGeom.rotateZ(Math.PI/6);
const leafMat=new THREE.MeshStandardMaterial({color:0xffb703,emissive:0xfb8500,emissiveIntensity:1.2,roughness:0.3});

for(let i=0;i<12;i++){
 const[x,z]=spot(12,88);
 const leafMesh=new THREE.Mesh(leafGeom,leafMat);
 leafMesh.position.set(x,ht(x,z)+1.2,z);
 const lLight=new THREE.PointLight(0xffa200,0.8,6);
 leafMesh.add(lLight);
 scene.add(leafMesh);
 leaves.push({x,z,mesh:leafMesh,got:false,ph:R()*6,light:lLight});
}

// --- Player Character 3D Model ---
const playerGroup=new THREE.Group();
// Body (Jacket)
const jacketGeom=new THREE.BoxGeometry(0.65,0.85,0.45);
const jacketMat=new THREE.MeshStandardMaterial({color:0xd4623a,roughness:0.8,flatShading:true});
const jacket=new THREE.Mesh(jacketGeom,jacketMat);
jacket.position.y=1.1;jacket.castShadow=true;playerGroup.add(jacket);
// Backpack
const packGeom=new THREE.BoxGeometry(0.48,0.55,0.28);
const packMat=new THREE.MeshStandardMaterial({color:0x7d5634,roughness:0.9,flatShading:true});
const pack=new THREE.Mesh(packGeom,packMat);
pack.position.set(0,1.15,-0.32);pack.castShadow=true;playerGroup.add(pack);
// Head & Hat
const headGeom=new THREE.SphereGeometry(0.24,8,8);
const skinMat=new THREE.MeshStandardMaterial({color:0xfbd1a2,roughness:0.9});
const head=new THREE.Mesh(headGeom,skinMat);
head.position.y=1.72;head.castShadow=true;playerGroup.add(head);
const hatGeom=new THREE.ConeGeometry(0.26,0.32,8);
const hatMat=new THREE.MeshStandardMaterial({color:0xf4a261,roughness:0.9,flatShading:true});
const hat=new THREE.Mesh(hatGeom,hatMat);
hat.position.y=1.92;hat.castShadow=true;playerGroup.add(hat);
// Scarf
const scarfGeom=new THREE.TorusGeometry(0.22,0.07,6,8);
scarfGeom.rotateX(Math.PI/2);
const scarfMat=new THREE.MeshStandardMaterial({color:0xffeedb,roughness:0.9});
const scarf=new THREE.Mesh(scarfGeom,scarfMat);
scarf.position.y=1.52;playerGroup.add(scarf);
// Legs
const legGeom=new THREE.BoxGeometry(0.2,0.7,0.22);
const pantsMat=new THREE.MeshStandardMaterial({color:0x3d4a68,roughness:0.85});
const legL=new THREE.Mesh(legGeom,pantsMat);legL.position.set(-0.16,0.38,0);legL.castShadow=true;playerGroup.add(legL);
const legR=new THREE.Mesh(legGeom,pantsMat);legR.position.set(0.16,0.38,0);legR.castShadow=true;playerGroup.add(legR);

// Brass Hand Lantern
const lanternLight=new THREE.PointLight(0xffb74d,1.5,14);
lanternLight.position.set(0.35,0.9,0.2);
playerGroup.add(lanternLight);

playerGroup.position.set(0,ht(0,0),0);
scene.add(playerGroup);

// --- Roaming Valley Critters ---
const animalList=[];
const critterKinds=[['bunny',0xfaf0ca,8],['fox',0xe76f51,5],['hedgehog',0x7f5539,4]];
let caughtN=0;

for(const[kind,colHex,cnt]of critterKinds){
 for(let i=0;i<cnt;i++){
  const[x,z]=spot(12,90);
  const mesh=new THREE.Group();
  const bodyGeom=new THREE.SphereGeometry(0.32,6,6);
  const cMat=new THREE.MeshStandardMaterial({color:colHex,roughness:0.8,flatShading:true});
  const body=new THREE.Mesh(bodyGeom,cMat);
  body.scale.set(1,0.8,1.4);body.position.y=0.28;body.castShadow=true;mesh.add(body);
  mesh.position.set(x,ht(x,z),z);
  scene.add(mesh);
  animalList.push({kind,mesh,x,z,vx:0,vz:0,ang:R()*6.28,tm:0,go:false,gone:0,hp:R()*6,mystic:false});
 }
}

// Mystic Creatures
const mysticKinds=[['glimmerpuff',0x00f5d4],['moonbun',0xc77dff],['sunwisp',0xffd166]];
for(const[kind,colHex]of mysticKinds){
 const[x,z]=spot(15,90);
 const mesh=new THREE.Group();
 const mGeom=new THREE.IcosahedronGeometry(0.35,1);
 const mMat=new THREE.MeshStandardMaterial({color:colHex,emissive:colHex,emissiveIntensity:0.9,roughness:0.2});
 const mSphere=new THREE.Mesh(mGeom,mMat);
 mSphere.position.y=1.1;mesh.add(mSphere);
 const mLight=new THREE.PointLight(colHex,1.0,8);
 mLight.position.y=1.1;mesh.add(mLight);
 mesh.position.set(x,ht(x,z),z);
 scene.add(mesh);
 animalList.push({kind,mesh,x,z,vx:0,vz:0,ang:R()*6.28,tm:0,go:false,gone:0,hp:R()*6,mystic:true});
}

// --- Seasonal Falling Particles ---
const P_COUNT=140;
const particleGeom=new THREE.BufferGeometry();
const particlePos=new Float32Array(P_COUNT*3);
for(let i=0;i<P_COUNT;i++){
 particlePos[i*3]=(R()-0.5)*90;
 particlePos[i*3+1]=2+R()*25;
 particlePos[i*3+2]=(R()-0.5)*90;
}
particleGeom.setAttribute('position',new THREE.BufferAttribute(particlePos,3));
const particleMat=new THREE.PointsMaterial({
 size:0.45,color:0xf09a32,transparent:true,opacity:0.8
});
const particleSystem=new THREE.Points(particleGeom,particleMat);
scene.add(particleSystem);

function updateParticleColors(seasonKey){
 if(seasonKey==='spring')particleMat.color.setHex(0xffb7c5);
 else if(seasonKey==='summer')particleMat.color.setHex(0xffea00);
 else if(seasonKey==='winter')particleMat.color.setHex(0xf8f9fa);
 else particleMat.color.setHex(0xf09a32);
}

// --- Spirit Wisps ---
const spiritWisps=[];
const wispGeom=new THREE.SphereGeometry(0.2,6,6);
const wispMat=new THREE.MeshStandardMaterial({color:0x00f5d4,emissive:0x00f5d4,emissiveIntensity:1.5});

// --- Gameplay State ---
let started=false,won=false,lit=false,got=0,T=0,toastT=0;
let a=0,ca=0,camDist=7.0,camHeight=3.4;
let jh=0,pjv=0,jumpLatch=0,moving=0,walk=0;
const pw={speed:0,jump:0,starlight:0,lakeStrider:0};
let inCabin=false,hearthLeaves=0;
const keys={};

addEventListener('keydown',e=>{keys[e.code]=1});
addEventListener('keyup',e=>{keys[e.code]=0});

// Drag to look around
let isDragging=false,lastPointerX=0;
addEventListener('pointerdown',e=>{
 if(e.target===renderer.domElement){
  isDragging=true;lastPointerX=e.clientX;
 }
});
addEventListener('pointermove',e=>{
 if(isDragging){
  const dx=e.clientX-lastPointerX;
  ca+=dx*0.0055;
  lastPointerX=e.clientX;
 }
});
const stopDrag=()=>{isDragging=false};
addEventListener('pointerup',stopDrag);
addEventListener('pointercancel',stopDrag);

// Mouse wheel zoom
addEventListener('wheel',e=>{
 const delta=Math.sign(e.deltaY)*0.6;
 camDist=Math.max(4.5,Math.min(12.0,camDist+delta));
},{passive:true});

const toast=t=>{const el=document.getElementById('toast');el.textContent=t;el.style.opacity=1;toastT=2.4};

// --- Season Switching ---
function setSeason(s,silent=false){
 if(!SEASONS.includes(s))return;
 currentSeason=s;
 updateTerrainColors(s);
 updateParticleColors(s);
 for(const tiers of pineMeshes){
  const list=pineMaterials[s];
  tiers.forEach((cone,idx)=>{
   cone.material=list[idx%list.length];
   if(cone.snowCap)cone.snowCap.visible=(s==='winter');
  });
 }
 const oakList=oakMaterials[s];
 oakCanopies.forEach((f,idx)=>{f.material=oakList[idx%oakList.length]});
 document.querySelectorAll('#season-btns button').forEach(b=>{
  b.classList.toggle('active',b.dataset.s===s);
 });
 document.getElementById('season-hud').textContent=SEASON_NAMES[s];
 if(!silent)toast('Season shifting to '+SEASON_NAMES[s]);
}

// --- Time of Day Updates ---
function updateTOD(tm){
 timeOfDay=tm;
 const isDay=tm>0.2&&tm<0.8;
 const sunFactor=Math.max(0,Math.sin(tm*Math.PI));
 // Ambient light
 ambientLight.intensity=0.12+sunFactor*0.65;
 // Sun position & intensity
 sunLight.position.set(Math.cos(tm*Math.PI*2)*60,Math.max(10,Math.sin(tm*Math.PI*2)*80),30);
 sunLight.intensity=sunFactor*1.15;
 
 if(tm<=0.2||tm>=0.8){
  // Deep dark night
  scene.background=new THREE.Color(0x060913);
  scene.fog.color.setHex(0x0a0f1d);
  ambientLight.color.setHex(0x1a263d);
  lanternLight.intensity=2.2;
 }else{
  // Day / Sunset
  const pal=SEASON_PALETTES[currentSeason];
  scene.background=new THREE.Color(pal.skyBot);
  scene.fog.color.setHex(pal.fog);
  ambientLight.color.setHex(0xffffff);
  lanternLight.intensity=0.6;
 }
}
updateTOD(timeOfDay);

function setTOD(t){
 updateTOD(t);
 document.querySelectorAll('#tod-btns button').forEach(b=>{
  b.classList.toggle('active',Math.abs(parseFloat(b.dataset.t)-t)<.05);
 });
}

function setWeather(w){
 weather=w;
 document.querySelectorAll('#weather-btns button').forEach(b=>{
  b.classList.toggle('active',b.dataset.w===w);
 });
 if(w==='fog')scene.fog.density=0.035;
 else scene.fog.density=0.009;
 if(w==='storm')toast('Thunderstorm rolling in');
 else if(w==='rain')toast(currentSeason==='winter'?'Snow flurry falling':'Gentle rain falling');
 else if(w==='fog')toast('Misty fog descending');
 else toast('Skies clearing up');
}

// --- Interaction System ---
let activePromptAction=null;
function updateInteractionPrompts(){
 const promptBtn=document.getElementById('interact-prompt');
 if(!promptBtn)return;
 if(!started||inCabin){promptBtn.hidden=true;return}
 
 const dCabin=Math.hypot(playerGroup.position.x-CABIN.x,playerGroup.position.z-CABIN.z);
 const dMono=Math.hypot(playerGroup.position.x-MONOLITH.x,playerGroup.position.z-MONOLITH.z);
 const dShrine=Math.hypot(playerGroup.position.x-SHRINE.x,playerGroup.position.z-SHRINE.z);
 const dRing=Math.hypot(playerGroup.position.x-FAIRYRING.x,playerGroup.position.z-FAIRYRING.z);

 if(dRing<2.6){
  if(jh<=0.2){
   jh=1.2;pjv=18;
   audio.playSpring();
   toast('✨ Fairy Mushroom Spring! Soaring high!');
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
   const d=Math.hypot(l.x-playerGroup.position.x,l.z-playerGroup.position.z);
   if(d<minD){minD=d;nearest=l}
  }
 }
 if(nearest){
  pw.starlight=30;
  for(let i=0;i<8;i++){
   const wMesh=new THREE.Mesh(wispGeom,wispMat);
   wMesh.position.copy(monolithGroup.position);
   wMesh.position.y+=6;
   scene.add(wMesh);
   spiritWisps.push({mesh:wMesh,tx:nearest.x,tz:nearest.z,life:1.2,ph:i*0.4});
  }
  toast(`✨ The Monolith speaks: 'A spirit wisp guides you (~${Math.round(minD)} paces away)!'`);
 }else{
  toast('✨ The Monolith resonates: All 12 leaves are gathered!');
 }
}

function activateShrine(){
 audio.playEthereal(440);
 pw.lakeStrider=50;
 toast('🌙 Blessed by the Moon Shrine! You can sprint across the lake waters!');
}

// --- Main Animation Loop ---
let lastT=performance.now();
let fpsCount=0,fpsTime=0;

function animate(now){
 requestAnimationFrame(animate);
 const dt=Math.min(0.05,(now-lastT)/1000);
 lastT=now;
 T+=dt;

 fpsCount++;fpsTime+=dt;
 if(fpsTime>=0.5){
  const curFps=Math.round(fpsCount/fpsTime);
  fpsCount=0;fpsTime=0;
  document.getElementById('fps-display').textContent=`FPS: ${curFps} (WebGL 3D)`;
 }

 // Season & Weather auto timers
 if(autoSeason){
  seasonTimer-=dt;
  if(seasonTimer<=0){
   seasonTimer=50.0;
   const nextIdx=(SEASONS.indexOf(currentSeason)+1)%SEASONS.length;
   setSeason(SEASONS[nextIdx]);
  }
 }
 if(autoTime){
  timeOfDay=(timeOfDay+dt*0.011)%1.0;
  updateTOD(timeOfDay);
 }
 if(autoWeather){
  weatherTimer-=dt;
  if(weatherTimer<=0){
   weatherTimer=25+Math.random()*20;
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
 if(lightningFlash>0){
  lightningFlash=Math.max(0,lightningFlash-dt*3.8);
  ambientLight.intensity=0.8+lightningFlash*2.5;
 }

 // Buff timers
 pw.speed=Math.max(0,pw.speed-dt);
 pw.jump=Math.max(0,pw.jump-dt);
 pw.starlight=Math.max(0,pw.starlight-dt);
 pw.lakeStrider=Math.max(0,pw.lakeStrider-dt);

 const tStr=[];
 if(pw.speed>0)tStr.push('Swift '+Math.ceil(pw.speed)+'s');
 if(pw.jump>0)tStr.push('Moon leap '+Math.ceil(pw.jump)+'s');
 if(pw.lakeStrider>0)tStr.push('Lake Strider '+Math.ceil(pw.lakeStrider)+'s');
 if(pw.starlight>0)tStr.push('Starlight Sight '+Math.ceil(pw.starlight)+'s');
 document.getElementById('pw').textContent=tStr.join('   ');

 // Player Jumping & Gravity
 if(keys.Space&&!jumpLatch&&jh<=0){
  pjv=pw.jump>0?13:7.2;jumpLatch=1;
  audio.playTone(320,'sine',0.15,0.1);
 }
 if(!keys.Space)jumpLatch=0;
 jh+=pjv*dt;pjv-=22*dt;
 if(jh<=0){jh=0;pjv=0}

 // Movement input
 let fx=0,fz=0,sp=(keys.ShiftLeft||keys.ShiftRight)?1.75:1;
 if(keys.KeyW) { fx+=Math.sin(ca); fz+=Math.cos(ca); }
 if(keys.KeyS) { fx-=Math.sin(ca); fz-=Math.cos(ca); }
 if(keys.KeyA) { fx-=Math.cos(ca); fz+=Math.sin(ca); }
 if(keys.KeyD) { fx+=Math.cos(ca); fz-=Math.sin(ca); }
 if(keys.ArrowUp)   { fx+=Math.sin(ca); fz+=Math.cos(ca); }
 if(keys.ArrowDown) { fx-=Math.sin(ca); fz-=Math.cos(ca); }
 if(keys.ArrowLeft)  ca-=dt*2.2;
 if(keys.ArrowRight) ca+=dt*2.2;

 const mLen=Math.hypot(fx,fz);
 if(mLen>0.05){
  const nx=fx/mLen,nz=fz/mLen,tAngle=Math.atan2(nx,nz);
  let da=tAngle-a;da=Math.atan2(Math.sin(da),Math.cos(da));
  a+=da*Math.min(1,dt*12);
  const onWater=inPond(playerGroup.position.x,playerGroup.position.z);
  const slow=(onWater&&pw.lakeStrider<=0)?0.45:1;
  const v=7.2*sp*slow*(pw.speed>0?1.75:1);
  playerGroup.position.x+=nx*v*dt;
  playerGroup.position.z+=nz*v*dt;
  moving=1;walk+=v*dt*1.5;
  if(jh<=0.1){
   audio.playStep(onWater?'water':currentSeason==='winter'?'snow':'grass');
  }
 }else{
  moving=0;
 }

 const rDist=Math.hypot(playerGroup.position.x,playerGroup.position.z);
 if(rDist>98){playerGroup.position.x*=98/rDist;playerGroup.position.z*=98/rDist}
 playerGroup.position.y=ht(playerGroup.position.x,playerGroup.position.z)+jh;
 playerGroup.rotation.y=a;

 // Leg walking animation
 legL.rotation.x=moving?Math.sin(walk*2)*0.55:0;
 legR.rotation.x=moving?-Math.sin(walk*2)*0.55:0;
 scarf.rotation.y=Math.sin(T*3)*0.15;

 // Leaves floating & collection
 for(const l of leaves){
  if(!l.got){
   l.mesh.rotation.y+=dt*1.8;
   l.mesh.position.y=ht(l.x,l.z)+1.2+Math.sin(T*2.5+l.ph)*0.25;
   if(Math.hypot(playerGroup.position.x-l.x,playerGroup.position.z-l.z)<2.2){
    l.got=true;l.mesh.visible=false;got++;
    document.getElementById('n').textContent=got;
    audio.playChime([523,659,784,1046]);
    if(got<12)toast(got+' of 12 leaves found');
    else{toast('All 12 found! Carry them to the cabin hearth!');document.getElementById('obj').textContent='Bring them to the cabin'}
   }
  }
 }

 // Animals AI
 for(const o of animalList){
  if(o.gone>0){
   o.gone-=dt;if(o.gone<=0){const s=spot(20,90);o.x=s[0];o.z=s[1];o.mesh.visible=true}
   continue;
  }
  const dx=o.x-playerGroup.position.x,dz=o.z-playerGroup.position.z,d=Math.hypot(dx,dz);let aSpeed=0;
  if(started&&d<10){o.ang=Math.atan2(dx,dz)+Math.sin(T*3+o.hp)*0.6;aSpeed=7.5}
  else{o.tm-=dt;if(o.tm<=0){o.tm=1+Math.random()*2.5;o.go=Math.random()<0.55;o.ang=Math.random()*6.283}aSpeed=o.go?1.8:0}
  o.vx=Math.sin(o.ang)*aSpeed;o.vz=Math.cos(o.ang)*aSpeed;
  o.x+=o.vx*dt;o.z+=o.vz*dt;
  o.mesh.position.set(o.x,ht(o.x,o.z)+(aSpeed>0?Math.abs(Math.sin(T*8))*0.25:0),o.z);
  o.mesh.rotation.y=o.ang;

  if(started&&d<1.7){
   o.gone=8;o.mesh.visible=false;caughtN++;
   document.getElementById('cn').textContent=caughtN;
   toast(o.mystic?power(o):'Caught a '+o.kind+'!');
   audio.playChime([659,784,988,1318]);
  }
 }

 // Spirit Wisps Movement
 for(let i=spiritWisps.length-1;i>=0;i--){
  const w=spiritWisps[i];
  w.life-=dt*0.8;
  if(w.life<=0){scene.remove(w.mesh);spiritWisps.splice(i,1);continue}
  const wdx=w.tx-w.mesh.position.x,wdz=w.tz-w.mesh.position.z,wd=Math.hypot(wdx,wdz);
  if(wd>1.2){
   w.mesh.position.x+=wdx/wd*18*dt+Math.sin(T*6+w.ph)*5*dt;
   w.mesh.position.z+=wdz/wd*18*dt+Math.cos(T*6+w.ph)*5*dt;
   w.mesh.position.y=ht(w.mesh.position.x,w.mesh.position.z)+2.5;
  }
 }

 // Seasonal Falling Particles
 const pPos=particleGeom.attributes.position.array;
 for(let i=0;i<P_COUNT;i++){
  pPos[i*3+1]-=(3.5+Math.sin(i))*dt;
  pPos[i*3]+=Math.sin(T+i)*0.8*dt;
  if(pPos[i*3+1]<0){
   pPos[i*3+1]=22;
   pPos[i*3]=playerGroup.position.x+(R()-0.5)*70;
   pPos[i*3+2]=playerGroup.position.z+(R()-0.5)*70;
  }
 }
 particleGeom.attributes.position.needsUpdate=true;

 // Smooth Camera Follow & LookAt
 camera.position.x=playerGroup.position.x-Math.sin(ca)*camDist;
 camera.position.z=playerGroup.position.z-Math.cos(ca)*camDist;
 camera.position.y=playerGroup.position.y+camHeight;
 camera.lookAt(playerGroup.position.x,playerGroup.position.y+1.2,playerGroup.position.z);

 updateInteractionPrompts();
 if(toastT>0&&(toastT-=dt)<=0)document.getElementById('toast').style.opacity=0;

 renderer.render(scene,camera);
 drawMinimap();
}
requestAnimationFrame(animate);

function power(o){
 if(o.kind==='glimmerpuff'){pw.speed=12;return'Swift! You feel light on your feet'}
 if(o.kind==='moonbun'){pw.jump=14;return'Moon leap! Press Space to soar high'}
 pw.speed=18;pw.jump=18;return'Sunwisp! Blazing speed and radiant leap together!';
}

// --- Minimap ---
const mapCv=document.getElementById('minimap-canvas'),mapG=mapCv.getContext('2d');
function drawMinimap(){
 mapG.clearRect(0,0,110,110);
 const cx=55,cy=55,sc=110/220;
 const m=(x,z)=>[cx+x*sc,cy+z*sc];
 // Pond
 const pp=m(POND.x,POND.z);
 mapG.fillStyle='#64b5f6';mapG.beginPath();mapG.arc(pp[0],pp[1],POND.rx*sc,0,7);mapG.fill();
 // Cabin
 const cp=m(CABIN.x,CABIN.z);
 mapG.fillStyle='#d4623a';mapG.fillRect(cp[0]-3,cp[1]-3,6,6);
 // Monolith & Shrine
 const mp=m(MONOLITH.x,MONOLITH.z);mapG.fillStyle='#00f5d4';mapG.beginPath();mapG.arc(mp[0],mp[1],3,0,7);mapG.fill();
 const sp=m(SHRINE.x,SHRINE.z);mapG.fillStyle='#48cae4';mapG.fillRect(sp[0]-2,sp[1]-2,4,4);
 // Leaves
 for(const l of leaves)if(!l.got){
  const lp=m(l.x,l.z);mapG.fillStyle='#ffb703';mapG.beginPath();mapG.arc(lp[0],lp[1],2.5,0,7);mapG.fill();
 }
 // Player
 const plp=m(playerGroup.position.x,playerGroup.position.z);
 mapG.fillStyle='#2b2d42';mapG.beginPath();mapG.arc(plp[0],plp[1],4,0,7);mapG.fill();
}

// --- Window Resize ---
addEventListener('resize',()=>{
 camera.aspect=innerWidth/innerHeight;
 camera.updateProjectionMatrix();
 renderer.setSize(innerWidth,innerHeight);
});

// --- UI Event Handlers ---
document.getElementById('go').onclick=()=>{started=true;document.getElementById('start').hidden=true;initAudio()};
document.getElementById('again').onclick=()=>{document.getElementById('win').hidden=true};

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
document.getElementById('auto-time').onchange=e=>{autoTime=e.target.checked};
document.getElementById('auto-weather').onchange=e=>{autoWeather=e.target.checked};

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
 if(e.code==='KeyE'){
  if(inCabin)closeCabin();
  else if(activePromptAction)activateInteraction();
 }
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
 playerGroup.position.set(CABIN.x,ht(CABIN.x,CABIN.z),CABIN.z-6.5);
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
 updateTOD(timeOfDay);
 if(weather==='storm')setWeather('clear');
 toast('Rested by the warm fire. A new time of day begins');
 const wNote=weather==='storm'?'Fierce thunderstorm howling outside the cedar walls':weather==='rain'?(currentSeason==='winter'?'Soft snowfall blanketing the windowsill':'Gentle rain tapping against the window'):weather==='fog'?'Misty fog blanketing the quiet pine trees':'Golden valley light streaming through the glass';
 document.getElementById('cabin-outside-note').textContent='Window: '+wNote;
};
</script></body></html>
'''

with open('Amber Valley.html', 'w', encoding='utf-8') as f:
    f.write(threejs_valley)

print("Amber Valley.html completely upgraded to Three.js! Size:", len(threejs_valley))
