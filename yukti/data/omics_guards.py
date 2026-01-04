
from yukti.data.omics import OmicsDeclaration

class OmicsGuardError(RuntimeError):
    pass

def enforce_omics_assumptions(omics: OmicsDeclaration):
    if omics.domain == "transcriptomics":
        if not omics.count_based:
            raise OmicsGuardError("RNA-seq must be count-based")
        if not omics.normalization_declared:
            raise OmicsGuardError("RNA-seq normalization not declared")
    if omics.domain == "metagenomics":
        if not omics.compositional:
            raise OmicsGuardError("Metagenomics requires compositional handling")
    if omics.domain in {"proteomics", "metabolomics"}:
        if not omics.batch_structure_declared:
            raise OmicsGuardError("Batch structure must be declared for MS-based omics")
    return True
