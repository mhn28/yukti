import numpy as np
import os
from yukti.plots.plot_spatial import plot_spatial_with_annotations

np.random.seed(42)
coords = np.random.rand(80,2)
values = coords[:,0] + np.random.normal(0,0.05,80)

annotations = {
    "p": 0.0041,
    "stars": "**",
    "effect": "Moran's I = 0.31"
}

plot_spatial_with_annotations(
    coords=coords,
    values=values,
    annotations=annotations,
    title="Spatial field with statistical annotation",
    out="phase_i3_spatial_plot.png"
)

assert os.path.exists("phase_i3_spatial_plot.png")
print("✓ Phase I.3 spatial annotation-aware plotting validated")
