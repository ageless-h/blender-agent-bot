"""Core Engine implementation using unified protocol."""

from __future__ import annotations

import logging
import os
import time
from typing import Any

from .adapters.base import BlenderAdapter
from .adapters.mock import MockAdapter
from .adapters.socket import SocketAdapter
from .catalog.catalog import CapabilityCatalog, minimal_capability_set, capability_to_dict
from .security.allowlist import Allowlist
from .security.audit import AuditEvent, JsonFileAuditLogger, MemoryAuditLogger
from .security.guardrails import Guardrails
from .security.rate_limit import RateLimiter

logger = logging.getLogger(__name__)


class BlenderEngine:
    def __init__(
        self,
        adapter: BlenderAdapter | None = None,
        audit_logger: Any | None = None,
        allowlist: Allowlist | None = None,
        guardrails: Guardrails | None = None,
        rate_limiter: RateLimiter | None = None,
    ):
        if adapter is None:
            adapter_mode = os.environ.get("ENGINE_ADAPTER", "socket").lower()
            if adapter_mode == "mock":
                adapter = MockAdapter()
            else:
                adapter = SocketAdapter(
                    host=os.environ.get("ENGINE_SOCKET_HOST", "127.0.0.1"),
                    port=int(os.environ.get("ENGINE_SOCKET_PORT", "9876")),
                    max_retries=int(os.environ.get("ENGINE_MAX_RETRIES", "3")),
                )
        self._adapter = adapter

        if audit_logger is None:
            audit_path = os.environ.get("ENGINE_AUDIT_LOG")
            audit_logger = JsonFileAuditLogger(audit_path) if audit_path else MemoryAuditLogger()
        self._audit = audit_logger

        if allowlist is None:
            allowlist = Allowlist(audit_logger=self._audit)
            if os.environ.get("ENGINE_ENABLE_SCRIPT_EXECUTE", "").lower() in ("1", "true", "yes"):
                allowlist.enable_script_execute()
        self._allowlist = allowlist

        if guardrails is None:
            guardrails = Guardrails.from_env()
        self._guardrails = guardrails

        if rate_limiter is None:
            rate_cfg: dict[str, int] = {}
            raw_limits = os.environ.get("ENGINE_RATE_LIMITS", "")
            for pair in raw_limits.split(","):
                pair = pair.strip()
                if "=" in pair:
                    cap, lim = pair.split("=", 1)
                    try:
                        rate_cfg[cap.strip()] = int(lim.strip())
                    except ValueError:
                        pass
            window = float(os.environ.get("ENGINE_RATE_WINDOW_SECONDS", "60"))
            rate_limiter = RateLimiter(rate_cfg, window_seconds=window)
        self._rate_limiter = rate_limiter

        self._catalog = CapabilityCatalog()
        for cap in minimal_capability_set():
            self._catalog.register(cap)

    def execute_capability(
        self,
        capability: str,
        payload: dict[str, Any],
    ) -> dict[str, Any]:
        call_start = time.perf_counter()

        if not self._allowlist.is_allowed(capability):
            logger.warning("Capability %s BLOCKED by allowlist", capability)
            self._audit.record(
                AuditEvent(
                    capability=capability,
                    ok=False,
                    error="capability_not_allowed",
                )
            )
            return {
                "status": "blocked",
                "error": f"Capability '{capability}' is not allowed",
                "error_type": "capability_not_allowed",
                "capability": capability,
            }

        if not self._guardrails.allow(capability, payload):
            logger.warning("Capability %s BLOCKED by guardrails", capability)
            self._audit.record(
                AuditEvent(
                    capability=capability,
                    ok=False,
                    error="guardrails_blocked",
                )
            )
            return {
                "status": "blocked",
                "error": f"Capability '{capability}' blocked by guardrails",
                "error_type": "guardrails_blocked",
                "capability": capability,
            }

        if not self._rate_limiter.allow(capability):
            logger.warning("Capability %s BLOCKED by rate limiter", capability)
            self._audit.record(
                AuditEvent(
                    capability=capability,
                    ok=False,
                    error="rate_limit_exceeded",
                )
            )
            return {
                "status": "blocked",
                "error": f"Rate limit exceeded for capability '{capability}'",
                "error_type": "rate_limit_exceeded",
                "capability": capability,
            }

        try:
            result = self._adapter.execute(capability, payload)
            execution_time = (time.perf_counter() - call_start) * 1000

            if result.ok:
                self._audit.record(
                    AuditEvent(
                        capability=capability,
                        ok=True,
                    )
                )
                return {
                    "status": "success",
                    "result": result.result,
                    "capability": capability,
                    "execution_time_ms": execution_time,
                }
            else:
                self._audit.record(
                    AuditEvent(
                        capability=capability,
                        ok=False,
                        error=result.error or "unknown_error",
                    )
                )
                return {
                    "status": "error",
                    "error": result.error or "Unknown error",
                    "error_type": "execution_error",
                    "capability": capability,
                    "execution_time_ms": execution_time,
                }
        except Exception as e:
            execution_time = (time.perf_counter() - call_start) * 1000
            logger.exception("Capability %s raised exception", capability)
            self._audit.record(
                AuditEvent(
                    capability=capability,
                    ok=False,
                    error=str(e),
                )
            )
            return {
                "status": "error",
                "error": str(e),
                "error_type": "exception",
                "capability": capability,
                "execution_time_ms": execution_time,
            }

    def list_capabilities(self, version: str | None = None) -> list[dict[str, Any]]:
        return [capability_to_dict(cap, version) for cap in self._catalog.list()]

    def get_capability_info(self, name: str, version: str | None = None) -> dict[str, Any] | None:
        cap = self._catalog.get(name)
        if cap is None:
            return None
        return capability_to_dict(cap, version)
