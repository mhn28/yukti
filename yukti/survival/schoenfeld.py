import numpy as np
from scipy.stats import spearmanr

def schoenfeld_test(time, residuals):
    rho, p = spearmanr(time, residuals)
    return {
        "rho": float(rho),
        "p": float(p),
        "ph_assumption_ok": p > 0.05
    }
