
import json
from pathlib import Path

def write_report(report, outdir="benchmark_reports"):
    Path(outdir).mkdir(exist_ok=True)
    fname = f"{report['name'].replace(' ','_')}.json"
    path = Path(outdir) / fname
    path.write_text(json.dumps(report, indent=2))
    return str(path)
