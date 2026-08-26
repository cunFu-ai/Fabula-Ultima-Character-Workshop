from __future__ import annotations

import ast
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = ROOT / "src"
PACKAGE_ROOT = SOURCE_ROOT / "fu_gm"


def test_all_internal_imports_are_present_in_this_repository() -> None:
    missing: set[str] = set()
    for path in PACKAGE_ROOT.rglob("*.py"):
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                names = [alias.name for alias in node.names]
            elif isinstance(node, ast.ImportFrom) and node.module:
                names = [node.module]
            else:
                continue
            for name in names:
                if not name.startswith("fu_gm"):
                    continue
                relative = Path(*name.split("."))
                module_file = SOURCE_ROOT / f"{relative}.py"
                package_file = SOURCE_ROOT / relative / "__init__.py"
                if not module_file.is_file() and not package_file.is_file():
                    missing.add(name)

    assert not missing, f"Missing standalone modules: {sorted(missing)}"


def test_browser_and_portrait_assets_are_bundled() -> None:
    browser_root = PACKAGE_ROOT / "web" / "character_builder"
    workflow_root = PACKAGE_ROOT / "workflows"

    assert (browser_root / "index.html").is_file()
    assert (browser_root / "app.js").is_file()
    assert (browser_root / "styles.css").is_file()
    assert (workflow_root / "anima-api.json").is_file()
    assert (workflow_root / "krea-lora-api.json").is_file()
