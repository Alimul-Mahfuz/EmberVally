// Procedural Textures Generator for Amber Valley
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
