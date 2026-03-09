"""Visual verification module.

Provides screenshot capture and visual comparison for operation verification.
"""

from .verifier import (
    MockVisualVerifier,
    Screenshot,
    VisualComparison,
    VisualVerifier,
)

__all__ = [
    "VisualVerifier",
    "Screenshot",
    "VisualComparison",
    "MockVisualVerifier",
]
