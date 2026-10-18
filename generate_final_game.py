# Comprehensive generator that creates the complete modular and bundled full-fledged Amber Valley game
import os

def build():
    print("Building full-fledged game...")
    os.makedirs('css', exist_ok=True)
    os.makedirs('js', exist_ok=True)
    os.makedirs('assets', exist_ok=True)

    # 1. css/style.css
    with open('css/style.css', 'w', encoding='utf-8') as f:
        f.write(r'''/* Amber Valley - Master Stylesheet */
:root {
  --ink: #382414;
  --paper: #fff5e4;
  --accent: #d25b2a;
  --accent-glow: rgba(210, 91, 42, 0.4);
  color-scheme: light dark;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --ink: #faecd6;
    --paper: #281a13;
    --accent: #f0834e;
    --accent-glow: rgba(240, 131, 78, 0.45);
  }
}
:root[data-theme="dark"] {
  --ink: #faecd6;
  --paper: #281a13;
  --accent: #f0834e;
}

html, body {
  height: 100%;
  margin: 0;
  overflow: hidden;
  background: #0b111c;
  font-family: 'Nunito', Gaegu, sans-serif;
  color: var(--ink);
  user-select: none;
  -webkit-user-select: none;
  touch-action: none;
}

canvas#game-canvas {
  display: block;
  width: 100%;
  height: 100%;
  touch-action: none;
}

#hud {
  position: fixed;
  top: calc(14px + env(safe-area-inset-top));
  left: 16px;
  background: rgba(255, 245, 228, 0.92);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  padding: 8px 18px;
  border-radius: 18px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.22);
  z-index: 10;
  pointer-events: none;
  border: 1px solid rgba(255, 255, 255, 0.5);
}
:root[data-theme="dark"] #hud {
  background: rgba(40, 26, 19, 0.92);
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.hud-title {
  font-family: 'Gaegu', cursive;
  font-size: 26px;
  font-weight: 700;
  line-height: 1.1;
  color: var(--ink);
}
.hud-sub {
  font-size: 15px;
  font-weight: 600;
  opacity: 0.92;
  margin-top: 2px;
}
.hud-buffs {
  font-size: 13px;
  font-weight: 800;
  color: #c04218;
  margin-top: 3px;
  letter-spacing: 0.3px;
}

#top-right-bar {
  position: fixed;
  top: calc(14px + env(safe-area-inset-top));
  right: 16px;
  display: flex;
  gap: 10px;
  z-index: 25;
}
.top-btn {
  background: rgba(255, 245, 228, 0.94);
  backdrop-filter: blur(8px);
  color: var(--ink);
  width: 44px;
  height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 14px;
  font-size: 21px;
  border: 0;
  cursor: pointer;
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.2);
  transition: transform 0.15s, background-color 0.2s;
}
:root[data-theme="dark"] .top-btn {
  background: rgba(40, 26, 19, 0.94);
}
.top-btn:hover {
  transform: scale(1.08);
}
.top-btn:active {
  transform: scale(0.95);
}

#toast {
  position: fixed;
  left: 50%;
  top: 18%;
  transform: translateX(-50%);
  font-family: 'Gaegu', cursive;
  font-size: 28px;
  font-weight: 700;
  color: #fff8eb;
  background: rgba(42, 24, 16, 0.88);
  backdrop-filter: blur(6px);
  padding: 8px 24px;
  border-radius: 20px;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.35);
  opacity: 0;
  transition: opacity 0.35s, transform 0.35s;
  pointer-events: none;
  text-align: center;
  z-index: 20;
}

.ov {
  position: fixed;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(12, 16, 25, 0.68);
  backdrop-filter: blur(5px);
  padding: env(safe-area-inset-top) 16px env(safe-area-inset-bottom);
  z-index: 35;
  transition: opacity 0.25s;
}
.ov[hidden] {
  display: none;
}
.card {
  background: var(--paper);
  max-width: 460px;
  width: 90%;
  padding: 26px 30px;
  border-radius: 24px;
  text-align: center;
  box-shadow: 0 12px 36px rgba(0, 0, 0, 0.38);
  border: 1px solid rgba(255, 255, 255, 0.2);
}
.card h1 {
  font-family: 'Gaegu', cursive;
  margin: 0 0 10px;
  font-size: 46px;
  line-height: 1;
  color: var(--accent);
}
.card p {
  margin: 10px 0;
  font-size: 16px;
  line-height: 1.45;
}
button.action-btn {
  font-family: 'Gaegu', cursive;
  font-size: 26px;
  font-weight: 700;
  background: var(--accent);
  color: #fff;
  border: 0;
  border-radius: 16px;
  padding: 9px 28px;
  margin-top: 14px;
  cursor: pointer;
  box-shadow: 0 4px 14px var(--accent-glow);
  transition: transform 0.15s, box-shadow 0.15s;
}
button.action-btn:hover {
  transform: scale(1.05);
  box-shadow: 0 6px 20px var(--accent-glow);
}
button.action-btn:active {
  transform: scale(0.97);
}

.settings-card {
  max-width: 460px;
  text-align: left;
  padding: 22px 26px;
  max-height: 88vh;
  overflow-y: auto;
}
.settings-card h2 {
  font-family: 'Gaegu', cursive;
  margin: 0;
  font-size: 38px;
  color: var(--accent);
}
.setting-group {
  margin: 14px 0;
}
.setting-label {
  font-size: 15px;
  font-weight: 800;
  display: block;
  margin-bottom: 6px;
  color: var(--ink);
  letter-spacing: 0.2px;
}
.btn-row {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}
.btn-row button {
  flex: 1 1 20%;
  min-width: 70px;
  margin-top: 0;
  padding: 7px 10px;
  font-size: 14px;
  font-weight: 700;
  border-radius: 12px;
  background: rgba(0, 0, 0, 0.07);
  color: var(--ink);
  border: 1px solid rgba(0,0,0,0.06);
  cursor: pointer;
  transition: all 0.15s;
}
.btn-row button.active {
  background: var(--accent);
  color: #fff;
  border-color: var(--accent);
  box-shadow: 0 2px 10px var(--accent-glow);
}
.check-label {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 14px;
  font-weight: 600;
  margin-top: 6px;
  cursor: pointer;
  user-select: none;
}
.check-label input {
  accent-color: var(--accent);
  width: 17px;
  height: 17px;
}

.cabin-card {
  max-width: 480px;
  text-align: left;
  padding: 24px 28px;
}
.hearth-box {
  background: rgba(210, 91, 42, 0.12);
  border: 2px dashed var(--accent);
  border-radius: 18px;
  padding: 16px;
  margin: 12px 0;
  text-align: center;
}
.cabin-actions {
  display: flex;
  gap: 10px;
  margin: 14px 0;
}
.cabin-btn {
  flex: 1;
  background: var(--paper);
  border: 2px solid var(--accent);
  color: var(--ink);
  font-size: 16px;
  font-weight: 800;
  padding: 10px 8px;
  border-radius: 16px;
  cursor: pointer;
  transition: all 0.15s;
  text-align: center;
}
.cabin-btn:hover {
  background: var(--accent);
  color: #fff;
}

#interact-prompt {
  position: fixed;
  bottom: 26px;
  left: 50%;
  transform: translateX(-50%);
  background: var(--accent);
  color: #fff;
  font-family: 'Gaegu', cursive;
  font-size: 24px;
  font-weight: 700;
  border: 0;
  border-radius: 20px;
  padding: 10px 28px;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.4);
  cursor: pointer;
  z-index: 20;
  transition: transform 0.15s;
  animation: promptBounce 1.8s infinite ease-in-out;
}
#interact-prompt:hover {
  transform: translateX(-50%) scale(1.06);
}
@keyframes promptBounce {
  0%, 100% { transform: translateX(-50%) translateY(0); }
  50% { transform: translateX(-50%) translateY(-7px); }
}

#minimap-canvas {
  position: fixed;
  bottom: 16px;
  right: 16px;
  width: 110px;
  height: 110px;
  border-radius: 50%;
  border: 3px solid rgba(56, 36, 20, 0.65);
  background: rgba(255, 245, 228, 0.88);
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.3);
  z-index: 10;
  pointer-events: none;
}

#touch-controls {
  position: fixed;
  bottom: 16px;
  left: 16px;
  width: 120px;
  height: 120px;
  z-index: 25;
  display: none;
  touch-action: none;
}
#touch-base {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.18);
  border: 2px solid rgba(255, 255, 255, 0.35);
  backdrop-filter: blur(4px);
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}
#touch-stick {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  background: var(--accent);
  box-shadow: 0 2px 10px rgba(0,0,0,0.3);
  position: absolute;
  pointer-events: none;
  transform: translate(0, 0);
  transition: transform 0.05s ease-out;
}
#mobile-buttons {
  position: fixed;
  bottom: 24px;
  right: 136px;
  display: none;
  gap: 12px;
  z-index: 25;
}
.mobile-btn {
  width: 52px;
  height: 52px;
  border-radius: 50%;
  background: rgba(255, 245, 228, 0.92);
  border: 2px solid var(--accent);
  color: var(--accent);
  font-size: 22px;
  font-weight: 800;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  box-shadow: 0 4px 12px rgba(0,0,0,0.25);
  touch-action: none;
}
.mobile-btn:active, .mobile-btn.pressed {
  background: var(--accent);
  color: #fff;
}
''')

    # 2. js/audio.js
    with open('js/audio.js', 'w', encoding='utf-8') as f:
        f.write(r'''// Procedural Web Audio Engine for Amber Valley
class ProceduralAudio {
  constructor() {
    this.ctx = null;
    this.enabled = true;
    this.lastStep = 0;
  }
  init() {
    if (this.ctx) return;
    const AudioCtx = window.AudioContext || window.webkitAudioContext;
    if (AudioCtx) {
      this.ctx = new AudioCtx();
      if (this.ctx.state === 'suspended') this.ctx.resume();
    }
  }
  playTone(freq, type = 'sine', dur = 0.2, vol = 0.15, delay = 0) {
    if (!this.enabled || !this.ctx) return;
    try {
      const t = this.ctx.currentTime + delay;
      const osc = this.ctx.createOscillator(), gn = this.ctx.createGain();
      osc.type = type; osc.frequency.setValueAtTime(freq, t);
      gn.gain.setValueAtTime(vol, t);
      gn.gain.exponentialRampToValueAtTime(0.0001, t + dur);
      osc.connect(gn); gn.connect(this.ctx.destination);
      osc.start(t); osc.stop(t + dur);
    } catch(e) {}
  }
  playChime(freqs = [523, 659, 784, 1046], dur = 0.4) {
    if (!this.enabled || !this.ctx) return;
    freqs.forEach((f, i) => this.playTone(f, 'sine', dur + i * 0.08, 0.12, i * 0.07));
  }
  playEthereal(root = 440) {
    if (!this.enabled || !this.ctx) return;
    [root, root * 1.25, root * 1.5, root * 2].forEach((f, i) => this.playTone(f, 'triangle', 1.4, 0.08, i * 0.05));
  }
  playSpring() {
    if (!this.enabled || !this.ctx) return;
    try {
      const t = this.ctx.currentTime, osc = this.ctx.createOscillator(), gn = this.ctx.createGain();
      osc.type = 'sine'; osc.frequency.setValueAtTime(260, t);
      osc.frequency.exponentialRampToValueAtTime(950, t + 0.35);
      gn.gain.setValueAtTime(0.18, t); gn.gain.exponentialRampToValueAtTime(0.001, t + 0.38);
      osc.connect(gn); gn.connect(this.ctx.destination);
      osc.start(t); osc.stop(t + 0.38);
    } catch(e) {}
  }
  playStep(surface = 'grass') {
    if (!this.enabled || !this.ctx) return;
    const now = performance.now();
    if (now - this.lastStep < 260) return;
    this.lastStep = now;
    try {
      const t = this.ctx.currentTime;
      const buf = this.ctx.createBuffer(1, this.ctx.sampleRate * 0.05, this.ctx.sampleRate);
      const d = buf.getChannelData(0);
      for (let i = 0; i < d.length; i++) d[i] = (Math.random() * 2 - 1) * Math.exp(-i / (this.ctx.sampleRate * 0.012));
      const src = this.ctx.createBufferSource(); src.buffer = buf;
      const filter = this.ctx.createBiquadFilter(); filter.type = 'lowpass';
      filter.frequency.value = surface === 'water' ? 600 : surface === 'snow' ? 1100 : 450;
      const gn = this.ctx.createGain(); gn.gain.setValueAtTime(surface === 'water' ? 0.14 : 0.06, t);
      src.connect(filter); filter.connect(gn); gn.connect(this.ctx.destination);
      src.start(t);
    } catch(e) {}
  }
  playThunder() {
    if (!this.enabled || !this.ctx) return;
    try {
      const t = this.ctx.currentTime, len = this.ctx.sampleRate * 1.8;
      const buf = this.ctx.createBuffer(1, len, this.ctx.sampleRate);
      const d = buf.getChannelData(0);
      for (let i = 0; i < len; i++) d[i] = (Math.random() * 2 - 1) * Math.exp(-i / (this.ctx.sampleRate * 0.6));
      const src = this.ctx.createBufferSource(); src.buffer = buf;
      const filter = this.ctx.createBiquadFilter(); filter.type = 'lowpass'; filter.frequency.value = 180;
      const gn = this.ctx.createGain(); gn.gain.setValueAtTime(0.45, t); gn.gain.linearRampToValueAtTime(0.01, t + 1.8);
      src.connect(filter); filter.connect(gn); gn.connect(this.ctx.destination);
      src.start(t);
    } catch(e) {}
  }
}
window.audio = new ProceduralAudio();
window.initAudio = () => { window.audio.init(); };
addEventListener('pointerdown', window.initAudio, { once: true });
addEventListener('keydown', window.initAudio, { once: true });
''')

    # 3. js/collision.js
    with open('js/collision.js', 'w', encoding='utf-8') as f:
        f.write(r'''// Solid Collision Physics System for Amber Valley
class CollisionSystem {
  constructor() {
    this.colliders = [];
  }
  addCircle(x, z, radius, tag = 'obstacle') {
    this.colliders.push({ type: 'circle', x, z, r: radius, tag });
  }
  addBox(minX, maxX, minZ, maxZ, tag = 'building') {
    this.colliders.push({ type: 'box', minX, maxX, minZ, maxZ, tag });
  }
  resolve(px, pz, radius = 0.45) {
    let rx = px;
    let rz = pz;
    for (const c of this.colliders) {
      if (c.type === 'circle') {
        const dx = rx - c.x;
        const dz = rz - c.z;
        const dist = Math.hypot(dx, dz);
        const minDist = c.r + radius;
        if (dist < minDist && dist > 0.0001) {
          const push = (minDist - dist) / dist;
          rx += dx * push;
          rz += dz * push;
        }
      } else if (c.type === 'box') {
        const closestX = Math.max(c.minX, Math.min(c.maxX, rx));
        const closestZ = Math.max(c.minZ, Math.min(c.maxZ, rz));
        const dx = rx - closestX;
        const dz = rz - closestZ;
        const dist = Math.hypot(dx, dz);
        if (dist < radius) {
          if (dist > 0.0001) {
            const push = (radius - dist) / dist;
            rx += dx * push;
            rz += dz * push;
          } else {
            const dLeft = Math.abs(rx - c.minX);
            const dRight = Math.abs(rx - c.maxX);
            const dNear = Math.abs(rz - c.minZ);
            const dFar = Math.abs(rz - c.maxZ);
            const minD = Math.min(dLeft, dRight, dNear, dFar);
            if (minD === dLeft) rx = c.minX - radius;
            else if (minD === dRight) rx = c.maxX + radius;
            else if (minD === dNear) rz = c.minZ - radius;
            else rz = c.maxZ + radius;
          }
        }
      }
    }
    const rDist = Math.hypot(rx, rz);
    if (rDist > 98) {
      rx *= 98 / rDist;
      rz *= 98 / rDist;
    }
    return { x: rx, z: rz };
  }
}
window.collisionSystem = new CollisionSystem();
''')

    # 4. js/textures.js
    with open('js/textures.js', 'w', encoding='utf-8') as f:
        f.write(r'''// Procedural Textures Generator for Amber Valley
function createProceduralNoiseCanvas(w, h, noiseFn) {
  const cv = document.createElement('canvas');
  cv.width = w; cv.height = h;
  const ctx = cv.getContext('2d');
  const imgData = ctx.createImageData(w, h);
  const data = imgData.data;
  for (let y = 0; y < h; y++) {
    for (let x = 0; x < w; x++) {
      const idx = (y * w + x) * 4;
      const [r, g, b, a] = noiseFn(x, y, w, h);
      data[idx] = r; data[idx + 1] = g; data[idx + 2] = b; data[idx + 3] = a !== undefined ? a : 255;
    }
  }
  ctx.putImageData(imgData, 0, 0);
  return cv;
}

window.terrainCanvas = createProceduralNoiseCanvas(256, 256, (x, y, w, h) => {
  const n1 = Math.sin(x * 0.173 + y * 0.291) * 14 + Math.sin(x * 0.431 - y * 0.267) * 9 + Math.cos(x * 0.817 + y * 0.653) * 6;
  const speckle = (Math.random() - 0.5) * 22;
  const base = Math.max(80, Math.min(240, 195 + n1 + speckle));
  return [base, base, base * 0.94];
});
window.terrainTexture = new THREE.CanvasTexture(window.terrainCanvas);
window.terrainTexture.wrapS = THREE.RepeatWrapping;
window.terrainTexture.wrapT = THREE.RepeatWrapping;
window.terrainTexture.repeat.set(40, 40);

window.barkCanvas = createProceduralNoiseCanvas(128, 256, (x, y, w, h) => {
  const stripe = Math.sin(x * 0.55) * 25 + Math.sin(x * 1.6 + y * 0.12) * 18;
  const grain = (Math.random() - 0.5) * 22;
  const val = Math.max(40, Math.min(190, 105 + stripe + grain));
  return [val * 0.85, val * 0.58, val * 0.42];
});
window.barkTexture = new THREE.CanvasTexture(window.barkCanvas);
window.barkTexture.wrapS = THREE.RepeatWrapping;
window.barkTexture.wrapT = THREE.RepeatWrapping;
window.barkTexture.repeat.set(2, 4);

window.plankCanvas = createProceduralNoiseCanvas(256, 256, (x, y, w, h) => {
  const plankH = 32;
  const isSeam = (y % plankH) < 2;
  if (isSeam) return [32, 20, 14];
  const grain = Math.sin(x * 0.15 + y * 0.05) * 15 + (Math.random() - 0.5) * 20;
  const base = 120 + grain;
  return [base * 0.9, base * 0.65, base * 0.45];
});
window.plankTexture = new THREE.CanvasTexture(window.plankCanvas);
window.plankTexture.wrapS = THREE.RepeatWrapping;
window.plankTexture.wrapT = THREE.RepeatWrapping;
window.plankTexture.repeat.set(3, 3);

window.graniteCanvas = createProceduralNoiseCanvas(256, 256, (x, y, w, h) => {
  const n1 = Math.sin(x * 0.15 + y * 0.08) * 15;
  const n2 = Math.cos(x * 0.32 - y * 0.28) * 12;
  const grain = (Math.random() - 0.5) * 35;
  const fleck = Math.random() < 0.08 ? -65 : (Math.random() < 0.06 ? 45 : 0);
  const base = 128 + n1 + n2 + grain + fleck;
  const clamped = Math.max(40, Math.min(230, base));
  const moss = (Math.sin(x * 0.05) + Math.cos(y * 0.05)) > 1.3 ? 15 : 0;
  return [clamped * 0.95 - moss * 0.5, clamped + moss, clamped * 0.98 - moss * 0.5];
});
window.graniteTexture = new THREE.CanvasTexture(window.graniteCanvas);
window.graniteTexture.wrapS = THREE.RepeatWrapping;
window.graniteTexture.wrapT = THREE.RepeatWrapping;
window.graniteTexture.repeat.set(2, 2);

window.masonryCanvas = createProceduralNoiseCanvas(256, 256, (x, y, w, h) => {
  const mortX = (x % 48) < 3, mortY = (y % 28) < 3;
  if (mortX || mortY) return [55, 55, 60];
  const bump = (Math.random() - 0.5) * 30;
  const base = 135 + bump;
  return [base * 0.95, base, base * 1.05];
});
window.masonryTexture = new THREE.CanvasTexture(window.masonryCanvas);
window.masonryTexture.wrapS = THREE.RepeatWrapping;
window.masonryTexture.wrapT = THREE.RepeatWrapping;
window.masonryTexture.repeat.set(3, 3);

window.grassCanvas = document.createElement('canvas');
window.grassCanvas.width = 128; window.grassCanvas.height = 128;
const gCtx = window.grassCanvas.getContext('2d');
gCtx.clearRect(0, 0, 128, 128);
const bladeDefs = [
  { bx: 64, by: 128, cx: 58, cy: 70, tx: 35, ty: 22, w: 9, col: '#559c3a' },
  { bx: 64, by: 128, cx: 62, cy: 60, tx: 55, ty: 10, w: 10, col: '#62b243' },
  { bx: 64, by: 128, cx: 66, cy: 55, tx: 72, ty: 8,  w: 11, col: '#72c84e' },
  { bx: 64, by: 128, cx: 70, cy: 65, tx: 92, ty: 18, w: 10, col: '#60ae41' },
  { bx: 64, by: 128, cx: 74, cy: 75, tx: 108, ty: 35, w: 8, col: '#529636' },
  { bx: 64, by: 128, cx: 52, cy: 80, tx: 20, ty: 40, w: 8, col: '#488730' },
  { bx: 64, by: 128, cx: 64, cy: 50, tx: 64, ty: 4,  w: 7, col: '#84db5d' }
];
bladeDefs.forEach(b => {
  const grad = gCtx.createLinearGradient(b.bx, b.by, b.tx, b.ty);
  grad.addColorStop(0, '#2d541e');
  grad.addColorStop(0.6, b.col);
  grad.addColorStop(1, '#a8e66e');
  gCtx.fillStyle = grad;
  gCtx.beginPath();
  gCtx.moveTo(b.bx - b.w / 2, b.by);
  gCtx.quadraticCurveTo(b.cx - b.w / 3, b.cy, b.tx, b.ty);
  gCtx.quadraticCurveTo(b.cx + b.w / 3, b.cy, b.bx + b.w / 2, b.by);
  gCtx.closePath();
  gCtx.fill();
});
window.grassTexture = new THREE.CanvasTexture(window.grassCanvas);

window.skinCanvas = document.createElement('canvas');
window.skinCanvas.width = 256; window.skinCanvas.height = 256;
const sCtx = window.skinCanvas.getContext('2d');
sCtx.fillStyle = '#f6d5be';
sCtx.fillRect(0, 0, 256, 256);
const skinGrad = sCtx.createRadialGradient(128, 140, 20, 128, 140, 100);
skinGrad.addColorStop(0, 'rgba(235, 145, 130, 0.45)');
skinGrad.addColorStop(1, 'rgba(246, 213, 190, 0)');
sCtx.fillStyle = skinGrad;
sCtx.fillRect(40, 100, 176, 80);

function drawEye(x, y) {
  sCtx.fillStyle = '#ffffff';
  sCtx.beginPath();
  sCtx.ellipse(x, y, 16, 10, 0, 0, Math.PI * 2);
  sCtx.fill();
  sCtx.fillStyle = '#4a2e18';
  sCtx.beginPath();
  sCtx.arc(x, y, 8, 0, Math.PI * 2);
  sCtx.fill();
  sCtx.fillStyle = '#111111';
  sCtx.beginPath();
  sCtx.arc(x, y, 4, 0, Math.PI * 2);
  sCtx.fill();
  sCtx.fillStyle = '#ffffff';
  sCtx.beginPath();
  sCtx.arc(x - 3, y - 3, 2.5, 0, Math.PI * 2);
  sCtx.fill();
  sCtx.strokeStyle = '#2b180d';
  sCtx.lineWidth = 2.5;
  sCtx.beginPath();
  sCtx.arc(x, y - 2, 17, 1.1 * Math.PI, 1.9 * Math.PI);
  sCtx.stroke();
  sCtx.strokeStyle = '#3e2413';
  sCtx.lineWidth = 3.5;
  sCtx.beginPath();
  sCtx.moveTo(x - 18, y - 18);
  sCtx.quadraticCurveTo(x, y - 23, x + 18, y - 17);
  sCtx.stroke();
}
drawEye(85, 115);
drawEye(171, 115);

sCtx.fillStyle = 'rgba(200, 130, 110, 0.4)';
sCtx.beginPath();
sCtx.arc(128, 148, 5, 0, Math.PI * 2);
sCtx.fill();

sCtx.strokeStyle = '#c86858';
sCtx.lineWidth = 3.5;
sCtx.beginPath();
sCtx.moveTo(108, 185);
sCtx.quadraticCurveTo(128, 196, 148, 185);
sCtx.stroke();

window.skinTexture = new THREE.CanvasTexture(window.skinCanvas);
''')

    # 5. js/leaf.js
    with open('js/leaf.js', 'w', encoding='utf-8') as f:
        f.write(r'''// High-Fidelity 3D Golden Leaf Asset Generator
function createRealisticLeafTexture() {
  const cv = document.createElement('canvas');
  cv.width = 256; cv.height = 256;
  const ctx = cv.getContext('2d');
  ctx.clearRect(0, 0, 256, 256);

  ctx.save();
  ctx.translate(128, 240);

  const grad = ctx.createRadialGradient(0, -110, 10, 0, -110, 120);
  grad.addColorStop(0, '#ffe066');
  grad.addColorStop(0.35, '#ff9e00');
  grad.addColorStop(0.75, '#e85d04');
  grad.addColorStop(1, '#9d0208');
  ctx.fillStyle = grad;

  ctx.beginPath();
  ctx.moveTo(0, 0);
  ctx.bezierCurveTo(-25, -30, -70, -45, -75, -75);
  ctx.bezierCurveTo(-85, -65, -95, -75, -85, -95);
  ctx.bezierCurveTo(-105, -110, -115, -145, -90, -165);
  ctx.bezierCurveTo(-80, -155, -65, -165, -55, -180);
  ctx.bezierCurveTo(-45, -200, -25, -235, 0, -248);
  ctx.bezierCurveTo(25, -235, 45, -200, 55, -180);
  ctx.bezierCurveTo(65, -165, 80, -155, 90, -165);
  ctx.bezierCurveTo(115, -145, 105, -110, 85, -95);
  ctx.bezierCurveTo(95, -75, 85, -65, 75, -75);
  ctx.bezierCurveTo(70, -45, 25, -30, 0, 0);
  ctx.closePath();
  ctx.fill();

  ctx.strokeStyle = '#fff3b0';
  ctx.lineWidth = 3.5;
  ctx.beginPath();
  ctx.moveTo(0, 0);
  ctx.lineTo(0, -240);
  ctx.stroke();

  ctx.lineWidth = 2.0;
  const veinPairs = [
    [-60, -140, 60, -140, -40],
    [-75, -95, 75, -95, -70],
    [-40, -175, 40, -175, -120]
  ];
  veinPairs.forEach(([lx, ly, rx, ry, startY]) => {
    ctx.beginPath();
    ctx.moveTo(0, startY); ctx.quadraticCurveTo(lx * 0.5, startY - 15, lx, ly);
    ctx.moveTo(0, startY); ctx.quadraticCurveTo(rx * 0.5, startY - 15, rx, ry);
    ctx.stroke();
  });

  ctx.restore();
  return new THREE.CanvasTexture(cv);
}

window.leafTexture = createRealisticLeafTexture();

function createRealisticLeafAsset(x, z) {
  const group = new THREE.Group();

  const bladeGeom = new THREE.PlaneGeometry(0.85, 1.1, 4, 4);
  const pos = bladeGeom.attributes.position;
  for (let i = 0; i < pos.count; i++) {
    const vx = pos.getX(i), vy = pos.getY(i);
    pos.setZ(i, Math.sin(vx * 3.5) * 0.08 - (vy * 0.04));
  }
  bladeGeom.computeVertexNormals();

  const leafMat = new THREE.MeshStandardMaterial({
    map: window.leafTexture,
    transparent: true,
    alphaTest: 0.35,
    roughness: 0.35,
    metalness: 0.1,
    emissive: 0xffaa00,
    emissiveIntensity: 0.85,
    side: THREE.DoubleSide
  });

  const leafMesh = new THREE.Mesh(bladeGeom, leafMat);
  leafMesh.rotation.x = -0.3;
  group.add(leafMesh);

  const stemGeom = new THREE.CylinderGeometry(0.015, 0.025, 0.35, 8);
  const stemMat = new THREE.MeshStandardMaterial({ color: 0x5c3214, roughness: 0.9 });
  const stem = new THREE.Mesh(stemGeom, stemMat);
  stem.position.set(0, -0.6, -0.05);
  stem.rotation.x = -0.3;
  group.add(stem);

  const light = new THREE.PointLight(0xffa200, 1.0, 7);
  group.add(light);

  const wisps = [];
  const wispGeom = new THREE.SphereGeometry(0.05, 8, 8);
  const wispMat = new THREE.MeshBasicMaterial({ color: 0xfff3b0 });
  for (let w = 0; w < 3; w++) {
    const wm = new THREE.Mesh(wispGeom, wispMat);
    group.add(wm);
    wisps.push({ mesh: wm, phase: w * (Math.PI * 2 / 3), speed: 2.2 + w * 0.4 });
  }

  group.position.set(x, ht(x, z) + 1.25, z);
  return { group, light, wisps, x, z, got: false, ph: Math.random() * 6 };
}
''')

    # 6. js/character.js
    with open('js/character.js', 'w', encoding='utf-8') as f:
        f.write(r'''// Realistic Character Model & Rigging for Amber Valley
function createRealisticCharacter() {
  const playerGroup = new THREE.Group();

  // Torso / Adventurer Coat with smooth curved geometry
  const coatGeom = new THREE.CylinderGeometry(0.28, 0.34, 0.85, 14);
  const coatMat = new THREE.MeshStandardMaterial({
    color: 0x9c4826, roughness: 0.78, flatShading: false
  });
  const coat = new THREE.Mesh(coatGeom, coatMat);
  coat.position.y = 1.15; coat.castShadow = true;
  playerGroup.add(coat);

  // Belt with bronze buckle
  const beltGeom = new THREE.CylinderGeometry(0.345, 0.345, 0.1, 14);
  const beltMat = new THREE.MeshStandardMaterial({ color: 0x2b1c11, roughness: 0.8 });
  const belt = new THREE.Mesh(beltGeom, beltMat);
  belt.position.y = 0.88; playerGroup.add(belt);

  // Head with realistic skin and painted facial features
  const headGeom = new THREE.SphereGeometry(0.24, 16, 14);
  const skinMat = new THREE.MeshStandardMaterial({
    map: window.skinTexture, roughness: 0.75, flatShading: false
  });
  const head = new THREE.Mesh(headGeom, skinMat);
  head.position.y = 1.76; head.castShadow = true;
  playerGroup.add(head);

  // Traveler Brim Hat
  const hatCrownGeom = new THREE.CylinderGeometry(0.22, 0.26, 0.28, 16);
  const hatBrimGeom = new THREE.CylinderGeometry(0.44, 0.44, 0.04, 16);
  const hatMat = new THREE.MeshStandardMaterial({ color: 0x5a3d28, roughness: 0.85 });
  const hatCrown = new THREE.Mesh(hatCrownGeom, hatMat); hatCrown.position.y = 1.95; hatCrown.castShadow = true;
  const hatBrim = new THREE.Mesh(hatBrimGeom, hatMat); hatBrim.position.y = 1.84; hatBrim.castShadow = true;
  playerGroup.add(hatCrown); playerGroup.add(hatBrim);

  // Scarf
  const scarfGeom = new THREE.TorusGeometry(0.24, 0.07, 8, 16);
  scarfGeom.rotateX(Math.PI / 2);
  const scarfMat = new THREE.MeshStandardMaterial({ color: 0xf4ece1, roughness: 0.85 });
  const scarf = new THREE.Mesh(scarfGeom, scarfMat);
  scarf.position.y = 1.54; playerGroup.add(scarf);

  // Rucksack Backpack with rolled bedroll
  const packGeom = new THREE.BoxGeometry(0.46, 0.55, 0.28);
  const packMat = new THREE.MeshStandardMaterial({ color: 0x60412b, roughness: 0.9 });
  const pack = new THREE.Mesh(packGeom, packMat);
  pack.position.set(0, 1.2, -0.32); pack.castShadow = true;
  playerGroup.add(pack);

  const bedrollGeom = new THREE.CylinderGeometry(0.12, 0.12, 0.52, 12);
  bedrollGeom.rotateZ(Math.PI / 2);
  const bedroll = new THREE.Mesh(bedrollGeom, new THREE.MeshStandardMaterial({ color: 0x3d5a80, roughness: 0.85 }));
  bedroll.position.set(0, 1.55, -0.32);
  playerGroup.add(bedroll);

  // Articulated Arms
  const armGeom = new THREE.CylinderGeometry(0.08, 0.07, 0.65, 12);
  const armL = new THREE.Mesh(armGeom, coatMat);
  armL.position.set(-0.38, 1.22, 0); armL.castShadow = true;
  playerGroup.add(armL);

  const armR = new THREE.Mesh(armGeom, coatMat);
  armR.position.set(0.38, 1.22, 0); armR.castShadow = true;
  playerGroup.add(armR);

  // Brass Hand Lantern
  const lanternGroup = new THREE.Group();
  const lanternBodyGeom = new THREE.CylinderGeometry(0.1, 0.12, 0.28, 10);
  const lanternGlassMat = new THREE.MeshStandardMaterial({
    color: 0xffb703, emissive: 0xffa200, emissiveIntensity: 1.2, roughness: 0.2
  });
  const lanternBody = new THREE.Mesh(lanternBodyGeom, lanternGlassMat);
  lanternGroup.add(lanternBody);

  const lanternLight = new THREE.PointLight(0xffa200, 1.6, 16);
  lanternGroup.add(lanternLight);

  lanternGroup.position.set(0, -0.35, 0.18);
  armR.add(lanternGroup);

  // Legs & Hiking Boots
  const legGeom = new THREE.CylinderGeometry(0.1, 0.09, 0.72, 12);
  const pantsMat = new THREE.MeshStandardMaterial({ color: 0x2b3848, roughness: 0.85 });
  const bootGeom = new THREE.BoxGeometry(0.16, 0.16, 0.28);
  const bootMat = new THREE.MeshStandardMaterial({ color: 0x2e1e12, roughness: 0.9 });

  const legL = new THREE.Mesh(legGeom, pantsMat);
  legL.position.set(-0.16, 0.42, 0); legL.castShadow = true;
  const bootL = new THREE.Mesh(bootGeom, bootMat); bootL.position.set(0, -0.32, 0.06); legL.add(bootL);
  playerGroup.add(legL);

  const legR = new THREE.Mesh(legGeom, pantsMat);
  legR.position.set(0.16, 0.42, 0); legR.castShadow = true;
  const bootR = new THREE.Mesh(bootGeom, bootMat); bootR.position.set(0, -0.32, 0.06); legR.add(bootR);
  playerGroup.add(legR);

  playerGroup.position.set(0, ht(0, 0), 0);
  scene.add(playerGroup);

  return { playerGroup, legL, legR, armL, armR, scarf, lanternGroup, lanternLight };
}
''')

    # 7. js/world.js
    with open('js/world.js', 'w', encoding='utf-8') as f:
        f.write(r'''// 3D Environment & Landmarks for Amber Valley
const CABIN = { x: 0, z: 48 }, POND = { x: -42, z: 24, rx: 17, rz: 17 };
const MONOLITH = { x: 36, z: -48 }, SHRINE = { x: -54, z: 10 }, FAIRYRING = { x: -24, z: -56 };
const WATER = -0.9, LAKE = { x: -42, z: 24 }, DES = { x: 68, z: -5 }, FOR = { x: -10, z: -60 };
const sm = (a, b, x) => { const t = Math.max(0, Math.min(1, (x - a) / (b - a))); return t * t * (3 - 2 * t); };
function wts(x, z) {
  return [
    sm(26, 9, Math.hypot(x - LAKE.x, z - LAKE.z)),
    sm(44, 24, Math.hypot(x - DES.x, (z - DES.z) * 0.8)),
    sm(40, 22, Math.hypot(x - FOR.x, z - FOR.z))
  ];
}
function ht(x, z) {
  let h = 2.6 * Math.sin(x * 0.042 + 1) * Math.cos(z * 0.037) + 1.2 * Math.sin(x * 0.1 + z * 0.085) + 0.5 * Math.sin(x * 0.22 - z * 0.17) + 1.6;
  const w = wts(x, z);
  h += w[1] * (2.4 * Math.sin(x * 0.13 + z * 0.04) * Math.sin(z * 0.09) + 1.5) + w[2] * Math.sin(x * 0.07) * Math.cos(z * 0.08) * 1.6;
  const fl = Math.max(sm(14, 5, Math.hypot(x, z)), sm(14, 6, Math.hypot(x - CABIN.x, z - CABIN.z)));
  h *= (1 - fl);
  return h * (1 - w[0]) - 4.0 * w[0];
}
const inPond = (x, z, m = 1) => ht(x, z) < WATER + (m > 1 ? 0.5 : 0);

let seed = 17;
const R = () => (seed = (seed * 16807) % 2147483647) / 2147483647;

const SEASON_NAMES = { spring: '🌸 Spring Valley', summer: '☀️ Summer Valley', autumn: '🍂 Autumn Valley', winter: '❄️ Winter Valley' };
const SEASONS = ['spring', 'summer', 'autumn', 'winter'];
let currentSeason = 'autumn', autoSeason = false, seasonTimer = 60.0;
let timeOfDay = 0.5, autoTime = false;
let weather = 'clear', autoWeather = false, weatherTimer = 30;
let lightningTimer = 4.0, lightningFlash = 0;

const SEASON_PALETTES = {
  spring: {
    meadow: [0.42, 0.74, 0.32], forest: [0.24, 0.52, 0.26], desert: [0.82, 0.76, 0.56], shore: [0.88, 0.82, 0.62],
    oak: [0xffb7c5, 0xffa4b6, 0xf78da7], pine: [0x2f6b3e, 0x3d7e4d],
    grass: 0x58a846, fog: 0xe2f0d9, skyTop: 0x6ca0dc, skyBot: 0xd5e8d4
  },
  summer: {
    meadow: [0.32, 0.64, 0.25], forest: [0.18, 0.45, 0.22], desert: [0.88, 0.76, 0.5], shore: [0.9, 0.82, 0.58],
    oak: [0x3c8b2f, 0x4aa03b, 0x2e7523], pine: [0x22552d, 0x2d6837],
    grass: 0x429633, fog: 0xcde2f2, skyTop: 0x4a90e2, skyBot: 0xcbe3fb
  },
  autumn: {
    meadow: [0.82, 0.56, 0.24], forest: [0.48, 0.34, 0.18], desert: [0.88, 0.74, 0.5], shore: [0.85, 0.75, 0.52],
    oak: [0xe26a20, 0xee8b24, 0xca4818], pine: [0x3a563c, 0x466649],
    grass: 0xb57028, fog: 0xebd1a8, skyTop: 0x667fa8, skyBot: 0xefcfad
  },
  winter: {
    meadow: [0.93, 0.95, 0.98], forest: [0.74, 0.8, 0.87], desert: [0.85, 0.87, 0.92], shore: [0.82, 0.88, 0.94],
    oak: [0xecf0f5, 0xdfe6ee, 0xd0dae6], pine: [0x4e6e66, 0x5c8077],
    grass: 0xd2dbe4, fog: 0xdfe7f0, skyTop: 0x4d658d, skyBot: 0xdce4ec
  }
};

// High-Density Smooth Terrain Mesh (180x180)
const T_SIZE = 260, T_SEGS = 180;
const terrainGeom = new THREE.PlaneGeometry(T_SIZE, T_SIZE, T_SEGS, T_SEGS);
terrainGeom.rotateX(-Math.PI / 2);
const posAttr = terrainGeom.attributes.position;
const colorAttr = new THREE.BufferAttribute(new Float32Array(posAttr.count * 3), 3);
terrainGeom.setAttribute('color', colorAttr);

for (let i = 0; i < posAttr.count; i++) {
  const vx = posAttr.getX(i), vz = posAttr.getZ(i);
  posAttr.setY(i, ht(vx, vz));
}
terrainGeom.computeVertexNormals();

function updateTerrainColors(seasonKey) {
  const pal = SEASON_PALETTES[seasonKey];
  for (let i = 0; i < posAttr.count; i++) {
    const vx = posAttr.getX(i), vy = posAttr.getY(i), vz = posAttr.getZ(i);
    const w = wts(vx, vz);
    let r = pal.meadow[0], g = pal.meadow[1], b = pal.meadow[2];
    r += (pal.forest[0] - r) * w[2];
    g += (pal.forest[1] - g) * w[2];
    b += (pal.forest[2] - b) * w[2];
    r += (pal.desert[0] - r) * w[1];
    g += (pal.desert[1] - g) * w[1];
    b += (pal.desert[2] - b) * w[1];
    if (vy < WATER + 0.7) {
      r = r * 0.35 + pal.shore[0] * 0.65;
      g = g * 0.35 + pal.shore[1] * 0.65;
      b = b * 0.35 + pal.shore[2] * 0.65;
    }
    colorAttr.setXYZ(i, r, g, b);
  }
  colorAttr.needsUpdate = true;
}
updateTerrainColors(currentSeason);

const terrainMat = new THREE.MeshStandardMaterial({
  vertexColors: true,
  map: window.terrainTexture,
  roughness: 0.86,
  metalness: 0.05,
  flatShading: false
});
const terrainMesh = new THREE.Mesh(terrainGeom, terrainMat);
terrainMesh.receiveShadow = true;
scene.add(terrainMesh);

// Smooth Water Surface
const waterGeom = new THREE.CircleGeometry(25, 48);
waterGeom.rotateX(-Math.PI / 2);
const waterMat = new THREE.MeshStandardMaterial({
  color: 0x2b80be, roughness: 0.08, metalness: 0.15, transparent: true, opacity: 0.78
});
const waterMesh = new THREE.Mesh(waterGeom, waterMat);
waterMesh.position.set(POND.x, WATER + 0.05, POND.z);
scene.add(waterMesh);

const shoreRingGeom = new THREE.RingGeometry(23.5, 25.4, 48);
shoreRingGeom.rotateX(-Math.PI / 2);
const shoreRing = new THREE.Mesh(shoreRingGeom, new THREE.MeshBasicMaterial({ color: 0xffffff, transparent: true, opacity: 0.28 }));
shoreRing.position.set(POND.x, WATER + 0.07, POND.z);
scene.add(shoreRing);

// Tree Materials
const oakMaterials = {}, pineMaterials = {};
for (const s of SEASONS) {
  const pal = SEASON_PALETTES[s];
  oakMaterials[s] = pal.oak.map(c => new THREE.MeshStandardMaterial({ color: c, roughness: 0.75, flatShading: false }));
  pineMaterials[s] = pal.pine.map(c => new THREE.MeshStandardMaterial({ color: c, roughness: 0.85, flatShading: false }));
}
const woodMat = new THREE.MeshStandardMaterial({ color: 0x583822, map: window.barkTexture, roughness: 0.88, flatShading: false });
const snowCapMat = new THREE.MeshStandardMaterial({ color: 0xf2f6fa, roughness: 0.7, flatShading: false });

const pineMeshes = [], oakCanopies = [];

function createRealisticPine(x, z, scale = 1) {
  const group = new THREE.Group();
  const trunkGeom = new THREE.CylinderGeometry(0.18 * scale, 0.42 * scale, 3.4 * scale, 16);
  const trunk = new THREE.Mesh(trunkGeom, woodMat);
  trunk.position.y = 1.7 * scale;
  trunk.castShadow = true; trunk.receiveShadow = true;
  group.add(trunk);

  const tiers = [];
  for (let i = 0; i < 5; i++) {
    const tierProgress = i / 4;
    const r = (1.8 - tierProgress * 0.9) * scale;
    const h = (1.6 - tierProgress * 0.4) * scale;
    const coneGeom = new THREE.ConeGeometry(r, h, 18);
    const matList = pineMaterials[currentSeason];
    const cone = new THREE.Mesh(coneGeom, matList[i % matList.length]);
    cone.position.y = (1.8 + i * 0.85) * scale;
    cone.castShadow = true; cone.receiveShadow = true;
    group.add(cone);
    tiers.push(cone);

    const snowGeom = new THREE.ConeGeometry(r * 0.72, h * 0.5, 18);
    const snowCap = new THREE.Mesh(snowGeom, snowCapMat);
    snowCap.position.y = (1.8 + i * 0.85 + h * 0.28) * scale;
    snowCap.visible = (currentSeason === 'winter');
    group.add(snowCap);
    cone.snowCap = snowCap;
  }
  group.position.set(x, ht(x, z), z);
  scene.add(group);
  pineMeshes.push(tiers);

  // Register solid collision circle
  window.collisionSystem.addCircle(x, z, 0.55 * scale, 'pine');
  return group;
}

function createRealisticOak(x, z, scale = 1) {
  const group = new THREE.Group();
  const trunkGeom = new THREE.CylinderGeometry(0.35 * scale, 0.65 * scale, 3.4 * scale, 16);
  const trunk = new THREE.Mesh(trunkGeom, woodMat);
  trunk.position.y = 1.7 * scale;
  trunk.castShadow = true; trunk.receiveShadow = true;
  group.add(trunk);

  for (let b = 0; b < 3; b++) {
    const branchGeom = new THREE.CylinderGeometry(0.18 * scale, 0.25 * scale, 1.8 * scale, 12);
    const branch = new THREE.Mesh(branchGeom, woodMat);
    const bAngle = b * (Math.PI * 2 / 3);
    branch.position.set(Math.cos(bAngle) * 0.5 * scale, 2.7 * scale, Math.sin(bAngle) * 0.5 * scale);
    branch.rotation.z = Math.cos(bAngle) * 0.45;
    branch.rotation.x = -Math.sin(bAngle) * 0.45;
    branch.castShadow = true;
    group.add(branch);
  }

  const canopyGroup = new THREE.Group();
  const matList = oakMaterials[currentSeason];
  for (let i = 0; i < 14; i++) {
    const an = i * 0.65 + R() * 0.3;
    const dist = (0.6 + R() * 1.0) * scale;
    const r = (1.1 + R() * 0.55) * scale;
    const sphereGeom = new THREE.SphereGeometry(r, 16, 14);
    const foliage = new THREE.Mesh(sphereGeom, matList[i % matList.length]);
    foliage.position.set(Math.cos(an) * dist, (3.6 + Math.sin(an * 2) * 0.5 + R() * 0.8) * scale, Math.sin(an) * dist);
    foliage.castShadow = true; foliage.receiveShadow = true;
    canopyGroup.add(foliage);
    oakCanopies.push(foliage);
  }
  group.add(canopyGroup);
  group.position.set(x, ht(x, z), z);
  scene.add(group);

  // Register solid collision circle
  window.collisionSystem.addCircle(x, z, 0.68 * scale, 'oak');
  return group;
}

function spot(minR, maxR) {
  for (;;) {
    const r = minR + R() * (maxR - minR), a = R() * 6.283, x = Math.cos(a) * r, z = Math.sin(a) * r;
    if (Math.hypot(x - CABIN.x, z - CABIN.z) < 10 || inPond(x, z, 1.3) || Math.hypot(x, z) < 14) continue;
    if (Math.abs(x) < 5 && z > -2 && z < 46) continue;
    return [x, z];
  }
}

for (let i = 0; i < 45; i++) { const [x, z] = spot(14, 95); createRealisticOak(x, z, 0.85 + R() * 0.4); }
for (let i = 0; i < 115; i++) { const [x, z] = spot(14, 98); createRealisticPine(x, z, 0.85 + R() * 0.55); }

// Natural Granite Boulders
const rockGeom = new THREE.IcosahedronGeometry(1.0, 2);
const rockMat = new THREE.MeshStandardMaterial({
  color: 0x908c86, map: window.graniteTexture, roughness: 0.9, metalness: 0.05, flatShading: false
});
for (let i = 0; i < 35; i++) {
  const [x, z] = spot(14, 96);
  const rMesh = new THREE.Mesh(rockGeom, rockMat);
  const s = 0.7 + R() * 1.1;
  rMesh.scale.set(s, s * 0.65, s * 1.1);
  rMesh.rotation.set(R() * 3, R() * 3, R() * 3);
  rMesh.position.set(x, ht(x, z) + s * 0.25, z);
  rMesh.castShadow = true; rMesh.receiveShadow = true;
  scene.add(rMesh);

  // Register solid collision circle
  window.collisionSystem.addCircle(x, z, 0.85 * s, 'boulder');
}

// Crossed 3D Grass Tufts
const crossTuftGeom = new THREE.BufferGeometry();
const pW = 0.7, pH = 0.75;
const tuftVerts = new Float32Array([
  -pW/2, 0, 0,    pW/2, 0, 0,    -pW/2, pH, 0,    pW/2, pH, 0,
  0, 0, -pW/2,    0, 0, pW/2,    0, pH, -pW/2,    0, pH, pW/2
]);
const tuftUVs = new Float32Array([
  0, 0,   1, 0,   0, 1,   1, 1,
  0, 0,   1, 0,   0, 1,   1, 1
]);
const tuftIndices = [
  0, 1, 2,  2, 1, 3,
  4, 5, 6,  6, 5, 7
];
crossTuftGeom.setAttribute('position', new THREE.BufferAttribute(tuftVerts, 3));
crossTuftGeom.setAttribute('uv', new THREE.BufferAttribute(tuftUVs, 2));
crossTuftGeom.setIndex(tuftIndices);
crossTuftGeom.computeVertexNormals();

const GRASS_COUNT = 1400;
const grassMat = new THREE.MeshStandardMaterial({
  map: window.grassTexture, transparent: true, alphaTest: 0.35, roughness: 0.85, side: THREE.DoubleSide
});
const grassInstanced = new THREE.InstancedMesh(crossTuftGeom, grassMat, GRASS_COUNT);
grassInstanced.receiveShadow = true;

const dummy = new THREE.Object3D();
for (let i = 0; i < GRASS_COUNT; i++) {
  const [x, z] = spot(6, 92);
  const y = ht(x, z);
  const s = 0.7 + R() * 0.7;
  dummy.position.set(x, y, z);
  dummy.rotation.set(0, R() * Math.PI * 2, 0);
  dummy.scale.set(s, s, s);
  dummy.updateMatrix();
  grassInstanced.setMatrixAt(i, dummy.matrix);
}
grassInstanced.instanceMatrix.needsUpdate = true;
scene.add(grassInstanced);

// Woodland Cabin
const cabinGroup = new THREE.Group();
const foundGeom = new THREE.BoxGeometry(7.2, 0.6, 6.0);
const cabinFound = new THREE.Mesh(foundGeom, new THREE.MeshStandardMaterial({ color: 0x6e6863, map: window.masonryTexture, roughness: 0.9 }));
cabinFound.position.y = 0.3; cabinFound.castShadow = true; cabinGroup.add(cabinFound);

const wallMat = new THREE.MeshStandardMaterial({ color: 0x8a5530, map: window.plankTexture, roughness: 0.78 });
const cabinWalls = new THREE.Mesh(new THREE.BoxGeometry(6.6, 3.4, 5.4), wallMat);
cabinWalls.position.y = 2.0; cabinWalls.castShadow = true; cabinGroup.add(cabinWalls);

const roof = new THREE.Mesh(new THREE.ConeGeometry(5.0, 2.4, 4), new THREE.MeshStandardMaterial({ color: 0x6b301c, map: window.plankTexture, roughness: 0.8 }));
roof.geometry.rotateY(Math.PI / 4);
roof.position.y = 4.6; roof.scale.set(1.15, 1.0, 1.45); roof.castShadow = true; cabinGroup.add(roof);

const chimney = new THREE.Mesh(new THREE.BoxGeometry(1.0, 3.0, 1.0), new THREE.MeshStandardMaterial({ color: 0x645e5a, map: window.masonryTexture, roughness: 0.92 }));
chimney.position.set(2.0, 4.6, 1.2); chimney.castShadow = true; cabinGroup.add(chimney);

const smokePuffs = [];
const smokeGeom = new THREE.SphereGeometry(0.24, 8, 8);
const smokeMat = new THREE.MeshBasicMaterial({ color: 0xd8d0c8, transparent: true, opacity: 0.45 });
for (let i = 0; i < 6; i++) {
  const smk = new THREE.Mesh(smokeGeom, smokeMat);
  smk.position.set(2.0, 6.2 + i * 0.45, 1.2);
  cabinGroup.add(smk);
  smokePuffs.push(smk);
}

const windowMat = new THREE.MeshStandardMaterial({ color: 0xffd166, emissive: 0xffa000, emissiveIntensity: 0.9, roughness: 0.15 });
const cabinWindow = new THREE.Mesh(new THREE.PlaneGeometry(1.3, 1.1), windowMat);
cabinWindow.position.set(-1.6, 2.2, 2.72); cabinGroup.add(cabinWindow);

const cabinLight = new THREE.PointLight(0xff9f1c, 1.6, 18);
cabinLight.position.set(-1.6, 2.4, 3.6); cabinGroup.add(cabinLight);

const porch = new THREE.Mesh(new THREE.BoxGeometry(2.8, 0.25, 1.6), wallMat);
porch.position.set(1.4, 0.5, 3.4); cabinGroup.add(porch);

const cabinDoor = new THREE.Mesh(new THREE.BoxGeometry(1.2, 2.2, 0.1), new THREE.MeshStandardMaterial({ color: 0x4d2a15, map: window.plankTexture, roughness: 0.85 }));
cabinDoor.position.set(1.4, 1.6, 2.73); cabinGroup.add(cabinDoor);

cabinGroup.position.set(CABIN.x, ht(CABIN.x, CABIN.z), CABIN.z);
scene.add(cabinGroup);

// Register solid cabin box collider so player cannot pass through walls!
window.collisionSystem.addBox(CABIN.x - 3.5, CABIN.x + 3.5, CABIN.z - 2.8, CABIN.z + 2.8, 'cabin_walls');

// Whispering Monolith Landmark
const monolithGroup = new THREE.Group();
const monoMesh = new THREE.Mesh(new THREE.CylinderGeometry(0.65, 0.95, 7.2, 8), new THREE.MeshStandardMaterial({ color: 0x3d485a, map: window.graniteTexture, roughness: 0.65 }));
monoMesh.position.y = 3.6; monoMesh.castShadow = true; monolithGroup.add(monoMesh);

const crystal = new THREE.Mesh(new THREE.OctahedronGeometry(0.75, 1), new THREE.MeshStandardMaterial({ color: 0x64dfdf, emissive: 0x00f5d4, emissiveIntensity: 1.1, roughness: 0.15 }));
crystal.position.y = 8.0; monolithGroup.add(crystal);
const monoLight = new THREE.PointLight(0x00f5d4, 1.5, 16);
monoLight.position.y = 8.0; monolithGroup.add(monoLight);
monolithGroup.position.set(MONOLITH.x, ht(MONOLITH.x, MONOLITH.z), MONOLITH.z);
scene.add(monolithGroup);
window.collisionSystem.addCircle(MONOLITH.x, MONOLITH.z, 1.0, 'monolith');

// Moon Goddess Shrine Landmark
const shrineGroup = new THREE.Group();
const shrineBase = new THREE.Mesh(new THREE.CylinderGeometry(2.6, 2.9, 0.7, 16), new THREE.MeshStandardMaterial({ color: 0x6e7888, map: window.masonryTexture, roughness: 0.8 }));
shrineBase.position.y = 0.35; shrineBase.castShadow = true; shrineGroup.add(shrineBase);

const shrinePoolGeom = new THREE.CircleGeometry(2.2, 32);
shrinePoolGeom.rotateX(-Math.PI / 2);
const shrinePool = new THREE.Mesh(shrinePoolGeom, new THREE.MeshStandardMaterial({ color: 0x48cae4, emissive: 0x0096c7, emissiveIntensity: 0.75, roughness: 0.08 }));
shrinePool.position.y = 0.72; shrineGroup.add(shrinePool);
const shrineLight = new THREE.PointLight(0x48cae4, 1.3, 14);
shrineLight.position.y = 1.4; shrineGroup.add(shrineLight);
shrineGroup.position.set(SHRINE.x, ht(SHRINE.x, SHRINE.z), SHRINE.z);
scene.add(shrineGroup);
window.collisionSystem.addCircle(SHRINE.x, SHRINE.z, 2.7, 'shrine');

// Fairy Mushroom Ring Landmark
const fairyGroup = new THREE.Group();
for (let i = 0; i < 8; i++) {
  const an = i * (Math.PI / 4), r = 2.4;
  const stem = new THREE.Mesh(new THREE.CylinderGeometry(0.09, 0.14, 0.7, 12), new THREE.MeshStandardMaterial({ color: 0xfaedcd, roughness: 0.8 }));
  const cap = new THREE.Mesh(new THREE.SphereGeometry(0.38, 12, 10, 0, Math.PI * 2, 0, Math.PI * 0.5), new THREE.MeshStandardMaterial({ color: 0xda2245, emissive: 0x7209b7, emissiveIntensity: 0.65, roughness: 0.3, side: THREE.DoubleSide }));
  stem.position.set(Math.cos(an) * r, 0.35, Math.sin(an) * r);
  cap.position.set(Math.cos(an) * r, 0.7, Math.sin(an) * r);
  stem.castShadow = true; fairyGroup.add(stem); fairyGroup.add(cap);
}
fairyGroup.position.set(FAIRYRING.x, ht(FAIRYRING.x, FAIRYRING.z), FAIRYRING.z);
scene.add(fairyGroup);

// Generate 12 Realistic Collectible Leaves
const leaves = [];
for (let i = 0; i < 12; i++) {
  const [x, z] = spot(14, 88);
  const leafAsset = createRealisticLeafAsset(x, z);
  scene.add(leafAsset.group);
  leaves.push(leafAsset);
}
''')

    # 8. js/critters.js
    with open('js/critters.js', 'w', encoding='utf-8') as f:
        f.write(r'''// Roaming Critters & Mystic Spirits for Amber Valley
const animalList = [];
const critterKinds = [['bunny', 0xf8edeb, 8], ['fox', 0xe07a5f, 5], ['hedgehog', 0x7f5539, 4]];
let caughtN = 0;

for (const [kind, colHex, cnt] of critterKinds) {
  for (let i = 0; i < cnt; i++) {
    const [x, z] = spot(14, 90);
    const mesh = new THREE.Group();
    const bodyGeom = new THREE.SphereGeometry(0.32, 12, 10);
    const cMat = new THREE.MeshStandardMaterial({ color: colHex, roughness: 0.78, flatShading: false });
    const body = new THREE.Mesh(bodyGeom, cMat);
    body.scale.set(1, 0.82, 1.4); body.position.y = 0.28; body.castShadow = true; mesh.add(body);
    
    if (kind === 'bunny') {
      const earGeom = new THREE.CylinderGeometry(0.04, 0.07, 0.35, 8);
      const earL = new THREE.Mesh(earGeom, cMat); earL.position.set(-0.12, 0.6, 0.1); earL.rotation.z = -0.2; mesh.add(earL);
      const earR = new THREE.Mesh(earGeom, cMat); earR.position.set(0.12, 0.6, 0.1); earR.rotation.z = 0.2; mesh.add(earR);
    }
    
    mesh.position.set(x, ht(x, z), z);
    scene.add(mesh);
    animalList.push({ kind, mesh, x, z, vx: 0, vz: 0, ang: R() * 6.28, tm: 0, go: false, gone: 0, hp: R() * 6, mystic: false });
  }
}

const mysticKinds = [['glimmerpuff', 0x00f5d4], ['moonbun', 0xc77dff], ['sunwisp', 0xffd166]];
for (const [kind, colHex] of mysticKinds) {
  const [x, z] = spot(16, 90);
  const mesh = new THREE.Group();
  const mGeom = new THREE.SphereGeometry(0.36, 16, 14);
  const mMat = new THREE.MeshStandardMaterial({
    color: colHex, emissive: colHex, emissiveIntensity: 1.0, roughness: 0.15
  });
  const mSphere = new THREE.Mesh(mGeom, mMat);
  mSphere.position.y = 1.1; mesh.add(mSphere);
  
  const haloGeom = new THREE.TorusGeometry(0.5, 0.03, 8, 24);
  haloGeom.rotateX(Math.PI / 2);
  const halo = new THREE.Mesh(haloGeom, mMat);
  halo.position.y = 1.1; mesh.add(halo);

  const mLight = new THREE.PointLight(colHex, 1.2, 9);
  mLight.position.y = 1.1; mesh.add(mLight);
  mesh.position.set(x, ht(x, z), z);
  scene.add(mesh);
  animalList.push({ kind, mesh, x, z, vx: 0, vz: 0, ang: R() * 6.28, tm: 0, go: false, gone: 0, hp: R() * 6, mystic: true });
}
''')

    # 9. js/game.js
    with open('js/game.js', 'w', encoding='utf-8') as f:
        f.write(r'''// Main Game Loop & Input System with Correct Non-Inverted Controls
const P_COUNT = 160;
const particleGeom = new THREE.BufferGeometry();
const particlePos = new Float32Array(P_COUNT * 3);
for (let i = 0; i < P_COUNT; i++) {
  particlePos[i * 3] = (R() - 0.5) * 90;
  particlePos[i * 3 + 1] = 2 + R() * 25;
  particlePos[i * 3 + 2] = (R() - 0.5) * 90;
}
particleGeom.setAttribute('position', new THREE.BufferAttribute(particlePos, 3));
const particleMat = new THREE.PointsMaterial({
  size: 0.5, color: 0xee8b24, transparent: true, opacity: 0.85
});
const particleSystem = new THREE.Points(particleGeom, particleMat);
scene.add(particleSystem);

function updateParticleColors(seasonKey) {
  if (seasonKey === 'spring') particleMat.color.setHex(0xffb7c5);
  else if (seasonKey === 'summer') particleMat.color.setHex(0xffea00);
  else if (seasonKey === 'winter') particleMat.color.setHex(0xf8f9fa);
  else particleMat.color.setHex(0xee8b24);
}

const spiritWisps = [];
const wispGeom = new THREE.SphereGeometry(0.22, 12, 10);
const wispMat = new THREE.MeshStandardMaterial({
  color: 0x00f5d4, emissive: 0x00f5d4, emissiveIntensity: 1.6
});

let started = false, won = false, got = 0, T = 0, toastT = 0;
let playerAngle = 0;
let ca = 0;
let camPitch = 0.38;
let targetCa = 0, targetCamPitch = 0.38;
let camDist = 7.5, targetCamDist = 7.5;
let jh = 0, pjv = 0, jumpLatch = 0, moving = 0, walk = 0;
const pw = { speed: 0, jump: 0, starlight: 0, lakeStrider: 0 };
let inCabin = false, hearthLeaves = 0;

const charData = createRealisticCharacter();
const playerGroup = charData.playerGroup;
const legL = charData.legL, legR = charData.legR;
const armL = charData.armL, armR = charData.armR;
const scarf = charData.scarf, lanternGroup = charData.lanternGroup, lanternLight = charData.lanternLight;

const keys = {};
addEventListener('keydown', e => {
  keys[e.code] = true;
  if (e.code === 'KeyE') {
    if (activePromptAction) activateInteraction();
  }
  if (e.code === 'KeyM' || (e.code === 'Escape' && !settingsModal.hidden)) {
    toggleMenu();
  }
});
addEventListener('keyup', e => {
  keys[e.code] = false;
});

// Fixed 360 Camera Drag Orbit & Pitch
let isDragging = false, lastPointerX = 0, lastPointerY = 0;
renderer.domElement.addEventListener('pointerdown', e => {
  if (e.target === renderer.domElement) {
    isDragging = true;
    lastPointerX = e.clientX;
    lastPointerY = e.clientY;
    try { renderer.domElement.setPointerCapture(e.pointerId); } catch(err) {}
  }
});
renderer.domElement.addEventListener('pointermove', e => {
  if (isDragging) {
    const dx = e.clientX - lastPointerX;
    const dy = e.clientY - lastPointerY;
    targetCa += dx * 0.0055;
    targetCamPitch = Math.max(0.12, Math.min(1.32, targetCamPitch - dy * 0.004));
    lastPointerX = e.clientX;
    lastPointerY = e.clientY;
  }
});
const stopDrag = e => {
  if (isDragging) {
    isDragging = false;
    try { renderer.domElement.releasePointerCapture(e.pointerId); } catch(err) {}
  }
};
renderer.domElement.addEventListener('pointerup', stopDrag);
renderer.domElement.addEventListener('pointercancel', stopDrag);

addEventListener('wheel', e => {
  const delta = Math.sign(e.deltaY) * 0.8;
  targetCamDist = Math.max(4.0, Math.min(14.0, targetCamDist + delta));
}, { passive: true });

// Virtual Touch Joystick
let joystickActive = false;
let joystickX = 0, joystickY = 0;
const touchControls = document.getElementById('touch-controls');
const touchStick = document.getElementById('touch-stick');
const mobileButtons = document.getElementById('mobile-buttons');

if ('ontouchstart' in window || navigator.maxTouchPoints > 0) {
  touchControls.style.display = 'block';
  mobileButtons.style.display = 'flex';
}

function handleTouchMove(clientX, clientY) {
  const rect = touchControls.getBoundingClientRect();
  const centerX = rect.left + rect.width / 2;
  const centerY = rect.top + rect.height / 2;
  let dx = clientX - centerX;
  let dy = clientY - centerY;
  const maxR = rect.width / 2 - 10;
  const dist = Math.hypot(dx, dy);
  if (dist > maxR) {
    dx = (dx / dist) * maxR;
    dy = (dy / dist) * maxR;
  }
  touchStick.style.transform = `translate(${dx}px, ${dy}px)`;
  joystickX = dx / maxR;
  joystickY = -dy / maxR;
}

touchControls.addEventListener('pointerdown', e => {
  joystickActive = true;
  try { touchControls.setPointerCapture(e.pointerId); } catch(err) {}
  handleTouchMove(e.clientX, e.clientY);
});
touchControls.addEventListener('pointermove', e => {
  if (joystickActive) handleTouchMove(e.clientX, e.clientY);
});
const endTouch = e => {
  joystickActive = false;
  joystickX = 0; joystickY = 0;
  touchStick.style.transform = 'translate(0, 0)';
  try { touchControls.releasePointerCapture(e.pointerId); } catch(err) {}
};
touchControls.addEventListener('pointerup', endTouch);
touchControls.addEventListener('pointercancel', endTouch);

const mobileJumpBtn = document.getElementById('mobile-jump');
const mobileSprintBtn = document.getElementById('mobile-sprint');
let mobileSprintActive = false;

mobileJumpBtn.addEventListener('pointerdown', () => { keys.Space = true; });
mobileJumpBtn.addEventListener('pointerup', () => { keys.Space = false; });
mobileJumpBtn.addEventListener('pointercancel', () => { keys.Space = false; });

mobileSprintBtn.addEventListener('pointerdown', () => {
  mobileSprintActive = !mobileSprintActive;
  mobileSprintBtn.classList.toggle('pressed', mobileSprintActive);
});

const toast = t => {
  const el = document.getElementById('toast');
  el.textContent = t;
  el.style.opacity = 1;
  toastT = 2.4;
};

function setSeason(s, silent = false) {
  if (!SEASONS.includes(s)) return;
  currentSeason = s;
  updateTerrainColors(s);
  updateParticleColors(s);
  
  for (const tiers of pineMeshes) {
    const list = pineMaterials[s];
    tiers.forEach((cone, idx) => {
      cone.material = list[idx % list.length];
      if (cone.snowCap) cone.snowCap.visible = (s === 'winter');
    });
  }
  const oakList = oakMaterials[s];
  oakCanopies.forEach((f, idx) => { f.material = oakList[idx % oakList.length]; });
  
  document.querySelectorAll('#season-btns button').forEach(b => {
    b.classList.toggle('active', b.dataset.s === s);
  });
  document.getElementById('season-hud').textContent = SEASON_NAMES[s];
  if (!silent) toast('Season shifting to ' + SEASON_NAMES[s]);
}

function updateTOD(tm) {
  timeOfDay = tm;
  const sunFactor = Math.max(0, Math.sin(tm * Math.PI));
  ambientLight.intensity = 0.16 + sunFactor * 0.68;
  sunLight.position.set(Math.cos(tm * Math.PI * 2) * 60, Math.max(12, Math.sin(tm * Math.PI * 2) * 85), 35);
  sunLight.intensity = sunFactor * 1.25;
  
  if (tm <= 0.2 || tm >= 0.8) {
    scene.background = new THREE.Color(0x060914);
    scene.fog.color.setHex(0x0a1020);
    ambientLight.color.setHex(0x1a263d);
    lanternLight.intensity = 2.4;
  } else {
    const pal = SEASON_PALETTES[currentSeason];
    scene.background = new THREE.Color(pal.skyBot);
    scene.fog.color.setHex(pal.fog);
    ambientLight.color.setHex(0xffffff);
    lanternLight.intensity = 0.7;
  }
}
updateTOD(timeOfDay);

function setTOD(t) {
  updateTOD(t);
  document.querySelectorAll('#tod-btns button').forEach(b => {
    b.classList.toggle('active', Math.abs(parseFloat(b.dataset.t) - t) < 0.05);
  });
}

function setWeather(w) {
  weather = w;
  document.querySelectorAll('#weather-btns button').forEach(b => {
    b.classList.toggle('active', b.dataset.w === w);
  });
  if (w === 'fog') scene.fog.density = 0.032;
  else scene.fog.density = 0.0085;
  if (w === 'storm') toast('Thunderstorm rolling in');
  else if (w === 'rain') toast(currentSeason === 'winter' ? 'Snow flurry falling' : 'Gentle rain falling');
  else if (w === 'fog') toast('Misty mountain fog descending');
  else toast('Skies clearing up');
}

let activePromptAction = null;
function updateInteractionPrompts() {
  const promptBtn = document.getElementById('interact-prompt');
  if (!promptBtn) return;
  if (!started || inCabin) { promptBtn.hidden = true; return; }
  
  const dCabin = Math.hypot(playerGroup.position.x - CABIN.x, playerGroup.position.z - CABIN.z);
  const dMono = Math.hypot(playerGroup.position.x - MONOLITH.x, playerGroup.position.z - MONOLITH.z);
  const dShrine = Math.hypot(playerGroup.position.x - SHRINE.x, playerGroup.position.z - SHRINE.z);
  const dRing = Math.hypot(playerGroup.position.x - FAIRYRING.x, playerGroup.position.z - FAIRYRING.z);

  if (dRing < 2.8) {
    if (jh <= 0.2) {
      jh = 1.2; pjv = 20;
      window.audio.playSpring();
      toast('✨ Fairy Mushroom Spring! Soaring high into the sky!');
    }
    promptBtn.hidden = true;
    activePromptAction = null;
    return;
  }

  if (dCabin < 8.5) {
    promptBtn.textContent = '🏡 Enter Cabin (Press E)';
    promptBtn.hidden = false;
    activePromptAction = 'cabin';
  } else if (dMono < 6.8) {
    promptBtn.textContent = '✨ Listen to Whispering Monolith (Press E)';
    promptBtn.hidden = false;
    activePromptAction = 'monolith';
  } else if (dShrine < 6.8) {
    promptBtn.textContent = '🌙 Pray at Moon Shrine (Press E)';
    promptBtn.hidden = false;
    activePromptAction = 'shrine';
  } else {
    promptBtn.hidden = true;
    activePromptAction = null;
  }
}

function activateInteraction() {
  if (activePromptAction === 'cabin') openCabin();
  else if (activePromptAction === 'monolith') activateMonolith();
  else if (activePromptAction === 'shrine') activateShrine();
}
document.getElementById('interact-prompt').onclick = activateInteraction;

function activateMonolith() {
  window.audio.playEthereal(520);
  let nearest = null, minD = 999999;
  for (const l of leaves) {
    if (!l.got) {
      const d = Math.hypot(l.x - playerGroup.position.x, l.z - playerGroup.position.z);
      if (d < minD) { minD = d; nearest = l; }
    }
  }
  if (nearest) {
    pw.starlight = 32;
    for (let i = 0; i < 8; i++) {
      const wMesh = new THREE.Mesh(wispGeom, wispMat);
      wMesh.position.copy(monolithGroup.position);
      wMesh.position.y += 6.5;
      scene.add(wMesh);
      spiritWisps.push({ mesh: wMesh, tx: nearest.x, tz: nearest.z, life: 1.3, ph: i * 0.4 });
    }
    toast(`✨ The Monolith resonates: 'A spirit wisp guides you (~${Math.round(minD)} paces away)!'`);
  } else {
    toast('✨ The Monolith resonates: All 12 leaves are gathered!');
  }
}

function activateShrine() {
  window.audio.playEthereal(440);
  pw.lakeStrider = 55;
  toast('🌙 Blessed by the Moon Goddess! You can sprint across the lake waters!');
}

let lastT = performance.now();
let fpsCount = 0, fpsTime = 0;

function animate(now) {
  requestAnimationFrame(animate);
  const dt = Math.min(0.05, (now - lastT) / 1000);
  lastT = now;
  T += dt;

  fpsCount++; fpsTime += dt;
  if (fpsTime >= 0.5) {
    const curFps = Math.round(fpsCount / fpsTime);
    fpsCount = 0; fpsTime = 0;
    document.getElementById('fps-display').textContent = `FPS: ${curFps} (Realistic WebGL)`;
  }

  // Keyboard camera turning (Q & E keys)
  if (keys.KeyQ) targetCa -= dt * 2.2;
  if (keys.KeyE && !activePromptAction) targetCa += dt * 2.2;

  // Smooth camera interpolation
  ca += (targetCa - ca) * Math.min(1, dt * 14);
  camPitch += (targetCamPitch - camPitch) * Math.min(1, dt * 14);
  camDist += (targetCamDist - camDist) * Math.min(1, dt * 12);

  // Auto Timers
  if (autoSeason) {
    seasonTimer -= dt;
    if (seasonTimer <= 0) {
      seasonTimer = 55.0;
      const nextIdx = (SEASONS.indexOf(currentSeason) + 1) % SEASONS.length;
      setSeason(SEASONS[nextIdx]);
    }
  }
  if (autoTime) {
    timeOfDay = (timeOfDay + dt * 0.012) % 1.0;
    updateTOD(timeOfDay);
  }
  if (autoWeather) {
    weatherTimer -= dt;
    if (weatherTimer <= 0) {
      weatherTimer = 25 + Math.random() * 20;
      const wl = ['clear', 'fog', 'rain', 'storm'];
      setWeather(wl[(wl.indexOf(weather) + 1 + ((Math.random() * 2) | 0)) % wl.length]);
    }
  }
  if (weather === 'storm') {
    lightningTimer -= dt;
    if (lightningTimer <= 0) {
      lightningFlash = 1.0; lightningTimer = 3.5 + Math.random() * 5.0;
      window.audio.playThunder();
    }
  }
  if (lightningFlash > 0) {
    lightningFlash = Math.max(0, lightningFlash - dt * 3.8);
    ambientLight.intensity = 0.8 + lightningFlash * 2.5;
  }

  // Buff timers
  pw.speed = Math.max(0, pw.speed - dt);
  pw.jump = Math.max(0, pw.jump - dt);
  pw.starlight = Math.max(0, pw.starlight - dt);
  pw.lakeStrider = Math.max(0, pw.lakeStrider - dt);

  const tStr = [];
  if (pw.speed > 0) tStr.push('Swift ' + Math.ceil(pw.speed) + 's');
  if (pw.jump > 0) tStr.push('Moon leap ' + Math.ceil(pw.jump) + 's');
  if (pw.lakeStrider > 0) tStr.push('Lake Strider ' + Math.ceil(pw.lakeStrider) + 's');
  if (pw.starlight > 0) tStr.push('Starlight Sight ' + Math.ceil(pw.starlight) + 's');
  document.getElementById('pw').textContent = tStr.join('   ');

  // Jumping & Gravity
  if (keys.Space && !jumpLatch && jh <= 0) {
    pjv = pw.jump > 0 ? 14 : 7.8; jumpLatch = 1;
    window.audio.playTone(320, 'sine', 0.15, 0.1);
  }
  if (!keys.Space) jumpLatch = 0;
  jh += pjv * dt; pjv -= 22 * dt;
  if (jh <= 0) { jh = 0; pjv = 0; }

  // --- FIXED CAMERA-RELATIVE CONTROLLER MOVEMENT ---
  // Forward/Backward: W, S, ArrowUp, ArrowDown
  // Strafe Left/Right: A, D, ArrowLeft, ArrowRight
  let inFwd = 0, inRight = 0;
  if (keys.KeyW || keys.ArrowUp) inFwd += 1;
  if (keys.KeyS || keys.ArrowDown) inFwd -= 1;
  if (keys.KeyD || keys.ArrowRight) inRight += 1;
  if (keys.KeyA || keys.ArrowLeft) inRight -= 1;

  if (joystickActive) {
    inFwd += joystickY;
    inRight += joystickX;
  }

  const inMag = Math.hypot(inFwd, inRight);
  if (inMag > 0.05) {
    const normFwd = inFwd / (inMag > 1 ? inMag : 1);
    const normRight = inRight / (inMag > 1 ? inMag : 1);

    // Camera forward vector in horizontal X-Z plane
    const camFwd = new THREE.Vector3();
    camera.getWorldDirection(camFwd);
    camFwd.y = 0;
    camFwd.normalize();

    // Camera right vector pointing to true screen RIGHT:
    // Cross product: (0, 1, 0) x camFwd
    const camRight = new THREE.Vector3(0, 1, 0).cross(camFwd).normalize();

    // Compute non-inverted world movement vector
    const moveX = camFwd.x * normFwd + camRight.x * normRight;
    const moveZ = camFwd.z * normFwd + camRight.z * normRight;

    // Smooth character rotation towards movement direction
    const targetAngle = Math.atan2(moveX, moveZ);
    let da = targetAngle - playerAngle;
    da = Math.atan2(Math.sin(da), Math.cos(da));
    playerAngle += da * Math.min(1, dt * 14);

    const onWater = inPond(playerGroup.position.x, playerGroup.position.z);
    const slow = (onWater && pw.lakeStrider <= 0) ? 0.42 : 1.0;
    const isSprinting = keys.ShiftLeft || keys.ShiftRight || mobileSprintActive;
    const sp = isSprinting ? 1.75 : 1.0;
    const v = 7.4 * sp * slow * (pw.speed > 0 ? 1.75 : 1.0);

    const proposedX = playerGroup.position.x + moveX * v * dt;
    const proposedZ = playerGroup.position.z + moveZ * v * dt;

    // SOLID COLLISION RESOLUTION: Character cannot pass through trees, rocks, cabin or boundaries!
    const resolved = window.collisionSystem.resolve(proposedX, proposedZ, 0.42);
    playerGroup.position.x = resolved.x;
    playerGroup.position.z = resolved.z;

    moving = 1; walk += v * dt * 1.6;
    if (jh <= 0.1) {
      window.audio.playStep(onWater ? 'water' : currentSeason === 'winter' ? 'snow' : 'grass');
    }
  } else {
    moving = 0;
  }

  playerGroup.position.y = ht(playerGroup.position.x, playerGroup.position.z) + jh;
  playerGroup.rotation.y = playerAngle;

  // Realistic Character Animations
  legL.rotation.x = moving ? Math.sin(walk * 2.2) * 0.58 : 0;
  legR.rotation.x = moving ? -Math.sin(walk * 2.2) * 0.58 : 0;
  armL.rotation.x = moving ? -Math.sin(walk * 2.2) * 0.45 : 0;
  armR.rotation.x = moving ? Math.sin(walk * 2.2) * 0.25 : 0;
  scarf.rotation.y = Math.sin(T * 3.2) * 0.2;
  lanternGroup.rotation.z = moving ? Math.sin(walk * 2.2) * 0.25 : Math.sin(T * 1.5) * 0.05;

  smokePuffs.forEach((smk, idx) => {
    smk.position.y += dt * 0.65;
    smk.position.x += Math.sin(T * 2 + idx) * 0.015;
    smk.scale.setScalar(1.0 + (smk.position.y - 6.2) * 0.5);
    if (smk.position.y > 9.5) smk.position.y = 6.2;
  });

  // Realistic 3D Leaf Asset floating and orbiting fireflies
  for (const l of leaves) {
    if (!l.got) {
      l.group.rotation.y += dt * 1.8;
      l.group.position.y = ht(l.x, l.z) + 1.25 + Math.sin(T * 2.6 + l.ph) * 0.22;
      
      // Orbiting firefly wisps
      l.wisps.forEach(w => {
        w.phase += dt * w.speed;
        w.mesh.position.set(Math.cos(w.phase) * 0.55, Math.sin(w.phase * 1.5) * 0.28, Math.sin(w.phase) * 0.55);
      });

      if (Math.hypot(playerGroup.position.x - l.x, playerGroup.position.z - l.z) < 2.2) {
        l.got = true; l.group.visible = false; got++;
        document.getElementById('n').textContent = got;
        window.audio.playChime([523, 659, 784, 1046]);
        if (got < 12) toast(got + ' of 12 leaves found');
        else {
          toast('All 12 found! Carry them to the cabin hearth!');
          document.getElementById('obj').textContent = 'Bring them to the cabin';
        }
      }
    }
  }

  // Critters AI
  for (const o of animalList) {
    if (o.gone > 0) {
      o.gone -= dt;
      if (o.gone <= 0) { const s = spot(20, 90); o.x = s[0]; o.z = s[1]; o.mesh.visible = true; }
      continue;
    }
    const dx = o.x - playerGroup.position.x, dz = o.z - playerGroup.position.z, d = Math.hypot(dx, dz);
    let aSpeed = 0;
    if (started && d < 10) { o.ang = Math.atan2(dx, dz) + Math.sin(T * 3 + o.hp) * 0.6; aSpeed = 7.5; }
    else {
      o.tm -= dt;
      if (o.tm <= 0) { o.tm = 1 + Math.random() * 2.5; o.go = Math.random() < 0.55; o.ang = Math.random() * 6.283; }
      aSpeed = o.go ? 1.8 : 0;
    }
    o.vx = Math.sin(o.ang) * aSpeed; o.vz = Math.cos(o.ang) * aSpeed;
    o.x += o.vx * dt; o.z += o.vz * dt;
    o.mesh.position.set(o.x, ht(o.x, o.z) + (aSpeed > 0 ? Math.abs(Math.sin(T * 8)) * 0.25 : 0), o.z);
    o.mesh.rotation.y = o.ang;

    if (started && d < 1.7) {
      o.gone = 8; o.mesh.visible = false; caughtN++;
      document.getElementById('cn').textContent = caughtN;
      toast(o.mystic ? power(o) : 'Caught a ' + o.kind + '!');
      window.audio.playChime([659, 784, 988, 1318]);
    }
  }

  // Spirit Wisps
  for (let i = spiritWisps.length - 1; i >= 0; i--) {
    const w = spiritWisps[i];
    w.life -= dt * 0.8;
    if (w.life <= 0) { scene.remove(w.mesh); spiritWisps.splice(i, 1); continue; }
    const wdx = w.tx - w.mesh.position.x, wdz = w.tz - w.mesh.position.z, wd = Math.hypot(wdx, wdz);
    if (wd > 1.2) {
      w.mesh.position.x += wdx / wd * 18 * dt + Math.sin(T * 6 + w.ph) * 5 * dt;
      w.mesh.position.z += wdz / wd * 18 * dt + Math.cos(T * 6 + w.ph) * 5 * dt;
      w.mesh.position.y = ht(w.mesh.position.x, w.mesh.position.z) + 2.5;
    }
  }

  // Falling Seasonal Particles
  const pPos = particleGeom.attributes.position.array;
  for (let i = 0; i < P_COUNT; i++) {
    pPos[i * 3 + 1] -= (3.5 + Math.sin(i)) * dt;
    pPos[i * 3] += Math.sin(T + i) * 0.8 * dt;
    if (pPos[i * 3 + 1] < 0) {
      pPos[i * 3 + 1] = 22;
      pPos[i * 3] = playerGroup.position.x + (R() - 0.5) * 70;
      pPos[i * 3 + 2] = playerGroup.position.z + (R() - 0.5) * 70;
    }
  }
  particleGeom.attributes.position.needsUpdate = true;

  // Smooth Camera Positioning with Pitch Elevation
  const horizDist = camDist * Math.cos(camPitch);
  const vertDist = camDist * Math.sin(camPitch);
  camera.position.x = playerGroup.position.x - Math.sin(ca) * horizDist;
  camera.position.z = playerGroup.position.z - Math.cos(ca) * horizDist;
  camera.position.y = playerGroup.position.y + vertDist + 1.2;
  camera.lookAt(playerGroup.position.x, playerGroup.position.y + 1.3, playerGroup.position.z);

  updateInteractionPrompts();
  if (toastT > 0 && (toastT -= dt) <= 0) document.getElementById('toast').style.opacity = 0;

  renderer.render(scene, camera);
  drawMinimap();
}
requestAnimationFrame(animate);

function power(o) {
  if (o.kind === 'glimmerpuff') { pw.speed = 12; return 'Swift! You feel light on your feet'; }
  if (o.kind === 'moonbun') { pw.jump = 14; return 'Moon leap! Press Space to soar high'; }
  pw.speed = 18; pw.jump = 18; return 'Sunwisp! Blazing speed and radiant leap together!';
}

// Minimap
const mapCv = document.getElementById('minimap-canvas'), mapG = mapCv.getContext('2d');
function drawMinimap() {
  mapG.clearRect(0, 0, 110, 110);
  const cx = 55, cy = 55, sc = 110 / 220;
  const m = (x, z) => [cx + x * sc, cy + z * sc];
  const pp = m(POND.x, POND.z);
  mapG.fillStyle = '#64b5f6'; mapG.beginPath(); mapG.arc(pp[0], pp[1], POND.rx * sc, 0, 7); mapG.fill();
  const cp = m(CABIN.x, CABIN.z);
  mapG.fillStyle = '#d4623a'; mapG.fillRect(cp[0] - 3, cp[1] - 3, 6, 6);
  const mp = m(MONOLITH.x, MONOLITH.z); mapG.fillStyle = '#00f5d4'; mapG.beginPath(); mapG.arc(mp[0], mp[1], 3, 0, 7); mapG.fill();
  const sp = m(SHRINE.x, SHRINE.z); mapG.fillStyle = '#48cae4'; mapG.fillRect(sp[0] - 2, sp[0] - 2, 4, 4);
  for (const l of leaves) if (!l.got) {
    const lp = m(l.x, l.z); mapG.fillStyle = '#ffb703'; mapG.beginPath(); mapG.arc(lp[0], lp[1], 2.5, 0, 7); mapG.fill();
  }
  const plp = m(playerGroup.position.x, playerGroup.position.z);
  mapG.fillStyle = '#2b2d42'; mapG.beginPath(); mapG.arc(plp[0], plp[1], 4, 0, 7); mapG.fill();
}

addEventListener('resize', () => {
  camera.aspect = innerWidth / innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(innerWidth, innerHeight);
});

// UI Event Handlers
document.getElementById('go').onclick = () => { started = true; document.getElementById('start').hidden = true; window.initAudio(); };
document.getElementById('again').onclick = () => { document.getElementById('win').hidden = true; };

document.getElementById('season-btns').onclick = e => {
  const b = e.target.closest('button'); if (!b) return;
  autoSeason = false; document.getElementById('auto-season').checked = false;
  setSeason(b.dataset.s);
};
document.getElementById('auto-season').onchange = e => { autoSeason = e.target.checked; };

document.getElementById('tod-btns').onclick = e => {
  const b = e.target.closest('button'); if (!b) return;
  autoTime = false; document.getElementById('auto-time').checked = false;
  setTOD(parseFloat(b.dataset.t));
};
document.getElementById('weather-btns').onclick = e => {
  const b = e.target.closest('button'); if (!b) return;
  autoWeather = false; document.getElementById('auto-weather').checked = false;
  setWeather(b.dataset.w);
};
document.getElementById('auto-time').onchange = e => { autoTime = e.target.checked; };
document.getElementById('auto-weather').onchange = e => { autoWeather = e.target.checked; };

const soundBtn = document.getElementById('sound-btn');
const toggleAudioBtn = document.getElementById('toggle-audio-btn');
const toggleSound = () => {
  window.initAudio();
  window.audio.enabled = !window.audio.enabled;
  soundBtn.textContent = window.audio.enabled ? '🔊' : '🔇';
  toggleAudioBtn.textContent = window.audio.enabled ? '🔊 Sound: ON' : '🔇 Sound: OFF';
  toast(window.audio.enabled ? 'Sound effects enabled' : 'Sound muted');
};
soundBtn.onclick = toggleSound;
toggleAudioBtn.onclick = toggleSound;

const menuBtn = document.getElementById('menu-btn');
const settingsModal = document.getElementById('settings-modal');
const closeSettings = document.getElementById('close-settings');
const toggleMenu = () => { settingsModal.hidden = !settingsModal.hidden; };
menuBtn.onclick = toggleMenu;
closeSettings.onclick = () => { settingsModal.hidden = true; };

const cabinView = document.getElementById('cabin-view');
function openCabin() {
  inCabin = true;
  cabinView.hidden = false;
  document.getElementById('avail-leaves').textContent = got - hearthLeaves;
  document.getElementById('hearth-leaves').textContent = hearthLeaves;
}
function closeCabin() {
  inCabin = false;
  cabinView.hidden = true;
}
document.getElementById('exit-cabin-top').onclick = closeCabin;
document.getElementById('exit-cabin-btn').onclick = closeCabin;

document.getElementById('add-leaves-btn').onclick = () => {
  const unburned = got - hearthLeaves;
  if (unburned > 0) {
    hearthLeaves += unburned;
    document.getElementById('hearth-leaves').textContent = hearthLeaves;
    document.getElementById('avail-leaves').textContent = 0;
    window.audio.playChime([523, 659, 784, 1046, 1318]);
    toast(`🔥 Added ${unburned} leaves to the hearth! The fire roars brightly.`);
    if (hearthLeaves >= 12) {
      document.getElementById('win').hidden = false;
      closeCabin();
    }
  } else {
    toast('No gathered leaves in your pouch to burn.');
  }
};

document.getElementById('cider-btn').onclick = () => {
  pw.speed = 30; pw.jump = 30;
  window.audio.playTone(550, 'triangle', 0.5, 0.2);
  toast('☕ Warm spiced cider drunk! Vitality surging for 30s!');
  closeCabin();
};

document.getElementById('sleep-btn').onclick = () => {
  timeOfDay = (timeOfDay + 0.5) % 1.0;
  updateTOD(timeOfDay);
  setWeather('clear');
  toast('🛌 You rested warmly by the hearth. Time has advanced and storm cleared.');
  closeCabin();
};

document.getElementById('travel-cabin-btn').onclick = () => {
  playerGroup.position.set(CABIN.x, ht(CABIN.x, CABIN.z + 7), CABIN.z + 7);
  playerAngle = Math.PI;
  settingsModal.hidden = true;
  toast('Fast traveled to Woodland Cabin porch.');
};
''')

    # Read all modules to bundle into Amber Valley.html
    with open('css/style.css', 'r', encoding='utf-8') as f: css_text = f.read()
    with open('js/audio.js', 'r', encoding='utf-8') as f: audio_text = f.read()
    with open('js/collision.js', 'r', encoding='utf-8') as f: collision_text = f.read()
    with open('js/textures.js', 'r', encoding='utf-8') as f: textures_text = f.read()
    with open('js/leaf.js', 'r', encoding='utf-8') as f: leaf_text = f.read()
    with open('js/character.js', 'r', encoding='utf-8') as f: character_text = f.read()
    with open('js/world.js', 'r', encoding='utf-8') as f: world_text = f.read()
    with open('js/critters.js', 'r', encoding='utf-8') as f: critters_text = f.read()
    with open('js/game.js', 'r', encoding='utf-8') as f: game_text = f.read()

    html_template = r'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Amber Valley</title>
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover, user-scalable=no">
<link href="https://fonts.googleapis.com/css2?family=Gaegu:wght@400;700&family=Nunito:wght@400;600;800&display=swap" rel="stylesheet">
__STYLE_TAG__
<script src="three.min.js"></script>
</head>
<body>

