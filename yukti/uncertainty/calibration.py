
import numpy as np

def sensitivity_envelope(stat_func, data, param_grid):
    results = []
    for p in param_grid:
        results.append(stat_func(data, p))
    return {
        "min": float(np.min(results)),
        "max": float(np.max(results)),
        "mean": float(np.mean(results))
    }

def decision_threshold(p_value, alpha):
    return {
        "p_value": float(p_value),
        "alpha": float(alpha),
        "decision": bool(p_value <= alpha)
    }
