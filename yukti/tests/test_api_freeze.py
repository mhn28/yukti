import json, importlib, inspect, hashlib
from yukti.api_lock.frozen_symbols import FROZEN_API

baseline = json.load(open("yukti/api_lock/api_fingerprint.json"))

for sym in FROZEN_API:
    mod, obj = sym.rsplit(".",1)
    m = importlib.import_module(mod)
    o = getattr(m, obj)
    src = inspect.getsource(o)
    h = hashlib.sha256(src.encode()).hexdigest()
    assert h == baseline[sym], f"API BREAK detected: {sym}"

print("✓ Phase J API freeze verified — rendering & annotation locked")
