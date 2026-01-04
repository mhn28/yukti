from yukti.data.schema import DataSchema
from yukti.data.guards import enforce_schema

# Ratio data — allowed
s1 = DataSchema(
    name="Biomarker concentration",
    measurement_scale="ratio"
)
assert enforce_schema(s1)

# Nominal data — blocked
try:
    s2 = DataSchema(
        name="Species",
        measurement_scale="nominal"
    )
    enforce_schema(s2)
    raise AssertionError("Nominal data should be blocked")
except RuntimeError:
    pass

# Temporal data — blocked unless opt-in
try:
    s3 = DataSchema(
        name="Time series",
        measurement_scale="temporal",
        temporal=True
    )
    enforce_schema(s3)
    raise AssertionError("Temporal data should require opt-in")
except RuntimeError:
    pass

print("✓ Phase 13 data schema validated")
