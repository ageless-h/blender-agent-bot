# Phase 0 深度复查 - 发现的问题和改进建议

## 执行时间
2026-03-08

## 复查范围
- Engine 层架构设计
- 统一协议设计
- MCP Frontend 适配
- 代码质量和可维护性
- 架构可扩展性

---

## 🔴 Critical Issues（必须修复）

### Issue #1: Engine 层未真正使用 Pydantic 协议
**问题描述**：
- 定义了 `EngineRequest/EngineResponse` Pydantic 模型
- 但 `BlenderEngine.execute_capability()` 直接接受 `dict` 参数，返回 `dict`
- 没有利用 Pydantic 的验证、序列化能力

**当前代码**：
```python
def execute_capability(
    self,
    capability: str,
    payload: dict[str, Any],
) -> dict[str, Any]:
    # 直接返回 dict，没有使用 EngineResponse
    return {
        "status": "success",
        "result": result.result,
        ...
    }
```

**影响**：
- 失去了类型安全
- 无法利用 Pydantic 的验证
- 前端需要手动构造/解析 dict

**建议修复**：
```python
def execute_capability(
    self,
    request: EngineRequest,
) -> EngineResponse:
    # 使用 Pydantic 模型
    return EngineResponse(
        status=EngineResponseStatus.SUCCESS,
        result=result.result,
        ...
    )
```

**优先级**：P0 - 必须在 Phase 1 开始前修复

---

### Issue #2: 缺少 Blender Addon 层
**问题描述**：
- Engine 层包含了 `adapters/socket.py`，但没有对应的 Blender Addon 代码
- `temp/blender-mcp` 中有 Addon 代码，但没有被抽取到 `packages/engine/`
- 无法独立运行和测试完整的 Engine → Blender 通信

**当前状态**：
```
packages/engine/blender_engine/
  ├── adapters/socket.py  ✅ 有
  └── addon/              ❌ 缺失
```

**影响**：
- 无法端到端测试
- Addon 代码仍然耦合在 blender-mcp 中
- 违反了 "Engine 层独立" 的设计目标

**建议修复**：
1. 从 `temp/blender-mcp` 抽取 Addon 代码到 `packages/engine/blender_engine/addon/`
2. 包含：
   - `__init__.py` - Addon 注册
   - `operators.py` - 自定义 Operator（支持 undo）
   - `panels.py` - N-panel UI（如果需要）
   - `timers.py` - `bpy.app.timers` 轮询逻辑
   - `socket_server.py` - Socket 服务器

**优先级**：P0 - 必须在 Phase 1 开始前修复

---

### Issue #3: 缺少 Stdio Transport
**问题描述**：
- `plan.md` 提到 "增加 stdin/stdout 传输模式"
- 当前只有 `SocketAdapter`，没有 `StdioAdapter`
- Blender UI Frontend 需要通过 stdin/stdout 与 Engine 子进程通信

**当前状态**：
```python
# packages/engine/blender_engine/adapters/
socket.py  ✅ 有
stdio.py   ❌ 缺失
```

**影响**：
- Blender UI Frontend 无法启动 Engine 子进程
- 必须依赖 Socket 通信（更复杂）

**建议修复**：
创建 `packages/engine/blender_engine/adapters/stdio.py`：
```python
class StdioAdapter:
    def execute(self, capability: str, payload: dict) -> AdapterResult:
        request = {"capability": capability, "payload": payload}
        print(json.dumps(request), flush=True)
        response = json.loads(sys.stdin.readline())
        return AdapterResult(...)
```

**优先级**：P1 - Phase 1 需要

---

## 🟡 High Priority Issues（强烈建议修复）

### Issue #4: 协议版本控制缺失
**问题描述**：
- `EngineRequest/EngineResponse` 没有版本字段
- 未来协议变更时无法向后兼容
- 无法支持多版本 Engine 共存

**建议修复**：
```python
class EngineRequest(BaseModel):
    protocol_version: str = "1.0"  # 添加版本
    request_type: EngineRequestType
    ...
```

**优先级**：P1 - 在 Phase 1 添加

---

### Issue #5: 错误处理不够细粒度
**问题描述**：
- `EngineResponseStatus` 只有 `SUCCESS/ERROR/BLOCKED` 三种状态
- `error_type` 是字符串，没有枚举
- 前端难以精确处理不同类型的错误

**当前代码**：
```python
error_type: str | None = None  # 太宽泛
```

**建议修复**：
```python
class EngineErrorType(str, Enum):
    CAPABILITY_NOT_FOUND = "capability_not_found"
    VALIDATION_ERROR = "validation_error"
    EXECUTION_ERROR = "execution_error"
    TIMEOUT = "timeout"
    ADAPTER_UNAVAILABLE = "adapter_unavailable"
    ...

class EngineResponse(BaseModel):
    error_type: EngineErrorType | None = None
```

