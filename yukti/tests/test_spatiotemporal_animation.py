import numpy as np, os
from yukti.spatial.temporal import SpatioTemporalData
from yukti.spatial.animations import animate_spatiotemporal

np.random.seed(0)
T = 10
N = 40
coords_t = []
values_t = []
times = list(range(T))

base = np.random.rand(N,2)
for t in range(T):
    drift = np.array([t*0.02, 0])
    coords_t.append(base + drift + np.random.normal(0,0.01,(N,2)))
    values_t.append(coords_t[-1][:,0] + np.random.normal(0,0.05,N))

st = SpatioTemporalData(coords_t, values_t, times)

os.makedirs("tmp_plots", exist_ok=True)
out = "tmp_plots/spatiotemporal.mp4"

def stat_fn(i):
    return f"mean={values_t[i].mean():.3f}"

animate_spatiotemporal(st, out, stat_text_fn=stat_fn, fps=5)

assert os.path.exists(out)
print("✓ Phase 15 spatio-temporal (4D) animation validated")
