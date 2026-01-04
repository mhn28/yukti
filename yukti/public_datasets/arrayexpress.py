
import urllib.parse, urllib.request, json

BASE = "https://www.ebi.ac.uk/arrayexpress/json/v3/experiments"

def ae_search(query: str, size: int = 5):
    url = BASE + "?" + urllib.parse.urlencode({"keywords": query, "pagesize": size})
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req) as r:
        data = r.read().decode("utf-8")
        if not data.strip().startswith("{"):
            raise RuntimeError("ArrayExpress did not return JSON (rate-limit or redirect)")
        return json.loads(data)
