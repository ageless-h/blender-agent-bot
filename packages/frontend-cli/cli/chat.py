from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

import typer
from rich.live import Live
from rich.markdown import Markdown

from .runtime import ensure_runtime, save_runtime_settings

CHAT_COMMANDS = ["/undo", "/clear", "/scene", "/screenshot", "/model", "/exit"]


@dataclass(slots=True)
class ChatHistory:
    messages: list[dict[str, Any]] = field(default_factory=list)

    def add(self, role: str, content: str) -> None:
        self.messages.append(
            {
                "role": role,
                "content": content,
                "timestamp": datetime.now().isoformat(timespec="seconds"),
            }
        )

    def undo(self) -> bool:
        removed = False
        while self.messages and self.messages[-1]["role"] == "assistant":
            self.messages.pop()
            removed = True
        if self.messages and self.messages[-1]["role"] == "user":
            self.messages.pop()
            removed = True
        return removed

    def clear(self) -> None:
        self.messages.clear()

    @classmethod
    def load(cls, file_path: Path) -> "ChatHistory":
        if not file_path.exists():
            return cls()
        try:
            payload = json.loads(file_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return cls()
        if not isinstance(payload, list):
            return cls()
        parsed = [item for item in payload if isinstance(item, dict)]
        return cls(messages=parsed)

    def save(self, file_path: Path) -> None:
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(
            json.dumps(self.messages, ensure_ascii=False, indent=2), encoding="utf-8"
        )


def chat_command(
    ctx: typer.Context,
    session: str = typer.Option("default", "--session", help="会话 ID，用于历史隔离"),
    history_file: Path | None = typer.Option(
        None, "--history-file", help="指定历史文件路径"
    ),
    model: str | None = typer.Option(None, "--model", help="仅本次会话覆盖模型"),
    no_history: bool = typer.Option(False, "--no-history", help="禁用历史加载与保存"),
) -> None:
    runtime = ensure_runtime(ctx)
    if model:
        runtime.settings = runtime.settings.model_copy(update={"model": model})

    _enable_tab_completion(
        CHAT_COMMANDS + [tool.name for tool in runtime.backend.list_tools()]
    )

    if history_file is not None:
        target_history_file = history_file.expanduser()
    else:
        target_history_file = runtime.settings.history_dir_path / f"{session}.json"

    history = ChatHistory() if no_history else ChatHistory.load(target_history_file)

    runtime.console.print(Markdown("### Blender Agent Chat"))
    runtime.console.print(
        "输入 `/exit` 退出，`/scene` 查看场景，`/model <name>` 切换模型。"
    )

    while True:
        try:
            user_input = _read_multiline_input()
        except (EOFError, KeyboardInterrupt):
            runtime.console.print("\n会话结束。")
            break

        if not user_input.strip():
            continue

        if user_input.startswith("/"):
            should_exit = _handle_chat_command(
                runtime=runtime, history=history, command=user_input
            )
            if should_exit:
                break
            continue

        history.add("user", user_input)
        assistant_text = runtime.backend.generate_assistant_reply(
            user_message=user_input,
            model_name=runtime.settings.model,
        )

        runtime.console.print("[bold cyan]assistant>[/bold cyan]")
        streamed_text = ""
        with Live(
            Markdown(""), console=runtime.console, refresh_per_second=20, transient=True
        ) as live:
            for token in runtime.backend.stream_text(assistant_text):
                streamed_text += token
                live.update(Markdown(streamed_text))
        runtime.console.print(Markdown(streamed_text))

        history.add("assistant", assistant_text)

    if not no_history:
        history.save(target_history_file)
    save_runtime_settings(runtime)


def _handle_chat_command(runtime: Any, history: ChatHistory, command: str) -> bool:
    parts = command.strip().split(maxsplit=1)
    op = parts[0]
    arg = parts[1] if len(parts) > 1 else ""

    if op == "/exit":
        runtime.console.print("已退出聊天。")
        return True

    if op == "/undo":
        history.undo()
        runtime.backend.call_tool("blender_undo", {})
        runtime.console.print("已撤销上一轮对话。")
        return False

    if op == "/clear":
        history.clear()
        runtime.console.print("聊天历史已清空。")
        return False

    if op == "/scene":
        scene = runtime.backend.call_tool("blender_get_scene", {})
        runtime.console.print_json(data=scene)
        return False

    if op == "/screenshot":
        output_path = arg.strip() if arg else None
        payload = {"output_path": output_path} if output_path else {}
        result = runtime.backend.call_tool("blender_capture_viewport", payload)
        runtime.console.print(f"截图已保存: {result['saved_to']}")
        return False

    if op == "/model":
        model_name = arg.strip()
        if not model_name:
            runtime.console.print(f"当前模型: {runtime.settings.model}")
            return False
        runtime.settings = runtime.settings.model_copy(update={"model": model_name})
        runtime.backend.update_settings(runtime.settings)
        runtime.console.print(f"模型已切换为: {model_name}")
        return False

    runtime.console.print(f"未知命令: {op}")
    runtime.console.print(f"支持命令: {', '.join(CHAT_COMMANDS)}")
    return False


def _read_multiline_input() -> str:
    first_line = input("you> ")

    if first_line.strip() == "```":
        lines: list[str] = []
        while True:
            line = input("... ")
            if line.strip() == "```":
                break
            lines.append(line)
        return "\n".join(lines)

    lines = [first_line]
    while lines[-1].endswith("\\"):
        lines[-1] = lines[-1][:-1]
        lines.append(input("... "))
    return "\n".join(lines)


def _enable_tab_completion(candidates: list[str]) -> None:
    try:
        import readline
    except ImportError:
        return

    words = sorted(set(candidates))

    def _completer(text: str, state: int) -> str | None:
        matched = [word for word in words if word.startswith(text)]
        if state < len(matched):
            return matched[state]
        return None

    set_completer = getattr(readline, "set_completer", None)
    parse_and_bind = getattr(readline, "parse_and_bind", None)
    if callable(set_completer):
        set_completer(_completer)
    if callable(parse_and_bind):
        parse_and_bind("tab: complete")
