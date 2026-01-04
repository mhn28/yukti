
from yukti.viz.grammar import VizIntent, validate_viz_intent

assert validate_viz_intent(VizIntent.ABUNDANCE, "count")

try:
    validate_viz_intent(VizIntent.NETWORK, "numeric")
    raise AssertionError("Should have blocked invalid visualization")
except RuntimeError:
    pass

print("✓ Phase 18 visualization grammar validated")
