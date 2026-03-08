from __future__ import annotations

from typing import Any

from fastapi.testclient import TestClient
from src.app import create_app


def build_client() -> TestClient:
    app = create_app()
    return TestClient(app)


def _receive_signal_type(websocket, expected_type: str) -> dict[str, Any]:
    for _ in range(20):
        event = websocket.receive_json()
        if event.get("type") != "signal":
            continue
        payload = event.get("payload", {})
        if isinstance(payload, dict) and payload.get("type") == expected_type:
            return event
    raise AssertionError(f"signal {expected_type} not received")


def test_webrtc_signaling_offer_and_candidate_relay() -> None:
    with build_client() as client:
        with (
            client.websocket_connect("/ws/webrtc/room-a?peer_id=peer-a") as ws_a,
            client.websocket_connect("/ws/webrtc/room-a?peer_id=peer-b") as ws_b,
        ):
            event_a = ws_a.receive_json()
            event_b = ws_b.receive_json()
            assert event_a["type"] == "system"
            assert event_b["type"] == "system"

            ws_a.send_json({"type": "offer", "sdp": "dummy-offer", "target": "peer-b"})
            relayed_offer = _receive_signal_type(ws_b, "offer")
            assert relayed_offer["type"] == "signal"
            assert relayed_offer["from"] == "peer-a"
            assert relayed_offer["payload"]["type"] == "offer"

            ws_b.send_json(
                {
                    "type": "candidate",
                    "target": "peer-a",
                    "candidate": {"candidate": "candidate:1 1 UDP 1 127.0.0.1 9999 typ host"},
                }
            )
            relayed_candidate = _receive_signal_type(ws_a, "candidate")
            assert relayed_candidate["type"] == "signal"
            assert relayed_candidate["from"] == "peer-b"
            assert relayed_candidate["payload"]["type"] == "candidate"


def test_webrtc_duplicate_peer_id_rejected() -> None:
    with build_client() as client:
        with client.websocket_connect("/ws/webrtc/room-dup?peer_id=same-peer") as ws_first:
            assert ws_first.receive_json()["type"] == "system"

            with client.websocket_connect("/ws/webrtc/room-dup?peer_id=same-peer") as ws_second:
                error_event = ws_second.receive_json()
                assert error_event["type"] == "error"
                assert "peer_id" in str(error_event["message"])
