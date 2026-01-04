import numpy as np
from libpysal.weights import DistanceBand
from esda.moran import Moran

class SpatialData:
    def __init__(self, coords: np.ndarray, values: np.ndarray):
        if coords.shape[0] != values.shape[0]:
            raise ValueError("Coordinates and values must align")
        self.coords = coords
        self.values = values

    def weights(self, threshold=1.5):
        return DistanceBand(self.coords, threshold=threshold, binary=True)

def morans_i(spatial: SpatialData, threshold=1.5):
    w = spatial.weights(threshold)
    mi = Moran(spatial.values, w)
    return {
        "test": "Moran_I",
        "I": float(mi.I),
        "p": float(mi.p_sim),
        "z": float(mi.z_sim)
    }
