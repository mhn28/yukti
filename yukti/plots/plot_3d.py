import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_3d_with_annotations(
    data: dict,
    groups: list,
    annotations: dict,
    title: str,
    labels: tuple,
    out: str
):
    """
    data: {group: (x, y, z)}
    annotations: {p, stars, effect}
    """
    fig = plt.figure(figsize=(6,5))
    ax = fig.add_subplot(111, projection="3d")

    for g in groups:
        x, y, z = data[g]
        ax.scatter(x, y, z, label=g, s=30)

    ax.set_title(title)
    ax.set_xlabel(labels[0])
    ax.set_ylabel(labels[1])
    ax.set_zlabel(labels[2])
    ax.legend(frameon=True)

    # ---- annotation overlay ----
    ax.text2D(
        0.02, 0.95,
        f"{annotations['stars']}  p={annotations['p']:.3e}",
        transform=ax.transAxes,
        fontsize=11
    )
    ax.text2D(
        0.02, 0.90,
        annotations["effect"],
        transform=ax.transAxes,
        fontsize=10
    )

    plt.tight_layout()
    plt.savefig(out, dpi=300)
    plt.close()
