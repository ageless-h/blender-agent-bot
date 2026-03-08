# BlenderAgentBot

> 从单一 MCP 工具进化为多前端 AI 平台 — 让所有用户都能通过 AI 驱动 Blender。

## 愿景

在 [blender-mcp](https://github.com/ageless-h/blender-mcp) 引擎之上，构建完整的多前端生态，覆盖艺术家、开发者、极客和 Pipeline 用户。

## 架构：三层分离

```
用户 → 前端层 → Agent Core (AI 大脑) → Engine (blender-mcp) → Blender
```

| 层 | 职责 | 状态 |
|:---|:---|:---:|
| **Engine** | 26 个工具 + Blender Addon + 通信传输 | 已验证 |
| **Agent Core** | LLM 适配 + 任务规划 + 安全网关 + 技能引擎 | 新建 |
| **Frontend** | Blender 面板 / Web / CLI / MCP | 新建 |

## 四个入口

| 入口 | 目标用户 | 技术 |
|:---|:---|:---|
| 🎨 **Blender 面板** | 艺术家 | bpy.types.Panel + stdin/stdout |
| 🌐 **Web App** | 远程/协作 | React + FastAPI + WebSocket |
| ⌨️ **TUI / CLI** | 极客/Pipeline | Typer + Rich |
| 💻 **IDE / MCP** | 开发者/TA | MCP Protocol |

## 项目结构

```
BlenderAgentBot/
├── packages/
│   ├── engine/              # 核心引擎 (from blender-mcp)
│   ├── agent-core/          # AI 大脑
│   ├── frontend-blender/    # Blender 面板 UI
│   ├── frontend-web/        # Web 应用
│   ├── frontend-cli/        # TUI / CLI
│   └── frontend-mcp/        # MCP 协议前端
├── shared/                  # 统一协议/配置/类型
├── skills/                  # 技能库 (Skill Capsule)
├── examples/                # 示例与模板
├── plan.md                  # 架构设计文档 v4.0
└── pyproject.toml
```

## 核心原则

- **安全第一**: 进程隔离 + 主线程执行 + 分级安全体系
- **版本务实**: 最低 Blender 4.2 LTS，推荐 4.5 LTS+
- **引擎与前端分离**: blender-mcp 是"手臂"，Agent Core 是"大脑"
- **模型自由**: 不绑定任何 LLM 供应商
- **渐进复杂**: 简单事情简单做，复杂事情有路可走

## 开发路线图

- **Phase 0**: 重构基础 (2-3 周) — Engine 抽取 + 统一协议
- **Phase 1**: Agent Core + Blender UI (4-6 周) — AI 大脑 + 艺术家入口
- **Phase 2**: CLI + Web (4-6 周) — 终端和浏览器扩展
- **Phase 3**: 打磨与生态 (4-6 周) — 降级/路由/技能进化/社区

## 快速开始

```bash
# 安装核心 + CLI
pip install -e ".[cli]"

# 或安装全部
pip install -e ".[all]"

# 交互式聊天
blender-agent chat

# 查看状态
blender-agent status
```

## 前置成果

[blender-mcp](https://github.com/ageless-h/blender-mcp) — 已验证核心引擎可行性（4 层架构，26 工具，18+ MCP 客户端，PyPI 发布）

## License

MIT
