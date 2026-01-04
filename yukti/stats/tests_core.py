import numpy as np
from scipy import stats

def t_test(a, b):
    stat, p = stats.ttest_ind(a, b, equal_var=False)
    return {"test": "Welch t-test", "stat": float(stat), "p": float(p)}

def mann_whitney(a, b):
    stat, p = stats.mannwhitneyu(a, b, alternative="two-sided")
    return {"test": "Mann–Whitney U", "stat": float(stat), "p": float(p)}
