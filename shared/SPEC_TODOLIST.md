# Shared 模块 — 详细规格与开发清单

> 模块: `shared`  
> 状态: 新建  
> 优先级: Phase 0 (基础设施)

---

## 1. 模块目标

提供跨模块复用的统一消息协议、共享配置 schema 和公共类型定义，确保所有 packages 之间通信格式一致。

---

## 2. 统一消息协议 (`protocol/`)

### 2.1 消息基类 (`messages.py`)

- [x] `MessageType` 枚举 — chat, tool_call, tool_result, error, stream_chunk, confirm_request, confirm_response
- [x] `BaseMessage` 基类 — id, timestamp, type, metadata
- [x] 消息序列化/反序列化 (JSON)
- [x] 消息校验 (Pydantic)

### 2.2 AgentRequest (`agent_request.py`)

- [x] `AgentRequest` — 前端到Agent Core的统一请求
  - [x] session_id — 会话标识
  - [x] message — 用户消息文本
  - [x] attachments — 附件列表(参考图等)
  - [x] context — 附加上下文(选中物体/场景片段)
  - [x] options — 请求选项(模型/角色/安全等级)
- [x] `ToolCallRequest` — 直接工具调用请求
- [x] `ConfirmResponse` — 用户确认/拒绝响应

### 2.3 AgentResponse (`agent_response.py`)

- [x] `AgentResponse` — Agent Core到前端的统一响应
  - [x] session_id — 会话标识
  - [x] message — AI响应文本
  - [x] tool_calls — 已执行的工具调用列表
  - [x] screenshots — 截图列表(base64)
  - [x] status — 成功/失败/需确认
- [x] `StreamChunk` — 流式响应片段
  - [x] delta — 增量文本
  - [x] tool_call_delta — 增量工具调用
  - [x] done — 是否结束
- [x] `ConfirmRequest` — 请求用户确认(Level 2操作)

---

## 3. 共享配置 (`config/`)

### 3.1 配置Schema (`schema.py`)

- [x] `AppConfig` — 顶层应用配置
- [x] `LLMConfig` — LLM配置(provider/model/api_key/base_url)
- [x] `EngineConfig` — Engine配置(transport/host/port)
- [x] `SafetyConfig` — 安全配置(default_level/auto_confirm等)
- [x] `SkillConfig` — 技能配置(builtin_path/community_path)
- [x] `UIConfig` — UI配置(theme/language)
- [x] Pydantic模型 + JSON Schema导出

### 3.2 默认配置 (`defaults.py`)

- [x] 各配置项默认值
- [x] 环境变量覆盖支持(BLENDER_AGENT_*)
- [x] 配置文件路径约定(~/.blender-agent/config.yaml)
- [x] 配置合并逻辑(defaults < file < env < cli args)

---

## 4. 共享类型 (`types/`)

### 4.1 通用类型 (`common.py`)

- [x] `ObjectInfo` — Blender对象信息
- [x] `SceneInfo` — 场景摘要信息
- [x] `ViewportCapture` — 视口截图数据
- [x] `Position3D` / `Rotation3D` / `Scale3D` — 3D变换类型
- [x] `Color` / `MaterialRef` — 颜色和材质引用

### 4.2 工具类型 (`tool_types.py`)

- [x] `ToolDefinition` — 工具定义(name/description/parameters/safety_level)
- [x] `ToolCall` — 工具调用(tool_name/arguments)
- [x] `ToolResult` — 工具执行结果(success/data/error)
- [x] `SafetyLevel` 枚举 — LEVEL_0, LEVEL_1, LEVEL_2, LEVEL_3, FORBIDDEN

### 4.3 会话类型 (`session_types.py`)

- [x] `Session` — 会话数据(id/user_id/created_at/messages)
- [x] `ChatMessage` — 聊天消息(role/content/tool_calls/screenshots)
- [x] `MessageRole` 枚举 — user, assistant, system, tool

---

## 5. 测试清单

- [x] 消息序列化/反序列化往返测试
- [x] AgentRequest/AgentResponse Pydantic校验测试
- [x] 配置Schema校验测试
- [x] 默认配置加载测试
- [x] 环境变量覆盖测试
- [x] 类型定义完整性测试
