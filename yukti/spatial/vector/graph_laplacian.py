import numpy as np
from sklearn.neighbors import NearestNeighbors

def graph_laplacian(coords, values, k=20, sigma=None):
    """
    Symmetric graph Laplacian using heat-kernel weights.
    Operator-faithful for point clouds.
    """
    coords = np.asarray(coords)
    values = np.asarray(values)
    n, d = coords.shape

    nbrs = NearestNeighbors(n_neighbors=k+1).fit(coords)
    dists, idx = nbrs.kneighbors(coords)

    if sigma is None:
        sigma = np.mean(dists[:,1:])

    lap = np.zeros(n)

    for i in range(n):
        wsum = 0.0
        acc = 0.0
        for j, dist in zip(idx[i][1:], dists[i][1:]):
            w = np.exp(-(dist**2)/(2*sigma**2))
            acc += w * (values[j] - values[i])
            wsum += w
        if wsum > 0:
            lap[i] = acc / wsum

    return {
        "test": "graph_laplacian",
        "mean": float(np.mean(lap)),
        "std": float(np.std(lap)),
        "values": lap
    }

def diffuse(coords, values, dt=0.01, steps=25, k=20):
    f = values.copy()
    for _ in range(steps):
        lap = graph_laplacian(coords, f, k=k)["values"]
        f = f + dt * lap
    return f
