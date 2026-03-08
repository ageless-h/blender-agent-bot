from __future__ import annotations

import socket
import time
from importlib import import_module
from threading import Thread

SocketTransport = import_module("packages.engine.transport").SocketTransport


def test_socket_transport_client_parses_buffered_frames() -> None:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 0))
    host, port = server.getsockname()
    server.listen(1)

    def server_worker() -> None:
        conn, _ = server.accept()
        conn.sendall(b'{"type":"ping-1"}\n{"type":"ping-2"}\n')
        conn.close()
        server.close()

    worker = Thread(target=server_worker, daemon=True)
    worker.start()

    transport = SocketTransport(host=host, port=port, mode="client", timeout=1.0, reconnect_retries=0)
    first = transport.receive(timeout=1.0)
    second = transport.receive(timeout=1.0)
    transport.close()
    worker.join(1.0)

    assert first is not None
    assert first["type"] == "ping-1"
    assert second is not None
    assert second["type"] == "ping-2"


def test_socket_transport_server_receive_no_client_non_blocking() -> None:
    transport = SocketTransport(host="127.0.0.1", port=0, mode="server", timeout=5.0, reconnect_retries=0)
    transport.start()

    started = time.perf_counter()
    result = transport.receive(timeout=0.05)
    elapsed = time.perf_counter() - started

    transport.close()

    assert result is None
    assert elapsed < 0.5
