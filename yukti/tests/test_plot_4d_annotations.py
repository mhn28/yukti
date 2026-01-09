import numpy as np, os
from yukti.plots.plot_4d import plot_4d_trajectory
from yukti.annotations.builder import build_p_annotation

coords = np.cumsum(np.random.randn(50,2), axis=0)
time = np.arange(50)
ann = [build_p_annotation(0.03)]

os.makedirs("tmp_plots", exist_ok=True)
plot_4d_trajectory(coords, time, ann, "tmp_plots/plot4d.png")

assert os.path.exists("tmp_plots/plot4d.png")
print("✓ Phase E.3 (4D annotated plotting) validated")
