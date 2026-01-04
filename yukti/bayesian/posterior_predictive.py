import numpy as np

def posterior_predictive(mu, sigma, n=1000):
    return np.random.normal(mu, sigma, size=n).tolist()
