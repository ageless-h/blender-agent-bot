from __future__ import annotations

import argparse
import logging
from typing import Sequence, cast

from config.setup_generator import TargetName, generate_setup_config
from server.mcp_server import (
    AgentCorePlanner,
    MCPFrontendServer,
    PassthroughAgentCorePlanner,
)


def build_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="blender-mcp", description="Blender Frontend MCP CLI"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    setup_parser = subparsers.add_parser("setup", help="Generate MCP client config")
    setup_parser.add_argument(
        "target",
        choices=["cursor", "claude-desktop", "windsurf", "vscode", "generic"],
        help="Target MCP client",
    )
    setup_parser.add_argument(
        "--output-root", default=None, help="Output root directory"
    )
    setup_parser.add_argument(
        "--python-path", default=None, help="Python executable path"
    )
    setup_parser.add_argument("--transport", choices=["stdio", "sse"], default="stdio")
    setup_parser.add_argument(
        "--server-name", default="blender-mcp", help="Server name"
    )
    setup_parser.add_argument(
        "--enable-agent-core",
        action="store_true",
        help="Enable Agent Core routing flag",
    )
    setup_parser.set_defaults(handler=_handle_setup)

    serve_parser = subparsers.add_parser("serve", help="Run MCP frontend server")
    serve_parser.add_argument("--transport", choices=["stdio", "sse"], default="stdio")
    serve_parser.add_argument("--host", default="127.0.0.1")
    serve_parser.add_argument("--port", type=int, default=8765)
    serve_parser.add_argument("--sse-path", default="/sse")
    serve_parser.add_argument("--messages-path", default="/messages/")
    serve_parser.add_argument("--server-name", default="blender-mcp")
    serve_parser.add_argument("--server-version", default="0.1.0")
    serve_parser.add_argument("--log-level", default="INFO")
    serve_parser.add_argument("--enable-agent-core", action="store_true")
    serve_parser.set_defaults(handler=_handle_serve)

    return parser


def _handle_setup(args: argparse.Namespace) -> int:
    target = cast(TargetName, args.target)
    generated = generate_setup_config(
        target=target,
        output_root=args.output_root,
        python_path=args.python_path,
        transport=args.transport,
        enable_agent_core=args.enable_agent_core,
        server_name=args.server_name,
    )
    print(generated.path)
    return 0


def _handle_serve(args: argparse.Namespace) -> int:
    logging.basicConfig(
        level=getattr(logging, str(args.log_level).upper(), logging.INFO),
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )
    planner: AgentCorePlanner | None = (
        PassthroughAgentCorePlanner() if args.enable_agent_core else None
    )

    server = MCPFrontendServer(
        server_name=args.server_name,
        server_version=args.server_version,
        agent_core_planner=planner,
    )
    server.run(
        transport=args.transport,
        host=args.host,
        port=args.port,
        sse_path=args.sse_path,
        messages_path=args.messages_path,
        log_level=str(args.log_level).lower(),
    )
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_argument_parser()
    args = parser.parse_args(list(argv) if argv is not None else None)
    handler = getattr(args, "handler", None)
    if handler is None:
        parser.print_help()
        return 2
    return int(handler(args))


if __name__ == "__main__":
    raise SystemExit(main())
