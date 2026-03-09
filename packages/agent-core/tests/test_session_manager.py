"""Tests for SessionManager."""

import pytest

from blender_agent_core.session import Session, SessionManager


def test_create_session():
    """Test session creation."""
    manager = SessionManager()
    session = manager.create_session("test-session")

    assert session.session_id == "test-session"
    assert len(session.history) == 0
    assert len(session.context) == 0


def test_create_session_auto_id():
    """Test session creation with auto-generated ID."""
    manager = SessionManager()
    session = manager.create_session()

    assert session.session_id is not None
    assert len(session.session_id) > 0


def test_get_session():
    """Test getting existing session."""
    manager = SessionManager()
    session = manager.create_session("test-session")

    retrieved = manager.get_session("test-session")
    assert retrieved.session_id == session.session_id


def test_get_nonexistent_session():
    """Test getting non-existent session raises error."""
    manager = SessionManager()

    with pytest.raises(ValueError, match="not found"):
        manager.get_session("nonexistent")


def test_get_or_create_session():
    """Test get_or_create_session."""
    manager = SessionManager()

    # Create new
    session1 = manager.get_or_create_session("test-session")
    assert session1.session_id == "test-session"

    # Get existing
    session2 = manager.get_or_create_session("test-session")
    assert session2.session_id == session1.session_id


def test_delete_session():
    """Test session deletion."""
    manager = SessionManager()
    manager.create_session("test-session")

    manager.delete_session("test-session")

    with pytest.raises(ValueError):
        manager.get_session("test-session")


def test_list_sessions():
    """Test listing sessions."""
    manager = SessionManager()
    manager.create_session("session-1")
    manager.create_session("session-2")

    sessions = manager.list_sessions()
    assert len(sessions) == 2
    assert "session-1" in sessions
    assert "session-2" in sessions


def test_session_add_message():
    """Test adding messages to session."""
    session = Session(session_id="test")

    session.add_message("user", "Hello")
    session.add_message("assistant", "Hi there")

    assert len(session.history) == 2
    assert session.history[0]["role"] == "user"
    assert session.history[0]["content"] == "Hello"
    assert session.history[1]["role"] == "assistant"


def test_session_get_history():
    """Test getting session history."""
    session = Session(session_id="test")

    session.add_message("user", "Message 1")
    session.add_message("assistant", "Response 1")
    session.add_message("user", "Message 2")

    # Get all
    history = session.get_history()
    assert len(history) == 3

    # Get last 2
    history = session.get_history(limit=2)
    assert len(history) == 2
    assert history[0]["content"] == "Response 1"


def test_session_clear_history():
    """Test clearing session history."""
    session = Session(session_id="test")

    session.add_message("user", "Hello")
    session.clear_history()

    assert len(session.history) == 0
