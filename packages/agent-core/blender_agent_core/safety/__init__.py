"""Safety module.

Provides security and safety features for operation validation.
"""

from .ast_analyzer import ASTAnalyzer, SecurityViolation
from .confirmation import (
    AutoApproveConfirmation,
    AutoDenyConfirmation,
    ConfirmationManager,
    ConfirmationRequest,
    ConfirmationResponse,
    InteractiveConfirmation,
)
from .security_gateway import SecurityGateway
from .security_levels import (
    OPERATION_CLASSIFICATIONS,
    OperationClassification,
    SecurityLevel,
    SecurityPolicy,
    classify_operation,
)

__all__ = [
    # Security levels
    "SecurityLevel",
    "SecurityPolicy",
    "OperationClassification",
    "OPERATION_CLASSIFICATIONS",
    "classify_operation",
    # AST analysis
    "ASTAnalyzer",
    "SecurityViolation",
    # Confirmation
    "ConfirmationManager",
    "ConfirmationRequest",
    "ConfirmationResponse",
    "InteractiveConfirmation",
    "AutoApproveConfirmation",
    "AutoDenyConfirmation",
    # Gateway
    "SecurityGateway",
]
