def decide_tests(
    *,
    measurement_scale,
    independent,
    normal,
    homogeneous_variance,
    n_groups
):
    if measurement_scale not in {"ordinal", "interval", "ratio"}:
        raise ValueError("Statistical inference not valid for nominal data")

    if not independent:
        return {
            "allowed_tests": [],
            "reason": "Data are not independent; repeated-measures logic required"
        }

    if n_groups == 2:
        if normal and homogeneous_variance:
            return {
                "allowed_tests": ["Welch t-test"],
                "reason": "Normality and variance homogeneity satisfied"
            }
        else:
            return {
                "allowed_tests": ["Mann–Whitney U"],
                "reason": "Parametric assumptions violated"
            }

    if n_groups > 2:
        if normal and homogeneous_variance:
            return {
                "allowed_tests": ["One-way ANOVA"],
                "reason": "Parametric assumptions satisfied"
            }
        else:
            return {
                "allowed_tests": ["Kruskal–Wallis"],
                "reason": "Non-parametric alternative required"
            }

    return {"allowed_tests": [], "reason": "Insufficient information"}
