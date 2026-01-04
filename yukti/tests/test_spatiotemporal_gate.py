from yukti.data.spatiotemporal_decl import SpatiotemporalDeclaration
from yukti.data.spatiotemporal_gate import enforce_spatiotemporal_gate, SpatiotemporalGateError
from yukti.data.reasoning_modes import ReasoningMode

# 1. No declaration + independent mode → OK
assert enforce_spatiotemporal_gate(
    SpatiotemporalDeclaration(),
    ReasoningMode.INDEPENDENT
)

# 2. No declaration + spatiotemporal mode → BLOCK
try:
    enforce_spatiotemporal_gate(
        SpatiotemporalDeclaration(),
        ReasoningMode.SPATIOTEMPORAL
    )
    raise AssertionError
except SpatiotemporalGateError:
    pass

# 3. Declaration + no mode → BLOCK
try:
    enforce_spatiotemporal_gate(
        SpatiotemporalDeclaration(temporal_axis="time"),
        None
    )
    raise AssertionError
except SpatiotemporalGateError:
    pass

# 4. Declaration + incompatible mode → BLOCK
try:
    enforce_spatiotemporal_gate(
        SpatiotemporalDeclaration(temporal_axis="time"),
        ReasoningMode.INDEPENDENT
    )
    raise AssertionError
except SpatiotemporalGateError:
    pass

# 5. Declaration + longitudinal → OK
assert enforce_spatiotemporal_gate(
    SpatiotemporalDeclaration(temporal_axis="visit"),
    ReasoningMode.LONGITUDINAL
)

# 6. Declaration + conservative → OK
assert enforce_spatiotemporal_gate(
    SpatiotemporalDeclaration(spatial_axes=["x","y"]),
    ReasoningMode.CONSERVATIVE
)

print("✓ Phase 14 STRICT spatiotemporal gate validated")
