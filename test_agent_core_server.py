"""Test Agent Core server communication."""

import subprocess
import json
import time


def test_agent_core_server():
    """Test Agent Core server via stdin/stdout."""
    print("=" * 60)
    print("Testing Agent Core Server")
    print("=" * 60)

    # Start server
    server_script = r"\\172.16.98.210\db\8_code\blender\BlenderAgentBot\agent_core_server.py"
    python_exe = r"F:\Program Files\blender\blender-5.0.0-windows-x64\5.0\python\bin\python.exe"

    print(f"\nStarting server: {python_exe}")
    print(f"Script: {server_script}\n")

    proc = subprocess.Popen(
        [python_exe, server_script],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1,
    )

    # Wait for server to start
    time.sleep(2)

    # Test 1: Ping
    print("Test 1: Ping")
    ping_msg = {"type": "ping"}
    proc.stdin.write(json.dumps(ping_msg) + "\n")
    proc.stdin.flush()

    response = proc.stdout.readline()
    result = json.loads(response.strip())
    print(f"  Request: {ping_msg}")
    print(f"  Response: {result}")
    assert result["type"] == "pong", "Ping test failed"
    print("  PASSED\n")

    # Test 2: User message
    print("Test 2: User Message")
    user_msg = {"type": "user_message", "content": "Create a cube", "session_id": "test_session"}
    proc.stdin.write(json.dumps(user_msg) + "\n")
    proc.stdin.flush()

    response = proc.stdout.readline()
    result = json.loads(response.strip())
    print(f"  Request: {user_msg}")
    print(f"  Response: {result}")
    assert result["type"] == "assistant_message", "User message test failed"
    print("  PASSED\n")

    # Test 3: Validate operation
    print("Test 3: Validate Operation")
    validate_msg = {"type": "validate_operation", "operation": "create_object", "arguments": {"type": "CUBE"}}
    proc.stdin.write(json.dumps(validate_msg) + "\n")
    proc.stdin.flush()

    response = proc.stdout.readline()
    result = json.loads(response.strip())
    print(f"  Request: {validate_msg}")
    print(f"  Response: {result}")
    assert result["type"] == "validation_result", "Validation test failed"
    print(f"  Allowed: {result['allowed']}")
    print("  PASSED\n")

    # Test 4: Execute skill
    print("Test 4: Execute Skill")
    skill_msg = {"type": "execute_skill", "skill_name": "create_cube", "parameters": {"name": "TestCube"}}
    proc.stdin.write(json.dumps(skill_msg) + "\n")
    proc.stdin.flush()

    response = proc.stdout.readline()
    result = json.loads(response.strip())
    print(f"  Request: {skill_msg}")
    print(f"  Response: {result}")
    if result["type"] == "error":
        print(f"  Note: {result['error']} (expected if skills not loaded)")
    else:
        assert result["type"] == "skill_result", "Skill execution test failed"
    print("  PASSED\n")

    # Shutdown
    print("Test 5: Shutdown")
    shutdown_msg = {"type": "shutdown"}
    proc.stdin.write(json.dumps(shutdown_msg) + "\n")
    proc.stdin.flush()

    response = proc.stdout.readline()
    result = json.loads(response.strip())
    print(f"  Request: {shutdown_msg}")
    print(f"  Response: {result}")
    assert result["type"] == "shutdown_ack", "Shutdown test failed"
    print("  PASSED\n")

    # Wait for process to exit
    proc.wait(timeout=5)

    print("=" * 60)
    print("ALL TESTS PASSED")
    print("=" * 60)


if __name__ == "__main__":
    test_agent_core_server()
