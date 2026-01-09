import numpy as np
import os
import matplotlib.pyplot as plt
from yukti.plots.figure_multipanel import compose_figure

np.random.seed(42)

x = np.linspace(0,10,50)
y1 = np.sin(x)
y2 = np.cos(x)
groups = [np.random.normal(0,1,30), np.random.normal(1,1,30)]

def panel_a(ax):
    ax.plot(x, y1)
    ax.set_ylabel("sin(x)")

def panel_b(ax):
    ax.plot(x, y2, color="orange")
    ax.set_ylabel("cos(x)")

def panel_c(ax):
    ax.boxplot(groups)
    ax.set_ylabel("Value")

def panel_d(ax):
    sc = ax.scatter(np.random.rand(50), np.random.rand(50), c=np.random.rand(50))
    plt.colorbar(sc, ax=ax, fraction=0.046)
    ax.set_ylabel("Y")

panels = [
    {"plot_fn": panel_a, "label": "A", "subtitle": "Signal 1"},
    {"plot_fn": panel_b, "label": "B", "subtitle": "Signal 2"},
    {"plot_fn": panel_c, "label": "C", "subtitle": "Group comparison"},
    {"plot_fn": panel_d, "label": "D", "subtitle": "Spatial scatter"},
]

out = "phase_i5_outputs/Figure1_ABCD.png"

compose_figure(
    panels=panels,
    title="Figure 1 | Multi-panel statistical summary",
    out_path=out
)

assert os.path.exists(out)
print("✓ Phase I.5 multi-panel figure composer validated")
