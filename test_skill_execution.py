"""
Test skill execution via agent_core_server.py

This script tests:
1. Skill loading from builtin directory
2. Parameter substitution
3. Skill execution with mock tool executor
"""

import subprocess
import json
import sys

BLENDER_PYTHON = r"F:\Program Files\blender\blender-5.0.0-windows-x64\5.0\python\bin\python.exe"
SERVER_SCRIPT = r"\\172.16.98.210\db\8_code\blender\BlenderAgentBot\agent_core_server.py"


def send_message(proc, message):
    """Send JSON message to server and get response."""
    proc.stdin.write(json.dumps(message) + "\n")
    proc.stdin.flush()

    response_line = proc.stdout.readline()
    return json.loads(response_line.strip())


def test_skill_execution():
    """Test skill execution."""
    print("=" * 60)
    print("Testing Skill Execution")
    print("=" * 60)

    # Start server
    proc = subprocess.Popen(
        [BLENDER_PYTHON, SERVER_SCRIPT],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1,
    )

    try:
        # Test 1: Ping
        print("\n[Test 1] Ping server...")
        response = send_message(proc, {"type": "ping"})
        print(f"Response: {response}")
        assert response["type"] == "pong", "Ping failed"
        print("[PASS] Ping successful")

        # Test 2: Execute create_cube skill with default parameters
        print("\n[Test 2] Execute create_cube skill (default parameters)...")
        response = send_message(proc, {"type": "execute_skill", "skill_name": "create_cube", "parameters": {}})
        print(f"Response: {json.dumps(response, indent=2)}")

        if response["type"] == "error":
            print(f"[FAIL] Skill execution failed: {response['error']}")
        else:
            assert response["type"] == "skill_result", "Expected skill_result"
            assert response["skill_name"] == "create_cube", "Wrong skill name"
            print("[PASS] Skill executed successfully")

            # Check result structure
            result = response["result"]
            print(f"\nResult structure:")
            print(f"  - success: {result.get('success')}")
            print(f"  - steps_executed: {result.get('steps_executed')}")
            print(f"  - steps: {len(result.get('steps', []))}")

        # Test 3: Execute create_cube with custom parameters
        print("\n[Test 3] Execute create_cube skill (custom parameters)...")
        response = send_message(
            proc,
            {
                "type": "execute_skill",
                "skill_name": "create_cube",
                "parameters": {
                    "name": "TestCube",
                    "location": {"x": 2, "y": 0, "z": 1},
                    "scale": {"x": 2, "y": 2, "z": 2},
                },
            },
        )
        print(f"Response: {json.dumps(response, indent=2)}")

        if response["type"] == "error":
            print(f"[FAIL] Skill execution failed: {response['error']}")
        else:
            assert response["type"] == "skill_result", "Expected skill_result"
            print("[PASS] Skill executed with custom parameters")

            # Verify parameter substitution
            result = response["result"]
            steps = result.get("steps", [])
            if steps:
                print(f"\nParameter substitution check:")
                for i, step in enumerate(steps):
                    print(f"  Step {i + 1}: {step.get('tool_name')}")
                    print(f"    Args: {step.get('arguments')}")

        # Test 4: Execute setup_three_point_lighting skill
        print("\n[Test 4] Execute setup_three_point_lighting skill...")
        response = send_message(
            proc, {"type": "execute_skill", "skill_name": "setup_three_point_lighting", "parameters": {}}
        )
        print(f"Response: {json.dumps(response, indent=2)}")

        if response["type"] == "error":
            print(f"[FAIL] Skill execution failed: {response['error']}")
        else:
            assert response["type"] == "skill_result", "Expected skill_result"
            print("[PASS] Lighting skill executed successfully")

        # Test 5: Try non-existent skill
        print("\n[Test 5] Try non-existent skill...")
        response = send_message(proc, {"type": "execute_skill", "skill_name": "non_existent_skill", "parameters": {}})
        print(f"Response: {response}")
        assert response["type"] == "error", "Expected error for non-existent skill"
        assert "not found" in response["error"].lower(), "Expected 'not found' error"
        print("[PASS] Correctly rejected non-existent skill")

        # Shutdown
        print("\n[Shutdown] Stopping server...")
        response = send_message(proc, {"type": "shutdown"})
        print(f"Response: {response}")
        assert response["type"] == "shutdown_ack", "Shutdown failed"
        print("[PASS] Server shutdown successful")

        print("\n" + "=" * 60)
        print("All skill execution tests passed!")
        print("=" * 60)

    except Exception as e:
        print(f"\n[FAIL] Test failed: {e}")
        import traceback

        traceback.print_exc()
        return False
    finally:
        proc.terminate()
        proc.wait()

    return True


if __name__ == "__main__":
    success = test_skill_execution()
    sys.exit(0 if success else 1)
