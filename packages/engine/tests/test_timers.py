from __future__ import annotations

from importlib import import_module

timers = import_module("packages.engine.addon.timers")


def test_register_timer_without_bpy_returns_false() -> None:
    result = timers.register_timer()
    assert result is False
    timers.unregister_timer()
