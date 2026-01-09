import numpy as np
from sklearn.neighbors import NearestNeighbors

def graph_curl_4d(coords, velocity, time, k=12):
    """
    Spatio-temporal graph curl (4D).
    coords: (n,2) spatial points
    velocity: (n,2) velocity vectors
    time: (n,) time index
    """
    coords = np.asarray(coords)
    velocity = np.asarray(velocity)
    time = np.asarray(time)

    nbrs = NearestNeighbors(n_neighbors=k+1).fit(coords)
    _, idx = nbrs.kneighbors(coords)

    curl_vals = np.zeros(len(coords))

    for i in range(len(coords)):
        acc = 0.0
        for j in idx[i][1:]:
            # spatial difference
            dx = coords[j] - coords[i]
            dv = velocity[j] - velocity[i]

            # temporal modulation
            dt = time[j] - time[i]
            if np.linalg.norm(dx) > 0:
                acc += (dx[0]*dv[1] - dx[1]*dv[0]) / (np.linalg.norm(dx)**2 + abs(dt) + 1e-6)
        curl_vals[i] = acc / k

    return {
        "test": "graph_curl_4d",
        "mean": float(np.mean(curl_vals)),
        "std": float(np.std(curl_vals)),
        "values": curl_vals
    }
