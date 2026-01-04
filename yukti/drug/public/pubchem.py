
import json, urllib.parse, urllib.request

BASE = "https://pubchem.ncbi.nlm.nih.gov/rest/pug"

def bioassay_search(term: str, limit: int = 5):
    url = f"{BASE}/assay/description/{urllib.parse.quote(term)}/JSON"
    with urllib.request.urlopen(url, timeout=10) as r:
        data = json.loads(r.read())
    return data.get("PC_AssayContainer", [])[:limit]