<canvas id="game-canvas"></canvas>

<!-- HUD -->
<div id="hud">
  <div class="hud-title">Leaves <span id="n">0</span> / 12 &nbsp;|&nbsp; Critters <span id="cn">0</span></div>
  <div class="hud-sub" id="season-hud">🍂 Autumn Valley</div>
  <div class="hud-sub" id="obj" style="font-weight:400">Find the glowing leaves</div>
  <div class="hud-buffs" id="pw"></div>
</div>

<!-- Top Bar -->
<div id="top-right-bar">
  <button id="sound-btn" class="top-btn" title="Toggle Sound">🔊</button>
  <button id="menu-btn" class="top-btn" title="Settings">☰</button>
</div>

<!-- Prompts & Minimap -->
<button id="interact-prompt" hidden>🏡 Enter Cabin (Press E)</button>
<canvas id="minimap-canvas" width="110" height="110"></canvas>
<div id="toast"></div>

<!-- Touch Controls for Mobile / Tablets -->
<div id="touch-controls">
  <div id="touch-base">
    <div id="touch-stick"></div>
  </div>
</div>
<div id="mobile-buttons">
  <button id="mobile-sprint" class="mobile-btn" title="Sprint">⚡</button>
  <button id="mobile-jump" class="mobile-btn" title="Jump">⤊</button>
