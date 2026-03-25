// PV Tool — Copyright (c) 2026 DanteAlighieri13210914
// Licensed under Non-Commercial License. See LICENSE for terms.

import * as PIXI from 'pixi.js';

export class MediaOutlineRenderer {
  readonly sprite: PIXI.Sprite;
  readonly w: number;
  readonly h: number;

  private srcCanvas: HTMLCanvasElement;
  private srcCtx: CanvasRenderingContext2D;
  private outCanvas: HTMLCanvasElement;
  private outCtx: CanvasRenderingContext2D;
  private tick = 0;

  constructor(sourceW: number, sourceH: number) {
    const maxDim = 280;
    const scale = Math.min(maxDim / Math.max(sourceW, sourceH), 1);
    this.w = Math.round(sourceW * scale);
    this.h = Math.round(sourceH * scale);

    this.srcCanvas = document.createElement('canvas');
    this.srcCanvas.width = this.w;
    this.srcCanvas.height = this.h;
    this.srcCtx = this.srcCanvas.getContext('2d', { willReadFrequently: true })!;

    this.outCanvas = document.createElement('canvas');
    this.outCanvas.width = this.w;
    this.outCanvas.height = this.h;
    this.outCtx = this.outCanvas.getContext('2d')!;

    const texture = PIXI.Texture.from(this.outCanvas);
    this.sprite = new PIXI.Sprite(texture);
    this.sprite.anchor.set(0.5);
  }

  update(source: HTMLVideoElement | HTMLImageElement): void {
    this.tick++;
    if (this.tick % 3 !== 0) return;

    this.srcCtx.drawImage(source, 0, 0, this.w, this.h);
    const imgData = this.srcCtx.getImageData(0, 0, this.w, this.h);
    const src = imgData.data;

    const edgeMap = new Float32Array(this.w * this.h);
    for (let y = 1; y < this.h - 1; y++) {
      for (let x = 1; x < this.w - 1; x++) {
        const gray = (ox: number, oy: number) => {
          const i = ((y + oy) * this.w + (x + ox)) * 4;
          return src[i] * 0.299 + src[i + 1] * 0.587 + src[i + 2] * 0.114;
        };
        const gx = -gray(-1, -1) - 2 * gray(-1, 0) - gray(-1, 1)
                   + gray(1, -1) + 2 * gray(1, 0) + gray(1, 1);
        const gy = -gray(-1, -1) - 2 * gray(0, -1) - gray(1, -1)
                   + gray(-1, 1) + 2 * gray(0, 1) + gray(1, 1);
        edgeMap[y * this.w + x] = Math.sqrt(gx * gx + gy * gy);
      }
    }

    const outImg = this.outCtx.createImageData(this.w, this.h);
    const out = outImg.data;
    const threshold = 90;

    for (let y = 1; y < this.h - 1; y++) {
      for (let x = 1; x < this.w - 1; x++) {
        const e = edgeMap[y * this.w + x];
        if (e > threshold) {
          const idx = (y * this.w + x) * 4;
          out[idx] = 0;
          out[idx + 1] = 0;
          out[idx + 2] = 0;
          out[idx + 3] = Math.min(e * 1.5, 220);
        }
      }
    }

    this.outCtx.putImageData(outImg, 0, 0);
    this.sprite.texture.source.update();
  }

  destroy(): void {
    this.sprite.destroy(true);
  }
}