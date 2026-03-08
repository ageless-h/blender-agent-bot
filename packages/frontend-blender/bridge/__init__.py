from __future__ import annotations

import threading
import time
import uuid
from dataclasses import dataclass, field
from queue import Empty, Queue
from typing import Any, Callable, Mapping

from .message_handler import (
    JSONDict,
    MessageCodecError,
    MessageQueue,
    StreamAssembler,
    decode_message,
    encode_message,
    parse_error_message,
)
from .subprocess_bridge import AgentProcessBridge, BridgeProcessError


@dataclass(slots=True)
class RuntimeSettings:
    """BridgeRuntime 启动参数。"""

    command: str | None = None
    env_overrides: dict[str, str] = field(default_factory=dict)
    cwd: str | None = None
    request_timeout: float = 45.0
    auto_restart: bool = True
    max_restart_attempts: int = 3
    restart_backoff_seconds: float = 1.0


class BridgeRuntime:
    """Agent Core 通信运行时（进程生命周期 + 请求队列 + 流式响应）。"""

    def __init__(self) -> None:
        self._settings = RuntimeSettings()
        self._bridge: AgentProcessBridge | None = None

        self._reader_thread: threading.Thread | None = None
        self._stop_event = threading.Event()

        self._lock = threading.RLock()
        self._pending_lock = threading.RLock()
        self._pending_requests: dict[str, Queue[JSONDict]] = {}
        self._cancelled_request_ids: set[str] = set()

        self._incoming_events = MessageQueue()
        self._stream_assembler = StreamAssembler()
        self._log_buffer: list[str] = []
        self._last_error = ""
        self._restart_attempts = 0

    def start(self, settings: RuntimeSettings | None = None) -> None:
        with self._lock:
            if settings is not None:
                self._settings = settings

            if self.is_connected():
                return

            self._last_error = ""
            self._stop_event.clear()

            self._bridge = AgentProcessBridge(
                command=self._settings.command,
                env_overrides=self._settings.env_overrides,
                cwd=self._settings.cwd,
                log_callback=self._append_log,
            )
            self._bridge.start()

            self._reader_thread = threading.Thread(
                target=self._reader_loop,
                name="blenderagent-bridge-stdout",
                daemon=True,
            )
            self._reader_thread.start()

    def stop(self) -> None:
        with self._lock:
            self._stop_event.set()
            self._fail_all_pending("Agent Core 连接已关闭。")

            if self._bridge is not None:
                self._bridge.stop()

            if self._reader_thread is not None and self._reader_thread.is_alive():
                self._reader_thread.join(timeout=2.0)

            self._reader_thread = None
            self._bridge = None

    def restart(self, settings: RuntimeSettings | None = None) -> None:
        with self._lock:
            self.stop()
            self._restart_attempts = 0
            self.start(settings=settings or self._settings)

    def is_connected(self) -> bool:
        return self._bridge is not None and self._bridge.is_running()

    def status(self) -> str:
        return "CONNECTED" if self.is_connected() else "DISCONNECTED"

    def health_check(self, *, auto_recover: bool = False) -> bool:
        if self.is_connected():
            return True

        if auto_recover:
            return self._auto_restart_bridge()
        return False

    def tail_logs(self, limit: int = 20) -> list[str]:
        if limit <= 0:
            return []
        return self._log_buffer[-limit:]

    @property
    def last_error(self) -> str:
        return self._last_error

    def send_request(
        self,
        payload: Mapping[str, Any],
        *,
        timeout: float | None = None,
        on_stream: Callable[[str, JSONDict], None] | None = None,
    ) -> JSONDict:
        if (not self.is_connected() or self._bridge is None) and not self._auto_restart_bridge():
            raise BridgeProcessError("Agent Core 尚未连接。")

        bridge = self._bridge
        if bridge is None:
            raise BridgeProcessError("Agent Core 连接不可用。")

        request_payload = dict(payload)
        request_id = str(request_payload.get("request_id") or uuid.uuid4().hex)
        request_payload["request_id"] = request_id

        response_queue: Queue[JSONDict] = Queue()
        with self._pending_lock:
            self._pending_requests[request_id] = response_queue

        try:
            bridge.send_line(encode_message(request_payload))
            response = self._wait_response(
                request_id=request_id,
                response_queue=response_queue,
                timeout=timeout or self._settings.request_timeout,
                on_stream=on_stream,
            )
            self._restart_attempts = 0
            return response
        finally:
            with self._pending_lock:
                self._pending_requests.pop(request_id, None)
                self._cancelled_request_ids.discard(request_id)
            self._stream_assembler.discard(request_id)

    def cancel_request(self, request_id: str) -> None:
        with self._pending_lock:
            if request_id in self._pending_requests:
                self._cancelled_request_ids.add(request_id)

    def cancel_all_requests(self) -> None:
        with self._pending_lock:
            self._cancelled_request_ids.update(self._pending_requests.keys())

    def poll_events(self, limit: int = 100) -> list[JSONDict]:
        return self._incoming_events.drain(limit=limit)

    def _wait_response(
        self,
        *,
        request_id: str,
        response_queue: Queue[JSONDict],
        timeout: float,
        on_stream: Callable[[str, JSONDict], None] | None,
    ) -> JSONDict:
        deadline = time.monotonic() + timeout

        while True:
            if self._is_cancelled(request_id):
                raise RuntimeError("请求已取消。")

            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise TimeoutError("等待 Agent Core 响应超时。")

            try:
                response = response_queue.get(timeout=min(remaining, 0.2))
            except Empty:
                if not self.is_connected():
                    raise BridgeProcessError("等待响应期间 Agent Core 已断开。")
                continue

            event = str(response.get("event", "")).strip().lower()

            if event in {"token", "stream_token", "delta"}:
                token = str(response.get("token") or response.get("delta") or "")
                if token:
                    self._stream_assembler.append(request_id, token)
                    if on_stream is not None:
                        on_stream(token, response)
                continue

            if event in {"error", "failed"} or "error" in response:
                raise RuntimeError(parse_error_message(response))

            if event in {"done", "completed", "response"}:
                fallback = str(response.get("content") or response.get("message") or "")
                response["content"] = self._stream_assembler.finalize(request_id, fallback=fallback)
                return response

            if "content" in response or "message" in response:
                fallback = str(response.get("content") or response.get("message") or "")
                response["content"] = self._stream_assembler.finalize(request_id, fallback=fallback)
                return response

            self._incoming_events.put(response)

    def _reader_loop(self) -> None:
        while not self._stop_event.is_set():
            bridge = self._bridge
            if bridge is None:
                break

            stdout = bridge.stdout
            if stdout is None:
                self._last_error = "Agent Core stdout 不可用。"
                break

            line = stdout.readline()
            if not line:
                if not bridge.is_running():
                    break
                time.sleep(0.05)
                continue

            try:
                payload = decode_message(line)
            except MessageCodecError as exc:
                self._incoming_events.put(
                    {
                        "event": "bridge_parse_error",
                        "message": str(exc),
                        "raw_line": line.rstrip(),
                    }
                )
                continue

            request_id = payload.get("request_id")
            if isinstance(request_id, str):
                with self._pending_lock:
                    response_queue = self._pending_requests.get(request_id)
                if response_queue is not None:
                    response_queue.put(payload)
                    continue

            self._incoming_events.put(payload)

        if not self._stop_event.is_set() and self._bridge is not None and not self._bridge.is_running():
            self._last_error = "Agent Core 进程已退出。"
            self._fail_all_pending(self._last_error)
            self._auto_restart_bridge()

    def _auto_restart_bridge(self) -> bool:
        if self._stop_event.is_set():
            return False

        if not self._settings.auto_restart:
            return False

        max_attempts = max(int(self._settings.max_restart_attempts), 0)
        if max_attempts and self._restart_attempts >= max_attempts:
            return False

        with self._lock:
            if self.is_connected():
                return True

            self._restart_attempts += 1
            backoff = max(float(self._settings.restart_backoff_seconds), 0.0)

        if backoff > 0:
            time.sleep(backoff)

        try:
            self.start(self._settings)
        except Exception as exc:
            self._last_error = f"自动重启失败: {exc}"
            return False

        self._incoming_events.put(
            {
                "event": "bridge_restarted",
                "attempt": self._restart_attempts,
            }
        )
        self._last_error = ""
        return True

    def _append_log(self, line: str) -> None:
        self._log_buffer.append(line)
        if len(self._log_buffer) > 200:
            self._log_buffer = self._log_buffer[-200:]

    def _fail_all_pending(self, message: str) -> None:
        with self._pending_lock:
            for request_id, response_queue in self._pending_requests.items():
                response_queue.put(
                    {
                        "request_id": request_id,
                        "event": "error",
                        "error": message,
                    }
                )

    def _is_cancelled(self, request_id: str) -> bool:
        with self._pending_lock:
            return request_id in self._cancelled_request_ids


_RUNTIME = BridgeRuntime()


def get_runtime() -> BridgeRuntime:
    return _RUNTIME


def start_runtime(settings: RuntimeSettings | None = None) -> None:
    _RUNTIME.start(settings=settings)


def stop_runtime() -> None:
    _RUNTIME.stop()


__all__ = [
    "BridgeRuntime",
    "RuntimeSettings",
    "get_runtime",
    "start_runtime",
    "stop_runtime",
]
