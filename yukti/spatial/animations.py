import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation, FFMpegWriter

def animate_spatiotemporal(st, out_mp4, stat_text_fn=None, fps=5):
    fig, ax = plt.subplots(figsize=(6,5))
    sc = ax.scatter([], [], c=[], cmap="viridis", vmin=None, vmax=None)
    cb = plt.colorbar(sc, ax=ax, label="Value")

    def init():
        ax.set_title("Spatio-temporal trajectory")
        return (sc,)

    def update(i):
        coords, values, t = st.frame(i)
        sc.set_offsets(coords)
        sc.set_array(values)
        ax.set_title(f"Time = {t}")
        if stat_text_fn:
            txt = stat_text_fn(i)
            ax.text(0.02, 0.98, txt, transform=ax.transAxes,
                    va="top", ha="left",
                    bbox=dict(boxstyle="round", fc="white", ec="black"))
        return (sc,)

    anim = FuncAnimation(fig, update, init_func=init,
                         frames=len(st.times), blit=False)
    writer = FFMpegWriter(fps=fps)
    anim.save(out_mp4, writer=writer)
    plt.close()
