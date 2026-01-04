
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
import hashlib, json, os

@dataclass
class RawDataOptIn:
    dataset_source: str          # GEO / SRA / ENCODE / TCGA
    accession: str
    user_confirmed: bool
    storage_path: str
    checksum_algorithm: str = "sha256"
    timestamp_utc: str = datetime.now(timezone.utc).isoformat()

    def validate(self):
        if not self.user_confirmed:
            raise RuntimeError("Raw data access requires explicit user opt-in")
        Path(self.storage_path).mkdir(parents=True, exist_ok=True)
        return True

def checksum_file(path: str, algo: str = "sha256") -> str:
    h = hashlib.new(algo)
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def write_provenance(opt: RawDataOptIn, files: list[str], out_json: str):
    records = []
    for f in files:
        records.append({
            "file": os.path.basename(f),
            "checksum": checksum_file(f, opt.checksum_algorithm),
            "algorithm": opt.checksum_algorithm
        })
    payload = {
        "opt_in": asdict(opt),
        "files": records
    }
    with open(out_json, "w") as fh:
        json.dump(payload, fh, indent=2)
    return payload
