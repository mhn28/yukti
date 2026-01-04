
from yukti.benchmarks.registry import BenchmarkCase
from yukti.benchmarks.runner import run_benchmark
from yukti.benchmarks.report import write_report

def dummy_runner():
    return {"effect": 1.01}

case = BenchmarkCase(
    name="infrastructure_smoke_test",
    paper_doi="10.0000/dummy",
    dataset_source="synthetic",
    expected={"effect": 1.0},
    tolerance={"effect": 0.05},
    runner=dummy_runner
)

report = run_benchmark(case)
path = write_report(report)

assert report["pass"]["effect"] is True
print("✓ Phase 10A benchmarking infrastructure validated")
