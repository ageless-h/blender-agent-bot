from __future__ import annotations

from datetime import datetime
from pathlib import Path
from uuid import uuid4

from fastapi import APIRouter, Depends, HTTPException, Query, Request, status
from fastapi.responses import FileResponse

from src.api.auth import get_store, require_api_token
from src.backend_client import AgentCoreClient, resolve_viewport_image
from src.schemas import (
    ChatHistoryResponse,
    ChatRequest,
    ChatResponse,
    ConfirmRequest,
    ConfirmResponse,
    ExportRequest,
    ExportResponse,
    SceneResponse,
    StatusResponse,
    UndoResponse,
    ViewportResponse,
)

router = APIRouter(prefix="/api", tags=["api"])


def _needs_confirmation(message: str) -> bool:
    lowered = message.lower()
    risky_keywords = ["delete", "remove", "destroy", "reset", "清空", "删除", "重置", "覆盖"]
    return any(keyword in lowered for keyword in risky_keywords)


def _assistant_reply(message: str) -> str:
    return f"已接收指令：{message}。我会继续处理 Blender 操作并同步状态。"


def get_backend_client(request: Request) -> AgentCoreClient:
    client = getattr(request.app.state, "backend_client", None)
    if isinstance(client, AgentCoreClient):
        return client
    return AgentCoreClient.from_env()


def _scene_payload_to_response(payload: dict[str, object]) -> SceneResponse:
    scene_name = str(payload.get("name") or payload.get("scene_name") or "Scene")
    raw_objects = payload.get("objects")
    objects: list[str]
    if isinstance(raw_objects, list):
        if raw_objects and isinstance(raw_objects[0], dict):
            objects = [
                str(item.get("name")) for item in raw_objects if isinstance(item, dict) and item.get("name") is not None
            ]
        else:
            objects = [str(item) for item in raw_objects]
    else:
        objects = []

    raw_count = payload.get("object_count") or payload.get("objects_count")
    if isinstance(raw_count, int):
        object_count = raw_count
    else:
        object_count = len(objects)

    active_object = payload.get("active_object")
    if active_object is None and isinstance(payload.get("selected_objects"), list):
        selected_objects = payload.get("selected_objects")
        if isinstance(selected_objects, list) and selected_objects:
            active_object = selected_objects[0]

    return SceneResponse(
        scene_name=scene_name,
        object_count=object_count,
        objects=objects,
        active_object=str(active_object) if active_object else None,
    )


@router.post("/chat", response_model=ChatResponse, dependencies=[Depends(require_api_token)])
async def send_chat(payload: ChatRequest, request: Request) -> ChatResponse:
    store = get_store(request)
    backend = get_backend_client(request)
    store.add_chat_message(role="user", user=payload.user, message=payload.message)
    if _needs_confirmation(payload.message):
        action_id = store.create_pending_action(user=payload.user, message=payload.message)
        return ChatResponse(
            reply="检测到高风险操作，请确认后执行。", requires_confirmation=True, pending_action_id=action_id
        )

    reply = backend.chat(user=payload.user, message=payload.message) or _assistant_reply(payload.message)
    store.add_chat_message(role="assistant", user="assistant", message=reply)
    return ChatResponse(reply=reply)


@router.get("/history", response_model=ChatHistoryResponse, dependencies=[Depends(require_api_token)])
async def get_history(
    request: Request,
    limit: int = Query(default=50, ge=1, le=500),
) -> ChatHistoryResponse:
    store = get_store(request)
    return ChatHistoryResponse(items=store.list_history(limit=limit))


@router.get("/scene", response_model=SceneResponse, dependencies=[Depends(require_api_token)])
async def get_scene(request: Request) -> SceneResponse:
    store = get_store(request)
    backend = get_backend_client(request)
    remote_scene = backend.get_scene()
    if remote_scene is not None:
        return _scene_payload_to_response(remote_scene)

    return SceneResponse(
        scene_name=store.scene_name,
        object_count=len(store.objects),
        objects=store.objects,
        active_object=store.active_object,
    )


