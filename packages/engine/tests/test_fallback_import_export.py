from __future__ import annotations

from importlib import import_module
from types import SimpleNamespace

fallback = import_module("packages.engine.tools.fallback")


def _build_dummy_bpy(*, include_wm_obj: bool) -> tuple[SimpleNamespace, list[str]]:
    calls: list[str] = []

    def make_operator(name: str):
        def _operator(**kwargs):
            del kwargs
            calls.append(name)
            return {"FINISHED"}

        return _operator

    wm_namespace = {
        "open_mainfile": make_operator("wm.open_mainfile"),
        "save_as_mainfile": make_operator("wm.save_as_mainfile"),
    }
    if include_wm_obj:
        wm_namespace["obj_import"] = make_operator("wm.obj_import")
        wm_namespace["obj_export"] = make_operator("wm.obj_export")

    bpy = SimpleNamespace(
        ops=SimpleNamespace(
            wm=SimpleNamespace(**wm_namespace),
            import_scene=SimpleNamespace(
                obj=make_operator("import_scene.obj"),
                fbx=make_operator("import_scene.fbx"),
                gltf=make_operator("import_scene.gltf"),
            ),
            export_scene=SimpleNamespace(
                obj=make_operator("export_scene.obj"),
                fbx=make_operator("export_scene.fbx"),
                gltf=make_operator("export_scene.gltf"),
            ),
        )
    )
    return bpy, calls


def test_import_export_prefers_wm_obj_import_when_available() -> None:
    bpy, calls = _build_dummy_bpy(include_wm_obj=True)
    original_require_bpy = fallback.require_bpy
    fallback.require_bpy = lambda _: bpy
    try:
        result = fallback.import_export({"action": "import", "format": "obj", "filepath": "a.obj"})
    finally:
        fallback.require_bpy = original_require_bpy

    assert result.success
    assert result.data["operator_id"] == "wm.obj_import"
    assert calls[0] == "wm.obj_import"


def test_import_export_falls_back_to_legacy_obj_operator() -> None:
    bpy, calls = _build_dummy_bpy(include_wm_obj=False)
    original_require_bpy = fallback.require_bpy
    fallback.require_bpy = lambda _: bpy
    try:
        result = fallback.import_export({"action": "import", "format": "obj", "filepath": "b.obj"})
    finally:
        fallback.require_bpy = original_require_bpy

    assert result.success
    assert result.data["operator_id"] == "import_scene.obj"
    assert calls[0] == "import_scene.obj"
