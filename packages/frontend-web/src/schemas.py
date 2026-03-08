from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field

ExportFormat = Literal["blend", "fbx", "glb", "obj", "stl"]
ShareMode = Literal["readonly", "interactive"]
ChatRole = Literal["user", "assistant", "system"]


class ChatRequest(BaseModel):
    user: str = Field(default="guest", min_length=1, max_length=64)
    message: str = Field(min_length=1, max_length=4000)


class ChatEntry(BaseModel):
    id: str
    role: ChatRole
    user: str
    message: str
    created_at: datetime


class ChatResponse(BaseModel):
    reply: str
    requires_confirmation: bool = False
    pending_action_id: str | None = None


class ChatHistoryResponse(BaseModel):
    items: list[ChatEntry]


class SceneResponse(BaseModel):
    scene_name: str
    object_count: int
    objects: list[str]
    active_object: str | None


class ViewportResponse(BaseModel):
    mime_type: str
    image_base64: str
    generated_at: datetime


class ExportRequest(BaseModel):
    format: ExportFormat
    filename: str | None = Field(default=None, max_length=128)


class ExportResponse(BaseModel):
    file_id: str
    filename: str
    format: ExportFormat
    download_url: str
    expires_at: datetime


class StatusResponse(BaseModel):
    status: Literal["running"]
    agent_connected: bool
    websocket_connections: int
    started_at: datetime
    version: str


class UndoResponse(BaseModel):
    undone: bool
    undone_message: ChatEntry | None = None


class ConfirmRequest(BaseModel):
    action_id: str


class ConfirmResponse(BaseModel):
    action_id: str
    executed: bool
    result: str


class ShareLinkCreateRequest(BaseModel):
    ttl_seconds: int = Field(default=900, ge=60, le=86400)
    mode: ShareMode = "readonly"


class ShareLinkCreateResponse(BaseModel):
    session_id: str
    token: str
    url_path: str
    expires_at: datetime
    mode: ShareMode


class ShareLinkVerifyRequest(BaseModel):
    token: str


class ShareLinkVerifyResponse(BaseModel):
    valid: bool
    session_id: str | None = None
    mode: ShareMode | None = None
    expires_at: datetime | None = None
