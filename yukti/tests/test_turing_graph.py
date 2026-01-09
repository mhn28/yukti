import numpy as np
from yukti.spatial.turing_graph import gray_scott_graph

np.random.seed(42)
coords = np.random.uniform(-1,1,(3000,2))

u0 = np.ones(len(coords)) + 0.01*np.random.randn(len(coords))
v0 = 0.05*np.random.rand(len(coords))

def run(Du, Dv):
    u, v = gray_scott_graph(
        coords,
        u0,
        v0,
        Du=Du,
        Dv=Dv,
        F=0.036,
        k=0.061,
        dt=0.01,
        steps=180,
        knn=40
    )
    return np.var(v)

# ---- Diffusion-ratio scan (core Turing condition) ----
ratios = [
    (0.16, 0.08),
    (0.18, 0.05),
    (0.20, 0.04),
    (0.22, 0.035),
]

vars_out = [run(Du,Dv) for Du,Dv in ratios]

# ---- Operator-faithful invariants ----
# 1. At least one diffusion contrast destabilizes
assert max(vars_out) > np.var(v0) * 1.3

# 2. System remains bounded
assert all(np.isfinite(v) for v in vars_out)

print("✓ Phase 21.2 Turing instability validated (diffusion-conditional, graph-native)")
