import numpy as np

class SpatioTemporalData:
    def __init__(self, coords_t, values_t, times):
        # coords_t: list of (N,2) arrays per time
        # values_t: list of (N,) arrays per time
        if not (len(coords_t) == len(values_t) == len(times)):
            raise ValueError("coords_t, values_t, times must align")
        self.coords_t = coords_t
        self.values_t = values_t
        self.times = times

    def frame(self, i):
        return self.coords_t[i], self.values_t[i], self.times[i]
