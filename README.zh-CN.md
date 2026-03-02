# Agent Skills

可复用的 AI Agent 技能集合。兼容 [Skills CLI](https://github.com/vercel-labs/skills)。

## 安装

### 通过 Skills CLI（推荐）

使用 `npx skills add` 安装单个 skill：

```bash
# 安装单个 skill
npx skills add stvlynn/skills --skill create-sticker

# 全局安装
npx skills add stvlynn/skills --skill searxng -g -y

# 安装前预览可用 skills
npx skills add stvlynn/skills --list
```

### 手动安装（git clone）

```bash
git clone https://github.com/stvlynn/skills.git
```

## Skills 列表

| Skill | 描述 |
|-------|------|
| [create-sticker](skills/create-sticker/) | 使用 Google Gemini 生成 LINE 风格角色贴纸，自动去背景 |
| [tsticker](skills/tsticker/) | 通过 tsticker CLI 管理 Telegram 贴纸包 |
| [searxng](skills/searxng/) | 基于本地 SearXNG 实例的隐私搜索引擎 |
| [qwen-tts](skills/qwen-tts/) | Qwen3-TTS CustomVoice 文字转语音（MLX，Apple Silicon） |
| [qwen-asr](skills/qwen-asr/) | Qwen3-ASR 语音转文字，本地 FastAPI 服务（MLX，Apple Silicon） |
| [xiaohongshu](skills/xiaohongshu/) | 小红书搜索与帖子详情，基于 xiaohongshu-mcp 本地服务 |
| [claude-code-operator](skills/claude-code-operator/) | 编程控制 Claude Code CLI — 启动、执行、部署 |

## 配置指南

每个 skill 可能需要额外配置，详见各 skill 目录下的 `SKILL.md`。

### create-sticker

<img width="712" height="760" alt="image" src="https://github.com/user-attachments/assets/c1784abd-0779-496d-b9bf-8e18b3ae66af" />

需要 `GEMINI_API_KEY`：

1. 前往 <https://aistudio.google.com/apikey> 获取 API Key
2. 写入 shell 配置文件：
   ```bash
   echo 'export GEMINI_API_KEY="your-api-key-here"' >> ~/.zshrc
   source ~/.zshrc
   ```
3. 安装 Python 依赖：
   ```bash
   cd skills/create-sticker/scripts
   pip install -r requirements.txt
   ```

### searxng

需要本地运行 SearXNG 实例。详见 [searxng/SKILL.md](skills/searxng/SKILL.md) 中的 **First-time Deployment** 部分（Docker Compose 部署）。

可选环境变量：
```bash
export SEARXNG_URL="http://localhost:8888"   # 默认值
```

### qwen-tts / qwen-asr

两个 skill 都基于 MLX 运行，**仅支持 Apple Silicon Mac**。模型自动从 hf-mirror.com 下载。

```bash
# TTS 部署
cd skills/qwen-tts
python3 -m venv venv && source venv/bin/activate
pip install -r scripts/requirements.txt

# ASR 部署
cd skills/qwen-asr
python3 -m venv venv && source venv/bin/activate
pip install -r service/requirements.txt
bash service/start.sh  # 启动 ASR 服务 (port 8100)
```

详见各 skill 的 SKILL.md 中 **First-time Deployment** 部分。

### xiaohongshu

需要部署 [xiaohongshu-mcp](https://github.com/peanut996/xiaohongshu-mcp) 服务。首次使用需登录。

### claude-code-operator

需要安装 [Claude Code](https://docs.anthropic.com/en/docs/claude-code)（`npm install -g @anthropic-ai/claude-code`）。配置选项详见 [SKILL.md](skills/claude-code-operator/SKILL.md)。
