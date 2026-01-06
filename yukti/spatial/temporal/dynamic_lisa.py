import numpy as np
from yukti.spatial.core import SpatialData
from yukti.spatial.lisa import local_moran
from yukti.spatial.temporal.schema import SpatioTemporalData

def dynamic_lisa(st: SpatioTemporalData, alpha=0.05):
    """
    Returns LISA clusters per timepoint
    """
    results = {}

    for t in st.unique_times():
        idx = np.where(st.time == t)[0]
        if len(idx) < 5:
            continue  # insufficient spatial support

        sd = SpatialData(
            coords=st.coords[idx],
            values=st.values[idx]
        )

        lisa = local_moran(sd.coords, sd.values, alpha=alpha)
        results[t] = lisa

    return results
