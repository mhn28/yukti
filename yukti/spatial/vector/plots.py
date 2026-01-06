import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

def quiver_2d(coords, velocity, out):
    fig, ax = plt.subplots(figsize=(6,5))
    ax.quiver(coords[:,0], coords[:,1], velocity[:,0], velocity[:,1],
              angles='xy', scale_units='xy', scale=1, width=0.003)
    ax.set_title("2D Velocity Field (Quiver)")
    ax.set_aspect('equal', adjustable='box')
    plt.tight_layout()
    plt.savefig(out)
    plt.close()

def streamlines_2d(coords, velocity, out, grid_n=30):
    # Interpolate to grid for streamlines
    x, y = coords[:,0], coords[:,1]
    u, v = velocity[:,0], velocity[:,1]
    xi = np.linspace(x.min(), x.max(), grid_n)
    yi = np.linspace(y.min(), y.max(), grid_n)
    Xi, Yi = np.meshgrid(xi, yi)
    Ui = np.interp(Xi, x, u)
    Vi = np.interp(Yi, y, v)

    fig, ax = plt.subplots(figsize=(6,5))
    ax.streamplot(Xi, Yi, Ui, Vi, density=1.2)
    ax.set_title("2D Velocity Field (Streamlines)")
    ax.set_aspect('equal', adjustable='box')
    plt.tight_layout()
    plt.savefig(out)
    plt.close()

def quiver_3d(coords, velocity, out):
    fig = plt.figure(figsize=(6,5))
    ax = fig.add_subplot(111, projection='3d')
    ax.quiver(coords[:,0], coords[:,1], coords[:,2],
              velocity[:,0], velocity[:,1], velocity[:,2],
              length=1.0, normalize=False)
    ax.set_title("3D Velocity Field (Quiver)")
    plt.tight_layout()
    plt.savefig(out)
    plt.close()
