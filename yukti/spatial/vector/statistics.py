import numpy as np

# -----------------------------
# Grid-faithful operators
# -----------------------------

def divergence_grid(u, v, dx=1.0, dy=1.0):
    du_dx = np.gradient(u, dx, axis=1)
    dv_dy = np.gradient(v, dy, axis=0)
    div = du_dx + dv_dy
    return div

def curl_grid(u, v, dx=1.0, dy=1.0):
    dv_dx = np.gradient(v, dx, axis=1)
    du_dy = np.gradient(u, dy, axis=0)
    return dv_dx - du_dy

# -----------------------------
# Public API (operator-faithful)
# -----------------------------

def divergence(coords, velocity):
    n = int(np.sqrt(coords.shape[0]))
    u = velocity[:,0].reshape(n, n)
    v = velocity[:,1].reshape(n, n)
    div = divergence_grid(u, v)
    return {
        "test": "divergence",
        "values": div,
        "mean": float(np.nanmean(div)),
        "std": float(np.nanstd(div)),
    }

def curl_2d(coords, velocity):
    n = int(np.sqrt(coords.shape[0]))
    u = velocity[:,0].reshape(n, n)
    v = velocity[:,1].reshape(n, n)
    cur = curl_grid(u, v)
    return {
        "test": "curl_2d",
        "values": cur,
        "mean": float(np.nanmean(cur)),
        "std": float(np.nanstd(cur)),
    }

def anisotropy(velocity):
    cov = np.cov(velocity.T)
    eigvals = np.linalg.eigvalsh(cov)
    idx = float(eigvals.max() / eigvals.min()) if eigvals.min() > 0 else float("inf")
    return {
        "test": "anisotropy",
        "eigenvalues": eigvals.tolist(),
        "index": idx,
    }
