# OpenClaw Agent Skills

Reusable skills for [OpenClaw](https://github.com/nicepkg/openclaw) agents.

## Skills

| Skill | Description |
|-------|-------------|
| [create-sticker](skills/create-sticker/) | Generate LINE-style character stickers with background removal using Google Gemini |
| [tsticker](skills/tsticker/) | Manage Telegram sticker packs via `tsticker` CLI |
| [searxng](skills/searxng/) | Privacy-respecting web search powered by local SearXNG instance |
| [qwen-tts](skills/qwen-tts/) | Text-to-speech using Qwen3-TTS CustomVoice (MLX, Apple Silicon) |
| [qwen-asr](skills/qwen-asr/) | Speech-to-text using Qwen3-ASR via local FastAPI service (MLX, Apple Silicon) |

## Guide

### create-sticker

<img width="712" height="760" alt="image" src="https://github.com/user-attachments/assets/c1784abd-0779-496d-b9bf-8e18b3ae66af" />

#### Environment Variables

首次使用前，需要获取并配置以下环境变量：

`GEMINI_API_KEY`（create-sticker 需要）

1. 前往 <https://aistudio.google.com/apikey> 获取 API Key
2. 写入 shell 配置文件：
   ```bash
   echo 'export GEMINI_API_KEY="your-api-key-here"' >> ~/.zshrc
   source ~/.zshrc
   ```

### SearXNG（searxng 需要）

searxng skill 需要本地运行 SearXNG 实例。详见 [searxng/SKILL.md](skills/searxng/SKILL.md) 中的 **First-time Deployment** 部分。

可选环境变量：
```bash
export SEARXNG_URL="http://localhost:8888"   # 默认值
```

### Qwen TTS / ASR（Apple Silicon 本地模型）

两个 skill 都基于 MLX 运行，仅支持 Apple Silicon Mac。模型自动从 hf-mirror.com 下载。

```bash
# TTS 部署
cd ~/.openclaw/skills/skills/qwen-tts
python3 -m venv venv && source venv/bin/activate
pip install -r scripts/requirements.txt

# ASR 部署
cd ~/.openclaw/skills/skills/qwen-asr
python3 -m venv venv && source venv/bin/activate
pip install -r service/requirements.txt
bash service/start.sh  # 启动 ASR 服务 (port 8100)
```

详见各 skill 的 SKILL.md 中 **First-time Deployment** 部分。

## Installation

```bash
git clone <repo-url> ~/.openclaw/skills
cd ~/.openclaw/skills/skills/create-sticker/scripts
pip install -r requirements.txt
```
