# Agent Core — 统一的 AI 大脑

> BlenderAgentBot 的核心智能层 — 所有前端共享同一套 Agent 逻辑。

## 概述

Agent Core 是整个 BlenderAgentBot 生态的"大脑"，负责 LLM 适配、任务规划、安全网关、上下文引擎、会话管理和技能引擎。所有前端（Blender面板/Web/CLI/MCP）共享同一套逻辑，避免重复实现和行为不一致。

## 架构

```
agent-core/
├── llm/                   # LLM 适配器
│   ├── __init__.py
│   ├── base.py            # LLMAdapter 抽象基类
│   ├── openai_adapter.py  # GPT + Ollama + vLLM + LM Studio + LocalAI
│   ├── anthropic_adapter.py # Claude 系列
│   ├── google_adapter.py  # Gemini 系列
│   └── fallback_adapter.py # 无 tool calling 的降级方案
├── planner/               # 任务规划器
│   ├── __init__.py
│   ├── task_planner.py    # 模糊指令 -> 工具调用序列
│   └── skill_router.py    # Skill优先 + LLM兜底 路由
├── safety/                # 安全网关
│   ├── __init__.py
│   ├── gateway.py         # 分级安全体系 (Level 0-3)
│   ├── ast_analyzer.py    # AST 静态分析
│   └── confirmation.py    # 用户确认流程
├── context/               # 上下文引擎
│   ├── __init__.py
│   ├── scene_context.py   # 操作前自动拉取场景数据
│   ├── visual_feedback.py # 操作后截图回传
│   └── history_manager.py # 滑动窗口 + 历史摘要压缩
├── session/               # 会话管理器
│   ├── __init__.py
│   ├── session_manager.py # 多用户/多会话隔离
│   └── message_store.py   # 对话历史维护
├── skills/                # 技能引擎
│   ├── __init__.py
│   ├── skill_store.py     # 本地技能库存储(YAML)
│   ├── skill_matcher.py   # 模糊匹配用户意图
│   ├── skill_executor.py  # 执行Capsule工具调用序列
│   ├── skill_recorder.py  # LLM操作自动录制为Skill
│   ├── skill_evolver.py   # 成功率驱动的自动优化
│   ├── skill_marketplace.py # 社区技能包发布/下载
│   └── undo_tracker.py    # 撤销事件监听(隐式负反馈)
├── router/                # 工具路由器
│   ├── __init__.py
│   └── tool_router.py     # Agent决策 -> blender-mcp调用映射
├── prompts/               # Prompt 工程
│   ├── __init__.py
│   ├── base_prompt.py     # Base Layer (所有模型共享)
│   ├── model_prompts.py   # Model Layer (模型特化指令)
│   └── persona_prompts.py # Persona Layer (角色模板)
├── __init__.py
├── pyproject.toml
└── SPEC_TODOLIST.md
```

## 多协议暴露

Agent Core 通过多协议同时服务不同前端：

- **HTTP REST API** -> Web Frontend
- **WebSocket** -> Web (实时流)
- **Stdin/Stdout** -> Blender 子进程 / CLI
- **MCP Protocol** -> IDE 客户端
- **gRPC (可选)** -> Pipeline 集成

## 模型支持

| 适配器 | 覆盖模型 |
|:---|:---|
| `OpenAIAdapter` | GPT + Ollama + vLLM + LM Studio + LocalAI |
| `AnthropicAdapter` | Claude 系列 |
| `GoogleAdapter` | Gemini 系列 |
| `FallbackAdapter` | 无 tool calling 模型(Prompt模拟) |

## 开发

```bash
cd packages/agent-core
pip install -e ".[dev]"
pytest
```
