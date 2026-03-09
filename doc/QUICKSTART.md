# 快速开始指南

> 5 分钟上手 BlenderAgentBot

## 前置要求

- **Python 3.10+**
- **Blender 4.2+** (推荐 5.0+)
- **OpenAI API Key** 或 **Anthropic API Key** (可选，可使用 Mock 模式)

## 安装

### 1. 克隆项目

```bash
git clone https://github.com/your-org/BlenderAgentBot.git
cd BlenderAgentBot
```

### 2. 安装 Agent Core

```bash
cd packages/agent-core
pip install -e ".[dev]"
```

### 3. 安装 Blender Addon (可选)

```bash
# 方法 1: 符号链接
ln -s $(pwd)/packages/frontend-blender ~/.config/blender/5.0/scripts/addons/blenderagent

# 方法 2: 复制
cp -r packages/frontend-blender ~/.config/blender/5.0/scripts/addons/blenderagent

# Windows 用户
mklink /D "%APPDATA%\Blender Foundation\Blender\5.0\scripts\addons\blenderagent" "packages\frontend-blender"
```

## 快速测试

### 测试 1: 运行集成示例

```bash
cd BlenderAgentBot
python examples/integration_test.py
```

**预期输出**:
```
=== Example: Basic Workflow ===
Created plan with 1 steps
  Executing: create_primitive({'type': 'CUBE'})
Plan status: completed

=== Example: With Security ===
✓ ALLOWED: create_primitive
✗ DENIED: delete_all_objects
  Reason: User denied operation 'delete_all_objects'
✗ DENIED: execute_script
  Reason: Operation 'execute_script' at level high is not allowed by policy

=== Example: With Skills ===
Loaded 6 skills
Search results for 'create cube':
  - create_cube (score: 0.70)
    创建一个立方体并设置其位置、旋转和缩放

=== Example: Code Safety ===
✓ SAFE: Safe code
✗ UNSAFE: Dangerous eval
  - code_execution: Dynamic code execution: eval
✗ UNSAFE: File access
  - blacklisted_function: Blacklisted function call: open
✗ UNSAFE: Import os
  - blacklisted_module: Blacklisted module import: os
```

### 测试 2: 运行单元测试

```bash
cd packages/agent-core
pytest tests/ -v
```

### 测试 3: 在 Blender 中测试

1. 启动 Blender 5.0
2. Edit → Preferences → Add-ons
3. 搜索 "BlenderAgent"
4. 启用插件
5. 在 3D Viewport 侧边栏找到 "BlenderAgent" 标签
6. 输入指令测试

## 基础使用

### 示例 1: 使用 Mock LLM (无需 API Key)

```python
import asyncio
from blender_agent_core.llm import MockAdapter
from blender_agent_core.planner import TaskPlanner

async def main():
    # 创建 Mock LLM
    llm = MockAdapter(
        response_text='{"steps": [{"description": "Create cube", "tool_calls": []}]}'
    )
    
    # 创建规划器
    def tool_executor(tool_name, args):
        print(f"Executing: {tool_name}({args})")
        return {"success": True}
    
    planner = TaskPlanner(llm_adapter=llm, tool_executor=tool_executor)
    
    # 创建并执行计划
    plan = await planner.create_plan(
        user_request="创建一个红色的立方体",
        available_tools=[
            {"name": "create_primitive", "description": "Create object"},
            {"name": "set_color", "description": "Set color"},
        ]
    )
    
    result = await planner.execute_plan(plan)
    print(f"Status: {result.status.value}")

asyncio.run(main())
```

### 示例 2: 使用真实 LLM

```python
import asyncio
from blender_agent_core.llm import OpenAIAdapter
from blender_agent_core.planner import TaskPlanner

async def main():
    # 创建 OpenAI 适配器
    llm = OpenAIAdapter(
        api_key="your-api-key",  # 或使用环境变量 OPENAI_API_KEY
        model="gpt-4"
    )
    
    # 创建规划器
    planner = TaskPlanner(llm_adapter=llm, tool_executor=your_tool_executor)
    
    # 创建计划
    plan = await planner.create_plan(
        user_request="创建一个简单的房间场景",
        available_tools=your_tools
    )
    
    # 执行计划
    result = await planner.execute_plan(plan)

asyncio.run(main())
```

