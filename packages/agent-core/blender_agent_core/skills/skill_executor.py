"""Skill executor for running skill capsules.

Executes skills by translating them into tool calls.
"""

from __future__ import annotations

from typing import Any, Callable

from ..planner import TaskPlan, ToolCall
from .skill_capsule import SkillCapsule


class SkillExecutor:
    """Executes skill capsules.

    Translates skill steps into tool calls and executes them.
    """

    def __init__(
        self,
        tool_executor: Callable[[str, dict[str, Any]], Any] | None = None,
    ):
        """Initialize skill executor.

        Args:
            tool_executor: Function to execute tool calls
        """
        self.tool_executor = tool_executor

    def skill_to_plan(
        self,
        skill: SkillCapsule,
        parameters: dict[str, Any],
    ) -> TaskPlan:
        """Convert a skill capsule to a task plan.

        Args:
            skill: Skill to execute
            parameters: Parameter values for the skill

        Returns:
            TaskPlan ready for execution
        """
        plan = TaskPlan(goal=skill.metadata.description)

        for step in skill.steps:
            # Substitute parameters in arguments
            arguments = self._substitute_parameters(
                step.arguments,
                parameters,
            )

            # Create tool call
            tool_call = ToolCall(
                tool_name=step.tool_name,
                arguments=arguments,
            )

            # Add step to plan
            plan.add_step(
                description=step.description or f"Execute {step.tool_name}",
                tool_calls=[tool_call],
            )

        return plan

    def _substitute_parameters(
        self,
        arguments: dict[str, Any],
        parameters: dict[str, Any],
    ) -> dict[str, Any]:
        """Substitute parameter placeholders in arguments.

        Args:
            arguments: Argument template with placeholders
            parameters: Parameter values

        Returns:
            Arguments with substituted values
        """
        result = {}

        for key, value in arguments.items():
            if isinstance(value, str) and value.startswith("$"):
                # Parameter placeholder
                param_name = value[1:]
                result[key] = parameters.get(param_name, value)
            elif isinstance(value, dict):
                # Recursive substitution
                result[key] = self._substitute_parameters(value, parameters)
            elif isinstance(value, list):
                # Substitute in list items
                result[key] = [
                    self._substitute_parameters({"_": item}, parameters)["_"]
                    if isinstance(item, (dict, str))
                    else item
                    for item in value
                ]
            else:
                result[key] = value

        return result

    async def execute_skill(
        self,
        skill: SkillCapsule,
        parameters: dict[str, Any],
    ) -> dict[str, Any]:
        """Execute a skill with given parameters.

        Args:
            skill: Skill to execute
            parameters: Parameter values

        Returns:
            Execution result

        Raises:
            RuntimeError: If execution fails
        """
        if not self.tool_executor:
            raise RuntimeError("No tool executor configured")

        # Convert skill to plan
        plan = self.skill_to_plan(skill, parameters)

        # Execute each step
        results = []
        for step in plan.steps:
            for tool_call in step.tool_calls:
                result = self.tool_executor(
                    tool_call.tool_name,
                    tool_call.arguments,
                )

                # Handle async executors
                if hasattr(result, "__await__"):
                    result = await result

                results.append(result)

        return {
            "skill": skill.metadata.name,
            "success": True,
            "results": results,
        }


__all__ = ["SkillExecutor"]
