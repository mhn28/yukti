import numpy as np
from yukti.spatial.vector.fields import velocity_field, divergence_2d

coords_t = [
    np.array([[0,0],[1,0],[0,1]]),
    np.array([[0.2,0.1],[1.3,0.1],[0.1,1.2]]),
    np.array([[0.5,0.3],[1.7,0.2],[0.3,1.6]])
]
times = [0, 1, 2]

vel = velocity_field(coords_t, times)
assert len(vel) == 2

v01 = vel[(0,1)]
div = divergence_2d(coords_t[0], v01)
assert div.mean() > 0

print("✓ Phase 17 spatio-temporal vector fields validated")
