def methods(meta):
    """
    Generate journal-grade METHODS text from workflow metadata.
    """
    if not meta or "workflow" not in meta:
        raise ValueError("Workflow metadata required for METHODS generation")
    return " ".join(step.get("description","") for step in meta["workflow"])


def results(res):
    """
    Generate journal-grade RESULTS sentence from statistical output.
    """
    if not isinstance(res, dict):
        raise TypeError("Result must be a dictionary")
    parts = []
    if "stat" in res:
        parts.append(f"Statistic={res['stat']:.4g}")
    if "p" in res:
        parts.append(f"p={res['p']:.3e}")
    if "p_adj" in res:
        parts.append(f"adjusted p={res['p_adj']:.3e}")
    if "effect_size" in res:
        parts.append(f"effect size={res['effect_size']}")
    return ", ".join(parts)
