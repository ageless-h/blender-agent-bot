from __future__ import annotations

import asyncio
import json
from collections import defaultdict
from datetime import datetime
from typing import Any
from uuid import uuid4

from fastapi import APIRouter, WebSocket, WebSocketDisconnect, status

from src.api.auth import get_auth_config
from src.backend_client import AgentCoreClient, resolve_viewport_image
from src.store import RuntimeStore, utc_iso_now

router = APIRouter(tags=["ws"])


class ConnectionManager:
    def __init__(self) -> None:
        self._channels: dict[str, set[WebSocket]] = defaultdict(set)
        self._lock = asyncio.Lock()

    async def connect(self, channel: str, websocket: WebSocket) -> None:
        await websocket.accept()
        async with self._lock:
            self._channels[channel].add(websocket)

    async def disconnect(self, channel: str, websocket: WebSocket) -> None:
        async with self._lock:
            if channel in self._channels:
                self._channels[channel].discard(websocket)
                if not self._channels[channel]:
                    self._channels.pop(channel, None)

    @property
    def total_connections(self) -> int:
        return sum(len(items) for items in self._channels.values())

    async def broadcast(self, channel: str, payload: dict[str, Any]) -> None:
        async with self._lock:
            clients = list(self._channels.get(channel, set()))
        stale: list[WebSocket] = []
        for websocket in clients:
            try:
                await websocket.send_json(payload)
            except RuntimeError:
                stale.append(websocket)
        if stale:
            async with self._lock:
                for socket in stale:
                    self._channels[channel].discard(socket)


class SignalingHub:
    def __init__(self) -> None:
        self._rooms: dict[str, dict[str, WebSocket]] = defaultdict(dict)
        self._lock = asyncio.Lock()

    async def join(self, room_id: str, peer_id: str, websocket: WebSocket) -> tuple[bool, list[str]]:
        await websocket.accept()
        async with self._lock:
            peers = list(self._rooms.get(room_id, {}).keys())
            if peer_id in self._rooms[room_id]:
                return False, peers
            self._rooms[room_id][peer_id] = websocket
        return True, peers

    async def leave(self, room_id: str, peer_id: str) -> None:
        async with self._lock:
            room = self._rooms.get(room_id)
            if not room:
                return
            room.pop(peer_id, None)
            if not room:
                self._rooms.pop(room_id, None)

    async def relay(
        self, room_id: str, sender_peer_id: str, payload: dict[str, Any], target_peer_id: str | None = None
    ) -> None:
        async with self._lock:
            room = self._rooms.get(room_id, {})
            if target_peer_id:
                targets = [(target_peer_id, room.get(target_peer_id))]
            else:
                targets = [(peer_id, socket) for peer_id, socket in room.items() if peer_id != sender_peer_id]

        for peer_id, socket in targets:
            if socket is None:
                continue
            try:
                await socket.send_json(
                    {
                        "type": "signal",
                        "from": sender_peer_id,
                        "to": peer_id,
                        "payload": payload,
                        "ts": utc_iso_now(),
                    }
                )
            except RuntimeError:
                await self.leave(room_id, peer_id)


def _parse_ws_message(raw: str) -> dict[str, Any]:
    try:
        payload = json.loads(raw)
        if isinstance(payload, dict):
            return payload
    except json.JSONDecodeError:
        pass
    return {"type": "message", "message": raw}


def _stream_chunks(content: str, size: int = 10) -> list[str]:
    return [content[index : index + size] for index in range(0, len(content), size)]


def _get_backend_client(websocket: WebSocket) -> AgentCoreClient:
    client = getattr(websocket.app.state, "backend_client", None)
    if isinstance(client, AgentCoreClient):
        return client
    return AgentCoreClient.from_env()


def _ensure_ws_authorized(websocket: WebSocket) -> bool:
    cfg = get_auth_config()
    if not cfg.api_token:
        return True
    header = websocket.headers.get("authorization", "")
    query_token = websocket.query_params.get("token")
    bearer_token = ""
    if header.lower().startswith("bearer "):
        bearer_token = header[7:].strip()
    return bearer_token == cfg.api_token or query_token == cfg.api_token


async def _reject_unauthorized(websocket: WebSocket) -> None:
    await websocket.close(code=status.WS_1008_POLICY_VIOLATION, reason="invalid api token")


