# Frontend CLI 模块 — 详细规格与开发清单

> 模块: `packages/frontend-cli`  
> 状态: 新建  
> 优先级: Phase 2 (扩展前端)

---

## 1. 模块目标

为极客和 Pipeline 用户提供终端交互入口，支持交互式聊天、批处理脚本执行、一键配置和直接工具调用。

---

## 2. CLI 入口 (`cli/main.py`)

- [x] Typer应用初始化
- [x] 全局选项: `--model`, `--api-key`, `--endpoint`, `--verbose`
- [x] 版本显示: `blender-agent --version`
- [x] 帮助信息: `blender-agent --help`
- [x] 子命令注册: chat, run, setup, status, tools

---

## 3. 交互式聊天 (`cli/chat.py`)

- [x] `blender-agent chat` — 启动交互式REPL
- [x] Rich美化输出(Markdown渲染、语法高亮)
- [x] 流式响应显示(逐token)
- [x] 聊天历史保存/加载
- [x] 特殊命令:
  - [x] `/undo` — 撤销上一步操作
  - [x] `/clear` — 清空聊天历史
  - [x] `/scene` — 显示当前场景信息
  - [x] `/screenshot` — 截取视口截图(保存到文件)
  - [x] `/model <name>` — 切换LLM模型
  - [x] `/exit` — 退出
- [x] 多行输入支持(用于粘贴复杂指令)
- [x] Tab补全(工具名/命令名)

---

## 4. 批处理模式 (`cli/batch.py`)

- [x] `blender-agent run script.yaml` — 执行YAML批处理脚本
- [x] YAML脚本格式定义:
  - [x] 顺序执行步骤
  - [x] 条件分支
  - [x] 循环(批量生成)
  - [x] 变量替换
- [x] 执行进度显示
- [x] 错误处理(继续/停止/重试)
- [x] 结果报告输出(JSON/文本)
- [x] 干运行模式(`--dry-run`)

---

## 5. 一键配置 (`cli/setup.py`)

- [x] `blender-agent setup` — 交互式配置向导
- [x] 自动检测已安装的Blender版本
- [x] LLM提供商选择与API Key配置
- [x] 本地模型检测(Ollama/vLLM/LM Studio)
- [x] Blender Addon自动安装/链接
- [x] IDE MCP配置生成:
  - [x] `blender-agent setup cursor` — Cursor MCP配置
  - [x] `blender-agent setup vscode` — VS Code配置
  - [x] `blender-agent setup windsurf` — Windsurf配置
- [x] 配置文件写入(~/.blender-agent/config.yaml)
- [x] 配置验证与连接测试

---

## 6. 连接状态 (`cli/status.py`)

- [x] `blender-agent status` — 显示系统状态
- [x] Blender连接状态(已连接/断开/版本)
- [x] Agent Core状态(运行中/停止)
- [x] 当前LLM模型信息
- [x] 当前场景摘要(物体数/选中物体)
- [x] 技能库统计(已加载技能数)

---

## 7. 直接工具调用 (`cli/tools.py`)

- [x] `blender-agent tools <tool_name> [args]` — 直接调用引擎工具
- [x] `blender-agent tools --list` — 列出所有可用工具
- [x] `blender-agent tools --info <tool_name>` — 工具详情
- [x] JSON参数输入支持
- [x] 输出格式化(JSON/表格/树形)

---

## 8. 技术规格

- [x] CLI框架: Typer (Click底层)
- [x] TUI美化: Rich
- [x] 配置管理: pyyaml + pydantic
- [x] 通信: Agent Core Stdin/Stdout 或 HTTP

---

## 9. 测试清单

- [x] CLI入口测试(所有子命令可用)
- [x] 交互式聊天REPL测试
- [x] 批处理脚本解析与执行测试
- [x] 配置向导流程测试
- [x] 状态检查测试
- [x] 工具直接调用测试
- [x] Tab补全测试
