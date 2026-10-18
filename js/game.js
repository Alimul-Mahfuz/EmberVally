// Main Game Loop & Input System with Correct Non-Inverted Controls
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
