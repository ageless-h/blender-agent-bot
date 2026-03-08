# Frontend MCP — MCP 协议前端

> 开发者的入口 — IDE / MCP 客户端直接连接。

## 概述

MCP 协议前端，为 IDE 和 MCP 客户端提供标准化接口。基于已验证的 blender-mcp 协议层，增强配置自动生成、Resource 视口截图回传和可选 Agent Core 二次规划能力。

## 架构

```
frontend-mcp/
├── cli.py                  # blender-mcp 命令入口
├── server/
│   ├── __init__.py
│   ├── mcp_server.py          # MCP Server 主入口
│   ├── resource_provider.py   # MCP Resource 提供(视口截图等)
│   └── tool_provider.py       # MCP Tool 提供(26个工具)
├── config/
│   ├── __init__.py
│   └── setup_generator.py     # 一键生成IDE配置
├── __init__.py
├── pyproject.toml
└── SPEC_TODOLIST.md
```

## 当前状态

已可用 — blender-mcp 天然支持 18+ MCP 客户端（Cursor、Claude Desktop、Windsurf 等）。

## 提升方向

| 当前 | 目标 |
|:---|:---|
| 手动配置 MCP JSON | `blender-mcp setup cursor` 一键生成配置 |
| 纯文本交互 | 利用 MCP Resource 回传视口截图 |
| 无 Agent 层 | 可选集成 Agent Core 做二次规划 |

## 开发

```bash
cd packages/frontend-mcp
pip install -e ".[dev]"
```

## 使用

```bash
# 生成 Cursor 配置
blender-mcp setup cursor

# 生成 VS Code 配置到指定目录
blender-mcp setup vscode --output-root .

# 启动 MCP server（stdio，供 MCP 客户端拉起）
blender-mcp serve --transport stdio

# 启动 MCP server（SSE，供 Web 场景）
blender-mcp serve --transport sse --host 127.0.0.1 --port 8765
```
