"""
GUI Adapter → Core API (read-only contract)

This file defines the ONLY surface the GUI may use.
No business logic. No state. No side effects.
"""

from yukti.reporting.methods_results import methods, results
from yukti.annotations.builder import build_p_annotation, build_effect_annotation
from yukti.plots.plot_2d import plot_2d_with_annotations

__all__ = [
    "methods",
    "results",
    "build_p_annotation",
    "build_effect_annotation",
    "plot_2d_with_annotations",
]
