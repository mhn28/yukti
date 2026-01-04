
import urllib.parse
import urllib.request
import json

GEO_SEARCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
GEO_SUMMARY = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"

def geo_search(query: str, retmax: int = 5):
    params = {
        "db": "gds",
        "term": query,
        "retmode": "json",
        "retmax": retmax
    }
    url = GEO_SEARCH + "?" + urllib.parse.urlencode(params)
    return json.loads(urllib.request.urlopen(url).read())

def geo_summary(gse_ids):
    params = {
        "db": "gds",
        "id": ",".join(gse_ids),
        "retmode": "json"
    }
    url = GEO_SUMMARY + "?" + urllib.parse.urlencode(params)
    return json.loads(urllib.request.urlopen(url).read())
