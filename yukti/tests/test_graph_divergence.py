import numpy as np
from yukti.spatial.vector.graph_ops import divergence_cloud

np.random.seed(42)

coords = np.random.uniform(-1, 1, (600, 2))
velocity = coords.copy()  # v(x) = x

res = divergence_cloud(coords, velocity, k=15)

# Analytic truth: div = 2
assert abs(res["mean"] - 2.0) < 0.15, res["mean"]

print("✓ Phase 20.1 graph-based divergence validated (dimension-correct)")
