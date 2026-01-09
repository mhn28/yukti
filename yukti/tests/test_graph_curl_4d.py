import numpy as np
from yukti.spatial.vector.graph_curl_4d import graph_curl_4d

np.random.seed(42)

# --- rotating field evolving in time ---
n = 1500
coords = np.random.uniform(-1,1,(n,2))
time = np.linspace(0, 2*np.pi, n)

# rotation with temporal phase
velocity = np.zeros_like(coords)
velocity[:,0] = -coords[:,1] * np.cos(time)
velocity[:,1] =  coords[:,0] * np.sin(time)

res = graph_curl_4d(coords, velocity, time, k=20)

# --- Operator-faithful invariants ---
# 1. Non-zero rotational structure
assert res["std"] > 0.01

# 2. Mean bounded (no artificial bias)
assert abs(res["mean"]) < 0.2

print("✓ Phase 20.4 spatio-temporal graph curl (4D) validated")
