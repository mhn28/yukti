import numpy as np
from yukti.spatial.reaction_diffusion import reaction_diffusion

np.random.seed(42)
coords = np.random.uniform(-1,1,(1500,2))

# Initial noisy concentration
u0 = np.exp(-np.sum(coords**2, axis=1)) + 0.05*np.random.randn(len(coords))

# Pure diffusion (no reaction)
reaction = lambda u: 0.0

u_final = reaction_diffusion(
    coords,
    u0,
    reaction,
    D=0.5,
    dt=0.02,
    steps=60,
    k=25
)

# ---- Operator-faithful invariants ----
# 1. Diffusion smooths field
assert np.var(u_final) < np.var(u0)

# 2. Mass approximately conserved (graph diffusion)
assert abs(np.mean(u_final) - np.mean(u0)) < 0.02

print("✓ Phase 21.1 graph reaction–diffusion validated (pure diffusion)")
