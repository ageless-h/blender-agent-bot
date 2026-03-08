from __future__ import annotations

import argparse
import logging
from typing import Any, Mapping, Protocol

import anyio
from mcp.server import NotificationOptions, Server
from mcp.server import sse as mcp_sse
from mcp.server import stdio as mcp_stdio

from .resource_provider import ResourceProvider
from .tool_provider import ToolExecutionError, ToolProvider

LOGGER = logging.getLogger(__name__)


class AgentCorePlanner(Protocol):
    async def plan_tool_call(self, tool_name: str, arguments: Mapping[str, Any]) -> tuple[str, dict[str, Any]]: ...


class PassthroughAgentCorePlanner:
    async def plan_tool_call(self, tool_name: str, arguments: Mapping[str, Any]) -> tuple[str, dict[str, Any]]:
        return tool_name, dict(arguments)


class MCPFrontendServer:
    def __init__(
        self,
        *,
        server_name: str = "blender-mcp",
        server_version: str = "0.1.0",
        instructions: str | None = None,
        tool_provider: ToolProvider | None = None,
        resource_provider: ResourceProvider | None = None,
        agent_core_planner: AgentCorePlanner | None = None,
    ) -> None:
        self.tool_provider = tool_provider or ToolProvider()
        self.resource_provider = resource_provider or ResourceProvider()
        self.agent_core_planner = agent_core_planner

        self.server = Server(
            name=server_name,
            version=server_version,
            instructions=instructions
            or "Blender MCP frontend. Provides 26 tools and 3 resources for Blender scene interaction.",
        )
        self._register_handlers()

    def _register_handlers(self) -> None:
        @self.server.list_tools()
        async def handle_list_tools() -> list[Any]:
            return self.tool_provider.list_tools()

        @self.server.call_tool()
        async def handle_call_tool(
            name: str,
            arguments: dict[str, Any] | None,
        ) -> list[Any]:
            target_name, target_arguments = await self._resolve_tool_call(name, arguments or {})

            try:
                result = await self.tool_provider.call_tool(target_name, target_arguments)
            except ToolExecutionError:
                raise

            if not self.tool_provider.is_read_only(target_name):
                await self._notify_mutation_resource_updates()

            return result

        @self.server.list_resources()
        async def handle_list_resources() -> list[Any]:
            return self.resource_provider.list_resources()

        @self.server.read_resource()
        async def handle_read_resource(uri: Any) -> list[Any]:
            return await self.resource_provider.read_resource(str(uri))

    async def _resolve_tool_call(
        self,
        tool_name: str,
        arguments: Mapping[str, Any],
    ) -> tuple[str, dict[str, Any]]:
        if self.agent_core_planner is None:
            return tool_name, dict(arguments)

        try:
            resolved_name, resolved_arguments = await self.agent_core_planner.plan_tool_call(tool_name, arguments)
            return resolved_name, resolved_arguments
        except Exception as error:
            LOGGER.warning("Agent Core 规划失败，降级直连执行: %s", error)
            return tool_name, dict(arguments)

    async def _notify_mutation_resource_updates(self) -> None:
        self.resource_provider.invalidate_viewport_cache()
        try:
            session = self.server.request_context.session
        except LookupError:
            return
        await self.resource_provider.notify_default_resources_changed(session)

    def create_initialization_options(self):
        return self.server.create_initialization_options(
            notification_options=NotificationOptions(
                resources_changed=True,
                tools_changed=False,
                prompts_changed=False,
            ),
            experimental_capabilities={
                "agentCore": {
                    "enabled": bool(self.agent_core_planner),
                }
            },
        )

    async def serve_stdio(self) -> None:
        initialization_options = self.create_initialization_options()
        async with mcp_stdio.stdio_server() as (read_stream, write_stream):
            await self.server.run(read_stream, write_stream, initialization_options)

    async def serve_sse(
        self,
        *,
        host: str = "127.0.0.1",
        port: int = 8765,
        sse_path: str = "/sse",
        messages_path: str = "/messages/",
        log_level: str = "info",
    ) -> None:
        try:
            import uvicorn
            from starlette.applications import Starlette
            from starlette.responses import Response
            from starlette.routing import Mount, Route
        except ImportError as error:
            raise RuntimeError("SSE 模式依赖 starlette + uvicorn，请先安装。") from error

        normalized_sse_path = sse_path if sse_path.startswith("/") else f"/{sse_path}"
        normalized_messages_path = messages_path if messages_path.startswith("/") else f"/{messages_path}"
        if not normalized_messages_path.endswith("/"):
            normalized_messages_path = f"{normalized_messages_path}/"

        transport = mcp_sse.SseServerTransport(normalized_messages_path)
        initialization_options = self.create_initialization_options()

        async def handle_sse(request: Any):
            send = getattr(request, "_send", None)
            if send is None:
                raise RuntimeError("SSE 请求对象缺少 send 通道")
            async with transport.connect_sse(request.scope, request.receive, send) as streams:
                await self.server.run(streams[0], streams[1], initialization_options)
            return Response()

        app = Starlette(
            routes=[
                Route(normalized_sse_path, endpoint=handle_sse, methods=["GET"]),
                Mount(normalized_messages_path, app=transport.handle_post_message),
            ]
        )
        config = uvicorn.Config(app=app, host=host, port=port, log_level=log_level)
        uvicorn_server = uvicorn.Server(config)
        await uvicorn_server.serve()

    def run(
        self,
        *,
        transport: str = "stdio",
        host: str = "127.0.0.1",
        port: int = 8765,
        sse_path: str = "/sse",
        messages_path: str = "/messages/",
        log_level: str = "info",
    ) -> None:
        normalized_transport = transport.strip().lower()
        if normalized_transport == "stdio":
            anyio.run(self.serve_stdio)
            return
        if normalized_transport == "sse":
            anyio.run(
                lambda: self.serve_sse(
                    host=host,
                    port=port,
                    sse_path=sse_path,
                    messages_path=messages_path,
                    log_level=log_level,
                )
            )
            return
        raise ValueError(f"不支持的 transport: {transport}")


def build_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Blender Frontend MCP Server")
    parser.add_argument("--transport", choices=["stdio", "sse"], default="stdio")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--sse-path", default="/sse")
    parser.add_argument("--messages-path", default="/messages/")
    parser.add_argument("--server-name", default="blender-mcp")
    parser.add_argument("--server-version", default="0.1.0")
    parser.add_argument("--log-level", default="INFO")
    parser.add_argument("--enable-agent-core", action="store_true")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_argument_parser()
    args = parser.parse_args(argv)

    logging.basicConfig(
        level=getattr(logging, str(args.log_level).upper(), logging.INFO),
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )

    planner: AgentCorePlanner | None = PassthroughAgentCorePlanner() if args.enable_agent_core else None

    server = MCPFrontendServer(
        server_name=args.server_name,
        server_version=args.server_version,
        agent_core_planner=planner,
    )

    try:
        server.run(
            transport=args.transport,
            host=args.host,
            port=args.port,
            sse_path=args.sse_path,
            messages_path=args.messages_path,
            log_level=str(args.log_level).lower(),
        )
    except KeyboardInterrupt:
        LOGGER.info("收到中断信号，MCP Server 已退出")
        return 130

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
