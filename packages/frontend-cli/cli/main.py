from __future__ import annotations

from importlib.metadata import PackageNotFoundError
from importlib.metadata import version as package_version
from pathlib import Path

import typer

from .batch import run_script_command
from .chat import chat_command
from .config import SettingsManager
from .runtime import build_runtime
from .setup import app as setup_app
from .status import status_command
from .tools import tools_command


def _version_callback(value: bool) -> None:
    if value:
        try:
            current_version = package_version("blender-frontend-cli")
        except PackageNotFoundError:
            current_version = "0.1.0"
        typer.echo(f"blender-agent {current_version}")
        raise typer.Exit()


app = typer.Typer(
    help="BlenderAgentBot CLI 前端。支持 chat、run、setup、status、tools。",
    no_args_is_help=True,
    rich_markup_mode="rich",
)


@app.callback()
def main_callback(
    ctx: typer.Context,
    model: str | None = typer.Option(None, "--model", help="覆盖默认模型"),
    api_key: str | None = typer.Option(None, "--api-key", help="覆盖 API Key"),
    endpoint: str | None = typer.Option(None, "--endpoint", help="覆盖 Agent Core endpoint"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="启用详细日志"),
    config: Path | None = typer.Option(None, "--config", help="指定配置文件路径"),
    version: bool = typer.Option(False, "--version", callback=_version_callback, is_eager=True, help="显示版本并退出"),
) -> None:
    del version
    settings_manager = SettingsManager(config_path=config)
    settings = settings_manager.load()
    settings = settings_manager.apply_overrides(
        settings,
        model=model,
        api_key=api_key,
        endpoint=endpoint,
        verbose=verbose,
    )
    runtime = build_runtime(settings=settings, settings_manager=settings_manager)
    ctx.obj = {"runtime": runtime}


app.command("chat", help="启动交互式聊天 REPL")(chat_command)
app.command("run", help="执行 YAML 批处理脚本")(run_script_command)
app.command("status", help="查看系统连接状态")(status_command)
app.command("tools", help="直接调用引擎工具")(tools_command)
app.add_typer(setup_app, name="setup")


def main() -> None:
    app()


if __name__ == "__main__":
    main()
