import numpy as np
from yukti.spatial.vector.statistics import divergence, curl_2d, anisotropy

# ---- structured grid (required for FD operators) ----
x, y = np.meshgrid(np.linspace(-1, 1, 50), np.linspace(-1, 1, 50))
coords = np.column_stack([x.ravel(), y.ravel()])

# Gradient field: u = x, v = y
velocity = np.column_stack([coords[:,0], coords[:,1]])

# ---- divergence ----
div = divergence(coords, velocity)
assert div["mean"] > 0, "Gradient field must show positive divergence"

# ---- curl (should be near zero for gradient field) ----
curl = curl_2d(coords, velocity)
assert abs(curl["mean"]) < 0.1, "Curl of gradient field must be near zero (FD noise allowed)"

# ---- anisotropy ----
ani = anisotropy(velocity)
assert ani["index"] >= 1, "Anisotropy index must be valid"

print("✓ Phase 19 vector-field statistics validated (operator-faithful)")
