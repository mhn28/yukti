from yukti.figures.spec import load_spec
from yukti.figures.render import render_figure
import os

spec = load_spec("yukti/tests/example_figure.yaml")
render_figure(spec)

assert os.path.exists(spec["output"])
print("✓ Phase F: Figure DSL → rendering validated")
