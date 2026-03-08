# Shared — 共享基础设施

> 所有模块共享的协议、配置和类型定义。

## 概述

Shared 层提供跨模块复用的基础设施：统一消息协议、共享配置 schema 和公共类型定义。确保所有 packages 模块之间通信格式一致、配置互通。

## 架构

```
shared/
├── protocol/              # 统一消息格式
│   ├── __init__.py
│   ├── messages.py        # 消息基类与枚举
│   ├── agent_request.py   # AgentRequest 定义
│   └── agent_response.py  # AgentResponse 定义
├── config/                # 共享配置 schema
│   ├── __init__.py
│   ├── schema.py          # 配置 schema (Pydantic)
│   └── defaults.py        # 默认配置值
├── types/                 # 共享类型定义
│   ├── __init__.py
│   ├── common.py          # 通用类型
│   ├── tool_types.py      # 工具相关类型
│   └── session_types.py   # 会话相关类型
├── __init__.py
├── pyproject.toml
└── SPEC_TODOLIST.md
```

## 核心协议

- **AgentRequest** — 前端 -> Agent Core 的统一请求格式
- **AgentResponse** — Agent Core -> 前端的统一响应格式
- 支持流式响应 (StreamChunk)

## 开发

```bash
cd shared
pip install -e ".[dev]"
pytest
```
