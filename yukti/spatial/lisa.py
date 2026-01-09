import numpy as np
from esda.moran import Moran_Local
from libpysal.weights import DistanceBand

def local_moran(coords, values, threshold=1.5, alpha=0.05):
    w = DistanceBand(coords, threshold=threshold, binary=True)
    lisa = Moran_Local(values, w)

    clusters = []
    for q, p in zip(lisa.q, lisa.p_sim):
        if p > alpha:
            clusters.append("NS")
        elif q == 1:
            clusters.append("HH")
        elif q == 2:
            clusters.append("LH")
        elif q == 3:
            clusters.append("LL")
        elif q == 4:
            clusters.append("HL")
        else:
            clusters.append("NS")

    return {
        "I_local": lisa.Is.tolist(),
        "p_values": lisa.p_sim.tolist(),
        "quadrant": lisa.q.tolist(),
        "clusters": clusters
    }
