import numpy as np
from yukti.spatial.core import SpatialData, morans_i

np.random.seed(42)
coords = np.random.rand(50, 2)
values = coords[:, 0] + np.random.normal(0, 0.05, 50)

sd = SpatialData(coords, values)
res = morans_i(sd)

assert res["I"] > 0
assert res["p"] < 0.05

print("✓ Phase 12 spatial statistics validated (Moran’s I)")
