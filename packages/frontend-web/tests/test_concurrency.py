from __future__ import annotations

from fastapi.testclient import TestClient
from src.app import create_app


def build_client() -> TestClient:
    app = create_app()
    return TestClient(app)


def _receive_chat_message(websocket) -> dict[str, object]:
    for _ in range(20):
        event = websocket.receive_json()
        if event.get("type") == "chat_message":
            return event
    raise AssertionError("chat_message not received")


def test_multi_user_websocket_concurrency() -> None:
    with build_client() as client:
        with (
            client.websocket_connect("/ws/chat") as ws_a,
            client.websocket_connect("/ws/chat") as ws_b,
            client.websocket_connect("/ws/chat") as ws_c,
        ):
            assert ws_a.receive_json()["type"] == "system"
            assert ws_b.receive_json()["type"] == "system"
            assert ws_c.receive_json()["type"] == "system"

            status_response = client.get("/api/status")
            assert status_response.status_code == 200
            assert status_response.json()["websocket_connections"] >= 3

            ws_a.send_json({"type": "message", "user": "alice", "message": "并发测试消息"})

            msg_b = _receive_chat_message(ws_b)
            msg_c = _receive_chat_message(ws_c)

            assert msg_b["type"] == "chat_message"
            assert msg_c["type"] == "chat_message"
