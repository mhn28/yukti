from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class DatasetProvenance:
    source: str
    accessions: List[str]
    organism: str
    assay: str
    description: str
    processed: bool = False

    def __post_init__(self):
        if not self.source:
            raise ValueError("Dataset source is required")
        if not self.accessions or not isinstance(self.accessions, list):
            raise ValueError("Accessions must be a non-empty list")
        if not self.organism:
            raise ValueError("Organism is required")
        if not self.assay:
            raise ValueError("Assay is required")
        if not self.description:
            raise ValueError("Dataset description is required")
