import matplotlib.pyplot as plt

def plot_2d_with_annotations(x, y, annotations, title, out):
    fig, ax = plt.subplots(figsize=(5,4))
    ax.scatter(x, y, s=40)

    for i, ann in enumerate(annotations):
        txt = f"p={ann['p']} {ann['significance']}, {ann['label']}={ann['value']}"
        ax.text(
            0.05, 0.95 - i*0.08,
            txt,
            transform=ax.transAxes,
            fontsize=10,
            verticalalignment='top'
        )

    ax.set_title(title)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    plt.tight_layout()
    plt.savefig(out, dpi=300)
    plt.close()
