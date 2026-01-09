
import numpy as np
from yukti.spatial.vector.graph_cache import get_knn_graph

def graph_laplacian_cached(coords, values, k=20, sigma=1.0):
    dist, idx = get_knn_graph(coords, k)
    lap = np.zeros(len(values))
    for i in range(len(values)):
        w = np.exp(-(dist[i]**2)/(2*sigma**2))
        lap[i] = (w * (values[idx[i]] - values[i])).sum()
    return {
        "test": "graph_laplacian_cached",
        "values": lap,
        "mean": float(np.mean(lap)),
        "std": float(np.std(lap))
    }
