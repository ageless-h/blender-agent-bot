from __future__ import annotations

import base64
import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib import error, request


def _ensure_dict(value: Any) -> dict[str, Any] | None:
    if isinstance(value, dict):
        return value
    return None


def _ensure_list(value: Any) -> list[Any] | None:
    if isinstance(value, list):
        return value
    return None


@dataclass(slots=True)
class AgentCoreClient:
    endpoint: str = ""
    timeout_seconds: float = 4.0

    @classmethod
    def from_env(cls) -> "AgentCoreClient":
        endpoint = os.getenv("AGENT_CORE_URL", "").strip().rstrip("/")
        return cls(endpoint=endpoint)

    @property
    def configured(self) -> bool:
        return bool(self.endpoint)

    def check_health(self) -> dict[str, Any]:
        if not self.configured:
            return {"status": "not_configured", "endpoint": ""}

        for route in ("/health", "/status", "/v1/health"):
            payload = self._request_json("GET", f"{self.endpoint}{route}")
            if payload is not None:
                return {"status": "running", "endpoint": self.endpoint, "response": payload}
        return {"status": "unreachable", "endpoint": self.endpoint}

    def chat(self, user: str, message: str) -> str | None:
        if not self.configured:
            return None

        requests_to_try = [
            ("POST", f"{self.endpoint}/api/chat", {"user": user, "message": message}),
            ("POST", f"{self.endpoint}/chat", {"user": user, "message": message}),
            ("POST", f"{self.endpoint}/v1/chat", {"user": user, "message": message}),
        ]
        for method, url, payload in requests_to_try:
            response = self._request_json(method, url, payload)
            if response is None:
                continue
            if isinstance(response, dict):
                for key in ("reply", "message", "text", "content"):
                    value = response.get(key)
                    if isinstance(value, str) and value.strip():
                        return value
            if isinstance(response, str) and response.strip():
                return response
        return None

    def get_scene(self) -> dict[str, Any] | None:
        return self.call_tool_candidates(["get_scene", "blender_get_scene"], {})

    def capture_viewport(self) -> dict[str, Any] | None:
        return self.call_tool_candidates(["capture_viewport", "blender_capture_viewport"], {})

    def export_scene(self, fmt: str, filepath: str) -> dict[str, Any] | None:
        payload = {"action": "export", "format": fmt, "filepath": filepath}
        return self.call_tool_candidates(["import_export", "blender_import_export"], payload)

    def undo(self) -> dict[str, Any] | None:
        return self.call_tool_candidates(["undo", "blender_undo"], {})

    def call_tool_candidates(self, tool_names: list[str], arguments: dict[str, Any]) -> dict[str, Any] | None:
        if not self.configured:
            return None

        for tool_name in tool_names:
            response = self._call_tool(tool_name, arguments)
            if response is not None:
                return response
        return None

    def _call_tool(self, tool_name: str, arguments: dict[str, Any]) -> dict[str, Any] | None:
        requests_to_try = [
            ("POST", f"{self.endpoint}/tools/call", {"tool": tool_name, "args": arguments}),
            ("POST", f"{self.endpoint}/tools/call", {"tool_name": tool_name, "arguments": arguments}),
            ("POST", f"{self.endpoint}/tools/{tool_name}", arguments),
            ("POST", f"{self.endpoint}/call", {"name": tool_name, "arguments": arguments}),
        ]
        for method, url, payload in requests_to_try:
            response = self._request_json(method, url, payload)
            extracted = self._extract_tool_payload(response)
            if extracted is not None:
                return extracted
        return None

    def _extract_tool_payload(self, response: Any) -> dict[str, Any] | None:
        as_dict = _ensure_dict(response)
        if as_dict is None:
            return None

        tool_results = _ensure_list(as_dict.get("tool_results"))
        if tool_results:
            for item in tool_results:
                row = _ensure_dict(item)
                if row is None:
                    continue
                if row.get("success") is True:
                    payload = _ensure_dict(row.get("data"))
                    if payload is not None:
                        return payload

        for key in ("data", "result", "payload"):
            payload = _ensure_dict(as_dict.get(key))
            if payload is not None:
                return payload

        if as_dict.get("success") is True:
            return as_dict
        return None

    def _request_json(self, method: str, url: str, payload: dict[str, Any] | None = None) -> Any:
        body = None
        headers: dict[str, str] = {}
        if payload is not None:
            body = json.dumps(payload).encode("utf-8")
            headers["Content-Type"] = "application/json"

        try:
            req = request.Request(url=url, data=body, headers=headers, method=method)
            with request.urlopen(req, timeout=self.timeout_seconds) as response:  # noqa: S310
                raw = response.read()
        except (error.URLError, error.HTTPError, TimeoutError, ValueError):
            return None

        if not raw:
            return {}

        try:
            return json.loads(raw.decode("utf-8"))
        except json.JSONDecodeError:
            return {"raw": raw.decode("utf-8", errors="replace")}


def resolve_viewport_image(payload: dict[str, Any]) -> tuple[str, str] | None:
    for key in ("image_base64", "base64"):
        value = payload.get(key)
        if isinstance(value, str) and value:
            mime_type = str(payload.get("mime_type") or "image/png")
            return mime_type, value

    filepath = payload.get("filepath")
    if isinstance(filepath, str) and filepath:
        path = Path(filepath)
        if path.exists() and path.is_file():
            content = path.read_bytes()
            encoded = base64.b64encode(content).decode("utf-8")
            mime_type = str(payload.get("mime_type") or "image/png")
            return mime_type, encoded
    return None
