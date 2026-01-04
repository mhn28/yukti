
from yukti.docs.cards.model_card import ModelCard
from yukti.docs.cards.data_card import DataCard
import datetime

mc = ModelCard(
    model_name="Yukti Statistical Engine",
    version="1.0",
    task="Hypothesis testing & estimation",
    intended_use="Exploratory and confirmatory statistical analysis",
    not_intended_use="Clinical or regulatory decision-making",
    algorithms=["Welch t-test","Mann–Whitney U","FDR correction"],
    assumptions=["Independence unless declared otherwise"],
    evaluation_metrics=["p-value","effect size","confidence interval"],
    uncertainty_handling="Explicit; no automatic inference",
    ethical_considerations="Human verification required",
    created_utc=datetime.datetime.utcnow().isoformat()
)

dc = DataCard(
    dataset_name="Example omics dataset",
    source="User-declared / public metadata",
    domain="Transcriptomics",
    modality="RNA-seq",
    sample_size="p >> n",
    feature_types=["counts","categorical metadata"],
    preprocessing_declared=False,
    missing_data_handling="User-declared only",
    leakage_controls=["duplicate","temporal","assay","target"],
    limitations="No normalization unless declared",
    created_utc=datetime.datetime.utcnow().isoformat()
)

assert "Model Card" in mc.to_markdown()
assert "Data Card" in dc.to_markdown()

print("✓ Phase 28 model card & data card validated")
