from __future__ import annotations

import base64
import json
import re
import shutil
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable
from urllib import error, request

import typer
from rich.console import Console
from rich.table import Table
from rich.tree import Tree

from .config import AppSettings, SettingsManager

ONE_PIXEL_PNG_BASE64 = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO3b6x0AAAAASUVORK5CYII="


@dataclass(slots=True, frozen=True)
class ToolDefinition:
    name: str
    description: str
    layer: str
    parameters: dict[str, Any] = field(default_factory=dict)

    def as_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "description": self.description,
            "layer": self.layer,
            "parameters": self.parameters,
        }


DEFAULT_TOOLS: dict[str, ToolDefinition] = {
    "blender_get_scene": ToolDefinition(
        name="blender_get_scene",
        description="获取当前场景摘要（对象数量、选中对象）",
        layer="perception",
    ),
    "blender_get_objects": ToolDefinition(
        name="blender_get_objects",
        description="列出场景中的对象",
        layer="perception",
    ),
    "blender_list_materials": ToolDefinition(
        name="blender_list_materials",
        description="列出材质信息",
        layer="perception",
    ),
    "blender_capture_viewport": ToolDefinition(
        name="blender_capture_viewport",
        description="截取视口截图并保存到文件",
        layer="perception",
        parameters={"output_path": "str, 可选"},
    ),
    "blender_create_object": ToolDefinition(
        name="blender_create_object",
        description="创建一个对象（本地模拟）",
        layer="imperative",
        parameters={"name": "str", "type": "str"},
    ),
    "blender_modify_object": ToolDefinition(
        name="blender_modify_object",
        description="修改对象属性（本地模拟）",
        layer="imperative",
        parameters={"name": "str", "updates": "object"},
    ),
    "blender_execute_script": ToolDefinition(
        name="blender_execute_script",
        description="执行脚本（本地模拟）",
        layer="fallback",
        parameters={"script": "str"},
    ),
    "blender_undo": ToolDefinition(
        name="blender_undo",
        description="撤销上一步操作（本地模拟）",
        layer="safety",
    ),
    "blender_get_skills": ToolDefinition(
        name="blender_get_skills",
        description="统计已加载技能数量",
        layer="perception",
    ),
}


@dataclass(slots=True)
class RuntimeContext:
    settings: AppSettings
    settings_manager: SettingsManager
    backend: "BackendClient"
    console: Console


