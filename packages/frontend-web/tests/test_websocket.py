from __future__ import annotations

from fastapi.testclient import TestClient
from src.app import create_app


def build_client() -> TestClient:
    app = create_app()
    return TestClient(app)


def test_chat_websocket_streaming() -> None:
    with build_client() as client:
        with client.websocket_connect("/ws/chat") as websocket:
            hello = websocket.receive_json()
            assert hello["type"] == "system"

            websocket.send_json({"type": "message", "user": "alice", "message": "你好 websocket"})

            event_types: list[str] = []
            for _ in range(20):
                event = websocket.receive_json()
                event_types.append(event["type"])
                if event["type"] == "done":
                    assert "流式响应" in event["reply"]
                    break

            assert "chat_message" in event_types
            assert "token" in event_types


def test_viewport_websocket_push() -> None:
    with build_client() as client:
        with client.websocket_connect("/ws/viewport?interval=0.2") as websocket:
            hello = websocket.receive_json()
            assert hello["type"] == "system"

            frame = websocket.receive_json()
            assert frame["type"] == "viewport"
            assert "image_base64" in frame["data"]
