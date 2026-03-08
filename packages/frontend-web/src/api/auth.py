from __future__ import annotations

import base64
import hashlib
import hmac
import json
import os
from datetime import UTC, datetime
from functools import lru_cache
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from src.schemas import (
    ShareLinkCreateRequest,
    ShareLinkCreateResponse,
    ShareLinkVerifyRequest,
    ShareLinkVerifyResponse,
)
from src.store import RuntimeStore

router = APIRouter(prefix="/api/auth", tags=["auth"])
bearer = HTTPBearer(auto_error=False)


class AuthConfig:
    def __init__(self, api_token: str, share_secret: str) -> None:
        self.api_token = api_token
        self.share_secret = share_secret


@lru_cache
def get_auth_config() -> AuthConfig:
    api_token = os.getenv("FRONTEND_WEB_API_TOKEN", "").strip()
    share_secret = os.getenv("FRONTEND_WEB_SHARE_SECRET", "frontend-web-dev-secret")
    return AuthConfig(api_token=api_token, share_secret=share_secret)


def get_store(request: Request) -> RuntimeStore:
    store = getattr(request.app.state, "store", None)
    if not isinstance(store, RuntimeStore):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="runtime store not initialized")
    return store


def require_api_token(credentials: HTTPAuthorizationCredentials | None = Depends(bearer)) -> bool:
    cfg = get_auth_config()
    if not cfg.api_token:
        return True
    if credentials is None or credentials.credentials != cfg.api_token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid api token")
    return True


def _sign_payload(payload_base64: str) -> str:
    cfg = get_auth_config()
    digest = hmac.new(cfg.share_secret.encode("utf-8"), payload_base64.encode("utf-8"), hashlib.sha256).hexdigest()
    return digest


def encode_share_token(payload: dict[str, Any]) -> str:
    payload_json = json.dumps(payload, separators=(",", ":"), ensure_ascii=False)
    payload_base64 = base64.urlsafe_b64encode(payload_json.encode("utf-8")).decode("utf-8").rstrip("=")
    signature = _sign_payload(payload_base64)
    return f"{payload_base64}.{signature}"


def decode_share_token(token: str) -> dict[str, Any] | None:
    parts = token.split(".")
    if len(parts) != 2:
        return None
    payload_base64, signature = parts
    expected = _sign_payload(payload_base64)
    if not hmac.compare_digest(signature, expected):
        return None
    padding = "=" * (-len(payload_base64) % 4)
    try:
        payload_raw = base64.urlsafe_b64decode(payload_base64 + padding)
        payload = json.loads(payload_raw.decode("utf-8"))
    except (json.JSONDecodeError, ValueError):
        return None
    expires_at = datetime.fromtimestamp(int(payload.get("exp", 0)), tz=UTC)
    if expires_at < datetime.now(tz=UTC):
        return None
    return payload


@router.post("/share-link", response_model=ShareLinkCreateResponse, dependencies=[Depends(require_api_token)])
async def create_share_link(payload: ShareLinkCreateRequest, request: Request) -> ShareLinkCreateResponse:
    store = get_store(request)
    session = store.create_share_session(mode=payload.mode, ttl_seconds=payload.ttl_seconds)
    expires_at = session["expires_at"]
    if not isinstance(expires_at, datetime):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="invalid share session")
    token_payload = {
        "sid": session["session_id"],
        "mode": session["mode"],
        "exp": int(expires_at.timestamp()),
    }
    token = encode_share_token(token_payload)
    return ShareLinkCreateResponse(
        session_id=str(session["session_id"]),
        token=token,
        url_path=f"/share/{token}",
        expires_at=expires_at,
        mode=str(session["mode"]),
    )


@router.post("/share-link/verify", response_model=ShareLinkVerifyResponse)
async def verify_share_link(payload: ShareLinkVerifyRequest, request: Request) -> ShareLinkVerifyResponse:
    store = get_store(request)
    token_payload = decode_share_token(payload.token)
    if token_payload is None:
        return ShareLinkVerifyResponse(valid=False)
    session_id = str(token_payload.get("sid", ""))
    mode = token_payload.get("mode")
    expires_at = datetime.fromtimestamp(int(token_payload.get("exp", 0)), tz=UTC)
    session = store.get_share_session(session_id)
    if session is None:
        return ShareLinkVerifyResponse(valid=False)
    if mode not in {"readonly", "interactive"}:
        return ShareLinkVerifyResponse(valid=False)
    return ShareLinkVerifyResponse(valid=True, session_id=session_id, mode=mode, expires_at=expires_at)
