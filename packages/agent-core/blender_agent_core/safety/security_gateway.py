"""Security gateway for operation validation.

Integrates all safety components to validate operations before execution.
"""

from __future__ import annotations

from typing import Any

from .ast_analyzer import ASTAnalyzer, SecurityViolation
from .confirmation import ConfirmationManager
from .security_levels import (
    OperationClassification,
    SecurityLevel,
    SecurityPolicy,
    classify_operation,
)


class SecurityGateway:
    """Central security gateway for validating operations.

    Coordinates:
    - Security level classification
    - AST analysis for code safety
    - User confirmation for risky operations
    - Policy enforcement
    """

    def __init__(
        self,
        policy: SecurityPolicy | None = None,
        confirmation_manager: ConfirmationManager | None = None,
    ):
        """Initialize security gateway.

        Args:
            policy: Security policy to enforce
            confirmation_manager: Manager for user confirmations
        """
        self.policy = policy or SecurityPolicy()
        self.confirmation_manager = confirmation_manager or ConfirmationManager()
        self.ast_analyzer = ASTAnalyzer(self.policy)

    async def validate_operation(
        self,
        operation_name: str,
        arguments: dict[str, Any] | None = None,
        context: dict[str, Any] | None = None,
    ) -> tuple[bool, str | None]:
        """Validate an operation before execution.

        Args:
            operation_name: Name of the operation
            arguments: Operation arguments
            context: Additional context

        Returns:
            Tuple of (is_allowed, reason)
            - is_allowed: True if operation can proceed
            - reason: Explanation if denied
        """
        # Classify the operation
        security_level = classify_operation(operation_name)

        # Check if operation is allowed by policy
        if not self.policy.can_execute_at_level(security_level):
            return (
                False,
                f"Operation '{operation_name}' at level {security_level.value} is not allowed by policy",
            )

        # Create operation classification
        classification = OperationClassification(
            operation_name=operation_name,
            security_level=security_level,
            reason=f"Operation classified as {security_level.value}",
            is_reversible=self._is_reversible(operation_name),
            affected_objects=self._extract_affected_objects(arguments),
        )

        # Check if confirmation is needed
        if security_level.requires_confirmation():
            approved = await self.confirmation_manager.request_confirmation(
                classification,
                context or {},
            )

            if not approved:
                return False, f"User denied operation '{operation_name}'"

        return True, None

    def validate_code(self, code: str) -> tuple[bool, list[SecurityViolation]]:
        """Validate Python code for security issues.

        Args:
            code: Python code to validate

        Returns:
            Tuple of (is_safe, violations)
        """
        if not self.policy.enable_ast_analysis:
            return True, []

        return self.ast_analyzer.is_code_safe(code)

    async def validate_tool_call(
        self,
        tool_name: str,
        tool_arguments: dict[str, Any],
        context: dict[str, Any] | None = None,
    ) -> tuple[bool, str | None]:
        """Validate a tool call before execution.

        Args:
            tool_name: Name of the tool
            tool_arguments: Tool arguments
            context: Additional context

        Returns:
            Tuple of (is_allowed, reason)
        """
        # Check if tool involves code execution
        if "code" in tool_arguments or "script" in tool_arguments:
            code = tool_arguments.get("code") or tool_arguments.get("script")
            if code:
                is_safe, violations = self.validate_code(code)
                if not is_safe:
                    violation_msgs = [
                        f"{v.violation_type} at line {v.line_number}: {v.description}"
                        for v in violations
                    ]
                    return False, f"Code safety violations: {'; '.join(violation_msgs)}"

        # Validate the operation itself
        return await self.validate_operation(tool_name, tool_arguments, context)

    def _is_reversible(self, operation_name: str) -> bool:
        """Check if an operation is reversible.

        Args:
            operation_name: Name of the operation

        Returns:
            True if operation can be undone
        """
        # Operations that are NOT reversible
        irreversible = [
            "delete_all",
            "clear_scene",
            "save_file",
            "load_file",
            "execute_script",
            "install_addon",
        ]

        return not any(keyword in operation_name.lower() for keyword in irreversible)

    def _extract_affected_objects(
        self,
        arguments: dict[str, Any] | None,
    ) -> list[str]:
        """Extract list of affected objects from arguments.

        Args:
            arguments: Operation arguments

        Returns:
            List of object names/IDs
        """
        if not arguments:
            return []

        affected = []

        # Common argument names for objects
        object_keys = ["object", "objects", "target", "targets", "name", "names"]

        for key in object_keys:
            if key in arguments:
                value = arguments[key]
                if isinstance(value, str):
                    affected.append(value)
                elif isinstance(value, list):
                    affected.extend(str(v) for v in value)

        return affected


__all__ = [
    "SecurityGateway",
]
