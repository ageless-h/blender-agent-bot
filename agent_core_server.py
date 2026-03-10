"""
Agent Core standalone server for Blender addon.

This script starts the Agent Core as a subprocess that communicates
with the Blender addon via stdin/stdout.
"""

import sys
import json
import asyncio
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from blender_agent_core.llm import MockAdapter
from blender_agent_core.safety import SecurityGateway, SecurityPolicy
from blender_agent_core.skills import SkillStore, SkillExecutor


class AgentCoreServer:
    """Agent Core server for stdin/stdout communication."""

    def __init__(self):
        """Initialize the server."""
        # Use MockAdapter for testing (no API key needed)
        self.llm_adapter = MockAdapter(
            response_text="I'll help you with that.", supports_tools=True, supports_streaming=False
        )

        # Initialize security
        policy = SecurityPolicy(allow_high_risk=False, enable_ast_analysis=True)
        self.security_gateway = SecurityGateway(policy=policy)

        # Initialize skills
        skills_dir = project_root / "skills" / "builtin"
        self.skill_store = SkillStore(skills_dir=skills_dir)
        if skills_dir.exists():
            self.skill_store.load_all_skills()

        self.running = True

    async def handle_message(self, message: dict) -> dict:
        """Handle incoming message from Blender addon."""
        msg_type = message.get("type")
        request_id = message.get("request_id")  # Preserve request_id for bridge routing

        if msg_type == "ping":
            response = {"type": "pong", "status": "ok", "event": "response"}
            if request_id:
                response["request_id"] = request_id
            return response

        elif msg_type == "user_message":
            content = message.get("content", "")
            session_id = message.get("session_id", "default")

            try:
                # Use MockAdapter directly for testing
                messages = [{"role": "user", "content": content}]
                response = await self.llm_adapter.generate(messages)

                result = {
                    "type": "assistant_message",
                    "event": "response",
                    "content": response.content,
                    "session_id": session_id,
                    "tool_calls": response.tool_calls if hasattr(response, "tool_calls") else [],
                }
                if request_id:
                    result["request_id"] = request_id
                return result
            except Exception as e:
                error_response = {"type": "error", "event": "error", "error": str(e), "session_id": session_id}
                if request_id:
                    error_response["request_id"] = request_id
                return error_response

        elif msg_type == "execute_skill":
            skill_name = message.get("skill_name")
            parameters = message.get("parameters", {})

            try:
                skill = self.skill_store.get_skill(skill_name)
                if not skill:
                    error_response = {"type": "error", "event": "error", "error": f"Skill '{skill_name}' not found"}
                    if request_id:
                        error_response["request_id"] = request_id
                    return error_response

                # Mock tool executor for testing
                async def mock_tool_executor(tool_name: str, args: dict):
                    return {"success": True, "tool": tool_name, "args": args}

                executor = SkillExecutor(tool_executor=mock_tool_executor)
                result = await executor.execute_skill(skill, parameters)

                response = {"type": "skill_result", "event": "response", "skill_name": skill_name, "result": result}
                if request_id:
                    response["request_id"] = request_id
                return response
            except Exception as e:
                error_response = {"type": "error", "event": "error", "error": str(e)}
                if request_id:
                    error_response["request_id"] = request_id
                return error_response

        elif msg_type == "validate_operation":
            operation = message.get("operation")
            arguments = message.get("arguments", {})

            try:
                is_allowed, reason = await self.security_gateway.validate_operation(operation, arguments)

                response = {
                    "type": "validation_result",
                    "event": "response",
                    "operation": operation,
                    "allowed": is_allowed,
                    "reason": reason,
                }
                if request_id:
                    response["request_id"] = request_id
                return response
            except Exception as e:
                error_response = {"type": "error", "event": "error", "error": str(e)}
                if request_id:
                    error_response["request_id"] = request_id
                return error_response

        elif msg_type == "shutdown":
            self.running = False
            response = {"type": "shutdown_ack", "event": "response"}
            if request_id:
                response["request_id"] = request_id
            return response

        else:
            error_response = {"type": "error", "event": "error", "error": f"Unknown message type: {msg_type}"}
            if request_id:
                error_response["request_id"] = request_id
            return error_response

    async def run(self):
        """Main server loop."""
        sys.stderr.write("Agent Core server started\n")
        sys.stderr.flush()

        while self.running:
            try:
                # Read line from stdin
                line = sys.stdin.readline()
                if not line:
                    break

                sys.stderr.write(f"Received: {line.strip()[:100]}\n")
                sys.stderr.flush()

                # Parse JSON message
                message = json.loads(line.strip())

                # Handle message
                response = await self.handle_message(message)

                sys.stderr.write(f"Sending: {json.dumps(response)[:100]}\n")
                sys.stderr.flush()

                # Send response to stdout
                sys.stdout.write(json.dumps(response) + "\n")
                sys.stdout.flush()

            except json.JSONDecodeError as e:
                error_response = {"type": "error", "error": f"Invalid JSON: {e}"}
                sys.stdout.write(json.dumps(error_response) + "\n")
                sys.stdout.flush()

            except Exception as e:
                error_response = {"type": "error", "error": f"Server error: {e}"}
                sys.stdout.write(json.dumps(error_response) + "\n")
                sys.stdout.flush()

        sys.stderr.write("Agent Core server stopped\n")
        sys.stderr.flush()


def main():
    """Entry point."""
    server = AgentCoreServer()
    asyncio.run(server.run())


if __name__ == "__main__":
    main()
