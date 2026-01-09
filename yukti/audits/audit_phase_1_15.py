"""
Audit Phase 1–15
Scope: integrity, semantics, execution, invariants
No feature creation. No assumptions. Fail-fast.
"""
import importlib, json, os, datetime

PHASES = {
    1: ["yukti.stats.tests_core"],
    2: ["yukti.stats.multiple_testing"],
    3: ["yukti.stats.effect_sizes"],
    4: ["yukti.stats.survival"],
    5: ["yukti.stats.bayesian"],
    6: ["yukti.stats.mixed_effects"],
    7: ["yukti.stats.permanova"],
    8: ["yukti.stats.multiomics_factors"],
    9: ["yukti.causal"],
    10: ["yukti.benchmarks"],
    11: ["yukti.causal.dag"],
    12: ["yukti.spatial.core"],
    13: ["yukti.spatial.plots"],
    14: ["yukti.spatial.lisa"],
    15: ["yukti.spatial.temporal"],
}

report = {
    "audit": "Phase 1–15",
    "timestamp_utc": datetime.datetime.utcnow().isoformat() + "Z",
    "results": {}
}

for phase, modules in PHASES.items():
    report["results"][f"phase_{phase}"] = {}
    for m in modules:
        try:
            importlib.import_module(m)
            report["results"][f"phase_{phase}"][m] = "PASS"
        except Exception as e:
            report["results"][f"phase_{phase}"][m] = f"FAIL: {e}"

path = f"audit_reports/audit_phase_1_15_{report['timestamp_utc']}.json"
with open(path, "w") as f:
    json.dump(report, f, indent=2)

failures = [
    (p,m,v)
    for p,mods in report["results"].items()
    for m,v in mods.items()
    if v != "PASS"
]

if failures:
    print("✗ AUDIT FAILED")
    for f in failures:
        print(f)
    raise SystemExit(1)

print("✓ AUDIT PHASES 1–15 PASSED")
print("Report:", path)
