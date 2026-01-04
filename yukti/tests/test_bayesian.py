import pymc as pm
import numpy as np

np.random.seed(42)
g1 = np.random.normal(0, 1, 30)
g2 = np.random.normal(0.8, 1, 30)

with pm.Model():
    mu1 = pm.Normal("mu1", 0, 1)
    mu2 = pm.Normal("mu2", 0, 1)
    sigma = pm.HalfNormal("sigma", 1)

    pm.Normal("y1", mu1, sigma, observed=g1)
    pm.Normal("y2", mu2, sigma, observed=g2)

    delta = pm.Deterministic("delta", mu2 - mu1)
    trace = pm.sample(1000, tune=1000, chains=4, progressbar=False)

assert abs(trace.posterior["delta"].mean()) > 0.3
print("✓ Phase 5 Bayesian inference validated")
