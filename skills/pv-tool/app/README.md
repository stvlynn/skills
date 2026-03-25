# PV Tool — Kinetic Typography & Post-Processing for Music Videos

A browser-based visual effects engine for creating PV (Promotional Video) style kinetic typography and post-processing overlays, built with [PixiJS](https://pixijs.com/) and TypeScript.

Designed for the Japanese PV / music video community and anyone creating lyric videos, motion graphics, or real-time visual performances.

## What It Does

PV Tool takes text (lyrics, titles, poetry) and renders them with layered visual effects in real-time — no video editing software required. Think of it as a programmable, template-driven motion graphics compositor that runs entirely in the browser.

**Core capabilities:**

- **16 preset templates** — curated visual styles ranging from clean typography to cyberpunk HUDs, each combining multiple effects into a cohesive look
- **54 configurable effects** — geometry, text layouts, overlays, textures, organic shapes, composition guides, and more
- **Custom mode** — mix and match any effects from the catalog to build your own style
- **Media input** — load images or videos as background layers with automatic color extraction
- **Audio-reactive** — BPM-synced beat reactivity drives animations and camera effects
- **Motion detection** — real-time browser-based object tracking for interactive HUD overlays
- **Post-processing** — shake, zoom, tilt, glitch, hue shift, chromatic aberration
- **HiDPI support** — renders at native device pixel ratio with automatic downscaling when many effects are active

## Templates

| Template | Style |
|---|---|
| 蓝色冲击 | Bold blue geometric impact |
| 斩击 | Kinetic split with diagonal energy |
| 蓝色构成 | Deconstructed blueprint with physics formulas |
| 城市、文字、雨 | Urban rain with flowing text |
| 夜色 | Soft nocturnal atmosphere |
| 波普 | Pop art halftone and bold colors |
| 青墨 | Ink wash minimalism |
| 电脑 | Digital / cyber aesthetic |
| 战场 | High-intensity battle theme |
| 几何 | Pure geometric composition |
| 全息 | Holographic glow rings |
| 赛博监控 | Cyberpunk HUD with motion tracking |
| 情绪电影 | Cinematic emotion overlay |
| 剪影极简 | Silhouette clean minimalism |
| 歇斯底里之夜 | Radial rectangles with glowing text cards |
| 戒尺 | Ruler guides with breathing blocks |

## Effects Library

Effects are organized by layer and category:

- **Background** — texture fills, gradients, triangle grids, checkerboards, color blocks
- **Decoration** — geometric shapes (circles, diamonds, lines, crosses), flowing lines, burst rays, perspective grids, composition guides (golden spiral, rule of thirds, phi grid), organic blobs, ocean waves, clouds
- **Text** — hero text, scattered text, text strips, text cards, outline text, layered text, glow cards, vertical sub-text, formula overlays, falling text rain
- **Overlay** — vignette, color mask, chromatic aberration, glitch bars, scanlines, film grain, dot screen (halftone), HUD elements
- **Motion** — real-time motion detection brackets with target tracking

## Getting Started

```bash
# Install dependencies
npm install

# Start dev server
npm run dev

# Build for production
npm run build
```

Open the browser and use the controls:

1. **Select a template** from the dropdown, or choose "Custom" to build your own
2. **Enter text** — use `/` to separate segments (e.g. `春を告げる/夜を越えて/踊れ踊れ`)
3. **Load media** — drag in an image or video as background
4. **Load audio** — add music for beat-reactive animations
5. **Adjust parameters** — animation speed, motion intensity, segment timing, post-FX

## Tech Stack

- **[PixiJS 8](https://pixijs.com/)** — WebGL/WebGPU 2D rendering
- **TypeScript** — full type safety
- **Vite** — development and build tooling
- **Canvas 2D** — motion detection, texture generation, media analysis

## License

> **Due to commercial misuse by vtblive and their refusal to negotiate a proper license, this project has been relicensed from AGPL-3.0 to a Non-Commercial License effective 2026/3/24. This change applies to all subsequent updates.**
>
> 由于 vtblive 的商业滥用行为及其拒绝进行合理的授权协商，本项目自 2026/3/24 起由 AGPL-3.0 变更为 Non-Commercial License。此变更适用于此日期之后的所有版本更新。

- **Non-Commercial License** — see [LICENSE](LICENSE) for full terms
- **Commercial License** — see [COMMERCIAL.md](COMMERCIAL.md) for paid license terms

Free for personal use, educational research, and non-commercial community projects.
Any commercial use requires a paid commercial license from the author.

## Author

Copyright (c) 2026 DanteAlighieri13210914. All rights reserved.
