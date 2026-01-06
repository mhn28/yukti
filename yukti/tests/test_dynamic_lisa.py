import numpy as np
from yukti.spatial.temporal.schema import SpatioTemporalData
from yukti.spatial.temporal.dynamic_lisa import dynamic_lisa
from yukti.spatial.temporal.plots import plot_dynamic_lisa
import os

np.random.seed(0)

n = 40
coords = np.random.rand(n*3, 2)
time = np.repeat([0,1,2], n)

# moving hotspot
values = np.concatenate([
    coords[:n,0],
    coords[n:2*n,0] + 1.5,
    coords[2*n:,0] + 3.0
])

st = SpatioTemporalData(coords, time, values)

res = dynamic_lisa(st)

assert len(res) == 3
assert all(set(r["clusters"]).issubset({"HH","LL","HL","LH","NS"}) for r in res.values())

plot_dynamic_lisa(coords, time, res, "tmp_plots/dynamic_lisa")

print("✓ Phase 16 dynamic spatio-temporal LISA validated")
