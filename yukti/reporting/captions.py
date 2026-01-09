def generate_caption(
    figure_id: str,
    title: str,
    panels: list,
    stats_summary: str,
    journal: str = "nature"
):
    """
    panels: list of dicts with keys:
        - label (A, B, C…)
        - description
    """

    journal = journal.lower()
    if journal not in {"nature","cell","science"}:
        raise ValueError("Unsupported journal style")

    panel_text = " ".join(
        f"({p['label']}) {p['description']}."
        for p in panels
    )

    if journal == "nature":
        caption = (
            f"{figure_id} | {title}. "
            f"{panel_text} "
            f"Statistical analysis: {stats_summary}."
        )

    elif journal == "cell":
        caption = (
            f"{figure_id}. {title}\n"
            f"{panel_text}\n"
            f"Statistics: {stats_summary}."
        )

    elif journal == "science":
        caption = (
            f"{figure_id}. {title}. "
            f"{panel_text} "
            f"{stats_summary}."
        )

    return caption
