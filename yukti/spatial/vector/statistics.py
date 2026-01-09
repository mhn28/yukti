import numpy as np

def divergence_grid(u, v, dx=1.0, dy=1.0):
    """
    Divergence on a 2D structured grid.
    u, v : 2D arrays
    """
    du_dx = np.gradient(u, dx, axis=1)
    dv_dy = np.gradient(v, dy, axis=0)
    div = du_dx + dv_dy
    interior = div[2:-2, 2:-2]
    return {
        "test": "divergence_2d_grid",
        "mean": float(np.mean(interior)),
        "std": float(np.std(interior)),
        "values": div
    }

def curl_grid(u, v, dx=1.0, dy=1.0):
    """
    Scalar curl on a 2D structured grid.
    """
    dv_dx = np.gradient(v, dx, axis=1)
    du_dy = np.gradient(u, dy, axis=0)
    curl = dv_dx - du_dy
    interior = curl[2:-2, 2:-2]
    return {
        "test": "curl_2d_grid",
        "mean": float(np.mean(interior)),
        "std": float(np.std(interior)),
        "values": curl
    }
