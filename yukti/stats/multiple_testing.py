from statsmodels.stats.multitest import multipletests

SUPPORTED_METHODS = {
    "bonferroni": "bonferroni",
    "holm": "holm",
    "fdr_bh": "fdr_bh",
    "fdr_by": "fdr_by"
}

def adjust_pvalues(pvalues, method="fdr_bh", alpha=0.05):
    if method not in SUPPORTED_METHODS:
        raise ValueError(f"Unsupported correction method: {method}")

    reject, pvals_adj, _, _ = multipletests(
        pvalues,
        alpha=alpha,
        method=SUPPORTED_METHODS[method]
    )

    return {
        "method": method,
        "alpha": float(alpha),
        "raw_pvalues": [float(p) for p in pvalues],
        "adjusted_pvalues": [float(p) for p in pvals_adj],
        "reject_null": [bool(r.item()) for r in reject]
    }
