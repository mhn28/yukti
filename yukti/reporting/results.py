def generate_results(result: dict) -> str:
    stat = result.get("statistic")
    p = result.get("p")
    p_adj = result.get("p_adj")
    effect = result.get("effect_size")
    return (
        f"The analysis yielded a test statistic of {stat:.3g}, "
        f"with p = {p:.3e}"
        + (f" (adjusted p = {p_adj:.3e})" if p_adj is not None else "")
        + (f", corresponding to an effect size of {effect:.2f}." if effect is not None else ".")
    )
