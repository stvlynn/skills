---
name: pv-tool
description: Operate the bundled PV Tool kinetic typography web app for lyric videos, promotional videos, and motion-graphics text overlays. Use this whenever the user mentions PV Tool, wants to run or preview the app locally, build it for distribution, experiment with PV templates and effects, or work with lyric text, media backgrounds, audio-reactive overlays, or LRC input inside PV Tool.
---

# PV Tool Skill

Use this skill to operate the vendored `pv-tool` application in `app/`.

## What this skill is for

- Start the local PV Tool dev server
- Build the bundled app
- Preview the production build
- Use the app for lyric-video and kinetic-typography workflows

## Important license note

The bundled upstream app in `app/` is **not** under a generic permissive license.

- Non-commercial use only by default
- Commercial use requires a separate license from the upstream author
- Check `app/LICENSE` and `app/COMMERCIAL.md` before using it for paid work

If the user asks to use PV Tool for a commercial workflow, call out this restriction explicitly.

## Runtime requirements

- Node.js 20+
- npm

## Commands

Run commands from `skills/pv-tool/`:

```bash
bash scripts/bootstrap.sh
bash scripts/dev.sh
bash scripts/build.sh
bash scripts/preview.sh
```

Environment overrides:

```bash
PV_TOOL_DEV_HOST=0.0.0.0
PV_TOOL_DEV_PORT=4173
PV_TOOL_PREVIEW_HOST=127.0.0.1
PV_TOOL_PREVIEW_PORT=4174
VITE_BASE=/pv-tool/
```

## Standard workflow

1. Run `bash scripts/bootstrap.sh` to install dependencies into `app/node_modules`.
2. Run `bash scripts/dev.sh` for local editing and experimentation.
3. Open the reported local URL and use the UI.
4. Run `bash scripts/build.sh` when the user wants a production build.
5. Run `bash scripts/preview.sh` to verify the built output in a browser.

## In-app usage

- Start from a preset template or switch to `Custom`
- Enter text with `/` as the segment separator
- Load an image or video as the background media layer
- Load audio for BPM and beat-reactive effects
- Import `.lrc` files for lyric timing
- Adjust post-FX such as shake, zoom, tilt, glitch, and hue shift
- Use the built-in recording/export controls when the user needs captured output

## Agent behavior

- Prefer running the provided scripts instead of manually restating npm commands.
- When starting `dev.sh` or `preview.sh`, report the exact local URL.
- Keep long-running server processes attached unless the user asks to daemonize them.
- If dependencies are missing, let the wrapper scripts install them first.
- If Node.js is too old, stop and tell the user to upgrade before proceeding.

## File layout

- `app/` — vendored upstream PV Tool source
- `scripts/bootstrap.sh` — dependency installation
- `scripts/dev.sh` — local Vite dev server
- `scripts/build.sh` — production build
- `scripts/preview.sh` — local preview server
