# Agent Core

> BlenderAgentBot 的 AI 大脑 — LLM 适配、任务规划、安全网关、技能引擎

## 概述

Agent Core 是 BlenderAgentBot 的核心智能层，负责：
- 统一不同 LLM 的调用接口（OpenAI/Anthropic/本地模型）
- 将用户指令拆解为工具调用序列
- 分级安全体系和 AST 黑名单检查
- 会话管理和上下文引擎
- 技能匹配、执行和进化

## 架构

```
blender_agent_core/
├── llm/                   # LLM 适配器
│   ├── base.py            # LLMAdapter 抽象基类
│   ├── capabilities.py    # ModelCapabilities 定义
│   ├── openai_adapter.py  # OpenAI 兼容适配器
│   ├── anthropic_adapter.py # Claude 适配器
│   └── fallback_adapter.py  # 降级方案
├── planner/               # 任务规划器
│   ├── task_planner.py    # 多步规划
│   └── execution_loop.py  # 执行循环
├── safety/                # 安全网关
│   ├── security_levels.py # 安全等级定义
│   ├── ast_analyzer.py    # AST 静态分析
│   └── confirmation.py    # 用户确认流程
├── context/               # 上下文引擎
│   └── context_manager.py # 场景数据拉取
├── session/               # 会话管理
│   └── session_manager.py # 多会话隔离
├── skills/                # 技能引擎
│   ├── skill_store.py     # 本地技能库
│   ├── skill_matcher.py   # 模糊匹配
│   ├── skill_executor.py  # 执行工具序列
│   └── skill_capsule.py   # Skill Capsule 格式
├── router/                # 工具路由器
│   └── tool_router.py     # Engine 调用映射
└── core.py                # AgentCore 主类
```

## 安装

```bash
cd packages/agent-core
pip install -e ".[dev]"
```

## 使用

```python
from blender_agent_core import AgentCore
from blender_agent_core.llm import OpenAIAdapter

# 初始化
adapter = OpenAIAdapter(api_key="your-key")
agent = AgentCore(llm_adapter=adapter)

# 处理请求
response = await agent.process("创建一个红色的立方体")
```

## 开发

```bash
# 运行测试
pytest

# 代码格式化
black .
ruff check .

# 类型检查
mypy blender_agent_core
```

## License

MIT
