
from dataclasses import dataclass, asdict
from typing import List, Optional
import json

@dataclass
class DataCard:
    dataset_name: str
    source: str
    domain: str
    modality: str
    sample_size: str
    feature_types: List[str]
    preprocessing_declared: bool
    missing_data_handling: str
    leakage_controls: List[str]
    limitations: str
    created_utc: str

    def to_json(self):
        return json.dumps(asdict(self), indent=2)

    def to_markdown(self):
        d = asdict(self)
        md = [f"# Data Card: {self.dataset_name}\n"]
        for k,v in d.items():
            if k == "dataset_name": continue
            md.append(f"## {k.replace('_',' ').title()}\n{v}\n")
        return "\n".join(md)
