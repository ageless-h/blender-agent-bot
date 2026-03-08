from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any
from uuid import uuid4


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


class SafetyLevel(str, Enum):
    LEVEL_0 = "level_0"
    LEVEL_1 = "level_1"
    LEVEL_2 = "level_2"
    LEVEL_3 = "level_3"
    FORBIDDEN = "forbidden"


class ResponseStatus(str, Enum):
    SUCCESS = "success"
    ERROR = "error"
    NEED_CONFIRM = "need_confirm"


@dataclass(slots=True)
class ToolCall:
    tool_name: str
    arguments: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {"tool_name": self.tool_name, "arguments": dict(self.arguments)}

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> "ToolCall":
        return cls(
            tool_name=str(payload.get("tool_name", "")),
            arguments=dict(payload.get("arguments", {})),
        )


@dataclass(slots=True)
class ToolResult:
    tool_name: str
    success: bool
    data: dict[str, Any] = field(default_factory=dict)
    error: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "tool_name": self.tool_name,
            "success": self.success,
            "data": dict(self.data),
            "error": self.error,
        }


@dataclass(slots=True)
class AgentRequest:
    session_id: str
    message: str | None = None
    tool_call: ToolCall | None = None
    context: dict[str, Any] = field(default_factory=dict)
    options: dict[str, Any] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)
    request_id: str = field(default_factory=lambda: str(uuid4()))
    timestamp: str = field(default_factory=_utc_now_iso)

    def validate(self) -> None:
        if not self.session_id:
            raise ValueError("session_id is required")
        if not self.message and not self.tool_call:
            raise ValueError("either message or tool_call must be provided")

    def to_dict(self) -> dict[str, Any]:
        payload = asdict(self)
        if self.tool_call is not None:
            payload["tool_call"] = self.tool_call.to_dict()
        return payload

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False)

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> "AgentRequest":
        tool_call_payload = payload.get("tool_call")
        tool_call = ToolCall.from_dict(tool_call_payload) if isinstance(tool_call_payload, dict) else None
        instance = cls(
            session_id=str(payload.get("session_id", "")),
            message=payload.get("message"),
            tool_call=tool_call,
            context=dict(payload.get("context", {})),
            options=dict(payload.get("options", {})),
            metadata=dict(payload.get("metadata", {})),
            request_id=str(payload.get("request_id", str(uuid4()))),
            timestamp=str(payload.get("timestamp", _utc_now_iso())),
        )
        instance.validate()
        return instance

    @classmethod
    def from_json(cls, payload: str) -> "AgentRequest":
        return cls.from_dict(json.loads(payload))


@dataclass(slots=True)
class AgentResponse:
    session_id: str
    status: ResponseStatus
    message: str
    tool_results: list[ToolResult] = field(default_factory=list)
    screenshots: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)
    request_id: str | None = None
    timestamp: str = field(default_factory=_utc_now_iso)
    error: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "session_id": self.session_id,
            "status": self.status.value,
            "message": self.message,
            "tool_results": [item.to_dict() for item in self.tool_results],
            "screenshots": list(self.screenshots),
            "metadata": dict(self.metadata),
            "request_id": self.request_id,
            "timestamp": self.timestamp,
            "error": self.error,
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False)

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> "AgentResponse":
        results: list[ToolResult] = []
        for item in payload.get("tool_results", []):
            if not isinstance(item, dict):
                continue
            results.append(
                ToolResult(
                    tool_name=str(item.get("tool_name", "")),
                    success=bool(item.get("success", False)),
                    data=dict(item.get("data", {})),
                    error=item.get("error"),
                )
            )

        return cls(
            session_id=str(payload.get("session_id", "")),
            status=ResponseStatus(payload.get("status", ResponseStatus.ERROR.value)),
            message=str(payload.get("message", "")),
            tool_results=results,
            screenshots=list(payload.get("screenshots", [])),
            metadata=dict(payload.get("metadata", {})),
            request_id=payload.get("request_id"),
            timestamp=str(payload.get("timestamp", _utc_now_iso())),
            error=payload.get("error"),
        )

    @classmethod
    def from_json(cls, payload: str) -> "AgentResponse":
        return cls.from_dict(json.loads(payload))
