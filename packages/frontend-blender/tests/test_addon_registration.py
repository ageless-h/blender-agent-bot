from __future__ import annotations

import pytest

from conftest import load_module_from_repo


addon_module = load_module_from_repo("__init__.py", "frontend_blender_addon_init")


def test_register_raises_without_bpy() -> None:
    with pytest.raises(RuntimeError, match="缺少 bpy"):
        addon_module.register()


def test_bl_info_has_minimum_fields() -> None:
    assert "name" in addon_module.bl_info
    assert "blender" in addon_module.bl_info
    assert addon_module.bl_info["blender"] >= (4, 2, 0)
