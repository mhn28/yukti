import numpy as np

def kaplan_meier(time, event):
    order = np.argsort(time)
    time = time[order]
    event = event[order]

    n = len(time)
    at_risk = n
    survival = []
    current = 1.0

    for t, e in zip(time, event):
        if e == 1:
            current *= (at_risk - 1) / at_risk
        survival.append((t, current))
        at_risk -= 1

    return survival
