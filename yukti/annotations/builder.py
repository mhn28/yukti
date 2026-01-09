def build_p_annotation(p, alpha=0.05):
    """
    Build statistical significance annotation.
    Accepts:
      - float p-value
      - dict with key 'p'
    """
    if isinstance(p, dict):
        if "p" not in p:
            raise TypeError("Result dict must contain key 'p'")
        p = p["p"]

    if not isinstance(p, (int, float)):
        raise TypeError(f"Invalid p-value type: {type(p)}")

    if p < 0.001:
        stars = "***"
    elif p < 0.01:
        stars = "**"
    elif p < alpha:
        stars = "*"
    else:
        stars = "ns"

    return {
        "p": float(p),
        "alpha": float(alpha),
        "significance": stars
    }


def build_effect_annotation(effect, label=None):
    """
    Build effect-size annotation.
    Accepts:
      - numeric value
      - dict with explicit effect-size keys
    """
    if isinstance(effect, dict):
        for key in (
            "effect_size",
            "cohen_d",
            "hedges_g",
            "cliff_delta",
            "value","effect",
        ):
            if key in effect:
                effect = effect[key]
                label = label or key.replace("_", " ")
                break
        else:
            raise TypeError(
                "Effect dict must contain an explicit effect-size key "
                "(effect_size, cohen_d, hedges_g, cliff_delta)"
            )

    if not isinstance(effect, (int, float)):
        raise TypeError("Effect size must be numeric")

    return {
        "label": label or "effect size",
        "value": float(effect)
    }
