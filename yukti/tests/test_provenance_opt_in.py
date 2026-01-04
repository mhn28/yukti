
from yukti.provenance.opt_in import RawDataOptIn, write_provenance
from pathlib import Path
import tempfile

tmp = tempfile.mkdtemp()
dummy = Path(tmp) / "dummy.bin"
dummy.write_bytes(b"test")

opt = RawDataOptIn(
    dataset_source="GEO",
    accession="GSE000000",
    user_confirmed=True,
    storage_path=tmp
)

assert opt.validate() is True
prov = write_provenance(opt, [str(dummy)], str(Path(tmp)/"prov.json"))
assert "opt_in" in prov and len(prov["files"]) == 1

print("✓ Phase 24 raw-data opt-in + provenance validated")
