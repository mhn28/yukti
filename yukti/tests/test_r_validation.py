import numpy as np
from yukti.stats.tests_core import t_test
from yukti.validation.r_bridge import run_r
from yukti.validation.compare import compare

np.random.seed(123)
a = np.random.normal(0, 1, 30)
b = np.random.normal(0.6, 1, 30)

py = t_test(a, b)

out = run_r(
    "yukti/validation/r_scripts/welch_t_test.R",
    [",".join(map(str, a)), ",".join(map(str, b))]
)

r_stat, r_p = out.split(";")
r = {
    "stat": float(r_stat.split("=")[1]),
    "p": float(r_p.split("=")[1]),
}

cmp = compare(py, r)
print(cmp)
assert cmp["agree"]

print("✓ Python–R numerical agreement validated")
