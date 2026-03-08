from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from typing import Any, Literal
from uuid import uuid4


def _utcnow() -> datetime:
    return datetime.now(timezone.utc)


ConfirmationChoice = Literal["confirm", "reject", "modify"]


@dataclass(slots=True)
class ConfirmationRequest:
    request_id: str
    operation: str
    level: int
    reason: str
    preview: dict[str, Any] = field(default_factory=dict)
    expires_at: datetime | None = None


@dataclass(slots=True)
class ConfirmationResult:
    request_id: str
    approved: bool
    final_arguments: dict[str, Any]
    choice: ConfirmationChoice
    reason: str


class ConfirmationFlow:
    """用户确认流程。"""

    def __init__(self, *, ttl_seconds: int = 120) -> None:
        self.ttl_seconds = ttl_seconds
        self._requests: dict[str, ConfirmationRequest] = {}

    def create_request(
        self,
        *,
        operation: str,
        level: int,
        reason: str,
        preview: dict[str, Any] | None = None,
    ) -> ConfirmationRequest:
        request_id = uuid4().hex
        request = ConfirmationRequest(
            request_id=request_id,
            operation=operation,
            level=level,
            reason=reason,
            preview=preview or {},
            expires_at=_utcnow() + timedelta(seconds=self.ttl_seconds),
        )
        self._requests[request_id] = request
        return request

    def resolve(
        self,
        request_id: str,
        *,
        choice: ConfirmationChoice,
        original_arguments: dict[str, Any],
        modified_arguments: dict[str, Any] | None = None,
        reason: str = "",
    ) -> ConfirmationResult:
        request = self._requests.pop(request_id, None)
        if request is None:
            return ConfirmationResult(
                request_id=request_id,
                approved=False,
                final_arguments=original_arguments,
                choice="reject",
                reason="确认请求不存在或已失效",
            )

        if request.expires_at is not None and _utcnow() > request.expires_at:
            return ConfirmationResult(
                request_id=request_id,
                approved=False,
                final_arguments=original_arguments,
                choice="reject",
                reason="确认请求超时",
            )

        if choice == "confirm":
            return ConfirmationResult(
                request_id=request_id,
                approved=True,
                final_arguments=original_arguments,
                choice=choice,
                reason=reason or "用户确认执行",
            )

        if choice == "modify":
            final_arguments = modified_arguments or original_arguments
            return ConfirmationResult(
                request_id=request_id,
                approved=True,
                final_arguments=final_arguments,
                choice=choice,
                reason=reason or "用户修改参数后确认执行",
            )

        return ConfirmationResult(
            request_id=request_id,
            approved=False,
            final_arguments=original_arguments,
            choice="reject",
            reason=reason or "用户拒绝执行",
        )
