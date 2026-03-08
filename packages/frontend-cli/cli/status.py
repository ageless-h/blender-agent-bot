from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import typer
from rich.table import Table

from .runtime import ensure_runtime


def status_command(
    ctx: typer.Context,
    as_json: bool = typer.Option(False, "--json", help="以 JSON 格式输出"),
) -> None:
    runtime = ensure_runtime(ctx)

    blender_status = runtime.backend.check_blender_connection()
    agent_status = runtime.backend.check_agent_core()

    scene_summary = runtime.backend.call_tool("blender_get_scene", {})
    skill_summary = runtime.backend.call_tool("blender_get_skills", {})

    payload = {
        "blender": blender_status,
        "agent_core": agent_status,
        "model": {
            "provider": runtime.settings.provider,
            "name": runtime.settings.model,
        },
        "scene": {
            "name": scene_summary.get("scene_name", "Scene"),
            "objects_count": scene_summary.get("objects_count", 0),
            "selected_objects": scene_summary.get("selected_objects", []),
        },
        "skills": skill_summary,
        "config": {
            "config_path": str(runtime.settings_manager.config_path),
            "blender_executable": runtime.settings.blender_executable,
            "endpoint": runtime.settings.endpoint,
        },
    }

    if as_json:
        runtime.console.print_json(data=payload)
        return

    _render_status_table(runtime=runtime, payload=payload)


def _render_status_table(runtime: Any, payload: dict[str, Any]) -> None:
    table = Table(show_header=True, header_style="bold cyan")
    table.add_column("检查项")
    table.add_column("状态")
    table.add_column("详情", overflow="fold")

    table.add_row(
        "Blender 连接",
        str(payload["blender"].get("status", "unknown")),
        json.dumps(payload["blender"], ensure_ascii=False),
    )
    table.add_row(
        "Blender 版本",
        str(payload["blender"].get("version", "unknown")),
        "from scene context",
    )
    table.add_row(
        "Agent Core",
        str(payload["agent_core"].get("status", "unknown")),
        json.dumps(payload["agent_core"], ensure_ascii=False),
    )
    table.add_row(
        "模型",
        payload["model"]["name"],
        f"provider={payload['model']['provider']}",
    )
    table.add_row(
        "场景摘要",
        payload["scene"]["name"],
        f"objects={payload['scene']['objects_count']}, selected={payload['scene']['selected_objects']}",
    )
    table.add_row(
        "技能库",
        str(payload["skills"].get("loaded_skills", 0)),
        str(payload["skills"].get("skills_dir", Path.home() / ".blender-agent/skills")),
    )

    runtime.console.print(table)
