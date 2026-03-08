from __future__ import annotations

from collections import deque
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any


def _get_bpy() -> Any | None:
    try:
        import bpy  # type: ignore

        return bpy
    except Exception:
        return None


CommandHandler = Callable[[dict[str, Any]], dict[str, Any]]


@dataclass(slots=True)
class TimerConfig:
    interval: float = 0.1
    max_batch: int = 8


_QUEUE: deque[dict[str, Any]] = deque()
_HANDLER: CommandHandler | None = None
_REGISTERED = False
_CONFIG = TimerConfig()


def pending_count() -> int:
    return len(_QUEUE)


def enqueue_command(command: dict[str, Any]) -> None:
    _QUEUE.append(dict(command))


def set_handler(handler: CommandHandler | None) -> None:
    global _HANDLER
    _HANDLER = handler


def _process_once() -> None:
    if _HANDLER is None:
        return
    for _ in range(_CONFIG.max_batch):
        if not _QUEUE:
            return
        command = _QUEUE.popleft()
        try:
            _HANDLER(command)
        except Exception:
            continue


def _timer_callback() -> float:
    _process_once()
    return _CONFIG.interval


def register_timer(config: TimerConfig | None = None) -> bool:
    global _REGISTERED, _CONFIG
    if config is not None:
        _CONFIG = config

    if _REGISTERED:
        return True

    bpy = _get_bpy()
    if bpy is None:
        _REGISTERED = False
        return False

    bpy.app.timers.register(_timer_callback, first_interval=_CONFIG.interval, persistent=True)
    _REGISTERED = True
    return True


def unregister_timer() -> None:
    global _REGISTERED
    if not _REGISTERED:
        return

    bpy = _get_bpy()
    if bpy is not None:
        try:
            bpy.app.timers.unregister(_timer_callback)
        except Exception:
            pass

    _REGISTERED = False
