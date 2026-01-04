
from dataclasses import dataclass
from typing import Callable, Dict, Any

@dataclass
class BenchmarkCase:
    name: str
    paper_doi: str
    dataset_source: str
    expected: Dict[str, float]
    tolerance: Dict[str, float]
    runner: Callable[[], Dict[str, float]]
