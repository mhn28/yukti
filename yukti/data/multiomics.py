
from dataclasses import dataclass
from typing import List
from yukti.data.omics import OmicsDeclaration

@dataclass(frozen=True)
class MultiOmicsDeclaration:
    layers: List[OmicsDeclaration]
    integration_strategy: str     # early | late | hierarchical | joint
    shared_samples_declared: bool
    alignment_declared: bool      # time / subject / spatial alignment
    batch_harmonization_declared: bool

    def declared(self) -> bool:
        if len(self.layers) < 2:
            raise ValueError("Multi-omics requires at least two omics layers")
        return True
