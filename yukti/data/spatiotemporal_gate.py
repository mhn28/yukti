from yukti.data.spatiotemporal_decl import SpatiotemporalDeclaration
from yukti.data.reasoning_modes import ReasoningMode

class SpatiotemporalGateError(RuntimeError):
    pass

def enforce_spatiotemporal_gate(
    decl: SpatiotemporalDeclaration,
    reasoning_mode: ReasoningMode | None
):
    # Case 1: No declaration → must NOT use spatiotemporal modes
    if not decl.declared():
        if reasoning_mode in {
            ReasoningMode.LONGITUDINAL,
            ReasoningMode.SPATIOTEMPORAL
        }:
            raise SpatiotemporalGateError(
                "Spatiotemporal reasoning selected without declaring spatiotemporal structure"
            )
        return True

    # Case 2: Declaration present → reasoning mode mandatory
    if reasoning_mode is None:
        raise SpatiotemporalGateError(
            "Spatiotemporal structure declared but no reasoning mode selected"
        )

    # Case 3: Incompatible modes blocked
    if reasoning_mode in {
        ReasoningMode.INDEPENDENT,
        ReasoningMode.REPEATED
    }:
        raise SpatiotemporalGateError(
            f"Reasoning mode '{reasoning_mode}' is incompatible with spatiotemporal data"
        )

    # Allowed: LONGITUDINAL, SPATIOTEMPORAL, CONSERVATIVE
    return True
