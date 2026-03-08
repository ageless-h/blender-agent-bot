from __future__ import annotations

import copy
import json
import os
from pathlib import Path
from typing import Any, Mapping

import yaml

from .schema import AppConfig

ENV_PREFIX = "BLENDER_AGENT_"
DEFAULT_CONFIG_PATH = Path("~/.blender-agent/config.yaml").expanduser()
DEFAULT_CONFIG: dict[str, Any] = AppConfig().to_dict()


def _parse_env_value(raw_value: str) -> Any:
    value = raw_value.strip()
    lower = value.lower()

    if lower in {"true", "false"}:
        return lower == "true"

    if lower in {"none", "null"}:
        return None

    try:
        return int(value)
    except ValueError:
        pass

    try:
        return float(value)
    except ValueError:
        pass

    if value.startswith("{") or value.startswith("["):
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            return value

    return value


def _set_nested_value(target: dict[str, Any], path: list[str], value: Any) -> None:
    current = target
    for key in path[:-1]:
        node = current.get(key)
        if not isinstance(node, dict):
            node = {}
            current[key] = node
        current = node
    current[path[-1]] = value


def deep_merge(base: Mapping[str, Any], override: Mapping[str, Any]) -> dict[str, Any]:
    merged = copy.deepcopy(dict(base))
    for key, value in override.items():
        existing = merged.get(key)
        if isinstance(existing, Mapping) and isinstance(value, Mapping):
            merged[key] = deep_merge(existing, value)
        else:
            merged[key] = copy.deepcopy(value)
    return merged


def load_config_file(path: str | Path | None = None) -> dict[str, Any]:
    config_path = Path(path).expanduser() if path is not None else DEFAULT_CONFIG_PATH
    if not config_path.exists():
        return {}

    loaded = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    if loaded is None:
        return {}
    if not isinstance(loaded, dict):
        raise ValueError(f"配置文件内容必须是对象: {config_path}")
    return loaded


def load_env_overrides(env: Mapping[str, str] | None = None, prefix: str = ENV_PREFIX) -> dict[str, Any]:
    source_env = dict(env) if env is not None else dict(os.environ)
    overrides: dict[str, Any] = {}

    for env_key, env_value in source_env.items():
        if not env_key.startswith(prefix):
            continue

        normalized = env_key[len(prefix) :]
        parts = [part.lower() for part in normalized.split("__") if part]
        if not parts:
            continue

        _set_nested_value(overrides, parts, _parse_env_value(env_value))

    return overrides


def merge_config(
    defaults: Mapping[str, Any] | None = None,
    file_config: Mapping[str, Any] | None = None,
    env_config: Mapping[str, Any] | None = None,
    cli_config: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    merged = copy.deepcopy(dict(defaults or DEFAULT_CONFIG))
    for extra in (file_config or {}, env_config or {}, cli_config or {}):
        merged = deep_merge(merged, extra)
    return merged


def load_app_config(
    config_path: str | Path | None = None,
    cli_overrides: Mapping[str, Any] | None = None,
    env: Mapping[str, str] | None = None,
) -> AppConfig:
    file_config = load_config_file(config_path)
    env_config = load_env_overrides(env=env)
    merged = merge_config(DEFAULT_CONFIG, file_config, env_config, cli_overrides or {})
    return AppConfig.from_dict(merged)


__all__ = [
    "ENV_PREFIX",
    "DEFAULT_CONFIG_PATH",
    "DEFAULT_CONFIG",
    "deep_merge",
    "load_config_file",
    "load_env_overrides",
    "merge_config",
    "load_app_config",
]
