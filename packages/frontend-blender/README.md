# Frontend Blender — Blender 内置面板 UI

> 艺术家的入口 — 不离开 Blender，纯自然语言交互。

## 概述

Blender 内置面板前端，通过 `bpy.types.Panel` 实现侧边栏聊天界面。用户在 Blender 3D 视口旁直接输入自然语言指令，AI 即时响应并操作场景。

## 架构

```
frontend-blender/
├── panels/                # UI 面板
│   ├── __init__.py
│   ├── chat_panel.py      # 聊天面板(消息列表+输入框)
│   ├── settings_panel.py  # 设置面板(模型选择/API Key)
│   └── preview_panel.py   # 操作预览面板
├── operators/             # 自定义操作符
│   ├── __init__.py
│   ├── chat_ops.py        # 发送消息/接收响应
│   ├── undo_ops.py        # 一键撤销AI操作
│   └── confirm_ops.py     # 操作确认/拒绝
├── bridge/                # Agent Core 通信桥
│   ├── __init__.py
│   ├── subprocess_bridge.py # 子进程管理(启动/停止Agent Core)
│   └── message_handler.py   # Stdin/Stdout消息处理
├── __init__.py
├── pyproject.toml
└── SPEC_TODOLIST.md
```

## 核心特性

| 特性 | 说明 |
|:---|:---|
| 零配置启动 | Addon 内置 Agent Core 子进程，自动启动 |
| 操作预览 | 执行前显示即将执行的操作，用户确认后执行 |
| 视觉反馈 | 每步操作后自动截图回显 |
| 一键撤销 | 每条消息旁有撤销按钮 |
| 场景感知 | 自动识别选中物体 |
| 多模态输入 | 支持拖入参考图 |

## 技术实现

```
Addon (bpy.types.Panel) → stdin/stdout → Agent Core 子进程 → Engine → Blender Socket
```

## 开发

```bash
# 将 frontend-blender/ 链接到 Blender addons 目录
# 在 Blender 中启用 BlenderAgentBot 插件
```
