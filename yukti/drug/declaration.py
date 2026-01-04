
from dataclasses import dataclass

@dataclass(frozen=True)
class DrugDiscoveryDeclaration:
    dataset_type: str            # ligand_based | target_based | phenotypic
    endpoint_type: str           # IC50 | EC50 | binary_hit | enrichment | other
    endpoint_units: str          # nM, uM, score, boolean, etc.
    censoring_present: bool
    censoring_handling_declared: bool
    assay_normalization_declared: bool
    species: str                 # human | mouse | other
    assay_aggregation_declared: bool
    in_vitro_vs_in_vivo: str     # in_vitro | in_vivo | both

    def declared(self) -> bool:
        return True

    def is_continuous_endpoint(self) -> bool:
        return self.endpoint_type in {"IC50","EC50","enrichment","other"}

    def requires_log_transform(self) -> bool:
        return self.endpoint_type in {"IC50","EC50"} and self.endpoint_units.lower() in {"nm","um","μm"}
