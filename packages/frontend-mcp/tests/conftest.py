from __future__ import annotations

import sys
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
PACKAGE_ROOT_TEXT = str(PACKAGE_ROOT)

if PACKAGE_ROOT_TEXT not in sys.path:
    sys.path.insert(0, PACKAGE_ROOT_TEXT)
