from __future__ import annotations

import importlib
import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def _yaml_module() -> Any | None:
    try:
        return importlib.import_module("yaml")
    except Exception:  # pragma: no cover - optional dependency
        return None


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass(slots=True)
class SkillMetadata:
    name: str
    description: str
    tags: list[str] = field(default_factory=list)
    success_rate: float = 1.0
    version: str = "0.1.0"
    author: str = "local"


@dataclass(slots=True)
class SkillStep:
    tool_name: str
    arguments: dict[str, Any] = field(default_factory=dict)
    validation: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class SkillRecord:
    skill_id: str
    metadata: SkillMetadata
    capsule: list[SkillStep] = field(default_factory=list)
    gene: dict[str, Any] = field(default_factory=dict)
    created_at: str = field(default_factory=_utc_now_iso)
    updated_at: str = field(default_factory=_utc_now_iso)

    def to_dict(self) -> dict[str, Any]:
        return {
            "skill_id": self.skill_id,
            "metadata": {
                "name": self.metadata.name,
                "description": self.metadata.description,
                "tags": self.metadata.tags,
                "success_rate": self.metadata.success_rate,
                "version": self.metadata.version,
                "author": self.metadata.author,
            },
            "gene": self.gene,
            "capsule": [
                {
                    "tool_name": step.tool_name,
                    "arguments": step.arguments,
                    "validation": step.validation,
                }
                for step in self.capsule
            ],
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "SkillRecord":
        metadata_data = data.get("metadata", {})
        metadata = SkillMetadata(
            name=str(metadata_data.get("name", "unnamed_skill")),
            description=str(metadata_data.get("description", "")),
            tags=list(metadata_data.get("tags", [])),
            success_rate=float(metadata_data.get("success_rate", 1.0)),
            version=str(metadata_data.get("version", "0.1.0")),
            author=str(metadata_data.get("author", "local")),
        )
        capsule = [
            SkillStep(
                tool_name=str(item.get("tool_name", "")),
                arguments=dict(item.get("arguments", {})),
                validation=dict(item.get("validation", {})),
            )
            for item in data.get("capsule", [])
            if isinstance(item, dict)
        ]
        return cls(
            skill_id=str(data.get("skill_id", "")),
            metadata=metadata,
            capsule=capsule,
            gene=dict(data.get("gene", {})),
            created_at=str(data.get("created_at", _utc_now_iso())),
            updated_at=str(data.get("updated_at", _utc_now_iso())),
        )


class SkillStore:
    """本地技能库存储（YAML 优先，JSON 兜底）。"""

    def __init__(self, root_dir: str | Path) -> None:
        self.root_dir = Path(root_dir)
        self.root_dir.mkdir(parents=True, exist_ok=True)

    def save(self, skill: SkillRecord) -> Path:
        skill.updated_at = _utc_now_iso()
        path = self._skill_path(skill.skill_id)
        return self._write_file(path, skill.to_dict())

    def load(self, skill_id: str) -> SkillRecord | None:
        path = self._skill_path(skill_id)
        candidate_paths = [path]
        if not path.exists():
            candidate_paths.append(path.with_suffix(".json"))

        data: Any = None
        for candidate in candidate_paths:
            if candidate.exists():
                data = self._read_file(candidate)
                break

        if not isinstance(data, dict):
            return None
        return SkillRecord.from_dict(data)

    def delete(self, skill_id: str) -> bool:
        path = self._skill_path(skill_id)
        if not path.exists():
            return False
        path.unlink()
        return True

    def list_skills(self) -> list[SkillRecord]:
        skills: list[SkillRecord] = []
        for path in sorted(self.root_dir.glob("*.yaml")):
            data = self._read_file(path)
            if isinstance(data, dict):
                skills.append(SkillRecord.from_dict(data))
        for path in sorted(self.root_dir.glob("*.json")):
            if path.with_suffix(".yaml").exists():
                continue
            data = self._read_file(path)
            if isinstance(data, dict):
                skills.append(SkillRecord.from_dict(data))
        return skills

    def search(self, query: str, *, tags: list[str] | None = None) -> list[SkillRecord]:
        needle = query.strip().lower()
        tag_set = {tag.lower() for tag in tags or []}
        results: list[SkillRecord] = []
        for skill in self.list_skills():
            haystack = " ".join(
                [
                    skill.skill_id,
                    skill.metadata.name,
                    skill.metadata.description,
                    *skill.metadata.tags,
                ]
            ).lower()
            if needle and needle not in haystack:
                continue
            if tag_set and not (tag_set & {tag.lower() for tag in skill.metadata.tags}):
                continue
            results.append(skill)
        return results

    def update_success_rate(self, skill_id: str, success: bool) -> SkillRecord | None:
        skill = self.load(skill_id)
        if skill is None:
            return None
        current = skill.metadata.success_rate
        target = 1.0 if success else 0.0
        skill.metadata.success_rate = round(current * 0.8 + target * 0.2, 4)
        self.save(skill)
        return skill

    def _skill_path(self, skill_id: str) -> Path:
        normalized = skill_id.strip().replace(" ", "_")
        return self.root_dir / f"{normalized}.yaml"

    def _write_file(self, path: Path, data: dict[str, Any]) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        yaml_mod = _yaml_module()
        if yaml_mod is not None:
            with path.open("w", encoding="utf-8") as handle:
                yaml_mod.safe_dump(data, handle, allow_unicode=True, sort_keys=False)
            return path
        fallback_path = path.with_suffix(".json")
        with fallback_path.open("w", encoding="utf-8") as handle:
            json.dump(data, handle, ensure_ascii=False, indent=2)
        return fallback_path

    def _read_file(self, path: Path) -> Any:
        yaml_mod = _yaml_module()
        if path.suffix == ".yaml" and yaml_mod is not None:
            with path.open("r", encoding="utf-8") as handle:
                return yaml_mod.safe_load(handle) or {}
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)
