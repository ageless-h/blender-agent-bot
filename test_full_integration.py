"""
Full integration test: Blender UI -> Agent Core Server -> Response

This script tests the complete flow:
1. Configure addon to use agent_core_server.py
2. Enable the addon
3. Send a message through the bridge
4. Verify response is received
"""

import sys
import os

# Add project root to path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

try:
    import bpy
except ImportError:
    print("[FAIL] This script must be run from within Blender")
    sys.exit(1)

# Configuration
BLENDER_PYTHON = r"F:\Program Files\blender\blender-5.0.0-windows-x64\5.0\python\bin\python.exe"
SERVER_SCRIPT = os.path.join(project_root, "agent_core_server.py")
ADDON_NAME = "blender_agent_bot"


def test_full_integration():
    """Test full integration flow."""
    print("=" * 60)
    print("Full Integration Test: Blender UI -> Agent Core -> Response")
    print("=" * 60)

    # Step 0: Enable addon if not already enabled
    print("\n[Step 0] Enabling addon...")

    import addon_utils

    # Check if addon is already enabled
    addon_enabled = False
    for mod in addon_utils.modules():
        if mod.__name__ == ADDON_NAME:
            addon_enabled = addon_utils.check(ADDON_NAME)[1]
            break

    if not addon_enabled:
        print(f"Addon not enabled, enabling '{ADDON_NAME}'...")
        try:
            addon_utils.enable(ADDON_NAME, default_set=True, persistent=True)
            print("[PASS] Addon enabled")
        except Exception as e:
            print(f"[FAIL] Failed to enable addon: {e}")
            return False
    else:
        print(f"[PASS] Addon already enabled")

    # Step 1: Configure addon preferences
    print("\n[Step 1] Configuring addon preferences...")

    # Build command to use agent_core_server.py
    # Use simple format without extra quotes - subprocess_bridge will parse it
    command = f"{BLENDER_PYTHON} {SERVER_SCRIPT}"
    print(f"Command: {command}")

    # Get addon preferences
    preferences = bpy.context.preferences.addons.get(ADDON_NAME)
    if preferences is None:
        print(f"[FAIL] Addon '{ADDON_NAME}' not found after enabling")
        return False

    # Set agent command
    preferences.preferences.agent_command = command
    preferences.preferences.auto_start_core = True
    print("[PASS] Addon preferences configured")

    # Step 2: Import and start runtime
    print("\n[Step 2] Starting Agent Core runtime...")

    try:
        from blender_agent_bot.bridge import get_runtime, RuntimeSettings

        runtime = get_runtime()

        # Stop if already running
        if runtime.is_connected():
            print("Runtime already running, restarting...")
            runtime.stop()

        # Start with configured command
        settings = RuntimeSettings(
            command=command, auto_restart=True, max_restart_attempts=3, restart_backoff_seconds=1.0
        )
        runtime.start(settings)

        # Wait a moment for startup
        import time

        time.sleep(2)

        if not runtime.is_connected():
            print(f"[FAIL] Runtime failed to start")
            print(f"Last error: {runtime.last_error}")
            print(f"Logs: {runtime.tail_logs(10)}")
            return False

        print("[PASS] Agent Core runtime started")

    except Exception as e:
        print(f"[FAIL] Failed to start runtime: {e}")
        import traceback

        traceback.print_exc()
        return False

    # Step 3: Send ping message
    print("\n[Step 3] Sending ping message...")

    # Show server logs before sending
    print(f"Server logs: {runtime.tail_logs(5)}")

    try:
        response = runtime.send_request({"type": "ping"}, timeout=5.0)
        print(f"Response: {response}")

        if response.get("type") != "pong":
            print(f"[FAIL] Expected pong, got: {response}")
            print(f"Server logs after ping: {runtime.tail_logs(10)}")
            return False

        print("[PASS] Ping successful")

    except Exception as e:
        print(f"[FAIL] Ping failed: {e}")
        print(f"Server logs after failure: {runtime.tail_logs(10)}")
        return False

    # Step 4: Send user message
    print("\n[Step 4] Sending user message...")

    try:
        response = runtime.send_request(
            {"type": "user_message", "content": "Create a cube", "session_id": "test_session"}, timeout=10.0
        )

        print(f"Response type: {response.get('type')}")
        print(f"Content: {response.get('content', '')[:100]}...")

        if response.get("type") not in ["assistant_message", "response"]:
            print(f"[FAIL] Expected assistant_message, got: {response.get('type')}")
            return False

        print("[PASS] User message processed")

    except Exception as e:
        print(f"[FAIL] User message failed: {e}")
        return False

    # Step 5: Test skill execution
    print("\n[Step 5] Testing skill execution...")

    try:
        response = runtime.send_request(
            {
                "type": "execute_skill",
                "skill_name": "create_cube",
                "parameters": {"name": "IntegrationTestCube", "location": {"x": 1, "y": 1, "z": 1}},
            },
            timeout=10.0,
        )

        print(f"Response type: {response.get('type')}")

        if response.get("type") == "error":
            print(f"[FAIL] Skill execution error: {response.get('error')}")
            return False

        if response.get("type") != "skill_result":
            print(f"[FAIL] Expected skill_result, got: {response.get('type')}")
            return False

        result = response.get("result", {})
        if not result.get("success"):
            print(f"[FAIL] Skill execution not successful: {result}")
            return False

        print("[PASS] Skill execution successful")

    except Exception as e:
        print(f"[FAIL] Skill execution failed: {e}")
        return False

    # Step 6: Test operation validation
    print("\n[Step 6] Testing operation validation...")

    try:
        response = runtime.send_request(
            {"type": "validate_operation", "operation": "create_object", "arguments": {"object_type": "MESH"}},
            timeout=5.0,
        )

        print(f"Response: {response}")

        if response.get("type") != "validation_result":
            print(f"[FAIL] Expected validation_result, got: {response.get('type')}")
            return False

        print(f"Operation allowed: {response.get('allowed')}")
        print(f"Reason: {response.get('reason')}")
        print("[PASS] Operation validation working")

    except Exception as e:
        print(f"[FAIL] Operation validation failed: {e}")
        return False

    # Step 7: Cleanup
    print("\n[Step 7] Cleanup...")

    try:
        runtime.stop()
        print("[PASS] Runtime stopped")
    except Exception as e:
        print(f"[WARN] Cleanup error: {e}")

    print("\n" + "=" * 60)
    print("All integration tests passed!")
    print("=" * 60)

    return True


if __name__ == "__main__":
    success = test_full_integration()

    if not success:
        print("\n[FAIL] Integration test failed")
        sys.exit(1)

    print("\n[SUCCESS] Integration test completed successfully")
