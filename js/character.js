// Realistic Character Model & Rigging for Amber Valley
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
