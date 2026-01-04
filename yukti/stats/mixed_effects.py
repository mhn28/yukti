
import pandas as pd
import statsmodels.formula.api as smf

def linear_mixed_model(data: pd.DataFrame, formula: str, group: str):
    """
    Explicit linear mixed-effects model.
    Example formula: 'y ~ x1 + x2'
    group: random effect grouping variable
    """
    model = smf.mixedlm(formula, data, groups=data[group])
    result = model.fit()
    return {
        "model": "LMM",
        "formula": formula,
        "group": group,
        "params": result.params.to_dict(),
        "pvalues": result.pvalues.to_dict(),
        "aic": float(result.aic),
        "bic": float(result.bic)
    }
