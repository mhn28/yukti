
import numpy as np, pandas as pd
from yukti.stats.mixed_effects import mixed_intercept

np.random.seed(42)

# Simulated clustered data
groups = np.repeat(np.arange(10), 10)
x = np.random.normal(0, 1, 100)
group_effect = np.repeat(np.random.normal(0, 1, 10), 10)
y = 1.5 * x + group_effect + np.random.normal(0, 0.5, 100)

df = pd.DataFrame({
    "y": y,
    "x": x,
    "group": groups
})

res = mixed_intercept(df, "y", "x", "group")

assert abs(res["fixed_effects"]["x"] - 1.5) < 0.3
assert res["random_effects_var"] > 0

print("✓ Phase 6 mixed-effects (random intercept) validated")