</div>

<!-- Start Overlay -->
<div class="ov" id="start">
  <div class="card">
    <h1>Amber Valley</h1>
    <p>Step into a realistic living valley across shifting seasons. Twelve ancient glowing leaves lie hidden amidst sun-dappled groves and whispering shores.</p>
    <p>Discover the <b>Whispering Monolith</b> to reveal leaf guidance, pray at the <b>Moon Shrine</b> to walk on water, and leap skyward from <b>Fairy Mushrooms</b>!</p>
    <p><b>W / S / Up / Down</b> Walk &nbsp; <b>A / D / Left / Right</b> Strafe &nbsp; <b>Q / E</b> Rotate Camera<br>
    <b>Shift</b> Sprint &nbsp; <b>Space</b> Jump<br>
    <b>Mouse Drag</b> Smooth 360° Camera Look & Pitch &nbsp; <b>Scroll</b> Zoom</p>
    <button id="go" class="action-btn">Enter the Valley</button>
  </div>
</div>

<!-- Win Overlay -->
<div class="ov" id="win" hidden>
  <div class="card">
    <h1>Hearth Lit</h1>
    <p>The cabin hearth blazes warmly, sending fragrant cedar smoke up into the mountain sky. The valley is peaceful and your journey complete.</p>
    <button id="again" class="action-btn">Keep Exploring</button>
  </div>