@router.websocket("/ws/chat")
async def chat_websocket(websocket: WebSocket) -> None:
    if not _ensure_ws_authorized(websocket):
        await _reject_unauthorized(websocket)
        return

    manager: ConnectionManager = websocket.app.state.ws_manager
    store: RuntimeStore = websocket.app.state.store
    backend = _get_backend_client(websocket)

    await manager.connect("chat", websocket)
    await websocket.send_json({"type": "system", "message": "chat connected", "ts": utc_iso_now()})
    try:
        while True:
            try:
                raw = await asyncio.wait_for(websocket.receive_text(), timeout=30)
            except asyncio.TimeoutError:
                await websocket.send_json({"type": "ping", "ts": utc_iso_now()})
                continue

            payload = _parse_ws_message(raw)
            message_type = str(payload.get("type", "message"))

            if message_type == "ping":
                await websocket.send_json({"type": "pong", "ts": utc_iso_now()})
                continue
            if message_type == "pong":
                continue

            user = str(payload.get("user", "guest"))
            text = str(payload.get("message", "")).strip()
            if not text:
                await websocket.send_json({"type": "error", "message": "message is empty"})
                continue

            user_entry = store.add_chat_message(role="user", user=user, message=text)
            await manager.broadcast("chat", {"type": "chat_message", "data": user_entry.model_dump(mode="json")})

            remote_reply = await asyncio.to_thread(backend.chat, user, text)
            reply = remote_reply or f"流式响应：已收到 {user} 的消息“{text}”。"
            for chunk in _stream_chunks(reply):
                await websocket.send_json({"type": "token", "value": chunk})
                await asyncio.sleep(0.01)

            assistant_entry = store.add_chat_message(role="assistant", user="assistant", message=reply)
            await manager.broadcast("chat", {"type": "chat_message", "data": assistant_entry.model_dump(mode="json")})
            await websocket.send_json({"type": "done", "reply": reply})
    except WebSocketDisconnect:
        pass
    finally:
        await manager.disconnect("chat", websocket)


@router.websocket("/ws/viewport")
async def viewport_websocket(websocket: WebSocket) -> None:
    if not _ensure_ws_authorized(websocket):
        await _reject_unauthorized(websocket)
        return

    manager: ConnectionManager = websocket.app.state.ws_manager
    store: RuntimeStore = websocket.app.state.store
    backend = _get_backend_client(websocket)

    await manager.connect("viewport", websocket)
    interval = max(float(websocket.query_params.get("interval", "1.5")), 0.2)
    await websocket.send_json({"type": "system", "message": "viewport connected", "ts": utc_iso_now()})
    try:
        while True:
            try:
                raw = await asyncio.wait_for(websocket.receive_text(), timeout=interval)
                payload = _parse_ws_message(raw)
                if str(payload.get("type")) == "ping":
                    await websocket.send_json({"type": "pong", "ts": utc_iso_now()})
                if str(payload.get("type")) == "interval":
                    next_interval = payload.get("seconds")
                    if isinstance(next_interval, (float, int)):
                        interval = max(float(next_interval), 0.2)
                continue
            except asyncio.TimeoutError:
                remote = await asyncio.to_thread(backend.capture_viewport)
                if remote is not None:
                    resolved = resolve_viewport_image(remote)
                    if resolved is not None:
                        mime_type, image_base64 = resolved
                        snapshot = {
                            "mime_type": mime_type,
                            "image_base64": image_base64,
                            "generated_at": utc_iso_now(),
                        }
                    else:
                        snapshot = store.viewport_snapshot()
                else:
                    snapshot = store.viewport_snapshot()
                generated_at = snapshot.get("generated_at")
                if isinstance(generated_at, datetime):
                    snapshot["generated_at"] = generated_at.isoformat()
                elif generated_at is None:
                    snapshot["generated_at"] = utc_iso_now()
                elif not isinstance(generated_at, str):
                    snapshot["generated_at"] = str(generated_at)
                await websocket.send_json({"type": "viewport", "data": snapshot})
    except WebSocketDisconnect:
        pass
    finally:
        await manager.disconnect("viewport", websocket)


@router.websocket("/ws/webrtc/{room_id}")
async def webrtc_signaling_websocket(websocket: WebSocket, room_id: str) -> None:
    if not _ensure_ws_authorized(websocket):
        await _reject_unauthorized(websocket)
        return

    peer_id = websocket.query_params.get("peer_id") or str(uuid4())
    hub = getattr(websocket.app.state, "webrtc_hub", None)
    if not isinstance(hub, SignalingHub):
        hub = SignalingHub()
        websocket.app.state.webrtc_hub = hub

    joined, existing_peers = await hub.join(room_id=room_id, peer_id=peer_id, websocket=websocket)
    if not joined:
        await websocket.send_json({"type": "error", "message": "peer_id already in use", "peer_id": peer_id})
        await websocket.close(code=4409, reason="peer_id already in use")
        return
    await websocket.send_json({"type": "system", "peer_id": peer_id, "peers": existing_peers, "room_id": room_id})
    await hub.relay(room_id=room_id, sender_peer_id=peer_id, payload={"event": "peer_join", "peer_id": peer_id})

    try:
        while True:
            try:
                raw = await asyncio.wait_for(websocket.receive_text(), timeout=30)
            except asyncio.TimeoutError:
                await websocket.send_json({"type": "ping", "ts": utc_iso_now()})
                continue

            payload = _parse_ws_message(raw)
            message_type = str(payload.get("type", "signal"))
            if message_type == "ping":
                await websocket.send_json({"type": "pong", "ts": utc_iso_now()})
                continue
            if message_type == "pong":
                continue

            target_peer_id = payload.get("target")
            if not isinstance(target_peer_id, str):
                target_peer_id = None
            await hub.relay(room_id=room_id, sender_peer_id=peer_id, payload=payload, target_peer_id=target_peer_id)
    except WebSocketDisconnect:
        pass
    finally:
        await hub.leave(room_id=room_id, peer_id=peer_id)
        await hub.relay(room_id=room_id, sender_peer_id=peer_id, payload={"event": "peer_leave", "peer_id": peer_id})
