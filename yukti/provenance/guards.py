from yukti.provenance.binding import ProvenanceBinding

def enforce_provenance(binding: ProvenanceBinding) -> bool:
    if binding.dataset is None:
        raise RuntimeError("Dataset provenance missing")
    if binding.citation is None:
        raise RuntimeError("Citation missing")
    if not binding.analysis_name:
        raise RuntimeError("Analysis name missing")
    return True
