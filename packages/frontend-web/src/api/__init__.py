"""API routers for frontend-web backend."""

from .auth import router as auth_router
from .routes import router as api_router
from .websocket import router as ws_router

__all__ = ["api_router", "auth_router", "ws_router"]
