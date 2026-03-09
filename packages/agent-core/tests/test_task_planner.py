"""Tests for task planner."""

import pytest

from blender_agent_core.llm import MockAdapter
from blender_agent_core.planner import (
    TaskPlan,
    TaskPlanner,
    TaskStatus,
    ToolCall,
    ToolResult,
)


class TestTaskPlan:
    """Test TaskPlan data structure."""

    def test_create_empty_plan(self):
        """Test creating an empty plan."""
        plan = TaskPlan(goal="Test goal")

        assert plan.goal == "Test goal"
        assert len(plan.steps) == 0
        assert plan.current_step == 0
        assert plan.status == TaskStatus.PENDING

    def test_add_steps(self):
        """Test adding steps to a plan."""
        plan = TaskPlan(goal="Test")

        step1 = plan.add_step("Step 1")
        step2 = plan.add_step(
            "Step 2", tool_calls=[ToolCall(tool_name="test_tool", arguments={"arg": "value"})]
        )

        assert len(plan.steps) == 2
        assert step1.step_id == 0
        assert step2.step_id == 1
        assert len(step2.tool_calls) == 1

    def test_get_current_step(self):
        """Test getting current step."""
        plan = TaskPlan(goal="Test")
        plan.add_step("Step 1")
        plan.add_step("Step 2")

        current = plan.get_current_step()
        assert current is not None
        assert current.step_id == 0

        plan.advance_step()
        current = plan.get_current_step()
        assert current is not None
        assert current.step_id == 1

    def test_advance_step(self):
        """Test advancing through steps."""
        plan = TaskPlan(goal="Test")
        plan.add_step("Step 1")
        plan.add_step("Step 2")

        assert plan.current_step == 0
        assert plan.advance_step() is True
        assert plan.current_step == 1
        assert plan.advance_step() is False  # At end
        assert plan.current_step == 1

    def test_is_complete(self):
        """Test completion detection."""
        plan = TaskPlan(goal="Test")
        plan.add_step("Step 1")

        assert plan.is_complete() is False

        plan.advance_step()
        assert plan.is_complete() is True

    def test_mark_complete(self):
        """Test marking plan as complete."""
        plan = TaskPlan(goal="Test")
        plan.mark_complete(result="Success")

        assert plan.status == TaskStatus.COMPLETED
        assert plan.final_result == "Success"

    def test_mark_failed(self):
        """Test marking plan as failed."""
        plan = TaskPlan(goal="Test")
        plan.mark_failed("Error occurred")

        assert plan.status == TaskStatus.FAILED
        assert plan.final_result == {"error": "Error occurred"}

    def test_to_dict(self):
        """Test serialization to dict."""
        plan = TaskPlan(goal="Test goal")
        plan.add_step("Step 1")

        data = plan.to_dict()

        assert data["goal"] == "Test goal"
        assert len(data["steps"]) == 1
        assert data["status"] == "pending"


class TestToolCall:
    """Test ToolCall data structure."""

    def test_create_tool_call(self):
        """Test creating a tool call."""
        tc = ToolCall(
            tool_name="test_tool",
            arguments={"arg1": "value1"},
            call_id="call_123",
        )

        assert tc.tool_name == "test_tool"
        assert tc.arguments == {"arg1": "value1"}
        assert tc.call_id == "call_123"

    def test_to_dict(self):
        """Test serialization."""
        tc = ToolCall(tool_name="test", arguments={})
        data = tc.to_dict()

        assert data["tool_name"] == "test"
        assert data["arguments"] == {}


class TestToolResult:
    """Test ToolResult data structure."""

    def test_success_result(self):
        """Test successful tool result."""
        result = ToolResult(
            call_id="call_123",
            tool_name="test_tool",
            success=True,
            result={"data": "value"},
        )

        assert result.success is True
        assert result.error is None

    def test_failed_result(self):
        """Test failed tool result."""
        result = ToolResult(
            call_id="call_123",
            tool_name="test_tool",
            success=False,
            result=None,
            error="Tool failed",
        )

        assert result.success is False
        assert result.error == "Tool failed"


