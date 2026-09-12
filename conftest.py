"""Make `import echonet` (the vendored upstream package) resolve during tests.

`src.echo...` already works as a namespace package once pytest's rootdir is
on sys.path (pytest does this automatically). The vendored echonet package
lives one level deeper, at vendor/echonet_dynamic/echonet, so it needs its
own explicit path entry.
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
_VENDOR_DIR = ROOT / "vendor" / "echonet_dynamic"
if str(_VENDOR_DIR) not in sys.path:
    sys.path.insert(0, str(_VENDOR_DIR))
