from enum import Enum

class ReasoningMode(str, Enum):
    INDEPENDENT = "independent"
    REPEATED = "repeated"
    LONGITUDINAL = "longitudinal"
    SPATIOTEMPORAL = "spatiotemporal"
    CONSERVATIVE = "conservative"
