from __future__ import annotations

import pytest

from conftest import load_module_from_repo


message_handler = load_module_from_repo("bridge/message_handler.py", "frontend_blender_message_handler")


def test_encode_decode_round_trip() -> None:
    payload = {"type": "chat", "request_id": "abc123", "message": "你好"}
    encoded = message_handler.encode_message(payload)
    decoded = message_handler.decode_message(encoded)
    assert decoded == payload


def test_decode_invalid_json_raises() -> None:
    with pytest.raises(message_handler.MessageCodecError):
        message_handler.decode_message("{bad-json")


def test_parse_error_message_priority() -> None:
    payload = {"error": {"code": "E_TIMEOUT", "message": "请求超时"}}
    assert message_handler.parse_error_message(payload) == "[E_TIMEOUT] 请求超时"

    payload = {"error": "直接错误"}
    assert message_handler.parse_error_message(payload) == "直接错误"

    payload = {"message": "普通消息"}
    assert message_handler.parse_error_message(payload) == "普通消息"


def test_stream_assembler_lifecycle() -> None:
    assembler = message_handler.StreamAssembler()
    assert assembler.append("r1", "A") == "A"
    assert assembler.append("r1", "B") == "AB"
    assert assembler.finalize("r1") == "AB"
    assert assembler.finalize("r1", fallback="fallback") == "fallback"


def test_message_queue_drain() -> None:
    queue = message_handler.MessageQueue()
    queue.put({"event": "one"})
    queue.put({"event": "two"})

    first = queue.get(timeout=0.01)
    assert first == {"event": "one"}

    drained = queue.drain(limit=10)
    assert drained == [{"event": "two"}]
