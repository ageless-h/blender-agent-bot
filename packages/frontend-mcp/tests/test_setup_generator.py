from __future__ import annotations

import json

from config.setup_generator import SetupGenerator, detect_python_executable


def test_detect_python_executable_returns_non_empty_path() -> None:
    python_path = detect_python_executable()
    assert python_path


def test_generate_cursor_config_file(tmp_path) -> None:
    generator = SetupGenerator(python_path="python")
    generated = generator.generate("cursor", output_root=tmp_path)

    assert generated.path == tmp_path / ".cursor" / "mcp.json"
    assert generated.path.exists()

    config = json.loads(generated.path.read_text(encoding="utf-8"))
    assert "mcpServers" in config
    assert "blender-mcp" in config["mcpServers"]
    assert config["mcpServers"]["blender-mcp"]["command"] == "python"


def test_generate_vscode_merges_existing_settings(tmp_path) -> None:
    settings_path = tmp_path / ".vscode" / "settings.json"
    settings_path.parent.mkdir(parents=True, exist_ok=True)
    settings_path.write_text(
        json.dumps(
            {
                "editor.formatOnSave": True,
                "mcp.servers": {
                    "existing-server": {
                        "command": "node",
                        "args": ["server.js"],
                    }
                },
            }
        ),
        encoding="utf-8",
    )

    generator = SetupGenerator(python_path="python")
    generator.generate("vscode", output_root=tmp_path)

    merged = json.loads(settings_path.read_text(encoding="utf-8"))
    assert merged["editor.formatOnSave"] is True
    assert "existing-server" in merged["mcp.servers"]
    assert "blender-mcp" in merged["mcp.servers"]


def test_generate_claude_windsurf_and_generic_configs(tmp_path) -> None:
    generator = SetupGenerator(python_path="python")

    claude = generator.generate("claude-desktop", output_root=tmp_path)
    windsurf = generator.generate("windsurf", output_root=tmp_path)
    generic = generator.generate("generic", output_root=tmp_path)

    assert claude.path == tmp_path / "claude_desktop_config.json"
    assert windsurf.path == tmp_path / ".windsurf" / "mcp.json"
    assert generic.path == tmp_path / "blender-mcp.json"

    claude_json = json.loads(claude.path.read_text(encoding="utf-8"))
    windsurf_json = json.loads(windsurf.path.read_text(encoding="utf-8"))
    generic_json = json.loads(generic.path.read_text(encoding="utf-8"))

    assert "blender-mcp" in claude_json["mcpServers"]
    assert "blender-mcp" in windsurf_json["mcpServers"]
    assert "blender-mcp" in generic_json["mcpServers"]
