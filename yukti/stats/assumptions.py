from scipy import stats
import numpy as np

def normality_test(data, alpha=0.05):
    stat, p = stats.shapiro(data)
    return {
        "test": "Shapiro-Wilk",
        "p": float(p),
        "normal": bool(p >= alpha)
    }

def variance_homogeneity_test(*groups, alpha=0.05):
    stat, p = stats.levene(*groups, center="median")
    return {
        "test": "Levene (median)",
        "p": float(p),
        "homogeneous": bool(p >= alpha)
    }
