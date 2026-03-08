from __future__ import annotations

from importlib.util import find_spec
import json
import shutil
from pathlib import Path
from typing import Any
from urllib import error, request

import typer
from rich.table import Table

from .runtime import detect_blender_executable, ensure_runtime, save_runtime_settings

app = typer.Typer(
    help="一键配置向导（模型、endpoint、Blender、IDE 配置）",
    no_args_is_help=False,
    invoke_without_command=True,
)


@app.callback()
def setup_command(
    ctx: typer.Context,
    non_interactive: bool = typer.Option(
        False, "--non-interactive", help="不提问，使用已有配置和默认值"
    ),
    provider: str | None = typer.Option(None, "--provider", help="LLM 提供商"),
    model: str | None = typer.Option(None, "--model", help="默认模型"),
    api_key: str | None = typer.Option(None, "--api-key", help="API Key"),
    endpoint: str | None = typer.Option(None, "--endpoint", help="Agent Core endpoint"),
    blender_path: Path | None = typer.Option(
        None, "--blender-path", help="Blender 可执行文件路径"
    ),
    link_addon: bool = typer.Option(
        True, "--link-addon/--no-link-addon", help="自动链接 Blender Addon"
    ),
) -> None:
    if ctx.invoked_subcommand is not None:
        return

    runtime = ensure_runtime(ctx)
    detected_blender = _detect_blender_versions()
    detected_local_models = _detect_local_model_servers()

    selected_provider = provider or runtime.settings.provider
    selected_model = model or runtime.settings.model
    selected_api_key = api_key or runtime.settings.api_key
    selected_endpoint = endpoint or runtime.settings.endpoint
    selected_blender = (
        str(blender_path.expanduser())
        if blender_path
        else runtime.settings.blender_executable
    )

    if not non_interactive:
        runtime.console.print("[bold]Blender Agent Setup 向导[/bold]")
        selected_provider = (
            typer.prompt(
                "LLM 提供商(openai/anthropic/google/ollama/local)",
                default=selected_provider,
            )
            .strip()
            .lower()
        )
        selected_model = typer.prompt("默认模型", default=selected_model)

        if selected_provider in {"openai", "anthropic", "google"}:
            selected_api_key = typer.prompt(
                "API Key(留空表示保持不变)",
                default=selected_api_key or "",
                hide_input=True,
                show_default=False,
            )
            if not selected_api_key:
                selected_api_key = runtime.settings.api_key

        selected_endpoint = typer.prompt(
            "Agent Core endpoint(可留空)",
            default=selected_endpoint
            or _default_endpoint_for_provider(selected_provider),
        ).strip()
        if not selected_endpoint:
            selected_endpoint = None

        if detected_blender:
            runtime.console.print("检测到 Blender 可执行文件:")
            for index, item in enumerate(detected_blender, start=1):
                runtime.console.print(f"  {index}. {item}")
            selected_index = typer.prompt(
                "选择 Blender (输入序号，0 保持当前)", default="1"
            )
            if selected_index.isdigit() and int(selected_index) > 0:
                chosen = int(selected_index) - 1
                if chosen < len(detected_blender):
                    selected_blender = str(detected_blender[chosen])
        else:
            selected_blender = (
                typer.prompt(
                    "Blender 可执行文件路径(可留空)",
                    default=selected_blender or "",
                ).strip()
                or None
            )

    updated = runtime.settings.model_copy(
        update={
            "provider": selected_provider,
            "model": selected_model,
            "api_key": selected_api_key,
            "endpoint": selected_endpoint,
            "blender_executable": selected_blender,
        }
    )

    runtime.settings = updated
    save_runtime_settings(runtime)

    addon_status = "skipped"
    if link_addon:
        addon_status = _link_engine_addon(runtime)

    validation = _validate_current_settings(runtime)
    _render_setup_summary(runtime, validation, detected_local_models, addon_status)


@app.command("cursor", help="生成 Cursor MCP 配置")
def setup_cursor(
    ctx: typer.Context,
    output: Path | None = typer.Option(None, "--output", help="输出路径"),
    print_only: bool = typer.Option(False, "--print-only", help="仅打印，不写文件"),
) -> None:
    _write_ide_config(ctx=ctx, ide="cursor", output=output, print_only=print_only)


@app.command("vscode", help="生成 VS Code MCP 配置")
def setup_vscode(
    ctx: typer.Context,
    output: Path | None = typer.Option(None, "--output", help="输出路径"),
    print_only: bool = typer.Option(False, "--print-only", help="仅打印，不写文件"),
) -> None:
    _write_ide_config(ctx=ctx, ide="vscode", output=output, print_only=print_only)


@app.command("windsurf", help="生成 Windsurf MCP 配置")
def setup_windsurf(
    ctx: typer.Context,
    output: Path | None = typer.Option(None, "--output", help="输出路径"),
    print_only: bool = typer.Option(False, "--print-only", help="仅打印，不写文件"),
) -> None:
    _write_ide_config(ctx=ctx, ide="windsurf", output=output, print_only=print_only)


def _write_ide_config(
    ctx: typer.Context, ide: str, output: Path | None, print_only: bool
) -> None:
    runtime = ensure_runtime(ctx)
    config = _generate_ide_payload(
        ide=ide,
        endpoint=runtime.settings.endpoint,
        model=runtime.settings.model,
    )
    serialized = json.dumps(config, ensure_ascii=False, indent=2)

    if print_only:
        runtime.console.print(serialized)
        return

    output_path = output.expanduser() if output else _default_ide_config_path(ide)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(serialized, encoding="utf-8")
    runtime.console.print(f"已生成 {ide} 配置: {output_path}")


