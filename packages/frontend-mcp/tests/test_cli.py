from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from cli import main as cli_main

PACKAGE_ROOT = Path(__file__).resolve().parents[1]


def test_cli_setup_subcommand_generates_config(tmp_path) -> None:
    code = cli_main(
        [
            "setup",
            "cursor",
            "--output-root",
            str(tmp_path),
            "--python-path",
            "python",
        ]
    )
    assert code == 0
    assert (tmp_path / ".cursor" / "mcp.json").exists()


def test_module_execution_help_has_no_runpy_warning() -> None:
    server_result = subprocess.run(
        [sys.executable, "-m", "server.mcp_server", "--help"],
        cwd=PACKAGE_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    setup_result = subprocess.run(
        [sys.executable, "-m", "config.setup_generator", "--help"],
        cwd=PACKAGE_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )

    assert server_result.returncode == 0
    assert setup_result.returncode == 0
    assert "RuntimeWarning" not in server_result.stderr
    assert "RuntimeWarning" not in setup_result.stderr
