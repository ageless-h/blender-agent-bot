# Phase 0 完成核对清单（夯实基础）

**核对日期**: 2026-03-09  
**目标**: 确保 Phase 0（引擎抽取 + 统一协议）真正夯实，所有基础问题都解决

---

## Phase 0 核心目标

根据 `plan.md`：

> **Phase 0：重构基础（2-3 周）**
> 
> 将 blender-mcp 拆分为 engine + mcp-frontend，不改变外部行为

**核心任务**：
- [ ] 从 blender-mcp 中抽取 engine 层为独立包
- [ ] 定义统一的 `AgentRequest / AgentResponse` 消息协议
- [ ] 确保重构后 MCP 模式完全兼容
- [ ] **里程碑**: 所有现有 MCP 测试通过，`uvx ageless-blender-mcp` 继续可用

---

## 🔴 P0 Critical Issues（必须修复才能进入 Phase 1）

### Issue #11: Engine 层 Pydantic 协议使用不完整

**链接**: https://github.com/ageless-h/blender-agent-bot/issues/11

**问题**: 
- Engine 内部使用 Pydantic（`execute_request`）
- 但对外暴露 dict 接口（`execute_capability`）
- 失去类型安全，API 不一致

**当前状态**: ❌ **未修复**

**修复方案**: 
1. 修改 MCP Frontend 使用 `execute_request()`
2. 废弃或标记 `execute_capability()` 为 deprecated
3. 更新测试用例

**验收标准**:
- [ ] MCP Frontend 使用 `execute_request(EngineRequest) -> EngineResponse`
- [ ] 所有测试通过
- [ ] 文档更新

**预计工作量**: 2-4 小时

**阻塞**: ✅ **阻塞 Phase 1** - 这是统一协议的核心

---

## ✅ 已完成的核心工作

### 1. Engine 层抽取

**状态**: ✅ **完成**

**验证**:
```bash
packages/engine/blender_engine/
├── adapters/
│   ├── base.py          ✅
│   ├── socket.py        ✅
│   ├── stdio.py         ✅
│   └── mock.py          ✅
├── security/
│   ├── allowlist.py     ✅
│   ├── guardrails.py    ✅
│   ├── rate_limit.py    ✅
│   └── audit.py         ✅
├── catalog/
│   └── catalog.py       ✅ (26 capabilities)
├── addon/
│   ├── __init__.py      ✅
│   ├── operators.py     ✅
│   ├── preferences.py   ✅
│   ├── ui.py            ✅
│   ├── handlers/        ✅
│   └── server/          ✅
└── engine.py            ✅
```

**结论**: Engine 层已完整抽取，包含所有必要组件。

---

### 2. 统一协议定义

**状态**: ⚠️ **部分完成**（Issue #11 待修复）

**验证**:
```python
# shared/protocol/engine_protocol.py
✅ EngineRequest          # 定义完整
✅ EngineResponse         # 定义完整
✅ EngineRequestType      # 枚举清晰
✅ EngineResponseStatus   # 枚举清晰
✅ CapabilityInfo         # 元数据完善

# packages/engine/blender_engine/engine.py
✅ execute_request(EngineRequest) -> EngineResponse  # 内部使用 Pydantic
❌ execute_capability(str, dict) -> dict             # 对外仍是 dict
```

**结论**: 协议定义完整，但使用不完整（Issue #11）。

---

### 3. MCP Frontend 抽取

**状态**: ✅ **完成**

**验证**:
```bash
packages/frontend-mcp/
├── blender_mcp_frontend/
│   ├── mcp_server.py      ✅ 使用 Engine 层
│   ├── tool_registry.py   ✅ 26 个工具定义
│   └── prompts/           ✅ prompts 系统
└── pyproject.toml         ✅
```

**结论**: MCP Frontend 已成功抽取并适配 Engine。

---

### 4. 验证测试

**状态**: ✅ **通过**

**验证**:
```bash
tests/test_phase0_verification.py
✅ Engine initialization successful
✅ Engine execute_capability returned: blocked
✅ Engine list_capabilities returned 26 capabilities
✅ MCP Frontend initialization successful
✅ MCP tools_list returned 26 tools
✅ MCP tools_call executed successfully
```

**结论**: 所有验证测试通过。

---

## 🟡 P1 High Priority Issues（强烈建议在 Phase 0 完成）

### Issue #2: 协议版本控制

**链接**: https://github.com/ageless-h/blender-agent-bot/issues/2

**问题**: `EngineRequest/EngineResponse` 缺少 `protocol_version` 字段

**当前状态**: ❌ **未修复**

**修复方案**:
```python
class EngineRequest(BaseModel):
    protocol_version: str = "1.0"  # 添加版本字段
    request_type: EngineRequestType
    ...
```

**验收标准**:
- [ ] `EngineRequest` 添加 `protocol_version` 字段
- [ ] `EngineResponse` 添加 `protocol_version` 字段
- [ ] Engine 添加版本验证逻辑
- [ ] 测试用例更新

**预计工作量**: 2-4 小时

**阻塞**: ⚠️ **不阻塞 Phase 1**，但强烈建议完成（前瞻性设计）

