import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

COLORS = {
    "HH": "red",
    "LL": "blue",
    "HL": "orange",
    "LH": "lightblue",
    "NS": "grey"
}

def plot_lisa(coords, clusters, out):
    fig, ax = plt.subplots(figsize=(6,5))
    for c in set(clusters):
        idx = [i for i,v in enumerate(clusters) if v == c]
        ax.scatter(
            coords[idx,0],
            coords[idx,1],
            label=c,
            c=COLORS.get(c,"black"),
            edgecolor="k",
            s=50
        )
    ax.set_title("Local Moran (LISA) Hotspot Map")
    ax.legend(frameon=True)
    plt.tight_layout()
    plt.savefig(out)
    plt.close()
