from __future__ import annotations

from fastapi.testclient import TestClient
from src.app import create_app


def build_client() -> TestClient:
    app = create_app()
    return TestClient(app)


def test_chat_and_history() -> None:
    with build_client() as client:
        chat_response = client.post("/api/chat", json={"user": "alice", "message": "你好"})
        assert chat_response.status_code == 200
        payload = chat_response.json()
        assert payload["requires_confirmation"] is False
        assert "已接收指令" in payload["reply"]

        history_response = client.get("/api/history")
        assert history_response.status_code == 200
        rows = history_response.json()["items"]
        assert len(rows) >= 2


def test_chat_confirm_flow() -> None:
    with build_client() as client:
        chat_response = client.post("/api/chat", json={"user": "alice", "message": "请删除全部对象"})
        assert chat_response.status_code == 200
        payload = chat_response.json()
        assert payload["requires_confirmation"] is True
        action_id = payload["pending_action_id"]
        assert action_id

        pending_response = client.get("/api/pending")
        assert pending_response.status_code == 200
        pending_items = pending_response.json()["items"]
        assert any(item["id"] == action_id for item in pending_items)

        confirm_response = client.post("/api/confirm", json={"action_id": action_id})
        assert confirm_response.status_code == 200
        confirm_payload = confirm_response.json()
        assert confirm_payload["executed"] is True


def test_export_and_download() -> None:
    with build_client() as client:
        export_response = client.post("/api/export", json={"format": "glb"})
        assert export_response.status_code == 200
        payload = export_response.json()
        assert payload["format"] == "glb"

        download_response = client.get(payload["download_url"])
        assert download_response.status_code == 200
        assert download_response.content


def test_share_link_create_and_verify() -> None:
    with build_client() as client:
        create_response = client.post("/api/auth/share-link", json={"ttl_seconds": 600, "mode": "readonly"})
        assert create_response.status_code == 200
        token = create_response.json()["token"]

        verify_response = client.post("/api/auth/share-link/verify", json={"token": token})
        assert verify_response.status_code == 200
        payload = verify_response.json()
        assert payload["valid"] is True
        assert payload["mode"] == "readonly"
