from yukti.reporting.methods import generate_methods
from yukti.reporting.results import generate_results
from yukti.reporting.figures import generate_figure_legend

workflow = [{"test": "Mann–Whitney U", "engine": "Yukti v1"}]
provenance = {"source": "GEO", "accessions": ["GSE00000"]}

methods = generate_methods(workflow, provenance)
assert "Data were obtained" in methods

results = generate_results({"statistic": 3.2, "p": 0.004, "effect_size": 0.82})
assert "p = 4.000e-03" in results

legend = generate_figure_legend(
    "Box plot",
    ["Control", "Treatment"],
    {"p": 0.004, "effect": "Cohen d = 0.82"}
)
assert "Box plot comparing" in legend

print("✓ Phase H automated METHODS / RESULTS / FIGURE LEGENDS validated")
