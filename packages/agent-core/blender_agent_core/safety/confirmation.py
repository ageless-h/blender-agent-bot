"""User confirmation flow for risky operations.

Handles requesting and processing user approval for operations
that require confirmation.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, Callable

from .security_levels import OperationClassification, SecurityLevel


class ConfirmationResponse(Enum):
    """User's response to a confirmation request."""

    APPROVE = "approve"
    DENY = "deny"
    APPROVE_ALL = "approve_all"  # Approve this and all future similar operations
    DENY_ALL = "deny_all"  # Deny this and all future similar operations


@dataclass
class ConfirmationRequest:
    """Request for user confirmation.

    Contains all information needed for the user to make an informed decision.
    """

    operation: OperationClassification
    context: dict[str, Any]
    request_id: str

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary for serialization.

        Returns:
            Dictionary representation
        """
        return {
            "request_id": self.request_id,
            "operation": self.operation.to_dict(),
            "context": self.context,
        }

    def format_for_user(self) -> str:
        """Format confirmation request for display to user.

        Returns:
            Human-readable confirmation message
        """
        op = self.operation

        message = f"""
⚠️  Confirmation Required

Operation: {op.operation_name}
Security Level: {op.security_level.value.upper()}
Reason: {op.reason}
Reversible: {"Yes" if op.is_reversible else "No"}
"""

        if op.affected_objects:
            message += f"\nAffected Objects: {', '.join(op.affected_objects)}"

        if self.context:
            message += f"\n\nContext:"
            for key, value in self.context.items():
                message += f"\n  {key}: {value}"

        message += "\n\nDo you want to proceed? (approve/deny/approve_all/deny_all)"

        return message


class ConfirmationManager:
    """Manages user confirmation requests.

    Handles:
    - Requesting confirmation from user
    - Tracking approval/denial history
    - Implementing "approve all" / "deny all" policies
    """

    def __init__(
        self,
        confirmation_callback: Callable[[ConfirmationRequest], ConfirmationResponse] | None = None,
    ):
        """Initialize confirmation manager.

        Args:
            confirmation_callback: Function to request user confirmation
                Takes ConfirmationRequest, returns ConfirmationResponse
        """
        self.confirmation_callback = confirmation_callback

        # Track "approve all" / "deny all" decisions
        self.approved_operations: set[str] = set()
        self.denied_operations: set[str] = set()

    async def request_confirmation(
        self,
        operation: OperationClassification,
        context: dict[str, Any] | None = None,
    ) -> bool:
        """Request user confirmation for an operation.

        Args:
            operation: Operation classification
            context: Additional context for the user

        Returns:
            True if approved, False if denied
        """
        # Check if operation was previously approved/denied for all
        if operation.operation_name in self.approved_operations:
            return True

        if operation.operation_name in self.denied_operations:
            return False

        # Check if confirmation is needed
        if not operation.security_level.requires_confirmation():
            return True  # Auto-approve safe operations

        # No callback means auto-deny risky operations
        if not self.confirmation_callback:
            return False

        # Create confirmation request
        import uuid

        request = ConfirmationRequest(
            operation=operation,
            context=context or {},
            request_id=str(uuid.uuid4()),
        )

        # Request user input
        response = self.confirmation_callback(request)

        # Handle response
        if response == ConfirmationResponse.APPROVE:
            return True

        elif response == ConfirmationResponse.DENY:
            return False

        elif response == ConfirmationResponse.APPROVE_ALL:
            self.approved_operations.add(operation.operation_name)
            return True

        elif response == ConfirmationResponse.DENY_ALL:
            self.denied_operations.add(operation.operation_name)
            return False

        # Default to deny
        return False

    def reset_approvals(self) -> None:
        """Clear all "approve all" / "deny all" decisions."""
        self.approved_operations.clear()
        self.denied_operations.clear()

    def approve_operation(self, operation_name: str) -> None:
        """Manually approve an operation for all future requests.

        Args:
            operation_name: Name of operation to approve
        """
        self.approved_operations.add(operation_name)
        # Remove from denied if present
        self.denied_operations.discard(operation_name)

    def deny_operation(self, operation_name: str) -> None:
        """Manually deny an operation for all future requests.

        Args:
            operation_name: Name of operation to deny
        """
        self.denied_operations.add(operation_name)
        # Remove from approved if present
        self.approved_operations.discard(operation_name)


class InteractiveConfirmation:
    """Interactive confirmation handler for CLI/TUI.

    Prompts user via stdin/stdout for confirmation.
    """

    def __call__(self, request: ConfirmationRequest) -> ConfirmationResponse:
        """Request confirmation interactively.

        Args:
            request: Confirmation request

        Returns:
            User's response
        """
        # Display request
        print(request.format_for_user())

        # Get user input
        while True:
            try:
                response = input("> ").strip().lower()

                if response in ["approve", "a", "yes", "y"]:
                    return ConfirmationResponse.APPROVE

                elif response in ["deny", "d", "no", "n"]:
                    return ConfirmationResponse.DENY

                elif response in ["approve_all", "aa", "all"]:
                    return ConfirmationResponse.APPROVE_ALL

                elif response in ["deny_all", "da", "none"]:
                    return ConfirmationResponse.DENY_ALL

                else:
                    print("Invalid response. Please enter: approve/deny/approve_all/deny_all")

            except (EOFError, KeyboardInterrupt):
                # User cancelled - default to deny
                return ConfirmationResponse.DENY


class AutoApproveConfirmation:
    """Auto-approve confirmation handler for testing/automation.

    Automatically approves all requests (use with caution!).
    """

    def __call__(self, request: ConfirmationRequest) -> ConfirmationResponse:
        """Auto-approve all requests.

        Args:
            request: Confirmation request (ignored)

        Returns:
            Always APPROVE
        """
        return ConfirmationResponse.APPROVE


class AutoDenyConfirmation:
    """Auto-deny confirmation handler for maximum safety.

    Automatically denies all requests that require confirmation.
    """

    def __call__(self, request: ConfirmationRequest) -> ConfirmationResponse:
        """Auto-deny all requests.

        Args:
            request: Confirmation request (ignored)

        Returns:
            Always DENY
        """
        return ConfirmationResponse.DENY


__all__ = [
    "ConfirmationResponse",
    "ConfirmationRequest",
    "ConfirmationManager",
    "InteractiveConfirmation",
    "AutoApproveConfirmation",
    "AutoDenyConfirmation",
]
