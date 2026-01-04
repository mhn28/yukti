
from yukti.uncertainty.calibration import sensitivity_envelope, decision_threshold
import numpy as np

def dummy_stat(data, scale):
    return np.mean(data) * scale

data = np.array([1,2,3,4,5])
env = sensitivity_envelope(dummy_stat, data, [0.5,1,2])
assert env["min"] <= env["mean"] <= env["max"]

d = decision_threshold(0.04, 0.05)
assert d["decision"] is True

print("✓ Phase 29 uncertainty calibration & sensitivity validated")
