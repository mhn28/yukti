import numpy as np

def cohens_d(a, b):
    a, b = np.asarray(a), np.asarray(b)
    na, nb = len(a), len(b)
    sa2, sb2 = np.var(a, ddof=1), np.var(b, ddof=1)
    sp = np.sqrt(((na - 1)*sa2 + (nb - 1)*sb2) / (na + nb - 2))
    d = (np.mean(a) - np.mean(b)) / sp
    return float(d)

def hedges_g(a, b):
    d = cohens_d(a, b)
    n = len(a) + len(b)
    correction = 1 - (3 / (4*n - 9))
    return float(d * correction)

def cliffs_delta(a, b):
    a, b = np.asarray(a), np.asarray(b)
    gt = sum(x > y for x in a for y in b)
    lt = sum(x < y for x in a for y in b)
    delta = (gt - lt) / (len(a) * len(b))
    return float(delta)

def bootstrap_ci(func, a, b, n_boot=2000, alpha=0.05, seed=42):
    rng = np.random.default_rng(seed)
    stats = []
    for _ in range(n_boot):
        ai = rng.choice(a, size=len(a), replace=True)
        bi = rng.choice(b, size=len(b), replace=True)
        stats.append(func(ai, bi))
    lo = np.percentile(stats, 100*(alpha/2))
    hi = np.percentile(stats, 100*(1 - alpha/2))
    return float(lo), float(hi)
