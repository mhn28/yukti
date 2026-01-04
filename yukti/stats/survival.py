
import pandas as pd
from lifelines import KaplanMeierFitter, CoxPHFitter

def kaplan_meier(time, event, label=None):
    kmf = KaplanMeierFitter()
    kmf.fit(time, event_observed=event, label=label)
    return {
        "model": "Kaplan–Meier",
        "survival_function": kmf.survival_function_.to_dict(),
        "median_survival": float(kmf.median_survival_time_)
    }

def cox_ph(data: pd.DataFrame, duration_col: str, event_col: str):
    cph = CoxPHFitter()
    cph.fit(data, duration_col=duration_col, event_col=event_col)
    return {
        "model": "Cox PH",
        "coefficients": cph.params_.to_dict(),
        "hazard_ratios": cph.hazard_ratios_.to_dict(),
        "pvalues": cph.summary["p"].to_dict(),
        "concordance": float(cph.concordance_index_)
    }
