from __future__ import annotations

from dataclasses import dataclass, field

from .protocol import AgentRequest, AgentResponse, ResponseStatus, ToolResult
from .tools import ToolRegistry, build_default_registry


@dataclass(slots=True)
class Engine:
    registry: ToolRegistry = field(default_factory=build_default_registry)

    def handle_request(self, request: AgentRequest) -> AgentResponse:
        request.validate()

        if request.tool_call is None:
            return AgentResponse(
                session_id=request.session_id,
                request_id=request.request_id,
                status=ResponseStatus.ERROR,
                message="当前仅支持显式 tool_call 请求",
                error="missing_tool_call",
            )

        result = self.registry.execute(request.tool_call.tool_name, request.tool_call.arguments)
        status = ResponseStatus.SUCCESS if result.success else ResponseStatus.ERROR
        message = "工具执行成功" if result.success else "工具执行失败"

        return AgentResponse(
            session_id=request.session_id,
            request_id=request.request_id,
            status=status,
            message=message,
            tool_results=[result],
            error=result.error,
        )

    def execute_tool(self, tool_name: str, arguments: dict[str, object] | None = None) -> ToolResult:
        payload = arguments or {}
        return self.registry.execute(tool_name, payload)
