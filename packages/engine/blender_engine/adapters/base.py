# -*- coding: utf-8 -*-
from __future__ import annotations

from typing import Any, Dict, Protocol, runtime_checkable

from .types import AdapterResult


@runtime_checkable
class BlenderAdapter(Protocol):
    def execute(self, capability: str, payload: Dict[str, Any]) -> AdapterResult: ...
