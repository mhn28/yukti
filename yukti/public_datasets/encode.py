
import urllib.parse, urllib.request, json

BASE = "https://www.encodeproject.org/search/"

def encode_search(assay_term: str, organism: str = "human", limit: int = 5):
    params = {
        "type": "Experiment",
        "assay_title": assay_term,
        "limit": limit,
        "format": "json"
    }
    url = BASE + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(
        url,
        headers={
            "Accept": "application/json",
            "User-Agent": "Yukti/1.0 (metadata-only)"
        }
    )
    with urllib.request.urlopen(req) as r:
        data = r.read().decode("utf-8")
        if not data.strip().startswith("{"):
            raise RuntimeError("ENCODE did not return JSON")
        return json.loads(data)
