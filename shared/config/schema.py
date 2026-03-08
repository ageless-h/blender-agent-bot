from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Mapping, TypeVar

from pydantic import BaseModel, ConfigDict, Field

from ..types.tool_types import SafetyLevel

ConfigModelT = TypeVar("ConfigModelT", bound="AppConfig")


class LLMConfig(BaseModel):
    provider: str = "openai"
    model: str = "gpt-4o-mini"
    api_key: str | None = None
    base_url: str | None = None
    temperature: float = 0.2
    max_tokens: int | None = None

    model_config = ConfigDict(extra="forbid")


class EngineConfig(BaseModel):
    transport: str = "stdio"
    host: str = "127.0.0.1"
    port: int = 8765
    startup_timeout: float = 30.0

    model_config = ConfigDict(extra="forbid")


class SafetyConfig(BaseModel):
    default_level: SafetyLevel = SafetyLevel.LEVEL_1
    auto_confirm_levels: list[SafetyLevel] = Field(default_factory=lambda: [SafetyLevel.LEVEL_0])
    blocked_tools: list[str] = Field(default_factory=list)

    model_config = ConfigDict(extra="forbid")


class SkillConfig(BaseModel):
    builtin_path: str = "~/.blender-agent/skills/builtin"
    community_path: str = "~/.blender-agent/skills/community"
    enabled: list[str] = Field(default_factory=list)

    model_config = ConfigDict(extra="forbid")


class UIConfig(BaseModel):
    theme: str = "dark"
    language: str = "zh-CN"
    stream_render: bool = True

    model_config = ConfigDict(extra="forbid")


class AppConfig(BaseModel):
    llm: LLMConfig = Field(default_factory=LLMConfig)
    engine: EngineConfig = Field(default_factory=EngineConfig)
    safety: SafetyConfig = Field(default_factory=SafetyConfig)
    skills: SkillConfig = Field(default_factory=SkillConfig)
    ui: UIConfig = Field(default_factory=UIConfig)

    model_config = ConfigDict(extra="forbid")

    def to_dict(self) -> dict[str, Any]:
        if hasattr(self, "model_dump"):
            return self.model_dump(mode="json")
        return self.dict()

    @classmethod
    def from_dict(cls: type[ConfigModelT], payload: Mapping[str, Any]) -> ConfigModelT:
        if hasattr(cls, "model_validate"):
            return cls.model_validate(payload)
        return cls.parse_obj(payload)

    @classmethod
    def json_schema(cls) -> dict[str, Any]:
        if hasattr(cls, "model_json_schema"):
            return cls.model_json_schema()
        return cls.schema()

    @classmethod
    def export_json_schema(cls, path: str | Path | None = None) -> dict[str, Any]:
        schema = cls.json_schema()
        if path is not None:
            output_path = Path(path).expanduser()
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(json.dumps(schema, ensure_ascii=False, indent=2), encoding="utf-8")
        return schema


__all__ = [
    "AppConfig",
    "LLMConfig",
    "EngineConfig",
    "SafetyConfig",
    "SkillConfig",
    "UIConfig",
]
