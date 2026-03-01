# OpenClaw Agent Skills

Reusable skills for [OpenClaw](https://github.com/nicepkg/openclaw) agents.

## Skills

| Skill | Description |
|-------|-------------|
| [create-sticker](skills/create-sticker/) | Generate LINE-style character stickers with background removal using Google Gemini |
| [tsticker](skills/tsticker/) | Manage Telegram sticker packs via `tsticker` CLI |

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

##### Installation

```bash
git clone <repo-url> ~/.openclaw/skills
cd ~/.openclaw/skills/skills/create-sticker/scripts
pip install -r requirements.txt
```