class BackendClient:
    def __init__(self, settings: AppSettings):
        self.settings = settings
        self.timeout_seconds = 3.0
        self._scene_state: dict[str, Any] = {
            "scene_name": "Scene",
            "blender_version": "5.0.0-mock",
            "objects": [
                {"name": "Camera", "type": "CAMERA"},
                {"name": "Cube", "type": "MESH"},
                {"name": "Light", "type": "LIGHT"},
            ],
            "selected_objects": ["Cube"],
            "materials": ["Material"],
            "last_tool": None,
        }

    def update_settings(self, settings: AppSettings) -> None:
        self.settings = settings

    def list_tools(self) -> list[ToolDefinition]:
        remote_tools = self._remote_list_tools()
        if remote_tools:
            return remote_tools
        return list(DEFAULT_TOOLS.values())

    def get_tool_info(self, tool_name: str) -> ToolDefinition | None:
        for item in self.list_tools():
            if item.name == tool_name:
                return item
        return None

    def call_tool(
        self, tool_name: str, args: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        payload = args or {}
        remote_result = self._remote_call_tool(tool_name, payload)
        if remote_result is not None:
            return remote_result

        local_handler = {
            "blender_get_scene": self._local_get_scene,
            "blender_get_objects": self._local_get_objects,
            "blender_list_materials": self._local_list_materials,
            "blender_capture_viewport": self._local_capture_viewport,
            "blender_create_object": self._local_create_object,
            "blender_modify_object": self._local_modify_object,
            "blender_execute_script": self._local_execute_script,
            "blender_undo": self._local_undo,
            "blender_get_skills": self._local_get_skills,
        }.get(tool_name)

        if local_handler is None:
            raise RuntimeError(f"未知工具: {tool_name}")

        result = local_handler(payload)
        self._scene_state["last_tool"] = tool_name
        return result

    def check_agent_core(self) -> dict[str, Any]:
        endpoint = self.settings.endpoint
        if not endpoint:
            return {"status": "not_configured", "message": "未配置 endpoint"}

        for route in ("/health", "/status", "/v1/health"):
            response = self._request_json("GET", f"{endpoint}{route}")
            if response is not None:
                return {"status": "running", "endpoint": endpoint, "response": response}

        return {"status": "unreachable", "endpoint": endpoint, "message": "连接失败"}

    def check_blender_connection(self) -> dict[str, Any]:
        try:
            scene = self.call_tool("blender_get_scene", {})
            return {
                "status": "connected",
                "scene": scene.get("scene_name", "Scene"),
                "objects": scene.get("objects_count", 0),
                "version": scene.get("blender_version", "unknown"),
            }
        except Exception as exc:  # noqa: BLE001
            return {"status": "disconnected", "message": str(exc)}

    def generate_assistant_reply(self, user_message: str, model_name: str) -> str:
        lowered = user_message.lower()
        if "scene" in lowered or "场景" in user_message:
            scene = self.call_tool("blender_get_scene", {})
            return (
                f"当前场景为 {scene['scene_name']}，共有 {scene['objects_count']} 个对象，"
                f"选中对象：{', '.join(scene['selected_objects']) or '无'}。"
            )

        if "截图" in user_message or "screenshot" in lowered:
            screenshot = self.call_tool("blender_capture_viewport", {})
            return f"已生成视口截图：{screenshot['saved_to']}"

        if "工具" in user_message or "tool" in lowered:
            tool_names = ", ".join(tool.name for tool in self.list_tools())
            return f"可用工具包括：{tool_names}"

        return f"[model={model_name}] 已收到：{user_message}。你可以输入 /scene 查看场景，或 /screenshot 截图。"

    @staticmethod
    def stream_text(text: str) -> Iterable[str]:
        for chunk in re.findall(r"\S+\s*", text):
            yield chunk

    def _remote_list_tools(self) -> list[ToolDefinition] | None:
        endpoint = self.settings.endpoint
        if not endpoint:
            return None

        response = self._request_json("GET", f"{endpoint}/tools")
        if response is None:
            return None

        if isinstance(response, dict) and "tools" in response:
            tools_payload = response["tools"]
        else:
            tools_payload = response

        if not isinstance(tools_payload, list):
            return None

        parsed: list[ToolDefinition] = []
        for item in tools_payload:
            if not isinstance(item, dict) or "name" not in item:
                continue
            parsed.append(
                ToolDefinition(
                    name=str(item["name"]),
                    description=str(item.get("description", "")),
                    layer=str(item.get("layer", "remote")),
                    parameters=item.get("parameters", {})
                    if isinstance(item.get("parameters", {}), dict)
                    else {},
                )
            )
        return parsed or None

    def _remote_call_tool(
        self, tool_name: str, args: dict[str, Any]
    ) -> dict[str, Any] | None:
        endpoint = self.settings.endpoint
        if not endpoint:
            return None

        requests_to_try = [
            ("POST", f"{endpoint}/tools/call", {"tool": tool_name, "args": args}),
            ("POST", f"{endpoint}/tools/{tool_name}", args),
            ("POST", f"{endpoint}/call", {"name": tool_name, "arguments": args}),
        ]

        for method, url, payload in requests_to_try:
            response = self._request_json(method, url, payload)
            if response is not None:
                if isinstance(response, dict):
                    return response
                return {"result": response}
        return None

    def _request_json(
        self, method: str, url: str, payload: dict[str, Any] | None = None
    ) -> Any:
        body = None
        headers: dict[str, str] = {}
        if payload is not None:
            body = json.dumps(payload).encode("utf-8")
            headers["Content-Type"] = "application/json"

        try:
            req = request.Request(url=url, data=body, headers=headers, method=method)
            with request.urlopen(req, timeout=self.timeout_seconds) as response:  # noqa: S310
                raw = response.read()
        except (error.URLError, error.HTTPError, TimeoutError):
            return None

        if not raw:
            return {}

        try:
            return json.loads(raw.decode("utf-8"))
        except json.JSONDecodeError:
            return {"raw": raw.decode("utf-8", errors="replace")}

    def _local_get_scene(self, _: dict[str, Any]) -> dict[str, Any]:
        objects = self._scene_state["objects"]
        return {
            "scene_name": self._scene_state["scene_name"],
            "blender_version": self._scene_state.get("blender_version", "unknown"),
            "objects_count": len(objects),
            "selected_objects": list(self._scene_state["selected_objects"]),
            "objects": objects,
            "last_tool": self._scene_state["last_tool"],
        }

    def _local_get_objects(self, _: dict[str, Any]) -> dict[str, Any]:
        return {
            "objects": list(self._scene_state["objects"]),
            "count": len(self._scene_state["objects"]),
        }

    def _local_list_materials(self, _: dict[str, Any]) -> dict[str, Any]:
        return {
            "materials": list(self._scene_state["materials"]),
            "count": len(self._scene_state["materials"]),
        }

    def _local_capture_viewport(self, args: dict[str, Any]) -> dict[str, Any]:
        output = args.get("output_path")
        if output:
            output_path = Path(str(output)).expanduser()
        else:
            output_path = (
                Path.cwd() / f"viewport_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            )

        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_bytes(base64.b64decode(ONE_PIXEL_PNG_BASE64))

        return {
            "saved_to": str(output_path),
            "width": 1,
            "height": 1,
            "format": "png",
        }

    def _local_create_object(self, args: dict[str, Any]) -> dict[str, Any]:
        name = str(
            args.get("name") or f"Object_{len(self._scene_state['objects']) + 1}"
        )
        object_type = str(args.get("type") or "MESH")
        self._scene_state["objects"].append({"name": name, "type": object_type})
        self._scene_state["selected_objects"] = [name]
        return {"created": True, "name": name, "type": object_type}

    def _local_modify_object(self, args: dict[str, Any]) -> dict[str, Any]:
        target_name = str(args.get("name") or "")
        updates = args.get("updates", {})

        if not isinstance(updates, dict):
            raise RuntimeError("updates 必须是对象")

        for obj in self._scene_state["objects"]:
            if obj["name"] == target_name:
                obj.update(updates)
                return {"updated": True, "name": target_name, "updates": updates}

        raise RuntimeError(f"对象不存在: {target_name}")

    def _local_execute_script(self, args: dict[str, Any]) -> dict[str, Any]:
        script = str(args.get("script") or "")
        if not script.strip():
            raise RuntimeError("script 不能为空")
        return {
            "executed": True,
            "preview": script[:120],
            "length": len(script),
        }

    def _local_undo(self, _: dict[str, Any]) -> dict[str, Any]:
        return {"undone": True, "message": "已撤销上一步（本地模拟）"}

    def _local_get_skills(self, _: dict[str, Any]) -> dict[str, Any]:
        skills_dir = self.settings.skills_dir_path
        skills_dir.mkdir(parents=True, exist_ok=True)
        total = len(list(skills_dir.glob("*.yaml"))) + len(
            list(skills_dir.glob("*.yml"))
        )
        return {"skills_dir": str(skills_dir), "loaded_skills": total}


def build_runtime(
    settings: AppSettings, settings_manager: SettingsManager
) -> RuntimeContext:
    console = Console()
    backend = BackendClient(settings)
    return RuntimeContext(
        settings=settings,
        settings_manager=settings_manager,
        backend=backend,
        console=console,
    )


def ensure_runtime(ctx: typer.Context) -> RuntimeContext:
    if isinstance(ctx.obj, dict) and "runtime" in ctx.obj:
        runtime = ctx.obj["runtime"]
        if isinstance(runtime, RuntimeContext):
            return runtime

    manager = SettingsManager()
    settings = manager.load()
    runtime = build_runtime(settings=settings, settings_manager=manager)
    ctx.obj = {"runtime": runtime}
    return runtime


def save_runtime_settings(runtime: RuntimeContext) -> None:
    runtime.settings_manager.save(runtime.settings)
    runtime.backend.update_settings(runtime.settings)


def render_data(
    console: Console, payload: dict[str, Any] | list[Any], output: str
) -> None:
    normalized_output = output.lower()
    if normalized_output == "json":
        console.print_json(data=payload)
        return

    if normalized_output == "tree":
        tree = Tree("result")
        _append_to_tree(tree, payload)
        console.print(tree)
        return

    table = Table(show_header=True, header_style="bold cyan")
    table.add_column("字段")
    table.add_column("值", overflow="fold")
    for key, value in _flatten_payload(payload):
        table.add_row(
            str(key),
            json.dumps(value, ensure_ascii=False)
            if isinstance(value, (dict, list))
            else str(value),
        )
    console.print(table)


def _append_to_tree(parent: Tree, value: Any, key: str | None = None) -> None:
    if isinstance(value, dict):
        node = parent.add(str(key) if key else "{}")
        for child_key, child_value in value.items():
            _append_to_tree(node, child_value, child_key)
        return

    if isinstance(value, list):
        node = parent.add(str(key) if key else "[]")
        for index, child in enumerate(value):
            _append_to_tree(node, child, f"[{index}]")
        return

    label = f"{key}: {value}" if key else str(value)
    parent.add(label)


def _flatten_payload(payload: dict[str, Any] | list[Any]) -> Iterable[tuple[str, Any]]:
    if isinstance(payload, dict):
        return payload.items()
    return [(f"[{index}]", item) for index, item in enumerate(payload)]


def detect_blender_executable() -> str | None:
    candidate_from_path = shutil.which("blender")
    if candidate_from_path:
        return candidate_from_path

    windows_candidates = [
        Path("C:/Program Files/Blender Foundation"),
        Path.home() / "AppData/Local/Programs/Blender Foundation",
    ]

    for base_dir in windows_candidates:
        if not base_dir.exists():
            continue
        for executable in sorted(base_dir.glob("Blender */blender.exe"), reverse=True):
            return str(executable)

    return None
