from __future__ import annotations

from fastapi.testclient import TestClient
from src.app import create_app


def build_client() -> TestClient:
    app = create_app()
    return TestClient(app)


def test_streaming_chat_end_to_end() -> None:
    with build_client() as client:
        with client.websocket_connect("/ws/chat") as websocket:
            system_event = websocket.receive_json()
            assert system_event["type"] == "system"

            websocket.send_json({"type": "message", "user": "e2e", "message": "请创建一个测试立方体"})

            token_count = 0
            done_reply = ""
            for _ in range(60):
                event = websocket.receive_json()
                if event["type"] == "token":
                    token_count += 1
                if event["type"] == "done":
                    done_reply = str(event["reply"])
                    break

            assert token_count > 0
            assert done_reply

        history_response = client.get("/api/history?limit=20")
        assert history_response.status_code == 200
        items = history_response.json()["items"]
        assert any(item["role"] == "user" and "测试立方体" in item["message"] for item in items)
        assert any(item["role"] == "assistant" for item in items)
