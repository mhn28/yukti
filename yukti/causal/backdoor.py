
import pandas as pd
import statsmodels.api as sm

class CausalError(RuntimeError):
    pass

def backdoor_adjustment(df, outcome, treatment, adjusters=None):
    if not adjusters or len(adjusters) == 0:
        raise CausalError(
            "Causal estimation blocked: no adjustment set declared"
        )

    X = df[[treatment] + adjusters]
    X = sm.add_constant(X)
    y = df[outcome]

    model = sm.OLS(y, X).fit()

    return {
        "treatment_effect": float(model.params[treatment]),
        "stderr": float(model.bse[treatment]),
        "p": float(model.pvalues[treatment]),
        "adjusters": adjusters,
        "n": int(df.shape[0])
    }
