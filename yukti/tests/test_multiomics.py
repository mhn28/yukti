
from yukti.data.omics import OmicsDeclaration
from yukti.data.multiomics import MultiOmicsDeclaration

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

met = OmicsDeclaration(
    domain="metabolomics",
    assay="LC-MS",
    feature_unit="metabolite",
    dimensionality="medium",
    count_based=False,
    compositional=True,
    normalization_declared=False,
    batch_structure_declared=False
)

mo = MultiOmicsDeclaration(
    layers=[rna, met],
    integration_strategy="late",
    shared_samples_declared=True,
    alignment_declared=True,
    batch_harmonization_declared=False
)

assert mo.declared() is True
assert len(mo.layers) == 2

print("✓ Phase 16 multi-omics integration validated")
