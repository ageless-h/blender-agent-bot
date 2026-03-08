from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel, ConfigDict, Field, ValidationError, field_validator


def default_config_dir() -> Path:
    return Path.home() / ".blender-agent"


def default_config_path() -> Path:
    return default_config_dir() / "config.yaml"


def default_history_dir() -> Path:
    return default_config_dir() / "history"


def default_skills_dir() -> Path:
    return default_config_dir() / "skills"


class AppSettings(BaseModel):
    model_config = ConfigDict(extra="allow")

    provider: str = "openai"
    model: str = "gpt-4.1-mini"
    api_key: str | None = None
    endpoint: str | None = None
    verbose: bool = False
    blender_executable: str | None = None
    config_dir: str = Field(default_factory=lambda: str(default_config_dir()))
    history_dir: str = Field(default_factory=lambda: str(default_history_dir()))
    skills_dir: str = Field(default_factory=lambda: str(default_skills_dir()))

    @field_validator("provider")
    @classmethod
    def normalize_provider(cls, value: str) -> str:
        normalized = value.strip().lower()
        if not normalized:
            raise ValueError("provider 不能为空")
        return normalized

    @field_validator("endpoint")
    @classmethod
    def normalize_endpoint(cls, value: str | None) -> str | None:
        if value is None:
            return None
        trimmed = value.strip()
        if not trimmed:
            return None
        return trimmed.rstrip("/")

    @property
    def config_dir_path(self) -> Path:
        return Path(self.config_dir).expanduser()

    @property
    def history_dir_path(self) -> Path:
        return Path(self.history_dir).expanduser()

    @property
    def skills_dir_path(self) -> Path:
        return Path(self.skills_dir).expanduser()


class SettingsManager:
    def __init__(self, config_path: Path | None = None):
        target_path = config_path.expanduser() if config_path else default_config_path()
        self._config_path = target_path

    @property
    def config_path(self) -> Path:
        return self._config_path

    def ensure_directories(self, settings: AppSettings) -> None:
        self._config_path.parent.mkdir(parents=True, exist_ok=True)
        settings.config_dir_path.mkdir(parents=True, exist_ok=True)
        settings.history_dir_path.mkdir(parents=True, exist_ok=True)
        settings.skills_dir_path.mkdir(parents=True, exist_ok=True)

    def load(self) -> AppSettings:
        if not self._config_path.exists():
            settings = AppSettings()
            self.ensure_directories(settings)
            return settings

        raw = yaml.safe_load(self._config_path.read_text(encoding="utf-8"))
        data = raw if isinstance(raw, dict) else {}

        try:
            settings = AppSettings.model_validate(data)
        except ValidationError:
            settings = AppSettings()

        self.ensure_directories(settings)
        return settings

    def save(self, settings: AppSettings) -> None:
        self.ensure_directories(settings)
        payload = settings.model_dump(mode="json")
        self._config_path.write_text(
            yaml.safe_dump(payload, allow_unicode=True, sort_keys=False),
            encoding="utf-8",
        )

    @staticmethod
    def apply_overrides(settings: AppSettings, **overrides: Any) -> AppSettings:
        normalized: dict[str, Any] = {}
        for key, value in overrides.items():
            if value is None:
                continue
            if isinstance(value, str) and value == "":
                continue
            normalized[key] = value

        if not normalized:
            return settings
        return settings.model_copy(update=normalized)
