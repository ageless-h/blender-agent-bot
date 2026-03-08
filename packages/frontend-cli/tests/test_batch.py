from __future__ import annotations

import json
import os
from pathlib import Path

from cli.main import app
from typer.testing import CliRunner


def _make_env(tmp_home: Path) -> dict[str, str]:
    env = os.environ.copy()
    env["HOME"] = str(tmp_home)
    env["USERPROFILE"] = str(tmp_home)
    return env


def test_run_batch_dry_run_with_loop_and_condition() -> None:
    runner = CliRunner()
    with runner.isolated_filesystem():
        home = Path.cwd() / "home"
        env = _make_env(home)

        script = Path("script.yaml")
        script.write_text(
            """
vars:
  prefix: Cube
  ids: [1, 2]
steps:
  - name: create-object
    tool: blender_create_object
    args:
      name: "{{ prefix }}_{{ item }}"
      type: MESH
    loop:
      var: item
      in: "{{ ids }}"
    on_error: stop
  - name: conditional-report
    if: "{{ prefix }} == 'Cube'"
    tool: blender_get_scene
    save_as: latest_scene
""".strip(),
            encoding="utf-8",
        )

        result = runner.invoke(
            app,
            ["run", str(script), "--dry-run", "--output", "json"],
            env=env,
            color=False,
        )
        assert result.exit_code == 0

        payload = json.loads(result.output)
        assert len(payload) == 3
        assert payload[0]["status"] == "success"
        assert payload[1]["status"] == "success"
        assert payload[2]["status"] == "success"
        assert payload[0]["detail"]["dry_run"] is True
