import numpy as np
from yukti.stats.multiomics_factors import multiomics_factors

np.random.seed(42)
n = 40

latent = np.random.normal(0, 1, (n, 1))

rna = latent @ np.array([[2.0, -1.5]]) + np.random.normal(0, 0.5, (n, 2))
prot = latent @ np.array([[1.2,  0.8, -0.6]]) + np.random.normal(0, 0.5, (n, 3))
met = latent @ np.array([[0.9]]) + np.random.normal(0, 0.5, (n, 1))

res = multiomics_factors({
    "transcriptomics": rna,
    "proteomics": prot,
    "metabolomics": met
}, n_factors=1)

Z = res["latent_factors"]
corr = np.corrcoef(Z[:,0], latent[:,0])[0,1]

assert abs(corr) > 0.7
print("✓ Phase 8 multi-omics factor model validated")
