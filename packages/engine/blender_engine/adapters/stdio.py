# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import logging
import subprocess
import time
from typing import Any, Dict

from .types import AdapterResult

logger = logging.getLogger(__name__)


class StdioAdapter:
    """Adapter that communicates with Blender via stdin/stdout subprocess.

    This adapter launches Blender as a subprocess and communicates via
    standard input/output streams. Useful for Blender UI Frontend where
    the addon runs inside Blender and communicates back to the Engine.
    """

    def __init__(
        self,
        blender_executable: str = "blender",
        timeout: float = 30.0,
        background: bool = True,
    ) -> None:
        self.blender_executable = blender_executable
        self.timeout = timeout
        self.background = background
        self._process: subprocess.Popen[bytes] | None = None

    def start(self) -> None:
        """Start the Blender subprocess."""
        if self._process is not None:
            logger.warning("Blender subprocess already running")
            return

        args = [self.blender_executable]
        if self.background:
            args.append("--background")
        args.extend(["--python-expr", "import bpy; bpy.ops.wm.addon_enable(module='blender_engine.addon')"])

        logger.info("Starting Blender subprocess: %s", " ".join(args))
        self._process = subprocess.Popen(
            args,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

    def stop(self) -> None:
        """Stop the Blender subprocess."""
        if self._process is None:
            return

        logger.info("Stopping Blender subprocess")
        if self._process.stdin:
            self._process.stdin.close()
        if self._process.stdout:
            self._process.stdout.close()
        if self._process.stderr:
            self._process.stderr.close()

        self._process.terminate()
        try:
            self._process.wait(timeout=5.0)
        except subprocess.TimeoutExpired:
            logger.warning("Blender subprocess did not terminate, killing")
            self._process.kill()
            self._process.wait()

        self._process = None

    def execute(self, capability: str, payload: Dict[str, Any]) -> AdapterResult:
        """Execute a capability via stdin/stdout communication."""
        if self._process is None:
            self.start()

        if self._process is None or self._process.stdin is None or self._process.stdout is None:
            return AdapterResult(
                ok=False,
                error="Blender subprocess not available",
                timing_ms=0.0,
            )

        started = time.perf_counter()
        logger.debug("Sending capability=%s via stdin", capability)

        try:
            request = json.dumps({"capability": capability, "payload": payload}, ensure_ascii=False)
            self._process.stdin.write((request + "\n").encode("utf-8"))
            self._process.stdin.flush()

            response_line = self._process.stdout.readline()
            elapsed_ms = (time.perf_counter() - started) * 1000.0

            if not response_line:
                return AdapterResult(
                    ok=False,
                    error="Empty response from Blender subprocess",
                    timing_ms=elapsed_ms,
                )

            response = json.loads(response_line.decode("utf-8").strip())
            return AdapterResult(
                ok=response.get("ok", False),
                result=response.get("result"),
                error=response.get("error", {}).get("code") if response.get("error") else None,
                timing_ms=elapsed_ms,
            )

        except json.JSONDecodeError as exc:
            elapsed_ms = (time.perf_counter() - started) * 1000.0
            logger.debug("Invalid JSON response after %.1fms: %s", elapsed_ms, exc)
            return AdapterResult(
                ok=False,
                error="Invalid JSON response from Blender subprocess",
                timing_ms=elapsed_ms,
            )
        except Exception as exc:
            elapsed_ms = (time.perf_counter() - started) * 1000.0
            logger.exception("Error communicating with Blender subprocess")
            return AdapterResult(
                ok=False,
                error=f"Subprocess communication error: {exc}",
                timing_ms=elapsed_ms,
            )

    def __enter__(self) -> StdioAdapter:
        self.start()
        return self

    def __exit__(self, *args: Any) -> None:
        self.stop()
