
from yukti.drug.declaration import DrugDiscoveryDeclaration
from yukti.drug.guards import enforce_drug_assumptions, DrugGuardError

# Block: IC50 without normalization
dd1 = DrugDiscoveryDeclaration(
    dataset_type="ligand_based",
    endpoint_type="IC50",
    endpoint_units="nM",
    censoring_present=False,
    censoring_handling_declared=False,
    assay_normalization_declared=False,
    species="human",
    assay_aggregation_declared=False,
    in_vitro_vs_in_vivo="in_vitro"
)

try:
    enforce_drug_assumptions(dd1)
    raise AssertionError("Guard should have blocked IC50 without normalization")
except DrugGuardError:
    pass

# Allow: IC50 with normalization + censoring handling
dd2 = DrugDiscoveryDeclaration(
    dataset_type="ligand_based",
    endpoint_type="IC50",
    endpoint_units="nM",
    censoring_present=True,
    censoring_handling_declared=True,
    assay_normalization_declared=True,
    species="human",
    assay_aggregation_declared=True,
    in_vitro_vs_in_vivo="in_vitro"
)

assert enforce_drug_assumptions(dd2) is True

print("✓ Phase 26A DrugDiscoveryDeclaration corrected & validated")
