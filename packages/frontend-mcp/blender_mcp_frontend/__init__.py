"""Blender MCP Frontend - MCP protocol adapter for BlenderAgentBot.

This package provides the MCP (Model Context Protocol) frontend that
translates MCP JSON-RPC calls into EngineRequest/EngineResponse protocol.
"""

from __future__ import annotations

__version__ = "0.1.0"

from .mcp_server import MCPServer

__all__ = ["MCPServer"]
