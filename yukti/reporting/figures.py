def generate_figure_legend(figure_type: str, groups: list, annotations: dict) -> str:
    legend = [f"{figure_type} comparing {', '.join(groups)}."]
    if "p" in annotations:
        legend.append(f"Statistical significance was assessed (p = {annotations['p']:.3e}).")
    if "effect" in annotations:
        legend.append(f"Effect size: {annotations['effect']}.")
    return " ".join(legend)
