from __future__ import annotations

from shared.types.common import (
    Color,
    MaterialRef,
    ObjectInfo,
    Position3D,
    Rotation3D,
    Scale3D,
    SceneInfo,
    ViewportCapture,
)
from shared.types.session_types import ChatMessage, MessageRole, Session
from shared.types.tool_types import SafetyLevel, ToolCall, ToolDefinition, ToolResult


def test_common_models_smoke() -> None:
    object_info = ObjectInfo(
        name="Cube",
        type="MESH",
        location=Position3D(x=0.0, y=0.0, z=0.0),
        rotation=Rotation3D(x=0.0, y=0.0, z=0.0),
        scale=Scale3D(x=1.0, y=1.0, z=1.0),
        materials=[MaterialRef(name="Default")],
    )
    scene_info = SceneInfo(name="Scene", frame_start=1, frame_end=250, frame_current=1, fps=24.0, object_count=1)
    capture = ViewportCapture(data_base64="ZmFrZQ==", width=1920, height=1080)
    color = Color(r=1.0, g=0.5, b=0.2, a=1.0)

    assert object_info.name == "Cube"
    assert scene_info.object_count == 1
    assert capture.mime_type == "image/png"
    assert color.g == 0.5


def test_tool_and_session_models_smoke() -> None:
    tool_def = ToolDefinition(
        name="create_cube",
        description="创建一个立方体",
        parameters={"size": {"type": "number"}},
        safety_level=SafetyLevel.LEVEL_0,
    )
    tool_call = ToolCall(tool_name="create_cube", arguments={"size": 2.0})
    tool_result = ToolResult(success=True, data={"object_name": "Cube"})

    message = ChatMessage(role=MessageRole.USER, content="创建立方体", tool_calls=[tool_call])
    session = Session(id="session-1", user_id="u-1", messages=[message])
    session.add_message(ChatMessage(role=MessageRole.ASSISTANT, content="已创建"))

    assert tool_def.safety_level == SafetyLevel.LEVEL_0
    assert tool_result.success is True
    assert len(session.messages) == 2
