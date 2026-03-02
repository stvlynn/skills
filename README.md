<div align="center">

# 🧩 Agent Skills

**Modular, reusable skills for AI coding agents.**

[![Skills](https://img.shields.io/badge/skills-7-blue?style=flat-square)](#skills)
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

### 🛠️ Developer Tools

| Skill | Description | Requires |
|-------|-------------|----------|
| **[claude-code-operator](skills/claude-code-operator/)** | Operate Claude Code CLI — spawn, execute, deploy | Claude Code |

---

## Setup

> Each skill has a `SKILL.md` with full setup instructions. Below is a quick reference.

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
