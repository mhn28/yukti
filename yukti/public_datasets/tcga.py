
import urllib.request, json

GDC = "https://api.gdc.cancer.gov/projects"

def tcga_projects():
    req = urllib.request.Request(GDC, headers={"Accept":"application/json"})
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read().decode("utf-8"))
