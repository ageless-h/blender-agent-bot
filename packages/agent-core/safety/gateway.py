from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .ast_analyzer import ASTAnalysis, ASTAnalyzer


@dataclass(slots=True)
class SecurityDecision:
    allowed: bool
    level: int | str
    reason: str
    requires_confirmation: bool = False
    ast_analysis: ASTAnalysis | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


class SecurityGateway:
    """分级安全网关（Level 0-3 + 禁止级）。"""

    FORBIDDEN_PATTERNS = (
        "os.system",
        "subprocess",
        "http://",
        "https://",
        "delete_file",
        "remove_file",
        "rmtree",
    )

    def __init__(self, *, analyzer: ASTAnalyzer | None = None) -> None:
        self.analyzer = analyzer or ASTAnalyzer()

    def evaluate(
        self,
        *,
        tool_name: str,
        arguments: dict[str, Any] | None = None,
        generated_code: str | None = None,
    ) -> SecurityDecision:
        args = arguments or {}
        forbidden = self._matches_forbidden(tool_name, args)
        if forbidden:
            return SecurityDecision(
                allowed=False,
                level="forbidden",
                reason=f"命中禁止规则: {forbidden}",
                requires_confirmation=False,
            )

        level = self.classify_level(tool_name, args)
        requires_confirmation = level >= 2

        ast_analysis: ASTAnalysis | None = None
        if generated_code:
            ast_analysis = self.analyzer.analyze(generated_code)
            if ast_analysis.level in {"critical", "high"}:
                return SecurityDecision(
                    allowed=False,
                    level="forbidden",
                    reason=f"AST 风险过高: {ast_analysis.summary}",
                    requires_confirmation=False,
                    ast_analysis=ast_analysis,
                )

        reason = {
            0: "只读操作，自动放行",
            1: "可逆写操作，允许执行",
            2: "高影响操作，需要用户确认",
            3: "危险操作，仅显式授权模式可执行",
        }.get(level, "未知操作等级")

        return SecurityDecision(
            allowed=level < 3,
            level=level,
            reason=reason,
            requires_confirmation=requires_confirmation,
            ast_analysis=ast_analysis,
        )

    def classify_level(self, tool_name: str, arguments: dict[str, Any]) -> int:
        name = tool_name.lower()

        if any(token in name for token in ("get", "list", "query", "inspect", "read")):
            return 0
        if any(token in name for token in ("create", "add", "set", "move", "transform", "update")):
            return 1
        if any(token in name for token in ("delete", "apply", "execute", "batch", "import")):
            return 2

        if arguments.get("dangerous") is True:
            return 3
        return 1

    def _matches_forbidden(self, tool_name: str, arguments: dict[str, Any]) -> str | None:
        scanned_parts = [tool_name, *(str(value) for value in arguments.values())]
        combined = " ".join(scanned_parts).lower()
        for pattern in self.FORBIDDEN_PATTERNS:
            if pattern in combined:
                return pattern
        return None
