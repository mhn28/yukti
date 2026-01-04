import numpy as np
from scipy.stats import chi2

def logrank_test(time, event, group):
    groups = np.unique(group)
    if len(groups) != 2:
        raise ValueError("Log-rank test requires exactly two groups.")

    tvals = np.unique(time)
    O1 = E1 = V1 = 0.0

    for t in tvals:
        ix = time >= t
        d = (time == t) & (event == 1)

        n1 = np.sum(ix & (group == groups[0]))
        n2 = np.sum(ix & (group == groups[1]))
        d1 = np.sum(d & (group == groups[0]))
        d2 = np.sum(d & (group == groups[1]))

        if n1 + n2 > 0:
            e1 = (n1 / (n1 + n2)) * (d1 + d2)
            v1 = (n1 * n2 * (d1 + d2) * (n1 + n2 - d1 - d2)) / (
                (n1 + n2)**2 * (n1 + n2 - 1)
            )
            O1 += d1
            E1 += e1
            V1 += v1

    z = (O1 - E1)**2 / V1 if V1 > 0 else 0
    p = 1 - chi2.cdf(z, df=1)

    return {"stat": float(z), "p": float(p)}
