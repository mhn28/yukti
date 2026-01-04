
import numpy as np
import pandas as pd
from yukti.causal.backdoor import backdoor_adjustment, CausalError

np.random.seed(42)
n = 200

# Confounder
Z = np.random.normal(0, 1, n)

# Treatment depends on confounder
T = 0.8 * Z + np.random.normal(0, 1, n)

# Outcome depends on both
Y = 2.0 * T + 1.5 * Z + np.random.normal(0, 1, n)

df = pd.DataFrame({"Y": Y, "T": T, "Z": Z})

# Correct adjustment
res = backdoor_adjustment(
    df,
    outcome="Y",
    treatment="T",
    adjusters=["Z"]
)

assert abs(res["treatment_effect"] - 2.0) < 0.3

# Block causal estimation without adjustment
try:
    backdoor_adjustment(df, "Y", "T", adjusters=[])
    raise AssertionError("Causal inference should have been blocked")
except CausalError:
    pass

print("✓ Phase 9 causal backdoor adjustment validated")
