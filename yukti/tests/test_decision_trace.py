
from yukti.trace.decision_trace import DecisionTrace

dt = DecisionTrace()
dt.record("declare_data", "User declared RNA-seq counts", domain="transcriptomics")
dt.record("block_test", "Normalization not declared")

trace = dt.export()
assert len(trace["decision_trace"]) == 2
assert trace["decision_trace"][0]["timestamp_utc"].endswith("Z") or "T" in trace["decision_trace"][0]["timestamp_utc"]

print("✓ Phase 19 decision trace validated")