### 示例 3: 使用安全网关

```python
from blender_agent_core.safety import SecurityGateway, SecurityPolicy

# 创建安全策略
policy = SecurityPolicy(
    allow_high_risk=False,  # 不允许高风险操作
    enable_ast_analysis=True,  # 启用代码分析
)

gateway = SecurityGateway(policy=policy)

# 验证操作
is_allowed, reason = await gateway.validate_operation(
    "create_primitive",
    {"type": "CUBE"}
)

if is_allowed:
    # 执行操作
    pass
else:
    print(f"操作被拒绝: {reason}")

# 验证代码
code = "import bpy\nbpy.ops.mesh.primitive_cube_add()"
is_safe, violations = gateway.validate_code(code)

if not is_safe:
    for v in violations:
        print(f"安全问题: {v.description}")
```

### 示例 4: 使用技能系统

```python
from pathlib import Path
from blender_agent_core.skills import SkillStore, SkillExecutor

# 加载技能
store = SkillStore(skills_dir=Path("skills/builtin"))
store.load_all_skills()

# 搜索技能
results = store.search_skills("create cube", limit=3)
for skill, score in results:
    print(f"{skill.metadata.name}: {score:.2f}")

# 执行技能
skill = store.get_skill("create_cube")
executor = SkillExecutor(tool_executor=your_tool_executor)

result = await executor.execute_skill(
    skill,
    parameters={
        "name": "MyCube",
        "location": {"x": 2, "y": 0, "z": 1}
    }
)
```

## 配置

### 环境变量

```bash
# OpenAI
export OPENAI_API_KEY="sk-..."

# Anthropic
export ANTHROPIC_API_KEY="sk-ant-..."

# Azure OpenAI
export AZURE_OPENAI_ENDPOINT="https://your-resource.openai.azure.com"
export AZURE_OPENAI_API_KEY="..."
export AZURE_OPENAI_DEPLOYMENT="your-deployment"
```

### 配置文件 (可选)

创建 `config.yaml`:

```yaml
llm:
  provider: openai  # openai, anthropic, azure
  model: gpt-4
  temperature: 0.7

security:
  allow_high_risk: false
  enable_ast_analysis: true
  auto_execute_threshold: low

skills:
  builtin_dir: skills/builtin
  user_dir: ~/.blenderagent/skills
```

## 常见问题

### Q: 如何切换 LLM 模型？

```python
# OpenAI
llm = OpenAIAdapter(model="gpt-4")

# Anthropic
llm = AnthropicAdapter(model="claude-3-5-sonnet-20241022")

# Azure
llm = AzureOpenAIAdapter(deployment_name="your-deployment")
```

### Q: 如何自定义安全策略？

```python
policy = SecurityPolicy(
    allow_high_risk=True,  # 允许高风险操作
    allow_critical=False,  # 禁止关键操作
    function_blacklist=["eval", "exec"],  # 自定义黑名单
)
```

### Q: 如何创建自定义技能？

参考 `skills/builtin/create_cube.json`，创建 JSON 文件：

```json
{
  "metadata": {
    "name": "my_skill",
    "version": "1.0.0",
    "description": "My custom skill",
    "category": "modeling",
    "parameters": [...]
  },
  "steps": [
    {
      "tool_name": "tool_name",
      "arguments": {...}
    }
  ]
}
```

### Q: 如何调试？

```python
import logging

# 启用调试日志
logging.basicConfig(level=logging.DEBUG)

# 或针对特定模块
logging.getLogger("blender_agent_core").setLevel(logging.DEBUG)
```

## 下一步

- 📖 阅读 [API 文档](API.md)
- 🎓 学习 [技能开发指南](SKILL_DEVELOPMENT.md)
- 🔧 查看 [架构设计](../planning/plan.md)
- 💡 浏览 [示例代码](../../examples/)

## 获取帮助

- 📝 [GitHub Issues](https://github.com/your-org/BlenderAgentBot/issues)
- 💬 [Discussions](https://github.com/your-org/BlenderAgentBot/discussions)
- 📧 Email: support@blenderagentbot.com

## 许可证

MIT License - 详见 [LICENSE](../../LICENSE)
