from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .skill_store import SkillMetadata, SkillRecord, SkillStep


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass(slots=True)
class RecordedOperation:
    tool_name: str
    arguments: dict[str, Any]
    result: dict[str, Any] = field(default_factory=dict)
    success: bool = True
    created_at: str = field(default_factory=_utc_now_iso)


class SkillRecorder:
    """将操作序列录制为 Skill。"""

    def __init__(self) -> None:
        self._operations: list[RecordedOperation] = []

    def record(
        self,
        *,
        tool_name: str,
        arguments: dict[str, Any],
        result: dict[str, Any] | None = None,
        success: bool = True,
    ) -> None:
        operation = RecordedOperation(
            tool_name=tool_name,
            arguments=dict(arguments),
            result=dict(result or {}),
            success=success,
        )
        self._operations.append(operation)

    def clear(self) -> None:
        self._operations.clear()

    def to_skill(
        self,
        *,
        skill_id: str,
        name: str,
        description: str,
        tags: list[str] | None = None,
        include_failed: bool = False,
    ) -> SkillRecord:
        selected_ops = [operation for operation in self._operations if include_failed or operation.success]
        capsule = [
            SkillStep(
                tool_name=operation.tool_name,
                arguments=operation.arguments,
                validation={},
            )
            for operation in selected_ops
        ]
        metadata = SkillMetadata(
            name=name,
            description=description,
            tags=tags or [],
            success_rate=self._calc_success_rate(selected_ops),
        )
        return SkillRecord(
            skill_id=skill_id,
            metadata=metadata,
            capsule=capsule,
            gene={"recorded_operations": len(selected_ops)},
        )

    def export_yaml(self, skill: SkillRecord, path: str | Path) -> Path:
        target = Path(path)
        target.parent.mkdir(parents=True, exist_ok=True)
        from .skill_store import SkillStore

        store = SkillStore(target.parent)
        temp_skill = SkillRecord(
            skill_id=target.stem,
            metadata=skill.metadata,
            capsule=skill.capsule,
            gene=skill.gene,
            created_at=skill.created_at,
            updated_at=skill.updated_at,
        )
        final_path = store.save(temp_skill)
        if final_path != target:
            final_path.replace(target)
            final_path = target
        return final_path

    def _calc_success_rate(self, operations: list[RecordedOperation]) -> float:
        if not operations:
            return 0.0
        success_count = sum(1 for operation in operations if operation.success)
        return round(success_count / len(operations), 4)
