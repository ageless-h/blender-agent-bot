from __future__ import annotations

import base64
import json
from datetime import UTC, datetime, timedelta
from pathlib import Path
from threading import RLock
from uuid import uuid4

from .schemas import ChatEntry


def utc_now() -> datetime:
    return datetime.now(tz=UTC)


def utc_iso_now() -> str:
    return utc_now().isoformat()


def generate_viewport_svg(label: str) -> str:
    svg = f"""<svg xmlns='http://www.w3.org/2000/svg' width='960' height='540'>
<defs>
  <linearGradient id='g' x1='0%' y1='0%' x2='100%' y2='100%'>
    <stop offset='0%' stop-color='#0f172a'/>
    <stop offset='100%' stop-color='#1e293b'/>
  </linearGradient>
</defs>
<rect width='100%' height='100%' fill='url(#g)'/>
<circle cx='180' cy='150' r='60' fill='#22d3ee' opacity='0.55'/>
<circle cx='760' cy='360' r='90' fill='#a78bfa' opacity='0.40'/>
<text x='48' y='70' fill='#e2e8f0' font-size='38' font-family='monospace'>Blender Viewport Preview</text>
<text x='48' y='120' fill='#94a3b8' font-size='26' font-family='monospace'>{label}</text>
</svg>"""
    return base64.b64encode(svg.encode("utf-8")).decode("utf-8")


class RuntimeStore:
    def __init__(self, export_root: Path) -> None:
        self._lock = RLock()
        self.started_at = utc_now()
        self.agent_connected = False
        self.scene_name = "Default Scene"
        self.objects = ["Camera", "Light", "Cube"]
        self.active_object = "Cube"
        self.chat_history: list[dict[str, str]] = []
        self.pending_actions: dict[str, dict[str, str]] = {}
        self.export_files: dict[str, dict[str, object]] = {}
        self.share_sessions: dict[str, dict[str, object]] = {}
        self.export_root = export_root
        self.export_root.mkdir(parents=True, exist_ok=True)

    def set_agent_connected(self, connected: bool) -> None:
        with self._lock:
            self.agent_connected = connected

    def add_chat_message(self, role: str, user: str, message: str) -> ChatEntry:
        item = {
            "id": str(uuid4()),
            "role": role,
            "user": user,
            "message": message,
            "created_at": utc_iso_now(),
        }
        with self._lock:
            self.chat_history.append(item)
            if len(self.chat_history) > 500:
                self.chat_history = self.chat_history[-500:]
        return ChatEntry.model_validate(item)

    def list_history(self, limit: int) -> list[ChatEntry]:
        with self._lock:
            rows = self.chat_history[-limit:]
        return [ChatEntry.model_validate(row) for row in rows]

    def undo_latest_user_message(self) -> ChatEntry | None:
        with self._lock:
            for index in range(len(self.chat_history) - 1, -1, -1):
                row = self.chat_history[index]
                if row["role"] == "user":
                    deleted = self.chat_history.pop(index)
                    return ChatEntry.model_validate(deleted)
        return None

    def create_pending_action(self, user: str, message: str) -> str:
        action_id = str(uuid4())
        with self._lock:
            self.pending_actions[action_id] = {
                "id": action_id,
                "user": user,
                "message": message,
                "created_at": utc_iso_now(),
            }
        return action_id

    def get_pending_actions(self) -> list[dict[str, str]]:
        with self._lock:
            return list(self.pending_actions.values())

    def confirm_action(self, action_id: str) -> tuple[bool, str]:
        with self._lock:
            action = self.pending_actions.pop(action_id, None)
        if action is None:
            return False, "未找到待确认操作"
        result = f"已执行确认操作: {action['message']}"
        self.add_chat_message(role="system", user="system", message=result)
        return True, result

    def _cleanup_exports(self) -> None:
        now = utc_now()
        expired: list[str] = []
        with self._lock:
            for file_id, meta in self.export_files.items():
                expires_at = meta["expires_at"]
                if isinstance(expires_at, datetime) and expires_at < now:
                    expired.append(file_id)
            for file_id in expired:
                meta = self.export_files.pop(file_id, None)
                if meta:
                    path = Path(str(meta["path"]))
                    if path.exists():
                        path.unlink(missing_ok=True)

    def create_export_file(self, fmt: str, filename: str | None) -> dict[str, object]:
        self._cleanup_exports()
        file_id = str(uuid4())
        safe_name = (filename or f"scene_export.{fmt}").strip() or f"scene_export.{fmt}"
        if "." not in safe_name:
            safe_name = f"{safe_name}.{fmt}"
        file_path = self.export_root / f"{file_id}-{safe_name}"
        payload = {
            "file_id": file_id,
            "format": fmt,
            "filename": safe_name,
            "created_at": utc_iso_now(),
            "scene": self.scene_name,
            "objects": self.objects,
        }
        file_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        meta = {
            "id": file_id,
            "format": fmt,
            "filename": safe_name,
            "path": str(file_path),
            "expires_at": utc_now() + timedelta(hours=1),
        }
        with self._lock:
            self.export_files[file_id] = meta
        return meta

    def register_export_file(self, fmt: str, filename: str, path: Path) -> dict[str, object]:
        self._cleanup_exports()
        file_id = str(uuid4())
        safe_name = filename.strip() or f"scene_export.{fmt}"
        if "." not in safe_name:
            safe_name = f"{safe_name}.{fmt}"
        meta = {
            "id": file_id,
            "format": fmt,
            "filename": safe_name,
            "path": str(path),
            "expires_at": utc_now() + timedelta(hours=1),
        }
        with self._lock:
            self.export_files[file_id] = meta
        return meta

    def get_export_file(self, file_id: str) -> dict[str, object] | None:
        self._cleanup_exports()
        with self._lock:
            meta = self.export_files.get(file_id)
            if not meta:
                return None
            return dict(meta)

    def create_share_session(self, mode: str, ttl_seconds: int) -> dict[str, object]:
        session_id = str(uuid4())
        expires_at = utc_now() + timedelta(seconds=ttl_seconds)
        session = {
            "session_id": session_id,
            "mode": mode,
            "expires_at": expires_at,
        }
        with self._lock:
            self.share_sessions[session_id] = session
        return session

    def get_share_session(self, session_id: str) -> dict[str, object] | None:
        with self._lock:
            session = self.share_sessions.get(session_id)
            if not session:
                return None
            if isinstance(session["expires_at"], datetime) and session["expires_at"] < utc_now():
                self.share_sessions.pop(session_id, None)
                return None
            return dict(session)

    def viewport_snapshot(self) -> dict[str, object]:
        label = f"{self.scene_name} · {utc_iso_now()}"
        return {
            "mime_type": "image/svg+xml",
            "image_base64": generate_viewport_svg(label),
            "generated_at": utc_now(),
        }
