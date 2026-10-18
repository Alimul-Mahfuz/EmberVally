// Roaming Critters & Mystic Spirits for Amber Valley
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
