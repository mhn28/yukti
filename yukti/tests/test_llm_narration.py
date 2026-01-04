
from yukti.llm.narration import ScientificNarrator

trace = {
    "decision_trace": [
        {"action": "declare_data", "rationale": "RNA-seq counts declared"},
        {"action": "apply_correction", "rationale": "Benjamini-Hochberg selected"}
    ]
}

stats = {
    "stat": 2.31,
    "p": 0.021,
    "correction": "BH"
}

n = ScientificNarrator()
report = n.full_report(trace, stats)

assert "informational only" in report["disclaimer"]
assert "RNA-seq counts declared" in report["methods"]

print("✓ Phase 20 LLM narration validated (non-authoritative)")
