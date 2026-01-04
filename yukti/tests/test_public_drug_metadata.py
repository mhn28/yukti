
from yukti.drug.public.chembl import chembl_target_search
from yukti.drug.public.pubchem import bioassay_search

# ChEMBL target metadata
c = chembl_target_search("EGFR", limit=1)
assert "targets" in c or "page_meta" in c

# PubChem BioAssay metadata
p = bioassay_search("kinase", limit=1)
assert isinstance(p, list)

print("✓ Phase 26B public drug-discovery metadata (ChEMBL + PubChem) validated")
