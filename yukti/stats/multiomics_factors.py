import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def multiomics_factors(blocks: dict[str, np.ndarray], n_factors: int = 2):
    omics_names = list(blocks.keys())
    Xs = []

    for name in omics_names:
        Xs.append(StandardScaler().fit_transform(blocks[name]))

    X_concat = np.concatenate(Xs, axis=1)

    pca = PCA(n_components=n_factors, random_state=42)
    Z = pca.fit_transform(X_concat)

    loadings = {}
    start = 0
    for name, X in zip(omics_names, Xs):
        end = start + X.shape[1]
        loadings[name] = pca.components_[:, start:end]
        start = end

    return {
        "latent_factors": Z,
        "explained_variance": pca.explained_variance_ratio_.tolist(),
        "loadings": loadings
    }