class TestTaskPlanner:
    """Test TaskPlanner."""

    @pytest.mark.asyncio
    async def test_create_plan(self):
        """Test creating a plan from user request."""
        llm = MockAdapter(
            response_text='```json\n{"steps": [{"description": "Step 1", "tool_calls": []}]}\n```'
        )
        planner = TaskPlanner(llm_adapter=llm)

        plan = await planner.create_plan(
            user_request="Create a cube",
            available_tools=[{"name": "create_object", "description": "Create an object"}],
        )

        assert plan.goal == "Create a cube"
        assert len(plan.steps) > 0

    @pytest.mark.asyncio
    async def test_execute_step_with_tools(self):
        """Test executing a step with tool calls."""
        llm = MockAdapter()

        # Mock tool executor
        tool_results = []

        def mock_executor(tool_name: str, args: dict):
            tool_results.append((tool_name, args))
            return {"success": True}

        planner = TaskPlanner(llm_adapter=llm, tool_executor=mock_executor)

        # Create a plan with a tool call
        plan = TaskPlan(goal="Test")
        step = plan.add_step(
            "Create cube",
            tool_calls=[
                ToolCall(
                    tool_name="create_object",
                    arguments={"type": "cube"},
                    call_id="call_1",
                )
            ],
        )

        # Execute the step
        results = await planner.execute_step(step, plan)

        assert len(results) == 1
        assert results[0].success is True
        assert step.status == TaskStatus.COMPLETED
        assert len(tool_results) == 1
        assert tool_results[0] == ("create_object", {"type": "cube"})

    @pytest.mark.asyncio
    async def test_execute_step_failure(self):
        """Test handling step execution failure."""
        llm = MockAdapter()

        def failing_executor(tool_name: str, args: dict):
            raise RuntimeError("Tool failed")

        planner = TaskPlanner(llm_adapter=llm, tool_executor=failing_executor)

        plan = TaskPlan(goal="Test")
        step = plan.add_step(
            "Failing step",
            tool_calls=[ToolCall(tool_name="fail_tool", arguments={}, call_id="call_1")],
        )

        results = await planner.execute_step(step, plan)

        assert len(results) == 1
        assert results[0].success is False
        assert results[0].error is not None
        assert "Tool failed" in results[0].error
        assert step.status == TaskStatus.FAILED

    @pytest.mark.asyncio
    async def test_execute_complete_plan(self):
        """Test executing a complete multi-step plan."""
        llm = MockAdapter()

        executed_steps = []

        def mock_executor(tool_name: str, args: dict):
            executed_steps.append(tool_name)
            return {"result": f"Executed {tool_name}"}

        planner = TaskPlanner(llm_adapter=llm, tool_executor=mock_executor)

        # Create a 3-step plan
        plan = TaskPlan(goal="Multi-step test")
        plan.add_step("Step 1", [ToolCall("tool1", {}, "c1")])
        plan.add_step("Step 2", [ToolCall("tool2", {}, "c2")])
        plan.add_step("Step 3", [ToolCall("tool3", {}, "c3")])

        # Execute the plan
        completed_plan = await planner.execute_plan(plan)

        assert completed_plan.status == TaskStatus.COMPLETED
        assert len(executed_steps) == 3
        assert executed_steps == ["tool1", "tool2", "tool3"]

    @pytest.mark.asyncio
    async def test_execute_plan_with_callback(self):
        """Test execution with step completion callback."""
        llm = MockAdapter()

        def mock_executor(tool_name: str, args: dict):
            return {"success": True}

        planner = TaskPlanner(llm_adapter=llm, tool_executor=mock_executor)

        # Track callbacks
        callback_steps = []

        def on_step_complete(step, results):
            callback_steps.append(step.step_id)

        plan = TaskPlan(goal="Test")
        plan.add_step("Step 1", [ToolCall("tool1", {}, "c1")])
        plan.add_step("Step 2", [ToolCall("tool2", {}, "c2")])

        await planner.execute_plan(plan, on_step_complete=on_step_complete)

        assert len(callback_steps) == 2
        assert callback_steps == [0, 1]

    @pytest.mark.asyncio
    async def test_plan_failure_stops_execution(self):
        """Test that plan execution stops on step failure."""
        llm = MockAdapter()

        executed_tools = []

        def mock_executor(tool_name: str, args: dict):
            executed_tools.append(tool_name)
            if tool_name == "fail_tool":
                raise RuntimeError("Intentional failure")
            return {"success": True}

        planner = TaskPlanner(llm_adapter=llm, tool_executor=mock_executor)

        plan = TaskPlan(goal="Test failure")
        plan.add_step("Step 1", [ToolCall("tool1", {}, "c1")])
        plan.add_step("Step 2", [ToolCall("fail_tool", {}, "c2")])
        plan.add_step("Step 3", [ToolCall("tool3", {}, "c3")])

        completed_plan = await planner.execute_plan(plan)

        assert completed_plan.status == TaskStatus.FAILED
        assert len(executed_tools) == 2  # Only first two steps
        assert "tool3" not in executed_tools

    def test_build_planning_prompt(self):
        """Test planning prompt generation."""
        llm = MockAdapter()
        planner = TaskPlanner(llm_adapter=llm)

        prompt = planner._build_planning_prompt(
            user_request="Create a red cube",
            available_tools=[
                {"name": "create_object", "description": "Create an object"},
                {"name": "set_color", "description": "Set object color"},
            ],
            context={"scene": "Scene1"},
        )

        assert "Create a red cube" in prompt
        assert "create_object" in prompt
        assert "set_color" in prompt
        assert "Scene1" in prompt
        assert "JSON" in prompt
