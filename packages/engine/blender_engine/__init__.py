"""Blender Engine - Core execution layer for Blender operations.

This package provides the core Engine layer that executes capabilities
in Blender. It's completely frontend-agnostic and uses the unified
EngineRequest/EngineResponse protocol defined in shared/protocol.
"""

from __future__ import annotations

__version__ = "0.1.0"

from .engine import BlenderEngine
from .adapters.base import BlenderAdapter
from .adapters.socket import SocketAdapter
from .adapters.mock import MockAdapter
from .adapters.stdio import StdioAdapter

__all__ = [
    "BlenderEngine",
    "BlenderAdapter",
    "SocketAdapter",
    "MockAdapter",
    "StdioAdapter",
]
