
import numpy as np
import pandas as pd
from yukti.stats.mixed_effects import linear_mixed_model

np.random.seed(0)

df = pd.DataFrame({
    "subject": np.repeat(range(10), 5),
    "time": list(range(5)) * 10,
    "treatment": np.random.choice([0,1], 50),
    "y": np.random.normal(0, 1, 50)
})

res = linear_mixed_model(
    data=df,
    formula="y ~ time + treatment",
    group="subject"
)

assert res["model"] == "LMM"
assert "time" in res["params"]
assert isinstance(res["aic"], float)

print("✓ Phase 3 mixed-effects model validated")
