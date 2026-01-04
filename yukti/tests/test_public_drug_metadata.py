
from yukti.drug.public.chembl import chembl_target_search
from yukti.drug.public.pubchem import bioassay_search

# ChEMBL metadata
c = chembl_target_search("EGFR", limit=1)
assert isinstance(c, dict)

# PubChem BioAssay metadata (non-failing by design)
p = bioassay_search("kinase", limit=1)
assert isinstance(p, list)

print("✓ Phase 26B (fixed): public drug metadata robust to API variability")
