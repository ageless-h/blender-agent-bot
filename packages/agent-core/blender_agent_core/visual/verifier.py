"""Visual verification system for Blender operations.

Provides screenshot capture and visual comparison capabilities
to verify that operations produced the expected results.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass
class Screenshot:
    """Represents a screenshot of the Blender viewport."""

    filepath: Path
    timestamp: float
    viewport_type: str  # '3D', 'UV', 'SHADER', etc.
    camera_position: dict[str, float] | None = None
    render_settings: dict[str, Any] | None = None

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary format."""
        return {
            "filepath": str(self.filepath),
            "timestamp": self.timestamp,
            "viewport_type": self.viewport_type,
            "camera_position": self.camera_position,
            "render_settings": self.render_settings,
        }


@dataclass
class VisualComparison:
    """Result of comparing two screenshots."""

    before: Screenshot
    after: Screenshot
    similarity_score: float  # 0.0 to 1.0
    differences_detected: bool
    difference_regions: list[dict[str, Any]] | None = None

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary format."""
        return {
            "before": self.before.to_dict(),
            "after": self.after.to_dict(),
            "similarity_score": self.similarity_score,
            "differences_detected": self.differences_detected,
            "difference_regions": self.difference_regions or [],
        }


class VisualVerifier:
    """Interface for visual verification operations.

    Implementations should provide:
    - Screenshot capture from Blender viewport
    - Image comparison and diff generation
    - Visual validation of operation results
    """

    def capture_screenshot(
        self,
        output_path: Path,
        viewport_type: str = "3D",
    ) -> Screenshot:
        """Capture a screenshot of the current viewport.

        Args:
            output_path: Where to save the screenshot
            viewport_type: Type of viewport to capture

        Returns:
            Screenshot object with metadata

        Raises:
            RuntimeError: If screenshot capture fails
        """
        raise NotImplementedError

    def compare_screenshots(
        self,
        before: Screenshot,
        after: Screenshot,
        threshold: float = 0.95,
    ) -> VisualComparison:
        """Compare two screenshots for differences.

        Args:
            before: Screenshot before operation
            after: Screenshot after operation
            threshold: Similarity threshold (0.0 to 1.0)

        Returns:
            VisualComparison with similarity metrics
        """
        raise NotImplementedError

    def verify_operation(
        self,
        operation_name: str,
        before: Screenshot,
        after: Screenshot,
    ) -> tuple[bool, str]:
        """Verify that an operation produced expected visual changes.

        Args:
            operation_name: Name of the operation
            before: Screenshot before operation
            after: Screenshot after operation

        Returns:
            Tuple of (success, message)
        """
        raise NotImplementedError


class MockVisualVerifier(VisualVerifier):
    """Mock visual verifier for testing without Blender."""

    def __init__(self):
        """Initialize mock verifier."""
        self.screenshots: list[Screenshot] = []

    def capture_screenshot(
        self,
        output_path: Path,
        viewport_type: str = "3D",
    ) -> Screenshot:
        """Mock screenshot capture."""
        import time

        screenshot = Screenshot(
            filepath=output_path,
            timestamp=time.time(),
            viewport_type=viewport_type,
            camera_position={"x": 0.0, "y": 0.0, "z": 5.0},
        )

        self.screenshots.append(screenshot)
        return screenshot

    def compare_screenshots(
        self,
        before: Screenshot,
        after: Screenshot,
        threshold: float = 0.95,
    ) -> VisualComparison:
        """Mock screenshot comparison."""
        # Mock: always detect differences
        return VisualComparison(
            before=before,
            after=after,
            similarity_score=0.85,
            differences_detected=True,
            difference_regions=[{"x": 100, "y": 100, "width": 50, "height": 50}],
        )

    def verify_operation(
        self,
        operation_name: str,
        before: Screenshot,
        after: Screenshot,
    ) -> tuple[bool, str]:
        """Mock operation verification."""
        comparison = self.compare_screenshots(before, after)

        if comparison.differences_detected:
            return True, f"Operation '{operation_name}' produced visual changes"
        else:
            return False, f"Operation '{operation_name}' produced no visible changes"


__all__ = [
    "Screenshot",
    "VisualComparison",
    "VisualVerifier",
    "MockVisualVerifier",
]
