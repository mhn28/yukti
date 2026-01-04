
from yukti.data.omics import OmicsDeclaration
from yukti.data.omics_guards import enforce_omics_assumptions, OmicsGuardError

rna = OmicsDeclaration(
    domain="transcriptomics",
    assay="RNA-seq",
    feature_unit="gene",
    dimensionality="high",
    count_based=True,
    compositional=False,
    normalization_declared=False,
    batch_structure_declared=False
)

try:
    enforce_omics_assumptions(rna)
    raise AssertionError("Guard should have blocked undeclared normalization")
except OmicsGuardError:
    pass

print("✓ Phase 17 omics assumption guards validated")
