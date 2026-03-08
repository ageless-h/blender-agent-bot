# -*- coding: utf-8 -*-
from __future__ import annotations

from typing import Any, Dict

from .types import AdapterResult


class MockAdapter:
    def __init__(self) -> None:
        self._responses: Dict[str, AdapterResult] = {}

    def set_response(self, capability: str, response: AdapterResult) -> None:
        self._responses[capability] = response

    def execute(self, capability: str, payload: Dict[str, Any]) -> AdapterResult:
        if capability in self._responses:
            return self._responses[capability]
        return AdapterResult(ok=True, result={})
