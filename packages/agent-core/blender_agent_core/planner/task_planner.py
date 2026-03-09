"""Task planner for multi-step execution.

The TaskPlanner breaks down complex user requests into executable steps,
coordinates with the LLM for planning, and manages execution flow.
"""

from __future__ import annotations

import json
import uuid
from typing import Any, Callable

from ..llm import LLMAdapter, LLMResponse
from .task_plan import TaskPlan, TaskStatus, ToolCall, ToolResult


class TaskPlanner:
    """Plans and executes multi-step tasks.

    The planner:
    1. Takes a user request and available tools
    2. Uses LLM to generate a step-by-step plan
    3. Executes each step, calling tools as needed
    4. Handles tool results and adapts the plan
    5. Returns the final result
    """

    def __init__(
        self,
        llm_adapter: LLMAdapter,
        tool_executor: Callable[[str, dict[str, Any]], Any] | None = None,
        max_steps: int = 10,
        max_retries: int = 3,
    ):
        """Initialize task planner.

        Args:
            llm_adapter: LLM adapter for planning and reasoning
            tool_executor: Function to execute tool calls (tool_name, args) -> result
            max_steps: Maximum number of steps in a plan
            max_retries: Maximum retries for failed steps
        """
        self.llm = llm_adapter
        self.tool_executor = tool_executor
        self.max_steps = max_steps
        self.max_retries = max_retries

    def _build_planning_prompt(
        self,
        user_request: str,
        available_tools: list[dict[str, Any]],
        context: dict[str, Any] | None = None,
    ) -> str:
        """Build the system prompt for task planning.

        Args:
            user_request: User's request
            available_tools: List of available tool definitions
            context: Optional context information

        Returns:
            Planning prompt for the LLM
        """
        tool_descriptions = []
        for tool in available_tools:
            tool_descriptions.append(
                f"- {tool['name']}: {tool.get('description', 'No description')}"
            )

        tools_text = "\n".join(tool_descriptions) if tool_descriptions else "No tools available"

        context_text = ""
        if context:
            context_text = f"\n\nContext:\n{json.dumps(context, indent=2)}"

        prompt = f"""You are a task planning assistant for Blender automation.

User Request: {user_request}

Available Tools:
{tools_text}
{context_text}

Your task is to break down the user's request into a step-by-step plan.
Each step should be clear and actionable. Use the available tools when needed.

Respond with a JSON plan in this format:
{{
  "steps": [
    {{
      "description": "Step description",
      "tool_calls": [
        {{
          "tool_name": "tool_name",
          "arguments": {{"arg1": "value1"}}
        }}
      ]
    }}
  ]
}}

If no tools are needed for a step, use an empty tool_calls array.
Keep the plan concise (max {self.max_steps} steps).
"""
        return prompt

    async def create_plan(
        self,
        user_request: str,
        available_tools: list[dict[str, Any]],
        context: dict[str, Any] | None = None,
    ) -> TaskPlan:
        """Create a task execution plan.

        Args:
            user_request: User's request to accomplish
            available_tools: List of available tool definitions
            context: Optional context information

        Returns:
            TaskPlan with steps to execute

        Raises:
            ValueError: If plan generation fails
        """
        # Build planning prompt
        planning_prompt = self._build_planning_prompt(
            user_request,
            available_tools,
            context,
        )

        # Get plan from LLM
        messages = [
            {"role": "system", "content": planning_prompt},
            {"role": "user", "content": user_request},
        ]

        response = await self.llm.generate(messages=messages, temperature=0.3)

        # Parse plan from response
        plan = self._parse_plan_from_response(user_request, response)

        return plan

    def _parse_plan_from_response(
        self,
        goal: str,
        response: LLMResponse,
    ) -> TaskPlan:
        """Parse TaskPlan from LLM response.

        Args:
            goal: Original user goal
            response: LLM response containing the plan

        Returns:
            Parsed TaskPlan

        Raises:
            ValueError: If parsing fails
        """
        plan = TaskPlan(goal=goal)

        # Try to extract JSON from response
        content = response.content

        # Look for JSON block
        try:
            # Try direct JSON parse
            plan_data = json.loads(content)
        except json.JSONDecodeError:
            # Try to find JSON in markdown code block
            import re

            json_match = re.search(r"```json\s*(\{.*?\})\s*```", content, re.DOTALL)
            if json_match:
                plan_data = json.loads(json_match.group(1))
            else:
                # Fallback: create single-step plan with the response
                plan.add_step(
                    description=f"Execute: {goal}",
                    tool_calls=[],
                )
                return plan

        # Parse steps from plan data
        steps = plan_data.get("steps", [])
        for step_data in steps[: self.max_steps]:
            description = step_data.get("description", "")
            tool_calls_data = step_data.get("tool_calls", [])

            # Convert tool calls
            tool_calls = []
            for tc_data in tool_calls_data:
                tool_calls.append(
                    ToolCall(
                        tool_name=tc_data.get("tool_name", ""),
                        arguments=tc_data.get("arguments", {}),
                        call_id=str(uuid.uuid4()),
                    )
                )

            plan.add_step(description=description, tool_calls=tool_calls)

        return plan

    async def execute_step(
        self,
        step: Any,
        plan: TaskPlan,
    ) -> list[ToolResult]:
        """Execute a single step in the plan.

        Args:
            step: TaskStep to execute
            plan: The overall plan (for context)

        Returns:
            List of tool results from this step

        Raises:
            RuntimeError: If step execution fails
        """
        if not self.tool_executor:
            raise RuntimeError("No tool executor configured")

        step.status = TaskStatus.IN_PROGRESS
        results = []

        for tool_call in step.tool_calls:
            try:
                # Execute the tool
                result = await self._execute_tool_call(tool_call)
                results.append(result)

                if not result.success:
                    step.status = TaskStatus.FAILED
                    step.error = result.error
                    return results

            except Exception as e:
                # Tool execution failed
                result = ToolResult(
                    call_id=tool_call.call_id or str(uuid.uuid4()),
                    tool_name=tool_call.tool_name,
                    success=False,
                    result=None,
                    error=str(e),
                )
                results.append(result)
                step.status = TaskStatus.FAILED
                step.error = str(e)
                return results

        # All tools succeeded
        step.status = TaskStatus.COMPLETED
        step.result = results
        return results

    async def _execute_tool_call(self, tool_call: ToolCall) -> ToolResult:
        """Execute a single tool call.

        Args:
            tool_call: Tool call to execute

        Returns:
            ToolResult with execution outcome
        """
        try:
            result = self.tool_executor(
                tool_call.tool_name,
                tool_call.arguments,
            )

            # Handle async tool executors
            if hasattr(result, "__await__"):
                result = await result

            return ToolResult(
                call_id=tool_call.call_id or str(uuid.uuid4()),
                tool_name=tool_call.tool_name,
                success=True,
                result=result,
            )

        except Exception as e:
            return ToolResult(
                call_id=tool_call.call_id or str(uuid.uuid4()),
                tool_name=tool_call.tool_name,
                success=False,
                result=None,
                error=str(e),
            )

    async def execute_plan(
        self,
        plan: TaskPlan,
        on_step_complete: Callable[[Any, list[ToolResult]], None] | None = None,
    ) -> TaskPlan:
        """Execute a complete task plan.

        Args:
            plan: TaskPlan to execute
            on_step_complete: Optional callback after each step (step, results)

        Returns:
            The completed plan with results
        """
        plan.status = TaskStatus.IN_PROGRESS

        while not plan.is_complete():
            step = plan.get_current_step()
            if not step:
                break

            try:
                # Execute the step
                results = await self.execute_step(step, plan)

                # Notify callback
                if on_step_complete:
                    on_step_complete(step, results)

                # Check if step failed
                if step.status == TaskStatus.FAILED:
                    plan.mark_failed(f"Step {step.step_id} failed: {step.error}")
                    return plan

                # Move to next step
                if not plan.advance_step():
                    # No more steps
                    break

            except Exception as e:
                plan.mark_failed(f"Execution error: {str(e)}")
                return plan

        # All steps completed successfully
        plan.mark_complete()
        return plan


__all__ = ["TaskPlanner"]
