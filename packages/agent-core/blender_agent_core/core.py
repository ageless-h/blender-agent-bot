from __future__ import annotations

import inspect
from typing import Any, Mapping

from shared.agent_types.tool_types import ToolCall
from shared.protocol import (
    AgentRequest,
    AgentResponse,
    EngineResponse,
    EngineResponseStatus,
    ResponseStatus,
)

from .router.tool_router import ToolRouter
from .session.session_manager import Session, SessionManager


class AgentCore:
    """Coordinate session state, LLM output, and Engine execution."""

    def __init__(
        self,
        llm_adapter: Any,
        engine: Any,
        session_manager: SessionManager,
        tool_router: ToolRouter,
    ) -> None:
        self.llm_adapter = llm_adapter
        self.engine = engine
        self.session_manager = session_manager
        self.tool_router = tool_router

    async def process(self, request: AgentRequest) -> AgentResponse:
        """Process one Agent request through the MVP coordination flow."""

        session = self.session_manager.get_session(request.session_id)
        if session is None:
            session = self.session_manager.create_session(
                request.session_id,
                context=request.context.model_dump(mode="json"),
            )
        else:
            session.context.update(request.context.model_dump(mode="json"))

        session.add_history(
            {
                "role": "user",
                "content": request.message,
                "attachments": [
                    attachment.model_dump(mode="json") for attachment in request.attachments
                ],
                "context": request.context.model_dump(mode="json"),
            }
        )

        try:
            llm_message, tool_calls = await self._invoke_llm(request, session)
            session.add_history(
                {
                    "role": "assistant",
                    "content": llm_message,
                    "tool_calls": [tool_call.model_dump(mode="json") for tool_call in tool_calls],
                }
            )

            for tool_call in tool_calls:
                engine_request = self.tool_router.map_to_engine(
                    tool_call.tool_name, tool_call.arguments
                )
                engine_response = await self._execute_engine_request(engine_request)
                self._raise_for_engine_error(engine_response)
                session.add_history(
                    {
                        "role": "tool",
                        "content": engine_response.capability or tool_call.tool_name,
                        "result": engine_response.result,
                        "status": engine_response.status.value,
                    }
                )

            return AgentResponse(
                session_id=request.session_id,
                message=llm_message,
                tool_calls=tool_calls,
                status=ResponseStatus.SUCCESS,
            )
        except Exception as error:
            return AgentResponse(
                session_id=request.session_id,
                message="Agent request processing failed.",
                status=ResponseStatus.FAILED,
                error=str(error),
            )

    async def _invoke_llm(
        self, request: AgentRequest, session: Session
    ) -> tuple[str, list[ToolCall]]:
        tools = self.tool_router.list_tools()

        if hasattr(self.llm_adapter, "generate_response"):
            llm_result = self.llm_adapter.generate_response(
                request=request, session=session, tools=tools
            )
        elif hasattr(self.llm_adapter, "generate"):
            llm_result = self.llm_adapter.generate(messages=session.history, tools=tools)
        else:
            raise TypeError("LLM adapter must define generate_response() or generate()")

        resolved_result = await self._maybe_await(llm_result)
        return self._normalize_llm_result(resolved_result)

    async def _execute_engine_request(self, engine_request: Any) -> EngineResponse:
        if hasattr(self.engine, "execute_request"):
            engine_result = self.engine.execute_request(engine_request)
        elif hasattr(self.engine, "execute_capability"):
            engine_result = self.engine.execute_capability(
                engine_request.capability, engine_request.payload
            )
        else:
            raise TypeError("Engine must define execute_request() or execute_capability()")

        resolved_result = await self._maybe_await(engine_result)
        if isinstance(resolved_result, EngineResponse):
            return resolved_result
        if isinstance(resolved_result, Mapping):
            return EngineResponse.model_validate(resolved_result)
        raise TypeError("Engine result must be an EngineResponse or mapping")

    def _normalize_llm_result(self, llm_result: Any) -> tuple[str, list[ToolCall]]:
        if isinstance(llm_result, AgentResponse):
            return llm_result.message, llm_result.tool_calls

        if isinstance(llm_result, Mapping):
            message = str(llm_result.get("message", llm_result.get("text", "")))
            tool_calls = self._normalize_tool_calls(llm_result.get("tool_calls", []))
            return message, tool_calls

        message = getattr(llm_result, "message", getattr(llm_result, "text", ""))
        tool_calls = self._normalize_tool_calls(getattr(llm_result, "tool_calls", []))
        return str(message), tool_calls

    def _normalize_tool_calls(self, tool_calls: Any) -> list[ToolCall]:
        normalized_calls: list[ToolCall] = []
        for tool_call in tool_calls or []:
            if isinstance(tool_call, ToolCall):
                normalized_calls.append(tool_call)
                continue

            if isinstance(tool_call, Mapping):
                tool_name = tool_call.get("tool_name", tool_call.get("name"))
                if tool_name is None:
                    raise ValueError("tool call is missing a tool name")
                arguments = tool_call.get("arguments", {})
                normalized_calls.append(
                    ToolCall(tool_name=str(tool_name), arguments=dict(arguments))
                )
                continue

            tool_name = getattr(tool_call, "tool_name", getattr(tool_call, "name", None))
            if tool_name is None:
                raise ValueError("tool call is missing a tool name")
            arguments = getattr(tool_call, "arguments", {})
            normalized_calls.append(ToolCall(tool_name=str(tool_name), arguments=dict(arguments)))

        return normalized_calls

    def _raise_for_engine_error(self, engine_response: EngineResponse) -> None:
        if engine_response.status != EngineResponseStatus.SUCCESS:
            raise RuntimeError(engine_response.error or "engine request failed")

    async def _maybe_await(self, value: Any) -> Any:
        if inspect.isawaitable(value):
            return await value
        return value
