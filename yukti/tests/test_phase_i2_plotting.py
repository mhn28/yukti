import numpy as np
from yukti.plots.plot_3d import plot_3d_with_annotations
import os

np.random.seed(42)

data = {
    "Control": (
        np.random.normal(0,1,40),
        np.random.normal(0,1,40),
        np.random.normal(0,1,40)
    ),
    "Treatment": (
        np.random.normal(1,1,40),
        np.random.normal(1,1,40),
        np.random.normal(1,1,40)
    )
}

annotations = {
    "p": 0.002,
    "stars": "**",
    "effect": "Cohen d = 0.91"
}

plot_3d_with_annotations(
    data=data,
    groups=["Control","Treatment"],
    annotations=annotations,
    title="3D group separation",
    labels=("PC1","PC2","PC3"),
    out="phase_i2_3d_plot.png"
)

assert os.path.exists("phase_i2_3d_plot.png")
print("✓ Phase I.2 annotation-aware 3D plotting validated")