---

### Issue #3: 错误类型枚举

**链接**: https://github.com/ageless-h/blender-agent-bot/issues/3

**问题**: `error_type` 是字符串而非枚举

**当前状态**: ❌ **未修复**

**修复方案**:
```python
class EngineErrorType(str, Enum):
    CAPABILITY_NOT_FOUND = "capability_not_found"
    VALIDATION_ERROR = "validation_error"
    EXECUTION_ERROR = "execution_error"
    TIMEOUT = "timeout"
    ADAPTER_UNAVAILABLE = "adapter_unavailable"
    RATE_LIMIT_EXCEEDED = "rate_limit_exceeded"
    GUARDRAILS_BLOCKED = "guardrails_blocked"
    CAPABILITY_NOT_ALLOWED = "capability_not_allowed"
    UNKNOWN_ERROR = "unknown_error"
```

**验收标准**:
- [ ] 创建 `EngineErrorType` 枚举
- [ ] 更新 `EngineResponse.error_type` 类型
- [ ] Engine 中使用枚举值
- [ ] 测试用例更新

**预计工作量**: 2-3 小时

**阻塞**: ⚠️ **不阻塞 Phase 1**，但强烈建议完成（改善错误处理）

---

## Phase 0 完成标准

### 必须完成（P0）

- [ ] **Issue #11**: Engine 层统一使用 Pydantic 协议
  - [ ] MCP Frontend 使用 `execute_request()`
  - [ ] 废弃 `execute_capability()` 或标记为 deprecated
  - [ ] 所有测试通过

### 强烈建议完成（P1）

- [ ] **Issue #2**: 协议版本控制
  - [ ] 添加 `protocol_version` 字段
  - [ ] 添加版本验证逻辑

- [ ] **Issue #3**: 错误类型枚举
  - [ ] 创建 `EngineErrorType` 枚举
  - [ ] 更新 Engine 使用枚举

### 验收测试

- [ ] 运行 `tests/test_phase0_verification.py` 全部通过
- [ ] MCP Frontend 可以正常调用 Engine
- [ ] Engine 返回的响应符合 Pydantic 模型
- [ ] 类型检查通过（mypy/pyright）

---

## Phase 0 → Phase 1 过渡条件

### 必须满足（硬性条件）

1. ✅ **Issue #11 修复完成** - 统一协议真正落地
2. ✅ **所有 P0 验收测试通过**
3. ✅ **文档更新完成**

### 建议满足（软性条件）

4. ⚠️ **Issue #2 完成** - 协议版本控制（前瞻性设计）
5. ⚠️ **Issue #3 完成** - 错误类型枚举（改善错误处理）

---

## 当前状态总结

### ✅ 已完成（5/6）

1. ✅ Engine 层抽取（adapters, security, catalog, addon）
2. ✅ 统一协议定义（Pydantic 模型）
3. ✅ MCP Frontend 抽取
4. ✅ 验证测试通过
5. ✅ 外部依赖稳定（blender-mcp v1.0.0）

### ❌ 未完成（1/6）

6. ❌ **统一协议真正使用**（Issue #11）

### 阻塞状态

**Phase 0 → Phase 1 过渡**: ❌ **被 Issue #11 阻塞**

**理由**: 
- Phase 0 的核心目标是 "统一协议"
- 如果 Engine 对外仍暴露 dict 接口，协议就没有真正统一
- Phase 1 开发 Agent Core 时，会延续这个问题

---

## 下一步行动

### 立即行动（必须）

1. **修复 Issue #11**（2-4 小时）
   - 修改 MCP Frontend 使用 `execute_request()`
   - 更新测试用例
   - 验证所有测试通过

### 建议行动（可选）

2. **修复 Issue #2**（2-4 小时）
   - 添加协议版本控制
   - 为未来协议演进做准备

3. **修复 Issue #3**（2-3 小时）
   - 添加错误类型枚举
   - 改善错误处理体验

### 验收

4. **运行完整验收测试**
   - `pytest tests/test_phase0_verification.py`
   - 手动测试 MCP Frontend
   - 类型检查（mypy/pyright）

5. **更新文档**
   - 更新 `PHASE0_COMPLETE.md`
   - 更新 `README.md`

---

## 预计完成时间

- **Issue #11（必须）**: 2-4 小时
- **Issue #2（建议）**: 2-4 小时
- **Issue #3（建议）**: 2-3 小时
- **验收测试**: 1 小时
- **文档更新**: 1 小时

**总计**: 
- **最少**: 3-5 小时（仅 P0）
- **建议**: 8-12 小时（P0 + P1）

---

## 结论

**Phase 0 核心工作已完成 83%（5/6）**

**剩余 1 个 P0 Critical Issue 必须修复才能进入 Phase 1**

**建议**: 
1. 先修复 Issue #11（P0，2-4h）
2. 再修复 Issue #2 和 #3（P1，4-7h）
3. 完成验收测试和文档更新（2h）
4. **总计 8-13 小时后，Phase 0 真正夯实完成**

---

**核对完成时间**: 2026-03-09  
**下一个里程碑**: Phase 0 完成 → Phase 1 开始
