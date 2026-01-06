import numpy as np

def divergence(coords, velocity):
    """
    Numerical divergence for 2D or 3D vector fields.
    coords: (n,d), velocity: (n,d)
    """
    d = coords.shape[1]
    div = np.zeros(coords.shape[0])
    for i in range(d):
        div += np.gradient(velocity[:, i], coords[:, i])
    return {
        "test": "divergence",
        "values": div.tolist(),
        "mean": float(np.mean(div)),
        "std": float(np.std(div))
    }

def curl_2d(coords, velocity):
    """
    Scalar curl for 2D fields: dVy/dx − dVx/dy
    """
    vx, vy = velocity[:,0], velocity[:,1]
    x, y = coords[:,0], coords[:,1]
    curl = np.gradient(vy, x) - np.gradient(vx, y)
    return {
        "test": "curl_2d",
        "values": curl.tolist(),
        "mean": float(np.mean(curl)),
        "std": float(np.std(curl))
    }

def anisotropy(velocity):
    """
    Anisotropy index based on eigenvalue ratio of velocity covariance
    """
    cov = np.cov(velocity.T)
    eigvals = np.linalg.eigvalsh(cov)
    if eigvals.min() <= 0:
        idx = float("inf")
    else:
        idx = float(eigvals.max() / eigvals.min())
    return {
        "test": "anisotropy",
        "eigenvalues": eigvals.tolist(),
        "index": idx
    }
