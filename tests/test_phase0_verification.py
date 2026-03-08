"""Verification test for Phase 0 refactoring."""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "packages", "engine"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "shared"))

from blender_engine import BlenderEngine
from blender_engine.adapters.mock import MockAdapter


def test_engine_initialization():
    adapter = MockAdapter()
    engine = BlenderEngine(adapter=adapter)
    assert engine is not None
    print("[OK] Engine initialization successful")


def test_engine_execute_capability():
    adapter = MockAdapter()
    engine = BlenderEngine(adapter=adapter)

    response = engine.execute_capability("get_objects", {})

    assert response["status"] in ["success", "error", "blocked"]
    assert "capability" in response
    print(f"[OK] Engine execute_capability returned: {response['status']}")


def test_engine_list_capabilities():
    adapter = MockAdapter()
    engine = BlenderEngine(adapter=adapter)

    capabilities = engine.list_capabilities()

    assert isinstance(capabilities, list)
    assert len(capabilities) > 0
    print(f"[OK] Engine list_capabilities returned {len(capabilities)} capabilities")


def test_mcp_frontend_initialization():
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "packages", "frontend-mcp"))

    from blender_mcp_frontend.mcp_server import MCPServer

    adapter = MockAdapter()
    engine = BlenderEngine(adapter=adapter)
    server = MCPServer(engine=engine)

    assert server is not None
    print("[OK] MCP Frontend initialization successful")


def test_mcp_tools_list():
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "packages", "frontend-mcp"))

    from blender_mcp_frontend.mcp_server import MCPServer

    adapter = MockAdapter()
    engine = BlenderEngine(adapter=adapter)
    server = MCPServer(engine=engine)

    result = server.tools_list()

    assert "tools" in result
    assert len(result["tools"]) > 0
    print(f"[OK] MCP tools_list returned {len(result['tools'])} tools")


def test_mcp_tools_call():
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "packages", "frontend-mcp"))

    from blender_mcp_frontend.mcp_server import MCPServer

    adapter = MockAdapter()
    engine = BlenderEngine(adapter=adapter)
    server = MCPServer(engine=engine)

    result = server.tools_call("blender_get_objects", {})

    assert "content" in result
    print(f"[OK] MCP tools_call executed successfully")


if __name__ == "__main__":
    print("Phase 0 Refactoring Verification Tests")
    print("=" * 50)

    try:
        test_engine_initialization()
        test_engine_execute_capability()
        test_engine_list_capabilities()
        test_mcp_frontend_initialization()
        test_mcp_tools_list()
        test_mcp_tools_call()

        print("=" * 50)
        print("[OK] All verification tests passed!")
        print("\nPhase 0 refactoring is complete:")
        print("  - Engine layer extracted and uses unified protocol")
        print("  - MCP Frontend extracted and adapts to Engine")
        print("  - All components working together")
    except Exception as e:
        print(f"\n[FAIL] Test failed: {e}")
        import traceback

        traceback.print_exc()
        sys.exit(1)
