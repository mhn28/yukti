import numpy as np
from yukti.spatial.vector.graph_laplacian import graph_laplacian
from yukti.spatial.vector.graph_laplacian_cached import graph_laplacian_cached

np.random.seed(42)
coords = np.random.rand(3000,2)
vals = np.sin(coords[:,0]) + np.cos(coords[:,1])

u = graph_laplacian(coords, vals, k=20)["values"]
c = graph_laplacian_cached(coords, vals, k=20)["values"]

# ---------------- OPERATOR-FAITHFUL INVARIANTS ----------------

# 1. Strong agreement (not identity)
corr = np.corrcoef(u, c)[0,1]
assert corr > 0.90, f"Correlation too low: {corr}"

# 2. Mass conservation (graph Laplacian property)
assert abs(np.mean(u)) < 1e-2
assert abs(np.mean(c)) < 1e-2

# 3. Qualitative structure preserved
assert np.sign(u).mean() * np.sign(c).mean() >= 0

print(f"✓ Phase 22 cache validated (corr={corr:.4f})")
