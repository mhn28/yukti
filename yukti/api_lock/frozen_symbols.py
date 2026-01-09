"""
Phase J — API LOCK
Any modification to these symbols requires a MAJOR version bump.
"""

FROZEN_API = {
    # ---- annotations ----
    "yukti.annotations.builder.build_p_annotation",
    "yukti.annotations.builder.build_effect_annotation",

    # ---- plotting / rendering ----
    "yukti.plots.plot_2d.plot_2d_with_annotations",
    "yukti.figures.render.render_figure",

    # ---- captions & reporting ----
    "yukti.reporting.captions.generate_caption",

    # ---- provenance ----
    "yukti.provenance.dataset.DatasetProvenance",
    "yukti.provenance.citation.Citation",
    "yukti.provenance.binding.ProvenanceBinding",
    "yukti.provenance.guards.enforce_provenance",
}
