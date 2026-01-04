from dataclasses import dataclass
from typing import Optional, List

@dataclass(frozen=True)
class SpatiotemporalDeclaration:
    temporal_axis: Optional[str] = None
    spatial_axes: Optional[List[str]] = None
    coordinate_system: Optional[str] = None
    regular_sampling: Optional[bool] = None

    def declared(self) -> bool:
        return bool(self.temporal_axis or self.spatial_axes)
