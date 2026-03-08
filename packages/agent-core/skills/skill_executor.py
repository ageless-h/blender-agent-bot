from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping

from router.tool_router import ToolRouter
from .skill_store import SkillRecord, SkillStep


@dataclass(slots=True)
class SkillExecutionStepResult:
    step_index: int
    tool_name: str
    ok: bool
    response: Any | None = None
    error: str | None = None
    validation_passed: bool = True


@dataclass(slots=True)
class SkillExecutionResult:
    skill_id: str
    ok: bool
    step_results: list[SkillExecutionStepResult] = field(default_factory=list)
    failed_step: int | None = None


class SkillExecutor:
    """执行 Skill Capsule 的工具调用序列。"""

    def __init__(self, tool_router: ToolRouter) -> None:
        self.tool_router = tool_router

    def execute(
        self,
        skill: SkillRecord,
        *,
        variables: Mapping[str, Any] | None = None,
        stop_on_error: bool = True,
    ) -> SkillExecutionResult:
        step_results: list[SkillExecutionStepResult] = []
        resolved_variables = dict(variables or {})

        for index, step in enumerate(skill.capsule, start=1):
            rendered_arguments = self._render_arguments(step, resolved_variables)
            try:
                response = self.tool_router.dispatch(step.tool_name, rendered_arguments)
            except Exception as exc:
                result = SkillExecutionStepResult(
                    step_index=index,
                    tool_name=step.tool_name,
                    ok=False,
                    error=str(exc),
                    validation_passed=False,
                )
                step_results.append(result)
                if stop_on_error:
                    return SkillExecutionResult(
                        skill_id=skill.skill_id,
                        ok=False,
                        step_results=step_results,
                        failed_step=index,
                    )
                continue

            validation_passed = self._validate_step(step, response)
            result = SkillExecutionStepResult(
                step_index=index,
                tool_name=step.tool_name,
                ok=validation_passed,
                response=response,
                validation_passed=validation_passed,
                error=None if validation_passed else "validation_failed",
            )
            step_results.append(result)

            if not validation_passed and stop_on_error:
                return SkillExecutionResult(
                    skill_id=skill.skill_id,
                    ok=False,
                    step_results=step_results,
                    failed_step=index,
                )

            resolved_variables[f"step_{index}_result"] = response

        return SkillExecutionResult(
            skill_id=skill.skill_id,
            ok=all(item.ok for item in step_results),
            step_results=step_results,
            failed_step=None,
        )

    def _render_arguments(self, step: SkillStep, variables: Mapping[str, Any]) -> dict[str, Any]:
        return self._render_value(step.arguments, variables)

    def _render_value(self, value: Any, variables: Mapping[str, Any]) -> Any:
        if isinstance(value, str):
            rendered = value
            for key, replacement in variables.items():
                rendered = rendered.replace(f"${{{key}}}", str(replacement))
            return rendered
        if isinstance(value, list):
            return [self._render_value(item, variables) for item in value]
        if isinstance(value, dict):
            return {key: self._render_value(item, variables) for key, item in value.items()}
        return value

    def _validate_step(self, step: SkillStep, response: Any) -> bool:
        if not step.validation:
            return True

        if step.validation.get("object_exists"):
            key = str(step.validation["object_exists"])
            if isinstance(response, Mapping):
                return bool(response.get(key))
            return False

        if "object_count" in step.validation:
            expected = int(step.validation["object_count"])
            if isinstance(response, Mapping):
                current = int(response.get("object_count", -1))
                return current == expected
            return False

        if "equals" in step.validation and isinstance(response, Mapping):
            expected_mapping = step.validation.get("equals")
            if not isinstance(expected_mapping, Mapping):
                return False
            for key, expected in expected_mapping.items():
                if response.get(key) != expected:
                    return False
            return True

        return True
