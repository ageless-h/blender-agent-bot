from __future__ import annotations

import os
import socket
from contextlib import asynccontextmanager
from pathlib import Path
from urllib.parse import urlparse

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles

from src.api import api_router, auth_router, ws_router
from src.api.auth import get_auth_config
from src.api.websocket import ConnectionManager, SignalingHub
from src.backend_client import AgentCoreClient
from src.store import RuntimeStore


def _try_connect_agent_core() -> bool:
    endpoint = os.getenv("AGENT_CORE_URL", "").strip()
    if not endpoint:
        return False
    parsed = urlparse(endpoint)
    host = parsed.hostname
    if host is None:
        return False

    port = parsed.port
    if port is None:
        if parsed.scheme in {"https", "wss"}:
            port = 443
        else:
            port = 80

    try:
        with socket.create_connection((host, port), timeout=1.5):
            return True
    except OSError:
        return False


def create_app() -> FastAPI:
    @asynccontextmanager
    async def lifespan(app_instance: FastAPI):
        app_instance.state.store.set_agent_connected(_try_connect_agent_core())
        app_instance.state.backend_client = AgentCoreClient.from_env()
        get_auth_config.cache_clear()
        try:
            yield
        finally:
            app_instance.state.store.set_agent_connected(False)

    app = FastAPI(title="Blender Frontend Web API", version="0.1.0", lifespan=lifespan)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    package_root = Path(__file__).resolve().parent
    export_root = package_root / "static" / "exports"
    app.state.store = RuntimeStore(export_root=export_root)
    app.state.ws_manager = ConnectionManager()
    app.state.webrtc_hub = SignalingHub()
    app.state.backend_client = AgentCoreClient.from_env()

    @app.get("/")
    async def root() -> JSONResponse:
        return JSONResponse(
            {
                "name": "blender-frontend-web",
                "status": "running",
                "api": "/api/status",
                "websocket": ["/ws/chat", "/ws/viewport", "/ws/webrtc/{room_id}"],
            }
        )

    app.include_router(api_router)
    app.include_router(auth_router)
    app.include_router(ws_router)

    static_dir = package_root / "static"
    static_dir.mkdir(parents=True, exist_ok=True)
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

    frontend_dist = package_root.parent / "frontend" / "dist"
    if frontend_dist.exists():
        app.mount("/app", StaticFiles(directory=frontend_dist, html=True), name="frontend")

    return app


app = create_app()
