import numpy as np

def bayes_factor_normal(x, mu0=0.0, sigma0=1.0, sigma=1.0):
    n = len(x)
    xbar = np.mean(x)

    num = np.exp(-(n*(xbar-mu0)**2)/(2*(sigma**2 + sigma0**2)))
    den = np.sqrt(1 + (n*sigma0**2)/(sigma**2))

    return {
        "bayes_factor_10": float(num / den)
    }
