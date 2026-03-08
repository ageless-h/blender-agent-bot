# Engine (blender-mcp 重构)

> BlenderAgentBot 的核心引擎层 — 从 blender-mcp 重构而来，提供 26 个工具 + Blender Addon + 通信传输。

## 概述

Engine 是整个 BlenderAgentBot 生态的"手臂"，负责与 Blender 主进程的所有直接交互。它从 blender-mcp 项目重构而来，抽取为独立包，与上层 Agent Core 完全解耦。

## 架构

```
engine/
├── tools/                 # 26 个工具定义（四层架构）
│   ├── __init__.py
│   ├── perception/        # 感知层 (11 工具) — 只读查询
│   ├── declarative/       # 声明式写入层 (3 工具) — 结构化编辑
│   ├── imperative/        # 命令式写入层 (9 工具) — 高级操作
│   └── fallback/          # 后备层 (3 工具) — 自由代码执行
├── transport/             # 通信传输层
│   ├── __init__.py
│   ├── socket_transport.py    # Socket 传输
│   └── stdio_transport.py     # Stdin/Stdout 传输
├── addon/                 # Blender 插件
│   ├── __init__.py
│   ├── operators.py       # 自定义 Operator（含撤销支持）
│   ├── panels.py          # UI 面板
│   └── timers.py          # bpy.app.timers 轮询
├── executor/              # 安全执行器
│   ├── __init__.py
│   ├── sandbox.py         # 沙箱环境
│   └── context_override.py # 动态上下文捕获
├── __init__.py
├── pyproject.toml
└── SPEC_TODOLIST.md
```

## 四层工具架构

| 层 | 工具数 | 职责 | 示例 |
|:---|:---:|:---|:---|
| **感知层** | 11 | 只读查询场景状态 | `get_objects`, `get_node_tree`, `capture_viewport` |
| **声明式写入层** | 3 | 结构化编辑 | `edit_nodes`, `edit_animation`, `edit_sequencer` |
| **命令式写入层** | 9 | 高级对象操作 | `create_object`, `modify_object`, `manage_material` |
| **后备层** | 3 | 自由代码执行 | `execute_script`, `execute_operator`, `import_export` |

## 通信机制

- Blender `bpy` 非线程安全
- 所有操作通过 `bpy.app.timers` 轮询在主线程执行（每 0.1s）
- 支持 Socket 和 Stdin/Stdout 两种传输模式

## 版本兼容

- **最低**: Blender 4.2 LTS
- **推荐**: Blender 4.5 LTS+
- 需兼容 `temp_override`（4.5+）和旧版上下文覆盖（4.2）

## 开发

```bash
cd packages/engine
pip install -e ".[dev]"
pytest
```

## 来源

重构自 [blender-mcp](https://github.com/ageless-h/blender-mcp)（已验证的核心引擎，26 工具，18+ MCP 客户端支持）