</div>

<!-- Settings Overlay -->
<div class="ov" id="settings-modal" hidden>
  <div class="card settings-card">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px">
      <h2>Valley Settings</h2>
      <button id="close-settings" style="background:none;border:0;font-size:26px;cursor:pointer;color:var(--ink)">✕</button>
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

    <div class="setting-group" style="margin-top:12px">
      <button id="travel-cabin-btn" style="width:100%;font-size:16px;font-weight:700;padding:9px;background:#8b482b;color:#fff;border:0;border-radius:12px;cursor:pointer">🏡 Fast Travel to Woodland Cabin</button>
    </div>

    <div class="setting-group">
      <div id="fps-display" style="font-size:13px;opacity:0.8;margin-top:6px">FPS: 60 (Realistic Three.js WebGL)</div>
    </div>
  </div>
</div>

<!-- Cabin Modal -->
<div class="ov" id="cabin-view" hidden>
  <div class="card cabin-card">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px">
      <h2 style="font-family:'Gaegu',cursive;margin:0;font-size:40px;color:var(--accent)">🏡 Woodland Cabin</h2>
      <button id="exit-cabin-top" style="background:none;border:0;font-size:26px;cursor:pointer;color:var(--ink)">✕</button>
    </div>
    <p style="margin:4px 0 12px;font-size:15px;opacity:0.92">Warm cedar logs and crackling pine embers shelter you from the chilly valley mountain wind.</p>
    
    <div class="hearth-box">
      <div id="hearth-status" style="font-family:'Gaegu',cursive;font-size:26px;font-weight:700;color:var(--accent)">🔥 Hearth: <span id="hearth-leaves">0</span> / 12 Leaves Burning</div>
      <div id="hearth-desc" style="font-size:14px;margin-top:4px">Leaves placed in the hearth keep the valley illuminated with ancient warmth.</div>
      <button id="add-leaves-btn" class="action-btn" style="margin-top:10px;font-size:22px;padding:8px 24px">🍂 Feed Leaves to Fire (<span id="avail-leaves">0</span> ready)</button>
    </div>

    <div class="cabin-actions">
      <button id="cider-btn" class="cabin-btn">☕ Spiced Cider<small style="display:block;font-size:12px;opacity:0.8;font-weight:400">Swift & Leap vitality</small></button>
      <button id="sleep-btn" class="cabin-btn">🛌 Rest by Fire<small style="display:block;font-size:12px;opacity:0.8;font-weight:400">Advance time & clear storm</small></button>
    </div>

    <div id="cabin-outside-note" style="font-size:14px;margin:8px 0;opacity:0.85;text-align:center">Window: Autumn leaves dancing outside</div>
    <button id="exit-cabin-btn" style="width:100%;margin-top:10px;padding:10px;font-weight:700;border-radius:14px;border:0;background:var(--ink);color:var(--paper);cursor:pointer">🚪 Step Outside into the Valley</button>
  </div>
