// PV Tool — Copyright (c) 2026 DanteAlighieri13210914
// Licensed under Non-Commercial License. See LICENSE for terms.

/**
 * Provides beat intensity (0~1) from either an internal metronome
 * or real-time audio analysis via Web Audio API (all free, built-in browser APIs).
 */
export class BeatProvider {
  private audioCtx: AudioContext | null = null;
  private analyser: AnalyserNode | null = null;
  private source: MediaElementAudioSourceNode | null = null;
  private audioEl: HTMLAudioElement | null = null;
  private freqData: Uint8Array<ArrayBuffer> | null = null;

  private _bpm = 120;
  private _useAudio = false;

  private energyHistory: number[] = [];
  private readonly historyLen = 30;
  private rawBeat = 0;
  private smoothBeat = 0;

  set bpm(val: number) { this._bpm = Math.max(30, Math.min(300, val)); }
  get bpm() { return this._bpm; }

  get isAudioMode() { return this._useAudio && this.audioEl !== null; }

  async loadAudio(file: File): Promise<HTMLAudioElement> {
    this.dispose();

    this.audioCtx = new AudioContext();
    this.analyser = this.audioCtx.createAnalyser();
    this.analyser.fftSize = 512;
    this.analyser.smoothingTimeConstant = 0.4;

    const url = URL.createObjectURL(file);
    this.audioEl = new Audio();
    this.audioEl.src = url;
    this.audioEl.loop = true;

    this.source = this.audioCtx.createMediaElementSource(this.audioEl);
    this.source.connect(this.analyser);
    this.analyser.connect(this.audioCtx.destination);

    this.freqData = new Uint8Array(this.analyser.frequencyBinCount) as Uint8Array<ArrayBuffer>;
    this._useAudio = true;
    this.energyHistory = [];

    await this.audioEl.play();
    return this.audioEl;
  }

  /** Get current beat intensity (0 ~ 1) */
  getIntensity(time: number): number {
    if (this._useAudio && this.analyser && this.freqData) {
      return this.analyzeAudio();
    }
    return this.internalBeat(time);
  }

  private internalBeat(time: number): number {
    const beatInterval = 60 / this._bpm;
    const phase = (time % beatInterval) / beatInterval;
    // Sharp attack, exponential decay
    const raw = Math.exp(-phase * 6);
    return raw;
  }

  private analyzeAudio(): number {
    this.analyser!.getByteFrequencyData(this.freqData!);

    // Bass energy: first ~10 bins cover roughly 0-430 Hz at 44.1kHz / 512 FFT
    const bassEnd = 10;
    let bassEnergy = 0;
    for (let i = 0; i < bassEnd; i++) {
      bassEnergy += this.freqData![i];
    }
    bassEnergy /= bassEnd * 255;

    // Mid energy for detecting snares/claps
    const midStart = 10;
    const midEnd = 40;
    let midEnergy = 0;
    for (let i = midStart; i < midEnd; i++) {
      midEnergy += this.freqData![i];
    }
    midEnergy /= (midEnd - midStart) * 255;

    const combined = bassEnergy * 0.7 + midEnergy * 0.3;

    this.energyHistory.push(combined);
    if (this.energyHistory.length > this.historyLen) {
      this.energyHistory.shift();
    }

    const avg = this.energyHistory.reduce((a, b) => a + b, 0) / this.energyHistory.length;

    // Onset detection: current energy significantly above rolling average
    const threshold = 1.3;
    if (combined > avg * threshold && combined > 0.15) {
      this.rawBeat = Math.min(1, (combined - avg * threshold) / 0.3 + 0.5);
    }

    // Smooth decay
    this.smoothBeat = Math.max(this.rawBeat, this.smoothBeat * 0.85);
    this.rawBeat *= 0.7;

    return Math.min(1, this.smoothBeat);
  }

  pause(): void {
    this.audioEl?.pause();
  }

  resume(): void {
    if (this.audioCtx?.state === 'suspended') {
      this.audioCtx.resume();
    }
    this.audioEl?.play();
  }

  get audioContext(): AudioContext | null { return this.audioCtx; }
  get sourceNode(): MediaElementAudioSourceNode | null { return this.source; }

  get paused(): boolean {
    return this.audioEl?.paused ?? true;
  }

  get currentTime(): number {
    return this.audioEl?.currentTime ?? 0;
  }

  get duration(): number {
    return this.audioEl?.duration ?? 0;
  }

  seek(time: number): void {
    if (!this.audioEl) return;
    const duration = Number.isFinite(this.audioEl.duration) ? this.audioEl.duration : Infinity;
    this.audioEl.currentTime = Math.max(0, Math.min(time, duration));
  }

  dispose(): void {
    this.audioEl?.pause();
    this.source?.disconnect();
    this.analyser?.disconnect();
    this.audioCtx?.close();
    this.audioEl = null;
    this.source = null;
    this.analyser = null;
    this.audioCtx = null;
    this.freqData = null;
    this._useAudio = false;
    this.energyHistory = [];
    this.rawBeat = 0;
    this.smoothBeat = 0;
  }
}