def _generate_ide_payload(ide: str, endpoint: str | None, model: str) -> dict[str, Any]:
    args, extra_env = _resolve_mcp_launch_config()
    env_payload = {
        "BLENDER_AGENT_ENDPOINT": endpoint or "",
        "BLENDER_AGENT_MODEL": model,
    }
    env_payload.update(extra_env)

    server_payload = {
        "command": "python",
        "args": args,
        "env": env_payload,
    }

    if ide == "vscode":
        return {
            "mcp.servers": {
                "blender-agent": server_payload,
            }
        }

    return {
        "mcpServers": {
            "blender-agent": server_payload,
        }
    }


def _default_ide_config_path(ide: str) -> Path:
    home = Path.home()
    mapping = {
        "cursor": home / ".cursor" / "mcp.json",
        "vscode": home / ".vscode" / "settings.json",
        "windsurf": home / ".windsurf" / "mcp.json",
    }
    return mapping[ide]


def _validate_current_settings(runtime: Any) -> dict[str, Any]:
    blender_file = runtime.settings.blender_executable
    blender_ok = bool(blender_file and Path(blender_file).exists())
    try:
        mcp_args, extra_env = _resolve_mcp_launch_config()
        if mcp_args[:1] == ["-m"]:
            mcp_entrypoint = f"module:{mcp_args[1]}"
        else:
            mcp_entrypoint = f"script:{mcp_args[0]}"
        if "PYTHONPATH" in extra_env:
            mcp_entrypoint = f"{mcp_entrypoint} (PYTHONPATH={extra_env['PYTHONPATH']})"
    except RuntimeError as exc:
        mcp_entrypoint = f"unavailable:{exc}"

    return {
        "blender_binary": "ok" if blender_ok else "missing",
        "agent_core": runtime.backend.check_agent_core().get("status", "unknown"),
        "model": runtime.settings.model,
        "provider": runtime.settings.provider,
        "mcp_entrypoint": mcp_entrypoint,
    }


def _render_setup_summary(
    runtime: Any,
    validation: dict[str, Any],
    model_servers: dict[str, bool],
    addon_status: str,
) -> None:
    table = Table(show_header=True, header_style="bold cyan")
    table.add_column("项")
    table.add_column("结果")
    table.add_row("配置文件", str(runtime.settings_manager.config_path))
    table.add_row("Provider", runtime.settings.provider)
    table.add_row("Model", runtime.settings.model)
    table.add_row("Endpoint", runtime.settings.endpoint or "(未配置)")
    table.add_row(
        "Blender 可执行文件", runtime.settings.blender_executable or "(未配置)"
    )
    table.add_row("Addon 链接", addon_status)
    table.add_row("Blender 状态", validation["blender_binary"])
    table.add_row("Agent Core 状态", validation["agent_core"])
    table.add_row("MCP 入口", validation["mcp_entrypoint"])
    runtime.console.print(table)

    model_table = Table(show_header=True, header_style="bold magenta")
    model_table.add_column("本地模型服务")
    model_table.add_column("状态")
    for name, up in model_servers.items():
        model_table.add_row(name, "online" if up else "offline")
    runtime.console.print(model_table)


def _link_engine_addon(runtime: Any) -> str:
    repo_root = Path(__file__).resolve().parents[3]
    addon_source = repo_root / "packages" / "engine" / "addon"
    target = runtime.settings.config_dir_path / "addons" / "engine-addon"

    if not addon_source.exists():
        return "source_missing"

    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists() or target.is_symlink():
        if target.is_symlink() or target.is_file():
            target.unlink()
        else:
            shutil.rmtree(target)

    try:
        target.symlink_to(addon_source, target_is_directory=True)
        return f"linked:{target}"
    except OSError:
        shutil.copytree(addon_source, target, dirs_exist_ok=True)
        return f"copied:{target}"


def _default_endpoint_for_provider(provider: str) -> str:
    if provider in {"ollama", "local"}:
        return "http://127.0.0.1:11434"
    return "http://127.0.0.1:8000"


def _detect_blender_versions() -> list[Path]:
    detected: list[Path] = []
    executable = detect_blender_executable()
    if executable:
        detected.append(Path(executable))

    base_candidates = [
        Path("C:/Program Files/Blender Foundation"),
        Path.home() / "AppData/Local/Programs/Blender Foundation",
    ]

    for base in base_candidates:
        if not base.exists():
            continue
        for item in sorted(base.glob("Blender */blender.exe"), reverse=True):
            if item not in detected:
                detected.append(item)
    return detected


def _detect_local_model_servers() -> dict[str, bool]:
    targets = {
        "ollama": "http://127.0.0.1:11434/api/tags",
        "vllm": "http://127.0.0.1:8000/v1/models",
        "lm-studio": "http://127.0.0.1:1234/v1/models",
    }
    return {name: _is_http_alive(url) for name, url in targets.items()}


def _is_http_alive(url: str) -> bool:
    try:
        req = request.Request(url=url, method="GET")
        with request.urlopen(req, timeout=1.0):  # noqa: S310
            return True
    except (error.URLError, error.HTTPError, TimeoutError):
        return False


def _resolve_mcp_launch_config() -> tuple[list[str], dict[str, str]]:
    repo_root = Path(__file__).resolve().parents[3]
    frontend_mcp_root = repo_root / "packages" / "frontend-mcp"
    script_path = frontend_mcp_root / "server" / "mcp_server.py"
    if script_path.exists():
        return ["-m", "server.mcp_server"], {"PYTHONPATH": str(frontend_mcp_root)}

    try:
        spec = find_spec("server.mcp_server")
    except ModuleNotFoundError:
        spec = None
    if spec is not None:
        return ["-m", "server.mcp_server"], {}

    raise RuntimeError("未找到可用的 MCP Server 入口(server.mcp_server)")
