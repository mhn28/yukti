import importlib, inspect, json, hashlib
from yukti.api_lock.frozen_symbols import FROZEN_API

def snapshot():
    snap = {}
    for sym in sorted(FROZEN_API):
        mod, obj = sym.rsplit(".",1)
        m = importlib.import_module(mod)
        o = getattr(m, obj)
        src = inspect.getsource(o)
        snap[sym] = hashlib.sha256(src.encode()).hexdigest()
    return snap

if __name__ == "__main__":
    snap = snapshot()
    with open("yukti/api_lock/api_fingerprint.json","w") as f:
        json.dump(snap, f, indent=2)
    print("✓ API fingerprint generated")
