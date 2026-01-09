import numpy as np
from yukti.spatial.vector.graph_laplacian import graph_laplacian

def gray_scott_graph(
    coords,
    u0,
    v0,
    Du=0.16,
    Dv=0.08,
    F=0.035,
    k=0.065,
    dt=0.01,
    steps=100,
    knn=25
):
    u = u0.copy()
    v = v0.copy()

    for _ in range(steps):
        Lu = graph_laplacian(coords, u, k=knn)["values"]
        Lv = graph_laplacian(coords, v, k=knn)["values"]

        uv2 = u * v * v
        u += dt * (Du * Lu - uv2 + F * (1 - u))
        v += dt * (Dv * Lv + uv2 - (F + k) * v)

    return u, v
