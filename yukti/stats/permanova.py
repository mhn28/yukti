
import numpy as np
from scipy.spatial.distance import pdist, squareform

def permanova(X, groups, permutations=999, metric="euclidean", seed=42):
    rng = np.random.default_rng(seed)
    X = np.asarray(X)
    groups = np.asarray(groups)

    D = squareform(pdist(X, metric=metric))
    n = len(groups)

    # Total sum of squares
    grand_mean = D.mean()
    SST = ((D - grand_mean) ** 2).sum() / n

    def ss_between(labels):
        ss = 0.0
        for g in np.unique(labels):
            idx = labels == g
            if idx.sum() > 1:
                d = D[np.ix_(idx, idx)]
                ss += ((d - d.mean()) ** 2).sum() / idx.sum()
        return ss

    SSB_obs = ss_between(groups)
    F_obs = SSB_obs / (SST - SSB_obs)

    count = 0
    for _ in range(permutations):
        perm = rng.permutation(groups)
        SSB_perm = ss_between(perm)
        F_perm = SSB_perm / (SST - SSB_perm)
        if F_perm >= F_obs:
            count += 1

    p_value = (count + 1) / (permutations + 1)

    return {
        "test": "PERMANOVA",
        "metric": metric,
        "permutations": permutations,
        "F": float(F_obs),
        "p": float(p_value)
    }
