from dataclasses import dataclass
from typing import Optional

@dataclass
class SurvivalDeclaration:
    time_col: str
    event_col: str
    group_col: Optional[str] = None
    censoring_declared: bool = True
    time_origin_declared: bool = True
