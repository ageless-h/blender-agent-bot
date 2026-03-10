"""Test addon loading in Blender."""

import bpy
import sys


def test_addon_loading():
    """Test if addon can be loaded."""
    addon_name = "blender_agent_bot"

    print(f"\n{'=' * 60}")
    print(f"Testing Addon Loading: {addon_name}")
    print(f"{'=' * 60}\n")

    # Check if addon is available
    import addon_utils

    available_addons = [mod.__name__ for mod in addon_utils.modules()]

    print(f"Total available addons: {len(available_addons)}")

    if addon_name in available_addons:
        print(f"✓ Addon '{addon_name}' found in available addons")
    else:
        print(f"✗ Addon '{addon_name}' NOT found")
        print(f"  First 10 available addons: {available_addons[:10]}")
        return False

    # Try to enable addon
    try:
        bpy.ops.preferences.addon_enable(module=addon_name)
        print(f"✓ Addon '{addon_name}' enabled successfully")
    except Exception as e:
        print(f"✗ Failed to enable addon: {e}")
        import traceback

        traceback.print_exc()
        return False

    # Check if addon is enabled
    if addon_name in bpy.context.preferences.addons:
        print(f"✓ Addon '{addon_name}' is active")
    else:
        print(f"✗ Addon '{addon_name}' not active after enable")
        return False

    # Check for registered classes
    print(f"\nChecking registered classes...")

    expected_panels = ["BLENDERAGENT_PT_chat", "BLENDERAGENT_PT_settings", "BLENDERAGENT_PT_preview"]

    for panel_name in expected_panels:
        if hasattr(bpy.types, panel_name):
            print(f"  ✓ Panel: {panel_name}")
        else:
            print(f"  ✗ Panel NOT found: {panel_name}")

    expected_operators = [
        "BLENDERAGENT_OT_send_message",
        "BLENDERAGENT_OT_undo_action",
        "BLENDERAGENT_OT_confirm_action",
    ]

    for op_name in expected_operators:
        if hasattr(bpy.types, op_name):
            print(f"  ✓ Operator: {op_name}")
        else:
            print(f"  ✗ Operator NOT found: {op_name}")

    print(f"\n{'=' * 60}")
    print(f"✓ ADDON LOADING TEST PASSED")
    print(f"{'=' * 60}\n")

    return True


if __name__ == "__main__":
    try:
        success = test_addon_loading()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n✗ TEST FAILED WITH EXCEPTION: {e}")
        import traceback

        traceback.print_exc()
        sys.exit(1)
