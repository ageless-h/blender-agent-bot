"""Skill store for managing skill capsules.

Provides storage, retrieval, and search for skills.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .skill_capsule import SkillCapsule, SkillCategory


class SkillStore:
    """Storage and retrieval for skill capsules.

    Manages a collection of skills, supporting:
    - Loading skills from files
    - Searching skills by query
    - Filtering by category
    - Fuzzy matching
    """

    def __init__(self, skills_dir: Path | None = None):
        """Initialize skill store.

        Args:
            skills_dir: Directory containing skill JSON files
        """
        self.skills_dir = skills_dir
        self.skills: dict[str, SkillCapsule] = {}

    def load_skill(self, filepath: Path) -> SkillCapsule:
        """Load a skill from JSON file.

        Args:
            filepath: Path to skill JSON file

        Returns:
            Loaded SkillCapsule

        Raises:
            ValueError: If file format is invalid
        """
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        skill = SkillCapsule.from_dict(data)
        self.skills[skill.metadata.name] = skill
        return skill

    def load_all_skills(self) -> int:
        """Load all skills from the skills directory.

        Returns:
            Number of skills loaded
        """
        if not self.skills_dir or not self.skills_dir.exists():
            return 0

        count = 0
        for filepath in self.skills_dir.glob("*.json"):
            try:
                self.load_skill(filepath)
                count += 1
            except Exception as e:
                print(f"Failed to load skill from {filepath}: {e}")

        return count

    def get_skill(self, name: str) -> SkillCapsule | None:
        """Get a skill by name.

        Args:
            name: Skill name

        Returns:
            SkillCapsule or None if not found
        """
        return self.skills.get(name)

    def search_skills(
        self,
        query: str,
        category: SkillCategory | None = None,
        limit: int = 5,
    ) -> list[tuple[SkillCapsule, float]]:
        """Search for skills matching a query.

        Args:
            query: Search query
            category: Optional category filter
            limit: Maximum number of results

        Returns:
            List of (skill, score) tuples, sorted by score descending
        """
        results: list[tuple[SkillCapsule, float]] = []

        for skill in self.skills.values():
            # Filter by category if specified
            if category and skill.metadata.category != category:
                continue

            # Calculate match score
            score = skill.match_score(query)
            if score > 0.0:
                results.append((skill, score))

        # Sort by score descending
        results.sort(key=lambda x: x[1], reverse=True)

        return results[:limit]

    def list_skills(
        self,
        category: SkillCategory | None = None,
    ) -> list[SkillCapsule]:
        """List all skills, optionally filtered by category.

        Args:
            category: Optional category filter

        Returns:
            List of skills
        """
        if category:
            return [skill for skill in self.skills.values() if skill.metadata.category == category]
        return list(self.skills.values())

    def add_skill(self, skill: SkillCapsule) -> None:
        """Add a skill to the store.

        Args:
            skill: Skill to add
        """
        self.skills[skill.metadata.name] = skill

    def remove_skill(self, name: str) -> bool:
        """Remove a skill from the store.

        Args:
            name: Name of skill to remove

        Returns:
            True if skill was removed, False if not found
        """
        if name in self.skills:
            del self.skills[name]
            return True
        return False

    def save_skill(self, skill: SkillCapsule, filepath: Path) -> None:
        """Save a skill to JSON file.

        Args:
            skill: Skill to save
            filepath: Where to save the skill
        """
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(skill.to_dict(), f, indent=2, ensure_ascii=False)


__all__ = ["SkillStore"]
