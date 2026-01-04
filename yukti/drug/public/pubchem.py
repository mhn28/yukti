
import json, urllib.parse, urllib.request

BASE = "https://pubchem.ncbi.nlm.nih.gov/rest/pug"

def bioassay_search(term: str, limit: int = 5):
    """
    Metadata-only BioAssay lookup.
    Uses text-based AID search.
    Gracefully degrades on API changes.
    """
    try:
        url = f"{BASE}/assay/name/{urllib.parse.quote(term)}/aids/JSON"
        with urllib.request.urlopen(url, timeout=10) as r:
            data = json.loads(r.read())
        aids = data.get("IdentifierList", {}).get("AID", [])
        return aids[:limit]
    except Exception:
        return []  # strict non-failure by design