</div>

__SCRIPT_TAGS__
</body>
</html>'''

    # Scene bootstrap script that initializes Three.js canvas, scene, camera, lights
    bootstrap_js = r'''
const canvas = document.getElementById('game-canvas');
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(50, innerWidth / innerHeight, 0.2, 400);

const renderer = new THREE.WebGLRenderer({
  canvas,
  antialias: true,
  powerPreference: 'high-performance'
});
renderer.setSize(innerWidth, innerHeight);
renderer.setPixelRatio(Math.min(devicePixelRatio || 1, 2));
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.08;

const ambientLight = new THREE.AmbientLight(0xffffff, 0.75);
scene.add(ambientLight);

const sunLight = new THREE.DirectionalLight(0xfff3dc, 1.25);
sunLight.position.set(45, 95, 45);
sunLight.castShadow = true;
sunLight.shadow.mapSize.width = 2048;
sunLight.shadow.mapSize.height = 2048;
sunLight.shadow.camera.near = 10;
sunLight.shadow.camera.far = 240;
sunLight.shadow.camera.left = -85;
sunLight.shadow.camera.right = 85;
sunLight.shadow.camera.top = 85;
sunLight.shadow.camera.bottom = -85;
sunLight.shadow.bias = -0.0006;
scene.add(sunLight);

