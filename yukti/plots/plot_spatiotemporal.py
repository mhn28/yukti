import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def plot_spatiotemporal_animation(
    coords,
    values_over_time,
    times,
    annotations,
    title,
    out_mp4="spatiotemporal.mp4",
    out_gif=None,
    cmap="viridis"
):
    """
    coords: (n,2)
    values_over_time: (t,n)
    times: (t,)
    annotations: {p, stars, effect}
    """

    fig, ax = plt.subplots(figsize=(6,5))
    sc = ax.scatter(
        coords[:,0],
        coords[:,1],
        c=values_over_time[0],
        cmap=cmap,
        s=40,
        edgecolor="k"
    )

    ax.set_title(title)
    cb = plt.colorbar(sc, ax=ax)
    cb.set_label("Value")

    ann_text = ax.text(
        0.01, 0.98,
        f"{annotations['stars']}  p={annotations['p']:.3e}\n{annotations['effect']}",
        transform=ax.transAxes,
        fontsize=11,
        verticalalignment="top"
    )

    time_text = ax.text(
        0.99, 0.01,
        f"t={times[0]}",
        transform=ax.transAxes,
        ha="right",
        fontsize=10
    )

    def update(frame):
        sc.set_array(values_over_time[frame])
        time_text.set_text(f"t={times[frame]}")
        return sc, time_text

    anim = FuncAnimation(
        fig,
        update,
        frames=len(times),
        interval=400,
        blit=False
    )

    anim.save(out_mp4, dpi=300)

    if out_gif is not None:
        anim.save(out_gif, writer="pillow", dpi=200)

    plt.close()
