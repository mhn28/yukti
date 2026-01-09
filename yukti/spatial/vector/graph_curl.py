import numpy as np
from sklearn.neighbors import NearestNeighbors

def curl_cloud_2d(coords, velocity, k=12):
    """
    Graph-based curl (z-component) for 2D point clouds.
    Operator-faithful with dimensional correction.
    """
    n, d = coords.shape
    assert d == 2, "curl_cloud_2d only valid for 2D fields"

    nbrs = NearestNeighbors(n_neighbors=k+1).fit(coords)
    _, idx = nbrs.kneighbors(coords)

    curl = np.zeros(n)

    for i in range(n):
        acc = 0.0
        for j in idx[i][1:]:
            dx = coords[j] - coords[i]
            dv = velocity[j] - velocity[i]
            r2 = np.dot(dx, dx)
            if r2 > 0:
                acc += (dv[1]*dx[0] - dv[0]*dx[1]) / r2
        curl[i] = 2.0 * acc / k   # <-- dimension correction

    return {
        "test": "curl_cloud_2d",
        "mean": float(np.mean(curl)),
        "std": float(np.std(curl)),
        "values": curl
    }
