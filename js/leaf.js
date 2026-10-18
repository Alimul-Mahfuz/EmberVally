// High-Fidelity 3D Golden Leaf Asset Generator
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
