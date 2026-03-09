"""Skill system data structures.

Defines the Skill Capsule format and skill metadata.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class SkillCategory(Enum):
    """Skill category classification."""

    MODELING = "modeling"
    MATERIALS = "materials"
    LIGHTING = "lighting"
    ANIMATION = "animation"
    RENDERING = "rendering"
    COMPOSITING = "compositing"
    SCRIPTING = "scripting"
    WORKFLOW = "workflow"
    GENERAL = "general"


@dataclass
class SkillParameter:
    """Parameter definition for a skill."""

    name: str
    type: str  # "string", "number", "boolean", "object", etc.
    description: str
    required: bool = True
    default: Any = None

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary format."""
        return {
            "name": self.name,
            "type": self.type,
            "description": self.description,
            "required": self.required,
            "default": self.default,
        }


@dataclass
class SkillExample:
    """Example usage of a skill."""

    description: str
    input: dict[str, Any]
    expected_output: str | None = None

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary format."""
        return {
            "description": self.description,
            "input": self.input,
            "expected_output": self.expected_output,
        }


@dataclass
class SkillMetadata:
    """Metadata for a skill.

    Describes what the skill does, its parameters, and usage examples.
    """

    name: str
    version: str
    description: str
    category: SkillCategory
    author: str | None = None
    tags: list[str] = field(default_factory=list)
    parameters: list[SkillParameter] = field(default_factory=list)
    examples: list[SkillExample] = field(default_factory=list)
    dependencies: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary format."""
        return {
            "name": self.name,
            "version": self.version,
            "description": self.description,
            "category": self.category.value,
            "author": self.author,
            "tags": self.tags,
            "parameters": [p.to_dict() for p in self.parameters],
            "examples": [e.to_dict() for e in self.examples],
            "dependencies": self.dependencies,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> SkillMetadata:
        """Create from dictionary format."""
        return cls(
            name=data["name"],
            version=data["version"],
            description=data["description"],
            category=SkillCategory(data["category"]),
            author=data.get("author"),
            tags=data.get("tags", []),
            parameters=[SkillParameter(**p) for p in data.get("parameters", [])],
            examples=[SkillExample(**e) for e in data.get("examples", [])],
            dependencies=data.get("dependencies", []),
        )


@dataclass
class SkillStep:
    """A single step in a skill's execution plan."""

    tool_name: str
    arguments: dict[str, Any]
    description: str | None = None

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary format."""
        return {
            "tool_name": self.tool_name,
            "arguments": self.arguments,
            "description": self.description,
        }


@dataclass
class SkillCapsule:
    """Complete skill capsule.

    A skill capsule contains:
    - Metadata describing the skill
    - Execution plan (sequence of tool calls)
    - Optional validation logic
    """

    metadata: SkillMetadata
    steps: list[SkillStep] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary format."""
        return {
            "metadata": self.metadata.to_dict(),
            "steps": [s.to_dict() for s in self.steps],
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> SkillCapsule:
        """Create from dictionary format."""
        return cls(
            metadata=SkillMetadata.from_dict(data["metadata"]),
            steps=[SkillStep(**s) for s in data.get("steps", [])],
        )

    def match_score(self, query: str) -> float:
        """Calculate how well this skill matches a query.

        Args:
            query: User query string

        Returns:
            Match score from 0.0 to 1.0
        """
        query_lower = query.lower()
        score = 0.0

        # Check name match
        if self.metadata.name.lower() in query_lower:
            score += 0.4

        # Check description match
        desc_words = self.metadata.description.lower().split()
        query_words = query_lower.split()
        matching_words = sum(1 for word in query_words if word in desc_words)
        if query_words:
            score += 0.3 * (matching_words / len(query_words))

        # Check tag match
        for tag in self.metadata.tags:
            if tag.lower() in query_lower:
                score += 0.1

        # Check category match
        if self.metadata.category.value in query_lower:
            score += 0.2

        return min(score, 1.0)


__all__ = [
    "SkillCategory",
    "SkillParameter",
    "SkillExample",
    "SkillMetadata",
    "SkillStep",
    "SkillCapsule",
]
