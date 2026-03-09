# GitHub Issues to Create

Based on PHASE0_ISSUES.md, here are the remaining issues that need to be created on GitHub.

**Note**: P0 issues (#1, #2, #3) have been fixed in commit `cffd202`.

---

## P1 Issues (High Priority - Phase 1)

### Issue #4: Add protocol version control to EngineRequest/EngineResponse

**Labels**: `enhancement`, `phase-1`, `protocol`

**Title**: [P1] Add protocol version control to EngineRequest/EngineResponse

**Body**:
```markdown
## Problem
Currently `EngineRequest/EngineResponse` models lack version fields, making it impossible to:
- Support backward compatibility when protocol changes
- Allow multiple Engine versions to coexist
- Gracefully handle protocol mismatches

## Proposed Solution
Add `protocol_version` field to both models:

```python
class EngineRequest(BaseModel):
    protocol_version: str = "1.0"
    request_type: EngineRequestType
    capability: str | None
    payload: dict[str, Any]
    request_id: str | None

class EngineResponse(BaseModel):
    protocol_version: str = "1.0"
    status: EngineResponseStatus
    request_id: str | None
    ...
```

## Implementation Notes
- Use semantic versioning (MAJOR.MINOR.PATCH)
- Add version validation in Engine
- Document version compatibility matrix

## Priority
P1 - Should be added in Phase 1

## Related
- PHASE0_ISSUES.md Issue #4
- `shared/protocol/engine_protocol.py`
```

---

### Issue #5: Create EngineErrorType enum for fine-grained error handling

**Labels**: `enhancement`, `phase-1`, `protocol`

**Title**: [P1] Create EngineErrorType enum for fine-grained error handling

**Body**:
```markdown
## Problem
Currently `error_type` in `EngineResponse` is a plain string:
```python
error_type: str | None = None  # Too broad
```

This makes it difficult for frontends to:
- Handle specific error types programmatically
- Provide appropriate user feedback
- Implement retry logic for transient errors

## Proposed Solution
Create an `EngineErrorType` enum:

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

class EngineResponse(BaseModel):
    error_type: EngineErrorType | None = None
    ...
```

## Benefits
- Type safety for error handling
- IDE autocomplete support
- Clear documentation of all possible errors
- Easier to maintain error handling logic

## Priority
P1 - Should be added in Phase 1

## Related
- PHASE0_ISSUES.md Issue #5
- `shared/protocol/engine_protocol.py`
```

---

### Issue #6: Add async support for Web Frontend

**Labels**: `enhancement`, `phase-2`, `async`

**Title**: [P1] Add async support for Web Frontend

**Body**:
```markdown
## Problem
`BlenderEngine.execute_capability()` is synchronous, which:
- Blocks the event loop in async contexts
- Makes Web Frontend implementation difficult
- Prevents concurrent request handling
- Causes poor UX for long-running operations

## Proposed Solution
Add async version of execute methods:

```python
class BlenderEngine:
    async def execute_request_async(
        self,
        request: EngineRequest,
    ) -> EngineResponse:
        """Async version for Web Frontend."""
        ...
    
    async def execute_capability_async(
        self,
        capability: str,
        payload: dict[str, Any],
    ) -> dict[str, Any]:
        """Async version for backward compatibility."""
        request = EngineRequest(...)
        response = await self.execute_request_async(request)
        return response.model_dump(exclude_none=True)
```

## Implementation Notes
- Keep sync methods for backward compatibility
- Adapters should support both sync and async
- Use `asyncio.to_thread()` for blocking operations

## Priority
P1 - Required for Phase 2 (Web Frontend)

## Related
- PHASE0_ISSUES.md Issue #6
- Phase 2 Web Frontend implementation
```

---

### Issue #7: Add streaming response support for long operations

**Labels**: `enhancement`, `phase-2`, `streaming`

**Title**: [P1] Add streaming response support for long operations

**Body**:
```markdown
## Problem
Long-running operations provide no progress feedback:
- Users see a black box while waiting
- No way to cancel operations
- Agent Core's streaming output can't reach Engine
- Poor user experience

## Proposed Solution
Add streaming support:

```python
class EngineStreamChunk(BaseModel):
    request_id: str
    chunk_type: Literal["progress", "log", "result"]
    data: dict[str, Any]
    done: bool = False

class BlenderEngine:
    async def execute_request_stream(
        self,
        request: EngineRequest,
    ) -> AsyncIterator[EngineStreamChunk]:
        """Stream progress updates and final result."""
        yield EngineStreamChunk(
            request_id=request.request_id,
            chunk_type="progress",
            data={"percent": 50, "message": "Processing..."},
        )
        ...
        yield EngineStreamChunk(
            request_id=request.request_id,
            chunk_type="result",
            data=result,
            done=True,
        )
```

## Use Cases
- Rendering animations (progress bar)
- Batch operations (item count)
- Script execution (console output)
- Agent reasoning (thinking process)

## Priority
P1 - Required for Phase 2

## Related
- PHASE0_ISSUES.md Issue #7
- Agent Core streaming integration
```

---

## P2 Issues (Medium Priority - Phase 1/2)

### Issue #8: Create EngineConfig dataclass to replace scattered env vars

**Labels**: `enhancement`, `phase-1`, `refactor`

**Title**: [P2] Create EngineConfig dataclass to replace scattered env vars

**Body**:
```markdown
## Problem
`BlenderEngine.__init__()` uses many `os.environ.get()` calls:
- Configuration is scattered and hard to manage
- No type safety for config values
- Difficult to test with different configs
- Can't configure dynamically via code

## Proposed Solution
Create `EngineConfig` dataclass:

```python
from dataclasses import dataclass, field

@dataclass
class EngineConfig:
    adapter_mode: str = "socket"
    socket_host: str = "127.0.0.1"
    socket_port: int = 9876
    socket_timeout: float = 30.0
    max_retries: int = 3
    
    enable_script_execute: bool = False
    rate_limits: dict[str, int] = field(default_factory=dict)
    rate_window_seconds: float = 60.0
    
    audit_log_path: str | None = None
    
    @classmethod
    def from_env(cls) -> EngineConfig:
        """Load configuration from environment variables."""
        return cls(
            adapter_mode=os.environ.get("ENGINE_ADAPTER", "socket"),
            socket_host=os.environ.get("ENGINE_SOCKET_HOST", "127.0.0.1"),
            socket_port=int(os.environ.get("ENGINE_SOCKET_PORT", "9876")),
            ...
        )

class BlenderEngine:
    def __init__(
        self,
        config: EngineConfig | None = None,
        adapter: BlenderAdapter | None = None,
        ...
    ):
        self._config = config or EngineConfig.from_env()
        ...
```

## Benefits
- Centralized configuration
- Type safety
- Easy testing with custom configs
- Better documentation

## Priority
P2 - Should be improved in Phase 1

## Related
- PHASE0_ISSUES.md Issue #8
- `packages/engine/blender_engine/engine.py`
```

---

### Issue #9: Add Engine lifecycle management (start/stop methods)

**Labels**: `enhancement`, `phase-1`, `lifecycle`

**Title**: [P2] Add Engine lifecycle management (start/stop methods)

**Body**:
```markdown
## Problem
`BlenderEngine` lacks explicit lifecycle management:
- No `start()/stop()` methods
- Resources (Socket connections, Audit Logger) not explicitly cleaned up
- Potential resource leaks
- No context manager support

## Proposed Solution
Add lifecycle methods:

```python
class BlenderEngine:
    async def start(self):
        """Initialize resources."""
        if hasattr(self._adapter, 'connect'):
            await self._adapter.connect()
        logger.info("Engine started")
    
    async def stop(self):
        """Clean up resources."""
        if hasattr(self._adapter, 'disconnect'):
            await self._adapter.disconnect()
        if hasattr(self._audit, 'close'):
            self._audit.close()
        logger.info("Engine stopped")
    
    async def __aenter__(self):
        await self.start()
        return self
    
    async def __aexit__(self, *args):
        await self.stop()

# Usage
async with BlenderEngine() as engine:
    response = await engine.execute_request_async(request)
```

## Benefits
- Explicit resource management
- Prevents resource leaks
- Better testability
- Pythonic context manager pattern

## Priority
P2 - Should be added in Phase 1

## Related
- PHASE0_ISSUES.md Issue #9
- `packages/engine/blender_engine/engine.py`
```

---

### Issue #10: Add comprehensive unit and integration tests

**Labels**: `testing`, `phase-1`

**Title**: [P2] Add comprehensive unit and integration tests

**Body**:
```markdown
## Problem
Current test coverage is minimal:
- Only 1 verification test file (`test_phase0_verification.py`)
- No unit tests for individual components
- No integration tests for end-to-end flows
- No adapter mock tests

## Proposed Test Structure
```
tests/
├── unit/
│   ├── test_engine.py              # Engine core logic
│   ├── test_adapters.py            # Adapter implementations
│   ├── test_security_allowlist.py  # Allowlist logic
│   ├── test_security_guardrails.py # Guardrails logic
│   ├── test_security_rate_limit.py # Rate limiter
│   ├── test_catalog.py             # Capability catalog
│   └── test_protocol.py            # Pydantic models
├── integration/
│   ├── test_engine_to_blender.py   # Engine → Blender Addon
│   ├── test_mcp_frontend.py        # MCP Frontend → Engine
│   └── test_security_pipeline.py   # Full security chain
└── test_phase0_verification.py     # Existing verification
```

## Test Requirements
- Use `pytest` and `pytest-asyncio`
- Mock Blender `bpy` module for unit tests
- Use `MockAdapter` for Engine tests
- Aim for >80% code coverage
- Add CI/CD pipeline (GitHub Actions)

## Priority
P2 - Should be added in Phase 1

## Related
- PHASE0_ISSUES.md Issue #10
- `tests/` directory
```

---

### Issue #11: Add structured logging and metrics

**Labels**: `enhancement`, `phase-2`, `observability`

**Title**: [P2] Add structured logging and metrics

**Body**:
```markdown
## Problem
Current logging is basic:
- Only simple `logger.info/warning` calls
- No structured logging (JSON format)
- No metrics (latency, success rate, error rate)
- Difficult to troubleshoot production issues

## Proposed Solution
Add metrics tracking:

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
    last_request_time: datetime | None = None
    
    def record_request(self, status: EngineResponseStatus, latency_ms: float):
        self.total_requests += 1
        if status == EngineResponseStatus.SUCCESS:
            self.successful_requests += 1
        elif status == EngineResponseStatus.ERROR:
            self.failed_requests += 1
        elif status == EngineResponseStatus.BLOCKED:
            self.blocked_requests += 1
        
        # Update average latency
        self.avg_latency_ms = (
            (self.avg_latency_ms * (self.total_requests - 1) + latency_ms)
            / self.total_requests
        )
        self.last_request_time = datetime.now()

class BlenderEngine:
    def __init__(self, ...):
        self._metrics = EngineMetrics()
    
    def get_metrics(self) -> EngineMetrics:
        return self._metrics
    
    def execute_request(self, request: EngineRequest) -> EngineResponse:
        start = time.perf_counter()
        response = ...
        latency_ms = (time.perf_counter() - start) * 1000
        self._metrics.record_request(response.status, latency_ms)
        return response
```

Add structured logging:
```python
import structlog

logger = structlog.get_logger()

logger.info(
    "capability_executed",
    capability=capability,
    status=response.status.value,
    latency_ms=latency_ms,
    request_id=request.request_id,
)
```

## Priority
P2 - Should be added in Phase 2

## Related
- PHASE0_ISSUES.md Issue #11
- Production monitoring requirements
```

---

### Issue #12: Generate MCP tool definitions dynamically from Engine Catalog

**Labels**: `enhancement`, `phase-1`, `refactor`

**Title**: [P2] Generate MCP tool definitions dynamically from Engine Catalog

**Body**:
```markdown
## Problem
`packages/frontend-mcp/blender_mcp_frontend/tool_registry.py`:
- Contains 1235 lines of hardcoded tool definitions
- Copied from blender-mcp
- Duplicates information already in Engine's Catalog
- Difficult to maintain sync between Engine and MCP Frontend

## Proposed Solution
Generate MCP tools dynamically from Engine Catalog:

```python
class MCPServer:
    def tools_list(self) -> dict[str, Any]:
        capabilities = self._engine.list_capabilities()
        
        tools = []
        for cap in capabilities:
            tool = {
                "name": f"blender_{cap['name']}",
                "description": cap['description'],
                "inputSchema": self._generate_schema(cap),
            }
            tools.append(tool)
        
        return {"tools": tools}
    
    def _generate_schema(self, capability: dict) -> dict:
        """Generate JSON Schema from capability definition."""
        # Convert capability schema to MCP inputSchema format
        ...
```

## Benefits
- Single source of truth (Engine Catalog)
- Automatic sync between Engine and MCP Frontend
- Easier to add new capabilities
- Reduced code duplication

## Migration Plan
1. Add schema generation logic to MCPServer
2. Verify generated schemas match existing ones
3. Remove hardcoded tool_registry.py
4. Update tests

## Priority
P2 - Should be refactored in Phase 1

## Related
- PHASE0_ISSUES.md Issue #12
- `packages/frontend-mcp/blender_mcp_frontend/tool_registry.py`
- `packages/engine/blender_engine/catalog/catalog.py`
```

---

## How to Create These Issues

### Option 1: Using GitHub CLI (gh)
```bash
# Install gh CLI first: https://cli.github.com/

# Then run:
cd /path/to/BlenderAgentBot
gh issue create --title "[P1] Add protocol version control" --body-file issue_body.md --label "enhancement,phase-1"
```

### Option 2: Using GitHub Web UI
1. Go to https://github.com/ageless-h/blender-agent-bot/issues/new
2. Copy the title and body from above
3. Add the specified labels
4. Click "Submit new issue"

### Option 3: Using GitHub API
```bash
curl -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  https://api.github.com/repos/ageless-h/blender-agent-bot/issues \
  -d '{"title":"[P1] Add protocol version control","body":"...","labels":["enhancement","phase-1"]}'
```

---

## Summary

**P0 Issues (Fixed)**: 3
- ✅ Issue #1: Pydantic protocol integration
- ✅ Issue #2: Blender Addon extraction
- ✅ Issue #3: Stdio Transport adapter

**P1 Issues (To Create)**: 4
- Issue #4: Protocol version control
- Issue #5: EngineErrorType enum
- Issue #6: Async support
- Issue #7: Streaming support

**P2 Issues (To Create)**: 5
- Issue #8: EngineConfig dataclass
- Issue #9: Lifecycle management
- Issue #10: Comprehensive tests
- Issue #11: Structured logging and metrics
- Issue #12: Dynamic MCP tool generation

**Total**: 12 issues (3 fixed, 9 to create)
