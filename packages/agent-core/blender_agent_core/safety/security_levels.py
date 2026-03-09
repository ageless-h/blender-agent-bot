"""Security levels and safety definitions.

Defines the security classification system for Blender operations.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any


class SecurityLevel(Enum):
    """Security classification for operations.

    Levels (from safest to most dangerous):
    - SAFE: Read-only, no side effects
    - LOW: Minor modifications, easily reversible
    - MEDIUM: Significant changes, requires confirmation
    - HIGH: Destructive operations, requires explicit approval
    - CRITICAL: System-level changes, requires elevated permissions
    """

    SAFE = "safe"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

    def requires_confirmation(self) -> bool:
        """Check if this level requires user confirmation.

        Returns:
            True if confirmation is needed
        """
        return self in [SecurityLevel.MEDIUM, SecurityLevel.HIGH, SecurityLevel.CRITICAL]

    def allows_auto_execution(self) -> bool:
        """Check if operations at this level can auto-execute.

        Returns:
            True if auto-execution is allowed
        """
        return self in [SecurityLevel.SAFE, SecurityLevel.LOW]


@dataclass
class SecurityPolicy:
    """Security policy configuration.

    Defines what operations are allowed and under what conditions.
    """

    # Maximum security level allowed without confirmation
    auto_execute_threshold: SecurityLevel = SecurityLevel.LOW

    # Whether to allow HIGH level operations at all
    allow_high_risk: bool = False

    # Whether to allow CRITICAL level operations
    allow_critical: bool = False

    # Whether to perform AST analysis on code execution
    enable_ast_analysis: bool = True

    # Blacklisted function names (never allowed)
    function_blacklist: list[str] | None = None

    # Blacklisted module names (never allowed)
    module_blacklist: list[str] | None = None

    def __post_init__(self):
        """Initialize default blacklists."""
        if self.function_blacklist is None:
            self.function_blacklist = [
                "eval",
                "exec",
                "compile",
                "__import__",
                "open",  # File I/O should go through controlled APIs
                "input",  # No interactive input in automation
            ]

        if self.module_blacklist is None:
            self.module_blacklist = [
                "os",  # System operations
                "sys",  # System configuration
                "subprocess",  # Process execution
                "shutil",  # File operations
                "pathlib",  # File system access
                "socket",  # Network access
                "urllib",  # Network access
                "requests",  # Network access
            ]

    def is_function_allowed(self, function_name: str) -> bool:
        """Check if a function is allowed.

        Args:
            function_name: Name of the function to check

        Returns:
            True if function is allowed
        """
        return function_name not in (self.function_blacklist or [])

    def is_module_allowed(self, module_name: str) -> bool:
        """Check if a module is allowed.

        Args:
            module_name: Name of the module to check

        Returns:
            True if module is allowed
        """
        # Check exact match and parent modules
        blacklist = self.module_blacklist or []
        for blocked in blacklist:
            if module_name == blocked or module_name.startswith(f"{blocked}."):
                return False
        return True

    def can_execute_at_level(self, level: SecurityLevel) -> bool:
        """Check if operations at given level can be executed.

        Args:
            level: Security level to check

        Returns:
            True if execution is allowed
        """
        if level == SecurityLevel.CRITICAL:
            return self.allow_critical

        if level == SecurityLevel.HIGH:
            return self.allow_high_risk

        # SAFE, LOW, MEDIUM are always allowed (with confirmation if needed)
        return True


@dataclass
class OperationClassification:
    """Classification of a specific operation.

    Describes the security characteristics of an operation.
    """

    operation_name: str
    security_level: SecurityLevel
    reason: str
    is_reversible: bool = True
    affected_objects: list[str] | None = None

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary format.

        Returns:
            Dictionary representation
        """
        return {
            "operation_name": self.operation_name,
            "security_level": self.security_level.value,
            "reason": self.reason,
            "is_reversible": self.is_reversible,
            "affected_objects": self.affected_objects or [],
        }


# Predefined operation classifications
OPERATION_CLASSIFICATIONS: dict[str, SecurityLevel] = {
    # SAFE operations (read-only)
    "get_objects": SecurityLevel.SAFE,
    "get_object_properties": SecurityLevel.SAFE,
    "get_scene_info": SecurityLevel.SAFE,
    "get_material_info": SecurityLevel.SAFE,
    "list_collections": SecurityLevel.SAFE,
    "get_camera_info": SecurityLevel.SAFE,
    "get_render_settings": SecurityLevel.SAFE,
    # LOW risk operations (minor, reversible changes)
    "create_primitive": SecurityLevel.LOW,
    "set_object_location": SecurityLevel.LOW,
    "set_object_rotation": SecurityLevel.LOW,
    "set_object_scale": SecurityLevel.LOW,
    "rename_object": SecurityLevel.LOW,
    "set_object_color": SecurityLevel.LOW,
    # MEDIUM risk operations (significant changes)
    "delete_object": SecurityLevel.MEDIUM,
    "apply_modifier": SecurityLevel.MEDIUM,
    "join_objects": SecurityLevel.MEDIUM,
    "separate_object": SecurityLevel.MEDIUM,
    "set_material": SecurityLevel.MEDIUM,
    "create_material": SecurityLevel.MEDIUM,
    "run_operator": SecurityLevel.MEDIUM,
    # HIGH risk operations (destructive, hard to reverse)
    "delete_all_objects": SecurityLevel.HIGH,
    "clear_scene": SecurityLevel.HIGH,
    "save_file": SecurityLevel.HIGH,
    "load_file": SecurityLevel.HIGH,
    "execute_script": SecurityLevel.HIGH,
    # CRITICAL operations (system-level)
    "install_addon": SecurityLevel.CRITICAL,
    "modify_preferences": SecurityLevel.CRITICAL,
    "execute_python": SecurityLevel.CRITICAL,
}


def classify_operation(operation_name: str) -> SecurityLevel:
    """Classify an operation's security level.

    Args:
        operation_name: Name of the operation

    Returns:
        SecurityLevel for this operation
    """
    # Check predefined classifications
    if operation_name in OPERATION_CLASSIFICATIONS:
        return OPERATION_CLASSIFICATIONS[operation_name]

    # Default classification based on name patterns
    if any(keyword in operation_name.lower() for keyword in ["get", "list", "info", "query"]):
        return SecurityLevel.SAFE

    if any(keyword in operation_name.lower() for keyword in ["delete", "remove", "clear"]):
        return SecurityLevel.HIGH

    if any(keyword in operation_name.lower() for keyword in ["execute", "run", "eval"]):
        return SecurityLevel.HIGH

    # Default to MEDIUM for unknown operations
    return SecurityLevel.MEDIUM


__all__ = [
    "SecurityLevel",
    "SecurityPolicy",
    "OperationClassification",
    "OPERATION_CLASSIFICATIONS",
    "classify_operation",
]
