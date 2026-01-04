
from yukti.drug.declaration import DrugDiscoveryDeclaration

class DrugGuardError(RuntimeError):
    pass

def enforce_drug_assumptions(dd: DrugDiscoveryDeclaration):
    if dd.is_continuous_endpoint():
        if not dd.assay_normalization_declared:
            raise DrugGuardError(
                "Continuous pharmacology endpoints require explicit normalization declaration."
            )
        if dd.censoring_present and not dd.censoring_handling_declared:
            raise DrugGuardError(
                "Censored IC50/EC50 values require explicit censoring-handling declaration."
            )
    return True
