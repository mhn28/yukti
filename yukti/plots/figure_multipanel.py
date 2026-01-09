import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def compose_figure(
    panels,
    title,
    out_path,
    figsize=(8,6),
    dpi=300
):
    """
    panels: list of dicts with keys:
        - plot_fn(ax)
        - label (e.g., 'A', 'B', 'C', 'D')
        - subtitle
    """

    n = len(panels)
    if n not in {2,3,4}:
        raise ValueError("Only 2–4 panels supported")

    rows = 2 if n > 2 else 1
    cols = 2 if n != 3 else 3

    fig, axes = plt.subplots(rows, cols, figsize=figsize)
    axes = axes.flatten() if n > 1 else [axes]

    for ax, panel in zip(axes, panels):
        panel["plot_fn"](ax)
        ax.set_title(panel["subtitle"], fontsize=10)
        ax.text(
            -0.15, 1.08,
            panel["label"],
            transform=ax.transAxes,
            fontsize=14,
            fontweight="bold"
        )

    # Remove unused axes
    for ax in axes[len(panels):]:
        ax.axis("off")

    fig.suptitle(title, fontsize=14)
    plt.tight_layout(rect=[0,0,1,0.96])
    plt.savefig(out_path, dpi=dpi)
    plt.close()
