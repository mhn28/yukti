
import numpy as np
from yukti.stats.permanova import permanova

np.random.seed(42)

# Two well-separated clusters in multivariate space
g1 = np.random.normal(0, 1, (30, 5))
g2 = np.random.normal(3, 1, (30, 5))

X = np.vstack([g1, g2])
groups = np.array([0]*30 + [1]*30)

res = permanova(X, groups, permutations=499)

assert res["p"] < 0.05
print("✓ Phase 7 PERMANOVA validated (distance-based inference)")
