from __future__ import annotations

from importlib import import_module

SandboxExecutor = import_module("packages.engine.executor").SandboxExecutor


def test_sandbox_blocks_dangerous_import() -> None:
    executor = SandboxExecutor(timeout_seconds=2.0)
    result = executor.execute("import os\nx = 1")

    assert not result.success
    assert result.error is not None
    assert "blocked_module" in result.error


def test_sandbox_executes_safe_code() -> None:
    executor = SandboxExecutor(timeout_seconds=2.0)
    result = executor.execute("x = 1 + 2\ny = x * 2")

    assert result.success
    assert result.data["locals"]["x"] == 3
    assert result.data["locals"]["y"] == 6
