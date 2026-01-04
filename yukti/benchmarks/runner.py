
import json
from datetime import datetime, timezone

def run_benchmark(case):
    observed = case.runner()
    report = {
        "name": case.name,
        "paper_doi": case.paper_doi,
        "dataset_source": case.dataset_source,
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "expected": case.expected,
        "observed": observed,
        "tolerance": case.tolerance,
        "pass": {
            k: abs(observed[k] - case.expected[k]) <= case.tolerance[k]
            for k in case.expected
        }
    }
    return report
