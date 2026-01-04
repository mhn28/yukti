
import json, urllib.parse, urllib.request

BASE = "https://www.ebi.ac.uk/chembl/api/data"

def chembl_target_search(query: str, limit: int = 5):
    params = {"q": query, "limit": limit, "format": "json"}
    url = f"{BASE}/target/search.json?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(url, timeout=10) as r:
        return json.loads(r.read())

def chembl_assay_search(query: str, limit: int = 5):
    params = {"q": query, "limit": limit, "format": "json"}
    url = f"{BASE}/assay/search.json?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(url, timeout=10) as r:
        return json.loads(r.read())
