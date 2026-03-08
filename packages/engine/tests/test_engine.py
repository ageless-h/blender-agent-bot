from __future__ import annotations

from packages.engine.engine import Engine
from packages.engine.protocol import AgentRequest, ResponseStatus, ToolCall


def test_engine_handles_tool_call() -> None:
    engine = Engine()
    request = AgentRequest(
        session_id="s1",
        tool_call=ToolCall(tool_name="missing_tool", arguments={}),
    )

    response = engine.handle_request(request)
    assert response.status == ResponseStatus.ERROR
    assert response.tool_results
    assert response.tool_results[0].tool_name == "missing_tool"
