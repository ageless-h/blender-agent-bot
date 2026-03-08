from __future__ import annotations

import json
from dataclasses import dataclass, field
from queue import Empty, Queue
from typing import Any, Mapping

JSONDict = dict[str, Any]


class MessageCodecError(ValueError):
    """Bridge 消息编解码失败。"""


def encode_message(payload: Mapping[str, Any]) -> str:
    """将消息对象编码为单行 JSON。"""
    if not isinstance(payload, Mapping):
        raise MessageCodecError("Bridge payload 必须是映射对象。")
    return json.dumps(dict(payload), ensure_ascii=False, separators=(",", ":"))


def decode_message(raw_line: str) -> JSONDict:
    """将单行 JSON 解码为字典消息。"""
    line = raw_line.strip()
    if not line:
        raise MessageCodecError("Bridge 消息为空。")

    try:
        decoded = json.loads(line)
    except json.JSONDecodeError as exc:
        raise MessageCodecError(f"Bridge 消息不是合法 JSON: {exc}") from exc

    if not isinstance(decoded, dict):
        raise MessageCodecError("Bridge 消息必须是 JSON 对象。")
    return decoded


def parse_error_message(payload: Mapping[str, Any]) -> str:
    """从 Agent 返回结构中提取可读错误信息。"""
    error_payload = payload.get("error")

    if isinstance(error_payload, dict):
        code = str(error_payload.get("code", "")).strip()
        message = str(error_payload.get("message", "")).strip()
        if code and message:
            return f"[{code}] {message}"
        if message:
            return message

    if isinstance(error_payload, str) and error_payload.strip():
        return error_payload.strip()

    message = payload.get("message")
    if isinstance(message, str) and message.strip():
        return message.strip()

    return "Agent Core 返回错误，但没有提供详细信息。"


@dataclass(slots=True)
class StreamChunk:
    """流式 token 事件。"""

    request_id: str
    token: str
    raw: JSONDict = field(default_factory=dict)


class StreamAssembler:
    """按 request_id 累积 token，并在完成时输出最终文本。"""

    def __init__(self) -> None:
        self._buffers: dict[str, list[str]] = {}

    def append(self, request_id: str, token: str) -> str:
        chunks = self._buffers.setdefault(request_id, [])
        chunks.append(token)
        return "".join(chunks)

    def finalize(self, request_id: str, fallback: str = "") -> str:
        chunks = self._buffers.pop(request_id, [])
        combined = "".join(chunks)
        if combined:
            return combined
        return fallback

    def discard(self, request_id: str) -> None:
        self._buffers.pop(request_id, None)


class MessageQueue:
    """线程安全消息队列，封装超时和批量排空逻辑。"""

    def __init__(self) -> None:
        self._queue: Queue[JSONDict] = Queue()

    def put(self, payload: Mapping[str, Any]) -> None:
        self._queue.put(dict(payload))

    def get(self, timeout: float | None = None) -> JSONDict | None:
        try:
            return self._queue.get(timeout=timeout)
        except Empty:
            return None

    def drain(self, limit: int = 200) -> list[JSONDict]:
        items: list[JSONDict] = []
        bounded_limit = max(limit, 0)

        for _ in range(bounded_limit):
            item = self.get(timeout=0)
            if item is None:
                break
            items.append(item)

        return items


__all__ = [
    "JSONDict",
    "MessageCodecError",
    "MessageQueue",
    "StreamAssembler",
    "StreamChunk",
    "decode_message",
    "encode_message",
    "parse_error_message",
]
