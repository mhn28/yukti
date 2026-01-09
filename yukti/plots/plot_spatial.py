import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def plot_spatial_with_annotations(
    coords,
    values,
    annotations,
    title,
    cmap="viridis",
    out="spatial_plot.png"
):
    """
    coords: (n,2) array
    values: (n,) scalar field
    annotations: {p, stars, effect}
    """
    fig, ax = plt.subplots(figsize=(6,5))
    sc = ax.scatter(
        coords[:,0],
        coords[:,1],
        c=values,
        cmap=cmap,
        s=40,
        edgecolor="k"
    )

    ax.set_title(title)
    plt.colorbar(sc, ax=ax, label="Value")

    # ---- annotation overlay ----
    ax.text(
        0.01, 0.98,
        f"{annotations['stars']}  p={annotations['p']:.3e}",
        transform=ax.transAxes,
        fontsize=11,
        verticalalignment="top"
    )
    ax.text(
        0.01, 0.92,
        annotations["effect"],
        transform=ax.transAxes,
        fontsize=10,
        verticalalignment="top"
    )

    plt.tight_layout()
    plt.savefig(out, dpi=300)
    plt.close()
