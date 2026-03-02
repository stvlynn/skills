# Agent Skills

Reusable skills for AI agents. Compatible with [Skills CLI](https://github.com/vercel-labs/skills).

[中文文档](README.zh-CN.md)

## Installation

### Via Skills CLI (recommended)

Install individual skills with `npx skills add`:

```bash
# Install a single skill
npx skills add stvlynn/skills --skill create-sticker

# Install globally
npx skills add stvlynn/skills --skill searxng -g -y

# List available skills before installing
npx skills add stvlynn/skills --list
```

### Manual (git clone)

```bash
git clone https://github.com/stvlynn/skills.git
```

## Skills

| Skill | Description |
|-------|-------------|
| [create-sticker](skills/create-sticker/) | Generate LINE-style character stickers with background removal using Google Gemini |
| [tsticker](skills/tsticker/) | Manage Telegram sticker packs via `tsticker` CLI |
| [searxng](skills/searxng/) | Privacy-respecting web search powered by a local SearXNG instance |
| [qwen-tts](skills/qwen-tts/) | Text-to-speech using Qwen3-TTS CustomVoice (MLX, Apple Silicon) |
| [qwen-asr](skills/qwen-asr/) | Speech-to-text using Qwen3-ASR via local FastAPI service (MLX, Apple Silicon) |
| [xiaohongshu](skills/xiaohongshu/) | Search and fetch Xiaohongshu (Little Red Book) posts via local MCP service |
| [claude-code-operator](skills/claude-code-operator/) | Operate Claude Code CLI programmatically — spawn, execute, deploy |

## Setup

Each skill may require additional setup. See the `SKILL.md` inside each skill directory for details.

### create-sticker

<img width="712" height="760" alt="image" src="https://github.com/user-attachments/assets/c1784abd-0779-496d-b9bf-8e18b3ae66af" />

Requires `GEMINI_API_KEY`:

1. Get an API key at <https://aistudio.google.com/apikey>
2. Add to your shell profile:
   ```bash
   echo 'export GEMINI_API_KEY="your-api-key-here"' >> ~/.zshrc
   source ~/.zshrc
   ```
3. Install Python dependencies:
   ```bash
   cd skills/create-sticker/scripts
   pip install -r requirements.txt
   ```

### searxng

Requires a local SearXNG instance. See [searxng/SKILL.md](skills/searxng/SKILL.md) **First-time Deployment** section for Docker Compose setup.

Optional environment variable:
```bash
export SEARXNG_URL="http://localhost:8888"  # default
```

### qwen-tts / qwen-asr

Both run on MLX — **Apple Silicon Mac only**. Models are downloaded automatically from hf-mirror.com.

```bash
# TTS setup
cd skills/qwen-tts
python3 -m venv venv && source venv/bin/activate
pip install -r scripts/requirements.txt

# ASR setup
cd skills/qwen-asr
python3 -m venv venv && source venv/bin/activate
pip install -r service/requirements.txt
bash service/start.sh  # starts ASR service on port 8100
```

See each skill's `SKILL.md` for full deployment guides.

### xiaohongshu

Requires [xiaohongshu-mcp](https://github.com/peanut996/xiaohongshu-mcp) service running locally. Login required on first use.

### claude-code-operator

Requires [Claude Code](https://docs.anthropic.com/en/docs/claude-code) installed (`npm install -g @anthropic-ai/claude-code`). See [SKILL.md](skills/claude-code-operator/SKILL.md) for configuration options.
