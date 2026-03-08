from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class VisualCheckResult:
    passed: bool
    issues: list[str] = field(default_factory=list)
    suggestions: list[str] = field(default_factory=list)
    summary: str = ""
    raw: dict[str, Any] = field(default_factory=dict)


class VisualFeedback:
    """视觉反馈与降级策略。"""

    def __init__(self, *, vision_enabled: bool = True) -> None:
        self.vision_enabled = vision_enabled

    def evaluate(
        self,
        *,
        before_summary: str,
        after_summary: str,
        screenshot_bytes: bytes | None = None,
    ) -> VisualCheckResult:
        if self.vision_enabled and screenshot_bytes:
            size_kb = len(screenshot_bytes) / 1024
            summary = f"已接收截图（{size_kb:.1f}KB），请结合模型视觉能力进一步判断。"
            return VisualCheckResult(
                passed=True,
                summary=summary,
                raw={"screenshot_size": len(screenshot_bytes)},
            )

        return self._textual_diff_check(before_summary=before_summary, after_summary=after_summary)

    def _textual_diff_check(self, *, before_summary: str, after_summary: str) -> VisualCheckResult:
        if before_summary.strip() == after_summary.strip():
            return VisualCheckResult(
                passed=False,
                issues=["操作前后摘要一致，疑似未生效"],
                suggestions=["检查工具参数", "确认目标对象是否选中"],
                summary="文本比对未发现变化",
            )

        before_lines = set(before_summary.splitlines())
        after_lines = set(after_summary.splitlines())
        added = sorted(after_lines - before_lines)
        removed = sorted(before_lines - after_lines)

        summary = "文本比对发现变化"
        issues: list[str] = []
        suggestions: list[str] = []
        if not added and removed:
            issues.append("对象可能被移除")
            suggestions.append("确认是否触发了删除操作")

        return VisualCheckResult(
            passed=True,
            issues=issues,
            suggestions=suggestions,
            summary=summary,
            raw={"added": added, "removed": removed},
        )

    def build_fallback_summary(
        self,
        *,
        scene_summary: str,
        operation_log: list[str] | None = None,
    ) -> str:
        log_text = "\n".join(f"- {item}" for item in (operation_log or []))
        lines = [
            "[视觉降级模式] 当前模型不支持图片理解，使用文本摘要代替截图。",
            "",
            "场景摘要:",
            scene_summary,
        ]
        if log_text:
            lines.extend(["", "操作日志:", log_text])
        return "\n".join(lines)
