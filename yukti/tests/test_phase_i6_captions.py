from yukti.reporting.captions import generate_caption

panels = [
    {"label": "A", "description": "Time-series signal"},
    {"label": "B", "description": "Frequency-domain transform"},
    {"label": "C", "description": "Group comparison"},
    {"label": "D", "description": "Spatial distribution"},
]

stats = "Two-sided Mann–Whitney U test with FDR correction"

cap_nature = generate_caption(
    figure_id="Figure 1",
    title="Multi-modal statistical summary",
    panels=panels,
    stats_summary=stats,
    journal="nature"
)

cap_cell = generate_caption(
    figure_id="Figure 1",
    title="Multi-modal statistical summary",
    panels=panels,
    stats_summary=stats,
    journal="cell"
)

cap_science = generate_caption(
    figure_id="Figure 1",
    title="Multi-modal statistical summary",
    panels=panels,
    stats_summary=stats,
    journal="science"
)

assert "Figure 1 |" in cap_nature
assert "\n" in cap_cell
assert cap_science.startswith("Figure 1.")

open("phase_i6_outputs/caption_nature.txt","w").write(cap_nature)
open("phase_i6_outputs/caption_cell.txt","w").write(cap_cell)
open("phase_i6_outputs/caption_science.txt","w").write(cap_science)

print("✓ Phase I.6 automatic journal-style captions validated")
