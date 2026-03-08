from __future__ import annotations

import json

from shared.config.defaults import load_app_config, load_env_overrides
from shared.config.schema import AppConfig


def test_export_json_schema_contains_core_sections(tmp_path) -> None:
    output = tmp_path / "app_config.schema.json"
    schema = AppConfig.export_json_schema(output)

    assert output.exists()
    assert "properties" in schema
    assert {"llm", "engine", "safety", "skills", "ui"}.issubset(schema["properties"].keys())

    loaded = json.loads(output.read_text(encoding="utf-8"))
    assert loaded["title"] == "AppConfig"


def test_config_merge_order_defaults_file_env_cli(tmp_path) -> None:
    config_path = tmp_path / "config.yaml"
    config_path.write_text(
        "\n".join(
            [
                "llm:",
                "  model: file-model",
                "ui:",
                "  theme: file-theme",
            ]
        ),
        encoding="utf-8",
    )

    env = {
        "BLENDER_AGENT_LLM__MODEL": "env-model",
        "BLENDER_AGENT_UI__THEME": "env-theme",
        "BLENDER_AGENT_ENGINE__PORT": "9900",
        "BLENDER_AGENT_UI__STREAM_RENDER": "false",
    }
    cli = {"llm": {"model": "cli-model"}}

    app_config = load_app_config(config_path=config_path, cli_overrides=cli, env=env)

    assert app_config.llm.model == "cli-model"
    assert app_config.ui.theme == "env-theme"
    assert app_config.engine.port == 9900
    assert app_config.ui.stream_render is False


def test_env_overrides_nested_mapping() -> None:
    env = {
        "BLENDER_AGENT_LLM__PROVIDER": "anthropic",
        "BLENDER_AGENT_SAFETY__AUTO_CONFIRM_LEVELS": '["level_0", "level_1"]',
    }

    overrides = load_env_overrides(env=env)

    assert overrides["llm"]["provider"] == "anthropic"
    assert overrides["safety"]["auto_confirm_levels"] == ["level_0", "level_1"]
