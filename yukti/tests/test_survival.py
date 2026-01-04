
import numpy as np
import pandas as pd
from yukti.stats.survival import kaplan_meier, cox_ph

np.random.seed(1)

n = 60
time = np.random.exponential(scale=10, size=n)
event = np.random.binomial(1, 0.7, size=n)
group = np.random.binomial(1, 0.5, size=n)

# Kaplan–Meier
km = kaplan_meier(time, event)
assert km["model"] == "Kaplan–Meier"
assert km["median_survival"] >= 0

# Cox PH
df = pd.DataFrame({
    "time": time,
    "event": event,
    "group": group
})

cox = cox_ph(df, duration_col="time", event_col="event")
assert cox["model"] == "Cox PH"
assert "group" in cox["hazard_ratios"]

print("✓ Phase 4 survival analysis validated")
