"""Integration test example for Agent Core.

This demonstrates how to use the complete system end-to-end.
"""

import asyncio
from pathlib import Path

from blender_agent_core import AgentCore
from blender_agent_core.llm import MockAdapter
from blender_agent_core.planner import TaskPlanner
from blender_agent_core.safety import AutoApproveConfirmation, ConfirmationManager, SecurityGateway
from blender_agent_core.skills import SkillStore


async def example_basic_workflow():
    """Example: Basic workflow with mock LLM."""
    print("=== Example: Basic Workflow ===\n")

    # 1. Setup LLM adapter
    llm = MockAdapter(response_text='```json\n{"steps": [{"description": "Create cube", "tool_calls": []}]}\n```')

    # 2. Setup task planner
    def mock_tool_executor(tool_name: str, args: dict):
        print(f"  Executing: {tool_name}({args})")
        return {"success": True, "result": f"Executed {tool_name}"}

    planner = TaskPlanner(llm_adapter=llm, tool_executor=mock_tool_executor)

    # 3. Create and execute plan
    plan = await planner.create_plan(
        user_request="Create a red cube",
        available_tools=[
            {"name": "create_primitive", "description": "Create primitive object"},
            {"name": "set_color", "description": "Set object color"},
        ],
    )

    print(f"Created plan with {len(plan.steps)} steps")

    # Execute plan
    completed_plan = await planner.execute_plan(plan)

    print(f"Plan status: {completed_plan.status.value}")
    print()


async def example_with_security():
    """Example: Workflow with security gateway."""
    print("=== Example: With Security ===\n")

    # Setup security gateway with auto-approve
    confirmation_manager = ConfirmationManager(confirmation_callback=AutoApproveConfirmation())
    gateway = SecurityGateway(confirmation_manager=confirmation_manager)

    # Validate operations
    operations = [
        ("create_primitive", {"type": "CUBE"}),
        ("delete_all_objects", {}),
        ("execute_script", {"code": "import os"}),
    ]

    for op_name, op_args in operations:
        is_allowed, reason = await gateway.validate_operation(op_name, op_args)
        status = "✓ ALLOWED" if is_allowed else "✗ DENIED"
        print(f"{status}: {op_name}")
        if reason:
            print(f"  Reason: {reason}")

    print()


async def example_with_skills():
    """Example: Using skill system."""
    print("=== Example: With Skills ===\n")

    # Setup skill store
    skills_dir = Path(__file__).parent.parent.parent / "skills" / "builtin"
    store = SkillStore(skills_dir=skills_dir)

    # Load skills
    count = store.load_all_skills()
    print(f"Loaded {count} skills")

    # Search for skills
    results = store.search_skills("create cube", limit=3)
    print(f"\nSearch results for 'create cube':")
    for skill, score in results:
        print(f"  - {skill.metadata.name} (score: {score:.2f})")
        print(f"    {skill.metadata.description}")

    print()


async def example_code_safety():
    """Example: Code safety validation."""
    print("=== Example: Code Safety ===\n")

    gateway = SecurityGateway()

    # Test various code snippets
    code_samples = [
        ("Safe code", "x = 1 + 2\nprint(x)"),
        ("Dangerous eval", "eval('malicious code')"),
        ("File access", "open('/etc/passwd', 'r')"),
        ("Import os", "import os\nos.system('ls')"),
    ]

    for name, code in code_samples:
        is_safe, violations = gateway.validate_code(code)
        status = "✓ SAFE" if is_safe else "✗ UNSAFE"
        print(f"{status}: {name}")
        if violations:
            for v in violations:
                print(f"  - {v.violation_type}: {v.description}")

    print()


async def main():
    """Run all examples."""
    print("BlenderAgentBot Integration Test Examples")
    print("=" * 50)
    print()

    await example_basic_workflow()
    await example_with_security()
    await example_with_skills()
    await example_code_safety()

    print("=" * 50)
    print("All examples completed!")


if __name__ == "__main__":
    asyncio.run(main())
