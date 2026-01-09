import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def plot_2d_with_annotations(
    data: dict,
    groups: list,
    annotations: dict,
    title: str,
    ylabel: str,
    out: str
):
    """
    data: {group_name: list of values}
    annotations: {
        "p": float,
        "stars": str,
        "effect": str
    }
    """
    fig, ax = plt.subplots(figsize=(6, 5))

    values = [data[g] for g in groups]
    ax.boxplot(values, labels=groups, patch_artist=True)

    ax.set_title(title)
    ax.set_ylabel(ylabel)

    # ---- statistical annotation ----
    ymax = max(max(v) for v in values)
    y = ymax * 1.1
    ax.plot([1, 2], [y, y], c="black")
    ax.text(
        1.5,
        y * 1.02,
        f"{annotations['stars']}  p={annotations['p']:.3e}",
        ha="center",
        va="bottom",
        fontsize=11
    )

    # ---- effect size ----
    ax.text(
        0.02,
        0.95,
        annotations["effect"],
        transform=ax.transAxes,
        ha="left",
        va="top",
        fontsize=10
    )

    plt.tight_layout()
    plt.savefig(out, dpi=300)
    plt.close()
