
from enum import Enum

class VizIntent(str, Enum):
    ABUNDANCE = "abundance_landscape"
    DIFFERENTIAL = "differential_effect"
    TEMPORAL = "temporal_trajectory"
    CONCORDANCE = "cross_layer_concordance"
    NETWORK = "regulatory_network"

ALLOWED = {
    VizIntent.ABUNDANCE: {"numeric", "count"},
    VizIntent.DIFFERENTIAL: {"numeric"},
    VizIntent.TEMPORAL: {"numeric", "longitudinal"},
    VizIntent.CONCORDANCE: {"numeric"},
    VizIntent.NETWORK: {"graph"}
}

def validate_viz_intent(intent: VizIntent, data_type: str):
    if data_type not in ALLOWED[intent]:
        raise RuntimeError(
            f"Visualization intent '{intent}' incompatible with data type '{data_type}'"
        )
    return True
