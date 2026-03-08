# Frontend MCP 模块 — 详细规格与开发清单

> 模块: `packages/frontend-mcp`  
> 状态: 部分已完成(从blender-mcp继承)  
> 优先级: Phase 0 (基础) + Phase 2 (增强)

---

## 1. 模块目标

为 IDE 和 MCP 客户端提供标准化 MCP 协议接口，支持 18+ MCP 客户端直接连接，并增强配置自动生成和视觉反馈能力。

---

## 2. MCP Server (`server/`)

### 2.1 主入口 (`mcp_server.py`)

- [x] MCP Server初始化与协议握手
- [x] stdio传输模式(默认)
- [x] SSE传输模式(可选，Web场景)
- [x] 服务器信息与能力声明
- [x] 优雅关闭处理
- [x] Agent Core可选集成(二次规划)

### 2.2 Resource Provider (`resource_provider.py`)

- [x] `blender://viewport` — 视口截图Resource
- [x] `blender://scene` — 场景信息Resource
- [x] `blender://objects` — 对象列表Resource
- [x] Resource变更通知(notify)
- [x] 截图缓存与过期策略

### 2.3 Tool Provider (`tool_provider.py`)

- [x] 26个工具的MCP Tool定义(name/description/inputSchema)
- [x] 工具调用路由到Engine层
- [x] 工具执行结果格式化(text/image content)
- [x] 错误处理与用户友好消息

---

## 3. 配置生成 (`config/`)

### 3.1 一键配置 (`setup_generator.py`)

- [x] `blender-mcp setup cursor` — 生成Cursor MCP配置
  - [x] 自动检测Python路径
  - [x] 生成mcp.json/settings.json
- [x] `blender-mcp setup claude-desktop` — Claude Desktop配置
- [x] `blender-mcp setup windsurf` — Windsurf配置
- [x] `blender-mcp setup vscode` — VS Code配置
- [x] `blender-mcp setup generic` — 通用MCP JSON输出
- [x] 配置模板系统(易于添加新客户端)

---

## 4. 兼容性

### 4.1 已验证客户端

- [ ] Cursor
- [ ] Claude Desktop
- [ ] Windsurf
- [ ] Continue (VS Code)
- [ ] Zed
- [ ] Cline
- [ ] 其他12+ MCP客户端

### 4.2 向后兼容

- [ ] 重构后 `uvx ageless-blender-mcp` 继续可用
- [ ] 现有用户配置无需修改
- [ ] 所有现有MCP测试通过

---

## 5. Agent Core 集成(可选)

- [ ] 直连模式: 前端 -> Engine(当前行为，零额外依赖)
- [ ] Agent模式: 前端 -> Agent Core -> Engine(AI规划+安全网关)
- [ ] 模式切换配置项
- [ ] Agent模式下的流式响应透传

---

## 6. 测试清单

- [ ] MCP协议握手测试
- [ ] 26个Tool调用端到端测试
- [x] Resource读取测试
- [x] 配置生成正确性测试(每个IDE)
- [ ] 向后兼容性测试(旧配置可用)
- [ ] 多客户端并发连接测试
