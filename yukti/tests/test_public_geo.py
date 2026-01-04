
from yukti.public_datasets.geo import geo_search

res = geo_search("RNA-seq human cancer", retmax=1)
assert "esearchresult" in res
print("✓ Phase 21 GEO metadata access validated (no data downloaded)")
