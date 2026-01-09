import numpy as np
from yukti.spatial.vector.graph_laplacian import graph_laplacian

def reaction_diffusion(
    coords,
    u0,
    reaction,
    D=1.0,
    dt=0.01,
    steps=50,
    k=20
):
    """
    Graph-based reaction–diffusion solver.
    coords: (n, d)
    u0: initial scalar field
    reaction: callable R(u)
    """
    u = u0.astype(float).copy()

    for _ in range(steps):
        lap = graph_laplacian(coords, u, k=k)["values"]
        u = u + dt * (D * lap + reaction(u))

    return u
