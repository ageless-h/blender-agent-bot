"""AST analyzer for Python code safety.

Analyzes Python code for security risks before execution.
"""

from __future__ import annotations

import ast
from dataclasses import dataclass
from typing import Any

from .security_levels import SecurityLevel, SecurityPolicy


@dataclass
class SecurityViolation:
    """Represents a security violation found in code."""

    violation_type: str
    severity: SecurityLevel
    line_number: int
    description: str
    code_snippet: str | None = None

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary format."""
        return {
            "violation_type": self.violation_type,
            "severity": self.severity.value,
            "line_number": self.line_number,
            "description": self.description,
            "code_snippet": self.code_snippet,
        }


class ASTAnalyzer:
    """Analyzes Python AST for security violations.

    Checks for:
    - Blacklisted functions (eval, exec, etc.)
    - Blacklisted modules (os, sys, etc.)
    - Dangerous operations (file I/O, network access)
    - Code injection patterns
    """

    def __init__(self, policy: SecurityPolicy | None = None):
        """Initialize AST analyzer.

        Args:
            policy: Security policy to enforce (uses default if None)
        """
        self.policy = policy or SecurityPolicy()

    def analyze_code(self, code: str) -> list[SecurityViolation]:
        """Analyze Python code for security violations.

        Args:
            code: Python code to analyze

        Returns:
            List of security violations found

        Raises:
            SyntaxError: If code has syntax errors
        """
        try:
            tree = ast.parse(code)
        except SyntaxError as e:
            return [
                SecurityViolation(
                    violation_type="syntax_error",
                    severity=SecurityLevel.HIGH,
                    line_number=e.lineno or 0,
                    description=f"Syntax error: {e.msg}",
                    code_snippet=e.text,
                )
            ]

        violations: list[SecurityViolation] = []

        # Walk the AST and check each node
        for node in ast.walk(tree):
            violations.extend(self._check_node(node, code))

        return violations

    def _check_node(self, node: ast.AST, code: str) -> list[SecurityViolation]:
        """Check a single AST node for violations.

        Args:
            node: AST node to check
            code: Original code (for line extraction)

        Returns:
            List of violations found in this node
        """
        violations: list[SecurityViolation] = []

        # Check function calls
        if isinstance(node, ast.Call):
            violations.extend(self._check_function_call(node, code))

        # Check imports
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            violations.extend(self._check_import(node, code))

        # Check attribute access
        elif isinstance(node, ast.Attribute):
            violations.extend(self._check_attribute(node, code))

        return violations

    def _check_function_call(self, node: ast.Call, code: str) -> list[SecurityViolation]:
        """Check function call for security issues.

        Args:
            node: Call node
            code: Original code

        Returns:
            List of violations
        """
        violations: list[SecurityViolation] = []

        # Get function name
        func_name = self._get_function_name(node.func)
        if not func_name:
            return violations

        # Check against blacklist
        if not self.policy.is_function_allowed(func_name):
            violations.append(
                SecurityViolation(
                    violation_type="blacklisted_function",
                    severity=SecurityLevel.CRITICAL,
                    line_number=node.lineno,
                    description=f"Blacklisted function call: {func_name}",
                    code_snippet=self._get_line(code, node.lineno),
                )
            )

        # Check for dangerous patterns
        if func_name in ["eval", "exec", "compile"]:
            violations.append(
                SecurityViolation(
                    violation_type="code_execution",
                    severity=SecurityLevel.CRITICAL,
                    line_number=node.lineno,
                    description=f"Dynamic code execution: {func_name}",
                    code_snippet=self._get_line(code, node.lineno),
                )
            )

        elif func_name == "__import__":
            violations.append(
                SecurityViolation(
                    violation_type="dynamic_import",
                    severity=SecurityLevel.HIGH,
                    line_number=node.lineno,
                    description="Dynamic import using __import__",
                    code_snippet=self._get_line(code, node.lineno),
                )
            )

        elif func_name in ["open", "file"]:
            violations.append(
                SecurityViolation(
                    violation_type="file_access",
                    severity=SecurityLevel.HIGH,
                    line_number=node.lineno,
                    description=f"File I/O operation: {func_name}",
                    code_snippet=self._get_line(code, node.lineno),
                )
            )

        return violations

    def _check_import(
        self,
        node: ast.Import | ast.ImportFrom,
        code: str,
    ) -> list[SecurityViolation]:
        """Check import statement for security issues.

        Args:
            node: Import node
            code: Original code

        Returns:
            List of violations
        """
        violations: list[SecurityViolation] = []

        # Get module names
        if isinstance(node, ast.Import):
            modules = [alias.name for alias in node.names]
        else:  # ImportFrom
            modules = [node.module] if node.module else []

        # Check each module
        for module in modules:
            if not self.policy.is_module_allowed(module):
                violations.append(
                    SecurityViolation(
                        violation_type="blacklisted_module",
                        severity=SecurityLevel.HIGH,
                        line_number=node.lineno,
                        description=f"Blacklisted module import: {module}",
                        code_snippet=self._get_line(code, node.lineno),
                    )
                )

        return violations

    def _check_attribute(self, node: ast.Attribute, code: str) -> list[SecurityViolation]:
        """Check attribute access for security issues.

        Args:
            node: Attribute node
            code: Original code

        Returns:
            List of violations
        """
        violations: list[SecurityViolation] = []

        # Check for dangerous attribute patterns
        dangerous_attrs = [
            "__globals__",
            "__builtins__",
            "__code__",
            "__class__",
            "__bases__",
            "__subclasses__",
        ]

        if node.attr in dangerous_attrs:
            violations.append(
                SecurityViolation(
                    violation_type="dangerous_attribute",
                    severity=SecurityLevel.CRITICAL,
                    line_number=node.lineno,
                    description=f"Access to dangerous attribute: {node.attr}",
                    code_snippet=self._get_line(code, node.lineno),
                )
            )

        return violations

    def _get_function_name(self, node: ast.expr) -> str | None:
        """Extract function name from call node.

        Args:
            node: Function expression node

        Returns:
            Function name or None
        """
        if isinstance(node, ast.Name):
            return node.id
        elif isinstance(node, ast.Attribute):
            return node.attr
        return None

    def _get_line(self, code: str, line_number: int) -> str:
        """Get a specific line from code.

        Args:
            code: Full code
            line_number: Line number (1-indexed)

        Returns:
            The line content
        """
        lines = code.split("\n")
        if 0 < line_number <= len(lines):
            return lines[line_number - 1].strip()
        return ""

    def is_code_safe(self, code: str) -> tuple[bool, list[SecurityViolation]]:
        """Check if code is safe to execute.

        Args:
            code: Python code to check

        Returns:
            Tuple of (is_safe, violations)
        """
        violations = self.analyze_code(code)

        # Check if any violations are blocking
        blocking_violations = [
            v for v in violations if v.severity in [SecurityLevel.HIGH, SecurityLevel.CRITICAL]
        ]

        is_safe = len(blocking_violations) == 0
        return is_safe, violations


__all__ = [
    "ASTAnalyzer",
    "SecurityViolation",
]
