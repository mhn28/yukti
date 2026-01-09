import numpy as np
from yukti.spatial.vector.graph_laplacian import graph_laplacian, diffuse

np.random.seed(42)
coords = np.random.uniform(-1,1,(2000,2))

# Quadratic field
values = coords[:,0]**2 + coords[:,1]**2

lap = graph_laplacian(coords, values, k=30)["values"]

# ---- Correct invariants ----
# 1. Mean ≈ 0 (discrete divergence theorem)
assert abs(np.mean(lap)) < 0.05

# 2. Low variance (nearly constant Laplacian)
assert np.std(lap) < 0.5

# 3. Diffusion reduces variance
f2 = diffuse(coords, values, dt=0.02, steps=40, k=30)
assert np.var(f2) < np.var(values)

print("✓ Phase 20.3 graph Laplacian & diffusion validated (operator-correct)")
