import numpy as np
from yukti.plots.plot_2d import plot_2d_with_annotations

np.random.seed(42)
data = {
    "Control": np.random.normal(0, 1, 30),
    "Treatment": np.random.normal(0.8, 1, 30),
}

annotations = {
    "p": 0.004,
    "stars": "**",
    "effect": "Cohen d = 0.82"
}

plot_2d_with_annotations(
    data=data,
    groups=["Control", "Treatment"],
    annotations=annotations,
    title="Treatment effect on response",
    ylabel="Response value",
    out="phase_i_boxplot.png"
)

import os
assert os.path.exists("phase_i_boxplot.png")
print("✓ Phase I.1 annotation-aware 2D plotting validated")
