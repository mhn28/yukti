
import numpy as np
from sklearn.neighbors import NearestNeighbors

def precompute_graph(coords, k=20, sigma=None):
    """
    Precompute kNN graph for reuse.
    Returns a dict with neighbors, distances, weights.
    """
    nbrs = NearestNeighbors(n_neighbors=k+1).fit(coords)
    dist, idx = nbrs.kneighbors(coords)

    # drop self-neighbor
    dist = dist[:, 1:]
    idx = idx[:, 1:]

    if sigma is None:
        sigma = np.mean(dist)

    weights = np.exp(-(dist**2) / (2 * sigma**2))

    return {
        "indices": idx,
        "distances": dist,
        "weights": weights,
        "sigma": sigma,
        "k": k
    }


def graph_laplacian(coords, values, k=20, graph=None):
    """
    Graph Laplacian using cached graph if provided.
    """
    if graph is None:
        graph = precompute_graph(coords, k=k)

    idx = graph["indices"]
    w   = graph["weights"]

    n = len(values)
    lap = np.zeros(n)

    for i in range(n):
        lap[i] = np.sum(w[i] * (values[idx[i]] - values[i]))

    return {
        "test": "graph_laplacian",
        "values": lap,
        "mean": float(np.mean(lap)),
        "std": float(np.std(lap))
    }
