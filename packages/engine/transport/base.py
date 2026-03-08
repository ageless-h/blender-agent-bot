from __future__ import annotations

import json
from abc import ABC, abstractmethod
from typing import Any, Mapping


class TransportBase(ABC):
    @abstractmethod
    def send(self, payload: Mapping[str, Any], *, session_id: str | None = None) -> None:
        raise NotImplementedError

    @abstractmethod
    def receive(self, *, timeout: float | None = None, session_id: str | None = None) -> dict[str, Any] | None:
        raise NotImplementedError

    @abstractmethod
    def close(self) -> None:
        raise NotImplementedError

    @staticmethod
    def encode_message(payload: Mapping[str, Any]) -> bytes:
        return (json.dumps(dict(payload), ensure_ascii=False) + "\n").encode("utf-8")

    @staticmethod
    def decode_message(raw_line: bytes | str) -> dict[str, Any]:
        text = raw_line.decode("utf-8") if isinstance(raw_line, bytes) else raw_line
        return dict(json.loads(text.strip()))
