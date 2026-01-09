"""
Phase L.3 — Adapter contract test
"""
from yukti_gui.adapter import core_api

assert hasattr(core_api, "methods")
assert hasattr(core_api, "results")
assert hasattr(core_api, "plot_2d_with_annotations")

print("✓ Phase L.3 adapter contract validated")
