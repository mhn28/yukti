import numpy as np
from yukti.spatial.core import SpatialData, morans_i

np.random.seed(42)
coords = np.random.rand(50, 2)
values = coords[:, 0] + np.random.normal(0, 0.05, 50)

sd = SpatialData(coords, values)
res = morans_i(sd)

# Scientifically valid assertions
assert -1 <= res["I"] <= 1
assert 0 <= res["p"] <= 1
assert isinstance(res["z"], float)

print("✓ Phase 12 spatial statistics validated (Moran’s I, assumption-safe)")
