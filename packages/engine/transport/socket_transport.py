from __future__ import annotations

import select
import socket
from collections.abc import Mapping
from typing import Any, Literal

from .base import TransportBase


class SocketTransport(TransportBase):
    def __init__(
        self,
        host: str = "127.0.0.1",
        port: int = 9876,
        mode: Literal["client", "server"] = "client",
        timeout: float = 10.0,
        reconnect_retries: int = 3,
    ) -> None:
        self.host = host
        self.port = port
        self.mode = mode
        self.timeout = timeout
        self.reconnect_retries = max(reconnect_retries, 0)
        self._server_socket: socket.socket | None = None
        self._client_socket: socket.socket | None = None
        self._client_buffer: bytes = b""
        self._client_buffers: dict[str, bytes] = {}
        self._clients: dict[str, socket.socket] = {}
        self._closed = False

    def start(self) -> None:
        if self.mode == "client":
            self._connect_client()
            return

        if self._server_socket is not None:
            return

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((self.host, self.port))
        server.listen(8)
        server.settimeout(self.timeout)
        self._server_socket = server

    def _connect_client(self) -> None:
        if self._client_socket is not None:
            return

        last_error: Exception | None = None
        for _ in range(self.reconnect_retries + 1):
            try:
                sock = socket.create_connection((self.host, self.port), timeout=self.timeout)
                sock.settimeout(self.timeout)
                self._client_socket = sock
                return
            except Exception as exc:
                last_error = exc
        raise RuntimeError(f"unable to connect socket transport: {last_error}")

    def _accept_new_client(self, accept_timeout: float | None = None) -> str | None:
        if self._server_socket is None:
            self.start()
        if self._server_socket is None:
            return None

        active_timeout = self.timeout if accept_timeout is None else max(accept_timeout, 0.0)
        original_timeout = self._server_socket.gettimeout()
        self._server_socket.settimeout(active_timeout)
        try:
            conn, addr = self._server_socket.accept()
        except (socket.timeout, BlockingIOError):
            return None
        finally:
            self._server_socket.settimeout(original_timeout)

        conn.settimeout(self.timeout)
        session_id = f"{addr[0]}:{addr[1]}"
        self._clients[session_id] = conn
        self._client_buffers.setdefault(session_id, b"")
        return session_id

    def health_check(self) -> bool:
        if self._closed:
            return False
        if self.mode == "client":
            return self._client_socket is not None and self._client_socket.fileno() != -1
        return self._server_socket is not None and self._server_socket.fileno() != -1

    def send(self, payload: Mapping[str, Any], *, session_id: str | None = None) -> None:
        if self._closed:
            raise RuntimeError("transport is closed")

        line = self.encode_message(payload)
        if self.mode == "client":
            self._connect_client()
            assert self._client_socket is not None
            self._client_socket.sendall(line)
            return

        if not self._clients:
            self._accept_new_client(accept_timeout=self.timeout)
        if not self._clients:
            raise RuntimeError("no active client session")

        target_session = session_id or next(iter(self._clients.keys()))
        client = self._clients.get(target_session)
        if client is None:
            raise ValueError(f"session not found: {target_session}")
        client.sendall(line)

    def receive(self, *, timeout: float | None = None, session_id: str | None = None) -> dict[str, Any] | None:
        if self._closed:
            return None

        active_timeout = self.timeout if timeout is None else timeout
        if self.mode == "client":
            self._connect_client()
            assert self._client_socket is not None
            self._client_socket.settimeout(active_timeout)
            while b"\n" not in self._client_buffer:
                try:
                    data = self._client_socket.recv(65536)
                except socket.timeout:
                    return None
                if not data:
                    return None
                self._client_buffer += data

            line, self._client_buffer = self._client_buffer.split(b"\n", 1)
            return self.decode_message(line)

        self._accept_new_client(accept_timeout=0.0)
        if not self._clients:
            return None

        target_sockets: list[socket.socket]
        if session_id is None:
            target_sockets = list(self._clients.values())
        else:
            client = self._clients.get(session_id)
            if client is None:
                return None
            target_sockets = [client]

        readable, _, _ = select.select(target_sockets, [], [], active_timeout)
        if not readable:
            return None

        sock = readable[0]
        current_session = next((key for key, value in self._clients.items() if value is sock), None)
        if current_session is None:
            return None

        data = sock.recv(65536)
        if not data:
            self._drop_session(current_session)
            return None

        buffer = self._client_buffers.get(current_session, b"") + data
        if b"\n" not in buffer:
            self._client_buffers[current_session] = buffer
            return None

        line, rest = buffer.split(b"\n", 1)
        self._client_buffers[current_session] = rest
        payload = self.decode_message(line)
        payload.setdefault("session_id", current_session)
        return payload

    def _drop_session(self, session_id: str) -> None:
        sock = self._clients.pop(session_id, None)
        self._client_buffers.pop(session_id, None)
        if sock is not None:
            try:
                sock.close()
            except OSError:
                pass

    def close(self) -> None:
        if self._closed:
            return
        self._closed = True

        if self._client_socket is not None:
            try:
                self._client_socket.close()
            except OSError:
                pass
            self._client_socket = None

        for session_id in list(self._clients.keys()):
            self._drop_session(session_id)

        if self._server_socket is not None:
            try:
                self._server_socket.close()
            except OSError:
                pass
            self._server_socket = None
