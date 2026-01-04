from dataclasses import dataclass
from typing import Optional

@dataclass
class DataSchema:
    name: str
    measurement_scale: str
    temporal: bool = False
    spatial: bool = False
    domain: Optional[str] = None
    description: Optional[str] = None

    def validate(self):
        valid_scales = {
            "nominal", "ordinal", "interval", "ratio",
            "temporal", "spatial", "spatiotemporal", "symbolic"
        }
        if self.measurement_scale not in valid_scales:
            raise ValueError(
                f"Unsupported measurement scale: {self.measurement_scale}"
            )

        if self.measurement_scale == "nominal":
            return "Nominal data: statistical inference not permitted"

        if self.temporal or self.spatial:
            return "Spatiotemporal data: inference requires explicit opt-in"

        return "Schema valid"
