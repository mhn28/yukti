def block_raw_counts(test, omics):
    if omics.get("count_based") and test in {"t_test", "anova"}:
        raise RuntimeError("Parametric test on raw counts blocked")

def block_correlation_compositional(data):
    if data.get("compositional"):
        raise RuntimeError("Correlation invalid for compositional data")
