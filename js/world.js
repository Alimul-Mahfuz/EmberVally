// 3D Environment & Landmarks for Amber Valley
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
