"""MCP Server adapter using BlenderEngine."""

from __future__ import annotations

import json
import logging
import sys
from typing import Any

logger = logging.getLogger(__name__)


class MCPServer:
    def __init__(self, engine: Any = None):
        if engine is None:
            from blender_engine import BlenderEngine

            engine = BlenderEngine()
        self._engine = engine

        # Import protocol types
        try:
            from protocol import EngineRequest, EngineRequestType, EngineResponseStatus
        except ImportError:
            # Fallback for development
            import importlib.util
            from pathlib import Path

            shared_path = Path(__file__).parent.parent.parent.parent / "shared"
            engine_protocol_path = shared_path / "protocol" / "engine_protocol.py"

            if engine_protocol_path.exists():
                spec = importlib.util.spec_from_file_location("engine_protocol", engine_protocol_path)
                if spec and spec.loader:
                    engine_protocol = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(engine_protocol)
                    EngineRequest = engine_protocol.EngineRequest
                    EngineRequestType = engine_protocol.EngineRequestType
                    EngineResponseStatus = engine_protocol.EngineResponseStatus

                    # Rebuild models with correct namespace
                    EngineRequest.model_rebuild(
                        _types_namespace={
                            "EngineRequestType": EngineRequestType,
                            "Any": Any,
                        }
                    )
            else:
                raise ImportError("Cannot find engine_protocol module")

        self._EngineRequest = EngineRequest
        self._EngineRequestType = EngineRequestType
        self._EngineResponseStatus = EngineResponseStatus

        from .tool_registry import TOOL_DEFINITIONS, get_tool

        self._tool_definitions = TOOL_DEFINITIONS
        self._get_tool = get_tool

        from .prompts.registry import BLENDER_PROMPTS, get_prompt_messages

        self._prompts = BLENDER_PROMPTS
        self._get_prompt_messages = get_prompt_messages

    def tools_list(self) -> dict[str, Any]:
        tools = []
        for tool_def in self._tool_definitions:
            tool_entry: dict[str, Any] = {
                "name": tool_def["name"],
                "description": tool_def["description"],
                "inputSchema": tool_def["inputSchema"],
            }
            if "annotations" in tool_def:
                tool_entry["annotations"] = tool_def["annotations"]
            tools.append(tool_entry)
        return {"tools": tools}

    def tools_call(self, name: str, arguments: dict[str, Any]) -> dict[str, Any]:
        if not name or not isinstance(name, str):
            return {
                "content": [
                    {
                        "type": "text",
                        "text": "Error: 'name' is required and must be a string",
                    }
                ],
                "isError": True,
            }
        if not isinstance(arguments, dict):
            arguments = {}

        tool_def = self._get_tool(name)
        if tool_def is None:
            return {
                "content": [{"type": "text", "text": f"Error: Unknown tool '{name}'"}],
                "isError": True,
            }

        internal_capability = tool_def["internal_capability"]
        logger.info("tools/call %s (capability=%s)", name, internal_capability)

        # Use Pydantic protocol
        request = self._EngineRequest(
            request_type=self._EngineRequestType.EXECUTE_CAPABILITY,
            capability=internal_capability,
            payload=arguments,
        )
        response = self._engine.execute_request(request)

        if response.status == self._EngineResponseStatus.SUCCESS:
            return {
                "content": [
                    {
                        "type": "text",
                        "text": json.dumps(response.result, indent=2),
                    }
                ]
            }
        elif response.status == self._EngineResponseStatus.BLOCKED:
            return {
                "content": [{"type": "text", "text": response.error}],
                "isError": True,
            }
        else:
            return {
                "content": [
                    {
                        "type": "text",
                        "text": f"Error: {response.error}",
                    }
                ],
                "isError": True,
            }

    def prompts_list(self) -> dict[str, Any]:
        prompts = []
        for prompt_def in self._prompts:
            prompts.append(
                {
                    "name": prompt_def["name"],
                    "description": prompt_def["description"],
                    "arguments": prompt_def.get("arguments", []),
                }
            )
        return {"prompts": prompts}

    def prompts_get(self, name: str, arguments: dict[str, Any]) -> dict[str, Any]:
        messages = self._get_prompt_messages(name, arguments)
        if messages is None:
            return {
                "messages": [],
                "description": f"Unknown prompt: {name}",
            }
        return {"messages": messages}


def run_mcp_server() -> None:
    import os

    level_name = os.environ.get("MCP_LOG_LEVEL", "WARNING").upper()
    level = getattr(logging, level_name, logging.WARNING)
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        stream=sys.stderr,
    )

    server = MCPServer()

    for line in sys.stdin:
        try:
            request = json.loads(line)
            method = request.get("method")
            params = request.get("params", {})
            request_id = request.get("id")

            if method == "tools/list":
                result = server.tools_list()
            elif method == "tools/call":
                result = server.tools_call(
                    params.get("name", ""),
                    params.get("arguments", {}),
                )
            elif method == "prompts/list":
                result = server.prompts_list()
            elif method == "prompts/get":
                result = server.prompts_get(
                    params.get("name", ""),
                    params.get("arguments", {}),
                )
            else:
                result = {"error": f"Unknown method: {method}"}

            response = {
                "jsonrpc": "2.0",
                "id": request_id,
                "result": result,
            }
            print(json.dumps(response), flush=True)
        except Exception as e:
            logger.exception("Error processing request")
            error_response = {
                "jsonrpc": "2.0",
                "id": request.get("id") if "request" in locals() else None,
                "error": {"code": -32603, "message": str(e)},
            }
            print(json.dumps(error_response), flush=True)
