"""Tests for AgentCore."""

import pytest

from blender_agent_core import AgentCore


@pytest.mark.asyncio
async def test_agent_core_init():
    """Test AgentCore initialization."""
    agent = AgentCore()

    assert agent.session_manager is not None
    assert agent.tool_router is not None


@pytest.mark.asyncio
async def test_agent_core_process_creates_session():
    """Test that processing request creates session."""
    agent = AgentCore()

    # Import here to avoid circular import issues
    try:
        from protocol import AgentRequest
    except ImportError:
        import sys
        from pathlib import Path
        import importlib.util

        shared_path = Path(__file__).parent.parent.parent.parent / "shared"
        agent_protocol_path = shared_path / "protocol" / "agent_protocol.py"

        spec = importlib.util.spec_from_file_location("agent_protocol", agent_protocol_path)
        if spec and spec.loader:
            agent_protocol = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(agent_protocol)
            AgentRequest = agent_protocol.AgentRequest

    request = AgentRequest(message="Hello", session_id=None)
    response = await agent.process(request)

    assert response.session_id is not None
    assert len(agent.list_sessions()) == 1


@pytest.mark.asyncio
async def test_agent_core_process_reuses_session():
    """Test that processing with session_id reuses session."""
    agent = AgentCore()

    try:
        from protocol import AgentRequest
    except ImportError:
        import sys
        from pathlib import Path
        import importlib.util

        shared_path = Path(__file__).parent.parent.parent.parent / "shared"
        agent_protocol_path = shared_path / "protocol" / "agent_protocol.py"

        spec = importlib.util.spec_from_file_location("agent_protocol", agent_protocol_path)
        if spec and spec.loader:
            agent_protocol = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(agent_protocol)
            AgentRequest = agent_protocol.AgentRequest

    # First request
    request1 = AgentRequest(message="Hello", session_id="test-session")
    response1 = await agent.process(request1)

    # Second request with same session
    request2 = AgentRequest(message="World", session_id="test-session")
    response2 = await agent.process(request2)

    assert response1.session_id == response2.session_id
    assert len(agent.list_sessions()) == 1

    # Check history
    session = agent.get_session("test-session")
    assert len(session.history) == 4  # 2 user + 2 assistant messages
