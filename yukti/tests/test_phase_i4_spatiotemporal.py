import numpy as np
import os
from yukti.plots.plot_spatiotemporal import plot_spatiotemporal_animation

np.random.seed(42)

n = 60
t = 8

coords = np.random.rand(n,2)
times = np.arange(t)

values = []
for i in range(t):
    values.append(coords[:,0] + i*0.15 + np.random.normal(0,0.05,n))
values = np.array(values)

annotations = {
    "p": 0.0023,
    "stars": "**",
    "effect": "Moran's I increases over time"
}

plot_spatiotemporal_animation(
    coords=coords,
    values_over_time=values,
    times=times,
    annotations=annotations,
    title="4D spatio-temporal dynamics",
    out_mp4="phase_i4_outputs/spatiotemporal.mp4",
    out_gif="phase_i4_outputs/spatiotemporal.gif"
)

assert os.path.exists("phase_i4_outputs/spatiotemporal.mp4")
assert os.path.exists("phase_i4_outputs/spatiotemporal.gif")
print("✓ Phase I.4 4D spatio-temporal animation validated")
