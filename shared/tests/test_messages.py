from __future__ import annotations

from shared.protocol.agent_request import AgentRequest, AttachmentRef, RequestOptions
from shared.protocol.agent_response import AgentResponse, StreamChunk
from shared.protocol.messages import MessageType
from shared.types.tool_types import ToolCall


def test_agent_request_json_roundtrip() -> None:
    request = AgentRequest(
        session_id="session-1",
        message="请帮我创建一个立方体",
        attachments=[
            AttachmentRef(
                name="reference.png",
                mime_type="image/png",
                uri="file:///tmp/reference.png",
            )
        ],
        options=RequestOptions(provider="openai", model="gpt-4o-mini"),
    )

    payload = request.to_json()
    restored = AgentRequest.from_json(payload)

    assert restored.session_id == "session-1"
    assert restored.message == "请帮我创建一个立方体"
    assert restored.options.model == "gpt-4o-mini"
    assert restored.type == MessageType.CHAT


def test_agent_response_and_stream_chunk_serialization() -> None:
    response = AgentResponse(
        session_id="session-2",
        message="已执行",
        tool_calls=[ToolCall(tool_name="create_cube", arguments={"size": 2.0})],
    )
    restored_response = AgentResponse.from_json(response.to_json())

    chunk = StreamChunk(
        session_id="session-2",
        delta="处理中",
        done=False,
    )
    restored_chunk = StreamChunk.from_json(chunk.to_json())

    assert restored_response.tool_calls[0].tool_name == "create_cube"
    assert restored_chunk.delta == "处理中"
    assert restored_chunk.type == MessageType.STREAM_CHUNK
