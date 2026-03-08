from __future__ import annotations

import pytest

from conftest import load_module_from_repo


subprocess_bridge = load_module_from_repo("bridge/subprocess_bridge.py", "frontend_blender_subprocess_bridge")


def test_build_command_uses_default_when_empty(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("BLENDERAGENT_CORE_CMD", raising=False)
    command = subprocess_bridge.AgentProcessBridge.build_command(None)
    assert command == ["python", "-m", "blender_agent_core.stdio_server"]


def test_build_command_prefers_explicit_command(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("BLENDERAGENT_CORE_CMD", "python -m fallback.server")
    command = subprocess_bridge.AgentProcessBridge.build_command("python -m custom.server")
    assert command == ["python", "-m", "custom.server"]


def test_send_line_without_running_process_raises() -> None:
    bridge = subprocess_bridge.AgentProcessBridge(command="python -m foo")
    with pytest.raises(subprocess_bridge.BridgeProcessError):
        bridge.send_line('{"type":"ping"}')


def test_tail_logs_limit() -> None:
    bridge = subprocess_bridge.AgentProcessBridge(command="python -m foo")
    bridge._stderr_logs.extend(["line-1", "line-2", "line-3"])
    assert bridge.tail_logs(limit=2) == ["line-2", "line-3"]


def test_build_command_uses_env_when_no_explicit(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("BLENDERAGENT_CORE_CMD", "python -m env.server")
    command = subprocess_bridge.AgentProcessBridge.build_command("")
    assert command == ["python", "-m", "env.server"]
