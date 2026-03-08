# Agent Core 模块 — 详细规格与开发清单

> 模块: `packages/agent-core`  
> 状态: 新建  
> 优先级: Phase 1 (核心构建)

---

## 1. 模块目标

构建统一的 AI 大脑，所有前端共享同一套 Agent 逻辑，通过多协议暴露服务不同前端。

---

## 2. LLM 适配器 (`llm/`)

### 2.1 抽象基类

- [ ] `LLMAdapter` ABC — 定义 `get_capabilities()`, `generate()`, `stream()` 接口
- [ ] `ModelCapabilities` 数据类 — tool_calling, vision, parallel_tools, max_context
- [ ] `LLMResponse` / `StreamChunk` 统一响应类型

### 2.2 具体适配器

- [ ] `OpenAIAdapter` — GPT系列 + 所有OpenAI兼容API(Ollama/vLLM/LM Studio/LocalAI)
  - [ ] 流式输出支持
  - [ ] tool_use / function_calling 支持
  - [ ] 自定义 base_url 配置
- [ ] `AnthropicAdapter` — Claude系列
  - [ ] 原生 tool_use 协议
  - [ ] 流式输出(SSE)
  - [ ] 200K上下文支持
- [ ] `GoogleAdapter` — Gemini系列
  - [ ] Function calling 支持
  - [ ] 超大上下文(2M)
- [ ] `FallbackAdapter` — 无tool calling的模型
  - [ ] Prompt模拟 + 正则解析JSON
  - [ ] 兼容小模型(Phi-4-mini等)

### 2.3 能力感知降级

- [ ] 无Tool Calling时: Prompt模拟 + 正则解析
- [ ] 无Vision时: 自动生成文本场景摘要替代截图
- [ ] 无并行工具时: 逐个串行调用
- [ ] 小上下文时: 滑动窗口 + 历史摘要压缩

---

## 3. 任务规划器 (`planner/`)

- [ ] `TaskPlanner` — 将模糊指令拆解为工具调用序列
  - [ ] "建个小屋" -> [create x N, material x N, ...]
  - [ ] 支持多步骤任务分解
  - [ ] 失败重试与错误恢复
- [ ] `SkillRouter` — Skill优先 + LLM兜底
  - [ ] 技能库匹配(成功率排序)
  - [ ] 无匹配时LLM从零生成
  - [ ] 执行后验证 + 更新成功率

---

## 4. 安全网关 (`safety/`)

- [ ] `SecurityGateway` — 分级安全体系
  - [ ] Level 0: 只读操作 -> 自动放行
  - [ ] Level 1: 可逆写操作 -> 默认执行，可撤销
  - [ ] Level 2: 高影响操作 -> 需用户确认
  - [ ] Level 3: 危险操作 -> 仅显式授权模式
  - [ ] 禁止级: os.system/subprocess/网络请求/文件删除 -> 绝对拒绝
- [ ] `ASTAnalyzer` — AST静态代码分析
  - [ ] 黑名单检测(危险模块/函数)
  - [ ] 操作危险等级自动标记
- [ ] `ConfirmationFlow` — 用户确认流程
  - [ ] 操作预览显示
  - [ ] 确认/拒绝/修改选项

---

## 5. 上下文引擎 (`context/`)

- [ ] `SceneContext` — 操作前自动拉取场景数据
  - [ ] 自动识别选中物体
  - [ ] 场景状态快照
- [ ] `VisualFeedback` — 操作后截图回传
  - [ ] 视觉验证循环(截图->LLM验证->修正)
  - [ ] 视觉模型降级(无vision时转文本摘要)
- [ ] `HistoryManager` — 对话历史管理
  - [ ] 滑动窗口策略
  - [ ] 历史摘要压缩(大上下文vs小上下文)

---

## 6. 会话管理器 (`session/`)

- [ ] `SessionManager` — 多用户/多会话隔离
  - [ ] 会话创建/销毁/超时
  - [ ] 用户级配置隔离
- [ ] `MessageStore` — 对话历史存储
  - [ ] 内存存储(默认)
  - [ ] 文件持久化(可选)

---

## 7. 技能引擎 (`skills/`)

### Phase 1 基础

- [ ] `SkillStore` — 本地技能库YAML存储
  - [ ] Skill Capsule格式解析(metadata/gene/capsule/validation)
  - [ ] 技能索引与检索
- [ ] `SkillMatcher` — 模糊匹配用户意图到已有技能
  - [ ] 关键词/标签匹配
  - [ ] 成功率排序
- [ ] `SkillExecutor` — 执行Capsule的工具调用序列
  - [ ] 参数替换
  - [ ] 执行后验证(object_exists, object_count等)

### Phase 2 录制与反馈

- [ ] `SkillRecorder` — LLM新操作自动录制为Skill
  - [ ] 操作序列捕获
  - [ ] YAML自动生成
- [ ] `UndoAwareTracker` — 撤销事件监听
  - [ ] undo_rate统计
  - [ ] partial_undo_stats分步统计
  - [ ] 捕获用户undo后手动修正操作

### Phase 3 进化与市场

- [ ] `SkillEvolver` — 成功率驱动的自动优化
  - [ ] 高undo_rate步骤自动标记
  - [ ] 触发LLM重新优化该步骤
- [ ] `SkillMarketplace` — 社区技能包发布/下载
  - [ ] 技能包打包/解包
  - [ ] 版本管理

---

## 8. 工具路由器 (`router/`)

- [ ] `ToolRouter` — Agent决策到blender-mcp调用映射
  - [ ] 工具名称解析
  - [ ] 参数校验
  - [ ] 重试逻辑
  - [ ] 错误恢复

---

## 9. Prompt工程 (`prompts/`)

- [ ] `BasePrompt` — Base Layer(所有模型共享的系统提示)
- [ ] `ModelPrompts` — Model Layer(模型特化指令)
  - [ ] Claude特化
  - [ ] GPT特化
  - [ ] Gemini特化
  - [ ] 本地模型特化
- [ ] `PersonaPrompts` — Persona Layer(角色模板)
  - [ ] `architect` — 建筑可视化
  - [ ] `character` — 角色建模
  - [ ] `game_assets` — 游戏资产
  - [ ] `beginner` — 教学助手

---

## 10. 多协议暴露

- [ ] HTTP REST API (FastAPI) -> Web Frontend
- [ ] WebSocket -> Web实时流
- [ ] Stdin/Stdout -> Blender子进程 / CLI
- [ ] MCP Protocol -> IDE客户端
- [ ] gRPC (可选) -> Pipeline集成

---

## 11. 智能路由与成本控制

- [ ] 任务复杂度评估
- [ ] 简单查询 -> Gemini Flash / 本地模型
- [ ] 常规操作 -> Claude Sonnet / GPT
- [ ] 复杂建模 -> Claude Opus
- [ ] 成本统计与预算控制

---

## 12. 测试清单

- [ ] LLM适配器单元测试(Mock API)
- [ ] 任务规划器集成测试
- [ ] 安全网关AST分析测试
- [ ] 上下文引擎场景快照测试
- [ ] 会话管理并发测试
- [ ] 技能引擎CRUD测试
- [ ] 技能匹配准确率测试
- [ ] 端到端: "建个小屋" 全流程测试
