// PV Tool — Copyright (c) 2026 DanteAlighieri13210914
// Licensed under Non-Commercial License. See LICENSE for terms.

export interface ExtractedColors {
  primary: string;
  secondary: string;
  complement: string;
}

export function extractDominantColors(source: CanvasImageSource): ExtractedColors {
  const canvas = document.createElement('canvas');
  const size = 64;
  canvas.width = size;
  canvas.height = size;
  const ctx = canvas.getContext('2d')!;
  ctx.drawImage(source, 0, 0, size, size);
  const data = ctx.getImageData(0, 0, size, size).data;

  const hueBuckets = new Map<number, { count: number; rSum: number; gSum: number; bSum: number }>();
  let totalSaturated = 0;

  for (let i = 0; i < data.length; i += 4) {
    const r = data[i], g = data[i + 1], b = data[i + 2], a = data[i + 3];
    if (a < 128) continue;

    const [h, s, l] = rgbToHsl(r, g, b);
    if (l > 0.82 || s < 0.12) continue;
    if (l < 0.08) continue;

    totalSaturated++;
    const bucket = Math.floor(h / 30) * 30;
    const prev = hueBuckets.get(bucket) || { count: 0, rSum: 0, gSum: 0, bSum: 0 };
    prev.count++;
    prev.rSum += r;
    prev.gSum += g;
    prev.bSum += b;
    hueBuckets.set(bucket, prev);
  }

  const sorted = [...hueBuckets.entries()].sort((a, b) => b[1].count - a[1].count);

  if (sorted.length === 0) {
    return { primary: '#2563eb', secondary: '#ffffff', complement: '#fbbf24' };
  }

  const top = sorted[0][1];
  const pR = Math.round(top.rSum / top.count);
  const pG = Math.round(top.gSum / top.count);
  const pB = Math.round(top.bSum / top.count);
  const primary = rgbToHex(pR, pG, pB);

  let secondary = '#ffffff';
  if (sorted.length > 1 && sorted[1][1].count > totalSaturated * 0.08) {
    const s2 = sorted[1][1];
    secondary = rgbToHex(
      Math.round(s2.rSum / s2.count),
      Math.round(s2.gSum / s2.count),
      Math.round(s2.bSum / s2.count),
    );
  }

  const [ph, , pl] = rgbToHsl(pR, pG, pB);
  const ch = (ph + 155) % 360;
  const cs = 0.6;
  const cl = Math.max(pl, 0.58);
  const [cR, cG, cB] = hslToRgb(ch, cs, cl);
  const complement = rgbToHex(cR, cG, cB);

  return { primary, secondary, complement };
}

function rgbToHsl(r: number, g: number, b: number): [number, number, number] {
  r /= 255; g /= 255; b /= 255;
  const max = Math.max(r, g, b), min = Math.min(r, g, b);
  let h = 0, s = 0;
  const l = (max + min) / 2;
  if (max !== min) {
    const d = max - min;
    s = l > 0.5 ? d / (2 - max - min) : d / (max + min);
    if (max === r) h = ((g - b) / d + (g < b ? 6 : 0)) * 60;
    else if (max === g) h = ((b - r) / d + 2) * 60;
    else h = ((r - g) / d + 4) * 60;
  }
  return [h, s, l];
}

function hslToRgb(h: number, s: number, l: number): [number, number, number] {
  if (s === 0) { const v = Math.round(l * 255); return [v, v, v]; }
  const hue2rgb = (p: number, q: number, t: number) => {
    if (t < 0) t += 1;
    if (t > 1) t -= 1;
    if (t < 1 / 6) return p + (q - p) * 6 * t;
    if (t < 1 / 2) return q;
    if (t < 2 / 3) return p + (q - p) * (2 / 3 - t) * 6;
    return p;
  };
  const q = l < 0.5 ? l * (1 + s) : l + s - l * s;
  const p = 2 * l - q;
  const hn = h / 360;
  return [
    Math.round(hue2rgb(p, q, hn + 1 / 3) * 255),
    Math.round(hue2rgb(p, q, hn) * 255),
    Math.round(hue2rgb(p, q, hn - 1 / 3) * 255),
  ];
}

function rgbToHex(r: number, g: number, b: number): string {
  return '#' + [r, g, b].map(c => c.toString(16).padStart(2, '0')).join('');
}