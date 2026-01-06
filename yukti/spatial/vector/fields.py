import numpy as np

def velocity_field(coords_t, times):
    if len(coords_t) < 2:
        raise ValueError("At least two timepoints required")
    velocities = {}
    for i in range(len(times) - 1):
        dt = times[i+1] - times[i]
        if dt <= 0:
            raise ValueError("Time must be strictly increasing")
        velocities[(times[i], times[i+1])] = (coords_t[i+1] - coords_t[i]) / dt
    return velocities

def divergence_2d(coords, velocity):
    if coords.shape[1] != 2:
        raise ValueError("2D coordinates required")
    return np.sum(velocity, axis=1)
