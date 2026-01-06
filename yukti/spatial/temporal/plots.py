import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from yukti.spatial.lisa_plots import plot_lisa
import os

def plot_dynamic_lisa(coords, time, lisa_results, out_dir):
    os.makedirs(out_dir, exist_ok=True)

    for t, res in lisa_results.items():
        out = os.path.join(out_dir, f"lisa_t{t}.png")
        plot_lisa(coords[time == t], res["clusters"], out)
