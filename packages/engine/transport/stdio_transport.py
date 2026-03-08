from __future__ import annotations

import json
import sys
from io import TextIOBase
from typing import Any, Mapping

from .base import TransportBase


class StdioTransport(TransportBase):
    def __init__(self, stdin: TextIOBase | None = None, stdout: TextIOBase | None = None) -> None:
        self.stdin = stdin or sys.stdin
        self.stdout = stdout or sys.stdout
        self._closed = False

    def send(self, payload: Mapping[str, Any], *, session_id: str | None = None) -> None:
        if self._closed:
            raise RuntimeError("transport is closed")

        envelope = dict(payload)
        if session_id is not None:
            envelope.setdefault("session_id", session_id)
        self.stdout.write(json.dumps(envelope, ensure_ascii=False) + "\n")
        self.stdout.flush()

    def receive(self, *, timeout: float | None = None, session_id: str | None = None) -> dict[str, Any] | None:
        if self._closed:
            return None

        line = self.stdin.readline()
        if not line:
            return None

        payload = dict(json.loads(line))
        if session_id is not None and payload.get("session_id") != session_id:
            return None
        return payload

    def close(self) -> None:
        self._closed = True
