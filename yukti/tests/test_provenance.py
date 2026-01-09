from yukti.provenance.dataset import DatasetProvenance
from yukti.provenance.citation import Citation
from yukti.provenance.binding import ProvenanceBinding
from yukti.provenance.guards import enforce_provenance

ds = DatasetProvenance(
    source="GEO",
    accessions=["GSE00000"],
    organism="Homo sapiens",
    assay="RNA-seq",
    description="Test RNA-seq dataset",
    processed=True
)

cite = Citation(
    title="Test study",
    authors="Doe et al.",
    journal="Journal of Testing",
    year=2024,
    pmid="12345678"
)

binding = ProvenanceBinding(
    dataset=ds,
    citation=cite,
    analysis_name="Differential expression"
)

assert enforce_provenance(binding) is True
print("✓ Phase G provenance binding validated")
