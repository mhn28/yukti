import json, hashlib, platform, datetime, sys
from pathlib import Path

def file_hash(path):
    h = hashlib.sha256()
    with open(path,'rb') as f:
        for b in iter(lambda: f.read(8192), b''):
            h.update(b)
    return h.hexdigest()

def generate_manifest(inputs, config, outputs):
    return {
        "utc_timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "platform": platform.platform(),
        "python": sys.version,
        "yukti_version": "dev",
        "inputs": {str(p): file_hash(p) for p in inputs},
        "config": config,
        "outputs": outputs
    }

def write_manifest(manifest, out):
    Path(out).write_text(json.dumps(manifest, indent=2))
