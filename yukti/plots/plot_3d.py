import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa

def plot_3d_with_annotations(x, y, z, annotations, title, out):
    fig = plt.figure(figsize=(6,5))
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(x, y, z, s=30)

    for i, ann in enumerate(annotations):
        ax.text2D(
            0.02, 0.95 - i*0.08,
            f"p={ann['p']} {ann['significance']}, {ann['label']}={ann['value']}",
            transform=ax.transAxes,
            fontsize=9
        )

    ax.set_title(title)
    plt.tight_layout()
    plt.savefig(out, dpi=300)
    plt.close()
