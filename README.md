<div align="center">

# 🧩 Agent Skills

**Modular, reusable skills for AI coding agents.**

[![Skills](https://img.shields.io/badge/skills-11-blue?style=flat-square)](#skills)
[![Skills CLI](https://img.shields.io/badge/skills_cli-compatible-green?style=flat-square)](https://github.com/vercel-labs/skills)
[![License](https://img.shields.io/github/license/stvlynn/skills?style=flat-square)](LICENSE)

[English](#installation) · [中文文档](README.zh-CN.md)

</div>

---

## Installation

### Via Skills CLI (recommended)

```bash
npx skills add stvlynn/skills --skill create-sticker
```

<details>
<summary>More installation options</summary>

```bash
# Install globally
npx skills add stvlynn/skills --skill searxng -g -y

# Install all skills
npx skills add stvlynn/skills --skill='*' -g

# Preview available skills before installing
npx skills add stvlynn/skills --list
```

</details>

### Manual

```bash
git clone https://github.com/stvlynn/skills.git
```

---

## Skills

### 🎨 Media & Creative

| Skill | Description | Requires |
|-------|-------------|----------|
| **[create-sticker](skills/create-sticker/)** | Generate LINE-style character stickers with background removal | `GEMINI_API_KEY` |
| **[pv-tool](skills/pv-tool/)** | Run a bundled kinetic typography PV web app for lyric videos, media overlays, and template-driven motion graphics | Node.js 20+, npm |
| **[tsticker](skills/tsticker/)** | Manage Telegram sticker packs via `tsticker` CLI | `tsticker`, Bot Token |

### 🔊 Speech

| Skill | Description | Requires |
|-------|-------------|----------|
| **[qwen-tts](skills/qwen-tts/)** | Text-to-speech with 9 voices & emotion control | Apple Silicon, MLX |
| **[qwen-asr](skills/qwen-asr/)** | Speech-to-text via local FastAPI service | Apple Silicon, MLX |

### 🔍 Search & Data

| Skill | Description | Requires |
|-------|-------------|----------|
| **[searxng](skills/searxng/)** | Privacy-respecting web search (70+ engines) | Docker |
| **[xiaohongshu](skills/xiaohongshu/)** | Search & fetch Xiaohongshu posts | [xiaohongshu-mcp](https://github.com/peanut996/xiaohongshu-mcp) |

### 🎛️ UI & Design

| Skill | Description | Requires |
|-------|-------------|----------|
| **[atlassian-design](skills/atlassian-design/)** | Local Atlassian Design System reference skill for Atlaskit, ADS components, xcss, primitives, and Jira-style React UI patterns | None |

### 🛠️ Developer Tools

| Skill | Description | Requires |
|-------|-------------|----------|
| **[clashctl-linux](skills/clashctl-linux/)** | Bootstrap, operate, and troubleshoot clashctl-linux, with a trimmed vendored upstream fallback for GitHub-constrained environments | Linux, `git` recommended |
| **[claude-code-operator](skills/claude-code-operator/)** | Operate Claude Code CLI — spawn, execute, deploy | Claude Code |
| **[tip-gui-skill](skills/tip-gui-skill/)** | Reuse Youtu-Tip as a guarded local GUI bridge for desktop automation | macOS, Youtu-Tip |

---

## Setup

> Each skill has a `SKILL.md` with full setup instructions. Below is a quick reference.
>
> Licensing note: `pv-tool` vendors upstream code under its own non-commercial license. See `skills/pv-tool/app/LICENSE` and `skills/pv-tool/app/COMMERCIAL.md`.

<details>
<summary><b>clashctl-linux</b> — Bootstrap and operate Clash/Mihomo on Linux</summary>

<br>

This skill vendors a trimmed copy of the upstream `nelvko/clash-for-linux-install` project under `skills/clashctl-linux/scripts/upstream-project/`.

Recommended bootstrap flow:

```bash
rm -rf /tmp/clash-for-linux-install
git clone --depth 1 https://github.com/nelvko/clash-for-linux-install.git /tmp/clash-for-linux-install || {
  mkdir -p /tmp/clash-for-linux-install
  cp -R skills/clashctl-linux/scripts/upstream-project/. /tmp/clash-for-linux-install/
}
cd /tmp/clash-for-linux-install
bash install.sh
```

After installation, the upstream project exposes shell functions and wrappers such as:

- `clashctl on`
- `clashctl off`
- `clashon`
- `clashoff`
- `clashsub`
- `clashmixin`

See [SKILL.md](skills/clashctl-linux/SKILL.md) for the full initialization flow, SOP, and troubleshooting guidance.

</details>

<details>
<summary><b>create-sticker</b> — Google Gemini sticker generator</summary>

<br>

<img width="712" height="760" alt="create-sticker demo" src="https://github.com/user-attachments/assets/c1784abd-0779-496d-b9bf-8e18b3ae66af" />

1. Get an API key at <https://aistudio.google.com/apikey>
2. Set the environment variable:
   ```bash
   export GEMINI_API_KEY="your-api-key-here"
   ```
3. Install dependencies:
   ```bash
   cd skills/create-sticker/scripts && pip install -r requirements.txt
   ```

</details>

<details>
<summary><b>pv-tool</b> — Kinetic typography PV web app</summary>

<br>

This skill bundles the upstream `pv-tool` app under `skills/pv-tool/app/` and wraps it with simple run/build scripts.

```bash
cd skills/pv-tool
bash scripts/bootstrap.sh
bash scripts/dev.sh
```

Default dev URL: `http://127.0.0.1:4173/pv-tool/`

Other common commands:

```bash
bash scripts/build.sh
bash scripts/preview.sh
```

Important: the bundled upstream app is released under a non-commercial license. See [app/LICENSE](skills/pv-tool/app/LICENSE) and [app/COMMERCIAL.md](skills/pv-tool/app/COMMERCIAL.md).

</details>

<details>
<summary><b>searxng</b> — Local SearXNG metasearch engine</summary>

<br>

Requires Docker. See [SKILL.md](skills/searxng/SKILL.md) for a complete `docker-compose.yml` and `settings.yml` setup.

```bash
# Quick start (after Docker setup)
cd ~/service/searxng && docker compose up -d
```

Optional: `export SEARXNG_URL="http://localhost:8888"`

</details>

<details>
<summary><b>qwen-tts</b> — Qwen3-TTS text-to-speech</summary>

<br>

> **Apple Silicon only.** Models download automatically from hf-mirror.com (~600MB).

```bash
cd skills/qwen-tts
python3 -m venv venv && source venv/bin/activate
pip install -r scripts/requirements.txt
python3 scripts/tts.py "Hello!" --speaker Ryan --language English
```

9 built-in voices: `Serena` `Vivian` `Uncle_Fu` `Ryan` `Aiden` `Ono_Anna` `Sohee` `Eric` `Dylan`

</details>

<details>
<summary><b>qwen-asr</b> — Qwen3-ASR speech-to-text service</summary>

<br>

> **Apple Silicon only.** Runs as a FastAPI service on port 8100.

```bash
cd skills/qwen-asr
python3 -m venv venv && source venv/bin/activate
pip install -r service/requirements.txt
bash service/start.sh
```

Test: `curl http://localhost:8100/health`

</details>

<details>
<summary><b>xiaohongshu</b> — Xiaohongshu (Little Red Book) search</summary>

<br>

Requires [xiaohongshu-mcp](https://github.com/peanut996/xiaohongshu-mcp) running locally. Login on first use:

```bash
cd /path/to/xiaohongshu-mcp
./xiaohongshu-login  # one-time browser login
./start.sh           # starts on port 18060
```

</details>

<details>
<summary><b>atlassian-design</b> — Atlassian Design System reference bundle</summary>

<br>

No runtime setup required. This skill packages a local mirror of the Atlassian Design System docs for:

- `@atlaskit/*` component selection
- `@atlaskit/primitives`, `xcss`, and `@atlaskit/css`
- Jira-style navigation, forms, layout, and feedback patterns

Start with [references/index.md](skills/atlassian-design/references/index.md) to route to the right mirrored docs.

</details>

<details>
<summary><b>tip-gui-skill</b> — Guarded Youtu-Tip desktop bridge</summary>

<br>

Requires macOS and Youtu-Tip with the needed system permissions:

- Accessibility
- Screen Recording

Quick checks:

```bash
python3 skills/tip-gui-skill/scripts/tip_gui_bridge.py health
python3 skills/tip-gui-skill/scripts/tip_gui_bridge.py config
```

</details>

<details>
<summary><b>claude-code-operator</b> — Claude Code CLI automation</summary>

<br>

```bash
npm install -g @anthropic-ai/claude-code
```

See [SKILL.md](skills/claude-code-operator/SKILL.md) for Zhipu configuration and MCP deployment workflows.

</details>

---

<div align="center">
<sub>Built for AI agents. Works with <a href="https://github.com/vercel-labs/skills">Skills CLI</a>, <a href="https://claude.ai/code">Claude Code</a>, and any agent that reads <code>SKILL.md</code>.</sub>
</div>
