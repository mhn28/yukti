import matplotlib.pyplot as plt

class StatisticalAnnotationError(RuntimeError):
    pass

def annotate_pairwise(
    ax,
    group_positions,
    comparisons,
    stats_results,
    y_offset=0.05,
    text_fmt="p = {p:.4g}",
    use_adjusted=True
):
    """
    group_positions: dict like {"A":0, "B":1, ...}
    comparisons: list of tuples [("A","B"), ("B","C")]
    stats_results: dict keyed by tuple with {"p","p_adj","test"}
    """
    ymax = max([p.get_height() for p in ax.patches])
    h = ymax * y_offset

    for i, (g1, g2) in enumerate(comparisons):
        key = (g1, g2)
        if key not in stats_results:
            raise StatisticalAnnotationError(
                f"No statistical result found for comparison {g1} vs {g2}"
            )

        res = stats_results[key]
        pval = res["p_adj"] if use_adjusted else res["p"]

        x1, x2 = group_positions[g1], group_positions[g2]
        y = ymax + h * (i + 1)

        ax.plot([x1, x1, x2, x2], [y, y+h, y+h, y], lw=1.5, c="black")
        ax.text(
            (x1 + x2) / 2,
            y + h,
            text_fmt.format(p=pval),
            ha="center",
            va="bottom",
            fontsize=10
        )
