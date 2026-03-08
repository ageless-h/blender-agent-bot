from __future__ import annotations

import json
from typing import Any, Callable


def _get_bpy() -> Any | None:
    try:
        import bpy  # type: ignore

        return bpy
    except Exception:
        return None


ExecutorCallback = Callable[[dict[str, Any]], dict[str, Any]]
_EXECUTOR_CALLBACK: ExecutorCallback | None = None


def set_executor_callback(callback: ExecutorCallback | None) -> None:
    global _EXECUTOR_CALLBACK
    _EXECUTOR_CALLBACK = callback


def execute_payload(payload: dict[str, Any]) -> dict[str, Any]:
    if _EXECUTOR_CALLBACK is None:
        return {"status": "error", "message": "executor callback is not configured"}
    return _EXECUTOR_CALLBACK(payload)


bpy = _get_bpy()

if bpy is not None:

    class BlenderAgentOtExecute(bpy.types.Operator):
        bl_idname = "blenderagent.execute"
        bl_label = "BlenderAgent Execute"
        bl_options = {"REGISTER", "UNDO"}

        payload: bpy.props.StringProperty(name="Payload", default="{}")  # type: ignore[misc]

        def execute(self, context: Any) -> set[str]:
            del context
            try:
                payload_data = json.loads(self.payload or "{}")
                response = execute_payload(payload_data)
                if response.get("status") == "error":
                    self.report({"ERROR"}, str(response.get("message", "unknown error")))
                    return {"CANCELLED"}
                return {"FINISHED"}
            except Exception as exc:
                self.report({"ERROR"}, str(exc))
                return {"CANCELLED"}

    BLENDERAGENT_OT_execute = BlenderAgentOtExecute
    OPERATOR_CLASSES = [BLENDERAGENT_OT_execute]

else:
    OPERATOR_CLASSES: list[type[Any]] = []
