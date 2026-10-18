// Procedural Web Audio Engine for Amber Valley
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
