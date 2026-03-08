# Frontend CLI — TUI / CLI

> 极客和 Pipeline 的入口 — 终端中控制 Blender。

## 概述

命令行前端，提供交互式聊天和批处理两种模式。基于 Typer/Click 实现，支持直接调用工具、一键配置安装和连接状态检查。

## 架构

```
frontend-cli/
├── cli/
│   ├── __init__.py
│   ├── main.py            # CLI 入口 (Typer app)
│   ├── chat.py            # 交互式聊天模式
│   ├── batch.py           # 批处理模式 (YAML 脚本)
│   ├── setup.py           # 一键配置安装
│   ├── status.py          # 连接状态检查
│   └── tools.py           # 直接调用工具
├── __init__.py
├── pyproject.toml
└── SPEC_TODOLIST.md
```

## 命令概览

```bash
$ blender-agent chat                    # 交互式聊天
$ blender-agent run script.yaml         # 批处理
$ blender-agent setup                   # 一键配置安装
$ blender-agent status                  # 连接状态
$ blender-agent tools blender_get_scene # 直接调用工具
```

## 批处理脚本示例

```yaml
vars:
  prefix: Cube
  ids: [1, 2, 3]

steps:
  - name: create-objects
    tool: blender_create_object
    args:
      name: "{{ prefix }}_{{ item }}"
      type: MESH
    loop:
      var: item
      in: "{{ ids }}"

  - name: snapshot
    if: "{{ prefix }} == 'Cube'"
    tool: blender_capture_viewport
    args:
      output_path: "./preview.png"
```

```bash
$ blender-agent run script.yaml --output json
$ blender-agent run script.yaml --dry-run
```

## Setup 子命令

```bash
$ blender-agent setup                         # 交互式配置向导
$ blender-agent setup --non-interactive      # 非交互式配置
$ blender-agent setup cursor                 # 生成 Cursor MCP 配置
$ blender-agent setup vscode                 # 生成 VS Code MCP 配置
$ blender-agent setup windsurf               # 生成 Windsurf MCP 配置
$ blender-agent setup cursor --print-only    # 仅打印 MCP 配置
```

## 技术栈

- **CLI框架**: Typer (Click底层)
- **TUI**: Rich (美化输出)
- **通信**: Agent Core Stdin/Stdout

## 开发

```bash
cd packages/frontend-cli
pip install -e ".[dev]"
blender-agent --help
```
