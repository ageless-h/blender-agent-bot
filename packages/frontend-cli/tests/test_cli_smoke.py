from __future__ import annotations

import json
import os
from pathlib import Path

import pytest
from cli import setup as setup_cli_module
from cli.main import app
from typer.testing import CliRunner


def _make_env(tmp_home: Path) -> dict[str, str]:
    env = os.environ.copy()
    env["HOME"] = str(tmp_home)
    env["USERPROFILE"] = str(tmp_home)
    return env


def test_help_and_version() -> None:
    runner = CliRunner()
    help_result = runner.invoke(app, ["--help"], color=False)
    assert help_result.exit_code == 0
    assert "chat" in help_result.output
    assert "run" in help_result.output

    version_result = runner.invoke(app, ["--version"], color=False)
    assert version_result.exit_code == 0
    assert "blender-agent" in version_result.output


def test_tools_and_status_json() -> None:
    runner = CliRunner()
    with runner.isolated_filesystem():
        home = Path.cwd() / "home"
        env = _make_env(home)

        list_result = runner.invoke(
            app, ["tools", "--list", "--output", "json"], env=env, color=False
        )
        assert list_result.exit_code == 0
        assert "blender_get_scene" in list_result.output

        info_result = runner.invoke(
            app,
            ["tools", "--info", "blender_get_scene", "--output", "json"],
            env=env,
            color=False,
        )
        assert info_result.exit_code == 0
        assert "blender_get_scene" in info_result.output

        call_result = runner.invoke(
            app,
            [
                "tools",
                "blender_create_object",
                "--args",
                '{"name":"Cube_A","type":"MESH"}',
                "--output",
                "json",
            ],
            env=env,
            color=False,
        )
        assert call_result.exit_code == 0
        payload = json.loads(call_result.output)
        assert payload["created"] is True

        status_result = runner.invoke(app, ["status", "--json"], env=env, color=False)
        assert status_result.exit_code == 0
        status_payload = json.loads(status_result.output)
        assert "blender" in status_payload
        assert "agent_core" in status_payload
        assert "version" in status_payload["blender"]
        assert "model" in status_payload
        assert "scene" in status_payload
        assert "skills" in status_payload
        assert "config" in status_payload


def test_setup_non_interactive_and_ide_config() -> None:
    runner = CliRunner()
    with runner.isolated_filesystem():
        home = Path.cwd() / "home"
        env = _make_env(home)

        setup_result = runner.invoke(
            app,
            [
                "setup",
                "--non-interactive",
                "--provider",
                "ollama",
                "--model",
                "qwen2.5",
                "--no-link-addon",
            ],
            env=env,
            color=False,
        )
        assert setup_result.exit_code == 0

        config_file = home / ".blender-agent" / "config.yaml"
        assert config_file.exists()

        cursor_config = home / "cursor-mcp.json"
        cursor_result = runner.invoke(
            app,
            ["setup", "cursor", "--output", str(cursor_config)],
            env=env,
            color=False,
        )
        assert cursor_result.exit_code == 0
        assert cursor_config.exists()

        mcp_payload = json.loads(cursor_config.read_text(encoding="utf-8"))
        server = mcp_payload["mcpServers"]["blender-agent"]
        assert server["command"] == "python"
        assert isinstance(server["args"], list) and server["args"]
        assert server["args"] == ["-m", "server.mcp_server"]
        assert Path(server["env"]["PYTHONPATH"]).exists()

        vscode_config = home / "vscode-settings.json"
        vscode_result = runner.invoke(
            app,
            ["setup", "vscode", "--output", str(vscode_config)],
            env=env,
            color=False,
        )
        assert vscode_result.exit_code == 0
        vscode_payload = json.loads(vscode_config.read_text(encoding="utf-8"))
        assert "mcp.servers" in vscode_payload
        assert "blender-agent" in vscode_payload["mcp.servers"]

        windsurf_config = home / "windsurf-mcp.json"
        windsurf_result = runner.invoke(
            app,
            ["setup", "windsurf", "--output", str(windsurf_config)],
            env=env,
            color=False,
        )
        assert windsurf_result.exit_code == 0
        windsurf_payload = json.loads(windsurf_config.read_text(encoding="utf-8"))
        assert "mcpServers" in windsurf_payload
        assert "blender-agent" in windsurf_payload["mcpServers"]


def test_setup_generate_payload_requires_mcp_entrypoint(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def _raise_runtime_error() -> tuple[list[str], dict[str, str]]:
        raise RuntimeError("missing mcp")

    monkeypatch.setattr(
        setup_cli_module,
        "_resolve_mcp_launch_config",
        _raise_runtime_error,
    )

    with pytest.raises(RuntimeError, match="missing mcp"):
        setup_cli_module._generate_ide_payload(
            ide="cursor",
            endpoint=None,
            model="gpt-4.1-mini",
        )