**优先级**：P1 - Phase 1 添加

---

### Issue #6: 缺少异步支持
**问题描述**：
- `BlenderEngine.execute_capability()` 是同步的
- Web Frontend 需要异步处理
- 长时间操作会阻塞

**建议修复**：
```python
async def execute_capability_async(
    self,
    request: EngineRequest,
) -> EngineResponse:
    # 异步版本
    ...
```

**优先级**：P1 - Phase 2（Web Frontend）需要

---

### Issue #7: 缺少流式响应支持
**问题描述**：
- 长时间操作无法提供进度反馈
- 用户体验差（黑盒等待）
- Agent Core 的流式输出无法传递到 Engine

**建议修复**：
```python
class EngineStreamChunk(BaseModel):
    request_id: str
    chunk_type: Literal["progress", "log", "result"]
    data: dict[str, Any]
    done: bool = False

async def execute_capability_stream(
    self,
    request: EngineRequest,
) -> AsyncIterator[EngineStreamChunk]:
    ...
```

**优先级**：P2 - Phase 2 添加

---

## 🟢 Medium Priority Issues（建议改进）

### Issue #8: 安全模块配置过于依赖环境变量
**问题描述**：
- `BlenderEngine.__init__()` 大量使用 `os.environ.get()`
- 配置分散，难以管理
- 无法通过代码动态配置

**建议修复**：
创建 `EngineConfig` 类：
```python
@dataclass
class EngineConfig:
    adapter_mode: str = "socket"
    socket_host: str = "127.0.0.1"
    socket_port: int = 9876
    enable_script_execute: bool = False
    rate_limits: dict[str, int] = field(default_factory=dict)
    
    @classmethod
    def from_env(cls) -> EngineConfig:
        # 从环境变量加载
        ...

class BlenderEngine:
    def __init__(self, config: EngineConfig | None = None):
        config = config or EngineConfig.from_env()
        ...
```

**优先级**：P2 - Phase 1 改进

---

### Issue #9: 缺少 Engine 生命周期管理
**问题描述**：
- `BlenderEngine` 没有 `start()/stop()` 方法
- 资源（Socket 连接、Audit Logger）没有显式清理
- 可能导致资源泄漏

**建议修复**：
```python
class BlenderEngine:
    async def start(self):
        # 初始化资源
        await self._adapter.connect()
        
    async def stop(self):
        # 清理资源
        await self._adapter.disconnect()
        self._audit.close()
    
    async def __aenter__(self):
        await self.start()
        return self
    
    async def __aexit__(self, *args):
        await self.stop()
```

**优先级**：P2 - Phase 1 添加

---

### Issue #10: 测试覆盖率不足
**问题描述**：
- 只有 1 个验证测试文件
- 没有单元测试
- 没有集成测试
- 没有 Adapter 的 Mock 测试

**建议修复**：
```
tests/
├── unit/
│   ├── test_engine.py
│   ├── test_adapters.py
│   ├── test_security.py
│   └── test_catalog.py
├── integration/
│   ├── test_engine_to_blender.py
│   └── test_mcp_frontend.py
└── test_phase0_verification.py
```

**优先级**：P2 - Phase 1 添加

---

### Issue #11: 缺少日志和可观测性
**问题描述**：
- 只有基础的 `logger.info/warning`
- 没有结构化日志
- 没有 Metrics（延迟、成功率、错误率）
- 难以排查生产问题

**建议修复**：
```python
from dataclasses import dataclass
from datetime import datetime

@dataclass
class EngineMetrics:
    total_requests: int = 0
    successful_requests: int = 0
    failed_requests: int = 0
    blocked_requests: int = 0
    avg_latency_ms: float = 0.0
    
class BlenderEngine:
    def __init__(self, ...):
        self._metrics = EngineMetrics()
    
    def get_metrics(self) -> EngineMetrics:
        return self._metrics
```

**优先级**：P2 - Phase 2 添加

---

### Issue #12: MCP Frontend 仍然依赖旧的 tool_registry
**问题描述**：
- `packages/frontend-mcp/blender_mcp_frontend/tool_registry.py` 是从 blender-mcp 复制的
- 包含 1235 行的工具定义
- 应该从 Engine 的 Catalog 动态生成

**建议修复**：
```python
# MCP Frontend 应该这样获取工具定义
class MCPServer:
    def tools_list(self) -> dict[str, Any]:
        capabilities = self._engine.list_capabilities()
        tools = []
        for cap in capabilities:
            tools.append({
                "name": f"blender_{cap['name']}",
                "description": cap['description'],
                "inputSchema": self._generate_schema(cap),
            })
        return {"tools": tools}
```

