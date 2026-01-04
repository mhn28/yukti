import matplotlib
matplotlib.use("Agg")  # headless safe
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa
import numpy as np

def spatial_scatter_2d(coords, values, stats, out):
    fig, ax = plt.subplots(figsize=(6,5))
    sc = ax.scatter(coords[:,0], coords[:,1], c=values, cmap="viridis")
    plt.colorbar(sc, ax=ax, label="Value")
    ax.set_title("Spatial 2D plot")
    txt = f"Moran's I = {stats['I']:.3f}\np = {stats['p']:.3g}"
    ax.text(0.02, 0.98, txt, transform=ax.transAxes,
            va="top", ha="left",
            bbox=dict(boxstyle="round", fc="white", ec="black"))
    plt.tight_layout()
    plt.savefig(out)
    plt.close()

def spatial_scatter_3d(coords, values, stats, out):
    fig = plt.figure(figsize=(6,5))
    ax = fig.add_subplot(111, projection="3d")
    sc = ax.scatter(coords[:,0], coords[:,1], values,
                    c=values, cmap="viridis")
    fig.colorbar(sc, ax=ax, label="Value")
    ax.set_title("Spatial 3D plot")
    txt = f"Moran's I = {stats['I']:.3f}\np = {stats['p']:.3g}"
    ax.text2D(0.02, 0.98, txt, transform=ax.transAxes,
              bbox=dict(boxstyle="round", fc="white", ec="black"))
    plt.tight_layout()
    plt.savefig(out)
    plt.close()
