import numpy as np
from yukti.spatial.vector.graph_curl import curl_cloud_2d

np.random.seed(42)

coords = np.random.uniform(-1, 1, (1000, 2))
velocity = np.column_stack([-coords[:,1], coords[:,0]])

res = curl_cloud_2d(coords, velocity, k=20)

assert abs(res["mean"] - 2.0) < 0.15, res["mean"]

print("✓ Phase 20.2 graph-based curl validated (dimension-correct)")
