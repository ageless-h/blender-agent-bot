from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Literal

TargetName = Literal["cursor", "claude-desktop", "windsurf", "vscode", "generic"]


@dataclass(frozen=True)
class MCPServerCommand:
    command: str
    args: list[str]
    env: dict[str, str]

    def to_dict(self) -> dict[str, Any]:
        return {
            "command": self.command,
            "args": self.args,
            "env": self.env,
        }


@dataclass(frozen=True)
class GeneratedConfig:
    target: TargetName
    path: Path
    content: str
    command: MCPServerCommand


def detect_python_executable() -> str:
    override = os.environ.get("PYTHON_EXECUTABLE")
    if override:
        return override
    if sys.executable:
        return sys.executable
    fallback = shutil.which("python3") or shutil.which("python")
    if fallback:
        return fallback
    raise RuntimeError("无法检测 Python 可执行路径，请手动传入 --python-path")


class SetupGenerator:
    def __init__(self, python_path: str | None = None, server_name: str = "blender-mcp") -> None:
        self.python_path = python_path or detect_python_executable()
        self.server_name = server_name

    def generate(
        self,
        target: TargetName,
        output_root: str | Path | None = None,
        *,
        transport: str = "stdio",
        enable_agent_core: bool = False,
        write: bool = True,
    ) -> GeneratedConfig:
        normalized_target = self._normalize_target(target)
        server_command = self._build_server_command(
            transport=transport,
            enable_agent_core=enable_agent_core,
        )
        rendered = self._render_target(normalized_target, server_command)
        output_path = self._resolve_output_path(normalized_target, output_root)
        merged_content = self._merge_existing_config(output_path, normalized_target, rendered)

        if write:
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(
                json.dumps(merged_content, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )

        return GeneratedConfig(
            target=normalized_target,
            path=output_path,
            content=json.dumps(merged_content, ensure_ascii=False, indent=2),
            command=server_command,
        )

    def _normalize_target(self, target: TargetName | str) -> TargetName:
        normalized = str(target).strip().lower()
        aliases: dict[str, TargetName] = {
            "claude": "claude-desktop",
            "claude_desktop": "claude-desktop",
            "claude-desktop": "claude-desktop",
            "cursor": "cursor",
            "windsurf": "windsurf",
            "vscode": "vscode",
            "generic": "generic",
        }
        if normalized not in aliases:
            valid_targets = ", ".join(sorted(set(aliases.values())))
            raise ValueError(f"不支持的 target: {target}，可选值: {valid_targets}")
        return aliases[normalized]

    def _build_server_command(self, *, transport: str, enable_agent_core: bool) -> MCPServerCommand:
        args = ["-m", "server.mcp_server", "--transport", transport]
        env = {
            "BLENDER_MCP_SERVER_NAME": self.server_name,
        }
        if enable_agent_core:
            args.append("--enable-agent-core")
            env["BLENDER_MCP_AGENT_CORE"] = "1"
        return MCPServerCommand(command=self.python_path, args=args, env=env)

    def _resolve_output_path(self, target: TargetName, output_root: str | Path | None) -> Path:
        base_root = Path(output_root).expanduser() if output_root else Path.cwd()

        if target == "cursor":
            return base_root / ".cursor" / "mcp.json"
        if target == "windsurf":
            return base_root / ".windsurf" / "mcp.json"
        if target == "vscode":
            return base_root / ".vscode" / "settings.json"
        if target == "generic":
            return base_root / "blender-mcp.json"
        if target == "claude-desktop":
            return self._resolve_claude_desktop_path(base_root, explicit_root=output_root is not None)
        raise ValueError(f"未知 target: {target}")

    def _resolve_claude_desktop_path(self, base_root: Path, *, explicit_root: bool) -> Path:
        if explicit_root:
            return base_root / "claude_desktop_config.json"
        appdata = os.environ.get("APPDATA")
        if appdata:
            return Path(appdata) / "Claude" / "claude_desktop_config.json"
        if sys.platform == "darwin":
            return Path.home() / "Library" / "Application Support" / "Claude" / "claude_desktop_config.json"
        return Path.home() / ".config" / "Claude" / "claude_desktop_config.json"

    def _render_target(self, target: TargetName, command: MCPServerCommand) -> dict[str, Any]:
        if target in {"cursor", "windsurf", "claude-desktop", "generic"}:
            return {
                "mcpServers": {
                    self.server_name: command.to_dict(),
                }
            }
        if target == "vscode":
            return {
                "mcp.servers": {
                    self.server_name: command.to_dict(),
                }
            }
        raise ValueError(f"未知 target: {target}")

    def _merge_existing_config(
        self,
        output_path: Path,
        target: TargetName,
        rendered: dict[str, Any],
    ) -> dict[str, Any]:
        existing = self._load_json_if_exists(output_path)
        if existing is None:
            return rendered

        merged = dict(existing)
        if target in {"cursor", "windsurf", "claude-desktop", "generic"}:
            merged_servers = dict(existing.get("mcpServers", {}))
            merged_servers.update(rendered.get("mcpServers", {}))
            merged["mcpServers"] = merged_servers
            return merged

        if target == "vscode":
            merged_servers = dict(existing.get("mcp.servers", {}))
            merged_servers.update(rendered.get("mcp.servers", {}))
            merged["mcp.servers"] = merged_servers
            return merged

        return rendered

    @staticmethod
    def _load_json_if_exists(path: Path) -> dict[str, Any] | None:
        if not path.exists():
            return None
        raw_text = path.read_text(encoding="utf-8").strip()
        if not raw_text:
            return {}
        try:
            loaded = json.loads(raw_text)
        except json.JSONDecodeError as error:
            raise ValueError(f"已有配置文件不是合法 JSON: {path}") from error
        if not isinstance(loaded, dict):
            raise ValueError(f"配置文件根节点必须是 JSON object: {path}")
        return loaded


def generate_setup_config(
    target: TargetName,
    output_root: str | Path | None = None,
    *,
    python_path: str | None = None,
    transport: str = "stdio",
    enable_agent_core: bool = False,
    server_name: str = "blender-mcp",
) -> GeneratedConfig:
    generator = SetupGenerator(python_path=python_path, server_name=server_name)
    return generator.generate(
        target=target,
        output_root=output_root,
        transport=transport,
        enable_agent_core=enable_agent_core,
        write=True,
    )


def build_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="生成 MCP 客户端配置文件")
    parser.add_argument(
        "target",
        choices=["cursor", "claude-desktop", "windsurf", "vscode", "generic"],
        help="目标客户端类型",
    )
    parser.add_argument("--output-root", default=None, help="输出根目录（不传则使用默认位置）")
    parser.add_argument("--python-path", default=None, help="Python 可执行路径")
    parser.add_argument("--transport", choices=["stdio", "sse"], default="stdio")
    parser.add_argument("--server-name", default="blender-mcp", help="MCP 服务器名")
    parser.add_argument("--enable-agent-core", action="store_true", help="启用 Agent Core 透传标记")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_argument_parser()
    args = parser.parse_args(argv)
    generated = generate_setup_config(
        target=args.target,
        output_root=args.output_root,
        python_path=args.python_path,
        transport=args.transport,
        enable_agent_core=args.enable_agent_core,
        server_name=args.server_name,
    )
    print(generated.path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
