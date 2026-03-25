// PV Tool — Copyright (c) 2026 DanteAlighieri13210914
// Licensed under Non-Commercial License. See LICENSE for terms.

/**
 * Browser-based motion detector using frame differencing.
 * Translates the OpenCV MOG2-based MotionDetector from the reference project
 * into a Canvas 2D implementation suitable for real-time use with video elements.
 */

export interface MotionTarget {
  id: string;
  x: number;
  y: number;
  w: number;
  h: number;
  area: number;
  framesUnseen: number;
}

export interface MotionDetectorConfig {
  /** Minimum contour area to be considered a target (in detector-resolution pixels) */
  minArea?: number;
  /** Maximum number of tracked targets */
  maxTargets?: number;
  /** Minimum distance between targets to avoid merging */
  minDistance?: number;
  /** Internal processing resolution width (lower = faster) */
  processWidth?: number;
  /** Pixel brightness diff threshold (0-255) */
  diffThreshold?: number;
  /** Morphological kernel size for noise removal */
  morphKernel?: number;
  /** How many unseen frames before dropping a target */
  maxUnseen?: number;
}

const DEFAULT_CONFIG: Required<MotionDetectorConfig> = {
  minArea: 200,
  maxTargets: 5,
  minDistance: 60,
  processWidth: 320,
  diffThreshold: 30,
  morphKernel: 3,
  maxUnseen: 15,
};

let nextTargetId = 1;
function genId(): string {
  return `T-${String(nextTargetId++).padStart(4, '0')}`;
}

function dist(x1: number, y1: number, x2: number, y2: number): number {
  return Math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2);
}

export class MotionDetector {
  private cfg: Required<MotionDetectorConfig>;
  private canvas: HTMLCanvasElement;
  private ctx: CanvasRenderingContext2D;
  private procW: number;
  private procH: number;
  private prevGray: Uint8ClampedArray | null = null;
  private targets: MotionTarget[] = [];
  private tick = 0;
  private scaleX = 1;
  private scaleY = 1;

  constructor(config?: MotionDetectorConfig) {
    this.cfg = { ...DEFAULT_CONFIG, ...config };
    this.procW = this.cfg.processWidth;
    this.procH = Math.round(this.procW * 9 / 16);
    this.canvas = document.createElement('canvas');
    this.canvas.width = this.procW;
    this.canvas.height = this.procH;
    this.ctx = this.canvas.getContext('2d', { willReadFrequently: true })!;
  }

  /**
   * Detect motion targets from a video frame.
   * Returns targets in source-resolution coordinates.
   */
  detect(source: HTMLVideoElement): MotionTarget[] {
    this.tick++;
    if (this.tick % 2 !== 0) return this.targets;

    const srcW = source.videoWidth || 1;
    const srcH = source.videoHeight || 1;

    const aspect = srcH / srcW;
    this.procH = Math.round(this.procW * aspect);
    if (this.canvas.height !== this.procH) {
      this.canvas.height = this.procH;
      this.prevGray = null;
    }

    this.scaleX = srcW / this.procW;
    this.scaleY = srcH / this.procH;

    this.ctx.drawImage(source, 0, 0, this.procW, this.procH);
    const imgData = this.ctx.getImageData(0, 0, this.procW, this.procH);
    const pixels = imgData.data;

    const gray = new Uint8ClampedArray(this.procW * this.procH);
    for (let i = 0; i < gray.length; i++) {
      const p = i * 4;
      gray[i] = Math.round(pixels[p] * 0.299 + pixels[p + 1] * 0.587 + pixels[p + 2] * 0.114);
    }

    if (!this.prevGray) {
      this.prevGray = gray;
      return this.targets;
    }

    const diff = this.frameDiff(this.prevGray, gray);
    const cleaned = this.morphOpen(diff, this.cfg.morphKernel);
    const bboxes = this.findContourBboxes(cleaned);
    this.prevGray = gray;

    const selected = this.filterAndSelect(bboxes);
    this.updateTargets(selected);

    return this.targets;
  }

  getTargetsForDisplay(screenW: number, screenH: number, sourceW: number, sourceH: number): MotionTarget[] {
    const displayScaleX = screenW / sourceW;
    const displayScaleY = screenH / sourceH;
    return this.targets.map(t => ({
      ...t,
      x: t.x * displayScaleX,
      y: t.y * displayScaleY,
      w: t.w * displayScaleX,
      h: t.h * displayScaleY,
    }));
  }

  private frameDiff(prev: Uint8ClampedArray, curr: Uint8ClampedArray): Uint8ClampedArray {
    const result = new Uint8ClampedArray(prev.length);
    const threshold = this.cfg.diffThreshold;
    for (let i = 0; i < prev.length; i++) {
      result[i] = Math.abs(curr[i] - prev[i]) > threshold ? 255 : 0;
    }
    return result;
  }

