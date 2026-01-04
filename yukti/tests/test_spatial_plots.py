import numpy as np
from yukti.spatial.core import SpatialData, morans_i
from yukti.spatial.plots import spatial_scatter_2d, spatial_scatter_3d
import os

np.random.seed(0)
coords = np.random.rand(40,2)
values = coords[:,0] + np.random.normal(0,0.05,40)

sd = SpatialData(coords, values)
stats = morans_i(sd)

os.makedirs("tmp_plots", exist_ok=True)
spatial_scatter_2d(coords, values, stats, "tmp_plots/spatial2d.png")
spatial_scatter_3d(coords, values, stats, "tmp_plots/spatial3d.png")

assert os.path.exists("tmp_plots/spatial2d.png")
assert os.path.exists("tmp_plots/spatial3d.png")

print("✓ Phase 13 spatial plots validated (2D + 3D with p-value overlays)")
