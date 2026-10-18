// Solid Collision Physics System for Amber Valley
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
