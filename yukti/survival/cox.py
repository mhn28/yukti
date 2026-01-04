import numpy as np
from scipy.optimize import minimize

def cox_ph(time, event, x):
    time = np.asarray(time)
    event = np.asarray(event)
    x = np.asarray(x)

    def neg_log_likelihood(beta):
        risk = np.exp(x * beta)
        ll = 0.0
        for i in range(len(time)):
            if event[i] == 1:
                ll += beta * x[i] - np.log(np.sum(risk[time >= time[i]]))
        return -ll

    res = minimize(neg_log_likelihood, x0=0.0)
    return {
        "beta": float(res.x),
        "loglik": float(-res.fun),
        "converged": res.success
    }
