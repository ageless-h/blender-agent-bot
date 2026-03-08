from __future__ import annotations

from packages.engine.protocol import AgentRequest, AgentResponse, ResponseStatus, ToolCall, ToolResult


def test_agent_request_roundtrip() -> None:
    request = AgentRequest(
        session_id="session-1",
        message="hello",
        tool_call=ToolCall(tool_name="get_scene", arguments={"scene_name": "Scene"}),
    )

    encoded = request.to_json()
    decoded = AgentRequest.from_json(encoded)

    assert decoded.session_id == "session-1"
    assert decoded.tool_call is not None
    assert decoded.tool_call.tool_name == "get_scene"
    assert decoded.tool_call.arguments["scene_name"] == "Scene"


def test_agent_response_roundtrip() -> None:
    response = AgentResponse(
        session_id="session-1",
        status=ResponseStatus.SUCCESS,
        message="ok",
        tool_results=[ToolResult(tool_name="get_scene", success=True, data={"name": "Scene"})],
    )

    encoded = response.to_json()
    decoded = AgentResponse.from_json(encoded)

    assert decoded.status == ResponseStatus.SUCCESS
    assert decoded.tool_results[0].tool_name == "get_scene"
    assert decoded.tool_results[0].data["name"] == "Scene"
