
from dataclasses import dataclass

@dataclass(frozen=True)
class OmicsDeclaration:
    domain: str                  # transcriptomics, genomics, metabolomics, etc.
    assay: str                   # RNA-seq, WGS, LC-MS, ATAC-seq
    feature_unit: str            # gene, transcript, peak, metabolite
    dimensionality: str          # low | medium | high (p >> n allowed)
    count_based: bool            # raw counts (RNA-seq)
    compositional: bool          # microbiome, metabolomics
    normalization_declared: bool # user explicitly declares normalization
    batch_structure_declared: bool

    def declared(self) -> bool:
        return True
