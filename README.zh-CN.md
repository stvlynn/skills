<div align="center">

# 🧩 Agent Skills

**模块化、可复用的 AI Agent 技能集合**

[![Skills](https://img.shields.io/badge/skills-11-blue?style=flat-square)](#skills-列表)
[![Skills CLI](https://img.shields.io/badge/skills_cli-compatible-green?style=flat-square)](https://github.com/vercel-labs/skills)
[![License](https://img.shields.io/github/license/stvlynn/skills?style=flat-square)](LICENSE)

[English](README.md) · 中文文档

</div>

---

## 安装

### 通过 Skills CLI（推荐）

```bash
npx skills add stvlynn/skills --skill create-sticker
```

<details>
<summary>更多安装选项</summary>

```bash
# 全局安装
npx skills add stvlynn/skills --skill searxng -g -y

# 安装全部 skills
npx skills add stvlynn/skills --skill='*' -g

# 安装前预览可用 skills
npx skills add stvlynn/skills --list
```

</details>

### 手动安装

```bash
git clone https://github.com/stvlynn/skills.git
```

---

## Skills 列表

### 🎨 媒体与创作

| Skill | 描述 | 依赖 |
|-------|------|------|
| **[create-sticker](skills/create-sticker/)** | 使用 Google Gemini 生成 LINE 风格角色贴纸，自动去背景 | `GEMINI_API_KEY` |
| **[pv-tool](skills/pv-tool/)** | 运行内置的 PV 动态排版 Web 工具，用于歌词视频、媒体叠加和模板化动效制作 | Node.js 20+、npm |
| **[tsticker](skills/tsticker/)** | 通过 tsticker CLI 管理 Telegram 贴纸包 | `tsticker`、Bot Token |

### 🔊 语音

| Skill | 描述 | 依赖 |
|-------|------|------|
| **[qwen-tts](skills/qwen-tts/)** | 9 种音色 + 情感控制的文字转语音 | Apple Silicon、MLX |
| **[qwen-asr](skills/qwen-asr/)** | 本地 FastAPI 语音转文字服务 | Apple Silicon、MLX |

### 🔍 搜索与数据

| Skill | 描述 | 依赖 |
|-------|------|------|
| **[searxng](skills/searxng/)** | 聚合 70+ 搜索引擎的隐私搜索 | Docker |
| **[xiaohongshu](skills/xiaohongshu/)** | 小红书搜索与帖子详情 | [xiaohongshu-mcp](https://github.com/peanut996/xiaohongshu-mcp) |

### 🎛️ UI 与设计

| Skill | 描述 | 依赖 |
|-------|------|------|
| **[atlassian-design](skills/atlassian-design/)** | 本地 Atlassian Design System 参考 skill，覆盖 Atlaskit、ADS 组件、`xcss`、primitives 和 Jira 风格 React 界面模式 | 无 |

### 🛠️ 开发工具

| Skill | 描述 | 依赖 |
|-------|------|------|
| **[clashctl-linux](skills/clashctl-linux/)** | 初始化、使用和排障 clash for linux，并内置一份裁剪后的上游项目副本以应对 GitHub 访问受限环境 | Linux，推荐有 `git` |
| **[claude-code-operator](skills/claude-code-operator/)** | 编程控制 Claude Code CLI — 启动、执行、部署 | Claude Code |
| **[tip-gui-skill](skills/tip-gui-skill/)** | 将 Youtu-Tip 复用为受保护的本地 GUI 桥接，用于桌面自动化 | macOS、Youtu-Tip |

---

## 配置指南

> 每个 skill 都有 `SKILL.md` 包含完整配置说明。以下为快速参考。
>
> 许可说明：`pv-tool` 内置了上游源码，并沿用其单独的非商用许可证。见 `skills/pv-tool/app/LICENSE` 和 `skills/pv-tool/app/COMMERCIAL.md`。

<details>
<summary><b>clashctl-linux</b> — Linux 上的 Clash/Mihomo 初始化与运维</summary>

<br>

这个 skill 在 `skills/clashctl-linux/scripts/upstream-project/` 下内置了上游 `nelvko/clash-for-linux-install` 项目的裁剪副本。

推荐初始化流程：

```bash
rm -rf /tmp/clash-for-linux-install
git clone --depth 1 https://github.com/nelvko/clash-for-linux-install.git /tmp/clash-for-linux-install || {
  mkdir -p /tmp/clash-for-linux-install
  cp -R skills/clashctl-linux/scripts/upstream-project/. /tmp/clash-for-linux-install/
}
cd /tmp/clash-for-linux-install
bash install.sh
```

安装完成后，上游项目会提供这类 shell functions / wrappers：

- `clashctl on`
- `clashctl off`
- `clashon`
- `clashoff`
- `clashsub`
- `clashmixin`

完整的初始化流程、SOP 和排障说明见 [SKILL.md](skills/clashctl-linux/SKILL.md)。

</details>

<details>
<summary><b>create-sticker</b> — Google Gemini 贴纸生成器</summary>

<br>

<img width="712" height="760" alt="create-sticker 演示" src="https://github.com/user-attachments/assets/c1784abd-0779-496d-b9bf-8e18b3ae66af" />

1. 前往 <https://aistudio.google.com/apikey> 获取 API Key
2. 设置环境变量：
   ```bash
   export GEMINI_API_KEY="your-api-key-here"
   ```
3. 安装依赖：
   ```bash
   cd skills/create-sticker/scripts && pip install -r requirements.txt
   ```

</details>

<details>
<summary><b>pv-tool</b> — PV 动态排版 Web 工具</summary>

<br>

这个 skill 将上游 `pv-tool` 应用内置在 `skills/pv-tool/app/` 下，并补充了简洁的运行与构建脚本。

```bash
cd skills/pv-tool
bash scripts/bootstrap.sh
bash scripts/dev.sh
```

默认开发地址：`http://127.0.0.1:4173/pv-tool/`

其他常用命令：

```bash
bash scripts/build.sh
bash scripts/preview.sh
```

注意：内置的上游应用采用非商用许可证。见 [app/LICENSE](skills/pv-tool/app/LICENSE) 和 [app/COMMERCIAL.md](skills/pv-tool/app/COMMERCIAL.md)。

</details>

<details>
<summary><b>searxng</b> — 本地 SearXNG 隐私搜索引擎</summary>

<br>

需要 Docker。完整的 `docker-compose.yml` 和 `settings.yml` 配置见 [SKILL.md](skills/searxng/SKILL.md)。

```bash
# Docker 配置完成后快速启动
cd ~/service/searxng && docker compose up -d
```

可选：`export SEARXNG_URL="http://localhost:8888"`

</details>

<details>
<summary><b>qwen-tts</b> — Qwen3-TTS 文字转语音</summary>

<br>

> **仅支持 Apple Silicon Mac。** 模型自动从 hf-mirror.com 下载（约 600MB）。

```bash
cd skills/qwen-tts
python3 -m venv venv && source venv/bin/activate
pip install -r scripts/requirements.txt
python3 scripts/tts.py "你好！" --speaker Serena --instruct 开心
```

9 种内置音色：`Serena` `Vivian` `Uncle_Fu` `Ryan` `Aiden` `Ono_Anna` `Sohee` `Eric` `Dylan`

</details>

<details>
<summary><b>qwen-asr</b> — Qwen3-ASR 语音转文字服务</summary>

<br>

> **仅支持 Apple Silicon Mac。** 运行为 FastAPI 服务（端口 8100）。

```bash
cd skills/qwen-asr
python3 -m venv venv && source venv/bin/activate
pip install -r service/requirements.txt
bash service/start.sh
```

验证：`curl http://localhost:8100/health`

</details>

<details>
<summary><b>xiaohongshu</b> — 小红书搜索</summary>

<br>

需要本地运行 [xiaohongshu-mcp](https://github.com/peanut996/xiaohongshu-mcp)。首次使用需登录：

```bash
cd /path/to/xiaohongshu-mcp
./xiaohongshu-login  # 浏览器登录（一次性）
./start.sh           # 启动服务（端口 18060）
```

</details>

<details>
<summary><b>atlassian-design</b> — Atlassian Design System 本地参考包</summary>

<br>

无需额外运行时配置。这个 skill 打包了 Atlassian Design System 文档镜像，适合用于：

- 选择 `@atlaskit/*` 组件
- 查阅 `@atlaskit/primitives`、`xcss`、`@atlaskit/css`
- 参考 Jira 风格导航、表单、布局和反馈模式

建议先从 [references/index.md](skills/atlassian-design/references/index.md) 开始定位对应文档。

</details>

<details>
<summary><b>tip-gui-skill</b> — 受保护的 Youtu-Tip 桌面桥接</summary>

<br>

需要 macOS 和已安装的 Youtu-Tip，并授予以下系统权限：

- 辅助功能
- 屏幕录制

快速检查：

```bash
python3 skills/tip-gui-skill/scripts/tip_gui_bridge.py health
python3 skills/tip-gui-skill/scripts/tip_gui_bridge.py config
```

</details>

<details>
<summary><b>claude-code-operator</b> — Claude Code CLI 自动化</summary>

<br>

```bash
npm install -g @anthropic-ai/claude-code
```

智谱配置和 MCP 部署工作流详见 [SKILL.md](skills/claude-code-operator/SKILL.md)。

</details>

---

<div align="center">
<sub>为 AI Agent 打造。兼容 <a href="https://github.com/vercel-labs/skills">Skills CLI</a>、<a href="https://claude.ai/code">Claude Code</a>，以及任何读取 <code>SKILL.md</code> 的 Agent。</sub>
</div>
