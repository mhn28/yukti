import numpy as np

class SpatioTemporalData:
    """
    coords: (n, 2)
    time:   (n,)
    values: (n,)
    """
    def __init__(self, coords: np.ndarray, time: np.ndarray, values: np.ndarray):
        if not (len(coords) == len(time) == len(values)):
            raise ValueError("coords, time, values must have equal length")
        self.coords = coords
        self.time = time
        self.values = values

    def unique_times(self):
        return sorted(set(self.time))