scene.fog = new THREE.FogExp2(0xebd1a8, 0.0085);
'''

    # Modular index.html
    modular_scripts = """<script>""" + bootstrap_js + """</script>
<script src="js/audio.js"></script>
<script src="js/collision.js"></script>
<script src="js/textures.js"></script>
<script src="js/leaf.js"></script>
<script src="js/character.js"></script>
<script src="js/world.js"></script>
<script src="js/critters.js"></script>
<script src="js/game.js"></script>"""

    index_html = html_template.replace('__STYLE_TAG__', '<link rel="stylesheet" href="css/style.css">').replace('__SCRIPT_TAGS__', modular_scripts)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(index_html)

    # Standalone bundled Amber Valley.html (includes all modules inlined)
    bundled_scripts = f"""<script>
{bootstrap_js}
{audio_text}
{collision_text}
{textures_text}
{leaf_text}
{character_text}
{world_text}
{critters_text}
{game_text}
</script>"""

    bundled_html = html_template.replace('__STYLE_TAG__', f'<style>\n{css_text}\n</style>').replace('__SCRIPT_TAGS__', bundled_scripts)
    with open('Amber Valley.html', 'w', encoding='utf-8') as f:
        f.write(bundled_html)

    print("Project successfully organized and compiled!")

if __name__ == '__main__':
    build()
