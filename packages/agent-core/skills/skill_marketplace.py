from __future__ import annotations

import json
import tarfile
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .skill_store import SkillRecord, SkillStore


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


class SkillMarketplace:
    """社区技能包打包与解包。"""

    def package_skills(
        self,
        *,
        store: SkillStore,
        skill_ids: list[str],
        output_path: str | Path,
        metadata: dict[str, Any] | None = None,
    ) -> Path:
        target = Path(output_path)
        target.parent.mkdir(parents=True, exist_ok=True)

        skills: list[SkillRecord] = []
        for skill_id in skill_ids:
            record = store.load(skill_id)
            if record is not None:
                skills.append(record)

        package_manifest = {
            "generated_at": _utc_now_iso(),
            "skill_count": len(skills),
            "skills": [skill.skill_id for skill in skills],
            "metadata": metadata or {},
        }

        with tempfile.TemporaryDirectory(prefix="skill_pkg_") as temp_dir_str:
            temp_dir = Path(temp_dir_str)
            manifest_path = temp_dir / "manifest.json"
            manifest_path.write_text(
                json.dumps(package_manifest, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
            for skill in skills:
                skill_path = temp_dir / f"{skill.skill_id}.json"
                skill_path.write_text(
                    json.dumps(skill.to_dict(), ensure_ascii=False, indent=2),
                    encoding="utf-8",
                )

            with tarfile.open(target, mode="w:gz") as archive:
                archive.add(manifest_path, arcname="manifest.json")
                for skill in skills:
                    archive.add(temp_dir / f"{skill.skill_id}.json", arcname=f"skills/{skill.skill_id}.json")

        return target

    def unpack_package(
        self,
        *,
        package_path: str | Path,
        target_store: SkillStore,
        overwrite: bool = False,
    ) -> list[str]:
        imported: list[str] = []
        package = Path(package_path)
        if not package.exists():
            return imported

        with tempfile.TemporaryDirectory(prefix="skill_unpack_") as temp_dir_str:
            temp_dir = Path(temp_dir_str)
            with tarfile.open(package, mode="r:gz") as archive:
                archive.extractall(path=temp_dir)

            skills_dir = temp_dir / "skills"
            if not skills_dir.exists():
                return imported

            for item in skills_dir.glob("*.json"):
                try:
                    data = json.loads(item.read_text(encoding="utf-8"))
                except json.JSONDecodeError:
                    continue
                skill = SkillRecord.from_dict(data)
                if not overwrite and target_store.load(skill.skill_id) is not None:
                    continue
                target_store.save(skill)
                imported.append(skill.skill_id)

        return imported
