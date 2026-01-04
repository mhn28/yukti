
from yukti.data.omics import OmicsDeclaration

od = OmicsDeclaration(
    domain="transcriptomics",
    assay="RNA-seq",
    feature_unit="gene",
    dimensionality="high",
    count_based=True,
    compositional=False,
    normalization_declared=False,
    batch_structure_declared=False
)

assert od.domain == "transcriptomics"
assert od.count_based is True
assert od.declared() is True

print("✓ Phase 15 OmicsDeclaration validated")
