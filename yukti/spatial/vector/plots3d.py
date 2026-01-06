import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def plot_quiver_3d(x, y, z, u, v, w, out, stride=3, title="3D Vector field"):
    fig = plt.figure(figsize=(7,6))
    ax = fig.add_subplot(111, projection="3d")
    ax.quiver(
        x[::stride, ::stride, ::stride],
        y[::stride, ::stride, ::stride],
        z[::stride, ::stride, ::stride],
        u[::stride, ::stride, ::stride],
        v[::stride, ::stride, ::stride],
        w[::stride, ::stride, ::stride],
        length=0.1,
        normalize=True
    )
    ax.set_title(title)
    plt.tight_layout()
    plt.savefig(out)
    plt.close()
