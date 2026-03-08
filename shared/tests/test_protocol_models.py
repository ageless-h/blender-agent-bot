from __future__ import annotations

import pytest
from pydantic import ValidationError

from shared.protocol.agent_request import AgentRequest, ConfirmResponse, ToolCallRequest
from shared.protocol.agent_response import AgentResponse, ConfirmRequest, ResponseStatus
from shared.types.tool_types import SafetyLevel, ToolCall


def test_agent_request_requires_required_fields() -> None:
    with pytest.raises(ValidationError):
        AgentRequest.from_dict({"message": "hello"})


def test_tool_call_request_payload() -> None:
    request = ToolCallRequest(
        session_id="s-tool",
        tool_call=ToolCall(tool_name="move_object", arguments={"name": "Cube", "x": 1.0}),
        require_confirmation=True,
    )

    assert request.tool_call.tool_name == "move_object"
    assert request.require_confirmation is True


def test_confirm_response_and_confirm_request() -> None:
    confirm_response = ConfirmResponse(
        session_id="s-confirm",
        request_id="req-1",
        approved=False,
        reason="风险较高",
    )

    confirm_request = ConfirmRequest(
        session_id="s-confirm",
        request_id="req-1",
        message="将删除场景中的全部对象",
        safety_level=SafetyLevel.LEVEL_3,
        operation={"tool": "delete_all"},
    )

    assert confirm_response.approved is False
    assert confirm_request.safety_level == SafetyLevel.LEVEL_3


def test_agent_response_status_enum() -> None:
    response = AgentResponse(
        session_id="s-resp",
        message="需要你确认",
        status=ResponseStatus.NEEDS_CONFIRM,
    )

    assert response.status.value == "needs_confirm"
