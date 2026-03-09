# API 参考文档

> BlenderAgentBot Agent Core API 完整参考

## 目录

- [核心模块](#核心模块)
- [LLM 适配器](#llm-适配器)
- [任务规划器](#任务规划器)
- [安全体系](#安全体系)
- [技能引擎](#技能引擎)
- [会话管理](#会话管理)
- [工具路由](#工具路由)
- [视觉验证](#视觉验证)

---

## 核心模块

### AgentCore

主协调类，管理所有子系统。

#### 初始化

```python
from blender_agent_core import AgentCore
from blender_agent_core.llm import OpenAIAdapter

agent = AgentCore(
    llm_adapter: LLMAdapter,           # LLM 适配器
    session_manager: SessionManager,   # 会话管理器（可选）
    tool_router: ToolRouter,           # 工具路由器（可选）
    security_gateway: SecurityGateway, # 安全网关（可选）
    skill_store: SkillStore            # 技能存储（可选）
)
```

#### 方法

##### `process(request: str, session_id: str = None) -> AgentResponse`

处理用户请求。

**参数**:
- `request` (str): 用户指令
- `session_id` (str, optional): 会话 ID

**返回**: `AgentResponse` 对象

**示例**:
```python
response = await agent.process("创建一个立方体")
print(response.message)
```

##### `create_session() -> str`

创建新会话。

**返回**: 会话 ID (str)

**示例**:
```python
session_id = agent.create_session()
```

##### `destroy_session(session_id: str) -> None`

销毁会话。

**参数**:
- `session_id` (str): 会话 ID

---

## LLM 适配器

### LLMAdapter (抽象基类)

所有 LLM 适配器的基类。

#### 方法

##### `generate(messages: list, tools: list = None, **kwargs) -> LLMResponse`

生成 LLM 响应。

**参数**:
- `messages` (list): 消息列表
  ```python
  [
      {"role": "system", "content": "You are..."},
      {"role": "user", "content": "Create a cube"}
  ]
  ```
- `tools` (list, optional): 可用工具列表
- `**kwargs`: 额外参数（temperature, max_tokens 等）

**返回**: `LLMResponse` 对象

**示例**:
```python
response = await llm.generate(
    messages=[{"role": "user", "content": "Hello"}],
    temperature=0.7
)
```

##### `stream(messages: list, tools: list = None, **kwargs) -> AsyncIterator[StreamChunk]`

流式生成响应。

**参数**: 同 `generate()`

**返回**: 异步迭代器，产生 `StreamChunk` 对象

**示例**:
```python
async for chunk in llm.stream(messages):
    print(chunk.content, end="")
```

##### `get_capabilities() -> ModelCapabilities`

获取模型能力。

**返回**: `ModelCapabilities` 对象

---

### OpenAIAdapter

OpenAI 兼容的适配器（支持 GPT-4, GPT-3.5, Ollama, vLLM 等）。

#### 初始化

```python
from blender_agent_core.llm import OpenAIAdapter

llm = OpenAIAdapter(
    api_key: str = None,        # API Key（默认从环境变量读取）
    model: str = "gpt-4",       # 模型名称
    base_url: str = None,       # 自定义 API 端点
    organization: str = None,   # 组织 ID
    timeout: float = 60.0       # 超时时间（秒）
)
```

#### 示例

```python
# 使用 OpenAI
llm = OpenAIAdapter(api_key="sk-...", model="gpt-4")

# 使用 Ollama
llm = OpenAIAdapter(
    base_url="http://localhost:11434/v1",
    model="llama3.2"
)

# 使用 vLLM
llm = OpenAIAdapter(
    base_url="http://your-server:8000/v1",
    model="meta-llama/Llama-3.2-8B"
)
```

---

### AnthropicAdapter

Anthropic Claude 适配器。

#### 初始化

```python
from blender_agent_core.llm import AnthropicAdapter

llm = AnthropicAdapter(
    api_key: str = None,              # API Key
    model: str = "claude-3-5-sonnet-20241022",
    timeout: float = 60.0
)
```

#### 支持的模型

- `claude-3-5-sonnet-20241022` (推荐)
- `claude-3-5-haiku-20241022`
- `claude-3-opus-20240229`

#### 示例

```python
llm = AnthropicAdapter(
    api_key="sk-ant-...",
    model="claude-3-5-sonnet-20241022"
)

response = await llm.generate(
    messages=[{"role": "user", "content": "Hello"}]
)
```

---

### AzureOpenAIAdapter

Azure OpenAI 适配器。

#### 初始化

```python
from blender_agent_core.llm import AzureOpenAIAdapter

llm = AzureOpenAIAdapter(
    api_key: str = None,           # Azure API Key
    endpoint: str = None,          # Azure 端点
    deployment_name: str,          # 部署名称
    api_version: str = "2024-02-15-preview"
)
```

#### 示例

```python
llm = AzureOpenAIAdapter(
    api_key="your-azure-key",
    endpoint="https://your-resource.openai.azure.com",
    deployment_name="gpt-4-deployment"
)
```

---

### FallbackAdapter

为不支持 tool calling 的模型提供降级方案。

#### 初始化

```python
from blender_agent_core.llm import FallbackAdapter

llm = FallbackAdapter(
    base_adapter: LLMAdapter,  # 底层适配器
    tool_format: str = "json"  # 工具格式（json/xml）
)
```

#### 工作原理

将工具定义注入到 system prompt，让模型以 JSON 格式返回工具调用。

#### 示例

```python
# 本地模型不支持 tool calling
base_llm = OpenAIAdapter(
    base_url="http://localhost:11434/v1",
    model="llama3.2"
)

# 使用 Fallback 适配器
llm = FallbackAdapter(base_adapter=base_llm)

# 现在可以使用工具调用
response = await llm.generate(
    messages=[{"role": "user", "content": "Create a cube"}],
    tools=[{"name": "create_primitive", "description": "..."}]
)
```

---

### MockAdapter

测试用模拟适配器。

#### 初始化

```python
from blender_agent_core.llm import MockAdapter

llm = MockAdapter(
    response_text: str = "Mock response",
    tool_calls: list = None,
    delay: float = 0.0  # 模拟延迟
)
```

#### 示例

```python
llm = MockAdapter(
    response_text="Created a cube",
    tool_calls=[
        {
            "id": "call_1",
            "function": {
                "name": "create_primitive",
                "arguments": '{"type": "CUBE"}'
            }
        }
    ]
)
```

---

## 任务规划器

### TaskPlanner

将用户指令拆解为工具调用序列。

#### 初始化

```python
from blender_agent_core.planner import TaskPlanner

planner = TaskPlanner(
    llm_adapter: LLMAdapter,
    tool_executor: Callable,  # 工具执行函数
    max_steps: int = 10,      # 最大步骤数
    retry_limit: int = 3      # 重试次数
)
```

#### 方法

##### `create_plan(user_request: str, available_tools: list) -> TaskPlan`

创建执行计划。

**参数**:
- `user_request` (str): 用户请求
- `available_tools` (list): 可用工具列表

**返回**: `TaskPlan` 对象

**示例**:
```python
plan = await planner.create_plan(
    user_request="创建一个红色的立方体",
    available_tools=[
        {
            "name": "create_primitive",
            "description": "Create a primitive object",
            "parameters": {...}
        },
        {
            "name": "set_material",
            "description": "Set object material",
            "parameters": {...}
        }
    ]
)
```

##### `execute_plan(plan: TaskPlan) -> TaskPlan`

执行计划。

**参数**:
- `plan` (TaskPlan): 任务计划

**返回**: 更新后的 `TaskPlan` 对象

**示例**:
```python
completed_plan = await planner.execute_plan(plan)
print(f"Status: {completed_plan.status.value}")
```

---

### TaskPlan

任务计划数据结构。

#### 属性

```python
@dataclass
class TaskPlan:
    request: str                    # 用户请求
    steps: list[TaskStep]           # 执行步骤
    status: PlanStatus              # 状态（pending/in_progress/completed/failed）
    current_step: int               # 当前步骤索引
    error: str | None               # 错误信息
    created_at: datetime
    updated_at: datetime
```

#### TaskStep

```python
@dataclass
class TaskStep:
    description: str                # 步骤描述
    tool_calls: list[ToolCall]      # 工具调用列表
    status: StepStatus              # 状态
    result: dict | None             # 执行结果
    error: str | None               # 错误信息
```

---

## 安全体系

### SecurityGateway

安全网关，验证操作和代码。

#### 初始化

```python
from blender_agent_core.safety import SecurityGateway, SecurityPolicy

policy = SecurityPolicy(
    allow_high_risk: bool = False,
    allow_critical: bool = False,
    enable_ast_analysis: bool = True,
    auto_execute_threshold: SecurityLevel = SecurityLevel.LOW
)

gateway = SecurityGateway(
    policy: SecurityPolicy,
    confirmation_manager: ConfirmationManager = None
)
```

#### 方法

##### `validate_operation(operation_name: str, arguments: dict) -> tuple[bool, str]`

验证操作是否允许。

**参数**:
- `operation_name` (str): 操作名称
- `arguments` (dict): 操作参数

**返回**: `(is_allowed, reason)` 元组

**示例**:
```python
is_allowed, reason = await gateway.validate_operation(
    "delete_all_objects",
    {}
)

if not is_allowed:
    print(f"操作被拒绝: {reason}")
```

##### `validate_code(code: str) -> tuple[bool, list[SecurityViolation]]`

验证 Python 代码安全性。

**参数**:
- `code` (str): Python 代码

**返回**: `(is_safe, violations)` 元组

**示例**:
```python
code = """
import os
os.system("rm -rf /")
"""

is_safe, violations = gateway.validate_code(code)

if not is_safe:
    for v in violations:
        print(f"{v.severity.value}: {v.description}")
```

---

### SecurityLevel

安全等级枚举。

```python
class SecurityLevel(Enum):
    SAFE = "safe"           # 完全安全（只读操作）
    LOW = "low"             # 低风险（可逆操作）
    MEDIUM = "medium"       # 中风险（部分可逆）
    HIGH = "high"           # 高风险（不可逆）
    CRITICAL = "critical"   # 关键操作（系统级）
```

#### 预定义分类

```python
# SAFE
get_objects, get_scene_info, list_collections, get_object_properties

# LOW
create_primitive, set_location, set_rotation, set_scale, set_color

# MEDIUM
delete_object, apply_modifier, set_material, join_objects

# HIGH
delete_all_objects, clear_scene, execute_script

# CRITICAL
install_addon, modify_preferences, file_operations
```

---

### ASTAnalyzer

Python 代码静态分析器。

#### 方法

##### `analyze(code: str) -> list[SecurityViolation]`

分析代码并返回安全问题。

**参数**:
- `code` (str): Python 代码

**返回**: `SecurityViolation` 列表

**示例**:
```python
from blender_agent_core.safety import ASTAnalyzer

analyzer = ASTAnalyzer()
violations = analyzer.analyze("eval('malicious code')")

for v in violations:
    print(f"{v.violation_type}: {v.description}")
```

#### 检测规则

- **黑名单函数**: `eval`, `exec`, `compile`, `__import__`
- **黑名单模块**: `os`, `sys`, `subprocess`, `shutil`
- **文件操作**: `open`, `file`
- **网络操作**: `socket`, `urllib`, `requests`
- **动态代码**: `eval`, `exec`

---

## 技能引擎

### SkillStore

技能存储和搜索。

#### 初始化

```python
from pathlib import Path
from blender_agent_core.skills import SkillStore

store = SkillStore(
    skills_dir: Path,           # 技能目录
    auto_load: bool = True      # 自动加载
)
```

#### 方法

##### `load_all_skills() -> None`

加载所有技能。

**示例**:
```python
store = SkillStore(skills_dir=Path("skills/builtin"))
store.load_all_skills()
print(f"Loaded {len(store.skills)} skills")
```

##### `load_skill(skill_path: Path) -> SkillCapsule`

加载单个技能。

**参数**:
- `skill_path` (Path): 技能文件路径

**返回**: `SkillCapsule` 对象

##### `get_skill(name: str) -> SkillCapsule | None`

按名称获取技能。

**参数**:
- `name` (str): 技能名称

**返回**: `SkillCapsule` 或 None

**示例**:
```python
skill = store.get_skill("create_cube")
if skill:
    print(skill.metadata.description)
```

##### `search_skills(query: str, category: str = None, limit: int = 5) -> list[tuple[SkillCapsule, float]]`

搜索技能（模糊匹配）。

**参数**:
- `query` (str): 搜索查询
- `category` (str, optional): 分类过滤
- `limit` (int): 返回数量

**返回**: `(skill, score)` 元组列表

**示例**:
```python
results = store.search_skills("create cube", limit=3)
for skill, score in results:
    print(f"{skill.metadata.name}: {score:.2f}")
```

---

### SkillExecutor

技能执行器。

#### 初始化

```python
from blender_agent_core.skills import SkillExecutor

executor = SkillExecutor(
    tool_executor: Callable  # 工具执行函数
)
```

#### 方法

##### `execute_skill(skill: SkillCapsule, parameters: dict) -> dict`

执行技能。

**参数**:
- `skill` (SkillCapsule): 技能对象
- `parameters` (dict): 参数字典

**返回**: 执行结果字典

**示例**:
```python
skill = store.get_skill("create_cube")

result = await executor.execute_skill(
    skill,
    parameters={
        "name": "MyCube",
        "location": {"x": 2, "y": 0, "z": 1}
    }
)

print(result)
```

---

### SkillCapsule

技能封装数据结构。

#### 结构

```python
@dataclass
class SkillCapsule:
    metadata: SkillMetadata
    steps: list[SkillStep]

@dataclass
class SkillMetadata:
    name: str
    version: str
    description: str
    category: str
    author: str | None
    tags: list[str]
    parameters: list[SkillParameter]
    examples: list[SkillExample]
    dependencies: list[str]

@dataclass
class SkillStep:
    tool_name: str
    arguments: dict
    description: str | None
```

---

## 会话管理

### SessionManager

多会话隔离和历史管理。

#### 初始化

```python
from blender_agent_core.session import SessionManager

manager = SessionManager(
    max_history: int = 100  # 最大历史记录数
)
```

#### 方法

##### `create_session() -> str`

创建新会话。

**返回**: 会话 ID

##### `get_session(session_id: str) -> Session | None`

获取会话。

**参数**:
- `session_id` (str): 会话 ID

**返回**: `Session` 对象或 None

##### `add_message(session_id: str, role: str, content: str) -> None`

添加消息到会话历史。

**参数**:
- `session_id` (str): 会话 ID
- `role` (str): 角色（user/assistant/system）
- `content` (str): 消息内容

##### `get_history(session_id: str, limit: int = None) -> list[dict]`

获取会话历史。

**参数**:
- `session_id` (str): 会话 ID
- `limit` (int, optional): 返回数量

**返回**: 消息列表

**示例**:
```python
manager = SessionManager()
session_id = manager.create_session()

manager.add_message(session_id, "user", "Create a cube")
manager.add_message(session_id, "assistant", "Created cube")

history = manager.get_history(session_id)
for msg in history:
    print(f"{msg['role']}: {msg['content']}")
```

---

## 工具路由

### ToolRouter

Engine 调用映射。

#### 初始化

```python
from blender_agent_core.router import ToolRouter

router = ToolRouter(
    engine_client: EngineClient  # Engine 客户端
)
```

#### 方法

##### `route(tool_name: str, arguments: dict) -> dict`

路由工具调用到 Engine。

**参数**:
- `tool_name` (str): 工具名称
- `arguments` (dict): 工具参数

**返回**: 执行结果

**示例**:
```python
result = await router.route(
    "create_primitive",
    {"type": "CUBE", "name": "MyCube"}
)
```

##### `get_available_tools() -> list[dict]`

获取可用工具列表。

**返回**: 工具定义列表

---

## 视觉验证

### VisualVerifier

视觉验证接口。

#### 方法

##### `capture_screenshot() -> Screenshot`

捕获当前视口截图。

**返回**: `Screenshot` 对象

##### `compare_screenshots(before: Screenshot, after: Screenshot) -> VisualComparison`

对比两张截图。

**参数**:
- `before` (Screenshot): 操作前截图
- `after` (Screenshot): 操作后截图

**返回**: `VisualComparison` 对象

#### 数据结构

```python
@dataclass
class Screenshot:
    image_data: bytes       # 图片数据（PNG）
    width: int
    height: int
    timestamp: datetime
    metadata: dict

@dataclass
class VisualComparison:
    similarity: float       # 相似度（0-1）
    differences: list[dict] # 差异区域
    has_changes: bool
```

---

## 数据类型

### LLMResponse

```python
@dataclass
class LLMResponse:
    content: str                    # 响应内容
    tool_calls: list[ToolCall]      # 工具调用列表
    finish_reason: str              # 结束原因
    usage: dict                     # Token 使用情况
```

### ToolCall

```python
@dataclass
class ToolCall:
    id: str
    function: FunctionCall

@dataclass
class FunctionCall:
    name: str
    arguments: str  # JSON 字符串
```

### ModelCapabilities

```python
@dataclass
class ModelCapabilities:
    supports_tool_calling: bool
    supports_vision: bool
    supports_streaming: bool
    context_length: int
    max_output_tokens: int
```

---

## 异常

### AgentError

基础异常类。

```python
class AgentError(Exception):
    pass
```

### LLMError

LLM 相关错误。

```python
class LLMError(AgentError):
    pass
```

### SecurityError

安全相关错误。

```python
class SecurityError(AgentError):
    pass
```

### SkillError

技能相关错误。

```python
class SkillError(AgentError):
    pass
```

---

## 完整示例

### 端到端工作流

```python
import asyncio
from pathlib import Path
from blender_agent_core import AgentCore
from blender_agent_core.llm import OpenAIAdapter
from blender_agent_core.planner import TaskPlanner
from blender_agent_core.safety import SecurityGateway, SecurityPolicy
from blender_agent_core.skills import SkillStore, SkillExecutor
from blender_agent_core.session import SessionManager
from blender_agent_core.router import ToolRouter

async def main():
    # 1. 初始化 LLM
    llm = OpenAIAdapter(model="gpt-4")
    
    # 2. 初始化安全网关
    policy = SecurityPolicy(
        allow_high_risk=False,
        enable_ast_analysis=True
    )
    gateway = SecurityGateway(policy=policy)
    
    # 3. 初始化技能系统
    store = SkillStore(skills_dir=Path("skills/builtin"))
    store.load_all_skills()
    
    # 4. 初始化工具执行器
    async def tool_executor(tool_name: str, args: dict) -> dict:
        # 安全检查
        is_allowed, reason = await gateway.validate_operation(tool_name, args)
        if not is_allowed:
            raise SecurityError(reason)
        
        # 执行工具（这里应该调用 Engine）
        print(f"Executing: {tool_name}({args})")
        return {"success": True}
    
    executor = SkillExecutor(tool_executor=tool_executor)
    
    # 5. 初始化规划器
    planner = TaskPlanner(
        llm_adapter=llm,
        tool_executor=tool_executor
    )
    
    # 6. 初始化会话管理
    session_manager = SessionManager()
    session_id = session_manager.create_session()
    
    # 7. 处理用户请求
    user_request = "创建一个红色的立方体"
    
    # 搜索相关技能
    skills = store.search_skills(user_request, limit=3)
    if skills:
        skill, score = skills[0]
        if score > 0.7:
            # 使用技能
            result = await executor.execute_skill(
                skill,
                parameters={"color": {"r": 1.0, "g": 0.0, "b": 0.0}}
            )
            print(f"Skill result: {result}")
        else:
            # 使用规划器
            plan = await planner.create_plan(
                user_request,
                available_tools=[...]
            )
            completed = await planner.execute_plan(plan)
            print(f"Plan status: {completed.status.value}")
    
    # 8. 保存历史
    session_manager.add_message(session_id, "user", user_request)
    session_manager.add_message(session_id, "assistant", "已创建红色立方体")

asyncio.run(main())
```

---

## 环境变量

```bash
# OpenAI
OPENAI_API_KEY=sk-...

# Anthropic
ANTHROPIC_API_KEY=sk-ant-...

# Azure OpenAI
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_DEPLOYMENT=your-deployment

# 日志级别
LOG_LEVEL=INFO  # DEBUG, INFO, WARNING, ERROR
```

---

## 更多资源

- 📖 [快速开始](QUICKSTART.md)
- 🎓 [技能开发指南](SKILL_DEVELOPMENT.md)
- 🔧 [架构设计](planning/plan.md)
- 💡 [示例代码](../examples/)

---

**版本**: 1.0.0  
**更新日期**: 2026-03-09
