from __future__ import annotations

import asyncio
import importlib

import pytest

from blender_agent_core import AgentCore, SessionManager, ToolRouter

protocol = importlib.import_module("shared.protocol")
AgentRequest = protocol.AgentRequest
EngineResponse = protocol.EngineResponse
EngineResponseStatus = protocol.EngineResponseStatus


class StubLLMAdapter:
    async def generate_response(self, *, request, session, tools):
        assert request.message == "创建一个立方体"
        assert session.session_id == "session-1"
        assert any(tool["name"] == "create_object" for tool in tools)
        return {
            "message": "正在创建立方体",
            "tool_calls": [
                {
                    "tool_name": "create_object",
                    "arguments": {"type": "CUBE", "name": "TestCube"},
                }
            ],
        }


class StubEngine:
    def __init__(self) -> None:
        self.requests = []

    def execute_request(self, request):
        self.requests.append(request)
        return EngineResponse(
            status=EngineResponseStatus.SUCCESS,
            request_id=request.request_id,
            capability=request.capability,
            result={"object_name": request.payload["name"]},
        )


def test_session_manager_keeps_sessions_isolated() -> None:
    manager = SessionManager()

    first = manager.create_session("session-a", context={"scene": "A"})
    second = manager.create_session("session-b")

    first.history.append({"role": "user", "content": "hello from a"})
    second.history.append({"role": "user", "content": "hello from b"})

    assert manager.get_session("session-a") is first
    assert manager.get_session("session-b") is second
    assert first.history == [{"role": "user", "content": "hello from a"}]
    assert second.history == [{"role": "user", "content": "hello from b"}]
    assert first.context == {"scene": "A"}

    assert manager.delete_session("session-a") is True
    assert manager.get_session("session-a") is None
    assert manager.get_session("session-b") is second


def test_tool_router_maps_to_engine_request() -> None:
    router = ToolRouter()

    engine_request = router.map_to_engine("create_object", {"type": "CUBE"})

    assert engine_request.request_type.value == "execute_capability"
    assert engine_request.capability == "blender.create_object"
    assert engine_request.payload == {"type": "CUBE"}


def test_tool_router_raises_for_unknown_tool() -> None:
    router = ToolRouter()

    with pytest.raises(KeyError, match="unknown tool"):
        router.map_to_engine("not_a_real_tool", {})


def test_agent_core_process_routes_tools_and_updates_history() -> None:
    session_manager = SessionManager()
    tool_router = ToolRouter()
    engine = StubEngine()
    core = AgentCore(
        llm_adapter=StubLLMAdapter(),
        engine=engine,
        session_manager=session_manager,
        tool_router=tool_router,
    )

    response = asyncio.run(
        core.process(
            AgentRequest(
                session_id="session-1",
                message="创建一个立方体",
            )
        )
    )

    session = session_manager.get_session("session-1")

    assert response.status.value == "success"
    assert response.message == "正在创建立方体"
    assert response.tool_calls[0].tool_name == "create_object"
    assert len(engine.requests) == 1
    assert engine.requests[0].capability == "blender.create_object"
    assert session is not None
    assert session.history[0]["role"] == "user"
    assert session.history[0]["content"] == "创建一个立方体"
    assert session.history[1]["role"] == "assistant"
    assert session.history[1]["tool_calls"][0]["tool_name"] == "create_object"
    assert session.history[2]["role"] == "tool"
    assert session.history[2]["content"] == "blender.create_object"


def test_agent_core_returns_failed_response_for_unknown_tool() -> None:
    class UnknownToolLLM:
        async def generate_response(self, *, request, session, tools):
            return {
                "message": "我要调用一个不存在的工具",
                "tool_calls": [{"tool_name": "missing_tool", "arguments": {}}],
            }

    core = AgentCore(
        llm_adapter=UnknownToolLLM(),
        engine=StubEngine(),
        session_manager=SessionManager(),
        tool_router=ToolRouter(),
    )

    response = asyncio.run(core.process(AgentRequest(session_id="session-2", message="test")))

    assert response.status.value == "failed"
    assert response.error is not None
    assert "missing_tool" in response.error
