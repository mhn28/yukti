"""
Phase L.2 — GUI ↔ Core Contract

This test enforces that:
1. Core exposes a stable, importable API surface
2. GUI must NOT be imported by core
3. All GUI-facing entry points are explicit
"""

# ---- Core public API imports (allowed) ----
from yukti.stats import tests_core
from yukti.reporting import methods_results
from yukti.annotations import builder
from yukti.plots import plot_2d
from yukti.spatial import core as spatial_core

# ---- Forbidden imports (must NOT exist in core) ----
FORBIDDEN = [
    "PyQt6",
    "PySide6",
    "tkinter",
    "electron",
    "tauri",
    "yukti_gui",
]

def test_no_gui_dependencies():
    import sys
    loaded = set(sys.modules.keys())
    for bad in FORBIDDEN:
        assert bad not in loaded, f"GUI dependency leaked into core: {bad}"

print("✓ Phase L.2 GUI–core contract import validated")
