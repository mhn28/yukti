
from dataclasses import dataclass, asdict
from typing import List, Dict, Optional
import datetime, json

@dataclass
class ModelCard:
    model_name: str
    version: str
    task: str
    intended_use: str
    not_intended_use: str
    algorithms: List[str]
    assumptions: List[str]
    evaluation_metrics: List[str]
    uncertainty_handling: str
    ethical_considerations: str
    created_utc: str

    def to_json(self):
        return json.dumps(asdict(self), indent=2)

    def to_markdown(self):
        d = asdict(self)
        md = [f"# Model Card: {self.model_name} (v{self.version})\n"]
        for k,v in d.items():
            if k == "model_name" or k == "version": continue
            md.append(f"## {k.replace('_',' ').title()}\n{v}\n")
        return "\n".join(md)
