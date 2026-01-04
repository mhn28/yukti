import numpy as np
from yukti.stats.effect_sizes import cohens_d, hedges_g, cliffs_delta, bootstrap_ci

np.random.seed(7)
a = np.random.normal(0, 1, 40)
b = np.random.normal(0.6, 1, 40)

d = cohens_d(a, b)
g = hedges_g(a, b)
cd = cliffs_delta(a, b)
ci_lo, ci_hi = bootstrap_ci(cohens_d, a, b)

print("Cohen's d:", d)
print("Hedges' g:", g)
print("Cliff's delta:", cd)
print("95% CI (bootstrap):", (ci_lo, ci_hi))

assert isinstance(d, float)
assert isinstance(g, float)
assert isinstance(cd, float)
assert ci_lo < d < ci_hi

print("✓ Effect sizes + CI validated")
