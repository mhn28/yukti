import numpy as np
from sklearn.neighbors import NearestNeighbors

def divergence_cloud(coords, velocity, k=12):
    """
    Dimension-correct, operator-faithful divergence on point clouds.
    """
    n, d = coords.shape
    nbrs = NearestNeighbors(n_neighbors=k+1).fit(coords)
    _, idx = nbrs.kneighbors(coords)

    div = np.zeros(n)

    for i in range(n):
        acc = 0.0
        for j in idx[i][1:]:
            dx = coords[j] - coords[i]
            dv = velocity[j] - velocity[i]
            r2 = np.dot(dx, dx)
            if r2 > 0:
                acc += np.dot(dv, dx) / r2
        div[i] = d * acc / k   # <-- critical dimensional correction

    return {
        "test": "divergence_cloud",
        "dimension": d,
        "mean": float(np.mean(div)),
        "std": float(np.std(div)),
        "values": div
    }
