from __future__ import annotations

import builtins
import sys
import types
from io import StringIO
from pathlib import Path
from typing import Any

from rich.console import Console

from cli.chat import (
    ChatHistory,
    _enable_tab_completion,
    _handle_chat_command,
    _read_multiline_input,
)
from cli.config import AppSettings


class DummyBackend:
    def __init__(self) -> None:
        self.updated_settings: AppSettings | None = None

    def call_tool(self, name: str, _: dict[str, Any]) -> dict[str, Any]:
        if name == "blender_get_scene":
            return {
                "scene_name": "Scene",
                "blender_version": "5.0.0-mock",
                "objects_count": 3,
                "selected_objects": ["Cube"],
            }
        if name == "blender_capture_viewport":
            return {"saved_to": str(Path.cwd() / "viewport.png")}
        if name == "blender_undo":
            return {"undone": True}
        return {}

    def update_settings(self, settings: AppSettings) -> None:
        self.updated_settings = settings


class DummyRuntime:
    def __init__(self) -> None:
        self.settings = AppSettings()
        self.backend = DummyBackend()
        self.console = Console(file=StringIO(), force_terminal=False, color_system=None)


def test_handle_chat_command_switch_model_and_exit() -> None:
    runtime = DummyRuntime()
    history = ChatHistory(
        messages=[
            {"role": "user", "content": "hi"},
            {"role": "assistant", "content": "ok"},
        ]
    )

    exit_now = _handle_chat_command(
        runtime=runtime, history=history, command="/model qwen2.5"
    )
    assert exit_now is False
    assert runtime.settings.model == "qwen2.5"
    assert runtime.backend.updated_settings is not None
    assert runtime.backend.updated_settings.model == "qwen2.5"

    exit_now = _handle_chat_command(runtime=runtime, history=history, command="/exit")
    assert exit_now is True


def test_handle_chat_command_undo_and_scene() -> None:
    runtime = DummyRuntime()
    history = ChatHistory(
        messages=[
            {"role": "user", "content": "a"},
            {"role": "assistant", "content": "b"},
            {"role": "user", "content": "c"},
            {"role": "assistant", "content": "d"},
        ]
    )

    _handle_chat_command(runtime=runtime, history=history, command="/scene")
    assert history.messages

    _handle_chat_command(runtime=runtime, history=history, command="/undo")
    assert len(history.messages) == 2
    assert history.messages[-1]["content"] == "b"


def test_read_multiline_input_with_code_fence(monkeypatch: Any) -> None:
    feed = iter(["```", "line-1", "line-2", "```"])
    monkeypatch.setattr(builtins, "input", lambda _: next(feed))

    text = _read_multiline_input()
    assert text == "line-1\nline-2"


def test_enable_tab_completion_with_fake_readline(monkeypatch: Any) -> None:
    state: dict[str, Any] = {"completer": None, "bind": None}

    def set_completer(func: Any) -> None:
        state["completer"] = func

    def parse_and_bind(value: str) -> None:
        state["bind"] = value

    fake_readline = types.SimpleNamespace(
        set_completer=set_completer, parse_and_bind=parse_and_bind
    )
    monkeypatch.setitem(sys.modules, "readline", fake_readline)

    _enable_tab_completion(["/scene", "/screenshot"])
    assert callable(state["completer"])
    assert state["bind"] == "tab: complete"