  /** Simple morphological open (erode then dilate) to remove noise */
  private morphOpen(mask: Uint8ClampedArray, kernelSize: number): Uint8ClampedArray {
    const half = Math.floor(kernelSize / 2);
    const w = this.procW;
    const h = this.procH;
    const eroded = new Uint8ClampedArray(mask.length);
    const dilated = new Uint8ClampedArray(mask.length);

    for (let y = half; y < h - half; y++) {
      for (let x = half; x < w - half; x++) {
        let allSet = true;
        for (let dy = -half; dy <= half && allSet; dy++) {
          for (let dx = -half; dx <= half && allSet; dx++) {
            if (mask[(y + dy) * w + (x + dx)] === 0) allSet = false;
          }
        }
        eroded[y * w + x] = allSet ? 255 : 0;
      }
    }

    for (let y = half; y < h - half; y++) {
      for (let x = half; x < w - half; x++) {
        let anySet = false;
        for (let dy = -half; dy <= half && !anySet; dy++) {
          for (let dx = -half; dx <= half && !anySet; dx++) {
            if (eroded[(y + dy) * w + (x + dx)] === 255) anySet = true;
          }
        }
        dilated[y * w + x] = anySet ? 255 : 0;
      }
    }

    return dilated;
  }

  /** Connected-component bounding box extraction via flood fill */
  private findContourBboxes(mask: Uint8ClampedArray): Array<{ x: number; y: number; w: number; h: number; area: number }> {
    const w = this.procW;
    const h = this.procH;
    const visited = new Uint8Array(w * h);
    const result: Array<{ x: number; y: number; w: number; h: number; area: number }> = [];

    for (let y = 0; y < h; y++) {
      for (let x = 0; x < w; x++) {
        const idx = y * w + x;
        if (mask[idx] === 0 || visited[idx]) continue;

        let minX = x, maxX = x, minY = y, maxY = y;
        let area = 0;
        const stack = [idx];
        visited[idx] = 1;

        while (stack.length > 0) {
          const ci = stack.pop()!;
          const cx = ci % w;
          const cy = Math.floor(ci / w);
          area++;
          if (cx < minX) minX = cx;
          if (cx > maxX) maxX = cx;
          if (cy < minY) minY = cy;
          if (cy > maxY) maxY = cy;

          const neighbors = [ci - 1, ci + 1, ci - w, ci + w];
          for (const ni of neighbors) {
            if (ni >= 0 && ni < w * h && !visited[ni] && mask[ni] === 255) {
              visited[ni] = 1;
              stack.push(ni);
            }
          }
        }

        if (area >= this.cfg.minArea) {
          const bw = maxX - minX + 1;
          const bh = maxY - minY + 1;
          const aspect = bw / bh;
          if (aspect > 0.2 && aspect < 5) {
            result.push({
              x: Math.round(minX * this.scaleX),
              y: Math.round(minY * this.scaleY),
              w: Math.round(bw * this.scaleX),
              h: Math.round(bh * this.scaleY),
              area: Math.round(area * this.scaleX * this.scaleY),
            });
          }
        }
      }
    }

    return result;
  }

  private filterAndSelect(bboxes: Array<{ x: number; y: number; w: number; h: number; area: number }>): Array<{ x: number; y: number; w: number; h: number; area: number }> {
    bboxes.sort((a, b) => b.area - a.area);
    const selected: typeof bboxes = [];

    for (const cand of bboxes) {
      if (selected.length >= this.cfg.maxTargets) break;
      const cx = cand.x + cand.w / 2;
      const cy = cand.y + cand.h / 2;
      const minDist = this.cfg.minDistance * this.scaleX;

      let tooClose = false;
      for (const s of selected) {
        const sx = s.x + s.w / 2;
        const sy = s.y + s.h / 2;
        if (dist(cx, cy, sx, sy) < minDist) {
          tooClose = true;
          break;
        }
      }
      if (!tooClose) selected.push(cand);
    }

    return selected;
  }

  private updateTargets(currentBboxes: Array<{ x: number; y: number; w: number; h: number; area: number }>): void {
    const updatedIndices = new Set<number>();
    const usedBboxes = new Set<number>();
    const matchDist = this.cfg.minDistance * this.scaleX * 1.5;

    for (let i = 0; i < this.targets.length; i++) {
      const t = this.targets[i];
      const tcx = t.x + t.w / 2;
      const tcy = t.y + t.h / 2;
      let bestDist = Infinity;
      let bestIdx = -1;

      for (let j = 0; j < currentBboxes.length; j++) {
        if (usedBboxes.has(j)) continue;
        const b = currentBboxes[j];
        const bcx = b.x + b.w / 2;
        const bcy = b.y + b.h / 2;
        const d = dist(tcx, tcy, bcx, bcy);
        if (d < matchDist && d < bestDist) {
          bestDist = d;
          bestIdx = j;
        }
      }

      if (bestIdx >= 0) {
        const b = currentBboxes[bestIdx];
        t.x = b.x;
        t.y = b.y;
        t.w = b.w;
        t.h = b.h;
        t.area = b.area;
        t.framesUnseen = 0;
        updatedIndices.add(i);
        usedBboxes.add(bestIdx);
      } else {
        t.framesUnseen++;
      }
    }

    this.targets = this.targets.filter((t, i) =>
      updatedIndices.has(i) || t.framesUnseen < this.cfg.maxUnseen
    );

    for (let j = 0; j < currentBboxes.length; j++) {
      if (usedBboxes.has(j)) continue;
      const b = currentBboxes[j];
      this.targets.push({
        id: genId(),
        x: b.x,
        y: b.y,
        w: b.w,
        h: b.h,
        area: b.area,
        framesUnseen: 0,
      });
    }
  }

  destroy(): void {
    this.prevGray = null;
    this.targets = [];
  }
}