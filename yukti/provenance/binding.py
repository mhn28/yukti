from dataclasses import dataclass
from yukti.provenance.dataset import DatasetProvenance
from yukti.provenance.citation import Citation

@dataclass(frozen=True)
class ProvenanceBinding:
    dataset: DatasetProvenance
    citation: Citation
    analysis_name: str
