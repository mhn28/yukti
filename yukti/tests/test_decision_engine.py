from yukti.stats.decision_engine import decide_tests

res = decide_tests(
    measurement_scale="ratio",
    independent=True,
    normal=True,
    homogeneous_variance=True,
    n_groups=2
)

print(res)
assert "Welch t-test" in res["allowed_tests"]

res = decide_tests(
    measurement_scale="ordinal",
    independent=True,
    normal=False,
    homogeneous_variance=False,
    n_groups=2
)

assert "Mann–Whitney U" in res["allowed_tests"]

print("✓ Decision engine validated")
