
import urllib.parse, urllib.request, json

ESEARCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
ESUMMARY = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"

def sra_search(term: str, retmax: int = 5):
    params = {"db":"sra","term":term,"retmode":"json","retmax":retmax}
    url = ESEARCH + "?" + urllib.parse.urlencode(params)
    return json.loads(urllib.request.urlopen(url).read())

def sra_summary(ids):
    params = {"db":"sra","id":",".join(ids),"retmode":"json"}
    url = ESUMMARY + "?" + urllib.parse.urlencode(params)
    return json.loads(urllib.request.urlopen(url).read())
