import importlib, json, os, datetime, sys

PHASES = {
    16: ["yukti.spatial.temporal"],
    17: ["yukti.spatial.vector.statistics"],
    18: ["yukti.spatial.vector.plots"],
    19: ["yukti.spatial.vector.statistics"],
    20: ["yukti.spatial.vector.graph_laplacian"],
    21: ["yukti.spatial.reaction_diffusion", "yukti.spatial.turing_graph"],
    22: ["yukti.spatial.vector.graph_laplacian_cached"],
}

timestamp = datetime.datetime.now(datetime.UTC).isoformat()
report = {
    "audit": "Phase 16–22",
    "timestamp_utc": timestamp,
    "results": {}
}

failures = []

for phase, modules in PHASES.items():
    report["results"][f"phase_{phase}"] = {}
    for m in modules:
        try:
            importlib.import_module(m)
            report["results"][f"phase_{phase}"][m] = "PASS"
        except Exception as e:
            report["results"][f"phase_{phase}"][m] = f"FAIL: {e}"
            failures.append((phase, m, str(e)))

os.makedirs("audit_reports", exist_ok=True)
path = f"audit_reports/audit_phase_16_22_{timestamp.replace(':','-')}.json"

with open(path, "w") as f:
    json.dump(report, f, indent=2)

if failures:
    print("\n✗ AUDIT FAILED (PHASES 16–22)")
    for f in failures:
        print(f)
    print("\nReport:", path)
    sys.exit(1)

print("\n✓ AUDIT PHASES 16–22 PASSED")
print("Report:", path)
