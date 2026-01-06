import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def plot_quiver(u, v, out, stride=5, title="Vector field (quiver)"):
    h, w = u.shape
    x, y = np.meshgrid(range(w), range(h))
    fig, ax = plt.subplots(figsize=(6,6))
    ax.quiver(
        x[::stride, ::stride],
        y[::stride, ::stride],
        u[::stride, ::stride],
        v[::stride, ::stride],
        angles="xy",
        scale_units="xy",
        scale=1
    )
    ax.set_title(title)
    ax.set_aspect("equal")
    plt.tight_layout()
    plt.savefig(out)
    plt.close()

def plot_streamlines(u, v, out, density=1.2, title="Vector field (streamlines)"):
    h, w = u.shape
    x, y = np.meshgrid(range(w), range(h))
    fig, ax = plt.subplots(figsize=(6,6))
    ax.streamplot(x, y, u, v, density=density)
    ax.set_title(title)
    ax.set_aspect("equal")
    plt.tight_layout()
    plt.savefig(out)
    plt.close()