@router.get("/viewport", response_model=ViewportResponse, dependencies=[Depends(require_api_token)])
async def get_viewport(request: Request) -> ViewportResponse:
    store = get_store(request)
    backend = get_backend_client(request)
    remote_viewport = backend.capture_viewport()
    if remote_viewport is not None:
        resolved = resolve_viewport_image(remote_viewport)
        if resolved is not None:
            mime_type, image_base64 = resolved
            return ViewportResponse(
                mime_type=mime_type, image_base64=image_base64, generated_at=datetime.now().astimezone()
            )

    snapshot = store.viewport_snapshot()
    generated_at = snapshot["generated_at"]
    if not isinstance(generated_at, datetime):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="invalid viewport timestamp")
    return ViewportResponse(
        mime_type=str(snapshot["mime_type"]),
        image_base64=str(snapshot["image_base64"]),
        generated_at=generated_at,
    )


@router.post("/export", response_model=ExportResponse, dependencies=[Depends(require_api_token)])
async def export_file(payload: ExportRequest, request: Request) -> ExportResponse:
    store = get_store(request)
    backend = get_backend_client(request)

    desired_name = payload.filename or f"scene_export.{payload.format}"
    export_root = store.export_root
    candidate_path = export_root / f"real-export-{uuid4()}.{payload.format}"
    remote = backend.export_scene(fmt=payload.format, filepath=str(candidate_path))

    if remote is not None and candidate_path.exists() and candidate_path.is_file():
        meta = store.register_export_file(fmt=payload.format, filename=desired_name, path=candidate_path)
    else:
        meta = store.create_export_file(fmt=payload.format, filename=payload.filename)
    expires_at = meta["expires_at"]
    if not isinstance(expires_at, datetime):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="invalid export metadata")
    return ExportResponse(
        file_id=str(meta["id"]),
        filename=str(meta["filename"]),
        format=payload.format,
        download_url=f"/api/download/{meta['id']}",
        expires_at=expires_at,
    )


@router.get("/download/{file_id}", dependencies=[Depends(require_api_token)])
async def download_file(file_id: str, request: Request) -> FileResponse:
    store = get_store(request)
    meta = store.get_export_file(file_id=file_id)
    if meta is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="file not found")
    file_path = Path(str(meta["path"]))
    if not file_path.exists():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="file not found")
    return FileResponse(path=file_path, filename=str(meta["filename"]), media_type="application/octet-stream")


@router.get("/status", response_model=StatusResponse, dependencies=[Depends(require_api_token)])
async def get_status(request: Request) -> StatusResponse:
    store = get_store(request)
    backend = get_backend_client(request)
    manager = getattr(request.app.state, "ws_manager", None)
    connections = 0
    if manager is not None and hasattr(manager, "total_connections"):
        connections = int(manager.total_connections)

    backend_status = backend.check_health()
    backend_running = backend_status.get("status") == "running"
    return StatusResponse(
        status="running",
        agent_connected=store.agent_connected or backend_running,
        websocket_connections=connections,
        started_at=store.started_at,
        version="0.1.0",
    )


@router.post("/undo", response_model=UndoResponse, dependencies=[Depends(require_api_token)])
async def undo_action(request: Request) -> UndoResponse:
    store = get_store(request)
    backend = get_backend_client(request)
    backend.undo()
    undone = store.undo_latest_user_message()
    return UndoResponse(undone=undone is not None, undone_message=undone)


@router.post("/confirm", response_model=ConfirmResponse, dependencies=[Depends(require_api_token)])
async def confirm_action(payload: ConfirmRequest, request: Request) -> ConfirmResponse:
    store = get_store(request)
    executed, result = store.confirm_action(payload.action_id)
    return ConfirmResponse(action_id=payload.action_id, executed=executed, result=result)


@router.get("/pending", dependencies=[Depends(require_api_token)])
async def get_pending_actions(request: Request) -> dict[str, list[dict[str, str]]]:
    store = get_store(request)
    return {"items": store.get_pending_actions()}


@router.get("/webrtc/config", dependencies=[Depends(require_api_token)])
async def get_webrtc_config() -> dict[str, object]:
    return {
        "ice_servers": [{"urls": ["stun:stun.l.google.com:19302"]}],
        "signal_url_template": "/ws/webrtc/{room_id}",
        "heartbeat_seconds": 15,
    }
