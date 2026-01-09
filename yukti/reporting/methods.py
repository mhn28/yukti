def generate_methods(workflow: list, provenance: dict) -> str:
    lines = []
    lines.append("Data provenance and acquisition")
    lines.append(
        f"Data were obtained from {provenance['source']} "
        f"(accessions: {', '.join(provenance['accessions'])})."
    )
    lines.append("\nStatistical analysis")
    for step in workflow:
        lines.append(
            f"{step['test']} was performed using {step['engine']} "
            f"under explicitly declared assumptions."
        )
    return "\n".join(lines)
