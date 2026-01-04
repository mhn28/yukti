import numpy as np

def bayesian_mean(data, prior_mu=0.0, prior_sigma=10.0):
    data = np.asarray(data)
    n = len(data)

    post_var = 1 / (n + 1/(prior_sigma**2))
    post_mu = post_var * (np.sum(data) + prior_mu/(prior_sigma**2))

    return {
        "posterior_mean": float(post_mu),
        "posterior_sd": float(np.sqrt(post_var))
    }
