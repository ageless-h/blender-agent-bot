from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Mapping


def _utcnow() -> datetime:
    return datetime.now(timezone.utc)


@dataclass(slots=True)
class SceneObject:
    name: str
    object_type: str
    location: tuple[float, float, float] = (0.0, 0.0, 0.0)
    selected: bool = False
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class SceneSnapshot:
    timestamp: datetime
    total_objects: int
    active_object: str | None
    selected_objects: list[str]
    objects: list[SceneObject] = field(default_factory=list)


class SceneContext:
    """操作前场景上下文提取与摘要。"""

    def from_payload(self, payload: Mapping[str, Any]) -> SceneSnapshot:
        objects_payload = payload.get("objects", []) if isinstance(payload, Mapping) else []
        objects: list[SceneObject] = []

        for item in objects_payload:
            if not isinstance(item, Mapping):
                continue
            location_raw = item.get("location", [0, 0, 0])
            if isinstance(location_raw, (list, tuple)) and len(location_raw) >= 3:
                location = (
                    float(location_raw[0]),
                    float(location_raw[1]),
                    float(location_raw[2]),
                )
            else:
                location = (0.0, 0.0, 0.0)

            scene_object = SceneObject(
                name=str(item.get("name", "unnamed")),
                object_type=str(item.get("type", "UNKNOWN")),
                location=location,
                selected=bool(item.get("selected", False)),
                metadata={
                    key: value for key, value in item.items() if key not in {"name", "type", "location", "selected"}
                },
            )
            objects.append(scene_object)

        selected_objects = [obj.name for obj in objects if obj.selected]
        active_object = payload.get("active_object") if isinstance(payload, Mapping) else None

        return SceneSnapshot(
            timestamp=_utcnow(),
            total_objects=len(objects),
            active_object=str(active_object) if active_object else None,
            selected_objects=selected_objects,
            objects=objects,
        )

    def summarize(self, snapshot: SceneSnapshot, *, max_objects: int = 8) -> str:
        object_lines = []
        for obj in snapshot.objects[:max_objects]:
            selected_mark = "*" if obj.selected else ""
            location_text = f"({obj.location[0]:.2f}, {obj.location[1]:.2f}, {obj.location[2]:.2f})"
            object_lines.append(f"- {obj.name}{selected_mark} [{obj.object_type}] @ {location_text}")

        if snapshot.total_objects > max_objects:
            object_lines.append(f"- ... 其余 {snapshot.total_objects - max_objects} 个对象已省略")

        selected = ", ".join(snapshot.selected_objects) if snapshot.selected_objects else "无"
        lines = [
            f"场景对象数: {snapshot.total_objects}",
            f"当前激活对象: {snapshot.active_object or '无'}",
            f"当前选中对象: {selected}",
            "对象列表:",
            *object_lines,
        ]
        return "\n".join(lines)

    def to_prompt_context(self, snapshot: SceneSnapshot) -> dict[str, Any]:
        return {
            "scene_summary": self.summarize(snapshot),
            "active_object": snapshot.active_object,
            "selected_objects": snapshot.selected_objects,
            "total_objects": snapshot.total_objects,
        }
