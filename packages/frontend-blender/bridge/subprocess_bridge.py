from __future__ import annotations

import os
import shlex
import subprocess
import threading
from collections import deque
from pathlib import Path
from typing import Callable, IO, Mapping

DEFAULT_CORE_COMMAND = "python -m blender_agent_core.stdio_server"


class BridgeProcessError(RuntimeError):
    """Agent Core 子进程相关错误。"""


class AgentProcessBridge:
    """管理 Agent Core 的 stdio 子进程。"""

    def __init__(
        self,
        *,
        command: str | None = None,
        env_overrides: Mapping[str, str] | None = None,
        cwd: str | Path | None = None,
        log_callback: Callable[[str], None] | None = None,
    ) -> None:
        self.command = command
        self.env_overrides = dict(env_overrides or {})
        self.cwd = str(cwd) if cwd is not None else None
        self.log_callback = log_callback

        self._process: subprocess.Popen[str] | None = None
        self._stderr_thread: threading.Thread | None = None
        self._lock = threading.RLock()
        self._stderr_logs: deque[str] = deque(maxlen=200)

    @staticmethod
    def build_command(command: str | None) -> list[str]:
        resolved = (command or "").strip() or os.getenv("BLENDERAGENT_CORE_CMD", "").strip() or DEFAULT_CORE_COMMAND
        return shlex.split(resolved, posix=os.name != "nt")

    def start(self) -> None:
        with self._lock:
            if self.is_running():
                return

            args = self.build_command(self.command)
            if not args:
                raise BridgeProcessError("未能解析 Agent Core 启动命令。")

            env = os.environ.copy()
            env.update(self.env_overrides)

            try:
                self._process = subprocess.Popen(
                    args,
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    bufsize=1,
                    cwd=self.cwd,
                    env=env,
                )
            except OSError as exc:
                raise BridgeProcessError(f"启动 Agent Core 失败: {exc}") from exc

            self._start_stderr_forwarder()

    def stop(self, timeout: float = 3.0) -> None:
        with self._lock:
            if self._process is None:
                return

            process = self._process

            if process.poll() is None:
                process.terminate()
                try:
                    process.wait(timeout=timeout)
                except subprocess.TimeoutExpired:
                    process.kill()
                    process.wait(timeout=timeout)

            self._process = None

            if self._stderr_thread is not None and self._stderr_thread.is_alive():
                self._stderr_thread.join(timeout=timeout)

            self._stderr_thread = None

    def restart(self) -> None:
        self.stop()
        self.start()

    def is_running(self) -> bool:
        return self._process is not None and self._process.poll() is None

    @property
    def process(self) -> subprocess.Popen[str] | None:
        return self._process

    @property
    def stdin(self) -> IO[str] | None:
        if self._process is None:
            return None
        return self._process.stdin

    @property
    def stdout(self) -> IO[str] | None:
        if self._process is None:
            return None
        return self._process.stdout

    def send_line(self, line: str) -> None:
        with self._lock:
            if not self.is_running():
                raise BridgeProcessError("Agent Core 尚未启动。")

            stdin = self.stdin
            if stdin is None:
                raise BridgeProcessError("Agent Core stdin 不可用。")

            try:
                stdin.write(f"{line.rstrip()}\n")
                stdin.flush()
            except OSError as exc:
                raise BridgeProcessError(f"写入 Agent Core 失败: {exc}") from exc

    def tail_logs(self, limit: int = 20) -> list[str]:
        if limit <= 0:
            return []
        return list(self._stderr_logs)[-limit:]

    def _start_stderr_forwarder(self) -> None:
        process = self._process
        if process is None or process.stderr is None:
            return

        self._stderr_thread = threading.Thread(
            target=self._forward_stderr,
            args=(process.stderr,),
            name="blenderagent-bridge-stderr",
            daemon=True,
        )
        self._stderr_thread.start()

    def _forward_stderr(self, stream: IO[str]) -> None:
        while True:
            line = stream.readline()
            if not line:
                break

            text = line.rstrip()
            if not text:
                continue

            self._stderr_logs.append(text)
            if self.log_callback is not None:
                self.log_callback(text)


__all__ = ["AgentProcessBridge", "BridgeProcessError", "DEFAULT_CORE_COMMAND"]
