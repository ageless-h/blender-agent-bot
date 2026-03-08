from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


def load_module_from_repo(relative_path: str, module_name: str):
    repo_root = Path(__file__).resolve().parents[1]
    target_file = repo_root / relative_path
    spec = importlib.util.spec_from_file_location(module_name, target_file)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"无法加载模块: {target_file}")

    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module
