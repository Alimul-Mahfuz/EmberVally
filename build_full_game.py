# Python script to build the full-fledged organized game architecture for Amber Valley
import os

# Complete build script generating all modular files and the integrated bundle
build_script = r'''
import os

print("Building Amber Valley - Full Fledged Game...")

# Ensure directories
os.makedirs('css', exist_ok=True)
os.makedirs('js', exist_ok=True)
os.makedirs('assets', exist_ok=True)

# 1. css/style.css
css_content = """/* Amber Valley - Master Stylesheet */
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

/* --- HUD Overlays --- */
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

/* Modals & Overlays */
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

/* Settings Modal */
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

/* Cabin Modal */
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

/* Interaction prompt */
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

/* Minimap */
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

/* Virtual Joystick for touch / mobile */
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
"""
with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

# 2. js/collision.js
collision_content = """// Solid Collision Physics System for Amber Valley
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
"""
with open('js/collision.js', 'w', encoding='utf-8') as f:
    f.write(collision_content)

# 3. js/textures.js
textures_content = """// Procedural High-Definition Textures Generator
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

// Terrain texture with natural grass & soil speckles
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

// Bark Texture
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

// Wood Plank Texture
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

// Natural Granite Stone Texture (NO grid lines!)
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

// Masonry Ashlar Stone Texture (for Cabin chimney/foundation)
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

// Photorealistic Tapered Grass Blade Cluster Canvas
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

// Realistic Human Skin & Face Canvas Texture
window.skinCanvas = document.createElement('canvas');
window.skinCanvas.width = 256; window.skinCanvas.height = 256;
const sCtx = window.skinCanvas.getContext('2d');
// Base warm skin tone
sCtx.fillStyle = '#f6d5be';
sCtx.fillRect(0, 0, 256, 256);
// Subtle natural skin gradient & blush
const skinGrad = sCtx.createRadialGradient(128, 140, 20, 128, 140, 100);
skinGrad.addColorStop(0, 'rgba(235, 145, 130, 0.45)');
skinGrad.addColorStop(1, 'rgba(246, 213, 190, 0)');
sCtx.fillStyle = skinGrad;
sCtx.fillRect(40, 100, 176, 80);

// Expressive Eyes
function drawEye(x, y) {
  // Eye white
  sCtx.fillStyle = '#ffffff';
  sCtx.beginPath();
  sCtx.ellipse(x, y, 16, 10, 0, 0, Math.PI * 2);
  sCtx.fill();
  // Iris (warm deep hazel)
  sCtx.fillStyle = '#4a2e18';
  sCtx.beginPath();
  sCtx.arc(x, y, 8, 0, Math.PI * 2);
  sCtx.fill();
  // Pupil
  sCtx.fillStyle = '#111111';
  sCtx.beginPath();
  sCtx.arc(x, y, 4, 0, Math.PI * 2);
  sCtx.fill();
  // Specular gleam
  sCtx.fillStyle = '#ffffff';
  sCtx.beginPath();
  sCtx.arc(x - 3, y - 3, 2.5, 0, Math.PI * 2);
  sCtx.fill();
  // Upper eyelid & lash line
  sCtx.strokeStyle = '#2b180d';
  sCtx.lineWidth = 2.5;
  sCtx.beginPath();
  sCtx.arc(x, y - 2, 17, 1.1 * Math.PI, 1.9 * Math.PI);
  sCtx.stroke();
  // Eyebrow
  sCtx.strokeStyle = '#3e2413';
  sCtx.lineWidth = 3.5;
  sCtx.beginPath();
  sCtx.moveTo(x - 18, y - 18);
  sCtx.quadraticCurveTo(x, y - 23, x + 18, y - 17);
  sCtx.stroke();
}
drawEye(85, 115);
drawEye(171, 115);

// Subtle nose tip
sCtx.fillStyle = 'rgba(200, 130, 110, 0.4)';
sCtx.beginPath();
sCtx.arc(128, 148, 5, 0, Math.PI * 2);
sCtx.fill();

// Friendly warm lips
sCtx.strokeStyle = '#c86858';
sCtx.lineWidth = 3.5;
sCtx.beginPath();
sCtx.moveTo(108, 185);
sCtx.quadraticCurveTo(128, 196, 148, 185);
sCtx.stroke();

window.skinTexture = new THREE.CanvasTexture(window.skinCanvas);
"""
with open('js/textures.js', 'w', encoding='utf-8') as f:
    f.write(textures_content)

# 4. js/leaf.js (High-Fidelity 3D Maple/Oak Leaf Asset Generator)
leaf_content = """// High-Fidelity 3D Golden Leaf Asset Generator
function createRealisticLeafTexture() {
  const cv = document.createElement('canvas');
  cv.width = 256; cv.height = 256;
  const ctx = cv.getContext('2d');
  ctx.clearRect(0, 0, 256, 256);

  // Draw authentic 5-pointed Maple / Oak Autumn Leaf
  ctx.save();
  ctx.translate(128, 240);

  // Gradient from glowing golden core to rich crimson edge
  const grad = ctx.createRadialGradient(0, -110, 10, 0, -110, 120);
  grad.addColorStop(0, '#ffe066');
  grad.addColorStop(0.35, '#ff9e00');
  grad.addColorStop(0.75, '#e85d04');
  grad.addColorStop(1, '#9d0208');
  ctx.fillStyle = grad;

  // Leaf perimeter path with serrated lobes
  ctx.beginPath();
  ctx.moveTo(0, 0); // stem base
  // Left lower lobe
  ctx.bezierCurveTo(-25, -30, -70, -45, -75, -75);
  ctx.bezierCurveTo(-85, -65, -95, -75, -85, -95);
  // Left main lobe
  ctx.bezierCurveTo(-105, -110, -115, -145, -90, -165);
  ctx.bezierCurveTo(-80, -155, -65, -165, -55, -180);
  // Center tip
  ctx.bezierCurveTo(-45, -200, -25, -235, 0, -248);
  ctx.bezierCurveTo(25, -235, 45, -200, 55, -180);
  // Right main lobe
  ctx.bezierCurveTo(65, -165, 80, -155, 90, -165);
  ctx.bezierCurveTo(115, -145, 105, -110, 85, -95);
  // Right lower lobe
  ctx.bezierCurveTo(95, -75, 85, -65, 75, -75);
  ctx.bezierCurveTo(70, -45, 25, -30, 0, 0);
  ctx.closePath();
  ctx.fill();

  // Primary & secondary leaf veins (golden glowing)
  ctx.strokeStyle = '#fff3b0';
  ctx.lineWidth = 3.5;
  ctx.beginPath();
  ctx.moveTo(0, 0);
  ctx.lineTo(0, -240); // central spine
  ctx.stroke();

  // Branch veins
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

// Generator for the 3D Collectible Leaf Asset
function createRealisticLeafAsset(x, z) {
  const group = new THREE.Group();

  // 1. Curved 3D Leaf Blade Mesh
  const bladeGeom = new THREE.PlaneGeometry(0.85, 1.1, 4, 4);
  // Curve the leaf geometry slightly along Z for realistic organic 3D curl
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

  // 2. Realistic wooden stem
  const stemGeom = new THREE.CylinderGeometry(0.015, 0.025, 0.35, 8);
  const stemMat = new THREE.MeshStandardMaterial({ color: 0x5c3214, roughness: 0.9 });
  const stem = new THREE.Mesh(stemGeom, stemMat);
  stem.position.set(0, -0.6, -0.05);
  stem.rotation.x = -0.3;
  group.add(stem);

  // 3. Magical Point Light
  const light = new THREE.PointLight(0xffa200, 1.0, 7);
  group.add(light);

  // 4. Orbiting magical firefly wisps (3 miniature spheres)
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
"""
with open('js/leaf.js', 'w', encoding='utf-8') as f:
    f.write(leaf_content)

print("Created css/style.css, js/collision.js, js/textures.js, js/leaf.js!")
'''

with open('build_full_game.py', 'w', encoding='utf-8') as f:
    f.write(build_script)

print("Generated build_full_game.py base.")
