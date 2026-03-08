from __future__ import annotations

from io import StringIO

from packages.engine.transport import StdioTransport


def test_stdio_send_and_receive() -> None:
    input_stream = StringIO('{"session_id": "s1", "type": "ping"}\n')
    output_stream = StringIO()
    transport = StdioTransport(stdin=input_stream, stdout=output_stream)

    received = transport.receive(session_id="s1")
    assert received is not None
    assert received["type"] == "ping"

    transport.send({"type": "pong"}, session_id="s1")
    output_stream.seek(0)
    written = output_stream.readline()
    assert '"type": "pong"' in written
    assert '"session_id": "s1"' in written
