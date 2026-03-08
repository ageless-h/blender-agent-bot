from safety import SecurityGateway


def test_security_gateway_allows_readonly() -> None:
    gateway = SecurityGateway()
    decision = gateway.evaluate(tool_name="get_scene_objects", arguments={})

    assert decision.allowed is True
    assert decision.level == 0
    assert decision.requires_confirmation is False


def test_security_gateway_requires_confirmation_on_delete() -> None:
    gateway = SecurityGateway()
    decision = gateway.evaluate(tool_name="delete_object", arguments={"target": "Cube"})

    assert decision.level == 2
    assert decision.requires_confirmation is True


def test_security_gateway_blocks_dangerous_code() -> None:
    gateway = SecurityGateway()
    decision = gateway.evaluate(
        tool_name="run_python",
        arguments={"script": "test"},
        generated_code="import subprocess\nsubprocess.run(['rm', '-rf', '/'])",
    )

    assert decision.allowed is False
    assert decision.level == "forbidden"
