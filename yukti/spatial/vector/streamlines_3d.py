import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D  # noqa

def plot_streamlines_3d(x, y, z, u, v, w, out, stride=5, title="3D Vector Field Streamlines"):
    fig = plt.figure(figsize=(7,6))
    ax = fig.add_subplot(111, projection="3d")

    xs = x[::stride, ::stride, ::stride].flatten()
    ys = y[::stride, ::stride, ::stride].flatten()
    zs = z[::stride, ::stride, ::stride].flatten()
    us = u[::stride, ::stride, ::stride].flatten()
    vs = v[::stride, ::stride, ::stride].flatten()
    ws = w[::stride, ::stride, ::stride].flatten()

    ax.quiver(xs, ys, zs, us, vs, ws, length=0.15, normalize=True)
    ax.set_title(title)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    plt.tight_layout()
    plt.savefig(out)
    plt.close()
