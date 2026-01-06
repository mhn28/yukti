"""
Bayesian inference primitives (explicit, opt-in).
No automatic decision thresholds.
"""

import pymc as pm
import numpy as np

def bayesian_two_group(g1, g2, draws=1000, tune=1000, chains=4):
    g1 = np.asarray(g1)
    g2 = np.asarray(g2)

    with pm.Model() as model:
        mu1 = pm.Normal("mu1", 0, 5)
        mu2 = pm.Normal("mu2", 0, 5)
        sigma = pm.HalfNormal("sigma", 5)

        pm.Normal("y1", mu1, sigma, observed=g1)
        pm.Normal("y2", mu2, sigma, observed=g2)

        delta = pm.Deterministic("delta", mu2 - mu1)

        trace = pm.sample(
            draws=draws,
            tune=tune,
            chains=chains,
            progressbar=False,
            target_accept=0.9
        )

    return {
        "model": "bayesian_two_group",
        "delta_mean": float(trace.posterior["delta"].mean()),
        "delta_hdi": tuple(
            map(float, pm.hdi(trace.posterior["delta"]).to_array())
        )
    }