**优先级**：P2 - Phase 1 重构

---

## 🔵 Low Priority Issues（可选改进）

### Issue #13: 缺少 Engine 健康检查
**问题描述**：
- 无法检查 Engine 是否正常运行
- 无法检查 Blender 连接状态
- 前端无法判断 Engine 可用性

**建议修复**：
```python
class BlenderEngine:
    def health_check(self) -> dict[str, Any]:
        return {
            "status": "healthy",
            "adapter_connected": self._adapter.is_connected(),
            "capabilities_loaded": len(self._catalog.list()),
            "uptime_seconds": time.time() - self._start_time,
        }
```

**优先级**：P3 - Phase 2 添加

---

### Issue #14: 缺少请求超时控制
**问题描述**：
- `execute_capability()` 没有超时参数
- 长时间操作可能永久阻塞
- 无法设置不同 capability 的超时时间

**建议修复**：
```python
class EngineRequest(BaseModel):
    timeout_seconds: float | None = None  # 添加超时

class BlenderEngine:
    def execute_capability(
        self,
        request: EngineRequest,
    ) -> EngineResponse:
        timeout = request.timeout_seconds or self._default_timeout
        # 使用 timeout
        ...
```

**优先级**：P3 - Phase 2 添加

---

### Issue #15: 缺少批量操作支持
**问题描述**：
- 每次只能执行一个 capability
- 批量操作需要多次往返
- 性能低下

**建议修复**：
```python
class EngineRequestType(str, Enum):
    EXECUTE_CAPABILITY = "execute_capability"
    EXECUTE_BATCH = "execute_batch"  # 新增
    ...

class EngineBatchRequest(BaseModel):
    requests: list[EngineRequest]
    stop_on_error: bool = True

class BlenderEngine:
    def execute_batch(
        self,
        batch: EngineBatchRequest,
    ) -> list[EngineResponse]:
        ...
```

**优先级**：P3 - Phase 3 添加

---

## 📊 架构改进建议

### 建议 #1: 引入 Transport 抽象层
**当前问题**：
- `SocketAdapter` 和未来的 `StdioAdapter` 混合了传输和协议
- 难以支持新的传输方式（gRPC, WebSocket）

**建议架构**：
```
Engine
  ↓ EngineRequest/EngineResponse
Transport Layer (Socket/Stdio/gRPC/WebSocket)
  ↓ 传输协议
Blender Adapter
  ↓ bpy API
Blender
```

---

### 建议 #2: 考虑引入 Event Bus
**当前问题**：
- Engine 和 Frontend 之间是请求-响应模式
- 无法支持 Blender 主动推送事件（场景变化、渲染完成）

**建议架构**：
```python
class EngineEvent(BaseModel):
    event_type: str
    data: dict[str, Any]
    timestamp: float

class BlenderEngine:
    def subscribe(self, event_type: str, callback: Callable):
        ...
    
    def emit_event(self, event: EngineEvent):
        ...
```

---

### 建议 #3: 考虑插件化架构
**当前问题**：
- 26 个 capabilities 硬编码在 Catalog 中
- 无法动态扩展新的 capabilities
- 第三方无法贡献新功能

**建议架构**：
```python
class CapabilityPlugin(Protocol):
    def get_metadata(self) -> CapabilityMeta:
        ...
    
    def execute(self, payload: dict) -> dict:
        ...

class BlenderEngine:
    def register_plugin(self, plugin: CapabilityPlugin):
        ...
```

---

## 🎯 Phase 1 优先修复清单

基于以上分析，Phase 1 开始前必须修复：

1. **Issue #1** - Engine 使用 Pydantic 协议（P0）
2. **Issue #2** - 抽取 Blender Addon 层（P0）
3. **Issue #3** - 实现 Stdio Transport（P1）
4. **Issue #4** - 添加协议版本控制（P1）
5. **Issue #5** - 细化错误类型枚举（P1）
6. **Issue #8** - 创建 EngineConfig 类（P2）
7. **Issue #9** - 添加生命周期管理（P2）
8. **Issue #10** - 补充单元测试（P2）

预计工作量：3-5 天

---

## 总结

Phase 0 重构成功完成了核心目标：
- ✅ Engine 层独立
- ✅ 统一协议定义
- ✅ MCP Frontend 适配
- ✅ 验证测试通过

但存在以下关键问题需要在 Phase 1 前修复：
- 🔴 Engine 未真正使用 Pydantic 协议
- 🔴 缺少 Blender Addon 层
- 🔴 缺少 Stdio Transport

建议在开始 Phase 1（Agent Core）之前，先用 3-5 天时间修复 P0/P1 问题，确保 Engine 层的基础架构稳固。
