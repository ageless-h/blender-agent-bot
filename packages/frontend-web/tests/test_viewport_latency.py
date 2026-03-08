from __future__ import annotations

from datetime import datetime, timezone
from time import perf_counter

from fastapi.testclient import TestClient
from src.app import create_app


def build_client() -> TestClient:
    app = create_app()
    return TestClient(app)


def test_viewport_push_latency_interval() -> None:
    with build_client() as client:
        with client.websocket_connect("/ws/viewport?interval=0.2") as websocket:
            system_event = websocket.receive_json()
            assert system_event["type"] == "system"

            receive_times: list[float] = []
            end_to_end_latency_seconds: list[float] = []
            for _ in range(3):
                frame = websocket.receive_json()
                assert frame["type"] == "viewport"
                receive_times.append(perf_counter())

                generated_at = datetime.fromisoformat(frame["data"]["generated_at"])
                now_utc = datetime.now(timezone.utc)
                end_to_end_latency_seconds.append((now_utc - generated_at.astimezone(timezone.utc)).total_seconds())

    deltas = [receive_times[index] - receive_times[index - 1] for index in range(1, len(receive_times))]
    avg_delta = sum(deltas) / len(deltas)
    assert avg_delta <= 0.6

    avg_e2e = sum(end_to_end_latency_seconds) / len(end_to_end_latency_seconds)
    assert avg_e2e <= 1.5
