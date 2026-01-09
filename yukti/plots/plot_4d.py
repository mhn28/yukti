import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def plot_4d_trajectory(coords, time, annotations, out):
    fig, ax = plt.subplots(figsize=(5,4))
    sc = ax.scatter(
        coords[:,0], coords[:,1],
        c=time, cmap="viridis"
    )
    plt.colorbar(sc, ax=ax, label="Time")

    for i,a in enumerate(annotations):
        ax.text(
            0.02, 0.95 - i*0.07,
            f"p={a['p']:.3g} ({a['significance']})",
            transform=ax.transAxes
        )

    ax.set_title("4D trajectory with annotations")
    plt.tight_layout()
    plt.savefig(out)
    plt.close()
