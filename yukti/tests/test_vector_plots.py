import numpy as np
import os
from yukti.spatial.vector.plots import quiver_2d, streamlines_2d, quiver_3d

np.random.seed(42)

# ---- 2D example ----
coords2d = np.random.rand(40,2)
velocity2d = np.column_stack([
    coords2d[:,0] + 0.1,
    coords2d[:,1] - 0.1
])

q2 = "tmp_plots/quiver2d.png"
s2 = "tmp_plots/stream2d.png"
quiver_2d(coords2d, velocity2d, q2)
streamlines_2d(coords2d, velocity2d, s2)

assert os.path.exists(q2)
assert os.path.exists(s2)

# ---- 3D example ----
coords3d = np.random.rand(30,3)
velocity3d = coords3d * 0.5

q3 = "tmp_plots/quiver3d.png"
quiver_3d(coords3d, velocity3d, q3)

assert os.path.exists(q3)

print("✓ Phase 18 vector field plots validated (2D quiver, streamlines, 3D)")
