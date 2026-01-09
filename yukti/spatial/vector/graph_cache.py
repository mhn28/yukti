
import numpy as np
from sklearn.neighbors import NearestNeighbors

_GRAPH_CACHE = {}

def get_knn_graph(coords, k):
    key = (coords.shape[0], k, coords.tobytes()[:64])
    if key in _GRAPH_CACHE:
        return _GRAPH_CACHE[key]
    nn = NearestNeighbors(n_neighbors=k+1).fit(coords)
    dist, idx = nn.kneighbors(coords)
    _GRAPH_CACHE[key] = (dist[:,1:], idx[:,1:])
    return _GRAPH_CACHE[key]
