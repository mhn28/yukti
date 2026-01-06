import numpy as np
from yukti.spatial.vector.statistics import divergence, curl_2d, anisotropy

np.random.seed(42)

# ---- synthetic expanding field (positive divergence) ----
coords = np.random.rand(100,2)
velocity = coords * 2.0

div = divergence(coords, velocity)
assert div["mean"] > 0

curl = curl_2d(coords, velocity)
assert abs(curl["mean"]) < 1e-2

ani = anisotropy(velocity)
assert ani["index"] >= 1

print("✓ Phase 19 vector-field statistics validated (divergence, curl, anisotropy)")
