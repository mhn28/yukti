import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def plot_streamlines(x, y, u, v, out, density=1.2, title="Vector field streamlines"):
    fig, ax = plt.subplots(figsize=(6,5))
    speed = np.sqrt(u**2 + v**2)
    strm = ax.streamplot(
        x, y, u, v,
        color=speed,
        cmap="viridis",
        density=density
    )
    ax.set_title(title)
    fig.colorbar(strm.lines, ax=ax, label="Speed")
    plt.tight_layout()
    plt.savefig(out)
    plt.close()
